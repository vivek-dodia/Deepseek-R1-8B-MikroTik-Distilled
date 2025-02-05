# Repository Information
Name: mikrotik-scripts

# Directory Structure
Directory structure:
└── github_repos/mikrotik-scripts/
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
    │   │       ├── pack-dc1e1733aee96bcc4560f994bd15f4e8b0b5b3bc.idx
    │   │       └── pack-dc1e1733aee96bcc4560f994bd15f4e8b0b5b3bc.pack
    │   ├── packed-refs
    │   └── refs/
    │       ├── heads/
    │       │   └── master
    │       ├── remotes/
    │       │   └── origin/
    │       │       └── HEAD
    │       └── tags/
    ├── 6to4/
    │   ├── 6to4-basic-firewall.rsc
    │   └── 6to4-setup.rsc
    ├── automatic-upgrade/
    │   ├── upgrade-setup.rsc
    │   └── upgrade.rsc
    ├── backup/
    │   ├── backup-setup.rsc
    │   └── backup.rsc
    ├── firewall/
    │   ├── firewall-input.rsc
    │   └── firewall-output.rsc
    ├── LICENSE
    ├── malware/
    │   ├── malware-refresh.rsc
    │   └── malware.py
    ├── mtu/
    │   └── clamp-mtu.rsc
    ├── README.md
    ├── restrict-country/
    │   ├── country-refresh.rsc
    │   ├── country.py
    │   └── country_ip_blocks.py
    ├── sstp-lets-encrypt/
    │   ├── sstp-cert-upload.sh
    │   └── sstp-setup.rsc
    └── tor-torrent/
        ├── tor-refresh.rsc
        ├── tor.py
        ├── tor.rsc
        └── torrent.rsc


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
	url = https://github.com/Disassembler0/mikrotik-scripts.git
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
0000000000000000000000000000000000000000 c4b3dbfd722803d7a1b6307ad5655269db1cc621 vivek-dodia <vivek.dodia@icloud.com> 1738605788 -0500	clone: from https://github.com/Disassembler0/mikrotik-scripts.git


File: /.git\logs\refs\heads\master
0000000000000000000000000000000000000000 c4b3dbfd722803d7a1b6307ad5655269db1cc621 vivek-dodia <vivek.dodia@icloud.com> 1738605788 -0500	clone: from https://github.com/Disassembler0/mikrotik-scripts.git


File: /.git\logs\refs\remotes\origin\HEAD
0000000000000000000000000000000000000000 c4b3dbfd722803d7a1b6307ad5655269db1cc621 vivek-dodia <vivek.dodia@icloud.com> 1738605788 -0500	clone: from https://github.com/Disassembler0/mikrotik-scripts.git


File: /.git\packed-refs
# pack-refs with: peeled fully-peeled sorted 
c4b3dbfd722803d7a1b6307ad5655269db1cc621 refs/remotes/origin/master


File: /.git\refs\heads\master
c4b3dbfd722803d7a1b6307ad5655269db1cc621


File: /.git\refs\remotes\origin\HEAD
ref: refs/remotes/origin/master


File: /6to4\6to4-basic-firewall.rsc
/ipv6 firewall filter

# INPUT
add chain=input in-interface=6to4-tunnel1 action=jump jump-target=wan-to-mkt comment="Jump to wan-to-mkt rules"
add chain=wan-to-mkt connection-state=established action=accept comment="Allow established connections"
add chain=wan-to-mkt connection-state=related action=accept comment="Allow related connections"
add chain=wan-to-mkt connection-state=invalid action=drop comment="Drop invalid connections"
add chain=wan-to-mkt protocol=icmpv6 action=accept comment="Accept ICMP"
add chain=wan-to-mkt action=drop log=yes log-prefix="6to4 INPUT:" comment="Log and drop everyting else"

# FORWARD
add chain=forward in-interface=6to4-tunnel1 action=jump jump-target=wan-to-lan comment="Jump to wan-to-lan rules"
add chain=wan-to-lan connection-state=established action=accept comment="Allow established connections"
add chain=wan-to-lan connection-state=related action=accept comment="Allow related connections"
add chain=wan-to-lan connection-state=invalid action=drop comment="Drop invalid connections"
add chain=wan-to-lan action=drop log=yes log-prefix="6to4 FORWARD:" comment="Log and drop everyting else"


