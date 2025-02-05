# Repository Information
Name: mikrotik-perl-api

# Directory Structure
Directory structure:
└── github_repos/mikrotik-perl-api/
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
    │   │       ├── pack-752089216c3cf427ea0326d61f600207fd886242.idx
    │   │       └── pack-752089216c3cf427ea0326d61f600207fd886242.pack
    │   ├── packed-refs
    │   └── refs/
    │       ├── heads/
    │       │   └── master
    │       ├── remotes/
    │       │   └── origin/
    │       │       └── HEAD
    │       └── tags/
    ├── LICENSE
    ├── Mtik.pm
    ├── mtik_api_example.pl
    ├── mtik_tty.pl
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
	url = https://github.com/ellocofray/mikrotik-perl-api.git
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
0000000000000000000000000000000000000000 bbc40fd44fddf117a1b970da1f9a731a3632c72c vivek-dodia <vivek.dodia@icloud.com> 1738606470 -0500	clone: from https://github.com/ellocofray/mikrotik-perl-api.git


File: /.git\logs\refs\heads\master
0000000000000000000000000000000000000000 bbc40fd44fddf117a1b970da1f9a731a3632c72c vivek-dodia <vivek.dodia@icloud.com> 1738606470 -0500	clone: from https://github.com/ellocofray/mikrotik-perl-api.git


File: /.git\logs\refs\remotes\origin\HEAD
0000000000000000000000000000000000000000 bbc40fd44fddf117a1b970da1f9a731a3632c72c vivek-dodia <vivek.dodia@icloud.com> 1738606470 -0500	clone: from https://github.com/ellocofray/mikrotik-perl-api.git


File: /.git\packed-refs
# pack-refs with: peeled fully-peeled sorted 
bbc40fd44fddf117a1b970da1f9a731a3632c72c refs/remotes/origin/master


File: /.git\refs\heads\master
bbc40fd44fddf117a1b970da1f9a731a3632c72c


File: /.git\refs\remotes\origin\HEAD
ref: refs/remotes/origin/master


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



File: /Mtik.pm
#! /usr/bin/perl -w
# Mtik.pm - a simple Mikrotik Router API client
# Version 1.0 Beta
# Hugh Messenger - hugh at alaweb dot com
# Released under Creative Commons license.
# Do with it what you will, but don't blame me!
#----------------

package Mtik;
$VERSION = '0.01';
$debug = 0;
$error_msg = '';

use strict;
use vars qw(
            $VERSION
            @ISA
            @EXPORT
            @EXPORT_OK
            $debug
            $error_msg
           );

use IO::Socket;
use Digest::MD5;

@ISA        = qw(Exporter);
@EXPORT     = qw();
@EXPORT_OK  = qw(
                 $debug
                 $error_msg
                );
                
my($sock);

sub mtik_connect
{
    my($host) = shift;
    my($port) = shift || 8728;
    if (!($host))
    {
        print "no host!\n";
        return 0;
    }
    my($sock) = new IO::Socket::INET(
                    PeerAddr => $host,
                    PeerPort => $port,
                    Proto    => 'tcp');
    if (!($sock))
    {
        print "no socket :$!\n";
        return 0;
    }
    return $sock;
}

sub write_word {
    my($word) = shift;
    &write_len(length($word));
    print $sock $word;
}

sub write_sentence {
    my($sentence_ref) = shift;
    my(@sentence) = @$sentence_ref;
    foreach my $word (@sentence)
    {
        write_word($word);
        if ($debug > 2)
        {
            print ">>> $word\n";
        }
    }
    write_word('');
}

sub write_len {
    my($len) = shift;
    if ($len < 0x80)
    {
        print $sock chr($len);
    }
    elsif ($len < 0x4000)
    {
        $len |= 0x8000;
        print $sock chr(($len >> 8) & 0xFF);
        print $sock chr($len & 0xFF);
    }
    elsif ($len < 0x200000)
    {
        $len |= 0xC00000;
        print $sock chr(($len >> 8) & 0xFF);
        print $sock chr(($len >> 8) & 0xFF);
        print $sock chr($len & 0xFF);
    }
    elsif ($len < 0x10000000)
    {
        $len |= 0xE0000000;
        print $sock chr(($len >> 8) & 0xFF);
        print $sock chr(($len >> 8) & 0xFF);
        print $sock chr(($len >> 8) & 0xFF);
        print $sock chr($len & 0xFF);
    }
    elsif ($len < 0x10000000)
    {
        $len |= 0xE0000000;
        print $sock chr(($len >> 8) & 0xFF);
        print $sock chr(($len >> 8) & 0xFF);
        print $sock chr(($len >> 8) & 0xFF);
        print $sock chr($len & 0xFF);
    }
}

