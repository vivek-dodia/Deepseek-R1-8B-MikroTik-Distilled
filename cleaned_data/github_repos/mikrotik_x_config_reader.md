# Repository Information
Name: mikrotik_x_config_reader

# Directory Structure
Directory structure:
└── github_repos/mikrotik_x_config_reader/
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
    │   │       ├── pack-66df91ce80fddc1f2aabffbb885f9c5d6219dc7a.idx
    │   │       └── pack-66df91ce80fddc1f2aabffbb885f9c5d6219dc7a.pack
    │   ├── packed-refs
    │   └── refs/
    │       ├── heads/
    │       │   └── master
    │       ├── remotes/
    │       │   └── origin/
    │       │       └── HEAD
    │       └── tags/
    ├── .gitignore
    ├── bins/
    │   ├── lhgg-60ad.bin
    │   ├── rb3011.bin
    │   └── rb450gx4.bin
    ├── dts/
    │   ├── decompile_dtb.sh
    │   ├── lhgg.dtb
    │   ├── lhgg.dts
    │   ├── rb5009.dtb
    │   └── rb5009.dts
    ├── Makefile
    ├── mibibs/
    │   └── rb3011.mibib
    ├── ptable.h
    ├── README.md
    └── x_conf_reader.c


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
	url = https://github.com/adron-s/mikrotik_x_config_reader.git
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
0000000000000000000000000000000000000000 aec20d3f1c7b682ab742ffec203892fbe08ee1c2 vivek-dodia <vivek.dodia@icloud.com> 1738606061 -0500	clone: from https://github.com/adron-s/mikrotik_x_config_reader.git


File: /.git\logs\refs\heads\master
0000000000000000000000000000000000000000 aec20d3f1c7b682ab742ffec203892fbe08ee1c2 vivek-dodia <vivek.dodia@icloud.com> 1738606061 -0500	clone: from https://github.com/adron-s/mikrotik_x_config_reader.git


File: /.git\logs\refs\remotes\origin\HEAD
0000000000000000000000000000000000000000 aec20d3f1c7b682ab742ffec203892fbe08ee1c2 vivek-dodia <vivek.dodia@icloud.com> 1738606061 -0500	clone: from https://github.com/adron-s/mikrotik_x_config_reader.git


File: /.git\packed-refs
# pack-refs with: peeled fully-peeled sorted 
aec20d3f1c7b682ab742ffec203892fbe08ee1c2 refs/remotes/origin/master


File: /.git\refs\heads\master
aec20d3f1c7b682ab742ffec203892fbe08ee1c2


File: /.git\refs\remotes\origin\HEAD
ref: refs/remotes/origin/master


