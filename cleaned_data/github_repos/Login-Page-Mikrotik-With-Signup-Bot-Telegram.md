# Repository Information
Name: Login-Page-Mikrotik-With-Signup-Bot-Telegram

# Directory Structure
Directory structure:
└── github_repos/Login-Page-Mikrotik-With-Signup-Bot-Telegram/
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
    │   │       ├── pack-c9058f3dfa3748b17c0ff1e86d724d7c04d31f4f.idx
    │   │       └── pack-c9058f3dfa3748b17c0ff1e86d724d7c04d31f4f.pack
    │   ├── packed-refs
    │   └── refs/
    │       ├── heads/
    │       │   └── master
    │       ├── remotes/
    │       │   └── origin/
    │       │       └── HEAD
    │       └── tags/
    ├── .gitattributes
    ├── alogin.html
    ├── css/
    │   └── custom.css
    ├── error.html
    ├── errors.txt
    ├── font/
    │   ├── nyessid.eot
    │   ├── nyessid.ttf
    │   ├── nyessid.woff
    │   └── nyessid.woff2
    ├── img/
    ├── js/
    │   ├── md5.js
    │   └── signup.js
    ├── login.html
    ├── logout.html
    ├── maintenance.html
    ├── paket.html
    ├── radvert.html
    ├── readme.txt
    ├── redirect.html
    ├── rlogin.html
    ├── status.html
    ├── tos.html
    ├── xml/
    │   ├── alogin.html
    │   ├── error.html
    │   ├── flogout.html
    │   ├── login.html
    │   ├── logout.html
    │   ├── rlogin.html
    │   └── WISPAccessGatewayParam.xsd
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
	url = https://github.com/linuxsidareja/Login-Page-Mikrotik-With-Signup-Bot-Telegram.git
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
0000000000000000000000000000000000000000 11d8c395bad08a2a0d2ea0ca00bf9ca6d830b41e vivek-dodia <vivek.dodia@icloud.com> 1738606304 -0500	clone: from https://github.com/linuxsidareja/Login-Page-Mikrotik-With-Signup-Bot-Telegram.git


File: /.git\logs\refs\heads\master
0000000000000000000000000000000000000000 11d8c395bad08a2a0d2ea0ca00bf9ca6d830b41e vivek-dodia <vivek.dodia@icloud.com> 1738606304 -0500	clone: from https://github.com/linuxsidareja/Login-Page-Mikrotik-With-Signup-Bot-Telegram.git


File: /.git\logs\refs\remotes\origin\HEAD
0000000000000000000000000000000000000000 11d8c395bad08a2a0d2ea0ca00bf9ca6d830b41e vivek-dodia <vivek.dodia@icloud.com> 1738606304 -0500	clone: from https://github.com/linuxsidareja/Login-Page-Mikrotik-With-Signup-Bot-Telegram.git


File: /.git\packed-refs
# pack-refs with: peeled fully-peeled sorted 
11d8c395bad08a2a0d2ea0ca00bf9ca6d830b41e refs/remotes/origin/master


File: /.git\refs\heads\master
11d8c395bad08a2a0d2ea0ca00bf9ca6d830b41e


File: /.git\refs\remotes\origin\HEAD
ref: refs/remotes/origin/master


File: /.gitattributes
# Auto detect text files and perform LF normalization
* text=auto

File: /alogin.html
<html>
	<head>
		<title>@wificorner - redirect</title>
		<meta http-equiv="refresh" content="2; url=$(link-redirect)">
		<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
		<meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1.0, user-scalable=no">
		<meta http-equiv="X-UA-Compatible" content="IE=edge">
		<meta http-equiv="pragma" content="no-cache" />
		<meta http-equiv="expires" content="-1" />
		<link rel="shortcut icon" href="img/corner.png" type="image/x-icon">
		<link rel="icon" href="img/corner.png" type="image/x-icon">
		<link rel="stylesheet" href="css/custom.css">
		<script language="JavaScript">
		<!--
		function startClock() {
		$(if popup == 'true')
		open('$(link-status)', 'hotspot_status', 'toolbar=0,location=0,directories=0,status=0,menubars=0,resizable=1,width=290,height=200');
			$(endif)
			location.href = unescape('$(link-redirect-esc)');
		}
		//-->
		</script>
	</head>
	<body class="bg-img" onLoad="startClock()">
		<table width="100%" height="100%">
			<tr>
				<td align="center" valign="middle" style="font-size: 14px;color:#888888;font-family: Arial;">
					<img style="width: 20px; height: 20px;" src="img/loading.gif">
					<br/><br/>
					Anda berhasil login
					<br><br>
					Jika tidak bisa redirect otomatis silahkan klik <a href="$(link-redirect)">disini</a>
				</td>
			</tr>
		</table>
	</body>
</html>

