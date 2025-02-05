# Repository Information
Name: DH-Mikrotik

# Directory Structure
Directory structure:
└── github_repos/DH-Mikrotik/
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
    │   │       ├── pack-d43410a373e9a823f355fceef9d0081002a7b633.idx
    │   │       └── pack-d43410a373e9a823f355fceef9d0081002a7b633.pack
    │   ├── packed-refs
    │   └── refs/
    │       ├── heads/
    │       │   └── main
    │       ├── remotes/
    │       │   └── origin/
    │       │       └── HEAD
    │       └── tags/
    ├── home-config.rsc
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
	url = https://github.com/jiwakreator/DH-Mikrotik.git
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
0000000000000000000000000000000000000000 9c4e65b7313223e5a529b5db0bc8a9dc233c752a vivek-dodia <vivek.dodia@icloud.com> 1738606414 -0500	clone: from https://github.com/jiwakreator/DH-Mikrotik.git


File: /.git\logs\refs\heads\main
0000000000000000000000000000000000000000 9c4e65b7313223e5a529b5db0bc8a9dc233c752a vivek-dodia <vivek.dodia@icloud.com> 1738606414 -0500	clone: from https://github.com/jiwakreator/DH-Mikrotik.git


File: /.git\logs\refs\remotes\origin\HEAD
0000000000000000000000000000000000000000 9c4e65b7313223e5a529b5db0bc8a9dc233c752a vivek-dodia <vivek.dodia@icloud.com> 1738606414 -0500	clone: from https://github.com/jiwakreator/DH-Mikrotik.git


File: /.git\packed-refs
# pack-refs with: peeled fully-peeled sorted 
9c4e65b7313223e5a529b5db0bc8a9dc233c752a refs/remotes/origin/main


File: /.git\refs\heads\main
9c4e65b7313223e5a529b5db0bc8a9dc233c752a


File: /.git\refs\remotes\origin\HEAD
ref: refs/remotes/origin/main


File: /home-config.rsc
# nov/10/2020 11:10:18 by RouterOS 6.47.7
# software id = W326-EUC6
#
# model = 951Ui-2HnD
# serial number = 815707DA1846
/interface ethernet
set [ find default-name=ether1 ] name=ether1-POE
set [ find default-name=ether2 ] name=ether2-Internet
/interface wireless security-profiles
set [ find default=yes ] supplicant-identity=MikroTik
add authentication-types=wpa-psk,wpa2-psk eap-methods="" group-ciphers=\
    tkip,aes-ccm mode=dynamic-keys name=utama supplicant-identity="" \
    unicast-ciphers=tkip,aes-ccm wpa-pre-shared-key=pastiberkah \
    wpa2-pre-shared-key=pastiberkah
/interface wireless
set [ find default-name=wlan1 ] band=2ghz-b/g/n disabled=no mode=ap-bridge \
    name=wlan1-home security-profile=utama ssid="Dree Hardware" \
    station-roaming=enabled
/ip pool
add name=dhcp_pool0 ranges=192.168.100.2-192.168.100.100
add name=dhcp_pool1 ranges=192.168.200.2-192.168.200.100
add name=dhcp_pool2 ranges=192.168.200.2-192.168.200.254
/ip dhcp-server
add address-pool=dhcp_pool2 disabled=no interface=wlan1-home lease-time=1d \
    name=dhcp1
/queue simple
add max-limit=20M/20M name="TOTAL BANDWIDTH" queue=default/default target=\
    192.168.200.0/24
add name="1.GAME ONLINE" packet-marks=Game-Upload,Game-Download parent=\
    "TOTAL BANDWIDTH" priority=1/1 queue=\
    pcq-upload-default/pcq-download-default target=192.168.200.0/24
add name="2.ICMP DNS" packet-marks=ICMP-DNS-Upload,ICMP-DNS-Download parent=\
    "TOTAL BANDWIDTH" queue=pcq-upload-default/pcq-download-default target=\
    192.168.200.0/24
add name="3.ALL TRAFFIC" packet-marks="Umum-Upload,Umum-Download,Youtube-Uploa\
    d,Youtube-Download,Sosmed-Upload,Sosmed-Download" parent=\
    "TOTAL BANDWIDTH" queue=default/default target=192.168.200.0/24
/queue tree
add name="GLOBAL ALL" parent=global queue=default
add max-limit=20M name="TOTAL DOWNLOAD" parent="GLOBAL ALL" queue=\
    pcq-download-default