File: /.gitignore
ex1/*
dumps/*
bins/*
.*
!.gitignore
x_conf_reader

File: /dts\decompile_dtb.sh
#!/bin/sh

OPENWRT_KERNEL="/home/prog/openwrt/2021-openwrt/last-openwrt/openwrt/build_dir/target-aarch64_cortex-a72_musl/linux-mvebu_cortexa72/linux-5.10.64"
DTC=${OPENWRT_KERNEL}/scripts/dtc/dtc

${DTC} -I dtb -O dts -o lhgg.dts lhgg.dtb
#${DTC} -I dtb -O dts -o rb5009.dts rb5009.dtb

File: /dts\lhgg.dts
/dts-v1/;

/ {
	#address-cells = <0x1>;
	#size-cells = <0x1>;
	compatible = "qcom,ipq40xx-apdk01.1", "qcom,ipq40xx";
	mac-address = [00 00 00 00 00 00];
	interrupt-parent = <0x1>;
	model = "LHG 60G";

	chosen {
		bootargs-append = " clk_ignore_unused";
		bootargs = [00];
		linux,initrd-start = <0x0>;
		linux,initrd-end = <0x0>;
	};

	aliases {
		spi0 = "/soc/spi@78b5000";
		i2c0 = "/soc/i2c@78b7000";
		ethernet0 = "/soc/edma/gmac0";
		ethernet1 = "/soc/edma/gmac1";
	};

	cpus {
		#address-cells = <0x1>;
		#size-cells = <0x0>;

		cpu@0 {
			device_type = "cpu";
			compatible = "arm,cortex-a7";
			enable-method = "qcom,arm-cortex-acc";
			reg = <0x0>;
			clocks = <0x2 0x9>;
			clock-frequency = <0x0>;
		};

		cpu@1 {
			device_type = "cpu";
			compatible = "arm,cortex-a7";
			enable-method = "qcom,arm-cortex-acc";
			reg = <0x1>;
			clocks = <0x2 0x9>;
			clock-frequency = <0x0>;
		};

		cpu@2 {
			device_type = "cpu";
			compatible = "arm,cortex-a7";
			enable-method = "qcom,arm-cortex-acc";
			reg = <0x2>;
			clocks = <0x2 0x9>;
			clock-frequency = <0x0>;
		};

		cpu@3 {
			device_type = "cpu";
			compatible = "arm,cortex-a7";
			enable-method = "qcom,arm-cortex-acc";
			reg = <0x3>;
			clocks = <0x2 0x9>;
			clock-frequency = <0x0>;
		};
	};

	clocks {

		gcc_sleep_clk_src {
			compatible = "fixed-clock";
			clock-frequency = <0x7d00>;
			#clock-cells = <0x0>;
			phandle = <0x47>;
		};

		xo {
			compatible = "fixed-clock";
			clock-frequency = <0x2dc6c00>;
			#clock-cells = <0x0>;
		};
	};

	soc {
		#address-cells = <0x1>;
		#size-cells = <0x1>;
		ranges;
		compatible = "simple-bus";

		ad-hoc-bus@500000 {
			compatible = "qcom,msm-bus-device";
			reg = <0x580000 0x14000 0x500000 0x11000>;
			reg-names = "snoc-base", "pcnoc-base";

			fab-pcnoc {
				cell-id = <0x1000>;
				label = "fab-pcnoc";
				qcom,fab-dev;
				qcom,base-name = "pcnoc-base";
				qcom,bypass-qos-prg;
				qcom,bus-type = <0x1>;
				qcom,qos-off = <0x1000>;
				qcom,base-offset = <0x0>;
				clocks;
				phandle = <0x4>;
			};

			fab-snoc {
				cell-id = <0x400>;
				label = "fab-snoc";
				qcom,fab-dev;
				qcom,base-name = "snoc-base";
				qcom,bypass-qos-prg;
				qcom,bus-type = <0x1>;
				qcom,qos-off = <0x80>;
				qcom,base-offset = <0x0>;
				clocks;
				phandle = <0x31>;
			};

			mas-blsp-bam {
				cell-id = <0x6d>;
				label = "mas-blsp-bam";
				qcom,buswidth = <0x4>;
				qcom,ap-owned;
				qcom,connections = <0x3>;
				qcom,bus-dev = <0x4>;
				qcom,mas-rpm-id = <0x82>;
				qcom,blacklist = <0x5 0x6 0x7 0x8 0x9 0xa 0xb 0xc 0xd 0xe 0xf 0x10 0x11 0x12 0x13 0x14 0x15 0x16 0x17 0x18 0x19 0x1a 0x1b 0x1c 0x1d 0x1e 0x1f 0x20 0x21 0x22 0x23 0x24 0x25 0x26 0x27 0x28 0x29 0x2a>;
			};

			mas-usb2-bam {
				cell-id = <0x6e>;
				label = "mas-usb2-bam";
				qcom,buswidth = <0x8>;
				qcom,ap-owned;
				qcom,qport = <0xf>;
				qcom,qos-mode = "fixed";
				qcom,connections = <0x2b>;
				qcom,prio1 = <0x1>;
				qcom,prio0 = <0x1>;
				qcom,bus-dev = <0x4>;
				qcom,mas-rpm-id = <0x83>;
				qcom,blacklist = <0x5 0x6 0x7 0x8 0x9 0xa 0xb 0xc 0xd 0xe 0xf 0x10 0x11 0x12 0x13 0x14 0x15 0x16 0x17 0x18 0x19 0x1a 0x1b 0x1c 0x1d 0x1e 0x1f 0x20 0x21 0x22 0x23 0x24 0x25 0x26 0x27 0x28 0x29 0x2a>;
			};

			mas-adss-dma0 {
				cell-id = <0x6f>;
				label = "mas-adss-dma0";
				qcom,buswidth = <0x4>;
				qcom,ap-owned;
				qcom,connections = <0x2c>;
				qcom,bus-dev = <0x4>;
				qcom,mas-rpm-id = <0x84>;
				qcom,blacklist = <0x5 0x6 0x7 0x8 0x9 0xa 0xb 0xc 0xd 0xe 0xf 0x10 0x11 0x12 0x13 0x14 0x15 0x16 0x17 0x18 0x19 0x1a 0x1b 0x1c 0x1d 0x1e 0x1f 0x20 0x21 0x22 0x23 0x24 0x25 0x26 0x27 0x28 0x29 0x2a>;
			};

			mas-adss-dma1 {
				cell-id = <0x70>;
				label = "mas-adss-dma1";
				qcom,buswidth = <0x4>;
				qcom,ap-owned;
				qcom,connections = <0x2c>;
				qcom,bus-dev = <0x4>;
				qcom,mas-rpm-id = <0x85>;
				qcom,blacklist = <0x5 0x6 0x7 0x8 0x9 0xa 0xb 0xc 0xd 0xe 0xf 0x10 0x11 0x12 0x13 0x14 0x15 0x16 0x17 0x18 0x19 0x1a 0x1b 0x1c 0x1d 0x1e 0x1f 0x20 0x21 0x22 0x23 0x24 0x25 0x26 0x27 0x28 0x29 0x2a>;
			};

			mas-adss-dma2 {
				cell-id = <0x71>;
				label = "mas-adss-dma2";
				qcom,buswidth = <0x4>;
				qcom,ap-owned;
				qcom,connections = <0x2c>;
				qcom,bus-dev = <0x4>;
				qcom,mas-rpm-id = <0x86>;
				qcom,blacklist = <0x5 0x6 0x7 0x8 0x9 0xa 0xb 0xc 0xd 0xe 0xf 0x10 0x11 0x12 0x13 0x14 0x15 0x16 0x17 0x18 0x19 0x1a 0x1b 0x1c 0x1d 0x1e 0x1f 0x20 0x21 0x22 0x23 0x24 0x25 0x26 0x27 0x28 0x29 0x2a>;
			};

			mas-adss-dma3 {
				cell-id = <0x72>;
				label = "mas-adss-dma3";
				qcom,buswidth = <0x4>;
				qcom,ap-owned;
				qcom,connections = <0x2c>;
				qcom,bus-dev = <0x4>;
				qcom,mas-rpm-id = <0x87>;
				qcom,blacklist = <0x5 0x6 0x7 0x8 0x9 0xa 0xb 0xc 0xd 0xe 0xf 0x10 0x11 0x12 0x13 0x14 0x15 0x16 0x17 0x18 0x19 0x1a 0x1b 0x1c 0x1d 0x1e 0x1f 0x20 0x21 0x22 0x23 0x24 0x25 0x26 0x27 0x28 0x29 0x2a>;
			};

			mas-qpic-bam {
				cell-id = <0x73>;
				label = "mas-qpic-bam";
				qcom,buswidth = <0x4>;
				qcom,ap-owned;
				qcom,connections = <0x3>;
				qcom,bus-dev = <0x4>;
				qcom,mas-rpm-id = <0x88>;
				qcom,blacklist = <0x5 0x6 0x7 0x8 0x9 0xa 0xb 0xc 0xd 0xe 0xf 0x10 0x11 0x12 0x13 0x14 0x15 0x16 0x17 0x18 0x19 0x1a 0x1b 0x1c 0x1d 0x1e 0x1f 0x20 0x21 0x22 0x23 0x24 0x25 0x26 0x27 0x28 0x29 0x2a>;
			};

			mas-spdm {
				cell-id = <0x24>;
				label = "mas-spdm";
				qcom,buswidth = <0x4>;
				qcom,ap-owned;
				qcom,connections = <0x3>;
				qcom,bus-dev = <0x4>;
				qcom,mas-rpm-id = <0x32>;
				qcom,blacklist = <0x5 0x6 0x7 0x8 0x9 0xa 0xb 0xc 0xd 0xe 0xf 0x10 0x11 0x12 0x13 0x14 0x15 0x16 0x17 0x18 0x19 0x1a 0x1b 0x1c 0x1d 0x1e 0x1f 0x20 0x21 0x22 0x23 0x24 0x25 0x26 0x27 0x28 0x29 0x2a>;
			};

			mas-pcnoc-cfg {
				cell-id = <0x58>;
				label = "mas-pcnoc-cfg";
				qcom,buswidth = <0x4>;
				qcom,ap-owned;
				qcom,connections = <0x26>;
				qcom,bus-dev = <0x4>;
				qcom,mas-rpm-id = <0x54>;
			};

			mas-tic {
				cell-id = <0x4d>;
				label = "mas-tic";
				qcom,buswidth = <0x4>;
				qcom,ap-owned;
				qcom,connections = <0x2d 0x2b>;
				qcom,bus-dev = <0x4>;
				qcom,mas-rpm-id = <0x33>;
			};

			mas-sdcc-bam {
				cell-id = <0x74>;
				label = "mas-sdcc-bam";
				qcom,buswidth = <0x8>;
				qcom,ap-owned;
				qcom,qport = <0xe>;
				qcom,qos-mode = "fixed";
				qcom,connections = <0x2b>;
				qcom,prio1 = <0x0>;
				qcom,prio0 = <0x0>;
				qcom,bus-dev = <0x4>;
				qcom,mas-rpm-id = <0x89>;
				qcom,blacklist = <0x5 0x6 0x7 0x8 0x9 0xa 0xb 0xc 0xd 0xe 0xf 0x10 0x11 0x12 0x13 0x14 0x15 0x16 0x17 0x18 0x19 0x1a 0x1b 0x1c 0x1d 0x1e 0x1f 0x20 0x21 0x22 0x23 0x24 0x25 0x26 0x27 0x28 0x29 0x2a>;
			};

			mas-snoc-pcnoc {
				cell-id = <0x2739>;
				label = "mas-snoc-pcnoc";
				qcom,buswidth = <0x4>;
				qcom,ap-owned;
				qcom,qport = <0x10>;
				qcom,qos-mode = "fixed";
				qcom,connections = <0x2d>;
				qcom,prio1 = <0x0>;
				qcom,prio0 = <0x0>;
				qcom,bus-dev = <0x4>;
				qcom,mas-rpm-id = <0x4d>;
			};

			mas-qdss-dap {
				cell-id = <0x4c>;
				label = "mas-qdss-dap";
				qcom,buswidth = <0x4>;
				qcom,ap-owned;
				qcom,connections = <0x2d 0x2b>;
				qcom,bus-dev = <0x4>;
				qcom,mas-rpm-id = <0x31>;
			};

			mas-ddrc-snoc {
				cell-id = <0x75>;
				label = "mas-ddrc-snoc";
				qcom,buswidth = <0x10>;
				qcom,ap-owned;
				qcom,connections = <0x2e 0x2f 0x30>;
				qcom,bus-dev = <0x31>;
				qcom,mas-rpm-id = <0x8a>;
				qcom,blacklist = <0x32 0x33>;
			};

			mas-wss-0 {
				cell-id = <0x76>;
				label = "mas-wss-0";
				qcom,buswidth = <0x4>;
				qcom,ap-owned;
				qcom,qport = <0x1a>;
				qcom,qos-mode = "fixed";
				qcom,connections = <0x2e 0x32>;
				qcom,prio1 = <0x0>;
				qcom,prio0 = <0x0>;
				qcom,bus-dev = <0x31>;
				qcom,mas-rpm-id = <0x8b>;
				qcom,blacklist = <0x34 0x35 0x30 0x36 0x37 0x38 0x33>;
			};

			mas-wss-1 {
				cell-id = <0x77>;
				label = "mas-wss-1";
				qcom,buswidth = <0x4>;
				qcom,ap-owned;
				qcom,qport = <0x1b>;
				qcom,qos-mode = "fixed";
				qcom,connections = <0x2e 0x32>;
				qcom,prio1 = <0x0>;
				qcom,prio0 = <0x0>;
				qcom,bus-dev = <0x31>;
				qcom,mas-rpm-id = <0x8c>;
				qcom,blacklist = <0x34 0x35 0x30 0x36 0x37 0x38 0x33>;
			};

			mas-crypto {
				cell-id = <0x2f>;
				label = "mas-crypto";
				qcom,buswidth = <0x8>;
				qcom,ap-owned;
				qcom,qport = <0x5>;
				qcom,qos-mode = "fixed";
				qcom,connections = <0x2e 0x2f 0x32>;
				qcom,prio1 = <0x0>;
				qcom,prio0 = <0x0>;
				qcom,bus-dev = <0x31>;
				qcom,mas-rpm-id = <0x17>;
				qcom,blacklist = <0x34 0x35 0x39 0x30 0x3a 0x38 0x33>;
			};

			mas-ess {
				cell-id = <0x78>;
				label = "mas-ess";
				qcom,buswidth = <0x8>;
				qcom,ap-owned;
				qcom,qport = <0x2c>;
				qcom,qos-mode = "fixed";
				qcom,connections = <0x2e 0x32>;
				qcom,prio1 = <0x0>;
				qcom,prio0 = <0x0>;
				qcom,bus-dev = <0x31>;
				qcom,mas-rpm-id = <0x8d>;
				qcom,blacklist = <0x34 0x35 0x39 0x30 0x3a 0x36 0x37 0x38 0x33>;
			};

			mas-pcie {
				cell-id = <0x2d>;
				label = "mas-pcie";
				qcom,buswidth = <0x8>;
				qcom,ap-owned;
				qcom,qport = <0x6>;
				qcom,qos-mode = "fixed";
				qcom,connections = <0x2e 0x32>;
				qcom,prio1 = <0x0>;
				qcom,prio0 = <0x0>;
				qcom,bus-dev = <0x31>;
				qcom,mas-rpm-id = <0x8e>;
				qcom,blacklist = <0x34 0x35 0x30 0x3a 0x36 0x37 0x38 0x33>;
			};

			mas-usb3 {
				cell-id = <0x3d>;
				label = "mas-usb3";
				qcom,buswidth = <0x8>;
				qcom,ap-owned;
				qcom,qport = <0x7>;
				qcom,qos-mode = "fixed";
				qcom,connections = <0x2e 0x32>;
				qcom,prio1 = <0x0>;
				qcom,prio0 = <0x0>;
				qcom,bus-dev = <0x31>;
				qcom,mas-rpm-id = <0x20>;
				qcom,blacklist = <0x34 0x35 0x39 0x30 0x3a 0x36 0x37 0x38 0x33>;
			};

			mas-qdss-etr {
				cell-id = <0x3c>;
				label = "mas-qdss-etr";
				qcom,buswidth = <0x8>;
				qcom,ap-owned;
				qcom,qport = <0x220>;
				qcom,qos-mode = "fixed";
				qcom,connections = <0x3b>;
				qcom,prio1 = <0x0>;
				qcom,prio0 = <0x0>;
				qcom,bus-dev = <0x31>;
				qcom,mas-rpm-id = <0x1f>;
				qcom,blacklist = <0x34 0x35 0x39 0x30 0x3a 0x36 0x37 0x38 0x33>;
			};

			mas-qdss-bamndp {
				cell-id = <0x79>;
				label = "mas-qdss-bamndp";
				qcom,buswidth = <0x4>;
				qcom,ap-owned;
				qcom,qport = <0x240>;
				qcom,qos-mode = "fixed";
				qcom,connections = <0x3b>;
				qcom,prio1 = <0x0>;
				qcom,prio0 = <0x0>;
				qcom,bus-dev = <0x31>;
				qcom,mas-rpm-id = <0x8f>;
				qcom,blacklist = <0x34 0x35 0x39 0x30 0x3a 0x36 0x37 0x38 0x33>;
			};

			mas-pcnoc-snoc {
				cell-id = <0x271a>;
				label = "mas-pcnoc-snoc";
				qcom,buswidth = <0x4>;
				qcom,ap-owned;
				qcom,qport = <0x180>;
				qcom,qos-mode = "fixed";
				qcom,connections = <0x2e 0x2f 0x32>;
				qcom,prio1 = <0x0>;
				qcom,prio0 = <0x0>;
				qcom,bus-dev = <0x31>;
				qcom,mas-rpm-id = <0x1d>;
				qcom,blacklist = <0x33>;
			};

			mas-snoc-cfg {
				cell-id = <0x7a>;
				label = "mas-snoc-cfg";
				qcom,buswidth = <0x4>;
				qcom,ap-owned;
				qcom,connections = <0x33>;
				qcom,bus-dev = <0x31>;
				qcom,mas-rpm-id = <0x90>;
			};

			pcnoc-m-0 {
				cell-id = <0x271e>;
				label = "pcnoc-m-0";
				qcom,buswidth = <0x4>;
				qcom,ap-owned;
				qcom,qport = <0xc>;
				qcom,qos-mode = "fixed";
				qcom,connections = <0x2b>;
				qcom,prio1 = <0x1>;
				qcom,prio0 = <0x1>;
				qcom,bus-dev = <0x4>;
				qcom,mas-rpm-id = <0x57>;
				qcom,slv-rpm-id = <0x74>;
				phandle = <0x3>;
			};

			pcnoc-m-1 {
				cell-id = <0x271f>;
				label = "pcnoc-m-1";
				qcom,buswidth = <0x4>;
				qcom,ap-owned;
				qcom,qport = <0xd>;
				qcom,qos-mode = "fixed";
				qcom,connections = <0x2b>;
				qcom,prio1 = <0x1>;
				qcom,prio0 = <0x1>;
				qcom,bus-dev = <0x4>;
				qcom,mas-rpm-id = <0x58>;
				qcom,slv-rpm-id = <0x75>;
				phandle = <0x2c>;
			};

			pcnoc-int-0 {
				cell-id = <0x271c>;
				label = "pcnoc-int-0";
				qcom,buswidth = <0x8>;
				qcom,ap-owned;
				qcom,connections = <0x3c 0x3d 0x3e 0x3f 0x40 0x41 0x42 0x43 0x44 0x45>;
				qcom,bus-dev = <0x4>;
				qcom,mas-rpm-id = <0x55>;
				qcom,slv-rpm-id = <0x72>;
				phandle = <0x2d>;
			};

			pcnoc-s-0 {
				cell-id = <0x2722>;
				label = "pcnoc-s-0";
				qcom,buswidth = <0x4>;
				qcom,ap-owned;
				qcom,connections = <0x22 0x5 0x1b 0x17>;
				qcom,bus-dev = <0x4>;
				qcom,mas-rpm-id = <0x59>;
				qcom,slv-rpm-id = <0x76>;
				phandle = <0x3e>;
			};

			pcnoc-s-1 {
				cell-id = <0x2723>;
				label = "pcnoc-s-1";
				qcom,buswidth = <0x4>;
				qcom,ap-owned;
				qcom,connections = <0x19 0x12 0x10>;
				qcom,bus-dev = <0x4>;
				qcom,mas-rpm-id = <0x5a>;
				qcom,slv-rpm-id = <0x77>;
				phandle = <0x3c>;
			};

			pcnoc-s-2 {
				cell-id = <0x2724>;
				label = "pcnoc-s-2";
				qcom,buswidth = <0x4>;
				qcom,ap-owned;
				qcom,connections = <0x1c 0x1d 0xe 0x1a>;
				qcom,bus-dev = <0x4>;
				qcom,mas-rpm-id = <0x5b>;
				qcom,slv-rpm-id = <0x78>;
				phandle = <0x3d>;
			};

			pcnoc-s-3 {
				cell-id = <0x2725>;
				label = "pcnoc-s-3";
				qcom,buswidth = <0x4>;
				qcom,ap-owned;
				qcom,connections = <0x13 0x16 0x2a 0x27>;
				qcom,bus-dev = <0x4>;
				qcom,mas-rpm-id = <0x5c>;
				qcom,slv-rpm-id = <0x79>;
				phandle = <0x45>;
			};

			pcnoc-s-4 {
				cell-id = <0x2726>;
				label = "pcnoc-s-4";
				qcom,buswidth = <0x4>;
				qcom,ap-owned;
				qcom,connections = <0x7 0x21 0x23>;
				qcom,bus-dev = <0x4>;
				qcom,mas-rpm-id = <0x5d>;
				qcom,slv-rpm-id = <0x7a>;
				phandle = <0x3f>;
			};

			pcnoc-s-5 {
				cell-id = <0x273f>;
				label = "pcnoc-s-5";
				qcom,buswidth = <0x4>;
				qcom,ap-owned;
				qcom,connections = <0x20 0x8 0x6 0x11>;
				qcom,bus-dev = <0x4>;
				qcom,mas-rpm-id = <0x81>;
				qcom,slv-rpm-id = <0xbd>;
				phandle = <0x40>;
			};

			pcnoc-s-6 {
				cell-id = <0x2740>;
				label = "pcnoc-s-6";
				qcom,buswidth = <0x4>;
				qcom,ap-owned;
				qcom,connections = <0xb 0x15 0x1e 0xd 0xa>;
				qcom,bus-dev = <0x4>;
				qcom,mas-rpm-id = <0x5e>;
				qcom,slv-rpm-id = <0x7b>;
				phandle = <0x41>;
			};

			pcnoc-s-7 {
				cell-id = <0x2752>;
				label = "pcnoc-s-7";
				qcom,buswidth = <0x4>;
				qcom,ap-owned;
				qcom,connections = <0xf 0x25 0x1f>;
				qcom,bus-dev = <0x4>;
				qcom,mas-rpm-id = <0x5f>;
				qcom,slv-rpm-id = <0x7c>;
				phandle = <0x42>;
			};

			pcnoc-s-8 {
				cell-id = <0x2727>;
				label = "pcnoc-s-8";
				qcom,buswidth = <0x4>;
				qcom,ap-owned;
				qcom,connections = <0x29 0xc 0x24>;
				qcom,bus-dev = <0x4>;
				qcom,mas-rpm-id = <0x60>;
				qcom,slv-rpm-id = <0x7d>;
				phandle = <0x43>;
			};

			pcnoc-s-9 {
				cell-id = <0x2728>;
				label = "pcnoc-s-9";
				qcom,buswidth = <0x4>;
				qcom,ap-owned;
				qcom,connections = <0x9 0x28 0x18 0x14>;
				qcom,bus-dev = <0x4>;
				qcom,mas-rpm-id = <0x61>;
				qcom,slv-rpm-id = <0x7e>;
				phandle = <0x44>;
			};

			snoc-int-0 {
				cell-id = <0x2714>;
				label = "snoc-int-0";
				qcom,buswidth = <0x8>;
				qcom,ap-owned;
				qcom,connections = <0x46 0x3a>;
				qcom,bus-dev = <0x31>;
				qcom,mas-rpm-id = <0x63>;
				qcom,slv-rpm-id = <0x82>;
				phandle = <0x2e>;
			};

			snoc-int-1 {
				cell-id = <0x2715>;
				label = "snoc-int-1";
				qcom,buswidth = <0x8>;
				qcom,ap-owned;
				qcom,connections = <0x38 0x39 0x35 0x34 0x36 0x37>;
				qcom,bus-dev = <0x31>;
				qcom,mas-rpm-id = <0x64>;
				qcom,slv-rpm-id = <0x83>;
				phandle = <0x2f>;
			};

			qdss-int {
				cell-id = <0x2719>;
				label = "qdss-int";
				qcom,buswidth = <0x8>;
				qcom,ap-owned;
				qcom,connections = <0x2e 0x32>;
				qcom,bus-dev = <0x31>;
				qcom,mas-rpm-id = <0x62>;
				qcom,slv-rpm-id = <0x80>;
				phandle = <0x3b>;
			};

			slv-clk-ctl {
				cell-id = <0x26c>;
				label = "slv-clk-ctl";
				qcom,buswidth = <0x4>;
				qcom,ap-owned;
				qcom,bus-dev = <0x4>;
				qcom,slv-rpm-id = <0x2f>;
				phandle = <0x22>;
			};

			slv-security {
				cell-id = <0x26e>;
				label = "slv-security";
				qcom,buswidth = <0x4>;
				qcom,ap-owned;
				qcom,bus-dev = <0x4>;
				qcom,slv-rpm-id = <0x31>;
				phandle = <0x1b>;
			};

			slv-tcsr {
				cell-id = <0x26f>;
				label = "slv-tcsr";
				qcom,buswidth = <0x4>;
				qcom,ap-owned;
				qcom,bus-dev = <0x4>;
				qcom,slv-rpm-id = <0x32>;
				phandle = <0x5>;
			};

			slv-tlmm {
				cell-id = <0x270>;
				label = "slv-tlmm";
				qcom,buswidth = <0x4>;
				qcom,ap-owned;
				qcom,bus-dev = <0x4>;
				qcom,slv-rpm-id = <0x33>;
				phandle = <0x17>;
			};

			slv-imem-cfg {
				cell-id = <0x273>;
				label = "slv-imem-cfg";
				qcom,buswidth = <0x4>;
				qcom,ap-owned;
				qcom,bus-dev = <0x4>;
				qcom,slv-rpm-id = <0x36>;
				phandle = <0x10>;
			};

			slv-prng {
				cell-id = <0x26a>;
				label = "slv-prng";
				qcom,buswidth = <0x4>;
				qcom,ap-owned;
				qcom,bus-dev = <0x4>;
				qcom,slv-rpm-id = <0x2c>;
				phandle = <0x12>;
			};

			slv-prng-apu-cfg {
				cell-id = <0x2cc>;
				label = "slv-prng-apu-cfg";
				qcom,buswidth = <0x4>;
				qcom,ap-owned;
				qcom,bus-dev = <0x4>;
				qcom,slv-rpm-id = <0xbe>;
				phandle = <0x19>;
			};

			slv-boot-rom {
				cell-id = <0x276>;
				label = "slv-boot-rom";
				qcom,buswidth = <0x4>;
				qcom,ap-owned;
				qcom,bus-dev = <0x4>;
				qcom,slv-rpm-id = <0x39>;
				phandle = <0x1a>;
			};

			slv-spdm {
				cell-id = <0x279>;
				label = "slv-spdm";
				qcom,buswidth = <0x4>;
				qcom,ap-owned;
				qcom,bus-dev = <0x4>;
				qcom,slv-rpm-id = <0x3c>;
				phandle = <0x1c>;
			};

			slv-pcnoc-cfg {
				cell-id = <0x281>;
				label = "slv-pcnoc-cfg";
				qcom,buswidth = <0x4>;
				qcom,ap-owned;
				qcom,bus-dev = <0x4>;
				qcom,slv-rpm-id = <0x45>;
				phandle = <0xe>;
			};

			slv-pcnoc-mpu-cfg {
				cell-id = <0x2cd>;
				label = "slv-pcnoc-mpu-cfg";
				qcom,buswidth = <0x4>;
				qcom,ap-owned;
				qcom,bus-dev = <0x4>;
				qcom,slv-rpm-id = <0xbf>;
				phandle = <0x1d>;
			};

			slv-gcnt {
				cell-id = <0x2ce>;
				label = "slv-gcnt";
				qcom,buswidth = <0x4>;
				qcom,ap-owned;
				qcom,bus-dev = <0x4>;
				qcom,slv-rpm-id = <0xc0>;
				phandle = <0x16>;
			};

			slv-qdss-cfg {
				cell-id = <0x27b>;
				label = "slv-qdss-cfg";
				qcom,buswidth = <0x4>;
				qcom,ap-owned;
				qcom,bus-dev = <0x4>;
				qcom,slv-rpm-id = <0x3f>;
				phandle = <0x13>;
			};

			slv-snoc-cfg {
				cell-id = <0x282>;
				label = "slv-snoc-cfg";
				qcom,buswidth = <0x4>;
				qcom,ap-owned;
				qcom,bus-dev = <0x4>;
				qcom,slv-rpm-id = <0x46>;
				phandle = <0x2a>;
			};

			slv-snoc-mpu-cfg {
				cell-id = <0x27e>;
				label = "slv-snoc-mpu-cfg";
				qcom,buswidth = <0x4>;
				qcom,ap-owned;
				qcom,bus-dev = <0x4>;
				qcom,slv-rpm-id = <0x43>;
				phandle = <0x27>;
			};

			slv-adss-cfg {
				cell-id = <0x2cf>;
				label = "slv-adss-cfg";
				qcom,buswidth = <0x4>;
				qcom,ap-owned;
				qcom,bus-dev = <0x4>;
				qcom,slv-rpm-id = <0xc1>;
				phandle = <0x7>;
			};

			slv-adss-apu {
				cell-id = <0x2d0>;
				label = "slv-adss-apu";
				qcom,buswidth = <0x4>;
				qcom,ap-owned;
				qcom,bus-dev = <0x4>;
				qcom,slv-rpm-id = <0xc2>;
				phandle = <0x23>;
			};

			slv-adss-vmidmt-cfg {
				cell-id = <0x2d0>;
				label = "slv-adss-vmidmt-cfg";
				qcom,buswidth = <0x4>;
				qcom,ap-owned;
				qcom,bus-dev = <0x4>;
				qcom,slv-rpm-id = <0xc3>;
				phandle = <0x21>;
			};

			slv-qhss-apu-cfg {
				cell-id = <0x2d1>;
				label = "slv-qhss-apu-cfg";
				qcom,buswidth = <0x4>;
				qcom,ap-owned;
				qcom,bus-dev = <0x4>;
				qcom,slv-rpm-id = <0xc4>;
				phandle = <0x20>;
			};

			slv-mdio {
				cell-id = <0x2d2>;
				label = "slv-mdio";
				qcom,buswidth = <0x4>;
				qcom,ap-owned;
				qcom,bus-dev = <0x4>;
				qcom,slv-rpm-id = <0xc5>;
				phandle = <0x6>;
			};

			slv-fephy-cfg {
				cell-id = <0x2d3>;
				label = "slv-fephy-cfg";
				qcom,buswidth = <0x4>;
				qcom,ap-owned;
				qcom,bus-dev = <0x4>;
				qcom,slv-rpm-id = <0xc6>;
				phandle = <0x8>;
			};

			slv-srif {
				cell-id = <0x2d4>;
				label = "slv-srif";
				qcom,buswidth = <0x4>;
				qcom,ap-owned;
				qcom,bus-dev = <0x4>;
				qcom,slv-rpm-id = <0xc7>;
				phandle = <0x11>;
			};

			slv-ddrc-cfg {
				cell-id = <0x2db>;
				label = "slv-ddrc-cfg";
				qcom,buswidth = <0x4>;
				qcom,ap-owned;
				qcom,bus-dev = <0x4>;
				qcom,slv-rpm-id = <0xc8>;
				phandle = <0xd>;
			};

			slv-ddrc-apu-cfg {
				cell-id = <0x2dc>;
				label = "slv-ddrc-apu-cfg";
				qcom,buswidth = <0x4>;
				qcom,ap-owned;
				qcom,bus-dev = <0x4>;
				qcom,slv-rpm-id = <0xc9>;
				phandle = <0x15>;
			};

			slv-ddrc-mpu0-cfg {
				cell-id = <0x2dd>;
				label = "slv-ddrc-mpu0-cfg";
				qcom,buswidth = <0x4>;
				qcom,ap-owned;
				qcom,bus-dev = <0x4>;
				qcom,slv-rpm-id = <0xca>;
				phandle = <0xb>;
			};

			slv-ddrc-mpu1-cfg {
				cell-id = <0x2de>;
				label = "slv-ddrc-mpu1-cfg";
				qcom,buswidth = <0x4>;
				qcom,ap-owned;
				qcom,bus-dev = <0x4>;
				qcom,slv-rpm-id = <0xcb>;
				phandle = <0xa>;
			};

			slv-ddrc-mpu2-cfg {
				cell-id = <0x2de>;
				label = "slv-ddrc-mpu2-cfg";
				qcom,buswidth = <0x4>;
				qcom,ap-owned;
				qcom,bus-dev = <0x4>;
				qcom,slv-rpm-id = <0xd2>;
				phandle = <0x1e>;
			};

			slv-ess-vmidmt-cfg {
				cell-id = <0x2df>;
				label = "slv-ess-vmidmt-cfg";
				qcom,buswidth = <0x4>;
				qcom,ap-owned;
				qcom,bus-dev = <0x4>;
				qcom,slv-rpm-id = <0xd3>;
				phandle = <0x1f>;
			};

			slv-ess-apu-cfg {
				cell-id = <0x2e0>;
				label = "slv-ess-apu-cfg";
				qcom,buswidth = <0x4>;
				qcom,ap-owned;
				qcom,bus-dev = <0x4>;
				qcom,slv-rpm-id = <0xd4>;
				phandle = <0xf>;
			};

			slv-usb2-cfg {
				cell-id = <0x2e1>;
				label = "slv-usb2-cfg";
				qcom,buswidth = <0x4>;
				qcom,ap-owned;
				qcom,bus-dev = <0x4>;
				qcom,slv-rpm-id = <0xd5>;
				phandle = <0x25>;
			};

			slv-blsp-cfg {
				cell-id = <0x2e2>;
				label = "slv-blsp-cfg";
				qcom,buswidth = <0x4>;
				qcom,ap-owned;
				qcom,bus-dev = <0x4>;
				qcom,slv-rpm-id = <0xd6>;
				phandle = <0x24>;
			};

			slv-qpic-cfg {
				cell-id = <0x2e3>;
				label = "slv-qpic-cfg";
				qcom,buswidth = <0x4>;
				qcom,ap-owned;
				qcom,bus-dev = <0x4>;
				qcom,slv-rpm-id = <0xd7>;
				phandle = <0xc>;
			};

			slv-sdcc-cfg {
				cell-id = <0x2e4>;
				label = "slv-sdcc-cfg";
				qcom,buswidth = <0x4>;
				qcom,ap-owned;
				qcom,bus-dev = <0x4>;
				qcom,slv-rpm-id = <0xd8>;
				phandle = <0x29>;
			};

			slv-wss0-vmidmt-cfg {
				cell-id = <0x2e5>;
				label = "slv-wss0-vmidmt-cfg";
				qcom,buswidth = <0x4>;
				qcom,ap-owned;
				qcom,bus-dev = <0x4>;
				qcom,slv-rpm-id = <0xd9>;
				phandle = <0x18>;
			};

			slv-wss0-apu-cfg {
				cell-id = <0x2e6>;
				label = "slv-wss0-apu-cfg";
				qcom,buswidth = <0x4>;
				qcom,ap-owned;
				qcom,bus-dev = <0x4>;
				qcom,slv-rpm-id = <0xda>;
				phandle = <0x14>;
			};

			slv-wss1-vmidmt-cfg {
				cell-id = <0x2e7>;
				label = "slv-wss1-vmidmt-cfg";
				qcom,buswidth = <0x4>;
				qcom,ap-owned;
				qcom,bus-dev = <0x4>;
				qcom,slv-rpm-id = <0xdb>;
				phandle = <0x28>;
			};

			slv-wss1-apu-cfg {
				cell-id = <0x2e8>;
				label = "slv-wss1-apu-cfg";
				qcom,buswidth = <0x4>;
				qcom,ap-owned;
				qcom,bus-dev = <0x4>;
				qcom,slv-rpm-id = <0xdc>;
				phandle = <0x9>;
			};

			slv-pcnoc-snoc {
				cell-id = <0x271b>;
				label = "slv-pcnoc-snoc";
				qcom,buswidth = <0x4>;
				qcom,ap-owned;
				qcom,bus-dev = <0x4>;
				qcom,slv-rpm-id = <0x2d>;
				phandle = <0x2b>;
			};

			slv-srvc-pcnoc {
				cell-id = <0x2e9>;
				label = "slv-srvc-pcnoc";
				qcom,buswidth = <0x4>;
				qcom,ap-owned;
				qcom,bus-dev = <0x4>;
				qcom,slv-rpm-id = <0xdd>;
				phandle = <0x26>;
			};

			slv-snoc-ddrc-m1 {
				cell-id = <0x2ea>;
				label = "slv-snoc-ddrc-m1";
				qcom,buswidth = <0x8>;
				qcom,ap-owned;
				qcom,bus-dev = <0x31>;
				qcom,slv-rpm-id = <0xde>;
				phandle = <0x32>;
			};

			slv-a7ss {
				cell-id = <0x2eb>;
				label = "slv-a7ss";
				qcom,buswidth = <0x4>;
				qcom,ap-owned;
				qcom,bus-dev = <0x31>;
				qcom,slv-rpm-id = <0xdf>;
				phandle = <0x39>;
			};

			slv-ocimem {
				cell-id = <0x249>;
				label = "slv-ocimem";
				qcom,buswidth = <0x8>;
				qcom,ap-owned;
				qcom,bus-dev = <0x31>;
				qcom,slv-rpm-id = <0x1a>;
				phandle = <0x46>;
			};

			slv-wss0-cfg {
				cell-id = <0x2ec>;
				label = "slv-wss0-cfg";
				qcom,buswidth = <0x4>;
				qcom,ap-owned;
				qcom,bus-dev = <0x31>;
				qcom,slv-rpm-id = <0xe0>;
				phandle = <0x37>;
			};

			slv-wss1-cfg {
				cell-id = <0x2ed>;
				label = "slv-wss1-cfg";
				qcom,buswidth = <0x4>;
				qcom,ap-owned;
				qcom,bus-dev = <0x31>;
				qcom,slv-rpm-id = <0xe1>;
				phandle = <0x36>;
			};

			slv-pcie {
				cell-id = <0x2ee>;
				label = "slv-pcie";
				qcom,buswidth = <0x8>;
				qcom,ap-owned;
				qcom,bus-dev = <0x31>;
				qcom,slv-rpm-id = <0xe2>;
				phandle = <0x30>;
			};

			slv-usb3-cfg {
				cell-id = <0x2ef>;
				label = "slv-usb3-cfg";
				qcom,buswidth = <0x4>;
				qcom,ap-owned;
				qcom,bus-dev = <0x31>;
				qcom,slv-rpm-id = <0xe3>;
				phandle = <0x34>;
			};

			slv-crypto-cfg {
				cell-id = <0x2f0>;
				label = "slv-crypto-cfg";
				qcom,buswidth = <0x4>;
				qcom,ap-owned;
				qcom,bus-dev = <0x31>;
				qcom,slv-rpm-id = <0xe4>;
				phandle = <0x38>;
			};

			slv-ess-cfg {
				cell-id = <0x2f1>;
				label = "slv-ess-cfg";
				qcom,buswidth = <0x4>;
				qcom,ap-owned;
				qcom,bus-dev = <0x31>;
				qcom,slv-rpm-id = <0xe5>;
				phandle = <0x35>;
			};

			slv-qdss-stm {
				cell-id = <0x24c>;
				label = "slv-qdss-stm";
				qcom,buswidth = <0x4>;
				qcom,ap-owned;
				qcom,bus-dev = <0x31>;
				qcom,slv-rpm-id = <0x1e>;
				phandle = <0x3a>;
			};

			slv-srvc-snoc {
				cell-id = <0x2f2>;
				label = "slv-srvc-snoc";
				qcom,buswidth = <0x8>;
				qcom,ap-owned;
				qcom,bus-dev = <0x31>;
				qcom,slv-rpm-id = <0xe6>;
				phandle = <0x33>;
			};
		};

		interrupt-controller@b000000 {
			compatible = "qcom,msm-qgic2";
			interrupt-controller;
			#interrupt-cells = <0x3>;
			reg = <0xb000000 0x1000 0xb002000 0x1000>;
			phandle = <0x1>;
		};

		counter@4a1000 {
			compatible = "qcom,qca-gcnt";
			reg = <0x4a1000 0x4>;
		};

		clock-controller@1800000 {
			compatible = "qcom,gcc-ipq40xx";
			#clock-cells = <0x1>;
			#reset-cells = <0x1>;
			reg = <0x1800000 0x60000>;
			phandle = <0x2>;
		};

		clock-controller@7700038 {
			compatible = "qcom,adcc-ipq40xx";
			#clock-cells = <0x1>;
			#reset-cells = <0x1>;
			reg = <0x7700038 0x1dc>;
			status = "ok";
		};

		timer {
			compatible = "arm,armv7-timer";
			interrupts = <0x1 0x2 0xf08 0x1 0x3 0xf08 0x1 0x4 0xf08 0x1 0x1 0xf08>;
			clock-frequency = <0x2dc6c00>;
		};

		restart@4ab000 {
			compatible = "qcom,pshold";
			reg = <0x4ab000 0x4>;
		};

		watchdog@b017000 {
			compatible = "qcom,kpss-wdt-ipq40xx";
			reg = <0xb017000 0x40>;
			interrupt-names = "bark_irq";
			interrupts = <0x0 0x3 0x0>;
			clocks = <0x47>;
			timeout-sec = <0xa>;
			wdt_res = <0x4>;
			wdt_en = <0x8>;
			wdt_bark_time = <0x10>;
			wdt_bite_time = <0x14>;
			status = "ok";
		};

		a7ss_base@b088000 {
			compatible = "qcom,arm-cortex-acc";
			reg = <0xb088000 0x1000>;
		};

		pinctrl@0x01000000 {
			compatible = "qcom,ipq40xx-pinctrl";
			reg = <0x1000000 0x300000>;
			gpio-controller;
			#gpio-cells = <0x2>;
			interrupt-controller;
			#interrupt-cells = <0x2>;
			interrupts = <0x0 0xd0 0x0>;

			serial_pinmux {
				phandle = <0x48>;

				mux {
					pins = "gpio60", "gpio61";
					function = "blsp_uart0";
					bias-disable;
				};
			};

			spi_0_pinmux {
				phandle = <0x49>;

				mux {
					pins = "gpio54", "gpio55", "gpio56", "gpio57";
					function = "blsp_spi0";
					bias-disable;
				};
			};
		};

		serial@78af000 {
			compatible = "qcom,msm-uartdm-v1.4", "qcom,msm-uartdm";
			reg = <0x78af000 0x200>;
			interrupts = <0x0 0x6b 0x0>;
			status = "ok";
			clocks = <0x2 0x1a 0x2 0x15>;
			clock-names = "core", "iface";
			pinctrl-0 = <0x48>;
			pinctrl-names = "default";
		};

		serial@78b0000 {
			compatible = "qcom,msm-uartdm-v1.4", "qcom,msm-uartdm";
			reg = <0x78b0000 0x200>;
			interrupts = <0x0 0x6c 0x0>;
			status = "disabled";
			clocks = <0x2 0x1b 0x2 0x15>;
			clock-names = "core", "iface";
		};

		qcom,sps {
			compatible = "qcom,msm_sps_4k";
			qcom,device-type = <0x3>;
			qcom,pipe-attr-ee;
		};

		spi@78b5000 {
			compatible = "qcom,spi-qup-v2";
			#address-cells = <0x1>;
			#size-cells = <0x0>;
			reg-names = "spi_physical", "spi_bam_physical";
			reg = <0x78b5000 0x600 0x7884000 0x23000>;
			interrupt-names = "spi_irq", "spi_bam_irq";
			interrupts = <0x0 0x5f 0x0 0x0 0xee 0x0>;
			spi-max-frequency = <0x16e3600>;
			clocks = <0x2 0x17 0x2 0x15>;
			clock-names = "core_clk", "iface_clk";
			qcom,infinite-mode = <0x0>;
			qcom,bam-consumer-pipe-index = <0x4>;
			qcom,bam-producer-pipe-index = <0x5>;
			qcom,master-id = <0x0>;
			status = "ok";
			pinctrl-0 = <0x49>;
			pinctrl-names = "default";

			m25p80@0 {
				#address-cells = <0x1>;
				#size-cells = <0x1>;
				compatible = "m25p80";
				reg = <0x0>;
				spi-max-frequency = <0x17d7840>;

				partition@0 {
					reg = <0x100000 0x0>;
					label = "RouterOS";
				};

				partition@1 {
					reg = <0x80000 0x40000>;
					label = "RouterBoot";
				};
			};
		};

		qcom,nand@7980000 {
			compatible = "qcom,msm-nand";
			reg = <0x7980000 0x40000 0x7984000 0x1a000>;
			reg-names = "nand_phys", "bam_phys";
			interrupts = <0x0 0x65 0x0>;
			interrupt-names = "bam_irq";
			qcom,msm-bus,name = "qpic_nand";
			qcom,msm-bus,num-cases = <0x2>;
			qcom,msm-bus,num-paths = <0x1>;
			qcom,msm-bus,vectors-KBps = <0x5b 0x200 0x0 0x0 0x5b 0x200 0x61a80 0xc3500>;
			clock-names = "iface_clk", "core_clk";
			clocks = <0x2 0x2b 0x2 0x2c>;
			status = "disabled";
		};

		tcsr@194b000 {
			compatible = "qcom,tcsr";
			reg = <0x194b000 0x100>;
			qcom,usb-hsphy-mode-select = <0xe700e7>;
			status = "ok";
		};

		ess_tcsr@1953000 {
			compatible = "qcom,tcsr";
			reg = <0x1953000 0x1000>;
			qcom,ess-interface-select = <0x0>;
		};

		ssphy@0 {
			compatible = "qca,uni-ssphy";
			reg = <0x9a000 0x800>;
			reg-names = "phy_base";
			resets = <0x2 0xc>;
			reset-names = "por_rst";
			qca,host = <0x1>;
			qca,emulation = <0x0>;
			status = "disabled";
			phandle = <0x4b>;
		};

		ssphy@1 {
			compatible = "qca,dummy-ssphy";
			status = "disabled";
			reg = <0x0 0x0>;
			phandle = <0x4d>;
		};

		rng@0x00022000 {
			compatible = "qcom,prng";
			reg = <0x22000 0x140>;
			clocks = <0x2 0x2a>;
			clock-names = "core";
		};

		i2c@78b7000 {
			compatible = "qcom,i2c-msm-v2";
			#address-cells = <0x1>;
			#size-cells = <0x0>;
			reg-names = "qup_phys_addr", "bam_phys_addr";
			reg = <0x78b7000 0x600 0x7884000 0x23000>;
			interrupt-names = "qup_irq", "bam_irq";
			interrupts = <0x0 0x61 0x0 0x0 0xee 0x0>;
			clocks = <0x2 0x15 0x2 0x16>;
			clock-names = "iface_clk", "core_clk";
			qcom,clk-freq-out = <0x186a0>;
			qcom,clk-freq-in = <0x122ae10>;
			qcom,noise-rjct-scl = <0x0>;
			qcom,noise-rjct-sda = <0x0>;
			qcom,bam-pipe-idx-cons = <0x8>;
			qcom,bam-pipe-idx-prod = <0x9>;
			qcom,master-id = <0x0>;
			status = "disabled";
		};

		qcrypto@8e20000 {
			compatible = "qcom,qcrypto";
			reg = <0x8e20000 0x20000 0x8e04000 0x20000>;
			reg-names = "crypto-base", "crypto-bam-base";
			interrupts = <0x0 0xcf 0x0>;
			qcom,bam-pipe-pair = <0x1>;
			qcom,ce-hw-instance = <0x0>;
			qcom,ce-hw-shared = <0x1>;
			qcom,ce-device = <0x0>;
			qcom,ce-opp-freq = <0x7735940>;
			clocks = <0x2 0x22 0x2 0x21 0x2 0x20>;
			clock-names = "core_clk", "bus_clk", "iface_clk";
			status = "ok";
		};

		qcedev@8e20000 {
			compatible = "qcom,qcedev";
			reg = <0x8e20000 0x20000 0x8e04000 0x20000>;
			reg-names = "crypto-base", "crypto-bam-base";
			interrupts = <0x0 0xcf 0x0>;
			qcom,bam-pipe-pair = <0x1>;
			qcom,ce-hw-instance = <0x0>;
			qcom,ce-hw-shared = <0x1>;
			qcom,ce-device = <0x0>;
			qcom,ce-opp-freq = <0x7735940>;
			clocks = <0x2 0x22 0x2 0x21 0x2 0x20>;
			clock-names = "core_clk", "bus_clk", "iface_clk";
			status = "ok";
		};

		tcsr@1949000 {
			compatible = "qcom,tcsr";
			reg = <0x1949000 0x100>;
			qcom,wifi_glb_cfg = <0x41000000>;
		};

		tcsr@1957000 {
			compatible = "qcom,tcsr";
			reg = <0x1957000 0x100>;
			qcom,wifi_noc_memtype_m0_m2 = <0x2222222>;
		};

		wifi@a000000 {
			compatible = "qca,wifi-ipq40xx";
			reg = <0xa000000 0x200000>;
			core-id = <0x0>;
			resets = <0x2 0x0 0x2 0x1 0x2 0x2 0x2 0x3 0x2 0x4 0x2 0x5>;
			reset-names = "wifi_cpu_init", "wifi_radio_srif", "wifi_radio_warm", "wifi_radio_cold", "wifi_core_warm", "wifi_core_cold";
			clocks = <0x2 0x3a 0x2 0x3b 0x2 0x3c>;
			clock-names = "wifi_wcss_cmd", "wifi_wcss_ref", "wifi_wcss_rtc";
			interrupts = <0x0 0x20 0x1 0x0 0x21 0x1 0x0 0x22 0x1 0x0 0x23 0x1 0x0 0x24 0x1 0x0 0x25 0x1 0x0 0x26 0x1 0x0 0x27 0x1 0x0 0x28 0x1 0x0 0x29 0x1 0x0 0x2a 0x1 0x0 0x2b 0x1 0x0 0x2c 0x1 0x0 0x2d 0x1 0x0 0x2e 0x1 0x0 0x2f 0x1 0x0 0xa8 0x0>;
			interrupt-names = "msi0", "msi1", "msi2", "msi3", "msi4", "msi5", "msi6", "msi7", "msi8", "msi9", "msi10", "msi11", "msi12", "msi13", "msi14", "msi15", "legacy";
			status = "ok";
			qca,msi_addr = <0xb006040>;
			qca,msi_base = <0x40>;
		};

		wifi@a800000 {
			compatible = "qca,wifi-ipq40xx";
			reg = <0xa800000 0x200000>;
			core-id = <0x1>;
			resets = <0x2 0x6 0x2 0x7 0x2 0x8 0x2 0x9 0x2 0xa 0x2 0xb>;
			reset-names = "wifi_cpu_init", "wifi_radio_srif", "wifi_radio_warm", "wifi_radio_cold", "wifi_core_warm", "wifi_core_cold";
			clocks = <0x2 0x3d 0x2 0x3e 0x2 0x3f>;
			clock-names = "wifi_wcss_cmd", "wifi_wcss_ref", "wifi_wcss_rtc";
			interrupts = <0x0 0x30 0x1 0x0 0x31 0x1 0x0 0x32 0x1 0x0 0x33 0x1 0x0 0x34 0x1 0x0 0x35 0x1 0x0 0x36 0x1 0x0 0x37 0x1 0x0 0x38 0x1 0x0 0x39 0x1 0x0 0x3a 0x1 0x0 0x3b 0x1 0x0 0x3c 0x1 0x0 0x3d 0x1 0x0 0x3e 0x1 0x0 0x3f 0x1 0x0 0xa9 0x0>;
			interrupt-names = "msi0", "msi1", "msi2", "msi3", "msi4", "msi5", "msi6", "msi7", "msi8", "msi9", "msi10", "msi11", "msi12", "msi13", "msi14", "msi15", "legacy";
			status = "ok";
			qca,msi_addr = <0xb006040>;
			qca,msi_base = <0x50>;
		};

		hsphy@a6000 {
			compatible = "qca,baldur-usb3-hsphy";
			reg = <0xa6000 0x40>;
			reg-names = "phy_base";
			resets = <0x2 0xd 0x2 0xe>;
			reset-names = "por_rst", "srif_rst";
			qca,host = <0x1>;
			qca,emulation = <0x0>;
			status = "disabled";
			phandle = <0x4a>;
		};

		hsphy@a8000 {
			compatible = "qca,baldur-usb2-hsphy";
			reg = <0xa8000 0x40>;
			reg-names = "phy_base";
			resets = <0x2 0xf 0x2 0x10>;
			reset-names = "por_rst", "srif_rst";
			qca,host = <0x1>;
			qca,emulation = <0x0>;
			status = "disabled";
			phandle = <0x4c>;
		};

		usb3@8a00000 {
			compatible = "qca,dwc3";
			#address-cells = <0x1>;
			#size-cells = <0x1>;
			ranges;
			reg = <0x8af8800 0x100>;
			reg-names = "qscratch_base";
			clocks = <0x2 0x37 0x2 0x38 0x2 0x39>;
			clock-names = "master", "sleep", "mock_utmi";
			qca,host = <0x1>;
			status = "disabled";

			dwc3@8a00000 {
				compatible = "snps,dwc3";
				reg = <0x8a00000 0xf8000>;
				interrupts = <0x0 0x84 0x0>;
				usb-phy = <0x4a 0x4b>;
				phy-names = "usb2-phy", "usb3-phy";
				tx-fifo-resize;
				dr_mode = "host";
				usb2-susphy-quirk;
				usb2-host-discon-quirk;
				usb2-host-discon-phy-misc-reg = <0x24>;
				usb2-host-discon-mask = <0x100>;
			};
		};

		usb2@6000000 {
			compatible = "qca,dwc3";
			#address-cells = <0x1>;
			#size-cells = <0x1>;
			ranges;
			reg = <0x60f8800 0x100>;
			reg-names = "qscratch_base";
			clocks = <0x2 0x34 0x2 0x35 0x2 0x36>;
			clock-names = "master", "sleep", "mock_utmi";
			qca,host = <0x1>;
			status = "disabled";

			dwc3@6000000 {
				compatible = "snps,dwc3";
				reg = <0x6000000 0xf8000>;
				interrupts = <0x0 0x88 0x0>;
				usb-phy = <0x4c 0x4d>;
				phy-names = "usb2-phy", "usb3-phy";
				tx-fifo-resize;
				dr_mode = "host";
				usb2-susphy-quirk;
				usb2-host-discon-quirk;
				usb2-host-discon-phy-misc-reg = <0x24>;
				usb2-host-discon-mask = <0x100>;
			};
		};

		msmgpio {
			compatible = "msmgpio";
			gpio-controller;
			#gpio-cells = <0x2>;
			phandle = <0x4f>;
		};

		poe-out-simple {
			compatible = "rb,poe-out-simple";
			status = "disabled";
		};

		edma@c080000 {
			compatible = "qcom,ess-edma";
			reg = <0xc080000 0x8000>;
			qcom,page-mode = <0x0>;
			qcom,rx_head_buf_size = <0x604>;
			qcom,wan_port_id_mask = <0x10>;
			qcom,mdio_supported;
			qcom,phy_mdio_addr = <0x4>;
			qcom,poll_required = <0x1>;
			qcom,forced_speed = <0x3e8>;
			qcom,forced_duplex = <0x1>;
			interrupts = <0x0 0x41 0x1 0x0 0x42 0x1 0x0 0x43 0x1 0x0 0x44 0x1 0x0 0x45 0x1 0x0 0x46 0x1 0x0 0x47 0x1 0x0 0x48 0x1 0x0 0x49 0x1 0x0 0x4a 0x1 0x0 0x4b 0x1 0x0 0x4c 0x1 0x0 0x4d 0x1 0x0 0x4e 0x1 0x0 0x4f 0x1 0x0 0x50 0x1 0x0 0xf0 0x1 0x0 0xf1 0x1 0x0 0xf2 0x1 0x0 0xf3 0x1 0x0 0xf4 0x1 0x0 0xf5 0x1 0x0 0xf6 0x1 0x0 0xf7 0x1 0x0 0xf8 0x1 0x0 0xf9 0x1 0x0 0xfa 0x1 0x0 0xfb 0x1 0x0 0xfc 0x1 0x0 0xfd 0x1 0x0 0xfe 0x1 0x0 0xff 0x1>;
			port_map = <0x100004 0xffffffff>;

			gmac0 {
				local-mac-address = [00 00 00 00 00 00];
			};

			gmac1 {
				local-mac-address = [00 00 00 00 00 00];
			};
		};

		qcom,pcie@80000 {
			compatible = "qcom,msm_pcie";
			cell-index = <0x0>;
			qcom,ctrl-amt = <0x1>;
			reg = <0x80000 0x2000 0x99000 0x800 0x40000000 0xf1d 0x40000f20 0xa8 0x40100000 0x1000 0x40200000 0x100000 0x40300000 0xd00000>;
			reg-names = "parf", "phy", "dm_core", "elbi", "conf", "io", "bars";
			#address-cells = <0x0>;
			interrupt-parent = <0x4e>;
			interrupts = <0x0 0x1 0x2 0x3 0x4 0x5 0x6 0x7 0x8 0x9 0xa 0xb 0xc>;
			#interrupt-cells = <0x1>;
			interrupt-map-mask = <0xffffffff>;
			interrupt-map = <0x0 0x1 0x0 0x8d 0x0 0x1 0x1 0x0 0x8e 0x0 0x2 0x1 0x0 0x8f 0x0 0x3 0x1 0x0 0x90 0x0 0x4 0x1 0x0 0x91 0x0 0x5 0x1 0x0 0x92 0x0 0x6 0x1 0x0 0x93 0x0 0x7 0x1 0x0 0x94 0x0 0x8 0x1 0x0 0x95 0x0 0x9 0x1 0x0 0x96 0x0 0xa 0x1 0x0 0x97 0x0 0xb 0x1 0x0 0x98 0x0>;
			interrupt-names = "int_msi", "int_a", "int_b", "int_c", "int_d", "int_pls_pme", "int_pme_legacy", "int_pls_err", "int_aer_legacy", "int_pls_link_up", "int_pls_link_down", "int_bridge_flush_n", "int_wake";
			qcom,ep-latency = <0xa>;
			clocks = <0x2 0x26 0x2 0x27 0x2 0x28>;
			clock-names = "pcie_0_cfg_ahb_clk", "pcie_0_mstr_axi_clk", "pcie_0_slv_axi_clk";
			max-clock-frequency-hz = <0x0 0x0 0x0>;
			resets = <0x2 0x1c 0x2 0x1b 0x2 0x1a 0x2 0x19 0x2 0x18 0x2 0x17 0x2 0x16 0x2 0x15 0x2 0x14 0x2 0x13 0x2 0x12 0x2 0x11>;
			reset-names = "pcie_rst_axi_m_ares", "pcie_rst_axi_s_ares", "pcie_rst_pipe_ares", "pcie_rst_axi_m_vmidmt_ares", "pcie_rst_axi_s_xpu_ares", "pcie_rst_parf_xpu_ares", "pcie_rst_phy_ares", "pcie_rst_axi_m_sticky_ares", "pcie_rst_pipe_sticky_ares", "pcie_rst_pwr_ares", "pcie_rst_ahb_res", "pcie_rst_phy_ahb_ares";
			status = "ok";
			gpio-booster = <0x4f 0x42 0x0>;
			phandle = <0x4e>;
		};

		ledc@1937000 {
			compatible = "qca,ledc";
			reg = <0x1937000 0x20070>;
			reg-names = "ledc_base_addr";
			qcom,tcsr_ledc_values = <0x320193 0x14720800 0x20d 0x0 0x0 0xffffffff 0x0 0x7 0x7d0010 0x0 0x10482090 0x3fffdfc>;
			qcom,ledc_blink_indices_cnt = <0x0>;
			qcom,ledc_blink_indices = <0x0>;
			status = "disabled";
		};

		pmu {
			compatible = "arm,cortex-a7-pmu";
			interrupts = <0x1 0x7 0xf04>;
		};

		sdhci@7824000 {
			compatible = "qcom,sdhci-msm-v4";
			reg = <0x7824900 0x11c 0x7824000 0x800>;
			interrupts = <0x0 0x7b 0x0 0x0 0x8a 0x0>;
			bus-width = <0x8>;
			clocks = <0x2 0x2e 0x2 0x2d>;
			clock-names = "core", "iface";
			status = "disabled";
		};

		ess-switch@c000000 {
			compatible = "qcom,ess-switch";
			reg = <0xc000000 0x80000>;
			switch_access_mode = "local bus";
			resets = <0x2 0x1d 0x2 0x4e 0x2 0x4f 0x2 0x50 0x2 0x51 0x2 0x52>;
			reset-names = "ess_rst", "ess_mac1_clk_dis", "ess_mac2_clk_dis", "ess_mac3_clk_dis", "ess_mac4_clk_dis", "ess_mac5_clk_dis";
			clocks = <0x2 0x23>;
			clock-names = "ess_clk";
			switch_cpu_bmp = <0x1>;
			switch_lan_bmp = <0x1e>;
			switch_wan_bmp = <0x20>;
			switch_mac_mode = <0x0>;
			switch_initvlas = <0x7c 0x54>;
		};

		ess-psgmii@98000 {
			compatible = "qcom,ess-psgmii";
			reg = <0x98000 0x800>;
			psgmii_access_mode = "local bus";
			resets = <0x2 0x4d>;
			reset-names = "psgmii_rst";
		};

		mdio@90000 {
			#address-cells = <0x1>;
			#size-cells = <0x1>;
			compatible = "qcom,ipq40xx-mdio";
			reg = <0x90000 0x64>;

			ethernet-phy@0 {
				reg = <0x0 0x4>;
			};

			ethernet-phy@1 {
				reg = <0x1 0x4>;
			};

			ethernet-phy@2 {
				reg = <0x2 0x4>;
			};

			ethernet-phy@3 {
				reg = <0x3 0x4>;
			};

			ethernet-phy@4 {
				reg = <0x4 0x4>;
			};
		};

		qca,scm_restart_reason {
			compatible = "qca,scm_restart_reason";
		};

		cpu_freq_ipq40xx {
			compatible = "qca,ipq40xx_freq";
			clock-latency = <0x186a0>;
			qcom,cpufreq-table = <0xaece0 0x5dc00 0x64d48 0x6d600 0x77240 0x7d000 0x831a8 0x89f08 0x91c08 0x9a4c0 0xa4100 0xbb800 0xc8ed8 0xdac00>;
		};
	};

	memory@80000000 {
		device_type = "memory";
		reg = <0x80000000 0x10000000>;
	};

	reserved-memory {
		#address-cells = <0x1>;
		#size-cells = <0x1>;
		ranges;

		rsvd1@87000000 {
			reg = <0x87000000 0x500000>;
			no-map;
		};

		wifi_dump@87500000 {
			reg = <0x87500000 0x600000>;
			no-map;
		};

		rsvd2@87B00000 {
			reg = <0x87b00000 0x500000>;
			no-map;
		};
	};

	leds {
		compatible = "leds-rb";

		user-led {
			gpios = <0x4f 0x3 0x0>;
		};

		power-led {
			gpios = <0x4f 0x0 0x0>;
			default-state = "keep";
		};

		led1 {
			gpios = <0x4f 0x3a 0x0>;
		};

		led2 {
			gpios = <0x4f 0x1 0x0>;
		};

		led3 {
			gpios = <0x4f 0x2 0x0>;
		};

		led4 {
			gpios = <0x4f 0x4 0x0>;
		};

		led5 {
			gpios = <0x4f 0x5 0x0>;
		};

		button {
			gpios = <0x4f 0x3f 0x1>;
			default-state = "input";
		};
	};
};


File: /dts\rb5009.dts
/dts-v1/;

/ {
	sha1 = "8c6defd127";
	compatible = "marvell,armada7040-db-E\0marvell,armada7040-db\0marvell,armada7040\0marvell,armada-ap806-quad\0marvell,armada-ap806";
	#address-cells = <0x02>;
	#size-cells = <0x02>;
	model = "RB5009";
	mac-address = [00 01 02 03 04 05];

	aliases {
		serial0 = "/ap806/config-space@f0000000/serial@512000";
		serial1 = "/ap806/config-space@f0000000/serial@512100";
		gpio0 = "/ap806/config-space@f0000000/system-controller@6f4000/gpio@1040";
		spi0 = "/ap806/config-space@f0000000/spi@510600";
		gpio1 = "/cp0/config-space/system-controller@440000/gpio@100";
		gpio2 = "/cp0/config-space/system-controller@440000/gpio@140";
		spi1 = "/cp0/config-space/spi@700600";
		spi2 = "/cp0/config-space/spi@700680";
		ethernet0 = "/cp0/config-space/ethernet@0/eth0";
		ethernet1 = "/cp0/config-space/ethernet@0/eth1";
	};

	psci {
		compatible = "arm,psci-0.2";
		method = "smc";
	};

	cpus {
		#address-cells = <0x01>;
		#size-cells = <0x00>;

		idle_states {
			entry_method = "arm,pcsi";

			cpu-sleep-0 {
				compatible = "arm,idle-state";
				local-timer-stop;
				arm,psci-suspend-param = <0x10000>;
				entry-latency-us = <0x50>;
				exit-latency-us = <0xa0>;
				min-residency-us = <0x140>;
				phandle = <0x02>;
			};

			cluster-sleep-0 {
				compatible = "arm,idle-state";
				local-timer-stop;
				arm,psci-suspend-param = <0x1010000>;
				entry-latency-us = <0x1f4>;
				exit-latency-us = <0x3e8>;
				min-residency-us = <0x9c4>;
			};
		};

		cpu@0 {
			device_type = "cpu";
			compatible = "arm,cortex-a72\0arm,armv8";
			reg = <0x00>;
			enable-method = "psci";
			clocks = <0x01 0x00>;
			cpu-idle-states = <0x02>;
			i-cache-size = <0xc000>;
			i-cache-line-size = <0x40>;
			i-cache-sets = <0x100>;
			d-cache-size = <0x8000>;
			d-cache-line-size = <0x40>;
			d-cache-sets = <0x100>;
			next-level-cache = <0x03>;
		};

		cpu@1 {
			device_type = "cpu";
			compatible = "arm,cortex-a72\0arm,armv8";
			reg = <0x01>;
			enable-method = "psci";
			clocks = <0x01 0x00>;
			cpu-idle-states = <0x02>;
			i-cache-size = <0xc000>;
			i-cache-line-size = <0x40>;
			i-cache-sets = <0x100>;
			d-cache-size = <0x8000>;
			d-cache-line-size = <0x40>;
			d-cache-sets = <0x100>;
			next-level-cache = <0x03>;
		};

		cpu@100 {
			device_type = "cpu";
			compatible = "arm,cortex-a72\0arm,armv8";
			reg = <0x100>;
			enable-method = "psci";
			clocks = <0x01 0x01>;
			cpu-idle-states = <0x02>;
			i-cache-size = <0xc000>;
			i-cache-line-size = <0x40>;
			i-cache-sets = <0x100>;
			d-cache-size = <0x8000>;
			d-cache-line-size = <0x40>;
			d-cache-sets = <0x100>;
			next-level-cache = <0x04>;
		};

		cpu@101 {
			device_type = "cpu";
			compatible = "arm,cortex-a72\0arm,armv8";
			reg = <0x101>;
			enable-method = "psci";
			clocks = <0x01 0x01>;
			cpu-idle-states = <0x02>;
			i-cache-size = <0xc000>;
			i-cache-line-size = <0x40>;
			i-cache-sets = <0x100>;
			d-cache-size = <0x8000>;
			d-cache-line-size = <0x40>;
			d-cache-sets = <0x100>;
			next-level-cache = <0x04>;
		};

		l2-cache0 {
			compatible = "cache";
			cache-size = <0x80000>;
			cache-line-size = <0x40>;
			cache-sets = <0x200>;
			phandle = <0x03>;
		};

		l2-cache1 {
			compatible = "cache";
			cache-size = <0x80000>;
			cache-line-size = <0x40>;
			cache-sets = <0x200>;
			phandle = <0x04>;
		};
	};

	reserved-memory {
		#address-cells = <0x02>;
		#size-cells = <0x02>;
		ranges;

		psci-area@4000000 {
			reg = <0x00 0x4000000 0x00 0x200000>;
			no-map;
		};

		tee@4400000 {
			reg = <0x00 0x4400000 0x00 0x1000000>;
			no-map;
		};
	};

	ap806 {
		#address-cells = <0x02>;
		#size-cells = <0x02>;
		compatible = "simple-bus";
		interrupt-parent = <0x05>;
		ranges;

		config-space@f0000000 {
			#address-cells = <0x01>;
			#size-cells = <0x01>;
			compatible = "simple-bus";
			ranges = <0x00 0x00 0xf0000000 0x1000000>;

			interrupt-controller@210000 {
				compatible = "arm,gic-400";
				#interrupt-cells = <0x03>;
				#address-cells = <0x01>;
				#size-cells = <0x01>;
				ranges;
				interrupt-controller;
				interrupts = <0x01 0x09 0xf04>;
				reg = <0x210000 0x10000 0x220000 0x20000 0x240000 0x20000 0x260000 0x20000>;
				phandle = <0x05>;

				v2m@280000 {
					compatible = "arm,gic-v2m-frame";
					msi-controller;
					reg = <0x280000 0x1000>;
					arm,msi-base-spi = <0xa0>;
					arm,msi-num-spis = <0x20>;
					phandle = <0x08>;
				};

				v2m@290000 {
					compatible = "arm,gic-v2m-frame";
					msi-controller;
					reg = <0x290000 0x1000>;
					arm,msi-base-spi = <0xc0>;
					arm,msi-num-spis = <0x20>;
				};

				v2m@2a0000 {
					compatible = "arm,gic-v2m-frame";
					msi-controller;
					reg = <0x2a0000 0x1000>;
					arm,msi-base-spi = <0xe0>;
					arm,msi-num-spis = <0x20>;
				};

				v2m@2b0000 {
					compatible = "arm,gic-v2m-frame";
					msi-controller;
					reg = <0x2b0000 0x1000>;
					arm,msi-base-spi = <0x100>;
					arm,msi-num-spis = <0x20>;
				};
			};

			timer {
				compatible = "arm,armv8-timer";
				interrupts = <0x01 0x0d 0xf08 0x01 0x0e 0xf08 0x01 0x0b 0xf08 0x01 0x0a 0xf08>;
			};

			pmu {
				compatible = "arm,cortex-a72-pmu";
				interrupt-parent = <0x06>;
				interrupts = <0x11>;
			};

			iommu@5000000 {
				compatible = "arm,mmu-500";
				reg = <0x100000 0x100000>;
				dma-coherent;
				#iommu-cells = <0x01>;
				#global-interrupts = <0x01>;
				interrupts = <0x00 0x06 0x04 0x00 0x06 0x04 0x00 0x06 0x04 0x00 0x06 0x04 0x00 0x06 0x04 0x00 0x06 0x04 0x00 0x06 0x04 0x00 0x06 0x04 0x00 0x06 0x04>;
			};

			axim-ddr-rd@840000 {
				compatible = "marvell,coresight-axim\0arm,primecell";
				reg = <0x840000 0x1000>;
				clocks = <0x07 0x03 0x07 0x05>;
				clock-names = "apb_pclk\0hclk";
				bus-width = <0x28>;

				port@0 {
				};
			};

			axim-ddr-wr@841000 {
				compatible = "marvell,coresight-axim\0arm,primecell";
				reg = <0x841000 0x1000>;
				clocks = <0x07 0x03 0x07 0x05>;
				clock-names = "apb_pclk\0hclk";
				bus-width = <0x28>;

				port@0 {
				};
			};

			axim-sb-rd@848000 {
				compatible = "marvell,coresight-axim\0arm,primecell";
				reg = <0x848000 0x1000>;
				clocks = <0x07 0x03 0x07 0x05>;
				clock-names = "apb_pclk\0hclk";
				bus-width = <0x28>;

				port@0 {
				};
			};

			axim-sb-wr@849000 {
				compatible = "marvell,coresight-axim\0arm,primecell";
				reg = <0x849000 0x1000>;
				clocks = <0x07 0x03 0x07 0x05>;
				clock-names = "apb_pclk\0hclk";
				bus-width = <0x28>;

				port@0 {
				};
			};

			odmi@300000 {
				compatible = "marvell,odmi-controller";
				interrupt-controller;
				msi-controller;
				marvell,odmi-frames = <0x04>;
				reg = <0x300000 0x4000 0x304000 0x4000 0x308000 0x4000 0x30c000 0x4000>;
				marvell,spi-base = <0x80 0x88 0x90 0x98>;
			};

			gicp@3f0040 {
				compatible = "marvell,ap806-gicp";
				reg = <0x3f0040 0x10>;
				marvell,spi-ranges = <0x40 0x40 0x120 0x40>;
				msi-controller;
				phandle = <0x14>;
			};

			interrupt-controller@3f0100 {
				compatible = "marvell,armada-8k-pic";
				reg = <0x3f0100 0x10>;
				#interrupt-cells = <0x01>;
				interrupt-controller;
				interrupts = <0x01 0x0f 0x04>;
				phandle = <0x06>;
			};

			xor@400000 {
				compatible = "marvell,armada-7k-xor\0marvell,xor-v2";
				reg = <0x400000 0x1000 0x410000 0x1000>;
				msi-parent = <0x08>;
				clocks = <0x07 0x03>;
				dma-coherent;
				phandle = <0x09>;
			};

			xor@420000 {
				compatible = "marvell,armada-7k-xor\0marvell,xor-v2";
				reg = <0x420000 0x1000 0x430000 0x1000>;
				msi-parent = <0x08>;
				clocks = <0x07 0x03>;
				dma-coherent;
				phandle = <0x0a>;
			};

			xor@440000 {
				compatible = "marvell,armada-7k-xor\0marvell,xor-v2";
				reg = <0x440000 0x1000 0x450000 0x1000>;
				msi-parent = <0x08>;
				clocks = <0x07 0x03>;
				dma-coherent;
				phandle = <0x0b>;
			};

			xor@460000 {
				compatible = "marvell,armada-7k-xor\0marvell,xor-v2";
				reg = <0x460000 0x1000 0x470000 0x1000>;
				msi-parent = <0x08>;
				clocks = <0x07 0x03>;
				dma-coherent;
				phandle = <0x0c>;
			};

			uio_xor0 {
				compatible = "marvell,uio-xor-v2";
				xor_access = <0x09>;
			};

			uio_xor1 {
				compatible = "marvell,uio-xor-v2";
				xor_access = <0x0a>;
			};

			uio_xor2 {
				compatible = "marvell,uio-xor-v2";
				xor_access = <0x0b>;
			};

			uio_xor3 {
				compatible = "marvell,uio-xor-v2";
				xor_access = <0x0c>;
			};

			spi@510600 {
				compatible = "marvell,armada-380-spi";
				reg = <0x510600 0x50>;
				#address-cells = <0x01>;
				#size-cells = <0x00>;
				interrupts = <0x00 0x15 0x04>;
				clocks = <0x07 0x03>;
				status = "okay";

				spi-flash@0 {
					#address-cells = <0x01>;
					#size-cells = <0x01>;
					compatible = "m25p80";
					reg = <0x00>;
					spi-max-frequency = <0x2faf080>;

					mtd0@00000000 {
						label = "RouterBoot";
						reg = <0x00 0x100000>;
					};
				};
			};

			i2c@511000 {
				compatible = "marvell,mv78230-i2c";
				reg = <0x511000 0x20>;
				#address-cells = <0x01>;
				#size-cells = <0x00>;
				interrupts = <0x00 0x14 0x04>;
				timeout-ms = <0x3e8>;
				clocks = <0x07 0x03>;
				status = "disabled";
			};

			serial@512000 {
				compatible = "snps,dw-apb-uart";
				reg = <0x512000 0x100>;
				reg-shift = <0x02>;
				interrupts = <0x00 0x13 0x04>;
				reg-io-width = <0x01>;
				clocks = <0x07 0x03>;
				status = "okay";
				pinctrl-0 = <0x0d>;
				pinctrl-names = "default";
			};

			serial@512100 {
				compatible = "snps,dw-apb-uart";
				reg = <0x512100 0x100>;
				reg-shift = <0x02>;
				interrupts = <0x00 0x1d 0x04>;
				reg-io-width = <0x01>;
				clocks = <0x07 0x03>;
				status = "disabled";
			};

			watchdog@610000 {
				compatible = "arm,sbsa-gwdt";
				reg = <0x610000 0x1000 0x600000 0x1000>;
				interrupts = <0x00 0x02 0x04>;
			};

			sdhci@6e0000 {
				compatible = "marvell,armada-ap806-sdhci";
				reg = <0x6e0000 0x300>;
				interrupts = <0x00 0x10 0x04>;
				clock-names = "core";
				clocks = <0x07 0x04>;
				dma-coherent;
				status = "disabled";
				bus-width = <0x04>;
				no-1-8-v;
				non-removable;
			};

			system-controller@6f4000 {
				compatible = "syscon\0simple-mfd";
				reg = <0x6f4000 0x2000>;

				pinctrl {
					compatible = "marvell,ap806-pinctrl";
					phandle = <0x0e>;

					uart0-pins {
						marvell,pins = "mpp11\0mpp19";
						marvell,function = "uart0";
						phandle = <0x0d>;
					};

					ap-poe-pins {
						marvell,pins = "mpp4\0mpp5";
						marvell,function = "gpio";
						phandle = <0x19>;
					};
				};

				gpio@1040 {
					compatible = "marvell,armada-8k-gpio";
					offset = <0x1040>;
					ngpios = <0x14>;
					gpio-controller;
					#gpio-cells = <0x02>;
					gpio-ranges = <0x0e 0x00 0x00 0x14>;
				};

				clock {
					compatible = "marvell,ap806-clock";
					#clock-cells = <0x01>;
					phandle = <0x07>;
				};
			};

			system-controller@6f8000 {
				compatible = "syscon\0simple-mfd";
				reg = <0x6f8000 0x1000>;
				#address-cells = <0x01>;
				#size-cells = <0x01>;

				thermal-sensor@80 {
					compatible = "marvell,armada-ap806-thermal";
					reg = <0x80 0x10>;
					#thermal-sensor-cells = <0x01>;
					phandle = <0x23>;
				};

				clock-cpu {
					compatible = "marvell,ap806-cpu-clock";
					clocks = <0x07 0x00 0x07 0x01>;
					#clock-cells = <0x01>;
					phandle = <0x01>;
				};
			};

			revision-info@610fcc {
				compatible = "marvell,ap806-rev-info";
				reg = <0x610fcc 0x04>;
			};

			musdk_cma {
				compatible = "marvell,musdk-cma";
				dma-coherent;
			};

			agnic-plat {
				compatible = "marvell,armada-giu-nic";
				reg = <0x6f00a0 0x08>;
				msi-parent = <0x08>;
				dma-coherent;
			};

			uio_agnic_0 {
				compatible = "marvell,armada-giu-nic-uio";
				reg = <0x6f0000 0x1000 0x280000 0x1000>;
				reg-names = "agnic_regs\0msi_regs";
			};
		};
	};

	firmware {

		optee {
			compatible = "linaro,optee-tz";
			method = "smc";
			status = "okay";
		};
	};

	cp0 {
		#address-cells = <0x02>;
		#size-cells = <0x02>;
		compatible = "simple-bus";
		interrupt-parent = <0x0f>;
		ranges;

		config-space {
			#address-cells = <0x01>;
			#size-cells = <0x01>;
			compatible = "simple-bus";
			ranges = <0x00 0x00 0xf2000000 0x2000000 0x2000000 0x00 0xf9000000 0x1000000>;

			ethernet@0 {
				compatible = "marvell,armada-7k-pp22";
				reg = <0x00 0x100000 0x129000 0xb000>;
				clocks = <0x10 0x01 0x03 0x10 0x01 0x09 0x10 0x01 0x05 0x10 0x01 0x06 0x10 0x01 0x12>;
				clock-names = "pp_clk\0gop_clk\0mg_clk\0mg_core_clk\0axi_clk";
				marvell,system-controller = <0x11>;
				status = "okay";
				dma-coherent;
				cm3-mem = <0x12>;

				eth0 {
					interrupts = <0x00 0x27 0x04 0x00 0x2b 0x04 0x00 0x2f 0x04 0x00 0x33 0x04 0x00 0x37 0x04 0x00 0x3b 0x04 0x00 0x3f 0x04 0x00 0x43 0x04 0x00 0x47 0x04 0x00 0x81 0x04>;
					interrupt-names = "hif0\0hif1\0hif2\0hif3\0hif4\0hif5\0hif6\0hif7\0hif8\0link";
					port-id = <0x00>;
					gop-port-id = <0x00>;
					status = "okay";
					phy-mode = "10gbase-kr";
					phys = <0x13 0x00>;
				};

				eth1 {
					interrupts = <0x00 0x28 0x04 0x00 0x2c 0x04 0x00 0x30 0x04 0x00 0x34 0x04 0x00 0x38 0x04 0x00 0x3c 0x04 0x00 0x40 0x04 0x00 0x44 0x04 0x00 0x48 0x04 0x00 0x80 0x04>;
					interrupt-names = "hif0\0hif1\0hif2\0hif3\0hif4\0hif5\0hif6\0hif7\0hif8\0link";
					port-id = <0x01>;
					gop-port-id = <0x02>;
					status = "disabled";
				};

				eth2 {
					interrupts = <0x00 0x29 0x04 0x00 0x2d 0x04 0x00 0x31 0x04 0x00 0x35 0x04 0x00 0x39 0x04 0x00 0x3d 0x04 0x00 0x41 0x04 0x00 0x45 0x04 0x00 0x49 0x04 0x00 0x7f 0x04>;
					interrupt-names = "hif0\0hif1\0hif2\0hif3\0hif4\0hif5\0hif6\0hif7\0hif8\0link";
					port-id = <0x02>;
					gop-port-id = <0x03>;
					status = "disabled";
				};
			};

			uio_pp_0@0 {
				compatible = "generic-uio";
				reg = <0x00 0x90000 0x130000 0x6000 0x220000 0x1000>;
				reg-names = "pp\0mspg\0cm3";
			};

			phy@120000 {
				compatible = "marvell,comphy-cp110";
				reg = <0x120000 0x6000>;
				reg-names = "comphy";
				marvell,system-controller = <0x11>;
				#address-cells = <0x01>;
				#size-cells = <0x00>;

				phy@0 {
					reg = <0x00>;
					#phy-cells = <0x01>;
				};

				phy@1 {
					reg = <0x01>;
					#phy-cells = <0x01>;
				};

				phy@2 {
					reg = <0x02>;
					#phy-cells = <0x01>;
					phandle = <0x13>;
				};

				phy@3 {
					reg = <0x03>;
					#phy-cells = <0x01>;
				};

				phy@4 {
					reg = <0x04>;
					#phy-cells = <0x01>;
				};

				phy@5 {
					reg = <0x05>;
					#phy-cells = <0x01>;
				};
			};

			mdio@12a200 {
				#address-cells = <0x01>;
				#size-cells = <0x00>;
				compatible = "marvell,orion-mdio";
				reg = <0x12a200 0x10>;
				clocks = <0x10 0x01 0x09 0x10 0x01 0x05 0x10 0x01 0x06 0x10 0x01 0x12>;
				status = "okay";

				ethernet-phy@0 {
					reg = <0x00>;
				};
			};

			mdio@12a600 {
				#address-cells = <0x01>;
				#size-cells = <0x00>;
				compatible = "marvell,xmdio";
				reg = <0x12a600 0x10>;
				clocks = <0x10 0x01 0x05 0x10 0x01 0x06 0x10 0x01 0x12>;
				status = "disabled";
			};

			interrupt-controller@1e0000 {
				compatible = "marvell,cp110-icu";
				reg = <0x1e0000 0x440>;
				#interrupt-cells = <0x03>;
				interrupt-controller;
				msi-parent = <0x14>;
				phandle = <0x0f>;
			};

			cm3@220000 {
				compatible = "mmio-sram";
				reg = <0x220000 0x800>;
				#address-cells = <0x01>;
				#size-cells = <0x01>;
				ranges = <0x00 0x220000 0x800>;
				phandle = <0x12>;
			};

			rtc@284000 {
				compatible = "marvell,armada-8k-rtc";
				reg = <0x284000 0x20 0x284080 0x24>;
				reg-names = "rtc\0rtc-soc";
				interrupts = <0x00 0x4d 0x04>;
			};

			axim-cp-rd@3c5000 {
				compatible = "marvell,coresight-axim\0arm,primecell";
				reg = <0x3c5000 0x1000>;
				clocks = <0x10 0x01 0x03>;
				clock-names = "apb_pclk";
				bus-width = <0x28>;

				port@0 {
				};
			};

			axim-cp-wr@3c6000 {
				compatible = "marvell,coresight-axim\0arm,primecell";
				reg = <0x3c6000 0x1000>;
				clocks = <0x10 0x01 0x03>;
				clock-names = "apb_pclk";
				bus-width = <0x28>;

				port@0 {
				};
			};

			axim-ppv2-rd@3c0000 {
				compatible = "marvell,coresight-axim\0arm,primecell";
				reg = <0x3c0000 0x1000>;
				clocks = <0x10 0x01 0x03>;
				clock-names = "apb_pclk";
				bus-width = <0x28>;

				port@0 {
				};
			};

			axim-ppv2-wr@3c1000 {
				compatible = "marvell,coresight-axim\0arm,primecell";
				reg = <0x3c1000 0x1000>;
				clocks = <0x10 0x01 0x03>;
				clock-names = "apb_pclk";
				bus-width = <0x28>;

				port@0 {
				};
			};

			axim-hb1-rd@3c8000 {
				compatible = "marvell,coresight-axim\0arm,primecell";
				reg = <0x3c8000 0x1000>;
				clocks = <0x10 0x01 0x03>;
				clock-names = "apb_pclk";
				bus-width = <0x28>;
				status = "disabled";

				port@0 {
				};
			};

			axim-hb1-wr@3c9000 {
				compatible = "marvell,coresight-axim\0arm,primecell";
				reg = <0x3c9000 0x1000>;
				clocks = <0x10 0x01 0x03>;
				clock-names = "apb_pclk";
				bus-width = <0x28>;
				status = "disabled";

				port@0 {
				};
			};

			system-controller@440000 {
				compatible = "syscon\0simple-mfd";
				reg = <0x440000 0x2000>;
				phandle = <0x11>;

				clock {
					compatible = "marvell,cp110-clock";
					#clock-cells = <0x02>;
					phandle = <0x10>;
				};

				gpio@100 {
					compatible = "marvell,armada-8k-gpio";
					offset = <0x100>;
					ngpios = <0x20>;
					gpio-controller;
					#gpio-cells = <0x02>;
					gpio-ranges = <0x15 0x00 0x00 0x20>;
					interrupt-controller;
					interrupts = <0x00 0x56 0x04 0x00 0x55 0x04 0x00 0x54 0x04 0x00 0x53 0x04>;
					status = "okay";
					phandle = <0x21>;
				};

				gpio@140 {
					compatible = "marvell,armada-8k-gpio";
					offset = <0x140>;
					ngpios = <0x1f>;
					gpio-controller;
					#gpio-cells = <0x02>;
					gpio-ranges = <0x15 0x00 0x20 0x1f>;
					interrupt-controller;
					interrupts = <0x00 0x52 0x04 0x00 0x51 0x04 0x00 0x50 0x04 0x00 0x4f 0x04>;
					status = "okay";
					phandle = <0x22>;
				};

				pinctrl {
					compatible = "marvell,armada-7k-pinctrl";
					phandle = <0x15>;

					sdhi-pins {
						marvell,pins = "mpp56\0mpp57\0mpp58\0mpp59\0mpp60\0mpp61\0mpp62";
						marvell,function = "sdio";
					};

					nand-pins {
						marvell,pins = "mpp15\0mpp16\0mpp17\0mpp18\0mpp19\0mpp20\0mpp21\0mpp22\0mpp23\0mpp24\0mpp25\0mpp26\0mpp27";
						marvell,function = "dev";
						phandle = <0x1d>;
					};

					nand-rb {
						marvell,pins = "mpp13";
						marvell,function = "nf";
						phandle = <0x1e>;
					};

					cp-i2c-pins {
						marvell,pins = "mpp0\0mpp1";
						marvell,function = "mss_i2c";
						phandle = <0x1b>;
					};

					cp-uart0-pins {
						marvell,pins = "mpp29\0mpp30";
						marvell,function = "uart0";
						phandle = <0x1c>;
					};

					led-rb-pins {
						marvell,pins = "mpp28\0mpp52\0mpp53\0mpp54\0mpp58\0mpp59\0mpp60\0mpp61\0mpp62";
						marvell,function = "gpio";
						phandle = <0x20>;
					};

					cp-poe-pins {
						marvell,pins = "mpp8";
						marvell,function = "gpio";
						phandle = <0x1a>;
					};

					cp-spi-poe-pins {
						marvell,pins = "mpp47\0mpp48\0mpp49\0mpp50";
						marvell,function = "spi1";
						phandle = <0x18>;
					};
				};
			};

			system-controller@400000 {
				compatible = "syscon\0simple-mfd";
				reg = <0x400000 0x1000>;
				#address-cells = <0x01>;
				#size-cells = <0x01>;

				thermal-sensor@70 {
					compatible = "marvell,armada-cp110-thermal";
					reg = <0x70 0x10>;
					#thermal-sensor-cells = <0x01>;
					phandle = <0x24>;
				};
			};

			usb3@500000 {
				compatible = "generic-xhci";
				reg = <0x500000 0x4000>;
				dma-coherent;
				interrupts = <0x00 0x6a 0x04>;
				clock-names = "core\0reg";
				clocks = <0x10 0x01 0x16 0x10 0x01 0x10>;
				status = "disabled";
			};

			usb3@510000 {
				compatible = "generic-xhci";
				reg = <0x510000 0x4000>;
				dma-coherent;
				interrupts = <0x00 0x69 0x04>;
				clock-names = "core\0reg";
				clocks = <0x10 0x01 0x17 0x10 0x01 0x10>;
				status = "okay";
			};

			sata@540000 {
				compatible = "generic-ahci";
				reg = <0x540000 0x30000>;
				dma-coherent;
				interrupts = <0x00 0x6b 0x04>;
				clocks = <0x10 0x01 0x0f 0x10 0x01 0x10>;
				status = "disabled";
				#address-cells = <0x01>;
				#size-cells = <0x00>;

				sata-port@0 {
					reg = <0x00>;
					satus = "disabled";
				};

				sata-port@1 {
					reg = <0x01>;
					status = "disabled";
				};
			};

			xor@6a0000 {
				compatible = "marvell,armada-7k-xor\0marvell,xor-v2";
				reg = <0x6a0000 0x1000 0x6b0000 0x1000>;
				dma-coherent;
				msi-parent = <0x08>;
				clock-names = "core\0reg";
				clocks = <0x10 0x01 0x08 0x10 0x01 0x0e>;
				phandle = <0x16>;
			};

			xor@6c0000 {
				compatible = "marvell,armada-7k-xor\0marvell,xor-v2";
				reg = <0x6c0000 0x1000 0x6d0000 0x1000>;
				dma-coherent;
				msi-parent = <0x08>;
				clock-names = "core\0reg";
				clocks = <0x10 0x01 0x07 0x10 0x01 0x0e>;
				phandle = <0x17>;
			};

			cp0_uio_xor0 {
				compatible = "marvell,uio-xor-v2";
				xor_access = <0x16>;
			};

			cp0_uio_xor1 {
				compatible = "marvell,uio-xor-v2";
				xor_access = <0x17>;
			};

			spi@700600 {
				compatible = "marvell,armada-380-spi";
				reg = <0x700600 0x50>;
				#address-cells = <0x01>;
				#size-cells = <0x00>;
				cell-index = <0x01>;
				clock-names = "core\0axi";
				clocks = <0x10 0x01 0x15 0x10 0x01 0x11>;
				status = "disabled";
			};

			spi@700680 {
				compatible = "marvell,armada-380-spi";
				reg = <0x700680 0x50>;
				#address-cells = <0x01>;
				#size-cells = <0x00>;
				cell-index = <0x02>;
				clock-names = "core\0axi";
				clocks = <0x10 0x01 0x15 0x10 0x01 0x11>;
				status = "okay";
				pinctrl-0 = <0x18>;
				pinctrl-names = "default";

				spi-poe@0 {
					status = "okay";
					pinctrl-0 = <0x19 0x1a>;
					pinctrl-names = "default";
					#address-cells = <0x01>;
					#size-cells = <0x01>;
					compatible = "rb-spi-poe";
					reg = <0x00>;
					spi-max-frequency = <0x1e8480>;
					reset = <0x28>;
					swdelay = <0x2710>;
					swcs = <0xff>;
					swclk = <0x05>;
					swdio = <0x04>;
					chCnt = <0x08>;
					psuCnt = <0x01>;
					chMap = <0x07 0x06 0x05 0x04 0x03 0x02 0x01 0x00>;
					in-label = "psu\0psu";
					curr-label = "psu\0psu";
					temp-label = "board";
				};
			};

			i2c@701000 {
				compatible = "marvell,mv78230-i2c";
				reg = <0x701000 0x20>;
				#address-cells = <0x01>;
				#size-cells = <0x00>;
				interrupts = <0x00 0x78 0x04>;
				clock-names = "core\0reg";
				clocks = <0x10 0x01 0x15 0x10 0x01 0x11>;
				status = "okay";
				pinctrl-0 = <0x1b>;
				pinctrl-names = "default";
				clock-frequency = <0x186a0>;
			};

			i2c@701100 {
				compatible = "marvell,mv78230-i2c";
				reg = <0x701100 0x20>;
				#address-cells = <0x01>;
				#size-cells = <0x00>;
				interrupts = <0x00 0x79 0x04>;
				clock-names = "core\0reg";
				clocks = <0x10 0x01 0x15 0x10 0x01 0x11>;
				status = "disabled";
			};

			serial@702000 {
				compatible = "snps,dw-apb-uart";
				reg = <0x702000 0x100>;
				reg-shift = <0x02>;
				interrupts = <0x00 0x7a 0x04>;
				reg-io-width = <0x01>;
				clock-names = "baudclk\0apb_pclk";
				clocks = <0x10 0x01 0x15 0x10 0x01 0x11>;
				status = "okay";
				pinctrl-0 = <0x1c>;
				pinctrl-names = "default";
			};

			serial@702100 {
				compatible = "snps,dw-apb-uart";
				reg = <0x702100 0x100>;
				reg-shift = <0x02>;
				interrupts = <0x00 0x7b 0x04>;
				reg-io-width = <0x01>;
				clock-names = "baudclk\0apb_pclk";
				clocks = <0x10 0x01 0x15 0x10 0x01 0x11>;
				status = "disabled";
			};

			serial@702200 {
				compatible = "snps,dw-apb-uart";
				reg = <0x702200 0x100>;
				reg-shift = <0x02>;
				interrupts = <0x00 0x7c 0x04>;
				reg-io-width = <0x01>;
				clock-names = "baudclk\0apb_pclk";
				clocks = <0x10 0x01 0x15 0x10 0x01 0x11>;
				status = "disabled";
			};

			serial@702300 {
				compatible = "snps,dw-apb-uart";
				reg = <0x702300 0x100>;
				reg-shift = <0x02>;
				interrupts = <0x00 0x7d 0x04>;
				reg-io-width = <0x01>;
				clock-names = "baudclk\0apb_pclk";
				clocks = <0x10 0x01 0x15 0x10 0x01 0x11>;
				status = "disabled";
			};

			nand@720000 {
				compatible = "marvell,armada-8k-nand-controller\0marvell,armada370-nand-controller";
				reg = <0x720000 0x54>;
				#address-cells = <0x01>;
				#size-cells = <0x00>;
				interrupts = <0x00 0x73 0x04>;
				clock-names = "core\0reg";
				clocks = <0x10 0x01 0x02 0x10 0x01 0x11>;
				marvell,system-controller = <0x11>;
				status = "okay";
				pinctrl-names = "default";
				pinctrl-0 = <0x1d 0x1e>;

				nand@0 {
					reg = <0x00>;
					label = "main-storage";
					nand-rb = <0x00>;
					nand-ecc-mode = "hw";
					nand-ecc-strength = <0x04>;
					nand-ecc-step-size = <0x200>;

					partitions {
						compatible = "fixed-partitions";
						#address-cells = <0x01>;
						#size-cells = <0x01>;

						partition@0 {
							reg = <0x00 0x800000>;
							label = "RouterBoard NAND Boot";
						};

						partition@1 {
							reg = <0x800000 0x00>;
							label = "RouterBoard NAND Main";
						};
					};
				};
			};

			trng@760000 {
				compatible = "marvell,armada-8k-rng\0inside-secure,safexcel-eip76";
				reg = <0x760000 0x7d>;
				interrupts = <0x00 0x5f 0x04>;
				clock-names = "core\0reg";
				clocks = <0x10 0x01 0x19 0x10 0x01 0x11>;
				status = "okay";
			};

			sdhci@780000 {
				compatible = "marvell,armada-cp110-sdhci";
				reg = <0x780000 0x300>;
				interrupts = <0x00 0x1b 0x04>;
				clock-names = "core\0axi";
				clocks = <0x10 0x01 0x04 0x10 0x01 0x12>;
				dma-coherent;
				status = "disabled";
			};

			crypto@800000 {
				compatible = "inside-secure,safexcel-eip197b";
				reg = <0x800000 0x200000>;
				interrupts = <0x00 0x57 0x04 0x00 0x58 0x04 0x00 0x59 0x04 0x00 0x5a 0x04 0x00 0x5b 0x04 0x00 0x5c 0x04>;
				interrupt-names = "mem\0ring0\0ring1\0ring2\0ring3\0eip";
				clock-names = "core\0reg";
				clocks = <0x10 0x01 0x1a 0x10 0x01 0x11>;
				cell-index = <0x00>;
				dma-coherent;
				status = "okay";
				phandle = <0x1f>;
			};

			uio_sam@800000 {
				compatible = "marvell,uio-sam";
				eip_access = <0x1f>;
			};

			leds {
				status = "okay";
				compatible = "leds-rb";
				pinctrl-0 = <0x20>;
				pinctrl-names = "default";

				button {
					gpios = <0x21 0x1c 0x01>;
					default-state = "input";
				};

				all-leds {
					gpios = <0x22 0x1b 0x00>;
					default-state = "keep";
				};

				user-led {
					gpios = <0x22 0x1a 0x01>;
					default-state = "keep";
				};

				sfp-led {
					gpios = <0x22 0x19 0x01>;
					default-state = "keep";
				};

				usb-power-off {
					gpios = <0x22 0x17 0x01>;
				};
			};
		};

		pcie@600000 {
			compatible = "marvell,armada8k-pcie\0snps,dw-pcie";
			reg = <0x00 0xf2600000 0x00 0x10000 0x00 0xf6f00000 0x00 0x80000>;
			reg-names = "ctrl\0config";
			#address-cells = <0x03>;
			#size-cells = <0x02>;
			#interrupt-cells = <0x01>;
			device_type = "pci";
			dma-coherent;
			msi-parent = <0x08>;
			bus-range = <0x00 0xff>;
			ranges = <0x81000000 0x00 0xf9000000 0x00 0xf9000000 0x00 0x10000 0x82000000 0x00 0xf6000000 0x00 0xf6000000 0x00 0xf00000>;
			interrupt-map-mask = <0x00 0x00 0x00 0x00>;
			interrupt-map = <0x00 0x00 0x00 0x00 0x0f 0x00 0x16 0x04>;
			interrupts = <0x00 0x16 0x04>;
			num-lanes = <0x02>;
			clock-names = "core\0reg";
			clocks = <0x10 0x01 0x0d 0x10 0x01 0x0e>;
			status = "okay";
		};

		pcie@620000 {
			compatible = "marvell,armada8k-pcie\0snps,dw-pcie";
			reg = <0x00 0xf2620000 0x00 0x10000 0x00 0xf7f00000 0x00 0x80000>;
			reg-names = "ctrl\0config";
			#address-cells = <0x03>;
			#size-cells = <0x02>;
			#interrupt-cells = <0x01>;
			device_type = "pci";
			dma-coherent;
			msi-parent = <0x08>;
			bus-range = <0x00 0xff>;
			ranges = <0x81000000 0x00 0xf9010000 0x00 0xf9010000 0x00 0x10000 0x82000000 0x00 0xf7000000 0x00 0xf7000000 0x00 0xf00000>;
			interrupt-map-mask = <0x00 0x00 0x00 0x00>;
			interrupt-map = <0x00 0x00 0x00 0x00 0x0f 0x00 0x18 0x04>;
			interrupts = <0x00 0x18 0x04>;
			num-lanes = <0x01>;
			clock-names = "core\0reg";
			clocks = <0x10 0x01 0x0b 0x10 0x01 0x0e>;
			status = "okay";
		};

		pcie@640000 {
			compatible = "marvell,armada8k-pcie\0snps,dw-pcie";
			reg = <0x00 0xf2640000 0x00 0x10000 0x00 0xf8f00000 0x00 0x80000>;
			reg-names = "ctrl\0config";
			#address-cells = <0x03>;
			#size-cells = <0x02>;
			#interrupt-cells = <0x01>;
			device_type = "pci";
			dma-coherent;
			msi-parent = <0x08>;
			bus-range = <0x00 0xff>;
			ranges = <0x81000000 0x00 0xf9020000 0x00 0xf9020000 0x00 0x10000 0x82000000 0x00 0xf8000000 0x00 0xf8000000 0x00 0xf00000>;
			interrupt-map-mask = <0x00 0x00 0x00 0x00>;
			interrupt-map = <0x00 0x00 0x00 0x00 0x0f 0x00 0x17 0x04>;
			interrupts = <0x00 0x17 0x04>;
			num-lanes = <0x01>;
			clock-names = "core\0reg";
			clocks = <0x10 0x01 0x0c 0x10 0x01 0x0e>;
			status = "okay";
		};
	};

	memory@0 {
		device_type = "memory";
		reg = <0x00 0x00 0x00 0x80000000>;
	};

	chosen {
		stdout-path = "serial0:115200n8";
		linux,initrd-start = <0x00>;
		linux,initrd-end = <0x00>;
		bootargs = [00];
	};

	thermal-zones {

		cpu-thermal {
			polling-delay-passive = <0xfa>;
			polling-delay = <0x3e8>;
			thermal-sensors = <0x23 0x00>;

			trips {

				ap-cpu-crit {
					temperature = <0x19a28>;
					hysteresis = <0x7d0>;
					type = "critical";
				};
			};
		};

		soc-thermal {
			polling-delay-passive = <0xfa>;
			polling-delay = <0x3e8>;
			thermal-sensors = <0x24 0x00>;

			trips {

				cpu-crit {
					temperature = <0x19a28>;
					hysteresis = <0x7d0>;
					type = "critical";
				};
			};
		};
	};
};


File: /Makefile
CC = gcc
CFLAGS = -Wall
OBJS = x_conf_reader.c

all: x_conf_reader

%.o: %.c
	$(CC) $(CFLAGS) -c -o $@ $<

rbcfg: $(OBJS)
	$(CC) -o $@ $(OBJS)

clean:
	rm -f x_conf_reader *.o


File: /mibibs\rb3011.mibib
  Parts list in DTS format:
	SBL1@0 {
		label = "SBL1";
		reg = <0x00000000 0x20000>;
		read-only;
	};
	MIBIB@20000 {
		label = "MIBIB";
		reg = <0x00020000 0x20000>;
		read-only;
	};
	SBL2@40000 {
		label = "SBL2";
		reg = <0x00040000 0x40000>;
		read-only;
	};
	SBL3@80000 {
		label = "SBL3";
		reg = <0x00080000 0x80000>;
		read-only;
	};
	DDRCONFIG@100000 {
		label = "DDRCONFIG";
		reg = <0x00100000 0x10000>;
		read-only;
	};
	SSD@110000 {
		label = "SSD";
		reg = <0x00110000 0x10000>;
		read-only;
	};
	TZ@120000 {
		label = "TZ";
		reg = <0x00120000 0x80000>;
		read-only;
	};
	RPM@1a0000 {
		label = "RPM";
		reg = <0x001a0000 0x20000>;
		read-only;
	};
	APPSBL@1c0000 {
		label = "APPSBL";
		reg = <0x001c0000 0x40000>;
		read-only;
	};
	APPSBLENV@200000 {
		label = "APPSBLENV";
		reg = <0x00200000 0x40000>;
		read-only;
	};
	ART@240000 {
		label = "ART";
		reg = <0x00240000 0x40000>;
		read-only;
	};
	NSS0@280000 {
		label = "NSS0";
		reg = <0x00280000 0x100000>;
		read-only;
	};
	NSS1@380000 {
		label = "NSS1";
		reg = <0x00380000 0x100000>;
		read-only;
	};
	HLOS@480000 {
		label = "HLOS";
		reg = <0x00480000 0x200000>;
		read-only;
	};
	rootfs@680000 {
		label = "rootfs";
		reg = <0x00680000 0xffff0000>;
		read-only;
	};


File: /ptable.h
#ifndef __PTABLE_H__
#define __PTABLE_H__

//####################################################################### 
//#         Описание структуры таблицы разделов
//#######################################################################


// Длина имени раздела. Она фиксирована, и имя не обязательно заканчивается на 0
//
#define FLASH_PART_NAME_LENGTH 16

// Сигнатура системной таблицы разделов (таблицы чтения)
#define FLASH_PART_MAGIC1     0x55EE73AA
#define FLASH_PART_MAGIC2     0xE35EBDDB

// Сигнатура пользовательской таблицы разделов (таблицы записи)
#define FLASH_USR_PART_MAGIC1     0xAA7D1B9A
#define FLASH_USR_PART_MAGIC2     0x1F7D48BC

// Идентификатор размера раздела, расширяющегося в сторону конца флешки
#define FLASH_PARTITION_GROW  0xFFFFFFFF

// Значения по умолчанию для атрибутов
#define FLASH_PART_FLAG_BASE  0xFF
#define FLASH_PART_ATTR_BASE  0xFF

/* Attributes for NAND paritions */
#define FLASH_PART_HEX_SIZE   0xFE

