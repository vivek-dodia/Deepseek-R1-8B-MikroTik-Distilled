# Repository Information
Name: mikrotik-caiway-routed-iptv

# Directory Structure
Directory structure:
└── github_repos/mikrotik-caiway-routed-iptv/
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
    │   │       ├── pack-80a99e2270ecc4fe34f7912fa4e49476057bcc58.idx
    │   │       └── pack-80a99e2270ecc4fe34f7912fa4e49476057bcc58.pack
    │   ├── packed-refs
    │   └── refs/
    │       ├── heads/
    │       │   └── master
    │       ├── remotes/
    │       │   └── origin/
    │       │       └── HEAD
    │       └── tags/
    ├── basic-191118.rsc
    ├── LICENSE
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
	url = https://github.com/jghek/mikrotik-caiway-routed-iptv.git
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
0000000000000000000000000000000000000000 edfda478afd6ffb427f0e6b88716b085041a4001 vivek-dodia <vivek.dodia@icloud.com> 1738606364 -0500	clone: from https://github.com/jghek/mikrotik-caiway-routed-iptv.git


File: /.git\logs\refs\heads\master
0000000000000000000000000000000000000000 edfda478afd6ffb427f0e6b88716b085041a4001 vivek-dodia <vivek.dodia@icloud.com> 1738606364 -0500	clone: from https://github.com/jghek/mikrotik-caiway-routed-iptv.git


File: /.git\logs\refs\remotes\origin\HEAD
0000000000000000000000000000000000000000 edfda478afd6ffb427f0e6b88716b085041a4001 vivek-dodia <vivek.dodia@icloud.com> 1738606364 -0500	clone: from https://github.com/jghek/mikrotik-caiway-routed-iptv.git


File: /.git\packed-refs
# pack-refs with: peeled fully-peeled sorted 
edfda478afd6ffb427f0e6b88716b085041a4001 refs/remotes/origin/master


File: /.git\refs\heads\master
edfda478afd6ffb427f0e6b88716b085041a4001


File: /.git\refs\remotes\origin\HEAD
ref: refs/remotes/origin/master


File: /basic-191118.rsc
# RouterOS 6.45.7, CCR1009-7G-1C-1S+

# Uitgebreide configuratie voor CAIWAY routed-IPTV voor Mikrotik RouterOS (Extra package: NTP Server)
# Bij CAIWAY zit internet op VLAN 100. Je kunt hier met DHCP een IP adres opvragen.
# De IPTV zit op VLAN 101. Je kunt hier ook met DHCP een VLAN opvragen, maar dit vereist de juiste optie (optie 60).
#
# Zelf maak ik gebruik van:
# VLAN 10  : 10.218.0.1/16    - Mijn netwerk voor kinderen en gasten. Gebruikt OpenDNS servers om ongewenste inhoud te filteren en een /16 reeks om veel DHCP leases aan te kunnen.
# VLAN 1218: 192.168.218.1/24 - Mijn thuis netwerk.
# VLAN 1251: 192.168.251.1/24 - Mijn IPTV LAN. Hierbinnen zitten de AMINO tv boxes. Mochten ze gehackt worden, dan zitten ze niet in mijn thuis LAN.

# Het maken van de L2 segmenten (bridges). IGMP snooping moet aan staan op ons IPTV LAN.
/interface bridge add name=bridge10
/interface bridge add fast-forward=no name=bridge1218 protocol-mode=none
/interface bridge add arp=proxy-arp fast-forward=no igmp-snooping=yes name=bridge1251 protocol-mode=none

# Geen STP pakketten naar de provider
/interface ethernet set [ find default-name=combo1 ] loop-protect=off

# Aanmaken van VLANs op de interfaces.

# Internet
/interface vlan add arp=proxy-arp interface=combo1 loop-protect=off name=combo1.100 vlan-id=100

# IPTV
/interface vlan add interface=combo1 loop-protect=off name=combo1.101 vlan-id=101

# Over ether7 gaan meerdere vlans naar mijn switch.
/interface vlan add interface=ether7 name=ether7.10 vlan-id=10
/interface vlan add interface=ether7 name=ether7.1218 vlan-id=1218

