# Repository Information
Name: Config-Mikrotik

# Directory Structure
Directory structure:
└── github_repos/Config-Mikrotik/
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
    │   │       ├── pack-9eb27bfd6cd63fab8fa46b02c772e34e76232e0c.idx
    │   │       └── pack-9eb27bfd6cd63fab8fa46b02c772e34e76232e0c.pack
    │   ├── packed-refs
    │   └── refs/
    │       ├── heads/
    │       │   └── main
    │       ├── remotes/
    │       │   └── origin/
    │       │       └── HEAD
    │       └── tags/
    ├── firewall/
    │   └── simple-firewall
    ├── firewall address-list/
    │   ├── facebook address-list
    │   ├── telkom address-list
    │   └── Twitter address-list
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
	url = https://github.com/kwattan/Config-Mikrotik.git
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
0000000000000000000000000000000000000000 316c2d72f1069e2e346dab34a446ef3e3ee61624 vivek-dodia <vivek.dodia@icloud.com> 1738606415 -0500	clone: from https://github.com/kwattan/Config-Mikrotik.git


File: /.git\logs\refs\heads\main
0000000000000000000000000000000000000000 316c2d72f1069e2e346dab34a446ef3e3ee61624 vivek-dodia <vivek.dodia@icloud.com> 1738606415 -0500	clone: from https://github.com/kwattan/Config-Mikrotik.git


File: /.git\logs\refs\remotes\origin\HEAD
0000000000000000000000000000000000000000 316c2d72f1069e2e346dab34a446ef3e3ee61624 vivek-dodia <vivek.dodia@icloud.com> 1738606415 -0500	clone: from https://github.com/kwattan/Config-Mikrotik.git


File: /.git\packed-refs
# pack-refs with: peeled fully-peeled sorted 
316c2d72f1069e2e346dab34a446ef3e3ee61624 refs/remotes/origin/main


File: /.git\refs\heads\main
316c2d72f1069e2e346dab34a446ef3e3ee61624


File: /.git\refs\remotes\origin\HEAD
ref: refs/remotes/origin/main


File: /firewall\simple-firewall
/ip firewall filter 
add chain=forward in-interface=Wan out-interface=Lan dst-address=192.168.0.0/16 action=accept comment="Allow semua akses internet to client" disabled=no
add chain=input in-interface=Wan protocol=tcp dst-port=8291 action=accept comment="Allow Remote winbox dari Publik" disabled=no
add chain=input in-interface=Wan protocol=udp src-port=123 action=accept comment="Allow NTP Traffic" disabled=no
add chain=input in-interface=Wan protocol=udp src-port=53 action=accept comment="Allow DNS Traffic" disabled=no
add chain=input in-interface=Wan protocol=icmp action=accept comment="Allow Ping Traceroute Traffic" disabled=no  
add chain=input in-interface=Wan connection-state=new action=add-src-to-address-list address-list=spam address-list-timeout=30m comment="Log Spam IP" disabled=no 
add chain=input in-interface=Wan action=drop comment="Drop Semua Akses yang tidak di ijinkan" disabled=no

/ip firewall raw
add chain=prerouting protocol=tcp dst-port=1433-1434,2745,2283,2535,2745,3127-3128,3410 action=drop
add chain=prerouting protocol=tcp dst-port=137,139,445,593,1024-1030,1080,1214,1363,1364,1368,1373,1377 action=drop
add chain=prerouting protocol=tcp dst-port=4444,5554,8866,9898,10000,10080,12345,17300,27374,65506 action=drop
add chain=prerouting protocol=udp dst-port=135-139,445,4444 action=drop
add chain=prerouting protocol=tcp dst-port=80,21,22,23,443,8728,8729 in-interface=Wan action=drop





File: /firewall address-list\facebook address-list
  
#AS32934
#https://bgp.he.net/AS32934
#https://www.dan.me.uk/bgplookup

/ip firewall address-list
add list="facebook" address=102.132.96.0/20
add list="facebook" address=103.4.96.0/22
add list="facebook" address=129.134.0.0/17
add list="facebook" address=129.134.25.0/24
add list="facebook" address=129.134.26.0/24
add list="facebook" address=129.134.27.0/24
add list="facebook" address=129.134.28.0/24
add list="facebook" address=129.134.29.0/24
add list="facebook" address=129.134.30.0/23
add list="facebook" address=129.134.30.0/24
add list="facebook" address=129.134.31.0/24
add list="facebook" address=129.134.64.0/24
add list="facebook" address=129.134.65.0/24
add list="facebook" address=129.134.66.0/24
add list="facebook" address=129.134.67.0/24
add list="facebook" address=129.134.68.0/24
add list="facebook" address=129.134.69.0/24
add list="facebook" address=157.240.0.0/17
add list="facebook" address=157.240.0.0/24
add list="facebook" address=157.240.1.0/24
add list="facebook" address=157.240.11.0/24
add list="facebook" address=157.240.13.0/24
add list="facebook" address=157.240.14.0/24
add list="facebook" address=157.240.18.0/24
add list="facebook" address=157.240.19.0/24
add list="facebook" address=157.240.192.0/18
add list="facebook" address=157.240.193.0/24
add list="facebook" address=157.240.194.0/24
add list="facebook" address=157.240.195.0/24
add list="facebook" address=157.240.196.0/24
add list="facebook" address=157.240.199.0/24
add list="facebook" address=157.240.2.0/24
add list="facebook" address=157.240.20.0/24
add list="facebook" address=157.240.200.0/24
add list="facebook" address=157.240.201.0/24
add list="facebook" address=157.240.205.0/24
add list="facebook" address=157.240.206.0/24
add list="facebook" address=157.240.207.0/24
add list="facebook" address=157.240.21.0/24
add list="facebook" address=157.240.210.0/24
add list="facebook" address=157.240.211.0/24
add list="facebook" address=157.240.217.0/24
add list="facebook" address=157.240.218.0/24
add list="facebook" address=157.240.22.0/24
add list="facebook" address=157.240.220.0/24
add list="facebook" address=157.240.221.0/24
add list="facebook" address=157.240.26.0/24
add list="facebook" address=157.240.27.0/24
add list="facebook" address=157.240.28.0/24
add list="facebook" address=157.240.3.0/24
add list="facebook" address=157.240.30.0/24
add list="facebook" address=157.240.7.0/24
add list="facebook" address=157.240.9.0/24
add list="facebook" address=173.252.64.0/19
add list="facebook" address=173.252.88.0/21
add list="facebook" address=173.252.96.0/19
add list="facebook" address=179.60.192.0/22
add list="facebook" address=179.60.192.0/24
add list="facebook" address=179.60.195.0/24
add list="facebook" address=185.60.216.0/22
add list="facebook" address=185.60.216.0/24
add list="facebook" address=185.60.217.0/24
add list="facebook" address=185.60.218.0/24
add list="facebook" address=185.89.218.0/23
add list="facebook" address=185.89.218.0/24
add list="facebook" address=185.89.219.0/24
add list="facebook" address=204.15.20.0/22
add list="facebook" address=31.13.24.0/21
add list="facebook" address=31.13.64.0/18
add list="facebook" address=31.13.64.0/19
add list="facebook" address=31.13.64.0/24
add list="facebook" address=31.13.65.0/24
add list="facebook" address=31.13.66.0/24
add list="facebook" address=31.13.67.0/24
add list="facebook" address=31.13.70.0/24
add list="facebook" address=31.13.71.0/24
add list="facebook" address=31.13.72.0/24
add list="facebook" address=31.13.73.0/24
add list="facebook" address=31.13.75.0/24
add list="facebook" address=31.13.77.0/24
add list="facebook" address=31.13.80.0/24
add list="facebook" address=31.13.81.0/24
add list="facebook" address=31.13.82.0/24
add list="facebook" address=31.13.83.0/24
add list="facebook" address=31.13.84.0/24
add list="facebook" address=31.13.86.0/24
add list="facebook" address=31.13.88.0/24
add list="facebook" address=31.13.89.0/24
add list="facebook" address=31.13.92.0/24
add list="facebook" address=31.13.93.0/24
add list="facebook" address=31.13.96.0/19
add list="facebook" address=45.64.40.0/22
add list="facebook" address=66.220.144.0/20
add list="facebook" address=66.220.144.0/21
add list="facebook" address=66.220.152.0/21
add list="facebook" address=69.171.224.0/19
add list="facebook" address=69.171.224.0/20
add list="facebook" address=69.171.240.0/20
add list="facebook" address=69.171.250.0/24
add list="facebook" address=69.63.176.0/20
add list="facebook" address=69.63.176.0/21
add list="facebook" address=74.119.76.0/22


File: /firewall address-list\telkom address-list
#AS7713
#https://bgp.he.net/AS7713
#https://www.dan.me.uk/bgplookup

/ip firewall address-list

