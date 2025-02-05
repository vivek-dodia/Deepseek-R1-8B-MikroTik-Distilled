# Repository Information
Name: template-login-hotspot-mikrotik-instagram

# Directory Structure
Directory structure:
└── github_repos/template-login-hotspot-mikrotik-instagram/
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
    │   │       ├── pack-bdbb89e98983445586421c79434a3b70d9b9c225.idx
    │   │       └── pack-bdbb89e98983445586421c79434a3b70d9b9c225.pack
    │   ├── packed-refs
    │   └── refs/
    │       ├── heads/
    │       │   └── master
    │       ├── remotes/
    │       │   └── origin/
    │       │       └── HEAD
    │       └── tags/
    ├── alogin.html
    ├── error.html
    ├── errors-en.txt
    ├── errors.txt
    ├── font/
    │   ├── fontello.eot
    │   ├── fontello.ttf
    │   ├── fontello.woff
    │   └── fontello.woff2
    ├── LICENSE
    ├── login.html
    ├── logout.html
    ├── md5.js
    ├── radvert.html
    ├── readme.md
    ├── redirect.html
    ├── rlogin.html
    ├── service.js
    ├── slider.css
    ├── status.html
    ├── style.css
    └── success.html


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
	url = https://github.com/balinux/template-login-hotspot-mikrotik-instagram.git
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
0000000000000000000000000000000000000000 3167d75429c1781e7ad58579e411d7a3cc2e6713 vivek-dodia <vivek.dodia@icloud.com> 1738606461 -0500	clone: from https://github.com/balinux/template-login-hotspot-mikrotik-instagram.git


File: /.git\logs\refs\heads\master
0000000000000000000000000000000000000000 3167d75429c1781e7ad58579e411d7a3cc2e6713 vivek-dodia <vivek.dodia@icloud.com> 1738606461 -0500	clone: from https://github.com/balinux/template-login-hotspot-mikrotik-instagram.git


File: /.git\logs\refs\remotes\origin\HEAD
0000000000000000000000000000000000000000 3167d75429c1781e7ad58579e411d7a3cc2e6713 vivek-dodia <vivek.dodia@icloud.com> 1738606461 -0500	clone: from https://github.com/balinux/template-login-hotspot-mikrotik-instagram.git


File: /.git\packed-refs
# pack-refs with: peeled fully-peeled sorted 
3167d75429c1781e7ad58579e411d7a3cc2e6713 refs/remotes/origin/master
3167d75429c1781e7ad58579e411d7a3cc2e6713 refs/tags/v1.0.0


File: /.git\refs\heads\master
3167d75429c1781e7ad58579e411d7a3cc2e6713


File: /.git\refs\remotes\origin\HEAD
ref: refs/remotes/origin/master


File: /alogin.html
<!DOCTYPE html>
<html>
<head>
<title id="title"></title>
<meta http-equiv="refresh" content="2; url=$(link-redirect)">
<meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1">
<meta name="theme-color" content="#3B5998" />
<meta name="viewport" content="width=device-width; initial-scale=1.0; maximum-scale=1.0;"/>
<link rel="stylesheet" href="style.css">
<script language="JavaScript">

    function startClock() {
        $(if popup == 'true')
        open('$(link-status)', 'hotspot_status', 'toolbar=0,location=0,directories=0,status=0,menubars=0,resizable=1,width=290,height=200');
	$(endif)
	location.href = './success.html';
    }

</script>
</head>
<body onLoad="startClock()">
<table width="100%" height="100%">
<tr>
	<td align="center" valign="middle">
	Anda telah terhubung
	<br><br>
	Juka belum, <a style="color:blue" href="./login">klik di sini</a></td>
</tr>
</table>
<script type="text/javascript">
	document.getElementById('title').innerHTML = window.location.hostname + " > redirect";
</script>
</body>
</html>


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


File: /errors-en.txt
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

not-logged-in = you are not logged in (ip $(ip))

# ippool-empty
# IP address for user is to be assigned from ip pool, but there are no more
# addresses in that pool

ippool-empty = cannot assign ip address - no more free addresses from pool

