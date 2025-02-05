# Repository Information
Name: mikrotik-kpn-xs4all

# Directory Structure
Directory structure:
└── github_repos/mikrotik-kpn-xs4all/
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
    │   │       ├── pack-ee4ca375940943c5445fc1551026227e46caa8de.idx
    │   │       └── pack-ee4ca375940943c5445fc1551026227e46caa8de.pack
    │   ├── packed-refs
    │   └── refs/
    │       ├── heads/
    │       │   └── main
    │       ├── remotes/
    │       │   └── origin/
    │       │       └── HEAD
    │       └── tags/
    ├── config-masterrouter.rsc
    ├── config-switchap.rsc
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
	url = https://github.com/shoop/mikrotik-kpn-xs4all.git
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
0000000000000000000000000000000000000000 ca738dee1f3cb5484fbc8e837ea6258647a30bd9 vivek-dodia <vivek.dodia@icloud.com> 1738606462 -0500	clone: from https://github.com/shoop/mikrotik-kpn-xs4all.git


File: /.git\logs\refs\heads\main
0000000000000000000000000000000000000000 ca738dee1f3cb5484fbc8e837ea6258647a30bd9 vivek-dodia <vivek.dodia@icloud.com> 1738606462 -0500	clone: from https://github.com/shoop/mikrotik-kpn-xs4all.git


File: /.git\logs\refs\remotes\origin\HEAD
0000000000000000000000000000000000000000 ca738dee1f3cb5484fbc8e837ea6258647a30bd9 vivek-dodia <vivek.dodia@icloud.com> 1738606462 -0500	clone: from https://github.com/shoop/mikrotik-kpn-xs4all.git


File: /.git\packed-refs
# pack-refs with: peeled fully-peeled sorted 
ca738dee1f3cb5484fbc8e837ea6258647a30bd9 refs/remotes/origin/main


File: /.git\refs\heads\main
ca738dee1f3cb5484fbc8e837ea6258647a30bd9


File: /.git\refs\remotes\origin\HEAD
ref: refs/remotes/origin/main


File: /config-masterrouter.rsc
# model = RB4011iGS+

#============================================================================
# RB4011iGS+ configuration
#
# Underlying decisions:
# - Home use with a number of statically allocated wired devices.
# - Configured for xs4all/KPN internet provider with IPTV, using
#   fiber to the home with GPON, so upstream interface is the SFP+.
# - Multiple switch/APs present on different floors of the house,
#   managed by CAPsMAN.
# - Separate VLAN for wireless guest network.
# - Separate VLAN for a stable IPTV setup.
# - Dual stack IPv4 and IPV6 ready.
# - Provide DHCPv4 service on all VLANs.
# - IPv6 configuration using SLAAC.
# - Provide home-local DNS service according to RFC 8375.
#
# Potential future expansions:
# - NTP server
# - TFTP server
# - 802.1x RADIUS server (not yet supported by MikroTik)
#
# The configuration below is in order of /export . Note that re-ordering
# may mess with the ability to reload this configuration.
#
# Reload of the configuration after factory reset:
# 1. Ensure the ipv6 and multicast packages are installed
# 2. Upload script to internal router memory
# 3. /system reset-configuration no-defaults=yes run-after-reset=<<SCRIPT>>
#============================================================================

# AP channel definitions.
# Check your area with the snooper tool:
#   /interface wireless snooper
#   https://wiki.mikrotik.com/wiki/Manual:Interface/Wireless#Snooper
/caps-man channel
add band=2ghz-g/n control-channel-width=20mhz extension-channel=disabled \
    frequency=2462 name=f-2462
add band=5ghz-n/ac control-channel-width=20mhz extension-channel=Ceee \
    frequency=5500 name=f-5500

# AP data path definitions.
# Uses local forwarding as home use does not need accounting of all data.
/caps-man datapath
add client-to-client-forwarding=yes local-forwarding=yes name=lan-10 vlan-id=\
    10 vlan-mode=use-tag
add client-to-client-forwarding=no local-forwarding=yes name=guest-30 \
    vlan-id=30 vlan-mode=use-tag

