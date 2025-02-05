# Repository Information
Name: mikrotik-examples

# Directory Structure
Directory structure:
└── github_repos/mikrotik-examples/
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
    │   │       ├── pack-c1123be74964a320b73c3153e316c39d9ab1d53d.idx
    │   │       └── pack-c1123be74964a320b73c3153e316c39d9ab1d53d.pack
    │   ├── packed-refs
    │   └── refs/
    │       ├── heads/
    │       │   └── master
    │       ├── remotes/
    │       │   └── origin/
    │       │       └── HEAD
    │       └── tags/
    ├── .gitignore
    ├── ex1/
    │   ├── bck_20180803.backup
    │   ├── config.rsc
    │   └── README.md
    ├── ex2/
    │   ├── config.rsc
    │   ├── es.backup
    │   └── README.md
    ├── ex3/
    │   ├── config.rsc
    │   ├── es.backup
    │   └── README.md
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
	url = https://github.com/lparolari/mikrotik-examples.git
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
0000000000000000000000000000000000000000 562754a8202484eb14bd42a9588352d0bd79d4bf vivek-dodia <vivek.dodia@icloud.com> 1738606328 -0500	clone: from https://github.com/lparolari/mikrotik-examples.git


File: /.git\logs\refs\heads\master
0000000000000000000000000000000000000000 562754a8202484eb14bd42a9588352d0bd79d4bf vivek-dodia <vivek.dodia@icloud.com> 1738606328 -0500	clone: from https://github.com/lparolari/mikrotik-examples.git


File: /.git\logs\refs\remotes\origin\HEAD
0000000000000000000000000000000000000000 562754a8202484eb14bd42a9588352d0bd79d4bf vivek-dodia <vivek.dodia@icloud.com> 1738606328 -0500	clone: from https://github.com/lparolari/mikrotik-examples.git


File: /.git\packed-refs
# pack-refs with: peeled fully-peeled sorted 
562754a8202484eb14bd42a9588352d0bd79d4bf refs/remotes/origin/master


File: /.git\refs\heads\master
562754a8202484eb14bd42a9588352d0bd79d4bf


File: /.git\refs\remotes\origin\HEAD
ref: refs/remotes/origin/master


File: /.gitignore
*~
#*#
temp/


File: /ex1\config.rsc
# aug/02/2018 17:52:08 by RouterOS 6.41
# software id = L25Z-BUUK
#
# model = RouterBOARD mAP L-2nD
# serial number = 65D204E1796B
/interface ethernet
set [ find default-name=ether1 ] name=ether_wan
/interface wireless security-profiles
set [ find default=yes ] supplicant-identity=MikroTik
add authentication-types=wpa2-psk eap-methods="" management-protection=\
    allowed mode=dynamic-keys name=security_master supplicant-identity="" \
    wpa2-pre-shared-key=AAaa-0000
add eap-methods="" management-protection=allowed name=security_guest \
    supplicant-identity=""
/interface wireless
set [ find default-name=wlan1 ] disabled=no frequency=auto mode=ap-bridge \
    name=wireless_master security-profile=security_master ssid=Master \
    vlan-id=10 vlan-mode=use-tag
/interface vlan
add interface=wireless_master name=vlan_master vlan-id=10
/interface wireless
add disabled=no keepalive-frames=disabled mac-address=4E:5E:0C:14:47:C9 \
    master-interface=wireless_master multicast-buffering=disabled name=\
    wireless_guest security-profile=security_guest ssid=Guest vlan-id=20 \
    vlan-mode=use-tag wds-cost-range=0 wds-default-cost=0 wps-mode=disabled
/interface vlan
add interface=wireless_guest name=vlan_guest vlan-id=20
/ip hotspot
add disabled=no idle-timeout=1m interface=vlan_guest login-timeout=1m name=\
    hots_srv_guest
/ip hotspot profile
set [ find default=yes ] html-directory=flash/hotspot
/ip pool
add name=pool_master ranges=192.168.10.100-192.168.10.199
add name=pool_guest ranges=172.16.10.100-172.16.10.199
/ip dhcp-server
add address-pool=pool_master disabled=no interface=vlan_master name=\
    dhcp_master
add address-pool=pool_guest disabled=no interface=vlan_guest name=dhcp_guest
/queue simple
add max-limit=64k/1M name=queue_guest target=vlan_guest
/ip neighbor discovery-settings
set discover-interface-list=!dynamic
/ip address
add address=192.168.10.1/24 interface=vlan_master network=192.168.10.0
add address=172.16.10.1/16 interface=vlan_guest network=172.16.0.0
/ip dhcp-client
add dhcp-options=hostname,clientid disabled=no interface=ether_wan
/ip dhcp-server network
add address=172.16.0.0/16 dns-server=172.16.10.1 gateway=172.16.10.1 netmask=\
    16
add address=192.168.10.0/24 dns-server=192.168.10.1 gateway=192.168.10.1 \
    netmask=24
/ip dns
set allow-remote-requests=yes servers=8.8.8.8,8.8.4.4
/ip firewall filter
add action=passthrough chain=unused-hs-chain comment=\
    "place hotspot rules here" disabled=yes