# shutting-down
# When shutdown is executed, new clients are not accepted

shutting-down = hotspot service is shutting down

# user-session-limit
# If user profile has limit of shared-users, then this error will be shown
# after reaching this limit

user-session-limit = no more sessions are allowed for user $(username)

# license-session-limit
# Depending on licence number of active hotspot clients is limited to
# one or another amount. If this limit is reached, following error is displayed.

license-session-limit = session limit reached ($(error-orig))

# wrong-mac-username
# If username looks like MAC address (12:34:56:78:9a:bc), but is not
# a MAC address of this client, login is rejected

wrong-mac-username = invalid username ($(username)): this MAC address is not yours

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

chap-missing = web browser did not send challenge response (try again, enable JavaScript)

# invalid-username
# Most general case of invalid username or password. If RADIUS server
# has sent an error string with Access-Reject message, then it will
# override this setting.

invalid-username = invalid username or password

# invalid-mac
# Local users (on hotspot server) can be bound to some MAC address. If login
# from different MAC is tried, this error message will be shown.

invalid-mac = user $(username) is not allowed to log in from this MAC address

# uptime-limit, traffic-limit
# For local hotspot users in case if limits are reached

uptime-limit = user $(username) has reached uptime limit
traffic-limit = user $(username) has reached traffic limit

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

internal-error = error internal ($(error-orig))

# config-error
# Should never happen if hotspot is configured properly.

config-error = error konfigurasi ($(error-orig))

# not-logged-in
# Will happen, if status or logout page is requested by user,
# which actually is not logged in

not-logged-in = Anda tidak masuk (ip $(ip))

# ippool-empty
# IP address for user is to be assigned from ip pool, but there are no more
# addresses in that pool

ippool-empty = cannot assign ip address - no more free addresses from pool

# shutting-down
# When shutdown is executed, new clients are not accepted

shutting-down = layanan hotspot tutup

# user-session-limit
# If user profile has limit of shared-users, then this error will be shown
# after reaching this limit

user-session-limit = kode voucher/user sedang aktif $(username)

# license-session-limit
# Depending on licence number of active hotspot clients is limited to
# one or another amount. If this limit is reached, following error is displayed.

license-session-limit = durasi voucher Anda sudah habis ($(error-orig))

# wrong-mac-username
# If username looks like MAC address (12:34:56:78:9a:bc), but is not
# a MAC address of this client, login is rejected

wrong-mac-username = kode voucher/user tidak sesuai ($(username)): MAC address ini bukan milik Anda

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

chap-missing = web browser did not send challenge response (try again, enable JavaScript)

# invalid-username
# Most general case of invalid username or password. If RADIUS server
# has sent an error string with Access-Reject message, then it will
# override this setting.

invalid-username = kode voucher/user tidak sesuai, masukkan kembali dengan benar.

# invalid-mac
# Local users (on hotspot server) can be bound to some MAC address. If login
# from different MAC is tried, this error message will be shown.

invalid-mac = kode voucher/user $(username) tidak dapat diaktifkan dari MAC address ini

# uptime-limit, traffic-limit
# For local hotspot users in case if limits are reached

uptime-limit = kode voucher/user $(username) sudah mencapai batas waktu
traffic-limit = kode voucher/user $(username) sudah mencapai batas kuota

# radius-timeout
# User is authenticated by RADIUS server, but no response is received from it,
# following error will be shown.

radius-timeout = RADIUS server tidak merespon

# auth-in-progress
# Authorization in progress. Client already has issued an authorization request
# which is not yet complete.

auth-in-progress = sudah diaktifkan, coba lagi nanti

# radius-reply
# Radius server returned some custom error message

radius-reply = $(error-orig)


File: /LICENSE
MIT License

Copyright (c) 2020 balinux

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.


File: /login.html
<!DOCTYPE html>
<html>

<head>
    <title id="title"></title>
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
    <meta name="theme-color" content="#3B5998" />
    <meta name="viewport" content="width=device-width; initial-scale=1.0; maximum-scale=1.0;" />
    <link rel="stylesheet" href="style.css">
    <link rel="stylesheet" href="slider.css">

