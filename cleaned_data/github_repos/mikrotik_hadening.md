# Repository Information
Name: mikrotik_hadening

# Directory Structure
Directory structure:
└── github_repos/mikrotik_hadening/
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
    │   │       ├── pack-36d2c4d346f985d81877c4ecc1d2cc22ab4855cc.idx
    │   │       └── pack-36d2c4d346f985d81877c4ecc1d2cc22ab4855cc.pack
    │   ├── packed-refs
    │   └── refs/
    │       ├── heads/
    │       │   └── main
    │       ├── remotes/
    │       │   └── origin/
    │       │       └── HEAD
    │       └── tags/
    ├── address-lists.rsc
    ├── Changelog.md
    ├── env-bkp.rsc
    ├── filter-forward.rsc
    ├── filter-input.rsc
    ├── install.rsc
    ├── interface-list.rsc
    ├── loganalytic.rsc
    ├── preinstall.rsc
    ├── README.md
    ├── router-enviroment.rsc
    ├── routes-v6.rsc
    ├── routes-v7.rsc
    ├── script-scheduler.rsc
    ├── system.rsc
    ├── unninstall.rsc
    └── version.txt


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
	url = https://github.com/facubertran/mikrotik_hadening.git
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
0000000000000000000000000000000000000000 2b1ac9fc1fcb6f604b3d711faf06447474da5ef3 vivek-dodia <vivek.dodia@icloud.com> 1738606300 -0500	clone: from https://github.com/facubertran/mikrotik_hadening.git


File: /.git\logs\refs\heads\main
0000000000000000000000000000000000000000 2b1ac9fc1fcb6f604b3d711faf06447474da5ef3 vivek-dodia <vivek.dodia@icloud.com> 1738606300 -0500	clone: from https://github.com/facubertran/mikrotik_hadening.git


File: /.git\logs\refs\remotes\origin\HEAD
0000000000000000000000000000000000000000 2b1ac9fc1fcb6f604b3d711faf06447474da5ef3 vivek-dodia <vivek.dodia@icloud.com> 1738606300 -0500	clone: from https://github.com/facubertran/mikrotik_hadening.git


File: /.git\packed-refs
# pack-refs with: peeled fully-peeled sorted 
2b1ac9fc1fcb6f604b3d711faf06447474da5ef3 refs/remotes/origin/main
8acf3c649fa20ae7b6344c9181b3bc30910d3ea3 refs/tags/6.1
eee09984dacac58b95233c5313faa24f52f1b950 refs/tags/6.2


File: /.git\refs\heads\main
2b1ac9fc1fcb6f604b3d711faf06447474da5ef3


File: /.git\refs\remotes\origin\HEAD
ref: refs/remotes/origin/main