# Add the single bridge interface used for all ports.
# - Recommended is to set a static MAC, especially for CAPsMAN managed
#   interfaces.
# - Ensure that the "CPU" interface is also part of the normal
#   LAN VLAN 10 by setting pvid property.
# - Enable igmp-snooping for IPTV service.
/interface bridge
add admin-mac=<<MAC-OF-FIRST-PORT>> auto-mac=no fast-forward=no igmp-snooping=yes \
    name=bridge-lan pvid=10 vlan-filtering=yes

# Do not enable auto-negotiation. The RB4011 software v6.47.10 has a bug
# where the interface shows that it is connected, however no packets are
# actually sent out. See (Dutch):
#   https://gathering.tweakers.net/forum/list_message/67936436#67936436
# The MTU is set because of the ISP PPPoE requirements.
/interface ethernet
set [ find default-name=sfp-sfpplus1 ] arp=reply-only auto-negotiation=no \
    l2mtu=1596 loop-protect=off mtu=1512 speed=1Gbps

# Add the three different internal VLANs
/interface vlan
add interface=bridge-lan name=guest-30 vlan-id=30
add interface=bridge-lan name=iptv-20 vlan-id=20
add interface=bridge-lan name=lan-10 vlan-id=10

# Add the ISP mandated VLANs as coming in on the fiber line.
add interface=sfp-sfpplus1 name=xs4all-iptv-4 vlan-id=4
add interface=sfp-sfpplus1 loop-protect=off name=xs4all-wan-6 vlan-id=6

# AP rate definition.
/caps-man rates
add basic=6Mbps,12Mbps,24Mbps name=rate1 supported=\
    6Mbps,9Mbps,12Mbps,18Mbps,24Mbps,36Mbps,48Mbps,54Mbps

# AP security definitions.
/caps-man security
add authentication-types=wpa2-psk encryption=aes-ccm group-encryption=aes-ccm \
    name=<<SSID>> passphrase=<<PASSPHRASE>>
add authentication-types=wpa2-psk encryption=aes-ccm group-encryption=aes-ccm \
    name=<<GUESTSSID>> passphrase=<<GUESTPASSPHRASE>>

# AP configurations.
# Note that CAPsMAN configurations are layered, so the configuration for the
# guest network only specifies the properties to change relative to both of
# the base network configurations.
/caps-man configuration
add channel=f-2462 country=netherlands datapath=lan-10 distance=indoors \
    hw-retries=3 installation=indoor mode=ap multicast-helper=full name=\
    conf-2ghz rates=rate1 security=<<SSID>> ssid=<<SSID>>
add datapath=guest-30 name=conf-guest rates=rate1 security=<<GUESTSSID>> ssid=\
    <<GUESTSSID>>
add channel=f-5500 country=netherlands datapath=lan-10 distance=indoors \
    hw-retries=3 installation=indoor mode=ap multicast-helper=full name=\
    conf-5ghz rates=rate1 security=<<SSID>> ssid=<<SSID>>

# Switch port definitions.
# This is related to the older MikroTik VLAN definitions. It is not necessary
# when using Bridge VLAN configuration as we do, however these settings
# always appear in exports.
/interface ethernet switch port
set 0 default-vlan-id=0
set 1 default-vlan-id=0
set 2 default-vlan-id=0
set 3 default-vlan-id=0
set 4 default-vlan-id=0
set 5 default-vlan-id=0
set 6 default-vlan-id=0
set 7 default-vlan-id=0
set 8 default-vlan-id=0
set 9 default-vlan-id=0
set 10 default-vlan-id=0
set 11 default-vlan-id=0

# Add different lists for the interfaces to be able to set up firewall rules.
/interface list
add name=WAN
add name=LAN
add name=GUEST

# Set this routers wireless interface identity.
# This line is always present in exports, but has no effect as the RB4011iGS
# does not have any wireless interfaces.
/interface wireless security-profiles
set [ find default=yes ] supplicant-identity=MikroTik

# Add DHCP client and server options necessary for the STB.
/ip dhcp-client option
add code=60 name=option60-vendorclass value="'IPTV_RG'"
/ip dhcp-server option
add code=60 name=option60-vendorclass value="'IPTV_RG'"
add code=28 name=option28-broadcast value="'192.168.20.255'"