</head>

<body>
    $(if chap-id)
    <form name="sendin" action="$(link-login-only)" method="post">
        <input type="hidden" name="username" />
        <input type="hidden" name="password" />
        <input type="hidden" name="dst" value="$(link-orig)" />
        <input type="hidden" name="popup" value="true" />
    </form>

    <script type="text/javascript" src="md5.js"></script>
    <script type="text/javascript">
        function doLogin() {
            document.sendin.username.value = document.login.username.value;
            document.sendin.password.value = hexMD5('$(chap-id)' + document.login.password.value +
                '$(chap-challenge)');
            document.sendin.submit();
            return false;
        }
    </script>
    $(endif)

    <div id="main" class="main">

        <div class="box">
            <h3 class="brand">VueNet</h3>
        </div>
        <div class="box">
            <button id="btnvrc" class="small-button" onclick="voucher();"><i class="icon icon-ticket">&#xe802;</i>
                Voucher</button>
            <button id="btnmem" class="small-button" onclick="member();"><i class="icon icon-user-circle-o">&#xf2be;</i>
                Member</button>
            <button id="qr" class="small-button" onclick="window.location='https://laksa19.github.io/myqr';"> <i
                    class="icon icon-qrcode">&#xe801;</i> QR
                Code</button>
        </div>
        <div class="box" id="infologin">
        </div>
        <form autocomplete="off" name="login" action="$(link-login-only)" method="post" $(if chap-id)
            onSubmit="return doLogin()" $(endif)>
            <input type="hidden" name="dst" value="$(link-orig)" />
            <input type="hidden" name="popup" value="true" />
            <input class="username" name="username" type="text" value="$(username)" />
            <input class="password" name="password" placeholder="Password" type="hidden" />

            <button class="button" type="submit"><i class="icon icon-login">&#xe803;</i> Login</button>

        </form>

        $(if trial == 'yes')
        <div class="box">Coba gratis <a style="text-decoration: underline; color:#fff;"
                href="$(link-login-only)?dst=$(link-orig-esc)&amp;username=T-$(mac-esc)">klik
                di sini</a></div>
        $(endif)

        $(if error)<div class="notice">$(error)</div>$(endif)

        <table class="table">
            <caption style="font-size: 16px; font-weight: bold; margin-bottom:5px;">Paket Internet Wifi</caption>
            <tr>
                <th>Paket</th>
                <th>Aktif</th>
                <th>Harga</th>
            </tr>
            <tr>
                <td>15H</td>
                <td>15 hari</td>
                <td>Rp 35.000</td>
            </tr>
            <tr>
                <td>30H</td>
                <td>30 Hari</td>
                <td>Rp 50.000</td>
            </tr>

        </table>
        <br />
        <div>
            Voucher bisa anda dapatkan dengan menghubungi Telegram: @balinux
        </div>
        <br />
        <div id="app">
            <covid19></covid19>
        </div>
        <!-- end app -->
    </div>
    <br />
    <div class="box" style="color:#000;">
        <i>Copyright &copy; 2018 Laksamadi</i><br />
        <i>Powered by <a style="color:#000; text-decoration:underline;" href="https://laksa19.github.io">Mikhmon</a></i><br/>
        <i>Modified by <a style="color:#000; text-decoration:underline;" href="https://yhotie.com">Yho Tie</a></i>
        <!-- Tolong jangan dihilangkan bagian ini-->
    </div>

    <script type="text/javascript">
        var hostname = window.location.hostname;
        document.getElementById('title').innerHTML = hostname + " > login";

        document.login.username.focus();

        var infologin = document.getElementById('infologin');
        infologin.innerHTML = "Masukkan Kode Voucher kemudian klik login.";

        // login page 2 mode by Laksamadi Guko
        var username = document.login.username;
        var password = document.login.password;

        username.placeholder = "Kode Voucher";

        // set password = username
        function setpass() {
            var user = username.value
            //user = user.toLowerCase();
            username.value = user;
            password.value = user;
        }

        username.onkeyup = setpass;

        // change to voucher mode
        function voucher() {
            username.focus();
            username.onkeyup = setpass;
            username.placeholder = "Kode Voucher";
            username.style = "border-radius:3px;"
            password.type = "hidden";
            infologin.innerHTML = "Masukkan Kode Voucher kemudian klik login.";
        }

        // change to member mode
        function member() {
            username.focus();
            username.onkeyup = "";
            username.placeholder = "Username";
            username.style = "border-radius:3px 3px 0px 0px;"
            password.type = "password";
            infologin.innerHTML = "Masukkan Username dan Password kemudian klik login.";
        }
    </script>

    <script type="text/javascript" src="vue.min.js"></script>
    <script type="text/javascript" src="service.js"></script>

    <script type="text/javascript">
        var app = new Vue({
            el: "#app",
        })
    </script>
