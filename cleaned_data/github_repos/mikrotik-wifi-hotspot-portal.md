# Repository Information
Name: mikrotik-wifi-hotspot-portal

# Directory Structure
Directory structure:
└── github_repos/mikrotik-wifi-hotspot-portal/
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
    │   │       ├── pack-ae411cf100d95982b8e4b0730596cea555f5363a.idx
    │   │       └── pack-ae411cf100d95982b8e4b0730596cea555f5363a.pack
    │   ├── packed-refs
    │   └── refs/
    │       ├── heads/
    │       │   └── master
    │       ├── remotes/
    │       │   └── origin/
    │       │       └── HEAD
    │       └── tags/
    ├── hotspot/
    │   ├── alogin.html
    │   ├── css/
    │   │   ├── form.css
    │   │   └── modal.css
    │   ├── error.html
    │   ├── errors.txt
    │   ├── img/
    │   ├── js/
    │   ├── login.html
    │   ├── logout.html
    │   ├── radvert.html
    │   ├── redirect.html
    │   ├── result.html
    │   ├── rlogin.html
    │   └── status.html
    ├── LICENSE
    ├── Log-in script on hotspot profile.txt
    ├── Log-out script on hotspot profile.txt
    ├── README.md
    └── script-KSC.txt


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
	url = https://github.com/drlight17/mikrotik-wifi-hotspot-portal.git
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
0000000000000000000000000000000000000000 24b110744e69b3a16d1b2d8fcbe4809a5c619851 vivek-dodia <vivek.dodia@icloud.com> 1738606072 -0500	clone: from https://github.com/drlight17/mikrotik-wifi-hotspot-portal.git


File: /.git\logs\refs\heads\master
0000000000000000000000000000000000000000 24b110744e69b3a16d1b2d8fcbe4809a5c619851 vivek-dodia <vivek.dodia@icloud.com> 1738606072 -0500	clone: from https://github.com/drlight17/mikrotik-wifi-hotspot-portal.git


File: /.git\logs\refs\remotes\origin\HEAD
0000000000000000000000000000000000000000 24b110744e69b3a16d1b2d8fcbe4809a5c619851 vivek-dodia <vivek.dodia@icloud.com> 1738606072 -0500	clone: from https://github.com/drlight17/mikrotik-wifi-hotspot-portal.git


File: /.git\packed-refs
# pack-refs with: peeled fully-peeled sorted 
24b110744e69b3a16d1b2d8fcbe4809a5c619851 refs/remotes/origin/master


File: /.git\refs\heads\master
24b110744e69b3a16d1b2d8fcbe4809a5c619851


File: /.git\refs\remotes\origin\HEAD
ref: refs/remotes/origin/master


File: /hotspot\alogin.html
<!doctype html>
<html lang="en">

<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <meta http-equiv="refresh" content="2; url=$(link-redirect)">
    <meta http-equiv="pragma" content="no-cache">
    <meta http-equiv="expires" content="-1">
    <title>Точка доступа в сеть Интернет - Перенаправление</title>
    <link rel="stylesheet" href="css/style.css">
    <script>
        function startClock() {
            $(if popup == 'true')
            open('$(link-status)', 'hotspot_status', 'toolbar=0,location=0,directories=0,status=0,menubars=0,resizable=1,width=290,height=200');
        $(endif)
        location.href = unescape('$(link-redirect-esc)');
        }

    </script> 
</head>

<body onLoad="startClock()">
    <div class="ie-fixMinHeight">
        <div class="main">
            <div class="wrap">
                <h1>Вы вошли</h1>
                <p class="info">Если ничего не происходит и для просмотра статистики, нажмите <a href="$(link-status)">здесь</a></p>
				<!--<p class="info2">Посмотреть <a href="$(link-status)">статистику</a></p>-->
            </div>
        </div>
    </div>
</body>

</html>


File: /hotspot\css\form.css
html, body {
    background: url(../img/background-ksc.png);
    height: 100%;
    background-size: cover;
    background-repeat: no-repeat;
}

.hide{
    display: none !important;
}

.container {
    width: 100%;
    width: 100%;
    height: 100% !important;
    margin: 0 auto;
    text-align: center;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
	font-family: Arial;
}

.logo {
    margin-bottom: 10px;
	/*margin-top: 45px;*/
}
.logo > img {
	width: 150px;
}
@media only screen and (max-width: 350px) {
	.logo > img {
        width: 90px;
    }
}

label {
    font-size: 12px;
    font-family: "Arial";
    color: rgb(50, 60, 71);
    text-transform: uppercase;
    line-height: 1.2;
    text-align: center;
}

.form {
    background: #fff;
    border: solid 1px rgb(220, 224, 226);
    border-radius: 15px;
    padding: 42px;

}

@media only screen and (min-width: 400px) {
    .form {
        padding: 24px;
    }
}

input[type="text"] {
    background-color: rgb(237, 245, 255);
    border: none;
    padding: 17px;
    margin: 7px;
    /*min-width: 280px;*/
    width: 100%;
    font-size: 18px;
}

.code input[type="text"], .form.already input[type="text"]{
    text-align: center !important;
}

.btn {

    font-size: 12px;
    font-family: "Arial";
    color: rgb(255, 255, 255);
    text-transform: uppercase;
    line-height: 1.2;
    text-align: center;

    border-radius: 5px;
    border: none;
    background-color: rgb(77, 161, 255);
    display: flex;
    flex-direction: row;
    flex-wrap: nowrap;

    padding: 12px 42px;
    cursor: pointer;
    transition: background-color .5s;

    margin: 0 auto;

}

.disabled, .disabled:hover{
    background: #eee !important;
    cursor: auto;
}

.btn:hover {
    background-color: rgb(110, 191, 255);
}

.form_description {
    font-size: 16px;
    font-family: "Arial";
    color: rgb(159, 166, 168);
    line-height: 1.2;
    text-align: center;
    margin-bottom: 14px;
}

.input_group {
    display: flex;
    align-items: center;
    justify-content: center;
}

.input_group img {
    margin-right: 14px;
}

#modal_trigger, #copyright, #copyright > small > a {
    padding: 4px;
    cursor: pointer;
	color: #ffffff !important;
	font-size: smaller;
}
#modal_trigger {
	text-decoration: underline;
}


File: /hotspot\css\modal.css
/*
Pure CSS modal box
Author: Jorge Chavez
Github: http://github.com/jorgechavz
*/


.modal .checkbox{
  display: none;
}

/* Gray background */
.modal .modal-overlay{
  opacity: 0;
  transition: all 0.3s ease;
  width: 50%;
  position: absolute;
  width: 100%;
  height: 100%;
  position: fixed;
  top: 0;
  left: 0;
  z-index: -100;
  transform: scale(1);
  display: none;
  background-color: rgba(0,0,0,0.7);
}

/* Box */
.modal .modal-wrap{
  background-color: #ddd;
  box-shadow: 3px 3px 3px rgba(0,0,0,0.2);
  padding: 40px 50px;
  width: 60%;
  margin: 20px auto;
  align-self: flex-start;
  border-radius: 2px;
  transition: all 0.5s ease;
}
.modal .modal-wrap.small{
  width: 30%;
}
.modal .modal-wrap.full{
  width: 100%;
  height: 100%;
}

.modal .modal-wrap.a-center {
  align-self: center;
}
.modal .modal-wrap.from-left {
  transform: translateX(-100%);
}
.modal .modal-wrap.from-right {
  transform: translateX(100%);
}
.modal .modal-wrap.from-top {
  transform: translateY(-100%);
}
.modal .modal-wrap.from-bottom {
  transform: translateY(100%);
}


/* Close button */
.modal .modal-overlay .close{
  position: absolute;
  right: 10px;
  top: 10px;
  font-size: 40px;
  width: 30px;
  height: 30px;
  color: #282c34;
}

.modal .modal-overlay .close:hover{
  cursor: pointer;
  color: #4b5361;
}


 .modal .o-close {
   width: 100%;
   height: 100%;
   position: fixed;
   left: 0;
   top: 0;
   z-index: -100;
 }