/ip firewall nat
add action=passthrough chain=unused-hs-chain comment=\
    "place hotspot rules here" disabled=yes
add action=masquerade chain=srcnat out-interface=ether_wan src-address=\
    192.168.10.0/24
add action=masquerade chain=srcnat out-interface=ether_wan src-address=\
    172.16.10.0/24
add action=masquerade chain=srcnat comment="masquerade hotspot network" \
    src-address=172.16.0.0/16
/ip hotspot user
add name=admin password=123
add name=guest password=123 server=hots_srv_guest
/system clock
set time-zone-name=Europe/Rome


File: /ex1\README.md
# Exercise 1

Create a wan connection over eth1; connection is provided by another
devices with dhcp server enabled. This configuration will get the ip
with a dhcp client.

Add two networks over wifi: one for guests and one for offices. For
both network use a vlan with tagged property, but for the guest
network use a /16 class with free access and right bandwidth limits,
while for the other use /24 class with protected access and all
bandwidth.

Then use a nat to allow both wifi networks to navigate on the
internet.


File: /ex2\config.rsc
# aug/03/2018 06:45:37 by RouterOS 6.41
# software id = L25Z-BUUK
#
# model = RouterBOARD mAP L-2nD
# serial number = 65D204E1796B
/interface wireless security-profiles
set [ find default=yes ] supplicant-identity=MikroTik
add authentication-types=wpa-psk,wpa2-psk eap-methods="" \
    management-protection=allowed mode=dynamic-keys name=sec_parolari \
    supplicant-identity="" wpa-pre-shared-key=davideluca wpa2-pre-shared-key=\
    davideluca
/interface wireless
set [ find default-name=wlan1 ] band=2ghz-b/g/n disabled=no frequency=2462 \
    security-profile=sec_parolari ssid=WiFi-Parolari
/ip pool
add name=pool_dhcp_wan ranges=192.168.10.100-192.168.10.199
/ip dhcp-server
add address-pool=pool_dhcp_wan disabled=no interface=ether1 name=dhcp_srv_wan
/ip neighbor discovery-settings
set discover-interface-list=!dynamic
/ip address
add address=192.168.10.1/24 interface=ether1 network=192.168.10.0
/ip dhcp-client
add dhcp-options=hostname,clientid disabled=no interface=wlan1
/ip dhcp-server network
add address=192.168.10.0/24 gateway=192.168.10.1 netmask=24
/ip firewall nat
add action=masquerade chain=srcnat out-interface=wlan1 src-address=\
    192.168.10.0/24
/system clock
set time-zone-name=Europe/Rome


File: /ex2\README.md
# Execise 2
Configure the router in order to pick the wifi connection of an
already working access point and use this connection over the eth
interface.

## Example

### Scenario
You have a server, but you cannot connect it to the network throught
wire. However, you must connect it to the network.

### Question
How would you do it?

### Answer
You can take a router with a wlan interface and a eth interface and
configure it in order to pick the network connection from the access
point, using a dhcp client which gets the ip from the network. Than
you must create a security profile matching the existent security
profile of the network.  After that you have only to configure a
network for the eth interface and nat the out interface to the wlan
interface.


File: /ex3\config.rsc
# aug/13/2018 11:05:19 by RouterOS 6.41
# software id = L25Z-BUUK
#
# model = RouterBOARD mAP L-2nD
# serial number = 65D204E1796B
/interface wireless
set [ find default-name=wlan1 ] frequency=auto mode=ap-bridge ssid=MikroTik
/interface wireless security-profiles
set [ find default=yes ] supplicant-identity=MikroTik
/ip hotspot profile
set [ find default=yes ] html-directory=flash/hotspot
/ip pool
add name=pool1 ranges=192.168.10.100-192.168.10.199
add name=pool2 ranges=192.168.20.100-192.168.20.199
/ip dhcp-server
add address-pool=pool1 disabled=no interface=ether1 name=server1
add address-pool=pool2 disabled=no interface=wlan1 name=server2
/ip neighbor discovery-settings
set discover-interface-list=!dynamic
/ip address
add address=192.168.10.1/24 interface=ether1 network=192.168.10.0
add address=192.168.20.1/24 interface=wlan1 network=192.168.20.0
/ip dhcp-server network
add address=192.168.10.0/24 dns-server=192.168.10.1 gateway=192.168.10.1 \
    netmask=24
add address=192.168.20.0/24 dns-server=192.168.20.1 gateway=192.168.20.1 \
    netmask=24
/ip firewall filter
add action=drop chain=forward comment="FORWARD_CHAIN (do not enable)" \
    disabled=yes
add action=accept chain=forward comment=accept_199_to199 dst-address=\
    192.168.10.199 src-address=192.168.20.199
add action=drop chain=forward comment=drop_lan_to_lan7 dst-address=\
    192.168.10.0/24 src-address=192.168.20.0/24
add action=drop chain=forward dst-address=192.168.20.0/24 src-address=\
    192.168.10.0/24