</body>

</html>

File: /logout.html
<!DOCTYPE html>
<html>
<head>
<title id="title"></title>
<meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1">
<meta name="theme-color" content="#3B5998" />
<meta name="viewport" content="width=device-width; initial-scale=1.0; maximum-scale=1.0;"/>
<link rel="stylesheet" href="style.css">
</head>

<body>
<script language="JavaScript">

    function openLogin() {
	if (window.name != 'hotspot_logout') return true;
	open('$(link-login)', '_blank', '');
	window.close();
	return false;
    }

</script>

<div class="main">
<div class="box">
    <div style="margin-top:30px; text-align: center;"><i style="font-size:50px;" class="icon icon-user-circle-o">&#xf2be;</i> <h3 id="user">$(username)</h3></div><br>
    <b style="margin-top:20px;">Anda telah keluar dari hotspot!</b> <br><br>
</div>
<table class="table2">
    <tr><td align="right">IP Address  <i class="icon icon-sitemap">&#xf0e8;</i> </td><td>$(ip)</td></tr>
    <tr><td align="right">MAC Address <i class="icon icon-barcode">&#xe80a;</i>  </td><td>$(mac)</td></tr>
    <tr><td align="right">Terkoneksi <i class="icon icon-exchange">&#xf0ec;</i> </td><td>$(uptime)</td></tr>
    <tr><td align="right">Upload <i class="icon icon-upload">&#xe808;</i> </td><td>$(bytes-in-nice)</td></tr>
    <tr><td align="right">Download <i class="icon icon-download">&#xe809;</i> </td><td>$(bytes-out-nice)</td></tr>
$(if remain-bytes-total)
    <tr><td align="right">Sisa Kuota <i class="icon icon-hourglass-2">&#xf252;</i> </td><td>$(remain-bytes-total-nice)</td></tr>
$(endif)
$(if session-time-left)
    <tr><td align="right">Sisa Waktu <i class="icon icon-clock">&#xe805;</i> </td><td>$(session-time-left)</td></tr>
$(endif)
</table>
<br>
<form action="$(link-login)" name="login" onSubmit="return openLogin()">
        <button class="button" type="submit"><i class="icon icon-login">&#xe803;</i> Login Kembali</button>
</form>
</div>
<script type="text/javascript">
	document.getElementById('title').innerHTML = window.location.hostname + " > logout";
</script>
</body>
</html>


File: /md5.js
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


File: /readme.md

## Membuat login Member menjadi default
Edit file login.html di baris 14 menjadi 
```
<body onload="member();">
```

