# Repository Information
Name: webpanel_ips_mikrotik_suricata

# Directory Structure
Directory structure:
└── github_repos/webpanel_ips_mikrotik_suricata/
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
    │   │       ├── pack-8ee8d2d3500c996ba9a9ec56159e65c79aa5be29.idx
    │   │       └── pack-8ee8d2d3500c996ba9a9ec56159e65c79aa5be29.pack
    │   ├── packed-refs
    │   └── refs/
    │       ├── heads/
    │       │   └── master
    │       ├── remotes/
    │       │   └── origin/
    │       │       └── HEAD
    │       └── tags/
    ├── a.css
    ├── functions.php
    ├── index.php
    ├── LICENSE
    ├── README
    ├── README.EN
    ├── schema.sql
    └── _config.yml


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
	url = https://github.com/elmaxid/webpanel_ips_mikrotik_suricata.git
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
0000000000000000000000000000000000000000 b1457fefbc46233cb40c7dc78833b236ea07d50e vivek-dodia <vivek.dodia@icloud.com> 1738606044 -0500	clone: from https://github.com/elmaxid/webpanel_ips_mikrotik_suricata.git


File: /.git\logs\refs\heads\master
0000000000000000000000000000000000000000 b1457fefbc46233cb40c7dc78833b236ea07d50e vivek-dodia <vivek.dodia@icloud.com> 1738606044 -0500	clone: from https://github.com/elmaxid/webpanel_ips_mikrotik_suricata.git


File: /.git\logs\refs\remotes\origin\HEAD
0000000000000000000000000000000000000000 b1457fefbc46233cb40c7dc78833b236ea07d50e vivek-dodia <vivek.dodia@icloud.com> 1738606044 -0500	clone: from https://github.com/elmaxid/webpanel_ips_mikrotik_suricata.git


File: /.git\packed-refs
# pack-refs with: peeled fully-peeled sorted 
b1457fefbc46233cb40c7dc78833b236ea07d50e refs/remotes/origin/master


File: /.git\refs\heads\master
b1457fefbc46233cb40c7dc78833b236ea07d50e


File: /.git\refs\remotes\origin\HEAD
ref: refs/remotes/origin/master