add max-limit=20M name="TOTAL UPLOAD" parent="GLOBAL ALL" queue=\
    pcq-upload-default
add name="1.GAME DOWNLOAD" packet-mark=Game-Download parent="TOTAL DOWNLOAD" \
    priority=1 queue=pcq-download-default
add name="1.GAME UPLOAD" packet-mark=Game-Upload parent="TOTAL UPLOAD" \
    priority=1 queue=pcq-upload-default
add name="2.ICMP DNS DOWNLOAD" packet-mark=ICMP-DNS-Download parent=\
    "TOTAL DOWNLOAD" queue=pcq-download-default
add name="2.ICMP DNS UPLOAD" packet-mark=ICMP-DNS-Upload parent=\
    "TOTAL UPLOAD" queue=pcq-upload-default
add max-limit=18M name="3.ALL TRAFFIC DOWNLOAD" parent="TOTAL DOWNLOAD" \
    queue=pcq-download-default
add max-limit=18M name="3.ALL TRAFFIC UPLOAD" parent="TOTAL UPLOAD" queue=\
    pcq-upload-default
add name="1.UMUM DOWNLOAD" packet-mark=Umum-Download parent=\
    "3.ALL TRAFFIC DOWNLOAD" priority=7 queue=pcq-download-default
add name="1.UMUM UPLOAD" packet-mark=Umum-Upload parent=\
    "3.ALL TRAFFIC UPLOAD" priority=7 queue=pcq-upload-default
add name="2.YOUTUBE DOWNLOAD" packet-mark=Youtube-Download parent=\
    "3.ALL TRAFFIC DOWNLOAD" priority=3 queue=pcq-download-default
add name="2.YOUTUBE UPLOAD" packet-mark=Youtube-Upload parent=\
    "3.ALL TRAFFIC UPLOAD" priority=3 queue=pcq-upload-default
add name="3.SOSMED DOWNLOAD" packet-mark=Sosmed-Download parent=\
    "3.ALL TRAFFIC DOWNLOAD" priority=5 queue=pcq-download-default
add name="3.SOSMED UPLOAD" packet-mark=Sosmed-Upload parent=\
    "3.ALL TRAFFIC UPLOAD" priority=5 queue=pcq-upload-default
/tool user-manager customer
set admin access=\
    own-routers,own-users,own-profiles,own-limits,config-payment-gw
/user group
set full policy="local,telnet,ssh,ftp,reboot,read,write,policy,test,winbox,pas\
    sword,web,sniff,sensitive,api,romon,dude,tikapp"
/ip neighbor discovery-settings
set discover-interface-list=!dynamic
/ip address
add address=192.168.200.1/24 interface=wlan1-home network=192.168.200.0
/ip cloud
set ddns-enabled=yes
/ip dhcp-client
add !dhcp-options disabled=no interface=ether2-Internet
/ip dhcp-server network
add address=192.168.200.0/24 gateway=192.168.200.1
/ip dns
set servers=8.8.8.8,8.8.4.4
/ip firewall address-list
add address=192.168.200.0/24 list=IP-WLAN
/ip firewall mangle
add action=mark-connection chain=prerouting comment="ICMP DNS" \
    dst-address-list=!IP-WLAN new-connection-mark=ICMP-DNS passthrough=yes \
    protocol=icmp src-address-list=IP-WLAN
add action=mark-connection chain=prerouting dst-address-list=!IP-WLAN \
    dst-port=53 new-connection-mark=ICMP-DNS passthrough=yes protocol=udp \
    src-address-list=IP-WLAN
add action=mark-packet chain=forward connection-mark=ICMP-DNS in-interface=\
    ether2-Internet new-packet-mark=ICMP-DNS-Download passthrough=no
add action=mark-packet chain=forward connection-mark=ICMP-DNS \
    new-packet-mark=ICMP-DNS-Upload out-interface=ether2-Internet \
    passthrough=no
add action=mark-connection chain=postrouting comment="GAME ONLINE" \
    dst-address-list=IP-Game new-connection-mark=Game-Online passthrough=yes \
    src-address-list=IP-WLAN
add action=mark-packet chain=forward connection-mark=Game-Online \
    in-interface=ether2-Internet new-packet-mark=Game-Download passthrough=no
add action=mark-packet chain=forward connection-mark=Game-Online \
    new-packet-mark=Game-Upload out-interface=ether2-Internet passthrough=no