File: /6to4\6to4-setup.rsc
/interface 6to4
add name=6to4-tunnel1 local-address=123.45.67.89 remote-address=192.88.99.1 disabled=no

/ipv6 address
add address=2002:7b2d:4359::1/48 interface=6to4-tunnel1 advertise=no
add address=2002:7b2d:4359:1::1/64 interface=bridge1

/ipv6 route
add distance=1 dst-address=2000::/3 gateway=6to4-tunnel1

/routing ospf-v3 instance
set [ find default=yes ] redistribute-connected=as-type-1 redistribute-static=as-type-1

/routing ospf-v3 interface
add area=backbone


File: /automatic-upgrade\upgrade-setup.rsc
/tool e-mail
set address=10.0.0.1 from=mikrotik@example.com password=xxx port=587 start-tls=yes user=mikrotik@example.com

/system scheduler
add interval=1w name=backup on-event="/system script run upgrade" start-date=jan/01/2000 start-time=22:00:00


File: /automatic-upgrade\upgrade.rsc
:local recipient "mikrotik@example.com"
:local identity [/system identity get name]

/system package update check-for-update
:delay 5

:local current [/system package update get installed-version]
:local latest [/system package update get latest-version]

:if ([:tostr $latest] != "" && $current != $latest) do={
    :local mailbody ("Identity: " . $identity . "\r\nBoard name: " . [/system resource get board-name] . "\r\nSerial number: " . [/system routerboard get serial-number]  . "\r\nFrom version: " . $current . "\r\nTo version: " . $latest)
    /tool e-mail send to=$recipient subject=($identity . " - RouterOS has been upgraded") body=$mailbody
    /system package update install
}


File: /backup\backup-setup.rsc
/tool e-mail
set address=10.0.0.1 from=mikrotik@example.com password=xxx port=587 start-tls=yes user=mikrotik@example.com

/system scheduler
add interval=1w name=backup on-event="/system script run backup" start-date=jan/01/2000 start-time=21:00:00


File: /backup\backup.rsc
:local recipient "mikrotik@example.com"
:local identity [/system identity get name]

/system backup save name=$identity
:delay 10
export file=$identity
:delay 10

:local mailbody ("Identity: " . $identity . "\r\nBoard name: " . [/system resource get board-name] . "\r\nSerial number: " . [/system routerboard get serial-number] . "\r\nRouterOS version: " . [/system resource get version] . "\r\nFirmware version: " . [/system routerboard get current-firmware])
/tool e-mail send to=$recipient subject=($identity . " - Backup") body=$mailbody file=($identity . ".backup")
/tool e-mail send to=$recipient subject=($identity . " - RSC") body=$mailbody file=($identity . ".rsc")


File: /firewall\firewall-input.rsc
/ip firewall filter

# INPUT - General
add action=accept chain=input comment="Allow 6to4" protocol=ipv6
add action=accept chain=input comment="Allow ICMP" protocol=icmp
add action=accept chain=input comment="Allow Broadcast" dst-address-type=broadcast
add action=accept chain=input comment="Allow local CAPsMAN" dst-address=127.0.0.1 dst-port=5246,5247 protocol=udp src-address=127.0.0.1

# INPUT - LAN Services
add action=jump chain=input comment="Jump to IN-LAN" rules" in-interface=bridge1-local jump-target=IN-LAN
add action=accept chain=IN-LAN comment="Allow DNS" dst-port=53 protocol=udp
add action=accept chain=IN-LAN comment="Allow DNS" dst-port=53 protocol=tcp
add action=accept chain=IN-LAN comment="Allow DHCP" dst-port=67 protocol=udp
add action=accept chain=IN-LAN comment="Allow CAPsMAN" dst-port=5246 protocol=udp
add action=return chain=IN-LAN comment="Return from IN-LAN rules"

# INPUT - Admin Services
add action=jump chain=input comment="Jump to IN-Admin rules" jump-target=IN-Admin src-address-list=Admins
add action=accept chain=IN-Admin comment="Allow SSH" dst-port=22 protocol=tcp
add action=accept chain=IN-Admin comment="Allow SNMP" dst-port=161 protocol=udp
add action=accept chain=IN-Admin comment="Allow WinBox" dst-port=8291 protocol=tcp
add action=return chain=IN-Admin comment="Return from IN-Admin rules"