File: /a.css
.colorgraph {
  height: 5px;
  border-top: 0;
  background: #c4e17f;
  border-radius: 5px;
  background-image: -webkit-linear-gradient(left, #c4e17f, #c4e17f 12.5%, #f7fdca 12.5%, #f7fdca 25%, #fecf71 25%, #fecf71 37.5%, #f0776c 37.5%, #f0776c 50%, #db9dbe 50%, #db9dbe 62.5%, #c49cde 62.5%, #c49cde 75%, #669ae1 75%, #669ae1 87.5%, #62c2e4 87.5%, #62c2e4);
  background-image: -moz-linear-gradient(left, #c4e17f, #c4e17f 12.5%, #f7fdca 12.5%, #f7fdca 25%, #fecf71 25%, #fecf71 37.5%, #f0776c 37.5%, #f0776c 50%, #db9dbe 50%, #db9dbe 62.5%, #c49cde 62.5%, #c49cde 75%, #669ae1 75%, #669ae1 87.5%, #62c2e4 87.5%, #62c2e4);
  background-image: -o-linear-gradient(left, #c4e17f, #c4e17f 12.5%, #f7fdca 12.5%, #f7fdca 25%, #fecf71 25%, #fecf71 37.5%, #f0776c 37.5%, #f0776c 50%, #db9dbe 50%, #db9dbe 62.5%, #c49cde 62.5%, #c49cde 75%, #669ae1 75%, #669ae1 87.5%, #62c2e4 87.5%, #62c2e4);
  background-image: linear-gradient(to right, #c4e17f, #c4e17f 12.5%, #f7fdca 12.5%, #f7fdca 25%, #fecf71 25%, #fecf71 37.5%, #f0776c 37.5%, #f0776c 50%, #db9dbe 50%, #db9dbe 62.5%, #c49cde 62.5%, #c49cde 75%, #669ae1 75%, #669ae1 87.5%, #62c2e4 87.5%, #62c2e4);
}

body {
    background-color: #dedede;
}

.topbar {
	background: #2A3F54;
	border-color: #2A3F54;
	border-radius: 0px;
}

.topbar .navbar-header a {
	color: #ffffff;
}

.wrapper {
    padding-left: 0px;
    -webkit-transition: all 0.5s ease;
    -moz-transition: all 0.5s ease;
    -o-transition: all 0.5s ease;
    transition: all 0.5s ease;
}

.sidebar {
    z-index: 1000;
    position: fixed;
    top: 50px;
    left: -50px;
    width: 50px;
    height: 100%;
    overflow-y: auto;
    background: #2A3F54;
	color: #ffffff;
	-webkit-transition: all 0.5s ease;
    -moz-transition: all 0.5s ease;
    -o-transition: all 0.5s ease;
    transition: all 0.5s ease;
}

.main {
	width: 100%;
    position: relative;
    padding-bottom:20px;
}

.wrapper.toggled {
	padding-left: 50px;
}

.wrapper.toggled .sidebar {
	left: 0;
}

/* Sidebar Styles */

.sidebar-nav {
    position: absolute;
    top: 52px;
    width: 50px;
    margin: 0;
    padding: 0;
    list-style: none;
}
.sidebar-nav li {
    line-height: 40px;
}
.sidebar-nav li a {
    display: block;
    text-decoration: none;
    color: #e8e8e8;
    padding: 0;
    text-align:center;
}

.sidebar-nav li a:hover, .sidebar-nav li.active a {
    text-decoration: none;
    color: #fff;
    background: #fff;
    background: rgba(255,255,255,0.2);
}

.sidebar-nav li a:active,
.sidebar-nav li a:focus {
    text-decoration: none;
}

.sidebar-nav li span, .subbar li span {
	display : none;
}

nav.subbar {
	position: relative;
	width: 100%;
	border-radius: 0px;
	background: #fff;
	margin: 50px 0 -50px 0;
	padding: 10px 0 0 0;
	z-index: 2;
}
nav.subbar > ul.nav.nav-tabs {
	padding: 0 5px;
}

nav.subbar > ul.nav.nav-tabs > li.active > a {
    background: #dedede;
    border-top: 1px solid #a6a6a6;
    border-left: 1px solid #a6a6a6;
    border-right: 1px solid #a6a6a6;
    border-radius: 0px;
}

.content {
    margin-top: 70px;
    padding: 0 30px;
}

@media(min-width:768px){
	.subbar li span {
		display: inline;
	}
}

@media(min-width:992px) {
    .wrapper {
    	padding-left: 50px;
    }

    .sidebar {
    	left: 0;
    	width: 50px;
	}

	.wrapper.toggled {
		padding-left: 200px;
	}

	.wrapper.toggled .sidebar, .wrapper.toggled .sidebar-nav {
		width: 200px;
	}
	
	.wrapper.toggled .sidebar-nav li a {
		text-align: left;
		padding: 0 0 0 10px;
	}

	.wrapper.toggled .sidebar-nav li span {
		display: inline;
	}

}

.navbar-btn {
    background: none;
    border: none;
    height: 35px;
    min-width: 35px;
    color: #fff;
}
.navbar-text {
  margin-top: 14px;
  margin-bottom: 14px;
}
@media (min-width: 768px) {
  .navbar-text {
    float: left;
    margin-left: 15px;
    margin-right: 15px;
  }
}

File: /functions.php
<?php
/**
 * [array_search_partial busca un string en un valor de un array y devuelve el key]
 * @param  [type] $arr     [description]
 * @param  [type] $keyword [description]
 * @return [type]          [description]
 */
function array_search_partial( $arr, $keyword ) {
    foreach ( $arr as $index => $string ) {
        if ( strpos( $keyword, $string ) !== FALSE )
            return $index;
    } //$arr as $index => $string
}

/**
 * [partial_search_array Busca si existe parte de un string en un array]
 * @param  [type] $haystack [description]
 * @param  [type] $needle   [description]
 * @return [type]           [description]
 */
function partial_search_array( $haystack, $needle ) {
    foreach ( $haystack as $item ) {
        if ( strpos( $item, $needle ) !== false ) {
            return true;
        } //strpos( $item, $needle ) !== false
    } //$haystack as $item
    return false;
}



/**
 * [partial_search_array Busca si existe parte de un string en un array]
 * @param  [type] $haystack [description]
 * @param  [type] $needle   [description]
 * @return [type]           [description]
 */
function partial_search_array_special( $haystack, $needle ) {
    foreach ( $haystack as $item ) {
        if ( count( $needle ) > count( $item ) ) { //busco item en needle
            if ( strpos( $item, $needle ) !== false ) {
                return true;
            } //strpos( $item, $needle ) !== false
            
        } //count( $needle ) > count( $item )
        else { //busco needle en item
            
            if ( strpos( $needle, $item ) !== false ) {
                return true;
            } //strpos( $needle, $item ) !== false
        }
    } //$haystack as $item
    return false;
}



/**
 * [get_total_rules_active Get the total record of active rules]
 * @return [type] [description]
 */
function get_total_rules_active( ) {
    global $db_;
    $SQL = "SELECT count(*) as TOTAL FROM `block_queue`;";
    if ( !$result = $db_->query( $SQL ) ) {
        die( 'There was an error running the query [' . $db_->error . ']' );
    } //!$result = $db_->query( $SQL )
    $row = $result->fetch_assoc();
    return $row[ TOTAL ];
}
/**
 * [get_rules_db Get array with rules on DB]
 * @return [type] [description]
 */
function get_rules_db( ) {
    global $db_;
    $SQL = "SELECT * FROM sigs_to_block order by sig_name ;";
    if ( !$result = $db_->query( $SQL ) ) {
        die( 'There was an error running the query [' . $db_->error . ']' );
    } //!$result = $db_->query( $SQL )
    while ( $row = $result->fetch_assoc() ) {
        $array_tmp[ ] = $row;
    } //$row = $result->fetch_assoc()
    return $array_tmp;
}

/**
 * [get_rules_db Get the info of signature]
 * @return [type] [description]
 */
function get_signature_info_db( $sid = NULL ) {
    if ( !$sid )
        return false;
    global $db_;
    $SQL = "SELECT * FROM signature,event  WHERE `sig_sid` = '$sid' AND sig_id=signature ORDER BY timestamp desc LIMIT 1;";
    if ( !$result = $db_->query( $SQL ) ) {
        die( 'There was an error running the query [' . $db_->error . ']' );
    } //!$result = $db_->query( $SQL )
    $row = $result->fetch_assoc();
    return $row;
}

/**
 *
 * TODO: Mejorar consulta SQL
 * 
 * [get_rules_db Get the header info of conextion]
 * @return [type] [description]
 */
function get_header_info_db( $cid = NULL ) {
    if ( !$cid )
        return false;
    global $db_;
    $SQL = "SELECT *,inet_ntoa(ip_src) as ip_src,inet_ntoa(ip_dst) as ip_dst  FROM `iphdr` WHERE `cid` = '$cid' LIMIT 1;";
    if ( !$result = $db_->query( $SQL ) )
        die( 'There was an error running the query [' . $db_->error . ']' );
    //!$result = $db_->query( $SQL ) 
    $row[ 'packet' ] = $result->fetch_assoc();
    $SQL             = "SELECT * FROM `udphdr` WHERE `cid` = '$cid' LIMIT 1;";
    if ( !$result = $db_->query( $SQL ) )
        die( 'There was an error running the query [' . $db_->error . ']' );
    //!$result = $db_->query( $SQL )
    
    if ( $result->num_rows )
        $row[ 'port' ] = $result->fetch_assoc();
    else {
        $SQL = "SELECT * FROM `tcphdr` WHERE `cid` = '$cid' LIMIT 1;";
        if ( !$result = $db_->query( $SQL ) )
            die( 'There was an error running the query [' . $db_->error . ']' ); //!$result = $db_->query( $SQL )
        $row[ 'port' ] = $result->fetch_assoc();
    }
    
    return $row;
    
}

function obtiene_server_status( ) {
    // UPTIME
    if ( false === ( $str = @file( "/proc/uptime" ) ) )
        return false;
    $str   = explode( " ", implode( "", $str ) );
    $str   = trim( $str[ 0 ] );
    $min   = $str / 60;
    $hours = $min / 60;
    $days  = floor( $hours / 24 );
    $hours = floor( $hours - ( $days * 24 ) );
    $min   = floor( $min - ( $days * 60 * 24 ) - ( $hours * 60 ) );
    if ( $days !== 0 )
        $res[ 'uptime' ] = $days . " Days ";
    if ( $hours !== 0 )
        $res[ 'uptime' ] .= $hours . " Hours ";
    $res[ 'server_uptime' ] .= $min . " Minutes ";
    
    // MEMORY
    if ( false === ( $str = @file( "/proc/meminfo" ) ) )
        return false;
    $str = implode( "", $str );
    preg_match_all( "/MemTotal\s{0,}\:+\s{0,}([\d\.]+).+?MemFree\s{0,}\:+\s{0,}([\d\.]+).+?Cached\s{0,}\:+\s{0,}([\d\.]+).+?SwapTotal\s{0,}\:+\s{0,}([\d\.]+).+?SwapFree\s{0,}\:+\s{0,}([\d\.]+)/s", $str, $buf );
    
    $res[ 'memTotal' ]       = round( $buf[ 1 ][ 0 ], 2 );
    $res[ 'memFree' ]        = round( $buf[ 2 ][ 0 ], 2 );
    $res[ 'memCached' ]      = round( $buf[ 3 ][ 0 ], 2 );
    $res[ 'memUsed' ]        = ( $res[ 'memTotal' ] - $res[ 'memFree' ] );
    $res[ 'memPercent' ]     = ( floatval( $res[ 'memTotal' ] ) != 0 ) ? round( $res[ 'memUsed' ] / $res[ 'memTotal' ] * 100, 2 ) : 0;
    $res[ 'memRealUsed' ]    = ( $res[ 'memTotal' ] - $res[ 'memFree' ] - $res[ 'memCached' ] );
    $res[ 'memRealPercent' ] = ( floatval( $res[ 'memTotal' ] ) != 0 ) ? round( $res[ 'memRealUsed' ] / $res[ 'memTotal' ] * 100, 2 ) : 0;
    
    $res[ 'swapTotal' ]   = round( $buf[ 4 ][ 0 ], 2 );
    $res[ 'swapFree' ]    = round( $buf[ 5 ][ 0 ], 2 );
    $res[ 'swapUsed' ]    = ( $res[ 'swapTotal' ] - $res[ 'swapFree' ] );
    $res[ 'swapPercent' ] = ( floatval( $res[ 'swapTotal' ] ) != 0 ) ? round( $res[ 'swapUsed' ] / $res[ 'swapTotal' ] * 100, 2 ) : 0;
    
    // LOAD AVG
    if ( false === ( $str = @file( "/proc/loadavg" ) ) )
        return false;
    $str              = explode( " ", implode( "", $str ) );
    $str              = array_chunk( $str, 4 );
    $res[ 'loadAvg' ] = implode( " ", $str[ 0 ] );
    
    
    $res[ 'memTotal' ]  = filesize_format( $res[ 'memTotal' ] * 1024 );
    $res[ 'memUsed' ]   = filesize_format( $res[ 'memUsed' ] * 1024 );
    $res[ 'memCached' ] = filesize_format( $res[ 'memCached' ] * 1024 );
    
    $res[ 'swapTotal' ] = filesize_format( $res[ 'swapTotal' ] * 1024, '', 'GB' );
    $res[ 'swapFree' ]  = filesize_format( $res[ 'swapFree' ] * 1024 );
    $res[ 'swapUsed' ]  = filesize_format( $res[ 'swapUsed' ] * 1024 );
    
    
    return $res;
}

// * Format a number of bytes into a human readable format.
// * Optionally choose the output format and/or force a particular unit

function filesize_format( $size, $level = 0, $precision = 2, $base = 1024 ) {
    $unit  = array(
         'B',
        'kB',
        'MB',
        'GB',
        'TB',
        'PB',
        'EB',
        'ZB',
        'YB' 
    );
    $times = floor( log( $size, $base ) );
    return sprintf( "%." . $precision . "f", $size / pow( $base, ( $times + $level ) ) ) . " " . $unit[ $times + $level ];
}


//Facebook like
function format_fecha( $time ) {
    if ( $time !== intval( $time ) ) {
        $time = strtotime( $time );
    } //$time !== intval( $time )
    $d = time() - $time;
    if ( $time < strtotime( date( 'Y-m-d 00:00:00' ) ) - 60 * 60 * 24 * 3 ) {
        $format = 'F j';
        if ( date( 'Y' ) !== date( 'Y', $time ) ) {
            $format .= ", Y";
        } //date( 'Y' ) !== date( 'Y', $time )
        return date( $format, $time );
    } //$time < strtotime( date( 'Y-m-d 00:00:00' ) ) - 60 * 60 * 24 * 3
    if ( $d >= 60 * 60 * 24 ) {
        $day = 'Ayer';
        if ( date( 'l', time() - 60 * 60 * 24 ) !== date( 'l', $time ) ) {
            $day = date( 'l', $time );
        } //date( 'l', time() - 60 * 60 * 24 ) !== date( 'l', $time )
        return $day . " a las " . date( 'g:ia', $time );
    } //$d >= 60 * 60 * 24
    if ( $d >= 60 * 60 * 2 ) {
        return intval( $d / ( 60 * 60 ) ) . " hours ago";
    } //$d >= 60 * 60 * 2
    if ( $d >= 60 * 60 ) {
        return "1 hour ago";
    } //$d >= 60 * 60
    if ( $d >= 60 * 2 ) {
        return intval( $d / 60 ) . " minutes ago";
    } //$d >= 60 * 2
    if ( $d >= 60 ) {
        return "a minute ago";
    } //$d >= 60
    if ( $d >= 2 ) {
        return intval( $d ) . " seconds";
    } //$d >= 2
    return "a few seconds ago";
}
 
function get_server_uptime( ) {
    
    $exec_uptime = preg_split( "/[\s]+/", trim( shell_exec( 'uptime' ) ) );
    $uptime      = $exec_uptime[ 2 ] . ' Days';
    return $uptime;
    
}

 

function check_connect_router_API( ) {
    global $router;
    require( '/opt/ips-mikrotik-suricata/share/routeros_api.php' );
    $API = new RouterosAPI();
    if ( $API->connect( $router[ 'ip' ], $router[ 'user' ], $router[ 'pass' ] ) )
        return "<span class='label label-success '>OK</span>";
    else
        return ( 'Unable to connect to RouterOS. Error:' . $e );
    $API->disconnect();
    
}

function check_service_running( $service = "ids" ) {
    global $PID_app_file;
    if ( $service == "ids" )
        $cmd = "suricata -c /etc/suricata/suricata.yaml";
    elseif ( $service == "db" )
        $cmd = "barnyard2 -c /etc/suricata/barnyard2.conf";
    elseif ( $service == "snorby" )
        $cmd = "ruby script/rails server -e production -d -b 0.0.0.0";
    elseif ( $service == "ips" )
        if ( file_exists( $PID_app_file ) )
            return "<span class='label label-success'>OK</span>";
        else
            return "<span class='label label-danger'>NO</span>";
    $cmd_exec = "ps ax | grep -v grep | grep '$cmd' | wc -l";
    // echo $cmd_exec;
    $ret      = exec( $cmd_exec );
    // return $ret;
    if ( $ret )
        return "<span class='label label-success '>OK</span>";
    else
        return "<span class='label label-danger lead'>NO</span>";
}
?>

File: /index.php
<?php
/*****************************
 *
 * WebPanel for Manager Alerts Rules for IPS MikroTik Suricata  
 *
 * This file is the webgui for update and manager rules of project:
 *
 * https://github.com/elmaxid/ips-mikrotik-suricata *
 * 
 * Author: Maximiliano Dobladez info@mkesolutions.net
 *
 * http://maxid.com.ar | http://www.mkesolutions.net  
 *
 *
 * LICENSE: GPLv2 GNU GENERAL PUBLIC LICENSE
 *
 * 
 * v1.0 - 13 April 17 - initial version
 ******************************/
error_reporting( E_ALL );
error_reporting( 0 );
//include the config DB and API.
include 'functions.php';
include '/opt/ips-mikrotik-suricata/config.php';
$url_update_rules = 'https://www.update.rules.mkesolutions.net/update.php?c=update';
/* Wait for a connection to the database */
$i                = 0;
while ( $i < 100 ) {
    $db_ = new mysqli( $server, $user_name, $password, $database );
    if ( $db_->connect_errno > 0 ) {
        print( 'Unable to connect to database [' . $db_->connect_error . ']' );
        sleep( 10 );
        $i = $i + 10;
    } //$db_->connect_errno > 0
    else {
        $i          = 100;
        $connect_DB = true;
    }
} //$i < 100
if ( isset( $_REQUEST[ 'c' ] ) )
    $cmd = trim( $_REQUEST[ 'c' ] ); //command

if ( isset( $_REQUEST[ 's' ] ) )
    $search = trim( $_REQUEST[ 's' ] ); //search

if ( isset( $_REQUEST[ 'updates_rules' ] ) )
    $updates_rules = $_REQUEST[ 'updates_rules' ]; //updates_rules
if ( isset( $_REQUEST[ 'id' ] ) )
    $id = trim( $_REQUEST[ 'id' ] ); //id

if ( isset( $_REQUEST[ 'sid' ] ) )
    $sid = trim( $_REQUEST[ 'sid' ] ); //sid

if ( isset( $_REQUEST[ 'cid' ] ) )
    $cid = trim( $_REQUEST[ 'cid' ] ); //cid


if ( isset( $_REQUEST[ 'sig_name' ] ) )
    $sig_name = trim( $_REQUEST[ 'sig_name' ] ); //sig_name
if ( isset( $_REQUEST[ 'src_or_dst' ] ) )
    $src_or_dst = trim( $_REQUEST[ 'src_or_dst' ] ); //src_or_dst
if ( isset( $_REQUEST[ 'timeout' ] ) )
    $timeout = trim( $_REQUEST[ 'timeout' ] ); //timeout
$active = trim( $_REQUEST[ 'active' ] ); //active
if ( $cmd == "edit_rule_save" ) {
    ( $active == "on" ) ? $active_tmp = 1 : $active_tmp = 0;
    if ( $id == "new" )
        $sql_query = "INSERT INTO   sigs_to_block ( active, sig_name, src_or_dst,timeout )
                    VALUES ( '$active','$sig_name','$src_or_dst','$timeout' )";
    else
        $sql_query = "UPDATE sigs_to_block SET active='$active_tmp', sig_name='$sig_name', src_or_dst='$src_or_dst', timeout='$timeout' WHERE id=$id ;";
    if ( !$result = $db_->query( $sql_query ) ) {
        die( 'There was an error running the query [' . $db_->error . ']' );
    } //!$result = $db_->query( $sql_query )
    else {
        echo '<div class="alert alert-success"> <strong>OK Saved</strong> <i class="fa fa-refresh fa-spin"></i> Reloading... </div>';
    }
    exit;
} //$cmd == "edit_rule_save"
elseif ( $cmd == "save_rule_db" ) { // Save the update rules to DB
    //  echo "SAVE";
    // var_dump($updates_rules);
    foreach ( $updates_rules as $value ) {
        $row_tmp   = explode( '##', $value );
        // echo $value;
        $sql_query = "INSERT INTO   sigs_to_block ( sig_name, src_or_dst,timeout )
                         VALUES ( '$row_tmp[0]','$row_tmp[1]','$row_tmp[2]' )";
        echo $sql_query;
        if ( !$result = $db_->query( $sql_query ) ) {
            // die( 'There was an error running the query [' . $db_->error . ']' );
            echo $db_->error;
        } //!$result = $db_->query( $sql_query )
    } //$updates_rules as $value
    // echo show_rules_db(); 
    exit;
} //$cmd == "save_rule_db"
    elseif ( $cmd == "list_rule" ) {
    // echo "HOLA";
    echo show_active_rules_db();
    exit;
} //$cmd == "list_rule"
    elseif ( $cmd == "delete" ) {
    if ( !$id )
        return false;
    $SQL = "DELETE FROM sigs_to_block WHERE  id='$id'  ;";
    if ( !$result = $db_->query( $SQL ) ) {
        die( 'There was an error running the query [' . $db_->error . ']' );
    } //!$result = $db_->query( $SQL )
    mysqli_free_result( $result );
    echo show_active_rules_db(); //show again the list rules
    exit;
} //$cmd == "delete"
    elseif ( $cmd == "add" ) {
    echo show_form_edit_rule();
    exit;
} //$cmd == "add"
    elseif ( $cmd == "import_rule" ) { //import rule
    echo show_form_edit_rule( NULL, $sid );
    exit;
} //$cmd == "import_rule"
    elseif ( $cmd == "edit" ) {
    echo show_form_edit_rule( $id );
    exit;
} //$cmd == "edit"
    elseif ( $cmd == "update" ) {
    echo get_update_rules();
    exit;
} //$cmd == "update"
    elseif ( $cmd == "dashboard" ) {
    echo show_server_status();
    echo show_dashboard();
    exit;
} //$cmd == "dashboard"
    elseif ( $cmd == "check_connect_router_API" ) {
    echo check_connect_router_API();
    exit;
} //$cmd == "check_connect_router_API"
    elseif ( $cmd == "alerts_popular" ) {
    if ( $search == "ALL" )
        echo show_popular_alerts();
    if ( $search )
        echo show_popular_alerts( $search );
    else
        echo show_table_popular_alerts();
    
    exit;
} //$cmd == "alerts_popular"
    elseif ( $cmd == "view_event" ) {
    echo show_table_ip_header( NULL, $cid );
    
    exit;
} //$cmd == "view_event"
?>

<!DOCTYPE html>
<html lang="es">

<head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Rules Administrator For IPS MikroTik Suricata</title>

    <!-- Bootstrap CSS -->
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/css/bootstrap.min.css" integrity="sha384-1q8mTJOASx8j1Au+a5WDVnPi2lkFfwwEAa8hDDdjZlpLegxhjVME1fgjWPGmkzs7" crossorigin="anonymous">

  <link rel="stylesheet" href="//maxcdn.bootstrapcdn.com/font-awesome/4.4.0/css/font-awesome.min.css">    <link href="a.css" rel="stylesheet" media="screen">

    <!-- HTML5 Shim and Respond.js IE8 support of HTML5 elements and media queries -->
    <!-- WARNING: Respond.js doesn't work if you view the page via file:// -->
    <!--[if lt IE 9]>
            <script src="https://oss.maxcdn.com/libs/html5shiv/3.7.2/html5shiv.min.js"></script>
            <script src="https://oss.maxcdn.com/libs/respond.js/1.4.2/respond.min.js"></script>
        <![endif]-->
</head>

<body>
    <!-- jQuery -->
    <script src="//code.jquery.com/jquery.js"></script>
    <!-- Bootstrap JavaScript -->
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/js/bootstrap.min.js" integrity="sha384-0mSbJDEHialfmuBBQP6A4Qrprq5OVfW37PRR3j5ELqxss1yVqOtnepnHVP9aJ7xS" crossorigin="anonymous"></script>
    <!-- IE10 viewport hack for Surface/desktop Windows 8 bug -->

    <nav class="navbar navbar-default navbar-fixed-top topbar">
        <div class="container-fluid">

            <div class="navbar-header">

                <a href="#" class="navbar-brand">
                    <span class="visible-xs">RM</span>
                    <span class="hidden-xs">Rules Manager</span>
                </a>

                <p class="navbar-text">
                    <a href="#" class="sidebar-toggle">
                        <i class="fa fa-bars"></i>
                    </a>
                </p>

            </div>

        </div>
    </nav>

    <article class="wrapper">

        <aside class="sidebar">
            <ul class="sidebar-nav">
                <li><a onclick=" get_data('?c=dashboard','central');" href="#"><i class="fa fa-dashboard"></i> <span>Active Blocked Rules</span></a></li>
               <!-- <li><a href="#"  ><i class="fa fa-search"></i> <span>Events Viewer</span></a></li>  -->

                <li><a href="#" onclick="get_data('?c=alerts_popular','central');"><i class="fa fa-server"></i> <span>Popular Alerts</span></a></li>
                <li><a href="#" onclick=" get_data('?c=list_rule','central'); "><i class="fa fa-exchange"></i> <span>Rules Editor & Update</span></a></li>

            </ul>
        </aside>

        <section class="main">

            <section class="tab-content">

                <section class="tab-pane active fade in content">
                    <div id="central">
                    <?php
echo show_server_status();
echo show_dashboard();
?>
                    </div>
                </section>

            </section>

        </section>

    </article>

    <script type="text/javascript">
      function get_data(a,b){if(null==b)var c="central";else var c=b;$.get(a,function(a){""!=a&&$("#"+c).html(a)})}$(document).on("click",".sidebar-toggle",function(){$(".wrapper").toggleClass("toggled")});  $(function () {  $("[rel='tooltip']").tooltip({html:true});  });
    </script>



  


</body>

</html>


<?php

function show_tooltip( ) {
    return '  <script type="text/javascript"> $(function () {  $("[rel=\'tooltip\']").tooltip({html:true});  }); </script>';
}
function show_active_rules_db( ) {
    global $db_;
    $SQL = "SELECT * FROM sigs_to_block  ORDER by sig_name LIMIT 200;";
    if ( !$result = $db_->query( $SQL ) ) {
        die( 'There was an error running the query [' . $db_->error . ']' );
    } //!$result = $db_->query( $SQL )
    $count = $result->num_rows;
    
    $str .= ' <div class="row">
                       
                         
                       
                       <div class="col-xs-12 col-sm-9">
                           <div class="panel panel-default">
                               <div class="panel-heading">
                                  Active Alerts Rules (' . $count . ') <a  title="Add new rule" onclick="get_data(\'?c=add\',\'central\');" href="#" ><i class="fa fa-plus-circle"></i></a>
                               </div>
                               <div class="panel-body">
                                   <table class="table table-condensed table-hover">
                                    <thead>
                                        <tr>
                                            <th></th> <th>Rule</th> <th>IP Block</th><th>Timeout</th><th></th>
                                        </tr>
                                    </thead>
                                    <tbody>   ';
    while ( $row = $result->fetch_assoc() ) {
        ( $row[ 'active' ] ) ? $color_str = 'success' : $color_str = 'info';
        $str .= '<tr><td><span class="label label-' . $color_str . '"><i class="fa fa-check"></i></span></td><td onclick="get_data(\'?c=edit&id=' . $row[ 'id' ] . '\',\'central\');" >' . $row[ 'sig_name' ] . '</td><td>' . $row[ 'src_or_dst' ] . '</td><td>' . $row[ 'timeout' ] . '</td><td> <a onclick="get_data(\'?c=edit&id=' . $row[ 'id' ] . '\',\'central\');"  href=# >  <i class="fa fa-edit"></i> </a> <a onclick="get_data(\'?c=delete&id=' . $row[ 'id' ] . '\',\'central\');"  href=# > <i class="fa fa-trash"></i></a></td></tr>';
    } //$row = $result->fetch_assoc()
    $str .= '
                                    </tbody>
                                   </table>
                               </div>
                           </div>
                       </div>
                       
                       <div class="col-xs-12 col-sm-3">
                           <div class="panel panel-default">
                               <div class="panel-heading">
                                   Update Channel
                               </div>
                               <div class="panel-body">
                                   
                                   <a href=# onclick="get_data(\'?c=update\',\'central\');" ><i class="fa fa-refresh"></i> Update Rules</a>
                               </div>
                           </div>
                           
                           <div class="panel panel-default">
                               <div class="panel-heading">
                                MKE Solutions
                               </div>
                               <div class="panel-body">
                                   Designed by <a href="http://maxid.com.ar" target="_blank">Maximiliano Dobladez</a></a>
                               </div>
                           </div>
                       </div>
                       
                   </div>';
    return $str;
}
function show_form_edit_rule( $id = NULL, $sid = NULL ) { //SID para importar regla
    global $db_;
    if ( !$id ) {
        $new       = true;
        $str_input = '<input type=hidden name="id" value="new">';
    } //!$id
    else {
        $SQL = "SELECT * FROM sigs_to_block  WHERE id=$id LIMIT 1;";
        if ( !$result = $db_->query( $SQL ) ) {
            die( 'There was an error running the query [' . $db_->error . ']' );
        } //!$result = $db_->query( $SQL )
        $row            = $result->fetch_assoc();
        $str_input      = '<input type=hidden name="id" value="' . $id . '">';
        $str_sig_name   = 'value="' . $row[ sig_name ] . '"';
        $str_src_or_dst = '<option value="' . $row[ src_or_dst ] . '" >' . $row[ src_or_dst ] . '</option>';
        $str_timeout    = 'value="' . $row[ timeout ] . '"';
        ( $row[ 'active' ] == 1 ) ? $str_active = "checked" : $str_active = '';
    }
    
    if ( $sid ) {
        //get the info of signature
        $info_signature = get_signature_info_db( $sid );
        // // 
        //  echo var_dump($info_signature);
        //  echo var_dump($info_header);
        // $str.=show_table_ip_header($info_signature[cid]);
        $str_input      = '<input type=hidden name="id" value="new">';
        $str_active     = "checked"; //to active the option
        $str .= '<script>
        $(\'#name\').val(\'' . $info_signature[ sig_name ] . '\');
        $("#helpBlock").html(\' <span  class="help-block">Check the correct IP SOURCE o DESTINATION to block.</span>\');
        </script>';
        $str_sidebar = ' <div class="col-xs-12 col-sm-4">
                ' . show_table_ip_header( $sid ) . '
                    </div>';
    } //$sid
    $str .= '
                    <div class="col-xs-12 col-sm-8">
                        <div class="panel panel-default">
                            <div class="panel-heading">
                              
                                &nbsp;
                            </div>
                            <div class="panel-body">
                             <span id="show_result"></span>

                                <form class="form-horizontal" role="form" autocomplete=off  method="post" id="edit" >
                        ' . $str_input . '
                                    <fieldset>
                                        <legend>Add New Alert Rule</legend>
                                        <div class="form-group">
                                            <label class="col-sm-3 control-label" for="name">Name Alert</label>
                                            <div class="col-sm-9">
                                                <input type="text" class="form-control" required ' . $str_sig_name . ' name="sig_name" autofocus id="name" placeholder="Name Alert">
                                            </div>
                                        </div>

                                        <div class="form-group">
                                            <label class="col-sm-3 control-label" for="src_or_dst">Target IP to Block</label>

                                            <div class="col-sm-6">
                                                <select name="src_or_dst" id="src_or_dst" class="form-control">
                                                ' . $str_src_or_dst . '
                                                    <option value="src">src</option>
                                                    <option value="dst">dst</option>
                                                </select>
                                                 <span id="helpBlock"></span>

                                            </div>

                                        </div>

                                        <div class="form-group">

                                            <label class="col-sm-3 control-label" for="timeout">Timeout </label>
                                            <div class="col-sm-3">
                                                <input type="text" class="form-control" ' . $str_timeout . ' name="timeout" value="01:00:00">
                                            </div>

                                            <div class="col-sm-2 ">
                                                <label for="active">Active
                                                    <input type="checkbox" name="active" ' . $str_active . ' value=on id="active">
                                                </label>
                                            </div>

                                        </div>

                                        <div class="form-group">
                                            <div class="col-sm-offset-3 col-sm-9">
                                                  <a onclick="get_data(\'?c=list_rule\',\'central\');" class="btn btn-default btn-lg"><i class="fa fa-backward"></i> Back</a>
                                                <button type="submit" id=save_btn class="btn btn-success btn-lg"><i class="fa fa-save"></i> Save</button>

                                            </div>
                                        </div>
                                    </fieldset>
                                </form>
                            </div>
                        </div>
                    </div>
                   ' . $str_sidebar . '
                <script type="text/javascript">
                        $(document).ready(function() {
                            $(\'#save_btn\').click(function(e) {                                 
                                var dataS = $(\'form#edit\').serialize();
                                e.preventDefault();
                                $.ajax({
                                    type: "POST",
                                    url: \'index.php?c=edit_rule_save\',
                                    data: dataS,
                                    success: function(data) {
                                          $(\'#show_result\').html(data) ;
                                      
                                          setTimeout("get_data(\'?c=list_rule\',\'central\')", 1000);                                       
                                    }
                                })
                                return false;
                            });
                        });

                     

                    </script>
                  ';
    return $str;
}




/**
 * [get_update_rules Get the last update rule from cloud]
 * @return [type] [description]
 */
function get_update_rules( ) {
    global $url_update_rules;
    $update       = file_get_contents( $url_update_rules );
    $update_array = json_decode( $update, true );
    $db_rules     = get_rules_db();
    // echo var_dump($db_rules);
    // echo var_dump($update_array);
    $str .= '<div class="panel panel-info">
        <div class="panel-heading">
            <h3 class="panel-title">Rules Update</h3>
        </div>
        <div class="panel-body">
            <div class="col-md-10">
           <form class="form-horizontal"  role="form" autocomplete=off  method="post" id="update_rules" >
            ';
    foreach ( $update_array as $value ) {
        
        // if ( array_search( $value[ sig_name ], array_column( $db_rules, 'sig_name' ) ) ) {
        // if ( array_search_partial(array_column( $db_rules, 'sig_name' ),  $value[ sig_name ]  ) ) {
        if ( partial_search_array_special( array_column( $db_rules, 'sig_name' ), $value[ sig_name ] ) ) {
            $value_tmp = '';
        } //partial_search_array_special( array_column( $db_rules, 'sig_name' ), $value[ sig_name ] )
        else {
            $value_tmp = "$value[sig_name]##$value[src_or_dst]##$value[timeout]";
            $str .= " 

             <div class='form-group'>   <label for='$value[sig_name]' >
                    <input type=checkbox checked name='updates_rules[]' value='$value_tmp'> $value[sig_name]
                    </label>
                    </div>";
            //$str.="NUEVO ".$value[sig_name]."<br>";
        }
    } //$update_array as $value
    $str .= '  <div class="form-group">
                                            <div class="col-sm-offset-3 col-sm-9">
                                                  <a onclick="get_data(\'?c=list_rule\',\'central\');" class="btn btn-default btn-lg"><i class="fa fa-backward"></i> Back</a>
                                                <button type="submit" id=save_btn class="btn btn-success btn-lg"><i class="fa fa-save"></i> Save</button>

                                            </div>

                                            <script type="text/javascript">
                        $(document).ready(function() {
                            $(\'#save_btn\').click(function(e) {                                 
                                var dataS = $(\'form#update_rules\').serialize();
                                e.preventDefault();
                                $.ajax({
                                    type: "POST",
                                    url: \'index.php?c=save_rule_db\',
                                    data: dataS,
                                    success: function(data) {
                                          $(\'#show_result\').html(data) ;
                                      
                                          setTimeout("get_data(\'?c=list_rule\',\'central\')", 1000);                                       
                                    }
                                })
                                return false;
                            });
                        });

                        

                    </script>


                    ';
    $str .= '
            </form>
            <div>
        </div>
    </div>';
    return $str;
}
/**
 * [show_dashboard show welcome panel for stats]
 * @return [type] [description]
 */
function show_dashboard( ) {
    global $db_;
    $SQL = "SELECT *,inet_ntoa(que_ip_adr) as ip FROM block_queue group by que_ip_adr order by que_event_timestamp desc LIMIT 50;";
    if ( !$result = $db_->query( $SQL ) ) {
        die( 'There was an error running the query [' . $db_->error . ']' );
    } //!$result = $db_->query( $SQL )
    // $count = $result->num_rows;
    $count = get_total_rules_active();
    $str .= ' <div class="row">
                       
                         
                       
                       <div class="col-xs-12 col-sm-7">
                           <div class="panel panel-default">
                               <div class="panel-heading">
                                Active Alert Blocked (' . $count . ')  - Time: ' . date( "H:i:s", time() ) . '
                               </div>
                               <div class="panel-body" style=" max-height: 800px;
            overflow:auto;">
                                   <table class="table table-condensed table-hover" >
                                    <thead>
                                        <tr>
                                                <th> <i class="fa fa-clock-o"></i> Time</th><th>IP Block</th> <th>Rule</th><th class="hidden-xs">SID</th><th class="hidden-xs">Action</th> 
                                        </tr>
                                    </thead>
                                    <tbody>   ';
    while ( $row = $result->fetch_assoc() ) {
        $str .= '<tr><td> ' . format_fecha( $row[ 'que_event_timestamp' ] ) . '</td> <td>' . $row[ 'ip' ] . '</td><td >' . $row[ 'que_sig_name' ] . '</td><td class="hidden-xs"><a target=_blank rel=tooltip title="View Rule Alert" href=http://doc.emergingthreats.net/' . $row[ 'que_sig_sid' ] . '>' . $row[ 'que_sig_sid' ] . '</a></small></td><td class="hidden-xs">

        <a  id="view_event" target=_blank href=# data-cid="index.php?c=view_event&cid=' . $row[ 'que_event_cid' ] . '" title="View Event" rel="tooltip" ><i class="fa fa-eye"></i></a>

        </small></td> </tr>';
    } //$row = $result->fetch_assoc()
    $str .= '
                                    </tbody>
                                   </table>
                               </div>
                           </div>
                       </div>
                       
                       <div class="col-xs-12 col-sm-5">
                           <div class="panel panel-default">
                               <div class="panel-heading">

                                  Active Top Ten IP Attack
                               </div>

                                <div class="panel-body">
                                 ';
    $str .= show_table_top_ten( 1 );
    $str .= '
                               </div>
                              
                           </div>


                           
                           <div class="panel panel-default">
                               <div class="panel-heading">

                                  Active Top Ten Alert Rules
                               </div>

                                <div class="panel-body">
                                 ';
    $str .= show_table_top_ten( 2 );
    $str .= '
                               </div>
                              
                           </div>
                           
                           <div class="panel panel-default">
                               <div class="panel-heading">
                                  MKE Solutions
                               </div>
                               <div class="panel-body">
                                   Designed by <a href="http://maxid.com.ar" target="_blank">Maximiliano Dobladez</a></a>
                               </div>
                           </div>
                       </div>
                       
                   </div>


<div class="modal fade in slacker-modal" tabindex="-1" role="dialog" id="preview_event" aria-hidden="false">
            <div class="modal-dialog modal-slacker">
                <div class="modal-content">
                    <div class="modal-header">
                        <br><br> <button type="button" class="close" data-dismiss="modal" aria-hidden="true">×</button>
                        <h4 class="modal-title" >Event Viewer </h4>
                    </div>
                    <div class="modal-body"> 


                        <div id="show_event"> </div>


                    </div>
                </div><!-- /.modal-content -->
            </div><!-- /.modal-dialog -->
        </div>

                   ';
    
    $str .= "<script>$('a#view_event').click(function(e){
    var anchor = this;
    $('#preview_event').modal({show:true});   
     $('#show_event').load($(anchor).attr('data-cid'));  
    return false;
    });</script>";
    return $str . show_tooltip();
}
/**
 * [show_table_top_ten show tables with TOP TEN]
 * @param  string $type [description]
 * @return [type]       [description]
 */
function show_table_top_ten( $type = '1' ) {
    global $db_;
    if ( $type == "1" ) {
        $sql_query = "SELECT  inet_ntoa(que_ip_adr) as ip , count(*) as total FROM block_queue GROUP BY que_ip_adr
                    ORDER BY count(*) DESC LIMIT 10;";
        $str_th    = '  <th>Count</th> <th>IP Block</th>  <th>Country</th>';
    } //$type == "1"
    else {
        $sql_query = "SELECT  que_sig_name,que_sig_sid ,count(*) as total FROM block_queue GROUP BY que_sig_name 
                    ORDER BY count(*) DESC LIMIT 10;";
        $str_th    = '  <th>Count</th> <th>Alert</th>  <th>Sid</th>';
    }
    if ( !$result = $db_->query( $sql_query ) ) {
        die( 'There was an error running the query [' . $db_->error . ']' );
    } //!$result = $db_->query( $sql_query )
    $count = $result->num_rows;
    $str .= '   <table class="table table-condensed table-hover">
                                    <thead>
                                        <tr>
                                            ' . $str_th . '
                                        </tr>
                                    </thead>
                                    <tbody>   ';
    while ( $row = $result->fetch_assoc() ) {
        if ( $type == "1" ) {
            $str .= '<tr><td><small class="label label-default">' . $row[ 'total' ] . '</small></td>  <td ><small>' . $row[ 'ip' ] . '</small></td> <td ><small>' . geoip_country_name_by_name( $row[ 'ip' ] ) . '</small></td> </tr>';
        } //$type == "1"
        else {
            $str .= '<tr><td><small class="label label-default">' . $row[ 'total' ] . '</small></td>  <td ><small>' . $row[ 'que_sig_name' ] . '</small></td> <td ><small><a target=_blank rel=tooltip title="View Rule Alert" href=http://doc.emergingthreats.net/' . $row[ 'que_sig_sid' ] . '>' . $row[ 'que_sig_sid' ] . '</a></small></td> </tr>';
        }
    } //$row = $result->fetch_assoc()
    $str .= '
                                    </tbody>
                                   </table>';
    return $str . show_tooltip();
}

function show_server_status( ) {
    
    $data = obtiene_server_status();
    
    // echo var_dump($data);
    $str .= '  <div class="row">
                       
                        <div class="col-xs-12 col-sm-6">
                            <div class="panel panel-primary">
                                <div class="panel-body">
                                 <i class="fa fa-square"></i> Uptime  <strong class="lead">' . $data[ server_uptime ] . '</strong>  &nbsp;&nbsp;
                                  <i class="fa fa-square"></i>  Load Avr: <strong class="lead">' . $data[ loadAvg ] . '</strong> &nbsp;&nbsp;
                                  <i class="fa fa-square"></i>  MEM Free: <strong class="lead">' . $data[ memPercent ] . '%</strong>  
                                   
                                </div>
                            </div>
                        </div>
                        
                        <div class="col-xs-12 col-sm-6">
                            <div class="panel panel-primary">
                                <div class="panel-body">
                                  <strong> Suricata IDS: </strong><span class="lead">' . check_service_running( 'ids' ) . ' </span> &nbsp;&nbsp;
                                 <strong>  DB Daemon: </strong> <span class="lead">' . check_service_running( 'db' ) . ' </span>   &nbsp;&nbsp;
                                <strong>   IPS Daemon: </strong> <span class="lead">' . check_service_running( 'ips' ) . '  </span> &nbsp;&nbsp; 
                                <strong>   Snorby: </strong> <span class="lead">' . check_service_running( 'snorby' ) . ' </span>  &nbsp;&nbsp;
                                <strong>   API: </strong> <span class="lead" id="check_connect_router_API"> <i class="fa fa-refresh fa-spin"></i> </span>  

                                </div>
                            </div>
                        </div>
                     <script type="text/javascript">
                      $(document).ready(function(){return $.ajax({type:"POST",url:"index.php?c=check_connect_router_API",success:function(a){$("#check_connect_router_API").html(a)}}),!1});
                        </script>
                       
                     
                       
                   </div>';
    return $str;
}

/**
 * [show_popular_alerts Get popular alerts of today]
 * @return [type] [description]
 */
function show_popular_alerts( $s = NULL ) {
    global $db_;
    if ( isset( $s ) )
        $str_sql = "and s.sig_name like '%ET $s%' ";
    $SQL = "select sig_sid,sig_id, sig_name  as sig_name,count(*) as total from signature as s, event as e where s.sig_id=e.signature and date(e.timestamp)=date(now()) $str_sql group by sig_name order by total desc limit 300;";
    if ( !$result = $db_->query( $SQL ) ) {
        die( 'There was an error running the query [' . $db_->error . ']' );
    } //!$result = $db_->query( $SQL )
    $count = $result->num_rows;
    
    //get the actual alert to block
    $alert_to_block = get_rules_db();
    $str .= ' <div class="panel-body"> 
                                   <table class="table table-condensed table-hover">
                                    <thead>
                                        <tr>
                                            <th>SID / ID</th> <th>Rule</th> <th>Total Alerts</th><th></th>
                                        </tr>
                                    </thead>
                                    <tbody>   ';
    while ( $row = $result->fetch_assoc() ) {
        
        if ( partial_search_array_special( array_column( $alert_to_block, 'sig_name' ), $row[ sig_name ] ) ) {
            $str_tr_color   = "class='' ";
            $str_action_tmp = "";
        } //partial_search_array_special( array_column( $alert_to_block, 'sig_name' ), $row[ sig_name ] )
        else {
            $str_tr_color   = "class='warning' title='No Match with actual rules' rel=tooltip ";
            $str_action_tmp = ' <a onclick="get_data(\'?c=import_rule&sid=' . $row[ 'sig_sid' ] . '\',\'central\');"  href=# >  <i class="fa fa-plus"></i> </a>  ';
            
        }
        $str .= '<tr ' . $str_tr_color . '> <td><a target=_blank href=http://doc.emergingthreats.net/' . $row[ 'sig_sid' ] . '>' . $row[ 'sig_sid' ] . '</a> / ' . $row[ 'sig_id' ] . ' ' . '</td> <td>' . $row[ 'sig_name' ] . '</td> <td>' . $row[ 'total' ] . '</td><td>' . $str_action_tmp . '</td></tr>';
    } //$row = $result->fetch_assoc()
    $str .= '
                                    </tbody>
                                   </table>
                               </div>';
    
    
    return $str;
}

function show_table_popular_alerts( $s = NULL ) {
    
    $str .= ' <div class="row">
                       
                         
                       
                       <div class="col-xs-12 col-sm-9">
                           <div class="panel panel-default">
                               <div class="panel-heading">
                                  Today Total Alerts - Most Active 
                                  <select onchange="get_data(\'?c=alerts_popular&s=\'+this.value,\'table_alerts\')">
                                  <option value="ALL">ALL</option>
                                  <option value="DOS">DOS</option>
                                  <option value="VOIP">VOIP</option>
                                  <option value="SCAN">SCAN</option>
                                  <option value="TROJAN">TROJAN</option>
                                  <option value="MALWARE">MALWARE</option>
                                  <option value="DROP">DROP</option>
                                  <option value="CINS">CINS</option>
                                  <option value="COMPROMISED">COMPROMISED</option>
                                  <option value="POLICY">POLICY</option>
                                  <option value="COMPROMISED">COMPROMISED</option>
                                  </select>
                               </div>
                               <span id="table_alerts"> ' . show_popular_alerts( $s ) . '</span>
                           </div>
                       </div>
                       
                       <div class="col-xs-12 col-sm-3">
                         
                       </div>
                       
                   </div>';
    return $str;
    
}

function show_table_ip_header( $sid = NULL, $cid = NULL ) {
    if ( !$sid ) {
        $cid_tmp = $cid;
    } //!$sid
    else {
        $info_signature = get_signature_info_db( $sid );
        $cid_tmp        = $info_signature[ 'cid' ];
        $str_th_name    = ' <tr><th colspan="5">Name: <span class="text-center lead"> ' . $info_signature[ 'sig_name' ] . '</span></th></tr>';
    }
    $row = get_header_info_db( $cid_tmp );
    // echo var_dump($info_signature);
    // echo var_dump($row);
    
    if ( $row[ 'port' ][ 'udp_sport' ] ) {
        $protocol = "UDP";
        $port_src = $row[ 'port' ][ 'udp_sport' ];
        $port_dst = $row[ 'port' ][ 'udp_dport' ];
    } //$row[ 'port' ][ 'udp_sport' ]
    else {
        $protocol = "TCP";
        $port_src = $row[ 'port' ][ 'tcp_sport' ];
        $port_dst = $row[ 'port' ][ 'tcp_dport' ];
    }
    
    
    $str .= '<div class="well table-responsive">
        <table class="table table-hover table-condensed">
            <thead>
               ' . $str_th_name . '
                <tr>
                 <th>Protocol</th>   <th>IP Source</th>  <th>Port Src</th>  <th>IP Destination</th>  <th>Port Dst</th>
                </tr>
            </thead>
            <tbody>

                <tr>
                    <td>' . $protocol . '</td> <td>' . $row[ 'packet' ][ 'ip_src' ] . '</td> <td>' . $port_src . '</td> <td>' . $row[ 'packet' ][ 'ip_dst' ] . '</td> <td>' . $port_dst . '</td>
                </tr>
            </tbody>
        </table>
    </div>';
    return $str;
}
?>

File: /LICENSE
                    GNU GENERAL PUBLIC LICENSE
                       Version 2, June 1991

 Copyright (C) 1989, 1991 Free Software Foundation, Inc., <http://fsf.org/>
 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA
 Everyone is permitted to copy and distribute verbatim copies
 of this license document, but changing it is not allowed.

                            Preamble

  The licenses for most software are designed to take away your
freedom to share and change it.  By contrast, the GNU General Public
License is intended to guarantee your freedom to share and change free
software--to make sure the software is free for all its users.  This
General Public License applies to most of the Free Software
Foundation's software and to any other program whose authors commit to
using it.  (Some other Free Software Foundation software is covered by
the GNU Lesser General Public License instead.)  You can apply it to
your programs, too.

  When we speak of free software, we are referring to freedom, not
price.  Our General Public Licenses are designed to make sure that you
have the freedom to distribute copies of free software (and charge for
this service if you wish), that you receive source code or can get it
if you want it, that you can change the software or use pieces of it
in new free programs; and that you know you can do these things.

  To protect your rights, we need to make restrictions that forbid
anyone to deny you these rights or to ask you to surrender the rights.
These restrictions translate to certain responsibilities for you if you
distribute copies of the software, or if you modify it.

  For example, if you distribute copies of such a program, whether
gratis or for a fee, you must give the recipients all the rights that
you have.  You must make sure that they, too, receive or can get the
source code.  And you must show them these terms so they know their
rights.

  We protect your rights with two steps: (1) copyright the software, and
(2) offer you this license which gives you legal permission to copy,
distribute and/or modify the software.

  Also, for each author's protection and ours, we want to make certain
that everyone understands that there is no warranty for this free
software.  If the software is modified by someone else and passed on, we
want its recipients to know that what they have is not the original, so
that any problems introduced by others will not reflect on the original
authors' reputations.

  Finally, any free program is threatened constantly by software
patents.  We wish to avoid the danger that redistributors of a free
program will individually obtain patent licenses, in effect making the
program proprietary.  To prevent this, we have made it clear that any
patent must be licensed for everyone's free use or not licensed at all.

  The precise terms and conditions for copying, distribution and
modification follow.

                    GNU GENERAL PUBLIC LICENSE
   TERMS AND CONDITIONS FOR COPYING, DISTRIBUTION AND MODIFICATION

  0. This License applies to any program or other work which contains
a notice placed by the copyright holder saying it may be distributed
under the terms of this General Public License.  The "Program", below,
refers to any such program or work, and a "work based on the Program"
means either the Program or any derivative work under copyright law:
that is to say, a work containing the Program or a portion of it,
either verbatim or with modifications and/or translated into another
language.  (Hereinafter, translation is included without limitation in
the term "modification".)  Each licensee is addressed as "you".

Activities other than copying, distribution and modification are not
covered by this License; they are outside its scope.  The act of
running the Program is not restricted, and the output from the Program
is covered only if its contents constitute a work based on the
Program (independent of having been made by running the Program).
Whether that is true depends on what the Program does.

  1. You may copy and distribute verbatim copies of the Program's
source code as you receive it, in any medium, provided that you
conspicuously and appropriately publish on each copy an appropriate
copyright notice and disclaimer of warranty; keep intact all the
notices that refer to this License and to the absence of any warranty;
and give any other recipients of the Program a copy of this License
along with the Program.

You may charge a fee for the physical act of transferring a copy, and
you may at your option offer warranty protection in exchange for a fee.

  2. You may modify your copy or copies of the Program or any portion
of it, thus forming a work based on the Program, and copy and
distribute such modifications or work under the terms of Section 1
above, provided that you also meet all of these conditions:

    a) You must cause the modified files to carry prominent notices
    stating that you changed the files and the date of any change.

    b) You must cause any work that you distribute or publish, that in
    whole or in part contains or is derived from the Program or any
    part thereof, to be licensed as a whole at no charge to all third
    parties under the terms of this License.

    c) If the modified program normally reads commands interactively
    when run, you must cause it, when started running for such
    interactive use in the most ordinary way, to print or display an
    announcement including an appropriate copyright notice and a
    notice that there is no warranty (or else, saying that you provide
    a warranty) and that users may redistribute the program under
    these conditions, and telling the user how to view a copy of this
    License.  (Exception: if the Program itself is interactive but
    does not normally print such an announcement, your work based on
    the Program is not required to print an announcement.)

These requirements apply to the modified work as a whole.  If
identifiable sections of that work are not derived from the Program,
and can be reasonably considered independent and separate works in
themselves, then this License, and its terms, do not apply to those
sections when you distribute them as separate works.  But when you
distribute the same sections as part of a whole which is a work based
on the Program, the distribution of the whole must be on the terms of
this License, whose permissions for other licensees extend to the
entire whole, and thus to each and every part regardless of who wrote it.

Thus, it is not the intent of this section to claim rights or contest
your rights to work written entirely by you; rather, the intent is to
exercise the right to control the distribution of derivative or
collective works based on the Program.

In addition, mere aggregation of another work not based on the Program
with the Program (or with a work based on the Program) on a volume of
a storage or distribution medium does not bring the other work under
the scope of this License.

  3. You may copy and distribute the Program (or a work based on it,
under Section 2) in object code or executable form under the terms of
Sections 1 and 2 above provided that you also do one of the following:

    a) Accompany it with the complete corresponding machine-readable
    source code, which must be distributed under the terms of Sections
    1 and 2 above on a medium customarily used for software interchange; or,

    b) Accompany it with a written offer, valid for at least three
    years, to give any third party, for a charge no more than your
    cost of physically performing source distribution, a complete
    machine-readable copy of the corresponding source code, to be
    distributed under the terms of Sections 1 and 2 above on a medium
    customarily used for software interchange; or,

    c) Accompany it with the information you received as to the offer
    to distribute corresponding source code.  (This alternative is
    allowed only for noncommercial distribution and only if you
    received the program in object code or executable form with such
    an offer, in accord with Subsection b above.)