# Add DHCP server option for the trusted LAN. Conforms to RFC 8375.
# Note that the binary prefixes correspond to the length of the
# string following, adjust if needed.
add code=119 name=option119-domainsearch value=\
    "0x07'example'0x04'home'0x04'arpa'0x00"

# Combine the options for the STB into an option set for easy reference.
/ip dhcp-server option sets
add name=IPTV options=option60-vendorclass,option28-broadcast

# Define DHCP server IP pools for each VLAN.
/ip pool
add name=dhcp-lan-10 ranges=192.168.10.50-192.168.10.199
add name=dhcp-iptv-20 ranges=192.168.20.50-192.168.20.199
add name=dhcp-guest-30 ranges=192.168.30.50-192.168.30.199

# Setup DHCP server for each VLAN.
# Note that technically the IPTV VLAN could have been setup
# as a static-only server. For testing purposes it is easier
# to also be able to connect a laptop and check connectivity.
/ip dhcp-server
add address-pool=dhcp-lan-10 disabled=no interface=lan-10 name=\
    dhcp-server-lan-10
add address-pool=dhcp-iptv-20 disabled=no interface=iptv-20 name=\
    dhcp-server-iptv-20
add address-pool=dhcp-guest-30 disabled=no interface=guest-30 name=\
    dhcp-server-guest-30

# Add IPv6 DHCP server options to ensure that the router is advertised
# as the DNS server, and that IPv6 only devices also get the correct
# DNS search domain. Note that this implies the setup of a unique ULA,
# below in the IPv6 pool definition.
/ipv6 dhcp-server option
add code=23 name=option23-dnsserver value="'<<ULA-PREFIX>>::1'"
add code=24 name=option24-domainsearch value=\
    "0x07'example'0x04'home'0x04'arpa'0x00"

# Setup a unique local address for IPv6, as per the following blog post:
#   https://blog.apnic.net/2020/05/20/getting-ipv6-private-addressing-right/
# Generated using
#   https://www.ip-six.de/
/ipv6 pool
add name=ula-pool prefix=<<ULA-PREFIX>>::/64 prefix-length=64

# Set the PPP profile used by the PPPoE client to also use IPv6.
/ppp profile
set *0 only-one=yes use-compression=yes use-ipv6=no use-upnp=no
add name=default-ipv6 only-one=yes use-compression=yes use-upnp=no

# xs4all/KPN configuration to request WAN connectivity using PPPoE
# on VLAN 6 on the fiber interface. All WAN traffic is tunneled
# using this PPPoE connection.
/interface pppoe-client
add add-default-route=yes allow=pap disabled=no interface=xs4all-wan-6 \
    keepalive-timeout=20 max-mru=1500 max-mtu=1500 name=\
    xs4all-wan-pppoe-client password=internet profile=default-ipv6 \
    use-peer-dns=yes user=internet

# Disable BGP routing.
/routing bgp instance
set default disabled=yes

# AP client access list.
# These rules ensure that clients switch to another AP if the signal is
# too weak.
/caps-man access-list
add action=accept allow-signal-out-of-range=10s disabled=no interface=any \
    signal-range=-85..-10 ssid-regexp=""
add action=reject allow-signal-out-of-range=10s disabled=no interface=any \
    signal-range=-120..-86 ssid-regexp=""

# Enable CAPsMAN management of APs.
/caps-man manager
set enabled=yes

# Provision the APs around the house.
# Repeat the two rules for every AP using the wlan1/wlan2 MAC addresses.
/caps-man provisioning
add action=create-dynamic-enabled master-configuration=conf-2ghz radio-mac=\
    <<AP1-WLAN1-MAC>> slave-configurations=conf-guest
add action=create-dynamic-enabled master-configuration=conf-5ghz radio-mac=\
    <<AP1-WLAN2-MAC>> slave-configurations=conf-guest