File: /address-lists.rsc
#Variables globales
:global redespublicas; :global publicasdentrodelared; :global redesdeorigenpermitidas; :global origenespermitidosnewnodnat;
#
:global testvelocidadlb;:global bgplb;:global dnslb;:global snmplb;:global winboxlb;:global apilb;
:global sshlb;:global httplb;:global ntplb;:global radiuslb;:global sockslb;:global l2tplb;
:global pptplb;:global grelb;:global ipseclb;:global webproxylb;
#
:global testvelocidadln;:global bgpln;:global dnsln;:global snmpln;:global winboxln;:global apiln;
:global sshln;:global httpln;:global ntpln;:global radiusln;:global socksln;:global l2tpln;
:global pptpln;:global greln;:global ipsecln;:global webproxyln;
##Menu address-list
/ip firewall address-list
##Redes que se permiten navegar
/ip firewall address-list remove [find list=F_OrigenesPermitidos]
:do {add address=10.0.0.0/8 list=F_OrigenesPermitidos} on-error={
    :put "INFO - El address-list address=10.0.0.0/8 list=F_OrigenesPermitidos ya existe o no se puede crear"
}
:do {add address=172.16.0.0/12 list=F_OrigenesPermitidos} on-error={
    :put "INFO - El address-list address=172.16.0.0/12 list=F_OrigenesPermitidos ya existe o no se puede crear"
}
:do {add address=192.168.0.0/16 list=F_OrigenesPermitidos} on-error={
    :put "INFO - El address-list address=192.168.0.0/16 list=F_OrigenesPermitidos ya existe o no se puede crear"
}
:do {add address=100.64.0.0/10 list=F_OrigenesPermitidos} on-error={
    :put "INFO - El address-list address=192.168.0.0/16 list=F_OrigenesPermitidos ya existe o no se puede crear"
}
##Redes que se permiten navegar personalizadas
:if ([:pick $redesdeorigenpermitidas] != "") do={
    :foreach alpp in=$redesdeorigenpermitidas do={
        :do {/ip firewall address-list add list=F_OrigenesPermitidos address=$alpp
        } on-error={
            :put "INFO - El address-list address=$alpp list=F_OrigenesPermitidos ya existe o no se puede crear";
        }
    }
}
##Origienes que se permiten establecer conexion del exterior sin dnat
:if ([:pick $origenespermitidosnewnodnat] != "") do={
    :foreach alpp in=$origenespermitidosnewnodnat do={
        :do {/ip firewall address-list add list=F_OrigenesPermitidosNewNoDnat address=$alpp
        } on-error={
            :put "INFO - El address-list address=$alpp list=F_OrigenesPermitidosNewNoDnat ya existe o no se puede crear";
        }
    }
}
##Redes publicas propias
/ip firewall address-list remove [find list=FN_RedesPublicasPropias]
:if ([:pick $redespublicas] != "") do={
    :foreach alpp in=$redespublicas do={
        :do {/ip firewall address-list add list=FN_RedesPublicasPropias address=$alpp
        } on-error={
            :put "INFO - El address-list address=$alpp list=FN_RedesPublicasPropias ya existe o no se puede crear"
        }
    }
    :foreach alpp in=$redespublicas do={
        :do {/ip firewall address-list add list=F_OrigenesPermitidos address=$alpp
        } on-error={
            :put "INFO - El address-list address=$alpp list=F_OrigenesPermitidos ya existe o no se puede crear"
        }
    }
}
##Publicas dentro de la red a bloquear
/ip firewall address-list remove [find list=F_ProteccionPublicasDentroDeLaRed]
:if ([:pick $publicasdentrodelared] != "") do={
    :foreach alpp in=$publicasdentrodelared do={
        :do {/ip firewall address-list add list=F_ProteccionPublicasDentroDeLaRed address=$alpp
        } on-error={
            :put "INFO - El address-list address=$alpp list=F_ProteccionPublicasDentroDeLaRed ya existe o no se puede crear"
        }
    }
}
##TestVelocidad
/ip firewall address-list remove [find list=F_ListaNegraTestVelocidad]
:if ([:pick $testvelocidadln] != "") do={
    :foreach alpp in=$testvelocidadln do={
        :do {/ip firewall address-list add list=F_ListaNegraTestVelocidad address=$alpp
        } on-error={
            :put "INFO - El address-list address=$alpp list=F_ListaBlancaTestVelocidad ya existe o no se puede crear"
        }
    }
}
/ip firewall address-list remove [find list=F_ListaBlancaTestVelocidad]
:if ([:pick $testvelocidadlb] != "") do={
    :foreach alpp in=$testvelocidadlb do={
        :do {/ip firewall address-list add list=F_ListaBlancaTestVelocidad address=$alpp
        } on-error={
            :put "INFO - El address-list address=$alpp list=F_ListaBlancaTestVelocidad ya existe o no se puede crear"
        }
    }
}
##BGP
/ip firewall address-list remove [find list=F_ListaNegraBGP]
:if ([:pick $bgpln] != "") do={
    :foreach alpp in=$bgpln do={
        :do {/ip firewall address-list add list=F_ListaNegraBGP address=$alpp
        } on-error={
            :put "INFO - El address-list address=$alpp list=F_ListaBlancaBGP ya existe o no se puede crear"
        }
    }
}
/ip firewall address-list remove [find list=F_ListaBlancaBGP]
:if ([:pick $bgplb] != "") do={
    :foreach alpp in=$bgplb do={
        :do {/ip firewall address-list add list=F_ListaBlancaBGP address=$alpp
        } on-error={
            :put "INFO - El address-list address=$alpp list=F_ListaBlancaBGP ya existe o no se puede crear"
        }
    }
}
##DNS
/ip firewall address-list remove [find list=F_ListaNegraDNS]
:if ([:pick $dnsln] != "") do={
    :foreach alpp in=$dnsln do={
        :do {/ip firewall address-list add list=F_ListaNegraDNS address=$alpp
        } on-error={
            :put "INFO - El address-list address=$alpp list=F_ListaBlancaDNS ya existe o no se puede crear"
        }
    }
}
/ip firewall address-list remove [find list=F_ListaBlancaDNS]
:if ([:pick $dnslb] != "") do={
    :foreach alpp in=$dnslb do={
        :do {/ip firewall address-list add list=F_ListaBlancaDNS address=$alpp
        } on-error={
            :put "INFO - El address-list address=$alpp list=F_ListaBlancaDNS ya existe o no se puede crear"
        }
    }
}
##SNMP
/ip firewall address-list remove [find list=F_ListaNegraSNMP]
:if ([:pick $snmpln] != "") do={
    :foreach alpp in=$snmpln do={
        :do {/ip firewall address-list add list=F_ListaNegraSNMP address=$alpp
        } on-error={
            :put "INFO - El address-list address=$alpp list=F_ListaBlancaSNMP ya existe o no se puede crear"
        }
    }
}
/ip firewall address-list remove [find list=F_ListaBlancaSNMP]
:if ([:pick $snmplb] != "") do={
    :foreach alpp in=$snmplb do={
        :do {/ip firewall address-list add list=F_ListaBlancaSNMP address=$alpp
        } on-error={
            :put "INFO - El address-list address=$alpp list=F_ListaBlancaSNMP ya existe o no se puede crear"
        }
    }
}
##Winbox
/ip firewall address-list remove [find list=F_ListaNegraWinbox]
:if ([:pick $winboxln] != "") do={
    :foreach alpp in=$winboxln do={
        :do {/ip firewall address-list add list=F_ListaNegraWinbox address=$alpp
        } on-error={
            :put "INFO - El address-list address=$alpp list=F_ListaBlancaWinbox ya existe o no se puede crear"
        }
    }
}
/ip firewall address-list remove [find list=F_ListaBlancaWinbox]
:if ([:pick $winboxlb] != "") do={
    :foreach alpp in=$winboxlb do={
        :do {/ip firewall address-list add list=F_ListaBlancaWinbox address=$alpp
        } on-error={
            :put "INFO - El address-list address=$alpp list=F_ListaBlancaWinbox ya existe o no se puede crear"
        }
    }
}
##API
/ip firewall address-list remove [find list=F_ListaNegraAPI]
:if ([:pick $apiln] != "") do={
    :foreach alpp in=$apiln do={
        :do {/ip firewall address-list add list=F_ListaNegraAPI address=$alpp
        } on-error={
            :put "INFO - El address-list address=$alpp list=F_ListaBlancaAPI ya existe o no se puede crear"
        }
    }
}
/ip firewall address-list remove [find list=F_ListaBlancaAPI]
:if ([:pick $apilb] != "") do={
    :foreach alpp in=$apilb do={
        :do {/ip firewall address-list add list=F_ListaBlancaAPI address=$alpp
        } on-error={
            :put "INFO - El address-list address=$alpp list=F_ListaBlancaAPI ya existe o no se puede crear"
        }
    }
}
##HTTP
/ip firewall address-list remove [find list=F_ListaNegraHTTP]
:if ([:pick $httpln] != "") do={
    :foreach alpp in=$httpln do={
        :do {/ip firewall address-list add list=F_ListaNegraHTTP address=$alpp
        } on-error={
            :put "INFO - El address-list address=$alpp list=F_ListaBlancaHTTP ya existe o no se puede crear"
        }
    }
}
/ip firewall address-list remove [find list=F_ListaBlancaHTTP]
:if ([:pick $httplb] != "") do={
    :foreach alpp in=$httplb do={
        :do {/ip firewall address-list add list=F_ListaBlancaHTTP address=$alpp
        } on-error={
            :put "INFO - El address-list address=$alpp list=F_ListaBlancaHTTP ya existe o no se puede crear"
        }
    }
}
##SSH
/ip firewall address-list remove [find list=F_ListaNegraSSH]
:if ([:pick $sshln] != "") do={
    :foreach alpp in=$sshln do={
        :do {/ip firewall address-list add list=F_ListaNegraSSH address=$alpp
        } on-error={
            :put "INFO - El address-list address=$alpp list=F_ListaBlancaSSH ya existe o no se puede crear"
        }
    }
}
/ip firewall address-list remove [find list=F_ListaBlancaSSH]
:if ([:pick $sshlb] != "") do={
    :foreach alpp in=$sshlb do={
        :do {/ip firewall address-list add list=F_ListaBlancaSSH address=$alpp
        } on-error={
            :put "INFO - El address-list address=$alpp list=F_ListaBlancaSSH ya existe o no se puede crear"
        }
    }
}
##NTP
/ip firewall address-list remove [find list=F_ListaNegraNTP]
:if ([:pick $ntpln] != "") do={
    :foreach alpp in=$ntpln do={
        :do {/ip firewall address-list add list=F_ListaNegraNTP address=$alpp
        } on-error={
            :put "INFO - El address-list address=$alpp list=F_ListaBlancaNTP ya existe o no se puede crear"
        }
    }
}
/ip firewall address-list remove [find list=F_ListaBlancaNTP]
:if ([:pick $ntplb] != "") do={
    :foreach alpp in=$ntplb do={
        :do {/ip firewall address-list add list=F_ListaBlancaNTP address=$alpp
        } on-error={
            :put "INFO - El address-list address=$alpp list=F_ListaBlancaNTP ya existe o no se puede crear"
        }
    }
}
##RADIUS
/ip firewall address-list remove [find list=F_ListaNegraRADIUS]
:if ([:pick $radiusln] != "") do={
    :foreach alpp in=$radiusln do={
        :do {/ip firewall address-list add list=F_ListaNegraRADIUS address=$alpp
        } on-error={
            :put "INFO - El address-list address=$alpp list=F_ListaBlancaRADIUS ya existe o no se puede crear"
        }
    }
}
/ip firewall address-list remove [find list=F_ListaBlancaRADIUS]
:if ([:pick $radiuslb] != "") do={
    :foreach alpp in=$radiuslb do={
        :do {/ip firewall address-list add list=F_ListaBlancaRADIUS address=$alpp
        } on-error={
            :put "INFO - El address-list address=$alpp list=F_ListaBlancaRADIUS ya existe o no se puede crear"
        }
    }
}
##SOCKS
/ip firewall address-list remove [find list=F_ListaNegraSOCKS]
:if ([:pick $socksln] != "") do={
    :foreach alpp in=$socksln do={
        :do {/ip firewall address-list add list=F_ListaNegraSOCKS address=$alpp
        } on-error={
            :put "INFO - El address-list address=$alpp list=F_ListaBlancaSOCKS ya existe o no se puede crear"
        }
    }
}
/ip firewall address-list remove [find list=F_ListaBlancaSOCKS]
:if ([:pick $sockslb] != "") do={
    :foreach alpp in=$sockslb do={
        :do {/ip firewall address-list add list=F_ListaBlancaSOCKS address=$alpp
        } on-error={
        :put "INFO - El address-list address=$alpp list=F_ListaBlancaSOCKS ya existe o no se puede crear"
        }
    }
}
##L2TP
/ip firewall address-list remove [find list=F_ListaNegraL2TP]
:if ([:pick $l2tpln] != "") do={
    :foreach alpp in=$l2tpln do={
        :do {/ip firewall address-list add list=F_ListaNegraL2TP address=$alpp
        } on-error={
            :put "INFO - El address-list address=$alpp list=F_ListaBlancaL2TP ya existe o no se puede crear"
        }
    }
}
/ip firewall address-list remove [find list=F_ListaBlancaL2TP]
:if ([:pick $l2tplb] != "") do={
    :foreach alpp in=$l2tplb do={
        :do {/ip firewall address-list add list=F_ListaBlancaL2TP address=$alpp
        } on-error={
            :put "INFO - El address-list address=$alpp list=F_ListaBlancaL2TP ya existe o no se puede crear"
        }
    }
}
##PPTP
/ip firewall address-list remove [find list=F_ListaNegraPPTP]
:if ([:pick $pptpln] != "") do={
    :foreach alpp in=$pptpln do={
        :do {/ip firewall address-list add list=F_ListaNegraPPTP address=$alpp
        } on-error={
            :put "INFO - El address-list address=$alpp list=F_ListaBlancaPPTP ya existe o no se puede crear"
        }
    }
}
/ip firewall address-list remove [find list=F_ListaBlancaPPTP]
:if ([:pick $pptplb] != "") do={
    :foreach alpp in=$pptplb do={
        :do {/ip firewall address-list add list=F_ListaBlancaPPTP address=$alpp
        } on-error={
            :put "INFO - El address-list address=$alpp list=F_ListaBlancaPPTP ya existe o no se puede crear"
        }
    }
}
##GRE
/ip firewall address-list remove [find list=F_ListaNegraGRE]
:if ([:pick $greln] != "") do={
    :foreach alpp in=$greln do={
        :do {/ip firewall address-list add list=F_ListaNegraGRE address=$alpp
        } on-error={
            :put "INFO - El address-list address=$alpp list=F_ListaBlancaGRE ya existe o no se puede crear"
        }
    }
}
/ip firewall address-list remove [find list=F_ListaBlancaGRE]
:if ([:pick $grelb] != "") do={
    :foreach alpp in=$grelb do={
        :do {/ip firewall address-list add list=F_ListaBlancaGRE address=$alpp
        } on-error={
            :put "INFO - El address-list address=$alpp list=F_ListaBlancaGRE ya existe o no se puede crear"
        }
    }
}
##IPSEC
/ip firewall address-list remove [find list=F_ListaNegraIPSEC]
:if ([:pick $ipsecln] != "") do={
    :foreach alpp in=$ipsecln do={
        :do {/ip firewall address-list add list=F_ListaNegraIPSEC address=$alpp
        } on-error={
            :put "INFO - El address-list address=$alpp list=F_ListaBlancaIPSEC ya existe o no se puede crear"
        }
    }
}
/ip firewall address-list remove [find list=F_ListaBlancaIPSEC]
:if ([:pick $ipseclb] != "") do={
    :foreach alpp in=$ipseclb do={
        :do {/ip firewall address-list add list=F_ListaBlancaIPSEC address=$alpp
        } on-error={
            :put "INFO - El address-list address=$alpp list=F_ListaBlancaIPSEC ya existe o no se puede crear"
        }
    }
}
##WebProxy
/ip firewall address-list remove [find list=F_ListaNegraWebProxy]
:if ([:pick $webproxyln] != "") do={
    :foreach alpp in=$webproxyln do={
        :do {/ip firewall address-list add list=F_ListaNegraWebProxy address=$alpp
        } on-error={
            :put "INFO - El address-list address=$alpp list=F_ListaNegraWebProxy ya existe o no se puede crear"
        }
    }
}
/ip firewall address-list remove [find list=F_ListaBlancaWebProxy]
:if ([:pick $webproxylb] != "") do={
    :foreach alpp in=$webproxylb do={
        :do {/ip firewall address-list add list=F_ListaBlancaWebProxy address=$alpp
        } on-error={
            :put "INFO - El address-list address=$alpp list=F_ListaBlancaWebProxy ya existe o no se puede crear"
        }
    }
}