The source code for a work means the preferred form of the work for
making modifications to it.  For an executable work, complete source
code means all the source code for all modules it contains, plus any
associated interface definition files, plus the scripts used to
control compilation and installation of the executable.  However, as a
special exception, the source code distributed need not include
anything that is normally distributed (in either source or binary
form) with the major components (compiler, kernel, and so on) of the
operating system on which the executable runs, unless that component
itself accompanies the executable.

If distribution of executable or object code is made by offering
access to copy from a designated place, then offering equivalent
access to copy the source code from the same place counts as
distribution of the source code, even though third parties are not
compelled to copy the source along with the object code.

  4. You may not copy, modify, sublicense, or distribute the Program
except as expressly provided under this License.  Any attempt
otherwise to copy, modify, sublicense or distribute the Program is
void, and will automatically terminate your rights under this License.
However, parties who have received copies, or rights, from you under
this License will not have their licenses terminated so long as such
parties remain in full compliance.

  5. You are not required to accept this License, since you have not
signed it.  However, nothing else grants you permission to modify or
distribute the Program or its derivative works.  These actions are
prohibited by law if you do not accept this License.  Therefore, by
modifying or distributing the Program (or any work based on the
Program), you indicate your acceptance of this License to do so, and
all its terms and conditions for copying, distributing or modifying
the Program or works based on it.

  6. Each time you redistribute the Program (or any work based on the
Program), the recipient automatically receives a license from the
original licensor to copy, distribute or modify the Program subject to
these terms and conditions.  You may not impose any further
restrictions on the recipients' exercise of the rights granted herein.
You are not responsible for enforcing compliance by third parties to
this License.

  7. If, as a consequence of a court judgment or allegation of patent