File: /css\custom.css
body{
margin-top: 20px;
}
.bg-img{
background: url('../img/bg.png');
}
.logo{
margin-top: 20px;
width: 100px;
}
.wrap {
background: rgba(0, 0, 0,0.80);
color:#eee;
-webkit-box-shadow: 0px 35px 44px -22px rgba(0,0,0,0.72);
-moz-box-shadow: 0px 35px 44px -22px rgba(0,0,0,0.72);
box-shadow: 0px 35px 44px -22px #1f181b;
padding: 40px 20px 40px 20px;
border-radius:8px;
margin-top: 20px;
}
.wrap h4{
font-size:16px;
color:#ffffff;
}
.wrap a{
font-weight: bold;
color: #555;
}
.title{
font-size:14px;
color:green;
margin-top: 40px;
margin-bottom: 20px;
}
ol li{
padding-top: 15px;
}
ol ol{
list-style-type: lower-alpha;
padding-left: 15px;
}
.legend{
border-style: none;
border-width: 0;
font-size: 14px;
line-height: 20px;
margin-bottom: 0;
width: auto;
padding: 0 10px;
border: 0;
color:#777777;
text-transform: uppercase;
}
.fieldset{
border-top: 1px solid #bbbbbb;
padding: 10px;
font-weight: bold;
}
.info-user{
position: relative;
top:-10px;
font-size: 12px;
color: #666666;
}
.input-login {
width:87%;
height: 50px;
margin-right:auto;
margin-left:auto;
margin-bottom:10px;
text-align: center;
background: none;
box-shadow: none;
border: 1px solid #bbbbbb;
color: green;
border-radius: 8px;
font-size: 14px;
z-index: 9999;
}
input:-webkit-autofill {
-webkit-box-shadow: inset 0 0 0px 99999px #ffffff !important;
}
.input-login:-ms-input-placeholder {
color: #bbbbbb;
}
.input-login::-moz-placeholder{
color: #bbbbbb;
}
.input-login::-webkit-input-placeholder {
color: #bbbbbb;
}
.input-login:focus{
color: green;
}
.btn{
width: 30%;
margin-top: 20px;
margin-bottom: 10px;
}
.btn:focus{
outline: 0 !important;
}
.error{
width: 87%;
margin: auto;
text-align:center;
}
.p{
color:#555555;
font-size: 13px;
}
.paket{
margin-bottom: 40px;
}
.paket .panel-heading{
height: 40px !important;
}
.paket .panel-heading h3{
font-size: 18px;
padding: 0;
margin-top:0;
}
.paket .panel:hover {
    box-shadow: 0 8px 12px 0 rgba(0,0,0,0.2);
}
.panel-body{
border-bottom: 1px solid #eee;
last-child
}
.panel-body:nth-child(4){
border-bottom: 0px;
}
.bg-panel1{
color:#ffffff;
background-color: #888888 !important;
border-radius: 0;
}
.border-panel1{
border:1px solid #888888 !important;
}
.bg-panel2{
color:#ffffff;
background-color: #e67e22 !important;
border-radius: 0;
}
.border-panel2{
border:1px solid #e67e22 !important;
}
.bg-panel3{
color:#ffffff;
background-color: #2980b9 !important;
border-radius: 0;
}
.border-panel3{
border:1px solid #2980b9 !important;
}
.harga {
font-size: 2.5rem;
font-weight: 300;
}
.masa-aktif {
font-weight: 500;
font-size: 1rem;
}
.masa-aktif::before {
content: '/';
margin-right: 2px;
}
.beli{
min-width: 80px;
margin-top:10px;
}
.check{
font-size: 12px;
color: #888888;
}
.info{
font-size: 13px;
margin: 20px auto 40px auto;
border: 1px solid #ccc;
border-left:5px solid #0097bc;
border-radius: 3px;
padding: 10px;
color: #555555;
text-align: justify !important;
}
.info h3{
position:relative;
font-weight: bold;
font-size: 15px;
padding: 0;
margin-top:8px;
top:0;
}
.info ul{
padding-left: 20px;
}
.info li:nth-child(1){
padding-bottom:10px;
}
/* end style paket internet/voucher */
.copyright{
margin-top: 40px;
font-size: 10px;
color: #666666;
}
.cs{
margin: -15px auto 20px auto;
font-size: 11px;
color: #666666;
}
.cs h4{
font-size: 12px;
color: #555555;
}
@font-face {
font-family: 'nyessid';
src: url('../font/nyessid.eot?63281300');
src: url('../font/nyessid.eot?63281300#iefix') format('embedded-opentype'),
url('../font/nyessid.woff2?63281300') format('woff2'),
url('../font/nyessid.woff?63281300') format('woff'),
url('../font/nyessid.ttf?63281300') format('truetype'),
url('../font/nyessid.svg?63281300#nyessid') format('svg');
font-weight: normal;
font-style: normal;
}
/* Chrome hack: SVG is rendered more smooth in Windozze. 100% magic, uncomment if you need it. */
/* Note, that will break hinting! In other OS-es font will be not as sharp as it could be */
/*
@media screen and (-webkit-min-device-pixel-ratio:0) {
@font-face {
font-family: 'nyessid';
src: url('../font/nyessid.svg?63281300#nyessid') format('svg');
}
}
*/
[class^="icon-"]:before, [class*=" icon-"]:before {
font-family: "nyessid";
font-style: normal;
font-weight: normal;
speak: none;
display: inline-block;
text-decoration: inherit;
width: 1em;
margin-right: .2em;
text-align: center;
font-variant: normal;
text-transform: none;
line-height: 1em;
margin-left: .2em;
-webkit-font-smoothing: antialiased;
-moz-osx-font-smoothing: grayscale;
}
.icon-lock:before { content: '\e800'; }
.icon-download:before { content: '\e801'; }
.icon-upload:before { content: '\e802'; }
.icon-attention-circled:before { content: '\e803'; }
.icon-calendar:before { content: '\e804'; }
.icon-drive:before { content: '\e805'; }
.icon-globe:before { content: '\e806'; }
.icon-arrows-cw:before { content: '\e807'; }
.icon-rss:before { content: '\e808'; }
.icon-rss-outline:before { content: '\e809'; }
.icon-wifi-1:before { content: '\e80a'; }
.icon-email:before { content: '\e80b'; }
.icon-emo-unhappy:before { content: '\e80c'; }
.icon-info-circled:before { content: '\e80d'; }
.icon-off:before { content: '\e80e'; }
.icon-clock-alt:before { content: '\e80f'; }
.icon-clock:before { content: '\e810'; }
.icon-spin4:before { content: '\e834'; }
.icon-location-1:before { content: '\f031'; }
.icon-phone-squared:before { content: '\f098'; }
.icon-mail-alt:before { content: '\f0e0'; }
.icon-gauge:before { content: '\f0e4'; }
.icon-circle:before { content: '\f111'; }
.icon-angle-circled-left:before { content: '\f137'; }
.icon-angle-circled-right:before { content: '\f138'; }
.icon-database:before { content: '\f1c0'; }
.icon-wechat:before { content: '\f1d7'; color:green;}
.icon-copyright:before { content: '\f1f9'; }
.icon-whatsapp:before { content: '\f232'; color:green;}
.icon-question-circle-o:before { content: '\f29c'; }
.icon-user-circle:before { content: '\f2bd'; }
.icon-user-circle-o:before { content: '\f2be'; }

File: /error.html
<html>
<head>
<title>mikrotik hotspot > error</title>
<meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1">
<meta http-equiv="pragma" content="no-cache">
<meta http-equiv="expires" content="-1">
<style type="text/css">
<!--
textarea,input,select {
	background-color: #FDFBFB;
	border: 1px #BBBBBB solid;
	padding: 2px;
	margin: 1px;
	font-size: 14px;
	color: #808080;
}