/* Attribute Masks */
#define FLASH_PART_ATTRIBUTE1_BMSK 0x000000FF
#define FLASH_PART_ATTRIBUTE2_BMSK 0x0000FF00
#define FLASH_PART_ATTRIBUTE3_BMSK 0x00FF0000

/* Attribute Shift Offsets */
#define FLASH_PART_ATTRIBUTE1_SHFT 0
#define FLASH_PART_ATTRIBUTE2_SHFT 8
#define FLASH_PART_ATTRIBUTE3_SHFT 16


#define FLASH_MI_BOOT_SEC_MODE_NON_TRUSTED 0x00
#define FLASH_MI_BOOT_SEC_MODE_TRUSTED     0x01

#define FLASH_PART_ATTRIB( val, attr ) (((val) & (attr##_BMSK)) >> attr##_SHFT)


// Описание атрибута 1
typedef enum {
  FLASH_PARTITION_DEFAULT_ATTRB = 0xFF,  // по умолчанию
  FLASH_PARTITION_READ_ONLY = 0,         // только чтение
} flash_partition_attrb_t;


// Описание атрибута 2
typedef enum {
  // По умолчанию - обычный раздел (512-байтовые секторы)
  FLASH_PARTITION_DEFAULT_ATTRB2 = 0xFF,

  // То же самое - 512-байтовые секторы
  FLASH_PARTITION_MAIN_AREA_ONLY = 0,

  // Линуксовый формат - 516-байтовые секторы, часть spare с тегом защищена ЕСС
  FLASH_PARTITION_MAIN_AND_SPARE_ECC,

  
} flash_partition_attrb2_t;