.modal input:checked ~ .o-close {
  z-index: 9998;
}
.modal input:checked ~ .modal-overlay{
  transform: scale(1);
  opacity:1;
  z-index: 9997;
  overflow: auto;
  display: flex;
  animation-duration: 0.5s;
  animation-name: fade-in;
  -moz-animation-duration: 0.5s;
  -moz-animation-name: fade-in;
  -webkit-animation-duration: 0.5s;
  -webkit-animation-name: fade-in;
}
.modal input:checked ~ .modal-overlay .modal-wrap {
  transform: translateY(0);
  z-index: 9999;
  text-align: justify;
}

/* Responsive Design */
/* Tablet size */
@media (max-width: 800px){
  .modal .modal-wrap {
    width: 80%;
    padding: 20px;
  }
}

/* Phone size */
@media (max-width: 500px){
  .modal .modal-wrap {
    width: 90%;
  }
}

/* Fadein from display:none */
@keyframes fade-in {
  0% {
    display: none;
    opacity: 0;
  }
  1% {
    display: flex;
    opacity: 0;
  }
  100% {
    display: flex;
    opacity: 1;
  }
}

@-moz-keyframes fade-in {
  0% {
    display: none;
    opacity: 0;
  }
  1% {
    display: flex;
    opacity: 0;
  }
  100% {
    display: flex;
    opacity: 1;
  }
}

@-webkit-keyframes fade-in {
  0% {
    display: none;
    opacity: 0;
  }
  1% {
    display: flex;
    opacity: 0;
  }
  100% {
    display: flex;
    opacity: 1;
  }
}


File: /hotspot\error.html
<html>

<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <meta http-equiv="pragma" content="no-cache">
    <meta http-equiv="expires" content="-1">
    <title>Точка доступа в сеть Интернет - Ошибка</title>
    <link rel="stylesheet" href="css/style.css">
</head>

<body>
    <div class="ie-fixMinHeight">
        <div class="main">
            <div class="wrap">
                <h1>Ошибка точки доступа: $(error)</h1>
                <p class="info">Страница входа: <a href="$(link-login)">$(link-login)</a></p>
            </div>
        </div>
    </div>
</body>

</html>


File: /hotspot\errors.txt
# This file contains error messages which are shown to user, when http/https
# login is used.
# These messages can be changed to make user interface more friendly, including
# translations to different languages.
#
# Various variables can be used here as well. Most frequently used ones are:
#	$(error-orig)	- original error message from hotspot
#	$(ip)		- ip address of a client
#	$(username)	- username of client trying to log in

# internal-error
# It should never happen. If it will, error page will be shown
# displaying this error message (error-orig will describe what has happened)

internal-error = Внутренняя ошибка ($(error-orig))

# config-error
# Should never happen if hotspot is configured properly.

config-error = Ошибка конфигурации ($(error-orig))

# not-logged-in
# Will happen, if status or logout page is requested by user,
# which actually is not logged in

not-logged-in = Вы не вошли (ip $(ip))

# ippool-empty
# IP address for user is to be assigned from ip pool, but there are no more
# addresses in that pool

ippool-empty = Невозможно назначить ip адрес - в пуле больше нет свободных адресов

# shutting-down
# When shutdown is executed, new clients are not accepted

shutting-down = Сервис отключается

# user-session-limit
# If user profile has limit of shared-users, then this error will be shown
# after reaching this limit

user-session-limit = Достигнут лимит подключений на логин $(username)

# license-session-limit
# Depending on licence number of active hotspot clients is limited to
# one or another amount. If this limit is reached, following error is displayed.

license-session-limit = Достигнут лимит времени сессии ($(error-orig))

# wrong-mac-username
# If username looks like MAC address (12:34:56:78:9a:bc), but is not
# a MAC address of this client, login is rejected

wrong-mac-username = Неверный логин ($(username)): этот MAC не ваш

# chap-missing
# If http-chap login method is used, but hotspot program does not receive
# back encrypted password, this error message is shown.
# Possible reasons of failure:
#	- JavaScript is not enabled in web browser;
#	- login.html page is not valid;
#	- challenge value has expired on server (more than 1h of inactivity);
#	- http-chap login method is recently removed;
# If JavaScript is enabled and login.html page is valid,
# then retrying to login usually fixes this problem.

chap-missing = Браузер не отправил ответ (проверьте, включена ли у вас поддержка JavaScript)

# invalid-username
# Most general case of invalid username or password. If RADIUS server
# has sent an error string with Access-Reject message, then it will
# override this setting.

invalid-username = Неправильный логин или пароль

# invalid-mac
# Local users (on hotspot server) can be bound to some MAC address. If login
# from different MAC is tried, this error message will be shown.

invalid-mac = Логин $(username) нельзя использовать с этого MAC адреса

# uptime-limit, traffic-limit
# For local hotspot users in case if limits are reached

uptime-limit = Достигнут лимит uptime для логина $(username)
traffic-limit = Достигнут лимит трафика для логина $(username)

# radius-timeout
# User is authenticated by RADIUS server, but no response is received from it,
# following error will be shown.

radius-timeout = RADIUS сервер не отвечает

# auth-in-progress
# Authorization in progress. Client already has issued an authorization request
# which is not yet complete.

auth-in-progress = Процесс авторизации уже начат, попробуйте еще раз чуть позже

# radius-reply
# Radius server returned some custom error message

radius-reply = $(error-orig)


