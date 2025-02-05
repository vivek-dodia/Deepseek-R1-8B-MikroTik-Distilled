# Repository Information
Name: linet.mikrotik

# Directory Structure
Directory structure:
└── github_repos/linet.mikrotik/
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
    │   │       ├── pack-92910e2566f8f91e2fe12d5cd9af44eb2f430cde.idx
    │   │       └── pack-92910e2566f8f91e2fe12d5cd9af44eb2f430cde.pack
    │   ├── packed-refs
    │   └── refs/
    │       ├── heads/
    │       │   └── master
    │       ├── remotes/
    │       │   └── origin/
    │       │       └── HEAD
    │       └── tags/
    ├── .github/
    │   ├── ISSUE_TEMPLATE.md
    │   └── PULL_REQUEST_TEMPLATE.md
    ├── .gitignore
    ├── CHANGELOG.md
    ├── images/
    ├── libs/
    │   ├── loadplugins.py
    │   ├── strings.py
    │   ├── time.py
    │   └── __init__.py
    ├── lld_plugins/
    │   ├── bgp.py
    │   ├── firewall.py
    │   ├── irq.py
    │   ├── radius.py
    │   └── __init__.py
    ├── plugins/
    │   ├── bgp.py
    │   ├── firewall.py
    │   ├── irq.py
    │   ├── radius.py
    │   └── __init__.py
    ├── README.md
    ├── requirements.txt
    ├── TODO.md
    ├── zabbix.py
    ├── zabbix_agentd.d/
    │   └── userparameter_mikrotik_getdata.conf
    └── zabbix_templates/
        ├── zbx_template_API_Poke.xml
        ├── zbx_template_BGP.xml
        ├── zbx_template_firewall_stats.xml
        ├── zbx_template_IRQ_Counters.xml
        ├── zbx_template_Radius_Counters.xml
        ├── zbx_valuemaps_bgp_status.xml
        ├── zbx_valuemaps_mtik_bgp_admin_status.xml
        └── zbx_valuemaps_mtik_firewall.xml


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
	url = https://github.com/zentavr/linet.mikrotik.git
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
0000000000000000000000000000000000000000 d9a373d2dc0cc77a2c2c0b9c1b6e7e2c11d43c23 vivek-dodia <vivek.dodia@icloud.com> 1738605964 -0500	clone: from https://github.com/zentavr/linet.mikrotik.git


File: /.git\logs\refs\heads\master
0000000000000000000000000000000000000000 d9a373d2dc0cc77a2c2c0b9c1b6e7e2c11d43c23 vivek-dodia <vivek.dodia@icloud.com> 1738605964 -0500	clone: from https://github.com/zentavr/linet.mikrotik.git


File: /.git\logs\refs\remotes\origin\HEAD
0000000000000000000000000000000000000000 d9a373d2dc0cc77a2c2c0b9c1b6e7e2c11d43c23 vivek-dodia <vivek.dodia@icloud.com> 1738605964 -0500	clone: from https://github.com/zentavr/linet.mikrotik.git


File: /.git\packed-refs
# pack-refs with: peeled fully-peeled sorted 
d9a373d2dc0cc77a2c2c0b9c1b6e7e2c11d43c23 refs/remotes/origin/master
7e3f8ad5eafcd6d258ef381026f31fbfd20cd106 refs/remotes/origin/python3
a2cbe422ae7440b5f0cd1c37bd01946c212e5e02 refs/tags/v0.1.0
^bf68f6ab79fbcf1865c0c38faa06f9b626e6653d
571f07c0d961e03b218439bc0b9b7b2928f10ac4 refs/tags/v0.2.0
02660e4dc55198f2d6ef60b1b4b741451e48c1ea refs/tags/v0.2.1
2bb14dcc60e598b93d9a42c03791e689bee69fbc refs/tags/v0.2.2


File: /.git\refs\heads\master
d9a373d2dc0cc77a2c2c0b9c1b6e7e2c11d43c23


File: /.git\refs\remotes\origin\HEAD
ref: refs/remotes/origin/master


File: /.github\ISSUE_TEMPLATE.md
<!---
Verify first that your issue/request is not already reported on GitHub.
Please consider to check closed issues as well.

ALWAYS add information AFTER (OUTSIDE) these html comments.
Otherwise it may end up being automatically closed.
--->

<!---
    Please put RouterOS Version here. You can get that with `/system resource print`
--->
**Router OS Version**: xx.yy.zz

##### SUMMARY
<!--- Explain the problem briefly -->

##### ISSUE TYPE
<!--- Pick one below and delete the rest -->
 - Bug Report
 - Feature Idea
 - Documentation Report

##### OS / ENVIRONMENT
<!---
Mention, BELOW THIS COMMENT, the OS you are running this code from.
Also mention the specific version of python and libraries you use.
-->
* OS: `Some OS`
* Python: `xx.yy.zz`
* Virtualenv: yes/no
* pip freeze:
    ```
    a very long ...
    list of libs
    ```

##### STEPS TO REPRODUCE
<!--- For bugs, show exactly how to reproduce the problem, using a minimal test-case.
For new features, show how the feature would be used. -->

<!--- Paste examples or commands between quotes below -->
```

```

<!--- You can also paste gist.github.com links for larger files -->

##### EXPECTED RESULTS
<!--- What did you expect to happen when running the steps above? -->

##### ACTUAL RESULTS
<!--- What actually happened? -->

<!--- Paste verbatim command output between quotes below -->
```

```


File: /.github\PULL_REQUEST_TEMPLATE.md
##### ISSUE TYPE
<!--- Pick one below and delete the rest: -->
 - Feature Pull Request
 - New Module Pull Request
 - Bugfix Pull Request
 - Docs Pull Request
 - Other (please specify)

##### SUMMARY
<!--- Describe the change, including rationale and design decisions -->

<!---
If you are fixing an existing issue, please include "Fixes #nnn" in your
commit message and your description; but you should still explain what
the change does.
-->


File: /.gitignore
File: /CHANGELOG.md
Changelog
=========

## 0.2.0 (2019-06-22)
* **BREAKING**: Added `--login-method` parameter, which specifies which the logging method to use when connecting to your mikrotik.
  Check [LibrouterOS: New Auth Method] for the details. The default method is login_plain for the firmware 6.43+.
  Before autodetect was used, but that polluted Mikrotik's log very greatly.
* **BREAKING**: plugins/lld_plugins's `run()` function now accepts the third parameter for doing the logging.
* Upgrading to `librouteros==2.2.0`
* Using `logging` library. `-v` up to `-vvvv` sets up the logging.
* Added `--encoding` parameter, where you can specify the encoding. Like `ASCII`, `UTF-8` or something else (`ASCII` is the default)
* Fixing an issue when app got crashed if BGP peer had been disabled manually
* Adding the module which allows to track firewall counters. The rule's comment must start with `ZBX` keyword, or the rule is skipped otherwise.


---
[LibrouterOS: New Auth Method]: https://librouteros.readthedocs.io/en/latest/usage.html#new-auth-method


File: /libs\loadplugins.py
# -*- coding: UTF-8 -*-
"""
The idea and the code mainly had been found at https://copyninja.info/blog/dynamic-module-loading.html

"""

import os
import re
import importlib
from logging import getLogger, NullHandler

LOGGER = getLogger('application')
LOGGER.addHandler(NullHandler())


def load_plugins(p_root_dir=os.path.dirname(__file__), p_dir='plugins'):
    """
    Dynamically loads the *.py files (except these starting with __) as modules.
    :param p_root_dir: the root folder where to search for the plugins dir
    :param p_dir: the name of the directory in the root dir where to search for the plugins
    :return: the list of modules
    """

    pysearchre = re.compile('.py$', re.IGNORECASE)
    pluginfiles = filter(pysearchre.search,
                         os.listdir(os.path.join(p_root_dir, p_dir)))

    form_module = lambda fp: '.' + os.path.splitext(fp)[0]
    plugins = map(form_module, pluginfiles)

    # import parent module / namespace
    importlib.import_module(p_dir)
    modules = []
    for plugin in plugins:
        if not plugin.startswith('.__'):
            LOGGER.debug('Loading ' + plugin + ' from ' + os.path.join(p_root_dir, p_dir) + '\n')
            modules.append(importlib.import_module(plugin, package=p_dir))

    return modules


File: /libs\strings.py
# -*- coding: UTF-8 -*-
"""
The idea and the code mainly had been found at https://copyninja.info/blog/dynamic-module-loading.html

"""
import re


def zabbix_escape(st):
    """
    Escapes the string as Zabbix wants
    :param st: string
    :return: escaped string
    """

    # + Quoted and non - quoted entries are supported.
    # + Double - quote is the quoting character.
    # + Entries with whitespace must be quoted.
    # + Double - quote and backslash characters inside quoted entry must be escaped with a backslash.
    # + Escaping is not supported in non - quoted entries.
    # + Linefeed escape sequences(\n) are supported in quoted strings.
    # + Linefeed escape sequences are trimmed from the end of an entry.

    #> https://www.cmi.ac.in/~madhavan/courses/python-2011/docs/diveintopython3/porting-code-to-python-3-with-2to3.html#types
    # (types.StringType, types.UnicodeType, types.BufferType) => (bytes, str, memoryview)
    if isinstance(st, (bytes, str, memoryview)):
        st = re.sub(r'(\"|\\)',
                    lambda m: {
                         '\"': '\\"',
                         '\\': '\\\\',
                    }[m.group()],
                    st)

    return '"{string}"'.format(
        string=st
    )


File: /libs\time.py
# -*- coding: UTF-8 -*-

import re

def time_convert(t):
    """
    Converts Mikrotik's time string to seconds
    :param t: Mikrotik's time string
    :return: seconds
    """
    # print("Received time: {time}".format(time=t))

    # Validate the format first
    if not re.fullmatch(r"(\d+[a-zA-Z]+)+", t):
        raise Exception("Invalid format: {time}".format(time=t))

    time_regex = re.findall(r"(?P<count>\d+)(?P<time_mult>[a-zA-Z]+)", t, flags=re.UNICODE)
    seconds = 0

    for count, time_mult in time_regex:
        # print("Time item: {count}{time_mult}".format(
        #     count=count,
        #     time_mult=time_mult)
        # )
        count = int(count)

        if time_mult == 'ms':
            # print("{count} msec".format(count=count))
            seconds += 0
        elif time_mult == 's':
            # print("{count} sec".format(count=count))
            seconds += count
        elif time_mult == 'm':
            # print("{count} min".format(count=count))
            seconds += count * 60
        elif time_mult == 'h':
            # print("{count} hours".format(count=count))
            seconds += count * 60 * 60
        elif time_mult == 'd':
            # print("{count} days".format(count=count))
            seconds += count * 60 * 60 * 24
        elif time_mult == 'w':
            # print("{count} weeks".format(count=count))
            seconds += count * 60 * 60 * 24 * 7
        else:
            raise Exception("Have no idea how to deal with {time_mult} value".format(
                time_mult=time_mult
            ))

    return seconds


File: /lld_plugins\bgp.py
# -*- coding: UTF-8 -*-
"""
This module pokes Mikrotik for BGP Peers
"""
import json
import time
from libs.strings import zabbix_escape
from logging import getLogger


def run(api, ts=False, log=getLogger(__name__), ver=''):
    """
    Returns BGP LLD JSON
    :param api: initialized librouteros' connect()
    :param ts: Use timestamps
    :return:
    """
    if ts:
        unixtime = " {time} ".format(
            time=int(time.time())
        )
    else:
        unixtime = " "

    peers = []

    if ver.startswith('7.'):
        bgpstats = api(cmd='/routing/bgp/session/print')
        for bgpitem in bgpstats:
            peers.append(
                {
                    '{#PEERNAME}': bgpitem.get('name'),
                    #'{#PEERCOMMENT}': bgpitem.get('comment', ''),
                    '{#PEERAS}': bgpitem.get('remote.as'),
                    '{#PEERLOCALADDR}': bgpitem.get('local.address'),
                    '{#PEERREMOTEADDR}': bgpitem.get('remote.address'),
                    '{#PEERREMOTEID}': bgpitem.get('remote.id'),
                }
            )

    else:
        bgpstats = api(cmd='/routing/bgp/peer/print')
        for bgpitem in bgpstats:
            peers.append(
                {
                    '{#PEERNAME}': bgpitem.get('name'),
                    '{#PEERCOMMENT}': bgpitem.get('comment', ''),
                    '{#PEERAS}': bgpitem.get('remote-as'),
                    '{#PEERLOCALADDR}': bgpitem.get('local-address'),
                    '{#PEERREMOTEADDR}': bgpitem.get('remote-address'),
                    '{#PEERREMOTEID}': bgpitem.get('remote-id'),
                }
            )

    # Composing JSON to return
    json_data = {
        'data': peers
    }

    # Return JSON
    print("{host} {key}{unixtime}{value}".format(
        host='-',
        key='mikrotik.bgp.discovery',
        unixtime=unixtime,
        value=zabbix_escape(json.dumps(json_data))
    ))


File: /lld_plugins\firewall.py
# -*- coding: UTF-8 -*-
"""
This module pokes Mikrotik for Firewall Rules
"""
import json
import time
import pprint
from libs.strings import zabbix_escape
from logging import getLogger


def run(api, ts=False, log=getLogger(__name__), ver=''):
    """
    Returns Firewall Rules LLD JSON
    :param api: initialized librouteros' connect()
    :param ts: Use timestamps
    :return:
    """
    pp = pprint.PrettyPrinter(indent=4)

    if ts:
        unixtime = " {time} ".format(
            time=int(time.time())
        )
    else:
        unixtime = " "

    # Fetch firewall stats
    tables = [
        "filter",
        "nat",
        "mangle",
        "raw"
    ]

    lld = []

    for t in tables:
        log.debug("Processing {table} firewall table".format(
            table=t
        ))

        cmd = '/ip/firewall/{table}/print'.format(table=t)

        log.debug(pp.pformat(cmd))

        stats = api(
            cmd=cmd,
            stats=True
        )

        for rule in stats:
            # We don't want ALL the rules here. We want only those, which has ZBX at the beginning of the comment
            comment = rule.get('comment', '')
            if not comment.startswith('ZBX'):
                continue

            lld.append(
                {
                    '{#MTIK_FW_RULE_ID}': t + '_' + rule.get('.id').strip('*'),
                    '{#MTIK_FW_RULE_COMMENT}': rule.get('comment', rule.get('.id'))
                }
            )

    # Composing JSON to return
    json_data = {
        'data': lld
    }

    # Return JSON
    print("{host} {key}{unixtime}{value}".format(
        host='-',
        key='mikrotik.firewall.discovery',
        unixtime=unixtime,
        value=zabbix_escape(json.dumps(json_data))
    ))


File: /lld_plugins\irq.py
# -*- coding: UTF-8 -*-
"""
This module pokes Mikrotik for IRQ Peers
"""
import json
import time
from libs.strings import zabbix_escape
from logging import getLogger


def run(api, ts=False, log=getLogger(__name__), ver=''):
    """
    Returns IRQ LLD JSON
    :param api: initialized librouteros' connect()
    :param ts: Use timestamps
    :return:
    """
    if ts:
        unixtime = " {time} ".format(
            time=int(time.time())
        )
    else:
        unixtime = " "

    irqstats = api(cmd='/system/resource/irq/print')

    peers = []

    for irqitem in irqstats:
        peers.append(
            {
                '{#IRQ}': irqitem.get('users').replace(",", "__"),
            }
        )

    # Composing JSON to return
    json_data = {
        'data': peers
    }

    # Return JSON
    print("{host} {key}{unixtime}{value}".format(
        host='-',
        key='mikrotik.irq.discovery',
        unixtime=unixtime,
        value=zabbix_escape(json.dumps(json_data))
    ))