// Описание атрибута 3
typedef enum {
  
  // по умолчанию
  FLASH_PART_DEF_ATTRB3 = 0xFF,

  // разрешено обновление по имени раздела
  FLASH_PART_ALLOW_NAMED_UPGRD = 0,

} flash_partition_attrb3_t;


//*******************************************************************
//* Описание раздела в системной таблица разделов (таблица чтения)
//*******************************************************************
struct flash_partition_entry;
typedef struct flash_partition_entry *flash_partentry_t;
typedef struct flash_partition_entry *flash_partentry_ptr_type;

struct flash_partition_entry {

  // имя раздела
  char name[FLASH_PART_NAME_LENGTH];

  // смещение в блоках до начала раздела
  uint32 offset;

  // размер раздела в блоках
  uint32 len;

  // атрибуты раздела
  uint8 attr1;
  uint8 attr2;
  uint8 attr3;

  // Флешка, на которой находится раздел (0 - первичная, 1 - вторичная)
  uint8 which_flash;
};

//*************************************************************************
//* Описание раздела в пользовательской таблице разделов (таблица записи)
//*************************************************************************
struct flash_usr_partition_entry;
typedef struct flash_usr_partition_entry *flash_usr_partentry_t;
typedef struct flash_usr_partition_entry *flash_usr_partentry_ptr_type;