## Input otomatis huruf kecil (auto lowercase) mode voucher dan member
Edit file login.html mulai baris 120 -> 148
```
// set password = username
function setpass(){
  var user = username.value		
  password.value = user;
}
username.onkeyup = setpass; 
// change to voucher mode
function voucher(){
  username.focus();
  username.onkeyup = setpass;
  username.placeholder = "Kode Voucher";
  username.style = "border-radius:3px;"
  password.type = "hidden";
  infologin.innerHTML  = "Masukkan Kode Voucher kemudian klik login.";
}
// change to member mode
function member(){
  username.focus();
  username.onkeyup = "";
  username.placeholder = "Username";
  username.style = "border-radius:3px 3px 0px 0px;"
  password.type = "password";	
  infologin.innerHTML  = "Masukkan Username dan Password kemudian klik login.";
}
//-->


```
menjadi
```
//set lowercase
function setlower(){
var cekMode = password.type;
if (cekMode === "hidden"){
  var user = username.value 
  user = user.toLowerCase();
  username.value = user;  
  password.value = user;
} else if (cekMode === "password"){
  var user = username.value 
  user = user.toLowerCase();
  username.value = user;
} 
}

username.onkeyup = setlower;

// change to voucher mode
function voucher(){
  username.focus();
  username.placeholder = "Kode Voucher";
  username.style = "border-radius:3px;"
  password.type = "hidden";
  password.value = username.value;
  infologin.innerHTML  = "Masukkan Kode Voucher kemudian klik login.";
}

// change to member mode
function member(){
  username.focus();
  username.placeholder = "Username";
  username.style = "border-radius:3px 3px 0px 0px;"
  password.type= "password";
  password.value = "";
  infologin.innerHTML  = "Masukkan Username dan Password kemudian klik login.";
}
//-->

```
## Fitur QR Code Scanner

Untuk menggunakan fitur QR CODE SCANNER Anda perlu menambahkan script berikut di MikroTik via Terminal.
```
/ip hotspot walled-garden ip

add action=accept comment="Mikhmon QR Code Scanner" disabled=no dst-host=laksa19.github.io

```

Centang HTTP PAP di hotspot server profile.

## Fitur Informasi Covid19

Untuk menambah fitur informasi Covid19 di halaman login Anda perlu menambahkan script berikut di MikroTik via Terminal
```
/ip hotspot walled-garden ip

add action=accept comment="Covid19 information" disabled=no dst-host=indonesia-covid-19.mathdro.id

```

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


File: /service.js
Vue.component("covid19",{data:function(){return{covid2:null}},created(){this.getData()},methods:{getData:function(){fetch("https://indonesia-covid-19.mathdro.id/api").then(t=>t.json()).then(t=>{this.covid2=t})}},template:' <table class="table"> <caption style="font-size: 16px; font-weight: bold; margin-bottom:5px;">Informasi Covid19 indonesia</caption> <tr> <th>Positif</th> <th>Sembuh</th> <th>Meninggal</th> </tr><tr v-if="covid2 !==null"> <td>{{covid2.jumlahKasus}}</td><td>{{covid2.sembuh}}</td><td>{{covid2.meninggal}}</td></tr></table>'}),Vue.component("yhotie-ig-banner",{props:{username:String,header:String},data:function(){return{imgIgCollection:[]}},created(){this.getInstagaramPost()},methods:{getInstagaramPost:function(){fetch(`https://www.instagram.com/${this.username}/?__a=1`).then(t=>t.json()).then(async t=>{const{edge_owner_to_timeline_media:e}=await t.graphql.user;this.imgIgCollection=[...this.imgIgCollection,...e.edges]}).then(()=>{0!=this.imgIgCollection.length&&this.getSlide()})},getSlide:function(){var t=0;!function e(){var i;var n=document.getElementsByClassName("mySlides");var a=document.getElementsByClassName("dot");for(i=0;i<n.length;i++)n[i].style.display="none";t++;t>n.length&&(t=1);for(i=0;i<a.length;i++)a[i].className=a[i].className.replace(" active","");n[t-1].style.display="block";a[t-1].className+=" active";setTimeout(e,3e3)}()}},template:' <div> <br/> <div style="font-size: 16px; font-weight: bold;   text-align: center; margin-bottom:5px;">{{header}}</div> <div class="slideshow-container"> <div v-for="(item, index) in imgIgCollection" :key="index" class="mySlides fade"> <div class="numbertext">{{index+1}}/{{imgIgCollection.length}}</div><img :src="item.node.display_url" style="width:100%"> </div></div><br/> <div style="text-align:center"> <span v-for="(item, index) in imgIgCollection" :key="index" class="dot"></span> <span class="dot"></span> </div></div>'});

File: /slider.css
* {
    box-sizing: border-box;
}

