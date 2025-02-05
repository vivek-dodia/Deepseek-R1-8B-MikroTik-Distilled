# Repository Information
Name: my-mikrotik-traffic-monitor

# Directory Structure
Directory structure:
└── github_repos/my-mikrotik-traffic-monitor/
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
    │   │       ├── pack-2c39487e03bc945a41fdab0b6963fde170842fb4.idx
    │   │       └── pack-2c39487e03bc945a41fdab0b6963fde170842fb4.pack
    │   ├── packed-refs
    │   └── refs/
    │       ├── heads/
    │       │   └── master
    │       ├── remotes/
    │       │   └── origin/
    │       │       └── HEAD
    │       └── tags/
    ├── .gitattributes
    ├── api_mt_include2.php
    ├── assets/
    │   ├── css/
    │   │   ├── demo.css
    │   │   ├── paper-dashboard.css
    │   │   └── themify-icons.css
    │   ├── fonts/
    │   │   ├── themify.eot
    │   │   ├── themify.ttf
    │   │   └── themify.woff
    │   ├── img/
    │   │   └── faces/
    │   ├── js/
    │   │   ├── bootstrap-checkbox-radio.js
    │   │   ├── bootstrap-notify.js
    │   │   ├── demo.js
    │   │   ├── jquery-1.10.2.js
    │   │   └── paper-dashboard.js
    │   └── sass/
    │       ├── paper/
    │       │   ├── mixins/
    │       │   │   ├── _buttons.scss
    │       │   │   ├── _cards.scss
    │       │   │   ├── _chartist.scss
    │       │   │   ├── _icons.scss
    │       │   │   ├── _inputs.scss
    │       │   │   ├── _labels.scss
    │       │   │   ├── _navbars.scss
    │       │   │   ├── _sidebar.scss
    │       │   │   ├── _tabs.scss
    │       │   │   ├── _transparency.scss
    │       │   │   └── _vendor-prefixes.scss
    │       │   ├── _alerts.scss
    │       │   ├── _buttons.scss
    │       │   ├── _cards.scss
    │       │   ├── _chartist.scss
    │       │   ├── _checkbox-radio.scss
    │       │   ├── _dropdown.scss
    │       │   ├── _footers.scss
    │       │   ├── _inputs.scss
    │       │   ├── _misc.scss
    │       │   ├── _mixins.scss
    │       │   ├── _navbars.scss
    │       │   ├── _responsive.scss
    │       │   ├── _sidebar-and-main-panel.scss
    │       │   ├── _tables.scss
    │       │   ├── _typography.scss
    │       │   └── _variables.scss
    │       └── paper-dashboard.scss
    ├── config.php
    ├── data.php
    ├── index.html
    ├── interfaces2.php
    ├── LICENSE
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
	url = https://github.com/AnasProgrammer2/my-mikrotik-traffic-monitor.git
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
0000000000000000000000000000000000000000 e5fabf08099d5ee43879510178188ed1a22a850f vivek-dodia <vivek.dodia@icloud.com> 1738606367 -0500	clone: from https://github.com/AnasProgrammer2/my-mikrotik-traffic-monitor.git


File: /.git\logs\refs\heads\master
0000000000000000000000000000000000000000 e5fabf08099d5ee43879510178188ed1a22a850f vivek-dodia <vivek.dodia@icloud.com> 1738606367 -0500	clone: from https://github.com/AnasProgrammer2/my-mikrotik-traffic-monitor.git


File: /.git\logs\refs\remotes\origin\HEAD
0000000000000000000000000000000000000000 e5fabf08099d5ee43879510178188ed1a22a850f vivek-dodia <vivek.dodia@icloud.com> 1738606367 -0500	clone: from https://github.com/AnasProgrammer2/my-mikrotik-traffic-monitor.git


File: /.git\packed-refs
# pack-refs with: peeled fully-peeled sorted 
2f71821b5dfa871a209af8959524ca90524da575 refs/remotes/origin/add-license-1
e5fabf08099d5ee43879510178188ed1a22a850f refs/remotes/origin/master


File: /.git\refs\heads\master
e5fabf08099d5ee43879510178188ed1a22a850f


File: /.git\refs\remotes\origin\HEAD
ref: refs/remotes/origin/master


File: /.gitattributes
# Auto detect text files and perform LF normalization
* text=auto

File: /api_mt_include2.php
<?php
/*****************************
 *
 * RouterOS PHP API class v1.4
 * Author: Denis Basta
 * Contributors:
 *    Nick Barnes
 *    Ben Menking (ben [at] infotechsc [dot] com)
 *    Jeremy Jefferson (http://jeremyj.com)
 *    Cristian Deluxe (djcristiandeluxe [at] gmail [dot] com)
 *    Nicolas Daitsch, Nro de Puerto publico 
 *
 * http://www.mikrotik.com
 * http://wiki.mikrotik.com/wiki/API_PHP_class
 *
 ******************************/

class routeros_api
{
    var $debug = false;      // Show debug information
    var $error_no;           // Variable for storing connection error number, if any
    var $error_str;          // Variable for storing connection error text, if any
    var $attempts = 5;       // Connection attempt count
    var $connected = false;  // Connection state
    var $delay = 3;          // Delay between connection attempts in seconds
    //var $port = 8728;        // Port to connect to
    var $timeout = 3;        // Connection attempt timeout and data read timeout
    var $socket;             // Variable for storing socket resource
    
    /**
     * Print text for debug purposes
     *
     * @param string      $text       Text to print
     *
     * @return void
     */
    function debug($text)
    {
        if ($this->debug)
            echo $text . "\n";
    }
	
	
    /**
     * 
     *
     * @param string        $length
     *
     * @return void
     */
    function encode_length($length)
    {
        if ($length < 0x80) {
            $length = chr($length);
        } else if ($length < 0x4000) {
            $length |= 0x8000;
            $length = chr(($length >> 8) & 0xFF) . chr($length & 0xFF);
        } else if ($length < 0x200000) {
            $length |= 0xC00000;
            $length = chr(($length >> 16) & 0xFF) . chr(($length >> 8) & 0xFF) . chr($length & 0xFF);
        } else if ($length < 0x10000000) {
            $length |= 0xE0000000;
            $length = chr(($length >> 24) & 0xFF) . chr(($length >> 16) & 0xFF) . chr(($length >> 8) & 0xFF) . chr($length & 0xFF);
        } else if ($length >= 0x10000000)
            $length = chr(0xF0) . chr(($length >> 24) & 0xFF) . chr(($length >> 16) & 0xFF) . chr(($length >> 8) & 0xFF) . chr($length & 0xFF);
        return $length;
    }
	
	
    /**
     * Login to RouterOS
     *
     * @param string      $ip         Hostname (IP or domain) of the RouterOS server
     * @param string      $login      The RouterOS username
     * @param string      $password   The RouterOS password
     *
     * @return boolean                If we are connected or not
     */
    function connect($ip, $login, $password, $port)
    {
        for ($ATTEMPT = 1; $ATTEMPT <= $this->attempts; $ATTEMPT++) {
            $this->connected = false;
            $this->debug('Connection attempt #' . $ATTEMPT . ' to ' . $ip . ':' . $port . '...');
            if ($this->socket = @fsockopen($ip, $port, $this->error_no, $this->error_str, $this->timeout)) {
                socket_set_timeout($this->socket, $this->timeout);
                $this->write('/login');
                $RESPONSE = $this->read(false);
                if ($RESPONSE[0] == '!done') {
                    if (preg_match_all('/[^=]+/i', $RESPONSE[1], $MATCHES)) {
                        if ($MATCHES[0][0] == 'ret' && strlen($MATCHES[0][1]) == 32) {
                            $this->write('/login', false);
                            $this->write('=name=' . $login, false);
                            $this->write('=response=00' . md5(chr(0) . $password . pack('H*', $MATCHES[0][1])));
                            $RESPONSE = $this->read(false);
                            if ($RESPONSE[0] == '!done') {
                                $this->connected = true;
                                break;
                            }
                        }
                    }
                }
                fclose($this->socket);
            }
            sleep($this->delay);
        }
        if ($this->connected)
            $this->debug('Connected...');
        else
            $this->debug('Error...');
        return $this->connected;
    }
	
	
    /**
     * Disconnect from RouterOS
     *
     * @return void
     */
    function disconnect()
    {
        fclose($this->socket);
        $this->connected = false;
        $this->debug('Disconnected...');
    }
	
	
    /**
     * Parse response from Router OS
     *
     * @param array       $response   Response data
     *
     * @return array                  Array with parsed data
     */
    function parse_response($response)
    {
        if (is_array($response)) {
            $PARSED      = array();
            $CURRENT     = null;
            $singlevalue = null;
            $count       = 0;
            foreach ($response as $x) {
                if (in_array($x, array(
                    '!fatal',
                    '!re',
                    '!trap'
                ))) {
                    if ($x == '!re') {
                        $CURRENT =& $PARSED[];
                    } else
                        $CURRENT =& $PARSED[$x][];
                } else if ($x != '!done') {
                    if (preg_match_all('/[^=]+/i', $x, $MATCHES)) {
                        if ($MATCHES[0][0] == 'ret') {
                            $singlevalue = $MATCHES[0][1];
                        }
						$CURRENT[$MATCHES[0][0]] = (isset($MATCHES[0][1]) ? $MATCHES[0][1] : '');
					}
                }
            }
            if (empty($PARSED) && !is_null($singlevalue)) {
                $PARSED = $singlevalue;
            }
            return $PARSED;
        } else
            return array();
    }
	
	
    /**
     * Parse response from Router OS
     *
     * @param array       $response   Response data
     *
     * @return array                  Array with parsed data
     */
    function parse_response4smarty($response)
    {
        if (is_array($response)) {
            $PARSED  = array();
            $CURRENT = null;
            $singlevalue = null;
            foreach ($response as $x) {
                if (in_array($x, array(
                    '!fatal',
                    '!re',
                    '!trap'
                ))) {
                    if ($x == '!re')
                        $CURRENT =& $PARSED[];
                    else
                        $CURRENT =& $PARSED[$x][];
                } else if ($x != '!done') {
                    if (preg_match_all('/[^=]+/i', $x, $MATCHES)) {
                        if ($MATCHES[0][0] == 'ret') {
                            $singlevalue = $MATCHES[0][1];
                        }
                        $CURRENT[$MATCHES[0][0]] = (isset($MATCHES[0][1]) ? $MATCHES[0][1] : '');
					}
                }
            }
            foreach ($PARSED as $key => $value) {
                $PARSED[$key] = $this->array_change_key_name($value);
            }
            return $PARSED;
            if (empty($PARSED) && !is_null($singlevalue)) {
                $PARSED = $singlevalue;
            }
        } else {
            return array();
        }
    }
	
	
    /**
     * Change "-" and "/" from array key to "_"
     *
     * @param array       $array      Input array
     *
     * @return array                  Array with changed key names
     */
    function array_change_key_name(&$array)
    {
        if (is_array($array)) {
            foreach ($array as $k => $v) {
                $tmp = str_replace("-", "_", $k);
                $tmp = str_replace("/", "_", $tmp);
                if ($tmp) {
                    $array_new[$tmp] = $v;
                } else {
                    $array_new[$k] = $v;
                }
            }
            return $array_new;
        } else {
            return $array;
        }
    }
	
	
    /**
     * Read data from Router OS
     *
     * @param boolean     $parse      Parse the data? default: true
     *
     * @return array                  Array with parsed or unparsed data
     */
    function read($parse = true)
    {
        $RESPONSE = array();
        while (true) {
            // Read the first byte of input which gives us some or all of the length
            // of the remaining reply.
            $BYTE   = ord(fread($this->socket, 1));
            $LENGTH = 0;
            // If the first bit is set then we need to remove the first four bits, shift left 8
            // and then read another byte in.
            // We repeat this for the second and third bits.
            // If the fourth bit is set, we need to remove anything left in the first byte
            // and then read in yet another byte.
            if ($BYTE & 128) {
                if (($BYTE & 192) == 128) {
                    $LENGTH = (($BYTE & 63) << 8) + ord(fread($this->socket, 1));
                } else {
                    if (($BYTE & 224) == 192) {
                        $LENGTH = (($BYTE & 31) << 8) + ord(fread($this->socket, 1));
                        $LENGTH = ($LENGTH << 8) + ord(fread($this->socket, 1));
                    } else {
                        if (($BYTE & 240) == 224) {
                            $LENGTH = (($BYTE & 15) << 8) + ord(fread($this->socket, 1));
                            $LENGTH = ($LENGTH << 8) + ord(fread($this->socket, 1));
                            $LENGTH = ($LENGTH << 8) + ord(fread($this->socket, 1));
                        } else {
                            $LENGTH = ord(fread($this->socket, 1));
                            $LENGTH = ($LENGTH << 8) + ord(fread($this->socket, 1));
                            $LENGTH = ($LENGTH << 8) + ord(fread($this->socket, 1));
                            $LENGTH = ($LENGTH << 8) + ord(fread($this->socket, 1));
                        }
                    }
                }
            } else {
                $LENGTH = $BYTE;
            }
            // If we have got more characters to read, read them in.
            if ($LENGTH > 0) {
                $_      = "";
                $retlen = 0;
                while ($retlen < $LENGTH) {
                    $toread = $LENGTH - $retlen;
                    $_ .= fread($this->socket, $toread);
                    $retlen = strlen($_);
                }
                $RESPONSE[] = $_;
                $this->debug('>>> [' . $retlen . '/' . $LENGTH . '] bytes read.');
            }
            // If we get a !done, make a note of it.
            if ($_ == "!done")
                $receiveddone = true;
            $STATUS = socket_get_status($this->socket);
            if ($LENGTH > 0)
                $this->debug('>>> [' . $LENGTH . ', ' . $STATUS['unread_bytes'] . ']' . $_);
            if ((!$this->connected && !$STATUS['unread_bytes']) || ($this->connected && !$STATUS['unread_bytes'] && $receiveddone))
                break;
        }
        if ($parse)
            $RESPONSE = $this->parse_response($RESPONSE);
        return $RESPONSE;
    }
	
	
    /**
     * Write (send) data to Router OS
     *
     * @param string      $command    A string with the command to send
     * @param mixed       $param2     If we set an integer, the command will send this data as a "tag"
     *                                If we set it to boolean true, the funcion will send the comand and finish
     *                                If we set it to boolean false, the funcion will send the comand and wait for next command
     *                                Default: true
     *
     * @return boolean                Return false if no command especified
     */
    function write($command, $param2 = true)
    {
        if ($command) {
            $data = explode("\n", $command);
            foreach ($data as $com) {
                $com = trim($com);
                fwrite($this->socket, $this->encode_length(strlen($com)) . $com);
                $this->debug('<<< [' . strlen($com) . '] ' . $com);
            }
            if (gettype($param2) == 'integer') {
                fwrite($this->socket, $this->encode_length(strlen('.tag=' . $param2)) . '.tag=' . $param2 . chr(0));
                $this->debug('<<< [' . strlen('.tag=' . $param2) . '] .tag=' . $param2);
            } else if (gettype($param2) == 'boolean')
                fwrite($this->socket, ($param2 ? chr(0) : ''));
            return true;
        } else
            return false;
    }
	
	
    /**
     * Write (send) data to Router OS
     *
     * @param string      $com        A string with the command to send
     * @param array       $arr        An array with arguments or queries
     *
     * @return array                  Array with parsed
     */
    function comm($com, $arr = array())
    {
        $count = count($arr);
        $this->write($com, !$arr);
        $i = 0;
        foreach ($arr as $k => $v) {
            switch ($k[0]) {
                case "?":
                    $el = "$k=$v";
                    break;
                case "~":
                    $el = "$k~$v";
                    break;
                default:
                    $el = "=$k=$v";
                    break;
            }
            $last = ($i++ == $count - 1);
            $this->write($el, $last);
        }
        return $this->read();
    }
}
?>


File: /assets\css\demo.css
@media (min-width: 992px){
    .typo-line{
        padding-left: 140px;
        margin-bottom: 40px;
        position: relative;
    }

    .typo-line .category{
        transform: translateY(-50%);
        top: 50%;
        left: 0px;
        position: absolute;
    }
}

.icon-section {
	margin: 0 0 3em;
	clear: both;
	overflow: hidden;
}
.icon-container {
	width: 240px;
	padding: .7em 0;
	float: left;
	position: relative;
	text-align: left;
}
.icon-container [class^="ti-"],
.icon-container [class*=" ti-"] {
	color: #000;
	position: absolute;
	margin-top: 3px;
	transition: .3s;
}
.icon-container:hover [class^="ti-"],
.icon-container:hover [class*=" ti-"] {
	font-size: 2.2em;
	margin-top: -5px;
}
.icon-container:hover .icon-name {
	color: #000;
}
.icon-name {
	color: #aaa;
	margin-left: 35px;
	font-size: .8em;
	transition: .3s;
}
.icon-container:hover .icon-name {
	margin-left: 45px;
}

.places-buttons .btn{
    margin-bottom: 30px
}
.sidebar .nav > li.active-pro{
    position: absolute;
    width: 100%;
    bottom: 10px;
}
.sidebar .nav > li.active-pro a{
    background: rgba(255, 255, 255, 0.14);
    opacity: 1;
    color: #FFFFFF;
}

.table-upgrade td:nth-child(2),
.table-upgrade td:nth-child(3){
    text-align: center;
}


File: /assets\css\paper-dashboard.css
/*!
    
 =========================================================
 * Paper Dashboard - v1.1.2
 =========================================================
 
 * Product Page: http://www.creative-tim.com/product/paper-dashboard
 * Copyright 2017 Creative Tim (http://www.creative-tim.com)
 * Licensed under MIT (https://github.com/creativetimofficial/paper-dashboard/blob/master/LICENSE.md)
 
 =========================================================
 
 * The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
 
 */
/*      light colors - used for select dropdown         */
.ct-blue {
  stroke: #7A9E9F !important; }

.ct-azure {
  stroke: #68B3C8 !important; }

.ct-green {
  stroke: #7AC29A !important; }

.ct-orange {
  stroke: #F3BB45 !important; }

.ct-red {
  stroke: #EB5E28 !important; }

h1, .h1, h2, .h2, h3, .h3, h4, .h4, h5, .h5, h6, .h6, p, .navbar, .brand, a, .td-name, td {
  -moz-osx-font-smoothing: grayscale;
  -webkit-font-smoothing: antialiased;
  font-family: 'Muli', "Helvetica", Arial, sans-serif; }

h1, .h1, h2, .h2, h3, .h3, h4, .h4 {
  font-weight: 400;
  margin: 30px 0 15px; }

h1, .h1 {
  font-size: 3.2em; }

h2, .h2 {
  font-size: 2.6em; }

h3, .h3 {
  font-size: 1.825em;
  line-height: 1.4;
  margin: 20px 0 10px; }

h4, .h4 {
  font-size: 1.5em;
  font-weight: 600;
  line-height: 1.2em; }

h5, .h5 {
  font-size: 1.25em;
  font-weight: 400;
  line-height: 1.4em;
  margin-bottom: 15px; }

h6, .h6 {
  font-size: 0.9em;
  font-weight: 600;
  text-transform: uppercase; }

p {
  font-size: 16px;
  line-height: 1.4em; }

h1 small, h2 small, h3 small, h4 small, h5 small, h6 small, .h1 small, .h2 small, .h3 small, .h4 small, .h5 small, .h6 small, h1 .small, h2 .small, h3 .small, h4 .small, h5 .small, h6 .small, .h1 .small, .h2 .small, .h3 .small, .h4 .small, .h5 .small, .h6 .small {
  color: #9A9A9A;
  font-weight: 300;
  line-height: 1.4em; }

h1 small, h2 small, h3 small, h1 .small, h2 .small, h3 .small {
  font-size: 60%; }

.title-uppercase {
  text-transform: uppercase; }

blockquote {
  font-style: italic; }

blockquote small {
  font-style: normal; }

.text-muted {
  color: #DDDDDD; }

.text-primary, .text-primary:hover {
  color: #427C89; }

.text-info, .text-info:hover {
  color: #3091B2; }

.text-success, .text-success:hover {
  color: #42A084; }

.text-warning, .text-warning:hover {
  color: #BB992F; }

.text-danger, .text-danger:hover {
  color: #B33C12; }

.glyphicon {
  line-height: 1; }

strong {
  color: #403D39; }

.icon-primary {
  color: #7A9E9F; }

.icon-info {
  color: #68B3C8; }

.icon-success {
  color: #7AC29A; }

.icon-warning {
  color: #F3BB45; }

.icon-danger {
  color: #EB5E28; }

.chart-legend .text-primary, .chart-legend .text-primary:hover {
  color: #7A9E9F; }
.chart-legend .text-info, .chart-legend .text-info:hover {
  color: #68B3C8; }
.chart-legend .text-success, .chart-legend .text-success:hover {
  color: #7AC29A; }
.chart-legend .text-warning, .chart-legend .text-warning:hover {
  color: #F3BB45; }
.chart-legend .text-danger, .chart-legend .text-danger:hover {
  color: #EB5E28; }

/*     General overwrite     */
body {
  color: #66615b;
  font-size: 14px;
  font-family: 'Muli', Arial, sans-serif; }
  body .wrapper {
    min-height: 100vh;
    position: relative; }

a {
  color: #68B3C8; }
  a:hover, a:focus {
    color: #3091B2;
    text-decoration: none; }

a:focus, a:active,
button::-moz-focus-inner,
input::-moz-focus-inner,
select::-moz-focus-inner,
input[type="file"] > input[type="button"]::-moz-focus-inner {
  outline: 0 !important; }

.ui-slider-handle:focus,
.navbar-toggle,
input:focus,
button:focus {
  outline: 0 !important; }

/*           Animations              */
.form-control,
.input-group-addon,
.tagsinput,
.navbar,
.navbar .alert {
  -webkit-transition: all 300ms linear;
  -moz-transition: all 300ms linear;
  -o-transition: all 300ms linear;
  -ms-transition: all 300ms linear;
  transition: all 300ms linear; }

.sidebar .nav a,
.table > tbody > tr .td-actions .btn {
  -webkit-transition: all 150ms ease-in;
  -moz-transition: all 150ms ease-in;
  -o-transition: all 150ms ease-in;
  -ms-transition: all 150ms ease-in;
  transition: all 150ms ease-in; }

.btn {
  -webkit-transition: all 100ms ease-in;
  -moz-transition: all 100ms ease-in;
  -o-transition: all 100ms ease-in;
  -ms-transition: all 100ms ease-in;
  transition: all 100ms ease-in; }

.fa {
  width: 21px;
  text-align: center; }

.fa-base {
  font-size: 1.25em !important; }

.margin-top {
  margin-top: 50px; }

hr {
  border-color: #F1EAE0; }

.wrapper {
  position: relative;
  top: 0;
  height: 100vh; }

.sidebar {
  position: absolute;
  top: 0;
  bottom: 0;
  left: 0;
  z-index: 1;
  background-size: cover;
  background-position: center center; }
  .sidebar .sidebar-wrapper {
    position: relative;
    max-height: none;
    min-height: 100%;
    overflow: hidden;
    width: 260px;
    z-index: 4;
    box-shadow: inset -1px 0px 0px 0px #DDDDDD; }
  .sidebar .sidebar-background {
    position: absolute;
    z-index: 1;
    height: 100%;
    width: 100%;
    display: block;
    top: 0;
    left: 0;
    background-size: cover;
    background-position: center center; }

.sidebar,
.off-canvas-sidebar {
  width: 260px;
  display: block;
  font-weight: 200; }
  .sidebar .logo,
  .off-canvas-sidebar .logo {
    padding: 18px 0px;
    margin: 0 20px; }
    .sidebar .logo p,
    .off-canvas-sidebar .logo p {
      float: left;
      font-size: 20px;
      margin: 10px 10px;
      line-height: 20px; }
    .sidebar .logo .simple-text,
    .off-canvas-sidebar .logo .simple-text {
      text-transform: uppercase;
      padding: 4px 0px;
      display: block;
      font-size: 18px;
      text-align: center;
      font-weight: 400;
      line-height: 30px; }
  .sidebar .nav,
  .off-canvas-sidebar .nav {
    margin-top: 20px; }
    .sidebar .nav li > a,
    .off-canvas-sidebar .nav li > a {
      margin: 10px 0px;
      padding-left: 25px;
      padding-right: 25px;
      opacity: .7; }
    .sidebar .nav li:hover > a,
    .off-canvas-sidebar .nav li:hover > a {
      opacity: 1; }
    .sidebar .nav li.active > a,
    .off-canvas-sidebar .nav li.active > a {
      color: #7A9E9F;
      opacity: 1; }
      .sidebar .nav li.active > a:before,
      .off-canvas-sidebar .nav li.active > a:before {
        border-right: 17px solid #DDDDDD;
        border-top: 17px solid transparent;
        border-bottom: 17px solid transparent;
        content: "";
        display: inline-block;
        position: absolute;
        right: 0;
        top: 8px; }
      .sidebar .nav li.active > a:after,
      .off-canvas-sidebar .nav li.active > a:after {
        border-right: 17px solid #f4f3ef;
        border-top: 17px solid transparent;
        border-bottom: 17px solid transparent;
        content: "";
        display: inline-block;
        position: absolute;
        right: -1px;
        top: 8px; }
    .sidebar .nav p,
    .off-canvas-sidebar .nav p {
      margin: 0;
      line-height: 30px;
      font-size: 12px;
      font-weight: 600;
      text-transform: uppercase; }
    .sidebar .nav i,
    .off-canvas-sidebar .nav i {
      font-size: 24px;
      float: left;
      margin-right: 15px;
      line-height: 30px;
      width: 30px;
      text-align: center; }
  .sidebar:after, .sidebar:before,
  .off-canvas-sidebar:after,
  .off-canvas-sidebar:before {
    display: block;
    content: "";
    position: absolute;
    width: 100%;
    height: 100%;
    top: 0;
    left: 0;
    z-index: 2;
    background: #FFFFFF; }
  .sidebar:after, .sidebar:before, .sidebar[data-background-color="white"]:after, .sidebar[data-background-color="white"]:before,
  .off-canvas-sidebar:after,
  .off-canvas-sidebar:before,
  .off-canvas-sidebar[data-background-color="white"]:after,
  .off-canvas-sidebar[data-background-color="white"]:before {
    background-color: #FFFFFF; }
  .sidebar .logo, .sidebar[data-background-color="white"] .logo,
  .off-canvas-sidebar .logo,
  .off-canvas-sidebar[data-background-color="white"] .logo {
    border-bottom: 1px solid rgba(102, 97, 91, 0.3); }
    .sidebar .logo p, .sidebar[data-background-color="white"] .logo p,
    .off-canvas-sidebar .logo p,
    .off-canvas-sidebar[data-background-color="white"] .logo p {
      color: #66615B; }
    .sidebar .logo .simple-text, .sidebar[data-background-color="white"] .logo .simple-text,
    .off-canvas-sidebar .logo .simple-text,
    .off-canvas-sidebar[data-background-color="white"] .logo .simple-text {
      color: #66615B; }
  .sidebar .nav li:not(.active) > a, .sidebar[data-background-color="white"] .nav li:not(.active) > a,
  .off-canvas-sidebar .nav li:not(.active) > a,
  .off-canvas-sidebar[data-background-color="white"] .nav li:not(.active) > a {
    color: #66615B; }
  .sidebar .nav .divider, .sidebar[data-background-color="white"] .nav .divider,
  .off-canvas-sidebar .nav .divider,
  .off-canvas-sidebar[data-background-color="white"] .nav .divider {
    background-color: rgba(102, 97, 91, 0.2); }
  .sidebar[data-background-color="black"]:after, .sidebar[data-background-color="black"]:before,
  .off-canvas-sidebar[data-background-color="black"]:after,
  .off-canvas-sidebar[data-background-color="black"]:before {
    background-color: #212120; }
  .sidebar[data-background-color="black"] .logo,
  .off-canvas-sidebar[data-background-color="black"] .logo {
    border-bottom: 1px solid rgba(255, 255, 255, 0.3); }
    .sidebar[data-background-color="black"] .logo p,
    .off-canvas-sidebar[data-background-color="black"] .logo p {
      color: #FFFFFF; }
    .sidebar[data-background-color="black"] .logo .simple-text,
    .off-canvas-sidebar[data-background-color="black"] .logo .simple-text {
      color: #FFFFFF; }
  .sidebar[data-background-color="black"] .nav li:not(.active) > a,
  .off-canvas-sidebar[data-background-color="black"] .nav li:not(.active) > a {
    color: #FFFFFF; }
  .sidebar[data-background-color="black"] .nav .divider,
  .off-canvas-sidebar[data-background-color="black"] .nav .divider {
    background-color: rgba(255, 255, 255, 0.2); }
  .sidebar[data-active-color="primary"] .nav li.active > a,
  .off-canvas-sidebar[data-active-color="primary"] .nav li.active > a {
    color: #7A9E9F;
    opacity: 1; }
  .sidebar[data-active-color="info"] .nav li.active > a,
  .off-canvas-sidebar[data-active-color="info"] .nav li.active > a {
    color: #68B3C8;
    opacity: 1; }
  .sidebar[data-active-color="success"] .nav li.active > a,
  .off-canvas-sidebar[data-active-color="success"] .nav li.active > a {
    color: #7AC29A;
    opacity: 1; }
  .sidebar[data-active-color="warning"] .nav li.active > a,
  .off-canvas-sidebar[data-active-color="warning"] .nav li.active > a {
    color: #F3BB45;
    opacity: 1; }
  .sidebar[data-active-color="danger"] .nav li.active > a,
  .off-canvas-sidebar[data-active-color="danger"] .nav li.active > a {
    color: #EB5E28;
    opacity: 1; }

.main-panel {
  background-color: #f4f3ef;
  position: relative;
  z-index: 2;
}
  .main-panel > .content {
    padding: 30px 15px;
    min-height: calc(100% - 123px); }
  .main-panel > .footer {
    border-top: 1px solid rgba(0, 0, 0, 0.1); }
  .main-panel .navbar {
    margin-bottom: 0; }

.sidebar,
.main-panel {
  overflow: auto;
  max-height: 100%;
  height: 100%;
  -webkit-transition-property: top,bottom;
  transition-property: top,bottom;
  -webkit-transition-duration: .2s,.2s;
  transition-duration: .2s,.2s;
  -webkit-transition-timing-function: linear,linear;
  transition-timing-function: linear,linear;
  -webkit-overflow-scrolling: touch; }

.btn,
.navbar .navbar-nav > li > a.btn {
  border-radius: 20px;
  box-sizing: border-box;
  border-width: 2px;
  background-color: transparent;
  font-size: 14px;
  font-weight: 500;
  padding: 7px 18px;
  border-color: #66615B;
  color: #66615B;
  -webkit-transition: all 150ms linear;
  -moz-transition: all 150ms linear;
  -o-transition: all 150ms linear;
  -ms-transition: all 150ms linear;
  transition: all 150ms linear; }
  .btn:hover, .btn:focus, .btn:active, .btn.active, .open > .btn.dropdown-toggle,
  .navbar .navbar-nav > li > a.btn:hover,
  .navbar .navbar-nav > li > a.btn:focus,
  .navbar .navbar-nav > li > a.btn:active,
  .navbar .navbar-nav > li > a.btn.active, .open >
  .navbar .navbar-nav > li > a.btn.dropdown-toggle {
    background-color: #66615B;
    color: rgba(255, 255, 255, 0.7);
    border-color: #66615B; }
    .btn:hover .caret, .btn:focus .caret, .btn:active .caret, .btn.active .caret, .open > .btn.dropdown-toggle .caret,
    .navbar .navbar-nav > li > a.btn:hover .caret,
    .navbar .navbar-nav > li > a.btn:focus .caret,
    .navbar .navbar-nav > li > a.btn:active .caret,
    .navbar .navbar-nav > li > a.btn.active .caret, .open >
    .navbar .navbar-nav > li > a.btn.dropdown-toggle .caret {
      border-top-color: rgba(255, 255, 255, 0.7); }
  .btn.disabled, .btn.disabled:hover, .btn.disabled:focus, .btn.disabled.focus, .btn.disabled:active, .btn.disabled.active, .btn:disabled, .btn:disabled:hover, .btn:disabled:focus, .btn:disabled.focus, .btn:disabled:active, .btn:disabled.active, .btn[disabled], .btn[disabled]:hover, .btn[disabled]:focus, .btn[disabled].focus, .btn[disabled]:active, .btn[disabled].active, fieldset[disabled] .btn, fieldset[disabled] .btn:hover, fieldset[disabled] .btn:focus, fieldset[disabled] .btn.focus, fieldset[disabled] .btn:active, fieldset[disabled] .btn.active,
  .navbar .navbar-nav > li > a.btn.disabled,
  .navbar .navbar-nav > li > a.btn.disabled:hover,
  .navbar .navbar-nav > li > a.btn.disabled:focus,
  .navbar .navbar-nav > li > a.btn.disabled.focus,
  .navbar .navbar-nav > li > a.btn.disabled:active,
  .navbar .navbar-nav > li > a.btn.disabled.active,
  .navbar .navbar-nav > li > a.btn:disabled,
  .navbar .navbar-nav > li > a.btn:disabled:hover,
  .navbar .navbar-nav > li > a.btn:disabled:focus,
  .navbar .navbar-nav > li > a.btn:disabled.focus,
  .navbar .navbar-nav > li > a.btn:disabled:active,
  .navbar .navbar-nav > li > a.btn:disabled.active,
  .navbar .navbar-nav > li > a.btn[disabled],
  .navbar .navbar-nav > li > a.btn[disabled]:hover,
  .navbar .navbar-nav > li > a.btn[disabled]:focus,
  .navbar .navbar-nav > li > a.btn[disabled].focus,
  .navbar .navbar-nav > li > a.btn[disabled]:active,
  .navbar .navbar-nav > li > a.btn[disabled].active, fieldset[disabled]
  .navbar .navbar-nav > li > a.btn, fieldset[disabled]
  .navbar .navbar-nav > li > a.btn:hover, fieldset[disabled]
  .navbar .navbar-nav > li > a.btn:focus, fieldset[disabled]
  .navbar .navbar-nav > li > a.btn.focus, fieldset[disabled]
  .navbar .navbar-nav > li > a.btn:active, fieldset[disabled]
  .navbar .navbar-nav > li > a.btn.active {
    background-color: transparent;
    border-color: #66615B; }
  .btn.btn-fill,
  .navbar .navbar-nav > li > a.btn.btn-fill {
    color: #FFFFFF;
    background-color: #66615B;
    opacity: 1;
    filter: alpha(opacity=100); }
    .btn.btn-fill:hover, .btn.btn-fill:focus, .btn.btn-fill:active, .btn.btn-fill.active, .open > .btn.btn-fill.dropdown-toggle,
    .navbar .navbar-nav > li > a.btn.btn-fill:hover,
    .navbar .navbar-nav > li > a.btn.btn-fill:focus,
    .navbar .navbar-nav > li > a.btn.btn-fill:active,
    .navbar .navbar-nav > li > a.btn.btn-fill.active, .open >
    .navbar .navbar-nav > li > a.btn.btn-fill.dropdown-toggle {
      background-color: #403D39;
      color: #FFFFFF;
      border-color: #403D39; }
    .btn.btn-fill .caret,
    .navbar .navbar-nav > li > a.btn.btn-fill .caret {
      border-top-color: #FFFFFF; }
  .btn.btn-simple:hover, .btn.btn-simple:focus, .btn.btn-simple:active, .btn.btn-simple.active, .open > .btn.btn-simple.dropdown-toggle,
  .navbar .navbar-nav > li > a.btn.btn-simple:hover,
  .navbar .navbar-nav > li > a.btn.btn-simple:focus,
  .navbar .navbar-nav > li > a.btn.btn-simple:active,
  .navbar .navbar-nav > li > a.btn.btn-simple.active, .open >
  .navbar .navbar-nav > li > a.btn.btn-simple.dropdown-toggle {
    background-color: transparent;
    color: #403D39; }
  .btn.btn-simple .caret,
  .navbar .navbar-nav > li > a.btn.btn-simple .caret {
    border-top-color: #FFFFFF; }
  .btn .caret,
  .navbar .navbar-nav > li > a.btn .caret {
    border-top-color: #66615B; }
  .btn:hover, .btn:focus,
  .navbar .navbar-nav > li > a.btn:hover,
  .navbar .navbar-nav > li > a.btn:focus {
    outline: 0 !important; }
  .btn:active, .btn.active, .open > .btn.dropdown-toggle,
  .navbar .navbar-nav > li > a.btn:active,
  .navbar .navbar-nav > li > a.btn.active, .open >
  .navbar .navbar-nav > li > a.btn.dropdown-toggle {
    -webkit-box-shadow: none;
    box-shadow: none;
    outline: 0 !important; }
  .btn.btn-icon,
  .navbar .navbar-nav > li > a.btn.btn-icon {
    padding: 7px; }

.btn-group .btn + .btn,
.btn-group .btn + .btn-group,
.btn-group .btn-group + .btn,
.btn-group .btn-group + .btn-group {
  margin-left: -2px; }

.navbar .navbar-nav > li > a.btn-primary, .btn-primary {
  border-color: #7A9E9F;
  color: #7A9E9F; }
  .navbar .navbar-nav > li > a.btn-primary:hover, .navbar .navbar-nav > li > a.btn-primary:focus, .navbar .navbar-nav > li > a.btn-primary:active, .navbar .navbar-nav > li > a.btn-primary.active, .open > .navbar .navbar-nav > li > a.btn-primary.dropdown-toggle, .btn-primary:hover, .btn-primary:focus, .btn-primary:active, .btn-primary.active, .open > .btn-primary.dropdown-toggle {
    background-color: #7A9E9F;
    color: rgba(255, 255, 255, 0.7);
    border-color: #7A9E9F; }
    .navbar .navbar-nav > li > a.btn-primary:hover .caret, .navbar .navbar-nav > li > a.btn-primary:focus .caret, .navbar .navbar-nav > li > a.btn-primary:active .caret, .navbar .navbar-nav > li > a.btn-primary.active .caret, .open > .navbar .navbar-nav > li > a.btn-primary.dropdown-toggle .caret, .btn-primary:hover .caret, .btn-primary:focus .caret, .btn-primary:active .caret, .btn-primary.active .caret, .open > .btn-primary.dropdown-toggle .caret {
      border-top-color: rgba(255, 255, 255, 0.7); }
  .navbar .navbar-nav > li > a.btn-primary.disabled, .navbar .navbar-nav > li > a.btn-primary.disabled:hover, .navbar .navbar-nav > li > a.btn-primary.disabled:focus, .navbar .navbar-nav > li > a.btn-primary.disabled.focus, .navbar .navbar-nav > li > a.btn-primary.disabled:active, .navbar .navbar-nav > li > a.btn-primary.disabled.active, .navbar .navbar-nav > li > a.btn-primary:disabled, .navbar .navbar-nav > li > a.btn-primary:disabled:hover, .navbar .navbar-nav > li > a.btn-primary:disabled:focus, .navbar .navbar-nav > li > a.btn-primary:disabled.focus, .navbar .navbar-nav > li > a.btn-primary:disabled:active, .navbar .navbar-nav > li > a.btn-primary:disabled.active, .navbar .navbar-nav > li > a.btn-primary[disabled], .navbar .navbar-nav > li > a.btn-primary[disabled]:hover, .navbar .navbar-nav > li > a.btn-primary[disabled]:focus, .navbar .navbar-nav > li > a.btn-primary[disabled].focus, .navbar .navbar-nav > li > a.btn-primary[disabled]:active, .navbar .navbar-nav > li > a.btn-primary[disabled].active, fieldset[disabled] .navbar .navbar-nav > li > a.btn-primary, fieldset[disabled] .navbar .navbar-nav > li > a.btn-primary:hover, fieldset[disabled] .navbar .navbar-nav > li > a.btn-primary:focus, fieldset[disabled] .navbar .navbar-nav > li > a.btn-primary.focus, fieldset[disabled] .navbar .navbar-nav > li > a.btn-primary:active, fieldset[disabled] .navbar .navbar-nav > li > a.btn-primary.active, .btn-primary.disabled, .btn-primary.disabled:hover, .btn-primary.disabled:focus, .btn-primary.disabled.focus, .btn-primary.disabled:active, .btn-primary.disabled.active, .btn-primary:disabled, .btn-primary:disabled:hover, .btn-primary:disabled:focus, .btn-primary:disabled.focus, .btn-primary:disabled:active, .btn-primary:disabled.active, .btn-primary[disabled], .btn-primary[disabled]:hover, .btn-primary[disabled]:focus, .btn-primary[disabled].focus, .btn-primary[disabled]:active, .btn-primary[disabled].active, fieldset[disabled] .btn-primary, fieldset[disabled] .btn-primary:hover, fieldset[disabled] .btn-primary:focus, fieldset[disabled] .btn-primary.focus, fieldset[disabled] .btn-primary:active, fieldset[disabled] .btn-primary.active {
    background-color: transparent;
    border-color: #7A9E9F; }
  .navbar .navbar-nav > li > a.btn-primary.btn-fill, .btn-primary.btn-fill {
    color: #FFFFFF;
    background-color: #7A9E9F;
    opacity: 1;
    filter: alpha(opacity=100); }
    .navbar .navbar-nav > li > a.btn-primary.btn-fill:hover, .navbar .navbar-nav > li > a.btn-primary.btn-fill:focus, .navbar .navbar-nav > li > a.btn-primary.btn-fill:active, .navbar .navbar-nav > li > a.btn-primary.btn-fill.active, .open > .navbar .navbar-nav > li > a.btn-primary.btn-fill.dropdown-toggle, .btn-primary.btn-fill:hover, .btn-primary.btn-fill:focus, .btn-primary.btn-fill:active, .btn-primary.btn-fill.active, .open > .btn-primary.btn-fill.dropdown-toggle {
      background-color: #427C89;
      color: #FFFFFF;
      border-color: #427C89; }
    .navbar .navbar-nav > li > a.btn-primary.btn-fill .caret, .btn-primary.btn-fill .caret {
      border-top-color: #FFFFFF; }
  .navbar .navbar-nav > li > a.btn-primary.btn-simple:hover, .navbar .navbar-nav > li > a.btn-primary.btn-simple:focus, .navbar .navbar-nav > li > a.btn-primary.btn-simple:active, .navbar .navbar-nav > li > a.btn-primary.btn-simple.active, .open > .navbar .navbar-nav > li > a.btn-primary.btn-simple.dropdown-toggle, .btn-primary.btn-simple:hover, .btn-primary.btn-simple:focus, .btn-primary.btn-simple:active, .btn-primary.btn-simple.active, .open > .btn-primary.btn-simple.dropdown-toggle {
    background-color: transparent;
    color: #427C89; }
  .navbar .navbar-nav > li > a.btn-primary.btn-simple .caret, .btn-primary.btn-simple .caret {
    border-top-color: #FFFFFF; }
  .navbar .navbar-nav > li > a.btn-primary .caret, .btn-primary .caret {
    border-top-color: #7A9E9F; }

.navbar .navbar-nav > li > a.btn-success, .btn-success {
  border-color: #7AC29A;
  color: #7AC29A; }
  .navbar .navbar-nav > li > a.btn-success:hover, .navbar .navbar-nav > li > a.btn-success:focus, .navbar .navbar-nav > li > a.btn-success:active, .navbar .navbar-nav > li > a.btn-success.active, .open > .navbar .navbar-nav > li > a.btn-success.dropdown-toggle, .btn-success:hover, .btn-success:focus, .btn-success:active, .btn-success.active, .open > .btn-success.dropdown-toggle {
    background-color: #7AC29A;
    color: rgba(255, 255, 255, 0.7);
    border-color: #7AC29A; }
    .navbar .navbar-nav > li > a.btn-success:hover .caret, .navbar .navbar-nav > li > a.btn-success:focus .caret, .navbar .navbar-nav > li > a.btn-success:active .caret, .navbar .navbar-nav > li > a.btn-success.active .caret, .open > .navbar .navbar-nav > li > a.btn-success.dropdown-toggle .caret, .btn-success:hover .caret, .btn-success:focus .caret, .btn-success:active .caret, .btn-success.active .caret, .open > .btn-success.dropdown-toggle .caret {
      border-top-color: rgba(255, 255, 255, 0.7); }
  .navbar .navbar-nav > li > a.btn-success.disabled, .navbar .navbar-nav > li > a.btn-success.disabled:hover, .navbar .navbar-nav > li > a.btn-success.disabled:focus, .navbar .navbar-nav > li > a.btn-success.disabled.focus, .navbar .navbar-nav > li > a.btn-success.disabled:active, .navbar .navbar-nav > li > a.btn-success.disabled.active, .navbar .navbar-nav > li > a.btn-success:disabled, .navbar .navbar-nav > li > a.btn-success:disabled:hover, .navbar .navbar-nav > li > a.btn-success:disabled:focus, .navbar .navbar-nav > li > a.btn-success:disabled.focus, .navbar .navbar-nav > li > a.btn-success:disabled:active, .navbar .navbar-nav > li > a.btn-success:disabled.active, .navbar .navbar-nav > li > a.btn-success[disabled], .navbar .navbar-nav > li > a.btn-success[disabled]:hover, .navbar .navbar-nav > li > a.btn-success[disabled]:focus, .navbar .navbar-nav > li > a.btn-success[disabled].focus, .navbar .navbar-nav > li > a.btn-success[disabled]:active, .navbar .navbar-nav > li > a.btn-success[disabled].active, fieldset[disabled] .navbar .navbar-nav > li > a.btn-success, fieldset[disabled] .navbar .navbar-nav > li > a.btn-success:hover, fieldset[disabled] .navbar .navbar-nav > li > a.btn-success:focus, fieldset[disabled] .navbar .navbar-nav > li > a.btn-success.focus, fieldset[disabled] .navbar .navbar-nav > li > a.btn-success:active, fieldset[disabled] .navbar .navbar-nav > li > a.btn-success.active, .btn-success.disabled, .btn-success.disabled:hover, .btn-success.disabled:focus, .btn-success.disabled.focus, .btn-success.disabled:active, .btn-success.disabled.active, .btn-success:disabled, .btn-success:disabled:hover, .btn-success:disabled:focus, .btn-success:disabled.focus, .btn-success:disabled:active, .btn-success:disabled.active, .btn-success[disabled], .btn-success[disabled]:hover, .btn-success[disabled]:focus, .btn-success[disabled].focus, .btn-success[disabled]:active, .btn-success[disabled].active, fieldset[disabled] .btn-success, fieldset[disabled] .btn-success:hover, fieldset[disabled] .btn-success:focus, fieldset[disabled] .btn-success.focus, fieldset[disabled] .btn-success:active, fieldset[disabled] .btn-success.active {
    background-color: transparent;
    border-color: #7AC29A; }
  .navbar .navbar-nav > li > a.btn-success.btn-fill, .btn-success.btn-fill {
    color: #FFFFFF;
    background-color: #7AC29A;
    opacity: 1;
    filter: alpha(opacity=100); }
    .navbar .navbar-nav > li > a.btn-success.btn-fill:hover, .navbar .navbar-nav > li > a.btn-success.btn-fill:focus, .navbar .navbar-nav > li > a.btn-success.btn-fill:active, .navbar .navbar-nav > li > a.btn-success.btn-fill.active, .open > .navbar .navbar-nav > li > a.btn-success.btn-fill.dropdown-toggle, .btn-success.btn-fill:hover, .btn-success.btn-fill:focus, .btn-success.btn-fill:active, .btn-success.btn-fill.active, .open > .btn-success.btn-fill.dropdown-toggle {
      background-color: #42A084;
      color: #FFFFFF;
      border-color: #42A084; }
    .navbar .navbar-nav > li > a.btn-success.btn-fill .caret, .btn-success.btn-fill .caret {
      border-top-color: #FFFFFF; }
  .navbar .navbar-nav > li > a.btn-success.btn-simple:hover, .navbar .navbar-nav > li > a.btn-success.btn-simple:focus, .navbar .navbar-nav > li > a.btn-success.btn-simple:active, .navbar .navbar-nav > li > a.btn-success.btn-simple.active, .open > .navbar .navbar-nav > li > a.btn-success.btn-simple.dropdown-toggle, .btn-success.btn-simple:hover, .btn-success.btn-simple:focus, .btn-success.btn-simple:active, .btn-success.btn-simple.active, .open > .btn-success.btn-simple.dropdown-toggle {
    background-color: transparent;
    color: #42A084; }
  .navbar .navbar-nav > li > a.btn-success.btn-simple .caret, .btn-success.btn-simple .caret {
    border-top-color: #FFFFFF; }
  .navbar .navbar-nav > li > a.btn-success .caret, .btn-success .caret {
    border-top-color: #7AC29A; }

.navbar .navbar-nav > li > a.btn-info, .btn-info {
  border-color: #68B3C8;
  color: #68B3C8; }
  .navbar .navbar-nav > li > a.btn-info:hover, .navbar .navbar-nav > li > a.btn-info:focus, .navbar .navbar-nav > li > a.btn-info:active, .navbar .navbar-nav > li > a.btn-info.active, .open > .navbar .navbar-nav > li > a.btn-info.dropdown-toggle, .btn-info:hover, .btn-info:focus, .btn-info:active, .btn-info.active, .open > .btn-info.dropdown-toggle {
    background-color: #68B3C8;
    color: rgba(255, 255, 255, 0.7);
    border-color: #68B3C8; }
    .navbar .navbar-nav > li > a.btn-info:hover .caret, .navbar .navbar-nav > li > a.btn-info:focus .caret, .navbar .navbar-nav > li > a.btn-info:active .caret, .navbar .navbar-nav > li > a.btn-info.active .caret, .open > .navbar .navbar-nav > li > a.btn-info.dropdown-toggle .caret, .btn-info:hover .caret, .btn-info:focus .caret, .btn-info:active .caret, .btn-info.active .caret, .open > .btn-info.dropdown-toggle .caret {
      border-top-color: rgba(255, 255, 255, 0.7); }
  .navbar .navbar-nav > li > a.btn-info.disabled, .navbar .navbar-nav > li > a.btn-info.disabled:hover, .navbar .navbar-nav > li > a.btn-info.disabled:focus, .navbar .navbar-nav > li > a.btn-info.disabled.focus, .navbar .navbar-nav > li > a.btn-info.disabled:active, .navbar .navbar-nav > li > a.btn-info.disabled.active, .navbar .navbar-nav > li > a.btn-info:disabled, .navbar .navbar-nav > li > a.btn-info:disabled:hover, .navbar .navbar-nav > li > a.btn-info:disabled:focus, .navbar .navbar-nav > li > a.btn-info:disabled.focus, .navbar .navbar-nav > li > a.btn-info:disabled:active, .navbar .navbar-nav > li > a.btn-info:disabled.active, .navbar .navbar-nav > li > a.btn-info[disabled], .navbar .navbar-nav > li > a.btn-info[disabled]:hover, .navbar .navbar-nav > li > a.btn-info[disabled]:focus, .navbar .navbar-nav > li > a.btn-info[disabled].focus, .navbar .navbar-nav > li > a.btn-info[disabled]:active, .navbar .navbar-nav > li > a.btn-info[disabled].active, fieldset[disabled] .navbar .navbar-nav > li > a.btn-info, fieldset[disabled] .navbar .navbar-nav > li > a.btn-info:hover, fieldset[disabled] .navbar .navbar-nav > li > a.btn-info:focus, fieldset[disabled] .navbar .navbar-nav > li > a.btn-info.focus, fieldset[disabled] .navbar .navbar-nav > li > a.btn-info:active, fieldset[disabled] .navbar .navbar-nav > li > a.btn-info.active, .btn-info.disabled, .btn-info.disabled:hover, .btn-info.disabled:focus, .btn-info.disabled.focus, .btn-info.disabled:active, .btn-info.disabled.active, .btn-info:disabled, .btn-info:disabled:hover, .btn-info:disabled:focus, .btn-info:disabled.focus, .btn-info:disabled:active, .btn-info:disabled.active, .btn-info[disabled], .btn-info[disabled]:hover, .btn-info[disabled]:focus, .btn-info[disabled].focus, .btn-info[disabled]:active, .btn-info[disabled].active, fieldset[disabled] .btn-info, fieldset[disabled] .btn-info:hover, fieldset[disabled] .btn-info:focus, fieldset[disabled] .btn-info.focus, fieldset[disabled] .btn-info:active, fieldset[disabled] .btn-info.active {
    background-color: transparent;
    border-color: #68B3C8; }
  .navbar .navbar-nav > li > a.btn-info.btn-fill, .btn-info.btn-fill {
    color: #FFFFFF;
    background-color: #68B3C8;
    opacity: 1;
    filter: alpha(opacity=100); }
    .navbar .navbar-nav > li > a.btn-info.btn-fill:hover, .navbar .navbar-nav > li > a.btn-info.btn-fill:focus, .navbar .navbar-nav > li > a.btn-info.btn-fill:active, .navbar .navbar-nav > li > a.btn-info.btn-fill.active, .open > .navbar .navbar-nav > li > a.btn-info.btn-fill.dropdown-toggle, .btn-info.btn-fill:hover, .btn-info.btn-fill:focus, .btn-info.btn-fill:active, .btn-info.btn-fill.active, .open > .btn-info.btn-fill.dropdown-toggle {
      background-color: #3091B2;
      color: #FFFFFF;
      border-color: #3091B2; }
    .navbar .navbar-nav > li > a.btn-info.btn-fill .caret, .btn-info.btn-fill .caret {
      border-top-color: #FFFFFF; }
  .navbar .navbar-nav > li > a.btn-info.btn-simple:hover, .navbar .navbar-nav > li > a.btn-info.btn-simple:focus, .navbar .navbar-nav > li > a.btn-info.btn-simple:active, .navbar .navbar-nav > li > a.btn-info.btn-simple.active, .open > .navbar .navbar-nav > li > a.btn-info.btn-simple.dropdown-toggle, .btn-info.btn-simple:hover, .btn-info.btn-simple:focus, .btn-info.btn-simple:active, .btn-info.btn-simple.active, .open > .btn-info.btn-simple.dropdown-toggle {
    background-color: transparent;
    color: #3091B2; }
  .navbar .navbar-nav > li > a.btn-info.btn-simple .caret, .btn-info.btn-simple .caret {
    border-top-color: #FFFFFF; }
  .navbar .navbar-nav > li > a.btn-info .caret, .btn-info .caret {
    border-top-color: #68B3C8; }

.navbar .navbar-nav > li > a.btn-warning, .btn-warning {
  border-color: #F3BB45;
  color: #F3BB45; }
  .navbar .navbar-nav > li > a.btn-warning:hover, .navbar .navbar-nav > li > a.btn-warning:focus, .navbar .navbar-nav > li > a.btn-warning:active, .navbar .navbar-nav > li > a.btn-warning.active, .open > .navbar .navbar-nav > li > a.btn-warning.dropdown-toggle, .btn-warning:hover, .btn-warning:focus, .btn-warning:active, .btn-warning.active, .open > .btn-warning.dropdown-toggle {
    background-color: #F3BB45;
    color: rgba(255, 255, 255, 0.7);
    border-color: #F3BB45; }
    .navbar .navbar-nav > li > a.btn-warning:hover .caret, .navbar .navbar-nav > li > a.btn-warning:focus .caret, .navbar .navbar-nav > li > a.btn-warning:active .caret, .navbar .navbar-nav > li > a.btn-warning.active .caret, .open > .navbar .navbar-nav > li > a.btn-warning.dropdown-toggle .caret, .btn-warning:hover .caret, .btn-warning:focus .caret, .btn-warning:active .caret, .btn-warning.active .caret, .open > .btn-warning.dropdown-toggle .caret {
      border-top-color: rgba(255, 255, 255, 0.7); }
  .navbar .navbar-nav > li > a.btn-warning.disabled, .navbar .navbar-nav > li > a.btn-warning.disabled:hover, .navbar .navbar-nav > li > a.btn-warning.disabled:focus, .navbar .navbar-nav > li > a.btn-warning.disabled.focus, .navbar .navbar-nav > li > a.btn-warning.disabled:active, .navbar .navbar-nav > li > a.btn-warning.disabled.active, .navbar .navbar-nav > li > a.btn-warning:disabled, .navbar .navbar-nav > li > a.btn-warning:disabled:hover, .navbar .navbar-nav > li > a.btn-warning:disabled:focus, .navbar .navbar-nav > li > a.btn-warning:disabled.focus, .navbar .navbar-nav > li > a.btn-warning:disabled:active, .navbar .navbar-nav > li > a.btn-warning:disabled.active, .navbar .navbar-nav > li > a.btn-warning[disabled], .navbar .navbar-nav > li > a.btn-warning[disabled]:hover, .navbar .navbar-nav > li > a.btn-warning[disabled]:focus, .navbar .navbar-nav > li > a.btn-warning[disabled].focus, .navbar .navbar-nav > li > a.btn-warning[disabled]:active, .navbar .navbar-nav > li > a.btn-warning[disabled].active, fieldset[disabled] .navbar .navbar-nav > li > a.btn-warning, fieldset[disabled] .navbar .navbar-nav > li > a.btn-warning:hover, fieldset[disabled] .navbar .navbar-nav > li > a.btn-warning:focus, fieldset[disabled] .navbar .navbar-nav > li > a.btn-warning.focus, fieldset[disabled] .navbar .navbar-nav > li > a.btn-warning:active, fieldset[disabled] .navbar .navbar-nav > li > a.btn-warning.active, .btn-warning.disabled, .btn-warning.disabled:hover, .btn-warning.disabled:focus, .btn-warning.disabled.focus, .btn-warning.disabled:active, .btn-warning.disabled.active, .btn-warning:disabled, .btn-warning:disabled:hover, .btn-warning:disabled:focus, .btn-warning:disabled.focus, .btn-warning:disabled:active, .btn-warning:disabled.active, .btn-warning[disabled], .btn-warning[disabled]:hover, .btn-warning[disabled]:focus, .btn-warning[disabled].focus, .btn-warning[disabled]:active, .btn-warning[disabled].active, fieldset[disabled] .btn-warning, fieldset[disabled] .btn-warning:hover, fieldset[disabled] .btn-warning:focus, fieldset[disabled] .btn-warning.focus, fieldset[disabled] .btn-warning:active, fieldset[disabled] .btn-warning.active {
    background-color: transparent;
    border-color: #F3BB45; }
  .navbar .navbar-nav > li > a.btn-warning.btn-fill, .btn-warning.btn-fill {
    color: #FFFFFF;
    background-color: #F3BB45;
    opacity: 1;
    filter: alpha(opacity=100); }
    .navbar .navbar-nav > li > a.btn-warning.btn-fill:hover, .navbar .navbar-nav > li > a.btn-warning.btn-fill:focus, .navbar .navbar-nav > li > a.btn-warning.btn-fill:active, .navbar .navbar-nav > li > a.btn-warning.btn-fill.active, .open > .navbar .navbar-nav > li > a.btn-warning.btn-fill.dropdown-toggle, .btn-warning.btn-fill:hover, .btn-warning.btn-fill:focus, .btn-warning.btn-fill:active, .btn-warning.btn-fill.active, .open > .btn-warning.btn-fill.dropdown-toggle {
      background-color: #BB992F;
      color: #FFFFFF;
      border-color: #BB992F; }
    .navbar .navbar-nav > li > a.btn-warning.btn-fill .caret, .btn-warning.btn-fill .caret {
      border-top-color: #FFFFFF; }
  .navbar .navbar-nav > li > a.btn-warning.btn-simple:hover, .navbar .navbar-nav > li > a.btn-warning.btn-simple:focus, .navbar .navbar-nav > li > a.btn-warning.btn-simple:active, .navbar .navbar-nav > li > a.btn-warning.btn-simple.active, .open > .navbar .navbar-nav > li > a.btn-warning.btn-simple.dropdown-toggle, .btn-warning.btn-simple:hover, .btn-warning.btn-simple:focus, .btn-warning.btn-simple:active, .btn-warning.btn-simple.active, .open > .btn-warning.btn-simple.dropdown-toggle {
    background-color: transparent;
    color: #BB992F; }
  .navbar .navbar-nav > li > a.btn-warning.btn-simple .caret, .btn-warning.btn-simple .caret {
    border-top-color: #FFFFFF; }
  .navbar .navbar-nav > li > a.btn-warning .caret, .btn-warning .caret {
    border-top-color: #F3BB45; }

.navbar .navbar-nav > li > a.btn-danger, .btn-danger {
  border-color: #EB5E28;
  color: #EB5E28; }
  .navbar .navbar-nav > li > a.btn-danger:hover, .navbar .navbar-nav > li > a.btn-danger:focus, .navbar .navbar-nav > li > a.btn-danger:active, .navbar .navbar-nav > li > a.btn-danger.active, .open > .navbar .navbar-nav > li > a.btn-danger.dropdown-toggle, .btn-danger:hover, .btn-danger:focus, .btn-danger:active, .btn-danger.active, .open > .btn-danger.dropdown-toggle {
    background-color: #EB5E28;
    color: rgba(255, 255, 255, 0.7);
    border-color: #EB5E28; }
    .navbar .navbar-nav > li > a.btn-danger:hover .caret, .navbar .navbar-nav > li > a.btn-danger:focus .caret, .navbar .navbar-nav > li > a.btn-danger:active .caret, .navbar .navbar-nav > li > a.btn-danger.active .caret, .open > .navbar .navbar-nav > li > a.btn-danger.dropdown-toggle .caret, .btn-danger:hover .caret, .btn-danger:focus .caret, .btn-danger:active .caret, .btn-danger.active .caret, .open > .btn-danger.dropdown-toggle .caret {
      border-top-color: rgba(255, 255, 255, 0.7); }
  .navbar .navbar-nav > li > a.btn-danger.disabled, .navbar .navbar-nav > li > a.btn-danger.disabled:hover, .navbar .navbar-nav > li > a.btn-danger.disabled:focus, .navbar .navbar-nav > li > a.btn-danger.disabled.focus, .navbar .navbar-nav > li > a.btn-danger.disabled:active, .navbar .navbar-nav > li > a.btn-danger.disabled.active, .navbar .navbar-nav > li > a.btn-danger:disabled, .navbar .navbar-nav > li > a.btn-danger:disabled:hover, .navbar .navbar-nav > li > a.btn-danger:disabled:focus, .navbar .navbar-nav > li > a.btn-danger:disabled.focus, .navbar .navbar-nav > li > a.btn-danger:disabled:active, .navbar .navbar-nav > li > a.btn-danger:disabled.active, .navbar .navbar-nav > li > a.btn-danger[disabled], .navbar .navbar-nav > li > a.btn-danger[disabled]:hover, .navbar .navbar-nav > li > a.btn-danger[disabled]:focus, .navbar .navbar-nav > li > a.btn-danger[disabled].focus, .navbar .navbar-nav > li > a.btn-danger[disabled]:active, .navbar .navbar-nav > li > a.btn-danger[disabled].active, fieldset[disabled] .navbar .navbar-nav > li > a.btn-danger, fieldset[disabled] .navbar .navbar-nav > li > a.btn-danger:hover, fieldset[disabled] .navbar .navbar-nav > li > a.btn-danger:focus, fieldset[disabled] .navbar .navbar-nav > li > a.btn-danger.focus, fieldset[disabled] .navbar .navbar-nav > li > a.btn-danger:active, fieldset[disabled] .navbar .navbar-nav > li > a.btn-danger.active, .btn-danger.disabled, .btn-danger.disabled:hover, .btn-danger.disabled:focus, .btn-danger.disabled.focus, .btn-danger.disabled:active, .btn-danger.disabled.active, .btn-danger:disabled, .btn-danger:disabled:hover, .btn-danger:disabled:focus, .btn-danger:disabled.focus, .btn-danger:disabled:active, .btn-danger:disabled.active, .btn-danger[disabled], .btn-danger[disabled]:hover, .btn-danger[disabled]:focus, .btn-danger[disabled].focus, .btn-danger[disabled]:active, .btn-danger[disabled].active, fieldset[disabled] .btn-danger, fieldset[disabled] .btn-danger:hover, fieldset[disabled] .btn-danger:focus, fieldset[disabled] .btn-danger.focus, fieldset[disabled] .btn-danger:active, fieldset[disabled] .btn-danger.active {
    background-color: transparent;
    border-color: #EB5E28; }
  .navbar .navbar-nav > li > a.btn-danger.btn-fill, .btn-danger.btn-fill {
    color: #FFFFFF;
    background-color: #EB5E28;
    opacity: 1;
    filter: alpha(opacity=100); }
    .navbar .navbar-nav > li > a.btn-danger.btn-fill:hover, .navbar .navbar-nav > li > a.btn-danger.btn-fill:focus, .navbar .navbar-nav > li > a.btn-danger.btn-fill:active, .navbar .navbar-nav > li > a.btn-danger.btn-fill.active, .open > .navbar .navbar-nav > li > a.btn-danger.btn-fill.dropdown-toggle, .btn-danger.btn-fill:hover, .btn-danger.btn-fill:focus, .btn-danger.btn-fill:active, .btn-danger.btn-fill.active, .open > .btn-danger.btn-fill.dropdown-toggle {
      background-color: #B33C12;
      color: #FFFFFF;
      border-color: #B33C12; }
    .navbar .navbar-nav > li > a.btn-danger.btn-fill .caret, .btn-danger.btn-fill .caret {
      border-top-color: #FFFFFF; }
  .navbar .navbar-nav > li > a.btn-danger.btn-simple:hover, .navbar .navbar-nav > li > a.btn-danger.btn-simple:focus, .navbar .navbar-nav > li > a.btn-danger.btn-simple:active, .navbar .navbar-nav > li > a.btn-danger.btn-simple.active, .open > .navbar .navbar-nav > li > a.btn-danger.btn-simple.dropdown-toggle, .btn-danger.btn-simple:hover, .btn-danger.btn-simple:focus, .btn-danger.btn-simple:active, .btn-danger.btn-simple.active, .open > .btn-danger.btn-simple.dropdown-toggle {
    background-color: transparent;
    color: #B33C12; }
  .navbar .navbar-nav > li > a.btn-danger.btn-simple .caret, .btn-danger.btn-simple .caret {
    border-top-color: #FFFFFF; }
  .navbar .navbar-nav > li > a.btn-danger .caret, .btn-danger .caret {
    border-top-color: #EB5E28; }

.btn-neutral {
  border-color: #FFFFFF;
  color: #FFFFFF; }
  .btn-neutral:hover, .btn-neutral:focus, .btn-neutral:active, .btn-neutral.active, .open > .btn-neutral.dropdown-toggle {
    background-color: #FFFFFF;
    color: rgba(255, 255, 255, 0.7);
    border-color: #FFFFFF; }
    .btn-neutral:hover .caret, .btn-neutral:focus .caret, .btn-neutral:active .caret, .btn-neutral.active .caret, .open > .btn-neutral.dropdown-toggle .caret {
      border-top-color: rgba(255, 255, 255, 0.7); }
  .btn-neutral.disabled, .btn-neutral.disabled:hover, .btn-neutral.disabled:focus, .btn-neutral.disabled.focus, .btn-neutral.disabled:active, .btn-neutral.disabled.active, .btn-neutral:disabled, .btn-neutral:disabled:hover, .btn-neutral:disabled:focus, .btn-neutral:disabled.focus, .btn-neutral:disabled:active, .btn-neutral:disabled.active, .btn-neutral[disabled], .btn-neutral[disabled]:hover, .btn-neutral[disabled]:focus, .btn-neutral[disabled].focus, .btn-neutral[disabled]:active, .btn-neutral[disabled].active, fieldset[disabled] .btn-neutral, fieldset[disabled] .btn-neutral:hover, fieldset[disabled] .btn-neutral:focus, fieldset[disabled] .btn-neutral.focus, fieldset[disabled] .btn-neutral:active, fieldset[disabled] .btn-neutral.active {
    background-color: transparent;
    border-color: #FFFFFF; }
  .btn-neutral.btn-fill {
    color: #FFFFFF;
    background-color: #FFFFFF;
    opacity: 1;
    filter: alpha(opacity=100); }
    .btn-neutral.btn-fill:hover, .btn-neutral.btn-fill:focus, .btn-neutral.btn-fill:active, .btn-neutral.btn-fill.active, .open > .btn-neutral.btn-fill.dropdown-toggle {
      background-color: #FFFFFF;
      color: #FFFFFF;
      border-color: #FFFFFF; }
    .btn-neutral.btn-fill .caret {
      border-top-color: #FFFFFF; }
  .btn-neutral.btn-simple:hover, .btn-neutral.btn-simple:focus, .btn-neutral.btn-simple:active, .btn-neutral.btn-simple.active, .open > .btn-neutral.btn-simple.dropdown-toggle {
    background-color: transparent;
    color: #FFFFFF; }
  .btn-neutral.btn-simple .caret {
    border-top-color: #FFFFFF; }
  .btn-neutral .caret {
    border-top-color: #FFFFFF; }
  .btn-neutral:hover, .btn-neutral:focus {
    color: #66615B; }
  .btn-neutral:active, .btn-neutral.active, .open > .btn-neutral.dropdown-toggle {
    background-color: #FFFFFF;
    color: #66615B; }
  .btn-neutral.btn-fill {
    color: #66615B; }
  .btn-neutral.btn-fill:hover, .btn-neutral.btn-fill:focus {
    color: #403D39; }
  .btn-neutral.btn-simple:active, .btn-neutral.btn-simple.active {
    background-color: transparent; }

.btn:disabled, .btn[disabled], .btn.disabled {
  opacity: 0.5;
  filter: alpha(opacity=50); }

.btn-simple {
  border: 0;
  padding: 7px 18px; }
  .btn-simple.btn-icon {
    padding: 7px; }

.btn-lg {
  font-size: 18px;
  border-radius: 50px;
  padding: 11px 30px;
  font-weight: 400; }
  .btn-lg.btn-simple {
    padding: 13px 30px; }

.btn-sm {
  font-size: 12px;
  border-radius: 26px;
  padding: 4px 10px; }
  .btn-sm.btn-simple {
    padding: 6px 10px; }

.btn-xs {
  font-size: 12px;
  border-radius: 26px;
  padding: 2px 5px; }
  .btn-xs.btn-simple {
    padding: 4px 5px; }

.btn-wd {
  min-width: 140px; }

.btn-group.select {
  width: 100%; }

.btn-group.select .btn {
  text-align: left; }

.btn-group.select .caret {
  position: absolute;
  top: 50%;
  margin-top: -1px;
  right: 8px; }

.form-control::-moz-placeholder {
  color: #DDDDDD;
  opacity: 1;
  filter: alpha(opacity=100); }

.form-control:-moz-placeholder {
  color: #DDDDDD;
  opacity: 1;
  filter: alpha(opacity=100); }

.form-control::-webkit-input-placeholder {
  color: #DDDDDD;
  opacity: 1;
  filter: alpha(opacity=100); }

.form-control:-ms-input-placeholder {
  color: #DDDDDD;
  opacity: 1;
  filter: alpha(opacity=100); }

.form-control {
  background-color: #fffcf5;
  border: medium none;
  border-radius: 4px;
  color: #66615b;
  font-size: 14px;
  transition: background-color 0.3s ease 0s;
  padding: 7px 18px;
  height: 40px;
  -webkit-box-shadow: none;
  box-shadow: none; }
  .form-control:focus {
    background-color: #FFFFFF;
    -webkit-box-shadow: none;
    box-shadow: none;
    outline: 0 !important; }
  .has-success .form-control, .has-error .form-control, .has-success .form-control:focus, .has-error .form-control:focus {
    -webkit-box-shadow: none;
    box-shadow: none; }
  .has-success .form-control {
    background-color: #ABF3CB;
    color: #7AC29A; }
    .has-success .form-control.border-input {
      border: 1px solid #7AC29A; }
  .has-success .form-control:focus {
    background-color: #FFFFFF; }
  .has-error .form-control {
    background-color: #FFC0A4;
    color: #EB5E28; }
    .has-error .form-control.border-input {
      border: 1px solid #EB5E28; }
  .has-error .form-control:focus {
    background-color: #FFFFFF; }
  .form-control + .form-control-feedback {
    border-radius: 6px;
    font-size: 14px;
    margin-top: -7px;
    position: absolute;
    right: 10px;
    top: 50%;
    vertical-align: middle; }
  .form-control.border-input {
    border: 1px solid #CCC5B9; }
  .open .form-control {
    border-bottom-color: transparent; }

.input-lg {
  height: 55px;
  padding: 11px 30px; }

.has-error .form-control-feedback, .has-error .control-label {
  color: #EB5E28; }

.has-success .form-control-feedback, .has-success .control-label {
  color: #7AC29A; }

.input-group-addon {
  background-color: #fffcf5;
  border: medium none;
  border-radius: 4px; }
  .has-success .input-group-addon, .has-error .input-group-addon {
    background-color: #FFFFFF; }
  .has-error .form-control:focus + .input-group-addon {
    color: #EB5E28; }
  .has-success .form-control:focus + .input-group-addon {
    color: #7AC29A; }
  .form-control:focus + .input-group-addon, .form-control:focus ~ .input-group-addon {
    background-color: #FFFFFF; }

.border-input .input-group-addon {
  border: solid 1px #CCC5B9; }

.input-group {
  margin-bottom: 15px; }

.input-group[disabled] .input-group-addon {
  background-color: #E3E3E3; }

.input-group .form-control:first-child,
.input-group-addon:first-child,
.input-group-btn:first-child > .dropdown-toggle,
.input-group-btn:last-child > .btn:not(:last-child):not(.dropdown-toggle) {
  border-right: 0 none; }

.input-group .form-control:last-child,
.input-group-addon:last-child,
.input-group-btn:last-child > .dropdown-toggle,
.input-group-btn:first-child > .btn:not(:first-child) {
  border-left: 0 none; }

.form-control[disabled], .form-control[readonly], fieldset[disabled] .form-control {
  background-color: #E3E3E3;
  cursor: not-allowed;
  color: #9A9A9A;
  opacity: 1;
  filter: alpha(opacity=100); }

.form-control[disabled]::-moz-placeholder {
  color: #9A9A9A;
  opacity: 1;
  filter: alpha(opacity=100); }

.form-control[disabled]:-moz-placeholder {
  color: #DDDDDD;
  opacity: 1;
  filter: alpha(opacity=100); }

.form-control[disabled]::-webkit-input-placeholder {
  color: #DDDDDD;
  opacity: 1;
  filter: alpha(opacity=100); }

.form-control[disabled]:-ms-input-placeholder {
  color: #DDDDDD;
  opacity: 1;
  filter: alpha(opacity=100); }

.input-group-btn .btn {
  border-width: 1px;
  padding: 9px 18px; }

.input-group-btn .btn-default:not(.btn-fill) {
  border-color: #DDDDDD; }

.input-group-btn:last-child > .btn {
  margin-left: 0; }

textarea.form-control {
  max-width: 100%;
  padding: 10px 18px;
  resize: none; }

.alert {
  border: 0;
  border-radius: 0;
  color: #FFFFFF;
  padding: 10px 15px;
  font-size: 14px; }
  .container .alert {
    border-radius: 4px; }
  .navbar .alert {
    border-radius: 0;
    left: 0;
    position: absolute;
    right: 0;
    top: 85px;
    width: 100%;
    z-index: 3; }
  .navbar:not(.navbar-transparent) .alert {
    top: 70px; }
  .alert span[data-notify="icon"] {
    font-size: 30px;
    display: block;
    left: 15px;
    position: absolute;
    top: 50%;
    margin-top: -20px; }
  .alert .close ~ span {
    display: block;
    max-width: 89%; }
  .alert[data-notify="container"] {
    padding: 10px 10px 10px 20px;
    border-radius: 4px; }
  .alert.alert-with-icon {
    padding-left: 65px; }

.alert-info {
  background-color: #7CE4FE;
  color: #3091B2; }

.alert-success {
  background-color: #8EF3C5;
  color: #42A084; }

.alert-warning {
  background-color: #FFE28C;
  color: #BB992F; }

.alert-danger {
  background-color: #FF8F5E;
  color: #B33C12; }

.table thead tr > th,
.table thead tr > td,
.table tbody tr > th,
.table tbody tr > td,
.table tfoot tr > th,
.table tfoot tr > td {
  border-top: 1px solid #CCC5B9; }
.table > thead > tr > th {
  border-bottom-width: 0;
  font-size: 1.25em;
  font-weight: 300; }
.table .radio,
.table .checkbox {
  margin-top: 0;
  margin-bottom: 22px;
  padding: 0;
  width: 15px; }
.table > thead > tr > th,
.table > tbody > tr > th,
.table > tfoot > tr > th,
.table > thead > tr > td,
.table > tbody > tr > td,
.table > tfoot > tr > td {
  padding: 12px;
  vertical-align: middle; }
.table .th-description {
  max-width: 150px; }
.table .td-price {
  font-size: 26px;
  font-weight: 300;
  margin-top: 5px;
  text-align: right; }
.table .td-total {
  font-weight: 600;
  font-size: 1.25em;
  padding-top: 20px;
  text-align: right; }
.table .td-actions .btn.btn-sm, .table .td-actions .btn.btn-xs {
  padding-left: 3px;
  padding-right: 3px; }
.table > tbody > tr {
  position: relative; }

.table-striped tbody > tr:nth-of-type(2n+1) {
  background-color: #fff; }
.table-striped tbody > tr:nth-of-type(2n) {
  background-color: #FFFCF5; }
.table-striped > thead > tr > th,
.table-striped > tbody > tr > th,
.table-striped > tfoot > tr > th,
.table-striped > thead > tr > td,
.table-striped > tbody > tr > td,
.table-striped > tfoot > tr > td {
  padding: 15px 8px; }

/*      Checkbox and radio         */
.checkbox,
.radio {
  margin-bottom: 12px;
  padding-left: 30px;
  position: relative;
  -webkit-transition: color,opacity 0.25s linear;
  transition: color,opacity 0.25s linear;
  font-size: 14px;
  font-weight: normal;
  line-height: 1.5;
  color: #66615b;
  cursor: pointer; }
  .checkbox .icons,
  .radio .icons {
    color: #66615b;
    display: block;
    height: 20px;
    left: 0;
    position: absolute;
    top: 0;
    width: 20px;
    text-align: center;
    line-height: 21px;
    font-size: 20px;
    cursor: pointer;
    -webkit-transition: color,opacity 0.15s linear;
    transition: color,opacity 0.15s linear;
    opacity: .50; }
  .checkbox.checked .icons,
  .radio.checked .icons {
    opacity: 1; }
  .checkbox input,
  .radio input {
    outline: none !important;
    display: none; }

.checkbox label,
.radio label {
  padding-left: 10px; }

.checkbox .icons .first-icon,
.radio .icons .first-icon,
.checkbox .icons .second-icon,
.radio .icons .second-icon {
  display: inline-table;
  position: absolute;
  left: 0;
  top: 0;
  background-color: transparent;
  margin: 0;
  opacity: 1;
  filter: alpha(opacity=100); }

.checkbox .icons .second-icon,
.radio .icons .second-icon {
  opacity: 0;
  filter: alpha(opacity=0); }

.checkbox:hover,
.radio:hover {
  -webkit-transition: color 0.2s linear;
  transition: color 0.2s linear; }

.checkbox:hover .first-icon,
.radio:hover .first-icon {
  opacity: 0;
  filter: alpha(opacity=0); }

.checkbox:hover .second-icon,
.radio:hover .second-icon {
  opacity: 1;
  filter: alpha(opacity=100); }

.checkbox.checked .first-icon,
.radio.checked .first-icon {
  opacity: 0;
  filter: alpha(opacity=0); }

.checkbox.checked .second-icon,
.radio.checked .second-icon {
  opacity: 1;
  filter: alpha(opacity=100);
  -webkit-transition: color 0.2s linear;
  transition: color 0.2s linear; }

.checkbox.disabled,
.radio.disabled {
  cursor: default;
  color: #DDDDDD; }

.checkbox.disabled .icons,
.radio.disabled .icons {
  color: #DDDDDD; }

.checkbox.disabled .first-icon,
.radio.disabled .first-icon {
  opacity: 1;
  filter: alpha(opacity=100); }

.checkbox.disabled .second-icon,
.radio.disabled .second-icon {
  opacity: 0;
  filter: alpha(opacity=0); }

.checkbox.disabled.checked .icons,
.radio.disabled.checked .icons {
  color: #DDDDDD; }

.checkbox.disabled.checked .first-icon,
.radio.disabled.checked .first-icon {
  opacity: 0;
  filter: alpha(opacity=0); }

.checkbox.disabled.checked .second-icon,
.radio.disabled.checked .second-icon {
  opacity: 1;
  color: #DDDDDD;
  filter: alpha(opacity=100); }

.nav > li > a:hover,
.nav > li > a:focus {
  background-color: transparent; }

.navbar {
  border: 0;
  border-radius: 0;
  font-size: 16px;
  z-index: 3; }
  .navbar .navbar-brand {
    font-weight: 600;
    margin: 5px 0px;
    padding: 20px 15px;
    font-size: 20px; }
  .navbar .navbar-nav > li > a {
    line-height: 1.42857;
    margin: 15px 0px;
    padding: 10px 15px; }
    .navbar .navbar-nav > li > a i,
    .navbar .navbar-nav > li > a p {
      display: inline-block;
      margin: 0; }
    .navbar .navbar-nav > li > a i {
      position: relative;
      top: 1px; }
  .navbar .navbar-nav > li > a.btn {
    margin: 15px 3px;
    padding: 7px 18px; }
  .navbar .btn {
    margin: 15px 3px;
    font-size: 14px; }
  .navbar .btn-simple {
    font-size: 16px; }

.navbar-nav > li > .dropdown-menu {
  border-radius: 6px;
  margin-top: -5px; }

.navbar-default {
  background-color: #f4f3ef;
  border-bottom: 1px solid #DDDDDD; }
  .navbar-default .brand {
    color: #66615b !important; }
  .navbar-default .navbar-nav > li > a:not(.btn) {
    color: #9A9A9A; }
  .navbar-default .navbar-nav > .active > a,
  .navbar-default .navbar-nav > .active > a:not(.btn):hover,
  .navbar-default .navbar-nav > .active > a:not(.btn):focus,
  .navbar-default .navbar-nav > li > a:not(.btn):hover,
  .navbar-default .navbar-nav > li > a:not(.btn):focus {
    background-color: transparent;
    border-radius: 3px;
    color: #68B3C8;
    opacity: 1;
    filter: alpha(opacity=100); }
  .navbar-default .navbar-nav > .dropdown > a:hover .caret,
  .navbar-default .navbar-nav > .dropdown > a:focus .caret {
    border-bottom-color: #68B3C8;
    border-top-color: #68B3C8; }
  .navbar-default .navbar-nav > .open > a,
  .navbar-default .navbar-nav > .open > a:hover,
  .navbar-default .navbar-nav > .open > a:focus {
    background-color: transparent;
    color: #68B3C8; }
  .navbar-default .navbar-nav .navbar-toggle:hover, .navbar-default .navbar-nav .navbar-toggle:focus {
    background-color: transparent; }
  .navbar-default:not(.navbar-transparent) .btn-default:hover {
    color: #68B3C8;
    border-color: #68B3C8; }
  .navbar-default:not(.navbar-transparent) .btn-neutral, .navbar-default:not(.navbar-transparent) .btn-neutral:hover, .navbar-default:not(.navbar-transparent) .btn-neutral:active {
    color: #9A9A9A; }

.navbar-form {
  -webkit-box-shadow: none;
  box-shadow: none; }
  .navbar-form .form-control {
    border-radius: 0;
    border: 0;
    padding: 0;
    background-color: transparent;
    height: 22px;
    font-size: 16px;
    line-height: 1.4em;
    color: #E3E3E3; }
  .navbar-transparent .navbar-form .form-control, [class*="navbar-ct"] .navbar-form .form-control {
    color: #FFFFFF;
    border: 0;
    border-bottom: 1px solid rgba(255, 255, 255, 0.6); }

.navbar-ct-primary {
  background-color: #8ECFD5; }

.navbar-ct-info {
  background-color: #7CE4FE; }

.navbar-ct-success {
  background-color: #8EF3C5; }

.navbar-ct-warning {
  background-color: #FFE28C; }

.navbar-ct-danger {
  background-color: #FF8F5E; }

.navbar-transparent {
  padding-top: 15px;
  background-color: transparent;
  border-bottom: 1px solid transparent; }

.navbar-toggle {
  margin-top: 19px;
  margin-bottom: 19px;
  border: 0; }
  .navbar-toggle .icon-bar {
    background-color: #FFFFFF; }
  .navbar-toggle .navbar-collapse,
  .navbar-toggle .navbar-form {
    border-color: transparent; }
  .navbar-toggle.navbar-default .navbar-toggle:hover, .navbar-toggle.navbar-default .navbar-toggle:focus {
    background-color: transparent; }

.navbar-transparent .navbar-brand, [class*="navbar-ct"] .navbar-brand {
  opacity: 0.9;
  filter: alpha(opacity=90); }
  .navbar-transparent .navbar-brand:focus, .navbar-transparent .navbar-brand:hover, [class*="navbar-ct"] .navbar-brand:focus, [class*="navbar-ct"] .navbar-brand:hover {
    background-color: transparent;
    opacity: 1;
    filter: alpha(opacity=100); }
.navbar-transparent .navbar-brand:not([class*="text"]), [class*="navbar-ct"] .navbar-brand:not([class*="text"]) {
  color: #FFFFFF; }
.navbar-transparent .navbar-nav > li > a:not(.btn), [class*="navbar-ct"] .navbar-nav > li > a:not(.btn) {
  color: #FFFFFF;
  border-color: #FFFFFF;
  opacity: 0.8;
  filter: alpha(opacity=80); }
.navbar-transparent .navbar-nav > .active > a:not(.btn),
.navbar-transparent .navbar-nav > .active > a:hover:not(.btn),
.navbar-transparent .navbar-nav > .active > a:focus:not(.btn),
.navbar-transparent .navbar-nav > li > a:hover:not(.btn),
.navbar-transparent .navbar-nav > li > a:focus:not(.btn), [class*="navbar-ct"] .navbar-nav > .active > a:not(.btn),
[class*="navbar-ct"] .navbar-nav > .active > a:hover:not(.btn),
[class*="navbar-ct"] .navbar-nav > .active > a:focus:not(.btn),
[class*="navbar-ct"] .navbar-nav > li > a:hover:not(.btn),
[class*="navbar-ct"] .navbar-nav > li > a:focus:not(.btn) {
  background-color: transparent;
  border-radius: 3px;
  color: #FFFFFF;
  opacity: 1;
  filter: alpha(opacity=100); }
.navbar-transparent .navbar-nav .nav > li > a.btn:hover, [class*="navbar-ct"] .navbar-nav .nav > li > a.btn:hover {
  background-color: transparent; }
.navbar-transparent .navbar-nav > .dropdown > a .caret,
.navbar-transparent .navbar-nav > .dropdown > a:hover .caret,
.navbar-transparent .navbar-nav > .dropdown > a:focus .caret, [class*="navbar-ct"] .navbar-nav > .dropdown > a .caret,
[class*="navbar-ct"] .navbar-nav > .dropdown > a:hover .caret,
[class*="navbar-ct"] .navbar-nav > .dropdown > a:focus .caret {
  border-bottom-color: #FFFFFF;
  border-top-color: #FFFFFF; }
.navbar-transparent .navbar-nav > .open > a,
.navbar-transparent .navbar-nav > .open > a:hover,
.navbar-transparent .navbar-nav > .open > a:focus, [class*="navbar-ct"] .navbar-nav > .open > a,
[class*="navbar-ct"] .navbar-nav > .open > a:hover,
[class*="navbar-ct"] .navbar-nav > .open > a:focus {
  background-color: transparent;
  color: #FFFFFF;
  opacity: 1;
  filter: alpha(opacity=100); }
.navbar-transparent .btn-default, [class*="navbar-ct"] .btn-default {
  color: #FFFFFF;
  border-color: #FFFFFF; }
.navbar-transparent .btn-default.btn-fill, [class*="navbar-ct"] .btn-default.btn-fill {
  color: #9A9A9A;
  background-color: #FFFFFF;
  opacity: 0.9;
  filter: alpha(opacity=90); }
.navbar-transparent .btn-default.btn-fill:hover,
.navbar-transparent .btn-default.btn-fill:focus,
.navbar-transparent .btn-default.btn-fill:active,
.navbar-transparent .btn-default.btn-fill.active,
.navbar-transparent .open .dropdown-toggle.btn-fill.btn-default, [class*="navbar-ct"] .btn-default.btn-fill:hover,
[class*="navbar-ct"] .btn-default.btn-fill:focus,
[class*="navbar-ct"] .btn-default.btn-fill:active,
[class*="navbar-ct"] .btn-default.btn-fill.active,
[class*="navbar-ct"] .open .dropdown-toggle.btn-fill.btn-default {
  border-color: #FFFFFF;
  opacity: 1;
  filter: alpha(opacity=100); }

.footer {
  background-attachment: fixed;
  position: relative;
  line-height: 20px; }
  .footer nav ul {
    list-style: none;
    margin: 0;
    padding: 0;
    font-weight: normal; }
    .footer nav ul li {
      display: inline-block;
      padding: 10px 15px;
      margin: 15px 3px;
      line-height: 20px;
      text-align: center; }
    .footer nav ul a:not(.btn) {
      color: #66615b;
      display: block;
      margin-bottom: 3px; }
      .footer nav ul a:not(.btn):focus, .footer nav ul a:not(.btn):hover {
        color: #403D39; }
  .footer .copyright {
    color: #66615b;
    padding: 10px 15px;
    font-size: 14px;
    white-space: nowrap;
    margin: 15px 3px;
    line-height: 20px;
    text-align: center; }
  .footer .heart {
    color: #EB5E28; }

.dropdown-menu {
  background-color: #FFFCF5;
  border: 0 none;
  border-radius: 6px;
  display: block;
  margin-top: 10px;
  padding: 0px;
  position: absolute;
  visibility: hidden;
  z-index: 9000;
  opacity: 0;
  filter: alpha(opacity=0);
  -webkit-box-shadow: 0 2px rgba(17, 16, 15, 0.1), 0 2px 10px rgba(17, 16, 15, 0.1);
  box-shadow: 0 2px rgba(17, 16, 15, 0.1), 0 2px 10px rgba(17, 16, 15, 0.1); }
  .open .dropdown-menu {
    opacity: 1;
    filter: alpha(opacity=100);
    visibility: visible; }
  .dropdown-menu .divider {
    background-color: #F1EAE0;
    margin: 0px; }
  .dropdown-menu .dropdown-header {
    color: #9A9A9A;
    font-size: 12px;
    padding: 10px 15px; }
  .select .dropdown-menu {
    border-radius: 0 0 10px 10px;
    -webkit-box-shadow: none;
    box-shadow: none;
    -webkit-transform-origin: 50% -40px;
    -moz-transform-origin: 50% -40px;
    -o-transform-origin: 50% -40px;
    -ms-transform-origin: 50% -40px;
    transform-origin: 50% -40px;
    -webkit-transform: scale(1);
    -moz-transform: scale(1);
    -o-transform: scale(1);
    -ms-transform: scale(1);
    transform: scale(1);
    -webkit-transition: all 150ms linear;
    -moz-transition: all 150ms linear;
    -o-transition: all 150ms linear;
    -ms-transition: all 150ms linear;
    transition: all 150ms linear;
    margin-top: -20px; }
  .select.open .dropdown-menu {
    margin-top: -1px; }
  .dropdown-menu > li > a {
    color: #66615b;
    font-size: 14px;
    padding: 10px 15px;
    -webkit-transition: none;
    -moz-transition: none;
    -o-transition: none;
    -ms-transition: none;
    transition: none; }
    .dropdown-menu > li > a img {
      margin-top: -3px; }
  .dropdown-menu > li > a:focus {
    outline: 0 !important; }
  .btn-group.select .dropdown-menu {
    min-width: 100%; }
  .dropdown-menu > li:first-child > a {
    border-top-left-radius: 6px;
    border-top-right-radius: 6px; }
  .dropdown-menu > li:last-child > a {
    border-bottom-left-radius: 6px;
    border-bottom-right-radius: 6px; }
  .select .dropdown-menu > li:first-child > a {
    border-radius: 0;
    border-bottom: 0 none; }
  .dropdown-menu > li > a:hover,
  .dropdown-menu > li > a:focus {
    background-color: #66615B;
    color: rgba(255, 255, 255, 0.7);
    opacity: 1;
    text-decoration: none; }
  .dropdown-menu.dropdown-primary > li > a:hover, .dropdown-menu.dropdown-primary > li > a:focus {
    background-color: #7A9E9F; }
  .dropdown-menu.dropdown-info > li > a:hover, .dropdown-menu.dropdown-info > li > a:focus {
    background-color: #68B3C8; }
  .dropdown-menu.dropdown-success > li > a:hover, .dropdown-menu.dropdown-success > li > a:focus {
    background-color: #7AC29A; }
  .dropdown-menu.dropdown-warning > li > a:hover, .dropdown-menu.dropdown-warning > li > a:focus {
    background-color: #F3BB45; }
  .dropdown-menu.dropdown-danger > li > a:hover, .dropdown-menu.dropdown-danger > li > a:focus {
    background-color: #EB5E28; }

.btn-group.select {
  overflow: hidden; }

.btn-group.select.open {
  overflow: visible; }

.card {
  border-radius: 6px;
  box-shadow: 0 2px 2px rgba(204, 197, 185, 0.5);
  background-color: #FFFFFF;
  color: #252422;
  margin-bottom: 20px;
  position: relative;
  z-index: 1; }
  .card .image {
    width: 100%;
    overflow: hidden;
    height: 260px;
    border-radius: 6px 6px 0 0;
    position: relative;
    -webkit-transform-style: preserve-3d;
    -moz-transform-style: preserve-3d;
    transform-style: preserve-3d; }
    .card .image img {
      width: 100%; }
  .card .content {
    padding: 15px 15px 10px 15px; }
  .card .header {
    padding: 20px 20px 0; }
  .card .description {
    font-size: 16px;
    color: #66615b; }
  .card h6 {
    font-size: 12px;
    margin: 0; }
  .card .category,
  .card label {
    font-size: 14px;
    font-weight: 400;
    color: #9A9A9A;
    margin-bottom: 0px; }
    .card .category i,
    .card label i {
      font-size: 16px; }
  .card label {
    font-size: 15px;
    margin-bottom: 5px; }
  .card .title {
    margin: 0;
    color: #252422;
    font-weight: 300; }
  .card .avatar {
    width: 50px;
    height: 50px;
    overflow: hidden;
    border-radius: 50%;
    margin-right: 5px; }
  .card .footer {
    padding: 0;
    line-height: 30px; }
    .card .footer .legend {
      padding: 5px 0; }
    .card .footer hr {
      margin-top: 5px;
      margin-bottom: 5px; }
  .card .stats {
    color: #a9a9a9;
    font-weight: 300; }
    .card .stats i {
      margin-right: 2px;
      min-width: 15px;
      display: inline-block; }
  .card .footer div {
    display: inline-block; }
  .card .author {
    font-size: 12px;
    font-weight: 600;
    text-transform: uppercase; }
  .card .author i {
    font-size: 14px; }
  .card.card-separator:after {
    height: 100%;
    right: -15px;
    top: 0;
    width: 1px;
    background-color: #DDDDDD;
    content: "";
    position: absolute; }
  .card .ct-chart {
    margin: 30px 0 30px;
    height: 245px; }
  .card .table tbody td:first-child,
  .card .table thead th:first-child {
    padding-left: 15px; }
  .card .table tbody td:last-child,
  .card .table thead th:last-child {
    padding-right: 15px; }
  .card .alert {
    border-radius: 4px;
    position: relative; }
    .card .alert.alert-with-icon {
      padding-left: 65px; }
  .card .icon-big {
    font-size: 3em;
    min-height: 64px; }
  .card .numbers {
    font-size: 2em;
   }
    .card .numbers p {
      margin: 0; }
  .card ul.team-members li {
    padding: 10px 0px; }
    .card ul.team-members li:not(:last-child) {
      border-bottom: 1px solid #F1EAE0; }

.card-user .image {
  border-radius: 8px 8px 0 0;
  height: 150px;
  position: relative;
  overflow: hidden; }
  .card-user .image img {
    width: 100%; }
.card-user .image-plain {
  height: 0;
  margin-top: 110px; }
.card-user .author {
  text-align: center;
  text-transform: none;
  margin-top: -65px; }
  .card-user .author .title {
    color: #403D39; }
    .card-user .author .title small {
      color: #ccc5b9; }
.card-user .avatar {
  width: 100px;
  height: 100px;
  border-radius: 50%;
  position: relative;
  margin-bottom: 15px; }
  .card-user .avatar.border-white {
    border: 5px solid #FFFFFF; }
  .card-user .avatar.border-gray {
    border: 5px solid #ccc5b9; }
.card-user .title {
  font-weight: 600;
  line-height: 24px; }
.card-user .description {
  margin-top: 10px; }
.card-user .content {
  min-height: 200px; }
.card-user.card-plain .avatar {
  height: 190px;
  width: 190px; }

.card-map .map {
  height: 500px;
  padding-top: 20px; }
  .card-map .map > div {
    height: 100%; }

.card-user .footer,
.card-price .footer {
  padding: 5px 15px 10px; }
.card-user hr,
.card-price hr {
  margin: 5px 15px; }

.card-plain {
  background-color: transparent;
  box-shadow: none;
  border-radius: 0; }
  .card-plain .image {
    border-radius: 4px; }

.ct-label {
  fill: rgba(0, 0, 0, 0.4);
  color: rgba(0, 0, 0, 0.4);
  font-size: 0.9em;
  line-height: 1; }

.ct-chart-line .ct-label,
.ct-chart-bar .ct-label {
  display: block;
  display: -webkit-box;
  display: -moz-box;
  display: -ms-flexbox;
  display: -webkit-flex;
  display: flex; }

.ct-label.ct-horizontal.ct-start {
  -webkit-box-align: flex-end;
  -webkit-align-items: flex-end;
  -ms-flex-align: flex-end;
  align-items: flex-end;
  -webkit-box-pack: flex-start;
  -webkit-justify-content: flex-start;
  -ms-flex-pack: flex-start;
  justify-content: flex-start;
  text-align: left;
  text-anchor: start; }

.ct-label.ct-horizontal.ct-end {
  -webkit-box-align: flex-start;
  -webkit-align-items: flex-start;
  -ms-flex-align: flex-start;
  align-items: flex-start;
  -webkit-box-pack: flex-start;
  -webkit-justify-content: flex-start;
  -ms-flex-pack: flex-start;
  justify-content: flex-start;
  text-align: left;
  text-anchor: start; }

.ct-label.ct-vertical.ct-start {
  -webkit-box-align: flex-end;
  -webkit-align-items: flex-end;
  -ms-flex-align: flex-end;
  align-items: flex-end;
  -webkit-box-pack: flex-end;
  -webkit-justify-content: flex-end;
  -ms-flex-pack: flex-end;
  justify-content: flex-end;
  text-align: right;
  text-anchor: end; }

.ct-label.ct-vertical.ct-end {
  -webkit-box-align: flex-end;
  -webkit-align-items: flex-end;
  -ms-flex-align: flex-end;
  align-items: flex-end;
  -webkit-box-pack: flex-start;
  -webkit-justify-content: flex-start;
  -ms-flex-pack: flex-start;
  justify-content: flex-start;
  text-align: left;
  text-anchor: start; }

.ct-chart-bar .ct-label.ct-horizontal.ct-start {
  -webkit-box-align: flex-end;
  -webkit-align-items: flex-end;
  -ms-flex-align: flex-end;
  align-items: flex-end;
  -webkit-box-pack: center;
  -webkit-justify-content: center;
  -ms-flex-pack: center;
  justify-content: center;
  text-align: center;
  text-anchor: start; }

.ct-chart-bar .ct-label.ct-horizontal.ct-end {
  -webkit-box-align: flex-start;
  -webkit-align-items: flex-start;
  -ms-flex-align: flex-start;
  align-items: flex-start;
  -webkit-box-pack: center;
  -webkit-justify-content: center;
  -ms-flex-pack: center;
  justify-content: center;
  text-align: center;
  text-anchor: start; }

.ct-chart-bar.ct-horizontal-bars .ct-label.ct-horizontal.ct-start {
  -webkit-box-align: flex-end;
  -webkit-align-items: flex-end;
  -ms-flex-align: flex-end;
  align-items: flex-end;
  -webkit-box-pack: flex-start;
  -webkit-justify-content: flex-start;
  -ms-flex-pack: flex-start;
  justify-content: flex-start;
  text-align: left;
  text-anchor: start; }

.ct-chart-bar.ct-horizontal-bars .ct-label.ct-horizontal.ct-end {
  -webkit-box-align: flex-start;
  -webkit-align-items: flex-start;
  -ms-flex-align: flex-start;
  align-items: flex-start;
  -webkit-box-pack: flex-start;
  -webkit-justify-content: flex-start;
  -ms-flex-pack: flex-start;
  justify-content: flex-start;
  text-align: left;
  text-anchor: start; }

.ct-chart-bar.ct-horizontal-bars .ct-label.ct-vertical.ct-start {
  -webkit-box-align: center;
  -webkit-align-items: center;
  -ms-flex-align: center;
  align-items: center;
  -webkit-box-pack: flex-end;
  -webkit-justify-content: flex-end;
  -ms-flex-pack: flex-end;
  justify-content: flex-end;
  text-align: right;
  text-anchor: end; }

.ct-chart-bar.ct-horizontal-bars .ct-label.ct-vertical.ct-end {
  -webkit-box-align: center;
  -webkit-align-items: center;
  -ms-flex-align: center;
  align-items: center;
  -webkit-box-pack: flex-start;
  -webkit-justify-content: flex-start;
  -ms-flex-pack: flex-start;
  justify-content: flex-start;
  text-align: left;
  text-anchor: end; }

.ct-grid {
  stroke: rgba(0, 0, 0, 0.2);
  stroke-width: 1px;
  stroke-dasharray: 2px; }

.ct-point {
  stroke-width: 10px;
  stroke-linecap: round; }

.ct-line {
  fill: none;
  stroke-width: 4px; }

.ct-area {
  stroke: none;
  fill-opacity: 0.7; }

.ct-bar {
  fill: none;
  stroke-width: 10px; }

.ct-slice-donut {
  fill: none;
  stroke-width: 60px; }

.ct-series-a .ct-point, .ct-series-a .ct-line, .ct-series-a .ct-bar, .ct-series-a .ct-slice-donut {
  stroke: #68B3C8; }
.ct-series-a .ct-slice-pie, .ct-series-a .ct-area {
  fill: #68B3C8; }

.ct-series-b .ct-point, .ct-series-b .ct-line, .ct-series-b .ct-bar, .ct-series-b .ct-slice-donut {
  stroke: #F3BB45; }
.ct-series-b .ct-slice-pie, .ct-series-b .ct-area {
  fill: #F3BB45; }

.ct-series-c .ct-point, .ct-series-c .ct-line, .ct-series-c .ct-bar, .ct-series-c .ct-slice-donut {
  stroke: #EB5E28; }
.ct-series-c .ct-slice-pie, .ct-series-c .ct-area {
  fill: #EB5E28; }

.ct-series-d .ct-point, .ct-series-d .ct-line, .ct-series-d .ct-bar, .ct-series-d .ct-slice-donut {
  stroke: #7AC29A; }
.ct-series-d .ct-slice-pie, .ct-series-d .ct-area {
  fill: #7AC29A; }

.ct-series-e .ct-point, .ct-series-e .ct-line, .ct-series-e .ct-bar, .ct-series-e .ct-slice-donut {
  stroke: #7A9E9F; }
.ct-series-e .ct-slice-pie, .ct-series-e .ct-area {
  fill: #7A9E9F; }

.ct-series-f .ct-point, .ct-series-f .ct-line, .ct-series-f .ct-bar, .ct-series-f .ct-slice-donut {
  stroke: rgba(104, 179, 200, 0.8); }
.ct-series-f .ct-slice-pie, .ct-series-f .ct-area {
  fill: rgba(104, 179, 200, 0.8); }

.ct-series-g .ct-point, .ct-series-g .ct-line, .ct-series-g .ct-bar, .ct-series-g .ct-slice-donut {
  stroke: rgba(122, 194, 154, 0.8); }
.ct-series-g .ct-slice-pie, .ct-series-g .ct-area {
  fill: rgba(122, 194, 154, 0.8); }

.ct-series-h .ct-point, .ct-series-h .ct-line, .ct-series-h .ct-bar, .ct-series-h .ct-slice-donut {
  stroke: rgba(243, 187, 69, 0.8); }
.ct-series-h .ct-slice-pie, .ct-series-h .ct-area {
  fill: rgba(243, 187, 69, 0.8); }

.ct-series-i .ct-point, .ct-series-i .ct-line, .ct-series-i .ct-bar, .ct-series-i .ct-slice-donut {
  stroke: rgba(235, 94, 40, 0.8); }
.ct-series-i .ct-slice-pie, .ct-series-i .ct-area {
  fill: rgba(235, 94, 40, 0.8); }

.ct-series-j .ct-point, .ct-series-j .ct-line, .ct-series-j .ct-bar, .ct-series-j .ct-slice-donut {
  stroke: rgba(122, 158, 159, 0.8); }
.ct-series-j .ct-slice-pie, .ct-series-j .ct-area {
  fill: rgba(122, 158, 159, 0.8); }

.ct-series-k .ct-point, .ct-series-k .ct-line, .ct-series-k .ct-bar, .ct-series-k .ct-slice-donut {
  stroke: rgba(104, 179, 200, 0.6); }
.ct-series-k .ct-slice-pie, .ct-series-k .ct-area {
  fill: rgba(104, 179, 200, 0.6); }

.ct-series-l .ct-point, .ct-series-l .ct-line, .ct-series-l .ct-bar, .ct-series-l .ct-slice-donut {
  stroke: rgba(122, 194, 154, 0.6); }
.ct-series-l .ct-slice-pie, .ct-series-l .ct-area {
  fill: rgba(122, 194, 154, 0.6); }

.ct-series-m .ct-point, .ct-series-m .ct-line, .ct-series-m .ct-bar, .ct-series-m .ct-slice-donut {
  stroke: rgba(243, 187, 69, 0.6); }
.ct-series-m .ct-slice-pie, .ct-series-m .ct-area {
  fill: rgba(243, 187, 69, 0.6); }

.ct-series-n .ct-point, .ct-series-n .ct-line, .ct-series-n .ct-bar, .ct-series-n .ct-slice-donut {
  stroke: rgba(235, 94, 40, 0.6); }
.ct-series-n .ct-slice-pie, .ct-series-n .ct-area {
  fill: rgba(235, 94, 40, 0.6); }

.ct-series-o .ct-point, .ct-series-o .ct-line, .ct-series-o .ct-bar, .ct-series-o .ct-slice-donut {
  stroke: rgba(122, 158, 159, 0.6); }
.ct-series-o .ct-slice-pie, .ct-series-o .ct-area {
  fill: rgba(122, 158, 159, 0.6); }

.ct-square {
  display: block;
  position: relative;
  width: 100%; }
  .ct-square:before {
    display: block;
    float: left;
    content: "";
    width: 0;
    height: 0;
    padding-bottom: 100%; }
  .ct-square:after {
    content: "";
    display: table;
    clear: both; }
  .ct-square > svg {
    display: block;
    position: absolute;
    top: 0;
    left: 0; }

.ct-minor-second {
  display: block;
  position: relative;
  width: 100%; }
  .ct-minor-second:before {
    display: block;
    float: left;
    content: "";
    width: 0;
    height: 0;
    padding-bottom: 93.75%; }
  .ct-minor-second:after {
    content: "";
    display: table;
    clear: both; }
  .ct-minor-second > svg {
    display: block;
    position: absolute;
    top: 0;
    left: 0; }

.ct-major-second {
  display: block;
  position: relative;
  width: 100%; }
  .ct-major-second:before {
    display: block;
    float: left;
    content: "";
    width: 0;
    height: 0;
    padding-bottom: 88.88889%; }
  .ct-major-second:after {
    content: "";
    display: table;
    clear: both; }
  .ct-major-second > svg {
    display: block;
    position: absolute;
    top: 0;
    left: 0; }

.ct-minor-third {
  display: block;
  position: relative;
  width: 100%; }
  .ct-minor-third:before {
    display: block;
    float: left;
    content: "";
    width: 0;
    height: 0;
    padding-bottom: 83.33333%; }
  .ct-minor-third:after {
    content: "";
    display: table;
    clear: both; }
  .ct-minor-third > svg {
    display: block;
    position: absolute;
    top: 0;
    left: 0; }

.ct-major-third {
  display: block;
  position: relative;
  width: 100%; }
  .ct-major-third:before {
    display: block;
    float: left;
    content: "";
    width: 0;
    height: 0;
    padding-bottom: 80%; }
  .ct-major-third:after {
    content: "";
    display: table;
    clear: both; }
  .ct-major-third > svg {
    display: block;
    position: absolute;
    top: 0;
    left: 0; }

.ct-perfect-fourth {
  display: block;
  position: relative;
  width: 100%; }
  .ct-perfect-fourth:before {
    display: block;
    float: left;
    content: "";
    width: 0;
    height: 0;
    padding-bottom: 75%; }
  .ct-perfect-fourth:after {
    content: "";
    display: table;
    clear: both; }
  .ct-perfect-fourth > svg {
    display: block;
    position: absolute;
    top: 0;
    left: 0; }

.ct-perfect-fifth {
  display: block;
  position: relative;
  width: 100%; }
  .ct-perfect-fifth:before {
    display: block;
    float: left;
    content: "";
    width: 0;
    height: 0;
    padding-bottom: 66.66667%; }
  .ct-perfect-fifth:after {
    content: "";
    display: table;
    clear: both; }
  .ct-perfect-fifth > svg {
    display: block;
    position: absolute;
    top: 0;
    left: 0; }

.ct-minor-sixth {
  display: block;
  position: relative;
  width: 100%; }
  .ct-minor-sixth:before {
    display: block;
    float: left;
    content: "";
    width: 0;
    height: 0;
    padding-bottom: 62.5%; }
  .ct-minor-sixth:after {
    content: "";
    display: table;
    clear: both; }
  .ct-minor-sixth > svg {
    display: block;
    position: absolute;
    top: 0;
    left: 0; }

.ct-golden-section {
  display: block;
  position: relative;
  width: 100%; }
  .ct-golden-section:before {
    display: block;
    float: left;
    content: "";
    width: 0;
    height: 0;
    padding-bottom: 61.8047%; }
  .ct-golden-section:after {
    content: "";
    display: table;
    clear: both; }
  .ct-golden-section > svg {
    display: block;
    position: absolute;
    top: 0;
    left: 0; }

.ct-major-sixth {
  display: block;
  position: relative;
  width: 100%; }
  .ct-major-sixth:before {
    display: block;
    float: left;
    content: "";
    width: 0;
    height: 0;
    padding-bottom: 60%; }
  .ct-major-sixth:after {
    content: "";
    display: table;
    clear: both; }
  .ct-major-sixth > svg {
    display: block;
    position: absolute;
    top: 0;
    left: 0; }

.ct-minor-seventh {
  display: block;
  position: relative;
  width: 100%; }
  .ct-minor-seventh:before {
    display: block;
    float: left;
    content: "";
    width: 0;
    height: 0;
    padding-bottom: 56.25%; }
  .ct-minor-seventh:after {
    content: "";
    display: table;
    clear: both; }
  .ct-minor-seventh > svg {
    display: block;
    position: absolute;
    top: 0;
    left: 0; }

.ct-major-seventh {
  display: block;
  position: relative;
  width: 100%; }
  .ct-major-seventh:before {
    display: block;
    float: left;
    content: "";
    width: 0;
    height: 0;
    padding-bottom: 53.33333%; }
  .ct-major-seventh:after {
    content: "";
    display: table;
    clear: both; }
  .ct-major-seventh > svg {
    display: block;
    position: absolute;
    top: 0;
    left: 0; }

.ct-octave {
  display: block;
  position: relative;
  width: 100%; }
  .ct-octave:before {
    display: block;
    float: left;
    content: "";
    width: 0;
    height: 0;
    padding-bottom: 50%; }
  .ct-octave:after {
    content: "";
    display: table;
    clear: both; }
  .ct-octave > svg {
    display: block;
    position: absolute;
    top: 0;
    left: 0; }

.ct-major-tenth {
  display: block;
  position: relative;
  width: 100%; }
  .ct-major-tenth:before {
    display: block;
    float: left;
    content: "";
    width: 0;
    height: 0;
    padding-bottom: 40%; }
  .ct-major-tenth:after {
    content: "";
    display: table;
    clear: both; }
  .ct-major-tenth > svg {
    display: block;
    position: absolute;
    top: 0;
    left: 0; }

.ct-major-eleventh {
  display: block;
  position: relative;
  width: 100%; }
  .ct-major-eleventh:before {
    display: block;
    float: left;
    content: "";
    width: 0;
    height: 0;
    padding-bottom: 37.5%; }
  .ct-major-eleventh:after {
    content: "";
    display: table;
    clear: both; }
  .ct-major-eleventh > svg {
    display: block;
    position: absolute;
    top: 0;
    left: 0; }

.ct-major-twelfth {
  display: block;
  position: relative;
  width: 100%; }
  .ct-major-twelfth:before {
    display: block;
    float: left;
    content: "";
    width: 0;
    height: 0;
    padding-bottom: 33.33333%; }
  .ct-major-twelfth:after {
    content: "";
    display: table;
    clear: both; }
  .ct-major-twelfth > svg {
    display: block;
    position: absolute;
    top: 0;
    left: 0; }

.ct-double-octave {
  display: block;
  position: relative;
  width: 100%; }
  .ct-double-octave:before {
    display: block;
    float: left;
    content: "";
    width: 0;
    height: 0;
    padding-bottom: 25%; }
  .ct-double-octave:after {
    content: "";
    display: table;
    clear: both; }
  .ct-double-octave > svg {
    display: block;
    position: absolute;
    top: 0;
    left: 0; }

@media (min-width: 992px) {
  .navbar {
    min-height: 75px; }

  .navbar-form {
    margin-top: 21px;
    margin-bottom: 21px;
    padding-left: 5px;
    padding-right: 5px; }

  .navbar-search-form {
    display: none; }

  .navbar-nav > li > .dropdown-menu,
  .dropdown .dropdown-menu {
    transform: translate3d(0px, -40px, 0px);
    transition: all 0.3s cubic-bezier(0.215, 0.61, 0.355, 1) 0s, opacity 0.3s ease 0s, height 0s linear 0.35s; }

  .navbar-nav > li.open > .dropdown-menu, .dropdown.open .dropdown-menu {
    transform: translate3d(0px, 0px, 0px); }

  .navbar-nav > li > .dropdown-menu:before {
    border-bottom: 11px solid #F1EAE0;
    border-left: 11px solid transparent;
    border-right: 11px solid transparent;
    content: "";
    display: inline-block;
    position: absolute;
    right: 12px;
    top: -11px; }

  .navbar-nav > li > .dropdown-menu:after {
    border-bottom: 11px solid #FFFCF5;
    border-left: 11px solid transparent;
    border-right: 11px solid transparent;
    content: "";
    display: inline-block;
    position: absolute;
    right: 12px;
    top: -10px; }

  .navbar-nav.navbar-left > li > .dropdown-menu:before {
    right: auto;
    left: 12px; }

  .navbar-nav.navbar-left > li > .dropdown-menu:after {
    right: auto;
    left: 12px; }

  .navbar .navbar-header {
    margin-left: 10px; }

  .footer:not(.footer-big) nav > ul li:first-child {
    margin-left: 0; }

  body > .navbar-collapse.collapse {
    display: none !important; }

  .card form [class*="col-"] {
    padding: 6px; }
  .card form [class*="col-"]:first-child {
    padding-left: 15px; }
  .card form [class*="col-"]:last-child {
    padding-right: 15px; } }
/*          Changes for small display      */
@media (max-width: 991px) {
  .sidebar {
    display: none; }

  .main-panel {
    width: 100%; }

  .navbar-transparent {
    padding-top: 15px;
    background-color: rgba(0, 0, 0, 0.45); }

  body {
    position: relative; }

  h6 {
    font-size: 1em; }

  .wrapper {
    -webkit-transform: translate3d(0px, 0, 0);
    -moz-transform: translate3d(0px, 0, 0);
    -o-transform: translate3d(0px, 0, 0);
    -ms-transform: translate3d(0px, 0, 0);
    transform: translate3d(0px, 0, 0);
    -webkit-transition: all 0.33s cubic-bezier(0.685, 0.0473, 0.346, 1);
    -moz-transition: all 0.33s cubic-bezier(0.685, 0.0473, 0.346, 1);
    -o-transition: all 0.33s cubic-bezier(0.685, 0.0473, 0.346, 1);
    -ms-transition: all 0.33s cubic-bezier(0.685, 0.0473, 0.346, 1);
    transition: all 0.33s cubic-bezier(0.685, 0.0473, 0.346, 1);
    left: 0;
    background-color: white; }

  .navbar .container {
    left: 0;
    width: 100%;
    -webkit-transition: all 0.33s cubic-bezier(0.685, 0.0473, 0.346, 1);
    -moz-transition: all 0.33s cubic-bezier(0.685, 0.0473, 0.346, 1);
    -o-transition: all 0.33s cubic-bezier(0.685, 0.0473, 0.346, 1);
    -ms-transition: all 0.33s cubic-bezier(0.685, 0.0473, 0.346, 1);
    transition: all 0.33s cubic-bezier(0.685, 0.0473, 0.346, 1);
    position: relative; }

  .navbar .navbar-collapse.collapse,
  .navbar .navbar-collapse.collapse.in,
  .navbar .navbar-collapse.collapsing {
    display: none !important; }

  .navbar-nav > li {
    float: none;
    position: relative;
    display: block; }

  .off-canvas-sidebar {
    position: fixed;
    display: block;
    top: 0;
    height: 100%;
    width: 230px;
    right: 0;
    z-index: 1032;
    visibility: visible;
    background-color: #999;
    overflow-y: visible;
    border-top: none;
    text-align: left;
    padding-right: 0px;
    padding-left: 0;
    -webkit-transform: translate3d(230px, 0, 0);
    -moz-transform: translate3d(230px, 0, 0);
    -o-transform: translate3d(230px, 0, 0);
    -ms-transform: translate3d(230px, 0, 0);
    transform: translate3d(230px, 0, 0);
    -webkit-transition: all 0.33s cubic-bezier(0.685, 0.0473, 0.346, 1);
    -moz-transition: all 0.33s cubic-bezier(0.685, 0.0473, 0.346, 1);
    -o-transition: all 0.33s cubic-bezier(0.685, 0.0473, 0.346, 1);
    -ms-transition: all 0.33s cubic-bezier(0.685, 0.0473, 0.346, 1);
    transition: all 0.33s cubic-bezier(0.685, 0.0473, 0.346, 1); }
    .off-canvas-sidebar .sidebar-wrapper {
      position: relative;
      z-index: 3;
      overflow-y: scroll;
      height: 100%;
      box-shadow: inset 1px 0px 0px 0px #DDDDDD; }
    .off-canvas-sidebar .nav {
      margin-top: 0;
      padding: 10px 15px 0; }
      .off-canvas-sidebar .nav > li > a {
        margin: 0px 0px;
        color: #66615B;
        text-transform: uppercase;
        font-weight: 600;
        font-size: 12px;
        line-height: 1.4em;
        padding: 10px 0; }
        .off-canvas-sidebar .nav > li > a:hover, .off-canvas-sidebar .nav > li > a.active {
          color: #403D39; }
        .off-canvas-sidebar .nav > li > a p,
        .off-canvas-sidebar .nav > li > a .notification,
        .off-canvas-sidebar .nav > li > a .caret {
          display: inline-block; }
        .off-canvas-sidebar .nav > li > a .caret {
          float: right;
          position: relative;
          top: 12px; }
        .off-canvas-sidebar .nav > li > a i {
          font-size: 18px;
          margin-right: 10px;
          line-height: 26px; }
      .off-canvas-sidebar .nav > li.active > a:before {
        border-right: none;
        border-left: 12px solid #DDDDDD;
        border-top: 12px solid transparent;
        border-bottom: 12px solid transparent;
        right: auto;
        margin-left: -15px;
        left: 0px;
        top: 10px; }
      .off-canvas-sidebar .nav > li.active > a:after {
        border-right: none;
        border-left: 12px solid #f4f3ef;
        border-top: 12px solid transparent;
        border-bottom: 12px solid transparent;
        right: auto;
        margin-left: -15px;
        left: -1px;
        top: 10px; }
    .off-canvas-sidebar::after {
      top: 0;
      left: 0;
      height: 100%;
      width: 100%;
      position: absolute;
      background-color: #f4f3ef;
      background-image: linear-gradient(to bottom, transparent 0%, rgba(112, 112, 112, 0) 60%, rgba(186, 186, 186, 0.15) 100%);
      display: block;
      content: "";
      z-index: 1; }
    .off-canvas-sidebar.has-image::after {
      top: 0;
      left: 0;
      height: 100%;
      width: 100%;
      position: absolute;
      background-color: rgba(17, 17, 17, 0.8);
      display: block;
      content: "";
      z-index: 1; }
    .off-canvas-sidebar .logo {
      position: relative;
      z-index: 4;
      padding-top: 11px;
      padding-bottom: 11px; }
    .off-canvas-sidebar .divider {
      height: 1px;
      margin: 10px 0; }

  .nav-open .navbar-collapse {
    -webkit-transform: translate3d(0px, 0, 0);
    -moz-transform: translate3d(0px, 0, 0);
    -o-transform: translate3d(0px, 0, 0);
    -ms-transform: translate3d(0px, 0, 0);
    transform: translate3d(0px, 0, 0); }

  .nav-open .navbar .container {
    left: -230px; }

  .nav-open .wrapper {
    left: 0;
    -webkit-transform: translate3d(-230px, 0, 0);
    -moz-transform: translate3d(-230px, 0, 0);
    -o-transform: translate3d(-230px, 0, 0);
    -ms-transform: translate3d(-230px, 0, 0);
    transform: translate3d(-230px, 0, 0); }

  .navbar-toggle .icon-bar {
    display: block;
    position: relative;
    background: #fff;
    width: 24px;
    height: 2px;
    border-radius: 1px;
    margin: 0 auto; }

  .navbar-header .navbar-toggle {
    margin: 10px 15px 10px 0;
    width: 40px;
    height: 40px; }

  .bar1,
  .bar2,
  .bar3 {
    outline: 1px solid transparent; }

  .bar1 {
    top: 0px;
    -webkit-animation: topbar-back 500ms linear 0s;
    -moz-animation: topbar-back 500ms linear 0s;
    animation: topbar-back 500ms 0s;
    -webkit-animation-fill-mode: forwards;
    -moz-animation-fill-mode: forwards;
    animation-fill-mode: forwards; }

  .bar2 {
    opacity: 1; }

  .bar3 {
    bottom: 0px;
    -webkit-animation: bottombar-back 500ms linear 0s;
    -moz-animation: bottombar-back 500ms linear 0s;
    animation: bottombar-back 500ms 0s;
    -webkit-animation-fill-mode: forwards;
    -moz-animation-fill-mode: forwards;
    animation-fill-mode: forwards; }

  .toggled .bar1 {
    top: 6px;
    -webkit-animation: topbar-x 500ms linear 0s;
    -moz-animation: topbar-x 500ms linear 0s;
    animation: topbar-x 500ms 0s;
    -webkit-animation-fill-mode: forwards;
    -moz-animation-fill-mode: forwards;
    animation-fill-mode: forwards; }

  .toggled .bar2 {
    opacity: 0; }

  .toggled .bar3 {
    bottom: 6px;
    -webkit-animation: bottombar-x 500ms linear 0s;
    -moz-animation: bottombar-x 500ms linear 0s;
    animation: bottombar-x 500ms 0s;
    -webkit-animation-fill-mode: forwards;
    -moz-animation-fill-mode: forwards;
    animation-fill-mode: forwards; }

  @keyframes topbar-x {
    0% {
      top: 0px;
      transform: rotate(0deg); }
    45% {
      top: 6px;
      transform: rotate(145deg); }
    75% {
      transform: rotate(130deg); }
    100% {
      transform: rotate(135deg); } }
  @-webkit-keyframes topbar-x {
    0% {
      top: 0px;
      -webkit-transform: rotate(0deg); }
    45% {
      top: 6px;
      -webkit-transform: rotate(145deg); }
    75% {
      -webkit-transform: rotate(130deg); }
    100% {
      -webkit-transform: rotate(135deg); } }
  @-moz-keyframes topbar-x {
    0% {
      top: 0px;
      -moz-transform: rotate(0deg); }
    45% {
      top: 6px;
      -moz-transform: rotate(145deg); }
    75% {
      -moz-transform: rotate(130deg); }
    100% {
      -moz-transform: rotate(135deg); } }
  @keyframes topbar-back {
    0% {
      top: 6px;
      transform: rotate(135deg); }
    45% {
      transform: rotate(-10deg); }
    75% {
      transform: rotate(5deg); }
    100% {
      top: 0px;
      transform: rotate(0); } }
  @-webkit-keyframes topbar-back {
    0% {
      top: 6px;
      -webkit-transform: rotate(135deg); }
    45% {
      -webkit-transform: rotate(-10deg); }
    75% {
      -webkit-transform: rotate(5deg); }
    100% {
      top: 0px;
      -webkit-transform: rotate(0); } }
  @-moz-keyframes topbar-back {
    0% {
      top: 6px;
      -moz-transform: rotate(135deg); }
    45% {
      -moz-transform: rotate(-10deg); }
    75% {
      -moz-transform: rotate(5deg); }
    100% {
      top: 0px;
      -moz-transform: rotate(0); } }
  @keyframes bottombar-x {
    0% {
      bottom: 0px;
      transform: rotate(0deg); }
    45% {
      bottom: 6px;
      transform: rotate(-145deg); }
    75% {
      transform: rotate(-130deg); }
    100% {
      transform: rotate(-135deg); } }
  @-webkit-keyframes bottombar-x {
    0% {
      bottom: 0px;
      -webkit-transform: rotate(0deg); }
    45% {
      bottom: 6px;
      -webkit-transform: rotate(-145deg); }
    75% {
      -webkit-transform: rotate(-130deg); }
    100% {
      -webkit-transform: rotate(-135deg); } }
  @-moz-keyframes bottombar-x {
    0% {
      bottom: 0px;
      -moz-transform: rotate(0deg); }
    45% {
      bottom: 6px;
      -moz-transform: rotate(-145deg); }
    75% {
      -moz-transform: rotate(-130deg); }
    100% {
      -moz-transform: rotate(-135deg); } }
  @keyframes bottombar-back {
    0% {
      bottom: 6px;
      transform: rotate(-135deg); }
    45% {
      transform: rotate(10deg); }
    75% {
      transform: rotate(-5deg); }
    100% {
      bottom: 0px;
      transform: rotate(0); } }
  @-webkit-keyframes bottombar-back {
    0% {
      bottom: 6px;
      -webkit-transform: rotate(-135deg); }
    45% {
      -webkit-transform: rotate(10deg); }
    75% {
      -webkit-transform: rotate(-5deg); }
    100% {
      bottom: 0px;
      -webkit-transform: rotate(0); } }
  @-moz-keyframes bottombar-back {
    0% {
      bottom: 6px;
      -moz-transform: rotate(-135deg); }
    45% {
      -moz-transform: rotate(10deg); }
    75% {
      -moz-transform: rotate(-5deg); }
    100% {
      bottom: 0px;
      -moz-transform: rotate(0); } }
  @-webkit-keyframes fadeIn {
    0% {
      opacity: 0; }
    100% {
      opacity: 1; } }
  @-moz-keyframes fadeIn {
    0% {
      opacity: 0; }
    100% {
      opacity: 1; } }
  @keyframes fadeIn {
    0% {
      opacity: 0; }
    100% {
      opacity: 1; } }
  .dropdown-menu .divider {
    background-color: rgba(229, 229, 229, 0.15); }

  .navbar-nav {
    margin: 1px 0; }

  .dropdown-menu {
    display: none; }
    .dropdown-menu > li > a:hover, .dropdown-menu > li > a:focus {
      background-color: transparent; }

  .navbar-fixed-top {
    -webkit-backface-visibility: hidden; }

  #bodyClick {
    height: 100%;
    width: 100%;
    position: fixed;
    opacity: 0;
    top: 0;
    left: auto;
    right: 230px;
    content: "";
    z-index: 9999;
    overflow-x: hidden; }

  .form-control + .form-control-feedback {
    margin-top: -8px; }

  .navbar-toggle:hover, .navbar-toggle:focus {
    background-color: transparent !important; }

  .btn.dropdown-toggle {
    margin-bottom: 0; }

  .media-post .author {
    width: 20%;
    float: none !important;
    display: block;
    margin: 0 auto 10px; }

  .media-post .media-body {
    width: 100%; }

  .navbar-collapse.collapse {
    height: 100% !important; }

  .navbar-collapse.collapse.in {
    display: block; }

  .navbar-header .collapse, .navbar-toggle {
    display: block !important; }

  .navbar-header {
    float: none; }

  .navbar-nav .open .dropdown-menu {
    position: static;
    float: none;
    width: auto;
    margin-top: 0;
    background-color: transparent;
    border: 0;
    -webkit-box-shadow: none;
    box-shadow: none; }

  .main-panel > .content {
    padding-left: 0;
    padding-right: 0; }

  .nav .open > a, .nav .open > a:focus, .nav .open > a:hover {
    background-color: transparent; }

  .footer .copyright {
    padding: 0px 15px;
    width: 100%; } }
@media (min-width: 992px) {
  .table-full-width {
    margin-left: -15px;
    margin-right: -15px; }

  .table-responsive {
    overflow: visible; } }
@media (max-width: 991px) {
  .table-responsive {
    width: 100%;
    margin-bottom: 15px;
    border: 1px solid #dddddd;
    overflow-x: scroll;
    overflow-y: hidden;
    -ms-overflow-style: -ms-autohiding-scrollbar;
    -webkit-overflow-scrolling: touch; } }


File: /assets\css\themify-icons.css
@font-face {
	font-family: 'themify';
	src:url('../fonts/themify.eot?-fvbane');
	src:url('../fonts/themify.eot?#iefix-fvbane') format('embedded-opentype'),
		url('../fonts/themify.woff?-fvbane') format('woff'),
		url('../fonts/themify.ttf?-fvbane') format('truetype'),
		url('../fonts/themify.svg?-fvbane#themify') format('svg');
	font-weight: normal;
	font-style: normal;
}

[class^="ti-"], [class*=" ti-"] {
	font-family: 'themify';
	speak: none;
	font-style: normal;
	font-weight: bold;
	font-variant: normal;
	text-transform: none;
	line-height: 1.42857;

	/* Better Font Rendering =========== */
	-webkit-font-smoothing: antialiased;
	-moz-osx-font-smoothing: grayscale;
}

.ti-wand:before {
	content: "\e600";
}
.ti-volume:before {
	content: "\e601";
}
.ti-user:before {
	content: "\e602";
}
.ti-unlock:before {
	content: "\e603";
}
.ti-unlink:before {
	content: "\e604";
}
.ti-trash:before {
	content: "\e605";
}
.ti-thought:before {
	content: "\e606";
}
.ti-target:before {
	content: "\e607";
}
.ti-tag:before {
	content: "\e608";
}
.ti-tablet:before {
	content: "\e609";
}
.ti-star:before {
	content: "\e60a";
}
.ti-spray:before {
	content: "\e60b";
}
.ti-signal:before {
	content: "\e60c";
}
.ti-shopping-cart:before {
	content: "\e60d";
}
.ti-shopping-cart-full:before {
	content: "\e60e";
}
.ti-settings:before {
	content: "\e60f";
}
.ti-search:before {
	content: "\e610";
}
.ti-zoom-in:before {
	content: "\e611";
}
.ti-zoom-out:before {
	content: "\e612";
}
.ti-cut:before {
	content: "\e613";
}
.ti-ruler:before {
	content: "\e614";
}
.ti-ruler-pencil:before {
	content: "\e615";
}
.ti-ruler-alt:before {
	content: "\e616";
}
.ti-bookmark:before {
	content: "\e617";
}
.ti-bookmark-alt:before {
	content: "\e618";
}
.ti-reload:before {
	content: "\e619";
}
.ti-plus:before {
	content: "\e61a";
}
.ti-pin:before {
	content: "\e61b";
}
.ti-pencil:before {
	content: "\e61c";
}
.ti-pencil-alt:before {
	content: "\e61d";
}
.ti-paint-roller:before {
	content: "\e61e";
}
.ti-paint-bucket:before {
	content: "\e61f";
}
.ti-na:before {
	content: "\e620";
}
.ti-mobile:before {
	content: "\e621";
}
.ti-minus:before {
	content: "\e622";
}
.ti-medall:before {
	content: "\e623";
}
.ti-medall-alt:before {
	content: "\e624";
}
.ti-marker:before {
	content: "\e625";
}
.ti-marker-alt:before {
	content: "\e626";
}
.ti-arrow-up:before {
	content: "\e627";
}
.ti-arrow-right:before {
	content: "\e628";
}
.ti-arrow-left:before {
	content: "\e629";
}
.ti-arrow-down:before {
	content: "\e62a";
}
.ti-lock:before {
	content: "\e62b";
}
.ti-location-arrow:before {
	content: "\e62c";
}
.ti-link:before {
	content: "\e62d";
}
.ti-layout:before {
	content: "\e62e";
}
.ti-layers:before {
	content: "\e62f";
}
.ti-layers-alt:before {
	content: "\e630";
}
.ti-key:before {
	content: "\e631";
}
.ti-import:before {
	content: "\e632";
}
.ti-image:before {
	content: "\e633";
}
.ti-heart:before {
	content: "\e634";
}
.ti-heart-broken:before {
	content: "\e635";
}
.ti-hand-stop:before {
	content: "\e636";
}
.ti-hand-open:before {
	content: "\e637";
}
.ti-hand-drag:before {
	content: "\e638";
}
.ti-folder:before {
	content: "\e639";
}
.ti-flag:before {
	content: "\e63a";
}
.ti-flag-alt:before {
	content: "\e63b";
}
.ti-flag-alt-2:before {
	content: "\e63c";
}
.ti-eye:before {
	content: "\e63d";
}
.ti-export:before {
	content: "\e63e";
}
.ti-exchange-vertical:before {
	content: "\e63f";
}
.ti-desktop:before {
	content: "\e640";
}
.ti-cup:before {
	content: "\e641";
}
.ti-crown:before {
	content: "\e642";
}
.ti-comments:before {
	content: "\e643";
}
.ti-comment:before {
	content: "\e644";
}
.ti-comment-alt:before {
	content: "\e645";
}
.ti-close:before {
	content: "\e646";
}
.ti-clip:before {
	content: "\e647";
}
.ti-angle-up:before {
	content: "\e648";
}
.ti-angle-right:before {
	content: "\e649";
}
.ti-angle-left:before {
	content: "\e64a";
}
.ti-angle-down:before {
	content: "\e64b";
}
.ti-check:before {
	content: "\e64c";
}
.ti-check-box:before {
	content: "\e64d";
}
.ti-camera:before {
	content: "\e64e";
}
.ti-announcement:before {
	content: "\e64f";
}
.ti-brush:before {
	content: "\e650";
}
.ti-briefcase:before {
	content: "\e651";
}
.ti-bolt:before {
	content: "\e652";
}
.ti-bolt-alt:before {
	content: "\e653";
}
.ti-blackboard:before {
	content: "\e654";
}
.ti-bag:before {
	content: "\e655";
}
.ti-move:before {
	content: "\e656";
}
.ti-arrows-vertical:before {
	content: "\e657";
}
.ti-arrows-horizontal:before {
	content: "\e658";
}
.ti-fullscreen:before {
	content: "\e659";
}
.ti-arrow-top-right:before {
	content: "\e65a";
}
.ti-arrow-top-left:before {
	content: "\e65b";
}
.ti-arrow-circle-up:before {
	content: "\e65c";
}
.ti-arrow-circle-right:before {
	content: "\e65d";
}
.ti-arrow-circle-left:before {
	content: "\e65e";
}
.ti-arrow-circle-down:before {
	content: "\e65f";
}
.ti-angle-double-up:before {
	content: "\e660";
}
.ti-angle-double-right:before {
	content: "\e661";
}
.ti-angle-double-left:before {
	content: "\e662";
}
.ti-angle-double-down:before {
	content: "\e663";
}
.ti-zip:before {
	content: "\e664";
}
.ti-world:before {
	content: "\e665";
}
.ti-wheelchair:before {
	content: "\e666";
}
.ti-view-list:before {
	content: "\e667";
}
.ti-view-list-alt:before {
	content: "\e668";
}
.ti-view-grid:before {
	content: "\e669";
}
.ti-uppercase:before {
	content: "\e66a";
}
.ti-upload:before {
	content: "\e66b";
}
.ti-underline:before {
	content: "\e66c";
}
.ti-truck:before {
	content: "\e66d";
}
.ti-timer:before {
	content: "\e66e";
}
.ti-ticket:before {
	content: "\e66f";
}
.ti-thumb-up:before {
	content: "\e670";
}
.ti-thumb-down:before {
	content: "\e671";
}
.ti-text:before {
	content: "\e672";
}
.ti-stats-up:before {
	content: "\e673";
}
.ti-stats-down:before {
	content: "\e674";
}
.ti-split-v:before {
	content: "\e675";
}
.ti-split-h:before {
	content: "\e676";
}
.ti-smallcap:before {
	content: "\e677";
}
.ti-shine:before {
	content: "\e678";
}
.ti-shift-right:before {
	content: "\e679";
}
.ti-shift-left:before {
	content: "\e67a";
}
.ti-shield:before {
	content: "\e67b";
}
.ti-notepad:before {
	content: "\e67c";
}
.ti-server:before {
	content: "\e67d";
}
.ti-quote-right:before {
	content: "\e67e";
}
.ti-quote-left:before {
	content: "\e67f";
}
.ti-pulse:before {
	content: "\e680";
}
.ti-printer:before {
	content: "\e681";
}
.ti-power-off:before {
	content: "\e682";
}
.ti-plug:before {
	content: "\e683";
}
.ti-pie-chart:before {
	content: "\e684";
}
.ti-paragraph:before {
	content: "\e685";
}
.ti-panel:before {
	content: "\e686";
}
.ti-package:before {
	content: "\e687";
}
.ti-music:before {
	content: "\e688";
}
.ti-music-alt:before {
	content: "\e689";
}
.ti-mouse:before {
	content: "\e68a";
}
.ti-mouse-alt:before {
	content: "\e68b";
}
.ti-money:before {
	content: "\e68c";
}
.ti-microphone:before {
	content: "\e68d";
}
.ti-menu:before {
	content: "\e68e";
}
.ti-menu-alt:before {
	content: "\e68f";
}
.ti-map:before {
	content: "\e690";
}
.ti-map-alt:before {
	content: "\e691";
}
.ti-loop:before {
	content: "\e692";
}
.ti-location-pin:before {
	content: "\e693";
}
.ti-list:before {
	content: "\e694";
}
.ti-light-bulb:before {
	content: "\e695";
}
.ti-Italic:before {
	content: "\e696";
}
.ti-info:before {
	content: "\e697";
}
.ti-infinite:before {
	content: "\e698";
}
.ti-id-badge:before {
	content: "\e699";
}
.ti-hummer:before {
	content: "\e69a";
}
.ti-home:before {
	content: "\e69b";
}
.ti-help:before {
	content: "\e69c";
}
.ti-headphone:before {
	content: "\e69d";
}
.ti-harddrives:before {
	content: "\e69e";
}
.ti-harddrive:before {
	content: "\e69f";
}
.ti-gift:before {
	content: "\e6a0";
}
.ti-game:before {
	content: "\e6a1";
}
.ti-filter:before {
	content: "\e6a2";
}
.ti-files:before {
	content: "\e6a3";
}
.ti-file:before {
	content: "\e6a4";
}
.ti-eraser:before {
	content: "\e6a5";
}
.ti-envelope:before {
	content: "\e6a6";
}
.ti-download:before {
	content: "\e6a7";
}
.ti-direction:before {
	content: "\e6a8";
}
.ti-direction-alt:before {
	content: "\e6a9";
}
.ti-dashboard:before {
	content: "\e6aa";
}
.ti-control-stop:before {
	content: "\e6ab";
}
.ti-control-shuffle:before {
	content: "\e6ac";
}
.ti-control-play:before {
	content: "\e6ad";
}
.ti-control-pause:before {
	content: "\e6ae";
}
.ti-control-forward:before {
	content: "\e6af";
}
.ti-control-backward:before {
	content: "\e6b0";
}
.ti-cloud:before {
	content: "\e6b1";
}
.ti-cloud-up:before {
	content: "\e6b2";
}
.ti-cloud-down:before {
	content: "\e6b3";
}
.ti-clipboard:before {
	content: "\e6b4";
}
.ti-car:before {
	content: "\e6b5";
}
.ti-calendar:before {
	content: "\e6b6";
}
.ti-book:before {
	content: "\e6b7";
}
.ti-bell:before {
	content: "\e6b8";
}
.ti-basketball:before {
	content: "\e6b9";
}
.ti-bar-chart:before {
	content: "\e6ba";
}
.ti-bar-chart-alt:before {
	content: "\e6bb";
}
.ti-back-right:before {
	content: "\e6bc";
}
.ti-back-left:before {
	content: "\e6bd";
}
.ti-arrows-corner:before {
	content: "\e6be";
}
.ti-archive:before {
	content: "\e6bf";
}
.ti-anchor:before {
	content: "\e6c0";
}
.ti-align-right:before {
	content: "\e6c1";
}
.ti-align-left:before {
	content: "\e6c2";
}
.ti-align-justify:before {
	content: "\e6c3";
}
.ti-align-center:before {
	content: "\e6c4";
}
.ti-alert:before {
	content: "\e6c5";
}
.ti-alarm-clock:before {
	content: "\e6c6";
}
.ti-agenda:before {
	content: "\e6c7";
}
.ti-write:before {
	content: "\e6c8";
}
.ti-window:before {
	content: "\e6c9";
}
.ti-widgetized:before {
	content: "\e6ca";
}
.ti-widget:before {
	content: "\e6cb";
}
.ti-widget-alt:before {
	content: "\e6cc";
}
.ti-wallet:before {
	content: "\e6cd";
}
.ti-video-clapper:before {
	content: "\e6ce";
}
.ti-video-camera:before {
	content: "\e6cf";
}
.ti-vector:before {
	content: "\e6d0";
}
.ti-themify-logo:before {
	content: "\e6d1";
}
.ti-themify-favicon:before {
	content: "\e6d2";
}
.ti-themify-favicon-alt:before {
	content: "\e6d3";
}
.ti-support:before {
	content: "\e6d4";
}
.ti-stamp:before {
	content: "\e6d5";
}
.ti-split-v-alt:before {
	content: "\e6d6";
}
.ti-slice:before {
	content: "\e6d7";
}
.ti-shortcode:before {
	content: "\e6d8";
}
.ti-shift-right-alt:before {
	content: "\e6d9";
}
.ti-shift-left-alt:before {
	content: "\e6da";
}
.ti-ruler-alt-2:before {
	content: "\e6db";
}
.ti-receipt:before {
	content: "\e6dc";
}
.ti-pin2:before {
	content: "\e6dd";
}
.ti-pin-alt:before {
	content: "\e6de";
}
.ti-pencil-alt2:before {
	content: "\e6df";
}
.ti-palette:before {
	content: "\e6e0";
}
.ti-more:before {
	content: "\e6e1";
}
.ti-more-alt:before {
	content: "\e6e2";
}
.ti-microphone-alt:before {
	content: "\e6e3";
}
.ti-magnet:before {
	content: "\e6e4";
}
.ti-line-double:before {
	content: "\e6e5";
}
.ti-line-dotted:before {
	content: "\e6e6";
}
.ti-line-dashed:before {
	content: "\e6e7";
}
.ti-layout-width-full:before {
	content: "\e6e8";
}
.ti-layout-width-default:before {
	content: "\e6e9";
}
.ti-layout-width-default-alt:before {
	content: "\e6ea";
}
.ti-layout-tab:before {
	content: "\e6eb";
}
.ti-layout-tab-window:before {
	content: "\e6ec";
}
.ti-layout-tab-v:before {
	content: "\e6ed";
}
.ti-layout-tab-min:before {
	content: "\e6ee";
}
.ti-layout-slider:before {
	content: "\e6ef";
}
.ti-layout-slider-alt:before {
	content: "\e6f0";
}
.ti-layout-sidebar-right:before {
	content: "\e6f1";
}
.ti-layout-sidebar-none:before {
	content: "\e6f2";
}
.ti-layout-sidebar-left:before {
	content: "\e6f3";
}
.ti-layout-placeholder:before {
	content: "\e6f4";
}
.ti-layout-menu:before {
	content: "\e6f5";
}
.ti-layout-menu-v:before {
	content: "\e6f6";
}
.ti-layout-menu-separated:before {
	content: "\e6f7";
}
.ti-layout-menu-full:before {
	content: "\e6f8";
}
.ti-layout-media-right-alt:before {
	content: "\e6f9";
}
.ti-layout-media-right:before {
	content: "\e6fa";
}
.ti-layout-media-overlay:before {
	content: "\e6fb";
}
.ti-layout-media-overlay-alt:before {
	content: "\e6fc";
}
.ti-layout-media-overlay-alt-2:before {
	content: "\e6fd";
}
.ti-layout-media-left-alt:before {
	content: "\e6fe";
}
.ti-layout-media-left:before {
	content: "\e6ff";
}
.ti-layout-media-center-alt:before {
	content: "\e700";
}
.ti-layout-media-center:before {
	content: "\e701";
}
.ti-layout-list-thumb:before {
	content: "\e702";
}
.ti-layout-list-thumb-alt:before {
	content: "\e703";
}
.ti-layout-list-post:before {
	content: "\e704";
}
.ti-layout-list-large-image:before {
	content: "\e705";
}
.ti-layout-line-solid:before {
	content: "\e706";
}
.ti-layout-grid4:before {
	content: "\e707";
}
.ti-layout-grid3:before {
	content: "\e708";
}
.ti-layout-grid2:before {
	content: "\e709";
}
.ti-layout-grid2-thumb:before {
	content: "\e70a";
}
.ti-layout-cta-right:before {
	content: "\e70b";
}
.ti-layout-cta-left:before {
	content: "\e70c";
}
.ti-layout-cta-center:before {
	content: "\e70d";
}
.ti-layout-cta-btn-right:before {
	content: "\e70e";
}
.ti-layout-cta-btn-left:before {
	content: "\e70f";
}
.ti-layout-column4:before {
	content: "\e710";
}
.ti-layout-column3:before {
	content: "\e711";
}
.ti-layout-column2:before {
	content: "\e712";
}
.ti-layout-accordion-separated:before {
	content: "\e713";
}
.ti-layout-accordion-merged:before {
	content: "\e714";
}
.ti-layout-accordion-list:before {
	content: "\e715";
}
.ti-ink-pen:before {
	content: "\e716";
}
.ti-info-alt:before {
	content: "\e717";
}
.ti-help-alt:before {
	content: "\e718";
}
.ti-headphone-alt:before {
	content: "\e719";
}
.ti-hand-point-up:before {
	content: "\e71a";
}
.ti-hand-point-right:before {
	content: "\e71b";
}
.ti-hand-point-left:before {
	content: "\e71c";
}
.ti-hand-point-down:before {
	content: "\e71d";
}
.ti-gallery:before {
	content: "\e71e";
}
.ti-face-smile:before {
	content: "\e71f";
}
.ti-face-sad:before {
	content: "\e720";
}
.ti-credit-card:before {
	content: "\e721";
}
.ti-control-skip-forward:before {
	content: "\e722";
}
.ti-control-skip-backward:before {
	content: "\e723";
}
.ti-control-record:before {
	content: "\e724";
}
.ti-control-eject:before {
	content: "\e725";
}
.ti-comments-smiley:before {
	content: "\e726";
}
.ti-brush-alt:before {
	content: "\e727";
}
.ti-youtube:before {
	content: "\e728";
}
.ti-vimeo:before {
	content: "\e729";
}
.ti-twitter:before {
	content: "\e72a";
}
.ti-time:before {
	content: "\e72b";
}
.ti-tumblr:before {
	content: "\e72c";
}
.ti-skype:before {
	content: "\e72d";
}
.ti-share:before {
	content: "\e72e";
}
.ti-share-alt:before {
	content: "\e72f";
}
.ti-rocket:before {
	content: "\e730";
}
.ti-pinterest:before {
	content: "\e731";
}
.ti-new-window:before {
	content: "\e732";
}
.ti-microsoft:before {
	content: "\e733";
}
.ti-list-ol:before {
	content: "\e734";
}
.ti-linkedin:before {
	content: "\e735";
}
.ti-layout-sidebar-2:before {
	content: "\e736";
}
.ti-layout-grid4-alt:before {
	content: "\e737";
}
.ti-layout-grid3-alt:before {
	content: "\e738";
}
.ti-layout-grid2-alt:before {
	content: "\e739";
}
.ti-layout-column4-alt:before {
	content: "\e73a";
}
.ti-layout-column3-alt:before {
	content: "\e73b";
}
.ti-layout-column2-alt:before {
	content: "\e73c";
}
.ti-instagram:before {
	content: "\e73d";
}
.ti-google:before {
	content: "\e73e";
}
.ti-github:before {
	content: "\e73f";
}
.ti-flickr:before {
	content: "\e740";
}
.ti-facebook:before {
	content: "\e741";
}
.ti-dropbox:before {
	content: "\e742";
}
.ti-dribbble:before {
	content: "\e743";
}
.ti-apple:before {
	content: "\e744";
}
.ti-android:before {
	content: "\e745";
}
.ti-save:before {
	content: "\e746";
}
.ti-save-alt:before {
	content: "\e747";
}
.ti-yahoo:before {
	content: "\e748";
}
.ti-wordpress:before {
	content: "\e749";
}
.ti-vimeo-alt:before {
	content: "\e74a";
}
.ti-twitter-alt:before {
	content: "\e74b";
}
.ti-tumblr-alt:before {
	content: "\e74c";
}
.ti-trello:before {
	content: "\e74d";
}
.ti-stack-overflow:before {
	content: "\e74e";
}
.ti-soundcloud:before {
	content: "\e74f";
}
.ti-sharethis:before {
	content: "\e750";
}
.ti-sharethis-alt:before {
	content: "\e751";
}
.ti-reddit:before {
	content: "\e752";
}
.ti-pinterest-alt:before {
	content: "\e753";
}
.ti-microsoft-alt:before {
	content: "\e754";
}
.ti-linux:before {
	content: "\e755";
}
.ti-jsfiddle:before {
	content: "\e756";
}
.ti-joomla:before {
	content: "\e757";
}
.ti-html5:before {
	content: "\e758";
}
.ti-flickr-alt:before {
	content: "\e759";
}
.ti-email:before {
	content: "\e75a";
}
.ti-drupal:before {
	content: "\e75b";
}
.ti-dropbox-alt:before {
	content: "\e75c";
}
.ti-css3:before {
	content: "\e75d";
}
.ti-rss:before {
	content: "\e75e";
}
.ti-rss-alt:before {
	content: "\e75f";
}


File: /assets\js\bootstrap-checkbox-radio.js
!function ($) {

 /* CHECKBOX PUBLIC CLASS DEFINITION
  * ============================== */

  var Checkbox = function (element, options) {
    this.init(element, options);
  }

  Checkbox.prototype = {

    constructor: Checkbox

  , init: function (element, options) {
    var $el = this.$element = $(element)

    this.options = $.extend({}, $.fn.checkbox.defaults, options);
    $el.before(this.options.template);
    this.setState();
  }

  , setState: function () {
      var $el = this.$element
        , $parent = $el.closest('.checkbox');

        $el.prop('disabled') && $parent.addClass('disabled');
        $el.prop('checked') && $parent.addClass('checked');
    }

  , toggle: function () {
      var ch = 'checked'
        , $el = this.$element
        , $parent = $el.closest('.checkbox')
        , checked = $el.prop(ch)
        , e = $.Event('toggle')

      if ($el.prop('disabled') == false) {
        $parent.toggleClass(ch) && checked ? $el.removeAttr(ch) : $el.prop(ch, ch);
        $el.trigger(e).trigger('change');
      }
    }

  , setCheck: function (option) {
      var d = 'disabled'
        , ch = 'checked'
        , $el = this.$element
        , $parent = $el.closest('.checkbox')
        , checkAction = option == 'check' ? true : false
        , e = $.Event(option)

      $parent[checkAction ? 'addClass' : 'removeClass' ](ch) && checkAction ? $el.prop(ch, ch) : $el.removeAttr(ch);
      $el.trigger(e).trigger('change');
    }

  }


 /* CHECKBOX PLUGIN DEFINITION
  * ======================== */

  var old = $.fn.checkbox

  $.fn.checkbox = function (option) {
    return this.each(function () {
      var $this = $(this)
        , data = $this.data('checkbox')
        , options = $.extend({}, $.fn.checkbox.defaults, $this.data(), typeof option == 'object' && option);
      if (!data) $this.data('checkbox', (data = new Checkbox(this, options)));
      if (option == 'toggle') data.toggle()
      if (option == 'check' || option == 'uncheck') data.setCheck(option)
      else if (option) data.setState();
    });
  }

  $.fn.checkbox.defaults = {
    template: '<span class="icons"><span class="first-icon fa fa-square fa-base"></span><span class="second-icon fa fa-check-square fa-base"></span></span>'
  }


 /* CHECKBOX NO CONFLICT
  * ================== */

  $.fn.checkbox.noConflict = function () {
    $.fn.checkbox = old;
    return this;
  }


 /* CHECKBOX DATA-API
  * =============== */

  $(document).on('click.checkbox.data-api', '[data-toggle^=checkbox], .checkbox', function (e) {
    var $checkbox = $(e.target);
    if (e.target.tagName != "A") {
      e && e.preventDefault() && e.stopPropagation();
      if (!$checkbox.hasClass('checkbox')) $checkbox = $checkbox.closest('.checkbox');
      $checkbox.find(':checkbox').checkbox('toggle');
    }
  });

  $(function () {
    $('input[type="checkbox"]').each(function () {
      var $checkbox = $(this);
      $checkbox.checkbox();
    });
  });

}(window.jQuery);

/* =============================================================
 * flatui-radio v0.0.3
 * ============================================================ */

!function ($) {

 /* RADIO PUBLIC CLASS DEFINITION
  * ============================== */

  var Radio = function (element, options) {
    this.init(element, options);
  }

  Radio.prototype = {

    constructor: Radio

  , init: function (element, options) {
      var $el = this.$element = $(element)

      this.options = $.extend({}, $.fn.radio.defaults, options);
      $el.before(this.options.template);
      this.setState();
    }

  , setState: function () {
      var $el = this.$element
        , $parent = $el.closest('.radio');

        $el.prop('disabled') && $parent.addClass('disabled');
        $el.prop('checked') && $parent.addClass('checked');
    }

  , toggle: function () {
      var d = 'disabled'
        , ch = 'checked'
        , $el = this.$element
        , checked = $el.prop(ch)
        , $parent = $el.closest('.radio')
        , $parentWrap = $el.closest('form').length ? $el.closest('form') : $el.closest('body')
        , $elemGroup = $parentWrap.find(':radio[name="' + $el.attr('name') + '"]')
        , e = $.Event('toggle')

        if ($el.prop(d) == false) {
            $elemGroup.not($el).each(function () {
              var $el = $(this)
                , $parent = $(this).closest('.radio');

                if ($el.prop(d) == false) {
                  $parent.removeClass(ch) && $el.removeAttr(ch).trigger('change');
                }
            });

            if (checked == false) $parent.addClass(ch) && $el.prop(ch, true);
            $el.trigger(e);

            if (checked !== $el.prop(ch)) {
                $el.trigger('change');
            }
        }
    }

  , setCheck: function (option) {
      var ch = 'checked'
        , $el = this.$element
        , $parent = $el.closest('.radio')
        , checkAction = option == 'check' ? true : false
        , checked = $el.prop(ch)
        , $parentWrap = $el.closest('form').length ? $el.closest('form') : $el.closest('body')
        , $elemGroup = $parentWrap.find(':radio[name="' + $el['attr']('name') + '"]')
        , e = $.Event(option)

      $elemGroup.not($el).each(function () {
        var $el = $(this)
          , $parent = $(this).closest('.radio');

          $parent.removeClass(ch) && $el.removeAttr(ch);
      });

      $parent[checkAction ? 'addClass' : 'removeClass'](ch) && checkAction ? $el.prop(ch, ch) : $el.removeAttr(ch);
      $el.trigger(e);

      if (checked !== $el.prop(ch)) {
        $el.trigger('change');
      }
    }

  }


 /* RADIO PLUGIN DEFINITION
  * ======================== */

  var old = $.fn.radio

  $.fn.radio = function (option) {
    return this.each(function () {
      var $this = $(this)
        , data = $this.data('radio')
        , options = $.extend({}, $.fn.radio.defaults, $this.data(), typeof option == 'object' && option);
      if (!data) $this.data('radio', (data = new Radio(this, options)));
      if (option == 'toggle') data.toggle()
      if (option == 'check' || option == 'uncheck') data.setCheck(option)
      else if (option) data.setState();
    });
  }

  $.fn.radio.defaults = {
    template: '<span class="icons"><span class="first-icon fa fa-circle-o fa-base"></span><span class="second-icon fa fa-dot-circle-o fa-base"></span></span>'
  }


 /* RADIO NO CONFLICT
  * ================== */

  $.fn.radio.noConflict = function () {
    $.fn.radio = old;
    return this;
  }


 /* RADIO DATA-API
  * =============== */

  $(document).on('click.radio.data-api', '[data-toggle^=radio], .radio', function (e) {
    var $radio = $(e.target);
    e && e.preventDefault() && e.stopPropagation();
    if (!$radio.hasClass('radio')) $radio = $radio.closest('.radio');
    $radio.find(':radio').radio('toggle');
  });

  $(function () {
    $('input[type="radio"]').each(function () {
      var $radio = $(this);
      $radio.radio();
    });
  });

}(window.jQuery);


File: /assets\js\bootstrap-notify.js
/*
    
    

     Creative Tim Modifications
     
     Lines: 239, 240 was changed from top: 5px to top: 50% and we added margin-top: -13px. In this way the close button will be aligned vertically 
     Line:242 - modified when the icon is set, we add the class "alert-with-icon", so there will be enough space for the icon.




*/


/*
* Project: Bootstrap Notify = v3.1.5
* Description: Turns standard Bootstrap alerts into "Growl-like" notifications.
* Author: Mouse0270 aka Robert McIntosh
* License: MIT License
* Website: https://github.com/mouse0270/bootstrap-growl
*/

/* global define:false, require: false, jQuery:false */

(function (factory) {
	if (typeof define === 'function' && define.amd) {
		// AMD. Register as an anonymous module.
		define(['jquery'], factory);
	} else if (typeof exports === 'object') {
		// Node/CommonJS
		factory(require('jquery'));
	} else {
		// Browser globals
		factory(jQuery);
	}
}(function ($) {
	// Create the defaults once
	var defaults = {
		element: 'body',
		position: null,
		type: "info",
		allow_dismiss: true,
		allow_duplicates: true,
		newest_on_top: false,
		showProgressbar: false,
		placement: {
			from: "top",
			align: "right"
		},
		offset: 20,
		spacing: 10,
		z_index: 1031,
		delay: 5000,
		timer: 1000,
		url_target: '_blank',
		mouse_over: null,
		animate: {
			enter: 'animated fadeInDown',
			exit: 'animated fadeOutUp'
		},
		onShow: null,
		onShown: null,
		onClose: null,
		onClosed: null,
		icon_type: 'class',
		template: '<div data-notify="container" class="col-xs-11 col-sm-4 alert alert-{0}" role="alert"><button type="button" aria-hidden="true" class="close" data-notify="dismiss">&times;</button><span data-notify="icon"></span> <span data-notify="title">{1}</span> <span data-notify="message">{2}</span><div class="progress" data-notify="progressbar"><div class="progress-bar progress-bar-{0}" role="progressbar" aria-valuenow="0" aria-valuemin="0" aria-valuemax="100" style="width: 0%;"></div></div><a href="{3}" target="{4}" data-notify="url"></a></div>'
	};

	String.format = function () {
		var str = arguments[0];
		for (var i = 1; i < arguments.length; i++) {
			str = str.replace(RegExp("\\{" + (i - 1) + "\\}", "gm"), arguments[i]);
		}
		return str;
	};

	function isDuplicateNotification(notification) {
		var isDupe = false;

		$('[data-notify="container"]').each(function (i, el) {
			var $el = $(el);
			var title = $el.find('[data-notify="title"]').text().trim();
			var message = $el.find('[data-notify="message"]').html().trim();

			// The input string might be different than the actual parsed HTML string!
			// (<br> vs <br /> for example)
			// So we have to force-parse this as HTML here!
			var isSameTitle = title === $("<div>" + notification.settings.content.title + "</div>").html().trim();
			var isSameMsg = message === $("<div>" + notification.settings.content.message + "</div>").html().trim();
			var isSameType = $el.hasClass('alert-' + notification.settings.type);

			if (isSameTitle && isSameMsg && isSameType) {
				//we found the dupe. Set the var and stop checking.
				isDupe = true;
			}
			return !isDupe;
		});

		return isDupe;
	}

	function Notify(element, content, options) {
		// Setup Content of Notify
		var contentObj = {
			content: {
				message: typeof content === 'object' ? content.message : content,
				title: content.title ? content.title : '',
				icon: content.icon ? content.icon : '',
				url: content.url ? content.url : '#',
				target: content.target ? content.target : '-'
			}
		};

		options = $.extend(true, {}, contentObj, options);
		this.settings = $.extend(true, {}, defaults, options);
		this._defaults = defaults;
		if (this.settings.content.target === "-") {
			this.settings.content.target = this.settings.url_target;
		}
		this.animations = {
			start: 'webkitAnimationStart oanimationstart MSAnimationStart animationstart',
			end: 'webkitAnimationEnd oanimationend MSAnimationEnd animationend'
		};

		if (typeof this.settings.offset === 'number') {
			this.settings.offset = {
				x: this.settings.offset,
				y: this.settings.offset
			};
		}

		//if duplicate messages are not allowed, then only continue if this new message is not a duplicate of one that it already showing
		if (this.settings.allow_duplicates || (!this.settings.allow_duplicates && !isDuplicateNotification(this))) {
			this.init();
		}
	}
	
	$.extend(Notify.prototype, {
		init: function () {
			var self = this;

			this.buildNotify();
			if (this.settings.content.icon) {
				this.setIcon();
			}
			if (this.settings.content.url != "#") {
				this.styleURL();
			}
			this.styleDismiss();
			this.placement();
			this.bind();

			this.notify = {
				$ele: this.$ele,
				update: function (command, update) {
					var commands = {};
					if (typeof command === "string") {
						commands[command] = update;
					} else {
						commands = command;
					}
					for (var cmd in commands) {
						switch (cmd) {
							case "type":
								this.$ele.removeClass('alert-' + self.settings.type);
								this.$ele.find('[data-notify="progressbar"] > .progress-bar').removeClass('progress-bar-' + self.settings.type);
								self.settings.type = commands[cmd];
								this.$ele.addClass('alert-' + commands[cmd]).find('[data-notify="progressbar"] > .progress-bar').addClass('progress-bar-' + commands[cmd]);
								break;
							case "icon":
								var $icon = this.$ele.find('[data-notify="icon"]');
								if (self.settings.icon_type.toLowerCase() === 'class') {
									$icon.removeClass(self.settings.content.icon).addClass(commands[cmd]);
								} else {
									if (!$icon.is('img')) {
										$icon.find('img');
									}
									$icon.attr('src', commands[cmd]);
								}
								break;
							case "progress":
								var newDelay = self.settings.delay - (self.settings.delay * (commands[cmd] / 100));
								this.$ele.data('notify-delay', newDelay);
								this.$ele.find('[data-notify="progressbar"] > div').attr('aria-valuenow', commands[cmd]).css('width', commands[cmd] + '%');
								break;
							case "url":
								this.$ele.find('[data-notify="url"]').attr('href', commands[cmd]);
								break;
							case "target":
								this.$ele.find('[data-notify="url"]').attr('target', commands[cmd]);
								break;
							default:
								this.$ele.find('[data-notify="' + cmd + '"]').html(commands[cmd]);
						}
					}
					var posX = this.$ele.outerHeight() + parseInt(self.settings.spacing) + parseInt(self.settings.offset.y);
					self.reposition(posX);
				},
				close: function () {
					self.close();
				}
			};

		},
		buildNotify: function () {
			var content = this.settings.content;
			this.$ele = $(String.format(this.settings.template, this.settings.type, content.title, content.message, content.url, content.target));
			this.$ele.attr('data-notify-position', this.settings.placement.from + '-' + this.settings.placement.align);
			if (!this.settings.allow_dismiss) {
				this.$ele.find('[data-notify="dismiss"]').css('display', 'none');
			}
			if ((this.settings.delay <= 0 && !this.settings.showProgressbar) || !this.settings.showProgressbar) {
				this.$ele.find('[data-notify="progressbar"]').remove();
			}
		},
		setIcon: function () {
    		
    		this.$ele.addClass('alert-with-icon');
    		
			if (this.settings.icon_type.toLowerCase() === 'class') {
				this.$ele.find('[data-notify="icon"]').addClass(this.settings.content.icon);
			} else {
				if (this.$ele.find('[data-notify="icon"]').is('img')) {
					this.$ele.find('[data-notify="icon"]').attr('src', this.settings.content.icon);
				} else {
					this.$ele.find('[data-notify="icon"]').append('<img src="' + this.settings.content.icon + '" alt="Notify Icon" />');
				}
			}
		},
		styleDismiss: function () {
			this.$ele.find('[data-notify="dismiss"]').css({
				position: 'absolute',
				right: '10px',
				top: '50%',
				marginTop: '-13px',
				zIndex: this.settings.z_index + 2
			});
		},
		styleURL: function () {
			this.$ele.find('[data-notify="url"]').css({
				backgroundImage: 'url(data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)',
				height: '100%',
				left: 0,
				position: 'absolute',
				top: 0,
				width: '100%',
				zIndex: this.settings.z_index + 1
			});
		},
		placement: function () {
			var self = this,
				offsetAmt = this.settings.offset.y,
				css = {
					display: 'inline-block',
					margin: '0px auto',
					position: this.settings.position ? this.settings.position : (this.settings.element === 'body' ? 'fixed' : 'absolute'),
					transition: 'all .5s ease-in-out',
					zIndex: this.settings.z_index
				},
				hasAnimation = false,
				settings = this.settings;

			$('[data-notify-position="' + this.settings.placement.from + '-' + this.settings.placement.align + '"]:not([data-closing="true"])').each(function () {
				offsetAmt = Math.max(offsetAmt, parseInt($(this).css(settings.placement.from)) + parseInt($(this).outerHeight()) + parseInt(settings.spacing));
			});
			if (this.settings.newest_on_top === true) {
				offsetAmt = this.settings.offset.y;
			}
			css[this.settings.placement.from] = offsetAmt + 'px';

			switch (this.settings.placement.align) {
				case "left":
				case "right":
					css[this.settings.placement.align] = this.settings.offset.x + 'px';
					break;
				case "center":
					css.left = 0;
					css.right = 0;
					break;
			}
			this.$ele.css(css).addClass(this.settings.animate.enter);
			$.each(Array('webkit-', 'moz-', 'o-', 'ms-', ''), function (index, prefix) {
				self.$ele[0].style[prefix + 'AnimationIterationCount'] = 1;
			});

			$(this.settings.element).append(this.$ele);

			if (this.settings.newest_on_top === true) {
				offsetAmt = (parseInt(offsetAmt) + parseInt(this.settings.spacing)) + this.$ele.outerHeight();
				this.reposition(offsetAmt);
			}

			if ($.isFunction(self.settings.onShow)) {
				self.settings.onShow.call(this.$ele);
			}

			this.$ele.one(this.animations.start, function () {
				hasAnimation = true;
			}).one(this.animations.end, function () {
				if ($.isFunction(self.settings.onShown)) {
					self.settings.onShown.call(this);
				}
			});

			setTimeout(function () {
				if (!hasAnimation) {
					if ($.isFunction(self.settings.onShown)) {
						self.settings.onShown.call(this);
					}
				}
			}, 600);
		},
		bind: function () {
			var self = this;

			this.$ele.find('[data-notify="dismiss"]').on('click', function () {
				self.close();
			});

			this.$ele.mouseover(function () {
				$(this).data('data-hover', "true");
			}).mouseout(function () {
				$(this).data('data-hover', "false");
			});
			this.$ele.data('data-hover', "false");

			if (this.settings.delay > 0) {
				self.$ele.data('notify-delay', self.settings.delay);
				var timer = setInterval(function () {
					var delay = parseInt(self.$ele.data('notify-delay')) - self.settings.timer;
					if ((self.$ele.data('data-hover') === 'false' && self.settings.mouse_over === "pause") || self.settings.mouse_over != "pause") {
						var percent = ((self.settings.delay - delay) / self.settings.delay) * 100;
						self.$ele.data('notify-delay', delay);
						self.$ele.find('[data-notify="progressbar"] > div').attr('aria-valuenow', percent).css('width', percent + '%');
					}
					if (delay <= -(self.settings.timer)) {
						clearInterval(timer);
						self.close();
					}
				}, self.settings.timer);
			}
		},
		close: function () {
			var self = this,
				posX = parseInt(this.$ele.css(this.settings.placement.from)),
				hasAnimation = false;

			this.$ele.data('closing', 'true').addClass(this.settings.animate.exit);
			self.reposition(posX);

			if ($.isFunction(self.settings.onClose)) {
				self.settings.onClose.call(this.$ele);
			}

			this.$ele.one(this.animations.start, function () {
				hasAnimation = true;
			}).one(this.animations.end, function () {
				$(this).remove();
				if ($.isFunction(self.settings.onClosed)) {
					self.settings.onClosed.call(this);
				}
			});

			setTimeout(function () {
				if (!hasAnimation) {
					self.$ele.remove();
					if (self.settings.onClosed) {
						self.settings.onClosed(self.$ele);
					}
				}
			}, 600);
		},
		reposition: function (posX) {
			var self = this,
				notifies = '[data-notify-position="' + this.settings.placement.from + '-' + this.settings.placement.align + '"]:not([data-closing="true"])',
				$elements = this.$ele.nextAll(notifies);
			if (this.settings.newest_on_top === true) {
				$elements = this.$ele.prevAll(notifies);
			}
			$elements.each(function () {
				$(this).css(self.settings.placement.from, posX);
				posX = (parseInt(posX) + parseInt(self.settings.spacing)) + $(this).outerHeight();
			});
		}
	});

	$.notify = function (content, options) {
		var plugin = new Notify(this, content, options);
		return plugin.notify;
	};
	$.notifyDefaults = function (options) {
		defaults = $.extend(true, {}, defaults, options);
		return defaults;
	};
	$.notifyClose = function (command) {
		if (typeof command === "undefined" || command === "all") {
			$('[data-notify]').find('[data-notify="dismiss"]').trigger('click');
		} else {
			$('[data-notify-position="' + command + '"]').find('[data-notify="dismiss"]').trigger('click');
		}
	};

}));


File: /assets\js\demo.js
type = ['','info','success','warning','danger'];


demo = {
    initPickColor: function(){
        $('.pick-class-label').click(function(){
            var new_class = $(this).attr('new-class');
            var old_class = $('#display-buttons').attr('data-class');
            var display_div = $('#display-buttons');
            if(display_div.length) {
            var display_buttons = display_div.find('.btn');
            display_buttons.removeClass(old_class);
            display_buttons.addClass(new_class);
            display_div.attr('data-class', new_class);
            }
        });
    },

    initChartist: function(){

        var dataSales = {
          labels: ['9:00AM', '12:00AM', '3:00PM', '6:00PM', '9:00PM', '12:00PM', '3:00AM', '6:00AM'],
          series: [
             [287, 385, 490, 562, 594, 626, 698, 895, 952],
            [67, 152, 193, 240, 387, 435, 535, 642, 744],
            [23, 113, 67, 108, 190, 239, 307, 410, 410]
          ]
        };

        var optionsSales = {
          lineSmooth: false,
          low: 0,
          high: 1000,
          showArea: true,
          height: "245px",
          axisX: {
            showGrid: false,
          },
          lineSmooth: Chartist.Interpolation.simple({
            divisor: 3
          }),
          showLine: true,
          showPoint: false,
        };

        var responsiveSales = [
          ['screen and (max-width: 640px)', {
            axisX: {
              labelInterpolationFnc: function (value) {
                return value[0];
              }
            }
          }]
        ];

        Chartist.Line('#chartHours', dataSales, optionsSales, responsiveSales);


        var data = {
          labels: ['Jan', 'Feb', 'Mar', 'Apr', 'Mai', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
          series: [
            [542, 543, 520, 680, 653, 753, 326, 434, 568, 610, 756, 895],
            [230, 293, 380, 480, 503, 553, 600, 664, 698, 710, 736, 795]
          ]
        };

        var options = {
            seriesBarDistance: 10,
            axisX: {
                showGrid: false
            },
            height: "245px"
        };

        var responsiveOptions = [
          ['screen and (max-width: 640px)', {
            seriesBarDistance: 5,
            axisX: {
              labelInterpolationFnc: function (value) {
                return value[0];
              }
            }
          }]
        ];

        Chartist.Line('#chartActivity', data, options, responsiveOptions);

        var dataPreferences = {
            series: [
                [25, 30, 20, 25]
            ]
        };

        var optionsPreferences = {
            donut: true,
            donutWidth: 40,
            startAngle: 0,
            total: 100,
            showLabel: false,
            axisX: {
                showGrid: false
            }
        };

        Chartist.Pie('#chartPreferences', dataPreferences, optionsPreferences);

        Chartist.Pie('#chartPreferences', {
          labels: ['62%','32%','6%'],
          series: [62, 32, 6]
        });
    },

    initGoogleMaps: function(){
        var myLatlng = new google.maps.LatLng(40.748817, -73.985428);
        var mapOptions = {
          zoom: 13,
          center: myLatlng,
          scrollwheel: false, //we disable de scroll over the map, it is a really annoing when you scroll through page
          styles: [{"featureType":"water","stylers":[{"saturation":43},{"lightness":-11},{"hue":"#0088ff"}]},{"featureType":"road","elementType":"geometry.fill","stylers":[{"hue":"#ff0000"},{"saturation":-100},{"lightness":99}]},{"featureType":"road","elementType":"geometry.stroke","stylers":[{"color":"#808080"},{"lightness":54}]},{"featureType":"landscape.man_made","elementType":"geometry.fill","stylers":[{"color":"#ece2d9"}]},{"featureType":"poi.park","elementType":"geometry.fill","stylers":[{"color":"#ccdca1"}]},{"featureType":"road","elementType":"labels.text.fill","stylers":[{"color":"#767676"}]},{"featureType":"road","elementType":"labels.text.stroke","stylers":[{"color":"#ffffff"}]},{"featureType":"poi","stylers":[{"visibility":"off"}]},{"featureType":"landscape.natural","elementType":"geometry.fill","stylers":[{"visibility":"on"},{"color":"#b8cb93"}]},{"featureType":"poi.park","stylers":[{"visibility":"on"}]},{"featureType":"poi.sports_complex","stylers":[{"visibility":"on"}]},{"featureType":"poi.medical","stylers":[{"visibility":"on"}]},{"featureType":"poi.business","stylers":[{"visibility":"simplified"}]}]

        }
        var map = new google.maps.Map(document.getElementById("map"), mapOptions);

        var marker = new google.maps.Marker({
            position: myLatlng,
            title:"Hello World!"
        });

        // To add the marker to the map, call setMap();
        marker.setMap(map);
    },

	showNotification: function(from, align){
    	color = Math.floor((Math.random() * 4) + 1);

    	$.notify({
        	icon: "ti-gift",
        	message: "Welcome to <b>Paper Dashboard</b> - a beautiful freebie for every web developer."

        },{
            type: type[color],
            timer: 4000,
            placement: {
                from: from,
                align: align
            }
        });
	},
    initDocumentationCharts: function(){
    //     	init single simple line chart
        var dataPerformance = {
          labels: ['6pm','9pm','11pm', '2am', '4am', '8am', '2pm', '5pm', '8pm', '11pm', '4am'],
          series: [
            [1, 6, 8, 7, 4, 7, 8, 12, 16, 17, 14, 13]
          ]
        };

        var optionsPerformance = {
          showPoint: false,
          lineSmooth: true,
          height: "200px",
          axisX: {
            showGrid: false,
            showLabel: true
          },
          axisY: {
            offset: 40,
          },
          low: 0,
          high: 16,
          height: "250px"
        };

        Chartist.Line('#chartPerformance', dataPerformance, optionsPerformance);

    //     init single line with points chart
        var dataStock = {
          labels: ['\'07','\'08','\'09', '\'10', '\'11', '\'12', '\'13', '\'14', '\'15'],
          series: [
            [22.20, 34.90, 42.28, 51.93, 62.21, 80.23, 62.21, 82.12, 102.50, 107.23]
          ]
        };

        var optionsStock = {
          lineSmooth: false,
          height: "200px",
          axisY: {
            offset: 40,
            labelInterpolationFnc: function(value) {
                return '$' + value;
              }

          },
          low: 10,
          height: "250px",
          high: 110,
            classNames: {
              point: 'ct-point ct-green',
              line: 'ct-line ct-green'
          }
        };

        Chartist.Line('#chartStock', dataStock, optionsStock);

    //      init multiple lines chart
        var dataSales = {
          labels: ['9:00AM', '12:00AM', '3:00PM', '6:00PM', '9:00PM', '12:00PM', '3:00AM', '6:00AM'],
          series: [
             [287, 385, 490, 562, 594, 626, 698, 895, 952],
            [67, 152, 193, 240, 387, 435, 535, 642, 744],
            [23, 113, 67, 108, 190, 239, 307, 410, 410]
          ]
        };

        var optionsSales = {
          lineSmooth: false,
          low: 0,
          high: 1000,
          showArea: true,
          height: "245px",
          axisX: {
            showGrid: false,
          },
          lineSmooth: Chartist.Interpolation.simple({
            divisor: 3
          }),
          showLine: true,
          showPoint: false,
        };

        var responsiveSales = [
          ['screen and (max-width: 640px)', {
            axisX: {
              labelInterpolationFnc: function (value) {
                return value[0];
              }
            }
          }]
        ];

        Chartist.Line('#chartHours', dataSales, optionsSales, responsiveSales);

    //      pie chart
        Chartist.Pie('#chartPreferences', {
          labels: ['62%','32%','6%'],
          series: [62, 32, 6]
        });

    //      bar chart
        var dataViews = {
          labels: ['Jan', 'Feb', 'Mar', 'Apr', 'Mai', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
          series: [
            [542, 443, 320, 780, 553, 453, 326, 434, 568, 610, 756, 895]
          ]
        };

        var optionsViews = {
          seriesBarDistance: 10,
          classNames: {
            bar: 'ct-bar'
          },
          axisX: {
            showGrid: false,

          },
          height: "250px"

        };

        var responsiveOptionsViews = [
          ['screen and (max-width: 640px)', {
            seriesBarDistance: 5,
            axisX: {
              labelInterpolationFnc: function (value) {
                return value[0];
              }
            }
          }]
        ];

        Chartist.Bar('#chartViews', dataViews, optionsViews, responsiveOptionsViews);

    //     multiple bars chart
        var data = {
          labels: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
          series: [
            [542, 543, 520, 680, 653, 753, 326, 434, 568, 610, 756, 895],
            [230, 293, 380, 480, 503, 553, 600, 664, 698, 710, 736, 795]
          ]
        };

        var options = {
            seriesBarDistance: 10,
            axisX: {
                showGrid: false
            },
            height: "245px"
        };

        var responsiveOptions = [
          ['screen and (max-width: 640px)', {
            seriesBarDistance: 5,
            axisX: {
              labelInterpolationFnc: function (value) {
                return value[0];
              }
            }
          }]
        ];

        Chartist.Line('#chartActivity', data, options, responsiveOptions);

    }

}


File: /assets\js\jquery-1.10.2.js
/*!
 * jQuery JavaScript Library v1.10.2
 * http://jquery.com/
 *
 * Includes Sizzle.js
 * http://sizzlejs.com/
 *
 * Copyright 2005, 2013 jQuery Foundation, Inc. and other contributors
 * Released under the MIT license
 * http://jquery.org/license
 *
 * Date: 2013-07-03T13:48Z
 */
(function( window, undefined ) {

// Can't do this because several apps including ASP.NET trace
// the stack via arguments.caller.callee and Firefox dies if
// you try to trace through "use strict" call chains. (#13335)
// Support: Firefox 18+
//"use strict";
var
	// The deferred used on DOM ready
	readyList,

	// A central reference to the root jQuery(document)
	rootjQuery,

	// Support: IE<10
	// For `typeof xmlNode.method` instead of `xmlNode.method !== undefined`
	core_strundefined = typeof undefined,

	// Use the correct document accordingly with window argument (sandbox)
	location = window.location,
	document = window.document,
	docElem = document.documentElement,

	// Map over jQuery in case of overwrite
	_jQuery = window.jQuery,

	// Map over the $ in case of overwrite
	_$ = window.$,

	// [[Class]] -> type pairs
	class2type = {},

	// List of deleted data cache ids, so we can reuse them
	core_deletedIds = [],

	core_version = "1.10.2",

	// Save a reference to some core methods
	core_concat = core_deletedIds.concat,
	core_push = core_deletedIds.push,
	core_slice = core_deletedIds.slice,
	core_indexOf = core_deletedIds.indexOf,
	core_toString = class2type.toString,
	core_hasOwn = class2type.hasOwnProperty,
	core_trim = core_version.trim,

	// Define a local copy of jQuery
	jQuery = function( selector, context ) {
		// The jQuery object is actually just the init constructor 'enhanced'
		return new jQuery.fn.init( selector, context, rootjQuery );
	},

	// Used for matching numbers
	core_pnum = /[+-]?(?:\d*\.|)\d+(?:[eE][+-]?\d+|)/.source,

	// Used for splitting on whitespace
	core_rnotwhite = /\S+/g,

	// Make sure we trim BOM and NBSP (here's looking at you, Safari 5.0 and IE)
	rtrim = /^[\s\uFEFF\xA0]+|[\s\uFEFF\xA0]+$/g,

	// A simple way to check for HTML strings
	// Prioritize #id over <tag> to avoid XSS via location.hash (#9521)
	// Strict HTML recognition (#11290: must start with <)
	rquickExpr = /^(?:\s*(<[\w\W]+>)[^>]*|#([\w-]*))$/,

	// Match a standalone tag
	rsingleTag = /^<(\w+)\s*\/?>(?:<\/\1>|)$/,

	// JSON RegExp
	rvalidchars = /^[\],:{}\s]*$/,
	rvalidbraces = /(?:^|:|,)(?:\s*\[)+/g,
	rvalidescape = /\\(?:["\\\/bfnrt]|u[\da-fA-F]{4})/g,
	rvalidtokens = /"[^"\\\r\n]*"|true|false|null|-?(?:\d+\.|)\d+(?:[eE][+-]?\d+|)/g,

	// Matches dashed string for camelizing
	rmsPrefix = /^-ms-/,
	rdashAlpha = /-([\da-z])/gi,

	// Used by jQuery.camelCase as callback to replace()
	fcamelCase = function( all, letter ) {
		return letter.toUpperCase();
	},

	// The ready event handler
	completed = function( event ) {

		// readyState === "complete" is good enough for us to call the dom ready in oldIE
		if ( document.addEventListener || event.type === "load" || document.readyState === "complete" ) {
			detach();
			jQuery.ready();
		}
	},
	// Clean-up method for dom ready events
	detach = function() {
		if ( document.addEventListener ) {
			document.removeEventListener( "DOMContentLoaded", completed, false );
			window.removeEventListener( "load", completed, false );

		} else {
			document.detachEvent( "onreadystatechange", completed );
			window.detachEvent( "onload", completed );
		}
	};

jQuery.fn = jQuery.prototype = {
	// The current version of jQuery being used
	jquery: core_version,

	constructor: jQuery,
	init: function( selector, context, rootjQuery ) {
		var match, elem;

		// HANDLE: $(""), $(null), $(undefined), $(false)
		if ( !selector ) {
			return this;
		}

		// Handle HTML strings
		if ( typeof selector === "string" ) {
			if ( selector.charAt(0) === "<" && selector.charAt( selector.length - 1 ) === ">" && selector.length >= 3 ) {
				// Assume that strings that start and end with <> are HTML and skip the regex check
				match = [ null, selector, null ];

			} else {
				match = rquickExpr.exec( selector );
			}

			// Match html or make sure no context is specified for #id
			if ( match && (match[1] || !context) ) {

				// HANDLE: $(html) -> $(array)
				if ( match[1] ) {
					context = context instanceof jQuery ? context[0] : context;

					// scripts is true for back-compat
					jQuery.merge( this, jQuery.parseHTML(
						match[1],
						context && context.nodeType ? context.ownerDocument || context : document,
						true
					) );

					// HANDLE: $(html, props)
					if ( rsingleTag.test( match[1] ) && jQuery.isPlainObject( context ) ) {
						for ( match in context ) {
							// Properties of context are called as methods if possible
							if ( jQuery.isFunction( this[ match ] ) ) {
								this[ match ]( context[ match ] );

							// ...and otherwise set as attributes
							} else {
								this.attr( match, context[ match ] );
							}
						}
					}

					return this;

				// HANDLE: $(#id)
				} else {
					elem = document.getElementById( match[2] );

					// Check parentNode to catch when Blackberry 4.6 returns
					// nodes that are no longer in the document #6963
					if ( elem && elem.parentNode ) {
						// Handle the case where IE and Opera return items
						// by name instead of ID
						if ( elem.id !== match[2] ) {
							return rootjQuery.find( selector );
						}

						// Otherwise, we inject the element directly into the jQuery object
						this.length = 1;
						this[0] = elem;
					}

					this.context = document;
					this.selector = selector;
					return this;
				}

			// HANDLE: $(expr, $(...))
			} else if ( !context || context.jquery ) {
				return ( context || rootjQuery ).find( selector );

			// HANDLE: $(expr, context)
			// (which is just equivalent to: $(context).find(expr)
			} else {
				return this.constructor( context ).find( selector );
			}

		// HANDLE: $(DOMElement)
		} else if ( selector.nodeType ) {
			this.context = this[0] = selector;
			this.length = 1;
			return this;

		// HANDLE: $(function)
		// Shortcut for document ready
		} else if ( jQuery.isFunction( selector ) ) {
			return rootjQuery.ready( selector );
		}

		if ( selector.selector !== undefined ) {
			this.selector = selector.selector;
			this.context = selector.context;
		}

		return jQuery.makeArray( selector, this );
	},

	// Start with an empty selector
	selector: "",

	// The default length of a jQuery object is 0
	length: 0,

	toArray: function() {
		return core_slice.call( this );
	},

	// Get the Nth element in the matched element set OR
	// Get the whole matched element set as a clean array
	get: function( num ) {
		return num == null ?

			// Return a 'clean' array
			this.toArray() :

			// Return just the object
			( num < 0 ? this[ this.length + num ] : this[ num ] );
	},

	// Take an array of elements and push it onto the stack
	// (returning the new matched element set)
	pushStack: function( elems ) {

		// Build a new jQuery matched element set
		var ret = jQuery.merge( this.constructor(), elems );

		// Add the old object onto the stack (as a reference)
		ret.prevObject = this;
		ret.context = this.context;

		// Return the newly-formed element set
		return ret;
	},

	// Execute a callback for every element in the matched set.
	// (You can seed the arguments with an array of args, but this is
	// only used internally.)
	each: function( callback, args ) {
		return jQuery.each( this, callback, args );
	},

	ready: function( fn ) {
		// Add the callback
		jQuery.ready.promise().done( fn );

		return this;
	},

	slice: function() {
		return this.pushStack( core_slice.apply( this, arguments ) );
	},

	first: function() {
		return this.eq( 0 );
	},

	last: function() {
		return this.eq( -1 );
	},

	eq: function( i ) {
		var len = this.length,
			j = +i + ( i < 0 ? len : 0 );
		return this.pushStack( j >= 0 && j < len ? [ this[j] ] : [] );
	},

	map: function( callback ) {
		return this.pushStack( jQuery.map(this, function( elem, i ) {
			return callback.call( elem, i, elem );
		}));
	},

	end: function() {
		return this.prevObject || this.constructor(null);
	},

	// For internal use only.
	// Behaves like an Array's method, not like a jQuery method.
	push: core_push,
	sort: [].sort,
	splice: [].splice
};

// Give the init function the jQuery prototype for later instantiation
jQuery.fn.init.prototype = jQuery.fn;

jQuery.extend = jQuery.fn.extend = function() {
	var src, copyIsArray, copy, name, options, clone,
		target = arguments[0] || {},
		i = 1,
		length = arguments.length,
		deep = false;

	// Handle a deep copy situation
	if ( typeof target === "boolean" ) {
		deep = target;
		target = arguments[1] || {};
		// skip the boolean and the target
		i = 2;
	}

	// Handle case when target is a string or something (possible in deep copy)
	if ( typeof target !== "object" && !jQuery.isFunction(target) ) {
		target = {};
	}

	// extend jQuery itself if only one argument is passed
	if ( length === i ) {
		target = this;
		--i;
	}

	for ( ; i < length; i++ ) {
		// Only deal with non-null/undefined values
		if ( (options = arguments[ i ]) != null ) {
			// Extend the base object
			for ( name in options ) {
				src = target[ name ];
				copy = options[ name ];

				// Prevent never-ending loop
				if ( target === copy ) {
					continue;
				}

				// Recurse if we're merging plain objects or arrays
				if ( deep && copy && ( jQuery.isPlainObject(copy) || (copyIsArray = jQuery.isArray(copy)) ) ) {
					if ( copyIsArray ) {
						copyIsArray = false;
						clone = src && jQuery.isArray(src) ? src : [];

					} else {
						clone = src && jQuery.isPlainObject(src) ? src : {};
					}

					// Never move original objects, clone them
					target[ name ] = jQuery.extend( deep, clone, copy );

				// Don't bring in undefined values
				} else if ( copy !== undefined ) {
					target[ name ] = copy;
				}
			}
		}
	}

	// Return the modified object
	return target;
};

jQuery.extend({
	// Unique for each copy of jQuery on the page
	// Non-digits removed to match rinlinejQuery
	expando: "jQuery" + ( core_version + Math.random() ).replace( /\D/g, "" ),

	noConflict: function( deep ) {
		if ( window.$ === jQuery ) {
			window.$ = _$;
		}

		if ( deep && window.jQuery === jQuery ) {
			window.jQuery = _jQuery;
		}

		return jQuery;
	},

	// Is the DOM ready to be used? Set to true once it occurs.
	isReady: false,

	// A counter to track how many items to wait for before
	// the ready event fires. See #6781
	readyWait: 1,

	// Hold (or release) the ready event
	holdReady: function( hold ) {
		if ( hold ) {
			jQuery.readyWait++;
		} else {
			jQuery.ready( true );
		}
	},

	// Handle when the DOM is ready
	ready: function( wait ) {

		// Abort if there are pending holds or we're already ready
		if ( wait === true ? --jQuery.readyWait : jQuery.isReady ) {
			return;
		}

		// Make sure body exists, at least, in case IE gets a little overzealous (ticket #5443).
		if ( !document.body ) {
			return setTimeout( jQuery.ready );
		}

		// Remember that the DOM is ready
		jQuery.isReady = true;

		// If a normal DOM Ready event fired, decrement, and wait if need be
		if ( wait !== true && --jQuery.readyWait > 0 ) {
			return;
		}

		// If there are functions bound, to execute
		readyList.resolveWith( document, [ jQuery ] );

		// Trigger any bound ready events
		if ( jQuery.fn.trigger ) {
			jQuery( document ).trigger("ready").off("ready");
		}
	},

	// See test/unit/core.js for details concerning isFunction.
	// Since version 1.3, DOM methods and functions like alert
	// aren't supported. They return false on IE (#2968).
	isFunction: function( obj ) {
		return jQuery.type(obj) === "function";
	},

	isArray: Array.isArray || function( obj ) {
		return jQuery.type(obj) === "array";
	},

	isWindow: function( obj ) {
		/* jshint eqeqeq: false */
		return obj != null && obj == obj.window;
	},

	isNumeric: function( obj ) {
		return !isNaN( parseFloat(obj) ) && isFinite( obj );
	},

	type: function( obj ) {
		if ( obj == null ) {
			return String( obj );
		}
		return typeof obj === "object" || typeof obj === "function" ?
			class2type[ core_toString.call(obj) ] || "object" :
			typeof obj;
	},

	isPlainObject: function( obj ) {
		var key;

		// Must be an Object.
		// Because of IE, we also have to check the presence of the constructor property.
		// Make sure that DOM nodes and window objects don't pass through, as well
		if ( !obj || jQuery.type(obj) !== "object" || obj.nodeType || jQuery.isWindow( obj ) ) {
			return false;
		}

		try {
			// Not own constructor property must be Object
			if ( obj.constructor &&
				!core_hasOwn.call(obj, "constructor") &&
				!core_hasOwn.call(obj.constructor.prototype, "isPrototypeOf") ) {
				return false;
			}
		} catch ( e ) {
			// IE8,9 Will throw exceptions on certain host objects #9897
			return false;
		}

		// Support: IE<9
		// Handle iteration over inherited properties before own properties.
		if ( jQuery.support.ownLast ) {
			for ( key in obj ) {
				return core_hasOwn.call( obj, key );
			}
		}

		// Own properties are enumerated firstly, so to speed up,
		// if last one is own, then all properties are own.
		for ( key in obj ) {}

		return key === undefined || core_hasOwn.call( obj, key );
	},

	isEmptyObject: function( obj ) {
		var name;
		for ( name in obj ) {
			return false;
		}
		return true;
	},

	error: function( msg ) {
		throw new Error( msg );
	},

	// data: string of html
	// context (optional): If specified, the fragment will be created in this context, defaults to document
	// keepScripts (optional): If true, will include scripts passed in the html string
	parseHTML: function( data, context, keepScripts ) {
		if ( !data || typeof data !== "string" ) {
			return null;
		}
		if ( typeof context === "boolean" ) {
			keepScripts = context;
			context = false;
		}
		context = context || document;

		var parsed = rsingleTag.exec( data ),
			scripts = !keepScripts && [];

		// Single tag
		if ( parsed ) {
			return [ context.createElement( parsed[1] ) ];
		}

		parsed = jQuery.buildFragment( [ data ], context, scripts );
		if ( scripts ) {
			jQuery( scripts ).remove();
		}
		return jQuery.merge( [], parsed.childNodes );
	},

	parseJSON: function( data ) {
		// Attempt to parse using the native JSON parser first
		if ( window.JSON && window.JSON.parse ) {
			return window.JSON.parse( data );
		}

		if ( data === null ) {
			return data;
		}

		if ( typeof data === "string" ) {

			// Make sure leading/trailing whitespace is removed (IE can't handle it)
			data = jQuery.trim( data );

			if ( data ) {
				// Make sure the incoming data is actual JSON
				// Logic borrowed from http://json.org/json2.js
				if ( rvalidchars.test( data.replace( rvalidescape, "@" )
					.replace( rvalidtokens, "]" )
					.replace( rvalidbraces, "")) ) {

					return ( new Function( "return " + data ) )();
				}
			}
		}

		jQuery.error( "Invalid JSON: " + data );
	},

	// Cross-browser xml parsing
	parseXML: function( data ) {
		var xml, tmp;
		if ( !data || typeof data !== "string" ) {
			return null;
		}
		try {
			if ( window.DOMParser ) { // Standard
				tmp = new DOMParser();
				xml = tmp.parseFromString( data , "text/xml" );
			} else { // IE
				xml = new ActiveXObject( "Microsoft.XMLDOM" );
				xml.async = "false";
				xml.loadXML( data );
			}
		} catch( e ) {
			xml = undefined;
		}
		if ( !xml || !xml.documentElement || xml.getElementsByTagName( "parsererror" ).length ) {
			jQuery.error( "Invalid XML: " + data );
		}
		return xml;
	},

	noop: function() {},

	// Evaluates a script in a global context
	// Workarounds based on findings by Jim Driscoll
	// http://weblogs.java.net/blog/driscoll/archive/2009/09/08/eval-javascript-global-context
	globalEval: function( data ) {
		if ( data && jQuery.trim( data ) ) {
			// We use execScript on Internet Explorer
			// We use an anonymous function so that context is window
			// rather than jQuery in Firefox
			( window.execScript || function( data ) {
				window[ "eval" ].call( window, data );
			} )( data );
		}
	},

	// Convert dashed to camelCase; used by the css and data modules
	// Microsoft forgot to hump their vendor prefix (#9572)
	camelCase: function( string ) {
		return string.replace( rmsPrefix, "ms-" ).replace( rdashAlpha, fcamelCase );
	},

	nodeName: function( elem, name ) {
		return elem.nodeName && elem.nodeName.toLowerCase() === name.toLowerCase();
	},

	// args is for internal usage only
	each: function( obj, callback, args ) {
		var value,
			i = 0,
			length = obj.length,
			isArray = isArraylike( obj );

		if ( args ) {
			if ( isArray ) {
				for ( ; i < length; i++ ) {
					value = callback.apply( obj[ i ], args );

					if ( value === false ) {
						break;
					}
				}
			} else {
				for ( i in obj ) {
					value = callback.apply( obj[ i ], args );

					if ( value === false ) {
						break;
					}
				}
			}

		// A special, fast, case for the most common use of each
		} else {
			if ( isArray ) {
				for ( ; i < length; i++ ) {
					value = callback.call( obj[ i ], i, obj[ i ] );

					if ( value === false ) {
						break;
					}
				}
			} else {
				for ( i in obj ) {
					value = callback.call( obj[ i ], i, obj[ i ] );

					if ( value === false ) {
						break;
					}
				}
			}
		}

		return obj;
	},

	// Use native String.trim function wherever possible
	trim: core_trim && !core_trim.call("\uFEFF\xA0") ?
		function( text ) {
			return text == null ?
				"" :
				core_trim.call( text );
		} :

		// Otherwise use our own trimming functionality
		function( text ) {
			return text == null ?
				"" :
				( text + "" ).replace( rtrim, "" );
		},

	// results is for internal usage only
	makeArray: function( arr, results ) {
		var ret = results || [];

		if ( arr != null ) {
			if ( isArraylike( Object(arr) ) ) {
				jQuery.merge( ret,
					typeof arr === "string" ?
					[ arr ] : arr
				);
			} else {
				core_push.call( ret, arr );
			}
		}

		return ret;
	},

	inArray: function( elem, arr, i ) {
		var len;

		if ( arr ) {
			if ( core_indexOf ) {
				return core_indexOf.call( arr, elem, i );
			}

			len = arr.length;
			i = i ? i < 0 ? Math.max( 0, len + i ) : i : 0;

			for ( ; i < len; i++ ) {
				// Skip accessing in sparse arrays
				if ( i in arr && arr[ i ] === elem ) {
					return i;
				}
			}
		}

		return -1;
	},

	merge: function( first, second ) {
		var l = second.length,
			i = first.length,
			j = 0;

		if ( typeof l === "number" ) {
			for ( ; j < l; j++ ) {
				first[ i++ ] = second[ j ];
			}
		} else {
			while ( second[j] !== undefined ) {
				first[ i++ ] = second[ j++ ];
			}
		}

		first.length = i;

		return first;
	},

	grep: function( elems, callback, inv ) {
		var retVal,
			ret = [],
			i = 0,
			length = elems.length;
		inv = !!inv;

		// Go through the array, only saving the items
		// that pass the validator function
		for ( ; i < length; i++ ) {
			retVal = !!callback( elems[ i ], i );
			if ( inv !== retVal ) {
				ret.push( elems[ i ] );
			}
		}

		return ret;
	},

	// arg is for internal usage only
	map: function( elems, callback, arg ) {
		var value,
			i = 0,
			length = elems.length,
			isArray = isArraylike( elems ),
			ret = [];

		// Go through the array, translating each of the items to their
		if ( isArray ) {
			for ( ; i < length; i++ ) {
				value = callback( elems[ i ], i, arg );

				if ( value != null ) {
					ret[ ret.length ] = value;
				}
			}

		// Go through every key on the object,
		} else {
			for ( i in elems ) {
				value = callback( elems[ i ], i, arg );

				if ( value != null ) {
					ret[ ret.length ] = value;
				}
			}
		}

		// Flatten any nested arrays
		return core_concat.apply( [], ret );
	},

	// A global GUID counter for objects
	guid: 1,

	// Bind a function to a context, optionally partially applying any
	// arguments.
	proxy: function( fn, context ) {
		var args, proxy, tmp;

		if ( typeof context === "string" ) {
			tmp = fn[ context ];
			context = fn;
			fn = tmp;
		}

		// Quick check to determine if target is callable, in the spec
		// this throws a TypeError, but we will just return undefined.
		if ( !jQuery.isFunction( fn ) ) {
			return undefined;
		}

		// Simulated bind
		args = core_slice.call( arguments, 2 );
		proxy = function() {
			return fn.apply( context || this, args.concat( core_slice.call( arguments ) ) );
		};

		// Set the guid of unique handler to the same of original handler, so it can be removed
		proxy.guid = fn.guid = fn.guid || jQuery.guid++;

		return proxy;
	},

	// Multifunctional method to get and set values of a collection
	// The value/s can optionally be executed if it's a function
	access: function( elems, fn, key, value, chainable, emptyGet, raw ) {
		var i = 0,
			length = elems.length,
			bulk = key == null;

		// Sets many values
		if ( jQuery.type( key ) === "object" ) {
			chainable = true;
			for ( i in key ) {
				jQuery.access( elems, fn, i, key[i], true, emptyGet, raw );
			}

		// Sets one value
		} else if ( value !== undefined ) {
			chainable = true;

			if ( !jQuery.isFunction( value ) ) {
				raw = true;
			}

			if ( bulk ) {
				// Bulk operations run against the entire set
				if ( raw ) {
					fn.call( elems, value );
					fn = null;

				// ...except when executing function values
				} else {
					bulk = fn;
					fn = function( elem, key, value ) {
						return bulk.call( jQuery( elem ), value );
					};
				}
			}

			if ( fn ) {
				for ( ; i < length; i++ ) {
					fn( elems[i], key, raw ? value : value.call( elems[i], i, fn( elems[i], key ) ) );
				}
			}
		}

		return chainable ?
			elems :

			// Gets
			bulk ?
				fn.call( elems ) :
				length ? fn( elems[0], key ) : emptyGet;
	},

	now: function() {
		return ( new Date() ).getTime();
	},

	// A method for quickly swapping in/out CSS properties to get correct calculations.
	// Note: this method belongs to the css module but it's needed here for the support module.
	// If support gets modularized, this method should be moved back to the css module.
	swap: function( elem, options, callback, args ) {
		var ret, name,
			old = {};

		// Remember the old values, and insert the new ones
		for ( name in options ) {
			old[ name ] = elem.style[ name ];
			elem.style[ name ] = options[ name ];
		}

		ret = callback.apply( elem, args || [] );

		// Revert the old values
		for ( name in options ) {
			elem.style[ name ] = old[ name ];
		}

		return ret;
	}
});

jQuery.ready.promise = function( obj ) {
	if ( !readyList ) {

		readyList = jQuery.Deferred();

		// Catch cases where $(document).ready() is called after the browser event has already occurred.
		// we once tried to use readyState "interactive" here, but it caused issues like the one
		// discovered by ChrisS here: http://bugs.jquery.com/ticket/12282#comment:15
		if ( document.readyState === "complete" ) {
			// Handle it asynchronously to allow scripts the opportunity to delay ready
			setTimeout( jQuery.ready );

		// Standards-based browsers support DOMContentLoaded
		} else if ( document.addEventListener ) {
			// Use the handy event callback
			document.addEventListener( "DOMContentLoaded", completed, false );

			// A fallback to window.onload, that will always work
			window.addEventListener( "load", completed, false );

		// If IE event model is used
		} else {
			// Ensure firing before onload, maybe late but safe also for iframes
			document.attachEvent( "onreadystatechange", completed );

			// A fallback to window.onload, that will always work
			window.attachEvent( "onload", completed );

			// If IE and not a frame
			// continually check to see if the document is ready
			var top = false;

			try {
				top = window.frameElement == null && document.documentElement;
			} catch(e) {}

			if ( top && top.doScroll ) {
				(function doScrollCheck() {
					if ( !jQuery.isReady ) {

						try {
							// Use the trick by Diego Perini
							// http://javascript.nwbox.com/IEContentLoaded/
							top.doScroll("left");
						} catch(e) {
							return setTimeout( doScrollCheck, 50 );
						}

						// detach all dom ready events
						detach();

						// and execute any waiting functions
						jQuery.ready();
					}
				})();
			}
		}
	}
	return readyList.promise( obj );
};

// Populate the class2type map
jQuery.each("Boolean Number String Function Array Date RegExp Object Error".split(" "), function(i, name) {
	class2type[ "[object " + name + "]" ] = name.toLowerCase();
});

function isArraylike( obj ) {
	var length = obj.length,
		type = jQuery.type( obj );

	if ( jQuery.isWindow( obj ) ) {
		return false;
	}

	if ( obj.nodeType === 1 && length ) {
		return true;
	}

	return type === "array" || type !== "function" &&
		( length === 0 ||
		typeof length === "number" && length > 0 && ( length - 1 ) in obj );
}

// All jQuery objects should point back to these
rootjQuery = jQuery(document);
/*!
 * Sizzle CSS Selector Engine v1.10.2
 * http://sizzlejs.com/
 *
 * Copyright 2013 jQuery Foundation, Inc. and other contributors
 * Released under the MIT license
 * http://jquery.org/license
 *
 * Date: 2013-07-03
 */
(function( window, undefined ) {

var i,
	support,
	cachedruns,
	Expr,
	getText,
	isXML,
	compile,
	outermostContext,
	sortInput,

	// Local document vars
	setDocument,
	document,
	docElem,
	documentIsHTML,
	rbuggyQSA,
	rbuggyMatches,
	matches,
	contains,

	// Instance-specific data
	expando = "sizzle" + -(new Date()),
	preferredDoc = window.document,
	dirruns = 0,
	done = 0,
	classCache = createCache(),
	tokenCache = createCache(),
	compilerCache = createCache(),
	hasDuplicate = false,
	sortOrder = function( a, b ) {
		if ( a === b ) {
			hasDuplicate = true;
			return 0;
		}
		return 0;
	},

	// General-purpose constants
	strundefined = typeof undefined,
	MAX_NEGATIVE = 1 << 31,

	// Instance methods
	hasOwn = ({}).hasOwnProperty,
	arr = [],
	pop = arr.pop,
	push_native = arr.push,
	push = arr.push,
	slice = arr.slice,
	// Use a stripped-down indexOf if we can't use a native one
	indexOf = arr.indexOf || function( elem ) {
		var i = 0,
			len = this.length;
		for ( ; i < len; i++ ) {
			if ( this[i] === elem ) {
				return i;
			}
		}
		return -1;
	},

	booleans = "checked|selected|async|autofocus|autoplay|controls|defer|disabled|hidden|ismap|loop|multiple|open|readonly|required|scoped",

	// Regular expressions

	// Whitespace characters http://www.w3.org/TR/css3-selectors/#whitespace
	whitespace = "[\\x20\\t\\r\\n\\f]",
	// http://www.w3.org/TR/css3-syntax/#characters
	characterEncoding = "(?:\\\\.|[\\w-]|[^\\x00-\\xa0])+",

	// Loosely modeled on CSS identifier characters
	// An unquoted value should be a CSS identifier http://www.w3.org/TR/css3-selectors/#attribute-selectors
	// Proper syntax: http://www.w3.org/TR/CSS21/syndata.html#value-def-identifier
	identifier = characterEncoding.replace( "w", "w#" ),

	// Acceptable operators http://www.w3.org/TR/selectors/#attribute-selectors
	attributes = "\\[" + whitespace + "*(" + characterEncoding + ")" + whitespace +
		"*(?:([*^$|!~]?=)" + whitespace + "*(?:(['\"])((?:\\\\.|[^\\\\])*?)\\3|(" + identifier + ")|)|)" + whitespace + "*\\]",

	// Prefer arguments quoted,
	//   then not containing pseudos/brackets,
	//   then attribute selectors/non-parenthetical expressions,
	//   then anything else
	// These preferences are here to reduce the number of selectors
	//   needing tokenize in the PSEUDO preFilter
	pseudos = ":(" + characterEncoding + ")(?:\\(((['\"])((?:\\\\.|[^\\\\])*?)\\3|((?:\\\\.|[^\\\\()[\\]]|" + attributes.replace( 3, 8 ) + ")*)|.*)\\)|)",

	// Leading and non-escaped trailing whitespace, capturing some non-whitespace characters preceding the latter
	rtrim = new RegExp( "^" + whitespace + "+|((?:^|[^\\\\])(?:\\\\.)*)" + whitespace + "+$", "g" ),

	rcomma = new RegExp( "^" + whitespace + "*," + whitespace + "*" ),
	rcombinators = new RegExp( "^" + whitespace + "*([>+~]|" + whitespace + ")" + whitespace + "*" ),

	rsibling = new RegExp( whitespace + "*[+~]" ),
	rattributeQuotes = new RegExp( "=" + whitespace + "*([^\\]'\"]*)" + whitespace + "*\\]", "g" ),

	rpseudo = new RegExp( pseudos ),
	ridentifier = new RegExp( "^" + identifier + "$" ),

	matchExpr = {
		"ID": new RegExp( "^#(" + characterEncoding + ")" ),
		"CLASS": new RegExp( "^\\.(" + characterEncoding + ")" ),
		"TAG": new RegExp( "^(" + characterEncoding.replace( "w", "w*" ) + ")" ),
		"ATTR": new RegExp( "^" + attributes ),
		"PSEUDO": new RegExp( "^" + pseudos ),
		"CHILD": new RegExp( "^:(only|first|last|nth|nth-last)-(child|of-type)(?:\\(" + whitespace +
			"*(even|odd|(([+-]|)(\\d*)n|)" + whitespace + "*(?:([+-]|)" + whitespace +
			"*(\\d+)|))" + whitespace + "*\\)|)", "i" ),
		"bool": new RegExp( "^(?:" + booleans + ")$", "i" ),
		// For use in libraries implementing .is()
		// We use this for POS matching in `select`
		"needsContext": new RegExp( "^" + whitespace + "*[>+~]|:(even|odd|eq|gt|lt|nth|first|last)(?:\\(" +
			whitespace + "*((?:-\\d)?\\d*)" + whitespace + "*\\)|)(?=[^-]|$)", "i" )
	},

	rnative = /^[^{]+\{\s*\[native \w/,

	// Easily-parseable/retrievable ID or TAG or CLASS selectors
	rquickExpr = /^(?:#([\w-]+)|(\w+)|\.([\w-]+))$/,

	rinputs = /^(?:input|select|textarea|button)$/i,
	rheader = /^h\d$/i,

	rescape = /'|\\/g,

	// CSS escapes http://www.w3.org/TR/CSS21/syndata.html#escaped-characters
	runescape = new RegExp( "\\\\([\\da-f]{1,6}" + whitespace + "?|(" + whitespace + ")|.)", "ig" ),
	funescape = function( _, escaped, escapedWhitespace ) {
		var high = "0x" + escaped - 0x10000;
		// NaN means non-codepoint
		// Support: Firefox
		// Workaround erroneous numeric interpretation of +"0x"
		return high !== high || escapedWhitespace ?
			escaped :
			// BMP codepoint
			high < 0 ?
				String.fromCharCode( high + 0x10000 ) :
				// Supplemental Plane codepoint (surrogate pair)
				String.fromCharCode( high >> 10 | 0xD800, high & 0x3FF | 0xDC00 );
	};

// Optimize for push.apply( _, NodeList )
try {
	push.apply(
		(arr = slice.call( preferredDoc.childNodes )),
		preferredDoc.childNodes
	);
	// Support: Android<4.0
	// Detect silently failing push.apply
	arr[ preferredDoc.childNodes.length ].nodeType;
} catch ( e ) {
	push = { apply: arr.length ?

		// Leverage slice if possible
		function( target, els ) {
			push_native.apply( target, slice.call(els) );
		} :

		// Support: IE<9
		// Otherwise append directly
		function( target, els ) {
			var j = target.length,
				i = 0;
			// Can't trust NodeList.length
			while ( (target[j++] = els[i++]) ) {}
			target.length = j - 1;
		}
	};
}

function Sizzle( selector, context, results, seed ) {
	var match, elem, m, nodeType,
		// QSA vars
		i, groups, old, nid, newContext, newSelector;

	if ( ( context ? context.ownerDocument || context : preferredDoc ) !== document ) {
		setDocument( context );
	}

	context = context || document;
	results = results || [];

	if ( !selector || typeof selector !== "string" ) {
		return results;
	}

	if ( (nodeType = context.nodeType) !== 1 && nodeType !== 9 ) {
		return [];
	}

	if ( documentIsHTML && !seed ) {

		// Shortcuts
		if ( (match = rquickExpr.exec( selector )) ) {
			// Speed-up: Sizzle("#ID")
			if ( (m = match[1]) ) {
				if ( nodeType === 9 ) {
					elem = context.getElementById( m );
					// Check parentNode to catch when Blackberry 4.6 returns
					// nodes that are no longer in the document #6963
					if ( elem && elem.parentNode ) {
						// Handle the case where IE, Opera, and Webkit return items
						// by name instead of ID
						if ( elem.id === m ) {
							results.push( elem );
							return results;
						}
					} else {
						return results;
					}
				} else {
					// Context is not a document
					if ( context.ownerDocument && (elem = context.ownerDocument.getElementById( m )) &&
						contains( context, elem ) && elem.id === m ) {
						results.push( elem );
						return results;
					}
				}

			// Speed-up: Sizzle("TAG")
			} else if ( match[2] ) {
				push.apply( results, context.getElementsByTagName( selector ) );
				return results;

			// Speed-up: Sizzle(".CLASS")
			} else if ( (m = match[3]) && support.getElementsByClassName && context.getElementsByClassName ) {
				push.apply( results, context.getElementsByClassName( m ) );
				return results;
			}
		}

		// QSA path
		if ( support.qsa && (!rbuggyQSA || !rbuggyQSA.test( selector )) ) {
			nid = old = expando;
			newContext = context;
			newSelector = nodeType === 9 && selector;

			// qSA works strangely on Element-rooted queries
			// We can work around this by specifying an extra ID on the root
			// and working up from there (Thanks to Andrew Dupont for the technique)
			// IE 8 doesn't work on object elements
			if ( nodeType === 1 && context.nodeName.toLowerCase() !== "object" ) {
				groups = tokenize( selector );

				if ( (old = context.getAttribute("id")) ) {
					nid = old.replace( rescape, "\\$&" );
				} else {
					context.setAttribute( "id", nid );
				}
				nid = "[id='" + nid + "'] ";

				i = groups.length;
				while ( i-- ) {
					groups[i] = nid + toSelector( groups[i] );
				}
				newContext = rsibling.test( selector ) && context.parentNode || context;
				newSelector = groups.join(",");
			}

			if ( newSelector ) {
				try {
					push.apply( results,
						newContext.querySelectorAll( newSelector )
					);
					return results;
				} catch(qsaError) {
				} finally {
					if ( !old ) {
						context.removeAttribute("id");
					}
				}
			}
		}
	}

	// All others
	return select( selector.replace( rtrim, "$1" ), context, results, seed );
}

/**
 * Create key-value caches of limited size
 * @returns {Function(string, Object)} Returns the Object data after storing it on itself with
 *	property name the (space-suffixed) string and (if the cache is larger than Expr.cacheLength)
 *	deleting the oldest entry
 */
function createCache() {
	var keys = [];

	function cache( key, value ) {
		// Use (key + " ") to avoid collision with native prototype properties (see Issue #157)
		if ( keys.push( key += " " ) > Expr.cacheLength ) {
			// Only keep the most recent entries
			delete cache[ keys.shift() ];
		}
		return (cache[ key ] = value);
	}
	return cache;
}

/**
 * Mark a function for special use by Sizzle
 * @param {Function} fn The function to mark
 */
function markFunction( fn ) {
	fn[ expando ] = true;
	return fn;
}

/**
 * Support testing using an element
 * @param {Function} fn Passed the created div and expects a boolean result
 */
function assert( fn ) {
	var div = document.createElement("div");

	try {
		return !!fn( div );
	} catch (e) {
		return false;
	} finally {
		// Remove from its parent by default
		if ( div.parentNode ) {
			div.parentNode.removeChild( div );
		}
		// release memory in IE
		div = null;
	}
}

/**
 * Adds the same handler for all of the specified attrs
 * @param {String} attrs Pipe-separated list of attributes
 * @param {Function} handler The method that will be applied
 */
function addHandle( attrs, handler ) {
	var arr = attrs.split("|"),
		i = attrs.length;

	while ( i-- ) {
		Expr.attrHandle[ arr[i] ] = handler;
	}
}

/**
 * Checks document order of two siblings
 * @param {Element} a
 * @param {Element} b
 * @returns {Number} Returns less than 0 if a precedes b, greater than 0 if a follows b
 */
function siblingCheck( a, b ) {
	var cur = b && a,
		diff = cur && a.nodeType === 1 && b.nodeType === 1 &&
			( ~b.sourceIndex || MAX_NEGATIVE ) -
			( ~a.sourceIndex || MAX_NEGATIVE );

	// Use IE sourceIndex if available on both nodes
	if ( diff ) {
		return diff;
	}

	// Check if b follows a
	if ( cur ) {
		while ( (cur = cur.nextSibling) ) {
			if ( cur === b ) {
				return -1;
			}
		}
	}

	return a ? 1 : -1;
}

/**
 * Returns a function to use in pseudos for input types
 * @param {String} type
 */
function createInputPseudo( type ) {
	return function( elem ) {
		var name = elem.nodeName.toLowerCase();
		return name === "input" && elem.type === type;
	};
}

/**
 * Returns a function to use in pseudos for buttons
 * @param {String} type
 */
function createButtonPseudo( type ) {
	return function( elem ) {
		var name = elem.nodeName.toLowerCase();
		return (name === "input" || name === "button") && elem.type === type;
	};
}

/**
 * Returns a function to use in pseudos for positionals
 * @param {Function} fn
 */
function createPositionalPseudo( fn ) {
	return markFunction(function( argument ) {
		argument = +argument;
		return markFunction(function( seed, matches ) {
			var j,
				matchIndexes = fn( [], seed.length, argument ),
				i = matchIndexes.length;

			// Match elements found at the specified indexes
			while ( i-- ) {
				if ( seed[ (j = matchIndexes[i]) ] ) {
					seed[j] = !(matches[j] = seed[j]);
				}
			}
		});
	});
}

/**
 * Detect xml
 * @param {Element|Object} elem An element or a document
 */
isXML = Sizzle.isXML = function( elem ) {
	// documentElement is verified for cases where it doesn't yet exist
	// (such as loading iframes in IE - #4833)
	var documentElement = elem && (elem.ownerDocument || elem).documentElement;
	return documentElement ? documentElement.nodeName !== "HTML" : false;
};

// Expose support vars for convenience
support = Sizzle.support = {};

/**
 * Sets document-related variables once based on the current document
 * @param {Element|Object} [doc] An element or document object to use to set the document
 * @returns {Object} Returns the current document
 */
setDocument = Sizzle.setDocument = function( node ) {
	var doc = node ? node.ownerDocument || node : preferredDoc,
		parent = doc.defaultView;

	// If no document and documentElement is available, return
	if ( doc === document || doc.nodeType !== 9 || !doc.documentElement ) {
		return document;
	}

	// Set our document
	document = doc;
	docElem = doc.documentElement;

	// Support tests
	documentIsHTML = !isXML( doc );

	// Support: IE>8
	// If iframe document is assigned to "document" variable and if iframe has been reloaded,
	// IE will throw "permission denied" error when accessing "document" variable, see jQuery #13936
	// IE6-8 do not support the defaultView property so parent will be undefined
	if ( parent && parent.attachEvent && parent !== parent.top ) {
		parent.attachEvent( "onbeforeunload", function() {
			setDocument();
		});
	}

	/* Attributes
	---------------------------------------------------------------------- */

	// Support: IE<8
	// Verify that getAttribute really returns attributes and not properties (excepting IE8 booleans)
	support.attributes = assert(function( div ) {
		div.className = "i";
		return !div.getAttribute("className");
	});

	/* getElement(s)By*
	---------------------------------------------------------------------- */

	// Check if getElementsByTagName("*") returns only elements
	support.getElementsByTagName = assert(function( div ) {
		div.appendChild( doc.createComment("") );
		return !div.getElementsByTagName("*").length;
	});

	// Check if getElementsByClassName can be trusted
	support.getElementsByClassName = assert(function( div ) {
		div.innerHTML = "<div class='a'></div><div class='a i'></div>";

		// Support: Safari<4
		// Catch class over-caching
		div.firstChild.className = "i";
		// Support: Opera<10
		// Catch gEBCN failure to find non-leading classes
		return div.getElementsByClassName("i").length === 2;
	});

	// Support: IE<10
	// Check if getElementById returns elements by name
	// The broken getElementById methods don't pick up programatically-set names,
	// so use a roundabout getElementsByName test
	support.getById = assert(function( div ) {
		docElem.appendChild( div ).id = expando;
		return !doc.getElementsByName || !doc.getElementsByName( expando ).length;
	});

	// ID find and filter
	if ( support.getById ) {
		Expr.find["ID"] = function( id, context ) {
			if ( typeof context.getElementById !== strundefined && documentIsHTML ) {
				var m = context.getElementById( id );
				// Check parentNode to catch when Blackberry 4.6 returns
				// nodes that are no longer in the document #6963
				return m && m.parentNode ? [m] : [];
			}
		};
		Expr.filter["ID"] = function( id ) {
			var attrId = id.replace( runescape, funescape );
			return function( elem ) {
				return elem.getAttribute("id") === attrId;
			};
		};
	} else {
		// Support: IE6/7
		// getElementById is not reliable as a find shortcut
		delete Expr.find["ID"];

		Expr.filter["ID"] =  function( id ) {
			var attrId = id.replace( runescape, funescape );
			return function( elem ) {
				var node = typeof elem.getAttributeNode !== strundefined && elem.getAttributeNode("id");
				return node && node.value === attrId;
			};
		};
	}

	// Tag
	Expr.find["TAG"] = support.getElementsByTagName ?
		function( tag, context ) {
			if ( typeof context.getElementsByTagName !== strundefined ) {
				return context.getElementsByTagName( tag );
			}
		} :
		function( tag, context ) {
			var elem,
				tmp = [],
				i = 0,
				results = context.getElementsByTagName( tag );

			// Filter out possible comments
			if ( tag === "*" ) {
				while ( (elem = results[i++]) ) {
					if ( elem.nodeType === 1 ) {
						tmp.push( elem );
					}
				}

				return tmp;
			}
			return results;
		};

	// Class
	Expr.find["CLASS"] = support.getElementsByClassName && function( className, context ) {
		if ( typeof context.getElementsByClassName !== strundefined && documentIsHTML ) {
			return context.getElementsByClassName( className );
		}
	};

	/* QSA/matchesSelector
	---------------------------------------------------------------------- */

	// QSA and matchesSelector support

	// matchesSelector(:active) reports false when true (IE9/Opera 11.5)
	rbuggyMatches = [];

	// qSa(:focus) reports false when true (Chrome 21)
	// We allow this because of a bug in IE8/9 that throws an error
	// whenever `document.activeElement` is accessed on an iframe
	// So, we allow :focus to pass through QSA all the time to avoid the IE error
	// See http://bugs.jquery.com/ticket/13378
	rbuggyQSA = [];

	if ( (support.qsa = rnative.test( doc.querySelectorAll )) ) {
		// Build QSA regex
		// Regex strategy adopted from Diego Perini
		assert(function( div ) {
			// Select is set to empty string on purpose
			// This is to test IE's treatment of not explicitly
			// setting a boolean content attribute,
			// since its presence should be enough
			// http://bugs.jquery.com/ticket/12359
			div.innerHTML = "<select><option selected=''></option></select>";

			// Support: IE8
			// Boolean attributes and "value" are not treated correctly
			if ( !div.querySelectorAll("[selected]").length ) {
				rbuggyQSA.push( "\\[" + whitespace + "*(?:value|" + booleans + ")" );
			}

			// Webkit/Opera - :checked should return selected option elements
			// http://www.w3.org/TR/2011/REC-css3-selectors-20110929/#checked
			// IE8 throws error here and will not see later tests
			if ( !div.querySelectorAll(":checked").length ) {
				rbuggyQSA.push(":checked");
			}
		});

		assert(function( div ) {

			// Support: Opera 10-12/IE8
			// ^= $= *= and empty values
			// Should not select anything
			// Support: Windows 8 Native Apps
			// The type attribute is restricted during .innerHTML assignment
			var input = doc.createElement("input");
			input.setAttribute( "type", "hidden" );
			div.appendChild( input ).setAttribute( "t", "" );

			if ( div.querySelectorAll("[t^='']").length ) {
				rbuggyQSA.push( "[*^$]=" + whitespace + "*(?:''|\"\")" );
			}

			// FF 3.5 - :enabled/:disabled and hidden elements (hidden elements are still enabled)
			// IE8 throws error here and will not see later tests
			if ( !div.querySelectorAll(":enabled").length ) {
				rbuggyQSA.push( ":enabled", ":disabled" );
			}

			// Opera 10-11 does not throw on post-comma invalid pseudos
			div.querySelectorAll("*,:x");
			rbuggyQSA.push(",.*:");
		});
	}

	if ( (support.matchesSelector = rnative.test( (matches = docElem.webkitMatchesSelector ||
		docElem.mozMatchesSelector ||
		docElem.oMatchesSelector ||
		docElem.msMatchesSelector) )) ) {

		assert(function( div ) {
			// Check to see if it's possible to do matchesSelector
			// on a disconnected node (IE 9)
			support.disconnectedMatch = matches.call( div, "div" );

			// This should fail with an exception
			// Gecko does not error, returns false instead
			matches.call( div, "[s!='']:x" );
			rbuggyMatches.push( "!=", pseudos );
		});
	}

	rbuggyQSA = rbuggyQSA.length && new RegExp( rbuggyQSA.join("|") );
	rbuggyMatches = rbuggyMatches.length && new RegExp( rbuggyMatches.join("|") );

	/* Contains
	---------------------------------------------------------------------- */

	// Element contains another
	// Purposefully does not implement inclusive descendent
	// As in, an element does not contain itself
	contains = rnative.test( docElem.contains ) || docElem.compareDocumentPosition ?
		function( a, b ) {
			var adown = a.nodeType === 9 ? a.documentElement : a,
				bup = b && b.parentNode;
			return a === bup || !!( bup && bup.nodeType === 1 && (
				adown.contains ?
					adown.contains( bup ) :
					a.compareDocumentPosition && a.compareDocumentPosition( bup ) & 16
			));
		} :
		function( a, b ) {
			if ( b ) {
				while ( (b = b.parentNode) ) {
					if ( b === a ) {
						return true;
					}
				}
			}
			return false;
		};

	/* Sorting
	---------------------------------------------------------------------- */

	// Document order sorting
	sortOrder = docElem.compareDocumentPosition ?
	function( a, b ) {

		// Flag for duplicate removal
		if ( a === b ) {
			hasDuplicate = true;
			return 0;
		}

		var compare = b.compareDocumentPosition && a.compareDocumentPosition && a.compareDocumentPosition( b );

		if ( compare ) {
			// Disconnected nodes
			if ( compare & 1 ||
				(!support.sortDetached && b.compareDocumentPosition( a ) === compare) ) {

				// Choose the first element that is related to our preferred document
				if ( a === doc || contains(preferredDoc, a) ) {
					return -1;
				}
				if ( b === doc || contains(preferredDoc, b) ) {
					return 1;
				}

				// Maintain original order
				return sortInput ?
					( indexOf.call( sortInput, a ) - indexOf.call( sortInput, b ) ) :
					0;
			}

			return compare & 4 ? -1 : 1;
		}

		// Not directly comparable, sort on existence of method
		return a.compareDocumentPosition ? -1 : 1;
	} :
	function( a, b ) {
		var cur,
			i = 0,
			aup = a.parentNode,
			bup = b.parentNode,
			ap = [ a ],
			bp = [ b ];

		// Exit early if the nodes are identical
		if ( a === b ) {
			hasDuplicate = true;
			return 0;

		// Parentless nodes are either documents or disconnected
		} else if ( !aup || !bup ) {
			return a === doc ? -1 :
				b === doc ? 1 :
				aup ? -1 :
				bup ? 1 :
				sortInput ?
				( indexOf.call( sortInput, a ) - indexOf.call( sortInput, b ) ) :
				0;

		// If the nodes are siblings, we can do a quick check
		} else if ( aup === bup ) {
			return siblingCheck( a, b );
		}

		// Otherwise we need full lists of their ancestors for comparison
		cur = a;
		while ( (cur = cur.parentNode) ) {
			ap.unshift( cur );
		}
		cur = b;
		while ( (cur = cur.parentNode) ) {
			bp.unshift( cur );
		}

		// Walk down the tree looking for a discrepancy
		while ( ap[i] === bp[i] ) {
			i++;
		}

		return i ?
			// Do a sibling check if the nodes have a common ancestor
			siblingCheck( ap[i], bp[i] ) :

			// Otherwise nodes in our document sort first
			ap[i] === preferredDoc ? -1 :
			bp[i] === preferredDoc ? 1 :
			0;
	};

	return doc;
};

Sizzle.matches = function( expr, elements ) {
	return Sizzle( expr, null, null, elements );
};

Sizzle.matchesSelector = function( elem, expr ) {
	// Set document vars if needed
	if ( ( elem.ownerDocument || elem ) !== document ) {
		setDocument( elem );
	}

	// Make sure that attribute selectors are quoted
	expr = expr.replace( rattributeQuotes, "='$1']" );

	if ( support.matchesSelector && documentIsHTML &&
		( !rbuggyMatches || !rbuggyMatches.test( expr ) ) &&
		( !rbuggyQSA     || !rbuggyQSA.test( expr ) ) ) {

		try {
			var ret = matches.call( elem, expr );

			// IE 9's matchesSelector returns false on disconnected nodes
			if ( ret || support.disconnectedMatch ||
					// As well, disconnected nodes are said to be in a document
					// fragment in IE 9
					elem.document && elem.document.nodeType !== 11 ) {
				return ret;
			}
		} catch(e) {}
	}

	return Sizzle( expr, document, null, [elem] ).length > 0;
};

Sizzle.contains = function( context, elem ) {
	// Set document vars if needed
	if ( ( context.ownerDocument || context ) !== document ) {
		setDocument( context );
	}
	return contains( context, elem );
};

Sizzle.attr = function( elem, name ) {
	// Set document vars if needed
	if ( ( elem.ownerDocument || elem ) !== document ) {
		setDocument( elem );
	}

	var fn = Expr.attrHandle[ name.toLowerCase() ],
		// Don't get fooled by Object.prototype properties (jQuery #13807)
		val = fn && hasOwn.call( Expr.attrHandle, name.toLowerCase() ) ?
			fn( elem, name, !documentIsHTML ) :
			undefined;

	return val === undefined ?
		support.attributes || !documentIsHTML ?
			elem.getAttribute( name ) :
			(val = elem.getAttributeNode(name)) && val.specified ?
				val.value :
				null :
		val;
};

Sizzle.error = function( msg ) {
	throw new Error( "Syntax error, unrecognized expression: " + msg );
};

/**
 * Document sorting and removing duplicates
 * @param {ArrayLike} results
 */
Sizzle.uniqueSort = function( results ) {
	var elem,
		duplicates = [],
		j = 0,
		i = 0;

	// Unless we *know* we can detect duplicates, assume their presence
	hasDuplicate = !support.detectDuplicates;
	sortInput = !support.sortStable && results.slice( 0 );
	results.sort( sortOrder );

	if ( hasDuplicate ) {
		while ( (elem = results[i++]) ) {
			if ( elem === results[ i ] ) {
				j = duplicates.push( i );
			}
		}
		while ( j-- ) {
			results.splice( duplicates[ j ], 1 );
		}
	}

	return results;
};

/**
 * Utility function for retrieving the text value of an array of DOM nodes
 * @param {Array|Element} elem
 */
getText = Sizzle.getText = function( elem ) {
	var node,
		ret = "",
		i = 0,
		nodeType = elem.nodeType;

	if ( !nodeType ) {
		// If no nodeType, this is expected to be an array
		for ( ; (node = elem[i]); i++ ) {
			// Do not traverse comment nodes
			ret += getText( node );
		}
	} else if ( nodeType === 1 || nodeType === 9 || nodeType === 11 ) {
		// Use textContent for elements
		// innerText usage removed for consistency of new lines (see #11153)
		if ( typeof elem.textContent === "string" ) {
			return elem.textContent;
		} else {
			// Traverse its children
			for ( elem = elem.firstChild; elem; elem = elem.nextSibling ) {
				ret += getText( elem );
			}
		}
	} else if ( nodeType === 3 || nodeType === 4 ) {
		return elem.nodeValue;
	}
	// Do not include comment or processing instruction nodes

	return ret;
};

Expr = Sizzle.selectors = {

	// Can be adjusted by the user
	cacheLength: 50,

	createPseudo: markFunction,

	match: matchExpr,

	attrHandle: {},

	find: {},

	relative: {
		">": { dir: "parentNode", first: true },
		" ": { dir: "parentNode" },
		"+": { dir: "previousSibling", first: true },
		"~": { dir: "previousSibling" }
	},

	preFilter: {
		"ATTR": function( match ) {
			match[1] = match[1].replace( runescape, funescape );

			// Move the given value to match[3] whether quoted or unquoted
			match[3] = ( match[4] || match[5] || "" ).replace( runescape, funescape );

			if ( match[2] === "~=" ) {
				match[3] = " " + match[3] + " ";
			}

			return match.slice( 0, 4 );
		},

		"CHILD": function( match ) {
			/* matches from matchExpr["CHILD"]
				1 type (only|nth|...)
				2 what (child|of-type)
				3 argument (even|odd|\d*|\d*n([+-]\d+)?|...)
				4 xn-component of xn+y argument ([+-]?\d*n|)
				5 sign of xn-component
				6 x of xn-component
				7 sign of y-component
				8 y of y-component
			*/
			match[1] = match[1].toLowerCase();

			if ( match[1].slice( 0, 3 ) === "nth" ) {
				// nth-* requires argument
				if ( !match[3] ) {
					Sizzle.error( match[0] );
				}

				// numeric x and y parameters for Expr.filter.CHILD
				// remember that false/true cast respectively to 0/1
				match[4] = +( match[4] ? match[5] + (match[6] || 1) : 2 * ( match[3] === "even" || match[3] === "odd" ) );
				match[5] = +( ( match[7] + match[8] ) || match[3] === "odd" );

			// other types prohibit arguments
			} else if ( match[3] ) {
				Sizzle.error( match[0] );
			}

			return match;
		},

		"PSEUDO": function( match ) {
			var excess,
				unquoted = !match[5] && match[2];

			if ( matchExpr["CHILD"].test( match[0] ) ) {
				return null;
			}

			// Accept quoted arguments as-is
			if ( match[3] && match[4] !== undefined ) {
				match[2] = match[4];

			// Strip excess characters from unquoted arguments
			} else if ( unquoted && rpseudo.test( unquoted ) &&
				// Get excess from tokenize (recursively)
				(excess = tokenize( unquoted, true )) &&
				// advance to the next closing parenthesis
				(excess = unquoted.indexOf( ")", unquoted.length - excess ) - unquoted.length) ) {

				// excess is a negative index
				match[0] = match[0].slice( 0, excess );
				match[2] = unquoted.slice( 0, excess );
			}

			// Return only captures needed by the pseudo filter method (type and argument)
			return match.slice( 0, 3 );
		}
	},

	filter: {

		"TAG": function( nodeNameSelector ) {
			var nodeName = nodeNameSelector.replace( runescape, funescape ).toLowerCase();
			return nodeNameSelector === "*" ?
				function() { return true; } :
				function( elem ) {
					return elem.nodeName && elem.nodeName.toLowerCase() === nodeName;
				};
		},

		"CLASS": function( className ) {
			var pattern = classCache[ className + " " ];

			return pattern ||
				(pattern = new RegExp( "(^|" + whitespace + ")" + className + "(" + whitespace + "|$)" )) &&
				classCache( className, function( elem ) {
					return pattern.test( typeof elem.className === "string" && elem.className || typeof elem.getAttribute !== strundefined && elem.getAttribute("class") || "" );
				});
		},

		"ATTR": function( name, operator, check ) {
			return function( elem ) {
				var result = Sizzle.attr( elem, name );

				if ( result == null ) {
					return operator === "!=";
				}
				if ( !operator ) {
					return true;
				}

				result += "";

				return operator === "=" ? result === check :
					operator === "!=" ? result !== check :
					operator === "^=" ? check && result.indexOf( check ) === 0 :
					operator === "*=" ? check && result.indexOf( check ) > -1 :
					operator === "$=" ? check && result.slice( -check.length ) === check :
					operator === "~=" ? ( " " + result + " " ).indexOf( check ) > -1 :
					operator === "|=" ? result === check || result.slice( 0, check.length + 1 ) === check + "-" :
					false;
			};
		},

		"CHILD": function( type, what, argument, first, last ) {
			var simple = type.slice( 0, 3 ) !== "nth",
				forward = type.slice( -4 ) !== "last",
				ofType = what === "of-type";

			return first === 1 && last === 0 ?

				// Shortcut for :nth-*(n)
				function( elem ) {
					return !!elem.parentNode;
				} :

				function( elem, context, xml ) {
					var cache, outerCache, node, diff, nodeIndex, start,
						dir = simple !== forward ? "nextSibling" : "previousSibling",
						parent = elem.parentNode,
						name = ofType && elem.nodeName.toLowerCase(),
						useCache = !xml && !ofType;

					if ( parent ) {

						// :(first|last|only)-(child|of-type)
						if ( simple ) {
							while ( dir ) {
								node = elem;
								while ( (node = node[ dir ]) ) {
									if ( ofType ? node.nodeName.toLowerCase() === name : node.nodeType === 1 ) {
										return false;
									}
								}
								// Reverse direction for :only-* (if we haven't yet done so)
								start = dir = type === "only" && !start && "nextSibling";
							}
							return true;
						}

						start = [ forward ? parent.firstChild : parent.lastChild ];

						// non-xml :nth-child(...) stores cache data on `parent`
						if ( forward && useCache ) {
							// Seek `elem` from a previously-cached index
							outerCache = parent[ expando ] || (parent[ expando ] = {});
							cache = outerCache[ type ] || [];
							nodeIndex = cache[0] === dirruns && cache[1];
							diff = cache[0] === dirruns && cache[2];
							node = nodeIndex && parent.childNodes[ nodeIndex ];

							while ( (node = ++nodeIndex && node && node[ dir ] ||

								// Fallback to seeking `elem` from the start
								(diff = nodeIndex = 0) || start.pop()) ) {

								// When found, cache indexes on `parent` and break
								if ( node.nodeType === 1 && ++diff && node === elem ) {
									outerCache[ type ] = [ dirruns, nodeIndex, diff ];
									break;
								}
							}

						// Use previously-cached element index if available
						} else if ( useCache && (cache = (elem[ expando ] || (elem[ expando ] = {}))[ type ]) && cache[0] === dirruns ) {
							diff = cache[1];

						// xml :nth-child(...) or :nth-last-child(...) or :nth(-last)?-of-type(...)
						} else {
							// Use the same loop as above to seek `elem` from the start
							while ( (node = ++nodeIndex && node && node[ dir ] ||
								(diff = nodeIndex = 0) || start.pop()) ) {

								if ( ( ofType ? node.nodeName.toLowerCase() === name : node.nodeType === 1 ) && ++diff ) {
									// Cache the index of each encountered element
									if ( useCache ) {
										(node[ expando ] || (node[ expando ] = {}))[ type ] = [ dirruns, diff ];
									}

									if ( node === elem ) {
										break;
									}
								}
							}
						}

						// Incorporate the offset, then check against cycle size
						diff -= last;
						return diff === first || ( diff % first === 0 && diff / first >= 0 );
					}
				};
		},

		"PSEUDO": function( pseudo, argument ) {
			// pseudo-class names are case-insensitive
			// http://www.w3.org/TR/selectors/#pseudo-classes
			// Prioritize by case sensitivity in case custom pseudos are added with uppercase letters
			// Remember that setFilters inherits from pseudos
			var args,
				fn = Expr.pseudos[ pseudo ] || Expr.setFilters[ pseudo.toLowerCase() ] ||
					Sizzle.error( "unsupported pseudo: " + pseudo );

			// The user may use createPseudo to indicate that
			// arguments are needed to create the filter function
			// just as Sizzle does
			if ( fn[ expando ] ) {
				return fn( argument );
			}

			// But maintain support for old signatures
			if ( fn.length > 1 ) {
				args = [ pseudo, pseudo, "", argument ];
				return Expr.setFilters.hasOwnProperty( pseudo.toLowerCase() ) ?
					markFunction(function( seed, matches ) {
						var idx,
							matched = fn( seed, argument ),
							i = matched.length;
						while ( i-- ) {
							idx = indexOf.call( seed, matched[i] );
							seed[ idx ] = !( matches[ idx ] = matched[i] );
						}
					}) :
					function( elem ) {
						return fn( elem, 0, args );
					};
			}

			return fn;
		}
	},

	pseudos: {
		// Potentially complex pseudos
		"not": markFunction(function( selector ) {
			// Trim the selector passed to compile
			// to avoid treating leading and trailing
			// spaces as combinators
			var input = [],
				results = [],
				matcher = compile( selector.replace( rtrim, "$1" ) );

			return matcher[ expando ] ?
				markFunction(function( seed, matches, context, xml ) {
					var elem,
						unmatched = matcher( seed, null, xml, [] ),
						i = seed.length;

					// Match elements unmatched by `matcher`
					while ( i-- ) {
						if ( (elem = unmatched[i]) ) {
							seed[i] = !(matches[i] = elem);
						}
					}
				}) :
				function( elem, context, xml ) {
					input[0] = elem;
					matcher( input, null, xml, results );
					return !results.pop();
				};
		}),

		"has": markFunction(function( selector ) {
			return function( elem ) {
				return Sizzle( selector, elem ).length > 0;
			};
		}),

		"contains": markFunction(function( text ) {
			return function( elem ) {
				return ( elem.textContent || elem.innerText || getText( elem ) ).indexOf( text ) > -1;
			};
		}),

		// "Whether an element is represented by a :lang() selector
		// is based solely on the element's language value
		// being equal to the identifier C,
		// or beginning with the identifier C immediately followed by "-".
		// The matching of C against the element's language value is performed case-insensitively.
		// The identifier C does not have to be a valid language name."
		// http://www.w3.org/TR/selectors/#lang-pseudo
		"lang": markFunction( function( lang ) {
			// lang value must be a valid identifier
			if ( !ridentifier.test(lang || "") ) {
				Sizzle.error( "unsupported lang: " + lang );
			}
			lang = lang.replace( runescape, funescape ).toLowerCase();
			return function( elem ) {
				var elemLang;
				do {
					if ( (elemLang = documentIsHTML ?
						elem.lang :
						elem.getAttribute("xml:lang") || elem.getAttribute("lang")) ) {

						elemLang = elemLang.toLowerCase();
						return elemLang === lang || elemLang.indexOf( lang + "-" ) === 0;
					}
				} while ( (elem = elem.parentNode) && elem.nodeType === 1 );
				return false;
			};
		}),

		// Miscellaneous
		"target": function( elem ) {
			var hash = window.location && window.location.hash;
			return hash && hash.slice( 1 ) === elem.id;
		},

		"root": function( elem ) {
			return elem === docElem;
		},

		"focus": function( elem ) {
			return elem === document.activeElement && (!document.hasFocus || document.hasFocus()) && !!(elem.type || elem.href || ~elem.tabIndex);
		},

		// Boolean properties
		"enabled": function( elem ) {
			return elem.disabled === false;
		},

		"disabled": function( elem ) {
			return elem.disabled === true;
		},

		"checked": function( elem ) {
			// In CSS3, :checked should return both checked and selected elements
			// http://www.w3.org/TR/2011/REC-css3-selectors-20110929/#checked
			var nodeName = elem.nodeName.toLowerCase();
			return (nodeName === "input" && !!elem.checked) || (nodeName === "option" && !!elem.selected);
		},

		"selected": function( elem ) {
			// Accessing this property makes selected-by-default
			// options in Safari work properly
			if ( elem.parentNode ) {
				elem.parentNode.selectedIndex;
			}

			return elem.selected === true;
		},

		// Contents
		"empty": function( elem ) {
			// http://www.w3.org/TR/selectors/#empty-pseudo
			// :empty is only affected by element nodes and content nodes(including text(3), cdata(4)),
			//   not comment, processing instructions, or others
			// Thanks to Diego Perini for the nodeName shortcut
			//   Greater than "@" means alpha characters (specifically not starting with "#" or "?")
			for ( elem = elem.firstChild; elem; elem = elem.nextSibling ) {
				if ( elem.nodeName > "@" || elem.nodeType === 3 || elem.nodeType === 4 ) {
					return false;
				}
			}
			return true;
		},

		"parent": function( elem ) {
			return !Expr.pseudos["empty"]( elem );
		},

		// Element/input types
		"header": function( elem ) {
			return rheader.test( elem.nodeName );
		},

		"input": function( elem ) {
			return rinputs.test( elem.nodeName );
		},

		"button": function( elem ) {
			var name = elem.nodeName.toLowerCase();
			return name === "input" && elem.type === "button" || name === "button";
		},

		"text": function( elem ) {
			var attr;
			// IE6 and 7 will map elem.type to 'text' for new HTML5 types (search, etc)
			// use getAttribute instead to test this case
			return elem.nodeName.toLowerCase() === "input" &&
				elem.type === "text" &&
				( (attr = elem.getAttribute("type")) == null || attr.toLowerCase() === elem.type );
		},

		// Position-in-collection
		"first": createPositionalPseudo(function() {
			return [ 0 ];
		}),

		"last": createPositionalPseudo(function( matchIndexes, length ) {
			return [ length - 1 ];
		}),

		"eq": createPositionalPseudo(function( matchIndexes, length, argument ) {
			return [ argument < 0 ? argument + length : argument ];
		}),

		"even": createPositionalPseudo(function( matchIndexes, length ) {
			var i = 0;
			for ( ; i < length; i += 2 ) {
				matchIndexes.push( i );
			}
			return matchIndexes;
		}),

		"odd": createPositionalPseudo(function( matchIndexes, length ) {
			var i = 1;
			for ( ; i < length; i += 2 ) {
				matchIndexes.push( i );
			}
			return matchIndexes;
		}),

		"lt": createPositionalPseudo(function( matchIndexes, length, argument ) {
			var i = argument < 0 ? argument + length : argument;
			for ( ; --i >= 0; ) {
				matchIndexes.push( i );
			}
			return matchIndexes;
		}),

		"gt": createPositionalPseudo(function( matchIndexes, length, argument ) {
			var i = argument < 0 ? argument + length : argument;
			for ( ; ++i < length; ) {
				matchIndexes.push( i );
			}
			return matchIndexes;
		})
	}
};

Expr.pseudos["nth"] = Expr.pseudos["eq"];

// Add button/input type pseudos
for ( i in { radio: true, checkbox: true, file: true, password: true, image: true } ) {
	Expr.pseudos[ i ] = createInputPseudo( i );
}
for ( i in { submit: true, reset: true } ) {
	Expr.pseudos[ i ] = createButtonPseudo( i );
}

// Easy API for creating new setFilters
function setFilters() {}
setFilters.prototype = Expr.filters = Expr.pseudos;
Expr.setFilters = new setFilters();

function tokenize( selector, parseOnly ) {
	var matched, match, tokens, type,
		soFar, groups, preFilters,
		cached = tokenCache[ selector + " " ];

	if ( cached ) {
		return parseOnly ? 0 : cached.slice( 0 );
	}

	soFar = selector;
	groups = [];
	preFilters = Expr.preFilter;

	while ( soFar ) {

		// Comma and first run
		if ( !matched || (match = rcomma.exec( soFar )) ) {
			if ( match ) {
				// Don't consume trailing commas as valid
				soFar = soFar.slice( match[0].length ) || soFar;
			}
			groups.push( tokens = [] );
		}

		matched = false;

		// Combinators
		if ( (match = rcombinators.exec( soFar )) ) {
			matched = match.shift();
			tokens.push({
				value: matched,
				// Cast descendant combinators to space
				type: match[0].replace( rtrim, " " )
			});
			soFar = soFar.slice( matched.length );
		}

		// Filters
		for ( type in Expr.filter ) {
			if ( (match = matchExpr[ type ].exec( soFar )) && (!preFilters[ type ] ||
				(match = preFilters[ type ]( match ))) ) {
				matched = match.shift();
				tokens.push({
					value: matched,
					type: type,
					matches: match
				});
				soFar = soFar.slice( matched.length );
			}
		}

		if ( !matched ) {
			break;
		}
	}

	// Return the length of the invalid excess
	// if we're just parsing
	// Otherwise, throw an error or return tokens
	return parseOnly ?
		soFar.length :
		soFar ?
			Sizzle.error( selector ) :
			// Cache the tokens
			tokenCache( selector, groups ).slice( 0 );
}

function toSelector( tokens ) {
	var i = 0,
		len = tokens.length,
		selector = "";
	for ( ; i < len; i++ ) {
		selector += tokens[i].value;
	}
	return selector;
}

function addCombinator( matcher, combinator, base ) {
	var dir = combinator.dir,
		checkNonElements = base && dir === "parentNode",
		doneName = done++;

	return combinator.first ?
		// Check against closest ancestor/preceding element
		function( elem, context, xml ) {
			while ( (elem = elem[ dir ]) ) {
				if ( elem.nodeType === 1 || checkNonElements ) {
					return matcher( elem, context, xml );
				}
			}
		} :

		// Check against all ancestor/preceding elements
		function( elem, context, xml ) {
			var data, cache, outerCache,
				dirkey = dirruns + " " + doneName;

			// We can't set arbitrary data on XML nodes, so they don't benefit from dir caching
			if ( xml ) {
				while ( (elem = elem[ dir ]) ) {
					if ( elem.nodeType === 1 || checkNonElements ) {
						if ( matcher( elem, context, xml ) ) {
							return true;
						}
					}
				}
			} else {
				while ( (elem = elem[ dir ]) ) {
					if ( elem.nodeType === 1 || checkNonElements ) {
						outerCache = elem[ expando ] || (elem[ expando ] = {});
						if ( (cache = outerCache[ dir ]) && cache[0] === dirkey ) {
							if ( (data = cache[1]) === true || data === cachedruns ) {
								return data === true;
							}
						} else {
							cache = outerCache[ dir ] = [ dirkey ];
							cache[1] = matcher( elem, context, xml ) || cachedruns;
							if ( cache[1] === true ) {
								return true;
							}
						}
					}
				}
			}
		};
}

function elementMatcher( matchers ) {
	return matchers.length > 1 ?
		function( elem, context, xml ) {
			var i = matchers.length;
			while ( i-- ) {
				if ( !matchers[i]( elem, context, xml ) ) {
					return false;
				}
			}
			return true;
		} :
		matchers[0];
}

function condense( unmatched, map, filter, context, xml ) {
	var elem,
		newUnmatched = [],
		i = 0,
		len = unmatched.length,
		mapped = map != null;

	for ( ; i < len; i++ ) {
		if ( (elem = unmatched[i]) ) {
			if ( !filter || filter( elem, context, xml ) ) {
				newUnmatched.push( elem );
				if ( mapped ) {
					map.push( i );
				}
			}
		}
	}

	return newUnmatched;
}

function setMatcher( preFilter, selector, matcher, postFilter, postFinder, postSelector ) {
	if ( postFilter && !postFilter[ expando ] ) {
		postFilter = setMatcher( postFilter );
	}
	if ( postFinder && !postFinder[ expando ] ) {
		postFinder = setMatcher( postFinder, postSelector );
	}
	return markFunction(function( seed, results, context, xml ) {
		var temp, i, elem,
			preMap = [],
			postMap = [],
			preexisting = results.length,

			// Get initial elements from seed or context
			elems = seed || multipleContexts( selector || "*", context.nodeType ? [ context ] : context, [] ),

			// Prefilter to get matcher input, preserving a map for seed-results synchronization
			matcherIn = preFilter && ( seed || !selector ) ?
				condense( elems, preMap, preFilter, context, xml ) :
				elems,

			matcherOut = matcher ?
				// If we have a postFinder, or filtered seed, or non-seed postFilter or preexisting results,
				postFinder || ( seed ? preFilter : preexisting || postFilter ) ?

					// ...intermediate processing is necessary
					[] :

					// ...otherwise use results directly
					results :
				matcherIn;

		// Find primary matches
		if ( matcher ) {
			matcher( matcherIn, matcherOut, context, xml );
		}

		// Apply postFilter
		if ( postFilter ) {
			temp = condense( matcherOut, postMap );
			postFilter( temp, [], context, xml );

			// Un-match failing elements by moving them back to matcherIn
			i = temp.length;
			while ( i-- ) {
				if ( (elem = temp[i]) ) {
					matcherOut[ postMap[i] ] = !(matcherIn[ postMap[i] ] = elem);
				}
			}
		}

		if ( seed ) {
			if ( postFinder || preFilter ) {
				if ( postFinder ) {
					// Get the final matcherOut by condensing this intermediate into postFinder contexts
					temp = [];
					i = matcherOut.length;
					while ( i-- ) {
						if ( (elem = matcherOut[i]) ) {
							// Restore matcherIn since elem is not yet a final match
							temp.push( (matcherIn[i] = elem) );
						}
					}
					postFinder( null, (matcherOut = []), temp, xml );
				}

				// Move matched elements from seed to results to keep them synchronized
				i = matcherOut.length;
				while ( i-- ) {
					if ( (elem = matcherOut[i]) &&
						(temp = postFinder ? indexOf.call( seed, elem ) : preMap[i]) > -1 ) {

						seed[temp] = !(results[temp] = elem);
					}
				}
			}

		// Add elements to results, through postFinder if defined
		} else {
			matcherOut = condense(
				matcherOut === results ?
					matcherOut.splice( preexisting, matcherOut.length ) :
					matcherOut
			);
			if ( postFinder ) {
				postFinder( null, results, matcherOut, xml );
			} else {
				push.apply( results, matcherOut );
			}
		}
	});
}

function matcherFromTokens( tokens ) {
	var checkContext, matcher, j,
		len = tokens.length,
		leadingRelative = Expr.relative[ tokens[0].type ],
		implicitRelative = leadingRelative || Expr.relative[" "],
		i = leadingRelative ? 1 : 0,

		// The foundational matcher ensures that elements are reachable from top-level context(s)
		matchContext = addCombinator( function( elem ) {
			return elem === checkContext;
		}, implicitRelative, true ),
		matchAnyContext = addCombinator( function( elem ) {
			return indexOf.call( checkContext, elem ) > -1;
		}, implicitRelative, true ),
		matchers = [ function( elem, context, xml ) {
			return ( !leadingRelative && ( xml || context !== outermostContext ) ) || (
				(checkContext = context).nodeType ?
					matchContext( elem, context, xml ) :
					matchAnyContext( elem, context, xml ) );
		} ];

	for ( ; i < len; i++ ) {
		if ( (matcher = Expr.relative[ tokens[i].type ]) ) {
			matchers = [ addCombinator(elementMatcher( matchers ), matcher) ];
		} else {
			matcher = Expr.filter[ tokens[i].type ].apply( null, tokens[i].matches );

			// Return special upon seeing a positional matcher
			if ( matcher[ expando ] ) {
				// Find the next relative operator (if any) for proper handling
				j = ++i;
				for ( ; j < len; j++ ) {
					if ( Expr.relative[ tokens[j].type ] ) {
						break;
					}
				}
				return setMatcher(
					i > 1 && elementMatcher( matchers ),
					i > 1 && toSelector(
						// If the preceding token was a descendant combinator, insert an implicit any-element `*`
						tokens.slice( 0, i - 1 ).concat({ value: tokens[ i - 2 ].type === " " ? "*" : "" })
					).replace( rtrim, "$1" ),
					matcher,
					i < j && matcherFromTokens( tokens.slice( i, j ) ),
					j < len && matcherFromTokens( (tokens = tokens.slice( j )) ),
					j < len && toSelector( tokens )
				);
			}
			matchers.push( matcher );
		}
	}

	return elementMatcher( matchers );
}

function matcherFromGroupMatchers( elementMatchers, setMatchers ) {
	// A counter to specify which element is currently being matched
	var matcherCachedRuns = 0,
		bySet = setMatchers.length > 0,
		byElement = elementMatchers.length > 0,
		superMatcher = function( seed, context, xml, results, expandContext ) {
			var elem, j, matcher,
				setMatched = [],
				matchedCount = 0,
				i = "0",
				unmatched = seed && [],
				outermost = expandContext != null,
				contextBackup = outermostContext,
				// We must always have either seed elements or context
				elems = seed || byElement && Expr.find["TAG"]( "*", expandContext && context.parentNode || context ),
				// Use integer dirruns iff this is the outermost matcher
				dirrunsUnique = (dirruns += contextBackup == null ? 1 : Math.random() || 0.1);

			if ( outermost ) {
				outermostContext = context !== document && context;
				cachedruns = matcherCachedRuns;
			}

			// Add elements passing elementMatchers directly to results
			// Keep `i` a string if there are no elements so `matchedCount` will be "00" below
			for ( ; (elem = elems[i]) != null; i++ ) {
				if ( byElement && elem ) {
					j = 0;
					while ( (matcher = elementMatchers[j++]) ) {
						if ( matcher( elem, context, xml ) ) {
							results.push( elem );
							break;
						}
					}
					if ( outermost ) {
						dirruns = dirrunsUnique;
						cachedruns = ++matcherCachedRuns;
					}
				}

				// Track unmatched elements for set filters
				if ( bySet ) {
					// They will have gone through all possible matchers
					if ( (elem = !matcher && elem) ) {
						matchedCount--;
					}

					// Lengthen the array for every element, matched or not
					if ( seed ) {
						unmatched.push( elem );
					}
				}
			}

			// Apply set filters to unmatched elements
			matchedCount += i;
			if ( bySet && i !== matchedCount ) {
				j = 0;
				while ( (matcher = setMatchers[j++]) ) {
					matcher( unmatched, setMatched, context, xml );
				}

				if ( seed ) {
					// Reintegrate element matches to eliminate the need for sorting
					if ( matchedCount > 0 ) {
						while ( i-- ) {
							if ( !(unmatched[i] || setMatched[i]) ) {
								setMatched[i] = pop.call( results );
							}
						}
					}

					// Discard index placeholder values to get only actual matches
					setMatched = condense( setMatched );
				}

				// Add matches to results
				push.apply( results, setMatched );

				// Seedless set matches succeeding multiple successful matchers stipulate sorting
				if ( outermost && !seed && setMatched.length > 0 &&
					( matchedCount + setMatchers.length ) > 1 ) {

					Sizzle.uniqueSort( results );
				}
			}

			// Override manipulation of globals by nested matchers
			if ( outermost ) {
				dirruns = dirrunsUnique;
				outermostContext = contextBackup;
			}

			return unmatched;
		};

	return bySet ?
		markFunction( superMatcher ) :
		superMatcher;
}

compile = Sizzle.compile = function( selector, group /* Internal Use Only */ ) {
	var i,
		setMatchers = [],
		elementMatchers = [],
		cached = compilerCache[ selector + " " ];

	if ( !cached ) {
		// Generate a function of recursive functions that can be used to check each element
		if ( !group ) {
			group = tokenize( selector );
		}
		i = group.length;
		while ( i-- ) {
			cached = matcherFromTokens( group[i] );
			if ( cached[ expando ] ) {
				setMatchers.push( cached );
			} else {
				elementMatchers.push( cached );
			}
		}

		// Cache the compiled function
		cached = compilerCache( selector, matcherFromGroupMatchers( elementMatchers, setMatchers ) );
	}
	return cached;
};

function multipleContexts( selector, contexts, results ) {
	var i = 0,
		len = contexts.length;
	for ( ; i < len; i++ ) {
		Sizzle( selector, contexts[i], results );
	}
	return results;
}

function select( selector, context, results, seed ) {
	var i, tokens, token, type, find,
		match = tokenize( selector );

	if ( !seed ) {
		// Try to minimize operations if there is only one group
		if ( match.length === 1 ) {

			// Take a shortcut and set the context if the root selector is an ID
			tokens = match[0] = match[0].slice( 0 );
			if ( tokens.length > 2 && (token = tokens[0]).type === "ID" &&
					support.getById && context.nodeType === 9 && documentIsHTML &&
					Expr.relative[ tokens[1].type ] ) {

				context = ( Expr.find["ID"]( token.matches[0].replace(runescape, funescape), context ) || [] )[0];
				if ( !context ) {
					return results;
				}
				selector = selector.slice( tokens.shift().value.length );
			}

			// Fetch a seed set for right-to-left matching
			i = matchExpr["needsContext"].test( selector ) ? 0 : tokens.length;
			while ( i-- ) {
				token = tokens[i];

				// Abort if we hit a combinator
				if ( Expr.relative[ (type = token.type) ] ) {
					break;
				}
				if ( (find = Expr.find[ type ]) ) {
					// Search, expanding context for leading sibling combinators
					if ( (seed = find(
						token.matches[0].replace( runescape, funescape ),
						rsibling.test( tokens[0].type ) && context.parentNode || context
					)) ) {

						// If seed is empty or no tokens remain, we can return early
						tokens.splice( i, 1 );
						selector = seed.length && toSelector( tokens );
						if ( !selector ) {
							push.apply( results, seed );
							return results;
						}

						break;
					}
				}
			}
		}
	}

	// Compile and execute a filtering function
	// Provide `match` to avoid retokenization if we modified the selector above
	compile( selector, match )(
		seed,
		context,
		!documentIsHTML,
		results,
		rsibling.test( selector )
	);
	return results;
}

// One-time assignments

// Sort stability
support.sortStable = expando.split("").sort( sortOrder ).join("") === expando;

// Support: Chrome<14
// Always assume duplicates if they aren't passed to the comparison function
support.detectDuplicates = hasDuplicate;

// Initialize against the default document
setDocument();

// Support: Webkit<537.32 - Safari 6.0.3/Chrome 25 (fixed in Chrome 27)
// Detached nodes confoundingly follow *each other*
support.sortDetached = assert(function( div1 ) {
	// Should return 1, but returns 4 (following)
	return div1.compareDocumentPosition( document.createElement("div") ) & 1;
});

// Support: IE<8
// Prevent attribute/property "interpolation"
// http://msdn.microsoft.com/en-us/library/ms536429%28VS.85%29.aspx
if ( !assert(function( div ) {
	div.innerHTML = "<a href='#'></a>";
	return div.firstChild.getAttribute("href") === "#" ;
}) ) {
	addHandle( "type|href|height|width", function( elem, name, isXML ) {
		if ( !isXML ) {
			return elem.getAttribute( name, name.toLowerCase() === "type" ? 1 : 2 );
		}
	});
}

// Support: IE<9
// Use defaultValue in place of getAttribute("value")
if ( !support.attributes || !assert(function( div ) {
	div.innerHTML = "<input/>";
	div.firstChild.setAttribute( "value", "" );
	return div.firstChild.getAttribute( "value" ) === "";
}) ) {
	addHandle( "value", function( elem, name, isXML ) {
		if ( !isXML && elem.nodeName.toLowerCase() === "input" ) {
			return elem.defaultValue;
		}
	});
}

// Support: IE<9
// Use getAttributeNode to fetch booleans when getAttribute lies
if ( !assert(function( div ) {
	return div.getAttribute("disabled") == null;
}) ) {
	addHandle( booleans, function( elem, name, isXML ) {
		var val;
		if ( !isXML ) {
			return (val = elem.getAttributeNode( name )) && val.specified ?
				val.value :
				elem[ name ] === true ? name.toLowerCase() : null;
		}
	});
}

jQuery.find = Sizzle;
jQuery.expr = Sizzle.selectors;
jQuery.expr[":"] = jQuery.expr.pseudos;
jQuery.unique = Sizzle.uniqueSort;
jQuery.text = Sizzle.getText;
jQuery.isXMLDoc = Sizzle.isXML;
jQuery.contains = Sizzle.contains;


})( window );
// String to Object options format cache
var optionsCache = {};

// Convert String-formatted options into Object-formatted ones and store in cache
function createOptions( options ) {
	var object = optionsCache[ options ] = {};
	jQuery.each( options.match( core_rnotwhite ) || [], function( _, flag ) {
		object[ flag ] = true;
	});
	return object;
}

/*
 * Create a callback list using the following parameters:
 *
 *	options: an optional list of space-separated options that will change how
 *			the callback list behaves or a more traditional option object
 *
 * By default a callback list will act like an event callback list and can be
 * "fired" multiple times.
 *
 * Possible options:
 *
 *	once:			will ensure the callback list can only be fired once (like a Deferred)
 *
 *	memory:			will keep track of previous values and will call any callback added
 *					after the list has been fired right away with the latest "memorized"
 *					values (like a Deferred)
 *
 *	unique:			will ensure a callback can only be added once (no duplicate in the list)
 *
 *	stopOnFalse:	interrupt callings when a callback returns false
 *
 */
jQuery.Callbacks = function( options ) {

	// Convert options from String-formatted to Object-formatted if needed
	// (we check in cache first)
	options = typeof options === "string" ?
		( optionsCache[ options ] || createOptions( options ) ) :
		jQuery.extend( {}, options );

	var // Flag to know if list is currently firing
		firing,
		// Last fire value (for non-forgettable lists)
		memory,
		// Flag to know if list was already fired
		fired,
		// End of the loop when firing
		firingLength,
		// Index of currently firing callback (modified by remove if needed)
		firingIndex,
		// First callback to fire (used internally by add and fireWith)
		firingStart,
		// Actual callback list
		list = [],
		// Stack of fire calls for repeatable lists
		stack = !options.once && [],
		// Fire callbacks
		fire = function( data ) {
			memory = options.memory && data;
			fired = true;
			firingIndex = firingStart || 0;
			firingStart = 0;
			firingLength = list.length;
			firing = true;
			for ( ; list && firingIndex < firingLength; firingIndex++ ) {
				if ( list[ firingIndex ].apply( data[ 0 ], data[ 1 ] ) === false && options.stopOnFalse ) {
					memory = false; // To prevent further calls using add
					break;
				}
			}
			firing = false;
			if ( list ) {
				if ( stack ) {
					if ( stack.length ) {
						fire( stack.shift() );
					}
				} else if ( memory ) {
					list = [];
				} else {
					self.disable();
				}
			}
		},
		// Actual Callbacks object
		self = {
			// Add a callback or a collection of callbacks to the list
			add: function() {
				if ( list ) {
					// First, we save the current length
					var start = list.length;
					(function add( args ) {
						jQuery.each( args, function( _, arg ) {
							var type = jQuery.type( arg );
							if ( type === "function" ) {
								if ( !options.unique || !self.has( arg ) ) {
									list.push( arg );
								}
							} else if ( arg && arg.length && type !== "string" ) {
								// Inspect recursively
								add( arg );
							}
						});
					})( arguments );
					// Do we need to add the callbacks to the
					// current firing batch?
					if ( firing ) {
						firingLength = list.length;
					// With memory, if we're not firing then
					// we should call right away
					} else if ( memory ) {
						firingStart = start;
						fire( memory );
					}
				}
				return this;
			},
			// Remove a callback from the list
			remove: function() {
				if ( list ) {
					jQuery.each( arguments, function( _, arg ) {
						var index;
						while( ( index = jQuery.inArray( arg, list, index ) ) > -1 ) {
							list.splice( index, 1 );
							// Handle firing indexes
							if ( firing ) {
								if ( index <= firingLength ) {
									firingLength--;
								}
								if ( index <= firingIndex ) {
									firingIndex--;
								}
							}
						}
					});
				}
				return this;
			},
			// Check if a given callback is in the list.
			// If no argument is given, return whether or not list has callbacks attached.
			has: function( fn ) {
				return fn ? jQuery.inArray( fn, list ) > -1 : !!( list && list.length );
			},
			// Remove all callbacks from the list
			empty: function() {
				list = [];
				firingLength = 0;
				return this;
			},
			// Have the list do nothing anymore
			disable: function() {
				list = stack = memory = undefined;
				return this;
			},
			// Is it disabled?
			disabled: function() {
				return !list;
			},
			// Lock the list in its current state
			lock: function() {
				stack = undefined;
				if ( !memory ) {
					self.disable();
				}
				return this;
			},
			// Is it locked?
			locked: function() {
				return !stack;
			},
			// Call all callbacks with the given context and arguments
			fireWith: function( context, args ) {
				if ( list && ( !fired || stack ) ) {
					args = args || [];
					args = [ context, args.slice ? args.slice() : args ];
					if ( firing ) {
						stack.push( args );
					} else {
						fire( args );
					}
				}
				return this;
			},
			// Call all the callbacks with the given arguments
			fire: function() {
				self.fireWith( this, arguments );
				return this;
			},
			// To know if the callbacks have already been called at least once
			fired: function() {
				return !!fired;
			}
		};

	return self;
};
jQuery.extend({

	Deferred: function( func ) {
		var tuples = [
				// action, add listener, listener list, final state
				[ "resolve", "done", jQuery.Callbacks("once memory"), "resolved" ],
				[ "reject", "fail", jQuery.Callbacks("once memory"), "rejected" ],
				[ "notify", "progress", jQuery.Callbacks("memory") ]
			],
			state = "pending",
			promise = {
				state: function() {
					return state;
				},
				always: function() {
					deferred.done( arguments ).fail( arguments );
					return this;
				},
				then: function( /* fnDone, fnFail, fnProgress */ ) {
					var fns = arguments;
					return jQuery.Deferred(function( newDefer ) {
						jQuery.each( tuples, function( i, tuple ) {
							var action = tuple[ 0 ],
								fn = jQuery.isFunction( fns[ i ] ) && fns[ i ];
							// deferred[ done | fail | progress ] for forwarding actions to newDefer
							deferred[ tuple[1] ](function() {
								var returned = fn && fn.apply( this, arguments );
								if ( returned && jQuery.isFunction( returned.promise ) ) {
									returned.promise()
										.done( newDefer.resolve )
										.fail( newDefer.reject )
										.progress( newDefer.notify );
								} else {
									newDefer[ action + "With" ]( this === promise ? newDefer.promise() : this, fn ? [ returned ] : arguments );
								}
							});
						});
						fns = null;
					}).promise();
				},
				// Get a promise for this deferred
				// If obj is provided, the promise aspect is added to the object
				promise: function( obj ) {
					return obj != null ? jQuery.extend( obj, promise ) : promise;
				}
			},
			deferred = {};

		// Keep pipe for back-compat
		promise.pipe = promise.then;

		// Add list-specific methods
		jQuery.each( tuples, function( i, tuple ) {
			var list = tuple[ 2 ],
				stateString = tuple[ 3 ];

			// promise[ done | fail | progress ] = list.add
			promise[ tuple[1] ] = list.add;

			// Handle state
			if ( stateString ) {
				list.add(function() {
					// state = [ resolved | rejected ]
					state = stateString;

				// [ reject_list | resolve_list ].disable; progress_list.lock
				}, tuples[ i ^ 1 ][ 2 ].disable, tuples[ 2 ][ 2 ].lock );
			}

			// deferred[ resolve | reject | notify ]
			deferred[ tuple[0] ] = function() {
				deferred[ tuple[0] + "With" ]( this === deferred ? promise : this, arguments );
				return this;
			};
			deferred[ tuple[0] + "With" ] = list.fireWith;
		});

		// Make the deferred a promise
		promise.promise( deferred );

		// Call given func if any
		if ( func ) {
			func.call( deferred, deferred );
		}

		// All done!
		return deferred;
	},

	// Deferred helper
	when: function( subordinate /* , ..., subordinateN */ ) {
		var i = 0,
			resolveValues = core_slice.call( arguments ),
			length = resolveValues.length,

			// the count of uncompleted subordinates
			remaining = length !== 1 || ( subordinate && jQuery.isFunction( subordinate.promise ) ) ? length : 0,

			// the master Deferred. If resolveValues consist of only a single Deferred, just use that.
			deferred = remaining === 1 ? subordinate : jQuery.Deferred(),

			// Update function for both resolve and progress values
			updateFunc = function( i, contexts, values ) {
				return function( value ) {
					contexts[ i ] = this;
					values[ i ] = arguments.length > 1 ? core_slice.call( arguments ) : value;
					if( values === progressValues ) {
						deferred.notifyWith( contexts, values );
					} else if ( !( --remaining ) ) {
						deferred.resolveWith( contexts, values );
					}
				};
			},

			progressValues, progressContexts, resolveContexts;

		// add listeners to Deferred subordinates; treat others as resolved
		if ( length > 1 ) {
			progressValues = new Array( length );
			progressContexts = new Array( length );
			resolveContexts = new Array( length );
			for ( ; i < length; i++ ) {
				if ( resolveValues[ i ] && jQuery.isFunction( resolveValues[ i ].promise ) ) {
					resolveValues[ i ].promise()
						.done( updateFunc( i, resolveContexts, resolveValues ) )
						.fail( deferred.reject )
						.progress( updateFunc( i, progressContexts, progressValues ) );
				} else {
					--remaining;
				}
			}
		}

		// if we're not waiting on anything, resolve the master
		if ( !remaining ) {
			deferred.resolveWith( resolveContexts, resolveValues );
		}

		return deferred.promise();
	}
});
jQuery.support = (function( support ) {

	var all, a, input, select, fragment, opt, eventName, isSupported, i,
		div = document.createElement("div");

	// Setup
	div.setAttribute( "className", "t" );
	div.innerHTML = "  <link/><table></table><a href='/a'>a</a><input type='checkbox'/>";

	// Finish early in limited (non-browser) environments
	all = div.getElementsByTagName("*") || [];
	a = div.getElementsByTagName("a")[ 0 ];
	if ( !a || !a.style || !all.length ) {
		return support;
	}

	// First batch of tests
	select = document.createElement("select");
	opt = select.appendChild( document.createElement("option") );
	input = div.getElementsByTagName("input")[ 0 ];

	a.style.cssText = "top:1px;float:left;opacity:.5";

	// Test setAttribute on camelCase class. If it works, we need attrFixes when doing get/setAttribute (ie6/7)
	support.getSetAttribute = div.className !== "t";

	// IE strips leading whitespace when .innerHTML is used
	support.leadingWhitespace = div.firstChild.nodeType === 3;

	// Make sure that tbody elements aren't automatically inserted
	// IE will insert them into empty tables
	support.tbody = !div.getElementsByTagName("tbody").length;

	// Make sure that link elements get serialized correctly by innerHTML
	// This requires a wrapper element in IE
	support.htmlSerialize = !!div.getElementsByTagName("link").length;

	// Get the style information from getAttribute
	// (IE uses .cssText instead)
	support.style = /top/.test( a.getAttribute("style") );

	// Make sure that URLs aren't manipulated
	// (IE normalizes it by default)
	support.hrefNormalized = a.getAttribute("href") === "/a";

	// Make sure that element opacity exists
	// (IE uses filter instead)
	// Use a regex to work around a WebKit issue. See #5145
	support.opacity = /^0.5/.test( a.style.opacity );

	// Verify style float existence
	// (IE uses styleFloat instead of cssFloat)
	support.cssFloat = !!a.style.cssFloat;

	// Check the default checkbox/radio value ("" on WebKit; "on" elsewhere)
	support.checkOn = !!input.value;

	// Make sure that a selected-by-default option has a working selected property.
	// (WebKit defaults to false instead of true, IE too, if it's in an optgroup)
	support.optSelected = opt.selected;

	// Tests for enctype support on a form (#6743)
	support.enctype = !!document.createElement("form").enctype;

	// Makes sure cloning an html5 element does not cause problems
	// Where outerHTML is undefined, this still works
	support.html5Clone = document.createElement("nav").cloneNode( true ).outerHTML !== "<:nav></:nav>";

	// Will be defined later
	support.inlineBlockNeedsLayout = false;
	support.shrinkWrapBlocks = false;
	support.pixelPosition = false;
	support.deleteExpando = true;
	support.noCloneEvent = true;
	support.reliableMarginRight = true;
	support.boxSizingReliable = true;

	// Make sure checked status is properly cloned
	input.checked = true;
	support.noCloneChecked = input.cloneNode( true ).checked;

	// Make sure that the options inside disabled selects aren't marked as disabled
	// (WebKit marks them as disabled)
	select.disabled = true;
	support.optDisabled = !opt.disabled;

	// Support: IE<9
	try {
		delete div.test;
	} catch( e ) {
		support.deleteExpando = false;
	}

	// Check if we can trust getAttribute("value")
	input = document.createElement("input");
	input.setAttribute( "value", "" );
	support.input = input.getAttribute( "value" ) === "";

	// Check if an input maintains its value after becoming a radio
	input.value = "t";
	input.setAttribute( "type", "radio" );
	support.radioValue = input.value === "t";

	// #11217 - WebKit loses check when the name is after the checked attribute
	input.setAttribute( "checked", "t" );
	input.setAttribute( "name", "t" );

	fragment = document.createDocumentFragment();
	fragment.appendChild( input );

	// Check if a disconnected checkbox will retain its checked
	// value of true after appended to the DOM (IE6/7)
	support.appendChecked = input.checked;

	// WebKit doesn't clone checked state correctly in fragments
	support.checkClone = fragment.cloneNode( true ).cloneNode( true ).lastChild.checked;

	// Support: IE<9
	// Opera does not clone events (and typeof div.attachEvent === undefined).
	// IE9-10 clones events bound via attachEvent, but they don't trigger with .click()
	if ( div.attachEvent ) {
		div.attachEvent( "onclick", function() {
			support.noCloneEvent = false;
		});

		div.cloneNode( true ).click();
	}

	// Support: IE<9 (lack submit/change bubble), Firefox 17+ (lack focusin event)
	// Beware of CSP restrictions (https://developer.mozilla.org/en/Security/CSP)
	for ( i in { submit: true, change: true, focusin: true }) {
		div.setAttribute( eventName = "on" + i, "t" );

		support[ i + "Bubbles" ] = eventName in window || div.attributes[ eventName ].expando === false;
	}

	div.style.backgroundClip = "content-box";
	div.cloneNode( true ).style.backgroundClip = "";
	support.clearCloneStyle = div.style.backgroundClip === "content-box";

	// Support: IE<9
	// Iteration over object's inherited properties before its own.
	for ( i in jQuery( support ) ) {
		break;
	}
	support.ownLast = i !== "0";

	// Run tests that need a body at doc ready
	jQuery(function() {
		var container, marginDiv, tds,
			divReset = "padding:0;margin:0;border:0;display:block;box-sizing:content-box;-moz-box-sizing:content-box;-webkit-box-sizing:content-box;",
			body = document.getElementsByTagName("body")[0];

		if ( !body ) {
			// Return for frameset docs that don't have a body
			return;
		}

		container = document.createElement("div");
		container.style.cssText = "border:0;width:0;height:0;position:absolute;top:0;left:-9999px;margin-top:1px";

		body.appendChild( container ).appendChild( div );

		// Support: IE8
		// Check if table cells still have offsetWidth/Height when they are set
		// to display:none and there are still other visible table cells in a
		// table row; if so, offsetWidth/Height are not reliable for use when
		// determining if an element has been hidden directly using
		// display:none (it is still safe to use offsets if a parent element is
		// hidden; don safety goggles and see bug #4512 for more information).
		div.innerHTML = "<table><tr><td></td><td>t</td></tr></table>";
		tds = div.getElementsByTagName("td");
		tds[ 0 ].style.cssText = "padding:0;margin:0;border:0;display:none";
		isSupported = ( tds[ 0 ].offsetHeight === 0 );

		tds[ 0 ].style.display = "";
		tds[ 1 ].style.display = "none";

		// Support: IE8
		// Check if empty table cells still have offsetWidth/Height
		support.reliableHiddenOffsets = isSupported && ( tds[ 0 ].offsetHeight === 0 );

		// Check box-sizing and margin behavior.
		div.innerHTML = "";
		div.style.cssText = "box-sizing:border-box;-moz-box-sizing:border-box;-webkit-box-sizing:border-box;padding:1px;border:1px;display:block;width:4px;margin-top:1%;position:absolute;top:1%;";

		// Workaround failing boxSizing test due to offsetWidth returning wrong value
		// with some non-1 values of body zoom, ticket #13543
		jQuery.swap( body, body.style.zoom != null ? { zoom: 1 } : {}, function() {
			support.boxSizing = div.offsetWidth === 4;
		});

		// Use window.getComputedStyle because jsdom on node.js will break without it.
		if ( window.getComputedStyle ) {
			support.pixelPosition = ( window.getComputedStyle( div, null ) || {} ).top !== "1%";
			support.boxSizingReliable = ( window.getComputedStyle( div, null ) || { width: "4px" } ).width === "4px";

			// Check if div with explicit width and no margin-right incorrectly
			// gets computed margin-right based on width of container. (#3333)
			// Fails in WebKit before Feb 2011 nightlies
			// WebKit Bug 13343 - getComputedStyle returns wrong value for margin-right
			marginDiv = div.appendChild( document.createElement("div") );
			marginDiv.style.cssText = div.style.cssText = divReset;
			marginDiv.style.marginRight = marginDiv.style.width = "0";
			div.style.width = "1px";

			support.reliableMarginRight =
				!parseFloat( ( window.getComputedStyle( marginDiv, null ) || {} ).marginRight );
		}

		if ( typeof div.style.zoom !== core_strundefined ) {
			// Support: IE<8
			// Check if natively block-level elements act like inline-block
			// elements when setting their display to 'inline' and giving
			// them layout
			div.innerHTML = "";
			div.style.cssText = divReset + "width:1px;padding:1px;display:inline;zoom:1";
			support.inlineBlockNeedsLayout = ( div.offsetWidth === 3 );

			// Support: IE6
			// Check if elements with layout shrink-wrap their children
			div.style.display = "block";
			div.innerHTML = "<div></div>";
			div.firstChild.style.width = "5px";
			support.shrinkWrapBlocks = ( div.offsetWidth !== 3 );

			if ( support.inlineBlockNeedsLayout ) {
				// Prevent IE 6 from affecting layout for positioned elements #11048
				// Prevent IE from shrinking the body in IE 7 mode #12869
				// Support: IE<8
				body.style.zoom = 1;
			}
		}

		body.removeChild( container );

		// Null elements to avoid leaks in IE
		container = div = tds = marginDiv = null;
	});

	// Null elements to avoid leaks in IE
	all = select = fragment = opt = a = input = null;

	return support;
})({});

var rbrace = /(?:\{[\s\S]*\}|\[[\s\S]*\])$/,
	rmultiDash = /([A-Z])/g;

function internalData( elem, name, data, pvt /* Internal Use Only */ ){
	if ( !jQuery.acceptData( elem ) ) {
		return;
	}

	var ret, thisCache,
		internalKey = jQuery.expando,

		// We have to handle DOM nodes and JS objects differently because IE6-7
		// can't GC object references properly across the DOM-JS boundary
		isNode = elem.nodeType,

		// Only DOM nodes need the global jQuery cache; JS object data is
		// attached directly to the object so GC can occur automatically
		cache = isNode ? jQuery.cache : elem,

		// Only defining an ID for JS objects if its cache already exists allows
		// the code to shortcut on the same path as a DOM node with no cache
		id = isNode ? elem[ internalKey ] : elem[ internalKey ] && internalKey;

	// Avoid doing any more work than we need to when trying to get data on an
	// object that has no data at all
	if ( (!id || !cache[id] || (!pvt && !cache[id].data)) && data === undefined && typeof name === "string" ) {
		return;
	}

	if ( !id ) {
		// Only DOM nodes need a new unique ID for each element since their data
		// ends up in the global cache
		if ( isNode ) {
			id = elem[ internalKey ] = core_deletedIds.pop() || jQuery.guid++;
		} else {
			id = internalKey;
		}
	}

	if ( !cache[ id ] ) {
		// Avoid exposing jQuery metadata on plain JS objects when the object
		// is serialized using JSON.stringify
		cache[ id ] = isNode ? {} : { toJSON: jQuery.noop };
	}

	// An object can be passed to jQuery.data instead of a key/value pair; this gets
	// shallow copied over onto the existing cache
	if ( typeof name === "object" || typeof name === "function" ) {
		if ( pvt ) {
			cache[ id ] = jQuery.extend( cache[ id ], name );
		} else {
			cache[ id ].data = jQuery.extend( cache[ id ].data, name );
		}
	}

	thisCache = cache[ id ];

	// jQuery data() is stored in a separate object inside the object's internal data
	// cache in order to avoid key collisions between internal data and user-defined
	// data.
	if ( !pvt ) {
		if ( !thisCache.data ) {
			thisCache.data = {};
		}

		thisCache = thisCache.data;
	}

	if ( data !== undefined ) {
		thisCache[ jQuery.camelCase( name ) ] = data;
	}

	// Check for both converted-to-camel and non-converted data property names
	// If a data property was specified
	if ( typeof name === "string" ) {

		// First Try to find as-is property data
		ret = thisCache[ name ];

		// Test for null|undefined property data
		if ( ret == null ) {

			// Try to find the camelCased property
			ret = thisCache[ jQuery.camelCase( name ) ];
		}
	} else {
		ret = thisCache;
	}

	return ret;
}

function internalRemoveData( elem, name, pvt ) {
	if ( !jQuery.acceptData( elem ) ) {
		return;
	}

	var thisCache, i,
		isNode = elem.nodeType,

		// See jQuery.data for more information
		cache = isNode ? jQuery.cache : elem,
		id = isNode ? elem[ jQuery.expando ] : jQuery.expando;

	// If there is already no cache entry for this object, there is no
	// purpose in continuing
	if ( !cache[ id ] ) {
		return;
	}

	if ( name ) {

		thisCache = pvt ? cache[ id ] : cache[ id ].data;

		if ( thisCache ) {

			// Support array or space separated string names for data keys
			if ( !jQuery.isArray( name ) ) {

				// try the string as a key before any manipulation
				if ( name in thisCache ) {
					name = [ name ];
				} else {

					// split the camel cased version by spaces unless a key with the spaces exists
					name = jQuery.camelCase( name );
					if ( name in thisCache ) {
						name = [ name ];
					} else {
						name = name.split(" ");
					}
				}
			} else {
				// If "name" is an array of keys...
				// When data is initially created, via ("key", "val") signature,
				// keys will be converted to camelCase.
				// Since there is no way to tell _how_ a key was added, remove
				// both plain key and camelCase key. #12786
				// This will only penalize the array argument path.
				name = name.concat( jQuery.map( name, jQuery.camelCase ) );
			}

			i = name.length;
			while ( i-- ) {
				delete thisCache[ name[i] ];
			}

			// If there is no data left in the cache, we want to continue
			// and let the cache object itself get destroyed
			if ( pvt ? !isEmptyDataObject(thisCache) : !jQuery.isEmptyObject(thisCache) ) {
				return;
			}
		}
	}

	// See jQuery.data for more information
	if ( !pvt ) {
		delete cache[ id ].data;

		// Don't destroy the parent cache unless the internal data object
		// had been the only thing left in it
		if ( !isEmptyDataObject( cache[ id ] ) ) {
			return;
		}
	}

	// Destroy the cache
	if ( isNode ) {
		jQuery.cleanData( [ elem ], true );

	// Use delete when supported for expandos or `cache` is not a window per isWindow (#10080)
	/* jshint eqeqeq: false */
	} else if ( jQuery.support.deleteExpando || cache != cache.window ) {
		/* jshint eqeqeq: true */
		delete cache[ id ];

	// When all else fails, null
	} else {
		cache[ id ] = null;
	}
}

jQuery.extend({
	cache: {},

	// The following elements throw uncatchable exceptions if you
	// attempt to add expando properties to them.
	noData: {
		"applet": true,
		"embed": true,
		// Ban all objects except for Flash (which handle expandos)
		"object": "clsid:D27CDB6E-AE6D-11cf-96B8-444553540000"
	},

	hasData: function( elem ) {
		elem = elem.nodeType ? jQuery.cache[ elem[jQuery.expando] ] : elem[ jQuery.expando ];
		return !!elem && !isEmptyDataObject( elem );
	},

	data: function( elem, name, data ) {
		return internalData( elem, name, data );
	},

	removeData: function( elem, name ) {
		return internalRemoveData( elem, name );
	},

	// For internal use only.
	_data: function( elem, name, data ) {
		return internalData( elem, name, data, true );
	},

	_removeData: function( elem, name ) {
		return internalRemoveData( elem, name, true );
	},

	// A method for determining if a DOM node can handle the data expando
	acceptData: function( elem ) {
		// Do not set data on non-element because it will not be cleared (#8335).
		if ( elem.nodeType && elem.nodeType !== 1 && elem.nodeType !== 9 ) {
			return false;
		}

		var noData = elem.nodeName && jQuery.noData[ elem.nodeName.toLowerCase() ];

		// nodes accept data unless otherwise specified; rejection can be conditional
		return !noData || noData !== true && elem.getAttribute("classid") === noData;
	}
});

jQuery.fn.extend({
	data: function( key, value ) {
		var attrs, name,
			data = null,
			i = 0,
			elem = this[0];

		// Special expections of .data basically thwart jQuery.access,
		// so implement the relevant behavior ourselves

		// Gets all values
		if ( key === undefined ) {
			if ( this.length ) {
				data = jQuery.data( elem );

				if ( elem.nodeType === 1 && !jQuery._data( elem, "parsedAttrs" ) ) {
					attrs = elem.attributes;
					for ( ; i < attrs.length; i++ ) {
						name = attrs[i].name;

						if ( name.indexOf("data-") === 0 ) {
							name = jQuery.camelCase( name.slice(5) );

							dataAttr( elem, name, data[ name ] );
						}
					}
					jQuery._data( elem, "parsedAttrs", true );
				}
			}

			return data;
		}

		// Sets multiple values
		if ( typeof key === "object" ) {
			return this.each(function() {
				jQuery.data( this, key );
			});
		}

		return arguments.length > 1 ?

			// Sets one value
			this.each(function() {
				jQuery.data( this, key, value );
			}) :

			// Gets one value
			// Try to fetch any internally stored data first
			elem ? dataAttr( elem, key, jQuery.data( elem, key ) ) : null;
	},

	removeData: function( key ) {
		return this.each(function() {
			jQuery.removeData( this, key );
		});
	}
});

function dataAttr( elem, key, data ) {
	// If nothing was found internally, try to fetch any
	// data from the HTML5 data-* attribute
	if ( data === undefined && elem.nodeType === 1 ) {

		var name = "data-" + key.replace( rmultiDash, "-$1" ).toLowerCase();

		data = elem.getAttribute( name );

		if ( typeof data === "string" ) {
			try {
				data = data === "true" ? true :
					data === "false" ? false :
					data === "null" ? null :
					// Only convert to a number if it doesn't change the string
					+data + "" === data ? +data :
					rbrace.test( data ) ? jQuery.parseJSON( data ) :
						data;
			} catch( e ) {}

			// Make sure we set the data so it isn't changed later
			jQuery.data( elem, key, data );

		} else {
			data = undefined;
		}
	}

	return data;
}

// checks a cache object for emptiness
function isEmptyDataObject( obj ) {
	var name;
	for ( name in obj ) {

		// if the public data object is empty, the private is still empty
		if ( name === "data" && jQuery.isEmptyObject( obj[name] ) ) {
			continue;
		}
		if ( name !== "toJSON" ) {
			return false;
		}
	}

	return true;
}
jQuery.extend({
	queue: function( elem, type, data ) {
		var queue;

		if ( elem ) {
			type = ( type || "fx" ) + "queue";
			queue = jQuery._data( elem, type );

			// Speed up dequeue by getting out quickly if this is just a lookup
			if ( data ) {
				if ( !queue || jQuery.isArray(data) ) {
					queue = jQuery._data( elem, type, jQuery.makeArray(data) );
				} else {
					queue.push( data );
				}
			}
			return queue || [];
		}
	},

	dequeue: function( elem, type ) {
		type = type || "fx";

		var queue = jQuery.queue( elem, type ),
			startLength = queue.length,
			fn = queue.shift(),
			hooks = jQuery._queueHooks( elem, type ),
			next = function() {
				jQuery.dequeue( elem, type );
			};

		// If the fx queue is dequeued, always remove the progress sentinel
		if ( fn === "inprogress" ) {
			fn = queue.shift();
			startLength--;
		}

		if ( fn ) {

			// Add a progress sentinel to prevent the fx queue from being
			// automatically dequeued
			if ( type === "fx" ) {
				queue.unshift( "inprogress" );
			}

			// clear up the last queue stop function
			delete hooks.stop;
			fn.call( elem, next, hooks );
		}

		if ( !startLength && hooks ) {
			hooks.empty.fire();
		}
	},

	// not intended for public consumption - generates a queueHooks object, or returns the current one
	_queueHooks: function( elem, type ) {
		var key = type + "queueHooks";
		return jQuery._data( elem, key ) || jQuery._data( elem, key, {
			empty: jQuery.Callbacks("once memory").add(function() {
				jQuery._removeData( elem, type + "queue" );
				jQuery._removeData( elem, key );
			})
		});
	}
});

jQuery.fn.extend({
	queue: function( type, data ) {
		var setter = 2;

		if ( typeof type !== "string" ) {
			data = type;
			type = "fx";
			setter--;
		}

		if ( arguments.length < setter ) {
			return jQuery.queue( this[0], type );
		}

		return data === undefined ?
			this :
			this.each(function() {
				var queue = jQuery.queue( this, type, data );

				// ensure a hooks for this queue
				jQuery._queueHooks( this, type );

				if ( type === "fx" && queue[0] !== "inprogress" ) {
					jQuery.dequeue( this, type );
				}
			});
	},
	dequeue: function( type ) {
		return this.each(function() {
			jQuery.dequeue( this, type );
		});
	},
	// Based off of the plugin by Clint Helfers, with permission.
	// http://blindsignals.com/index.php/2009/07/jquery-delay/
	delay: function( time, type ) {
		time = jQuery.fx ? jQuery.fx.speeds[ time ] || time : time;
		type = type || "fx";

		return this.queue( type, function( next, hooks ) {
			var timeout = setTimeout( next, time );
			hooks.stop = function() {
				clearTimeout( timeout );
			};
		});
	},
	clearQueue: function( type ) {
		return this.queue( type || "fx", [] );
	},
	// Get a promise resolved when queues of a certain type
	// are emptied (fx is the type by default)
	promise: function( type, obj ) {
		var tmp,
			count = 1,
			defer = jQuery.Deferred(),
			elements = this,
			i = this.length,
			resolve = function() {
				if ( !( --count ) ) {
					defer.resolveWith( elements, [ elements ] );
				}
			};

		if ( typeof type !== "string" ) {
			obj = type;
			type = undefined;
		}
		type = type || "fx";

		while( i-- ) {
			tmp = jQuery._data( elements[ i ], type + "queueHooks" );
			if ( tmp && tmp.empty ) {
				count++;
				tmp.empty.add( resolve );
			}
		}
		resolve();
		return defer.promise( obj );
	}
});
var nodeHook, boolHook,
	rclass = /[\t\r\n\f]/g,
	rreturn = /\r/g,
	rfocusable = /^(?:input|select|textarea|button|object)$/i,
	rclickable = /^(?:a|area)$/i,
	ruseDefault = /^(?:checked|selected)$/i,
	getSetAttribute = jQuery.support.getSetAttribute,
	getSetInput = jQuery.support.input;

jQuery.fn.extend({
	attr: function( name, value ) {
		return jQuery.access( this, jQuery.attr, name, value, arguments.length > 1 );
	},

	removeAttr: function( name ) {
		return this.each(function() {
			jQuery.removeAttr( this, name );
		});
	},

	prop: function( name, value ) {
		return jQuery.access( this, jQuery.prop, name, value, arguments.length > 1 );
	},

	removeProp: function( name ) {
		name = jQuery.propFix[ name ] || name;
		return this.each(function() {
			// try/catch handles cases where IE balks (such as removing a property on window)
			try {
				this[ name ] = undefined;
				delete this[ name ];
			} catch( e ) {}
		});
	},

	addClass: function( value ) {
		var classes, elem, cur, clazz, j,
			i = 0,
			len = this.length,
			proceed = typeof value === "string" && value;

		if ( jQuery.isFunction( value ) ) {
			return this.each(function( j ) {
				jQuery( this ).addClass( value.call( this, j, this.className ) );
			});
		}

		if ( proceed ) {
			// The disjunction here is for better compressibility (see removeClass)
			classes = ( value || "" ).match( core_rnotwhite ) || [];

			for ( ; i < len; i++ ) {
				elem = this[ i ];
				cur = elem.nodeType === 1 && ( elem.className ?
					( " " + elem.className + " " ).replace( rclass, " " ) :
					" "
				);

				if ( cur ) {
					j = 0;
					while ( (clazz = classes[j++]) ) {
						if ( cur.indexOf( " " + clazz + " " ) < 0 ) {
							cur += clazz + " ";
						}
					}
					elem.className = jQuery.trim( cur );

				}
			}
		}

		return this;
	},

	removeClass: function( value ) {
		var classes, elem, cur, clazz, j,
			i = 0,
			len = this.length,
			proceed = arguments.length === 0 || typeof value === "string" && value;

		if ( jQuery.isFunction( value ) ) {
			return this.each(function( j ) {
				jQuery( this ).removeClass( value.call( this, j, this.className ) );
			});
		}
		if ( proceed ) {
			classes = ( value || "" ).match( core_rnotwhite ) || [];

			for ( ; i < len; i++ ) {
				elem = this[ i ];
				// This expression is here for better compressibility (see addClass)
				cur = elem.nodeType === 1 && ( elem.className ?
					( " " + elem.className + " " ).replace( rclass, " " ) :
					""
				);

				if ( cur ) {
					j = 0;
					while ( (clazz = classes[j++]) ) {
						// Remove *all* instances
						while ( cur.indexOf( " " + clazz + " " ) >= 0 ) {
							cur = cur.replace( " " + clazz + " ", " " );
						}
					}
					elem.className = value ? jQuery.trim( cur ) : "";
				}
			}
		}

		return this;
	},

	toggleClass: function( value, stateVal ) {
		var type = typeof value;

		if ( typeof stateVal === "boolean" && type === "string" ) {
			return stateVal ? this.addClass( value ) : this.removeClass( value );
		}

		if ( jQuery.isFunction( value ) ) {
			return this.each(function( i ) {
				jQuery( this ).toggleClass( value.call(this, i, this.className, stateVal), stateVal );
			});
		}

		return this.each(function() {
			if ( type === "string" ) {
				// toggle individual class names
				var className,
					i = 0,
					self = jQuery( this ),
					classNames = value.match( core_rnotwhite ) || [];

				while ( (className = classNames[ i++ ]) ) {
					// check each className given, space separated list
					if ( self.hasClass( className ) ) {
						self.removeClass( className );
					} else {
						self.addClass( className );
					}
				}

			// Toggle whole class name
			} else if ( type === core_strundefined || type === "boolean" ) {
				if ( this.className ) {
					// store className if set
					jQuery._data( this, "__className__", this.className );
				}

				// If the element has a class name or if we're passed "false",
				// then remove the whole classname (if there was one, the above saved it).
				// Otherwise bring back whatever was previously saved (if anything),
				// falling back to the empty string if nothing was stored.
				this.className = this.className || value === false ? "" : jQuery._data( this, "__className__" ) || "";
			}
		});
	},

	hasClass: function( selector ) {
		var className = " " + selector + " ",
			i = 0,
			l = this.length;
		for ( ; i < l; i++ ) {
			if ( this[i].nodeType === 1 && (" " + this[i].className + " ").replace(rclass, " ").indexOf( className ) >= 0 ) {
				return true;
			}
		}

		return false;
	},

	val: function( value ) {
		var ret, hooks, isFunction,
			elem = this[0];

		if ( !arguments.length ) {
			if ( elem ) {
				hooks = jQuery.valHooks[ elem.type ] || jQuery.valHooks[ elem.nodeName.toLowerCase() ];

				if ( hooks && "get" in hooks && (ret = hooks.get( elem, "value" )) !== undefined ) {
					return ret;
				}

				ret = elem.value;

				return typeof ret === "string" ?
					// handle most common string cases
					ret.replace(rreturn, "") :
					// handle cases where value is null/undef or number
					ret == null ? "" : ret;
			}

			return;
		}

		isFunction = jQuery.isFunction( value );

		return this.each(function( i ) {
			var val;

			if ( this.nodeType !== 1 ) {
				return;
			}

			if ( isFunction ) {
				val = value.call( this, i, jQuery( this ).val() );
			} else {
				val = value;
			}

			// Treat null/undefined as ""; convert numbers to string
			if ( val == null ) {
				val = "";
			} else if ( typeof val === "number" ) {
				val += "";
			} else if ( jQuery.isArray( val ) ) {
				val = jQuery.map(val, function ( value ) {
					return value == null ? "" : value + "";
				});
			}

			hooks = jQuery.valHooks[ this.type ] || jQuery.valHooks[ this.nodeName.toLowerCase() ];

			// If set returns undefined, fall back to normal setting
			if ( !hooks || !("set" in hooks) || hooks.set( this, val, "value" ) === undefined ) {
				this.value = val;
			}
		});
	}
});

jQuery.extend({
	valHooks: {
		option: {
			get: function( elem ) {
				// Use proper attribute retrieval(#6932, #12072)
				var val = jQuery.find.attr( elem, "value" );
				return val != null ?
					val :
					elem.text;
			}
		},
		select: {
			get: function( elem ) {
				var value, option,
					options = elem.options,
					index = elem.selectedIndex,
					one = elem.type === "select-one" || index < 0,
					values = one ? null : [],
					max = one ? index + 1 : options.length,
					i = index < 0 ?
						max :
						one ? index : 0;

				// Loop through all the selected options
				for ( ; i < max; i++ ) {
					option = options[ i ];

					// oldIE doesn't update selected after form reset (#2551)
					if ( ( option.selected || i === index ) &&
							// Don't return options that are disabled or in a disabled optgroup
							( jQuery.support.optDisabled ? !option.disabled : option.getAttribute("disabled") === null ) &&
							( !option.parentNode.disabled || !jQuery.nodeName( option.parentNode, "optgroup" ) ) ) {

						// Get the specific value for the option
						value = jQuery( option ).val();

						// We don't need an array for one selects
						if ( one ) {
							return value;
						}

						// Multi-Selects return an array
						values.push( value );
					}
				}

				return values;
			},

			set: function( elem, value ) {
				var optionSet, option,
					options = elem.options,
					values = jQuery.makeArray( value ),
					i = options.length;

				while ( i-- ) {
					option = options[ i ];
					if ( (option.selected = jQuery.inArray( jQuery(option).val(), values ) >= 0) ) {
						optionSet = true;
					}
				}

				// force browsers to behave consistently when non-matching value is set
				if ( !optionSet ) {
					elem.selectedIndex = -1;
				}
				return values;
			}
		}
	},

	attr: function( elem, name, value ) {
		var hooks, ret,
			nType = elem.nodeType;

		// don't get/set attributes on text, comment and attribute nodes
		if ( !elem || nType === 3 || nType === 8 || nType === 2 ) {
			return;
		}

		// Fallback to prop when attributes are not supported
		if ( typeof elem.getAttribute === core_strundefined ) {
			return jQuery.prop( elem, name, value );
		}

		// All attributes are lowercase
		// Grab necessary hook if one is defined
		if ( nType !== 1 || !jQuery.isXMLDoc( elem ) ) {
			name = name.toLowerCase();
			hooks = jQuery.attrHooks[ name ] ||
				( jQuery.expr.match.bool.test( name ) ? boolHook : nodeHook );
		}

		if ( value !== undefined ) {

			if ( value === null ) {
				jQuery.removeAttr( elem, name );

			} else if ( hooks && "set" in hooks && (ret = hooks.set( elem, value, name )) !== undefined ) {
				return ret;

			} else {
				elem.setAttribute( name, value + "" );
				return value;
			}

		} else if ( hooks && "get" in hooks && (ret = hooks.get( elem, name )) !== null ) {
			return ret;

		} else {
			ret = jQuery.find.attr( elem, name );

			// Non-existent attributes return null, we normalize to undefined
			return ret == null ?
				undefined :
				ret;
		}
	},

	removeAttr: function( elem, value ) {
		var name, propName,
			i = 0,
			attrNames = value && value.match( core_rnotwhite );

		if ( attrNames && elem.nodeType === 1 ) {
			while ( (name = attrNames[i++]) ) {
				propName = jQuery.propFix[ name ] || name;

				// Boolean attributes get special treatment (#10870)
				if ( jQuery.expr.match.bool.test( name ) ) {
					// Set corresponding property to false
					if ( getSetInput && getSetAttribute || !ruseDefault.test( name ) ) {
						elem[ propName ] = false;
					// Support: IE<9
					// Also clear defaultChecked/defaultSelected (if appropriate)
					} else {
						elem[ jQuery.camelCase( "default-" + name ) ] =
							elem[ propName ] = false;
					}

				// See #9699 for explanation of this approach (setting first, then removal)
				} else {
					jQuery.attr( elem, name, "" );
				}

				elem.removeAttribute( getSetAttribute ? name : propName );
			}
		}
	},

	attrHooks: {
		type: {
			set: function( elem, value ) {
				if ( !jQuery.support.radioValue && value === "radio" && jQuery.nodeName(elem, "input") ) {
					// Setting the type on a radio button after the value resets the value in IE6-9
					// Reset value to default in case type is set after value during creation
					var val = elem.value;
					elem.setAttribute( "type", value );
					if ( val ) {
						elem.value = val;
					}
					return value;
				}
			}
		}
	},

	propFix: {
		"for": "htmlFor",
		"class": "className"
	},

	prop: function( elem, name, value ) {
		var ret, hooks, notxml,
			nType = elem.nodeType;

		// don't get/set properties on text, comment and attribute nodes
		if ( !elem || nType === 3 || nType === 8 || nType === 2 ) {
			return;
		}

		notxml = nType !== 1 || !jQuery.isXMLDoc( elem );

		if ( notxml ) {
			// Fix name and attach hooks
			name = jQuery.propFix[ name ] || name;
			hooks = jQuery.propHooks[ name ];
		}

		if ( value !== undefined ) {
			return hooks && "set" in hooks && (ret = hooks.set( elem, value, name )) !== undefined ?
				ret :
				( elem[ name ] = value );

		} else {
			return hooks && "get" in hooks && (ret = hooks.get( elem, name )) !== null ?
				ret :
				elem[ name ];
		}
	},

	propHooks: {
		tabIndex: {
			get: function( elem ) {
				// elem.tabIndex doesn't always return the correct value when it hasn't been explicitly set
				// http://fluidproject.org/blog/2008/01/09/getting-setting-and-removing-tabindex-values-with-javascript/
				// Use proper attribute retrieval(#12072)
				var tabindex = jQuery.find.attr( elem, "tabindex" );

				return tabindex ?
					parseInt( tabindex, 10 ) :
					rfocusable.test( elem.nodeName ) || rclickable.test( elem.nodeName ) && elem.href ?
						0 :
						-1;
			}
		}
	}
});

// Hooks for boolean attributes
boolHook = {
	set: function( elem, value, name ) {
		if ( value === false ) {
			// Remove boolean attributes when set to false
			jQuery.removeAttr( elem, name );
		} else if ( getSetInput && getSetAttribute || !ruseDefault.test( name ) ) {
			// IE<8 needs the *property* name
			elem.setAttribute( !getSetAttribute && jQuery.propFix[ name ] || name, name );

		// Use defaultChecked and defaultSelected for oldIE
		} else {
			elem[ jQuery.camelCase( "default-" + name ) ] = elem[ name ] = true;
		}

		return name;
	}
};
jQuery.each( jQuery.expr.match.bool.source.match( /\w+/g ), function( i, name ) {
	var getter = jQuery.expr.attrHandle[ name ] || jQuery.find.attr;

	jQuery.expr.attrHandle[ name ] = getSetInput && getSetAttribute || !ruseDefault.test( name ) ?
		function( elem, name, isXML ) {
			var fn = jQuery.expr.attrHandle[ name ],
				ret = isXML ?
					undefined :
					/* jshint eqeqeq: false */
					(jQuery.expr.attrHandle[ name ] = undefined) !=
						getter( elem, name, isXML ) ?

						name.toLowerCase() :
						null;
			jQuery.expr.attrHandle[ name ] = fn;
			return ret;
		} :
		function( elem, name, isXML ) {
			return isXML ?
				undefined :
				elem[ jQuery.camelCase( "default-" + name ) ] ?
					name.toLowerCase() :
					null;
		};
});

// fix oldIE attroperties
if ( !getSetInput || !getSetAttribute ) {
	jQuery.attrHooks.value = {
		set: function( elem, value, name ) {
			if ( jQuery.nodeName( elem, "input" ) ) {
				// Does not return so that setAttribute is also used
				elem.defaultValue = value;
			} else {
				// Use nodeHook if defined (#1954); otherwise setAttribute is fine
				return nodeHook && nodeHook.set( elem, value, name );
			}
		}
	};
}

// IE6/7 do not support getting/setting some attributes with get/setAttribute
if ( !getSetAttribute ) {

	// Use this for any attribute in IE6/7
	// This fixes almost every IE6/7 issue
	nodeHook = {
		set: function( elem, value, name ) {
			// Set the existing or create a new attribute node
			var ret = elem.getAttributeNode( name );
			if ( !ret ) {
				elem.setAttributeNode(
					(ret = elem.ownerDocument.createAttribute( name ))
				);
			}

			ret.value = value += "";

			// Break association with cloned elements by also using setAttribute (#9646)
			return name === "value" || value === elem.getAttribute( name ) ?
				value :
				undefined;
		}
	};
	jQuery.expr.attrHandle.id = jQuery.expr.attrHandle.name = jQuery.expr.attrHandle.coords =
		// Some attributes are constructed with empty-string values when not defined
		function( elem, name, isXML ) {
			var ret;
			return isXML ?
				undefined :
				(ret = elem.getAttributeNode( name )) && ret.value !== "" ?
					ret.value :
					null;
		};
	jQuery.valHooks.button = {
		get: function( elem, name ) {
			var ret = elem.getAttributeNode( name );
			return ret && ret.specified ?
				ret.value :
				undefined;
		},
		set: nodeHook.set
	};

	// Set contenteditable to false on removals(#10429)
	// Setting to empty string throws an error as an invalid value
	jQuery.attrHooks.contenteditable = {
		set: function( elem, value, name ) {
			nodeHook.set( elem, value === "" ? false : value, name );
		}
	};

	// Set width and height to auto instead of 0 on empty string( Bug #8150 )
	// This is for removals
	jQuery.each([ "width", "height" ], function( i, name ) {
		jQuery.attrHooks[ name ] = {
			set: function( elem, value ) {
				if ( value === "" ) {
					elem.setAttribute( name, "auto" );
					return value;
				}
			}
		};
	});
}


// Some attributes require a special call on IE
// http://msdn.microsoft.com/en-us/library/ms536429%28VS.85%29.aspx
if ( !jQuery.support.hrefNormalized ) {
	// href/src property should get the full normalized URL (#10299/#12915)
	jQuery.each([ "href", "src" ], function( i, name ) {
		jQuery.propHooks[ name ] = {
			get: function( elem ) {
				return elem.getAttribute( name, 4 );
			}
		};
	});
}

if ( !jQuery.support.style ) {
	jQuery.attrHooks.style = {
		get: function( elem ) {
			// Return undefined in the case of empty string
			// Note: IE uppercases css property names, but if we were to .toLowerCase()
			// .cssText, that would destroy case senstitivity in URL's, like in "background"
			return elem.style.cssText || undefined;
		},
		set: function( elem, value ) {
			return ( elem.style.cssText = value + "" );
		}
	};
}

// Safari mis-reports the default selected property of an option
// Accessing the parent's selectedIndex property fixes it
if ( !jQuery.support.optSelected ) {
	jQuery.propHooks.selected = {
		get: function( elem ) {
			var parent = elem.parentNode;

			if ( parent ) {
				parent.selectedIndex;

				// Make sure that it also works with optgroups, see #5701
				if ( parent.parentNode ) {
					parent.parentNode.selectedIndex;
				}
			}
			return null;
		}
	};
}

jQuery.each([
	"tabIndex",
	"readOnly",
	"maxLength",
	"cellSpacing",
	"cellPadding",
	"rowSpan",
	"colSpan",
	"useMap",
	"frameBorder",
	"contentEditable"
], function() {
	jQuery.propFix[ this.toLowerCase() ] = this;
});

// IE6/7 call enctype encoding
if ( !jQuery.support.enctype ) {
	jQuery.propFix.enctype = "encoding";
}

// Radios and checkboxes getter/setter
jQuery.each([ "radio", "checkbox" ], function() {
	jQuery.valHooks[ this ] = {
		set: function( elem, value ) {
			if ( jQuery.isArray( value ) ) {
				return ( elem.checked = jQuery.inArray( jQuery(elem).val(), value ) >= 0 );
			}
		}
	};
	if ( !jQuery.support.checkOn ) {
		jQuery.valHooks[ this ].get = function( elem ) {
			// Support: Webkit
			// "" is returned instead of "on" if a value isn't specified
			return elem.getAttribute("value") === null ? "on" : elem.value;
		};
	}
});
var rformElems = /^(?:input|select|textarea)$/i,
	rkeyEvent = /^key/,
	rmouseEvent = /^(?:mouse|contextmenu)|click/,
	rfocusMorph = /^(?:focusinfocus|focusoutblur)$/,
	rtypenamespace = /^([^.]*)(?:\.(.+)|)$/;

function returnTrue() {
	return true;
}

function returnFalse() {
	return false;
}

function safeActiveElement() {
	try {
		return document.activeElement;
	} catch ( err ) { }
}

/*
 * Helper functions for managing events -- not part of the public interface.
 * Props to Dean Edwards' addEvent library for many of the ideas.
 */
jQuery.event = {

	global: {},

	add: function( elem, types, handler, data, selector ) {
		var tmp, events, t, handleObjIn,
			special, eventHandle, handleObj,
			handlers, type, namespaces, origType,
			elemData = jQuery._data( elem );

		// Don't attach events to noData or text/comment nodes (but allow plain objects)
		if ( !elemData ) {
			return;
		}

		// Caller can pass in an object of custom data in lieu of the handler
		if ( handler.handler ) {
			handleObjIn = handler;
			handler = handleObjIn.handler;
			selector = handleObjIn.selector;
		}

		// Make sure that the handler has a unique ID, used to find/remove it later
		if ( !handler.guid ) {
			handler.guid = jQuery.guid++;
		}

		// Init the element's event structure and main handler, if this is the first
		if ( !(events = elemData.events) ) {
			events = elemData.events = {};
		}
		if ( !(eventHandle = elemData.handle) ) {
			eventHandle = elemData.handle = function( e ) {
				// Discard the second event of a jQuery.event.trigger() and
				// when an event is called after a page has unloaded
				return typeof jQuery !== core_strundefined && (!e || jQuery.event.triggered !== e.type) ?
					jQuery.event.dispatch.apply( eventHandle.elem, arguments ) :
					undefined;
			};
			// Add elem as a property of the handle fn to prevent a memory leak with IE non-native events
			eventHandle.elem = elem;
		}

		// Handle multiple events separated by a space
		types = ( types || "" ).match( core_rnotwhite ) || [""];
		t = types.length;
		while ( t-- ) {
			tmp = rtypenamespace.exec( types[t] ) || [];
			type = origType = tmp[1];
			namespaces = ( tmp[2] || "" ).split( "." ).sort();

			// There *must* be a type, no attaching namespace-only handlers
			if ( !type ) {
				continue;
			}

			// If event changes its type, use the special event handlers for the changed type
			special = jQuery.event.special[ type ] || {};

			// If selector defined, determine special event api type, otherwise given type
			type = ( selector ? special.delegateType : special.bindType ) || type;

			// Update special based on newly reset type
			special = jQuery.event.special[ type ] || {};

			// handleObj is passed to all event handlers
			handleObj = jQuery.extend({
				type: type,
				origType: origType,
				data: data,
				handler: handler,
				guid: handler.guid,
				selector: selector,
				needsContext: selector && jQuery.expr.match.needsContext.test( selector ),
				namespace: namespaces.join(".")
			}, handleObjIn );

			// Init the event handler queue if we're the first
			if ( !(handlers = events[ type ]) ) {
				handlers = events[ type ] = [];
				handlers.delegateCount = 0;

				// Only use addEventListener/attachEvent if the special events handler returns false
				if ( !special.setup || special.setup.call( elem, data, namespaces, eventHandle ) === false ) {
					// Bind the global event handler to the element
					if ( elem.addEventListener ) {
						elem.addEventListener( type, eventHandle, false );

					} else if ( elem.attachEvent ) {
						elem.attachEvent( "on" + type, eventHandle );
					}
				}
			}

			if ( special.add ) {
				special.add.call( elem, handleObj );

				if ( !handleObj.handler.guid ) {
					handleObj.handler.guid = handler.guid;
				}
			}

			// Add to the element's handler list, delegates in front
			if ( selector ) {
				handlers.splice( handlers.delegateCount++, 0, handleObj );
			} else {
				handlers.push( handleObj );
			}

			// Keep track of which events have ever been used, for event optimization
			jQuery.event.global[ type ] = true;
		}

		// Nullify elem to prevent memory leaks in IE
		elem = null;
	},

	// Detach an event or set of events from an element
	remove: function( elem, types, handler, selector, mappedTypes ) {
		var j, handleObj, tmp,
			origCount, t, events,
			special, handlers, type,
			namespaces, origType,
			elemData = jQuery.hasData( elem ) && jQuery._data( elem );

		if ( !elemData || !(events = elemData.events) ) {
			return;
		}

		// Once for each type.namespace in types; type may be omitted
		types = ( types || "" ).match( core_rnotwhite ) || [""];
		t = types.length;
		while ( t-- ) {
			tmp = rtypenamespace.exec( types[t] ) || [];
			type = origType = tmp[1];
			namespaces = ( tmp[2] || "" ).split( "." ).sort();

			// Unbind all events (on this namespace, if provided) for the element
			if ( !type ) {
				for ( type in events ) {
					jQuery.event.remove( elem, type + types[ t ], handler, selector, true );
				}
				continue;
			}

			special = jQuery.event.special[ type ] || {};
			type = ( selector ? special.delegateType : special.bindType ) || type;
			handlers = events[ type ] || [];
			tmp = tmp[2] && new RegExp( "(^|\\.)" + namespaces.join("\\.(?:.*\\.|)") + "(\\.|$)" );

			// Remove matching events
			origCount = j = handlers.length;
			while ( j-- ) {
				handleObj = handlers[ j ];

				if ( ( mappedTypes || origType === handleObj.origType ) &&
					( !handler || handler.guid === handleObj.guid ) &&
					( !tmp || tmp.test( handleObj.namespace ) ) &&
					( !selector || selector === handleObj.selector || selector === "**" && handleObj.selector ) ) {
					handlers.splice( j, 1 );

					if ( handleObj.selector ) {
						handlers.delegateCount--;
					}
					if ( special.remove ) {
						special.remove.call( elem, handleObj );
					}
				}
			}

			// Remove generic event handler if we removed something and no more handlers exist
			// (avoids potential for endless recursion during removal of special event handlers)
			if ( origCount && !handlers.length ) {
				if ( !special.teardown || special.teardown.call( elem, namespaces, elemData.handle ) === false ) {
					jQuery.removeEvent( elem, type, elemData.handle );
				}

				delete events[ type ];
			}
		}

		// Remove the expando if it's no longer used
		if ( jQuery.isEmptyObject( events ) ) {
			delete elemData.handle;

			// removeData also checks for emptiness and clears the expando if empty
			// so use it instead of delete
			jQuery._removeData( elem, "events" );
		}
	},

	trigger: function( event, data, elem, onlyHandlers ) {
		var handle, ontype, cur,
			bubbleType, special, tmp, i,
			eventPath = [ elem || document ],
			type = core_hasOwn.call( event, "type" ) ? event.type : event,
			namespaces = core_hasOwn.call( event, "namespace" ) ? event.namespace.split(".") : [];

		cur = tmp = elem = elem || document;

		// Don't do events on text and comment nodes
		if ( elem.nodeType === 3 || elem.nodeType === 8 ) {
			return;
		}

		// focus/blur morphs to focusin/out; ensure we're not firing them right now
		if ( rfocusMorph.test( type + jQuery.event.triggered ) ) {
			return;
		}

		if ( type.indexOf(".") >= 0 ) {
			// Namespaced trigger; create a regexp to match event type in handle()
			namespaces = type.split(".");
			type = namespaces.shift();
			namespaces.sort();
		}
		ontype = type.indexOf(":") < 0 && "on" + type;

		// Caller can pass in a jQuery.Event object, Object, or just an event type string
		event = event[ jQuery.expando ] ?
			event :
			new jQuery.Event( type, typeof event === "object" && event );

		// Trigger bitmask: & 1 for native handlers; & 2 for jQuery (always true)
		event.isTrigger = onlyHandlers ? 2 : 3;
		event.namespace = namespaces.join(".");
		event.namespace_re = event.namespace ?
			new RegExp( "(^|\\.)" + namespaces.join("\\.(?:.*\\.|)") + "(\\.|$)" ) :
			null;

		// Clean up the event in case it is being reused
		event.result = undefined;
		if ( !event.target ) {
			event.target = elem;
		}

		// Clone any incoming data and prepend the event, creating the handler arg list
		data = data == null ?
			[ event ] :
			jQuery.makeArray( data, [ event ] );

		// Allow special events to draw outside the lines
		special = jQuery.event.special[ type ] || {};
		if ( !onlyHandlers && special.trigger && special.trigger.apply( elem, data ) === false ) {
			return;
		}

		// Determine event propagation path in advance, per W3C events spec (#9951)
		// Bubble up to document, then to window; watch for a global ownerDocument var (#9724)
		if ( !onlyHandlers && !special.noBubble && !jQuery.isWindow( elem ) ) {

			bubbleType = special.delegateType || type;
			if ( !rfocusMorph.test( bubbleType + type ) ) {
				cur = cur.parentNode;
			}
			for ( ; cur; cur = cur.parentNode ) {
				eventPath.push( cur );
				tmp = cur;
			}

			// Only add window if we got to document (e.g., not plain obj or detached DOM)
			if ( tmp === (elem.ownerDocument || document) ) {
				eventPath.push( tmp.defaultView || tmp.parentWindow || window );
			}
		}

		// Fire handlers on the event path
		i = 0;
		while ( (cur = eventPath[i++]) && !event.isPropagationStopped() ) {

			event.type = i > 1 ?
				bubbleType :
				special.bindType || type;

			// jQuery handler
			handle = ( jQuery._data( cur, "events" ) || {} )[ event.type ] && jQuery._data( cur, "handle" );
			if ( handle ) {
				handle.apply( cur, data );
			}

			// Native handler
			handle = ontype && cur[ ontype ];
			if ( handle && jQuery.acceptData( cur ) && handle.apply && handle.apply( cur, data ) === false ) {
				event.preventDefault();
			}
		}
		event.type = type;

		// If nobody prevented the default action, do it now
		if ( !onlyHandlers && !event.isDefaultPrevented() ) {

			if ( (!special._default || special._default.apply( eventPath.pop(), data ) === false) &&
				jQuery.acceptData( elem ) ) {

				// Call a native DOM method on the target with the same name name as the event.
				// Can't use an .isFunction() check here because IE6/7 fails that test.
				// Don't do default actions on window, that's where global variables be (#6170)
				if ( ontype && elem[ type ] && !jQuery.isWindow( elem ) ) {

					// Don't re-trigger an onFOO event when we call its FOO() method
					tmp = elem[ ontype ];

					if ( tmp ) {
						elem[ ontype ] = null;
					}

					// Prevent re-triggering of the same event, since we already bubbled it above
					jQuery.event.triggered = type;
					try {
						elem[ type ]();
					} catch ( e ) {
						// IE<9 dies on focus/blur to hidden element (#1486,#12518)
						// only reproducible on winXP IE8 native, not IE9 in IE8 mode
					}
					jQuery.event.triggered = undefined;

					if ( tmp ) {
						elem[ ontype ] = tmp;
					}
				}
			}
		}

		return event.result;
	},

	dispatch: function( event ) {

		// Make a writable jQuery.Event from the native event object
		event = jQuery.event.fix( event );

		var i, ret, handleObj, matched, j,
			handlerQueue = [],
			args = core_slice.call( arguments ),
			handlers = ( jQuery._data( this, "events" ) || {} )[ event.type ] || [],
			special = jQuery.event.special[ event.type ] || {};

		// Use the fix-ed jQuery.Event rather than the (read-only) native event
		args[0] = event;
		event.delegateTarget = this;

		// Call the preDispatch hook for the mapped type, and let it bail if desired
		if ( special.preDispatch && special.preDispatch.call( this, event ) === false ) {
			return;
		}

		// Determine handlers
		handlerQueue = jQuery.event.handlers.call( this, event, handlers );

		// Run delegates first; they may want to stop propagation beneath us
		i = 0;
		while ( (matched = handlerQueue[ i++ ]) && !event.isPropagationStopped() ) {
			event.currentTarget = matched.elem;

			j = 0;
			while ( (handleObj = matched.handlers[ j++ ]) && !event.isImmediatePropagationStopped() ) {

				// Triggered event must either 1) have no namespace, or
				// 2) have namespace(s) a subset or equal to those in the bound event (both can have no namespace).
				if ( !event.namespace_re || event.namespace_re.test( handleObj.namespace ) ) {

					event.handleObj = handleObj;
					event.data = handleObj.data;

					ret = ( (jQuery.event.special[ handleObj.origType ] || {}).handle || handleObj.handler )
							.apply( matched.elem, args );

					if ( ret !== undefined ) {
						if ( (event.result = ret) === false ) {
							event.preventDefault();
							event.stopPropagation();
						}
					}
				}
			}
		}

		// Call the postDispatch hook for the mapped type
		if ( special.postDispatch ) {
			special.postDispatch.call( this, event );
		}

		return event.result;
	},

	handlers: function( event, handlers ) {
		var sel, handleObj, matches, i,
			handlerQueue = [],
			delegateCount = handlers.delegateCount,
			cur = event.target;

		// Find delegate handlers
		// Black-hole SVG <use> instance trees (#13180)
		// Avoid non-left-click bubbling in Firefox (#3861)
		if ( delegateCount && cur.nodeType && (!event.button || event.type !== "click") ) {

			/* jshint eqeqeq: false */
			for ( ; cur != this; cur = cur.parentNode || this ) {
				/* jshint eqeqeq: true */

				// Don't check non-elements (#13208)
				// Don't process clicks on disabled elements (#6911, #8165, #11382, #11764)
				if ( cur.nodeType === 1 && (cur.disabled !== true || event.type !== "click") ) {
					matches = [];
					for ( i = 0; i < delegateCount; i++ ) {
						handleObj = handlers[ i ];

						// Don't conflict with Object.prototype properties (#13203)
						sel = handleObj.selector + " ";

						if ( matches[ sel ] === undefined ) {
							matches[ sel ] = handleObj.needsContext ?
								jQuery( sel, this ).index( cur ) >= 0 :
								jQuery.find( sel, this, null, [ cur ] ).length;
						}
						if ( matches[ sel ] ) {
							matches.push( handleObj );
						}
					}
					if ( matches.length ) {
						handlerQueue.push({ elem: cur, handlers: matches });
					}
				}
			}
		}

		// Add the remaining (directly-bound) handlers
		if ( delegateCount < handlers.length ) {
			handlerQueue.push({ elem: this, handlers: handlers.slice( delegateCount ) });
		}

		return handlerQueue;
	},

	fix: function( event ) {
		if ( event[ jQuery.expando ] ) {
			return event;
		}

		// Create a writable copy of the event object and normalize some properties
		var i, prop, copy,
			type = event.type,
			originalEvent = event,
			fixHook = this.fixHooks[ type ];

		if ( !fixHook ) {
			this.fixHooks[ type ] = fixHook =
				rmouseEvent.test( type ) ? this.mouseHooks :
				rkeyEvent.test( type ) ? this.keyHooks :
				{};
		}
		copy = fixHook.props ? this.props.concat( fixHook.props ) : this.props;

		event = new jQuery.Event( originalEvent );

		i = copy.length;
		while ( i-- ) {
			prop = copy[ i ];
			event[ prop ] = originalEvent[ prop ];
		}

		// Support: IE<9
		// Fix target property (#1925)
		if ( !event.target ) {
			event.target = originalEvent.srcElement || document;
		}

		// Support: Chrome 23+, Safari?
		// Target should not be a text node (#504, #13143)
		if ( event.target.nodeType === 3 ) {
			event.target = event.target.parentNode;
		}

		// Support: IE<9
		// For mouse/key events, metaKey==false if it's undefined (#3368, #11328)
		event.metaKey = !!event.metaKey;

		return fixHook.filter ? fixHook.filter( event, originalEvent ) : event;
	},

	// Includes some event props shared by KeyEvent and MouseEvent
	props: "altKey bubbles cancelable ctrlKey currentTarget eventPhase metaKey relatedTarget shiftKey target timeStamp view which".split(" "),

	fixHooks: {},

	keyHooks: {
		props: "char charCode key keyCode".split(" "),
		filter: function( event, original ) {

			// Add which for key events
			if ( event.which == null ) {
				event.which = original.charCode != null ? original.charCode : original.keyCode;
			}

			return event;
		}
	},

	mouseHooks: {
		props: "button buttons clientX clientY fromElement offsetX offsetY pageX pageY screenX screenY toElement".split(" "),
		filter: function( event, original ) {
			var body, eventDoc, doc,
				button = original.button,
				fromElement = original.fromElement;

			// Calculate pageX/Y if missing and clientX/Y available
			if ( event.pageX == null && original.clientX != null ) {
				eventDoc = event.target.ownerDocument || document;
				doc = eventDoc.documentElement;
				body = eventDoc.body;

				event.pageX = original.clientX + ( doc && doc.scrollLeft || body && body.scrollLeft || 0 ) - ( doc && doc.clientLeft || body && body.clientLeft || 0 );
				event.pageY = original.clientY + ( doc && doc.scrollTop  || body && body.scrollTop  || 0 ) - ( doc && doc.clientTop  || body && body.clientTop  || 0 );
			}

			// Add relatedTarget, if necessary
			if ( !event.relatedTarget && fromElement ) {
				event.relatedTarget = fromElement === event.target ? original.toElement : fromElement;
			}

			// Add which for click: 1 === left; 2 === middle; 3 === right
			// Note: button is not normalized, so don't use it
			if ( !event.which && button !== undefined ) {
				event.which = ( button & 1 ? 1 : ( button & 2 ? 3 : ( button & 4 ? 2 : 0 ) ) );
			}

			return event;
		}
	},

	special: {
		load: {
			// Prevent triggered image.load events from bubbling to window.load
			noBubble: true
		},
		focus: {
			// Fire native event if possible so blur/focus sequence is correct
			trigger: function() {
				if ( this !== safeActiveElement() && this.focus ) {
					try {
						this.focus();
						return false;
					} catch ( e ) {
						// Support: IE<9
						// If we error on focus to hidden element (#1486, #12518),
						// let .trigger() run the handlers
					}
				}
			},
			delegateType: "focusin"
		},
		blur: {
			trigger: function() {
				if ( this === safeActiveElement() && this.blur ) {
					this.blur();
					return false;
				}
			},
			delegateType: "focusout"
		},
		click: {
			// For checkbox, fire native event so checked state will be right
			trigger: function() {
				if ( jQuery.nodeName( this, "input" ) && this.type === "checkbox" && this.click ) {
					this.click();
					return false;
				}
			},

			// For cross-browser consistency, don't fire native .click() on links
			_default: function( event ) {
				return jQuery.nodeName( event.target, "a" );
			}
		},

		beforeunload: {
			postDispatch: function( event ) {

				// Even when returnValue equals to undefined Firefox will still show alert
				if ( event.result !== undefined ) {
					event.originalEvent.returnValue = event.result;
				}
			}
		}
	},

	simulate: function( type, elem, event, bubble ) {
		// Piggyback on a donor event to simulate a different one.
		// Fake originalEvent to avoid donor's stopPropagation, but if the
		// simulated event prevents default then we do the same on the donor.
		var e = jQuery.extend(
			new jQuery.Event(),
			event,
			{
				type: type,
				isSimulated: true,
				originalEvent: {}
			}
		);
		if ( bubble ) {
			jQuery.event.trigger( e, null, elem );
		} else {
			jQuery.event.dispatch.call( elem, e );
		}
		if ( e.isDefaultPrevented() ) {
			event.preventDefault();
		}
	}
};

jQuery.removeEvent = document.removeEventListener ?
	function( elem, type, handle ) {
		if ( elem.removeEventListener ) {
			elem.removeEventListener( type, handle, false );
		}
	} :
	function( elem, type, handle ) {
		var name = "on" + type;

		if ( elem.detachEvent ) {

			// #8545, #7054, preventing memory leaks for custom events in IE6-8
			// detachEvent needed property on element, by name of that event, to properly expose it to GC
			if ( typeof elem[ name ] === core_strundefined ) {
				elem[ name ] = null;
			}

			elem.detachEvent( name, handle );
		}
	};

jQuery.Event = function( src, props ) {
	// Allow instantiation without the 'new' keyword
	if ( !(this instanceof jQuery.Event) ) {
		return new jQuery.Event( src, props );
	}

	// Event object
	if ( src && src.type ) {
		this.originalEvent = src;
		this.type = src.type;

		// Events bubbling up the document may have been marked as prevented
		// by a handler lower down the tree; reflect the correct value.
		this.isDefaultPrevented = ( src.defaultPrevented || src.returnValue === false ||
			src.getPreventDefault && src.getPreventDefault() ) ? returnTrue : returnFalse;

	// Event type
	} else {
		this.type = src;
	}

	// Put explicitly provided properties onto the event object
	if ( props ) {
		jQuery.extend( this, props );
	}

	// Create a timestamp if incoming event doesn't have one
	this.timeStamp = src && src.timeStamp || jQuery.now();

	// Mark it as fixed
	this[ jQuery.expando ] = true;
};

// jQuery.Event is based on DOM3 Events as specified by the ECMAScript Language Binding
// http://www.w3.org/TR/2003/WD-DOM-Level-3-Events-20030331/ecma-script-binding.html
jQuery.Event.prototype = {
	isDefaultPrevented: returnFalse,
	isPropagationStopped: returnFalse,
	isImmediatePropagationStopped: returnFalse,

	preventDefault: function() {
		var e = this.originalEvent;

		this.isDefaultPrevented = returnTrue;
		if ( !e ) {
			return;
		}

		// If preventDefault exists, run it on the original event
		if ( e.preventDefault ) {
			e.preventDefault();

		// Support: IE
		// Otherwise set the returnValue property of the original event to false
		} else {
			e.returnValue = false;
		}
	},
	stopPropagation: function() {
		var e = this.originalEvent;

		this.isPropagationStopped = returnTrue;
		if ( !e ) {
			return;
		}
		// If stopPropagation exists, run it on the original event
		if ( e.stopPropagation ) {
			e.stopPropagation();
		}

		// Support: IE
		// Set the cancelBubble property of the original event to true
		e.cancelBubble = true;
	},
	stopImmediatePropagation: function() {
		this.isImmediatePropagationStopped = returnTrue;
		this.stopPropagation();
	}
};

// Create mouseenter/leave events using mouseover/out and event-time checks
jQuery.each({
	mouseenter: "mouseover",
	mouseleave: "mouseout"
}, function( orig, fix ) {
	jQuery.event.special[ orig ] = {
		delegateType: fix,
		bindType: fix,

		handle: function( event ) {
			var ret,
				target = this,
				related = event.relatedTarget,
				handleObj = event.handleObj;

			// For mousenter/leave call the handler if related is outside the target.
			// NB: No relatedTarget if the mouse left/entered the browser window
			if ( !related || (related !== target && !jQuery.contains( target, related )) ) {
				event.type = handleObj.origType;
				ret = handleObj.handler.apply( this, arguments );
				event.type = fix;
			}
			return ret;
		}
	};
});

// IE submit delegation
if ( !jQuery.support.submitBubbles ) {

	jQuery.event.special.submit = {
		setup: function() {
			// Only need this for delegated form submit events
			if ( jQuery.nodeName( this, "form" ) ) {
				return false;
			}

			// Lazy-add a submit handler when a descendant form may potentially be submitted
			jQuery.event.add( this, "click._submit keypress._submit", function( e ) {
				// Node name check avoids a VML-related crash in IE (#9807)
				var elem = e.target,
					form = jQuery.nodeName( elem, "input" ) || jQuery.nodeName( elem, "button" ) ? elem.form : undefined;
				if ( form && !jQuery._data( form, "submitBubbles" ) ) {
					jQuery.event.add( form, "submit._submit", function( event ) {
						event._submit_bubble = true;
					});
					jQuery._data( form, "submitBubbles", true );
				}
			});
			// return undefined since we don't need an event listener
		},

		postDispatch: function( event ) {
			// If form was submitted by the user, bubble the event up the tree
			if ( event._submit_bubble ) {
				delete event._submit_bubble;
				if ( this.parentNode && !event.isTrigger ) {
					jQuery.event.simulate( "submit", this.parentNode, event, true );
				}
			}
		},

		teardown: function() {
			// Only need this for delegated form submit events
			if ( jQuery.nodeName( this, "form" ) ) {
				return false;
			}

			// Remove delegated handlers; cleanData eventually reaps submit handlers attached above
			jQuery.event.remove( this, "._submit" );
		}
	};
}

// IE change delegation and checkbox/radio fix
if ( !jQuery.support.changeBubbles ) {

	jQuery.event.special.change = {

		setup: function() {

			if ( rformElems.test( this.nodeName ) ) {
				// IE doesn't fire change on a check/radio until blur; trigger it on click
				// after a propertychange. Eat the blur-change in special.change.handle.
				// This still fires onchange a second time for check/radio after blur.
				if ( this.type === "checkbox" || this.type === "radio" ) {
					jQuery.event.add( this, "propertychange._change", function( event ) {
						if ( event.originalEvent.propertyName === "checked" ) {
							this._just_changed = true;
						}
					});
					jQuery.event.add( this, "click._change", function( event ) {
						if ( this._just_changed && !event.isTrigger ) {
							this._just_changed = false;
						}
						// Allow triggered, simulated change events (#11500)
						jQuery.event.simulate( "change", this, event, true );
					});
				}
				return false;
			}
			// Delegated event; lazy-add a change handler on descendant inputs
			jQuery.event.add( this, "beforeactivate._change", function( e ) {
				var elem = e.target;

				if ( rformElems.test( elem.nodeName ) && !jQuery._data( elem, "changeBubbles" ) ) {
					jQuery.event.add( elem, "change._change", function( event ) {
						if ( this.parentNode && !event.isSimulated && !event.isTrigger ) {
							jQuery.event.simulate( "change", this.parentNode, event, true );
						}
					});
					jQuery._data( elem, "changeBubbles", true );
				}
			});
		},

		handle: function( event ) {
			var elem = event.target;

			// Swallow native change events from checkbox/radio, we already triggered them above
			if ( this !== elem || event.isSimulated || event.isTrigger || (elem.type !== "radio" && elem.type !== "checkbox") ) {
				return event.handleObj.handler.apply( this, arguments );
			}
		},

		teardown: function() {
			jQuery.event.remove( this, "._change" );

			return !rformElems.test( this.nodeName );
		}
	};
}

// Create "bubbling" focus and blur events
if ( !jQuery.support.focusinBubbles ) {
	jQuery.each({ focus: "focusin", blur: "focusout" }, function( orig, fix ) {

		// Attach a single capturing handler while someone wants focusin/focusout
		var attaches = 0,
			handler = function( event ) {
				jQuery.event.simulate( fix, event.target, jQuery.event.fix( event ), true );
			};

		jQuery.event.special[ fix ] = {
			setup: function() {
				if ( attaches++ === 0 ) {
					document.addEventListener( orig, handler, true );
				}
			},
			teardown: function() {
				if ( --attaches === 0 ) {
					document.removeEventListener( orig, handler, true );
				}
			}
		};
	});
}

jQuery.fn.extend({

	on: function( types, selector, data, fn, /*INTERNAL*/ one ) {
		var type, origFn;

		// Types can be a map of types/handlers
		if ( typeof types === "object" ) {
			// ( types-Object, selector, data )
			if ( typeof selector !== "string" ) {
				// ( types-Object, data )
				data = data || selector;
				selector = undefined;
			}
			for ( type in types ) {
				this.on( type, selector, data, types[ type ], one );
			}
			return this;
		}

		if ( data == null && fn == null ) {
			// ( types, fn )
			fn = selector;
			data = selector = undefined;
		} else if ( fn == null ) {
			if ( typeof selector === "string" ) {
				// ( types, selector, fn )
				fn = data;
				data = undefined;
			} else {
				// ( types, data, fn )
				fn = data;
				data = selector;
				selector = undefined;
			}
		}
		if ( fn === false ) {
			fn = returnFalse;
		} else if ( !fn ) {
			return this;
		}

		if ( one === 1 ) {
			origFn = fn;
			fn = function( event ) {
				// Can use an empty set, since event contains the info
				jQuery().off( event );
				return origFn.apply( this, arguments );
			};
			// Use same guid so caller can remove using origFn
			fn.guid = origFn.guid || ( origFn.guid = jQuery.guid++ );
		}
		return this.each( function() {
			jQuery.event.add( this, types, fn, data, selector );
		});
	},
	one: function( types, selector, data, fn ) {
		return this.on( types, selector, data, fn, 1 );
	},
	off: function( types, selector, fn ) {
		var handleObj, type;
		if ( types && types.preventDefault && types.handleObj ) {
			// ( event )  dispatched jQuery.Event
			handleObj = types.handleObj;
			jQuery( types.delegateTarget ).off(
				handleObj.namespace ? handleObj.origType + "." + handleObj.namespace : handleObj.origType,
				handleObj.selector,
				handleObj.handler
			);
			return this;
		}
		if ( typeof types === "object" ) {
			// ( types-object [, selector] )
			for ( type in types ) {
				this.off( type, selector, types[ type ] );
			}
			return this;
		}
		if ( selector === false || typeof selector === "function" ) {
			// ( types [, fn] )
			fn = selector;
			selector = undefined;
		}
		if ( fn === false ) {
			fn = returnFalse;
		}
		return this.each(function() {
			jQuery.event.remove( this, types, fn, selector );
		});
	},

	trigger: function( type, data ) {
		return this.each(function() {
			jQuery.event.trigger( type, data, this );
		});
	},
	triggerHandler: function( type, data ) {
		var elem = this[0];
		if ( elem ) {
			return jQuery.event.trigger( type, data, elem, true );
		}
	}
});
var isSimple = /^.[^:#\[\.,]*$/,
	rparentsprev = /^(?:parents|prev(?:Until|All))/,
	rneedsContext = jQuery.expr.match.needsContext,
	// methods guaranteed to produce a unique set when starting from a unique set
	guaranteedUnique = {
		children: true,
		contents: true,
		next: true,
		prev: true
	};

jQuery.fn.extend({
	find: function( selector ) {
		var i,
			ret = [],
			self = this,
			len = self.length;

		if ( typeof selector !== "string" ) {
			return this.pushStack( jQuery( selector ).filter(function() {
				for ( i = 0; i < len; i++ ) {
					if ( jQuery.contains( self[ i ], this ) ) {
						return true;
					}
				}
			}) );
		}

		for ( i = 0; i < len; i++ ) {
			jQuery.find( selector, self[ i ], ret );
		}

		// Needed because $( selector, context ) becomes $( context ).find( selector )
		ret = this.pushStack( len > 1 ? jQuery.unique( ret ) : ret );
		ret.selector = this.selector ? this.selector + " " + selector : selector;
		return ret;
	},

	has: function( target ) {
		var i,
			targets = jQuery( target, this ),
			len = targets.length;

		return this.filter(function() {
			for ( i = 0; i < len; i++ ) {
				if ( jQuery.contains( this, targets[i] ) ) {
					return true;
				}
			}
		});
	},

	not: function( selector ) {
		return this.pushStack( winnow(this, selector || [], true) );
	},

	filter: function( selector ) {
		return this.pushStack( winnow(this, selector || [], false) );
	},

	is: function( selector ) {
		return !!winnow(
			this,

			// If this is a positional/relative selector, check membership in the returned set
			// so $("p:first").is("p:last") won't return true for a doc with two "p".
			typeof selector === "string" && rneedsContext.test( selector ) ?
				jQuery( selector ) :
				selector || [],
			false
		).length;
	},

	closest: function( selectors, context ) {
		var cur,
			i = 0,
			l = this.length,
			ret = [],
			pos = rneedsContext.test( selectors ) || typeof selectors !== "string" ?
				jQuery( selectors, context || this.context ) :
				0;

		for ( ; i < l; i++ ) {
			for ( cur = this[i]; cur && cur !== context; cur = cur.parentNode ) {
				// Always skip document fragments
				if ( cur.nodeType < 11 && (pos ?
					pos.index(cur) > -1 :

					// Don't pass non-elements to Sizzle
					cur.nodeType === 1 &&
						jQuery.find.matchesSelector(cur, selectors)) ) {

					cur = ret.push( cur );
					break;
				}
			}
		}

		return this.pushStack( ret.length > 1 ? jQuery.unique( ret ) : ret );
	},

	// Determine the position of an element within
	// the matched set of elements
	index: function( elem ) {

		// No argument, return index in parent
		if ( !elem ) {
			return ( this[0] && this[0].parentNode ) ? this.first().prevAll().length : -1;
		}

		// index in selector
		if ( typeof elem === "string" ) {
			return jQuery.inArray( this[0], jQuery( elem ) );
		}

		// Locate the position of the desired element
		return jQuery.inArray(
			// If it receives a jQuery object, the first element is used
			elem.jquery ? elem[0] : elem, this );
	},

	add: function( selector, context ) {
		var set = typeof selector === "string" ?
				jQuery( selector, context ) :
				jQuery.makeArray( selector && selector.nodeType ? [ selector ] : selector ),
			all = jQuery.merge( this.get(), set );

		return this.pushStack( jQuery.unique(all) );
	},

	addBack: function( selector ) {
		return this.add( selector == null ?
			this.prevObject : this.prevObject.filter(selector)
		);
	}
});

function sibling( cur, dir ) {
	do {
		cur = cur[ dir ];
	} while ( cur && cur.nodeType !== 1 );

	return cur;
}

jQuery.each({
	parent: function( elem ) {
		var parent = elem.parentNode;
		return parent && parent.nodeType !== 11 ? parent : null;
	},
	parents: function( elem ) {
		return jQuery.dir( elem, "parentNode" );
	},
	parentsUntil: function( elem, i, until ) {
		return jQuery.dir( elem, "parentNode", until );
	},
	next: function( elem ) {
		return sibling( elem, "nextSibling" );
	},
	prev: function( elem ) {
		return sibling( elem, "previousSibling" );
	},
	nextAll: function( elem ) {
		return jQuery.dir( elem, "nextSibling" );
	},
	prevAll: function( elem ) {
		return jQuery.dir( elem, "previousSibling" );
	},
	nextUntil: function( elem, i, until ) {
		return jQuery.dir( elem, "nextSibling", until );
	},
	prevUntil: function( elem, i, until ) {
		return jQuery.dir( elem, "previousSibling", until );
	},
	siblings: function( elem ) {
		return jQuery.sibling( ( elem.parentNode || {} ).firstChild, elem );
	},
	children: function( elem ) {
		return jQuery.sibling( elem.firstChild );
	},
	contents: function( elem ) {
		return jQuery.nodeName( elem, "iframe" ) ?
			elem.contentDocument || elem.contentWindow.document :
			jQuery.merge( [], elem.childNodes );
	}
}, function( name, fn ) {
	jQuery.fn[ name ] = function( until, selector ) {
		var ret = jQuery.map( this, fn, until );

		if ( name.slice( -5 ) !== "Until" ) {
			selector = until;
		}

		if ( selector && typeof selector === "string" ) {
			ret = jQuery.filter( selector, ret );
		}

		if ( this.length > 1 ) {
			// Remove duplicates
			if ( !guaranteedUnique[ name ] ) {
				ret = jQuery.unique( ret );
			}

			// Reverse order for parents* and prev-derivatives
			if ( rparentsprev.test( name ) ) {
				ret = ret.reverse();
			}
		}

		return this.pushStack( ret );
	};
});

jQuery.extend({
	filter: function( expr, elems, not ) {
		var elem = elems[ 0 ];

		if ( not ) {
			expr = ":not(" + expr + ")";
		}

		return elems.length === 1 && elem.nodeType === 1 ?
			jQuery.find.matchesSelector( elem, expr ) ? [ elem ] : [] :
			jQuery.find.matches( expr, jQuery.grep( elems, function( elem ) {
				return elem.nodeType === 1;
			}));
	},

	dir: function( elem, dir, until ) {
		var matched = [],
			cur = elem[ dir ];

		while ( cur && cur.nodeType !== 9 && (until === undefined || cur.nodeType !== 1 || !jQuery( cur ).is( until )) ) {
			if ( cur.nodeType === 1 ) {
				matched.push( cur );
			}
			cur = cur[dir];
		}
		return matched;
	},

	sibling: function( n, elem ) {
		var r = [];

		for ( ; n; n = n.nextSibling ) {
			if ( n.nodeType === 1 && n !== elem ) {
				r.push( n );
			}
		}

		return r;
	}
});

// Implement the identical functionality for filter and not
function winnow( elements, qualifier, not ) {
	if ( jQuery.isFunction( qualifier ) ) {
		return jQuery.grep( elements, function( elem, i ) {
			/* jshint -W018 */
			return !!qualifier.call( elem, i, elem ) !== not;
		});

	}

	if ( qualifier.nodeType ) {
		return jQuery.grep( elements, function( elem ) {
			return ( elem === qualifier ) !== not;
		});

	}

	if ( typeof qualifier === "string" ) {
		if ( isSimple.test( qualifier ) ) {
			return jQuery.filter( qualifier, elements, not );
		}

		qualifier = jQuery.filter( qualifier, elements );
	}

	return jQuery.grep( elements, function( elem ) {
		return ( jQuery.inArray( elem, qualifier ) >= 0 ) !== not;
	});
}
function createSafeFragment( document ) {
	var list = nodeNames.split( "|" ),
		safeFrag = document.createDocumentFragment();

	if ( safeFrag.createElement ) {
		while ( list.length ) {
			safeFrag.createElement(
				list.pop()
			);
		}
	}
	return safeFrag;
}

var nodeNames = "abbr|article|aside|audio|bdi|canvas|data|datalist|details|figcaption|figure|footer|" +
		"header|hgroup|mark|meter|nav|output|progress|section|summary|time|video",
	rinlinejQuery = / jQuery\d+="(?:null|\d+)"/g,
	rnoshimcache = new RegExp("<(?:" + nodeNames + ")[\\s/>]", "i"),
	rleadingWhitespace = /^\s+/,
	rxhtmlTag = /<(?!area|br|col|embed|hr|img|input|link|meta|param)(([\w:]+)[^>]*)\/>/gi,
	rtagName = /<([\w:]+)/,
	rtbody = /<tbody/i,
	rhtml = /<|&#?\w+;/,
	rnoInnerhtml = /<(?:script|style|link)/i,
	manipulation_rcheckableType = /^(?:checkbox|radio)$/i,
	// checked="checked" or checked
	rchecked = /checked\s*(?:[^=]|=\s*.checked.)/i,
	rscriptType = /^$|\/(?:java|ecma)script/i,
	rscriptTypeMasked = /^true\/(.*)/,
	rcleanScript = /^\s*<!(?:\[CDATA\[|--)|(?:\]\]|--)>\s*$/g,

	// We have to close these tags to support XHTML (#13200)
	wrapMap = {
		option: [ 1, "<select multiple='multiple'>", "</select>" ],
		legend: [ 1, "<fieldset>", "</fieldset>" ],
		area: [ 1, "<map>", "</map>" ],
		param: [ 1, "<object>", "</object>" ],
		thead: [ 1, "<table>", "</table>" ],
		tr: [ 2, "<table><tbody>", "</tbody></table>" ],
		col: [ 2, "<table><tbody></tbody><colgroup>", "</colgroup></table>" ],
		td: [ 3, "<table><tbody><tr>", "</tr></tbody></table>" ],

		// IE6-8 can't serialize link, script, style, or any html5 (NoScope) tags,
		// unless wrapped in a div with non-breaking characters in front of it.
		_default: jQuery.support.htmlSerialize ? [ 0, "", "" ] : [ 1, "X<div>", "</div>"  ]
	},
	safeFragment = createSafeFragment( document ),
	fragmentDiv = safeFragment.appendChild( document.createElement("div") );

wrapMap.optgroup = wrapMap.option;
wrapMap.tbody = wrapMap.tfoot = wrapMap.colgroup = wrapMap.caption = wrapMap.thead;
wrapMap.th = wrapMap.td;

jQuery.fn.extend({
	text: function( value ) {
		return jQuery.access( this, function( value ) {
			return value === undefined ?
				jQuery.text( this ) :
				this.empty().append( ( this[0] && this[0].ownerDocument || document ).createTextNode( value ) );
		}, null, value, arguments.length );
	},

	append: function() {
		return this.domManip( arguments, function( elem ) {
			if ( this.nodeType === 1 || this.nodeType === 11 || this.nodeType === 9 ) {
				var target = manipulationTarget( this, elem );
				target.appendChild( elem );
			}
		});
	},

	prepend: function() {
		return this.domManip( arguments, function( elem ) {
			if ( this.nodeType === 1 || this.nodeType === 11 || this.nodeType === 9 ) {
				var target = manipulationTarget( this, elem );
				target.insertBefore( elem, target.firstChild );
			}
		});
	},

	before: function() {
		return this.domManip( arguments, function( elem ) {
			if ( this.parentNode ) {
				this.parentNode.insertBefore( elem, this );
			}
		});
	},

	after: function() {
		return this.domManip( arguments, function( elem ) {
			if ( this.parentNode ) {
				this.parentNode.insertBefore( elem, this.nextSibling );
			}
		});
	},

	// keepData is for internal use only--do not document
	remove: function( selector, keepData ) {
		var elem,
			elems = selector ? jQuery.filter( selector, this ) : this,
			i = 0;

		for ( ; (elem = elems[i]) != null; i++ ) {

			if ( !keepData && elem.nodeType === 1 ) {
				jQuery.cleanData( getAll( elem ) );
			}

			if ( elem.parentNode ) {
				if ( keepData && jQuery.contains( elem.ownerDocument, elem ) ) {
					setGlobalEval( getAll( elem, "script" ) );
				}
				elem.parentNode.removeChild( elem );
			}
		}

		return this;
	},

	empty: function() {
		var elem,
			i = 0;

		for ( ; (elem = this[i]) != null; i++ ) {
			// Remove element nodes and prevent memory leaks
			if ( elem.nodeType === 1 ) {
				jQuery.cleanData( getAll( elem, false ) );
			}

			// Remove any remaining nodes
			while ( elem.firstChild ) {
				elem.removeChild( elem.firstChild );
			}

			// If this is a select, ensure that it displays empty (#12336)
			// Support: IE<9
			if ( elem.options && jQuery.nodeName( elem, "select" ) ) {
				elem.options.length = 0;
			}
		}

		return this;
	},

	clone: function( dataAndEvents, deepDataAndEvents ) {
		dataAndEvents = dataAndEvents == null ? false : dataAndEvents;
		deepDataAndEvents = deepDataAndEvents == null ? dataAndEvents : deepDataAndEvents;

		return this.map( function () {
			return jQuery.clone( this, dataAndEvents, deepDataAndEvents );
		});
	},

	html: function( value ) {
		return jQuery.access( this, function( value ) {
			var elem = this[0] || {},
				i = 0,
				l = this.length;

			if ( value === undefined ) {
				return elem.nodeType === 1 ?
					elem.innerHTML.replace( rinlinejQuery, "" ) :
					undefined;
			}

			// See if we can take a shortcut and just use innerHTML
			if ( typeof value === "string" && !rnoInnerhtml.test( value ) &&
				( jQuery.support.htmlSerialize || !rnoshimcache.test( value )  ) &&
				( jQuery.support.leadingWhitespace || !rleadingWhitespace.test( value ) ) &&
				!wrapMap[ ( rtagName.exec( value ) || ["", ""] )[1].toLowerCase() ] ) {

				value = value.replace( rxhtmlTag, "<$1></$2>" );

				try {
					for (; i < l; i++ ) {
						// Remove element nodes and prevent memory leaks
						elem = this[i] || {};
						if ( elem.nodeType === 1 ) {
							jQuery.cleanData( getAll( elem, false ) );
							elem.innerHTML = value;
						}
					}

					elem = 0;

				// If using innerHTML throws an exception, use the fallback method
				} catch(e) {}
			}

			if ( elem ) {
				this.empty().append( value );
			}
		}, null, value, arguments.length );
	},

	replaceWith: function() {
		var
			// Snapshot the DOM in case .domManip sweeps something relevant into its fragment
			args = jQuery.map( this, function( elem ) {
				return [ elem.nextSibling, elem.parentNode ];
			}),
			i = 0;

		// Make the changes, replacing each context element with the new content
		this.domManip( arguments, function( elem ) {
			var next = args[ i++ ],
				parent = args[ i++ ];

			if ( parent ) {
				// Don't use the snapshot next if it has moved (#13810)
				if ( next && next.parentNode !== parent ) {
					next = this.nextSibling;
				}
				jQuery( this ).remove();
				parent.insertBefore( elem, next );
			}
		// Allow new content to include elements from the context set
		}, true );

		// Force removal if there was no new content (e.g., from empty arguments)
		return i ? this : this.remove();
	},

	detach: function( selector ) {
		return this.remove( selector, true );
	},

	domManip: function( args, callback, allowIntersection ) {

		// Flatten any nested arrays
		args = core_concat.apply( [], args );

		var first, node, hasScripts,
			scripts, doc, fragment,
			i = 0,
			l = this.length,
			set = this,
			iNoClone = l - 1,
			value = args[0],
			isFunction = jQuery.isFunction( value );

		// We can't cloneNode fragments that contain checked, in WebKit
		if ( isFunction || !( l <= 1 || typeof value !== "string" || jQuery.support.checkClone || !rchecked.test( value ) ) ) {
			return this.each(function( index ) {
				var self = set.eq( index );
				if ( isFunction ) {
					args[0] = value.call( this, index, self.html() );
				}
				self.domManip( args, callback, allowIntersection );
			});
		}

		if ( l ) {
			fragment = jQuery.buildFragment( args, this[ 0 ].ownerDocument, false, !allowIntersection && this );
			first = fragment.firstChild;

			if ( fragment.childNodes.length === 1 ) {
				fragment = first;
			}

			if ( first ) {
				scripts = jQuery.map( getAll( fragment, "script" ), disableScript );
				hasScripts = scripts.length;

				// Use the original fragment for the last item instead of the first because it can end up
				// being emptied incorrectly in certain situations (#8070).
				for ( ; i < l; i++ ) {
					node = fragment;

					if ( i !== iNoClone ) {
						node = jQuery.clone( node, true, true );

						// Keep references to cloned scripts for later restoration
						if ( hasScripts ) {
							jQuery.merge( scripts, getAll( node, "script" ) );
						}
					}

					callback.call( this[i], node, i );
				}

				if ( hasScripts ) {
					doc = scripts[ scripts.length - 1 ].ownerDocument;

					// Reenable scripts
					jQuery.map( scripts, restoreScript );

					// Evaluate executable scripts on first document insertion
					for ( i = 0; i < hasScripts; i++ ) {
						node = scripts[ i ];
						if ( rscriptType.test( node.type || "" ) &&
							!jQuery._data( node, "globalEval" ) && jQuery.contains( doc, node ) ) {

							if ( node.src ) {
								// Hope ajax is available...
								jQuery._evalUrl( node.src );
							} else {
								jQuery.globalEval( ( node.text || node.textContent || node.innerHTML || "" ).replace( rcleanScript, "" ) );
							}
						}
					}
				}

				// Fix #11809: Avoid leaking memory
				fragment = first = null;
			}
		}

		return this;
	}
});

// Support: IE<8
// Manipulating tables requires a tbody
function manipulationTarget( elem, content ) {
	return jQuery.nodeName( elem, "table" ) &&
		jQuery.nodeName( content.nodeType === 1 ? content : content.firstChild, "tr" ) ?

		elem.getElementsByTagName("tbody")[0] ||
			elem.appendChild( elem.ownerDocument.createElement("tbody") ) :
		elem;
}

// Replace/restore the type attribute of script elements for safe DOM manipulation
function disableScript( elem ) {
	elem.type = (jQuery.find.attr( elem, "type" ) !== null) + "/" + elem.type;
	return elem;
}
function restoreScript( elem ) {
	var match = rscriptTypeMasked.exec( elem.type );
	if ( match ) {
		elem.type = match[1];
	} else {
		elem.removeAttribute("type");
	}
	return elem;
}

// Mark scripts as having already been evaluated
function setGlobalEval( elems, refElements ) {
	var elem,
		i = 0;
	for ( ; (elem = elems[i]) != null; i++ ) {
		jQuery._data( elem, "globalEval", !refElements || jQuery._data( refElements[i], "globalEval" ) );
	}
}

function cloneCopyEvent( src, dest ) {

	if ( dest.nodeType !== 1 || !jQuery.hasData( src ) ) {
		return;
	}

	var type, i, l,
		oldData = jQuery._data( src ),
		curData = jQuery._data( dest, oldData ),
		events = oldData.events;

	if ( events ) {
		delete curData.handle;
		curData.events = {};

		for ( type in events ) {
			for ( i = 0, l = events[ type ].length; i < l; i++ ) {
				jQuery.event.add( dest, type, events[ type ][ i ] );
			}
		}
	}

	// make the cloned public data object a copy from the original
	if ( curData.data ) {
		curData.data = jQuery.extend( {}, curData.data );
	}
}

function fixCloneNodeIssues( src, dest ) {
	var nodeName, e, data;

	// We do not need to do anything for non-Elements
	if ( dest.nodeType !== 1 ) {
		return;
	}

	nodeName = dest.nodeName.toLowerCase();

	// IE6-8 copies events bound via attachEvent when using cloneNode.
	if ( !jQuery.support.noCloneEvent && dest[ jQuery.expando ] ) {
		data = jQuery._data( dest );

		for ( e in data.events ) {
			jQuery.removeEvent( dest, e, data.handle );
		}

		// Event data gets referenced instead of copied if the expando gets copied too
		dest.removeAttribute( jQuery.expando );
	}

	// IE blanks contents when cloning scripts, and tries to evaluate newly-set text
	if ( nodeName === "script" && dest.text !== src.text ) {
		disableScript( dest ).text = src.text;
		restoreScript( dest );

	// IE6-10 improperly clones children of object elements using classid.
	// IE10 throws NoModificationAllowedError if parent is null, #12132.
	} else if ( nodeName === "object" ) {
		if ( dest.parentNode ) {
			dest.outerHTML = src.outerHTML;
		}

		// This path appears unavoidable for IE9. When cloning an object
		// element in IE9, the outerHTML strategy above is not sufficient.
		// If the src has innerHTML and the destination does not,
		// copy the src.innerHTML into the dest.innerHTML. #10324
		if ( jQuery.support.html5Clone && ( src.innerHTML && !jQuery.trim(dest.innerHTML) ) ) {
			dest.innerHTML = src.innerHTML;
		}

	} else if ( nodeName === "input" && manipulation_rcheckableType.test( src.type ) ) {
		// IE6-8 fails to persist the checked state of a cloned checkbox
		// or radio button. Worse, IE6-7 fail to give the cloned element
		// a checked appearance if the defaultChecked value isn't also set

		dest.defaultChecked = dest.checked = src.checked;

		// IE6-7 get confused and end up setting the value of a cloned
		// checkbox/radio button to an empty string instead of "on"
		if ( dest.value !== src.value ) {
			dest.value = src.value;
		}

	// IE6-8 fails to return the selected option to the default selected
	// state when cloning options
	} else if ( nodeName === "option" ) {
		dest.defaultSelected = dest.selected = src.defaultSelected;

	// IE6-8 fails to set the defaultValue to the correct value when
	// cloning other types of input fields
	} else if ( nodeName === "input" || nodeName === "textarea" ) {
		dest.defaultValue = src.defaultValue;
	}
}

jQuery.each({
	appendTo: "append",
	prependTo: "prepend",
	insertBefore: "before",
	insertAfter: "after",
	replaceAll: "replaceWith"
}, function( name, original ) {
	jQuery.fn[ name ] = function( selector ) {
		var elems,
			i = 0,
			ret = [],
			insert = jQuery( selector ),
			last = insert.length - 1;

		for ( ; i <= last; i++ ) {
			elems = i === last ? this : this.clone(true);
			jQuery( insert[i] )[ original ]( elems );

			// Modern browsers can apply jQuery collections as arrays, but oldIE needs a .get()
			core_push.apply( ret, elems.get() );
		}

		return this.pushStack( ret );
	};
});

function getAll( context, tag ) {
	var elems, elem,
		i = 0,
		found = typeof context.getElementsByTagName !== core_strundefined ? context.getElementsByTagName( tag || "*" ) :
			typeof context.querySelectorAll !== core_strundefined ? context.querySelectorAll( tag || "*" ) :
			undefined;

	if ( !found ) {
		for ( found = [], elems = context.childNodes || context; (elem = elems[i]) != null; i++ ) {
			if ( !tag || jQuery.nodeName( elem, tag ) ) {
				found.push( elem );
			} else {
				jQuery.merge( found, getAll( elem, tag ) );
			}
		}
	}

	return tag === undefined || tag && jQuery.nodeName( context, tag ) ?
		jQuery.merge( [ context ], found ) :
		found;
}

// Used in buildFragment, fixes the defaultChecked property
function fixDefaultChecked( elem ) {
	if ( manipulation_rcheckableType.test( elem.type ) ) {
		elem.defaultChecked = elem.checked;
	}
}

jQuery.extend({
	clone: function( elem, dataAndEvents, deepDataAndEvents ) {
		var destElements, node, clone, i, srcElements,
			inPage = jQuery.contains( elem.ownerDocument, elem );

		if ( jQuery.support.html5Clone || jQuery.isXMLDoc(elem) || !rnoshimcache.test( "<" + elem.nodeName + ">" ) ) {
			clone = elem.cloneNode( true );

		// IE<=8 does not properly clone detached, unknown element nodes
		} else {
			fragmentDiv.innerHTML = elem.outerHTML;
			fragmentDiv.removeChild( clone = fragmentDiv.firstChild );
		}

		if ( (!jQuery.support.noCloneEvent || !jQuery.support.noCloneChecked) &&
				(elem.nodeType === 1 || elem.nodeType === 11) && !jQuery.isXMLDoc(elem) ) {

			// We eschew Sizzle here for performance reasons: http://jsperf.com/getall-vs-sizzle/2
			destElements = getAll( clone );
			srcElements = getAll( elem );

			// Fix all IE cloning issues
			for ( i = 0; (node = srcElements[i]) != null; ++i ) {
				// Ensure that the destination node is not null; Fixes #9587
				if ( destElements[i] ) {
					fixCloneNodeIssues( node, destElements[i] );
				}
			}
		}

		// Copy the events from the original to the clone
		if ( dataAndEvents ) {
			if ( deepDataAndEvents ) {
				srcElements = srcElements || getAll( elem );
				destElements = destElements || getAll( clone );

				for ( i = 0; (node = srcElements[i]) != null; i++ ) {
					cloneCopyEvent( node, destElements[i] );
				}
			} else {
				cloneCopyEvent( elem, clone );
			}
		}

		// Preserve script evaluation history
		destElements = getAll( clone, "script" );
		if ( destElements.length > 0 ) {
			setGlobalEval( destElements, !inPage && getAll( elem, "script" ) );
		}

		destElements = srcElements = node = null;

		// Return the cloned set
		return clone;
	},

	buildFragment: function( elems, context, scripts, selection ) {
		var j, elem, contains,
			tmp, tag, tbody, wrap,
			l = elems.length,

			// Ensure a safe fragment
			safe = createSafeFragment( context ),

			nodes = [],
			i = 0;

		for ( ; i < l; i++ ) {
			elem = elems[ i ];

			if ( elem || elem === 0 ) {

				// Add nodes directly
				if ( jQuery.type( elem ) === "object" ) {
					jQuery.merge( nodes, elem.nodeType ? [ elem ] : elem );

				// Convert non-html into a text node
				} else if ( !rhtml.test( elem ) ) {
					nodes.push( context.createTextNode( elem ) );

				// Convert html into DOM nodes
				} else {
					tmp = tmp || safe.appendChild( context.createElement("div") );

					// Deserialize a standard representation
					tag = ( rtagName.exec( elem ) || ["", ""] )[1].toLowerCase();
					wrap = wrapMap[ tag ] || wrapMap._default;

					tmp.innerHTML = wrap[1] + elem.replace( rxhtmlTag, "<$1></$2>" ) + wrap[2];

					// Descend through wrappers to the right content
					j = wrap[0];
					while ( j-- ) {
						tmp = tmp.lastChild;
					}

					// Manually add leading whitespace removed by IE
					if ( !jQuery.support.leadingWhitespace && rleadingWhitespace.test( elem ) ) {
						nodes.push( context.createTextNode( rleadingWhitespace.exec( elem )[0] ) );
					}

					// Remove IE's autoinserted <tbody> from table fragments
					if ( !jQuery.support.tbody ) {

						// String was a <table>, *may* have spurious <tbody>
						elem = tag === "table" && !rtbody.test( elem ) ?
							tmp.firstChild :

							// String was a bare <thead> or <tfoot>
							wrap[1] === "<table>" && !rtbody.test( elem ) ?
								tmp :
								0;

						j = elem && elem.childNodes.length;
						while ( j-- ) {
							if ( jQuery.nodeName( (tbody = elem.childNodes[j]), "tbody" ) && !tbody.childNodes.length ) {
								elem.removeChild( tbody );
							}
						}
					}

					jQuery.merge( nodes, tmp.childNodes );

					// Fix #12392 for WebKit and IE > 9
					tmp.textContent = "";

					// Fix #12392 for oldIE
					while ( tmp.firstChild ) {
						tmp.removeChild( tmp.firstChild );
					}

					// Remember the top-level container for proper cleanup
					tmp = safe.lastChild;
				}
			}
		}

		// Fix #11356: Clear elements from fragment
		if ( tmp ) {
			safe.removeChild( tmp );
		}

		// Reset defaultChecked for any radios and checkboxes
		// about to be appended to the DOM in IE 6/7 (#8060)
		if ( !jQuery.support.appendChecked ) {
			jQuery.grep( getAll( nodes, "input" ), fixDefaultChecked );
		}

		i = 0;
		while ( (elem = nodes[ i++ ]) ) {

			// #4087 - If origin and destination elements are the same, and this is
			// that element, do not do anything
			if ( selection && jQuery.inArray( elem, selection ) !== -1 ) {
				continue;
			}

			contains = jQuery.contains( elem.ownerDocument, elem );

			// Append to fragment
			tmp = getAll( safe.appendChild( elem ), "script" );

			// Preserve script evaluation history
			if ( contains ) {
				setGlobalEval( tmp );
			}

			// Capture executables
			if ( scripts ) {
				j = 0;
				while ( (elem = tmp[ j++ ]) ) {
					if ( rscriptType.test( elem.type || "" ) ) {
						scripts.push( elem );
					}
				}
			}
		}

		tmp = null;

		return safe;
	},

	cleanData: function( elems, /* internal */ acceptData ) {
		var elem, type, id, data,
			i = 0,
			internalKey = jQuery.expando,
			cache = jQuery.cache,
			deleteExpando = jQuery.support.deleteExpando,
			special = jQuery.event.special;

		for ( ; (elem = elems[i]) != null; i++ ) {

			if ( acceptData || jQuery.acceptData( elem ) ) {

				id = elem[ internalKey ];
				data = id && cache[ id ];

				if ( data ) {
					if ( data.events ) {
						for ( type in data.events ) {
							if ( special[ type ] ) {
								jQuery.event.remove( elem, type );

							// This is a shortcut to avoid jQuery.event.remove's overhead
							} else {
								jQuery.removeEvent( elem, type, data.handle );
							}
						}
					}

					// Remove cache only if it was not already removed by jQuery.event.remove
					if ( cache[ id ] ) {

						delete cache[ id ];

						// IE does not allow us to delete expando properties from nodes,
						// nor does it have a removeAttribute function on Document nodes;
						// we must handle all of these cases
						if ( deleteExpando ) {
							delete elem[ internalKey ];

						} else if ( typeof elem.removeAttribute !== core_strundefined ) {
							elem.removeAttribute( internalKey );

						} else {
							elem[ internalKey ] = null;
						}

						core_deletedIds.push( id );
					}
				}
			}
		}
	},

	_evalUrl: function( url ) {
		return jQuery.ajax({
			url: url,
			type: "GET",
			dataType: "script",
			async: false,
			global: false,
			"throws": true
		});
	}
});
jQuery.fn.extend({
	wrapAll: function( html ) {
		if ( jQuery.isFunction( html ) ) {
			return this.each(function(i) {
				jQuery(this).wrapAll( html.call(this, i) );
			});
		}

		if ( this[0] ) {
			// The elements to wrap the target around
			var wrap = jQuery( html, this[0].ownerDocument ).eq(0).clone(true);

			if ( this[0].parentNode ) {
				wrap.insertBefore( this[0] );
			}

			wrap.map(function() {
				var elem = this;

				while ( elem.firstChild && elem.firstChild.nodeType === 1 ) {
					elem = elem.firstChild;
				}

				return elem;
			}).append( this );
		}

		return this;
	},

	wrapInner: function( html ) {
		if ( jQuery.isFunction( html ) ) {
			return this.each(function(i) {
				jQuery(this).wrapInner( html.call(this, i) );
			});
		}

		return this.each(function() {
			var self = jQuery( this ),
				contents = self.contents();

			if ( contents.length ) {
				contents.wrapAll( html );

			} else {
				self.append( html );
			}
		});
	},

	wrap: function( html ) {
		var isFunction = jQuery.isFunction( html );

		return this.each(function(i) {
			jQuery( this ).wrapAll( isFunction ? html.call(this, i) : html );
		});
	},

	unwrap: function() {
		return this.parent().each(function() {
			if ( !jQuery.nodeName( this, "body" ) ) {
				jQuery( this ).replaceWith( this.childNodes );
			}
		}).end();
	}
});
var iframe, getStyles, curCSS,
	ralpha = /alpha\([^)]*\)/i,
	ropacity = /opacity\s*=\s*([^)]*)/,
	rposition = /^(top|right|bottom|left)$/,
	// swappable if display is none or starts with table except "table", "table-cell", or "table-caption"
	// see here for display values: https://developer.mozilla.org/en-US/docs/CSS/display
	rdisplayswap = /^(none|table(?!-c[ea]).+)/,
	rmargin = /^margin/,
	rnumsplit = new RegExp( "^(" + core_pnum + ")(.*)$", "i" ),
	rnumnonpx = new RegExp( "^(" + core_pnum + ")(?!px)[a-z%]+$", "i" ),
	rrelNum = new RegExp( "^([+-])=(" + core_pnum + ")", "i" ),
	elemdisplay = { BODY: "block" },

	cssShow = { position: "absolute", visibility: "hidden", display: "block" },
	cssNormalTransform = {
		letterSpacing: 0,
		fontWeight: 400
	},

	cssExpand = [ "Top", "Right", "Bottom", "Left" ],
	cssPrefixes = [ "Webkit", "O", "Moz", "ms" ];

// return a css property mapped to a potentially vendor prefixed property
function vendorPropName( style, name ) {

	// shortcut for names that are not vendor prefixed
	if ( name in style ) {
		return name;
	}

	// check for vendor prefixed names
	var capName = name.charAt(0).toUpperCase() + name.slice(1),
		origName = name,
		i = cssPrefixes.length;

	while ( i-- ) {
		name = cssPrefixes[ i ] + capName;
		if ( name in style ) {
			return name;
		}
	}

	return origName;
}

function isHidden( elem, el ) {
	// isHidden might be called from jQuery#filter function;
	// in that case, element will be second argument
	elem = el || elem;
	return jQuery.css( elem, "display" ) === "none" || !jQuery.contains( elem.ownerDocument, elem );
}

function showHide( elements, show ) {
	var display, elem, hidden,
		values = [],
		index = 0,
		length = elements.length;

	for ( ; index < length; index++ ) {
		elem = elements[ index ];
		if ( !elem.style ) {
			continue;
		}

		values[ index ] = jQuery._data( elem, "olddisplay" );
		display = elem.style.display;
		if ( show ) {
			// Reset the inline display of this element to learn if it is
			// being hidden by cascaded rules or not
			if ( !values[ index ] && display === "none" ) {
				elem.style.display = "";
			}

			// Set elements which have been overridden with display: none
			// in a stylesheet to whatever the default browser style is
			// for such an element
			if ( elem.style.display === "" && isHidden( elem ) ) {
				values[ index ] = jQuery._data( elem, "olddisplay", css_defaultDisplay(elem.nodeName) );
			}
		} else {

			if ( !values[ index ] ) {
				hidden = isHidden( elem );

				if ( display && display !== "none" || !hidden ) {
					jQuery._data( elem, "olddisplay", hidden ? display : jQuery.css( elem, "display" ) );
				}
			}
		}
	}

	// Set the display of most of the elements in a second loop
	// to avoid the constant reflow
	for ( index = 0; index < length; index++ ) {
		elem = elements[ index ];
		if ( !elem.style ) {
			continue;
		}
		if ( !show || elem.style.display === "none" || elem.style.display === "" ) {
			elem.style.display = show ? values[ index ] || "" : "none";
		}
	}

	return elements;
}

jQuery.fn.extend({
	css: function( name, value ) {
		return jQuery.access( this, function( elem, name, value ) {
			var len, styles,
				map = {},
				i = 0;

			if ( jQuery.isArray( name ) ) {
				styles = getStyles( elem );
				len = name.length;

				for ( ; i < len; i++ ) {
					map[ name[ i ] ] = jQuery.css( elem, name[ i ], false, styles );
				}

				return map;
			}

			return value !== undefined ?
				jQuery.style( elem, name, value ) :
				jQuery.css( elem, name );
		}, name, value, arguments.length > 1 );
	},
	show: function() {
		return showHide( this, true );
	},
	hide: function() {
		return showHide( this );
	},
	toggle: function( state ) {
		if ( typeof state === "boolean" ) {
			return state ? this.show() : this.hide();
		}

		return this.each(function() {
			if ( isHidden( this ) ) {
				jQuery( this ).show();
			} else {
				jQuery( this ).hide();
			}
		});
	}
});

jQuery.extend({
	// Add in style property hooks for overriding the default
	// behavior of getting and setting a style property
	cssHooks: {
		opacity: {
			get: function( elem, computed ) {
				if ( computed ) {
					// We should always get a number back from opacity
					var ret = curCSS( elem, "opacity" );
					return ret === "" ? "1" : ret;
				}
			}
		}
	},

	// Don't automatically add "px" to these possibly-unitless properties
	cssNumber: {
		"columnCount": true,
		"fillOpacity": true,
		"fontWeight": true,
		"lineHeight": true,
		"opacity": true,
		"order": true,
		"orphans": true,
		"widows": true,
		"zIndex": true,
		"zoom": true
	},

	// Add in properties whose names you wish to fix before
	// setting or getting the value
	cssProps: {
		// normalize float css property
		"float": jQuery.support.cssFloat ? "cssFloat" : "styleFloat"
	},

	// Get and set the style property on a DOM Node
	style: function( elem, name, value, extra ) {
		// Don't set styles on text and comment nodes
		if ( !elem || elem.nodeType === 3 || elem.nodeType === 8 || !elem.style ) {
			return;
		}

		// Make sure that we're working with the right name
		var ret, type, hooks,
			origName = jQuery.camelCase( name ),
			style = elem.style;

		name = jQuery.cssProps[ origName ] || ( jQuery.cssProps[ origName ] = vendorPropName( style, origName ) );

		// gets hook for the prefixed version
		// followed by the unprefixed version
		hooks = jQuery.cssHooks[ name ] || jQuery.cssHooks[ origName ];

		// Check if we're setting a value
		if ( value !== undefined ) {
			type = typeof value;

			// convert relative number strings (+= or -=) to relative numbers. #7345
			if ( type === "string" && (ret = rrelNum.exec( value )) ) {
				value = ( ret[1] + 1 ) * ret[2] + parseFloat( jQuery.css( elem, name ) );
				// Fixes bug #9237
				type = "number";
			}

			// Make sure that NaN and null values aren't set. See: #7116
			if ( value == null || type === "number" && isNaN( value ) ) {
				return;
			}

			// If a number was passed in, add 'px' to the (except for certain CSS properties)
			if ( type === "number" && !jQuery.cssNumber[ origName ] ) {
				value += "px";
			}

			// Fixes #8908, it can be done more correctly by specifing setters in cssHooks,
			// but it would mean to define eight (for every problematic property) identical functions
			if ( !jQuery.support.clearCloneStyle && value === "" && name.indexOf("background") === 0 ) {
				style[ name ] = "inherit";
			}

			// If a hook was provided, use that value, otherwise just set the specified value
			if ( !hooks || !("set" in hooks) || (value = hooks.set( elem, value, extra )) !== undefined ) {

				// Wrapped to prevent IE from throwing errors when 'invalid' values are provided
				// Fixes bug #5509
				try {
					style[ name ] = value;
				} catch(e) {}
			}

		} else {
			// If a hook was provided get the non-computed value from there
			if ( hooks && "get" in hooks && (ret = hooks.get( elem, false, extra )) !== undefined ) {
				return ret;
			}

			// Otherwise just get the value from the style object
			return style[ name ];
		}
	},

	css: function( elem, name, extra, styles ) {
		var num, val, hooks,
			origName = jQuery.camelCase( name );

		// Make sure that we're working with the right name
		name = jQuery.cssProps[ origName ] || ( jQuery.cssProps[ origName ] = vendorPropName( elem.style, origName ) );

		// gets hook for the prefixed version
		// followed by the unprefixed version
		hooks = jQuery.cssHooks[ name ] || jQuery.cssHooks[ origName ];

		// If a hook was provided get the computed value from there
		if ( hooks && "get" in hooks ) {
			val = hooks.get( elem, true, extra );
		}

		// Otherwise, if a way to get the computed value exists, use that
		if ( val === undefined ) {
			val = curCSS( elem, name, styles );
		}

		//convert "normal" to computed value
		if ( val === "normal" && name in cssNormalTransform ) {
			val = cssNormalTransform[ name ];
		}

		// Return, converting to number if forced or a qualifier was provided and val looks numeric
		if ( extra === "" || extra ) {
			num = parseFloat( val );
			return extra === true || jQuery.isNumeric( num ) ? num || 0 : val;
		}
		return val;
	}
});

// NOTE: we've included the "window" in window.getComputedStyle
// because jsdom on node.js will break without it.
if ( window.getComputedStyle ) {
	getStyles = function( elem ) {
		return window.getComputedStyle( elem, null );
	};

	curCSS = function( elem, name, _computed ) {
		var width, minWidth, maxWidth,
			computed = _computed || getStyles( elem ),

			// getPropertyValue is only needed for .css('filter') in IE9, see #12537
			ret = computed ? computed.getPropertyValue( name ) || computed[ name ] : undefined,
			style = elem.style;

		if ( computed ) {

			if ( ret === "" && !jQuery.contains( elem.ownerDocument, elem ) ) {
				ret = jQuery.style( elem, name );
			}

			// A tribute to the "awesome hack by Dean Edwards"
			// Chrome < 17 and Safari 5.0 uses "computed value" instead of "used value" for margin-right
			// Safari 5.1.7 (at least) returns percentage for a larger set of values, but width seems to be reliably pixels
			// this is against the CSSOM draft spec: http://dev.w3.org/csswg/cssom/#resolved-values
			if ( rnumnonpx.test( ret ) && rmargin.test( name ) ) {

				// Remember the original values
				width = style.width;
				minWidth = style.minWidth;
				maxWidth = style.maxWidth;

				// Put in the new values to get a computed value out
				style.minWidth = style.maxWidth = style.width = ret;
				ret = computed.width;

				// Revert the changed values
				style.width = width;
				style.minWidth = minWidth;
				style.maxWidth = maxWidth;
			}
		}

		return ret;
	};
} else if ( document.documentElement.currentStyle ) {
	getStyles = function( elem ) {
		return elem.currentStyle;
	};

	curCSS = function( elem, name, _computed ) {
		var left, rs, rsLeft,
			computed = _computed || getStyles( elem ),
			ret = computed ? computed[ name ] : undefined,
			style = elem.style;

		// Avoid setting ret to empty string here
		// so we don't default to auto
		if ( ret == null && style && style[ name ] ) {
			ret = style[ name ];
		}

		// From the awesome hack by Dean Edwards
		// http://erik.eae.net/archives/2007/07/27/18.54.15/#comment-102291

		// If we're not dealing with a regular pixel number
		// but a number that has a weird ending, we need to convert it to pixels
		// but not position css attributes, as those are proportional to the parent element instead
		// and we can't measure the parent instead because it might trigger a "stacking dolls" problem
		if ( rnumnonpx.test( ret ) && !rposition.test( name ) ) {

			// Remember the original values
			left = style.left;
			rs = elem.runtimeStyle;
			rsLeft = rs && rs.left;

			// Put in the new values to get a computed value out
			if ( rsLeft ) {
				rs.left = elem.currentStyle.left;
			}
			style.left = name === "fontSize" ? "1em" : ret;
			ret = style.pixelLeft + "px";

			// Revert the changed values
			style.left = left;
			if ( rsLeft ) {
				rs.left = rsLeft;
			}
		}

		return ret === "" ? "auto" : ret;
	};
}

function setPositiveNumber( elem, value, subtract ) {
	var matches = rnumsplit.exec( value );
	return matches ?
		// Guard against undefined "subtract", e.g., when used as in cssHooks
		Math.max( 0, matches[ 1 ] - ( subtract || 0 ) ) + ( matches[ 2 ] || "px" ) :
		value;
}

function augmentWidthOrHeight( elem, name, extra, isBorderBox, styles ) {
	var i = extra === ( isBorderBox ? "border" : "content" ) ?
		// If we already have the right measurement, avoid augmentation
		4 :
		// Otherwise initialize for horizontal or vertical properties
		name === "width" ? 1 : 0,

		val = 0;

	for ( ; i < 4; i += 2 ) {
		// both box models exclude margin, so add it if we want it
		if ( extra === "margin" ) {
			val += jQuery.css( elem, extra + cssExpand[ i ], true, styles );
		}

		if ( isBorderBox ) {
			// border-box includes padding, so remove it if we want content
			if ( extra === "content" ) {
				val -= jQuery.css( elem, "padding" + cssExpand[ i ], true, styles );
			}

			// at this point, extra isn't border nor margin, so remove border
			if ( extra !== "margin" ) {
				val -= jQuery.css( elem, "border" + cssExpand[ i ] + "Width", true, styles );
			}
		} else {
			// at this point, extra isn't content, so add padding
			val += jQuery.css( elem, "padding" + cssExpand[ i ], true, styles );

			// at this point, extra isn't content nor padding, so add border
			if ( extra !== "padding" ) {
				val += jQuery.css( elem, "border" + cssExpand[ i ] + "Width", true, styles );
			}
		}
	}

	return val;
}

function getWidthOrHeight( elem, name, extra ) {

	// Start with offset property, which is equivalent to the border-box value
	var valueIsBorderBox = true,
		val = name === "width" ? elem.offsetWidth : elem.offsetHeight,
		styles = getStyles( elem ),
		isBorderBox = jQuery.support.boxSizing && jQuery.css( elem, "boxSizing", false, styles ) === "border-box";

	// some non-html elements return undefined for offsetWidth, so check for null/undefined
	// svg - https://bugzilla.mozilla.org/show_bug.cgi?id=649285
	// MathML - https://bugzilla.mozilla.org/show_bug.cgi?id=491668
	if ( val <= 0 || val == null ) {
		// Fall back to computed then uncomputed css if necessary
		val = curCSS( elem, name, styles );
		if ( val < 0 || val == null ) {
			val = elem.style[ name ];
		}

		// Computed unit is not pixels. Stop here and return.
		if ( rnumnonpx.test(val) ) {
			return val;
		}

		// we need the check for style in case a browser which returns unreliable values
		// for getComputedStyle silently falls back to the reliable elem.style
		valueIsBorderBox = isBorderBox && ( jQuery.support.boxSizingReliable || val === elem.style[ name ] );

		// Normalize "", auto, and prepare for extra
		val = parseFloat( val ) || 0;
	}

	// use the active box-sizing model to add/subtract irrelevant styles
	return ( val +
		augmentWidthOrHeight(
			elem,
			name,
			extra || ( isBorderBox ? "border" : "content" ),
			valueIsBorderBox,
			styles
		)
	) + "px";
}

// Try to determine the default display value of an element
function css_defaultDisplay( nodeName ) {
	var doc = document,
		display = elemdisplay[ nodeName ];

	if ( !display ) {
		display = actualDisplay( nodeName, doc );

		// If the simple way fails, read from inside an iframe
		if ( display === "none" || !display ) {
			// Use the already-created iframe if possible
			iframe = ( iframe ||
				jQuery("<iframe frameborder='0' width='0' height='0'/>")
				.css( "cssText", "display:block !important" )
			).appendTo( doc.documentElement );

			// Always write a new HTML skeleton so Webkit and Firefox don't choke on reuse
			doc = ( iframe[0].contentWindow || iframe[0].contentDocument ).document;
			doc.write("<!doctype html><html><body>");
			doc.close();

			display = actualDisplay( nodeName, doc );
			iframe.detach();
		}

		// Store the correct default display
		elemdisplay[ nodeName ] = display;
	}

	return display;
}

// Called ONLY from within css_defaultDisplay
function actualDisplay( name, doc ) {
	var elem = jQuery( doc.createElement( name ) ).appendTo( doc.body ),
		display = jQuery.css( elem[0], "display" );
	elem.remove();
	return display;
}

jQuery.each([ "height", "width" ], function( i, name ) {
	jQuery.cssHooks[ name ] = {
		get: function( elem, computed, extra ) {
			if ( computed ) {
				// certain elements can have dimension info if we invisibly show them
				// however, it must have a current display style that would benefit from this
				return elem.offsetWidth === 0 && rdisplayswap.test( jQuery.css( elem, "display" ) ) ?
					jQuery.swap( elem, cssShow, function() {
						return getWidthOrHeight( elem, name, extra );
					}) :
					getWidthOrHeight( elem, name, extra );
			}
		},

		set: function( elem, value, extra ) {
			var styles = extra && getStyles( elem );
			return setPositiveNumber( elem, value, extra ?
				augmentWidthOrHeight(
					elem,
					name,
					extra,
					jQuery.support.boxSizing && jQuery.css( elem, "boxSizing", false, styles ) === "border-box",
					styles
				) : 0
			);
		}
	};
});

if ( !jQuery.support.opacity ) {
	jQuery.cssHooks.opacity = {
		get: function( elem, computed ) {
			// IE uses filters for opacity
			return ropacity.test( (computed && elem.currentStyle ? elem.currentStyle.filter : elem.style.filter) || "" ) ?
				( 0.01 * parseFloat( RegExp.$1 ) ) + "" :
				computed ? "1" : "";
		},

		set: function( elem, value ) {
			var style = elem.style,
				currentStyle = elem.currentStyle,
				opacity = jQuery.isNumeric( value ) ? "alpha(opacity=" + value * 100 + ")" : "",
				filter = currentStyle && currentStyle.filter || style.filter || "";

			// IE has trouble with opacity if it does not have layout
			// Force it by setting the zoom level
			style.zoom = 1;

			// if setting opacity to 1, and no other filters exist - attempt to remove filter attribute #6652
			// if value === "", then remove inline opacity #12685
			if ( ( value >= 1 || value === "" ) &&
					jQuery.trim( filter.replace( ralpha, "" ) ) === "" &&
					style.removeAttribute ) {

				// Setting style.filter to null, "" & " " still leave "filter:" in the cssText
				// if "filter:" is present at all, clearType is disabled, we want to avoid this
				// style.removeAttribute is IE Only, but so apparently is this code path...
				style.removeAttribute( "filter" );

				// if there is no filter style applied in a css rule or unset inline opacity, we are done
				if ( value === "" || currentStyle && !currentStyle.filter ) {
					return;
				}
			}

			// otherwise, set new filter values
			style.filter = ralpha.test( filter ) ?
				filter.replace( ralpha, opacity ) :
				filter + " " + opacity;
		}
	};
}

// These hooks cannot be added until DOM ready because the support test
// for it is not run until after DOM ready
jQuery(function() {
	if ( !jQuery.support.reliableMarginRight ) {
		jQuery.cssHooks.marginRight = {
			get: function( elem, computed ) {
				if ( computed ) {
					// WebKit Bug 13343 - getComputedStyle returns wrong value for margin-right
					// Work around by temporarily setting element display to inline-block
					return jQuery.swap( elem, { "display": "inline-block" },
						curCSS, [ elem, "marginRight" ] );
				}
			}
		};
	}

	// Webkit bug: https://bugs.webkit.org/show_bug.cgi?id=29084
	// getComputedStyle returns percent when specified for top/left/bottom/right
	// rather than make the css module depend on the offset module, we just check for it here
	if ( !jQuery.support.pixelPosition && jQuery.fn.position ) {
		jQuery.each( [ "top", "left" ], function( i, prop ) {
			jQuery.cssHooks[ prop ] = {
				get: function( elem, computed ) {
					if ( computed ) {
						computed = curCSS( elem, prop );
						// if curCSS returns percentage, fallback to offset
						return rnumnonpx.test( computed ) ?
							jQuery( elem ).position()[ prop ] + "px" :
							computed;
					}
				}
			};
		});
	}

});

if ( jQuery.expr && jQuery.expr.filters ) {
	jQuery.expr.filters.hidden = function( elem ) {
		// Support: Opera <= 12.12
		// Opera reports offsetWidths and offsetHeights less than zero on some elements
		return elem.offsetWidth <= 0 && elem.offsetHeight <= 0 ||
			(!jQuery.support.reliableHiddenOffsets && ((elem.style && elem.style.display) || jQuery.css( elem, "display" )) === "none");
	};

	jQuery.expr.filters.visible = function( elem ) {
		return !jQuery.expr.filters.hidden( elem );
	};
}

// These hooks are used by animate to expand properties
jQuery.each({
	margin: "",
	padding: "",
	border: "Width"
}, function( prefix, suffix ) {
	jQuery.cssHooks[ prefix + suffix ] = {
		expand: function( value ) {
			var i = 0,
				expanded = {},

				// assumes a single number if not a string
				parts = typeof value === "string" ? value.split(" ") : [ value ];

			for ( ; i < 4; i++ ) {
				expanded[ prefix + cssExpand[ i ] + suffix ] =
					parts[ i ] || parts[ i - 2 ] || parts[ 0 ];
			}

			return expanded;
		}
	};

	if ( !rmargin.test( prefix ) ) {
		jQuery.cssHooks[ prefix + suffix ].set = setPositiveNumber;
	}
});
var r20 = /%20/g,
	rbracket = /\[\]$/,
	rCRLF = /\r?\n/g,
	rsubmitterTypes = /^(?:submit|button|image|reset|file)$/i,
	rsubmittable = /^(?:input|select|textarea|keygen)/i;

jQuery.fn.extend({
	serialize: function() {
		return jQuery.param( this.serializeArray() );
	},
	serializeArray: function() {
		return this.map(function(){
			// Can add propHook for "elements" to filter or add form elements
			var elements = jQuery.prop( this, "elements" );
			return elements ? jQuery.makeArray( elements ) : this;
		})
		.filter(function(){
			var type = this.type;
			// Use .is(":disabled") so that fieldset[disabled] works
			return this.name && !jQuery( this ).is( ":disabled" ) &&
				rsubmittable.test( this.nodeName ) && !rsubmitterTypes.test( type ) &&
				( this.checked || !manipulation_rcheckableType.test( type ) );
		})
		.map(function( i, elem ){
			var val = jQuery( this ).val();

			return val == null ?
				null :
				jQuery.isArray( val ) ?
					jQuery.map( val, function( val ){
						return { name: elem.name, value: val.replace( rCRLF, "\r\n" ) };
					}) :
					{ name: elem.name, value: val.replace( rCRLF, "\r\n" ) };
		}).get();
	}
});

//Serialize an array of form elements or a set of
//key/values into a query string
jQuery.param = function( a, traditional ) {
	var prefix,
		s = [],
		add = function( key, value ) {
			// If value is a function, invoke it and return its value
			value = jQuery.isFunction( value ) ? value() : ( value == null ? "" : value );
			s[ s.length ] = encodeURIComponent( key ) + "=" + encodeURIComponent( value );
		};

	// Set traditional to true for jQuery <= 1.3.2 behavior.
	if ( traditional === undefined ) {
		traditional = jQuery.ajaxSettings && jQuery.ajaxSettings.traditional;
	}

	// If an array was passed in, assume that it is an array of form elements.
	if ( jQuery.isArray( a ) || ( a.jquery && !jQuery.isPlainObject( a ) ) ) {
		// Serialize the form elements
		jQuery.each( a, function() {
			add( this.name, this.value );
		});

	} else {
		// If traditional, encode the "old" way (the way 1.3.2 or older
		// did it), otherwise encode params recursively.
		for ( prefix in a ) {
			buildParams( prefix, a[ prefix ], traditional, add );
		}
	}

	// Return the resulting serialization
	return s.join( "&" ).replace( r20, "+" );
};

function buildParams( prefix, obj, traditional, add ) {
	var name;

	if ( jQuery.isArray( obj ) ) {
		// Serialize array item.
		jQuery.each( obj, function( i, v ) {
			if ( traditional || rbracket.test( prefix ) ) {
				// Treat each array item as a scalar.
				add( prefix, v );

			} else {
				// Item is non-scalar (array or object), encode its numeric index.
				buildParams( prefix + "[" + ( typeof v === "object" ? i : "" ) + "]", v, traditional, add );
			}
		});

	} else if ( !traditional && jQuery.type( obj ) === "object" ) {
		// Serialize object item.
		for ( name in obj ) {
			buildParams( prefix + "[" + name + "]", obj[ name ], traditional, add );
		}

	} else {
		// Serialize scalar item.
		add( prefix, obj );
	}
}
jQuery.each( ("blur focus focusin focusout load resize scroll unload click dblclick " +
	"mousedown mouseup mousemove mouseover mouseout mouseenter mouseleave " +
	"change select submit keydown keypress keyup error contextmenu").split(" "), function( i, name ) {

	// Handle event binding
	jQuery.fn[ name ] = function( data, fn ) {
		return arguments.length > 0 ?
			this.on( name, null, data, fn ) :
			this.trigger( name );
	};
});

jQuery.fn.extend({
	hover: function( fnOver, fnOut ) {
		return this.mouseenter( fnOver ).mouseleave( fnOut || fnOver );
	},

	bind: function( types, data, fn ) {
		return this.on( types, null, data, fn );
	},
	unbind: function( types, fn ) {
		return this.off( types, null, fn );
	},

	delegate: function( selector, types, data, fn ) {
		return this.on( types, selector, data, fn );
	},
	undelegate: function( selector, types, fn ) {
		// ( namespace ) or ( selector, types [, fn] )
		return arguments.length === 1 ? this.off( selector, "**" ) : this.off( types, selector || "**", fn );
	}
});
var
	// Document location
	ajaxLocParts,
	ajaxLocation,
	ajax_nonce = jQuery.now(),

	ajax_rquery = /\?/,
	rhash = /#.*$/,
	rts = /([?&])_=[^&]*/,
	rheaders = /^(.*?):[ \t]*([^\r\n]*)\r?$/mg, // IE leaves an \r character at EOL
	// #7653, #8125, #8152: local protocol detection
	rlocalProtocol = /^(?:about|app|app-storage|.+-extension|file|res|widget):$/,
	rnoContent = /^(?:GET|HEAD)$/,
	rprotocol = /^\/\//,
	rurl = /^([\w.+-]+:)(?:\/\/([^\/?#:]*)(?::(\d+)|)|)/,

	// Keep a copy of the old load method
	_load = jQuery.fn.load,

	/* Prefilters
	 * 1) They are useful to introduce custom dataTypes (see ajax/jsonp.js for an example)
	 * 2) These are called:
	 *    - BEFORE asking for a transport
	 *    - AFTER param serialization (s.data is a string if s.processData is true)
	 * 3) key is the dataType
	 * 4) the catchall symbol "*" can be used
	 * 5) execution will start with transport dataType and THEN continue down to "*" if needed
	 */
	prefilters = {},

	/* Transports bindings
	 * 1) key is the dataType
	 * 2) the catchall symbol "*" can be used
	 * 3) selection will start with transport dataType and THEN go to "*" if needed
	 */
	transports = {},

	// Avoid comment-prolog char sequence (#10098); must appease lint and evade compression
	allTypes = "*/".concat("*");

// #8138, IE may throw an exception when accessing
// a field from window.location if document.domain has been set
try {
	ajaxLocation = location.href;
} catch( e ) {
	// Use the href attribute of an A element
	// since IE will modify it given document.location
	ajaxLocation = document.createElement( "a" );
	ajaxLocation.href = "";
	ajaxLocation = ajaxLocation.href;
}

// Segment location into parts
ajaxLocParts = rurl.exec( ajaxLocation.toLowerCase() ) || [];

// Base "constructor" for jQuery.ajaxPrefilter and jQuery.ajaxTransport
function addToPrefiltersOrTransports( structure ) {

	// dataTypeExpression is optional and defaults to "*"
	return function( dataTypeExpression, func ) {

		if ( typeof dataTypeExpression !== "string" ) {
			func = dataTypeExpression;
			dataTypeExpression = "*";
		}

		var dataType,
			i = 0,
			dataTypes = dataTypeExpression.toLowerCase().match( core_rnotwhite ) || [];

		if ( jQuery.isFunction( func ) ) {
			// For each dataType in the dataTypeExpression
			while ( (dataType = dataTypes[i++]) ) {
				// Prepend if requested
				if ( dataType[0] === "+" ) {
					dataType = dataType.slice( 1 ) || "*";
					(structure[ dataType ] = structure[ dataType ] || []).unshift( func );

				// Otherwise append
				} else {
					(structure[ dataType ] = structure[ dataType ] || []).push( func );
				}
			}
		}
	};
}

// Base inspection function for prefilters and transports
function inspectPrefiltersOrTransports( structure, options, originalOptions, jqXHR ) {

	var inspected = {},
		seekingTransport = ( structure === transports );

	function inspect( dataType ) {
		var selected;
		inspected[ dataType ] = true;
		jQuery.each( structure[ dataType ] || [], function( _, prefilterOrFactory ) {
			var dataTypeOrTransport = prefilterOrFactory( options, originalOptions, jqXHR );
			if( typeof dataTypeOrTransport === "string" && !seekingTransport && !inspected[ dataTypeOrTransport ] ) {
				options.dataTypes.unshift( dataTypeOrTransport );
				inspect( dataTypeOrTransport );
				return false;
			} else if ( seekingTransport ) {
				return !( selected = dataTypeOrTransport );
			}
		});
		return selected;
	}

	return inspect( options.dataTypes[ 0 ] ) || !inspected[ "*" ] && inspect( "*" );
}

// A special extend for ajax options
// that takes "flat" options (not to be deep extended)
// Fixes #9887
function ajaxExtend( target, src ) {
	var deep, key,
		flatOptions = jQuery.ajaxSettings.flatOptions || {};

	for ( key in src ) {
		if ( src[ key ] !== undefined ) {
			( flatOptions[ key ] ? target : ( deep || (deep = {}) ) )[ key ] = src[ key ];
		}
	}
	if ( deep ) {
		jQuery.extend( true, target, deep );
	}

	return target;
}

jQuery.fn.load = function( url, params, callback ) {
	if ( typeof url !== "string" && _load ) {
		return _load.apply( this, arguments );
	}

	var selector, response, type,
		self = this,
		off = url.indexOf(" ");

	if ( off >= 0 ) {
		selector = url.slice( off, url.length );
		url = url.slice( 0, off );
	}

	// If it's a function
	if ( jQuery.isFunction( params ) ) {

		// We assume that it's the callback
		callback = params;
		params = undefined;

	// Otherwise, build a param string
	} else if ( params && typeof params === "object" ) {
		type = "POST";
	}

	// If we have elements to modify, make the request
	if ( self.length > 0 ) {
		jQuery.ajax({
			url: url,

			// if "type" variable is undefined, then "GET" method will be used
			type: type,
			dataType: "html",
			data: params
		}).done(function( responseText ) {

			// Save response for use in complete callback
			response = arguments;

			self.html( selector ?

				// If a selector was specified, locate the right elements in a dummy div
				// Exclude scripts to avoid IE 'Permission Denied' errors
				jQuery("<div>").append( jQuery.parseHTML( responseText ) ).find( selector ) :

				// Otherwise use the full result
				responseText );

		}).complete( callback && function( jqXHR, status ) {
			self.each( callback, response || [ jqXHR.responseText, status, jqXHR ] );
		});
	}

	return this;
};

// Attach a bunch of functions for handling common AJAX events
jQuery.each( [ "ajaxStart", "ajaxStop", "ajaxComplete", "ajaxError", "ajaxSuccess", "ajaxSend" ], function( i, type ){
	jQuery.fn[ type ] = function( fn ){
		return this.on( type, fn );
	};
});

jQuery.extend({

	// Counter for holding the number of active queries
	active: 0,

	// Last-Modified header cache for next request
	lastModified: {},
	etag: {},

	ajaxSettings: {
		url: ajaxLocation,
		type: "GET",
		isLocal: rlocalProtocol.test( ajaxLocParts[ 1 ] ),
		global: true,
		processData: true,
		async: true,
		contentType: "application/x-www-form-urlencoded; charset=UTF-8",
		/*
		timeout: 0,
		data: null,
		dataType: null,
		username: null,
		password: null,
		cache: null,
		throws: false,
		traditional: false,
		headers: {},
		*/

		accepts: {
			"*": allTypes,
			text: "text/plain",
			html: "text/html",
			xml: "application/xml, text/xml",
			json: "application/json, text/javascript"
		},

		contents: {
			xml: /xml/,
			html: /html/,
			json: /json/
		},

		responseFields: {
			xml: "responseXML",
			text: "responseText",
			json: "responseJSON"
		},

		// Data converters
		// Keys separate source (or catchall "*") and destination types with a single space
		converters: {

			// Convert anything to text
			"* text": String,

			// Text to html (true = no transformation)
			"text html": true,

			// Evaluate text as a json expression
			"text json": jQuery.parseJSON,

			// Parse text as xml
			"text xml": jQuery.parseXML
		},

		// For options that shouldn't be deep extended:
		// you can add your own custom options here if
		// and when you create one that shouldn't be
		// deep extended (see ajaxExtend)
		flatOptions: {
			url: true,
			context: true
		}
	},

	// Creates a full fledged settings object into target
	// with both ajaxSettings and settings fields.
	// If target is omitted, writes into ajaxSettings.
	ajaxSetup: function( target, settings ) {
		return settings ?

			// Building a settings object
			ajaxExtend( ajaxExtend( target, jQuery.ajaxSettings ), settings ) :

			// Extending ajaxSettings
			ajaxExtend( jQuery.ajaxSettings, target );
	},

	ajaxPrefilter: addToPrefiltersOrTransports( prefilters ),
	ajaxTransport: addToPrefiltersOrTransports( transports ),

	// Main method
	ajax: function( url, options ) {

		// If url is an object, simulate pre-1.5 signature
		if ( typeof url === "object" ) {
			options = url;
			url = undefined;
		}

		// Force options to be an object
		options = options || {};

		var // Cross-domain detection vars
			parts,
			// Loop variable
			i,
			// URL without anti-cache param
			cacheURL,
			// Response headers as string
			responseHeadersString,
			// timeout handle
			timeoutTimer,

			// To know if global events are to be dispatched
			fireGlobals,

			transport,
			// Response headers
			responseHeaders,
			// Create the final options object
			s = jQuery.ajaxSetup( {}, options ),
			// Callbacks context
			callbackContext = s.context || s,
			// Context for global events is callbackContext if it is a DOM node or jQuery collection
			globalEventContext = s.context && ( callbackContext.nodeType || callbackContext.jquery ) ?
				jQuery( callbackContext ) :
				jQuery.event,
			// Deferreds
			deferred = jQuery.Deferred(),
			completeDeferred = jQuery.Callbacks("once memory"),
			// Status-dependent callbacks
			statusCode = s.statusCode || {},
			// Headers (they are sent all at once)
			requestHeaders = {},
			requestHeadersNames = {},
			// The jqXHR state
			state = 0,
			// Default abort message
			strAbort = "canceled",
			// Fake xhr
			jqXHR = {
				readyState: 0,

				// Builds headers hashtable if needed
				getResponseHeader: function( key ) {
					var match;
					if ( state === 2 ) {
						if ( !responseHeaders ) {
							responseHeaders = {};
							while ( (match = rheaders.exec( responseHeadersString )) ) {
								responseHeaders[ match[1].toLowerCase() ] = match[ 2 ];
							}
						}
						match = responseHeaders[ key.toLowerCase() ];
					}
					return match == null ? null : match;
				},

				// Raw string
				getAllResponseHeaders: function() {
					return state === 2 ? responseHeadersString : null;
				},

				// Caches the header
				setRequestHeader: function( name, value ) {
					var lname = name.toLowerCase();
					if ( !state ) {
						name = requestHeadersNames[ lname ] = requestHeadersNames[ lname ] || name;
						requestHeaders[ name ] = value;
					}
					return this;
				},

				// Overrides response content-type header
				overrideMimeType: function( type ) {
					if ( !state ) {
						s.mimeType = type;
					}
					return this;
				},

				// Status-dependent callbacks
				statusCode: function( map ) {
					var code;
					if ( map ) {
						if ( state < 2 ) {
							for ( code in map ) {
								// Lazy-add the new callback in a way that preserves old ones
								statusCode[ code ] = [ statusCode[ code ], map[ code ] ];
							}
						} else {
							// Execute the appropriate callbacks
							jqXHR.always( map[ jqXHR.status ] );
						}
					}
					return this;
				},

				// Cancel the request
				abort: function( statusText ) {
					var finalText = statusText || strAbort;
					if ( transport ) {
						transport.abort( finalText );
					}
					done( 0, finalText );
					return this;
				}
			};

		// Attach deferreds
		deferred.promise( jqXHR ).complete = completeDeferred.add;
		jqXHR.success = jqXHR.done;
		jqXHR.error = jqXHR.fail;

		// Remove hash character (#7531: and string promotion)
		// Add protocol if not provided (#5866: IE7 issue with protocol-less urls)
		// Handle falsy url in the settings object (#10093: consistency with old signature)
		// We also use the url parameter if available
		s.url = ( ( url || s.url || ajaxLocation ) + "" ).replace( rhash, "" ).replace( rprotocol, ajaxLocParts[ 1 ] + "//" );

		// Alias method option to type as per ticket #12004
		s.type = options.method || options.type || s.method || s.type;

		// Extract dataTypes list
		s.dataTypes = jQuery.trim( s.dataType || "*" ).toLowerCase().match( core_rnotwhite ) || [""];

		// A cross-domain request is in order when we have a protocol:host:port mismatch
		if ( s.crossDomain == null ) {
			parts = rurl.exec( s.url.toLowerCase() );
			s.crossDomain = !!( parts &&
				( parts[ 1 ] !== ajaxLocParts[ 1 ] || parts[ 2 ] !== ajaxLocParts[ 2 ] ||
					( parts[ 3 ] || ( parts[ 1 ] === "http:" ? "80" : "443" ) ) !==
						( ajaxLocParts[ 3 ] || ( ajaxLocParts[ 1 ] === "http:" ? "80" : "443" ) ) )
			);
		}

		// Convert data if not already a string
		if ( s.data && s.processData && typeof s.data !== "string" ) {
			s.data = jQuery.param( s.data, s.traditional );
		}

		// Apply prefilters
		inspectPrefiltersOrTransports( prefilters, s, options, jqXHR );

		// If request was aborted inside a prefilter, stop there
		if ( state === 2 ) {
			return jqXHR;
		}

		// We can fire global events as of now if asked to
		fireGlobals = s.global;

		// Watch for a new set of requests
		if ( fireGlobals && jQuery.active++ === 0 ) {
			jQuery.event.trigger("ajaxStart");
		}

		// Uppercase the type
		s.type = s.type.toUpperCase();

		// Determine if request has content
		s.hasContent = !rnoContent.test( s.type );

		// Save the URL in case we're toying with the If-Modified-Since
		// and/or If-None-Match header later on
		cacheURL = s.url;

		// More options handling for requests with no content
		if ( !s.hasContent ) {

			// If data is available, append data to url
			if ( s.data ) {
				cacheURL = ( s.url += ( ajax_rquery.test( cacheURL ) ? "&" : "?" ) + s.data );
				// #9682: remove data so that it's not used in an eventual retry
				delete s.data;
			}

			// Add anti-cache in url if needed
			if ( s.cache === false ) {
				s.url = rts.test( cacheURL ) ?

					// If there is already a '_' parameter, set its value
					cacheURL.replace( rts, "$1_=" + ajax_nonce++ ) :

					// Otherwise add one to the end
					cacheURL + ( ajax_rquery.test( cacheURL ) ? "&" : "?" ) + "_=" + ajax_nonce++;
			}
		}

		// Set the If-Modified-Since and/or If-None-Match header, if in ifModified mode.
		if ( s.ifModified ) {
			if ( jQuery.lastModified[ cacheURL ] ) {
				jqXHR.setRequestHeader( "If-Modified-Since", jQuery.lastModified[ cacheURL ] );
			}
			if ( jQuery.etag[ cacheURL ] ) {
				jqXHR.setRequestHeader( "If-None-Match", jQuery.etag[ cacheURL ] );
			}
		}

		// Set the correct header, if data is being sent
		if ( s.data && s.hasContent && s.contentType !== false || options.contentType ) {
			jqXHR.setRequestHeader( "Content-Type", s.contentType );
		}

		// Set the Accepts header for the server, depending on the dataType
		jqXHR.setRequestHeader(
			"Accept",
			s.dataTypes[ 0 ] && s.accepts[ s.dataTypes[0] ] ?
				s.accepts[ s.dataTypes[0] ] + ( s.dataTypes[ 0 ] !== "*" ? ", " + allTypes + "; q=0.01" : "" ) :
				s.accepts[ "*" ]
		);

		// Check for headers option
		for ( i in s.headers ) {
			jqXHR.setRequestHeader( i, s.headers[ i ] );
		}

		// Allow custom headers/mimetypes and early abort
		if ( s.beforeSend && ( s.beforeSend.call( callbackContext, jqXHR, s ) === false || state === 2 ) ) {
			// Abort if not done already and return
			return jqXHR.abort();
		}

		// aborting is no longer a cancellation
		strAbort = "abort";

		// Install callbacks on deferreds
		for ( i in { success: 1, error: 1, complete: 1 } ) {
			jqXHR[ i ]( s[ i ] );
		}

		// Get transport
		transport = inspectPrefiltersOrTransports( transports, s, options, jqXHR );

		// If no transport, we auto-abort
		if ( !transport ) {
			done( -1, "No Transport" );
		} else {
			jqXHR.readyState = 1;

			// Send global event
			if ( fireGlobals ) {
				globalEventContext.trigger( "ajaxSend", [ jqXHR, s ] );
			}
			// Timeout
			if ( s.async && s.timeout > 0 ) {
				timeoutTimer = setTimeout(function() {
					jqXHR.abort("timeout");
				}, s.timeout );
			}

			try {
				state = 1;
				transport.send( requestHeaders, done );
			} catch ( e ) {
				// Propagate exception as error if not done
				if ( state < 2 ) {
					done( -1, e );
				// Simply rethrow otherwise
				} else {
					throw e;
				}
			}
		}

		// Callback for when everything is done
		function done( status, nativeStatusText, responses, headers ) {
			var isSuccess, success, error, response, modified,
				statusText = nativeStatusText;

			// Called once
			if ( state === 2 ) {
				return;
			}

			// State is "done" now
			state = 2;

			// Clear timeout if it exists
			if ( timeoutTimer ) {
				clearTimeout( timeoutTimer );
			}

			// Dereference transport for early garbage collection
			// (no matter how long the jqXHR object will be used)
			transport = undefined;

			// Cache response headers
			responseHeadersString = headers || "";

			// Set readyState
			jqXHR.readyState = status > 0 ? 4 : 0;

			// Determine if successful
			isSuccess = status >= 200 && status < 300 || status === 304;

			// Get response data
			if ( responses ) {
				response = ajaxHandleResponses( s, jqXHR, responses );
			}

			// Convert no matter what (that way responseXXX fields are always set)
			response = ajaxConvert( s, response, jqXHR, isSuccess );

			// If successful, handle type chaining
			if ( isSuccess ) {

				// Set the If-Modified-Since and/or If-None-Match header, if in ifModified mode.
				if ( s.ifModified ) {
					modified = jqXHR.getResponseHeader("Last-Modified");
					if ( modified ) {
						jQuery.lastModified[ cacheURL ] = modified;
					}
					modified = jqXHR.getResponseHeader("etag");
					if ( modified ) {
						jQuery.etag[ cacheURL ] = modified;
					}
				}

				// if no content
				if ( status === 204 || s.type === "HEAD" ) {
					statusText = "nocontent";

				// if not modified
				} else if ( status === 304 ) {
					statusText = "notmodified";

				// If we have data, let's convert it
				} else {
					statusText = response.state;
					success = response.data;
					error = response.error;
					isSuccess = !error;
				}
			} else {
				// We extract error from statusText
				// then normalize statusText and status for non-aborts
				error = statusText;
				if ( status || !statusText ) {
					statusText = "error";
					if ( status < 0 ) {
						status = 0;
					}
				}
			}

			// Set data for the fake xhr object
			jqXHR.status = status;
			jqXHR.statusText = ( nativeStatusText || statusText ) + "";

			// Success/Error
			if ( isSuccess ) {
				deferred.resolveWith( callbackContext, [ success, statusText, jqXHR ] );
			} else {
				deferred.rejectWith( callbackContext, [ jqXHR, statusText, error ] );
			}

			// Status-dependent callbacks
			jqXHR.statusCode( statusCode );
			statusCode = undefined;

			if ( fireGlobals ) {
				globalEventContext.trigger( isSuccess ? "ajaxSuccess" : "ajaxError",
					[ jqXHR, s, isSuccess ? success : error ] );
			}

			// Complete
			completeDeferred.fireWith( callbackContext, [ jqXHR, statusText ] );

			if ( fireGlobals ) {
				globalEventContext.trigger( "ajaxComplete", [ jqXHR, s ] );
				// Handle the global AJAX counter
				if ( !( --jQuery.active ) ) {
					jQuery.event.trigger("ajaxStop");
				}
			}
		}

		return jqXHR;
	},

	getJSON: function( url, data, callback ) {
		return jQuery.get( url, data, callback, "json" );
	},

	getScript: function( url, callback ) {
		return jQuery.get( url, undefined, callback, "script" );
	}
});

jQuery.each( [ "get", "post" ], function( i, method ) {
	jQuery[ method ] = function( url, data, callback, type ) {
		// shift arguments if data argument was omitted
		if ( jQuery.isFunction( data ) ) {
			type = type || callback;
			callback = data;
			data = undefined;
		}

		return jQuery.ajax({
			url: url,
			type: method,
			dataType: type,
			data: data,
			success: callback
		});
	};
});

/* Handles responses to an ajax request:
 * - finds the right dataType (mediates between content-type and expected dataType)
 * - returns the corresponding response
 */
function ajaxHandleResponses( s, jqXHR, responses ) {
	var firstDataType, ct, finalDataType, type,
		contents = s.contents,
		dataTypes = s.dataTypes;

	// Remove auto dataType and get content-type in the process
	while( dataTypes[ 0 ] === "*" ) {
		dataTypes.shift();
		if ( ct === undefined ) {
			ct = s.mimeType || jqXHR.getResponseHeader("Content-Type");
		}
	}

	// Check if we're dealing with a known content-type
	if ( ct ) {
		for ( type in contents ) {
			if ( contents[ type ] && contents[ type ].test( ct ) ) {
				dataTypes.unshift( type );
				break;
			}
		}
	}

	// Check to see if we have a response for the expected dataType
	if ( dataTypes[ 0 ] in responses ) {
		finalDataType = dataTypes[ 0 ];
	} else {
		// Try convertible dataTypes
		for ( type in responses ) {
			if ( !dataTypes[ 0 ] || s.converters[ type + " " + dataTypes[0] ] ) {
				finalDataType = type;
				break;
			}
			if ( !firstDataType ) {
				firstDataType = type;
			}
		}
		// Or just use first one
		finalDataType = finalDataType || firstDataType;
	}

	// If we found a dataType
	// We add the dataType to the list if needed
	// and return the corresponding response
	if ( finalDataType ) {
		if ( finalDataType !== dataTypes[ 0 ] ) {
			dataTypes.unshift( finalDataType );
		}
		return responses[ finalDataType ];
	}
}

/* Chain conversions given the request and the original response
 * Also sets the responseXXX fields on the jqXHR instance
 */
function ajaxConvert( s, response, jqXHR, isSuccess ) {
	var conv2, current, conv, tmp, prev,
		converters = {},
		// Work with a copy of dataTypes in case we need to modify it for conversion
		dataTypes = s.dataTypes.slice();

	// Create converters map with lowercased keys
	if ( dataTypes[ 1 ] ) {
		for ( conv in s.converters ) {
			converters[ conv.toLowerCase() ] = s.converters[ conv ];
		}
	}

	current = dataTypes.shift();

	// Convert to each sequential dataType
	while ( current ) {

		if ( s.responseFields[ current ] ) {
			jqXHR[ s.responseFields[ current ] ] = response;
		}

		// Apply the dataFilter if provided
		if ( !prev && isSuccess && s.dataFilter ) {
			response = s.dataFilter( response, s.dataType );
		}

		prev = current;
		current = dataTypes.shift();

		if ( current ) {

			// There's only work to do if current dataType is non-auto
			if ( current === "*" ) {

				current = prev;

			// Convert response if prev dataType is non-auto and differs from current
			} else if ( prev !== "*" && prev !== current ) {

				// Seek a direct converter
				conv = converters[ prev + " " + current ] || converters[ "* " + current ];

				// If none found, seek a pair
				if ( !conv ) {
					for ( conv2 in converters ) {

						// If conv2 outputs current
						tmp = conv2.split( " " );
						if ( tmp[ 1 ] === current ) {

							// If prev can be converted to accepted input
							conv = converters[ prev + " " + tmp[ 0 ] ] ||
								converters[ "* " + tmp[ 0 ] ];
							if ( conv ) {
								// Condense equivalence converters
								if ( conv === true ) {
									conv = converters[ conv2 ];

								// Otherwise, insert the intermediate dataType
								} else if ( converters[ conv2 ] !== true ) {
									current = tmp[ 0 ];
									dataTypes.unshift( tmp[ 1 ] );
								}
								break;
							}
						}
					}
				}

				// Apply converter (if not an equivalence)
				if ( conv !== true ) {

					// Unless errors are allowed to bubble, catch and return them
					if ( conv && s[ "throws" ] ) {
						response = conv( response );
					} else {
						try {
							response = conv( response );
						} catch ( e ) {
							return { state: "parsererror", error: conv ? e : "No conversion from " + prev + " to " + current };
						}
					}
				}
			}
		}
	}

	return { state: "success", data: response };
}
// Install script dataType
jQuery.ajaxSetup({
	accepts: {
		script: "text/javascript, application/javascript, application/ecmascript, application/x-ecmascript"
	},
	contents: {
		script: /(?:java|ecma)script/
	},
	converters: {
		"text script": function( text ) {
			jQuery.globalEval( text );
			return text;
		}
	}
});

// Handle cache's special case and global
jQuery.ajaxPrefilter( "script", function( s ) {
	if ( s.cache === undefined ) {
		s.cache = false;
	}
	if ( s.crossDomain ) {
		s.type = "GET";
		s.global = false;
	}
});

// Bind script tag hack transport
jQuery.ajaxTransport( "script", function(s) {

	// This transport only deals with cross domain requests
	if ( s.crossDomain ) {

		var script,
			head = document.head || jQuery("head")[0] || document.documentElement;

		return {

			send: function( _, callback ) {

				script = document.createElement("script");

				script.async = true;

				if ( s.scriptCharset ) {
					script.charset = s.scriptCharset;
				}

				script.src = s.url;

				// Attach handlers for all browsers
				script.onload = script.onreadystatechange = function( _, isAbort ) {

					if ( isAbort || !script.readyState || /loaded|complete/.test( script.readyState ) ) {

						// Handle memory leak in IE
						script.onload = script.onreadystatechange = null;

						// Remove the script
						if ( script.parentNode ) {
							script.parentNode.removeChild( script );
						}

						// Dereference the script
						script = null;

						// Callback if not abort
						if ( !isAbort ) {
							callback( 200, "success" );
						}
					}
				};

				// Circumvent IE6 bugs with base elements (#2709 and #4378) by prepending
				// Use native DOM manipulation to avoid our domManip AJAX trickery
				head.insertBefore( script, head.firstChild );
			},

			abort: function() {
				if ( script ) {
					script.onload( undefined, true );
				}
			}
		};
	}
});
var oldCallbacks = [],
	rjsonp = /(=)\?(?=&|$)|\?\?/;

// Default jsonp settings
jQuery.ajaxSetup({
	jsonp: "callback",
	jsonpCallback: function() {
		var callback = oldCallbacks.pop() || ( jQuery.expando + "_" + ( ajax_nonce++ ) );
		this[ callback ] = true;
		return callback;
	}
});

// Detect, normalize options and install callbacks for jsonp requests
jQuery.ajaxPrefilter( "json jsonp", function( s, originalSettings, jqXHR ) {

	var callbackName, overwritten, responseContainer,
		jsonProp = s.jsonp !== false && ( rjsonp.test( s.url ) ?
			"url" :
			typeof s.data === "string" && !( s.contentType || "" ).indexOf("application/x-www-form-urlencoded") && rjsonp.test( s.data ) && "data"
		);

	// Handle iff the expected data type is "jsonp" or we have a parameter to set
	if ( jsonProp || s.dataTypes[ 0 ] === "jsonp" ) {

		// Get callback name, remembering preexisting value associated with it
		callbackName = s.jsonpCallback = jQuery.isFunction( s.jsonpCallback ) ?
			s.jsonpCallback() :
			s.jsonpCallback;

		// Insert callback into url or form data
		if ( jsonProp ) {
			s[ jsonProp ] = s[ jsonProp ].replace( rjsonp, "$1" + callbackName );
		} else if ( s.jsonp !== false ) {
			s.url += ( ajax_rquery.test( s.url ) ? "&" : "?" ) + s.jsonp + "=" + callbackName;
		}

		// Use data converter to retrieve json after script execution
		s.converters["script json"] = function() {
			if ( !responseContainer ) {
				jQuery.error( callbackName + " was not called" );
			}
			return responseContainer[ 0 ];
		};

		// force json dataType
		s.dataTypes[ 0 ] = "json";

		// Install callback
		overwritten = window[ callbackName ];
		window[ callbackName ] = function() {
			responseContainer = arguments;
		};

		// Clean-up function (fires after converters)
		jqXHR.always(function() {
			// Restore preexisting value
			window[ callbackName ] = overwritten;

			// Save back as free
			if ( s[ callbackName ] ) {
				// make sure that re-using the options doesn't screw things around
				s.jsonpCallback = originalSettings.jsonpCallback;

				// save the callback name for future use
				oldCallbacks.push( callbackName );
			}

			// Call if it was a function and we have a response
			if ( responseContainer && jQuery.isFunction( overwritten ) ) {
				overwritten( responseContainer[ 0 ] );
			}

			responseContainer = overwritten = undefined;
		});

		// Delegate to script
		return "script";
	}
});
var xhrCallbacks, xhrSupported,
	xhrId = 0,
	// #5280: Internet Explorer will keep connections alive if we don't abort on unload
	xhrOnUnloadAbort = window.ActiveXObject && function() {
		// Abort all pending requests
		var key;
		for ( key in xhrCallbacks ) {
			xhrCallbacks[ key ]( undefined, true );
		}
	};

// Functions to create xhrs
function createStandardXHR() {
	try {
		return new window.XMLHttpRequest();
	} catch( e ) {}
}

function createActiveXHR() {
	try {
		return new window.ActiveXObject("Microsoft.XMLHTTP");
	} catch( e ) {}
}

// Create the request object
// (This is still attached to ajaxSettings for backward compatibility)
jQuery.ajaxSettings.xhr = window.ActiveXObject ?
	/* Microsoft failed to properly
	 * implement the XMLHttpRequest in IE7 (can't request local files),
	 * so we use the ActiveXObject when it is available
	 * Additionally XMLHttpRequest can be disabled in IE7/IE8 so
	 * we need a fallback.
	 */
	function() {
		return !this.isLocal && createStandardXHR() || createActiveXHR();
	} :
	// For all other browsers, use the standard XMLHttpRequest object
	createStandardXHR;

// Determine support properties
xhrSupported = jQuery.ajaxSettings.xhr();
jQuery.support.cors = !!xhrSupported && ( "withCredentials" in xhrSupported );
xhrSupported = jQuery.support.ajax = !!xhrSupported;

// Create transport if the browser can provide an xhr
if ( xhrSupported ) {

	jQuery.ajaxTransport(function( s ) {
		// Cross domain only allowed if supported through XMLHttpRequest
		if ( !s.crossDomain || jQuery.support.cors ) {

			var callback;

			return {
				send: function( headers, complete ) {

					// Get a new xhr
					var handle, i,
						xhr = s.xhr();

					// Open the socket
					// Passing null username, generates a login popup on Opera (#2865)
					if ( s.username ) {
						xhr.open( s.type, s.url, s.async, s.username, s.password );
					} else {
						xhr.open( s.type, s.url, s.async );
					}

					// Apply custom fields if provided
					if ( s.xhrFields ) {
						for ( i in s.xhrFields ) {
							xhr[ i ] = s.xhrFields[ i ];
						}
					}

					// Override mime type if needed
					if ( s.mimeType && xhr.overrideMimeType ) {
						xhr.overrideMimeType( s.mimeType );
					}

					// X-Requested-With header
					// For cross-domain requests, seeing as conditions for a preflight are
					// akin to a jigsaw puzzle, we simply never set it to be sure.
					// (it can always be set on a per-request basis or even using ajaxSetup)
					// For same-domain requests, won't change header if already provided.
					if ( !s.crossDomain && !headers["X-Requested-With"] ) {
						headers["X-Requested-With"] = "XMLHttpRequest";
					}

					// Need an extra try/catch for cross domain requests in Firefox 3
					try {
						for ( i in headers ) {
							xhr.setRequestHeader( i, headers[ i ] );
						}
					} catch( err ) {}

					// Do send the request
					// This may raise an exception which is actually
					// handled in jQuery.ajax (so no try/catch here)
					xhr.send( ( s.hasContent && s.data ) || null );

					// Listener
					callback = function( _, isAbort ) {
						var status, responseHeaders, statusText, responses;

						// Firefox throws exceptions when accessing properties
						// of an xhr when a network error occurred
						// http://helpful.knobs-dials.com/index.php/Component_returned_failure_code:_0x80040111_(NS_ERROR_NOT_AVAILABLE)
						try {

							// Was never called and is aborted or complete
							if ( callback && ( isAbort || xhr.readyState === 4 ) ) {

								// Only called once
								callback = undefined;

								// Do not keep as active anymore
								if ( handle ) {
									xhr.onreadystatechange = jQuery.noop;
									if ( xhrOnUnloadAbort ) {
										delete xhrCallbacks[ handle ];
									}
								}

								// If it's an abort
								if ( isAbort ) {
									// Abort it manually if needed
									if ( xhr.readyState !== 4 ) {
										xhr.abort();
									}
								} else {
									responses = {};
									status = xhr.status;
									responseHeaders = xhr.getAllResponseHeaders();

									// When requesting binary data, IE6-9 will throw an exception
									// on any attempt to access responseText (#11426)
									if ( typeof xhr.responseText === "string" ) {
										responses.text = xhr.responseText;
									}

									// Firefox throws an exception when accessing
									// statusText for faulty cross-domain requests
									try {
										statusText = xhr.statusText;
									} catch( e ) {
										// We normalize with Webkit giving an empty statusText
										statusText = "";
									}

									// Filter status for non standard behaviors

									// If the request is local and we have data: assume a success
									// (success with no data won't get notified, that's the best we
									// can do given current implementations)
									if ( !status && s.isLocal && !s.crossDomain ) {
										status = responses.text ? 200 : 404;
									// IE - #1450: sometimes returns 1223 when it should be 204
									} else if ( status === 1223 ) {
										status = 204;
									}
								}
							}
						} catch( firefoxAccessException ) {
							if ( !isAbort ) {
								complete( -1, firefoxAccessException );
							}
						}

						// Call complete if needed
						if ( responses ) {
							complete( status, statusText, responses, responseHeaders );
						}
					};

					if ( !s.async ) {
						// if we're in sync mode we fire the callback
						callback();
					} else if ( xhr.readyState === 4 ) {
						// (IE6 & IE7) if it's in cache and has been
						// retrieved directly we need to fire the callback
						setTimeout( callback );
					} else {
						handle = ++xhrId;
						if ( xhrOnUnloadAbort ) {
							// Create the active xhrs callbacks list if needed
							// and attach the unload handler
							if ( !xhrCallbacks ) {
								xhrCallbacks = {};
								jQuery( window ).unload( xhrOnUnloadAbort );
							}
							// Add to list of active xhrs callbacks
							xhrCallbacks[ handle ] = callback;
						}
						xhr.onreadystatechange = callback;
					}
				},

				abort: function() {
					if ( callback ) {
						callback( undefined, true );
					}
				}
			};
		}
	});
}
var fxNow, timerId,
	rfxtypes = /^(?:toggle|show|hide)$/,
	rfxnum = new RegExp( "^(?:([+-])=|)(" + core_pnum + ")([a-z%]*)$", "i" ),
	rrun = /queueHooks$/,
	animationPrefilters = [ defaultPrefilter ],
	tweeners = {
		"*": [function( prop, value ) {
			var tween = this.createTween( prop, value ),
				target = tween.cur(),
				parts = rfxnum.exec( value ),
				unit = parts && parts[ 3 ] || ( jQuery.cssNumber[ prop ] ? "" : "px" ),

				// Starting value computation is required for potential unit mismatches
				start = ( jQuery.cssNumber[ prop ] || unit !== "px" && +target ) &&
					rfxnum.exec( jQuery.css( tween.elem, prop ) ),
				scale = 1,
				maxIterations = 20;

			if ( start && start[ 3 ] !== unit ) {
				// Trust units reported by jQuery.css
				unit = unit || start[ 3 ];

				// Make sure we update the tween properties later on
				parts = parts || [];

				// Iteratively approximate from a nonzero starting point
				start = +target || 1;

				do {
					// If previous iteration zeroed out, double until we get *something*
					// Use a string for doubling factor so we don't accidentally see scale as unchanged below
					scale = scale || ".5";

					// Adjust and apply
					start = start / scale;
					jQuery.style( tween.elem, prop, start + unit );

				// Update scale, tolerating zero or NaN from tween.cur()
				// And breaking the loop if scale is unchanged or perfect, or if we've just had enough
				} while ( scale !== (scale = tween.cur() / target) && scale !== 1 && --maxIterations );
			}

			// Update tween properties
			if ( parts ) {
				start = tween.start = +start || +target || 0;
				tween.unit = unit;
				// If a +=/-= token was provided, we're doing a relative animation
				tween.end = parts[ 1 ] ?
					start + ( parts[ 1 ] + 1 ) * parts[ 2 ] :
					+parts[ 2 ];
			}

			return tween;
		}]
	};

// Animations created synchronously will run synchronously
function createFxNow() {
	setTimeout(function() {
		fxNow = undefined;
	});
	return ( fxNow = jQuery.now() );
}

function createTween( value, prop, animation ) {
	var tween,
		collection = ( tweeners[ prop ] || [] ).concat( tweeners[ "*" ] ),
		index = 0,
		length = collection.length;
	for ( ; index < length; index++ ) {
		if ( (tween = collection[ index ].call( animation, prop, value )) ) {

			// we're done with this property
			return tween;
		}
	}
}

function Animation( elem, properties, options ) {
	var result,
		stopped,
		index = 0,
		length = animationPrefilters.length,
		deferred = jQuery.Deferred().always( function() {
			// don't match elem in the :animated selector
			delete tick.elem;
		}),
		tick = function() {
			if ( stopped ) {
				return false;
			}
			var currentTime = fxNow || createFxNow(),
				remaining = Math.max( 0, animation.startTime + animation.duration - currentTime ),
				// archaic crash bug won't allow us to use 1 - ( 0.5 || 0 ) (#12497)
				temp = remaining / animation.duration || 0,
				percent = 1 - temp,
				index = 0,
				length = animation.tweens.length;

			for ( ; index < length ; index++ ) {
				animation.tweens[ index ].run( percent );
			}

			deferred.notifyWith( elem, [ animation, percent, remaining ]);

			if ( percent < 1 && length ) {
				return remaining;
			} else {
				deferred.resolveWith( elem, [ animation ] );
				return false;
			}
		},
		animation = deferred.promise({
			elem: elem,
			props: jQuery.extend( {}, properties ),
			opts: jQuery.extend( true, { specialEasing: {} }, options ),
			originalProperties: properties,
			originalOptions: options,
			startTime: fxNow || createFxNow(),
			duration: options.duration,
			tweens: [],
			createTween: function( prop, end ) {
				var tween = jQuery.Tween( elem, animation.opts, prop, end,
						animation.opts.specialEasing[ prop ] || animation.opts.easing );
				animation.tweens.push( tween );
				return tween;
			},
			stop: function( gotoEnd ) {
				var index = 0,
					// if we are going to the end, we want to run all the tweens
					// otherwise we skip this part
					length = gotoEnd ? animation.tweens.length : 0;
				if ( stopped ) {
					return this;
				}
				stopped = true;
				for ( ; index < length ; index++ ) {
					animation.tweens[ index ].run( 1 );
				}

				// resolve when we played the last frame
				// otherwise, reject
				if ( gotoEnd ) {
					deferred.resolveWith( elem, [ animation, gotoEnd ] );
				} else {
					deferred.rejectWith( elem, [ animation, gotoEnd ] );
				}
				return this;
			}
		}),
		props = animation.props;

	propFilter( props, animation.opts.specialEasing );

	for ( ; index < length ; index++ ) {
		result = animationPrefilters[ index ].call( animation, elem, props, animation.opts );
		if ( result ) {
			return result;
		}
	}

	jQuery.map( props, createTween, animation );

	if ( jQuery.isFunction( animation.opts.start ) ) {
		animation.opts.start.call( elem, animation );
	}

	jQuery.fx.timer(
		jQuery.extend( tick, {
			elem: elem,
			anim: animation,
			queue: animation.opts.queue
		})
	);

	// attach callbacks from options
	return animation.progress( animation.opts.progress )
		.done( animation.opts.done, animation.opts.complete )
		.fail( animation.opts.fail )
		.always( animation.opts.always );
}

function propFilter( props, specialEasing ) {
	var index, name, easing, value, hooks;

	// camelCase, specialEasing and expand cssHook pass
	for ( index in props ) {
		name = jQuery.camelCase( index );
		easing = specialEasing[ name ];
		value = props[ index ];
		if ( jQuery.isArray( value ) ) {
			easing = value[ 1 ];
			value = props[ index ] = value[ 0 ];
		}

		if ( index !== name ) {
			props[ name ] = value;
			delete props[ index ];
		}

		hooks = jQuery.cssHooks[ name ];
		if ( hooks && "expand" in hooks ) {
			value = hooks.expand( value );
			delete props[ name ];

			// not quite $.extend, this wont overwrite keys already present.
			// also - reusing 'index' from above because we have the correct "name"
			for ( index in value ) {
				if ( !( index in props ) ) {
					props[ index ] = value[ index ];
					specialEasing[ index ] = easing;
				}
			}
		} else {
			specialEasing[ name ] = easing;
		}
	}
}

jQuery.Animation = jQuery.extend( Animation, {

	tweener: function( props, callback ) {
		if ( jQuery.isFunction( props ) ) {
			callback = props;
			props = [ "*" ];
		} else {
			props = props.split(" ");
		}

		var prop,
			index = 0,
			length = props.length;

		for ( ; index < length ; index++ ) {
			prop = props[ index ];
			tweeners[ prop ] = tweeners[ prop ] || [];
			tweeners[ prop ].unshift( callback );
		}
	},

	prefilter: function( callback, prepend ) {
		if ( prepend ) {
			animationPrefilters.unshift( callback );
		} else {
			animationPrefilters.push( callback );
		}
	}
});

function defaultPrefilter( elem, props, opts ) {
	/* jshint validthis: true */
	var prop, value, toggle, tween, hooks, oldfire,
		anim = this,
		orig = {},
		style = elem.style,
		hidden = elem.nodeType && isHidden( elem ),
		dataShow = jQuery._data( elem, "fxshow" );

	// handle queue: false promises
	if ( !opts.queue ) {
		hooks = jQuery._queueHooks( elem, "fx" );
		if ( hooks.unqueued == null ) {
			hooks.unqueued = 0;
			oldfire = hooks.empty.fire;
			hooks.empty.fire = function() {
				if ( !hooks.unqueued ) {
					oldfire();
				}
			};
		}
		hooks.unqueued++;

		anim.always(function() {
			// doing this makes sure that the complete handler will be called
			// before this completes
			anim.always(function() {
				hooks.unqueued--;
				if ( !jQuery.queue( elem, "fx" ).length ) {
					hooks.empty.fire();
				}
			});
		});
	}

	// height/width overflow pass
	if ( elem.nodeType === 1 && ( "height" in props || "width" in props ) ) {
		// Make sure that nothing sneaks out
		// Record all 3 overflow attributes because IE does not
		// change the overflow attribute when overflowX and
		// overflowY are set to the same value
		opts.overflow = [ style.overflow, style.overflowX, style.overflowY ];

		// Set display property to inline-block for height/width
		// animations on inline elements that are having width/height animated
		if ( jQuery.css( elem, "display" ) === "inline" &&
				jQuery.css( elem, "float" ) === "none" ) {

			// inline-level elements accept inline-block;
			// block-level elements need to be inline with layout
			if ( !jQuery.support.inlineBlockNeedsLayout || css_defaultDisplay( elem.nodeName ) === "inline" ) {
				style.display = "inline-block";

			} else {
				style.zoom = 1;
			}
		}
	}

	if ( opts.overflow ) {
		style.overflow = "hidden";
		if ( !jQuery.support.shrinkWrapBlocks ) {
			anim.always(function() {
				style.overflow = opts.overflow[ 0 ];
				style.overflowX = opts.overflow[ 1 ];
				style.overflowY = opts.overflow[ 2 ];
			});
		}
	}


	// show/hide pass
	for ( prop in props ) {
		value = props[ prop ];
		if ( rfxtypes.exec( value ) ) {
			delete props[ prop ];
			toggle = toggle || value === "toggle";
			if ( value === ( hidden ? "hide" : "show" ) ) {
				continue;
			}
			orig[ prop ] = dataShow && dataShow[ prop ] || jQuery.style( elem, prop );
		}
	}

	if ( !jQuery.isEmptyObject( orig ) ) {
		if ( dataShow ) {
			if ( "hidden" in dataShow ) {
				hidden = dataShow.hidden;
			}
		} else {
			dataShow = jQuery._data( elem, "fxshow", {} );
		}

		// store state if its toggle - enables .stop().toggle() to "reverse"
		if ( toggle ) {
			dataShow.hidden = !hidden;
		}
		if ( hidden ) {
			jQuery( elem ).show();
		} else {
			anim.done(function() {
				jQuery( elem ).hide();
			});
		}
		anim.done(function() {
			var prop;
			jQuery._removeData( elem, "fxshow" );
			for ( prop in orig ) {
				jQuery.style( elem, prop, orig[ prop ] );
			}
		});
		for ( prop in orig ) {
			tween = createTween( hidden ? dataShow[ prop ] : 0, prop, anim );

			if ( !( prop in dataShow ) ) {
				dataShow[ prop ] = tween.start;
				if ( hidden ) {
					tween.end = tween.start;
					tween.start = prop === "width" || prop === "height" ? 1 : 0;
				}
			}
		}
	}
}

function Tween( elem, options, prop, end, easing ) {
	return new Tween.prototype.init( elem, options, prop, end, easing );
}
jQuery.Tween = Tween;

Tween.prototype = {
	constructor: Tween,
	init: function( elem, options, prop, end, easing, unit ) {
		this.elem = elem;
		this.prop = prop;
		this.easing = easing || "swing";
		this.options = options;
		this.start = this.now = this.cur();
		this.end = end;
		this.unit = unit || ( jQuery.cssNumber[ prop ] ? "" : "px" );
	},
	cur: function() {
		var hooks = Tween.propHooks[ this.prop ];

		return hooks && hooks.get ?
			hooks.get( this ) :
			Tween.propHooks._default.get( this );
	},
	run: function( percent ) {
		var eased,
			hooks = Tween.propHooks[ this.prop ];

		if ( this.options.duration ) {
			this.pos = eased = jQuery.easing[ this.easing ](
				percent, this.options.duration * percent, 0, 1, this.options.duration
			);
		} else {
			this.pos = eased = percent;
		}
		this.now = ( this.end - this.start ) * eased + this.start;

		if ( this.options.step ) {
			this.options.step.call( this.elem, this.now, this );
		}

		if ( hooks && hooks.set ) {
			hooks.set( this );
		} else {
			Tween.propHooks._default.set( this );
		}
		return this;
	}
};

Tween.prototype.init.prototype = Tween.prototype;

Tween.propHooks = {
	_default: {
		get: function( tween ) {
			var result;

			if ( tween.elem[ tween.prop ] != null &&
				(!tween.elem.style || tween.elem.style[ tween.prop ] == null) ) {
				return tween.elem[ tween.prop ];
			}

			// passing an empty string as a 3rd parameter to .css will automatically
			// attempt a parseFloat and fallback to a string if the parse fails
			// so, simple values such as "10px" are parsed to Float.
			// complex values such as "rotate(1rad)" are returned as is.
			result = jQuery.css( tween.elem, tween.prop, "" );
			// Empty strings, null, undefined and "auto" are converted to 0.
			return !result || result === "auto" ? 0 : result;
		},
		set: function( tween ) {
			// use step hook for back compat - use cssHook if its there - use .style if its
			// available and use plain properties where available
			if ( jQuery.fx.step[ tween.prop ] ) {
				jQuery.fx.step[ tween.prop ]( tween );
			} else if ( tween.elem.style && ( tween.elem.style[ jQuery.cssProps[ tween.prop ] ] != null || jQuery.cssHooks[ tween.prop ] ) ) {
				jQuery.style( tween.elem, tween.prop, tween.now + tween.unit );
			} else {
				tween.elem[ tween.prop ] = tween.now;
			}
		}
	}
};

// Support: IE <=9
// Panic based approach to setting things on disconnected nodes

Tween.propHooks.scrollTop = Tween.propHooks.scrollLeft = {
	set: function( tween ) {
		if ( tween.elem.nodeType && tween.elem.parentNode ) {
			tween.elem[ tween.prop ] = tween.now;
		}
	}
};

jQuery.each([ "toggle", "show", "hide" ], function( i, name ) {
	var cssFn = jQuery.fn[ name ];
	jQuery.fn[ name ] = function( speed, easing, callback ) {
		return speed == null || typeof speed === "boolean" ?
			cssFn.apply( this, arguments ) :
			this.animate( genFx( name, true ), speed, easing, callback );
	};
});

jQuery.fn.extend({
	fadeTo: function( speed, to, easing, callback ) {

		// show any hidden elements after setting opacity to 0
		return this.filter( isHidden ).css( "opacity", 0 ).show()

			// animate to the value specified
			.end().animate({ opacity: to }, speed, easing, callback );
	},
	animate: function( prop, speed, easing, callback ) {
		var empty = jQuery.isEmptyObject( prop ),
			optall = jQuery.speed( speed, easing, callback ),
			doAnimation = function() {
				// Operate on a copy of prop so per-property easing won't be lost
				var anim = Animation( this, jQuery.extend( {}, prop ), optall );

				// Empty animations, or finishing resolves immediately
				if ( empty || jQuery._data( this, "finish" ) ) {
					anim.stop( true );
				}
			};
			doAnimation.finish = doAnimation;

		return empty || optall.queue === false ?
			this.each( doAnimation ) :
			this.queue( optall.queue, doAnimation );
	},
	stop: function( type, clearQueue, gotoEnd ) {
		var stopQueue = function( hooks ) {
			var stop = hooks.stop;
			delete hooks.stop;
			stop( gotoEnd );
		};

		if ( typeof type !== "string" ) {
			gotoEnd = clearQueue;
			clearQueue = type;
			type = undefined;
		}
		if ( clearQueue && type !== false ) {
			this.queue( type || "fx", [] );
		}

		return this.each(function() {
			var dequeue = true,
				index = type != null && type + "queueHooks",
				timers = jQuery.timers,
				data = jQuery._data( this );

			if ( index ) {
				if ( data[ index ] && data[ index ].stop ) {
					stopQueue( data[ index ] );
				}
			} else {
				for ( index in data ) {
					if ( data[ index ] && data[ index ].stop && rrun.test( index ) ) {
						stopQueue( data[ index ] );
					}
				}
			}

			for ( index = timers.length; index--; ) {
				if ( timers[ index ].elem === this && (type == null || timers[ index ].queue === type) ) {
					timers[ index ].anim.stop( gotoEnd );
					dequeue = false;
					timers.splice( index, 1 );
				}
			}

			// start the next in the queue if the last step wasn't forced
			// timers currently will call their complete callbacks, which will dequeue
			// but only if they were gotoEnd
			if ( dequeue || !gotoEnd ) {
				jQuery.dequeue( this, type );
			}
		});
	},
	finish: function( type ) {
		if ( type !== false ) {
			type = type || "fx";
		}
		return this.each(function() {
			var index,
				data = jQuery._data( this ),
				queue = data[ type + "queue" ],
				hooks = data[ type + "queueHooks" ],
				timers = jQuery.timers,
				length = queue ? queue.length : 0;

			// enable finishing flag on private data
			data.finish = true;

			// empty the queue first
			jQuery.queue( this, type, [] );

			if ( hooks && hooks.stop ) {
				hooks.stop.call( this, true );
			}

			// look for any active animations, and finish them
			for ( index = timers.length; index--; ) {
				if ( timers[ index ].elem === this && timers[ index ].queue === type ) {
					timers[ index ].anim.stop( true );
					timers.splice( index, 1 );
				}
			}

			// look for any animations in the old queue and finish them
			for ( index = 0; index < length; index++ ) {
				if ( queue[ index ] && queue[ index ].finish ) {
					queue[ index ].finish.call( this );
				}
			}

			// turn off finishing flag
			delete data.finish;
		});
	}
});

// Generate parameters to create a standard animation
function genFx( type, includeWidth ) {
	var which,
		attrs = { height: type },
		i = 0;

	// if we include width, step value is 1 to do all cssExpand values,
	// if we don't include width, step value is 2 to skip over Left and Right
	includeWidth = includeWidth? 1 : 0;
	for( ; i < 4 ; i += 2 - includeWidth ) {
		which = cssExpand[ i ];
		attrs[ "margin" + which ] = attrs[ "padding" + which ] = type;
	}

	if ( includeWidth ) {
		attrs.opacity = attrs.width = type;
	}

	return attrs;
}

// Generate shortcuts for custom animations
jQuery.each({
	slideDown: genFx("show"),
	slideUp: genFx("hide"),
	slideToggle: genFx("toggle"),
	fadeIn: { opacity: "show" },
	fadeOut: { opacity: "hide" },
	fadeToggle: { opacity: "toggle" }
}, function( name, props ) {
	jQuery.fn[ name ] = function( speed, easing, callback ) {
		return this.animate( props, speed, easing, callback );
	};
});

jQuery.speed = function( speed, easing, fn ) {
	var opt = speed && typeof speed === "object" ? jQuery.extend( {}, speed ) : {
		complete: fn || !fn && easing ||
			jQuery.isFunction( speed ) && speed,
		duration: speed,
		easing: fn && easing || easing && !jQuery.isFunction( easing ) && easing
	};

	opt.duration = jQuery.fx.off ? 0 : typeof opt.duration === "number" ? opt.duration :
		opt.duration in jQuery.fx.speeds ? jQuery.fx.speeds[ opt.duration ] : jQuery.fx.speeds._default;

	// normalize opt.queue - true/undefined/null -> "fx"
	if ( opt.queue == null || opt.queue === true ) {
		opt.queue = "fx";
	}

	// Queueing
	opt.old = opt.complete;

	opt.complete = function() {
		if ( jQuery.isFunction( opt.old ) ) {
			opt.old.call( this );
		}

		if ( opt.queue ) {
			jQuery.dequeue( this, opt.queue );
		}
	};

	return opt;
};

jQuery.easing = {
	linear: function( p ) {
		return p;
	},
	swing: function( p ) {
		return 0.5 - Math.cos( p*Math.PI ) / 2;
	}
};

jQuery.timers = [];
jQuery.fx = Tween.prototype.init;
jQuery.fx.tick = function() {
	var timer,
		timers = jQuery.timers,
		i = 0;

	fxNow = jQuery.now();

	for ( ; i < timers.length; i++ ) {
		timer = timers[ i ];
		// Checks the timer has not already been removed
		if ( !timer() && timers[ i ] === timer ) {
			timers.splice( i--, 1 );
		}
	}

	if ( !timers.length ) {
		jQuery.fx.stop();
	}
	fxNow = undefined;
};

jQuery.fx.timer = function( timer ) {
	if ( timer() && jQuery.timers.push( timer ) ) {
		jQuery.fx.start();
	}
};

jQuery.fx.interval = 13;

jQuery.fx.start = function() {
	if ( !timerId ) {
		timerId = setInterval( jQuery.fx.tick, jQuery.fx.interval );
	}
};

jQuery.fx.stop = function() {
	clearInterval( timerId );
	timerId = null;
};

jQuery.fx.speeds = {
	slow: 600,
	fast: 200,
	// Default speed
	_default: 400
};

// Back Compat <1.8 extension point
jQuery.fx.step = {};

if ( jQuery.expr && jQuery.expr.filters ) {
	jQuery.expr.filters.animated = function( elem ) {
		return jQuery.grep(jQuery.timers, function( fn ) {
			return elem === fn.elem;
		}).length;
	};
}
jQuery.fn.offset = function( options ) {
	if ( arguments.length ) {
		return options === undefined ?
			this :
			this.each(function( i ) {
				jQuery.offset.setOffset( this, options, i );
			});
	}

	var docElem, win,
		box = { top: 0, left: 0 },
		elem = this[ 0 ],
		doc = elem && elem.ownerDocument;

	if ( !doc ) {
		return;
	}

	docElem = doc.documentElement;

	// Make sure it's not a disconnected DOM node
	if ( !jQuery.contains( docElem, elem ) ) {
		return box;
	}

	// If we don't have gBCR, just use 0,0 rather than error
	// BlackBerry 5, iOS 3 (original iPhone)
	if ( typeof elem.getBoundingClientRect !== core_strundefined ) {
		box = elem.getBoundingClientRect();
	}
	win = getWindow( doc );
	return {
		top: box.top  + ( win.pageYOffset || docElem.scrollTop )  - ( docElem.clientTop  || 0 ),
		left: box.left + ( win.pageXOffset || docElem.scrollLeft ) - ( docElem.clientLeft || 0 )
	};
};

jQuery.offset = {

	setOffset: function( elem, options, i ) {
		var position = jQuery.css( elem, "position" );

		// set position first, in-case top/left are set even on static elem
		if ( position === "static" ) {
			elem.style.position = "relative";
		}

		var curElem = jQuery( elem ),
			curOffset = curElem.offset(),
			curCSSTop = jQuery.css( elem, "top" ),
			curCSSLeft = jQuery.css( elem, "left" ),
			calculatePosition = ( position === "absolute" || position === "fixed" ) && jQuery.inArray("auto", [curCSSTop, curCSSLeft]) > -1,
			props = {}, curPosition = {}, curTop, curLeft;

		// need to be able to calculate position if either top or left is auto and position is either absolute or fixed
		if ( calculatePosition ) {
			curPosition = curElem.position();
			curTop = curPosition.top;
			curLeft = curPosition.left;
		} else {
			curTop = parseFloat( curCSSTop ) || 0;
			curLeft = parseFloat( curCSSLeft ) || 0;
		}

		if ( jQuery.isFunction( options ) ) {
			options = options.call( elem, i, curOffset );
		}

		if ( options.top != null ) {
			props.top = ( options.top - curOffset.top ) + curTop;
		}
		if ( options.left != null ) {
			props.left = ( options.left - curOffset.left ) + curLeft;
		}

		if ( "using" in options ) {
			options.using.call( elem, props );
		} else {
			curElem.css( props );
		}
	}
};


jQuery.fn.extend({

	position: function() {
		if ( !this[ 0 ] ) {
			return;
		}

		var offsetParent, offset,
			parentOffset = { top: 0, left: 0 },
			elem = this[ 0 ];

		// fixed elements are offset from window (parentOffset = {top:0, left: 0}, because it is it's only offset parent
		if ( jQuery.css( elem, "position" ) === "fixed" ) {
			// we assume that getBoundingClientRect is available when computed position is fixed
			offset = elem.getBoundingClientRect();
		} else {
			// Get *real* offsetParent
			offsetParent = this.offsetParent();

			// Get correct offsets
			offset = this.offset();
			if ( !jQuery.nodeName( offsetParent[ 0 ], "html" ) ) {
				parentOffset = offsetParent.offset();
			}

			// Add offsetParent borders
			parentOffset.top  += jQuery.css( offsetParent[ 0 ], "borderTopWidth", true );
			parentOffset.left += jQuery.css( offsetParent[ 0 ], "borderLeftWidth", true );
		}

		// Subtract parent offsets and element margins
		// note: when an element has margin: auto the offsetLeft and marginLeft
		// are the same in Safari causing offset.left to incorrectly be 0
		return {
			top:  offset.top  - parentOffset.top - jQuery.css( elem, "marginTop", true ),
			left: offset.left - parentOffset.left - jQuery.css( elem, "marginLeft", true)
		};
	},

	offsetParent: function() {
		return this.map(function() {
			var offsetParent = this.offsetParent || docElem;
			while ( offsetParent && ( !jQuery.nodeName( offsetParent, "html" ) && jQuery.css( offsetParent, "position") === "static" ) ) {
				offsetParent = offsetParent.offsetParent;
			}
			return offsetParent || docElem;
		});
	}
});


// Create scrollLeft and scrollTop methods
jQuery.each( {scrollLeft: "pageXOffset", scrollTop: "pageYOffset"}, function( method, prop ) {
	var top = /Y/.test( prop );

	jQuery.fn[ method ] = function( val ) {
		return jQuery.access( this, function( elem, method, val ) {
			var win = getWindow( elem );

			if ( val === undefined ) {
				return win ? (prop in win) ? win[ prop ] :
					win.document.documentElement[ method ] :
					elem[ method ];
			}

			if ( win ) {
				win.scrollTo(
					!top ? val : jQuery( win ).scrollLeft(),
					top ? val : jQuery( win ).scrollTop()
				);

			} else {
				elem[ method ] = val;
			}
		}, method, val, arguments.length, null );
	};
});

function getWindow( elem ) {
	return jQuery.isWindow( elem ) ?
		elem :
		elem.nodeType === 9 ?
			elem.defaultView || elem.parentWindow :
			false;
}
// Create innerHeight, innerWidth, height, width, outerHeight and outerWidth methods
jQuery.each( { Height: "height", Width: "width" }, function( name, type ) {
	jQuery.each( { padding: "inner" + name, content: type, "": "outer" + name }, function( defaultExtra, funcName ) {
		// margin is only for outerHeight, outerWidth
		jQuery.fn[ funcName ] = function( margin, value ) {
			var chainable = arguments.length && ( defaultExtra || typeof margin !== "boolean" ),
				extra = defaultExtra || ( margin === true || value === true ? "margin" : "border" );

			return jQuery.access( this, function( elem, type, value ) {
				var doc;

				if ( jQuery.isWindow( elem ) ) {
					// As of 5/8/2012 this will yield incorrect results for Mobile Safari, but there
					// isn't a whole lot we can do. See pull request at this URL for discussion:
					// https://github.com/jquery/jquery/pull/764
					return elem.document.documentElement[ "client" + name ];
				}

				// Get document width or height
				if ( elem.nodeType === 9 ) {
					doc = elem.documentElement;

					// Either scroll[Width/Height] or offset[Width/Height] or client[Width/Height], whichever is greatest
					// unfortunately, this causes bug #3838 in IE6/8 only, but there is currently no good, small way to fix it.
					return Math.max(
						elem.body[ "scroll" + name ], doc[ "scroll" + name ],
						elem.body[ "offset" + name ], doc[ "offset" + name ],
						doc[ "client" + name ]
					);
				}

				return value === undefined ?
					// Get width or height on the element, requesting but not forcing parseFloat
					jQuery.css( elem, type, extra ) :

					// Set width or height on the element
					jQuery.style( elem, type, value, extra );
			}, type, chainable ? margin : undefined, chainable, null );
		};
	});
});
// Limit scope pollution from any deprecated API
// (function() {

// The number of elements contained in the matched element set
jQuery.fn.size = function() {
	return this.length;
};

jQuery.fn.andSelf = jQuery.fn.addBack;

// })();
if ( typeof module === "object" && module && typeof module.exports === "object" ) {
	// Expose jQuery as module.exports in loaders that implement the Node
	// module pattern (including browserify). Do not create the global, since
	// the user will be storing it themselves locally, and globals are frowned
	// upon in the Node module world.
	module.exports = jQuery;
} else {
	// Otherwise expose jQuery to the global object as usual
	window.jQuery = window.$ = jQuery;

	// Register as a named AMD module, since jQuery can be concatenated with other
	// files that may use define, but not via a proper concatenation script that
	// understands anonymous AMD modules. A named AMD is safest and most robust
	// way to register. Lowercase jquery is used because AMD module names are
	// derived from file names, and jQuery is normally delivered in a lowercase
	// file name. Do this after creating the global so that if an AMD module wants
	// to call noConflict to hide this version of jQuery, it will work.
	if ( typeof define === "function" && define.amd ) {
		define( "jquery", [], function () { return jQuery; } );
	}
}

})( window );

File: /assets\js\paper-dashboard.js
/*!
    
 =========================================================
 * Paper Dashboard - v1.1.2
 =========================================================
 
 * Product Page: http://www.creative-tim.com/product/paper-dashboard
 * Copyright 2017 Creative Tim (http://www.creative-tim.com)
 * Licensed under MIT (https://github.com/creativetimofficial/paper-dashboard/blob/master/LICENSE.md)
 
 =========================================================
 
 * The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
 
 */


var fixedTop = false;
var transparent = true;
var navbar_initialized = false;

$(document).ready(function(){
    window_width = $(window).width();

    // Init navigation toggle for small screens
    if(window_width <= 991){
        pd.initRightMenu();
    }

    //  Activate the tooltips
    $('[rel="tooltip"]').tooltip();

});

// activate collapse right menu when the windows is resized
$(window).resize(function(){
    if($(window).width() <= 991){
        pd.initRightMenu();
    }
});

pd = {
    misc:{
        navbar_menu_visible: 0
    },
    checkScrollForTransparentNavbar: debounce(function() {
        if($(document).scrollTop() > 381 ) {
            if(transparent) {
                transparent = false;
                $('.navbar-color-on-scroll').removeClass('navbar-transparent');
                $('.navbar-title').removeClass('hidden');
            }
        } else {
            if( !transparent ) {
                transparent = true;
                $('.navbar-color-on-scroll').addClass('navbar-transparent');
                $('.navbar-title').addClass('hidden');
            }
        }
    }),
    initRightMenu: function(){
         if(!navbar_initialized){
            $off_canvas_sidebar = $('nav').find('.navbar-collapse').first().clone(true);

            $sidebar = $('.sidebar');
            sidebar_bg_color = $sidebar.data('background-color');
            sidebar_active_color = $sidebar.data('active-color');

            $logo = $sidebar.find('.logo').first();
            logo_content = $logo[0].outerHTML;

            ul_content = '';

            // set the bg color and active color from the default sidebar to the off canvas sidebar;
            $off_canvas_sidebar.attr('data-background-color',sidebar_bg_color);
            $off_canvas_sidebar.attr('data-active-color',sidebar_active_color);

            $off_canvas_sidebar.addClass('off-canvas-sidebar');

            //add the content from the regular header to the right menu
            $off_canvas_sidebar.children('ul').each(function(){
                content_buff = $(this).html();
                ul_content = ul_content + content_buff;
            });

            // add the content from the sidebar to the right menu
            content_buff = $sidebar.find('.nav').html();
            ul_content = ul_content + '<li class="divider"></li>'+ content_buff;

            ul_content = '<ul class="nav navbar-nav">' + ul_content + '</ul>';

            navbar_content = logo_content + ul_content;
            navbar_content = '<div class="sidebar-wrapper">' + navbar_content + '</div>';

            $off_canvas_sidebar.html(navbar_content);

            $('body').append($off_canvas_sidebar);

             $toggle = $('.navbar-toggle');

             $off_canvas_sidebar.find('a').removeClass('btn btn-round btn-default');
             $off_canvas_sidebar.find('button').removeClass('btn-round btn-fill btn-info btn-primary btn-success btn-danger btn-warning btn-neutral');
             $off_canvas_sidebar.find('button').addClass('btn-simple btn-block');

             $toggle.click(function (){
                if(pd.misc.navbar_menu_visible == 1) {
                    $('html').removeClass('nav-open');
                    pd.misc.navbar_menu_visible = 0;
                    $('#bodyClick').remove();
                     setTimeout(function(){
                        $toggle.removeClass('toggled');
                     }, 400);

                } else {
                    setTimeout(function(){
                        $toggle.addClass('toggled');
                    }, 430);

                    div = '<div id="bodyClick"></div>';
                    $(div).appendTo("body").click(function() {
                        $('html').removeClass('nav-open');
                        pd.misc.navbar_menu_visible = 0;
                        $('#bodyClick').remove();
                         setTimeout(function(){
                            $toggle.removeClass('toggled');
                         }, 400);
                    });

                    $('html').addClass('nav-open');
                    pd.misc.navbar_menu_visible = 1;

                }
            });
            navbar_initialized = true;
        }

    }
}


// Returns a function, that, as long as it continues to be invoked, will not
// be triggered. The function will be called after it stops being called for
// N milliseconds. If `immediate` is passed, trigger the function on the
// leading edge, instead of the trailing.

function debounce(func, wait, immediate) {
	var timeout;
	return function() {
		var context = this, args = arguments;
		clearTimeout(timeout);
		timeout = setTimeout(function() {
			timeout = null;
			if (!immediate) func.apply(context, args);
		}, wait);
		if (immediate && !timeout) func.apply(context, args);
	};
};


File: /assets\sass\paper\mixins\_buttons.scss
// Mixin for generating new styles
@mixin btn-styles($btn-color, $btn-states-color) {
  border-color: $btn-color;
  color: $btn-color;
  
  &:hover,
  &:focus,
  &:active,
  &.active,
  .open > &.dropdown-toggle {
    background-color: $btn-color;
    color: $fill-font-color;
    border-color: $btn-color;
    .caret{
        border-top-color: $fill-font-color;
    }
  }
  
  &.disabled,
  &:disabled,
  &[disabled],
  fieldset[disabled] & {
    &,
    &:hover,
    &:focus,
    &.focus,
    &:active,
    &.active {
      background-color: $transparent-bg;
      border-color: $btn-color;
    }
  }
  

  &.btn-fill {
    color: $white-color;
    background-color: $btn-color;
    @include opacity(1);  

    &:hover,
    &:focus,
    &:active,
    &.active,
    .open > &.dropdown-toggle{
        background-color: $btn-states-color;
        color: $white-color;
        border-color: $btn-states-color;
    }
    
    .caret{
        border-top-color: $white-color;
    }
  }
  
  &.btn-simple {
    &:hover,
    &:focus,
    &:active,
    &.active,
    .open > &.dropdown-toggle{
        background-color: $transparent-bg;
        color: $btn-states-color;
    }
    
    .caret{
        border-top-color: $white-color;
    }
  }  
  
  .caret{
      border-top-color: $btn-color;
  }
}


@mixin btn-size($padding-vertical, $padding-horizontal, $font-size, $border, $line-height){
   font-size: $font-size;
   border-radius: $border;
   padding: $padding-vertical $padding-horizontal;
    
   &.btn-simple{
       padding: $padding-vertical + 2 $padding-horizontal; 
   }
    
}

File: /assets\sass\paper\mixins\_cards.scss
@mixin filter($color){
    @if $color == #FFFFFF{
         background-color: rgba($color,.91);
    } @else {
         background-color: rgba($color,.69);
    }
}



File: /assets\sass\paper\mixins\_chartist.scss
// Scales for responsive SVG containers
$ct-scales: ((1), (15/16), (8/9), (5/6), (4/5), (3/4), (2/3), (5/8), (1/1.618), (3/5), (9/16), (8/15), (1/2), (2/5), (3/8), (1/3), (1/4)) !default;
$ct-scales-names: (ct-square, ct-minor-second, ct-major-second, ct-minor-third, ct-major-third, ct-perfect-fourth, ct-perfect-fifth, ct-minor-sixth, ct-golden-section, ct-major-sixth, ct-minor-seventh, ct-major-seventh, ct-octave, ct-major-tenth, ct-major-eleventh, ct-major-twelfth, ct-double-octave) !default;

// Class names to be used when generating CSS
$ct-class-chart: ct-chart !default;
$ct-class-chart-line: ct-chart-line !default;
$ct-class-chart-bar: ct-chart-bar !default;
$ct-class-horizontal-bars: ct-horizontal-bars !default;
$ct-class-chart-pie: ct-chart-pie !default;
$ct-class-chart-donut: ct-chart-donut !default;
$ct-class-label: ct-label !default;
$ct-class-series: ct-series !default;
$ct-class-line: ct-line !default;
$ct-class-point: ct-point !default;
$ct-class-area: ct-area !default;
$ct-class-bar: ct-bar !default;
$ct-class-slice-pie: ct-slice-pie !default;
$ct-class-slice-donut: ct-slice-donut !default;
$ct-class-grid: ct-grid !default;
$ct-class-vertical: ct-vertical !default;
$ct-class-horizontal: ct-horizontal !default;
$ct-class-start: ct-start !default;
$ct-class-end: ct-end !default;

// Container ratio
$ct-container-ratio: (1/1.618) !default;

// Text styles for labels
$ct-text-color: rgba(0, 0, 0, 0.4) !default;
$ct-text-size: 0.9em !default;
$ct-text-align: flex-start !default;
$ct-text-justify: flex-start !default;
$ct-text-line-height: 1;

// Grid styles
$ct-grid-color: rgba(0, 0, 0, 0.2) !default;
$ct-grid-dasharray: 2px !default;
$ct-grid-width: 1px !default;

// Line chart properties
$ct-line-width: 4px !default;
$ct-line-dasharray: false !default;
$ct-point-size: 10px !default;
// Line chart point, can be either round or square
$ct-point-shape: round !default;
// Area fill transparency between 0 and 1
$ct-area-opacity: 0.7 !default;

// Bar chart bar width
$ct-bar-width: 10px !default;

// Donut width (If donut width is to big it can cause issues where the shape gets distorted)
$ct-donut-width: 60px !default;

// If set to true it will include the default classes and generate CSS output. If you're planning to use the mixins you
// should set this property to false
$ct-include-classes: true !default;

// If this is set to true the CSS will contain colored series. You can extend or change the color with the
// properties below
$ct-include-colored-series: $ct-include-classes !default;

// If set to true this will include all responsive container variations using the scales defined at the top of the script
$ct-include-alternative-responsive-containers: $ct-include-classes !default;

// Series names and colors. This can be extended or customized as desired. Just add more series and colors.
$ct-series-names: (a, b, c, d, e, f, g, h, i, j, k, l, m, n, o) !default;
$ct-series-colors: (
  $info-color,
  $warning-color,
  $danger-color,
  $success-color,
  $primary-color,
  rgba($info-color,.8),
  rgba($success-color,.8),
  rgba($warning-color,.8),
  rgba($danger-color,.8),
  rgba($primary-color,.8),
  rgba($info-color,.6),
  rgba($success-color,.6),
  rgba($warning-color,.6),
  rgba($danger-color,.6),
  rgba($primary-color,.6)
  
) !default;

// Paper Kit Colors

.ct-blue{
    stroke: $primary-color !important;
}
.ct-azure{
    stroke: $info-color !important;
}
.ct-green{
    stroke: $success-color !important;
}
.ct-orange{
    stroke: $warning-color !important;
}
.ct-red{
    stroke: $danger-color !important;
}

File: /assets\sass\paper\mixins\_icons.scss
@mixin icon-background ($icon-url){
	background-image : url($icon-url);
		
}

@mixin icon-shape ($size, $padding, $border-radius) {
	height: $size;
	width: $size;
	padding: $padding;
	border-radius: $border-radius;
	display: inline-table;

}

File: /assets\sass\paper\mixins\_inputs.scss
@mixin input-size($padding-vertical, $padding-horizontal, $height){
    padding: $padding-vertical $padding-horizontal;
    height: $height;
}

@mixin placeholder($color, $opacity){
   color: $color;
   @include opacity(1);
}

@mixin light-form(){
    border-radius: 0;
    border:0;
    padding: 0;
    background-color: transparent;

}

File: /assets\sass\paper\mixins\_labels.scss
@mixin label-style(){
     padding: $padding-label-vertical $padding-label-horizontal;
     border: 1px solid $default-color;
     border-radius: $border-radius-small;
     color: $default-color;
     font-weight: $font-weight-semi;
     font-size: $font-size-small;
     text-transform: uppercase;
     display: inline-block;
     vertical-align: middle;
}

@mixin label-color($color){
     border-color: $color;
     color: $color;
}
@mixin label-color-fill($color){
     border-color: $color;
     color: $white-color;
     background-color: $color;
}

File: /assets\sass\paper\mixins\_navbars.scss
@mixin navbar-color($color){
    background-color: $color;
}

@mixin center-item(){
    left: 0;
    right: 0;
    margin-right: auto;
    margin-left: auto;
    position: absolute;
}

File: /assets\sass\paper\mixins\_sidebar.scss
@mixin sidebar-background-color($background-color, $font-color){
    &:after,
    &:before{
	    background-color: $background-color;
	}

    .logo{
        border-bottom: 1px solid rgba($font-color,.3);

        p{
            color: $font-color;
        }

        .simple-text{
            color: $font-color;
        }
    }

    .nav{
        li:not(.active){
            > a{
                color: $font-color;
            }
        }
        .divider{
            background-color: rgba($font-color,.2);
        }
        
    }

}

@mixin sidebar-active-color($font-color){
    .nav{
        li{
            &.active > a{
                color: $font-color;
                opacity: 1;
            }
        }
    }
}


File: /assets\sass\paper\mixins\_tabs.scss
@mixin pill-style($color){
    border: 1px solid $color;
    color: $color;
}

File: /assets\sass\paper\mixins\_transparency.scss
// Opacity

@mixin opacity($opacity) {
  opacity: $opacity;
  // IE8 filter
  $opacity-ie: ($opacity * 100);
  filter: #{alpha(opacity=$opacity-ie)};
}

@mixin black-filter($opacity){
    top: 0;
    left: 0;
    height: 100%;
    width: 100%;
    position: absolute;
    background-color: rgba(17,17,17,$opacity);
    display: block;
    content: "";
    z-index: 1; 
}

File: /assets\sass\paper\mixins\_vendor-prefixes.scss
// User select
// For selecting text on the page

@mixin user-select($select) {
  -webkit-user-select: $select;
     -moz-user-select: $select;
      -ms-user-select: $select; // IE10+
          user-select: $select;
}

@mixin box-shadow($shadow...) {
  -webkit-box-shadow: $shadow; // iOS <4.3 & Android <4.1
          box-shadow: $shadow;
}

// Box sizing
@mixin box-sizing($boxmodel) {
  -webkit-box-sizing: $boxmodel;
     -moz-box-sizing: $boxmodel;
          box-sizing: $boxmodel;
}


@mixin transition($time, $type){
    -webkit-transition: all $time $type;
    -moz-transition: all $time $type;
    -o-transition: all $time $type;
    -ms-transition: all $time $type;
    transition: all $time $type;
}

@mixin transition-none(){
    -webkit-transition: none;
    -moz-transition: none;
    -o-transition: none;
    -ms-transition: none;
    transition: none;
}

@mixin transform-scale($value){
     -webkit-transform: scale($value);
        -moz-transform: scale($value);
        -o-transform: scale($value);
        -ms-transform: scale($value);
        transform: scale($value);
}

@mixin transform-translate-x($value){
     -webkit-transform:  translate3d($value, 0, 0);
        -moz-transform: translate3d($value, 0, 0);
        -o-transform: translate3d($value, 0, 0);
        -ms-transform: translate3d($value, 0, 0);
        transform: translate3d($value, 0, 0);
}

@mixin transform-origin($coordinates){
      -webkit-transform-origin: $coordinates;
        -moz-transform-origin: $coordinates;
        -o-transform-origin: $coordinates;
        -ms-transform-origin: $coordinates;
        transform-origin: $coordinates;
}

@mixin icon-gradient ($top-color, $bottom-color){
    background: $top-color;
    background: -moz-linear-gradient(top,  $top-color 0%, $bottom-color 100%);
    background: -webkit-gradient(linear, left top, left bottom, color-stop(0%,$top-color), color-stop(100%,$bottom-color));
    background: -webkit-linear-gradient(top,  $top-color 0%,$bottom-color 100%);
    background: -o-linear-gradient(top,  $top-color 0%,$bottom-color 100%);
    background: -ms-linear-gradient(top,  $top-color 0%,$bottom-color 100%);
    background: linear-gradient(to bottom,  $top-color 0%,$bottom-color 100%);
    background-size: 150% 150%;
}

@mixin radial-gradient($extern-color, $center-color){
    background: $extern-color;
    background: -moz-radial-gradient(center, ellipse cover, $center-color 0%, $extern-color 100%); /* FF3.6+ */
    background: -webkit-gradient(radial, center center, 0px, center center, 100%, color-stop(0%,$center-color), color-stop(100%,$extern-color)); /* Chrome,Safari4+ */
    background: -webkit-radial-gradient(center, ellipse cover, $center-color 0%,$extern-color 100%); /* Chrome10+,Safari5.1+ */
    background: -o-radial-gradient(center, ellipse cover, $center-color 0%,$extern-color 100%); /* Opera 12+ */
    background: -ms-radial-gradient(center, ellipse cover, $center-color 0%,$extern-color 100%); /* IE10+ */
    background: radial-gradient(ellipse at center, $center-color 0%,$extern-color 100%); /* W3C */
    background-size: 550% 450%;
}

@mixin vertical-align {
  position: relative;
  top: 50%;
  -webkit-transform: translateY(-50%);
  -ms-transform: translateY(-50%);
  transform: translateY(-50%);
}

@mixin rotate-180(){
    filter: progid:DXImageTransform.Microsoft.BasicImage(rotation=2);
    -webkit-transform: rotate(180deg);
    -ms-transform: rotate(180deg);
    transform: rotate(180deg);
}

@mixin bar-animation($type){
     -webkit-animation: $type 500ms linear 0s;
     -moz-animation: $type 500ms linear 0s;
     animation: $type 500ms 0s;
     -webkit-animation-fill-mode: forwards;
     -moz-animation-fill-mode: forwards;
     animation-fill-mode: forwards;
}

@mixin topbar-x-rotation(){
    @keyframes topbar-x {
      0% {top: 0px; transform: rotate(0deg); }
      45% {top: 6px; transform: rotate(145deg); }
      75% {transform: rotate(130deg); }
      100% {transform: rotate(135deg); }
    }
    @-webkit-keyframes topbar-x {
      0% {top: 0px; -webkit-transform: rotate(0deg); }
      45% {top: 6px; -webkit-transform: rotate(145deg); }
      75% {-webkit-transform: rotate(130deg); }
      100% { -webkit-transform: rotate(135deg); }
    }
    @-moz-keyframes topbar-x {
      0% {top: 0px; -moz-transform: rotate(0deg); }
      45% {top: 6px; -moz-transform: rotate(145deg); }
      75% {-moz-transform: rotate(130deg); }
      100% { -moz-transform: rotate(135deg); }
    }
}

@mixin topbar-back-rotation(){
    @keyframes topbar-back {
      0% { top: 6px; transform: rotate(135deg); }
      45% { transform: rotate(-10deg); }
      75% { transform: rotate(5deg); }
      100% { top: 0px; transform: rotate(0); }
    }
    
    @-webkit-keyframes topbar-back {
      0% { top: 6px; -webkit-transform: rotate(135deg); }
      45% { -webkit-transform: rotate(-10deg); }
      75% { -webkit-transform: rotate(5deg); }
      100% { top: 0px; -webkit-transform: rotate(0); }
    }
    
    @-moz-keyframes topbar-back {
      0% { top: 6px; -moz-transform: rotate(135deg); }
      45% { -moz-transform: rotate(-10deg); }
      75% { -moz-transform: rotate(5deg); }
      100% { top: 0px; -moz-transform: rotate(0); }
    }
}

@mixin bottombar-x-rotation(){
    @keyframes bottombar-x {
      0% {bottom: 0px; transform: rotate(0deg);}
      45% {bottom: 6px; transform: rotate(-145deg);}
      75% {transform: rotate(-130deg);}
      100% {transform: rotate(-135deg);}
    }
    @-webkit-keyframes bottombar-x {
      0% {bottom: 0px; -webkit-transform: rotate(0deg);}
      45% {bottom: 6px; -webkit-transform: rotate(-145deg);}
      75% {-webkit-transform: rotate(-130deg);}
      100% {-webkit-transform: rotate(-135deg);}
    }
    @-moz-keyframes bottombar-x {
      0% {bottom: 0px; -moz-transform: rotate(0deg);}
      45% {bottom: 6px; -moz-transform: rotate(-145deg);}
      75% {-moz-transform: rotate(-130deg);}
      100% {-moz-transform: rotate(-135deg);}
    }
}

@mixin bottombar-back-rotation{
    @keyframes bottombar-back {
      0% { bottom: 6px;transform: rotate(-135deg);}
      45% { transform: rotate(10deg);}
      75% { transform: rotate(-5deg);}
      100% { bottom: 0px;transform: rotate(0);}
    }
    @-webkit-keyframes bottombar-back {
      0% {bottom: 6px;-webkit-transform: rotate(-135deg);}
      45% {-webkit-transform: rotate(10deg);}
      75% {-webkit-transform: rotate(-5deg);}
      100% {bottom: 0px;-webkit-transform: rotate(0);}
    }
    @-moz-keyframes bottombar-back {
      0% {bottom: 6px;-moz-transform: rotate(-135deg);}
      45% {-moz-transform: rotate(10deg);}
      75% {-moz-transform: rotate(-5deg);}
      100% {bottom: 0px;-moz-transform: rotate(0);}
    }

}




File: /assets\sass\paper\_alerts.scss
.alert{
    border: 0;
    border-radius: 0;
    color: #FFFFFF;
    padding: 10px 15px;
    font-size: 14px;
    
    .container &{
        border-radius: 4px;
    
    }
    .navbar &{
        border-radius: 0;
        left: 0;
        position: absolute;
        right: 0;
        top: 85px;
        width: 100%;
        z-index: 3;
    }
    .navbar:not(.navbar-transparent) &{
        top: 70px;
    }
    
    span[data-notify="icon"]{
        font-size: 30px;
        display: block;
        left: 15px;
        position: absolute;
        top: 50%;
        margin-top: -20px;
    }
    
    .close ~ span{
        display: block;
        max-width: 89%;
    }
    
    &[data-notify="container"]{
        padding: 10px 10px 10px 20px;
        border-radius: $border-radius-base;
    }
    
    &.alert-with-icon{
        padding-left: 65px;
    }
}
.alert-info{
    background-color: $bg-info;
    color: $info-states-color;
}
.alert-success {
    background-color: $bg-success;
    color: $success-states-color;
}
.alert-warning {
    background-color: $bg-warning;
    color: $warning-states-color;
}
.alert-danger {
    background-color: $bg-danger;
    color: $danger-states-color;
}



File: /assets\sass\paper\_buttons.scss
.btn,
.navbar .navbar-nav > li > a.btn{
    border-radius: $border-radius-btn-base;
    box-sizing: border-box;
    border-width: $border-thick;
    background-color: $transparent-bg;
    font-size: $font-size-base;
    font-weight: $font-weight-semi;
    
    padding: $padding-base-vertical $padding-base-horizontal;
    
    @include btn-styles($default-color, $default-states-color);
    @include transition($fast-transition-time, linear);
    
    &:hover,
    &:focus{
        outline: 0 !important;
    }
    &:active,
    &.active,
    .open > &.dropdown-toggle {
         @include box-shadow(none);
         outline: 0 !important;
    }
    
    &.btn-icon{
        padding: $padding-base-vertical;
    } 
}

.btn-group .btn + .btn, 
.btn-group .btn + .btn-group, 
.btn-group .btn-group + .btn, 
.btn-group .btn-group + .btn-group{
    margin-left: -2px;
}

// Apply the mixin to the buttons
//.btn-default { @include btn-styles($default-color, $default-states-color); }
.navbar .navbar-nav > li > a.btn-primary, .btn-primary { @include btn-styles($primary-color, $primary-states-color); }
.navbar .navbar-nav > li > a.btn-success, .btn-success { @include btn-styles($success-color, $success-states-color); }
.navbar .navbar-nav > li > a.btn-info, .btn-info    { @include btn-styles($info-color, $info-states-color); }
.navbar .navbar-nav > li > a.btn-warning, .btn-warning { @include btn-styles($warning-color, $warning-states-color); }
.navbar .navbar-nav > li > a.btn-danger, .btn-danger  { @include btn-styles($danger-color, $danger-states-color); }
.btn-neutral { 
    @include btn-styles($white-color, $white-color);
    
    &:hover,
    &:focus{
        color: $default-color;
    }
    
    &:active,
    &.active,
    .open > &.dropdown-toggle{
         background-color: $white-color;
         color: $default-color;
    }    
    
    &.btn-fill{
        color: $default-color;
    }
    &.btn-fill:hover,
    &.btn-fill:focus{
        color: $default-states-color;
    }
    
    &.btn-simple:active,
    &.btn-simple.active{
        background-color: transparent;
    }
}

.btn{
     &:disabled,
     &[disabled],
     &.disabled{
        @include opacity(.5);
    }
}
.btn-simple{
    border: $none;
    padding: $padding-base-vertical $padding-base-horizontal;
    
    &.btn-icon{
        padding: $padding-base-vertical;
    }
}
.btn-lg{
   @include btn-size($padding-large-vertical, $padding-large-horizontal, $font-size-large, $border-radius-btn-large, $line-height-small);
   font-weight: $font-weight-normal;
}
.btn-sm{
    @include btn-size($padding-small-vertical, $padding-small-horizontal, $font-size-small, $border-radius-btn-small, $line-height-small);    
}
.btn-xs {
    @include btn-size($padding-xs-vertical, $padding-xs-horizontal, $font-size-xs, $border-radius-btn-small, $line-height-small);
}
.btn-wd {
    min-width: 140px;
}

.btn-group.select{
    width: 100%;
}
.btn-group.select .btn{
    text-align: left;
}
.btn-group.select .caret{
    position: absolute;
    top: 50%;
    margin-top: -1px;
    right: 8px;
}


File: /assets\sass\paper\_cards.scss
.card{
    border-radius: $border-radius-extreme;
    box-shadow: 0 2px 2px rgba(204, 197, 185, 0.5);
    background-color: #FFFFFF;
    color: $card-black-color;
    margin-bottom: 20px;
    position: relative;
    z-index: 1;

    .image{
        width: 100%;
        overflow: hidden;
        height: 260px;
        border-radius: $border-radius-extreme $border-radius-extreme 0 0;
        position: relative;
        -webkit-transform-style: preserve-3d;
        -moz-transform-style: preserve-3d;
        transform-style: preserve-3d;

        img {
            width: 100%;
        }
    }
    .content{
        padding: 15px 15px 10px 15px;
    }
    .header{
        padding: 20px 20px 0;
    }
    .description{
        font-size: $font-paragraph;
        color: $font-color;
    }

    h6{
        font-size: $font-size-small;
        margin: 0;
    }
    .category,
    label{
        font-size: $font-size-base;
        font-weight: $font-weight-normal;
        color: $dark-gray;
        margin-bottom: 0px;
        i{
            font-size: $font-paragraph;
        }
    }

    label{
        font-size: 15px;
        margin-bottom: 5px;
    }

    .title{
        margin: $none;
        color: $card-black-color;
        font-weight: $font-weight-light;
    }
    .avatar{
        width: 50px;
        height: 50px;
        overflow: hidden;
        border-radius: 50%;
        margin-right: 5px;
    }
    .footer{
        padding: 0;
        line-height: 30px;

        .legend{
            padding: 5px 0;
        }

        hr{
            margin-top: 5px;
            margin-bottom: 5px;
        }
    }
    .stats{
        color: #a9a9a9;
        font-weight: 300;
        i{
            margin-right: 2px;
            min-width: 15px;
            display: inline-block;
        }
    }
    .footer div{
        display: inline-block;
    }

    .author{
        font-size: $font-size-small;
        font-weight: $font-weight-bold;
        text-transform: uppercase;
    }
    .author i{
        font-size: $font-size-base;
    }

    &.card-separator:after{
        height: 100%;
        right: -15px;
        top: 0;
        width: 1px;
        background-color: $medium-gray;
        content: "";
        position: absolute;
    }

    .ct-chart{
        margin: 30px 0 30px;
        height: 245px;
    }

    .table{
        tbody td:first-child,
        thead th:first-child{
            padding-left: 15px;
        }

        tbody td:last-child,
        thead th:last-child{
            padding-right: 15px;
        }
    }

    .alert{
        border-radius: $border-radius-base;
        position: relative;

        &.alert-with-icon{
            padding-left: 65px;
        }
    }
    .icon-big{
        font-size: 3em;
        min-height: 64px;
    }
    .numbers{
        font-size: 2em;
        text-align: right;
        p{
            margin: 0;
        }
    }
    ul.team-members{
        li{
            padding: 10px 0px;
            &:not(:last-child){
                border-bottom: 1px solid $medium-pale-bg;
            }
        }
    }
}
.card-user{
    .image{
        border-radius: 8px 8px 0 0;
        height: 150px;
        position: relative;
        overflow: hidden;

        img{
            width: 100%;
        }
    }
    .image-plain{
        height: 0;
        margin-top: 110px;
    }
    .author{
        text-align: center;
        text-transform: none;
        margin-top: -65px;
        .title{
            color: $default-states-color;
            small{
                color: $card-muted-color;
            }
        }
    }
    .avatar{
        width: 100px;
        height: 100px;
        border-radius: 50%;
        position: relative;
        margin-bottom: 15px;

        &.border-white{
            border: 5px solid $white-color;
        }
        &.border-gray{
            border: 5px solid $card-muted-color;
        }
    }
    .title{
        font-weight: 600;
        line-height: 24px;
    }
    .description{
        margin-top: 10px;
    }
    .content{
        min-height: 200px;
    }

    &.card-plain{
        .avatar{
            height: 190px;
            width: 190px;
        }
    }
}

.card-map{
    .map{
        height: 500px;
        padding-top: 20px;

        > div{
            height: 100%;
        }
    }
}
.card-user,
.card-price{
    .footer{
        padding: 5px 15px 10px;
    }
    hr{
        margin: 5px 15px;
    }
}
.card-plain{
    background-color: transparent;
    box-shadow: none;
    border-radius: 0;

    .image{
        border-radius: 4px;
    }
}


File: /assets\sass\paper\_chartist.scss
@mixin ct-responsive-svg-container($width: 100%, $ratio: $ct-container-ratio) {
  display: block;
  position: relative;
  width: $width;

  &:before {
    display: block;
    float: left;
    content: "";
    width: 0;
    height: 0;
    padding-bottom: $ratio * 100%;
  }

  &:after {
    content: "";
    display: table;
    clear: both;
  }

  > svg {
    display: block;
    position: absolute;
    top: 0;
    left: 0;
  }
}

@mixin ct-align-justify($ct-text-align: $ct-text-align, $ct-text-justify: $ct-text-justify) {
  -webkit-box-align: $ct-text-align;
  -webkit-align-items: $ct-text-align;
  -ms-flex-align: $ct-text-align;
  align-items: $ct-text-align;
  -webkit-box-pack: $ct-text-justify;
  -webkit-justify-content: $ct-text-justify;
  -ms-flex-pack: $ct-text-justify;
  justify-content: $ct-text-justify;
  // Fallback to text-align for non-flex browsers
  @if($ct-text-justify == 'flex-start') {
    text-align: left;
  } @else if ($ct-text-justify == 'flex-end') {
    text-align: right;
  } @else {
    text-align: center;
  }
}

@mixin ct-flex() {
  // Fallback to block
  display: block;
  display: -webkit-box;
  display: -moz-box;
  display: -ms-flexbox;
  display: -webkit-flex;
  display: flex;
}

@mixin ct-chart-label($ct-text-color: $ct-text-color, $ct-text-size: $ct-text-size, $ct-text-line-height: $ct-text-line-height) {
  fill: $ct-text-color;
  color: $ct-text-color;
  font-size: $ct-text-size;
  line-height: $ct-text-line-height;
}

@mixin ct-chart-grid($ct-grid-color: $ct-grid-color, $ct-grid-width: $ct-grid-width, $ct-grid-dasharray: $ct-grid-dasharray) {
  stroke: $ct-grid-color;
  stroke-width: $ct-grid-width;

  @if ($ct-grid-dasharray) {
    stroke-dasharray: $ct-grid-dasharray;
  }
}

@mixin ct-chart-point($ct-point-size: $ct-point-size, $ct-point-shape: $ct-point-shape) {
  stroke-width: $ct-point-size;
  stroke-linecap: $ct-point-shape;
}

@mixin ct-chart-line($ct-line-width: $ct-line-width, $ct-line-dasharray: $ct-line-dasharray) {
  fill: none;
  stroke-width: $ct-line-width;

  @if ($ct-line-dasharray) {
    stroke-dasharray: $ct-line-dasharray;
  }
}

@mixin ct-chart-area($ct-area-opacity: $ct-area-opacity) {
  stroke: none;
  fill-opacity: $ct-area-opacity;
}

@mixin ct-chart-bar($ct-bar-width: $ct-bar-width) {
  fill: none;
  stroke-width: $ct-bar-width;
}

@mixin ct-chart-donut($ct-donut-width: $ct-donut-width) {
  fill: none;
  stroke-width: $ct-donut-width;
}

@mixin ct-chart-series-color($color) {
  .#{$ct-class-point}, .#{$ct-class-line}, .#{$ct-class-bar}, .#{$ct-class-slice-donut} {
    stroke: $color;
  }

  .#{$ct-class-slice-pie}, .#{$ct-class-area} {
    fill: $color;
  }
}

@mixin ct-chart($ct-container-ratio: $ct-container-ratio, $ct-text-color: $ct-text-color, $ct-text-size: $ct-text-size, $ct-grid-color: $ct-grid-color, $ct-grid-width: $ct-grid-width, $ct-grid-dasharray: $ct-grid-dasharray, $ct-point-size: $ct-point-size, $ct-point-shape: $ct-point-shape, $ct-line-width: $ct-line-width, $ct-bar-width: $ct-bar-width, $ct-donut-width: $ct-donut-width, $ct-series-names: $ct-series-names, $ct-series-colors: $ct-series-colors) {

  .#{$ct-class-label} {
    @include ct-chart-label($ct-text-color, $ct-text-size);
  }

  .#{$ct-class-chart-line} .#{$ct-class-label},
  .#{$ct-class-chart-bar} .#{$ct-class-label} {
    @include ct-flex();
  }

  .#{$ct-class-label}.#{$ct-class-horizontal}.#{$ct-class-start} {
    @include ct-align-justify(flex-end, flex-start);
    // Fallback for browsers that don't support foreignObjects
    text-anchor: start;
  }

  .#{$ct-class-label}.#{$ct-class-horizontal}.#{$ct-class-end} {
    @include ct-align-justify(flex-start, flex-start);
    // Fallback for browsers that don't support foreignObjects
    text-anchor: start;
  }

  .#{$ct-class-label}.#{$ct-class-vertical}.#{$ct-class-start} {
    @include ct-align-justify(flex-end, flex-end);
    // Fallback for browsers that don't support foreignObjects
    text-anchor: end;
  }

  .#{$ct-class-label}.#{$ct-class-vertical}.#{$ct-class-end} {
    @include ct-align-justify(flex-end, flex-start);
    // Fallback for browsers that don't support foreignObjects
    text-anchor: start;
  }

  .#{$ct-class-chart-bar} .#{$ct-class-label}.#{$ct-class-horizontal}.#{$ct-class-start} {
    @include ct-align-justify(flex-end, center);
    // Fallback for browsers that don't support foreignObjects
    text-anchor: start;
  }

  .#{$ct-class-chart-bar} .#{$ct-class-label}.#{$ct-class-horizontal}.#{$ct-class-end} {
    @include ct-align-justify(flex-start, center);
    // Fallback for browsers that don't support foreignObjects
    text-anchor: start;
  }

  .#{$ct-class-chart-bar}.#{$ct-class-horizontal-bars} .#{$ct-class-label}.#{$ct-class-horizontal}.#{$ct-class-start} {
    @include ct-align-justify(flex-end, flex-start);
    // Fallback for browsers that don't support foreignObjects
    text-anchor: start;
  }

  .#{$ct-class-chart-bar}.#{$ct-class-horizontal-bars} .#{$ct-class-label}.#{$ct-class-horizontal}.#{$ct-class-end} {
    @include ct-align-justify(flex-start, flex-start);
    // Fallback for browsers that don't support foreignObjects
    text-anchor: start;
  }

  .#{$ct-class-chart-bar}.#{$ct-class-horizontal-bars} .#{$ct-class-label}.#{$ct-class-vertical}.#{$ct-class-start} {
    //@include ct-chart-label($ct-text-color, $ct-text-size, center, $ct-vertical-text-justify);
    @include ct-align-justify(center, flex-end);
    // Fallback for browsers that don't support foreignObjects
    text-anchor: end;
  }

  .#{$ct-class-chart-bar}.#{$ct-class-horizontal-bars} .#{$ct-class-label}.#{$ct-class-vertical}.#{$ct-class-end} {
    @include ct-align-justify(center, flex-start);
    // Fallback for browsers that don't support foreignObjects
    text-anchor: end;
  }

  .#{$ct-class-grid} {
    @include ct-chart-grid($ct-grid-color, $ct-grid-width, $ct-grid-dasharray);
  }

  .#{$ct-class-point} {
    @include ct-chart-point($ct-point-size, $ct-point-shape);
  }

  .#{$ct-class-line} {
    @include ct-chart-line($ct-line-width);
  }

  .#{$ct-class-area} {
    @include ct-chart-area();
  }

  .#{$ct-class-bar} {
    @include ct-chart-bar($ct-bar-width);
  }

  .#{$ct-class-slice-donut} {
    @include ct-chart-donut($ct-donut-width);
  }

  @if $ct-include-colored-series {
    @for $i from 0 to length($ct-series-names) {
      .#{$ct-class-series}-#{nth($ct-series-names, $i + 1)} {
        $color: nth($ct-series-colors, $i + 1);

        @include ct-chart-series-color($color);
      }
    }
  }
}

@if $ct-include-classes {
  @include ct-chart();

  @if $ct-include-alternative-responsive-containers {
    @for $i from 0 to length($ct-scales-names) {
      .#{nth($ct-scales-names, $i + 1)} {
        @include ct-responsive-svg-container($ratio: nth($ct-scales, $i + 1));
      }
    }
  }
}

File: /assets\sass\paper\_checkbox-radio.scss
/*      Checkbox and radio         */
.checkbox,
.radio {
    margin-bottom: 12px;
    padding-left: 30px;
    position: relative;
    -webkit-transition: color,opacity 0.25s linear;
    transition: color,opacity 0.25s linear;
    font-size: $font-size-base;
    font-weight: normal;
    line-height: 1.5;
    color: $font-color;
    cursor: pointer;

    .icons {
      color: $font-color;
      display: block;
      height: 20px;
      left: 0;
      position: absolute;
      top: 0;
      width: 20px;
      text-align: center;
      line-height: 21px;
      font-size: 20px;
      cursor: pointer;
      -webkit-transition: color,opacity 0.15s linear;
      transition: color,opacity 0.15s linear;

       opacity: .50;
    }


    &.checked{
        .icons{
            opacity: 1;
        }
    }

    input{
        outline: none !important;
        display: none;
    }
}

.checkbox,
.radio{
    label{
        padding-left: 10px;
    }
}

.checkbox .icons .first-icon,
.radio .icons .first-icon,
.checkbox .icons .second-icon,
.radio .icons .second-icon {
  display: inline-table;
  position: absolute;
  left: 0;
  top: 0;
  background-color: transparent;
  margin: 0;
  @include opacity(1);
}
.checkbox .icons .second-icon,
.radio .icons .second-icon {
  @include opacity(0);
}
.checkbox:hover,
.radio:hover {
  -webkit-transition: color 0.2s linear;
  transition: color 0.2s linear;
}
.checkbox:hover .first-icon,
.radio:hover .first-icon {
 @include opacity(0);
}
.checkbox:hover .second-icon,
.radio:hover .second-icon {
 @include opacity (1);
}
.checkbox.checked,
.radio.checked {
//   color: $info-color;
}
.checkbox.checked .first-icon,
.radio.checked .first-icon {
  opacity: 0;
  filter: alpha(opacity=0);
}
.checkbox.checked .second-icon,
.radio.checked .second-icon {
  opacity: 1;
  filter: alpha(opacity=100);
//   color: $info-color;
  -webkit-transition: color 0.2s linear;
  transition: color 0.2s linear;
}
.checkbox.disabled,
.radio.disabled {
  cursor: default;
  color: $medium-gray;
}
.checkbox.disabled .icons,
.radio.disabled .icons {
  color: $medium-gray;
}
.checkbox.disabled .first-icon,
.radio.disabled .first-icon {
  opacity: 1;
  filter: alpha(opacity=100);
}
.checkbox.disabled .second-icon,
.radio.disabled .second-icon {
  opacity: 0;
  filter: alpha(opacity=0);
}
.checkbox.disabled.checked .icons,
.radio.disabled.checked .icons {
  color: $medium-gray;
}
.checkbox.disabled.checked .first-icon,
.radio.disabled.checked .first-icon {
  opacity: 0;
  filter: alpha(opacity=0);
}
.checkbox.disabled.checked .second-icon,
.radio.disabled.checked .second-icon {
  opacity: 1;
  color: $medium-gray;
  filter: alpha(opacity=100);
}


File: /assets\sass\paper\_dropdown.scss
.dropdown-menu{
    background-color: $pale-bg;
    border: 0 none;
    border-radius: $border-radius-extreme;
    display: block;
    margin-top: 10px;
    padding: 0px;
    position: absolute;
    visibility: hidden;
    z-index: 9000;  
    
    @include opacity(0); 
    @include box-shadow($dropdown-shadow);
        
//     the style for opening dropdowns on mobile devices; for the desktop version check the _responsive.scss file    
    .open &{
        @include opacity(1);
        visibility: visible;
    }    
    
    .divider{
        background-color: $medium-pale-bg;
        margin: 0px;
    }
    
    .dropdown-header{
        color: $dark-gray;
        font-size: $font-size-small;
        padding: $padding-dropdown-vertical $padding-dropdown-horizontal;
    }
    
//     the style for the dropdown menu that appears under select, it is different from the default one
    .select &{
       border-radius: $border-radius-bottom; 
       @include box-shadow(none);
       @include transform-origin($select-coordinates);
       @include transform-scale(1);
       @include transition($fast-transition-time, $transition-linear);
       margin-top: -20px;
    }
    .select.open &{
        margin-top: -1px;
    }
    
    > li > a {
       color: $font-color;
       font-size: $font-size-base;
       padding: $padding-dropdown-vertical $padding-dropdown-horizontal;
       @include transition-none();
       
       img{
           margin-top: -3px;
       }
    }
    > li > a:focus{
        outline: 0 !important;
    }

    .btn-group.select &{
        min-width: 100%;
    }
    
    > li:first-child > a{
       border-top-left-radius: $border-radius-extreme;
       border-top-right-radius: $border-radius-extreme;
    }
    
    > li:last-child > a{
        border-bottom-left-radius: $border-radius-extreme;
        border-bottom-right-radius: $border-radius-extreme;
    }
    
    .select & > li:first-child > a{
        border-radius: 0;
        border-bottom: 0 none;
    }
    
    > li > a:hover,
    > li > a:focus {
        background-color: $default-color;
        color: $fill-font-color;
        opacity: 1;
        text-decoration: none;
    }
    
    &.dropdown-primary > li > a:hover,
    &.dropdown-primary > li > a:focus{
        background-color: $primary-color;
    }
    &.dropdown-info > li > a:hover,
    &.dropdown-info > li > a:focus{
        background-color: $info-color;
    }
    &.dropdown-success > li > a:hover,
    &.dropdown-success > li > a:focus{
        background-color: $success-color;
    }
    &.dropdown-warning > li > a:hover,
    &.dropdown-warning > li > a:focus{
        background-color: $warning-color;
    }
    &.dropdown-danger > li > a:hover,
    &.dropdown-danger > li > a:focus{
        background-color: $danger-color;
    }

}

//fix bug for the select items in btn-group 
.btn-group.select{
    overflow: hidden;
}
.btn-group.select.open{
    overflow: visible;
}


File: /assets\sass\paper\_footers.scss
.footer{
    background-attachment: fixed;
    position: relative;
    line-height: 20px;
    nav {
        ul {
          list-style: none;
          margin: 0;
          padding: 0;
          font-weight: normal;
            li{
                    display: inline-block;
                    padding: 10px 15px;
                    margin: 15px 3px;
                    line-height: 20px;
                    text-align: center;
            }
            a:not(.btn){
                color: $font-color;
                display: block;
                margin-bottom: 3px;

                &:focus,
                &:hover{
                    color: $default-states-color;
                }
            }
        }
    }
    .copyright{
        color: $font-color;
        padding: 10px 15px;
        font-size: 14px;
        white-space: nowrap;
        margin: 15px 3px;
        line-height: 20px;
        text-align: center;
    }
    .heart{
        color: $danger-color;
    }
}


File: /assets\sass\paper\_inputs.scss
.form-control::-moz-placeholder{
   @include placeholder($medium-gray,1);
}
.form-control:-moz-placeholder{
   @include placeholder($medium-gray,1);
}  
.form-control::-webkit-input-placeholder{
   @include placeholder($medium-gray,1); 
} 
.form-control:-ms-input-placeholder{
   @include placeholder($medium-gray,1);
}

.form-control {
    background-color: $gray-input-bg;
    border: medium none;
    border-radius: $border-radius-base;
    color: $font-color;
    font-size: $font-size-base;
    transition: background-color 0.3s ease 0s;
    @include input-size($padding-base-vertical, $padding-base-horizontal, $height-base);
    @include box-shadow(none);
    
    &:focus{
           background-color: $white-bg;
           @include box-shadow(none);
           outline: 0 !important;       
    }
    
    .has-success &,
    .has-error &,
    .has-success &:focus,
    .has-error &:focus{
        @include box-shadow(none);
    }
    
    .has-success &{
        background-color: $success-input-bg;
        color: $success-color;
        &.border-input{
             border: 1px solid $success-color;
        }
    }
    .has-success &:focus{
        background-color: $white-bg;
    }
    .has-error &{
        background-color: $danger-input-bg;
        color: $danger-color;
        &.border-input{
             border: 1px solid $danger-color;
        }
    }
    .has-error &:focus{
        background-color: $white-bg;
    }
    
    & + .form-control-feedback{
        border-radius: $border-radius-large;
        font-size: $font-size-base;
        margin-top: -7px;
        position: absolute;
        right: 10px;
        top: 50%;
        vertical-align: middle;
    }
    &.border-input{
         border: 1px solid $table-line-color;
    }
    .open &{
        border-bottom-color: transparent;
    }
}

.input-lg{
    height: 55px;
    padding: $padding-large-vertical $padding-large-horizontal;
}

.has-error{
    .form-control-feedback, .control-label{
        color: $danger-color;
    }
}
.has-success{
    .form-control-feedback, .control-label{
        color: $success-color;
    }
}


.input-group-addon {
    background-color: $gray-input-bg;
    border: medium none;
    border-radius: $border-radius-base;
    
    
    .has-success &,
    .has-error &{
        background-color: $white-color;
    }
    .has-error .form-control:focus + &{
        color: $danger-color;
    }
    .has-success .form-control:focus + &{
        color: $success-color;
    }
    .form-control:focus + &,
    .form-control:focus ~ &{
        background-color: $white-color;
    }
}
.border-input{ 
    .input-group-addon{
        border: solid 1px $table-line-color;
    }
}
.input-group{
    margin-bottom: 15px;
}
.input-group[disabled]{
    .input-group-addon{
        background-color: $light-gray;
    }
}
.input-group .form-control:first-child, 
.input-group-addon:first-child,  
.input-group-btn:first-child > .dropdown-toggle, 
.input-group-btn:last-child > .btn:not(:last-child):not(.dropdown-toggle) {
    border-right: 0 none;
}
.input-group .form-control:last-child, 
.input-group-addon:last-child,  
.input-group-btn:last-child > .dropdown-toggle, 
.input-group-btn:first-child > .btn:not(:first-child) {
    border-left: 0 none;
}
.form-control[disabled], .form-control[readonly], fieldset[disabled] .form-control {
    background-color: $light-gray;
    cursor: not-allowed;
    @include placeholder($dark-gray,1);
}
.form-control[disabled]::-moz-placeholder{
   @include placeholder($dark-gray,1);
}
.form-control[disabled]:-moz-placeholder{
   @include placeholder($medium-gray,1);
}  
.form-control[disabled]::-webkit-input-placeholder{
   @include placeholder($medium-gray,1); 
} 
.form-control[disabled]:-ms-input-placeholder{
   @include placeholder($medium-gray,1);
}
.input-group-btn .btn{
    border-width: $border-thin;
    padding: $padding-round-vertical $padding-base-horizontal;
}
.input-group-btn .btn-default:not(.btn-fill){
    border-color: $medium-gray;
}

.input-group-btn:last-child > .btn{
    margin-left: 0;
}
textarea.form-control{
    max-width: 100%;
    padding: 10px 18px;
    resize: none;
}



File: /assets\sass\paper\_misc.scss
/*     General overwrite     */
body{
    color: $font-color;
    font-size: $font-size-base;
    font-family: 'Muli', Arial, sans-serif;
    .wrapper{
        min-height: 100vh;
        position: relative;
    }
}
a{
  color: $info-color;

  &:hover, &:focus{
     color: $info-states-color;
     text-decoration: none;
  }
}

a:focus, a:active,
button::-moz-focus-inner,
input::-moz-focus-inner,
select::-moz-focus-inner,
input[type="file"] > input[type="button"]::-moz-focus-inner{
    outline:0 !important;
}
.ui-slider-handle:focus,
.navbar-toggle,
input:focus,
button:focus {
    outline : 0 !important;
}

/*           Animations              */
.form-control,
.input-group-addon,
.tagsinput,
.navbar,
.navbar .alert{
    @include transition($general-transition-time, $transition-linear);
}

.sidebar .nav a,
.table > tbody > tr .td-actions .btn{
    @include transition($fast-transition-time, $transition-ease-in);
}

.btn{
    @include transition($ultra-fast-transition-time, $transition-ease-in);
}
.fa{
    width: 21px;
    text-align: center;
}
.fa-base{
    font-size: 1.25em !important;
}

.margin-top{
    margin-top: 50px;
}
hr{
    border-color: $medium-pale-bg;
}
.wrapper{
    position: relative;
    top: 0;
    height: 100vh;
}


File: /assets\sass\paper\_mixins.scss
//Utilities 

@import "mixins/transparency";
@import "mixins/vendor-prefixes";


//Components

@import "mixins/buttons";
@import "mixins/inputs";
@import "mixins/labels";
@import "mixins/tabs";
@import "mixins/navbars";
@import "mixins/icons";
@import "mixins/cards";
@import "mixins/chartist";
@import "mixins/sidebar";

File: /assets\sass\paper\_navbars.scss
.nav {
    > li{
        > a:hover,
        > a:focus{
            background-color: transparent;
        }
    }
}
.navbar{
    border: $none;
    border-radius: 0;
    font-size: $font-size-navbar;
    z-index: 3;

    .navbar-brand{
        font-weight: $font-weight-bold;
        margin: $navbar-margin-brand;
        padding: $navbar-padding-brand;
        font-size: $font-size-large-navbar;
    }
    .navbar-nav{
         > li > a {
             line-height: 1.42857;
             margin: $navbar-margin-a;
             padding: $navbar-padding-a;

            i,
            p{
                display: inline-block;
                margin: 0;
            }
            i{
                position: relative;
                top: 1px;
            }
         }
         > li > a.btn{
             margin: $navbar-margin-a-btn;
             padding: $padding-base-vertical $padding-base-horizontal;
         }
    }
    .btn{
       margin: $navbar-margin-btn;
       font-size: $font-size-base;
    }
    .btn-simple{
        font-size: $font-size-medium;
    }
}

.navbar-nav > li > .dropdown-menu{
    border-radius: $border-radius-extreme;
    margin-top: -5px;
}

.navbar-default {
    background-color: $bg-nude;
    border-bottom: 1px solid $medium-gray;

    .brand{
        color: $font-color !important;
    }
    .navbar-nav{
        > li > a:not(.btn){
            color: $dark-gray;
        }

        > .active > a,
        > .active > a:not(.btn):hover,
        > .active > a:not(.btn):focus,
        > li > a:not(.btn):hover,
        > li > a:not(.btn):focus {
            background-color: transparent;
            border-radius: 3px;
            color: $info-color;
            @include opacity(1);
        }

        > .dropdown > a:hover .caret,
        > .dropdown > a:focus .caret {
            border-bottom-color: $info-color;
            border-top-color: $info-color;

        }

        > .open > a,
        > .open > a:hover,
        > .open > a:focus{
            background-color: transparent;
            color: $info-color;
        }

        .navbar-toggle:hover,.navbar-toggle:focus {
            background-color: transparent;
        }

    }

    &:not(.navbar-transparent) .btn-default:hover{
        color: $info-color;
        border-color: $info-color;
    }
    &:not(.navbar-transparent) .btn-neutral,
    &:not(.navbar-transparent) .btn-neutral:hover,
    &:not(.navbar-transparent) .btn-neutral:active{
            color: $dark-gray;
        }
}

.navbar-form{
   @include box-shadow(none);
   .form-control{
        @include light-form();
        height: 22px;
        font-size: $font-size-navbar;
        line-height: $line-height-general;
        color: $light-gray;
    }
    .navbar-transparent & .form-control,
    [class*="navbar-ct"] & .form-control{
        color: $white-color;
        border: $none;
        border-bottom: 1px solid rgba($white-color,.6);
    }

}

.navbar-ct-primary{
    @include navbar-color($bg-primary);
}
.navbar-ct-info{
    @include navbar-color($bg-info);
}
.navbar-ct-success{
    @include navbar-color($bg-success);
}
.navbar-ct-warning{
    @include navbar-color($bg-warning);
}
.navbar-ct-danger{
    @include navbar-color($bg-danger);
}

.navbar-transparent{
    padding-top: 15px;
    background-color: transparent;
    border-bottom: 1px solid transparent;
}

.navbar-toggle{
    margin-top: 19px;
    margin-bottom: 19px;
    border: $none;

    .icon-bar {
        background-color: $white-color;
    }
     .navbar-collapse,
     .navbar-form {
        border-color: transparent;
    }

    &.navbar-default .navbar-toggle:hover,
    &.navbar-default .navbar-toggle:focus {
        background-color: transparent;
    }
}

.navbar-transparent, [class*="navbar-ct"]{

    .navbar-brand{

        @include opacity(.9);

        &:focus,

        &:hover{

            background-color: transparent;

            @include opacity(1);

        }

    }

    .navbar-brand:not([class*="text"]){

        color: $white-color;

    }

    .navbar-nav{

        > li > a:not(.btn){

            color: $white-color;

            border-color: $white-color;

            @include opacity(0.8);

        }

        > .active > a:not(.btn),

        > .active > a:hover:not(.btn),

        > .active > a:focus:not(.btn),

        > li > a:hover:not(.btn),

        > li > a:focus:not(.btn){

            background-color: transparent;

            border-radius: 3px;

            color: $white-color;

            @include opacity(1);

        }

        .nav > li > a.btn:hover{

            background-color: transparent;

        }

        > .dropdown > a .caret,

        > .dropdown > a:hover .caret,

        > .dropdown > a:focus .caret{

            border-bottom-color: $white-color;

            border-top-color: $white-color;

        }

        > .open > a,

        > .open > a:hover,

        > .open > a:focus {

            background-color: transparent;

            color: $white-color;

            @include opacity(1);

        }

    }

    .btn-default{

        color: $white-color;

        border-color: $white-color;

    }

    .btn-default.btn-fill{

        color: $dark-gray;

        background-color: $white-color;

        @include opacity(.9);

    }

    .btn-default.btn-fill:hover,

    .btn-default.btn-fill:focus,

    .btn-default.btn-fill:active,

    .btn-default.btn-fill.active,

    .open .dropdown-toggle.btn-fill.btn-default{

        border-color: $white-color;

        @include opacity(1);

    }

}


File: /assets\sass\paper\_responsive.scss
@media (min-width: 992px){
    .navbar{
        min-height: 75px;
    }
    .navbar-form {
        margin-top: 21px;
        margin-bottom: 21px;
        padding-left: 5px;
        padding-right: 5px;
    }
    .navbar-search-form{
        display: none;
    }
    .navbar-nav > li > .dropdown-menu,
    .dropdown .dropdown-menu{
        transform: translate3d(0px, -40px, 0px);
        transition: all 0.3s cubic-bezier(0.215, 0.61, 0.355, 1) 0s, opacity 0.3s ease 0s, height 0s linear 0.35s;
    }
    .navbar-nav > li.open > .dropdown-menu, .dropdown.open .dropdown-menu{
        transform: translate3d(0px, 0px, 0px);
    }

    .navbar-nav > li > .dropdown-menu:before{
        border-bottom: 11px solid $medium-pale-bg;
        border-left: 11px solid rgba(0, 0, 0, 0);
        border-right: 11px solid rgba(0, 0, 0, 0);
        content: "";
        display: inline-block;
        position: absolute;
        right: 12px;
        top: -11px;
    }
    .navbar-nav > li > .dropdown-menu:after {
        border-bottom: 11px solid $pale-bg;
        border-left: 11px solid rgba(0, 0, 0, 0);
        border-right: 11px solid rgba(0, 0, 0, 0);
        content: "";
        display: inline-block;
        position: absolute;
        right: 12px;
        top: -10px;
    }

    .navbar-nav.navbar-left > li > .dropdown-menu:before{
        right: auto;
        left: 12px;
    }

    .navbar-nav.navbar-left > li > .dropdown-menu:after{
        right: auto;
        left: 12px;
    }

    .navbar{
        .navbar-header{
            margin-left: 10px;
        }
    }

    .footer:not(.footer-big){
        nav > ul{
           li:first-child{
             margin-left: 0;
           }
        }
    }

    body > .navbar-collapse.collapse{
        display: none !important;
    }

    .card{
        form{
            [class*="col-"]{
                padding: 6px;
            }
            [class*="col-"]:first-child{
                padding-left: 15px;
            }
            [class*="col-"]:last-child{
                padding-right: 15px;
            }
        }
    }
}

/*          Changes for small display      */

@media (max-width: 991px){
    .sidebar{
        display: none;
    }

    .main-panel{
        width: 100%;
    }
    .navbar-transparent{
        padding-top: 15px;
        background-color: rgba(0, 0, 0, 0.45);
    }
    body {
         position: relative;
    }
    h6{
        font-size: 1em;
    }
    .wrapper{
       @include transform-translate-x(0px);
       @include transition (0.33s, cubic-bezier(0.685, 0.0473, 0.346, 1));
       left: 0;
       background-color: white;
    }
    .navbar .container{
         left: 0;
          width: 100%;
         @include transition (0.33s, cubic-bezier(0.685, 0.0473, 0.346, 1));
         position: relative;
    }
    .navbar .navbar-collapse.collapse,
    .navbar .navbar-collapse.collapse.in,
    .navbar .navbar-collapse.collapsing{
        display: none !important;
    }

    .navbar-nav > li{
        float: none;
        position: relative;
        display: block;
    }

    .off-canvas-sidebar {
        position: fixed;
        display: block;
        top: 0;
        height: 100%;
        width: 230px;
        right: 0;
        z-index: 1032;
        visibility: visible;
        background-color: #999;
        overflow-y: visible;
        border-top: none;
        text-align: left;
        padding-right: 0px;
        padding-left: 0;

        @include transform-translate-x(230px);
        @include transition (0.33s, cubic-bezier(0.685, 0.0473, 0.346, 1));

        .sidebar-wrapper {
            position: relative;
            z-index: 3;
            overflow-y: scroll;
            height: 100%;
            box-shadow: inset 1px 0px 0px 0px $medium-gray;
        }

        .nav{
            margin-top: 0;
            padding: 10px $margin-base-vertical 0;

            > li{

                > a{
                    margin: 0px 0px;
                    color: $default-color;
                    text-transform: uppercase;
                    font-weight: 600;
                    font-size: $font-size-small;
                    line-height: $line-height-general;
                    padding: 10px 0;

                    &:hover,
                    &.active{
                        color: $default-states-color;
                    }

                    p,
                    .notification,
                    .caret,
                    {
                        display: inline-block;
                    }

                    .caret{
                        float: right;
                        position: relative;
                        top: 12px;
                    }

                    i{
                        font-size: 18px;
                        margin-right: 10px;
                        line-height: 26px;
                    }
                }

                &.active > a{

                    &:before{
                        border-right: none;
                        border-left:  12px solid $medium-gray;
                        border-top: 12px solid transparent;
                        border-bottom: 12px solid transparent;
                        right: auto;
                        margin-left: -$margin-base-vertical;
                        left: 0px;
                        top: 10px;
                    }

                    &:after{
                        border-right: none;
                        border-left: 12px solid $bg-nude;
                        border-top: 12px solid transparent;
                        border-bottom: 12px solid transparent;
                        right: auto;
                        margin-left: -$margin-base-vertical;
                        left: -1px;
                        top: 10px;
                    }
                }

            }



        }

        &::after{
            top: 0;
            left: 0;
            height: 100%;
            width: 100%;
            position: absolute;
            background-color: $bg-nude;
            background-image: linear-gradient(to bottom, rgba(0, 0, 0, 0) 0%, rgba(112, 112, 112, 0) 60%, rgba(186, 186, 186, 0.15) 100%);
            display: block;
            content: "";
            z-index: 1;
        }
        &.has-image::after{
            @include black-filter(.8);
        }

        .logo{
            position: relative;
            z-index: 4;
            padding-top: 11px;
            padding-bottom: 11px;
        }

        .divider{
            height: 1px;
            margin: 10px 0;
        }
    }
    .nav-open .navbar-collapse{
        @include transform-translate-x(0px);
    }
    .nav-open .navbar .container{
        left: -230px;
    }
    .nav-open .wrapper{
        left: 0;
        @include transform-translate-x(-230px);
    }
    .navbar-toggle .icon-bar {
          display: block;
          position: relative;
          background: #fff;
          width: 24px;
          height: 2px;
          border-radius: 1px;
          margin: 0 auto;
    }

    .navbar-header .navbar-toggle {
        margin: 10px 15px 10px 0;
        width: 40px;
        height: 40px;
    }
    .bar1,
    .bar2,
    .bar3 {
      outline: 1px solid transparent;
    }
    .bar1 {
      top: 0px;
      @include bar-animation($topbar-back);
    }
    .bar2 {
      opacity: 1;
    }
    .bar3 {
      bottom: 0px;
      @include bar-animation($bottombar-back);
    }
    .toggled .bar1 {
      top: 6px;
      @include bar-animation($topbar-x);
    }
    .toggled .bar2 {
      opacity: 0;
    }
    .toggled .bar3 {
      bottom: 6px;
      @include bar-animation($bottombar-x);
    }

    @include topbar-x-rotation();
    @include topbar-back-rotation();
    @include bottombar-x-rotation();
    @include bottombar-back-rotation();

    @-webkit-keyframes fadeIn {
      0% {opacity: 0;}
      100% {opacity: 1;}
    }
    @-moz-keyframes fadeIn {
      0% {opacity: 0;}
      100% {opacity: 1;}
    }
    @keyframes fadeIn {
      0% {opacity: 0;}
      100% {opacity: 1;}
    }

    .dropdown-menu .divider{
        background-color: rgba(229, 229, 229, 0.15);
    }

    .navbar-nav {
        margin: 1px 0;
    }

    .dropdown-menu {
        display: none;

        & > li > a{
            &:hover,
            &:focus{
                background-color: transparent;
            }
        }
    }

    .navbar-fixed-top {
        -webkit-backface-visibility: hidden;
    }
    #bodyClick {
        height: 100%;
        width: 100%;
        position: fixed;
        opacity: 0;
        top: 0;
        left: auto;
        right: 230px;
        content: "";
        z-index: 9999;
        overflow-x: hidden;
    }
    .form-control + .form-control-feedback{
        margin-top: -8px;
    }
    .navbar-toggle:hover,.navbar-toggle:focus {
        background-color: transparent !important;
    }
    .btn.dropdown-toggle{
        margin-bottom: 0;
    }
    .media-post .author{
        width: 20%;
        float: none !important;
        display: block;
        margin: 0 auto 10px;
    }
    .media-post .media-body{
        width: 100%;
    }

    .navbar-collapse.collapse{
        height: 100% !important;
    }
    .navbar-collapse.collapse.in {
        display: block;
    }
    .navbar-header .collapse, .navbar-toggle {
        display:block !important;
    }
    .navbar-header {
        float:none;
    }
    .navbar-nav .open .dropdown-menu {
        position: static;
        float: none;
        width: auto;
        margin-top: 0;
        background-color: transparent;
        border: 0;
        -webkit-box-shadow: none;
        box-shadow: none;
    }

    .main-panel > .content{
        padding-left: 0;
        padding-right: 0;
    }
    .nav .open > a{
        &,
        &:focus,
        &:hover{
            background-color: transparent;
        }

    }

    .footer .copyright{
        padding: 0px 15px;
        width: 100%;
    }
}

//overwrite table responsive for 768px screens

@media (min-width: 992px){
    .table-full-width{
        margin-left: -15px;
        margin-right: -15px;
    }
    .table-responsive{
        overflow: visible;
    }

}

@media (max-width: 991px){
    .table-responsive {
        width: 100%;
        margin-bottom: 15px;
        border: 1px solid #dddddd;
        overflow-x: scroll;
        overflow-y: hidden;
        -ms-overflow-style: -ms-autohiding-scrollbar;
        -webkit-overflow-scrolling: touch;
    }

}


File: /assets\sass\paper\_sidebar-and-main-panel.scss
.sidebar{
    position: absolute;
    top: 0;
    bottom: 0;
    left: 0;
    z-index: 1;
    background-size: cover;
    background-position: center center;
    .sidebar-wrapper{
        position: relative;
        max-height: none;
        min-height: 100%;
        overflow: hidden;
        width: 260px;
        z-index: 4;
        box-shadow: inset -1px 0px 0px 0px $medium-gray;
    }
    .sidebar-background{
        position: absolute;
        z-index: 1;
        height: 100%;
        width: 100%;
        display: block;
        top: 0;
        left: 0;
        background-size: cover;
        background-position: center center;
    }

}
.sidebar,
.off-canvas-sidebar{
    width: 260px;
    display: block;
    font-weight: 200;

    .logo{
        padding: 18px 0px;
        margin: 0 20px;

        p{
            float: left;
            font-size: 20px;
            margin: 10px 10px;
            line-height: 20px;
        }

        .simple-text{
            text-transform: uppercase;
            padding: $padding-small-vertical $padding-zero;
            display: block;
            font-size: $font-size-large;
            text-align: center;
            font-weight: $font-weight-normal;
            line-height: 30px;
        }
    }

    .nav{
        margin-top: 20px;

        li{
            > a{
                margin: 10px 0px;
                padding-left: 25px;
                padding-right: 25px;

                opacity: .7;
            }

            &:hover > a{
                opacity: 1;
            }

            &.active > a{
                color: $primary-color;
                opacity: 1;

                &:before{
                    border-right: 17px solid $medium-gray;
                    border-top: 17px solid transparent;
                    border-bottom: 17px solid transparent;
                    content: "";
                    display: inline-block;
                    position: absolute;
                    right: 0;
                    top: 8px;
                }

                &:after{
                    border-right: 17px solid $bg-nude;
                    border-top: 17px solid transparent;
                    border-bottom: 17px solid transparent;
                    content: "";
                    display: inline-block;
                    position: absolute;
                    right: -1px;
                    top: 8px;
                }
            }
        }

        p{
            margin: 0;
            line-height: 30px;
            font-size: 12px;
            font-weight: 600;
            text-transform: uppercase;
        }

        i{
            font-size: 24px;
            float: left;
            margin-right: 15px;
            line-height: 30px;
            width: 30px;
            text-align: center;
        }
    }

    &:after,
    &:before{
        display: block;
        content: "";
        position: absolute;
        width: 100%;
        height: 100%;
        top: 0;
        left: 0;
        z-index: 2;
        background:  $white-background-color;
    }

    &,
    &[data-background-color="white"]{
        @include sidebar-background-color($white-background-color, $default-color);
    }
    &[data-background-color="black"]{
        @include sidebar-background-color($black-background-color, $white-color);
    }

    &[data-active-color="primary"]{
        @include sidebar-active-color($primary-color);
    }
    &[data-active-color="info"]{
        @include sidebar-active-color($info-color);
    }
    &[data-active-color="success"]{
        @include sidebar-active-color($success-color);
    }
    &[data-active-color="warning"]{
        @include sidebar-active-color($warning-color);
    }
    &[data-active-color="danger"]{
        @include sidebar-active-color($danger-color);
    }

}

.main-panel{
    background-color: $bg-nude;
    position: relative;
    z-index: 2;
    float: right;
    width: $sidebar-width;
    min-height: 100%;

    > .content{
        padding: 30px 15px;
        min-height: calc(100% - 123px);
    }

    > .footer{
        border-top: 1px solid rgba(0, 0, 0, 0.1);
    }

    .navbar{
        margin-bottom: 0;
    }
}

.sidebar,
.main-panel{
    overflow: auto;
    max-height: 100%;
    height: 100%;
    -webkit-transition-property: top,bottom;
    transition-property: top,bottom;
    -webkit-transition-duration: .2s,.2s;
    transition-duration: .2s,.2s;
    -webkit-transition-timing-function: linear,linear;
    transition-timing-function: linear,linear;
    -webkit-overflow-scrolling: touch;
}


File: /assets\sass\paper\_tables.scss
.table{
    thead,
    tbody,
    tfoot{
        tr > th,
        tr > td{
            border-top: 1px solid $table-line-color;
        }
    }
   > thead > tr > th{
       border-bottom-width: 0;
       font-size: $font-size-h5;
       font-weight: $font-weight-light;
   }

   .radio,
   .checkbox{
       margin-top: 0;
       margin-bottom: 22px;
       padding: 0;
       width: 15px;
   }
   > thead > tr > th,
   > tbody > tr > th,
   > tfoot > tr > th,
   > thead > tr > td,
   > tbody > tr > td,
   > tfoot > tr > td{
       padding: 12px;
       vertical-align: middle;
   }

   .th-description{
       max-width: 150px;
   }
   .td-price{
       font-size: 26px;
       font-weight: $font-weight-light;
       margin-top: 5px;
       text-align: right;
   }
   .td-total{
        font-weight: $font-weight-bold;
        font-size: $font-size-h5;
        padding-top: 20px;
        text-align: right;
    }

   .td-actions .btn{

        &.btn-sm,
        &.btn-xs{
            padding-left: 3px;
            padding-right: 3px;
        }
    }

    > tbody > tr{
        position: relative;
    }
}
.table-striped{
    tbody > tr:nth-of-type(2n+1) {
        background-color: #fff;
    }
    tbody > tr:nth-of-type(2n) {
        background-color: $pale-bg;
    }
    > thead > tr > th,
    > tbody > tr > th,
    > tfoot > tr > th,
    > thead > tr > td,
    > tbody > tr > td,
    > tfoot > tr > td{
        padding: 15px 8px;
    }
}

File: /assets\sass\paper\_typography.scss
h1, .h1, h2, .h2, h3, .h3, h4, .h4, h5, .h5, h6, .h6, p, .navbar, .brand, a, .td-name, td{
    -moz-osx-font-smoothing: grayscale;
    -webkit-font-smoothing: antialiased;
    font-family: 'Muli', "Helvetica", Arial, sans-serif;
}

h1, .h1, h2, .h2, h3, .h3, h4, .h4{
    font-weight: $font-weight-normal;
    margin: $margin-large-vertical 0 $margin-base-vertical;
}

h1, .h1 {
    font-size: $font-size-h1;
}
h2, .h2{
    font-size: $font-size-h2;
}
h3, .h3{
    font-size: $font-size-h3;
    line-height: 1.4;
    margin: 20px 0 10px;
}
h4, .h4{
    font-size: $font-size-h4;
    font-weight: $font-weight-bold;
    line-height: 1.2em;
}
h5, .h5 {
    font-size: $font-size-h5;
    font-weight: $font-weight-normal;
    line-height: 1.4em;
    margin-bottom: 15px;
}
h6, .h6{
    font-size: $font-size-h6;
    font-weight: $font-weight-bold;
    text-transform: uppercase;
}
p{
    font-size: $font-paragraph;
    line-height: $line-height-general;
}

h1 small, h2 small, h3 small, h4 small, h5 small, h6 small, .h1 small, .h2 small, .h3 small, .h4 small, .h5 small, .h6 small, h1 .small, h2 .small, h3 .small, h4 .small, h5 .small, h6 .small, .h1 .small, .h2 .small, .h3 .small, .h4 .small, .h5 .small, .h6 .small {
    color: $dark-gray;
    font-weight: $font-weight-light;
    line-height: $line-height-general;
}

h1 small, h2 small, h3 small, h1 .small, h2 .small, h3 .small {
    font-size: 60%;
}
.title-uppercase{
    text-transform: uppercase;
}
blockquote{
    font-style: italic;
}
blockquote small{
    font-style: normal;
}
.text-muted{
    color: $medium-gray;
}
.text-primary, .text-primary:hover{
    color: $primary-states-color;
}
.text-info, .text-info:hover{
    color: $info-states-color;
}
.text-success, .text-success:hover{
    color: $success-states-color;
}
.text-warning, .text-warning:hover{
    color: $warning-states-color;
}
.text-danger, .text-danger:hover{
    color: $danger-states-color;
}
.glyphicon{
    line-height: 1;
}
strong{
    color: $default-states-color;
}
.icon-primary{
    color: $primary-color;
}
.icon-info{
    color: $info-color;
}
.icon-success{
    color: $success-color;
}
.icon-warning{
    color: $warning-color;
}
.icon-danger{
    color: $danger-color;
}
.chart-legend{
    .text-primary, .text-primary:hover{
        color: $primary-color;
    }
    .text-info, .text-info:hover{
        color: $info-color;
    }
    .text-success, .text-success:hover{
        color: $success-color;
    }
    .text-warning, .text-warning:hover{
        color: $warning-color;
    }
    .text-danger, .text-danger:hover{
        color: $danger-color;
    }
}


File: /assets\sass\paper\_variables.scss
$font-color:                 #66615b !default;
$fill-font-color:            rgba(255, 255, 255, 0.7);

$none:                       0   !default;
$border-thin:                1px !default;
$border-thick:               2px !default;

$white-color:                #FFFFFF !default;
$white-bg:                   #FFFFFF !default;

$smoke-bg:                   #F5F5F5 !default;
$pale-bg:                    #FFFCF5 !default;
$medium-pale-bg:             #F1EAE0 !default;

$table-line-color:           #CCC5B9 !default;
$muted-color:                #a49e93 !default;

$black-bg:                   rgba(30,30,30,.97) !default;

$black-color:                #333333 !default;
$black-hr:                   #444444 !default;

$white-background-color:        #FFFFFF !default;
$black-background-color:        #212120 !default;

$light-gray:                 #E3E3E3 !default;
$medium-gray:                #DDDDDD !default;
$dark-gray:                  #9A9A9A !default;

$gray-input-bg:              #fffcf5 !default;
$danger-input-bg:            #FFC0A4 !default;
$success-input-bg:           #ABF3CB !default;
$other-medium-gray:          #A49E93 !default;
$transparent-bg:             transparent !default;

$default-color:              #66615B !default;
$default-bg:                 #66615B !default;
$default-states-color:       #403D39 !default;

$primary-color:              #7A9E9F !default;
$primary-bg:                 #7A9E9F !default;
$primary-states-color:       #427C89 !default;

$success-color:              #7AC29A !default;
$success-bg:                 #7AC29A !default;
$success-states-color:       #42A084 !default;

$info-color:                 #68B3C8 !default;
$info-bg:                    #68B3C8 !default;
$info-states-color:          #3091B2 !default;

$warning-color:              #F3BB45 !default;
$warning-bg:                 #F3BB45 !default;
$warning-states-color:       #BB992F !default;


$danger-color:               #EB5E28 !default;
$danger-bg:                  #EB5E28 !default;
$danger-states-color:        #B33C12 !default;


$link-disabled-color:        #666666 !default;


/*      light colors - used for select dropdown         */

$light-blue:                 rgba($primary-color, .2);
$light-azure:                rgba($info-color, .2);
$light-green:                rgba($success-color, .2);
$light-orange:               rgba($warning-color, .2);
$light-red:                  rgba($danger-color, .2);


//== Components
//
$padding-base-vertical:         7px !default;
$padding-base-horizontal:       18px !default;

$padding-round-vertical:        9px !default;
$padding-round-horizontal:     18px !default;

$padding-simple-vertical:      10px !default;
$padding-simple-horizontal:    18px !default;

$padding-large-vertical:       11px !default;
$padding-large-horizontal:     30px !default;

$padding-small-vertical:        4px !default;
$padding-small-horizontal:     10px !default;

$padding-xs-vertical:           2px !default;
$padding-xs-horizontal:         5px !default;

$padding-label-vertical:        2px !default;
$padding-label-horizontal:     12px !default;

// padding for links inside dropdown menu
$padding-dropdown-vertical:     10px !default;
$padding-dropdown-horizontal:   15px !default;

$margin-large-vertical:        30px !default;
$margin-base-vertical:         15px !default;

// border radius for buttons
$border-radius-btn-small:      26px !default;
$border-radius-btn-base:       20px !default;
$border-radius-btn-large:      50px !default;


// Cristina: am schimbat aici si s-au modificat inputurile
$margin-bottom:                0 0 10px 0 !default;
$border-radius-small:           3px !default;
$border-radius-base:            4px !default;
$border-radius-large:           6px !default;
$border-radius-extreme:        6px !default;

$border-radius-large-top:      $border-radius-large $border-radius-large 0 0 !default;
$border-radius-large-bottom:   0 0 $border-radius-large $border-radius-large !default;

$btn-round-radius:             30px !default;

$height-base:                  40px !default;

$font-size-base:               14px !default;
$font-size-xs:                 12px !default;
$font-size-small:              12px !default;
$font-size-medium:             16px !default;
$font-size-large:              18px !default;
$font-size-large-navbar:       20px !default;

$font-size-h1:                 3.2em   !default;
$font-size-h2:                 2.6em     !default;
$font-size-h3:                 1.825em !default;
$font-size-h4:                 1.5em   !default;
$font-size-h5:                 1.25em  !default;
$font-size-h6:                 0.9em   !default;
$font-paragraph:               16px    !default;
$font-size-navbar:             16px    !default;
$font-size-small:              12px    !default;

$font-weight-light:          300 !default;
$font-weight-normal:         400 !default;
$font-weight-semi:           500 !default;
$font-weight-bold:           600 !default;

$line-height-small:            20px !default;
$line-height-general:          1.4em !default;
$line-height:                 36px !default;
$line-height-lg:              54px !default;


$border-radius-top:        10px 10px 0 0 !default;
$border-radius-bottom:     0 0 10px 10px !default;

$dropdown-shadow:          0 2px rgba(17, 16, 15, 0.1), 0 2px 10px rgba(17, 16, 15, 0.1);

$general-transition-time:  300ms !default;

$slow-transition-time:           300ms !default;
$dropdown-coordinates:      29px -50px !default;

$fast-transition-time:           150ms !default;
$select-coordinates:         50% -40px !default;

$transition-linear:                                   linear !default;
$transition-bezier:         cubic-bezier(0.34, 1.61, 0.7, 1) !default;
$transition-ease:           ease 0s;

$navbar-padding-a:               10px 15px;
$navbar-margin-a:                15px  0px;

$padding-social-a:               10px  5px;

$navbar-margin-a-btn:            15px 3px;
$navbar-margin-a-btn-round:      16px 3px;


$navbar-padding-brand:           20px 15px;
$navbar-margin-brand:             5px  0px;

$navbar-margin-brand-icons:      12px auto;

$navbar-margin-btn:              15px  3px;

$height-icon:					 64px !default;
$width-icon:					 64px !default;
$padding-icon:					 12px !default;
$border-radius-icon:		     15px !default;


$white-navbar:              rgba(#FFFFFF, .96);
$blue-navbar:               rgba(#34ACDC, .98);
$azure-navbar:              rgba(#5BCAFF, .98);
$green-navbar:              rgba(#4CD964, .98);
$orange-navbar:             rgba(#FF9500, .98);
$red-navbar:                rgba(#FF4C40, .98);

$bg-nude:               #f4f3ef !default;
$bg-primary:            #8ECFD5 !default;
$bg-info:               #7CE4FE !default;
$bg-success:            #8EF3C5 !default;
$bg-warning:            #FFE28C !default;
$bg-danger:             #FF8F5E !default;

$topbar-x:             topbar-x !default;
$topbar-back:          topbar-back !default;
$bottombar-x:          bottombar-x !default;
$bottombar-back:       bottombar-back !default;

$transition-linear:                                   linear !default;
$transition-bezier:         cubic-bezier(0.34, 1.61, 0.7, 1) !default;
$transition-ease:           ease 0s;
$transition-ease-in:              ease-in !default;
$transition-ease-out:             ease-out !default;

$general-transition-time:  300ms !default;

$slow-transition-time:           370ms !default;
$dropdown-coordinates:      29px -50px !default;

$fast-transition-time:           150ms !default;

$ultra-fast-transition-time:     100ms  !default;

$select-coordinates:         50% -40px !default;

$padding-zero:                   0px !default;

$sidebar-width:               calc(100% - 260px) !default;
$medium-dark-gray:           #AAAAAA !default;

//variables used in cards
$card-black-color:          #252422 !default;
$card-muted-color:          #ccc5b9 !default;


//variables used for sidebar
$sidebar-background-dark-blue: #506367;

$sidebar-background-blue:      #b8d8d8 !default;
$sidebar-font-blue:            #506568 !default;
$sidebar-subtitle-blue:        #7a9e9f !default;

$sidebar-background-green:      #d5e5a3 !default;
$sidebar-font-green:            #60773d !default;
$sidebar-subtitle-green:        #92ac56 !default;

$sidebar-background-yellow:      #ffe28c !default;
$sidebar-font-yellow:            #b25825 !default;
$sidebar-subtitle-yellow:        #d88715 !default;

$sidebar-background-brown:      #d6c1ab !default;
$sidebar-font-brown:            #75442e !default;
$sidebar-subtitle-brown:        #a47e65 !default;

$sidebar-background-purple:      #baa9ba !default;
$sidebar-font-purple:            #3a283d !default;
$sidebar-subtitle-purple:        #5a283d !default;

$sidebar-background-orange:      #ff8f5e !default;
$sidebar-font-orange:            #772510 !default;
$sidebar-subtitle-orange:        #e95e37 !default;


File: /assets\sass\paper-dashboard.scss
/*!
    
 =========================================================
 * Paper Dashboard - v1.1.2
 =========================================================
 
 * Product Page: http://www.creative-tim.com/product/paper-dashboard
 * Copyright 2017 Creative Tim (http://www.creative-tim.com)
 * Licensed under MIT (https://github.com/creativetimofficial/paper-dashboard/blob/master/LICENSE.md)
 
 =========================================================
 
 * The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
 
 */


@import "paper/variables";
@import "paper/mixins";

@import "paper/typography";

// Core CSS
@import "paper/misc";
@import "paper/sidebar-and-main-panel";
@import "paper/buttons";
@import "paper/inputs";

@import "paper/alerts";
@import "paper/tables";

@import "paper/checkbox-radio";
@import "paper/navbars";
@import "paper/footers";

// Fancy Stuff

@import "paper/dropdown";
@import "paper/cards";
@import "paper/chartist";
@import "paper/responsive";






File: /config.php
<?php 
$ipRouteros = "111.111.111.111"; // host or ip of mikrotik
$Username="api"; // user with readonly perrmison 
$Pass="1234"; //password
$api_puerto=8728;
?>


File: /data.php
<?php
 require_once('api_mt_include2.php');
include 'config.php'; 
$interface = $_GET["interface"]; //"<pppoe-nombreusuario>";

	$API = new routeros_api();
	$API->debug = false;
	if ($API->connect($ipRouteros , $Username , $Pass, $api_puerto)) {
		$rows = array(); $rows2 = array();	
		   $API->write("/interface/monitor-traffic",false);
		   $API->write("=interface=".$interface,false);  
		   $API->write("=once=",true);
		   $READ = $API->read(false);
		   $ARRAY = $API->parse_response($READ);
			if(count($ARRAY)>0){  
				$rx = number_format($ARRAY[0]["rx-bits-per-second"]/1024,1);
				$tx = number_format($ARRAY[0]["tx-bits-per-second"]/1024,1);
				$rows['name'] = 'Tx';
				$rows['data'][] = $tx;
				$rows2['name'] = 'Rx';
				$rows2['data'][] = $rx;
			}else{  
				echo $ARRAY['!trap'][0]['message'];	 
			} 
	}else{
		echo "<font color='#ff0000'></font>";
	}
	$API->disconnect();

	$result = array();
	array_push($result,$rows);
	array_push($result,$rows2);
	print json_encode($result, JSON_NUMERIC_CHECK);

?>


File: /index.html
<!doctype html>
<html lang="en">
<head>
	<meta charset="utf-8" />
	<link rel="apple-touch-icon" sizes="76x76" href="logo-fiberisp.png">
	<link rel="icon" type="image/png" sizes="96x96" href="logo-fiberisp.png">
	<meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1" />

	<title>Anas Programmer</title>

	<meta content='width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=0' name='viewport' />
    <meta name="viewport" content="width=device-width" />


    <!-- Bootstrap core CSS     -->
    <link href="assets/css/bootstrap.min.css" rel="stylesheet" />

    <!-- Animation library for notifications   -->
    <link href="assets/css/animate.min.css" rel="stylesheet"/>

    <!--  Paper Dashboard core CSS    -->
    <link href="assets/css/paper-dashboard.css" rel="stylesheet"/>



    <!--  Fonts and icons     -->
    <link href="http://maxcdn.bootstrapcdn.com/font-awesome/latest/css/font-awesome.min.css" rel="stylesheet">
    <link href='https://fonts.googleapis.com/css?family=Muli:400,300' rel='stylesheet' type='text/css'>
    <link href="assets/css/themify-icons.css" rel="stylesheet">
	     
		  <script src="http://code.jquery.com/jquery-1.9.1.js"></script>
		 
		 
<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0-beta.2/css/bootstrap.min.css" integrity="sha384-PsH8R72JQ3SOdhVi3uxftmaW6Vc51MKb0q5P2rRUpPvrszuE4W1povHYgTpBfshb" crossorigin="anonymous">


<style>
#loogo {
    width: 91%;
}
</style>

<script> 

	function get_interface() {
	
	$.ajax({
    url: "interfaces2.php",
    type: 'POST',
    data: "x=1",
    dataType:"json",
    success: function(data) {
        
		     $.each(data, function(key, val) {
 //alert(val.name);          
   $('#interface_list')
         .append($("<option></option>")
                    .attr("value",val.name)
                    .text(val.name));  

								});
		
   }
	})
}	
	// 
	function requestDatta(tag,interfacee) {


		$.ajax({
			url: 'data.php?interface='+interfacee,
			datatype: "json",
			success: function(data) {
				var midata = JSON.parse(data);
				if( midata.length > 0 ) {
					var TX=parseInt(midata[0].data);
					var RX=parseInt(midata[1].data);
					
					var x = (new Date()).getTime(); 
			
					document.getElementById(tag).innerHTML= " <font color='red'>UP "+ TX + " Mb </font>" +" / <font color='blue'> DW " + RX +" Mb  </font>";
				}else{
					document.getElementById(tag).innerHTML="- / -";
				}
			},
			error: function(XMLHttpRequest, textStatus, errorThrown) { 
				console.error("Status: " + textStatus + " request: " + XMLHttpRequest); console.error("Error: " + errorThrown); 
			}       
		});
	}	

	$(document).ready(function() {
	var id_moniter=1;
	var tag_moniter=1;
	

		$("#addmoniter").click(function()
		{
		
		$.notify({
	// options
	message: 'add '+$('#interface_list  option:selected').text()+' is a successful' 
},{
	// settings
	type: 'success'
});
		
		window[ 'moniter'+ id_moniter ] = 'trafico' + tag_moniter; 
		
		
  var interface_select = $('#interface_list  option:selected').text();
		$("#addmore").append(' <div class="col-lg-3 col-sm-6"><div class="card"><div class="content"><div class="row"><center><div class="col-xs-12"><div class="icon-big icon-danger text-center"><i class="ti-pulse"></i></div><h2><B>'+interface_select+'</B></h2></div><div class="col-xs-12 "><div class="numbers"> <div id="'+window[ 'moniter'+ id_moniter ]+'"></div></div> </div></center> </div><div class="footer"><hr /><div class="stats"><i class="ti-timer"></i> Realtime</div><B style="float:right;"></B></div> </div> </div></div>');
		//$("#addmore").append('<H1>TEST</H1> ');	


var moniterssid= window[ 'moniter'+ id_moniter ];
		setInterval(function () {
							requestDatta(moniterssid,interface_select);
							
						}, 500);
						id_moniter++;
						tag_moniter++;
					
		});
	
					get_interface(); // get all interface and append to list
  });
  
 
</script>

</head>
<body>



<div class="wrapper">
   
    <div class="main-panel">
  

        <div class="content">
            <div class="container-fluid">

	
      

   <center> <img src="logo-fiberisp.png" class="img-rounded" id="loogo" alt="Cinque Terre"></center>
   
<div class="row">
  <div class="col-lg-12 col-sm-12">				 
				
    <div class="form-group"  style="font-size:2em;">
      <label for="sel1">Select Interface</label>
      <select class="form-control" id="interface_list"  >
      
      </select>
      <br>
	  <center>
     <button id="addmoniter" class="btn btn-primary" style="font-size:0.9em;">Add</button>
	 </center>
    </div>

  </div>
</div>
                <div class="row" id="addmore" >
      
                </div>
               
			   
          
            </div>
        </div>

	 
   
      
        <footer class="footer">
            <div class="container-fluid">
                <nav class="pull-left">
                    <ul>

                    
                    </ul>
                </nav>
                <div class="copyright pull-right">
                    &copy; <script>document.write(new Date().getFullYear())</script>, made with <i class="fa fa-heart heart"></i> by Anas Programmer</a>
                </div>
            </div>
        </footer>

    </div>
</div>


</body>

    <!--   Core JS Files   -->

	<script src="assets/js/bootstrap.min.js" type="text/javascript"></script>

	<!--  Checkbox, Radio & Switch Plugins -->
	<script src="assets/js/bootstrap-checkbox-radio.js"></script>

	<!--  Charts Plugin -->
	<script src="assets/js/chartist.min.js"></script>

    <!--  Notifications Plugin    -->
    <script src="assets/js/bootstrap-notify.js"></script>




</html>


File: /interfaces2.php
<?php
header("Content-type: text/javascript");
require_once('api_mt_include2.php'); 
include 'config.php'; 

	$API = new routeros_api();
	$API->debug = false;
	if ($API->connect($ipRouteros , $Username , $Pass, $api_puerto)) {
$rows = array(); $rows2 = array();	
		  $API->write('/interface/getall');
		  
		   $READ = $API->read(false);
		   $ARRAY = $API->parse_response($READ);
		
   $API->disconnect();
  

  print json_encode($ARRAY);

	}
	


?>

File: /LICENSE
MIT License

Copyright (c) 2017 Anas Programmer

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


File: /README.md
# mikrotik-traffic-monitor
edit file config only 


#anas_programmer