# Add the bridge ports with VLAN configuration.
# First three Ethernet ports are TRUNK ports where the APs are connected.
# The last Ethernet port (10) connects the STB for IPTV.
# The rest is part of the regular LAN.
# Note that we could have chosen to use untagged VLAN for the normal LAN
# as trunk port security cannot be guaranteed in a normal home. However
# this makes it harder to provide e.g. DHCP services from the router so
# we go for tagged traffic up until each access port.
/interface bridge port
add bridge=bridge-lan comment=TRUNK frame-types=admit-only-vlan-tagged \
    ingress-filtering=yes interface=ether1
add bridge=bridge-lan comment=TRUNK frame-types=admit-only-vlan-tagged \
    ingress-filtering=yes interface=ether2
add bridge=bridge-lan comment=TRUNK frame-types=admit-only-vlan-tagged \
    ingress-filtering=yes interface=ether3
add bridge=bridge-lan comment=LAN interface=ether4 pvid=10
add bridge=bridge-lan comment=LAN interface=ether5 pvid=10
add bridge=bridge-lan comment=LAN interface=ether6 pvid=10
add bridge=bridge-lan comment=LAN interface=ether7 pvid=10
add bridge=bridge-lan comment=LAN interface=ether8 pvid=10
add bridge=bridge-lan comment=LAN interface=ether9 pvid=10
add bridge=bridge-lan comment=IPTV interface=ether10 pvid=20

# Allow discovery. The security risks in a home environment are minimal.
# Due to the use of the LAN list, the GUEST network is excluded.
/ip neighbor discovery-settings
set discover-interface-list=LAN

# Set bridge trunk/access port configuration. Ensure that the bridge-lan
# interface itself is part of the tagged list so that services such as
# DHCP can run per VLAN.
/interface bridge vlan
add bridge=bridge-lan tagged=bridge-lan,ether1,ether2,ether3 untagged=\
    ether4,ether5,ether6,ether7,ether8,ether9 vlan-ids=10
add bridge=bridge-lan tagged=bridge-lan,ether1,ether2,ether3 untagged=ether10 \
    vlan-ids=20
add bridge=bridge-lan tagged=bridge-lan,ether1,ether2,ether3 vlan-ids=30

# Add the correct interfaces to each list, for security.
# Note that IPTV is combined with LAN, for simplicities sake. For a home
# environment, the STB is not anymore dangerous than any other device.
/interface list member
add interface=sfp-sfpplus1 list=WAN
add interface=lan-10 list=LAN
add interface=iptv-20 list=LAN
add interface=guest-30 list=GUEST

# Add gateway IP addresses per VLAN.
/ip address
add address=192.168.10.1/24 comment=LAN interface=lan-10 network=192.168.10.0
add address=192.168.20.1/24 comment=IPTV interface=iptv-20 network=\
    192.168.20.0
add address=192.168.30.1/24 comment=GUEST interface=guest-30 network=\
    192.168.30.0

# Set the IPTV DHCP client as per xs4all/KPN ISP requirements.
# The routes provided by the DHCP offer should be ignored, hence the high
# default route distance.
/ip dhcp-client
add default-route-distance=210 dhcp-options=option60-vendorclass disabled=no \
    interface=xs4all-iptv-4 use-peer-dns=no use-peer-ntp=no

# Add static DHCP server leases for the wired connected devices in the home.
# This is a preference, there is no real need to do so.
/ip dhcp-server lease
add address=192.168.20.20 comment=stb.example.home.arpa mac-address=\
    <<MAC-OF-STB>> server=dhcp-server-iptv-20
add address=192.168.10.20 comment=fixed.example.home.arpa mac-address=\
    <<MAC-OF-FIXED-SERVICE>> server=dhcp-server-lan-10

# Add a DHCP server for each VLAN. Note that this requires that the
# traffic generated from the router itself is tagged by including the
# bridge interface in the list of tagged ports.
# Note that the IPTV VLAN will be using the upstream DNS servers directly.
# The GUEST VLAN will be using Google/Cloudflare DNS servers directly.
/ip dhcp-server network
add address=192.168.10.0/24 comment=lan-10 dhcp-option=option119-domainsearch \
    dns-server=192.168.10.1 gateway=192.168.10.1