struct flash_usr_partition_entry {

  // имя раздела
  char name[FLASH_PART_NAME_LENGTH];

  // Размер раздела в KB 
  uint32 img_size;

  // Размер резервируемой (на бедблоки) области раздела в КВ
  uint16 padding;

  // Флешка, на которой находится раздел (0 - первичная, 1 - вторичная)
  uint16 which_flash;

  // Атрибуты раздела (те же что и в таблице чтения)
  uint8 reserved_flag1;
  uint8 reserved_flag2;
  uint8 reserved_flag3;

  uint8 reserved_flag4; 

};

/*  Number of partition tables which will fit in 512 byte page, calculated
 *  by subtracting the partition table header size from 512 and dividing
 *  the result by the size of each entry.  There is no easy way to do this
 *  with calculations made by the compiler.
 *
 *     16 bytes for header
 *     28 bytes for each entry
 *     512 - 16 = 496
 *     496/28 = 17.71 = round down to 16 entries
 */

// Максимальное число разделов в таблице		
#define FLASH_NUM_PART_ENTRIES  32

//*************************************************************************
//* Структура системной таблицы разделов (таблицы чтения)
//*************************************************************************
struct flash_partition_table {

  // Сигнатуры таблицы
  uint32 magic1;
  uint32 magic2;
  // Версия таблицы
  uint32 version;