# INPUT - General
add action=accept chain=input comment="Allow established and related connections" connection-state=established,related
add action=drop chain=input comment="Drop invalid connections" connection-state=invalid
add action=drop chain=input comment="Drop everything else" log=yes log-prefix="IN FILTER:"


File: /firewall\firewall-output.rsc
/ip firewall filter

# FORWARD - General
add action=drop chain=forward comment="Drop blocked IPs" src-address-list=Blocked
add action=drop chain=forward comment="Log and drop malware traffic" dst-address-list=Malware log=yes log-prefix="OUT MALWARE:"
add action=accept chain=forward comment="Bypass firewall for allowed IPs" dst-address-list=Allowed

# FORWARD - Output from LAN clients
add action=jump chain=forward comment="Jump to OUT-Clients rules" in-interface=bridge1-local jump-target=OUT-Clients out-interface=ether1-WAN
add action=accept chain=OUT-Clients comment="Allow ICMP" protocol=icmp
add action=accept chain=OUT-Clients comment="Allow FTP" dst-port=21 protocol=tcp
add action=accept chain=OUT-Clients comment="Allow SSH" dst-port=22 protocol=tcp
add action=accept chain=OUT-Clients comment="Allow SMTP" dst-port=25 protocol=tcp
add action=accept chain=OUT-Clients comment="Allow DNS" dst-port=53 protocol=tcp
add action=accept chain=OUT-Clients comment="Allow DNS" dst-port=53 protocol=udp
add action=accept chain=OUT-Clients comment="Allow HTTP" dst-port=80 protocol=tcp
add action=accept chain=OUT-Clients comment="Allow POP3" dst-port=110 protocol=tcp
add action=accept chain=OUT-Clients comment="Allow NTP" dst-port=123 protocol=udp
add action=accept chain=OUT-Clients comment="Allow IMAP" dst-port=143 protocol=tcp
add action=accept chain=OUT-Clients comment="Allow SNMP" dst-port=161 protocol=udp
add action=accept chain=OUT-Clients comment="Allow LDAP" dst-port=389 protocol=tcp
add action=accept chain=OUT-Clients comment="Allow HTTPS" dst-port=443 protocol=tcp
add action=accept chain=OUT-Clients comment="Allow QUIC" dst-port=443 protocol=udp
add action=accept chain=OUT-Clients comment="Allow SMTPS" dst-port=465 protocol=tcp
add action=accept chain=OUT-Clients comment="Allow Syslog" dst-port=514 protocol=udp
add action=accept chain=OUT-Clients comment="Allow RTSP" dst-port=554 protocol=tcp
add action=accept chain=OUT-Clients comment="Allow RTSP" dst-port=554 protocol=udp
add action=accept chain=OUT-Clients comment="Allow Submission" dst-port=587 protocol=tcp
add action=accept chain=OUT-Clients comment="Allow LDAPS" dst-port=636 protocol=tcp
add action=accept chain=OUT-Clients comment="Allow Flash Socket Policy" dst-port=843 protocol=tcp
add action=accept chain=OUT-Clients comment="Allow SFTP" dst-port=990 protocol=tcp
add action=accept chain=OUT-Clients comment="Allow IMAPS" dst-port=993 protocol=tcp
add action=accept chain=OUT-Clients comment="Allow POP3S" dst-port=995 protocol=tcp
add action=accept chain=OUT-Clients comment="Allow SOCKS5" dst-port=1080 protocol=tcp
add action=accept chain=OUT-Clients comment="Allow Blizzard games" dst-port=1119,3724,6012,6112-6119 protocol=tcp
add action=accept chain=OUT-Clients comment="Allow Blizzard games" dst-port=1119,3724,6012,6112-6119 protocol=udp
add action=accept chain=OUT-Clients comment="Allow OpenVPN" dst-port=1194 protocol=tcp
add action=accept chain=OUT-Clients comment="Allow OpenVPN" dst-port=1194 protocol=udp
add action=accept chain=OUT-Clients comment="Allow Xbox" dst-port=1836,3074 protocol=tcp
add action=accept chain=OUT-Clients comment="Allow Xbox" dst-port=1836,3074,3544 protocol=udp
add action=accept chain=OUT-Clients comment="Allow MQTT" dst-port=1883 protocol=tcp
add action=accept chain=OUT-Clients comment="Allow RTMP" dst-port=1935 protocol=tcp
add action=accept chain=OUT-Clients comment="Allow Squid" dst-port=3128 protocol=tcp
add action=accept chain=OUT-Clients comment="Allow MySQL" dst-port=3306 protocol=tcp
add action=accept chain=OUT-Clients comment="Allow RDP" dst-port=3389 protocol=tcp
add action=accept chain=OUT-Clients comment="Allow STUN" dst-port=3478 protocol=tcp
add action=accept chain=OUT-Clients comment="Allow STUN" dst-port=3478 protocol=udp
add action=accept chain=OUT-Clients comment="Allow PlayStation" dst-port=3480,3658-3659 protocol=tcp
add action=accept chain=OUT-Clients comment="Allow Teredo" dst-port=3544 protocol=udp
add action=accept chain=OUT-Clients comment="Allow PlayStation" dst-port=3658-3659 protocol=udp
add action=accept chain=OUT-Clients comment="Allow Viber" dst-port=4244,5242 protocol=tcp
add action=accept chain=OUT-Clients comment="Allow Steam" dst-port=4379,4380,27000-27036 protocol=udp
add action=accept chain=OUT-Clients comment="Allow Signal" dst-port=4433 protocol=tcp
add action=accept chain=OUT-Clients comment="Allow SIP" dst-port=5060 protocol=tcp
add action=accept chain=OUT-Clients comment="Allow SIP" dst-port=5060 protocol=udp
add action=accept chain=OUT-Clients comment="Allow SIPS" dst-port=5061 protocol=tcp
add action=accept chain=OUT-Clients comment="Allow OSCAR" dst-port=5190 protocol=tcp
add action=accept chain=OUT-Clients comment="Allow XMPP" dst-port=5222 protocol=tcp
add action=accept chain=OUT-Clients comment="Allow XMPPS, Apple Push" dst-port=5223 protocol=tcp
add action=accept chain=OUT-Clients comment="Allow Google Play" dst-port=5228 protocol=tcp
add action=accept chain=OUT-Clients comment="Allow Viber" dst-port=5243,9785 protocol=udp
add action=accept chain=OUT-Clients comment="Allow XMPP Federation" dst-port=5269 protocol=tcp
add action=accept chain=OUT-Clients comment="Allow PostgreSQL" dst-port=5432 protocol=tcp
add action=accept chain=OUT-Clients comment="Allow VNC" dst-port=5900 protocol=tcp
add action=accept chain=OUT-Clients comment="Allow TeamViewer" dst-port=5938 protocol=tcp
add action=accept chain=OUT-Clients comment="Allow TeamViewer" dst-port=5938 protocol=udp
add action=accept chain=OUT-Clients comment="Allow SUPL" dst-port=7275 protocol=tcp
add action=accept chain=OUT-Clients comment="Allow Alternative HTTP" dst-port=8080 protocol=tcp
add action=accept chain=OUT-Clients comment="Allow WinBox" dst-port=8291 protocol=tcp
add action=accept chain=OUT-Clients comment="Allow Alternative HTTPS" dst-port=8443 protocol=tcp
add action=accept chain=OUT-Clients comment="Allow MQTTS" dst-port=8883 protocol=tcp
add action=accept chain=OUT-Clients comment="Allow TeamSpeak" dst-port=9987 protocol=udp
add action=accept chain=OUT-Clients comment="Allow TeamSpeak" dst-port=10011,30033 protocol=tcp
add action=accept chain=OUT-Clients comment="Allow Apple FaceTime" dst-port=16384-16387 protocol=udp
add action=accept chain=OUT-Clients comment="Allow Apple FaceTime" dst-port=16393-16402 protocol=udp
add action=accept chain=OUT-Clients comment="Allow Google Hangouts" dst-port=19302-19309 protocol=udp
add action=accept chain=OUT-Clients comment="Allow Google Hangouts" dst-port=19305-19309 protocol=tcp
add action=accept chain=OUT-Clients comment="Allow Steam" dst-port=27014-27050 protocol=tcp
add action=accept chain=OUT-Clients comment="Allow Windows Update" dst-port=40001-40046 protocol=tcp
add action=accept chain=OUT-Clients comment="Allow Windows Update" dst-port=40001-40046 protocol=udp
add action=accept chain=OUT-Clients comment="Allow established and related connections" connection-state=established,related
add action=drop chain=OUT-Clients comment="Drop invalid connections" connection-state=invalid
add action=drop chain=OUT-Clients comment="Log and drop everything else" log=yes log-prefix="OUT FILTER:"