# DHCP client optie. Nodig om een IP adres te krijgen van de CAIWAY IPTV DHCP.
/ip dhcp-client option add code=60 name=IPTV_RG value="'IPTV_RG'"

# DHCP server optie. Deze levert de mikrotik aan de ANIMO boxes.
/ip dhcp-server option add code=60 name=option60-vendorclass value="'IPTV_RG'"
/ip dhcp-server option add code=28 name=option28-broadcast value="'192.168.251.255'"
/ip dhcp-server option sets add name=IPTV options=option60-vendorclass,option28-broadcast

# Adres ranges (pools) die de DHCP servers mogen uitgeven.
/ip pool add name=dhcp-1218 ranges=192.168.218.32-192.168.218.254
/ip pool add name=dhcp-10 ranges=10.218.1.1-10.218.255.254
/ip pool add name=dhcp-1251 ranges=192.168.251.32-192.168.251.254

# Opzetten van de DHCP servers
/ip dhcp-server add address-pool=dhcp-10 disabled=no interface=bridge10 lease-time=1h30m name=dhcp-server-10
/ip dhcp-server add address-pool=dhcp-1218 disabled=no interface=bridge1218 lease-time=1h30m name=dhcp-server-1218
/ip dhcp-server add address-pool=dhcp-1251 dhcp-option-set=IPTV disabled=no interface=bridge1251 name=dhcp-server-1251

# BGP routering uit.
/routing bgp instance set default disabled=yes

# interfaces koppelen aan L2 segmenten (bridges).
/interface bridge port add bridge=bridge1251 interface=ether4
/interface bridge port add bridge=bridge1251 interface=ether5
/interface bridge port add bridge=bridge10 interface=ether7.10
/interface bridge port add bridge=bridge1218 interface=ether7.1218

# IP adressen koppelen aan L2 segmenten (bridges).
/ip address add address=10.218.0.1/16 interface=bridge10 network=10.218.0.0
/ip address add address=192.168.218.1/24 interface=bridge1218 network=192.168.218.0
/ip address add address=192.168.251.1/24 interface=bridge1251 network=192.168.251.0

# Via CAIWAY heb je geen fixed ip-adres. Mikrotik geeft je een gratis (en geintregeerde DDNS service). Top!
# gebruik '/ip cloud print' om te achterhalen wat jouw gekoppelde domeinnaam is. Iets als: <serie-nummer>.sn.mynetname.net
# Als je zelf een domeinnaam hebt de je wilt gebruiken, dan kun je het beste een CNAME record aanmaken die verwijst naar de mikrotik ddns naam.
/ip cloud set ddns-enabled=yes

# DHCP Clients: kortom, op welke L2 segmenten gaan we via DHCP een IP adres opvragen en met welke opties?
/ip dhcp-client add dhcp-options=hostname,clientid disabled=no interface=combo1.100
/ip dhcp-client add default-route-distance=210 dhcp-options=IPTV_RG,hostname,clientid disabled=no interface=combo1.101 use-peer-dns=no use-peer-ntp=no

# DHCP Server voor gasten gebruikt OpenDNS adressen.
/ip dhcp-server network add address=10.218.0.0/16 dns-server=208.67.222.123,208.67.220.123 domain=guest.local gateway=10.218.0.1 ntp-server=10.218.0.1 netmask=24
/ip dhcp-server network add address=192.168.218.0/24 dns-server=192.168.218.1 domain=hek.local gateway=192.168.218.1 ntp-server=192.168.218.1 netmask=24
/ip dhcp-server network add address=192.168.251.0/24 dhcp-option-set=IPTV dns-server=192.168.251.1 domain=iptv.local gateway=192.168.251.1 ntp-server=192.168.251.1 netmask=24

# Onze router zal DNS request beantwoorden.
/ip dns set allow-remote-requests=yes cache-max-ttl=1d servers=8.8.8.8,8.8.4.4