add address=192.168.20.0/24 comment=iptv-20 dns-server=\
    194.109.6.66,194.109.9.99 gateway=192.168.20.1
add address=192.168.30.0/24 comment=guest-30 dns-server=8.8.8.8,1.1.1.1 \
    gateway=192.168.30.1

# Set up DNS service for the home LAN, using the upstream servers.
/ip dns
set allow-remote-requests=yes cache-max-ttl=1d servers=\
    194.109.6.66,194.109.9.99,2001:888:0:6::66,2001:888:0:9::99

# Add static DNS entries.
# Just like static DHCP leases, this is not entirely necessary,
# rather just convenient.
/ip dns static
add address=192.168.10.20 name=fixed.example.home.arpa
add address=192.168.20.20 name=stb.example.home.arpa

# IPv4 firewall rules.
# Based on the default rules, with the addition of IPTV and SSH
# service rules.
/ip firewall filter
add action=fasttrack-connection chain=forward comment="DEF: fasttrack" \
    connection-state=established,related
add action=accept chain=input comment=\
    "DEF: accept established,related,untracked" connection-state=\
    established,related,untracked
add action=accept chain=forward comment=\
    "DEF: accept established,related, untracked" connection-state=\
    established,related,untracked
add action=accept chain=input comment="DEF: accept ICMP" protocol=icmp

# IPTV requires IGMP and UDP traffic.
# TODO: the forward rule is now rather broad, due to a lot of
#       experimenting and failures with the STB. It can probably
#       be narrowed.
add action=accept chain=input comment="IPTV Multicast" dst-address=\
    224.0.0.0/8 in-interface=xs4all-iptv-4 protocol=igmp
add action=accept chain=input comment="IPTV Multicast" dst-address=\
    224.0.0.0/8 in-interface=xs4all-iptv-4 protocol=udp
add action=accept chain=forward comment="IPTV traffic" in-interface=\
    xs4all-iptv-4

add action=drop chain=input comment="DEF: drop invalid" connection-state=\
    invalid

# TODO: this rule is only necessary for devices with wireless capability,
#       so that CAPsMAN can manage the device itself. It does not hurt,
#       but should probably be removed.
add action=accept chain=input comment=\
    "DEF: accept to local loopback (for CAPsMAN)" dst-address=127.0.0.1

# Allow SSH access on the non-standard port, from the LAN.
# Using static DHCP/IP entries this can be limited even more, but once
# an attacker is in the LAN network and able to probe user/pass there
# are bigger problems.
add action=accept chain=input comment="Allow SSH to MikroTik from LAN" \
    dst-address=192.168.10.1 dst-port=2222 in-interface-list=LAN protocol=tcp

add action=drop chain=input comment="DEF: drop all not coming from LAN" \
    in-interface-list=!LAN log=yes

# TODO: these next two IPSEC policy rules are default. Not sure why, and
#       whether they are needed.
add action=accept chain=forward comment="DEF: accept in ipsec policy" \
    ipsec-policy=in,ipsec
add action=accept chain=forward comment="DEF: accept out ipsec policy" \
    ipsec-policy=out,ipsec

add action=drop chain=forward comment="DEF: drop invalid" connection-state=\
    invalid
add action=drop chain=forward comment="DEF: drop all from WAN not DSTNATed" \
    connection-nat-state=!dstnat connection-state=new in-interface-list=WAN \
    log=yes

# Ensure WAN traffic is correctly NATted.
/ip firewall nat
add action=masquerade chain=srcnat comment="IPTV masquerade" out-interface=\
    xs4all-iptv-4
add action=masquerade chain=srcnat comment="WAN masquerade" ipsec-policy=\
    out,none out-interface=xs4all-wan-pppoe-client

# Disable unnecessary services. Set SSH to port 2222 to avoid conflict
# with port 22 on the outside.
/ip service
set telnet disabled=yes
set ftp disabled=yes
set www disabled=yes
set ssh address=192.168.10.0/24 port=2222
set api disabled=yes
set winbox disabled=yes
set api-ssl disabled=yes

# Enable better SSH crypto.
/ip ssh
set strong-crypto=yes