add action=mark-connection chain=postrouting comment=\
    "ALIHKAN KONEKSI GAME KE KONEKSI UMUM" connection-rate=200k-100M \
    dst-address-list=IP-Game new-connection-mark=Koneksi-Umum passthrough=yes \
    src-address-list=IP-WLAN
add action=mark-connection chain=postrouting comment="KONEKSI UMUM" \
    dst-address-list=IP-UMUM new-connection-mark=Koneksi-Umum passthrough=yes \
    src-address-list=IP-WLAN
add action=mark-packet chain=forward connection-mark=Koneksi-Umum \
    in-interface=ether2-Internet new-packet-mark=Umum-Download passthrough=no
add action=mark-packet chain=forward connection-mark=Koneksi-Umum \
    new-packet-mark=Umum-Upload out-interface=ether2-Internet passthrough=no
add action=mark-connection chain=postrouting comment=YOUTUBE \
    dst-address-list=IP-YOUTUBE new-connection-mark=Koneksi-Youtube \
    passthrough=yes src-address-list=IP-WLAN
add action=mark-packet chain=forward connection-mark=Koneksi-Youtube \
    in-interface=ether2-Internet new-packet-mark=Youtube-Download \
    passthrough=no
add action=mark-packet chain=forward connection-mark=Koneksi-Youtube \
    new-packet-mark=Youtube-Upload out-interface=ether2-Internet passthrough=\
    no
add action=mark-connection chain=postrouting comment=SOSMED dst-address-list=\
    IP-SOSMED new-connection-mark=Koneksi-Sosmed passthrough=yes \
    src-address-list=IP-WLAN
add action=mark-packet chain=forward connection-mark=Koneksi-Sosmed \
    in-interface=ether2-Internet new-packet-mark=Sosmed-Download passthrough=\
    no
add action=mark-packet chain=forward connection-mark=Koneksi-Sosmed \
    new-packet-mark=Sosmed-Upload out-interface=ether2-Internet passthrough=\
    no
/ip firewall nat
add action=masquerade chain=srcnat
/ip firewall raw
add action=add-dst-to-address-list address-list=IP-Game address-list-timeout=\
    12h chain=prerouting comment="MOBILE LEGENDS" dst-address-list=!IP-WLAN \
    dst-port=5000-5508,5551-5558,5601-5608,5651-5658,30097-30147,9000-9010 \
    protocol=tcp src-address-list=IP-WLAN
add action=add-dst-to-address-list address-list=IP-Game address-list-timeout=\
    12h chain=prerouting dst-address-list=!IP-WLAN dst-port=\
    5000-5200,5500-5700,8001,30000-30300,9000-9010 protocol=udp \
    src-address-list=IP-WLAN
add action=add-dst-to-address-list address-list=IP-UMUM address-list-timeout=\
    3h chain=prerouting comment="IP UMUM" dst-address-list=!IP-WLAN dst-port=\
    80,81,443,8000-8081,21,22,23,81,88,5050,843,182,53 protocol=tcp \
    src-address-list=IP-WLAN
add action=add-dst-to-address-list address-list=IP-UMUM address-list-timeout=\
    3h chain=prerouting dst-address-list=!IP-WLAN dst-port=\
    80,81,443,8000-8081,21,22,23,81,88,5050,843,182,53 protocol=udp \
    src-address-list=IP-WLAN
add action=add-dst-to-address-list address-list=IP-YOUTUBE \
    address-list-timeout=1h chain=prerouting comment="IP YOUTUBE" content=\
    googlevideo.com dst-address-list=!IP-WLAN src-address-list=IP-WLAN
add action=add-dst-to-address-list address-list=IP-Game address-list-timeout=\
    12h chain=prerouting comment="FREE FIRE" dst-address-list=!IP-WLAN \
    dst-port=10000-10007,7008,10000-10009,17000 protocol=udp \
    src-address-list=IP-WLAN
add action=add-dst-to-address-list address-list=IP-Game address-list-timeout=\
    12h chain=prerouting dst-address-list=!IP-WLAN dst-port=\
    7006,14000,20561,39698,39779,39003 protocol=tcp src-address-list=IP-WLAN
add action=add-dst-to-address-list address-list=IP-Game address-list-timeout=\
    12h chain=prerouting comment=PUBG dst-address-list=!IP-WLAN dst-port=\
    7889,10012,17500,18081 protocol=tcp src-address-list=IP-WLAN