File: /LICENSE
MIT License

Copyright (c) 2017 Disassembler <disassembler@dasm.cz>

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


File: /malware\malware-refresh.rsc
/tool fetch url=http://linux-host/malware.rsc

# Disable info logging to avoid log spam
:foreach rule in=[/system logging find] do={
    :if ([:find [/system logging get $rule topics] "info" -1] > -1) do={
        /system logging disable $rule
    }
}

import malware.rsc

# Re-enable info logging
:foreach rule in=[/system logging find] do={
    :if ([:find [/system logging get $rule topics] "info" -1] > -1) do={
        /system logging enable $rule
    }
}


File: /malware\malware.py
#!/usr/bin/python3
# -*- coding: utf-8 -*-

import re
import requests

sources = (
    'https://feodotracker.abuse.ch/downloads/ipblocklist.txt',
    'https://malc0de.com/bl/IP_Blacklist.txt',
    'https://www.malwaredomainlist.com/hostslist/ip.txt',
)
destination = '/var/www/html/malware.rsc'

ips = [
    '192.168.x.y',      # Custom
]

ip_re = re.compile(r'(?<![0-9])(?:(?:[0-1]?[0-9]{1,2}|2[0-4][0-9]|25[0-5])[.](?:[0-1]?[0-9]{1,2}|2[0-4][0-9]|25[0-5])[.](?:[0-1]?[0-9]{1,2}|2[0-4][0-9]|25[0-5])[.](?:[0-1]?[0-9]{1,2}|2[0-4][0-9]|25[0-5]))(?![0-9])')

