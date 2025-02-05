# Repository Information
Name: indoads-mikrotik

# Directory Structure
Directory structure:
└── github_repos/indoads-mikrotik/
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
    │   │       ├── pack-7875edac1bf82ef6b0fcf394ddc3e8d1d5549859.idx
    │   │       └── pack-7875edac1bf82ef6b0fcf394ddc3e8d1d5549859.pack
    │   ├── packed-refs
    │   └── refs/
    │       ├── heads/
    │       │   └── master
    │       ├── remotes/
    │       │   └── origin/
    │       │       └── HEAD
    │       └── tags/
    ├── adlists.rsc
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
	url = https://github.com/laksa19/indoads-mikrotik.git
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
0000000000000000000000000000000000000000 1b25b969d4d31482b18db91bb7e9171148576377 vivek-dodia <vivek.dodia@icloud.com> 1738606470 -0500	clone: from https://github.com/laksa19/indoads-mikrotik.git


File: /.git\logs\refs\heads\master
0000000000000000000000000000000000000000 1b25b969d4d31482b18db91bb7e9171148576377 vivek-dodia <vivek.dodia@icloud.com> 1738606470 -0500	clone: from https://github.com/laksa19/indoads-mikrotik.git


File: /.git\logs\refs\remotes\origin\HEAD
0000000000000000000000000000000000000000 1b25b969d4d31482b18db91bb7e9171148576377 vivek-dodia <vivek.dodia@icloud.com> 1738606470 -0500	clone: from https://github.com/laksa19/indoads-mikrotik.git


File: /.git\packed-refs
# pack-refs with: peeled fully-peeled sorted 
1b25b969d4d31482b18db91bb7e9171148576377 refs/remotes/origin/master


File: /.git\refs\heads\master
1b25b969d4d31482b18db91bb7e9171148576377


File: /.git\refs\remotes\origin\HEAD
ref: refs/remotes/origin/master