File: /Changelog.md
# Version 6.5 - 29/09/2021
* Internal interfaces excluir dinamicas
* Lista negra vpn siempre se crea
* Lista negra gral opcional, configurable en enviroment
* Esenario equipos privados despues del firewall, nueva lista de permitir x origenges
* Configuracion para habilitar o no scheduler api log
* Problemas al generar el script EdgeHardeningEnviroment_Crenein

# Version 6.4 - 19/07/2021
* Correccion port knoking

# Version 6.3 - 15/07/2021
* Ahora se pueden definir listas de IPs Blancas y Negras para cada servicio admás de las Interfaces Lists.
* Se optimizó la creacion de filters. Solo se crean las reglas que tengan alguna configuracón.
* Se incorporó la creación de un scheduler de reconocimiento de login fallido API. Este crea una lista de las IPs atacantes.
* Se agrego la red 100.64.0.0/10 como bogons configurable.
* Se corrigio un error al crear los filtros para web-proxy. Si el proxy tiene 2 puertos configurados, la regla se creaba erroneamente.

File: /filter-forward.rsc
:global smtp;
/ip firewall filter
add action=accept chain=forward comment=DeshabilitarFirewal_Crenein disabled=no
add action=passthrough chain=forward comment="Proteccion de Forward - Crenein v6.5"
add action=jump chain=forward comment=ProteccionPublicasDentroDeLaRed_Crenein \
    dst-address-list=F_ProteccionPublicasDentroDeLaRed jump-target=\
    ProteccionPublicasDentroDeLaRed_Crenein
add action=accept chain=ProteccionPublicasDentroDeLaRed_Crenein disabled=yes
add action=drop chain=ProteccionPublicasDentroDeLaRed_Crenein
add action=jump chain=forward comment=ProteccionForwardEntrada_Crenein \
    in-interface-list=InterfacesExternas jump-target=ProteccionForwardEntrada_Crenein
add action=drop chain=ProteccionForwardEntrada_Crenein src-address-list=\
    F_ListaNegraGeneral
add action=accept chain=ProteccionForwardEntrada_Crenein connection-state=\
    established,related,new dst-address-list=FN_RedesPublicasPropias
add action=accept chain=ProteccionForwardEntrada_Crenein connection-state=\
    established,related,new src-address-list=F_OrigenesPermitidosNewNoDnat
add action=accept chain=ProteccionForwardEntrada_Crenein connection-state=\
    established,related
add action=drop chain=ProteccionForwardEntrada_Crenein connection-nat-state=!dstnat \
    connection-state=new
add action=drop chain=ProteccionForwardEntrada_Crenein connection-state=invalid \
    protocol=tcp
add action=drop chain=ProteccionForwardEntrada_Crenein connection-state=invalid
add action=jump chain=forward comment=ProteccionSMTP_Crenein dst-port=\
    25,110,465,587,995,143,993 jump-target=ProteccionSMTP_Crenein protocol=tcp
add action=drop chain=ProteccionSMTP_Crenein src-address-list=F_ListaNegraSMTP
add action=accept chain=ProteccionSMTP_Crenein src-address-list=F_ListaBlancaSMTP
:if ($smtp = 1) do={add action=drop chain=ProteccionSMTP_Crenein disabled=no} \
else={add action=drop chain=ProteccionSMTP_Crenein disabled=yes}
add action=jump chain=forward comment=ProteccionForwardSalida_Crenein jump-target=\
    ProteccionForwardSalida_Crenein out-interface-list=InterfacesExternas
add action=drop chain=ProteccionForwardSalida_Crenein src-address-list=\
    !F_OrigenesPermitidos
add action=drop chain=ProteccionForwardSalida_Crenein dst-address-list=\
    F_ListaNegraGeneral
add action=accept chain=ProteccionForwardSalida_Crenein connection-state=\
    established,related,new src-address-list=FN_RedesPublicasPropias
add action=accept chain=ProteccionForwardSalida_Crenein connection-state=\
    established,related,new dst-address-list=F_OrigenesPermitidosNewNoDnat
add action=accept chain=ProteccionForwardSalida_Crenein connection-state=\
    established,related
add action=drop chain=ProteccionForwardSalida_Crenein connection-state=invalid \
    protocol=tcp
add action=drop chain=ProteccionForwardSalida_Crenein connection-state=invalid


File: /filter-input.rsc
#Variables globales a utilizar
:global portknoking;
#
:global testvelocidadii ; :global ospfii ; :global bgpii ; :global dnsii ; :global dhcpii ;
:global snmpii ; :global mndpii ; :global winboxii ; :global sshii ; :global httpii ;
:global ntpii ; :global radiusii ; :global socksii ; :global smbii ; :global l2tpii ;
:global pptpii ; :global greii ; :global ipsecii ; :global webproxyii ; :global apiii ;
#
:global testvelocidadie ; :global ospfie ; :global bgpie ; :global dhcpie ; :global snmpie ;
:global mndpie ; :global winboxie ; :global sshie ; :global httpie ; :global ntpie ; :global radiusie ;
:global socksie ; :global smbie ; :global l2tpie ; :global pptpie ; :global greie ; :global ipsecie ; :global webproxyie ;
:global apiie;
#
:global testvelocidadiec ; :global ospfiec ; :global bgpiec ; :global dnsiec ; :global dhcpiec ;
:global snmpiec ; :global mndpiec ; :global winboxiec ; :global sshiec ; :global httpiec ; :global ntpiec ; :global radiusiec ;
:global socksiec ; :global smbiec ; :global l2tpiec ; :global pptpiec ; :global greiec ; :global ipseciec ; :global webproxyiec ;
:global apiiec;
#
:global testvelocidadlb;:global bgplb;:global dnslb;:global snmplb;:global winboxlb;:global apilb;
:global sshlb;:global httplb;:global ntplb;:global radiuslb;:global sockslb;:global l2tplb;
:global pptplb;:global grelb;:global ipseclb;:global webproxylb;
#
:global testvelocidadln;:global bgpln;:global dnsln;:global snmpln;:global winboxln;:global apiln;
:global sshln;:global httpln;:global ntpln;:global radiusln;:global socksln;:global l2tpln;
:global pptpln;:global greln;:global ipsecln;:global webproxyln;
##Configuraicon
/ip firewall filter
add action=accept chain=input comment=DeshabilitarFirewal_Crenein disabled=no
add action=passthrough chain=input comment="Proteccion de Input - Crenein v6.5"
add action=jump chain=input comment=ReconocimientoParaAccesoPublico_Crenein dst-port=($portknoking->"port1") jump-target=ReconocimientoParaAccesoPublico_Crenein protocol=tcp
add action=jump chain=input comment=ReconocimientoParaAccesoPublico_Crenein dst-port=($portknoking->"port2") jump-target=ReconocimientoParaAccesoPublico_Crenein protocol=tcp
add action=add-src-to-address-list address-list=F_ReconocimientoParaAccesoPublico_Fase1 address-list-timeout=1m chain=ReconocimientoParaAccesoPublico_Crenein dst-port=($portknoking->"port1") \
    protocol=tcp