for source in sources:
    try:
        r = requests.get(source)
        for line in r.text.splitlines():
            m = ip_re.match(line)
            if m:
                ips.append(m.group(0))
    except:
        pass

with open(destination, 'w') as f:
    f.write('/ip firewall address-list\n')
    f.write('remove [find list=Malware]\n')
    for ip in sorted(set(ips)):
        f.write('add list=Malware address={}\n'.format(ip))



File: /mtu\clamp-mtu.rsc
/ip firewall mangle add action=change-mss chain=forward new-mss=clamp-to-pmtu passthrough=yes protocol=tcp tcp-flags=syn


File: /README.md
## Description
This is a set of scripts, tips, tricks and snippets for various tasks performed on MikroTik routers. Some of the scripts and their usage is well described in articles on https://www.dasm.cz/tag/mikrotik (written in Czech). Use them at your own risk as there is often some context or additional configuration needed.

### 6to4
Snippets for 6to4 tunneling setup on IPv4 networks with public IP terminated on MikroTik.

### Automatic upgrade
Automatic upgrade of RouterOS with mail notification. Be really careful with this one as it already happened several times that MikroTik guys made the packages incompatible between versions.

### Backup
Automatic backup over mail. Sends both RSC script and a encrypted backup file.

### Firewall
Filtering incoming and outgoing IPv4 traffic. Lots of ports in outgoing rules allow to collect nice traffic statistics.

### Malware
Additional filtering for malware IPs obtained from publicly available blacklists.

### MTU
Just a small mangle script for smooth packet forwarding between networks with different MTU lengths.

### Restrict country
Filtering based on country IP blocks.

### SSTP Let's Encrypt
Core scripts for SSTP server using Let's Encrypt certificates. Much more configuration needed as described on https://www.dasm.cz/clanek/mikrotik-sstp-server-s-let-s-encrypt-certifikatem

### Tor / Torrent
Filtering of Tor nodes based on their type and Torrent services, including bootstraps and DHT.


File: /restrict-country\country-refresh.rsc
/tool fetch url=http://linux-host/country-xx.rsc