# Ensure UPnP is disabled.
/ip upnp
set enabled=no

# Add IPv6 address as assigned by ISP. This will be requested using DHCPv6.
/ipv6 address
add address=::1 from-pool=ISP interface=lan-10

# Add IPv6 address from the ULA pool defined above.
add address=<<ULA-PREFIX>>::1 comment="IPv6 ULA address" interface=lan-10

# Setup DHCPv6 request on established PPPoE connection from ISP.
/ipv6 dhcp-client
add add-default-route=yes interface=xs4all-wan-pppoe-client pool-name=ISP \
    pool-prefix-length=48 request=prefix use-peer-dns=no

# Add a stateless DHCPv6 server that will respond with IPv6 address of
# DNS server, and the correct domain search option.
/ipv6 dhcp-server
add dhcp-option=option23-dnsserver,option24-domainsearch interface=lan-10 \
    name=ipv6-dns-advertisement

# Add default IPv6 firewall.
/ipv6 firewall address-list
add address=::/128 comment="defconf: unspecified address" list=bad_ipv6
add address=::1/128 comment="defconf: lo" list=bad_ipv6
add address=fec0::/10 comment="defconf: site-local" list=bad_ipv6
add address=::ffff:0.0.0.0/96 comment="defconf: ipv4-mapped" list=bad_ipv6
add address=::/96 comment="defconf: ipv4 compat" list=bad_ipv6
add address=100::/64 comment="defconf: discard only " list=bad_ipv6
add address=2001:db8::/32 comment="defconf: documentation" list=bad_ipv6
add address=2001:10::/28 comment="defconf: ORCHID" list=bad_ipv6
add address=3ffe::/16 comment="defconf: 6bone" list=bad_ipv6
add address=::224.0.0.0/100 comment="defconf: other" list=bad_ipv6
add address=::127.0.0.0/104 comment="defconf: other" list=bad_ipv6
add address=::/104 comment="defconf: other" list=bad_ipv6
add address=::255.0.0.0/104 comment="defconf: other" list=bad_ipv6
/ipv6 firewall filter
add action=accept chain=input comment=\
    "defconf: accept established,related,untracked" connection-state=\
    established,related,untracked
add action=drop chain=input comment="defconf: drop invalid" connection-state=\
    invalid
add action=accept chain=input comment="defconf: accept ICMPv6" protocol=\
    icmpv6
add action=accept chain=input comment="defconf: accept UDP traceroute" port=\
    33434-33534 protocol=udp
add action=accept chain=input comment=\
    "defconf: accept DHCPv6-Client prefix delegation." dst-port=546 protocol=\
    udp src-address=fe80::/10
add action=accept chain=input comment="defconf: accept IKE" dst-port=500,4500 \
    protocol=udp
add action=accept chain=input comment="defconf: accept ipsec AH" protocol=\
    ipsec-ah
add action=accept chain=input comment="defconf: accept ipsec ESP" protocol=\
    ipsec-esp
add action=accept chain=input comment=\
    "defconf: accept all that matches ipsec policy" ipsec-policy=in,ipsec
add action=drop chain=input comment=\
    "defconf: drop everything else not coming from LAN" in-interface-list=\
    !LAN
add action=accept chain=forward comment=\
    "defconf: accept established,related,untracked" connection-state=\
    established,related,untracked
add action=drop chain=forward comment="defconf: drop invalid" \
    connection-state=invalid
add action=drop chain=forward comment=\
    "defconf: drop packets with bad src ipv6" src-address-list=bad_ipv6
add action=drop chain=forward comment=\
    "defconf: drop packets with bad dst ipv6" dst-address-list=bad_ipv6
add action=drop chain=forward comment="defconf: rfc4890 drop hop-limit=1" \
    hop-limit=equal:1 protocol=icmpv6
add action=accept chain=forward comment="defconf: accept ICMPv6" protocol=\
    icmpv6
add action=accept chain=forward comment="defconf: accept HIP" protocol=139
add action=accept chain=forward comment="defconf: accept IKE" dst-port=\
    500,4500 protocol=udp