  // Число определенных разделов
  uint32 numparts;   
  // Список разделов
  struct flash_partition_entry part[FLASH_NUM_PART_ENTRIES];
//  int8 trash[112]; 
};


//*************************************************************************
//* Структура пользовательской таблицы разделов (таблицы записи)
//*************************************************************************
struct flash_usr_partition_table {

  // Сигнатуры таблицы
  uint32 magic1;
  uint32 magic2;
  // Версия таблицы
  uint32 version;
  // Число определенных разделов
  uint32 numparts;   /* number of partition entries */
  // Список разделов
  struct flash_usr_partition_entry part[FLASH_NUM_PART_ENTRIES];
};

#endif // __PTABLE_H__



File: /README.md
# Mikrotik soft/hard config reader

A simple program that reads soft/hard config section of Mikrotik's RouterOS.


File: /x_conf_reader.c
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <arpa/inet.h>
#include <string.h>
#include <stdint.h>
#include <arpa/inet.h>

#define u8 uint8_t
#define u16 uint16_t
#define u32 uint32_t

#define uint8 uint8_t
#define uint16 uint16_t
#define uint32 uint32_t
#include "ptable.h"

#define DO_ENDIANS_CONV 0

static u32 get_u32(void *buf)
{
#if DO_ENDIANS_CONV == 1
	const uint8_t *p = buf;
	return ((uint32_t) p[3] + ((uint32_t) p[2] << 8) +
	       ((uint32_t) p[1] << 16) + ((uint32_t) p[0] << 24));
#else
	return *(u32 *)buf;
#endif
}