# Disable info logging to avoid log spam
:foreach rule in=[/system logging find] do={
    :if ([:find [/system logging get $rule topics] "info" -1] > -1) do={
        /system logging disable $rule
    }
}

import country-xx.rsc

# Re-enable info logging
:foreach rule in=[/system logging find] do={
    :if ([:find [/system logging get $rule topics] "info" -1] > -1) do={
        /system logging enable $rule
    }
}


File: /restrict-country\country.py
#!/usr/bin/python3
# -*- coding: utf-8 -*-

country = 'cz'
source = '/var/www/html/ipblocks/{}.ipv4.collapsed'.format(country)
destination = '/var/www/html/country-{}.rsc'.format(country)

with open(source) as src, open(destination, 'w') as dst:
    dst.write('/ip firewall address-list\n')
    dst.write('remove [find list=CZ.zone]\n')
    for block in src.readlines():
        dst.write('add list=CZ.zone address={}'.format(block))


File: /restrict-country\country_ip_blocks.py
#!/usr/bin/python3
# -*- coding: utf-8 -*-

import csv
import io
import ipaddress
import os
import requests
import zipfile

DST_DIR = '/var/www/html/ipblocks'
MAXMIND_LICENSE_KEY = 'YOUR_LICENSE_KEY'

# Dictionary of (name, ipv4, ipv6) tuples with geoname_id as key
countries = {'': ('unknown', [], [])}

with requests.Session() as session:
    # Download the zipped CSVs
    r = session.get('https://download.maxmind.com/app/geoip_download?edition_id=GeoLite2-Country-CSV&suffix=zip&license_key={}'.format(MAXMIND_LICENSE_KEY))

    # Unpack the zip in memory
    with zipfile.ZipFile(io.BytesIO(r.content)) as zip:
        date = zip.namelist()[0][21:29]

        # Parse countries CSV
        with io.BytesIO(zip.read('GeoLite2-Country-CSV_{}/GeoLite2-Country-Locations-en.csv'.format(date))) as f:
            reader = csv.reader(io.TextIOWrapper(f))
            next(reader, None) # Skip header
            for row in reader:
                country_code = row[4] if row[4] else row[2]
                countries[row[0]] = (country_code.lower(), [], [])

        # Parse IPv4 blocks CSV
        with io.BytesIO(zip.read('GeoLite2-Country-CSV_{}/GeoLite2-Country-Blocks-IPv4.csv'.format(date))) as f:
            reader = csv.reader(io.TextIOWrapper(f))
            next(reader, None)
            for row in reader:
                geoname_id = row[2] if row[2] else row[1]
                countries[geoname_id][1].append(row[0])

        # Parse IPv6 blocks CSV
        with io.BytesIO(zip.read('GeoLite2-Country-CSV_{}/GeoLite2-Country-Blocks-IPv6.csv'.format(date))) as f:
            reader = csv.reader(io.TextIOWrapper(f))
            next(reader, None)
            for row in reader:
                geoname_id = row[2] if row[2] else row[1]
                countries[geoname_id][2].append(row[0])

for country in countries.values():
    country_code = country[0]

    # Write IPv4 blocks file per country
    with open(os.path.join(DST_DIR, '{}.ipv4.blocks'.format(country_code)), 'w') as f:
        for block in country[1]:
            f.write(block)
            f.write('\n')

    # Write IPv6 blocks file per country
    with open(os.path.join(DST_DIR, '{}.ipv6.blocks'.format(country_code)), 'w') as f:
        for block in country[2]:
            f.write(block)
            f.write('\n')

    # Write collapsed IPv4 blocks file per country
    with open(os.path.join(DST_DIR, '{}.ipv4.collapsed'.format(country_code)), 'w') as f:
        for block in ipaddress.collapse_addresses([ipaddress.IPv4Network(b) for b in country[1]]):
            f.write(str(block))
            f.write('\n')

    # Write collapsed IPv6 blocks file per country
    with open(os.path.join(DST_DIR, '{}.ipv6.collapsed'.format(country_code)), 'w') as f:
        for block in ipaddress.collapse_addresses([ipaddress.IPv6Network(b) for b in country[2]]):
            f.write(str(block))
            f.write('\n')


File: /sstp-lets-encrypt\sstp-cert-upload.sh
#!/bin/sh