add action=add-src-to-address-list address-list=F_PermitidoPorReconocimientoParaAccesoPublico address-list-timeout=30m chain=ReconocimientoParaAccesoPublico_Crenein \
    dst-port=($portknoking->"port2") protocol=tcp src-address-list=F_ReconocimientoParaAccesoPublico_Fase1
add action=return chain=ReconocimientoParaAccesoPublico_Crenein
##Test de velocidad
add action=jump chain=input comment=ProteccionTestVelocidadMikrotik_Crenein dst-port=2000 jump-target=ProteccionTestVelocidadMikrotik_Crenein protocol=tcp
add action=jump chain=input dst-port=2000 jump-target=ProteccionTestVelocidadMikrotik_Crenein protocol=udp
#Control de IPs
:if ([:pick $testvelocidadln] != "") do={
    /ip firewall filter add chain=ProteccionTestVelocidadMikrotik_Crenein src-address-list=F_ListaNegraTestVelocidad action=drop;
}
:if ([:pick $testvelocidadlb] != "") do={
    /ip firewall filter add chain=ProteccionTestVelocidadMikrotik_Crenein src-address-list=F_ListaBlancaTestVelocidad action=accept;
}
#Control de interfaces
:if ($testvelocidadii=1) do={
    /ip firewall filter add action=accept chain=ProteccionTestVelocidadMikrotik_Crenein in-interface-list=InterfacesInternas
}
:if ($testvelocidadie=1) do={
    /ip firewall filter add action=accept chain=ProteccionTestVelocidadMikrotik_Crenein in-interface-list=InterfacesExternas
}
:if ($testvelocidadiec=1) do={
    /ip firewall filter add action=accept chain=ProteccionTestVelocidadMikrotik_Crenein in-interface-list=InterfacesExternasDeConfianza
}
add action=drop chain=ProteccionTestVelocidadMikrotik_Crenein
##Proteccion general
add action=jump chain=input comment=ProteccionGeneralDeEntrada_Crenein jump-target=ProteccionGeneralDeEntrada_Crenein
add action=accept chain=ProteccionGeneralDeEntrada_Crenein src-address-list=F_PermitidoPorReconocimientoParaAccesoPublico
add action=reject chain=ProteccionGeneralDeEntrada_Crenein reject-with=icmp-host-unreachable src-address-list=F_DeteccionEscaneoDePuertos
add action=return chain=ProteccionGeneralDeEntrada_Crenein connection-state=new limit=150,20:packet
##Proteccion tcp
add action=jump chain=input comment=ProteccionTCPGeneralDeEntrada_Crenein jump-target=ProteccionTCPGeneralDeEntrada_Crenein protocol=tcp
add action=drop chain=ProteccionTCPGeneralDeEntrada_Crenein connection-state=new protocol=tcp tcp-flags=!syn
add action=add-src-to-address-list address-list=F_DeteccionEscaneoDePuertos address-list-timeout=1w3d chain=ProteccionTCPGeneralDeEntrada_Crenein in-interface-list=\
    InterfacesExternas protocol=tcp psd=21,3s,3,1
add action=return chain=ProteccionTCPGeneralDeEntrada_Crenein
##Ping
add action=jump chain=input comment=ProteccionPING_Crenein icmp-options=0:0-255 jump-target=ProteccionPING_Crenein protocol=icmp
add action=jump chain=input icmp-options=8:0-255 jump-target=ProteccionPING_Crenein protocol=icmp
add action=accept chain=ProteccionPING_Crenein limit=80,5:packet packet-size=!128-65535
add action=drop chain=ProteccionPING_Crenein
##OSPF
add action=jump chain=input comment=ProteccionOSPF_Crenein jump-target=ProteccionOSPF_Crenein protocol=ospf
#Control de interfaces
:if ($ospfii=1) do={
    /ip firewall filter add action=accept chain=ProteccionOSPF_Crenein disabled=$a in-interface-list=InterfacesInternas
}
:if ($ospfie=1) do={
    /ip firewall filter add action=accept chain=ProteccionOSPF_Crenein disabled=$a in-interface-list=InterfacesExternas
}
:if ($ospfiec=1) do={
    /ip firewall filter add action=accept chain=ProteccionOSPF_Crenein disabled=$a in-interface-list=InterfacesExternasDeConfianza
}
add action=drop chain=ProteccionOSPF_Crenein
##BGP
add action=jump chain=input comment=ProteccionBGP_Crenein jump-target=ProteccionBGP_Crenein port=179 protocol=tcp
#Control de IPs
:if ([:pick $bgpln] != "") do={
    /ip firewall filter add chain=ProteccionBGP_Crenein src-address-list=F_ListaNegraBGP action=drop;
}
:if ([:pick $bgplb] != "") do={
    /ip firewall filter add chain=ProteccionBGP_Crenein src-address-list=F_ListaBlancaBGP action=accept;
}
#Control de interfaces
:if ($bgpii=1) do={
    /ip firewall filter add action=accept chain=ProteccionBGP_Crenein in-interface-list=InterfacesInternas
}
:if ($bgpie=1) do={
    /ip firewall filter add action=accept chain=ProteccionBGP_Crenein in-interface-list=InterfacesExternas
}
:if ($bgpiec=1) do={
    /ip firewall filter add action=accept chain=ProteccionBGP_Crenein in-interface-list=InterfacesExternasDeConfianza
}
add action=drop chain=ProteccionBGP_Crenein
##DNS
add action=jump chain=input comment=ProteccionDNS_Crenein jump-target=ProteccionDNS_Crenein port=53 protocol=udp
add action=jump chain=input jump-target=ProteccionDNS_Crenein port=53 protocol=tcp
#Control de IPs
:if ([:pick $dnsln] != "") do={
    /ip firewall filter add chain=ProteccionDNS_Crenein src-address-list=F_ListaNegraDNS action=drop;
}
:if ([:pick $dnslb] != "") do={
    /ip firewall filter add chain=ProteccionDNS_Crenein src-address-list=F_ListaBlancaDNS action=accept;
}
#Control de interfaces
:if ($dnsii=1) do={
    /ip firewall filter add action=accept chain=ProteccionDNS_Crenein in-interface-list=InterfacesInternas
}
:if ($dnsiec=1) do={
    /ip firewall filter add action=accept chain=ProteccionDNS_Crenein in-interface-list=InterfacesExternasDeConfianza
}
add action=accept chain=ProteccionDNS_Crenein in-interface-list=InterfacesExternas protocol=udp src-port=53
add action=drop chain=ProteccionDNS_Crenein
##SNMP
add action=jump chain=input comment=ProteccionSNMP_Crenein dst-port=161 jump-target=ProteccionSNMP_Crenein protocol=udp
#Control de IPs
:if ([:pick $snmpln] != "") do={
    /ip firewall filter add chain=ProteccionSNMP_Crenein src-address-list=F_ListaNegraSNMP action=drop;
}
:if ([:pick $snmplb] != "") do={
    /ip firewall filter add chain=ProteccionSNMP_Crenein src-address-list=F_ListaBlancaSNMP action=accept;
}
#Control de interfaces
:if ($snmpii=1) do={
    /ip firewall filter add action=accept chain=ProteccionSNMP_Crenein in-interface-list=InterfacesInternas
}
:if ($snmpie=1) do={
    /ip firewall filter add action=accept chain=ProteccionSNMP_Crenein in-interface-list=InterfacesExternas
}
:if ($snmpiec=1) do={
    /ip firewall filter add action=accept chain=ProteccionSNMP_Crenein in-interface-list=InterfacesExternasDeConfianza
}
add action=drop chain=ProteccionSNMP_Crenein
##DHCP
add action=jump chain=input comment=ProteccionDHCP_Crenein jump-target=ProteccionDHCP_Crenein port=67,68 protocol=udp
#Control de interfaces
:if ($dhcpii=1) do={
    /ip firewall filter add action=accept chain=ProteccionDHCP_Crenein in-interface-list=InterfacesInternas
}
:if ($dhcpie=1) do={
    /ip firewall filter add action=accept chain=ProteccionDHCP_Crenein in-interface-list=InterfacesExternas
}
:if ($dhcpiec=1) do={
    /ip firewall filter add action=accept chain=ProteccionDHCP_Crenein in-interface-list=InterfacesExternasDeConfianza
}
add action=drop chain=ProteccionDHCP_Crenein
##Winbox
add action=jump chain=input comment=ProteccionWinbox_Crenein dst-port=[/ip service get 6 port] jump-target=ProteccionWinbox_Crenein protocol=tcp
#Control de IPs
:if ([:pick $winboxln] != "") do={
    /ip firewall filter add chain=ProteccionWinbox_Crenein src-address-list=F_ListaNegraWinbox action=drop;
}
:if ([:pick $winboxlb] != "") do={
    /ip firewall filter add chain=ProteccionWinbox_Crenein src-address-list=F_ListaBlancaWinbox action=accept;
}
#Control de interfaces
:if ($winboxii=1) do={
    /ip firewall filter add action=accept chain=ProteccionWinbox_Crenein in-interface-list=InterfacesInternas
}
:if ($winboxie=1) do={
    /ip firewall filter add action=accept chain=ProteccionWinbox_Crenein in-interface-list=InterfacesExternas
}
:if ($winboxiec=1) do={
    /ip firewall filter add action=accept chain=ProteccionWinbox_Crenein in-interface-list=InterfacesExternasDeConfianza
}
add action=drop chain=ProteccionWinbox_Crenein
##API
:foreach apis in=[/ip service find name~"api"] do= {
    /ip firewall filter add action=jump chain=input comment=ProteccionAPIMikrotik_Crenein \
    dst-port=[/ip service get $apis port] jump-target=ProteccionAPIMikrotik_Crenein protocol=tcp
}
#Control de IPs
/ip firewall filter add chain=ProteccionAPIMikrotik_Crenein src-address-list=F_ListaNegraAPI action=drop;
:if ([:pick $apilb] != "") do={
    /ip firewall filter add chain=ProteccionAPIMikrotik_Crenein src-address-list=F_ListaBlancaAPI action=accept;
}
#Control de interfaces
:if ($apiii=1) do={
    /ip firewall filter add action=accept chain=ProteccionAPIMikrotik_Crenein in-interface-list=InterfacesInternas
}
:if ($apiie=1) do={
    /ip firewall filter add action=accept chain=ProteccionAPIMikrotik_Crenein in-interface-list=InterfacesExternas
}
:if ($apiiec=1) do={
    /ip firewall filter add action=accept chain=ProteccionAPIMikrotik_Crenein in-interface-list=InterfacesExternasDeConfianza
}
add action=drop chain=ProteccionAPIMikrotik_Crenein
##HTTP
:foreach www in=[/ip service find name~"www"] do= {
    /ip firewall filter add action=jump chain=input comment=ProteccionHTTP_Crenein \
    dst-port=[/ip service get $www port] jump-target=ProteccionHTTP_Crenein protocol=tcp
}
#Control de IPs
:if ([:pick $httpln] != "") do={
    /ip firewall filter add chain=ProteccionHTTP_Crenein src-address-list=F_ListaNegraHTTP action=drop;
}
:if ([:pick $httplb] != "") do={
    /ip firewall filter add chain=ProteccionHTTP_Crenein src-address-list=F_ListaBlancaHTTP action=accept;
}
#Control de interfaces
:if ($httpii=1) do={
    /ip firewall filter add action=accept chain=ProteccionHTTP_Crenein in-interface-list=InterfacesInternas
}
:if ($httpie=1) do={
    /ip firewall filter add action=accept chain=ProteccionHTTP_Crenein in-interface-list=InterfacesExternas
}
:if ($httpiec=1) do={
    /ip firewall filter add action=accept chain=ProteccionHTTP_Crenein in-interface-list=InterfacesExternasDeConfianza
}
add action=drop chain=ProteccionHTTP_Crenein
##SSH
add action=jump chain=input comment=ProteccionSSH_Crenein dst-port=[/ip service get 3 port] jump-target=ProteccionSSH_Crenein protocol=tcp
#Control de IPs
/ip firewall filter add chain=ProteccionSSH_Crenein src-address-list=F_ListaNegraSSH action=drop;
:if ([:pick $sshlb] != "") do={
    /ip firewall filter add chain=ProteccionSSH_Crenein src-address-list=F_ListaBlancaSSH action=accept;
}
#Control login fallidos
add action=add-src-to-address-list address-list=F_ListaNegraSSH address-list-timeout=1w3d chain=ProteccionSSH_Crenein connection-state=new src-address-list=\
    F_ProteccionSSH_Crenein_Intento3