File: /lld_plugins\radius.py
# -*- coding: UTF-8 -*-
"""
This module pokes Mikrotik for Radius Servers
"""
import json
import time
from libs.strings import zabbix_escape
from logging import getLogger


def run(api, ts=False, log=getLogger(__name__), ver=''):
    """
    Returns Radius LLD JSON
    :param api: initialized librouteros' connect()
    :param ts: Use timestamps
    :return:
    """
    if ts:
        unixtime = " {time} ".format(
            time=int(time.time())
        )
    else:
        unixtime = " "

    radservers = api(cmd='/radius/print')

    servers = []

    for s in radservers:
        servers.append(
            {
                '{#MTIK_RADIUS_ID}': s.get('.id').strip('*'),
                '{#MTIK_RADIUS_COMMENT}': s.get('comment', s.get('.id')),
                '{#MTIK_RADIUS_ADDRESS}': s.get('address'),
            }
        )

    # Composing JSON to return
    json_data = {
        'data': servers
    }

    # Return JSON
    print("{host} {key}{unixtime}{value}".format(
        host='-',
        key='mikrotik.radius-out.discovery',
        unixtime=unixtime,
        value=zabbix_escape(json.dumps(json_data))
    ))


File: /plugins\bgp.py
# -*- coding: UTF-8 -*-
"""
This module pokes Mikrotik for BGP Counters
"""
import logging
import time
import pprint

from libs.time import time_convert
from libs.strings import zabbix_escape


def run(api, ts=False, log=logging.getLogger(__name__), ver=''):
    """
    Returns BGP Counters
    :param api: initialized librouteros' connect()
    :param ts: Use timestamps
    :return:
    """
    if ts:
        unixtime = " {time} ".format(
            time=int(time.time())
        )
    else:
        unixtime = " "

    # The list of BGP values to monitor
    values_to_monitor = {
        "6": {
            'remote-as': 'remote-as',                    # Remote AS for peer
            'prefix-count': 'prefix-count',              # Accepted Prefixes
            'disabled': 'disabled',                      # Administrative status
            'comment': 'comment',                        # Printing the comment
            'updates-received': 'updates-received',      # Updates Received
            'updates-sent': 'updates-sent',              # Updates Sent
            'withdrawn-received': 'withdrawn-received',  # Withdrawn Received
            'withdrawn-sent': 'withdrawn-sent'           # Withdrawn Sent
        },
        "7": {
            'remote-as': 'remote.as',                    # Remote AS for peer
            'prefix-count': 'prefix-count',              # Accepted Prefixes
            'updates-received': 'remote.messages',       # Updates Received
            'updates-sent': 'local.messages',            # Updates Sent
        }
    }

    if ver.startswith('7.'):
        log.debug("BGP: Dealing with firmware version 7.x ({ver})".format(
            ver=ver
        ))
        bgpstats = api(cmd='/routing/bgp/session/print')
        major_version = "7"
    else:
        log.debug("BGP: Dealing with firmware version 6.x ({ver})".format(
            ver=ver
        ))
        bgpstats = api(cmd='/routing/bgp/peer/print')
        major_version = "6"

    for bgpitem in bgpstats:
        log.debug("BGP: Fetching item {item}".format(
            item=bgpitem
        ))
        if log.getEffectiveLevel() <= logging.DEBUG:
            pprint.pp(bgpitem)

        """
            BGP item for RouterOS v 7.12 looks like this:
            {'.id': '*2800002',
             'name': 'ucomline-1',
             'remote.address': '78.x.x.x',
             'remote.as': 12883,
             'remote.id': '213.x.x.x',
             'remote.capabilities': 'mp,rr,as4,err',
             'remote.messages': 269324,
             'remote.bytes': 31476311,
             'remote.eor': 'ip',
             'local.role': 'ebgp-customer',
             'local.address': '78.x.x.x',
             'local.as': 34605,
             'local.id': '194.x.x.x',
             'local.capabilities': 'mp,rr,gr,as4',
             'local.messages': 139711,
             'local.bytes': 17700041,
             'local.eor': '',
             'output.affinity': 'alone',
             'output.procid': 23,
             'output.filter-chain': 'UCOMLINE-OUT',
             'output.network': 'BGP-Advertisements',
             'output.keep-sent-attributes': True,
             'input.procid': 22,
             'input.filter': 'UCOMLINE-IN',
             'ebgp': '',
             'hold-time': '1m30s',
             'keepalive-time': '30s',
             'uptime': '18h8m41s680ms',
             'last-started': '2023-11-17 08:50:29',
             'last-stopped': '2023-11-17 08:50:28',
             'prefix-count': 902665,
             'established': True} 
            BGP Item for 6.49.2 looks like this:
            {'.id': '*0',
             'name': 'ucomline',
             'instance': 'default',
             'remote-address': '78.x.x.x',
             'remote-as': 12883,
             'tcp-md5-key': '*****',
             'nexthop-choice': 'default',
             'multihop': False,
             'route-reflect': False,
             'hold-time': '1m30s',
             'keepalive-time': '30s',
             'ttl': 'default',
             'in-filter': 'UCOMLINE-IN',
             'out-filter': 'UCOMLINE-OUT',
             'address-families': 'ip',
             'update-source': 'vlan202',
             'default-originate': 'never',
             'remove-private-as': False,
             'as-override': False,
             'passive': False,
             'use-bfd': False,
             'remote-id': '213.x.x.x',
             'local-address': '78.x.x.x',
             'uptime': '19w3d21h51m11s',
             'prefix-count': 902668,
             'updates-sent': 1223,
             'updates-received': 74537047,
             'withdrawn-sent': 800,
             'withdrawn-received': 4966247,
             'remote-hold-time': '3m',
             'used-hold-time': '1m30s',
             'used-keepalive-time': '30s',
             'refresh-capability': True,
             'as4-capability': True,
             'state': 'established',
             'established': True,
             'disabled': False,
             'comment': 'Ucomline'}
        """

        for zabbix_key, ros_key in values_to_monitor[major_version].items():
            print("{host} \"{key}\"{unixtime}{value}".format(
                host='-',
                key='mikrotik.bgp.node[{name},{val}]'.format(
                    name=bgpitem['name'],
                    val=zabbix_key
                ),
                unixtime=unixtime,
                value=zabbix_escape(bgpitem.get(ros_key, 0))
            ))

        # Established time for peer
        uptime = bgpitem.get('uptime', '0s')
        print("{host} \"{key}\"{unixtime}{value}".format(
            host='-',
            key='mikrotik.bgp.node[{name},uptime]'.format(
                name=bgpitem['name']
            ),
            unixtime=unixtime,
            # value=bgpitem['uptime']
            value=zabbix_escape(time_convert(uptime))
        ))

        if not ver.startswith('7.'):
            state = bgpitem.get('state', 'disabled')
            # operational status
            if state == "idle":
                bgp_state = 1
            elif state == "connect":
                bgp_state = 2
            elif state == "active":
                bgp_state = 3
            elif state == "opensent":
                bgp_state = 4
            elif state == "openconfirm":
                bgp_state = 5
            elif state == "established":
                bgp_state = 6
            else:
                bgp_state = 0

            print("{host} \"{key}\"{unixtime}{value}".format(
                host='-',
                key='mikrotik.bgp.node[{name},state]'.format(
                    name=bgpitem['name']
                ),
                unixtime=unixtime,
                value=zabbix_escape(bgp_state)
            ))


File: /plugins\firewall.py
# -*- coding: UTF-8 -*-
# /ip firewall filter print stats where comment ~ ".*Hotspot.*AUTH"
# /ip firewall filter print stats where comment ~ ".*Hotspot.*ACC"
# /ip firewall filter print stats where comment ~ ".*DHCP.*AUTH"
# /ip firewall filter print stats where comment ~ ".*DHCP.*ACC"
"""
This module pokes Mikrotik for Firewall Counters
"""
import time
import pprint

from libs.strings import zabbix_escape
from logging import getLogger


def run(api, ts=False, log=getLogger(__name__), ver=''):
    """
    Returns firewall counters
    :param api: initialized librouteros' connect()
    :param ts: Use timestamps
    :return:
    """
    pp = pprint.PrettyPrinter(indent=4)

    if ts:
        unixtime = " {time} ".format(
            time=int(time.time())
        )
    else:
        unixtime = " "

    # Fetch firewall stats
    tables = [
        "filter",
        "nat",
        "mangle",
        "raw"
    ]

    for t in tables:
        log.debug("Processing {table} firewall table".format(
            table=t
        ))

        cmd = '/ip/firewall/{table}/print'.format(table=t)

        log.debug(pp.pformat(cmd))

        stats = api(
            cmd=cmd,
            stats=True
        )

        metrics_to_monitor = [
            'bytes',
            'packets',
            'disabled',
            # 'comment'
        ]

        for rule in stats:
            """
            {   
                u'.id': u'*3D',
                u'action': u'accept',
                u'bytes': 113970290691,
                u'chain': u'forward',
                u'comment': u'Allow Incoming from CORE to WAN',
                u'disabled': False,
                u'dynamic': False,
                u'in-interface-list': u'CORE',
                u'invalid': False,
                u'log': False,
                u'log-prefix': u'',
                u'out-interface-list': u'WAN',
                u'packets': 102508788
            }
            """

            # We don't want ALL the rules here. We want only those, which has ZBX at the beginning of the comment
            comment = rule.get('comment', '')
            if not comment.startswith('ZBX'):
                continue

            log.info(pp.pformat(comment))
            for metric in metrics_to_monitor:
                print("{host} \"{key}\"{unixtime}{value}".format(
                    host='-',
                    key='mikrotik.firewall[{table}_{id},{metric}]'.format(
                        table=t,
                        id=rule.get('.id').strip('*'),
                        metric=metric
                    ),
                    unixtime=unixtime,
                    value=zabbix_escape(rule.get(metric))
                ))


File: /plugins\irq.py
# -*- coding: UTF-8 -*-
"""
This module pokes Mikrotik for IRQ Counters
"""
import time
from libs.strings import zabbix_escape
from logging import getLogger


def run(api, ts=False, log=getLogger(__name__), ver=''):
    """
    Returns IRQ Counters
    :param api: initialized librouteros' connect()
    :param ts: Use timestamps
    :return:
    """
    if ts:
        unixtime = " {time} ".format(
            time=int(time.time())
        )
    else:
        unixtime = " "

    irqstats = api(cmd='/system/resource/irq/print')

    for irqitem in irqstats:
        print("{host} \"{key}\"{unixtime}{value}".format(
            host='-',
            key='mikrotik.irq[' + irqitem.get('users').replace(",", "__") + ']',
            unixtime=unixtime,
            value=zabbix_escape(irqitem['count'])
        ))


File: /plugins\radius.py
# -*- coding: UTF-8 -*-
"""
This module pokes Mikrotik for Radius Counters
"""
import time
# import pprint

from libs.strings import zabbix_escape
from logging import getLogger


def run(api, ts=False, log=getLogger(__name__), ver=''):
    """
    Returns Radius Counters
    :param api: initialized librouteros' connect()
    :param ts: Use timestamps
    :return:
    """
    if ts:
        unixtime = " {time} ".format(
            time=int(time.time())
        )
    else:
        unixtime = " "

    # Fetch Incoming (CoA) stats
    # ({   u'acks': 263085, u'bad-requests': 0, u'naks': 11304, u'requests': 274388},)
    coastats = api(cmd='/radius/incoming/monitor', once=True)

    coa_values_to_monitor = [
        'acks',          # Acknowledged
        'bad-requests',  # Bad Requests
        'naks',          # Rejects
        'requests'       # Requests

    ]

    for coaitem in coastats:
        for val in coa_values_to_monitor:
            print("{host} \"{key}\"{unixtime}{value}".format(
                host='-',
                key='mikrotik.radius-in.coa[{val}]'.format(
                    val=val
                ),
                unixtime=unixtime,
                value=zabbix_escape(coaitem.get(val, 0))
            ))

    # We need to figure out which Radius settings do we have
    radservers = api(cmd='/radius/print')

    # pp = pprint.PrettyPrinter(indent=4)
    # pp.pprint(radservers)

    radius_values_to_monitor = [
        'accepts',      # Accepts
        'bad-replies',  # Bad Replies
        'pending',      # Pending
        'rejects',      # Rejects
        'requests',     # Requests
        'resends',      # Resends
        'timeouts',     # Timeouts
        # 'comment'
    ]

    for server in radservers:
        # Lets fetch the stats for the every server
        params = {'.id': server.get('.id')}
        stats = api(cmd='/radius/monitor', once=True, **params)
        # pp.pprint(stats)

        for item in stats:
            for val in radius_values_to_monitor:
                print("{host} \"{key}\"{unixtime}{value}".format(
                    host='-',
                    key='mikrotik.radius-out.node[' + server.get('.id').strip('*') + ',' + val + ']',
                    unixtime=unixtime,
                    value=zabbix_escape(item.get(val))
                ))


File: /README.md
Zabbix Helpers To Fetch Mikrotik's Counters via API
---------------------------------------------------

These scripts rely on [PyPi librouteros library].
The reason is why this code was born is that Mikrotik's vendor does not hurry with implementing SNMP OIDs for the 
certain interesting counters. When **Linet LTD** started to migrate to Mikrotiks - they missed an opportunity to monitor
the health of their NAS in many ways like they did before.

Currently, we monitor the next:

*  [radius.py](plugins/radius.py): Radius CoA counters: `/radius incoming monitor`
*  [radius.py](plugins/radius.py): Radius Client counters: `/radius monitor`
*  [bgp.py](plugins/bgp.py): BGP Peer Counters: `/routing bgp peer print status`
*  [irq.py](plugins/irq.py): System IRQ Counters: `/system resource irq print`
*  [firewall.py](plugins/firewall.py): Firewall Counters `/ip firewall <table> print stats`

## Installation

In the example below we use a template which monitors the single Mikrotik Node. If you want to minitor several Mikrotiks 
from a single zabbix_agent - you can fetch the concept and clone the items for several Mikrotiks.

The concept is:

1.  We define **mikrotik.api.discovery** item (manually or using the template) on the node with `zabbix_agentd` available. 
  The item accepts a couple of parameters
2.  We define **mikrotik.api.discovery** in `zabbix_agentd` configuration file
3.  Zabbix Server pokes for **mikrotik.api.discovery**. The item's first parameter is **another** host name  of Mikrotik 
  we want to monitor. Mikrotik does not have zabbix_agentd inside, right?
4.  Poking **mikrotik.api.discovery** spawns the execution of `zabbix.py` which returns some data. This bunch of data get
  forwarded to `zabbix_sender`
5.  A lot of other items defined via Zabbix Template as **Zabbix Trapper** items. So they are being collected during the 
  previous step and pushed into the server with `zabbix_sender`.

### Creating the user in Mikrotik
You need to create an separate group. Go to *System* - *Users* and create the new group:

*  **Name**: `api_read`
*  **Policies**:
    *  `test`
    *  `api`
    *  `read`
    *  `winbox`

Create a user and put it into `api_read` group.

### Tuning up Zabbix

Tested with Zabbix 3.2.

There is a Zabbix Template **Template Mikrotik API Poke**. It contains few macroses which you need probably to re-apply
when attach it to your host:

-  **{$MTIK_HOSTNAME}** (default: `Mikrotik`) - the host name in Zabbix inventory to assign values to.
-  **{$MTIK_API_HOST}** (default: `192.168.0.1`) - the IP address API listens to
-  **{$MTIK_API_USER}** (default: `admin`) - the api user name. *read* permissions for the user is OK to start.
-  **{$MTIK_API_PASSWORD}** (default: `admin`) - the API password
-  **{$MTIK_API_SCRIPT_PARAMS}** (default: `-t`) - the additional parameters you want to pass to `zabbix.py` script.
    Separate with spaces. Probably the most interesting are:
    *  `-t`: Use timestamps when sending the values
    *  `-s`: Use SSL when do API call. The Certificate verification is disabled.
    *  `-P PLUGINS`: the directory with the plugins to use related to the directory where `zabbix.py` is located.