HOST=vpn.example.com
MTUSER=admin
MTADDR=192.168.88.1

scp /etc/acme-sh/${HOST}/fullchain.cer ${MTUSER}@${MTADDR}:/${HOST}.pem >/dev/null
scp /etc/acme-sh/${HOST}/${HOST}.key ${MTUSER}@${MTADDR}:/${HOST}.key >/dev/null

ssh -T ${MTUSER}@${MTADDR} <<EOF >/dev/null
:delay 3

/certificate remove [find common-name="${HOST}"]
/certificate import file-name="${HOST}.pem" passphrase=""
/certificate import file-name="${HOST}.key" passphrase=""

/file remove "${HOST}.pem"
/file remove "${HOST}.key"

# Reset SSTP certificate and prevent "cert hash not matching" errors
/interface sstp-server server set certificate=none
:delay 1
/interface sstp-server server set certificate="${HOST}.pem_0"
EOF


File: /sstp-lets-encrypt\sstp-setup.rsc
/interface sstp-server server set enabled=yes port=8443
/ppp profile add dns-server=192.168.88.1 local-address=192.168.88.1 name=sstp remote-address=pool1
/ppp secret add name=client password=xxx profile=sstp service=sstp


File: /tor-torrent\tor-refresh.rsc
/tool fetch url=http://linux-host/tor.rsc

# Disable info logging to avoid log spam
:foreach rule in=[/system logging find] do={
    :if ([:find [/system logging get $rule topics] "info" -1] > -1) do={
        /system logging disable $rule
    }
}

import tor.rsc

# Re-enable info logging
:foreach rule in=[/system logging find] do={
    :if ([:find [/system logging get $rule topics] "info" -1] > -1) do={
        /system logging enable $rule
    }
}


File: /tor-torrent\tor.py
#!/usr/bin/python3
# -*- coding: utf-8 -*-

import csv
import re
import requests

File: /tor-torrent\tor.rsc
/ip firewall filter

# INPUT - General
add action=drop chain=input comment="Block Tor exit nodes" dst-address-list=Tor-Exit

# FORWARD - Output from LAN clients
add action=jump chain=forward comment="Jump to OUT-Tor rules" in-interface=bridge1-local jump-target=OUT-Tor out-interface=ether1-WAN
add action=drop chain=OUT-Tor comment="Block Tor directory nodes" dst-address-list=Tor-Dir
add action=drop chain=OUT-Tor comment="Block Tor guard nodes" dst-address-list=Tor-Guard
add action=return chain=OUT-Tor comment="Return from OUT-Tor rules"


File: /tor-torrent\torrent.rsc
/ip firewall layer7-protocol
add name=torrent-tcp regexp="^(\\x13BitTorrent protocol|GET /announce\\\?info_hash=)"
add name=torrent-udp regexp="^(\\x04\\x17\\x27\\x10\\x19\\x80|d1:ad2:id20:)"

/ip firewall address-list
add address=dht.vuze.com list=Torrent
add address=inside.bitcomet.com list=Torrent
add address=dispersy1.tribler.org list=Torrent
add address=dispersy2.tribler.org list=Torrent
add address=dispersy3.tribler.org list=Torrent
add address=dispersy4.tribler.org list=Torrent
add address=dispersy5.tribler.org list=Torrent
add address=dispersy6.tribler.org list=Torrent
add address=dispersy7.tribler.org list=Torrent
add address=dispersy8.tribler.org list=Torrent

/ip firewall filter
add action=jump chain=forward comment="Jump to OUT-Torrent" jump-target=OUT-Torrent out-interface=ether1-WAN
add action=drop chain=OUT-Torrent comment="Bootstrap hosts" dst-address-list=Torrent
add action=drop chain=OUT-Torrent comment="Teredo" dst-port=3544 protocol=udp
add action=drop chain=OUT-Torrent comment="DHT Routers" dst-port=6881 protocol=udp
add action=drop chain=OUT-Torrent comment="L7 UDP" layer7-protocol=torrent-udp protocol=udp
add action=drop chain=OUT-Torrent comment="L7 TCP" layer7-protocol=torrent-tcp protocol=tcp
add action=return chain=OUT-Torrent comment="Return from OUT-Torrent rules"