File: /hotspot\login.html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Авторизация</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta name="author" content="Alexander A Kusakin <alexander.a.kusakin@gmail.com>">

    <link rel="stylesheet" href="./css/form.css">
    <link rel="stylesheet" href="./css/modal.css">

    <script src="./js/jquery-3.3.1.min.js"></script>
    <script src="./js/jquery.maskedinput.min.js"></script>
    <script type="text/javascript" src="/md5.js"></script>

    <script>
		function year_func()
			{
				var d = new Date();
				var year = d.getFullYear();
				document.getElementById("date").innerHTML=+year;
			}
        function isValidPhoneNumber(phone) {
            var pattern = new RegExp(/^\s*(8|\+7)\s*-?\s*\(?[\d-]{3,6}\)?[\d-]{5,11}$/i
            );
            return pattern.test(phone);
        }
		
		var count=60;
		var counter=setInterval(timer, 1000); //1000 will  run it every 1 second
		
		function timer()
			{
			  if ($('#timer:visible').length == 0) return;

			  count=count-1;
			  if (count <= 0)
			  {
				 clearInterval(counter);
				 jQuery('#timer').hide();
				 jQuery('.code .send_again').removeClass('disabled').addClass('active').show();
				 return;
			  }

			 document.getElementById("timer").innerHTML="Подождите пароль "+ count + " сек."; // watch for spelling
			}

		function check_send_email()
			{
				send_email = "";
				if (document.getElementById('send_email').checked) $("#username1").val("_email" + $("#username1").val());
			}

        jQuery(document).ready(function () {
			
			year_func();
			
			timer();
			
			check_send_email();
			
			jQuery('.code .send_again').on('keyup', function (e) {
				jQuery('form.login').fadeIn();
            });
			
            jQuery('#login').mask('+9-(999)-999-99-99').on('keyup', function (e) {
                if (e.keyCode === 13) {
                    return jQuery('.login .btn.active').click();
                }

                if (isValidPhoneNumber(jQuery(this).val())) {
                    jQuery('.login .btn.next').removeClass('disabled').addClass('active');
                    jQuery('#login_form').attr('action', '$(link-login-only)#' + document.getElementById('login').value.replace(/[\-\(\)]/g, ''));
					//jQuery('#login_form').attr('action', 'login.html#' + document.getElementById('login').value.replace(/[\-\(\)]/g, ''));
                    jQuery('#username1').val(document.getElementById('login').value.replace(/[\-\(\)]/g, ''));
					check_send_email();
                } else {
                    jQuery('.login .btn.next').removeClass('active').addClass('disabled');
                }

            });

            jQuery('#login2').mask('+9-(999)-999-99-99');

            jQuery('.already').on('keyup', '#login2', function (e) {

                if (e.keyCode === 13) {
                    return jQuery('.already .btn.active').click();
                }

                if (isValidPhoneNumber(jQuery(this).val())) {
                    jQuery('#username3').val(document.getElementById('login2').value.replace(/[\-\(\)]/g, ''));
                }

            }).on('keyup', '#code2', function (e) {

                if (event.keyCode === 13) {
                    return jQuery('.already .btn.active').click();
                }

                jQuery('#password2').val(hexMD5('$(chap-id)' + jQuery(this).val() + '$(chap-challenge)'));

            }).on('keyup', '#code2, #login2', function () {

                console.log(isValidPhoneNumber(jQuery('#login2').val()), jQuery('#password2').val().length >= 4)

                if (isValidPhoneNumber(jQuery('#login2').val()) && jQuery('#password2').val().length >= 4) {
                    jQuery('.already .btn').removeClass('disabled').addClass('active');
                } else {
                    jQuery('.already .btn').removeClass('active').addClass('disabled');
                }

            });

			jQuery('#send_email').change(function() {
				check_send_email();
			});

            jQuery('.btn').on('click', function (event) {

                if (jQuery(this).hasClass('disabled')) {
                    event.preventDefault();
                    event.stopPropagation();

                    return false;
                }

            });
			
			jQuery('.btn.next').on('click', function (event) {
				jQuery('#error_mess').hide();
            });

            jQuery('#code').on('keyup', function (event) {

                if (event.keyCode === 13) {
                    return jQuery('.code .btn.active').click();
                }

                if (jQuery(this).val().length < 4) {
                    jQuery(this).addClass('disabled').removeClass('active');
					jQuery('#timer').show();
					timer();
                } else {
                    jQuery(".code .btn").addClass('active').removeClass('disabled');
                    jQuery('#password').val(hexMD5('$(chap-id)' + jQuery(this).val() + '$(chap-challenge)'));
					jQuery('#timer').hide();
					jQuery('.code .send_again').removeClass('active').addClass('disabled').hide();
                }
            });

            jQuery('#has_code').on('click', function () {
				var login=$('#login').val();
				jQuery('#login2').val(login);
                jQuery('form.code, form.login').fadeOut(500, function () {
                    setTimeout(function () {
                        jQuery('form.already').fadeIn()
                    }, 500);
					//$('#login').val
					//$('#input').val("GeeksForGeeks"); 
                });
            });
			
			jQuery('#forgot_code').on('click', function () {
                jQuery('form.already').fadeOut(500, function () {
                    setTimeout(function () {
                        jQuery('form.login').fadeIn()
                    }, 500)
                });
            });
			jQuery('#forgot_code2').on('click', function () {
                jQuery('form.code').fadeOut(500, function () {
                    setTimeout(function () {
                        jQuery('form.login').fadeIn();
						jQuery('details').attr("open","true");
						jQuery('#error_mess').hide();
                    }, 500)
                });

            });

            if (!!window.location.hash) {
                jQuery('#username2').val(window.location.hash.replace('#', ''));
                jQuery('form.code').fadeIn();
            } else {
                jQuery('form.login').fadeIn();
            }

        });
		
    </script>
</head>
<body>
<div class="container">
    <div class="logo">
        <img src="./img/logo-ksc.png" alt="integrasky">
    </div>
	<!-- Обслуживание 
	<form class="form login" id="login_form" method="get" name="sendin"
	<label for="login2">По техническим причинам регистрация в гостевой wifi сети в настоящий момент недоступна! Попробуйте подключиться позже!</label>
	</form>-->
	<!-- раскомментировать после обслуживания -->
    <form class="form login" id="login_form" style="display: none" method="post" name="sendin"
          action="$(link-login-only)">
		                <p class="info $(if error)alert$(endif)">
                        $(if error == "")<label>Пожалуйста, зарегистрируйтесь, чтобы<br>воспользоваться доступом в Интернет</label>$(if trial == 'yes')<br />Free trial available, <a href="$(link-login-only)?dst=$(link-orig-esc)&amp;username=T-$(mac-esc)">click here</a>.$(endif)
                        $(endif)

                        $(if error)<label id="error_mess" style="color:red;">$(error)</label>$(endif)
                    </p>
        <label for="login">Введите Ваш номер телефона</label>
        <br>
        <div class="input_group tel">
            <img src="./img/number.svg" alt="number">
            <input type="hidden" name="username" id="username1">
            <input type="text" id="login" placeholder="+X-(XXX)-XXX-XX-XX">
			<input type="hidden" name="popup" value="true" />
        </div>
        <br>
        <button class="btn next disabled">
            Далее
        </button>
				<br>
		<label><details>
			<summary style="cursor:pointer"><strong>Не приходит СМС?</strong></summary>
			<br>Если ответная СМС при регистрации не приходит,<br>поставьте чек бокс ниже и обратитесь в отдел НОО, либо<br>к администратору гостиницы, если вы проживаете в гостинице КНЦ РАН.
		    <p><input style="vertical-align: middle;" type="checkbox" id="send_email"  name="send_email"/><label for="send_email">отправить копию пароля администратору</label></p>
		<br>
		</details></label>

		<br>
				<a id="has_code" href="#">У меня уже есть пароль доступа</a>
    </form>

    <form class="form code" style="display: none" name="sendin" action="$(link-login-only)" method="post">
		<!--$(if error)<label id="error_mess" style="color:red;">$(error)</label>$(endif)<br>-->
		<label for="instr">В течение 1-2 минут Вам придет<br>цифровой пароль с номера <strong>+79533044398</strong></label><br>
        <label for="code">Введите полученный пароль</label>
        <div class="input_group">
            <input type="hidden" name="username" id="username2">
            <input type="hidden" name="password" id="password">
            <input type="text" id="code" maxlength="4" placeholder="****">
			<input type="hidden" name="popup" value="true" />
        </div>
        <br>
		<small>Система вновь запросит ввод пароля, если не подключаться к сети в течение 3 дней.</small>
        <br>
		<br>
        <input type="submit" class="btn disabled" value="Далее">
		<br>
		<small id="timer"></small>
		<!--<br>
		<input type="submit" name="send_again" class="btn send_again" style="display:none" value="Выслать пароль повторно">-->
		<br>
		<label><details class="send_again" style="display:none">
			<summary style="cursor:pointer"><strong>Не приходит СМС?</strong></summary>
			<br><br>Если ответная СМС при регистрации не приходит,<br><a id="forgot_code2" href="#">вернитесь к началу регистрации</a>, поставьте<br>чек бокс "отправить копию пароля администратору" и<br>обратитесь в отдел НОО, либо к администратору гостиницы,<br>если вы проживаете в гостинице КНЦ РАН.
		</details></label>
		<br>
    </form>

    <form class="form already" style="display: none" name="sendin" action="" method="post">
        <label for="login2">Введите Ваш номер телефона</label>
        <br>
        <div class="input_group tel">
            <input type="text" id="login2" placeholder="+X-(XXX)-XXX-XX-XX">
        </div>
        <label for="code">Введите пароль доступа</label>
        <br>
        <div class="input_group">
            <input type="hidden" name="username" id="username3">
            <input type="hidden" name="password" id="password2">
            <input type="text" id="code2" maxlength="4" placeholder="пароль">
			<input type="hidden" name="popup" value="true" />
        </div>
		<br>
        <input type="submit" class="btn disabled" value="Далее">
				<br>
				<a id="forgot_code" href="#">Я забыл пароль доступа</a>
    </form>
	<br>
    <label id="modal_trigger" for="modal-trigger">Авторизуясь, Вы принимаете Правила<br>доступа в сеть Интернет</label>
	<br>
	<div id="copyright"><small><a href="https://www.ksc.ru">©2020-<span id="date"/> ФИЦ КНЦ РАН Wi-Fi</a> | <a href="https://mikrotik.com/software">Powered by MikroTik RouterOS</a></small></div>