Before importing any templates you need to import Value Maps (Administration - General - Value Maps):

*  **ciscoBgpPeerState** can be found [here][ciscoBgpPeerState value maps]
*  **Mikrotik BGP Administrative Status** can be found [here][Mikrotik BGP Administrative Status value maps]
*  **Mikrotik Firewall Rule Status** can be found [here][Mikrotik Firewall Rule Status value maps]

The next templates are available:

*  **Template Mikrotik API Poke** - defines 2 items which Zabbix server pokes to (user parameters defined in zabbix_agent
    config). While it happens, the execution of `zabbix.py` happens - it pokes for values using Mikrotik API and 
    forwarding the results through `zabbix_sender` happens.
    
    The [template][Template Mikrotik API Poke] should be attached to the host where zabbix_sender and Python is installed.
    Also, the macroses should be defined (see above).

*  **Template Mikrotik BGPv4** - is being used for BGP Peers Monitoring. It discovers for the peers using low level 
    discovery, assigns items and triggers for the peer and also builds a couple of charts.
    
    The [template][Template Mikrotik BGPv4] should be attached to the Mikrotik node.
    Very likely, you need to edit an every single item and define/redefine `Allowed Hosts` value. The default is 
    `127.0.0.1`. This option tells Zabbix from which hosts it will accept the values for *Zabbix Trapper* items.

*  **Template Mikrotik Firewall Statistics** Monitors the stats coming from Mikrotik Firewall. In order to discover the 
   rule, assign a comment to it. The comment **must** start with `ZBX` in order to be monitored by the plugin. Currently
   we monitor bytes and packets per second values. The chart is available for the counters as well.

    The [template][Template Mikrotik Firewall Statistics] should be attached to the Mikrotik node. likely, you need to 
    edit an every     single item and define/redefine `Allowed Hosts` value. 
    The default is `127.0.0.1`. This option tells Zabbix from which hosts it will accept the values for *Zabbix Trapper* 
    items.

*  **Template Mikrotik Radius Counters** - is being used for RADIUS Client counters monitoring. It discovers the servers
    defined in Mikrotik's settings and adds items and charts for them. It monitors RADIUS Incoming CoA counters as well. 
    
    The [template][Template Mikrotik Radius Counters] should be attached to 
    the Mikrotik node. Very likely, you need to edit an every single item and define/redefine `Allowed Hosts` value. 
    The default is `127.0.0.1`. This option tells Zabbix from which hosts it will accept the values for *Zabbix Trapper* 
    items.

*  **Template Mikrotik IRQ Counters** - is being used for System IRQ counters monitoring. It discovers the IRQs
    available in Mikrotik's settings and adds items and charts for them.
    
    The [template][Template Mikrotik IRQ Counters] should be attached to 
    the Mikrotik node. Very likely, you need to edit an every single item and define/redefine `Allowed Hosts` value. 
    The default is `127.0.0.1`. This option tells Zabbix from which hosts it will accept the values for *Zabbix Trapper* 
    items.

### Installation on Zabbix Server

The code uses Python 3 (tested in 3.11.3). All the dependencies are listed in [requirements.txt](requirements.txt) file.
Very likely you will use *Virtualenv* for the installation. I used `/etc/zabbix/.venv` as a virtualenv directory.

As usual, everything which is in `/etc/zabbix/zabbix_agentd.d` gets included by `zabbix_agentd`. Put or symlink 
[userparameter_mikrotik_getdata.conf](zabbix_agentd.d/userparameter_mikrotik_getdata.conf) to something in 
`/etc/zabbix/zabbix_agentd.d` in order to start.

#### Known Issues
*  Python2 support was removed

## Hints

### Low Level Discovery

Low Level discovery plugins are in `lld_plugins` folder. Everything which is `*.py` (except `__*`) will be dynamically 
included and `run()` with the parameters will be executed. 

    ./zabbix.py -H 192.168.0.1 -u apiuser -p apipassword -s -P lld_plugins 2>/dev/null

### Fetch Counters

The plugins which fetch the data using API calls are in `plugins` folder. Everything which is `*.py` (except `__*`) will
be dynamically included and `run()` with the parameters will be executed. 

    ./zabbix.py -H 192.168.0.1 -u apiuser -p apipassword -s 2>/dev/null

### Zabbix Sender Examples

On the Zabbix server an item of type **Zabbix trapper** should be created with corresponding key(s). 
**Note** that incoming values will only be accepted from hosts specified in **Allowed hosts** field for this item.  

Read the values from file:

    zabbix_sender -c /etc/zabbix/zabbix_agentd.conf \
        --host mtik.local \
        --input-file /path/to/parameters_file

Read the values from STDIN:

    cat /path/to/parameters_file | zabbix_sender -c /etc/zabbix/zabbix_agentd.conf \
        --host mtik.local \
        --real-time \
        --input-file -

---
[Upgrade to Python 2.7.11 on Ubuntu]: http://mbless.de/blog/2016/01/09/upgrade-to-python-2711-on-ubuntu-1404-lts.html
[PyPi librouteros library]: https://pypi.org/project/librouteros/

[ciscoBgpPeerState value maps]: zabbix_templates/zbx_valuemaps_bgp_status.xml
[Mikrotik BGP Administrative Status value maps]: zabbix_templates/zbx_valuemaps_mtik_bgp_admin_status.xml
[Mikrotik Firewall Rule Status value maps]: zabbix_templates/zbx_valuemaps_mtik_firewall.xml

[Template Mikrotik API Poke]: zabbix_templates/zbx_template_API_Poke.xml
[Template Mikrotik BGPv4]: zabbix_templates/zbx_template_BGP.xml
[Template Mikrotik Firewall Statistics]: zabbix_templates/zbx_template_firewall_stats.xml
[Template Mikrotik Radius Counters]: zabbix_templates/zbx_template_Radius_Counters.xml
[Template Mikrotik IRQ Counters]: zabbix_templates/zbx_template_IRQ_Counters.xml

[Keeping in sync git repos]: https://moox.io/blog/keep-in-sync-git-repos-on-github-gitlab-bitbucket/


File: /requirements.txt
librouteros==3.2.1


File: /TODO.md
TODO List
---------

## Nothing :)


File: /zabbix.py
#!/usr/bin/env python

import argparse
import ssl
import os
import logging
from sys import stdout, stdin, stderr
import re
import pprint

from librouteros import connect
from libs.loadplugins import load_plugins
from librouteros.login import plain, token


def main():
    parser = argparse.ArgumentParser(
        prog='zabbix-helper',
        description='Zabbix Helper')
    parser.add_argument('-H', '--hostname', default='', dest='hostname', help='API Hostname.')
    parser.add_argument('-e', '--encoding', default='ASCII', dest='encoding',
                        help='The encoding to use during the connect')
    parser.add_argument('-u', '--user', default='admin', dest='username', help='API User.')
    parser.add_argument('-p', '--password', default='', dest='password', help='API Password.')
    parser.add_argument('-s', '--ssl', dest='use_ssl', action='store_true', help='Use SSL.')
    parser.add_argument('-t', '--timestamps', dest='use_timestamps', action='store_true',
                        help='Use unixtime timestamps.')
    parser.add_argument('-P', '--plugins', dest='plugins', default='plugins',
                        help='The folder related to this file where to seek for the plugins')
    parser.add_argument('-m', '--login-method', dest='login_method', default='plain',
                        choices=['plain', 'token'], help='Mikrotik login method to use. "plain" for '
                        'firmware>=6.43, "token" for firmware<6.43.')
    parser.add_argument("-v", "--verbosity", action="count", dest='verbosity', default=0,
                        help="increase output verbosity")

    args = parser.parse_args()

    # Setting up loglevels
    liblog = logging.getLogger('librouteros')
    applog = logging.getLogger('application')

    console = logging.StreamHandler(stderr)
    formatter = logging.Formatter(fmt='%(message)s')
    console.setFormatter(formatter)

    if args.verbosity == 1:
        liblog.setLevel(logging.ERROR)
        applog.setLevel(logging.ERROR)
    elif args.verbosity == 2:
        liblog.setLevel(logging.WARNING)
        applog.setLevel(logging.WARNING)
    elif args.verbosity == 3:
        liblog.setLevel(logging.INFO)
        applog.setLevel(logging.INFO)
    elif args.verbosity > 3:
        liblog.setLevel(logging.DEBUG)
        applog.setLevel(logging.DEBUG)

    # Set up librouteros logging
    liblog.addHandler(console)
    applog.addHandler(console)

    # Connection Arguments
    connect_args = {
        'encoding': args.encoding,
        'port': 8728
    }

    if args.use_ssl:
        ssl_ctx = ssl.create_default_context()
        ssl_ctx.check_hostname = False
        ssl_ctx.verify_mode = ssl.CERT_NONE
        ssl_wrapper = ssl_ctx.wrap_socket

        connect_args.update(port=8729)
        connect_args.update(ssl_wrapper=ssl_wrapper)

    # Dynamically init the class (we expect login_plain() or login_token() here)
    if args.verbosity is not None and args.verbosity > 3:
        pprint.pprint(args)
    applog.debug("LibrouterOS logging method: {method}".format(
        method=args.login_method
    ))
    method = globals()[args.login_method]
    login_methods = (method, )

    # Connect to Mikrotik
    api = connect(
        username=args.username,
        password=args.password,
        host=args.hostname,
        login_methods=login_methods,
        **connect_args
    )

    # pp = pprint.PrettyPrinter(indent=4)

    resources = api(cmd='/system/resource/print')
    firmware_version = ''
    # i.e.: 6.49.2 (stable)
    firmware_re_long = re.compile(r'^(?P<version>\d+\.\d+\.\d+)')
    # i.e.: 7.12 (stable)
    firmware_re_short = re.compile(r'^(?P<version>\d+\.\d+)')
    for r in resources:
        version_raw = r['version']
        applog.debug("RouterOS raw version: {raw}".format(
            raw=version_raw
        ))
        match_long = firmware_re_long.match(version_raw)
        match_short = firmware_re_short.match(version_raw)
        if match_long:
            firmware_version = match_long.group('version')
        elif match_short:
            firmware_version = match_short.group('version')
        else:
            applog.error("Cannot detect RouterOS version")
    applog.debug("RouterOS version is {ver}".format(
        ver=firmware_version
    ))

    # Dynamically import the modules
    modules = load_plugins(os.path.dirname(__file__), args.plugins)
    for m in modules:
        # pp.pprint(m)
        m.run(api, args.use_timestamps, applog, firmware_version)

    # Closing Mikrotik's API Session
    api.close()


if __name__ == '__main__':
    main()


File: /zabbix_agentd.d\userparameter_mikrotik_getdata.conf
# The values accept 5 parameters:
# $1 - Host name of the monitored node.
# $2 - IP Address of the Mikrotik router.
# $3 - API username.
# $4 - API password.
# $5 - additional parameters.

UserParameter=mikrotik.api.getdata[*],/etc/zabbix/.venv/bin/python /etc/zabbix/mikrotik/zabbix.py -H $2 -u $3 -p $4 $5 2>/dev/null | /usr/bin/zabbix_sender -c /etc/zabbix/zabbix_agentd.conf --host $1 --real-time --with-timestamps --input-file - | echo $?
UserParameter=mikrotik.api.discovery[*],/etc/zabbix/.venv/bin/python /etc/zabbix/mikrotik/zabbix.py -H $2 -u $3 -p $4 $5 -P lld_plugins 2>/dev/null | /usr/bin/zabbix_sender -c /etc/zabbix/zabbix_agentd.conf --host $1 --real-time --input-file - | echo $?


File: /zabbix_templates\zbx_template_API_Poke.xml
<?xml version="1.0" encoding="UTF-8"?>
<zabbix_export>
    <version>3.2</version>
    <date>2018-07-02T22:12:03Z</date>
    <groups>
        <group>
            <name>Custom Templates</name>
        </group>
    </groups>
    <templates>
        <template>
            <template>Template Mikrotik API Poke</template>
            <name>Template Mikrotik API Poke</name>
            <description>Just pokes mikrotik.api.** which executes the script</description>
            <groups>
                <group>
                    <name>Custom Templates</name>
                </group>
            </groups>
            <applications>
                <application>
                    <name>Mikrotik API Poke</name>
                </application>
            </applications>
            <items>
                <item>
                    <name>API Discovery Services</name>
                    <type>7</type>
                    <snmp_community/>
                    <multiplier>0</multiplier>
                    <snmp_oid/>
                    <key>mikrotik.api.discovery[{$MTIK_HOSTNAME},{$MTIK_API_HOST},{$MTIK_API_USER},{$MTIK_API_PASSWORD},-s]</key>
                    <delay>1800</delay>
                    <history>1</history>
                    <trends>1</trends>
                    <status>0</status>
                    <value_type>3</value_type>
                    <allowed_hosts/>
                    <units/>
                    <delta>0</delta>
                    <snmpv3_contextname/>
                    <snmpv3_securityname/>
                    <snmpv3_securitylevel>0</snmpv3_securitylevel>
                    <snmpv3_authprotocol>0</snmpv3_authprotocol>
                    <snmpv3_authpassphrase/>
                    <snmpv3_privprotocol>0</snmpv3_privprotocol>
                    <snmpv3_privpassphrase/>
                    <formula>1</formula>
                    <delay_flex/>
                    <params/>
                    <ipmi_sensor/>
                    <data_type>0</data_type>
                    <authtype>0</authtype>
                    <username/>
                    <password/>
                    <publickey/>
                    <privatekey/>
                    <port/>
                    <description>Executes the script which discovers the services doing API call to Mikrotik</description>
                    <inventory_link>0</inventory_link>
                    <applications>
                        <application>
                            <name>Mikrotik API Poke</name>
                        </application>
                    </applications>
                    <valuemap/>
                    <logtimefmt/>
                </item>
                <item>
                    <name>API Getdata Call</name>
                    <type>7</type>
                    <snmp_community/>
                    <multiplier>0</multiplier>
                    <snmp_oid/>
                    <key>mikrotik.api.getdata[{$MTIK_HOSTNAME},{$MTIK_API_HOST},{$MTIK_API_USER},{$MTIK_API_PASSWORD},-s -t]</key>
                    <delay>60</delay>
                    <history>1</history>
                    <trends>1</trends>
                    <status>0</status>
                    <value_type>3</value_type>
                    <allowed_hosts/>
                    <units/>
                    <delta>0</delta>
                    <snmpv3_contextname/>
                    <snmpv3_securityname/>
                    <snmpv3_securitylevel>0</snmpv3_securitylevel>
                    <snmpv3_authprotocol>0</snmpv3_authprotocol>
                    <snmpv3_authpassphrase/>
                    <snmpv3_privprotocol>0</snmpv3_privprotocol>
                    <snmpv3_privpassphrase/>
                    <formula>1</formula>
                    <delay_flex/>
                    <params/>
                    <ipmi_sensor/>
                    <data_type>0</data_type>
                    <authtype>0</authtype>
                    <username/>
                    <password/>
                    <publickey/>
                    <privatekey/>
                    <port/>
                    <description>Executes the script which gets the data doing API call to Mikrotik</description>
                    <inventory_link>0</inventory_link>
                    <applications>
                        <application>
                            <name>Mikrotik API Poke</name>
                        </application>
                    </applications>
                    <valuemap/>
                    <logtimefmt/>
                </item>
            </items>
            <discovery_rules/>
            <httptests/>
            <macros>
                <macro>
                    <macro>{$MTIK_API_HOST}</macro>
                    <value>192.168.0.1</value>
                </macro>
                <macro>
                    <macro>{$MTIK_API_PASSWORD}</macro>
                    <value>admin</value>
                </macro>
                <macro>
                    <macro>{$MTIK_API_SCRIPT_PARAMS}</macro>
                    <value>-t</value>
                </macro>
                <macro>
                    <macro>{$MTIK_API_USER}</macro>
                    <value>admin</value>
                </macro>
                <macro>
                    <macro>{$MTIK_HOSTNAME}</macro>
                    <value>Mikrotik</value>
                </macro>
            </macros>
            <templates/>
            <screens/>
        </template>
    </templates>