add list="telkom" address=103.231.121.0/24
add list="telkom" address=103.245.120.0/24
add list="telkom" address=103.245.121.0/24
add list="telkom" address=104.111.0.0/19
add list="telkom" address=104.93.112.0/20
add list="telkom" address=104.93.198.0/23
add list="telkom" address=104.93.200.0/22
add list="telkom" address=104.93.208.0/20
add list="telkom" address=104.93.224.0/20
add list="telkom" address=104.93.84.0/22
add list="telkom" address=104.93.88.0/23
add list="telkom" address=104.93.96.0/20
add list="telkom" address=104.99.176.0/23
add list="telkom" address=104.99.178.0/23
add list="telkom" address=104.99.180.0/23
add list="telkom" address=104.99.182.0/23
add list="telkom" address=104.99.184.0/23
add list="telkom" address=104.99.186.0/23
add list="telkom" address=110.136.0.0/20
add list="telkom" address=110.136.104.0/22
add list="telkom" address=110.136.108.0/22
add list="telkom" address=110.136.112.0/22
add list="telkom" address=110.136.116.0/22
add list="telkom" address=110.136.120.0/21
add list="telkom" address=110.136.128.0/21
add list="telkom" address=110.136.136.0/21
add list="telkom" address=110.136.144.0/22
add list="telkom" address=110.136.148.0/23
add list="telkom" address=110.136.150.0/23
add list="telkom" address=110.136.152.0/22
add list="telkom" address=110.136.156.0/23
add list="telkom" address=110.136.158.0/23
add list="telkom" address=110.136.160.0/22
add list="telkom" address=110.136.164.0/23
add list="telkom" address=110.136.166.0/23
add list="telkom" address=110.136.168.0/23
add list="telkom" address=110.136.170.0/23
add list="telkom" address=110.136.172.0/22
add list="telkom" address=110.136.176.0/22
add list="telkom" address=110.136.18.0/23
add list="telkom" address=110.136.180.0/22
add list="telkom" address=110.136.184.0/22
add list="telkom" address=110.136.188.0/23
add list="telkom" address=110.136.190.0/23
add list="telkom" address=110.136.192.0/22
add list="telkom" address=110.136.196.0/22
add list="telkom" address=110.136.20.0/22
add list="telkom" address=110.136.200.0/22
add list="telkom" address=110.136.204.0/22
add list="telkom" address=110.136.208.0/21
add list="telkom" address=110.136.216.0/22
add list="telkom" address=110.136.220.0/22
add list="telkom" address=110.136.224.0/21
add list="telkom" address=110.136.234.0/23
add list="telkom" address=110.136.236.0/22
add list="telkom" address=110.136.24.0/22
add list="telkom" address=110.136.240.0/21
add list="telkom" address=110.136.248.0/22
add list="telkom" address=110.136.252.0/22
add list="telkom" address=110.136.28.0/22
add list="telkom" address=110.136.32.0/24
add list="telkom" address=110.136.33.0/24
add list="telkom" address=110.136.34.0/24
add list="telkom" address=110.136.36.0/24
add list="telkom" address=110.136.37.0/24
add list="telkom" address=110.136.38.0/24
add list="telkom" address=110.136.39.0/24
add list="telkom" address=110.136.40.0/21
add list="telkom" address=110.136.48.0/20
add list="telkom" address=110.136.65.0/24
add list="telkom" address=110.136.66.0/24
add list="telkom" address=110.136.67.0/24
add list="telkom" address=110.136.68.0/24
add list="telkom" address=110.136.69.0/24
add list="telkom" address=110.136.70.0/24
add list="telkom" address=110.136.71.0/24
add list="telkom" address=110.136.72.0/24
add list="telkom" address=110.136.73.0/24
add list="telkom" address=110.136.74.0/24
add list="telkom" address=110.136.75.0/24
add list="telkom" address=110.136.76.0/24
add list="telkom" address=110.136.77.0/24
add list="telkom" address=110.136.78.0/24
add list="telkom" address=110.136.79.0/24
add list="telkom" address=110.136.81.0/24
add list="telkom" address=110.136.82.0/24
add list="telkom" address=110.136.83.0/24
add list="telkom" address=110.136.86.0/24
add list="telkom" address=110.136.87.0/24
add list="telkom" address=110.136.89.0/24
add list="telkom" address=110.136.90.0/24
add list="telkom" address=110.136.91.0/24
add list="telkom" address=110.136.92.0/23
add list="telkom" address=110.136.95.0/24
add list="telkom" address=110.136.96.0/21
add list="telkom" address=110.137.0.0/22
add list="telkom" address=110.137.10.0/23
add list="telkom" address=110.137.100.0/22
add list="telkom" address=110.137.104.0/22
add list="telkom" address=110.137.108.0/22
add list="telkom" address=110.137.112.0/22
add list="telkom" address=110.137.116.0/23
add list="telkom" address=110.137.118.0/23
add list="telkom" address=110.137.12.0/23
add list="telkom" address=110.137.120.0/23
add list="telkom" address=110.137.122.0/23
add list="telkom" address=110.137.124.0/23
add list="telkom" address=110.137.126.0/23
add list="telkom" address=110.137.128.0/23
add list="telkom" address=110.137.130.0/23
add list="telkom" address=110.137.132.0/22
add list="telkom" address=110.137.136.0/23
add list="telkom" address=110.137.138.0/23
add list="telkom" address=110.137.14.0/23
add list="telkom" address=110.137.140.0/22
add list="telkom" address=110.137.144.0/21
add list="telkom" address=110.137.152.0/21
add list="telkom" address=110.137.16.0/22
add list="telkom" address=110.137.160.0/20
add list="telkom" address=110.137.180.0/22
add list="telkom" address=110.137.184.0/21
add list="telkom" address=110.137.192.0/20
add list="telkom" address=110.137.20.0/22
add list="telkom" address=110.137.208.0/21
add list="telkom" address=110.137.216.0/22
add list="telkom" address=110.137.220.0/22
add list="telkom" address=110.137.224.0/21
add list="telkom" address=110.137.232.0/21
add list="telkom" address=110.137.24.0/21
add list="telkom" address=110.137.240.0/22
add list="telkom" address=110.137.244.0/22
add list="telkom" address=110.137.248.0/21
add list="telkom" address=110.137.32.0/22
add list="telkom" address=110.137.36.0/24
add list="telkom" address=110.137.37.0/24
add list="telkom" address=110.137.38.0/24
add list="telkom" address=110.137.39.0/24
add list="telkom" address=110.137.4.0/22
add list="telkom" address=110.137.40.0/22
add list="telkom" address=110.137.44.0/23
add list="telkom" address=110.137.46.0/23
add list="telkom" address=110.137.48.0/23
add list="telkom" address=110.137.50.0/23
add list="telkom" address=110.137.52.0/22
add list="telkom" address=110.137.56.0/23
add list="telkom" address=110.137.58.0/23
add list="telkom" address=110.137.60.0/22
add list="telkom" address=110.137.64.0/22
add list="telkom" address=110.137.68.0/22
add list="telkom" address=110.137.72.0/24
add list="telkom" address=110.137.73.0/24
add list="telkom" address=110.137.74.0/24
add list="telkom" address=110.137.75.0/24
add list="telkom" address=110.137.76.0/23
add list="telkom" address=110.137.78.0/23
add list="telkom" address=110.137.8.0/24
add list="telkom" address=110.137.80.0/24
add list="telkom" address=110.137.81.0/24
add list="telkom" address=110.137.82.0/24
add list="telkom" address=110.137.83.0/24
add list="telkom" address=110.137.84.0/23
add list="telkom" address=110.137.86.0/24
add list="telkom" address=110.137.87.0/24
add list="telkom" address=110.137.88.0/23
add list="telkom" address=110.137.9.0/24
add list="telkom" address=110.137.90.0/23
add list="telkom" address=110.137.92.0/22
add list="telkom" address=110.137.96.0/23
add list="telkom" address=110.137.98.0/23
add list="telkom" address=110.138.0.0/21
add list="telkom" address=110.138.100.0/22
add list="telkom" address=110.138.104.0/21
add list="telkom" address=110.138.112.0/21
add list="telkom" address=110.138.120.0/23
add list="telkom" address=110.138.122.0/23
add list="telkom" address=110.138.124.0/23
add list="telkom" address=110.138.126.0/23
add list="telkom" address=110.138.128.0/21
add list="telkom" address=110.138.136.0/21
add list="telkom" address=110.138.144.0/22
add list="telkom" address=110.138.148.0/24
add list="telkom" address=110.138.149.0/24
add list="telkom" address=110.138.150.0/24
add list="telkom" address=110.138.151.0/24
add list="telkom" address=110.138.152.0/21
add list="telkom" address=110.138.16.0/22
add list="telkom" address=110.138.160.0/22
add list="telkom" address=110.138.164.0/22
add list="telkom" address=110.138.168.0/22
add list="telkom" address=110.138.172.0/23
add list="telkom" address=110.138.174.0/24
add list="telkom" address=110.138.175.0/24
add list="telkom" address=110.138.176.0/24
add list="telkom" address=110.138.177.0/24
add list="telkom" address=110.138.178.0/23
add list="telkom" address=110.138.180.0/23
add list="telkom" address=110.138.182.0/24
add list="telkom" address=110.138.183.0/24
add list="telkom" address=110.138.184.0/24
add list="telkom" address=110.138.185.0/24
add list="telkom" address=110.138.186.0/23
add list="telkom" address=110.138.188.0/22
add list="telkom" address=110.138.192.0/22
add list="telkom" address=110.138.196.0/22
add list="telkom" address=110.138.20.0/22
add list="telkom" address=110.138.200.0/23
add list="telkom" address=110.138.202.0/23
add list="telkom" address=110.138.204.0/23
add list="telkom" address=110.138.206.0/24
add list="telkom" address=110.138.207.0/24
add list="telkom" address=110.138.208.0/24
add list="telkom" address=110.138.209.0/24
add list="telkom" address=110.138.210.0/23
add list="telkom" address=110.138.212.0/23
add list="telkom" address=110.138.214.0/24
add list="telkom" address=110.138.215.0/24
add list="telkom" address=110.138.216.0/24
add list="telkom" address=110.138.217.0/24
add list="telkom" address=110.138.218.0/23
add list="telkom" address=110.138.220.0/22
add list="telkom" address=110.138.224.0/22
add list="telkom" address=110.138.228.0/22
add list="telkom" address=110.138.232.0/22
add list="telkom" address=110.138.236.0/23
add list="telkom" address=110.138.238.0/24
add list="telkom" address=110.138.24.0/22
add list="telkom" address=110.138.240.0/24
add list="telkom" address=110.138.241.0/24
add list="telkom" address=110.138.242.0/23
add list="telkom" address=110.138.244.0/23
add list="telkom" address=110.138.246.0/24
add list="telkom" address=110.138.247.0/24
add list="telkom" address=110.138.248.0/24
add list="telkom" address=110.138.249.0/24
add list="telkom" address=110.138.250.0/23
add list="telkom" address=110.138.252.0/22
add list="telkom" address=110.138.28.0/23
add list="telkom" address=110.138.30.0/23
add list="telkom" address=110.138.32.0/21
add list="telkom" address=110.138.40.0/21
add list="telkom" address=110.138.48.0/22
add list="telkom" address=110.138.52.0/22
add list="telkom" address=110.138.56.0/21
add list="telkom" address=110.138.64.0/21
add list="telkom" address=110.138.72.0/22
add list="telkom" address=110.138.76.0/22
add list="telkom" address=110.138.8.0/21
add list="telkom" address=110.138.80.0/20
add list="telkom" address=110.138.96.0/22
add list="telkom" address=110.139.0.0/24
add list="telkom" address=110.139.1.0/24
add list="telkom" address=110.139.10.0/23
add list="telkom" address=110.139.100.0/23
add list="telkom" address=110.139.102.0/23
add list="telkom" address=110.139.104.0/22
add list="telkom" address=110.139.108.0/22
add list="telkom" address=110.139.112.0/22
add list="telkom" address=110.139.116.0/23
add list="telkom" address=110.139.118.0/23
add list="telkom" address=110.139.12.0/24
add list="telkom" address=110.139.120.0/22
add list="telkom" address=110.139.124.0/23
add list="telkom" address=110.139.126.0/23
add list="telkom" address=110.139.128.0/22
add list="telkom" address=110.139.13.0/24
add list="telkom" address=110.139.132.0/23
add list="telkom" address=110.139.134.0/23
add list="telkom" address=110.139.136.0/22
add list="telkom" address=110.139.14.0/24
add list="telkom" address=110.139.140.0/23
add list="telkom" address=110.139.142.0/23
add list="telkom" address=110.139.144.0/22
add list="telkom" address=110.139.148.0/23
add list="telkom" address=110.139.15.0/24
add list="telkom" address=110.139.150.0/23
add list="telkom" address=110.139.152.0/22
add list="telkom" address=110.139.156.0/22
add list="telkom" address=110.139.16.0/22
add list="telkom" address=110.139.160.0/22
add list="telkom" address=110.139.164.0/23
add list="telkom" address=110.139.166.0/23
add list="telkom" address=110.139.168.0/22
add list="telkom" address=110.139.172.0/22
add list="telkom" address=110.139.176.0/22
add list="telkom" address=110.139.180.0/23
add list="telkom" address=110.139.182.0/23
add list="telkom" address=110.139.184.0/22
add list="telkom" address=110.139.188.0/22
add list="telkom" address=110.139.192.0/21
add list="telkom" address=110.139.2.0/24
add list="telkom" address=110.139.20.0/22
add list="telkom" address=110.139.200.0/22
add list="telkom" address=110.139.204.0/23
add list="telkom" address=110.139.206.0/23
add list="telkom" address=110.139.208.0/21
add list="telkom" address=110.139.218.0/24
add list="telkom" address=110.139.224.0/22
add list="telkom" address=110.139.228.0/23
add list="telkom" address=110.139.230.0/23
add list="telkom" address=110.139.232.0/23
add list="telkom" address=110.139.234.0/23
add list="telkom" address=110.139.236.0/22
add list="telkom" address=110.139.24.0/24
add list="telkom" address=110.139.240.0/23
add list="telkom" address=110.139.242.0/23
add list="telkom" address=110.139.244.0/23
add list="telkom" address=110.139.246.0/24
add list="telkom" address=110.139.247.0/24
add list="telkom" address=110.139.248.0/24
add list="telkom" address=110.139.249.0/24
add list="telkom" address=110.139.25.0/24
add list="telkom" address=110.139.252.0/22
add list="telkom" address=110.139.26.0/23
add list="telkom" address=110.139.28.0/23
add list="telkom" address=110.139.3.0/24
add list="telkom" address=110.139.30.0/23
add list="telkom" address=110.139.32.0/21
add list="telkom" address=110.139.4.0/22
add list="telkom" address=110.139.40.0/22
add list="telkom" address=110.139.44.0/23
add list="telkom" address=110.139.46.0/23
add list="telkom" address=110.139.48.0/24
add list="telkom" address=110.139.49.0/24
add list="telkom" address=110.139.50.0/24
add list="telkom" address=110.139.51.0/24
add list="telkom" address=110.139.52.0/22
add list="telkom" address=110.139.56.0/24
add list="telkom" address=110.139.57.0/24
add list="telkom" address=110.139.58.0/24
add list="telkom" address=110.139.59.0/24
add list="telkom" address=110.139.60.0/23
add list="telkom" address=110.139.62.0/24
add list="telkom" address=110.139.63.0/24
add list="telkom" address=110.139.64.0/22
add list="telkom" address=110.139.68.0/22
add list="telkom" address=110.139.72.0/21
add list="telkom" address=110.139.8.0/23
add list="telkom" address=110.139.80.0/24
add list="telkom" address=110.139.81.0/24
add list="telkom" address=110.139.82.0/23
add list="telkom" address=110.139.84.0/22
add list="telkom" address=110.139.88.0/21
add list="telkom" address=110.139.96.0/22
add list="telkom" address=118.96.0.0/22
add list="telkom" address=118.96.100.0/22
add list="telkom" address=118.96.104.0/22
add list="telkom" address=118.96.108.0/23
add list="telkom" address=118.96.110.0/23
add list="telkom" address=118.96.112.0/22
add list="telkom" address=118.96.116.0/22
add list="telkom" address=118.96.12.0/23
add list="telkom" address=118.96.120.0/22
add list="telkom" address=118.96.124.0/23
add list="telkom" address=118.96.126.0/23
add list="telkom" address=118.96.128.0/22
add list="telkom" address=118.96.132.0/22
add list="telkom" address=118.96.136.0/23
add list="telkom" address=118.96.138.0/23
add list="telkom" address=118.96.14.0/23
add list="telkom" address=118.96.140.0/23
add list="telkom" address=118.96.142.0/23
add list="telkom" address=118.96.144.0/22
add list="telkom" address=118.96.148.0/22
add list="telkom" address=118.96.152.0/23
add list="telkom" address=118.96.154.0/23
add list="telkom" address=118.96.156.0/22
add list="telkom" address=118.96.16.0/22
add list="telkom" address=118.96.160.0/21
add list="telkom" address=118.96.168.0/21
add list="telkom" address=118.96.176.0/21
add list="telkom" address=118.96.184.0/22
add list="telkom" address=118.96.188.0/22
add list="telkom" address=118.96.192.0/22
add list="telkom" address=118.96.196.0/22
add list="telkom" address=118.96.20.0/22
add list="telkom" address=118.96.200.0/22
add list="telkom" address=118.96.204.0/23
add list="telkom" address=118.96.206.0/23
add list="telkom" address=118.96.208.0/23
add list="telkom" address=118.96.210.0/23
add list="telkom" address=118.96.212.0/23
add list="telkom" address=118.96.214.0/23
add list="telkom" address=118.96.216.0/22
add list="telkom" address=118.96.220.0/22
add list="telkom" address=118.96.224.0/22
add list="telkom" address=118.96.228.0/22
add list="telkom" address=118.96.232.0/21
add list="telkom" address=118.96.24.0/22
add list="telkom" address=118.96.240.0/22
add list="telkom" address=118.96.244.0/22
add list="telkom" address=118.96.248.0/23
add list="telkom" address=118.96.250.0/23
add list="telkom" address=118.96.252.0/23
add list="telkom" address=118.96.255.0/24
add list="telkom" address=118.96.28.0/23
add list="telkom" address=118.96.30.0/23
add list="telkom" address=118.96.32.0/22
add list="telkom" address=118.96.36.0/22
add list="telkom" address=118.96.4.0/22
add list="telkom" address=118.96.40.0/22
add list="telkom" address=118.96.44.0/23
add list="telkom" address=118.96.46.0/23
add list="telkom" address=118.96.48.0/22
add list="telkom" address=118.96.52.0/22
add list="telkom" address=118.96.56.0/22
add list="telkom" address=118.96.60.0/23
add list="telkom" address=118.96.62.0/23
add list="telkom" address=118.96.64.0/22
add list="telkom" address=118.96.68.0/22
add list="telkom" address=118.96.72.0/22
add list="telkom" address=118.96.76.0/23
add list="telkom" address=118.96.78.0/23
add list="telkom" address=118.96.8.0/22
add list="telkom" address=118.96.80.0/22
add list="telkom" address=118.96.84.0/22
add list="telkom" address=118.96.88.0/22
add list="telkom" address=118.96.92.0/23
add list="telkom" address=118.96.94.0/23
add list="telkom" address=118.96.96.0/22
add list="telkom" address=118.97.192.0/24
add list="telkom" address=118.97.233.0/24
add list="telkom" address=118.97.242.0/24
add list="telkom" address=118.97.243.0/24
add list="telkom" address=118.97.244.0/24
add list="telkom" address=118.97.245.0/24
add list="telkom" address=118.97.246.0/24
add list="telkom" address=118.97.254.0/24
add list="telkom" address=118.97.49.0/24
add list="telkom" address=118.97.52.0/24
add list="telkom" address=118.98.104.0/21
add list="telkom" address=118.98.113.0/24
add list="telkom" address=118.98.115.0/24
add list="telkom" address=118.98.20.0/22
add list="telkom" address=118.98.26.0/24
add list="telkom" address=118.98.30.0/24
add list="telkom" address=118.98.32.0/24
add list="telkom" address=118.98.34.0/24
add list="telkom" address=118.98.36.0/24
add list="telkom" address=118.98.46.0/24
add list="telkom" address=118.98.64.0/22
add list="telkom" address=118.98.72.0/22
add list="telkom" address=118.98.76.0/22
add list="telkom" address=118.98.91.0/24
add list="telkom" address=118.98.92.0/22
add list="telkom" address=118.98.96.0/22
add list="telkom" address=125.160.112.0/22
add list="telkom" address=125.160.116.0/22
add list="telkom" address=125.160.12.0/23
add list="telkom" address=125.160.120.0/21
add list="telkom" address=125.160.128.0/21
add list="telkom" address=125.160.136.0/21
add list="telkom" address=125.160.144.0/21
add list="telkom" address=125.160.15.0/24
add list="telkom" address=125.160.152.0/22
add list="telkom" address=125.160.156.0/22
add list="telkom" address=125.160.16.0/24
add list="telkom" address=125.160.160.0/20
add list="telkom" address=125.160.176.0/21
add list="telkom" address=125.160.184.0/21
add list="telkom" address=125.160.19.0/24
add list="telkom" address=125.160.192.0/21
add list="telkom" address=125.160.20.0/23
add list="telkom" address=125.160.200.0/22
add list="telkom" address=125.160.204.0/23
add list="telkom" address=125.160.208.0/21
add list="telkom" address=125.160.216.0/22
add list="telkom" address=125.160.22.0/24
add list="telkom" address=125.160.220.0/23
add list="telkom" address=125.160.222.0/23
add list="telkom" address=125.160.224.0/20
add list="telkom" address=125.160.240.0/22
add list="telkom" address=125.160.244.0/22
add list="telkom" address=125.160.248.0/22
add list="telkom" address=125.160.252.0/23
add list="telkom" address=125.160.254.0/24
add list="telkom" address=125.160.255.0/24
add list="telkom" address=125.160.32.0/22
add list="telkom" address=125.160.36.0/23
add list="telkom" address=125.160.38.0/23
add list="telkom" address=125.160.40.0/22
add list="telkom" address=125.160.44.0/24
add list="telkom" address=125.160.45.0/24
add list="telkom" address=125.160.46.0/24
add list="telkom" address=125.160.47.0/24
add list="telkom" address=125.160.48.0/21
add list="telkom" address=125.160.5.0/24
add list="telkom" address=125.160.56.0/22
add list="telkom" address=125.160.60.0/24
add list="telkom" address=125.160.61.0/24
add list="telkom" address=125.160.62.0/24
add list="telkom" address=125.160.63.0/24
add list="telkom" address=125.160.64.0/22
add list="telkom" address=125.160.68.0/23
add list="telkom" address=125.160.70.0/23
add list="telkom" address=125.160.72.0/22
add list="telkom" address=125.160.76.0/24
add list="telkom" address=125.160.77.0/24
add list="telkom" address=125.160.78.0/24
add list="telkom" address=125.160.8.0/24
add list="telkom" address=125.160.80.0/22
add list="telkom" address=125.160.84.0/22
add list="telkom" address=125.160.88.0/22
add list="telkom" address=125.160.92.0/24
add list="telkom" address=125.160.93.0/24
add list="telkom" address=125.160.94.0/24
add list="telkom" address=125.160.95.0/24
add list="telkom" address=125.160.96.0/20
add list="telkom" address=125.161.0.0/22
add list="telkom" address=125.161.108.0/23
add list="telkom" address=125.161.110.0/23
add list="telkom" address=125.161.112.0/23
add list="telkom" address=125.161.114.0/23
add list="telkom" address=125.161.116.0/23
add list="telkom" address=125.161.118.0/23
add list="telkom" address=125.161.12.0/22
add list="telkom" address=125.161.120.0/23
add list="telkom" address=125.161.122.0/23
add list="telkom" address=125.161.124.0/23
add list="telkom" address=125.161.126.0/23
add list="telkom" address=125.161.128.0/24
add list="telkom" address=125.161.129.0/24
add list="telkom" address=125.161.130.0/24
add list="telkom" address=125.161.131.0/24
add list="telkom" address=125.161.132.0/24
add list="telkom" address=125.161.133.0/24
add list="telkom" address=125.161.134.0/23
add list="telkom" address=125.161.136.0/22
add list="telkom" address=125.161.140.0/22
add list="telkom" address=125.161.144.0/24
add list="telkom" address=125.161.145.0/24
add list="telkom" address=125.161.146.0/24
add list="telkom" address=125.161.147.0/24
add list="telkom" address=125.161.148.0/22
add list="telkom" address=125.161.152.0/22
add list="telkom" address=125.161.156.0/22
add list="telkom" address=125.161.16.0/23
add list="telkom" address=125.161.160.0/19
add list="telkom" address=125.161.18.0/23
add list="telkom" address=125.161.192.0/20
add list="telkom" address=125.161.20.0/22
add list="telkom" address=125.161.224.0/21
add list="telkom" address=125.161.232.0/21
add list="telkom" address=125.161.24.0/21
add list="telkom" address=125.161.240.0/21
add list="telkom" address=125.161.248.0/21
add list="telkom" address=125.161.32.0/22
add list="telkom" address=125.161.36.0/22
add list="telkom" address=125.161.4.0/23
add list="telkom" address=125.161.40.0/23
add list="telkom" address=125.161.42.0/23
add list="telkom" address=125.161.44.0/22
add list="telkom" address=125.161.48.0/21
add list="telkom" address=125.161.56.0/21
add list="telkom" address=125.161.6.0/23
add list="telkom" address=125.161.64.0/21
add list="telkom" address=125.161.72.0/21
add list="telkom" address=125.161.8.0/22
add list="telkom" address=125.161.80.0/23
add list="telkom" address=125.161.82.0/23
add list="telkom" address=125.161.84.0/22
add list="telkom" address=125.161.88.0/23
add list="telkom" address=125.161.90.0/23
add list="telkom" address=125.161.92.0/23
add list="telkom" address=125.161.94.0/23
add list="telkom" address=125.161.96.0/21
add list="telkom" address=125.162.0.0/21
add list="telkom" address=125.162.112.0/22
add list="telkom" address=125.162.116.0/22
add list="telkom" address=125.162.120.0/22
add list="telkom" address=125.162.124.0/23
add list="telkom" address=125.162.126.0/23
add list="telkom" address=125.162.128.0/21
add list="telkom" address=125.162.136.0/21
add list="telkom" address=125.162.144.0/21
add list="telkom" address=125.162.152.0/21
add list="telkom" address=125.162.16.0/21
add list="telkom" address=125.162.160.0/23
add list="telkom" address=125.162.162.0/23
add list="telkom" address=125.162.164.0/22
add list="telkom" address=125.162.168.0/23
add list="telkom" address=125.162.170.0/23
add list="telkom" address=125.162.172.0/22
add list="telkom" address=125.162.176.0/22
add list="telkom" address=125.162.180.0/23
add list="telkom" address=125.162.182.0/24
add list="telkom" address=125.162.183.0/24
add list="telkom" address=125.162.184.0/23
add list="telkom" address=125.162.186.0/23
add list="telkom" address=125.162.192.0/23
add list="telkom" address=125.162.194.0/23
add list="telkom" address=125.162.196.0/23
add list="telkom" address=125.162.198.0/23
add list="telkom" address=125.162.200.0/21
add list="telkom" address=125.162.208.0/21
add list="telkom" address=125.162.216.0/22
add list="telkom" address=125.162.220.0/22
add list="telkom" address=125.162.224.0/22
add list="telkom" address=125.162.228.0/23
add list="telkom" address=125.162.230.0/23
add list="telkom" address=125.162.232.0/21
add list="telkom" address=125.162.24.0/21
add list="telkom" address=125.162.240.0/23
add list="telkom" address=125.162.242.0/23
add list="telkom" address=125.162.244.0/22
add list="telkom" address=125.162.248.0/24
add list="telkom" address=125.162.250.0/23
add list="telkom" address=125.162.252.0/23
add list="telkom" address=125.162.254.0/24
add list="telkom" address=125.162.255.0/24
add list="telkom" address=125.162.32.0/23
add list="telkom" address=125.162.34.0/23
add list="telkom" address=125.162.36.0/23
add list="telkom" address=125.162.38.0/23
add list="telkom" address=125.162.40.0/23
add list="telkom" address=125.162.42.0/23
add list="telkom" address=125.162.44.0/23
add list="telkom" address=125.162.46.0/23
add list="telkom" address=125.162.48.0/23
add list="telkom" address=125.162.50.0/23
add list="telkom" address=125.162.52.0/24
add list="telkom" address=125.162.53.0/24
add list="telkom" address=125.162.54.0/23
add list="telkom" address=125.162.56.0/21
add list="telkom" address=125.162.64.0/22
add list="telkom" address=125.162.68.0/23
add list="telkom" address=125.162.70.0/23
add list="telkom" address=125.162.72.0/22
add list="telkom" address=125.162.76.0/22
add list="telkom" address=125.162.8.0/21
add list="telkom" address=125.162.80.0/23
add list="telkom" address=125.162.82.0/23
add list="telkom" address=125.162.84.0/22
add list="telkom" address=125.162.88.0/22
add list="telkom" address=125.162.92.0/22
add list="telkom" address=125.162.96.0/20
add list="telkom" address=125.163.0.0/19
add list="telkom" address=125.163.104.0/21
add list="telkom" address=125.163.112.0/22
add list="telkom" address=125.163.116.0/22
add list="telkom" address=125.163.120.0/22
add list="telkom" address=125.163.124.0/22
add list="telkom" address=125.163.128.0/21
add list="telkom" address=125.163.136.0/21
add list="telkom" address=125.163.144.0/20
add list="telkom" address=125.163.160.0/22
add list="telkom" address=125.163.164.0/22
add list="telkom" address=125.163.168.0/22
add list="telkom" address=125.163.172.0/22
add list="telkom" address=125.163.176.0/21
add list="telkom" address=125.163.184.0/21
add list="telkom" address=125.163.192.0/21
add list="telkom" address=125.163.200.0/21
add list="telkom" address=125.163.208.0/21
add list="telkom" address=125.163.216.0/23
add list="telkom" address=125.163.218.0/24
add list="telkom" address=125.163.220.0/22
add list="telkom" address=125.163.224.0/22
add list="telkom" address=125.163.228.0/22
add list="telkom" address=125.163.232.0/22
add list="telkom" address=125.163.236.0/22
add list="telkom" address=125.163.240.0/22
add list="telkom" address=125.163.244.0/22
add list="telkom" address=125.163.248.0/22
add list="telkom" address=125.163.252.0/23
add list="telkom" address=125.163.254.0/24
add list="telkom" address=125.163.255.0/24
add list="telkom" address=125.163.32.0/20
add list="telkom" address=125.163.48.0/22
add list="telkom" address=125.163.52.0/22
add list="telkom" address=125.163.56.0/21
add list="telkom" address=125.163.64.0/21
add list="telkom" address=125.163.72.0/21
add list="telkom" address=125.163.80.0/22
add list="telkom" address=125.163.84.0/22
add list="telkom" address=125.163.88.0/21
add list="telkom" address=125.163.96.0/21
add list="telkom" address=125.164.0.0/20
add list="telkom" address=125.164.112.0/21
add list="telkom" address=125.164.120.0/22
add list="telkom" address=125.164.124.0/24
add list="telkom" address=125.164.125.0/24
add list="telkom" address=125.164.126.0/24
add list="telkom" address=125.164.127.0/24
add list="telkom" address=125.164.128.0/20
add list="telkom" address=125.164.144.0/20
add list="telkom" address=125.164.16.0/20
add list="telkom" address=125.164.160.0/20
add list="telkom" address=125.164.176.0/20
add list="telkom" address=125.164.192.0/20
add list="telkom" address=125.164.208.0/21
add list="telkom" address=125.164.216.0/23
add list="telkom" address=125.164.218.0/23
add list="telkom" address=125.164.220.0/23
add list="telkom" address=125.164.222.0/23
add list="telkom" address=125.164.224.0/21
add list="telkom" address=125.164.232.0/24
add list="telkom" address=125.164.233.0/24
add list="telkom" address=125.164.234.0/24
add list="telkom" address=125.164.235.0/24
add list="telkom" address=125.164.236.0/24
add list="telkom" address=125.164.237.0/24
add list="telkom" address=125.164.238.0/24
add list="telkom" address=125.164.239.0/24
add list="telkom" address=125.164.240.0/21
add list="telkom" address=125.164.248.0/23
add list="telkom" address=125.164.250.0/23
add list="telkom" address=125.164.252.0/24
add list="telkom" address=125.164.253.0/24
add list="telkom" address=125.164.254.0/24
add list="telkom" address=125.164.255.0/24
add list="telkom" address=125.164.32.0/20
add list="telkom" address=125.164.48.0/20
add list="telkom" address=125.164.64.0/21
add list="telkom" address=125.164.72.0/21
add list="telkom" address=125.164.80.0/21
add list="telkom" address=125.164.88.0/22
add list="telkom" address=125.164.92.0/23
add list="telkom" address=125.164.94.0/23
add list="telkom" address=125.164.96.0/20
add list="telkom" address=125.165.0.0/21
add list="telkom" address=125.165.104.0/21
add list="telkom" address=125.165.112.0/21
add list="telkom" address=125.165.112.0/24
add list="telkom" address=125.165.113.0/24
add list="telkom" address=125.165.114.0/24
add list="telkom" address=125.165.115.0/24
add list="telkom" address=125.165.116.0/22
add list="telkom" address=125.165.12.0/23
add list="telkom" address=125.165.120.0/23
add list="telkom" address=125.165.122.0/23
add list="telkom" address=125.165.124.0/23
add list="telkom" address=125.165.126.0/23
add list="telkom" address=125.165.128.0/21
add list="telkom" address=125.165.136.0/21
add list="telkom" address=125.165.14.0/24
add list="telkom" address=125.165.144.0/21
add list="telkom" address=125.165.15.0/24
add list="telkom" address=125.165.152.0/22
add list="telkom" address=125.165.156.0/22
add list="telkom" address=125.165.16.0/21
add list="telkom" address=125.165.160.0/22
add list="telkom" address=125.165.164.0/23
add list="telkom" address=125.165.166.0/23
add list="telkom" address=125.165.168.0/21
add list="telkom" address=125.165.176.0/21
add list="telkom" address=125.165.184.0/23
add list="telkom" address=125.165.186.0/23
add list="telkom" address=125.165.188.0/22
add list="telkom" address=125.165.192.0/18
add list="telkom" address=125.165.24.0/21
add list="telkom" address=125.165.32.0/22
add list="telkom" address=125.165.36.0/22
add list="telkom" address=125.165.40.0/22
add list="telkom" address=125.165.44.0/22
add list="telkom" address=125.165.48.0/22
add list="telkom" address=125.165.52.0/22
add list="telkom" address=125.165.56.0/22
add list="telkom" address=125.165.60.0/24
add list="telkom" address=125.165.63.0/24
add list="telkom" address=125.165.64.0/21
add list="telkom" address=125.165.72.0/21
add list="telkom" address=125.165.8.0/22
add list="telkom" address=125.165.80.0/21
add list="telkom" address=125.165.88.0/21
add list="telkom" address=125.165.96.0/21
add list="telkom" address=125.166.0.0/24
add list="telkom" address=125.166.1.0/24
add list="telkom" address=125.166.100.0/23
add list="telkom" address=125.166.102.0/23
add list="telkom" address=125.166.104.0/21
add list="telkom" address=125.166.112.0/23
add list="telkom" address=125.166.114.0/23
add list="telkom" address=125.166.116.0/22
add list="telkom" address=125.166.120.0/21
add list="telkom" address=125.166.128.0/20
add list="telkom" address=125.166.144.0/22
add list="telkom" address=125.166.148.0/22
add list="telkom" address=125.166.152.0/22
add list="telkom" address=125.166.156.0/22
add list="telkom" address=125.166.16.0/22
add list="telkom" address=125.166.160.0/19
add list="telkom" address=125.166.192.0/21
add list="telkom" address=125.166.2.0/24
add list="telkom" address=125.166.20.0/23
add list="telkom" address=125.166.200.0/21
add list="telkom" address=125.166.208.0/21
add list="telkom" address=125.166.216.0/22
add list="telkom" address=125.166.22.0/23
add list="telkom" address=125.166.220.0/23
add list="telkom" address=125.166.222.0/24
add list="telkom" address=125.166.223.0/24
add list="telkom" address=125.166.224.0/20
add list="telkom" address=125.166.24.0/23
add list="telkom" address=125.166.240.0/20
add list="telkom" address=125.166.26.0/23
add list="telkom" address=125.166.28.0/23
add list="telkom" address=125.166.3.0/24
add list="telkom" address=125.166.30.0/23
add list="telkom" address=125.166.32.0/23
add list="telkom" address=125.166.34.0/23
add list="telkom" address=125.166.36.0/22
add list="telkom" address=125.166.4.0/24
add list="telkom" address=125.166.40.0/22
add list="telkom" address=125.166.44.0/22
add list="telkom" address=125.166.48.0/22
add list="telkom" address=125.166.5.0/24
add list="telkom" address=125.166.52.0/22
add list="telkom" address=125.166.56.0/23
add list="telkom" address=125.166.59.0/24
add list="telkom" address=125.166.6.0/24
add list="telkom" address=125.166.60.0/24
add list="telkom" address=125.166.61.0/24
add list="telkom" address=125.166.62.0/23
add list="telkom" address=125.166.64.0/21
add list="telkom" address=125.166.7.0/24
add list="telkom" address=125.166.72.0/21
add list="telkom" address=125.166.8.0/21
add list="telkom" address=125.166.80.0/22
add list="telkom" address=125.166.84.0/23
add list="telkom" address=125.166.86.0/23
add list="telkom" address=125.166.88.0/21
add list="telkom" address=125.166.96.0/22
add list="telkom" address=125.167.0.0/23
add list="telkom" address=125.167.10.0/24
add list="telkom" address=125.167.104.0/23
add list="telkom" address=125.167.106.0/23
add list="telkom" address=125.167.108.0/23
add list="telkom" address=125.167.11.0/24
add list="telkom" address=125.167.110.0/23
add list="telkom" address=125.167.112.0/21
add list="telkom" address=125.167.12.0/24
add list="telkom" address=125.167.120.0/23
add list="telkom" address=125.167.122.0/23
add list="telkom" address=125.167.124.0/22
add list="telkom" address=125.167.128.0/21
add list="telkom" address=125.167.13.0/24
add list="telkom" address=125.167.136.0/23
add list="telkom" address=125.167.138.0/23
add list="telkom" address=125.167.14.0/23
add list="telkom" address=125.167.140.0/23
add list="telkom" address=125.167.142.0/24
add list="telkom" address=125.167.143.0/24
add list="telkom" address=125.167.144.0/22
add list="telkom" address=125.167.148.0/23
add list="telkom" address=125.167.150.0/24
add list="telkom" address=125.167.151.0/24
add list="telkom" address=125.167.152.0/22
add list="telkom" address=125.167.156.0/23
add list="telkom" address=125.167.158.0/23
add list="telkom" address=125.167.16.0/21
add list="telkom" address=125.167.166.0/24
add list="telkom" address=125.167.167.0/24
add list="telkom" address=125.167.168.0/24
add list="telkom" address=125.167.169.0/24
add list="telkom" address=125.167.170.0/24
add list="telkom" address=125.167.171.0/24
add list="telkom" address=125.167.172.0/24
add list="telkom" address=125.167.174.0/24
add list="telkom" address=125.167.175.0/24
add list="telkom" address=125.167.176.0/23
add list="telkom" address=125.167.178.0/23
add list="telkom" address=125.167.180.0/22
add list="telkom" address=125.167.184.0/22
add list="telkom" address=125.167.188.0/24
add list="telkom" address=125.167.189.0/24
add list="telkom" address=125.167.190.0/23
add list="telkom" address=125.167.192.0/23
add list="telkom" address=125.167.194.0/23
add list="telkom" address=125.167.196.0/23
add list="telkom" address=125.167.198.0/23
add list="telkom" address=125.167.2.0/23
add list="telkom" address=125.167.200.0/22
add list="telkom" address=125.167.204.0/23
add list="telkom" address=125.167.206.0/23
add list="telkom" address=125.167.208.0/21
add list="telkom" address=125.167.216.0/24
add list="telkom" address=125.167.217.0/24
add list="telkom" address=125.167.219.0/24
add list="telkom" address=125.167.220.0/23
add list="telkom" address=125.167.222.0/23
add list="telkom" address=125.167.224.0/22
add list="telkom" address=125.167.228.0/22
add list="telkom" address=125.167.232.0/22
add list="telkom" address=125.167.236.0/23
add list="telkom" address=125.167.238.0/23
add list="telkom" address=125.167.24.0/23
add list="telkom" address=125.167.240.0/21
add list="telkom" address=125.167.248.0/23
add list="telkom" address=125.167.250.0/23
add list="telkom" address=125.167.252.0/23
add list="telkom" address=125.167.254.0/23
add list="telkom" address=125.167.26.0/23
add list="telkom" address=125.167.28.0/23
add list="telkom" address=125.167.30.0/23
add list="telkom" address=125.167.32.0/22
add list="telkom" address=125.167.36.0/22
add list="telkom" address=125.167.4.0/22
add list="telkom" address=125.167.40.0/21
add list="telkom" address=125.167.48.0/21
add list="telkom" address=125.167.56.0/21
add list="telkom" address=125.167.64.0/22
add list="telkom" address=125.167.68.0/22
add list="telkom" address=125.167.72.0/21
add list="telkom" address=125.167.8.0/23
add list="telkom" address=125.167.80.0/21
add list="telkom" address=125.167.88.0/21
add list="telkom" address=125.167.96.0/21
add list="telkom" address=150.129.160.0/24
add list="telkom" address=150.129.161.0/24
add list="telkom" address=154.195.4.0/24
add list="telkom" address=154.195.5.0/24
add list="telkom" address=156.233.24.0/23
add list="telkom" address=180.240.128.0/17
add list="telkom" address=180.240.128.0/24
add list="telkom" address=180.240.131.0/24
add list="telkom" address=180.240.135.0/24
add list="telkom" address=180.240.136.0/24
add list="telkom" address=180.240.144.0/24
add list="telkom" address=180.240.177.0/24
add list="telkom" address=180.240.178.0/24
add list="telkom" address=180.240.179.0/24
add list="telkom" address=180.240.180.0/24
add list="telkom" address=180.240.181.0/24
add list="telkom" address=180.240.184.0/24
add list="telkom" address=180.240.185.0/24
add list="telkom" address=180.240.190.0/24
add list="telkom" address=180.240.191.0/24
add list="telkom" address=180.240.192.0/24
add list="telkom" address=180.240.193.0/24
add list="telkom" address=180.240.195.0/24
add list="telkom" address=180.240.196.0/24
add list="telkom" address=180.240.197.0/24
add list="telkom" address=180.240.199.0/24
add list="telkom" address=180.240.201.0/24
add list="telkom" address=180.240.203.0/24
add list="telkom" address=180.241.0.0/21
add list="telkom" address=180.241.100.0/23
add list="telkom" address=180.241.102.0/23
add list="telkom" address=180.241.104.0/23
add list="telkom" address=180.241.106.0/23
add list="telkom" address=180.241.112.0/23
add list="telkom" address=180.241.114.0/23
add list="telkom" address=180.241.116.0/22
add list="telkom" address=180.241.12.0/22
add list="telkom" address=180.241.120.0/22
add list="telkom" address=180.241.124.0/23
add list="telkom" address=180.241.126.0/23
add list="telkom" address=180.241.128.0/21
add list="telkom" address=180.241.138.0/23
add list="telkom" address=180.241.140.0/23
add list="telkom" address=180.241.142.0/23
add list="telkom" address=180.241.144.0/20
add list="telkom" address=180.241.16.0/21
add list="telkom" address=180.241.160.0/20
add list="telkom" address=180.241.160.0/22
add list="telkom" address=180.241.165.0/24
add list="telkom" address=180.241.166.0/23
add list="telkom" address=180.241.168.0/21
add list="telkom" address=180.241.176.0/20
add list="telkom" address=180.241.192.0/21
add list="telkom" address=180.241.200.0/22
add list="telkom" address=180.241.204.0/22
add list="telkom" address=180.241.208.0/23
add list="telkom" address=180.241.210.0/23
add list="telkom" address=180.241.212.0/24
add list="telkom" address=180.241.213.0/24
add list="telkom" address=180.241.214.0/24
add list="telkom" address=180.241.215.0/24
add list="telkom" address=180.241.216.0/24
add list="telkom" address=180.241.217.0/24
add list="telkom" address=180.241.218.0/23
add list="telkom" address=180.241.220.0/23
add list="telkom" address=180.241.222.0/23
add list="telkom" address=180.241.224.0/23
add list="telkom" address=180.241.226.0/23
add list="telkom" address=180.241.228.0/23
add list="telkom" address=180.241.230.0/24
add list="telkom" address=180.241.231.0/24
add list="telkom" address=180.241.233.0/24
add list="telkom" address=180.241.236.0/22
add list="telkom" address=180.241.24.0/23
add list="telkom" address=180.241.240.0/22
add list="telkom" address=180.241.244.0/23
add list="telkom" address=180.241.246.0/23
add list="telkom" address=180.241.248.0/23
add list="telkom" address=180.241.250.0/23
add list="telkom" address=180.241.252.0/22
add list="telkom" address=180.241.252.0/24
add list="telkom" address=180.241.254.0/24
add list="telkom" address=180.241.255.0/24
add list="telkom" address=180.241.27.0/24
add list="telkom" address=180.241.28.0/22
add list="telkom" address=180.241.32.0/21
add list="telkom" address=180.241.41.0/24
add list="telkom" address=180.241.42.0/23
add list="telkom" address=180.241.44.0/22
add list="telkom" address=180.241.48.0/21
add list="telkom" address=180.241.56.0/23
add list="telkom" address=180.241.58.0/23
add list="telkom" address=180.241.60.0/23
add list="telkom" address=180.241.62.0/23
add list="telkom" address=180.241.64.0/22
add list="telkom" address=180.241.68.0/24
add list="telkom" address=180.241.69.0/24
add list="telkom" address=180.241.70.0/24
add list="telkom" address=180.241.72.0/22
add list="telkom" address=180.241.76.0/24
add list="telkom" address=180.241.77.0/24
add list="telkom" address=180.241.78.0/23
add list="telkom" address=180.241.8.0/22
add list="telkom" address=180.241.80.0/23
add list="telkom" address=180.241.82.0/23
add list="telkom" address=180.241.84.0/22
add list="telkom" address=180.241.88.0/22
add list="telkom" address=180.241.92.0/22
add list="telkom" address=180.241.96.0/23
add list="telkom" address=180.241.98.0/23
add list="telkom" address=180.242.0.0/20
add list="telkom" address=180.242.112.0/22
add list="telkom" address=180.242.116.0/24
add list="telkom" address=180.242.117.0/24
add list="telkom" address=180.242.118.0/23
add list="telkom" address=180.242.128.0/21
add list="telkom" address=180.242.136.0/21
add list="telkom" address=180.242.144.0/22
add list="telkom" address=180.242.148.0/23
add list="telkom" address=180.242.150.0/23
add list="telkom" address=180.242.152.0/24
add list="telkom" address=180.242.153.0/24
add list="telkom" address=180.242.155.0/24
add list="telkom" address=180.242.156.0/22
add list="telkom" address=180.242.16.0/20
add list="telkom" address=180.242.160.0/22
add list="telkom" address=180.242.164.0/22
add list="telkom" address=180.242.168.0/23
add list="telkom" address=180.242.170.0/23
add list="telkom" address=180.242.172.0/23
add list="telkom" address=180.242.174.0/23
add list="telkom" address=180.242.176.0/22
add list="telkom" address=180.242.180.0/22
add list="telkom" address=180.242.184.0/23
add list="telkom" address=180.242.186.0/23
add list="telkom" address=180.242.188.0/22
add list="telkom" address=180.242.192.0/21
add list="telkom" address=180.242.200.0/21
add list="telkom" address=180.242.208.0/22
add list="telkom" address=180.242.212.0/22
add list="telkom" address=180.242.216.0/22
add list="telkom" address=180.242.220.0/23
add list="telkom" address=180.242.222.0/24
add list="telkom" address=180.242.224.0/24
add list="telkom" address=180.242.225.0/24
add list="telkom" address=180.242.226.0/23
add list="telkom" address=180.242.228.0/22
add list="telkom" address=180.242.232.0/22
add list="telkom" address=180.242.236.0/22
add list="telkom" address=180.242.240.0/23
add list="telkom" address=180.242.242.0/23
add list="telkom" address=180.242.244.0/23
add list="telkom" address=180.242.246.0/23
add list="telkom" address=180.242.248.0/22
add list="telkom" address=180.242.252.0/23
add list="telkom" address=180.242.254.0/23
add list="telkom" address=180.242.32.0/21
add list="telkom" address=180.242.40.0/23
add list="telkom" address=180.242.42.0/23
add list="telkom" address=180.242.44.0/22
add list="telkom" address=180.242.48.0/23
add list="telkom" address=180.242.50.0/23
add list="telkom" address=180.242.52.0/23
add list="telkom" address=180.242.54.0/23
add list="telkom" address=180.242.56.0/22
add list="telkom" address=180.242.60.0/23
add list="telkom" address=180.242.62.0/23
add list="telkom" address=180.242.64.0/24
add list="telkom" address=180.242.65.0/24
add list="telkom" address=180.242.66.0/23
add list="telkom" address=180.242.68.0/22
add list="telkom" address=180.242.72.0/23
add list="telkom" address=180.242.74.0/24
add list="telkom" address=180.242.75.0/24
add list="telkom" address=180.242.76.0/24
add list="telkom" address=180.242.78.0/23
add list="telkom" address=180.242.80.0/21
add list="telkom" address=180.242.88.0/23
add list="telkom" address=180.242.90.0/23
add list="telkom" address=180.242.92.0/22
add list="telkom" address=180.242.96.0/20
add list="telkom" address=180.243.0.0/20
add list="telkom" address=180.243.104.0/21
add list="telkom" address=180.243.112.0/21
add list="telkom" address=180.243.120.0/21
add list="telkom" address=180.243.128.0/21
add list="telkom" address=180.243.136.0/21
add list="telkom" address=180.243.144.0/22
add list="telkom" address=180.243.148.0/22
add list="telkom" address=180.243.152.0/24
add list="telkom" address=180.243.153.0/24
add list="telkom" address=180.243.154.0/24
add list="telkom" address=180.243.155.0/24
add list="telkom" address=180.243.156.0/22
add list="telkom" address=180.243.16.0/21
add list="telkom" address=180.243.160.0/24
add list="telkom" address=180.243.162.0/24
add list="telkom" address=180.243.163.0/24
add list="telkom" address=180.243.164.0/24
add list="telkom" address=180.243.165.0/24
add list="telkom" address=180.243.166.0/23
add list="telkom" address=180.243.168.0/22
add list="telkom" address=180.243.172.0/22
add list="telkom" address=180.243.176.0/22
add list="telkom" address=180.243.180.0/23
add list="telkom" address=180.243.182.0/23
add list="telkom" address=180.243.184.0/23
add list="telkom" address=180.243.186.0/23
add list="telkom" address=180.243.188.0/22
add list="telkom" address=180.243.192.0/20
add list="telkom" address=180.243.208.0/22
add list="telkom" address=180.243.212.0/22
add list="telkom" address=180.243.216.0/23
add list="telkom" address=180.243.218.0/23
add list="telkom" address=180.243.220.0/22
add list="telkom" address=180.243.224.0/22
add list="telkom" address=180.243.228.0/23
add list="telkom" address=180.243.230.0/23
add list="telkom" address=180.243.232.0/23
add list="telkom" address=180.243.234.0/23
add list="telkom" address=180.243.236.0/23
add list="telkom" address=180.243.238.0/23
add list="telkom" address=180.243.24.0/22
add list="telkom" address=180.243.240.0/23
add list="telkom" address=180.243.242.0/23
add list="telkom" address=180.243.244.0/23
add list="telkom" address=180.243.246.0/23
add list="telkom" address=180.243.248.0/22
add list="telkom" address=180.243.252.0/22
add list="telkom" address=180.243.28.0/22
add list="telkom" address=180.243.32.0/21
add list="telkom" address=180.243.40.0/22
add list="telkom" address=180.243.44.0/23
add list="telkom" address=180.243.46.0/24
add list="telkom" address=180.243.47.0/24
add list="telkom" address=180.243.48.0/24
add list="telkom" address=180.243.49.0/24
add list="telkom" address=180.243.50.0/24
add list="telkom" address=180.243.51.0/24
add list="telkom" address=180.243.52.0/22
add list="telkom" address=180.243.56.0/22
add list="telkom" address=180.243.60.0/22
add list="telkom" address=180.243.64.0/23
add list="telkom" address=180.243.66.0/23
add list="telkom" address=180.243.70.0/23
add list="telkom" address=180.243.72.0/22
add list="telkom" address=180.243.76.0/23
add list="telkom" address=180.243.78.0/23
add list="telkom" address=180.243.80.0/23
add list="telkom" address=180.243.84.0/23
add list="telkom" address=180.243.86.0/23
add list="telkom" address=180.243.88.0/22
add list="telkom" address=180.243.92.0/23
add list="telkom" address=180.243.94.0/23
add list="telkom" address=180.243.96.0/21
add list="telkom" address=180.244.0.0/24
add list="telkom" address=180.244.1.0/24
add list="telkom" address=180.244.100.0/22
add list="telkom" address=180.244.104.0/22
add list="telkom" address=180.244.108.0/22
add list="telkom" address=180.244.112.0/23
add list="telkom" address=180.244.114.0/23
add list="telkom" address=180.244.118.0/23
add list="telkom" address=180.244.120.0/22
add list="telkom" address=180.244.124.0/22
add list="telkom" address=180.244.128.0/20
add list="telkom" address=180.244.144.0/22
add list="telkom" address=180.244.148.0/22
add list="telkom" address=180.244.152.0/21
add list="telkom" address=180.244.16.0/21
add list="telkom" address=180.244.160.0/20
add list="telkom" address=180.244.176.0/21
add list="telkom" address=180.244.184.0/23
add list="telkom" address=180.244.186.0/24
add list="telkom" address=180.244.187.0/24
add list="telkom" address=180.244.188.0/22
add list="telkom" address=180.244.192.0/22
add list="telkom" address=180.244.196.0/22
add list="telkom" address=180.244.2.0/24
add list="telkom" address=180.244.200.0/22
add list="telkom" address=180.244.208.0/22
add list="telkom" address=180.244.212.0/22
add list="telkom" address=180.244.216.0/22
add list="telkom" address=180.244.220.0/23
add list="telkom" address=180.244.222.0/23
add list="telkom" address=180.244.224.0/22
add list="telkom" address=180.244.228.0/22
add list="telkom" address=180.244.232.0/24
add list="telkom" address=180.244.233.0/24
add list="telkom" address=180.244.234.0/24
add list="telkom" address=180.244.235.0/24
add list="telkom" address=180.244.236.0/24
add list="telkom" address=180.244.237.0/24
add list="telkom" address=180.244.238.0/23
add list="telkom" address=180.244.24.0/21
add list="telkom" address=180.244.240.0/22
add list="telkom" address=180.244.244.0/22
add list="telkom" address=180.244.248.0/22
add list="telkom" address=180.244.252.0/22
add list="telkom" address=180.244.3.0/24
add list="telkom" address=180.244.32.0/21
add list="telkom" address=180.244.4.0/24
add list="telkom" address=180.244.40.0/23
add list="telkom" address=180.244.42.0/23
add list="telkom" address=180.244.44.0/23
add list="telkom" address=180.244.46.0/23
add list="telkom" address=180.244.48.0/22
add list="telkom" address=180.244.5.0/24
add list="telkom" address=180.244.52.0/22
add list="telkom" address=180.244.56.0/21
add list="telkom" address=180.244.6.0/23
add list="telkom" address=180.244.64.0/21
add list="telkom" address=180.244.72.0/21
add list="telkom" address=180.244.8.0/21
add list="telkom" address=180.244.80.0/21
add list="telkom" address=180.244.88.0/22
add list="telkom" address=180.244.92.0/23
add list="telkom" address=180.244.94.0/24
add list="telkom" address=180.244.95.0/24
add list="telkom" address=180.244.96.0/24
add list="telkom" address=180.244.98.0/24
add list="telkom" address=180.244.99.0/24
add list="telkom" address=180.245.0.0/24
add list="telkom" address=180.245.1.0/24
add list="telkom" address=180.245.100.0/22
add list="telkom" address=180.245.104.0/22
add list="telkom" address=180.245.108.0/22
add list="telkom" address=180.245.112.0/23
add list="telkom" address=180.245.114.0/23
add list="telkom" address=180.245.116.0/23
add list="telkom" address=180.245.118.0/23
add list="telkom" address=180.245.12.0/22
add list="telkom" address=180.245.120.0/23
add list="telkom" address=180.245.122.0/23
add list="telkom" address=180.245.124.0/23
add list="telkom" address=180.245.126.0/23
add list="telkom" address=180.245.128.0/21
add list="telkom" address=180.245.136.0/23
add list="telkom" address=180.245.138.0/23
add list="telkom" address=180.245.140.0/23
add list="telkom" address=180.245.142.0/23
add list="telkom" address=180.245.144.0/23
add list="telkom" address=180.245.146.0/23
add list="telkom" address=180.245.148.0/23
add list="telkom" address=180.245.150.0/23
add list="telkom" address=180.245.152.0/24
add list="telkom" address=180.245.153.0/24
add list="telkom" address=180.245.154.0/23
add list="telkom" address=180.245.156.0/22
add list="telkom" address=180.245.16.0/22
add list="telkom" address=180.245.160.0/21
add list="telkom" address=180.245.168.0/21
add list="telkom" address=180.245.176.0/20
add list="telkom" address=180.245.192.0/22
add list="telkom" address=180.245.196.0/22
add list="telkom" address=180.245.2.0/24
add list="telkom" address=180.245.20.0/22
add list="telkom" address=180.245.200.0/24
add list="telkom" address=180.245.201.0/24
add list="telkom" address=180.245.202.0/23
add list="telkom" address=180.245.204.0/22
add list="telkom" address=180.245.208.0/22
add list="telkom" address=180.245.212.0/22
add list="telkom" address=180.245.216.0/21
add list="telkom" address=180.245.224.0/22
add list="telkom" address=180.245.228.0/23
add list="telkom" address=180.245.230.0/23
add list="telkom" address=180.245.232.0/22
add list="telkom" address=180.245.236.0/23
add list="telkom" address=180.245.238.0/23
add list="telkom" address=180.245.24.0/22
add list="telkom" address=180.245.240.0/22
add list="telkom" address=180.245.244.0/23
add list="telkom" address=180.245.246.0/23
add list="telkom" address=180.245.248.0/22
add list="telkom" address=180.245.252.0/22
add list="telkom" address=180.245.28.0/22
add list="telkom" address=180.245.3.0/24
add list="telkom" address=180.245.32.0/21
add list="telkom" address=180.245.4.0/24
add list="telkom" address=180.245.40.0/21
add list="telkom" address=180.245.48.0/21
add list="telkom" address=180.245.5.0/24
add list="telkom" address=180.245.56.0/21
add list="telkom" address=180.245.6.0/23
add list="telkom" address=180.245.64.0/21
add list="telkom" address=180.245.72.0/21
add list="telkom" address=180.245.8.0/22
add list="telkom" address=180.245.80.0/21
add list="telkom" address=180.245.88.0/23
add list="telkom" address=180.245.90.0/23
add list="telkom" address=180.245.92.0/23
add list="telkom" address=180.245.94.0/24
add list="telkom" address=180.245.95.0/24
add list="telkom" address=180.245.96.0/22
add list="telkom" address=180.246.0.0/23
add list="telkom" address=180.246.100.0/22
add list="telkom" address=180.246.104.0/23
add list="telkom" address=180.246.106.0/23
add list="telkom" address=180.246.108.0/23
add list="telkom" address=180.246.110.0/23
add list="telkom" address=180.246.112.0/23
add list="telkom" address=180.246.114.0/23
add list="telkom" address=180.246.116.0/23
add list="telkom" address=180.246.118.0/23
add list="telkom" address=180.246.120.0/23
add list="telkom" address=180.246.122.0/23
add list="telkom" address=180.246.124.0/22
add list="telkom" address=180.246.128.0/21
add list="telkom" address=180.246.136.0/22
add list="telkom" address=180.246.140.0/22
add list="telkom" address=180.246.144.0/22
add list="telkom" address=180.246.148.0/22
add list="telkom" address=180.246.152.0/22
add list="telkom" address=180.246.156.0/22
add list="telkom" address=180.246.16.0/22
add list="telkom" address=180.246.160.0/22
add list="telkom" address=180.246.166.0/23
add list="telkom" address=180.246.168.0/23
add list="telkom" address=180.246.170.0/23
add list="telkom" address=180.246.172.0/22
add list="telkom" address=180.246.176.0/23
add list="telkom" address=180.246.178.0/23
add list="telkom" address=180.246.180.0/23
add list="telkom" address=180.246.182.0/23
add list="telkom" address=180.246.184.0/23
add list="telkom" address=180.246.186.0/23
add list="telkom" address=180.246.188.0/22
add list="telkom" address=180.246.192.0/22
add list="telkom" address=180.246.196.0/24
add list="telkom" address=180.246.197.0/24
add list="telkom" address=180.246.198.0/24
add list="telkom" address=180.246.199.0/24
add list="telkom" address=180.246.2.0/23
add list="telkom" address=180.246.20.0/22
add list="telkom" address=180.246.200.0/24
add list="telkom" address=180.246.201.0/24
add list="telkom" address=180.246.202.0/23
add list="telkom" address=180.246.204.0/22
add list="telkom" address=180.246.208.0/22
add list="telkom" address=180.246.212.0/22
add list="telkom" address=180.246.216.0/22
add list="telkom" address=180.246.220.0/22
add list="telkom" address=180.246.224.0/23
add list="telkom" address=180.246.226.0/23
add list="telkom" address=180.246.228.0/22
add list="telkom" address=180.246.232.0/22
add list="telkom" address=180.246.236.0/22
add list="telkom" address=180.246.24.0/22
add list="telkom" address=180.246.240.0/21
add list="telkom" address=180.246.248.0/21
add list="telkom" address=180.246.28.0/23
add list="telkom" address=180.246.30.0/23
add list="telkom" address=180.246.32.0/21
add list="telkom" address=180.246.4.0/22
add list="telkom" address=180.246.40.0/22
add list="telkom" address=180.246.44.0/22
add list="telkom" address=180.246.48.0/22
add list="telkom" address=180.246.52.0/22
add list="telkom" address=180.246.56.0/22
add list="telkom" address=180.246.60.0/22
add list="telkom" address=180.246.64.0/22
add list="telkom" address=180.246.68.0/22
add list="telkom" address=180.246.72.0/22
add list="telkom" address=180.246.76.0/22
add list="telkom" address=180.246.8.0/21
add list="telkom" address=180.246.80.0/22
add list="telkom" address=180.246.84.0/22
add list="telkom" address=180.246.88.0/22
add list="telkom" address=180.246.92.0/22
add list="telkom" address=180.246.96.0/24
add list="telkom" address=180.246.97.0/24
add list="telkom" address=180.246.98.0/24
add list="telkom" address=180.247.0.0/24
add list="telkom" address=180.247.1.0/24
add list="telkom" address=180.247.10.0/23
add list="telkom" address=180.247.100.0/23
add list="telkom" address=180.247.102.0/23
add list="telkom" address=180.247.104.0/23
add list="telkom" address=180.247.106.0/23
add list="telkom" address=180.247.108.0/22
add list="telkom" address=180.247.112.0/23
add list="telkom" address=180.247.114.0/23
add list="telkom" address=180.247.116.0/23
add list="telkom" address=180.247.118.0/23
add list="telkom" address=180.247.12.0/23
add list="telkom" address=180.247.120.0/22
add list="telkom" address=180.247.124.0/23
add list="telkom" address=180.247.126.0/23
add list="telkom" address=180.247.128.0/21
add list="telkom" address=180.247.136.0/22
add list="telkom" address=180.247.14.0/23
add list="telkom" address=180.247.140.0/22
add list="telkom" address=180.247.144.0/22
add list="telkom" address=180.247.148.0/22
add list="telkom" address=180.247.152.0/22
add list="telkom" address=180.247.156.0/24
add list="telkom" address=180.247.157.0/24
add list="telkom" address=180.247.158.0/24
add list="telkom" address=180.247.159.0/24
add list="telkom" address=180.247.16.0/23
add list="telkom" address=180.247.160.0/24
add list="telkom" address=180.247.161.0/24
add list="telkom" address=180.247.162.0/23
add list="telkom" address=180.247.164.0/23
add list="telkom" address=180.247.166.0/23
add list="telkom" address=180.247.168.0/22
add list="telkom" address=180.247.172.0/22
add list="telkom" address=180.247.176.0/21
add list="telkom" address=180.247.18.0/23
add list="telkom" address=180.247.184.0/21
add list="telkom" address=180.247.192.0/22
add list="telkom" address=180.247.196.0/23
add list="telkom" address=180.247.198.0/23
add list="telkom" address=180.247.2.0/24
add list="telkom" address=180.247.20.0/22
add list="telkom" address=180.247.200.0/23
add list="telkom" address=180.247.202.0/24
add list="telkom" address=180.247.203.0/24
add list="telkom" address=180.247.204.0/24
add list="telkom" address=180.247.205.0/24
add list="telkom" address=180.247.206.0/24
add list="telkom" address=180.247.207.0/24
add list="telkom" address=180.247.208.0/22
add list="telkom" address=180.247.212.0/22
add list="telkom" address=180.247.216.0/23
add list="telkom" address=180.247.218.0/23
add list="telkom" address=180.247.220.0/22
add list="telkom" address=180.247.224.0/21
add list="telkom" address=180.247.232.0/22
add list="telkom" address=180.247.236.0/23
add list="telkom" address=180.247.238.0/24
add list="telkom" address=180.247.239.0/24
add list="telkom" address=180.247.24.0/21
add list="telkom" address=180.247.240.0/24
add list="telkom" address=180.247.241.0/24
add list="telkom" address=180.247.242.0/24
add list="telkom" address=180.247.243.0/24
add list="telkom" address=180.247.244.0/22
add list="telkom" address=180.247.248.0/23
add list="telkom" address=180.247.250.0/23
add list="telkom" address=180.247.252.0/22
add list="telkom" address=180.247.3.0/24
add list="telkom" address=180.247.32.0/22
add list="telkom" address=180.247.36.0/24
add list="telkom" address=180.247.37.0/24
add list="telkom" address=180.247.38.0/24
add list="telkom" address=180.247.39.0/24
add list="telkom" address=180.247.4.0/22
add list="telkom" address=180.247.40.0/24
add list="telkom" address=180.247.41.0/24
add list="telkom" address=180.247.42.0/23
add list="telkom" address=180.247.44.0/22
add list="telkom" address=180.247.48.0/23
add list="telkom" address=180.247.50.0/23
add list="telkom" address=180.247.52.0/23
add list="telkom" address=180.247.54.0/23
add list="telkom" address=180.247.56.0/22
add list="telkom" address=180.247.60.0/22
add list="telkom" address=180.247.64.0/21
add list="telkom" address=180.247.72.0/22
add list="telkom" address=180.247.76.0/23
add list="telkom" address=180.247.78.0/24
add list="telkom" address=180.247.79.0/24
add list="telkom" address=180.247.8.0/23
add list="telkom" address=180.247.80.0/24
add list="telkom" address=180.247.81.0/24
add list="telkom" address=180.247.82.0/24
add list="telkom" address=180.247.83.0/24
add list="telkom" address=180.247.84.0/22
add list="telkom" address=180.247.88.0/21
add list="telkom" address=180.247.96.0/22
add list="telkom" address=180.248.0.0/20
add list="telkom" address=180.248.100.0/23
add list="telkom" address=180.248.102.0/23
add list="telkom" address=180.248.104.0/23
add list="telkom" address=180.248.106.0/23
add list="telkom" address=180.248.108.0/23
add list="telkom" address=180.248.110.0/24
add list="telkom" address=180.248.111.0/24
add list="telkom" address=180.248.112.0/24
add list="telkom" address=180.248.113.0/24
add list="telkom" address=180.248.114.0/24
add list="telkom" address=180.248.115.0/24
add list="telkom" address=180.248.116.0/22
add list="telkom" address=180.248.120.0/22
add list="telkom" address=180.248.126.0/23
add list="telkom" address=180.248.128.0/22
add list="telkom" address=180.248.132.0/22
add list="telkom" address=180.248.136.0/22
add list="telkom" address=180.248.140.0/22
add list="telkom" address=180.248.144.0/23
add list="telkom" address=180.248.146.0/23
add list="telkom" address=180.248.148.0/24
add list="telkom" address=180.248.149.0/24
add list="telkom" address=180.248.150.0/24
add list="telkom" address=180.248.151.0/24
add list="telkom" address=180.248.152.0/24
add list="telkom" address=180.248.153.0/24
add list="telkom" address=180.248.154.0/23
add list="telkom" address=180.248.156.0/23
add list="telkom" address=180.248.158.0/23
add list="telkom" address=180.248.16.0/20
add list="telkom" address=180.248.160.0/23
add list="telkom" address=180.248.162.0/23
add list="telkom" address=180.248.164.0/22
add list="telkom" address=180.248.168.0/22
add list="telkom" address=180.248.172.0/23
add list="telkom" address=180.248.174.0/23
add list="telkom" address=180.248.176.0/23
add list="telkom" address=180.248.178.0/24
add list="telkom" address=180.248.179.0/24
add list="telkom" address=180.248.180.0/24
add list="telkom" address=180.248.181.0/24
add list="telkom" address=180.248.182.0/24
add list="telkom" address=180.248.183.0/24
add list="telkom" address=180.248.184.0/22
add list="telkom" address=180.248.188.0/22
add list="telkom" address=180.248.192.0/23
add list="telkom" address=180.248.194.0/23
add list="telkom" address=180.248.196.0/22
add list="telkom" address=180.248.200.0/23
add list="telkom" address=180.248.202.0/24
add list="telkom" address=180.248.204.0/22
add list="telkom" address=180.248.208.0/23
add list="telkom" address=180.248.210.0/23
add list="telkom" address=180.248.212.0/22
add list="telkom" address=180.248.216.0/23
add list="telkom" address=180.248.218.0/24
add list="telkom" address=180.248.219.0/24
add list="telkom" address=180.248.220.0/24
add list="telkom" address=180.248.221.0/24
add list="telkom" address=180.248.222.0/24
add list="telkom" address=180.248.223.0/24
add list="telkom" address=180.248.224.0/21
add list="telkom" address=180.248.232.0/21
add list="telkom" address=180.248.240.0/21
add list="telkom" address=180.248.248.0/21
add list="telkom" address=180.248.32.0/20
add list="telkom" address=180.248.48.0/20
add list="telkom" address=180.248.64.0/23
add list="telkom" address=180.248.66.0/23
add list="telkom" address=180.248.68.0/22
add list="telkom" address=180.248.72.0/22
add list="telkom" address=180.248.76.0/22
add list="telkom" address=180.248.80.0/23
add list="telkom" address=180.248.82.0/23
add list="telkom" address=180.248.84.0/24
add list="telkom" address=180.248.85.0/24
add list="telkom" address=180.248.86.0/24
add list="telkom" address=180.248.87.0/24
add list="telkom" address=180.248.88.0/24
add list="telkom" address=180.248.89.0/24
add list="telkom" address=180.248.90.0/23
add list="telkom" address=180.248.92.0/23
add list="telkom" address=180.248.94.0/23
add list="telkom" address=180.248.96.0/23
add list="telkom" address=180.248.98.0/23
add list="telkom" address=180.249.0.0/21
add list="telkom" address=180.249.104.0/22
add list="telkom" address=180.249.108.0/22
add list="telkom" address=180.249.112.0/22
add list="telkom" address=180.249.116.0/22
add list="telkom" address=180.249.120.0/22
add list="telkom" address=180.249.124.0/23
add list="telkom" address=180.249.126.0/23
add list="telkom" address=180.249.128.0/23
add list="telkom" address=180.249.130.0/23
add list="telkom" address=180.249.132.0/23
add list="telkom" address=180.249.134.0/23
add list="telkom" address=180.249.136.0/23
add list="telkom" address=180.249.138.0/23
add list="telkom" address=180.249.140.0/23
add list="telkom" address=180.249.142.0/24
add list="telkom" address=180.249.143.0/24
add list="telkom" address=180.249.144.0/24
add list="telkom" address=180.249.145.0/24
add list="telkom" address=180.249.147.0/24
add list="telkom" address=180.249.148.0/23
add list="telkom" address=180.249.151.0/24
add list="telkom" address=180.249.152.0/22
add list="telkom" address=180.249.156.0/22
add list="telkom" address=180.249.16.0/22
add list="telkom" address=180.249.160.0/23
add list="telkom" address=180.249.162.0/23
add list="telkom" address=180.249.164.0/22
add list="telkom" address=180.249.168.0/21
add list="telkom" address=180.249.176.0/24
add list="telkom" address=180.249.177.0/24
add list="telkom" address=180.249.179.0/24
add list="telkom" address=180.249.180.0/24
add list="telkom" address=180.249.182.0/23
add list="telkom" address=180.249.184.0/22
add list="telkom" address=180.249.188.0/23
add list="telkom" address=180.249.190.0/24
add list="telkom" address=180.249.191.0/24
add list="telkom" address=180.249.192.0/22
add list="telkom" address=180.249.196.0/23
add list="telkom" address=180.249.198.0/23
add list="telkom" address=180.249.20.0/22
add list="telkom" address=180.249.200.0/22
add list="telkom" address=180.249.204.0/22
add list="telkom" address=180.249.208.0/22
add list="telkom" address=180.249.212.0/22
add list="telkom" address=180.249.216.0/23
add list="telkom" address=180.249.218.0/23
add list="telkom" address=180.249.220.0/24
add list="telkom" address=180.249.221.0/24
add list="telkom" address=180.249.222.0/24
add list="telkom" address=180.249.223.0/24
add list="telkom" address=180.249.224.0/21
add list="telkom" address=180.249.232.0/22
add list="telkom" address=180.249.236.0/23
add list="telkom" address=180.249.238.0/23
add list="telkom" address=180.249.24.0/23
add list="telkom" address=180.249.240.0/23
add list="telkom" address=180.249.242.0/23
add list="telkom" address=180.249.244.0/22
add list="telkom" address=180.249.248.0/21
add list="telkom" address=180.249.26.0/23
add list="telkom" address=180.249.28.0/22
add list="telkom" address=180.249.32.0/22
add list="telkom" address=180.249.36.0/23
add list="telkom" address=180.249.39.0/24
add list="telkom" address=180.249.40.0/24
add list="telkom" address=180.249.41.0/24
add list="telkom" address=180.249.42.0/24
add list="telkom" address=180.249.43.0/24
add list="telkom" address=180.249.44.0/24
add list="telkom" address=180.249.46.0/23
add list="telkom" address=180.249.48.0/22
add list="telkom" address=180.249.52.0/23
add list="telkom" address=180.249.54.0/23
add list="telkom" address=180.249.56.0/23
add list="telkom" address=180.249.58.0/23
add list="telkom" address=180.249.60.0/23
add list="telkom" address=180.249.62.0/23
add list="telkom" address=180.249.64.0/21
add list="telkom" address=180.249.72.0/21
add list="telkom" address=180.249.8.0/21
add list="telkom" address=180.249.80.0/22
add list="telkom" address=180.249.84.0/22
add list="telkom" address=180.249.88.0/23
add list="telkom" address=180.249.90.0/24
add list="telkom" address=180.249.92.0/24
add list="telkom" address=180.249.93.0/24
add list="telkom" address=180.249.94.0/24
add list="telkom" address=180.249.95.0/24
add list="telkom" address=180.249.96.0/21
add list="telkom" address=180.250.116.0/24
add list="telkom" address=180.250.118.0/24
add list="telkom" address=180.250.119.0/24
add list="telkom" address=180.250.124.0/24
add list="telkom" address=180.250.125.0/24
add list="telkom" address=180.250.152.0/24
add list="telkom" address=180.250.169.0/24
add list="telkom" address=180.250.18.0/24
add list="telkom" address=180.250.19.0/24
add list="telkom" address=180.250.230.0/24
add list="telkom" address=180.250.240.0/24
add list="telkom" address=180.250.246.0/24
add list="telkom" address=180.250.247.0/24
add list="telkom" address=180.250.248.0/24
add list="telkom" address=180.250.249.0/24
add list="telkom" address=180.250.29.0/24
add list="telkom" address=180.250.81.0/24
add list="telkom" address=180.251.0.0/20
add list="telkom" address=180.251.112.0/20
add list="telkom" address=180.251.128.0/20
add list="telkom" address=180.251.144.0/20
add list="telkom" address=180.251.160.0/20
add list="telkom" address=180.251.176.0/20
add list="telkom" address=180.251.192.0/20
add list="telkom" address=180.251.20.0/24
add list="telkom" address=180.251.208.0/20
add list="telkom" address=180.251.22.0/24
add list="telkom" address=180.251.224.0/20
add list="telkom" address=180.251.240.0/21
add list="telkom" address=180.251.248.0/22
add list="telkom" address=180.251.252.0/22
add list="telkom" address=180.251.28.0/24
add list="telkom" address=180.251.32.0/20
add list="telkom" address=180.251.48.0/20
add list="telkom" address=180.251.64.0/20
add list="telkom" address=180.251.80.0/20
add list="telkom" address=180.251.96.0/20
add list="telkom" address=180.252.112.0/20
add list="telkom" address=180.252.128.0/20
add list="telkom" address=180.252.144.0/20
add list="telkom" address=180.252.16.0/20
add list="telkom" address=180.252.160.0/20
add list="telkom" address=180.252.178.0/24
add list="telkom" address=180.252.179.0/24
add list="telkom" address=180.252.180.0/24
add list="telkom" address=180.252.184.0/24
add list="telkom" address=180.252.185.0/24
add list="telkom" address=180.252.186.0/24
add list="telkom" address=180.252.192.0/20
add list="telkom" address=180.252.208.0/20
add list="telkom" address=180.252.224.0/20
add list="telkom" address=180.252.240.0/20
add list="telkom" address=180.252.32.0/20
add list="telkom" address=180.252.4.0/22
add list="telkom" address=180.252.48.0/20
add list="telkom" address=180.252.64.0/20
add list="telkom" address=180.252.8.0/21
add list="telkom" address=180.252.80.0/20
add list="telkom" address=180.252.96.0/20
add list="telkom" address=180.253.0.0/22
add list="telkom" address=180.253.104.0/21
add list="telkom" address=180.253.112.0/21
add list="telkom" address=180.253.120.0/21
add list="telkom" address=180.253.128.0/21
add list="telkom" address=180.253.136.0/21
add list="telkom" address=180.253.144.0/21
add list="telkom" address=180.253.152.0/21
add list="telkom" address=180.253.16.0/21
add list="telkom" address=180.253.160.0/21
add list="telkom" address=180.253.168.0/21
add list="telkom" address=180.253.176.0/21
add list="telkom" address=180.253.184.0/21
add list="telkom" address=180.253.192.0/21
add list="telkom" address=180.253.200.0/21
add list="telkom" address=180.253.208.0/21
add list="telkom" address=180.253.216.0/21
add list="telkom" address=180.253.224.0/21
add list="telkom" address=180.253.232.0/21
add list="telkom" address=180.253.24.0/21
add list="telkom" address=180.253.240.0/21
add list="telkom" address=180.253.248.0/21
add list="telkom" address=180.253.32.0/20
add list="telkom" address=180.253.4.0/22
add list="telkom" address=180.253.48.0/20
add list="telkom" address=180.253.64.0/20
add list="telkom" address=180.253.8.0/21
add list="telkom" address=180.253.80.0/20
add list="telkom" address=180.253.96.0/21
add list="telkom" address=180.254.0.0/21
add list="telkom" address=180.254.112.0/20
add list="telkom" address=180.254.128.0/20
add list="telkom" address=180.254.144.0/20
add list="telkom" address=180.254.16.0/21
add list="telkom" address=180.254.160.0/20
add list="telkom" address=180.254.176.0/20
add list="telkom" address=180.254.192.0/20
add list="telkom" address=180.254.208.0/20
add list="telkom" address=180.254.224.0/20
add list="telkom" address=180.254.24.0/21
add list="telkom" address=180.254.240.0/20
add list="telkom" address=180.254.32.0/21
add list="telkom" address=180.254.40.0/21
add list="telkom" address=180.254.48.0/21
add list="telkom" address=180.254.56.0/21
add list="telkom" address=180.254.64.0/20
add list="telkom" address=180.254.8.0/21
add list="telkom" address=180.254.80.0/20
add list="telkom" address=180.254.96.0/20
add list="telkom" address=184.26.108.0/22
add list="telkom" address=2001:4488:2000::/48
add list="telkom" address=2001:4488::/32
add list="telkom" address=2001:4489::/32
add list="telkom" address=2001:448a:1060::/44
add list="telkom" address=2001:448a:10a0::/44
add list="telkom" address=2001:448a:10c0::/44
add list="telkom" address=2001:448a:10e0::/44
add list="telkom" address=2001:448a:2000::/44
add list="telkom" address=2001:448a:2020::/44
add list="telkom" address=2001:448a:2040::/44
add list="telkom" address=2001:448a:2060::/44
add list="telkom" address=2001:448a:2080::/44
add list="telkom" address=2001:448a:20a0::/44
add list="telkom" address=2001:448a:3000::/44
add list="telkom" address=2001:448a:3020::/44
add list="telkom" address=2001:448a:3040::/44
add list="telkom" address=2001:448a:3060::/44
add list="telkom" address=2001:448a:4000::/44
add list="telkom" address=2001:448a:4020::/44
add list="telkom" address=2001:448a:4040::/44
add list="telkom" address=2001:448a:4060::/44
add list="telkom" address=2001:448a:5020::/44
add list="telkom" address=2001:448a:5040::/44
add list="telkom" address=2001:448a:50a0::/44
add list="telkom" address=2001:448a:50e0::/44
add list="telkom" address=2001:448a:6000::/44
add list="telkom" address=2001:448a:6020::/44
add list="telkom" address=2001:448a:6040::/44
add list="telkom" address=2001:448a:6060::/44
add list="telkom" address=2001:448a:6080::/44
add list="telkom" address=2001:448a:60c0::/44
add list="telkom" address=2001:448a:7020::/44
add list="telkom" address=2001:448a:7060::/44
add list="telkom" address=2001:448a:7080::/44
add list="telkom" address=2001:448a:70a0::/44
add list="telkom" address=2001:df0:2400::/48
add list="telkom" address=202.134.0.0/24
add list="telkom" address=202.134.4.0/23
add list="telkom" address=202.134.7.0/24
add list="telkom" address=202.93.236.0/22
add list="telkom" address=202.93.236.0/24
add list="telkom" address=202.93.239.0/24
add list="telkom" address=203.130.217.0/24
add list="telkom" address=203.130.218.0/23
add list="telkom" address=203.130.220.0/23
add list="telkom" address=222.124.100.0/22
add list="telkom" address=222.124.108.0/23
add list="telkom" address=222.124.112.0/22
add list="telkom" address=222.124.116.0/23
add list="telkom" address=222.124.118.0/23
add list="telkom" address=222.124.120.0/22
add list="telkom" address=222.124.124.0/22
add list="telkom" address=222.124.252.0/23
add list="telkom" address=222.124.40.0/22
add list="telkom" address=222.124.44.0/22
add list="telkom" address=222.124.48.0/22
add list="telkom" address=222.124.52.0/22
add list="telkom" address=222.124.56.0/21
add list="telkom" address=222.124.64.0/22
add list="telkom" address=222.124.76.0/23
add list="telkom" address=222.124.78.0/23
add list="telkom" address=222.124.80.0/23
add list="telkom" address=222.124.84.0/23
add list="telkom" address=222.124.94.0/23
add list="telkom" address=23.195.104.0/24
add list="telkom" address=23.195.240.0/22
add list="telkom" address=23.2.15.0/24
add list="telkom" address=23.220.172.0/22
add list="telkom" address=23.221.70.0/23
add list="telkom" address=23.221.76.0/22
add list="telkom" address=36.65.0.0/20
add list="telkom" address=36.65.112.0/20
add list="telkom" address=36.65.128.0/20
add list="telkom" address=36.65.144.0/20
add list="telkom" address=36.65.16.0/21
add list="telkom" address=36.65.160.0/20
add list="telkom" address=36.65.176.0/20
add list="telkom" address=36.65.192.0/20
add list="telkom" address=36.65.208.0/20
add list="telkom" address=36.65.224.0/20
add list="telkom" address=36.65.24.0/21
add list="telkom" address=36.65.240.0/20
add list="telkom" address=36.65.32.0/20
add list="telkom" address=36.65.48.0/20
add list="telkom" address=36.65.64.0/20
add list="telkom" address=36.65.80.0/20
add list="telkom" address=36.65.96.0/20
add list="telkom" address=36.66.19.0/24
add list="telkom" address=36.66.2.0/24
add list="telkom" address=36.66.223.0/24
add list="telkom" address=36.66.23.0/24
add list="telkom" address=36.66.24.0/24
add list="telkom" address=36.67.179.0/24
add list="telkom" address=36.67.180.0/24
add list="telkom" address=36.68.0.0/22
add list="telkom" address=36.68.10.0/24
add list="telkom" address=36.68.104.0/21
add list="telkom" address=36.68.11.0/24
add list="telkom" address=36.68.112.0/22
add list="telkom" address=36.68.116.0/22
add list="telkom" address=36.68.12.0/24
add list="telkom" address=36.68.120.0/21
add list="telkom" address=36.68.128.0/21
add list="telkom" address=36.68.13.0/24
add list="telkom" address=36.68.136.0/22
add list="telkom" address=36.68.14.0/24
add list="telkom" address=36.68.140.0/22
add list="telkom" address=36.68.144.0/23
add list="telkom" address=36.68.146.0/23
add list="telkom" address=36.68.148.0/23
add list="telkom" address=36.68.15.0/24
add list="telkom" address=36.68.150.0/23
add list="telkom" address=36.68.152.0/22
add list="telkom" address=36.68.156.0/22
add list="telkom" address=36.68.16.0/21
add list="telkom" address=36.68.160.0/21
add list="telkom" address=36.68.168.0/21
add list="telkom" address=36.68.176.0/21
add list="telkom" address=36.68.184.0/21
add list="telkom" address=36.68.192.0/21
add list="telkom" address=36.68.200.0/21
add list="telkom" address=36.68.208.0/21
add list="telkom" address=36.68.216.0/21
add list="telkom" address=36.68.224.0/21
add list="telkom" address=36.68.232.0/23
add list="telkom" address=36.68.234.0/23
add list="telkom" address=36.68.236.0/22
add list="telkom" address=36.68.24.0/21
add list="telkom" address=36.68.240.0/21
add list="telkom" address=36.68.248.0/22
add list="telkom" address=36.68.252.0/23
add list="telkom" address=36.68.254.0/23
add list="telkom" address=36.68.32.0/21
add list="telkom" address=36.68.40.0/21
add list="telkom" address=36.68.48.0/22
add list="telkom" address=36.68.52.0/22
add list="telkom" address=36.68.53.0/24
add list="telkom" address=36.68.54.0/24
add list="telkom" address=36.68.56.0/21
add list="telkom" address=36.68.64.0/21
add list="telkom" address=36.68.72.0/21
add list="telkom" address=36.68.8.0/24
add list="telkom" address=36.68.80.0/21
add list="telkom" address=36.68.88.0/21
add list="telkom" address=36.68.9.0/24
add list="telkom" address=36.68.96.0/21
add list="telkom" address=36.69.0.0/21
add list="telkom" address=36.69.10.0/24
add list="telkom" address=36.69.104.0/22
add list="telkom" address=36.69.108.0/22
add list="telkom" address=36.69.11.0/24
add list="telkom" address=36.69.112.0/20
add list="telkom" address=36.69.12.0/24
add list="telkom" address=36.69.128.0/23
add list="telkom" address=36.69.13.0/24
add list="telkom" address=36.69.130.0/23
add list="telkom" address=36.69.132.0/22
add list="telkom" address=36.69.136.0/22
add list="telkom" address=36.69.14.0/24
add list="telkom" address=36.69.140.0/22
add list="telkom" address=36.69.144.0/20
add list="telkom" address=36.69.15.0/24
add list="telkom" address=36.69.16.0/21
add list="telkom" address=36.69.160.0/20
add list="telkom" address=36.69.176.0/20
add list="telkom" address=36.69.192.0/21
add list="telkom" address=36.69.200.0/22
add list="telkom" address=36.69.204.0/22
add list="telkom" address=36.69.208.0/21
add list="telkom" address=36.69.216.0/21
add list="telkom" address=36.69.224.0/21
add list="telkom" address=36.69.232.0/21
add list="telkom" address=36.69.24.0/22
add list="telkom" address=36.69.240.0/22
add list="telkom" address=36.69.244.0/22
add list="telkom" address=36.69.248.0/22
add list="telkom" address=36.69.252.0/22
add list="telkom" address=36.69.28.0/22
add list="telkom" address=36.69.32.0/20
add list="telkom" address=36.69.48.0/20
add list="telkom" address=36.69.64.0/20
add list="telkom" address=36.69.8.0/24
add list="telkom" address=36.69.80.0/20
add list="telkom" address=36.69.9.0/24
add list="telkom" address=36.69.96.0/21
add list="telkom" address=36.70.0.0/20
add list="telkom" address=36.70.112.0/20
add list="telkom" address=36.70.128.0/21
add list="telkom" address=36.70.136.0/21
add list="telkom" address=36.70.144.0/20
add list="telkom" address=36.70.16.0/21
add list="telkom" address=36.70.168.0/21
add list="telkom" address=36.70.176.0/21
add list="telkom" address=36.70.184.0/21
add list="telkom" address=36.70.192.0/20
add list="telkom" address=36.70.208.0/20
add list="telkom" address=36.70.224.0/20
add list="telkom" address=36.70.24.0/21
add list="telkom" address=36.70.240.0/21
add list="telkom" address=36.70.248.0/22
add list="telkom" address=36.70.252.0/22
add list="telkom" address=36.70.32.0/20
add list="telkom" address=36.70.48.0/20
add list="telkom" address=36.70.64.0/20
add list="telkom" address=36.70.80.0/21
add list="telkom" address=36.70.88.0/22
add list="telkom" address=36.70.92.0/22
add list="telkom" address=36.70.96.0/20
add list="telkom" address=36.71.0.0/22
add list="telkom" address=36.71.100.0/22
add list="telkom" address=36.71.104.0/22
add list="telkom" address=36.71.108.0/22
add list="telkom" address=36.71.112.0/21
add list="telkom" address=36.71.120.0/21
add list="telkom" address=36.71.128.0/22
add list="telkom" address=36.71.132.0/22
add list="telkom" address=36.71.136.0/24
add list="telkom" address=36.71.137.0/24
add list="telkom" address=36.71.138.0/24
add list="telkom" address=36.71.139.0/24
add list="telkom" address=36.71.140.0/24
add list="telkom" address=36.71.141.0/24
add list="telkom" address=36.71.142.0/24
add list="telkom" address=36.71.143.0/24
add list="telkom" address=36.71.145.0/24
add list="telkom" address=36.71.146.0/23
add list="telkom" address=36.71.148.0/23
add list="telkom" address=36.71.150.0/23
add list="telkom" address=36.71.152.0/21
add list="telkom" address=36.71.16.0/20
add list="telkom" address=36.71.160.0/20
add list="telkom" address=36.71.176.0/20
add list="telkom" address=36.71.192.0/20
add list="telkom" address=36.71.208.0/20
add list="telkom" address=36.71.224.0/21
add list="telkom" address=36.71.232.0/24
add list="telkom" address=36.71.233.0/24
add list="telkom" address=36.71.234.0/24
add list="telkom" address=36.71.235.0/24
add list="telkom" address=36.71.236.0/24
add list="telkom" address=36.71.237.0/24
add list="telkom" address=36.71.238.0/24
add list="telkom" address=36.71.239.0/24
add list="telkom" address=36.71.240.0/21
add list="telkom" address=36.71.248.0/21
add list="telkom" address=36.71.32.0/21
add list="telkom" address=36.71.40.0/23
add list="telkom" address=36.71.42.0/23
add list="telkom" address=36.71.44.0/22
add list="telkom" address=36.71.48.0/21
add list="telkom" address=36.71.56.0/21
add list="telkom" address=36.71.64.0/22
add list="telkom" address=36.71.68.0/22
add list="telkom" address=36.71.72.0/21
add list="telkom" address=36.71.8.0/22
add list="telkom" address=36.71.80.0/20
add list="telkom" address=36.71.96.0/22
add list="telkom" address=36.72.0.0/20
add list="telkom" address=36.72.104.0/21
add list="telkom" address=36.72.112.0/21
add list="telkom" address=36.72.120.0/21
add list="telkom" address=36.72.128.0/21
add list="telkom" address=36.72.136.0/21
add list="telkom" address=36.72.144.0/21
add list="telkom" address=36.72.152.0/21
add list="telkom" address=36.72.16.0/21
add list="telkom" address=36.72.160.0/21
add list="telkom" address=36.72.168.0/21
add list="telkom" address=36.72.180.0/23
add list="telkom" address=36.72.182.0/23
add list="telkom" address=36.72.184.0/21
add list="telkom" address=36.72.192.0/20
add list="telkom" address=36.72.208.0/22
add list="telkom" address=36.72.212.0/24
add list="telkom" address=36.72.213.0/24
add list="telkom" address=36.72.214.0/24
add list="telkom" address=36.72.215.0/24
add list="telkom" address=36.72.216.0/24
add list="telkom" address=36.72.217.0/24
add list="telkom" address=36.72.218.0/24
add list="telkom" address=36.72.219.0/24
add list="telkom" address=36.72.220.0/22
add list="telkom" address=36.72.228.0/22
add list="telkom" address=36.72.232.0/22
add list="telkom" address=36.72.236.0/22
add list="telkom" address=36.72.24.0/21
add list="telkom" address=36.72.240.0/20
add list="telkom" address=36.72.32.0/21
add list="telkom" address=36.72.40.0/21
add list="telkom" address=36.72.48.0/21
add list="telkom" address=36.72.56.0/21
add list="telkom" address=36.72.64.0/20
add list="telkom" address=36.72.80.0/21
add list="telkom" address=36.72.88.0/21
add list="telkom" address=36.72.96.0/21
add list="telkom" address=36.73.0.0/20
add list="telkom" address=36.73.112.0/20
add list="telkom" address=36.73.128.0/20
add list="telkom" address=36.73.144.0/20
add list="telkom" address=36.73.16.0/20
add list="telkom" address=36.73.160.0/21
add list="telkom" address=36.73.168.0/21
add list="telkom" address=36.73.176.0/20
add list="telkom" address=36.73.192.0/20
add list="telkom" address=36.73.208.0/21
add list="telkom" address=36.73.216.0/23
add list="telkom" address=36.73.218.0/23
add list="telkom" address=36.73.220.0/22
add list="telkom" address=36.73.224.0/20
add list="telkom" address=36.73.240.0/21
add list="telkom" address=36.73.248.0/21
add list="telkom" address=36.73.32.0/22
add list="telkom" address=36.73.33.0/24
add list="telkom" address=36.73.34.0/24
add list="telkom" address=36.73.36.0/22
add list="telkom" address=36.73.40.0/23
add list="telkom" address=36.73.42.0/23
add list="telkom" address=36.73.44.0/22
add list="telkom" address=36.73.48.0/20
add list="telkom" address=36.73.64.0/20
add list="telkom" address=36.73.80.0/20
add list="telkom" address=36.73.96.0/20
add list="telkom" address=36.74.0.0/21
add list="telkom" address=36.74.100.0/22
add list="telkom" address=36.74.104.0/21
add list="telkom" address=36.74.112.0/20
add list="telkom" address=36.74.128.0/20
add list="telkom" address=36.74.144.0/21
add list="telkom" address=36.74.152.0/21
add list="telkom" address=36.74.16.0/21
add list="telkom" address=36.74.160.0/20
add list="telkom" address=36.74.176.0/20
add list="telkom" address=36.74.192.0/20
add list="telkom" address=36.74.208.0/20
add list="telkom" address=36.74.224.0/20
add list="telkom" address=36.74.24.0/21
add list="telkom" address=36.74.240.0/21
add list="telkom" address=36.74.248.0/21
add list="telkom" address=36.74.32.0/21
add list="telkom" address=36.74.40.0/24
add list="telkom" address=36.74.41.0/24
add list="telkom" address=36.74.42.0/24
add list="telkom" address=36.74.43.0/24
add list="telkom" address=36.74.44.0/24
add list="telkom" address=36.74.45.0/24
add list="telkom" address=36.74.46.0/24
add list="telkom" address=36.74.47.0/24
add list="telkom" address=36.74.48.0/20
add list="telkom" address=36.74.64.0/21
add list="telkom" address=36.74.72.0/22
add list="telkom" address=36.74.76.0/22
add list="telkom" address=36.74.8.0/21
add list="telkom" address=36.74.80.0/22
add list="telkom" address=36.74.84.0/22
add list="telkom" address=36.74.88.0/21
add list="telkom" address=36.74.96.0/22
add list="telkom" address=36.75.0.0/21
add list="telkom" address=36.75.104.0/21
add list="telkom" address=36.75.112.0/21
add list="telkom" address=36.75.120.0/21
add list="telkom" address=36.75.128.0/21
add list="telkom" address=36.75.136.0/22
add list="telkom" address=36.75.144.0/21
add list="telkom" address=36.75.152.0/21
add list="telkom" address=36.75.16.0/20
add list="telkom" address=36.75.160.0/22
add list="telkom" address=36.75.164.0/22
add list="telkom" address=36.75.168.0/21
add list="telkom" address=36.75.176.0/23
add list="telkom" address=36.75.180.0/22
add list="telkom" address=36.75.184.0/22
add list="telkom" address=36.75.188.0/22
add list="telkom" address=36.75.192.0/23
add list="telkom" address=36.75.195.0/24
add list="telkom" address=36.75.196.0/22
add list="telkom" address=36.75.200.0/22
add list="telkom" address=36.75.204.0/22
add list="telkom" address=36.75.208.0/22
add list="telkom" address=36.75.212.0/22
add list="telkom" address=36.75.216.0/22
add list="telkom" address=36.75.220.0/22
add list="telkom" address=36.75.224.0/21
add list="telkom" address=36.75.232.0/22
add list="telkom" address=36.75.236.0/22
add list="telkom" address=36.75.240.0/20
add list="telkom" address=36.75.32.0/20
add list="telkom" address=36.75.48.0/20
add list="telkom" address=36.75.64.0/22
add list="telkom" address=36.75.68.0/22
add list="telkom" address=36.75.72.0/22
add list="telkom" address=36.75.76.0/22
add list="telkom" address=36.75.8.0/21
add list="telkom" address=36.75.80.0/22
add list="telkom" address=36.75.84.0/22
add list="telkom" address=36.75.88.0/21
add list="telkom" address=36.75.96.0/21
add list="telkom" address=36.76.0.0/21
add list="telkom" address=36.76.112.0/20
add list="telkom" address=36.76.128.0/20
add list="telkom" address=36.76.144.0/20
add list="telkom" address=36.76.160.0/20
add list="telkom" address=36.76.176.0/20
add list="telkom" address=36.76.192.0/20
add list="telkom" address=36.76.208.0/20
add list="telkom" address=36.76.224.0/20
add list="telkom" address=36.76.240.0/22
add list="telkom" address=36.76.244.0/22
add list="telkom" address=36.76.248.0/22
add list="telkom" address=36.76.252.0/23
add list="telkom" address=36.76.254.0/24
add list="telkom" address=36.76.255.0/24
add list="telkom" address=36.76.32.0/20
add list="telkom" address=36.76.48.0/20
add list="telkom" address=36.76.64.0/20
add list="telkom" address=36.76.8.0/21
add list="telkom" address=36.76.80.0/20
add list="telkom" address=36.76.96.0/20
add list="telkom" address=36.77.0.0/22
add list="telkom" address=36.77.112.0/22
add list="telkom" address=36.77.116.0/22
add list="telkom" address=36.77.120.0/22
add list="telkom" address=36.77.124.0/22
add list="telkom" address=36.77.128.0/20
add list="telkom" address=36.77.144.0/24
add list="telkom" address=36.77.145.0/24
add list="telkom" address=36.77.146.0/24
add list="telkom" address=36.77.147.0/24
add list="telkom" address=36.77.148.0/22
add list="telkom" address=36.77.152.0/21
add list="telkom" address=36.77.156.0/22
add list="telkom" address=36.77.16.0/22
add list="telkom" address=36.77.160.0/20
add list="telkom" address=36.77.176.0/23
add list="telkom" address=36.77.178.0/23
add list="telkom" address=36.77.180.0/22
add list="telkom" address=36.77.184.0/21
add list="telkom" address=36.77.192.0/20
add list="telkom" address=36.77.20.0/22
add list="telkom" address=36.77.208.0/20
add list="telkom" address=36.77.224.0/20
add list="telkom" address=36.77.24.0/21
add list="telkom" address=36.77.240.0/20
add list="telkom" address=36.77.32.0/20
add list="telkom" address=36.77.4.0/22
add list="telkom" address=36.77.48.0/20
add list="telkom" address=36.77.64.0/20
add list="telkom" address=36.77.8.0/21
add list="telkom" address=36.77.80.0/23
add list="telkom" address=36.77.82.0/23
add list="telkom" address=36.77.84.0/23
add list="telkom" address=36.77.86.0/23
add list="telkom" address=36.77.88.0/23
add list="telkom" address=36.77.90.0/23
add list="telkom" address=36.77.92.0/22
add list="telkom" address=36.77.96.0/20
add list="telkom" address=36.78.0.0/20
add list="telkom" address=36.78.128.0/22
add list="telkom" address=36.78.136.0/21
add list="telkom" address=36.78.144.0/23
add list="telkom" address=36.78.146.0/23
add list="telkom" address=36.78.148.0/22
add list="telkom" address=36.78.152.0/21
add list="telkom" address=36.78.16.0/22
add list="telkom" address=36.78.160.0/22
add list="telkom" address=36.78.164.0/22
add list="telkom" address=36.78.168.0/22
add list="telkom" address=36.78.172.0/22
add list="telkom" address=36.78.176.0/22
add list="telkom" address=36.78.181.0/24
add list="telkom" address=36.78.182.0/24
add list="telkom" address=36.78.183.0/24
add list="telkom" address=36.78.184.0/24
add list="telkom" address=36.78.186.0/23
add list="telkom" address=36.78.188.0/23
add list="telkom" address=36.78.190.0/23
add list="telkom" address=36.78.192.0/21
add list="telkom" address=36.78.20.0/22
add list="telkom" address=36.78.200.0/22
add list="telkom" address=36.78.204.0/23
add list="telkom" address=36.78.206.0/24
add list="telkom" address=36.78.207.0/24
add list="telkom" address=36.78.208.0/24
add list="telkom" address=36.78.209.0/24
add list="telkom" address=36.78.210.0/24
add list="telkom" address=36.78.211.0/24
add list="telkom" address=36.78.212.0/24
add list="telkom" address=36.78.213.0/24
add list="telkom" address=36.78.214.0/24
add list="telkom" address=36.78.215.0/24
add list="telkom" address=36.78.216.0/24
add list="telkom" address=36.78.217.0/24
add list="telkom" address=36.78.218.0/24
add list="telkom" address=36.78.219.0/24
add list="telkom" address=36.78.220.0/22
add list="telkom" address=36.78.24.0/23
add list="telkom" address=36.78.240.0/24
add list="telkom" address=36.78.242.0/24
add list="telkom" address=36.78.243.0/24
add list="telkom" address=36.78.244.0/23
add list="telkom" address=36.78.246.0/24
add list="telkom" address=36.78.247.0/24
add list="telkom" address=36.78.248.0/24
add list="telkom" address=36.78.249.0/24
add list="telkom" address=36.78.250.0/24
add list="telkom" address=36.78.251.0/24
add list="telkom" address=36.78.252.0/24
add list="telkom" address=36.78.253.0/24
add list="telkom" address=36.78.255.0/24
add list="telkom" address=36.78.26.0/23
add list="telkom" address=36.78.28.0/22
add list="telkom" address=36.78.32.0/19
add list="telkom" address=36.78.64.0/19
add list="telkom" address=36.78.96.0/19
add list="telkom" address=36.79.0.0/19
add list="telkom" address=36.79.128.0/19
add list="telkom" address=36.79.160.0/20
add list="telkom" address=36.79.176.0/22
add list="telkom" address=36.79.180.0/23
add list="telkom" address=36.79.182.0/23
add list="telkom" address=36.79.184.0/21
add list="telkom" address=36.79.192.0/21
add list="telkom" address=36.79.200.0/21
add list="telkom" address=36.79.208.0/20
add list="telkom" address=36.79.224.0/20
add list="telkom" address=36.79.240.0/21
add list="telkom" address=36.79.248.0/24
add list="telkom" address=36.79.249.0/24
add list="telkom" address=36.79.250.0/24
add list="telkom" address=36.79.251.0/24
add list="telkom" address=36.79.32.0/19
add list="telkom" address=36.79.64.0/19
add list="telkom" address=36.79.96.0/19
add list="telkom" address=36.80.0.0/20
add list="telkom" address=36.80.112.0/20
add list="telkom" address=36.80.128.0/20
add list="telkom" address=36.80.144.0/20
add list="telkom" address=36.80.16.0/20
add list="telkom" address=36.80.160.0/20
add list="telkom" address=36.80.176.0/20
add list="telkom" address=36.80.192.0/21
add list="telkom" address=36.80.200.0/21
add list="telkom" address=36.80.208.0/23
add list="telkom" address=36.80.210.0/23
add list="telkom" address=36.80.212.0/22
add list="telkom" address=36.80.216.0/21
add list="telkom" address=36.80.224.0/20
add list="telkom" address=36.80.240.0/20
add list="telkom" address=36.80.32.0/22
add list="telkom" address=36.80.36.0/22
add list="telkom" address=36.80.40.0/21
add list="telkom" address=36.80.48.0/23
add list="telkom" address=36.80.50.0/23
add list="telkom" address=36.80.52.0/23
add list="telkom" address=36.80.54.0/23
add list="telkom" address=36.80.56.0/23
add list="telkom" address=36.80.58.0/23
add list="telkom" address=36.80.60.0/23
add list="telkom" address=36.80.62.0/23
add list="telkom" address=36.80.64.0/20
add list="telkom" address=36.80.80.0/21
add list="telkom" address=36.80.88.0/21
add list="telkom" address=36.80.96.0/20
add list="telkom" address=36.81.0.0/22
add list="telkom" address=36.81.10.0/24
add list="telkom" address=36.81.11.0/24
add list="telkom" address=36.81.112.0/20
add list="telkom" address=36.81.12.0/24
add list="telkom" address=36.81.128.0/20
add list="telkom" address=36.81.13.0/24
add list="telkom" address=36.81.14.0/24
add list="telkom" address=36.81.144.0/20
add list="telkom" address=36.81.15.0/24
add list="telkom" address=36.81.16.0/20
add list="telkom" address=36.81.160.0/20
add list="telkom" address=36.81.176.0/21
add list="telkom" address=36.81.184.0/23
add list="telkom" address=36.81.186.0/23
add list="telkom" address=36.81.188.0/22
add list="telkom" address=36.81.192.0/21
add list="telkom" address=36.81.200.0/22
add list="telkom" address=36.81.204.0/23
add list="telkom" address=36.81.206.0/23
add list="telkom" address=36.81.208.0/21
add list="telkom" address=36.81.216.0/21
add list="telkom" address=36.81.224.0/21
add list="telkom" address=36.81.232.0/21
add list="telkom" address=36.81.240.0/21
add list="telkom" address=36.81.248.0/23
add list="telkom" address=36.81.250.0/23
add list="telkom" address=36.81.252.0/22
add list="telkom" address=36.81.32.0/20
add list="telkom" address=36.81.48.0/20
add list="telkom" address=36.81.64.0/20
add list="telkom" address=36.81.8.0/24
add list="telkom" address=36.81.80.0/20
add list="telkom" address=36.81.9.0/24
add list="telkom" address=36.81.96.0/20
add list="telkom" address=36.82.0.0/20
add list="telkom" address=36.82.104.0/21
add list="telkom" address=36.82.112.0/22
add list="telkom" address=36.82.116.0/22
add list="telkom" address=36.82.120.0/21
add list="telkom" address=36.82.128.0/21
add list="telkom" address=36.82.136.0/21
add list="telkom" address=36.82.144.0/23
add list="telkom" address=36.82.148.0/23
add list="telkom" address=36.82.16.0/21
add list="telkom" address=36.82.168.0/21
add list="telkom" address=36.82.176.0/21
add list="telkom" address=36.82.184.0/21
add list="telkom" address=36.82.192.0/20
add list="telkom" address=36.82.208.0/20
add list="telkom" address=36.82.224.0/21
add list="telkom" address=36.82.232.0/21
add list="telkom" address=36.82.24.0/21
add list="telkom" address=36.82.240.0/20
add list="telkom" address=36.82.32.0/20
add list="telkom" address=36.82.48.0/22
add list="telkom" address=36.82.52.0/22
add list="telkom" address=36.82.72.0/23
add list="telkom" address=36.82.74.0/23
add list="telkom" address=36.82.76.0/22
add list="telkom" address=36.82.80.0/21
add list="telkom" address=36.82.88.0/21
add list="telkom" address=36.83.0.0/24
add list="telkom" address=36.83.1.0/24
add list="telkom" address=36.83.112.0/20
add list="telkom" address=36.83.12.0/22
add list="telkom" address=36.83.128.0/20
add list="telkom" address=36.83.144.0/20
add list="telkom" address=36.83.16.0/20
add list="telkom" address=36.83.160.0/20
add list="telkom" address=36.83.176.0/20
add list="telkom" address=36.83.192.0/20
add list="telkom" address=36.83.2.0/24
add list="telkom" address=36.83.208.0/20
add list="telkom" address=36.83.224.0/20
add list="telkom" address=36.83.240.0/21
add list="telkom" address=36.83.248.0/22
add list="telkom" address=36.83.252.0/22
add list="telkom" address=36.83.3.0/24
add list="telkom" address=36.83.32.0/20
add list="telkom" address=36.83.4.0/22
add list="telkom" address=36.83.48.0/20
add list="telkom" address=36.83.64.0/20
add list="telkom" address=36.83.8.0/22
add list="telkom" address=36.83.80.0/20
add list="telkom" address=36.83.96.0/20
add list="telkom" address=36.84.0.0/24
add list="telkom" address=36.84.100.0/24
add list="telkom" address=36.84.101.0/24
add list="telkom" address=36.84.102.0/23
add list="telkom" address=36.84.104.0/21
add list="telkom" address=36.84.112.0/21
add list="telkom" address=36.84.12.0/24
add list="telkom" address=36.84.120.0/21
add list="telkom" address=36.84.128.0/20
add list="telkom" address=36.84.13.0/24
add list="telkom" address=36.84.14.0/24
add list="telkom" address=36.84.144.0/22
add list="telkom" address=36.84.148.0/22
add list="telkom" address=36.84.152.0/21
add list="telkom" address=36.84.16.0/22
add list="telkom" address=36.84.160.0/21
add list="telkom" address=36.84.184.0/21
add list="telkom" address=36.84.192.0/21
add list="telkom" address=36.84.2.0/24
add list="telkom" address=36.84.200.0/21
add list="telkom" address=36.84.208.0/21
add list="telkom" address=36.84.216.0/21
add list="telkom" address=36.84.227.0/24
add list="telkom" address=36.84.231.0/24
add list="telkom" address=36.84.232.0/21
add list="telkom" address=36.84.24.0/24
add list="telkom" address=36.84.244.0/22
add list="telkom" address=36.84.248.0/21
add list="telkom" address=36.84.25.0/24
add list="telkom" address=36.84.26.0/24
add list="telkom" address=36.84.27.0/24
add list="telkom" address=36.84.35.0/24
add list="telkom" address=36.84.36.0/23
add list="telkom" address=36.84.38.0/23
add list="telkom" address=36.84.40.0/22
add list="telkom" address=36.84.44.0/22
add list="telkom" address=36.84.49.0/24
add list="telkom" address=36.84.52.0/22
add list="telkom" address=36.84.56.0/23
add list="telkom" address=36.84.58.0/23
add list="telkom" address=36.84.60.0/23
add list="telkom" address=36.84.63.0/24
add list="telkom" address=36.84.65.0/24
add list="telkom" address=36.84.72.0/24
add list="telkom" address=36.84.73.0/24
add list="telkom" address=36.84.74.0/24
add list="telkom" address=36.84.75.0/24
add list="telkom" address=36.84.76.0/22
add list="telkom" address=36.84.8.0/22
add list="telkom" address=36.84.80.0/22
add list="telkom" address=36.84.84.0/22
add list="telkom" address=36.84.90.0/23
add list="telkom" address=36.84.92.0/23
add list="telkom" address=36.84.94.0/23
add list="telkom" address=36.84.96.0/22
add list="telkom" address=36.85.0.0/20
add list="telkom" address=36.85.100.0/22
add list="telkom" address=36.85.104.0/22
add list="telkom" address=36.85.108.0/22
add list="telkom" address=36.85.112.0/21
add list="telkom" address=36.85.120.0/21
add list="telkom" address=36.85.128.0/21
add list="telkom" address=36.85.136.0/21
add list="telkom" address=36.85.144.0/21
add list="telkom" address=36.85.152.0/21
add list="telkom" address=36.85.16.0/20
add list="telkom" address=36.85.160.0/21
add list="telkom" address=36.85.168.0/21
add list="telkom" address=36.85.176.0/21
add list="telkom" address=36.85.184.0/21
add list="telkom" address=36.85.192.0/21
add list="telkom" address=36.85.204.0/22
add list="telkom" address=36.85.208.0/21
add list="telkom" address=36.85.216.0/22
add list="telkom" address=36.85.220.0/22
add list="telkom" address=36.85.224.0/22
add list="telkom" address=36.85.228.0/22
add list="telkom" address=36.85.232.0/22
add list="telkom" address=36.85.236.0/23
add list="telkom" address=36.85.238.0/23
add list="telkom" address=36.85.240.0/23
add list="telkom" address=36.85.242.0/23
add list="telkom" address=36.85.244.0/23
add list="telkom" address=36.85.246.0/23
add list="telkom" address=36.85.248.0/21
add list="telkom" address=36.85.32.0/20
add list="telkom" address=36.85.48.0/20
add list="telkom" address=36.85.64.0/20
add list="telkom" address=36.85.80.0/23
add list="telkom" address=36.85.83.0/24
add list="telkom" address=36.85.84.0/24
add list="telkom" address=36.85.85.0/24
add list="telkom" address=36.85.86.0/23
add list="telkom" address=36.85.88.0/22
add list="telkom" address=36.85.92.0/23
add list="telkom" address=36.85.94.0/23
add list="telkom" address=36.85.96.0/22
add list="telkom" address=36.86.0.0/19
add list="telkom" address=36.86.192.0/18
add list="telkom" address=36.86.32.0/20
add list="telkom" address=36.86.52.0/23
add list="telkom" address=36.86.56.0/24
add list="telkom" address=36.86.58.0/23
add list="telkom" address=36.86.64.0/18
add list="telkom" address=36.87.128.0/18
add list="telkom" address=36.87.192.0/18
add list="telkom" address=36.87.32.0/19
add list="telkom" address=36.87.64.0/19
add list="telkom" address=36.88.0.0/18
add list="telkom" address=36.88.0.0/19
add list="telkom" address=36.88.128.0/19
add list="telkom" address=36.88.192.0/19
add list="telkom" address=36.88.224.0/19
add list="telkom" address=36.88.32.0/19
add list="telkom" address=36.88.64.0/19
add list="telkom" address=36.88.96.0/19
add list="telkom" address=36.89.0.0/24
add list="telkom" address=36.89.2.0/23
add list="telkom" address=36.89.220.0/24
add list="telkom" address=36.89.4.0/23
add list="telkom" address=36.90.0.0/16
add list="telkom" address=36.90.0.0/22
add list="telkom" address=36.90.100.0/22
add list="telkom" address=36.90.104.0/22
add list="telkom" address=36.90.108.0/22
add list="telkom" address=36.90.112.0/23
add list="telkom" address=36.90.114.0/23
add list="telkom" address=36.90.116.0/23
add list="telkom" address=36.90.118.0/23
add list="telkom" address=36.90.12.0/22
add list="telkom" address=36.90.122.0/23
add list="telkom" address=36.90.124.0/23
add list="telkom" address=36.90.126.0/23
add list="telkom" address=36.90.128.0/23
add list="telkom" address=36.90.130.0/23
add list="telkom" address=36.90.132.0/23
add list="telkom" address=36.90.134.0/23
add list="telkom" address=36.90.136.0/23
add list="telkom" address=36.90.138.0/23
add list="telkom" address=36.90.140.0/23
add list="telkom" address=36.90.142.0/23
add list="telkom" address=36.90.144.0/23
add list="telkom" address=36.90.146.0/23
add list="telkom" address=36.90.148.0/23
add list="telkom" address=36.90.150.0/23
add list="telkom" address=36.90.152.0/23
add list="telkom" address=36.90.154.0/23
add list="telkom" address=36.90.156.0/23
add list="telkom" address=36.90.158.0/23
add list="telkom" address=36.90.16.0/22
add list="telkom" address=36.90.160.0/23
add list="telkom" address=36.90.162.0/23
add list="telkom" address=36.90.164.0/23
add list="telkom" address=36.90.166.0/23
add list="telkom" address=36.90.168.0/23
add list="telkom" address=36.90.170.0/23
add list="telkom" address=36.90.172.0/23
add list="telkom" address=36.90.174.0/23
add list="telkom" address=36.90.176.0/22
add list="telkom" address=36.90.180.0/23
add list="telkom" address=36.90.182.0/23
add list="telkom" address=36.90.184.0/23
add list="telkom" address=36.90.186.0/23
add list="telkom" address=36.90.190.0/23
add list="telkom" address=36.90.192.0/23
add list="telkom" address=36.90.194.0/23
add list="telkom" address=36.90.196.0/22
add list="telkom" address=36.90.20.0/22
add list="telkom" address=36.90.200.0/23
add list="telkom" address=36.90.202.0/23
add list="telkom" address=36.90.204.0/23
add list="telkom" address=36.90.206.0/23
add list="telkom" address=36.90.208.0/23
add list="telkom" address=36.90.210.0/23
add list="telkom" address=36.90.214.0/23
add list="telkom" address=36.90.216.0/23
add list="telkom" address=36.90.218.0/23
add list="telkom" address=36.90.220.0/23
add list="telkom" address=36.90.222.0/23
add list="telkom" address=36.90.224.0/23
add list="telkom" address=36.90.226.0/23
add list="telkom" address=36.90.228.0/23
add list="telkom" address=36.90.230.0/23
add list="telkom" address=36.90.232.0/22
add list="telkom" address=36.90.236.0/23
add list="telkom" address=36.90.238.0/23
add list="telkom" address=36.90.24.0/22
add list="telkom" address=36.90.240.0/23
add list="telkom" address=36.90.242.0/23
add list="telkom" address=36.90.244.0/23
add list="telkom" address=36.90.246.0/23
add list="telkom" address=36.90.248.0/23
add list="telkom" address=36.90.250.0/23
add list="telkom" address=36.90.252.0/23
add list="telkom" address=36.90.254.0/23
add list="telkom" address=36.90.28.0/23
add list="telkom" address=36.90.30.0/23
add list="telkom" address=36.90.32.0/22
add list="telkom" address=36.90.36.0/22
add list="telkom" address=36.90.4.0/22
add list="telkom" address=36.90.40.0/22
add list="telkom" address=36.90.44.0/22
add list="telkom" address=36.90.48.0/22
add list="telkom" address=36.90.52.0/22
add list="telkom" address=36.90.56.0/22
add list="telkom" address=36.90.60.0/22
add list="telkom" address=36.90.64.0/22
add list="telkom" address=36.90.68.0/22
add list="telkom" address=36.90.72.0/22
add list="telkom" address=36.90.76.0/22
add list="telkom" address=36.90.8.0/22
add list="telkom" address=36.90.80.0/22
add list="telkom" address=36.90.84.0/22
add list="telkom" address=36.90.88.0/22
add list="telkom" address=36.90.92.0/23
add list="telkom" address=36.90.94.0/23
add list="telkom" address=36.90.96.0/22
add list="telkom" address=36.91.202.0/24
add list="telkom" address=36.91.217.0/24
add list="telkom" address=36.91.231.0/24
add list="telkom" address=36.91.232.0/24
add list="telkom" address=36.91.250.0/24
add list="telkom" address=36.92.158.0/24
add list="telkom" address=36.92.224.0/20
add list="telkom" address=36.92.227.0/24
add list="telkom" address=36.92.53.0/24
add list="telkom" address=36.93.0.0/16
add list="telkom" address=36.94.0.0/16
add list="telkom" address=36.94.131.0/24
add list="telkom" address=36.94.138.0/24
add list="telkom" address=36.94.144.0/24
add list="telkom" address=61.5.0.0/22
add list="telkom" address=61.5.100.0/22
add list="telkom" address=61.5.104.0/21
add list="telkom" address=61.5.112.0/22
add list="telkom" address=61.5.117.0/24
add list="telkom" address=61.5.120.0/21
add list="telkom" address=61.5.16.0/20
add list="telkom" address=61.5.32.0/21
add list="telkom" address=61.5.4.0/22
add list="telkom" address=61.5.44.0/22
add list="telkom" address=61.5.52.0/22
add list="telkom" address=61.5.57.0/24
add list="telkom" address=61.5.58.0/23
add list="telkom" address=61.5.60.0/22
add list="telkom" address=61.5.64.0/21
add list="telkom" address=61.5.72.0/22
add list="telkom" address=61.5.76.0/22
add list="telkom" address=61.5.8.0/22
add list="telkom" address=61.5.80.0/20
add list="telkom" address=61.5.96.0/23
add list="telkom" address=61.5.98.0/23
add list="telkom" address=61.94.100.0/22
add list="telkom" address=61.94.104.0/23
add list="telkom" address=61.94.108.0/23
add list="telkom" address=61.94.110.0/24
add list="telkom" address=61.94.112.0/24
add list="telkom" address=61.94.113.0/24
add list="telkom" address=61.94.118.0/23
add list="telkom" address=61.94.122.0/23
add list="telkom" address=61.94.124.0/22
add list="telkom" address=61.94.128.0/24
add list="telkom" address=61.94.131.0/24
add list="telkom" address=61.94.132.0/23
add list="telkom" address=61.94.135.0/24
add list="telkom" address=61.94.139.0/24
add list="telkom" address=61.94.140.0/23
add list="telkom" address=61.94.142.0/23
add list="telkom" address=61.94.145.0/24
add list="telkom" address=61.94.146.0/23
add list="telkom" address=61.94.148.0/22
add list="telkom" address=61.94.152.0/21
add list="telkom" address=61.94.16.0/22
add list="telkom" address=61.94.160.0/22
add list="telkom" address=61.94.164.0/23
add list="telkom" address=61.94.173.0/24
add list="telkom" address=61.94.174.0/23
add list="telkom" address=61.94.176.0/22
add list="telkom" address=61.94.182.0/24
add list="telkom" address=61.94.183.0/24
add list="telkom" address=61.94.184.0/24
add list="telkom" address=61.94.185.0/24
add list="telkom" address=61.94.187.0/24
add list="telkom" address=61.94.189.0/24
add list="telkom" address=61.94.190.0/24
add list="telkom" address=61.94.193.0/24
add list="telkom" address=61.94.194.0/24
add list="telkom" address=61.94.195.0/24
add list="telkom" address=61.94.198.0/23
add list="telkom" address=61.94.20.0/23
add list="telkom" address=61.94.205.0/24
add list="telkom" address=61.94.206.0/23
add list="telkom" address=61.94.208.0/24
add list="telkom" address=61.94.210.0/23
add list="telkom" address=61.94.212.0/22
add list="telkom" address=61.94.216.0/23
add list="telkom" address=61.94.220.0/23
add list="telkom" address=61.94.222.0/24
add list="telkom" address=61.94.225.0/24
add list="telkom" address=61.94.226.0/23
add list="telkom" address=61.94.228.0/24
add list="telkom" address=61.94.233.0/24
add list="telkom" address=61.94.234.0/24
add list="telkom" address=61.94.235.0/24
add list="telkom" address=61.94.236.0/24
add list="telkom" address=61.94.237.0/24
add list="telkom" address=61.94.238.0/23
add list="telkom" address=61.94.240.0/24
add list="telkom" address=61.94.242.0/23
add list="telkom" address=61.94.244.0/22
add list="telkom" address=61.94.248.0/23
add list="telkom" address=61.94.251.0/24
add list="telkom" address=61.94.252.0/23
add list="telkom" address=61.94.32.0/21
add list="telkom" address=61.94.40.0/22
add list="telkom" address=61.94.44.0/23
add list="telkom" address=61.94.46.0/24
add list="telkom" address=61.94.47.0/24
add list="telkom" address=61.94.49.0/24
add list="telkom" address=61.94.50.0/23
add list="telkom" address=61.94.52.0/22
add list="telkom" address=61.94.56.0/24
add list="telkom" address=61.94.58.0/24
add list="telkom" address=61.94.59.0/24
add list="telkom" address=61.94.60.0/22
add list="telkom" address=61.94.65.0/24
add list="telkom" address=61.94.66.0/23
add list="telkom" address=61.94.72.0/22
add list="telkom" address=61.94.74.0/23
add list="telkom" address=61.94.84.0/22
add list="telkom" address=61.94.88.0/22
add list="telkom" address=61.94.92.0/23
add list="telkom" address=61.94.94.0/24
add list="telkom" address=61.94.97.0/24
add list="telkom" address=61.94.98.0/24