</div>
<div class="modal">
    <input id="modal-trigger" class="checkbox" type="checkbox">
    <div class="modal-overlay">
        <label for="modal-trigger" class="o-close"></label>
        <div class="modal-wrap">
		   <label for="modal-trigger" class="close">&#10006;</label>
            <h1 style="text-align: center;">П Р А В И Л А</h1>
<p style="text-align: center;"><strong> пользования доступом в сеть Интернет </strong></p>
<p>1. При пользовании гостевого Wi-Fi пользователям запрещается:</p>
<p>1.1. Ограничивать доступ других пользователей или препятствовать другим Пользователям при использовании гостевого Wi-Fi; </p>
<p>1.2. Производить "веерную" (массовую) рассылку рекламных, информационных и других материалов другим пользователям сети Интернет, кроме случаев, когда адресаты согласны получить эти материалы.</p>
<p>1.3. Производить самовольное (несанкционированное) проникновение в любые технологические компоненты (узлы), программы, базы данных и иные составляющие элементы ИВС ФИЦ КНЦ РАН, имея в виду действия, совершение или покушение на совершение которых предусматривает установленную в РФ уголовную ответственность за такие деяния, как гл. 21 УК РФ "Преступления против собственности" ст. 159 "Мошенничество"; гл. 28 УК РФ "Преступления в сфере компьютерной информации": ст. 272 "Неправомерный доступ к компьютерной информации", ст. 273 "Создание, использование и распространение вредоносных программ для ЭВМ", ст. 274 "Нарушение правил эксплуатации ЭВМ, системы ЭВМ или их сети".</p>
<p>1.4. Посылать или делать доступной по сети Интернет любую информацию, распространение которой, так или иначе, противоречит российскому или международному праву.</p>
<p>1.5. Передавать любую информацию или программное обеспечение, которое содержит в себе вирусы или другие вредоносные компоненты.</p>
<p>1.6. Посылать, передавать, воспроизводить, предоставлять или в любом виде использовать в коммерческих целях информацию, программное обеспечение, или другие материалы, полностью или частично, полученные посредством гостевого доступа в сеть Интернет (если это явно не разрешено поставщиком подобной информации, программного обеспечения или другой продукции).</p>
<p>1.7. Посылать, передавать, воспроизводить или распространять любым способом полученные посредством предоставленного гостевого доступа в сеть Интернет программное обеспечение или другие материалы, полностью или частично, защищенные авторскими или другими правами, без разрешения владельца или законного правообладателя.</p>
<p>1.8. Нарушать правила использования любых ресурсов сети Интернет, установленные ФИЦ КНЦ РАН и/или владельцами этих ресурсов.</p>
<p>1.9. Использовать программное обеспечение, производящее автоматическую авторизацию Пользователя в целях получения гостевого доступа в сеть Интернет, за исключением программного обеспечения, предоставленного либо одобренного ФИЦ КНЦ РАН.</P>
<P>1.10. Если Пользователь не согласен с правилами использования какого-либо ресурса, он должен немедленно отказаться от его использования.</p>
<P>2. ФИЦ КНЦ РАН не будет преднамеренно просматривать или разглашать любые частные сообщения электронной почты (за исключением случаев, предусмотренных законом).</P>
<P>3. ФИЦ КНЦ РАН не обязан следить за содержанием информации, распространяемой посредством Услуг. Однако Пользователь принимает условие, что ФИЦ КНЦ РАН имеет право отслеживать проходящую через Услуги информацию и раскрывать любые сведения, если это необходимо в соответствии с законом, требованиями уполномоченных государственных учреждений, для нормального функционирования Услуг, либо для защиты ФИЦ КНЦ РАН и иных Пользователей (третьих лиц), чьи законные права и интересы были или могут быть нарушены.</P>
<P>4. ФИЦ КНЦ РАН оставляет за собой право отказать в пересылке или удалять со своих серверов любую информацию или материалы полностью или частично, если они, исключительно с точки зрения ФИЦ КНЦ РАН, являются неприемлемыми, нежелательными или нарушают настоящее Положение.</P>
<center>***</center>
<p>С полным текстом Положения "Об использовании сети гостевого беспроводного доступа в Интернет в ФИЦ КНЦ РАН" можно ознакомиться <a href="https://cloud.ksc.ru/s/3CwzQneKpGtapsc">здесь</a>.</p>
<p>С полным текстом Приказа "Об утверждении и введении в действие Положения "Об использовании сети гостевого беспроводного доступа в Интернет в ФИЦ КНЦ РАН"" можно ознакомиться <a href="https://cloud.ksc.ru/s/aiKfFxJkGPW428D">здесь</a>.</p>


        </div>
    </div>
</div
</body>
</html>

File: /hotspot\logout.html
<html>
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0" />   
<meta http-equiv="pragma" content="no-cache">
<meta http-equiv="expires" content="-1">
<title>Точка доступа в сеть Интернет - Выход</title>
<link rel="stylesheet" href="css/style.css">
<script>
    function openLogin() {
	if (window.name != 'hotspot_logout') return true;
	open('$(link-login)', '_blank', '');
	window.close();
	return false;
    }
</script>
</head>

<body>
    <div class="ie-fixMinHeight">
        <div class="main">
            <div class="wrap">
                <h1>Вы вышли!</h1> 
                <table>  
                    <tr><td>Логин</td><td>$(username)</td></tr>
                    <tr><td>IP адрес</td><td>$(ip)</td></tr>
                    <tr><td>MAC адрес</td><td>$(mac)</td></tr>
                    <tr><td>Время сессии</td><td>$(uptime)</td></tr>
                    $(if session-time-left)
                    <tr><td>Осталось времени</td><td>$(session-time-left)</td></tr>
                    $(endif)
                    <tr><td>Передано/получено байт:</td><td>$(bytes-in-nice) / $(bytes-out-nice)</td></tr>
                </table>


                <form action="$(link-login)" name="login" onSubmit="return openLogin()">
                <input type="submit" value="Войти">
                </form>
            </div>
        </div>
    </div>

</body>
</html>


File: /hotspot\radvert.html
<html>
<head>
<meta http-equiv="refresh" content="2; url=$(link-orig)">
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0" />   
<meta http-equiv="pragma" content="no-cache">
<meta http-equiv="expires" content="-1">
<title>Точка доступа в сеть Интернет - Реклама</title>
<link rel="stylesheet" href="css/style.css">
<script>

    var popup = '';
    function openOrig() {
	if (window.focus) popup.focus();
	location.href = unescape('$(link-orig-esc)');
    }
    function openAd() {
	location.href = unescape('$(link-redirect-esc)');
    }
    function openAdvert() {
	if (window.name != 'hotspot_advert') {
		popup = open('$(link-redirect)', 'hotspot_advert', '');
		setTimeout("openOrig()", 1000);
		return;
	}
	setTimeout("openAd()", 1000);
    }
</script>
</head>
<body onLoad="openAdvert()">
    <div class="ie-fixMinHeight">
        <div class="main">
            <div class="wrap">
                <h1>Реклама</h1>
                <p class="info">Если ничего не происходит откройте <a href="$(link-redirect)" target="hotspot_advert">рекламу</a> самостоятельно.</p>
            </div>
        </div>
    </div>
</body>
</html>


File: /hotspot\redirect.html
$(if http-status == 302)Hotspot redirect$(endif)
$(if http-header == "Location")$(link-redirect)$(endif)
<html>
<head>
<title>...</title>
<meta http-equiv="refresh" content="0; url=$(link-redirect)">
<meta http-equiv="pragma" content="no-cache">
<meta http-equiv="expires" content="-1">
</head>
<body>
</body>
</html>