</zabbix_export>


File: /zabbix_templates\zbx_template_BGP.xml
<?xml version="1.0" encoding="UTF-8"?>
<zabbix_export>
    <version>3.2</version>
    <date>2019-06-30T11:56:50Z</date>
    <groups>
        <group>
            <name>Custom Templates</name>
        </group>
        <group>
            <name>Templates</name>
        </group>
    </groups>
    <templates>
        <template>
            <template>Template Mikrotik BGPv4</template>
            <name>Template Mikrotik BGPv4</name>
            <description>Monitors BGP states using Zabbix active checks</description>
            <groups>
                <group>
                    <name>Custom Templates</name>
                </group>
                <group>
                    <name>Templates</name>
                </group>
            </groups>
            <applications>
                <application>
                    <name>Mikrotik BGP</name>
                </application>
            </applications>
            <items/>
            <discovery_rules>
                <discovery_rule>
                    <name>Mikrotik BGP4 Peer(s)</name>
                    <type>2</type>
                    <snmp_community/>
                    <snmp_oid/>
                    <key>mikrotik.bgp.discovery</key>
                    <delay>0</delay>
                    <status>0</status>
                    <allowed_hosts>127.0.0.1</allowed_hosts>
                    <snmpv3_contextname/>
                    <snmpv3_securityname/>
                    <snmpv3_securitylevel>0</snmpv3_securitylevel>
                    <snmpv3_authprotocol>0</snmpv3_authprotocol>
                    <snmpv3_authpassphrase/>
                    <snmpv3_privprotocol>0</snmpv3_privprotocol>
                    <snmpv3_privpassphrase/>
                    <delay_flex/>
                    <params/>
                    <ipmi_sensor/>
                    <authtype>0</authtype>
                    <username/>
                    <password/>
                    <publickey/>
                    <privatekey/>
                    <port/>
                    <filter>
                        <evaltype>0</evaltype>
                        <formula/>
                        <conditions/>
                    </filter>
                    <lifetime>3</lifetime>
                    <description>Explores for the current BGP Sessions</description>
                    <item_prototypes>
                        <item_prototype>
                            <name>Connection description for peer {#PEERNAME}</name>
                            <type>2</type>
                            <snmp_community/>
                            <multiplier>0</multiplier>
                            <snmp_oid/>
                            <key>mikrotik.bgp.node[{#PEERNAME},comment]</key>
                            <delay>0</delay>
                            <history>1</history>
                            <trends>0</trends>
                            <status>0</status>
                            <value_type>4</value_type>
                            <allowed_hosts>127.0.0.1</allowed_hosts>
                            <units/>
                            <delta>0</delta>
                            <snmpv3_contextname/>
                            <snmpv3_securityname/>
                            <snmpv3_securitylevel>0</snmpv3_securitylevel>
                            <snmpv3_authprotocol>0</snmpv3_authprotocol>
                            <snmpv3_authpassphrase/>
                            <snmpv3_privprotocol>0</snmpv3_privprotocol>
                            <snmpv3_privpassphrase/>
                            <formula>1</formula>
                            <delay_flex/>
                            <params/>
                            <ipmi_sensor/>
                            <data_type>0</data_type>
                            <authtype>0</authtype>
                            <username/>
                            <password/>
                            <publickey/>
                            <privatekey/>
                            <port/>
                            <description>Connection Description for the peer</description>
                            <inventory_link>0</inventory_link>
                            <applications>
                                <application>
                                    <name>Mikrotik BGP</name>
                                </application>
                            </applications>
                            <valuemap/>
                            <logtimefmt/>
                            <application_prototypes/>
                        </item_prototype>
                        <item_prototype>
                            <name>Administrative status for peer {#PEERNAME}</name>
                            <type>2</type>
                            <snmp_community/>
                            <multiplier>0</multiplier>
                            <snmp_oid/>
                            <key>mikrotik.bgp.node[{#PEERNAME},disabled]</key>
                            <delay>0</delay>
                            <history>7</history>
                            <trends>180</trends>
                            <status>0</status>
                            <value_type>3</value_type>
                            <allowed_hosts>127.0.0.1</allowed_hosts>
                            <units/>
                            <delta>0</delta>
                            <snmpv3_contextname/>
                            <snmpv3_securityname/>
                            <snmpv3_securitylevel>0</snmpv3_securitylevel>
                            <snmpv3_authprotocol>0</snmpv3_authprotocol>
                            <snmpv3_authpassphrase/>
                            <snmpv3_privprotocol>0</snmpv3_privprotocol>
                            <snmpv3_privpassphrase/>
                            <formula>1</formula>
                            <delay_flex/>
                            <params/>
                            <ipmi_sensor/>
                            <data_type>3</data_type>
                            <authtype>0</authtype>
                            <username/>
                            <password/>
                            <publickey/>
                            <privatekey/>
                            <port/>
                            <description>Administrative status of the peer</description>
                            <inventory_link>0</inventory_link>
                            <applications>
                                <application>
                                    <name>Mikrotik BGP</name>
                                </application>
                            </applications>
                            <valuemap>
                                <name>Mikrotik BGP Administrative Status</name>
                            </valuemap>
                            <logtimefmt/>
                            <application_prototypes/>
                        </item_prototype>
                        <item_prototype>
                            <name>BGP Accepted Prefixes for peer {#PEERNAME}</name>
                            <type>2</type>
                            <snmp_community/>
                            <multiplier>0</multiplier>
                            <snmp_oid/>
                            <key>mikrotik.bgp.node[{#PEERNAME},prefix-count]</key>
                            <delay>0</delay>
                            <history>7</history>
                            <trends>180</trends>
                            <status>0</status>
                            <value_type>3</value_type>
                            <allowed_hosts>127.0.0.1</allowed_hosts>
                            <units/>
                            <delta>0</delta>
                            <snmpv3_contextname/>
                            <snmpv3_securityname/>
                            <snmpv3_securitylevel>0</snmpv3_securitylevel>
                            <snmpv3_authprotocol>0</snmpv3_authprotocol>
                            <snmpv3_authpassphrase/>
                            <snmpv3_privprotocol>0</snmpv3_privprotocol>
                            <snmpv3_privpassphrase/>
                            <formula>1</formula>
                            <delay_flex/>
                            <params/>
                            <ipmi_sensor/>
                            <data_type>0</data_type>
                            <authtype>0</authtype>
                            <username/>
                            <password/>
                            <publickey/>
                            <privatekey/>
                            <port/>
                            <description>Accepted Prefixes from the remote peer</description>
                            <inventory_link>0</inventory_link>
                            <applications>
                                <application>
                                    <name>Mikrotik BGP</name>
                                </application>
                            </applications>
                            <valuemap/>
                            <logtimefmt/>
                            <application_prototypes/>
                        </item_prototype>
                        <item_prototype>
                            <name>BGP AS Peer Number for peer {#PEERNAME}</name>
                            <type>2</type>
                            <snmp_community/>
                            <multiplier>0</multiplier>
                            <snmp_oid/>
                            <key>mikrotik.bgp.node[{#PEERNAME},remote-as]</key>
                            <delay>0</delay>
                            <history>3</history>
                            <trends>3</trends>
                            <status>0</status>
                            <value_type>3</value_type>
                            <allowed_hosts>127.0.0.1</allowed_hosts>
                            <units/>
                            <delta>0</delta>
                            <snmpv3_contextname/>
                            <snmpv3_securityname/>
                            <snmpv3_securitylevel>0</snmpv3_securitylevel>
                            <snmpv3_authprotocol>0</snmpv3_authprotocol>
                            <snmpv3_authpassphrase/>
                            <snmpv3_privprotocol>0</snmpv3_privprotocol>
                            <snmpv3_privpassphrase/>
                            <formula>1</formula>
                            <delay_flex/>
                            <params/>
                            <ipmi_sensor/>
                            <data_type>0</data_type>
                            <authtype>0</authtype>
                            <username/>
                            <password/>
                            <publickey/>
                            <privatekey/>
                            <port/>
                            <description>AS Number of the remote peer</description>
                            <inventory_link>0</inventory_link>
                            <applications>
                                <application>
                                    <name>Mikrotik BGP</name>
                                </application>
                            </applications>
                            <valuemap/>
                            <logtimefmt/>
                            <application_prototypes/>
                        </item_prototype>
                        <item_prototype>
                            <name>Operational Status with peer {#PEERNAME}</name>
                            <type>2</type>
                            <snmp_community/>
                            <multiplier>0</multiplier>
                            <snmp_oid/>
                            <key>mikrotik.bgp.node[{#PEERNAME},state]</key>
                            <delay>0</delay>
                            <history>1</history>
                            <trends>1</trends>
                            <status>0</status>
                            <value_type>3</value_type>
                            <allowed_hosts>127.0.0.1</allowed_hosts>
                            <units/>
                            <delta>0</delta>
                            <snmpv3_contextname/>
                            <snmpv3_securityname/>
                            <snmpv3_securitylevel>0</snmpv3_securitylevel>
                            <snmpv3_authprotocol>0</snmpv3_authprotocol>
                            <snmpv3_authpassphrase/>
                            <snmpv3_privprotocol>0</snmpv3_privprotocol>
                            <snmpv3_privpassphrase/>
                            <formula>1</formula>
                            <delay_flex/>
                            <params/>
                            <ipmi_sensor/>
                            <data_type>0</data_type>
                            <authtype>0</authtype>
                            <username/>
                            <password/>
                            <publickey/>
                            <privatekey/>
                            <port/>
                            <description>Operational status for the peer</description>
                            <inventory_link>0</inventory_link>
                            <applications>
                                <application>
                                    <name>Mikrotik BGP</name>
                                </application>
                            </applications>
                            <valuemap>
                                <name>ciscoBgpPeerState</name>
                            </valuemap>
                            <logtimefmt/>
                            <application_prototypes/>
                        </item_prototype>
                        <item_prototype>
                            <name>Updates-Received from peer {#PEERNAME}</name>
                            <type>2</type>
                            <snmp_community/>
                            <multiplier>0</multiplier>
                            <snmp_oid/>
                            <key>mikrotik.bgp.node[{#PEERNAME},updates-received]</key>
                            <delay>0</delay>
                            <history>7</history>
                            <trends>180</trends>
                            <status>0</status>
                            <value_type>3</value_type>
                            <allowed_hosts>127.0.0.1</allowed_hosts>
                            <units/>
                            <delta>1</delta>
                            <snmpv3_contextname/>
                            <snmpv3_securityname/>
                            <snmpv3_securitylevel>0</snmpv3_securitylevel>
                            <snmpv3_authprotocol>0</snmpv3_authprotocol>
                            <snmpv3_authpassphrase/>
                            <snmpv3_privprotocol>0</snmpv3_privprotocol>
                            <snmpv3_privpassphrase/>
                            <formula>1</formula>
                            <delay_flex/>
                            <params/>
                            <ipmi_sensor/>
                            <data_type>0</data_type>
                            <authtype>0</authtype>
                            <username/>
                            <password/>
                            <publickey/>
                            <privatekey/>
                            <port/>
                            <description>Number of reachable routing prefixes received</description>
                            <inventory_link>0</inventory_link>
                            <applications>
                                <application>
                                    <name>Mikrotik BGP</name>
                                </application>
                            </applications>
                            <valuemap/>
                            <logtimefmt/>
                            <application_prototypes/>
                        </item_prototype>
                        <item_prototype>
                            <name>Updates-Sent to peer {#PEERNAME}</name>
                            <type>2</type>
                            <snmp_community/>
                            <multiplier>0</multiplier>
                            <snmp_oid/>
                            <key>mikrotik.bgp.node[{#PEERNAME},updates-sent]</key>
                            <delay>0</delay>
                            <history>7</history>
                            <trends>180</trends>
                            <status>0</status>
                            <value_type>3</value_type>
                            <allowed_hosts>127.0.0.1</allowed_hosts>
                            <units/>
                            <delta>1</delta>
                            <snmpv3_contextname/>
                            <snmpv3_securityname/>
                            <snmpv3_securitylevel>0</snmpv3_securitylevel>
                            <snmpv3_authprotocol>0</snmpv3_authprotocol>
                            <snmpv3_authpassphrase/>
                            <snmpv3_privprotocol>0</snmpv3_privprotocol>
                            <snmpv3_privpassphrase/>
                            <formula>1</formula>
                            <delay_flex/>
                            <params/>
                            <ipmi_sensor/>
                            <data_type>0</data_type>
                            <authtype>0</authtype>
                            <username/>
                            <password/>
                            <publickey/>
                            <privatekey/>
                            <port/>
                            <description>Updates Sent per sec</description>
                            <inventory_link>0</inventory_link>
                            <applications>
                                <application>
                                    <name>Mikrotik BGP</name>
                                </application>
                            </applications>
                            <valuemap/>
                            <logtimefmt/>
                            <application_prototypes/>
                        </item_prototype>
                        <item_prototype>
                            <name>Established time with peer {#PEERNAME}</name>
                            <type>2</type>
                            <snmp_community/>
                            <multiplier>0</multiplier>
                            <snmp_oid/>
                            <key>mikrotik.bgp.node[{#PEERNAME},uptime]</key>
                            <delay>0</delay>
                            <history>30</history>
                            <trends>180</trends>
                            <status>0</status>
                            <value_type>3</value_type>
                            <allowed_hosts>127.0.0.1</allowed_hosts>
                            <units>s</units>
                            <delta>0</delta>
                            <snmpv3_contextname/>
                            <snmpv3_securityname/>
                            <snmpv3_securitylevel>0</snmpv3_securitylevel>
                            <snmpv3_authprotocol>0</snmpv3_authprotocol>
                            <snmpv3_authpassphrase/>
                            <snmpv3_privprotocol>0</snmpv3_privprotocol>
                            <snmpv3_privpassphrase/>
                            <formula>1</formula>
                            <delay_flex/>
                            <params/>
                            <ipmi_sensor/>
                            <data_type>0</data_type>
                            <authtype>0</authtype>
                            <username/>
                            <password/>
                            <publickey/>
                            <privatekey/>
                            <port/>
                            <description>Established time with the peer</description>
                            <inventory_link>0</inventory_link>
                            <applications>
                                <application>
                                    <name>Mikrotik BGP</name>
                                </application>
                            </applications>
                            <valuemap/>
                            <logtimefmt/>
                            <application_prototypes/>
                        </item_prototype>
                        <item_prototype>
                            <name>Withdrawn-Received from peer {#PEERNAME}</name>
                            <type>2</type>
                            <snmp_community/>
                            <multiplier>0</multiplier>
                            <snmp_oid/>
                            <key>mikrotik.bgp.node[{#PEERNAME},withdrawn-received]</key>
                            <delay>0</delay>
                            <history>7</history>
                            <trends>180</trends>
                            <status>0</status>
                            <value_type>3</value_type>
                            <allowed_hosts>127.0.0.1</allowed_hosts>
                            <units/>
                            <delta>1</delta>
                            <snmpv3_contextname/>
                            <snmpv3_securityname/>
                            <snmpv3_securitylevel>0</snmpv3_securitylevel>
                            <snmpv3_authprotocol>0</snmpv3_authprotocol>
                            <snmpv3_authpassphrase/>
                            <snmpv3_privprotocol>0</snmpv3_privprotocol>
                            <snmpv3_privpassphrase/>
                            <formula>1</formula>
                            <delay_flex/>
                            <params/>
                            <ipmi_sensor/>
                            <data_type>0</data_type>
                            <authtype>0</authtype>
                            <username/>
                            <password/>
                            <publickey/>
                            <privatekey/>
                            <port/>
                            <description>Withdrawn Received per sec</description>
                            <inventory_link>0</inventory_link>
                            <applications>
                                <application>
                                    <name>Mikrotik BGP</name>
                                </application>
                            </applications>
                            <valuemap/>
                            <logtimefmt/>
                            <application_prototypes/>
                        </item_prototype>
                        <item_prototype>
                            <name>Withdrawn-Sent to peer {#PEERNAME}</name>
                            <type>2</type>
                            <snmp_community/>
                            <multiplier>0</multiplier>
                            <snmp_oid/>
                            <key>mikrotik.bgp.node[{#PEERNAME},withdrawn-sent]</key>
                            <delay>0</delay>
                            <history>7</history>
                            <trends>180</trends>
                            <status>0</status>
                            <value_type>3</value_type>
                            <allowed_hosts>127.0.0.1</allowed_hosts>
                            <units/>
                            <delta>1</delta>
                            <snmpv3_contextname/>
                            <snmpv3_securityname/>
                            <snmpv3_securitylevel>0</snmpv3_securitylevel>
                            <snmpv3_authprotocol>0</snmpv3_authprotocol>
                            <snmpv3_authpassphrase/>
                            <snmpv3_privprotocol>0</snmpv3_privprotocol>
                            <snmpv3_privpassphrase/>
                            <formula>1</formula>
                            <delay_flex/>
                            <params/>
                            <ipmi_sensor/>
                            <data_type>0</data_type>
                            <authtype>0</authtype>
                            <username/>
                            <password/>
                            <publickey/>
                            <privatekey/>
                            <port/>
                            <description>Withdrawn Sent per sec</description>
                            <inventory_link>0</inventory_link>
                            <applications>
                                <application>
                                    <name>Mikrotik BGP</name>
                                </application>
                            </applications>
                            <valuemap/>
                            <logtimefmt/>
                            <application_prototypes/>
                        </item_prototype>
                    </item_prototypes>
                    <trigger_prototypes>
                        <trigger_prototype>
                            <expression>{Template Mikrotik BGPv4:mikrotik.bgp.node[{#PEERNAME},remote-as].diff(0)}&gt;0</expression>
                            <recovery_mode>0</recovery_mode>
                            <recovery_expression/>
                            <name>BGP AS Number of the peer {#PEERNAME} was changed</name>
                            <correlation_mode>0</correlation_mode>
                            <correlation_tag/>
                            <url/>
                            <status>0</status>
                            <priority>1</priority>
                            <description/>
                            <type>0</type>
                            <manual_close>0</manual_close>
                            <dependencies/>
                            <tags/>
                        </trigger_prototype>
                        <trigger_prototype>
                            <expression>{Template Mikrotik BGPv4:mikrotik.bgp.node[{#PEERNAME},disabled].last(0)}=0 and {Template Mikrotik BGPv4:mikrotik.bgp.node[{#PEERNAME},state].last(#3)}&lt;&gt;6</expression>
                            <recovery_mode>0</recovery_mode>
                            <recovery_expression/>
                            <name>BGP Peer {#PEERNAME} is DOWN</name>
                            <correlation_mode>0</correlation_mode>
                            <correlation_tag/>
                            <url/>
                            <status>0</status>
                            <priority>4</priority>
                            <description/>
                            <type>0</type>
                            <manual_close>0</manual_close>
                            <dependencies/>
                            <tags/>
                        </trigger_prototype>
                        <trigger_prototype>
                            <expression>{Template Mikrotik BGPv4:mikrotik.bgp.node[{#PEERNAME},prefix-count].last()}&lt;0.9*{Template Mikrotik BGPv4:mikrotik.bgp.node[{#PEERNAME},prefix-count].avg(10800)}</expression>
                            <recovery_mode>0</recovery_mode>
                            <recovery_expression/>
                            <name>BGP Peer {#PEERNAME} is lost more than 10% of prefixes on {HOST.NAME}</name>
                            <correlation_mode>0</correlation_mode>
                            <correlation_tag/>
                            <url/>
                            <status>0</status>
                            <priority>2</priority>
                            <description/>
                            <type>0</type>
                            <manual_close>0</manual_close>
                            <dependencies>
                                <dependency>
                                    <name>BGP Peer {#PEERNAME} is DOWN</name>
                                    <expression>{Template Mikrotik BGPv4:mikrotik.bgp.node[{#PEERNAME},disabled].last(0)}=0 and {Template Mikrotik BGPv4:mikrotik.bgp.node[{#PEERNAME},state].last(#3)}&lt;&gt;6</expression>
                                    <recovery_expression/>
                                </dependency>
                                <dependency>
                                    <name>BGP Peer {#PEERNAME} is lost more than 20% of prefixes on {HOST.NAME}</name>
                                    <expression>{Template Mikrotik BGPv4:mikrotik.bgp.node[{#PEERNAME},prefix-count].last()}&lt;0.8*{Template Mikrotik BGPv4:mikrotik.bgp.node[{#PEERNAME},prefix-count].avg(10800)}</expression>
                                    <recovery_expression/>
                                </dependency>
                            </dependencies>
                            <tags/>
                        </trigger_prototype>
                        <trigger_prototype>
                            <expression>{Template Mikrotik BGPv4:mikrotik.bgp.node[{#PEERNAME},prefix-count].last()}&lt;0.8*{Template Mikrotik BGPv4:mikrotik.bgp.node[{#PEERNAME},prefix-count].avg(10800)}</expression>
                            <recovery_mode>0</recovery_mode>
                            <recovery_expression/>
                            <name>BGP Peer {#PEERNAME} is lost more than 20% of prefixes on {HOST.NAME}</name>
                            <correlation_mode>0</correlation_mode>
                            <correlation_tag/>
                            <url/>
                            <status>0</status>
                            <priority>3</priority>
                            <description/>
                            <type>0</type>
                            <manual_close>0</manual_close>
                            <dependencies>
                                <dependency>
                                    <name>BGP Peer {#PEERNAME} is DOWN</name>
                                    <expression>{Template Mikrotik BGPv4:mikrotik.bgp.node[{#PEERNAME},disabled].last(0)}=0 and {Template Mikrotik BGPv4:mikrotik.bgp.node[{#PEERNAME},state].last(#3)}&lt;&gt;6</expression>
                                    <recovery_expression/>
                                </dependency>
                                <dependency>
                                    <name>BGP Peer {#PEERNAME} is lost more than 30% of prefixes on {HOST.NAME}</name>
                                    <expression>{Template Mikrotik BGPv4:mikrotik.bgp.node[{#PEERNAME},prefix-count].last()}&lt;0.7*{Template Mikrotik BGPv4:mikrotik.bgp.node[{#PEERNAME},prefix-count].avg(10800)}</expression>
                                    <recovery_expression/>
                                </dependency>
                            </dependencies>
                            <tags/>
                        </trigger_prototype>
                        <trigger_prototype>
                            <expression>{Template Mikrotik BGPv4:mikrotik.bgp.node[{#PEERNAME},prefix-count].last()}&lt;0.7*{Template Mikrotik BGPv4:mikrotik.bgp.node[{#PEERNAME},prefix-count].avg(10800)}</expression>
                            <recovery_mode>0</recovery_mode>
                            <recovery_expression/>
                            <name>BGP Peer {#PEERNAME} is lost more than 30% of prefixes on {HOST.NAME}</name>
                            <correlation_mode>0</correlation_mode>
                            <correlation_tag/>
                            <url/>
                            <status>0</status>
                            <priority>4</priority>
                            <description/>
                            <type>0</type>
                            <manual_close>0</manual_close>
                            <dependencies>
                                <dependency>
                                    <name>BGP Peer {#PEERNAME} is DOWN</name>
                                    <expression>{Template Mikrotik BGPv4:mikrotik.bgp.node[{#PEERNAME},disabled].last(0)}=0 and {Template Mikrotik BGPv4:mikrotik.bgp.node[{#PEERNAME},state].last(#3)}&lt;&gt;6</expression>
                                    <recovery_expression/>
                                </dependency>
                            </dependencies>
                            <tags/>
                        </trigger_prototype>
                        <trigger_prototype>
                            <expression>{Template Mikrotik BGPv4:mikrotik.bgp.node[{#PEERNAME},uptime].last()}&lt;600</expression>
                            <recovery_mode>0</recovery_mode>
                            <recovery_expression/>
                            <name>BGP Session with {#PEERNAME} had been restarted</name>
                            <correlation_mode>0</correlation_mode>
                            <correlation_tag/>
                            <url/>
                            <status>0</status>
                            <priority>2</priority>
                            <description/>
                            <type>0</type>
                            <manual_close>0</manual_close>
                            <dependencies/>
                            <tags/>
                        </trigger_prototype>
                        <trigger_prototype>
                            <expression>{Template Mikrotik BGPv4:mikrotik.bgp.node[{#PEERNAME},prefix-count].last()}=0</expression>
                            <recovery_mode>0</recovery_mode>
                            <recovery_expression/>
                            <name>No Prefixes from BGP peer {#PEERNAME}</name>
                            <correlation_mode>0</correlation_mode>
                            <correlation_tag/>
                            <url/>
                            <status>0</status>
                            <priority>5</priority>
                            <description/>
                            <type>0</type>
                            <manual_close>0</manual_close>
                            <dependencies/>
                            <tags/>
                        </trigger_prototype>
                    </trigger_prototypes>
                    <graph_prototypes>
                        <graph_prototype>
                            <name>BGP Accepted Prefixes for peer {#PEERNAME}</name>
                            <width>1000</width>
                            <height>300</height>
                            <yaxismin>0.0000</yaxismin>
                            <yaxismax>100.0000</yaxismax>
                            <show_work_period>1</show_work_period>
                            <show_triggers>1</show_triggers>
                            <type>0</type>
                            <show_legend>1</show_legend>
                            <show_3d>0</show_3d>
                            <percent_left>0.0000</percent_left>
                            <percent_right>0.0000</percent_right>
                            <ymin_type_1>0</ymin_type_1>
                            <ymax_type_1>0</ymax_type_1>
                            <ymin_item_1>0</ymin_item_1>
                            <ymax_item_1>0</ymax_item_1>
                            <graph_items>
                                <graph_item>
                                    <sortorder>0</sortorder>
                                    <drawtype>5</drawtype>
                                    <color>1A7C11</color>
                                    <yaxisside>0</yaxisside>
                                    <calc_fnc>2</calc_fnc>
                                    <type>0</type>
                                    <item>
                                        <host>Template Mikrotik BGPv4</host>
                                        <key>mikrotik.bgp.node[{#PEERNAME},prefix-count]</key>
                                    </item>
                                </graph_item>
                            </graph_items>
                        </graph_prototype>
                        <graph_prototype>
                            <name>BGP Established time with peer {#PEERNAME}</name>
                            <width>1000</width>
                            <height>300</height>
                            <yaxismin>0.0000</yaxismin>
                            <yaxismax>100.0000</yaxismax>
                            <show_work_period>1</show_work_period>
                            <show_triggers>1</show_triggers>
                            <type>0</type>
                            <show_legend>1</show_legend>
                            <show_3d>0</show_3d>
                            <percent_left>0.0000</percent_left>
                            <percent_right>0.0000</percent_right>
                            <ymin_type_1>0</ymin_type_1>
                            <ymax_type_1>0</ymax_type_1>
                            <ymin_item_1>0</ymin_item_1>
                            <ymax_item_1>0</ymax_item_1>
                            <graph_items>
                                <graph_item>
                                    <sortorder>0</sortorder>
                                    <drawtype>5</drawtype>
                                    <color>BB00BB</color>
                                    <yaxisside>0</yaxisside>
                                    <calc_fnc>2</calc_fnc>
                                    <type>0</type>
                                    <item>
                                        <host>Template Mikrotik BGPv4</host>
                                        <key>mikrotik.bgp.node[{#PEERNAME},uptime]</key>
                                    </item>
                                </graph_item>
                            </graph_items>
                        </graph_prototype>
                        <graph_prototype>
                            <name>BGP Updates stats for peer {#PEERNAME}</name>
                            <width>1000</width>
                            <height>300</height>
                            <yaxismin>0.0000</yaxismin>
                            <yaxismax>100.0000</yaxismax>
                            <show_work_period>1</show_work_period>
                            <show_triggers>1</show_triggers>
                            <type>0</type>
                            <show_legend>1</show_legend>
                            <show_3d>0</show_3d>
                            <percent_left>0.0000</percent_left>
                            <percent_right>0.0000</percent_right>
                            <ymin_type_1>0</ymin_type_1>
                            <ymax_type_1>0</ymax_type_1>
                            <ymin_item_1>0</ymin_item_1>
                            <ymax_item_1>0</ymax_item_1>
                            <graph_items>
                                <graph_item>
                                    <sortorder>0</sortorder>
                                    <drawtype>5</drawtype>
                                    <color>1A7C11</color>
                                    <yaxisside>0</yaxisside>
                                    <calc_fnc>2</calc_fnc>
                                    <type>0</type>
                                    <item>
                                        <host>Template Mikrotik BGPv4</host>
                                        <key>mikrotik.bgp.node[{#PEERNAME},updates-sent]</key>
                                    </item>
                                </graph_item>
                                <graph_item>
                                    <sortorder>1</sortorder>
                                    <drawtype>5</drawtype>
                                    <color>0000EE</color>
                                    <yaxisside>0</yaxisside>
                                    <calc_fnc>2</calc_fnc>
                                    <type>0</type>
                                    <item>
                                        <host>Template Mikrotik BGPv4</host>
                                        <key>mikrotik.bgp.node[{#PEERNAME},updates-received]</key>
                                    </item>
                                </graph_item>
                            </graph_items>
                        </graph_prototype>
                        <graph_prototype>
                            <name>BGP Withdraws stats for peer {#PEERNAME}</name>
                            <width>1000</width>
                            <height>300</height>
                            <yaxismin>0.0000</yaxismin>
                            <yaxismax>100.0000</yaxismax>
                            <show_work_period>1</show_work_period>
                            <show_triggers>1</show_triggers>
                            <type>0</type>
                            <show_legend>1</show_legend>
                            <show_3d>0</show_3d>
                            <percent_left>0.0000</percent_left>
                            <percent_right>0.0000</percent_right>
                            <ymin_type_1>0</ymin_type_1>
                            <ymax_type_1>0</ymax_type_1>
                            <ymin_item_1>0</ymin_item_1>
                            <ymax_item_1>0</ymax_item_1>
                            <graph_items>
                                <graph_item>
                                    <sortorder>0</sortorder>
                                    <drawtype>0</drawtype>
                                    <color>00DD00</color>
                                    <yaxisside>0</yaxisside>
                                    <calc_fnc>2</calc_fnc>
                                    <type>0</type>
                                    <item>
                                        <host>Template Mikrotik BGPv4</host>
                                        <key>mikrotik.bgp.node[{#PEERNAME},withdrawn-sent]</key>
                                    </item>
                                </graph_item>
                                <graph_item>
                                    <sortorder>1</sortorder>
                                    <drawtype>0</drawtype>
                                    <color>AA0000</color>
                                    <yaxisside>0</yaxisside>
                                    <calc_fnc>2</calc_fnc>
                                    <type>0</type>
                                    <item>
                                        <host>Template Mikrotik BGPv4</host>
                                        <key>mikrotik.bgp.node[{#PEERNAME},withdrawn-received]</key>
                                    </item>
                                </graph_item>
                            </graph_items>
                        </graph_prototype>
                    </graph_prototypes>
                    <host_prototypes/>
                </discovery_rule>
            </discovery_rules>
            <httptests/>
            <macros/>
            <templates/>
            <screens/>
        </template>
    </templates>
    <value_maps>
        <value_map>
            <name>ciscoBgpPeerState</name>
            <mappings>
                <mapping>
                    <value>0</value>
                    <newvalue>Weird</newvalue>
                </mapping>
                <mapping>
                    <value>1</value>
                    <newvalue>Idle</newvalue>
                </mapping>
                <mapping>
                    <value>2</value>
                    <newvalue>Connect</newvalue>
                </mapping>
                <mapping>
                    <value>3</value>
                    <newvalue>Active</newvalue>
                </mapping>
                <mapping>
                    <value>4</value>
                    <newvalue>OpenSent</newvalue>
                </mapping>
                <mapping>
                    <value>5</value>
                    <newvalue>OpenConfirm</newvalue>
                </mapping>
                <mapping>
                    <value>6</value>
                    <newvalue>Established</newvalue>
                </mapping>
            </mappings>
        </value_map>
        <value_map>
            <name>Mikrotik BGP Administrative Status</name>
            <mappings>
                <mapping>
                    <value>0</value>
                    <newvalue>Up</newvalue>
                </mapping>
                <mapping>
                    <value>1</value>
                    <newvalue>Down</newvalue>
                </mapping>
            </mappings>
        </value_map>
    </value_maps>
</zabbix_export>


File: /zabbix_templates\zbx_template_firewall_stats.xml
<?xml version="1.0" encoding="UTF-8"?>
<zabbix_export>
    <version>3.2</version>
    <date>2019-06-30T18:57:22Z</date>
    <groups>
        <group>
            <name>Custom Templates</name>
        </group>
        <group>
            <name>Templates</name>
        </group>
    </groups>
    <templates>
        <template>
            <template>Template Mikrotik Firewall Statistics</template>
            <name>Template Mikrotik Firewall Statistics</name>
            <description>Monitors the stats coming from Mikrotik Firewall</description>
            <groups>
                <group>
                    <name>Custom Templates</name>
                </group>
                <group>
                    <name>Templates</name>
                </group>
            </groups>
            <applications>
                <application>
                    <name>Mikrotik Firewall Stats</name>
                </application>
            </applications>
            <items/>
            <discovery_rules>
                <discovery_rule>
                    <name>Mikrotik Firewall Rules</name>
                    <type>2</type>
                    <snmp_community/>
                    <snmp_oid/>
                    <key>mikrotik.firewall.discovery</key>
                    <delay>0</delay>
                    <status>0</status>
                    <allowed_hosts>127.0.0.1</allowed_hosts>
                    <snmpv3_contextname/>
                    <snmpv3_securityname/>
                    <snmpv3_securitylevel>0</snmpv3_securitylevel>
                    <snmpv3_authprotocol>0</snmpv3_authprotocol>
                    <snmpv3_authpassphrase/>
                    <snmpv3_privprotocol>0</snmpv3_privprotocol>
                    <snmpv3_privpassphrase/>
                    <delay_flex/>
                    <params/>
                    <ipmi_sensor/>
                    <authtype>0</authtype>
                    <username/>
                    <password/>
                    <publickey/>
                    <privatekey/>
                    <port/>
                    <filter>
                        <evaltype>0</evaltype>
                        <formula/>
                        <conditions/>
                    </filter>
                    <lifetime>3</lifetime>
                    <description>The rules discovers Mikrotik's Firewall Rules. They must have a comments, which starts with ZBX word.</description>
                    <item_prototypes>
                        <item_prototype>
                            <name>Bytes/sec for {#MTIK_FW_RULE_COMMENT}</name>
                            <type>2</type>
                            <snmp_community/>
                            <multiplier>0</multiplier>
                            <snmp_oid/>
                            <key>mikrotik.firewall[{#MTIK_FW_RULE_ID},bytes]</key>
                            <delay>0</delay>
                            <history>7</history>
                            <trends>180</trends>
                            <status>0</status>
                            <value_type>3</value_type>
                            <allowed_hosts>127.0.0.1</allowed_hosts>
                            <units>bps</units>
                            <delta>1</delta>
                            <snmpv3_contextname/>
                            <snmpv3_securityname/>
                            <snmpv3_securitylevel>0</snmpv3_securitylevel>
                            <snmpv3_authprotocol>0</snmpv3_authprotocol>
                            <snmpv3_authpassphrase/>
                            <snmpv3_privprotocol>0</snmpv3_privprotocol>
                            <snmpv3_privpassphrase/>
                            <formula>1</formula>
                            <delay_flex/>
                            <params/>
                            <ipmi_sensor/>
                            <data_type>0</data_type>
                            <authtype>0</authtype>
                            <username/>
                            <password/>
                            <publickey/>
                            <privatekey/>
                            <port/>
                            <description>Bytes per sec over firewall rule</description>
                            <inventory_link>0</inventory_link>
                            <applications>
                                <application>
                                    <name>Mikrotik Firewall Stats</name>
                                </application>
                            </applications>
                            <valuemap/>
                            <logtimefmt/>
                            <application_prototypes/>
                        </item_prototype>
                        <item_prototype>
                            <name>Administrative status for {#MTIK_FW_RULE_COMMENT}</name>
                            <type>2</type>
                            <snmp_community/>
                            <multiplier>0</multiplier>
                            <snmp_oid/>
                            <key>mikrotik.firewall[{#MTIK_FW_RULE_ID},disabled]</key>
                            <delay>0</delay>
                            <history>7</history>
                            <trends>180</trends>
                            <status>0</status>
                            <value_type>3</value_type>
                            <allowed_hosts>127.0.0.1</allowed_hosts>
                            <units/>
                            <delta>0</delta>
                            <snmpv3_contextname/>
                            <snmpv3_securityname/>
                            <snmpv3_securitylevel>0</snmpv3_securitylevel>
                            <snmpv3_authprotocol>0</snmpv3_authprotocol>
                            <snmpv3_authpassphrase/>
                            <snmpv3_privprotocol>0</snmpv3_privprotocol>
                            <snmpv3_privpassphrase/>
                            <formula>1</formula>
                            <delay_flex/>
                            <params/>
                            <ipmi_sensor/>
                            <data_type>3</data_type>
                            <authtype>0</authtype>
                            <username/>
                            <password/>
                            <publickey/>
                            <privatekey/>
                            <port/>
                            <description>Administrative status of the firewall rule</description>
                            <inventory_link>0</inventory_link>
                            <applications>
                                <application>
                                    <name>Mikrotik Firewall Stats</name>
                                </application>
                            </applications>
                            <valuemap>
                                <name>Mikrotik Firewall Rule Status</name>
                            </valuemap>
                            <logtimefmt/>
                            <application_prototypes/>
                        </item_prototype>
                        <item_prototype>
                            <name>Packets/sec for {#MTIK_FW_RULE_COMMENT}</name>
                            <type>2</type>
                            <snmp_community/>
                            <multiplier>0</multiplier>
                            <snmp_oid/>
                            <key>mikrotik.firewall[{#MTIK_FW_RULE_ID},packets]</key>
                            <delay>0</delay>
                            <history>7</history>
                            <trends>180</trends>
                            <status>0</status>
                            <value_type>3</value_type>
                            <allowed_hosts>127.0.0.1</allowed_hosts>
                            <units>pps</units>
                            <delta>1</delta>
                            <snmpv3_contextname/>
                            <snmpv3_securityname/>
                            <snmpv3_securitylevel>0</snmpv3_securitylevel>
                            <snmpv3_authprotocol>0</snmpv3_authprotocol>
                            <snmpv3_authpassphrase/>
                            <snmpv3_privprotocol>0</snmpv3_privprotocol>
                            <snmpv3_privpassphrase/>
                            <formula>1</formula>
                            <delay_flex/>
                            <params/>
                            <ipmi_sensor/>
                            <data_type>0</data_type>
                            <authtype>0</authtype>
                            <username/>
                            <password/>
                            <publickey/>
                            <privatekey/>
                            <port/>
                            <description>Packets per sec over firewall rule</description>
                            <inventory_link>0</inventory_link>
                            <applications>
                                <application>
                                    <name>Mikrotik Firewall Stats</name>
                                </application>
                            </applications>
                            <valuemap/>
                            <logtimefmt/>
                            <application_prototypes/>
                        </item_prototype>
                    </item_prototypes>
                    <trigger_prototypes/>
                    <graph_prototypes>
                        <graph_prototype>
                            <name>Firewall stats metrics for {#MTIK_FW_RULE_COMMENT}</name>
                            <width>1000</width>
                            <height>300</height>
                            <yaxismin>0.0000</yaxismin>
                            <yaxismax>100.0000</yaxismax>
                            <show_work_period>1</show_work_period>
                            <show_triggers>1</show_triggers>
                            <type>0</type>
                            <show_legend>1</show_legend>
                            <show_3d>0</show_3d>
                            <percent_left>0.0000</percent_left>
                            <percent_right>0.0000</percent_right>
                            <ymin_type_1>0</ymin_type_1>
                            <ymax_type_1>0</ymax_type_1>
                            <ymin_item_1>0</ymin_item_1>
                            <ymax_item_1>0</ymax_item_1>
                            <graph_items>
                                <graph_item>
                                    <sortorder>0</sortorder>
                                    <drawtype>5</drawtype>
                                    <color>1A7C11</color>
                                    <yaxisside>0</yaxisside>
                                    <calc_fnc>2</calc_fnc>
                                    <type>0</type>
                                    <item>
                                        <host>Template Mikrotik Firewall Statistics</host>
                                        <key>mikrotik.firewall[{#MTIK_FW_RULE_ID},bytes]</key>
                                    </item>
                                </graph_item>
                                <graph_item>
                                    <sortorder>1</sortorder>
                                    <drawtype>5</drawtype>
                                    <color>F63100</color>
                                    <yaxisside>1</yaxisside>
                                    <calc_fnc>2</calc_fnc>
                                    <type>0</type>
                                    <item>
                                        <host>Template Mikrotik Firewall Statistics</host>
                                        <key>mikrotik.firewall[{#MTIK_FW_RULE_ID},packets]</key>
                                    </item>
                                </graph_item>
                            </graph_items>
                        </graph_prototype>
                    </graph_prototypes>
                    <host_prototypes/>
                </discovery_rule>
            </discovery_rules>
            <httptests/>
            <macros/>
            <templates/>
            <screens/>
        </template>
    </templates>
    <value_maps>
        <value_map>
            <name>Mikrotik Firewall Rule Status</name>
            <mappings>
                <mapping>
                    <value>0</value>
                    <newvalue>enabled</newvalue>
                </mapping>
                <mapping>
                    <value>1</value>
                    <newvalue>disabled</newvalue>
                </mapping>
            </mappings>
        </value_map>
    </value_maps>
</zabbix_export>


File: /zabbix_templates\zbx_template_IRQ_Counters.xml
<?xml version="1.0" encoding="UTF-8"?>
<zabbix_export>
    <version>3.2</version>
    <date>2019-06-30T11:56:34Z</date>
    <groups>
        <group>
            <name>Custom Templates</name>
        </group>
        <group>
            <name>Templates</name>
        </group>
    </groups>
    <templates>
        <template>
            <template>Template Mikrotik IRQ Counters</template>
            <name>Template Mikrotik IRQ Counters</name>
            <description>Monitors IRQ counters using Zabbix active checks</description>
            <groups>
                <group>
                    <name>Custom Templates</name>
                </group>
                <group>
                    <name>Templates</name>
                </group>
            </groups>
            <applications>
                <application>
                    <name>Mikrotik IRQ Counters</name>
                </application>
            </applications>
            <items/>
            <discovery_rules>
                <discovery_rule>
                    <name>Mikrotik IRQs</name>
                    <type>2</type>
                    <snmp_community/>
                    <snmp_oid/>
                    <key>mikrotik.irq.discovery</key>
                    <delay>0</delay>
                    <status>0</status>
                    <allowed_hosts>127.0.0.1</allowed_hosts>
                    <snmpv3_contextname/>
                    <snmpv3_securityname/>
                    <snmpv3_securitylevel>0</snmpv3_securitylevel>
                    <snmpv3_authprotocol>0</snmpv3_authprotocol>
                    <snmpv3_authpassphrase/>
                    <snmpv3_privprotocol>0</snmpv3_privprotocol>
                    <snmpv3_privpassphrase/>
                    <delay_flex/>
                    <params/>
                    <ipmi_sensor/>
                    <authtype>0</authtype>
                    <username/>
                    <password/>
                    <publickey/>
                    <privatekey/>
                    <port/>
                    <filter>
                        <evaltype>0</evaltype>
                        <formula/>
                        <conditions/>
                    </filter>
                    <lifetime>3</lifetime>
                    <description>Explores for the current IRQs</description>
                    <item_prototypes>
                        <item_prototype>
                            <name>System - Resources - IRQ {#IRQ}: Counter</name>
                            <type>2</type>
                            <snmp_community/>
                            <multiplier>0</multiplier>
                            <snmp_oid/>
                            <key>mikrotik.irq[{#IRQ}]</key>
                            <delay>0</delay>
                            <history>90</history>
                            <trends>365</trends>
                            <status>0</status>
                            <value_type>3</value_type>
                            <allowed_hosts>127.0.0.1</allowed_hosts>
                            <units/>
                            <delta>1</delta>
                            <snmpv3_contextname/>
                            <snmpv3_securityname/>
                            <snmpv3_securitylevel>0</snmpv3_securitylevel>
                            <snmpv3_authprotocol>0</snmpv3_authprotocol>
                            <snmpv3_authpassphrase/>
                            <snmpv3_privprotocol>0</snmpv3_privprotocol>
                            <snmpv3_privpassphrase/>
                            <formula>1</formula>
                            <delay_flex/>
                            <params/>
                            <ipmi_sensor/>
                            <data_type>0</data_type>
                            <authtype>0</authtype>
                            <username/>
                            <password/>
                            <publickey/>
                            <privatekey/>
                            <port/>
                            <description/>
                            <inventory_link>0</inventory_link>
                            <applications>
                                <application>
                                    <name>Mikrotik IRQ Counters</name>
                                </application>
                            </applications>
                            <valuemap/>
                            <logtimefmt/>
                            <application_prototypes/>
                        </item_prototype>
                    </item_prototypes>
                    <trigger_prototypes/>
                    <graph_prototypes>
                        <graph_prototype>
                            <name>System - Resources - IRQ {#IRQ}: Counter</name>
                            <width>1000</width>
                            <height>300</height>
                            <yaxismin>0.0000</yaxismin>
                            <yaxismax>100.0000</yaxismax>
                            <show_work_period>1</show_work_period>
                            <show_triggers>1</show_triggers>
                            <type>0</type>
                            <show_legend>1</show_legend>
                            <show_3d>0</show_3d>
                            <percent_left>0.0000</percent_left>
                            <percent_right>0.0000</percent_right>
                            <ymin_type_1>0</ymin_type_1>
                            <ymax_type_1>0</ymax_type_1>
                            <ymin_item_1>0</ymin_item_1>
                            <ymax_item_1>0</ymax_item_1>
                            <graph_items>
                                <graph_item>
                                    <sortorder>0</sortorder>
                                    <drawtype>5</drawtype>
                                    <color>550055</color>
                                    <yaxisside>0</yaxisside>
                                    <calc_fnc>2</calc_fnc>
                                    <type>0</type>
                                    <item>
                                        <host>Template Mikrotik IRQ Counters</host>
                                        <key>mikrotik.irq[{#IRQ}]</key>
                                    </item>
                                </graph_item>
                            </graph_items>
                        </graph_prototype>
                    </graph_prototypes>
                    <host_prototypes/>
                </discovery_rule>
            </discovery_rules>
            <httptests/>
            <macros/>
            <templates/>
            <screens/>
        </template>
    </templates>
</zabbix_export>


File: /zabbix_templates\zbx_template_Radius_Counters.xml
<?xml version="1.0" encoding="UTF-8"?>
<zabbix_export>
    <version>3.2</version>
    <date>2019-06-30T11:55:49Z</date>
    <groups>
        <group>
            <name>Custom Templates</name>
        </group>
        <group>
            <name>Templates</name>
        </group>
    </groups>
    <templates>
        <template>
            <template>Template Mikrotik Radius Counters</template>
            <name>Template Mikrotik Radius Counters</name>
            <description>Monitors RADIUS counters using Zabbix active checks</description>
            <groups>
                <group>
                    <name>Custom Templates</name>
                </group>
                <group>
                    <name>Templates</name>
                </group>
            </groups>
            <applications>
                <application>
                    <name>Mikrotik Radius Counters</name>
                </application>
            </applications>
            <items>
                <item>
                    <name>Radius CoA: Acknowledged</name>
                    <type>2</type>
                    <snmp_community/>
                    <multiplier>0</multiplier>
                    <snmp_oid/>
                    <key>mikrotik.radius-in.coa[acks]</key>
                    <delay>0</delay>
                    <history>30</history>
                    <trends>365</trends>
                    <status>0</status>
                    <value_type>3</value_type>
                    <allowed_hosts>127.0.0.1</allowed_hosts>
                    <units/>
                    <delta>1</delta>
                    <snmpv3_contextname/>
                    <snmpv3_securityname/>
                    <snmpv3_securitylevel>0</snmpv3_securitylevel>
                    <snmpv3_authprotocol>0</snmpv3_authprotocol>
                    <snmpv3_authpassphrase/>
                    <snmpv3_privprotocol>0</snmpv3_privprotocol>
                    <snmpv3_privpassphrase/>
                    <formula>1</formula>
                    <delay_flex/>
                    <params/>
                    <ipmi_sensor/>
                    <data_type>0</data_type>
                    <authtype>0</authtype>
                    <username/>
                    <password/>
                    <publickey/>
                    <privatekey/>
                    <port/>
                    <description/>
                    <inventory_link>0</inventory_link>
                    <applications>
                        <application>
                            <name>Mikrotik Radius Counters</name>
                        </application>
                    </applications>
                    <valuemap/>
                    <logtimefmt/>
                </item>
                <item>
                    <name>Radius CoA: Bad Requests</name>
                    <type>2</type>
                    <snmp_community/>
                    <multiplier>0</multiplier>
                    <snmp_oid/>
                    <key>mikrotik.radius-in.coa[bad-requests]</key>
                    <delay>0</delay>
                    <history>30</history>
                    <trends>365</trends>
                    <status>0</status>
                    <value_type>3</value_type>
                    <allowed_hosts>127.0.0.1</allowed_hosts>
                    <units/>
                    <delta>1</delta>
                    <snmpv3_contextname/>
                    <snmpv3_securityname/>
                    <snmpv3_securitylevel>0</snmpv3_securitylevel>
                    <snmpv3_authprotocol>0</snmpv3_authprotocol>
                    <snmpv3_authpassphrase/>
                    <snmpv3_privprotocol>0</snmpv3_privprotocol>
                    <snmpv3_privpassphrase/>
                    <formula>1</formula>
                    <delay_flex/>
                    <params/>
                    <ipmi_sensor/>
                    <data_type>0</data_type>
                    <authtype>0</authtype>
                    <username/>
                    <password/>
                    <publickey/>
                    <privatekey/>
                    <port/>
                    <description/>
                    <inventory_link>0</inventory_link>
                    <applications>
                        <application>
                            <name>Mikrotik Radius Counters</name>
                        </application>
                    </applications>
                    <valuemap/>
                    <logtimefmt/>
                </item>
                <item>
                    <name>Radius CoA: Rejects</name>
                    <type>2</type>
                    <snmp_community/>
                    <multiplier>0</multiplier>
                    <snmp_oid/>
                    <key>mikrotik.radius-in.coa[naks]</key>
                    <delay>0</delay>
                    <history>30</history>
                    <trends>365</trends>
                    <status>0</status>
                    <value_type>3</value_type>
                    <allowed_hosts>127.0.0.1</allowed_hosts>
                    <units/>
                    <delta>1</delta>
                    <snmpv3_contextname/>
                    <snmpv3_securityname/>
                    <snmpv3_securitylevel>0</snmpv3_securitylevel>
                    <snmpv3_authprotocol>0</snmpv3_authprotocol>
                    <snmpv3_authpassphrase/>
                    <snmpv3_privprotocol>0</snmpv3_privprotocol>
                    <snmpv3_privpassphrase/>
                    <formula>1</formula>
                    <delay_flex/>
                    <params/>
                    <ipmi_sensor/>
                    <data_type>0</data_type>
                    <authtype>0</authtype>
                    <username/>
                    <password/>
                    <publickey/>
                    <privatekey/>
                    <port/>
                    <description/>
                    <inventory_link>0</inventory_link>
                    <applications>
                        <application>
                            <name>Mikrotik Radius Counters</name>
                        </application>
                    </applications>
                    <valuemap/>
                    <logtimefmt/>
                </item>
                <item>
                    <name>Radius CoA: Requests</name>
                    <type>2</type>
                    <snmp_community/>
                    <multiplier>0</multiplier>
                    <snmp_oid/>
                    <key>mikrotik.radius-in.coa[requests]</key>
                    <delay>0</delay>
                    <history>30</history>
                    <trends>365</trends>
                    <status>0</status>
                    <value_type>3</value_type>
                    <allowed_hosts>127.0.0.1</allowed_hosts>
                    <units/>
                    <delta>1</delta>
                    <snmpv3_contextname/>
                    <snmpv3_securityname/>
                    <snmpv3_securitylevel>0</snmpv3_securitylevel>
                    <snmpv3_authprotocol>0</snmpv3_authprotocol>
                    <snmpv3_authpassphrase/>
                    <snmpv3_privprotocol>0</snmpv3_privprotocol>
                    <snmpv3_privpassphrase/>
                    <formula>1</formula>
                    <delay_flex/>
                    <params/>
                    <ipmi_sensor/>
                    <data_type>0</data_type>
                    <authtype>0</authtype>
                    <username/>
                    <password/>
                    <publickey/>
                    <privatekey/>
                    <port/>
                    <description/>
                    <inventory_link>0</inventory_link>
                    <applications>
                        <application>
                            <name>Mikrotik Radius Counters</name>
                        </application>
                    </applications>
                    <valuemap/>
                    <logtimefmt/>
                </item>
            </items>
            <discovery_rules>
                <discovery_rule>
                    <name>Mikrotik Radius Clients</name>
                    <type>2</type>
                    <snmp_community/>
                    <snmp_oid/>
                    <key>mikrotik.radius-out.discovery</key>
                    <delay>0</delay>
                    <status>0</status>
                    <allowed_hosts>127.0.0.1</allowed_hosts>
                    <snmpv3_contextname/>
                    <snmpv3_securityname/>
                    <snmpv3_securitylevel>0</snmpv3_securitylevel>
                    <snmpv3_authprotocol>0</snmpv3_authprotocol>
                    <snmpv3_authpassphrase/>
                    <snmpv3_privprotocol>0</snmpv3_privprotocol>
                    <snmpv3_privpassphrase/>
                    <delay_flex/>
                    <params/>
                    <ipmi_sensor/>
                    <authtype>0</authtype>
                    <username/>
                    <password/>
                    <publickey/>
                    <privatekey/>
                    <port/>
                    <filter>
                        <evaltype>0</evaltype>
                        <formula/>
                        <conditions/>
                    </filter>
                    <lifetime>3</lifetime>
                    <description>Explores for the current Radius Clients</description>
                    <item_prototypes>
                        <item_prototype>
                            <name>Radius Client {#MTIK_RADIUS_COMMENT}: Accepts</name>
                            <type>2</type>
                            <snmp_community/>
                            <multiplier>0</multiplier>
                            <snmp_oid/>
                            <key>mikrotik.radius-out.node[{#MTIK_RADIUS_ID},accepts]</key>
                            <delay>0</delay>
                            <history>90</history>
                            <trends>365</trends>
                            <status>0</status>
                            <value_type>3</value_type>
                            <allowed_hosts>127.0.0.1</allowed_hosts>
                            <units/>
                            <delta>1</delta>
                            <snmpv3_contextname/>
                            <snmpv3_securityname/>
                            <snmpv3_securitylevel>0</snmpv3_securitylevel>
                            <snmpv3_authprotocol>0</snmpv3_authprotocol>
                            <snmpv3_authpassphrase/>
                            <snmpv3_privprotocol>0</snmpv3_privprotocol>
                            <snmpv3_privpassphrase/>
                            <formula>1</formula>
                            <delay_flex/>
                            <params/>
                            <ipmi_sensor/>
                            <data_type>0</data_type>
                            <authtype>0</authtype>
                            <username/>
                            <password/>
                            <publickey/>
                            <privatekey/>
                            <port/>
                            <description/>
                            <inventory_link>0</inventory_link>
                            <applications>
                                <application>
                                    <name>Mikrotik Radius Counters</name>
                                </application>
                            </applications>
                            <valuemap/>
                            <logtimefmt/>
                            <application_prototypes/>
                        </item_prototype>
                        <item_prototype>
                            <name>Radius Client {#MTIK_RADIUS_COMMENT}: Bad Replies</name>
                            <type>2</type>
                            <snmp_community/>
                            <multiplier>0</multiplier>
                            <snmp_oid/>
                            <key>mikrotik.radius-out.node[{#MTIK_RADIUS_ID},bad-replies]</key>
                            <delay>0</delay>
                            <history>90</history>
                            <trends>365</trends>
                            <status>0</status>
                            <value_type>3</value_type>
                            <allowed_hosts>127.0.0.1</allowed_hosts>
                            <units/>
                            <delta>1</delta>
                            <snmpv3_contextname/>
                            <snmpv3_securityname/>
                            <snmpv3_securitylevel>0</snmpv3_securitylevel>
                            <snmpv3_authprotocol>0</snmpv3_authprotocol>
                            <snmpv3_authpassphrase/>
                            <snmpv3_privprotocol>0</snmpv3_privprotocol>
                            <snmpv3_privpassphrase/>
                            <formula>1</formula>
                            <delay_flex/>
                            <params/>
                            <ipmi_sensor/>
                            <data_type>0</data_type>
                            <authtype>0</authtype>
                            <username/>
                            <password/>
                            <publickey/>
                            <privatekey/>
                            <port/>
                            <description/>
                            <inventory_link>0</inventory_link>
                            <applications>
                                <application>
                                    <name>Mikrotik Radius Counters</name>
                                </application>
                            </applications>
                            <valuemap/>
                            <logtimefmt/>
                            <application_prototypes/>
                        </item_prototype>
                        <item_prototype>
                            <name>Radius Client {#MTIK_RADIUS_COMMENT}: Pending Requests</name>
                            <type>2</type>
                            <snmp_community/>
                            <multiplier>0</multiplier>
                            <snmp_oid/>
                            <key>mikrotik.radius-out.node[{#MTIK_RADIUS_ID},pending]</key>
                            <delay>0</delay>
                            <history>90</history>
                            <trends>365</trends>
                            <status>0</status>
                            <value_type>3</value_type>
                            <allowed_hosts>127.0.0.1</allowed_hosts>
                            <units/>
                            <delta>0</delta>
                            <snmpv3_contextname/>
                            <snmpv3_securityname/>
                            <snmpv3_securitylevel>0</snmpv3_securitylevel>
                            <snmpv3_authprotocol>0</snmpv3_authprotocol>
                            <snmpv3_authpassphrase/>
                            <snmpv3_privprotocol>0</snmpv3_privprotocol>
                            <snmpv3_privpassphrase/>
                            <formula>1</formula>
                            <delay_flex/>
                            <params/>
                            <ipmi_sensor/>
                            <data_type>0</data_type>
                            <authtype>0</authtype>
                            <username/>
                            <password/>
                            <publickey/>
                            <privatekey/>
                            <port/>
                            <description/>
                            <inventory_link>0</inventory_link>
                            <applications>
                                <application>
                                    <name>Mikrotik Radius Counters</name>
                                </application>
                            </applications>
                            <valuemap/>
                            <logtimefmt/>
                            <application_prototypes/>
                        </item_prototype>
                        <item_prototype>
                            <name>Radius Client {#MTIK_RADIUS_COMMENT}: Rejects</name>
                            <type>2</type>
                            <snmp_community/>
                            <multiplier>0</multiplier>
                            <snmp_oid/>
                            <key>mikrotik.radius-out.node[{#MTIK_RADIUS_ID},rejects]</key>
                            <delay>0</delay>
                            <history>90</history>
                            <trends>365</trends>
                            <status>0</status>
                            <value_type>3</value_type>
                            <allowed_hosts>127.0.0.1</allowed_hosts>
                            <units/>
                            <delta>1</delta>
                            <snmpv3_contextname/>
                            <snmpv3_securityname/>
                            <snmpv3_securitylevel>0</snmpv3_securitylevel>
                            <snmpv3_authprotocol>0</snmpv3_authprotocol>
                            <snmpv3_authpassphrase/>
                            <snmpv3_privprotocol>0</snmpv3_privprotocol>
                            <snmpv3_privpassphrase/>
                            <formula>1</formula>
                            <delay_flex/>
                            <params/>
                            <ipmi_sensor/>
                            <data_type>0</data_type>
                            <authtype>0</authtype>
                            <username/>
                            <password/>
                            <publickey/>
                            <privatekey/>
                            <port/>
                            <description/>
                            <inventory_link>0</inventory_link>
                            <applications>
                                <application>
                                    <name>Mikrotik Radius Counters</name>
                                </application>
                            </applications>
                            <valuemap/>
                            <logtimefmt/>
                            <application_prototypes/>
                        </item_prototype>
                        <item_prototype>
                            <name>Radius Client {#MTIK_RADIUS_COMMENT}: Requests</name>
                            <type>2</type>
                            <snmp_community/>
                            <multiplier>0</multiplier>
                            <snmp_oid/>
                            <key>mikrotik.radius-out.node[{#MTIK_RADIUS_ID},requests]</key>
                            <delay>0</delay>
                            <history>90</history>
                            <trends>365</trends>
                            <status>0</status>
                            <value_type>3</value_type>
                            <allowed_hosts>127.0.0.1</allowed_hosts>
                            <units/>
                            <delta>1</delta>
                            <snmpv3_contextname/>
                            <snmpv3_securityname/>
                            <snmpv3_securitylevel>0</snmpv3_securitylevel>
                            <snmpv3_authprotocol>0</snmpv3_authprotocol>
                            <snmpv3_authpassphrase/>
                            <snmpv3_privprotocol>0</snmpv3_privprotocol>
                            <snmpv3_privpassphrase/>
                            <formula>1</formula>
                            <delay_flex/>
                            <params/>
                            <ipmi_sensor/>
                            <data_type>0</data_type>
                            <authtype>0</authtype>
                            <username/>
                            <password/>
                            <publickey/>
                            <privatekey/>
                            <port/>
                            <description/>
                            <inventory_link>0</inventory_link>
                            <applications>
                                <application>
                                    <name>Mikrotik Radius Counters</name>
                                </application>
                            </applications>
                            <valuemap/>
                            <logtimefmt/>
                            <application_prototypes/>
                        </item_prototype>
                        <item_prototype>
                            <name>Radius Client {#MTIK_RADIUS_COMMENT}: Resends</name>
                            <type>2</type>
                            <snmp_community/>
                            <multiplier>0</multiplier>
                            <snmp_oid/>
                            <key>mikrotik.radius-out.node[{#MTIK_RADIUS_ID},resends]</key>
                            <delay>0</delay>
                            <history>90</history>
                            <trends>365</trends>
                            <status>0</status>
                            <value_type>3</value_type>
                            <allowed_hosts>127.0.0.1</allowed_hosts>
                            <units/>
                            <delta>1</delta>
                            <snmpv3_contextname/>
                            <snmpv3_securityname/>
                            <snmpv3_securitylevel>0</snmpv3_securitylevel>
                            <snmpv3_authprotocol>0</snmpv3_authprotocol>
                            <snmpv3_authpassphrase/>
                            <snmpv3_privprotocol>0</snmpv3_privprotocol>
                            <snmpv3_privpassphrase/>
                            <formula>1</formula>
                            <delay_flex/>
                            <params/>
                            <ipmi_sensor/>
                            <data_type>0</data_type>
                            <authtype>0</authtype>
                            <username/>
                            <password/>
                            <publickey/>
                            <privatekey/>
                            <port/>
                            <description/>
                            <inventory_link>0</inventory_link>
                            <applications>
                                <application>
                                    <name>Mikrotik Radius Counters</name>
                                </application>
                            </applications>
                            <valuemap/>
                            <logtimefmt/>
                            <application_prototypes/>
                        </item_prototype>
                        <item_prototype>
                            <name>Radius Client {#MTIK_RADIUS_COMMENT}: Timeouts</name>
                            <type>2</type>
                            <snmp_community/>
                            <multiplier>0</multiplier>
                            <snmp_oid/>
                            <key>mikrotik.radius-out.node[{#MTIK_RADIUS_ID},timeouts]</key>
                            <delay>0</delay>
                            <history>90</history>
                            <trends>365</trends>
                            <status>0</status>
                            <value_type>3</value_type>
                            <allowed_hosts>127.0.0.1</allowed_hosts>
                            <units/>
                            <delta>1</delta>
                            <snmpv3_contextname/>
                            <snmpv3_securityname/>
                            <snmpv3_securitylevel>0</snmpv3_securitylevel>
                            <snmpv3_authprotocol>0</snmpv3_authprotocol>
                            <snmpv3_authpassphrase/>
                            <snmpv3_privprotocol>0</snmpv3_privprotocol>
                            <snmpv3_privpassphrase/>
                            <formula>1</formula>
                            <delay_flex/>
                            <params/>
                            <ipmi_sensor/>
                            <data_type>0</data_type>
                            <authtype>0</authtype>
                            <username/>
                            <password/>
                            <publickey/>
                            <privatekey/>
                            <port/>
                            <description/>
                            <inventory_link>0</inventory_link>
                            <applications>
                                <application>
                                    <name>Mikrotik Radius Counters</name>
                                </application>
                            </applications>
                            <valuemap/>
                            <logtimefmt/>
                            <application_prototypes/>
                        </item_prototype>
                    </item_prototypes>
                    <trigger_prototypes/>
                    <graph_prototypes>
                        <graph_prototype>
                            <name>Radius Client {#MTIK_RADIUS_COMMENT}: Pending Requests</name>
                            <width>1000</width>
                            <height>300</height>
                            <yaxismin>0.0000</yaxismin>
                            <yaxismax>100.0000</yaxismax>
                            <show_work_period>1</show_work_period>
                            <show_triggers>1</show_triggers>
                            <type>0</type>
                            <show_legend>1</show_legend>
                            <show_3d>0</show_3d>
                            <percent_left>0.0000</percent_left>
                            <percent_right>0.0000</percent_right>
                            <ymin_type_1>0</ymin_type_1>
                            <ymax_type_1>0</ymax_type_1>
                            <ymin_item_1>0</ymin_item_1>
                            <ymax_item_1>0</ymax_item_1>
                            <graph_items>
                                <graph_item>
                                    <sortorder>0</sortorder>
                                    <drawtype>5</drawtype>
                                    <color>F63100</color>
                                    <yaxisside>0</yaxisside>
                                    <calc_fnc>2</calc_fnc>
                                    <type>0</type>
                                    <item>
                                        <host>Template Mikrotik Radius Counters</host>
                                        <key>mikrotik.radius-out.node[{#MTIK_RADIUS_ID},pending]</key>
                                    </item>
                                </graph_item>
                            </graph_items>
                        </graph_prototype>
                        <graph_prototype>
                            <name>Radius Client {#MTIK_RADIUS_COMMENT}: Requests</name>
                            <width>1000</width>
                            <height>300</height>
                            <yaxismin>0.0000</yaxismin>
                            <yaxismax>100.0000</yaxismax>
                            <show_work_period>1</show_work_period>
                            <show_triggers>1</show_triggers>
                            <type>0</type>
                            <show_legend>1</show_legend>
                            <show_3d>0</show_3d>
                            <percent_left>0.0000</percent_left>
                            <percent_right>0.0000</percent_right>
                            <ymin_type_1>0</ymin_type_1>
                            <ymax_type_1>0</ymax_type_1>
                            <ymin_item_1>0</ymin_item_1>
                            <ymax_item_1>0</ymax_item_1>
                            <graph_items>
                                <graph_item>
                                    <sortorder>0</sortorder>
                                    <drawtype>5</drawtype>
                                    <color>550055</color>
                                    <yaxisside>0</yaxisside>
                                    <calc_fnc>2</calc_fnc>
                                    <type>0</type>
                                    <item>
                                        <host>Template Mikrotik Radius Counters</host>
                                        <key>mikrotik.radius-out.node[{#MTIK_RADIUS_ID},requests]</key>
                                    </item>
                                </graph_item>
                            </graph_items>
                        </graph_prototype>
                        <graph_prototype>
                            <name>Radius Client {#MTIK_RADIUS_COMMENT}: Requests per type</name>
                            <width>1000</width>
                            <height>300</height>
                            <yaxismin>0.0000</yaxismin>
                            <yaxismax>100.0000</yaxismax>
                            <show_work_period>1</show_work_period>
                            <show_triggers>1</show_triggers>
                            <type>1</type>
                            <show_legend>1</show_legend>
                            <show_3d>0</show_3d>
                            <percent_left>0.0000</percent_left>
                            <percent_right>0.0000</percent_right>
                            <ymin_type_1>0</ymin_type_1>
                            <ymax_type_1>0</ymax_type_1>
                            <ymin_item_1>0</ymin_item_1>
                            <ymax_item_1>0</ymax_item_1>
                            <graph_items>
                                <graph_item>
                                    <sortorder>0</sortorder>
                                    <drawtype>0</drawtype>
                                    <color>1A7C11</color>
                                    <yaxisside>0</yaxisside>
                                    <calc_fnc>2</calc_fnc>
                                    <type>0</type>
                                    <item>
                                        <host>Template Mikrotik Radius Counters</host>
                                        <key>mikrotik.radius-out.node[{#MTIK_RADIUS_ID},accepts]</key>
                                    </item>
                                </graph_item>
                                <graph_item>
                                    <sortorder>1</sortorder>
                                    <drawtype>0</drawtype>
                                    <color>F63100</color>
                                    <yaxisside>0</yaxisside>
                                    <calc_fnc>2</calc_fnc>
                                    <type>0</type>
                                    <item>
                                        <host>Template Mikrotik Radius Counters</host>
                                        <key>mikrotik.radius-out.node[{#MTIK_RADIUS_ID},bad-replies]</key>
                                    </item>
                                </graph_item>
                                <graph_item>
                                    <sortorder>2</sortorder>
                                    <drawtype>0</drawtype>
                                    <color>2774A4</color>
                                    <yaxisside>0</yaxisside>
                                    <calc_fnc>2</calc_fnc>
                                    <type>0</type>
                                    <item>
                                        <host>Template Mikrotik Radius Counters</host>
                                        <key>mikrotik.radius-out.node[{#MTIK_RADIUS_ID},rejects]</key>
                                    </item>
                                </graph_item>
                                <graph_item>
                                    <sortorder>3</sortorder>
                                    <drawtype>0</drawtype>
                                    <color>A54F10</color>
                                    <yaxisside>0</yaxisside>
                                    <calc_fnc>2</calc_fnc>
                                    <type>0</type>
                                    <item>
                                        <host>Template Mikrotik Radius Counters</host>
                                        <key>mikrotik.radius-out.node[{#MTIK_RADIUS_ID},resends]</key>
                                    </item>
                                </graph_item>
                                <graph_item>
                                    <sortorder>4</sortorder>
                                    <drawtype>0</drawtype>
                                    <color>FC6EA3</color>
                                    <yaxisside>0</yaxisside>
                                    <calc_fnc>2</calc_fnc>
                                    <type>0</type>
                                    <item>
                                        <host>Template Mikrotik Radius Counters</host>
                                        <key>mikrotik.radius-out.node[{#MTIK_RADIUS_ID},timeouts]</key>
                                    </item>
                                </graph_item>
                            </graph_items>
                        </graph_prototype>
                    </graph_prototypes>
                    <host_prototypes/>
                </discovery_rule>
            </discovery_rules>
            <httptests/>
            <macros/>
            <templates/>
            <screens/>
        </template>
    </templates>
    <triggers>
        <trigger>
            <expression>{Template Mikrotik Radius Counters:mikrotik.radius-in.coa[requests].avg(1800)}&lt;0.5</expression>
            <recovery_mode>0</recovery_mode>
            <recovery_expression/>
            <name>Too few Radius CoA Requests from {HOSTNAME}</name>
            <correlation_mode>0</correlation_mode>
            <correlation_tag/>
            <url/>
            <status>0</status>
            <priority>3</priority>
            <description/>
            <type>0</type>
            <manual_close>0</manual_close>
            <dependencies/>
            <tags/>
        </trigger>
    </triggers>
    <graphs>
        <graph>
            <name>Radius CoA: Requests</name>
            <width>1000</width>
            <height>300</height>
            <yaxismin>0.0000</yaxismin>
            <yaxismax>100.0000</yaxismax>
            <show_work_period>1</show_work_period>
            <show_triggers>1</show_triggers>
            <type>0</type>
            <show_legend>1</show_legend>
            <show_3d>0</show_3d>
            <percent_left>0.0000</percent_left>
            <percent_right>0.0000</percent_right>
            <ymin_type_1>0</ymin_type_1>
            <ymax_type_1>0</ymax_type_1>
            <ymin_item_1>0</ymin_item_1>
            <ymax_item_1>0</ymax_item_1>
            <graph_items>
                <graph_item>
                    <sortorder>0</sortorder>
                    <drawtype>5</drawtype>
                    <color>660000</color>
                    <yaxisside>0</yaxisside>
                    <calc_fnc>2</calc_fnc>
                    <type>0</type>
                    <item>
                        <host>Template Mikrotik Radius Counters</host>
                        <key>mikrotik.radius-in.coa[requests]</key>
                    </item>
                </graph_item>
            </graph_items>
        </graph>
        <graph>
            <name>Radius CoA: Requests per type</name>
            <width>1000</width>
            <height>300</height>
            <yaxismin>0.0000</yaxismin>
            <yaxismax>100.0000</yaxismax>
            <show_work_period>1</show_work_period>
            <show_triggers>1</show_triggers>
            <type>1</type>
            <show_legend>1</show_legend>
            <show_3d>0</show_3d>
            <percent_left>0.0000</percent_left>
            <percent_right>0.0000</percent_right>
            <ymin_type_1>0</ymin_type_1>
            <ymax_type_1>0</ymax_type_1>
            <ymin_item_1>0</ymin_item_1>
            <ymax_item_1>0</ymax_item_1>
            <graph_items>
                <graph_item>
                    <sortorder>0</sortorder>
                    <drawtype>0</drawtype>
                    <color>1A7C11</color>
                    <yaxisside>0</yaxisside>
                    <calc_fnc>2</calc_fnc>
                    <type>0</type>
                    <item>
                        <host>Template Mikrotik Radius Counters</host>
                        <key>mikrotik.radius-in.coa[acks]</key>
                    </item>
                </graph_item>
                <graph_item>
                    <sortorder>1</sortorder>
                    <drawtype>0</drawtype>
                    <color>F63100</color>
                    <yaxisside>0</yaxisside>
                    <calc_fnc>2</calc_fnc>
                    <type>0</type>
                    <item>
                        <host>Template Mikrotik Radius Counters</host>
                        <key>mikrotik.radius-in.coa[bad-requests]</key>
                    </item>
                </graph_item>
                <graph_item>
                    <sortorder>2</sortorder>
                    <drawtype>0</drawtype>
                    <color>2774A4</color>
                    <yaxisside>0</yaxisside>
                    <calc_fnc>2</calc_fnc>
                    <type>0</type>
                    <item>
                        <host>Template Mikrotik Radius Counters</host>
                        <key>mikrotik.radius-in.coa[naks]</key>
                    </item>
                </graph_item>
            </graph_items>
        </graph>
    </graphs>
</zabbix_export>


File: /zabbix_templates\zbx_valuemaps_bgp_status.xml
<?xml version="1.0" encoding="UTF-8"?>
<zabbix_export>
    <version>3.2</version>
    <date>2018-07-02T20:22:44Z</date>
    <value_maps>
        <value_map>
            <name>ciscoBgpPeerState</name>
            <mappings>
                <mapping>
                    <value>0</value>
                    <newvalue>Weird</newvalue>
                </mapping>
                <mapping>
                    <value>1</value>
                    <newvalue>Idle</newvalue>
                </mapping>
                <mapping>
                    <value>2</value>
                    <newvalue>Connect</newvalue>
                </mapping>
                <mapping>
                    <value>3</value>
                    <newvalue>Active</newvalue>
                </mapping>
                <mapping>
                    <value>4</value>
                    <newvalue>OpenSent</newvalue>
                </mapping>
                <mapping>
                    <value>5</value>
                    <newvalue>OpenConfirm</newvalue>
                </mapping>
                <mapping>
                    <value>6</value>
                    <newvalue>Established</newvalue>
                </mapping>
            </mappings>
        </value_map>
    </value_maps>
</zabbix_export>


File: /zabbix_templates\zbx_valuemaps_mtik_bgp_admin_status.xml
<?xml version="1.0" encoding="UTF-8"?>
<zabbix_export>
    <version>3.2</version>
    <date>2018-07-02T20:07:35Z</date>
    <value_maps>
        <value_map>
            <name>Mikrotik BGP Administrative Status</name>
            <mappings>
                <mapping>
                    <value>0</value>
                    <newvalue>Up</newvalue>
                </mapping>
                <mapping>
                    <value>1</value>
                    <newvalue>Down</newvalue>
                </mapping>
            </mappings>
        </value_map>
    </value_maps>
</zabbix_export>


File: /zabbix_templates\zbx_valuemaps_mtik_firewall.xml
<?xml version="1.0" encoding="UTF-8"?>
<zabbix_export>
    <version>3.2</version>
    <date>2019-06-30T17:48:54Z</date>
    <value_maps>
        <value_map>
            <name>Mikrotik Firewall Rule Status</name>
            <mappings>
                <mapping>
                    <value>0</value>
                    <newvalue>enabled</newvalue>
                </mapping>
                <mapping>
                    <value>1</value>
                    <newvalue>disabled</newvalue>
                </mapping>
            </mappings>
        </value_map>
    </value_maps>
</zabbix_export>


