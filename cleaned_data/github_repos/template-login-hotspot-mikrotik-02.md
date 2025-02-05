# Repository Information
Name: template-login-hotspot-mikrotik-02

# Directory Structure
Directory structure:
└── github_repos/template-login-hotspot-mikrotik-02/
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
    │   │       ├── pack-344e77fd10cb1daf92e085bd723656b5e51096e0.idx
    │   │       └── pack-344e77fd10cb1daf92e085bd723656b5e51096e0.pack
    │   ├── packed-refs
    │   └── refs/
    │       ├── heads/
    │       │   └── main
    │       ├── remotes/
    │       │   └── origin/
    │       │       └── HEAD
    │       └── tags/
    ├── alogin.html
    ├── assets/
    │   ├── css/
    │   │   └── app.css
    │   ├── fonts/
    │   │   └── lpmq.ttf
    │   └── js/
    │       ├── app.js
    │       ├── config.js
    │       └── md5.js
    ├── error.html
    ├── login.html
    ├── logout.html
    ├── public/
    │   └── icons/
    ├── radvert.html
    ├── README.md
    ├── redirect.html
    ├── rlogin.html
    └── status.html


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
	url = https://github.com/eriiksanjaya/template-login-hotspot-mikrotik-02.git
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
0000000000000000000000000000000000000000 0de476087027fbde22167ec01eac6ef7f3ce9256 vivek-dodia <vivek.dodia@icloud.com> 1738606330 -0500	clone: from https://github.com/eriiksanjaya/template-login-hotspot-mikrotik-02.git


File: /.git\logs\refs\heads\main
0000000000000000000000000000000000000000 0de476087027fbde22167ec01eac6ef7f3ce9256 vivek-dodia <vivek.dodia@icloud.com> 1738606330 -0500	clone: from https://github.com/eriiksanjaya/template-login-hotspot-mikrotik-02.git


File: /.git\logs\refs\remotes\origin\HEAD
0000000000000000000000000000000000000000 0de476087027fbde22167ec01eac6ef7f3ce9256 vivek-dodia <vivek.dodia@icloud.com> 1738606330 -0500	clone: from https://github.com/eriiksanjaya/template-login-hotspot-mikrotik-02.git


File: /.git\packed-refs
# pack-refs with: peeled fully-peeled sorted 
0de476087027fbde22167ec01eac6ef7f3ce9256 refs/remotes/origin/main


File: /.git\refs\heads\main
0de476087027fbde22167ec01eac6ef7f3ce9256


File: /.git\refs\remotes\origin\HEAD
ref: refs/remotes/origin/main


File: /alogin.html
<html>

<head>
  <title>mikrotik hotspot > redirect</title>
  <meta http-equiv="refresh" content="2; url=$(link-redirect)">
  <meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1">
  <meta http-equiv="pragma" content="no-cache">
  <meta http-equiv="expires" content="-1">
  <style type="text/css">
    <!--
    textarea,
    input,
    select {
      background-color: #FDFBFB;
      border: 1px #BBBBBB solid;
      padding: 2px;
      margin: 1px;
      font-size: 14px;
      color: #808080;
    }

    body {
      color: #737373;
      font-size: 12px;
      font-family: verdana;
    }

    a,
    a:link,
    a:visited,
    a:active {
      color: #AAAAAA;
      text-decoration: none;
      font-size: 12px;
    }

    a:hover {
      border-bottom: 1px dotted #c1c1c1;
      color: #AAAAAA;
    }

    img {
      border: none;
    }

    td {
      font-size: 12px;
      color: #7A7A7A;
    }
    -->
  </style>
  <script language="JavaScript">
< !--
      function startClock() {
        $(if popup == 'true')
          open('$(link-status)', 'hotspot_status', 'toolbar=0,location=0,directories=0,status=0,menubars=0,resizable=1,width=290,height=200');
        $(endif)
        location.href = '$(link-redirect)';
      }
//-->
  </script>
</head>

<body onLoad="startClock()">
  <table width="100%" height="100%">
    <tr>
      <td align="center" valign="middle">
        You are logged in
        <br><br>
        If nothing happens, click <a href="$(link-redirect)">here</a>
      </td>
    </tr>
  </table>
</body>

</html>

File: /assets\css\app.css
/*! tailwindcss v2.2.19 | MIT License | https://tailwindcss.com*/

/*! modern-normalize v1.1.0 | MIT License | https://github.com/sindresorhus/modern-normalize */html{-moz-tab-size:4;-o-tab-size:4;tab-size:4;line-height:1.15;-webkit-text-size-adjust:100%}body{margin:0;font-family:system-ui,-apple-system,Segoe UI,Roboto,Helvetica,Arial,sans-serif,Apple Color Emoji,Segoe UI Emoji}hr{height:0;color:inherit}abbr[title]{-webkit-text-decoration:underline dotted;text-decoration:underline dotted}b,strong{font-weight:bolder}code,kbd,pre,samp{font-family:ui-monospace,SFMono-Regular,Consolas,Liberation Mono,Menlo,monospace;font-size:1em}small{font-size:80%}sub,sup{font-size:75%;line-height:0;position:relative;vertical-align:initial}sub{bottom:-.25em}sup{top:-.5em}table{text-indent:0;border-color:inherit}button,input,optgroup,select,textarea{font-family:inherit;font-size:100%;line-height:1.15;margin:0}button,select{text-transform:none}[type=button],[type=reset],[type=submit],button{-webkit-appearance:button}::-moz-focus-inner{border-style:none;padding:0}:-moz-focusring{outline:1px dotted ButtonText}:-moz-ui-invalid{box-shadow:none}legend{padding:0}progress{vertical-align:initial}::-webkit-inner-spin-button,::-webkit-outer-spin-button{height:auto}[type=search]{-webkit-appearance:textfield;outline-offset:-2px}::-webkit-search-decoration{-webkit-appearance:none}::-webkit-file-upload-button{-webkit-appearance:button;font:inherit}summary{display:list-item}blockquote,dd,dl,figure,h1,h2,h3,h4,h5,h6,hr,p,pre{margin:0}button{background-color:initial;background-image:none}fieldset,ol,ul{margin:0;padding:0}ol,ul{list-style:none}html{font-family:ui-sans-serif,system-ui,-apple-system,BlinkMacSystemFont,Segoe UI,Roboto,Helvetica Neue,Arial,Noto Sans,sans-serif,Apple Color Emoji,Segoe UI Emoji,Segoe UI Symbol,Noto Color Emoji;line-height:1.5}body{font-family:inherit;line-height:inherit}*,:after,:before{box-sizing:border-box;border:0 solid}hr{border-top-width:1px}img{border-style:solid}textarea{resize:vertical}input::-moz-placeholder,textarea::-moz-placeholder{opacity:1;color:#9ca3af}input:-ms-input-placeholder,textarea:-ms-input-placeholder{opacity:1;color:#9ca3af}input::placeholder,textarea::placeholder{opacity:1;color:#9ca3af}[role=button],button{cursor:pointer}:-moz-focusring{outline:auto}table{border-collapse:collapse}h1,h2,h3,h4,h5,h6{font-size:inherit;font-weight:inherit}a{color:inherit;text-decoration:inherit}button,input,optgroup,select,textarea{padding:0;line-height:inherit;color:inherit}code,kbd,pre,samp{font-family:ui-monospace,SFMono-Regular,Menlo,Monaco,Consolas,Liberation Mono,Courier New,monospace}audio,canvas,embed,iframe,img,object,svg,video{display:block;vertical-align:middle}img,video{max-width:100%;height:auto}[hidden]{display:none}*,:after,:before{--tw-border-opacity:1;border-color:rgba(229,231,235,var(--tw-border-opacity));--tw-ring-inset:var(--tw-empty,/*!*/ /*!*/);--tw-ring-offset-width:0px;--tw-ring-offset-color:#fff;--tw-ring-color:rgba(59,130,246,0.5);--tw-ring-offset-shadow:0 0 #0000;--tw-ring-shadow:0 0 #0000;--tw-shadow:0 0 #0000}.container{width:100%}@media (min-width:640px){.container{max-width:640px}}@media (min-width:768px){.container{max-width:768px}}@media (min-width:1024px){.container{max-width:1024px}}@media (min-width:1280px){.container{max-width:1280px}}@media (min-width:1536px){.container{max-width:1536px}}.row-span-2{grid-row:span 2/span 2}.mx-3{margin-left:.75rem;margin-right:.75rem}.mt-3{margin-top:.75rem}.block{display:block}.flex{display:flex}.grid{display:grid}.hidden{display:none}.h-screen{height:100vh}.h-full{height:100%}.h-16{height:4rem}.h-8{height:2rem}.h-4{height:1rem}.h-20{height:5rem}.h-12{height:3rem}.h-1{height:.25rem}.h-3{height:.75rem}.h-28{height:7rem}.w-screen{width:100vw}.w-16{width:4rem}.w-8{width:2rem}.w-4{width:1rem}.w-12{width:3rem}.w-full{width:100%}.w-5{width:1.25rem}.w-10{width:2.5rem}.w-14{width:3.5rem}.w-3{width:.75rem}.min-w-0{min-width:0}.max-w-full{max-width:100%}.flex-none{flex:none}.flex-auto{flex:1 1 auto}@-webkit-keyframes bounce{0%,to{transform:translateY(-25%);-webkit-animation-timing-function:cubic-bezier(.8,0,1,1);animation-timing-function:cubic-bezier(.8,0,1,1)}50%{transform:none;-webkit-animation-timing-function:cubic-bezier(0,0,.2,1);animation-timing-function:cubic-bezier(0,0,.2,1)}}@keyframes bounce{0%,to{transform:translateY(-25%);-webkit-animation-timing-function:cubic-bezier(.8,0,1,1);animation-timing-function:cubic-bezier(.8,0,1,1)}50%{transform:none;-webkit-animation-timing-function:cubic-bezier(0,0,.2,1);animation-timing-function:cubic-bezier(0,0,.2,1)}}.animate-bounce{-webkit-animation:bounce 1s infinite;animation:bounce 1s infinite}@-webkit-keyframes pulse{50%{opacity:.5}}@keyframes pulse{50%{opacity:.5}}.animate-pulse{-webkit-animation:pulse 2s cubic-bezier(.4,0,.6,1) infinite;animation:pulse 2s cubic-bezier(.4,0,.6,1) infinite}.select-all{-webkit-user-select:all;-moz-user-select:all;user-select:all}.grid-cols-1{grid-template-columns:repeat(1,minmax(0,1fr))}.grid-cols-6{grid-template-columns:repeat(6,minmax(0,1fr))}.grid-cols-2{grid-template-columns:repeat(2,minmax(0,1fr))}.grid-cols-3{grid-template-columns:repeat(3,minmax(0,1fr))}.grid-cols-4{grid-template-columns:repeat(4,minmax(0,1fr))}.grid-cols-5{grid-template-columns:repeat(5,minmax(0,1fr))}.grid-cols-7{grid-template-columns:repeat(7,minmax(0,1fr))}.grid-cols-8{grid-template-columns:repeat(8,minmax(0,1fr))}.grid-cols-9{grid-template-columns:repeat(9,minmax(0,1fr))}.grid-cols-10{grid-template-columns:repeat(10,minmax(0,1fr))}.grid-rows-5{grid-template-rows:repeat(5,minmax(0,1fr))}.flex-col{flex-direction:column}.items-center{align-items:center}.justify-end{justify-content:flex-end}.justify-center{justify-content:center}.justify-between{justify-content:space-between}.gap-1{gap:.25rem}.gap-3{gap:.75rem}.space-y-2>:not([hidden])~:not([hidden]){--tw-space-y-reverse:0;margin-top:calc(.5rem*(1 - var(--tw-space-y-reverse)));margin-bottom:calc(.5rem*var(--tw-space-y-reverse))}.space-x-3>:not([hidden])~:not([hidden]){--tw-space-x-reverse:0;margin-right:calc(.75rem*var(--tw-space-x-reverse));margin-left:calc(.75rem*(1 - var(--tw-space-x-reverse)))}.space-y-3>:not([hidden])~:not([hidden]){--tw-space-y-reverse:0;margin-top:calc(.75rem*(1 - var(--tw-space-y-reverse)));margin-bottom:calc(.75rem*var(--tw-space-y-reverse))}.space-x-3\.5>:not([hidden])~:not([hidden]){--tw-space-x-reverse:0;margin-right:calc(.875rem*var(--tw-space-x-reverse));margin-left:calc(.875rem*(1 - var(--tw-space-x-reverse)))}.space-y-0\.5>:not([hidden])~:not([hidden]){--tw-space-y-reverse:0;margin-top:calc(.125rem*(1 - var(--tw-space-y-reverse)));margin-bottom:calc(.125rem*var(--tw-space-y-reverse))}.space-y-0>:not([hidden])~:not([hidden]){--tw-space-y-reverse:0;margin-top:calc(0px*(1 - var(--tw-space-y-reverse)));margin-bottom:calc(0px*var(--tw-space-y-reverse))}.space-x-12>:not([hidden])~:not([hidden]){--tw-space-x-reverse:0;margin-right:calc(3rem*var(--tw-space-x-reverse));margin-left:calc(3rem*(1 - var(--tw-space-x-reverse)))}.space-x-1>:not([hidden])~:not([hidden]){--tw-space-x-reverse:0;margin-right:calc(.25rem*var(--tw-space-x-reverse));margin-left:calc(.25rem*(1 - var(--tw-space-x-reverse)))}.space-y-1>:not([hidden])~:not([hidden]){--tw-space-y-reverse:0;margin-top:calc(.25rem*(1 - var(--tw-space-y-reverse)));margin-bottom:calc(.25rem*var(--tw-space-y-reverse))}.overflow-hidden{overflow:hidden}.overflow-x-auto{overflow-x:auto}.overflow-y-auto{overflow-y:auto}.truncate{overflow:hidden;text-overflow:ellipsis;white-space:nowrap}.rounded-3xl{border-radius:30px}.rounded-full{border-radius:9999px}.rounded-md{border-radius:.25rem}.rounded-xl{border-radius:10px}.rounded-lg{border-radius:.5rem}.rounded-t-xl{border-top-left-radius:10px;border-top-right-radius:10px}.rounded-b-3xl{border-bottom-right-radius:30px;border-bottom-left-radius:30px}.rounded-b-xl{border-bottom-right-radius:10px;border-bottom-left-radius:10px}.rounded-bl-50{border-bottom-left-radius:50px}.rounded-tr-none{border-top-right-radius:0}.rounded-tr-50{border-top-right-radius:50px}.border-2{border-width:2px}.border-l-4{border-left-width:4px}.border-t{border-top-width:1px}.border-l{border-left-width:1px}.border-solid{border-style:solid}.border-dashed{border-style:dashed}.border-cyan-600{--tw-border-opacity:1;border-color:rgba(8,145,178,var(--tw-border-opacity))}.border-lime-500{--tw-border-opacity:1;border-color:rgba(132,204,22,var(--tw-border-opacity))}.border-sky-600{--tw-border-opacity:1;border-color:rgba(2,132,199,var(--tw-border-opacity))}.border-red-400{--tw-border-opacity:1;border-color:rgba(248,113,113,var(--tw-border-opacity))}.border-amber-400{--tw-border-opacity:1;border-color:rgba(251,191,36,var(--tw-border-opacity))}.bg-coolGray-700{--tw-bg-opacity:1;background-color:rgba(55,65,81,var(--tw-bg-opacity))}.bg-coolGray-100{--tw-bg-opacity:1;background-color:rgba(243,244,246,var(--tw-bg-opacity))}.bg-sky-600{--tw-bg-opacity:1;background-color:rgba(2,132,199,var(--tw-bg-opacity))}.bg-blueGray-800{--tw-bg-opacity:1;background-color:rgba(30,41,59,var(--tw-bg-opacity))}.bg-white{--tw-bg-opacity:1;background-color:rgba(255,255,255,var(--tw-bg-opacity))}.bg-black{--tw-bg-opacity:1;background-color:rgba(0,0,0,var(--tw-bg-opacity))}.bg-coolGray-800{--tw-bg-opacity:1;background-color:rgba(31,41,55,var(--tw-bg-opacity))}.bg-gray-900{--tw-bg-opacity:1;background-color:rgba(17,24,39,var(--tw-bg-opacity))}.bg-gray-100{--tw-bg-opacity:1;background-color:rgba(243,244,246,var(--tw-bg-opacity))}.bg-coolGray-900{--tw-bg-opacity:1;background-color:rgba(17,24,39,var(--tw-bg-opacity))}.bg-coolGray-500{--tw-bg-opacity:1;background-color:rgba(107,114,128,var(--tw-bg-opacity))}.bg-opacity-50{--tw-bg-opacity:0.5}.bg-opacity-80{--tw-bg-opacity:0.8}.bg-opacity-10{--tw-bg-opacity:0.1}.bg-opacity-100{--tw-bg-opacity:1}.bg-opacity-20{--tw-bg-opacity:0.2}.bg-gradient-to-r{background-image:linear-gradient(to right,var(--tw-gradient-stops))}.from-cyan-600{--tw-gradient-from:#0891b2;--tw-gradient-stops:var(--tw-gradient-from),var(--tw-gradient-to,rgba(8,145,178,0))}.to-teal-500{--tw-gradient-to:#14b8a6}.stroke-current{stroke:currentColor}.p-1{padding:.25rem}.py-3{padding-top:.75rem;padding-bottom:.75rem}.px-3{padding-left:.75rem;padding-right:.75rem}.px-2{padding-left:.5rem;padding-right:.5rem}.py-2{padding-top:.5rem;padding-bottom:.5rem}.py-1{padding-top:.25rem;padding-bottom:.25rem}.py-6{padding-top:1.5rem;padding-bottom:1.5rem}.pt-3{padding-top:.75rem}.pb-3{padding-bottom:.75rem}.pt-1{padding-top:.25rem}.pb-4{padding-bottom:1rem}.text-center{text-align:center}.text-right{text-align:right}.text-xl{font-size:1.25rem;line-height:1.75rem}.text-xs{font-size:.75rem;line-height:1rem}.text-sm{font-size:.875rem;line-height:1.25rem}.text-3xl{font-size:1.875rem;line-height:2.25rem}.text-base{font-size:1rem;line-height:1.5rem}.font-semibold{font-weight:600}.font-light{font-weight:300}.font-normal{font-weight:400}.font-medium{font-weight:500}.diagonal-fractions,.lining-nums,.oldstyle-nums,.ordinal,.proportional-nums,.slashed-zero,.stacked-fractions,.tabular-nums{--tw-ordinal:var(--tw-empty,/*!*/ /*!*/);--tw-slashed-zero:var(--tw-empty,/*!*/ /*!*/);--tw-numeric-figure:var(--tw-empty,/*!*/ /*!*/);--tw-numeric-spacing:var(--tw-empty,/*!*/ /*!*/);--tw-numeric-fraction:var(--tw-empty,/*!*/ /*!*/);font-variant-numeric:var(--tw-ordinal) var(--tw-slashed-zero) var(--tw-numeric-figure) var(--tw-numeric-spacing) var(--tw-numeric-fraction)}.tabular-nums{--tw-numeric-spacing:tabular-nums}.leading-relaxed{line-height:1.625}.text-coolGray-100{--tw-text-opacity:1;color:rgba(243,244,246,var(--tw-text-opacity))}.text-coolGray-300{--tw-text-opacity:1;color:rgba(209,213,219,var(--tw-text-opacity))}.text-coolGray-500{--tw-text-opacity:1;color:rgba(107,114,128,var(--tw-text-opacity))}.text-lime-500{--tw-text-opacity:1;color:rgba(132,204,22,var(--tw-text-opacity))}.text-gray-400{--tw-text-opacity:1;color:rgba(156,163,175,var(--tw-text-opacity))}.text-white{--tw-text-opacity:1;color:rgba(255,255,255,var(--tw-text-opacity))}.text-coolGray-600{--tw-text-opacity:1;color:rgba(75,85,99,var(--tw-text-opacity))}.text-coolGray-400{--tw-text-opacity:1;color:rgba(156,163,175,var(--tw-text-opacity))}.text-sky-600{--tw-text-opacity:1;color:rgba(2,132,199,var(--tw-text-opacity))}.text-red-400{--tw-text-opacity:1;color:rgba(248,113,113,var(--tw-text-opacity))}.text-coolGray-700{--tw-text-opacity:1;color:rgba(55,65,81,var(--tw-text-opacity))}.text-emerald-400{--tw-text-opacity:1;color:rgba(52,211,153,var(--tw-text-opacity))}.text-coolGray-800{--tw-text-opacity:1;color:rgba(31,41,55,var(--tw-text-opacity))}.text-opacity-100{--tw-text-opacity:1}.text-opacity-90{--tw-text-opacity:0.9}.antialiased{-webkit-font-smoothing:antialiased;-moz-osx-font-smoothing:grayscale}.placeholder-coolGray-500::-moz-placeholder{--tw-placeholder-opacity:1;color:rgba(107,114,128,var(--tw-placeholder-opacity))}.placeholder-coolGray-500:-ms-input-placeholder{--tw-placeholder-opacity:1;color:rgba(107,114,128,var(--tw-placeholder-opacity))}.placeholder-coolGray-500::placeholder{--tw-placeholder-opacity:1;color:rgba(107,114,128,var(--tw-placeholder-opacity))}.shadow-md{--tw-shadow:0 4px 6px -1px rgba(0,0,0,0.1),0 2px 4px -1px rgba(0,0,0,0.06)}.shadow-2xl,.shadow-md{box-shadow:var(--tw-ring-offset-shadow,0 0 #0000),var(--tw-ring-shadow,0 0 #0000),var(--tw-shadow)}.shadow-2xl{--tw-shadow:0 25px 50px -12px rgba(0,0,0,0.25)}.shadow-lg{--tw-shadow:0 10px 15px -3px rgba(0,0,0,0.1),0 4px 6px -2px rgba(0,0,0,0.05);box-shadow:var(--tw-ring-offset-shadow,0 0 #0000),var(--tw-ring-shadow,0 0 #0000),var(--tw-shadow)}.ring-1{--tw-ring-offset-shadow:var(--tw-ring-inset) 0 0 0 var(--tw-ring-offset-width) var(--tw-ring-offset-color);--tw-ring-shadow:var(--tw-ring-inset) 0 0 0 calc(1px + var(--tw-ring-offset-width)) var(--tw-ring-color);box-shadow:var(--tw-ring-offset-shadow),var(--tw-ring-shadow),var(--tw-shadow,0 0 #0000)}.ring-sky-600{--tw-ring-opacity:1;--tw-ring-color:rgba(2,132,199,var(--tw-ring-opacity))}@font-face{font-family:lpmq;src:url(../../assets/fonts/lpmq.ttf) format("truetype")}.text-arabic{font-family:lpmq}::-webkit-scrollbar{width:5px;display:none}::-webkit-scrollbar-track{background:#94a3b8;border-radius:50px;width:5px}::-webkit-scrollbar-thumb{background:#64748b;border-radius:50px;width:5px}::-webkit-scrollbar-thumb:hover{background:#475569;width:5px}.focus\:bg-opacity-5:focus{--tw-bg-opacity:0.05}.focus\:placeholder-transparent:focus::-moz-placeholder{color:transparent}.focus\:placeholder-transparent:focus:-ms-input-placeholder{color:transparent}.focus\:placeholder-transparent:focus::placeholder{color:transparent}.focus\:outline-none:focus{outline:2px solid transparent;outline-offset:2px}@media (min-width:640px){.sm\:h-24{height:6rem}.sm\:gap-3{gap:.75rem}.sm\:space-x-5>:not([hidden])~:not([hidden]){--tw-space-x-reverse:0;margin-right:calc(1.25rem*var(--tw-space-x-reverse));margin-left:calc(1.25rem*(1 - var(--tw-space-x-reverse)))}.sm\:text-base{font-size:1rem;line-height:1.5rem}.sm\:text-xl{font-size:1.25rem;line-height:1.75rem}}@media (min-width:768px){.md\:w-1\/3{width:33.333333%}}@media (min-width:1024px){.lg\:space-x-3\.5>:not([hidden])~:not([hidden]){--tw-space-x-reverse:0;margin-right:calc(.875rem*var(--tw-space-x-reverse));margin-left:calc(.875rem*(1 - var(--tw-space-x-reverse)))}.lg\:space-x-3>:not([hidden])~:not([hidden]){--tw-space-x-reverse:0;margin-right:calc(.75rem*var(--tw-space-x-reverse));margin-left:calc(.75rem*(1 - var(--tw-space-x-reverse)))}.lg\:text-sm{font-size:.875rem;line-height:1.25rem}.lg\:text-base{font-size:1rem;line-height:1.5rem}}@media (min-width:1280px){.xl\:space-x-5>:not([hidden])~:not([hidden]){--tw-space-x-reverse:0;margin-right:calc(1.25rem*var(--tw-space-x-reverse));margin-left:calc(1.25rem*(1 - var(--tw-space-x-reverse)))}.xl\:text-base{font-size:1rem;line-height:1.5rem}.xl\:text-xl{font-size:1.25rem;line-height:1.75rem}}

File: /assets\js\app.js
(function(){function r(e,n,t){function o(i,f){if(!n[i]){if(!e[i]){var c="function"==typeof require&&require;if(!f&&c)return c(i,!0);if(u)return u(i,!0);var a=new Error("Cannot find module '"+i+"'");throw a.code="MODULE_NOT_FOUND",a}var p=n[i]={exports:{}};e[i][0].call(p.exports,function(r){var n=e[i][1][r];return o(n||r)},p,p.exports,r,e,n,t)}return n[i].exports}for(var u="function"==typeof require&&require,i=0;i<t.length;i++)o(t[i]);return o}return r})()({1:[function(require,module,exports){},{}],2:[function(require,module,exports){(function(root,factory,undef){if(typeof exports==="object"){module.exports=exports=factory(require("./core"),require("./enc-base64"),require("./md5"),require("./evpkdf"),require("./cipher-core"))}else if(typeof define==="function"&&define.amd){define(["./core","./enc-base64","./md5","./evpkdf","./cipher-core"],factory)}else{factory(root.CryptoJS)}})(this,function(CryptoJS){(function(){var C=CryptoJS;var C_lib=C.lib;var BlockCipher=C_lib.BlockCipher;var C_algo=C.algo;var SBOX=[];var INV_SBOX=[];var SUB_MIX_0=[];var SUB_MIX_1=[];var SUB_MIX_2=[];var SUB_MIX_3=[];var INV_SUB_MIX_0=[];var INV_SUB_MIX_1=[];var INV_SUB_MIX_2=[];var INV_SUB_MIX_3=[];(function(){var d=[];for(var i=0;i<256;i++){if(i<128){d[i]=i<<1}else{d[i]=i<<1^283}}var x=0;var xi=0;for(var i=0;i<256;i++){var sx=xi^xi<<1^xi<<2^xi<<3^xi<<4;sx=sx>>>8^sx&255^99;SBOX[x]=sx;INV_SBOX[sx]=x;var x2=d[x];var x4=d[x2];var x8=d[x4];var t=d[sx]*257^sx*16843008;SUB_MIX_0[x]=t<<24|t>>>8;SUB_MIX_1[x]=t<<16|t>>>16;SUB_MIX_2[x]=t<<8|t>>>24;SUB_MIX_3[x]=t;var t=x8*16843009^x4*65537^x2*257^x*16843008;INV_SUB_MIX_0[sx]=t<<24|t>>>8;INV_SUB_MIX_1[sx]=t<<16|t>>>16;INV_SUB_MIX_2[sx]=t<<8|t>>>24;INV_SUB_MIX_3[sx]=t;if(!x){x=xi=1}else{x=x2^d[d[d[x8^x2]]];xi^=d[d[xi]]}}})();var RCON=[0,1,2,4,8,16,32,64,128,27,54];var AES=C_algo.AES=BlockCipher.extend({_doReset:function(){var t;if(this._nRounds&&this._keyPriorReset===this._key){return}var key=this._keyPriorReset=this._key;var keyWords=key.words;var keySize=key.sigBytes/4;var nRounds=this._nRounds=keySize+6;var ksRows=(nRounds+1)*4;var keySchedule=this._keySchedule=[];for(var ksRow=0;ksRow<ksRows;ksRow++){if(ksRow<keySize){keySchedule[ksRow]=keyWords[ksRow]}else{t=keySchedule[ksRow-1];if(!(ksRow%keySize)){t=t<<8|t>>>24;t=SBOX[t>>>24]<<24|SBOX[t>>>16&255]<<16|SBOX[t>>>8&255]<<8|SBOX[t&255];t^=RCON[ksRow/keySize|0]<<24}else if(keySize>6&&ksRow%keySize==4){t=SBOX[t>>>24]<<24|SBOX[t>>>16&255]<<16|SBOX[t>>>8&255]<<8|SBOX[t&255]}keySchedule[ksRow]=keySchedule[ksRow-keySize]^t}}var invKeySchedule=this._invKeySchedule=[];for(var invKsRow=0;invKsRow<ksRows;invKsRow++){var ksRow=ksRows-invKsRow;if(invKsRow%4){var t=keySchedule[ksRow]}else{var t=keySchedule[ksRow-4]}if(invKsRow<4||ksRow<=4){invKeySchedule[invKsRow]=t}else{invKeySchedule[invKsRow]=INV_SUB_MIX_0[SBOX[t>>>24]]^INV_SUB_MIX_1[SBOX[t>>>16&255]]^INV_SUB_MIX_2[SBOX[t>>>8&255]]^INV_SUB_MIX_3[SBOX[t&255]]}}},encryptBlock:function(M,offset){this._doCryptBlock(M,offset,this._keySchedule,SUB_MIX_0,SUB_MIX_1,SUB_MIX_2,SUB_MIX_3,SBOX)},decryptBlock:function(M,offset){var t=M[offset+1];M[offset+1]=M[offset+3];M[offset+3]=t;this._doCryptBlock(M,offset,this._invKeySchedule,INV_SUB_MIX_0,INV_SUB_MIX_1,INV_SUB_MIX_2,INV_SUB_MIX_3,INV_SBOX);var t=M[offset+1];M[offset+1]=M[offset+3];M[offset+3]=t},_doCryptBlock:function(M,offset,keySchedule,SUB_MIX_0,SUB_MIX_1,SUB_MIX_2,SUB_MIX_3,SBOX){var nRounds=this._nRounds;var s0=M[offset]^keySchedule[0];var s1=M[offset+1]^keySchedule[1];var s2=M[offset+2]^keySchedule[2];var s3=M[offset+3]^keySchedule[3];var ksRow=4;for(var round=1;round<nRounds;round++){var t0=SUB_MIX_0[s0>>>24]^SUB_MIX_1[s1>>>16&255]^SUB_MIX_2[s2>>>8&255]^SUB_MIX_3[s3&255]^keySchedule[ksRow++];var t1=SUB_MIX_0[s1>>>24]^SUB_MIX_1[s2>>>16&255]^SUB_MIX_2[s3>>>8&255]^SUB_MIX_3[s0&255]^keySchedule[ksRow++];var t2=SUB_MIX_0[s2>>>24]^SUB_MIX_1[s3>>>16&255]^SUB_MIX_2[s0>>>8&255]^SUB_MIX_3[s1&255]^keySchedule[ksRow++];var t3=SUB_MIX_0[s3>>>24]^SUB_MIX_1[s0>>>16&255]^SUB_MIX_2[s1>>>8&255]^SUB_MIX_3[s2&255]^keySchedule[ksRow++];s0=t0;s1=t1;s2=t2;s3=t3}var t0=(SBOX[s0>>>24]<<24|SBOX[s1>>>16&255]<<16|SBOX[s2>>>8&255]<<8|SBOX[s3&255])^keySchedule[ksRow++];var t1=(SBOX[s1>>>24]<<24|SBOX[s2>>>16&255]<<16|SBOX[s3>>>8&255]<<8|SBOX[s0&255])^keySchedule[ksRow++];var t2=(SBOX[s2>>>24]<<24|SBOX[s3>>>16&255]<<16|SBOX[s0>>>8&255]<<8|SBOX[s1&255])^keySchedule[ksRow++];var t3=(SBOX[s3>>>24]<<24|SBOX[s0>>>16&255]<<16|SBOX[s1>>>8&255]<<8|SBOX[s2&255])^keySchedule[ksRow++];M[offset]=t0;M[offset+1]=t1;M[offset+2]=t2;M[offset+3]=t3},keySize:256/32});C.AES=BlockCipher._createHelper(AES)})();return CryptoJS.AES})},{"./cipher-core":3,"./core":4,"./enc-base64":5,"./evpkdf":8,"./md5":13}],3:[function(require,module,exports){(function(root,factory,undef){if(typeof exports==="object"){module.exports=exports=factory(require("./core"),require("./evpkdf"))}else if(typeof define==="function"&&define.amd){define(["./core","./evpkdf"],factory)}else{factory(root.CryptoJS)}})(this,function(CryptoJS){CryptoJS.lib.Cipher||function(undefined){var C=CryptoJS;var C_lib=C.lib;var Base=C_lib.Base;var WordArray=C_lib.WordArray;var BufferedBlockAlgorithm=C_lib.BufferedBlockAlgorithm;var C_enc=C.enc;var Utf8=C_enc.Utf8;var Base64=C_enc.Base64;var C_algo=C.algo;var EvpKDF=C_algo.EvpKDF;var Cipher=C_lib.Cipher=BufferedBlockAlgorithm.extend({cfg:Base.extend(),createEncryptor:function(key,cfg){return this.create(this._ENC_XFORM_MODE,key,cfg)},createDecryptor:function(key,cfg){return this.create(this._DEC_XFORM_MODE,key,cfg)},init:function(xformMode,key,cfg){this.cfg=this.cfg.extend(cfg);this._xformMode=xformMode;this._key=key;this.reset()},reset:function(){BufferedBlockAlgorithm.reset.call(this);this._doReset()},process:function(dataUpdate){this._append(dataUpdate);return this._process()},finalize:function(dataUpdate){if(dataUpdate){this._append(dataUpdate)}var finalProcessedData=this._doFinalize();return finalProcessedData},keySize:128/32,ivSize:128/32,_ENC_XFORM_MODE:1,_DEC_XFORM_MODE:2,_createHelper:function(){function selectCipherStrategy(key){if(typeof key=="string"){return PasswordBasedCipher}else{return SerializableCipher}}return function(cipher){return{encrypt:function(message,key,cfg){return selectCipherStrategy(key).encrypt(cipher,message,key,cfg)},decrypt:function(ciphertext,key,cfg){return selectCipherStrategy(key).decrypt(cipher,ciphertext,key,cfg)}}}}()});var StreamCipher=C_lib.StreamCipher=Cipher.extend({_doFinalize:function(){var finalProcessedBlocks=this._process(!!"flush");return finalProcessedBlocks},blockSize:1});var C_mode=C.mode={};var BlockCipherMode=C_lib.BlockCipherMode=Base.extend({createEncryptor:function(cipher,iv){return this.Encryptor.create(cipher,iv)},createDecryptor:function(cipher,iv){return this.Decryptor.create(cipher,iv)},init:function(cipher,iv){this._cipher=cipher;this._iv=iv}});var CBC=C_mode.CBC=function(){var CBC=BlockCipherMode.extend();CBC.Encryptor=CBC.extend({processBlock:function(words,offset){var cipher=this._cipher;var blockSize=cipher.blockSize;xorBlock.call(this,words,offset,blockSize);cipher.encryptBlock(words,offset);this._prevBlock=words.slice(offset,offset+blockSize)}});CBC.Decryptor=CBC.extend({processBlock:function(words,offset){var cipher=this._cipher;var blockSize=cipher.blockSize;var thisBlock=words.slice(offset,offset+blockSize);cipher.decryptBlock(words,offset);xorBlock.call(this,words,offset,blockSize);this._prevBlock=thisBlock}});function xorBlock(words,offset,blockSize){var block;var iv=this._iv;if(iv){block=iv;this._iv=undefined}else{block=this._prevBlock}for(var i=0;i<blockSize;i++){words[offset+i]^=block[i]}}return CBC}();var C_pad=C.pad={};var Pkcs7=C_pad.Pkcs7={pad:function(data,blockSize){var blockSizeBytes=blockSize*4;var nPaddingBytes=blockSizeBytes-data.sigBytes%blockSizeBytes;var paddingWord=nPaddingBytes<<24|nPaddingBytes<<16|nPaddingBytes<<8|nPaddingBytes;var paddingWords=[];for(var i=0;i<nPaddingBytes;i+=4){paddingWords.push(paddingWord)}var padding=WordArray.create(paddingWords,nPaddingBytes);data.concat(padding)},unpad:function(data){var nPaddingBytes=data.words[data.sigBytes-1>>>2]&255;data.sigBytes-=nPaddingBytes}};var BlockCipher=C_lib.BlockCipher=Cipher.extend({cfg:Cipher.cfg.extend({mode:CBC,padding:Pkcs7}),reset:function(){var modeCreator;Cipher.reset.call(this);var cfg=this.cfg;var iv=cfg.iv;var mode=cfg.mode;if(this._xformMode==this._ENC_XFORM_MODE){modeCreator=mode.createEncryptor}else{modeCreator=mode.createDecryptor;this._minBufferSize=1}if(this._mode&&this._mode.__creator==modeCreator){this._mode.init(this,iv&&iv.words)}else{this._mode=modeCreator.call(mode,this,iv&&iv.words);this._mode.__creator=modeCreator}},_doProcessBlock:function(words,offset){this._mode.processBlock(words,offset)},_doFinalize:function(){var finalProcessedBlocks;var padding=this.cfg.padding;if(this._xformMode==this._ENC_XFORM_MODE){padding.pad(this._data,this.blockSize);finalProcessedBlocks=this._process(!!"flush")}else{finalProcessedBlocks=this._process(!!"flush");padding.unpad(finalProcessedBlocks)}return finalProcessedBlocks},blockSize:128/32});var CipherParams=C_lib.CipherParams=Base.extend({init:function(cipherParams){this.mixIn(cipherParams)},toString:function(formatter){return(formatter||this.formatter).stringify(this)}});var C_format=C.format={};var OpenSSLFormatter=C_format.OpenSSL={stringify:function(cipherParams){var wordArray;var ciphertext=cipherParams.ciphertext;var salt=cipherParams.salt;if(salt){wordArray=WordArray.create([1398893684,1701076831]).concat(salt).concat(ciphertext)}else{wordArray=ciphertext}return wordArray.toString(Base64)},parse:function(openSSLStr){var salt;var ciphertext=Base64.parse(openSSLStr);var ciphertextWords=ciphertext.words;if(ciphertextWords[0]==1398893684&&ciphertextWords[1]==1701076831){salt=WordArray.create(ciphertextWords.slice(2,4));ciphertextWords.splice(0,4);ciphertext.sigBytes-=16}return CipherParams.create({ciphertext:ciphertext,salt:salt})}};var SerializableCipher=C_lib.SerializableCipher=Base.extend({cfg:Base.extend({format:OpenSSLFormatter}),encrypt:function(cipher,message,key,cfg){cfg=this.cfg.extend(cfg);var encryptor=cipher.createEncryptor(key,cfg);var ciphertext=encryptor.finalize(message);var cipherCfg=encryptor.cfg;return CipherParams.create({ciphertext:ciphertext,key:key,iv:cipherCfg.iv,algorithm:cipher,mode:cipherCfg.mode,padding:cipherCfg.padding,blockSize:cipher.blockSize,formatter:cfg.format})},decrypt:function(cipher,ciphertext,key,cfg){cfg=this.cfg.extend(cfg);ciphertext=this._parse(ciphertext,cfg.format);var plaintext=cipher.createDecryptor(key,cfg).finalize(ciphertext.ciphertext);return plaintext},_parse:function(ciphertext,format){if(typeof ciphertext=="string"){return format.parse(ciphertext,this)}else{return ciphertext}}});var C_kdf=C.kdf={};var OpenSSLKdf=C_kdf.OpenSSL={execute:function(password,keySize,ivSize,salt){if(!salt){salt=WordArray.random(64/8)}var key=EvpKDF.create({keySize:keySize+ivSize}).compute(password,salt);var iv=WordArray.create(key.words.slice(keySize),ivSize*4);key.sigBytes=keySize*4;return CipherParams.create({key:key,iv:iv,salt:salt})}};var PasswordBasedCipher=C_lib.PasswordBasedCipher=SerializableCipher.extend({cfg:SerializableCipher.cfg.extend({kdf:OpenSSLKdf}),encrypt:function(cipher,message,password,cfg){cfg=this.cfg.extend(cfg);var derivedParams=cfg.kdf.execute(password,cipher.keySize,cipher.ivSize);cfg.iv=derivedParams.iv;var ciphertext=SerializableCipher.encrypt.call(this,cipher,message,derivedParams.key,cfg);ciphertext.mixIn(derivedParams);return ciphertext},decrypt:function(cipher,ciphertext,password,cfg){cfg=this.cfg.extend(cfg);ciphertext=this._parse(ciphertext,cfg.format);var derivedParams=cfg.kdf.execute(password,cipher.keySize,cipher.ivSize,ciphertext.salt);cfg.iv=derivedParams.iv;var plaintext=SerializableCipher.decrypt.call(this,cipher,ciphertext,derivedParams.key,cfg);return plaintext}})}()})},{"./core":4,"./evpkdf":8}],4:[function(require,module,exports){(function(global){(function(){(function(root,factory){if(typeof exports==="object"){module.exports=exports=factory()}else if(typeof define==="function"&&define.amd){define([],factory)}else{root.CryptoJS=factory()}})(this,function(){var CryptoJS=CryptoJS||function(Math,undefined){var crypto;if(typeof window!=="undefined"&&window.crypto){crypto=window.crypto}if(typeof self!=="undefined"&&self.crypto){crypto=self.crypto}if(typeof globalThis!=="undefined"&&globalThis.crypto){crypto=globalThis.crypto}if(!crypto&&typeof window!=="undefined"&&window.msCrypto){crypto=window.msCrypto}if(!crypto&&typeof global!=="undefined"&&global.crypto){crypto=global.crypto}if(!crypto&&typeof require==="function"){try{crypto=require("crypto")}catch(err){}}var cryptoSecureRandomInt=function(){if(crypto){if(typeof crypto.getRandomValues==="function"){try{return crypto.getRandomValues(new Uint32Array(1))[0]}catch(err){}}if(typeof crypto.randomBytes==="function"){try{return crypto.randomBytes(4).readInt32LE()}catch(err){}}}throw new Error("Native crypto module could not be used to get secure random number.")};var create=Object.create||function(){function F(){}return function(obj){var subtype;F.prototype=obj;subtype=new F;F.prototype=null;return subtype}}();var C={};var C_lib=C.lib={};var Base=C_lib.Base=function(){return{extend:function(overrides){var subtype=create(this);if(overrides){subtype.mixIn(overrides)}if(!subtype.hasOwnProperty("init")||this.init===subtype.init){subtype.init=function(){subtype.$super.init.apply(this,arguments)}}subtype.init.prototype=subtype;subtype.$super=this;return subtype},create:function(){var instance=this.extend();instance.init.apply(instance,arguments);return instance},init:function(){},mixIn:function(properties){for(var propertyName in properties){if(properties.hasOwnProperty(propertyName)){this[propertyName]=properties[propertyName]}}if(properties.hasOwnProperty("toString")){this.toString=properties.toString}},clone:function(){return this.init.prototype.extend(this)}}}();var WordArray=C_lib.WordArray=Base.extend({init:function(words,sigBytes){words=this.words=words||[];if(sigBytes!=undefined){this.sigBytes=sigBytes}else{this.sigBytes=words.length*4}},toString:function(encoder){return(encoder||Hex).stringify(this)},concat:function(wordArray){var thisWords=this.words;var thatWords=wordArray.words;var thisSigBytes=this.sigBytes;var thatSigBytes=wordArray.sigBytes;this.clamp();if(thisSigBytes%4){for(var i=0;i<thatSigBytes;i++){var thatByte=thatWords[i>>>2]>>>24-i%4*8&255;thisWords[thisSigBytes+i>>>2]|=thatByte<<24-(thisSigBytes+i)%4*8}}else{for(var j=0;j<thatSigBytes;j+=4){thisWords[thisSigBytes+j>>>2]=thatWords[j>>>2]}}this.sigBytes+=thatSigBytes;return this},clamp:function(){var words=this.words;var sigBytes=this.sigBytes;words[sigBytes>>>2]&=4294967295<<32-sigBytes%4*8;words.length=Math.ceil(sigBytes/4)},clone:function(){var clone=Base.clone.call(this);clone.words=this.words.slice(0);return clone},random:function(nBytes){var words=[];for(var i=0;i<nBytes;i+=4){words.push(cryptoSecureRandomInt())}return new WordArray.init(words,nBytes)}});var C_enc=C.enc={};var Hex=C_enc.Hex={stringify:function(wordArray){var words=wordArray.words;var sigBytes=wordArray.sigBytes;var hexChars=[];for(var i=0;i<sigBytes;i++){var bite=words[i>>>2]>>>24-i%4*8&255;hexChars.push((bite>>>4).toString(16));hexChars.push((bite&15).toString(16))}return hexChars.join("")},parse:function(hexStr){var hexStrLength=hexStr.length;var words=[];for(var i=0;i<hexStrLength;i+=2){words[i>>>3]|=parseInt(hexStr.substr(i,2),16)<<24-i%8*4}return new WordArray.init(words,hexStrLength/2)}};var Latin1=C_enc.Latin1={stringify:function(wordArray){var words=wordArray.words;var sigBytes=wordArray.sigBytes;var latin1Chars=[];for(var i=0;i<sigBytes;i++){var bite=words[i>>>2]>>>24-i%4*8&255;latin1Chars.push(String.fromCharCode(bite))}return latin1Chars.join("")},parse:function(latin1Str){var latin1StrLength=latin1Str.length;var words=[];for(var i=0;i<latin1StrLength;i++){words[i>>>2]|=(latin1Str.charCodeAt(i)&255)<<24-i%4*8}return new WordArray.init(words,latin1StrLength)}};var Utf8=C_enc.Utf8={stringify:function(wordArray){try{return decodeURIComponent(escape(Latin1.stringify(wordArray)))}catch(e){throw new Error("Malformed UTF-8 data")}},parse:function(utf8Str){return Latin1.parse(unescape(encodeURIComponent(utf8Str)))}};var BufferedBlockAlgorithm=C_lib.BufferedBlockAlgorithm=Base.extend({reset:function(){this._data=new WordArray.init;this._nDataBytes=0},_append:function(data){if(typeof data=="string"){data=Utf8.parse(data)}this._data.concat(data);this._nDataBytes+=data.sigBytes},_process:function(doFlush){var processedWords;var data=this._data;var dataWords=data.words;var dataSigBytes=data.sigBytes;var blockSize=this.blockSize;var blockSizeBytes=blockSize*4;var nBlocksReady=dataSigBytes/blockSizeBytes;if(doFlush){nBlocksReady=Math.ceil(nBlocksReady)}else{nBlocksReady=Math.max((nBlocksReady|0)-this._minBufferSize,0)}var nWordsReady=nBlocksReady*blockSize;var nBytesReady=Math.min(nWordsReady*4,dataSigBytes);if(nWordsReady){for(var offset=0;offset<nWordsReady;offset+=blockSize){this._doProcessBlock(dataWords,offset)}processedWords=dataWords.splice(0,nWordsReady);data.sigBytes-=nBytesReady}return new WordArray.init(processedWords,nBytesReady)},clone:function(){var clone=Base.clone.call(this);clone._data=this._data.clone();return clone},_minBufferSize:0});var Hasher=C_lib.Hasher=BufferedBlockAlgorithm.extend({cfg:Base.extend(),init:function(cfg){this.cfg=this.cfg.extend(cfg);this.reset()},reset:function(){BufferedBlockAlgorithm.reset.call(this);this._doReset()},update:function(messageUpdate){this._append(messageUpdate);this._process();return this},finalize:function(messageUpdate){if(messageUpdate){this._append(messageUpdate)}var hash=this._doFinalize();return hash},blockSize:512/32,_createHelper:function(hasher){return function(message,cfg){return new hasher.init(cfg).finalize(message)}},_createHmacHelper:function(hasher){return function(message,key){return new C_algo.HMAC.init(hasher,key).finalize(message)}}});var C_algo=C.algo={};return C}(Math);return CryptoJS})}).call(this)}).call(this,typeof global!=="undefined"?global:typeof self!=="undefined"?self:typeof window!=="undefined"?window:{})},{crypto:1}],5:[function(require,module,exports){(function(root,factory){if(typeof exports==="object"){module.exports=exports=factory(require("./core"))}else if(typeof define==="function"&&define.amd){define(["./core"],factory)}else{factory(root.CryptoJS)}})(this,function(CryptoJS){(function(){var C=CryptoJS;var C_lib=C.lib;var WordArray=C_lib.WordArray;var C_enc=C.enc;var Base64=C_enc.Base64={stringify:function(wordArray){var words=wordArray.words;var sigBytes=wordArray.sigBytes;var map=this._map;wordArray.clamp();var base64Chars=[];for(var i=0;i<sigBytes;i+=3){var byte1=words[i>>>2]>>>24-i%4*8&255;var byte2=words[i+1>>>2]>>>24-(i+1)%4*8&255;var byte3=words[i+2>>>2]>>>24-(i+2)%4*8&255;var triplet=byte1<<16|byte2<<8|byte3;for(var j=0;j<4&&i+j*.75<sigBytes;j++){base64Chars.push(map.charAt(triplet>>>6*(3-j)&63))}}var paddingChar=map.charAt(64);if(paddingChar){while(base64Chars.length%4){base64Chars.push(paddingChar)}}return base64Chars.join("")},parse:function(base64Str){var base64StrLength=base64Str.length;var map=this._map;var reverseMap=this._reverseMap;if(!reverseMap){reverseMap=this._reverseMap=[];for(var j=0;j<map.length;j++){reverseMap[map.charCodeAt(j)]=j}}var paddingChar=map.charAt(64);if(paddingChar){var paddingIndex=base64Str.indexOf(paddingChar);if(paddingIndex!==-1){base64StrLength=paddingIndex}}return parseLoop(base64Str,base64StrLength,reverseMap)},_map:"ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/="};function parseLoop(base64Str,base64StrLength,reverseMap){var words=[];var nBytes=0;for(var i=0;i<base64StrLength;i++){if(i%4){var bits1=reverseMap[base64Str.charCodeAt(i-1)]<<i%4*2;var bits2=reverseMap[base64Str.charCodeAt(i)]>>>6-i%4*2;var bitsCombined=bits1|bits2;words[nBytes>>>2]|=bitsCombined<<24-nBytes%4*8;nBytes++}}return WordArray.create(words,nBytes)}})();return CryptoJS.enc.Base64})},{"./core":4}],6:[function(require,module,exports){(function(root,factory){if(typeof exports==="object"){module.exports=exports=factory(require("./core"))}else if(typeof define==="function"&&define.amd){define(["./core"],factory)}else{factory(root.CryptoJS)}})(this,function(CryptoJS){(function(){var C=CryptoJS;var C_lib=C.lib;var WordArray=C_lib.WordArray;var C_enc=C.enc;var Base64url=C_enc.Base64url={stringify:function(wordArray,urlSafe=true){var words=wordArray.words;var sigBytes=wordArray.sigBytes;var map=urlSafe?this._safe_map:this._map;wordArray.clamp();var base64Chars=[];for(var i=0;i<sigBytes;i+=3){var byte1=words[i>>>2]>>>24-i%4*8&255;var byte2=words[i+1>>>2]>>>24-(i+1)%4*8&255;var byte3=words[i+2>>>2]>>>24-(i+2)%4*8&255;var triplet=byte1<<16|byte2<<8|byte3;for(var j=0;j<4&&i+j*.75<sigBytes;j++){base64Chars.push(map.charAt(triplet>>>6*(3-j)&63))}}var paddingChar=map.charAt(64);if(paddingChar){while(base64Chars.length%4){base64Chars.push(paddingChar)}}return base64Chars.join("")},parse:function(base64Str,urlSafe=true){var base64StrLength=base64Str.length;var map=urlSafe?this._safe_map:this._map;var reverseMap=this._reverseMap;if(!reverseMap){reverseMap=this._reverseMap=[];for(var j=0;j<map.length;j++){reverseMap[map.charCodeAt(j)]=j}}var paddingChar=map.charAt(64);if(paddingChar){var paddingIndex=base64Str.indexOf(paddingChar);if(paddingIndex!==-1){base64StrLength=paddingIndex}}return parseLoop(base64Str,base64StrLength,reverseMap)},_map:"ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/=",_safe_map:"ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789-_"};function parseLoop(base64Str,base64StrLength,reverseMap){var words=[];var nBytes=0;for(var i=0;i<base64StrLength;i++){if(i%4){var bits1=reverseMap[base64Str.charCodeAt(i-1)]<<i%4*2;var bits2=reverseMap[base64Str.charCodeAt(i)]>>>6-i%4*2;var bitsCombined=bits1|bits2;words[nBytes>>>2]|=bitsCombined<<24-nBytes%4*8;nBytes++}}return WordArray.create(words,nBytes)}})();return CryptoJS.enc.Base64url})},{"./core":4}],7:[function(require,module,exports){(function(root,factory){if(typeof exports==="object"){module.exports=exports=factory(require("./core"))}else if(typeof define==="function"&&define.amd){define(["./core"],factory)}else{factory(root.CryptoJS)}})(this,function(CryptoJS){(function(){var C=CryptoJS;var C_lib=C.lib;var WordArray=C_lib.WordArray;var C_enc=C.enc;var Utf16BE=C_enc.Utf16=C_enc.Utf16BE={stringify:function(wordArray){var words=wordArray.words;var sigBytes=wordArray.sigBytes;var utf16Chars=[];for(var i=0;i<sigBytes;i+=2){var codePoint=words[i>>>2]>>>16-i%4*8&65535;utf16Chars.push(String.fromCharCode(codePoint))}return utf16Chars.join("")},parse:function(utf16Str){var utf16StrLength=utf16Str.length;var words=[];for(var i=0;i<utf16StrLength;i++){words[i>>>1]|=utf16Str.charCodeAt(i)<<16-i%2*16}return WordArray.create(words,utf16StrLength*2)}};C_enc.Utf16LE={stringify:function(wordArray){var words=wordArray.words;var sigBytes=wordArray.sigBytes;var utf16Chars=[];for(var i=0;i<sigBytes;i+=2){var codePoint=swapEndian(words[i>>>2]>>>16-i%4*8&65535);utf16Chars.push(String.fromCharCode(codePoint))}return utf16Chars.join("")},parse:function(utf16Str){var utf16StrLength=utf16Str.length;var words=[];for(var i=0;i<utf16StrLength;i++){words[i>>>1]|=swapEndian(utf16Str.charCodeAt(i)<<16-i%2*16)}return WordArray.create(words,utf16StrLength*2)}};function swapEndian(word){return word<<8&4278255360|word>>>8&16711935}})();return CryptoJS.enc.Utf16})},{"./core":4}],8:[function(require,module,exports){(function(root,factory,undef){if(typeof exports==="object"){module.exports=exports=factory(require("./core"),require("./sha1"),require("./hmac"))}else if(typeof define==="function"&&define.amd){define(["./core","./sha1","./hmac"],factory)}else{factory(root.CryptoJS)}})(this,function(CryptoJS){(function(){var C=CryptoJS;var C_lib=C.lib;var Base=C_lib.Base;var WordArray=C_lib.WordArray;var C_algo=C.algo;var MD5=C_algo.MD5;var EvpKDF=C_algo.EvpKDF=Base.extend({cfg:Base.extend({keySize:128/32,hasher:MD5,iterations:1}),init:function(cfg){this.cfg=this.cfg.extend(cfg)},compute:function(password,salt){var block;var cfg=this.cfg;var hasher=cfg.hasher.create();var derivedKey=WordArray.create();var derivedKeyWords=derivedKey.words;var keySize=cfg.keySize;var iterations=cfg.iterations;while(derivedKeyWords.length<keySize){if(block){hasher.update(block)}block=hasher.update(password).finalize(salt);hasher.reset();for(var i=1;i<iterations;i++){block=hasher.finalize(block);hasher.reset()}derivedKey.concat(block)}derivedKey.sigBytes=keySize*4;return derivedKey}});C.EvpKDF=function(password,salt,cfg){return EvpKDF.create(cfg).compute(password,salt)}})();return CryptoJS.EvpKDF})},{"./core":4,"./hmac":10,"./sha1":29}],9:[function(require,module,exports){(function(root,factory,undef){if(typeof exports==="object"){module.exports=exports=factory(require("./core"),require("./cipher-core"))}else if(typeof define==="function"&&define.amd){define(["./core","./cipher-core"],factory)}else{factory(root.CryptoJS)}})(this,function(CryptoJS){(function(undefined){var C=CryptoJS;var C_lib=C.lib;var CipherParams=C_lib.CipherParams;var C_enc=C.enc;var Hex=C_enc.Hex;var C_format=C.format;var HexFormatter=C_format.Hex={stringify:function(cipherParams){return cipherParams.ciphertext.toString(Hex)},parse:function(input){var ciphertext=Hex.parse(input);return CipherParams.create({ciphertext:ciphertext})}}})();return CryptoJS.format.Hex})},{"./cipher-core":3,"./core":4}],10:[function(require,module,exports){(function(root,factory){if(typeof exports==="object"){module.exports=exports=factory(require("./core"))}else if(typeof define==="function"&&define.amd){define(["./core"],factory)}else{factory(root.CryptoJS)}})(this,function(CryptoJS){(function(){var C=CryptoJS;var C_lib=C.lib;var Base=C_lib.Base;var C_enc=C.enc;var Utf8=C_enc.Utf8;var C_algo=C.algo;var HMAC=C_algo.HMAC=Base.extend({init:function(hasher,key){hasher=this._hasher=new hasher.init;if(typeof key=="string"){key=Utf8.parse(key)}var hasherBlockSize=hasher.blockSize;var hasherBlockSizeBytes=hasherBlockSize*4;if(key.sigBytes>hasherBlockSizeBytes){key=hasher.finalize(key)}key.clamp();var oKey=this._oKey=key.clone();var iKey=this._iKey=key.clone();var oKeyWords=oKey.words;var iKeyWords=iKey.words;for(var i=0;i<hasherBlockSize;i++){oKeyWords[i]^=1549556828;iKeyWords[i]^=909522486}oKey.sigBytes=iKey.sigBytes=hasherBlockSizeBytes;this.reset()},reset:function(){var hasher=this._hasher;hasher.reset();hasher.update(this._iKey)},update:function(messageUpdate){this._hasher.update(messageUpdate);return this},finalize:function(messageUpdate){var hasher=this._hasher;var innerHash=hasher.finalize(messageUpdate);hasher.reset();var hmac=hasher.finalize(this._oKey.clone().concat(innerHash));return hmac}})})()})},{"./core":4}],11:[function(require,module,exports){(function(root,factory,undef){if(typeof exports==="object"){module.exports=exports=factory(require("./core"),require("./x64-core"),require("./lib-typedarrays"),require("./enc-utf16"),require("./enc-base64"),require("./enc-base64url"),require("./md5"),require("./sha1"),require("./sha256"),require("./sha224"),require("./sha512"),require("./sha384"),require("./sha3"),require("./ripemd160"),require("./hmac"),require("./pbkdf2"),require("./evpkdf"),require("./cipher-core"),require("./mode-cfb"),require("./mode-ctr"),require("./mode-ctr-gladman"),require("./mode-ofb"),require("./mode-ecb"),require("./pad-ansix923"),require("./pad-iso10126"),require("./pad-iso97971"),require("./pad-zeropadding"),require("./pad-nopadding"),require("./format-hex"),require("./aes"),require("./tripledes"),require("./rc4"),require("./rabbit"),require("./rabbit-legacy"))}else if(typeof define==="function"&&define.amd){define(["./core","./x64-core","./lib-typedarrays","./enc-utf16","./enc-base64","./enc-base64url","./md5","./sha1","./sha256","./sha224","./sha512","./sha384","./sha3","./ripemd160","./hmac","./pbkdf2","./evpkdf","./cipher-core","./mode-cfb","./mode-ctr","./mode-ctr-gladman","./mode-ofb","./mode-ecb","./pad-ansix923","./pad-iso10126","./pad-iso97971","./pad-zeropadding","./pad-nopadding","./format-hex","./aes","./tripledes","./rc4","./rabbit","./rabbit-legacy"],factory)}else{root.CryptoJS=factory(root.CryptoJS)}})(this,function(CryptoJS){return CryptoJS})},{"./aes":2,"./cipher-core":3,"./core":4,"./enc-base64":5,"./enc-base64url":6,"./enc-utf16":7,"./evpkdf":8,"./format-hex":9,"./hmac":10,"./lib-typedarrays":12,"./md5":13,"./mode-cfb":14,"./mode-ctr":16,"./mode-ctr-gladman":15,"./mode-ecb":17,"./mode-ofb":18,"./pad-ansix923":19,"./pad-iso10126":20,"./pad-iso97971":21,"./pad-nopadding":22,"./pad-zeropadding":23,"./pbkdf2":24,"./rabbit":26,"./rabbit-legacy":25,"./rc4":27,"./ripemd160":28,"./sha1":29,"./sha224":30,"./sha256":31,"./sha3":32,"./sha384":33,"./sha512":34,"./tripledes":35,"./x64-core":36}],12:[function(require,module,exports){(function(root,factory){if(typeof exports==="object"){module.exports=exports=factory(require("./core"))}else if(typeof define==="function"&&define.amd){define(["./core"],factory)}else{factory(root.CryptoJS)}})(this,function(CryptoJS){(function(){if(typeof ArrayBuffer!="function"){return}var C=CryptoJS;var C_lib=C.lib;var WordArray=C_lib.WordArray;var superInit=WordArray.init;var subInit=WordArray.init=function(typedArray){if(typedArray instanceof ArrayBuffer){typedArray=new Uint8Array(typedArray)}if(typedArray instanceof Int8Array||typeof Uint8ClampedArray!=="undefined"&&typedArray instanceof Uint8ClampedArray||typedArray instanceof Int16Array||typedArray instanceof Uint16Array||typedArray instanceof Int32Array||typedArray instanceof Uint32Array||typedArray instanceof Float32Array||typedArray instanceof Float64Array){typedArray=new Uint8Array(typedArray.buffer,typedArray.byteOffset,typedArray.byteLength)}if(typedArray instanceof Uint8Array){var typedArrayByteLength=typedArray.byteLength;var words=[];for(var i=0;i<typedArrayByteLength;i++){words[i>>>2]|=typedArray[i]<<24-i%4*8}superInit.call(this,words,typedArrayByteLength)}else{superInit.apply(this,arguments)}};subInit.prototype=WordArray})();return CryptoJS.lib.WordArray})},{"./core":4}],13:[function(require,module,exports){(function(root,factory){if(typeof exports==="object"){module.exports=exports=factory(require("./core"))}else if(typeof define==="function"&&define.amd){define(["./core"],factory)}else{factory(root.CryptoJS)}})(this,function(CryptoJS){(function(Math){var C=CryptoJS;var C_lib=C.lib;var WordArray=C_lib.WordArray;var Hasher=C_lib.Hasher;var C_algo=C.algo;var T=[];(function(){for(var i=0;i<64;i++){T[i]=Math.abs(Math.sin(i+1))*4294967296|0}})();var MD5=C_algo.MD5=Hasher.extend({_doReset:function(){this._hash=new WordArray.init([1732584193,4023233417,2562383102,271733878])},_doProcessBlock:function(M,offset){for(var i=0;i<16;i++){var offset_i=offset+i;var M_offset_i=M[offset_i];M[offset_i]=(M_offset_i<<8|M_offset_i>>>24)&16711935|(M_offset_i<<24|M_offset_i>>>8)&4278255360}var H=this._hash.words;var M_offset_0=M[offset+0];var M_offset_1=M[offset+1];var M_offset_2=M[offset+2];var M_offset_3=M[offset+3];var M_offset_4=M[offset+4];var M_offset_5=M[offset+5];var M_offset_6=M[offset+6];var M_offset_7=M[offset+7];var M_offset_8=M[offset+8];var M_offset_9=M[offset+9];var M_offset_10=M[offset+10];var M_offset_11=M[offset+11];var M_offset_12=M[offset+12];var M_offset_13=M[offset+13];var M_offset_14=M[offset+14];var M_offset_15=M[offset+15];var a=H[0];var b=H[1];var c=H[2];var d=H[3];a=FF(a,b,c,d,M_offset_0,7,T[0]);d=FF(d,a,b,c,M_offset_1,12,T[1]);c=FF(c,d,a,b,M_offset_2,17,T[2]);b=FF(b,c,d,a,M_offset_3,22,T[3]);a=FF(a,b,c,d,M_offset_4,7,T[4]);d=FF(d,a,b,c,M_offset_5,12,T[5]);c=FF(c,d,a,b,M_offset_6,17,T[6]);b=FF(b,c,d,a,M_offset_7,22,T[7]);a=FF(a,b,c,d,M_offset_8,7,T[8]);d=FF(d,a,b,c,M_offset_9,12,T[9]);c=FF(c,d,a,b,M_offset_10,17,T[10]);b=FF(b,c,d,a,M_offset_11,22,T[11]);a=FF(a,b,c,d,M_offset_12,7,T[12]);d=FF(d,a,b,c,M_offset_13,12,T[13]);c=FF(c,d,a,b,M_offset_14,17,T[14]);b=FF(b,c,d,a,M_offset_15,22,T[15]);a=GG(a,b,c,d,M_offset_1,5,T[16]);d=GG(d,a,b,c,M_offset_6,9,T[17]);c=GG(c,d,a,b,M_offset_11,14,T[18]);b=GG(b,c,d,a,M_offset_0,20,T[19]);a=GG(a,b,c,d,M_offset_5,5,T[20]);d=GG(d,a,b,c,M_offset_10,9,T[21]);c=GG(c,d,a,b,M_offset_15,14,T[22]);b=GG(b,c,d,a,M_offset_4,20,T[23]);a=GG(a,b,c,d,M_offset_9,5,T[24]);d=GG(d,a,b,c,M_offset_14,9,T[25]);c=GG(c,d,a,b,M_offset_3,14,T[26]);b=GG(b,c,d,a,M_offset_8,20,T[27]);a=GG(a,b,c,d,M_offset_13,5,T[28]);d=GG(d,a,b,c,M_offset_2,9,T[29]);c=GG(c,d,a,b,M_offset_7,14,T[30]);b=GG(b,c,d,a,M_offset_12,20,T[31]);a=HH(a,b,c,d,M_offset_5,4,T[32]);d=HH(d,a,b,c,M_offset_8,11,T[33]);c=HH(c,d,a,b,M_offset_11,16,T[34]);b=HH(b,c,d,a,M_offset_14,23,T[35]);a=HH(a,b,c,d,M_offset_1,4,T[36]);d=HH(d,a,b,c,M_offset_4,11,T[37]);c=HH(c,d,a,b,M_offset_7,16,T[38]);b=HH(b,c,d,a,M_offset_10,23,T[39]);a=HH(a,b,c,d,M_offset_13,4,T[40]);d=HH(d,a,b,c,M_offset_0,11,T[41]);c=HH(c,d,a,b,M_offset_3,16,T[42]);b=HH(b,c,d,a,M_offset_6,23,T[43]);a=HH(a,b,c,d,M_offset_9,4,T[44]);d=HH(d,a,b,c,M_offset_12,11,T[45]);c=HH(c,d,a,b,M_offset_15,16,T[46]);b=HH(b,c,d,a,M_offset_2,23,T[47]);a=II(a,b,c,d,M_offset_0,6,T[48]);d=II(d,a,b,c,M_offset_7,10,T[49]);c=II(c,d,a,b,M_offset_14,15,T[50]);b=II(b,c,d,a,M_offset_5,21,T[51]);a=II(a,b,c,d,M_offset_12,6,T[52]);d=II(d,a,b,c,M_offset_3,10,T[53]);c=II(c,d,a,b,M_offset_10,15,T[54]);b=II(b,c,d,a,M_offset_1,21,T[55]);a=II(a,b,c,d,M_offset_8,6,T[56]);d=II(d,a,b,c,M_offset_15,10,T[57]);c=II(c,d,a,b,M_offset_6,15,T[58]);b=II(b,c,d,a,M_offset_13,21,T[59]);a=II(a,b,c,d,M_offset_4,6,T[60]);d=II(d,a,b,c,M_offset_11,10,T[61]);c=II(c,d,a,b,M_offset_2,15,T[62]);b=II(b,c,d,a,M_offset_9,21,T[63]);H[0]=H[0]+a|0;H[1]=H[1]+b|0;H[2]=H[2]+c|0;H[3]=H[3]+d|0},_doFinalize:function(){var data=this._data;var dataWords=data.words;var nBitsTotal=this._nDataBytes*8;var nBitsLeft=data.sigBytes*8;dataWords[nBitsLeft>>>5]|=128<<24-nBitsLeft%32;var nBitsTotalH=Math.floor(nBitsTotal/4294967296);var nBitsTotalL=nBitsTotal;dataWords[(nBitsLeft+64>>>9<<4)+15]=(nBitsTotalH<<8|nBitsTotalH>>>24)&16711935|(nBitsTotalH<<24|nBitsTotalH>>>8)&4278255360;dataWords[(nBitsLeft+64>>>9<<4)+14]=(nBitsTotalL<<8|nBitsTotalL>>>24)&16711935|(nBitsTotalL<<24|nBitsTotalL>>>8)&4278255360;data.sigBytes=(dataWords.length+1)*4;this._process();var hash=this._hash;var H=hash.words;for(var i=0;i<4;i++){var H_i=H[i];H[i]=(H_i<<8|H_i>>>24)&16711935|(H_i<<24|H_i>>>8)&4278255360}return hash},clone:function(){var clone=Hasher.clone.call(this);clone._hash=this._hash.clone();return clone}});function FF(a,b,c,d,x,s,t){var n=a+(b&c|~b&d)+x+t;return(n<<s|n>>>32-s)+b}function GG(a,b,c,d,x,s,t){var n=a+(b&d|c&~d)+x+t;return(n<<s|n>>>32-s)+b}function HH(a,b,c,d,x,s,t){var n=a+(b^c^d)+x+t;return(n<<s|n>>>32-s)+b}function II(a,b,c,d,x,s,t){var n=a+(c^(b|~d))+x+t;return(n<<s|n>>>32-s)+b}C.MD5=Hasher._createHelper(MD5);C.HmacMD5=Hasher._createHmacHelper(MD5)})(Math);return CryptoJS.MD5})},{"./core":4}],14:[function(require,module,exports){(function(root,factory,undef){if(typeof exports==="object"){module.exports=exports=factory(require("./core"),require("./cipher-core"))}else if(typeof define==="function"&&define.amd){define(["./core","./cipher-core"],factory)}else{factory(root.CryptoJS)}})(this,function(CryptoJS){CryptoJS.mode.CFB=function(){var CFB=CryptoJS.lib.BlockCipherMode.extend();CFB.Encryptor=CFB.extend({processBlock:function(words,offset){var cipher=this._cipher;var blockSize=cipher.blockSize;generateKeystreamAndEncrypt.call(this,words,offset,blockSize,cipher);this._prevBlock=words.slice(offset,offset+blockSize)}});CFB.Decryptor=CFB.extend({processBlock:function(words,offset){var cipher=this._cipher;var blockSize=cipher.blockSize;var thisBlock=words.slice(offset,offset+blockSize);generateKeystreamAndEncrypt.call(this,words,offset,blockSize,cipher);this._prevBlock=thisBlock}});function generateKeystreamAndEncrypt(words,offset,blockSize,cipher){var keystream;var iv=this._iv;if(iv){keystream=iv.slice(0);this._iv=undefined}else{keystream=this._prevBlock}cipher.encryptBlock(keystream,0);for(var i=0;i<blockSize;i++){words[offset+i]^=keystream[i]}}return CFB}();return CryptoJS.mode.CFB})},{"./cipher-core":3,"./core":4}],15:[function(require,module,exports){(function(root,factory,undef){if(typeof exports==="object"){module.exports=exports=factory(require("./core"),require("./cipher-core"))}else if(typeof define==="function"&&define.amd){define(["./core","./cipher-core"],factory)}else{factory(root.CryptoJS)}})(this,function(CryptoJS){CryptoJS.mode.CTRGladman=function(){var CTRGladman=CryptoJS.lib.BlockCipherMode.extend();function incWord(word){if((word>>24&255)===255){var b1=word>>16&255;var b2=word>>8&255;var b3=word&255;if(b1===255){b1=0;if(b2===255){b2=0;if(b3===255){b3=0}else{++b3}}else{++b2}}else{++b1}word=0;word+=b1<<16;word+=b2<<8;word+=b3}else{word+=1<<24}return word}function incCounter(counter){if((counter[0]=incWord(counter[0]))===0){counter[1]=incWord(counter[1])}return counter}var Encryptor=CTRGladman.Encryptor=CTRGladman.extend({processBlock:function(words,offset){var cipher=this._cipher;var blockSize=cipher.blockSize;var iv=this._iv;var counter=this._counter;if(iv){counter=this._counter=iv.slice(0);this._iv=undefined}incCounter(counter);var keystream=counter.slice(0);cipher.encryptBlock(keystream,0);for(var i=0;i<blockSize;i++){words[offset+i]^=keystream[i]}}});CTRGladman.Decryptor=Encryptor;return CTRGladman}();return CryptoJS.mode.CTRGladman})},{"./cipher-core":3,"./core":4}],16:[function(require,module,exports){(function(root,factory,undef){if(typeof exports==="object"){module.exports=exports=factory(require("./core"),require("./cipher-core"))}else if(typeof define==="function"&&define.amd){define(["./core","./cipher-core"],factory)}else{factory(root.CryptoJS)}})(this,function(CryptoJS){CryptoJS.mode.CTR=function(){var CTR=CryptoJS.lib.BlockCipherMode.extend();var Encryptor=CTR.Encryptor=CTR.extend({processBlock:function(words,offset){var cipher=this._cipher;var blockSize=cipher.blockSize;var iv=this._iv;var counter=this._counter;if(iv){counter=this._counter=iv.slice(0);this._iv=undefined}var keystream=counter.slice(0);cipher.encryptBlock(keystream,0);counter[blockSize-1]=counter[blockSize-1]+1|0;for(var i=0;i<blockSize;i++){words[offset+i]^=keystream[i]}}});CTR.Decryptor=Encryptor;return CTR}();return CryptoJS.mode.CTR})},{"./cipher-core":3,"./core":4}],17:[function(require,module,exports){(function(root,factory,undef){if(typeof exports==="object"){module.exports=exports=factory(require("./core"),require("./cipher-core"))}else if(typeof define==="function"&&define.amd){define(["./core","./cipher-core"],factory)}else{factory(root.CryptoJS)}})(this,function(CryptoJS){CryptoJS.mode.ECB=function(){var ECB=CryptoJS.lib.BlockCipherMode.extend();ECB.Encryptor=ECB.extend({processBlock:function(words,offset){this._cipher.encryptBlock(words,offset)}});ECB.Decryptor=ECB.extend({processBlock:function(words,offset){this._cipher.decryptBlock(words,offset)}});return ECB}();return CryptoJS.mode.ECB})},{"./cipher-core":3,"./core":4}],18:[function(require,module,exports){(function(root,factory,undef){if(typeof exports==="object"){module.exports=exports=factory(require("./core"),require("./cipher-core"))}else if(typeof define==="function"&&define.amd){define(["./core","./cipher-core"],factory)}else{factory(root.CryptoJS)}})(this,function(CryptoJS){CryptoJS.mode.OFB=function(){var OFB=CryptoJS.lib.BlockCipherMode.extend();var Encryptor=OFB.Encryptor=OFB.extend({processBlock:function(words,offset){var cipher=this._cipher;var blockSize=cipher.blockSize;var iv=this._iv;var keystream=this._keystream;if(iv){keystream=this._keystream=iv.slice(0);this._iv=undefined}cipher.encryptBlock(keystream,0);for(var i=0;i<blockSize;i++){words[offset+i]^=keystream[i]}}});OFB.Decryptor=Encryptor;return OFB}();return CryptoJS.mode.OFB})},{"./cipher-core":3,"./core":4}],19:[function(require,module,exports){(function(root,factory,undef){if(typeof exports==="object"){module.exports=exports=factory(require("./core"),require("./cipher-core"))}else if(typeof define==="function"&&define.amd){define(["./core","./cipher-core"],factory)}else{factory(root.CryptoJS)}})(this,function(CryptoJS){CryptoJS.pad.AnsiX923={pad:function(data,blockSize){var dataSigBytes=data.sigBytes;var blockSizeBytes=blockSize*4;var nPaddingBytes=blockSizeBytes-dataSigBytes%blockSizeBytes;var lastBytePos=dataSigBytes+nPaddingBytes-1;data.clamp();data.words[lastBytePos>>>2]|=nPaddingBytes<<24-lastBytePos%4*8;data.sigBytes+=nPaddingBytes},unpad:function(data){var nPaddingBytes=data.words[data.sigBytes-1>>>2]&255;data.sigBytes-=nPaddingBytes}};return CryptoJS.pad.Ansix923})},{"./cipher-core":3,"./core":4}],20:[function(require,module,exports){(function(root,factory,undef){if(typeof exports==="object"){module.exports=exports=factory(require("./core"),require("./cipher-core"))}else if(typeof define==="function"&&define.amd){define(["./core","./cipher-core"],factory)}else{factory(root.CryptoJS)}})(this,function(CryptoJS){CryptoJS.pad.Iso10126={pad:function(data,blockSize){var blockSizeBytes=blockSize*4;var nPaddingBytes=blockSizeBytes-data.sigBytes%blockSizeBytes;data.concat(CryptoJS.lib.WordArray.random(nPaddingBytes-1)).concat(CryptoJS.lib.WordArray.create([nPaddingBytes<<24],1))},unpad:function(data){var nPaddingBytes=data.words[data.sigBytes-1>>>2]&255;data.sigBytes-=nPaddingBytes}};return CryptoJS.pad.Iso10126})},{"./cipher-core":3,"./core":4}],21:[function(require,module,exports){(function(root,factory,undef){if(typeof exports==="object"){module.exports=exports=factory(require("./core"),require("./cipher-core"))}else if(typeof define==="function"&&define.amd){define(["./core","./cipher-core"],factory)}else{factory(root.CryptoJS)}})(this,function(CryptoJS){CryptoJS.pad.Iso97971={pad:function(data,blockSize){data.concat(CryptoJS.lib.WordArray.create([2147483648],1));CryptoJS.pad.ZeroPadding.pad(data,blockSize)},unpad:function(data){CryptoJS.pad.ZeroPadding.unpad(data);data.sigBytes--}};return CryptoJS.pad.Iso97971})},{"./cipher-core":3,"./core":4}],22:[function(require,module,exports){(function(root,factory,undef){if(typeof exports==="object"){module.exports=exports=factory(require("./core"),require("./cipher-core"))}else if(typeof define==="function"&&define.amd){define(["./core","./cipher-core"],factory)}else{factory(root.CryptoJS)}})(this,function(CryptoJS){CryptoJS.pad.NoPadding={pad:function(){},unpad:function(){}};return CryptoJS.pad.NoPadding})},{"./cipher-core":3,"./core":4}],23:[function(require,module,exports){(function(root,factory,undef){if(typeof exports==="object"){module.exports=exports=factory(require("./core"),require("./cipher-core"))}else if(typeof define==="function"&&define.amd){define(["./core","./cipher-core"],factory)}else{factory(root.CryptoJS)}})(this,function(CryptoJS){CryptoJS.pad.ZeroPadding={pad:function(data,blockSize){var blockSizeBytes=blockSize*4;data.clamp();data.sigBytes+=blockSizeBytes-(data.sigBytes%blockSizeBytes||blockSizeBytes)},unpad:function(data){var dataWords=data.words;var i=data.sigBytes-1;for(var i=data.sigBytes-1;i>=0;i--){if(dataWords[i>>>2]>>>24-i%4*8&255){data.sigBytes=i+1;break}}}};return CryptoJS.pad.ZeroPadding})},{"./cipher-core":3,"./core":4}],24:[function(require,module,exports){(function(root,factory,undef){if(typeof exports==="object"){module.exports=exports=factory(require("./core"),require("./sha1"),require("./hmac"))}else if(typeof define==="function"&&define.amd){define(["./core","./sha1","./hmac"],factory)}else{factory(root.CryptoJS)}})(this,function(CryptoJS){(function(){var C=CryptoJS;var C_lib=C.lib;var Base=C_lib.Base;var WordArray=C_lib.WordArray;var C_algo=C.algo;var SHA1=C_algo.SHA1;var HMAC=C_algo.HMAC;var PBKDF2=C_algo.PBKDF2=Base.extend({cfg:Base.extend({keySize:128/32,hasher:SHA1,iterations:1}),init:function(cfg){this.cfg=this.cfg.extend(cfg)},compute:function(password,salt){var cfg=this.cfg;var hmac=HMAC.create(cfg.hasher,password);var derivedKey=WordArray.create();var blockIndex=WordArray.create([1]);var derivedKeyWords=derivedKey.words;var blockIndexWords=blockIndex.words;var keySize=cfg.keySize;var iterations=cfg.iterations;while(derivedKeyWords.length<keySize){var block=hmac.update(salt).finalize(blockIndex);hmac.reset();var blockWords=block.words;var blockWordsLength=blockWords.length;var intermediate=block;for(var i=1;i<iterations;i++){intermediate=hmac.finalize(intermediate);hmac.reset();var intermediateWords=intermediate.words;for(var j=0;j<blockWordsLength;j++){blockWords[j]^=intermediateWords[j]}}derivedKey.concat(block);blockIndexWords[0]++}derivedKey.sigBytes=keySize*4;return derivedKey}});C.PBKDF2=function(password,salt,cfg){return PBKDF2.create(cfg).compute(password,salt)}})();return CryptoJS.PBKDF2})},{"./core":4,"./hmac":10,"./sha1":29}],25:[function(require,module,exports){(function(root,factory,undef){if(typeof exports==="object"){module.exports=exports=factory(require("./core"),require("./enc-base64"),require("./md5"),require("./evpkdf"),require("./cipher-core"))}else if(typeof define==="function"&&define.amd){define(["./core","./enc-base64","./md5","./evpkdf","./cipher-core"],factory)}else{factory(root.CryptoJS)}})(this,function(CryptoJS){(function(){var C=CryptoJS;var C_lib=C.lib;var StreamCipher=C_lib.StreamCipher;var C_algo=C.algo;var S=[];var C_=[];var G=[];var RabbitLegacy=C_algo.RabbitLegacy=StreamCipher.extend({_doReset:function(){var K=this._key.words;var iv=this.cfg.iv;var X=this._X=[K[0],K[3]<<16|K[2]>>>16,K[1],K[0]<<16|K[3]>>>16,K[2],K[1]<<16|K[0]>>>16,K[3],K[2]<<16|K[1]>>>16];var C=this._C=[K[2]<<16|K[2]>>>16,K[0]&4294901760|K[1]&65535,K[3]<<16|K[3]>>>16,K[1]&4294901760|K[2]&65535,K[0]<<16|K[0]>>>16,K[2]&4294901760|K[3]&65535,K[1]<<16|K[1]>>>16,K[3]&4294901760|K[0]&65535];this._b=0;for(var i=0;i<4;i++){nextState.call(this)}for(var i=0;i<8;i++){C[i]^=X[i+4&7]}if(iv){var IV=iv.words;var IV_0=IV[0];var IV_1=IV[1];var i0=(IV_0<<8|IV_0>>>24)&16711935|(IV_0<<24|IV_0>>>8)&4278255360;var i2=(IV_1<<8|IV_1>>>24)&16711935|(IV_1<<24|IV_1>>>8)&4278255360;var i1=i0>>>16|i2&4294901760;var i3=i2<<16|i0&65535;C[0]^=i0;C[1]^=i1;C[2]^=i2;C[3]^=i3;C[4]^=i0;C[5]^=i1;C[6]^=i2;C[7]^=i3;for(var i=0;i<4;i++){nextState.call(this)}}},_doProcessBlock:function(M,offset){var X=this._X;nextState.call(this);S[0]=X[0]^X[5]>>>16^X[3]<<16;S[1]=X[2]^X[7]>>>16^X[5]<<16;S[2]=X[4]^X[1]>>>16^X[7]<<16;S[3]=X[6]^X[3]>>>16^X[1]<<16;for(var i=0;i<4;i++){S[i]=(S[i]<<8|S[i]>>>24)&16711935|(S[i]<<24|S[i]>>>8)&4278255360;M[offset+i]^=S[i]}},blockSize:128/32,ivSize:64/32});function nextState(){var X=this._X;var C=this._C;for(var i=0;i<8;i++){C_[i]=C[i]}C[0]=C[0]+1295307597+this._b|0;C[1]=C[1]+3545052371+(C[0]>>>0<C_[0]>>>0?1:0)|0;C[2]=C[2]+886263092+(C[1]>>>0<C_[1]>>>0?1:0)|0;C[3]=C[3]+1295307597+(C[2]>>>0<C_[2]>>>0?1:0)|0;C[4]=C[4]+3545052371+(C[3]>>>0<C_[3]>>>0?1:0)|0;C[5]=C[5]+886263092+(C[4]>>>0<C_[4]>>>0?1:0)|0;C[6]=C[6]+1295307597+(C[5]>>>0<C_[5]>>>0?1:0)|0;C[7]=C[7]+3545052371+(C[6]>>>0<C_[6]>>>0?1:0)|0;this._b=C[7]>>>0<C_[7]>>>0?1:0;for(var i=0;i<8;i++){var gx=X[i]+C[i];var ga=gx&65535;var gb=gx>>>16;var gh=((ga*ga>>>17)+ga*gb>>>15)+gb*gb;var gl=((gx&4294901760)*gx|0)+((gx&65535)*gx|0);G[i]=gh^gl}X[0]=G[0]+(G[7]<<16|G[7]>>>16)+(G[6]<<16|G[6]>>>16)|0;X[1]=G[1]+(G[0]<<8|G[0]>>>24)+G[7]|0;X[2]=G[2]+(G[1]<<16|G[1]>>>16)+(G[0]<<16|G[0]>>>16)|0;X[3]=G[3]+(G[2]<<8|G[2]>>>24)+G[1]|0;X[4]=G[4]+(G[3]<<16|G[3]>>>16)+(G[2]<<16|G[2]>>>16)|0;X[5]=G[5]+(G[4]<<8|G[4]>>>24)+G[3]|0;X[6]=G[6]+(G[5]<<16|G[5]>>>16)+(G[4]<<16|G[4]>>>16)|0;X[7]=G[7]+(G[6]<<8|G[6]>>>24)+G[5]|0}C.RabbitLegacy=StreamCipher._createHelper(RabbitLegacy)})();return CryptoJS.RabbitLegacy})},{"./cipher-core":3,"./core":4,"./enc-base64":5,"./evpkdf":8,"./md5":13}],26:[function(require,module,exports){(function(root,factory,undef){if(typeof exports==="object"){module.exports=exports=factory(require("./core"),require("./enc-base64"),require("./md5"),require("./evpkdf"),require("./cipher-core"))}else if(typeof define==="function"&&define.amd){define(["./core","./enc-base64","./md5","./evpkdf","./cipher-core"],factory)}else{factory(root.CryptoJS)}})(this,function(CryptoJS){(function(){var C=CryptoJS;var C_lib=C.lib;var StreamCipher=C_lib.StreamCipher;var C_algo=C.algo;var S=[];var C_=[];var G=[];var Rabbit=C_algo.Rabbit=StreamCipher.extend({_doReset:function(){var K=this._key.words;var iv=this.cfg.iv;for(var i=0;i<4;i++){K[i]=(K[i]<<8|K[i]>>>24)&16711935|(K[i]<<24|K[i]>>>8)&4278255360}var X=this._X=[K[0],K[3]<<16|K[2]>>>16,K[1],K[0]<<16|K[3]>>>16,K[2],K[1]<<16|K[0]>>>16,K[3],K[2]<<16|K[1]>>>16];var C=this._C=[K[2]<<16|K[2]>>>16,K[0]&4294901760|K[1]&65535,K[3]<<16|K[3]>>>16,K[1]&4294901760|K[2]&65535,K[0]<<16|K[0]>>>16,K[2]&4294901760|K[3]&65535,K[1]<<16|K[1]>>>16,K[3]&4294901760|K[0]&65535];this._b=0;for(var i=0;i<4;i++){nextState.call(this)}for(var i=0;i<8;i++){C[i]^=X[i+4&7]}if(iv){var IV=iv.words;var IV_0=IV[0];var IV_1=IV[1];var i0=(IV_0<<8|IV_0>>>24)&16711935|(IV_0<<24|IV_0>>>8)&4278255360;var i2=(IV_1<<8|IV_1>>>24)&16711935|(IV_1<<24|IV_1>>>8)&4278255360;var i1=i0>>>16|i2&4294901760;var i3=i2<<16|i0&65535;C[0]^=i0;C[1]^=i1;C[2]^=i2;C[3]^=i3;C[4]^=i0;C[5]^=i1;C[6]^=i2;C[7]^=i3;for(var i=0;i<4;i++){nextState.call(this)}}},_doProcessBlock:function(M,offset){var X=this._X;nextState.call(this);S[0]=X[0]^X[5]>>>16^X[3]<<16;S[1]=X[2]^X[7]>>>16^X[5]<<16;S[2]=X[4]^X[1]>>>16^X[7]<<16;S[3]=X[6]^X[3]>>>16^X[1]<<16;for(var i=0;i<4;i++){S[i]=(S[i]<<8|S[i]>>>24)&16711935|(S[i]<<24|S[i]>>>8)&4278255360;M[offset+i]^=S[i]}},blockSize:128/32,ivSize:64/32});function nextState(){var X=this._X;var C=this._C;for(var i=0;i<8;i++){C_[i]=C[i]}C[0]=C[0]+1295307597+this._b|0;C[1]=C[1]+3545052371+(C[0]>>>0<C_[0]>>>0?1:0)|0;C[2]=C[2]+886263092+(C[1]>>>0<C_[1]>>>0?1:0)|0;C[3]=C[3]+1295307597+(C[2]>>>0<C_[2]>>>0?1:0)|0;C[4]=C[4]+3545052371+(C[3]>>>0<C_[3]>>>0?1:0)|0;C[5]=C[5]+886263092+(C[4]>>>0<C_[4]>>>0?1:0)|0;C[6]=C[6]+1295307597+(C[5]>>>0<C_[5]>>>0?1:0)|0;C[7]=C[7]+3545052371+(C[6]>>>0<C_[6]>>>0?1:0)|0;this._b=C[7]>>>0<C_[7]>>>0?1:0;for(var i=0;i<8;i++){var gx=X[i]+C[i];var ga=gx&65535;var gb=gx>>>16;var gh=((ga*ga>>>17)+ga*gb>>>15)+gb*gb;var gl=((gx&4294901760)*gx|0)+((gx&65535)*gx|0);G[i]=gh^gl}X[0]=G[0]+(G[7]<<16|G[7]>>>16)+(G[6]<<16|G[6]>>>16)|0;X[1]=G[1]+(G[0]<<8|G[0]>>>24)+G[7]|0;X[2]=G[2]+(G[1]<<16|G[1]>>>16)+(G[0]<<16|G[0]>>>16)|0;X[3]=G[3]+(G[2]<<8|G[2]>>>24)+G[1]|0;X[4]=G[4]+(G[3]<<16|G[3]>>>16)+(G[2]<<16|G[2]>>>16)|0;X[5]=G[5]+(G[4]<<8|G[4]>>>24)+G[3]|0;X[6]=G[6]+(G[5]<<16|G[5]>>>16)+(G[4]<<16|G[4]>>>16)|0;X[7]=G[7]+(G[6]<<8|G[6]>>>24)+G[5]|0}C.Rabbit=StreamCipher._createHelper(Rabbit)})();return CryptoJS.Rabbit})},{"./cipher-core":3,"./core":4,"./enc-base64":5,"./evpkdf":8,"./md5":13}],27:[function(require,module,exports){(function(root,factory,undef){if(typeof exports==="object"){module.exports=exports=factory(require("./core"),require("./enc-base64"),require("./md5"),require("./evpkdf"),require("./cipher-core"))}else if(typeof define==="function"&&define.amd){define(["./core","./enc-base64","./md5","./evpkdf","./cipher-core"],factory)}else{factory(root.CryptoJS)}})(this,function(CryptoJS){(function(){var C=CryptoJS;var C_lib=C.lib;var StreamCipher=C_lib.StreamCipher;var C_algo=C.algo;var RC4=C_algo.RC4=StreamCipher.extend({_doReset:function(){var key=this._key;var keyWords=key.words;var keySigBytes=key.sigBytes;var S=this._S=[];for(var i=0;i<256;i++){S[i]=i}for(var i=0,j=0;i<256;i++){var keyByteIndex=i%keySigBytes;var keyByte=keyWords[keyByteIndex>>>2]>>>24-keyByteIndex%4*8&255;j=(j+S[i]+keyByte)%256;var t=S[i];S[i]=S[j];S[j]=t}this._i=this._j=0},_doProcessBlock:function(M,offset){M[offset]^=generateKeystreamWord.call(this)},keySize:256/32,ivSize:0});function generateKeystreamWord(){var S=this._S;var i=this._i;var j=this._j;var keystreamWord=0;for(var n=0;n<4;n++){i=(i+1)%256;j=(j+S[i])%256;var t=S[i];S[i]=S[j];S[j]=t;keystreamWord|=S[(S[i]+S[j])%256]<<24-n*8}this._i=i;this._j=j;return keystreamWord}C.RC4=StreamCipher._createHelper(RC4);var RC4Drop=C_algo.RC4Drop=RC4.extend({cfg:RC4.cfg.extend({drop:192}),_doReset:function(){RC4._doReset.call(this);for(var i=this.cfg.drop;i>0;i--){generateKeystreamWord.call(this)}}});C.RC4Drop=StreamCipher._createHelper(RC4Drop)})();return CryptoJS.RC4})},{"./cipher-core":3,"./core":4,"./enc-base64":5,"./evpkdf":8,"./md5":13}],28:[function(require,module,exports){(function(root,factory){if(typeof exports==="object"){module.exports=exports=factory(require("./core"))}else if(typeof define==="function"&&define.amd){define(["./core"],factory)}else{factory(root.CryptoJS)}})(this,function(CryptoJS){(function(Math){var C=CryptoJS;var C_lib=C.lib;var WordArray=C_lib.WordArray;var Hasher=C_lib.Hasher;var C_algo=C.algo;var _zl=WordArray.create([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,7,4,13,1,10,6,15,3,12,0,9,5,2,14,11,8,3,10,14,4,9,15,8,1,2,7,0,6,13,11,5,12,1,9,11,10,0,8,12,4,13,3,7,15,14,5,6,2,4,0,5,9,7,12,2,10,14,1,3,8,11,6,15,13]);var _zr=WordArray.create([5,14,7,0,9,2,11,4,13,6,15,8,1,10,3,12,6,11,3,7,0,13,5,10,14,15,8,12,4,9,1,2,15,5,1,3,7,14,6,9,11,8,12,2,10,0,4,13,8,6,4,1,3,11,15,0,5,12,2,13,9,7,10,14,12,15,10,4,1,5,8,7,6,2,13,14,0,3,9,11]);var _sl=WordArray.create([11,14,15,12,5,8,7,9,11,13,14,15,6,7,9,8,7,6,8,13,11,9,7,15,7,12,15,9,11,7,13,12,11,13,6,7,14,9,13,15,14,8,13,6,5,12,7,5,11,12,14,15,14,15,9,8,9,14,5,6,8,6,5,12,9,15,5,11,6,8,13,12,5,12,13,14,11,8,5,6]);var _sr=WordArray.create([8,9,9,11,13,15,15,5,7,7,8,11,14,14,12,6,9,13,15,7,12,8,9,11,7,7,12,7,6,15,13,11,9,7,15,11,8,6,6,14,12,13,5,14,13,13,7,5,15,5,8,11,14,14,6,14,6,9,12,9,12,5,15,8,8,5,12,9,12,5,14,6,8,13,6,5,15,13,11,11]);var _hl=WordArray.create([0,1518500249,1859775393,2400959708,2840853838]);var _hr=WordArray.create([1352829926,1548603684,1836072691,2053994217,0]);var RIPEMD160=C_algo.RIPEMD160=Hasher.extend({_doReset:function(){this._hash=WordArray.create([1732584193,4023233417,2562383102,271733878,3285377520])},_doProcessBlock:function(M,offset){for(var i=0;i<16;i++){var offset_i=offset+i;var M_offset_i=M[offset_i];M[offset_i]=(M_offset_i<<8|M_offset_i>>>24)&16711935|(M_offset_i<<24|M_offset_i>>>8)&4278255360}var H=this._hash.words;var hl=_hl.words;var hr=_hr.words;var zl=_zl.words;var zr=_zr.words;var sl=_sl.words;var sr=_sr.words;var al,bl,cl,dl,el;var ar,br,cr,dr,er;ar=al=H[0];br=bl=H[1];cr=cl=H[2];dr=dl=H[3];er=el=H[4];var t;for(var i=0;i<80;i+=1){t=al+M[offset+zl[i]]|0;if(i<16){t+=f1(bl,cl,dl)+hl[0]}else if(i<32){t+=f2(bl,cl,dl)+hl[1]}else if(i<48){t+=f3(bl,cl,dl)+hl[2]}else if(i<64){t+=f4(bl,cl,dl)+hl[3]}else{t+=f5(bl,cl,dl)+hl[4]}t=t|0;t=rotl(t,sl[i]);t=t+el|0;al=el;el=dl;dl=rotl(cl,10);cl=bl;bl=t;t=ar+M[offset+zr[i]]|0;if(i<16){t+=f5(br,cr,dr)+hr[0]}else if(i<32){t+=f4(br,cr,dr)+hr[1]}else if(i<48){t+=f3(br,cr,dr)+hr[2]}else if(i<64){t+=f2(br,cr,dr)+hr[3]}else{t+=f1(br,cr,dr)+hr[4]}t=t|0;t=rotl(t,sr[i]);t=t+er|0;ar=er;er=dr;dr=rotl(cr,10);cr=br;br=t}t=H[1]+cl+dr|0;H[1]=H[2]+dl+er|0;H[2]=H[3]+el+ar|0;H[3]=H[4]+al+br|0;H[4]=H[0]+bl+cr|0;H[0]=t},_doFinalize:function(){var data=this._data;var dataWords=data.words;var nBitsTotal=this._nDataBytes*8;var nBitsLeft=data.sigBytes*8;dataWords[nBitsLeft>>>5]|=128<<24-nBitsLeft%32;dataWords[(nBitsLeft+64>>>9<<4)+14]=(nBitsTotal<<8|nBitsTotal>>>24)&16711935|(nBitsTotal<<24|nBitsTotal>>>8)&4278255360;data.sigBytes=(dataWords.length+1)*4;this._process();var hash=this._hash;var H=hash.words;for(var i=0;i<5;i++){var H_i=H[i];H[i]=(H_i<<8|H_i>>>24)&16711935|(H_i<<24|H_i>>>8)&4278255360}return hash},clone:function(){var clone=Hasher.clone.call(this);clone._hash=this._hash.clone();return clone}});function f1(x,y,z){return x^y^z}function f2(x,y,z){return x&y|~x&z}function f3(x,y,z){return(x|~y)^z}function f4(x,y,z){return x&z|y&~z}function f5(x,y,z){return x^(y|~z)}function rotl(x,n){return x<<n|x>>>32-n}C.RIPEMD160=Hasher._createHelper(RIPEMD160);C.HmacRIPEMD160=Hasher._createHmacHelper(RIPEMD160)})(Math);return CryptoJS.RIPEMD160})},{"./core":4}],29:[function(require,module,exports){(function(root,factory){if(typeof exports==="object"){module.exports=exports=factory(require("./core"))}else if(typeof define==="function"&&define.amd){define(["./core"],factory)}else{factory(root.CryptoJS)}})(this,function(CryptoJS){(function(){var C=CryptoJS;var C_lib=C.lib;var WordArray=C_lib.WordArray;var Hasher=C_lib.Hasher;var C_algo=C.algo;var W=[];var SHA1=C_algo.SHA1=Hasher.extend({_doReset:function(){this._hash=new WordArray.init([1732584193,4023233417,2562383102,271733878,3285377520])},_doProcessBlock:function(M,offset){var H=this._hash.words;var a=H[0];var b=H[1];var c=H[2];var d=H[3];var e=H[4];for(var i=0;i<80;i++){if(i<16){W[i]=M[offset+i]|0}else{var n=W[i-3]^W[i-8]^W[i-14]^W[i-16];W[i]=n<<1|n>>>31}var t=(a<<5|a>>>27)+e+W[i];if(i<20){t+=(b&c|~b&d)+1518500249}else if(i<40){t+=(b^c^d)+1859775393}else if(i<60){t+=(b&c|b&d|c&d)-1894007588}else{t+=(b^c^d)-899497514}e=d;d=c;c=b<<30|b>>>2;b=a;a=t}H[0]=H[0]+a|0;H[1]=H[1]+b|0;H[2]=H[2]+c|0;H[3]=H[3]+d|0;H[4]=H[4]+e|0},_doFinalize:function(){var data=this._data;var dataWords=data.words;var nBitsTotal=this._nDataBytes*8;var nBitsLeft=data.sigBytes*8;dataWords[nBitsLeft>>>5]|=128<<24-nBitsLeft%32;dataWords[(nBitsLeft+64>>>9<<4)+14]=Math.floor(nBitsTotal/4294967296);dataWords[(nBitsLeft+64>>>9<<4)+15]=nBitsTotal;data.sigBytes=dataWords.length*4;this._process();return this._hash},clone:function(){var clone=Hasher.clone.call(this);clone._hash=this._hash.clone();return clone}});C.SHA1=Hasher._createHelper(SHA1);C.HmacSHA1=Hasher._createHmacHelper(SHA1)})();return CryptoJS.SHA1})},{"./core":4}],30:[function(require,module,exports){(function(root,factory,undef){if(typeof exports==="object"){module.exports=exports=factory(require("./core"),require("./sha256"))}else if(typeof define==="function"&&define.amd){define(["./core","./sha256"],factory)}else{factory(root.CryptoJS)}})(this,function(CryptoJS){(function(){var C=CryptoJS;var C_lib=C.lib;var WordArray=C_lib.WordArray;var C_algo=C.algo;var SHA256=C_algo.SHA256;var SHA224=C_algo.SHA224=SHA256.extend({_doReset:function(){this._hash=new WordArray.init([3238371032,914150663,812702999,4144912697,4290775857,1750603025,1694076839,3204075428])},_doFinalize:function(){var hash=SHA256._doFinalize.call(this);hash.sigBytes-=4;return hash}});C.SHA224=SHA256._createHelper(SHA224);C.HmacSHA224=SHA256._createHmacHelper(SHA224)})();return CryptoJS.SHA224})},{"./core":4,"./sha256":31}],31:[function(require,module,exports){(function(root,factory){if(typeof exports==="object"){module.exports=exports=factory(require("./core"))}else if(typeof define==="function"&&define.amd){define(["./core"],factory)}else{factory(root.CryptoJS)}})(this,function(CryptoJS){(function(Math){var C=CryptoJS;var C_lib=C.lib;var WordArray=C_lib.WordArray;var Hasher=C_lib.Hasher;var C_algo=C.algo;var H=[];var K=[];(function(){function isPrime(n){var sqrtN=Math.sqrt(n);for(var factor=2;factor<=sqrtN;factor++){if(!(n%factor)){return false}}return true}function getFractionalBits(n){return(n-(n|0))*4294967296|0}var n=2;var nPrime=0;while(nPrime<64){if(isPrime(n)){if(nPrime<8){H[nPrime]=getFractionalBits(Math.pow(n,1/2))}K[nPrime]=getFractionalBits(Math.pow(n,1/3));nPrime++}n++}})();var W=[];var SHA256=C_algo.SHA256=Hasher.extend({_doReset:function(){this._hash=new WordArray.init(H.slice(0))},_doProcessBlock:function(M,offset){var H=this._hash.words;var a=H[0];var b=H[1];var c=H[2];var d=H[3];var e=H[4];var f=H[5];var g=H[6];var h=H[7];for(var i=0;i<64;i++){if(i<16){W[i]=M[offset+i]|0}else{var gamma0x=W[i-15];var gamma0=(gamma0x<<25|gamma0x>>>7)^(gamma0x<<14|gamma0x>>>18)^gamma0x>>>3;var gamma1x=W[i-2];var gamma1=(gamma1x<<15|gamma1x>>>17)^(gamma1x<<13|gamma1x>>>19)^gamma1x>>>10;W[i]=gamma0+W[i-7]+gamma1+W[i-16]}var ch=e&f^~e&g;var maj=a&b^a&c^b&c;var sigma0=(a<<30|a>>>2)^(a<<19|a>>>13)^(a<<10|a>>>22);var sigma1=(e<<26|e>>>6)^(e<<21|e>>>11)^(e<<7|e>>>25);var t1=h+sigma1+ch+K[i]+W[i];var t2=sigma0+maj;h=g;g=f;f=e;e=d+t1|0;d=c;c=b;b=a;a=t1+t2|0}H[0]=H[0]+a|0;H[1]=H[1]+b|0;H[2]=H[2]+c|0;H[3]=H[3]+d|0;H[4]=H[4]+e|0;H[5]=H[5]+f|0;H[6]=H[6]+g|0;H[7]=H[7]+h|0},_doFinalize:function(){var data=this._data;var dataWords=data.words;var nBitsTotal=this._nDataBytes*8;var nBitsLeft=data.sigBytes*8;dataWords[nBitsLeft>>>5]|=128<<24-nBitsLeft%32;dataWords[(nBitsLeft+64>>>9<<4)+14]=Math.floor(nBitsTotal/4294967296);dataWords[(nBitsLeft+64>>>9<<4)+15]=nBitsTotal;data.sigBytes=dataWords.length*4;this._process();return this._hash},clone:function(){var clone=Hasher.clone.call(this);clone._hash=this._hash.clone();return clone}});C.SHA256=Hasher._createHelper(SHA256);C.HmacSHA256=Hasher._createHmacHelper(SHA256)})(Math);return CryptoJS.SHA256})},{"./core":4}],32:[function(require,module,exports){(function(root,factory,undef){if(typeof exports==="object"){module.exports=exports=factory(require("./core"),require("./x64-core"))}else if(typeof define==="function"&&define.amd){define(["./core","./x64-core"],factory)}else{factory(root.CryptoJS)}})(this,function(CryptoJS){(function(Math){var C=CryptoJS;var C_lib=C.lib;var WordArray=C_lib.WordArray;var Hasher=C_lib.Hasher;var C_x64=C.x64;var X64Word=C_x64.Word;var C_algo=C.algo;var RHO_OFFSETS=[];var PI_INDEXES=[];var ROUND_CONSTANTS=[];(function(){var x=1,y=0;for(var t=0;t<24;t++){RHO_OFFSETS[x+5*y]=(t+1)*(t+2)/2%64;var newX=y%5;var newY=(2*x+3*y)%5;x=newX;y=newY}for(var x=0;x<5;x++){for(var y=0;y<5;y++){PI_INDEXES[x+5*y]=y+(2*x+3*y)%5*5}}var LFSR=1;for(var i=0;i<24;i++){var roundConstantMsw=0;var roundConstantLsw=0;for(var j=0;j<7;j++){if(LFSR&1){var bitPosition=(1<<j)-1;if(bitPosition<32){roundConstantLsw^=1<<bitPosition}else{roundConstantMsw^=1<<bitPosition-32}}if(LFSR&128){LFSR=LFSR<<1^113}else{LFSR<<=1}}ROUND_CONSTANTS[i]=X64Word.create(roundConstantMsw,roundConstantLsw)}})();var T=[];(function(){for(var i=0;i<25;i++){T[i]=X64Word.create()}})();var SHA3=C_algo.SHA3=Hasher.extend({cfg:Hasher.cfg.extend({outputLength:512}),_doReset:function(){var state=this._state=[];for(var i=0;i<25;i++){state[i]=new X64Word.init}this.blockSize=(1600-2*this.cfg.outputLength)/32},_doProcessBlock:function(M,offset){var state=this._state;var nBlockSizeLanes=this.blockSize/2;for(var i=0;i<nBlockSizeLanes;i++){var M2i=M[offset+2*i];var M2i1=M[offset+2*i+1];M2i=(M2i<<8|M2i>>>24)&16711935|(M2i<<24|M2i>>>8)&4278255360;M2i1=(M2i1<<8|M2i1>>>24)&16711935|(M2i1<<24|M2i1>>>8)&4278255360;var lane=state[i];lane.high^=M2i1;lane.low^=M2i}for(var round=0;round<24;round++){for(var x=0;x<5;x++){var tMsw=0,tLsw=0;for(var y=0;y<5;y++){var lane=state[x+5*y];tMsw^=lane.high;tLsw^=lane.low}var Tx=T[x];Tx.high=tMsw;Tx.low=tLsw}for(var x=0;x<5;x++){var Tx4=T[(x+4)%5];var Tx1=T[(x+1)%5];var Tx1Msw=Tx1.high;var Tx1Lsw=Tx1.low;var tMsw=Tx4.high^(Tx1Msw<<1|Tx1Lsw>>>31);var tLsw=Tx4.low^(Tx1Lsw<<1|Tx1Msw>>>31);for(var y=0;y<5;y++){var lane=state[x+5*y];lane.high^=tMsw;lane.low^=tLsw}}for(var laneIndex=1;laneIndex<25;laneIndex++){var tMsw;var tLsw;var lane=state[laneIndex];var laneMsw=lane.high;var laneLsw=lane.low;var rhoOffset=RHO_OFFSETS[laneIndex];if(rhoOffset<32){tMsw=laneMsw<<rhoOffset|laneLsw>>>32-rhoOffset;tLsw=laneLsw<<rhoOffset|laneMsw>>>32-rhoOffset}else{tMsw=laneLsw<<rhoOffset-32|laneMsw>>>64-rhoOffset;tLsw=laneMsw<<rhoOffset-32|laneLsw>>>64-rhoOffset}var TPiLane=T[PI_INDEXES[laneIndex]];TPiLane.high=tMsw;TPiLane.low=tLsw}var T0=T[0];var state0=state[0];T0.high=state0.high;T0.low=state0.low;for(var x=0;x<5;x++){for(var y=0;y<5;y++){var laneIndex=x+5*y;var lane=state[laneIndex];var TLane=T[laneIndex];var Tx1Lane=T[(x+1)%5+5*y];var Tx2Lane=T[(x+2)%5+5*y];lane.high=TLane.high^~Tx1Lane.high&Tx2Lane.high;lane.low=TLane.low^~Tx1Lane.low&Tx2Lane.low}}var lane=state[0];var roundConstant=ROUND_CONSTANTS[round];lane.high^=roundConstant.high;lane.low^=roundConstant.low}},_doFinalize:function(){var data=this._data;var dataWords=data.words;var nBitsTotal=this._nDataBytes*8;var nBitsLeft=data.sigBytes*8;var blockSizeBits=this.blockSize*32;dataWords[nBitsLeft>>>5]|=1<<24-nBitsLeft%32;dataWords[(Math.ceil((nBitsLeft+1)/blockSizeBits)*blockSizeBits>>>5)-1]|=128;data.sigBytes=dataWords.length*4;this._process();var state=this._state;var outputLengthBytes=this.cfg.outputLength/8;var outputLengthLanes=outputLengthBytes/8;var hashWords=[];for(var i=0;i<outputLengthLanes;i++){var lane=state[i];var laneMsw=lane.high;var laneLsw=lane.low;laneMsw=(laneMsw<<8|laneMsw>>>24)&16711935|(laneMsw<<24|laneMsw>>>8)&4278255360;laneLsw=(laneLsw<<8|laneLsw>>>24)&16711935|(laneLsw<<24|laneLsw>>>8)&4278255360;hashWords.push(laneLsw);hashWords.push(laneMsw)}return new WordArray.init(hashWords,outputLengthBytes)},clone:function(){var clone=Hasher.clone.call(this);var state=clone._state=this._state.slice(0);for(var i=0;i<25;i++){state[i]=state[i].clone()}return clone}});C.SHA3=Hasher._createHelper(SHA3);C.HmacSHA3=Hasher._createHmacHelper(SHA3)})(Math);return CryptoJS.SHA3})},{"./core":4,"./x64-core":36}],33:[function(require,module,exports){(function(root,factory,undef){if(typeof exports==="object"){module.exports=exports=factory(require("./core"),require("./x64-core"),require("./sha512"))}else if(typeof define==="function"&&define.amd){define(["./core","./x64-core","./sha512"],factory)}else{factory(root.CryptoJS)}})(this,function(CryptoJS){(function(){var C=CryptoJS;var C_x64=C.x64;var X64Word=C_x64.Word;var X64WordArray=C_x64.WordArray;var C_algo=C.algo;var SHA512=C_algo.SHA512;var SHA384=C_algo.SHA384=SHA512.extend({_doReset:function(){this._hash=new X64WordArray.init([new X64Word.init(3418070365,3238371032),new X64Word.init(1654270250,914150663),new X64Word.init(2438529370,812702999),new X64Word.init(355462360,4144912697),new X64Word.init(1731405415,4290775857),new X64Word.init(2394180231,1750603025),new X64Word.init(3675008525,1694076839),new X64Word.init(1203062813,3204075428)])},_doFinalize:function(){var hash=SHA512._doFinalize.call(this);hash.sigBytes-=16;return hash}});C.SHA384=SHA512._createHelper(SHA384);C.HmacSHA384=SHA512._createHmacHelper(SHA384)})();return CryptoJS.SHA384})},{"./core":4,"./sha512":34,"./x64-core":36}],34:[function(require,module,exports){(function(root,factory,undef){if(typeof exports==="object"){module.exports=exports=factory(require("./core"),require("./x64-core"))}else if(typeof define==="function"&&define.amd){define(["./core","./x64-core"],factory)}else{factory(root.CryptoJS)}})(this,function(CryptoJS){(function(){var C=CryptoJS;var C_lib=C.lib;var Hasher=C_lib.Hasher;var C_x64=C.x64;var X64Word=C_x64.Word;var X64WordArray=C_x64.WordArray;var C_algo=C.algo;function X64Word_create(){return X64Word.create.apply(X64Word,arguments)}var K=[X64Word_create(1116352408,3609767458),X64Word_create(1899447441,602891725),X64Word_create(3049323471,3964484399),X64Word_create(3921009573,2173295548),X64Word_create(961987163,4081628472),X64Word_create(1508970993,3053834265),X64Word_create(2453635748,2937671579),X64Word_create(2870763221,3664609560),X64Word_create(3624381080,2734883394),X64Word_create(310598401,1164996542),X64Word_create(607225278,1323610764),X64Word_create(1426881987,3590304994),X64Word_create(1925078388,4068182383),X64Word_create(2162078206,991336113),X64Word_create(2614888103,633803317),X64Word_create(3248222580,3479774868),X64Word_create(3835390401,2666613458),X64Word_create(4022224774,944711139),X64Word_create(264347078,2341262773),X64Word_create(604807628,2007800933),X64Word_create(770255983,1495990901),X64Word_create(1249150122,1856431235),X64Word_create(1555081692,3175218132),X64Word_create(1996064986,2198950837),X64Word_create(2554220882,3999719339),X64Word_create(2821834349,766784016),X64Word_create(2952996808,2566594879),X64Word_create(3210313671,3203337956),X64Word_create(3336571891,1034457026),X64Word_create(3584528711,2466948901),X64Word_create(113926993,3758326383),X64Word_create(338241895,168717936),X64Word_create(666307205,1188179964),X64Word_create(773529912,1546045734),X64Word_create(1294757372,1522805485),X64Word_create(1396182291,2643833823),X64Word_create(1695183700,2343527390),X64Word_create(1986661051,1014477480),X64Word_create(2177026350,1206759142),X64Word_create(2456956037,344077627),X64Word_create(2730485921,1290863460),X64Word_create(2820302411,3158454273),X64Word_create(3259730800,3505952657),X64Word_create(3345764771,106217008),X64Word_create(3516065817,3606008344),X64Word_create(3600352804,1432725776),X64Word_create(4094571909,1467031594),X64Word_create(275423344,851169720),X64Word_create(430227734,3100823752),X64Word_create(506948616,1363258195),X64Word_create(659060556,3750685593),X64Word_create(883997877,3785050280),X64Word_create(958139571,3318307427),X64Word_create(1322822218,3812723403),X64Word_create(1537002063,2003034995),X64Word_create(1747873779,3602036899),X64Word_create(1955562222,1575990012),X64Word_create(2024104815,1125592928),X64Word_create(2227730452,2716904306),X64Word_create(2361852424,442776044),X64Word_create(2428436474,593698344),X64Word_create(2756734187,3733110249),X64Word_create(3204031479,2999351573),X64Word_create(3329325298,3815920427),X64Word_create(3391569614,3928383900),X64Word_create(3515267271,566280711),X64Word_create(3940187606,3454069534),X64Word_create(4118630271,4000239992),X64Word_create(116418474,1914138554),X64Word_create(174292421,2731055270),X64Word_create(289380356,3203993006),X64Word_create(460393269,320620315),X64Word_create(685471733,587496836),X64Word_create(852142971,1086792851),X64Word_create(1017036298,365543100),X64Word_create(1126000580,2618297676),X64Word_create(1288033470,3409855158),X64Word_create(1501505948,4234509866),X64Word_create(1607167915,987167468),X64Word_create(1816402316,1246189591)];var W=[];(function(){for(var i=0;i<80;i++){W[i]=X64Word_create()}})();var SHA512=C_algo.SHA512=Hasher.extend({_doReset:function(){this._hash=new X64WordArray.init([new X64Word.init(1779033703,4089235720),new X64Word.init(3144134277,2227873595),new X64Word.init(1013904242,4271175723),new X64Word.init(2773480762,1595750129),new X64Word.init(1359893119,2917565137),new X64Word.init(2600822924,725511199),new X64Word.init(528734635,4215389547),new X64Word.init(1541459225,327033209)])},_doProcessBlock:function(M,offset){var H=this._hash.words;var H0=H[0];var H1=H[1];var H2=H[2];var H3=H[3];var H4=H[4];var H5=H[5];var H6=H[6];var H7=H[7];var H0h=H0.high;var H0l=H0.low;var H1h=H1.high;var H1l=H1.low;var H2h=H2.high;var H2l=H2.low;var H3h=H3.high;var H3l=H3.low;var H4h=H4.high;var H4l=H4.low;var H5h=H5.high;var H5l=H5.low;var H6h=H6.high;var H6l=H6.low;var H7h=H7.high;var H7l=H7.low;var ah=H0h;var al=H0l;var bh=H1h;var bl=H1l;var ch=H2h;var cl=H2l;var dh=H3h;var dl=H3l;var eh=H4h;var el=H4l;var fh=H5h;var fl=H5l;var gh=H6h;var gl=H6l;var hh=H7h;var hl=H7l;for(var i=0;i<80;i++){var Wil;var Wih;var Wi=W[i];if(i<16){Wih=Wi.high=M[offset+i*2]|0;Wil=Wi.low=M[offset+i*2+1]|0}else{var gamma0x=W[i-15];var gamma0xh=gamma0x.high;var gamma0xl=gamma0x.low;var gamma0h=(gamma0xh>>>1|gamma0xl<<31)^(gamma0xh>>>8|gamma0xl<<24)^gamma0xh>>>7;var gamma0l=(gamma0xl>>>1|gamma0xh<<31)^(gamma0xl>>>8|gamma0xh<<24)^(gamma0xl>>>7|gamma0xh<<25);var gamma1x=W[i-2];var gamma1xh=gamma1x.high;var gamma1xl=gamma1x.low;var gamma1h=(gamma1xh>>>19|gamma1xl<<13)^(gamma1xh<<3|gamma1xl>>>29)^gamma1xh>>>6;var gamma1l=(gamma1xl>>>19|gamma1xh<<13)^(gamma1xl<<3|gamma1xh>>>29)^(gamma1xl>>>6|gamma1xh<<26);var Wi7=W[i-7];var Wi7h=Wi7.high;var Wi7l=Wi7.low;var Wi16=W[i-16];var Wi16h=Wi16.high;var Wi16l=Wi16.low;Wil=gamma0l+Wi7l;Wih=gamma0h+Wi7h+(Wil>>>0<gamma0l>>>0?1:0);Wil=Wil+gamma1l;Wih=Wih+gamma1h+(Wil>>>0<gamma1l>>>0?1:0);Wil=Wil+Wi16l;Wih=Wih+Wi16h+(Wil>>>0<Wi16l>>>0?1:0);Wi.high=Wih;Wi.low=Wil}var chh=eh&fh^~eh&gh;var chl=el&fl^~el&gl;var majh=ah&bh^ah&ch^bh&ch;var majl=al&bl^al&cl^bl&cl;var sigma0h=(ah>>>28|al<<4)^(ah<<30|al>>>2)^(ah<<25|al>>>7);var sigma0l=(al>>>28|ah<<4)^(al<<30|ah>>>2)^(al<<25|ah>>>7);var sigma1h=(eh>>>14|el<<18)^(eh>>>18|el<<14)^(eh<<23|el>>>9);var sigma1l=(el>>>14|eh<<18)^(el>>>18|eh<<14)^(el<<23|eh>>>9);var Ki=K[i];var Kih=Ki.high;var Kil=Ki.low;var t1l=hl+sigma1l;var t1h=hh+sigma1h+(t1l>>>0<hl>>>0?1:0);var t1l=t1l+chl;var t1h=t1h+chh+(t1l>>>0<chl>>>0?1:0);var t1l=t1l+Kil;var t1h=t1h+Kih+(t1l>>>0<Kil>>>0?1:0);var t1l=t1l+Wil;var t1h=t1h+Wih+(t1l>>>0<Wil>>>0?1:0);var t2l=sigma0l+majl;var t2h=sigma0h+majh+(t2l>>>0<sigma0l>>>0?1:0);hh=gh;hl=gl;gh=fh;gl=fl;fh=eh;fl=el;el=dl+t1l|0;eh=dh+t1h+(el>>>0<dl>>>0?1:0)|0;dh=ch;dl=cl;ch=bh;cl=bl;bh=ah;bl=al;al=t1l+t2l|0;ah=t1h+t2h+(al>>>0<t1l>>>0?1:0)|0}H0l=H0.low=H0l+al;H0.high=H0h+ah+(H0l>>>0<al>>>0?1:0);H1l=H1.low=H1l+bl;H1.high=H1h+bh+(H1l>>>0<bl>>>0?1:0);H2l=H2.low=H2l+cl;H2.high=H2h+ch+(H2l>>>0<cl>>>0?1:0);H3l=H3.low=H3l+dl;H3.high=H3h+dh+(H3l>>>0<dl>>>0?1:0);H4l=H4.low=H4l+el;H4.high=H4h+eh+(H4l>>>0<el>>>0?1:0);H5l=H5.low=H5l+fl;H5.high=H5h+fh+(H5l>>>0<fl>>>0?1:0);H6l=H6.low=H6l+gl;H6.high=H6h+gh+(H6l>>>0<gl>>>0?1:0);H7l=H7.low=H7l+hl;H7.high=H7h+hh+(H7l>>>0<hl>>>0?1:0)},_doFinalize:function(){var data=this._data;var dataWords=data.words;var nBitsTotal=this._nDataBytes*8;var nBitsLeft=data.sigBytes*8;dataWords[nBitsLeft>>>5]|=128<<24-nBitsLeft%32;dataWords[(nBitsLeft+128>>>10<<5)+30]=Math.floor(nBitsTotal/4294967296);dataWords[(nBitsLeft+128>>>10<<5)+31]=nBitsTotal;data.sigBytes=dataWords.length*4;this._process();var hash=this._hash.toX32();return hash},clone:function(){var clone=Hasher.clone.call(this);clone._hash=this._hash.clone();return clone},blockSize:1024/32});C.SHA512=Hasher._createHelper(SHA512);C.HmacSHA512=Hasher._createHmacHelper(SHA512)})();return CryptoJS.SHA512})},{"./core":4,"./x64-core":36}],35:[function(require,module,exports){(function(root,factory,undef){if(typeof exports==="object"){module.exports=exports=factory(require("./core"),require("./enc-base64"),require("./md5"),require("./evpkdf"),require("./cipher-core"))}else if(typeof define==="function"&&define.amd){define(["./core","./enc-base64","./md5","./evpkdf","./cipher-core"],factory)}else{factory(root.CryptoJS)}})(this,function(CryptoJS){(function(){var C=CryptoJS;var C_lib=C.lib;var WordArray=C_lib.WordArray;var BlockCipher=C_lib.BlockCipher;var C_algo=C.algo;var PC1=[57,49,41,33,25,17,9,1,58,50,42,34,26,18,10,2,59,51,43,35,27,19,11,3,60,52,44,36,63,55,47,39,31,23,15,7,62,54,46,38,30,22,14,6,61,53,45,37,29,21,13,5,28,20,12,4];var PC2=[14,17,11,24,1,5,3,28,15,6,21,10,23,19,12,4,26,8,16,7,27,20,13,2,41,52,31,37,47,55,30,40,51,45,33,48,44,49,39,56,34,53,46,42,50,36,29,32];var BIT_SHIFTS=[1,2,4,6,8,10,12,14,15,17,19,21,23,25,27,28];var SBOX_P=[{0:8421888,268435456:32768,536870912:8421378,805306368:2,1073741824:512,1342177280:8421890,1610612736:8389122,1879048192:8388608,2147483648:514,2415919104:8389120,2684354560:33280,2952790016:8421376,3221225472:32770,3489660928:8388610,3758096384:0,4026531840:33282,134217728:0,402653184:8421890,671088640:33282,939524096:32768,1207959552:8421888,1476395008:512,1744830464:8421378,2013265920:2,2281701376:8389120,2550136832:33280,2818572288:8421376,3087007744:8389122,3355443200:8388610,3623878656:32770,3892314112:514,4160749568:8388608,1:32768,268435457:2,536870913:8421888,805306369:8388608,1073741825:8421378,1342177281:33280,1610612737:512,1879048193:8389122,2147483649:8421890,2415919105:8421376,2684354561:8388610,2952790017:33282,3221225473:514,3489660929:8389120,3758096385:32770,4026531841:0,134217729:8421890,402653185:8421376,671088641:8388608,939524097:512,1207959553:32768,1476395009:8388610,1744830465:2,2013265921:33282,2281701377:32770,2550136833:8389122,2818572289:514,3087007745:8421888,3355443201:8389120,3623878657:0,3892314113:33280,4160749569:8421378},{0:1074282512,16777216:16384,33554432:524288,50331648:1074266128,67108864:1073741840,83886080:1074282496,100663296:1073758208,117440512:16,134217728:540672,150994944:1073758224,167772160:1073741824,184549376:540688,201326592:524304,218103808:0,234881024:16400,251658240:1074266112,8388608:1073758208,25165824:540688,41943040:16,58720256:1073758224,75497472:1074282512,92274688:1073741824,109051904:524288,125829120:1074266128,142606336:524304,159383552:0,176160768:16384,192937984:1074266112,209715200:1073741840,226492416:540672,243269632:1074282496,260046848:16400,268435456:0,285212672:1074266128,301989888:1073758224,318767104:1074282496,335544320:1074266112,352321536:16,369098752:540688,385875968:16384,402653184:16400,419430400:524288,436207616:524304,452984832:1073741840,469762048:540672,486539264:1073758208,503316480:1073741824,520093696:1074282512,276824064:540688,293601280:524288,310378496:1074266112,327155712:16384,343932928:1073758208,360710144:1074282512,377487360:16,394264576:1073741824,411041792:1074282496,427819008:1073741840,444596224:1073758224,461373440:524304,478150656:0,494927872:16400,511705088:1074266128,528482304:540672},{0:260,1048576:0,2097152:67109120,3145728:65796,4194304:65540,5242880:67108868,6291456:67174660,7340032:67174400,8388608:67108864,9437184:67174656,10485760:65792,11534336:67174404,12582912:67109124,13631488:65536,14680064:4,15728640:256,524288:67174656,1572864:67174404,2621440:0,3670016:67109120,4718592:67108868,5767168:65536,6815744:65540,7864320:260,8912896:4,9961472:256,11010048:67174400,12058624:65796,13107200:65792,14155776:67109124,15204352:67174660,16252928:67108864,16777216:67174656,17825792:65540,18874368:65536,19922944:67109120,20971520:256,22020096:67174660,23068672:67108868,24117248:0,25165824:67109124,26214400:67108864,27262976:4,28311552:65792,29360128:67174400,30408704:260,31457280:65796,32505856:67174404,17301504:67108864,18350080:260,19398656:67174656,20447232:0,21495808:65540,22544384:67109120,23592960:256,24641536:67174404,25690112:65536,26738688:67174660,27787264:65796,28835840:67108868,29884416:67109124,30932992:67174400,31981568:4,33030144:65792},{0:2151682048,65536:2147487808,131072:4198464,196608:2151677952,262144:0,327680:4198400,393216:2147483712,458752:4194368,524288:2147483648,589824:4194304,655360:64,720896:2147487744,786432:2151678016,851968:4160,917504:4096,983040:2151682112,32768:2147487808,98304:64,163840:2151678016,229376:2147487744,294912:4198400,360448:2151682112,425984:0,491520:2151677952,557056:4096,622592:2151682048,688128:4194304,753664:4160,819200:2147483648,884736:4194368,950272:4198464,1015808:2147483712,1048576:4194368,1114112:4198400,1179648:2147483712,1245184:0,1310720:4160,1376256:2151678016,1441792:2151682048,1507328:2147487808,1572864:2151682112,1638400:2147483648,1703936:2151677952,1769472:4198464,1835008:2147487744,1900544:4194304,1966080:64,2031616:4096,1081344:2151677952,1146880:2151682112,1212416:0,1277952:4198400,1343488:4194368,1409024:2147483648,1474560:2147487808,1540096:64,1605632:2147483712,1671168:4096,1736704:2147487744,1802240:2151678016,1867776:4160,1933312:2151682048,1998848:4194304,2064384:4198464},{0:128,4096:17039360,8192:262144,12288:536870912,16384:537133184,20480:16777344,24576:553648256,28672:262272,32768:16777216,36864:537133056,40960:536871040,45056:553910400,49152:553910272,53248:0,57344:17039488,61440:553648128,2048:17039488,6144:553648256,10240:128,14336:17039360,18432:262144,22528:537133184,26624:553910272,30720:536870912,34816:537133056,38912:0,43008:553910400,47104:16777344,51200:536871040,55296:553648128,59392:16777216,63488:262272,65536:262144,69632:128,73728:536870912,77824:553648256,81920:16777344,86016:553910272,90112:537133184,94208:16777216,98304:553910400,102400:553648128,106496:17039360,110592:537133056,114688:262272,118784:536871040,122880:0,126976:17039488,67584:553648256,71680:16777216,75776:17039360,79872:537133184,83968:536870912,88064:17039488,92160:128,96256:553910272,100352:262272,104448:553910400,108544:0,112640:553648128,116736:16777344,120832:262144,124928:537133056,129024:536871040},{0:268435464,256:8192,512:270532608,768:270540808,1024:268443648,1280:2097152,1536:2097160,1792:268435456,2048:0,2304:268443656,2560:2105344,2816:8,3072:270532616,3328:2105352,3584:8200,3840:270540800,128:270532608,384:270540808,640:8,896:2097152,1152:2105352,1408:268435464,1664:268443648,1920:8200,2176:2097160,2432:8192,2688:268443656,2944:270532616,3200:0,3456:270540800,3712:2105344,3968:268435456,4096:268443648,4352:270532616,4608:270540808,4864:8200,5120:2097152,5376:268435456,5632:268435464,5888:2105344,6144:2105352,6400:0,6656:8,6912:270532608,7168:8192,7424:268443656,7680:270540800,7936:2097160,4224:8,4480:2105344,4736:2097152,4992:268435464,5248:268443648,5504:8200,5760:270540808,6016:270532608,6272:270540800,6528:270532616,6784:8192,7040:2105352,7296:2097160,7552:0,7808:268435456,8064:268443656},{0:1048576,16:33555457,32:1024,48:1049601,64:34604033,80:0,96:1,112:34603009,128:33555456,144:1048577,160:33554433,176:34604032,192:34603008,208:1025,224:1049600,240:33554432,8:34603009,24:0,40:33555457,56:34604032,72:1048576,88:33554433,104:33554432,120:1025,136:1049601,152:33555456,168:34603008,184:1048577,200:1024,216:34604033,232:1,248:1049600,256:33554432,272:1048576,288:33555457,304:34603009,320:1048577,336:33555456,352:34604032,368:1049601,384:1025,400:34604033,416:1049600,432:1,448:0,464:34603008,480:33554433,496:1024,264:1049600,280:33555457,296:34603009,312:1,328:33554432,344:1048576,360:1025,376:34604032,392:33554433,408:34603008,424:0,440:34604033,456:1049601,472:1024,488:33555456,504:1048577},{0:134219808,1:131072,2:134217728,3:32,4:131104,5:134350880,6:134350848,7:2048,8:134348800,9:134219776,10:133120,11:134348832,12:2080,13:0,14:134217760,15:133152,2147483648:2048,2147483649:134350880,2147483650:134219808,2147483651:134217728,2147483652:134348800,2147483653:133120,2147483654:133152,2147483655:32,2147483656:134217760,2147483657:2080,2147483658:131104,2147483659:134350848,2147483660:0,2147483661:134348832,2147483662:134219776,2147483663:131072,16:133152,17:134350848,18:32,19:2048,20:134219776,21:134217760,22:134348832,23:131072,24:0,25:131104,26:134348800,27:134219808,28:134350880,29:133120,30:2080,31:134217728,2147483664:131072,2147483665:2048,2147483666:134348832,2147483667:133152,2147483668:32,2147483669:134348800,2147483670:134217728,2147483671:134219808,2147483672:134350880,2147483673:134217760,2147483674:134219776,2147483675:0,2147483676:133120,2147483677:2080,2147483678:131104,2147483679:134350848}];var SBOX_MASK=[4160749569,528482304,33030144,2064384,129024,8064,504,2147483679];var DES=C_algo.DES=BlockCipher.extend({_doReset:function(){var key=this._key;var keyWords=key.words;var keyBits=[];for(var i=0;i<56;i++){var keyBitPos=PC1[i]-1;keyBits[i]=keyWords[keyBitPos>>>5]>>>31-keyBitPos%32&1}var subKeys=this._subKeys=[];for(var nSubKey=0;nSubKey<16;nSubKey++){var subKey=subKeys[nSubKey]=[];var bitShift=BIT_SHIFTS[nSubKey];for(var i=0;i<24;i++){subKey[i/6|0]|=keyBits[(PC2[i]-1+bitShift)%28]<<31-i%6;subKey[4+(i/6|0)]|=keyBits[28+(PC2[i+24]-1+bitShift)%28]<<31-i%6}subKey[0]=subKey[0]<<1|subKey[0]>>>31;for(var i=1;i<7;i++){subKey[i]=subKey[i]>>>(i-1)*4+3}subKey[7]=subKey[7]<<5|subKey[7]>>>27}var invSubKeys=this._invSubKeys=[];for(var i=0;i<16;i++){invSubKeys[i]=subKeys[15-i]}},encryptBlock:function(M,offset){this._doCryptBlock(M,offset,this._subKeys)},decryptBlock:function(M,offset){this._doCryptBlock(M,offset,this._invSubKeys)},_doCryptBlock:function(M,offset,subKeys){this._lBlock=M[offset];this._rBlock=M[offset+1];exchangeLR.call(this,4,252645135);exchangeLR.call(this,16,65535);exchangeRL.call(this,2,858993459);exchangeRL.call(this,8,16711935);exchangeLR.call(this,1,1431655765);for(var round=0;round<16;round++){var subKey=subKeys[round];var lBlock=this._lBlock;var rBlock=this._rBlock;var f=0;for(var i=0;i<8;i++){f|=SBOX_P[i][((rBlock^subKey[i])&SBOX_MASK[i])>>>0]}this._lBlock=rBlock;this._rBlock=lBlock^f}var t=this._lBlock;this._lBlock=this._rBlock;this._rBlock=t;exchangeLR.call(this,1,1431655765);exchangeRL.call(this,8,16711935);exchangeRL.call(this,2,858993459);exchangeLR.call(this,16,65535);exchangeLR.call(this,4,252645135);M[offset]=this._lBlock;M[offset+1]=this._rBlock},keySize:64/32,ivSize:64/32,blockSize:64/32});function exchangeLR(offset,mask){var t=(this._lBlock>>>offset^this._rBlock)&mask;this._rBlock^=t;this._lBlock^=t<<offset}function exchangeRL(offset,mask){var t=(this._rBlock>>>offset^this._lBlock)&mask;this._lBlock^=t;this._rBlock^=t<<offset}C.DES=BlockCipher._createHelper(DES);var TripleDES=C_algo.TripleDES=BlockCipher.extend({_doReset:function(){var key=this._key;var keyWords=key.words;if(keyWords.length!==2&&keyWords.length!==4&&keyWords.length<6){throw new Error("Invalid key length - 3DES requires the key length to be 64, 128, 192 or >192.")}var key1=keyWords.slice(0,2);var key2=keyWords.length<4?keyWords.slice(0,2):keyWords.slice(2,4);var key3=keyWords.length<6?keyWords.slice(0,2):keyWords.slice(4,6);this._des1=DES.createEncryptor(WordArray.create(key1));this._des2=DES.createEncryptor(WordArray.create(key2));this._des3=DES.createEncryptor(WordArray.create(key3))},encryptBlock:function(M,offset){this._des1.encryptBlock(M,offset);this._des2.decryptBlock(M,offset);this._des3.encryptBlock(M,offset)},decryptBlock:function(M,offset){this._des3.decryptBlock(M,offset);this._des2.encryptBlock(M,offset);this._des1.decryptBlock(M,offset)},keySize:192/32,ivSize:64/32,blockSize:64/32});C.TripleDES=BlockCipher._createHelper(TripleDES)})();return CryptoJS.TripleDES})},{"./cipher-core":3,"./core":4,"./enc-base64":5,"./evpkdf":8,"./md5":13}],36:[function(require,module,exports){(function(root,factory){if(typeof exports==="object"){module.exports=exports=factory(require("./core"))}else if(typeof define==="function"&&define.amd){define(["./core"],factory)}else{factory(root.CryptoJS)}})(this,function(CryptoJS){(function(undefined){var C=CryptoJS;var C_lib=C.lib;var Base=C_lib.Base;var X32WordArray=C_lib.WordArray;var C_x64=C.x64={};var X64Word=C_x64.Word=Base.extend({init:function(high,low){this.high=high;this.low=low}});var X64WordArray=C_x64.WordArray=Base.extend({init:function(words,sigBytes){words=this.words=words||[];if(sigBytes!=undefined){this.sigBytes=sigBytes}else{this.sigBytes=words.length*8}},toX32:function(){var x64Words=this.words;var x64WordsLength=x64Words.length;var x32Words=[];for(var i=0;i<x64WordsLength;i++){var x64Word=x64Words[i];x32Words.push(x64Word.high);x32Words.push(x64Word.low)}return X32WordArray.create(x32Words,this.sigBytes)},clone:function(){var clone=Base.clone.call(this);var words=clone.words=this.words.slice(0);var wordsLength=words.length;for(var i=0;i<wordsLength;i++){words[i]=words[i].clone()}return clone}})})();return CryptoJS})},{"./core":4}],37:[function(require,module,exports){"use strict";(function(root,factory){if(typeof define==="function"&&define.amd){define(["moment"],function(moment){root.moment=factory(moment);return root.moment})}else if(typeof exports==="object"){module.exports=factory(require("moment"))}else{root.moment=factory(root.moment)}})(this,function(moment){if(moment==null){throw new Error("Cannot find moment")}var ummalqura={ummalquraData:[28607,28636,28665,28695,28724,28754,28783,28813,28843,28872,28901,28931,28960,28990,29019,29049,29078,29108,29137,29167,29196,29226,29255,29285,29315,29345,29375,29404,29434,29463,29492,29522,29551,29580,29610,29640,29669,29699,29729,29759,29788,29818,29847,29876,29906,29935,29964,29994,30023,30053,30082,30112,30141,30171,30200,30230,30259,30289,30318,30348,30378,30408,30437,30467,30496,30526,30555,30585,30614,30644,30673,30703,30732,30762,30791,30821,30850,30880,30909,30939,30968,30998,31027,31057,31086,31116,31145,31175,31204,31234,31263,31293,31322,31352,31381,31411,31441,31471,31500,31530,31559,31589,31618,31648,31676,31706,31736,31766,31795,31825,31854,31884,31913,31943,31972,32002,32031,32061,32090,32120,32150,32180,32209,32239,32268,32298,32327,32357,32386,32416,32445,32475,32504,32534,32563,32593,32622,32652,32681,32711,32740,32770,32799,32829,32858,32888,32917,32947,32976,33006,33035,33065,33094,33124,33153,33183,33213,33243,33272,33302,33331,33361,33390,33420,33450,33479,33509,33539,33568,33598,33627,33657,33686,33716,33745,33775,33804,33834,33863,33893,33922,33952,33981,34011,34040,34069,34099,34128,34158,34187,34217,34247,34277,34306,34336,34365,34395,34424,34454,34483,34512,34542,34571,34601,34631,34660,34690,34719,34749,34778,34808,34837,34867,34896,34926,34955,34985,35015,35044,35074,35103,35133,35162,35192,35222,35251,35280,35310,35340,35370,35399,35429,35458,35488,35517,35547,35576,35605,35635,35665,35694,35723,35753,35782,35811,35841,35871,35901,35930,35960,35989,36019,36048,36078,36107,36136,36166,36195,36225,36254,36284,36314,36343,36373,36403,36433,36462,36492,36521,36551,36580,36610,36639,36669,36698,36728,36757,36786,36816,36845,36875,36904,36934,36963,36993,37022,37052,37081,37111,37141,37170,37200,37229,37259,37288,37318,37347,37377,37406,37436,37465,37495,37524,37554,37584,37613,37643,37672,37701,37731,37760,37790,37819,37849,37878,37908,37938,37967,37997,38027,38056,38085,38115,38144,38174,38203,38233,38262,38292,38322,38351,38381,38410,38440,38469,38499,38528,38558,38587,38617,38646,38676,38705,38735,38764,38794,38823,38853,38882,38912,38941,38971,39001,39030,39059,39089,39118,39148,39178,39208,39237,39267,39297,39326,39355,39385,39414,39444,39473,39503,39532,39562,39592,39621,39650,39680,39709,39739,39768,39798,39827,39857,39886,39916,39946,39975,40005,40035,40064,40094,40123,40153,40182,40212,40241,40271,40300,40330,40359,40389,40418,40448,40477,40507,40536,40566,40595,40625,40655,40685,40714,40744,40773,40803,40832,40862,40892,40921,40951,40980,41009,41039,41068,41098,41127,41157,41186,41216,41245,41275,41304,41334,41364,41393,41422,41452,41481,41511,41540,41570,41599,41629,41658,41688,41718,41748,41777,41807,41836,41865,41894,41924,41953,41983,42012,42042,42072,42102,42131,42161,42190,42220,42249,42279,42308,42337,42367,42397,42426,42456,42485,42515,42545,42574,42604,42633,42662,42692,42721,42751,42780,42810,42839,42869,42899,42929,42958,42988,43017,43046,43076,43105,43135,43164,43194,43223,43253,43283,43312,43342,43371,43401,43430,43460,43489,43519,43548,43578,43607,43637,43666,43696,43726,43755,43785,43814,43844,43873,43903,43932,43962,43991,44021,44050,44080,44109,44139,44169,44198,44228,44258,44287,44317,44346,44375,44405,44434,44464,44493,44523,44553,44582,44612,44641,44671,44700,44730,44759,44788,44818,44847,44877,44906,44936,44966,44996,45025,45055,45084,45114,45143,45172,45202,45231,45261,45290,45320,45350,45380,45409,45439,45468,45498,45527,45556,45586,45615,45644,45674,45704,45733,45763,45793,45823,45852,45882,45911,45940,45970,45999,46028,46058,46088,46117,46147,46177,46206,46236,46265,46295,46324,46354,46383,46413,46442,46472,46501,46531,46560,46590,46620,46649,46679,46708,46738,46767,46797,46826,46856,46885,46915,46944,46974,47003,47033,47063,47092,47122,47151,47181,47210,47240,47269,47298,47328,47357,47387,47417,47446,47476,47506,47535,47565,47594,47624,47653,47682,47712,47741,47771,47800,47830,47860,47890,47919,47949,47978,48008,48037,48066,48096,48125,48155,48184,48214,48244,48273,48303,48333,48362,48392,48421,48450,48480,48509,48538,48568,48598,48627,48657,48687,48717,48746,48776,48805,48834,48864,48893,48922,48952,48982,49011,49041,49071,49100,49130,49160,49189,49218,49248,49277,49306,49336,49365,49395,49425,49455,49484,49514,49543,49573,49602,49632,49661,49690,49720,49749,49779,49809,49838,49868,49898,49927,49957,49986,50016,50045,50075,50104,50133,50163,50192,50222,50252,50281,50311,50340,50370,50400,50429,50459,50488,50518,50547,50576,50606,50635,50665,50694,50724,50754,50784,50813,50843,50872,50902,50931,50960,50990,51019,51049,51078,51108,51138,51167,51197,51227,51256,51286,51315,51345,51374,51403,51433,51462,51492,51522,51552,51582,51611,51641,51670,51699,51729,51758,51787,51816,51846,51876,51906,51936,51965,51995,52025,52054,52083,52113,52142,52171,52200,52230,52260,52290,52319,52349,52379,52408,52438,52467,52497,52526,52555,52585,52614,52644,52673,52703,52733,52762,52792,52822,52851,52881,52910,52939,52969,52998,53028,53057,53087,53116,53146,53176,53205,53235,53264,53294,53324,53353,53383,53412,53441,53471,53500,53530,53559,53589,53619,53648,53678,53708,53737,53767,53796,53825,53855,53884,53913,53943,53973,54003,54032,54062,54092,54121,54151,54180,54209,54239,54268,54297,54327,54357,54387,54416,54446,54476,54505,54535,54564,54593,54623,54652,54681,54711,54741,54770,54800,54830,54859,54889,54919,54948,54977,55007,55036,55066,55095,55125,55154,55184,55213,55243,55273,55302,55332,55361,55391,55420,55450,55479,55508,55538,55567,55597,55627,55657,55686,55716,55745,55775,55804,55834,55863,55892,55922,55951,55981,56011,56040,56070,56100,56129,56159,56188,56218,56247,56276,56306,56335,56365,56394,56424,56454,56483,56513,56543,56572,56601,56631,56660,56690,56719,56749,56778,56808,56837,56867,56897,56926,56956,56985,57015,57044,57074,57103,57133,57162,57192,57221,57251,57280,57310,57340,57369,57399,57429,57458,57487,57517,57546,57576,57605,57634,57664,57694,57723,57753,57783,57813,57842,57871,57901,57930,57959,57989,58018,58048,58077,58107,58137,58167,58196,58226,58255,58285,58314,58343,58373,58402,58432,58461,58491,58521,58551,58580,58610,58639,58669,58698,58727,58757,58786,58816,58845,58875,58905,58934,58964,58994,59023,59053,59082,59111,59141,59170,59200,59229,59259,59288,59318,59348,59377,59407,59436,59466,59495,59525,59554,59584,59613,59643,59672,59702,59731,59761,59791,59820,59850,59879,59909,59939,59968,59997,60027,60056,60086,60115,60145,60174,60204,60234,60264,60293,60323,60352,60381,60411,60440,60469,60499,60528,60558,60588,60618,60648,60677,60707,60736,60765,60795,60824,60853,60883,60912,60942,60972,61002,61031,61061,61090,61120,61149,61179,61208,61237,61267,61296,61326,61356,61385,61415,61445,61474,61504,61533,61563,61592,61621,61651,61680,61710,61739,61769,61799,61828,61858,61888,61917,61947,61976,62006,62035,62064,62094,62123,62153,62182,62212,62242,62271,62301,62331,62360,62390,62419,62448,62478,62507,62537,62566,62596,62625,62655,62685,62715,62744,62774,62803,62832,62862,62891,62921,62950,62980,63009,63039,63069,63099,63128,63157,63187,63216,63246,63275,63305,63334,63363,63393,63423,63453,63482,63512,63541,63571,63600,63630,63659,63689,63718,63747,63777,63807,63836,63866,63895,63925,63955,63984,64014,64043,64073,64102,64131,64161,64190,64220,64249,64279,64309,64339,64368,64398,64427,64457,64486,64515,64545,64574,64603,64633,64663,64692,64722,64752,64782,64811,64841,64870,64899,64929,64958,64987,65017,65047,65076,65106,65136,65166,65195,65225,65254,65283,65313,65342,65371,65401,65431,65460,65490,65520,65549,65579,65608,65638,65667,65697,65726,65755,65785,65815,65844,65874,65903,65933,65963,65992,66022,66051,66081,66110,66140,66169,66199,66228,66258,66287,66317,66346,66376,66405,66435,66465,66494,66524,66553,66583,66612,66641,66671,66700,66730,66760,66789,66819,66849,66878,66908,66937,66967,66996,67025,67055,67084,67114,67143,67173,67203,67233,67262,67292,67321,67351,67380,67409,67439,67468,67497,67527,67557,67587,67617,67646,67676,67705,67735,67764,67793,67823,67852,67882,67911,67941,67971,68e3,68030,68060,68089,68119,68148,68177,68207,68236,68266,68295,68325,68354,68384,68414,68443,68473,68502,68532,68561,68591,68620,68650,68679,68708,68738,68768,68797,68827,68857,68886,68916,68946,68975,69004,69034,69063,69092,69122,69152,69181,69211,69240,69270,69300,69330,69359,69388,69418,69447,69476,69506,69535,69565,69595,69624,69654,69684,69713,69743,69772,69802,69831,69861,69890,69919,69949,69978,70008,70038,70067,70097,70126,70156,70186,70215,70245,70274,70303,70333,70362,70392,70421,70451,70481,70510,70540,70570,70599,70629,70658,70687,70717,70746,70776,70805,70835,70864,70894,70924,70954,70983,71013,71042,71071,71101,71130,71159,71189,71218,71248,71278,71308,71337,71367,71397,71426,71455,71485,71514,71543,71573,71602,71632,71662,71691,71721,71751,71781,71810,71839,71869,71898,71927,71957,71986,72016,72046,72075,72105,72135,72164,72194,72223,72253,72282,72311,72341,72370,72400,72429,72459,72489,72518,72548,72577,72607,72637,72666,72695,72725,72754,72784,72813,72843,72872,72902,72931,72961,72991,73020,73050,73080,73109,73139,73168,73197,73227,73256,73286,73315,73345,73375,73404,73434,73464,73493,73523,73552,73581,73611,73640,73669,73699,73729,73758,73788,73818,73848,73877,73907,73936,73965,73995,74024,74053,74083,74113,74142,74172,74202,74231,74261,74291,74320,74349,74379,74408,74437,74467,74497,74526,74556,74586,74615,74645,74675,74704,74733,74763,74792,74822,74851,74881,74910,74940,74969,74999,75029,75058,75088,75117,75147,75176,75206,75235,75264,75294,75323,75353,75383,75412,75442,75472,75501,75531,75560,75590,75619,75648,75678,75707,75737,75766,75796,75826,75856,75885,75915,75944,75974,76003,76032,76062,76091,76121,76150,76180,76210,76239,76269,76299,76328,76358,76387,76416,76446,76475,76505,76534,76564,76593,76623,76653,76682,76712,76741,76771,76801,76830,76859,76889,76918,76948,76977,77007,77036,77066,77096,77125,77155,77185,77214,77243,77273,77302,77332,77361,77390,77420,77450,77479,77509,77539,77569,77598,77627,77657,77686,77715,77745,77774,77804,77833,77863,77893,77923,77952,77982,78011,78041,78070,78099,78129,78158,78188,78217,78247,78277,78307,78336,78366,78395,78425,78454,78483,78513,78542,78572,78601,78631,78661,78690,78720,78750,78779,78808,78838,78867,78897,78926,78956,78985,79015,79044,79074,79104,79133,79163,79192,79222,79251,79281,79310,79340,79369,79399,79428,79458,79487,79517,79546,79576,79606,79635,79665,79695,79724,79753,79783,79812,79841,79871,79900,79930,79960,79990]};var formattingTokens=/(\[[^\[]*\])|(\\)?i(Mo|MM?M?M?|Do|DDDo|DD?D?D?|w[o|w]?|YYYYY|YYYY|YY|gg(ggg?)?)|(\\)?(Mo|MM?M?M?|Do|DDDo|DD?D?D?|ddd?d?|do?|w[o|w]?|W[o|W]?|YYYYY|YYYY|YY|gg(ggg?)?|GG(GGG?)?|e|E|a|A|hh?|HH?|mm?|ss?|SS?S?|X|zz?|ZZ?|.)/g,localFormattingTokens=/(\[[^\[]*\])|(\\)?(LTS|LT|LL?L?L?|l{1,4})/g,parseTokenOneOrTwoDigits=/\d\d?/,parseTokenOneToThreeDigits=/\d{1,3}/,parseTokenThreeDigits=/\d{3}/,parseTokenFourDigits=/\d{1,4}/,parseTokenSixDigits=/[+\-]?\d{1,6}/,parseTokenWord=/[0-9]*['a-z\u00A0-\u05FF\u0700-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF]+(\.?)|[\u0600-\u06FF\/]+(\s*?[\u0600-\u06FF]+){1,2}/i,parseTokenTimezone=/Z|[\+\-]\d\d:?\d\d/i,parseTokenT=/T/i,parseTokenTimestampMs=/[\+\-]?\d+(\.\d{1,3})?/,unitAliases={hd:"idate",hm:"imonth",hy:"iyear"},formatFunctions={},ordinalizeTokens="DDD w M D".split(" "),paddedTokens="M D w".split(" "),formatTokenFunctions={iM:function(){return this.iMonth()+1},iMMM:function(format){return this.localeData().iMonthsShort(this,format)},iMMMM:function(format){return this.localeData().iMonths(this,format)},iD:function(){return this.iDate()},iDDD:function(){return this.iDayOfYear()},iw:function(){return this.iWeek()},iYY:function(){return leftZeroFill(this.iYear()%100,2)},iYYYY:function(){return leftZeroFill(this.iYear(),4)},iYYYYY:function(){return leftZeroFill(this.iYear(),5)},igg:function(){return leftZeroFill(this.iWeekYear()%100,2)},igggg:function(){return this.iWeekYear()},iggggg:function(){return leftZeroFill(this.iWeekYear(),5)}},i;function padToken(func,count){return function(a){return leftZeroFill(func.call(this,a),count)}}function ordinalizeToken(func,period){return function(a){return this.localeData().ordinal(func.call(this,a),period)}}while(ordinalizeTokens.length){i=ordinalizeTokens.pop();formatTokenFunctions["i"+i+"o"]=ordinalizeToken(formatTokenFunctions["i"+i],i)}while(paddedTokens.length){i=paddedTokens.pop();formatTokenFunctions["i"+i+i]=padToken(formatTokenFunctions["i"+i],2)}formatTokenFunctions.iDDDD=padToken(formatTokenFunctions.iDDD,3);function extend(a,b){var key;for(key in b)if(b.hasOwnProperty(key))a[key]=b[key];return a}function leftZeroFill(number,targetLength){var output=number+"";while(output.length<targetLength)output="0"+output;return output}function isArray(input){return Object.prototype.toString.call(input)==="[object Array]"}function normalizeUnits(units){return units?unitAliases[units]||units.toLowerCase().replace(/(.)s$/,"$1"):units}function setDate(moment,year,month,date){var utc=moment._isUTC?"UTC":"";moment._d["set"+utc+"FullYear"](year);moment._d["set"+utc+"Month"](month);moment._d["set"+utc+"Date"](date)}function objectCreate(parent){function F(){}F.prototype=parent;return new F}function getPrototypeOf(object){if(Object.getPrototypeOf)return Object.getPrototypeOf(object);else if("".__proto__)return object.__proto__;else return object.constructor.prototype}extend(getPrototypeOf(moment.localeData()),{_iMonths:["Muharram","Safar","Rabi' al-Awwal","Rabi' al-Thani","Jumada al-Ula","Jumada al-Alkhirah","Rajab","Sha’ban","Ramadhan","Shawwal","Thul-Qi’dah","Thul-Hijjah"],iMonths:function(m){return this._iMonths[m.iMonth()]},_iMonthsShort:["Muh","Saf","Rab-I","Rab-II","Jum-I","Jum-II","Raj","Sha","Ram","Shw","Dhu-Q","Dhu-H"],iMonthsShort:function(m){return this._iMonthsShort[m.iMonth()]},iMonthsParse:function(monthName){var i,mom,regex;if(!this._iMonthsParse)this._iMonthsParse=[];for(i=0;i<12;i+=1){if(!this._iMonthsParse[i]){mom=hMoment([2e3,(2+i)%12,25]);regex="^"+this.iMonths(mom,"")+"$|^"+this.iMonthsShort(mom,"")+"$";this._iMonthsParse[i]=new RegExp(regex.replace(".",""),"i")}if(this._iMonthsParse[i].test(monthName))return i}}});var iMonthNames={iMonths:"محرم_صفر_ربيع الأول_ربيع الثاني_جمادى الأولى_جمادى الآخرة_رجب_شعبان_رمضان_شوال_ذو القعدة_ذو الحجة".split("_"),iMonthsShort:"محرم_صفر_ربيع ١_ربيع ٢_جمادى ١_جمادى ٢_رجب_شعبان_رمضان_شوال_ذو القعدة_ذو الحجة".split("_")};if(typeof moment.updateLocale==="function"){moment.updateLocale("ar-sa",iMonthNames)}else{var oldLocale=moment.locale();moment.defineLocale("ar-sa",iMonthNames);moment.locale(oldLocale)}function makeFormatFunction(format){var array=format.match(formattingTokens),length=array.length,i;for(i=0;i<length;i+=1)if(formatTokenFunctions[array[i]])array[i]=formatTokenFunctions[array[i]];return function(mom){var output="";for(i=0;i<length;i+=1)output+=array[i]instanceof Function?"["+array[i].call(mom,format)+"]":array[i];return output}}function getParseRegexForToken(token,config){switch(token){case"iDDDD":return parseTokenThreeDigits;case"iYYYY":return parseTokenFourDigits;case"iYYYYY":return parseTokenSixDigits;case"iDDD":return parseTokenOneToThreeDigits;case"iMMM":case"iMMMM":return parseTokenWord;case"iMM":case"iDD":case"iYY":case"iM":case"iD":return parseTokenOneOrTwoDigits;case"DDDD":return parseTokenThreeDigits;case"YYYY":return parseTokenFourDigits;case"YYYYY":return parseTokenSixDigits;case"S":case"SS":case"SSS":case"DDD":return parseTokenOneToThreeDigits;case"MMM":case"MMMM":case"dd":case"ddd":case"dddd":return parseTokenWord;case"a":case"A":return moment.localeData(config._l)._meridiemParse;case"X":return parseTokenTimestampMs;case"Z":case"ZZ":return parseTokenTimezone;case"T":return parseTokenT;case"MM":case"DD":case"YY":case"HH":case"hh":case"mm":case"ss":case"M":case"D":case"d":case"H":case"h":case"m":case"s":return parseTokenOneOrTwoDigits;default:return new RegExp(token.replace("\\",""))}}function addTimeToArrayFromToken(token,input,config){var a,datePartArray=config._a;switch(token){case"iM":case"iMM":datePartArray[1]=input==null?0:~~input-1;break;case"iMMM":case"iMMMM":a=moment.localeData(config._l).iMonthsParse(input);if(a!=null)datePartArray[1]=a;else config._isValid=false;break;case"iD":case"iDD":case"iDDD":case"iDDDD":if(input!=null)datePartArray[2]=~~input;break;case"iYY":datePartArray[0]=~~input+(~~input>47?1300:1400);break;case"iYYYY":case"iYYYYY":datePartArray[0]=~~input}if(input==null)config._isValid=false}function dateFromArray(config){var g,h,hy=config._a[0],hm=config._a[1],hd=config._a[2];if(hy==null&&hm==null&&hd==null)return[0,0,1];hy=hy||0;hm=hm||0;hd=hd||1;if(hd<1||hd>hMoment.iDaysInMonth(hy,hm))config._isValid=false;g=toGregorian(hy,hm,hd);h=toHijri(g.gy,g.gm,g.gd);config._hDiff=0;if(~~h.hy!==hy)config._hDiff+=1;if(~~h.hm!==hm)config._hDiff+=1;if(~~h.hd!==hd)config._hDiff+=1;return[g.gy,g.gm,g.gd]}function makeDateFromStringAndFormat(config){var tokens=config._f.match(formattingTokens),string=config._i,len=tokens.length,i,token,parsedInput;config._a=[];for(i=0;i<len;i+=1){token=tokens[i];parsedInput=(getParseRegexForToken(token,config).exec(string)||[])[0];if(parsedInput)string=string.slice(string.indexOf(parsedInput)+parsedInput.length);if(formatTokenFunctions[token])addTimeToArrayFromToken(token,parsedInput,config)}if(string)config._il=string;return dateFromArray(config)}function makeDateFromStringAndArray(config,utc){var len=config._f.length,i,format,tempMoment,bestMoment,currentScore,scoreToBeat;if(len===0){return makeMoment(new Date(NaN))}for(i=0;i<len;i+=1){format=config._f[i];currentScore=0;tempMoment=makeMoment(config._i,format,config._l,utc);if(!tempMoment.isValid())continue;currentScore+=tempMoment._hDiff;if(tempMoment._il)currentScore+=tempMoment._il.length;if(scoreToBeat==null||currentScore<scoreToBeat){scoreToBeat=currentScore;bestMoment=tempMoment}}return bestMoment}function removeParsedTokens(config){var string=config._i,input="",format="",array=config._f.match(formattingTokens),len=array.length,i,match,parsed;for(i=0;i<len;i+=1){match=array[i];parsed=(getParseRegexForToken(match,config).exec(string)||[])[0];if(parsed)string=string.slice(string.indexOf(parsed)+parsed.length);if(!(formatTokenFunctions[match]instanceof Function)){format+=match;if(parsed)input+=parsed}}config._i=input;config._f=format}function iWeekOfYear(mom,firstDayOfWeek,firstDayOfWeekOfYear){var end=firstDayOfWeekOfYear-firstDayOfWeek,daysToDayOfWeek=firstDayOfWeekOfYear-mom.day(),adjustedMoment;if(daysToDayOfWeek>end){daysToDayOfWeek-=7}if(daysToDayOfWeek<end-7){daysToDayOfWeek+=7}adjustedMoment=hMoment(mom).add(daysToDayOfWeek,"d");return{week:Math.ceil(adjustedMoment.iDayOfYear()/7),year:adjustedMoment.iYear()}}function makeMoment(input,format,lang,utc){var config={_i:input,_f:format,_l:lang},date,m,hm;if(format){if(isArray(format)){return makeDateFromStringAndArray(config,utc)}else{date=makeDateFromStringAndFormat(config);removeParsedTokens(config);format="YYYY-MM-DD-"+config._f;input=leftZeroFill(date[0],4)+"-"+leftZeroFill(date[1]+1,2)+"-"+leftZeroFill(date[2],2)+"-"+config._i}}if(utc)m=moment.utc(input,format,lang);else m=moment(input,format,lang);if(config._isValid===false)m._isValid=false;m._hDiff=config._hDiff||0;hm=objectCreate(hMoment.fn);extend(hm,m);return hm}function hMoment(input,format,lang){return makeMoment(input,format,lang,false)}extend(hMoment,moment);hMoment.fn=objectCreate(moment.fn);hMoment.utc=function(input,format,lang){return makeMoment(input,format,lang,true)};hMoment.fn.format=function(format){var i,replace,me=this;if(format){i=5;replace=function(input){return me.localeData().longDateFormat(input)||input};while(i>0&&localFormattingTokens.test(format)){i-=1;format=format.replace(localFormattingTokens,replace)}if(!formatFunctions[format]){formatFunctions[format]=makeFormatFunction(format)}format=formatFunctions[format](this)}return moment.fn.format.call(this,format)};hMoment.fn.iYear=function(input){var lastDay,h,g;if(typeof input==="number"){h=toHijri(this.year(),this.month(),this.date());lastDay=Math.min(h.hd,hMoment.iDaysInMonth(input,h.hm));g=toGregorian(input,h.hm,lastDay);setDate(this,g.gy,g.gm,g.gd);if(this.month()!==g.gm||this.date()!==g.gd||this.year()!==g.gy){setDate(this,g.gy,g.gm,g.gd)}moment.updateOffset(this);return this}else{return toHijri(this.year(),this.month(),this.date()).hy}};hMoment.fn.iMonth=function(input){var lastDay,h,g;if(input!=null){if(typeof input==="string"){input=this.localeData().iMonthsParse(input);if(input>=0){input-=1}else{return this}}h=toHijri(this.year(),this.month(),this.date());lastDay=Math.min(h.hd,hMoment.iDaysInMonth(h.hy,input));this.iYear(h.hy+div(input,12));input=mod(input,12);if(input<0){input+=12;this.iYear(this.iYear()-1)}g=toGregorian(this.iYear(),input,lastDay);setDate(this,g.gy,g.gm,g.gd);if(this.month()!==g.gm||this.date()!==g.gd||this.year()!==g.gy){setDate(this,g.gy,g.gm,g.gd)}moment.updateOffset(this);return this}else{return toHijri(this.year(),this.month(),this.date()).hm}};hMoment.fn.iDate=function(input){var h,g;if(typeof input==="number"){h=toHijri(this.year(),this.month(),this.date());g=toGregorian(h.hy,h.hm,input);setDate(this,g.gy,g.gm,g.gd);if(this.month()!==g.gm||this.date()!==g.gd||this.year()!==g.gy){setDate(this,g.gy,g.gm,g.gd)}moment.updateOffset(this);return this}else{return toHijri(this.year(),this.month(),this.date()).hd}};hMoment.fn.iDayOfYear=function(input){var dayOfYear=Math.round((hMoment(this).startOf("day")-hMoment(this).startOf("iYear"))/864e5)+1;return input==null?dayOfYear:this.add(input-dayOfYear,"d")};hMoment.fn.iDaysInMonth=function(){return parseInt(hMoment(this).endOf("iMonth").format("iDD"))};hMoment.fn.iWeek=function(input){var week=iWeekOfYear(this,this.localeData()._week.dow,this.localeData()._week.doy).week;return input==null?week:this.add((input-week)*7,"d")};hMoment.fn.iWeekYear=function(input){var year=iWeekOfYear(this,this.localeData()._week.dow,this.localeData()._week.doy).year;return input==null?year:this.add(input-year,"y")};hMoment.fn.add=function(val,units){var temp;if(units!==null&&!isNaN(+units)){temp=val;val=units;units=temp}units=normalizeUnits(units);if(units==="iyear"){this.iYear(this.iYear()+val)}else if(units==="imonth"){this.iMonth(this.iMonth()+val)}else if(units==="idate"){this.iDate(this.iDate()+val)}else{moment.fn.add.call(this,val,units)}return this};hMoment.fn.subtract=function(val,units){var temp;if(units!==null&&!isNaN(+units)){temp=val;val=units;units=temp}units=normalizeUnits(units);if(units==="iyear"){this.iYear(this.iYear()-val)}else if(units==="imonth"){this.iMonth(this.iMonth()-val)}else if(units==="idate"){this.iDate(this.iDate()-val)}else{moment.fn.subtract.call(this,val,units)}return this};hMoment.fn.startOf=function(units){units=normalizeUnits(units);if(units==="iyear"||units==="imonth"){if(units==="iyear"){this.iMonth(0)}this.iDate(1);this.hours(0);this.minutes(0);this.seconds(0);this.milliseconds(0);return this}else{return moment.fn.startOf.call(this,units)}};hMoment.fn.endOf=function(units){units=normalizeUnits(units);if(units===undefined||units==="milisecond"){return this}return this.startOf(units).add(1,units==="isoweek"?"week":units).subtract(1,"milliseconds")};hMoment.fn.clone=function(){return hMoment(this)};hMoment.fn.iYears=hMoment.fn.iYear;hMoment.fn.iMonths=hMoment.fn.iMonth;hMoment.fn.iDates=hMoment.fn.iDate;hMoment.fn.iWeeks=hMoment.fn.iWeek;hMoment.iDaysInMonth=function(year,month){var i=getNewMoonMJDNIndex(year,month+1),daysInMonth=ummalqura.ummalquraData[i]-ummalqura.ummalquraData[i-1];return daysInMonth};function toHijri(gy,gm,gd){var h=d2h(g2d(gy,gm+1,gd));h.hm-=1;return h}function toGregorian(hy,hm,hd){var g=d2g(h2d(hy,hm+1,hd));g.gm-=1;return g}hMoment.iConvert={toHijri:toHijri,toGregorian:toGregorian};return hMoment;function div(a,b){return~~(a/b)}function mod(a,b){return a-~~(a/b)*b}function h2d(hy,hm,hd){var i=getNewMoonMJDNIndex(hy,hm),mjdn=hd+ummalqura.ummalquraData[i-1]-1,jdn=mjdn+24e5;return jdn}function d2h(jdn){var mjdn=jdn-24e5,i=getNewMoonMJDNIndexByJDN(mjdn),totalMonths=i+16260,cYears=Math.floor((totalMonths-1)/12),hy=cYears+1,hm=totalMonths-12*cYears,hd=mjdn-ummalqura.ummalquraData[i-1]+1;return{hy:hy,hm:hm,hd:hd}}function g2d(gy,gm,gd){var d=div((gy+div(gm-8,6)+100100)*1461,4)+div(153*mod(gm+9,12)+2,5)+gd-34840408;d=d-div(div(gy+100100+div(gm-8,6),100)*3,4)+752;return d}function d2g(jdn){var j,i,gd,gm,gy;j=4*jdn+139361631;j=j+div(div(4*jdn+183187720,146097)*3,4)*4-3908;i=div(mod(j,1461),4)*5+308;gd=div(mod(i,153),5)+1;gm=mod(div(i,153),12)+1;gy=div(j,1461)-100100+div(8-gm,6);return{gy:gy,gm:gm,gd:gd}}function getNewMoonMJDNIndex(hy,hm){var cYears=hy-1,totalMonths=cYears*12+1+(hm-1),i=totalMonths-16260;return i}function getNewMoonMJDNIndexByJDN(mjdn){for(var i=0;i<ummalqura.ummalquraData.length;i=i+1){if(ummalqura.ummalquraData[i]>mjdn)return i}}})},{moment:39}],38:[function(require,module,exports){(function(global,factory){typeof exports==="object"&&typeof module!=="undefined"&&typeof require==="function"?factory(require("../moment")):typeof define==="function"&&define.amd?define(["../moment"],factory):factory(global.moment)})(this,function(moment){"use strict";var id=moment.defineLocale("id",{months:"Januari_Februari_Maret_April_Mei_Juni_Juli_Agustus_September_Oktober_November_Desember".split("_"),monthsShort:"Jan_Feb_Mar_Apr_Mei_Jun_Jul_Agt_Sep_Okt_Nov_Des".split("_"),weekdays:"Minggu_Senin_Selasa_Rabu_Kamis_Jumat_Sabtu".split("_"),weekdaysShort:"Min_Sen_Sel_Rab_Kam_Jum_Sab".split("_"),weekdaysMin:"Mg_Sn_Sl_Rb_Km_Jm_Sb".split("_"),longDateFormat:{LT:"HH.mm",LTS:"HH.mm.ss",L:"DD/MM/YYYY",LL:"D MMMM YYYY",LLL:"D MMMM YYYY [pukul] HH.mm",LLLL:"dddd, D MMMM YYYY [pukul] HH.mm"},meridiemParse:/pagi|siang|sore|malam/,meridiemHour:function(hour,meridiem){if(hour===12){hour=0}if(meridiem==="pagi"){return hour}else if(meridiem==="siang"){return hour>=11?hour:hour+12}else if(meridiem==="sore"||meridiem==="malam"){return hour+12}},meridiem:function(hours,minutes,isLower){if(hours<11){return"pagi"}else if(hours<15){return"siang"}else if(hours<19){return"sore"}else{return"malam"}},calendar:{sameDay:"[Hari ini pukul] LT",nextDay:"[Besok pukul] LT",nextWeek:"dddd [pukul] LT",lastDay:"[Kemarin pukul] LT",lastWeek:"dddd [lalu pukul] LT",sameElse:"L"},relativeTime:{future:"dalam %s",past:"%s yang lalu",s:"beberapa detik",ss:"%d detik",m:"semenit",mm:"%d menit",h:"sejam",hh:"%d jam",d:"sehari",dd:"%d hari",M:"sebulan",MM:"%d bulan",y:"setahun",yy:"%d tahun"},week:{dow:0,doy:6}});return id})},{"../moment":39}],39:[function(require,module,exports){(function(global,factory){typeof exports==="object"&&typeof module!=="undefined"?module.exports=factory():typeof define==="function"&&define.amd?define(factory):global.moment=factory()})(this,function(){"use strict";var hookCallback;function hooks(){return hookCallback.apply(null,arguments)}function setHookCallback(callback){hookCallback=callback}function isArray(input){return input instanceof Array||Object.prototype.toString.call(input)==="[object Array]"}function isObject(input){return input!=null&&Object.prototype.toString.call(input)==="[object Object]"}function hasOwnProp(a,b){return Object.prototype.hasOwnProperty.call(a,b)}function isObjectEmpty(obj){if(Object.getOwnPropertyNames){return Object.getOwnPropertyNames(obj).length===0}else{var k;for(k in obj){if(hasOwnProp(obj,k)){return false}}return true}}function isUndefined(input){return input===void 0}function isNumber(input){return typeof input==="number"||Object.prototype.toString.call(input)==="[object Number]"}function isDate(input){return input instanceof Date||Object.prototype.toString.call(input)==="[object Date]"}function map(arr,fn){var res=[],i;for(i=0;i<arr.length;++i){res.push(fn(arr[i],i))}return res}function extend(a,b){for(var i in b){if(hasOwnProp(b,i)){a[i]=b[i]}}if(hasOwnProp(b,"toString")){a.toString=b.toString}if(hasOwnProp(b,"valueOf")){a.valueOf=b.valueOf}return a}function createUTC(input,format,locale,strict){return createLocalOrUTC(input,format,locale,strict,true).utc()}function defaultParsingFlags(){return{empty:false,unusedTokens:[],unusedInput:[],overflow:-2,charsLeftOver:0,nullInput:false,invalidEra:null,invalidMonth:null,invalidFormat:false,userInvalidated:false,iso:false,parsedDateParts:[],era:null,meridiem:null,rfc2822:false,weekdayMismatch:false}}function getParsingFlags(m){if(m._pf==null){m._pf=defaultParsingFlags()}return m._pf}var some;if(Array.prototype.some){some=Array.prototype.some}else{some=function(fun){var t=Object(this),len=t.length>>>0,i;for(i=0;i<len;i++){if(i in t&&fun.call(this,t[i],i,t)){return true}}return false}}function isValid(m){if(m._isValid==null){var flags=getParsingFlags(m),parsedParts=some.call(flags.parsedDateParts,function(i){return i!=null}),isNowValid=!isNaN(m._d.getTime())&&flags.overflow<0&&!flags.empty&&!flags.invalidEra&&!flags.invalidMonth&&!flags.invalidWeekday&&!flags.weekdayMismatch&&!flags.nullInput&&!flags.invalidFormat&&!flags.userInvalidated&&(!flags.meridiem||flags.meridiem&&parsedParts);if(m._strict){isNowValid=isNowValid&&flags.charsLeftOver===0&&flags.unusedTokens.length===0&&flags.bigHour===undefined}if(Object.isFrozen==null||!Object.isFrozen(m)){m._isValid=isNowValid}else{return isNowValid}}return m._isValid}function createInvalid(flags){var m=createUTC(NaN);if(flags!=null){extend(getParsingFlags(m),flags)}else{getParsingFlags(m).userInvalidated=true}return m}var momentProperties=hooks.momentProperties=[],updateInProgress=false;function copyConfig(to,from){var i,prop,val;if(!isUndefined(from._isAMomentObject)){to._isAMomentObject=from._isAMomentObject}if(!isUndefined(from._i)){to._i=from._i}if(!isUndefined(from._f)){to._f=from._f}if(!isUndefined(from._l)){to._l=from._l}if(!isUndefined(from._strict)){to._strict=from._strict}if(!isUndefined(from._tzm)){to._tzm=from._tzm}if(!isUndefined(from._isUTC)){to._isUTC=from._isUTC}if(!isUndefined(from._offset)){to._offset=from._offset}if(!isUndefined(from._pf)){to._pf=getParsingFlags(from)}if(!isUndefined(from._locale)){to._locale=from._locale}if(momentProperties.length>0){for(i=0;i<momentProperties.length;i++){prop=momentProperties[i];val=from[prop];if(!isUndefined(val)){to[prop]=val}}}return to}function Moment(config){copyConfig(this,config);this._d=new Date(config._d!=null?config._d.getTime():NaN);if(!this.isValid()){this._d=new Date(NaN)}if(updateInProgress===false){updateInProgress=true;hooks.updateOffset(this);updateInProgress=false}}function isMoment(obj){return obj instanceof Moment||obj!=null&&obj._isAMomentObject!=null}function warn(msg){if(hooks.suppressDeprecationWarnings===false&&typeof console!=="undefined"&&console.warn){console.warn("Deprecation warning: "+msg)}}function deprecate(msg,fn){var firstTime=true;return extend(function(){if(hooks.deprecationHandler!=null){hooks.deprecationHandler(null,msg)}if(firstTime){var args=[],arg,i,key;for(i=0;i<arguments.length;i++){arg="";if(typeof arguments[i]==="object"){arg+="\n["+i+"] ";for(key in arguments[0]){if(hasOwnProp(arguments[0],key)){arg+=key+": "+arguments[0][key]+", "}}arg=arg.slice(0,-2)}else{arg=arguments[i]}args.push(arg)}warn(msg+"\nArguments: "+Array.prototype.slice.call(args).join("")+"\n"+(new Error).stack);firstTime=false}return fn.apply(this,arguments)},fn)}var deprecations={};function deprecateSimple(name,msg){if(hooks.deprecationHandler!=null){hooks.deprecationHandler(name,msg)}if(!deprecations[name]){warn(msg);deprecations[name]=true}}hooks.suppressDeprecationWarnings=false;hooks.deprecationHandler=null;function isFunction(input){return typeof Function!=="undefined"&&input instanceof Function||Object.prototype.toString.call(input)==="[object Function]"}function set(config){var prop,i;for(i in config){if(hasOwnProp(config,i)){prop=config[i];if(isFunction(prop)){this[i]=prop}else{this["_"+i]=prop}}}this._config=config;this._dayOfMonthOrdinalParseLenient=new RegExp((this._dayOfMonthOrdinalParse.source||this._ordinalParse.source)+"|"+/\d{1,2}/.source)}function mergeConfigs(parentConfig,childConfig){var res=extend({},parentConfig),prop;for(prop in childConfig){if(hasOwnProp(childConfig,prop)){if(isObject(parentConfig[prop])&&isObject(childConfig[prop])){res[prop]={};extend(res[prop],parentConfig[prop]);extend(res[prop],childConfig[prop])}else if(childConfig[prop]!=null){res[prop]=childConfig[prop]}else{delete res[prop]}}}for(prop in parentConfig){if(hasOwnProp(parentConfig,prop)&&!hasOwnProp(childConfig,prop)&&isObject(parentConfig[prop])){res[prop]=extend({},res[prop])}}return res}function Locale(config){if(config!=null){this.set(config)}}var keys;if(Object.keys){keys=Object.keys}else{keys=function(obj){var i,res=[];for(i in obj){if(hasOwnProp(obj,i)){res.push(i)}}return res}}var defaultCalendar={sameDay:"[Today at] LT",nextDay:"[Tomorrow at] LT",nextWeek:"dddd [at] LT",lastDay:"[Yesterday at] LT",lastWeek:"[Last] dddd [at] LT",sameElse:"L"};function calendar(key,mom,now){var output=this._calendar[key]||this._calendar["sameElse"];return isFunction(output)?output.call(mom,now):output}function zeroFill(number,targetLength,forceSign){var absNumber=""+Math.abs(number),zerosToFill=targetLength-absNumber.length,sign=number>=0;return(sign?forceSign?"+":"":"-")+Math.pow(10,Math.max(0,zerosToFill)).toString().substr(1)+absNumber}var formattingTokens=/(\[[^\[]*\])|(\\)?([Hh]mm(ss)?|Mo|MM?M?M?|Do|DDDo|DD?D?D?|ddd?d?|do?|w[o|w]?|W[o|W]?|Qo?|N{1,5}|YYYYYY|YYYYY|YYYY|YY|y{2,4}|yo?|gg(ggg?)?|GG(GGG?)?|e|E|a|A|hh?|HH?|kk?|mm?|ss?|S{1,9}|x|X|zz?|ZZ?|.)/g,localFormattingTokens=/(\[[^\[]*\])|(\\)?(LTS|LT|LL?L?L?|l{1,4})/g,formatFunctions={},formatTokenFunctions={};function addFormatToken(token,padded,ordinal,callback){var func=callback;if(typeof callback==="string"){func=function(){return this[callback]()}}if(token){formatTokenFunctions[token]=func}if(padded){formatTokenFunctions[padded[0]]=function(){return zeroFill(func.apply(this,arguments),padded[1],padded[2])}}if(ordinal){formatTokenFunctions[ordinal]=function(){return this.localeData().ordinal(func.apply(this,arguments),token)}}}function removeFormattingTokens(input){if(input.match(/\[[\s\S]/)){return input.replace(/^\[|\]$/g,"")}return input.replace(/\\/g,"")}function makeFormatFunction(format){var array=format.match(formattingTokens),i,length;for(i=0,length=array.length;i<length;i++){if(formatTokenFunctions[array[i]]){array[i]=formatTokenFunctions[array[i]]}else{array[i]=removeFormattingTokens(array[i])}}return function(mom){var output="",i;for(i=0;i<length;i++){output+=isFunction(array[i])?array[i].call(mom,format):array[i]}return output}}function formatMoment(m,format){if(!m.isValid()){return m.localeData().invalidDate()}format=expandFormat(format,m.localeData());formatFunctions[format]=formatFunctions[format]||makeFormatFunction(format);return formatFunctions[format](m)}function expandFormat(format,locale){var i=5;function replaceLongDateFormatTokens(input){return locale.longDateFormat(input)||input}localFormattingTokens.lastIndex=0;while(i>=0&&localFormattingTokens.test(format)){format=format.replace(localFormattingTokens,replaceLongDateFormatTokens);localFormattingTokens.lastIndex=0;i-=1}return format}var defaultLongDateFormat={LTS:"h:mm:ss A",LT:"h:mm A",L:"MM/DD/YYYY",LL:"MMMM D, YYYY",LLL:"MMMM D, YYYY h:mm A",LLLL:"dddd, MMMM D, YYYY h:mm A"};function longDateFormat(key){var format=this._longDateFormat[key],formatUpper=this._longDateFormat[key.toUpperCase()];if(format||!formatUpper){return format}this._longDateFormat[key]=formatUpper.match(formattingTokens).map(function(tok){if(tok==="MMMM"||tok==="MM"||tok==="DD"||tok==="dddd"){return tok.slice(1)}return tok}).join("");return this._longDateFormat[key]}var defaultInvalidDate="Invalid date";function invalidDate(){return this._invalidDate}var defaultOrdinal="%d",defaultDayOfMonthOrdinalParse=/\d{1,2}/;function ordinal(number){return this._ordinal.replace("%d",number)}var defaultRelativeTime={future:"in %s",past:"%s ago",s:"a few seconds",ss:"%d seconds",m:"a minute",mm:"%d minutes",h:"an hour",hh:"%d hours",d:"a day",dd:"%d days",w:"a week",ww:"%d weeks",M:"a month",MM:"%d months",y:"a year",yy:"%d years"};function relativeTime(number,withoutSuffix,string,isFuture){var output=this._relativeTime[string];return isFunction(output)?output(number,withoutSuffix,string,isFuture):output.replace(/%d/i,number)}function pastFuture(diff,output){var format=this._relativeTime[diff>0?"future":"past"];return isFunction(format)?format(output):format.replace(/%s/i,output)}var aliases={};function addUnitAlias(unit,shorthand){var lowerCase=unit.toLowerCase();aliases[lowerCase]=aliases[lowerCase+"s"]=aliases[shorthand]=unit}function normalizeUnits(units){return typeof units==="string"?aliases[units]||aliases[units.toLowerCase()]:undefined}function normalizeObjectUnits(inputObject){var normalizedInput={},normalizedProp,prop;for(prop in inputObject){if(hasOwnProp(inputObject,prop)){normalizedProp=normalizeUnits(prop);if(normalizedProp){normalizedInput[normalizedProp]=inputObject[prop]}}}return normalizedInput}var priorities={};function addUnitPriority(unit,priority){priorities[unit]=priority}function getPrioritizedUnits(unitsObj){var units=[],u;for(u in unitsObj){if(hasOwnProp(unitsObj,u)){units.push({unit:u,priority:priorities[u]})}}units.sort(function(a,b){return a.priority-b.priority});return units}function isLeapYear(year){return year%4===0&&year%100!==0||year%400===0}function absFloor(number){if(number<0){return Math.ceil(number)||0}else{return Math.floor(number)}}function toInt(argumentForCoercion){var coercedNumber=+argumentForCoercion,value=0;if(coercedNumber!==0&&isFinite(coercedNumber)){value=absFloor(coercedNumber)}return value}function makeGetSet(unit,keepTime){return function(value){if(value!=null){set$1(this,unit,value);hooks.updateOffset(this,keepTime);return this}else{return get(this,unit)}}}function get(mom,unit){return mom.isValid()?mom._d["get"+(mom._isUTC?"UTC":"")+unit]():NaN}function set$1(mom,unit,value){if(mom.isValid()&&!isNaN(value)){if(unit==="FullYear"&&isLeapYear(mom.year())&&mom.month()===1&&mom.date()===29){value=toInt(value);mom._d["set"+(mom._isUTC?"UTC":"")+unit](value,mom.month(),daysInMonth(value,mom.month()))}else{mom._d["set"+(mom._isUTC?"UTC":"")+unit](value)}}}function stringGet(units){units=normalizeUnits(units);if(isFunction(this[units])){return this[units]()}return this}function stringSet(units,value){if(typeof units==="object"){units=normalizeObjectUnits(units);var prioritized=getPrioritizedUnits(units),i;for(i=0;i<prioritized.length;i++){this[prioritized[i].unit](units[prioritized[i].unit])}}else{units=normalizeUnits(units);if(isFunction(this[units])){return this[units](value)}}return this}var match1=/\d/,match2=/\d\d/,match3=/\d{3}/,match4=/\d{4}/,match6=/[+-]?\d{6}/,match1to2=/\d\d?/,match3to4=/\d\d\d\d?/,match5to6=/\d\d\d\d\d\d?/,match1to3=/\d{1,3}/,match1to4=/\d{1,4}/,match1to6=/[+-]?\d{1,6}/,matchUnsigned=/\d+/,matchSigned=/[+-]?\d+/,matchOffset=/Z|[+-]\d\d:?\d\d/gi,matchShortOffset=/Z|[+-]\d\d(?::?\d\d)?/gi,matchTimestamp=/[+-]?\d+(\.\d{1,3})?/,matchWord=/[0-9]{0,256}['a-z\u00A0-\u05FF\u0700-\uD7FF\uF900-\uFDCF\uFDF0-\uFF07\uFF10-\uFFEF]{1,256}|[\u0600-\u06FF\/]{1,256}(\s*?[\u0600-\u06FF]{1,256}){1,2}/i,regexes;regexes={};function addRegexToken(token,regex,strictRegex){regexes[token]=isFunction(regex)?regex:function(isStrict,localeData){return isStrict&&strictRegex?strictRegex:regex}}function getParseRegexForToken(token,config){if(!hasOwnProp(regexes,token)){return new RegExp(unescapeFormat(token))}return regexes[token](config._strict,config._locale)}function unescapeFormat(s){return regexEscape(s.replace("\\","").replace(/\\(\[)|\\(\])|\[([^\]\[]*)\]|\\(.)/g,function(matched,p1,p2,p3,p4){return p1||p2||p3||p4}))}function regexEscape(s){return s.replace(/[-\/\\^$*+?.()|[\]{}]/g,"\\$&")}var tokens={};function addParseToken(token,callback){var i,func=callback;if(typeof token==="string"){token=[token]}if(isNumber(callback)){func=function(input,array){array[callback]=toInt(input)}}for(i=0;i<token.length;i++){tokens[token[i]]=func}}function addWeekParseToken(token,callback){addParseToken(token,function(input,array,config,token){config._w=config._w||{};callback(input,config._w,config,token)})}function addTimeToArrayFromToken(token,input,config){if(input!=null&&hasOwnProp(tokens,token)){tokens[token](input,config._a,config,token)}}var YEAR=0,MONTH=1,DATE=2,HOUR=3,MINUTE=4,SECOND=5,MILLISECOND=6,WEEK=7,WEEKDAY=8;function mod(n,x){return(n%x+x)%x}var indexOf;if(Array.prototype.indexOf){indexOf=Array.prototype.indexOf}else{indexOf=function(o){var i;for(i=0;i<this.length;++i){if(this[i]===o){return i}}return-1}}function daysInMonth(year,month){if(isNaN(year)||isNaN(month)){return NaN}var modMonth=mod(month,12);year+=(month-modMonth)/12;return modMonth===1?isLeapYear(year)?29:28:31-modMonth%7%2}addFormatToken("M",["MM",2],"Mo",function(){return this.month()+1});addFormatToken("MMM",0,0,function(format){return this.localeData().monthsShort(this,format)});addFormatToken("MMMM",0,0,function(format){return this.localeData().months(this,format)});addUnitAlias("month","M");addUnitPriority("month",8);addRegexToken("M",match1to2);addRegexToken("MM",match1to2,match2);addRegexToken("MMM",function(isStrict,locale){return locale.monthsShortRegex(isStrict)});addRegexToken("MMMM",function(isStrict,locale){return locale.monthsRegex(isStrict)});addParseToken(["M","MM"],function(input,array){array[MONTH]=toInt(input)-1});addParseToken(["MMM","MMMM"],function(input,array,config,token){var month=config._locale.monthsParse(input,token,config._strict);if(month!=null){array[MONTH]=month}else{getParsingFlags(config).invalidMonth=input}});var defaultLocaleMonths="January_February_March_April_May_June_July_August_September_October_November_December".split("_"),defaultLocaleMonthsShort="Jan_Feb_Mar_Apr_May_Jun_Jul_Aug_Sep_Oct_Nov_Dec".split("_"),MONTHS_IN_FORMAT=/D[oD]?(\[[^\[\]]*\]|\s)+MMMM?/,defaultMonthsShortRegex=matchWord,defaultMonthsRegex=matchWord;function localeMonths(m,format){if(!m){return isArray(this._months)?this._months:this._months["standalone"]}return isArray(this._months)?this._months[m.month()]:this._months[(this._months.isFormat||MONTHS_IN_FORMAT).test(format)?"format":"standalone"][m.month()]}function localeMonthsShort(m,format){if(!m){return isArray(this._monthsShort)?this._monthsShort:this._monthsShort["standalone"]}return isArray(this._monthsShort)?this._monthsShort[m.month()]:this._monthsShort[MONTHS_IN_FORMAT.test(format)?"format":"standalone"][m.month()]}function handleStrictParse(monthName,format,strict){var i,ii,mom,llc=monthName.toLocaleLowerCase();if(!this._monthsParse){this._monthsParse=[];this._longMonthsParse=[];this._shortMonthsParse=[];for(i=0;i<12;++i){mom=createUTC([2e3,i]);this._shortMonthsParse[i]=this.monthsShort(mom,"").toLocaleLowerCase();this._longMonthsParse[i]=this.months(mom,"").toLocaleLowerCase()}}if(strict){if(format==="MMM"){ii=indexOf.call(this._shortMonthsParse,llc);return ii!==-1?ii:null}else{ii=indexOf.call(this._longMonthsParse,llc);return ii!==-1?ii:null}}else{if(format==="MMM"){ii=indexOf.call(this._shortMonthsParse,llc);if(ii!==-1){return ii}ii=indexOf.call(this._longMonthsParse,llc);return ii!==-1?ii:null}else{ii=indexOf.call(this._longMonthsParse,llc);if(ii!==-1){return ii}ii=indexOf.call(this._shortMonthsParse,llc);return ii!==-1?ii:null}}}function localeMonthsParse(monthName,format,strict){var i,mom,regex;if(this._monthsParseExact){return handleStrictParse.call(this,monthName,format,strict)}if(!this._monthsParse){this._monthsParse=[];this._longMonthsParse=[];this._shortMonthsParse=[]}for(i=0;i<12;i++){mom=createUTC([2e3,i]);if(strict&&!this._longMonthsParse[i]){this._longMonthsParse[i]=new RegExp("^"+this.months(mom,"").replace(".","")+"$","i");this._shortMonthsParse[i]=new RegExp("^"+this.monthsShort(mom,"").replace(".","")+"$","i")}if(!strict&&!this._monthsParse[i]){regex="^"+this.months(mom,"")+"|^"+this.monthsShort(mom,"");this._monthsParse[i]=new RegExp(regex.replace(".",""),"i")}if(strict&&format==="MMMM"&&this._longMonthsParse[i].test(monthName)){return i}else if(strict&&format==="MMM"&&this._shortMonthsParse[i].test(monthName)){return i}else if(!strict&&this._monthsParse[i].test(monthName)){return i}}}function setMonth(mom,value){var dayOfMonth;if(!mom.isValid()){return mom}if(typeof value==="string"){if(/^\d+$/.test(value)){value=toInt(value)}else{value=mom.localeData().monthsParse(value);if(!isNumber(value)){return mom}}}dayOfMonth=Math.min(mom.date(),daysInMonth(mom.year(),value));mom._d["set"+(mom._isUTC?"UTC":"")+"Month"](value,dayOfMonth);return mom}function getSetMonth(value){if(value!=null){setMonth(this,value);hooks.updateOffset(this,true);return this}else{return get(this,"Month")}}function getDaysInMonth(){return daysInMonth(this.year(),this.month())}function monthsShortRegex(isStrict){if(this._monthsParseExact){if(!hasOwnProp(this,"_monthsRegex")){computeMonthsParse.call(this)}if(isStrict){return this._monthsShortStrictRegex}else{return this._monthsShortRegex}}else{if(!hasOwnProp(this,"_monthsShortRegex")){this._monthsShortRegex=defaultMonthsShortRegex}return this._monthsShortStrictRegex&&isStrict?this._monthsShortStrictRegex:this._monthsShortRegex}}function monthsRegex(isStrict){if(this._monthsParseExact){if(!hasOwnProp(this,"_monthsRegex")){computeMonthsParse.call(this)}if(isStrict){return this._monthsStrictRegex}else{return this._monthsRegex}}else{if(!hasOwnProp(this,"_monthsRegex")){this._monthsRegex=defaultMonthsRegex}return this._monthsStrictRegex&&isStrict?this._monthsStrictRegex:this._monthsRegex}}function computeMonthsParse(){function cmpLenRev(a,b){return b.length-a.length}var shortPieces=[],longPieces=[],mixedPieces=[],i,mom;for(i=0;i<12;i++){mom=createUTC([2e3,i]);shortPieces.push(this.monthsShort(mom,""));longPieces.push(this.months(mom,""));mixedPieces.push(this.months(mom,""));mixedPieces.push(this.monthsShort(mom,""))}shortPieces.sort(cmpLenRev);longPieces.sort(cmpLenRev);mixedPieces.sort(cmpLenRev);for(i=0;i<12;i++){shortPieces[i]=regexEscape(shortPieces[i]);longPieces[i]=regexEscape(longPieces[i])}for(i=0;i<24;i++){mixedPieces[i]=regexEscape(mixedPieces[i])}this._monthsRegex=new RegExp("^("+mixedPieces.join("|")+")","i");this._monthsShortRegex=this._monthsRegex;this._monthsStrictRegex=new RegExp("^("+longPieces.join("|")+")","i");this._monthsShortStrictRegex=new RegExp("^("+shortPieces.join("|")+")","i")}addFormatToken("Y",0,0,function(){var y=this.year();return y<=9999?zeroFill(y,4):"+"+y});addFormatToken(0,["YY",2],0,function(){return this.year()%100});addFormatToken(0,["YYYY",4],0,"year");addFormatToken(0,["YYYYY",5],0,"year");addFormatToken(0,["YYYYYY",6,true],0,"year");addUnitAlias("year","y");addUnitPriority("year",1);addRegexToken("Y",matchSigned);addRegexToken("YY",match1to2,match2);addRegexToken("YYYY",match1to4,match4);addRegexToken("YYYYY",match1to6,match6);addRegexToken("YYYYYY",match1to6,match6);addParseToken(["YYYYY","YYYYYY"],YEAR);addParseToken("YYYY",function(input,array){array[YEAR]=input.length===2?hooks.parseTwoDigitYear(input):toInt(input)});addParseToken("YY",function(input,array){array[YEAR]=hooks.parseTwoDigitYear(input)});addParseToken("Y",function(input,array){array[YEAR]=parseInt(input,10)});function daysInYear(year){return isLeapYear(year)?366:365}hooks.parseTwoDigitYear=function(input){return toInt(input)+(toInt(input)>68?1900:2e3)};var getSetYear=makeGetSet("FullYear",true);function getIsLeapYear(){return isLeapYear(this.year())}function createDate(y,m,d,h,M,s,ms){var date;if(y<100&&y>=0){date=new Date(y+400,m,d,h,M,s,ms);if(isFinite(date.getFullYear())){date.setFullYear(y)}}else{date=new Date(y,m,d,h,M,s,ms)}return date}function createUTCDate(y){var date,args;if(y<100&&y>=0){args=Array.prototype.slice.call(arguments);args[0]=y+400;date=new Date(Date.UTC.apply(null,args));if(isFinite(date.getUTCFullYear())){date.setUTCFullYear(y)}}else{date=new Date(Date.UTC.apply(null,arguments))}return date}function firstWeekOffset(year,dow,doy){var fwd=7+dow-doy,fwdlw=(7+createUTCDate(year,0,fwd).getUTCDay()-dow)%7;return-fwdlw+fwd-1}function dayOfYearFromWeeks(year,week,weekday,dow,doy){var localWeekday=(7+weekday-dow)%7,weekOffset=firstWeekOffset(year,dow,doy),dayOfYear=1+7*(week-1)+localWeekday+weekOffset,resYear,resDayOfYear;if(dayOfYear<=0){resYear=year-1;resDayOfYear=daysInYear(resYear)+dayOfYear}else if(dayOfYear>daysInYear(year)){resYear=year+1;resDayOfYear=dayOfYear-daysInYear(year)}else{resYear=year;resDayOfYear=dayOfYear}return{year:resYear,dayOfYear:resDayOfYear}}function weekOfYear(mom,dow,doy){var weekOffset=firstWeekOffset(mom.year(),dow,doy),week=Math.floor((mom.dayOfYear()-weekOffset-1)/7)+1,resWeek,resYear;if(week<1){resYear=mom.year()-1;resWeek=week+weeksInYear(resYear,dow,doy)}else if(week>weeksInYear(mom.year(),dow,doy)){resWeek=week-weeksInYear(mom.year(),dow,doy);resYear=mom.year()+1}else{resYear=mom.year();resWeek=week}return{week:resWeek,year:resYear}}function weeksInYear(year,dow,doy){var weekOffset=firstWeekOffset(year,dow,doy),weekOffsetNext=firstWeekOffset(year+1,dow,doy);return(daysInYear(year)-weekOffset+weekOffsetNext)/7}addFormatToken("w",["ww",2],"wo","week");addFormatToken("W",["WW",2],"Wo","isoWeek");addUnitAlias("week","w");addUnitAlias("isoWeek","W");addUnitPriority("week",5);addUnitPriority("isoWeek",5);addRegexToken("w",match1to2);addRegexToken("ww",match1to2,match2);addRegexToken("W",match1to2);addRegexToken("WW",match1to2,match2);addWeekParseToken(["w","ww","W","WW"],function(input,week,config,token){week[token.substr(0,1)]=toInt(input)});function localeWeek(mom){return weekOfYear(mom,this._week.dow,this._week.doy).week}var defaultLocaleWeek={dow:0,doy:6};function localeFirstDayOfWeek(){return this._week.dow}function localeFirstDayOfYear(){return this._week.doy}function getSetWeek(input){var week=this.localeData().week(this);return input==null?week:this.add((input-week)*7,"d")}function getSetISOWeek(input){var week=weekOfYear(this,1,4).week;return input==null?week:this.add((input-week)*7,"d")}addFormatToken("d",0,"do","day");addFormatToken("dd",0,0,function(format){return this.localeData().weekdaysMin(this,format)});addFormatToken("ddd",0,0,function(format){return this.localeData().weekdaysShort(this,format)});addFormatToken("dddd",0,0,function(format){return this.localeData().weekdays(this,format)});addFormatToken("e",0,0,"weekday");addFormatToken("E",0,0,"isoWeekday");addUnitAlias("day","d");addUnitAlias("weekday","e");addUnitAlias("isoWeekday","E");addUnitPriority("day",11);addUnitPriority("weekday",11);addUnitPriority("isoWeekday",11);addRegexToken("d",match1to2);addRegexToken("e",match1to2);addRegexToken("E",match1to2);addRegexToken("dd",function(isStrict,locale){return locale.weekdaysMinRegex(isStrict)});addRegexToken("ddd",function(isStrict,locale){return locale.weekdaysShortRegex(isStrict)});addRegexToken("dddd",function(isStrict,locale){return locale.weekdaysRegex(isStrict)});addWeekParseToken(["dd","ddd","dddd"],function(input,week,config,token){var weekday=config._locale.weekdaysParse(input,token,config._strict);if(weekday!=null){week.d=weekday}else{getParsingFlags(config).invalidWeekday=input}});addWeekParseToken(["d","e","E"],function(input,week,config,token){week[token]=toInt(input)});function parseWeekday(input,locale){if(typeof input!=="string"){return input}if(!isNaN(input)){return parseInt(input,10)}input=locale.weekdaysParse(input);if(typeof input==="number"){return input}return null}function parseIsoWeekday(input,locale){if(typeof input==="string"){return locale.weekdaysParse(input)%7||7}return isNaN(input)?null:input}function shiftWeekdays(ws,n){return ws.slice(n,7).concat(ws.slice(0,n))}var defaultLocaleWeekdays="Sunday_Monday_Tuesday_Wednesday_Thursday_Friday_Saturday".split("_"),defaultLocaleWeekdaysShort="Sun_Mon_Tue_Wed_Thu_Fri_Sat".split("_"),defaultLocaleWeekdaysMin="Su_Mo_Tu_We_Th_Fr_Sa".split("_"),defaultWeekdaysRegex=matchWord,defaultWeekdaysShortRegex=matchWord,defaultWeekdaysMinRegex=matchWord;function localeWeekdays(m,format){var weekdays=isArray(this._weekdays)?this._weekdays:this._weekdays[m&&m!==true&&this._weekdays.isFormat.test(format)?"format":"standalone"];return m===true?shiftWeekdays(weekdays,this._week.dow):m?weekdays[m.day()]:weekdays}function localeWeekdaysShort(m){return m===true?shiftWeekdays(this._weekdaysShort,this._week.dow):m?this._weekdaysShort[m.day()]:this._weekdaysShort}function localeWeekdaysMin(m){return m===true?shiftWeekdays(this._weekdaysMin,this._week.dow):m?this._weekdaysMin[m.day()]:this._weekdaysMin}function handleStrictParse$1(weekdayName,format,strict){var i,ii,mom,llc=weekdayName.toLocaleLowerCase();if(!this._weekdaysParse){this._weekdaysParse=[];this._shortWeekdaysParse=[];this._minWeekdaysParse=[];for(i=0;i<7;++i){mom=createUTC([2e3,1]).day(i);this._minWeekdaysParse[i]=this.weekdaysMin(mom,"").toLocaleLowerCase();this._shortWeekdaysParse[i]=this.weekdaysShort(mom,"").toLocaleLowerCase();this._weekdaysParse[i]=this.weekdays(mom,"").toLocaleLowerCase()}}if(strict){if(format==="dddd"){ii=indexOf.call(this._weekdaysParse,llc);return ii!==-1?ii:null}else if(format==="ddd"){ii=indexOf.call(this._shortWeekdaysParse,llc);return ii!==-1?ii:null}else{ii=indexOf.call(this._minWeekdaysParse,llc);return ii!==-1?ii:null}}else{if(format==="dddd"){ii=indexOf.call(this._weekdaysParse,llc);if(ii!==-1){return ii}ii=indexOf.call(this._shortWeekdaysParse,llc);if(ii!==-1){return ii}ii=indexOf.call(this._minWeekdaysParse,llc);return ii!==-1?ii:null}else if(format==="ddd"){ii=indexOf.call(this._shortWeekdaysParse,llc);if(ii!==-1){return ii}ii=indexOf.call(this._weekdaysParse,llc);if(ii!==-1){return ii}ii=indexOf.call(this._minWeekdaysParse,llc);return ii!==-1?ii:null}else{ii=indexOf.call(this._minWeekdaysParse,llc);if(ii!==-1){return ii}ii=indexOf.call(this._weekdaysParse,llc);if(ii!==-1){return ii}ii=indexOf.call(this._shortWeekdaysParse,llc);return ii!==-1?ii:null}}}function localeWeekdaysParse(weekdayName,format,strict){var i,mom,regex;if(this._weekdaysParseExact){return handleStrictParse$1.call(this,weekdayName,format,strict)}if(!this._weekdaysParse){this._weekdaysParse=[];this._minWeekdaysParse=[];this._shortWeekdaysParse=[];this._fullWeekdaysParse=[]}for(i=0;i<7;i++){mom=createUTC([2e3,1]).day(i);if(strict&&!this._fullWeekdaysParse[i]){this._fullWeekdaysParse[i]=new RegExp("^"+this.weekdays(mom,"").replace(".","\\.?")+"$","i");this._shortWeekdaysParse[i]=new RegExp("^"+this.weekdaysShort(mom,"").replace(".","\\.?")+"$","i");this._minWeekdaysParse[i]=new RegExp("^"+this.weekdaysMin(mom,"").replace(".","\\.?")+"$","i")}if(!this._weekdaysParse[i]){regex="^"+this.weekdays(mom,"")+"|^"+this.weekdaysShort(mom,"")+"|^"+this.weekdaysMin(mom,"");this._weekdaysParse[i]=new RegExp(regex.replace(".",""),"i")}if(strict&&format==="dddd"&&this._fullWeekdaysParse[i].test(weekdayName)){return i}else if(strict&&format==="ddd"&&this._shortWeekdaysParse[i].test(weekdayName)){return i}else if(strict&&format==="dd"&&this._minWeekdaysParse[i].test(weekdayName)){return i}else if(!strict&&this._weekdaysParse[i].test(weekdayName)){return i}}}function getSetDayOfWeek(input){if(!this.isValid()){return input!=null?this:NaN}var day=this._isUTC?this._d.getUTCDay():this._d.getDay();if(input!=null){input=parseWeekday(input,this.localeData());return this.add(input-day,"d")}else{return day}}function getSetLocaleDayOfWeek(input){if(!this.isValid()){return input!=null?this:NaN}var weekday=(this.day()+7-this.localeData()._week.dow)%7;return input==null?weekday:this.add(input-weekday,"d")}function getSetISODayOfWeek(input){if(!this.isValid()){return input!=null?this:NaN}if(input!=null){var weekday=parseIsoWeekday(input,this.localeData());return this.day(this.day()%7?weekday:weekday-7)}else{return this.day()||7}}function weekdaysRegex(isStrict){if(this._weekdaysParseExact){if(!hasOwnProp(this,"_weekdaysRegex")){computeWeekdaysParse.call(this)}if(isStrict){return this._weekdaysStrictRegex}else{return this._weekdaysRegex}}else{if(!hasOwnProp(this,"_weekdaysRegex")){this._weekdaysRegex=defaultWeekdaysRegex}return this._weekdaysStrictRegex&&isStrict?this._weekdaysStrictRegex:this._weekdaysRegex}}function weekdaysShortRegex(isStrict){if(this._weekdaysParseExact){if(!hasOwnProp(this,"_weekdaysRegex")){computeWeekdaysParse.call(this)}if(isStrict){return this._weekdaysShortStrictRegex}else{return this._weekdaysShortRegex}}else{if(!hasOwnProp(this,"_weekdaysShortRegex")){this._weekdaysShortRegex=defaultWeekdaysShortRegex}return this._weekdaysShortStrictRegex&&isStrict?this._weekdaysShortStrictRegex:this._weekdaysShortRegex}}function weekdaysMinRegex(isStrict){if(this._weekdaysParseExact){if(!hasOwnProp(this,"_weekdaysRegex")){computeWeekdaysParse.call(this)}if(isStrict){return this._weekdaysMinStrictRegex}else{return this._weekdaysMinRegex}}else{if(!hasOwnProp(this,"_weekdaysMinRegex")){this._weekdaysMinRegex=defaultWeekdaysMinRegex}return this._weekdaysMinStrictRegex&&isStrict?this._weekdaysMinStrictRegex:this._weekdaysMinRegex}}function computeWeekdaysParse(){function cmpLenRev(a,b){return b.length-a.length}var minPieces=[],shortPieces=[],longPieces=[],mixedPieces=[],i,mom,minp,shortp,longp;for(i=0;i<7;i++){mom=createUTC([2e3,1]).day(i);minp=regexEscape(this.weekdaysMin(mom,""));shortp=regexEscape(this.weekdaysShort(mom,""));longp=regexEscape(this.weekdays(mom,""));minPieces.push(minp);shortPieces.push(shortp);longPieces.push(longp);mixedPieces.push(minp);mixedPieces.push(shortp);mixedPieces.push(longp)}minPieces.sort(cmpLenRev);shortPieces.sort(cmpLenRev);longPieces.sort(cmpLenRev);mixedPieces.sort(cmpLenRev);this._weekdaysRegex=new RegExp("^("+mixedPieces.join("|")+")","i");this._weekdaysShortRegex=this._weekdaysRegex;this._weekdaysMinRegex=this._weekdaysRegex;this._weekdaysStrictRegex=new RegExp("^("+longPieces.join("|")+")","i");this._weekdaysShortStrictRegex=new RegExp("^("+shortPieces.join("|")+")","i");this._weekdaysMinStrictRegex=new RegExp("^("+minPieces.join("|")+")","i")}function hFormat(){return this.hours()%12||12}function kFormat(){return this.hours()||24}addFormatToken("H",["HH",2],0,"hour");addFormatToken("h",["hh",2],0,hFormat);addFormatToken("k",["kk",2],0,kFormat);addFormatToken("hmm",0,0,function(){return""+hFormat.apply(this)+zeroFill(this.minutes(),2)});addFormatToken("hmmss",0,0,function(){return""+hFormat.apply(this)+zeroFill(this.minutes(),2)+zeroFill(this.seconds(),2)});addFormatToken("Hmm",0,0,function(){return""+this.hours()+zeroFill(this.minutes(),2)});addFormatToken("Hmmss",0,0,function(){return""+this.hours()+zeroFill(this.minutes(),2)+zeroFill(this.seconds(),2)});function meridiem(token,lowercase){addFormatToken(token,0,0,function(){return this.localeData().meridiem(this.hours(),this.minutes(),lowercase)})}meridiem("a",true);meridiem("A",false);addUnitAlias("hour","h");addUnitPriority("hour",13);function matchMeridiem(isStrict,locale){return locale._meridiemParse}addRegexToken("a",matchMeridiem);addRegexToken("A",matchMeridiem);addRegexToken("H",match1to2);addRegexToken("h",match1to2);addRegexToken("k",match1to2);addRegexToken("HH",match1to2,match2);addRegexToken("hh",match1to2,match2);addRegexToken("kk",match1to2,match2);addRegexToken("hmm",match3to4);addRegexToken("hmmss",match5to6);addRegexToken("Hmm",match3to4);addRegexToken("Hmmss",match5to6);addParseToken(["H","HH"],HOUR);addParseToken(["k","kk"],function(input,array,config){var kInput=toInt(input);array[HOUR]=kInput===24?0:kInput});addParseToken(["a","A"],function(input,array,config){config._isPm=config._locale.isPM(input);config._meridiem=input});addParseToken(["h","hh"],function(input,array,config){array[HOUR]=toInt(input);getParsingFlags(config).bigHour=true});addParseToken("hmm",function(input,array,config){var pos=input.length-2;array[HOUR]=toInt(input.substr(0,pos));array[MINUTE]=toInt(input.substr(pos));getParsingFlags(config).bigHour=true});addParseToken("hmmss",function(input,array,config){var pos1=input.length-4,pos2=input.length-2;array[HOUR]=toInt(input.substr(0,pos1));array[MINUTE]=toInt(input.substr(pos1,2));array[SECOND]=toInt(input.substr(pos2));getParsingFlags(config).bigHour=true});addParseToken("Hmm",function(input,array,config){var pos=input.length-2;array[HOUR]=toInt(input.substr(0,pos));array[MINUTE]=toInt(input.substr(pos))});addParseToken("Hmmss",function(input,array,config){var pos1=input.length-4,pos2=input.length-2;array[HOUR]=toInt(input.substr(0,pos1));array[MINUTE]=toInt(input.substr(pos1,2));array[SECOND]=toInt(input.substr(pos2))});function localeIsPM(input){return(input+"").toLowerCase().charAt(0)==="p"}var defaultLocaleMeridiemParse=/[ap]\.?m?\.?/i,getSetHour=makeGetSet("Hours",true);function localeMeridiem(hours,minutes,isLower){if(hours>11){return isLower?"pm":"PM"}else{return isLower?"am":"AM"}}var baseConfig={calendar:defaultCalendar,longDateFormat:defaultLongDateFormat,invalidDate:defaultInvalidDate,ordinal:defaultOrdinal,dayOfMonthOrdinalParse:defaultDayOfMonthOrdinalParse,relativeTime:defaultRelativeTime,months:defaultLocaleMonths,monthsShort:defaultLocaleMonthsShort,week:defaultLocaleWeek,weekdays:defaultLocaleWeekdays,weekdaysMin:defaultLocaleWeekdaysMin,weekdaysShort:defaultLocaleWeekdaysShort,meridiemParse:defaultLocaleMeridiemParse};var locales={},localeFamilies={},globalLocale;function commonPrefix(arr1,arr2){var i,minl=Math.min(arr1.length,arr2.length);for(i=0;i<minl;i+=1){if(arr1[i]!==arr2[i]){return i}}return minl}function normalizeLocale(key){return key?key.toLowerCase().replace("_","-"):key}function chooseLocale(names){var i=0,j,next,locale,split;while(i<names.length){split=normalizeLocale(names[i]).split("-");j=split.length;next=normalizeLocale(names[i+1]);next=next?next.split("-"):null;while(j>0){locale=loadLocale(split.slice(0,j).join("-"));if(locale){return locale}if(next&&next.length>=j&&commonPrefix(split,next)>=j-1){break}j--}i++}return globalLocale}function loadLocale(name){var oldLocale=null,aliasedRequire;if(locales[name]===undefined&&typeof module!=="undefined"&&module&&module.exports){try{oldLocale=globalLocale._abbr;aliasedRequire=require;aliasedRequire("./locale/"+name);getSetGlobalLocale(oldLocale)}catch(e){locales[name]=null}}return locales[name]}function getSetGlobalLocale(key,values){var data;if(key){if(isUndefined(values)){data=getLocale(key)}else{data=defineLocale(key,values)}if(data){globalLocale=data}else{if(typeof console!=="undefined"&&console.warn){console.warn("Locale "+key+" not found. Did you forget to load it?")}}}return globalLocale._abbr}function defineLocale(name,config){if(config!==null){var locale,parentConfig=baseConfig;config.abbr=name;if(locales[name]!=null){deprecateSimple("defineLocaleOverride","use moment.updateLocale(localeName, config) to change "+"an existing locale. moment.defineLocale(localeName, "+"config) should only be used for creating a new locale "+"See http://momentjs.com/guides/#/warnings/define-locale/ for more info.");parentConfig=locales[name]._config}else if(config.parentLocale!=null){if(locales[config.parentLocale]!=null){parentConfig=locales[config.parentLocale]._config}else{locale=loadLocale(config.parentLocale);if(locale!=null){parentConfig=locale._config}else{if(!localeFamilies[config.parentLocale]){localeFamilies[config.parentLocale]=[]}localeFamilies[config.parentLocale].push({name:name,config:config});return null}}}locales[name]=new Locale(mergeConfigs(parentConfig,config));if(localeFamilies[name]){localeFamilies[name].forEach(function(x){defineLocale(x.name,x.config)})}getSetGlobalLocale(name);return locales[name]}else{delete locales[name];return null}}function updateLocale(name,config){if(config!=null){var locale,tmpLocale,parentConfig=baseConfig;if(locales[name]!=null&&locales[name].parentLocale!=null){locales[name].set(mergeConfigs(locales[name]._config,config))}else{tmpLocale=loadLocale(name);if(tmpLocale!=null){parentConfig=tmpLocale._config}config=mergeConfigs(parentConfig,config);if(tmpLocale==null){config.abbr=name}locale=new Locale(config);locale.parentLocale=locales[name];locales[name]=locale}getSetGlobalLocale(name)}else{if(locales[name]!=null){if(locales[name].parentLocale!=null){locales[name]=locales[name].parentLocale;if(name===getSetGlobalLocale()){getSetGlobalLocale(name)}}else if(locales[name]!=null){delete locales[name]}}}return locales[name]}function getLocale(key){var locale;if(key&&key._locale&&key._locale._abbr){key=key._locale._abbr}if(!key){return globalLocale}if(!isArray(key)){locale=loadLocale(key);if(locale){return locale}key=[key]}return chooseLocale(key)}function listLocales(){return keys(locales)}function checkOverflow(m){var overflow,a=m._a;if(a&&getParsingFlags(m).overflow===-2){overflow=a[MONTH]<0||a[MONTH]>11?MONTH:a[DATE]<1||a[DATE]>daysInMonth(a[YEAR],a[MONTH])?DATE:a[HOUR]<0||a[HOUR]>24||a[HOUR]===24&&(a[MINUTE]!==0||a[SECOND]!==0||a[MILLISECOND]!==0)?HOUR:a[MINUTE]<0||a[MINUTE]>59?MINUTE:a[SECOND]<0||a[SECOND]>59?SECOND:a[MILLISECOND]<0||a[MILLISECOND]>999?MILLISECOND:-1;if(getParsingFlags(m)._overflowDayOfYear&&(overflow<YEAR||overflow>DATE)){overflow=DATE}if(getParsingFlags(m)._overflowWeeks&&overflow===-1){overflow=WEEK}if(getParsingFlags(m)._overflowWeekday&&overflow===-1){overflow=WEEKDAY}getParsingFlags(m).overflow=overflow}return m}var extendedIsoRegex=/^\s*((?:[+-]\d{6}|\d{4})-(?:\d\d-\d\d|W\d\d-\d|W\d\d|\d\d\d|\d\d))(?:(T| )(\d\d(?::\d\d(?::\d\d(?:[.,]\d+)?)?)?)([+-]\d\d(?::?\d\d)?|\s*Z)?)?$/,basicIsoRegex=/^\s*((?:[+-]\d{6}|\d{4})(?:\d\d\d\d|W\d\d\d|W\d\d|\d\d\d|\d\d|))(?:(T| )(\d\d(?:\d\d(?:\d\d(?:[.,]\d+)?)?)?)([+-]\d\d(?::?\d\d)?|\s*Z)?)?$/,tzRegex=/Z|[+-]\d\d(?::?\d\d)?/,isoDates=[["YYYYYY-MM-DD",/[+-]\d{6}-\d\d-\d\d/],["YYYY-MM-DD",/\d{4}-\d\d-\d\d/],["GGGG-[W]WW-E",/\d{4}-W\d\d-\d/],["GGGG-[W]WW",/\d{4}-W\d\d/,false],["YYYY-DDD",/\d{4}-\d{3}/],["YYYY-MM",/\d{4}-\d\d/,false],["YYYYYYMMDD",/[+-]\d{10}/],["YYYYMMDD",/\d{8}/],["GGGG[W]WWE",/\d{4}W\d{3}/],["GGGG[W]WW",/\d{4}W\d{2}/,false],["YYYYDDD",/\d{7}/],["YYYYMM",/\d{6}/,false],["YYYY",/\d{4}/,false]],isoTimes=[["HH:mm:ss.SSSS",/\d\d:\d\d:\d\d\.\d+/],["HH:mm:ss,SSSS",/\d\d:\d\d:\d\d,\d+/],["HH:mm:ss",/\d\d:\d\d:\d\d/],["HH:mm",/\d\d:\d\d/],["HHmmss.SSSS",/\d\d\d\d\d\d\.\d+/],["HHmmss,SSSS",/\d\d\d\d\d\d,\d+/],["HHmmss",/\d\d\d\d\d\d/],["HHmm",/\d\d\d\d/],["HH",/\d\d/]],aspNetJsonRegex=/^\/?Date\((-?\d+)/i,rfc2822=/^(?:(Mon|Tue|Wed|Thu|Fri|Sat|Sun),?\s)?(\d{1,2})\s(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)\s(\d{2,4})\s(\d\d):(\d\d)(?::(\d\d))?\s(?:(UT|GMT|[ECMP][SD]T)|([Zz])|([+-]\d{4}))$/,obsOffsets={UT:0,GMT:0,EDT:-4*60,EST:-5*60,CDT:-5*60,CST:-6*60,MDT:-6*60,MST:-7*60,PDT:-7*60,PST:-8*60};function configFromISO(config){var i,l,string=config._i,match=extendedIsoRegex.exec(string)||basicIsoRegex.exec(string),allowTime,dateFormat,timeFormat,tzFormat;if(match){getParsingFlags(config).iso=true;for(i=0,l=isoDates.length;i<l;i++){if(isoDates[i][1].exec(match[1])){dateFormat=isoDates[i][0];allowTime=isoDates[i][2]!==false;break}}if(dateFormat==null){config._isValid=false;return}if(match[3]){for(i=0,l=isoTimes.length;i<l;i++){if(isoTimes[i][1].exec(match[3])){timeFormat=(match[2]||" ")+isoTimes[i][0];break}}if(timeFormat==null){config._isValid=false;return}}if(!allowTime&&timeFormat!=null){config._isValid=false;return}if(match[4]){if(tzRegex.exec(match[4])){tzFormat="Z"}else{config._isValid=false;return}}config._f=dateFormat+(timeFormat||"")+(tzFormat||"");configFromStringAndFormat(config)}else{config._isValid=false}}function extractFromRFC2822Strings(yearStr,monthStr,dayStr,hourStr,minuteStr,secondStr){var result=[untruncateYear(yearStr),defaultLocaleMonthsShort.indexOf(monthStr),parseInt(dayStr,10),parseInt(hourStr,10),parseInt(minuteStr,10)];if(secondStr){result.push(parseInt(secondStr,10))}return result}function untruncateYear(yearStr){var year=parseInt(yearStr,10);if(year<=49){return 2e3+year}else if(year<=999){return 1900+year}return year}function preprocessRFC2822(s){return s.replace(/\([^)]*\)|[\n\t]/g," ").replace(/(\s\s+)/g," ").replace(/^\s\s*/,"").replace(/\s\s*$/,"")}function checkWeekday(weekdayStr,parsedInput,config){if(weekdayStr){var weekdayProvided=defaultLocaleWeekdaysShort.indexOf(weekdayStr),weekdayActual=new Date(parsedInput[0],parsedInput[1],parsedInput[2]).getDay();if(weekdayProvided!==weekdayActual){getParsingFlags(config).weekdayMismatch=true;config._isValid=false;return false}}return true}function calculateOffset(obsOffset,militaryOffset,numOffset){if(obsOffset){return obsOffsets[obsOffset]}else if(militaryOffset){return 0}else{var hm=parseInt(numOffset,10),m=hm%100,h=(hm-m)/100;return h*60+m}}function configFromRFC2822(config){var match=rfc2822.exec(preprocessRFC2822(config._i)),parsedArray;if(match){parsedArray=extractFromRFC2822Strings(match[4],match[3],match[2],match[5],match[6],match[7]);if(!checkWeekday(match[1],parsedArray,config)){return}config._a=parsedArray;config._tzm=calculateOffset(match[8],match[9],match[10]);config._d=createUTCDate.apply(null,config._a);config._d.setUTCMinutes(config._d.getUTCMinutes()-config._tzm);getParsingFlags(config).rfc2822=true}else{config._isValid=false}}function configFromString(config){var matched=aspNetJsonRegex.exec(config._i);if(matched!==null){config._d=new Date(+matched[1]);return}configFromISO(config);if(config._isValid===false){delete config._isValid}else{return}configFromRFC2822(config);if(config._isValid===false){delete config._isValid}else{return}if(config._strict){config._isValid=false}else{hooks.createFromInputFallback(config)}}hooks.createFromInputFallback=deprecate("value provided is not in a recognized RFC2822 or ISO format. moment construction falls back to js Date(), "+"which is not reliable across all browsers and versions. Non RFC2822/ISO date formats are "+"discouraged. Please refer to http://momentjs.com/guides/#/warnings/js-date/ for more info.",function(config){config._d=new Date(config._i+(config._useUTC?" UTC":""))});function defaults(a,b,c){if(a!=null){return a}if(b!=null){return b}return c}function currentDateArray(config){var nowValue=new Date(hooks.now());if(config._useUTC){return[nowValue.getUTCFullYear(),nowValue.getUTCMonth(),nowValue.getUTCDate()]}return[nowValue.getFullYear(),nowValue.getMonth(),nowValue.getDate()]}function configFromArray(config){var i,date,input=[],currentDate,expectedWeekday,yearToUse;if(config._d){return}currentDate=currentDateArray(config);if(config._w&&config._a[DATE]==null&&config._a[MONTH]==null){dayOfYearFromWeekInfo(config)}if(config._dayOfYear!=null){yearToUse=defaults(config._a[YEAR],currentDate[YEAR]);if(config._dayOfYear>daysInYear(yearToUse)||config._dayOfYear===0){getParsingFlags(config)._overflowDayOfYear=true}date=createUTCDate(yearToUse,0,config._dayOfYear);config._a[MONTH]=date.getUTCMonth();config._a[DATE]=date.getUTCDate()}for(i=0;i<3&&config._a[i]==null;++i){config._a[i]=input[i]=currentDate[i]}for(;i<7;i++){config._a[i]=input[i]=config._a[i]==null?i===2?1:0:config._a[i]}if(config._a[HOUR]===24&&config._a[MINUTE]===0&&config._a[SECOND]===0&&config._a[MILLISECOND]===0){config._nextDay=true;config._a[HOUR]=0}config._d=(config._useUTC?createUTCDate:createDate).apply(null,input);expectedWeekday=config._useUTC?config._d.getUTCDay():config._d.getDay();if(config._tzm!=null){config._d.setUTCMinutes(config._d.getUTCMinutes()-config._tzm)}if(config._nextDay){config._a[HOUR]=24}if(config._w&&typeof config._w.d!=="undefined"&&config._w.d!==expectedWeekday){getParsingFlags(config).weekdayMismatch=true}}function dayOfYearFromWeekInfo(config){var w,weekYear,week,weekday,dow,doy,temp,weekdayOverflow,curWeek;w=config._w;if(w.GG!=null||w.W!=null||w.E!=null){dow=1;doy=4;weekYear=defaults(w.GG,config._a[YEAR],weekOfYear(createLocal(),1,4).year);week=defaults(w.W,1);weekday=defaults(w.E,1);if(weekday<1||weekday>7){weekdayOverflow=true}}else{dow=config._locale._week.dow;doy=config._locale._week.doy;curWeek=weekOfYear(createLocal(),dow,doy);weekYear=defaults(w.gg,config._a[YEAR],curWeek.year);week=defaults(w.w,curWeek.week);if(w.d!=null){weekday=w.d;if(weekday<0||weekday>6){weekdayOverflow=true}}else if(w.e!=null){weekday=w.e+dow;if(w.e<0||w.e>6){weekdayOverflow=true}}else{weekday=dow}}if(week<1||week>weeksInYear(weekYear,dow,doy)){getParsingFlags(config)._overflowWeeks=true}else if(weekdayOverflow!=null){getParsingFlags(config)._overflowWeekday=true}else{temp=dayOfYearFromWeeks(weekYear,week,weekday,dow,doy);config._a[YEAR]=temp.year;config._dayOfYear=temp.dayOfYear}}hooks.ISO_8601=function(){};hooks.RFC_2822=function(){};function configFromStringAndFormat(config){if(config._f===hooks.ISO_8601){configFromISO(config);return}if(config._f===hooks.RFC_2822){configFromRFC2822(config);return}config._a=[];getParsingFlags(config).empty=true;var string=""+config._i,i,parsedInput,tokens,token,skipped,stringLength=string.length,totalParsedInputLength=0,era;tokens=expandFormat(config._f,config._locale).match(formattingTokens)||[];for(i=0;i<tokens.length;i++){token=tokens[i];parsedInput=(string.match(getParseRegexForToken(token,config))||[])[0];if(parsedInput){skipped=string.substr(0,string.indexOf(parsedInput));if(skipped.length>0){getParsingFlags(config).unusedInput.push(skipped)}string=string.slice(string.indexOf(parsedInput)+parsedInput.length);totalParsedInputLength+=parsedInput.length}if(formatTokenFunctions[token]){if(parsedInput){getParsingFlags(config).empty=false}else{getParsingFlags(config).unusedTokens.push(token)}addTimeToArrayFromToken(token,parsedInput,config)}else if(config._strict&&!parsedInput){getParsingFlags(config).unusedTokens.push(token)}}getParsingFlags(config).charsLeftOver=stringLength-totalParsedInputLength;if(string.length>0){getParsingFlags(config).unusedInput.push(string)}if(config._a[HOUR]<=12&&getParsingFlags(config).bigHour===true&&config._a[HOUR]>0){getParsingFlags(config).bigHour=undefined}getParsingFlags(config).parsedDateParts=config._a.slice(0);getParsingFlags(config).meridiem=config._meridiem;config._a[HOUR]=meridiemFixWrap(config._locale,config._a[HOUR],config._meridiem);era=getParsingFlags(config).era;if(era!==null){config._a[YEAR]=config._locale.erasConvertYear(era,config._a[YEAR])}configFromArray(config);checkOverflow(config)}function meridiemFixWrap(locale,hour,meridiem){var isPm;if(meridiem==null){return hour}if(locale.meridiemHour!=null){return locale.meridiemHour(hour,meridiem)}else if(locale.isPM!=null){isPm=locale.isPM(meridiem);if(isPm&&hour<12){hour+=12}if(!isPm&&hour===12){hour=0}return hour}else{return hour}}function configFromStringAndArray(config){var tempConfig,bestMoment,scoreToBeat,i,currentScore,validFormatFound,bestFormatIsValid=false;if(config._f.length===0){getParsingFlags(config).invalidFormat=true;config._d=new Date(NaN);return}for(i=0;i<config._f.length;i++){currentScore=0;validFormatFound=false;tempConfig=copyConfig({},config);if(config._useUTC!=null){tempConfig._useUTC=config._useUTC}tempConfig._f=config._f[i];configFromStringAndFormat(tempConfig);if(isValid(tempConfig)){validFormatFound=true}currentScore+=getParsingFlags(tempConfig).charsLeftOver;currentScore+=getParsingFlags(tempConfig).unusedTokens.length*10;getParsingFlags(tempConfig).score=currentScore;if(!bestFormatIsValid){if(scoreToBeat==null||currentScore<scoreToBeat||validFormatFound){scoreToBeat=currentScore;bestMoment=tempConfig;if(validFormatFound){bestFormatIsValid=true}}}else{if(currentScore<scoreToBeat){scoreToBeat=currentScore;bestMoment=tempConfig}}}extend(config,bestMoment||tempConfig)}function configFromObject(config){if(config._d){return}var i=normalizeObjectUnits(config._i),dayOrDate=i.day===undefined?i.date:i.day;config._a=map([i.year,i.month,dayOrDate,i.hour,i.minute,i.second,i.millisecond],function(obj){return obj&&parseInt(obj,10)});configFromArray(config)}function createFromConfig(config){var res=new Moment(checkOverflow(prepareConfig(config)));if(res._nextDay){res.add(1,"d");res._nextDay=undefined}return res}function prepareConfig(config){var input=config._i,format=config._f;config._locale=config._locale||getLocale(config._l);if(input===null||format===undefined&&input===""){return createInvalid({nullInput:true})}if(typeof input==="string"){config._i=input=config._locale.preparse(input)}if(isMoment(input)){return new Moment(checkOverflow(input))}else if(isDate(input)){config._d=input}else if(isArray(format)){configFromStringAndArray(config)}else if(format){configFromStringAndFormat(config)}else{configFromInput(config)}if(!isValid(config)){config._d=null}return config}function configFromInput(config){var input=config._i;if(isUndefined(input)){config._d=new Date(hooks.now())}else if(isDate(input)){config._d=new Date(input.valueOf())}else if(typeof input==="string"){configFromString(config)}else if(isArray(input)){config._a=map(input.slice(0),function(obj){return parseInt(obj,10)});configFromArray(config)}else if(isObject(input)){configFromObject(config)}else if(isNumber(input)){config._d=new Date(input)}else{hooks.createFromInputFallback(config)}}function createLocalOrUTC(input,format,locale,strict,isUTC){var c={};if(format===true||format===false){strict=format;format=undefined}if(locale===true||locale===false){strict=locale;locale=undefined}if(isObject(input)&&isObjectEmpty(input)||isArray(input)&&input.length===0){input=undefined}c._isAMomentObject=true;c._useUTC=c._isUTC=isUTC;c._l=locale;c._i=input;c._f=format;c._strict=strict;return createFromConfig(c)}function createLocal(input,format,locale,strict){return createLocalOrUTC(input,format,locale,strict,false)}var prototypeMin=deprecate("moment().min is deprecated, use moment.max instead. http://momentjs.com/guides/#/warnings/min-max/",function(){var other=createLocal.apply(null,arguments);if(this.isValid()&&other.isValid()){return other<this?this:other}else{return createInvalid()}}),prototypeMax=deprecate("moment().max is deprecated, use moment.min instead. http://momentjs.com/guides/#/warnings/min-max/",function(){var other=createLocal.apply(null,arguments);if(this.isValid()&&other.isValid()){return other>this?this:other}else{return createInvalid()}});function pickBy(fn,moments){var res,i;if(moments.length===1&&isArray(moments[0])){moments=moments[0]}if(!moments.length){return createLocal()}res=moments[0];for(i=1;i<moments.length;++i){if(!moments[i].isValid()||moments[i][fn](res)){res=moments[i]}}return res}function min(){var args=[].slice.call(arguments,0);return pickBy("isBefore",args)}function max(){var args=[].slice.call(arguments,0);return pickBy("isAfter",args)}var now=function(){return Date.now?Date.now():+new Date};var ordering=["year","quarter","month","week","day","hour","minute","second","millisecond"];function isDurationValid(m){var key,unitHasDecimal=false,i;for(key in m){if(hasOwnProp(m,key)&&!(indexOf.call(ordering,key)!==-1&&(m[key]==null||!isNaN(m[key])))){return false}}for(i=0;i<ordering.length;++i){if(m[ordering[i]]){if(unitHasDecimal){return false}if(parseFloat(m[ordering[i]])!==toInt(m[ordering[i]])){unitHasDecimal=true}}}return true}function isValid$1(){return this._isValid}function createInvalid$1(){return createDuration(NaN)}function Duration(duration){var normalizedInput=normalizeObjectUnits(duration),years=normalizedInput.year||0,quarters=normalizedInput.quarter||0,months=normalizedInput.month||0,weeks=normalizedInput.week||normalizedInput.isoWeek||0,days=normalizedInput.day||0,hours=normalizedInput.hour||0,minutes=normalizedInput.minute||0,seconds=normalizedInput.second||0,milliseconds=normalizedInput.millisecond||0;this._isValid=isDurationValid(normalizedInput);this._milliseconds=+milliseconds+seconds*1e3+minutes*6e4+hours*1e3*60*60;this._days=+days+weeks*7;this._months=+months+quarters*3+years*12;this._data={};this._locale=getLocale();this._bubble()}function isDuration(obj){return obj instanceof Duration}function absRound(number){if(number<0){return Math.round(-1*number)*-1}else{return Math.round(number)}}function compareArrays(array1,array2,dontConvert){var len=Math.min(array1.length,array2.length),lengthDiff=Math.abs(array1.length-array2.length),diffs=0,i;for(i=0;i<len;i++){if(dontConvert&&array1[i]!==array2[i]||!dontConvert&&toInt(array1[i])!==toInt(array2[i])){diffs++}}return diffs+lengthDiff}function offset(token,separator){addFormatToken(token,0,0,function(){var offset=this.utcOffset(),sign="+";if(offset<0){offset=-offset;sign="-"}return sign+zeroFill(~~(offset/60),2)+separator+zeroFill(~~offset%60,2)})}offset("Z",":");offset("ZZ","");addRegexToken("Z",matchShortOffset);addRegexToken("ZZ",matchShortOffset);addParseToken(["Z","ZZ"],function(input,array,config){config._useUTC=true;config._tzm=offsetFromString(matchShortOffset,input)});var chunkOffset=/([\+\-]|\d\d)/gi;function offsetFromString(matcher,string){var matches=(string||"").match(matcher),chunk,parts,minutes;if(matches===null){return null}chunk=matches[matches.length-1]||[];parts=(chunk+"").match(chunkOffset)||["-",0,0];minutes=+(parts[1]*60)+toInt(parts[2]);return minutes===0?0:parts[0]==="+"?minutes:-minutes}function cloneWithOffset(input,model){var res,diff;if(model._isUTC){res=model.clone();diff=(isMoment(input)||isDate(input)?input.valueOf():createLocal(input).valueOf())-res.valueOf();res._d.setTime(res._d.valueOf()+diff);hooks.updateOffset(res,false);return res}else{return createLocal(input).local()}}function getDateOffset(m){return-Math.round(m._d.getTimezoneOffset())}hooks.updateOffset=function(){};function getSetOffset(input,keepLocalTime,keepMinutes){var offset=this._offset||0,localAdjust;if(!this.isValid()){return input!=null?this:NaN}if(input!=null){if(typeof input==="string"){input=offsetFromString(matchShortOffset,input);if(input===null){return this}}else if(Math.abs(input)<16&&!keepMinutes){input=input*60}if(!this._isUTC&&keepLocalTime){localAdjust=getDateOffset(this)}this._offset=input;this._isUTC=true;if(localAdjust!=null){this.add(localAdjust,"m")}if(offset!==input){if(!keepLocalTime||this._changeInProgress){addSubtract(this,createDuration(input-offset,"m"),1,false)}else if(!this._changeInProgress){this._changeInProgress=true;hooks.updateOffset(this,true);this._changeInProgress=null}}return this}else{return this._isUTC?offset:getDateOffset(this)}}function getSetZone(input,keepLocalTime){if(input!=null){if(typeof input!=="string"){input=-input}this.utcOffset(input,keepLocalTime);return this}else{return-this.utcOffset()}}function setOffsetToUTC(keepLocalTime){return this.utcOffset(0,keepLocalTime)}function setOffsetToLocal(keepLocalTime){if(this._isUTC){this.utcOffset(0,keepLocalTime);this._isUTC=false;if(keepLocalTime){this.subtract(getDateOffset(this),"m")}}return this}function setOffsetToParsedOffset(){if(this._tzm!=null){this.utcOffset(this._tzm,false,true)}else if(typeof this._i==="string"){var tZone=offsetFromString(matchOffset,this._i);if(tZone!=null){this.utcOffset(tZone)}else{this.utcOffset(0,true)}}return this}function hasAlignedHourOffset(input){if(!this.isValid()){return false}input=input?createLocal(input).utcOffset():0;return(this.utcOffset()-input)%60===0}function isDaylightSavingTime(){return this.utcOffset()>this.clone().month(0).utcOffset()||this.utcOffset()>this.clone().month(5).utcOffset()}function isDaylightSavingTimeShifted(){if(!isUndefined(this._isDSTShifted)){return this._isDSTShifted}var c={},other;copyConfig(c,this);c=prepareConfig(c);if(c._a){other=c._isUTC?createUTC(c._a):createLocal(c._a);this._isDSTShifted=this.isValid()&&compareArrays(c._a,other.toArray())>0}else{this._isDSTShifted=false}return this._isDSTShifted}function isLocal(){return this.isValid()?!this._isUTC:false}function isUtcOffset(){return this.isValid()?this._isUTC:false}function isUtc(){return this.isValid()?this._isUTC&&this._offset===0:false}var aspNetRegex=/^(-|\+)?(?:(\d*)[. ])?(\d+):(\d+)(?::(\d+)(\.\d*)?)?$/,isoRegex=/^(-|\+)?P(?:([-+]?[0-9,.]*)Y)?(?:([-+]?[0-9,.]*)M)?(?:([-+]?[0-9,.]*)W)?(?:([-+]?[0-9,.]*)D)?(?:T(?:([-+]?[0-9,.]*)H)?(?:([-+]?[0-9,.]*)M)?(?:([-+]?[0-9,.]*)S)?)?$/;function createDuration(input,key){var duration=input,match=null,sign,ret,diffRes;if(isDuration(input)){duration={ms:input._milliseconds,d:input._days,M:input._months}}else if(isNumber(input)||!isNaN(+input)){duration={};if(key){duration[key]=+input}else{duration.milliseconds=+input}}else if(match=aspNetRegex.exec(input)){sign=match[1]==="-"?-1:1;duration={y:0,d:toInt(match[DATE])*sign,h:toInt(match[HOUR])*sign,m:toInt(match[MINUTE])*sign,s:toInt(match[SECOND])*sign,ms:toInt(absRound(match[MILLISECOND]*1e3))*sign}}else if(match=isoRegex.exec(input)){sign=match[1]==="-"?-1:1;duration={y:parseIso(match[2],sign),M:parseIso(match[3],sign),w:parseIso(match[4],sign),d:parseIso(match[5],sign),h:parseIso(match[6],sign),m:parseIso(match[7],sign),s:parseIso(match[8],sign)}}else if(duration==null){duration={}}else if(typeof duration==="object"&&("from"in duration||"to"in duration)){diffRes=momentsDifference(createLocal(duration.from),createLocal(duration.to));duration={};duration.ms=diffRes.milliseconds;duration.M=diffRes.months}ret=new Duration(duration);if(isDuration(input)&&hasOwnProp(input,"_locale")){ret._locale=input._locale}if(isDuration(input)&&hasOwnProp(input,"_isValid")){ret._isValid=input._isValid}return ret}createDuration.fn=Duration.prototype;createDuration.invalid=createInvalid$1;function parseIso(inp,sign){var res=inp&&parseFloat(inp.replace(",","."));return(isNaN(res)?0:res)*sign}function positiveMomentsDifference(base,other){var res={};res.months=other.month()-base.month()+(other.year()-base.year())*12;if(base.clone().add(res.months,"M").isAfter(other)){--res.months}res.milliseconds=+other-+base.clone().add(res.months,"M");return res}function momentsDifference(base,other){var res;if(!(base.isValid()&&other.isValid())){return{milliseconds:0,months:0}}other=cloneWithOffset(other,base);if(base.isBefore(other)){res=positiveMomentsDifference(base,other)}else{res=positiveMomentsDifference(other,base);res.milliseconds=-res.milliseconds;res.months=-res.months}return res}function createAdder(direction,name){return function(val,period){var dur,tmp;if(period!==null&&!isNaN(+period)){deprecateSimple(name,"moment()."+name+"(period, number) is deprecated. Please use moment()."+name+"(number, period). "+"See http://momentjs.com/guides/#/warnings/add-inverted-param/ for more info.");tmp=val;val=period;period=tmp}dur=createDuration(val,period);addSubtract(this,dur,direction);return this}}function addSubtract(mom,duration,isAdding,updateOffset){var milliseconds=duration._milliseconds,days=absRound(duration._days),months=absRound(duration._months);if(!mom.isValid()){return}updateOffset=updateOffset==null?true:updateOffset;if(months){setMonth(mom,get(mom,"Month")+months*isAdding)}if(days){set$1(mom,"Date",get(mom,"Date")+days*isAdding)}if(milliseconds){mom._d.setTime(mom._d.valueOf()+milliseconds*isAdding)}if(updateOffset){hooks.updateOffset(mom,days||months)}}var add=createAdder(1,"add"),subtract=createAdder(-1,"subtract");function isString(input){return typeof input==="string"||input instanceof String}function isMomentInput(input){return isMoment(input)||isDate(input)||isString(input)||isNumber(input)||isNumberOrStringArray(input)||isMomentInputObject(input)||input===null||input===undefined}function isMomentInputObject(input){var objectTest=isObject(input)&&!isObjectEmpty(input),propertyTest=false,properties=["years","year","y","months","month","M","days","day","d","dates","date","D","hours","hour","h","minutes","minute","m","seconds","second","s","milliseconds","millisecond","ms"],i,property;for(i=0;i<properties.length;i+=1){property=properties[i];propertyTest=propertyTest||hasOwnProp(input,property)}return objectTest&&propertyTest}function isNumberOrStringArray(input){var arrayTest=isArray(input),dataTypeTest=false;if(arrayTest){dataTypeTest=input.filter(function(item){return!isNumber(item)&&isString(input)}).length===0}return arrayTest&&dataTypeTest}function isCalendarSpec(input){var objectTest=isObject(input)&&!isObjectEmpty(input),propertyTest=false,properties=["sameDay","nextDay","lastDay","nextWeek","lastWeek","sameElse"],i,property;for(i=0;i<properties.length;i+=1){property=properties[i];propertyTest=propertyTest||hasOwnProp(input,property)}return objectTest&&propertyTest}function getCalendarFormat(myMoment,now){var diff=myMoment.diff(now,"days",true);return diff<-6?"sameElse":diff<-1?"lastWeek":diff<0?"lastDay":diff<1?"sameDay":diff<2?"nextDay":diff<7?"nextWeek":"sameElse"}function calendar$1(time,formats){if(arguments.length===1){if(!arguments[0]){time=undefined;formats=undefined}else if(isMomentInput(arguments[0])){time=arguments[0];formats=undefined}else if(isCalendarSpec(arguments[0])){formats=arguments[0];time=undefined}}var now=time||createLocal(),sod=cloneWithOffset(now,this).startOf("day"),format=hooks.calendarFormat(this,sod)||"sameElse",output=formats&&(isFunction(formats[format])?formats[format].call(this,now):formats[format]);return this.format(output||this.localeData().calendar(format,this,createLocal(now)))}function clone(){return new Moment(this)}function isAfter(input,units){var localInput=isMoment(input)?input:createLocal(input);if(!(this.isValid()&&localInput.isValid())){return false}units=normalizeUnits(units)||"millisecond";if(units==="millisecond"){return this.valueOf()>localInput.valueOf()}else{return localInput.valueOf()<this.clone().startOf(units).valueOf()}}function isBefore(input,units){var localInput=isMoment(input)?input:createLocal(input);if(!(this.isValid()&&localInput.isValid())){return false}units=normalizeUnits(units)||"millisecond";if(units==="millisecond"){return this.valueOf()<localInput.valueOf()}else{return this.clone().endOf(units).valueOf()<localInput.valueOf()}}function isBetween(from,to,units,inclusivity){var localFrom=isMoment(from)?from:createLocal(from),localTo=isMoment(to)?to:createLocal(to);if(!(this.isValid()&&localFrom.isValid()&&localTo.isValid())){return false}inclusivity=inclusivity||"()";return(inclusivity[0]==="("?this.isAfter(localFrom,units):!this.isBefore(localFrom,units))&&(inclusivity[1]===")"?this.isBefore(localTo,units):!this.isAfter(localTo,units))}function isSame(input,units){var localInput=isMoment(input)?input:createLocal(input),inputMs;if(!(this.isValid()&&localInput.isValid())){return false}units=normalizeUnits(units)||"millisecond";if(units==="millisecond"){return this.valueOf()===localInput.valueOf()}else{inputMs=localInput.valueOf();return this.clone().startOf(units).valueOf()<=inputMs&&inputMs<=this.clone().endOf(units).valueOf()}}function isSameOrAfter(input,units){return this.isSame(input,units)||this.isAfter(input,units)}function isSameOrBefore(input,units){return this.isSame(input,units)||this.isBefore(input,units)}function diff(input,units,asFloat){var that,zoneDelta,output;if(!this.isValid()){return NaN}that=cloneWithOffset(input,this);if(!that.isValid()){return NaN}zoneDelta=(that.utcOffset()-this.utcOffset())*6e4;units=normalizeUnits(units);switch(units){case"year":output=monthDiff(this,that)/12;break;case"month":output=monthDiff(this,that);break;case"quarter":output=monthDiff(this,that)/3;break;case"second":output=(this-that)/1e3;break;case"minute":output=(this-that)/6e4;break;case"hour":output=(this-that)/36e5;break;case"day":output=(this-that-zoneDelta)/864e5;break;case"week":output=(this-that-zoneDelta)/6048e5;break;default:output=this-that}return asFloat?output:absFloor(output)}function monthDiff(a,b){if(a.date()<b.date()){return-monthDiff(b,a)}var wholeMonthDiff=(b.year()-a.year())*12+(b.month()-a.month()),anchor=a.clone().add(wholeMonthDiff,"months"),anchor2,adjust;if(b-anchor<0){anchor2=a.clone().add(wholeMonthDiff-1,"months");adjust=(b-anchor)/(anchor-anchor2)}else{anchor2=a.clone().add(wholeMonthDiff+1,"months");adjust=(b-anchor)/(anchor2-anchor)}return-(wholeMonthDiff+adjust)||0}hooks.defaultFormat="YYYY-MM-DDTHH:mm:ssZ";hooks.defaultFormatUtc="YYYY-MM-DDTHH:mm:ss[Z]";function toString(){return this.clone().locale("en").format("ddd MMM DD YYYY HH:mm:ss [GMT]ZZ")}function toISOString(keepOffset){if(!this.isValid()){return null}var utc=keepOffset!==true,m=utc?this.clone().utc():this;if(m.year()<0||m.year()>9999){return formatMoment(m,utc?"YYYYYY-MM-DD[T]HH:mm:ss.SSS[Z]":"YYYYYY-MM-DD[T]HH:mm:ss.SSSZ")}if(isFunction(Date.prototype.toISOString)){if(utc){return this.toDate().toISOString()}else{return new Date(this.valueOf()+this.utcOffset()*60*1e3).toISOString().replace("Z",formatMoment(m,"Z"))}}return formatMoment(m,utc?"YYYY-MM-DD[T]HH:mm:ss.SSS[Z]":"YYYY-MM-DD[T]HH:mm:ss.SSSZ")}function inspect(){if(!this.isValid()){return"moment.invalid(/* "+this._i+" */)"}var func="moment",zone="",prefix,year,datetime,suffix;if(!this.isLocal()){func=this.utcOffset()===0?"moment.utc":"moment.parseZone";zone="Z"}prefix="["+func+'("]';year=0<=this.year()&&this.year()<=9999?"YYYY":"YYYYYY";datetime="-MM-DD[T]HH:mm:ss.SSS";suffix=zone+'[")]';return this.format(prefix+year+datetime+suffix)}function format(inputString){if(!inputString){inputString=this.isUtc()?hooks.defaultFormatUtc:hooks.defaultFormat}var output=formatMoment(this,inputString);return this.localeData().postformat(output)}function from(time,withoutSuffix){if(this.isValid()&&(isMoment(time)&&time.isValid()||createLocal(time).isValid())){return createDuration({to:this,from:time}).locale(this.locale()).humanize(!withoutSuffix)}else{return this.localeData().invalidDate()}}function fromNow(withoutSuffix){return this.from(createLocal(),withoutSuffix)}function to(time,withoutSuffix){if(this.isValid()&&(isMoment(time)&&time.isValid()||createLocal(time).isValid())){return createDuration({from:this,to:time}).locale(this.locale()).humanize(!withoutSuffix)}else{return this.localeData().invalidDate()}}function toNow(withoutSuffix){return this.to(createLocal(),withoutSuffix)}function locale(key){var newLocaleData;if(key===undefined){return this._locale._abbr}else{newLocaleData=getLocale(key);if(newLocaleData!=null){this._locale=newLocaleData}return this}}var lang=deprecate("moment().lang() is deprecated. Instead, use moment().localeData() to get the language configuration. Use moment().locale() to change languages.",function(key){if(key===undefined){return this.localeData()}else{return this.locale(key)}});function localeData(){return this._locale}var MS_PER_SECOND=1e3,MS_PER_MINUTE=60*MS_PER_SECOND,MS_PER_HOUR=60*MS_PER_MINUTE,MS_PER_400_YEARS=(365*400+97)*24*MS_PER_HOUR;function mod$1(dividend,divisor){return(dividend%divisor+divisor)%divisor}function localStartOfDate(y,m,d){if(y<100&&y>=0){return new Date(y+400,m,d)-MS_PER_400_YEARS}else{return new Date(y,m,d).valueOf()}}function utcStartOfDate(y,m,d){if(y<100&&y>=0){return Date.UTC(y+400,m,d)-MS_PER_400_YEARS}else{return Date.UTC(y,m,d)}}function startOf(units){var time,startOfDate;units=normalizeUnits(units);if(units===undefined||units==="millisecond"||!this.isValid()){return this}startOfDate=this._isUTC?utcStartOfDate:localStartOfDate;switch(units){case"year":time=startOfDate(this.year(),0,1);break;case"quarter":time=startOfDate(this.year(),this.month()-this.month()%3,1);break;case"month":time=startOfDate(this.year(),this.month(),1);break;case"week":time=startOfDate(this.year(),this.month(),this.date()-this.weekday());break;case"isoWeek":time=startOfDate(this.year(),this.month(),this.date()-(this.isoWeekday()-1));break;case"day":case"date":time=startOfDate(this.year(),this.month(),this.date());break;case"hour":time=this._d.valueOf();time-=mod$1(time+(this._isUTC?0:this.utcOffset()*MS_PER_MINUTE),MS_PER_HOUR);break;case"minute":time=this._d.valueOf();time-=mod$1(time,MS_PER_MINUTE);break;case"second":time=this._d.valueOf();time-=mod$1(time,MS_PER_SECOND);break}this._d.setTime(time);hooks.updateOffset(this,true);return this}function endOf(units){var time,startOfDate;units=normalizeUnits(units);if(units===undefined||units==="millisecond"||!this.isValid()){return this}startOfDate=this._isUTC?utcStartOfDate:localStartOfDate;switch(units){case"year":time=startOfDate(this.year()+1,0,1)-1;break;case"quarter":time=startOfDate(this.year(),this.month()-this.month()%3+3,1)-1;break;case"month":time=startOfDate(this.year(),this.month()+1,1)-1;break;case"week":time=startOfDate(this.year(),this.month(),this.date()-this.weekday()+7)-1;break;case"isoWeek":time=startOfDate(this.year(),this.month(),this.date()-(this.isoWeekday()-1)+7)-1;break;case"day":case"date":time=startOfDate(this.year(),this.month(),this.date()+1)-1;break;case"hour":time=this._d.valueOf();time+=MS_PER_HOUR-mod$1(time+(this._isUTC?0:this.utcOffset()*MS_PER_MINUTE),MS_PER_HOUR)-1;break;case"minute":time=this._d.valueOf();time+=MS_PER_MINUTE-mod$1(time,MS_PER_MINUTE)-1;break;case"second":time=this._d.valueOf();time+=MS_PER_SECOND-mod$1(time,MS_PER_SECOND)-1;break}this._d.setTime(time);hooks.updateOffset(this,true);return this}function valueOf(){return this._d.valueOf()-(this._offset||0)*6e4}function unix(){return Math.floor(this.valueOf()/1e3)}function toDate(){return new Date(this.valueOf())}function toArray(){var m=this;return[m.year(),m.month(),m.date(),m.hour(),m.minute(),m.second(),m.millisecond()]}function toObject(){var m=this;return{years:m.year(),months:m.month(),date:m.date(),hours:m.hours(),minutes:m.minutes(),seconds:m.seconds(),milliseconds:m.milliseconds()}}function toJSON(){return this.isValid()?this.toISOString():null}function isValid$2(){return isValid(this)}function parsingFlags(){return extend({},getParsingFlags(this))}function invalidAt(){return getParsingFlags(this).overflow}function creationData(){return{input:this._i,format:this._f,locale:this._locale,isUTC:this._isUTC,strict:this._strict}}addFormatToken("N",0,0,"eraAbbr");addFormatToken("NN",0,0,"eraAbbr");addFormatToken("NNN",0,0,"eraAbbr");addFormatToken("NNNN",0,0,"eraName");addFormatToken("NNNNN",0,0,"eraNarrow");addFormatToken("y",["y",1],"yo","eraYear");addFormatToken("y",["yy",2],0,"eraYear");addFormatToken("y",["yyy",3],0,"eraYear");addFormatToken("y",["yyyy",4],0,"eraYear");addRegexToken("N",matchEraAbbr);addRegexToken("NN",matchEraAbbr);addRegexToken("NNN",matchEraAbbr);addRegexToken("NNNN",matchEraName);addRegexToken("NNNNN",matchEraNarrow);addParseToken(["N","NN","NNN","NNNN","NNNNN"],function(input,array,config,token){var era=config._locale.erasParse(input,token,config._strict);if(era){getParsingFlags(config).era=era}else{getParsingFlags(config).invalidEra=input}});addRegexToken("y",matchUnsigned);addRegexToken("yy",matchUnsigned);addRegexToken("yyy",matchUnsigned);addRegexToken("yyyy",matchUnsigned);addRegexToken("yo",matchEraYearOrdinal);addParseToken(["y","yy","yyy","yyyy"],YEAR);addParseToken(["yo"],function(input,array,config,token){var match;if(config._locale._eraYearOrdinalRegex){match=input.match(config._locale._eraYearOrdinalRegex)}if(config._locale.eraYearOrdinalParse){array[YEAR]=config._locale.eraYearOrdinalParse(input,match)}else{array[YEAR]=parseInt(input,10)}});function localeEras(m,format){var i,l,date,eras=this._eras||getLocale("en")._eras;for(i=0,l=eras.length;i<l;++i){switch(typeof eras[i].since){case"string":date=hooks(eras[i].since).startOf("day");eras[i].since=date.valueOf();break}switch(typeof eras[i].until){case"undefined":eras[i].until=+Infinity;break;case"string":date=hooks(eras[i].until).startOf("day").valueOf();eras[i].until=date.valueOf();break}}return eras}function localeErasParse(eraName,format,strict){var i,l,eras=this.eras(),name,abbr,narrow;eraName=eraName.toUpperCase();for(i=0,l=eras.length;i<l;++i){name=eras[i].name.toUpperCase();abbr=eras[i].abbr.toUpperCase();narrow=eras[i].narrow.toUpperCase();if(strict){switch(format){case"N":case"NN":case"NNN":if(abbr===eraName){return eras[i]}break;case"NNNN":if(name===eraName){return eras[i]}break;case"NNNNN":if(narrow===eraName){return eras[i]}break}}else if([name,abbr,narrow].indexOf(eraName)>=0){return eras[i]}}}function localeErasConvertYear(era,year){var dir=era.since<=era.until?+1:-1;if(year===undefined){return hooks(era.since).year()}else{return hooks(era.since).year()+(year-era.offset)*dir}}function getEraName(){var i,l,val,eras=this.localeData().eras();for(i=0,l=eras.length;i<l;++i){val=this.clone().startOf("day").valueOf();if(eras[i].since<=val&&val<=eras[i].until){return eras[i].name}if(eras[i].until<=val&&val<=eras[i].since){return eras[i].name}}return""}function getEraNarrow(){var i,l,val,eras=this.localeData().eras();for(i=0,l=eras.length;i<l;++i){val=this.clone().startOf("day").valueOf();if(eras[i].since<=val&&val<=eras[i].until){return eras[i].narrow}if(eras[i].until<=val&&val<=eras[i].since){return eras[i].narrow}}return""}function getEraAbbr(){var i,l,val,eras=this.localeData().eras();for(i=0,l=eras.length;i<l;++i){val=this.clone().startOf("day").valueOf();if(eras[i].since<=val&&val<=eras[i].until){return eras[i].abbr}if(eras[i].until<=val&&val<=eras[i].since){return eras[i].abbr}}return""}function getEraYear(){var i,l,dir,val,eras=this.localeData().eras();for(i=0,l=eras.length;i<l;++i){dir=eras[i].since<=eras[i].until?+1:-1;val=this.clone().startOf("day").valueOf();if(eras[i].since<=val&&val<=eras[i].until||eras[i].until<=val&&val<=eras[i].since){return(this.year()-hooks(eras[i].since).year())*dir+eras[i].offset}}return this.year()}function erasNameRegex(isStrict){if(!hasOwnProp(this,"_erasNameRegex")){computeErasParse.call(this)}return isStrict?this._erasNameRegex:this._erasRegex}function erasAbbrRegex(isStrict){if(!hasOwnProp(this,"_erasAbbrRegex")){computeErasParse.call(this)}return isStrict?this._erasAbbrRegex:this._erasRegex}function erasNarrowRegex(isStrict){if(!hasOwnProp(this,"_erasNarrowRegex")){computeErasParse.call(this)}return isStrict?this._erasNarrowRegex:this._erasRegex}function matchEraAbbr(isStrict,locale){return locale.erasAbbrRegex(isStrict)}function matchEraName(isStrict,locale){return locale.erasNameRegex(isStrict)}function matchEraNarrow(isStrict,locale){return locale.erasNarrowRegex(isStrict)}function matchEraYearOrdinal(isStrict,locale){return locale._eraYearOrdinalRegex||matchUnsigned}function computeErasParse(){var abbrPieces=[],namePieces=[],narrowPieces=[],mixedPieces=[],i,l,eras=this.eras();for(i=0,l=eras.length;i<l;++i){namePieces.push(regexEscape(eras[i].name));abbrPieces.push(regexEscape(eras[i].abbr));narrowPieces.push(regexEscape(eras[i].narrow));mixedPieces.push(regexEscape(eras[i].name));mixedPieces.push(regexEscape(eras[i].abbr));mixedPieces.push(regexEscape(eras[i].narrow))}this._erasRegex=new RegExp("^("+mixedPieces.join("|")+")","i");this._erasNameRegex=new RegExp("^("+namePieces.join("|")+")","i");this._erasAbbrRegex=new RegExp("^("+abbrPieces.join("|")+")","i");this._erasNarrowRegex=new RegExp("^("+narrowPieces.join("|")+")","i")}addFormatToken(0,["gg",2],0,function(){return this.weekYear()%100});addFormatToken(0,["GG",2],0,function(){return this.isoWeekYear()%100});function addWeekYearFormatToken(token,getter){addFormatToken(0,[token,token.length],0,getter)}addWeekYearFormatToken("gggg","weekYear");addWeekYearFormatToken("ggggg","weekYear");addWeekYearFormatToken("GGGG","isoWeekYear");addWeekYearFormatToken("GGGGG","isoWeekYear");addUnitAlias("weekYear","gg");addUnitAlias("isoWeekYear","GG");addUnitPriority("weekYear",1);addUnitPriority("isoWeekYear",1);addRegexToken("G",matchSigned);addRegexToken("g",matchSigned);addRegexToken("GG",match1to2,match2);addRegexToken("gg",match1to2,match2);addRegexToken("GGGG",match1to4,match4);addRegexToken("gggg",match1to4,match4);addRegexToken("GGGGG",match1to6,match6);addRegexToken("ggggg",match1to6,match6);addWeekParseToken(["gggg","ggggg","GGGG","GGGGG"],function(input,week,config,token){week[token.substr(0,2)]=toInt(input)});addWeekParseToken(["gg","GG"],function(input,week,config,token){week[token]=hooks.parseTwoDigitYear(input)});function getSetWeekYear(input){return getSetWeekYearHelper.call(this,input,this.week(),this.weekday(),this.localeData()._week.dow,this.localeData()._week.doy)}function getSetISOWeekYear(input){return getSetWeekYearHelper.call(this,input,this.isoWeek(),this.isoWeekday(),1,4)}function getISOWeeksInYear(){return weeksInYear(this.year(),1,4)}function getISOWeeksInISOWeekYear(){return weeksInYear(this.isoWeekYear(),1,4)}function getWeeksInYear(){var weekInfo=this.localeData()._week;return weeksInYear(this.year(),weekInfo.dow,weekInfo.doy)}function getWeeksInWeekYear(){var weekInfo=this.localeData()._week;return weeksInYear(this.weekYear(),weekInfo.dow,weekInfo.doy)}function getSetWeekYearHelper(input,week,weekday,dow,doy){var weeksTarget;if(input==null){return weekOfYear(this,dow,doy).year}else{weeksTarget=weeksInYear(input,dow,doy);if(week>weeksTarget){week=weeksTarget}return setWeekAll.call(this,input,week,weekday,dow,doy)}}function setWeekAll(weekYear,week,weekday,dow,doy){var dayOfYearData=dayOfYearFromWeeks(weekYear,week,weekday,dow,doy),date=createUTCDate(dayOfYearData.year,0,dayOfYearData.dayOfYear);this.year(date.getUTCFullYear());this.month(date.getUTCMonth());this.date(date.getUTCDate());return this}addFormatToken("Q",0,"Qo","quarter");addUnitAlias("quarter","Q");addUnitPriority("quarter",7);addRegexToken("Q",match1);addParseToken("Q",function(input,array){array[MONTH]=(toInt(input)-1)*3});function getSetQuarter(input){return input==null?Math.ceil((this.month()+1)/3):this.month((input-1)*3+this.month()%3)}addFormatToken("D",["DD",2],"Do","date");addUnitAlias("date","D");addUnitPriority("date",9);addRegexToken("D",match1to2);addRegexToken("DD",match1to2,match2);addRegexToken("Do",function(isStrict,locale){return isStrict?locale._dayOfMonthOrdinalParse||locale._ordinalParse:locale._dayOfMonthOrdinalParseLenient});addParseToken(["D","DD"],DATE);addParseToken("Do",function(input,array){array[DATE]=toInt(input.match(match1to2)[0])});var getSetDayOfMonth=makeGetSet("Date",true);addFormatToken("DDD",["DDDD",3],"DDDo","dayOfYear");addUnitAlias("dayOfYear","DDD");addUnitPriority("dayOfYear",4);addRegexToken("DDD",match1to3);addRegexToken("DDDD",match3);addParseToken(["DDD","DDDD"],function(input,array,config){config._dayOfYear=toInt(input)});function getSetDayOfYear(input){var dayOfYear=Math.round((this.clone().startOf("day")-this.clone().startOf("year"))/864e5)+1;return input==null?dayOfYear:this.add(input-dayOfYear,"d")}addFormatToken("m",["mm",2],0,"minute");addUnitAlias("minute","m");addUnitPriority("minute",14);addRegexToken("m",match1to2);addRegexToken("mm",match1to2,match2);addParseToken(["m","mm"],MINUTE);var getSetMinute=makeGetSet("Minutes",false);addFormatToken("s",["ss",2],0,"second");addUnitAlias("second","s");addUnitPriority("second",15);addRegexToken("s",match1to2);addRegexToken("ss",match1to2,match2);addParseToken(["s","ss"],SECOND);var getSetSecond=makeGetSet("Seconds",false);addFormatToken("S",0,0,function(){return~~(this.millisecond()/100)});addFormatToken(0,["SS",2],0,function(){return~~(this.millisecond()/10)});addFormatToken(0,["SSS",3],0,"millisecond");addFormatToken(0,["SSSS",4],0,function(){return this.millisecond()*10});addFormatToken(0,["SSSSS",5],0,function(){return this.millisecond()*100});addFormatToken(0,["SSSSSS",6],0,function(){return this.millisecond()*1e3});addFormatToken(0,["SSSSSSS",7],0,function(){return this.millisecond()*1e4});addFormatToken(0,["SSSSSSSS",8],0,function(){return this.millisecond()*1e5});addFormatToken(0,["SSSSSSSSS",9],0,function(){return this.millisecond()*1e6});addUnitAlias("millisecond","ms");addUnitPriority("millisecond",16);addRegexToken("S",match1to3,match1);addRegexToken("SS",match1to3,match2);addRegexToken("SSS",match1to3,match3);var token,getSetMillisecond;for(token="SSSS";token.length<=9;token+="S"){addRegexToken(token,matchUnsigned)}function parseMs(input,array){array[MILLISECOND]=toInt(("0."+input)*1e3)}for(token="S";token.length<=9;token+="S"){addParseToken(token,parseMs)}getSetMillisecond=makeGetSet("Milliseconds",false);addFormatToken("z",0,0,"zoneAbbr");addFormatToken("zz",0,0,"zoneName");function getZoneAbbr(){return this._isUTC?"UTC":""}function getZoneName(){return this._isUTC?"Coordinated Universal Time":""}var proto=Moment.prototype;proto.add=add;proto.calendar=calendar$1;proto.clone=clone;proto.diff=diff;proto.endOf=endOf;proto.format=format;proto.from=from;proto.fromNow=fromNow;proto.to=to;proto.toNow=toNow;proto.get=stringGet;proto.invalidAt=invalidAt;proto.isAfter=isAfter;proto.isBefore=isBefore;proto.isBetween=isBetween;proto.isSame=isSame;proto.isSameOrAfter=isSameOrAfter;proto.isSameOrBefore=isSameOrBefore;proto.isValid=isValid$2;proto.lang=lang;proto.locale=locale;proto.localeData=localeData;proto.max=prototypeMax;proto.min=prototypeMin;proto.parsingFlags=parsingFlags;proto.set=stringSet;proto.startOf=startOf;proto.subtract=subtract;proto.toArray=toArray;proto.toObject=toObject;proto.toDate=toDate;proto.toISOString=toISOString;proto.inspect=inspect;if(typeof Symbol!=="undefined"&&Symbol.for!=null){proto[Symbol.for("nodejs.util.inspect.custom")]=function(){return"Moment<"+this.format()+">"}}proto.toJSON=toJSON;proto.toString=toString;proto.unix=unix;proto.valueOf=valueOf;proto.creationData=creationData;proto.eraName=getEraName;proto.eraNarrow=getEraNarrow;proto.eraAbbr=getEraAbbr;proto.eraYear=getEraYear;proto.year=getSetYear;proto.isLeapYear=getIsLeapYear;proto.weekYear=getSetWeekYear;proto.isoWeekYear=getSetISOWeekYear;proto.quarter=proto.quarters=getSetQuarter;proto.month=getSetMonth;proto.daysInMonth=getDaysInMonth;proto.week=proto.weeks=getSetWeek;proto.isoWeek=proto.isoWeeks=getSetISOWeek;proto.weeksInYear=getWeeksInYear;proto.weeksInWeekYear=getWeeksInWeekYear;proto.isoWeeksInYear=getISOWeeksInYear;proto.isoWeeksInISOWeekYear=getISOWeeksInISOWeekYear;proto.date=getSetDayOfMonth;proto.day=proto.days=getSetDayOfWeek;proto.weekday=getSetLocaleDayOfWeek;proto.isoWeekday=getSetISODayOfWeek;proto.dayOfYear=getSetDayOfYear;proto.hour=proto.hours=getSetHour;proto.minute=proto.minutes=getSetMinute;proto.second=proto.seconds=getSetSecond;proto.millisecond=proto.milliseconds=getSetMillisecond;proto.utcOffset=getSetOffset;proto.utc=setOffsetToUTC;proto.local=setOffsetToLocal;proto.parseZone=setOffsetToParsedOffset;proto.hasAlignedHourOffset=hasAlignedHourOffset;proto.isDST=isDaylightSavingTime;proto.isLocal=isLocal;proto.isUtcOffset=isUtcOffset;proto.isUtc=isUtc;proto.isUTC=isUtc;proto.zoneAbbr=getZoneAbbr;proto.zoneName=getZoneName;proto.dates=deprecate("dates accessor is deprecated. Use date instead.",getSetDayOfMonth);proto.months=deprecate("months accessor is deprecated. Use month instead",getSetMonth);proto.years=deprecate("years accessor is deprecated. Use year instead",getSetYear);proto.zone=deprecate("moment().zone is deprecated, use moment().utcOffset instead. http://momentjs.com/guides/#/warnings/zone/",getSetZone);proto.isDSTShifted=deprecate("isDSTShifted is deprecated. See http://momentjs.com/guides/#/warnings/dst-shifted/ for more information",isDaylightSavingTimeShifted);function createUnix(input){return createLocal(input*1e3)}function createInZone(){return createLocal.apply(null,arguments).parseZone()}function preParsePostFormat(string){return string}var proto$1=Locale.prototype;proto$1.calendar=calendar;proto$1.longDateFormat=longDateFormat;proto$1.invalidDate=invalidDate;proto$1.ordinal=ordinal;proto$1.preparse=preParsePostFormat;proto$1.postformat=preParsePostFormat;proto$1.relativeTime=relativeTime;proto$1.pastFuture=pastFuture;proto$1.set=set;proto$1.eras=localeEras;proto$1.erasParse=localeErasParse;proto$1.erasConvertYear=localeErasConvertYear;proto$1.erasAbbrRegex=erasAbbrRegex;proto$1.erasNameRegex=erasNameRegex;proto$1.erasNarrowRegex=erasNarrowRegex;proto$1.months=localeMonths;proto$1.monthsShort=localeMonthsShort;proto$1.monthsParse=localeMonthsParse;proto$1.monthsRegex=monthsRegex;proto$1.monthsShortRegex=monthsShortRegex;proto$1.week=localeWeek;proto$1.firstDayOfYear=localeFirstDayOfYear;proto$1.firstDayOfWeek=localeFirstDayOfWeek;proto$1.weekdays=localeWeekdays;proto$1.weekdaysMin=localeWeekdaysMin;proto$1.weekdaysShort=localeWeekdaysShort;proto$1.weekdaysParse=localeWeekdaysParse;proto$1.weekdaysRegex=weekdaysRegex;proto$1.weekdaysShortRegex=weekdaysShortRegex;proto$1.weekdaysMinRegex=weekdaysMinRegex;proto$1.isPM=localeIsPM;proto$1.meridiem=localeMeridiem;function get$1(format,index,field,setter){var locale=getLocale(),utc=createUTC().set(setter,index);return locale[field](utc,format)}function listMonthsImpl(format,index,field){if(isNumber(format)){index=format;format=undefined}format=format||"";if(index!=null){return get$1(format,index,field,"month")}var i,out=[];for(i=0;i<12;i++){out[i]=get$1(format,i,field,"month")}return out}function listWeekdaysImpl(localeSorted,format,index,field){if(typeof localeSorted==="boolean"){if(isNumber(format)){index=format;format=undefined}format=format||""}else{format=localeSorted;index=format;localeSorted=false;if(isNumber(format)){index=format;format=undefined}format=format||""}var locale=getLocale(),shift=localeSorted?locale._week.dow:0,i,out=[];if(index!=null){return get$1(format,(index+shift)%7,field,"day")}for(i=0;i<7;i++){out[i]=get$1(format,(i+shift)%7,field,"day")}return out}function listMonths(format,index){return listMonthsImpl(format,index,"months")}function listMonthsShort(format,index){return listMonthsImpl(format,index,"monthsShort")}function listWeekdays(localeSorted,format,index){return listWeekdaysImpl(localeSorted,format,index,"weekdays")}function listWeekdaysShort(localeSorted,format,index){return listWeekdaysImpl(localeSorted,format,index,"weekdaysShort")}function listWeekdaysMin(localeSorted,format,index){return listWeekdaysImpl(localeSorted,format,index,"weekdaysMin")}getSetGlobalLocale("en",{eras:[{since:"0001-01-01",until:+Infinity,offset:1,name:"Anno Domini",narrow:"AD",abbr:"AD"},{since:"0000-12-31",until:-Infinity,offset:1,name:"Before Christ",narrow:"BC",abbr:"BC"}],dayOfMonthOrdinalParse:/\d{1,2}(th|st|nd|rd)/,ordinal:function(number){var b=number%10,output=toInt(number%100/10)===1?"th":b===1?"st":b===2?"nd":b===3?"rd":"th";return number+output}});hooks.lang=deprecate("moment.lang is deprecated. Use moment.locale instead.",getSetGlobalLocale);hooks.langData=deprecate("moment.langData is deprecated. Use moment.localeData instead.",getLocale);var mathAbs=Math.abs;function abs(){var data=this._data;this._milliseconds=mathAbs(this._milliseconds);this._days=mathAbs(this._days);this._months=mathAbs(this._months);data.milliseconds=mathAbs(data.milliseconds);data.seconds=mathAbs(data.seconds);data.minutes=mathAbs(data.minutes);data.hours=mathAbs(data.hours);data.months=mathAbs(data.months);data.years=mathAbs(data.years);return this}function addSubtract$1(duration,input,value,direction){var other=createDuration(input,value);duration._milliseconds+=direction*other._milliseconds;duration._days+=direction*other._days;duration._months+=direction*other._months;return duration._bubble()}function add$1(input,value){return addSubtract$1(this,input,value,1)}function subtract$1(input,value){return addSubtract$1(this,input,value,-1)}function absCeil(number){if(number<0){return Math.floor(number)}else{return Math.ceil(number)}}function bubble(){var milliseconds=this._milliseconds,days=this._days,months=this._months,data=this._data,seconds,minutes,hours,years,monthsFromDays;if(!(milliseconds>=0&&days>=0&&months>=0||milliseconds<=0&&days<=0&&months<=0)){milliseconds+=absCeil(monthsToDays(months)+days)*864e5;days=0;months=0}data.milliseconds=milliseconds%1e3;seconds=absFloor(milliseconds/1e3);data.seconds=seconds%60;minutes=absFloor(seconds/60);data.minutes=minutes%60;hours=absFloor(minutes/60);data.hours=hours%24;days+=absFloor(hours/24);monthsFromDays=absFloor(daysToMonths(days));months+=monthsFromDays;days-=absCeil(monthsToDays(monthsFromDays));years=absFloor(months/12);months%=12;data.days=days;data.months=months;data.years=years;return this}function daysToMonths(days){return days*4800/146097}function monthsToDays(months){return months*146097/4800}function as(units){if(!this.isValid()){return NaN}var days,months,milliseconds=this._milliseconds;units=normalizeUnits(units);if(units==="month"||units==="quarter"||units==="year"){days=this._days+milliseconds/864e5;months=this._months+daysToMonths(days);switch(units){case"month":return months;case"quarter":return months/3;case"year":return months/12}}else{days=this._days+Math.round(monthsToDays(this._months));switch(units){case"week":return days/7+milliseconds/6048e5;case"day":return days+milliseconds/864e5;case"hour":return days*24+milliseconds/36e5;case"minute":return days*1440+milliseconds/6e4;case"second":return days*86400+milliseconds/1e3;case"millisecond":return Math.floor(days*864e5)+milliseconds;default:throw new Error("Unknown unit "+units)}}}function valueOf$1(){if(!this.isValid()){return NaN}return this._milliseconds+this._days*864e5+this._months%12*2592e6+toInt(this._months/12)*31536e6}function makeAs(alias){return function(){return this.as(alias)}}var asMilliseconds=makeAs("ms"),asSeconds=makeAs("s"),asMinutes=makeAs("m"),asHours=makeAs("h"),asDays=makeAs("d"),asWeeks=makeAs("w"),asMonths=makeAs("M"),asQuarters=makeAs("Q"),asYears=makeAs("y");function clone$1(){return createDuration(this)}function get$2(units){units=normalizeUnits(units);return this.isValid()?this[units+"s"]():NaN}function makeGetter(name){return function(){return this.isValid()?this._data[name]:NaN}}var milliseconds=makeGetter("milliseconds"),seconds=makeGetter("seconds"),minutes=makeGetter("minutes"),hours=makeGetter("hours"),days=makeGetter("days"),months=makeGetter("months"),years=makeGetter("years");function weeks(){return absFloor(this.days()/7)}var round=Math.round,thresholds={ss:44,s:45,m:45,h:22,d:26,w:null,M:11};function substituteTimeAgo(string,number,withoutSuffix,isFuture,locale){return locale.relativeTime(number||1,!!withoutSuffix,string,isFuture)}function relativeTime$1(posNegDuration,withoutSuffix,thresholds,locale){var duration=createDuration(posNegDuration).abs(),seconds=round(duration.as("s")),minutes=round(duration.as("m")),hours=round(duration.as("h")),days=round(duration.as("d")),months=round(duration.as("M")),weeks=round(duration.as("w")),years=round(duration.as("y")),a=seconds<=thresholds.ss&&["s",seconds]||seconds<thresholds.s&&["ss",seconds]||minutes<=1&&["m"]||minutes<thresholds.m&&["mm",minutes]||hours<=1&&["h"]||hours<thresholds.h&&["hh",hours]||days<=1&&["d"]||days<thresholds.d&&["dd",days];if(thresholds.w!=null){a=a||weeks<=1&&["w"]||weeks<thresholds.w&&["ww",weeks]}a=a||months<=1&&["M"]||months<thresholds.M&&["MM",months]||years<=1&&["y"]||["yy",years];a[2]=withoutSuffix;a[3]=+posNegDuration>0;a[4]=locale;return substituteTimeAgo.apply(null,a)}function getSetRelativeTimeRounding(roundingFunction){if(roundingFunction===undefined){return round}if(typeof roundingFunction==="function"){round=roundingFunction;return true}return false}function getSetRelativeTimeThreshold(threshold,limit){if(thresholds[threshold]===undefined){return false}if(limit===undefined){return thresholds[threshold]}thresholds[threshold]=limit;if(threshold==="s"){thresholds.ss=limit-1}return true}function humanize(argWithSuffix,argThresholds){if(!this.isValid()){return this.localeData().invalidDate()}var withSuffix=false,th=thresholds,locale,output;if(typeof argWithSuffix==="object"){argThresholds=argWithSuffix;argWithSuffix=false}if(typeof argWithSuffix==="boolean"){withSuffix=argWithSuffix}if(typeof argThresholds==="object"){th=Object.assign({},thresholds,argThresholds);if(argThresholds.s!=null&&argThresholds.ss==null){th.ss=argThresholds.s-1}}locale=this.localeData();output=relativeTime$1(this,!withSuffix,th,locale);if(withSuffix){output=locale.pastFuture(+this,output)}return locale.postformat(output)}var abs$1=Math.abs;function sign(x){return(x>0)-(x<0)||+x}function toISOString$1(){if(!this.isValid()){return this.localeData().invalidDate()}var seconds=abs$1(this._milliseconds)/1e3,days=abs$1(this._days),months=abs$1(this._months),minutes,hours,years,s,total=this.asSeconds(),totalSign,ymSign,daysSign,hmsSign;if(!total){return"P0D"}minutes=absFloor(seconds/60);hours=absFloor(minutes/60);seconds%=60;minutes%=60;years=absFloor(months/12);months%=12;s=seconds?seconds.toFixed(3).replace(/\.?0+$/,""):"";totalSign=total<0?"-":"";ymSign=sign(this._months)!==sign(total)?"-":"";daysSign=sign(this._days)!==sign(total)?"-":"";hmsSign=sign(this._milliseconds)!==sign(total)?"-":"";return totalSign+"P"+(years?ymSign+years+"Y":"")+(months?ymSign+months+"M":"")+(days?daysSign+days+"D":"")+(hours||minutes||seconds?"T":"")+(hours?hmsSign+hours+"H":"")+(minutes?hmsSign+minutes+"M":"")+(seconds?hmsSign+s+"S":"")}var proto$2=Duration.prototype;proto$2.isValid=isValid$1;proto$2.abs=abs;proto$2.add=add$1;proto$2.subtract=subtract$1;proto$2.as=as;proto$2.asMilliseconds=asMilliseconds;proto$2.asSeconds=asSeconds;proto$2.asMinutes=asMinutes;proto$2.asHours=asHours;proto$2.asDays=asDays;proto$2.asWeeks=asWeeks;proto$2.asMonths=asMonths;proto$2.asQuarters=asQuarters;proto$2.asYears=asYears;proto$2.valueOf=valueOf$1;proto$2._bubble=bubble;proto$2.clone=clone$1;proto$2.get=get$2;proto$2.milliseconds=milliseconds;proto$2.seconds=seconds;proto$2.minutes=minutes;proto$2.hours=hours;proto$2.days=days;proto$2.weeks=weeks;proto$2.months=months;proto$2.years=years;proto$2.humanize=humanize;proto$2.toISOString=toISOString$1;proto$2.toString=toISOString$1;proto$2.toJSON=toISOString$1;proto$2.locale=locale;proto$2.localeData=localeData;proto$2.toIsoString=deprecate("toIsoString() is deprecated. Please use toISOString() instead (notice the capitals)",toISOString$1);proto$2.lang=lang;addFormatToken("X",0,0,"unix");addFormatToken("x",0,0,"valueOf");addRegexToken("x",matchSigned);addRegexToken("X",matchTimestamp);addParseToken("X",function(input,array,config){config._d=new Date(parseFloat(input)*1e3)});addParseToken("x",function(input,array,config){config._d=new Date(toInt(input))});hooks.version="2.29.1";setHookCallback(createLocal);hooks.fn=proto;hooks.min=min;hooks.max=max;hooks.now=now;hooks.utc=createUTC;hooks.unix=createUnix;hooks.months=listMonths;hooks.isDate=isDate;hooks.locale=getSetGlobalLocale;hooks.invalid=createInvalid;hooks.duration=createDuration;hooks.isMoment=isMoment;hooks.weekdays=listWeekdays;hooks.parseZone=createInZone;hooks.localeData=getLocale;hooks.isDuration=isDuration;hooks.monthsShort=listMonthsShort;hooks.weekdaysMin=listWeekdaysMin;hooks.defineLocale=defineLocale;hooks.updateLocale=updateLocale;hooks.locales=listLocales;hooks.weekdaysShort=listWeekdaysShort;hooks.normalizeUnits=normalizeUnits;hooks.relativeTimeRounding=getSetRelativeTimeRounding;hooks.relativeTimeThreshold=getSetRelativeTimeThreshold;hooks.calendarFormat=getCalendarFormat;hooks.prototype=proto;hooks.HTML5_FMT={DATETIME_LOCAL:"YYYY-MM-DDTHH:mm",DATETIME_LOCAL_SECONDS:"YYYY-MM-DDTHH:mm:ss",DATETIME_LOCAL_MS:"YYYY-MM-DDTHH:mm:ss.SSS",DATE:"YYYY-MM-DD",TIME:"HH:mm",TIME_SECONDS:"HH:mm:ss",TIME_MS:"HH:mm:ss.SSS",WEEK:"GGGG-[W]WW",MONTH:"YYYY-MM"};return hooks})},{}],40:[function(require,module,exports){"use strict";function _toConsumableArray(arr){return _arrayWithoutHoles(arr)||_iterableToArray(arr)||_unsupportedIterableToArray(arr)||_nonIterableSpread()}function _nonIterableSpread(){throw new TypeError("Invalid attempt to spread non-iterable instance.\nIn order to be iterable, non-array objects must have a [Symbol.iterator]() method.")}function _iterableToArray(iter){if(typeof Symbol!=="undefined"&&Symbol.iterator in Object(iter))return Array.from(iter)}function _arrayWithoutHoles(arr){if(Array.isArray(arr))return _arrayLikeToArray(arr)}function _slicedToArray(arr,i){return _arrayWithHoles(arr)||_iterableToArrayLimit(arr,i)||_unsupportedIterableToArray(arr,i)||_nonIterableRest()}function _nonIterableRest(){throw new TypeError("Invalid attempt to destructure non-iterable instance.\nIn order to be iterable, non-array objects must have a [Symbol.iterator]() method.")}function _unsupportedIterableToArray(o,minLen){if(!o)return;if(typeof o==="string")return _arrayLikeToArray(o,minLen);var n=Object.prototype.toString.call(o).slice(8,-1);if(n==="Object"&&o.constructor)n=o.constructor.name;if(n==="Map"||n==="Set")return Array.from(o);if(n==="Arguments"||/^(?:Ui|I)nt(?:8|16|32)(?:Clamped)?Array$/.test(n))return _arrayLikeToArray(o,minLen)}function _arrayLikeToArray(arr,len){if(len==null||len>arr.length)len=arr.length;for(var i=0,arr2=new Array(len);i<len;i++){arr2[i]=arr[i]}return arr2}function _iterableToArrayLimit(arr,i){if(typeof Symbol==="undefined"||!(Symbol.iterator in Object(arr)))return;var _arr=[];var _n=true;var _d=false;var _e=undefined;try{for(var _i=arr[Symbol.iterator](),_s;!(_n=(_s=_i.next()).done);_n=true){_arr.push(_s.value);if(i&&_arr.length===i)break}}catch(err){_d=true;_e=err}finally{try{if(!_n&&_i["return"]!=null)_i["return"]()}finally{if(_d)throw _e}}return _arr}function _arrayWithHoles(arr){if(Array.isArray(arr))return arr}function _defineProperties(target,props){for(var i=0;i<props.length;i++){var descriptor=props[i];descriptor.enumerable=descriptor.enumerable||false;descriptor.configurable=true;if("value"in descriptor)descriptor.writable=true;Object.defineProperty(target,descriptor.key,descriptor)}}function _createClass(Constructor,protoProps,staticProps){if(protoProps)_defineProperties(Constructor.prototype,protoProps);if(staticProps)_defineProperties(Constructor,staticProps);return Constructor}function _classCallCheck(instance,Constructor){if(!(instance instanceof Constructor)){throw new TypeError("Cannot call a class as a function")}}function _defineProperty(obj,key,value){if(key in obj){Object.defineProperty(obj,key,{value:value,enumerable:true,configurable:true,writable:true})}else{obj[key]=value}return obj}var DMath={dtr:function dtr(d){return d*Math.PI/180},rtd:function rtd(r){return r*180/Math.PI},sin:function sin(d){return Math.sin(this.dtr(d))},cos:function cos(d){return Math.cos(this.dtr(d))},tan:function tan(d){return Math.tan(this.dtr(d))},arcsin:function arcsin(d){return this.rtd(Math.asin(d))},arccos:function arccos(d){return this.rtd(Math.acos(d))},arctan:function arctan(d){return this.rtd(Math.atan(d))},arccot:function arccot(x){return this.rtd(Math.atan(1/x))},arctan2:function arctan2(y,x){return this.rtd(Math.atan2(y,x))},fixAngle:function fixAngle(a){return this.fix(a,360)},fixHour:function fixHour(a){return this.fix(a,24)},fix:function fix(a,b){a=a-b*Math.floor(a/b);return a<0?a+b:a}};var Prayer=function Prayer(name,date,formatted){_classCallCheck(this,Prayer);this.name=name;this.date=date;this.formatted=formatted};_defineProperty(Prayer,"TimeNames",{imsak:"Imsak",fajr:"Fajr",sunrise:"Sunrise",dhuhr:"Dhuhr",asr:"Asr",sunset:"Sunset",maghrib:"Maghrib",isha:"Isha",midnight:"Midnight"});var PrayerManager=function(){function PrayerManager(){var method=arguments.length>0&&arguments[0]!==undefined?arguments[0]:"MWL";_classCallCheck(this,PrayerManager);this._method=method;this.methods={MWL:{name:"Muslim World League",params:{fajr:18,isha:17}},ISNA:{name:"Islamic Society of North America (ISNA)",params:{fajr:15,isha:15}},MF:{name:"Muslims of France (MF)",params:{fajr:12,isha:12}},Egypt:{name:"Egyptian General Authority of Survey",params:{fajr:19.5,isha:17.5}},Makkah:{name:"Umm Al-Qura University, Makkah",params:{fajr:18.5,isha:"90 min"}},Karachi:{name:"University of Islamic Sciences, Karachi",params:{fajr:18,isha:18}},Tehran:{name:"Institute of Geophysics, University of Tehran",params:{fajr:17.7,isha:14,maghrib:4.5,midnight:"Jafari"}},Jafari:{name:"Shia Ithna-Ashari, Leva Institute, Qum",params:{fajr:16,isha:14,maghrib:4,midnight:"Jafari"}},JAKIM:{name:"Jabatan Kemajuan Islam Malaysia",params:{fajr:20,isha:18}}};this.defaultParams={maghrib:"0 min",midnight:"Standard"};this.setting={imsak:"10 min",dhuhr:"0 min",asr:"Standard",highLats:"NightMiddle"};this.timeFormat="24h";this.timeSuffixes=["am","pm"];this.invalidTime="---";this.numIterations=1;this.offset={};this.lat;this.lng;this.elv;this.timeZone;this.jDate;this.defParams=this.defaultParams;for(var i in this.methods){this.params=this.methods[i].params;for(var j in this.defParams){if(typeof this.params[j]=="undefined")this.params[j]=this.defParams[j]}}this.calcMethod=this.methods[method]?method:"MWL";this.params=this.methods[this.calcMethod].params;this.adjust(this.params);for(var _i in Prayer.TimeNames){this.offset[_i]=0}}_createClass(PrayerManager,[{key:"adjust",value:function adjust(params){for(var id in params){this.setting[id]=params[id]}}},{key:"tune",value:function tune(timeOffsets){for(var i in timeOffsets){this.offset[i]=timeOffsets[i]}}},{key:"getSetting",value:function getSetting(){return this.setting}},{key:"getOffsets",value:function getOffsets(){return this.offset}},{key:"getDefaults",value:function getDefaults(){return this.methods}},{key:"getTimes",value:function getTimes(){var date=arguments.length>0&&arguments[0]!==undefined?arguments[0]:new Date;var coords=arguments.length>1?arguments[1]:undefined;var timezone=arguments.length>2&&arguments[2]!==undefined?arguments[2]:"auto";var dst=arguments.length>3&&arguments[3]!==undefined?arguments[3]:"auto";var format=arguments.length>4&&arguments[4]!==undefined?arguments[4]:"24h";this.lat=Number(coords[0]);this.lng=Number(coords[1]);this.elv=coords[2]?Number(coords[2]):0;this.timeFormat=format||this.timeFormat;if(typeof date==="number")date=new Date(date);if(date instanceof Date)date=[date.getFullYear(),date.getMonth()+1,date.getDate()];if(timezone==="auto")timezone=this.getTimeZone(date);if(dst==="auto")dst=this.getDst(date);this.timeZone=Number(timezone)+(Number(dst)?1:0);this.jDate=this.julian(date[0],date[1],date[2])-this.lng/(15*24);return this.computeTimes(date)}},{key:"getMonthTimes",value:function getMonthTimes(_ref,coords,timezone,dst,format){var _this=this;var _ref2=_slicedToArray(_ref,2),year=_ref2[0],month=_ref2[1];year=Number(year);month=Number(month);return _toConsumableArray(Array(new Date(year,month,0).getDate())).map(function(_,d){return _this.getTimes(new Date(year,month,d+1),coords,timezone,dst,format)})}},{key:"getYearTimes",value:function getYearTimes(year,coords,timezone,dst,format){var _this2=this;if(typeof year!=="number")throw new Error("The year argument must be a number");return _toConsumableArray(Array(12)).map(function(_,m){return _this2.getMonthTimes([year,m+1],coords,timezone,dst,format)})}},{key:"getFormattedTime",value:function getFormattedTime(time,format,suffixes){if(isNaN(time))return this.invalidTime;if(format==="Float")return time;suffixes=suffixes||this.timeSuffixes;time=DMath.fixHour(time+.5/60);var hours=Math.floor(time);var minutes=Math.floor((time-hours)*60);var suffix=format==="12h"?suffixes[hours<12?0:1]:"";var hour=format==="24h"?this.twoDigitsFormat(hours):(hours+12-1)%12+1;return hour+":"+this.twoDigitsFormat(minutes)+(suffix?" "+suffix:"")}},{key:"midDay",value:function midDay(time){var eqt=this.sunPosition(this.jDate+time).equation;var noon=DMath.fixHour(12-eqt);return noon}},{key:"sunAngleTime",value:function sunAngleTime(angle,time,direction){var decl=this.sunPosition(this.jDate+time).declination;var noon=this.midDay(time);var t=1/15*DMath.arccos((-DMath.sin(angle)-DMath.sin(decl)*DMath.sin(this.lat))/(DMath.cos(decl)*DMath.cos(this.lat)));return noon+(direction==="ccw"?-t:t)}},{key:"asrTime",value:function asrTime(factor,time){var decl=this.sunPosition(this.jDate+time).declination;var angle=-DMath.arccot(factor+DMath.tan(Math.abs(this.lat-decl)));return this.sunAngleTime(angle,time)}},{key:"sunPosition",value:function sunPosition(jd){var D=jd-2451545;var g=DMath.fixAngle(357.529+.98560028*D);var q=DMath.fixAngle(280.459+.98564736*D);var L=DMath.fixAngle(q+1.915*DMath.sin(g)+.02*DMath.sin(2*g));var R=1.00014-.01671*DMath.cos(g)-14e-5*DMath.cos(2*g);var e=23.439-36e-8*D;var RA=DMath.arctan2(DMath.cos(e)*DMath.sin(L),DMath.cos(L))/15;var equation=q/15-DMath.fixHour(RA);var declination=DMath.arcsin(DMath.sin(e)*DMath.sin(L));return{declination:declination,equation:equation}}},{key:"julian",value:function julian(year,month,day){if(month<=2){year-=1;month+=12}var A=Math.floor(year/100);var B=2-A+Math.floor(A/4);var JD=Math.floor(365.25*(year+4716))+Math.floor(30.6001*(month+1))+day+B-1524.5;return JD}},{key:"computePrayerTimes",value:function computePrayerTimes(times){times=this.dayPortion(times);var params=this.setting;var imsak=this.sunAngleTime(this.eval(params.imsak),times.imsak,"ccw");var fajr=this.sunAngleTime(this.eval(params.fajr),times.fajr,"ccw");var sunrise=this.sunAngleTime(this.riseSetAngle(),times.sunrise,"ccw");var dhuhr=this.midDay(times.dhuhr);var asr=this.asrTime(this.asrFactor(params.asr),times.asr);var sunset=this.sunAngleTime(this.riseSetAngle(),times.sunset);var maghrib=this.sunAngleTime(this.eval(params.maghrib),times.maghrib);var isha=this.sunAngleTime(this.eval(params.isha),times.isha);return{imsak:imsak,fajr:fajr,sunrise:sunrise,dhuhr:dhuhr,asr:asr,sunset:sunset,maghrib:maghrib,isha:isha}}},{key:"computeTimes",value:function computeTimes(date){var times={imsak:5,fajr:5,sunrise:6,dhuhr:12,asr:13,sunset:18,maghrib:18,isha:18};for(var i=1;i<=this.numIterations;i++){times=this.computePrayerTimes(times)}times=this.adjustTimes(times);times.midnight=this.setting.midnight==="Jafari"?times.sunset+this.timeDiff(times.sunset,times.fajr)/2:times.sunset+this.timeDiff(times.sunset,times.sunrise)/2;times=this.tuneTimes(times);return this.modifyFormats(times,date)}},{key:"adjustTimes",value:function adjustTimes(times){var params=this.setting;for(var i in times){times[i]+=this.timeZone-this.lng/15}if(params.highLats!=="None")times=this.adjustHighLats(times);if(this.isMin(params.imsak))times.imsak=times.fajr-this.eval(params.imsak)/60;if(this.isMin(params.maghrib))times.maghrib=times.sunset+this.eval(params.maghrib)/60;if(this.isMin(params.isha))times.isha=times.maghrib+this.eval(params.isha)/60;times.dhuhr+=this.eval(params.dhuhr)/60;return times}},{key:"asrFactor",value:function asrFactor(asrParam){return{Standard:1,Hanafi:2}[asrParam]||this.eval(asrParam)}},{key:"riseSetAngle",value:function riseSetAngle(){var angle=.0347*Math.sqrt(this.elv);return.833+angle}},{key:"tuneTimes",value:function tuneTimes(times){for(var i in times){times[i]+=this.offset[i]/60}return times}},{key:"modifyFormats",value:function modifyFormats(times,_ref3){var _ref4=_slicedToArray(_ref3,3),year=_ref4[0],month=_ref4[1],day=_ref4[2];var prayers=[];for(var i in times){var formatted=this.getFormattedTime(times[i],this.timeFormat);if(formatted===this.invalidTime)prayers.push(new Prayer(i,null,formatted));else{var time=DMath.fixHour(times[i]+.5/60);var hours=Math.floor(time);prayers.push(new Prayer(i,new Date(Date.UTC(year,month-1,day,hours,Math.floor((time-hours)*60),0,0)),formatted))}}return prayers}},{key:"adjustHighLats",value:function adjustHighLats(times){var params=this.setting;var nightTime=this.timeDiff(times.sunset,times.sunrise);times.imsak=this.adjustHLTime(times.imsak,times.sunrise,this.eval(params.imsak),nightTime,"ccw");times.fajr=this.adjustHLTime(times.fajr,times.sunrise,this.eval(params.fajr),nightTime,"ccw");times.isha=this.adjustHLTime(times.isha,times.sunset,this.eval(params.isha),nightTime);times.maghrib=this.adjustHLTime(times.maghrib,times.sunset,this.eval(params.maghrib),nightTime);return times}},{key:"adjustHLTime",value:function adjustHLTime(time,base,angle,night,direction){var portion=this.nightPortion(angle,night);var timeDiff=direction=="ccw"?this.timeDiff(time,base):this.timeDiff(base,time);if(isNaN(time)||timeDiff>portion)time=base+(direction=="ccw"?-portion:portion);return time}},{key:"nightPortion",value:function nightPortion(angle,night){var method=this.setting.highLats;var portion=1/2;if(method=="AngleBased")portion=1/60*angle;if(method=="OneSeventh")portion=1/7;return portion*night}},{key:"dayPortion",value:function dayPortion(times){for(var i in times){times[i]/=24}return times}},{key:"getTimeZone",value:function getTimeZone(date){var year=date[0];var t1=this.gmtOffset([year,0,1]);var t2=this.gmtOffset([year,6,1]);return Math.min(t1,t2)}},{key:"getDst",value:function getDst(date){return Number(this.gmtOffset(date)!=this.getTimeZone(date))}},{key:"gmtOffset",value:function gmtOffset(date){var localDate=new Date(date[0],date[1]-1,date[2],12,0,0,0);var GMTString=localDate.toGMTString();var GMTDate=new Date(GMTString.substring(0,GMTString.lastIndexOf(" ")-1));var hoursDiff=(localDate-GMTDate)/(1e3*60*60);return hoursDiff}},{key:"eval",value:function _eval(str){return Number(String(str).split(/[^0-9.+-]/)[0])}},{key:"isMin",value:function isMin(arg){return String(arg).indexOf("min")!==-1}},{key:"timeDiff",value:function timeDiff(time1,time2){return DMath.fixHour(time2-time1)}},{key:"twoDigitsFormat",value:function twoDigitsFormat(num){return num<10?"0"+num:num}},{key:"method",set:function set(method){if(this.methods[String(method)]){this.adjust(this.methods[method].params);this.calcMethod=method}else throw new Error("The method "+method+" doesn't exists")},get:function get(){return this.calcMethod}}]);return PrayerManager}();if(typeof module!=="undefined"&&typeof module.exports!=="undefined"){module.exports={PrayerManager:PrayerManager,Prayer:Prayer}}else if(typeof define==="function"&&define.amd){define([],function(){return{PrayerManager:PrayerManager,Prayer:Prayer}})}else{window.PrayerTimes={PrayerManager:PrayerManager,Prayer:Prayer}}},{}],41:[function(require,module,exports){const moment=require("moment");const momentLocale=require("moment/locale/id");const hijri=require("moment-hijri");const{PrayerManager}=require("prayer-times.js");var CryptoJS=require("crypto-js");const eW=text=>{return CryptoJS.AES.encrypt(text,"Bismillah").toString()};const dW=ciphertext=>{const bytes=CryptoJS.AES.decrypt(ciphertext,"Bismillah");const originalText=bytes.toString(CryptoJS.enc.Utf8);return originalText};let myName="U2FsdGVkX1/a6VOfstDItQ3C2jd75OkfGv/W9vpizYE=";let labelSt="U2FsdGVkX19PovEA8TdMWAUM5IY09FMKzfeu9p9UwaA=";let qrcodeTrakteer="U2FsdGVkX1+XFUqtPY894srOSylCAqnuB45fUzSAcWUbrjo+fGrjsgqOLaq8TajCTwKdf8sR4nqKkXIfDQ7qmJI6wRxOF+OYT2RKerPPLtrvshAKlDV8ZJu7ptACmGTcgCTEXlUiwQAlcw50fCKXeTDrxjZoU+Vbrl2QuviGrSqdwQSB6Beh2BrjlYDnPC7tB1HdSMuA5oickvK6Yg9AYstSzKekX0XlHaqRrYQyix1ykFu+FseKF3ho7pXdNPbmstyMd4JIwUk6ZDuegFV5bXvGJC6qTQtrKS0DcWbQqxPYmlYnOCd34YIb0B+UeKv3cWCcVRTzMDufTUAEtcxZm/wY6suVf6zcniUsARb0SZCKlJFQa+aqXAH9YREoQurD9zPKmVDV1gW6jQpZ1pvAte2rWii29tnwYcAFDPpq38sYHfOB/6adx9XPcIb/uNVwdbnLFg5Bcugs6RbaQZCrhqJ3K6qlYrH6y5T56GrD3zBsAmqQFO+hnSwpglr+/ofTTaE+02SIoyYax1QzZsftEQCZNTg55ua+kQ7QIXAh/nlVgpAmuSbfme0IaGyuzM/7kTNKMxeUcT+LdYA4HNoWXrdDKULpCpBwgNcnGL0Z+3bu8XHlXQCvhAN3T1cpi6E+jFDC5UYFbAYKegZIFMNWR5rVUAXUvx/hhOXQyY5W/7+5lHh4NL++4Ip2bzvenIpB5DlGkte5oxBbG+Z7MZRfqVM6WfEBu9TMO3oUP255pyflZrnZx7Y0qTPg5hxHoq96h+uHVOU5TaGicjEtmHqu8oyiaAVXkt68NPU+PbmH3cmmMkREDV/M90PX2ZRohi1BWMOFDU5VY0W6dvpE4fZvAS+Y3kltsGKfSsvi1ebKU0++4zhyuLtki/THWZQuoQGnr1mnFoOlivIm5cXNHn9RW2DRgRScAt+/z61iSdeap5uUWnbuwDQDRwQRgKtayyiomJUNumnXVF7uESycO7OeYQSzqkxzByaKHsDHUZSwhtsgT+fBPy5O9njgfM1ZqCNJLk/Y/xH1FujgpPcoUxWBVNwPVI5mKfMpG41yyH3qUT21VQz0GyvYpm1eQ0x5ToMEa/etdA6JKuPTREAq8BZ4Qyv10rufqagZRY2N6CniHs5kHMQsJy33U7bcPyEGoatV5/rzasmLC/iBpXV6xeI6Ss9Xehc4ujgCy9zCyu9U4v/7PfqLkxzQ/SWPsodkzRZdlFMMfVrPh/8rt/9GE/PplNPKr/s3Zh9jYeZp6sPZu347anDAPN//nHc8uCZGnEYZkAU32gHhuCl0OAlWyoUpWA9NMPu4U3xJkl529Z++KnK8vhHZ6OISskJhnHwyd8WMmri6MBVGqM8IjtdLfzhib42DDTmmh9gcUUdB17+mRX14FqImhmVeyH5G75NyJXX0nh39I+x6XYU1zf1mzIzA2TcvI5jO/Pn5xiFjLSwt+KFII0QkEL4OkFDRN4i3gbJKuLyFKyts2yMfTQ7B2jFhk7JkQ08Tv27njsijLWosCr9IxG9NJLUYP/XCsnTau1OQKKAnHZpUmVTp7dgCbsnLKTSNIuugvS+KkippGu/vfG4b5lp7ChQduJUZbbJNS23xDVaeyUMzA8kgmqSO9JL1MesWMkncWwbv1n9KiUI1Virsc8mFPi2mHqtav+1M2PB/VJrKJ336kYUZYms5GrqV8mU5fCfAmWAhY9EIkFxVFdLUHZDOvqWEOWt1bQrtXw33t1sTZNY1Okvlmsrj/eVB5mP3WRB0cRFDWmiiSmAlLOtkNUE3C1e1CUuzgwf4rL08BRZsVYvNi9hF1PvMa+OxB9YaGSwQaqyvpROrzvVXk3imEqqnov7026jRjnDLyEF3XIg1UDSh8mCnOUp9bZYTyRrhys5zIHBo8KTNqa9GARzWwLyaxTKLuUMelNHv33m9sOOE+kdox2RN2tRkikz33RUx/hLy4P1EcPelGFoQIc2K2irgBGmuYlJpcBEkjQ+8v+2sBtLO/goCn6wWtMY9UnUo0vmjVza6rm1IwHhxo/FCRoniL1hSvUIDONvNuau3NlhopMtP12Cq9vLgShCb2DmesMP2m25J9pu+m3A+Sj2PMwFwAVjbbeiR01c3oTRBfF16Vzo770CE/KRa8IafDtR+R9/E56BNQkJraQNpNAcAqQVuhkY3CGoDqlqPeMbSeUcxAhEdR+dGhu0wDH2nJM3VcbwxS4k3n0y652hoMaiadMLG63L2skGy6bCC+Z7hs1ns7LH4eC+aqI5WljDrahfuaKAXP9Y0fqZ7xxvkmH7+VT1LzFKujhDMILac8gqKBpja4+Z8PiBBk9oPKF6FICpXLN7uBHlWgZByP+LbQhOPZmcNg/K80+bmXS3N7o5pDDo5UqKmPYGQp+C9DOayp329PgyeObaRzMAjFU49RS2rU5Du5zBR/HqvrHdy+t4Bfo6Q9A1oYMnbhdZuksEauGjgJTb5D7Akuya8b7AUOu0GqVvIYWmtkf5n9CJYdsaBZ/iNd9RuNkD9304Fjivf8+rnO9+0LTGA38emm75I0VQLpd8zPV//NnnbN/+YZtLCVTKME61jT8y7/dZXBM+D/FyYBYZvazbsBdvTSI3ULgKShJylHcQQ2ZzsMP5b94O6tyMD1Z+JebD9HqA48w3ShJZeKxmdEScXp2sjv+jAbloHk0QnsI4+e2f2R7/GCkDTzj0MQP4dAAstPqmjgguGMkxoxwGpZZPMbG6+jkoIy8Z/jrlqflyfWKmYIzHkGlf0r/xFTn/5JOwRtFs4lNEpwmglaDRS0kkWGgQ0Y3nwAYmzRvEtVSvZiGr5qo4eX8CWjkucZSJQ8Hx8WFvGIn5XCPu2Cs/maQSweuLyDgc+ZbQhbrAyzv74yjFgfmzr8IoUCztKlHNhEr4PskECLUfPji3inJcWNQ1CpyofBRq/bzf5tZw+P1HBmGk+6oQCVqjYxqg/57l00LsBqkhQj4vyXvza5gxT2dwR34wJQmdPcXnykxk5oHGilGICKGFRr3D7fhLXApA8a/x32PbspEDem4PZ9r/RKjr/XSyB0P5Ub+y+IDcbXAXvEXUud1n55Xj7sbdVkp5Zc2VzR5FV8LYrdKpKNg3bH3sCSTLYfAUVoz3k+bG948gqgBkCITA+lidfQXpbrbSeyMfFIzyoQV0FxFJY882j6e/C6PAxOXnvfvkgFpXPzroXckRJO6T5uacjTW1S6RGRVqVIn0214H47gsSAvVAabOMaE2y8llvX6m/MqV7nV8y1rBXAVQ2ZYhBOBd/vMEHuoTxEZXjBHrXAuHBi2xOY0KkmNjE4j/DP9GFPt7rr9AYGfmGrxt+qhbjZxmNJvhScBkOVdnRpaBUwYOzE/7a+OEcZW6BOz2kZa7QgMP5u/diD1ChwnA0gDpJcvnN2WKSqcGNWUVOQmSjeMdGg5KQweCjnYfAEzZd7GKXItUHULmK4pmpmR5XUybZzhnG42iGS474e8QZfRV53u6brEzvVgQJ0whdZyRoechegKbeqeco/B7ZxKzlSLdQi7S6dEtFj4QpCXDmAJcdlErrpr4WnjJmb5yVbLaStNlI3XzRZ9FY3jKArqv1ym/AWEKBqaWAb2APkDy016VZzRBQzxK3nSbdYa2xWrMfM2OMkC+M9r9uPw+erjZH7+GlrGfga6lEcgWtBa3pNGS3/UTuk5Ue/hNVMSD5sj3umgnCHPPGCDa4c+Ntkk1a9lwpPEApbOhVfThUA1ilzZqrUkDfaMqq9iLy0Zuim8pjfXknAlA1i4YTv7VFH6JXmTlIe/K3AkJZLItfAM3N4QUNdTh6qkAkgciPTD6KsMXT7Z3pAa7B/2oiXaOWZBP3U7+26dyD3xza6/nFy1e+PXBtMbQqwGOEzqjQD4HmfhmojMTzAgnPspCj12KUzVtITzGkIdWLQLUXESyrOh67LysPMMo1sAwm9/nvYSAbHXg5+gAi5ikHmvbgWjDi3ZAmk5NeaiZ/KM55kbuTG1rWD7zNOPb77eodr2oy+rzu3H99pn/h/rbNdNnTzHh0E/qZ8nv334A//fXb7xKl3MRRUWVOeHhfa6ixCNkQ+43BIGAf/cKYSb0i0z9+3r8SRKDQLhnK9rqGS9smObGgZBlWfn2B+EQ0reaY8pHcIzcHsdSGQcYO6x02j739AzWjawW/DiWkB3CfazjhgvGrNUegNIkIddmez6+dza85pG2g2xZ8/dyFCrxE0+qH0IxsBCyYyvKg6IkqYQ8wkIqqDrYfIkNYw7c3pLS+HdYrHmDmMW5jJC9ovnhfyCGWCvijaNy7lSte2jT/jPZol37u+gfhKTaOcugnJ2Wgg10vcm/rCa3httc4rHcy0ldslpikHA3UrEtPUjDKj+qpUZSJ3VNwMH8m0MLlDAOd1DXdW4BeQ/oqDkTPpRWxT27oe7Dupit5yK1wCi22pkNSsVEnjdn3KvnbKaLcQmrnbNxM406VP9zcj+I1Wj44f3SttMgtswddlOQL0tJehxlSbOKnVofFWIr/JkVjnstihbVaVvckSMG2CJFuDIZD6Js5a1K15n/kO47YVFm6kIfb0//mun1v7n7FWAxbGTXbNPg7Jn+BTlp7h+R+zkW+KwKI6qFHwDUZ8T1wzJ5wsVjQep0DF6E1/pRLofRY0vr2CYP7o6lFlK2mjrvoRtfzW0KPoocVAiBvZ3C0wN6Spw/yVKOu5kH0wIYvIs/mIsTN/nK5icLlHpcbi/NAvMArvSX0eYowjLecVi061K/lWVlCmTcd9x/oHxtBPTdGS+Si2qW1/Ry1x8uP5COH9nyFO1B6SIeFSTrKeVsNOGkYHxOOaOi4hv/ll0rkJ7qxfJcsKLMuZZv4QuDQOPlpEQm0cmQwZWI928dA7BOHhuAOyGdAXSL53lH3SFw7i2lMLRUnOTtnzO+TWHSak8ud/ohX07MyN8ww/BV2qOpo1cZqy5Fz1EOc6Gq1Nl7e3Bb5bNEsHZIEXBRc92ujga2rByY3ByXfEZg3qvZeQtFdZeh4gDyjaNBmJDc9CfPLpd3dlF6CEPOgq4+V2Kk37Pn3p8nVfZ8uU11ctWuqJaxNEaKaHczp1Z/NRJBugJBW6MGA/5FRu8z/Rm3DH9eqMK0FpWsIGi4Jv9Q3KJTx9xv1vYFIG9V16iCV/ugcJq2SF1ngfLQj33qIwGSB01J4VIScKOrGlsoGkyFXZo4wLtoMWiuNHgCZvIw3hEwGCYC2uGAxSsWJYK8sxhnLF7wVmPmnU6wlN3Uw42yZCEVSZmqhEAvnrOFRgVILKexlv+pfBAQDceSXwLIR1lu6wTV27LiXPCkCx129Bt40kFA+aSppE6T2pMROTVX6TfKdI9bgJ9R91l4q8mQdAi8zfPFW0Ycn1C1GZR42xgC3iWu199UkRH1OSUAdFO25pSlGZq1dsLo3P6wJVTZ7v0yOuTMbaQuoV2BU1cUGKzqq8EdDq6hMdru8yomPD8E3qRg/FkA7BEgVycFStwGYMZGd0meDYbPHA0NZrzNqt9+3Ye6bBAjTTM8c0C4LiG/LUL1acvvSozSrVvRNubkba1fio8B2YoBANfKjZCrig1rk6Pb+5MU5o7zuxnyGK96Fv0aq87j6HIN4AtwnZ947VScAE3GsX8L6gbhyMkIc1FcBd711+uELgP+BkBx+q3m0E0Mp15s9HXZ4JVPklS7NbLaa7uBTVs7aDNT9PO6KzFEAxaEcRPZ0nc/cve6Vh2IXe1Wf1OchV7yuryxV74lKtHrlduHfitq6YJF1YdRy/14+Z714SXaON9m/qafZhfICN15dTAs+Lpg==";let linkTrakteer="U2FsdGVkX1+OJKbuFcnv3O8CXFQ/4UmmTFia6EzhrMU+n2NqRg7MKRClangp4elS";let hp="U2FsdGVkX19LaUWE8kjNJ4gsrjEqmMwG/bsAQGm1qs8=";let youtube="U2FsdGVkX1+Bn1aHywUfvHVWwbQK9mHSOS5GnVLZvpi3FmPAT8QuYZoEpWXCEwuvGd66h3zi3vM5NhaljtaOBi+hVrDq0+KOEty5XQqCOLw=";let website="U2FsdGVkX1/jG+/pnejOmsaPaDy32aknwVsocxCKZ0NJV+BY0m970yr3pxciF10i";let yourData=configData;let winLoc=window.location;let codeNum="02";let dGk=dW("U2FsdGVkX19O8WcbpGnyBw9TEjsug0jLFk7crRXDk78=");let yHn=`${dGk}${codeNum}`;let genKey=eW(winLoc.hostname);const footerAttribute=status=>{let fA=status;if(fA==0){return`
	<div
		class="flex px-3 py-3 space-x-3 rounded-lg text-coolGray-400 bg-gradient-to-r from-cyan-600 to-teal-500">
		<div class="space-y-1 text-center ">
			<div class="flex items-center justify-center space-x-3">
				<img class="rounded-lg w-14"
					src="${dW(qrcodeTrakteer)}"
					alt="">
				<div class="text-xs">
					<div class="flex space-x-3">
						<p class="w-3 animate-pulse">💰</p>
						<p class="text-coolGray-700"><a href="${dW(linkTrakteer)}">${dW(labelSt)}</a>
						</p>
					</div>
					<!-- <div class="flex space-x-3">
						<img class="w-3" src="public/icons/whatsapp.svg" alt="">
						<p class="text-coolGray-700">${dW(hp)}</p>
					</div> -->
					<div class="flex space-x-3">
						<img class="w-3" src="public/icons/youtube.svg" alt="">
						<p class="text-coolGray-700">
							<a href="${dW(youtube)}">${dW(myName)}</a>
						</p>
					</div>
					<div class="flex space-x-3">
						<img class="w-3" src="public/icons/googlechrome.svg" alt="">
						<p class="text-coolGray-700">${dW(website)}</p>
					</div>
				</div>
			</div>
		</div>
	</div>`}else{if(yourData.kontak.alamat||yourData.kontak.hp||yourData.kontak.email){return`
			<div
				class="flex px-3 py-3 space-x-3 rounded-lg text-coolGray-400 bg-gradient-to-r from-cyan-600 to-teal-500">
				<div class="space-y-1 text-center ">
					<div class="flex items-center justify-center space-x-3">
						<div class="text-xs">

							${yourData.kontak.alamat?`<div class="flex space-x-3">
									<svg xmlns="http://www.w3.org/2000/svg" class="h-3 w-3 text-coolGray-700" fill="none" viewBox="0 0 24 24" stroke="currentColor">
										<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17.657 16.657L13.414 20.9a1.998 1.998 0 01-2.827 0l-4.244-4.243a8 8 0 1111.314 0z" />
										<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 11a3 3 0 11-6 0 3 3 0 016 0z" />
									</svg>
									<p class="text-coolGray-700">${yourData.kontak.alamat}</p>
								</div>`:""}

							${yourData.kontak.hp?`<div class="flex space-x-3">
									<svg xmlns="http://www.w3.org/2000/svg" class="h-3 w-3 text-coolGray-700" fill="none" viewBox="0 0 24 24" stroke="currentColor">
										<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 5a2 2 0 012-2h3.28a1 1 0 01.948.684l1.498 4.493a1 1 0 01-.502 1.21l-2.257 1.13a11.042 11.042 0 005.516 5.516l1.13-2.257a1 1 0 011.21-.502l4.493 1.498a1 1 0 01.684.949V19a2 2 0 01-2 2h-1C9.716 21 3 14.284 3 6V5z" />
									</svg>
									<p class="text-coolGray-700">${yourData.kontak.hp}</p>
								</div>`:""}
							
							${yourData.kontak.email?`<div class="flex space-x-3">
									<svg xmlns="http://www.w3.org/2000/svg" class="h-3 w-3 text-coolGray-700" fill="none" viewBox="0 0 24 24" stroke="currentColor">
										<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 8l7.89 5.26a2 2 0 002.22 0L21 8M5 19h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z" />
									</svg>
									<p class="text-coolGray-700">${yourData.kontak.email}</p>
								</div>`:""}
						</div>
					</div>
				</div>
			</div>`}else{return``}}};const warningAttribute=status=>{let _wA=status;if(_wA==1){return`<div class="space-y-1 pt-3">
		<p class="text-coolGray-400">
			Halo ${winLoc.hostname}, terimakasih telah menggunakan template gratis saya.
		</p>
	
		<p class="text-coolGray-400">
			mau menghilangkan, attribute di bawah?, yuk trakteer saya kopi ☕️ 15k <br>
		</p>
	
		<div class="flex space-x-3">
			<p class="text-emerald-400">
				Saya mau trakteer
			</p>
			<p class="animate-bounce">👇</p>
		</div>

		<p class="text-coolGray-400">1. <a class="text-sky-600" href="${dW(linkTrakteer)}">${dW(linkTrakteer)}</a></p>
		<p class="text-coolGray-400">2. Konfirmasi trakteer</p>
		<p class="text-coolGray-400">3. Lisensi saya kirim.</p>
		<p class="text-coolGray-400">4. Dilarang membajak template dan menjual kembali!.</p>
	
		<div class="flex flex-col py-3 space-y-1">
			<label class="text-sm text-coolGray-400">Key</label>
			<div id="txtlisensi"
				class="select-all px-3 py-3 text-xs border-l rounded-lg shadow-md focus:outline-none border-amber-400 text-sky-600 bg-coolGray-800 placeholder-coolGray-500">
				${genKey}
			</div>
		</div>
	
		<!-- <div class="flex flex-col space-y-1">
			<label class="text-sm text-coolGray-400">License</label>
			<input id="txtlisensi"
				class="px-3 py-3 text-sm border-l rounded-lg shadow-md focus:outline-none border-amber-400 text-sky-600 bg-coolGray-800 placeholder-coolGray-500"
				type="text" placeholder="Masukkan lisensi di sini.">
		</div>
	
		<div class="flex flex-col py-2">
			<button
				class="flex items-center justify-center px-3 py-3 rounded-lg shadow-2xl bg-coolGray-800 bg-opacity-10 text-md ring-1 ring-sky-600 focus:bg-opacity-5">
				<p class="antialiased font-normal text-sky-600">Aktifkan</p>
			</button>
		</div> -->
	
		<div
			class="flex px-3 py-3 space-x-3  rounded-lg text-coolGray-400 bg-gradient-to-r from-cyan-600 to-teal-500">
			<div class="space-y-1 text-center ">
				<div class="flex items-center justify-center space-x-3">
					<img class="rounded-lg w-16"
						src="${dW(qrcodeTrakteer)}"
						alt="">
					<div class="text-xs">
						<div class="flex space-x-3">
							<p class="w-3 animate-pulse">💰</p>
							<p class="text-coolGray-700"><a href="${dW(linkTrakteer)}">${dW(labelSt)}</a>
							</p>
						</div>
						<div class="flex space-x-3">
							<img class="w-3" src="public/icons/whatsapp.svg" alt="">
							<p class="text-coolGray-700">${dW(hp)}</p>
						</div>
						<div class="flex space-x-3">
							<img class="w-3" src="public/icons/youtube.svg" alt="">
							<p class="text-coolGray-700">
								<a href="${dW(youtube)}">${dW(myName)}</a>
							</p>
						</div>
						<div class="flex space-x-3">
							<img class="w-3" src="public/icons/googlechrome.svg" alt="">
							<p class="text-coolGray-700">${dW(website)}</p>
						</div>
					</div>
				</div>
			</div>
		</div>
		</div>`}else{return``}};let loginPage=document.getElementById("loginPage");let formHead=document.getElementById("formhead");let formBody=document.getElementById("formbody");var copyright=document.getElementById("copyright");let content=document.getElementById("content");formHead.innerHTML=warningAttribute(1);const myForm=()=>{if(loginPage){const btnVoucher=document.getElementById("btnVoucher");const btnMember=document.getElementById("btnMember");let voucherActive=document.getElementById("voucherActive");let userVoucher=document.getElementById("userVoucher");let passVoucher=document.getElementById("passVoucher");let labelPassVoucher=document.getElementById("labelPassVoucher");passVoucher.hidden=true;labelPassVoucher.hidden=true;btnMember.classList.add("text-coolGray-500");btnVoucher.addEventListener("click",()=>{btnVoucher.classList.add("bg-white","text-lime-500");btnMember.classList.remove("bg-white","text-lime-500");btnMember.classList.add("text-coolGray-500");passVoucher.hidden=true;labelPassVoucher.hidden=true;voucherActive.value="1";passVoucher.value=""});btnMember.addEventListener("click",()=>{btnMember.classList.add("bg-white","text-lime-500");btnVoucher.classList.remove("bg-white","text-lime-500");btnVoucher.classList.add("text-coolGray-500");passVoucher.hidden=false;labelPassVoucher.hidden=false;voucherActive.value="0";passVoucher.value=""});userVoucher.onkeyup=setpass;function setpass(){if(voucherActive.value==1){var user=userVoucher.value;userVoucher.value=user;passVoucher.value=user}}let priceList=`<div class="grid grid-cols-${configData.paket.kolom} gap-3 p-1 px-3 py-3 overflow-x-auto border-t rounded-lg shadow-md border-lime-500 bg-coolGray-900">`;configData.paket.data.map(row=>{priceList+=`
				<div class="flex flex-col items-center justify-center px-3 py-1 rounded-md shadow-lg bg-sky-600">
					<p class="text-sm text-coolGray-800">${row.waktu}</p>
					<p class="text-sm font-semibold text-coolGray-800">${row.harga}</p>
				</div>`});priceList+=`</div>`;document.getElementById("priceList").innerHTML=priceList}};if(!winLoc.hostname){console.log("dilocal boleh edit")}else{if(winLoc.hostname==dW(yourData.lisensi).slice(0,-2)){console.log("lisensi ok");if(copyright){copyright.innerHTML=footerAttribute(1)}}else{console.log("lisensi not ok");if(copyright){copyright.innerHTML=footerAttribute(0)}}}if(!copyright){formBody.style.display="none";formHead.style.display="block";if(winLoc.hostname==dW(yourData.lisensi).slice(0,-2)){formBody.style.display="block";formHead.style.display="none";myForm()}}else{formBody.style.display="block";formHead.innerHTML=warningAttribute(0);copyright.classList.remove("hidden");copyright.removeAttribute("style");myForm();let kontak_alamat=document.getElementById("kontak_alamat");let kontak_hp=document.getElementById("kontak_hp");let kontak_email=document.getElementById("kontak_email");if(kontak_alamat){kontak_alamat.innerText=configData.kontak.alamat}if(kontak_hp){kontak_hp.innerText=configData.kontak.hp}if(kontak_email){kontak_email.innerText=configData.kontak.email}let isSlideText=document.getElementById("slideText");if(isSlideText){let slideText=`<div
			class="grid items-center justify-center grid-cols-1 border-2 border-dashed rounded-lg shadow-md border-lime-500 bg-coolGray-900 rounded-tr-50 h-28">
			<div class="px-3 py-3 space-y-1 leading-relaxed">`;configData.konten.map(row=>{slideText+=`
				<p class="text-sm text-center text-coolGray-400 text-arabic">${row.textArabic}</p>
				<p class="text-xs text-center text-coolGray-400">${row.textIndo}</p>
				<p class="text-xs text-center text-coolGray-400">${row.textRef}</p>
			`});slideText+=`</div></div>`;isSlideText.innerHTML=slideText}}moment.updateLocale("id",{});moment.locale("id");let masehi=moment().format("dddd")+", "+moment().format("DD MMMM YYYY");let hijriDate=hijri().format("iDD");let hijriMonth=iTranslate(hijri().format("iMMMM"));let hijriYear=hijri().format("iYYYY");let hijriah=`${hijriDate} ${hijriMonth} ${hijriYear} H`;function iTranslate(hijriName){let hijriahName=[{Muharram:"Muḥarram",Safar:"Shafar","Rabi' al-Awwal":"Rabī‘ul Awwal","Rabi' al-Thani":"Rabī‘ust Tsānī","Jumada al-Ula":"Jumādal Ūlā","Jumada al-Alkhirah":"Jumādal Ākhirah",Rajab:"Rajab","Sha’ban":"Sya‘bān",Ramadhan:"Ramadhan",Shawwal:"Syawwāl","Thul-Qi’dah":"Dzul Qa‘dah","Thul-Hijjah":"Dzul Ḥijjah"},{Muharram:"Muḥarram",Safar:"Safar","Rabi' al-Awwal":"Rabiul awal","Rabi' al-Thani":"Rabiul akhir","Jumada al-Ula":"Jumadil awal","Jumada al-Alkhirah":"Jumadil akhir",Rajab:"Rajab","Sha’ban":"Syaban",Ramadhan:"Ramadhan",Shawwal:"Syawal","Thul-Qi’dah":"Zulkaidah","Thul-Hijjah":"Zulhijah"}];return hijriahName[configData.prayTimes.hijriahNama][hijriName]}setInterval(()=>{let time=moment().format("HH:mm:ss");document.getElementById("time").innerText=time},1e3);document.getElementById("masehi").innerText=masehi;document.getElementById("hijriah").innerText=hijriah;let latitude=configData.prayTimes.latitude;let longitude=configData.prayTimes.longitude;let gmt=configData.prayTimes.gmt;let wifi_nama=configData.wifi_nama;let wifi_slogan=configData.wifi_slogan;let lokasi_nama=configData.lokasi_nama;document.getElementById("wifi_nama").innerText=wifi_nama;document.getElementById("wifi_slogan").innerText=wifi_slogan;let position={coords:{latitude:latitude,longitude:longitude}};successLocation(position);function successLocation(position){let lat=position.coords.latitude;let lng=position.coords.longitude;let prayTimes=new PrayerManager;prayTimes.method="Egypt";prayTimes.tune({sunrise:configData.prayTimes.tune.terbit,fajr:configData.prayTimes.tune.subuh,dhuhr:configData.prayTimes.tune.dzuhur,asr:configData.prayTimes.tune.ashar,maghrib:configData.prayTimes.tune.maghrib,isha:configData.prayTimes.tune.isya});let thisDay=prayTimes.getTimes(new Date,[lat,lng],gmt);let list=["Fajr","Sunrise","Dhuhr","Asr","Maghrib","Isha","Midnight"];let sunrise=thisDay[2].formatted;let fajr=thisDay[1].formatted;let dhuhr=thisDay[3].formatted;let asr=thisDay[4].formatted;let maghrib=thisDay[6].formatted;let isha=thisDay[7].formatted;document.getElementById("terbit").innerText=sunrise;document.getElementById("subuh").innerText=fajr;document.getElementById("dzuhur").innerText=dhuhr;document.getElementById("ashar").innerText=asr;document.getElementById("maghrib").innerText=maghrib;document.getElementById("isya").innerText=isha;let pergantianHijriah=0;setInterval(()=>{let today_date=moment().format("YYYY-MM-DD");let today=moment().format("x");let _maghrib=moment(`${today_date} ${maghrib}:00`).format("x");if(today>_maghrib&&pergantianHijriah==0){let hijriDate=hijri().add(1,"days").format("iDD");let hijriMonth=iTranslate(hijri().format("iMMMM"));let hijriYear=hijri().format("iYYYY");let hijriah=`${hijriDate} ${hijriMonth} ${hijriYear} H`;document.getElementById("hijriah").innerText=hijriah;pergantianHijriah=1}},1e3)}document.getElementById("location_name").innerText=lokasi_nama},{"crypto-js":11,moment:39,"moment-hijri":37,"moment/locale/id":38,"prayer-times.js":40}]},{},[41]);


File: /assets\js\config.js
let configData = {
  
  creator: { /* haram, hapus / edit data creator :D */
    name: "Erik Sanjaya",
    whatsapp: "https://wa.me/6289517000409",
    website: "https://eriksanjaya.com",
    youtube: "https://www.youtube.com/channel/UC1jSKHbhMg3JDZ-vFcXHTjQ",
    trakteer: "https://trakteer.id/eriksanjaya"
    /*
      dukung saya dengan subcribe,
      aktifkan tombol loncengnya, biar dapat notif template baru / update

      In Syaa Allah, kedepan saya akan update, 
      - pilihan warna template
      - slider text (info / konten)
      - running text
      - audio
      
      nb: boleh dishare, dilarang membajak template dan menjual kembali.
    */ 
  },

  /*
    lisensi free, wajib ada attribute kontak saya di semua halaman.
    jika ingin dihilangkan bisa trakteer saya kopi 15k.
    https://trakteer.id/eriksanjaya
  */ 
  
  lisensi: "free",

  wifi_nama: "MetaNET",
  wifi_slogan: "Internet Cepat, Unlimited.",
  
  lokasi_nama: "Dayeuhkolot, Bandung.",

  /*
    Dapatkan Latitude dan Longitude di sini.
    https://eriksanjaya.com/app/koordinat.html

    jika muncul pop up, klik ALLOW
    
    aktifkan GPS terlebih dahulu, jika via smartphone.
  */

  prayTimes: {
    latitude: -6.9238784,
    longitude: 107.6166656,
    gmt: 7, /* wib = 7, wita = 8, wit = 9 */

    hijriahNama: 1, /* 0 atau 1 */ 

    tune:{ // menyesuaikan jadwal sholat (tambah / kurangi)
      terbit: -4,
      subuh: -1,
      dzuhur: 1,
      ashar: 1,
      maghrib: 2,
      isya: 3,
    },
  },

  kontak: { // akan muncul jika lisensi non-free
    alamat: "Jalan Raya Laswi",
    hp: "0895-1700-0409",
    email: "halo@meta.net",
  },
  
  konten: [
    {
      textArabic: "يٰٓاَيُّهَا الَّذِيْنَ اٰمَنُوْا قُوْٓا اَنْفُسَكُمْ وَاَهْلِيْكُمْ نَارًا",
      textIndo: "Wahai orang-orang yang beriman! Peliharalah dirimu dan keluargamu dari api neraka",
      textRef: "QS. At Tahrim : 6",
    }
  ],

  paket: {
    kolom: 3, // 1 - 10
    data:  [
      {
        waktu: "1 Jam",
        harga: "Rp1200",
      },
      {
        waktu: "5 Jam",
        harga: "Rp3000",
      },
      {
        waktu: "1 Hari",
        harga: "Rp5000",
      },
      {
        waktu: "7 Hari",
        harga: "Rp15.000",
      },
      {
        waktu: "15 Hari",
        harga: "Rp30.000",
      },
      {
        waktu: "30 Hari",
        harga: "Rp50.000",
      }
    ],
  }

}

File: /assets\js\md5.js
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
function safe_add(x, y) {
  var lsw = (x & 0xFFFF) + (y & 0xFFFF)
  var msw = (x >> 16) + (y >> 16) + (lsw >> 16)
  return (msw << 16) | (lsw & 0xFFFF)
}

/*
 * Bitwise rotate a 32-bit number to the left.
 */
function rol(num, cnt) {
  return (num << cnt) | (num >>> (32 - cnt))
}

/*
 * These functions implement the four basic operations the algorithm uses.
 */
function cmn(q, a, b, x, s, t) {
  return safe_add(rol(safe_add(safe_add(a, q), safe_add(x, t)), s), b)
}
function ff(a, b, c, d, x, s, t) {
  return cmn((b & c) | ((~b) & d), a, b, x, s, t)
}
function gg(a, b, c, d, x, s, t) {
  return cmn((b & d) | (c & (~d)), a, b, x, s, t)
}
function hh(a, b, c, d, x, s, t) {
  return cmn(b ^ c ^ d, a, b, x, s, t)
}
function ii(a, b, c, d, x, s, t) {
  return cmn(c ^ (b | (~d)), a, b, x, s, t)
}

/*
 * Calculate the MD5 of an array of little-endian words, producing an array
 * of little-endian words.
 */
function coreMD5(x) {
  var a = 1732584193
  var b = -271733879
  var c = -1732584194
  var d = 271733878

  for (i = 0; i < x.length; i += 16) {
    var olda = a
    var oldb = b
    var oldc = c
    var oldd = d

    a = ff(a, b, c, d, x[i + 0], 7, -680876936)
    d = ff(d, a, b, c, x[i + 1], 12, -389564586)
    c = ff(c, d, a, b, x[i + 2], 17, 606105819)
    b = ff(b, c, d, a, x[i + 3], 22, -1044525330)
    a = ff(a, b, c, d, x[i + 4], 7, -176418897)
    d = ff(d, a, b, c, x[i + 5], 12, 1200080426)
    c = ff(c, d, a, b, x[i + 6], 17, -1473231341)
    b = ff(b, c, d, a, x[i + 7], 22, -45705983)
    a = ff(a, b, c, d, x[i + 8], 7, 1770035416)
    d = ff(d, a, b, c, x[i + 9], 12, -1958414417)
    c = ff(c, d, a, b, x[i + 10], 17, -42063)
    b = ff(b, c, d, a, x[i + 11], 22, -1990404162)
    a = ff(a, b, c, d, x[i + 12], 7, 1804603682)
    d = ff(d, a, b, c, x[i + 13], 12, -40341101)
    c = ff(c, d, a, b, x[i + 14], 17, -1502002290)
    b = ff(b, c, d, a, x[i + 15], 22, 1236535329)

    a = gg(a, b, c, d, x[i + 1], 5, -165796510)
    d = gg(d, a, b, c, x[i + 6], 9, -1069501632)
    c = gg(c, d, a, b, x[i + 11], 14, 643717713)
    b = gg(b, c, d, a, x[i + 0], 20, -373897302)
    a = gg(a, b, c, d, x[i + 5], 5, -701558691)
    d = gg(d, a, b, c, x[i + 10], 9, 38016083)
    c = gg(c, d, a, b, x[i + 15], 14, -660478335)
    b = gg(b, c, d, a, x[i + 4], 20, -405537848)
    a = gg(a, b, c, d, x[i + 9], 5, 568446438)
    d = gg(d, a, b, c, x[i + 14], 9, -1019803690)
    c = gg(c, d, a, b, x[i + 3], 14, -187363961)
    b = gg(b, c, d, a, x[i + 8], 20, 1163531501)
    a = gg(a, b, c, d, x[i + 13], 5, -1444681467)
    d = gg(d, a, b, c, x[i + 2], 9, -51403784)
    c = gg(c, d, a, b, x[i + 7], 14, 1735328473)
    b = gg(b, c, d, a, x[i + 12], 20, -1926607734)

    a = hh(a, b, c, d, x[i + 5], 4, -378558)
    d = hh(d, a, b, c, x[i + 8], 11, -2022574463)
    c = hh(c, d, a, b, x[i + 11], 16, 1839030562)
    b = hh(b, c, d, a, x[i + 14], 23, -35309556)
    a = hh(a, b, c, d, x[i + 1], 4, -1530992060)
    d = hh(d, a, b, c, x[i + 4], 11, 1272893353)
    c = hh(c, d, a, b, x[i + 7], 16, -155497632)
    b = hh(b, c, d, a, x[i + 10], 23, -1094730640)
    a = hh(a, b, c, d, x[i + 13], 4, 681279174)
    d = hh(d, a, b, c, x[i + 0], 11, -358537222)
    c = hh(c, d, a, b, x[i + 3], 16, -722521979)
    b = hh(b, c, d, a, x[i + 6], 23, 76029189)
    a = hh(a, b, c, d, x[i + 9], 4, -640364487)
    d = hh(d, a, b, c, x[i + 12], 11, -421815835)
    c = hh(c, d, a, b, x[i + 15], 16, 530742520)
    b = hh(b, c, d, a, x[i + 2], 23, -995338651)

    a = ii(a, b, c, d, x[i + 0], 6, -198630844)
    d = ii(d, a, b, c, x[i + 7], 10, 1126891415)
    c = ii(c, d, a, b, x[i + 14], 15, -1416354905)
    b = ii(b, c, d, a, x[i + 5], 21, -57434055)
    a = ii(a, b, c, d, x[i + 12], 6, 1700485571)
    d = ii(d, a, b, c, x[i + 3], 10, -1894986606)
    c = ii(c, d, a, b, x[i + 10], 15, -1051523)
    b = ii(b, c, d, a, x[i + 1], 21, -2054922799)
    a = ii(a, b, c, d, x[i + 8], 6, 1873313359)
    d = ii(d, a, b, c, x[i + 15], 10, -30611744)
    c = ii(c, d, a, b, x[i + 6], 15, -1560198380)
    b = ii(b, c, d, a, x[i + 13], 21, 1309151649)
    a = ii(a, b, c, d, x[i + 4], 6, -145523070)
    d = ii(d, a, b, c, x[i + 11], 10, -1120210379)
    c = ii(c, d, a, b, x[i + 2], 15, 718787259)
    b = ii(b, c, d, a, x[i + 9], 21, -343485551)

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
function binl2hex(binarray) {
  var hex_tab = "0123456789abcdef"
  var str = ""
  for (var i = 0; i < binarray.length * 4; i++) {
    str += hex_tab.charAt((binarray[i >> 2] >> ((i % 4) * 8 + 4)) & 0xF) +
      hex_tab.charAt((binarray[i >> 2] >> ((i % 4) * 8)) & 0xF)
  }
  return str
}

/*
 * Convert an array of little-endian words to a base64 encoded string.
 */
function binl2b64(binarray) {
  var tab = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
  var str = ""
  for (var i = 0; i < binarray.length * 32; i += 6) {
    str += tab.charAt(((binarray[i >> 5] << (i % 32)) & 0x3F) |
      ((binarray[i >> 5 + 1] >> (32 - i % 32)) & 0x3F))
  }
  return str
}

/*
 * Convert an 8-bit character string to a sequence of 16-word blocks, stored
 * as an array, and append appropriate padding for MD4/5 calculation.
 * If any of the characters are >255, the high byte is silently ignored.
 */
function str2binl(str) {
  var nblk = ((str.length + 8) >> 6) + 1 // number of 16-word blocks
  var blks = new Array(nblk * 16)
  for (var i = 0; i < nblk * 16; i++) blks[i] = 0
  for (var i = 0; i < str.length; i++)
    blks[i >> 2] |= (str.charCodeAt(i) & 0xFF) << ((i % 4) * 8)
  blks[i >> 2] |= 0x80 << ((i % 4) * 8)
  blks[nblk * 16 - 2] = str.length * 8
  return blks
}

/*
 * Convert a wide-character string to a sequence of 16-word blocks, stored as
 * an array, and append appropriate padding for MD4/5 calculation.
 */
function strw2binl(str) {
  var nblk = ((str.length + 4) >> 5) + 1 // number of 16-word blocks
  var blks = new Array(nblk * 16)
  for (var i = 0; i < nblk * 16; i++) blks[i] = 0
  for (var i = 0; i < str.length; i++)
    blks[i >> 1] |= str.charCodeAt(i) << ((i % 2) * 16)
  blks[i >> 1] |= 0x80 << ((i % 2) * 16)
  blks[nblk * 16 - 2] = str.length * 16
  return blks
}

/*
 * External interface
 */
function hexMD5(str) { return binl2hex(coreMD5(str2binl(str))) }
function hexMD5w(str) { return binl2hex(coreMD5(strw2binl(str))) }
function b64MD5(str) { return binl2b64(coreMD5(str2binl(str))) }
function b64MD5w(str) { return binl2b64(coreMD5(strw2binl(str))) }
/* Backward compatibility */
function calcMD5(str) { return binl2hex(coreMD5(str2binl(str))) }


File: /error.html
<html>

<head>
	<title>mikrotik hotspot > error</title>
	<meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1">
	<meta http-equiv="pragma" content="no-cache">
	<meta http-equiv="expires" content="-1">
	<style type="text/css">
		<!--
		textarea,
		input,
		select {
			background-color: #FDFBFB;
			border: 1px #BBBBBB solid;
			padding: 2px;
			margin: 1px;
			font-size: 14px;
			color: #808080;
		}

		body {
			color: #737373;
			font-size: 12px;
			font-family: verdana;
		}

		a,
		a:link,
		a:visited,
		a:active {
			color: #AAAAAA;
			text-decoration: none;
			font-size: 12px;
		}

		a:hover {
			border-bottom: 1px dotted #c1c1c1;
			color: #AAAAAA;
		}

		img {
			border: none;
		}

		td {
			font-size: 12px;
			color: #7A7A7A;
		}
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

File: /login.html
<!DOCTYPE html>
<html>

<head>
	<meta charSet="utf-8" />
	<meta name="viewport" content="width=device-width" />
	<meta http-equiv="Cache-Control" content="no-cache, no-store, must-revalidate" />
	<meta http-equiv="Pragma" content="no-cache" />
	<meta name="theme-color" content="#1F2937" />
	<meta http-equiv="Expires" content="-1" />
	<link rel="stylesheet" href="assets/css/app.css" />
	<title>Home</title>
	<style>
		.bg {
			background-color: #15375C;
			background-image: url(public/images/bg-01.jpg);
			background-position: bottom right;
			background-repeat: no-repeat;
			background-size: cover;
		}

		.overlay {
			background-color: rgba(0, 0, 0, 0.8);
			top: 0;
			left: 0;
			width: 100%;
			height: 100%;
			position: relative;
			z-index: 3;
		}
	</style>
</head>

<body>
	<div id="loginPage" class="container h-screen max-w-full">
		<div class="flex justify-center h-full max-w-full py-3 bg-coolGray-700">

			<div class="grid w-screen grid-rows-5 mx-3 overflow-y-auto shadow-md md:w-1/3 lg:1/3 xl:1/3 rounded-3xl">

				<!-- <div class="grid grid-cols-1 row-span-2 bg-coolGray-100"> -->
				<div class="grid grid-cols-1 row-span-2 bg-sky-600">
					<div class="flex flex-col justify-center bg-blueGray-800 rounded-bl-50">
						<div class="flex-col px-3 space-y-2">
							<div class="flex items-center space-x-3">
								<div
									class="flex flex-col items-center justify-center w-16 h-16 rounded-full rounded-tr-none bg-sky-600">
									<svg xmlns="http://www.w3.org/2000/svg" class="w-8 h-8 text-coolGray-100" fill="none"
										viewBox="0 0 24 24" stroke="currentColor">
										<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
											d="M8.111 16.404a5.5 5.5 0 017.778 0M12 20h.01m-7.08-7.071c3.904-3.905 10.236-3.905 14.141 0M1.394 9.393c5.857-5.857 15.355-5.857 21.213 0" />
									</svg>
								</div>
								<div class="flex flex-col">
									<p id="wifi_nama" class="text-xl text-coolGray-300">MetaNet</p>
									<p id="wifi_slogan" class="text-coolGray-300">Internet Cepat, Unlimited.</p>
								</div>
							</div>
							<!-- <div class="px-2 py-2 bg-white bg-opacity-50 border-l-4 rounded-md shadow-md border-cyan-600">
								<p class="text-xs text-coolGray-500">Musim hujan nih, jika ada petir, wifi akan kami matikan.</p>
							</div> -->
						</div>

						<div class="flex items-center justify-between px-3 pt-3">
							<div class="flex-none">
								<p id="masehi" class="text-sm antialiased font-semibold text-lime-500"></p>
								<p id="hijriah" class="text-sm antialiased font-semibold text-coolGray-300"></p>
							</div>
							<p id="time" class="text-3xl antialiased font-light text-lime-500"></p>
						</div>

						<div class="flex justify-end">
							<svg class="w-4 h-4 mt-3 stroke-current text-coolGray-300 animate-bounce"
								xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor">
								<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
									d="M17.657 16.657L13.414 20.9a1.998 1.998 0 01-2.827 0l-4.244-4.243a8 8 0 1111.314 0z"></path>
								<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
									d="M15 11a3 3 0 11-6 0 3 3 0 016 0z">
								</path>
							</svg>
							<p id="location_name" class="px-3 pt-3 pb-3 text-xs font-semibold text-right text-coolGray-300"></p>
						</div>


						<div class="grid grid-cols-6 gap-1 px-3 sm:gap-3">
							<div
								class="flex flex-col items-center justify-center h-20 py-1 text-center border-2 border-solid rounded-full shadow-md border-lime-500 sm:h-24">
								<p class="text-xs antialiased font-light text-opacity-100 text-coolGray-300 ">Terbit</p>
								<p id="terbit" class="text-sm antialiased font-semibold text-coolGray-300 text-opacity-90"></p>
							</div>
							<div
								class="flex flex-col items-center justify-center h-20 py-1 text-center border-2 border-solid rounded-full shadow-md border-lime-500 sm:h-24">
								<p class="text-xs antialiased font-light text-opacity-100 text-coolGray-300 ">Subuh</p>
								<p id="subuh" class="text-sm antialiased font-semibold text-coolGray-300 text-opacity-90"></p>
							</div>
							<div
								class="flex flex-col items-center justify-center h-20 py-1 text-center border-2 border-solid rounded-full shadow-md border-lime-500 sm:h-24">
								<p class="text-xs antialiased font-light text-opacity-100 text-coolGray-300 ">Dzuhur</p>
								<p id="dzuhur" class="text-sm antialiased font-semibold text-coolGray-300 text-opacity-90"></p>
							</div>
							<div
								class="flex flex-col items-center justify-center h-20 py-1 text-center border-2 border-solid rounded-full shadow-md border-lime-500 sm:h-24">
								<p class="text-xs antialiased font-light text-opacity-100 text-coolGray-300 ">Ashar</p>
								<p id="ashar" class="text-sm antialiased font-semibold text-coolGray-300 text-opacity-90"></p>
							</div>
							<div
								class="flex flex-col items-center justify-center h-20 py-1 text-center border-2 border-solid rounded-full shadow-md border-lime-500 sm:h-24">
								<p class="text-xs antialiased font-light text-opacity-100 text-coolGray-300 ">Maghrib</p>
								<p id="maghrib" class="text-sm antialiased font-semibold text-coolGray-300 text-opacity-90"></p>
							</div>
							<div
								class="flex flex-col items-center justify-center h-20 py-1 text-center border-2 border-solid rounded-full shadow-md border-lime-500 sm:h-24">
								<p class="text-xs antialiased font-light text-opacity-100 text-coolGray-300 ">Isya</p>
								<p id="isya" class="text-sm antialiased font-semibold text-coolGray-300 text-opacity-90"></p>
							</div>
						</div>

					</div>
				</div>

				<!-- <div class="grid grid-cols-1 bg-black bg-opacity-80"> -->
				<div class="grid grid-cols-1 bg-blueGray-800">
					<!-- <div class="bg-coolGray-100 rounded-tr-50"> -->
					<div class="px-3 py-3 h-8/12 bg-sky-600 rounded-tr-50">
						<div id="content"
							class="h-full px-3 pb-3 space-y-3 overflow-hidden bg-opacity-100 bg-coolGray-800 rounded-t-xl rounded-b-3xl rounded-tr-50">

							<div id="formhead"></div>

							<div id="formbody" class="space-y-3">

								<div id="slideText">

								</div>

								<div>
									$(if chap-id)
									<form name="sendin" action="$(link-login-only)" method="post">
										<input type="hidden" name="username" />
										<input type="hidden" name="password" />
										<input type="hidden" name="dst" value="$(link-orig)" />
										<input type="hidden" name="popup" value="true" />
									</form>

									<script type="text/javascript" src="assets/js/md5.js"></script>
									<script type="text/javascript">
										function doLogin() {
											document.sendin.username.value = document.login.username.value;
											document.sendin.password.value = hexMD5('$(chap-id)' + document.login.password.value + '$(chap-challenge)');
											document.sendin.submit();
											return false;
										}
									</script>
									$(endif)

									<div align="center">
										<a href="$(link-login-only)?target=lv&amp;dst=$(link-orig-esc)"></a>
									</div>

									$(if trial == 'yes')
									<a class="text-coolGray-600" href="$(link-login-only)?dst=$(link-orig-esc)&amp;username=T-$(mac-esc)">
										<div class="py-3 text-center rounded-md shadow-md bg-gradient-to-r from-cyan-600 to-teal-500">
											Free Trial
										</div>
									</a>
									$(endif)
								</div>

								<div
									class="grid items-center justify-center grid-cols-2 p-1 space-x-1 border-t rounded-lg shadow-md border-lime-500 bg-coolGray-900">
									<button id="btnVoucher"
										class="px-3 py-3 text-xs bg-white rounded-lg shadow-md text-lime-500 bg-opacity-10 focus:placeholder-transparent focus:outline-none">Voucher</button>
									<button id="btnMember"
										class="px-3 py-3 text-xs rounded-lg shadow-md bg-opacity-10 focus:placeholder-transparent focus:outline-none">Member</button>
								</div>

								<form name="login" action="$(link-login-only)" method="post" $(if chap-id) onSubmit="return doLogin()"
									$(endif)>
									<input type="hidden" name="dst" value="$(link-orig)" />
									<input type="hidden" name="popup" value="true" />

									<div
										class="flex flex-col px-3 py-3 space-y-2 border-t rounded-lg shadow-md border-lime-500 bg-coolGray-900">
										<input type="hidden" id="voucherActive" value="1">


										<div class="flex flex-col">
											<label class="text-sm text-coolGray-400">Username</label>
											<input name="username" id="userVoucher" value="$(username)"
												class="px-3 py-3 text-sm border-l rounded-lg shadow-md focus:outline-none border-sky-600 text-sky-600 bg-coolGray-800 placeholder-coolGray-500"
												type="text" placeholder="Username">
										</div>

										<div class="flex flex-col">
											<label id="labelPassVoucher" class="text-sm text-coolGray-400">Password</label>
											<input name="password" id="passVoucher"
												class="px-3 py-3 text-sm border-l rounded-lg shadow-md border-sky-600 text-sky-600 bg-coolGray-800 placeholder-coolGray-500 focus:outline-none"
												type="text" placeholder="Password">
										</div>

										$(if error)
										<div
											class="flex px-3 py-3 border-l border-red-400 rounded-lg shadow-md bg-coolGray-500 bg-opacity-20">
											<p class="text-sm text-red-400">$(error)</p>
										</div>
										$(endif)

										<div class="flex flex-col py-2">
											<button type="submit"
												class="flex items-center justify-center px-3 py-3 rounded-lg shadow-2xl bg-coolGray-800 bg-opacity-10 text-md ring-1 ring-sky-600 focus:bg-opacity-5">
												<p class="antialiased font-normal text-sky-600">Login</p>
											</button>
										</div>
									</div>
								</form>

								<div id="priceList"></div>
								<div id="copyright"></div>

							</div>

						</div>
					</div>
				</div>

			</div>
		</div>
	</div>

	<script src="assets/js/config.js"></script>
	<script src="assets/js/app.js"></script>
</body>

</html>

File: /logout.html
<!DOCTYPE html>
<html>

<head>
	<meta charSet="utf-8" />
	<meta name="viewport" content="width=device-width" />
	<meta http-equiv="Cache-Control" content="no-cache, no-store, must-revalidate" />
	<meta http-equiv="Pragma" content="no-cache" />
	<meta name="theme-color" content="#1F2937" />
	<meta http-equiv="Expires" content="-1" />
	<link rel="stylesheet" href="assets/css/app.css" />
	<title>Logout</title>
</head>

<body>

	<script language="JavaScript">
		// < !--
		function openLogin() {
			if (window.name != 'hotspot_logout') return true;
			open('$(link-login)', '_blank', '');
			window.close();
			return false;
		}
		//-->
	</script>
	<div class="container h-screen max-w-full">
		<div class="flex justify-center h-full max-w-full py-3 bg-coolGray-700">

			<div class="grid w-screen grid-rows-5 mx-3 overflow-y-auto shadow-md md:w-1/3 lg:1/3 xl:1/3 rounded-3xl">

				<!-- <div class="grid grid-cols-1 row-span-2 bg-coolGray-100"> -->
				<div class="grid grid-cols-1 row-span-2 bg-sky-600">
					<div class="flex flex-col justify-center bg-blueGray-800 rounded-bl-50">
						<div class="flex-col px-3 space-y-2">
							<div class="flex items-center space-x-3">
								<div
									class="flex flex-col items-center justify-center w-16 h-16 rounded-full rounded-tr-none bg-sky-600">
									<svg xmlns="http://www.w3.org/2000/svg" class="w-8 h-8 text-coolGray-100" fill="none"
										viewBox="0 0 24 24" stroke="currentColor">
										<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
											d="M8.111 16.404a5.5 5.5 0 017.778 0M12 20h.01m-7.08-7.071c3.904-3.905 10.236-3.905 14.141 0M1.394 9.393c5.857-5.857 15.355-5.857 21.213 0" />
									</svg>
								</div>
								<div class="flex flex-col">
									<p id="wifi_nama" class="text-xl text-coolGray-300">MetaNet</p>
									<p id="wifi_slogan" class="text-coolGray-300">Internet Cepat, Unlimited.</p>
								</div>
							</div>
							<!-- <div class="px-2 py-2 bg-white bg-opacity-50 border-l-4 rounded-md shadow-md border-cyan-600">
									<p class="text-xs text-coolGray-500">Musim hujan nih, jika ada petir, wifi akan kami matikan.</p>
								</div> -->
						</div>

						<div class="flex items-center justify-between px-3 pt-3">
							<div class="flex-none">
								<p id="masehi" class="text-sm antialiased font-semibold text-lime-500"></p>
								<p id="hijriah" class="text-sm antialiased font-semibold text-coolGray-300"></p>
							</div>
							<p id="time" class="text-3xl antialiased font-light text-lime-500"></p>
						</div>

						<div class="flex justify-end">
							<svg class="w-4 h-4 mt-3 stroke-current text-coolGray-300 animate-bounce"
								xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor">
								<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
									d="M17.657 16.657L13.414 20.9a1.998 1.998 0 01-2.827 0l-4.244-4.243a8 8 0 1111.314 0z"></path>
								<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
									d="M15 11a3 3 0 11-6 0 3 3 0 016 0z">
								</path>
							</svg>
							<p id="location_name" class="px-3 pt-3 pb-3 text-xs font-semibold text-right text-coolGray-300"></p>
						</div>


						<div class="grid grid-cols-6 gap-1 px-3 sm:gap-3">
							<div
								class="flex flex-col items-center justify-center h-20 py-1 text-center border-2 border-solid rounded-full shadow-md border-lime-500 sm:h-24">
								<p class="text-xs antialiased font-light text-opacity-100 text-coolGray-300 ">Terbit</p>
								<p id="terbit" class="text-sm antialiased font-semibold text-coolGray-300 text-opacity-90"></p>
							</div>
							<div
								class="flex flex-col items-center justify-center h-20 py-1 text-center border-2 border-solid rounded-full shadow-md border-lime-500 sm:h-24">
								<p class="text-xs antialiased font-light text-opacity-100 text-coolGray-300 ">Subuh</p>
								<p id="subuh" class="text-sm antialiased font-semibold text-coolGray-300 text-opacity-90"></p>
							</div>
							<div
								class="flex flex-col items-center justify-center h-20 py-1 text-center border-2 border-solid rounded-full shadow-md border-lime-500 sm:h-24">
								<p class="text-xs antialiased font-light text-opacity-100 text-coolGray-300 ">Dzuhur</p>
								<p id="dzuhur" class="text-sm antialiased font-semibold text-coolGray-300 text-opacity-90"></p>
							</div>
							<div
								class="flex flex-col items-center justify-center h-20 py-1 text-center border-2 border-solid rounded-full shadow-md border-lime-500 sm:h-24">
								<p class="text-xs antialiased font-light text-opacity-100 text-coolGray-300 ">Ashar</p>
								<p id="ashar" class="text-sm antialiased font-semibold text-coolGray-300 text-opacity-90"></p>
							</div>
							<div
								class="flex flex-col items-center justify-center h-20 py-1 text-center border-2 border-solid rounded-full shadow-md border-lime-500 sm:h-24">
								<p class="text-xs antialiased font-light text-opacity-100 text-coolGray-300 ">Maghrib</p>
								<p id="maghrib" class="text-sm antialiased font-semibold text-coolGray-300 text-opacity-90"></p>
							</div>
							<div
								class="flex flex-col items-center justify-center h-20 py-1 text-center border-2 border-solid rounded-full shadow-md border-lime-500 sm:h-24">
								<p class="text-xs antialiased font-light text-opacity-100 text-coolGray-300 ">Isya</p>
								<p id="isya" class="text-sm antialiased font-semibold text-coolGray-300 text-opacity-90"></p>
							</div>
						</div>

					</div>
				</div>

				<!-- <div class="grid grid-cols-1 bg-black bg-opacity-80"> -->
				<div class="grid grid-cols-1 bg-blueGray-800">
					<!-- <div class="bg-coolGray-100 rounded-tr-50"> -->
					<div class="px-3 py-3 bg-sky-600 rounded-tr-50">
						<div id="content"
							class="h-full px-3 py-3 pb-3 space-y-3 overflow-hidden bg-opacity-100 bg-coolGray-800 rounded-t-xl rounded-b-3xl rounded-tr-50">

							<div id="formhead"></div>

							<div id="formbody" class="space-y-3">

								<div id="slideText">

								</div>

								<div
									class="grid items-center justify-center grid-cols-1 p-1 space-x-1 border-t rounded-lg shadow-md border-lime-500 bg-coolGray-900">
									<div class="px-3 py-3">
										<p class="text-sm antialiased font-medium text-red-400">
											Anda berhasil logout
										</p>
									</div>
								</div>

								<div
									class="grid items-center justify-center grid-cols-1 p-1 space-x-1 border-l rounded-lg shadow-md border-lime-500 bg-coolGray-900">

									<div class="px-3 py-3">

										<table class="text-sm antialiased text-red-400">
											<tr>
												<td width="110">Username</td>
												$(if login-by == 'trial')
												<td>: Trial</td>
												$(elif login-by != 'mac')
												<td>: $(username)</td>
												$(endif)
											</tr>
											<tr>
												<td>IP Address</td>
												<td>: $(ip)</td>
											</tr>
											<tr>
												<td>Upload</td>
												<td>: $(bytes-in-nice)</td>
											</tr>
											<tr>
												<td>Download</td>
												<td>: $(bytes-out-nice)</td>
											</tr>
											$(if session-time-left)
											<tr>
												<td>Sisa Waktu</td>
												<td>: $(session-time-left)</td>
											</tr>
											$(else)
											<tr>
												<td>Tersambung</td>
												<td>: $(uptime)</td>
											</tr>
											$(endif)
											<tr>
												<td>Status Refresh</td>
												<td>: $(refresh-timeout)</td>
											</tr>
										</table>
									</div>
								</div>

								<div>
									<a href="./login.html">
										<div class="grid grid-cols-1 gap-2">
											<button type="submit"
												class="flex items-center justify-center px-3 py-3 rounded-lg shadow-2xl bg-coolGray-800 bg-opacity-10 text-md ring-1 ring-sky-600 focus:bg-opacity-5">
												<p class="antialiased font-normal text-sky-600">Login</p>
											</button>
										</div>
									</a>
								</div>
								<div id="copyright"></div>
							</div>
						</div>
					</div>

				</div>
			</div>
		</div>
	</div>

	<script src="assets/js/config.js"></script>
	<script src="assets/js/app.js"></script>
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
		textarea,
		input,
		select {
			background-color: #FDFBFB;
			border: 1px #BBBBBB solid;
			padding: 2px;
			margin: 1px;
			font-size: 14px;
			color: #808080;
		}

		body {
			color: #737373;
			font-size: 12px;
			font-family: verdana;
		}

		a,
		a:link,
		a:visited,
		a:active {
			color: #AAAAAA;
			text-decoration: none;
			font-size: 12px;
		}

		a:hover {
			border-bottom: 1px dotted #c1c1c1;
			color: #AAAAAA;
		}

		img {
			border: none;
		}

		td {
			font-size: 12px;
			color: #7A7A7A;
		}
		-->
	</style>
	<script language="JavaScript">
< !--
    var popup = '';
		function openOrig() {
			if (window.focus) popup.focus();
			location.href = '$(link-orig)';
		}
		function openAd() {
			location.href = '$(link-redirect)';
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

File: /README.md
### template-login-hotspot-mikrotik-02
Template login hotspot Mikrotik Freemium [Erik Sanjaya](https://github.com/eriiksanjaya)

#### Lihat Demo
[Youtube](https://www.youtube.com/watch?v=j2ffHxSmaJ4)

#### Download
[Download Template](https://github.com/eriiksanjaya/template-login-hotspot-mikrotik-02/archive/refs/heads/main.zip)

>**Template ini Freemium, untuk yang gratis, atribut wajib ada**

#### Konfigurasi
untuk melakukan configurasi template, edit file config.js
file tersebut berada di folder assets/js/config.js

#### assets/js/config.js
      Contoh : 
      ```let configData = {
        
        creator: { /* haram, hapus / edit data creator :D */
          name: "Erik Sanjaya",
          whatsapp: "https://wa.me/6289517000409",
          website: "https://eriksanjaya.com",
          youtube: "https://www.youtube.com/channel/UC1jSKHbhMg3JDZ-vFcXHTjQ",
          trakteer: "https://trakteer.id/eriksanjaya"
          /*
            dukung saya dengan subcribe,
            aktifkan tombol loncengnya, biar dapat notif template baru / update

            In Syaa Allah, kedepan saya akan update, 
            - pilihan warna template
            - slider text (info / konten)
            - running text
            - audio
            
            nb: boleh dishare, dilarang membajak template dan menjual kembali.
          */ 
        },

        /*
          lisensi free, wajib ada attribute kontak saya di semua halaman.
          jika ingin dihilangkan bisa trakteer saya kopi 15k.
          https://trakteer.id/eriksanjaya
        */ 
        
        lisensi: "free",

        wifi_nama: "MetaNET",
        wifi_slogan: "Internet Cepat, Unlimited.",
        
        lokasi_nama: "Dayeuhkolot, Bandung.",

        /*
          Dapatkan Latitude dan Longitude di sini.
          https://eriksanjaya.com/app/koordinat.html

          jika muncul pop up, klik ALLOW
          
          aktifkan GPS terlebih dahulu, jika via smartphone.
        */

        prayTimes: {
          latitude: -6.9238784,
          longitude: 107.6166656,
          gmt: 7, /* wib = 7, wita = 8, wit = 9 */

          hijriahNama: 1, /* 0 atau 1 */ 

          tune:{ // menyesuaikan jadwal sholat (tambah / kurangi)
            terbit: -4,
            subuh: -1,
            dzuhur: 1,
            ashar: 1,
            maghrib: 2,
            isya: 3,
          },
        },

        kontak: { // akan muncul jika lisensi non-free
          alamat: "Jalan Raya Laswi",
          hp: "0895-1700-0409",
          email: "halo@meta.net",
        },
        
        konten: [
          {
            textArabic: "يٰٓاَيُّهَا الَّذِيْنَ اٰمَنُوْا قُوْٓا اَنْفُسَكُمْ وَاَهْلِيْكُمْ نَارًا",
            textIndo: "Wahai orang-orang yang beriman! Peliharalah dirimu dan keluargamu dari api neraka",
            textRef: "QS. At Tahrim : 6",
          }
        ],

        paket: {
          kolom: 3, // 1 - 10
          data:  [
            {
              waktu: "1 Jam",
              harga: "Rp1200",
            },
            {
              waktu: "5 Jam",
              harga: "Rp3000",
            },
            {
              waktu: "1 Hari",
              harga: "Rp5000",
            },
            {
              waktu: "7 Hari",
              harga: "Rp15.000",
            },
            {
              waktu: "15 Hari",
              harga: "Rp30.000",
            },
            {
              waktu: "30 Hari",
              harga: "Rp50.000",
            }
          ],
        }
      }```

#### Screenshoot
<img width="200" src="https://eriksanjaya.com/public/images/hotspot/02/hs001.jpeg" />
<img width="200" src="https://eriksanjaya.com/public/images/hotspot/02/hs002.jpeg" />
<img width="200" src="https://eriksanjaya.com/public/images/hotspot/02/hs003.jpeg" />
<img width="200" src="https://eriksanjaya.com/public/images/hotspot/02/hs004.jpeg" />

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
  <meta charSet="utf-8" />
  $(if refresh-timeout)
  <meta http-equiv="refresh" content="$(refresh-timeout-secs)">
  $(endif)
  <meta name="viewport" content="width=device-width" />
  <meta http-equiv="Cache-Control" content="no-cache, no-store, must-revalidate" />
  <meta http-equiv="Pragma" content="no-cache" />
  <meta name="theme-color" content="#1F2937" />
  <meta http-equiv="Expires" content="-1" />
  <link rel="stylesheet" href="assets/css/app.css" />
  <title>Status</title>
  <style>
    .bg {
      background-color: #15375C;
      background-image: url(public/images/bg-01.jpg);
      background-position: bottom right;
      background-repeat: no-repeat;
      background-size: cover;
    }

    .overlay {
      background-color: rgba(0, 0, 0, 0.8);
      top: 0;
      left: 0;
      width: 100%;
      height: 100%;
      position: relative;
      z-index: 3;
    }
  </style>

  <script language="JavaScript">
  < !--
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
  //-->
  </script>

</head>

<body>
  <div class="container h-screen max-w-full">
    <div class="flex justify-center h-full max-w-full py-3 bg-coolGray-700">

      <div class="grid w-screen grid-rows-5 mx-3 overflow-y-auto shadow-md md:w-1/3 lg:1/3 xl:1/3 rounded-3xl">

        <!-- <div class="grid grid-cols-1 row-span-2 bg-coolGray-100"> -->
        <div class="grid grid-cols-1 row-span-2 bg-sky-600">
          <div class="flex flex-col justify-center bg-blueGray-800 rounded-bl-50">
            <div class="flex-col px-3 space-y-2">
              <div class="flex items-center space-x-3">
                <div
                  class="flex flex-col items-center justify-center w-16 h-16 rounded-full rounded-tr-none bg-sky-600">
                  <svg xmlns="http://www.w3.org/2000/svg" class="w-8 h-8 text-coolGray-100" fill="none"
                    viewBox="0 0 24 24" stroke="currentColor">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                      d="M8.111 16.404a5.5 5.5 0 017.778 0M12 20h.01m-7.08-7.071c3.904-3.905 10.236-3.905 14.141 0M1.394 9.393c5.857-5.857 15.355-5.857 21.213 0" />
                  </svg>
                </div>
                <div class="flex flex-col">
                  <p id="wifi_nama" class="text-xl text-coolGray-300">MetaNet</p>
                  <p id="wifi_slogan" class="text-coolGray-300">Internet Cepat, Unlimited.</p>
                </div>
              </div>
              <!-- <div class="px-2 py-2 bg-white bg-opacity-50 border-l-4 rounded-md shadow-md border-cyan-600">
                  <p class="text-xs text-coolGray-500">Musim hujan nih, jika ada petir, wifi akan kami matikan.</p>
                </div> -->
            </div>

            <div class="flex items-center justify-between px-3 pt-3">
              <div class="flex-none">
                <p id="masehi" class="text-sm antialiased font-semibold text-lime-500"></p>
                <p id="hijriah" class="text-sm antialiased font-semibold text-coolGray-300"></p>
              </div>
              <p id="time" class="text-3xl antialiased font-light text-lime-500"></p>
            </div>

            <div class="flex justify-end">
              <svg class="w-4 h-4 mt-3 stroke-current text-coolGray-300 animate-bounce"
                xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                  d="M17.657 16.657L13.414 20.9a1.998 1.998 0 01-2.827 0l-4.244-4.243a8 8 0 1111.314 0z"></path>
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                  d="M15 11a3 3 0 11-6 0 3 3 0 016 0z">
                </path>
              </svg>
              <p id="location_name" class="px-3 pt-3 pb-3 text-xs font-semibold text-right text-coolGray-300"></p>
            </div>


            <div class="grid grid-cols-6 gap-1 px-3 sm:gap-3">
              <div
                class="flex flex-col items-center justify-center h-20 py-1 text-center border-2 border-solid rounded-full shadow-md border-lime-500 sm:h-24">
                <p class="text-xs antialiased font-light text-opacity-100 text-coolGray-300 ">Terbit</p>
                <p id="terbit" class="text-sm antialiased font-semibold text-coolGray-300 text-opacity-90"></p>
              </div>
              <div
                class="flex flex-col items-center justify-center h-20 py-1 text-center border-2 border-solid rounded-full shadow-md border-lime-500 sm:h-24">
                <p class="text-xs antialiased font-light text-opacity-100 text-coolGray-300 ">Subuh</p>
                <p id="subuh" class="text-sm antialiased font-semibold text-coolGray-300 text-opacity-90"></p>
              </div>
              <div
                class="flex flex-col items-center justify-center h-20 py-1 text-center border-2 border-solid rounded-full shadow-md border-lime-500 sm:h-24">
                <p class="text-xs antialiased font-light text-opacity-100 text-coolGray-300 ">Dzuhur</p>
                <p id="dzuhur" class="text-sm antialiased font-semibold text-coolGray-300 text-opacity-90"></p>
              </div>
              <div
                class="flex flex-col items-center justify-center h-20 py-1 text-center border-2 border-solid rounded-full shadow-md border-lime-500 sm:h-24">
                <p class="text-xs antialiased font-light text-opacity-100 text-coolGray-300 ">Ashar</p>
                <p id="ashar" class="text-sm antialiased font-semibold text-coolGray-300 text-opacity-90"></p>
              </div>
              <div
                class="flex flex-col items-center justify-center h-20 py-1 text-center border-2 border-solid rounded-full shadow-md border-lime-500 sm:h-24">
                <p class="text-xs antialiased font-light text-opacity-100 text-coolGray-300 ">Maghrib</p>
                <p id="maghrib" class="text-sm antialiased font-semibold text-coolGray-300 text-opacity-90"></p>
              </div>
              <div
                class="flex flex-col items-center justify-center h-20 py-1 text-center border-2 border-solid rounded-full shadow-md border-lime-500 sm:h-24">
                <p class="text-xs antialiased font-light text-opacity-100 text-coolGray-300 ">Isya</p>
                <p id="isya" class="text-sm antialiased font-semibold text-coolGray-300 text-opacity-90"></p>
              </div>
            </div>

          </div>
        </div>

        <!-- <div class="grid grid-cols-1 bg-black bg-opacity-80"> -->
        <div class="grid grid-cols-1 bg-blueGray-800">
          <!-- <div class="bg-coolGray-100 rounded-tr-50"> -->
          <div class="px-3 py-3 bg-sky-600 rounded-tr-50">
            <div id="content"
              class="h-full px-3 py-3 pb-3 space-y-3 overflow-hidden bg-opacity-100 bg-coolGray-800 rounded-t-xl rounded-b-3xl rounded-tr-50">

              <div id="formhead"></div>

              <div id="formbody" class="space-y-3">

                <div id="slideText">

                </div>

                <div
                  class="grid items-center justify-center grid-cols-1 p-1 space-x-1 border-t rounded-lg shadow-md border-lime-500 bg-coolGray-900">
                  <div class="px-3 py-3">
                    <p class="text-sm antialiased font-medium text-sky-600">
                      Anda berhasil login
                    </p>
                  </div>
                </div>

                <div
                  class="grid items-center justify-center grid-cols-1 p-1 space-x-1 border-l rounded-lg shadow-md border-lime-500 bg-coolGray-900">

                  <div class="px-3 py-3">

                    <table class="text-sm antialiased text-sky-600">
                      <tr>
                        <td width="110">Username</td>
                        $(if login-by == 'trial')
                        <td>: Trial</td>
                        $(elif login-by != 'mac')
                        <td>: $(username)</td>
                        $(endif)
                      </tr>
                      <tr>
                        <td>IP Address</td>
                        <td>: $(ip)</td>
                      </tr>
                      <tr>
                        <td>Upload</td>
                        <td>: $(bytes-in-nice)</td>
                      </tr>
                      <tr>
                        <td>Download</td>
                        <td>: $(bytes-out-nice)</td>
                      </tr>
                      $(if session-time-left)
                      <tr>
                        <td>Sisa Waktu</td>
                        <td>: $(session-time-left)</td>
                      </tr>
                      $(else)
                      <tr>
                        <td>Tersambung</td>
                        <td>: $(uptime)</td>
                      </tr>
                      $(endif)
                      <tr>
                        <td>Status Refresh</td>
                        <td>: $(refresh-timeout)</td>
                      </tr>
                    </table>
                  </div>
                </div>

                <div>
                  <form action="$(link-logout)" name="logout" onSubmit="return openLogout()">
                    <div class="grid grid-cols-1 gap-2">
                      $(if login-by-mac != 'yes')
                      <button type="submit"
                        class="flex items-center justify-center px-3 py-3 rounded-lg shadow-2xl bg-coolGray-800 bg-opacity-10 text-md ring-1 ring-red-400 focus:bg-opacity-5">
                        <p class="antialiased font-normal text-red-400">Logout</p>
                      </button>
                      $(endif)
                    </div>
                  </form>
                </div>
              </div>

              <div id="copyright"></div>

            </div>
          </div>
        </div>

      </div>
    </div>
  </div>

  <script src="assets/js/config.js"></script>
  <script src="assets/js/app.js"></script>
</body>

</html>