infringement or for any other reason (not limited to patent issues),
conditions are imposed on you (whether by court order, agreement or
otherwise) that contradict the conditions of this License, they do not
excuse you from the conditions of this License.  If you cannot
distribute so as to satisfy simultaneously your obligations under this
License and any other pertinent obligations, then as a consequence you
may not distribute the Program at all.  For example, if a patent
license would not permit royalty-free redistribution of the Program by
all those who receive copies directly or indirectly through you, then
the only way you could satisfy both it and this License would be to
refrain entirely from distribution of the Program.

If any portion of this section is held invalid or unenforceable under
any particular circumstance, the balance of the section is intended to
apply and the section as a whole is intended to apply in other
circumstances.

It is not the purpose of this section to induce you to infringe any
patents or other property right claims or to contest validity of any
such claims; this section has the sole purpose of protecting the
integrity of the free software distribution system, which is
implemented by public license practices.  Many people have made
generous contributions to the wide range of software distributed
through that system in reliance on consistent application of that
system; it is up to the author/donor to decide if he or she is willing
to distribute software through any other system and a licensee cannot
impose that choice.

This section is intended to make thoroughly clear what is believed to
be a consequence of the rest of this License.

  8. If the distribution and/or use of the Program is restricted in
certain countries either by patents or by copyrighted interfaces, the
original copyright holder who places the Program under this License
may add an explicit geographical distribution limitation excluding
those countries, so that distribution is permitted only in or among
countries not thus excluded.  In such case, this License incorporates
the limitation as if written in the body of this License.

  9. The Free Software Foundation may publish revised and/or new versions