//#define RB_BLOCK_SIZE		0x100
#define RB_BLOCK_SIZE		0x1000
#define RB_MAGIC_HARD	0x64726148 /* "Hard" */
#define RB_MAGIC_SOFT	0x74666F53 /* "Soft" */
#define RB_MAGIC_DAWN	0x6E776144 /* "Dawn" */
#define RB_MAGIC_DTS	0xEDFE0DD0 /* "DTS" */
#define ELF_MAGIC			0x464C457F /* "ELF" */
#define MIBIB_MAGIC		0xFE569FAC /* MIBIB */

static u32 hard_cfg_offset = 0;
static u32 soft_cfg_offset = 0;
static u32 mibib_block_offset = 0;

static int dump_num = 0;
void dump_config(char *data, unsigned int size){
	int fd;
	char fname[32];
	ssize_t wr_len;
	sprintf(fname, "./dumps/%d.bin", dump_num++);
	fd = open(fname, O_WRONLY | O_CREAT);
	if(fd < 0){
		perror("Can't dump!");
		return;
	}
	wr_len = write(fd, data, size);
	printf("   dumped %zd bytes to %s\n", wr_len, fname);
}

void find_configs(void *data, unsigned int size){
	unsigned int offset;

	for (offset = 0; offset < size; offset += 1) {
		u32 magic;

		magic = get_u32(data + offset);
		switch (magic) {
		case RB_MAGIC_HARD:
			printf("Hard config detected at 0x%x\n", offset);
			hard_cfg_offset = offset;
			dump_config(data + offset, 0x1000);
			break;

		case RB_MAGIC_SOFT:
			soft_cfg_offset = offset;
			printf("Soft config detected at 0x%x\n", offset);
			dump_config(data + offset, 0x1000);
			break;
		case RB_MAGIC_DTS:
			printf("DTS config detected at 0x%x\n", offset);
			dump_config(data + offset, 0x5a90);
			break;
		case ELF_MAGIC:
			printf("ELF header detected at 0x%x\n", offset);
			break;
		case MIBIB_MAGIC:
			if(get_u32(data + offset + 0x100) != FLASH_PART_MAGIC1)
				break;
			printf("MIBIB block detected at 0x%x\n", offset);
			if(mibib_block_offset == 0) //comment it for second block
				mibib_block_offset = offset;
			break;
		}
	}
}