add action=accept chain=forward comment="defconf: accept ipsec AH" protocol=\
    ipsec-ah
add action=accept chain=forward comment="defconf: accept ipsec ESP" protocol=\
    ipsec-esp
add action=accept chain=forward comment=\
    "defconf: accept all that matches ipsec policy" ipsec-policy=in,ipsec
add action=drop chain=forward comment=\
    "defconf: drop everything else not coming from LAN" in-interface-list=\
    !LAN

# Setup IPv6 SLAAC on the LAN VLAN. The DNS server and domain search list
# will be requested by clients using DHCPv6 because of the other-configuration
# setting.
/ipv6 nd
set [ find default=yes ] disabled=yes
add advertise-dns=no advertise-mac-address=no hop-limit=64 interface=lan-10 \
    other-configuration=yes

# Set IGMP proxy for the IPTV subnet. Quick leave is on as currently there is
# only one STB connected.
/routing igmp-proxy
set quick-leave=yes

# Set the IGMP proxy upstream and downstream interfaces.
# TODO: test whether we can use 0.0.0.0/0 as alternative-subnets. The explicit
#       xs4all/KPN IP ranges are set due to a lot of experimenting and failures
#       with the STB.
/routing igmp-proxy interface
add alternative-subnets=217.166.0.0/16,213.75.0.0/16,10.29.0.0/18 interface=\
    xs4all-iptv-4 upstream=yes
add interface=iptv-20

# Set the time zone. This is actually automatically set by the default
# /ip cloud set update-time=yes setting, however it appears in the export.
/system clock
set time-zone-name=Europe/Amsterdam

# Set the system short hostname.
/system identity
set name=<<ROUTERNAME>>

# Disable the bandwith-server tool for security.
/tool bandwidth-server
set enabled=no

# Allow Winbox connections from the LAN VLAN.
/tool mac-server
set allowed-interface-list=LAN
/tool mac-server mac-winbox
set allowed-interface-list=LAN

# Follow LTS package.
/system package update
set channel=long-term


File: /config-switchap.rsc
# model = RBD52G-5HacD2HnD

#============================================================================
# Switch/AP configuration for hAP^2.
#
# Requires CAPsMAN on the master router. See also the RB4011iGS
# configuration for underlying decisions.
#============================================================================

# Add the single bridge interface used for all ports.
# - Recommended is to set a static MAC, especially for CAPsMAN managed
#   interfaces.
# - Ensure that the "CPU" interface is also part of the normal
#   LAN VLAN 10 by setting pvid property.
/interface bridge
add admin-mac=<<MAC-OF-FIRST-PORT>> auto-mac=no name=bridge-lan pvid=10 \
    vlan-filtering=yes

# The wireless interfaces are managed by CAPsMAN, however they always
# appear in the export as well.
/interface wireless
set [ find default-name=wlan1 ] disabled=no ssid=MikroTik
set [ find default-name=wlan2 ] disabled=no ssid=MikroTik

# Define the necessary VLANs.
/interface vlan
add interface=bridge-lan name=guest-30 vlan-id=30
add interface=bridge-lan name=iptv-20 vlan-id=20
add interface=bridge-lan name=lan-10 vlan-id=10

# Define two interface lists for security.
/interface list
add name=LAN
add name=GUEST

# Set this APs wireless interface identity.
# Currently unused, but automatically exported.
/interface wireless security-profiles
set [ find default=yes ] supplicant-identity=MikroTik

# Set default hotspot HTML directory.
# Currently unused, but automatically exported.
/ip hotspot profile
set [ find default=yes ] html-directory=flash/hotspot

# Add the bridge ports with VLAN configuration.
# The first Ethernet ports is the TRUNK ports connected to the master
# router.
# CAPsMAN managed wlan interfaces will automatically be added to the
# correct bridge ports conforming to the datapath configuration.
/interface bridge port
add bridge=bridge-lan comment=TRUNK frame-types=admit-only-vlan-tagged \
    ingress-filtering=yes interface=ether1 pvid=10
add bridge=bridge-lan comment=LAN interface=ether2 pvid=10
add bridge=bridge-lan comment=LAN interface=ether3 pvid=10
add bridge=bridge-lan comment=LAN interface=ether4 pvid=10
add bridge=bridge-lan comment=LAN interface=ether5 pvid=10