body{ color: #737373; font-size: 12px; font-family: verdana; }

a, a:link, a:visited, a:active { color: #AAAAAA; text-decoration: none; font-size: 12px; }
a:hover { border-bottom: 1px dotted #c1c1c1; color: #AAAAAA; }
img {border: none;}
td { font-size: 12px; color: #7A7A7A; }

-->
</style>
</head>
<body>
<table width="100%" height="100%">

<tr>
<td align="center" valign="middle">
Hotspot ERROR: $(error)<br>
<br>
Login page: <a href="$(link-login)">$(link-login)</a>
</td>
</tr>
</table>
</body>
</html>


File: /errors.txt
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

internal-error = internal error ($(error-orig))

# config-error
# Should never happen if hotspot is configured properly.

config-error = configuration error ($(error-orig))

# not-logged-in
# Will happen, if status or logout page is requested by user,
# which actually is not logged in

not-logged-in = Anda belum login (ip $(ip))

# ippool-empty
# IP address for user is to be assigned from ip pool, but there are no more
# addresses in that pool

ippool-empty = Tidak dapat menetapkan alamat IP - IP sudah terpakai semua 

# shutting-down
# When shutdown is executed, new clients are not accepted

shutting-down = hotspot service is shutting down

# user-session-limit
# If user profile has limit of shared-users, then this error will be shown
# after reaching this limit

user-session-limit = Tidak ada lagi sesi yang diizinkan untuk user $(username)

# license-session-limit
# Depending on licence number of active hotspot clients is limited to
# one or another amount. If this limit is reached, following error is displayed.

license-session-limit = Masa aktif telah habis ($(error-orig))

# wrong-mac-username
# If username looks like MAC address (12:34:56:78:9a:bc), but is not
# a MAC address of this client, login is rejected

wrong-mac-username = Username tidak valid : MAC ini bukan milik Anda!

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

chap-missing = Web browser tidak merespon, coba lagi

# invalid-username
# Most general case of invalid username or password. If RADIUS server
# has sent an error string with Access-Reject message, then it will
# override this setting.

invalid-username = username / password tidak valid!

# invalid-mac
# Local users (on hotspot server) can be bound to some MAC address. If login
# from different MAC is tried, this error message will be shown.

invalid-mac = User $(username) tidak diizinkan menggunakan alamat MAC ini!

# uptime-limit, traffic-limit
# For local hotspot users in case if limits are reached

uptime-limit = Masa aktif user $(username) telah habis
traffic-limit = Kuota user $(username) telah habis

# radius-timeout
# User is authenticated by RADIUS server, but no response is received from it,
# following error will be shown.

radius-timeout = RADIUS server is not responding

# auth-in-progress
# Authorization in progress. Client already has issued an authorization request
# which is not yet complete.

auth-in-progress = already authorizing, retry later

# radius-reply
# Radius server returned some custom error message

radius-reply = $(error-orig)


File: /js\md5.js
/*
 * A JavaScript implementation of the RSA Data Security, Inc. MD5 Message
 * Digest Algorithm, as defined in RFC 1321.
 * Version 1.1 Copyright (C) Paul Johnston 1999 - 2002.
 * Code also contributed by Greg Holt
 * See http://pajhome.org.uk/site/legal.html for details.
 */

/*
 * Add integers, wrapping at 2^32. This uses 16-bit operations internally
 * to work around bugs in some JS interpreters.
 */
function safe_add(x, y)
{
  var lsw = (x & 0xFFFF) + (y & 0xFFFF)
  var msw = (x >> 16) + (y >> 16) + (lsw >> 16)
  return (msw << 16) | (lsw & 0xFFFF)
}

/*
 * Bitwise rotate a 32-bit number to the left.
 */
function rol(num, cnt)
{
  return (num << cnt) | (num >>> (32 - cnt))
}

/*
 * These functions implement the four basic operations the algorithm uses.
 */
function cmn(q, a, b, x, s, t)
{
  return safe_add(rol(safe_add(safe_add(a, q), safe_add(x, t)), s), b)
}
function ff(a, b, c, d, x, s, t)
{
  return cmn((b & c) | ((~b) & d), a, b, x, s, t)
}
function gg(a, b, c, d, x, s, t)
{
  return cmn((b & d) | (c & (~d)), a, b, x, s, t)
}
function hh(a, b, c, d, x, s, t)
{
  return cmn(b ^ c ^ d, a, b, x, s, t)
}
function ii(a, b, c, d, x, s, t)
{
  return cmn(c ^ (b | (~d)), a, b, x, s, t)
}

/*
 * Calculate the MD5 of an array of little-endian words, producing an array
 * of little-endian words.
 */
function coreMD5(x)
{
  var a =  1732584193
  var b = -271733879
  var c = -1732584194
  var d =  271733878

  for(i = 0; i < x.length; i += 16)
  {
    var olda = a
    var oldb = b
    var oldc = c
    var oldd = d

    a = ff(a, b, c, d, x[i+ 0], 7 , -680876936)
    d = ff(d, a, b, c, x[i+ 1], 12, -389564586)
    c = ff(c, d, a, b, x[i+ 2], 17,  606105819)
    b = ff(b, c, d, a, x[i+ 3], 22, -1044525330)
    a = ff(a, b, c, d, x[i+ 4], 7 , -176418897)
    d = ff(d, a, b, c, x[i+ 5], 12,  1200080426)
    c = ff(c, d, a, b, x[i+ 6], 17, -1473231341)
    b = ff(b, c, d, a, x[i+ 7], 22, -45705983)
    a = ff(a, b, c, d, x[i+ 8], 7 ,  1770035416)
    d = ff(d, a, b, c, x[i+ 9], 12, -1958414417)
    c = ff(c, d, a, b, x[i+10], 17, -42063)
    b = ff(b, c, d, a, x[i+11], 22, -1990404162)
    a = ff(a, b, c, d, x[i+12], 7 ,  1804603682)
    d = ff(d, a, b, c, x[i+13], 12, -40341101)
    c = ff(c, d, a, b, x[i+14], 17, -1502002290)
    b = ff(b, c, d, a, x[i+15], 22,  1236535329)

    a = gg(a, b, c, d, x[i+ 1], 5 , -165796510)
    d = gg(d, a, b, c, x[i+ 6], 9 , -1069501632)
    c = gg(c, d, a, b, x[i+11], 14,  643717713)
    b = gg(b, c, d, a, x[i+ 0], 20, -373897302)
    a = gg(a, b, c, d, x[i+ 5], 5 , -701558691)
    d = gg(d, a, b, c, x[i+10], 9 ,  38016083)
    c = gg(c, d, a, b, x[i+15], 14, -660478335)
    b = gg(b, c, d, a, x[i+ 4], 20, -405537848)
    a = gg(a, b, c, d, x[i+ 9], 5 ,  568446438)
    d = gg(d, a, b, c, x[i+14], 9 , -1019803690)
    c = gg(c, d, a, b, x[i+ 3], 14, -187363961)
    b = gg(b, c, d, a, x[i+ 8], 20,  1163531501)
    a = gg(a, b, c, d, x[i+13], 5 , -1444681467)
    d = gg(d, a, b, c, x[i+ 2], 9 , -51403784)
    c = gg(c, d, a, b, x[i+ 7], 14,  1735328473)
    b = gg(b, c, d, a, x[i+12], 20, -1926607734)

    a = hh(a, b, c, d, x[i+ 5], 4 , -378558)
    d = hh(d, a, b, c, x[i+ 8], 11, -2022574463)
    c = hh(c, d, a, b, x[i+11], 16,  1839030562)
    b = hh(b, c, d, a, x[i+14], 23, -35309556)
    a = hh(a, b, c, d, x[i+ 1], 4 , -1530992060)
    d = hh(d, a, b, c, x[i+ 4], 11,  1272893353)
    c = hh(c, d, a, b, x[i+ 7], 16, -155497632)
    b = hh(b, c, d, a, x[i+10], 23, -1094730640)
    a = hh(a, b, c, d, x[i+13], 4 ,  681279174)
    d = hh(d, a, b, c, x[i+ 0], 11, -358537222)
    c = hh(c, d, a, b, x[i+ 3], 16, -722521979)
    b = hh(b, c, d, a, x[i+ 6], 23,  76029189)
    a = hh(a, b, c, d, x[i+ 9], 4 , -640364487)
    d = hh(d, a, b, c, x[i+12], 11, -421815835)
    c = hh(c, d, a, b, x[i+15], 16,  530742520)
    b = hh(b, c, d, a, x[i+ 2], 23, -995338651)

    a = ii(a, b, c, d, x[i+ 0], 6 , -198630844)
    d = ii(d, a, b, c, x[i+ 7], 10,  1126891415)
    c = ii(c, d, a, b, x[i+14], 15, -1416354905)
    b = ii(b, c, d, a, x[i+ 5], 21, -57434055)
    a = ii(a, b, c, d, x[i+12], 6 ,  1700485571)
    d = ii(d, a, b, c, x[i+ 3], 10, -1894986606)
    c = ii(c, d, a, b, x[i+10], 15, -1051523)
    b = ii(b, c, d, a, x[i+ 1], 21, -2054922799)
    a = ii(a, b, c, d, x[i+ 8], 6 ,  1873313359)
    d = ii(d, a, b, c, x[i+15], 10, -30611744)
    c = ii(c, d, a, b, x[i+ 6], 15, -1560198380)
    b = ii(b, c, d, a, x[i+13], 21,  1309151649)
    a = ii(a, b, c, d, x[i+ 4], 6 , -145523070)
    d = ii(d, a, b, c, x[i+11], 10, -1120210379)
    c = ii(c, d, a, b, x[i+ 2], 15,  718787259)
    b = ii(b, c, d, a, x[i+ 9], 21, -343485551)

    a = safe_add(a, olda)
    b = safe_add(b, oldb)
    c = safe_add(c, oldc)
    d = safe_add(d, oldd)
  }
  return [a, b, c, d]
}

/*
 * Convert an array of little-endian words to a hex string.
 */
function binl2hex(binarray)
{
  var hex_tab = "0123456789abcdef"
  var str = ""
  for(var i = 0; i < binarray.length * 4; i++)
  {
    str += hex_tab.charAt((binarray[i>>2] >> ((i%4)*8+4)) & 0xF) +
           hex_tab.charAt((binarray[i>>2] >> ((i%4)*8)) & 0xF)
  }
  return str
}

/*
 * Convert an array of little-endian words to a base64 encoded string.
 */
function binl2b64(binarray)
{
  var tab = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
  var str = ""
  for(var i = 0; i < binarray.length * 32; i += 6)
  {
    str += tab.charAt(((binarray[i>>5] << (i%32)) & 0x3F) |
                      ((binarray[i>>5+1] >> (32-i%32)) & 0x3F))
  }
  return str
}

/*
 * Convert an 8-bit character string to a sequence of 16-word blocks, stored
 * as an array, and append appropriate padding for MD4/5 calculation.
 * If any of the characters are >255, the high byte is silently ignored.
 */
function str2binl(str)
{
  var nblk = ((str.length + 8) >> 6) + 1 // number of 16-word blocks
  var blks = new Array(nblk * 16)
  for(var i = 0; i < nblk * 16; i++) blks[i] = 0
  for(var i = 0; i < str.length; i++)
    blks[i>>2] |= (str.charCodeAt(i) & 0xFF) << ((i%4) * 8)
  blks[i>>2] |= 0x80 << ((i%4) * 8)
  blks[nblk*16-2] = str.length * 8
  return blks
}

/*
 * Convert a wide-character string to a sequence of 16-word blocks, stored as
 * an array, and append appropriate padding for MD4/5 calculation.
 */
function strw2binl(str)
{
  var nblk = ((str.length + 4) >> 5) + 1 // number of 16-word blocks
  var blks = new Array(nblk * 16)
  for(var i = 0; i < nblk * 16; i++) blks[i] = 0
  for(var i = 0; i < str.length; i++)
    blks[i>>1] |= str.charCodeAt(i) << ((i%2) * 16)
  blks[i>>1] |= 0x80 << ((i%2) * 16)
  blks[nblk*16-2] = str.length * 16
  return blks
}

/*
 * External interface
 */
function hexMD5 (str) { return binl2hex(coreMD5( str2binl(str))) }
function hexMD5w(str) { return binl2hex(coreMD5(strw2binl(str))) }
function b64MD5 (str) { return binl2b64(coreMD5( str2binl(str))) }
function b64MD5w(str) { return binl2b64(coreMD5(strw2binl(str))) }
/* Backward compatibility */
function calcMD5(str) { return binl2hex(coreMD5( str2binl(str))) }


File: /js\signup.js
$("#modal-signup").on("hidden.bs.modal", function () {
$(this).find('form').trigger('reset');
document.getElementById("password2").style.display = "none";
document.getElementById("validate-status").style.display = "none";
$("#password1").prop("readonly", false);
});
document.getElementById("password2").style.display = "none";
$(document).ready(function(){
$("#password1").keyup(input);
$("#password2").keyup(readonly);
$("#password2").keyup(validate);
});
function input(){
if($("#password1").val() == 0){
document.getElementById("validate-status").style.display = "none";
document.getElementById("password2").style.display = "none";
 }else{
document.getElementById("password2").style.display = "block";
 }
}
function readonly(){
if($("#password2").val() == 0){
$("#password1").prop("readonly", false);
 }else{
$("#password1").prop("readonly", true);
 }
}
function validate() {
var password1 = $("#password1").val();
var password2 = $("#password2").val();
if(password1 == password2) {
document.getElementById("validate-status").style.display = "block";
$("#validate-status").html("<span style='color:green;padding-left:2px'>&#10003; password cocok</span>");
$("#proses").prop("disabled", false);
 }else {
document.getElementById("validate-status").style.display = "block";
$("#validate-status").html("<span style='color:red;padding-left:2px'>&#x2717; password tidak cocok!</span>");
$("#proses").prop("disabled", true);
 }
}
function signup(){
// chat_id = "-239942270";
chat_id = " ";
// token = "423903821:AAE9-rq9NMS_HFVMTk09UVyDnEFRBfdCkkc";
token = " ";
message = "<b>MEMBER SIGNUP</b>%0Anama : "+ $("#nama").val() + "%0Aalamat : " + $("#alamat").val() + "%0Ano. hp : " + $("#nomor").val() + "%0Amac : " + $("#mac").val() + "%0Apaket : " + $("#paket").val() + "%0Ausername : " + $("#username").val() + "%0Apassword : " + $("#password2").val();
$.get("https://api.telegram.org/bot"+token+"/sendMessage?text="+message+"&chat_id="+chat_id+"&parse_mode=html");
$("#modal-signup").modal("hide");
$("#confirm").modal("show");
}


File: /login.html
<!DOCTYPE html>
<html>
	<head>
		<title>IDSkyNetwork - Login</title>
		<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
		<meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1.0, user-scalable=no">
		<meta http-equiv="X-UA-Compatible" content="IE=edge">
		<meta http-equiv="pragma" content="no-cache" />
		<meta http-equiv="expires" content="-1" />
		<link rel="shortcut icon" href="img/corner.png" type="image/x-icon">
		<link rel="icon" href="img/corner.png" type="image/x-icon">
		<link rel="stylesheet" href="css/custom.bootstrap.min.css">
		<link rel="stylesheet" href="css/custom.css">
	</head>
	<body class="bg-img">
		$(if chap-id)
		<form name="sendin" action="$(link-login-only)" method="post">
			<input type="hidden" name="username" />
			<input type="hidden" name="password" />
			<input type="hidden" name="dst" value="$(link-orig)" />
			<input type="hidden" name="popup" value="true" />
		</form>
		<script type="text/javascript" src="js/md5.js"></script>
		<script type="text/javascript">
		function doLogin() {
			document.sendin.username.value = document.login.username.value;
			document.sendin.password.value = hexMD5('$(chap-id)' + document.login.password.value + '$(chap-challenge)');
			document.sendin.submit();
			return false;
		}
		</script>
		$(endif)
		<div class="jumbroton">
			<div class="col-md-4 col-md-offset-4 text-center">
				<img class="logo" src="img/corner.png">
				<fieldset class="fieldset title">
					<legend align="center" class="legend">
						<span class="text-center">MEMBER LOGIN</span>
					</legend>
				</fieldset>
				<div id="error" class='error'>
					<script type="text/javascript">
					var error="$(error)";
					if(error=="credit limit reached"){
						document.write('<div class="alert alert-danger"><i class="icon-attention-circled"></i>Batas kredit user <b>$(username)</b> sudah habis</div>');
						}
					else if(error=="uptime limit reached"){
						document.write('<div class="alert alert-danger"><i class="icon-attention-circled"></i>Masa aktif user <b>$(username)</b> sudah habis</div>');
						}
					else if(error=="download limit reached"){
						document.write('<div class="alert alert-danger"><i class="icon-attention-circled"></i>Kuota user <b>$(username)</b> telah habis</div>');
						}
					else if(error=="no valid profile found"){
						document.write('<div class="alert alert-danger"><i class="icon-attention-circled"></i>Masa aktif user <b>$(username)</b> telah habis</div>');
						}
					else if(error=="invalid password"){
						document.write('<div class="alert alert-danger"><i class="icon-attention-circled"></i>username / password tidak valid!</div>');
						}
					else if(error=="simultaneous session limit reached") {
						document.write('<div class="alert alert-danger"><i class="icon-attention-circled"></i>User <b>$(username)</b> sudah login di device lain</div>');
						}
					else if(error){
						document.write('<div class="alert alert-danger"><i class="icon-attention-circled"></i>$(error)</div>');
					}
					</script>
				</div>
				<form name="login" action="$(link-login-only)" method="post" $(if chap-id) onSubmit="return doLogin()" $(endif)>
					<input type="hidden" name="dst" value="$(link-orig)" />
					<input type="hidden" name="popup" value="true" />
					<div class="form-group">
						<input type="text" class="form-control text-center input-login" name="username"  placeholder="username" value="$(username)" required="required" autocomplete="off">
					</div>
					<div class="form-group">
						<input type="password" class="form-control text-center input-login" name="password"  placeholder="password" required="required" autocomplete="off">
					</div>
					<div class="form-group text-center">
						<button type="submit" class="btn btn-success">LOGIN</button>
					</div>
					<div class="form-group text-center">
						<p class="p">Belum punya akun? klik <a href="paket.html">DISINI</a></p>
					</div>
				</form>
			</div>
			<div class="col-md-4 col-md-offset-4 text-center copyright">
				<fieldset class="fieldset">
					<legend align="center" class="legend">
						<span class="icon-copyright text-center copyright">wificorner 2017</span>
					</legend>
				</fieldset>
				<div class="cs">
                    <h4>Sleman, Yogyakarta, Indonesia</h4>
				    CS : <span class="icon-whatsapp">t.me/lspcisec</span>
				</div>
			</div>
			<div id="modal-notice" class="modal fade" role="dialog" data-backdrop="static">
				<div class="modal-dialog modal-sm">
					<!-- Modal content-->
					<div class="modal-content">
						<div class="text-warning modal-header">
							<h4 class="modal-title text-center icon-attention-circled">Oops..</h4>
						</div>
						<div class="modal-body">
							<h4>Hello.. $(username)</h4>
							<p>Mohon maaf, masa aktif Anda telah habis, silahkan melakukan pembayaran jika Anda ingin memperpanjang masa aktif.</p>
							<p>Atau</p>
							<p>Klik <a href="paket.html">DISINI</a> untuk melihat daftar paket terbaru.</p>
						</div>
						<div class="modal-footer">
							<button type="button" class="btn btn-default btn-sm center-block" data-dismiss="modal">OK</button>
						</div>
					</div>
				</div>
			</div>
		</div>
		<script src="js/jquery.min.js"></script>
		<script src="js/bootstrap.min.js"></script>
		<script language="JavaScript">
		if(error=="no valid profile found"){
		$("#modal-notice").modal('show');
	    }
		var margin=10;
		var speed=20;
		var times=4;
		for(var i=0;i<times;i++){
		$("#error").animate({'margin-left':"+="+(margin=-margin)+'px'},speed);
		$("#error").animate({'margin-right':"+="+(margin=-margin)+'px'},speed);
		$("#error").animate({'margin-right':"+="+(margin=-margin)+'px'},speed);
		$("#error").animate({'margin-left':"+="+(margin=-margin)+'px'},speed);
		}
		</script>
	</body>
</html>

File: /logout.html
<!DOCTYPE html>
<html>
	<head>
		<title>@wificorner - Logout</title>
		<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
		<meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1.0, user-scalable=no">
		<meta http-equiv="X-UA-Compatible" content="IE=edge">
		<meta http-equiv="pragma" content="no-cache" />
		<meta http-equiv="expires" content="-1" />
		<link rel="shortcut icon" href="img/corner.png" type="image/x-icon">
		<link rel="icon" href="img/corner.png" type="image/x-icon">
		<link rel="stylesheet" href="css/custom.bootstrap.min.css">
		<link rel="stylesheet" href="css/custom.css">
	</head>
	<body class="bg-img">
		<script language="JavaScript">
		function openLogin() {
			if (window.name != 'hotspot_logout') return true;
			open('$(link-login)', '_blank', '');
			window.close();
			return false;
		}
		</script>
		<div class="jumbroton">
			<div class="col-md-4 col-md-offset-4 text-center">
				<img class="logo" src="img/corner.png">
				<fieldset class="fieldset title">
					<legend align="center" class="legend">
						<span class="text-center">LOGOUT</span>
					</legend>
				</fieldset>
				<p class="text-center info-user">Anda telah logout, silahkan relogin untuk terhubung kembali</p>
				<table class="table table-bordered text-left">
				<tr>
				<td>User</td><td>
					$(if login-by == 'trial')
					TRIAL
					$(elif login-by != 'mac')
					$(username)
					$(endif)
				</td>
				</tr>
				<tr><td>Alamat IP</td><td>$(ip)</td></tr>
				<tr><td>Terhubung</td><td>$(uptime)</td></tr>
				<tr><td>Trafik</td><td>$(bytes-total-nice)</td></tr>
				<tr><td>Sisa kuota</td><td>$(remain-bytes-total-nice)</td></tr>
				$(if session-time-left)
				<tr><td>Sisa masa aktif</td><td>$(session-time-left)</td></tr>
				$(else)
				<tr><td>Sisa masa aktif</td><td>unlimited</td></tr>
				$(endif)
			</table>
			<div class="form-group">
				<form action="$(link-login)" name="login" onSubmit="return openLogin()">
					<button type="submit" class="btn btn-success">RELOGIN</button>
				</form>
			</div>
		</div>
		<div class="col-md-4 col-md-offset-4 text-center copyright">
			<fieldset class="fieldset">
				<legend align="center" class="legend">
					<span class="icon-copyright text-center copyright">wificorner 2017</span>
				</legend>
			</fieldset>
			<div class="cs">
				<h4>Jl. Anggrek No. 25B - Nganjuk</h4>
				CS : <span class="icon-whatsapp">08123456789</span>
			</div>
		</div>
	</div>
	<script src="js/jquery.min.js"></script>
	<script src="js/bootstrap.min.js"></script>
</body>
</html>

File: /maintenance.html
<!DOCTYPE html>
<html>
	<head>
		<title>@IDSkyNetwork - Maintenance</title>
		<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
		<meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1.0, user-scalable=no">
		<meta http-equiv="X-UA-Compatible" content="IE=edge">
		<meta http-equiv="pragma" content="no-cache" />
		<link rel="shortcut icon" href="img/corner.png" type="image/x-icon">
		<link rel="icon" href="img/corner.png" type="image/x-icon">
		<link rel="stylesheet" href="css/custom.bootstrap.min.css">
		<link rel="stylesheet" href="css/custom.css">
	</head>
	<body class="bg-img">
		<div class="jumbroton">
			<div class="col-md-4 col-md-offset-4 text-center">
				<img class="logo" src="img/corner.png">
				<fieldset class="fieldset title">
					<legend align="center" class="legend">
						<span class="text-center">MAINTENANCE</span>
					</legend>
				</fieldset>
				<div class="col-sm-12 text-center">
					<h4 class="icon-attention-circled text-danger">SEDANG PERBAIKAN SERVER</h4>
					<p>Kami mohon maaf atas ketidaknyamanan ini</p>
					<p>Silahkan coba lagi nanti</p>
					<img class="img-responsive" src="img/maintenance.png">
				</div>
			</div>
			<div class="col-md-4 col-md-offset-4 text-center copyright">
				<fieldset class="fieldset">
					<legend align="center" class="legend">
						<span class="icon-copyright text-center copyright">IDSkyNetwork 2017</span>
					</legend>
				</fieldset>
				<div class="cs">
					<h4>Jl. Gempol Raya No.3</h4>
					CS : <span class="icon-whatsapp">089689055046</span>
				</div>
			</div>
		</div>
	</body>
</html>

File: /paket.html
<!DOCTYPE html>
<html>
	<head>
		<title>@IDSkyNetwork - Paket Internet</title>
		<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
		<meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1.0, user-scalable=no">
		<meta http-equiv="X-UA-Compatible" content="IE=edge">
		<link rel="shortcut icon" href="img/corner.png" type="image/x-icon">
		<link rel="icon" href="img/corner.png" type="image/x-icon">
		<link rel="stylesheet" href="css/custom.bootstrap.min.css">
		<link rel="stylesheet" href="css/custom.css">
	</head>
	<body class="bg-img">
		<div class="jumbroton">
			<div class="col-md-4 col-md-offset-4 text-center">
			<img class="logo" src="img/corner.png">
				<fieldset class="fieldset title">
					<legend align="center" class="legend">
						<span class="text-center">PAKET INTERNET</span>
					</legend>
				</fieldset>
				<div class="paket">
					<div class="panel border-panel1 text-center">
						<div class="panel-heading bg-panel1">
						<h3>TRIAL</h3>
						</div>
						<div class="panel-body">
							<p>Kecepatan : up to <b>20</b> Mbps</p>
							<p>Kuota : Unlimited</p>
							<p>Masa Aktif : 10 menit /hari</p>
						</div><div class="panel-footer">
						<p>
						$(if logged-in == 'yes')
						<button class="btn btn-default beli disabled">TRIAL</button> 
						$(else) 
						$(if trial == 'yes')
						<a href='$(link-login-only)?dst=$(link-orig-esc)&amp;username=T-$(mac-esc)' class="btn btn-success beli" data-toggle="tooltip" data-placement="top" title="Klik untuk auto login">TRIAL</a
						>
						$(else)
						<button class="btn btn-success beli disabled" data-toggle="popover" data-placement="top" data-content="Server Offline">TRIAL</button>
						$(endif)
						$(endif)
						</p>
					</div>
				</div>
			</div>
			<div class="paket">
				<div class="panel border-panel2 text-center">
					<div class="panel-heading bg-panel2">
						<h3>BASIC</h3>
					</div>
					<div class="panel-body">
						<p>Kecepatan : up to <b>10</b> Mbps</p>
						<p>Kuota : Unlimited</p>
						<p>Masa Aktif : 30 hari</p>
						<span class="harga">Rp <b>110.000</b></span>
						<span class="masa-aktif">bulan</span>
					</div>
					<div class="panel-footer">
						<p><button class="btn btn-success beli" data-toggle="modal" data-target="#modal-signup">SIGNUP</button></p>
					</div>
				</div>
			</div>
			<div class="paket">
				<div class="panel border-panel3 text-center">
					<div class="panel-heading bg-panel3">
						<h3>PRO</h3>
					</div>
					<div class="panel-body">
						<p>Kecepatan : up to <b>20</b> Mbps</p>
						<p>Kuota : Unlimited</p>
						<p>Masa Aktif : 30 hari</p>
						<span class="harga">Rp <b>200.000</b></span>
						<span class="masa-aktif">bulan</span>
					</div>
					<div class="panel-footer">
						<p><button class="btn btn-success beli" data-toggle="modal" data-target="#modal-signup">SIGNUP</button></p>
					</div>
				</div>
			</div>
			<div class="info bg-info">
				<h3 class="icon-info-circled text-info">info</h3>
				<ul>
					<li><b>Promo!</b> Diskon 20% di bulan pertama untuk pelanggan baru.</li>
					$(if trial == 'yes')
					<li>Silahkan pilih <b>TRIAL</b> jika Anda ingin mencoba dulu layanan kami.</li>
					$(endif)
				</ul>
			</div>
			<div class="text-center copyright">
				<fieldset class="fieldset">
					<legend align="center" class="legend">
						<span class="icon-copyright copyright">IDSkyNetwork 2017</span>
					</legend>
				</fieldset>
				<div class="cs">
                    <h4>Jl. Anggrek No. 25B - Nganjuk</h4>
				    CS : <span class="icon-whatsapp">08123456789</span>
				</div>
			</div>
			<div id="modal-signup" class="modal fade" role="dialog" data-backdrop="static">
				<div class="modal-dialog">
					<!-- Modal content-->
					<div class="modal-content">
						<div class="modal-header">
							<h4 class="modal-title text-center">SIGNUP</h4>
						</div>
						<form id="form-signup" action="javascript:signup();">
							<div class="modal-body text-left">
								<div class="form-group">
									<input id="nama" class="form-control" type="text" placeholder="nama" pattern="[A-z\s]{3,20}" required title="minim 3 karakter yg diperbolehkan a-z A-Z">
								</div>
								<div class="form-group">
									<input id="alamat" class="form-control" type="text" placeholder="alamat" required>
								</div>
								<div class="form-group">
									<input id="nomor" class="form-control" type="text" placeholder="no. hp" pattern="[0-9-]+" required title="karakter yg diperbolehkan 0-9">
								</div>
								<div class="form-group input-group">
								    <span class="input-group-addon">mac</span>
									<input id="mac" class="form-control" type="text" value="$(mac)" readonly="readonly">
								</div>
								<div class="form-group">
									<select id="paket" class="form-control" required>
										<option value="" selected>- pilih paket -</option>
										<option value="10Mbps - Rp 110.000">10Mbps - Rp 110.000</option>
										<option value="20Mbps - Rp 200.000">20Mbps - Rp 200.000</option>
									</select>
								</div>
								<div class="form-group">
									<input id="username" class="form-control" type="text" placeholder="username" pattern="[A-z0-9]{4,20}" required title="minimal 4 karakter yg diperbolehkan a-z A-Z 0-9 tanpa spasi">
								</div>
								<div class="form-group">
									<input id="password1" class="form-control" type="password" placeholder="password" autocomplete="off" pattern=".{3,}" required title="minimal 3 karakter">
								</div>
								<div class="form-group">
								    <div id="validate-status"></div>
									<input id="password2" class="form-control" type="password" placeholder="ulangi password" autocomplete="off" pattern=".{3,}" required title="minimal 3 karakter">
								</div>
								<div class="form-check">
									<label class="form-check-label">
										<input type="checkbox" class="form-check-input" required="required">
										<span class="check">Saya setuju dengan <a href="tos.html" target="_blank">syarat &amp; ketentuan</a> @IDSkyNetwork</span>
									</label>
								</div>
							</div>
							<div class="modal-footer">
								<button id="proses" type="submit" class="btn btn-success btn-md pull-right">PROSES</button>
								<button class="btn btn-warning btn-md pull-left" data-dismiss="modal">BATAL</button>
							</div>
						</form>
					</div>
				</div>
			</div>
			<div id="confirm" class="modal fade" role="dialog" data-backdrop="static">
				<div class="modal-dialog modal-sm">
					<!-- Modal content-->
					<div class="modal-content">
						<div class="modal-body text-center">
						    <p></p>
							<p>Permintaan Anda berhasil terkirim, silahkan tunggu konfirmasi dari kami via sms.</p>
							<button type="button" class="btn btn-success center-block" data-dismiss="modal">OK</button>
						</div>
					</div>
				</div>
			</div>
		</div>
	</div>
	<script src="js/jquery.min.js"></script>
	<script src="js/signup.js"></script>
	<script src="js/bootstrap.min.js"></script>
</body>
</html>

File: /radvert.html
<html>
<head>
<title>mikrotik hotspot > advertisement</title>
<meta http-equiv="refresh" content="2; url=$(link-orig)">
<meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1">
<meta http-equiv="pragma" content="no-cache">
<meta http-equiv="expires" content="-1">
<style type="text/css">
<!--
textarea,input,select {
	background-color: #FDFBFB;
	border: 1px #BBBBBB solid;
	padding: 2px;
	margin: 1px;
	font-size: 14px;
	color: #808080;
}

body{ color: #737373; font-size: 12px; font-family: verdana; }

a, a:link, a:visited, a:active { color: #AAAAAA; text-decoration: none; font-size: 12px; }
a:hover { border-bottom: 1px dotted #c1c1c1; color: #AAAAAA; }
img {border: none;}
td { font-size: 12px; color: #7A7A7A; }

-->
</style>
<script language="JavaScript">
<!--
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
//-->
</script>
</head>
<body onLoad="openAdvert()">
<table width="100%" height="100%">
<tr>
	<td align="center" valign="middle">
	Advertisement.
	<br><br>
	If nothing happens, open
	<a href="$(link-redirect)" target="hotspot_advert">advertisement</a>
	manually.
	</td>
</tr>
</table>
</body>
</html>


File: /readme.txt
=============== LOGIN PAGE HOTSPOT MIKROTIK ===========

WIFICORNER 1.3
License : Free
Author : Agus Purnomo
Facebook url : https://www.facebook.com/nyess.id


- Simple design 
- Responsive template
- Halaman harga paket internet + signup form (paket.html)
- Notifikasi signup user lewat chat bot telegram
- Halaman terms of service (tos.html) 
- Halaman maintenance (maintenance.html)



# Konfigurasi bot telegram

1. Bagi yg belum punya bot telegram silahkan bikin dulu ya botnya, caranya bisa googling biar lebih mudah biasanya ada screenshot disana.

2. Skip, saya anggap Anda sudah punya TOKEN dan CHAT_ID bot telegram.

3. Edit file /js/signup.js dengan text editor kesayangan Anda.

4. Cari kode token = " "; dan chat_id =" "; isikan token dan chat_id Anda.

5. Save

6. Tambahkan walled garden api.telegram.org di hotspot mikrotik, buka terminal kemudian ketik/copy kode

   /ip hotspot walled-garden
   add action=allow disabled=no dst-host=api.telegram.org

7. Done!

Note : Fitur ini hanya untuk notifikasi saja, untuk menambahkan user di mikrotik silahkan input manual.



# Edit file 

1. Edit untuk ganti title, alamat, kontak di file :

/login.html
/status.html
/logout.html
/tos.html
/maintenance.html
/paket.html

2. Edit harga paket di file /paket.html , sesuaikan dengan harga paket layanan hotspot Anda.


3. Edit syarat & ketentuan di file /tos.html sesuaikan dengan aturan layanan hotspot Anda.



* DILARANG MEMPERJUAL BELIKAN TEMPLATE INI *






File: /redirect.html
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


File: /rlogin.html
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


File: /status.html
<!DOCTYPE html>
<html>
	<head>
		<title>IDSkyNetwork - Status</title>
		$(if refresh-timeout)
		<meta http-equiv="refresh" content="$(refresh-timeout-secs)">
		$(endif)
		<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
		<meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1.0, user-scalable=no">
		<meta http-equiv="X-UA-Compatible" content="IE=edge">
		<meta http-equiv="pragma" content="no-cache" />
		<meta http-equiv="expires" content="-1" />
		<link rel="shortcut icon" href="img/corner.png" type="image/x-icon">
		<link rel="icon" href="img/corner.png" type="image/x-icon">
		<link rel="stylesheet" href="css/custom.bootstrap.min.css">
		<link rel="stylesheet" href="css/custom.css">
		<script language="JavaScript">
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
	<body class="bg-img" bottommargin="0" topmargin="0" leftmargin="0" rightmargin="0"
		$(if advert-pending == 'yes')
		onLoad="openAdvert()"
		$(endif)
		>
		<div class="jumbroton">
			<div class="col-md-4 col-md-offset-4 text-center">
				<img class="logo" src="img/corner.png">
				<fieldset class="fieldset title">
					<legend align="center" class="legend">
						<span class="text-center">
							WELCOME $(if login-by == 'trial')
							TRIAL
							$(elif login-by != 'mac')
							$(username)
							$(endif)
						</span>
					</legend>
				</fieldset>
				<p class="text-center info-user">Silahkan pergunakan internet dengan bijak</p>
				<table class="table table-bordered text-left">
					<tr>
						<td>User</td>
						<td>
							$(if login-by == 'trial')
							TRIAL
							$(elif login-by != 'mac')
							$(username)
							$(endif)
						</td>
					</tr>
					<tr><td>Alamat IP</td><td>$(ip)</td></tr>
					<tr><td>Terhubung</td><td>$(uptime)</td></tr>
					<tr><td>Trafik</td><td>$(bytes-total-nice)</td></tr>
					<tr><td>Sisa kuota</td><td>$(remain-bytes-total-nice)</td></tr>
					$(if session-time-left)
					<tr><td>Sisa masa aktif</td><td>$(session-time-left)</td></tr>
					$(else)
					<tr><td>Sisa masa aktif</td><td>unlimited</td></tr>
					$(endif)
				</table>
				<div class="form-group">
					<form action="$(link-logout)" name="logout" onSubmit="return openLogout()">
						<input type="hidden" name="erase-cookie" value="on">
						$(if login-by-mac != 'yes')
						<button type="submit" class="btn btn-danger">LOGOUT</button>
						$(endif)
					</form>
				</div>
			</div>
			<div class="col-md-4 col-md-offset-4 text-center copyright">
				<fieldset class="fieldset">
					<legend align="center" class="legend">
						<span class="icon-copyright text-center copyright">IDSkyNetwork</span>
					</legend>
				</fieldset>
				<div class="cs">
					<h4>Sleman, Yogyakarta, Indonesia</h4>
					CS : <span class="icon-whatsapp">t.me/lspcisec</span>
				</div>
			</div>
		</div>
		<script src="js/jquery.min.js"></script>
		<script src="js/bootstrap.min.js"></script>
	</body>
</html>

File: /tos.html
<!DOCTYPE html>
<html>
	<head>
		<title>@IDSkyNetwork - TOS</title>
		<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
		<meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1.0, user-scalable=no">
		<meta http-equiv="X-UA-Compatible" content="IE=edge">
		<meta http-equiv="pragma" content="no-cache" />
		<link rel="shortcut icon" href="img/corner.png" type="image/x-icon">
		<link rel="icon" href="img/corner.png" type="image/x-icon">
		<link rel="stylesheet" href="css/custom.bootstrap.min.css">
		<link rel="stylesheet" href="css/custom.css">
	</head>
	<body class="bg-img">
		<div class="jumbroton">
			<div class="col-md-4 col-md-offset-4 text-center">
				<img class="logo" src="img/corner.png">
				<fieldset class="fieldset title">
					<legend align="center" class="legend">
						<span class="text-center">SYARAT &amp; KETENTUAN</span>
					</legend>
				</fieldset>
				<div class="text-left tos">
				
					<!-- tulis konten tos disini-->

				</div>
			</div>
			<div class="col-md-4 col-md-offset-4 text-center copyright">
				<fieldset class="fieldset">
					<legend align="center" class="legend">
						<span class="icon-copyright text-center copyright">IDSkyNetwork 2017</span>
					</legend>
				</fieldset>
				<div class="cs">
					<h4>Jl. Gempol Raya No.3</h4>
					CS : <span class="icon-whatsapp">089689055046</span>
				</div>
			</div>
		</div>
	</body>
</html>

File: /xml\alogin.html
<HTML> <!--
<?xml version="1.0" encoding="UTF-8"?>
  <WISPAccessGatewayParam
  xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
  xsi:noNamespaceSchemaLocation="http://$(hostname)/xml/WISPAccessGatewayParam.xsd">
    <AuthenticationReply>
	<MessageType>120</MessageType>
	<ResponseCode>50</ResponseCode>
	<LogoffURL>$(link-logout)</LogoffURL>
	<RedirectionURL>$(link-redirect)</RedirectionURL>
$(if radius18[0])	<ReplyMessage>$(radius18[0])</ReplyMessage>	$(endif)
$(if radius18[1])	<ReplyMessage>$(radius18[1])</ReplyMessage>	$(endif)
$(if radius18[2])	<ReplyMessage>$(radius18[2])</ReplyMessage>	$(endif)
$(if radius18[3])	<ReplyMessage>$(radius18[3])</ReplyMessage>	$(endif)
$(if radius18[4])	<ReplyMessage>$(radius18[4])</ReplyMessage>	$(endif)
    </AuthenticationReply>
  </WISPAccessGatewayParam>
--> </HTML>


File: /xml\error.html
<HTML> <!--
<?xml version="1.0" encoding="UTF-8"?>
  <WISPAccessGatewayParam
  xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
  xsi:noNamespaceSchemaLocation="http://$(hostname)/xml/WISPAccessGatewayParam.xsd">
    <AuthenticationReply>
	<MessageType>120</MessageType>
	<ResponseCode>255</ResponseCode>
	<ReplyMessage>$(error)</ReplyMessage>
    </AuthenticationReply>
  </WISPAccessGatewayParam>
--> </HTML>


File: /xml\flogout.html
<HTML> <!--
<?xml version="1.0" encoding="UTF-8"?>
  <WISPAccessGatewayParam
  xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
  xsi:noNamespaceSchemaLocation="http://$(hostname)/xml/WISPAccessGatewayParam.xsd">
    <LogoffReply>
	<MessageType>130</MessageType>
	<ResponseCode>150</ResponseCode>
    </LogoffReply>
  </WISPAccessGatewayParam>
--> </HTML>


File: /xml\login.html
<HTML> <!--
<?xml version="1.0" encoding="UTF-8"?>
  <WISPAccessGatewayParam
  xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
  xsi:noNamespaceSchemaLocation="http://$(hostname)/xml/WISPAccessGatewayParam.xsd">
    <AuthenticationReply>
	<MessageType>120</MessageType>
	<ResponseCode>
$(if error-type == 'radius-timeout')
		102
$(else)
		100
$(endif)
	</ResponseCode>
$(if error)		<ReplyMessage>$(error)</ReplyMessage>		$(endif)
$(if radius18[1])	<ReplyMessage>$(radius18[1])</ReplyMessage>	$(endif)
$(if radius18[2])	<ReplyMessage>$(radius18[2])</ReplyMessage>	$(endif)
$(if radius18[3])	<ReplyMessage>$(radius18[3])</ReplyMessage>	$(endif)
$(if radius18[4])	<ReplyMessage>$(radius18[4])</ReplyMessage>	$(endif)
    </AuthenticationReply>
  </WISPAccessGatewayParam>
--> </HTML>


File: /xml\logout.html
<HTML> <!--
<?xml version="1.0" encoding="UTF-8"?>
<WISPAccessGatewayParam
  xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
  xsi:noNamespaceSchemaLocation="http://$(hostname)/xml/WISPAccessGatewayParam.xsd">
    <LogoffReply>
	<MessageType>130</MessageType>
	<ResponseCode>150</ResponseCode>
    </LogoffReply>
  </WISPAccessGatewayParam>
--> </HTML>


File: /xml\rlogin.html
<HTML> <!--
<?xml version="1.0" encoding="UTF-8"?>
  <WISPAccessGatewayParam
  xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
  xsi:noNamespaceSchemaLocation="http://$(hostname)/xml/WISPAccessGatewayParam.xsd">
    <Redirect>
	<AccessProcedure>1.0</AccessProcedure>
	<AccessLocation>$(location-id)</AccessLocation>
	<LocationName>$(location-name)</LocationName>
	<LoginURL>$(link-login-only)</LoginURL>
	<MessageType>100</MessageType>
	<ResponseCode>0</ResponseCode>
    </Redirect>
  </WISPAccessGatewayParam>
--> </HTML>


File: /xml\WISPAccessGatewayParam.xsd
<?xml version="1.0" encoding="UTF-8"?>
<xs:schema xmlns:xs="http://www.w3.org/2001/XMLSchema" elementFormDefault="qualified" attributeFormDefault="unqualified">
	<xs:element name="WISPAccessGatewayParam">
		<xs:complexType>
			<xs:choice>
				<xs:element name="Redirect" type="RedirectType"/>
				<xs:element name="Proxy" type="ProxyType"/>
				<xs:element name="AuthenticationReply" type="AuthenticationReplyType"/>
				<xs:element name="AuthenticationPollReply" type="AuthenticationPollReplyType"/>
				<xs:element name="LogoffReply" type="LogoffReplyType"/>
				<xs:element name="AbortLoginReply" type="AbortLoginReplyType"/>
			</xs:choice>
		</xs:complexType>
	</xs:element>
	<xs:simpleType name="AbortLoginURLType">
		<xs:restriction base="xs:anyURI"/>
	</xs:simpleType>
	<xs:simpleType name="NextURLType">
		<xs:restriction base="xs:anyURI"/>
	</xs:simpleType>
	<xs:simpleType name="AccessProcedureType">
		<xs:restriction base="xs:string"/>
	</xs:simpleType>
	<xs:simpleType name="AccessLocationType">
		<xs:restriction base="xs:string"/>
	</xs:simpleType>
	<xs:simpleType name="LocationNameType">
		<xs:restriction base="xs:string"/>
	</xs:simpleType>
	<xs:simpleType name="LoginURLType">
		<xs:restriction base="xs:anyURI"/>
	</xs:simpleType>
	<xs:simpleType name="MessageTypeType">
		<xs:restriction base="xs:integer"/>
	</xs:simpleType>
	<xs:simpleType name="ResponseCodeType">
		<xs:restriction base="xs:integer"/>
	</xs:simpleType>
	<xs:simpleType name="ReplyMessageType">
		<xs:restriction base="xs:string"/>
	</xs:simpleType>
	<xs:simpleType name="LoginResultsURLType">
		<xs:restriction base="xs:anyURI"/>
	</xs:simpleType>
	<xs:simpleType name="LogoffURLType">
		<xs:restriction base="xs:anyURI"/>
	</xs:simpleType>
	<xs:simpleType name="DelayType">
		<xs:restriction base="xs:integer"/>
	</xs:simpleType>
	<xs:complexType name="RedirectType">
		<xs:all>
			<xs:element name="AccessProcedure" type="AccessProcedureType"/>
			<xs:element name="AccessLocation" type="AccessLocationType"/>
			<xs:element name="LocationName" type="LocationNameType"/>
			<xs:element name="LoginURL" type="LoginURLType"/>
			<xs:element name="AbortLoginURL" type="AbortLoginURLType"/>
			<xs:element name="MessageType" type="MessageTypeType"/>
			<xs:element name="ResponseCode" type="ResponseCodeType"/>
		</xs:all>
	</xs:complexType>
	<xs:complexType name="ProxyType">
		<xs:all>
			<xs:element name="MessageType" type="MessageTypeType"/>
			<xs:element name="ResponseCode" type="ResponseCodeType"/>
			<xs:element name="NextURL" type="NextURLType" minOccurs="0" maxOccurs="1"/>
			<xs:element name="Delay" type="DelayType" minOccurs="0" maxOccurs="1"/>
		</xs:all>
	</xs:complexType>
	<xs:complexType name="AuthenticationReplyType">
		<xs:all>
			<xs:element name="MessageType" type="MessageTypeType"/>
			<xs:element name="ResponseCode" type="ResponseCodeType"/>
			<xs:element name="ReplyMessage" type="ReplyMessageType" minOccurs="0" maxOccurs="1"/>
			<xs:element name="LoginResultsURL" type="LoginResultsURLType" minOccurs="0" maxOccurs="1"/>
			<xs:element name="LogoffURL" type="LogoffURLType" minOccurs="0" maxOccurs="1"/>
		</xs:all>
	</xs:complexType>
	<xs:complexType name="AuthenticationPollReplyType">
		<xs:all>
			<xs:element name="MessageType" type="MessageTypeType"/>
			<xs:element name="ResponseCode" type="ResponseCodeType"/>
			<xs:element name="ReplyMessage" type="ReplyMessageType" minOccurs="0" maxOccurs="1"/>
			<xs:element name="Delay" type="DelayType" minOccurs="0" maxOccurs="1"/>
			<xs:element name="LogoffURL" type="LogoffURLType" minOccurs="0" maxOccurs="1"/>
		</xs:all>
	</xs:complexType>
	<xs:complexType name="LogoffReplyType">
		<xs:sequence>
			<xs:element name="MessageType" type="MessageTypeType"/>
			<xs:element name="ResponseCode" type="ResponseCodeType"/>
		</xs:sequence>
	</xs:complexType>
	<xs:complexType name="AbortLoginReplyType">
		<xs:sequence>
			<xs:element name="MessageType" type="MessageTypeType"/>
			<xs:element name="ResponseCode" type="ResponseCodeType"/>
			<xs:element name="LogoffURL" type="LogoffURLType" minOccurs="0" maxOccurs="1"/>
		</xs:sequence>
	</xs:complexType>
</xs:schema>


File: /_config.yml
theme: jekyll-theme-cayman