add action=add-src-to-address-list address-list=F_ProteccionSSH_Crenein_Intento3 address-list-timeout=1m chain=ProteccionSSH_Crenein connection-state=new src-address-list=\
    F_ProteccionSSH_Crenein_Intento2
add action=add-src-to-address-list address-list=F_ProteccionSSH_Crenein_Intento2 address-list-timeout=1m chain=ProteccionSSH_Crenein connection-state=new src-address-list=\
    F_ProteccionSSH_Crenein_Intento1
add action=add-src-to-address-list address-list=F_ProteccionSSH_Crenein_Intento1 address-list-timeout=1m chain=ProteccionSSH_Crenein connection-state=new
#Control de interfaces
:if ($sshii=1) do={
    /ip firewall filter add action=accept chain=ProteccionSSH_Crenein in-interface-list=InterfacesInternas
}
:if ($sshie=1) do={
    /ip firewall filter add action=accept chain=ProteccionSSH_Crenein in-interface-list=InterfacesExternas
}
:if ($sshiec=1) do={
    /ip firewall filter add action=accept chain=ProteccionSSH_Crenein in-interface-list=InterfacesExternasDeConfianza
}
add action=drop chain=ProteccionSSH_Crenein

##NTP
add action=jump chain=input comment=ProteccionNTP_Crenein jump-target=ProteccionNTP_Crenein port=123 protocol=udp
#Control de IPs
:if ([:pick $ntpln] != "") do={
    /ip firewall filter add chain=ProteccionNTP_Crenein src-address-list=F_ListaNegraNTP action=drop;
}
:if ([:pick $ntplb] != "") do={
    /ip firewall filter add chain=ProteccionNTP_Crenein src-address-list=F_ListaBlancaNTP action=accept;
}
#Control de interfaces
:if ($ntpii=1) do={
    /ip firewall filter add action=accept chain=ProteccionNTP_Crenein in-interface-list=InterfacesInternas
}
:if ($ntpie=1) do={
    /ip firewall filter add action=accept chain=ProteccionNTP_Crenein in-interface-list=InterfacesExternas
}
:if ($ntpiec=1) do={
    /ip firewall filter add action=accept chain=ProteccionNTP_Crenein in-interface-list=InterfacesExternasDeConfianza
}
add action=drop chain=ProteccionNTP_Crenein
##RADIUS
add action=jump chain=input comment=ProteccionRADIUS_Crenein jump-target=ProteccionRADIUS_Crenein port=1812,1813 protocol=udp
#Control de IPs
:if ([:pick $radiusln] != "") do={
    /ip firewall filter add chain=ProteccionRADIUS_Crenein src-address-list=F_ListaNegraRADIUS action=drop;
}
:if ([:pick $radiuslb] != "") do={
    /ip firewall filter add chain=ProteccionRADIUS_Crenein src-address-list=F_ListaBlancaRADIUS action=accept;
}
#Control de interfaces
:if ($radiusii=1) do={
    /ip firewall filter add action=accept chain=ProteccionRADIUS_Crenein in-interface-list=InterfacesInternas
}
:if ($radiusie=1) do={
    /ip firewall filter add action=accept chain=ProteccionRADIUS_Crenein in-interface-list=InterfacesExternas
}
:if ($radiusiec=1) do={
    /ip firewall filter add action=accept chain=ProteccionRADIUS_Crenein in-interface-list=InterfacesExternasDeConfianza
}
add action=drop chain=ProteccionRADIUS_Crenein
##MNDP
add action=jump chain=input comment=ProteccionDescubrimientoMikrotik_Crenein jump-target=ProteccionDescubrimientoMikrotik_Crenein port=5678 protocol=udp
#Control de interfaces
:if ($mndpii=1) do={
    /ip firewall filter add action=accept chain=ProteccionDescubrimientoMikrotik_Crenein in-interface-list=InterfacesInternas
}
:if ($mndpie=1) do={
    /ip firewall filter add action=accept chain=ProteccionDescubrimientoMikrotik_Crenein in-interface-list=InterfacesExternas
}
:if ($mndpic=1) do={
    /ip firewall filter add action=accept chain=ProteccionDescubrimientoMikrotik_Crenein in-interface-list=InterfacesExternasDeConfianza
}
add action=drop chain=ProteccionDescubrimientoMikrotik_Crenein
##SOCKS
add action=jump chain=input comment=ProteccionSOCKS_Crenein dst-port=[/ip socks get port]  jump-target=ProteccionSOCKS_Crenein protocol=tcp
#Control de IPs
:if ([:pick $socksln] != "") do={
    /ip firewall filter add chain=ProteccionSOCKS_Crenein src-address-list=F_ListaNegraSOCKS action=drop;
}
:if ([:pick $sockslb] != "") do={
    /ip firewall filter add chain=ProteccionSOCKS_Crenein src-address-list=F_ListaBlancaSOCKS action=accept;
}
#Control de interfaces
:if ($socksii=1) do={
    /ip firewall filter add action=accept chain=ProteccionSOCKS_Crenein in-interface-list=InterfacesInternas
}
:if ($socksie=1) do={
    /ip firewall filter add action=accept chain=ProteccionSOCKS_Crenein in-interface-list=InterfacesExternas
}
:if ($socksiec=1) do={
    /ip firewall filter add action=accept chain=ProteccionSOCKS_Crenein in-interface-list=InterfacesExternasDeConfianza
}
add action=drop chain=ProteccionSOCKS_Crenein
##SMB
add action=jump chain=input comment=ProteccionSMB_Crenein dst-port=135-139,445 jump-target=ProteccionSMB_Crenein protocol=tcp
#Control de interfaces
:if ($smbii=1) do={
    /ip firewall filter add action=accept chain=ProteccionSMB_Crenein in-interface-list=InterfacesInternas
}
:if ($smbie=1) do={
    /ip firewall filter add action=accept chain=ProteccionSMB_Crenein in-interface-list=InterfacesExternas
}
:if ($smbic=1) do={
    /ip firewall filter add action=accept chain=ProteccionSMB_Crenein in-interface-list=InterfacesExternasDeConfianza
}
add action=drop chain=ProteccionSMB_Crenein
##PPTP
add action=jump chain=input comment=ProteccionPPTP_Crenein dst-port=1723 jump-target=ProteccionPPTP_Crenein protocol=tcp
#Control de IPs
/ip firewall filter add chain=ProteccionPPTP_Crenein src-address-list=F_ListaNegraPPTP action=drop;