# Allow router discovery over the normal LAN.
/ip neighbor discovery-settings
set discover-interface-list=LAN

# Accept IPv6 router advertisements. This will grant the router itself
# an IPv6 address and default route, and will then allow clients to
# use IPv6 to connect.
#
# However, due to a bug in RouterOS 6.47.10 this address and route
# are NOT visible in the /ipv6 address and /ipv6 route settings.
# Test with:
#    /ping [:resolve ipv6.google.com]
# Hopefully this gets fixed in RouterOS 7.
# See
#    https://forum.mikrotik.com/viewtopic.php?t=162802
/ipv6 settings
set accept-router-advertisements=yes

# Set bridge trunk/access port configuration. Ensure that the bridge-lan
# interface itself is part of the tagged list, required to use services
# on the VLAN such as DHCP.
/interface bridge vlan
add bridge=bridge-lan tagged=bridge-lan,ether1 untagged=\
    ether2,ether3,ether4,ether5 vlan-ids=10
add bridge=bridge-lan tagged=bridge-lan,ether1 vlan-ids=20
add bridge=bridge-lan tagged=bridge-lan,ether1 vlan-ids=30

# Add the correct interfaces to each list, for security.
# Note that IPTV is combined with LAN, for simplicities sake. For a home
# environment, the STB is not anymore dangerous than any other device.
/interface list member
add interface=lan-10 list=LAN
add interface=iptv-20 list=LAN
add interface=guest-30 list=GUEST

# Set CAPsMAN management link, auto discovery on the LAN network.
/interface wireless cap
set bridge=bridge-lan discovery-interfaces=lan-10 enabled=yes interfaces=\
    wlan1,wlan2

# Configure static IP address, DNS and route for the switch/AP itself.
# Necessary for correct time keeping and checking for system updates.
/ip address
add address=192.168.10.<<ADDRESS>>/24 interface=lan-10 network=192.168.10.0
/ip dns
set servers=192.168.10.1
/ip route
add distance=1 gateway=192.168.10.1

# Disable unnecessary services. Set SSH to port 2222 to avoid conflict
# with port 22 on the outside.
/ip service
set telnet disabled=yes
set ftp disabled=yes
set www disabled=yes
set ssh address=192.168.10.0/24 port=2222
set api disabled=yes
set winbox disabled=yes
set api-ssl disabled=yes

# Enable better SSH crypto.
/ip ssh
set strong-crypto=yes

# Disable IPv6 advertising as this is done from the master router.
/ipv6 nd
set [ find default=yes ] disabled=yes

# Set the time zone. This is actually automatically set by the default
# /ip cloud set update-time=yes setting, however it appears in the export.
/system clock
set time-zone-name=Europe/Amsterdam

# Set the system short hostname.
/system identity
set name=<<ROUTERNAME>>

# Follow LTS package.
/system package update
set channel=long-term


File: /README.md
# Example MikroTik configuration for xs4all/KPN

## Assumptions and requirements

- Home use with a limited number of statically allocated wired devices.
- Configured for xs4all/KPN internet provider with IPTV, using
  fiber to the home with GPON, so upstream interface is the SFP+.
- Multiple switch/APs present on different floors of the house,
  managed by CAPsMAN.
- Separate VLAN for wireless guest network.
- Separate VLAN for a stable IPTV setup.
- Dual stack IPv4 and IPV6 ready.
- Provide DHCPv4 service on all VLANs.
- IPv6 configuration using SLAAC.
- Provide home-local DNS service according to RFC 8375.

## Usage
The configuration is in order of /export . Note that re-ordering
may mess with the ability to reload this configuration.

Be sure to replace all parameters, enclosed in << >> .

Reload of the configuration after factory reset:
1. Ensure the ipv6 and multicast packages are installed
2. Upload script to internal router memory
3. /system reset-configuration no-defaults=yes run-after-reset=SCRIPT

This is in use on an RB4011iGS (model without WiFi), two hAP AC^2 and one cAP AC.