of the General Public License from time to time.  Such new versions will
be similar in spirit to the present version, but may differ in detail to
address new problems or concerns.

Each version is given a distinguishing version number.  If the Program
specifies a version number of this License which applies to it and "any
later version", you have the option of following the terms and conditions
either of that version or of any later version published by the Free
Software Foundation.  If the Program does not specify a version number of
this License, you may choose any version ever published by the Free Software
Foundation.

  10. If you wish to incorporate parts of the Program into other free
programs whose distribution conditions are different, write to the author
to ask for permission.  For software which is copyrighted by the Free
Software Foundation, write to the Free Software Foundation; we sometimes
make exceptions for this.  Our decision will be guided by the two goals
of preserving the free status of all derivatives of our free software and
of promoting the sharing and reuse of software generally.

                            NO WARRANTY

  11. BECAUSE THE PROGRAM IS LICENSED FREE OF CHARGE, THERE IS NO WARRANTY
FOR THE PROGRAM, TO THE EXTENT PERMITTED BY APPLICABLE LAW.  EXCEPT WHEN
OTHERWISE STATED IN WRITING THE COPYRIGHT HOLDERS AND/OR OTHER PARTIES
PROVIDE THE PROGRAM "AS IS" WITHOUT WARRANTY OF ANY KIND, EITHER EXPRESSED
OR IMPLIED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF
MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE.  THE ENTIRE RISK AS
TO THE QUALITY AND PERFORMANCE OF THE PROGRAM IS WITH YOU.  SHOULD THE
PROGRAM PROVE DEFECTIVE, YOU ASSUME THE COST OF ALL NECESSARY SERVICING,
REPAIR OR CORRECTION.

  12. IN NO EVENT UNLESS REQUIRED BY APPLICABLE LAW OR AGREED TO IN WRITING