body {
    font-family: Verdana, sans-serif;
}

.mySlides {
    display: none;
}

img {
    vertical-align: middle;
}

/* Slideshow container */
.slideshow-container {
    max-width: 1000px;
    position: relative;
    margin: auto;
}

/* Caption text */
.text {
    color: #f2f2f2;
    font-size: 15px;
    padding: 8px 12px;
    position: absolute;
    bottom: 8px;
    width: 100%;
    text-align: center;
}

/* Number text (1/3 etc) */
.numbertext {
    color: #f2f2f2;
    font-size: 12px;
    padding: 8px 12px;
    position: absolute;
    top: 0;
}

/* The dots/bullets/indicators */
.dot {
    height: 15px;
    width: 15px;
    margin: 0 2px;
    background-color: #bbb;
    border-radius: 50%;
    display: inline-block;
    transition: background-color 0.6s ease;
}

.active {
    background-color: #717171;
}

/* Fading animation */
.fade {
    -webkit-animation-name: fade;
    -webkit-animation-duration: 1.5s;
    animation-name: fade;
    animation-duration: 1.5s;
}

@-webkit-keyframes fade {
    from {
        opacity: .4
    }

    to {
        opacity: 1
    }
}

@keyframes fade {
    from {
        opacity: .4
    }

    to {
        opacity: 1
    }
}

/* On smaller screens, decrease text size */
@media only screen and (max-width: 300px) {
    .text {
        font-size: 11px
    }
}

File: /status.html
<!DOCTYPE html>
<html>
<head>
<title id="title"></title>
$(if refresh-timeout)
<meta http-equiv="refresh" content="$(refresh-timeout-secs)">
$(endif)
<meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1">
<meta name="theme-color" content="#3B5998" />
<meta name="viewport" content="width=device-width; initial-scale=1.0; maximum-scale=1.0;"/>
<link rel="stylesheet" href="style.css">
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
<body $(if advert-pending == 'yes')	onLoad="openAdvert()" $(endif) >
<div class="main">
<form action="$(link-logout)" name="logout" onSubmit="return openLogout()">

$(if login-by == 'trial')
	<div style="margin-top:20px; text-align: center;"><h3>Welcome</h3><i style="font-size:50px;" class="icon icon-user-circle-o">&#xf2be;</i> <h3>trial user</h3></div><br>
$(elif login-by != 'mac')
	<div style="margin-top:20px; text-align: center;"><h3>Welcome</h3><i style="font-size:50px;" class="icon icon-user-circle-o">&#xf2be;</i> <h3 id="user">$(username)</h3></div><br>
$(endif)
<table class="table2">
	<tr><td align="right" style="width: 40%;">IP Address <i class="icon icon-sitemap">&#xf0e8;</i> </td><td>$(ip)</td></tr>
    <tr><td align="right">MAC Address <i class="icon icon-barcode">&#xe80a;</i> </td><td>$(mac)</td></tr>
    <tr><td align="right">Upload <i class="icon icon-upload">&#xe808;</i> </td><td>$(bytes-in-nice)</td></tr>
    <tr><td align="right">Download <i class="icon icon-download">&#xe809;</i> </td><td>$(bytes-out-nice)</td></tr>
	<tr><td align="right">Terkoneksi <i class="icon icon-exchange">&#xf0ec;</i> </td><td>$(uptime)</td></tr>
$(if remain-bytes-total)
    <tr><td align="right">Sisa Kuota <i class="icon icon-hourglass-2">&#xf252;</i> </td><td>$(remain-bytes-total-nice)</td></tr>
$(endif)
$(if session-time-left)
    <tr><td align="right">Sisa Waktu <i class="icon icon-clock">&#xe805;</i> </td><td>$(session-time-left)</td></tr>
$(endif)
$(if blocked == 'yes')
	<tr><td align="right">Status <i class="icon icon-check">&#xe807;</i> </td><td><div style="color: #FF8080">