File: /firewall address-list\Twitter address-list
#https://bgp.he.net/AS13414
#https://www.dan.me.uk/bgplookup


/ip firewall address-list


add list="twitter" address=103.252.112.0/23
add list="twitter" address=103.252.114.0/23
add list="twitter" address=104.244.40.0/24
add list="twitter" address=104.244.41.0/24
add list="twitter" address=104.244.42.0/24
add list="twitter" address=104.244.44.0/24
add list="twitter" address=104.244.45.0/24
add list="twitter" address=104.244.46.0/24
add list="twitter" address=104.244.47.0/24
add list="twitter" address=185.45.5.0/24
add list="twitter" address=185.45.6.0/23
add list="twitter" address=192.133.76.0/22
add list="twitter" address=192.133.76.0/23
add list="twitter" address=192.44.69.0/24
add list="twitter" address=199.16.156.0/22
add list="twitter" address=199.16.156.0/23
add list="twitter" address=199.59.148.0/22
add list="twitter" address=199.96.56.0/23
add list="twitter" address=199.96.56.0/24
add list="twitter" address=199.96.57.0/24
add list="twitter" address=199.96.58.0/23
add list="twitter" address=199.96.60.0/23
add list="twitter" address=199.96.60.0/24
add list="twitter" address=199.96.61.0/24
add list="twitter" address=199.96.62.0/23
add list="twitter" address=202.160.128.0/24
add list="twitter" address=202.160.129.0/24
add list="twitter" address=202.160.130.0/24
add list="twitter" address=202.160.131.0/24
add list="twitter" address=209.237.192.0/24
add list="twitter" address=209.237.193.0/24
add list="twitter" address=209.237.194.0/24
add list="twitter" address=209.237.195.0/24
add list="twitter" address=209.237.196.0/24
add list="twitter" address=209.237.198.0/24
add list="twitter" address=209.237.199.0/24
add list="twitter" address=209.237.200.0/24
add list="twitter" address=209.237.203.0/24
add list="twitter" address=209.237.204.0/24
add list="twitter" address=209.237.205.0/24
add list="twitter" address=209.237.206.0/24
add list="twitter" address=209.237.207.0/24
add list="twitter" address=209.237.208.0/24
add list="twitter" address=209.237.209.0/24
add list="twitter" address=209.237.210.0/24
add list="twitter" address=209.237.211.0/24
add list="twitter" address=209.237.212.0/24
add list="twitter" address=209.237.213.0/24
add list="twitter" address=209.237.214.0/24
add list="twitter" address=209.237.215.0/24
add list="twitter" address=209.237.216.0/24
add list="twitter" address=209.237.217.0/24
add list="twitter" address=209.237.218.0/24
add list="twitter" address=209.237.221.0/24
add list="twitter" address=209.237.222.0/24
add list="twitter" address=209.237.223.0/24
add list="twitter" address=64.63.0.0/18
add list="twitter" address=69.195.160.0/24
add list="twitter" address=69.195.162.0/24
add list="twitter" address=69.195.163.0/24
add list="twitter" address=69.195.164.0/24
add list="twitter" address=69.195.166.0/24
add list="twitter" address=69.195.168.0/24
add list="twitter" address=69.195.171.0/24
add list="twitter" address=69.195.172.0/24
add list="twitter" address=69.195.174.0/24
add list="twitter" address=69.195.175.0/24
add list="twitter" address=69.195.176.0/24
add list="twitter" address=69.195.177.0/24
add list="twitter" address=69.195.178.0/24
add list="twitter" address=69.195.179.0/24
add list="twitter" address=69.195.180.0/24
add list="twitter" address=69.195.181.0/24
add list="twitter" address=69.195.182.0/24
add list="twitter" address=69.195.184.0/24
add list="twitter" address=69.195.185.0/24
add list="twitter" address=69.195.186.0/24
add list="twitter" address=69.195.187.0/24
add list="twitter" address=69.195.188.0/24
add list="twitter" address=69.195.189.0/24
add list="twitter" address=69.195.190.0/24
add list="twitter" address=69.195.191.0/24


File: /README.md
# ngonfig-Mikrotik