# Deze reeksen mogen niet op internet voorkomen, omdat het private ranges zijn of test reeksen. We filteren ze.
/ip firewall address-list add address=0.0.0.0/8 comment="Self-Identification [RFC 3330]" list=Unrouted
/ip firewall address-list add address=10.0.0.0/8 comment="Private class A" list=Unrouted
/ip firewall address-list add address=127.0.0.0/8 comment="Loopback [RFC 3330]" list=Unrouted
/ip firewall address-list add address=169.254.0.0/16 comment="Link Local [RFC 3330]" list=Unrouted
/ip firewall address-list add address=172.16.0.0/12 comment="Private class B" list=Unrouted
/ip firewall address-list add address=192.0.2.0/24 comment="Reserved - IANA - TestNet1" list=Unrouted
/ip firewall address-list add address=192.88.99.0/24 comment="6to4 Relay Anycast [RFC 3068]" list=Unrouted
/ip firewall address-list add address=198.18.0.0/15 comment="NIDB Testing" list=Unrouted
/ip firewall address-list add address=198.51.100.0/24 comment="Reserved - IANA - TestNet2" list=Unrouted
/ip firewall address-list add address=203.0.113.0/24 comment="Reserved - IANA - TestNet3" list=Unrouted
/ip firewall address-list add address=192.168.0.0/16 comment="Private class C" list=Unrouted

# De firewall regels
/ip firewall filter add action=accept chain=input in-interface=combo1.100 protocol=icmp
/ip firewall filter add action=accept chain=input connection-state=established,related in-interface=combo1.100
/ip firewall filter add action=drop chain=input in-interface=combo1.100 protocol=tcp
/ip firewall filter add action=drop chain=input in-interface=combo1.100 protocol=udp
/ip firewall filter add action=accept chain=forward disabled=yes in-interface=bridge1252 src-address-list=IoT-Allow-internet
/ip firewall filter add action=drop chain=forward disabled=yes in-interface=bridge1252
/ip firewall filter add action=drop chain=forward comment="Drop to unrouted addresses list" in-interface=combo1.100 src-address-list=Unrouted
/ip firewall filter add action=drop chain=forward comment="Drop all from WAN not DSTNATed" connection-nat-state=!dstnat connection-state=new in-interface=combo1.100

# Deze reeksen zijn overgenomen uit KPN configuraties. Ik weet niet of deze nodig zijn.
/ip firewall nat add action=masquerade chain=srcnat comment="Needed for IPTV" dst-address=213.75.112.0/21 out-interface=combo1.101
/ip firewall nat add action=masquerade chain=srcnat comment="Needed for IPTV" dst-address=217.166.0.0/16 out-interface=combo1.101
/ip firewall nat add action=masquerade chain=srcnat src-address=10.218.0.0/16
/ip firewall nat add action=masquerade chain=srcnat src-address=192.168.218.0/24
/ip firewall nat add action=masquerade chain=srcnat src-address=192.168.251.0/24

# IGMP Routering tussen 1251 en combo1.101
/routing igmp-proxy set quick-leave=yes
/routing igmp-proxy interface add alternative-subnets=0.0.0.0/0 interface=combo1.101 upstream=yes
/routing igmp-proxy interface add interface=bridge1251

# NTP Settings. Hiervoor is het NTP Package nodig op de Mikrotik.
/system clock set time-zone-name=Europe/Amsterdam
/system ntp client set enabled=yes primary-ntp=193.78.240.12 secondary-ntp=130.89.0.19
/system ntp server set enabled=yes manycast=no


File: /LICENSE
MIT License

Copyright (c) 2019 Jan Geert Hek

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


