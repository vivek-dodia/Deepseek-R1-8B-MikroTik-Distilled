# Repository Information
Name: EC-MikroTik-Materials

# Directory Structure
Directory structure:
└── github_repos/EC-MikroTik-Materials/
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
    │   │       ├── pack-dab0df67a0c4e554544d320f71875442cd8922d0.idx
    │   │       └── pack-dab0df67a0c4e554544d320f71875442cd8922d0.pack
    │   ├── packed-refs
    │   └── refs/
    │       ├── heads/
    │       │   └── master
    │       ├── remotes/
    │       │   └── origin/
    │       │       └── HEAD
    │       └── tags/
    ├── 30-ecbformatting.conf
    ├── address_list_IP_emailer
    ├── address_list_IP_exporter
    ├── dude_custom_files/
    │   ├── CAMBIUM-cnPilot-R-4.2-R3-MIB.txt
    │   ├── CAMBIUM-ePMP-3.5.1-MIB.txt
    │   ├── IEEE802dot11-MIB.txt
    │   ├── MIMOSA-MIB-B5.txt
    │   ├── MIMOSA-MIB-COMMON.txt
    │   ├── MIMOSA-MIB-PTMP.txt
    │   ├── MIMOSA-MIB-TC.txt
    │   ├── MIMOSA-MIB.txt
    │   ├── Thumbs.db
    │   ├── UBNT-AirFIBER-MIB.txt
    │   ├── UBNT-AirMAX-MIB.txt
    │   └── UBNT-MIB.txt
    ├── fur_elise_unfinished
    ├── mikrotik_backup_script
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
	url = https://github.com/doctorcompton/EC-MikroTik-Materials.git
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
0000000000000000000000000000000000000000 ac175212efcb223b517485153b4eb5d564896874 vivek-dodia <vivek.dodia@icloud.com> 1738606456 -0500	clone: from https://github.com/doctorcompton/EC-MikroTik-Materials.git


File: /.git\logs\refs\heads\master
0000000000000000000000000000000000000000 ac175212efcb223b517485153b4eb5d564896874 vivek-dodia <vivek.dodia@icloud.com> 1738606456 -0500	clone: from https://github.com/doctorcompton/EC-MikroTik-Materials.git


File: /.git\logs\refs\remotes\origin\HEAD
0000000000000000000000000000000000000000 ac175212efcb223b517485153b4eb5d564896874 vivek-dodia <vivek.dodia@icloud.com> 1738606456 -0500	clone: from https://github.com/doctorcompton/EC-MikroTik-Materials.git


File: /.git\packed-refs
# pack-refs with: peeled fully-peeled sorted 
ac175212efcb223b517485153b4eb5d564896874 refs/remotes/origin/master


File: /.git\refs\heads\master
ac175212efcb223b517485153b4eb5d564896874


File: /.git\refs\remotes\origin\HEAD
ref: refs/remotes/origin/master


File: /30-ecbformatting.conf
template(name="json-template"
  type="list") {
    constant(value="{")
      constant(value="\"@timestamp\":\"")     property(name="timereported" dateFormat="rfc3339")
      constant(value="\",\"@version\":\"1")
      constant(value="\",\"message\":\"")     property(name="msg" format="json")
      constant(value="\",\"sysloghost\":\"")  property(name="hostname")
      constant(value="\",\"severity\":\"")    property(name="syslogseverity-text")
      constant(value="\",\"facility\":\"")    property(name="syslogfacility-text")
      constant(value="\",\"programname\":\"") property(name="programname")
      constant(value="\",\"procid\":\"")      property(name="procid")
    constant(value="\"}\n")
}

template(name="json-template-detailed"
  type="list") {
    constant(value="{")
      constant(value="\"@timestamp\":\"")     property(name="timereported" dateFormat="rfc3339")
      constant(value="\",\"inputiface\":\"")  property(name="msg" regex.type="ERE" regex.expression="in:(ether[[:digit:]]-?[[:alpha:]]*)" regex.submatch="1")
      constant(value="\",\"outputiface\":\"") property(name="msg" regex.type="ERE" regex.expression="out:(ether[[:digit:]]-?[[:alpha:]]*)" regex.submatch="1")
      constant(value="\",\"srcmac\":\"")      property(name="msg" regex.type="ERE" regex.expression="src-mac ([[:xdigit:]:]{17})" regex.submatch="1")
      constant(value="\",\"protocol\":\"")    property(name="msg" regex.type="ERE" regex.expression="proto ([A-Z]{3,4})" regex.submatch="1")
      constant(value="\",\"srcip\":\"")       property(name="msg" regex.type="ERE" regex.expression=", ([[:digit:].]+)" regex.submatch="1")
      constant(value="\",\"destip\":\"")      property(name="msg" regex.type="ERE" regex.expression=">([[:digit:].]+)" regex.submatch="1")
      constant(value="\",\"srcport\":\"")     property(name="msg" regex.type="ERE" regex.expression="[[:digit:]]{1,3}:([[:digit:]]+)->" regex.submatch="1")
      constant(value="\",\"destport\":\"")    property(name="msg" regex.type="ERE" regex.expression="->[[:digit:].]+:([[:digit:]]+)," regex.submatch="1")
      constant(value="\",\"sysloghost\":\"")  property(name="hostname")
      constant(value="\",\"programname\":\"") property(name="programname")
    constant(value="\"}\n")
}


File: /address_list_IP_emailer
{
	# ============================================
	# set some variables
	# filename: self explanatory
	# IPs: the total number of IPs in address list
	# sysname: current hostname of router
	# datetime: the current date and time...
	# ============================================
	
	:global filename "IPlist"
	:local numIPs [:len [/ip firewall address-list find]]
	:global sysname [/system identity get name]
	:global datetime "$[/system clock get date] $[/system clock get time]"
	
	# ==========================
	# make the file and clear it
	# ==========================
	
	/file print file=$filename
	:delay 1
	/file set $filename contents="7-Day Address List of Assholes\n==============================\n"
	
	# =======================================================================
	# iterate current total of IPs, print to console, and concatenate to file
	# =======================================================================
	
	:for k from=0 to={ ($numIPs - 1) } step=1 do={ \
		:put [/ip firewall address-list get number=$k value-name=address]; \
		/file set $filename contents=([/file get $filename contents] . \
		[/ip firewall address-list get number=$k value-name=address] . "\n"); }
		
	# ==========================================================
	# finally, send an email with the address list as attachment
	# ==========================================================
	:delay 3
	/tool e-mail send to="<REDACTED, YOUR EMAIL HERE>" subject="$[/system identity get name] asshole address list" file=($filename . ".txt") body="$sysname \n $datetime \n Currently banned IP addresses, maximum of 7 days. Contains scriptkiddies trying to bruteforce SSH and Telnet. \n This is the asshole list.";
}


File: /address_list_IP_exporter
{
	# ============================================
	# set two variables
	# filename: self explanatory
	# IPs: the total number of IPs in address list
	# ============================================
	
	:global filename "IPlist"
	:local numIPs [:len [/ip firewall address-list find]]
	
	# ==========================
	# make the file and clear it
	# ==========================
	
	/file print file=$filename
	:delay 1
	/file set $filename contents=""
	
	# =======================================================================
	# iterate current total of IPs, print to console, and concatenate to file
	# =======================================================================
	
	:for k from=0 to={ ($numIPs - 1) } step=1 do={ \
		:put [/ip firewall address-list get number=$k value-name=address]; \
		/file set $filename contents=([/file get $filename contents] . \
		[/ip firewall address-list get number=$k value-name=address] . "\n"); }
}


File: /dude_custom_files\CAMBIUM-cnPilot-R-4.2-R3-MIB.txt

	CAMBIUM-MIB DEFINITIONS ::= BEGIN
 
		IMPORTS
			enterprises, Integer32, Gauge32, Counter32, OBJECT-TYPE, IpAddress,
			MODULE-IDENTITY, NOTIFICATION-TYPE			
				FROM SNMPv2-SMI			
			TEXTUAL-CONVENTION			
				FROM SNMPv2-TC;
	
		-- 1.3.6.1.4.1.41010
		cambiumnetwork OBJECT IDENTIFIER ::= { enterprises 41010 }
		-- 1.3.6.1.4.1.41010.1
		ata MODULE-IDENTITY 
			LAST-UPDATED "201309161714Z"		-- September 16, 2013 at 17:14 GMT
			ORGANIZATION 
				"cambiumnetwork."
			CONTACT-INFO 
				"Contact info."
			DESCRIPTION 
				"cambiumnetwork Mib."

			::= { cambiumnetwork 1 }


		-- 1.3.6.1.4.1.41010.1.1
		status OBJECT IDENTIFIER ::= { ata 1 }

		-- 1.3.6.1.4.1.41010.1.1.1
		productName OBJECT-TYPE
			SYNTAX OCTET STRING
			MAX-ACCESS read-only
			STATUS current
			DESCRIPTION
				""
			::= { status 1 }

		-- 1.3.6.1.4.1.41010.1.1.2
		internetWanMacAddress OBJECT-TYPE
			SYNTAX OCTET STRING
			MAX-ACCESS read-only
			STATUS current
			DESCRIPTION
				""
			::= { status 2 }

		-- 1.3.6.1.4.1.41010.1.1.3
		pcLanMacAddress OBJECT-TYPE
			SYNTAX OCTET STRING
			MAX-ACCESS read-only
			STATUS current
			DESCRIPTION
				""
			::= { status 3 }	

		-- 1.3.6.1.4.1.41010.1.1.4
		 hardwareVersion OBJECT-TYPE
			SYNTAX OCTET STRING
			MAX-ACCESS read-only
			STATUS current
			DESCRIPTION
				""
			::= { status 4 }

		-- 1.3.6.1.4.1.41010.1.1.5
		firmwareVersion OBJECT-TYPE
			SYNTAX OCTET STRING
			MAX-ACCESS read-only
			STATUS current
			DESCRIPTION
				""
			::= { status 5 }   
			
		-- 1.3.6.1.4.1.41010.1.1.6
		serialNumber OBJECT-TYPE
			SYNTAX OCTET STRING
			MAX-ACCESS read-only
			STATUS current
			DESCRIPTION
				""
			::= { status 6 }  
		
		-- 1.3.6.1.4.1.41010.1.1.7	  
		connectionType OBJECT-TYPE
			SYNTAX INTEGER
				{
				dhcp(0),
				static(1),
				pppoe(2)
				}			
			MAX-ACCESS read-only
			STATUS current
			DESCRIPTION
				""
			::= { status 7 }
          
        -- 1.3.6.1.4.1.41010.1.1.8
        managementPortIpAddress OBJECT-TYPE
			SYNTAX IpAddress
			MAX-ACCESS read-only
			STATUS current
			DESCRIPTION
				""
			::= { status 8 } 
		
		-- 1.3.6.1.4.1.41010.1.1.9	
		managementPortSubnetMask OBJECT-TYPE
			SYNTAX IpAddress
			MAX-ACCESS read-only
			STATUS current
			DESCRIPTION
				""
			::= { status 9 }
	
		-- 1.3.6.1.4.1.41010.1.1.10		
		managementPortDefaultGateway OBJECT-TYPE
			SYNTAX IpAddress
			MAX-ACCESS read-only
			STATUS current
			DESCRIPTION
				""
			::= { status 10 } 
			
		-- 1.3.6.1.4.1.41010.1.1.11		
		managementPortPrimaryDns OBJECT-TYPE
			SYNTAX IpAddress
			MAX-ACCESS read-only
			STATUS current
			DESCRIPTION
				""
			::= { status 11 }
			
		-- 1.3.6.1.4.1.41010.1.1.12		
		managementPortSecondaryDns OBJECT-TYPE
			SYNTAX IpAddress
			MAX-ACCESS read-only
			STATUS current
			DESCRIPTION
				""
			::= { status 12 }
					
		-- 1.3.6.1.4.1.41010.1.1.13		
		lanPortIpAddress OBJECT-TYPE
			SYNTAX IpAddress
			MAX-ACCESS read-only
			STATUS current
			DESCRIPTION
				""
			::= { status 13 }
			
		-- 1.3.6.1.4.1.41010.1.1.14		
		lanPortSubnetMask OBJECT-TYPE
			SYNTAX IpAddress
			MAX-ACCESS read-only
			STATUS current
			DESCRIPTION
				""
			::= { status 14 }			

		-- 1.3.6.1.4.1.41010.1.1.15		
		systemCurrentTime OBJECT-TYPE
			SYNTAX OCTET STRING
			MAX-ACCESS read-only
			STATUS current
			DESCRIPTION
				""
			::= { status 15 }

			-- 1.3.6.1.4.1.41010.1.1.16		
		fxs1SipAccountStatus OBJECT-TYPE
			SYNTAX INTEGER
			{
				disable(0),
				registered(1), 
				registering(2),
				fail(3)
			}
			MAX-ACCESS read-only
			STATUS current
			DESCRIPTION
				""
			::= { status 16 }
		
     		-- 1.3.6.1.4.1.41010.1.1.17		
		fxs2SipAccountStatus OBJECT-TYPE
			SYNTAX INTEGER  
			{
				disable(0),
				registered(1),
				registering(2),
				fail(3)
			}
			MAX-ACCESS read-only
			STATUS current
			DESCRIPTION
				""
			::= { status 17 }
  
  			-- 1.3.6.1.4.1.41010.1.1.18		
		wanPortStatus OBJECT-TYPE
			SYNTAX OCTET STRING
			MAX-ACCESS read-only
			STATUS current
			DESCRIPTION
				"10MHalf,10MFull,100MHalf,100MFull,Disconnected"
			::= { status 18 }
		
     		-- 1.3.6.1.4.1.41010.1.1.19		
		lanPortStatus OBJECT-TYPE
			SYNTAX OCTET STRING  
			MAX-ACCESS read-only
			STATUS current
			DESCRIPTION
				"10MHalf,10MFull,100MHalf,100MFull,Disconnected"
			::= { status 19 }
               
         	-- 1.3.6.1.4.1.41010.1.1.20
		lineStatus OBJECT IDENTIFIER ::= { status 20 }		

		lineStatusTable OBJECT-TYPE
			SYNTAX SEQUENCE OF LineStatusEntry
			MAX-ACCESS not-accessible
			STATUS current
			DESCRIPTION
				""
			::= { lineStatus 1 }

		
		lineStatusEntry OBJECT-TYPE
			SYNTAX LineStatusEntry
			MAX-ACCESS not-accessible
			STATUS current
			DESCRIPTION
				""
			INDEX { lineIndex }
			::= { lineStatusTable 1 }

		
		LineStatusEntry ::=
			SEQUENCE { 
				lineIndex
					Integer32,
				sipLineStatus
					INTEGER,
			 }


		lineIndex OBJECT-TYPE
			SYNTAX Integer32 (1..2)
			MAX-ACCESS read-only
			STATUS current
			DESCRIPTION
				""
			::= { lineStatusEntry 1 }

		
		sipLineStatus OBJECT-TYPE
			SYNTAX INTEGER
			{
				disable(0),
				registered(1), 
				registering(2),
				fail(3)
			}
			MAX-ACCESS read-only
			STATUS current
			DESCRIPTION
				""
			::= { lineStatusEntry 2 }

			
		-- 1.3.6.1.4.1.41010.1.2
		wan OBJECT IDENTIFIER ::= { ata 2 }

 		wanTable OBJECT-TYPE
			SYNTAX SEQUENCE OF WanEntry
			MAX-ACCESS not-accessible
			STATUS current
			DESCRIPTION
				""
			::= { wan 1 }

		
		wanEntry OBJECT-TYPE
			SYNTAX WanEntry
			MAX-ACCESS not-accessible
			STATUS current
			DESCRIPTION
				""
			INDEX { wanIndex }
			::= { wanTable 1 }

		
		WanEntry ::=
			SEQUENCE { 
				wanIndex
					Integer32,
				vlanId
					Integer32,
				vlanPri
					Integer32,
				bridgeMode
					INTEGER,
				service
					INTEGER,
				vlanTag
					INTEGER, 
				internetMode
					INTEGER,
				dnsMode
					INTEGER,
				primaryDNS
					IpAddress,
				secondaryDNS
					IpAddress,
				portBind
					INTEGER,
				ipAddress
					IpAddress,
				subnetMask
					IpAddress,
				gateway
					IpAddress,
				bridgeType
					INTEGER
			 }


		wanIndex OBJECT-TYPE
			SYNTAX Integer32 (1..16)
			MAX-ACCESS read-only
			STATUS current
			DESCRIPTION
				"max vlan number is 16"
			::= { wanEntry 1 }

		vlanId OBJECT-TYPE
			SYNTAX Integer32 (1..4094)
			MAX-ACCESS read-write
			STATUS current
			DESCRIPTION
				""
			::= { wanEntry 2 }

		vlanPri OBJECT-TYPE
			SYNTAX Integer32 (0..7)
			MAX-ACCESS read-write
			STATUS current
			DESCRIPTION
				""
			::= { wanEntry 3 }
			
 		bridgeMode OBJECT-TYPE
			SYNTAX INTEGER
			{
				route(0),
				bridge(1)		
			}
			MAX-ACCESS read-write
			STATUS current
			DESCRIPTION
				""
			::= { wanEntry 4 }

 		service OBJECT-TYPE
			SYNTAX INTEGER
			{
				voice(0),
				tr069(1),
				internet(2),
				tr069-internet(3),
				tr069-voice(4),
				voice-internet(5),
				tr069-voice-internet(6)				
			}
			MAX-ACCESS read-write
			STATUS current
			DESCRIPTION
				""
			::= { wanEntry 5 }

 		vlanTag OBJECT-TYPE
			SYNTAX INTEGER
			{
				disable(0),
				enable(1)
				
			}
			MAX-ACCESS read-write
			STATUS current
			DESCRIPTION
				""
			::= { wanEntry 6 }

 		internetMode OBJECT-TYPE
			SYNTAX INTEGER
			{
				static(0),
				dhcp(1),
				pppoe(2),
				noip(3)
				
			}
			MAX-ACCESS read-write
			STATUS current
			DESCRIPTION
				""
			::= { wanEntry 7 }
 
  		dnsMode OBJECT-TYPE
			SYNTAX INTEGER
			{
				auto(0),
				manual(1)
			}
			MAX-ACCESS read-write
			STATUS current
			DESCRIPTION
				""
			::= { wanEntry 8 }   

  		primaryDNS OBJECT-TYPE
			SYNTAX IpAddress
			MAX-ACCESS read-write
			STATUS current
			DESCRIPTION
				""
			::= { wanEntry 9 }  
			 			
   		secondaryDNS OBJECT-TYPE
			SYNTAX IpAddress
			MAX-ACCESS read-write
			STATUS current
			DESCRIPTION
				""
			::= { wanEntry 10 }  

   		portBind OBJECT-TYPE
			SYNTAX INTEGER
				{
				disable(0),
				enable(1)
				}			
			MAX-ACCESS read-write
			STATUS current
			DESCRIPTION
				"bind lan port to wan"
			::= { wanEntry 11 } 	

   		ipAddress OBJECT-TYPE
			SYNTAX IpAddress
			MAX-ACCESS read-write
			STATUS current
			DESCRIPTION
				"bind lan port to wan"
			::= { wanEntry 12 } 	

   		subnetMask OBJECT-TYPE
			SYNTAX IpAddress
			MAX-ACCESS read-write
			STATUS current
			DESCRIPTION
				"static ip mask"
			::= { wanEntry 13 } 				

   		gateway OBJECT-TYPE
			SYNTAX IpAddress
			MAX-ACCESS read-write
			STATUS current
			DESCRIPTION
				"static gateway"
			::= { wanEntry 14 } 
			
 		bridgeType OBJECT-TYPE
			SYNTAX INTEGER
			{
				ip(0),
				pppoe(1),
				hardware-ip(2)
			}
			MAX-ACCESS read-write
			STATUS current
			DESCRIPTION
				""
			::= { wanEntry 15 }

		-- 1.3.6.1.4.1.41010.1.3
		lan OBJECT IDENTIFIER ::= { ata 3 }    
		
			-- 1.3.6.1.4.1.41010.1.3.1
		localIpAddress OBJECT-TYPE
			SYNTAX IpAddress			
			MAX-ACCESS read-write
			STATUS current
			DESCRIPTION
				""
			::= { lan 1 }

 		-- 1.3.6.1.4.1.41010.1.3.2
		localSubnetMask OBJECT-TYPE
			SYNTAX IpAddress			
			MAX-ACCESS read-write
			STATUS current
			DESCRIPTION
				""
			::= { lan 2 }   

		-- 1.3.6.1.4.1.41010.1.4
		sip OBJECT IDENTIFIER ::= { ata 4 }
 
 
	        -- 1.3.6.1.4.1.41010.1.4.1
		natTraversal OBJECT-TYPE
			SYNTAX INTEGER
				{
				disable(0),
				enable(1)
				}			
			MAX-ACCESS read-write
			STATUS current
			DESCRIPTION
				""
			::= { sip 1 }

		-- 1.3.6.1.4.1.41010.1.4.2			
 		stunServerAddress OBJECT-TYPE
			SYNTAX OCTET STRING	(SIZE(0..63))		
			MAX-ACCESS read-write
			STATUS current
			DESCRIPTION
				""
			::= { sip 2 }
        
        -- 1.3.6.1.4.1.41010.1.4.3
 		stunServerPort OBJECT-TYPE
			SYNTAX Integer32 (0..65535)			
			MAX-ACCESS read-write
			STATUS current
			DESCRIPTION
				""
			::= { sip 3 }
        
        -- 1.3.6.1.4.1.41010.1.4.4
		sipQos OBJECT-TYPE
			SYNTAX Integer32 (0..63)
			MAX-ACCESS read-write
			STATUS current
			DESCRIPTION
				""
			::= { sip 4 }
        
        -- 1.3.6.1.4.1.41010.1.4.5
		rtpQos OBJECT-TYPE
			SYNTAX Integer32 (0..63)			
			MAX-ACCESS read-write
			STATUS current
			DESCRIPTION
				""
			::= { sip 5 }   

		-- 1.3.6.1.4.1.41010.1.4.6			
		dataQos OBJECT-TYPE
			SYNTAX Integer32 (0..63)		
			MAX-ACCESS read-write
			STATUS current
			DESCRIPTION
				""
			::= { sip 6 } 			


		-- 1.3.6.1.4.1.41010.1.5
		account OBJECT IDENTIFIER ::= { ata 5 }		
	
	
		
		sipUaTable OBJECT-TYPE
			SYNTAX SEQUENCE OF SipUaEntry
			MAX-ACCESS not-accessible
			STATUS current
			DESCRIPTION
				""
			::= { account 1 }

		
		sipUaEntry OBJECT-TYPE
			SYNTAX SipUaEntry
			MAX-ACCESS not-accessible
			STATUS current
			DESCRIPTION
				""
			INDEX { sipLineIndex }
			::= { sipUaTable 1 }

		
		SipUaEntry ::=
			SEQUENCE { 
				sipLineIndex
					Integer32,
				lineEnable
					INTEGER,
				proxyServer
					OCTET STRING,
				proxyPort
					Integer32,
				outboundServer
					OCTET STRING,
				outboundPort
					Integer32,
				backupOutboundServer
					OCTET STRING,
				backupOutboundPort
					Integer32,
				displayName
					OCTET STRING,
				phoneNumber
					OCTET STRING,
				sipAccount
					OCTET STRING,
				sipPassword
					OCTET STRING,
				codecType1
					INTEGER,
				codecType2
					INTEGER,
				codecType3
					INTEGER,
				codecType4
					INTEGER,
				codecType5
					INTEGER,
				g723Coding
					INTEGER,
				packetCycle
					INTEGER,
				silenceSupp
					INTEGER,
				echoCancel
					INTEGER,
				dtmfType
					INTEGER,
				registerRefreshInterval
					Integer32,															
			 }


		sipLineIndex OBJECT-TYPE
			SYNTAX Integer32 (1..2)
			MAX-ACCESS read-only
			STATUS current
			DESCRIPTION
				""
			::= { sipUaEntry 1 }

		
		lineEnable OBJECT-TYPE
			SYNTAX INTEGER
				{
				disable(0),
				enable(1)
				}
			MAX-ACCESS read-write
			STATUS current
			DESCRIPTION
				""
			::= { sipUaEntry 2 }


		proxyServer OBJECT-TYPE
			SYNTAX OCTET STRING (SIZE(0..63))
			MAX-ACCESS read-write
			STATUS current
			DESCRIPTION
				""
			::= { sipUaEntry 3 }

		
		proxyPort OBJECT-TYPE
			SYNTAX Integer32 (0..65535) 
			MAX-ACCESS read-write
			STATUS current
			DESCRIPTION
				""
			::= { sipUaEntry 4 }

		
		outboundServer OBJECT-TYPE
			SYNTAX OCTET STRING (SIZE(0..63))
			MAX-ACCESS read-write
			STATUS current
			DESCRIPTION
				""
			::= { sipUaEntry 5 }

		
		outboundPort OBJECT-TYPE
			SYNTAX Integer32 (0..65535)
			MAX-ACCESS read-write
			STATUS current
			DESCRIPTION
				""
			::= { sipUaEntry 6 }

		backupOutboundServer OBJECT-TYPE
			SYNTAX OCTET STRING (SIZE(0..63))
			MAX-ACCESS read-write
			STATUS current
			DESCRIPTION
				""
			::= { sipUaEntry 7 }

		
		backupOutboundPort OBJECT-TYPE
			SYNTAX Integer32 (0..65535)
			MAX-ACCESS read-write
			STATUS current
			DESCRIPTION
				""
			::= { sipUaEntry 8 }

		
		displayName OBJECT-TYPE
			SYNTAX OCTET STRING (SIZE(0..63))
			MAX-ACCESS read-write
			STATUS current
			DESCRIPTION
				""
			::= { sipUaEntry 9 }

		phoneNumber OBJECT-TYPE
			SYNTAX OCTET STRING (SIZE(0..63))
			MAX-ACCESS read-write
			STATUS current
			DESCRIPTION
				""
			::= { sipUaEntry 10 }

		sipAccount OBJECT-TYPE
			SYNTAX OCTET STRING (SIZE(0..63))
			MAX-ACCESS read-write
			STATUS current
			DESCRIPTION
				""
			::= { sipUaEntry 11 } 
			
		sipPassword OBJECT-TYPE
			SYNTAX OCTET STRING (SIZE(0..63))
			MAX-ACCESS read-write
			STATUS current
			DESCRIPTION
				""
			::= { sipUaEntry 12 } 
			
		codecType1 OBJECT-TYPE
			SYNTAX INTEGER
				{
				g711u(0),
				g711a(1),
				g722(2),
				g729(3),
				g723(4)
				}
			MAX-ACCESS read-write
			STATUS current
			DESCRIPTION
				""
			::= { sipUaEntry 13 } 
			
		codecType2 OBJECT-TYPE
			SYNTAX INTEGER
			{
				g711u(0),
				g711a(1),
				g722(2),
				g729(3),
				g723(4)
			}
			MAX-ACCESS read-write
			STATUS current
			DESCRIPTION
				""
			::= { sipUaEntry 14 }

		codecType3 OBJECT-TYPE
			SYNTAX INTEGER
			{
				g711u(0),
				g711a(1),
				g722(2),
				g729(3),
				g723(4)
			}
			MAX-ACCESS read-write
			STATUS current
			DESCRIPTION
				""
			::= { sipUaEntry 15 } 
			
		codecType4 OBJECT-TYPE
			SYNTAX INTEGER
			{
				g711u(0),
				g711a(1),
				g722(2),
				g729(3),
				g723(4)
			}
			MAX-ACCESS read-write
			STATUS current
			DESCRIPTION
				""
			::= { sipUaEntry 16 }

		codecType5 OBJECT-TYPE
			SYNTAX INTEGER
			{
				g711u(0),
				g711a(1),
				g722(2),
				g729(3),
				g723(4)
			}
			MAX-ACCESS read-write
			STATUS current
			DESCRIPTION
				""
			::= { sipUaEntry 17 }
 
 		g723Coding OBJECT-TYPE
			SYNTAX INTEGER
			{
				g723-53(0),
				g723-63(1)
			}
			MAX-ACCESS read-write
			STATUS current
			DESCRIPTION
				""
			::= { sipUaEntry 18 }

 		packetCycle OBJECT-TYPE
			SYNTAX INTEGER
			{
				ptime-10(0),
				ptime-20(1),
				ptime-30(2),
				ptime-40(3),
				ptime-50(4),
				ptime-60(5)				
			}
			MAX-ACCESS read-write
			STATUS current
			DESCRIPTION
				""
			::= { sipUaEntry 19 }

 		silenceSupp OBJECT-TYPE
			SYNTAX INTEGER
			{
				disable(0),
				enable(1)
			}
			MAX-ACCESS read-write
			STATUS current
			DESCRIPTION
				"VAD/CNG"
			::= { sipUaEntry 20 }

 		echoCancel OBJECT-TYPE
			SYNTAX INTEGER
				{
				disable(0),
				enable(1)
				}
			MAX-ACCESS read-write
			STATUS current
			DESCRIPTION
				""
			::= { sipUaEntry 21 } 
			
  		dtmfType OBJECT-TYPE
			SYNTAX INTEGER
				{
				inband(0),
				rfc2833(1),
				sipinfo(2)
				}
			MAX-ACCESS read-write
			STATUS current
			DESCRIPTION
				""
			::= { sipUaEntry 22 } 
			
 		registerRefreshInterval OBJECT-TYPE
			SYNTAX Integer32 (10..3600)
			MAX-ACCESS read-write
			STATUS current
			DESCRIPTION
				"unit is seconds."
			DEFVAL { 3600 }
			::= { sipUaEntry 23 }


 
		-- 1.3.6.1.4.1.41010.1.6
		preferences OBJECT IDENTIFIER ::= { ata 6 }	
  
  		preferencesTable OBJECT-TYPE
			SYNTAX SEQUENCE OF PreferencesEntry
			MAX-ACCESS not-accessible
			STATUS current
			DESCRIPTION
				""
			::= { preferences 1 }

		
		preferencesEntry OBJECT-TYPE
			SYNTAX PreferencesEntry
			MAX-ACCESS not-accessible
			STATUS current
			DESCRIPTION
				""
			INDEX { lineIndex }
			::= { preferencesTable 1 }

		
		PreferencesEntry ::=
			SEQUENCE { 
				lineIndex
					Integer32,
				inputGain
					Integer32,
				outputGain
					Integer32,	
				toneType
					INTEGER,
	            flashTimeMax
	                OCTET STRING,
	            flashTimeMin
	            	OCTET STRING,
	            loopCurrent
	                Integer32,
	            impedanceMaching
	                INTEGER				
			 }


		lineIndex OBJECT-TYPE
			SYNTAX Integer32 (1..2)
			MAX-ACCESS read-only
			STATUS current
			DESCRIPTION
				"line number."
			::= { preferencesEntry 1 }

		inputGain OBJECT-TYPE
			SYNTAX Integer32 (0..7)
			MAX-ACCESS read-write
			STATUS current
			DESCRIPTION
				"mic gain"
			::= { preferencesEntry 2 }

		outputGain OBJECT-TYPE
			SYNTAX Integer32  (0..7)
			MAX-ACCESS read-write
			STATUS current
			DESCRIPTION
				"speaker gain"
			::= { preferencesEntry 3 }
         
		toneType OBJECT-TYPE
			SYNTAX INTEGER
			{       
				  custom(0),
		          australia(1),
		          austria(2),
		          brazil(3),
		          belgium(4),
		          china(5),
		          czech(6),
		          denmark(7),
		          finland(8),
		          france(9),
		          germany(10),
		          great-britain(11),
		          greece(12),
		          hungary(13),
		          lithuania(14),
		          india(15),
		          italy(16),
		          japan(17),
		          korea(18),
		          mexico(19),
		          new-zealand(20),      
		          netherlands(21),
		          norway(22),
		          portugal(23),
		          spain(24),
		          switzerland(25),
		          sweden(26),
		          russia(27),
		          united-states(28)			
			}
			MAX-ACCESS read-write
			STATUS current
			DESCRIPTION
				""
			::= { preferencesEntry 4 }

        flashTimeMax  OBJECT-TYPE
			SYNTAX OCTET STRING (SIZE(0..63))
			MAX-ACCESS read-write
			STATUS current
			DESCRIPTION
				"unit is second"    
			DEFVAL { "0.9" }	
			::= { preferencesEntry 5 }

        flashTimeMin  OBJECT-TYPE
			SYNTAX OCTET STRING (SIZE(0..63))
			MAX-ACCESS read-write
			STATUS current
			DESCRIPTION
				"unit is second" 
			DEFVAL { "0.1" }
			::= { preferencesEntry 6 }

        loopCurrent  OBJECT-TYPE
			SYNTAX Integer32 (20..41)
			MAX-ACCESS read-write
			STATUS current
			DESCRIPTION
				""
			::= { preferencesEntry 7 }

        impedanceMaching OBJECT-TYPE
			SYNTAX INTEGER
			{
			   us-korean-taiwan(0),
			   standard(1),
			   japan(2),
			   bellcore(3),
			   ctr21(4),
			   china-co(5),
			   china-pbx(6),
			   japan-pbx(7),
			   india-newzealand(8),
			   germany-legacy(9),
			   uk-legacy(10),
			   australia(11),
			   variation(12)
			}
			MAX-ACCESS read-write
			STATUS current
			DESCRIPTION
				""
			::= { preferencesEntry 8 }


  
		-- 1.3.6.1.4.1.41010.1.7
		management OBJECT IDENTIFIER ::= { ata 7 }	

		-- 1.3.6.1.4.1.41010.1.7.1	
  		save OBJECT-TYPE
			SYNTAX Integer32 (0..1)
			MAX-ACCESS read-write
			STATUS current
			DESCRIPTION
				"1:save.
				Return 0 after saving."
			::= { management 1 }

		-- 1.3.6.1.4.1.41010.1.7.2	
   		reboot OBJECT-TYPE
			SYNTAX Integer32 (0..1)
			MAX-ACCESS read-write
			STATUS current
			DESCRIPTION
				"1:reboot.
				Return 0 after reboot."
			::= { management 2 } 
			                      
		-- 1.3.6.1.4.1.41010.1.7.3				                      
   		factoryDefault OBJECT-TYPE
			SYNTAX Integer32 (0..1)
			MAX-ACCESS read-write
			STATUS current
			DESCRIPTION
				"1:factory reset.
				Return 0 after factory reset finish."
			::= { management 3 }

		-- 1.3.6.1.4.1.41010.1.7.4	  
		ntpSetting OBJECT-TYPE
			SYNTAX INTEGER
				{
				west-11-MidwayIsland-Samoa(0),
				west-10-Hawaii(1),
				west-09-Alaska(2),
				west-08-PacificTime(3), 
				west-07-MountainTime(4),
				west-07-Arizona(5),
				west-06-CentralTime(6),
				west-06-MiddleAmerica(7),
				west-05-IndianaEast-Colombia(8),
				west-05-EasternTime(9),
				west-05-Altanticime-BrazilWest(10),
				west-04-Bolivia-Venezuela(11),
				west-03-Guyana(12),
				west-03-BrazilEast-Greenland(13),
				west-02-Mid-Atlantic(14), 
				west-01-AzoresIslands(15),
				east-00-Gambia-Liberia-Morocco(16),
				east-00-England(17),   
				east-01-CzechRepublic-N(18), 
				east-01-Germany(19), 
				east-01-Tunisia(20), 
				east-02-Greece-Ukraine-Turkey(21), 
				east-02-SouthAfrica(22), 
				east-03-Iraq-Jordan-Kuwait(23), 
				east-03-MoscowWinterTime(24),  
				east-04-Armenia(25),  
				east-05-Pakistan-Russia(26),  
				east-06-Bangladesh-Russia(27),  
				east-07-Thailand-Russia(28), 
				east-08-ChinaCoast-HongKong(29),
				east-08-Taipei(30),  
				east-08-Singapore(31),   
				east-08-AustraliaWA(32), 
				east-09-Japan-Korea(33), 
				east-09-Korean(34),      
				east-10-Guam-Russia(35), 
				east-10-Australia-QLD-TAS-NSW-ACT-VIC(36),
				east-11-SolomonIslands(37), 
				east-12-Fiji(38), 
				east-12-NewZealand(39)
				}			
			MAX-ACCESS read-write
			STATUS current
			DESCRIPTION
				"time zone"
			::= { management 4 }
			
		-- 1.3.6.1.4.1.41010.1.7.5
		primaryNtpServer OBJECT-TYPE
			SYNTAX OCTET STRING (SIZE(0..63))
			MAX-ACCESS read-write
			STATUS current
			DESCRIPTION
				""
			::= { management 5 } 

		-- 1.3.6.1.4.1.41010.1.7.6			
		secondaryNtpServer OBJECT-TYPE
			SYNTAX OCTET STRING (SIZE(0..63))
			MAX-ACCESS read-write
			STATUS current
			DESCRIPTION
				""
			::= { management 6 }

		-- 1.3.6.1.4.1.41010.1.7.7			
		daylightSavingTime OBJECT-TYPE
			SYNTAX INTEGER
			{
			disable(0),
			enable(1)
			}
			MAX-ACCESS read-write
			STATUS current
			DESCRIPTION
				"Summer time."
			::= { management 7 }
			
		-- 1.3.6.1.4.1.41010.1.7.8			
		offset OBJECT-TYPE
			SYNTAX Integer32 (0..23)
			MAX-ACCESS read-write
			STATUS current
			DESCRIPTION
				"The offset specifies the time value you must add to the local time to get a Coordinated Universal Time value.
				The hour must be between 0 and 23"
			::= { management 8 } 
			
		-- 1.3.6.1.4.1.41010.1.7.9			
		dstStartByWeek OBJECT-TYPE
			SYNTAX OCTET STRING (SIZE(0..63))
			MAX-ACCESS read-write
			STATUS current
			DESCRIPTION
				"Start time of summer time.
				Format: m.w.d.h
				This specifies day d of week w of month m. The day d must be between 0 (Sunday) and 6. 
				The week w must be between 1 and 5; week 1 is the first week in which day d occurs, 
				and week 5 specifies the last d day in the month. The month m should be between 1 and 12.
				Default setting is that summer time begins on the first Sunday in April at 2:00am."  
		    DEFVAL { "04.1.0.2" }
			::= { management 9 }
			
		-- 1.3.6.1.4.1.41010.1.7.10			
		dstEndByWeek OBJECT-TYPE 
		    SYNTAX OCTET STRING (SIZE(0..63))
			MAX-ACCESS read-write
			STATUS current
			DESCRIPTION
				"End time of summer time.
				Format: m.w.d.h
				This specifies day d of week w of month m. The day d must be between 0 (Sunday) and 6. 
				The week w must be between 1 and 5; week 1 is the first week in which day d occurs, 
				and week 5 specifies the last d day in the month. The month m should be between 1 and 12.
				Default setting is that summer time ends on the last Sunday in October at 2:00am."  
		    DEFVAL { "10.5.0.2" }
			::= { management 10 }
			
   
   		-- 1.3.6.1.4.1.41010.1.7.11			
		userType OBJECT-TYPE
			SYNTAX INTEGER
			{
				 admin(0),
				 basic(1),
				 normal(2)
			}
			MAX-ACCESS read-write
			STATUS current
			DESCRIPTION
				"admin: high level.
				basic: middle level.
				normal: low level."
			::= { management 11 }
			
   		-- 1.3.6.1.4.1.41010.1.7.12			
		userName OBJECT-TYPE
			SYNTAX OCTET STRING (SIZE(0..63))
			MAX-ACCESS read-write
			STATUS current
			DESCRIPTION
				""
			::= { management 12 }

   		-- 1.3.6.1.4.1.41010.1.7.13			
		password OBJECT-TYPE
			SYNTAX OCTET STRING (SIZE(0..63))
			MAX-ACCESS read-write
			STATUS current
			DESCRIPTION
				""
			::= { management 13 }
            
         -- 1.3.6.1.4.1.41010.1.7.14	 
         resyncProvision OBJECT-TYPE
			SYNTAX Integer32 (0..1)
			MAX-ACCESS read-write
			STATUS current
			DESCRIPTION
				"1:Synchronous provision.
				Return 0 after Synchronous provision finish."
			::= { management 14 }

        -- 1.3.6.1.4.1.41010.1.7.15	 
         operatingmode OBJECT-TYPE
			SYNTAX Integer32 (0..1)
			MAX-ACCESS read-write
			STATUS current
			DESCRIPTION
				"1:Basic Mode. 0: Advanced Mode.
				Return 0 after finish."
			::= { management 15 }
   
		-- 1.3.6.1.4.1.41010.1.8
		firmware OBJECT IDENTIFIER ::= { ata 8 }
			
		upgradeUrl OBJECT-TYPE
			SYNTAX OCTET STRING (SIZE(0..128))
			MAX-ACCESS read-write
			STATUS current
			DESCRIPTION
				"For example: http://url/firmware.bin.
				Ftp and Tftp are supported also."
			::= { firmware 1 } 

		upgradeSet OBJECT-TYPE
			SYNTAX INTEGER
				{
				normal(0),
				upgrade(1)
				}
			MAX-ACCESS read-write
			STATUS current
			DESCRIPTION
				"1: start upgrade.
				After upgrade, it will return 0."
			::= { firmware 2 }
			
  		upgradeStatus OBJECT-TYPE
			SYNTAX INTEGER
				{
				idle(10),
				updateProgress(20),
				updateFail(30),
				updateSuccess(40)
				}
			MAX-ACCESS read-only
			STATUS current
			DESCRIPTION
				""
			::= { firmware 3 }


 
		-- 1.3.6.1.4.1.41010.1.9
		snmp OBJECT IDENTIFIER ::= { ata 9 }	
		-- 1.3.6.1.4.1.41010.1.9.1			
		trapServerAddress OBJECT-TYPE
			SYNTAX OCTET STRING (SIZE(0..63))
			MAX-ACCESS read-write
			STATUS current
			DESCRIPTION
				"trap address"
			::= { snmp 1 }
			
		-- 1.3.6.1.4.1.41010.1.9.2			
		readCommunityName OBJECT-TYPE
			SYNTAX OCTET STRING (SIZE(0..63))
			MAX-ACCESS read-write
			STATUS current
			DESCRIPTION
				""
			::= { snmp 2 }
			
		-- 1.3.6.1.4.1.41010.1.9.3			
		writeCommunityName OBJECT-TYPE
			SYNTAX OCTET STRING (SIZE(0..63))
			MAX-ACCESS read-write
			STATUS current
			DESCRIPTION
				""
			::= { snmp 3 }
		
		-- 1.3.6.1.4.1.41010.1.9.4			
		trapCommunity OBJECT-TYPE
			SYNTAX OCTET STRING (SIZE(0..63))
			MAX-ACCESS read-write
			STATUS current
			DESCRIPTION
				""
			::= { snmp 4 }	

	     -- 1.3.6.1.4.1.41010.1.9.5			
		trapPeriodInterval OBJECT-TYPE
			SYNTAX Integer32 (0..3600)
			MAX-ACCESS read-write
			STATUS current
			DESCRIPTION
				"interval of keep alive trap"
			::= { snmp 5 }     
			
			
			
			
		-- 1.3.6.1.4.1.41010.1.10
		wlan OBJECT IDENTIFIER ::= { ata 10 }

		-- 1.3.6.1.4.1.41010.1.10.1
		bssid OBJECT-TYPE
			SYNTAX OCTET STRING (SIZE(0..63))
			MAX-ACCESS read-only
			STATUS current
			DESCRIPTION
				""
			::= { wlan 1 }	

		
		-- 1.3.6.1.4.1.41010.1.10.2
	
		ssid OBJECT IDENTIFIER ::= { wlan 2 }
		-- 1.3.6.1.4.1.41010.1.10.2.1
		ssid_2g OBJECT IDENTIFIER ::= { ssid 1 }
        -- 1.3.6.1.4.1.41010.1.10.2.1.1
 		ssid_2gTable OBJECT-TYPE
			SYNTAX SEQUENCE OF Ssid_2gEntry
			MAX-ACCESS not-accessible
			STATUS current
			DESCRIPTION
				""
			::= { ssid_2g 1 }

		-- 1.3.6.1.4.1.41010.1.10.2.1.1.1
		ssid_2gEntry OBJECT-TYPE
			SYNTAX Ssid_2gEntry
			MAX-ACCESS not-accessible
			STATUS current
			DESCRIPTION
				""
			INDEX { lineIndex }
			::= { ssid_2gTable 1 }

		Ssid_2gEntry ::=
			SEQUENCE { 
				lineIndex
					INTEGER,
				radioOnOff
					INTEGER,
				wlanMode
					OCTET STRING,
				channel
					INTEGER,
				autoChannel
					INTEGER,
				ssid_2gName
					OCTET STRING,
				authMode
					OCTET STRING,
				pskPasswd
					OCTET STRING,
				defaultKey
					INTEGER,
				wepkey1
					OCTET STRING,
				wepkey2
					OCTET STRING,
				wepkey3
					OCTET STRING,
				wepkey4
					OCTET STRING,
				bandwidth
					INTEGER,
			 }
		lineIndex OBJECT-TYPE
			SYNTAX INTEGER
			MAX-ACCESS read-only
			STATUS current
			DESCRIPTION
				"MIB index number."
			::= { ssid_2gEntry 1 }
		radioOnOff OBJECT-TYPE
			SYNTAX INTEGER
				{
				on(0),
				off(1)
				}
			MAX-ACCESS read-write
			STATUS	current
			DESCRIPTION
				"wlan_2g on\off"
			::= { ssid_2gEntry 2 }
		wlanMode OBJECT-TYPE
			SYNTAX OCTET STRING (SIZE(0..63))
			MAX-ACCESS read-only
			STATUS current
			DESCRIPTION
				""
			::= { ssid_2gEntry 3 }
			
		channel OBJECT-TYPE
			SYNTAX INTEGER (0..11)
			MAX-ACCESS read-write
			STATUS current
			DESCRIPTION
				"your choice of channel"
			::= { ssid_2gEntry 4 }	
		autoChannel OBJECT-TYPE
			SYNTAX INTEGER
			MAX-ACCESS read-write
			STATUS current
			DESCRIPTION
				"if your choice is 0,the system will choose 'autoChannel'."
			::= { ssid_2gEntry 5 }
		ssid_2gName OBJECT-TYPE
			SYNTAX OCTET STRING (SIZE(0..63))
			MAX-ACCESS read-write
			STATUS current
			DESCRIPTION
				"ssid_2gname."
			::= { ssid_2gEntry 6 }
		authMode OBJECT-TYPE
			SYNTAX OCTET STRING (SIZE(0..63))
			MAX-ACCESS read-write
			STATUS current
			DESCRIPTION
				"ssid_2g connect AuthMode."
			::= { ssid_2gEntry 7 }
			
		pskPasswd OBJECT-TYPE
			SYNTAX OCTET STRING (SIZE(0..63))
			MAX-ACCESS read-write
			STATUS current
			DESCRIPTION
				"pskPasswd."
			::= { ssid_2gEntry 8 }
		defaultKey OBJECT-TYPE
			SYNTAX INTEGER
				{
					null(0),
					key1(1),
					key2(2),
					key3(3),
					key4(4)
				}
			MAX-ACCESS read-write
			STATUS current
			DESCRIPTION
				"ssid_2g default wepkey."
			::= { ssid_2gEntry 9 }
		wepkey1 OBJECT-TYPE
			SYNTAX OCTET STRING (SIZE(0..26))
			MAX-ACCESS read-write
			STATUS current
			DESCRIPTION
				"ssid_2g wepKey1."
			::= { ssid_2gEntry 10 }
		wepkey2 OBJECT-TYPE
			SYNTAX OCTET STRING (SIZE(0..26))
			MAX-ACCESS read-write
			STATUS current
			DESCRIPTION
				"ssid_2g wepkey2."
			::= { ssid_2gEntry 11 }
		wepkey3 OBJECT-TYPE
			SYNTAX OCTET STRING (SIZE(0..26))
			MAX-ACCESS read-write
			STATUS current
			DESCRIPTION
				"ssid_2g wepkey3."
			::= { ssid_2gEntry 12 }
		wepkey4 OBJECT-TYPE
			SYNTAX OCTET STRING (SIZE(0..26))
			MAX-ACCESS read-write
			STATUS current
			DESCRIPTION
				"ssid_2g wepkey4."
			::= { ssid_2gEntry 13 }
			
		bandwidth OBJECT-TYPE
			SYNTAX INTEGER (0..1)
			MAX-ACCESS read-write
			STATUS current
			DESCRIPTION
				"Channel Bandwidth .0:20,1:20/40"
			::= { ssid_2gEntry 14 }
			
		-- 1.3.6.1.4.1.41010.1.10.2.2			
		ssid_5g OBJECT IDENTIFIER ::= { ssid 2 }
        
        -- 1.3.6.1.4.1.41010.1.10.2.2.1
 		ssid_5gTable OBJECT-TYPE
			SYNTAX SEQUENCE OF Ssid_5gEntry
			MAX-ACCESS not-accessible
			STATUS current
			DESCRIPTION
				""
			::= { ssid_5g 1 }

		-- 1.3.6.1.4.1.41010.1.10.2.2.1.1
		ssid_5gEntry OBJECT-TYPE
			SYNTAX Ssid_5gEntry
			MAX-ACCESS not-accessible
			STATUS current
			DESCRIPTION
				""
			INDEX { lineIndex }
			::= { ssid_5gTable 1 }

		Ssid_5gEntry ::=
			SEQUENCE { 
				lineIndex
					INTEGER,
				radioOnOff
					INTEGER,
				wlanMode
					OCTET STRING,
				channel
					INTEGER,
				autoChannel
					INTEGER,
				ssid_5gName
					OCTET STRING,
				authMode
					OCTET STRING,
				pskPasswd
					OCTET STRING,
				defaultKey
					INTEGER,
				wepkey1
					OCTET STRING,
				wepkey2
					OCTET STRING,
				wepkey3
					OCTET STRING,
				wepkey4
					OCTET STRING,
				bandwidth
					INTEGER,
				vhtbandwidth
					INTEGER,
			 }
		lineIndex OBJECT-TYPE
			SYNTAX INTEGER
			MAX-ACCESS read-only
			STATUS current
			DESCRIPTION
				"MIB index number."
			::= { ssid_5gEntry 1 }
		radioOnOff OBJECT-TYPE
			SYNTAX INTEGER
				{
				on(0),
				off(1)
				}
			MAX-ACCESS read-write
			STATUS	current
			DESCRIPTION
				"wlan_5g on\off"
			::= { ssid_5gEntry 2 }
		wlanMode OBJECT-TYPE
			SYNTAX OCTET STRING (SIZE(0..63))
			MAX-ACCESS read-only
			STATUS current
			DESCRIPTION
				""
			::= { ssid_5gEntry 3 }
			
		channel OBJECT-TYPE
			SYNTAX INTEGER (0..200)
			MAX-ACCESS read-write
			STATUS current
			DESCRIPTION
				""
			::= { ssid_5gEntry 4 }
		 autoChannel OBJECT-TYPE
			SYNTAX INTEGER
			MAX-ACCESS read-write
			STATUS current
			DESCRIPTION
				""
			::= { ssid_5gEntry 5 }
		ssid_5gName OBJECT-TYPE
			SYNTAX OCTET STRING (SIZE(0..63))
			MAX-ACCESS read-write
			STATUS current
			DESCRIPTION
				"ssid_5gname."
			::= { ssid_5gEntry 6 }
		authMode OBJECT-TYPE
			SYNTAX OCTET STRING (SIZE(0..63))
			MAX-ACCESS read-write
			STATUS current
			DESCRIPTION
				"ssid_5g connect AuthMode."
			::= { ssid_5gEntry 7 }
			
		pskPasswd OBJECT-TYPE
			SYNTAX OCTET STRING (SIZE(0..63))
			MAX-ACCESS read-write
			STATUS current
			DESCRIPTION
				"pskPasswd."
			::= { ssid_5gEntry 8 }
		defaultKey OBJECT-TYPE
			SYNTAX INTEGER
				{
					null(0),
					key1(1),
					key2(2),
					key3(3),
					key4(4)
				}
			MAX-ACCESS read-write
			STATUS current
			DESCRIPTION
				"ssid_5g default wepkey."
			::= { ssid_5gEntry 9 }
		wepkey1 OBJECT-TYPE
			SYNTAX OCTET STRING (SIZE(0..26))
			MAX-ACCESS read-write
			STATUS current
			DESCRIPTION
				"ssid_5g wepKey4."
			::= { ssid_5gEntry 10 }
		wepkey2 OBJECT-TYPE
			SYNTAX OCTET STRING (SIZE(0..26))
			MAX-ACCESS read-write
			STATUS current
			DESCRIPTION
				"ssid_5g wepkey4."
			::= { ssid_5gEntry 11 }
		wepkey3 OBJECT-TYPE
			SYNTAX OCTET STRING (SIZE(0..26))
			MAX-ACCESS read-write
			STATUS current
			DESCRIPTION
				"ssid_5g wepkey4."
			::= { ssid_5gEntry 12 }
		wepkey4 OBJECT-TYPE
			SYNTAX OCTET STRING (SIZE(0..26))
			MAX-ACCESS read-write
			STATUS current
			DESCRIPTION
				"ssid_5g wepkey4."
			::= { ssid_5gEntry 13 }
			
		bandwidth OBJECT-TYPE
			SYNTAX INTEGER (0..1)
			MAX-ACCESS read-write
			STATUS current
			DESCRIPTION
				"Channel Bandwidth .0:20,1:20/40"
			::= { ssid_5gEntry 14 }
		
		vhtbandwidth OBJECT-TYPE
			SYNTAX INTEGER (0..1)
			MAX-ACCESS read-write
			STATUS current
			DESCRIPTION
				"Channel VHT Bandwidth .0:20/40,1:80"
			::= { ssid_5gEntry 15 }
			
		repeater OBJECT IDENTIFIER ::= { wlan 3 } 
		
		wifi_2g OBJECT IDENTIFIER ::= { repeater 1 }

 		wifi_2gTable OBJECT-TYPE
			SYNTAX SEQUENCE OF Wifi_2gEntry
			MAX-ACCESS not-accessible
			STATUS current
			DESCRIPTION
				""
			::= { wifi_2g 1 }

		
		wifi_2gEntry OBJECT-TYPE
			SYNTAX Wifi_2gEntry
			MAX-ACCESS not-accessible
			STATUS current
			DESCRIPTION
				""
			INDEX { lineIndex }
			::= { wifi_2gTable 1 }

		Wifi_2gEntry ::=
			SEQUENCE { 
				lineIndex
					INTEGER,
				connectedWIFI
					OCTET STRING,
				authMode
					OCTET STRING,
				enctryptType
					OCTET STRING,
				passWord
					OCTET STRING,
				defaultKey
					INTEGER,
				wepKey1
					OCTET STRING,
				wepKey2
					OCTET STRING,
				wepKey3
					OCTET STRING,
				wepKey4
					OCTET STRING,
				wifiIPmode
					INTEGER,
				wifiIPaddr
					OCTET STRING,
			 }
		lineIndex OBJECT-TYPE
			SYNTAX INTEGER
			MAX-ACCESS read-only
			STATUS current
			DESCRIPTION
				"MIB index number."
			::= { wifi_2gEntry 1 }
		
		connectedWIFI OBJECT-TYPE
			SYNTAX OCTET STRING (SIZE(0..63))
			MAX-ACCESS read-write
			STATUS current
			DESCRIPTION
				"DBID_WIFI_SSID."
			::= { wifi_2gEntry 2 }
		authMode OBJECT-TYPE
			SYNTAX OCTET STRING (SIZE(0..63))
			MAX-ACCESS read-only
			STATUS current
			DESCRIPTION
				"DBID_WIFI_AUTH_MODE."
			::= { wifi_2gEntry 3 }
		enctryptType OBJECT-TYPE
			SYNTAX OCTET STRING (SIZE(0..63))
			MAX-ACCESS read-only
			STATUS current
			DESCRIPTION
				"DBID_WIFI_ENCTRYPT_TYPE."
			::= { wifi_2gEntry 4 }
		passWord OBJECT-TYPE
			SYNTAX OCTET STRING (SIZE(0..63))
			MAX-ACCESS read-write
			STATUS current
			DESCRIPTION
				"WIFI password."
			::= { wifi_2gEntry 5 }
		defaultKey OBJECT-TYPE
			SYNTAX INTEGER
				{
					null(0),
					key1(1),
					key2(2),
					key3(3),
					key4(4)
				}
			MAX-ACCESS read-write
			STATUS current
			DESCRIPTION
				"WIFI_OPEN_WEP_DEFAULT_KEY"
			::= { wifi_2gEntry 6 }
		wepKey1 OBJECT-TYPE
			SYNTAX OCTET STRING (SIZE (0..63))
			MAX-ACCESS read-write
			STATUS current
			DESCRIPTION
				"WIFI_WEP_KEY_PASSWD1"
			::= { wifi_2gEntry 7 }
		wepKey2 OBJECT-TYPE
			SYNTAX OCTET STRING (SIZE (0..63))
			MAX-ACCESS read-write
			STATUS current
			DESCRIPTION
				"WIFI_WEP_KEY_PASSWD2"
			::= { wifi_2gEntry 8 }
		wepKey3 OBJECT-TYPE
			SYNTAX OCTET STRING (SIZE (0..63))
			MAX-ACCESS read-write
			STATUS current
			DESCRIPTION
				"WIFI_WEP_KEY_PASSWD3"
			::= { wifi_2gEntry 9 }
		wepKey4 OBJECT-TYPE
			SYNTAX OCTET STRING (SIZE (0..63))
			MAX-ACCESS read-write
			STATUS current
			DESCRIPTION
				"WIFI_WEP_KEY_PASSWD4"
			::= { wifi_2gEntry 10}
		wifiIPmode OBJECT-TYPE
			SYNTAX INTEGER
			MAX-ACCESS read-write
			STATUS current
			DESCRIPTION
				"IP Mode"
			::= { wifi_2gEntry 11 }
		wifiIPaddr OBJECT-TYPE
			SYNTAX OCTET STRING (SIZE (0..63))
			MAX-ACCESS read-only
			STATUS current
			DESCRIPTION
				"IP address"
			::= { wifi_2gEntry 12 }
			
		
	-- 1.3.6.1.4.1.41010.1.11
		deviceagent OBJECT IDENTIFIER ::= { ata 11 }	
		-- 1.3.6.1.4.1.41010.1.11.1			
		cambium_id OBJECT-TYPE
			SYNTAX OCTET STRING (SIZE(0..63))
			MAX-ACCESS read-write
			STATUS current
			DESCRIPTION
				"cambium id"
			::= { deviceagent 1 }
			
		-- 1.3.6.1.4.1.41010.1.9.2			
		cambium_token OBJECT-TYPE
			SYNTAX OCTET STRING (SIZE(0..63))
			MAX-ACCESS read-write
			STATUS current
			DESCRIPTION
				"cambium token"
			::= { deviceagent 2 }
			
		-- 1.3.6.1.4.1.41010.1.9.3			
		cns_staic_url OBJECT-TYPE
			SYNTAX OCTET STRING (SIZE(0..127))
			MAX-ACCESS read-write
			STATUS current
			DESCRIPTION
				"Cloud Manager URL"
			::= { deviceagent 3 }
			
		END
--
-- 20150609-CAMBIUM-MIB.my
--

File: /dude_custom_files\CAMBIUM-ePMP-3.5.1-MIB.txt
--Cambium MIB Release CAMBIUM_MIB_VERSION

CAMBIUM-PMP80211-MIB DEFINITIONS ::= BEGIN

IMPORTS
		OBJECT-TYPE, MODULE-IDENTITY, NOTIFICATION-TYPE, enterprises,
		IpAddress, Integer32, Counter32, Counter64, TimeTicks
				FROM SNMPv2-SMI
		OBJECT-GROUP
				FROM SNMPv2-CONF
		MacAddress, DisplayString
				FROM SNMPv2-TC
		Ipv6Address
				FROM IPV6-TC;

pmpMibTree MODULE-IDENTITY
	LAST-UPDATED "201304261238Z"
	ORGANIZATION 
		"Cambium Networks Inc."
	CONTACT-INFO 
		"Cambium Networks Support"
	DESCRIPTION 
		"This module contains MIB definitions for APs."

	REVISION "201304261238Z"
	DESCRIPTION 
		"Initial Production Version."

::= { cambium 21 }

cambium				 OBJECT IDENTIFIER ::= { enterprises 17713 }

cambiumPmp80211SystemStatus	 OBJECT IDENTIFIER ::= { pmpMibTree 1 }
cambiumGeneralStatus	 OBJECT IDENTIFIER ::= { cambiumPmp80211SystemStatus 1 }
cambiumRFStatus			 OBJECT IDENTIFIER ::= { cambiumPmp80211SystemStatus 2 }
cambiumGPSStatus		 OBJECT IDENTIFIER ::= { cambiumPmp80211SystemStatus 3 }
cambiumLinkStatus		 OBJECT IDENTIFIER ::= { cambiumPmp80211SystemStatus 4 }
cambiumAcsStatus		 OBJECT IDENTIFIER ::= { cambiumPmp80211SystemStatus 5 }
cambiumMcastStatus		 OBJECT IDENTIFIER ::= { cambiumPmp80211SystemStatus 6 }
cambiumDhcpStatus		 OBJECT IDENTIFIER ::= { cambiumPmp80211SystemStatus 7 }
cambiumLicenseInfo	 OBJECT IDENTIFIER ::= { cambiumPmp80211SystemStatus 8 }
cambiumRadiusVSAStatus	 OBJECT IDENTIFIER ::= { cambiumPmp80211SystemStatus 9 }
cambiumPmp80211SystemMonitoring	 OBJECT IDENTIFIER ::= { pmpMibTree 2 }
cambiumPerformanceMonitoring   OBJECT IDENTIFIER ::= { cambiumPmp80211SystemMonitoring 1 }
cambiumRealTimeStatsMonitoring	OBJECT IDENTIFIER ::= { cambiumPmp80211SystemMonitoring 2 }
cambiumAdvancedPerformanceMonitoring OBJECT IDENTIFIER ::= { cambiumPmp80211SystemMonitoring 3 }
cambiumpmp80211SystemConfiguration	OBJECT IDENTIFIER ::= { pmpMibTree 3 }
cambiumSystemLog	 OBJECT IDENTIFIER ::= { cambiumpmp80211SystemConfiguration 1 }
cambiumDHCP			 OBJECT IDENTIFIER ::= { cambiumpmp80211SystemConfiguration 2 }
cambiumSSHServer	 OBJECT IDENTIFIER ::= { cambiumpmp80211SystemConfiguration 3 }
network				 OBJECT IDENTIFIER ::= { cambiumpmp80211SystemConfiguration 4 }
networkLan			 OBJECT IDENTIFIER ::= { network 2 }
networkWan			 OBJECT IDENTIFIER ::= { network 3 }
snmp				 OBJECT IDENTIFIER ::= { cambiumpmp80211SystemConfiguration 5 }
cambiumSystem		 OBJECT IDENTIFIER ::= { cambiumpmp80211SystemConfiguration 6 }
systemConfig		 OBJECT IDENTIFIER ::= { cambiumSystem 1 }
systemNtpServer		 OBJECT IDENTIFIER ::= { cambiumSystem 2 }
cambiumWebServer	 OBJECT IDENTIFIER ::= { cambiumpmp80211SystemConfiguration 7 }
wireless			 OBJECT IDENTIFIER ::= { cambiumpmp80211SystemConfiguration 8 }
wirelessDevice		 OBJECT IDENTIFIER ::= { wireless 1 }
wirelessInterface	 OBJECT IDENTIFIER ::= { wireless 2 }
wirelessPrefList	 OBJECT IDENTIFIER ::= { wireless 3 }
wirelessMIRList		 OBJECT IDENTIFIER ::= { wireless 4 }
wirelessRadius		 OBJECT IDENTIFIER ::= { wireless 5 }
wirelessRadiusServerList  OBJECT IDENTIFIER ::= { wireless 6 }
wirelessRadiusCertificateList  OBJECT IDENTIFIER ::= { wireless 7 }
wirelessRadiusCertificateListRow1  OBJECT IDENTIFIER ::= { wirelessRadiusCertificateList 1 }
wirelessRadiusCertificateListRow2  OBJECT IDENTIFIER ::= { wirelessRadiusCertificateList 2 }
wirelessRadiusCertificateListRow3  OBJECT IDENTIFIER ::= { wirelessRadiusCertificateList 3 }
wirelessRadiusCertificateSet  OBJECT IDENTIFIER ::= { wireless 8 }
wirelessRadiusExtraCertificateSet  OBJECT IDENTIFIER ::= { wireless 9 }
l2Firewall			 OBJECT IDENTIFIER ::= { cambiumpmp80211SystemConfiguration 9 }
l3Firewall			 OBJECT IDENTIFIER ::= { cambiumpmp80211SystemConfiguration 10 }
confQoS				 OBJECT IDENTIFIER ::= { cambiumpmp80211SystemConfiguration 11 }
dmz					 OBJECT IDENTIFIER ::= { cambiumpmp80211SystemConfiguration 12 }
portForwarding		 OBJECT IDENTIFIER ::= { cambiumpmp80211SystemConfiguration 13 }
vlans				 OBJECT IDENTIFIER ::= { cambiumpmp80211SystemConfiguration 14 }
dlkm                 OBJECT IDENTIFIER ::= { cambiumpmp80211SystemConfiguration 15 }
routing				 OBJECT IDENTIFIER ::= { cambiumpmp80211SystemConfiguration 16 }
cambiumTelnetServer	OBJECT IDENTIFIER ::= { cambiumpmp80211SystemConfiguration 17 }
cambiumDeviceAgent	 OBJECT IDENTIFIER ::= { cambiumpmp80211SystemConfiguration 20 }
upnpd                OBJECT IDENTIFIER ::= { cambiumpmp80211SystemConfiguration 21 }
lldpd                OBJECT IDENTIFIER ::= { cambiumpmp80211SystemConfiguration 23 }
mactelnet			 OBJECT IDENTIFIER ::= { cambiumpmp80211SystemConfiguration 25 }
licensed			 OBJECT IDENTIFIER ::= { cambiumpmp80211SystemConfiguration 27 }
mgmtVLAN			 OBJECT IDENTIFIER ::= { network 4 }
dataVLAN			 OBJECT IDENTIFIER ::= { network 5 }
mcastVLAN			 OBJECT IDENTIFIER ::= { network 15 }
networkBridge		 OBJECT IDENTIFIER ::= { network 7 }
mgmtIF				 OBJECT IDENTIFIER ::= { network 20 }
networkAliases		OBJECT IDENTIFIER ::= { network 27 }
networkPPPoE		OBJECT IDENTIFIER ::= { network 30 }
cambiumpmp80211SystemActions  OBJECT IDENTIFIER ::= { pmpMibTree 4 }
cambiumpmp80211SystemTraps	OBJECT IDENTIFIER ::= { pmpMibTree 0 }
cambiumpmp80211Tools  OBJECT IDENTIFIER ::= { pmpMibTree 6 }
cambiumLinkTest		 OBJECT IDENTIFIER ::= { cambiumpmp80211Tools 1 }
caminfo				 OBJECT IDENTIFIER ::= { cambiumpmp80211Tools 2 }
cambiumToolBar		 OBJECT IDENTIFIER ::= { cambiumpmp80211Tools 3 }
cambiumCfg			 OBJECT IDENTIFIER ::= { cambiumpmp80211Tools 4 }
cambiumIDM			 OBJECT IDENTIFIER ::= { cambiumpmp80211Tools 5 }
cambiumACSCfg		 OBJECT IDENTIFIER ::= { cambiumpmp80211Tools 6 }
cambiumToolBarOpts	 OBJECT IDENTIFIER ::= { cambiumToolBar 1 }
cambiumToolBarStates OBJECT IDENTIFIER ::= { cambiumToolBar 2 }
multicast            OBJECT IDENTIFIER ::= { wireless 10 }

cambiumCurrentSWInfo  OBJECT-TYPE
	SYNTAX	   DisplayString (SIZE(1..128))
	MAX-ACCESS read-only
	STATUS	   current
	DESCRIPTION 
		"Software information - version, etc.
	 Device Allocation: AP, SM"
	::= { cambiumGeneralStatus 1 }

cambiumHWInfo  OBJECT-TYPE
	SYNTAX     Integer32 (-1..6|8..20|100..250)
	MAX-ACCESS read-only
	STATUS	   current
	DESCRIPTION 
		"Hardware SKU:
			-1 - Not available
			0 - 5 GHz Connectorized Radio with Sync
			1 - 5 GHz Connectorized Radio
			2 - 5 GHz Integrated Radio
			3 - 2.4 GHz Connectorized Radio with Sync
			4 - 2.4 GHz Connectorized Radio
			5 - 2.4 GHz Integrated Radio
			6 - 5 GHz Force 200 (ROW)
			8 - 5 GHz Force 200 (FCC)
			9 - 2.4 GHz Force 200
			10 - ePMP 2000
			11 - 5 GHz Force 180 (ROW)
			12 - 5 GHz Force 180 (FCC)
			13 - 5 GHz Force 190 Radio (ROW/ETSI)
			14 - 5 GHz Force 190 Radio (FCC)
			15 - Hawkeye with different clocking scheme for FPGA
			16 - 6 GHz Force 200 Radio
			17 - 6 GHz Connectorized Radio with Sync
			18 - 6 GHz Connectorized Radio
			19 - 2.5 GHz Connectorized Radio with Sync
			20 - 2.5 GHz Connectorized Radio
			100 - (0xe855) ePMP Elevate NSM5-XW
			110 - (0xe845) ePMP Elevate NSlocoM5-XW
			111 - (0xe8a2) ePMP Elevate NSlocoM2-XW
			112 - (0xe867) ePMP Elevate NSlocoM2-V2-XW
			113 - (0xe866) ePMP Elevate NSlocoM2-V3-XW
			120 - (0xe6b5) ePMP Elevate RM5-XW-V1
			121 - (0xe3b5) ePMP Elevate RM5-XW-V2
			130 - (0xe815) ePMP Elevate NBE-M5-16-XW
			131 - (0xe825) ePMP Elevate NBE-M5-19-XW
			132 - (0xe812) ePMP Elevate NBE-M2-13-XW
			150 - (0xe3e5) ePMP Elevate PBE-M5-300-XW
			151 - (0xe4e5) ePMP Elevate PBE-M5-400-XW
			152 - (0xe885) ePMP Elevate PBE-M5-620-XW
			153 - (0xe2c2) ePMP Elevate PBE-M2-400-XW
			160 - (0xe835) ePMP Elevate AG-HP-5G-XW
			161 - (0xe832) ePMP Elevate AG-HP-2G-XW
			170 - (0xe005) ePMP Elevate NSM5-XM-V1
			171 - (0xe805) ePMP Elevate NSM5-XM-V2
			173 - (0xe012) ePMP Elevate NS-M2-V1
			176 - (0xe002) ePMP Elevate NS-M2-V2
			180 - (0xe0a5) ePMP Elevate NSlocoM5-XM-V1
			181 - (0xe8a5) ePMP Elevate NSlocoM5-XM-V2
			183 - (0xe0a2) ePMP Elavate NSloco-M2
			193 - (0xe2b5) ePMP Elevate NB-5G22-XM
			194 - (0xe2e5) ePMP Elevate NB-5G25-XM
			195 - (0xe235) ePMP Elevate NB-XM
			196 - (0xe2b2) ePMP Elevate NB-M2-V1-XM
			197 - (0xe232) ePMP Elevate NB-M2-V2-XM
			220 - (0xe006) ePMP Elevate NS-M6
			230 - (0xe215) ePMP Elevate AG-M5-23-XM
			231 - (0xe245) ePMP Elevate AG-M5-28-XM
			232 - (0xe255) ePMP Elevate AG-HP-5G-XM
			233 - (0xe212) ePMP Elevate AG-M2-16-XM
			234 - (0xe242) ePMP Elevate AG-M2-20-XM
			235 - (0xe252) ePMP Elevate AG-M2-HP-XM
			241 - (0xe105) ePMP Elevate RM5-V1-XM
			242 - (0xe1b5) ePMP Elevate RM5-V2-XM
			243 - (0xe1c5) ePMP Elevate RM5-V3-XM
			244 - (9xe8b5) ePMP Elevate RM5-V4-XM
			245 - (0xe102) ePMP Elevate RM2-V1-XM
			246 - (0xe112) ePMP Elevate RM2-V2-XM
			247 - (0xe1b2) ePMP Elevate RM2-V3-XM
			248 - (0xe1c2) ePMP Elevate RM2-V4-XM

		Device Allocation: AP, SM"
	::= { cambiumGeneralStatus 2 }

cambiumDateTime	 OBJECT-TYPE
		SYNTAX	   DisplayString (SIZE(1..128))
		MAX-ACCESS read-only
		STATUS	   current
		DESCRIPTION
		"Date and Time in format mm/dd/yyyy:hh:mm:ss
		Device Allocation: AP, SM"
		::= { cambiumGeneralStatus 3 }

cambiumSystemUptime	 OBJECT-TYPE
		SYNTAX	   DisplayString (SIZE(1..128))
		MAX-ACCESS read-only
		STATUS	   current
		DESCRIPTION
		"Device UpTime in format days, hours, minutes, and seconds -> dddd:hh:mm:ss
		Device Allocation: AP, SM"
		::= { cambiumGeneralStatus 4 }

cambiumWirelessMACAddress  OBJECT-TYPE
		SYNTAX	   DisplayString (SIZE(11..17))
		MAX-ACCESS read-only
		STATUS	   current
		DESCRIPTION
		"The device Wireless MAC address
		Device Allocation: AP, SM"
		::= { cambiumGeneralStatus 5 }

cambiumDFSStatus  OBJECT-TYPE
		SYNTAX	   Integer32 (1..6)
		MAX-ACCESS read-only
		STATUS	   current
		DESCRIPTION
		"DFS Status:
			1 - N/A, 
			2 - Channel Availability Check, 
			3 - In-Service,
			4 - Radar Signal Detected,
			5 - In-Service Monitoring at Alternative Channel,
			6 - System Not In Service due to DFS
		Device Allocation: AP, SM"
		::= { cambiumGeneralStatus 6 }

cambiumEffectiveSyncSource OBJECT-TYPE
		SYNTAX	   Integer32 (1|2|3|4)
		MAX-ACCESS read-only 
		STATUS	   current
		DESCRIPTION
		"Sync Source Status:
			1 - GPS Sync Up, 
			2 - GPS Sync Down, 
			3 - CMM4 Sync,
			4 - CMM3 Sync
		Device Allocation: AP"
		::= { cambiumGeneralStatus 7 }

cambiumEffectiveCountryCode OBJECT-TYPE
		SYNTAX	   DisplayString (SIZE(2))
		MAX-ACCESS read-only
		STATUS	   current
		DESCRIPTION
		"Current device Country Code
		Device Allocation: AP, SM"
		::= { cambiumGeneralStatus 8 }

cambiumEffectiveAntennaGain OBJECT-TYPE
		SYNTAX	   Integer32 (0..40)
		MAX-ACCESS read-only
		STATUS	   current
		DESCRIPTION
		"Effective Antenna Gain in dBi
		Device Allocation: AP, SM"
		::= { cambiumGeneralStatus 9 }

cambiumEffectiveTDDRatio OBJECT-TYPE
		SYNTAX	   Integer32 (0..4)
		MAX-ACCESS read-only 
		STATUS	   current
		DESCRIPTION
		"Effective DL/UL Ratio:
			1 - 75/25, 
			2 - 50/50, 
			3 - 30/70, 
			4 - Flexible
		Device Allocation: AP, SM"
		::= { cambiumGeneralStatus 10 }

cambiumEffectiveSSID OBJECT-TYPE
		SYNTAX	   DisplayString (SIZE(0..128))
		MAX-ACCESS read-only
		STATUS	   current
		DESCRIPTION
		"Effective SSID
		Device Allocation: AP"
		::= { cambiumGeneralStatus 11 }

cambiumEffectiveAuthenticationType OBJECT-TYPE
		SYNTAX	   Integer32 (0|1|2|3)
		MAX-ACCESS read-only
		STATUS	   current
		DESCRIPTION
		"Effective Authentication Type:
			1 - Open,
			2 - WPA2,
			3 - EAP-TTLS"
		::= { cambiumGeneralStatus 12 }

cambiumEffectiveDeviceName OBJECT-TYPE
		SYNTAX	   DisplayString (SIZE(0..128))
		MAX-ACCESS read-only
		STATUS	   current
		DESCRIPTION
		"Effective Device Name
		Device Allocation: AP, SM"
		::= { cambiumGeneralStatus 13 }

cambiumUbootVersion OBJECT-TYPE
		SYNTAX	   DisplayString (SIZE(0..128))
		MAX-ACCESS read-only
		STATUS	   current
		DESCRIPTION
		"U-boot version
		Device Allocation: AP, SM"
		::= { cambiumGeneralStatus 14 }

cambiumLANMACAddress  OBJECT-TYPE
		SYNTAX	   DisplayString (SIZE(11..17))
		MAX-ACCESS read-only
		STATUS	   current
		DESCRIPTION
		"The device LAN MAC address
		Device Allocation: AP, SM"
		::= { cambiumGeneralStatus 15 }

cambiumCurrentuImageIVersion OBJECT-TYPE
		SYNTAX	   DisplayString (SIZE(0..20))
		MAX-ACCESS read-only
		STATUS	   current
		DESCRIPTION
		"Version of firmware on uimagei partition
		Device Allocation: AP"
		::= { cambiumGeneralStatus 16 }
		
cambiumCurrentuImageVersion OBJECT-TYPE
		SYNTAX	   DisplayString (SIZE(0..20))
		MAX-ACCESS read-only
		STATUS	   current
		DESCRIPTION
		"Version of firmware on uimage partition
		Device Allocation: AP, SM"
		::= { cambiumGeneralStatus 17 }

cambiumDeviceLatitude OBJECT-TYPE
		SYNTAX	   DisplayString
		MAX-ACCESS read-only
		STATUS	   current
		DESCRIPTION
				"Current location information. GPS cordinates (latitude).
				Device Allocation: AP, SM"
		::= { cambiumGeneralStatus 18 }

cambiumDeviceLongitude OBJECT-TYPE
		SYNTAX	   DisplayString
		MAX-ACCESS read-only
		STATUS	   current
		DESCRIPTION
				"Current location information.GPS cordinates (longitude).
				Device Allocation: AP, SM"
		::= { cambiumGeneralStatus 19 }

sysRebootCounter OBJECT-TYPE
		SYNTAX	   Integer32
		MAX-ACCESS read-only
		STATUS	   current
		DESCRIPTION
				"Device Reboot Counter
				 Device Allocation: AP, SM"
		::= { cambiumGeneralStatus 20 }

cambiumDFSStatusStr	 OBJECT-TYPE
		SYNTAX	   DisplayString (SIZE(0..128))
		MAX-ACCESS read-only
		STATUS	   current
		DESCRIPTION
		"DFS Status (text)
		Device Allocation: AP, SM"
		::= { cambiumGeneralStatus 21 }

cambiumDriverType  OBJECT-TYPE
		SYNTAX	   Integer32 (1|2)
		MAX-ACCESS read-only
		STATUS	   current
		DESCRIPTION
		"SM current driver (TDD - 1, standard Wi-Fi - 2).
		Device Allocation: SM"
		::= { cambiumGeneralStatus 22 }

cambiumESN	OBJECT-TYPE
		SYNTAX	   DisplayString (SIZE(13))
		MAX-ACCESS read-only
		STATUS	   current
		DESCRIPTION
		"Device' serial number (ESN), based on MAC address
		Device Allocation: AP, SM"
		::= { cambiumGeneralStatus 30 }
		
cambiumEPMPMSN OBJECT-TYPE
		SYNTAX	   DisplayString (SIZE(13))
		MAX-ACCESS read-only
		STATUS	   current
		DESCRIPTION
		"CNS MSN serial number: AP, SM"
		::= { cambiumGeneralStatus 31 }

cambiumFactoryReset OBJECT-TYPE
		SYNTAX	   Integer32 (0|1)
		MAX-ACCESS read-only
		STATUS	   current
		DESCRIPTION
		"Factory Reset feature state.
		Default allocation: AP, SM"
		::= { cambiumGeneralStatus 32 }

cambiumSubModeType OBJECT-TYPE
		SYNTAX	   Integer32 (1|2|3|4|5)
		MAX-ACCESS read-only
		STATUS	   current
		DESCRIPTION
		"Protocol (Sub) Mode type:
			1 - TDD,
			2 - TDD PTP,
			3 - Standard WiFi,
			4 - ePTP Slave,
			5 - ePTP Master
			Device Allocation: AP, SM"
		::= { cambiumGeneralStatus 33 }

cambiumDAVersion OBJECT-TYPE
                SYNTAX     DisplayString (SIZE(8))
                MAX-ACCESS read-only
                STATUS     current
                DESCRIPTION
                "cnMaestro Device-Agent version.
                Device Allocation: AP, SM"
                ::= { cambiumGeneralStatus 35 }

ePMP2000PowerSupplyStatus OBJECT-TYPE
		SYNTAX	   Integer32 (1|2)
		MAX-ACCESS read-only
		STATUS	   current
		DESCRIPTION
				"ePMP2000: Power supply status
				Device Allocation: AP"
		::= { cambiumGeneralStatus 40 }
		
ePMP2000SmartAntennaStatus OBJECT-TYPE
		SYNTAX	   Integer32 (0|1|2|3)
		MAX-ACCESS read-only
		STATUS	   current
		DESCRIPTION
				"Smart antenna state
				Bit 0 - Smart Antenna powered, Bit 1 - Smart Antenna detected
				0 - Disabled
				1 - Enabled
				Device Allocation: AP"
		::= { cambiumGeneralStatus 41 }
		
ePMP2000ULAntennaStatus OBJECT-TYPE
		SYNTAX     Integer32 (0|1|2|3)
		MAX-ACCESS read-only
		STATUS     current
		DESCRIPTION
				"Uplink antenna state
				Bit 0 - Forced Antenna, Bit 1 - Smart Antenna Active
				0 - Disabled
				1 - Enabled
				Device Allocation: AP"
		::= { cambiumGeneralStatus 42 }

ePMP2000FPGALoadStatus OBJECT-TYPE
		SYNTAX     Integer32 (-31..1)
		MAX-ACCESS read-only
		STATUS     current
		DESCRIPTION
				"ePMP2000: FPGA Load Status:
				  1 - FPGA loaded successfully
				  0 - Undefined error
				 -1 - Initialize algorithm file fail
				 -2 - Initialize data file fail
				 -3 - Version not supported
				 -4 - Header checksum fail
				 -5 - Initialize SPI fail
				 -6 - Initialization fail
				 -7 - IDCODE verification fail
				 -8 - USERCODE verification fail
				 -9 - SED CRC verification fail
				 -10 - TAG Memory verification fail
				 -11 - Incorrect algorithm format
				 -12 - Invalid data
				 -13 - Hardware fail
				 -14 - LOOP condition fail
				 -20 - Verification fail
				 -30 - FPGA has invalid firmware
				 -31 - System use current FPGA firmware
				Device Allocation: AP"
		::= { cambiumGeneralStatus 43 }

cambiumSTAForceAntennaSelection OBJECT-TYPE
		SYNTAX	   Integer32 (0|1)
		MAX-ACCESS read-only
		STATUS	   current
		DESCRIPTION
			"is forcing antenna allowed on station
			1 - force antenna allowed on STA
			0 - force antenna forbidden
		Device Allocation: AP"
		::= { cambiumGeneralStatus 44 }

cambiumSTALinktestForceSelection OBJECT-TYPE
		SYNTAX	   Integer32 (0|1)
		MAX-ACCESS read-only
		STATUS	   current
		DESCRIPTION
			"is forcing antenna allowed on station
			during link_test
			1 - force antenna allowed on STA
			0 - force antenna forbidden
		Device Allocation: AP, SM"
		::= { cambiumGeneralStatus 45 }

cambiumEffectiveNTPServers	 OBJECT-TYPE
		SYNTAX	   IpAddress
		MAX-ACCESS read-only
		STATUS	   current
		DESCRIPTION
		"Effective NTP Server
		Device Allocation: AP, SM"
		::= { cambiumGeneralStatus 46 }

cambiumNTPDateState	 OBJECT-TYPE
		SYNTAX	   Integer32 (0|1|2)
		MAX-ACCESS read-only
		STATUS	   current
		DESCRIPTION
		"NTP date state:
			0 - NTP Disabled
			1 - NTP Enabled, Date and Time is not obtained
			2 - NTP Enabled, Date and Time is obtained from NTP Server
		Device Allocation: AP, SM"
		::= { cambiumGeneralStatus 47 }

cambiumSTAConnectedRFFrequency OBJECT-TYPE
		SYNTAX	   Integer32 (2407..6420)
		MAX-ACCESS read-only
		STATUS	   current
		DESCRIPTION
		"The frequency connected to AP
		Device Allocation: AP, SM"
		::= { cambiumRFStatus 1 }

cambiumSTAConnectedRFBandwidth OBJECT-TYPE
		SYNTAX	   Integer32 (1|2)
		MAX-ACCESS read-only 
		STATUS	   current
		DESCRIPTION
		"Connected RF Bandwidth: 
			1 for 20MHz, 
			2 for 40 MHz
		Device Allocation: SM"
		::= { cambiumRFStatus 2 }

cambiumSTADLRSSI OBJECT-TYPE
		SYNTAX	   Integer32
		MAX-ACCESS read-only
		STATUS	   current
		DESCRIPTION
		"SM RSSI in dBm
		Device Allocation: SM"
		::= { cambiumRFStatus 3 }

cambiumSTADLCINR OBJECT-TYPE
		SYNTAX	   Integer32
		MAX-ACCESS read-only
		STATUS	   obsolete
		DESCRIPTION
		"SM CINR in dBm
		Device Allocation: SM"
		::= { cambiumRFStatus 4 }

cambiumSTAConductedTXPower OBJECT-TYPE
		SYNTAX	   Integer32 (-25..30)
		MAX-ACCESS read-only
		STATUS	   current
		DESCRIPTION
		"Current TX Power (Board Output Conducted) in dBm
		Device Allocation: SM"
		::= { cambiumRFStatus 5 }

cambiumSTAUplinkMCSMode OBJECT-TYPE
		SYNTAX	   Integer32 (1..7|9..15)
		MAX-ACCESS read-only 
		STATUS	   current
		DESCRIPTION
		"UL MCS Mode: 
			1 for MCS1, 
			2 for MCS2, 
			3 for MCS3, 
			4 for MCS4, 
			5 for MCS5, 
			6 for MCS6, 
			7 for MCS7, 
			9 for MCS9, 
			10 for MCS10, 
			11 for MCS11, 
			12 for MCS12, 
			13 for MCS13, 
			14 for MCS14, 
			15 for MCS15
		Device Allocation: SM"
		::= { cambiumRFStatus 6 }

cambiumSTADownlinkMCSMode OBJECT-TYPE
		SYNTAX	   Integer32 (1..7|9..15)
		MAX-ACCESS read-only 
		STATUS	   current
		DESCRIPTION
		"DL MCS Mode: 
			1 for MCS1, 
			2 for MCS2, 
			3 for MCS3, 
			4 for MCS4, 
			5 for MCS5, 
			6 for MCS6, 
			7 for MCS7, 
			9 for MCS9, 
			10 for MCS10, 
			11 for MCS11, 
			12 for MCS12, 
			13 for MCS13, 
			14 for MCS14, 
			15 for MCS15
		Device Allocation: SM"
		::= { cambiumRFStatus 7 }

cambiumSTAConnectedAP OBJECT-TYPE
		SYNTAX	   DisplayString (SIZE(1..128))
		MAX-ACCESS read-only
		STATUS	   current
		DESCRIPTION
		"Connected AP Name (SSID), If no AP is connected, Scanning should be returned
		Device Allocation: SM"
		::= { cambiumRFStatus 8 }

cambiumSTAPowerControlMode OBJECT-TYPE
		SYNTAX	   Integer32 (-1|0|1|2)
		MAX-ACCESS read-only
		STATUS	   current
		DESCRIPTION
		"Power Control Mode on SM:
			-1 - No Value,
			0 - Disable, 
			1 - Open Loop, 
			2 - Close Loop
		Device Allocation: SM"
		::= { cambiumRFStatus 9 }

cambiumAPNumberOfConnectedSTA OBJECT-TYPE
		SYNTAX	   Integer32 (1..128)
		MAX-ACCESS read-only
		STATUS	   current
		DESCRIPTION
		"Number Of connected stations
		Device Allocation: AP"
		::= { cambiumRFStatus 10 }

cambiumAPConnectedSTAListTable OBJECT-TYPE
	SYNTAX	   SEQUENCE OF CambiumAPConnectedSTAListEntry
	MAX-ACCESS not-accessible
	STATUS	   obsolete
	DESCRIPTION
		"This table contains information relevant to the Connected Subscriber Modules:
			Subscriber Module MAC Address,
			Subscriber Module AID,
			Subscriber Module Channel,
			UL RSSI per SM,
			DL RSSI per SM,
			DL CINR per SM,
			UL CINR per SM,
			UL MCS Mode per SM,
			DL MCS Mode per SM,
			Subscriber Module IP Address
		Device Allocation: AP"
	::= { cambiumRFStatus 11 }

cambiumAPConnectedSTAListEntry OBJECT-TYPE
	SYNTAX	   CambiumAPConnectedSTAListEntry
	MAX-ACCESS not-accessible
	STATUS	   obsolete
	DESCRIPTION
		"Wireless parameters mapping for particular station.
		Device Allocation: AP"
	INDEX	{ cambiumAPNumberOfConnectedSTA }
	::= { cambiumAPConnectedSTAListTable 1 }

CambiumAPConnectedSTAListEntry ::= SEQUENCE {
		connectedSTAListMAC			   DisplayString,
		connectedSTAListAID			   Integer32,
		connectedSTAListChannel		   Integer32,
		connectedSTAListULRSSI		   Integer32,
		connectedSTAListDLRSSI		   Integer32,
		connectedSTAListULCINR		   Integer32,
		connectedSTAListDLCINR		   Integer32,
		connectedSTAListULMCS		   Integer32,
		connectedSTAListDLMCS		   Integer32,
		connectedSTAListIP			   IpAddress,
		connectedSTAListMirSrc		   DisplayString,
		connectedSTAListMirULRate	   DisplayString,
		connectedSTAListMirDLRate	   DisplayString
	}
									  
connectedSTAListMAC OBJECT-TYPE
	SYNTAX	   DisplayString (SIZE(0|11..17))
	MAX-ACCESS read-only
	STATUS	   obsolete
	DESCRIPTION
		"Connected SM WLAN MAC Address
		Device Allocation: AP"
	::= { cambiumAPConnectedSTAListEntry 1 }

connectedSTAListAID OBJECT-TYPE
	SYNTAX	   Integer32
	MAX-ACCESS read-only
	STATUS	   obsolete
	DESCRIPTION
		"Association ID
		Device Allocation: AP"
	::= { cambiumAPConnectedSTAListEntry 2 }

connectedSTAListChannel OBJECT-TYPE
	SYNTAX	   Integer32
	MAX-ACCESS read-only
	STATUS	   obsolete
	DESCRIPTION
		"Connected SM Channel
		Device Allocation: AP"
	::= { cambiumAPConnectedSTAListEntry 3 }

connectedSTAListULRSSI OBJECT-TYPE
	SYNTAX	   Integer32
	MAX-ACCESS read-only
	STATUS	   obsolete
	DESCRIPTION
		"UL RSSI per SM
		Device Allocation: AP"
	::= { cambiumAPConnectedSTAListEntry 4 }

connectedSTAListDLRSSI OBJECT-TYPE
	SYNTAX	   Integer32
	MAX-ACCESS read-only
	STATUS	   obsolete
	DESCRIPTION
		"DL RSSI per SM
		Device Allocation: AP"
	::= { cambiumAPConnectedSTAListEntry 5 }

connectedSTAListULCINR OBJECT-TYPE
	SYNTAX	   Integer32
	MAX-ACCESS read-only
	STATUS	   obsolete
	DESCRIPTION
		"UL CINR per SM
		Device Allocation: AP"
	::= { cambiumAPConnectedSTAListEntry 6 }

connectedSTAListDLCINR OBJECT-TYPE
	SYNTAX	   Integer32
	MAX-ACCESS read-only
	STATUS	   obsolete
	DESCRIPTION
		"DL CINR per SM
		Device Allocation: AP"
	::= { cambiumAPConnectedSTAListEntry 7 }

connectedSTAListULMCS OBJECT-TYPE
	SYNTAX	   Integer32 (1..15)
	MAX-ACCESS read-only
	STATUS	   obsolete
	DESCRIPTION
		"UL MCS Mode per SM:
			1 for MCS1, 
			2 for MCS2, 
			3 for MCS3, 
			4 for MCS4, 
			5 for MCS5, 
			6 for MCS6, 
			7 for MCS7, 
			9 for MCS9, 
			10 for MCS10, 
			11 for MCS11, 
			12 for MCS12, 
			13 for MCS13, 
			14 for MCS14, 
			15 for MCS15
		Device Allocation: AP"
	::= { cambiumAPConnectedSTAListEntry 8 }

connectedSTAListDLMCS OBJECT-TYPE
	SYNTAX	   Integer32 (1..15)
	MAX-ACCESS read-only
	STATUS	   obsolete
	DESCRIPTION
		"DL MCS Mode per SM:
			1 for MCS1, 
			2 for MCS2, 
			3 for MCS3, 
			4 for MCS4, 
			5 for MCS5, 
			6 for MCS6, 
			7 for MCS7, 
			9 for MCS9, 
			10 for MCS10, 
			11 for MCS11, 
			12 for MCS12, 
			13 for MCS13, 
			14 for MCS14, 
			15 for MCS15
		Device Allocation: AP"
	::= { cambiumAPConnectedSTAListEntry 9 }

connectedSTAListIP OBJECT-TYPE
	SYNTAX	   IpAddress
	MAX-ACCESS read-only
	STATUS	   obsolete
	DESCRIPTION
		"Connected SM WLAN IP Address
		Device Allocation: AP"
	::= { cambiumAPConnectedSTAListEntry 10 }

connectedSTAListMirSrc OBJECT-TYPE
	SYNTAX	   DisplayString
	MAX-ACCESS read-only
	STATUS	   obsolete
	DESCRIPTION
		"Connected SM MIR source: RADIUS server or profile ID
		Device Allocation: AP"
	::= { cambiumAPConnectedSTAListEntry 12 }

connectedSTAListMirULRate OBJECT-TYPE
	SYNTAX	   DisplayString
	MAX-ACCESS read-only
	STATUS	   obsolete
	DESCRIPTION
		"Connected SM MIR UL Rate
		Device Allocation: AP"
	::= { cambiumAPConnectedSTAListEntry 13 }

connectedSTAListMirDLRate OBJECT-TYPE
	SYNTAX	   DisplayString
	MAX-ACCESS read-only
	STATUS	   obsolete
	DESCRIPTION
		"Connected SM MIR DL Rate
		Device Allocation: AP"
	::= { cambiumAPConnectedSTAListEntry 14 }

cambiumSTADistanceKm OBJECT-TYPE
		SYNTAX	   DisplayString
		MAX-ACCESS read-only
		STATUS	   current
		DESCRIPTION
		"The distance between AP and SM in kilometers
		Device Allocation: SM"
		::= { cambiumRFStatus 12 } 

cambiumSTADistanceMil OBJECT-TYPE
		SYNTAX	   DisplayString
		MAX-ACCESS read-only
		STATUS	   current
		DESCRIPTION
		"The distance between AP and SM in miles
		Device Allocation: SM"
		::= { cambiumRFStatus 13 }	 

cambiumPropagationDelay OBJECT-TYPE
		SYNTAX	   Integer32 (-2000..5000000)
		MAX-ACCESS read-only
		STATUS	   current
		DESCRIPTION
		"SM use the calculated propagation delay to adjust the UL starting time
		Device Allocation: SM"
		::= { cambiumRFStatus 14 }	 

cambiumSTAConnectedAPListTable OBJECT-TYPE
	SYNTAX	   SEQUENCE OF CambiumSTAConnectedAPListEntry
	MAX-ACCESS not-accessible
	STATUS	   obsolete
	DESCRIPTION
		"This table contains information relevant to the Connected Subscriber Modules:
			SSID - AP Name (SSID)
			BSSID - AP MAC Address
			Channel - Operating channgel number
			Frequency - AP Operating frequency
			Bandwitdth - AP Operating Bandwidth
			Rate - AP Operating Rate
			CINR - AP Signal to Noise Ratio
			RSSI - AP Received Signal Strength Indication
			Noise - AP Noise level
			INT - Beacon Interval
			NE_ST - Last Network Entry State
			NE_AGE - Time from last Network Entry event
			SCAN_AGE - Time from last AP scanning
			Remaining_SM  - Capacity on AP from beacon
			CAPS - IEEE80211 capability flags
			MeetNEAttemptCriteria - status for eachAP after scanning
		Device Allocation: SM"
	::= { cambiumRFStatus 15 }

cambiumSTAConnectedAPListEntry OBJECT-TYPE
	SYNTAX	   CambiumSTAConnectedAPListEntry
	MAX-ACCESS not-accessible
	STATUS	   obsolete
	DESCRIPTION
		"Wireless parameters mapping for particular station.
		Device Allocation: SM"
	INDEX	{ connectedAPListSSID }
	::= { cambiumSTAConnectedAPListTable 1 }

CambiumSTAConnectedAPListEntry ::= SEQUENCE {
		connectedAPListSSID		 DisplayString,
		connectedAPListBSSID	 DisplayString,
		connectedAPListChannel	 Integer32,
		connectedAPListFrequency Integer32,
		connectedAPListBandwidth DisplayString,
		connectedAPListRate		 DisplayString,
		connectedAPListCINR		 Integer32,
		connectedAPListRSSI		 Integer32,
		connectedAPListNoise	 Integer32,
		connectedAPListINT		 Integer32,
		connectedAPListNEState	 Integer32,
		connectedAPListNEAge	 DisplayString,
		connectedAPListScanAge	DisplayString,		
		connectedAPListRemainingSTA	 Integer32,
		connectedAPListCAPS		 DisplayString,
		connectedAPAuthMethod	   DisplayString,
		connectedAPListMeetNEAttemptCriteria DisplayString
	}

connectedAPListSSID OBJECT-TYPE
	SYNTAX	   DisplayString
	MAX-ACCESS read-only
	STATUS	   obsolete
	DESCRIPTION
		"AP Name (SSID)
		Device Allocation: SM"
	::= { cambiumSTAConnectedAPListEntry 1 }

connectedAPListBSSID OBJECT-TYPE
	SYNTAX	   DisplayString
	MAX-ACCESS read-only
	STATUS	   obsolete
	DESCRIPTION
		"AP MAC Address
		Device Allocation: SM"
	::= { cambiumSTAConnectedAPListEntry 2 }

connectedAPListChannel OBJECT-TYPE
	SYNTAX	   Integer32
	MAX-ACCESS read-only
	STATUS	   obsolete
	DESCRIPTION
		"Operating channgel number
		Device Allocation: SM"
	::= { cambiumSTAConnectedAPListEntry 3 }

connectedAPListFrequency OBJECT-TYPE
	SYNTAX	   Integer32
	MAX-ACCESS read-only
	STATUS	   obsolete
	DESCRIPTION
		"AP Operating frequency
		Device Allocation: SM"
	::= { cambiumSTAConnectedAPListEntry 4 }

connectedAPListBandwidth OBJECT-TYPE
	SYNTAX	   DisplayString
	MAX-ACCESS read-only
	STATUS	   obsolete
	DESCRIPTION
		"AP Operating Bandwidth
		Device Allocation: SM"
	::= { cambiumSTAConnectedAPListEntry 5 }

connectedAPListRate OBJECT-TYPE
	SYNTAX	   DisplayString
	MAX-ACCESS read-only
	STATUS	   obsolete
	DESCRIPTION
		"AP Operating Rate
		Device Allocation: SM"
	::= { cambiumSTAConnectedAPListEntry 6 }

connectedAPListCINR OBJECT-TYPE
	SYNTAX	   Integer32
	MAX-ACCESS read-only
	STATUS	   obsolete
	DESCRIPTION
		"AP	 Carrier to Interference Noise Ratio
		Device Allocation: SM"
	::= { cambiumSTAConnectedAPListEntry 7 }

connectedAPListRSSI	 OBJECT-TYPE
	SYNTAX	   Integer32
	MAX-ACCESS read-only
	STATUS	   obsolete
	DESCRIPTION
		"AP Received Signal Strength Indication
		Device Allocation: SM"
	::= { cambiumSTAConnectedAPListEntry 8 }

connectedAPListNoise  OBJECT-TYPE
	SYNTAX	   Integer32
	MAX-ACCESS read-only
	STATUS	   obsolete
	DESCRIPTION
		"AP Noise level
		Device Allocation: SM"
	::= { cambiumSTAConnectedAPListEntry 9 }

connectedAPListINT	OBJECT-TYPE
	SYNTAX	   Integer32
	MAX-ACCESS read-only
	STATUS	   obsolete
	DESCRIPTION
		"Beacon Interval
		Device Allocation: SM"
	::= { cambiumSTAConnectedAPListEntry 10 }

connectedAPListNEState	OBJECT-TYPE
	SYNTAX	   Integer32
	MAX-ACCESS read-only
	STATUS	   obsolete
	DESCRIPTION
		"Last Network Entry State
		Device Allocation: SM"
	::= { cambiumSTAConnectedAPListEntry 11 }

connectedAPListNEAge OBJECT-TYPE
	SYNTAX	   DisplayString
	MAX-ACCESS read-only
	STATUS	   obsolete
	DESCRIPTION
		"Time from last Network Entry event
		Device Allocation: SM"
	::= { cambiumSTAConnectedAPListEntry 12 }

connectedAPListScanAge OBJECT-TYPE
	SYNTAX	   DisplayString
	MAX-ACCESS read-only
	STATUS	   obsolete
	DESCRIPTION
		"Time from last AP scanning
		Device Allocation: SM"
	::= { cambiumSTAConnectedAPListEntry 13 }

connectedAPListRemainingSTA	 OBJECT-TYPE
	SYNTAX	   Integer32
	MAX-ACCESS read-only
	STATUS	   obsolete
	DESCRIPTION
		"Remaining SM on AP
		Device Allocation: SM"
	::= { cambiumSTAConnectedAPListEntry 14 }

connectedAPListCAPS OBJECT-TYPE
	SYNTAX	   DisplayString
	MAX-ACCESS read-only
	STATUS	   obsolete
	DESCRIPTION
		"IEEE80211 capability flags
		Device Allocation: SM"
	::= { cambiumSTAConnectedAPListEntry 15 }	
	
connectedAPAuthMethod OBJECT-TYPE
	SYNTAX	   DisplayString
	MAX-ACCESS read-only
	STATUS	   obsolete
	DESCRIPTION
		   "Authentication Method
		   Device Allocation: SM"
	::= { cambiumSTAConnectedAPListEntry 16 }

connectedAPListMeetNEAttemptCriteria OBJECT-TYPE
	SYNTAX	   DisplayString
	MAX-ACCESS read-only
	STATUS	   obsolete
	DESCRIPTION
		   "Status meet NE attempt criteria
		   Device Allocation: SM"
	::= { cambiumSTAConnectedAPListEntry 17 } 

wirelessInterfaceConnectionState OBJECT-TYPE
	SYNTAX Integer32 (1|2|3)
	MAX-ACCESS read-only
	STATUS	   current
	DESCRIPTION
		"Connection State:
			1 - Scanning,
			2 - Connecting,
			3 - Connected
		Device Allocation: SM"
	::= { cambiumRFStatus 16 }

cambiumSTAPriority OBJECT-TYPE
		SYNTAX	   Integer32 (0|1|2)
		MAX-ACCESS read-only
		STATUS	   current
		DESCRIPTION
		"SM priority value:
			0 - Normal,
			1 - High,
			2 - Low
		Device Allocation: SM"
		::= { cambiumRFStatus 17 }

cambiumSTADLSNR OBJECT-TYPE
		SYNTAX	   Integer32
		MAX-ACCESS read-only
		STATUS	   current
		DESCRIPTION
		"SM SNR in dBm
		Device Allocation: SM"
		::= { cambiumRFStatus 18 }

cambiumConnectedAPMACAddress OBJECT-TYPE
		SYNTAX	   DisplayString (SIZE(0|11..17))
		MAX-ACCESS read-only
		STATUS	   current
		DESCRIPTION
		"Connected AP MAC Address
		Device Allocation: SM"
		::= { cambiumRFStatus 19 }

cambiumSTAConnectedAPTable OBJECT-TYPE
	SYNTAX	   SEQUENCE OF CambiumSTAConnectedAPEntry
	MAX-ACCESS not-accessible
	STATUS	   current
	DESCRIPTION
		"This table contains information relevant to the Connected Subscriber Modules:
			SSID - AP Name (SSID)
			BSSID - AP MAC Address
			Channel - Operating channgel number
			Frequency - AP Operating frequency
			Bandwitdth - AP Operating Bandwidth
			Rate - AP Operating Rate
			SNR - AP Signal to Noise Ratio
			RSSI - AP Received Signal Strength Indication
			Noise - AP Noise level
			INT - Beacon Interval
			NE_ST - Last Network Entry State
			NE_AGE - Time from last Network Entry event
			SCAN_AGE - Time from last AP scanning
			Remaining_SM  - Capacity on AP from beacon
			CAPS - IEEE80211 capability flags
			MeetNEAttemptCriteria - status for eachAP after scanning
		Device Allocation: SM"
	::= { cambiumRFStatus 20 }

cambiumSTAConnectedAPEntry OBJECT-TYPE
	SYNTAX	   CambiumSTAConnectedAPEntry
	MAX-ACCESS not-accessible
	STATUS	   current
	DESCRIPTION
		"Wireless parameters mapping for particular station.
		Device Allocation: SM"
	INDEX	{ connectedAPListSSID }
	::= { cambiumSTAConnectedAPTable 1 }

CambiumSTAConnectedAPEntry ::= SEQUENCE {
		connectedAPSSID		 DisplayString,
		connectedAPBSSID	 DisplayString,
		connectedAPChannel	 Integer32,
		connectedAPFrequency Integer32,
		connectedAPBandwidth DisplayString,
		connectedAPRate		 DisplayString,
		connectedAPSNR		 Integer32,
		connectedAPRSSI		 Integer32,
		connectedAPNoise	 Integer32,
		connectedAPINT		 Integer32,
		connectedAPNEState	 Integer32,
		connectedAPNEAge	 DisplayString,
		connectedAPScanAge	 DisplayString,		 
		connectedAPRemainingSTA	 Integer32,
		connectedAPCAPS		 DisplayString,
		connectedAPAuthenticationMethod		 DisplayString,
		connectedAPMeetNEAttemptCriteria DisplayString
	}

connectedAPSSID OBJECT-TYPE
	SYNTAX	   DisplayString
	MAX-ACCESS read-only
	STATUS	   current
	DESCRIPTION
		"AP Name (SSID)
		Device Allocation: SM"
	::= { cambiumSTAConnectedAPEntry 1 }

connectedAPBSSID OBJECT-TYPE
	SYNTAX	   DisplayString
	MAX-ACCESS read-only
	STATUS	   current
	DESCRIPTION
		"AP MAC Address
		Device Allocation: SM"
	::= { cambiumSTAConnectedAPEntry 2 }

connectedAPChannel OBJECT-TYPE
	SYNTAX	   Integer32
	MAX-ACCESS read-only
	STATUS	   current
	DESCRIPTION
		"Operating channgel number
		Device Allocation: SM"
	::= { cambiumSTAConnectedAPEntry 3 }

connectedAPFrequency OBJECT-TYPE
	SYNTAX	   Integer32
	MAX-ACCESS read-only
	STATUS	   current
	DESCRIPTION
		"AP Operating frequency
		Device Allocation: SM"
	::= { cambiumSTAConnectedAPEntry 4 }

connectedAPBandwidth OBJECT-TYPE
	SYNTAX	   DisplayString
	MAX-ACCESS read-only
	STATUS	   current
	DESCRIPTION
		"AP Operating Bandwidth
		Device Allocation: SM"
	::= { cambiumSTAConnectedAPEntry 5 }

connectedAPRate OBJECT-TYPE
	SYNTAX	   DisplayString
	MAX-ACCESS read-only
	STATUS	   current
	DESCRIPTION
		"AP Operating Rate
		Device Allocation: SM"
	::= { cambiumSTAConnectedAPEntry 6 }

connectedAPSNR OBJECT-TYPE
	SYNTAX	   Integer32
	MAX-ACCESS read-only
	STATUS	   current
	DESCRIPTION
		"AP Signal to Noise Ratio
		Device Allocation: SM"
	::= { cambiumSTAConnectedAPEntry 7 }

connectedAPRSSI	 OBJECT-TYPE
	SYNTAX	   Integer32
	MAX-ACCESS read-only
	STATUS	   current
	DESCRIPTION
		"AP Received Signal Strength Indication
		Device Allocation: SM"
	::= { cambiumSTAConnectedAPEntry 8 }

connectedAPNoise  OBJECT-TYPE
	SYNTAX	   Integer32
	MAX-ACCESS read-only
	STATUS	   current
	DESCRIPTION
		"AP Noise level
		Device Allocation: SM"
	::= { cambiumSTAConnectedAPEntry 9 }

connectedAPINT	OBJECT-TYPE
	SYNTAX	   Integer32
	MAX-ACCESS read-only
	STATUS	   current
	DESCRIPTION
		"Beacon Interval
		Device Allocation: SM"
	::= { cambiumSTAConnectedAPEntry 10 }

connectedAPNEState	OBJECT-TYPE
	SYNTAX	   Integer32
	MAX-ACCESS read-only
	STATUS	   current
	DESCRIPTION
		"Last Network Entry State
		Device Allocation: SM"
	::= { cambiumSTAConnectedAPEntry 11 }

connectedAPNEAge OBJECT-TYPE
	SYNTAX	   DisplayString
	MAX-ACCESS read-only
	STATUS	   current
	DESCRIPTION
		"Time from last Network Entry event
		Device Allocation: SM"
	::= { cambiumSTAConnectedAPEntry 12 }

connectedAPScanAge OBJECT-TYPE
	SYNTAX	   DisplayString
	MAX-ACCESS read-only
	STATUS	   current
	DESCRIPTION
		"Time from last AP scanning
		Device Allocation: SM"
	::= { cambiumSTAConnectedAPEntry 13 }

connectedAPRemainingSTA	 OBJECT-TYPE
	SYNTAX	   Integer32
	MAX-ACCESS read-only
	STATUS	   current
	DESCRIPTION
		"Remaining SM on AP
		Device Allocation: SM"
	::= { cambiumSTAConnectedAPEntry 14 }

connectedAPCAPS OBJECT-TYPE
	SYNTAX	   DisplayString
	MAX-ACCESS read-only
	STATUS	   current
	DESCRIPTION
		"IEEE80211 capability flags
		Device Allocation: SM"
	::= { cambiumSTAConnectedAPEntry 15 }	
	
connectedAPAuthenticationMethod OBJECT-TYPE
	SYNTAX	   DisplayString
	MAX-ACCESS read-only
	STATUS	   current
	DESCRIPTION
		   "Authentication Method
		   Device Allocation: SM"
	::= { cambiumSTAConnectedAPEntry 16 }

connectedAPMeetNEAttemptCriteria OBJECT-TYPE
	SYNTAX	   DisplayString
	MAX-ACCESS read-only
	STATUS	   current
	DESCRIPTION
		   "Status meet NE attempt criteria
		   Device Allocation: SM"
	::= { cambiumSTAConnectedAPEntry 17 }

staTxCapacity OBJECT-TYPE
	SYNTAX	   Integer32 (0..100)
	MAX-ACCESS read-only
	STATUS	   current
	DESCRIPTION
			"TX Capacity for SM
			 Device Allocation: SM"
	::= { cambiumRFStatus 21 }

staTxQuality OBJECT-TYPE
	SYNTAX	   Integer32 (0..100)
	MAX-ACCESS read-only
	STATUS	   current
	DESCRIPTION
			"TX Quality for SM
			 Device Allocation: SM"
	::= { cambiumRFStatus 22 }

cambiumePMPElevateConnected OBJECT-TYPE
		SYNTAX	   Integer32 (1..128)
		MAX-ACCESS read-only
		STATUS	   current
		DESCRIPTION
		"Number of ePMP Elevate HW is connected to ePMP AP
		Device Allocation: AP"
		::= { cambiumRFStatus 23 }

acsState OBJECT-TYPE
	SYNTAX	   Integer32 (0..3)
	MAX-ACCESS read-only
	STATUS	   current
	DESCRIPTION
		"Indicates the state of the Automatic Channel Selection (ACS) feature:
		 0 - Disabled,
		 1 - Enabled,
		 2 - Running,
		 3 - Aborting
		Device Allocation: AP"
	::= { cambiumAcsStatus 1 }

cambiumEffectiveMcastGroupLimit OBJECT-TYPE
	SYNTAX	   Integer32 (0..10)
	MAX-ACCESS read-only
	STATUS	   current
	DESCRIPTION
		"Disaplays the Effective Multicast Group Limit number:
		 0 - 10 Groups
		Device Allocation: SM"
	::= { cambiumMcastStatus 1 }

cambiumSubscribedMcastGroupNum OBJECT-TYPE
	SYNTAX	   Integer32 (0..5)
	MAX-ACCESS read-only
	STATUS	   current
	DESCRIPTION
		"Disaplays the number of subscribed Multicast Groups:
		 0 - 5 Groups
		Device Allocation: SM"
	::= { cambiumMcastStatus 2 }

cambiumAPMcastTotalGroupCount OBJECT-TYPE
	SYNTAX	   Integer32 (0..512)
	MAX-ACCESS read-only
	STATUS	   current
	DESCRIPTION
		"Disaplays the count of subscribed Multicast Groups:
		 0 - 512 Groups
		Device Allocation: AP"
	::= { cambiumMcastStatus 3 }

cambiumMcastHandlingStatus OBJECT-TYPE
	SYNTAX	   Integer32 (0|3)
	MAX-ACCESS read-only
	STATUS	   current
	DESCRIPTION
		"Disaplays the status of the Multicast features:
			0 - Fixed MCS
			3 - Multicast to Unicast
		Device Allocation: AP"
	::= { cambiumMcastStatus 4 }

cambiumSubscribedMcastGroupTable OBJECT-TYPE
	SYNTAX	   SEQUENCE OF CambiumSubscribedMcastGroupEntry
	MAX-ACCESS not-accessible
	STATUS	   current
	DESCRIPTION
		"This table contains Registered Multicast Group information:
			Multicast Group IP
		Device Allocation: SM"
	::= { cambiumMcastStatus 10 }

cambiumSubscribedMcastGroupEntry OBJECT-TYPE
	SYNTAX	   CambiumSubscribedMcastGroupEntry
	MAX-ACCESS not-accessible
	STATUS	   current
	DESCRIPTION 
				"Multicast group information for particular subscription
				Device Allocation: SM"
	INDEX	{ cambiumSubscribedMcastGroupNum }
	::= { cambiumSubscribedMcastGroupTable 1 }

CambiumSubscribedMcastGroupEntry ::= SEQUENCE {
		cambiumRegisteredMcastGroupIP			 IpAddress
	}

cambiumRegisteredMcastGroupIP OBJECT-TYPE
		SYNTAX	   IpAddress
		MAX-ACCESS read-only
		STATUS	   current
		DESCRIPTION
				"Registered Multicast Group IP
				Device Allocation: SM"
		::= { cambiumSubscribedMcastGroupEntry 1 }

dhcpServerStartIP  OBJECT-TYPE
	SYNTAX	   IpAddress
	MAX-ACCESS read-write
	STATUS	   current
	DESCRIPTION
		"Dhcp server start address
		Device Allocation: STA"
	::= { cambiumDhcpStatus 1 }

dhcpServerEndIP	 OBJECT-TYPE
	SYNTAX	   IpAddress
	MAX-ACCESS read-write
	STATUS	   current
	DESCRIPTION
		"Dhcp server end address
		Device Allocation: STA"
	::= { cambiumDhcpStatus 2 }

dhcpServerGatewayIP	 OBJECT-TYPE
	SYNTAX	   IpAddress
	MAX-ACCESS read-write
	STATUS	   current
	DESCRIPTION
		"DHCP Gateway IP Address
		Device Allocation: STA"
	::= { cambiumDhcpStatus 3 }

dhcpServerDNSIP	 OBJECT-TYPE
	SYNTAX	   IpAddress
	MAX-ACCESS read-write
	STATUS	   current
	DESCRIPTION
		"DHCP server DNS IP Address
		Device Allocation: STA"
	::= { cambiumDhcpStatus 4 }

dhcpServerStaticHostTable  OBJECT-TYPE
	SYNTAX SEQUENCE OF DhcpServerStaticHostEntry
	MAX-ACCESS not-accessible
	STATUS	   current
	DESCRIPTION
		"Table for DHCP static MAC to IP"
	::= { cambiumDhcpStatus 5 }

cambLicenseVersion OBJECT-TYPE
		SYNTAX	   DisplayString (SIZE(0|1))
		MAX-ACCESS read-only
		STATUS	   current
		DESCRIPTION
		"Device Operational Lincense Version
		Device Allocation: AP, SM"
		::= { cambiumLicenseInfo 1 }

cambLicenseSMcntUnlock OBJECT-TYPE
		SYNTAX	   DisplayString (SIZE(0|1))
		MAX-ACCESS read-only
		STATUS	   current
		DESCRIPTION
		"Full Capacity AP feature unlock, based on information from
		 Operational Lincense
		Device Allocation: AP, SM"
		::= { cambiumLicenseInfo 2 }

cambLicenseMACaddr OBJECT-TYPE
		SYNTAX	   DisplayString (SIZE(0|17))
		MAX-ACCESS read-only
		STATUS	   current
		DESCRIPTION
		"Device Operational Lincense MAC address
		Device Allocation: AP, SM"
		::= { cambiumLicenseInfo 3 }

cambLicenseCountry OBJECT-TYPE
		SYNTAX	   DisplayString (SIZE(0|1..2))
		MAX-ACCESS read-only
		STATUS	   current
		DESCRIPTION
		"Country Code for ETSI locked device, based on information from
		 Operational Lincense
		Device Allocation: AP, SM"
		::= { cambiumLicenseInfo 4 }

cambLicenseStatus OBJECT-TYPE
		SYNTAX	   Integer32 (0..4)
		MAX-ACCESS read-only
		STATUS	   current
		DESCRIPTION
		"Device Operational Lincense Status:
		 0 - Unknown
		 1 - License Valid
		 2 - Validation procedure was not provided
		 3 - Validation Fail
		 4 - License not valid for current device
		Device Allocation: AP, SM"
		::= { cambiumLicenseInfo 5 }

dhcpServerStaticHostEntry OBJECT-TYPE
	SYNTAX	   DhcpServerStaticHostEntry
	MAX-ACCESS not-accessible
	STATUS	   current
	DESCRIPTION
		"DHCP Hosts Table Entry
		Device Allocation: STA"
	INDEX	{ dhcpStaticIndex }
	::= { dhcpServerStaticHostTable 1 }

DhcpServerStaticHostEntry ::= SEQUENCE {
	dhcpStaticIndex
		Integer32,
	dhcpStaticMAC
		DisplayString,
	dhcpStaticIP
		IpAddress
}

dhcpStaticIndex	 OBJECT-TYPE
	SYNTAX	   Integer32 (0..65535)
	MAX-ACCESS read-only
	STATUS	   current
	DESCRIPTION
		"DHCP Static Table Index"
	::= { dhcpServerStaticHostEntry 1 }

dhcpStaticMAC  OBJECT-TYPE
	SYNTAX	   DisplayString (SIZE(0|17))
	MAX-ACCESS read-only
	STATUS	   current
	DESCRIPTION
		"DHCP Static MAC"
	::= { dhcpServerStaticHostEntry 2 }

dhcpStaticIP  OBJECT-TYPE
	SYNTAX	   IpAddress
	MAX-ACCESS read-only
	STATUS	   current
	DESCRIPTION
		"DHCP Static IP"
	::= { dhcpServerStaticHostEntry 3 }

dhcpServerLeaseTable  OBJECT-TYPE
		SYNTAX SEQUENCE OF DhcpServerLeaseEntry
		MAX-ACCESS not-accessible
		STATUS	   current
		DESCRIPTION
				"DHCP Assigned IP Address Table"
		::= { cambiumDhcpStatus 6 }

networkRadiusVSAmgmtVLANVID  OBJECT-TYPE
	SYNTAX	   Integer32 (0|1..4095)
	MAX-ACCESS read-only
	STATUS	   current
	DESCRIPTION
		"VSA Management VLAN ID"
	::= { cambiumRadiusVSAStatus 1 }

networkRadiusVSAmgmtVLANVP  OBJECT-TYPE
	SYNTAX	   Integer32 (0|1..7)
	MAX-ACCESS read-only
	STATUS	   current
	DESCRIPTION
		"VSA Management VLAN VP"
	::= { cambiumRadiusVSAStatus 2 }

networkRadiusVSAdataVLANVID  OBJECT-TYPE
	SYNTAX	   Integer32 (0|1..4095)
	MAX-ACCESS read-only
	STATUS	   current
	DESCRIPTION
		"VSA Data VLAN ID"
	::= { cambiumRadiusVSAStatus 3 }

networkRadiusVSAdataVLANVP  OBJECT-TYPE
	SYNTAX	   Integer32 (0|1..7)
	MAX-ACCESS read-only
	STATUS	   current
	DESCRIPTION
		"VSA Data VLAN VP"
	::= { cambiumRadiusVSAStatus 4 }

networkRadiusVSAmgmtIFVID  OBJECT-TYPE
	SYNTAX	   Integer32 (0|1..4095)
	MAX-ACCESS read-only
	STATUS	   current
	DESCRIPTION
		"VSA Separate Management Interface VLAN ID"
	::= { cambiumRadiusVSAStatus 5 }

networkRadiusVSAmgmtIFVP  OBJECT-TYPE
	SYNTAX	   Integer32 (0|1..7)
	MAX-ACCESS read-only
	STATUS	   current
	DESCRIPTION
		"VSA Separate Management Interface VLAN VP"
	::= { cambiumRadiusVSAStatus 6 }

networkRadiusVSAmcastVLANVID  OBJECT-TYPE
	SYNTAX	   Integer32 (0|1..4095)
	MAX-ACCESS read-only
	STATUS	   current
	DESCRIPTION
		"VSA Multicast VLAN ID"
	::= { cambiumRadiusVSAStatus 7 }

networkRadiusVSAmembershipVLANTable OBJECT-TYPE
	SYNTAX SEQUENCE OF NetworkRadiusVSAmembershipVLANEntry
	MAX-ACCESS not-accessible
	STATUS     current
	DESCRIPTION
		"VSA Membership VLAN Table"
	INDEX   { networkRadiusVSAmembershipVLANIndex }
        ::= { cambiumRadiusVSAStatus 10 }

networkRadiusVSAmembershipVLANEntry OBJECT-TYPE
	SYNTAX	   NetworkRadiusVSAmembershipVLANEntry
	MAX-ACCESS not-accessible
	STATUS	   current
	DESCRIPTION
		"VSA Membership VLAN Table Rule Entry"
	INDEX	{ networkRadiusVSAmembershipVLANIndex }
	::= { networkRadiusVSAmembershipVLANTable 1 }

NetworkRadiusVSAmembershipVLANEntry ::= SEQUENCE {
	networkRadiusVSAmembershipVLANIndex
		Integer32,
	networkRadiusVSAmembershipVLANVIDBegin
		Integer32,
	networkRadiusVSAmembershipVLANVIDEnd
		Integer32
}

networkRadiusVSAmembershipVLANIndex  OBJECT-TYPE
	SYNTAX	  Integer32 (0..16)
	MAX-ACCESS read-only
	STATUS	   current
	DESCRIPTION
		"VSA Membership VLAN Table Entry Index"
		::= { networkRadiusVSAmembershipVLANEntry 1 }

networkRadiusVSAmembershipVLANVIDBegin  OBJECT-TYPE
	SYNTAX	   Integer32 (0|1..4095)
	MAX-ACCESS read-only
	STATUS	   current
	DESCRIPTION
		"VSA Membership VLAN Table Entry VLAN ID Begin"
	::= { networkRadiusVSAmembershipVLANEntry 2 }

networkRadiusVSAmembershipVLANVIDEnd  OBJECT-TYPE
	SYNTAX	   Integer32 (0|1..4095)
	MAX-ACCESS read-only
	STATUS	   current
	DESCRIPTION
		"VSA Membership VLAN Table Entry VLAN ID End"
	::= { networkRadiusVSAmembershipVLANEntry 3 }

networkRadiusVSAmappingVLANTable OBJECT-TYPE
	SYNTAX SEQUENCE OF NetworkRadiusVSAmappingVLANEntry
	MAX-ACCESS not-accessible
	STATUS     current
	DESCRIPTION
		"VSA Mapping VLAN Table Rule Entry"
	INDEX   { networkRadiusVSAmappingVLANIndex }
	::= { cambiumRadiusVSAStatus 20 }

networkRadiusVSAmappingVLANEntry  OBJECT-TYPE
	SYNTAX	   NetworkRadiusVSAmappingVLANEntry
	MAX-ACCESS not-accessible
	STATUS	   current
	DESCRIPTION
		"VSA Mapping VLAN Table Rule Entry"
	INDEX	{ networkRadiusVSAmappingVLANIndex }
	::= { networkRadiusVSAmappingVLANTable 1 }

NetworkRadiusVSAmappingVLANEntry ::= SEQUENCE {
	networkRadiusVSAmappingVLANIndex
		Integer32,
	networkRadiusVSAmappingVLANCVLAN
		Integer32,
	networkRadiusVSAmappingVLANSVLAN
		Integer32
}

networkRadiusVSAmappingVLANIndex  OBJECT-TYPE
	SYNTAX	  Integer32 (0..16)
	MAX-ACCESS read-only
	STATUS	   current
	DESCRIPTION
		"VSA Mapping VLAN Table Entry Index"
		::= { networkRadiusVSAmappingVLANEntry 1 }

networkRadiusVSAmappingVLANCVLAN  OBJECT-TYPE
	SYNTAX	   Integer32 (0|1..4095)
	MAX-ACCESS read-only
	STATUS	   current
	DESCRIPTION
		"VSA Mapping VLAN Table C-VLAN ID"
	::= { networkRadiusVSAmappingVLANEntry 2 }

networkRadiusVSAmappingVLANSVLAN  OBJECT-TYPE
	SYNTAX	   Integer32 (0|1..4095)
	MAX-ACCESS read-only
	STATUS	   current
	DESCRIPTION
		"VSA Mapping VLAN Table S-VLAN ID"
	::= { networkRadiusVSAmappingVLANEntry 3 }

dhcpServerLeaseEntry OBJECT-TYPE
	SYNTAX	   DhcpServerLeaseEntry
	MAX-ACCESS not-accessible
	STATUS	   current
	DESCRIPTION
		"DHCP Assigned IP Address Entry
		Device Allocation: STA"
	INDEX	{ dhcpLeaseIndex }
	::= { dhcpServerLeaseTable 1 }

DhcpServerLeaseEntry ::= SEQUENCE {
	dhcpLeaseIndex
		Integer32,
	dhcpLeaseMAC
		DisplayString,
	dhcpLeaseIP
		IpAddress,
	dhcpLeaseDevName
		DisplayString
}

dhcpLeaseIndex	OBJECT-TYPE
	SYNTAX	   Integer32 (0..65535)
	MAX-ACCESS read-only
	STATUS	   current
	DESCRIPTION
		"DHCP lease table index"
	::= { dhcpServerLeaseEntry 1 }

dhcpLeaseMAC  OBJECT-TYPE
	SYNTAX	   DisplayString (SIZE(0|17))
	MAX-ACCESS read-only
	STATUS	   current
	DESCRIPTION
		"DHCP Assigned MAC Address"
	::= { dhcpServerLeaseEntry 2 }

dhcpLeaseIP	 OBJECT-TYPE
	SYNTAX	   IpAddress
	MAX-ACCESS read-only
	STATUS	   current
	DESCRIPTION
		"DHCP Assigned IP Address"
	::= { dhcpServerLeaseEntry 3 }

dhcpLeaseDevName  OBJECT-TYPE
	SYNTAX	   DisplayString
	MAX-ACCESS read-only
	STATUS	   current
	DESCRIPTION
		"DHCP Assigned Device Name"
	::= { dhcpServerLeaseEntry 4 }

cambiumAPConnectedSTATable OBJECT-TYPE
	SYNTAX	   SEQUENCE OF CambiumAPConnectedSTAEntry
	MAX-ACCESS not-accessible
	STATUS	   current
	DESCRIPTION
		"This table contains information relevant to the Connected Subscriber Modules:
			Subscriber Module MAC Address,
			Subscriber Module AID,
			Subscriber Module Channel,
			UL RSSI per SM,
			DL RSSI per SM,
			UL SNR per SM,
			DL SNR per SM,
			UL MCS Mode per SM,
			DL MCS Mode per SM,
			Subscriber Module IP Address,
			SM Priority,
			MIR,
			MIR UL Rate,
			MIR DL Rate,
		Device Allocation: AP"
	::= { cambiumRFStatus 30 }

cambiumAPConnectedSTAEntry OBJECT-TYPE
	SYNTAX	   CambiumAPConnectedSTAEntry
	MAX-ACCESS not-accessible
	STATUS	   current
	DESCRIPTION
		"Wireless parameters mapping for particular station.
		Device Allocation: AP"
	INDEX	{ cambiumAPNumberOfConnectedSTA }
	::= { cambiumAPConnectedSTATable 1 }

CambiumAPConnectedSTAEntry ::= SEQUENCE {
	connectedSTAMAC			   DisplayString,
	connectedSTAAID			   Integer32,
	connectedSTAChannel		   Integer32,
	connectedSTAULRSSI		   Integer32,
	connectedSTADLRSSI		   Integer32,
	connectedSTAULSNR		   Integer32,
	connectedSTADLSNR		   Integer32,
	connectedSTAULMCS		   Integer32,
	connectedSTADLMCS		   Integer32,
	connectedSTAIP			   IpAddress,
	connectedSTAPriority	   DisplayString,
	connectedSTAMirSrc		   DisplayString,
	connectedSTAMirULRate	   DisplayString,
	connectedSTAMirDLRate	   DisplayString,
	connectedSTAClickTHWAddr   DisplayString,
	connectedSTAClickTWebPort  Integer32,
	connectedSTAClickTWebSec   Integer32,
	connectedSTAClickTHostName DisplayString,
	connectedSTATXCapacity	   Integer32,
	connectedSTATXQuality	   Integer32,
	connectedSTAMcastTotalGroups Integer32,
	connectedSTAMcastGRP0	   IpAddress,
	connectedSTAMcastGRP1	   IpAddress,
	connectedSTAMcastGRP2	   IpAddress,
	connectedSTAMcastGRP3	   IpAddress,
	connectedSTAMcastGRP4	   IpAddress,
	connectedSTASessionTime	   DisplayString,
	connectedSTADLRateMbps	   DisplayString,
	connectedSTADistance       Integer32,
	connectedSTAVerticalAngle  DisplayString,
	connectedSTAHorizontalAngle DisplayString,
	connectedSTAIsForcedAngle  Integer32,
	connectedSTASKU            Integer32,
	connectedSTALinktestForceAllow Integer32,
	connectedSTAIPv6	       Ipv6Address
}

connectedSTAMAC OBJECT-TYPE
	SYNTAX	   DisplayString (SIZE(0|11..17))
	MAX-ACCESS read-only
	STATUS	   current
	DESCRIPTION
		"Connected SM WLAN MAC Address
		Device Allocation: AP"
	::= { cambiumAPConnectedSTAEntry 1 }

connectedSTAAID OBJECT-TYPE
	SYNTAX	   Integer32
	MAX-ACCESS read-only
	STATUS	   current
	DESCRIPTION
		"Association ID
		Device Allocation: AP"
	::= { cambiumAPConnectedSTAEntry 2 }

connectedSTAChannel OBJECT-TYPE
	SYNTAX	   Integer32
	MAX-ACCESS read-only
	STATUS	   current
	DESCRIPTION
		"Connected SM Channel
		Device Allocation: AP"
	::= { cambiumAPConnectedSTAEntry 3 }

connectedSTAULRSSI OBJECT-TYPE
	SYNTAX	   Integer32
	MAX-ACCESS read-only
	STATUS	   current
	DESCRIPTION
		"UL RSSI per SM
		Device Allocation: AP"
	::= { cambiumAPConnectedSTAEntry 4 }

connectedSTADLRSSI OBJECT-TYPE
	SYNTAX	   Integer32
	MAX-ACCESS read-only
	STATUS	   current
	DESCRIPTION
		"DL RSSI per SM
		Device Allocation: AP"
	::= { cambiumAPConnectedSTAEntry 5 }

connectedSTAULSNR OBJECT-TYPE
	SYNTAX	   Integer32
	MAX-ACCESS read-only
	STATUS	   current
	DESCRIPTION
		"UL SNR per SM
		Device Allocation: AP"
	::= { cambiumAPConnectedSTAEntry 6 }

connectedSTADLSNR OBJECT-TYPE
	SYNTAX	   Integer32
	MAX-ACCESS read-only
	STATUS	   current
	DESCRIPTION
		"DL SNR per SM
		Device Allocation: AP"
	::= { cambiumAPConnectedSTAEntry 7 }

connectedSTAULMCS OBJECT-TYPE
	SYNTAX	   Integer32 (1..15)
	MAX-ACCESS read-only
	STATUS	   current
	DESCRIPTION
		"UL MCS Mode per SM:
			1 for MCS1, 
			2 for MCS2, 
			3 for MCS3, 
			4 for MCS4, 
			5 for MCS5, 
			6 for MCS6, 
			7 for MCS7, 
			9 for MCS9, 
			10 for MCS10, 
			11 for MCS11, 
			12 for MCS12, 
			13 for MCS13, 
			14 for MCS14, 
			15 for MCS15
		Device Allocation: AP"
	::= { cambiumAPConnectedSTAEntry 8 }

connectedSTADLMCS OBJECT-TYPE
	SYNTAX	   Integer32 (1..15)
	MAX-ACCESS read-only
	STATUS	   current
	DESCRIPTION
		"DL MCS Mode per SM:
			1 for MCS1, 
			2 for MCS2, 
			3 for MCS3, 
			4 for MCS4, 
			5 for MCS5, 
			6 for MCS6, 
			7 for MCS7, 
			9 for MCS9, 
			10 for MCS10, 
			11 for MCS11, 
			12 for MCS12, 
			13 for MCS13, 
			14 for MCS14, 
			15 for MCS15
		Device Allocation: AP"
	::= { cambiumAPConnectedSTAEntry 9 }

connectedSTAIP OBJECT-TYPE
	SYNTAX	   IpAddress
	MAX-ACCESS read-only
	STATUS	   current
	DESCRIPTION
		"Connected SM WLAN IP Address
		Device Allocation: AP"
	::= { cambiumAPConnectedSTAEntry 10 }

connectedSTAPriority OBJECT-TYPE
	SYNTAX	   DisplayString
	MAX-ACCESS read-only
	STATUS	   current
	DESCRIPTION
		"Connected SM Priority
		Device Allocation: AP"
	::= { cambiumAPConnectedSTAEntry 11 }

connectedSTAMirSrc OBJECT-TYPE
	SYNTAX	   DisplayString
	MAX-ACCESS read-only
	STATUS	   current
	DESCRIPTION
		"Connected SM MIR source: RADIUS server or profile ID
		Device Allocation: AP"
	::= { cambiumAPConnectedSTAEntry 12 }

connectedSTAMirULRate OBJECT-TYPE
	SYNTAX	   DisplayString
	MAX-ACCESS read-only
	STATUS	   current
	DESCRIPTION
		"Connected SM MIR UL Rate
		Device Allocation: AP"
	::= { cambiumAPConnectedSTAEntry 13 }

connectedSTAMirDLRate OBJECT-TYPE
	SYNTAX	   DisplayString
	MAX-ACCESS read-only
	STATUS	   current
	DESCRIPTION
		"Connected SM MIR DL Rate
		Device Allocation: AP"
	::= { cambiumAPConnectedSTAEntry 14 }
	
connectedSTAClickTHWAddr OBJECT-TYPE
	SYNTAX	   DisplayString
	MAX-ACCESS read-only
	STATUS	   current
	DESCRIPTION
		"Connected SM BR or NAT HW addr 
		Device Allocation: AP"
	::= { cambiumAPConnectedSTAEntry 15 }

connectedSTAClickTWebPort OBJECT-TYPE
	SYNTAX	   Integer32
	MAX-ACCESS read-only
	STATUS	   current
	DESCRIPTION
		"Connected SM WEB port 
		Device Allocation: AP"
	::= { cambiumAPConnectedSTAEntry 16 }

connectedSTAClickTWebSec OBJECT-TYPE
	SYNTAX	   Integer32
	MAX-ACCESS read-only
	STATUS	   current
	DESCRIPTION
		"Connected SM WEB security (HTTPS) 
		Device Allocation: AP"
	::= { cambiumAPConnectedSTAEntry 17 }

connectedSTAClickTHostName OBJECT-TYPE
	SYNTAX	   DisplayString
	MAX-ACCESS read-only
	STATUS	   current
	DESCRIPTION
		"Connected SM Host Name 
		Device Allocation: AP"
	::= { cambiumAPConnectedSTAEntry 18 }
connectedSTATXCapacity OBJECT-TYPE
        SYNTAX     Integer32 (0..100)
        MAX-ACCESS read-only
        STATUS     current
        DESCRIPTION
                "TX Capacity per SM
                Device Allocation: AP"
        ::= { cambiumAPConnectedSTAEntry 19 }

connectedSTATXQuality OBJECT-TYPE
        SYNTAX     Integer32 (0..100)
        MAX-ACCESS read-only
        STATUS     current
        DESCRIPTION
                "TX Quality per SM
                Device Allocation: AP"
        ::= { cambiumAPConnectedSTAEntry 20 }

connectedSTAMcastTotalGroups OBJECT-TYPE
	SYNTAX	   Integer32
	MAX-ACCESS read-only
	STATUS	   current
	DESCRIPTION
		"Connected SM Total multicast groups
		subscribed count
		Device Allocation: AP"
	::= { cambiumAPConnectedSTAEntry 21 }

connectedSTAMcastGRP0 OBJECT-TYPE
	SYNTAX	   IpAddress
	MAX-ACCESS read-only
	STATUS	   current
	DESCRIPTION
		"Connected SM subscribed multicast
		group 0
		Device Allocation: AP"
	::= { cambiumAPConnectedSTAEntry 22 }

connectedSTAMcastGRP1 OBJECT-TYPE
	SYNTAX	   IpAddress
	MAX-ACCESS read-only
	STATUS	   current
	DESCRIPTION
		"Connected SM subscribed multicast
		group 1
		Device Allocation: AP"
	::= { cambiumAPConnectedSTAEntry 23 }

connectedSTAMcastGRP2 OBJECT-TYPE
	SYNTAX	   IpAddress
	MAX-ACCESS read-only
	STATUS	   current
	DESCRIPTION
		"Connected SM subscribed multicast
		group 2
		Device Allocation: AP"
	::= { cambiumAPConnectedSTAEntry 24 }

connectedSTAMcastGRP3 OBJECT-TYPE
	SYNTAX	   IpAddress
	MAX-ACCESS read-only
	STATUS	   current
	DESCRIPTION
		"Connected SM subscribed multicast
		group 3
		Device Allocation: AP"
	::= { cambiumAPConnectedSTAEntry 25 }

connectedSTAMcastGRP4 OBJECT-TYPE
	SYNTAX	   IpAddress
	MAX-ACCESS read-only
	STATUS	   current
	DESCRIPTION
		"Connected SM subscribed multicast
		group 4
		Device Allocation: AP"
	::= { cambiumAPConnectedSTAEntry 26 }

connectedSTASessionTime OBJECT-TYPE
	SYNTAX	   DisplayString
	MAX-ACCESS read-only
	STATUS	   current
	DESCRIPTION
		"Connected SM time since allocation 
		Device Allocation: AP"
	::= { cambiumAPConnectedSTAEntry 27 }
	
connectedSTADLRateMbps OBJECT-TYPE
	SYNTAX	   DisplayString
	MAX-ACCESS read-only
	STATUS	   current
	DESCRIPTION
		"Connected SM DL Rate in MBits/sec
		Device Allocation: AP"
	::= { cambiumAPConnectedSTAEntry 28 }

connectedSTADistance OBJECT-TYPE
	SYNTAX	   Integer32
	MAX-ACCESS read-only
	STATUS	   current
	DESCRIPTION
		"STA distnce to AP
		Device Allocation: AP"
	::= { cambiumAPConnectedSTAEntry 29 }

connectedSTAVerticalAngle OBJECT-TYPE
	SYNTAX	   DisplayString
	MAX-ACCESS read-only
	STATUS	   current
	DESCRIPTION
		"Connected SM vertical angle"
	::= { cambiumAPConnectedSTAEntry 30 }

connectedSTAHorizontalAngle OBJECT-TYPE
	SYNTAX	   DisplayString
	MAX-ACCESS read-only
	STATUS	   current
	DESCRIPTION
		"Connected SM horizontal angle"
	::= { cambiumAPConnectedSTAEntry 31 }

connectedSTAIsForcedAngle OBJECT-TYPE
    SYNTAX     Integer32 (0..3)
    MAX-ACCESS read-only
    STATUS     current
    DESCRIPTION
        "Shows that antenna is forced by user. 
         Bit 0 - polarization H, Bit 1 - polarization V. 
         0 - means that antenna and angle are selected by algorithm;
         1 - means that antenna and angle are forced by user."
    ::= { cambiumAPConnectedSTAEntry 32 }

connectedSTASKU OBJECT-TYPE
        SYNTAX     Integer32 (0..255)
        MAX-ACCESS read-only
        STATUS     current
        DESCRIPTION
                "SKU Number of the connected SM
                Device Allocation: AP"
        ::= { cambiumAPConnectedSTAEntry 33 }

connectedSTALinktestForceAllow OBJECT-TYPE
	SYNTAX     Integer32 (0..1)
	MAX-ACCESS read-only
	STATUS     current
	DESCRIPTION
		"Shows is force antenna allowed during linktest.
		0 - means that linktest have to run with default antenna
		1 - means that antenna can be selected during linktest"
	::= { cambiumAPConnectedSTAEntry 34 }

connectedSTAIPv6 OBJECT-TYPE
	SYNTAX	   Ipv6Address
	MAX-ACCESS read-only
	STATUS	   current
	DESCRIPTION
		"Connected SM WLAN IPv6 Address
		Device Allocation: AP"
	::= { cambiumAPConnectedSTAEntry 35 }        

cambiumAPBridgeTable OBJECT-TYPE
	SYNTAX	   SEQUENCE OF CambiumAPBridgeEntry
	MAX-ACCESS not-accessible
	STATUS	   current
	DESCRIPTION
		"This table contains information relevant to the particular AP bridge
		 interfaces list:
			Bridge Name,
			Device MAC Address,
			Device Port,
			SM MAC Address,
			Aging Time in seconds
		Device Allocation: AP"
	::= { cambiumRFStatus 40 }

cambiumAPBridgeEntry OBJECT-TYPE
	SYNTAX	   CambiumAPBridgeEntry
	MAX-ACCESS not-accessible
	STATUS	   current
	DESCRIPTION
		"Interface list for particular bridge.
		Device Allocation: AP"
	INDEX	{ camAPBrTabDevMACAddress }
	::= { cambiumAPBridgeTable 1 }

CambiumAPBridgeEntry ::= SEQUENCE {
	camAPBrTabBridgeName	DisplayString,
	camAPBrTabDevMACAddress DisplayString,
	camAPBrTabDevPort		DisplayString,
	camAPBrTabSTAMACAddress DisplayString,
	camAPBrTabAgingTime		Counter32
}

camAPBrTabBridgeName OBJECT-TYPE
	SYNTAX	   DisplayString
	MAX-ACCESS read-only
	STATUS	   current
	DESCRIPTION
		"Bridge Name
		Device Allocation: AP"
	::= { cambiumAPBridgeEntry 1 }

camAPBrTabDevMACAddress OBJECT-TYPE
	SYNTAX	   DisplayString
	MAX-ACCESS read-only
	STATUS	   current
	DESCRIPTION
		"Device MAC Address
		Device Allocation: AP"
	::= { cambiumAPBridgeEntry 2 }

camAPBrTabDevPort OBJECT-TYPE
	SYNTAX	   DisplayString
	MAX-ACCESS read-only
	STATUS	   current
	DESCRIPTION
		"Device Port
		Device Allocation: AP"
	::= { cambiumAPBridgeEntry 3 }

camAPBrTabSTAMACAddress OBJECT-TYPE
	SYNTAX	   DisplayString
	MAX-ACCESS read-only
	STATUS	   current
	DESCRIPTION
		"SM MAC Address
		Device Allocation: AP"
	::= { cambiumAPBridgeEntry 4 }

camAPBrTabAgingTime OBJECT-TYPE
	SYNTAX	   Counter32
	MAX-ACCESS read-only
	STATUS	   current
	DESCRIPTION
		"Aging time in seconds
		Device Allocation: AP"
	::= { cambiumAPBridgeEntry 5 }

cambiumSTABridgeTable OBJECT-TYPE
	SYNTAX	   SEQUENCE OF CambiumSTABridgeEntry
	MAX-ACCESS not-accessible
	STATUS	   current
	DESCRIPTION
		"This table contains information relevant to the particular SM bridge
		 interfaces list:
			Bridge Name,
			Device MAC Address,
			Device Port,
			Aging Time in seconds
		Device Allocation: SM"
	::= { cambiumRFStatus 50 }

cambiumSTABridgeEntry OBJECT-TYPE
	SYNTAX	   CambiumSTABridgeEntry
	MAX-ACCESS not-accessible
	STATUS	   current
	DESCRIPTION
		"Interface list for particular bridge.
		Device Allocation: SM"
	INDEX	{ camSTABrTabDevMACAddress }
	::= { cambiumSTABridgeTable 1 }

CambiumSTABridgeEntry ::= SEQUENCE {
	camSTABrTabBridgeName		DisplayString,
	camSTABrTabDevMACAddress	DisplayString,
	camSTABrTabDevPort			DisplayString,
	camSTABrTabAgingTime		Counter32
}

camSTABrTabBridgeName OBJECT-TYPE
	SYNTAX	   DisplayString
	MAX-ACCESS read-only
	STATUS	   current
	DESCRIPTION
		"Bridge Name
		Device Allocation: SM"
	::= { cambiumSTABridgeEntry 1 }

camSTABrTabDevMACAddress OBJECT-TYPE
	SYNTAX	   DisplayString
	MAX-ACCESS read-only
	STATUS	   current
	DESCRIPTION
		"Device MAC Address
		Device Allocation: SM"
	::= { cambiumSTABridgeEntry 2 }

camSTABrTabDevPort OBJECT-TYPE
	SYNTAX	   DisplayString
	MAX-ACCESS read-only
	STATUS	   current
	DESCRIPTION
		"Device Port
		Device Allocation: SM"
	::= { cambiumSTABridgeEntry 3 }

camSTABrTabAgingTime OBJECT-TYPE
	SYNTAX	   Counter32
	MAX-ACCESS read-only
	STATUS	   current
	DESCRIPTION
		"Aging time in seconds
		Device Allocation: SM"
	::= { cambiumSTABridgeEntry 4 }

cambiumSTAMAC OBJECT-TYPE
	SYNTAX	   DisplayString (SIZE(17))
	MAX-ACCESS read-only
	STATUS	   current
	DESCRIPTION
			"String with dropped SM's MAC address
			 Device Allocation: AP"
	::= { cambiumRFStatus 60 }

cambiumSTADropReason OBJECT-TYPE
	SYNTAX	   DisplayString (SIZE(0..64))
	MAX-ACCESS read-only
	STATUS	   current
	DESCRIPTION
			"String with SM's drop reason
			 Device Allocation: AP"
	::= { cambiumRFStatus 61 }

cambiumNetworkEntryFailureSTAMAC OBJECT-TYPE
	SYNTAX	   DisplayString (SIZE(17))
	MAX-ACCESS read-only
	STATUS	   current
	DESCRIPTION
			"String with rejected SM's MAC 
			 Device Allocation: AP "
	::= { cambiumRFStatus 62 }

cambiumNetworkEntryFailureReason OBJECT-TYPE
	SYNTAX	   DisplayString (SIZE(0..64))
	MAX-ACCESS read-only
	STATUS	   current
	DESCRIPTION
			"String with SM's reject reason
			 Device Allocation: AP "
	::= { cambiumRFStatus 63 }	


cambiumGPSCurrentSyncState OBJECT-TYPE
		SYNTAX	   Integer32 (0..5)
		MAX-ACCESS read-only
		STATUS	   current
		DESCRIPTION
		"GPS Current SYNC State:
			0 - The Initialization State
			1 - The No Synchronization State
			2 - The Synchronization State
			3 - The Hold Off State
			4 - The Regaining Sync State
			5 - The Free Run State
		Device Allocation: AP"
		::= { cambiumGPSStatus 1 }
		
cambiumGPSLatitude OBJECT-TYPE
		SYNTAX	   DisplayString (SIZE(0..128))
		MAX-ACCESS read-only
		STATUS	   current
		DESCRIPTION
		"Current location information from GPS Device. GPS cordinates (latitude).
		Device Allocation: AP, SM"
		::= { cambiumGPSStatus 2 }
		
cambiumGPSLongitude OBJECT-TYPE
		SYNTAX	   DisplayString (SIZE(0..128))
		MAX-ACCESS read-only
		STATUS	   current
		DESCRIPTION
		"Current location information from GPS Device. GPS cordinates (longitude).
		Device Allocation: AP, SM"
		::= { cambiumGPSStatus 3 }
		
cambiumGPSHeight OBJECT-TYPE
		SYNTAX	   DisplayString (SIZE(0..128))
		MAX-ACCESS read-only
		STATUS	   current
		DESCRIPTION
		"Current location information from GPS Device. GPS coordinates (Height).
		Device Allocation: AP, SM"
		::= { cambiumGPSStatus 4 }
		
cambiumGPSTime OBJECT-TYPE
		SYNTAX	   DisplayString (SIZE(0..128))
		MAX-ACCESS read-only
		STATUS	   current
		DESCRIPTION
		"Current Time/Date information from GPS Device. GPS (Time).
		Device Allocation: AP, SM"
		::= { cambiumGPSStatus 5 }
		
cambiumGPSNumTrackedSat OBJECT-TYPE
		SYNTAX	   Integer32 (1..128)
		MAX-ACCESS read-only
		STATUS	   current
		DESCRIPTION
		"Current Satellite information from GPS Device. GPS (Number of Satellites Tracked).
		Device Allocation: AP, SM"
		::= { cambiumGPSStatus 6 }
		
cambiumGPSNumVisibleSat OBJECT-TYPE
		SYNTAX	   Integer32 (1..128)
		MAX-ACCESS read-only
		STATUS	   current
		DESCRIPTION
		"Current Satellite information from GPS Device. GPS (Number of Satellites Visible).
		Device Allocation: AP, SM"
		::= { cambiumGPSStatus 7 }
	   
cambiumGPSSatSNRTable OBJECT-TYPE
		SYNTAX SEQUENCE OF CambiumGPSSatSNREntry
		MAX-ACCESS not-accessible
		STATUS	   current
		DESCRIPTION
		"Table of Current Satellite information from GPS Device. GPS (SNR of Satellites).
		Device Allocation: AP, SM"
		::= { cambiumGPSStatus 8 }
		
cambiumGPSSatSNREntry OBJECT-TYPE
		SYNTAX	   CambiumGPSSatSNREntry
		MAX-ACCESS not-accessible
		STATUS	   current
		DESCRIPTION
		"Satellite SNR values for Visible and Tracked Satellites 
		Device Allocation: AP"
		 INDEX	 { gpsSatelliteId }
		 ::= { cambiumGPSSatSNRTable 1 }
	
CambiumGPSSatSNREntry  ::= SEQUENCE {
	gpsSatelliteId Integer32,
	gpsSnrValue Integer32,
	gpsSatelliteStatus Integer32
	}
	
gpsSatelliteId OBJECT-TYPE
		 SYNTAX Integer32 (0..255)
		 MAX-ACCESS read-only
		 STATUS	 current
		 DESCRIPTION
			"Satellite ID for which SNR is displayed"
		 ::= {cambiumGPSSatSNREntry 1 }

gpsSnrValue OBJECT-TYPE
		 SYNTAX Integer32 (0..99)
		 MAX-ACCESS read-only
		 STATUS current
		 DESCRIPTION
			"SNR value for a satellite"
		::= {cambiumGPSSatSNREntry 2 }

gpsSatelliteStatus OBJECT-TYPE
		SYNTAX Integer32 (1|2)
		MAX-ACCESS read-only
		STATUS current
		DESCRIPTION
			"Satellite Status whether they are visible or tracked
			 1 - Visible
			 2 - Tracked"
		DEFVAL { 1 }
		::= {cambiumGPSSatSNREntry	3} 
		
cambiumGPSDeviceInfo OBJECT-TYPE
		SYNTAX	   DisplayString (SIZE(0..128))
		MAX-ACCESS read-only
		STATUS	   current
		DESCRIPTION
		"GPS Device Information
		Device Allocation: AP, SM"
		::= { cambiumGPSStatus 9 }
		
cambiumGPSFirmwareUpdateStatus	OBJECT-TYPE
	SYNTAX	   Integer32 (0..10)
	MAX-ACCESS read-only
	STATUS	   current
	DESCRIPTION 
		"Software Update Status OID
			0 - No GPS FW Update is progress or No FW update is required,
			1 - GPS FW Update is in progress, Uploading SW package to device,
			2 - GPS FW Update is in progress, Verifying SHA2 signature,
			3 - GPS FW Update is in progress, Executing pre-update script,
			4 - GPS FW Update is in progress, Uploading Firmware to GPS device,
			5 - GPS FW Update is in progress, Uploading Firmware to GPS device,
			6 - GPS FW Update is in progress, Executing post-update script,
			7 - GPS FW Update is finished, waiting for reboot,
			8 - GPS FW Update is Required, Please upgrade to latest GPS FW,
		When GPS FW Update is successfully, return value is 7,
		GUI or NMS indicate that GPS FW update was successful,
		Device can be rebooted.
		Device Allocation: AP, SM"
	::= { cambiumGPSStatus 10} 
		
cambiumLANStatus OBJECT-TYPE
		SYNTAX	   Integer32 (0|1|2)
		MAX-ACCESS read-only
		STATUS	   current
		DESCRIPTION
		"Use the RFC-1213 ifTable to view the physical port status. 
		This attribute indicates the Linux driver status of the port.
		LAN Status:
			0 - Down,
			1 - Up,
			2 - Disabled
		Device Allocation: AP, SM"
		::= { cambiumLinkStatus 1 }

cambiumWLANStatus OBJECT-TYPE
		SYNTAX	   Integer32 (0|1|2)
		MAX-ACCESS read-only
		STATUS	   current
		DESCRIPTION
		"WLAN Status:
			0 - Down, 
			1 - Up
		Device Allocation: AP, SM"
		::= { cambiumLinkStatus 2 }

cambiumEffectiveDeviceIPAddress OBJECT-TYPE
		SYNTAX	   IpAddress
		MAX-ACCESS read-only
		STATUS	   current
		DESCRIPTION
		"Current Device IP address
		Device Allocation: AP, SM"
		::= { cambiumLinkStatus 3 }

cambiumEffectiveSTANetworkMode OBJECT-TYPE
		SYNTAX	   Integer32 (1|2|3)
		MAX-ACCESS read-only
		STATUS	   current
		DESCRIPTION
		"Effective SM Network Mode:
			1 - NAT,
			2 - Bridge,
			3 - Router
		Device Allocation: SM"
		::= { cambiumLinkStatus 4 }

cambiumEffectiveDeviceLANNetMask OBJECT-TYPE
		SYNTAX	   IpAddress
		MAX-ACCESS read-only
		STATUS	   current
		DESCRIPTION
		"Current Device Network Mask
		Device Allocation: AP, SM"
		::= { cambiumLinkStatus 5 }

cambiumEffectiveDeviceDefaultGateWay OBJECT-TYPE
		SYNTAX	   IpAddress
		MAX-ACCESS read-only
		STATUS	   current
		DESCRIPTION
		"Effective Device Default Gateway IP Address,
		NOTE: This parameters lists only the first gateway IP
		Device Allocation: AP, SM"
		::= { cambiumLinkStatus 6 }

cambiumEffectiveDeviceDNSIPAddress OBJECT-TYPE
		SYNTAX	   IpAddress
		MAX-ACCESS read-only
		STATUS	   current
		DESCRIPTION
		"Current Device DNS IP Address,
		NOTE: This parameter displays only the first DNS IP
		Device Allocation: AP, SM"
		::= { cambiumLinkStatus 7 }

cambiumEffectiveWANIPAddress OBJECT-TYPE
		SYNTAX	   IpAddress
		MAX-ACCESS read-only
		STATUS	   current
		DESCRIPTION
		"Current Device WLAN IP address
		Device Allocation: SM"
		::= { cambiumLinkStatus 8 }

cambiumEffectiveDeviceWANNetMask OBJECT-TYPE
		SYNTAX	   IpAddress
		MAX-ACCESS read-only
		STATUS	   current
		DESCRIPTION
		"Current Device Network Mask
		Device Allocation: SM"
		::= { cambiumLinkStatus 9 }

cambiumEffectiveDeviceWANPPPoEStatus OBJECT-TYPE
	SYNTAX	   Integer32 (0|1)
	MAX-ACCESS read-only
	STATUS	   current
	DESCRIPTION
		"WAN PPPoE Status:
			0 - Disabled
			1 - Enabled-Connected
			2 - Enabled-Connecting
			3 - Enabled-Disconnected
		Device Allocation: SM"
	DEFVAL	{ 0 }
	::= { cambiumLinkStatus 10 }

cambiumLANModeStatus  OBJECT-TYPE
	SYNTAX	   Integer32 (-1|0|1)
	MAX-ACCESS read-only
	STATUS	   current
	DESCRIPTION
		"LAN Mode Status
			-1 - No data,
			 0 - Half,
			 1 - Full
		Device Allocation: AP, SM"
	::= { cambiumLinkStatus 11 }

cambiumLANSpeedStatus  OBJECT-TYPE
	SYNTAX	   Integer32 (-1|10|100|1000)
	MAX-ACCESS read-only
	STATUS	   current
	DESCRIPTION
		"LAN Speed Status
			-1 - No data,
			 10 - 10 Mb/s,
			 100 - 100 Mb/s,
			 1000 - 1000 Mb/s
		Device Allocation: AP, SM"
	::= { cambiumLinkStatus 12 }

cambiumDHCPOption82Status OBJECT-TYPE
	SYNTAX	   Integer32 (0|1)
	MAX-ACCESS read-only
	STATUS	   current
	DESCRIPTION
		"DHCP Option82 Status:
			0 - Disabled
			1 - Enabled
		Device Allocation: AP"
	::= { cambiumLinkStatus 13 }

cambiumLAN2ModeStatus  OBJECT-TYPE
	SYNTAX	   Integer32 (-1|0|1)
	MAX-ACCESS read-only
	STATUS	   current
	DESCRIPTION
		"2nd LAN Mode Status
			-1 - No data,
			 0 - Half,
			 1 - Full
		Device Allocation: AP, SM"
	::= { cambiumLinkStatus 14 }

cambiumLAN2SpeedStatus  OBJECT-TYPE
	SYNTAX	   Integer32 (-1|10|100|1000)
	MAX-ACCESS read-only
	STATUS	   current
	DESCRIPTION
		"2nd LAN Speed Status
			-1 - No data,
			 10 - 10 Mb/s,
			 100 - 100 Mb/s,
			 1000 - 1000 Mb/s
		Device Allocation: AP, SM"
	::= { cambiumLinkStatus 15 }

cambiumLAN2Status OBJECT-TYPE
		SYNTAX	   Integer32 (0|1|2)
		MAX-ACCESS read-only
		STATUS	   current
		DESCRIPTION
		"Use the RFC-1213 ifTable to view the physical port status.
		This attribute indicates the Linux driver status of the port.
		2nd LAN Status:
			0 - Down,
			1 - Up,
			2 - Disabled
		Device Allocation: AP, SM"
		::= { cambiumLinkStatus 16 }

cambiumARPTable	 OBJECT-TYPE
	SYNTAX SEQUENCE OF CambiumARPEntry
	MAX-ACCESS not-accessible
	STATUS	   current
	DESCRIPTION
		"Neibour devices IP/MAC pair
		 Table"
	::= { cambiumLinkStatus 20 }

cambiumManagementIFStatus OBJECT-TYPE
		SYNTAX	   Integer32 (0|1)
		MAX-ACCESS read-only
		STATUS	   current
		DESCRIPTION
		"Separate Management Interface Status:
			0 - Down, 
			1 - Up 
		Device Allocation: SM"
		::= { cambiumLinkStatus 25 }

cambiumManagementIFIPAddress OBJECT-TYPE
		SYNTAX	   IpAddress
		MAX-ACCESS read-only
		STATUS	   current
		DESCRIPTION
		"Current Device Separate Management IP address
		Device Allocation: SM"
		::= { cambiumLinkStatus 26 }

cambiumManagementIFNetMask OBJECT-TYPE
		SYNTAX	   IpAddress
		MAX-ACCESS read-only
		STATUS	   current
		DESCRIPTION
		"Current Device Separate Management Network Mask
		Device Allocation: SM"
		::= { cambiumLinkStatus 27 }

cambiumManagementIFGateway OBJECT-TYPE
		SYNTAX	   IpAddress
		MAX-ACCESS read-only
		STATUS	   current
		DESCRIPTION
		"Current Device Separate Management Gateway
		Device Allocation: SM"
		::= { cambiumLinkStatus 28 }

cambiumEffectiveNetworkLanMTU OBJECT-TYPE
		SYNTAX	   Integer32 (0|576..1700)
		MAX-ACCESS read-only
		STATUS	   current
		DESCRIPTION
			"SM NAT LAN MTU size
			Device Allocation: SM"
		DEFVAL	{ 1500 }
		::= { cambiumLinkStatus 29 }

cambiumEffectiveNetworkBridgeMTU OBJECT-TYPE
		SYNTAX	   Integer32 (0|576..1700)
		MAX-ACCESS read-only
		STATUS	   current
		DESCRIPTION
			"Device Bridge MTU size
			Device Allocation: AP, SM"
		DEFVAL	{ 1500 }
		::= { cambiumLinkStatus 30 }

cambiumStaticRoutesTable  OBJECT-TYPE
	SYNTAX SEQUENCE OF CambiumStaticRoutesEntry
	MAX-ACCESS not-accessible
	STATUS	   current
	DESCRIPTION
		"Static Routes Table"
	::= { cambiumLinkStatus 31 }

cambiumIPAliasTable OBJECT-TYPE
	SYNTAX SEQUENCE OF CambiumIPAliasEntry
	MAX-ACCESS not-accessible
	STATUS	   current
	DESCRIPTION
		"IP aliases list table.
		Device Allocation: AP, SM"
	::= { cambiumLinkStatus 32 }

cambiumCnsServConsStat OBJECT-TYPE
		SYNTAX	   DisplayString (SIZE(0..128))
		MAX-ACCESS read-only
		STATUS	   current
		DESCRIPTION
			"cnMaestro Connection Status:
			Cambium provides cloud management of Cambium devices, called cnMaestro.
			This describes the state of the connection to the cnMaestro"
		::= { cambiumLinkStatus 33 }

cambiumCnsServAccountID  OBJECT-TYPE
		SYNTAX	   DisplayString (SIZE(0..128))
		MAX-ACCESS read-only
		STATUS	   current
		DESCRIPTION
			"cnMaestro Account ID:
			Displays cnMaestro Account ID, 
			This is the account ID for the customer.
			It is returned from the cloud management system."
		::= { cambiumLinkStatus 34 }

cambiumAPCnsMGMTState  OBJECT-TYPE
		SYNTAX	   Integer32 (0..1)
		MAX-ACCESS read-only
		STATUS	   current
		DESCRIPTION
		"AP Device management State"
		::= { cambiumLinkStatus 35 }
cambiumEffectiveDeviceIPv6Address OBJECT-TYPE
                SYNTAX     Ipv6Address
                MAX-ACCESS read-only
                STATUS     current
                DESCRIPTION
                "Current Device IPv6 address
                Device Allocation: AP, SM"
                ::= { cambiumLinkStatus 36 }

cambiumLinkLocalDeviceIPv6Address OBJECT-TYPE
                SYNTAX     Ipv6Address
                MAX-ACCESS read-only
                STATUS     current
                DESCRIPTION
                "Device Link Local IPv6 address
                Device Allocation: AP, SM"
                ::= { cambiumLinkStatus 37 }

cambiumEffectiveWANIPv6Address OBJECT-TYPE
                SYNTAX     Ipv6Address
                MAX-ACCESS read-only
                STATUS     current
                DESCRIPTION
                "Current Device WLAN IPv6 address
                Device Allocation: SM"
                ::= { cambiumLinkStatus 38 }

cambiumLinkLocalWANIPv6Address OBJECT-TYPE
                SYNTAX     Ipv6Address
                MAX-ACCESS read-only
                STATUS     current
                DESCRIPTION
                "Current Device WLAN Link Local IPv6 address
                Device Allocation: SM"
                ::= { cambiumLinkStatus 39 }

cambiumManagementIFIPv6Address OBJECT-TYPE
                SYNTAX     Ipv6Address
                MAX-ACCESS read-only
                STATUS     current
                DESCRIPTION
                "Current Device Separate Management IPv6 address
                Device Allocation: SM"
                ::= { cambiumLinkStatus 40 }

cambiumLinkLocalManagementIFIPv6Address OBJECT-TYPE
                SYNTAX     Ipv6Address
                MAX-ACCESS read-only
                STATUS     current
                DESCRIPTION
                "Current Device Separate Management Link Local IPv6 address
                Device Allocation: SM"
                ::= { cambiumLinkStatus 41 }

cambiumEffectiveDeviceIPv6DefaultGateWay OBJECT-TYPE
                SYNTAX     Ipv6Address
                MAX-ACCESS read-only
                STATUS     current
                DESCRIPTION
                "Effective Device Gateway IPv6 Address,
                NOTE: This parameters lists only the first gateway IPv6
                for Bridge and NAT/Router modes.
                Device Allocation: AP, SM"
                ::= { cambiumLinkStatus 42 }

cambiumManagementIFIPv6Gateway OBJECT-TYPE
                SYNTAX     Ipv6Address
                MAX-ACCESS read-only
                STATUS     current
                DESCRIPTION
                "Current Device Separate Management IPv6 Gateway
                Device Allocation: SM"
                ::= { cambiumLinkStatus 43 }

cambiumIPAliasEntry OBJECT-TYPE
	SYNTAX	   CambiumIPAliasEntry
	MAX-ACCESS not-accessible
	STATUS	   current
	DESCRIPTION
		"IP aliases list table entry.
		Device Allocation: AP, SM."
	INDEX	{ cambiumIPAliasTableIndex }
	::= { cambiumIPAliasTable 1 }

CambiumIPAliasEntry ::= SEQUENCE {
	cambiumIPAliasTableIndex
		Integer32,
	cambiumIPAliasIP
		IpAddress,
	cambiumIPAliasNetmask
		IpAddress
}

cambiumIPAliasTableIndex  OBJECT-TYPE
	SYNTAX	  Integer32 (0..10)
	MAX-ACCESS read-only
	STATUS	   current
	DESCRIPTION
		"IP aliases table index."
		::= { cambiumIPAliasEntry 1 }

cambiumIPAliasIP  OBJECT-TYPE
	SYNTAX	   IpAddress
	MAX-ACCESS read-only
	STATUS	   current
	DESCRIPTION
		"IP alias IP address."
	::= { cambiumIPAliasEntry 2 }

cambiumIPAliasNetmask  OBJECT-TYPE
	SYNTAX	   IpAddress
	MAX-ACCESS read-only
	STATUS	   current
	DESCRIPTION
		"IP alias netmask."
	::= { cambiumIPAliasEntry 3 }

cambiumARPEntry OBJECT-TYPE
	SYNTAX	   CambiumARPEntry
	MAX-ACCESS not-accessible
	STATUS	   current
	DESCRIPTION
		"Neighbour device IP/MAC pair entry"
	INDEX	{ cambiumARPIndex }
	::= { cambiumARPTable 1 }

CambiumARPEntry ::= SEQUENCE {
	cambiumARPIndex
		Integer32,
	cambiumARPMAC
		DisplayString,
	cambiumARPIP
		IpAddress,
	cambiumARPInterface
		DisplayString
}

cambiumARPIndex	 OBJECT-TYPE
	SYNTAX	  Integer32 (0..1024)
	MAX-ACCESS read-only
	STATUS	   current
	DESCRIPTION
		"Index"
	::= { cambiumARPEntry 1 }

cambiumARPMAC  OBJECT-TYPE
	SYNTAX	   DisplayString (SIZE(0|17))
	MAX-ACCESS read-only
	STATUS	   current
	DESCRIPTION
		"Neighbour device MAC Address"
	::= { cambiumARPEntry 2 }

cambiumARPIP  OBJECT-TYPE
	SYNTAX	   IpAddress
	MAX-ACCESS read-only
	STATUS	   current
	DESCRIPTION
		"Neighbour device IP Address"
	::= { cambiumARPEntry 3 }

cambiumARPInterface	 OBJECT-TYPE
	SYNTAX	   DisplayString (SIZE(0|16))
	MAX-ACCESS read-only
	STATUS	   current
	DESCRIPTION
		"Neighbour device Interface"
	::= { cambiumARPEntry 4 }

cambiumStaticRoutesEntry OBJECT-TYPE
	SYNTAX	   CambiumStaticRoutesEntry
	MAX-ACCESS not-accessible
	STATUS	   current
	DESCRIPTION
		"Static Routes Dest/Getway pair entry"
	INDEX	{ cambiumStaticRoutesIndex }
	::= { cambiumStaticRoutesTable 1 }

CambiumStaticRoutesEntry ::= SEQUENCE {
	cambiumStaticRoutesIndex
		Integer32,
	cambiumStaticRoutesDestIP
		IpAddress,
	cambiumStaticRoutesGW
		IpAddress,
	cambiumStaticRoutesNetmask
		IpAddress,
	cambiumStaticRoutesInterface
		DisplayString
}

cambiumStaticRoutesIndex  OBJECT-TYPE
	SYNTAX	  Integer32 (0..32)
	MAX-ACCESS read-only
	STATUS	   current
	DESCRIPTION
		"Index"
	::= { cambiumStaticRoutesEntry 1 }

cambiumStaticRoutesDestIP  OBJECT-TYPE
	SYNTAX	   IpAddress
	MAX-ACCESS read-only
	STATUS	   current
	DESCRIPTION
		"Destination IP"
	::= { cambiumStaticRoutesEntry 2 }

cambiumStaticRoutesGW  OBJECT-TYPE
	SYNTAX	   IpAddress
	MAX-ACCESS read-only
	STATUS	   current
	DESCRIPTION
		"Getway IP"
	::= { cambiumStaticRoutesEntry 3 }

cambiumStaticRoutesNetmask	OBJECT-TYPE
	SYNTAX	   IpAddress
	MAX-ACCESS read-only
	STATUS	   current
	DESCRIPTION
		"Dest IP Netmask"
	::= { cambiumStaticRoutesEntry 4 }

cambiumStaticRoutesInterface  OBJECT-TYPE
	SYNTAX	   DisplayString (SIZE(0|16))
	MAX-ACCESS read-only
	STATUS	   current
	DESCRIPTION
		"Static Routes Interface Name"
	::= { cambiumStaticRoutesEntry 5 }

cambiumStatsForceUpdate OBJECT-TYPE
		SYNTAX	   Integer32 (0|1)
		MAX-ACCESS read-write
		STATUS	   current
		DESCRIPTION
		"Cambium Statistics Update/Reset Action
		Statistic is updated automatically in the background each 15sec
		SNMP-GET on This OID forces update of subsequent Statistics tree
		SNMP-SET on This OID Resets all of the subsequent Statistic
		Device Allocation: AP, SM"
		::= { cambiumPerformanceMonitoring 1 }

cambiumEthRXBytes OBJECT-TYPE
		SYNTAX	   Counter64
		MAX-ACCESS read-only
		STATUS	   current
		DESCRIPTION
		"Total Ethernet RX bytes
		Device Allocation: AP, SM"
		::= { cambiumPerformanceMonitoring 2 }

cambiumEthRXPackets OBJECT-TYPE
		SYNTAX	   Counter64
		MAX-ACCESS read-only
		STATUS	   current
		DESCRIPTION
		"Total Ethernet RX packets
		Device Allocation: AP, SM"
		::= { cambiumPerformanceMonitoring 3 }

cambiumEthRXErrors OBJECT-TYPE
		SYNTAX	   Counter64
		MAX-ACCESS read-only
		STATUS	   current
		DESCRIPTION
		"Total Ethernet RX errors
		Device Allocation: AP, SM"
		::= { cambiumPerformanceMonitoring 4 }

cambiumEthRXDrops OBJECT-TYPE
		SYNTAX	   Counter64
		MAX-ACCESS read-only
		STATUS	   current
		DESCRIPTION
		"Total Ethernet RX drops
		Device Allocation: AP, SM"
		::= { cambiumPerformanceMonitoring 5 }

cambiumEthRXMulticast OBJECT-TYPE
		SYNTAX	   Counter64
		MAX-ACCESS read-only
		STATUS	   current
		DESCRIPTION
		"Total Ethernet RX multicast
		Device Allocation: AP, SM"
		::= { cambiumPerformanceMonitoring 6 }

cambiumEthRXBroadcast OBJECT-TYPE
		SYNTAX	   Counter64
		MAX-ACCESS read-only
		STATUS	   current
		DESCRIPTION
		"Total Ethernet RX broadcast
		Device Allocation: AP, SM"
		::= { cambiumPerformanceMonitoring 7 }

cambiumEthTXBytes OBJECT-TYPE
		SYNTAX	   Counter64
		MAX-ACCESS read-only
		STATUS	   current
		DESCRIPTION
		"Total Ethernet TX bytes
		Device Allocation: AP, SM"
		::= { cambiumPerformanceMonitoring 8 }

cambiumEthTXPackets OBJECT-TYPE
		SYNTAX	   Counter64
		MAX-ACCESS read-only
		STATUS	   current
		DESCRIPTION
		"Total Ethernet TX packets
		Device Allocation: AP, SM"
		::= { cambiumPerformanceMonitoring 9 }

cambiumEthTXErrors OBJECT-TYPE
		SYNTAX	   Counter64
		MAX-ACCESS read-only
		STATUS	   current
		DESCRIPTION
		"Total Ethernet TX errors
		Device Allocation: AP, SM"
		::= { cambiumPerformanceMonitoring 10 }

cambiumEthTXDrops OBJECT-TYPE
		SYNTAX	   Counter64
		MAX-ACCESS read-only
		STATUS	   current
		DESCRIPTION
		"Total Ethernet TX drops
		Device Allocation: AP, SM"
		::= { cambiumPerformanceMonitoring 11 }

cambiumEthTXMulticast OBJECT-TYPE
		SYNTAX	   Counter64
		MAX-ACCESS read-only
		STATUS	   current
		DESCRIPTION
		"Total Ethernet TX multicast
		Device Allocation: AP, SM"
		::= { cambiumPerformanceMonitoring 12 }
		
cambiumEthTXBroadcast OBJECT-TYPE
		SYNTAX	   Counter64
		MAX-ACCESS read-only
		STATUS	   current
		DESCRIPTION
		"Total Ethernet TX broadcast
		Device Allocation: AP, SM"
		::= { cambiumPerformanceMonitoring 13 }

cambiumAthRXBytes OBJECT-TYPE
		SYNTAX	   Counter64
		MAX-ACCESS read-only
		STATUS	   obsolete
		DESCRIPTION
		"Total Wireless RX bytes
		Device Allocation: AP, SM"
		::= { cambiumPerformanceMonitoring 21 }

cambiumAthRXPackets OBJECT-TYPE
		SYNTAX	   Counter64
		MAX-ACCESS read-only
		STATUS	   obsolete
		DESCRIPTION
		"Total Wireless RX packets
		Device Allocation: AP, SM"
		::= { cambiumPerformanceMonitoring 22 }

cambiumAthRXErrors OBJECT-TYPE
		SYNTAX	   Counter64
		MAX-ACCESS read-only
		STATUS	   obsolete
		DESCRIPTION
		"Total Wireless RX errors
		Device Allocation: AP, SM"
		::= { cambiumPerformanceMonitoring 23 }

cambiumAthRXDrops OBJECT-TYPE
		SYNTAX	   Counter64
		MAX-ACCESS read-only
		STATUS	   obsolete
		DESCRIPTION
		"Total Wireless RX drops
		Device Allocation: AP, SM"
		::= { cambiumPerformanceMonitoring 24 }

cambiumAthRXMulticast OBJECT-TYPE
		SYNTAX	   Counter64
		MAX-ACCESS read-only
		STATUS	   obsolete
		DESCRIPTION
		"Total Wireless RX multicast
		Device Allocation: AP, SM"
		::= { cambiumPerformanceMonitoring 25 }

cambiumAthRXBroadcast OBJECT-TYPE
		SYNTAX	   Counter64
		MAX-ACCESS read-only
		STATUS	   obsolete
		DESCRIPTION
		"Total Wireless RX broadcast
		Device Allocation: AP, SM"
		::= { cambiumPerformanceMonitoring 26 }

cambiumAthTXBytes OBJECT-TYPE
		SYNTAX	   Counter64
		MAX-ACCESS read-only
		STATUS	   obsolete
		DESCRIPTION
		"Total Wireless TX bytes
		Device Allocation: AP, SM"
		::= { cambiumPerformanceMonitoring 27 }

cambiumAthTXPackets OBJECT-TYPE
		SYNTAX	   Counter64
		MAX-ACCESS read-only
		STATUS	   obsolete
		DESCRIPTION
		"Total Wireless TX packets
		Device Allocation: AP, SM"
		::= { cambiumPerformanceMonitoring 28 }

cambiumAthTXErrors OBJECT-TYPE
		SYNTAX	   Counter64
		MAX-ACCESS read-only
		STATUS	   obsolete
		DESCRIPTION
		"Total Wireless TX errors
		Device Allocation: AP, SM"
		::= { cambiumPerformanceMonitoring 29 }

cambiumAthTXDrops OBJECT-TYPE
		SYNTAX	   Counter64
		MAX-ACCESS read-only
		STATUS	   obsolete
		DESCRIPTION
		"Total Wireless TX drops
		Device Allocation: AP, SM"
		::= { cambiumPerformanceMonitoring 30 }

cambiumAthTXMulticast OBJECT-TYPE
		SYNTAX	   Counter64
		MAX-ACCESS read-only
		STATUS	   obsolete
		DESCRIPTION
		"Total Wireless TX multicast
		Device Allocation: AP, SM"
		::= { cambiumPerformanceMonitoring 31 }

cambiumAthTXBroadcast OBJECT-TYPE
		SYNTAX	   Counter64
		MAX-ACCESS read-only
		STATUS	   obsolete
		DESCRIPTION
		"Total Wireless TX broadcast
		Device Allocation: AP, SM"
		::= { cambiumPerformanceMonitoring 32 }

sysNetworkEntryAttempt OBJECT-TYPE
		SYNTAX	   Counter32
		MAX-ACCESS read-only
		STATUS	   current
		DESCRIPTION
				"Number of attempt to enter the AP network
				Device Allocation: AP"
		::= { cambiumPerformanceMonitoring 33 }

sysNetworkEntrySuccess OBJECT-TYPE
		SYNTAX	   Counter32
		MAX-ACCESS read-only
		STATUS	   current
		DESCRIPTION
				"Number of successful network entry into the AP
				Device Allocation: AP"
		::= { cambiumPerformanceMonitoring 34 }

sysNetworkEntryAuthenticationFailure OBJECT-TYPE
		SYNTAX	   Counter32
		MAX-ACCESS read-only
		STATUS	   current
		DESCRIPTION
				"Number of failed network entry into the AP due to
				authentication failure
				Device Allocation: AP"
		::= { cambiumPerformanceMonitoring 35 }

sysDFSDetectedCount OBJECT-TYPE
		SYNTAX	   Counter32
		MAX-ACCESS read-only
		STATUS	   current
		DESCRIPTION
				"Number of DFS detected during channel initialization or during
				service which causes channel remap
				Device Allocation: AP, SM"
		::= { cambiumPerformanceMonitoring 36 }

ulWLanKbitCount OBJECT-TYPE
		SYNTAX	   Counter64
		MAX-ACCESS read-only
		STATUS	   current
		DESCRIPTION
				"Aggregated total Uplink data traffic in kilobits
				Device Allocation: AP, SM"
		::= { cambiumPerformanceMonitoring 37 }

dlWLanKbitCount OBJECT-TYPE
		SYNTAX	   Counter64
		MAX-ACCESS read-only
		STATUS	   current
		DESCRIPTION
				"Aggregated total Downlink data traffic in kilobits
				Device Allocation: AP, SM"
		::= { cambiumPerformanceMonitoring 38 }

ulWLanTotalPacketCount OBJECT-TYPE
		SYNTAX	   Counter64
		MAX-ACCESS read-only
		STATUS	   current
		DESCRIPTION
				"Aggregated number of total Uplink data packet transmitted by
				SM or received by AP
				Device Allocation: AP, SM"
		::= { cambiumPerformanceMonitoring 39 }

sysRebootCount OBJECT-TYPE
		SYNTAX	   Integer32
		MAX-ACCESS read-only
		STATUS	   obsolete
		DESCRIPTION
				"Device Reboot Counter
				Device Allocation: AP, SM"
		::= { cambiumPerformanceMonitoring 41 }

dlWLanTotalPacketCount OBJECT-TYPE
		SYNTAX	   Counter64
		MAX-ACCESS read-only
		STATUS	   current
		DESCRIPTION
				"Aggregated number of total Downlink data packet transmitted by
				AP or received by SM
				Device Allocation: AP, SM"
		::= { cambiumPerformanceMonitoring 42 }

ulWLanMultiBroadcastKbitCount OBJECT-TYPE
		SYNTAX	   Counter64
		MAX-ACCESS read-only
		STATUS	   current
		DESCRIPTION
				"Aggregated total Uplink multicast and broadcast data traffic in
				kilobits
				Device Allocation: AP, SM"
		::= { cambiumPerformanceMonitoring 43 }

dlWLanMultiBroadcastKbitCount OBJECT-TYPE
		SYNTAX	   Counter64
		MAX-ACCESS read-only
		STATUS	   current
		DESCRIPTION
				"Aggregated total Downlink multicast and broadcast data traffic
				in kilobits
				Device Allocation: AP, SM"
		::= { cambiumPerformanceMonitoring 44 }

wLanSessionDroppedCount OBJECT-TYPE
		SYNTAX	   Counter32
		MAX-ACCESS read-only
		STATUS	   current
		DESCRIPTION
				"Aggregated number of SM session dropped due to no responses of
				bandwidth request response
				Device Allocation: AP, SM"
		::= { cambiumPerformanceMonitoring 45 }

cambiumTDDStatsPerSTATable OBJECT-TYPE
	SYNTAX	   SEQUENCE OF CambiumTDDStatsPerSTAEntry
	MAX-ACCESS not-accessible
	STATUS	   current
	DESCRIPTION
		   "This table contains information relevant to customer TDD Statistics
		   for connected SMs:
		   - station MAC Address,
		   - uplink data traffic in Kbits for a single SM;
		   - downlink data traffic in Kbits for a single SM;
		   - number of uplink total data packet received at AP for a single SM;
		   - number of downlink total data packet transmitted at AP for a single
			 SM;
		   - number of uplink data packet dropped due to data integrity error or
			 other RF related packer errors for a single SM;
		   - number of downlink data packet dropped due to no-acknowledgement or
			 other RF related packet error for a single SM;
		   - number of downlink data packet dropped due to data buffer/queue
			 overflow or other system internal buffer/sending related packet
			 error for a single SM;
		   - number of downlink data packet retransmitted due to no-acknowledge
			 for a single SM.
		   Device Allocation: AP"
	::= { cambiumPerformanceMonitoring 46 }

cambiumTDDStatsPerSTAEntry OBJECT-TYPE
	SYNTAX	   CambiumTDDStatsPerSTAEntry
	MAX-ACCESS not-accessible
	STATUS	   current
	DESCRIPTION
		   "Customer TDD Statistics for particular SM
		   Device Allocation: AP"
	INDEX	{ cambiumTDDStatsPerSTAIndex }
	::= { cambiumTDDStatsPerSTATable 1 }

CambiumTDDStatsPerSTAEntry ::= SEQUENCE {
		cambiumTDDStatsPerSTAIndex				Integer32,
		cambiumTDDStatsListMAC					DisplayString,
		ulWLanPerUserKbitCount					Counter64,
		dlWLanPerUserKbitCount					Counter64,
		ulWLanPerUserTotalPacketCount			Counter64,
		dlWLanPerUserTotalPacketCount			Counter64,
		ulWLanPerUserErrorDroppedPacketCount	Counter64,
		dlWLanPerUserErrorDroppedPacketCount	Counter64,
		dlWLanPerUserCapacityDroppedPacketCount Counter64,
		dlWLanPerUserRetransmitPacketCount		Counter64,
		dlWLanPerUserTxPower					Integer32
	}

cambiumTDDStatsPerSTAIndex OBJECT-TYPE
	SYNTAX	   Integer32 (0..120)
	MAX-ACCESS read-only
	STATUS	   current
	DESCRIPTION
		   "Table index"
	::= { cambiumTDDStatsPerSTAEntry 1 }

cambiumTDDStatsListMAC OBJECT-TYPE
	SYNTAX	   DisplayString (SIZE(0|11..17))
	MAX-ACCESS read-only
	STATUS	   current
	DESCRIPTION
		   "Connected SM WLAN MAC Address
		   Device Allocation: AP"
	::= { cambiumTDDStatsPerSTAEntry 2 }
	
ulWLanPerUserKbitCount OBJECT-TYPE
	SYNTAX	   Counter64
	MAX-ACCESS read-only
	STATUS	   current
	DESCRIPTION
		   "Uplink data traffic in Kbits for a single SM
		   Device Allocation: AP"
	::= { cambiumTDDStatsPerSTAEntry 3 }

dlWLanPerUserKbitCount OBJECT-TYPE
	SYNTAX	   Counter64
	MAX-ACCESS read-only
	STATUS	   current
	DESCRIPTION
		   "Downlink data traffic in Kbits for a single SM
		   Device Allocation: AP"
	::= { cambiumTDDStatsPerSTAEntry 4 }

ulWLanPerUserTotalPacketCount OBJECT-TYPE
	SYNTAX	   Counter64
	MAX-ACCESS read-only
	STATUS	   current
	DESCRIPTION
		   "Number of uplink total data packet received at AP for a single SM
		   Device Allocation: AP"
	::= { cambiumTDDStatsPerSTAEntry 5 }

dlWLanPerUserTotalPacketCount OBJECT-TYPE
	SYNTAX	   Counter64
	MAX-ACCESS read-only
	STATUS	   current
	DESCRIPTION
		   "Number of downlink total data packet transmitted at AP for a single
		  SM 
		   Device Allocation: AP"
	::= { cambiumTDDStatsPerSTAEntry 6 }

ulWLanPerUserErrorDroppedPacketCount OBJECT-TYPE
	SYNTAX	   Counter64
	MAX-ACCESS read-only
	STATUS	   current
	DESCRIPTION
		   "Number of uplink data packet dropped due to data integrity error or
		   other RF related packer errors for a single SM
		   Device Allocation: AP"
	::= { cambiumTDDStatsPerSTAEntry 7 }

dlWLanPerUserErrorDroppedPacketCount OBJECT-TYPE
	SYNTAX	   Counter64
	MAX-ACCESS read-only
	STATUS	   current
	DESCRIPTION
		   "Number of downlink data packet dropped due to no-acknowledgement or
		   other RF related packet error for a single SM
		   Device Allocation: AP"
	::= { cambiumTDDStatsPerSTAEntry 8 }

dlWLanPerUserCapacityDroppedPacketCount OBJECT-TYPE
	SYNTAX	   Counter64
	MAX-ACCESS read-only
	STATUS	   current
	DESCRIPTION
		   "Number of downlink data packet dropped due to data buffer/queue
		   overflow or other system internal buffer/sending related packet error
		   for a single SM
		   Device Allocation: AP"
	::= { cambiumTDDStatsPerSTAEntry 9 }

dlWLanPerUserRetransmitPacketCount OBJECT-TYPE
	SYNTAX	   Counter64
	MAX-ACCESS read-only
	STATUS	   current
	DESCRIPTION
		   "Number of downlink data packet retransmitted due to no-acknowledge
		   for a single SM
		   Device Allocation: AP"
	::= { cambiumTDDStatsPerSTAEntry 10 }

dlWLanPerUserTxPower OBJECT-TYPE
	SYNTAX	   Integer32
	MAX-ACCESS read-only
	STATUS	   current
	DESCRIPTION
		   "Downlink TxPower of data packages for a single SM
		   Device Allocation: AP"
	::= { cambiumTDDStatsPerSTAEntry 11 }

ulWLanErrorDroppedPacketCount OBJECT-TYPE
		SYNTAX	   Counter64
		MAX-ACCESS read-only
		STATUS	   current
		DESCRIPTION
				"Aggregated number of total Uplink data packet dropped due to
				data integrity error or other data packet association or RF
				error in packet
				Device Allocation: AP, SM"
		::= { cambiumPerformanceMonitoring 47 }

dlWLanErrorDroppedPacketCount OBJECT-TYPE
		SYNTAX	   Counter64
		MAX-ACCESS read-only
		STATUS	   current
		DESCRIPTION
				"Aggregated number of total Downlink data packet dropped due to
				data integrity error or other data packet association error in
				packet
				Device Allocation: AP, SM"
		::= { cambiumPerformanceMonitoring 48 }

ulWLanCapacityDroppedPacketCount OBJECT-TYPE
		SYNTAX	   Counter64
		MAX-ACCESS read-only
		STATUS	   current
		DESCRIPTION
				"Aggregated number of total Uplink data packet dropped due to
				WLAN capacity issue in packets
				Device Allocation: AP, SM"
		::= { cambiumPerformanceMonitoring 49 }

dlWLanCapacityDroppedPacketCount OBJECT-TYPE
		SYNTAX	   Counter64
		MAX-ACCESS read-only
		STATUS	   current
		DESCRIPTION
				"Aggregated number of total Downlink data packet dropped due to
				exceed data buffer, over capacity or internal packet package
				sent issues in packet
				Device Allocation: AP, SM"
		::= { cambiumPerformanceMonitoring 50 }

ulWLanTotalAvailableFrameTimePerSecond OBJECT-TYPE
		SYNTAX	   Integer32
		MAX-ACCESS read-only
		STATUS	   current
		DESCRIPTION
				"Aggregated number of total uplink available frame time can be
				scheduled for traffic in micro second for 1 second period
				Device Allocation: AP"
		::= { cambiumPerformanceMonitoring 51 }

dlWLanTotalAvailableFrameTimePerSecond OBJECT-TYPE
		SYNTAX	   Integer32
		MAX-ACCESS read-only
		STATUS	   current
		DESCRIPTION
				"Aggregated number of total downlink available frame time can be
				scheduled for traffic in micro second for 1 second period
				Device Allocation: AP"
		::= { cambiumPerformanceMonitoring 52 }

ulWLanTotalUsedFrameTimePerSecond OBJECT-TYPE
		SYNTAX	   Integer32
		MAX-ACCESS read-only
		STATUS	   current
		DESCRIPTION
				"Aggregated number of uplink frame time schedule to be used in
				microsecond for 1 second period
				Device Allocation: AP"
		::= { cambiumPerformanceMonitoring 53 }

dlWLanTotalUsedFrameTimePerSecond OBJECT-TYPE
		SYNTAX	   Integer32
		MAX-ACCESS read-only
		STATUS	   current
		DESCRIPTION
				"Aggregated number of downlink frame time scheduled to be used
				per frame for 1 second period
				Device Allocation: AP"
		::= { cambiumPerformanceMonitoring 54 }

ulWLanTotalOverheadFrameTimePerSecond OBJECT-TYPE
		SYNTAX	   Integer32
		MAX-ACCESS read-only
		STATUS	   current
		DESCRIPTION
				"Aggregated number of uplink frame time is used for overhead
				(preamble and inter-frame gap) in microsecond for 1 second
				period
				Device Allocation: AP"
		::= { cambiumPerformanceMonitoring 55 }

dlWLanTotalOverheadFrameTimePerSecond OBJECT-TYPE
		SYNTAX	   Integer32
		MAX-ACCESS read-only
		STATUS	   current
		DESCRIPTION
				"Aggregated number of downlink frame time is used for overhead
				(preamble ans inter-frame gap) per frame for 1 second period
				Device Allocation: AP"
		::= { cambiumPerformanceMonitoring 56 }

cambiumMCSTable OBJECT-TYPE
	SYNTAX	   SEQUENCE OF CambiumMCSEntry
	MAX-ACCESS not-accessible
	STATUS	   obsolete
	DESCRIPTION
		   "This table contains information relevant to customer TDD Statistics
		   for MCS RX and TX rates:
		   - MCS number (MCSxx);
		   - Aggregated number of uplink frame time used for MCSxx in
			 microsecond for 1 second period;
		   - Aggregated number of downlink frame time used for MCSxx in
			 microsecond for 1 second period.
		   Device Allocation: AP"
	::= { cambiumPerformanceMonitoring 57 }

cambiumMCSEntry OBJECT-TYPE
	SYNTAX	   CambiumMCSEntry
	MAX-ACCESS not-accessible
	STATUS	   obsolete
	DESCRIPTION
		   "MCS table
		   Device Allocation: AP"
	INDEX	{ cambiumMCSIndex }
	::= { cambiumMCSTable 1 }

CambiumMCSEntry ::= SEQUENCE {
		cambiumMCSIndex					Integer32,
		cambiumMCSNumber				DisplayString,
		ulWLanMCSUsedFrameTimePerSecond Counter32,
		dlWLanMCSUsedFrameTimePerSecond Counter32
	}

cambiumMCSIndex OBJECT-TYPE
	SYNTAX	   Integer32 (0..24)
	MAX-ACCESS read-only
	STATUS	   obsolete
	DESCRIPTION
		   "MCS index
		   Device Allocation: AP"
	::= { cambiumMCSEntry 1 }

cambiumMCSNumber OBJECT-TYPE
	SYNTAX	   DisplayString
	MAX-ACCESS read-only
	STATUS	   obsolete
	DESCRIPTION
		   "MCS number (MCSxx)
		   Device Allocation: AP"
	::= { cambiumMCSEntry 2 }

ulWLanMCSUsedFrameTimePerSecond OBJECT-TYPE
	SYNTAX	   Counter32
	MAX-ACCESS read-only
	STATUS	   obsolete
	DESCRIPTION
		   "Aggregated number of uplink frame time used for MCSxx in
			microsecond for 1 second period
		   Device Allocation: AP"
	::= { cambiumMCSEntry 3 }

dlWLanMCSUsedFrameTimePerSecond OBJECT-TYPE
	SYNTAX	   Counter32
	MAX-ACCESS read-only
	STATUS	   obsolete
	DESCRIPTION
		   "Aggregated number of downlink frame time used for MCSxx in
			microsecond for 1 second period
		   Device Allocation: AP"
	::= { cambiumMCSEntry 4 }

ulWLanRetransPacketCount OBJECT-TYPE
		SYNTAX	   Counter64
		MAX-ACCESS read-only
		STATUS	   current
		DESCRIPTION
				"Aggregated number of total Uplink data packet retransmitted due
				to no-acknowledgement.
				Device Allocation: SM"
		::= { cambiumPerformanceMonitoring 58 }

dlWLanRetransPacketCount OBJECT-TYPE
		SYNTAX	   Counter64
		MAX-ACCESS read-only
		STATUS	   current
		DESCRIPTION
				"Aggregated number of total Downlink data packet retransmitted
				due to no-acknowledgement
				Device Allocation: AP"
		::= { cambiumPerformanceMonitoring 59 }

ulWLanBroadcastPacketCount OBJECT-TYPE
		SYNTAX	   Counter32
		MAX-ACCESS read-only
		STATUS	   current
		DESCRIPTION
				"Aggregated total Uplink broadcast packet counter
				Device Allocation: AP, SM"
		::= { cambiumPerformanceMonitoring 60 }

dlWLanBroadcastPacketCount OBJECT-TYPE
		SYNTAX	   Counter32
		MAX-ACCESS read-only
		STATUS	   current
		DESCRIPTION
				"Aggregated total Downlink broadcast packet counter
				Device Allocation: AP, SM"
		::= { cambiumPerformanceMonitoring 61 }

ulWLanMulticastPacketCount OBJECT-TYPE
		SYNTAX	   Counter32
		MAX-ACCESS read-only
		STATUS	   current
		DESCRIPTION
				"Aggregated total Uplink multicast packet counter
				Device Allocation: AP, SM"
		::= { cambiumPerformanceMonitoring 62 }

dlWLanMulticastPacketCount OBJECT-TYPE
		SYNTAX	   Counter32
		MAX-ACCESS read-only
		STATUS	   current
		DESCRIPTION
				"Aggregated total Downlink multicast packet counter
				Device Allocation: AP, SM"
		::= { cambiumPerformanceMonitoring 63 }

sysCPUUsage OBJECT-TYPE
		SYNTAX	   Counter32
		MAX-ACCESS read-only
		STATUS	   current
		DESCRIPTION
				"CPU Usage, measuring up to 0.1%
				Range: 0..1000
				Device Allocation: AP, SM"
		::= { cambiumPerformanceMonitoring 64 }

rxEtherLanKbitCount OBJECT-TYPE
		SYNTAX	   Counter64
		MAX-ACCESS read-only
		STATUS	   current
		DESCRIPTION
		"Total Ethernet RX bytes
		Device Allocation: AP, SM"
		::= { cambiumPerformanceMonitoring 65 }

rxEtherLanTotalPacketCount OBJECT-TYPE
		SYNTAX	   Counter64
		MAX-ACCESS read-only
		STATUS	   current
		DESCRIPTION
		"Total Ethernet RX packets
		Device Allocation: AP, SM"
		::= { cambiumPerformanceMonitoring 66 }

rxEtherLanErrorPacketCount OBJECT-TYPE
		SYNTAX	   Counter64
		MAX-ACCESS read-only
		STATUS	   current
		DESCRIPTION
		"Total Ethernet RX errors
		Device Allocation: AP, SM"
		::= { cambiumPerformanceMonitoring 67 }

rxEtherLanDroppedPacketCount OBJECT-TYPE
		SYNTAX	   Counter64
		MAX-ACCESS read-only
		STATUS	   current
		DESCRIPTION
		"Total Ethernet RX drops
		Device Allocation: AP, SM"
		::= { cambiumPerformanceMonitoring 68 }

rxEtherLanMulticastPacketCount OBJECT-TYPE
		SYNTAX	   Counter64
		MAX-ACCESS read-only
		STATUS	   current
		DESCRIPTION
		"Total Ethernet RX multicast
		Device Allocation: AP, SM"
		::= { cambiumPerformanceMonitoring 69 }

rxEtherLanBroadcastPacketCount OBJECT-TYPE
		SYNTAX	   Counter64
		MAX-ACCESS read-only
		STATUS	   current
		DESCRIPTION
		"Total Ethernet RX broadcast
		Device Allocation: AP, SM"
		::= { cambiumPerformanceMonitoring 70 }

rxEtherLanMultiBroadcastKbitCount OBJECT-TYPE
		SYNTAX	   Counter64
		MAX-ACCESS read-only
		STATUS	   current
		DESCRIPTION
		"Aggregated total Ethernet RX multicast and broadcast data traffic 
		Device Allocation: AP, SM"
		::= { cambiumPerformanceMonitoring 71 }

txEtherLanKbitCount OBJECT-TYPE
		SYNTAX	   Counter64
		MAX-ACCESS read-only
		STATUS	   current
		DESCRIPTION
		"Total Ethernet TX bytes
		Device Allocation: AP, SM"
		::= { cambiumPerformanceMonitoring 72 }

txEtherLanTotalPacketCount OBJECT-TYPE
		SYNTAX	   Counter64
		MAX-ACCESS read-only
		STATUS	   current
		DESCRIPTION
		"Total Ethernet TX packets
		Device Allocation: AP, SM"
		::= { cambiumPerformanceMonitoring 73 }

txEtherLanErrorPacketCount OBJECT-TYPE
		SYNTAX	   Counter64
		MAX-ACCESS read-only
		STATUS	   current
		DESCRIPTION
		"Total Ethernet TX errors
		Device Allocation: AP, SM"
		::= { cambiumPerformanceMonitoring 74 }

txEtherLanDroppedPacketCount OBJECT-TYPE
		SYNTAX	   Counter64
		MAX-ACCESS read-only
		STATUS	   current
		DESCRIPTION
		"Total Ethernet TX drops
		Device Allocation: AP, SM"
		::= { cambiumPerformanceMonitoring 75 }

txEtherLanMulticastPacketCount OBJECT-TYPE
		SYNTAX	   Counter64
		MAX-ACCESS read-only
		STATUS	   current
		DESCRIPTION
		"Total Ethernet TX multicast
		Device Allocation: AP, SM"
		::= { cambiumPerformanceMonitoring 76 }
		
txEtherLanBroadcastPacketCount OBJECT-TYPE
		SYNTAX	   Counter64
		MAX-ACCESS read-only
		STATUS	   current
		DESCRIPTION
		"Total Ethernet TX broadcast
		Device Allocation: AP, SM"
		::= { cambiumPerformanceMonitoring 77 }

txEtherLanMultiBroadcastKbitCount OBJECT-TYPE
		SYNTAX	   Counter64
		MAX-ACCESS read-only
		STATUS	   current
		DESCRIPTION
		"Aggregated total Ethernet TX multicast and broadcast data traffic
		Device Allocation: AP, SM"
		::= { cambiumPerformanceMonitoring 78 }

cambiumStatsResetTimer OBJECT-TYPE
		SYNTAX	   TimeTicks
		MAX-ACCESS read-only
		STATUS	   current
		DESCRIPTION
				"Status time to indicate when is the last time stats are reset
				Device Allocation: AP, SM"
		::= { cambiumPerformanceMonitoring 79 }

ulWLanMCS00Packets OBJECT-TYPE
		SYNTAX	   Counter64
		MAX-ACCESS read-only
		STATUS	   current
		DESCRIPTION
				"Aggregated number of uplink packet received for MCS00
				Device Allocation: AP"
		::= { cambiumPerformanceMonitoring 80 }

ulWLanMCS01Packets OBJECT-TYPE
		SYNTAX	   Counter64
		MAX-ACCESS read-only
		STATUS	   current
		DESCRIPTION
				"Aggregated number of uplink packet received for MCS01
				Device Allocation: AP"
		::= { cambiumPerformanceMonitoring 81 }

ulWLanMCS02Packets OBJECT-TYPE
		SYNTAX	   Counter64
		MAX-ACCESS read-only
		STATUS	   current
		DESCRIPTION
				"Aggregated number of uplink packet received for MCS02
				Device Allocation: AP"
		::= { cambiumPerformanceMonitoring 82 }

ulWLanMCS03Packets OBJECT-TYPE
		SYNTAX	   Counter64
		MAX-ACCESS read-only
		STATUS	   current
		DESCRIPTION
				"Aggregated number of uplink packet received for MCS03
				Device Allocation: AP"
		::= { cambiumPerformanceMonitoring 83 }

ulWLanMCS04Packets OBJECT-TYPE
		SYNTAX	   Counter64
		MAX-ACCESS read-only
		STATUS	   current
		DESCRIPTION
				"Aggregated number of uplink packet received for MCS04
				Device Allocation: AP"
		::= { cambiumPerformanceMonitoring 84 }

ulWLanMCS05Packets OBJECT-TYPE
		SYNTAX	   Counter64
		MAX-ACCESS read-only
		STATUS	   current
		DESCRIPTION
				"Aggregated number of uplink packet received for MCS05
				Device Allocation: AP"
		::= { cambiumPerformanceMonitoring 85 }

ulWLanMCS06Packets OBJECT-TYPE
		SYNTAX	   Counter64
		MAX-ACCESS read-only
		STATUS	   current
		DESCRIPTION
				"Aggregated number of uplink packet received for MCS06
				Device Allocation: AP"
		::= { cambiumPerformanceMonitoring 86 }

ulWLanMCS07Packets OBJECT-TYPE
		SYNTAX	   Counter64
		MAX-ACCESS read-only
		STATUS	   current
		DESCRIPTION
				"Aggregated number of uplink packet received for MCS07
				Device Allocation: AP"
		::= { cambiumPerformanceMonitoring 87 }

ulWLanMCS08Packets OBJECT-TYPE
		SYNTAX	   Counter64
		MAX-ACCESS read-only
		STATUS	   current
		DESCRIPTION
				"Aggregated number of uplink packet received for MCS08
				Device Allocation: AP"
		::= { cambiumPerformanceMonitoring 88 }

ulWLanMCS09Packets OBJECT-TYPE
		SYNTAX	   Counter64
		MAX-ACCESS read-only
		STATUS	   current
		DESCRIPTION
				"Aggregated number of uplink packet received for MCS09
				Device Allocation: AP"
		::= { cambiumPerformanceMonitoring 89 }

ulWLanMCS10Packets OBJECT-TYPE
		SYNTAX	   Counter64
		MAX-ACCESS read-only
		STATUS	   current
		DESCRIPTION
				"Aggregated number of uplink packet received for MCS10
				Device Allocation: AP"
		::= { cambiumPerformanceMonitoring 90 }

ulWLanMCS11Packets OBJECT-TYPE
		SYNTAX	   Counter64
		MAX-ACCESS read-only
		STATUS	   current
		DESCRIPTION
				"Aggregated number of uplink packet received for MCS11
				Device Allocation: AP"
		::= { cambiumPerformanceMonitoring 91 }

ulWLanMCS12Packets OBJECT-TYPE
		SYNTAX	   Counter64
		MAX-ACCESS read-only
		STATUS	   current
		DESCRIPTION
				"Aggregated number of uplink packet received for MCS12
				Device Allocation: AP"
		::= { cambiumPerformanceMonitoring 92 }

ulWLanMCS13Packets OBJECT-TYPE
		SYNTAX	   Counter64
		MAX-ACCESS read-only
		STATUS	   current
		DESCRIPTION
				"Aggregated number of uplink packet received for MCS13
				Device Allocation: AP"
		::= { cambiumPerformanceMonitoring 93 }

ulWLanMCS14Packets OBJECT-TYPE
		SYNTAX	   Counter64
		MAX-ACCESS read-only
		STATUS	   current
		DESCRIPTION
				"Aggregated number of uplink packet received for MCS14
				Device Allocation: AP"
		::= { cambiumPerformanceMonitoring 94 }

ulWLanMCS15Packets OBJECT-TYPE
		SYNTAX	   Counter64
		MAX-ACCESS read-only
		STATUS	   current
		DESCRIPTION
				"Aggregated number of uplink packet received for MCS15
				Device Allocation: AP"
		::= { cambiumPerformanceMonitoring 95 }

dlWLanMCS00Packets OBJECT-TYPE
		SYNTAX	   Counter64
		MAX-ACCESS read-only
		STATUS	   current
		DESCRIPTION
				"Aggregated number of downlink packet received for MCS00
				Device Allocation: AP"
		::= { cambiumPerformanceMonitoring 96 }

dlWLanMCS01Packets OBJECT-TYPE
		SYNTAX	   Counter64
		MAX-ACCESS read-only
		STATUS	   current
		DESCRIPTION
				"Aggregated number of downlink packet received for MCS01
				Device Allocation: AP"
		::= { cambiumPerformanceMonitoring 97 }

dlWLanMCS02Packets OBJECT-TYPE
		SYNTAX	   Counter64
		MAX-ACCESS read-only
		STATUS	   current
		DESCRIPTION
				"Aggregated number of downlink packet received for MCS02
				Device Allocation: AP"
		::= { cambiumPerformanceMonitoring 98 }

dlWLanMCS03Packets OBJECT-TYPE
		SYNTAX	   Counter64
		MAX-ACCESS read-only
		STATUS	   current
		DESCRIPTION
				"Aggregated number of downlink packet received for MCS03
				Device Allocation: AP"
		::= { cambiumPerformanceMonitoring 99 }

dlWLanMCS04Packets OBJECT-TYPE
		SYNTAX	   Counter64
		MAX-ACCESS read-only
		STATUS	   current
		DESCRIPTION
				"Aggregated number of downlink packet received for MCS04
				Device Allocation: AP"
		::= { cambiumPerformanceMonitoring 100 }

dlWLanMCS05Packets OBJECT-TYPE
		SYNTAX	   Counter64
		MAX-ACCESS read-only
		STATUS	   current
		DESCRIPTION
				"Aggregated number of downlink packet received for MCS05
				Device Allocation: AP"
		::= { cambiumPerformanceMonitoring 101 }

dlWLanMCS06Packets OBJECT-TYPE
		SYNTAX	   Counter64
		MAX-ACCESS read-only
		STATUS	   current
		DESCRIPTION
				"Aggregated number of downlink packet received for MCS06
				Device Allocation: AP"
		::= { cambiumPerformanceMonitoring 102 }

dlWLanMCS07Packets OBJECT-TYPE
		SYNTAX	   Counter64
		MAX-ACCESS read-only
		STATUS	   current
		DESCRIPTION
				"Aggregated number of downlink packet received for MCS07
				Device Allocation: AP"
		::= { cambiumPerformanceMonitoring 103 }

dlWLanMCS08Packets OBJECT-TYPE
		SYNTAX	   Counter64
		MAX-ACCESS read-only
		STATUS	   current
		DESCRIPTION
				"Aggregated number of downlink packet received for MCS08
				Device Allocation: AP"
		::= { cambiumPerformanceMonitoring 104 }

dlWLanMCS09Packets OBJECT-TYPE
		SYNTAX	   Counter64
		MAX-ACCESS read-only
		STATUS	   current
		DESCRIPTION
				"Aggregated number of downlink packet received for MCS09
				Device Allocation: AP"
		::= { cambiumPerformanceMonitoring 105 }

dlWLanMCS10Packets OBJECT-TYPE
		SYNTAX	   Counter64
		MAX-ACCESS read-only
		STATUS	   current
		DESCRIPTION
				"Aggregated number of downlink packet received for MCS10
				Device Allocation: AP"
		::= { cambiumPerformanceMonitoring 106 }

dlWLanMCS11Packets OBJECT-TYPE
		SYNTAX	   Counter64
		MAX-ACCESS read-only
		STATUS	   current
		DESCRIPTION
				"Aggregated number of downlink packet received for MCS11
				Device Allocation: AP"
		::= { cambiumPerformanceMonitoring 107 }

dlWLanMCS12Packets OBJECT-TYPE
		SYNTAX	   Counter64
		MAX-ACCESS read-only
		STATUS	   current
		DESCRIPTION
				"Aggregated number of downlink packet received for MCS12
				Device Allocation: AP"
		::= { cambiumPerformanceMonitoring 108 }

dlWLanMCS13Packets OBJECT-TYPE
		SYNTAX	   Counter64
		MAX-ACCESS read-only
		STATUS	   current
		DESCRIPTION
				"Aggregated number of downlink packet received for MCS13
				Device Allocation: AP"
		::= { cambiumPerformanceMonitoring 109 }

dlWLanMCS14Packets OBJECT-TYPE
		SYNTAX	   Counter64
		MAX-ACCESS read-only
		STATUS	   current
		DESCRIPTION
				"Aggregated number of downlink packet received for MCS14
				Device Allocation: AP"
		::= { cambiumPerformanceMonitoring 110 }

dlWLanMCS15Packets OBJECT-TYPE
		SYNTAX	   Counter64
		MAX-ACCESS read-only
		STATUS	   current
		DESCRIPTION
				"Aggregated number of downlink packet received for MCS15
				Device Allocation: AP"
		::= { cambiumPerformanceMonitoring 111 }

ulWLanTotalAvailableFrameTimePercentage OBJECT-TYPE
        SYNTAX     Integer32
        MAX-ACCESS read-only
        STATUS     current
        DESCRIPTION
                "Aggregated uplink frame 10X percentage time
                Range = [1..1000] 0.1% = 1; 100% = 1000
                Device Allocation: AP"
        ::= { cambiumPerformanceMonitoring 112 }

dlWLanTotalAvailableFrameTimePercentage OBJECT-TYPE
        SYNTAX     Integer32
        MAX-ACCESS read-only
        STATUS     current
        DESCRIPTION
                "Aggregated downlink frame 10X percentage time
                Range = [1..1000] 0.1% = 1; 100% = 1000
                Device Allocation: AP"
        ::= { cambiumPerformanceMonitoring 113 }
ePMP2000MapMissCounter OBJECT-TYPE
		SYNTAX	   Counter32
		MAX-ACCESS read-only
		STATUS	   current
		DESCRIPTION
				"ePMP2000: Map Miss counter
				Device Allocation: AP"
		::= { cambiumPerformanceMonitoring 115 }

ePMP2000PatternSkipCounter OBJECT-TYPE
		SYNTAX	   Counter32
		MAX-ACCESS read-only
		STATUS	   current
		DESCRIPTION
				"ePMP2000: Pattern skip counter
				Device Allocation: AP"
		::= { cambiumPerformanceMonitoring 116 }

ePMP2000ErrorsSmartAntennaInterface OBJECT-TYPE
		SYNTAX	   Counter32
		MAX-ACCESS read-only
		STATUS	   current
		DESCRIPTION
				"ePMP2000: Number of errors seen on the SmartAntenna interface (handshake errors)
				Device Allocation: AP"
		::= { cambiumPerformanceMonitoring 117 }

classificationVoiceQueuePutPacketCount OBJECT-TYPE
		SYNTAX	   Counter32
		MAX-ACCESS read-only
		STATUS	   current
		DESCRIPTION
				"Total count of put packets to VOICE queue
				Device Allocation: AP, SM"
		::= { cambiumPerformanceMonitoring 118 }

classificationVoiceQueueGetPacketCount OBJECT-TYPE
		SYNTAX	   Counter32
		MAX-ACCESS read-only
		STATUS	   current
		DESCRIPTION
				"Total count of get packets from VOICE queue
				Device Allocation: AP, SM"
		::= { cambiumPerformanceMonitoring 119 }

classificationVoiceQueueDropPacketCount OBJECT-TYPE
		SYNTAX	   Counter32
		MAX-ACCESS read-only
		STATUS	   current
		DESCRIPTION
				"Total count of dropped packets from VOICE queue
				Device Allocation: AP, SM"
		::= { cambiumPerformanceMonitoring 120 }

classificationHighQueuePutPacketCount OBJECT-TYPE
		SYNTAX	   Counter32
		MAX-ACCESS read-only
		STATUS	   current
		DESCRIPTION
				"Total count of put packets to HIGH queue
				Device Allocation: AP, SM"
		::= { cambiumPerformanceMonitoring 121 }

classificationHighQueueGetPacketCount OBJECT-TYPE
		SYNTAX	   Counter32
		MAX-ACCESS read-only
		STATUS	   current
		DESCRIPTION
				"Total count of get packets from HIGH queue
				Device Allocation: AP, SM"
		::= { cambiumPerformanceMonitoring 122 }

classificationHighQueueDropPacketCount OBJECT-TYPE
		SYNTAX	   Counter32
		MAX-ACCESS read-only
		STATUS	   current
		DESCRIPTION
				"Total count of dropped packets from HIGH queue
				Device Allocation: AP, SM"
		::= { cambiumPerformanceMonitoring 123 }

classificationLowQueuePutPacketCount OBJECT-TYPE
		SYNTAX	   Counter32
		MAX-ACCESS read-only
		STATUS	   current
		DESCRIPTION
				"Total count of put packets to LOW queue
				Device Allocation: AP, SM"
		::= { cambiumPerformanceMonitoring 124 }

classificationLowQueueGetPacketCount OBJECT-TYPE
		SYNTAX	   Counter32
		MAX-ACCESS read-only
		STATUS	   current
		DESCRIPTION
				"Total count of get packets from LOW queue
				Device Allocation: AP, SM"
		::= { cambiumPerformanceMonitoring 125 }

classificationLowQueueDropPacketCount OBJECT-TYPE
		SYNTAX	   Counter32
		MAX-ACCESS read-only
		STATUS	   current
		DESCRIPTION
				"Total count of dropped packets from LOW queue
				Device Allocation: AP, SM"
		::= { cambiumPerformanceMonitoring 126 }

classificationTotalQueuePutPacketCount OBJECT-TYPE
		SYNTAX	   Counter32
		MAX-ACCESS read-only
		STATUS	   current
		DESCRIPTION
				"Total count of put packets to all queues
				Device Allocation: AP, SM"
		::= { cambiumPerformanceMonitoring 127 }

classificationTotalQueueGetPacketCount OBJECT-TYPE
		SYNTAX	   Counter32
		MAX-ACCESS read-only
		STATUS	   current
		DESCRIPTION
				"Total count of get packets from all queues
				Device Allocation: AP, SM"
		::= { cambiumPerformanceMonitoring 128 }

classificationTotalQueueDropPacketCount OBJECT-TYPE
		SYNTAX	   Counter32
		MAX-ACCESS read-only
		STATUS	   current
		DESCRIPTION
				"Total count of dropped packets from all queues
				Device Allocation: AP, SM"
		::= { cambiumPerformanceMonitoring 129 }

syslogServerIPFirst	 OBJECT-TYPE
		SYNTAX	   IpAddress
		MAX-ACCESS read-write
		STATUS	   current
		DESCRIPTION
		"Syslog Server IP Address 1
		Device Allocation: AP, SM"
		::= { cambiumSystemLog 1 }

syslogServerIPSecond  OBJECT-TYPE
		SYNTAX	   IpAddress
		MAX-ACCESS read-write
		STATUS	   current
		DESCRIPTION
		"Syslog Server IP Address 2
		Device Allocation: AP, SM"
		::= { cambiumSystemLog 2 }

syslogServerIPThird	 OBJECT-TYPE
		SYNTAX	   IpAddress
		MAX-ACCESS read-write
		STATUS	   current
		DESCRIPTION
		"Syslog Server IP Address 3
		Device Allocation: AP, SM"
		::= { cambiumSystemLog 3 }

syslogServerIPFourth  OBJECT-TYPE
		SYNTAX	   IpAddress
		MAX-ACCESS read-write
		STATUS	   current
		DESCRIPTION
		"Syslog Server IP Address 4
		Device Allocation: AP, SM"
		::= { cambiumSystemLog 4 }

syslogServerLogToWeb  OBJECT-TYPE
		SYNTAX	   Integer32 (0|1)
		MAX-ACCESS read-write
		STATUS	   current
		DESCRIPTION
		"Enable Log to WEB Interface:
			0 - Disable, 
			1 - Enable
		Device Allocation: AP, SM"
		DEFVAL	{ 0 }
		::= { cambiumSystemLog 5 }

syslogServerLogMask	 OBJECT-TYPE
		SYNTAX	   Integer32 (0..255)
		MAX-ACCESS read-write
		STATUS	   current
		DESCRIPTION
		"Log Level Mask:
			0   (0x00) - all messages, 
			1   (0x01) - emerg,
			2   (0x02) - alert, 
			4   (0x04) - crit,
			8   (0x08) - err,
			16  (0x10) - warning,
			32  (0x20) - notice,
			64  (0x40) - info,
			128 (0x80) - debug
		Device Allocation: AP, SM"
		DEFVAL	{ 0 }
		::= { cambiumSystemLog 6 }

dhcpLanEnable  OBJECT-TYPE
		SYNTAX	   Integer32 (0|1)
		MAX-ACCESS read-write
		STATUS	   current
		DESCRIPTION
		"Local DHCP Server Enable:
			0 - Disable
			1 - Enable
		Device Allocation: SM"
		DEFVAL	{ 0 }
		::= { cambiumDHCP 1 }

dhcpLanStart  OBJECT-TYPE
	SYNTAX	   Integer32 (-2147483647..2147483647)
	MAX-ACCESS read-write
	STATUS	   current
	DESCRIPTION 
		"Local DHCP Server IP Start Address
		Offset from the Network address.
		Device Allocation: SM"
	DEFVAL	{ 1 }
	::= { cambiumDHCP 2 }

dhcpLanLimit  OBJECT-TYPE
	SYNTAX	   Integer32 (-2147483647..2147483647)
	MAX-ACCESS read-write
	STATUS	   current
	DESCRIPTION 
		"Local DHCP Server IP End Address
		Offset from the Network address.
		Device Allocation: SM"
	DEFVAL	{ 10 }
	::= { cambiumDHCP 3 }

dhcpLanLeasetime  OBJECT-TYPE
	SYNTAX	   Integer32 (0..24)
	MAX-ACCESS read-write
	STATUS	   current
	DESCRIPTION 
		"Local DHCP Lease Setup in hours
		Valid Range: 1 hour - 24 hours
		Device Allocation: SM"
	DEFVAL	{ 24 }
	::= { cambiumDHCP 4 }
	
dhcpLanHostTable  OBJECT-TYPE
	SYNTAX SEQUENCE OF DhcpLanHostEntry
	MAX-ACCESS not-accessible
	STATUS	   current
	DESCRIPTION 
		"Table for DHCP Hosts
		Device Allocation: SM"
	::= { cambiumDHCP 5 }

dhcpLanHostEntry  OBJECT-TYPE
	SYNTAX	DhcpLanHostEntry
	MAX-ACCESS not-accessible
	STATUS	   current
	DESCRIPTION 
		"DHCP Hosts Table Entry
		Device Allocation: SM"
	INDEX	{ dhcpLanHostIndex }
	::= { dhcpLanHostTable 1 }

DhcpLanHostEntry ::= SEQUENCE {
	dhcpLanHostIndex
		Integer32,
	dhcpLanHostIP
		IpAddress,
	dhcpLanHostMAC
		DisplayString,
	dhcpLanHostName
		DisplayString
}

dhcpLanHostIndex OBJECT-TYPE
		SYNTAX	   Integer32 (0..8)
		MAX-ACCESS read-write
		STATUS	   current
		DESCRIPTION
		"DHCP host Table Index
		Table Entry is cleared if Index is set to zero
		Device Allocation: SM"
		::= { dhcpLanHostEntry 1 }

dhcpLanHostIP  OBJECT-TYPE
	SYNTAX	   IpAddress
	MAX-ACCESS read-write
	STATUS	   current
	DESCRIPTION 
		"DHCP Lan Host IP
		'ignore' or the IP address to be used for DHCP host
		Device Allocation: SM"
	::= { dhcpLanHostEntry 2 }

dhcpLanHostMAC	OBJECT-TYPE
	SYNTAX	   DisplayString (SIZE(0|17))
	MAX-ACCESS read-write
	STATUS	   current
	DESCRIPTION 
		"The hardware address of this host
		Device Allocation: SM"
	::= { dhcpLanHostEntry 3 }

dhcpLanHostName	 OBJECT-TYPE
	SYNTAX	   DisplayString (SIZE(0|1..128))
	MAX-ACCESS read-write
	STATUS	   current
	DESCRIPTION 
		"Optional hostname to assign
		Device Allocation: SM"
	::= { dhcpLanHostEntry 4 }

dhcpOption82  OBJECT-TYPE
		SYNTAX	   Integer32 (0|1)
		MAX-ACCESS read-write
		STATUS	   current
		DESCRIPTION
				"DHCP Option82:
				 0 - Disable
				 1 - Enable
				Device Allocation: AP"
		DEFVAL	{ 0 }
		::= { cambiumDHCP 6 }

cambiumSSHServerEnable	OBJECT-TYPE
		SYNTAX	   Integer32 (0|1)
		MAX-ACCESS read-write
		STATUS	   current
		DESCRIPTION
				"Cambium SSH Server:
						0 - Disable,
						1 - Enable
				Device Allocation: AP, SM"
	DEFVAL	{ 1 }
		::= { cambiumSSHServer 1 }

networkMode	 OBJECT-TYPE
		SYNTAX	   Integer32 (1|2|3)
		MAX-ACCESS read-write
		STATUS	   current
		DESCRIPTION
		"SM Network Mode:
			1 - NAT,
			2 - Bridge,
			3 - Router
		Device Allocation: SM"
		::= { network 1 }

networkSTP OBJECT-TYPE
		SYNTAX	   Integer32 (0|1)
		MAX-ACCESS read-write
		STATUS	   current
		DESCRIPTION
		"Spanning Tree Protocol:
			0 - Disable STP (Default mode)
			1 - Enable STP
		Device Allocation: AP, SM"
		DEFVAL	{ 0 }
		::= { network 6 }

networkLanIPAddressMode	 OBJECT-TYPE
	SYNTAX	   Integer32 (1|2)
	MAX-ACCESS read-write
	STATUS	   current
	DESCRIPTION 
		"SM NAT LAN IP Address Mode
			1 - Static, 
			2 - DHCP
		Device Allocation: AP, SM"
	DEFVAL	{ 1 }
	::= { networkLan 1 }

networkLanIPAddr  OBJECT-TYPE
	SYNTAX	   IpAddress
	MAX-ACCESS read-write
	STATUS	   current
	DESCRIPTION 
		"SM NAT LAN IP Address
		Device Allocation: SM"
	::= { networkLan 2 }

networkLanNetmask  OBJECT-TYPE
	SYNTAX	   IpAddress
	MAX-ACCESS read-write
	STATUS	   current
	DESCRIPTION 
		"SM NAT LAN IP Subnet Mask
		Device Allocation: SM"
	::= { networkLan 3 }

networkLanGatewayIP	 OBJECT-TYPE
	SYNTAX	   IpAddress
	MAX-ACCESS read-write
	STATUS	   current
	DESCRIPTION 
		"SM NAT LAN Gateway IP Address
		Device Allocation: SM"
	::= { networkLan 4 }

networkLanDNSIPAddr	 OBJECT-TYPE
	SYNTAX	   IpAddress
	MAX-ACCESS read-write
	STATUS	   obsolete
	DESCRIPTION
		"SM NAT LAN DNS Server IP Address
		Device Allocation: SM"
	::= { networkLan 5 }

networkLanMTU  OBJECT-TYPE
	SYNTAX	   Integer32 (0|576..1700)
	MAX-ACCESS read-write
	STATUS	   current
	DESCRIPTION
		"SM NAT LAN MTU size
		Device Allocation: SM"
	DEFVAL	{ 1500 }
	::= { networkLan 6 }

networkLanDNSIPAddrPrimary	OBJECT-TYPE
	SYNTAX	   IpAddress
	MAX-ACCESS read-write
	STATUS	   current
	DESCRIPTION 
		"SM NAT LAN DNS Server IP Address
		Device Allocation: SM
		Primary Server IP"
	::= { networkLan 7 }

networkLanDNSIPAddrSecondary  OBJECT-TYPE
	SYNTAX	   IpAddress
	MAX-ACCESS read-write
	STATUS	   current
	DESCRIPTION
		"SM NAT LAN DNS Server IP Address
		Device Allocation: SM
		Secondary Server IP"
	::= { networkLan 8 }

networkLanAutoNegotiation  OBJECT-TYPE
	SYNTAX	   Integer32 (0|1)
	MAX-ACCESS read-write
	STATUS	   current
	DESCRIPTION
		"Lan Autonegotiation 
			0 - Disable,
			1 - Enable
		Device Allocation: AP, SM"
		DEFVAL	{ 1 }
	::= { networkLan 9 }

networkLanSpeed	 OBJECT-TYPE
	SYNTAX	   Integer32 (10|100|1000)
	MAX-ACCESS read-write
	STATUS	   current
	DESCRIPTION
		"LAN Speed 
			10	 - 10 Mb/s,
			100	 - 100 Mb/s,
			1000 - 1000 Mb/s
		Device Allocation: AP, SM"
		DEFVAL	{ 100 }
	::= { networkLan 10 }

networkLanDuplex  OBJECT-TYPE
	SYNTAX	   Integer32 (0|1)
	MAX-ACCESS read-write
	STATUS	   current
	DESCRIPTION
		"LAN Duplex Mode 
			0 - Half,
			1 - Full
		Device Allocation: AP, SM"
		DEFVAL	{ 1 }
	::= { networkLan 11 }
	
networkBroadcastStormEnabled  OBJECT-TYPE
	SYNTAX	   Integer32 (0|1)
	MAX-ACCESS read-write
	STATUS	   current
	DESCRIPTION
		"Broadcast Strom Control 
			0 - Disabled,
			1 - Enabled
		Device Allocation: AP, SM"
		DEFVAL	{ 0 }
	::= { networkLan 12 }
	
networkBroadcastStormRate  OBJECT-TYPE
	SYNTAX	   Integer32 (0..16000)
	MAX-ACCESS read-write
	STATUS	   current
	DESCRIPTION
		"Broadcast Strom Control Rate
			in frames per second
		Device Allocation: AP, SM"
		DEFVAL	{ 0 }
	::= { networkLan 13 }

networkLan2Enabled	OBJECT-TYPE
	SYNTAX	   Integer32 (0|1)
	MAX-ACCESS read-write
	STATUS	   current
	DESCRIPTION
		"AUX Lan Port Enabled 
			0 - Disable,
			1 - Enable
		Device Allocation: AP, SM"
		DEFVAL	{ 1 }
	::= { networkLan 20 }

networkLan2AutoNegotiation	OBJECT-TYPE
	SYNTAX	   Integer32 (0|1)
	MAX-ACCESS read-write
	STATUS	   current
	DESCRIPTION
		"Lan Autonegotiation 
			0 - Disable,
			1 - Enable
		Device Allocation: AP, SM"
		DEFVAL	{ 1 }
	::= { networkLan 21 }

networkLan2Speed  OBJECT-TYPE
	SYNTAX	   Integer32 (10|100)
	MAX-ACCESS read-write
	STATUS	   current
	DESCRIPTION
		"LAN Speed 
			10	 - 10 Mb/s,
			100	 - 100 Mb/s
		Device Allocation: AP, SM"
		DEFVAL	{ 100 }
	::= { networkLan 22 }

networkLan2Duplex  OBJECT-TYPE
	SYNTAX	   Integer32 (0|1)
	MAX-ACCESS read-write
	STATUS	   current
	DESCRIPTION
		"LAN Duplex Mode 
			0 - Half,
			1 - Full
		Device Allocation: AP, SM"
		DEFVAL	{ 1 }
	::= { networkLan 23 }
	
networkLan2PoEEnabled  OBJECT-TYPE
	SYNTAX	   Integer32 (0|1)
	MAX-ACCESS read-write
	STATUS	   current
	DESCRIPTION
		"PoE Enabled 
			0 - Disabled,
			1 - Enabled
		Device Allocation: SM"
		DEFVAL	{ 1 }
	::= { networkLan 24 }

networkLanEnabled  OBJECT-TYPE
	SYNTAX	   Integer32 (0|1)
	MAX-ACCESS read-write
	STATUS	   current
	DESCRIPTION
		"Lan Port Enabled
			0 - Disable,
			1 - Enable
		Device Allocation: SM"
		DEFVAL	{ 1 }
	::= { networkLan 25 }

networkLanIPv6Addr  OBJECT-TYPE
        SYNTAX     Ipv6Address
        MAX-ACCESS read-write
        STATUS     current
        DESCRIPTION
                "SM NAT LAN IPv6 Address
                Device Allocation: SM"
        ::= { networkLan 31 }

networkWanIPAddressMode	 OBJECT-TYPE
		SYNTAX	   Integer32 (1|2)
		MAX-ACCESS read-write
		STATUS	   current
		DESCRIPTION
		"SM NAT WAN IP Address Mode
			1 - Static, 
			2 - DHCP
		Device Allocation: SM"
		DEFVAL	{ 1 }
		::= { networkWan 1 }

networkWanIPAddr  OBJECT-TYPE
		SYNTAX	   IpAddress
		MAX-ACCESS read-write
		STATUS	   current
		DESCRIPTION
		"SM NAT WAN IP Address
		Device Allocation: SM"
		::= { networkWan 2 }
		
networkWanNetmask  OBJECT-TYPE
		SYNTAX	   IpAddress
		MAX-ACCESS read-write
		STATUS	   current
		DESCRIPTION
		"SM NAT WAN IP Subnet Mask
		Device Allocation: SM"
		::= { networkWan 3 }

networkWanGatewayIP	 OBJECT-TYPE
		SYNTAX	   IpAddress
		MAX-ACCESS read-write
		STATUS	   current
		DESCRIPTION
		"SM NAT WAN Gateway IP Address
		Device Allocation: SM"
		::= { networkWan 4 }

networkWanDNSIPAddr	 OBJECT-TYPE
	SYNTAX	   IpAddress
	MAX-ACCESS read-write
	STATUS	   obsolete
	DESCRIPTION
		"SM NAT WAN DNS Server IP Address
		Device Allocation: SM"
	::= { networkWan 5 }

networkWanMTU  OBJECT-TYPE
	SYNTAX	   Integer32 (0|576..1700)
	MAX-ACCESS read-write
	STATUS	   current
	DESCRIPTION
		"SM NAT WAN MTU size
		Device Allocation: SM"
	DEFVAL	{ 1500 }
	::= { networkWan 6 }

networkWanDNSIPAddrPrimary	OBJECT-TYPE
	SYNTAX	   IpAddress
	MAX-ACCESS read-write
	STATUS	   current
	DESCRIPTION
		"SM NAT WAN DNS Server IP Address
		Device Allocation: SM
		Primary Server IP"
	::= { networkWan 7 }

networkWanDNSIPAddrSecondary  OBJECT-TYPE
	SYNTAX	   IpAddress
	MAX-ACCESS read-write
	STATUS	   current
	DESCRIPTION
		"SM NAT WAN DNS Server IP Address
		Device Allocation: SM
		Secondary Server IP"
	::= { networkWan 8 }

networkWanPPPoE	 OBJECT-TYPE
		SYNTAX	   Integer32 (0|1)
		MAX-ACCESS read-write
		STATUS	   current
		DESCRIPTION
		"SM only.Enable or Disable PPPoE
		mode. 1 is enable 0 is disable"
		DEFVAL	{ 0 }
		::= { networkWan 9 }
		
networkWanPPPoEUsername	 OBJECT-TYPE
		SYNTAX	   DisplayString (SIZE(0..128))
		MAX-ACCESS read-write
		STATUS	   current
		DESCRIPTION
		"SM only.Username to authenticate with
		PPPoE Server"
		::= { networkWan 10 }
		
networkWanPPPoEPassword	 OBJECT-TYPE
		SYNTAX	   DisplayString (SIZE(0..128))
		MAX-ACCESS read-write
		STATUS	   current
		DESCRIPTION
		"SM only.Password to authenticate with
		PPPoE Server"
		::= { networkWan 11 }
		
networkWanPPPoEAC  OBJECT-TYPE
		SYNTAX	   DisplayString (SIZE(0..128))
		MAX-ACCESS read-write
		STATUS	   current
		DESCRIPTION
		"SM only.PPPoE Access Concentrator Name"
		::= { networkWan 12 }
		
networkWanPPPoEService	OBJECT-TYPE
		SYNTAX	   DisplayString (SIZE(0..128))
		MAX-ACCESS read-write
		STATUS	   current
		DESCRIPTION
		"SM only.PPPoE Service Name"
		::= { networkWan 13 }
		
networkWanPPPoEAuth	 OBJECT-TYPE
		SYNTAX	   Integer32 (0|1|2)
		MAX-ACCESS read-write
		STATUS	   current
		DESCRIPTION
		"SM only.This indicates type of authentication
		with PPPoE Server. Options are
		0 - All
		1 - PAP
		2 - CHAP"
		DEFVAL	{ 0 }
		::= { networkWan 14 }
		
networkWanPPPoEMTU	OBJECT-TYPE
		SYNTAX	   Integer32 (0|576..1492)
		MAX-ACCESS read-write
		STATUS	   current
		DESCRIPTION
		"SM only.MTU size to be used for PPPoE
		connection"
		DEFVAL	{ 1492 }
		::= { networkWan 15 }
		
networkWanPPPoEKeepAlive OBJECT-TYPE
		SYNTAX	   Integer32 (0|5..180)
		MAX-ACCESS read-write
		STATUS	   current
		DESCRIPTION
		"SM only.Time in seconds for the keep Alive
		messages from PPPoE client to PPPoE
		Server"
		DEFVAL	{ 10 }
		::= { networkWan 16 }
		
networkWanPPPoEMSSClamping OBJECT-TYPE
		SYNTAX	   Integer32 (0|1)
		MAX-ACCESS read-write
		STATUS	   current
		DESCRIPTION
		"SM only.Enable or disable MSS Clamping
		0 - Disable
		1 - Enable"
		DEFVAL	{ 0 }
		::= { networkWan 17 }		

networkPPPoEIAEnable OBJECT-TYPE
                SYNTAX     Integer32 (0|1)
                MAX-ACCESS read-write
                STATUS     current
                DESCRIPTION
                "PPPoE Intermediate Agent
                0 - Disable
                1 - Enable
                Device Allocation: AP"
                DEFVAL  { 0 }
                ::= { networkPPPoE 1 }

networkPPPoEIATable   OBJECT-TYPE
        SYNTAX SEQUENCE OF NetworkPPPoEIAEntry
        MAX-ACCESS not-accessible
        STATUS     current
        DESCRIPTION
                "PPPoE IA Table"
        ::= { networkPPPoE 2 }

networkPPPoEIAEntry OBJECT-TYPE
        SYNTAX     NetworkPPPoEIAEntry
        MAX-ACCESS not-accessible
        STATUS     current
        DESCRIPTION
                "PPPoE IA Table Entry
                Device Allocation: AP"
        INDEX   { networkPPPoEIAIndex }
        ::= { networkPPPoEIATable 1 }

NetworkPPPoEIAEntry ::= SEQUENCE {
        networkPPPoEIAIndex
                Integer32,
        networkPPPoEIAUID
                Integer32,
        networkPPPoEIASMMAC
                DisplayString,
        networkPPPoEIAPhoneNumber
                DisplayString,
        networkPPPoEIATerminal
                DisplayString,
        networkPPPoEIAFrame
                DisplayString,
        networkPPPoEIASlot
                DisplayString,
        networkPPPoEIAPort
                DisplayString,
        networkPPPoEIAVlanId
                Integer32
}

networkPPPoEIAIndex OBJECT-TYPE
        SYNTAX     Integer32 (0..127)
        MAX-ACCESS read-write
        STATUS     current
        DESCRIPTION
        "PPPoE IA Table Index
        Table Entry is cleared if Index is set to zero
        Device Allocation: AP"
        ::= { networkPPPoEIAEntry 1 }

networkPPPoEIAUID OBJECT-TYPE
        SYNTAX     Integer32 (1..128)
        MAX-ACCESS read-write
        STATUS     current
        DESCRIPTION
        "PPPoE IA UID
        Device Allocation: AP"
        ::= { networkPPPoEIAEntry 2 }

networkPPPoEIASMMAC OBJECT-TYPE
        SYNTAX     DisplayString (SIZE(0|11..17))
        MAX-ACCESS read-write
        STATUS     current
        DESCRIPTION
        "PPPoE IA Registered SM MAC Address
        Device Allocation: AP"
        ::= { networkPPPoEIAEntry 3 }

networkPPPoEIAPhoneNumber OBJECT-TYPE
        SYNTAX     DisplayString (SIZE(0..32))
        MAX-ACCESS read-write
        STATUS     current
        DESCRIPTION
        "PPPoE IA Phone Number
        Device Allocation: AP"
        ::= { networkPPPoEIAEntry 4 }

networkPPPoEIATerminal OBJECT-TYPE
        SYNTAX     DisplayString (SIZE(0..3))
        MAX-ACCESS read-write
        STATUS     current
        DESCRIPTION
        "PPPoE IA Terminal ID
        Device Allocation: AP"
        ::= { networkPPPoEIAEntry 5 }

networkPPPoEIAFrame OBJECT-TYPE
        SYNTAX     DisplayString (SIZE(0..1))
        MAX-ACCESS read-write
        STATUS     current
        DESCRIPTION
        "PPPoE IA Frame ID
        Device Allocation: AP"
        ::= { networkPPPoEIAEntry 6 }

networkPPPoEIASlot OBJECT-TYPE
        SYNTAX     DisplayString (SIZE(0..2))
        MAX-ACCESS read-write
        STATUS     current
        DESCRIPTION
        "PPPoE IA Slot
        Device Allocation: AP"
        ::= { networkPPPoEIAEntry 7 }

networkPPPoEIAPort OBJECT-TYPE
        SYNTAX     DisplayString (SIZE(0..1))
        MAX-ACCESS read-write
        STATUS     current
        DESCRIPTION
        "PPPoE IA Port number
        Device Allocation: AP"
        ::= { networkPPPoEIAEntry 8 }

networkPPPoEIAVlanId OBJECT-TYPE
        SYNTAX     Integer32 (1..4095)
        MAX-ACCESS read-write
        STATUS     current
        DESCRIPTION
        "PPPoE IA VLAN ID
        Device Allocation: AP"
        ::= { networkPPPoEIAEntry 9 }

networkWanIPv6AddressMode  OBJECT-TYPE
		SYNTAX     Integer32 (0|1|2)
		MAX-ACCESS read-write
		STATUS     current
		DESCRIPTION
		"SM NAT WAN IPv6 Address Mode
			1 - Static,
			2 - DHCPv6
		Device Allocation: SM"
		DEFVAL  { 1 }
		::= { networkWan 30 }

networkWanIPv6Addr  OBJECT-TYPE
                SYNTAX     Ipv6Address
                MAX-ACCESS read-write
                STATUS     current
                DESCRIPTION
                "SM NAT WAN IPv6 Address
                Device Allocation: SM"
                ::= { networkWan 31 }

networkWanGatewayIPv6  OBJECT-TYPE
                SYNTAX     Ipv6Address
                MAX-ACCESS read-write
                STATUS     current
                DESCRIPTION
                "SM NAT WAN IPv6 Gateway Address
                Device Allocation: SM"
                ::= { networkWan 32 }
		
networkBridgeIPAddressMode	OBJECT-TYPE
	SYNTAX	   Integer32 (1|2)
	MAX-ACCESS read-write
	STATUS	   current
	DESCRIPTION 
		"Device Bridge IP Address Mode
			1 - Static, 
			2 - DHCP
		Device Allocation: AP, SM"
	DEFVAL	{ 1 }
	::= { networkBridge 1 }

networkBridgeIPAddr	 OBJECT-TYPE
	SYNTAX	   IpAddress
	MAX-ACCESS read-write
	STATUS	   current
	DESCRIPTION 
		"Device Bridge IP Address
		Device Allocation: AP, SM"
	::= { networkBridge 2 }

networkBridgeNetmask  OBJECT-TYPE
	SYNTAX	   IpAddress
	MAX-ACCESS read-write
	STATUS	   current
	DESCRIPTION 
		"Device Bridge IP Subnet Mask
		Device Allocation: AP, SM"
	::= { networkBridge 3 }

networkBridgeGatewayIP	OBJECT-TYPE
	SYNTAX	   IpAddress
	MAX-ACCESS read-write
	STATUS	   current
	DESCRIPTION 
		"Device Bridge Gateway IP Address
		Device Allocation: AP, SM"
	::= { networkBridge 4 }

networkBridgeDNSIPAddr	OBJECT-TYPE
	SYNTAX	   IpAddress
	MAX-ACCESS read-write
	STATUS	   obsolete
	DESCRIPTION
		"Device Bridge DNS Server IP Address
		Device Allocation: AP, SM"
	::= { networkBridge 5 }

networkBridgeMTU  OBJECT-TYPE
	SYNTAX	   Integer32 (0|576..1700)
	MAX-ACCESS read-write
	STATUS	   current
	DESCRIPTION
		"Device Bridge MTU size
		Device Allocation: AP, SM"
	DEFVAL	{ 1500 }
	::= { networkBridge 6 }

networkBridgeDNSIPAddrPrimary  OBJECT-TYPE
	SYNTAX	   IpAddress
	MAX-ACCESS read-write
	STATUS	   current
	DESCRIPTION
		"Device Bridge DNS Server IP Address
		Device Allocation: AP, SM
		Primary Server IP"
	::= { networkBridge 7 }

networkBridgeDNSIPAddrSecondary	 OBJECT-TYPE
	SYNTAX	   IpAddress
	MAX-ACCESS read-write
	STATUS	   current
	DESCRIPTION
		"Device Bridge DNS Server IP Address
		Device Allocation: AP, SM
		Secondary Server IP"
	::= { networkBridge 8 }
networkBridgeIPv6AddressMode  OBJECT-TYPE
	SYNTAX     Integer32 (0|1|2)
	MAX-ACCESS read-write
	STATUS     current
	DESCRIPTION
	"Device Bridge IPv6 Address Mode
		1 - Static,
		2 - DHCPv6
	Device Allocation: AP, SM"
	DEFVAL  { 1 }
	::= { networkBridge 30 }

networkBridgeIPv6Addr  OBJECT-TYPE
        SYNTAX     Ipv6Address
        MAX-ACCESS read-write
        STATUS     current
        DESCRIPTION
                "Device Bridge IPv6 Address
                Device Allocation: AP, SM"
        ::= { networkBridge 31 }

networkBridgeGatewayIPv6  OBJECT-TYPE
        SYNTAX     Ipv6Address
        MAX-ACCESS read-write
        STATUS     current
        DESCRIPTION
                "Device Bridge IPv6 Gateway Address
                Device Allocation: AP, SM"
        ::= { networkBridge 32 }

networkPortSecurity OBJECT-TYPE
		SYNTAX	   Integer32 (0|1)
		MAX-ACCESS read-write
		STATUS	   current
		DESCRIPTION
				"LAN Port Security switch:
						0 - Disable
						1 - Enable
				Device Allocation: SM"
		DEFVAL	{ 0 }
		::= { network 8 }

networkPortSecurityMax OBJECT-TYPE
		SYNTAX	   Integer32 (0..255)
		MAX-ACCESS read-write
		STATUS	   current
		DESCRIPTION
			"Number of secure MAC addresses:
						1-254 - Fixed Learned MAC limit
				Device Allocation: SM"
		DEFVAL	{ 5 }
		::= { network 9 }

networkPortSecurityAgingTime OBJECT-TYPE
		SYNTAX	   Integer32 (0..1440)
		MAX-ACCESS read-write
		STATUS	   current
		DESCRIPTION
				"Security MAC address aging time:
						This prameter indicates on how long to store learned MAC address in the cache in seconds,
						0 - do not delete MAC address from the buffer,
						Default - is 300 seconds.
				Device Allocation: AP, SM"
		DEFVAL	{ 300 }
		::= { network 10 }

mcastGroupLimit OBJECT-TYPE
		SYNTAX	   Integer32 (0|1..5)
		MAX-ACCESS read-write
		STATUS	   current
		DESCRIPTION
				"Multicast Group Limit:
						Default - 3 Multicast Groups for SM, unlimited for AP.
				Device Allocation: SM"
		DEFVAL	{ 3 }
		::= { network 17 }

mgmtIFEnable OBJECT-TYPE
		SYNTAX	   Integer32 (0|1)
		MAX-ACCESS read-write
		STATUS	   current
		DESCRIPTION
				"Separate Management Interface Enabled:
				0 - Disabled,
				1 - Enabled
				Device Allocation: SM"
		DEFVAL	{ 0 }
		::= { mgmtIF 1 }

mgmtIFVLAN OBJECT-TYPE
		SYNTAX	   Integer32 (0|1)
		MAX-ACCESS read-write
		STATUS	   current
		DESCRIPTION
				"Separate Management Interface VLAN Enabled:
				0 - Disabled,
				1 - Enabled
				Device Allocation: SM"
		DEFVAL	{ 0 }
		::= { mgmtIF 2 }

mgmtIFVID OBJECT-TYPE
		SYNTAX	   Integer32 (0..4094)
		MAX-ACCESS read-write
		STATUS	   current
		DESCRIPTION
				"Separate Management Interface VLAN
				Device Allocation: SM"
		::= { mgmtIF 3 }

mgmtIFVP OBJECT-TYPE
		SYNTAX	   Integer32 (0..7)
		MAX-ACCESS read-write
		STATUS	   current
		DESCRIPTION
				"Separate Management Interface VP
				Device Allocation: SM"
		::= { mgmtIF 4 }

mgmtIFIPAddressMode OBJECT-TYPE
		SYNTAX	   Integer32 (1|2)
		MAX-ACCESS read-write
		STATUS	   current
		DESCRIPTION
				"Separate Management IP Address Mode
			1 - Static,
			2 - DHCP
		Device Allocation: SM"
		::= { mgmtIF 5 }

mgmtIFIPAddr OBJECT-TYPE
		SYNTAX	   IpAddress
		MAX-ACCESS read-write
		STATUS	   current
		DESCRIPTION
				"Separate Management IP Address
				Device Allocation: SM"
		::= { mgmtIF 6 }

mgmtIFNetmask OBJECT-TYPE
		SYNTAX	   IpAddress
		MAX-ACCESS read-write
		STATUS	   current
		DESCRIPTION
				"Separate Management IP Subnet Mask
				Device Allocation: SM"
		::= { mgmtIF 7 }

mgmtIFGateway OBJECT-TYPE
		SYNTAX	   IpAddress
		MAX-ACCESS read-write
		STATUS	   current
		DESCRIPTION
				"Separate Management IP Gateway
				Device Allocation: SM"
		::= { mgmtIF 8 }
mgmtIFIPv6AddressMode OBJECT-TYPE
		SYNTAX     Integer32 (0|1|2)
		MAX-ACCESS read-write
		STATUS     current
		DESCRIPTION
				"Separate Management IPv6 Address Mode
					1 - Static,
					2 - DHCPv6
				Device Allocation: SM"
		::= { mgmtIF 30 }

mgmtIFIPv6Addr OBJECT-TYPE
		SYNTAX     Ipv6Address
		MAX-ACCESS read-write
		STATUS     current
		DESCRIPTION
				"Separate Management IPv6 Address
				Device Allocation: SM"
		::= { mgmtIF 31 }

mgmtIFIPv6Gateway  OBJECT-TYPE
                SYNTAX     Ipv6Address
                MAX-ACCESS read-write
                STATUS     current
                DESCRIPTION
                                "Separate Management IPv6 Gateway Address
                                Device Allocation: SM"
                ::= { mgmtIF 32 }

cambiumIPAliasCnfTable	 OBJECT-TYPE
	SYNTAX SEQUENCE OF CambiumIPAliasCnfEntry
	MAX-ACCESS not-accessible
	STATUS	   current
	DESCRIPTION
		"Static Network Table"
	::= { networkAliases 1 }

cambiumIPAliasCnfEntry OBJECT-TYPE
	SYNTAX	   CambiumIPAliasCnfEntry
	MAX-ACCESS not-accessible
	STATUS	   current
	DESCRIPTION
		"Static Network Table Entry
		Device Allocation: SM"
	INDEX	{ cambiumIPAliasesIndex }
	::= { cambiumIPAliasCnfTable 1 }

CambiumIPAliasCnfEntry ::= SEQUENCE {
	cambiumIPAliasesIndex
		Integer32,
	cambiumIPAliasesIpAddr
		IpAddress,
	cambiumIPAliasesNetmask
		IpAddress,
	cambiumIPAliasesInfo
		DisplayString
}

cambiumIPAliasesIndex OBJECT-TYPE
	SYNTAX	   Integer32 (0..16)
	MAX-ACCESS read-write 
	STATUS	   current
	DESCRIPTION
	"IP Alias Table Index
	Table Entry is cleared if Index is set to zero
	Device Allocation: AP, SM"
	::= { cambiumIPAliasCnfEntry 1 }

cambiumIPAliasesIpAddr	OBJECT-TYPE
	SYNTAX	   IpAddress
	MAX-ACCESS read-write
	STATUS	   current
	DESCRIPTION 
		"Network IP Alliases address"
	::= { cambiumIPAliasCnfEntry 2 }

cambiumIPAliasesNetmask OBJECT-TYPE
	SYNTAX		IpAddress
	MAX-ACCESS	read-write
	STATUS		current
	DESCRIPTION 
		"Network Dest IP Netmask"
	::= { cambiumIPAliasCnfEntry 3 }

cambiumIPAliasesInfo  OBJECT-TYPE
	SYNTAX	   DisplayString (SIZE(0..128))
	MAX-ACCESS read-write
	STATUS	   current
	DESCRIPTION
		"Network Info message"
	::= { cambiumIPAliasCnfEntry 4 }

cambiumIPAliasesEnable	OBJECT-TYPE
	SYNTAX	   Integer32 (0|1)
	MAX-ACCESS read-write
	STATUS	   current
	DESCRIPTION
		"Enable/Disable IP Aliases in Router mode
		Device Allocation: SM"
	::= { networkAliases 2 }

networkLanDefaultIP OBJECT-TYPE
		SYNTAX	   IpAddress
		MAX-ACCESS read-write
		STATUS	   current
		DESCRIPTION
				"Default Network IP
				Device Allocation: SM"
		::= { network 25 }

networkRelaydEnable OBJECT-TYPE
		SYNTAX	   Integer32 (0|1)
		MAX-ACCESS read-write
		STATUS	   current
		DESCRIPTION
		"Relay for forwarding DHCP packets:
			0 - Disable
			1 - Enable
		Device Allocation: AP,SM"
	DEFVAL	{ 0 }
	::= { network 26 }

networkUPNP OBJECT-TYPE
        SYNTAX     Integer32 (0|1)
        MAX-ACCESS read-write
        STATUS     current
        DESCRIPTION
                "Enable UPnP on SM in NAT mode
                0 - Disable,
                1 - Enable
                Device Allocation: SM"
        ::= { upnpd 1 }

networkNATPMP OBJECT-TYPE
        SYNTAX     Integer32 (0|1)
        MAX-ACCESS read-write
        STATUS     current
        DESCRIPTION
                "Enable NAT-PMP on SM in NAT mode
                0 - Disable,
                1 - Enable
                Device Allocation: SM"
        ::= { upnpd 2 }

networkLLDP OBJECT-TYPE
        SYNTAX     Integer32 (0|1)
        MAX-ACCESS read-write
        STATUS     current
        DESCRIPTION
                "Enable LLDP
                0 - Disable,
                1 - Enable
                Device Allocation: AP,SM"
        ::= { lldpd 1 }

networkLLDPMode OBJECT-TYPE
        SYNTAX     Integer32 (1|2)
        MAX-ACCESS read-write
        STATUS     current
        DESCRIPTION
                "LLDP mode
				1 - receive and transmit LLDPDU
				2 - only receive LLDPDU
                Device Allocation: AP,SM"
        ::= { lldpd 2 }

networkMACTELNET OBJECT-TYPE
        SYNTAX     Integer32 (0|1)
        MAX-ACCESS read-write
        STATUS     current
        DESCRIPTION
                "Enable MAC-Telnet Service
                 0 - Disable,
                 1 - Enable
                 Device Allocation: AP,SM"
	DEFVAL { 1 }
        ::= { mactelnet 1 }

networkMACTELNETProto OBJECT-TYPE
        SYNTAX     Integer32 (1|2)
        MAX-ACCESS read-write
        STATUS     current
        DESCRIPTION
                "MAC-Telnet Service Protocol
                 1 - MAC-Telnet
                 2 - MAC-SSH
                 Device Allocation: AP,SM"
	DEFVAL { 1 }
        ::= { mactelnet 2 }

cambiumLicenseServerEnable OBJECT-TYPE
	SYNTAX     Integer32 (0|1)
	MAX-ACCESS read-write
	STATUS     current
	DESCRIPTION
		"Enable License Server Connector
		 0 - Disable,
		 1 - Enable
		 Device Allocation: AP"
	DEFVAL { 1 }
	::= { licensed 1 }

cambiumLicenseServerCloudLicensingID OBJECT-TYPE
	SYNTAX     DisplayString
	MAX-ACCESS read-write
	STATUS     current
	DESCRIPTION
		"Cambium Cloud Licensing Identification number. Used for AP identification on the Licensing Server.
		 Device Allocation: AP"
	::= { licensed 2 }

cambiumLicenseServerStatus OBJECT-TYPE
	SYNTAX     Integer32 (-1|0|1|2|2001..2034)
	MAX-ACCESS read-only
	STATUS     current
	DESCRIPTION
		"Status of License Server Connector or error code from License Server
		 -1 - Unknown,
		 0 - Connecting to License Server,
		 1 - Connected. ePMP Elevate Subscriber Module Limit synced with License Server,
		 2 - Connected. ePMP Elevate Subscriber Module Limit Exceeded,
		 2004 - Units are not supported with limited concurrency,
		 2012 - Not authorized to process any request,
		 2015 - Internal error,
		 2018 - License is expired,
		 2019 - License is disabled,
		 2023 - License does not exist or license is not in active state,
		 2024 - Invalid parameter,
		 2025 - Session terminated,
		 2026 - Access denied to the requested feature,
		 2031 - No authorization server mapped to given vendorId
		 Device Allocation: AP"
	::= { licensed 3 }

cambiumLicenseServerRefreshFail OBJECT-TYPE
	SYNTAX     Integer32
	MAX-ACCESS read-only
	STATUS     current
	DESCRIPTION
		"Counter of consecutive failures on License Server allocation refresh.
		 Refresh request is made at some intervals (each 20 minutes).
		 Device Allocation: AP"
	::= { licensed 4 }

cambiumLicenseServerUpdateFail OBJECT-TYPE
	SYNTAX     Integer32
	MAX-ACCESS read-only
	STATUS     current
	DESCRIPTION
		"Counter of consecutive failures on License Server allocation request.
		 Allocation request is made either after reboot or when number of
		 connected SMs is changed.
		 Device Allocation: AP"
	::= { licensed 5 }

snmpReadOnlyCommunity  OBJECT-TYPE
	SYNTAX	   DisplayString
	MAX-ACCESS read-write
	STATUS	   current
	DESCRIPTION 
		"SNMP read-only community name
		Device Allocation: AP, SM"
	DEFVAL	{ "public" }
	::= { snmp 1 }

snmpReadWriteCommunity	OBJECT-TYPE
	SYNTAX	   DisplayString
	MAX-ACCESS read-write
	STATUS	   current
	DESCRIPTION 
		"SNMP read-write community name
		Device Allocation: AP, SM"
	DEFVAL	{ "private" }
	::= { snmp 2 }

snmpSystemName	OBJECT-TYPE
	SYNTAX	   DisplayString
	MAX-ACCESS read-write
	STATUS	   current
	DESCRIPTION 
		"SNMP System Name
		Device Allocation: AP, SM"
	DEFVAL	{ "CambiumNetworks" }
	::= { snmp 3 }

snmpSystemDescription  OBJECT-TYPE
	SYNTAX	   DisplayString
	MAX-ACCESS read-write
	STATUS	   current
	DESCRIPTION 
		"SNMP System Description
		Device Allocation: AP, SM"
	::= { snmp 4 }

snmpTrapEnable	OBJECT-TYPE
		SYNTAX	   Integer32 (0|1)
		MAX-ACCESS read-write
		STATUS	   current
		DESCRIPTION
		"SNMP Trap Support Enable
			0 - Disable, 
			1 - Enable
		Device Allocation: AP, SM"
		DEFVAL	{ 0 }
		::= { snmp 5 }

snmpTrapCommunity  OBJECT-TYPE
		SYNTAX	   DisplayString
		MAX-ACCESS read-write
		STATUS	   current
		DESCRIPTION
		"SNMP Trap Community
		Device Allocation: AP, SM"
		::= { snmp 6 }

snmpTrapTable  OBJECT-TYPE
		SYNTAX SEQUENCE OF SNMPTrapEntry
		MAX-ACCESS not-accessible
		STATUS	   current
		DESCRIPTION
		"SNMP Trap Servers Table
		Device Allocation: AP, SM"
		::= { snmp 7 }

snmpTrapEntry  OBJECT-TYPE
		SYNTAX	SNMPTrapEntry
		MAX-ACCESS not-accessible
		STATUS	   current
		DESCRIPTION
		"SNMP Trap Table Entry
		Device Allocation: AP, SM"
		INDEX	{ snmpTrapEntryIndex }
		::= { snmpTrapTable 1 }

SNMPTrapEntry ::= SEQUENCE {
		snmpTrapEntryIndex
				Integer32,
		snmpTrapEntryIP
				IpAddress,
		snmpTrapEntryPort
				Integer32
}

snmpTrapEntryIndex OBJECT-TYPE
		SYNTAX	   Integer32 (0..4)
		MAX-ACCESS read-write
		STATUS	   current
		DESCRIPTION
		"SNMP Trap Server IP Table Index
		Table Entry is cleared if Index is set to zero
		Device Allocation: AP, SM"
		::= { snmpTrapEntry 1 }

snmpTrapEntryIP OBJECT-TYPE
		SYNTAX	   IpAddress
		MAX-ACCESS read-write
		STATUS	   current
		DESCRIPTION
		"SNMP Trap Server IP Address
		Device Allocation: AP, SM"
		::= { snmpTrapEntry 2 }

snmpTrapEntryPort OBJECT-TYPE
		SYNTAX	   Integer32 (0..65535)
		MAX-ACCESS read-write
		STATUS	   current
		DESCRIPTION
		"SNMP Trap Server Port Number
		Device Allocation: AP, SM"
		DEFVAL	{ 162 }
		::= { snmpTrapEntry 3 }

snmpDomainAccessEnable	OBJECT-TYPE
		SYNTAX	   Integer32 (0|1)
		MAX-ACCESS read-write
		STATUS	   current
		DESCRIPTION
		"SNMP Access Domain Enable
			0 - Disable, 
			1 - Enable
		Device Allocation: AP, SM"
		DEFVAL	{ 0 }
		::= { snmp 8 }

snmpDomainAccessIP OBJECT-TYPE
		SYNTAX	   DisplayString(SIZE(0|7..15))
		MAX-ACCESS read-write
		STATUS	   current
		DESCRIPTION
		"SNMP Access Domain IP Address
		Device Allocation: AP, SM"
		::= { snmp 9 }

snmpDomainAccessIPMask OBJECT-TYPE
		SYNTAX	   DisplayString(SIZE(0|7..15))
		MAX-ACCESS read-write
		STATUS	   current
		DESCRIPTION
		"SNMP Access Domain IP Mask
		Device Allocation: AP, SM"
		::= { snmp 10 }

systemConfigTimezone  OBJECT-TYPE
	SYNTAX	   DisplayString
	MAX-ACCESS read-write
	STATUS	   current
	DESCRIPTION 
		"Time Zone
		Device Allocation: AP, SM"
	DEFVAL	{ "GMT" }
	::= { systemConfig 1 }

systemConfigDeviceName	OBJECT-TYPE
		SYNTAX	   DisplayString (SIZE(0|1..128))
		MAX-ACCESS read-write
		STATUS	   current
		DESCRIPTION
		"SM Device Name
		Device Allocation: AP, SM"
		DEFVAL	{ "Cambium-STA" }
		::= { systemConfig 2 }
		
systemConfigETSILicense	 OBJECT-TYPE
		SYNTAX	   DisplayString (SIZE(0..128))
		MAX-ACCESS read-write
		STATUS	   obsolete
		DESCRIPTION
		"ETSI Country Code. 
		Set the country code using license key on AP. Visit Cambium Webserver
		to get the license key. The country code set in license key will
		be used to set country code on AP if the key validation pass. This 
		parameter is for AP only.
		Device Allocation: AP"
		DEFVAL	{ "ETSIkey" }
		::= { systemConfig 3 }		  

systemConfigSWLockBit  OBJECT-TYPE
		SYNTAX	   Integer32 (0|1)
		MAX-ACCESS read-only
		STATUS	   current
		DESCRIPTION
		"Software Lock Bit.
		This bit indicates if the Software Lock Bit is set or not.
		If the software bit is set then country code needs to be
		set using License Key from Cambium Webserver
			0 - Bit not Set, 
			1 - Bit is set
		Device Allocation: AP, SM"
		DEFVAL	{ 0 }
		::= { systemConfig 4 } 

systemConfigHWLockBit  OBJECT-TYPE
		SYNTAX	   Integer32 (0|1)
		MAX-ACCESS read-only
		STATUS	   current
		DESCRIPTION
		"Hardware Lock Bit.
		This bit indicates if the hardware Lock Bit is set or not.
		If the hardware bit is set then country code cannot be changed.
			0 - Bit not Set, 
			1 - Bit is set
		Device Allocation: AP, SM"
		DEFVAL	{ 0 }
		::= { systemConfig 5 }								  

systemDeviceLocLatitude	 OBJECT-TYPE
		SYNTAX	   DisplayString (SIZE(0..128))
		MAX-ACCESS read-write
		STATUS	   current
		DESCRIPTION
		"Device GPS Location Latitude.
		Coordinates of device in (h ddd.ddddd) format.
		Used to display location at Google Maps service.
		Device Allocation: AP, SM"
		::= { systemConfig 6 }

systemDeviceLocLongitude  OBJECT-TYPE
		SYNTAX	   DisplayString (SIZE(0..128))
		MAX-ACCESS read-write
		STATUS	   current
		DESCRIPTION
		"Device GPS Location Longitude.
		Coordinates of device in (h ddd.ddddd) format.
		Used to display location at Google Maps service.
		Device Allocation: AP, SM"
		::= { systemConfig 7 }
		
systemDeviceLocHeight  OBJECT-TYPE
		SYNTAX	   DisplayString (SIZE(0..128))
		MAX-ACCESS read-write
		STATUS	   current
		DESCRIPTION
		"Device GPS Location Longitude.
		Altitude of device above/below mean sea level.
		Device Allocation: AP, SM"
		::= { systemConfig 8 }

-- skip systemConfig 9 for GPSKey License

systemConfigisGPSkeyOK  OBJECT-TYPE
        SYNTAX     Integer32 (0|1)
        MAX-ACCESS read-only
        STATUS     obsolete
        DESCRIPTION
		"GPS Lock.
		This field indicates if the GPS Key is OK. Based on this the GPS
		is locked on the board.
			0 - GPS Key is bad. Sync Source defaulted to Internal GPS only
			1 - GPS Key is good. User can set sync source to any value 
		Device Allocation: AP"
        DEFVAL  { 0 }
        ::= { systemConfig 10 }

systemConfigGPSLockBit  OBJECT-TYPE
        SYNTAX     Integer32 (0..2)
        MAX-ACCESS read-only
        STATUS     obsolete
        DESCRIPTION
                "GPS Lock Bit.
                This bit indicates if the GPS feature Lock Bit is set or not.
                If the hardware bit is set then GPS synchronisation can't be used.
                        0 - No limitation of usage GPS synchronisation,
                        1 - GPS synchronisation not allowed,
                        2 - The GPSkey required to allow synchronisation
                Device Allocation: AP"
        DEFVAL  { 0 }
        ::= { systemConfig 11 }

systemConfigSMLockBit  OBJECT-TYPE
        SYNTAX     Integer32 (0..2)
        MAX-ACCESS read-only
        STATUS     current
        DESCRIPTION
		"SM Lock Bit
                This bit indicates if the AP is locked for Maximum SM registrations support.
                If the bit is set then maximum of 10 SMs can be registered on the AP.
                        0 - No limitation, up to 120 SM registrations are supported,
                        1 - AP is tiered with 10 SM registrations
                Device Allocation: AP"
        DEFVAL  { 0 }
        ::= { systemConfig 12 }

systemConfigSMLimit  OBJECT-TYPE
        SYNTAX     Integer32 (0..120)
        MAX-ACCESS read-only
        STATUS     current
        DESCRIPTION
		"SM Registrations limit, based on Operational License content.
		Indicates the maximum number of SMs with could be registered to an AP.
		Valid only in TDD mode if device is AP Lite.
		Device Allocation: AP"
        DEFVAL  { 0 }
        ::= { systemConfig 13 }

cambiumePMPElevateHWLicenseLimit  OBJECT-TYPE
	SYNTAX	   Integer32 (0..120)		
	MAX-ACCESS read-only
	STATUS	   current
	DESCRIPTION
	"ePMP Elevate STA according to the license
	Device Allocation: AP"
	DEFVAL	{ 0 }
	::= { systemConfig 14 }
		
powerSequenceFactoryDefault OBJECT-TYPE
	SYNTAX	   Integer32 (0|1)
	MAX-ACCESS read-write
	STATUS	   current
	DESCRIPTION
		"Set this to enable or disable the ability to factory default the radio's 
		configuration using the power cycle sequence(explained in the User Guide). 
			0 - Disabled 
			1 - Enabled
		Device Allocation: AP, SM"
	DEFVAL	{ 1 }
	::= { systemConfig 15 }

systemConfigLockedCC OBJECT-TYPE
	SYNTAX	   DisplayString (SIZE(0|1..2))
	MAX-ACCESS read-only
	STATUS	   current
	DESCRIPTION
		"Return Locked Country Value in case if device is locked for particular country.
		Device Allocation: AP, SM"
	::= { systemConfig 16 }

systemConfigMinAntGain OBJECT-TYPE
	SYNTAX	   Integer32 (0..40)
	MAX-ACCESS read-only
	STATUS	   current
	DESCRIPTION
		"Return Minimum allowed Antenna Gain.
		Device Allocation: AP, SM"
	::= { systemConfig 17 }

systemConfigOperationalLicense OBJECT-TYPE
	SYNTAX	   DisplayString (SIZE(0..128))
	MAX-ACCESS read-write
	STATUS	   current
	DESCRIPTION
		"Device Operational License. 
		Set Operational License on AP to extend basic functionality. 
		Visit Cambium Webserver to get the license key. ETSI country code and 
		maximum SMs count value will be set on AP if the key validation pass.
		License is required on locked devices only.
		Device Allocation: AP"
	::= { systemConfig 18 }

systemConfigIPv6Support OBJECT-TYPE
        SYNTAX     Integer32 (0|1)
        MAX-ACCESS read-write
        STATUS     current
        DESCRIPTION
                "Systemwide IPv6 support.
                Enables Systemwide IPv6 support:
                        0 - IPv6 Support Disabled,
                        1 - IPv6 Support Enabled,
                Device Allocation: AP, SM"
        ::= { systemConfig 19 }

systemConfigFactoryResetKeepPwd OBJECT-TYPE
	SYNTAX	   Integer32 (0|1)
	MAX-ACCESS read-write
	STATUS	   current
	DESCRIPTION
		"Keep Passwords after Factory Default
			0 - Disabled
			1 - Enabled
		Device Allocation: AP, SM"
	DEFVAL	{ 0 }
	::= { systemConfig 20 }

systemNtpServerIPMode OBJECT-TYPE 
	SYNTAX	   Integer32 (1|2)
	MAX-ACCESS read-write
	STATUS	   current
	DESCRIPTION
		"NTP Server IP Address receive mode
			1 - Static, 
			2 - DHCP
		Device Allocation: AP, SM"
	DEFVAL	{ 2 }
	::= { systemNtpServer 1 }

systemNtpServerPrimaryIP  OBJECT-TYPE
	SYNTAX	   IpAddress
	MAX-ACCESS read-write
	STATUS	   current
	DESCRIPTION 
		"NTP Server 1 IP Address
		Device Allocation: AP, SM"
	::= { systemNtpServer 2 }
	
systemNtpServerSecondaryIP	OBJECT-TYPE
	SYNTAX	   IpAddress
	MAX-ACCESS read-write
	STATUS	   current
	DESCRIPTION 
		"NTP Server 2 IP Address
		Device Allocation: AP, SM"
	::= { systemNtpServer 3 }

webService OBJECT-TYPE 
		SYNTAX	   Integer32 (1|2)
		MAX-ACCESS read-write
		STATUS	   current
		DESCRIPTION
		"Web Service
			1 - HTTP, 
			2 - HTTPS
		Device Allocation: AP, SM"
		DEFVAL	{ 1 }
		::= { cambiumWebServer 1 }

httpPort  OBJECT-TYPE
	SYNTAX	   Integer32 (0..65535)
	MAX-ACCESS read-write
	STATUS	   current
	DESCRIPTION 
		"HTTP Port
		Device Allocation: AP, SM"
	DEFVAL	{ 80 }
	::= { cambiumWebServer 2 }

httpsPort  OBJECT-TYPE
	SYNTAX	   Integer32 (0..65535)
	MAX-ACCESS read-write
	STATUS	   current
	DESCRIPTION 
		"HTTPs Port"
	DEFVAL	{ 443 }
	::= { cambiumWebServer 3 }

wirelessDeviceCountryCode  OBJECT-TYPE
	SYNTAX	   DisplayString (SIZE(0|2))
	MAX-ACCESS read-write
	STATUS	   current
	DESCRIPTION 
		"Country Code. 
		If US Lock SKU, this is US and cannot be changed. 
		If not locked, for 9350, it will be None, for 9344, it will be Follow AP CC. 
		When user change CC at SM, the SM Scan Frequency Type  will be FA
		Device Allocation: AP"
	DEFVAL	{ "NS" }
	::= { wirelessDevice 1 }

wirelessType  OBJECT-TYPE
		SYNTAX	   Integer32 (1|2)
		MAX-ACCESS read-write
		STATUS	   obsolete
		DESCRIPTION
				"Wireless type:
						1 - tdd driver,
						2 - 80211 (aquila) driver
				Device Allocation: AP, SM"
	DEFVAL	{ 1 }
	::= { wirelessDevice 2 }

wirelessDefaultCountryCode	OBJECT-TYPE
	SYNTAX	   DisplayString (SIZE(0|2))
	MAX-ACCESS read-write
	STATUS	   current
	DESCRIPTION 
		"Default Country Code."
	DEFVAL	{ "OT" }
	::= { wirelessDevice 3 }

wirelessSmartAntennaEnabled	OBJECT-TYPE
	SYNTAX	   Integer32 (0|1)
	MAX-ACCESS read-write
	STATUS	   current
	DESCRIPTION 
		"Enable/Disable SmartAntenna"
	DEFVAL	{ 0 }
	::= { wirelessDevice 4 }

wirelessAPForcedSector  OBJECT-TYPE
	SYNTAX     Integer32 (0|1|2)
	MAX-ACCESS read-write
	STATUS     current
	DESCRIPTION 
		"Enable/Disable Forcing of Sector/Smart Antenna for all SMs.
		0 - auto mode (default)
		1 - force sector antenna
		2 - force Smart antenna
		Device Allocation: AP"
	DEFVAL  { 0 }
	::= { wirelessDevice 5 }

wirelessSTAForcedSector  OBJECT-TYPE
    SYNTAX     Integer32 (0|1|2)
    MAX-ACCESS read-write
    STATUS     current
    DESCRIPTION 
        "Enable/Disable Forcing of Sector/Smart Antenna for current SM.
        0 - auto mode (default)
        1 - force sector antenna
        2 - force Smart antenna
        Device Allocation: STA"
    DEFVAL  { 0 }
    ::= { wirelessDevice 6 }

wirelessInterfaceMode  OBJECT-TYPE
	SYNTAX	   Integer32 (1|2|3)
	MAX-ACCESS read-write
	STATUS	   current
	DESCRIPTION 
		"Wireless Interface Mode:
			1 for AP, 
			2 for SM, 
			3 for Spectrum Analyzer
		Device Allocation: AP, SM"
	::= { wirelessInterface 1 }

wirelessInterfaceSSID  OBJECT-TYPE
	SYNTAX	   DisplayString (SIZE(1..32))
	MAX-ACCESS read-write
	STATUS	   current
	DESCRIPTION 
		"Wireless SSID
		Device Allocation: AP"
	DEFVAL	{ "Cambium-AP" }
	::= { wirelessInterface 2 }

wirelessInterfaceEncryption	 OBJECT-TYPE
	SYNTAX	   Integer32 (1|2|3)
	MAX-ACCESS read-write
	STATUS	   current
	DESCRIPTION 
		"Wireless authentication type:
			1 - Open mode,
			2 - wpa2 mode,
			3 - EAP-TTLS
		Device Allocation: AP"
	DEFVAL	{ 2 }
	::= { wirelessInterface 3 }

wirelessInterfaceEncryptionKey	OBJECT-TYPE
	SYNTAX	   DisplayString (SIZE(0|8..63))
	MAX-ACCESS read-write
	STATUS	   current
	DESCRIPTION 
		"Pre-shared authentication key.
		Device Allocation: AP"
	DEFVAL	{ "Cam39-Tai!wdmv" }
	::= { wirelessInterface 4 }

wirelessInterfaceHTMode	 OBJECT-TYPE
	SYNTAX	   Integer32 (1..5)
	MAX-ACCESS read-write
	STATUS	   current
	DESCRIPTION 
		"Frequency Bandwidth
			1 - 20Mhz, 
			2 - 40Mhz, 
			3 - 10Mhz,
			4 - 5MHz
			5 - 20Mhz (Non HT), 
		Device Allocation: AP"
	DEFVAL	{ 1 }
	::= { wirelessInterface 5 }

wirelessInterfaceTXPower  OBJECT-TYPE
	SYNTAX	   Integer32 (-24..30)
	MAX-ACCESS read-write
	STATUS	   current
	DESCRIPTION 
		"TX Power (Board Output Conducted)
		In the SM mode this parameter can be changed
		only if wirelessTXPowerManualLimit is 1;
		For ePMP Elevate devices low limit is equal -4;
		Device Allocation: AP, SM"
	DEFVAL	{ 7 }
	::= { wirelessInterface 6 }

wirelessInterfaceTDDAntennaGain	 OBJECT-TYPE
	SYNTAX	   Integer32 (0..40)
	MAX-ACCESS read-write
	STATUS	   current
	DESCRIPTION 
		"Antenna Gain
		Device Allocation: AP, SM"
	DEFVAL	{ 16 }
	::= { wirelessInterface 7 }

wirelessInterfaceTDDRatio  OBJECT-TYPE
	SYNTAX	   Integer32 (1|2|3|4)
	MAX-ACCESS read-write
	STATUS	   current
	DESCRIPTION 
		"DL/UL Ratio: 
			1 - 75/25,
			2 - 50/50,
			3 - 30/70,
			4 - Flexible
		Device Allocation: AP"
	DEFVAL	{ 4 }
	::= { wirelessInterface 9 }

wirelessInterfaceTPCTRL	 OBJECT-TYPE
	SYNTAX	   Integer32 (-80..-40)
	MAX-ACCESS read-write
	STATUS	   current
	DESCRIPTION 
		"Set/get target receive level (TRL)
		Device Allocation: AP"
	DEFVAL	{ -60 }
	::= { wirelessInterface 10 }

wirelessInterfaceTPCMode  OBJECT-TYPE
	SYNTAX	   Integer32 (0|1|2)
	MAX-ACCESS read-write
	STATUS	   obsolete
	DESCRIPTION 
		"Power mode selection.
		Values:0 - Disable, 1 - Open Loop, 2 - Close Loop
		When system is in Fixed mode (75/35, 50/50, 30/70), this parameter can only be Close or Open Loop.
		When system is in Flexible mode, this parameter can be either Close Loop, Open Loop or Disable.
		The default TPC mode is Close Loop.
		Device Allocation: AP"
	DEFVAL	{ 2 }
	::= { wirelessInterface 11 }

wirelessInterfacePTPMode  OBJECT-TYPE
		SYNTAX	   Integer32 (0|1|2)
		MAX-ACCESS read-write
		STATUS	   current
		DESCRIPTION
		"PTP Setting
			0 - Off
			1 - Connect First SM,
			2 - MAC Address Limited
		Device Allocation: AP"
		DEFVAL	{ 1 }
		::= { wirelessInterface 12 }

wirelessInterfacePTPMACAddress	OBJECT-TYPE
		SYNTAX	   DisplayString (SIZE(0|11..17))
		MAX-ACCESS read-write
		STATUS	   current
		DESCRIPTION
		"PTP MAC Address
		Device Allocation: AP"
		::= { wirelessInterface 13 }

wirelessInterfaceSyncSource	 OBJECT-TYPE
		SYNTAX	   Integer32 (1|2|3|4)
		MAX-ACCESS read-write
		STATUS	   current
		DESCRIPTION
		"1PPS Sync Source
			1 - GPS,
			2 - CMM4,
			3 - Internal Free Run,
			4 - CMM3
		Device Allocation: AP"
		DEFVAL	{ 3 }
		::= { wirelessInterface 14 }

wirelessInterfaceSyncHoldTime  OBJECT-TYPE
		SYNTAX	   Integer32 (20..864000)
		MAX-ACCESS read-write
		STATUS	   current
		DESCRIPTION
		"GPS Sync Hold Time in seconds
		Device Allocation: AP"
		DEFVAL	{ 30 }
		::= { wirelessInterface 15 }

wirelessInterfaceScanFrequencyListTwenty  OBJECT-TYPE
		SYNTAX	   DisplayString (SIZE(0|1..1064))
		MAX-ACCESS read-write
		STATUS	   current
		DESCRIPTION
		"Scan Frequency List for 20 MHz
		Device Allocation: SM"
		::= { wirelessInterface 16 }

wirelessInterfaceScanFrequencyListForty	 OBJECT-TYPE
		SYNTAX	   DisplayString (SIZE(0|1..1064))
		MAX-ACCESS read-write
		STATUS	   current
		DESCRIPTION
		"Scan Frequency List for 40 MHz
		Device Allocation: SM"
		::= { wirelessInterface 17 }

centerFrequency	 OBJECT-TYPE
	SYNTAX	   Integer32 (0|2407..6420)
	MAX-ACCESS read-write
	STATUS	   current
	DESCRIPTION 
		"Per freq band: 5725 GHz for 5G SKU, 2407 for 2.4G SKU
		Device Allocation: AP"
	::= { wirelessInterface 18 }

dfsAlternative1CenterFrequency	OBJECT-TYPE
	SYNTAX	   Integer32 (0|2407..6420)
	MAX-ACCESS read-write
	STATUS	   current
	DESCRIPTION 
		"Per freq band
		Device Allocation: AP"
	::= { wirelessInterface 19 }

dfsAlternative2CenterFrequency	OBJECT-TYPE
	SYNTAX	   Integer32 (0|2407..6420)
	MAX-ACCESS read-write
	STATUS	   current
	DESCRIPTION 
		"Per freq band
		Device Allocation: AP"
	::= { wirelessInterface 20 }

wirelessMaximumCellSize	 OBJECT-TYPE
		SYNTAX	   Integer32 (0..65)
		MAX-ACCESS read-write
		STATUS	   current
		DESCRIPTION
		"Maximum Cell Size in units
		wirelessCellSizeUnit defines the unit type: 
			1 - Miles 
			2 - Kilometers
		Device Allocation: AP"
	DEFVAL	{ 3 }
		::= { wirelessInterface 21 }

wirelessCellSizeUnit  OBJECT-TYPE
		SYNTAX	   Integer32 (1|2)
		MAX-ACCESS read-write
		STATUS	   current
		DESCRIPTION
		"Maximum Cell Size units:
			1 - Miles
			2 - Kilometers
		Device Allocation: AP"
		::= { wirelessInterface 22 }

wirelessMaximumSTA	OBJECT-TYPE
		SYNTAX	   Integer32 (0|1..120)
		MAX-ACCESS read-write
		STATUS	   current
		DESCRIPTION
		"Maximum Number of SM
		Device Allocation: AP"
		DEFVAL	{ 60 }
		::= { wirelessInterface 23 }

wirelessRadiusTimeout  OBJECT-TYPE
	SYNTAX	   Integer32 (1..20)
	MAX-ACCESS read-write
	STATUS	   current
	DESCRIPTION 
		"RADIUS server response timeout
		Device Allocation: AP"
	DEFVAL	{ 5 }
	::= { wirelessRadius 1 }

wirelessRadiusRetry	 OBJECT-TYPE
	SYNTAX	   Integer32 (0..5)
	MAX-ACCESS read-write
	STATUS	   current
	DESCRIPTION 
		"RADIUS server retry
		Device Allocation: AP"
	DEFVAL	{ 1 }
	::= { wirelessRadius 2 }
	
wirelessRadiusGUIUserAuth  OBJECT-TYPE
	SYNTAX	   Integer32 (0|1|2)
	MAX-ACCESS read-write
	STATUS	   current
	DESCRIPTION 
		"SM GUI User Authentication Option
			0 - Device Local Only
			1 - Remote RADIUS Server Only
			2 - Remote RADIUS Server and Fallback to Local
		Device Allocation: AP"
	DEFVAL	{ 0 }
	::= { wirelessRadius 3 }
	
wirelessRadiusCurrentGUIUserAuth  OBJECT-TYPE
	SYNTAX	   Integer32 (0|1|2)
	MAX-ACCESS read-only
	STATUS	   current
	DESCRIPTION 
		"Current GUI User Authentication Option
			0 - Device Local Only
			1 - Remote RADIUS Server Only
			2 - Remote RADIUS Server and Fallback to Local
		Device Allocation: SM"
	::= { wirelessRadius 4 }
	
wirelessRadiusSeverInfo	 OBJECT-TYPE
	SYNTAX	   DisplayString (SIZE(0..128))
	MAX-ACCESS read-only
	STATUS	   current
	DESCRIPTION 
		"RADIUS server info
		Device Allocation: SM"
	::= { wirelessRadius 5 }
	
wirelessRadiusIdentityStr  OBJECT-TYPE
	SYNTAX	   DisplayString (SIZE(0..128))
	MAX-ACCESS read-write
	STATUS	   current
	DESCRIPTION 
		"Authentication Identity String
		Device Allocation: SM"
	DEFVAL	{ "anonymous" }
	::= { wirelessRadius 6 }

wirelessRadiusIdentityRealm	 OBJECT-TYPE
	SYNTAX	   DisplayString (SIZE(0..128))
	MAX-ACCESS read-write
	STATUS	   current
	DESCRIPTION 
		"Authentication Identity Realm
		Device Allocation: SM"
	DEFVAL	{ "cambiumnetworks.com" }
	::= { wirelessRadius 7 }
	
wirelessRadiusUsername	OBJECT-TYPE
	SYNTAX	   DisplayString (SIZE(1..128))
	MAX-ACCESS read-write
	STATUS	   current
	DESCRIPTION 
		"Authentication Username
		Device Allocation: SM"
	DEFVAL	{ "cambium-station" }
	::= { wirelessRadius 8 }
	
wirelessRadiusPassword	OBJECT-TYPE
	SYNTAX	   DisplayString (SIZE(0..128))
	MAX-ACCESS read-write
	STATUS	   current
	DESCRIPTION 
		"Authentication Password
		Device Allocation: SM"
	DEFVAL	{ "cambium" }
	::= { wirelessRadius 9 }

useMACAddressAsWirelessRadiusUsername  OBJECT-TYPE
	SYNTAX	   Integer32 (0|1|2)
	MAX-ACCESS read-write
	STATUS	   current
	DESCRIPTION 
		"For using an Ethernet MAC address instead of RADIUS username
		0 - Off (default),
		1 - using ':' as format,
		2 - using '-' as format
		Device Allocation: SM"
	DEFVAL	{ 0 }
	::= { wirelessRadius 10 }

wirelessRadiusServerTable  OBJECT-TYPE
		SYNTAX SEQUENCE OF WirelessRadiusServerEntry
		MAX-ACCESS not-accessible
		STATUS	   current
		DESCRIPTION
			"RADIUS servers table
			Device Allocation: AP"
		::= { wirelessRadiusServerList 1 }
		
wirelessRadiusServerEntry  OBJECT-TYPE
		SYNTAX	WirelessRadiusServerEntry
		MAX-ACCESS not-accessible
		STATUS	   current
		DESCRIPTION
			"RADIUS servers table entry
			Device Allocation: AP"
		INDEX	{ wirelessRadiusServerIndex }
		
		::= { wirelessRadiusServerTable 1 }
		
WirelessRadiusServerEntry ::= SEQUENCE {
		wirelessRadiusServerIndex
				Integer32,
		wirelessRadiusServerIP
				IpAddress,
		wirelessRadiusServerPort
				Integer32,
		wirelessRadiusServerSecret
				DisplayString
}

wirelessRadiusServerIndex  OBJECT-TYPE
		SYNTAX	   Integer32 (0..3)
		MAX-ACCESS read-write
		STATUS	   current
		DESCRIPTION
			"RADIUS servers limiting number
			Device Allocation: AP"
		::= { wirelessRadiusServerEntry 1 }
		
wirelessRadiusServerIP	OBJECT-TYPE
		SYNTAX	   IpAddress
		MAX-ACCESS read-write
		STATUS	   current
		DESCRIPTION
			"RADIUS server IP address
			Device Allocation: AP"
		::= { wirelessRadiusServerEntry 2 }
		
wirelessRadiusServerPort  OBJECT-TYPE
		SYNTAX	   Integer32(1..65535)
		MAX-ACCESS read-write
		STATUS	   current
		DESCRIPTION
			"RADIUS server port
			Device Allocation: AP"
		DEFVAL	{ 1812 }
		::= { wirelessRadiusServerEntry 3 }
		
wirelessRadiusServerSecret	OBJECT-TYPE
		SYNTAX	   DisplayString (SIZE(0|1..128))
		MAX-ACCESS read-write
		STATUS	   current
		DESCRIPTION
			"RADIUS server port
			Device Allocation: AP"
		::= { wirelessRadiusServerEntry 4 }
		
wirelessRadiusDefaultCertificate OBJECT-TYPE
		SYNTAX	   OCTET STRING (SIZE(0..8192))
		MAX-ACCESS read-only
		STATUS	   current
		DESCRIPTION
			"Default RADIUS certificate
			Device Allocation: SM"
		::= { wirelessRadiusCertificateSet 1 }
		
wirelessRadiusUser1Certificate OBJECT-TYPE
		SYNTAX	   OCTET STRING (SIZE(0|1..8192))
		MAX-ACCESS read-write
		STATUS	   current
		DESCRIPTION
			"Default RADIUS certificate
			Device Allocation: SM"
		::= { wirelessRadiusCertificateSet 2 }
		
wirelessRadiusUser2Certificate OBJECT-TYPE
		SYNTAX	   OCTET STRING (SIZE(0|1..8192))
		MAX-ACCESS read-write
		STATUS	   current
		DESCRIPTION
			"Default RADIUS certificate
			Device Allocation: SM"
		::= { wirelessRadiusCertificateSet 3 }
		
wirelessRadiusUseDefaultCertificate	 OBJECT-TYPE
		SYNTAX	   Integer32(0|1)
		MAX-ACCESS read-write
		STATUS	   current
		DESCRIPTION
			"RADIUS default certificate use
			Device Allocation: SM"
		DEFVAL	{ 1 }
		::= { wirelessRadiusCertificateSet 4 }
		
wirelessRadiusPMP320Certificate OBJECT-TYPE
		SYNTAX	   OCTET STRING (SIZE(0..8192))
		MAX-ACCESS read-only
		STATUS	   current
		DESCRIPTION
			"PMP320 RADIUS certificate
			Device Allocation: SM"
		::= { wirelessRadiusExtraCertificateSet 1 }
		
wirelessRadiusUsePMP320Certificate	OBJECT-TYPE
		SYNTAX	   Integer32(0|1)
		MAX-ACCESS read-write
		STATUS	   current
		DESCRIPTION
			"RADIUS PMP320 certificate use
			Device Allocation: SM"
		DEFVAL	{ 1 }
		::= { wirelessRadiusExtraCertificateSet 2 }
		
wirelessRadiusPMP450Certificate OBJECT-TYPE
		SYNTAX	   OCTET STRING (SIZE(0..8192))
		MAX-ACCESS read-only
		STATUS	   current
		DESCRIPTION
			"PMP450 RADIUS certificate
			Device Allocation: SM"
		::= { wirelessRadiusExtraCertificateSet 3 }
		
wirelessRadiusUsePMP450Certificate	OBJECT-TYPE
		SYNTAX	   Integer32(0|1)
		MAX-ACCESS read-write
		STATUS	   current
		DESCRIPTION
			"RADIUS PMP450 certificate use
			Device Allocation: SM"
		DEFVAL	{ 1 }
		::= { wirelessRadiusExtraCertificateSet 4 }

wirelessRadiusUseDefCertificate	 OBJECT-TYPE
		SYNTAX	   Integer32(0|1)
		MAX-ACCESS read-write
		STATUS	   obsolete
		DESCRIPTION
			"RADIUS default certificate use
			Device Allocation: SM"
		DEFVAL	{ 1 }
		::= { wirelessRadiusCertificateListRow1 1 }

wirelessRadiusUser1CertificateName	OBJECT-TYPE
		SYNTAX	   DisplayString
		MAX-ACCESS read-write
		STATUS	   obsolete
		DESCRIPTION
			"First user RADIUS certificate name
			Device Allocation: AP"
		DEFVAL	{ "cert2" }
		::= { wirelessRadiusCertificateListRow2 1 }

wirelessRadiusUser2CertificateName	OBJECT-TYPE
		SYNTAX	   DisplayString
		MAX-ACCESS read-write
		STATUS	   obsolete
		DESCRIPTION
			"Second user RADIUS certificate name
			Device Allocation: AP"
		DEFVAL	{ "cert3" }
		::= { wirelessRadiusCertificateListRow3 1 }

wirelessRadiusDefCertificateView  OBJECT-TYPE
		SYNTAX	   DisplayString
		MAX-ACCESS read-only
		STATUS	   obsolete
		DESCRIPTION
			"RADIUS default certificate view
			Device Allocation: AP"
		::= { wirelessRadiusCertificateListRow1 2 }

wirelessRadiusUser1CertificateView	OBJECT-TYPE
		SYNTAX	   DisplayString
		MAX-ACCESS read-only
		STATUS	   obsolete
		DESCRIPTION
			"First user RADIUS certificate view
			Device Allocation: AP"
		::= { wirelessRadiusCertificateListRow2 2 }

wirelessRadiusUser2CertificateView	OBJECT-TYPE
		SYNTAX	   DisplayString
		MAX-ACCESS read-only
		STATUS	   obsolete
		DESCRIPTION
			"Second user RADIUS certificate view
			Device Allocation: AP"
		::= { wirelessRadiusCertificateListRow3 2 }
		
dfsAlternative1Bandwidth  OBJECT-TYPE
	SYNTAX	   Integer32 (1|2|3|4)
	MAX-ACCESS read-write
	STATUS	   current
	DESCRIPTION 
		"Frequency Bandwidth
			1 - 20Mhz, 
			2 - 40Mhz, 
			3 - 10Mhz, 
			4 - 5Mhz, 
		Device Allocation: AP"
	DEFVAL	{ 1 }
	::= { wirelessInterface 24 }

dfsAlternative2Bandwidth  OBJECT-TYPE
	SYNTAX	   Integer32 (1|2|3|4)
	MAX-ACCESS read-write
	STATUS	   current
	DESCRIPTION 
		"Frequency Bandwidth
			1 - 20Mhz, 
			2 - 40Mhz, 
			3 - 10Mhz, 
			4 - 5Mhz, 
		Device Allocation: AP"
	DEFVAL	{ 1 }
	::= { wirelessInterface 25 }

wirelessAcceptableAPRSSIThreshold  OBJECT-TYPE
		SYNTAX	   Integer32 (-100..-20)
		MAX-ACCESS read-write
		STATUS	   current
		DESCRIPTION
		"AP RSSI Threshold
		Device Allocation: SM"
		DEFVAL	{ -90 }
		::= { wirelessInterface 26 }
		
wirelessAcceptableAPCINRThreshold  OBJECT-TYPE 
		SYNTAX	   Integer32 (-5..60)
		MAX-ACCESS read-write
		STATUS	   obsolete
		DESCRIPTION
		"AP CINR Threshold
		Device Allocation: SM"
		DEFVAL	{ 0 }
		::= { wirelessInterface 27 }

wirelessInterfaceUnblockUSfreqs	 OBJECT-TYPE
		SYNTAX	   Integer32 (0|1)
		MAX-ACCESS read-write
		STATUS	   obsolete
		DESCRIPTION
		"Block US 5.2 and 5.4 bands
		5.2 and 5.4 bands are blocked until DFS certification is acheived
		Device Allocation: AP, SM"
		::= { wirelessInterface 28 }

wirelessMIREnable  OBJECT-TYPE
		SYNTAX	   Integer32 (0|1)
		MAX-ACCESS read-write
		STATUS	   current
		DESCRIPTION
		"Maximum Information Rate (MIR) Limiting:
			0 - Disable,
			1 - Enable
		Device Allocation: AP"
		DEFVAL	{ 0 }
		::= { wirelessInterface 29 }

wirelessMIRSTAProfileNumber	 OBJECT-TYPE
		SYNTAX	   Integer32 (0..15)
		MAX-ACCESS read-write
		STATUS	   current
		DESCRIPTION
		"Maximum Information Rate (MIR) Limiting Profile Number on SM
		Device Allocation: SM"
		::= { wirelessInterface 30 }

wirelessMIRAPDefaultProfileNumber  OBJECT-TYPE
		SYNTAX	   Integer32 (0..15)
		MAX-ACCESS read-write
		STATUS	   current
		DESCRIPTION
		"Maximum Information Rate (MIR) Limiting Default Profile number on AP
		This Profile Number will be used by AP is SM provides improper profile
		Device Allocation: AP"
		::= { wirelessInterface 31 }

wirelessMIRProfileTable	 OBJECT-TYPE
		SYNTAX SEQUENCE OF WirelessMIRProfileEntry
		MAX-ACCESS not-accessible
		STATUS	   current
		DESCRIPTION
		"Maximum Information Rate (MIR) Limiting profile Table
		Device Allocation: AP"
		::= { wirelessMIRList 1 }

wirelessMIRProfileEntry	 OBJECT-TYPE
		SYNTAX	WirelessMIRProfileEntry
		MAX-ACCESS not-accessible
		STATUS	   current
		DESCRIPTION
		"Maximum Information Rate (MIR) Limiting profile Table Entry
		Device Allocation: AP"
		INDEX	{ wirelessMIRProfileIndex }
		::= { wirelessMIRProfileTable 1 }

WirelessMIRProfileEntry ::= SEQUENCE {
		wirelessMIRProfileIndex
				Integer32,
		wirelessMIRProfileNumber
				Integer32,
		wirelessMIRProfileDescription
				DisplayString,
		wirelessDLMIR
				Integer32,
		wirelessULMIR
				Integer32
}

wirelessMIRProfileIndex	 OBJECT-TYPE
		SYNTAX	   Integer32 (0..16)
		MAX-ACCESS read-write
		STATUS	   current
		DESCRIPTION
		"Maximum Information Rate (MIR) Limiting profile Number
		Device Allocation: AP"
		::= { wirelessMIRProfileEntry 1 }

wirelessMIRProfileNumber  OBJECT-TYPE
		SYNTAX	   Integer32 (0..15)
		MAX-ACCESS read-write
		STATUS	   current
		DESCRIPTION
		"Number of MIR profile
		Device Allocation: AP"
		::= { wirelessMIRProfileEntry 2 }

wirelessMIRProfileDescription  OBJECT-TYPE
		SYNTAX	   DisplayString (SIZE(0|1..128))
		MAX-ACCESS read-write
		STATUS	   current
		DESCRIPTION
		"MIR profile description
		Device Allocation: AP"
		::= { wirelessMIRProfileEntry 3 }


wirelessDLMIR  OBJECT-TYPE
		SYNTAX	   Integer32 (100..1000000)
		MAX-ACCESS read-write
		STATUS	   current
		DESCRIPTION
		"DL MIR in kilobits per second
		Device Allocation: AP"
		::= { wirelessMIRProfileEntry 4 }

wirelessULMIR  OBJECT-TYPE
		SYNTAX	   Integer32 (100..1000000)
		MAX-ACCESS read-write
		STATUS	   current
		DESCRIPTION
		"UL MIR in kilobits per second
		Device Allocation: AP"
		::= { wirelessMIRProfileEntry 5 }

wirelessInterfaceScanFrequencyBandwidth OBJECT-TYPE
	SYNTAX	   Integer32 (1..15)
	MAX-ACCESS read-write
	STATUS	   current
	DESCRIPTION 
		"Frequency Bandwidth as bitmask, fields are:
			1 - 20Mhz, 
			2 - 40Mhz, 
			4 - 10Mhz, 
			8 - 5Mhz
		Device Allocation: SM"
	DEFVAL	{ 1 }
	::= { wirelessInterface 32 }

wirelessInterfaceGuardInterval OBJECT-TYPE
		SYNTAX Integer32 (1|2)
		MAX-ACCESS read-write
		STATUS	   current
		DESCRIPTION
		"Guard Interval:
			1 - Long GuardInterval,
			2 - Short GuardInterval
		Device Allocation: AP"
		DEFVAL	{ 1 }
	::= { wirelessInterface 33 }

wirelessInterfaceiFreqReuseMode OBJECT-TYPE
			SYNTAX Integer32 (0|1|2)
		MAX-ACCESS read-write
		STATUS	   current
		DESCRIPTION
		"Frequency Reuse Mode:
			0 - Off,
			1 - Frequency-Reuse-Front,
			2 - Frequency-Reuse-Back
		Device Allocation: AP"
		DEFVAL	{ 0 }
		::= { wirelessInterface 34 }
		
wirelessSTAPriority	 OBJECT-TYPE
		SYNTAX	   Integer32 (0|1|2)
		MAX-ACCESS read-write
		STATUS	   current
		DESCRIPTION
		"SM priority value:
			0 - Normal,
			1 - High,
			2 - Low
		Device Allocation: SM"
		DEFVAL	{ 0 }
		::= { wirelessInterface 35 }

wirelessSmoothingBit  OBJECT-TYPE
		SYNTAX	   Integer32 (0|1)
		MAX-ACCESS read-write
		STATUS	   obsolete
		DESCRIPTION
		"Smoothing Bit values:
			0 - Bit is cleared, smoothing is off,
			1 - Bit is set, smoothing is on
		Device Allocation: AP"
		DEFVAL	{ 0 }
		::= { wirelessInterface 36 }
		
wirelessSecurityMethod	OBJECT-TYPE
		SYNTAX	   Integer32 (0..6)
		MAX-ACCESS read-write
		STATUS	   current
		DESCRIPTION
				"Allowed types of authentications on SM side
				(Preferred AP list is not set)
				Use bitmask to enable pereferred methods, 0 - means enable method:
				set 0-th bit to 0 - Open method (110b)
				set 1-st bit to 0 - WPA2 method (101b)
				set 2-nd bit to 0 - EAP-TTLS method (011b)
				0x00 - All enabled"
		DEFVAL	{ 0 }
		::= { wirelessInterface 37 }

wirelessAcceptableAPSNRThreshold  OBJECT-TYPE
		SYNTAX	   Integer32 (-5..60)
		MAX-ACCESS read-write
		STATUS	   current
		DESCRIPTION
		"AP CINR Threshold
		Device Allocation: SM"
		DEFVAL	{ 0 }
		::= { wirelessInterface 38 }

wirelessMgmtPacketRate	OBJECT-TYPE
		SYNTAX	   Integer32 (0|1)
		MAX-ACCESS read-write
		STATUS	   current
		DESCRIPTION
		"Management rate:
			0 - MCS0
			1 - MCS1
		Device Allocation: AP"
		DEFVAL	{ 1 }
		::= { wirelessInterface 39 }

wirelessStaIsolate	OBJECT-TYPE
		SYNTAX	   Integer32 (0|1)
		MAX-ACCESS read-write
		STATUS	   current
		DESCRIPTION
		"Enables or disables bridging within the AP driver
		between SMs.
			0 - Disabled
			1 - Enabled
		Device Allocation: AP"
		DEFVAL	{ 0 }
		::= { wirelessInterface 40 }

wirelessCcaEnable	OBJECT-TYPE
		SYNTAX		Integer32 (0|1)
		MAX-ACCESS	read-write
		STATUS		current
		DESCRIPTION
		"Clear Channel Assignment:
			0 - Disable
			1 - Enable
		Device Allocation: AP"
		DEFVAL	{ 0 }
		::= { wirelessInterface 41 }

wirelessInterfaceScanFrequencyListTen  OBJECT-TYPE
		SYNTAX	   DisplayString (SIZE(0|1..1064))
		MAX-ACCESS read-write
		STATUS	   current
		DESCRIPTION
		"Scan Frequency List for 10MHz
		Device Allocation: SM"
		::= { wirelessInterface 42 }

wirelessInterfaceScanFrequencyListFive	OBJECT-TYPE
		SYNTAX	   DisplayString (SIZE(0|1..1064))
		MAX-ACCESS read-write
		STATUS	   current
		DESCRIPTION
		"Scan Frequency List for 5MHz
		Device Allocation: SM"
		::= { wirelessInterface 43 }

wirelessMulticastEnhanceMode  OBJECT-TYPE
		SYNTAX	   Integer32 (0|3)
		MAX-ACCESS read-write
		STATUS	   current
		DESCRIPTION
		"Multicast enhancement mode 
			0 - Disabled
			3 - IGMP Snooping + MC Passthru
		Device Allocation: AP"
		DEFVAL	{ 0 }
		::= { wirelessInterface 44 }

wirelessTXPowerManualLimit	OBJECT-TYPE
	SYNTAX	   Integer32 (0|1)
	MAX-ACCESS read-write
	STATUS	   current
	DESCRIPTION 
		"Allow user to limit MAX output TX Power
		Device Allocation: SM"
	DEFVAL	{ 0 }
	::= { wirelessInterface 48 }

wirelessRateMaxMCS OBJECT-TYPE
	SYNTAX	   Integer32 (1..15)
	MAX-ACCESS read-write
	STATUS	   current
	DESCRIPTION 
		"Allow user to set MAX TX rate
		Not allowed for SNMP processing
		Device Allocation: AP, SM"
	::= { wirelessInterface 49 }

wirelessSMWifiDistance	OBJECT-TYPE
		SYNTAX	   Integer32 (1..52)
		MAX-ACCESS read-write
		STATUS	   current
		DESCRIPTION
		"Distance to AP for SM in Standard Wi-Fi mode
		wirelessCellSizeUnitdefines the unit type:
			1 - Miles
			2 - Kilometers
		Device Allocation: SM"
	DEFVAL	{ 1 }
		::= { wirelessInterface 50 }

wirelessInterfaceProtocolMode  OBJECT-TYPE
		SYNTAX	   Integer32 (1|2|3|4)
		MAX-ACCESS read-write
		STATUS	   current
		DESCRIPTION
	   "Protocol Module Mode:
		   1 - TDD
		   2 - AP/SM WiFi
		   3 - PTP.LL
		   4 - TDD PTP
	   Device Allocation: AP/SM"
   DEFVAL  { 1 }
		::= { wirelessInterface 51 }
wirelessClientBridgeMode OBJECT-TYPE
		SYNTAX Integer32 (0|1)
		MAX-ACCESS read-write
		STATUS     current
		DESCRIPTION
		"Enables ARPNAT feature, translates ARP requests from Ethernet side of SM to Wireless and vice-versa:
			0 - Disabled
			1 - Enabled
           Device Allocation: SM"
   DEFVAL  { 0 }
                ::= { wirelessInterface 52 }

forceMcastBcast4Addr  OBJECT-TYPE
		SYNTAX	   Integer32 (0|1)
		MAX-ACCESS read-write
		STATUS	   current
		DESCRIPTION
	   "1 - TRUE
		0 - FALSE"
   DEFVAL  { 1 }
		::= { wirelessInterface 53 }

wirelessInterfaceRateMinMCS	 OBJECT-TYPE
		SYNTAX	   Integer32 (0..15)
		MAX-ACCESS read-write
		STATUS	   current
		DESCRIPTION
		"Minimum locked MCS rate.
		Default allocation: AP, SM."
		DEFVAL	{ 0 }
		::= { wirelessInterface 55 }

wirelessInterfaceRateMaxMCS  OBJECT-TYPE
        SYNTAX     Integer32 (0..15)
        MAX-ACCESS read-write
        STATUS     current
        DESCRIPTION
        "Maximum locked MCS rate.
        Default allocation: AP, SM."
        DEFVAL  { 15 }
        ::= { wirelessInterface 56 }

wirelessMulticastIgmpFastLeave  OBJECT-TYPE
        SYNTAX     Integer32 (0|1)
        MAX-ACCESS read-write
        STATUS     current
        DESCRIPTION
        "Multicast enhancement mode 
            0 - IGMP Fast Leave OFF
            1 - IGMP Fast Leave ON
        Device Allocation: AP"
        DEFVAL  { 0 }
        ::= { wirelessInterface 57 }

wirelessInterfaceTDDFrameSize  OBJECT-TYPE
		SYNTAX     Integer32 (2500|5000)
		MAX-ACCESS read-write
		STATUS     current
		DESCRIPTION
		"TDD Frame Duration in microseconds
			2500 - 2.5 ms
			5000 - 5 ms
		Device Allocation: AP"
		DEFVAL  { 5000 }
		::= { wirelessInterface 58 }

wirelessInterfaceColocState  OBJECT-TYPE
		SYNTAX     Integer32 (0|1)
		MAX-ACCESS read-write
		STATUS     current
		DESCRIPTION
		"Co-location state
			0 - disabled
			1 - FSK co-location
		Device Allocation: AP"
		DEFVAL  { 0 }
		::= { wirelessInterface 59 }

wirelessInterfaceColocSystemSyncSrc  OBJECT-TYPE
		SYNTAX     Integer32 (1|2|4)
		MAX-ACCESS read-write
		STATUS     current
		DESCRIPTION
		"Co-location state
			1 - GPS,
			2 - CMM4,
			4 - CMM3
		Device Allocation: AP"
		DEFVAL  { 2 }
		::= { wirelessInterface 60 }

wirelessAPWifiWLANmode  OBJECT-TYPE
                SYNTAX     Integer32 (0|1)
                MAX-ACCESS read-write
                STATUS     current
                DESCRIPTION
                "AP Wi-Fi WLAN mode (short, 1000m operational distance)
                        0 - Disabled,
                        1 - Enabled
                Device Allocation: AP"
                DEFVAL  { 0 }
                ::= { wirelessInterface 61 }

apWiFiDLCTSMode  OBJECT-TYPE
                SYNTAX     Integer32 (0|1)
                MAX-ACCESS read-write
                STATUS     current
                DESCRIPTION
                "Force AP WiFi to enable Self CTS
                        0 - Disabled,
                        1 - Enabled
                Device Allocation: AP"
                DEFVAL  { 1 }
                ::= { wirelessInterface 62 }

apWiFiULCTSRTSMode  OBJECT-TYPE
                SYNTAX     Integer32 (0|1)
                MAX-ACCESS read-write
                STATUS     current
                DESCRIPTION
                "Force AP WiFi to add ERP IE to the Beacon
                        0 - Disabled,
                        1 - Enabled
                Device Allocation: AP"
                DEFVAL  { 1 }
                ::= { wirelessInterface 63 }

apWiFiRTSThreshold  OBJECT-TYPE
                SYNTAX     Integer32 (1..2346)
                MAX-ACCESS read-write
                STATUS     current
                DESCRIPTION
                "Wi-Fi interface RTS Threshold
                Device Allocation: AP, SM"
                DEFVAL  { 2346 }
                ::= { wirelessInterface 64 }
apWiFiCompWDSTrBridge  OBJECT-TYPE
                SYNTAX     Integer32 (0|1)
                MAX-ACCESS read-write
                STATUS     current
                DESCRIPTION
                "AP Wi-Fi WDS Transparent bridge mode 
                Compatibility mode for Ubiquity WDS Transparent bridge 
                and Mikrotik station wds
                        0 - Disabled,
                        1 - Enabled
                Device Allocation: AP"
                DEFVAL  { 1 }
                ::= { wirelessInterface 65 }

wirelessFreqShift  OBJECT-TYPE
		SYNTAX	   Integer32 (0..50)
		MAX-ACCESS read-write
		STATUS	   current
		DESCRIPTION
		"Freq shift in 0.1 Mhz units:
			Range: 0..50 (0..5Mhz)
		Device Allocation: AP, STA"
		DEFVAL	{ 0 }
		::= { wirelessInterface 66 }

wirelessMACFilter  OBJECT-TYPE
		SYNTAX     Integer32 (0|1)
		MAX-ACCESS read-write
		STATUS     current
		DESCRIPTION
		"Enable/Disable MAC list filter
			0 - Disabled,
			1 - Enabled
		Device Allocation: AP"
		DEFVAL  { 0 }
		::= { wirelessInterface 70 }

wirelessMACFilterPolicy  OBJECT-TYPE
		SYNTAX     Integer32 (1|2)
		MAX-ACCESS read-write
		STATUS     current
		DESCRIPTION
		"Permit/Prevent policy for MAC list
			1 - Prevent
			2 - Permit
		Device Allocation: AP"
		DEFVAL  { 1 }
		::= { wirelessInterface 71 }
		
wirelessMACFilterTable	 OBJECT-TYPE
	SYNTAX SEQUENCE OF WirelessMACFilterEntry
	MAX-ACCESS not-accessible
	STATUS	   current
	DESCRIPTION 
		"Table for MAC filter list
		Device Allocation: AP"
	::= { wirelessInterface 72 }

wirelessMACFilterEntry	 OBJECT-TYPE
	SYNTAX	WirelessMACFilterEntry
	MAX-ACCESS not-accessible
	STATUS	   current
	DESCRIPTION 
		"L2 ACL Table Entry
		Device Allocation: AP"
	INDEX	{ wirelessMACFilterIndex }
	::= { wirelessMACFilterTable 1 }
	
WirelessMACFilterEntry ::= SEQUENCE {
	wirelessMACFilterIndex
		Integer32,
	wirelessFilterMAC
		DisplayString,
	wirelessFilterInfo
		DisplayString
}

wirelessMACFilterIndex  OBJECT-TYPE
		SYNTAX	   Integer32 (0..128)
		MAX-ACCESS read-write
		STATUS	   current
		DESCRIPTION
		"MAC filter list table Index(equal max STA)
		Table Entry is cleared if Index is set to zero
		Device Allocation: AP"
		::= { wirelessMACFilterEntry 1 }

wirelessFilterMAC	 OBJECT-TYPE
		SYNTAX	   DisplayString (SIZE(0|1..128))
		MAX-ACCESS read-write
		STATUS	   current
		DESCRIPTION
		"MAC of SM for filter table
		Device Allocation: AP"
		::= { wirelessMACFilterEntry 2 }
		
wirelessFilterInfo	 OBJECT-TYPE
		SYNTAX	   DisplayString (SIZE(0|1..128))
		MAX-ACCESS read-write
		STATUS	   current
		DESCRIPTION
		"Description for MAC in the filter table
		Device Allocation: AP"
		::= { wirelessMACFilterEntry 3 }

l2FirewallEnable  OBJECT-TYPE
		SYNTAX	   Integer32 (0|1)
		MAX-ACCESS read-write
		STATUS	   current
		DESCRIPTION
		"L2 ACL Status Flag: 
			0 - Disable, 
			1 - Enable.
		Device Allocation: AP, SM"
		::= { l2Firewall 1 }

l2FirewallTable	 OBJECT-TYPE
	SYNTAX SEQUENCE OF L2FirewallEntry
	MAX-ACCESS not-accessible
	STATUS	   current
	DESCRIPTION 
		"Table for L2 ACL
		Device Allocation: AP, SM"
	::= { l2Firewall 2 }

l2FirewallEntry	 OBJECT-TYPE
	SYNTAX	L2FirewallEntry
	MAX-ACCESS not-accessible
	STATUS	   current
	DESCRIPTION 
		"L2 ACL Table Entry
		Device Allocation: AP, SM"
	INDEX	{ l2FirewallEntryIndex }
	::= { l2FirewallTable 1 }

L2FirewallEntry ::= SEQUENCE {
	l2FirewallEntryIndex
		Integer32,
	l2FirewallEntryName
		DisplayString,
	l2FirewallEntryAction
		Integer32,
	l2FirewallEntryInterface
		Integer32,
	l2FirewallEntryLog
		Integer32,
	l2FirewallEntryEtherType
		Integer32,
	l2FirewallEntryVlanID
		Integer32,
	l2FirewallEntrySrcMAC
		DisplayString,
	l2FirewallEntrySrcMask
		DisplayString,
	l2FirewallEntryDstMAC
		DisplayString,
	l2FirewallEntryDstMask
		DisplayString
}

l2FirewallEntryIndex  OBJECT-TYPE
		SYNTAX	   Integer32 (0..16)
		MAX-ACCESS read-write
		STATUS	   current
		DESCRIPTION
		"L2 Firewall Table Index
		Table Entry is cleared if Index is set to zero
		Device Allocation: AP, SM"
		::= { l2FirewallEntry 1 }

l2FirewallEntryName	 OBJECT-TYPE
		SYNTAX	   DisplayString (SIZE(0|1..128))
		MAX-ACCESS read-write
		STATUS	   current
		DESCRIPTION
		"L2 ACL Rule Name.
		Device Allocation: AP, SM"
		::= { l2FirewallEntry 2 }

l2FirewallEntryAction  OBJECT-TYPE
	SYNTAX	   Integer32 (0|1)
	MAX-ACCESS read-write
	STATUS	   current
	DESCRIPTION 
		"Action:
			0 - Reject, 
			1 - Permit.
		Device Allocation: AP, SM"
	::= { l2FirewallEntry 3 }

l2FirewallEntryInterface  OBJECT-TYPE
	SYNTAX	   Integer32 (0|1|2)
	MAX-ACCESS read-write
	STATUS	   current
	DESCRIPTION 
		"Interface:
			1 - WAN, 
			2 - LAN.
		Device Allocation: AP, SM"
	::= { l2FirewallEntry 4 }

l2FirewallEntryLog	OBJECT-TYPE
	SYNTAX	   Integer32 (0|1)
	MAX-ACCESS read-write
	STATUS	   current
	DESCRIPTION 
		"Log:
			1 - On, 
			0 - Off.
		Device Allocation: AP, SM"
	::= { l2FirewallEntry 5 }

l2FirewallEntryEtherType  OBJECT-TYPE
	SYNTAX	   Integer32 (0..65535)
	MAX-ACCESS read-write
	STATUS	   current
	DESCRIPTION 
		"L2 ACL Ethernet type: 0000-ffff
		Device Allocation: AP, SM"
	::= { l2FirewallEntry 6 }

l2FirewallEntryVlanID  OBJECT-TYPE
	SYNTAX	   Integer32 (0|1..4094)
	MAX-ACCESS read-write
	STATUS	   current
	DESCRIPTION 
		"L2 ACL Vlan ID
		Device Allocation: AP, SM"
	::= { l2FirewallEntry 7 }

l2FirewallEntrySrcMAC  OBJECT-TYPE
	SYNTAX	   DisplayString (SIZE(0|11..17))
	MAX-ACCESS read-write
	STATUS	   current
	DESCRIPTION 
		"L2 ACL Source MAC Address
		Device Allocation: AP, SM"
	::= { l2FirewallEntry 8 }

l2FirewallEntrySrcMask	OBJECT-TYPE
	SYNTAX	   DisplayString (SIZE(0|11..17))
	MAX-ACCESS read-write
	STATUS	   current
	DESCRIPTION 
		"L2 ACL Source MAC Address Mask
		Device Allocation: AP, SM"
	::= { l2FirewallEntry 9 }

l2FirewallEntryDstMAC  OBJECT-TYPE
	SYNTAX	   DisplayString (SIZE(0|11..17))
	MAX-ACCESS read-write
	STATUS	   current
	DESCRIPTION 
		"L2 ACL Destination MAC Address
		Device Allocation: AP, SM"
	::= { l2FirewallEntry 10 }

l2FirewallEntryDstMask	OBJECT-TYPE
	SYNTAX	   DisplayString (SIZE(0|11..17))
	MAX-ACCESS read-write
	STATUS	   current
	DESCRIPTION 
		"L2 ACL Destination MAC Address Mask
		Device Allocation: AP, SM"
	::= { l2FirewallEntry 11 }

l2WanRemoteAccess  OBJECT-TYPE
		SYNTAX	   Integer32 (0|1)
		MAX-ACCESS read-write
		STATUS	   current
		DESCRIPTION
		"Remote Access To AP Through Wan:
			0 - Decline, 
			1 - Allow
		Device Allocation: AP, SM"
		DEFVAL	{ 0 }
		::= { l2Firewall 3 }

l2SnmpLanRemoteAccess  OBJECT-TYPE
		SYNTAX	   Integer32 (0|1)
		MAX-ACCESS read-write
		STATUS	   current
		DESCRIPTION
		"SNMP access from LAN:
			0 - Decline, 
			1 - Allow
		Device Allocation: AP, SM"
		DEFVAL	{ 1 }
		::= { l2Firewall 4 }

l2DHCPServersBelowSTA  OBJECT-TYPE
		SYNTAX	   Integer32 (0|1)
		MAX-ACCESS read-write
		STATUS	   current
		DESCRIPTION
		"Allow DHCP Servers Below SM:
			0 - Decline, 
			1 - Allow
		Device Allocation: SM"
		DEFVAL	{ 0 }
		::= { l2Firewall 5 }

l2LanRemoteAccess  OBJECT-TYPE
        SYNTAX     Integer32 (0|1)
        MAX-ACCESS read-write
        STATUS     current
        DESCRIPTION
		"SM Management Access Through LAN:
			0 - Wireless Only,
			1 - Ethernet and Wireless
		Device Allocation: SM"
        DEFVAL  { 0 }
        ::= { l2Firewall 6 }

l3FirewallEnable  OBJECT-TYPE
		SYNTAX	   Integer32 (0|1)
		MAX-ACCESS read-write
		STATUS	   current
		DESCRIPTION
		"L3 ACL Rule Status
			1 - Enable, 
			0 - Disable
		Device Allocation: AP, SM"
		::= { l3Firewall 1 }
		
l3FirewallTable	 OBJECT-TYPE
	SYNTAX SEQUENCE OF L3FirewallEntry
	MAX-ACCESS not-accessible
	STATUS	   current
	DESCRIPTION 
		"L3 Firewall Table
		Device Allocation: AP, SM"
	::= { l3Firewall 2 }

l3FirewallEntry	 OBJECT-TYPE
	SYNTAX	L3FirewallEntry
	MAX-ACCESS not-accessible
	STATUS	   current
	DESCRIPTION 
		"L3 Firewall Table Entry
		Device Allocation: AP, SM"
	INDEX	{ l3FirewallEntryIndex }
	::= { l3FirewallTable 1 }

L3FirewallEntry ::= SEQUENCE {
	l3FirewallEntryIndex
		Integer32,
	l3FirewallEntryName
		DisplayString,
	l3FirewallEntryAction
		Integer32,
	l3FirewallEntryInterface
		Integer32,
	l3FirewallEntryLog
		Integer32,
	l3FirewallEntryProtocol
		Integer32,
	l3FirewallEntryPort
		Integer32,
	l3FirewallEntrySrcIP
		IpAddress,
	l3FirewallEntrySrcMask
		IpAddress,
	l3FirewallEntryDstIP
		IpAddress,
	l3FirewallEntryDstMask
		IpAddress,
	l3FirewallEntryDSCP
		Integer32,
	l3FirewallEntryToS
		Integer32,
	l3FirewallEntrySrcPort
		Integer32
}

l3FirewallEntryIndex  OBJECT-TYPE
		SYNTAX	   Integer32 (0..16)
		MAX-ACCESS read-write
		STATUS	   current
		DESCRIPTION
		"L3 ACL Table Index
		Table Entry is cleared if Index is set to zero
		Device Allocation: AP, SM"
		::= { l3FirewallEntry 1 }

l3FirewallEntryName	 OBJECT-TYPE
	SYNTAX	   DisplayString(SIZE(0|1..128))
	MAX-ACCESS read-write
	STATUS	   current
	DESCRIPTION 
		"L3 ACL Rule Name
		Device Allocation: AP, SM"
	::= { l3FirewallEntry 2 }

l3FirewallEntryAction  OBJECT-TYPE
	SYNTAX	   Integer32 (0|1)
	MAX-ACCESS read-write
	STATUS	   current
	DESCRIPTION 
		"L3 ACL Rule Acrion
			0 - Reject, 
			1 - Permit
		Device Allocation: AP, SM"
	::= { l3FirewallEntry 3 }

l3FirewallEntryInterface  OBJECT-TYPE
	SYNTAX	   Integer32 (0|1|2)
	MAX-ACCESS read-write
	STATUS	   current
	DESCRIPTION 
		"L3 ACL Rule Interface
			1 - WAN, 
			2 - LAN
		Device Allocation: AP, SM"
	::= { l3FirewallEntry 4 }

l3FirewallEntryLog	OBJECT-TYPE
	SYNTAX	   Integer32 (0|1)
	MAX-ACCESS read-write
	STATUS	   current
	DESCRIPTION 
		"L3 ACL Rule Log Flag
			1 - Rule Loggin is On, 
			0 - Rule Logging is Off
		Device Allocation: AP, SM"
	::= { l3FirewallEntry 5 }

l3FirewallEntryProtocol	 OBJECT-TYPE
	SYNTAX	   Integer32 (0|1|2|3|4|5)
	MAX-ACCESS read-write
	STATUS	   current
	DESCRIPTION 
		"L3 ACL Rules IP Protocol
			1 - TCP, 
			2 - UDP, 
			3 - TCP+UDP, 
			4 - ICMP, 
			5 - IP
		Device Allocation: AP, SM"
	::= { l3FirewallEntry 6 }

l3FirewallEntryPort	 OBJECT-TYPE
	SYNTAX	   Integer32 (0..65535)
	MAX-ACCESS read-write
	STATUS	   current
	DESCRIPTION 
		"L3 ACL Rule Destination Port
		Device Allocation: AP, SM"
	::= { l3FirewallEntry 7 }

l3FirewallEntrySrcIP  OBJECT-TYPE
	SYNTAX	   IpAddress
	MAX-ACCESS read-write
	STATUS	   current
	DESCRIPTION 
		"L3 ACL Rule Source IP Address
		Device Allocation: AP, SM"
	::= { l3FirewallEntry 8 }

l3FirewallEntrySrcMask	OBJECT-TYPE
	SYNTAX	   IpAddress
	MAX-ACCESS read-write
	STATUS	   current
	DESCRIPTION 
		"L3 ACL Rule Source Network Mask
		Device Allocation: AP, SM"
	::= { l3FirewallEntry 9 }

l3FirewallEntryDstIP  OBJECT-TYPE
	SYNTAX	   IpAddress
	MAX-ACCESS read-write
	STATUS	   current
	DESCRIPTION 
		"L3 ACL Rule Destination IP Address
		Device Allocation: AP, SM"
	::= { l3FirewallEntry 10 }

l3FirewallEntryDstMask	OBJECT-TYPE
	SYNTAX	   IpAddress
	MAX-ACCESS read-write
	STATUS	   current
	DESCRIPTION 
		"L3 ACL Rule Destination Network Mask
		Device Allocation: AP, SM"
	::= { l3FirewallEntry 11 }

l3FirewallEntryDSCP	 OBJECT-TYPE
	SYNTAX	   Integer32 (0..63)
	MAX-ACCESS read-write
	STATUS	   current
	DESCRIPTION 
		"L3 ACL Rule DSCP
		Device Allocation: AP, SM"
	::= { l3FirewallEntry 12 }

l3FirewallEntryToS	OBJECT-TYPE
	SYNTAX	   Integer32 (0..255)
	MAX-ACCESS read-write
	STATUS	   current
	DESCRIPTION 
		"L3 ACL Rule TOS
		Device Allocation: AP, SM"
	::= { l3FirewallEntry 13 }

l3FirewallEntrySrcPort      OBJECT-TYPE
        SYNTAX     Integer32 (0..65535)
        MAX-ACCESS read-write
        STATUS     current
        DESCRIPTION
                "L3 ACL Rule Source Port
                Device Allocation: AP, SM"
        ::= { l3FirewallEntry 14 }

dmzEnable  OBJECT-TYPE
	SYNTAX	   Integer32 (0|1)
	MAX-ACCESS read-write
	STATUS	   current
	DESCRIPTION 
		"Enable DMZ:
			1 - Enable, 
			0 - Disable.
		Device Allocation: SM"
	DEFVAL	{ 0 }
	::= { dmz 1 }

dmzIPAddress  OBJECT-TYPE
	SYNTAX	   IpAddress
	MAX-ACCESS read-write
	STATUS	   current
	DESCRIPTION 
		"DMZ IP Address.
		Device Allocation: SM"
	::= { dmz 2 }

voipEnable	OBJECT-TYPE
	SYNTAX	   Integer32 (0|1)
	MAX-ACCESS read-write
	STATUS	   current
	DESCRIPTION 
		"VoIP Enable:
			0 - disable, 
			1 - enable
		Device Allocation: AP, SM"
	DEFVAL	{ 0 }
	::= { confQoS 1 }

qosEnable  OBJECT-TYPE
	SYNTAX	   Integer32 (0|1)
	MAX-ACCESS read-write
	STATUS	   current
	DESCRIPTION 
		"Enable QoS:
			0 - disable, 
			1 - enable
		Device Allocation: AP, SM"
	DEFVAL	{ 0 }
	::= { confQoS 2 }

classificationListTable	 OBJECT-TYPE
	SYNTAX SEQUENCE OF ClassificationListEntry
	MAX-ACCESS not-accessible
	STATUS	   current
	DESCRIPTION 
		"Quality of Service rules Table
		Device Allocation: AP, SM"
	::= { confQoS 3 }
	
mcPriority	OBJECT-TYPE
	SYNTAX	   Integer32 (0|1)
	MAX-ACCESS read-write
	STATUS	   current
	DESCRIPTION
		"Multicast Priority:
			0 - low, 
			1 - high
		Device Allocation: AP, SM"
	DEFVAL	{ 0 }
	::= { confQoS 4 }

bcPriority	OBJECT-TYPE
	SYNTAX	   Integer32 (0|1)
	MAX-ACCESS read-write
	STATUS	   current
	DESCRIPTION
		"Broadcast Priority:
			0 - low, 
			1 - high
		Device Allocation: AP, SM"
	DEFVAL	{ 0 }
	::= { confQoS 5 }

classificationListEntry	 OBJECT-TYPE
	SYNTAX	ClassificationListEntry
	MAX-ACCESS not-accessible
	STATUS	   current
	DESCRIPTION 
		"Quality of Service Rule Entry
		Device Allocation: AP, SM"
	INDEX	{ classificationRuleIndex }
	::= { classificationListTable 1 }

ClassificationListEntry ::= SEQUENCE {
	classificationRuleIndex
		Integer32,
	classificationRuleType
		Integer32,
	classificationRuleValue
		Integer32,
	classificationRuleIP
		IpAddress,
	classificationRuleMAC
		DisplayString,
	classificationRuleMask
		DisplayString,
	classificationRuleDirection
		Integer32,
	classificationRuleQueue
		Integer32
}

classificationRuleIndex	 OBJECT-TYPE
		SYNTAX	   Integer32 (0..14)
		MAX-ACCESS read-write
		STATUS	   current
		DESCRIPTION
		"QoS Rule Table Index
		Table Entry is cleared if Index is set to zero
		Device Allocation: AP, SM"
		::= { classificationListEntry 1 }

classificationRuleType	OBJECT-TYPE
	SYNTAX	   Integer32 (0|1..9)
	MAX-ACCESS read-write
	STATUS	   current
	DESCRIPTION 
		"QoS Rule Type: 
			1 - voip, 
			2 - dscp, 
			3 - cos, 
			4 - vlanid, 
			5 - ethertype, 
			6 - ipv4, 
			7 - mac, 
			8 - broadcast, 
			9 - multicast
		Device Allocation: AP, SM"
	::= { classificationListEntry 2 }

classificationRuleValue	 OBJECT-TYPE
	SYNTAX	   Integer32 (0..65535)
	MAX-ACCESS read-write
	STATUS	   current
	DESCRIPTION 
		"QoS Rule Value. Qos rule value is valid only for dscp, cos, vlanid and ethertype Rule types
		Device Allocation: AP, SM"
	::= { classificationListEntry 3 }

classificationRuleIP  OBJECT-TYPE
	SYNTAX	   IpAddress
	MAX-ACCESS read-write
	STATUS	   current
	DESCRIPTION 
		"QoS IP Address
		Device Allocation: AP, SM"
	::= { classificationListEntry 4 }

classificationRuleMAC  OBJECT-TYPE
	SYNTAX	   DisplayString (SIZE(0|17))
	MAX-ACCESS read-write
	STATUS	   current
	DESCRIPTION 
		"QoS MAC Address
		Device Allocation: AP, SM"
	::= { classificationListEntry 5 }

classificationRuleMask	OBJECT-TYPE
	SYNTAX	   DisplayString (SIZE(0|7..17))
	MAX-ACCESS read-write
	STATUS	   current
	DESCRIPTION 
		"QoS Netmask
		Device Allocation: AP, SM"
	::= { classificationListEntry 6 }

classificationRuleDirection	 OBJECT-TYPE
	SYNTAX	   Integer32 (0|1..3)
	MAX-ACCESS read-write
	STATUS	   current
	DESCRIPTION 
		"IP or MAC Rules direction: 
			1 - Source, 
			2 - Destination, 
			3 - Either (or Both directions)
		Device Allocation: AP, SM"
	::= { classificationListEntry 7 }

classificationRuleQueue	 OBJECT-TYPE
	SYNTAX	   Integer32 (0|1..3)
	MAX-ACCESS read-write
	STATUS	   current
	DESCRIPTION 
		"Rule Queue: 
			1- Hight, 
			2 - Low, 
			3 - VoIP
		Device Allocation: AP, SM"
	::= { classificationListEntry 8 }

portForwardingEntryEnable  OBJECT-TYPE
		SYNTAX	   Integer32 (0|1)
		MAX-ACCESS read-write
		STATUS	   current
		DESCRIPTION
		"Port Forwarding feature:
			0 - Disable, 
			1 - Enable
		Device Allocation: SM"
		::= { portForwarding 1 }

portForwardingTable	 OBJECT-TYPE
		SYNTAX SEQUENCE OF PortForwardingEntry
		MAX-ACCESS not-accessible
		STATUS	   current
		DESCRIPTION
		"Port Forwarding Rules Table
		Device Allocation: SM"
		::= { portForwarding 2 }
		
portForwardingEntry	 OBJECT-TYPE
		SYNTAX	PortForwardingEntry
		MAX-ACCESS not-accessible
		STATUS	   current
		DESCRIPTION
		"Port Forwarding Table Rule Entry
		Device Allocation: SM"
		INDEX	{ portForwardingTableEntryIndex }
		::= { portForwardingTable 1 }

PortForwardingEntry ::= SEQUENCE {
		portForwardingTableEntryIndex
				Integer32,
		portForwardingTableEntryProtocol
				Integer32,
		portForwardingTableEntryWLANPortBegin
				Integer32,
		portForwardingTableEntryWLANPortEnd
				Integer32,
		portForwardingTableEntryLANIP
				IpAddress,
		portForwardingTableEntryWLANPortMappedBegin
				Integer32
}

portForwardingTableEntryIndex  OBJECT-TYPE
		SYNTAX	   Integer32 (0..16)
		MAX-ACCESS read-write
		STATUS	   current
		DESCRIPTION
		"Port Forwarding Table Entry Index
		Table Entry is cleared if Index is set to zero
		Device Allocation: SM"
		::= { portForwardingEntry 1 }

portForwardingTableEntryProtocol  OBJECT-TYPE
		SYNTAX	   Integer32 (0|1|2|3)
		MAX-ACCESS read-write
		STATUS	   current
		DESCRIPTION
		"Port Forwarding Table Entry Rule Protocol:
			0 - Clear Rule, 
			1 - UDP, 
			2 - TCP, 
			3 - UDP+TCP
		Device Allocation: SM"
		::= { portForwardingEntry 2 }

portForwardingTableEntryWLANPortBegin  OBJECT-TYPE
		SYNTAX	   Integer32 (0..65535)
		MAX-ACCESS read-write
		STATUS	   current
		DESCRIPTION
		"Port Forwarding WLAN Port Start number
		Device Allocation: SM"
		::= { portForwardingEntry 3 }

portForwardingTableEntryWLANPortEnd	 OBJECT-TYPE
		SYNTAX	   Integer32 (0..65535)
		MAX-ACCESS read-write
		STATUS	   current
		DESCRIPTION
		"Port Forwarding WLAN Port End number
		Device Allocation: SM"
		::= { portForwardingEntry 4 }

portForwardingTableEntryLANIP  OBJECT-TYPE
		SYNTAX	   IpAddress
		MAX-ACCESS read-write
		STATUS	   current
		DESCRIPTION
		"Port Forwarding LAN IP Address
		Device Allocation: SM"
		::= { portForwardingEntry 5 }

portForwardingTableEntryWLANPortMappedBegin  OBJECT-TYPE
		SYNTAX     Integer32 (0..65535)
		MAX-ACCESS read-write
		STATUS     current
		DESCRIPTION
		"Port Forwarding Mapped Port number
		Device Allocation: SM"
		::= { portForwardingEntry 6 }

portForwardingSepMangIPEntryEnable  OBJECT-TYPE
                SYNTAX     Integer32 (0|1)
                MAX-ACCESS read-write
                STATUS     current
                DESCRIPTION     
                "SM Separate Management IP Port Forwarding feature:
                        0 - Disable,
                        1 - Enable
                Device Allocation: SM"
                ::= { portForwarding 3 }

portForwardingSepMangIPTable      OBJECT-TYPE
                SYNTAX SEQUENCE OF PortForwardingSepMangIPEntry
                MAX-ACCESS not-accessible
                STATUS     current
                DESCRIPTION
                "SM Separate Management IP Port Forwarding Rules Table
                Device Allocation: SM"
                ::= { portForwarding 4 }

portForwardingSepMangIPEntry      OBJECT-TYPE
                SYNTAX  PortForwardingSepMangIPEntry
                MAX-ACCESS not-accessible
                STATUS     current
                DESCRIPTION
                "SM Separate Management IP Port Forwarding Table Rule Entry
                Device Allocation: SM"
                INDEX   { portForwardingSepMangIPTableEntryIndex }
                ::= { portForwardingSepMangIPTable 1 }

PortForwardingSepMangIPEntry ::= SEQUENCE {
                portForwardingSepMangIPTableEntryIndex
                                Integer32,
                portForwardingSepMangIPTableEntryProtocol
                                Integer32,
                portForwardingSepMangIPTableEntryWLANPortBegin
                                Integer32,
                portForwardingSepMangIPTableEntryWLANPortEnd
                                Integer32,
                portForwardingSepMangIPTableEntryLANIP
                                IpAddress,
		portForwardingSepMangIPTableEntryWLANPortMappedBegin
				Integer32
}

portForwardingSepMangIPTableEntryIndex  OBJECT-TYPE
                SYNTAX     Integer32 (0..16)
                MAX-ACCESS read-write
                STATUS     current
                DESCRIPTION
                "SM Separate Management IP Port Forwarding Table Entry Index
                Table Entry is cleared if Index is set to zero
                Device Allocation: SM"
                ::= { portForwardingSepMangIPEntry 1 }

portForwardingSepMangIPTableEntryProtocol  OBJECT-TYPE
                SYNTAX     Integer32 (0|1|2|3)
                MAX-ACCESS read-write
                STATUS     current
                DESCRIPTION
                "SM Separate Management IP Port Forwarding Table Entry Rule Protocol:
                        0 - Clear Rule,
                        1 - UDP,
                        2 - TCP,
                        3 - UDP+TCP
                Device Allocation: SM"
                ::= { portForwardingSepMangIPEntry 2 }

portForwardingSepMangIPTableEntryWLANPortBegin  OBJECT-TYPE
                SYNTAX     Integer32 (0..65535)
                MAX-ACCESS read-write
                STATUS     current
                DESCRIPTION
                "SM Separate Management IP Port Forwarding WLAN Port Start number
                Device Allocation: SM"
                ::= { portForwardingSepMangIPEntry 3 }

portForwardingSepMangIPTableEntryWLANPortEnd      OBJECT-TYPE
                SYNTAX     Integer32 (0..65535)
                MAX-ACCESS read-write
                STATUS     current
                DESCRIPTION
                "SM Separate Management IP Port Forwarding WLAN Port End number
                Device Allocation: SM"
                ::= { portForwardingSepMangIPEntry 4 }

portForwardingSepMangIPTableEntryLANIP  OBJECT-TYPE
                SYNTAX     IpAddress
                MAX-ACCESS read-write
                STATUS     current
                DESCRIPTION
                "SM Separate Management IP Port Forwarding LAN IP Address
                Device Allocation: SM"
                ::= { portForwardingSepMangIPEntry 5 }

portForwardingSepMangIPTableEntryWLANPortMappedBegin  OBJECT-TYPE
                SYNTAX     Integer32 (0..65535)
                MAX-ACCESS read-write
                STATUS     current
                DESCRIPTION
                "SM Separate Management IP Port Forwarding Mapped Port number
                Device Allocation: SM"
                ::= { portForwardingSepMangIPEntry 6 }

staticRoutesEnableMain	 OBJECT-TYPE
		SYNTAX		Integer32 (0|1)
		MAX-ACCESS	read-write
		STATUS		current
		DESCRIPTION
		"Static Routes trigger
			0 - Disable
			1 - Enable"
		DEFVAL	{ 0 }
		::= { routing 1 }

cambiumStaticRoutesCnfTable	 OBJECT-TYPE
	SYNTAX SEQUENCE OF CambiumStaticRoutesCnfEntry
	MAX-ACCESS not-accessible
	STATUS	   current
	DESCRIPTION
		"Static Routes Table"
	::= { routing 2 }

cambiumTelnetServerEnable  OBJECT-TYPE
	SYNTAX     Integer32 (0|1)
	MAX-ACCESS read-write
	STATUS     current
	DESCRIPTION
		"Cambium Telnet Server:
			0 - Disable,
			1 - Enable
		Device Allocation: AP, SM"
	DEFVAL  { 0 }
	::= { cambiumTelnetServer 1 }

cambiumDeviceAgentEnable  OBJECT-TYPE
		SYNTAX		Integer32 (0|1)
		MAX-ACCESS	read-write
		STATUS		current
		DESCRIPTION
			"Remote Management:
				0 - Disable
				1 - Enable
			Cambium provides cloud management of Cambium devices called cnMaestro.
			This allows a user to manage all of their various Cambium devices via the web from any location in the world.
			This field enables this cnMaestro Cloud Management."
		DEFVAL	{ 1 }
		::= { cambiumDeviceAgent 1 }

cambiumDeviceAgentCNSURL  OBJECT-TYPE
		SYNTAX	   DisplayString (SIZE(0..128))
		MAX-ACCESS read-write
		STATUS	   current
		DESCRIPTION
			"cnMaestro URL:
			 This specifies the URL for accessing the cnMaestro Cloud Manager"
		::= { cambiumDeviceAgent 2 }

cambiumCNSDeviceAgentID  OBJECT-TYPE
		SYNTAX     DisplayString (SIZE(0..128))
		MAX-ACCESS read-write
		STATUS     current
		DESCRIPTION
			"Cambium ID:
			This is a user name for the cnMaestro Remote Management system.
			This is used with the 'Onboarding Key' to on-board older Cambium devices, 
			which are not provisioned with an MSN in the Cambium factory."
		::= { cambiumDeviceAgent 3 }

cambiumCNSDeviceAgentPassword  OBJECT-TYPE
		SYNTAX     DisplayString (SIZE(0..128))
		MAX-ACCESS read-write
		STATUS     current
		DESCRIPTION
			"Onboarding Key:
			This is a password for the cnMaestro Remote Management system.
			This is used with the 'Cambium ID' to on-board older Cambium devices,
			which are not provisioned with an MSN in the Cambium factory."
		::= { cambiumDeviceAgent 4 }

cambiumStaticRoutesCnfEntry OBJECT-TYPE
	SYNTAX	   CambiumStaticRoutesCnfEntry
	MAX-ACCESS not-accessible
	STATUS	   current
	DESCRIPTION
		"Static Routes Dest/Getway pair entry"
	INDEX	{ cambiumStaticRoutesCnfIndex }
	::= { cambiumStaticRoutesCnfTable 1 }

CambiumStaticRoutesCnfEntry ::= SEQUENCE {
	cambiumStaticRoutesCnfIndex
		Integer32,
	cambiumStaticRoutesCnfDestIP
		IpAddress,
	cambiumStaticRoutesCnfGW
		IpAddress,
	cambiumStaticRoutesCnfNetmask
		IpAddress,
	cambiumStaticRoutesCnfEnbl
		Integer32,
	cambiumStaticRoutesCnfInfo
		DisplayString
}

cambiumStaticRoutesCnfIndex	 OBJECT-TYPE
	SYNTAX	  Integer32 (0..16)
	MAX-ACCESS read-write
	STATUS	   current
	DESCRIPTION
		"Index"
	::= { cambiumStaticRoutesCnfEntry 1 }

cambiumStaticRoutesCnfDestIP  OBJECT-TYPE
	SYNTAX	   IpAddress
	MAX-ACCESS read-write
	STATUS	   current
	DESCRIPTION
		"Destination IP"
	::= { cambiumStaticRoutesCnfEntry 2 }

cambiumStaticRoutesCnfGW  OBJECT-TYPE
	SYNTAX	   IpAddress
	MAX-ACCESS read-write
	STATUS	   current
	DESCRIPTION
		"Getway IP"
	::= { cambiumStaticRoutesCnfEntry 3 }

cambiumStaticRoutesCnfNetmask  OBJECT-TYPE
	SYNTAX	   IpAddress
	MAX-ACCESS read-write
	STATUS	   current
	DESCRIPTION
		"Dest IP Netmask"
	::= { cambiumStaticRoutesCnfEntry 4 }

cambiumStaticRoutesCnfEnbl	OBJECT-TYPE
	SYNTAX	   Integer32 (0|1)
	MAX-ACCESS read-write
	STATUS	   current
	DESCRIPTION
		"Static Routes enable an entry"
	::= { cambiumStaticRoutesCnfEntry 5 }

cambiumStaticRoutesCnfInfo	OBJECT-TYPE
	SYNTAX	   DisplayString (SIZE(0..100))
	MAX-ACCESS read-write
	STATUS	   current
	DESCRIPTION
		"Static Routes Interface Name"
	::= { cambiumStaticRoutesCnfEntry 6 }


mgmtVLANEnable	OBJECT-TYPE
		SYNTAX	   Integer32 (0|1)
		MAX-ACCESS read-write
		STATUS	   current
		DESCRIPTION
		"Management VLANs State:
			0 - Disable, 
			1 - Enable
		Device Allocation: AP, SM"
		DEFVAL	{ 0 }
		::= { mgmtVLAN 1 }

mgmtVLANVID	 OBJECT-TYPE
		SYNTAX	   Integer32 (0..4094)
		MAX-ACCESS read-write
		STATUS	   current
		DESCRIPTION
		"Management VLAN ID
		Device Allocation: AP, SM"
		::= { mgmtVLAN 2 }

mgmtVLANVP	OBJECT-TYPE
		SYNTAX	   Integer32 (0..7)
		MAX-ACCESS read-write
		STATUS	   current
		DESCRIPTION
		"Management VLAN VP
		Device Allocation: AP, SM"
		::= { mgmtVLAN 3 }

dataVLANEnable	OBJECT-TYPE
		SYNTAX	   Integer32 (0|1)
		MAX-ACCESS read-write
		STATUS	   current
		DESCRIPTION
		"Data VLANs State:
			0 - Disable, 
			1 - Enable
		Device Allocation: SM"
		DEFVAL	{ 0 }
		::= { dataVLAN 1 }

dataVLANVID	 OBJECT-TYPE
		SYNTAX	   Integer32 (0..4094)
		MAX-ACCESS read-write
		STATUS	   current
		DESCRIPTION
		"Data VLAN ID
		Device Allocation: SM"
		::= { dataVLAN 2 }

dataVLANVP	OBJECT-TYPE
		SYNTAX	   Integer32 (0..7)
		MAX-ACCESS read-write
		STATUS	   current
		DESCRIPTION
		"Data VLAN VP
		Device Allocation: SM"
		::= { dataVLAN 3 }

mcastVLANEnable	 OBJECT-TYPE
		SYNTAX	   Integer32 (0|1)
		MAX-ACCESS read-write
		STATUS	   current
		DESCRIPTION
				"Multicast VLAN State:
						0 - Disable,
						1 - Enable
				Device Allocation: SM"
		DEFVAL	{ 0 }
		::= { mcastVLAN 1 }

mcastVLANVID  OBJECT-TYPE
		SYNTAX	   Integer32 (0..4094)
		MAX-ACCESS read-write
		STATUS	   current
		DESCRIPTION
				"Multicast VLAN ID
				Device Allocation: SM"
		::= { mcastVLAN 2 }

mcastVLANVP	 OBJECT-TYPE
		SYNTAX	   Integer32 (0..7)
		MAX-ACCESS read-write
		STATUS	   current
		DESCRIPTION
				"Multicast VLAN VP
				Device Allocation: SM"
		::= { mcastVLAN 3 }

membershipVLANTable	 OBJECT-TYPE
		SYNTAX SEQUENCE OF MembershipVLANEntry
		MAX-ACCESS not-accessible
		STATUS	   current
		DESCRIPTION
		"Membership VLAN Rules Table
		Device Allocation: SM"
		::= { vlans 3 }
		
membershipVLANEntry	 OBJECT-TYPE
		SYNTAX	MembershipVLANEntry
		MAX-ACCESS not-accessible
		STATUS	   current
		DESCRIPTION
		"Membership VLAN Table Rule Entry
		Device Allocation: SM"
		INDEX	{ membershipVLANTableEntryIndex }
		::= { membershipVLANTable 1 }

MembershipVLANEntry ::= SEQUENCE {
		membershipVLANTableEntryIndex
				Integer32,
		membershipVLANTableEntryVIDBegin
				Integer32,
		membershipVLANTableEntryVIDEnd
				Integer32
}

membershipVLANTableEntryIndex  OBJECT-TYPE
		SYNTAX	   Integer32 (0..16)
		MAX-ACCESS read-write
		STATUS	   current
		DESCRIPTION
		"Membership VLAN Table Entry Index
		Table Entry is cleared if Index is set to zero
		Device Allocation: SM"
		::= { membershipVLANEntry 1 }

membershipVLANTableEntryVIDBegin  OBJECT-TYPE
		SYNTAX	   Integer32 (0|1..4095)
		MAX-ACCESS read-write
		STATUS	   current
		DESCRIPTION
		"Membership VLAN Table Entry VLAN ID Begin
		Device Allocation: SM"
		::= { membershipVLANEntry 2 }

membershipVLANTableEntryVIDEnd	OBJECT-TYPE
		SYNTAX	   Integer32 (0|1..4095)
		MAX-ACCESS read-write
		STATUS	   current
		DESCRIPTION
		"Membership VLAN Table Entry VLAN ID End
		Device Allocation: SM"
		::= { membershipVLANEntry 3 }

mappingVLANTable  OBJECT-TYPE
		SYNTAX SEQUENCE OF MappingVLANEntry
		MAX-ACCESS not-accessible
		STATUS	   current
		DESCRIPTION
				"Mapping VLAN Rules Table
				Device Allocation: SM"
		::= { vlans 5 }

mappingVLANEntry  OBJECT-TYPE
		SYNTAX	MappingVLANEntry
		MAX-ACCESS not-accessible
		STATUS	   current
		DESCRIPTION
				"Mapping VLAN Table Rule Entry
				Device Allocation: SM"
		INDEX	{ mappingVLANTableEntryIndex }
		::= { mappingVLANTable 1 }

MappingVLANEntry ::= SEQUENCE {
		mappingVLANTableEntryIndex
				Integer32,
		mappingVLANTableEntryCVLAN
				Integer32,
		mappingVLANTableEntrySVLAN
				Integer32
}

mappingVLANTableEntryIndex	OBJECT-TYPE
		SYNTAX	   Integer32 (0..16)
		MAX-ACCESS read-write
		STATUS	   current
		DESCRIPTION
				"Mapping VLAN Table Entry Index
				Table Entry is cleared if Index is set to zero
				Device Allocation: SM"
		::= { mappingVLANEntry 1 }

mappingVLANTableEntryCVLAN	OBJECT-TYPE
		SYNTAX	   Integer32 (0|1..4095)
		MAX-ACCESS read-write
		STATUS	   current
		DESCRIPTION
				"Mapping VLAN Table C-VLAN ID,
				 Defines VLAN ID to be mapped from CPE side.
				Device Allocation: SM"
		::= { mappingVLANEntry 2 }

mappingVLANTableEntrySVLAN  OBJECT-TYPE
        SYNTAX     Integer32 (0|1..4095)
        MAX-ACCESS read-write
        STATUS     current
        DESCRIPTION
                "Mapping VLAN Table S-VLAN ID,
                 Defines VLAN ID to be mapped from Service provider.
                Device Allocation: SM"
        ::= { mappingVLANEntry 3 }

dlkmNATSIPHelpers OBJECT-TYPE
	SYNTAX     Integer32 (0|1)
	MAX-ACCESS read-write
	STATUS     current
	DESCRIPTION
		"Enables Auxiliary Netfilter NAT SIP Helper modules support:
			0 - Disable,
			1 - Enabled
		Device Allocation: AP, SM"
	::= { dlkm 1 }

prefferedAPTable OBJECT-TYPE
		SYNTAX SEQUENCE OF PrefferedAPEntry
		MAX-ACCESS not-accessible
		STATUS	   current
		DESCRIPTION
		"Preffered AP Table
		Device Allocation: SM"
		::= { wirelessPrefList 1 }

prefferedAPEntry  OBJECT-TYPE
		SYNTAX	PrefferedAPEntry
		MAX-ACCESS not-accessible
		STATUS	   current
		DESCRIPTION
		"Preffered SSID Table Entry
		Device Allocation: SM"
		INDEX	{ prefferedListTableEntryIndex }
		::= { prefferedAPTable 1 }

PrefferedAPEntry ::= SEQUENCE {
		prefferedListTableEntryIndex
				Integer32,
		prefferedListTableEntrySSID
				DisplayString,
		prefferedListTableEntryKEY
				DisplayString,
		prefferedListTableSecurityMethod
				Integer32
}

prefferedListTableEntryIndex  OBJECT-TYPE
		SYNTAX	   Integer32 (0..16)
		MAX-ACCESS read-write
		STATUS	   current
		DESCRIPTION
		"Preferred AP Table Index
		Table Entry is cleared if Index is set to zero
		Device Allocation: SM"
		::= { prefferedAPEntry 1 }

prefferedListTableEntrySSID	 OBJECT-TYPE
		SYNTAX	   DisplayString (SIZE(0|1..32))
		MAX-ACCESS read-write
		STATUS	   current
		DESCRIPTION
		"Preferred AP SSID
		Device Allocation: SM"
		::= { prefferedAPEntry 2 }

prefferedListTableEntryKEY	OBJECT-TYPE
		SYNTAX	   DisplayString (SIZE(0|8..63))
		MAX-ACCESS read-write
		STATUS	   current
		DESCRIPTION
		"Preferred AP Shared Key
		Device Allocation: SM"
		::= { prefferedAPEntry 3 }
		
prefferedListTableSecurityMethod  OBJECT-TYPE
		SYNTAX	   Integer32(0..6)
		MAX-ACCESS read-write
		STATUS	   current
		DESCRIPTION
		"Authentication modes to connect to AP
		Device Allocation: SM
		Use bitmask to enable pereferred methods, 0 - means enable method:
		set 0-th bit to 0 - Open method (110b)
		set 1-st bit to 0 - WPA2 method (101b)
		set 2-nd bit to 0 - EAP-TTLS method (011b)
		0x00 - All enabled"
		DEFVAL	{ 0 }
		::= { prefferedAPEntry 4 }


cambiumpmp80211DeviceReboot	 OBJECT-TYPE
	SYNTAX	   Integer32 (1)
	MAX-ACCESS read-write
	STATUS	   current
	DESCRIPTION 
		"OID for Device Reboot, send reboot command to device
		Device Allocation: AP, SM"
	::= { cambiumpmp80211SystemActions 1 }

cambiumpmp80211ConfigurationReset  OBJECT-TYPE
	SYNTAX	   Integer32 (0..7)
	MAX-ACCESS read-write
	STATUS	   current
	DESCRIPTION 
		"OID for System Configuration reset to Defaults
		Device Allocation: AP, SM
		Use bitmask to enable options:
		set 0-th bit to 1 to do reset at all (001b)
		set 1-st bit to 1 to preserve license (011b)
		set 2-nd bit to 1 to preserve passwords (101b)"
	::= { cambiumpmp80211SystemActions 2 }

cambiumpmp80211ConfigurationSave  OBJECT-TYPE
	SYNTAX	   Integer32 (1)
	MAX-ACCESS read-write
	STATUS	   current
	DESCRIPTION 
		"OID for configuration save
		Device Allocation: AP, SM"
	::= { cambiumpmp80211SystemActions 3 }

-- OID for configuration Apply action

cambiumpmp80211ConfigurationApply  OBJECT-TYPE
	SYNTAX	   Integer32 (1)
	MAX-ACCESS read-write
	STATUS	   current
	DESCRIPTION 
		"OID for configuration Apply
		Device Allocation: AP, SM"
	::= { cambiumpmp80211SystemActions 4 }

cambiumpmp80211ConfigurationDiscard	 OBJECT-TYPE
		SYNTAX	   Integer32 (1)
		MAX-ACCESS read-write
		STATUS	   current
		DESCRIPTION
		"OID for configuration Discard
		Device Allocation: AP, SM"
		::= { cambiumpmp80211SystemActions 5 }

cambiumpmp80211ConfigurationState  OBJECT-TYPE
		SYNTAX	   Integer32 (0..255)
		MAX-ACCESS read-only
		STATUS	   current
		DESCRIPTION
		"System configuration state OID.
		Bit masks:
			0000 0001 - System is configured.
			0000 0010 - There are unsaved changesets.
			0000 0100 - There are unrestarted services.
			0000 1000 - Needed reboot of the system.
			0001 0000 - Configurations was reset.
			0010 0000 - Services restarting in process.
			0100 0000 - Software Update performed.
			1000 0000 - IP Address or protocol was changed.
		Device Allocation: AP, SM"
		::= { cambiumpmp80211SystemActions 6 }

cambiumpmp80211SoftwareUpdate  OBJECT-TYPE
	SYNTAX	   DisplayString
	MAX-ACCESS read-write
	STATUS	   current
	DESCRIPTION 
		"System OID for Software Update Agent,
		SW Update link value can be either remote firmware link (http, https, ftp),
		or local file link: /tmp/firmware.tar.gz
		NOTE: Device is automatically rebooted if link type is remote
		Device Allocation: AP, SM"
	::= { cambiumpmp80211SystemActions 7 }

cambiumpmp80211SoftwareUpdateStatus	 OBJECT-TYPE
	SYNTAX	   Integer32 (0..10)
	MAX-ACCESS read-only
	STATUS	   current
	DESCRIPTION 
		"Software Update Status OID
			0 - No SW Update is pending or No SW upgrade occurs,
			1 - SW Update is in progress, Uploading image to device,
			2 - SW Update is in progress, Verifying SHA2 signature,
			3 - SW Update is in progress, Executing pre-update script,
			4 - SW Update is in progress, Uploading image to flash,
			5 - SW Update is in progress, Uploading u-boot to flash,
			6 - SW Update is in progress, Executing post-update script,
			7 - SW Update is finished, waiting for reboot,
			8 - SW Update is in progress, Executing config down-grade script,
			9 - SW Update is in progress, Uploading firmware to flash & Reboot
		When SW Update is successfully, return value is 7 for ePMP 1000/2000,
		and 9 for ePMP Elevate
		GUI or NMS indicate that SW update was successful,
		Device can be rebooted.
		Device Allocation: AP, SM"
	::= { cambiumpmp80211SystemActions 8 }

cambiumpmp80211STAListUpdate  OBJECT-TYPE
		SYNTAX	   Integer32 (1)
		MAX-ACCESS read-write
		STATUS	   current
		DESCRIPTION
		"System OID for SM List update
		When this OID is received, 
		Connected SM list table is getting updated with actual SM list
		Device Allocation: AP"
		::= { cambiumpmp80211SystemActions 9 }

cambiumpmp80211STAListUpdateStatus	OBJECT-TYPE
		SYNTAX	   Integer32 (0|1|2)
		MAX-ACCESS read-write
		STATUS	   current
		DESCRIPTION
		"Sta List Update Status OID.
		This OID is used to indicate SM list table status:
			0 - No SMs are registerd to AP
			1 - SM List Table is getting updated
			2 - SM Data is ready
		Device Allocation: AP"
		::= { cambiumpmp80211SystemActions 10 }

cambiumpmp80211APListUpdate	 OBJECT-TYPE
		SYNTAX	   Integer32 (1)
		MAX-ACCESS read-write
		STATUS	   current
		DESCRIPTION
		"System OID for AP List update
		When this OID is received,
		Scanned AP list table is getting updated with actual AP scan list
		Device Allocation: SM"
		::= { cambiumpmp80211SystemActions 11 }

cambiumpmp80211APListUpdateStatus  OBJECT-TYPE
		SYNTAX	   Integer32 (0|1|2)
		MAX-ACCESS read-write
		STATUS	   current
		DESCRIPTION
		"AP List Update Status OID.
		This OID is used to indicate AP list table status:
			0 - No APs are available in the list
			1 - AP List Table is getting updated
			2 - AP Data is ready
		Device Allocation: SM"
		::= { cambiumpmp80211SystemActions 12 }

cambiumpmp80211SoftwareUpdateError  OBJECT-TYPE
        SYNTAX     Integer32 (0..32)
        MAX-ACCESS read-only
        STATUS     current
        DESCRIPTION
	  "Software Update error code:
		0 - Finished successfully, waiting for reboot.
		1 - SW update file download failed.
		2 - Unpack failed, damaged or wrong format package.
		3 - Firmware digital signature check failed.
		4 - U-Boot digital signature check failed.
		5 - Firmware FLASH write failed.
		6 - U-Boot FLASH write failed.
		7 - Boot partition switch failed.
		8 - Board SKU is not supported for this firmware.
		9 - Can't read firmware version, upgrade is impossible.
		10 - Down-grade not supported for WiFi & ePTP modes.
		11 - Down-grade below 2.3.1 is not supported for AP Lite device.
		12 - Down-grade not supported for non SM TDD mode.
		13 - Down-grade below 2.4.2 not supported for Force180/200 board types.
		14 - Down-grade below 2.5.0 not supported for AP WiFi.
		15 - Down-grade below 2.4.3 not supported for Reset Via Power Sequence.
		16 - Down-grade below 2.4.3 not supported for Particular Country Locked device.
		17 - Down-grade below 2.5.0 not supported for 2.5ms mode.
		18 - Down-grade below 2.5.2 not supported for Use MAC Address as EAP-TTLS Username.
		19 - Down-grade below 2.6.0 not supported for 5/10Mhz BW for WiFi & ePTP mode.
		20 - Separate Management IP Port Forwarding and Data Port Mapping are not supported in SW versions below 2.6.0.
		21 - General error. Device has no free memory.
		22 - General error code.
		23 - Downgrade below release 3.0 is not supported for ePMP2000.
		24 - Incorrect firmware type for the current device type.
		25 - Firmware file format is wrong for the current device type.
		26 - Downgrade below 5.6.6 is not supported for ePMP-Elevate board type.
		27 - Downgrade below 3.0.1 is not supported for 2.5G board type.
		28 - Downgrade below 3.1 is not supported if Preffered AP Table contains SSIDs with spaces.
		29 - Manifest Digital signature check failed.
		30 - Downgrade below 3.4 is not supported for Force 190 boards.
		31 - Downgrade below 3.4.0 not supported for MARGARET 6G board type.
		32 - Downgrade below 3.4 is not supported for Elevate 2.4 GHz board.
		33 - Versions below 3.5 do not support License Server. Disable the License Server option before downgrade.
                Device Allocation: AP, SM"
        ::= { cambiumpmp80211SystemActions 13 }

cambiumpmp80211StatsPerSTAListUpdateStatus	OBJECT-TYPE
		SYNTAX	   Integer32 (0|1|2)
		MAX-ACCESS read-write
		STATUS	   current
		DESCRIPTION
				"Stats per SM List Update Status OID.
				 This OID is used to indicate Stats per SM list table status:
				 0 - No SMs are registerd to AP
				 1 - TBD
				 2 - TBD"
		::= { cambiumpmp80211SystemActions 14 }

cambiumpmp80211StatsPerSTAListUpdate  OBJECT-TYPE
		SYNTAX	   Integer32 (1)
		MAX-ACCESS read-write
		STATUS	   current
		DESCRIPTION
				"System OID for Stats per SM table update
				 When this OID is received,
				 Stats per SM table is getting updated with actual data"
		::= { cambiumpmp80211SystemActions 15 }

cambiumpmp80211STADisconnect OBJECT-TYPE
		SYNTAX	   Integer32 (1..120)
		MAX-ACCESS read-write
		STATUS	   current
		DESCRIPTION
				"System OID for particular SM disconnection
				Device Allocation: AP"
		::= { cambiumpmp80211SystemActions 16 }
		
cambiumpmp80211GPSAutopopulate OBJECT-TYPE
		SYNTAX	   Integer32 (1)
		MAX-ACCESS read-write
		STATUS	   current
		DESCRIPTION
				"System action to auto-populate GPS stats for device
				 into system configuration
				 device location for latitude, longitude and height
				Device Allocation: AP, SM"
		::= { cambiumpmp80211SystemActions 17 }
		
cambiumpmp80211SoftwareUpdateErrorStr  OBJECT-TYPE
		SYNTAX	   DisplayString (SIZE(1..128))
		MAX-ACCESS read-only
		STATUS	   current
		DESCRIPTION "Software Update error, text descriprion"
		::= { cambiumpmp80211SystemActions 18 }	 
		
cambiumpmp80211GpsFirmwareUpdate  OBJECT-TYPE
	SYNTAX	   DisplayString
	MAX-ACCESS read-write
	STATUS	   current
	DESCRIPTION 
		"System OID for GPS Firmware Update Agent,
		Gps FW Update link value can be either remote firmware link (http, https, ftp),
		or local file link: /tmp/firmware.tar.gz
		NOTE: Device is automatically rebooted if link type is remote
		Device Allocation: AP, SM"
	::= { cambiumpmp80211SystemActions 19 } 
	
cambiumpmp80211GpsFirmwareUpdateError  OBJECT-TYPE
		SYNTAX	   Integer32 (0..8)
		MAX-ACCESS read-only
		STATUS	   current
		DESCRIPTION
				"Firmware Update error code:
						0 - Finished successfully
						1 - SW update file download failed
						2 - Unpack failed, damaged or wrong format package, or file access error
						3 - GPS Firmware digital signature check failed
						4 - GPS DA digital signature check failed
						5 - GPS DA download to GPS device failed
						6 - GPS FW download to GPS device failed
						7 - Board SKU is not supported for this firmware
						8 - GPS general communication error					  
				Device Allocation: AP, SM"
		::= { cambiumpmp80211SystemActions 21 }
		
cambiumpmp80211GpsFirmwareUpdateErrorStr  OBJECT-TYPE
		SYNTAX	   DisplayString (SIZE(1..128))
		MAX-ACCESS read-only
		STATUS	   current
		DESCRIPTION "GPS Firmware Update error, text description"
		::= { cambiumpmp80211SystemActions 22 }	  

cambiumBridgeTableAPStatus	OBJECT-TYPE
		SYNTAX	   Integer32 (0|1|2)
		MAX-ACCESS read-write
		STATUS	   current
		DESCRIPTION
		"AP Bridge Table Update Status OID.
		This OID is used to indicate bridge table status:
			0 - Bridge table is empty
			1 - Bridge table is filled with data
			2 - AP Data is ready
		Device Allocation: AP"
		::= { cambiumpmp80211SystemActions 25 }

cambiumBridgeTableSTAUpdate	 OBJECT-TYPE
		SYNTAX	   Integer32 (1)
		MAX-ACCESS read-write
		STATUS	   current
		DESCRIPTION
		"System OID for AP Bridge Table update.
		 When this OID is received, bridge table is getting updated with actual
		 bridge table list
		 Device Allocation: SM"
		::= { cambiumpmp80211SystemActions 26 }

cambiumBridgeTableSTAStatus	 OBJECT-TYPE
		SYNTAX	   Integer32 (0|1|2)
		MAX-ACCESS read-write
		STATUS	   current
		DESCRIPTION
		"Bridge Table Update Status OID.
		This OID is used to indicate bridge table status:
			0 - Bridge table is empty
			1 - Bridge table is filled with data
			2 - SM Data is ready
		Device Allocation: SM"
		::= { cambiumpmp80211SystemActions 27 }
		
cambiumBridgeTableAPUpdate	OBJECT-TYPE
		SYNTAX	   Integer32 (1)
		MAX-ACCESS read-write
		STATUS	   current
		DESCRIPTION
		"System OID for Bridge Table update.
		 When this OID is received, bridge table is getting updated with actual
		 bridge table list
		 Device Allocation: AP"
		::= { cambiumpmp80211SystemActions 28 }
			
cambiumForceTabUpdDHCP	OBJECT-TYPE
	SYNTAX	   Integer32 (1)
	MAX-ACCESS read-write
	STATUS	   current
	DESCRIPTION
	"Force update DHCP Host table, 
		1 - Force action
	Device Allocation: SM"
	::= { cambiumpmp80211SystemActions 30 }

cambiumForceTabUpdTrap	OBJECT-TYPE
	SYNTAX	   Integer32 (1)
	MAX-ACCESS read-write
	STATUS	   current
	DESCRIPTION
	"Force update SNMP Trap table, 
		1 - Force action
	Device Allocation: AP, SM"
	::= { cambiumpmp80211SystemActions 31 }

cambiumForceTabUpdl2Frw	 OBJECT-TYPE
	SYNTAX	   Integer32 (1)
	MAX-ACCESS read-write
	STATUS	   current
	DESCRIPTION
	"Force update l2 Firewal table, 
		1 - Force action
	Device Allocation: AP, SM"
	::= { cambiumpmp80211SystemActions 32 }

cambiumForceTabUpdl3Frw	 OBJECT-TYPE
	SYNTAX	   Integer32 (1)
	MAX-ACCESS read-write
	STATUS	   current
	DESCRIPTION
	"Force update l3 Firewal table, 
		1 - Force action
	Device Allocation: AP, SM"
	::= { cambiumpmp80211SystemActions 33 }

cambiumForceTabUpdQos  OBJECT-TYPE
	SYNTAX	   Integer32 (1)
	MAX-ACCESS read-write
	STATUS	   current
	DESCRIPTION
	"Force update Quality of Service table, 
		1 - Force action
	Device Allocation: AP, SM"
	::= { cambiumpmp80211SystemActions 34 }

cambiumForceTabUpdPortFw  OBJECT-TYPE
	SYNTAX	   Integer32 (1)
	MAX-ACCESS read-write
	STATUS	   current
	DESCRIPTION
	"Force update Port Forwarding table, 
		1 - Force action
	Device Allocation: SM"
	::= { cambiumpmp80211SystemActions 35 }

cambiumForceTabUpdVlan	OBJECT-TYPE
	SYNTAX	   Integer32 (1)
	MAX-ACCESS read-write
	STATUS	   current
	DESCRIPTION
	"Force update Membership VLAN table, 
		1 - Force action
	Device Allocation: SM"
	::= { cambiumpmp80211SystemActions 36 }

cambiumForceTabUpdMappingVlan OBJECT-TYPE
	SYNTAX	   Integer32 (1)
		MAX-ACCESS read-write
		STATUS	   current
		DESCRIPTION
		"Force update VLAN Mapping table,
				1 - Force action
		Device Allocation: AP, SM"
		::= { cambiumpmp80211SystemActions 37 }

cambiumConfigurationApplyOnReboot  OBJECT-TYPE
		SYNTAX	   Integer32 (1)
		MAX-ACCESS read-write
		STATUS	   current
		DESCRIPTION
				"OID for configuration Apply
				on stage of device reboot.
				Device Allocation: AP, SM"
		::= { cambiumpmp80211SystemActions 38 }
		
cambiumForceSTARescan OBJECT-TYPE
	SYNTAX	   Integer32 (1)
		MAX-ACCESS read-write
		STATUS	   current
		DESCRIPTION
		"force a STA rescan,
				1 - Force action
		Device Allocation: AP, SM"
		::= { cambiumpmp80211SystemActions 39 }

cambiumForceTabUpdMcastDeny OBJECT-TYPE
	SYNTAX	   Integer32 (1)
		MAX-ACCESS read-write
		STATUS	   current
		DESCRIPTION
		"Force update Multicast deny table,
				1 - Force action
		Device Allocation: AP, SM"
		::= { cambiumpmp80211SystemActions 40 }

cambiumForceTabUpdStaticRoutesCnf OBJECT-TYPE
	SYNTAX	   Integer32 (1)
		MAX-ACCESS read-write
		STATUS	   current
		DESCRIPTION
		"Force update Static Routes Conf table,
				1 - Force action
		Device Allocation: AP, SM"
		::= { cambiumpmp80211SystemActions 41 }

cambiumForceTabUpdMIR OBJECT-TYPE
	SYNTAX	   Integer32 (1)
		MAX-ACCESS read-write
		STATUS	   current
		DESCRIPTION
		"Force update MIR table,
				1 - Force action
		Device Allocation: AP, SM"
		::= { cambiumpmp80211SystemActions 42 }

cambiumForceTabUpdRadiusServ OBJECT-TYPE
	SYNTAX	   Integer32 (1)
		MAX-ACCESS read-write
		STATUS	   current
		DESCRIPTION
		"Force update Radius Server table,
				1 - Force action
		Device Allocation: AP, SM"
		::= { cambiumpmp80211SystemActions 43 }

cambiumForceTabUpdPrefAPList OBJECT-TYPE
	SYNTAX	   Integer32 (1)
		MAX-ACCESS read-write
		STATUS	   current
		DESCRIPTION
		"Force update Preferred AP list table,
				1 - Force action
		Device Allocation: AP, SM"
		::= { cambiumpmp80211SystemActions 44 }

cambiumForceTabUpdAPAlias OBJECT-TYPE
	SYNTAX	   Integer32 (1)
		MAX-ACCESS read-write
		STATUS	   current
		DESCRIPTION
		"Force update AP Alias table,
				1 - Force action
		Device Allocation: AP, SM"
		::= { cambiumpmp80211SystemActions 45 }

cambiumForceTabUpdPortFwSepMangIP  OBJECT-TYPE
        SYNTAX     Integer32 (1)
        MAX-ACCESS read-write
        STATUS     current
        DESCRIPTION
        "Force update Separate Management IP Port Forwarding table,
                1 - Force action
        Device Allocation: SM"
        ::= { cambiumpmp80211SystemActions 46 }

cambiumpmp80211SoftwareUpdateStatusTrap NOTIFICATION-TYPE
	OBJECTS { 
		cambiumpmp80211SoftwareUpdateError, 
		cambiumpmp80211SoftwareUpdateErrorStr 
	}
	STATUS	   current
	DESCRIPTION 
		"Software Update error TRAP. Trap indicating Software Update State. 
		This state is indicated by the included value of cambiumpmp80211GpsFirmwareUpdateError
		Device Allocation: AP, SM"
	::= { cambiumpmp80211SystemTraps 1 }

cambiumpmp80211GPSSyncStatusTrap NOTIFICATION-TYPE
		OBJECTS { cambiumToolbarGPSSyncState }
		STATUS	   current
		DESCRIPTION
		"GPS Sync Status TRAP. Trap indicating GPS Sync State change.
		This state is indicated by the included value of cambiumToolbarGPSSyncState
		Device Allocation: AP, SM"
		::= { cambiumpmp80211SystemTraps 2 }

cambiumpmp80211SystemUpTrap NOTIFICATION-TYPE
		STATUS	   current
		DESCRIPTION
		"System UP TRAP. Trap indicating SNMP subSystem UP
		Device Allocation: AP, SM"
		::= { cambiumpmp80211SystemTraps 3 }

cambiumpmp80211DFSStatusTrap NOTIFICATION-TYPE
		OBJECTS { cambiumDFSStatus, cambiumDFSStatusStr }
		STATUS	   current
		DESCRIPTION
		"DFS Status TRAP. Trap indicating DFS Event.
		This event is indicated by the included value of cambiumDFSStatus
		Device Allocation: AP, SM"
		::= { cambiumpmp80211SystemTraps 4 }

cambiumpmp80211JSONCfgImportTrap NOTIFICATION-TYPE
		OBJECTS { cambiumJSONCfgImportError }
		STATUS	   current
		DESCRIPTION
		"JSON configuration import error trap. Trap catches JSON configuration
		import state. This state is indicated by the included value of
		cambiumJSONCfgImportError.
		Device Allocation: AP, SM"
		::= { cambiumpmp80211SystemTraps 5 }

cambiumpmp80211JSONCfgExportTrap NOTIFICATION-TYPE
		OBJECTS { cambiumJSONCfgExportError }
		STATUS	   current
		DESCRIPTION
		"JSON configuration export error trap. Trap catches JSON configuration
		export state. This state is indicated by the included value of
		cambiumJSONCfgExportError.
		Device Allocation: AP, SM"
		::= { cambiumpmp80211SystemTraps 6 }

cambiumpmp80211FullCfgRestoreTrap NOTIFICATION-TYPE
		OBJECTS { cambiumFullCfgRestoreError }
		STATUS	   current
		DESCRIPTION
		"Full configuration restore error trap. Trap catches full configuration
		restoring state. This state is indicated by the included value of
		cambiumFullCfgRestoreError.
		Device Allocation: AP, SM"
		::= { cambiumpmp80211SystemTraps 7 }

cambiumpmp80211FullCfgBackupTrap NOTIFICATION-TYPE
		OBJECTS { cambiumFullCfgBackUpError }
		STATUS	   current
		DESCRIPTION
		"Full configuration backup error trap. Trap catches full configuration
		backup state. This state is indicated by the included value of
		cambiumFullCfgBackUpError.
		Device Allocation: AP, SM"
		::= { cambiumpmp80211SystemTraps 8 }
		
cambiumpmp80211GpsFirmwareUpdateStatusTrap NOTIFICATION-TYPE
	OBJECTS {  
		cambiumpmp80211GpsFirmwareUpdateError, 
		cambiumpmp80211GpsFirmwareUpdateErrorStr
	}
	STATUS	   current
	DESCRIPTION 
		"GPS Update error TRAP. Trap indicating GPS Firmware Update State. 
		This state is indicated by the included value of cambiumpmp80211GpsFirmwareUpdateError
		Device Allocation: AP, SM"
	::= { cambiumpmp80211SystemTraps 9 }

cambiumpmp80211STADropTrap NOTIFICATION-TYPE
		OBJECTS { cambiumSTAMAC, cambiumSTADropReason }
		STATUS	   current
		DESCRIPTION
		"SM Drop trap. Trap catches dropped SM info. Information is
		contained in the included values of cambiumSTAMAC and
		cambiumSTADropReason.
		Device Allocation: AP"
		::= { cambiumpmp80211SystemTraps 10 }

cambiumpmp80211SMRegTrap NOTIFICATION-TYPE
		OBJECTS { cambiumSTAMAC }
		STATUS	   current
		DESCRIPTION
		"SM Registration trap. Trap catches registered SM info. Information is
		contained in the included value of cambiumSTAMAC.
		Device Allocation: AP"
		::= { cambiumpmp80211SystemTraps 11 }

cambiumpmp80211SystemRebootTrap NOTIFICATION-TYPE
		STATUS	   current
		DESCRIPTION
		"System reboot trap. Trap indicates that snmpd daemon has been shut
		down and the system is going to reboot.
		Device Allocation: AP, SM"
		::= { cambiumpmp80211SystemTraps 12 }
		
cambiumpmp80211SAModeTrap NOTIFICATION-TYPE
		STATUS	   current
		DESCRIPTION
		"Spectrum Analyzer mode trap. Trap indicates that he system is going to
		reboot in SA mode.
		Device Allocation: AP, SM"
		::= { cambiumpmp80211SystemTraps 13 }

cambiumpmpETSIframeSkipTrap NOTIFICATION-TYPE
		STATUS	   current
		DESCRIPTION
		"To much frame skipped due to CCA.
		Device Allocation: AP"
		::= { cambiumpmp80211SystemTraps 14 }

cambiumpmp80211NetworkEntryFailureTrap NOTIFICATION-TYPE
		OBJECTS { cambiumNetworkEntryFailureSTAMAC, cambiumNetworkEntryFailureReason }
		STATUS	   current
		DESCRIPTION
		"SM rejected trap. Trap obtains info about the latest rejected SM. Trap string
		is contained an information string with rejected reason and MAC of 
		rejected SM. Trap message for a host is consisted of cambiumNetworkEntryFailureSTAMAC and 
		cambiumNetworkEntryFailureReason objects.
		Device Allocation: AP"
		::= { cambiumpmp80211SystemTraps 15 }		

cambiumLinkTestDuration	 OBJECT-TYPE
	SYNTAX	   Integer32 (2|4|6|8|10|12|14|16|18|20)
	MAX-ACCESS read-write
	STATUS	   current
	DESCRIPTION
		"Link Test Duration OID.
		Device Allocation: AP, SM"
	DEFVAL	{ 10 }
	::= { cambiumLinkTest 1 }

cambiumLinkTestPckSize	OBJECT-TYPE
	SYNTAX	   Integer32 (128|800|1500)
	MAX-ACCESS read-write
	STATUS	   current
	DESCRIPTION
		"Link Test Packet Size OID.
		Device Allocation: AP, SM"
	DEFVAL	{ 1500 }
	::= { cambiumLinkTest 2 }

cambiumLinkTestStartForMAC	OBJECT-TYPE
	SYNTAX	   DisplayString (SIZE(11..17))
	MAX-ACCESS read-write
	STATUS	   current
	DESCRIPTION
		"The Link Test Destination MAC address.
		Start Link Test by write this OID.
		Device Allocation: AP, SM"
	::= { cambiumLinkTest 3 }

cambiumLinkTestStatus  OBJECT-TYPE
	SYNTAX	   Integer32 (0..6)
	MAX-ACCESS read-only
	STATUS	   current
	DESCRIPTION
		"The Link Test Status OID.
		0: WAIT
		1: START
		2: BUSY
		3: SUCCESS
		4: SUCCESS (PREF PERIOD)
		5: ERROR UNREACHABLE
		6: ERROR FAIL
		Device Allocation: AP, SM"
	::= { cambiumLinkTest 4 }

cambiumLinkTestResultDate  OBJECT-TYPE
	SYNTAX	   DisplayString (SIZE(6..24))
	MAX-ACCESS read-only
	STATUS	   current
	DESCRIPTION
		"The Link Test Result Timestamp
		Device Allocation: AP, SM"
	::= { cambiumLinkTest 5 }

cambiumLinkTestResultUL	 OBJECT-TYPE
	SYNTAX	   Integer32 (0..1000000)
	MAX-ACCESS read-only
	STATUS	   current
	DESCRIPTION
		"Link Test Result Uplink.
		Device Allocation: AP, SM"
	DEFVAL	{ 0 }
	::= { cambiumLinkTest 6 }

cambiumLinkTestResultDL	 OBJECT-TYPE
	SYNTAX	   Integer32 (0..1000000)
	MAX-ACCESS read-only
	STATUS	   current
	DESCRIPTION
		"Link Test Result Downlink.
		Device Allocation: AP, SM"
	DEFVAL	{ 0 }
	::= { cambiumLinkTest 7 }

cambiumLinkTestForceAnt	OBJECT-TYPE
	SYNTAX	   Integer32 (0|1|2)
	MAX-ACCESS read-write
	STATUS	   current
	DESCRIPTION
		"Link Test Force Antenna OID.
			0: Auto
			1: Force Sector Antenna
			2: Force Smart Antenna
		Device Allocation: AP, SM"
	DEFVAL	{ 0 }
	::= { cambiumLinkTest 8 }

caminfoScanFrequencyListCountry	 OBJECT-TYPE
		SYNTAX	   DisplayString (SIZE(0..128))
		MAX-ACCESS read-write
		STATUS	   current
		DESCRIPTION
		"Country for Frequency List 20/40 MHz band
		Device Allocation: AP, SM"
		::= { caminfo 1 }

caminfoScanFrequencyListTwentyBand	OBJECT-TYPE
		SYNTAX	   DisplayString (SIZE(0..1064))
		MAX-ACCESS read-only
		STATUS	   current
		DESCRIPTION
		"Scan Frequency List for 20 MHz band
		Device Allocation: SM"
		::= { caminfo 2 }

caminfoScanFrequencyListFortyBand  OBJECT-TYPE
		SYNTAX	   DisplayString (SIZE(0..1064))
		MAX-ACCESS read-only
		STATUS	   current
		DESCRIPTION
		"Scan Frequency List for 40 MHz band
		Device Allocation: SM"
		::= { caminfo 3 }

caminfoScanFrequencyListAllow59band	 OBJECT-TYPE
		SYNTAX	   Integer32 (0|1)
		MAX-ACCESS read-only
		STATUS	   current
		DESCRIPTION
		"Allow 59 band if the board is calibrated
		using new frequency values. 
			0 - Do not Allow 
			1 - Allow
		Device Allocation: AP, SM"
		::= { caminfo 4 }		 

cambiumInternetConnectionServerIP OBJECT-TYPE
		SYNTAX	   IpAddress
		MAX-ACCESS read-write
		STATUS	   current
		DESCRIPTION
		"Internet Connection Server IP Address
		This is auxiliary IP address to ping 
		in order to define Internet connection Status
		Device Allocation: AP, SM"
		::= { cambiumToolBarOpts 1 }

cambiumInternetConnectionPollPeriod OBJECT-TYPE
		SYNTAX	   Integer32 (1..3600)
		MAX-ACCESS read-write
		STATUS	   current
		DESCRIPTION
		"Internet Connection Server Ping period in seconds
		Device Allocation: AP, SM"
		::= { cambiumToolBarOpts 2 }

cambiumToolbarGlobeState OBJECT-TYPE
		SYNTAX	   Integer32 (0|1)
		MAX-ACCESS read-only
		STATUS	   current 
		DESCRIPTION 
		"Globe Internet Connectivity Status Icon State:
			0 - No Internet Connectivity,
			1 - Internet Connectivity
		Device Allocation: AP, SM"
		::= { cambiumToolBarStates 1 }

cambiumToolbarGPSSyncState OBJECT-TYPE
		SYNTAX	   Integer32 (0..5)
		MAX-ACCESS read-only
		STATUS	   current
		DESCRIPTION
		"GPS Current SYNC State:
			0 - The Initialization State
			1 - The No Synchronization State
			2 - The Synchronization State
			3 - The Hold Off State
			4 - The Regaining Sync State
			5 - The Free Run State
		Device Allocation: AP"
		::= { cambiumToolBarStates 2 }

cambiumToolbarDeviceConfigurationState	OBJECT-TYPE
		SYNTAX	   Integer32 (0..127)
		MAX-ACCESS read-only
		STATUS	   current
		DESCRIPTION
		"System configuration state OID.
		Bit masks:
			0000 0001 - System is configured.
			0000 0010 - There are unsaved changesets.
			0000 0100 - There are unrestarted services.
			0000 1000 - Needed reboot of the system.
			0001 0000 - Configurations was reset.
			0010 0000 - Services restarting in process.
			0100 0000 - Software Update performed.
		Device Allocation: AP, SM"
		::= { cambiumToolBarStates 3 }

cambiumToolbarSyncSource OBJECT-TYPE
		SYNTAX	   Integer32 (1|2|3|4)
		MAX-ACCESS read-only
		STATUS	   current
		DESCRIPTION
		"Sync Source Status:
			1 - GPS Sync Up, 
			2 - GPS Sync Down, 
			3 - CMM4 Sync,
			4 - CMM3 Sync
		Device Allocation: AP"
		::= { cambiumToolBarStates 4 }

cambiumToolbarGPSSyncStateStr OBJECT-TYPE
		SYNTAX	   DisplayString (SIZE(0..128))
		MAX-ACCESS read-only
		STATUS	   current
		DESCRIPTION
		"GPS Current SYNC State (text)
		Device Allocation: AP"
		::= { cambiumToolBarStates 5 }

cambiumJSONCfgImport OBJECT-TYPE
		SYNTAX	   DisplayString (SIZE(0..128))
		MAX-ACCESS read-write
		STATUS	   current
		DESCRIPTION
		"OID to start import process, when valid link to JSON configuration file
		is received.
		Device Allocation: AP, SM"
		::= { cambiumCfg 1 }

cambiumJSONCfgImportStatus OBJECT-TYPE
		SYNTAX	   Integer32 (-1..3)
		MAX-ACCESS read-only
		STATUS	   current
		DESCRIPTION
		"OID to get the status of the import process:
		-1	Error
		 0	Idle
		 1	Downloading file
		 2	Importing file
		 3	Rebooting
		Device Allocation: AP, SM"
		::= { cambiumCfg 2 }

cambiumJSONCfgImportError OBJECT-TYPE
		SYNTAX	   DisplayString (SIZE(1..128))
		MAX-ACCESS read-only
		STATUS	   current
		DESCRIPTION
		"Import config Error message (text) 
		Device Allocation: AP, SM"
		::= { cambiumCfg 3 }

cambiumJSONCfgExport OBJECT-TYPE
		SYNTAX	   Integer32 (0|1)
		MAX-ACCESS read-write
		STATUS	   current
		DESCRIPTION
		"OID to start export process
		0	No action
		1	Start
		Device Allocation: AP, SM"
		::= { cambiumCfg 10 }

cambiumJSONCfgExportStatus OBJECT-TYPE
		SYNTAX	   Integer32 (-1..4)
		MAX-ACCESS read-only
		STATUS	   current
		DESCRIPTION
		"OID to get the status of the export process:
		-1	Error
		 0	Idle
		 1	Exporting JSON config
		 2	Moving config into upload directory
		 3	Preparing link for uploading
		 4	Success
		Device Allocation: AP, SM"
		::= { cambiumCfg 11 }

cambiumJSONCfgExportError OBJECT-TYPE
		SYNTAX	   DisplayString (SIZE(1..128))
		MAX-ACCESS read-only
		STATUS	   current
		DESCRIPTION
		"Export config Error message (text)
		Device Allocation: AP, SM"
		::= { cambiumCfg 12 }

cambiumJSONCfgExportLink OBJECT-TYPE
		SYNTAX	   DisplayString (SIZE(0..128))
		MAX-ACCESS read-only
		STATUS	   current
		DESCRIPTION
		"Link to the configuration file on the board
		Device Allocation: AP, SM"
		::= { cambiumCfg 13 }

cambiumFullCfgRestore OBJECT-TYPE
		SYNTAX	   DisplayString (SIZE(0..128))
		MAX-ACCESS read-write
		STATUS	   current
		DESCRIPTION
		"OID to start restore process, when valid link to full configuration
		file is received.
		Device Allocation: AP, SM"
		::= { cambiumCfg 20 }

cambiumFullCfgRestoreStatus OBJECT-TYPE
		SYNTAX	   Integer32 (-1..5)
		MAX-ACCESS read-only
		STATUS	   current
		DESCRIPTION
		"OID to get the status of the restore process:
		-1	Error
		 0	Idle
		 1	Downloading file
		 2	Decrypting
		 3	Unpacking
		 4	Importing
		 5	Rebooting
		Device Allocation: AP, SM"
		::= { cambiumCfg 21 }

cambiumFullCfgRestoreError OBJECT-TYPE
		SYNTAX	   DisplayString (SIZE(1..128))
		MAX-ACCESS read-only
		STATUS	   current
		DESCRIPTION
		"Restore config Error message (text)
		Device Allocation: AP, SM"
		::= { cambiumCfg 22 }

cambiumFullCfgBackUp OBJECT-TYPE
		SYNTAX	   Integer32 (1..7)
		MAX-ACCESS read-write
		STATUS	   current
		DESCRIPTION
		"OID to start backup process
		Bitmask indicating which part of configuration to backup:
		001 - json-config files
		010 - files of security & certificates
		100 - log files 
		Device Allocation: AP, SM"
		::= { cambiumCfg 30 }

cambiumFullCfgBackUpStatus OBJECT-TYPE
		SYNTAX	   Integer32 (-1..5)
		MAX-ACCESS read-only
		STATUS	   current
		DESCRIPTION
		"OID to get the status of the backup process:
		-1	Error
		 0	Idle
		 1	Packing configuration files
		 2	Encrypting configuration files
		 3	Moving packed files into upload directory
		 4	Preparing link for uploading
		 5	Success
		Device Allocation: AP, SM"
		::= { cambiumCfg 31 }

cambiumFullCfgBackUpError OBJECT-TYPE
		SYNTAX	   DisplayString (SIZE(1..128))
		MAX-ACCESS read-only
		STATUS	   current
		DESCRIPTION
		"Backup config Error message (text)
		Device Allocation: AP, SM"
		::= { cambiumCfg 32 }

cambiumFullCfgBackUpLink OBJECT-TYPE
		SYNTAX	   DisplayString
		MAX-ACCESS read-only
		STATUS	   current
		DESCRIPTION
		"Link to the packed configuration files on the board, ready to upload
		Device Allocation: AP, SM"
		::= { cambiumCfg 33 }

acsEnable  OBJECT-TYPE
		SYNTAX	   Integer32 (0|1)
		MAX-ACCESS read-write
		STATUS	   current
		DESCRIPTION
		"Automatic Channel Selection (ACS) automatically selects best values for
		centerFrequency, dfsAlternative1CenterFrequency and dfsAlternative2CenterFrequency:
		 0 - Disable,
		 1 - Enable
		Device Allocation: AP"
		DEFVAL	{ 0 }
		::= { cambiumACSCfg 1 }

acsScanMinDwellTime	 OBJECT-TYPE
		SYNTAX	   Integer32 (50..500)
		MAX-ACCESS read-write
		STATUS	   current
		DESCRIPTION
		"Minimum dwell time during Automatic Channel Selection (ACS) scan in milliseconds.
		Device Allocation: AP"
		DEFVAL	{ 200 }
		::= { cambiumACSCfg 2 }

acsScanMaxDwellTime	 OBJECT-TYPE
		SYNTAX	   Integer32 (300..600)
		MAX-ACCESS read-write
		STATUS	   current
		DESCRIPTION
		"Maximum dwell time during Automatic Channel Selection (ACS) scan in milliseconds.
		Device Allocation: AP"
		DEFVAL	{ 300 }
		::= { cambiumACSCfg 3 }

acsControl	OBJECT-TYPE
		SYNTAX	   Integer32 (0..2)
		MAX-ACCESS read-write
		STATUS	   current
		DESCRIPTION
		"Automatic Channel Selection (ACS) control:
		 0 - No change,
		 1 - Run scan now,
		 2 - Abort current scan
		Device Allocation: AP"
		DEFVAL	{ 0 }
		::= { cambiumACSCfg 4 }

cambiumIDMMode OBJECT-TYPE
		SYNTAX	   Integer32 (0..1)
		MAX-ACCESS read-write
		STATUS	   current
		DESCRIPTION
		"OID to configure IDM Mode
		0 - System Wide
		1 - Local
		Device Allocation: AP, SM"
		::= { cambiumIDM 1 }

cambiumIDMTime OBJECT-TYPE
		SYNTAX	   Integer32 (1000..120000)
		MAX-ACCESS read-write
		STATUS	   current
		DESCRIPTION
		"OID to configure IDM Time.
		Device Allocation: AP, SM"
		::= { cambiumIDM 2 }

cambiumIDMEnable OBJECT-TYPE
		SYNTAX	   Integer32 (0|1)
		MAX-ACCESS read-write
		STATUS	   current
		DESCRIPTION
		"OID to enable/disable IDM feature
		0 - Disable IDM
		1 - Enable IDM
		Device Allocation: AP, SM"
		::= { cambiumIDM 3 }

cambiumIDMResultsTable OBJECT-TYPE
	SYNTAX	   SEQUENCE OF CambiumIDMResultsEntry
	MAX-ACCESS not-accessible
	STATUS	   current
	DESCRIPTION
	"This table contains information of IDM Results:
		  IDM Cycle,
		  Device MAC,
		  Last Comb RSSI,
		  Last Rate,
		  Max Rate,
		  Number of Packets,
		  CRC Comb RSSI,
		  CRC Ch0 RSSI,
		  CRC Ch1 RSSI,
		  CRC Number of Packets,
		  PRQ Comb RSSI,
		  PRQ Ch0 RSSI,
		  PRQ Ch1 RSSI,
		  PRQ Number of Packets,
	Device Allocation: AP, SM"
	::= { cambiumIDM 10 }

cambiumIDMResultsEntry OBJECT-TYPE
	SYNTAX	   CambiumIDMResultsEntry
	MAX-ACCESS not-accessible
	STATUS	   current
	DESCRIPTION
	"Wireless parameters mapping for particular device.
	Device Allocation: AP, SM"
	INDEX	{ cambiumAPNumberOfConnectedSTA }
	::= { cambiumIDMResultsTable 1 }

CambiumIDMResultsEntry ::= SEQUENCE {
		idmDeviceListCycle		  Integer32,
		idmDeviceListMAC		  DisplayString,
		idmDeviceListLCombRSSI	  Integer32,
		idmDeviceListLRate		  DisplayString,
		idmDeviceListMaxRate	  DisplayString,
		idmDeviceListPcktsNum	  Integer32,
		idmDeviceListCRCCombRSSI  Integer32,
		idmDeviceListCRCCh0RSSI	  Integer32,
		idmDeviceListCRCCh1RSSI	  Integer32,
		idmDeviceListCRCPcktsNum  Integer32,
		idmDeviceListPRQCombRSSI  Integer32,
		idmDeviceListPRQCh0RSSI	  Integer32,
		idmDeviceListPRQCh1RSSI	  Integer32,
		idmDeviceListPRQPcktsNum  Integer32
	}

idmDeviceListCycle OBJECT-TYPE
	SYNTAX	   Integer32(1..1024)
	MAX-ACCESS read-only
	STATUS	   current
	DESCRIPTION
	"IDM Cycle Number.
	Device Allocation: AP, SM"
	::= { cambiumIDMResultsEntry 1 }

idmDeviceListMAC OBJECT-TYPE
	SYNTAX	   DisplayString (SIZE(11..17))
	MAX-ACCESS read-only
	STATUS	   current
	DESCRIPTION
	"MAC Address of device collected IDM Statistics.
	Device Allocation: AP, SM"
	::= { cambiumIDMResultsEntry 2 }

idmDeviceListLCombRSSI OBJECT-TYPE
	SYNTAX	   Integer32(-128..127)
	MAX-ACCESS read-only
	STATUS	   current
	DESCRIPTION
	"Combined RSSI of last received MPDU.
	Device Allocation: AP, SM"
	::= { cambiumIDMResultsEntry 3 }

idmDeviceListLRate OBJECT-TYPE
	SYNTAX	   DisplayString (SIZE(1..5))
	MAX-ACCESS read-only
	STATUS	   current
	DESCRIPTION
	"Rate code of last received MPDU.
	Device Allocation: AP, SM"
	::= { cambiumIDMResultsEntry 4 }

idmDeviceListMaxRate OBJECT-TYPE
	SYNTAX	   DisplayString (SIZE(1..5))
	MAX-ACCESS read-only
	STATUS	   current
	DESCRIPTION
	"Maximum rate code.
	Device Allocation: AP, SM"
	::= { cambiumIDMResultsEntry 5 }

idmDeviceListPcktsNum OBJECT-TYPE
	SYNTAX	   Integer32
	MAX-ACCESS read-only
	STATUS	   current
	DESCRIPTION
	"Number of packets filtered by IDM.
	Device Allocation: AP, SM"
	::= { cambiumIDMResultsEntry 6 }

idmDeviceListCRCCombRSSI OBJECT-TYPE
	SYNTAX	   Integer32(-128..127)
	MAX-ACCESS read-only
	STATUS	   current
	DESCRIPTION
	"Combined RSSI of maximum received CRC error MPDU.
	Device Allocation: AP, SM"
	::= { cambiumIDMResultsEntry 7 }

idmDeviceListCRCCh0RSSI OBJECT-TYPE
	SYNTAX	   Integer32(-128..127)
	MAX-ACCESS read-only
	STATUS	   current
	DESCRIPTION
	"Channel 0 RSSI of maximum received CRC error MPDU.
	Device Allocation: AP, SM"
	::= { cambiumIDMResultsEntry 8 }

idmDeviceListCRCCh1RSSI OBJECT-TYPE
	SYNTAX	   Integer32(-128..127)
	MAX-ACCESS read-only
	STATUS	   current
	DESCRIPTION
	"Channel 1 RSSI of maximum received CRC error MPDU.
	Device Allocation: AP, SM"
	::= { cambiumIDMResultsEntry 9 }

idmDeviceListCRCPcktsNum OBJECT-TYPE
	SYNTAX	   Integer32
	MAX-ACCESS read-only
	STATUS	   current
	DESCRIPTION
	"Number of packets with CRC error filtered by IDM.
	Device Allocation: AP, SM"
	::= { cambiumIDMResultsEntry 10 }

idmDeviceListPRQCombRSSI OBJECT-TYPE
	SYNTAX	   Integer32(-128..127)
	MAX-ACCESS read-only
	STATUS	   current
	DESCRIPTION
	"Combined RSSI of maximum received Probe Requests MPDU.
	Device Allocation: AP, SM"
	::= { cambiumIDMResultsEntry 11 }

idmDeviceListPRQCh0RSSI OBJECT-TYPE
	SYNTAX	   Integer32(-128..127)
	MAX-ACCESS read-only
	STATUS	   current
	DESCRIPTION
	"Channel 0 RSSI of maximum received Probe Requests MPDU.
	Device Allocation: AP, SM"
	::= { cambiumIDMResultsEntry 12 }

idmDeviceListPRQCh1RSSI OBJECT-TYPE
	SYNTAX	   Integer32(-128..127)
	MAX-ACCESS read-only
	STATUS	   current
	DESCRIPTION
	"Channel 1 RSSI of maximum received Probe Requests MPDU.
	Device Allocation: AP, SM"
	::= { cambiumIDMResultsEntry 13 }

idmDeviceListPRQPcktsNum OBJECT-TYPE
	SYNTAX	   Integer32
	MAX-ACCESS read-only
	STATUS	   current
	DESCRIPTION
	"Number of Probe Requests filtered by IDM.
	Device Allocation: AP, SM"
	::= { cambiumIDMResultsEntry 14 }

cambiumIDMSumMAC OBJECT-TYPE
	SYNTAX	   DisplayString (SIZE(11..17))
	MAX-ACCESS read-write
	STATUS	   current
	DESCRIPTION
	"MAC Address of device collected IDM Summary Statistics.
	Device Allocation: AP, SM"
	::= { cambiumIDM 11 }

cambiumIDMSumLCombRSSI OBJECT-TYPE
	SYNTAX	   Integer32(-128..127)
	MAX-ACCESS read-only
	STATUS	   current
	DESCRIPTION
	"Summary Combined RSSI of last received MPDU.
	Device Allocation: AP, SM"
	::= { cambiumIDM 12 }

cambiumIDMSumLRate OBJECT-TYPE
	SYNTAX	   DisplayString (SIZE(1..5))
	MAX-ACCESS read-only
	STATUS	   current
	DESCRIPTION
	"Summary Rate code of last received MPDU.
	Device Allocation: AP, SM"
	::= { cambiumIDM 13 }

cambiumIDMSumMaxRate OBJECT-TYPE
	SYNTAX	   DisplayString (SIZE(1..5))
	MAX-ACCESS read-only
	STATUS	   current
	DESCRIPTION
	"Summary Maximum rate code.
	Device Allocation: AP, SM"
	::= { cambiumIDM 14 }

cambiumIDMSumPcktsNum OBJECT-TYPE
	SYNTAX	   Integer32
	MAX-ACCESS read-only
	STATUS	   current
	DESCRIPTION
	"Summary Number of packets filtered by IDM.
	Device Allocation: AP, SM"
	::= { cambiumIDM 15 }

cambiumIDMSumCRCCombRSSI OBJECT-TYPE
	SYNTAX	   Integer32(-128..127)
	MAX-ACCESS read-only
	STATUS	   current
	DESCRIPTION
	"Summary Combined RSSI of maximum received CRC error MPDU.
	Device Allocation: AP, SM"
	::= { cambiumIDM 16 }

cambiumIDMSumCRCCh0RSSI OBJECT-TYPE
	SYNTAX	   Integer32(-128..127)
	MAX-ACCESS read-only
	STATUS	   current
	DESCRIPTION
	"Summary Channel 0 RSSI of maximum received CRC error MPDU.
	Device Allocation: AP, SM"
	::= { cambiumIDM 17 }

cambiumIDMSumCRCCh1RSSI OBJECT-TYPE
	SYNTAX	   Integer32(-128..127)
	MAX-ACCESS read-only
	STATUS	   current
	DESCRIPTION
	"Summary Channel 1 RSSI of maximum received CRC error MPDU.
	Device Allocation: AP, SM"
	::= { cambiumIDM 18 }

cambiumIDMSumCRCPcktsNum OBJECT-TYPE
	SYNTAX	   Integer32
	MAX-ACCESS read-only
	STATUS	   current
	DESCRIPTION
	"Summary Number of packets with CRC error filtered by IDM.
	Device Allocation: AP, SM"
	::= { cambiumIDM 19 }

cambiumIDMSumPRQCombRSSI OBJECT-TYPE
	SYNTAX	   Integer32(-128..127)
	MAX-ACCESS read-only
	STATUS	   current
	DESCRIPTION
	"Summary Combined RSSI of maximum received Probe Requests MPDU.
	Device Allocation: AP, SM"
	::= { cambiumIDM 20 }

cambiumIDMSumPRQCh0RSSI OBJECT-TYPE
	SYNTAX	   Integer32(-128..127)
	MAX-ACCESS read-only
	STATUS	   current
	DESCRIPTION
	"Summary Channel 0 RSSI of maximum received Probe Requests MPDU.
	Device Allocation: AP, SM"
	::= { cambiumIDM 21 }

cambiumIDMSumPRQCh1RSSI OBJECT-TYPE
	SYNTAX	   Integer32(-128..127)
	MAX-ACCESS read-only
	STATUS	   current
	DESCRIPTION
	"Summary Channel 1 RSSI of maximum received Probe Requests MPDU.
	Device Allocation: AP, SM"
	::= { cambiumIDM 22 }

cambiumIDMSumPRQPcktsNum OBJECT-TYPE
	SYNTAX	   Integer32
	MAX-ACCESS read-only
	STATUS	   current
	DESCRIPTION
	"Summary Number of Probe Requests filtered by IDM.
	Device Allocation: AP, SM"
	::= { cambiumIDM 23 }

cambiumIDMSummaryTable OBJECT-TYPE
	SYNTAX	   SEQUENCE OF CambiumIDMSummaryEntry
	MAX-ACCESS not-accessible
	STATUS	   current
	DESCRIPTION
	"This table contains information of IDM Summary Top Interferers:
		  Intrf MAC,
		  Intrf RSSI,
		  Intrf Ch0 RSSI,
		  Intrf Ch1 RSSI,
		  Intrf SSID,
	Device Allocation: AP, SM"
	::= { cambiumIDM 30 }

cambiumIDMSummaryEntry OBJECT-TYPE
	SYNTAX	   CambiumIDMSummaryEntry
	MAX-ACCESS not-accessible
	STATUS	   current
	DESCRIPTION
	"Wireless parameters mapping for particular device.
	Device Allocation: AP, SM"
	INDEX	{ cambiumAPNumberOfConnectedSTA }
	::= { cambiumIDMSummaryTable 1 }

CambiumIDMSummaryEntry ::= SEQUENCE {
		idmSummaryIntMAC	  DisplayString,
		idmSummaryIntCombRSSI Integer32,
		idmSummaryIntCh0RSSI  Integer32,
		idmSummaryIntCh1RSSI  Integer32,
		idmSummaryIntSSID	   DisplayString
	}

idmSummaryIntMAC OBJECT-TYPE SYNTAX		DisplayString (SIZE(11..17))
	MAX-ACCESS read-only
	STATUS	   current
	DESCRIPTION
	"MAC Address of Interferer.
	Device Allocation: AP, SM"
	::= { cambiumIDMSummaryEntry 1 }
idmSummaryIntCombRSSI OBJECT-TYPE SYNTAX	 Integer32(-128..127)
	MAX-ACCESS read-only
	STATUS	   current
	DESCRIPTION
	"Interferer Combined RSSI.
	Device Allocation: AP, SM"
	::= { cambiumIDMSummaryEntry 2 }
idmSummaryIntCh0RSSI OBJECT-TYPE SYNTAX		Integer32(-128..127)
	MAX-ACCESS read-only
	STATUS	   current
	DESCRIPTION
	"Interferer Channel 0 RSSI.
	Device Allocation: AP, SM"
	::= { cambiumIDMSummaryEntry 3 }
idmSummaryIntCh1RSSI OBJECT-TYPE SYNTAX		Integer32(-128..127)
	MAX-ACCESS read-only
	STATUS	   current
	DESCRIPTION
	"Interferer Channel 1 RSSI.
	Device Allocation: AP, SM"
	::= { cambiumIDMSummaryEntry 4 }
idmSummaryIntSSID OBJECT-TYPE SYNTAX	 DisplayString (SIZE(0..32))
	MAX-ACCESS read-only
	STATUS	   current
	DESCRIPTION
	"SSID name of Interferer.
	Device Allocation: AP, SM"
	::= { cambiumIDMSummaryEntry 5 } 

END




File: /dude_custom_files\IEEE802dot11-MIB.txt
-- -*- mib -*-
-- **********************************************************************
-- * IEEE 802.11 Management Information Base
-- **********************************************************************
IEEE802dot11-MIB DEFINITIONS ::= BEGIN
    IMPORTS
        MODULE-IDENTITY, OBJECT-TYPE, 
        NOTIFICATION-TYPE,Integer32, Counter32  FROM SNMPv2-SMI
        DisplayString , MacAddress, RowStatus,
        TruthValue                              FROM SNMPv2-TC
        MODULE-COMPLIANCE, OBJECT-GROUP, 
        NOTIFICATION-GROUP                      FROM SNMPv2-CONF 
        ifIndex                                 FROM RFC1213-MIB;

-- **********************************************************************
-- *  MODULE IDENTITY
-- **********************************************************************
    ieee802dot11 MODULE-IDENTITY
    LAST-UPDATED "9807080000Z"
    ORGANIZATION "IEEE 802.11"
    CONTACT-INFO 
           "WG E-mail: stds-802-11@ieee.org

                Chair: Vic Hayes
               Postal: Lucent Technologies, Inc.
                       Zadelstede 1-10
                       Nieuwegein, Netherlands
                       3431 JZ
                  Tel: +31 30 609 7528
                  Fax: +31 30 231 6233
               E-mail: vichayes@lucent.com

               Editor: Bob O'Hara
               Postal: Informed Technology, Inc.
                       1750 Nantucket Circle, Suite 138
                       Santa Clara, CA 95054 USA
                  Tel: +1 408 986 9596
                  Fax: +1 408 727 2654
               E-mail: bob@informed-technology.com"
    DESCRIPTION
        "The MIB module for IEEE 802.11 entities.
        iso(1).member-body(2).us(840).ieee802dot11(10036)"
    ::= { 1 2 840 10036 }

-- **********************************************************************
-- *  Major sections
-- **********************************************************************
--  Station ManagemenT (SMT) Attributes
    --  DEFINED AS "The SMT object class provides the necessary support at the
    --  station to manage the processes in the station such that the
    --  station may work cooperatively as a part of an IEEE 802.11 network.";

    dot11smt OBJECT IDENTIFIER ::=   {ieee802dot11 1}

      --  dot11smt GROUPS
      --  dot11StationConfigTable            ::= {dot11smt 1}
      --  dot11AuthenticationAlgorithmsTable ::= {dot11smt 2}
      --  dot11WEPDefaultKeysTable           ::= {dot11smt 3}
      --  dot11WEPKeyMappingsTable           ::= {dot11smt 4}
      --  dot11PrivacyTable                  ::= {dot11smt 5}
      --  dot11SMTnotification               ::= {dot11smt 6}

--  MAC Attributes
    --  DEFINED AS "The MAC object class provides the necessary support
    --  for the access control, generation, and verification of frame check
    --  sequences, and proper delivery of valid data to upper layers.";

    dot11mac OBJECT IDENTIFIER ::=   {ieee802dot11 2}

      --  MAC GROUPS
      --  reference IEEE Std 802.1f-1993
         --  dot11OperationTable   	::=    {dot11mac 1}
         --  dot11CountersTable    	::=    {dot11mac 2}
         --  dot11GroupAddressesTable 	::=    {dot11mac 3}

--  Resource Type ID
      dot11res OBJECT IDENTIFIER 		::=   {ieee802dot11 3}
      dot11resAttribute OBJECT IDENTIFIER 	::=   {dot11res 1 }

--  PHY Attributes
    --  DEFINED AS "The PHY object class provides the necessary support
    --  for required PHY operational information that may vary from PHY
    --  to PHY and from STA to STA to be communicated to upper layers."

   dot11phy OBJECT IDENTIFIER ::=   {ieee802dot11 4}

    --  phy GROUPS
    --  dot11PhyOperationTable    	::=  {dot11phy 1}
--  dot11PhyAntennaTable      		::=  {dot11phy 2}
    --  dot11PhyTxPowerTable      	::=  {dot11phy 3}
    --  dot11PhyFHSSTable         	::=  {dot11phy 4}
    --  dot11PhyDSSSTable         	::=  {dot11phy 5}
    --  dot11PhyIRTable           	::=  {dot11phy 6}
    --  dot11RegDomainsSupportedTable   ::=  {dot11phy 7}
    --  dot11AntennasListTable          ::=  {dot11phy 8}
    --  dot11SupportedDataRatesTxTable  ::=  {dot11phy 9}
    --  dot11SupportedDataRatesRxTable  ::=  {dot11phy 10}


-- **********************************************************************
-- *  Textual conventions from 802 definitions
-- **********************************************************************
    WEPKeytype ::= OCTET STRING (SIZE (5))

-- **********************************************************************
-- *  MIB attribute OBJECT-TYPE definitions follow
-- **********************************************************************

-- **********************************************************************
-- *  SMT Station Config  Table
-- **********************************************************************
dot11StationConfigTable OBJECT-TYPE
        SYNTAX SEQUENCE OF Dot11StationConfigEntry
        MAX-ACCESS not-accessible
        STATUS current
        DESCRIPTION
            "Station Configuration attributes.  In tablular form to
            allow for multiple instances on an agent."
    ::= {  dot11smt 1 }

dot11StationConfigEntry OBJECT-TYPE
        SYNTAX Dot11StationConfigEntry
        MAX-ACCESS not-accessible
        STATUS current
        DESCRIPTION

            "An entry in the dot11StationConfigTable.  It is
            possible for there to be multiple IEEE 802.11 interfaces
            on one agent, each with its unique MAC address. The
            relationship between an IEEE 802.11 interface and an
            interface in the context of the Internet-standard MIB is
            one-to-one.  As such, the value of an ifIndex object
            instance can be directly used to identify corresponding
            instances of the objects defined herein.  

            ifIndex - Each 802.11 interface is represented by an
            ifEntry.  Interface tables in this MIB module are indexed
            by ifIndex."


        INDEX {ifIndex}
    ::= {  dot11StationConfigTable 1 }

Dot11StationConfigEntry ::=
        SEQUENCE {
         	dot11StationID                     MacAddress,
             	dot11MediumOccupancyLimit          INTEGER,
             	dot11CFPollable                    TruthValue,
             	dot11CFPPeriod                     INTEGER, 
             	dot11CFPMaxDuration                INTEGER,
             	dot11AuthenticationResponseTimeOut INTEGER,
             	dot11PrivacyOptionImplemented      TruthValue,
		dot11PowerManagementMode	   INTEGER,
		dot11DesiredSSID		   OCTET STRING,
		dot11DesiredBSSType		   INTEGER,
		dot11OperationalRateSet		   OCTET STRING,
		dot11BeaconPeriod		   INTEGER,
		dot11DTIMPeriod			   INTEGER,
		dot11AssociationResponseTimeOut	   INTEGER,
             	dot11DisassociateReason            INTEGER,
             	dot11DisassociateStation           MacAddress,
             	dot11DeauthenticateReason          INTEGER,
             	dot11DeauthenticateStation         MacAddress,
             	dot11AuthenticateFailStatus        INTEGER,
             	dot11AuthenticateFailStation       MacAddress }

dot11StationID OBJECT-TYPE
        SYNTAX MacAddress
        MAX-ACCESS read-write
        STATUS deprecated
        DESCRIPTION

            "The purpose of dot11StationID is to allow a manager to identify
            a station for its own purposes.  This attribute provides
            for that eventuality while keeping the true MAC address
            independent.  Its syntax is MAC address and default value
            is the station's assigned, unique MAC address."

    ::= { dot11StationConfigEntry 1 }

dot11MediumOccupancyLimit OBJECT-TYPE
        SYNTAX INTEGER (0..1000)
        MAX-ACCESS read-write
        STATUS current
        DESCRIPTION

            "This attribute shall indicate the maximum amount of time,
            in TU, that a point coordinator may control the usage of
            the wireless medium without relinquishing control for long
            enough to allow at least one instance of DCF access to the
            medium.  The default value of this attribute shall be 100,
            and the maximum value shall be 1000."

    ::= { dot11StationConfigEntry 2 }

dot11CFPollable OBJECT-TYPE
        SYNTAX TruthValue
        MAX-ACCESS read-only
        STATUS current
        DESCRIPTION

        "When this attribute is true, it shall indicate that the STA
        is able to respond to a CF-Poll with a data frame within a
        SIFS time. This attribute shall be false if the STA is not
        able to respond to a CF-Poll with a data frame within a SIFS
        time."

    ::= { dot11StationConfigEntry 3 }

dot11CFPPeriod OBJECT-TYPE
        SYNTAX INTEGER (0..255)
        MAX-ACCESS read-write
        STATUS current
        DESCRIPTION

            "The attribute shall describe the number of DTIM intervals
            between the start of CFPs.  It is modified by
            MLME-START.request primitive."

::= {  dot11StationConfigEntry 4 }

dot11CFPMaxDuration OBJECT-TYPE
        SYNTAX INTEGER (0..65535)
        MAX-ACCESS read-write
        STATUS current
        DESCRIPTION

        "The attribute shall describe the maximum duration of the CFP
        in TU that may be generated by the PCF. It is modified by
        MLME-START.request primitive."

::= {  dot11StationConfigEntry 5 }

dot11AuthenticationResponseTimeOut OBJECT-TYPE
        SYNTAX INTEGER (1..4294967295)
        MAX-ACCESS read-write
        STATUS current
        DESCRIPTION

            "This attribute shall specify the number of TU that a
            responding STA should wait for the next frame in the
            authentication sequence."

    ::= {  dot11StationConfigEntry 6 }

dot11PrivacyOptionImplemented OBJECT-TYPE
        SYNTAX TruthValue
        MAX-ACCESS read-only
        STATUS current
        DESCRIPTION

            "This attribute, when true, shall indicate that the IEEE
             802.11 WEP option is implemented.  The default value of
             this attribute shall be false."

    ::= {  dot11StationConfigEntry 7 }

dot11PowerManagementMode OBJECT-TYPE
		SYNTAX INTEGER { active(1), powersave(2) }
		MAX-ACCESS read-write
		STATUS current
		DESCRIPTION
			"This attribute shall specify the power management
			 mode of the STA. When set to active, it shall indicate
			 that the station is not in power-save mode. When set
			 to powersave, it shall indicate that the station is
			 in power-save mode. The power management mode is
			 transmitted in all frames according to the rules
			 in  7.1.3.1.7."
	::= { dot11StationConfigEntry 8 }

dot11DesiredSSID OBJECT-TYPE
		SYNTAX OCTET STRING (SIZE(0..32))
		MAX-ACCESS read-write
		STATUS current
		DESCRIPTION
			"This attribute reflects the Service Set ID used
			in the DesiredSSID parameter of the most recent
			MLME_Scan.request.  This value may be modified
			by an external management entity and used by the
			local SME to make decisions about the Scanning process."
	::= { dot11StationConfigEntry 9 }

dot11DesiredBSSType OBJECT-TYPE
		SYNTAX INTEGER { infrastructure(1), independent(2), any(3) }
		MAX-ACCESS read-write
		STATUS current
		DESCRIPTION
			"This attribute shall specify the type of BSS the
			 station shall use when scanning for a BSS with which
			 to synchronize. This value is used to filter Probe
			 Response frames and Beacons. When set to infrastructure,
			 the station shall only synchronize with a BSS whose
			 Capability Information field has the ESS subfield set
			 to 1. When set to independent, the station shall only
			 synchronize with a BSS whose Capability Information
			 field has the IBSS subfield set to 1. When set to
			 any, the station may synchronize to either type of
			 BSS."
	::= { dot11StationConfigEntry 10 }

dot11OperationalRateSet OBJECT-TYPE
		SYNTAX OCTET STRING (SIZE(1..126))
		MAX-ACCESS read-write
		STATUS current
		DESCRIPTION
			"This attribute shall specify the set of data rates
			 at which the station may transmit data.  Each octet
 contains a value representing a rate.  Each rate
			 shall be within the range from 2 to 127,
			 corresponding to data rates in increments of
			 500 kb/s from 1 Mb/s to 63.5 Mb/s, and shall be
			 supported (as indicated in the supported rates
			 table) for receiving data. This value is reported in
			 transmitted Beacon, Probe Request, Probe Response,
			 Association Request, Association Response,
			 Reassociation Request, and Reassociation Response
			 frames, and is used to determine whether a BSS
			 with which the station desires to synchronize is
			 suitable. It is also used when starting a BSS,
			 as specified in  10.3."
	::= { dot11StationConfigEntry 11 }

dot11BeaconPeriod OBJECT-TYPE
		SYNTAX INTEGER (1..65535)
		MAX-ACCESS read-write
		STATUS current
		DESCRIPTION
			"This attribute shall specify the number of TU that a
			 station shall use for scheduling Beacon transmissions.
			 This value is transmitted in Beacon and Probe Response
			 frames."
	::= { dot11StationConfigEntry 12 }

dot11DTIMPeriod OBJECT-TYPE
		SYNTAX INTEGER(1..255)
		MAX-ACCESS read-write
		STATUS current
		DESCRIPTION
			"This attribute shall specify the number of beacon
			 intervals that shall elapse between transmission of
			 Beacons frames containing a TIM element whose DTIM
			 Count field is 0. This value is transmitted in
			 the DTIM Period field of Beacon frames."
	::= { dot11StationConfigEntry 13 }

dot11AssociationResponseTimeOut OBJECT-TYPE
		SYNTAX INTEGER(1..4294967295)
		MAX-ACCESS read-write
		STATUS current
		DESCRIPTION
			"This attribute shall specify the number of TU that a
			 requesting STA should wait for a response to a
			 transmitted association-request MMPDU."
	::= { dot11StationConfigEntry 14 }

dot11DisassociateReason OBJECT-TYPE
		SYNTAX INTEGER(0..65535)
		MAX-ACCESS read-only
		STATUS current
		DESCRIPTION
			"This attribute holds the most recently
			transmitted Reason Code in a Disassociation
			frame.  If no Disassociation frame has been
			transmitted, the value of this attribute shall
			be 0."

REFERENCE "IEEE Std 802.11-1997, 7.3.1.7"
	::= { dot11StationConfigEntry 15 }

dot11DisassociateStation OBJECT-TYPE
		SYNTAX MacAddress
		MAX-ACCESS read-only
		STATUS current
		DESCRIPTION
			"This attribute holds the MAC address from the
			Address 1 field of the most recently transmitted
			Disassociation frame.  If no Disassociation
			frame has been transmitted, the value of this
			attribute shall be 0."
	::= { dot11StationConfigEntry 16 }

dot11DeauthenticateReason OBJECT-TYPE
		SYNTAX INTEGER(0..65535)
		MAX-ACCESS read-only
		STATUS current
		DESCRIPTION
			"This attribute holds the most recently
			transmitted Reason Code in a Deauthentication
			frame.  If no Deauthentication frame has been
			transmitted, the value of this attribute shall
			be 0."

REFERENCE "IEEE Std 802.11-1997, 7.3.1.7"
	::= { dot11StationConfigEntry 17 }


dot11DeauthenticateStation OBJECT-TYPE
		SYNTAX MacAddress
		MAX-ACCESS read-only
		STATUS current
		DESCRIPTION
			"This attribute holds the MAC address from the
			Address 1 field of the most recently transmitted
			Deauthentication frame.  If no Deauthentication
			frame has been transmitted, the value of this
			attribute shall be 0."
	::= { dot11StationConfigEntry 18 }

dot11AuthenticateFailStatus OBJECT-TYPE
		SYNTAX INTEGER(0..65535)
		MAX-ACCESS read-only
		STATUS current
		DESCRIPTION
			"This attribute holds the most recently
			transmitted Status Code in a failed
			Authentication frame.  If no failed
			Authentication frame has been transmitted, the
			value of this attribute shall be 0."

REFERENCE "IEEE Std 802.11-1997, 7.3.1.9"
	::= { dot11StationConfigEntry 19 }

dot11AuthenticateFailStation OBJECT-TYPE
		SYNTAX MacAddress
		MAX-ACCESS read-only
		STATUS current
		DESCRIPTION
			"This attribute holds the MAC address from the
			Address 1 field of the most recently transmitted
			failed Authentication frame.  If no failed
			Authentication frame has been transmitted, the
			value of this attribute shall be 0."
	::= { dot11StationConfigEntry 20 }


-- **********************************************************************
-- *    End of dot11StationConfig  TABLE
-- **********************************************************************

-- **********************************************************************
-- *    AuthenticationAlgorithms  TABLE
-- **********************************************************************
dot11AuthenticationAlgorithmsTable OBJECT-TYPE
        SYNTAX SEQUENCE OF Dot11AuthenticationAlgorithmsEntry
        MAX-ACCESS not-accessible
        STATUS current
        DESCRIPTION
            "This (conceptual) table of attributes shall be a set of
            all the authentication algorithms supported by the
            stations.  The following are the default values and the
            associated algorithm:
                Value = 1: Open System
                Value = 2: Shared Key"
        REFERENCE "IEEE Std 802.11-1997, 7.3.1.1"
    ::= {  dot11smt 2 }

dot11AuthenticationAlgorithmsEntry OBJECT-TYPE
        SYNTAX Dot11AuthenticationAlgorithmsEntry
        MAX-ACCESS not-accessible
        STATUS current
        DESCRIPTION

            "An Entry (conceptual row) in the Authentication
            Algorithms Table.  

            ifIndex - Each 802.11 interface is represented by an
            ifEntry.  Interface tables in this MIB module are indexed
            by ifIndex."

        INDEX { ifIndex,
              dot11AuthenticationAlgorithmsIndex}
    ::= {  dot11AuthenticationAlgorithmsTable  1 }

Dot11AuthenticationAlgorithmsEntry ::= SEQUENCE {
            dot11AuthenticationAlgorithmsIndex	Integer32,
            dot11AuthenticationAlgorithm      	INTEGER,
	    dot11AuthenticationAlgorithmsEnable	TruthValue }


dot11AuthenticationAlgorithmsIndex OBJECT-TYPE
        SYNTAX Integer32
        MAX-ACCESS not-accessible
        STATUS current
        DESCRIPTION
            "The auxiliary variable used to identify instances
            of the columnar objects in the Authentication Algorithms Table."
    ::= {  dot11AuthenticationAlgorithmsEntry 1 }

dot11AuthenticationAlgorithm OBJECT-TYPE
        SYNTAX INTEGER {  openSystem (1),   sharedKey (2) }
        MAX-ACCESS read-only
        STATUS current
        DESCRIPTION

        "This attribute shall be a set of all the authentication
        algorithms supported by the STAs. The following are the
        default values and the associated algorithm.  
        Value = 1: Open System 
        Value = 2: Shared Key"

    ::= {  dot11AuthenticationAlgorithmsEntry 2 }

dot11AuthenticationAlgorithmsEnable  OBJECT-TYPE
        SYNTAX TruthValue
        MAX-ACCESS read-write
        STATUS current
        DESCRIPTION

        "This attribute, when true at a station, shall enable the acceptance 
        of the authentication algorithm described in the corresponding table 
        entry in authentication frames received by the station that have odd 
        authentication sequence numbers.  The default value of this attribute 
        shall be 1 for the Open System table entry and 2 for all other table 
        entries."

    ::= {  dot11AuthenticationAlgorithmsEntry 3 }

-- **********************************************************************
-- *    End of AuthenticationAlgorithms  TABLE
-- **********************************************************************

-- **********************************************************************
-- *    WEPDefaultKeys  TABLE
-- **********************************************************************
dot11WEPDefaultKeysTable OBJECT-TYPE
        SYNTAX SEQUENCE OF Dot11WEPDefaultKeysEntry
        MAX-ACCESS not-accessible
        STATUS current
        DESCRIPTION

            "Conceptual table for WEP default keys.  This table shall
            contain the four WEP default secret key values
            corresponding to the four possible KeyID values.  The WEP
            default secret keys are logically WRITE-ONLY.  Attempts to
            read the entries in this table shall return unsuccessful
            status and values of null or zero.  The default value of
            each WEP default key shall be null."

        REFERENCE "IEEE Std 802.11-1997, 8.3.2"
    ::= {  dot11smt 3 }

dot11WEPDefaultKeysEntry OBJECT-TYPE
        SYNTAX Dot11WEPDefaultKeysEntry
        MAX-ACCESS not-accessible
        STATUS current
        DESCRIPTION

            "An Entry (conceptual row) in the WEP Default Keys Table.

            ifIndex - Each 802.11 interface is represented by an
            ifEntry.  Interface tables in this MIB module are indexed
            by ifIndex."

        INDEX {ifIndex, dot11WEPDefaultKeyIndex}
    ::= {  dot11WEPDefaultKeysTable  1 }

Dot11WEPDefaultKeysEntry ::= SEQUENCE {
            dot11WEPDefaultKeyIndex     INTEGER,
            dot11WEPDefaultKeyValue     WEPKeytype}

dot11WEPDefaultKeyIndex OBJECT-TYPE
        SYNTAX INTEGER (1..4)
        MAX-ACCESS not-accessible
        STATUS current
        DESCRIPTION
            "The auxiliary variable used to identify instances
            of the columnar objects in the WEP Default Keys Table.
The value of this variable is equal to the WEPDefaultKeyID + 1"
    ::= {  dot11WEPDefaultKeysEntry 1 }

dot11WEPDefaultKeyValue OBJECT-TYPE
        SYNTAX WEPKeytype
        MAX-ACCESS read-write
        STATUS current
        DESCRIPTION
            "A WEP default secret key value."
    ::= {  dot11WEPDefaultKeysEntry 2 }

-- **********************************************************************
-- *    End of WEPDefaultKeys  TABLE
-- **********************************************************************

-- **********************************************************************
-- *    WEPKeyMappings  TABLE
-- **********************************************************************
dot11WEPKeyMappingsTable OBJECT-TYPE
        SYNTAX SEQUENCE OF Dot11WEPKeyMappingsEntry
        MAX-ACCESS not-accessible
        STATUS current
        DESCRIPTION
            "Conceptual table for WEP Key Mappings.  The MIB supports
            the ability to share a separate WEP key for each RA/TA
            pair.  The Key Mappings Table contains zero or one entry
            for each MAC address and contains two fields for each
            entry: WEPOn and the corresponding WEP key.  The WEP key
            mappings are logically WRITE-ONLY.  Attempts to read the
            entries in this table shall return unsuccessful status and
            values of null or zero.  The default value for all WEPOn
            fields is false."
        REFERENCE "IEEE Std 802.11-1997, 8.3.2"
    ::= {  dot11smt 4 }

dot11WEPKeyMappingsEntry OBJECT-TYPE
        SYNTAX Dot11WEPKeyMappingsEntry
        MAX-ACCESS not-accessible
        STATUS current
        DESCRIPTION

            "An Entry (conceptual row) in the WEP Key Mappings Table.

            ifIndex - Each 802.11 interface is represented by an
            ifEntry.  Interface tables in this MIB module are indexed
            by ifIndex."

        INDEX {ifIndex, dot11WEPKeyMappingIndex}
    ::= {  dot11WEPKeyMappingsTable  1 }

Dot11WEPKeyMappingsEntry ::= SEQUENCE {
            dot11WEPKeyMappingIndex	Integer32,
            dot11WEPKeyMappingAddress   MacAddress,
            dot11WEPKeyMappingWEPOn 	TruthValue,
            dot11WEPKeyMappingValue     WEPKeytype,
	    dot11WEPKeyMappingStatus	RowStatus }

dot11WEPKeyMappingIndex OBJECT-TYPE
        SYNTAX Integer32 
        MAX-ACCESS not-accessible
        STATUS current
        DESCRIPTION
            "The auxiliary variable used to identify instances
            of the columnar objects in the WEP Key Mappings Table."
    ::= {  dot11WEPKeyMappingsEntry 1 }

dot11WEPKeyMappingAddress OBJECT-TYPE
        SYNTAX MacAddress
        MAX-ACCESS read-create
        STATUS current
        DESCRIPTION
            "The MAC address of the STA for which the values from this
            key mapping entry are to be used."
    ::= {  dot11WEPKeyMappingsEntry 2 }

dot11WEPKeyMappingWEPOn OBJECT-TYPE
        SYNTAX TruthValue
        MAX-ACCESS read-create
        STATUS current
        DESCRIPTION
            "Boolean as to whether WEP is to be used when communicating
            with the dot11WEPKeyMappingAddress STA."
    ::= {  dot11WEPKeyMappingsEntry 3 }

dot11WEPKeyMappingValue OBJECT-TYPE
        SYNTAX WEPKeytype
        MAX-ACCESS read-create
        STATUS current
        DESCRIPTION
            "A WEP secret key value."
    ::= {  dot11WEPKeyMappingsEntry 4 }

dot11WEPKeyMappingStatus OBJECT-TYPE
        SYNTAX RowStatus
        MAX-ACCESS read-create
        STATUS current
        DESCRIPTION

            "The status column used for creating, modifying, and
            deleting instances of the columnar objects in the WEP key
            mapping Table."

        DEFVAL {active}
    ::= { dot11WEPKeyMappingsEntry 5 }

-- **********************************************************************
-- *    End of WEPKeyMappings  TABLE
-- **********************************************************************

-- **********************************************************************
-- *    dot11PrivacyTable  TABLE
-- **********************************************************************
dot11PrivacyTable OBJECT-TYPE
        SYNTAX SEQUENCE OF Dot11PrivacyEntry
        MAX-ACCESS not-accessible
        STATUS current
        DESCRIPTION

            "Group containing attributes concerned with IEEE 802.11
            Privacy.  Created as a table to allow multiple
            instantiations on an agent."

    ::= {  dot11smt 5 }

dot11PrivacyEntry OBJECT-TYPE
        SYNTAX Dot11PrivacyEntry
        MAX-ACCESS not-accessible
        STATUS current
        DESCRIPTION
            "An entry in the dot11PrivacyTable Table.

            ifIndex - Each 802.11 interface is represented by an
            ifEntry.  Interface tables in this MIB module are indexed
            by ifIndex."
        INDEX {ifIndex}
    ::= {  dot11PrivacyTable 1 }

Dot11PrivacyEntry ::= SEQUENCE {
             dot11PrivacyInvoked                TruthValue,
             dot11WEPDefaultKeyID               INTEGER,
             dot11WEPKeyMappingLength           INTEGER,
             dot11ExcludeUnencrypted            TruthValue,
             dot11WEPICVErrorCount              Counter32,
             dot11WEPExcludedCount              Counter32}


dot11PrivacyInvoked OBJECT-TYPE
        SYNTAX TruthValue
        MAX-ACCESS read-write
        STATUS current
        DESCRIPTION

        "When this attribute is true, it shall indicate that the IEEE
        802.11 WEP mechanism is used for transmitting frames of type
        Data. The default value of this attribute shall be false."
    ::= {  dot11PrivacyEntry 1 }

dot11WEPDefaultKeyID  OBJECT-TYPE
        SYNTAX INTEGER (0..3)
        MAX-ACCESS read-write
        STATUS current
        DESCRIPTION

            "This attribute shall indicate the use of the first,
            second, third, or fourth element of the WEPDefaultKeys
            array when set to values of zero, one, two, or three.  The
            default value of this attribute shall be 0."
        REFERENCE "IEEE Std 802.11-1997, 8.3.2"
    ::= {  dot11PrivacyEntry 2 }

dot11WEPKeyMappingLength  OBJECT-TYPE
        SYNTAX INTEGER (10..4294967295)
        MAX-ACCESS read-write
        STATUS current
        DESCRIPTION
            "The maximum number of tuples that dot11WEPKeyMappings can hold."
        REFERENCE "IEEE Std 802.11-1997, 8.3.2"
    ::= {  dot11PrivacyEntry 3 }

dot11ExcludeUnencrypted  OBJECT-TYPE
        SYNTAX TruthValue
        MAX-ACCESS read-write
        STATUS current
        DESCRIPTION

        "When this attribute is true, the STA shall not indicate at
        the MAC service interface received MSDUs that have the WEP
        subfield of the Frame Control field equal to zero. When this
        attribute is false, the STA may accept MSDUs that have the WEP
        subfield of the Frame Control field equal to zero. The default
        value of this attribute shall be false."

    ::= {  dot11PrivacyEntry 4 }

dot11WEPICVErrorCount  OBJECT-TYPE
        SYNTAX Counter32
        MAX-ACCESS read-only
        STATUS current
        DESCRIPTION
            "This counter shall increment when a frame is received with the
            WEP subfield of the Frame Control field set to one and the value
            of the ICV as received in the frame does not match the ICV value
            that is calculated for the contents of the received frame."
    ::= {  dot11PrivacyEntry 5 }

dot11WEPExcludedCount  OBJECT-TYPE
        SYNTAX Counter32
        MAX-ACCESS read-only
        STATUS current
        DESCRIPTION
            "This counter shall increment when a frame is received with the
            WEP subfield of the Frame Control field set to zero and the value
            of dot11ExcludeUnencrypted causes that frame to be discarded."
    ::= {  dot11PrivacyEntry 6 }

-- **********************************************************************
-- *    End of dot11Privacy  TABLE
-- **********************************************************************

-- **********************************************************************
-- *    SMT notification Objects
-- **********************************************************************
    dot11SMTnotification OBJECT IDENTIFIER ::= { dot11smt 6 }

dot11Disassociate NOTIFICATION-TYPE
        OBJECTS { ifIndex, dot11DisassociateReason, dot11DisassociateStation }
        STATUS current
        DESCRIPTION

        "The disassociate notification shall be sent when the STA
        sends a Disassociation frame. The value of the notification
        shall include the MAC address of the MAC to which the Disassociation
        frame was sent and the reason for the disassociation.

            ifIndex - Each 802.11 interface is represented by an
            ifEntry.  Interface tables in this MIB module are indexed
            by ifIndex."

    ::= { dot11SMTnotification 0 1 }

dot11Deauthenticate NOTIFICATION-TYPE
        OBJECTS { ifIndex, dot11DeauthenticateReason, dot11DeauthenticateStation }
        STATUS current
        DESCRIPTION

        "The deauthenticate notification shall be sent when the STA
        sends a Deauthentication frame. The value of the notification
        shall include the MAC address of the MAC to which the Deauthentication
        frame was sent and the reason for the deauthentication.

            ifIndex - Each 802.11 interface is represented by an
            ifEntry.  Interface tables in this MIB module are indexed
            by ifIndex."

    ::= { dot11SMTnotification 0 2 }

dot11AuthenticateFail NOTIFICATION-TYPE
        OBJECTS { ifIndex, dot11AuthenticateFailStatus, dot11AuthenticateFailStation }
        STATUS current
        DESCRIPTION

        "The authenticate failure notification shall be sent when the STA
        sends an Authentication frame with a status code other than 
        ?successful?. The value of the notification
        shall include the MAC address of the MAC to which the Authentication
        frame was sent and the reason for the authentication failure.

            ifIndex - Each 802.11 interface is represented by an
            ifEntry.  Interface tables in this MIB module are indexed
            by ifIndex."

::= { dot11SMTnotification 0 3 }


-- **********************************************************************
-- *    End of SMT notification Objects
-- **********************************************************************

-- **********************************************************************
-- *    MAC Attribute Templates
-- **********************************************************************

-- **********************************************************************
-- *    dot11OperationTable  TABLE
-- **********************************************************************
dot11OperationTable OBJECT-TYPE
        SYNTAX SEQUENCE OF Dot11OperationEntry
        MAX-ACCESS not-accessible
        STATUS current
        DESCRIPTION

            "Group contains MAC attributes pertaining to the operation
            of the MAC.  This has been implemented as a table in order
            to allow for multiple instantiations on an agent."

    ::= {  dot11mac 1 }

dot11OperationEntry OBJECT-TYPE
        SYNTAX Dot11OperationEntry
        MAX-ACCESS not-accessible
        STATUS current
        DESCRIPTION
            "An entry in the dot11OperationEntry Table.

            ifIndex - Each 802.11 interface is represented by an
            ifEntry.  Interface tables in this MIB module are indexed
            by ifIndex."
        INDEX {ifIndex}
    ::= {  dot11OperationTable 1 }

Dot11OperationEntry ::= SEQUENCE {
            dot11MACAddress                 MacAddress,
            dot11RTSThreshold               INTEGER,
            dot11ShortRetryLimit            INTEGER,
            dot11LongRetryLimit             INTEGER,
            dot11FragmentationThreshold     INTEGER,
            dot11MaxTransmitMSDULifetime    INTEGER,
            dot11MaxReceiveLifetime         INTEGER,
            dot11ManufacturerID             DisplayString,
            dot11ProductID                  DisplayString}


dot11MACAddress OBJECT-TYPE
        SYNTAX MacAddress

        MAX-ACCESS read-only
        STATUS current
        DESCRIPTION
                "Unique MAC Address assigned to the STA."
    ::= {  dot11OperationEntry 1 }

dot11RTSThreshold OBJECT-TYPE
        SYNTAX INTEGER (0..2347)
        MAX-ACCESS read-write
        STATUS current
        DESCRIPTION

        "This attribute shall indicate the number of octets in an MPDU,
        below which an RTS/CTS handshake shall not be performed. An
        RTS/CTS handshake shall be performed at the beginning of any
        frame exchange sequence where the MPDU is of type Data or
        Management, the MPDU has an individual address in the Address1
        field, and the length of the MPDU is greater than
        this threshold. (For additional details, refer to Table 21 in
        9.7.) Setting this attribute to be larger than the maximum
        MSDU size shall have the effect of turning off the RTS/CTS
        handshake for frames of Data or Management type transmitted by
        this STA. Setting this attribute to zero shall have the effect
        of turning on the RTS/CTS handshake for all frames of Data or
        Management type transmitted by this STA. The default value of
        this attribute shall be 2347."

    ::= {  dot11OperationEntry 2 }

dot11ShortRetryLimit OBJECT-TYPE
        SYNTAX INTEGER (1..255)
        MAX-ACCESS read-write
        STATUS current
        DESCRIPTION

        "This attribute shall indicate the maximum number of
        transmission attempts of a frame, the length of which is less
        than or equal to dot11RTSThreshold, that shall be made before a
        failure condition is indicated. The default value of this
        attribute shall be 7."

    ::= {  dot11OperationEntry 3 }

dot11LongRetryLimit OBJECT-TYPE
        SYNTAX INTEGER (1..255)
        MAX-ACCESS read-write
        STATUS current
        DESCRIPTION

        "This attribute shall indicate the maximum number of
        transmission attempts of a frame, the length of which is
        greater than dot11RTSThreshold, that shall be made before a
        failure condition is indicated. The default value of this
        attribute shall be 4."

    ::= {  dot11OperationEntry 4 }

dot11FragmentationThreshold OBJECT-TYPE
        SYNTAX INTEGER (256..2346)
        MAX-ACCESS read-write
        STATUS current

        DESCRIPTION

        "This attribute shall specify the current maximum size, in
        octets, of the MPDU that may be delivered to the PHY. An MSDU
        shall be broken into fragments if its size exceeds the value
of this attribute after adding MAC headers and trailers. An MSDU or MMPDU shall be fragmented when the resulting frame has an individual address in the Address1 field, and the length of the frame is larger than this threshold. The default value for this attribute shall be the lesser of 2346 or the aMPDUMaxLength of the attached PHY and shall never exceed the lesser of 2346 or the  aMPDUMaxLength of the attached PHY. The value of this attribute shall never be less than 256. "

    ::= {  dot11OperationEntry 5 }

dot11MaxTransmitMSDULifetime OBJECT-TYPE
        SYNTAX INTEGER (1..4294967295)
        MAX-ACCESS read-write
        STATUS current
        DESCRIPTION

        "The MaxTransmitMSDULifetime shall be the elapsed time in TU,
        after the initial transmission of an MSDU, after which further
        attempts to transmit the MSDU shall be terminated. The default
        value of this attribute shall be 512."

    ::= {  dot11OperationEntry 6 }

dot11MaxReceiveLifetime OBJECT-TYPE
        SYNTAX INTEGER (1..4294967295)
        MAX-ACCESS read-write
        STATUS current
        DESCRIPTION

            "The MaxReceiveLifetime shall be the elapsed time in TU,
            after the initial reception of a fragmented MMPDU or MSDU,
            after which further attempts to reassemble the MMPDU or
            MSDU shall be terminated. The default value shall be
            512."
    ::= {  dot11OperationEntry 7 }

dot11ManufacturerID OBJECT-TYPE
        SYNTAX DisplayString (SIZE(0..128))
        MAX-ACCESS read-only
        STATUS current
        DESCRIPTION

            "The ManufacturerID shall include, at a minimum, the name
            of the manufacturer.  It may include additional
            information at the manufacturer's discretion.  The default
            value of this attribute shall be null."

    ::= {  dot11OperationEntry 8 }

dot11ProductID OBJECT-TYPE
        SYNTAX DisplayString (SIZE(0..128))
        MAX-ACCESS read-only
        STATUS current
        DESCRIPTION

            "The ProductID shall include, at a minimum, an identifier
            that is unique to the manufacturer.  It may include
            additional information at the manufacturer's discretion.
            The default value of this attribute shall be null."

    ::= {  dot11OperationEntry 9 }

-- **********************************************************************
-- *    End of dot11OperationEntry  TABLE
-- **********************************************************************

-- **********************************************************************
-- *    dot11Counters TABLE
-- **********************************************************************
dot11CountersTable OBJECT-TYPE
        SYNTAX SEQUENCE OF Dot11CountersEntry
        MAX-ACCESS not-accessible
        STATUS current
        DESCRIPTION

            "Group containing attributes that are MAC counters.
            Implemented as a table to allow for multiple
            instantiations on an agent."

    ::= {  dot11mac 2 }

dot11CountersEntry OBJECT-TYPE
        SYNTAX Dot11CountersEntry
        MAX-ACCESS not-accessible
        STATUS current
        DESCRIPTION
            "An entry in the dot11CountersEntry Table.

            ifIndex - Each 802.11 interface is represented by an
            ifEntry.  Interface tables in this MIB module are indexed
            by ifIndex."
        INDEX {ifIndex}
    ::= {  dot11CountersTable 1 }

Dot11CountersEntry ::= SEQUENCE {
            dot11TransmittedFragmentCount       Counter32,
            dot11MulticastTransmittedFrameCount Counter32,
            dot11FailedCount                    Counter32,
            dot11RetryCount                     Counter32,
            dot11MultipleRetryCount             Counter32,
            dot11FrameDuplicateCount            Counter32,
            dot11RTSSuccessCount                Counter32,
            dot11RTSFailureCount                Counter32,
            dot11ACKFailureCount                Counter32,
            dot11ReceivedFragmentCount          Counter32,
            dot11MulticastReceivedFrameCount    Counter32,
            dot11FCSErrorCount                  Counter32,
	    dot11TransmittedFrameCount          Counter32,
	    dot11WEPUndecryptableCount          Counter32 }

dot11TransmittedFragmentCount OBJECT-TYPE
        SYNTAX Counter32
        MAX-ACCESS read-only
        STATUS current
        DESCRIPTION

            "This counter shall be incremented for an acknowledged MPDU
            with an individual address in the address 1 field or an MPDU
            with a multicast address in the address 1 field of type Data
            or Management."

    ::= {  dot11CountersEntry 1 }

dot11MulticastTransmittedFrameCount OBJECT-TYPE
        SYNTAX Counter32
        MAX-ACCESS read-only
        STATUS current
        DESCRIPTION

            " This counter shall increment only when the multicast bit
            is set in the destination MAC address of a successfully
            transmitted MSDU.  When operating as a STA in an ESS, where
            these frames are directed to the AP, this implies having
            received an acknowledgment to all associated MPDUs. "

    ::= {  dot11CountersEntry 2 }

dot11FailedCount OBJECT-TYPE
        SYNTAX Counter32
        MAX-ACCESS read-only
        STATUS current
        DESCRIPTION

        "This counter shall increment when an MSDU is not transmitted
        successfully due to the number of transmit attempts exceeding
        either the  dot11ShortRetryLimit or dot11LongRetryLimit. "

    ::= {  dot11CountersEntry 3 }

dot11RetryCount OBJECT-TYPE
        SYNTAX Counter32
        MAX-ACCESS read-only
        STATUS current
        DESCRIPTION

            "This counter shall increment when an MSDU is successfully
            transmitted after one or more retransmissions."
    ::= {  dot11CountersEntry 4 }

dot11MultipleRetryCount OBJECT-TYPE
        SYNTAX Counter32
        MAX-ACCESS read-only
        STATUS current
        DESCRIPTION

            "This counter shall increment when an MSDU is successfully
            transmitted after more than one retransmission."

    ::= {  dot11CountersEntry 5 }

dot11FrameDuplicateCount  OBJECT-TYPE
        SYNTAX Counter32
        MAX-ACCESS read-only
        STATUS current
        DESCRIPTION

            "This counter shall increment when a frame is received
            that the Sequence Control field indicates is a
            duplicate."

    ::= {  dot11CountersEntry 6 }

dot11RTSSuccessCount OBJECT-TYPE
        SYNTAX Counter32
        MAX-ACCESS read-only
        STATUS current
        DESCRIPTION

            "This counter shall increment when a CTS is received in
            response to an RTS."
        ::= {  dot11CountersEntry 7 }

dot11RTSFailureCount OBJECT-TYPE
        SYNTAX Counter32
        MAX-ACCESS read-only
        STATUS current
        DESCRIPTION


        "This counter shall increment when a CTS is not received in
        response to an RTS."

    ::= { dot11CountersEntry 8 }

dot11ACKFailureCount OBJECT-TYPE
        SYNTAX Counter32
        MAX-ACCESS read-only
        STATUS current
        DESCRIPTION

            "This counter shall increment when an ACK is not received
            when expected."

    ::= {  dot11CountersEntry 9 }

dot11ReceivedFragmentCount OBJECT-TYPE
        SYNTAX Counter32
        MAX-ACCESS read-only
        STATUS current
        DESCRIPTION

            "This counter shall be incremented for each successfully
            received MPDU of type Data or Management."

    ::= {  dot11CountersEntry 10 }

dot11MulticastReceivedFrameCount OBJECT-TYPE
        SYNTAX Counter32
        MAX-ACCESS read-only
        STATUS current
        DESCRIPTION

            "This counter shall increment when a MSDU is received
            with the multicast bit set in the destination
            MAC address."
    ::= {  dot11CountersEntry 11 }

dot11FCSErrorCount OBJECT-TYPE
        SYNTAX Counter32
        MAX-ACCESS read-only
        STATUS current
        DESCRIPTION

            "This counter shall increment when an FCS error is
            detected in a received MPDU."

    ::= {  dot11CountersEntry 12 }

dot11TransmittedFrameCount OBJECT-TYPE
        SYNTAX Counter32
        MAX-ACCESS read-only
        STATUS current
        DESCRIPTION

"This counter shall increment for each successfully transmitted MSDU."

    ::= {  dot11CountersEntry 13 }

dot11WEPUndecryptableCount OBJECT-TYPE
        SYNTAX Counter32
        MAX-ACCESS read-only
        STATUS current
        DESCRIPTION

        "This counter shall increment when a frame is received with
        the WEP subfield of the Frame Control field set to one and the
        WEPOn value for the key mapped to the TA's MAC address
        indicates that the frame should not have been encrypted or
        that frame is discarded due to the receiving STA not
        implementing the privacy option."

    ::= { dot11CountersEntry 14 }

-- **********************************************************************
-- *    End of dot11CountersEntry  TABLE
-- **********************************************************************

-- **********************************************************************
-- *    GroupAddresses  TABLE
-- **********************************************************************
dot11GroupAddressesTable OBJECT-TYPE
        SYNTAX SEQUENCE OF Dot11GroupAddressesEntry
        MAX-ACCESS not-accessible
        STATUS current
        DESCRIPTION

            "A conceptual table containing a set of MAC addresses
            identifying the multicast addresses for which this STA
            will receive frames.  The default value of this attribute
            shall be null."

    ::= {  dot11mac 3 }

dot11GroupAddressesEntry OBJECT-TYPE
        SYNTAX Dot11GroupAddressesEntry
        MAX-ACCESS not-accessible
        STATUS current
        DESCRIPTION
            "An Entry (conceptual row) in the Group Addresses Table.

            ifIndex - Each 802.11 interface is represented by an
            ifEntry.  Interface tables in this MIB module are indexed
            by ifIndex."
        INDEX {ifIndex, dot11GroupAddressesIndex}
    ::= {  dot11GroupAddressesTable  1 }

Dot11GroupAddressesEntry ::= SEQUENCE {
            dot11GroupAddressesIndex    Integer32,
            dot11Address                MacAddress,
            dot11GroupAddressesStatus   RowStatus}

dot11GroupAddressesIndex OBJECT-TYPE
        SYNTAX Integer32
        MAX-ACCESS not-accessible
        STATUS current
        DESCRIPTION
            "The auxiliary variable used to identify instances
            of the columnar objects in the Group Addresses Table."
    ::= {  dot11GroupAddressesEntry 1 }

dot11Address OBJECT-TYPE
        SYNTAX MacAddress
        MAX-ACCESS read-create
        STATUS current
        DESCRIPTION
            "MAC address identifying a multicast addresses
            from which this STA will receive frames."
    ::= {  dot11GroupAddressesEntry 2 }

dot11GroupAddressesStatus OBJECT-TYPE
        SYNTAX RowStatus
        MAX-ACCESS read-create
        STATUS current
        DESCRIPTION

            "The status column used for creating, modifying, and
            deleting instances of the columnar objects in the Group
            Addresses Table."

        DEFVAL {active}
    ::= {  dot11GroupAddressesEntry 3 }
-- **********************************************************************
-- *    End of GroupAddress  TABLE
-- **********************************************************************

-- **********************************************************************
-- *    Resource Type Attribute Templates
-- **********************************************************************
dot11ResourceTypeIDName OBJECT-TYPE
        SYNTAX DisplayString (SIZE(4))
        MAX-ACCESS read-only
        STATUS current
        DESCRIPTION

            "Contains the name of the Resource Type ID managed object.
            The attribute is read-only and always contains the value
            RTID.  This attribute value shall not be used as a naming
            attribute for any other managed object class."

        REFERENCE "IEEE Std 802.1F-1993,  A.7"
        DEFVAL {"RTID"}
    ::= {  dot11resAttribute 1 }

-- **********************************************************************
-- *    dot11ResourceInfo  TABLE
-- **********************************************************************
dot11ResourceInfoTable OBJECT-TYPE
        SYNTAX SEQUENCE OF Dot11ResourceInfoEntry
        MAX-ACCESS not-accessible
        STATUS current
        DESCRIPTION

            "Provides a means of indicating, in data readable from a
            managed object, information that identifies the source of
            the implementation."

        REFERENCE "IEEE Std 802.1F-1993,  A.7"
    ::= {  dot11resAttribute 2 }

dot11ResourceInfoEntry OBJECT-TYPE
        SYNTAX Dot11ResourceInfoEntry
        MAX-ACCESS not-accessible
        STATUS current
        DESCRIPTION
            "An entry in the dot11ResourceInfo Table.

            ifIndex - Each 802.11 interface is represented by an
            ifEntry.  Interface tables in this MIB module are indexed
            by ifIndex."
        INDEX {ifIndex}
    ::= {  dot11ResourceInfoTable 1 }

Dot11ResourceInfoEntry ::= SEQUENCE {
            dot11manufacturerOUI             OCTET STRING,
            dot11manufacturerName            DisplayString,
            dot11manufacturerProductName     DisplayString,
            dot11manufacturerProductVersion  DisplayString}


dot11manufacturerOUI OBJECT-TYPE
        SYNTAX OCTET STRING (SIZE(3))
        MAX-ACCESS read-only
        STATUS current
        DESCRIPTION
            "Takes the value of an organizationally unique identifier."
    ::= {  dot11ResourceInfoEntry 1 }

dot11manufacturerName OBJECT-TYPE
        SYNTAX DisplayString (SIZE(0..128))
        MAX-ACCESS read-only
        STATUS current
        DESCRIPTION
            "A printable string used to identify the manufacturer of the
            resource.  Maximum string length is 128 octets."
    ::= {  dot11ResourceInfoEntry 2 }

dot11manufacturerProductName OBJECT-TYPE
        SYNTAX DisplayString (SIZE(0..128))
        MAX-ACCESS read-only
        STATUS current
        DESCRIPTION
            "A printable string used to identify the manufacturer's product
            name of the resource.  Maximum string length is 128 octets."
    ::= {  dot11ResourceInfoEntry 3 }

dot11manufacturerProductVersion OBJECT-TYPE
        SYNTAX DisplayString (SIZE(0..128))
        MAX-ACCESS read-only
        STATUS current
        DESCRIPTION
            "Printable string used to identify the manufacturer's product
            version of the resource.  Maximum string length is 128 octets."
    ::= {  dot11ResourceInfoEntry 4 }

-- **********************************************************************
-- *    End of dot11ResourceInfo  TABLE
-- **********************************************************************

-- **********************************************************************
-- *   PHY Attribute Templates
-- **********************************************************************

-- **********************************************************************
-- *    dot11PhyOperation  TABLE
-- **********************************************************************
dot11PhyOperationTable OBJECT-TYPE
        SYNTAX SEQUENCE OF Dot11PhyOperationEntry
        MAX-ACCESS not-accessible
        STATUS current
        DESCRIPTION

        "PHY level attributes concerned with
        operation.  Implemented as a table indexed on
        ifIndex to allow for multiple instantiations on an
        Agent."

    ::= {  dot11phy 1 }

dot11PhyOperationEntry OBJECT-TYPE
        SYNTAX Dot11PhyOperationEntry
        MAX-ACCESS not-accessible
        STATUS current
        DESCRIPTION
            "An entry in the dot11PhyOperation Table.

            ifIndex - Each 802.11 interface is represented by an
            ifEntry.  Interface tables in this MIB module are indexed
            by ifIndex."
        INDEX {ifIndex}
    ::= {  dot11PhyOperationTable 1 }

Dot11PhyOperationEntry ::= SEQUENCE {
            dot11PHYType            INTEGER,
            dot11CurrentRegDomain   Integer32,
            dot11TempType           INTEGER }

dot11PHYType OBJECT-TYPE
        SYNTAX INTEGER {fhss(1), dsss(2), irbaseband(3)}
        MAX-ACCESS read-only
        STATUS current
        DESCRIPTION

        "This is an 8-bit integer value that identifies the PHY type
        supported by the attached PLCP and PMD. Currently defined
        values and their corresponding PHY types are:

        FHSS 2.4 GHz = 01 , DSSS 2.4 GHz = 02, IR Baseband = 03"

    ::= {  dot11PhyOperationEntry 1 }

dot11CurrentRegDomain OBJECT-TYPE
        SYNTAX Integer32
        MAX-ACCESS read-write
        STATUS current
        DESCRIPTION

            "The current regulatory domain this instance of the PMD is
            supporting.  This object corresponds to one of the
            RegDomains listed in dot11RegDomainsSupported."

    ::= {   dot11PhyOperationEntry 2 }

dot11TempType OBJECT-TYPE
        SYNTAX INTEGER {tempType1(1), tempType2(2) }
        MAX-ACCESS read-only
        STATUS current
        DESCRIPTION

        "There are different operating temperature requirements
        dependent on the anticipated environmental conditions. This
        attribute describes the current PHY's operating temperature
        range capability. Currently defined values and their
        corresponding temperature ranges are:

        Type 1 = X'01'-Commercial range of 0 to 40 degrees C,

        Type 2 = X'02'-Industrial range of -30 to 70 degrees C."

    ::= {   dot11PhyOperationEntry 3 }




-- **********************************************************************
-- *    End of dot11PhyOperation  TABLE
-- **********************************************************************

-- **********************************************************************
-- *    dot11PhyAntenna  TABLE
-- **********************************************************************
dot11PhyAntennaTable OBJECT-TYPE
        SYNTAX SEQUENCE OF Dot11PhyAntennaEntry
        MAX-ACCESS not-accessible
        STATUS current
        DESCRIPTION

            "Group of attributes for PhyAntenna.  Implemented as a
            table indexed on ifIndex to allow for multiple instances on
            an agent."

    ::= {  dot11phy 2}

dot11PhyAntennaEntry OBJECT-TYPE
        SYNTAX Dot11PhyAntennaEntry
        MAX-ACCESS not-accessible
        STATUS current
        DESCRIPTION
            "An entry in the dot11PhyAntenna Table.

            ifIndex - Each 802.11 interface is represented by an
            ifEntry.  Interface tables in this MIB module are indexed
            by ifIndex."
        INDEX {ifIndex}
    ::= {  dot11PhyAntennaTable 1 }

Dot11PhyAntennaEntry ::= SEQUENCE {
             dot11CurrentTxAntenna  Integer32,
             dot11DiversitySupport  INTEGER,
	     dot11CurrentRxAntenna  Integer32 }

dot11CurrentTxAntenna OBJECT-TYPE
        SYNTAX Integer32 (1..255)
        MAX-ACCESS read-write
        STATUS current
        DESCRIPTION

            "The current antenna being used to transmit.  This value
        is one of the values appearing in
        dot11SupportedTxAntenna. This may be used by a management agent to control which antenna is used for transmission. "

    ::= {  dot11PhyAntennaEntry 1 }

dot11DiversitySupport OBJECT-TYPE
        SYNTAX INTEGER {fixedlist(1), notsupported(2), dynamic(3)}
        MAX-ACCESS read-only
        STATUS current
        DESCRIPTION

        "This implementation's support for diversity, encoded as:

        X'01'-diversity is available and is performed over the fixed
            list of antennas defined in dot11DiversitySelectionRx.

        X'02'-diversity is not supported.

        X'03'-diversity is supported and control of diversity is also
            available, in which case the attribute 
            dot11DiversitySelectionRx can be dynamically modified by the
            LME."
    ::= {  dot11PhyAntennaEntry 2 }

dot11CurrentRxAntenna OBJECT-TYPE
        SYNTAX Integer32 (1..255)
        MAX-ACCESS read-write
        STATUS current
        DESCRIPTION

"The current antenna being used to receive, if the dot11 DiversitySupport indicates that diversity is not supported.  The selected antenna shall be one of the antennae marked for receive in the dot11AntennasListTable. "

    ::= {  dot11PhyAntennaEntry 3 }

-- **********************************************************************
-- *    End of dot11PhyAntenna  TABLE
-- **********************************************************************

-- **********************************************************************
-- *    dot11PhyTxPower  TABLE
-- **********************************************************************
dot11PhyTxPowerTable OBJECT-TYPE
        SYNTAX SEQUENCE OF Dot11PhyTxPowerEntry
        MAX-ACCESS not-accessible
        STATUS current
        DESCRIPTION

            "Group of attributes for dot11PhyTxPowerTable.  Implemented
            as a table indexed on STA ID to allow for multiple
            instances on an Agent."

    ::= {  dot11phy 3}

dot11PhyTxPowerEntry OBJECT-TYPE
        SYNTAX Dot11PhyTxPowerEntry
        MAX-ACCESS not-accessible
        STATUS current
        DESCRIPTION
            "An entry in the dot11PhyTxPower Table.

            ifIndex - Each 802.11 interface is represented by an
            ifEntry.  Interface tables in this MIB module are indexed
            by ifIndex."
        INDEX {ifIndex}
    ::= {  dot11PhyTxPowerTable 1 }

Dot11PhyTxPowerEntry ::= SEQUENCE {
            dot11NumberSupportedPowerLevels  INTEGER,
            dot11TxPowerLevel1               INTEGER,
            dot11TxPowerLevel2               INTEGER,
            dot11TxPowerLevel3               INTEGER,
            dot11TxPowerLevel4               INTEGER,
            dot11TxPowerLevel5               INTEGER,
            dot11TxPowerLevel6               INTEGER,
            dot11TxPowerLevel7               INTEGER,
            dot11TxPowerLevel8               INTEGER,
            dot11CurrentTxPowerLevel         INTEGER}

dot11NumberSupportedPowerLevels OBJECT-TYPE
        SYNTAX INTEGER (1..8)
        MAX-ACCESS read-only
        STATUS current
        DESCRIPTION
            "The number of power levels supported by the PMD.
            This attribute can have a value of 1 to 8."
    ::= {  dot11PhyTxPowerEntry 1 }

dot11TxPowerLevel1 OBJECT-TYPE
        SYNTAX INTEGER (0..10000)
        MAX-ACCESS read-only
        STATUS current
        DESCRIPTION
            "The transmit output power for LEVEL1 in mW.
            This is also the default power level."
    ::= {   dot11PhyTxPowerEntry 2 }

dot11TxPowerLevel2 OBJECT-TYPE
        SYNTAX INTEGER (0..10000)
        MAX-ACCESS read-only
        STATUS current
        DESCRIPTION
            "The transmit output power for LEVEL2 in mW."
    ::= {   dot11PhyTxPowerEntry 3 }

dot11TxPowerLevel3 OBJECT-TYPE
        SYNTAX INTEGER (0..10000)
        MAX-ACCESS read-only
        STATUS current
        DESCRIPTION
            "The transmit output power for LEVEL3 in mW."
    ::= {   dot11PhyTxPowerEntry 4 }

dot11TxPowerLevel4 OBJECT-TYPE
        SYNTAX INTEGER (0..10000)
        MAX-ACCESS read-only
        STATUS current
        DESCRIPTION
            "The transmit output power for LEVEL4 in mW."
    ::= {   dot11PhyTxPowerEntry 5 }

dot11TxPowerLevel5 OBJECT-TYPE
        SYNTAX INTEGER (0..10000)
        MAX-ACCESS read-only
        STATUS current
        DESCRIPTION
            "The transmit output power for LEVEL5 in mW."
    ::= {   dot11PhyTxPowerEntry 6 }

dot11TxPowerLevel6 OBJECT-TYPE
        SYNTAX INTEGER (0..10000)
        MAX-ACCESS read-only
        STATUS current
        DESCRIPTION
            "The transmit output power for LEVEL6 in mW."
    ::= {   dot11PhyTxPowerEntry 7 }

dot11TxPowerLevel7 OBJECT-TYPE
        SYNTAX INTEGER (0..10000)
        MAX-ACCESS read-only
        STATUS current
        DESCRIPTION
            "The transmit output power for LEVEL7 in mW."
    ::= {   dot11PhyTxPowerEntry 8 }

dot11TxPowerLevel8 OBJECT-TYPE
        SYNTAX INTEGER (0..10000)
        MAX-ACCESS read-only
        STATUS current
        DESCRIPTION
            "The transmit output power for LEVEL8 in mW."
    ::= {   dot11PhyTxPowerEntry 9 }

dot11CurrentTxPowerLevel OBJECT-TYPE
        SYNTAX INTEGER (1..8)
        MAX-ACCESS read-write
        STATUS current
        DESCRIPTION

            "The TxPowerLevel N currently being used to transmit data.
            Some PHYs also use this value to determine the receiver
            sensitivity requirements for CCA."

    ::= {   dot11PhyTxPowerEntry 10 }

-- **********************************************************************
-- *    End of dot11PhyTxPower  TABLE
-- **********************************************************************

-- **********************************************************************
-- *    dot11PhyFHSS  TABLE
-- **********************************************************************
dot11PhyFHSSTable OBJECT-TYPE
        SYNTAX SEQUENCE OF Dot11PhyFHSSEntry
        MAX-ACCESS not-accessible
        STATUS current
        DESCRIPTION

            "Group of attributes for dot11PhyFHSSTable.  Implemented as a
            table indexed on STA ID to allow for multiple instances on
            an Agent."

    ::= {  dot11phy 4 }

dot11PhyFHSSEntry OBJECT-TYPE
        SYNTAX Dot11PhyFHSSEntry
        MAX-ACCESS not-accessible
        STATUS current
        DESCRIPTION
            "An entry in the dot11PhyFHSS Table.

            ifIndex - Each 802.11 interface is represented by an
            ifEntry.  Interface tables in this MIB module are indexed
            by ifIndex."
        INDEX {ifIndex}
    ::= {  dot11PhyFHSSTable 1 }

Dot11PhyFHSSEntry ::= SEQUENCE {
             dot11HopTime   		INTEGER,
             dot11CurrentChannelNumber  INTEGER,
             dot11MaxDwellTime  	INTEGER,
             dot11CurrentDwellTime  	INTEGER,
             dot11CurrentSet    	INTEGER,
             dot11CurrentPattern    	INTEGER,

             dot11CurrentIndex  	INTEGER}

dot11HopTime OBJECT-TYPE
        SYNTAX INTEGER (224)
        MAX-ACCESS read-only
        STATUS current
        DESCRIPTION
            "The time in microseconds for the PMD to change from
            channel 2 to channel 80"
    ::= {   dot11PhyFHSSEntry 1 }

dot11CurrentChannelNumber OBJECT-TYPE
        SYNTAX INTEGER (0..99)
        MAX-ACCESS read-write
        STATUS current
        DESCRIPTION
        "The current channel number of the frequency output by the RF
        synthesizer"
    ::= {   dot11PhyFHSSEntry 2 }

dot11MaxDwellTime OBJECT-TYPE
        SYNTAX INTEGER (1..65535)
        MAX-ACCESS read-only
        STATUS current
        DESCRIPTION
            "The maximum time in TU that the transmitter
            is permitted to operate on a single channel."
    ::= {   dot11PhyFHSSEntry 3 }

dot11CurrentDwellTime OBJECT-TYPE
        SYNTAX INTEGER (1..65535)
        MAX-ACCESS read-write
        STATUS current
        DESCRIPTION
            "The current time in TU that the transmitter shall operate
            on a single channel, as set by the MAC.  Default is 19 TU."
    ::= {   dot11PhyFHSSEntry 4 }

dot11CurrentSet OBJECT-TYPE
        SYNTAX INTEGER (1..255)
        MAX-ACCESS read-write
        STATUS current
        DESCRIPTION
            "The current set of patterns the PHY
            LME is using to determine the hopping sequence. "
    ::= {   dot11PhyFHSSEntry 5 }

dot11CurrentPattern OBJECT-TYPE
        SYNTAX INTEGER (0..255)
        MAX-ACCESS read-write
        STATUS current
        DESCRIPTION
            "The current pattern the PHY LME is
            using to determine the hop sequence."
    ::= {   dot11PhyFHSSEntry 6 }

dot11CurrentIndex OBJECT-TYPE
        SYNTAX INTEGER (1..255)
        MAX-ACCESS read-write
        STATUS current
        DESCRIPTION

            "The current index value the PHY LME is using to determine
            the CurrentChannelNumber."

    ::= {   dot11PhyFHSSEntry 7 }

-- **********************************************************************
-- *    End of dot11PhyFHSS  TABLE
-- **********************************************************************

-- **********************************************************************
-- *    dot11PhyDSSSEntry  TABLE
-- **********************************************************************
dot11PhyDSSSTable OBJECT-TYPE
        SYNTAX SEQUENCE OF Dot11PhyDSSSEntry
        MAX-ACCESS not-accessible
        STATUS current
        DESCRIPTION

            "Entry of attributes for dot11PhyDSSSEntry.  Implemented as a
            table indexed on ifIndex allow for multiple instances on
            an Agent."

    ::= {  dot11phy 5 }

dot11PhyDSSSEntry OBJECT-TYPE
        SYNTAX Dot11PhyDSSSEntry
        MAX-ACCESS not-accessible
        STATUS current
        DESCRIPTION
            "An entry in the dot11PhyDSSSEntry Table.

            ifIndex - Each 802.11 interface is represented by an
            ifEntry.  Interface tables in this MIB module are indexed
            by ifIndex."
        INDEX {ifIndex}
    ::= {  dot11PhyDSSSTable 1 }

Dot11PhyDSSSEntry ::= SEQUENCE {
             dot11CurrentChannel    INTEGER,
             dot11CCAModeSupported  INTEGER,
             dot11CurrentCCAMode    INTEGER,
             dot11EDThreshold       Integer32}

dot11CurrentChannel OBJECT-TYPE
        SYNTAX INTEGER (1..14)
        MAX-ACCESS read-write
        STATUS current
        DESCRIPTION
            "The current operating frequency channel of the DSSS
            PHY. Valid channel numbers are as defined in 15.4.6.2"
    ::= {   dot11PhyDSSSEntry 1 }

dot11CCAModeSupported OBJECT-TYPE
        SYNTAX INTEGER (1..7)
        MAX-ACCESS read-only
        STATUS current
        DESCRIPTION
            "dot11CCAModeSupported is a bit-significant value, representing all of the CCA modes supported by the PHY.  Valid values are:

            energy detect only (ED_ONLY) = 01,
		carrier sense only (CS_ONLY) = 02,
		carrier sense and energy detect (ED_and_CS)= 04

or the logical sum of any of these values."
    ::= {   dot11PhyDSSSEntry 2 }

dot11CurrentCCAMode OBJECT-TYPE
        SYNTAX INTEGER {edonly(1), csonly(2), edandcs(4)}
        MAX-ACCESS read-write
        STATUS current
        DESCRIPTION
            "The current CCA method in operation.   Valid values are:
                energy detect only (edonly) = 01,
                carrier sense only (csonly) = 02,
                carrier sense and energy detect (edandcs)= 04."
::= {   dot11PhyDSSSEntry 3 }

dot11EDThreshold OBJECT-TYPE
        SYNTAX Integer32
        MAX-ACCESS read-write
        STATUS current
        DESCRIPTION
            "The current Energy Detect Threshold being used by the DSSS PHY."
    ::= {   dot11PhyDSSSEntry 4 }

-- **********************************************************************
-- *    End of dot11PhyDSSSEntry  TABLE
-- **********************************************************************

-- **********************************************************************
-- *    dot11PhyIR  TABLE
-- **********************************************************************
dot11PhyIRTable OBJECT-TYPE
        SYNTAX SEQUENCE OF Dot11PhyIREntry
        MAX-ACCESS not-accessible
        STATUS current
        DESCRIPTION

            "Group of attributes for dot11PhyIRTable.  Implemented as a
            table indexed on ifIndex to allow for multiple instances on
            an Agent."

    ::= {  dot11phy 6 }

dot11PhyIREntry OBJECT-TYPE
        SYNTAX Dot11PhyIREntry
        MAX-ACCESS not-accessible
        STATUS current
        DESCRIPTION
            "An entry in the dot11PhyIR Table.

            ifIndex - Each 802.11 interface is represented by an
            ifEntry.  Interface tables in this MIB module are indexed
            by ifIndex."
        INDEX {ifIndex}
    ::= {  dot11PhyIRTable 1 }

Dot11PhyIREntry ::= SEQUENCE {
             dot11CCAWatchdogTimerMax       Integer32,
             dot11CCAWatchdogCountMax       Integer32,
             dot11CCAWatchdogTimerMin       Integer32,
             dot11CCAWatchdogCountMin       Integer32}

dot11CCAWatchdogTimerMax OBJECT-TYPE
        SYNTAX Integer32
        MAX-ACCESS read-write
        STATUS current
        DESCRIPTION

            "This parameter, together with CCAWatchdogCountMax,
            determines when energy detected in the channel can be
            ignored."

    ::= {   dot11PhyIREntry 1 }

dot11CCAWatchdogCountMax OBJECT-TYPE
        SYNTAX Integer32
        MAX-ACCESS read-write
        STATUS current
        DESCRIPTION

            "This parameter, together with CCAWatchdogTimerMax,
            determines when energy detected in the channel can be
            ignored."

    ::= {   dot11PhyIREntry 2 }

dot11CCAWatchdogTimerMin OBJECT-TYPE
        SYNTAX Integer32
        MAX-ACCESS read-write
        STATUS current
        DESCRIPTION

            "The minimum value to which CCAWatchdogTimerMax can be
            set."

    ::= {   dot11PhyIREntry 3 }

dot11CCAWatchdogCountMin OBJECT-TYPE
        SYNTAX Integer32
        MAX-ACCESS read-write
        STATUS current
        DESCRIPTION
            "The minimum value to which CCAWatchdogCount can be set."
    ::= {   dot11PhyIREntry 4 }

-- **********************************************************************
-- *    End of dot11PhyIR  TABLE
-- **********************************************************************

-- **********************************************************************
-- *    dot11RegDomainsSupported  TABLE
-- **********************************************************************
dot11RegDomainsSupportedTable OBJECT-TYPE
        SYNTAX SEQUENCE OF Dot11RegDomainsSupportEntry
        MAX-ACCESS not-accessible
        STATUS current
        DESCRIPTION

            "There are different operational requirements dependent on
            the regulatory domain.  This attribute list describes the
            regulatory domains the PLCP and PMD support in this
            implementation.  Currently defined values and their
            corresponding Regulatory Domains are:

            FCC (USA) = X'10', DOC (Canada) = X'20', ETSI (most of
            Europe) = X'30', Spain = X'31', France = X'32', MKK
            (Japan) = X'40' "

    ::= {   dot11phy 7}

dot11RegDomainsSupportEntry OBJECT-TYPE
        SYNTAX Dot11RegDomainsSupportEntry
        MAX-ACCESS not-accessible
        STATUS current
        DESCRIPTION
            "An entry in the dot11RegDomainsSupport Table.

            ifIndex - Each 802.11 interface is represented by an
            ifEntry.  Interface tables in this MIB module are indexed
            by ifIndex."
        INDEX {ifIndex, dot11RegDomainsSupportIndex}
    ::= {  dot11RegDomainsSupportedTable 1 }

Dot11RegDomainsSupportEntry ::= SEQUENCE {
             dot11RegDomainsSupportIndex    Integer32,
             dot11RegDomainsSupportValue    INTEGER}

dot11RegDomainsSupportIndex OBJECT-TYPE
        SYNTAX Integer32
        MAX-ACCESS not-accessible
        STATUS current
        DESCRIPTION
            "The auxiliary variable used to identify instances
            of the columnar objects in the RegDomainsSupport Table."
    ::= {  dot11RegDomainsSupportEntry 1 }

dot11RegDomainsSupportValue OBJECT-TYPE

        SYNTAX INTEGER {fcc(16), doc(32), etsi(48), spain (49), france
        (50), mkk (64) }
        MAX-ACCESS read-only
        STATUS current
        DESCRIPTION
            "There are different operational requirements dependent on
            the regulatory domain.  This attribute list describes the
            regulatory domains the PLCP and PMD support in this
            implementation.  Currently de- fined values and their
            corresponding Regulatory Domains are:

            FCC (USA) = X'10', DOC (Canada) = X'20', ETSI (most of
            Europe) = X'30', Spain = X'31', France = X'32', MKK
            (Japan) = X'40' "
    ::= {  dot11RegDomainsSupportEntry 2 }

-- **********************************************************************
-- *    End of dot11RegDomainsSupported  TABLE
-- **********************************************************************

-- **********************************************************************
-- *    dot11AntennasList  TABLE
-- **********************************************************************
dot11AntennasListTable OBJECT-TYPE
        SYNTAX SEQUENCE OF Dot11AntennasListEntry
        MAX-ACCESS not-accessible
        STATUS current
        DESCRIPTION
"This table represents the list of antennae.  An antenna can be marked to be capable of transmitting, receiving, and/or for participation in receive diversity.  Each entry in this table represents a single antenna with its properties.  The maximum number of antennae that can be contained in this table is 255."
    ::= {   dot11phy 8 }

dot11AntennasListEntry OBJECT-TYPE
        SYNTAX Dot11AntennasListEntry
        MAX-ACCESS not-accessible
        STATUS current
        DESCRIPTION
            "An entry in the dot11AntennasListTable, representing the properties of a single antenna.

            ifIndex - Each 802.11 interface is represented by an
            ifEntry.  Interface tables in this MIB module are indexed
            by ifIndex."
        INDEX {ifIndex, dot11AntennaListIndex}
    ::= {  dot11AntennasListTable 1 }

Dot11AntennasListEntry ::= SEQUENCE {
             dot11AntennaListIndex     Integer32,
             dot11SupportedTxAntenna   TruthValue,
             dot11SupportedRxAntenna   TruthValue,
             dot11DiversitySelectionRx TruthValue }

dot11AntennaListIndex OBJECT-TYPE
        SYNTAX Integer32 (1..255)
        MAX-ACCESS not-accessible
        STATUS current
        DESCRIPTION
            "The unique index of an antenna which is used to identify the columnar objects in the dot11AntennasList Table."
    ::= {  dot11AntennasListEntry 1 }

dot11SupportedTxAntenna OBJECT-TYPE
        SYNTAX TruthValue
        MAX-ACCESS read-write
        STATUS current
        DESCRIPTION

            "When true, this object indicates that the antenna represented by dot11AntennaIndex can be used as a transmit antenna."

    ::= {  dot11AntennasListEntry 2 }

dot11SupportedRxAntenna OBJECT-TYPE
        SYNTAX TruthValue
        MAX-ACCESS read-write
        STATUS current
        DESCRIPTION

            "When true, this object indocates that the antenna represented by the dot11AntennaIndex xan be used as a receive antenna."

    ::= {  dot11AntennasListEntry 3 }

dot11DiversitySelectionRx OBJECT-TYPE
        SYNTAX TruthValue
        MAX-ACCESS read-write
        STATUS current
        DESCRIPTION

            "When true, this object indicates that the antenna represented by dot11AntennaIndex can be used for receive diversity.  This object may only be true if the antenna can be used as a receive antenna, as indicated by dot11SupportedRxAntenna."

    ::= {  dot11AntennasListEntry 4 }

-- **********************************************************************
-- *    End of dot11AntennasList  TABLE
-- **********************************************************************


-- **********************************************************************
-- *    SupportedDataRatesTx  TABLE
-- **********************************************************************
dot11SupportedDataRatesTxTable OBJECT-TYPE
        SYNTAX SEQUENCE OF Dot11SupportedDataRatesTxEntry
        MAX-ACCESS not-accessible
        STATUS current
        DESCRIPTION

            "The Transmit bit rates supported by the PLCP and PMD,
            represented by a count from X?02-X?7f, corresponding to data
            rates in increments of 500Kb/s from 1 Mb/s to 63.5 Mb/s subject
            to limitations of each individual PHY."

    ::= {  dot11phy 9 }

dot11SupportedDataRatesTxEntry OBJECT-TYPE
        SYNTAX Dot11SupportedDataRatesTxEntry
        MAX-ACCESS not-accessible
        STATUS current
        DESCRIPTION

            "An Entry (conceptual row) in the dot11SupportedDataRatesTx
            Table.

            ifIndex - Each 802.11 interface is represented by an
            ifEntry.  Interface tables in this MIB module are indexed
            by ifIndex."

        INDEX {ifIndex, dot11SupportedDataRatesTxIndex}

    ::= {  dot11SupportedDataRatesTxTable  1 }

Dot11SupportedDataRatesTxEntry ::= SEQUENCE {
            dot11SupportedDataRatesTxIndex  Integer32,
            dot11SupportedDataRatesTxValue  Integer32}

dot11SupportedDataRatesTxIndex OBJECT-TYPE
        SYNTAX Integer32 (1..8)
        MAX-ACCESS not-accessible
        STATUS current
        DESCRIPTION

            "Index object which identifies which data rate to access.
            Range is 1..8."

    ::= {  dot11SupportedDataRatesTxEntry 1 }

dot11SupportedDataRatesTxValue OBJECT-TYPE
        SYNTAX Integer32 (2..127)
        MAX-ACCESS read-only
        STATUS current
        DESCRIPTION

            "The Transmit bit rates supported by the PLCP and PMD,
            represented by a count from X?02-X?7f, corresponding to data
            rates in increments of 500Kb/s from 1 Mb/s to 63.5 Mb/s subject
            to limitations of each individual PHY."

    ::= {  dot11SupportedDataRatesTxEntry 2 }

-- **********************************************************************
-- *    End of dot11SupportedDataRatesTx  TABLE
-- **********************************************************************


-- **********************************************************************
-- *    SupportedDataRatesRx  TABLE
-- **********************************************************************
dot11SupportedDataRatesRxTable OBJECT-TYPE
        SYNTAX SEQUENCE OF Dot11SupportedDataRatesRxEntry
        MAX-ACCESS not-accessible
        STATUS current
        DESCRIPTION
            "The receive bit rates supported by the PLCP and PMD,
            represented by a count from X?002-X?7f, corresponding to data
            rates in increments of 500Kb/s from 1 Mb/s to 63.5 Mb/s."

    ::= {  dot11phy 10 }

dot11SupportedDataRatesRxEntry OBJECT-TYPE
        SYNTAX Dot11SupportedDataRatesRxEntry
        MAX-ACCESS not-accessible
        STATUS current
        DESCRIPTION

            "An Entry (conceptual row) in the
        dot11SupportedDataRatesRx Table.

            ifIndex - Each 802.11 interface is represented by an
            ifEntry.  Interface tables in this MIB module are indexed
            by ifIndex."

        INDEX {ifIndex, dot11SupportedDataRatesRxIndex}

    ::= {  dot11SupportedDataRatesRxTable  1 }

Dot11SupportedDataRatesRxEntry ::= SEQUENCE {
            dot11SupportedDataRatesRxIndex  Integer32,
            dot11SupportedDataRatesRxValue  Integer32}

dot11SupportedDataRatesRxIndex OBJECT-TYPE
        SYNTAX Integer32 (1..8)
        MAX-ACCESS not-accessible
        STATUS current
        DESCRIPTION
            "Index object which identifies which data rate to access.
            Range is 1..8."
    ::= {  dot11SupportedDataRatesRxEntry 1 }

dot11SupportedDataRatesRxValue OBJECT-TYPE
        SYNTAX Integer32 (2..127)
        MAX-ACCESS read-only
        STATUS current
        DESCRIPTION
            "The receive bit rates supported by the PLCP and PMD,
            represented by a count from X?02-X?7f, corresponding to data
            rates in increments of 500Kb/s from 1 Mb/s to 63.5 Mb/s."
    ::= {  dot11SupportedDataRatesRxEntry 2 }

-- **********************************************************************
-- *    End of dot11SupportedDataRatesRx  TABLE
-- **********************************************************************

-- **********************************************************************
-- *   conformance information
-- **********************************************************************

dot11Conformance  OBJECT IDENTIFIER ::= { ieee802dot11 5 }
dot11Groups  OBJECT IDENTIFIER ::= { dot11Conformance 1 }
dot11Compliances  OBJECT IDENTIFIER ::= { dot11Conformance 2 }

-- **********************************************************************
-- *   compliance statements
-- **********************************************************************
dot11Compliance MODULE-COMPLIANCE
        STATUS  current
        DESCRIPTION
            "The compliance statement for SNMPv2 entities
            that implement the IEEE 802.11 MIB."

  MODULE  -- this module
    MANDATORY-GROUPS {
        dot11SMTbase2,
        dot11MACbase, dot11CountersGroup,
        dot11SmtAuthenticationAlgorithms, 
        dot11ResourceTypeID, dot11PhyOperationComplianceGroup }

   GROUP dot11PhyDSSSComplianceGroup
           DESCRIPTION
               "Implementation of this group is required when object
               dot11PHYType has the value of dsss.  This group is
               mutually exclusive with the groups
               dot11PhyIRComplianceGroup and
               dot11PhyFHSSComplianceGroup."

    GROUP dot11PhyIRComplianceGroup
           DESCRIPTION
               "Implementation of this group is required when object
               dot11PHYType has the value of irbaseband.  This group is
               mutually exclusive with the groups
               dot11PhyDSSSComplianceGroup and
               dot11PhyFHSSComplianceGroup."


    GROUP dot11PhyFHSSComplianceGroup
           DESCRIPTION
               "Implementation of this group is required when object
               dot11PHYType has the value of fhss.  This group is
               mutually exclusive with the groups
               dot11PhyDSSSComplianceGroup and
               dot11PhyIRComplianceGroup."


    -- OPTIONAL-GROUPS { dot11SMTprivacy, dot11MACStatistics,
    --    dot11PhyAntennaComplianceGroup, dot11PhyTxPowerComplianceGroup, 
    --    dot11PhyRegDomainsSupportGroup,
    --    dot11PhyAntennasListGroup, dot11PhyRateGroup }
    -- 

    ::= { dot11Compliances 1 }

-- **********************************************************************
-- *   Groups - units of conformance
-- **********************************************************************
dot11SMTbase OBJECT-GROUP
        OBJECTS { dot11StationID, dot11MediumOccupancyLimit, 
             dot11CFPollable,
             dot11CFPPeriod,
             dot11CFPMaxDuration,
             dot11AuthenticationResponseTimeOut,
	     dot11PrivacyOptionImplemented,
	     dot11PowerManagementMode,
	     dot11DesiredSSID, dot11DesiredBSSType,
	     dot11OperationalRateSet,
	     dot11BeaconPeriod, dot11DTIMPeriod,
	     dot11AssociationResponseTimeOut 
             }
        STATUS deprecated
        DESCRIPTION
         "The SMT object class provides the necessary support at the
         STA to manage the processes in the STA such that the STA may
         work cooperatively as a part of an IEEE 802.11 network."
    ::= {dot11Groups 1   }

dot11SMTprivacy OBJECT-GROUP
        OBJECTS { dot11PrivacyInvoked, 
		dot11WEPKeyMappingLength, dot11ExcludeUnencrypted,
		dot11WEPICVErrorCount , dot11WEPExcludedCount ,
		dot11WEPDefaultKeyID,
                dot11WEPDefaultKeyValue,
	        dot11WEPKeyMappingWEPOn,
                dot11WEPKeyMappingValue , dot11WEPKeyMappingAddress,
    		dot11WEPKeyMappingStatus }

        STATUS current
        DESCRIPTION
            "The SMTPrivacy package is a set of attributes that shall be
            present if WEP is implemented in the STA."
    ::= {dot11Groups 2 }

dot11MACbase OBJECT-GROUP

            OBJECTS { dot11MACAddress, dot11Address,
		    dot11GroupAddressesStatus,
                    dot11RTSThreshold, dot11ShortRetryLimit,
                    dot11LongRetryLimit, dot11FragmentationThreshold,
                    dot11MaxTransmitMSDULifetime,
                    dot11MaxReceiveLifetime, dot11ManufacturerID,
                    dot11ProductID
                    }
        STATUS current
        DESCRIPTION
         "The MAC object class provides the necessary support for the
         access control, generation, and verification of frame check
         sequences, and proper delivery of valid data to upper
         layers."
    ::= {dot11Groups 3 }


dot11MACStatistics OBJECT-GROUP

        OBJECTS { dot11RetryCount, dot11MultipleRetryCount,
            dot11RTSSuccessCount, dot11RTSFailureCount,
            dot11ACKFailureCount, dot11FrameDuplicateCount }

        STATUS current
        DESCRIPTION
            "The MACStatistics package provides extended statistical
            information on the operation of the MAC.  This 
            package is completely optional."
    ::= {dot11Groups 4 }

dot11ResourceTypeID OBJECT-GROUP
        OBJECTS { dot11ResourceTypeIDName, dot11manufacturerOUI,
            dot11manufacturerName, dot11manufacturerProductName,
            dot11manufacturerProductVersion }
        STATUS current
        DESCRIPTION

                "Attributes used to identify a STA, its manufacturer,
                and various product names and versions."

    ::= {dot11Groups 5  }

dot11SmtAuthenticationAlgorithms OBJECT-GROUP
        OBJECTS { dot11AuthenticationAlgorithm,
                  dot11AuthenticationAlgorithmsEnable }
        STATUS current
        DESCRIPTION
                "Authentication Algorithm Table."
    ::= {dot11Groups 6 }


dot11PhyOperationComplianceGroup OBJECT-GROUP
        OBJECTS { dot11PHYType, dot11CurrentRegDomain, dot11TempType }
        STATUS current
        DESCRIPTION
            "PHY layer operations attributes."
    ::= { dot11Groups 7 }


dot11PhyAntennaComplianceGroup OBJECT-GROUP
        OBJECTS {dot11CurrentTxAntenna, dot11DiversitySupport,
dot11CurrentRxAntenna }
        STATUS current
        DESCRIPTION
            "Attributes for Data Rates for IEEE 802.11."
    ::= { dot11Groups 8 }

dot11PhyTxPowerComplianceGroup OBJECT-GROUP
        OBJECTS {dot11NumberSupportedPowerLevels, dot11TxPowerLevel1,
            dot11TxPowerLevel2, dot11TxPowerLevel3, dot11TxPowerLevel4,
            dot11TxPowerLevel5, dot11TxPowerLevel6, dot11TxPowerLevel7,
            dot11TxPowerLevel8, dot11CurrentTxPowerLevel }
        STATUS current
        DESCRIPTION
            "Attributes for Control and Management of transmit power."
    ::= { dot11Groups 9 }

dot11PhyFHSSComplianceGroup OBJECT-GROUP
        OBJECTS {dot11HopTime, dot11CurrentChannelNumber, dot11MaxDwellTime,
            dot11CurrentDwellTime, dot11CurrentSet, dot11CurrentPattern,
            dot11CurrentIndex}

        STATUS current
        DESCRIPTION

            "Attributes that configure the Frequency Hopping for IEEE
            802.11."

    ::= { dot11Groups 10 }

dot11PhyDSSSComplianceGroup OBJECT-GROUP

        OBJECTS {dot11CurrentChannel, dot11CCAModeSupported,
            dot11CurrentCCAMode, dot11EDThreshold}

        STATUS current
        DESCRIPTION
            "Attributes that configure the DSSS for IEEE 802.11."
    ::= { dot11Groups 11 }

dot11PhyIRComplianceGroup OBJECT-GROUP
        OBJECTS {dot11CCAWatchdogTimerMax, dot11CCAWatchdogCountMax,
        dot11CCAWatchdogTimerMin, dot11CCAWatchdogCountMin}
        STATUS current
        DESCRIPTION
            "Attributes that configure the baseband IR for IEEE 802.11."
    ::= { dot11Groups 12 }

dot11PhyRegDomainsSupportGroup OBJECT-GROUP
        OBJECTS { dot11RegDomainsSupportValue}
        STATUS current
        DESCRIPTION
            "Attributes that specify the supported Regulation Domains."
    ::= { dot11Groups 13}

dot11PhyAntennasListGroup OBJECT-GROUP
        OBJECTS { dot11SupportedTxAntenna,
             dot11SupportedRxAntenna, dot11DiversitySelectionRx }
        STATUS current
        DESCRIPTION
            "Attributes that specify the supported Regulation Domains."
    ::= { dot11Groups 14 }

dot11PhyRateGroup OBJECT-GROUP
        OBJECTS {dot11SupportedDataRatesTxValue,
            dot11SupportedDataRatesRxValue }
        STATUS current
        DESCRIPTION
            "Attributes for Data Rates for IEEE 802.11."
    ::= { dot11Groups 15 }


dot11CountersGroup OBJECT-GROUP
        OBJECTS {  
                    dot11TransmittedFragmentCount   ,
                    dot11MulticastTransmittedFrameCount ,
                    dot11FailedCount, dot11ReceivedFragmentCount,
                    dot11MulticastReceivedFrameCount    ,
                    dot11FCSErrorCount,
		    dot11WEPUndecryptableCount,
		    dot11TransmittedFrameCount }

        STATUS current
        DESCRIPTION
            "Attributes from the dot11CountersGroup that are not described
            in the dot11MACStatistics group.  These objects are
            mandatory."
    ::= {dot11Groups 16 }

dot11NotificationGroup NOTIFICATION-GROUP
	NOTIFICATIONS { dot11Disassociate, 
			    dot11Deauthenticate,
			    dot11AuthenticateFail }
	STATUS current
	DESCRIPTION
		"IEEE 802.11 notifications"
	::= { dot11Groups 17 }

dot11SMTbase2 OBJECT-GROUP
        OBJECTS { dot11MediumOccupancyLimit, 
             dot11CFPollable,
             dot11CFPPeriod,
             dot11CFPMaxDuration,
             dot11AuthenticationResponseTimeOut,
	     dot11PrivacyOptionImplemented,
	     dot11PowerManagementMode,
	     dot11DesiredSSID, dot11DesiredBSSType,
	     dot11OperationalRateSet,
	     dot11BeaconPeriod, dot11DTIMPeriod,
	     dot11AssociationResponseTimeOut,
	     dot11DisassociateReason,
             dot11DisassociateStation,
             dot11DeauthenticateReason,
             dot11DeauthenticateStation,
             dot11AuthenticateFailStatus,
             dot11AuthenticateFailStation 
             }
        STATUS current
        DESCRIPTION
         "The SMTbase2 object class provides the necessary support at the
         STA to manage the processes in the STA such that the STA may
         work cooperatively as a part of an IEEE 802.11 network."
    ::= {dot11Groups 18 }

-- **********************************************************************
-- *   End of 80211 MIB
-- **********************************************************************
END




File: /dude_custom_files\MIMOSA-MIB-B5.txt
MIMOSA-NETWORKS-BFIVE-MIB DEFINITIONS ::= BEGIN

--  Copyright (C) 2017, Mimosa Networks, Inc. All Rights Reserved.
--
--  Mimosa Networks MIB
--  Revision: 1.02
--  Date: April 28, 2017
--
--  Mimosa Networks, Inc.
--  469 El Camino Real Ste 100
--  Santa Clara, CA 95050
--  support@mimosa.co
--
--  This MIB defines the MIB specification for Mimosa Network's Products
--
--  Mimosa reserves the right to make changes to this MIB specification as
--  well as other information related to this specification without prior
--  notice.  The user of this specification should consult Mimosa Networks,
--  to determine if any such changes have been made.
--
--  Current MIBs are available from Mimosa Networks at the following URLs:
--
--		http://help.mimosa.co
--
--  In no event shall Mimosa Networks, Inc. be liable for any indirect,
--  consequential, special or incidental damages whatsoever (including
--  but not limited to lost profits or lost revenue) arising out of or
--  related to this specification or the information contained in it.
--  This non-liability extends to even if Mimosa Networks Inc. has been
--  advised of, known, or should have known, the potential for such damages.

--  Mimosa Networks, Inc. hereby grants end-users, and other parties a
--  a non-exclusive license to use this MIB specification in order to
--  manage products of Mimosa Networks, Inc.


IMPORTS
    MODULE-IDENTITY, OBJECT-TYPE,
    NOTIFICATION-TYPE, Integer32,
    Counter32, Counter64, Unsigned32,
    TimeTicks, IpAddress                  FROM SNMPv2-SMI

    DisplayString , MacAddress,
    RowStatus, TruthValue,
    PhysAddress, TEXTUAL-CONVENTION       FROM SNMPv2-TC

    MODULE-COMPLIANCE, OBJECT-GROUP,
    NOTIFICATION-GROUP 	                  FROM SNMPv2-CONF

    ifIndex                               FROM IF-MIB
    mimosaWireless,
    mimosaConformanceGroup                FROM MIMOSA-NETWORKS-BASE-MIB;

mimosaB5Module MODULE-IDENTITY
    LAST-UPDATED "201506030000Z"
    ORGANIZATION "Mimosa Networks
    			  www.mimosa.co"
    CONTACT-INFO
    	"postal:
    	Mimosa Networks, Inc.
		469 El Camino Real Ste 100
		Santa Clara, CA 95050
        email: support@mimosa.co"
    DESCRIPTION
		"Mimosa device MIB definitions"
	REVISION	"201704280000Z"
    DESCRIPTION
		"Compatible with Firmware 1.4.5"
    ::= { mimosaConformanceGroup 1 }

mimosaGeneral       OBJECT IDENTIFIER ::= { mimosaWireless 1 }
mimosaLocInfo       OBJECT IDENTIFIER ::= { mimosaWireless 2 }
mimosaWanInfo       OBJECT IDENTIFIER ::= { mimosaWireless 3 }
mimosaTdmaInfo      OBJECT IDENTIFIER ::= { mimosaWireless 4 }
mimosaMgmtInfo      OBJECT IDENTIFIER ::= { mimosaWireless 5 }
mimosaRfInfo        OBJECT IDENTIFIER ::= { mimosaWireless 6 }
mimosaPerfInfo      OBJECT IDENTIFIER ::= { mimosaWireless 7 }
mimosaServices      OBJECT IDENTIFIER ::= { mimosaWireless 8 }


-- *****************************************************************
-- ***                   Mimosa Textual Conventions              ***
-- *****************************************************************
DecimalOne ::= TEXTUAL-CONVENTION
    DISPLAY-HINT "d-1"
    STATUS       current
    DESCRIPTION  "Fixed point, one decimal"
    SYNTAX       Integer32

DecimalTwo ::= TEXTUAL-CONVENTION
    DISPLAY-HINT "d-2"
    STATUS       current
    DESCRIPTION  "Fixed point, two decimals"
    SYNTAX       Integer32

DecimalFive ::= TEXTUAL-CONVENTION
    DISPLAY-HINT "d-5"
    STATUS       current
    DESCRIPTION  "Fixed point, five decimals"
    SYNTAX       Integer32

-- *****************************************************************
-- ***       Mimosa General variables are specified below.    ***
-- *****************************************************************

mimosaDeviceName OBJECT-TYPE
    SYNTAX      DisplayString (SIZE (0..64))
    MAX-ACCESS  read-only
    STATUS      current
    DESCRIPTION
        "The name of the local Mimosa device. This unique identifier could
         be the same as the sysName object."
    ::= { mimosaGeneral 1 }

mimosaSerialNumber OBJECT-TYPE
    SYNTAX      DisplayString (SIZE (0..64))
    MAX-ACCESS  read-only
    STATUS      current
    DESCRIPTION
        "The unique serial number of the Mimosa device."
    ::= { mimosaGeneral 2 }

mimosaFirmwareVersion OBJECT-TYPE
    SYNTAX      DisplayString (SIZE (0..64))
    MAX-ACCESS  read-only
    STATUS      current
    DESCRIPTION
        "The version of the currently installed and/or running firmware
         on the Mimosa device."
    ::= { mimosaGeneral 3 }

mimosaFirmwareBuildDate OBJECT-TYPE
    SYNTAX      DisplayString (SIZE (0..64))
    MAX-ACCESS  read-only
    STATUS      current
    DESCRIPTION
        "The creation date of the currently installed and/or running
         firmware on the Mimosa device."
    ::= { mimosaGeneral 4 }

mimosaLastRebootTime OBJECT-TYPE
    SYNTAX      DisplayString (SIZE (0..64))
    MAX-ACCESS  read-only
    STATUS      current
    DESCRIPTION
        "The last time the Mimosa device rebooted."
    ::= { mimosaGeneral 5 }

mimosaUnlockCode OBJECT-TYPE
    SYNTAX      DisplayString (SIZE (0..64))
    MAX-ACCESS  read-only
    STATUS      current
    DESCRIPTION
        "The code used to unlock the Mimosa device."
    ::= { mimosaGeneral 6 }

mimosaLEDBrightness OBJECT-TYPE
    SYNTAX  INTEGER {
                auto(1),
                low(2),
                medium(3),
                high(4)
            }
    MAX-ACCESS  read-only
    STATUS      current
    DESCRIPTION
        "Indicates the intensity of the status indicator lights on the
         device exterior. The Auto option adjusts the amount of light
         based upon ambient conditions. Manual options include Low,
         Medium, and High."
    ::= { mimosaGeneral 7 }

mimosaInternalTemp OBJECT-TYPE
    SYNTAX       DecimalOne
    UNITS        "C" 
    MAX-ACCESS   read-only
    STATUS       current
    DESCRIPTION
        "The internal temperature of the Mimosa device."
    ::= { mimosaGeneral 8 }

mimosaRegulatoryDomain OBJECT-TYPE
    SYNTAX      DisplayString (SIZE (0..64))
    MAX-ACCESS  read-only
    STATUS      current
    DESCRIPTION
        "The country in which the Mimosa device has been configured to run."
    ::= { mimosaGeneral 9 }


-- **********************************************************************
-- ***     Mimosa Device Location variables are specified below.      ***
-- **********************************************************************

mimosaLongitude OBJECT-TYPE
    SYNTAX       DecimalFive
    MAX-ACCESS   read-only
    STATUS       current
    DESCRIPTION
        "The Longitude of the Mimosa device location, in 5 decimal points."
    ::= { mimosaLocInfo 1 }

mimosaLatitude OBJECT-TYPE
    SYNTAX       DecimalFive
    MAX-ACCESS   read-only
    STATUS       current
    DESCRIPTION
        "The Latitude of the Mimosa device location, in 5 decimal points."
    ::= { mimosaLocInfo 2 }

mimosaAltitude OBJECT-TYPE
    SYNTAX      Integer32
    UNITS       "meters" 
    MAX-ACCESS  read-only
    STATUS      current
    DESCRIPTION
        "The Altitude of the Mimosa device location in meters."
    ::= { mimosaLocInfo 3 }

mimosaSatelliteSNR OBJECT-TYPE
    SYNTAX       DecimalOne
    UNITS        "dB"
    MAX-ACCESS   read-only
    STATUS       current
    DESCRIPTION
        "The average Signal to Noise Ratio (SNR) amongst all of the satellites
         detected by the Mimosa device. Display is in 1 decimal point."
    ::= { mimosaLocInfo 4 }

mimosaSatelliteStrength OBJECT-TYPE
    SYNTAX  INTEGER {
                good(1),
                bad(2)
            }
    MAX-ACCESS   read-only
    STATUS       current
    DESCRIPTION
        "Strength of the satellites based on the number of satellites available.
         It is considered good if more than 2 satellites are available."
    ::= { mimosaLocInfo 5 }

mimosaGPSSatellites OBJECT-TYPE
    SYNTAX       Integer32
    MAX-ACCESS   read-only
    STATUS       current
    DESCRIPTION
        "Total number of GPS satellites detected."
    ::= { mimosaLocInfo 6 }

mimosaGlonassSatellites OBJECT-TYPE
    SYNTAX       Integer32
    MAX-ACCESS   read-only
    STATUS       current
    DESCRIPTION
        "Total number of GLONASS satellites detected."
    ::= { mimosaLocInfo 7 }

mimosaClockAccuracy OBJECT-TYPE
    SYNTAX       DecimalTwo
    UNITS        "PPB"
    MAX-ACCESS   read-only
    STATUS       current
    DESCRIPTION
        "Timing signal accuracy measured in parts per billion (PPB) by the
         Mimosa device. Display is in 2 decimal points."
    ::= { mimosaLocInfo 8 }


-- **********************************************************************
-- ***  Mimosa Device TDMA Information variables are specified below. ***
-- **********************************************************************

mimosaWirelessMode OBJECT-TYPE
    SYNTAX  INTEGER {
                accessPoint(1),
                station(2)
            }
    MAX-ACCESS  read-only
    STATUS      current
    DESCRIPTION
        "Describes wherger the Mimosa device acts as an access point or station."
    ::= { mimosaTdmaInfo 1 }

mimosaWirelessProtocol OBJECT-TYPE
    SYNTAX  INTEGER {
                tdma(1),
                csma(2)
            }
    MAX-ACCESS  read-only
    STATUS      current
    DESCRIPTION
        "Describes the wireless protocol configured on the Mimosa device. 
	     Both TDMA and CSMA are supported. TDMA is a deterministic protocol
         where each device is assigned a time slot during which it is allowed
         to transmit. This allows for collocated radios to utilize the same
         channel and avoid Tx/Rx collisions and interference."
    ::= { mimosaTdmaInfo 2 }

mimosaTDMAMode OBJECT-TYPE
    SYNTAX  INTEGER {
                a(1),
                b(2)
            }
    MAX-ACCESS  read-only
    STATUS      current
    DESCRIPTION
        "Specifies the TDMA Gender of the radio (A or B)."
    ::= { mimosaTdmaInfo 3 }

mimosaTDMAWindow OBJECT-TYPE
    SYNTAX      Integer32
    UNITS       "ms"
    MAX-ACCESS  read-only
    STATUS      current
    DESCRIPTION
        "Specifies the length of the transmit time slot in milliseconds."
    ::= { mimosaTdmaInfo 4 }

mimosaTrafficSplit OBJECT-TYPE
    SYNTAX  INTEGER {
                symmetric(1),
                asymmetric(2),
                auto(3)
            }
    MAX-ACCESS  read-only
    STATUS      current
    DESCRIPTION
        "The radio can be configured to allocate bandwidth symmetrically (50/50)
         or asymmetrically (75/25 or 25/75) in environments where traffic
         direction is expected to be heavier in one direction than the other.
         With an asymmetrical split, the local radio is represented first in the
         slash notation, (local/remote). For example, in the (75/25) split, the
         local radio gets 75, while the remote radio gets 25. If Auto is selected
         the radio will automatically determine, based upon traffic flow, which
         ratio will be used. The radio will continue to evaluate the flow and
         adjust accordingly."
    ::= { mimosaTdmaInfo 5 }


-- **********************************************************************
-- *** Mimosa Device Radio Information variables are specified below. ***
-- **********************************************************************

mimosaChainTable OBJECT-TYPE
    SYNTAX      SEQUENCE OF MimosaChainEntry
    MAX-ACCESS  not-accessible
    STATUS      current
    DESCRIPTION
        "A list of RF chain entries, which is part of MIMO tables. MIMO stands
         for Multiple In Multiple Out."
    ::= { mimosaRfInfo 1 }

mimosaChainEntry OBJECT-TYPE
    SYNTAX      MimosaChainEntry
    MAX-ACCESS  not-accessible
    STATUS      current
    DESCRIPTION
        "An entry containing chain information applicable to a particular
         RF chain."
    INDEX   { mimosaChain }
    ::= { mimosaChainTable 1 }

MimosaChainEntry ::=
    SEQUENCE {
        mimosaChain        Integer32,
        mimosaTxPower      DecimalOne,
        mimosaRxPower      DecimalOne,
        mimosaRxNoise      DecimalOne,
        mimosaSNR          DecimalOne,
        mimosaCenterFreq   Integer32,
        mimosaPolarization INTEGER
    }

mimosaChain OBJECT-TYPE
    SYNTAX      Integer32 (0..65535)
    MAX-ACCESS  not-accessible
    STATUS      current
    DESCRIPTION
        "An index which is used to access a particular entry in the chain table."
    ::= { mimosaChainEntry 1 }

mimosaTxPower OBJECT-TYPE
    SYNTAX      DecimalOne
    UNITS       "dBm"
    MAX-ACCESS  read-only
    STATUS      current
    DESCRIPTION
        "Specifies the transmit power of the given RF chain. A value of -8 means
         this particular TxChain is not a valid entry."
    ::= { mimosaChainEntry 2 }

mimosaRxPower OBJECT-TYPE
    SYNTAX      DecimalOne
    UNITS       "dBm"
    MAX-ACCESS  read-only
    STATUS      current
    DESCRIPTION
        "Specifies the receive power of the given RF chain. A value of -100
         means this particular RxChain is not a valid entry (SNR must be -100)."
    ::= { mimosaChainEntry 3 }

mimosaRxNoise OBJECT-TYPE
    SYNTAX      DecimalOne
    UNITS       "dBm"
    MAX-ACCESS  read-only
    STATUS      current
    DESCRIPTION
        "Specifies the received noise level for the given RF chain."
    ::= { mimosaChainEntry 4 }

mimosaSNR OBJECT-TYPE
    SYNTAX      DecimalOne
    UNITS       "dB"
    MAX-ACCESS  read-only
    STATUS      current
    DESCRIPTION
        "Indicates the Signal to Noise Ratio (SNR) for the given RF chain.
         A value of -100 means this particular RxChain is not a valid entry."
    ::= { mimosaChainEntry 5 }

mimosaCenterFreq OBJECT-TYPE
    SYNTAX      Integer32
    UNITS       "MHz"
    MAX-ACCESS  read-only
    STATUS      current
    DESCRIPTION
        "The center frequency for the given RF chain. A value of 0 means this
         particular Chain is not a valid entry."
    ::= { mimosaChainEntry 6 }

mimosaPolarization OBJECT-TYPE
    SYNTAX  INTEGER {
                horizontal(1),
                vertical(2)
            }
    MAX-ACCESS  read-only
    STATUS      current
    DESCRIPTION
        "The ploarization of the given RF chain. It could be horizontal or
         vertical."
    ::= { mimosaChainEntry 7 }


mimosaStreamTable OBJECT-TYPE
    SYNTAX      SEQUENCE OF MimosaStreamEntry
    MAX-ACCESS  not-accessible
    STATUS      current
    DESCRIPTION
        "A list of data stream entries, which are part of MIMO tables. MIMO
         stands for Multiple In Multiple Out."
    ::= { mimosaRfInfo 2 }

mimosaStreamEntry OBJECT-TYPE
    SYNTAX      MimosaStreamEntry
    MAX-ACCESS  not-accessible
    STATUS      current
    DESCRIPTION
        "The entry containing information applicable to a particular stream."
    INDEX   { mimosaStream }
    ::= { mimosaStreamTable 1 }

MimosaStreamEntry ::=
    SEQUENCE {
        mimosaStream       Integer32,
        mimosaTxPhy        Integer32,
        mimosaTxMCS        Integer32,
        mimosaTxWidth      Integer32,
	mimosaRxPhy        Integer32,
        mimosaRxMCS        Integer32,
        mimosaRxWidth      Integer32,
	mimosaRxEVM        DecimalOne
   }

mimosaStream OBJECT-TYPE
    SYNTAX      Integer32 (0..65535)
    MAX-ACCESS  not-accessible
    STATUS      current
    DESCRIPTION
        "The index used to access a particular entry in the stream table."
    ::= { mimosaStreamEntry 1 }

mimosaTxPhy OBJECT-TYPE
    SYNTAX      Integer32
    UNITS       "Mbps"
    MAX-ACCESS  read-only
    STATUS      current
    DESCRIPTION
        "Specifies the transmit rate of the given data stream."
    ::= { mimosaStreamEntry 2 }

mimosaTxMCS OBJECT-TYPE
    SYNTAX      Integer32
    MAX-ACCESS  read-only
    STATUS      current
    DESCRIPTION
        "Specifies the transmit MCS of the given data stream. A value of
         -1 means this particular TxStream is not a valid entry."
    ::= { mimosaStreamEntry 3 }

mimosaTxWidth OBJECT-TYPE
    SYNTAX      Integer32
    UNITS       "MHz"
    MAX-ACCESS  read-only
    STATUS      current
    DESCRIPTION
        "Specifies the channel width based on MCS. A value of 
	 -1 means this particular TxWidth is not a valid entry"
    ::= { mimosaStreamEntry 4 }

mimosaRxPhy OBJECT-TYPE
    SYNTAX      Integer32
    UNITS       "Mbps"
    MAX-ACCESS  read-only
    STATUS      current
    DESCRIPTION
        "Specifies the receive rate of the given data stream."
    ::= { mimosaStreamEntry 5 }

mimosaRxMCS OBJECT-TYPE
    SYNTAX      Integer32
    MAX-ACCESS  read-only
    STATUS      current
    DESCRIPTION
        "Specifies the receive MCS of the given data stream. A value of
         -1 means this particular RxStream is not a valid entry."
    ::= { mimosaStreamEntry 6 }

mimosaRxWidth OBJECT-TYPE
    SYNTAX      Integer32
    UNITS	"MHz"
    MAX-ACCESS  read-only
    STATUS      current
    DESCRIPTION
        "Specifies the receive Rx Width of the given data stream. A value of
         -1 means this particular RxWidth is not a valid entry."
    ::= { mimosaStreamEntry 7 }

mimosaRxEVM OBJECT-TYPE
    SYNTAX      DecimalOne
    UNITS       "dB"
    MAX-ACCESS  read-only
    STATUS      current
    DESCRIPTION
        "Specifies the receive Error Vector Magnitude (EVM) of the given data
         stream."
    ::= { mimosaStreamEntry 8 }

mimosaChannelTable OBJECT-TYPE
    SYNTAX      SEQUENCE OF MimosaChannelEntry
    MAX-ACCESS  not-accessible
    STATUS      current
    DESCRIPTION
            "A list of RF channel entries on the Mimosa device."
    ::= { mimosaRfInfo 3 }

mimosaChannelEntry OBJECT-TYPE
    SYNTAX      MimosaChannelEntry
    MAX-ACCESS  not-accessible
    STATUS      current
    DESCRIPTION
        "The entry containing management information applicable to a particular
         channel."
    INDEX   { mimosaChannel }
    ::= { mimosaChannelTable 1 }

MimosaChannelEntry ::=
    SEQUENCE {
        mimosaChannel            Integer32,
        mimosaChannelMode        INTEGER,
        mimosaChannelWidth       Integer32,
        mimosaChannelTxPower     DecimalOne,
        mimosaChannelCenterFreq  Integer32
    }

mimosaChannel OBJECT-TYPE
    SYNTAX      Integer32 (0..65535)
    MAX-ACCESS  not-accessible
    STATUS      current
    DESCRIPTION
        "The index used to access a particular entry in the RF channel table."
    ::= { mimosaChannelEntry 1 }

mimosaChannelMode OBJECT-TYPE
    SYNTAX  INTEGER {
                transmit(1),
                receive(2),
                bidirectional(3)
            }
    MAX-ACCESS  read-only
    STATUS      current
    DESCRIPTION
	"Specifies the mode for the given channel. The transmit or receive
	 values indicate Frequency Diversity (FD) mode is in use. The
	 bidirectional value means that the channel is used for both transmit
	 and receive in all other single or dual channel modes."
    ::= { mimosaChannelEntry 2 }

mimosaChannelWidth OBJECT-TYPE
    SYNTAX      Integer32
    UNITS       "MHz"
    MAX-ACCESS  read-only
    STATUS      current
    DESCRIPTION
        "Specifies the channel width of the given channel."
    ::= { mimosaChannelEntry 3 }

mimosaChannelTxPower OBJECT-TYPE
    SYNTAX      Integer32
    UNITS       "dBm"
    MAX-ACCESS  read-only
    STATUS      current
    DESCRIPTION
        "Specifies the transmit power level on the channel. If Channel Width
         is set to 1xN MHz, Channel 2 is not be used. In Frequency Diversity mode,
         Power 1 and Power 2 represent transmit power on the local and remote
         sides, respectively."
    ::= { mimosaChannelEntry 4 }

mimosaChannelCenterFreq OBJECT-TYPE
    SYNTAX      Integer32
    UNITS       "MHz"
    MAX-ACCESS  read-only
    STATUS      current
    DESCRIPTION
        "Specifies the center frequency of the channel used on the link. In all
         modes, the center frequency represents the absolute center of the
         selected channel width without any offset, and the center can be moved
         in 5 MHz increments.

         A value of 0 means this particular channel is not a valid entry."
    ::= { mimosaChannelEntry 5 }

mimosaAntennaGain OBJECT-TYPE
    SYNTAX       Integer32
    UNITS        "dBi"
    MAX-ACCESS   read-only
    STATUS       current
    DESCRIPTION
        "The antenna gain on the Mimosa device."
    ::= { mimosaRfInfo 4 }

mimosaTotalTxPower OBJECT-TYPE
    SYNTAX      DecimalOne
    UNITS        "dBm"
    MAX-ACCESS   read-only
    STATUS       current
    DESCRIPTION
        "The total transmit power for all the channels on the Mimosa device."
    ::= { mimosaRfInfo 5 }

mimosaTotalRxPower OBJECT-TYPE
    SYNTAX      DecimalOne
    UNITS        "dBm"
    MAX-ACCESS   read-only
    STATUS       current
    DESCRIPTION
        "The total receive power for all the channels on the Mimosa device."
    ::= { mimosaRfInfo 6 }

mimosaTargetSignalStrength OBJECT-TYPE
    SYNTAX      Integer32
    UNITS        "dB"
    MAX-ACCESS   read-only
    STATUS       current
    DESCRIPTION
        "The calculated target receive signal strength based on device coordinates and settings."
    ::= { mimosaRfInfo 7 }


-- **********************************************************************
-- ***  Mimosa Device WAN Information variables are specified below.  ***
-- **********************************************************************

mimosaWanSsid OBJECT-TYPE
    SYNTAX      DisplayString (SIZE (0..64))
    MAX-ACCESS  read-only
    STATUS      current
    DESCRIPTION
        "The wireless link name used by both radios. Both AP and Station must
         use the same SSID to communicate with each other."
    ::= { mimosaWanInfo 1 }

mimosaWanMac OBJECT-TYPE
    SYNTAX      PhysAddress
    MAX-ACCESS  read-only
    STATUS      current
    DESCRIPTION
        "The MAC address used for the wireless link."
    ::= { mimosaWanInfo 2 }

mimosaWanStatus OBJECT-TYPE
    SYNTAX  INTEGER {
                connected(1),
                disconnected(2)
            }
    MAX-ACCESS  read-only
    STATUS      current
    DESCRIPTION
        "The wireless link status between the Mimosa devices."
    ::= { mimosaWanInfo 3 }

mimosaWanUpTime OBJECT-TYPE
    SYNTAX      TimeTicks
    MAX-ACCESS  read-only
    STATUS      current
    DESCRIPTION
        "The wireless link up time since last reboot."
    ::= { mimosaWanInfo 4 }


-- ****************************************************************************
-- *** Mimosa Device Performance Information variables are specified below. ***
-- ****************************************************************************

mimosaPhyTxRate OBJECT-TYPE
    SYNTAX      DecimalTwo
    UNITS       "kbps" 
    MAX-ACCESS  read-only
    STATUS      current
    DESCRIPTION
        "The transmit packet rate at the physical level over a 5 second interval."
    ::= { mimosaPerfInfo 1 }

mimosaPhyRxRate OBJECT-TYPE
    SYNTAX      DecimalTwo
    UNITS       "kbps" 
    MAX-ACCESS  read-only
    STATUS      current
    DESCRIPTION
        "The receive packet rate at the physical level over a 5 second interval."
    ::= { mimosaPerfInfo 2 }

mimosaPerTxRate OBJECT-TYPE
    SYNTAX      DecimalTwo
    UNITS       "%"
    MAX-ACCESS  read-only
    STATUS      current
    DESCRIPTION
        "The trasnmit Packet Error Rate (PER) over a 5 second interval. It is
         caluculated as packets with errors versuss packets without errors."
    ::= { mimosaPerfInfo 3 }

mimosaPerRxRate OBJECT-TYPE
    SYNTAX      DecimalTwo
    MAX-ACCESS  read-only
    STATUS      current
    DESCRIPTION
        "The receive Packet Error Rate (PER) over a 5 second interval. It is
         caluculated as packets with errors versuss packets without errors."
    ::= { mimosaPerfInfo 4 }


-- ****************************************************************************
-- *** Mimosa Device Management  Information variables are specified below. ***
-- ****************************************************************************

mimosaNetworkMode OBJECT-TYPE
    SYNTAX  INTEGER {
                enabled(1),
                disabled(2),
                auto(3)
            }
    MAX-ACCESS  read-only
    STATUS      current
    DESCRIPTION
        "Specifies the mode for the local 2.4 GHz wireless network operation.
         If Auto is selected, the 2.4 GHz management network is turned on for a
         limited time (defined in Console Timeout ) after boot and then turned
         off if there is no activity. If a user associates with the radio within
         the timeout period, they will not be disconnected."
    ::= { mimosaMgmtInfo 1 }

mimosaRecoverySsid OBJECT-TYPE
    SYNTAX      DisplayString (SIZE (0..32))
    MAX-ACCESS  read-only
    STATUS      current
    DESCRIPTION
        "The recovery SSID that allows the device to be reset to factory
         defaults. This is available for 10 minutes after device boot. Disabling
         the 2.4 GHz management network will not impact availability of this
         option. The serial number of the device must be known in order to
         perform the factory reset."
    ::= { mimosaMgmtInfo 2 }

mimosaLocalSsid OBJECT-TYPE
    SYNTAX      DisplayString (SIZE (0..32))
    MAX-ACCESS  read-only
    STATUS      current
    DESCRIPTION
        "The SSID for managing the local 2.4 GHz wireless interface."
    ::= { mimosaMgmtInfo 3 }

mimosaLocalChannel OBJECT-TYPE
    SYNTAX      Integer32
    MAX-ACCESS  read-only
    STATUS      current
    DESCRIPTION
	"The channel used for the local 2.4 GHz wireless interface."
    ::= { mimosaMgmtInfo 4 }

mimosaConsoleTimeout OBJECT-TYPE
    SYNTAX      Integer32
    UNITS       "min"
    MAX-ACCESS  read-only
    STATUS      current
    DESCRIPTION
	"The amount inactivity on the 2.4 GHz wireless interface before
         turning it off in Auto mode."
    ::= { mimosaMgmtInfo 5 }

mimosaMaxClients OBJECT-TYPE
    SYNTAX      Integer32
    MAX-ACCESS  read-only
    STATUS      current
    DESCRIPTION
	"The maximum number of wireless clients that can simultaneously access
         the 2.4 GHz management interface."
    ::= { mimosaMgmtInfo 6 }

mimosaLocalMac OBJECT-TYPE
    SYNTAX      PhysAddress
    MAX-ACCESS  read-only
    STATUS      current
    DESCRIPTION
        "The MAC address used for 2.4 GHz wireless link."
    ::= { mimosaMgmtInfo 7 }

mimosaLocalIpAddr OBJECT-TYPE
    SYNTAX      IpAddress
    MAX-ACCESS  read-only
    STATUS      current
    DESCRIPTION
        "The IP address assigned to the 2.4 GHz wireless link."
    ::= { mimosaMgmtInfo 8 }

mimosaLocalNetMask OBJECT-TYPE
    SYNTAX      IpAddress
    MAX-ACCESS  read-only
    STATUS      current
    DESCRIPTION
        "The IP netmask assigned to the 2.4 GHz wireless link."
    ::= { mimosaMgmtInfo 9 }

mimosaLocalGateway OBJECT-TYPE
    SYNTAX      IpAddress
    MAX-ACCESS  read-only
    STATUS      current
    DESCRIPTION
        "The IP address of the gateway for the 2.4 GHz wireless link."
    ::= { mimosaMgmtInfo 10 }

mimosaFlowControl OBJECT-TYPE
    SYNTAX      INTEGER {
                    enabled(1),
                    disabled(2)
                }
    MAX-ACCESS  read-only
    STATUS      current
    DESCRIPTION
        "Specifies whether Flow Control is enabled on the Mimosa device."
    ::= { mimosaMgmtInfo 11 }
 


-- *************************************************************************
-- *** Mimosa Device Services Information variables are specified below. ***
-- *************************************************************************

mimosaHttpsEnabled OBJECT-TYPE
    SYNTAX  INTEGER {
                enabled(1),
                disabled(2)
            }
    MAX-ACCESS  read-only
    STATUS      current
    DESCRIPTION
        "Specifies whether HTTPS is enabled on the Mimosa device."
    ::= { mimosaServices 1 }

mimosaMgmtVlanEnabled OBJECT-TYPE
    SYNTAX  INTEGER {
                enabled(1),
                disabled(2)
            }
    MAX-ACCESS  read-only
    STATUS      current
    DESCRIPTION
        "Specifies whether the Management VLAN is enabled on the Mimosa device."
    ::= { mimosaServices 2 }

mimosaMgmtCloudEnabled OBJECT-TYPE
    SYNTAX  INTEGER {
                enabled(1),
                disabled(2)
            }
    MAX-ACCESS  read-only
    STATUS      current
    DESCRIPTION
        "Specifies whether the Management Cloud is enabled on the Mimosa device."
    ::= { mimosaServices 3 }

mimosaRestMgmtEnabled OBJECT-TYPE
    SYNTAX  INTEGER {
                enabled(1),
                disabled(2)
            }
    MAX-ACCESS  read-only
    STATUS      current
    DESCRIPTION
        "Specifies whether the REST management is enabled on the Mimosa device."
    ::= { mimosaServices 4 }

mimosaPingWatchdogEnabled OBJECT-TYPE
    SYNTAX  INTEGER {
                enabled(1),
                disabled(2)
            }
    MAX-ACCESS  read-only
    STATUS      current
    DESCRIPTION
        "Specifies whether the IP Ping watchdog is enabled on the Mimosa device.
         This is used to reset the device if a configured IP address is
         not reached in certain number of retries."
    ::= { mimosaServices 5 }

mimosaSyslogEnabled OBJECT-TYPE
    SYNTAX  INTEGER {
                enabled(1),
                disabled(2)
            }
    MAX-ACCESS  read-only
    STATUS      current
    DESCRIPTION
        "Specifies whether the Syslog client is enabled on the Mimosa device.
         Syslog client sends the log messages to configured syslog server."
    ::= { mimosaServices 6 }

mimosaNtpMode OBJECT-TYPE
    SYNTAX  INTEGER {
                custom(1),
                standard(2)
            }
    MAX-ACCESS  read-only
    STATUS      current
    DESCRIPTION
        "Specifies whether the NTP client is configured to use standard servers
         from NIST, NTP organizations or custom NTP server."
    ::= { mimosaServices 7 }

mimosaNtpServer OBJECT-TYPE
    SYNTAX      DisplayString (SIZE (0..64))
    MAX-ACCESS  read-only
    STATUS      current
    DESCRIPTION
        "Specifies the name or address of the custom NTP server."
    ::= { mimosaServices 8 }

END



File: /dude_custom_files\MIMOSA-MIB-COMMON.txt
MIMOSA-NETWORKS-COMMON-MIB DEFINITIONS ::= BEGIN

--  Copyright (C) 2017, Mimosa Networks, Inc. All Rights Reserved.
--
--  Mimosa Networks MIB
--  Revision: 1.00
--  Date: February 15, 2017
--
--  Mimosa Networks, Inc.
--  469 El Camino Real Suite 100
--  Santa Clara, CA 95050
--  support@mimosa.co
--
--  This MIB defines the MIB specification for Mimosa Network's Products
--
--  Mimosa reserves the right to make changes to this MIB specification as
--  well as other information related to this specification without prior
--  notice.  The user of this specification should consult Mimosa Networks,
--  to determine if any such changes have been made.
--
--  Current MIBs are available from Mimosa Networks at the following URLs:
--
--		http://help.mimosa.co
--
--  In no event shall Mimosa Networks, Inc. be liable for any indirect,
--  consequential, special or incidental damages whatsoever (including
--  but not limited to lost profits or lost revenue) arising out of or
--  related to this specification or the information contained in it.
--  This non-liability extends to even if Mimosa Networks Inc. has been
--  advised of, known, or should have known, the potential for such damages.

--  Mimosa Networks, Inc. hereby grants end-users, and other parties a
--  a non-exclusive license to use this MIB specification in order to
--  manage products of Mimosa Networks, Inc.


IMPORTS
    MODULE-IDENTITY, OBJECT-TYPE,
    Integer32                             FROM SNMPv2-SMI

    DisplayString                         FROM SNMPv2-TC

    MODULE-COMPLIANCE, OBJECT-GROUP 	  FROM SNMPv2-CONF

    mimosaWireless,
    mimosaConformanceGroup                FROM MIMOSA-NETWORKS-BASE-MIB

    DecimalOne, DecimalTwo, DecimalFive   FROM MIMOSA-MIB-TC;


mimosaCommonModule MODULE-IDENTITY
    LAST-UPDATED "201702150000Z"
    ORGANIZATION "Mimosa Networks
    			  www.mimosa.co"
    CONTACT-INFO
    	"postal:
    	Mimosa Networks, Inc.
		469 El Camino Real Suite 100
		Santa Clara, CA 95050
        email: support@mimosa.co"
    DESCRIPTION
		"Mimosa device MIB definitions"
	REVISION	"201702150000Z"
    DESCRIPTION
		"Common MIB definitions for all Mimosa Products"
    ::= { mimosaConformanceGroup 3 }

mimosaGeneral       OBJECT IDENTIFIER ::= { mimosaWireless 1 }
mimosaLocInfo       OBJECT IDENTIFIER ::= { mimosaWireless 2 }

-- *****************************************************************
-- ***       Mimosa General variables are specified below.    ***
-- *****************************************************************

mimosaDeviceName OBJECT-TYPE
    SYNTAX      DisplayString (SIZE (0..64))
    MAX-ACCESS  read-only
    STATUS      current
    DESCRIPTION
        "The name of the local Mimosa device. This unique identifier could
         be the same as the sysName object."
    ::= { mimosaGeneral 1 }

mimosaSerialNumber OBJECT-TYPE
    SYNTAX      DisplayString (SIZE (0..64))
    MAX-ACCESS  read-only
    STATUS      current
    DESCRIPTION
        "The unique serial number of the Mimosa device."
    ::= { mimosaGeneral 2 }

mimosaFirmwareVersion OBJECT-TYPE
    SYNTAX      DisplayString (SIZE (0..64))
    MAX-ACCESS  read-only
    STATUS      current
    DESCRIPTION
        "The version of the currently installed and/or running firmware
         on the Mimosa device."
    ::= { mimosaGeneral 3 }

mimosaFirmwareBuildDate OBJECT-TYPE
    SYNTAX      DisplayString (SIZE (0..64))
    MAX-ACCESS  read-only
    STATUS      current
    DESCRIPTION
        "The creation date of the currently installed and/or running
         firmware on the Mimosa device."
    ::= { mimosaGeneral 4 }

mimosaLastRebootTime OBJECT-TYPE
    SYNTAX      DisplayString (SIZE (0..64))
    MAX-ACCESS  read-only
    STATUS      current
    DESCRIPTION
        "The last time the Mimosa device rebooted."
    ::= { mimosaGeneral 5 }

mimosaUnlockCode OBJECT-TYPE
    SYNTAX      DisplayString (SIZE (0..64))
    MAX-ACCESS  read-only
    STATUS      current
    DESCRIPTION
        "The code used to unlock the Mimosa device."
    ::= { mimosaGeneral 6 }

mimosaLEDBrightness OBJECT-TYPE
    SYNTAX  INTEGER {
                auto(1),
                low(2),
                medium(3),
                high(4),
                off(5)
            }
    MAX-ACCESS  read-only
    STATUS      current
    DESCRIPTION
        "Indicates the intensity of the status indicator lights on the
         device exterior. The Auto option adjusts the amount of light
         based upon ambient conditions. Manual options include Low,
         Medium, and High."
    ::= { mimosaGeneral 7 }

mimosaInternalTemp OBJECT-TYPE
    SYNTAX       Integer32
    UNITS        "C" 
    MAX-ACCESS   read-only
    STATUS       current
    DESCRIPTION
        "The internal temperature of the Mimosa device."
    ::= { mimosaGeneral 8 }

mimosaRegulatoryDomain OBJECT-TYPE
    SYNTAX      DisplayString (SIZE (0..64))
    MAX-ACCESS  read-only
    STATUS      current
    DESCRIPTION
        "The country in which the Mimosa device has been configured to run."
    ::= { mimosaGeneral 9 }

mimosaRebootReason OBJECT-TYPE
    SYNTAX      DisplayString (SIZE (0..64))
    MAX-ACCESS  read-only
    STATUS      current
    DESCRIPTION
        "Displays the reason of the last reboot of the Mimosa device"
    ::= { mimosaGeneral 10 }

-- **********************************************************************
-- ***     Mimosa Device Location variables are specified below.      ***
-- **********************************************************************

mimosaLongitude OBJECT-TYPE
    SYNTAX       DecimalFive
    MAX-ACCESS   read-only
    STATUS       current
    DESCRIPTION
        "The Longitude of the Mimosa device location, in 5 decimal points."
    ::= { mimosaLocInfo 1 }

mimosaLatitude OBJECT-TYPE
    SYNTAX       DecimalFive
    MAX-ACCESS   read-only
    STATUS       current
    DESCRIPTION
        "The Latitude of the Mimosa device location, in 5 decimal points."
    ::= { mimosaLocInfo 2 }

mimosaAltitude OBJECT-TYPE
    SYNTAX      DecimalTwo
    UNITS       "meters" 
    MAX-ACCESS  read-only
    STATUS      current
    DESCRIPTION
        "The Altitude of the Mimosa device location in meters."
    ::= { mimosaLocInfo 3 }

mimosaSatelliteSNR OBJECT-TYPE
    SYNTAX       DecimalOne
    UNITS        "dB"
    MAX-ACCESS   read-only
    STATUS       current
    DESCRIPTION
        "The average Signal to Noise Ratio (SNR) amongst all of the satellites
         detected by the Mimosa device. Display is in 1 decimal point."
    ::= { mimosaLocInfo 4 }

mimosaSatelliteStrength OBJECT-TYPE
    SYNTAX  INTEGER {
                good(1),
                bad(2)
            }
    MAX-ACCESS   read-only
    STATUS       current
    DESCRIPTION
        "Strength of the satellites based on the number of satellites available.
         It is considered good if more than 2 satellites are available."
    ::= { mimosaLocInfo 5 }

mimosaGPSSatellites OBJECT-TYPE
    SYNTAX       Integer32
    MAX-ACCESS   read-only
    STATUS       current
    DESCRIPTION
        "Total number of GPS satellites detected."
    ::= { mimosaLocInfo 6 }

mimosaGlonassSatellites OBJECT-TYPE
    SYNTAX       Integer32
    MAX-ACCESS   read-only
    STATUS       current
    DESCRIPTION
        "Total number of GLONASS satellites detected."
    ::= { mimosaLocInfo 7 }

mimosaClockAccuracy OBJECT-TYPE
    SYNTAX       DecimalTwo
    UNITS        "PPB"
    MAX-ACCESS   read-only
    STATUS       current
    DESCRIPTION
        "Timing signal accuracy measured in parts per billion (PPB) by the
         Mimosa device. Display is in 2 decimal points."
    ::= { mimosaLocInfo 8 }

---
---  Conformance/Compliance Statements
---
mimosaCommonConformance         OBJECT IDENTIFIER ::= { mimosaConformanceGroup 1 }

mimosaCommonCompliances         OBJECT IDENTIFIER ::= { mimosaCommonConformance 1 }
mimosaCommonGroups              OBJECT IDENTIFIER ::= { mimosaCommonConformance 2 }


mimosaCommonCompliance      MODULE-COMPLIANCE
    STATUS      current
    DESCRIPTION
        "The compliance statement for all Mimosa products that implement
         this MIB."
    MODULE
        GROUP mimosaGeneralGroup
        DESCRIPTION
            "The mimosaGeneralGroup is mandatory only devices that implement
             B5 MIB and PTMP MIB."

        GROUP mimosaLocationGroup
        DESCRIPTION
            "The mimosaLocationGroup is mandatory only devices that have GPS
             capabilities."
        
    ::= { mimosaCommonCompliances 1 }


mimosaGeneralGroup           OBJECT-GROUP
    OBJECTS {
            mimosaDeviceName,
            mimosaSerialNumber,
            mimosaFirmwareVersion,
            mimosaFirmwareBuildDate,
            mimosaLastRebootTime,
            mimosaUnlockCode,
            mimosaLEDBrightness,
            mimosaInternalTemp,
            mimosaRegulatoryDomain,
            mimosaRebootReason
    }
    STATUS      current
    DESCRIPTION
        "A collection of objects for the general information of the device."
    ::= { mimosaCommonGroups 1 }


mimosaLocationGroup           OBJECT-GROUP
    OBJECTS {
            mimosaLongitude,
            mimosaLatitude,
            mimosaAltitude,
            mimosaSatelliteSNR,
            mimosaSatelliteStrength,
            mimosaGPSSatellites,
            mimosaGlonassSatellites,
            mimosaClockAccuracy
    }
    STATUS      current
    DESCRIPTION
        "A collection of objects for the location information of the device."
    ::= { mimosaCommonGroups 2 }

END



File: /dude_custom_files\MIMOSA-MIB-PTMP.txt
MIMOSA-NETWORKS-PTMP-MIB DEFINITIONS ::= BEGIN

--  Copyright (C) 2017, Mimosa Networks, Inc. All Rights Reserved.
--
--  Mimosa Networks MIB
--  Revision: 0.3
--  Date: April 05, 2017
--
--  Mimosa Networks, Inc.
--  469 El Camino Real, Suite 100
--  Santa Clara, CA 95050
--  support@mimosa.co
--
--  This MIB defines the MIB specification for Mimosa Network's Products
--
--  Mimosa reserves the right to make changes to this MIB specification as
--  well as other information related to this specification without prior
--  notice.  The user of this specification should consult Mimosa Networks,
--  to determine if any such changes have been made.
--
--  Current MIBs are available from Mimosa Networks at the following URLs:
--
--      http://help.mimosa.co
--
--  In no event shall Mimosa Networks, Inc. be liable for any indirect,
--  consequential, special or incidental damages whatsoever (including
--  but not limited to lost profits or lost revenue) arising out of or
--  related to this specification or the information contained in it.
--  This non-liability extends to even if Mimosa Networks Inc. has been
--  advised of, known, or should have known, the potential for such damages.

--  Mimosa Networks, Inc. hereby grants end-users, and other parties a
--  a non-exclusive license to use this MIB specification in order to
--  manage products of Mimosa Networks, Inc.


IMPORTS
    OBJECT-TYPE, MODULE-IDENTITY,
    IpAddress, Integer32, Counter64,
    Unsigned32                              FROM SNMPv2-SMI

    DisplayString, TruthValue,
    MacAddress, TimeStamp                   FROM SNMPv2-TC

    MODULE-COMPLIANCE, OBJECT-GROUP         FROM SNMPv2-CONF

    DecimalOne, DecimalTwo,
    Mimosa5GHzFrequency,
    Mimosa5GHzChannelNumber                 FROM MIMOSA-MIB-TC

    mimosaWireless, mimosaConformanceGroup  FROM MIMOSA-NETWORKS-BASE-MIB;


-- *****************************************************************
-- ***       Mimosa PTMP variables are specified below.          ***
-- *****************************************************************

mimosaPtmp  MODULE-IDENTITY
    LAST-UPDATED    "201704050000Z"
    ORGANIZATION    "Mimosa Networks"
    CONTACT-INFO
        "
            Postal: Mimosa Networks, Inc.
                    469 El Camino Real, Suite 100
                    Santa Clara, CA 95050
                    US

               Tel: +1-408-628-1277

            E-mail: inquiry@mimosa.co
        "
    DESCRIPTION
        "The MIB module for Mimosa PTMP products"
    REVISION        "201704050000Z"
    DESCRIPTION
            "The first version of this MIB"
    ::= { mimosaWireless 9 }

mimosaPtmpSsid          OBJECT IDENTIFIER ::= { mimosaPtmp 1 }
mimosaPtmpLinkInfo      OBJECT IDENTIFIER ::= { mimosaPtmp 2 }
mimosaPtmpChannelPower  OBJECT IDENTIFIER ::= { mimosaPtmp 3 }
mimosaPtmpApStats       OBJECT IDENTIFIER ::= { mimosaPtmp 4 }
mimosaPtmpClientInfo    OBJECT IDENTIFIER ::= { mimosaPtmp 5 }
mimosaPtmpClientStats   OBJECT IDENTIFIER ::= { mimosaPtmp 6 }
mimosaPtmpMgmtInfo      OBJECT IDENTIFIER ::= { mimosaPtmp 7 }


-- *************************************************************************
-- ***      Mimosa SSID Information variables are specified below.       ***
-- *************************************************************************

mimosaPtmpSsidTable                 OBJECT-TYPE
    SYNTAX      SEQUENCE OF MimosaPtmpSsidEntry
    MAX-ACCESS  not-accessible
    STATUS      current
    DESCRIPTION
        "A list of A5 SSID entries"
    ::= { mimosaPtmpSsid 1 }


mimosaPtmpSsidEntry                 OBJECT-TYPE
    SYNTAX      MimosaPtmpSsidEntry
    MAX-ACCESS  not-accessible
    STATUS      current
    DESCRIPTION
        "Entry that describes each SSID and all its related configuration"
    INDEX   { mimosaPtmpSsidIndex }
    ::= { mimosaPtmpSsidTable 1 }

MimosaPtmpSsidEntry ::=
    SEQUENCE {
        mimosaPtmpSsidIndex                 Integer32,
        mimosaPtmpSsidName                  DisplayString,
        mimosaPtmpSsidType                  INTEGER,
        mimosaPtmpSsidEnabled               TruthValue,
        mimosaPtmpSsidBroadcastEnabled      TruthValue,
        mimosaPtmpSsidIsolationEnabled      TruthValue
   }

mimosaPtmpSsidIndex                 OBJECT-TYPE
    SYNTAX      Integer32(1..24)
    MAX-ACCESS  not-accessible
    STATUS      current
    DESCRIPTION
        "Describes the index used to access a particular entry in the SSID
        table."
    ::= { mimosaPtmpSsidEntry 1 }

mimosaPtmpSsidName                  OBJECT-TYPE
    SYNTAX      DisplayString (SIZE (1..32))
    MAX-ACCESS  read-only
    STATUS      current
    DESCRIPTION
        "Describes the name of the SSID"
    ::= { mimosaPtmpSsidEntry 2 }

mimosaPtmpSsidType                  OBJECT-TYPE
    SYNTAX      INTEGER {
                    hotspot(0),
                    cpe(1)
                }
    MAX-ACCESS  read-only
    STATUS      current
    DESCRIPTION
        "Describes the type of clients that will connect to this SSID. CPE
         represents fixed, or Hotspot represents mobile devices"
    ::= { mimosaPtmpSsidEntry 3 }

mimosaPtmpSsidEnabled               OBJECT-TYPE
    SYNTAX      TruthValue
    MAX-ACCESS  read-only
    STATUS      current
    DESCRIPTION
        "Describes if the SSID is enabled (True) or disabled (False)"
    ::= { mimosaPtmpSsidEntry 4 }

mimosaPtmpSsidBroadcastEnabled      OBJECT-TYPE
    SYNTAX      TruthValue
    MAX-ACCESS  read-only
    STATUS      current
    DESCRIPTION
        "Describes if the Broadcast feature for this SSID is enabled or 
        disabled"
    ::= { mimosaPtmpSsidEntry 5 }

mimosaPtmpSsidIsolationEnabled      OBJECT-TYPE
    SYNTAX      TruthValue
    MAX-ACCESS  read-only
    STATUS      current
    DESCRIPTION
        "Describes if the client isolation is enabled or disabled"
    ::= { mimosaPtmpSsidEntry 6 }


-- *************************************************************************
-- *** Mimosa PTMP Link Information variables are specified below.       ***
-- *************************************************************************

mimosaPtmpWirelessMode              OBJECT-TYPE
    SYNTAX      INTEGER {
                    srs (1),
                    wifiinterop (2)
                }
    MAX-ACCESS  read-only
    STATUS      current
    DESCRIPTION
        "Describes the wireless protocol configured on the Mimosa Device"
    ::= { mimosaPtmpLinkInfo 1 }

mimosaPtmpWirelessGender            OBJECT-TYPE
    SYNTAX      INTEGER {
                    a (1),
                    b (2)
                }
    MAX-ACCESS  read-only
    STATUS      current
    DESCRIPTION
        "Describes the wireless protocol gender that defines the transmit
         and receive timing"
    ::= { mimosaPtmpLinkInfo 2 }

mimosaPtmpWirelessTrafficSplit      OBJECT-TYPE
    SYNTAX      DisplayString
    MAX-ACCESS  read-only
    STATUS      current
    DESCRIPTION
        "Describes how the bandwidth is split between the AP and Station"
    ::= { mimosaPtmpLinkInfo 3 }

mimosaPtmpWirelessWindowLength      OBJECT-TYPE
    SYNTAX      Integer32
    MAX-ACCESS  read-only
    STATUS      current
    DESCRIPTION
        "Describes the length of the transmit time slot in milliseconds"
    ::= { mimosaPtmpLinkInfo 4 }

-- *************************************************************************
-- *** Mimosa Radio Channel Power Information variables are specified  . ***
-- *************************************************************************

mimosaPtmpAutoChannelEnabled        OBJECT-TYPE
    SYNTAX      TruthValue
    MAX-ACCESS  read-only
    STATUS      current
    DESCRIPTION
        "Describes if the Auto Channel feature is Enabled or Disabled. This
         function selects the channel that results in the best RF
         performance."
    ::= { mimosaPtmpChannelPower 1 }

mimosaPtmpAntennaGain               OBJECT-TYPE
    SYNTAX      Unsigned32
    MAX-ACCESS  read-only
    STATUS      current
    DESCRIPTION
        "Describes the antenna gain for connectorized version of the device.
        Measured in dBi."
    ::= { mimosaPtmpChannelPower 2 }

mimosaPtmpChannelPowerTable         OBJECT-TYPE
    SYNTAX      SEQUENCE OF MimosaPtmpChannelPowerEntry
    MAX-ACCESS  not-accessible
    STATUS      current
    DESCRIPTION
        "A list of Channel and Power related information per radio."
    ::= { mimosaPtmpChannelPower 3 }

mimosaPtmpChannelPowerEntry         OBJECT-TYPE
    SYNTAX      MimosaPtmpChannelPowerEntry
    MAX-ACCESS  not-accessible
    STATUS      current
    DESCRIPTION
        "An entry containing channel and power information"
    INDEX   { mimosaPtmpChPwrRadioIndex }
    ::= { mimosaPtmpChannelPowerTable 1 }

MimosaPtmpChannelPowerEntry ::=
    SEQUENCE {
        mimosaPtmpChPwrRadioIndex       Unsigned32,
        mimosaPtmpChPwrRadioName        DisplayString,
        mimosaPtmpChPwrCntrFreqCfg      Mimosa5GHzFrequency,
        mimosaPtmpChPwrPrimChannelCfg   Mimosa5GHzChannelNumber,
        mimosaPtmpChPwrChWidthCfg       Unsigned32,
        mimosaPtmpChPwrTxPowerCfg       Integer32,
        mimosaPtmpChPwrCntrFreqCur      Mimosa5GHzFrequency,
        mimosaPtmpChPwrPrimChannelCur   Mimosa5GHzChannelNumber,
        mimosaPtmpChPwrChWidthCur       Unsigned32,
        mimosaPtmpChPwrTxPowerCur       Integer32,
        mimosaPtmpChPwrAgcMode          INTEGER,
        mimosaPtmpChPwrMinRxPower       Integer32
    }

mimosaPtmpChPwrRadioIndex           OBJECT-TYPE
    SYNTAX      Unsigned32
    MAX-ACCESS  not-accessible
    STATUS      current
    DESCRIPTION
        "Describes the index of the radio."
    ::= { mimosaPtmpChannelPowerEntry 1 }

mimosaPtmpChPwrRadioName            OBJECT-TYPE
    SYNTAX      DisplayString (SIZE (1..32))
    MAX-ACCESS  read-only
    STATUS      current
    DESCRIPTION
        "Describes the name of the radio."
    ::= { mimosaPtmpChannelPowerEntry 2 }

mimosaPtmpChPwrCntrFreqCfg          OBJECT-TYPE
    SYNTAX      Mimosa5GHzFrequency
    MAX-ACCESS  read-only
    STATUS      current
    DESCRIPTION
        "Describes the configured center frequency of the channel used on the
         access point. The center frequency represents the absolute center
         of the selected channel width without any offset. Measured in MHz"
    ::= { mimosaPtmpChannelPowerEntry 3 }

mimosaPtmpChPwrPrimChannelCfg       OBJECT-TYPE
    SYNTAX      Mimosa5GHzChannelNumber
    MAX-ACCESS  read-only
    STATUS      current
    DESCRIPTION
        "Describes the primary channel number that corresponds with the
         operating frequency."
    ::= { mimosaPtmpChannelPowerEntry 4 }

mimosaPtmpChPwrChWidthCfg           OBJECT-TYPE
    SYNTAX      Unsigned32
    MAX-ACCESS  read-only
    STATUS      current
    DESCRIPTION
        "Describes the channel width for access point operation: 20 MHz,
         40 MHz or 80 MHz"
    ::= { mimosaPtmpChannelPowerEntry 5 }

mimosaPtmpChPwrTxPowerCfg           OBJECT-TYPE
    SYNTAX      Integer32
    MAX-ACCESS  read-only
    STATUS      current
    DESCRIPTION
        "Describes the desired transmit power level. The allowed options
         are determined by a combination of country and chosen frequency.
         Measured in dBm"
    ::= { mimosaPtmpChannelPowerEntry 6 }

mimosaPtmpChPwrCntrFreqCur          OBJECT-TYPE
    SYNTAX      Mimosa5GHzFrequency
    MAX-ACCESS  read-only
    STATUS      current
    DESCRIPTION
        "Describes the current center frequency of the channel used on the
         access point. The center frequency represents the absolute center
         of the selected channel width without any offset. Measured in MHz"
    ::= { mimosaPtmpChannelPowerEntry 7 }

mimosaPtmpChPwrPrimChannelCur       OBJECT-TYPE
    SYNTAX      Mimosa5GHzChannelNumber
    MAX-ACCESS  read-only
    STATUS      current
    DESCRIPTION
        "Describes the current primary channel number that corresponds with the
         operating frequency."
    ::= { mimosaPtmpChannelPowerEntry 8 }

mimosaPtmpChPwrChWidthCur           OBJECT-TYPE
    SYNTAX      Unsigned32
    MAX-ACCESS  read-only
    STATUS      current
    DESCRIPTION
        "Describes the current channel width for access point operation: 20 MHz,
         40 MHz or 80 MHz"
    ::= { mimosaPtmpChannelPowerEntry 9 }

mimosaPtmpChPwrTxPowerCur           OBJECT-TYPE
    SYNTAX      Integer32
    MAX-ACCESS  read-only
    STATUS      current
    DESCRIPTION
        "Describes the current transmit power level. The allowed options
         are determined by a combination of country and chosen frequency.
         Measured in dBm"
    ::= { mimosaPtmpChannelPowerEntry 10 }

mimosaPtmpChPwrAgcMode              OBJECT-TYPE
    SYNTAX      INTEGER {
                    off (0),
                    manual (1)
                }
    MAX-ACCESS  read-only
    STATUS      current
    DESCRIPTION
        "Describes the setting for Automatic Gain Control (AGC) feature,
        which is used to set the signal level below which the radio
        ignores incoming RF interference. The choices are Off or Manual"
    ::= { mimosaPtmpChannelPowerEntry 11 }

mimosaPtmpChPwrMinRxPower           OBJECT-TYPE
    SYNTAX      Integer32 (-90..-10)
    MAX-ACCESS  read-only
    STATUS      current
    DESCRIPTION
        "Describes the Rx power level (in manual AGC Mode) below your
        expected signal, but above other interference, measured in dBm"
    ::= { mimosaPtmpChannelPowerEntry 12 }

mimosaPtmpChannelExclusionTable     OBJECT-TYPE
    SYNTAX      SEQUENCE OF MimosaPtmpChannelExclusionEntry
    MAX-ACCESS  not-accessible
    STATUS      current
    DESCRIPTION
        "A list of Exclusions and Restrictions"
    ::= { mimosaPtmpChannelPower 4 }

mimosaPtmpChannelExclusionEntry     OBJECT-TYPE
    SYNTAX      MimosaPtmpChannelExclusionEntry
    MAX-ACCESS  not-accessible
    STATUS      current
    DESCRIPTION
        "Entry that describes each SSID and all its related configuration"
    INDEX   { mimosaPtmpChannelExclusionIndex }
    ::= { mimosaPtmpChannelExclusionTable 1 }

MimosaPtmpChannelExclusionEntry ::=
    SEQUENCE {
        mimosaPtmpChannelExclusionIndex     Integer32,
        mimosaPtmpChannelExclusionStart     Integer32,
        mimosaPtmpChannelExclusionEnd       Integer32
   }

mimosaPtmpChannelExclusionIndex     OBJECT-TYPE
    SYNTAX      Integer32 (1..16)
    MAX-ACCESS  not-accessible
    STATUS      current
    DESCRIPTION
        "Describes the index used to access a particular entry in the
        Exclusion list table."
    ::= { mimosaPtmpChannelExclusionEntry 1 }

mimosaPtmpChannelExclusionStart     OBJECT-TYPE
    SYNTAX      Integer32
    MAX-ACCESS  read-only
    STATUS      current
    DESCRIPTION
        "Describes the lower limit for the exclusion range, not including
        this frequency"
    ::= { mimosaPtmpChannelExclusionEntry 2 }

mimosaPtmpChannelExclusionEnd       OBJECT-TYPE
    SYNTAX      Integer32
    MAX-ACCESS  read-only
    STATUS      current
    DESCRIPTION
        "Describes the upper limit for the exclusion range, not including
         this frequency."
    ::= { mimosaPtmpChannelExclusionEntry 3 }


-- *************************************************************************
-- *** Mimosa Access Point Statistics                                    ***
-- *************************************************************************
mimosaPtmpApStatsRxBytes            OBJECT-TYPE
    SYNTAX      Counter64
    MAX-ACCESS  read-only
    STATUS      current
    DESCRIPTION
        "Describes the number of bytes received by the AP in single-User mode"
        ::= { mimosaPtmpApStats 1 }

mimosaPtmpApStatsTxBytes            OBJECT-TYPE
    SYNTAX      Counter64
    MAX-ACCESS  read-only
    STATUS      current
    DESCRIPTION
        "Describes the number of bytes transmitted by the AP in single-user
        mode"
        ::= { mimosaPtmpApStats 2 }

mimosaPtmpApStatsRxPkts             OBJECT-TYPE
    SYNTAX      Counter64
    MAX-ACCESS  read-only
    STATUS      current
    DESCRIPTION
        "Describes the number of packets received by the AP in single-user mode"
        ::= { mimosaPtmpApStats 3 }

mimosaPtmpApStatsTxPkts             OBJECT-TYPE
    SYNTAX      Counter64
    MAX-ACCESS  read-only
    STATUS      current
    DESCRIPTION
        "Describes the number of packets transmitted by the AP in
        single-user mode"
        ::= { mimosaPtmpApStats 4 }

mimosaPtmpApStatsTxPer              OBJECT-TYPE
    SYNTAX      Integer32
    MAX-ACCESS  read-only
    STATUS      current
    DESCRIPTION
        "Describes the packet error rate on the transmit path of the
        AP, in single-user mode"
        ::= { mimosaPtmpApStats 5 }

mimosaPtmpApStatsLastUpdated        OBJECT-TYPE
    SYNTAX      TimeStamp
    MAX-ACCESS  read-only
    STATUS      current
    DESCRIPTION
        "Describes the last updated time for these statistics"
        ::= { mimosaPtmpApStats 6 }


-- *************************************************************************
-- *** Mimosa Access Point Client Information                            ***
-- *************************************************************************

mimosaPtmpClientInfoTable           OBJECT-TYPE
    SYNTAX      SEQUENCE OF MimosaPtmpClientInfoEntry
    MAX-ACCESS  not-accessible
    STATUS      current
    DESCRIPTION
        "A list of all the associated clients and related information of
        each of them."
    ::= { mimosaPtmpClientInfo 1 }

mimosaPtmpClientInfoEntry           OBJECT-TYPE
    SYNTAX      MimosaPtmpClientInfoEntry
    MAX-ACCESS  not-accessible
    STATUS      current
    DESCRIPTION
        "Entry that describes each client and related configuration and
        statistics."
    INDEX   { mimosaPtmpClientInfoIndex }
    ::= { mimosaPtmpClientInfoTable 1 }

MimosaPtmpClientInfoEntry ::=
    SEQUENCE { mimosaPtmpClientInfoIndex        Unsigned32,
               mimosaPtmpClientInfoMacAddress   MacAddress,
               mimosaPtmpClientName             DisplayString,
               mimosaPtmpClientFWVersion        DisplayString,
               mimosaPtmpClientIPAddress        IpAddress,
               mimosaPtmpClientAssociatedTime   TimeStamp,
               mimosaPtmpClientPlanName         DisplayString,
               mimosaPtmpClientUlCommitted      Unsigned32,
               mimosaPtmpClientUlPeak           Unsigned32,
               mimosaPtmpClientDlCommitted      Unsigned32,
               mimosaPtmpClientDlPeak           Unsigned32,
               mimosaPtmpClientInfoLastUpdated  TimeStamp }

mimosaPtmpClientInfoIndex           OBJECT-TYPE
    SYNTAX      Unsigned32
    MAX-ACCESS  not-accessible
    STATUS      current
    DESCRIPTION
        "Describes the index used to access a particular entry in the
        Client Traffic Shaping Information table."
    ::= { mimosaPtmpClientInfoEntry 1 }

mimosaPtmpClientInfoMacAddress      OBJECT-TYPE
    SYNTAX      MacAddress
    MAX-ACCESS  read-only
    STATUS      current
    DESCRIPTION
        "Describes the MAC address of the client associated to this access-
        point."
    ::= { mimosaPtmpClientInfoEntry 2 }

mimosaPtmpClientName                OBJECT-TYPE
    SYNTAX      DisplayString (SIZE (1..64))
    MAX-ACCESS  read-only
    STATUS      current
    DESCRIPTION
        "Describes the name associated with this client."
    ::= { mimosaPtmpClientInfoEntry 3 }

mimosaPtmpClientFWVersion           OBJECT-TYPE
    SYNTAX      DisplayString (SIZE (1..64))
    MAX-ACCESS  read-only
    STATUS      current
    DESCRIPTION
        "Describes the firmware version of this client.

        This is supported only if the client is a Mimosa device."
    ::= { mimosaPtmpClientInfoEntry 4 }

mimosaPtmpClientIPAddress           OBJECT-TYPE
    SYNTAX      IpAddress
    MAX-ACCESS  read-only
    STATUS      current
    DESCRIPTION
        "Describes the IP Address associated with this client."
    ::= { mimosaPtmpClientInfoEntry 5 }

mimosaPtmpClientAssociatedTime      OBJECT-TYPE
    SYNTAX      TimeStamp
    MAX-ACCESS  read-only
    STATUS      current
    DESCRIPTION
        "Describes how long the client is associated with this access-point."
    ::= { mimosaPtmpClientInfoEntry 6 }

mimosaPtmpClientPlanName            OBJECT-TYPE
    SYNTAX      DisplayString
    MAX-ACCESS  read-only
    STATUS      current
    DESCRIPTION
        "Describes the Traffic Shaping plan associated with this client."
    ::= { mimosaPtmpClientInfoEntry 7 }

mimosaPtmpClientUlCommitted         OBJECT-TYPE
    SYNTAX      Unsigned32
    MAX-ACCESS  read-only
    STATUS      current
    DESCRIPTION
        "Describes the Uplink Committed Rate configured for the client."
    ::= { mimosaPtmpClientInfoEntry 8 }

mimosaPtmpClientUlPeak              OBJECT-TYPE
    SYNTAX      Unsigned32
    MAX-ACCESS  read-only
    STATUS      current
    DESCRIPTION
        "Describes the Uplink Peak Rate configured for the client."
    ::= { mimosaPtmpClientInfoEntry 9 }

mimosaPtmpClientDlCommitted         OBJECT-TYPE
    SYNTAX      Unsigned32
    MAX-ACCESS  read-only
    STATUS      current
    DESCRIPTION
        "Describes the Downlink Committed Rate configured for the client."
    ::= { mimosaPtmpClientInfoEntry 10 }

mimosaPtmpClientDlPeak              OBJECT-TYPE
    SYNTAX      Unsigned32
    MAX-ACCESS  read-only
    STATUS      current
    DESCRIPTION
        "Describes the Downlink Peak Rate configured for the client."
    ::= { mimosaPtmpClientInfoEntry 11 }

mimosaPtmpClientInfoLastUpdated     OBJECT-TYPE
    SYNTAX      TimeStamp
    MAX-ACCESS  read-only
    STATUS      current
    DESCRIPTION
        "Describes the last updated time of this information for the Client."
    ::= { mimosaPtmpClientInfoEntry 12 }


-- *************************************************************************
-- *** Mimosa Access Point Client Statistics                             ***
-- *************************************************************************

mimosaPtmpClientStatsTable          OBJECT-TYPE
    SYNTAX      SEQUENCE OF MimosaPtmpClientStatsEntry
    MAX-ACCESS  not-accessible
    STATUS      current
    DESCRIPTION
        "A list of all the associated clients and related information of each
         of them."

    ::= { mimosaPtmpClientStats 1 }

mimosaPtmpClientStatsEntry          OBJECT-TYPE
    SYNTAX      MimosaPtmpClientStatsEntry
    MAX-ACCESS  not-accessible
    STATUS      current
    DESCRIPTION
        "Entry that describes each client all its related configuration and
        statistics."
    INDEX   { mimosaPtmpClientStatsIndex }
    ::= { mimosaPtmpClientStatsTable 1 }

MimosaPtmpClientStatsEntry ::=
    SEQUENCE { mimosaPtmpClientStatsIndex           Unsigned32,
               mimosaPtmpClientStatsMacAddress      MacAddress,
               mimosaPtmpClientAssocBW              Unsigned32,
               mimosaPtmpClientRxBytes              Counter64,
               mimosaPtmpClientTxBytes              Counter64,
               mimosaPtmpClientRxPkts               Counter64,
               mimosaPtmpClientTxPkts               Counter64,
               mimosaPtmpClientRxPhyRate            Unsigned32,
               mimosaPtmpClientTxPhyRate            Unsigned32,
               mimosaPtmpClientTxAvgPer             DecimalTwo,
               mimosaPtmpClientRssiAvg              DecimalOne,
               mimosaPtmpClientStatsLastUpdated     TimeStamp,
               mimosaPtmpClientRssi1                DecimalOne,
               mimosaPtmpClientRssi2                DecimalOne,
               mimosaPtmpClientRssi3                DecimalOne,
               mimosaPtmpClientRssi4                DecimalOne,
               mimosaPtmpClientRxEVM1               DecimalOne,
               mimosaPtmpClientRxEVM2               DecimalOne,
               mimosaPtmpClientRxEVM3               DecimalOne,
               mimosaPtmpClientRxEVM4               DecimalOne,
               mimosaPtmpClientRxNss                Unsigned32,
               mimosaPtmpClientTxNss                Unsigned32,
               mimosaPtmpClientRxMcs                Unsigned32,
               mimosaPtmpClientTxMcs                Unsigned32,
               mimosaPtmpClientSNR                  DecimalOne
             }

mimosaPtmpClientStatsIndex          OBJECT-TYPE
    SYNTAX      Unsigned32
    MAX-ACCESS  not-accessible
    STATUS      current
    DESCRIPTION
        "Describes the index used to access a particular entry in the
        Client Information table."
    ::= { mimosaPtmpClientStatsEntry 1 }

mimosaPtmpClientStatsMacAddress          OBJECT-TYPE
    SYNTAX      MacAddress
    MAX-ACCESS  read-only
    STATUS      current
    DESCRIPTION
        "Describes the MAC address of the client associated to this access-
        point."
    ::= { mimosaPtmpClientStatsEntry 2 }

mimosaPtmpClientAssocBW             OBJECT-TYPE
    SYNTAX      Unsigned32
    MAX-ACCESS  read-only
    STATUS      current
    DESCRIPTION
        "Describes the associated bandwidth of the client."
    ::= { mimosaPtmpClientStatsEntry 3 }

mimosaPtmpClientRxBytes             OBJECT-TYPE
    SYNTAX      Counter64
    MAX-ACCESS  read-only
    STATUS      current
    DESCRIPTION
        "Describes the number of bytes received from this client."
    ::= { mimosaPtmpClientStatsEntry 4 }

mimosaPtmpClientTxBytes             OBJECT-TYPE
    SYNTAX      Counter64
    MAX-ACCESS  read-only
    STATUS      current
    DESCRIPTION
        "Describes the number of bytes transmitted to this client."
    ::= { mimosaPtmpClientStatsEntry 5 }

mimosaPtmpClientRxPkts              OBJECT-TYPE
    SYNTAX      Counter64
    MAX-ACCESS  read-only
    STATUS      current
    DESCRIPTION
        "Describes the number of packets received from this client."
    ::= { mimosaPtmpClientStatsEntry 6 }

mimosaPtmpClientTxPkts              OBJECT-TYPE
    SYNTAX      Counter64
    MAX-ACCESS  read-only
    STATUS      current
    DESCRIPTION
        "Describes the number of packets transmitted to this client."
    ::= { mimosaPtmpClientStatsEntry 7 }

mimosaPtmpClientRxPhyRate           OBJECT-TYPE
    SYNTAX      Unsigned32
    MAX-ACCESS  read-only
    STATUS      current
    DESCRIPTION
        "Describes the receive rate of this client."
    ::= { mimosaPtmpClientStatsEntry 8 }

mimosaPtmpClientTxPhyRate           OBJECT-TYPE
    SYNTAX      Unsigned32
    MAX-ACCESS  read-only
    STATUS      current
    DESCRIPTION
        "Describes the transmit rate of this client."
    ::= { mimosaPtmpClientStatsEntry 9 }

mimosaPtmpClientTxAvgPer            OBJECT-TYPE
    SYNTAX      DecimalTwo
    MAX-ACCESS  read-only
    STATUS      current
    DESCRIPTION
        "Describes the average packet error rate on the transmit side for
        this client."
    ::= { mimosaPtmpClientStatsEntry 10 }

mimosaPtmpClientRssiAvg             OBJECT-TYPE
    SYNTAX      DecimalOne
    MAX-ACCESS  read-only
    STATUS      current
    DESCRIPTION
        "Describes the average RSSI for this Client."
    ::= { mimosaPtmpClientStatsEntry 11 }

mimosaPtmpClientStatsLastUpdated         OBJECT-TYPE
    SYNTAX      TimeStamp
    MAX-ACCESS  read-only
    STATUS      current
    DESCRIPTION
        "Describes the last updated time of this information for the Client."
    ::= { mimosaPtmpClientStatsEntry 12 }

mimosaPtmpClientRssi1                       OBJECT-TYPE
    SYNTAX      DecimalOne
    MAX-ACCESS  read-only
    STATUS      current
    DESCRIPTION
        "Describes the RSSI of chain 1 for this Client. Measured in dBm"
    ::= { mimosaPtmpClientStatsEntry 13 }

mimosaPtmpClientRssi2                       OBJECT-TYPE
    SYNTAX      DecimalOne
    MAX-ACCESS  read-only
    STATUS      current
    DESCRIPTION
        "Describes the RSSI of chain 2 for this Client. Measured in dBm"
    ::= { mimosaPtmpClientStatsEntry 14 }

mimosaPtmpClientRssi3                       OBJECT-TYPE
    SYNTAX      DecimalOne
    MAX-ACCESS  read-only
    STATUS      current
    DESCRIPTION
        "Describes the RSSI of chain 3 for this Client. Measured in dBm"
    ::= { mimosaPtmpClientStatsEntry 15 }

mimosaPtmpClientRssi4                       OBJECT-TYPE
    SYNTAX      DecimalOne
    MAX-ACCESS  read-only
    STATUS      current
    DESCRIPTION
        "Describes the RSSI of chain 4 for this Client. Measured in dBm"
    ::= { mimosaPtmpClientStatsEntry 16 }

mimosaPtmpClientRxEVM1                        OBJECT-TYPE
    SYNTAX      DecimalOne
    MAX-ACCESS  read-only
    STATUS      current
    DESCRIPTION
        "Describes the RxEVM of stream 1 for this Client. Measured in dB"
    ::= { mimosaPtmpClientStatsEntry 17 }

mimosaPtmpClientRxEVM2                        OBJECT-TYPE
    SYNTAX      DecimalOne
    MAX-ACCESS  read-only
    STATUS      current
    DESCRIPTION
        "Describes the RxEVM of stream 2 for this Client. Measured in dB"
    ::= { mimosaPtmpClientStatsEntry 18 }

mimosaPtmpClientRxEVM3                       OBJECT-TYPE
    SYNTAX      DecimalOne
    MAX-ACCESS  read-only
    STATUS      current
    DESCRIPTION
        "Describes the RxEVM of stream 3 for this Client. Measured in dB"
    ::= { mimosaPtmpClientStatsEntry 19 }

mimosaPtmpClientRxEVM4                      OBJECT-TYPE
    SYNTAX      DecimalOne
    MAX-ACCESS  read-only
    STATUS      current
    DESCRIPTION
        "Describes the RxEVM of stream 4 for this Client. Measured in dB"
    ::= { mimosaPtmpClientStatsEntry 20 }

mimosaPtmpClientRxNss                        OBJECT-TYPE
    SYNTAX      Unsigned32
    MAX-ACCESS  read-only
    STATUS      current
    DESCRIPTION
        "Describes the for this Client."
    ::= { mimosaPtmpClientStatsEntry 21 }

mimosaPtmpClientTxNss                         OBJECT-TYPE
    SYNTAX      Unsigned32
    MAX-ACCESS  read-only
    STATUS      current
    DESCRIPTION
        "Describes the for this Client."
    ::= { mimosaPtmpClientStatsEntry 22 }

mimosaPtmpClientRxMcs                         OBJECT-TYPE
    SYNTAX      Unsigned32
    MAX-ACCESS  read-only
    STATUS      current
    DESCRIPTION
        "Describes the  for this Client."
    ::= { mimosaPtmpClientStatsEntry 23 }

mimosaPtmpClientTxMcs                          OBJECT-TYPE
    SYNTAX      Unsigned32
    MAX-ACCESS  read-only
    STATUS      current
    DESCRIPTION
        "Describes the  for this Client."
    ::= { mimosaPtmpClientStatsEntry 24 }

mimosaPtmpClientSNR                            OBJECT-TYPE
    SYNTAX      DecimalOne
    MAX-ACCESS  read-only
    STATUS      current
    DESCRIPTION
        "Describes the SNR for this Client."
    ::= { mimosaPtmpClientStatsEntry 25 }

-- *************************************************************************
-- *** Mimosa PTMP Management Information variables are specified below. ***
-- *************************************************************************

mimosaPtmpMgmtIpAddress             OBJECT-TYPE
    SYNTAX      IpAddress
    MAX-ACCESS  read-only
    STATUS      current
    DESCRIPTION
        "Describes the IP Address configured on the Mimosa Device"
    ::= { mimosaPtmpMgmtInfo 1 }

mimosaPtmpMgmtIpNetmask             OBJECT-TYPE
    SYNTAX      IpAddress
    MAX-ACCESS  read-only
    STATUS      current
    DESCRIPTION
        "Describes the IP netmask configured on the Mimosa Device"
    ::= { mimosaPtmpMgmtInfo 2 }

mimosaPtmpMgmtIpGateway             OBJECT-TYPE
    SYNTAX      IpAddress
    MAX-ACCESS  read-only
    STATUS      current
    DESCRIPTION
        "Describes the IP Address of the Gateway configured on the Mimosa
        Device"
    ::= { mimosaPtmpMgmtInfo 3 }

mimosaPtmpMgmtIpMode                OBJECT-TYPE
    SYNTAX      DisplayString (SIZE (4..6))
    MAX-ACCESS  read-only
    STATUS      current
    DESCRIPTION
        "Describes the IP Address assignment mode configured on the Mimosa
        Device"
    ::= { mimosaPtmpMgmtInfo 4 }

mimosaPtmpMgmtPrimaryDNS            OBJECT-TYPE
    SYNTAX      IpAddress
    MAX-ACCESS  read-only
    STATUS      current
    DESCRIPTION
        "Describes the IP Address of the Primary DNS server configured on the
        Mimosa Device"
    ::= { mimosaPtmpMgmtInfo 5 }

mimosaPtmpMgmtSecondaryDNS          OBJECT-TYPE
    SYNTAX      IpAddress
    MAX-ACCESS  read-only
    STATUS      current
    DESCRIPTION
        "Describes the IP Address of the Secondary DNS server configured on the
        Mimosa Device"
    ::= { mimosaPtmpMgmtInfo 6 }

mimosaPtmpMgmtVlanStatus            OBJECT-TYPE
    SYNTAX      INTEGER {
                    disable (0),
                    enable (1)
                }
    MAX-ACCESS  read-only
    STATUS      current
    DESCRIPTION
        "Describes the status of management vlan configured on the Mimosa Device"
    ::= { mimosaPtmpMgmtInfo 7 }

mimosaPtmpMgmtVlanId                OBJECT-TYPE
    SYNTAX      Integer32 
    MAX-ACCESS  read-only
    STATUS      current
    DESCRIPTION
        "Describes the management vlan-id configured on the Mimosa Device"
    ::= { mimosaPtmpMgmtInfo 8 }

mimosaPtmpMgmtVlanPassthrough       OBJECT-TYPE
    SYNTAX      INTEGER {
                    disable (0),
                    enable (1)
                }
    MAX-ACCESS  read-only
    STATUS      current
    DESCRIPTION
        "Describes the status of the vlan passthrough configured on the Mimosa Device"
    ::= { mimosaPtmpMgmtInfo 9 }

mimosaPtmpMgmtEthernetMac           OBJECT-TYPE
    SYNTAX      MacAddress 
    MAX-ACCESS  read-only
    STATUS      current
    DESCRIPTION
        "Describes the Ethernet MAC address configured on the Mimosa Device"
    ::= { mimosaPtmpMgmtInfo 10 }

---
---  Conformance/Compliance Statements
---
mimosaPtmpConformance         OBJECT IDENTIFIER ::= { mimosaConformanceGroup 2 }

mimosaPtmpCompliances         OBJECT IDENTIFIER ::= { mimosaPtmpConformance 1 }
mimosaPtmpGroups              OBJECT IDENTIFIER ::= { mimosaPtmpConformance 2 }


mimosaPtmpCompliance      MODULE-COMPLIANCE
    STATUS      current
    DESCRIPTION
        "The compliance statement for PTMP supported Access Points that
        implement this MIB."
    MODULE
        GROUP mimosaPtmpSsidGroup
        DESCRIPTION
            "The mimosaPtmpSsidGroup is mandatory only for access-point device
            supporting PTMP."

        GROUP mimosaPtmpLinkInfoGroup
        DESCRIPTION
            "The mimosaPtmpLinkInfoGroup is mandatory only for access-point
            device supporting PTMP."

        GROUP mimosaPtmpChannelPowerGroup
        DESCRIPTION
            "The mimosaPtmpChannelPowerGroup is mandatory only for access-point
            device supporting PTMP."

        GROUP mimosaPtmpApStatsGroup
        DESCRIPTION
            "The mimosaPtmpApStatsGroup is mandatory only for access-point
            device supporting PTMP."

        GROUP mimosaPtmpClientStatsGroup
        DESCRIPTION
            "The mimosaPtmpClientStatsGroup is mandatory only for access-point
            device supporting PTMP."

        GROUP mimosaPtmpClientInfoGroup
        DESCRIPTION
            "The mimosaPtmpClientInfoGroup is mandatory only for access-point
            device supporting PTMP."

        GROUP mimosaPtmpMgmtInfoGroup
        DESCRIPTION
            "The mimosaPtmpMgmtInfoGroup is mandatory only for access-point
            device supporting PTMP."
    ::= { mimosaPtmpCompliances 1 }


mimosaPtmpSsidGroup                 OBJECT-GROUP
    OBJECTS {
            mimosaPtmpSsidName,
            mimosaPtmpSsidType,
            mimosaPtmpSsidEnabled,
            mimosaPtmpSsidBroadcastEnabled,
            mimosaPtmpSsidIsolationEnabled
    }
    STATUS      current
    DESCRIPTION
        "A collection of objects for the SSID Table."
    ::= { mimosaPtmpGroups 1 }

mimosaPtmpLinkInfoGroup             OBJECT-GROUP
    OBJECTS {
            mimosaPtmpWirelessMode,
            mimosaPtmpWirelessGender,
            mimosaPtmpWirelessTrafficSplit,
            mimosaPtmpWirelessWindowLength
    }
    STATUS      current
    DESCRIPTION
        "A collection of objects for the wireless link objects."
    ::= { mimosaPtmpGroups 2 }

mimosaPtmpChannelPowerGroup         OBJECT-GROUP
    OBJECTS {
            mimosaPtmpAutoChannelEnabled,
            mimosaPtmpAntennaGain,
            mimosaPtmpChPwrRadioName,
            mimosaPtmpChPwrCntrFreqCfg,
            mimosaPtmpChPwrPrimChannelCfg,
            mimosaPtmpChPwrChWidthCfg,
            mimosaPtmpChPwrTxPowerCfg,
            mimosaPtmpChPwrCntrFreqCur,
            mimosaPtmpChPwrPrimChannelCur,
            mimosaPtmpChPwrChWidthCur,
            mimosaPtmpChPwrTxPowerCur,
            mimosaPtmpChPwrAgcMode,
            mimosaPtmpChPwrMinRxPower,
            mimosaPtmpChannelExclusionStart,
            mimosaPtmpChannelExclusionEnd
    }
    STATUS      current
    DESCRIPTION
        "A collection of objects for the wireless channel and power settings."
    ::= { mimosaPtmpGroups 3 }

mimosaPtmpApStatsGroup              OBJECT-GROUP
    OBJECTS {
            mimosaPtmpApStatsRxBytes,
            mimosaPtmpApStatsTxBytes,
            mimosaPtmpApStatsRxPkts,
            mimosaPtmpApStatsTxPkts,
            mimosaPtmpApStatsTxPer,
            mimosaPtmpApStatsLastUpdated
    }
    STATUS      current
    DESCRIPTION
        "A collection of objects describing the AP related statistics."
    ::= { mimosaPtmpGroups 4 }

mimosaPtmpClientInfoGroup           OBJECT-GROUP
    OBJECTS {
            mimosaPtmpClientName,
            mimosaPtmpClientFWVersion,
            mimosaPtmpClientIPAddress,
            mimosaPtmpClientAssociatedTime,
            mimosaPtmpClientPlanName,
            mimosaPtmpClientUlCommitted,
            mimosaPtmpClientUlPeak,
            mimosaPtmpClientDlCommitted,
            mimosaPtmpClientDlPeak,
            mimosaPtmpClientInfoLastUpdated
    }
    STATUS      current
    DESCRIPTION
        "A collection of objects describing the client details."
    ::= { mimosaPtmpGroups 5 }
    
mimosaPtmpClientStatsGroup          OBJECT-GROUP
    OBJECTS {
            mimosaPtmpClientStatsMacAddress,
            mimosaPtmpClientAssocBW,
            mimosaPtmpClientRxBytes,
            mimosaPtmpClientRxPkts,
            mimosaPtmpClientTxPkts,
            mimosaPtmpClientRssiAvg,
            mimosaPtmpClientRxPhyRate,
            mimosaPtmpClientTxAvgPer,
            mimosaPtmpClientTxPhyRate,
            mimosaPtmpClientTxBytes,
            mimosaPtmpClientStatsLastUpdated,
            mimosaPtmpClientRssi1,
            mimosaPtmpClientRssi2,
            mimosaPtmpClientRssi3,
            mimosaPtmpClientRssi4,
            mimosaPtmpClientRxEVM1,
            mimosaPtmpClientRxEVM2,
            mimosaPtmpClientRxEVM3,
            mimosaPtmpClientRxEVM4,
            mimosaPtmpClientRxNss,
            mimosaPtmpClientTxNss,
            mimosaPtmpClientRxMcs,
            mimosaPtmpClientTxMcs
    }
    STATUS      current
    DESCRIPTION
        "A collection of objects describing the client statistics."
    ::= { mimosaPtmpGroups 6 }

mimosaPtmpMgmtInfoGroup             OBJECT-GROUP
    OBJECTS {
            mimosaPtmpMgmtIpAddress,
            mimosaPtmpMgmtIpNetmask,
            mimosaPtmpMgmtIpGateway,
            mimosaPtmpMgmtIpMode,
            mimosaPtmpMgmtPrimaryDNS,
            mimosaPtmpMgmtSecondaryDNS,
            mimosaPtmpMgmtVlanStatus,
            mimosaPtmpMgmtVlanId,
            mimosaPtmpMgmtVlanPassthrough,
            mimosaPtmpMgmtEthernetMac
    }
    STATUS      current
    DESCRIPTION
        "A collection of objects describing the client details."
    ::= { mimosaPtmpGroups 7 }

END



File: /dude_custom_files\MIMOSA-MIB-TC.txt
MIMOSA-MIB-TC DEFINITIONS ::= BEGIN

--  Copyright (C) 2017, Mimosa Networks, Inc. All Rights Reserved.
--
--  Mimosa Networks MIB
--  Revision: 1.00
--  Date: February 15, 2017
--
--  Mimosa Networks, Inc.
--  469 El Camino Real, Suite 100
--  Santa Clara, CA 95050
--  support@mimosa.co
--
--  This MIB defines the base MIB specification for Mimosa Network's
--  products.
--
--  Mimosa reserves the right to make changes to this MIB specification as
--  well as other information related to this specification without prior
--  notice.  The user of this specification should consult Mimosa Networks,
--  to determine if any such changes have been made.
--
--  Current MIBs are available from Mimosa Networks at the following URLs:
--
--      http://help.mimosa.co
--
--  In no event shall Mimosa Networks, Inc. be liable for any indirect,
--  consequential, special or incidental damages whatsoever (including
--  but not limited to lost profits or lost revenue) arising out of or
--  related to this specification or the information contained in it.
--  This non-liability extends to even if Mimosa Networks Inc. has been
--  advised of, known, or should have known, the potential for such damages.
--  Mimosa Networks, Inc. hereby grants end-users, and other parties a                                                                                         
--  a non-exclusive license to use this MIB specification in order to
--  manage products of Mimosa Networks, Inc.

IMPORTS
    MODULE-IDENTITY, Integer32              FROM SNMPv2-SMI
    TEXTUAL-CONVENTION                      FROM SNMPv2-TC
    mimosa                                  FROM MIMOSA-NETWORKS-BASE-MIB;

mimosaMibTC     MODULE-IDENTITY
    LAST-UPDATED    "201702150000Z"
    ORGANIZATION "Mimosa Networks
    			  www.mimosa.co"
    CONTACT-INFO
    	"postal:
    	Mimosa Networks, Inc.
		469 El Camino Real, Suite 100
		Santa Clara, CA 95050
        email: support@mimosa.co"
    DESCRIPTION
		"Mimosa device MIB definitions"
	REVISION	"201702150000Z"
    DESCRIPTION
		"First Revision of Textual Conventions defined for MIMOSA-MIB modules."
    ::= { mimosa 3 }

-- *****************************************************************
-- ***                   Mimosa Textual Conventions              ***
-- *****************************************************************

DecimalOne ::= TEXTUAL-CONVENTION
    DISPLAY-HINT "d-1"
    STATUS       current
    DESCRIPTION  "Fixed point, one decimal"
    SYNTAX       Integer32

DecimalTwo ::= TEXTUAL-CONVENTION
    DISPLAY-HINT "d-2"
    STATUS       current
    DESCRIPTION  "Fixed point, two decimals"
    SYNTAX       Integer32

DecimalFive ::= TEXTUAL-CONVENTION
    DISPLAY-HINT "d-5"
    STATUS       current
    DESCRIPTION  "Fixed point, five decimals"
    SYNTAX       Integer32

Mimosa5GHzFrequency ::= TEXTUAL-CONVENTION
    STATUS       current
    DESCRIPTION  "Represents the frequency in the range of 4800 to 6200"
    SYNTAX       Integer32 (4800..6200)

Mimosa5GHzChannelNumber ::= TEXTUAL-CONVENTION
    STATUS       current
    DESCRIPTION  "Reprensents the channel Wifi ChannelWidth"
    SYNTAX       Integer32

END


File: /dude_custom_files\MIMOSA-MIB.txt
MIMOSA-NETWORKS-BASE-MIB DEFINITIONS ::= BEGIN

--  Copyright (C) 2015, Mimosa Networks, Inc. All Rights Reserved.
--
--  Mimosa Networks MIB
--  Revision: 1.00
--  Date: June 03, 2015
--
--  Mimosa Networks, Inc.
--  300 Orchard City Dr.
--  Campbell, CA 95008
--  support@mimosa.co
--
--  This MIB defines the base MIB specification for Mimosa Network's
--  products.
--
--  Mimosa reserves the right to make changes to this MIB specification as
--  well as other information related to this specification without prior
--  notice.  The user of this specification should consult Mimosa Networks,
--  to determine if any such changes have been made.
--
--  Current MIBs are available from Mimosa Networks at the following URLs:
--
--		http://help.mimosa.co
--
--  In no event shall Mimosa Networks, Inc. be liable for any indirect,
--  consequential, special or incidental damages whatsoever (including
--  but not limited to lost profits or lost revenue) arising out of or
--  related to this specification or the information contained in it.
--  This non-liability extends to even if Mimosa Networks Inc. has been
--  advised of, known, or should have known, the potential for such damages.

--  Mimosa Networks, Inc. hereby grants end-users, and other parties a
--  a non-exclusive license to use this MIB specification in order to
--  manage products of Mimosa Networks, Inc.

IMPORTS
    MODULE-IDENTITY, OBJECT-TYPE, Integer32,
    NOTIFICATION-TYPE            			FROM SNMPv2-SMI
    OBJECT-GROUP, NOTIFICATION-GROUP		FROM SNMPv2-CONF
    enterprises				     			FROM RFC1155-SMI 
    ifIndex						 			FROM IF-MIB;


-- EXPORTS mimosa...
mimosa MODULE-IDENTITY
    LAST-UPDATED "201506030000Z"
    ORGANIZATION "Mimosa Networks
    			  www.mimosa.co"
    CONTACT-INFO
    	"postal:
    	Mimosa Networks, Inc.
		300 Orchard City Dr.
		Campbell, CA 95008
        email: support@mimosa.co"
    DESCRIPTION
		"Mimosa device MIB definitions"
	REVISION	"201506030000Z"
    DESCRIPTION
		"First draft"
    ::= { enterprises 43356 }
    
--mimosa                        OBJECT IDENTIFIER ::= { enterprises 43356 }

mimosaProduct                 OBJECT IDENTIFIER ::= { mimosa 1 }
mimosaMgmt                    OBJECT IDENTIFIER ::= { mimosa 2 }


mimosaHardware                OBJECT IDENTIFIER ::= { mimosaProduct 1 }
mimosaSoftware                OBJECT IDENTIFIER ::= { mimosaProduct 2 }

mimosaB5                      OBJECT IDENTIFIER ::= { mimosaHardware 1 }
mimosaB5Lite                  OBJECT IDENTIFIER ::= { mimosaHardware 2 }
mimosaA5                      OBJECT IDENTIFIER ::= { mimosaHardware 3 }
mimosaC5                      OBJECT IDENTIFIER ::= { mimosaHardware 4 }

mimosaTrap                    OBJECT IDENTIFIER ::= { mimosaMgmt 0 }
mimosaMib                     OBJECT IDENTIFIER ::= { mimosaMgmt 1 }
mimosaMIBGroups               OBJECT IDENTIFIER ::= { mimosaMgmt 3 }
mimosaConformanceGroup        OBJECT IDENTIFIER ::= { mimosaMgmt 4 }

mimosaTrapMib                 OBJECT IDENTIFIER ::= { mimosaMib 1 }
mimosaWireless                OBJECT IDENTIFIER ::= { mimosaMib 2 }


-- **********************************************************************
-- ***       Mimosa General MIB variables are specified below.        ***
-- ***       These varbinds are common to all Mimosa products.        ***
-- **********************************************************************

mimosaTrapMIBGroup OBJECT-GROUP
    OBJECTS { mimosaTrapMessage,
              mimosaOldSpeed,
              mimosaNewSpeed
            }
    STATUS  current
    DESCRIPTION
            "A collection of objects providing basic Trap function."
    ::= { mimosaMIBGroups 1 }


mimosaTrapMessage OBJECT-TYPE
    SYNTAX OCTET STRING
    MAX-ACCESS read-only
    STATUS current
    DESCRIPTION
        "General Octet String object to contain message sent with traps."
    ::= { mimosaTrapMib 1 }

mimosaOldSpeed OBJECT-TYPE
    SYNTAX      Integer32
    MAX-ACCESS  read-only
    STATUS      current
    DESCRIPTION
        "The speed of the Ethernet link before the change within Ethernet
         Speed Change Notifications."
    ::= { mimosaTrapMib 2 }

mimosaNewSpeed OBJECT-TYPE
    SYNTAX      Integer32
    MAX-ACCESS  read-only
    STATUS      current
    DESCRIPTION
        "The speed of the Ethernet link after the change within Ethernet
         Speed Change Notifications."
    ::= { mimosaTrapMib 3 }


-- **********************************************************************
-- ***       Mimosa Generic Traps are specified below.                ***
-- ***       These traps are common to all Mimosa products.           ***
-- **********************************************************************

mimosaGenericNotificationsGroup NOTIFICATION-GROUP
    NOTIFICATIONS { mimosaCriticalFault, mimosaTempWarning,
    				mimosaTempNormal, mimosaEthernetSpeedChange }
    STATUS        current
    DESCRIPTION
       "The basic Trap notifications for all Mimosa products."
    ::= { mimosaMIBGroups 2 }


mimosaCriticalFault NOTIFICATION-TYPE
    OBJECTS { mimosaTrapMessage }
    STATUS current
    DESCRIPTION
        "The mimosaCriticalFault notification is sent when the log manager
         in the Mimosa product determines that a fault with a critical
         severity has been detected. The mimosaCriticalFaultLog contains
         the description of the general error."
    ::= {mimosaTrap 1 }

mimosaTempWarning NOTIFICATION-TYPE
    OBJECTS { mimosaTrapMessage }
    STATUS current
    DESCRIPTION
        "The mimosaTempWarning notification is sent when the log manager in
         the Mimosa product receives an indication that the temperature is
         outside the safe range."
    ::= {mimosaTrap 2 }

mimosaTempNormal NOTIFICATION-TYPE
    OBJECTS { mimosaTrapMessage }
    STATUS current
    DESCRIPTION
        "The mimosaTempNormal notification is sent when the log manager in the
         Mimosa product receives an indication that the temperature is with
         in the safe range."
    ::= {mimosaTrap 3 }

mimosaEthernetSpeedChange NOTIFICATION-TYPE
    OBJECTS  { ifIndex, mimosaOldSpeed, mimosaNewSpeed }
    STATUS   current
    DESCRIPTION
        "The mimosaEthernetSpeedChange notification is sent when the log manager
         in the Mimosa product determines that a speed change on the Ethernet
         port was detected. The mimosaOldSpeed and mimosaNewSpeed indicates the
         speed in bits per second of the change. ifIndex is used per the ifTable
         in the IF-MIB."
    ::= {mimosaTrap 4 }

-- Note the following publicly defined traps are also used for Mimosa Product
-- Notifications:
--
-- From SNMPv2-MIB:	coldStart, warmStart, linkUp, LinkDown and
--                      authenticationFailure
END



File: /dude_custom_files\UBNT-AirFIBER-MIB.txt
UBNT-AirFIBER-MIB DEFINITIONS ::= BEGIN
    IMPORTS
        MODULE-IDENTITY, OBJECT-TYPE, Integer32, Counter64, 
        IpAddress FROM SNMPv2-SMI
        DisplayString, TruthValue, MacAddress FROM SNMPv2-TC
        OBJECT-GROUP FROM SNMPv2-CONF
        ubntMIB FROM UBNT-MIB;


    ubntAirFIBER MODULE-IDENTITY
    LAST-UPDATED "201405270000Z"
    ORGANIZATION "Ubiquiti Networks, Inc."
    CONTACT-INFO "support@ubnt.com"
    DESCRIPTION  "The AirFIBER MIB module for Ubiquiti Networks, Inc. entities"
    REVISION "201405090000Z"
    DESCRIPTION "ubntAirFIBER revision"
    ::= { ubntMIB 3 }

    -- --------------------------------------------------------------------------------
    --                           AirFiber Config Table
    -- --------------------------------------------------------------------------------


    airFiberConfig OBJECT-TYPE
        SYNTAX     SEQUENCE OF AirFiberConfigEntry
        MAX-ACCESS not-accessible
        STATUS     current
        DESCRIPTION "AirFiber Configuration Group"
        ::= { ubntAirFIBER 1 }


    airFiberConfigEntry OBJECT-TYPE
       SYNTAX     AirFiberConfigEntry
       MAX-ACCESS not-accessible
       STATUS     current
       DESCRIPTION "An entry in the airFiberConfig Table"
       INDEX      { airFiberConfigIndex }
       ::= { airFiberConfig 1 }


    AirFiberConfigEntry ::= SEQUENCE {
    airFiberConfigIndex Integer32,
    radioEnable         Integer32,
    radioLinkMode       Integer32,
    radioDuplex         Integer32,
    txFrequency         Integer32,
    rxFrequency         Integer32,
    regDomain           Integer32,
    gpsSync             Integer32,
    txPower             Integer32,
    rxGain              Integer32,
    maxTxModRate        Integer32,
    modRateControl      Integer32,
    ethDPortLinkSpeed   Integer32,
    linkName            DisplayString,
    encryptKey          DisplayString,
    ethFlowControl      Integer32,
    ethMcastFilter      Integer32,
    ethTrackRFLink      Integer32,
    ethLinkOffDuration  Integer32,
    ethLinkOffSpacing   Integer32,
    txFrequency1        Integer32,
    rxFrequency1        Integer32,
    txFrequency2        Integer32,
    rxFrequency2        Integer32,
    txFrequency3        Integer32,
    rxFrequency3        Integer32,
    channelWidth        Integer32,
    txChannelWidth      Integer32,
    rxChannelWidth      Integer32
    }


    airFiberConfigIndex OBJECT-TYPE
        SYNTAX     Integer32 (1..255)
        MAX-ACCESS not-accessible
        STATUS     current
        DESCRIPTION "Index for the airFiberConfig"
        ::= { airFiberConfigEntry 1 }

    radioEnable OBJECT-TYPE
        SYNTAX     Integer32 {
                enabled   (1),
                eisabled  (2)
        } 
        MAX-ACCESS read-only
        STATUS current
        DESCRIPTION "Radio Enabled State (Enabled/Disabled)"
        ::= { airFiberConfigEntry 2 }

   radioLinkMode OBJECT-TYPE
        SYNTAX     Integer32 {
                master (1),
                slave  (2),
                spectral (3)
        } 
        MAX-ACCESS read-only
        STATUS     current
        DESCRIPTION "Radio Operating Mode"
        ::= { airFiberConfigEntry 3 }

    radioDuplex OBJECT-TYPE
        SYNTAX     Integer32 {
                halfDuplex (1),
                fullDuplex (2)
        } 
        MAX-ACCESS read-only
        STATUS     current
        DESCRIPTION "Radio Duplex Mode"
        ::= { airFiberConfigEntry 4 }

    txFrequency OBJECT-TYPE
        SYNTAX Integer32
        MAX-ACCESS read-only
        STATUS current
        DESCRIPTION "TX Operating frequency (MHz)"
        ::= { airFiberConfigEntry 5 }

    rxFrequency OBJECT-TYPE
        SYNTAX Integer32
        MAX-ACCESS read-only
        STATUS current
        DESCRIPTION "RX Operating frequency (MHz)"
        ::= { airFiberConfigEntry 6 }

    regDomain OBJECT-TYPE
        SYNTAX     DisplayString
        MAX-ACCESS read-only
        STATUS     current
        DESCRIPTION "Regulatory Domain"
        ::= { airFiberConfigEntry 7 }

    gpsSync OBJECT-TYPE
        SYNTAX     Integer32 {
                off (1),
                on  (2)
        } 
        MAX-ACCESS read-only
        STATUS current
        DESCRIPTION "GPS Synchronization state (OFF, ON)"
        ::= { airFiberConfigEntry 8 }
        
    txPower OBJECT-TYPE
        SYNTAX Integer32
        MAX-ACCESS read-only
        STATUS current
        DESCRIPTION "Radio Transmit Power Setting (dBm)"
        ::= { airFiberConfigEntry 9 }

    rxGain OBJECT-TYPE
        SYNTAX     Integer32 {
                low  (1),
                high (2)
        } 
        MAX-ACCESS read-only
        STATUS     current
        DESCRIPTION "Radio Receiver Gain Setting"
        ::= { airFiberConfigEntry 10 }

    maxTxModRate OBJECT-TYPE
        SYNTAX     Integer32 {
            qPSK-SISO-1-4x (0),
            qPSK-SISO-1x   (1),
            qPSK-MIMO-2x   (2),
            qAM16-MIMO-4x  (4),
            qAM64-MIMO-6x  (6),
            qAM256-MIMO-8x (8)
        } 
        MAX-ACCESS read-only
        STATUS     current
        DESCRIPTION "Maximum TX Modulation Rate"
        ::= { airFiberConfigEntry 11 }

    modRateControl OBJECT-TYPE
        SYNTAX     Integer32 {
                manual    (1),
                automatic (2)
        }
        MAX-ACCESS read-only
        STATUS current
        DESCRIPTION "Transmit Modulation Rate Control"
        ::= { airFiberConfigEntry 12 }

    ethDPortLinkSpeed OBJECT-TYPE
        SYNTAX     Integer32 {
            auto          (1),
            half-10Mbps   (2),
            half-100Mbps  (3),
            full-10Mbps   (4),
            full-100Mbps  (5),
            full-1000Mbps (6)
        } 
        MAX-ACCESS read-only
        STATUS     current
        DESCRIPTION "Ethernet Data Port Configuration"
        ::= { airFiberConfigEntry 13 }

    linkName OBJECT-TYPE
        SYNTAX     DisplayString
        MAX-ACCESS read-only
        STATUS     current
        DESCRIPTION "Radio Link Name"
        ::= { airFiberConfigEntry 14 }

    encryptKey OBJECT-TYPE
        SYNTAX     DisplayString
        MAX-ACCESS read-only
        STATUS     obsolete
        DESCRIPTION "Radio Link Encryption Key"
        ::= { airFiberConfigEntry 15 }

    ethFlowControl OBJECT-TYPE
        SYNTAX     Integer32 {
                off (1),
                on  (2)
        }         
        MAX-ACCESS read-only
        STATUS current
        DESCRIPTION "Ethernet DATA port Flow Control (OFF, ON)"
        ::= { airFiberConfigEntry 16 }
   
    ethMcastFilter OBJECT-TYPE
        SYNTAX     Integer32 {
                off (1),
                on  (2)
        }         
        MAX-ACCESS read-only
        STATUS current
        DESCRIPTION "Ethernet DATA port Multicast Filter.  Enabling Filter prevents all multicast packets from reaching the CPU."
        ::= { airFiberConfigEntry 17 }

    ethTrackRFLink OBJECT-TYPE
        SYNTAX     Integer32 {
                disabled (0),
                use-Timers (1),
                enabled  (2)
        }         
        MAX-ACCESS read-only
        STATUS current
        DESCRIPTION "Enable Ethernet DATA port state to track RF Link.  Enabled forces DATA port to follow RF Link State. Use-Timers drops Data Port for timeout period"
        ::= { airFiberConfigEntry 18 }

    ethLinkOffDuration OBJECT-TYPE
        SYNTAX Integer32
        MAX-ACCESS read-only
        STATUS current
        DESCRIPTION "Duration (seconds) of Ethernet Link Drop when ethTrackRFLink is set to Use-Timers"
        ::= { airFiberConfigEntry 19 }

    ethLinkOffSpacing OBJECT-TYPE
        SYNTAX Integer32
        MAX-ACCESS read-only
        STATUS current
        DESCRIPTION "Spacing (seconds) of consecutive Etherenet Link Drops when ethTrackLink is set to Use-Timers"
        ::= { airFiberConfigEntry 20 }
        
    txFrequency1 OBJECT-TYPE
        SYNTAX Integer32
        MAX-ACCESS read-only
        STATUS current
        DESCRIPTION "First configured TX Frequency (MHz) of radio."
        ::= { airFiberConfigEntry 21 }

    rxFrequency1 OBJECT-TYPE
        SYNTAX Integer32
        MAX-ACCESS read-only
        STATUS current
        DESCRIPTION "First configured RX Frequency (MHz) of radio."
        ::= { airFiberConfigEntry 22 }

    txFrequency2 OBJECT-TYPE
        SYNTAX Integer32
        MAX-ACCESS read-only
        STATUS current
        DESCRIPTION "Second configured TX Frequency (MHz) of radio. 5 GHz radios only."
        ::= { airFiberConfigEntry 23 }

    rxFrequency2 OBJECT-TYPE
        SYNTAX Integer32
        MAX-ACCESS read-only
        STATUS current
        DESCRIPTION "Second configured RX Frequency (MHz) of radio.  5 GHz radios only."
        ::= { airFiberConfigEntry 24 }

    txFrequency3 OBJECT-TYPE
        SYNTAX Integer32
        MAX-ACCESS read-only
        STATUS current
        DESCRIPTION "Third configured TX Frequency (MHz) of radio. 5 GHz radios only."
        ::= { airFiberConfigEntry 25 }

    rxFrequency3 OBJECT-TYPE
        SYNTAX Integer32
        MAX-ACCESS read-only
        STATUS current
        DESCRIPTION "Third configured RX Frequency (MHz) of radio.  5 GHz radios only."
        ::= { airFiberConfigEntry 26 }

    channelWidth OBJECT-TYPE
        SYNTAX Integer32
        MAX-ACCESS read-only
        STATUS obsolete
        DESCRIPTION "Current RF Channel Bandwidth.  5 GHz radios only."
        ::= { airFiberConfigEntry 27 }

    txChannelWidth OBJECT-TYPE
        SYNTAX Integer32
        MAX-ACCESS read-only
        STATUS current
        DESCRIPTION "Current TX RF Channel Bandwidth (MHz).  5 GHz radios only."
        ::= { airFiberConfigEntry 28 }

    rxChannelWidth OBJECT-TYPE
        SYNTAX Integer32
        MAX-ACCESS read-only
        STATUS current
        DESCRIPTION "Current RX RF Channel Bandwidth (MHz).  5 GHz radios only."
        ::= { airFiberConfigEntry 29 }

    -- --------------------------------------------------------------------------------
    --                           AirFiber Status Table
    -- --------------------------------------------------------------------------------


    airFiberStatus OBJECT-TYPE
        SYNTAX     SEQUENCE OF AirFiberStatusEntry
        MAX-ACCESS not-accessible
        STATUS     current
        DESCRIPTION "AirFiber Status Group"
        ::= { ubntAirFIBER 2 }


    airFiberStatusEntry OBJECT-TYPE
       SYNTAX     AirFiberStatusEntry
       MAX-ACCESS not-accessible
       STATUS     current
       DESCRIPTION "An entry in the airFiberStatus Table"
       INDEX      { airFiberStatusIndex }
       ::= { airFiberStatus 1 }


    AirFiberStatusEntry ::= SEQUENCE {
    airFiberStatusIndex     Integer32,
    curTXModRate            Integer32,
    radioLinkDistFt         Integer32,
    radioLinkDistM          Integer32,
    rxCapacity              Integer32,
    txCapacity              Integer32,
    radio0TempC             Integer32,
    radio0TempF             Integer32,
    radio1TempC             Integer32,
    radio1TempF             Integer32,
    rxPower0                Integer32,
    rxPower0Valid           TruthValue,
    rxOverload0             TruthValue,
    rxPower1                Integer32,
    rxPower1Valid           TruthValue,
    rxOverload1             TruthValue,
    remoteTXPower           Integer32,
    remoteTXModRate         Integer32,
    remoteRXPower0          Integer32,
    remoteRXPower0Valid     TruthValue,
    remoteRXPower0Overload  TruthValue,
    remoteRXPower1          Integer32,
    remoteRXPower1Valid     TruthValue,
    remoteRXPower1Overload  TruthValue,
    countryCode             Integer32,
    radioLinkState          Integer32,
    ethDataPortState        Integer32,
    gpsPulse                DisplayString,
    gpsFix                  DisplayString,
    gpsLat                  DisplayString,
    gpsLong                 DisplayString,
    gpsAltMeters            DisplayString,
    gpsAltFeet              DisplayString,
    gpsSatsVisible          Integer32,
    gpsSatsTracked          Integer32,
    gpsHDOP                 OCTET STRING,
    dfsState                DisplayString,
    upTime                  Integer32,
    dateTime                DisplayString,  
    fwVersion               DisplayString,
    remoteRXGain            DisplayString,
    radioLinkInfo           DisplayString,
    ethDataPortInfo         DisplayString,    
    linkUpTime              Integer32,
    remoteMAC               DisplayString,
    remoteIP                DisplayString,
    dfsDetections           Integer32,
    dfsDomain               DisplayString,
    dfsStateTxFreq1         DisplayString,
    dfsStateTxFreq2         DisplayString,
    dfsStateTxFreq3         DisplayString,
    dfsTimerTxFreq1         Integer32,
    dfsTimerTxFreq2         Integer32,
    dfsTimerTxFreq3         Integer32    
    }        
    
    airFiberStatusIndex OBJECT-TYPE
        SYNTAX     Integer32 (1..255)
        MAX-ACCESS not-accessible
        STATUS     current
        DESCRIPTION "Index for the air0 interface"
        ::= { airFiberStatusEntry 1 }

    curTXModRate OBJECT-TYPE
       SYNTAX     Integer32 {
            qPSK-SISO-1-4x (0),
            qPSK-SISO-1x   (1),
            qPSK-MIMO-2x   (2),
            qAM16-MIMO-4x  (4),
            qAM64-MIMO-6x  (6),
            qAM256-MIMO-8x (8)
        } 
        MAX-ACCESS read-only
        STATUS     current
        DESCRIPTION "Current Transmit Modulation Rate"
        ::= { airFiberStatusEntry 2 }

    radioLinkDistFt OBJECT-TYPE
        SYNTAX Integer32
        MAX-ACCESS read-only
        STATUS current
        DESCRIPTION "Radio Link Distance (Feet)"
        ::= { airFiberStatusEntry 3 }

    radioLinkDistM OBJECT-TYPE
        SYNTAX Integer32
        MAX-ACCESS read-only
        STATUS current
        DESCRIPTION "Radio Link Distance (Meters)"
        ::= { airFiberStatusEntry 4 }

    rxCapacity OBJECT-TYPE
        SYNTAX Integer32
        MAX-ACCESS read-only
        STATUS current
        DESCRIPTION "Radio Receive Throughput Capacity (bits/sec)"
        ::= { airFiberStatusEntry 5 }

    txCapacity OBJECT-TYPE
        SYNTAX Integer32
        MAX-ACCESS read-only
        STATUS current
        DESCRIPTION "Radio Transmit Throughput Capacity (bits/sec)"
        ::= { airFiberStatusEntry 6 }

    radio0TempF OBJECT-TYPE
        SYNTAX Integer32
        MAX-ACCESS read-only
        STATUS current
        DESCRIPTION "Radio Chain 0 DAC Temperature (F)"
        ::= { airFiberStatusEntry 7 }

    radio0TempC OBJECT-TYPE
        SYNTAX Integer32
        MAX-ACCESS read-only
        STATUS current
        DESCRIPTION "Radio Chain 0 DAC Temperature (C)"
        ::= { airFiberStatusEntry 8 }

    radio1TempF OBJECT-TYPE
        SYNTAX Integer32
        MAX-ACCESS read-only
        STATUS current
        DESCRIPTION "Radio Chain 1 DAC Temperature (F)"
        ::= { airFiberStatusEntry 9 }

    radio1TempC OBJECT-TYPE
        SYNTAX Integer32
        MAX-ACCESS read-only
        STATUS current
        DESCRIPTION "Radio Chain 0 DAC Temperature (C)"
        ::= { airFiberStatusEntry 10 }

    rxPower0 OBJECT-TYPE
        SYNTAX Integer32
        MAX-ACCESS read-only
        STATUS current
        DESCRIPTION "Radio Chain 0 RX Power Level (dBm)"
        ::= { airFiberStatusEntry 11 }

    rxPower0Valid OBJECT-TYPE
        SYNTAX TruthValue
        MAX-ACCESS read-only
        STATUS current
        DESCRIPTION "Radio Chain 0 RX Power Valid"
        ::= { airFiberStatusEntry 12 }

    rxOverload0 OBJECT-TYPE
        SYNTAX TruthValue
        MAX-ACCESS read-only
        STATUS current
        DESCRIPTION "Radio Chain 0 RX Overloaded"
        ::= { airFiberStatusEntry 13 }

    rxPower1 OBJECT-TYPE
        SYNTAX Integer32
        MAX-ACCESS read-only
        STATUS current
        DESCRIPTION "Radio Chain 1 RX Power Level (dBm)"
        ::= { airFiberStatusEntry 14 }

    rxPower1Valid OBJECT-TYPE
        SYNTAX TruthValue
        MAX-ACCESS read-only
        STATUS current
        DESCRIPTION "Radio  Chain 1 RX Power Valid"
        ::= { airFiberStatusEntry 15 }

    rxOverload1 OBJECT-TYPE
        SYNTAX TruthValue
        MAX-ACCESS read-only
        STATUS current
        DESCRIPTION "Radio  Chain 1 RX Overloaded"
        ::= { airFiberStatusEntry 16 }

    remoteTXPower OBJECT-TYPE
        SYNTAX Integer32
        MAX-ACCESS read-only
        STATUS current
        DESCRIPTION "Remote Radio Transmit Power Level (dBm)"
        ::= { airFiberStatusEntry 17 }

    remoteTXModRate OBJECT-TYPE
       SYNTAX     Integer32 {
            qPSK-SISO-1-4x (0),
            qPSK-SISO-1x   (1),
            qPSK-MIMO-2x   (2),
            qAM16-MIMO-4x  (4),
            qAM64-MIMO-6x  (6),
            qAM256-MIMO-8x (8)
        } 
        MAX-ACCESS read-only
        STATUS     current
        DESCRIPTION "Remote Transmit Modulation Rate"
        ::= { airFiberStatusEntry 18 }

    remoteRXPower0 OBJECT-TYPE
        SYNTAX Integer32
        MAX-ACCESS read-only
        STATUS current
        DESCRIPTION "Remote Radio Chain 0 RX Power Level (dBm)"
        ::= { airFiberStatusEntry 19 }

    remoteRXPower0Valid OBJECT-TYPE
        SYNTAX TruthValue
        MAX-ACCESS read-only
        STATUS current
        DESCRIPTION "Remote Radio Chain 0 RX Power Valid"
        ::= { airFiberStatusEntry 20 }

    remoteRXPower0Overload OBJECT-TYPE
        SYNTAX TruthValue
        MAX-ACCESS read-only
        STATUS current
        DESCRIPTION "Remote Radio Chain 0 RX Overloaded"
        ::= { airFiberStatusEntry 21 }

    remoteRXPower1 OBJECT-TYPE
        SYNTAX Integer32
        MAX-ACCESS read-only
        STATUS current
        DESCRIPTION "Remote Radio Chain 1 RX Power Level (dBm)"
        ::= { airFiberStatusEntry 22 }

    remoteRXPower1Valid OBJECT-TYPE
        SYNTAX TruthValue
        MAX-ACCESS read-only
        STATUS current
        DESCRIPTION "Remote Radio  Chain 1 RX Power Valid"
        ::= { airFiberStatusEntry 23 }

    remoteRXPower1Overload OBJECT-TYPE
        SYNTAX TruthValue
        MAX-ACCESS read-only
        STATUS current
        DESCRIPTION "Remote Radio  Chain 1 RX Overloaded"
        ::= { airFiberStatusEntry 24 }

    countryCode OBJECT-TYPE
        SYNTAX Integer32
        MAX-ACCESS read-only
        STATUS current
        DESCRIPTION "Configured Country Code"
        ::= { airFiberStatusEntry 25 }

    radioLinkState OBJECT-TYPE
        SYNTAX     Integer32 {
                down (0),
                up   (1)
        }         
        MAX-ACCESS read-only
        STATUS     current
        DESCRIPTION "Radio Link State"
        ::= { airFiberStatusEntry 26 }

    ethDataPortState OBJECT-TYPE
        SYNTAX     Integer32 {
                down (0),
                up   (1)
        }         
        MAX-ACCESS read-only
        STATUS     current
        DESCRIPTION "Ethernet Data Port State"
        ::= { airFiberStatusEntry 27 }

    gpsPulse OBJECT-TYPE
        SYNTAX     DisplayString
        MAX-ACCESS read-only
        STATUS     current
        DESCRIPTION "GPS Pulse Detected"
        ::= { airFiberStatusEntry 28 }

    gpsFix OBJECT-TYPE
        SYNTAX     DisplayString
        MAX-ACCESS read-only
        STATUS     current
        DESCRIPTION "GPS Fix Obtained"
        ::= { airFiberStatusEntry 29 }

    gpsLat OBJECT-TYPE
        SYNTAX     DisplayString
        MAX-ACCESS read-only
        STATUS     current
        DESCRIPTION "GPS Latitude"
        ::= { airFiberStatusEntry 30 }

    gpsLong OBJECT-TYPE
        SYNTAX     DisplayString
        MAX-ACCESS read-only
        STATUS     current
        DESCRIPTION "GPS Longitude"
        ::= { airFiberStatusEntry 31 }

    gpsAltMeters OBJECT-TYPE
        SYNTAX     DisplayString
        MAX-ACCESS read-only
        STATUS     current
        DESCRIPTION "GPS Altitude (m)"
        ::= { airFiberStatusEntry 32 }

    gpsAltFeet OBJECT-TYPE
        SYNTAX     DisplayString
        MAX-ACCESS read-only
        STATUS     current
        DESCRIPTION "GPS Altitude (ft)"
        ::= { airFiberStatusEntry 33 }

    gpsSatsVisible OBJECT-TYPE
        SYNTAX Integer32
        MAX-ACCESS read-only
        STATUS current
        DESCRIPTION "GPS Satellites Visible"
        ::= { airFiberStatusEntry 34 }

    gpsSatsTracked OBJECT-TYPE
        SYNTAX Integer32
        MAX-ACCESS read-only
        STATUS current
        DESCRIPTION "GPS Satellites Tracked"
        ::= { airFiberStatusEntry 35 }

    gpsHDOP OBJECT-TYPE
        SYNTAX OCTET STRING
        MAX-ACCESS read-only
        STATUS current
        DESCRIPTION "GPS Horizontal Dilution of Precision"
        ::= { airFiberStatusEntry 36 }

    dfsState OBJECT-TYPE
        SYNTAX DisplayString
        MAX-ACCESS read-only
        STATUS current
        DESCRIPTION "Radio DFS State"
        ::= { airFiberStatusEntry 37 }

    upTime OBJECT-TYPE
        SYNTAX Integer32
        MAX-ACCESS read-only
        STATUS current
        DESCRIPTION "Board uptime (seconds)"
        ::= { airFiberStatusEntry 38 }

    dateTime OBJECT-TYPE
        SYNTAX     DisplayString
        MAX-ACCESS read-only
        STATUS     current
        DESCRIPTION "Board date and time"
        ::= { airFiberStatusEntry 39 }

    fwVersion OBJECT-TYPE
        SYNTAX     DisplayString
        MAX-ACCESS read-only
        STATUS     current
        DESCRIPTION "Board Firmware Revision"
        ::= { airFiberStatusEntry 40 }

    remoteRXGain OBJECT-TYPE
        SYNTAX     DisplayString
        MAX-ACCESS read-only
        STATUS     current
        DESCRIPTION "Remote radio Receiver Gain"
        ::= { airFiberStatusEntry 41 }

    radioLinkInfo OBJECT-TYPE
        SYNTAX     DisplayString
        MAX-ACCESS read-only
        STATUS     current
        DESCRIPTION "Radio Link Connection Information"
        ::= { airFiberStatusEntry 42 }

    ethDataPortInfo OBJECT-TYPE
        SYNTAX     DisplayString
        MAX-ACCESS read-only
        STATUS     current
        DESCRIPTION "Ethernet Data Port Link Connection Speed"
        ::= { airFiberStatusEntry 43 }        

    linkUpTime OBJECT-TYPE
        SYNTAX Integer32
        MAX-ACCESS read-only
        STATUS current
        DESCRIPTION "Radio Link uptime (seconds)"
        ::= { airFiberStatusEntry 44 }

    remoteMAC OBJECT-TYPE
        SYNTAX     DisplayString
        MAX-ACCESS read-only
        STATUS     current
        DESCRIPTION "Remote radio MAC Address"
        ::= { airFiberStatusEntry 45 }

    remoteIP OBJECT-TYPE
        SYNTAX     DisplayString
        MAX-ACCESS read-only
        STATUS     current
        DESCRIPTION "Remote radio IP Address"
        ::= { airFiberStatusEntry 46 }

    dfsDetections OBJECT-TYPE
        SYNTAX Integer32
        MAX-ACCESS read-only
        STATUS current
        DESCRIPTION "Number of DFS Detections since boot.  5 GHz radios only."
        ::= { airFiberStatusEntry 47 }

    dfsDomain OBJECT-TYPE
        SYNTAX     DisplayString
        MAX-ACCESS read-only
        STATUS     current
        DESCRIPTION "DFS Regulatory Domain for current TX Frequency.  5 GHz radios only."
        ::= { airFiberStatusEntry 48 }

    dfsStateTxFreq1 OBJECT-TYPE
        SYNTAX     DisplayString
        MAX-ACCESS read-only
        STATUS     current
        DESCRIPTION "State of first TX Frequency.  5 GHz radios only."
        ::= { airFiberStatusEntry 49 }

    dfsStateTxFreq2 OBJECT-TYPE
        SYNTAX     DisplayString
        MAX-ACCESS read-only
        STATUS     current
        DESCRIPTION "State of second TX Frequency.  5 GHz radios only."
        ::= { airFiberStatusEntry 50 }

    dfsStateTxFreq3 OBJECT-TYPE
        SYNTAX     DisplayString
        MAX-ACCESS read-only
        STATUS     current
        DESCRIPTION "State of third TX Frequency.  5 GHz radios only."
        ::= { airFiberStatusEntry 51 }

    dfsTimerTxFreq1 OBJECT-TYPE
        SYNTAX     Integer32
        MAX-ACCESS read-only
        STATUS     current
        DESCRIPTION "Seconds remaining before first TX Frequency can advance to next operating state.  Channel availability check timeout 
                     is 60 seconds and DFS detection timeout is 30 minutes.  5 GHz radios only."
        ::= { airFiberStatusEntry 52 }

    dfsTimerTxFreq2 OBJECT-TYPE
        SYNTAX     Integer32
        MAX-ACCESS read-only
        STATUS     current
        DESCRIPTION "Seconds remaining before second TX Frequency can advance to next operating state.  Channel availability check timeout 
                     is 60 seconds and DFS detection timeout is 30 minutes.  5 GHz radios only."
        ::= { airFiberStatusEntry 53 }

    dfsTimerTxFreq3 OBJECT-TYPE
        SYNTAX     Integer32
        MAX-ACCESS read-only
        STATUS     current
         DESCRIPTION "Seconds remaining before third TX Frequency can advance to next operating state.  Channel availability check timeout 
                     is 60 seconds and DFS detection timeout is 30 minutes.  5 GHz radios only."
        ::= { airFiberStatusEntry 54 }

    -- --------------------------------------------------------------------------------
    --                            AirFiber Statistics Table
    -- --------------------------------------------------------------------------------

    airFiberStatistics OBJECT-TYPE
        SYNTAX     SEQUENCE OF AirFiberStatisticsEntry
        MAX-ACCESS not-accessible
        STATUS     current
        DESCRIPTION "AirFiber Statistics"
        ::= { ubntAirFIBER 3 }


    airFiberStatisticsEntry OBJECT-TYPE
       SYNTAX     AirFiberStatisticsEntry
       MAX-ACCESS not-accessible
       STATUS     current
       DESCRIPTION "An entry in the AirFiberStatisticsTable"
       INDEX      { airFiberStatisticsIndex }
       ::= { airFiberStatistics 1 }


    AirFiberStatisticsEntry ::= SEQUENCE {
    airFiberStatisticsIndex     Integer32,
    txFramesOK                  Counter64,
    rxFramesOK                  Counter64,
    rxFrameCrcErr               Counter64,
    rxAlignErr                  Counter64,
    txOctetsOK                  Counter64,
    rxOctetsOK                  Counter64,
    txPauseFrames               Counter64,
    rxPauseFrames               Counter64,
    rxErroredFrames             Counter64,
    txErroredFrames             Counter64,
    rxValidUnicastFrames        Counter64,
    rxValidMulticastFrames      Counter64,
    rxValidBroadcastFrames      Counter64,
    txValidUnicastFrames        Counter64,
    txValidMulticastFrames      Counter64,
    txValidBroadcastFrames      Counter64,
    rxDroppedMacErrFrames       Counter64,
    rxTotalOctets               Counter64,
    rxTotalFrames               Counter64,
    rxLess64ByteFrames          Counter64,
    rxOverLengthFrames          Counter64,
    rx64BytePackets             Counter64,
    rx65-127BytePackets         Counter64,
    rx128-255BytePackets        Counter64,
    rx256-511BytePackets        Counter64,
    rx512-1023BytePackets       Counter64,
    rx1024-1518BytesPackets     Counter64,
    rx1519PlusBytePackets       Counter64,
    rxTooLongFrameCrcErr        Counter64,
    rxTooShortFrameCrcErr       Counter64,
    txqosoct0                   Counter64,
    txqosoct1                   Counter64,
    txqosoct2                   Counter64,
    txqosoct3                   Counter64,
    txqosoct4                   Counter64,
    txqosoct5                   Counter64,
    txqosoct6                   Counter64,
    txqosoct7                   Counter64,
    txqospkt0                   Counter64,
    txqospkt1                   Counter64,
    txqospkt2                   Counter64,
    txqospkt3                   Counter64,
    txqospkt4                   Counter64,
    txqospkt5                   Counter64,
    txqospkt6                   Counter64,
    txqospkt7                   Counter64,
    rxqosoct0                   Counter64,
    rxqosoct1                   Counter64,
    rxqosoct2                   Counter64,
    rxqosoct3                   Counter64,
    rxqosoct4                   Counter64,
    rxqosoct5                   Counter64,
    rxqosoct6                   Counter64,
    rxqosoct7                   Counter64,
    rxqospkt0                   Counter64,
    rxqospkt1                   Counter64,
    rxqospkt2                   Counter64,
    rxqospkt3                   Counter64,
    rxqospkt4                   Counter64,
    rxqospkt5                   Counter64,
    rxqospkt6                   Counter64,
    rxqospkt7                   Counter64,
    txoctetsAll                 Counter64,
    txpktsAll                   Counter64,
    rxoctetsAll                 Counter64,
    rxpktsAll                   Counter64
    }

    airFiberStatisticsIndex OBJECT-TYPE
        SYNTAX     Integer32 (1..255)
        MAX-ACCESS not-accessible
        STATUS     current
        DESCRIPTION "Index for the airFiberStatus"
        ::= { airFiberStatisticsEntry 1 }

    txFramesOK OBJECT-TYPE
        SYNTAX Counter64
        MAX-ACCESS read-only
        STATUS current
        DESCRIPTION "Eth Data Port  TX Frames"
        ::= { airFiberStatisticsEntry 2 }

    rxFramesOK OBJECT-TYPE
        SYNTAX Counter64
        MAX-ACCESS read-only
        STATUS current
        DESCRIPTION "Eth Data Port RX Frames"
        ::= { airFiberStatisticsEntry 3 }

    rxFrameCrcErr OBJECT-TYPE
        SYNTAX Counter64
        MAX-ACCESS read-only
        STATUS current
        DESCRIPTION "Eth Data Port CRC Errors"
        ::= { airFiberStatisticsEntry 4 }

    rxAlignErr OBJECT-TYPE
        SYNTAX Counter64
        MAX-ACCESS read-only
        STATUS current
        DESCRIPTION "Eth Data Port Receive Alignment Errors"
        ::= { airFiberStatisticsEntry 5 }

    txOctetsOK OBJECT-TYPE
        SYNTAX Counter64
        MAX-ACCESS read-only
        STATUS current
        DESCRIPTION "Eth Data Port  TX Octets"
        ::= { airFiberStatisticsEntry 6 }

    rxOctetsOK OBJECT-TYPE
        SYNTAX Counter64
        MAX-ACCESS read-only
        STATUS current
        DESCRIPTION "Eth Data Port RX Octets"
        ::= { airFiberStatisticsEntry 7 }

    txPauseFrames OBJECT-TYPE
        SYNTAX Counter64
        MAX-ACCESS read-only
        STATUS current
        DESCRIPTION "Eth Data Port Pause Frames Transmitted"
        ::= { airFiberStatisticsEntry 8 }

    rxPauseFrames OBJECT-TYPE
        SYNTAX Counter64
        MAX-ACCESS read-only
        STATUS current
        DESCRIPTION "Eth Data Port Pause Frames Received"
        ::= { airFiberStatisticsEntry 9 }

    rxErroredFrames OBJECT-TYPE
        SYNTAX Counter64
        MAX-ACCESS read-only
        STATUS current
        DESCRIPTION "Eth Data Port Bad Frames Received"
        ::= { airFiberStatisticsEntry 10 }

    txErroredFrames OBJECT-TYPE
        SYNTAX Counter64
        MAX-ACCESS read-only
        STATUS current
        DESCRIPTION "Eth Data Port Bad Frames Transmitted"
        ::= { airFiberStatisticsEntry 11 }

    rxValidUnicastFrames OBJECT-TYPE
        SYNTAX Counter64
        MAX-ACCESS read-only
        STATUS current
        DESCRIPTION "Eth Data Port Unicast Frames Received"
        ::= { airFiberStatisticsEntry 12 }

    rxValidMulticastFrames OBJECT-TYPE
        SYNTAX Counter64
        MAX-ACCESS read-only
        STATUS current
        DESCRIPTION "Eth Data Port Multicast Frames Received"
        ::= { airFiberStatisticsEntry 13 }

    rxValidBroadcastFrames OBJECT-TYPE
        SYNTAX Counter64
        MAX-ACCESS read-only
        STATUS current
        DESCRIPTION "Eth Data Port Broadcast Frames Received"
        ::= { airFiberStatisticsEntry 14 }

    txValidUnicastFrames OBJECT-TYPE
        SYNTAX Counter64
        MAX-ACCESS read-only
        STATUS current
        DESCRIPTION "Eth Data Port Unicast Frames Transmitted"
        ::= { airFiberStatisticsEntry 15 }

    txValidMulticastFrames OBJECT-TYPE
        SYNTAX Counter64
        MAX-ACCESS read-only
        STATUS current
        DESCRIPTION "Eth Data Port Multicast Frames Transmitted"
        ::= { airFiberStatisticsEntry 16 }

    txValidBroadcastFrames OBJECT-TYPE
        SYNTAX Counter64
        MAX-ACCESS read-only
        STATUS current
        DESCRIPTION "Eth Data Port Broadcast Frames Transmitted"
        ::= { airFiberStatisticsEntry 17 }

    rxDroppedMacErrFrames OBJECT-TYPE
        SYNTAX Counter64
        MAX-ACCESS read-only
        STATUS current
        DESCRIPTION "Eth Data Port Dropped MAC Receive Errors"
        ::= { airFiberStatisticsEntry 18 }

    rxTotalOctets OBJECT-TYPE
        SYNTAX Counter64
        MAX-ACCESS read-only
        STATUS current
        DESCRIPTION "Eth Data Port Total Octets Received"
        ::= { airFiberStatisticsEntry 19 }

    rxTotalFrames OBJECT-TYPE
        SYNTAX Counter64
        MAX-ACCESS read-only
        STATUS current
        DESCRIPTION "Eth Data Port Total Frames Received"
        ::= { airFiberStatisticsEntry 20 }

    rxLess64ByteFrames OBJECT-TYPE
        SYNTAX Counter64
        MAX-ACCESS read-only
        STATUS current
        DESCRIPTION "Eth Data Port Undersized Frames Received"
        ::= { airFiberStatisticsEntry 21 }

    rxOverLengthFrames OBJECT-TYPE
        SYNTAX Counter64
        MAX-ACCESS read-only
        STATUS current
        DESCRIPTION "Eth Data Port Over Max Length Frames Received"
        ::= { airFiberStatisticsEntry 22 }

    rx64BytePackets OBJECT-TYPE
        SYNTAX Counter64
        MAX-ACCESS read-only
        STATUS current
        DESCRIPTION "Eth Data Port 64 Byte Frames Received"
        ::= { airFiberStatisticsEntry 23 }

    rx65-127BytePackets OBJECT-TYPE
        SYNTAX Counter64
        MAX-ACCESS read-only
        STATUS current
        DESCRIPTION "Eth Data Port 65-127 Byte Frames Received"
        ::= { airFiberStatisticsEntry 24 }

    rx128-255BytePackets OBJECT-TYPE
        SYNTAX Counter64
        MAX-ACCESS read-only
        STATUS current
        DESCRIPTION "Eth Data Port 128-256 Byte Frames Received"
        ::= { airFiberStatisticsEntry 25 }

    rx256-511BytePackets OBJECT-TYPE
        SYNTAX Counter64
        MAX-ACCESS read-only
        STATUS current
        DESCRIPTION "Eth Data Port 256-511 Byte Frames Received"
        ::= { airFiberStatisticsEntry 26 }

    rx512-1023BytePackets OBJECT-TYPE
        SYNTAX Counter64
        MAX-ACCESS read-only
        STATUS current
        DESCRIPTION "Eth Data Port 512-1023 Byte Frames Received"
        ::= { airFiberStatisticsEntry 27 }

    rx1024-1518BytesPackets OBJECT-TYPE
        SYNTAX Counter64
        MAX-ACCESS read-only
        STATUS current
        DESCRIPTION "Eth Data Port 1024-1518 Byte Frames Received"
        ::= { airFiberStatisticsEntry 28 }

    rx1519PlusBytePackets OBJECT-TYPE
        SYNTAX Counter64
        MAX-ACCESS read-only
        STATUS current
        DESCRIPTION "Eth Data Port Greater Than 1518 Byte Frames Received"
        ::= { airFiberStatisticsEntry 29 }

    rxTooLongFrameCrcErr OBJECT-TYPE
        SYNTAX Counter64
        MAX-ACCESS read-only
        STATUS current
        DESCRIPTION "Eth Data Port Too Long Frame CRC Errors Received"
        ::= { airFiberStatisticsEntry 30 }

    rxTooShortFrameCrcErr OBJECT-TYPE
        SYNTAX Counter64
        MAX-ACCESS read-only
        STATUS current
        DESCRIPTION "Eth Data Port Too Short Frame CRC Errors Received"
        ::= { airFiberStatisticsEntry 31 }

    txqosoct0 OBJECT-TYPE
        SYNTAX Counter64
        MAX-ACCESS read-only
        STATUS current
        DESCRIPTION "RF TX Octets QOS 0"
        ::= { airFiberStatisticsEntry 32 }

    txqosoct1 OBJECT-TYPE
        SYNTAX Counter64
        MAX-ACCESS read-only
        STATUS current
        DESCRIPTION "RF TX Octets QOS 1"
        ::= { airFiberStatisticsEntry 33 }

    txqosoct2 OBJECT-TYPE
        SYNTAX Counter64
        MAX-ACCESS read-only
        STATUS current
        DESCRIPTION "RF TX Octets QOS 2"
        ::= { airFiberStatisticsEntry 34 }

    txqosoct3 OBJECT-TYPE
        SYNTAX Counter64
        MAX-ACCESS read-only
        STATUS current
        DESCRIPTION "RF TX Octets QOS 3"
        ::= { airFiberStatisticsEntry 35 }

    txqosoct4 OBJECT-TYPE
        SYNTAX Counter64
        MAX-ACCESS read-only
        STATUS current
        DESCRIPTION "RF TX Octets QOS 4"
        ::= { airFiberStatisticsEntry 36 }

    txqosoct5 OBJECT-TYPE
        SYNTAX Counter64
        MAX-ACCESS read-only
        STATUS current
        DESCRIPTION "RF TX Octets QOS 5"
        ::= { airFiberStatisticsEntry 37 }

    txqosoct6 OBJECT-TYPE
        SYNTAX Counter64
        MAX-ACCESS read-only
        STATUS current
        DESCRIPTION "RF TX Octets QOS 6"
        ::= { airFiberStatisticsEntry 38 }

    txqosoct7 OBJECT-TYPE
        SYNTAX Counter64
        MAX-ACCESS read-only
        STATUS current
        DESCRIPTION "RF TX Octets QOS 7"
        ::= { airFiberStatisticsEntry 39 }

    txqospkt0 OBJECT-TYPE
        SYNTAX Counter64
        MAX-ACCESS read-only
        STATUS current
        DESCRIPTION "RF TX Packets QOS 0"
        ::= { airFiberStatisticsEntry 40 }

    txqospkt1 OBJECT-TYPE
        SYNTAX Counter64
        MAX-ACCESS read-only
        STATUS current
        DESCRIPTION "RF TX Packets QOS 1"
        ::= { airFiberStatisticsEntry 41 }

    txqospkt2 OBJECT-TYPE
        SYNTAX Counter64
        MAX-ACCESS read-only
        STATUS current
        DESCRIPTION "RF TX Packets QOS 2"
        ::= { airFiberStatisticsEntry 42 }

    txqospkt3 OBJECT-TYPE
        SYNTAX Counter64
        MAX-ACCESS read-only
        STATUS current
        DESCRIPTION "RF TX Packets QOS 3"
        ::= { airFiberStatisticsEntry 43 }

    txqospkt4 OBJECT-TYPE
        SYNTAX Counter64
        MAX-ACCESS read-only
        STATUS current
        DESCRIPTION "RF TX Packets QOS 4"
        ::= { airFiberStatisticsEntry 44 }

    txqospkt5 OBJECT-TYPE
        SYNTAX Counter64
        MAX-ACCESS read-only
        STATUS current
        DESCRIPTION "RF TX Packets QOS 5"
        ::= { airFiberStatisticsEntry 45 }

    txqospkt6 OBJECT-TYPE
        SYNTAX Counter64
        MAX-ACCESS read-only
        STATUS current
        DESCRIPTION "RF TX Packets QOS 6"
        ::= { airFiberStatisticsEntry 46 }

    txqospkt7 OBJECT-TYPE
        SYNTAX Counter64
        MAX-ACCESS read-only
        STATUS current
        DESCRIPTION "RF TX Packets QOS 7"
        ::= { airFiberStatisticsEntry 47 }

    rxqosoct0 OBJECT-TYPE
        SYNTAX Counter64
        MAX-ACCESS read-only
        STATUS current
        DESCRIPTION "RF RX Octets QOS 0"
        ::= { airFiberStatisticsEntry 48 }

    rxqosoct1 OBJECT-TYPE
        SYNTAX Counter64
        MAX-ACCESS read-only
        STATUS current
        DESCRIPTION "RF RX Octets QOS 1"
        ::= { airFiberStatisticsEntry 49 }

    rxqosoct2 OBJECT-TYPE
        SYNTAX Counter64
        MAX-ACCESS read-only
        STATUS current
        DESCRIPTION "RF RX Octets QOS 2"
        ::= { airFiberStatisticsEntry 50 }

    rxqosoct3 OBJECT-TYPE
        SYNTAX Counter64
        MAX-ACCESS read-only
        STATUS current
        DESCRIPTION "RF RX Octets QOS 3"
        ::= { airFiberStatisticsEntry 51 }

    rxqosoct4 OBJECT-TYPE
        SYNTAX Counter64
        MAX-ACCESS read-only
        STATUS current
        DESCRIPTION "RF RX Octets QOS 4"
        ::= { airFiberStatisticsEntry 52 }

    rxqosoct5 OBJECT-TYPE
        SYNTAX Counter64
        MAX-ACCESS read-only
        STATUS current
        DESCRIPTION "RF RX Octets QOS 5"
        ::= { airFiberStatisticsEntry 53 }

    rxqosoct6 OBJECT-TYPE
        SYNTAX Counter64
        MAX-ACCESS read-only
        STATUS current
        DESCRIPTION "RF RX Octets QOS 6"
        ::= { airFiberStatisticsEntry 54 }

    rxqosoct7 OBJECT-TYPE
        SYNTAX Counter64
        MAX-ACCESS read-only
        STATUS current
        DESCRIPTION "RF RX Octets QOS 7"
        ::= { airFiberStatisticsEntry 55 }

    rxqospkt0 OBJECT-TYPE
        SYNTAX Counter64
        MAX-ACCESS read-only
        STATUS current
        DESCRIPTION "RF RX Packets QOS 0"
        ::= { airFiberStatisticsEntry 56 }

    rxqospkt1 OBJECT-TYPE
        SYNTAX Counter64
        MAX-ACCESS read-only
        STATUS current
        DESCRIPTION "RF RX Packets QOS 1"
        ::= { airFiberStatisticsEntry 57 }

    rxqospkt2 OBJECT-TYPE
        SYNTAX Counter64
        MAX-ACCESS read-only
        STATUS current
        DESCRIPTION "RF RX Packets QOS 2"
        ::= { airFiberStatisticsEntry 58 }

    rxqospkt3 OBJECT-TYPE
        SYNTAX Counter64
        MAX-ACCESS read-only
        STATUS current
        DESCRIPTION "RF RX Packets QOS 3"
        ::= { airFiberStatisticsEntry 59 }

    rxqospkt4 OBJECT-TYPE
        SYNTAX Counter64
        MAX-ACCESS read-only
        STATUS current
        DESCRIPTION "RF RX Packets QOS 4"
        ::= { airFiberStatisticsEntry 60 }

    rxqospkt5 OBJECT-TYPE
        SYNTAX Counter64
        MAX-ACCESS read-only
        STATUS current
        DESCRIPTION "RF RX Packets QOS 5"
        ::= { airFiberStatisticsEntry 61 }

    rxqospkt6 OBJECT-TYPE
        SYNTAX Counter64
        MAX-ACCESS read-only
        STATUS current
        DESCRIPTION "RF RX Packets QOS 6"
        ::= { airFiberStatisticsEntry 62 }

    rxqospkt7 OBJECT-TYPE
        SYNTAX Counter64
        MAX-ACCESS read-only
        STATUS current
        DESCRIPTION "RF RX Packets QOS 7"
        ::= { airFiberStatisticsEntry 63 }

    txoctetsAll OBJECT-TYPE
        SYNTAX Counter64
        MAX-ACCESS read-only
        STATUS current
        DESCRIPTION "RF Total Octets Transmitted"
        ::= { airFiberStatisticsEntry 64 }

    txpktsAll OBJECT-TYPE
        SYNTAX Counter64
        MAX-ACCESS read-only
        STATUS current
        DESCRIPTION "RF Total Packets Transmitted"
        ::= { airFiberStatisticsEntry 65 }

    rxoctetsAll OBJECT-TYPE
        SYNTAX Counter64
        MAX-ACCESS read-only
        STATUS current
        DESCRIPTION "RF Total Octets Received"
        ::= { airFiberStatisticsEntry 66 }

    rxpktsAll OBJECT-TYPE
        SYNTAX Counter64
        MAX-ACCESS read-only
        STATUS current
        DESCRIPTION "RF Total Packets Received"
        ::= { airFiberStatisticsEntry 67 }

 END


File: /dude_custom_files\UBNT-AirMAX-MIB.txt
UBNT-AirMAX-MIB DEFINITIONS ::= BEGIN
    IMPORTS
        MODULE-IDENTITY, OBJECT-TYPE, Integer32, Gauge32, Counter64,
        IpAddress, TimeTicks FROM SNMPv2-SMI
        DisplayString, TruthValue, MacAddress FROM SNMPv2-TC
        OBJECT-GROUP, MODULE-COMPLIANCE FROM SNMPv2-CONF
        ubntAirosGroups, ubntMIB FROM UBNT-MIB;

    ubntAirMAX MODULE-IDENTITY
    LAST-UPDATED "201405250000Z"
    ORGANIZATION "Ubiquiti Networks, Inc."
    CONTACT-INFO "support@ubnt.com"
    DESCRIPTION  "The AirMAX MIB module for Ubiquiti Networks, Inc. entities"
    REVISION "201405250000Z"
    DESCRIPTION "ubntAirMAX revision"
    ::= { ubntMIB 4 }

    -- --------------------------------------------------------------------------------
    --                            radio table
    -- --------------------------------------------------------------------------------

    ubntRadioTable OBJECT-TYPE
        SYNTAX     SEQUENCE OF UbntRadioEntry
        MAX-ACCESS not-accessible
        STATUS     current
        DESCRIPTION "Radio status & statistics"
        ::= { ubntAirMAX 1 }

    ubntRadioEntry OBJECT-TYPE
       SYNTAX     UbntRadioEntry
       MAX-ACCESS not-accessible
       STATUS     current
       DESCRIPTION "An entry in the ubntRadioTable"
       INDEX      { ubntRadioIndex }
       ::= { ubntRadioTable 1 }

    UbntRadioEntry ::= SEQUENCE {
        ubntRadioIndex      Integer32,
        ubntRadioMode       INTEGER,
        ubntRadioCCode      Integer32,
        ubntRadioFreq       Integer32,
        ubntRadioDfsEnabled TruthValue,
        ubntRadioTxPower    Integer32,
        ubntRadioDistance   Integer32,
        ubntRadioChainmask  Integer32,
        ubntRadioAntenna    DisplayString
    }

    ubntRadioIndex OBJECT-TYPE
        SYNTAX     Integer32 (1..255)
        MAX-ACCESS not-accessible
        STATUS     current
        DESCRIPTION "Index for the ubntRadioTable"
        ::= { ubntRadioEntry 1 }

    ubntRadioMode OBJECT-TYPE
        SYNTAX     INTEGER {
		sta(1),
		ap(2),
		aprepeater(3),
		apwds(4)
	}
        MAX-ACCESS read-only
        STATUS     current
        DESCRIPTION "Radio mode"
        ::= { ubntRadioEntry 2 }

    ubntRadioCCode OBJECT-TYPE
        SYNTAX     Integer32
        MAX-ACCESS read-only
        STATUS     current
        DESCRIPTION "Country code"
        ::= { ubntRadioEntry 3 }

    ubntRadioFreq OBJECT-TYPE
        SYNTAX Integer32 (1..65535)
        MAX-ACCESS read-only
        STATUS current
        DESCRIPTION "Operating frequency"
        ::= { ubntRadioEntry 4 }

    ubntRadioDfsEnabled OBJECT-TYPE
        SYNTAX TruthValue
        MAX-ACCESS read-only
        STATUS current
        DESCRIPTION "DFS status"
        ::= { ubntRadioEntry 5 }

    ubntRadioTxPower OBJECT-TYPE
        SYNTAX Integer32 (1..65535)
        MAX-ACCESS read-only
        STATUS current
        DESCRIPTION "Transmit power"
        ::= { ubntRadioEntry 6 }

    ubntRadioDistance OBJECT-TYPE
        SYNTAX Integer32 (1..65535)
        MAX-ACCESS read-only
        STATUS current
        DESCRIPTION "Distance"
        ::= { ubntRadioEntry 7 }

    ubntRadioChainmask OBJECT-TYPE
        SYNTAX Integer32 (1..255)
        MAX-ACCESS read-only
        STATUS current
        DESCRIPTION "Chainmask"
        ::= { ubntRadioEntry 8 }

    ubntRadioAntenna OBJECT-TYPE
        SYNTAX     DisplayString
        MAX-ACCESS read-only
        STATUS     current
        DESCRIPTION "Antenna"
        ::= { ubntRadioEntry 9 }

    ubntRadioRssiTable OBJECT-TYPE
        SYNTAX     SEQUENCE OF UbntRadioRssiEntry
        MAX-ACCESS not-accessible
        STATUS     current
        DESCRIPTION "Radio RSSI per chain"
        ::= { ubntAirMAX 2 }

    ubntRadioRssiEntry OBJECT-TYPE
       SYNTAX     UbntRadioRssiEntry
       MAX-ACCESS not-accessible
       STATUS     current
       DESCRIPTION "An entry in the ubntRadioRssiTable"
       INDEX      { ubntRadioIndex, ubntRadioRssiIndex }
       ::= { ubntRadioRssiTable 1 }

    UbntRadioRssiEntry ::= SEQUENCE {
        ubntRadioRssiIndex Integer32,
        ubntRadioRssi      Integer32,
        ubntRadioRssiMgmt  Integer32,
        ubntRadioRssiExt   Integer32
    }

    ubntRadioRssiIndex OBJECT-TYPE
        SYNTAX     Integer32 (1..255)
        MAX-ACCESS not-accessible 
        STATUS     current
        DESCRIPTION "Index for the ubntRadioRssiTable"
        ::= { ubntRadioRssiEntry 1 }

    ubntRadioRssi OBJECT-TYPE
        SYNTAX Integer32
        MAX-ACCESS read-only
        STATUS current
        DESCRIPTION "Data frames rssi per chain"
        ::= { ubntRadioRssiEntry 2 }

    ubntRadioRssiMgmt OBJECT-TYPE
        SYNTAX Integer32
        MAX-ACCESS read-only
        STATUS current
        DESCRIPTION "Management frames rssi per chain"
        ::= { ubntRadioRssiEntry 3 }

    ubntRadioRssiExt OBJECT-TYPE
        SYNTAX Integer32
        MAX-ACCESS read-only
        STATUS current
        DESCRIPTION "Extension channel rssi per chain"
        ::= { ubntRadioRssiEntry 4 }

    -- --------------------------------------------------------------------------------
    --                            airMAX table
    -- --------------------------------------------------------------------------------

    ubntAirMaxTable OBJECT-TYPE
        SYNTAX     SEQUENCE OF UbntAirMaxEntry
        MAX-ACCESS not-accessible
        STATUS     current
        DESCRIPTION "airMAX protocol statistics"
        ::= { ubntAirMAX 6 }

    ubntAirMaxEntry OBJECT-TYPE
       SYNTAX     UbntAirMaxEntry
       MAX-ACCESS not-accessible
       STATUS     current
       DESCRIPTION "An entry in the ubntAirMaxTable"
       INDEX      { ubntAirMaxIfIndex }
       ::= { ubntAirMaxTable 1 }

    UbntAirMaxEntry ::= SEQUENCE {
        ubntAirMaxIfIndex     Integer32,
        ubntAirMaxEnabled     TruthValue,
        ubntAirMaxQuality     Integer32,
        ubntAirMaxCapacity    Integer32,
        ubntAirMaxPriority    INTEGER,
        ubntAirMaxNoAck       TruthValue
    }

    ubntAirMaxIfIndex OBJECT-TYPE
        SYNTAX     Integer32 (1..255)
        MAX-ACCESS not-accessible 
        STATUS     current
        DESCRIPTION "Index for the ubntAirMaxTable"
        ::= { ubntAirMaxEntry 1 }

    ubntAirMaxEnabled OBJECT-TYPE
        SYNTAX TruthValue
        MAX-ACCESS read-only
        STATUS current
        DESCRIPTION "airMAX status - on/off"
        ::= { ubntAirMaxEntry 2 }

    ubntAirMaxQuality OBJECT-TYPE
        SYNTAX Integer32 (0..100)
        MAX-ACCESS read-only
        STATUS current
        DESCRIPTION "airMAX quality - percentage"
        ::= { ubntAirMaxEntry 3 }

    ubntAirMaxCapacity OBJECT-TYPE
        SYNTAX Integer32 (0..100)
        MAX-ACCESS read-only
        STATUS current
        DESCRIPTION "airMAX capacity - percentage"
        ::= { ubntAirMaxEntry 4 }

    ubntAirMaxPriority OBJECT-TYPE
        SYNTAX INTEGER {
        high(0),
        medium(1),
        low(2),
        none(3)
    }
        MAX-ACCESS read-only
        STATUS current
        DESCRIPTION "airMAX priority - none/high/low/medium"
        ::= { ubntAirMaxEntry 5 }

    ubntAirMaxNoAck OBJECT-TYPE
        SYNTAX TruthValue
        MAX-ACCESS read-only
        STATUS current
        DESCRIPTION "airMAX NoACK mode - on/off"
        ::= { ubntAirMaxEntry 6 }

    -- --------------------------------------------------------------------------------
    --                            airSync table
    -- --------------------------------------------------------------------------------

    ubntAirSyncTable OBJECT-TYPE
        SYNTAX     SEQUENCE OF UbntAirSyncEntry
        MAX-ACCESS not-accessible
        STATUS     current
        DESCRIPTION "airSync protocol statistics"
        ::= { ubntAirMAX 3 }

    ubntAirSyncEntry OBJECT-TYPE
       SYNTAX     UbntAirSyncEntry
       MAX-ACCESS not-accessible
       STATUS     current
       DESCRIPTION "An entry in the ubntAirSyncTable"
       INDEX      { ubntAirSyncIfIndex }
       ::= { ubntAirSyncTable 1 }

    UbntAirSyncEntry ::= SEQUENCE {
        ubntAirSyncIfIndex    Integer32,
        ubntAirSyncMode       INTEGER,
        ubntAirSyncCount      Integer32,
        ubntAirSyncDownUtil   Integer32,
        ubntAirSyncUpUtil     Integer32
    }

    ubntAirSyncIfIndex OBJECT-TYPE
        SYNTAX     Integer32 (1..255)
        MAX-ACCESS not-accessible 
        STATUS     current
        DESCRIPTION "Index for the ubntAirSyncTable"
        ::= { ubntAirSyncEntry 1 }

    ubntAirSyncMode OBJECT-TYPE
        SYNTAX     INTEGER {
        disabled(0),
        master(1),
        slave(2)
    }
        MAX-ACCESS read-only
        STATUS     current
        DESCRIPTION "airSync mode - master/slave"
        ::= { ubntAirSyncEntry 2 }

    ubntAirSyncCount OBJECT-TYPE
        SYNTAX     Integer32 (0..255)
        MAX-ACCESS read-only
        STATUS     current
        DESCRIPTION "airSync client count"
        ::= { ubntAirSyncEntry 3 }

    ubntAirSyncDownUtil OBJECT-TYPE
        SYNTAX     Integer32 (0..100)
        MAX-ACCESS read-only
        STATUS     current
        DESCRIPTION "airSync down utilization"
        ::= { ubntAirSyncEntry 4 }

    ubntAirSyncUpUtil OBJECT-TYPE
        SYNTAX     Integer32 (0..100)
        MAX-ACCESS read-only
        STATUS     current
        DESCRIPTION "airSync up utilization"
        ::= { ubntAirSyncEntry 5 }

    -- --------------------------------------------------------------------------------
    --                            airSelect table
    -- --------------------------------------------------------------------------------

    ubntAirSelTable OBJECT-TYPE
        SYNTAX     SEQUENCE OF UbntAirSelEntry
        MAX-ACCESS not-accessible
        STATUS     current
        DESCRIPTION "airSelect protocol statistics"
        ::= { ubntAirMAX 4 }

    ubntAirSelEntry OBJECT-TYPE
       SYNTAX     UbntAirSelEntry
       MAX-ACCESS not-accessible
       STATUS     current
       DESCRIPTION "An entry in the ubntAirSelTable"
       INDEX      { ubntAirSelIfIndex }
       ::= { ubntAirSelTable 1 }

    UbntAirSelEntry ::= SEQUENCE {
        ubntAirSelIfIndex    Integer32,
        ubntAirSelEnabled    TruthValue,
        ubntAirSelInterval   Integer32
    }

    ubntAirSelIfIndex OBJECT-TYPE
        SYNTAX     Integer32 (1..255)
        MAX-ACCESS not-accessible 
        STATUS     current
        DESCRIPTION "Index for the ubntAirSelTable"
        ::= { ubntAirSelEntry 1 }

    ubntAirSelEnabled OBJECT-TYPE
        SYNTAX TruthValue
        MAX-ACCESS read-only
        STATUS current
        DESCRIPTION "airSelect status - on/off"
        ::= { ubntAirSelEntry 2 }

    ubntAirSelInterval OBJECT-TYPE
        SYNTAX     Integer32 (0..65535)
        MAX-ACCESS read-only
        STATUS     current
        DESCRIPTION "airSelect hop interval (miliseconds)"
        ::= { ubntAirSelEntry 3 }

    -- --------------------------------------------------------------------------------
    --                            wireless statistics table
    -- --------------------------------------------------------------------------------

    ubntWlStatTable OBJECT-TYPE
        SYNTAX     SEQUENCE OF UbntWlStatEntry
        MAX-ACCESS not-accessible
        STATUS     current
        DESCRIPTION "Wireless statistics"
        ::= { ubntAirMAX 5 }

    ubntWlStatEntry OBJECT-TYPE
       SYNTAX     UbntWlStatEntry
       MAX-ACCESS not-accessible
       STATUS     current
       DESCRIPTION "An entry in the ubntWlStatTable"
       INDEX      { ubntWlStatIndex }
       ::= { ubntWlStatTable 1 }

    UbntWlStatEntry ::= SEQUENCE {
        ubntWlStatIndex      Integer32,
        ubntWlStatSsid       DisplayString,
        ubntWlStatHideSsid   TruthValue,
        ubntWlStatApMac      MacAddress,
        ubntWlStatSignal     Integer32,
        ubntWlStatRssi       Integer32,
        ubntWlStatCcq        Integer32,
        ubntWlStatNoiseFloor Integer32,
        ubntWlStatTxRate     Integer32,
        ubntWlStatRxRate     Integer32,
        ubntWlStatSecurity   DisplayString,
        ubntWlStatWdsEnabled TruthValue,
        ubntWlStatApRepeater TruthValue,
        ubntWlStatChanWidth  Integer32,
        ubntWlStatStaCount   Gauge32
    }

    ubntWlStatIndex OBJECT-TYPE
        SYNTAX     Integer32 (1..255)
        MAX-ACCESS not-accessible 
        STATUS     current
        DESCRIPTION "Index for the ubntWlStatTable"
        ::= { ubntWlStatEntry 1 }

    ubntWlStatSsid OBJECT-TYPE
        SYNTAX     DisplayString
        MAX-ACCESS read-only
        STATUS     current
        DESCRIPTION "SSID"
        ::= { ubntWlStatEntry 2 }

    ubntWlStatHideSsid OBJECT-TYPE
        SYNTAX     TruthValue
        MAX-ACCESS read-only
        STATUS     current
        DESCRIPTION "Hide SSID - on/off"
        ::= { ubntWlStatEntry 3 }

    ubntWlStatApMac OBJECT-TYPE
        SYNTAX     MacAddress
        MAX-ACCESS read-only
        STATUS     current
        DESCRIPTION "AP MAC address"
        ::= { ubntWlStatEntry 4 }

    ubntWlStatSignal OBJECT-TYPE
        SYNTAX     Integer32
        MAX-ACCESS read-only
        STATUS     current
        DESCRIPTION "Signal strength, dBm"
        ::= { ubntWlStatEntry 5 }

    ubntWlStatRssi OBJECT-TYPE
        SYNTAX     Integer32
        MAX-ACCESS read-only
        STATUS     current
        DESCRIPTION "RSSI, dBm"
        ::= { ubntWlStatEntry 6 }

    ubntWlStatCcq OBJECT-TYPE
        SYNTAX     Integer32
        MAX-ACCESS read-only
        STATUS     current
        DESCRIPTION "CCQ in %"
        ::= { ubntWlStatEntry 7 }

    ubntWlStatNoiseFloor OBJECT-TYPE
        SYNTAX     Integer32
        MAX-ACCESS read-only
        STATUS     current
        DESCRIPTION "Noise floor"
        ::= { ubntWlStatEntry 8 }

    ubntWlStatTxRate OBJECT-TYPE
        SYNTAX     Integer32
        MAX-ACCESS read-only
        STATUS     current
        DESCRIPTION "TX rate"
        ::= { ubntWlStatEntry 9 }

    ubntWlStatRxRate OBJECT-TYPE
        SYNTAX     Integer32
        MAX-ACCESS read-only
        STATUS     current
        DESCRIPTION "RX rate"
        ::= { ubntWlStatEntry 10 }

    ubntWlStatSecurity OBJECT-TYPE
        SYNTAX     DisplayString
        MAX-ACCESS read-only
        STATUS     current
        DESCRIPTION "Wireless security mode"
        ::= { ubntWlStatEntry 11 }

    ubntWlStatWdsEnabled OBJECT-TYPE
        SYNTAX     TruthValue
        MAX-ACCESS read-only
        STATUS     current
        DESCRIPTION "WDS - on/off"
        ::= { ubntWlStatEntry 12 }

    ubntWlStatApRepeater OBJECT-TYPE
        SYNTAX     TruthValue
        MAX-ACCESS read-only
        STATUS     current
        DESCRIPTION "AP repeater - on/off"
        ::= { ubntWlStatEntry 13 }

    ubntWlStatChanWidth OBJECT-TYPE
        SYNTAX     Integer32
        MAX-ACCESS read-only
        STATUS     current
        DESCRIPTION "Channel Width"
        ::= { ubntWlStatEntry 14 }

    ubntWlStatStaCount OBJECT-TYPE
        SYNTAX     Gauge32
        MAX-ACCESS read-only
        STATUS     current
        DESCRIPTION "Station count"
        ::= { ubntWlStatEntry 15 }

    -- --------------------------------------------------------------------------------
    --                            station list table
    -- --------------------------------------------------------------------------------

    ubntStaTable OBJECT-TYPE
        SYNTAX     SEQUENCE OF UbntStaEntry
        MAX-ACCESS not-accessible
        STATUS     current
        DESCRIPTION "Station list"
        ::= { ubntAirMAX 7 }

    ubntStaEntry OBJECT-TYPE
        SYNTAX     UbntStaEntry
        MAX-ACCESS not-accessible
        STATUS     current
        DESCRIPTION "An entry in the ubntStaEntry"
        INDEX      { ubntWlStatIndex, ubntStaMac }
        ::= { ubntStaTable 1 }

    UbntStaEntry ::= SEQUENCE {
        ubntStaMac        MacAddress,
        ubntStaName       DisplayString,
        ubntStaSignal     Integer32,
        ubntStaNoiseFloor Integer32,
        ubntStaDistance   Integer32,
        ubntStaCcq        Integer32,
        ubntStaAmp        Integer32,
        ubntStaAmq        Integer32,
        ubntStaAmc        Integer32,
        ubntStaLastIp     IpAddress,
        ubntStaTxRate     Integer32,
        ubntStaRxRate     Integer32,
        ubntStaTxBytes    Counter64,
        ubntStaRxBytes    Counter64,
        ubntStaConnTime   TimeTicks,
        ubntStaLocalCINR  Integer32,
        ubntStaTxCapacity Integer32,
        ubntStaRxCapacity Integer32
    }

    ubntStaMac OBJECT-TYPE
        SYNTAX     MacAddress
        MAX-ACCESS not-accessible 
        STATUS     current
        DESCRIPTION "Station MAC address"
        ::= { ubntStaEntry 1 }

    ubntStaName OBJECT-TYPE
        SYNTAX     DisplayString
        MAX-ACCESS read-only
        STATUS     current
        DESCRIPTION "Station name"
        ::= { ubntStaEntry 2 }

    ubntStaSignal OBJECT-TYPE
        SYNTAX     Integer32
        MAX-ACCESS read-only
        STATUS     current
        DESCRIPTION "Signal strength, dBm"
        ::= { ubntStaEntry 3 }

    ubntStaNoiseFloor OBJECT-TYPE
        SYNTAX     Integer32
        MAX-ACCESS read-only
        STATUS     current
        DESCRIPTION "Noise floor"
        ::= { ubntStaEntry 4 }

    ubntStaDistance OBJECT-TYPE
        SYNTAX Integer32 (1..65535)
        MAX-ACCESS read-only
        STATUS current
        DESCRIPTION "Distance"
        ::= { ubntStaEntry 5 }

    ubntStaCcq OBJECT-TYPE
        SYNTAX     Integer32
        MAX-ACCESS read-only
        STATUS     current
        DESCRIPTION "CCQ in %"
        ::= { ubntStaEntry 6 }


    ubntStaAmp OBJECT-TYPE
        SYNTAX     Integer32
        MAX-ACCESS read-only
        STATUS     current
        DESCRIPTION "airMAX priority"
        ::= { ubntStaEntry 7 }

    ubntStaAmq OBJECT-TYPE
        SYNTAX     Integer32
        MAX-ACCESS read-only
        STATUS     current
        DESCRIPTION "airMAX quality"
        ::= { ubntStaEntry 8 }

    ubntStaAmc OBJECT-TYPE
        SYNTAX     Integer32
        MAX-ACCESS read-only
        STATUS     current
        DESCRIPTION "airMAX capacity"
        ::= { ubntStaEntry 9 }

    ubntStaLastIp OBJECT-TYPE
        SYNTAX     IpAddress
        MAX-ACCESS read-only
        STATUS     current
        DESCRIPTION "Last known IP address"
        ::= { ubntStaEntry 10 }

    ubntStaTxRate OBJECT-TYPE
        SYNTAX     Integer32
        MAX-ACCESS read-only
        STATUS     current
        DESCRIPTION "TX rate"
        ::= { ubntStaEntry 11 }

    ubntStaRxRate OBJECT-TYPE
        SYNTAX     Integer32
        MAX-ACCESS read-only
        STATUS     current
        DESCRIPTION "RX rate"
        ::= { ubntStaEntry 12 }

    ubntStaTxBytes OBJECT-TYPE
        SYNTAX     Counter64
        MAX-ACCESS read-only
        STATUS     current
        DESCRIPTION "TX bytes"
        ::= { ubntStaEntry 13 }

    ubntStaRxBytes OBJECT-TYPE
        SYNTAX     Counter64
        MAX-ACCESS read-only
        STATUS     current
        DESCRIPTION "TX rate"
        ::= { ubntStaEntry 14 }

    ubntStaConnTime OBJECT-TYPE
        SYNTAX     TimeTicks
        MAX-ACCESS read-only
        STATUS     current
        DESCRIPTION "Connection Time in seconds"
        ::= { ubntStaEntry 15 }

    ubntStaLocalCINR OBJECT-TYPE
        SYNTAX     Integer32
        MAX-ACCESS read-only
        STATUS     current
        DESCRIPTION "Local CINR"
        ::= { ubntStaEntry 16 }

    ubntStaTxCapacity OBJECT-TYPE
        SYNTAX     Integer32
        MAX-ACCESS read-only
        STATUS     current
        DESCRIPTION "Uplink Capacity in Kbps"
        ::= { ubntStaEntry 17 }

    ubntStaRxCapacity OBJECT-TYPE
        SYNTAX     Integer32
        MAX-ACCESS read-only
        STATUS     current
        DESCRIPTION "Downlink Capacity in Kbps"
        ::= { ubntStaEntry 18 }

    ubntAirMAXStatusGroup OBJECT-GROUP OBJECTS {
        ubntStaName,
        ubntStaSignal,
        ubntStaNoiseFloor,
        ubntStaDistance,
        ubntStaCcq,
        ubntStaAmp,
        ubntStaAmq,
        ubntStaAmc,
        ubntStaLastIp,
        ubntStaTxRate,
        ubntStaRxRate,
        ubntStaTxBytes,
        ubntStaRxBytes,
        ubntStaConnTime,
        ubntStaLocalCINR,
        ubntStaTxCapacity,
        ubntStaRxCapacity,
        ubntRadioMode,
        ubntRadioCCode,
        ubntRadioFreq,
        ubntRadioDfsEnabled,
        ubntRadioTxPower,
        ubntRadioDistance,
        ubntRadioChainmask,
        ubntRadioAntenna,
        ubntRadioRssi,
        ubntRadioRssiMgmt,
        ubntRadioRssiExt,
        ubntAirMaxEnabled,
        ubntAirMaxQuality,
        ubntAirMaxCapacity,
        ubntAirMaxPriority,
        ubntAirMaxNoAck,
        ubntAirSyncMode,
        ubntAirSyncCount,
        ubntAirSyncDownUtil,
        ubntAirSyncUpUtil,
        ubntAirSelEnabled,
        ubntAirSelInterval,
        ubntWlStatSsid,
        ubntWlStatHideSsid,
        ubntWlStatApMac,
        ubntWlStatSignal,
        ubntWlStatRssi,
        ubntWlStatCcq,
        ubntWlStatNoiseFloor,
        ubntWlStatTxRate,
        ubntWlStatRxRate,
        ubntWlStatSecurity,
        ubntWlStatWdsEnabled,
        ubntWlStatApRepeater,
        ubntWlStatChanWidth,
        ubntWlStatStaCount }
        STATUS current
        DESCRIPTION "Status and statistics for AirMax monitoring"
        ::= { ubntAirosGroups 1 }

    ubntAirMAXStatusCompliance MODULE-COMPLIANCE
        STATUS current
        DESCRIPTION "The compliance statement for Ubiquiti AirMax entities."
        MODULE
            GROUP ubntAirMAXStatusGroup
            DESCRIPTION "This group is for Ubiquiti systems."
        ::= { ubntAirosGroups 2 }

END


File: /dude_custom_files\UBNT-MIB.txt
UBNT-MIB DEFINITIONS ::= BEGIN
    IMPORTS
        MODULE-IDENTITY, OBJECT-TYPE, Integer32, enterprises FROM SNMPv2-SMI
        DisplayString FROM SNMPv2-TC
        OBJECT-GROUP, MODULE-COMPLIANCE FROM SNMPv2-CONF;

    ubntMIB MODULE-IDENTITY
    LAST-UPDATED "201402270000Z"
    ORGANIZATION "Ubiquiti Networks, Inc."
    CONTACT-INFO "support@ubnt.com"
    DESCRIPTION  "The MIB module for Ubiquiti Networks, Inc. entities"
    REVISION "201402270000Z"
    DESCRIPTION "Split revision"
    ::= { ubnt 1 }

    -- --------------------------------------------------------------------------------
    --                         Ubiquiti Networks Root
    -- --------------------------------------------------------------------------------

    ubnt OBJECT IDENTIFIER ::= { enterprises 41112 }

    -- --------------------------------------------------------------------------------
    --                         Ubiquiti Networks SNMP Information
    -- --------------------------------------------------------------------------------

    ubntSnmpInfo OBJECT IDENTIFIER ::= { ubntMIB 2 }
    ubntSnmpGroups OBJECT IDENTIFIER ::= { ubntSnmpInfo 1}
    ubntAirosGroups OBJECT IDENTIFIER ::= { ubntSnmpInfo 2}
    ubntAirFiberGroups OBJECT IDENTIFIER ::= { ubntSnmpInfo 3}
    ubntEdgeMaxGroups OBJECT IDENTIFIER ::= { ubntSnmpInfo 4}
    ubntUniFiGroups OBJECT IDENTIFIER ::= { ubntSnmpInfo 5}
    ubntAirVisionGroups OBJECT IDENTIFIER ::= { ubntSnmpInfo 6}
    ubntMFiGroups OBJECT IDENTIFIER ::= { ubntSnmpInfo 7}
    ubntUniTelGroups OBJECT IDENTIFIER ::= { ubntSnmpInfo 8}

    -- --------------------------------------------------------------------------------
    --                         Ubiquiti Networks Products
    -- --------------------------------------------------------------------------------
    
    ubntAirFIBER OBJECT IDENTIFIER ::= { ubntMIB 3 }
    ubntEdgeMax OBJECT IDENTIFIER ::= { ubntMIB 5 }
    ubntUniFi OBJECT IDENTIFIER ::= { ubntMIB 6 }
    ubntAirVision OBJECT IDENTIFIER ::= { ubntMIB 7 }
    ubntMFi OBJECT IDENTIFIER ::= { ubntMIB 8 }
    ubntUniTel OBJECT IDENTIFIER ::= { ubntMIB 9 }

    -- --------------------------------------------------------------------------------
    --                         Ubiquiti Networks OR table
    -- --------------------------------------------------------------------------------

    ubntORTable OBJECT-TYPE
        SYNTAX     SEQUENCE OF UbntOREntry
        MAX-ACCESS not-accessible
        STATUS     current
        DESCRIPTION "Capabilities"
        ::= { ubntMIB 1 }

    ubntOREntry OBJECT-TYPE
       SYNTAX     UbntOREntry
       MAX-ACCESS not-accessible
       STATUS     current
       DESCRIPTION "An entry in the ubntORTable"
       INDEX      { ubntORIndex }
       ::= { ubntORTable 1 }

    UbntOREntry ::= SEQUENCE {
        ubntORIndex     Integer32,
        ubntORID        OBJECT IDENTIFIER,
        ubntORDescr     DisplayString
    }

    ubntORIndex OBJECT-TYPE
        SYNTAX     Integer32 (1..255)
        MAX-ACCESS not-accessible
        STATUS     current
        DESCRIPTION "Index for the ubntORTable"
        ::= { ubntOREntry 1 }

    ubntORID OBJECT-TYPE
        SYNTAX     OBJECT IDENTIFIER
        MAX-ACCESS read-only
        STATUS     current
        DESCRIPTION "OR ID"
        ::= { ubntOREntry 2 }

    ubntORDescr OBJECT-TYPE
        SYNTAX     DisplayString
        MAX-ACCESS read-only
        STATUS     current
        DESCRIPTION "Description of idenfifier"
        ::= { ubntOREntry 3 }

    ubntORInfoGroup OBJECT-GROUP
        OBJECTS { ubntORID,
                  ubntORDescr }
        STATUS current
        DESCRIPTION "Collection of related objects"
        ::= { ubntSnmpGroups 1 }

    ubntORCompliance MODULE-COMPLIANCE
        STATUS current
        DESCRIPTION "The compliance statement for Ubiquiti entities."
        MODULE
            GROUP ubntORInfoGroup
            DESCRIPTION "This group is for Ubiquiti systems."
        ::= { ubntSnmpGroups 2 }

END


File: /fur_elise_unfinished
# this is a silly beep script that sounds pretty close to fur elise, not entirely finished however
:beep frequency=329.63 length=300;
:delay 0.350;
:beep frequency=311.13 length=300;
:delay 0.350;
:beep frequency=329.63 length=300;
:delay 0.350;
:beep frequency=311.13 length=300;
:delay 0.350;
:beep frequency=329.63 length=300;
:delay 0.350;
:beep frequency=246.94 length=300;
:delay 0.400;
:beep frequency=293.66 length=300;
:delay 0.400;
:beep frequency=261.63 length=300;
:delay 0.400;
:beep frequency=220 length=900;
:delay 0.1000;
:beep frequency=146.83 length=300;
:delay 0.350;
:beep frequency=174.61 length=300;
:delay 0.400;
:beep frequency=220 length=300;
:delay 0.400;
:beep frequency=246.94 length=900;
:delay 0.1000;
:beep frequency=174.61 length=300;
:delay 0.400;
:beep frequency=233.08 length=300;
:delay 0.400;
:beep frequency=246.94 length=300;
:delay 0.400;
:beep frequency=261.63 length=900;
:delay 0.1000;
:beep frequency=329.63 length=300;
:delay 0.400;
:beep frequency=311.13 length=300;
:delay 0.400;
:beep frequency=329.63 length=300;
:delay 0.400;
:beep frequency=311.13 length=300;
:delay 0.400;
:beep frequency=329.63 length=300;
:delay 0.400;
:beep frequency=246.94 length=300;
:delay 0.400;
:beep frequency=293.66 length=300;
:delay 0.400;
:beep frequency=261.63 length=300;
:delay 0.400;
:beep frequency=220 length=900;
:delay 0.1000;
:beep frequency=146.83 length=300;
:delay 0.400;
:beep frequency=174.61 length=300;
:delay 0.400;
:beep frequency=220 length=300;
:delay 0.400;
:beep frequency=246.94 length=900;
:delay 0.1000;
:beep frequency=174.61 length=300;
:delay 0.400;
:beep frequency=261.63 length=300;
:delay 0.400;
:beep frequency=246.94 length=300;
:delay 0.400;
:beep frequency=220 length=900;
:delay 0.1000;
:beep frequency=246.94 length=300;
:delay 0.400;
:beep frequency=261.63 length=300;
:delay 0.400;
:beep frequency=293.66 length=300;
:delay 0.400;
:beep frequency=329.63 length=900;
:delay 0.1000;
:beep frequency=196 length=300;
:delay 0.400;
:beep frequency=349.23 length=300;
:delay 0.400;
:beep frequency=329.23 length=300;
:delay 0.400;
:beep frequency=293.63 length=900;
:delay 0.1000;
:beep frequency=164.81 length=300;
:delay 0.400;
:beep frequency=329.63 length=300;
:delay 0.400;
:beep frequency=293.63 length=300;
:delay 0.400;
:beep frequency=261.63 length=900;
:delay 0.1000;
:beep frequency=146.83 length=300;
:delay 0.400;
:beep frequency=293.63 length=300;
:delay 0.400;
:beep frequency=261.63 length=300;
:delay 0.400;
:beep frequency=246.94 length=900;
:delay 0.1000;
:beep frequency=329.63 length=300;
:delay 0.400;
:beep frequency=311.13 length=300;
:delay 0.350;
:beep frequency=329.63 length=300;
:delay 0.350;
:beep frequency=311.13 length=300;
:delay 0.350;
:beep frequency=329.63 length=300;
:delay 0.350;
:beep frequency=246.94 length=300;
:delay 0.400;
:beep frequency=293.66 length=300;
:delay 0.400;
:beep frequency=261.63 length=300;
:delay 0.400;
:beep frequency=220 length=900;
:delay 0.1000;
:beep frequency=146.83 length=300;
:delay 0.350;
:beep frequency=174.61 length=300;
:delay 0.400;
:beep frequency=220 length=300;
:delay 0.400;
:beep frequency=246.94 length=900;
:delay 0.1000;
:beep frequency=174.61 length=300;
:delay 0.400;
:beep frequency=233.08 length=300;
:delay 0.400;
:beep frequency=246.94 length=300;
:delay 0.400;
:beep frequency=261.63 length=900;
:delay 0.1000;
:beep frequency=329.63 length=300;
:delay 0.400;
:beep frequency=311.13 length=300;
:delay 0.400;
:beep frequency=329.63 length=300;
:delay 0.400;
:beep frequency=311.13 length=300;
:delay 0.400;
:beep frequency=329.63 length=300;
:delay 0.400;
:beep frequency=246.94 length=300;
:delay 0.400;
:beep frequency=293.66 length=300;
:delay 0.400;
:beep frequency=261.63 length=300;
:delay 0.400;
:beep frequency=220 length=900;
:delay 0.1000;
:beep frequency=146.83 length=300;
:delay 0.400;
:beep frequency=174.61 length=300;
:delay 0.400;
:beep frequency=220 length=300;
:delay 0.400;
:beep frequency=246.94 length=900;
:delay 0.1000;
:beep frequency=174.61 length=300;
:delay 0.400;
:beep frequency=261.63 length=300;
:delay 0.400;
:beep frequency=246.94 length=300;
:delay 0.400;
:beep frequency=220 length=900;
:delay 0.1000;


File: /mikrotik_backup_script
:local sysname [/system identity get name]
:local datetime "$[/system clock get date] $[/system clock get time]"

/system backup save name="$sysname";
/tool e-mail send to="<REDACTED, YOUR EMAIL GOES HERE>" subject=([/system identity get name]." backup") file="$sysname.backup" body="$sysname \n $datetime \n Backup completed.";
:log info "Backup e-mail sent.";


File: /README.md
# EC-MikroTik-Materials
my collection of MikroTik RouterOS samples, scripts, and otherwise related materials