File: /hotspot\result.html
<!doctype html>
<html lang="en">
  <head>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

    <!-- Bootstrap CSS -->
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.2.1/css/bootstrap.min.css" integrity="sha384-GJzZqFGwb1QTTN6wy59ffF1BuGJpLSa9DkKMp0DgiMDm4iYMj70gZWKYbI706tWS" crossorigin="anonymous">

    <style>
      .bg-black { background-color:#000; }
      a { font-weight:bold; }
    </style>

    <title>AsbraSMS</title>
  </head>

  <nav class="navbar navbar-dark bg-dark mb-5">
    <div class='container'>
      <a class="navbar-brand" href="/index.php">Asbra<b class='text-primary'>SMS</b></a>
      <button class="navbar-toggler border-0" type="button" data-toggle="collapse" data-target="#navbarNavAltMarkup" aria-controls="navbarNavAltMarkup" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarNavAltMarkup">
        <div class="navbar-nav">
          <a class="nav-item nav-link active" href="https://xn--1ca.se">Author</a>
          <a class="nav-item nav-link active" href="/index.php">Home <span class="sr-only">(current)</span></a>
        </div>
      </div>
    </div>
  </nav>

  <body class='bg-black text-light'>

    <div class='container'>

      <div class='row mb-4'>
        <div class='col-lg-6 mb-3'>

          <div class='card card-body bg-dark text-light'>
            <h3 class='mb-3'>Compose your message</h3>
            <form method=get>
              <div class="form-group">
                <label for="inputPhone">Mobile Phone Number</label>
                <input name="phone" value="79086051495" type="text" class="form-control" id="inputPhone" aria-describedby="phoneHelp" placeholder="Phone number">
                <small id="phoneHelp" class="form-text text-muted">Dont forget country code (+46)</small>
              </div>
              <div class="form-group">
                <label for="inputSms">SMS Message</label>
                <input name="message" value="   WiFi: 12345   ,       3 .  ,   " type="text" class="form-control" id="inputSms" placeholder="SMS Message">
              </div>
              <button type="submit" class="btn btn-primary">Submit</button>
            </form>
          </div>

        </div>
        <div class='col-lg-6 mb-3'>

                        <div class='card card-body bg-warning text-light mb-4'>
              <h3>Sending...</h3>
                                <pre>To: 79086051495

   WiFi: 12345   ,       3 .  ,   </pre>
                
              </div>
                  </div>
      </div> <!-- /row -->

      <div class='row'>

        <div class='col-lg-6 mb-3'>
          <div class='card card-body bg-dark text-light'>
          <h4>Sent</h4>
            <table class='table table-striped table-dark table-sm'><tr><td><a href='smsd/sent/200905_022010.txt'>200905_022010.txt</a></td><td><div class='float-right'>2020-09-05 02:20:19</div></td></tr><tr><td><a href='smsd/sent/200905_021658.txt'>200905_021658.txt</a></td><td><div class='float-right'>2020-09-05 02:17:08</div></td></tr><tr><td><a href='smsd/sent/200905_015810.txt'>200905_015810.txt</a></td><td><div class='float-right'>2020-09-05 01:58:21</div></td></tr><tr><td><a href='smsd/sent/200905_015513.txt'>200905_015513.txt</a></td><td><div class='float-right'>2020-09-05 01:55:20</div></td></tr><tr><td><a href='smsd/sent/200905_013850.txt'>200905_013850.txt</a></td><td><div class='float-right'>2020-09-05 01:39:05</div></td></tr><tr><td><a href='smsd/sent/200905_005400.txt'>200905_005400.txt</a></td><td><div class='float-right'>2020-09-05 00:54:09</div></td></tr><tr><td><a href='smsd/sent/200904_190806.txt'>200904_190806.txt</a></td><td><div class='float-right'>2020-09-04 19:08:20</div></td></tr><tr><td><a href='smsd/sent/200904_190406.txt'>200904_190406.txt</a></td><td><div class='float-right'>2020-09-04 19:04:19</div></td></tr><tr><td><a href='smsd/sent/200904_185206.txt'>200904_185206.txt</a></td><td><div class='float-right'>2020-09-04 18:52:18</div></td></tr><tr><td><a href='smsd/sent/200904_183906.txt'>200904_183906.txt</a></td><td><div class='float-right'>2020-09-04 18:39:17</div></td></tr><tr><td><a href='smsd/sent/200904_183506.txt'>200904_183506.txt</a></td><td><div class='float-right'>2020-09-04 18:35:18</div></td></tr><tr><td><a href='smsd/sent/200904_174206.txt'>200904_174206.txt</a></td><td><div class='float-right'>2020-09-04 17:42:17</div></td></tr><tr><td><a href='smsd/sent/200904_161906.txt'>200904_161906.txt</a></td><td><div class='float-right'>2020-09-04 16:19:15</div></td></tr><tr><td><a href='smsd/sent/200904_161005.txt'>200904_161005.txt</a></td><td><div class='float-right'>2020-09-04 16:10:14</div></td></tr><tr><td><a href='smsd/sent/200904_154104.txt'>200904_154104.txt</a></td><td><div class='float-right'>2020-09-04 15:41:13</div></td></tr><tr><td><a href='smsd/sent/200904_134647.txt'>200904_134647.txt</a></td><td><div class='float-right'>2020-09-04 13:47:00</div></td></tr><tr><td><a href='smsd/sent/200904_134422.txt'>200904_134422.txt</a></td><td><div class='float-right'>2020-09-04 13:44:29</div></td></tr><tr><td><a href='smsd/sent/200904_133211.txt'>200904_133211.txt</a></td><td><div class='float-right'>2020-09-04 13:32:18</div></td></tr><tr><td><a href='smsd/sent/200904_133125.txt'>200904_133125.txt</a></td><td><div class='float-right'>2020-09-04 13:31:37</div></td></tr><tr><td><a href='smsd/sent/200904_132939.txt'>200904_132939.txt</a></td><td><div class='float-right'>2020-09-04 13:29:46</div></td></tr><tr><td><a href='smsd/sent/200904_132739.txt'>200904_132739.txt</a></td><td><div class='float-right'>2020-09-04 13:27:46</div></td></tr><tr><td><a href='smsd/sent/200904_132217.txt'>200904_132217.txt</a></td><td><div class='float-right'>2020-09-04 13:22:24</div></td></tr><tr><td><a href='smsd/sent/200904_131913.txt'>200904_131913.txt</a></td><td><div class='float-right'>2020-09-04 13:19:23</div></td></tr></table>          </div>
        </div>

        <div class='col-lg-6 mb-3'>
          <div class='card card-body bg-dark text-light'>
          <h4>incoming</h4>
            <table class='table table-striped table-dark table-sm'><tr><td><a href='smsd/incoming/GSM1.zB6vyN'>GSM1.zB6vyN</a></td><td><div class='float-right'>2020-09-02 14:41:11</div></td></tr></table>          </div>
        </div>

        <div class='col-lg-12 mb-3'>
          <div class='card card-body bg-danger text-light'>
          <h4>Failed</h4>
            <table class='table table-striped table-dark table-sm'><tr><td><a href='smsd/failed/200905_022743.txt'>200905_022743.txt</a></td><td><div class='float-right'>2020-09-05 02:27:44</div></td></tr><tr><td><a href='smsd/failed/200905_022404.txt'>200905_022404.txt</a></td><td><div class='float-right'>2020-09-05 02:24:14</div></td></tr><tr><td><a href='smsd/failed/200905_022257.txt'>200905_022257.txt</a></td><td><div class='float-right'>2020-09-05 02:23:03</div></td></tr><tr><td><a href='smsd/failed/200905_021405.txt'>200905_021405.txt</a></td><td><div class='float-right'>2020-09-05 02:14:10</div></td></tr><tr><td><a href='smsd/failed/200905_015224.txt'>200905_015224.txt</a></td><td><div class='float-right'>2020-09-05 01:52:35</div></td></tr><tr><td><a href='smsd/failed/200905_014823.txt'>200905_014823.txt</a></td><td><div class='float-right'>2020-09-05 01:48:34</div></td></tr><tr><td><a href='smsd/failed/200905_014725.txt'>200905_014725.txt</a></td><td><div class='float-right'>2020-09-05 01:47:32</div></td></tr><tr><td><a href='smsd/failed/200905_014637.txt'>200905_014637.txt</a></td><td><div class='float-right'>2020-09-05 01:46:41</div></td></tr><tr><td><a href='smsd/failed/200905_014303.txt'>200905_014303.txt</a></td><td><div class='float-right'>2020-09-05 01:43:11</div></td></tr><tr><td><a href='smsd/failed/200905_013446.txt'>200905_013446.txt</a></td><td><div class='float-right'>2020-09-05 01:34:47</div></td></tr><tr><td><a href='smsd/failed/200905_012815.txt'>200905_012815.txt</a></td><td><div class='float-right'>2020-09-05 01:28:25</div></td></tr><tr><td><a href='smsd/failed/20200905-01:14:19.043884624.txt'>20200905-01:14:19.043884624.txt</a></td><td><div class='float-right'>2020-09-05 01:14:22</div></td></tr><tr><td><a href='smsd/failed/200905_011145.txt'>200905_011145.txt</a></td><td><div class='float-right'>2020-09-05 01:11:52</div></td></tr><tr><td><a href='smsd/failed/200905_010253.txt'>200905_010253.txt</a></td><td><div class='float-right'>2020-09-05 01:02:57</div></td></tr><tr><td><a href='smsd/failed/200905_005604.txt'>200905_005604.txt</a></td><td><div class='float-right'>2020-09-05 00:56:06</div></td></tr><tr><td><a href='smsd/failed/200905_005213.txt'>200905_005213.txt</a></td><td><div class='float-right'>2020-09-05 00:52:24</div></td></tr><tr><td><a href='smsd/failed/200904_133423.txt'>200904_133423.txt</a></td><td><div class='float-right'>2020-09-04 13:34:25</div></td></tr></table>          </div>
        </div>
      </div>
    </div>

    <!-- Optional JavaScript -->
    <!-- jQuery first, then Popper.js, then Bootstrap JS -->
    <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.6/umd/popper.min.js" integrity="sha384-wHAiFfRlMFy6i5SRaxvfOCifBUQy1xHdJ/yoi7FRNXMRBu5WHdZYu1hA6ZOblgut" crossorigin="anonymous"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.2.1/js/bootstrap.min.js" integrity="sha384-B0UglyR+jN6CkvvICOB2joaf5I4l3gm9GU6Hc1og6Ls7i6U/mkkaduKaBhlAXv9k" crossorigin="anonymous"></script>
  </body>
<footer class='text-center py-5'>
  <small>
    <strong>AsbraSMS Copyright © 2019 ASBRA AB, <j@asbra.nu></strong><br>
    <hr style="border-top:1px solid #fff; max-width:250px;">
    This is free software, and you are welcome to redistribute it
    under certain conditions.<br>
    See <a href='https://www.gnu.org/licenses/gpl-3.0.en.html'>GNU GPL v3</a> for more information.
  </small>
</footer>
</html>



File: /hotspot\rlogin.html
$(if http-status == 302)Hotspot login required$(endif)
$(if http-header == "Location")$(link-redirect)$(endif)
<html>
<!--
<?xml version="1.0" encoding="UTF-8"?>
  <WISPAccessGatewayParam
  xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
  xsi:noNamespaceSchemaLocation="http://$(hostname)/xml/WISPAccessGatewayParam.xsd">
    <Redirect>
	<AccessProcedure>1.0</AccessProcedure>
	<AccessLocation>$(location-id)</AccessLocation>
	<LocationName>$(location-name)</LocationName>
	<LoginURL>$(link-login-only)?target=xml</LoginURL>
	<MessageType>100</MessageType>
	<ResponseCode>0</ResponseCode>
    </Redirect>
  </WISPAccessGatewayParam>
-->
<head>
<title>...</title>
<meta http-equiv="refresh" content="0; url=$(link-redirect)">
<meta http-equiv="pragma" content="no-cache">
<meta http-equiv="expires" content="-1">
</head>
<body>
</body>
</html>


File: /hotspot\status.html
<html>
<head>
$(if refresh-timeout)
<meta http-equiv="refresh" content="$(refresh-timeout-secs)">
$(endif)
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0" />   
<meta http-equiv="pragma" content="no-cache">
<meta http-equiv="expires" content="-1">
<title>Точка доступа в сеть Интернет - Статистика</title>
<link rel="stylesheet" href="css/style.css">
<script>

$(if advert-pending == 'yes')
    var popup = '';
    function focusAdvert() {
	if (window.focus) popup.focus();
    }
    function openAdvert() {
	popup = open('$(link-advert)', 'hotspot_advert', '');
	setTimeout("focusAdvert()", 1000);
    }
$(endif)
    function openLogout() {
	if (window.name != 'hotspot_status') return true;
        open('$(link-logout)', 'hotspot_logout', 'toolbar=0,location=0,directories=0,status=0,menubars=0,resizable=1,width=280,height=250');
	window.close();
	return false;
    }
</script>
    
</head>
<body $(if advert-pending == 'yes') onLoad="openAdvert()" $(endif)>
    <div class="ie-fixMinHeight">
        <div class="main">
            <div class="wrap">
                $(if login-by == 'trial')
                    <h1>Здравствуйте, trial user!</h1>
                $(elif login-by != 'mac')
                    <h1>Здравствуйте, $(username)!</h1>
                $(endif)                

                <form action="$(link-logout)" name="logout" onSubmit="return openLogout()">
                    <table>
                        <tr><td>Ваш IP адрес</td><td>$(ip)</td></tr>
                        <tr><td>Передано/получено байт</td><td>$(bytes-in-nice) / $(bytes-out-nice)</td></tr>
                    $(if session-time-left)
                        <tr><td>Подключено / таймаут сессии </td><td>$(uptime) / $(session-time-left)</td></tr>
                    $(else)
                        <tr><td>Подключено</td><td>$(uptime)</td></tr>
                    $(endif)
                    $(if blocked == 'yes')
                        <tr><td>Статус</td><td>
                    <a href="$(link-advert)" target="hotspot_advert">Advertisement required</a></td>
                        </tr>
                    $(elif refresh-timeout)
                        <tr><td>Обновление статуса каждые</td><td>$(refresh-timeout)</td></tr>
                    $(endif)
                        </table>
                    $(if login-by-mac != 'yes')
                    <!-- user manager link. if user manager resides on other router, replace $(hostname) by its address
                    <button onclick="document.location='http://$(hostname)/user?subs='; return false;">status</button>
                    <!-- end of user manager link -->
                    <input type="submit" value="Выйти">
                    $(endif)
                </form>
            </div>
        </div>
    </div>
</body>
</html>

File: /LICENSE
                                 Apache License
                           Version 2.0, January 2004
                        http://www.apache.org/licenses/

   TERMS AND CONDITIONS FOR USE, REPRODUCTION, AND DISTRIBUTION

   1. Definitions.

      "License" shall mean the terms and conditions for use, reproduction,
      and distribution as defined by Sections 1 through 9 of this document.

      "Licensor" shall mean the copyright owner or entity authorized by
      the copyright owner that is granting the License.

      "Legal Entity" shall mean the union of the acting entity and all
      other entities that control, are controlled by, or are under common
      control with that entity. For the purposes of this definition,
      "control" means (i) the power, direct or indirect, to cause the
      direction or management of such entity, whether by contract or
      otherwise, or (ii) ownership of fifty percent (50%) or more of the
      outstanding shares, or (iii) beneficial ownership of such entity.

      "You" (or "Your") shall mean an individual or Legal Entity
      exercising permissions granted by this License.

      "Source" form shall mean the preferred form for making modifications,
      including but not limited to software source code, documentation
      source, and configuration files.

      "Object" form shall mean any form resulting from mechanical
      transformation or translation of a Source form, including but
      not limited to compiled object code, generated documentation,
      and conversions to other media types.

      "Work" shall mean the work of authorship, whether in Source or
      Object form, made available under the License, as indicated by a
      copyright notice that is included in or attached to the work
      (an example is provided in the Appendix below).

      "Derivative Works" shall mean any work, whether in Source or Object
      form, that is based on (or derived from) the Work and for which the
      editorial revisions, annotations, elaborations, or other modifications
      represent, as a whole, an original work of authorship. For the purposes
      of this License, Derivative Works shall not include works that remain
      separable from, or merely link (or bind by name) to the interfaces of,
      the Work and Derivative Works thereof.

      "Contribution" shall mean any work of authorship, including
      the original version of the Work and any modifications or additions
      to that Work or Derivative Works thereof, that is intentionally
      submitted to Licensor for inclusion in the Work by the copyright owner
      or by an individual or Legal Entity authorized to submit on behalf of
      the copyright owner. For the purposes of this definition, "submitted"
      means any form of electronic, verbal, or written communication sent
      to the Licensor or its representatives, including but not limited to
      communication on electronic mailing lists, source code control systems,
      and issue tracking systems that are managed by, or on behalf of, the
      Licensor for the purpose of discussing and improving the Work, but
      excluding communication that is conspicuously marked or otherwise
      designated in writing by the copyright owner as "Not a Contribution."

      "Contributor" shall mean Licensor and any individual or Legal Entity
      on behalf of whom a Contribution has been received by Licensor and
      subsequently incorporated within the Work.

   2. Grant of Copyright License. Subject to the terms and conditions of
      this License, each Contributor hereby grants to You a perpetual,
      worldwide, non-exclusive, no-charge, royalty-free, irrevocable
      copyright license to reproduce, prepare Derivative Works of,
      publicly display, publicly perform, sublicense, and distribute the
      Work and such Derivative Works in Source or Object form.

   3. Grant of Patent License. Subject to the terms and conditions of
      this License, each Contributor hereby grants to You a perpetual,
      worldwide, non-exclusive, no-charge, royalty-free, irrevocable
      (except as stated in this section) patent license to make, have made,
      use, offer to sell, sell, import, and otherwise transfer the Work,
      where such license applies only to those patent claims licensable
      by such Contributor that are necessarily infringed by their
      Contribution(s) alone or by combination of their Contribution(s)
      with the Work to which such Contribution(s) was submitted. If You
      institute patent litigation against any entity (including a
      cross-claim or counterclaim in a lawsuit) alleging that the Work
      or a Contribution incorporated within the Work constitutes direct
      or contributory patent infringement, then any patent licenses
      granted to You under this License for that Work shall terminate
      as of the date such litigation is filed.

   4. Redistribution. You may reproduce and distribute copies of the
      Work or Derivative Works thereof in any medium, with or without
      modifications, and in Source or Object form, provided that You
      meet the following conditions:

      (a) You must give any other recipients of the Work or
          Derivative Works a copy of this License; and

      (b) You must cause any modified files to carry prominent notices
          stating that You changed the files; and

      (c) You must retain, in the Source form of any Derivative Works
          that You distribute, all copyright, patent, trademark, and
          attribution notices from the Source form of the Work,
          excluding those notices that do not pertain to any part of
          the Derivative Works; and

      (d) If the Work includes a "NOTICE" text file as part of its
          distribution, then any Derivative Works that You distribute must
          include a readable copy of the attribution notices contained
          within such NOTICE file, excluding those notices that do not
          pertain to any part of the Derivative Works, in at least one
          of the following places: within a NOTICE text file distributed
          as part of the Derivative Works; within the Source form or
          documentation, if provided along with the Derivative Works; or,
          within a display generated by the Derivative Works, if and
          wherever such third-party notices normally appear. The contents
          of the NOTICE file are for informational purposes only and
          do not modify the License. You may add Your own attribution
          notices within Derivative Works that You distribute, alongside
          or as an addendum to the NOTICE text from the Work, provided
          that such additional attribution notices cannot be construed
          as modifying the License.

      You may add Your own copyright statement to Your modifications and
      may provide additional or different license terms and conditions
      for use, reproduction, or distribution of Your modifications, or
      for any such Derivative Works as a whole, provided Your use,
      reproduction, and distribution of the Work otherwise complies with
      the conditions stated in this License.

   5. Submission of Contributions. Unless You explicitly state otherwise,
      any Contribution intentionally submitted for inclusion in the Work
      by You to the Licensor shall be under the terms and conditions of
      this License, without any additional terms or conditions.
      Notwithstanding the above, nothing herein shall supersede or modify
      the terms of any separate license agreement you may have executed
      with Licensor regarding such Contributions.

   6. Trademarks. This License does not grant permission to use the trade
      names, trademarks, service marks, or product names of the Licensor,
      except as required for reasonable and customary use in describing the
      origin of the Work and reproducing the content of the NOTICE file.

   7. Disclaimer of Warranty. Unless required by applicable law or
      agreed to in writing, Licensor provides the Work (and each
      Contributor provides its Contributions) on an "AS IS" BASIS,
      WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
      implied, including, without limitation, any warranties or conditions
      of TITLE, NON-INFRINGEMENT, MERCHANTABILITY, or FITNESS FOR A
      PARTICULAR PURPOSE. You are solely responsible for determining the
      appropriateness of using or redistributing the Work and assume any
      risks associated with Your exercise of permissions under this License.

   8. Limitation of Liability. In no event and under no legal theory,
      whether in tort (including negligence), contract, or otherwise,
      unless required by applicable law (such as deliberate and grossly
      negligent acts) or agreed to in writing, shall any Contributor be
      liable to You for damages, including any direct, indirect, special,
      incidental, or consequential damages of any character arising as a
      result of this License or out of the use or inability to use the
      Work (including but not limited to damages for loss of goodwill,
      work stoppage, computer failure or malfunction, or any and all
      other commercial damages or losses), even if such Contributor
      has been advised of the possibility of such damages.

   9. Accepting Warranty or Additional Liability. While redistributing
      the Work or Derivative Works thereof, You may choose to offer,
      and charge a fee for, acceptance of support, warranty, indemnity,
      or other liability obligations and/or rights consistent with this
      License. However, in accepting such obligations, You may act only
      on Your own behalf and on Your sole responsibility, not on behalf
      of any other Contributor, and only if You agree to indemnify,
      defend, and hold each Contributor harmless for any liability
      incurred by, or claims asserted against, such Contributor by reason
      of your accepting any such warranty or additional liability.

   END OF TERMS AND CONDITIONS

   APPENDIX: How to apply the Apache License to your work.

      To apply the Apache License to your work, attach the following
      boilerplate notice, with the fields enclosed by brackets "[]"
      replaced with your own identifying information. (Don't include
      the brackets!)  The text should be enclosed in the appropriate
      comment syntax for the file format. We also recommend that a
      file or class name and description of purpose be included on the
      same "printed page" as the copyright notice for easier
      identification within third-party archives.

   Copyright [yyyy] [name of copyright owner]

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.


File: /Log-in script on hotspot profile.txt
# Edit in /ip hotspot user profile edit default on-login 

:local smtpserv [:resolve "mail.com"];

:local Eaccount "sdg@yyy.com";

:local pass "xxxx";

:local nas [/system identity get name];

:local today [/system clock get date];

:local time1 [/system clock get time ];

:local ipuser [/ip hotspot active get [find user=$user] address];

:local usermac [/ip hotspot active get [find user=$user] mac-address];

:local userphone [/ip hotspot active get [find user=$user] user];

:local userphonelength [:len $userphone];

:set $userphone [:pick $userphone 1 $userphonelength];

:put $userphone;

:put $today;

:put $time1;

:local hour [:pick $time1 0 2]; 

:local min [:pick $time1 3 5]; 

:local sec [:pick $time1 6 8];

:set $time1 [:put ({hour} . {min} . {sec})];

:local mac1 [:pick $usermac 0 2];

:local mac2 [:pick $usermac 3 5];

:local mac3 [:pick $usermac 6 8];

:local mac4 [:pick $usermac 9 11];

:local mac5 [:pick $usermac 12 14];

:local mac6 [:pick $usermac 15 17];

:set $usermac [:put ({mac1} . {mac2} . {mac3} . {mac4} . {mac5} . {mac6})];

:put $time1;

/ip firewall address-list add list=$today address="log-in.$time1.$userphone.$usermac.$ipuser";

do {/tool e-mail send from=df@kjhv.com to="jkgdf@jsudhf.com" server=$smtpserv port=587 user=$Eaccount password=$pass start-tls=yes subject="Login number: $user on $nas" body="Login number: $user mac-address: $usermac time: $time1 ip-address: $ipuser"} on-error={};


File: /Log-out script on hotspot profile.txt
# Edit in /ip hotspot user profile edit default on-logout

:local smtpserv [:resolve "kjdgf.com"];

:local Eaccount "asjkhgdsf@jkfg.com";

:local pass "adfgljja";

:local nas [/system identity get name];

:local today [/system clock get date];

:local time1 [/system clock get time ];

:local userphone $user;

:local userphonelength [:len $userphone];

:set $userphone [:pick $userphone 1 $userphonelength];

:put $userphone;

:put $today;

:put $time1;

:local hour [:pick $time1 0 2]; 

:local min [:pick $time1 3 5];

:local sec [:pick $time1 6 8];

:set $time1 [:put ({hour} . {min} . {sec})]; 

:put $time1;

/ip firewall address-list add list=$today address="log-out.$time1.$userphone";

/tool e-mail send from=jahsfd@khsdf.com to="dsfjkgfh@jghsdf.com" server=$smtpserv port=587 user=$Eaccount password=$pass start-tls=yes subject="Logout number: $user on $nas" body="Logout number: $user time: $time1";


File: /README.md
# mikrotik-wifi-hotspot-portal
Login portal for Mikrotik hotspot with SMS auth


File: /script-KSC.txt
#Search number in log hotspot

  :local smtpserv [:resolve "mail.yyy.com"];

  :local Eaccount "xxx@yyy.com";

  :local passwd "xxxxx";

 :foreach line in=[/log find buffer=hotspot message~"login failed: no more sessions are allowed"] do={
	:do {:local content [/log get $line message];
	:put $content;  
  :local pos1 [:find $content " (" 0];
  :put $pos1;
  :if ($pos1 != " ") do={ 
   :local uname ""; 
   :local uname7 "";
   :local uname8 "";
   :local uname9 "";
   :local phone ""; 
   :local mess "";
   :local mess1 "Достигнут+лимит+подключений+на+логин+";
   :local mess2 ".+Если+сессии+заняты+не+вашими+устройствами,+то+запросите+код+заново+и+авторизуйтесь+повторно.+Если+данное+сообщение+приходит+и+после+этого,+обратитесь+в+отдел+НОО.+С+уважением,+ФИЦ+КНЦ+РАН";
    :set uname [:pick $content ($pos1-12) ($pos1-0)];
    :put $uname;
	:set mess ($mess1 . $uname . $mess2);
	:put $mess;
	##SMS
	do {/tool fetch mode=http url="http://sms.ksc.loc/api.php"  http-method=post  http-data="phone=$uname&message=$mess" keep-result=no} on-error={};
	#Email
    do {/tool e-mail send from=router@ksc.ru to=root@ksc.ru server=$smtpserv port=25 user=$Eaccount password=$passwd subject="У пользователя $uname лимит сессий исчерпан" body="У пользователя Wi-Fi $uname исчерпан лимит сессий."} on-error={};
  }
  # Clear hostpot log

/system logging action set hotspot memory-lines=1;
/system logging action set hotspot memory-lines=1000;
  }
  }

:foreach line in=[/log find buffer=hotspot message~"trying to log in by http-pap"] do={
#:foreach line in=[/log find buffer=hotspot message~"login failed: invalid username or password"] do={
 :do {:local content [/log get $line message];
  :put $content;  
  :local pos2 [:find $content "_email"];
  :put $pos2;
  :local pos1 [:find $content " (" 0];
  :put $pos1;
  :if ($pos1 != " ") do={ 
   :local uname ""; 
   :local uname7 "";
   :local uname8 "";
   :local uname9 "";
   :local phone ""; 
   :local mess "";
   :local mess1 "Ваш+пароль+от+WiFi:+";
   :local mess2 "+.Он+станет+недействительным,+если+не+подключаться+к+сети+более+3+дней.+Максимальное+количество+устройств+на+логин+2.+С+уважением,+ФИЦ+КНЦ+РАН";
    :set uname [:pick $content ($pos1-12) ($pos1-0)];  
    :put $uname;
    #Password generation 
	:local ruleprefix "random-";
	:put "list rules to void unseen changes";

	/ip firewall filter print without-paging;

	:put "set up password length"
	:local passlen
	if ([:tostr $passlen]="") do={:set passlen 4}

	:put "make passthrough rules if none. according to passlen"
	:for i from=1 to=$passlen do={
		:local coment ($ruleprefix.[:tostr $i])
		if ([/ip firewall filter find comment=$coment]="") do={
			/ip firewall filter add action=passthrough chain=forward place-before=0 random=($i+1) comment=$coment
		}
	}
                :delay 2;
	:put "define char table"
	:global chArray
	if ([:tostr $chArray]="") do={:set chArray 1,2,3,4,5,6,7,8,9,0}

	:put "count letters"
	:local letters ( [:len $chArray ] - 1 )

	:global pass
	:set pass ""
	:put "generate new password"
	:for i from=1 to=$passlen do={
		:local chnum [/ip firewall filter get [find comment=($ruleprefix.[:tostr $i])] packets ]
		if ( chnum > $letters ) do={
			:set chnum ( chnum - $letters * ( chnum / $letters ) )
			# need to reset?
			#/ip firewall filter reset-counters [find comment=($ruleprefix.[:tostr $i])]
		}
		:set pass [:tostr ( $pass . [ :tostr [ :pick $chArray $chnum ] ] ) ]
	}
	/ip firewall filter remove [ find comment~$ruleprefix ]
    # Password generation ends
    :put $pass;
    :set mess ($mess1 . $pass . $mess2);
#     :set mess ("Your+password+is+" . $pass);
 #    :set mess $pass;
    :put $mess;
#    :log info "$mess";

    #Add user to hotspot / user-manager 

    do {/ip hotspot user add name=$uname} on-error={};
    do {/ip hotspot user set password=$pass numbers=[find name=$uname]} on-error={};
    #do {/tool user-manager user add username=$uname password=$pass customer=admin copy-from=test disabled=no phone=$uname;} on-error={};
    #do {/tool user-manager user set password=$pass number=[find username=$uname]} on-error={}; 
    ##SMS.ru
    #do {/tool fetch url="http://sms.ksc.loc/index.php\?phone=$uname&message=$mess" keep-result=no} on-error={};
    do {/tool fetch mode=http url="http://sms.ksc.loc/api.php"  http-method=post  http-data="phone=$uname&message=$mess" keep-result=no} on-error={};
    #do {/tool sms send usb1 phone-number="$uname7" message="login $uname password $pass"} on-error={};
     :if ([:len $pos2] != 0) do={
      :log info "Sending email to administrator!";
     #Email
     do {/tool e-mail send from=xxx@yyy.com to=asf@yyy.com cc=asf2@yyy.com server=$smtpserv port=25 user=$Eaccount password=$passwd subject="=?UTF-8?B?0J3QvtCy0YvQuSDQv9C+0LvRjNC30L7QstCw0YLQtdC70YwgV2ktRmkg0YEg0L3QvtC80LXRgNC+0Lwg0YLQtdC70LXRhNC+0L3QsA==?= $uname\r\nContent-type: text/plain;charset=windows-1251" body=Эздравствуйте!\r\n\r\nу нового пользователя Wi-Fi возникли проблемы с доставкой СМС. Ждите обращения.\r\nЛогин: $uname\r\nПароль: $pass"} on-error={}
    }
    #Email
    #do {/tool e-mail send from=xxx@yyy.com to=asf@yyy.com server=$smtpserv port=25 user=$Eaccount password=$passwd subject="Новый пользователь Wi-Fi с номером телефона $uname" body="Авторизован новый пользователь Wi-Fi.\r\nЛогин: $uname\r\nПароль: $pass"} on-error={};    
  }
# Clear hostpot log

/system logging action set hotspot memory-lines=1;
/system logging action set hotspot memory-lines=1000;
 }
}