sub read_len {
    if ($debug > 4)
    {
        print "start read_len\n";
    }
    my $line;
    $sock->recv($line,1);
    my($len) = ord($line);
    if ($len & 0x80)
    {
        return $len;
    }
    elsif ($len & 0xC0 == 0x80)
    {
        $len &= !0xC0;
        $len <<= 8;
        $len += read_len();
    }
    elsif ($len & 0xE0 == 0xC0)
    {
        $len &= !0xE0;
        $len <<= 8;
        $len += read_len();
        $len <<=8;
        $len += read_len();
    }
    elsif ($len & 0xF0 == 0xE0)
    {
        $len &= !0xF0;
        $len <<= 8;
        $len += read_len();
        $len <<=8;
        $len += read_len();        
        $len <<=8;
        $len += read_len();        
    }
    elsif ($len & 0xF8 == 0xF0)
    {
        $len = read_len();
        $len <<= 8;
        $len += read_len();
        $len <<=8;
        $len += read_len();        
        $len <<=8;
        $len += read_len();    
    }
    if ($debug > 4)
    {
        print "read_len got $len\n";
    }
    return $len;
}

sub read_word {
    my($ret_line) = '';
    my($len) = &read_len();
    if ($len > 0)
    {
        if ($debug > 3)
        {
            print "recv $len\n";
        }
        while (1) {
            my($line) = '';
            $sock->recv($line,$len);
            # append to $ret_line, in case we didn't get the whole word and are going round again
            $ret_line .= $line;
            my $got_len = length($line);
            if ($got_len < $len)
            {
                # we didn't get the whole word, so adjust length and try again
                $len -= $got_len;
            }
            else
            {
                # woot woot!  we got the required length
                last;
            }
        }
    }
    return $ret_line;
}

sub read_sentence {
    my ($word);
    my ($i) = 0;
    my (@reply);
    my($retval) = 0;
    while ($word = &read_word())
    {
            if ($word =~ /!done/)
            {
                $retval = 1;
            }
            elsif ($word =~ /!trap/)
            {
                $retval = 2;
            }
            elsif ($word =~ /!fatal/)
            {
                $retval = 3;
            }
        $reply[$i++] = $word;
        if ($debug > 2)
        {
            print "<<< $word\n"
        }
    }
    return ($retval,@reply);
}

######## PUBLIC FUNCTIONS ############

sub talk
{
    #my(@sentence) = shift;
    my($sentence_ref) = shift;
    my(@sentence) = @$sentence_ref;
    &write_sentence(\@sentence);
    my(@reply);
    my(@attrs);
    my($i) = 0;
    my($retval) = 0;
    while (($retval,@reply) = &read_sentence())
    {
        foreach my $line (@reply)
        {
            if ($line =~ /^=(\S+)=(.*)/)
            {
                $attrs[$i]{$1} = $2;
            }
        }
        if ($retval > 0)
        {
            last;
        }
        $i++;
    }
    return ($retval, @attrs);
}

sub raw_talk
{
    my(@sentence) = @{(shift)};
    &write_sentence(\@sentence);
    my(@reply);
    my(@response);
    my($i) = 0;
    my($retval) = 0;
    while (($retval,@reply) = &read_sentence())
    {
        foreach my $line (@reply)
        {
            push(@response, $line);
        }
        if ($retval > 0)
        {
            last;
        }
    }
    return ($retval,@response);
}

sub login
{
    my($host) = shift;
    my($username) = shift;
    my($passwd) = shift;

    if (!($sock = &mtik_connect($host)))
    {
        return 0;
    }
    my(@command);
    push(@command,'/login');
    my($retval,@results) = talk(\@command);
    my($chal) = pack("H*",$results[0]{'ret'});
    my($md) = new Digest::MD5;
    $md->add(chr(0));
    $md->add($passwd);
    $md->add($chal);
    my($hexdigest) = $md->hexdigest;
    undef(@command);
    push(@command, '/login');
    push(@command, '=name=' . $username);
    push(@command, '=response=00' . $hexdigest);
    ($retval,@results) = &talk(\@command);
    if ($retval > 1)
    {
        $error_msg = $results[0]{'message'};
        return 0;
    }
    if ($debug > 0)
    {
        print "Logged in to $host as $username\n";
    }
    return 1;
}

sub logout
{
    close $sock;     
}