:if ([:pick $pptplb] != "") do={
    /ip firewall filter add chain=ProteccionPPTP_Crenein src-address-list=F_ListaBlancaPPTP action=accept;
}
#Control de interfaces
:if ($pptpii=1) do={
    /ip firewall filter add action=accept chain=ProteccionPPTP_Crenein in-interface-list=InterfacesInternas
}
:if ($pptpie=1) do={
    /ip firewall filter add action=accept chain=ProteccionPPTP_Crenein in-interface-list=InterfacesExternas
}
:if ($pptpiec=1) do={
    /ip firewall filter add action=accept chain=ProteccionPPTP_Crenein in-interface-list=InterfacesExternasDeConfianza
}
add action=drop chain=ProteccionPPTP_Crenein
##GRE
add action=jump chain=input comment=ProteccionGRE_Crenein jump-target=ProteccionGRE_Crenein protocol=gre
#Control de IPs
/ip firewall filter add chain=ProteccionGRE_Crenein src-address-list=F_ListaNegraGRE action=drop;

:if ([:pick $grelb] != "") do={
    /ip firewall filter add chain=ProteccionGRE_Crenein src-address-list=F_ListaBlancaGRE action=accept;
}
#Control de interfaces
:if ($greii=1) do={
    /ip firewall filter add action=accept chain=ProteccionGRE_Crenein in-interface-list=InterfacesInternas
}
:if ($greie=1) do={
    /ip firewall filter add action=accept chain=ProteccionGRE_Crenein in-interface-list=InterfacesExternas
}
:if ($greiec=1) do={
    /ip firewall filter add action=accept chain=ProteccionGRE_Crenein in-interface-list=InterfacesExternasDeConfianza
}
add action=drop chain=ProteccionGRE_Crenein

##L2TP
add action=jump chain=input comment=ProteccionL2TP_Crenein dst-port=1701 jump-target=ProteccionL2TP_Crenein protocol=udp
#Control de IPs
/ip firewall filter add chain=ProteccionL2TP_Crenein src-address-list=F_ListaNegraL2TP action=drop;

:if ([:pick $l2tplb] != "") do={
    /ip firewall filter add chain=ProteccionL2TP_Crenein src-address-list=F_ListaBlancaL2TP action=accept;
}
#Control de interfaces
:if ($l2tpii=1) do={
    /ip firewall filter add action=accept chain=ProteccionL2TP_Crenein in-interface-list=InterfacesInternas
}
:if ($l2tpie=1) do={
    /ip firewall filter add action=accept chain=ProteccionL2TP_Crenein in-interface-list=InterfacesExternas
}
:if ($l2tpiec=1) do={
    /ip firewall filter add action=accept chain=ProteccionL2TP_Crenein in-interface-list=InterfacesExternasDeConfianza
}
add action=drop chain=ProteccionL2TP_Crenein
##IPSec
add action=jump chain=input comment=ProteccionIPSEC_Crenein dst-port=500 jump-target=ProteccionIPSEC_Crenein protocol=udp
add action=jump chain=input jump-target=ProteccionIPSEC_Crenein protocol=ipsec-esp
add action=jump chain=input jump-target=ProteccionIPSEC_Crenein protocol=ipsec-ah
#Control de IPs
/ip firewall filter add chain=ProteccionIPSEC_Crenein src-address-list=F_ListaNegraIPSEC action=drop;

:if ([:pick $ipseclb] != "") do={
    /ip firewall filter add chain=ProteccionIPSEC_Crenein src-address-list=F_ListaBlancaIPSEC action=accept;
}
#Control de interfaces
:if ($ipsecii=1) do={
    /ip firewall filter add action=accept chain=ProteccionIPSEC_Crenein in-interface-list=InterfacesInternas
}
:if ($ipsecie=1) do={
    /ip firewall filter add action=accept chain=ProteccionIPSEC_Crenein in-interface-list=InterfacesExternas
}
:if ($ipseciec=1) do={
    /ip firewall filter add action=accept chain=ProteccionIPSEC_Crenein in-interface-list=InterfacesExternasDeConfianza
}
add action=drop chain=ProteccionIPSEC_Crenein
##WebProxy
:foreach wbp in=[/ip proxy get port] do= {
    /ip firewall filter add action=jump chain=input comment=ProteccionWebProxy_Crenein \
    dst-port=$wbp jump-target=ProteccionWebProxy_Crenein protocol=tcp
}
#Control de IPs
:if ([:pick $webproxyln] != "") do={
    /ip firewall filter add chain=ProteccionWebProxy_Crenein src-address-list=F_ListaNegraWebProxy action=drop;
}
:if ([:pick $webproxylb] != "") do={
    /ip firewall filter add chain=ProteccionWebProxy_Crenein src-address-list=F_ListaBlancaWebProxy action=accept;
}
#Control de interfaces
:if ($webproxyii=1) do={
    /ip firewall filter add action=accept chain=ProteccionWebProxy_Crenein in-interface-list=InterfacesInternas
}
:if ($webproxyie=1) do={
    /ip firewall filter add action=accept chain=ProteccionWebProxy_Crenein in-interface-list=InterfacesExternas
}
:if ($webproxyiec=1) do={
    /ip firewall filter add action=accept chain=ProteccionWebProxy_Crenein in-interface-list=InterfacesExternasDeConfianza
}
add action=drop chain=ProteccionWebProxy_Crenein

File: /install.rsc
##Instalacion de RSCs
:put "Setting Enviroment"
/system script run EdgeHardeningEnviroment_Crenein
:put "Import Interface-List"
/import mikrotik-edge-hardening/interface-list.rsc
:put "Import Address-Lists"
/import mikrotik-edge-hardening/address-lists.rsc
:put "Purge Filter"
/ip firewall filter remove [find chain~"_Crenein"]
/ip firewall filter remove [find jump-target~"_Crenein"]
/ip firewall filter remove [find comment~"Crenein"]
:put "Import Filter-Forward"
/import mikrotik-edge-hardening/filter-forward.rsc
:put "Import Filter-Input"
/import mikrotik-edge-hardening/filter-input.rsc
:if ([pick [/system resource get version] 0 1] = "6") do={
:put "Import Routes v6"
/import mikrotik-edge-hardening/routes-v6.rsc
}
:if ([pick [/system resource get version] 0 1] = "7") do={
:put "Import Routes v7"
/import mikrotik-edge-hardening/routes-v7.rsc
}
:put "Import Scripts"
/import mikrotik-edge-hardening/script-scheduler.rsc
:put "Import System"
/import mikrotik-edge-hardening/system.rsc
:put "Import Install hardening"