<a href="$(link-advert)" target="hotspot_advert">advertisement</a> required</div></td></tr>
$(elif refresh-timeout)
	<tr><td align="right">Refresh <i <i class="icon icon-arrows-cw">&#xe800;</i> </td><td>$(refresh-timeout)</td></tr>
$(endif)
    <tr><td align="right">Expired <i <i class="icon icon-calendar">&#xe806;</i> </td><td style="padding-top:0px; padding-left:2px;"><iframe id="exp" frameborder="0" scrolling="no" src="about:blank"></iframe></td></tr>

</table>

<div id="app">
    <br/>
    <covid19></covid19>
    <yhotie-ig-banner username="balinux" header="Informasi Iklan"></yhotie-ig-banner>
</div>

$(if login-by-mac != 'yes')
<br>
<!-- user manager link. if user manager resides on other router, replace $(hostname) by its address
<button onclick="document.location='http://$(hostname)/user?subs='; return false;">status</button>
<!-- end of user manager link -->
<button class="button2" type="submit"><i class="icon icon-logout">&#xe804;</i> Logout</button>
$(endif)
</form>
</div>
<script type="text/javascript">
    document.getElementById('title').innerHTML = window.location.hostname + " > status";
//get vaidity
    var usr = document.getElementById('user').innerHTML
    var url = "https://example.com/status/status.php?name="; // http://ip-server-mikhmon/mikhmonv2/status/status.php?name=
    var SessionName = "wifijoss"
    var getvalid = url+usr+"&session="+SessionName
    document.getElementById('exp').src = getvalid;
        
</script>
<script type="text/javascript" src="vue.min.js"></script>
<script type="text/javascript" src="service.js"></script>

<script type="text/javascript">
    var app = new Vue({
        el: "#app",
    })
</script>
</body>
</html>


File: /style.css
body {
  font-family: -apple-system, BlinkMacSystemFont, "segoe ui", Verdana, Roboto, "helvetica neue", Arial, sans-serif, "apple color emoji";
  font-size: 14px; 
  margin: 0;
}