sub get_by_key
{
    my($cmd) = shift;
    my($id) = shift || '.id';
    $error_msg = '';
    my(@command);
    push(@command,$cmd);
    my(%ids);
    my($retval,@results) = &Mtik::talk(\@command);
    if ($retval > 1)
    {
        $error_msg = $results[0]{'message'};
        return %ids;
    }
    foreach my $attrs (@results)
    {
        my $key = '';
        foreach my $attr (keys (%{$attrs}))
        {
            my $val = ${$attrs}{$attr};
            if ($attr eq $id)
            {
                $key = $val;
                #delete(${$attrs}{$attr});
            }
        }
        if ($key)
        {
            $ids{$key} = $attrs;
        }
    }
    return %ids;
}

sub mtik_cmd
{
    my($cmd) = shift;
    my(%attrs) = %{(shift)};
    $error_msg = '';
    my(@command);
    push(@command,$cmd);
    foreach my $attr (keys (%attrs))
    {
        push(@command,'=' . $attr . '=' . $attrs{$attr});
    }
    my($retval,@results) = talk(\@command);
    if ($retval > 1)
    {
        $error_msg = $results[0]{'message'};
    }
    return ($retval,@results);
}

1;


File: /mtik_api_example.pl
#!/usr/bin/perl -w
use strict;

use vars qw($error_msg $debug);
use Mtik;

$Mtik::debug = 2;

###############################################################################
######
###### Examples of how to drive the Mtik module.
######
###### Some useful routines for manipulating wireless ACL's, i.e. using commands
###### from:
######
###### /interface wireless access-list
######

sub mtik_wireless_access_get_macs
{
    # get a list of all wireless access items.  We're specifying 'mac-address'
    # as the key, so the resulting associative array will be indexed by mac.
    # If we left the second argument off, it would index by the Mtik internal ID
    my(%wireless_macs) = Mtik::get_by_key('/interface/wireless/access-list/print','mac-address');
    if ($Mtik::error_msg eq '')
    {
        # so now we have a two domensional associative array, first keyed
        # by the MAC, then by attributes.  Print it out if in debug.
        if ($Mtik::debug > 5)
        {
            foreach my $mac (keys (%wireless_macs))
            {
                print "MAC: $mac\n";
                foreach my $attr (keys (%{$wireless_macs{$mac}}))
                {
                    print "   $attr: $wireless_macs{$mac}{$attr}\n";
                }
            }
        }
    }
    # we return the array rather than setting a global, as we pretty much always
    # want to call this routine prior to doing anything with ACL's, even if it
    # has already been called, in case someone else has changed the ACL list
    # underneath us.
    return %wireless_macs;
}

sub mtik_wireless_access_mac_exists
{
    my($mac) = shift;
    # we need to load the access list every time we check, because other
    # people could be actively making changes
    my(%wireless_macs) = &mtik_wireless_access_get_macs();
    if ($Mtik::error_msg)
    {
        chomp($Mtik::error_msg);
        $Mtik::error_msg .= "\nWireless access list not loaded\n";
        return -1;
    }
    return(defined($wireless_macs{$mac}));
}

sub mtik_wireless_access_add
{
    my(%attrs) = %{(shift)};
    # first lets check to see if this MAC already exists
    my($exists) = mtik_wireless_access_mac_exists($attrs{'mac-address'});
    if ($exists != 0)
    {
        if ($exists > 0)
        {
            print "Wireless MAC already on access list: $attrs{'mac-address'}\n";
        }
        else
        {
            print "Unknow error: $Mtik::error_msg\n";
        }
        return 0;
    }
    
    # doesn't exist, so go ahead and add it
    my($retval,@results) = Mtik::mtik_cmd('/interface/wireless/access-list/add',\%attrs);
    if ($retval == 1)
    {
        # Mtik ID of the added item will be in $results[0]{'ret'}
        my($mtik_id) = $results[0]{'ret'};
        if ($Mtik::debug)
        {
            print "New Mtik ID: $mtik_id\n";
        }
        return $mtik_id;
    }
    else
    {
        # Error message will be in $Mtik::error_msg
        print "Unknown error: $Mtik::error_msg\n";
        return 0;
    }
}

sub mtik_wireless_access_set_by_mac
{
    my($mac) = shift;
    my(%attrs) = %{(shift)};
    # First we need to get the internal ID for the one we want to change.
    my(%wireless_macs) = &mtik_wireless_access_get_macs();
    if (my $mtik_id = $wireless_macs{$mac}{'.id'})
    {
        $attrs{'.id'} = $mtik_id;
        my($retval,@results) = Mtik::mtik_cmd('/interface/wireless/access-list/set',\%attrs);
        if ($retval == 1)
        {
            return 1;
        }
        # Error message will be in $Mtik::error_msg
        print "Unknown error: $Mtik::error_msg\n";
        return 0;
    }
    if ($Mtik::debug > 0)
    {
        print "MAC not found: $mac\n";
    }
    return 0;
}