add action=drop chain=forward comment=drop_boggon_ip src-address=0.0.0.0/8
add action=drop chain=forward dst-address=0.0.0.0/8
add action=drop chain=forward src-address=127.0.0.0/8
add action=drop chain=forward dst-address=127.0.0.0/8
add action=drop chain=forward src-address=224.0.0.0/3
add action=drop chain=forward dst-address=224.0.0.0/3
add action=drop chain=input comment="INPUT_CHAIN (do not enable)" disabled=\
    yes
add action=accept chain=input comment=accept_trusted in-interface=!ether1 \
    src-address=192.168.0.0/24
add action=drop chain=input comment=drop_invalid_connections \
    connection-state=invalid
add action=drop chain=input comment=drop_dhcp_relay dst-port=53 protocol=udp \
    src-port=""
add action=accept chain=input comment=accept_known_connections \
    connection-state=established,related
add action=accept chain=input comment=accept_mikrotik_connections dst-port=\
    58291 protocol=tcp
add action=drop chain=input comment=drop_everything_else
add action=drop chain=output comment="OUTPUT_CHAIN (do not enable)" disabled=\
    yes
add action=accept chain=output comment=accept_everything
add action=drop chain=tcp comment="TCP_CHAIN (do not enable)" disabled=yes
add action=drop chain=tcp comment=drop_tftp dst-port=69 protocol=tcp
add action=drop chain=tcp comment=drop_rpc_portmapper dst-port=111 protocol=\
    tcp
add action=drop chain=tcp dst-port=135 protocol=tcp
add action=drop chain=tcp comment=drop_netbios dst-port=137-139 protocol=tcp
add action=drop chain=tcp comment=drop_cifs dst-port=445 protocol=tcp
add action=drop chain=tcp comment=drop_nfs dst-port=2049 protocol=tcp
add action=drop chain=tcp comment=drop_netbus dst-port=12345-12346 protocol=\
    tcp
add action=drop chain=tcp dst-port=20034 protocol=tcp
add action=drop chain=tcp comment=drop_backoriffice dst-port=3133 protocol=\
    tcp
add action=drop chain=udp comment="UDP_CHAIN (do not enable)" disabled=yes
add action=drop chain=udp comment=drop_tftp dst-port=69 protocol=udp
add action=drop chain=udp comment=drop_prc_portmapper dst-port=111 protocol=\
    udp
add action=drop chain=udp comment=drop_prc_portmapper dst-port=135 protocol=\
    udp
add action=drop chain=udp comment=drop_nbt dst-port=137-139 protocol=udp
add action=drop chain=udp comment=drop_nfs dst-port=2049 protocol=udp
add action=drop chain=udp comment=drop_backoriffice dst-port=3133 protocol=\
    udp
add action=drop chain=icmp comment="ICMP_CHAIN (do not enable)" disabled=yes
add action=accept chain=icmp comment=accept_icmp_echo_replay icmp-options=0:0 \
    protocol=icmp
add action=accept chain=icmp comment=accept_icmp_net_unreachable \
    icmp-options=3:0 protocol=icmp
add action=accept chain=icmp comment=accept_icmp_host_unreachable \
    icmp-options=3:1 protocol=icmp
add action=accept chain=icmp comment=\
    accept_icmp_host_unreachable_fragmentation_required icmp-options=3:4 \
    protocol=icmp
add action=accept chain=icmp comment=accept_icmp_source_quench icmp-options=\
    4:0 protocol=icmp
add action=accept chain=icmp comment=accept_icmp_echo_request icmp-options=\
    8:0 protocol=icmp
add action=accept chain=icmp comment=accept_icmp_time_exceed icmp-options=\
    11:0 protocol=icmp
add action=accept chain=icmp comment=accept_icmp_parameter_bad icmp-options=\
    12:0 protocol=icmp
add action=drop chain=icmp comment=drop_everything_else
/ip firewall nat
add action=masquerade chain=srcnat disabled=yes dst-port=58291 protocol=tcp
/ip service
set winbox port=58291
/snmp
set contact=test enabled=yes location=Luca trap-generators=start-trap \
    trap-interfaces=all
/system clock
set time-zone-name=Europe/Rome


File: /ex3\README.md
# Execise 3
Configure the router to create a set of firewall rules.



File: /README.md
# MikroTik and RouterOS examples

This repository contains a collection of simple example and exercises for MikroTik systems using Router OS.

Exercises are made for learning purposes: some details can be neglected and the examples are purposely trivial.

If this material helped you please star this repo! Your simple click is a big thanks for me!

### Usage
In every exercise' directory you will find:
- a README that will explai the exercise and the adopted solution;
- a `.backup` file which you can use to restore the whole router's configuration;
- a `.rsc` file which you can use to load only the exported configuration.

### Download
```
git clone https://github.com/lparolari/mikrotik-examples.git
cd mikrotik-examples
```

## Author(s)

Luca Parolari <luca.parolari23@gmail.com> (Student of Computer Science at University of Parma, Italy)

Antonio Toselli <antonio.toselli@gmail.com> (My tutor, the exercises' creator)