/*
 * ID values for Software settings
 */
#define RB_ID_TERMINATOR	0
#define RB_ID_UART_SPEED	1
#define RB_ID_BOOT_DELAY	2
#define RB_ID_BOOT_DEVICE	3
#define RB_ID_BOOT_KEY		4
#define RB_ID_CPU_MODE		5
#define RB_ID_FW_VERSION	6
#define RB_ID_SOFT_07		7
#define RB_ID_SOFT_08		8
#define RB_ID_BOOT_PROTOCOL	9
#define RB_ID_SOFT_10		10
#define RB_ID_SOFT_11		11
#define RB_ID_CPU_FREQ		12
#define RB_ID_BOOTER		13
void read_config(void *data, size_t cfg_offset, size_t buflen){
	int id;
	int len;
	unsigned char *buf = data + cfg_offset;
	/* skip magic and CRC value */
	buf += 8;
	buflen -= 8;

	while (buflen > 4){
		u32 id_and_len = get_u32(buf);
		buf += 4;
		buflen -= 4;
		id = id_and_len & 0xFFFF;
		len = id_and_len >> 16;
		printf("id = 0x%x, len = 0x%x, val = 0x%x\n", id, len, *(u32 *)buf);
		if (id == RB_ID_TERMINATOR){
			break;
		}
		if (buflen < len)
			break;
		buf += len;
		buflen -= len;
	}
}
void read_soft_config(void *data, size_t buflen){
	printf("Soft config tags:\n");
	read_config(data, soft_cfg_offset, buflen);
}

//https://github.com/forth32/qtools/blob/master/ptable.h
void read_mibib_block(void *data, size_t buflen, int in_dts){
	unsigned char *buf = data + mibib_block_offset;
	u32 *p = (void*)buf + 0x100;
	struct flash_partition_entry *part = NULL;
	int a;
	int numparts = 0;
	printf("MIBIB(0x%08x):\n", mibib_block_offset);
	if(*(p++) != FLASH_PART_MAGIC1){
		printf("  FLASH_PART_MAGIC1 - MISMATCH: 0x%x vs 0x%x\n", *(p++), FLASH_PART_MAGIC1);
		return;
	}
	printf("  FLASH_PART_MAGIC1 - OK\n");
	if(*(p++) != FLASH_PART_MAGIC2){
		printf("  FLASH_PART_MAGIC2 - MISMATCH\n");
		return;
	}
	printf("  FLASH_PART_MAGIC2 - OK\n");
	printf("  Version - %d\n", *(p++));
	numparts = *(p++);
	if(numparts > FLASH_NUM_PART_ENTRIES){
		printf("  Numparts - OWERFLOW! (%d > %d)\n", numparts, FLASH_NUM_PART_ENTRIES);
		return;
	}
	printf("  Numparts - %d\n", numparts);
	if(!in_dts){
		printf("  Parts list:\n");
		//список разделов
		part = (void*)p;
		for(a = 0; a < numparts; a++, part++){
			printf("    part %02d: %-15s offset = 0x%08x, len = 0x%x\n", a, part->name,
				part->offset * 0x10000,
				part->len * 0x10000);
		}
	}
	if(in_dts){
		char spaces[20];
		printf("\n");
		printf("  Parts list in DTS format:\n");
		part = (void*)p;
		for(a = 0; a < in_dts && a < sizeof(spaces); a++)
			spaces[a] = '\t';
		spaces[a] = '\0';
		for(a = 0; a < numparts; a++, part++){
			u32 offset = part->offset * 0x10000;
			u32 len = part->len * 0x10000;
			char *name = part->name;
			if(*name == '0' && *(name + 1) == ':')
				name += 2;
			printf("%s%s@%x {\n", spaces, name, offset);
			printf("%s\tlabel = \"%s\";\n", spaces, name);
			printf("%s\treg = <0x%08x 0x%x>;\n", spaces, offset, len);
			printf("%s\tread-only;\n", spaces);
			printf("%s};\n", spaces);
		}
	}
}

unsigned char data[17*1024*1024];
int main(void){
	int fd;
	size_t len;
	unsigned char *p = data;
	ssize_t rest = sizeof(data);
	//fd = open("./bins/rb450gx4.bin", O_RDONLY);
	//fd = open("/home/prog/openwrt/work/rb962-us/mtd/mtdX1.EU", O_RDONLY);
	fd = open("/home/prog/openwrt/work/RB5009/dumps/mtdblock2.bin", O_RDONLY);
	//fd = open("./bins/old/rb3011.bin", O_RDONLY);
	if(fd < 0){
		perror("Can't open file");
		return -1;
	}

	memset(data, 0x0, sizeof(data));
	while(rest > 0){
		len = read(fd, p, rest);
		if(len <= 0)
			break;
		rest -= len;
		p += len;
	}
	close(fd);

	/* if(rest > 0){
		fprintf(stderr, "Error reading data from file. rest = %zd\n", rest);
		return -2;
	} */
	find_configs(data, sizeof(data));
	//printf("\n");
	read_soft_config(data, 0x1000);

	printf("\n");
	//mibib_block_offset = 0x20000;
	//mibib_block_offset = 0x30000;
	if(mibib_block_offset > 0)
		read_mibib_block(data, 0x20000, 1);

	return 0;
}