File: /interface-list.rsc
:global interfacesexternas; :global interfacesexternasdeconfianza
/interface list
:do {add name=InterfacesInternas} on-error={:put "INFO -  El InterfaceList InterfacesInternas ya existe"}
:do {add name=InterfacesExternas} on-error={:put "INFO - El InterfaceList InterfacesExternas ya existe"}
:do {add name=InterfacesExternasDeConfianza} on-error={:put "INFO - El InterfaceList InterfacesExternasDeConfianza ya existe"}
##Agregado automático de todas las interfaces como Internas
/interface list member remove [/interface list member find]
/
:foreach ie in=$interfacesexternas do={:if ([:len $ie] > 2) do={/interface list member add list=InterfacesExternas interface=$ie}}
:foreach iec in=$interfacesexternasdeconfianza do={:if ([:len $iec] > 2) do={/interface list member add list=InterfacesExternasDeConfianza interface=$iec}}
:foreach ii in=[/interface find dynamic!=yes] do={:if ([:len [/interface list member find interface=[/interface get $ii name]]] = 0) do={\
/interface list member add list=InterfacesInternas interface=$ii}}

File: /loganalytic.rsc
#Get logs
:global intentosfallidos;
:global ultimologid;
:local alllogs [/log find];
:local countlogs [:len $alllogs];
:local newslogs [:pick $alllogs [find $alllogs $ultimologid] (($countlogs)-1)];
:global ultimologid [:pick $alllogs (($countlogs)-1)];
##Analisis de logs
:foreach auth in=$newslogs do={
  :local message [/log get $auth message];
  :if ($message ~ "login failure for user" and $message ~ "api") do={
    :local iponly [:pick [/log get $auth message ] 23 [:find [/log get $auth message ] " api"]];
    :local iponly2 [:pick $iponly [:find $iponly "m "] [:find $iponly " via"] ];
    :local iponly3 [:pick $iponly2 2 100];
    :if ([:len $iponly3] > 6) do={
      :local countip [:len [/log find $auth message ~ "login failure for user" ~ $iponly3 ~ "api"]];
      :if ($countip >= $intentosfallidos) do={
        :do {
          [/ip firewall address-list add list=F_ListaNegraAPI address=$iponly3];
        } on-error={:put "Error al agregar IP a lista. La IP $iponly3 ya existe."};
      }
    }
  }
}

File: /preinstall.rsc
:do { /system script \
add name=EdgeHardeningEnviroment_Crenein owner=admin \
source=[/file get mikrotik-edge-hardening/router-enviroment.rsc content]} \
on-error={:put "WARNING - El script EdgeHardeningEnviroment_Crenein ya existe."}

:if ([/system script get EdgeHardeningEnviroment_Crenein source]~"__Version 6.1 __") do={} else={\
:put "\nWARNING - Existe una nueva version de Enviroment. Por favor reconstruya su script de enviroment a partir del archivo router-enviroment.rsc"} 

:do {/system script remove EdgeHardeningInstall_Crenein} \
on-error={:put "INFO - El script EdgeHardeningInstall_Crenein no se pudo eliminar porque no existe"}
/system script
add name=EdgeHardeningInstall_Crenein owner=admin \
source=[/file get mikrotik-edge-hardening/install.rsc content]

File: /README.md
# Hardening de router de borde Mikrotik
#### Esta configuracion fue desarrollada desde 0 por Facundo Bertran para Crenein SAS.
#### Su uso es libre y muestra la capacidad de control de routers Mikrotik.
#### Si desea asesoria técnica para su ISP o red empresarial puede comunicarse via whatsapp a+5493725409044

## Procedimiento de instalación.

1. Descargar archivos de github
2. Renombre la carpeta que contiene los archivos rsc como "mikrotik-edge-hardening"
3. Subir carpeta a files dentro del RB
4. Ejecutar los siguientes comandos:
```
/system script remove preinstall
/system script add name=preinstall owner=admin \
source=[/file get mikrotik-edge-hardening/preinstall.rsc content]}
/system script run preinstall
/system script remove preinstall
```
5. Completar script de entorno "EdgeHardeningEnviroment_Crenein"
6. Ejecutar script de instalacion "EdgeHardeningInstall_Crenein"
```
/system script run EdgeHardeningInstall_Crenein
```
7. Deshabilitar los accepts "DeshabilitarFirewal_Crenein" para encender el firewall. Son 2

File: /router-enviroment.rsc
##-----------__Version 6.5 __-------------####
##
#Registra los puertos para port-knoking
##
##----------Configuracion de redes o IPs de confianza------------##
:global portknoking {port1="1"; port2="2"};
##
##--------Configuracion login failure API------##
:global loginfailureapi 0; #-- 1 habilitado 0 deshabilitado
##--------Configuracion de reconocimiento de login fallido api------##
:global intentosfallidos 3;
##--------Configuracion lista negra general------##
:global listanegragral 0; #-- 1 habilitado 0 deshabilitado
##----------Configuracion de redes o IPs de confianza------------##
#Registra las redes o IPs de confianza
##----------Configuracion listas generales------------##
:global redespublicas {""}
:global redesdeorigenpermitidas {""}
:global origenespermitidosnewnodnat {""}; #-Permite conexiones del exterior a redes privadas
:global publicasdentrodelared {""}
##----------Configuracion bogons------------##
#Crea o no bogons de redes privadas y CGNAT
:global bogons10 1;
:global bogons172 1;
:global bogons192 1;
:global bogons100 1;
##----------Configuracion de interfaces------------##
##
#Registra el esquema de interfaces que requieras
##
:global interfacesexternas {""}
:global interfacesexternasdeconfianza {""}
##----------Configuracion de SMTP------------##
##
#Valor 1; habilitado, valor 0 deshabilitado
##
:global smtp 0;
##----------Configuracion de servicios------------##
##
#Habilita o deshabilita servicios en las interfaces. Valor 1; habilitado, valor 0 deshabilitado.
#Crea listas blancas y negras para control por IP. Si la lista esta vacia la regla no se activa.
##
#TestVelocidad
:global testvelocidadln {""}; #Lista Negra
:global testvelocidadlb {""}; #Lista Blanca
:global testvelocidadii 1; #Interfaces Internas
:global testvelocidadie 0; #Interfaces Externas
:global testvelocidadiec 0; #Interfaces ExternasDeConfianza
#OSPF
:global ospfii 1; #Interfaces Internas
:global ospfie 0; #Interfaces Externas
:global ospfiec 0; #Interfaces ExternasDeConfianza
#BGP
:global bgpln {""};
:global bgplb {""};
:global bgpii 1;
:global bgpie 0;
:global bgpiec 1;
#DNS
:global dnsln {""};
:global dnslb {""};
:global dnsii 1;
:global dnsiec 0;
#DCHP
:global dhcpii 1;
:global dhcpie 1;
:global dhcpiec 0;
#SNMP
:global snmpln {""};
:global snmplb {""};
:global snmpii 1;
:global snmpie 0;
:global snmpiec 0;
#MNDP
:global mndpii 1;
:global mndpie 0;
:global mndpiec 0;
#Winbox
:global winboxln {""};
:global winboxlb {""};
:global winboxii 1;
:global winboxie 0;
:global winboxiec 1;
#API
:global apiln {""};
:global apilb {""};
:global apiii 0;
:global apiie 0;
:global apiiec 0;
#SSH
:global sshln {""};
:global sshlb {"10.0.0.0/8"};
:global sshii 1;
:global sshie 1;
:global sshiec 1;
#HTTP
:global httpln {""};
:global httplb {""};
:global httpii 1;
:global httpie 0;
:global httpiec 0;
#NTP
:global ntpln {""};
:global ntplb {""};
:global ntpii 1;
:global ntpie 0;
:global ntpiec 0;
#RADIUS
:global radiusln {""};
:global radiuslb {""};
:global radiusii 0;
:global radiusie 0;
:global radiusiec 0;
#SOCKS
:global socksln {""};
:global sockslb {""};
:global socksii 0;
:global socksie 0;
:global socksiec 0;
#SMB
:global smbii 0;
:global smbie 0;
:global smbiec 0;
#L2TP
:global l2tpln {""};
:global l2tplb {""};
:global l2tpii 0;
:global l2tpie 1;
:global l2tpiec 0;
#PPTP
:global pptpln {""};
:global pptplb {""};
:global pptpii 0;
:global pptpie 1;
:global pptpiec 0;
#GRE
:global greln {""};
:global grelb {""};
:global greii 0;
:global greie 1;
:global greiec 0;
#IPSEC
:global ipsecln {""};
:global ipseclb {""};
:global ipsecii 0;
:global ipsecie 1;
:global ipseciec 0;
#WebProxy
:global webproxyln {""};
:global webproxylb {""};
:global webproxyii 0;
:global webproxyie 0;
:global webproxyiec 0;