add action=add-dst-to-address-list address-list=IP-Game address-list-timeout=\
    12h chain=prerouting dst-address-list=!IP-WLAN dst-port=\
    8011,9030,10010-10650,11000-14000,17000,20000,20001,20002 protocol=udp \
    src-address-list=IP-WLAN
add action=add-dst-to-address-list address-list=IP-SOSMED \
    address-list-timeout=5h chain=prerouting comment=INSTAGRAM content=\
    .cdninstagram.com dst-address-list=!IP-WLAN src-address-list=IP-WLAN
add action=add-dst-to-address-list address-list=IP-SOSMED \
    address-list-timeout=5h chain=prerouting content=\
    scontent-sin6-2.cdninstagram.com dst-address-list=!IP-WLAN \
    src-address-list=IP-WLAN
add action=add-dst-to-address-list address-list=IP-SOSMED \
    address-list-timeout=5h chain=prerouting content=.instagram.com \
    dst-address-list=!IP-WLAN src-address-list=IP-WLAN
add action=add-src-to-address-list address-list=IP-SOSMED \
    address-list-timeout=3h chain=prerouting comment=FACEBOOK content=\
    .facebook.com dst-address-list=!IP-WLAN src-address-list=IP-WLAN
add action=add-dst-to-address-list address-list=IP-SOSMED \
    address-list-timeout=3h chain=prerouting content=.facebook.net \
    dst-address-list=!IP-WLAN src-address-list=IP-WLAN
add action=add-dst-to-address-list address-list=IP-SOSMED \
    address-list-timeout=3h chain=prerouting content=.fbcdn.net \
    dst-address-list=!IP-WLAN src-address-list=IP-WLAN
add action=add-dst-to-address-list address-list=IP-SOSMED \
    address-list-timeout=2h chain=prerouting comment=TIKTOK content=\
    tiktokcdn.com dst-address-list=!IP-WLAN src-address-list=IP-WLAN
add action=add-dst-to-address-list address-list=IP-SOSMED \
    address-list-timeout=2h chain=prerouting content=tiktokv.com \
    dst-address-list=!IP-WLAN src-address-list=IP-WLAN
add action=add-dst-to-address-list address-list=IP-SOSMED \
    address-list-timeout=2h chain=prerouting content=.amemv.com \
    dst-address-list=!IP-WLAN src-address-list=IP-WLAN
add action=add-dst-to-address-list address-list=IP-SOSMED \
    address-list-timeout=2h chain=prerouting content=.musical.ly \
    dst-address-list=!IP-WLAN src-address-list=IP-WLAN
add action=add-dst-to-address-list address-list=IP-SOSMED \
    address-list-timeout=1d chain=prerouting comment=TELEGRAM content=\
    .telegram.org dst-address-list=!IP-WLAN src-address-list=IP-WLAN
add action=add-dst-to-address-list address-list=IP-SOSMED \
    address-list-timeout=1d chain=prerouting dst-address-list=!IP-WLAN \
    dst-port=5222,8443 protocol=tcp src-address-list=IP-WLAN
add action=add-dst-to-address-list address-list=IP-SOSMED \
    address-list-timeout=1d chain=prerouting comment=WHATSAPP content=\
    .whatsapp.net dst-address-list=!IP-WLAN src-address-list=IP-WLAN
add action=add-dst-to-address-list address-list=IP-SOSMED \
    address-list-timeout=1d chain=prerouting content=.whatsapp.com \
    dst-address-list=!IP-WLAN src-address-list=IP-WLAN
add action=add-dst-to-address-list address-list=IP-SOSMED \
    address-list-timeout=3h chain=prerouting comment=TWITTER content=\
    .twitter.com dst-address-list=!IP-WLAN src-address-list=IP-WLAN
add action=add-dst-to-address-list address-list=IP-SOSMED \
    address-list-timeout=3h chain=prerouting content=.twimg.com \
    dst-address-list=!IP-WLAN src-address-list=IP-WLAN
/ip proxy
set cache-administrator=admin@langkasa.id cache-on-disk=yes
/system clock
set time-zone-name=Asia/Jakarta
/system identity
set name=DH-MikroTik
/system logging
set 0 action=disk prefix="akses ke router -->"
/system ntp client
set enabled=yes primary-ntp=202.65.114.202 secondary-ntp=162.159.200.1
/tool user-manager database
set db-path=user-manager


File: /README.md
# DH-Mikrotik
RSC File Configuration Backup

<ul>Feature
  <li>DHCP Client & Server
  <li>Managament Bandwidth
  <li>Raw Firewall
  <li>Optimize Game Network