WILL ANY COPYRIGHT HOLDER, OR ANY OTHER PARTY WHO MAY MODIFY AND/OR
REDISTRIBUTE THE PROGRAM AS PERMITTED ABOVE, BE LIABLE TO YOU FOR DAMAGES,
INCLUDING ANY GENERAL, SPECIAL, INCIDENTAL OR CONSEQUENTIAL DAMAGES ARISING
OUT OF THE USE OR INABILITY TO USE THE PROGRAM (INCLUDING BUT NOT LIMITED
TO LOSS OF DATA OR DATA BEING RENDERED INACCURATE OR LOSSES SUSTAINED BY
YOU OR THIRD PARTIES OR A FAILURE OF THE PROGRAM TO OPERATE WITH ANY OTHER
PROGRAMS), EVEN IF SUCH HOLDER OR OTHER PARTY HAS BEEN ADVISED OF THE
POSSIBILITY OF SUCH DAMAGES.

                     END OF TERMS AND CONDITIONS

            How to Apply These Terms to Your New Programs

  If you develop a new program, and you want it to be of the greatest
possible use to the public, the best way to achieve this is to make it
free software which everyone can redistribute and change under these terms.

  To do so, attach the following notices to the program.  It is safest
to attach them to the start of each source file to most effectively
convey the exclusion of warranty; and each file should have at least
the "copyright" line and a pointer to where the full notice is found.

    {description}
    Copyright (C) {year}  {fullname}

    This program is free software; you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation; either version 2 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License along
    with this program; if not, write to the Free Software Foundation, Inc.,
    51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.