File: /routes-v6.rsc
:global bogons10; :global bogons172; :global bogons192; :global bogons100;
##RouterOS v6
/ip route remove [find comment=Bogons]
/ip route
add dst-address=0.0.0.0/8 type=blackhole comment=Bogons
:if ($bogons10 = 1) do={add dst-address=10.0.0.0/8 type=blackhole comment=Bogons}
:if ($bogons172 = 1) do={add dst-address=172.16.0.0/12 type=blackhole comment=Bogons}
:if ($bogons192 = 1) do={add dst-address=192.168.0.0/16 type=blackhole comment=Bogons}
:if ($bogons100 = 1) do={add dst-address=100.64.0.0/10 type=blackhole comment=Bogons}
add dst-address=127.0.0.0/8 type=blackhole comment=Bogons
add dst-address=169.254.0.0/16 type=blackhole comment=Bogons
add dst-address=192.0.0.0/24 type=blackhole comment=Bogons
add dst-address=192.0.2.0/24 type=blackhole comment=Bogons
add dst-address=192.88.99.0/24 type=blackhole comment=Bogons
add dst-address=198.18.0.0/15 type=blackhole comment=Bogons
add dst-address=198.51.100.0/24 type=blackhole comment=Bogons
add dst-address=203.0.113.0/24 type=blackhole comment=Bogons
add dst-address=224.0.0.0/4 type=blackhole comment=Bogons
add dst-address=240.0.0.0/4 type=blackhole comment=Bogons

File: /routes-v7.rsc
:global bogons10; :global bogons172; :global bogons192; :global bogons100;
##RouterOS v7
/ip route remove [find comment=Bogons]
/ip route
add dst-address=0.0.0.0/8 blackhole comment=Bogons
:if ($bogons10 = 1) do={add dst-address=10.0.0.0/8 blackhole comment=Bogons}
:if ($bogons172 = 1) do={add dst-address=172.16.0.0/12 blackhole comment=Bogons}
:if ($bogons192 = 1) do={add dst-address=192.168.0.0/16 blackhole comment=Bogons}
:if ($bogons100 = 1) do={add dst-address=100.64.0.0/10 blackhole comment=Bogons}
add dst-address=127.0.0.0/8 blackhole comment=Bogons
add dst-address=169.254.0.0/16 blackhole comment=Bogons
add dst-address=192.0.0.0/24 blackhole comment=Bogons
add dst-address=192.0.2.0/24 blackhole comment=Bogons
add dst-address=192.88.99.0/24 blackhole comment=Bogons
add dst-address=198.18.0.0/15 blackhole comment=Bogons
add dst-address=198.51.100.0/24 blackhole comment=Bogons
add dst-address=203.0.113.0/24 blackhole comment=Bogons
add dst-address=224.0.0.0/4 blackhole comment=Bogons
add dst-address=240.0.0.0/4 blackhole comment=Bogons


File: /script-scheduler.rsc
:global listanegragral;
:global loginfailureapi;
##--------------------------------##
##-------Lista negra general---------##
:do {/system script remove F_ListaNegraGeneral} on-error={:put "INFO - No se pudo eliminar el script F_ListaNegraGeneral porque no existe"}
:do {/system scheduler remove F_ListaNegraGeneral} on-error={:put "INFO - No se pudo eliminar el scheduler F_ListaNegraGeneral porque no existe"}

:if ($listanegragral = 1) do={
    /system script
    add name=F_ListaNegraGeneral source="ip firewall ad\
        dress-list\r\
        \n:local update do={\r\
        \n:do {\r\
        \n:local data ([:tool fetch url=\$url output=user as-value]->\"data\")\r\
        \nremove [find list=F_ListaNegraGeneral comment=\$description]\r\
        \n:while ([:len \$data]!=0) do={\r\
        \n:if ([:pick \$data 0 [:find \$data \"\\n\"]]~\"^[0-9]{1,3}\\\\.[0-9]{1,3}\\\\.[0-9]{1,3}\\\\.[0-9]{1,3}\") do={\r\
        \n:do {add list=F_ListaNegraGeneral address=([:pick \$data 0 [:find \$data \$delimiter]].\$cidr) comment=\$description timeout=1d} on-error={}\r\
        \n}\r\
        \n:set data [:pick \$data ([:find \$data \"\\n\"]+1) [:len \$data]]\r\
        \n}\r\
        \n} on-error={:log warning \"Address list <\$description> update failed\"}\r\
        \n}\r\
        \n\$update url=https://www.dshield.org/block.txt description=DShield delimiter=(\"\\t\") cidr=/24\r\
        \n\$update url=https://www.spamhaus.org/drop/drop.txt description=\"Spamhaus DROP\" delimiter=(\"\\_\")\r\
        \n\$update url=https://www.spamhaus.org/drop/edrop.txt description=\"Spamhaus EDROP\" delimiter=(\"\\_\")\r\
        \n\$update url=https://sslbl.abuse.ch/blacklist/sslipblacklist.txt description=\"Abuse.ch SSLBL\" delimiter=(\"\\r\")"
    :execute "F_ListaNegraGeneral"

    /system scheduler
    add interval=1d name=F_ListaNegraGeneral on-event=F_ListaNegraGeneral start-date=\
        may/27/2021 start-time=19:56:16
}
##-------Login Failure API---------##
:do {/system scheduler remove LoginFailureForUserXViaAPI_Crenein} on-error={:put "INFO - No se pudo eliminar el scheduler LoginFailureForUserXViaAPI_Crenein porque no existe"}

:if ($loginfailureapi = 1) do={
    :do {
        /system scheduler add name=LoginFailureForUserXViaAPI_Crenein interval=00:05:00 \
        on-event=[/file get mikrotik-edge-hardening/loganalytic.rsc content]
    } on-error={:put "INFO - No se pudo crear el scheduler LoginFailureForUserXViaAPI_Crenein porque ya existe"}
}

File: /system.rsc
/ip settings
set tcp-syncookies=yes
/file set mikrotik-edge-hardening/env-bkp.rsc content=[/system script get EdgeHardeningEnviroment_Crenein source]

File: /unninstall.rsc
#Filter
/ip firewall filter remove [find chain~"_Crenein"]
/ip firewall filter remove [find jump-target~"_Crenein"]
/ip firewall filter remove [find comment~"Crenein"]
#Address-List
/ip firewall address-list
remove [find dynamic=yes]
remove [find list=F_OrigenesPermitidos]
remove [find list=FN_RedesPublicasPropias]
remove [find list=F_OrigenesPermitidos]
remove [find list=F_ProteccionBGP_IPsPermitidas]
remove [find list=F_ListaBlancaAPIMikrotik]
remove [find list=F_ProteccionPublicasDentroDeLaRed]
remove [find list=F_ListaBlancaAPI]
remove [find list=F_ListaBlancaBGP]
remove [find list=F_ListaBlancaDNS]
remove [find list=F_ListaBlancaGRE]
remove [find list=F_ListaBlancaHTTP]
remove [find list=F_ListaBlancaIPSEC]
remove [find list=F_ListaBlancaL2TP]
remove [find list=F_ListaBlancaNTP]
remove [find list=F_ListaBlancaPPTP]
remove [find list=F_ListaBlancaRADIUS]
remove [find list=F_ListaBlancaSNMP]
remove [find list=F_ListaBlancaSOCKS]
remove [find list=F_ListaBlancaSSH]
remove [find list=F_ListaBlancaTestVelocidad]
remove [find list=F_ListaBlancaWebProxy]
remove [find list=F_ListaBlancaWinbox]
remove [find list=F_ListaNegraAPI]
remove [find list=F_ListaNegraBGP]
remove [find list=F_ListaNegraDNS]
remove [find list=F_ListaNegraGRE]
remove [find list=F_ListaNegraHTTP]
remove [find list=F_ListaNegraIPSEC]
remove [find list=F_ListaNegraL2TP]
remove [find list=F_ListaNegraNTP]
remove [find list=F_ListaNegraPPTP]
remove [find list=F_ListaNegraRADIUS]
remove [find list=F_ListaNegraSNMP]
remove [find list=F_ListaNegraSOCKS]
remove [find list=F_ListaNegraSSH]
remove [find list=F_ListaNegraTestVelocidad]
remove [find list=F_ListaNegraWebProxy]
remove [find list=F_ListaNegraWinbox]
#Interface-list-members
:do {/interface list member remove [find list=InterfacesExternas]} on-error {};
:do {/interface list member remove [find list=InterfacesExternasDeConfianza]} on-error {};
:do {/interface list member remove [find list=InterfacesInternas]} on-error {};
#Interface-list
:do {/interface list remove InterfacesExternas} on-error {};
:do {/interface list remove InterfacesExternasDeConfianza} on-error {};
:do {/interface list remove InterfacesInternas} on-error {};
#Routes
/ip route remove [find comment=Bogons]
#Scripts-Scheduler
:do {/system script remove EdgeHardeningInstall_Crenein} on-error {};
:do {/system script remove F_ListaNegraGeneral} on-error {};
:do {/system scheduler remove F_ListaNegraGeneral} on-error {};
#System
/ip settings
set tcp-syncookies=no

File: /version.txt
V6.5