File: /README.md
# Mikrotik configuratie voor CAIWAY via Glasvezel Buitenaf
Deze basis-configuratie gebruik ik op een [CCR1009-7G-1C-1S+ Mikrotik Cloud Core Router](https://mikrotik.com/product/CCR1009-7G-1C-1SplusPC), op RouterOS 6.45.7. Naar verwachting gaat dit ook prima werken met goedkopere modellen. Eén verschil is wel dat dit model geen switch chip kent en daarom mogelijk enkele tweaks nodig heeft om het geheel efficient aan het werk te krijgen.

## Waarschuwing!
Dit is niet simpel. De standaard Genexis router is vrij beperkt, maar de meeste dingen kun je er prima mee doen. Als je deze router wilt vervangen, kun je dat doen omdat jouw netwerkconfiguratie wat meer vereist (tunnels, meerdere lokale netwerken, dual/fallback isp), of omdat dubbel NAT gewoon jeukt en je het net erg vind dat je vrienden je een beetje raar vinden. Je dient wel het één en ander van netwerken te begrijpen. Anders niet aan beginnen.

## Credits
Dit was mijn eerste Mikrotik avontuur. Ik heb de nodige ervaring met Cisco, HP, Sophos apparatuur, maar dat werkt toch weer net wat anders dan Mikrotik. Voor de prijs heb je zeer goede kwaliteit en zeer veel mogelijkheden. Nadeel: zeer veel mogelijkheden. De taal is daarnaast ook geen Cisco derivaat zoals je op veel plekken tegenkomt. Ik heb veel gebruikt van [netwerkje.com](https://netwerkje.com/routed-iptv) en dat aangepast voor CAIWAY. Bedankt daarvoor!

# Wat levert CAIWAY
CAIWAY levert een [GENEXIS Platinum 7840](https://nl.hardware.info/routers.9/genexis-genexis-platinum-7840.534715) router. Deze zit op de glas aangesloten met een SC connector op een [Genexis SFP module (1Gb/s)](https://en.wikipedia.org/wiki/Small_form-factor_pluggable_transceiver). Deze SFP zit verstopt op de achterkant achter een klepje met een blauwe garantie sticker. Op de verbinding leveren ze twee VLANs:

| VLAN | Techniek | Beschrijving |
| --- | --- | --- |
| 100 | DHCP | Internet |
| 101 | DHCP (optie 60 vereist) | IPTV |

Misschien is er nog één voor telefonie, maar dat gebruik ik niet.

# Aansluiten
De Genexis SFP module werkte niet in de Mikrotik. Ik heb het opgelost door de SPF in een HP1920-24G (mijn LAN switch met 4 SFP slots) en een SFP direct attach kabel van de switch naar de mikrotik te leggen. Op de switch dien je dan wel beide aansluitingen te configureren om VLAN 100 en 101 tagged te gebruiken. In plaats van een switch is een mediaconvertor (SFP<->RJ45) ook mogelijk. Deze direct attach SFP kabel is aangesloten op de SFP/Combo1 poort. Mocht de Mikrotik later wel de SFP gaan ondersteunen, dan kan ik hem rechtstreeks plaatsen zonder configuratie aanpassingen. Verder gebruik ik ether7 als de verbinding naar mijn HP switch, later wil ik dit doen via de SFP+ poort (10Gb/s) als ik een switch heb die dit aan kan (en het zinvol is). De AMINO STBs zijn aangesloten op ether4 en ether5.

# Netwerkinrichting
In deze configuratie ga ik uit van de volgende inrichting:

| VLAN | Netwerk | Beschrijving |
| --- | --- | --- |
| 10 | 10.218.0.1/16 | Mijn netwerk voor kinderen en gasten. Gebruikt OpenDNS servers om ongewenste inhoud te filteren en een /16 reeks om veel DHCP leases aan te kunnen. |
| 1218 | 192.168.218.1/24 | Mijn thuis netwerk. |
| 1251 | 192.168.251.1/24 | Mijn IPTV LAN. Hierbinnen zitten de AMINO tv boxes. Mochten ze gehackt worden, dan zitten ze niet in mijn thuis LAN. |

# Overige bijzonderheden
Bij upgrade naar een nieuwe RouterOS heb ik er voor gekozen ook de NTP Server package te installeren. Hiermee is de router ook een NTP Server. In de configuratie zitten er verwijzingen naar.

# De configuratie
Hieronder volgt de configuratie met uitleg. Je kunt de config ook direct [openen](basic-191118.rsc).

```
# Het maken van de L2 segmenten (bridges). IGMP snooping moet aan staan op ons IPTV LAN.
/interface bridge add name=bridge10
/interface bridge add fast-forward=no name=bridge1218 protocol-mode=none
/interface bridge add arp=proxy-arp fast-forward=no igmp-snooping=yes name=bridge1251 protocol-mode=none

# Geen STP (spanning-tree) pakketten naar de provider
/interface ethernet set [ find default-name=combo1 ] loop-protect=off

# Aanmaken van VLANs op de interfaces.

# Internet
/interface vlan add arp=proxy-arp interface=combo1 loop-protect=off name=combo1.100 vlan-id=100

# IPTV
/interface vlan add interface=combo1 loop-protect=off name=combo1.101 vlan-id=101

# Over ether7 gaan meerdere vlans naar mijn switch.
/interface vlan add interface=ether7 name=ether7.10 vlan-id=10
/interface vlan add interface=ether7 name=ether7.1218 vlan-id=1218

# DHCP client optie. Nodig om een IP adres te krijgen van de CAIWAY IPTV DHCP.
/ip dhcp-client option add code=60 name=IPTV_RG value="'IPTV_RG'"

# DHCP server optie. Deze levert de mikrotik aan de ANIMO boxes.
/ip dhcp-server option add code=60 name=option60-vendorclass value="'IPTV_RG'"
/ip dhcp-server option add code=28 name=option28-broadcast value="'192.168.251.255'"
/ip dhcp-server option sets add name=IPTV options=option60-vendorclass,option28-broadcast

# Adres ranges (pools) die de DHCP servers mogen uitgeven.
/ip pool add name=dhcp-1218 ranges=192.168.218.32-192.168.218.254
/ip pool add name=dhcp-10 ranges=10.218.1.1-10.218.255.254
/ip pool add name=dhcp-1251 ranges=192.168.251.32-192.168.251.254

# Opzetten van de DHCP servers
/ip dhcp-server add address-pool=dhcp-10 disabled=no interface=bridge10 lease-time=1h30m name=dhcp-server-10
/ip dhcp-server add address-pool=dhcp-1218 disabled=no interface=bridge1218 lease-time=1h30m name=dhcp-server-1218
/ip dhcp-server add address-pool=dhcp-1251 dhcp-option-set=IPTV disabled=no interface=bridge1251 name=dhcp-server-1251

# BGP routering uit.
/routing bgp instance set default disabled=yes

# interfaces koppelen aan L2 segmenten (bridges).

# AMINO boxes
/interface bridge port add bridge=bridge1251 interface=ether4
/interface bridge port add bridge=bridge1251 interface=ether5

# VLANs naar de switch
/interface bridge port add bridge=bridge10 interface=ether7.10
/interface bridge port add bridge=bridge1218 interface=ether7.1218

# IP adressen koppelen aan L2 segmenten (bridges).
/ip address add address=10.218.0.1/16 interface=bridge10 network=10.218.0.0
/ip address add address=192.168.218.1/24 interface=bridge1218 network=192.168.218.0
/ip address add address=192.168.251.1/24 interface=bridge1251 network=192.168.251.0

# Via CAIWAY heb je geen fixed ip-adres. Mikrotik geeft je een gratis (en geintregeerde DDNS service). Top!
# gebruik '/ip cloud print' om te achterhalen wat jouw gekoppelde domeinnaam is. Iets als: <serie-nummer>.sn.mynetname.net
# Als je zelf een domeinnaam hebt de je wilt gebruiken, dan kun je het beste een CNAME record aanmaken die verwijst naar de mikrotik ddns naam.
/ip cloud set ddns-enabled=yes

# DHCP Clients: Op welke L2 segmenten gaan we via DHCP een IP adres opvragen en met welke opties?
/ip dhcp-client add dhcp-options=hostname,clientid disabled=no interface=combo1.100
/ip dhcp-client add default-route-distance=210 dhcp-options=IPTV_RG,hostname,clientid disabled=no interface=combo1.101 use-peer-dns=no use-peer-ntp=no

# DHCP Server voor gasten gebruikt OpenDNS adressen.
/ip dhcp-server network add address=10.218.0.0/16 dns-server=208.67.222.123,208.67.220.123 domain=guest.local gateway=10.218.0.1 ntp-server=10.218.0.1 netmask=24
/ip dhcp-server network add address=192.168.218.0/24 dns-server=192.168.218.1 domain=hek.local gateway=192.168.218.1 ntp-server=192.168.218.1 netmask=24
/ip dhcp-server network add address=192.168.251.0/24 dhcp-option-set=IPTV dns-server=192.168.251.1 domain=iptv.local gateway=192.168.251.1 ntp-server=192.168.251.1 netmask=24

# Onze router zal DNS request beantwoorden en fungeert daarmee als interne DNS server.
/ip dns set allow-remote-requests=yes cache-max-ttl=1d servers=8.8.8.8,8.8.4.4

# Deze reeksen mogen niet op internet voorkomen, omdat het private ranges zijn of test reeksen.
/ip firewall address-list add address=0.0.0.0/8 comment="Self-Identification [RFC 3330]" list=Unrouted
/ip firewall address-list add address=10.0.0.0/8 comment="Private class A" list=Unrouted
/ip firewall address-list add address=127.0.0.0/8 comment="Loopback [RFC 3330]" list=Unrouted
/ip firewall address-list add address=169.254.0.0/16 comment="Link Local [RFC 3330]" list=Unrouted
/ip firewall address-list add address=172.16.0.0/12 comment="Private class B" list=Unrouted
/ip firewall address-list add address=192.0.2.0/24 comment="Reserved - IANA - TestNet1" list=Unrouted
/ip firewall address-list add address=192.88.99.0/24 comment="6to4 Relay Anycast [RFC 3068]" list=Unrouted
/ip firewall address-list add address=198.18.0.0/15 comment="NIDB Testing" list=Unrouted
/ip firewall address-list add address=198.51.100.0/24 comment="Reserved - IANA - TestNet2" list=Unrouted
/ip firewall address-list add address=203.0.113.0/24 comment="Reserved - IANA - TestNet3" list=Unrouted
/ip firewall address-list add address=192.168.0.0/16 comment="Private class C" list=Unrouted

# De firewall regels
/ip firewall filter add action=accept chain=input in-interface=combo1.100 protocol=icmp
/ip firewall filter add action=accept chain=input connection-state=established,related in-interface=combo1.100
/ip firewall filter add action=drop chain=input in-interface=combo1.100 protocol=tcp
/ip firewall filter add action=drop chain=input in-interface=combo1.100 protocol=udp
/ip firewall filter add action=accept chain=forward disabled=yes in-interface=bridge1252 src-address-list=IoT-Allow-internet
/ip firewall filter add action=drop chain=forward disabled=yes in-interface=bridge1252
/ip firewall filter add action=drop chain=forward comment="Drop to unrouted addresses list" in-interface=combo1.100 src-address-list=Unrouted
/ip firewall filter add action=drop chain=forward comment="Drop all from WAN not DSTNATed" connection-nat-state=!dstnat connection-state=new in-interface=combo1.100

# Deze reeksen zijn overgenomen uit KPN configuraties. Ik weet niet of deze nodig zijn.
/ip firewall nat add action=masquerade chain=srcnat comment="IPTV" dst-address=213.75.112.0/21 out-interface=combo1.101
/ip firewall nat add action=masquerade chain=srcnat comment="IPTV" dst-address=217.166.0.0/16 out-interface=combo1.101
/ip firewall nat add action=masquerade chain=srcnat src-address=10.218.0.0/16
/ip firewall nat add action=masquerade chain=srcnat src-address=192.168.218.0/24
/ip firewall nat add action=masquerade chain=srcnat src-address=192.168.251.0/24

# IGMP Proxy tussen 1251 en combo1.101, de kern van de IPTV routed configuratie. Hiermee geen IGMP (tv beeld) pakketten via VLAN101 naar CAIWAY.
/routing igmp-proxy set quick-leave=yes
/routing igmp-proxy interface add alternative-subnets=0.0.0.0/0 interface=combo1.101 upstream=yes
/routing igmp-proxy interface add interface=bridge1251

# NTP Settings. Hiervoor is het NTP Package nodig op de Mikrotik.
/system clock set time-zone-name=Europe/Amsterdam
/system ntp client set enabled=yes primary-ntp=193.78.240.12 secondary-ntp=130.89.0.19
/system ntp server set enabled=yes manycast=no
```