sub mtik_wireless_access_get_by_mac
{
    my($mac) = shift;
    # even if we already fetched the acl list, we need to fetch it again
    # in case someone else has changed it.
    my(%wireless_macs) = &mtik_wireless_access_get_macs();
    return %{$wireless_macs{$mac}};
}

###############################################################################
######
###### Example test code
######
###### Obviously remove this section and replace with ...
###### 1;
###### ... if you want to use the above as library code.
######
###############################################################################

# CHANGE THESE to suit your environment.  Make sure $test_mac does NOT exist
# on the $mtik_host, as this test code will add / modify an ACL for it.
my($mtik_host) = '192.168.1.254';
my($mtik_username) = 'admin';
my($mtik_password) = 'SomeStr0ngPa33w0rd';
my($test_mac) = '00:12:34:56:78:9B';

print "Logging in to Mtik: $mtik_host\n";
if (Mtik::login($mtik_host,$mtik_username,$mtik_password))
{   
    # add a new wireless ACL.
    print "\nAdding new ACL for MAC: $test_mac\n";
    my(%attrs);
    $attrs{'mac-address'} = $test_mac;
    $attrs{'ap-tx-limit'} = '0';
    $attrs{'authentication'} = 'yes';
    $attrs{'client-tx-limit'} = '0';
    $attrs{'comment'} = "HUGH TEST";
    $attrs{'forwarding'} = 'no';
    $attrs{'interface'} = 'wlan1';
    $attrs{'private-algo'} = 'none';
    $attrs{'private-key'} = '';
    $attrs{'private-pre-shared-key'} = '';
    $attrs{'signal-range'} = '-120.120';
    if (my $mtik_id = &mtik_wireless_access_add(\%attrs))
    {
        print "Added new ACL for $test_mac with id: $mtik_id\n";
    }
    
    print "\nGetting ACL attributes for MAC: $test_mac\n";
    my(%attrs2) = &mtik_wireless_access_get_by_mac($test_mac);
    foreach my $attr (keys(%attrs2))
    {
        print "   $attr: $attrs2{$attr}\n"
    }
    
    # change attributes for a wireless ACL with a specified MAC.
    print "\nChanging attributes for $test_mac\n";
    my(%attrs3);
    $attrs3{'forwarding'} = 'yes';
    $attrs3{'comment'} = "SCOOBYDOO";
    if (&mtik_wireless_access_set_by_mac($test_mac,\%attrs3))
    {
        print "Set ACL attributes for MAC: $test_mac\n";
    }
    
    print "\nGetting ACL attributes for MAC: $test_mac\n";
    my(%attrs4) = &mtik_wireless_access_get_by_mac($test_mac);
    foreach my $attr (keys(%attrs4))
    {
        print "   $attr: $attrs4{$attr}\n"
    }

    Mtik::logout;
}



File: /mtik_tty.pl
use Mtik;

use Getopt::Std;

sub usage {
  print STDERR <<EOF;
Raw interface for testing the Mikrotik API.  Examples:

>>> /interface/wireless/access-list/print
>>>
[lots of output]
>>> !done
<<< /interface/wireless/access-list/set
<<< =.id=*F
<<< =comment=SKOOBYDOO2
<<<
>>> !done
<<< quit

Terminate commands sequences with blank line.
Type 'quit' (no quotes) to quit.

usage: $0 -m mtik_host -u mtik_user -p mtik_passwd

-h : help (this message)
-m : hostname or IP of Mikrotik router
-u : admin username
-p : password
EOF
  exit;
}

my($option_str) = "hm:u:p:";
my(%options);
getopts($option_str,\%options);
my($mtik_host) =  $options{'m'};
my($mtik_user) =  $options{'u'};
my($mtik_passwd) =  $options{'p'};
if ($options{'h'} || !($mtik_host && $mtik_user && $mtik_passwd)) {
  usage();
}

$Mtik::debug = 0;
if (Mtik::login($mtik_host,$mtik_user,$mtik_passwd)) {
  my($quit) = 0;
  while (!($quit)) {
    my(@cmd);
    print "<<< ";
    while (<>) {
      chomp;
      $_ =~ s/^<<< //;
      if (/^quit$/i) {
        $quit = 1;
        last;
      }
      elsif (/^$/) {
        last;
      }
      push(@cmd,$_);
      print "<<< ";
    }
    if (!($quit))
    {
      my($retval,@results) = Mtik::raw_talk(\@cmd);
      foreach my $result (@results) {
        print ">>> $result\n";
      }
    }
  }
  Mtik::logout();
}
else {
  print "Couldn't log in to $mtik_host\n";
}


File: /README.md
# mikrotik-perl-api
Perl API to manupulate Mikrotik devices.

API manual at http://wiki.mikrotik.com/wiki/Manual:API