Also add information on how to contact you by electronic and paper mail.

If the program is interactive, make it output a short notice like this
when it starts in an interactive mode:

    Gnomovision version 69, Copyright (C) year name of author
    Gnomovision comes with ABSOLUTELY NO WARRANTY; for details type `show w'.
    This is free software, and you are welcome to redistribute it
    under certain conditions; type `show c' for details.

The hypothetical commands `show w' and `show c' should show the appropriate
parts of the General Public License.  Of course, the commands you use may
be called something other than `show w' and `show c'; they could even be
mouse-clicks or menu items--whatever suits your program.

You should also get your employer (if you work as a programmer) or your
school, if any, to sign a "copyright disclaimer" for the program, if
necessary.  Here is a sample; alter the names:

  Yoyodyne, Inc., hereby disclaims all copyright interest in the program
  `Gnomovision' (which makes passes at compilers) written by James Hacker.

  {signature of Ty Coon}, 1 April 1989
  Ty Coon, President of Vice

This General Public License does not permit incorporating your program into
proprietary programs.  If your program is a subroutine library, you may
consider it more useful to permit linking proprietary applications with the
library.  If this is what you want to do, use the GNU Lesser General
Public License instead of this License.


File: /README
README.EN

File: /README.EN
WebPanel for Manager Alerts Rules for IPS MikroTik Suricata:

This is the WebPanel for Manager Alerts Rules of IPS MikroTik Suricata project

https://github.com/elmaxid/ips-mikrotik-suricata

Changelog:

13 April 17: v1.0

* Initial Version

Requeriment:

* ips-mikrotik-suricata Working
* PHP5 with support Mysql and GeoLib
* GIT

** Features

* Panel to monitor the active alerts blocked and update the rules for new patterns.


Instalation

Check you have the requeriments:

apt-get install php5-geoip php5-mysql

Once we have IPS-MikroTik-Suricata working and running on our network, the next step is the instalation of panel :

--
To install, Clone the repository and copy to /www/html/snorby/public/rules or another you choice

cd /www/html/snorby/public/

git clone https://github.com/elmaxid/webpanel_ips_mikrotik_suricata.git

mv webpanel_ips_mikrotik_suricata rules

-- to Config

* Modify for the new DB schema 

mysql -u username -p snorby < schema.sql


* Use it:

Enter to http://IP_HOST/rules

----
 

File: /schema.sql




USE snorby;

ALTER TABLE `block_queue`
ADD `que_event_cid` int(10) NULL AFTER `que_sig_sid`;


ALTER TABLE `sigs_to_block`
ADD `id` int NOT NULL AUTO_INCREMENT PRIMARY KEY FIRST,
ADD `active` int(1) NOT NULL DEFAULT '1' AFTER `id`;


DROP TRIGGER `after_iphdr_insert`;
DELIMITER ;;
CREATE TRIGGER `after_iphdr_insert` AFTER INSERT ON `iphdr` FOR EACH ROW
BEGIN
                        DECLARE this_event INT(11) default 0;
                        DECLARE this_event_signature INT(10) default 0;
                        DECLARE this_event_timestamp TIMESTAMP;
                        DECLARE this_sig INT(10) default 0;
                        DECLARE this_sig_name VARCHAR(256) default "";
                        DECLARE this_sig_gid INT(10) default 0;

  						DECLARE this_que_event_cid INT(10) default 0;

                        DECLARE timeout VARCHAR(12) default "";
                        DECLARE interested INT default 0;
                        DECLARE direction VARCHAR(3) default "";
                        DECLARE ip_src VARCHAR(64) default "";
                        DECLARE ip_dst VARCHAR(64) default "";
                        SELECT event.id, event.signature, event.timestamp, event.cid
                        INTO this_event, this_event_signature, this_event_timestamp, this_que_event_cid
                        FROM event
                        WHERE event.sid = NEW.sid and event.cid = NEW.cid;  
                        SELECT signature.sig_sid, signature.sig_gid, signature.sig_name 
                        INTO this_sig, this_sig_gid, this_sig_name
                        FROM signature
                        WHERE signature.sig_id = this_event_signature;
                        SELECT count(*), sigs_to_block.src_or_dst, sigs_to_block.timeout
                        INTO interested, direction, timeout
                        FROM sigs_to_block
                        WHERE this_sig_name LIKE CONCAT(sigs_to_block.sig_name, '%');
                        IF (interested > 0) THEN
                         IF (direction = "src") THEN
                            INSERT INTO block_queue
                         SET que_ip_adr =NEW.ip_src,
                                que_timeout = timeout,
                                que_sig_name = this_sig_name,
                                que_sig_gid = this_sig_gid,
                                que_sig_sid = this_sig,
que_event_cid=this_que_event_cid,
                                que_event_timestamp = this_event_timestamp;
                          ELSE
                            INSERT INTO block_queue
                         SET que_ip_adr =NEW.ip_dst,
                                que_timeout = timeout,
                                que_sig_name = this_sig_name,
                                que_sig_gid = this_sig_gid,
                                que_sig_sid = this_sig,
que_event_cid=this_que_event_cid,
                                que_event_timestamp = this_event_timestamp;
                          END IF;
                        END IF;
                      END;;
DELIMITER ;

File: /_config.yml
theme: jekyll-theme-slate