File: /adlists.rsc
/ip dns static
add address=127.0.0.1 name=3g.qq.com
add address=127.0.0.1 name=a01.uadexchange.com
add address=127.0.0.1 name=abrts.pro
add address=127.0.0.1 name=aclickads.com
add address=127.0.0.1 name=ada.avocarrot.com
add address=127.0.0.1 name=ad.adflazz.com
add address=127.0.0.1 name=ad.admitad.com
add address=127.0.0.1 name=ad.amgdgt.com
add address=127.0.0.1 name=addesigner.com
add address=127.0.0.1 name=ad.doubleclick.net
add address=127.0.0.1 name=adexchangecloud.com
add address=127.0.0.1 name=adexp.net
add address=127.0.0.1 name=ad-g.doubleclick.net
add address=127.0.0.1 name=admarketplace.net
add address=127.0.0.1 name=admin.appnext.com
add address=127.0.0.1 name=ad.mo.doubleclick.net
add address=127.0.0.1 name=adnety.com
add address=127.0.0.1 name=adplus.co.id
add address=127.0.0.1 name=adpop-1.com
add address=127.0.0.1 name=adpstatic.com
add address=127.0.0.1 name=adreviewcamp.com
add address=127.0.0.1 name=ads8.kompasads.com
add address=127.0.0.1 name=ads.admarvel.com
add address=127.0.0.1 name=ads.avad.net
add address=127.0.0.1 name=ads.bca.co.id
add address=127.0.0.1 name=adsbingo.com
add address=127.0.0.1 name=adsdelivery.bid
add address=127.0.0.1 name=ads.diggoods.com
add address=127.0.0.1 name=ads.exdynsrv.com
add address=127.0.0.1 name=ads.flurry.com
add address=127.0.0.1 name=ads.genieessp.com
add address=127.0.0.1 name=ads.glispa.com
add address=127.0.0.1 name=adsglow.net
add address=127.0.0.1 name=ads.gold
add address=127.0.0.1 name=adskom.com
add address=127.0.0.1 name=ads-link.net
add address=127.0.0.1 name=ads.medi-8.net
add address=127.0.0.1 name=ads.mopub.com
add address=127.0.0.1 name=ads.nexage.com
add address=127.0.0.1 name=ads.pubmatic.com
add address=127.0.0.1 name=adstars.co.id
add address=127.0.0.1 name=ads.themoneytizer.com
add address=127.0.0.1 name=ad-stir.com
add address=127.0.0.1 name=adstract.trackclk.com
add address=127.0.0.1 name=ads.yahoo.com
add address=127.0.0.1 name=ad.turn.com
add address=127.0.0.1 name=afbcashidr.com
add address=127.0.0.1 name=ajangiklangratis.com
add address=127.0.0.1 name=aktrack.pubmatic.edgekey.net
add address=127.0.0.1 name=alertpay.com
add address=127.0.0.1 name=ampclicks.com
add address=127.0.0.1 name=analisis.io
add address=127.0.0.1 name=analytics.picsart.com
add address=127.0.0.1 name=anekaiklan.com
add address=127.0.0.1 name=api.ipify.org
add address=127.0.0.1 name=apmmedia.net
add address=127.0.0.1 name=app.adjust.com
add address=127.0.0.1 name=app-measurement.com
add address=127.0.0.1 name=appnext.com
add address=127.0.0.1 name=appnext.hs.llnwd.net
add address=127.0.0.1 name=asxzd.pro
add address=127.0.0.1 name=a.teads.tv
add address=127.0.0.1 name=axzsd.pro
add address=127.0.0.1 name=azxsd.pro
add address=127.0.0.1 name=baliadv.com
add address=127.0.0.1 name=bellaads.com
add address=127.0.0.1 name=bestadbid.com
add address=127.0.0.1 name=bes-t-to-p-applicatio-and-dev-online.site
add address=127.0.0.1 name=big.kingcontests.win
add address=127.0.0.1 name=bisa88.com
add address=127.0.0.1 name=bmnet-ads.com
add address=127.0.0.1 name=browsergames2019.com
add address=127.0.0.1 name=bunchofwinners.win
add address=127.0.0.1 name=cas.criteo.com
add address=127.0.0.1 name=cd8iw9mh.cricket
add address=127.0.0.1 name=cdn.adsafeprotected.com
add address=127.0.0.1 name=cdnasiaclub.com
add address=127.0.0.1 name=cdn.onesignal.com
add address=127.0.0.1 name=cdn.run-syndicate.com
add address=127.0.0.1 name=cdnstatic.detik.com
add address=127.0.0.1 name=cfasync.ga
add address=127.0.0.1 name=cjsab.com
add address=127.0.0.1 name=click.accesstrade.co.id
add address=127.0.0.1 name=clickforfreeandready2updating.bid
add address=127.0.0.1 name=clickmedia.co.id
add address=127.0.0.1 name=clickredirection.com
add address=127.0.0.1 name=clksite.com
add address=127.0.0.1 name=cmdts.ksmobile.com
add address=127.0.0.1 name=cm.marketgid.com
add address=127.0.0.1 name=codeonclick.com
add address=127.0.0.1 name=connect.facebook.net
add address=127.0.0.1 name=cpaclickoffers.com
add address=127.0.0.1 name=cytochemistryrecitativewrasse.com
add address=127.0.0.1 name=d15cjcet1djbmv.cloudfront.net
add address=127.0.0.1 name=d28k9nkt2spnp.cloudfront.net
add address=127.0.0.1 name=d2jn12r3o7an7z.cloudfront.net
add address=127.0.0.1 name=d31qbv1cthcecs.cloudfront.net
add address=127.0.0.1 name=d6swopgiplmy0.cloudfront.net
add address=127.0.0.1 name=dafa.io
add address=127.0.0.1 name=dashbo15myapp.com
add address=127.0.0.1 name=dearerfonder.info
add address=127.0.0.1 name=dewsburg.info
add address=127.0.0.1 name=digitalmerkat.info
add address=127.0.0.1 name=dk7rftbivnkgr.cloudfront.net
add address=127.0.0.1 name=dolohen.com
add address=127.0.0.1 name=downloadgot.com
add address=127.0.0.1 name=dqqulesm3pfse.cloudfront.net
add address=127.0.0.1 name=dubshub.com$script,third-party
add address=127.0.0.1 name=dulcetcgvcxr.com
add address=127.0.0.1 name=dzbx8qv1at614.cloudfront.net
add address=127.0.0.1 name=e93-apps.com
add address=127.0.0.1 name=eclkmpbn.com
add address=127.0.0.1 name=eclkmpsa.com
add address=127.0.0.1 name=edomz.com
add address=127.0.0.1 name=engine.spotscenered.info
add address=127.0.0.1 name=entitlements.jwplayer.com
add address=127.0.0.1 name=everyday-carry.com
add address=127.0.0.1 name=eze99.net
add address=127.0.0.1 name=fcjiqwghf.bid
add address=127.0.0.1 name=find.magicadsroute.com
add address=127.0.0.1 name=flexterkita.com
add address=127.0.0.1 name=fnkyyrgraizy.com
add address=127.0.0.1 name=fonderreaders.info
add address=127.0.0.1 name=forumiklan.com
add address=127.0.0.1 name=gahhlbxdgw.com
add address=127.0.0.1 name=gjeyqtunbnap.com
add address=127.0.0.1 name=global.appnext.com
add address=127.0.0.1 name=go.mobifunworld.com
add address=127.0.0.1 name=googleadapis.l.google.com
add address=127.0.0.1 name=googleadservices.com
add address=127.0.0.1 name=googleads.g.doubleclick.net
add address=127.0.0.1 name=google-analytics.com
add address=127.0.0.1 name=googletagmanager.com
add address=127.0.0.1 name=googletagservices.com
add address=127.0.0.1 name=graph.accountkit.com
add address=127.0.0.1 name=graph.instagram.com
add address=127.0.0.1 name=greatwork.info
add address=127.0.0.1 name=groupiklan.com
add address=127.0.0.1 name=gudangbanner.com
add address=127.0.0.1 name=gxwjkbxubfjd.com
add address=127.0.0.1 name=halal.ad
add address=127.0.0.1 name=hclccadfmkpw.com
add address=127.0.0.1 name=hsoyrqqsludd.com
add address=127.0.0.1 name=huzcotxmghlfip.bid
add address=127.0.0.1 name=hwoxt.com
add address=127.0.0.1 name=id.asia.gettoday.info
add address=127.0.0.1 name=iklanads.com
add address=127.0.0.1 name=iklanbarisgratis.co.uk
add address=127.0.0.1 name=iklanbarisgratispasang.com
add address=127.0.0.1 name=iklanbarisgratispasang.net
add address=127.0.0.1 name=iklanbarismu.com
add address=127.0.0.1 name=iklanbisnispro.com
add address=127.0.0.1 name=iklanblogger.com
add address=127.0.0.1 name=iklanbogor.com
add address=127.0.0.1 name=iklandenpasar.com
add address=127.0.0.1 name=iklandiweb.com
add address=127.0.0.1 name=iklangratis88.com
add address=127.0.0.1 name=iklangratis.co.uk
add address=127.0.0.1 name=iklangratismu.com
add address=127.0.0.1 name=iklanhemat.com
add address=127.0.0.1 name=iklanhoki.com
add address=127.0.0.1 name=iklan-indo.org
add address=127.0.0.1 name=iklan-laris.com
add address=127.0.0.1 name=iklanoke.com
add address=127.0.0.1 name=iklanonlinemu.com
add address=127.0.0.1 name=iklanpasanggratis.com
add address=127.0.0.1 name=iklan-sukses.com
add address=127.0.0.1 name=iklantanpadaftar.com
add address=127.0.0.1 name=iklantelevisi.com
add address=127.0.0.1 name=iklantext.com
add address=127.0.0.1 name=iklantop.net
add address=127.0.0.1 name=iklanumum.com
add address=127.0.0.1 name=ikoh6ie.top
add address=127.0.0.1 name=ilxhsgd.com
add address=127.0.0.1 name=imasdk.googleapis.com
add address=127.0.0.1 name=imaxbet.com
add address=127.0.0.1 name=imgg-cdn.adskeeper.co.uk
add address=127.0.0.1 name=indobanner.com
add address=127.0.0.1 name=indofreeads.com
add address=127.0.0.1 name=indonesia.thor-hammer.me
add address=127.0.0.1 name=istanaiklan.com
add address=127.0.0.1 name=iupqelechcmj.com
add address=127.0.0.1 name=jagoiklan.com
add address=127.0.0.1 name=jagopromo.com
add address=127.0.0.1 name=jasaiklan.com
add address=127.0.0.1 name=javaiklan.com
add address=127.0.0.1 name=jillsclickcorner.com
add address=127.0.0.1 name=jjxsdkphpcwu.com
add address=127.0.0.1 name=jomys.xyz
add address=127.0.0.1 name=js.ad-stir.com
add address=127.0.0.1 name=jsc.mgid.com
add address=127.0.0.1 name=juda0vnw.celi.gdn
add address=127.0.0.1 name=juruiklan.com
add address=127.0.0.1 name=jwpltx.com
add address=127.0.0.1 name=klikabadi.com
add address=127.0.0.1 name=klikabadi.net
add address=127.0.0.1 name=klikajadeh.com
add address=127.0.0.1 name=kmiobghwsc.bid
add address=127.0.0.1 name=koolmedia.info
add address=127.0.0.1 name=ktrackdata.com
add address=127.0.0.1 name=l9tdhe6.com
add address=127.0.0.1 name=lacakqq.com
add address=127.0.0.1 name=ld82ydd.com
add address=127.0.0.1 name=lokeriklan.com
add address=127.0.0.1 name=m.9clubasia.com
add address=127.0.0.1 name=macarier.review
add address=127.0.0.1 name=masteriklan.net
add address=127.0.0.1 name=masternaga99.com
add address=127.0.0.1 name=medi8.genieesspv.jp
add address=127.0.0.1 name=mediab.uy
add address=127.0.0.1 name=mesiniklan.andipublisher.com
add address=127.0.0.1 name=mgid.com
add address=127.0.0.1 name=mobile.foma-ds.com
add address=127.0.0.1 name=mobile.pipe.aria.microsoft.com
add address=127.0.0.1 name=mrperfect.in$script,third-party
add address=127.0.0.1 name=mybannermaker.com
add address=127.0.0.1 name=net-s-sof-t-open.site
add address=127.0.0.1 name=newopenx.detik.com
add address=127.0.0.1 name=newrevive.detik.com
add address=127.0.0.1 name=new-winners-online.com
add address=127.0.0.1 name=n.popclck.org
add address=127.0.0.1 name=octafx.com
add address=127.0.0.1 name=offerjuice.me
add address=127.0.0.1 name=ola.com
add address=127.0.0.1 name=onclkds.com
add address=127.0.0.1 name=onedollarptc.com
add address=127.0.0.1 name=openadserving.com
add address=127.0.0.1 name=outbrain.com
add address=127.0.0.1 name=ov2ochu.bid
add address=127.0.0.1 name=p.adsymptotic.com
add address=127.0.0.1 name=pagead1.googlesyndication.com
add address=127.0.0.1 name=pagead2.googleadservices.com
add address=127.0.0.1 name=pagead2.googlesyndication.com
add address=127.0.0.1 name=pagead.googlesyndication.com
add address=127.0.0.1 name=paidforfree.com
add address=127.0.0.1 name=paid.outbrain.com
add address=127.0.0.1 name=partner.googleadservices.com
add address=127.0.0.1 name=pasangiklan.com
add address=127.0.0.1 name=pasangiklangratisbaris.com
add address=127.0.0.1 name=pasangiklangratisbaris.net
add address=127.0.0.1 name=pasariklanbaris.com
add address=127.0.0.1 name=paypopup.com
add address=127.0.0.1 name=pendekarqq.net
add address=127.0.0.1 name=pippio.com
add address=127.0.0.1 name=play.leadzu.com
add address=127.0.0.1 name=pondokiklan.com
add address=127.0.0.1 name=popmyads.com
add address=127.0.0.1 name=popunderjs.club
add address=127.0.0.1 name=prmvz.net
add address=127.0.0.1 name=promobagus.com
add address=127.0.0.1 name=promotioncamp.com
add address=127.0.0.1 name=props.id
add address=127.0.0.1 name=publish.web.id
add address=127.0.0.1 name=pusatiklan.com
add address=127.0.0.1 name=pussl13.com
add address=127.0.0.1 name=pwdmtyzyq.com
add address=127.0.0.1 name=qqpilihan.com
add address=127.0.0.1 name=realwap.net
add address=127.0.0.1 name=redonetype.com
add address=127.0.0.1 name=referral-secrets.com
add address=127.0.0.1 name=replase.gq
add address=127.0.0.1 name=replase.ml
add address=127.0.0.1 name=rkbjbtxhdi.bid
add address=127.0.0.1 name=runative.com
add address=127.0.0.1 name=runreproducerow.com
add address=127.0.0.1 name=run-syndicate.com
add address=127.0.0.1 name=s0.2mdn.net
add address=127.0.0.1 name=s2pops.club
add address=127.0.0.1 name=s2.youtube.com
add address=127.0.0.1 name=s7.addthis.com
add address=127.0.0.1 name=sanglah.com
add address=127.0.0.1 name=scriptall.ml
add address=127.0.0.1 name=search.linkmyc.com
add address=127.0.0.1 name=sebar.idblognetwork.com
add address=127.0.0.1 name=securepubads.g.doubleclick.net
add address=127.0.0.1 name=seen-on-screen.thewhizmarketing.com
add address=127.0.0.1 name=see-work.info
add address=127.0.0.1 name=sentrapromosi.com
add address=127.0.0.1 name=serbapromo.com
add address=127.0.0.1 name=serve.popads.net
add address=127.0.0.1 name=settings.crashlytics.com
add address=127.0.0.1 name=sidikiwinnings.webcam
add address=127.0.0.1 name=sitti.co.id
add address=127.0.0.1 name=situsiklanbaris.com
add address=127.0.0.1 name=slotsbig777.com
add address=127.0.0.1 name=ssl.google-analytics.com
add address=127.0.0.1 name=sspintrafmsmt.com
add address=127.0.0.1 name=ssp.zryydi.com
add address=127.0.0.1 name=static.criteo.net
add address=127.0.0.1 name=static.doubleclick.net
add address=127.0.0.1 name=stats.appsflyer.com
add address=127.0.0.1 name=sumberiklan.com
add address=127.0.0.1 name=suryaiklan.com
add address=127.0.0.1 name=sworatio.co
add address=127.0.0.1 name=sync.aralego.com
add address=127.0.0.1 name=sync.search.spotxchange.com
add address=127.0.0.1 name=s.youtube.com
add address=127.0.0.1 name=taboola.com
add address=127.0.0.1 name=tangkasnet.cool
add address=127.0.0.1 name=t.appsflyer.com
add address=127.0.0.1 name=teliad.com
add address=127.0.0.1 name=tgw-pmir.3g.qq.com
add address=127.0.0.1 name=theclickers.net
add address=127.0.0.1 name=tinggalklik.com
add address=127.0.0.1 name=topklik.com
add address=127.0.0.1 name=topsurfer.com
add address=127.0.0.1 name=torimochi.line-apps.com
add address=127.0.0.1 name=traacker2.info
add address=127.0.0.1 name=track.aptitudemedia.co
add address=127.0.0.1 name=track.atom-data.io
add address=127.0.0.1 name=track.spzan.com
add address=127.0.0.1 name=tradeadexchange.com
add address=127.0.0.1 name=translationbuddy.com
add address=127.0.0.1 name=trc.taboola.com
add address=127.0.0.1 name=trdks.com
add address=127.0.0.1 name=trk.cpaoptimizer.com
add address=127.0.0.1 name=trk.yexmox.com
add address=127.0.0.1 name=trndoffers.com
add address=127.0.0.1 name=tummiarunzpf.com
add address=127.0.0.1 name=twap.eu
add address=127.0.0.1 name=undef8trust.com
add address=127.0.0.1 name=uoarbhxfyygn.com
add address=127.0.0.1 name=u-on.eu
add address=127.0.0.1 name=usa.ime.cootek.com
add address=127.0.0.1 name=useads.com
add address=127.0.0.1 name=vdtrack.com
add address=127.0.0.1 name=video-ad-stats.googlesyndication.com
add address=127.0.0.1 name=vrewpywootyu.com
add address=127.0.0.1 name=webiklan.com
add address=127.0.0.1 name=weblogiklan.com
add address=127.0.0.1 name=win2.sponsergift.club
add address=127.0.0.1 name=window-close.cf
add address=127.0.0.1 name=window-close.ga
add address=127.0.0.1 name=winplaygotwofri.info
add address=127.0.0.1 name=www.adskeeper.co
add address=127.0.0.1 name=www.adskeeper.co.uk
add address=127.0.0.1 name=www.appnext.com
add address=127.0.0.1 name=www.bisa88.com
add address=127.0.0.1 name=www.googleadservices.com
add address=127.0.0.1 name=www.google-analytics.com
add address=127.0.0.1 name=www.googletagservices.com
add address=127.0.0.1 name=www.gotrack1.es
add address=127.0.0.1 name=www.headwaydigital.com
add address=127.0.0.1 name=www.ionwin88.net
add address=127.0.0.1 name=www.judibolanet.com
add address=127.0.0.1 name=www.mgid.com
add address=127.0.0.1 name=www.outbrain.com
add address=127.0.0.1 name=www.pokerpedia.us
add address=127.0.0.1 name=www.translationbuddy.com
add address=127.0.0.1 name=www.u1trkqf.com
add address=127.0.0.1 name=xbfk51p7.review
add address=127.0.0.1 name=xqquphzq.bid
add address=127.0.0.1 name=yeah-mobile.com
add address=127.0.0.1 name=yesads.com
add address=127.0.0.1 name=yllix.com
add address=127.0.0.1 name=ylx-2.com
add address=127.0.0.1 name=ylx-4.com
add address=127.0.0.1 name=yx-ads6.com


File: /README.md
# adlists
Daftar iklan ngumpulin satu-satu