@font-face {
  font-family: 'fontello';
  src: url('./font/fontello.eot?78273339');
  src: url('./font/fontello.eot?78273339#iefix') format('embedded-opentype'),
       url('./font/fontello.woff?78273339') format('woff'),
       url('./font/fontello.ttf?78273339') format('truetype'),
       url('./font/fontello.svg?78273339#fontello') format('svg');
  font-weight: normal;
  font-style: normal;
}
 
 
.icon
{
  font-family: "fontello";
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

iframe  {
  float:left; 
  height:22px; 
  width:100%;
}
.main{
  background: #097486;
  color: #f2f2f2;
  max-width: 300px;
  height: 100%;
  border-radius:5px;
  padding: 10px;
  margin-top: 10%;
  margin-left:auto;
  margin-right:auto;
  transition: 0.3s;
  text-align:center;
  min-height:300px;
  animation: fadein 1s;
  -moz-animation: fadein 1s; /* Firefox */
  -webkit-animation: fadein 1s; /* Safari and Chrome */
  -o-animation: fadein 1s; /* Opera */
}

.box{
  margin-bottom:10px;
  text-align:center;
}

.brand{
  color:#ffffff;
  padding:0px;
  margin:10px;
  font-size:35px;
  border-bottom: solid 2px #fff;
}

.username {
  background-color: #FDFBFB;
  border: none;
  border-radius:3px;
  border-bottom: 1px solid #f2f2f2;
  text-align:center;
  font-size: 16px;
  color: #000000;
  outline: none;
  width: 100%;
  height: 35px;
}

.password {
  background-color: #FDFBFB;
  border: none;
  border-radius:0px 0px 3px 3px;
  border-top: 1px solid #f2f2f2;
  text-align:center;
  font-size: 16px;
  color: #000000;
  outline: none;
  width: 100%;
  height: 35px;
}

.button {
  background-color: #d9d9d9;
  background-image: linear-gradient(#d9d9d9, #e6e6e6, #d9d9d9);
  border: none;
  border-radius:3px;
  color: #595959;
  font-weight: bold;
  text-align: center;
  vertical-align: middle;
  text-decoration: none;
  display: inline-block;
  font-size: 16px;
  margin-top: 10px;
  margin-bottom: 10px;
  cursor: pointer;
  width: 100%;
  height: 40px;
}
.button:hover{
  font-weight:bold;
  box-shadow: 0 10px 15px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19);
}

.button2 {
  background-color: #d32f2f;
  background-image: linear-gradient(#d32f2f, #ef5350, #d32f2f);
  border: none;
  border-radius:3px;
  color: #f2f2f2;
  font-weight: bold;
  text-align: center;
  vertical-align: middle;
  text-decoration: none;
  display: inline-block;
  font-size: 16px;
  margin-top: 10px;
  margin-bottom: 10px;
  cursor: pointer;
  width: 100%;
  height: 40px;
}
.button2:hover{
  font-weight:bold;
  box-shadow: 0 10px 15px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19);
}


.small-button {
  background-color: #d9d9d9;
  background-image: linear-gradient(#d9d9d9, #e6e6e6, #d9d9d9);
  border: none;
  border-radius:3px;
  color: #595959;
  font-weight: bold;
  text-align: center;
  vertical-align: middle;
  text-decoration: none;
  display: inline-block;
  cursor: pointer;
  height: 30px;
  width : 32%;
}

.notice{
  background-color:#fff8e1;
  border-radius:3px;
  padding:5px;
  margin-bottom:10px;
  font-size:14px;
  color: #000;
}
.table {
  width: 100%;
  border-collapse: collapse !important;
}
.table td,
.table th {
  padding: 5px;
  border: 1px solid #f2f2f2 !important;
  color:  #f3f4f5;
}

.table td, th, a{
  color: #f3f4f5;
  text-decoration: none;
}

.table2 {
  width: 100%;
  border-collapse: collapse !important;
  background-color: #fff;
  text-align:left;
}
.table2 td,
.table2 th {
  padding: 5px;
  border: 1px solid #000 !important;
}

.table2 td, th, a{
  color: #000;
  text-decoration: none;
}

@keyframes fadein {
  from {opacity:0;}
  to {opacity: 1;}
}
@-moz-keyframes fadein { /* Firefox */
  from {opacity:0;}
  to {opacity: 1;}
}
@-webkit-keyframes fadein { /* Safari and Chrome */
  from {opacity:0;}
  to {opacity: 1;}
}
@-o-keyframes fadein { /* Opera */
  from {opacity:0;}
  to {opacity: 1;}
}

/* @media */
@media screen and (max-width: 600px) {
  .main{
	width:90%;
    margin-top: 10%;
}}

/* @media */
@media screen and (min-width: 600px) {
  .main{
	margin-top: 2%;
}}


File: /success.html
<!DOCTYPE html>
<html>
<head>
<title id="title"></title>
<meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1">
<meta name="theme-color" content="#3B5998" />
<meta name="viewport" content="width=device-width; initial-scale=1.0; maximum-scale=1.0;"/>
<link rel="stylesheet" href="style.css">
$(if refresh-timeout)
<script>
	setTimeout(function(){
	location.href = './status';
	},4000)
</script>
$(endif)
</head>
<body>
<div class="main">

$(if login-by == 'trial')
		<div style="margin-top:20px; text-align: center;"><h3>Welcome</h3><i style="font-size:150px;" class="icon icon-user-circle-o">&#xf2be;</i> <h3>trial user</h3></div><br>
	$(elif login-by != 'mac')
		<div style="margin-top:20px; text-align: center;"><h3>Welcome</h3><i style="font-size:150px;" class="icon icon-user-circle-o">&#xf2be;</i><br> <h3 id="user">$(username)</h3></div><br>
$(endif)
<h3>Anda telah terhubung di jaringan <br /><b id="dname"></b></h3>
<button class="button" onclick="window.location='./status'"><i class="icon icon-check">&#xe807;</i> Check Status</buton>
</div>
<script type="text/javascript">
	document.getElementById('title').innerHTML = window.location.hostname + " > success";	
    document.getElementById('dname').innerHTML = window.location.hostname;	
</script>
</body>
</html>


