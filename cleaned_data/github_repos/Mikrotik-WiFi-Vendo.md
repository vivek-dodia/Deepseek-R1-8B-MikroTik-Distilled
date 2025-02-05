# Repository Information
Name: Mikrotik-WiFi-Vendo

# Directory Structure
Directory structure:
└── github_repos/Mikrotik-WiFi-Vendo/
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
    │   │       ├── pack-5b03aaec8e3dd008bda3859869e49b31ee0c90c5.idx
    │   │       └── pack-5b03aaec8e3dd008bda3859869e49b31ee0c90c5.pack
    │   ├── packed-refs
    │   └── refs/
    │       ├── heads/
    │       │   └── master
    │       ├── remotes/
    │       │   └── origin/
    │       │       └── HEAD
    │       └── tags/
    ├── .github/
    │   └── FUNDING.yml
    ├── .gitignore
    ├── alogin.html
    ├── assets/
    │   ├── css/
    │   │   └── style.css
    │   ├── img/
    │   └── js/
    │       ├── md5.js
    │       └── script.js
    ├── CHANGELOG.MD
    ├── config/
    │   ├── Default Credentials.xlsx
    │   ├── interent-v1.0.0.backup
    │   └── Signage.docx
    ├── CONTRIBUTING
    ├── error.html
    ├── errors-en.txt
    ├── errors.txt
    ├── LICENSE
    ├── login.html
    ├── logout.html
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
	url = https://github.com/KalikotPH/Mikrotik-WiFi-Vendo.git
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
0000000000000000000000000000000000000000 111a64667fc5559b243e30556921416f0a881c90 vivek-dodia <vivek.dodia@icloud.com> 1738606308 -0500	clone: from https://github.com/KalikotPH/Mikrotik-WiFi-Vendo.git


File: /.git\logs\refs\heads\master
0000000000000000000000000000000000000000 111a64667fc5559b243e30556921416f0a881c90 vivek-dodia <vivek.dodia@icloud.com> 1738606308 -0500	clone: from https://github.com/KalikotPH/Mikrotik-WiFi-Vendo.git


File: /.git\logs\refs\remotes\origin\HEAD
0000000000000000000000000000000000000000 111a64667fc5559b243e30556921416f0a881c90 vivek-dodia <vivek.dodia@icloud.com> 1738606308 -0500	clone: from https://github.com/KalikotPH/Mikrotik-WiFi-Vendo.git


File: /.git\packed-refs
# pack-refs with: peeled fully-peeled sorted 
111a64667fc5559b243e30556921416f0a881c90 refs/remotes/origin/master


File: /.git\refs\heads\master
111a64667fc5559b243e30556921416f0a881c90


File: /.git\refs\remotes\origin\HEAD
ref: refs/remotes/origin/master


File: /.github\FUNDING.yml
# These are supported funding model platforms

github: # Replace with up to 4 GitHub Sponsors-enabled usernames e.g., [user1, user2]
patreon: bytescrafter
open_collective: # Replace with a single Open Collective username
ko_fi: # Replace with a single Ko-fi username
tidelift: # Replace with a single Tidelift platform-name/package-name e.g., npm/babel
community_bridge: # Replace with a single Community Bridge project-name e.g., cloud-foundry
liberapay: # Replace with a single Liberapay username
issuehunt: # Replace with a single IssueHunt username
otechie: # Replace with a single Otechie username
custom: # Replace with up to 4 custom sponsorship URLs e.g., ['link1', 'link2']


File: /.gitignore
# ignore everything in the root except the "wp-content" directory.
!wp-content/

# ignore everything in the "wp-content" directory, except:
# "mu-plugins", "plugins", "themes" directory
wp-content/*
!wp-content/mu-plugins/
!wp-content/plugins/
!wp-content/themes/

# ignore these plugins
wp-content/plugins/hello.php

# ignore specific themes
wp-content/themes/twenty*/

# ignore node dependency directories
File: /alogin.html
<html>
	<head>
		<title id="title">WiFi4Rent by Bytes Crafter</title>
		<meta http-equiv="refresh" content="2; url=$(link-redirect)">
		<meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1">
		<meta name="viewport" content="width=device-width; initial-scale=1.0; maximum-scale=1.0;"/>
		<meta http-equiv="pragma" content="no-cache">
		<meta http-equiv="expires" content="-1">
		<link rel="stylesheet" href="assets/css/style.css">
		<script language="JavaScript">
			function startClock() {
				$(if popup == 'true')
				open('$(link-status)', 'hotspot_status', 'toolbar=0,location=0,directories=0,status=0,menubars=0,resizable=1,width=290,height=200');
			$(endif)
			location.href = './status';
			}
		</script>
	</head>
	<body onLoad="startClock()">
		<table width="100%" height="100%">
			<tr>
				<td align="center" valign="middle">
				Want to use your internet time?
				<br><br>
				Gustong gumamit ng internet ngayun? 
				<br><br>
				<a class="text-primary" href="./login">Login your account</a></td>
			</tr>
		</table>
	</body>
</html>


File: /assets\css\style.css

body {
  font-family: -apple-system, BlinkMacSystemFont, "segoe ui", Roboto, "helvetica neue", Arial, sans-serif, "apple color emoji", "segoe ui emoji", "segoe ui symbol";
  font-size: 14px;
  font-weight: 400;
  line-height: 1.5;
  text-align: left;
  margin: 0px;
}

input {
  vertical-align: middle;
  margin: auto;
  box-sizing: border-box;
     -webkit-box-sizing:border-box;
     -moz-box-sizing: border-box;
}

.plch-center::-webkit-input-placeholder {
   text-align: center;
}
.plch-center:-moz-placeholder {
   text-align: center;
}

/* button */
button{
  text-decoration: none;
  display: inline-block;
  border:none;
  background-color: none;
  font-size: 14px;
  line-height: 1.5;
}

/* container */
.container{
  width: 100%;
}
/* box */
.box{
  padding: 5px;
  margin: 5px;
  border-radius: 3px;
}
.box a{
  text-decoration: none;
}
.box h1, h3, h3, p{
  padding: 0px;
  margin: 0px;
}
.box-bordered{
  border: 1px solid #23282c;
}
/* box minh-50px*/
.bmh-50{
  min-height: 50px;
}
.bmh-55{
  min-height: 55px;
}
.bmh-60{
  min-height: 60px;
}
.bmh-65{
  min-height: 65px;
}
.bmh-70{
  min-height: 70px;
}
.bmh-75{
  min-height: 75px;
}
.bmh-80{
  min-height: 80px;
}
.bmh-85{
  min-height: 85px;
}
.bmh-90{
  min-height: 90px;
}
.bmh-95{
  min-height: 95px;
}
.bmh-100{
  min-height: 100px;
}

.box-group > div{
  display: table-cell;
  vertical-align: middle;
}
.box-group-icon{
  font-size: 40px;
  display: inline-block;
  text-align: center;
  text-decoration: none;
  white-space: nowrap;
  vertical-align: middle;
  width: 25%;
  user-select: none;
  border: 1px solid transparent;
  padding: 5px 10px 5px 10px;
  margin: 5px;
  line-height: 1.5;
  border-radius: 3px;
}
.box-group-area{
  padding: 5px;
}
.login-box,
.register-box {
  width: 400px;
  margin: 10px auto;
  padding-top:10%;
}

.col-c{
  float:none; 
  margin: auto;
}


.box-shadow{
  box-shadow: 0 10px 15px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19);
}
/* card */
.card{
  margin: 5px;
  border-radius: 3px;
  background-color: #fff;
}
.card a{

  text-decoration: none;
}
.card h3{
  margin: 0px;
}
.card-header{
  padding: 5px 10px 5px 10px;
  margin-bottom: 5px;
  border-bottom: 1px solid #ccc;
  background-color: #fff;
  border-radius: 2px 2px 0px 0px;
}
.card-body{
  padding: 5px 10px 5px 10px;
  margin-bottom: 10px;
}
.card-footer{
  padding: 5px 10px 5px 10px;
  margin-top: 5px;
  min-height: 20px;
  border-radius: 0px 0px 2px 2px;
}
.overflow{
  overflow-x:auto; 
  overflow-y:auto; 
  max-height: 80vh;
}


.btn{
  display: inline-block;
  text-align: center;
  text-decoration: none;
  white-space: nowrap;
  vertical-align: middle;
  user-select: none;
  border: 1px solid transparent;
  border-radius: 3px;
  font-size: 14px;
  cursor: pointer;
}
.btn:hover{
  box-shadow: inset 0 0 0 transparent, 0 0 0 0.2rem rgba(166, 166, 166, 0.15);
}
.btn-md{
  display: inline-block;
  text-align: center;
  text-decoration: none;
  white-space: nowrap;
  vertical-align: middle;
  user-select: none;
  border: 1px solid transparent;
  border-radius: 3px;
  font-size: 18px;
  cursor: pointer;
}
.btn-md:hover{
  box-shadow: inset 0 0 0 transparent, 0 0 0 0.2rem rgba(166, 166, 166, 0.15);
}

/* backgound */
[class*="bg-"] {
  text-decoration: none;
}
.bg-primary{
  background-color: #20a8d8;
  color: #f3f4f5;
}
.bg-secondary{
  background-color: #73818f;
  color: #f3f4f5;
}
.bg-success{
  background-color: #4dbd74;
  color: #f3f4f5;
}
.bg-info{
  background-color: #63c2de;
  color: #f3f4f5;
}
.bg-warning{
  background-color: #ffc107;
  color: #f3f4f5;
}    
.bg-danger{
  background-color: #f86c6b;
  color: #f3f4f5;
}
.bg-light{
  background-color: #f3f4f5;
  color: #2f353a;
}
.bg-dark{
  background-color: #2f353a;
  color: #f3f4f5;
}
.bg-blue{
  background-color: #20a8d8;
  color: #f3f4f5;
}
.bg-indigo{
  background-color: #6610f2;
  color: #f3f4f5;
}
.bg-purple{
  background-color: #9f6efc;
  color: #f3f4f5;
}
.bg-pink{
  background-color: #ff6fb2;
  color: #f3f4f5;
}
.bg-red{
  background-color: #f86c6b;
  color: #f3f4f5;
}
.bg-orange{
  background-color: #e6c01b;
  color: #f3f4f5;
}
.bg-yellow{
  background-color: #f78223;
  color: #f3f4f5;
}
.bg-green{
  background-color: #4dbd74;
  color: #f3f4f5;
}
.bg-teal{
  background-color: #20c997;
  color: #f3f4f5;
}
.bg-cyan{
  background-color: #17a2b8;
  color: #f3f4f5;
}
.bg-white{
  background-color: #fff;
  color: #2f353a;
}
.bg-grey{
  background-color: #5a5a5a;
  color: #f3f4f5;
}
.bg-grey-dark{
  background-color: #3a3a3a;
  color: #f3f4f5;
}
.bg-light-blue{
  background-color: #63c2de;
  color: #f3f4f5;
}



/* text */
[class*="text-"] {
  text-decoration: none;
}
.text-primary{
  color: #20a8d8;
}
.text-secondary{
  color: #73818f;
}
.text-success{
  color: #4dbd74;
}
.text-info{
  color: #63c2de;
}
.text-warning{
  color: #ffc107;
}    
.text-danger{
  color: #f86c6b;
}
.text-light{
  color: #f3f4f5;
}
.text-dark{
  color: #2f353a;
}
.text-blue{
  color: #20a8d8;
}
.text-indigo{
  color: #6610f2;
}
.text-purple{
  color: #6f42c1;
}
.text-pink{
  color: #e83e8c;
}
.text-red{
  color: #f86c6b;
}
.text-orange{
  color: #f8cb00;
}
.text-yellow{
  color: #ffc107;
}
.text-green{
  color: #4dbd74;
}
.text-teal{
  color: #20c997;
}
.text-cyan{
  color: #17a2b8;
}
.text-white{
  color: #fff;
}
.text-grey{
  color: #73818f;
}
.text-grey-dark{
  color: #2f353a;
}
.text-light-blue{
  color: #63c2de;
}
.text-bold{
  font-weight: bold;
}

/* align */
.align-middle{
  vertical-align: middle;
}
.text-center{
  text-align: center;
}
.text-right{
  text-align: right;
}
.text-left{
  text-align: left;
}
.text-nowrap{
  white-space: nowrap;
}
 
/* row */
.row::after {
  content: "";
  clear: both;
  display: table;
}

.w-1 {width: 8.33%;}
.w-2 {width: 16.66%;}
.w-3 {width: 25%;}
.w-4 {width: 33.33%;}
.w-5 {width: 41.66%;}
.w-6 {width: 50%;}
.w-7 {width: 58.33%;}
.w-8 {width: 66.66%;}
.w-9 {width: 75%;}
.w-10 {width: 83.33%;}
.w-11 {width: 91.66%;}
.w-12 {width: 100%;}

/* column */
[class*="col-"] {
  float: left;

}
.col-1 {width: 8.33%;}
.col-2 {width: 16.66%;}
.col-3 {width: 25%;}
.col-4 {width: 33.33%;}
.col-5 {width: 41.66%;}
.col-6 {width: 50%;}
.col-7 {width: 58.33%;}
.col-8 {width: 66.66%;}
.col-9 {width: 75%;}
.col-10 {width: 83.33%;}
.col-11 {width: 91.66%;}
.col-12 {width: 100%;}

/*table*/
.table {
  width: 100%;
  border-collapse: collapse !important;
}
.table td,
.table th {
    padding: 5px;
}

.table td, th, a{
  color: #000;
  text-decoration: none;
}
.table-bordered th,
.table-bordered td {
    border: 1px solid #ccc !important;
}
.table-hover:hover tbody tr:hover {
  background-color: #f2f2f2;
}


.radius-l-3 {
  border-radius: 3px 0pc 0pc 3px;
}
.radius-r-3 {
  border-radius: 0px 3px 3px 0px;
}
.radius-b-3 {
  border-radius: 0px 0px 3px 3px;
}
.radius-3 {
  border-radius: 3px;
}
.radius-l-5 {
  border-radius: 5px 0pc 0pc 5px;
}
.radius-r-5 {
  border-radius: 0px 5px 5px 0px;
}
.radius-5 {
  border-radius: 5px;
}


/* alert */
.alert{
width: 100%; padding:5px 0px 5px 0px; border-radius: 3px;
}
/*padding*/
.pd-2{padding: 2px;}
.pd-3{padding: 3px;}
.pd-4{padding: 4px;}
.pd-5 {padding: 5px;}
.pd-6 {padding: 6px;}
.pd-7 {padding: 7px;}
.pd-8 {padding: 8px;}
.pd-9 {padding: 9px;}
.pd-10 {padding: 10px;}

.pd-t-2{padding-top: 2px;}
.pd-t-3{padding-top: 3px;}
.pd-t-4{padding-top: 4px;}
.pd-t-5 {padding-top: 5px;}
.pd-t-6 {padding-top: 6px;}
.pd-t-7 {padding-top: 7px;}
.pd-t-8 {padding-top: 8px;}
.pd-t-9 {padding-top: 9px;}
.pd-t-10 {padding-top: 10px;}

.pd-b-2{padding-bottom: 2px;}
.pd-b-3{padding-bottom: 3px;}
.pd-b-4{padding-bottom: 4px;}
.pd-b-5 {padding-bottom: 5px;}
.pd-b-6 {padding-bottom: 6px;}
.pd-b-7 {padding-bottom: 7px;}
.pd-b-8 {padding-bottom: 8px;}
.pd-b-9 {padding-bottom: 9px;}
.pd-b-10 {padding-bottom: 10px;}

.pd-r-2{padding-right: 2px;}
.pd-r-3{padding-right: 3px;}
.pd-r-4{padding-right: 4px;}
.pd-r-5 {padding-right: 5px;}
.pd-r-6 {padding-right: 6px;}
.pd-r-7 {padding-right: 7px;}
.pd-r-8 {padding-right: 8px;}
.pd-r-9 {padding-right: 9px;}
.pd-r-10 {padding-right: 10px;}

.pd-l-2{padding-left: 2px;}
.pd-l-3{padding-left: 3px;}
.pd-l-4{padding-left: 4px;}
.pd-l-5 {padding-left: 5px;}
.pd-l-6 {padding-left: 6px;}
.pd-l-7 {padding-left: 7px;}
.pd-l-8 {padding-left: 8px;}
.pd-l-9 {padding-left: 9px;}
.pd-l-10 {padding-left: 10px;}

/*margin*/
.mr-a {margin: auto;}

.mr-2{margin: 2px;}
.mr-3{margin: 3px;}
.mr-4{margin: 4px;}
.mr-5 {margin: 5px;}
.mr-6 {margin: 6px;}
.mr-7 {margin: 7px;}
.mr-8 {margin: 8px;}
.mr-9 {margin: 9px;}
.mr-10 {margin: 10px;}

.mr-t-2{margin-top: 2px;}
.mr-t-3{margin-top: 3px;}
.mr-t-4{margin-top: 4px;}
.mr-t-5 {margin-top: 5px;}
.mr-t-6 {margin-top: 6px;}
.mr-t-7 {margin-top: 7px;}
.mr-t-8 {margin-top: 8px;}
.mr-t-9 {margin-top: 9px;}
.mr-t-10 {margin-top: 10px;}

.mr-b-2{margin-bottom: 2px;}
.mr-b-3{margin-bottom: 3px;}
.mr-b-4{margin-bottom: 4px;}
.mr-b-5 {margin-bottom: 5px;}
.mr-b-6 {margin-bottom: 6px;}
.mr-b-7 {margin-bottom: 7px;}
.mr-b-8 {margin-bottom: 8px;}
.mr-b-9 {margin-bottom: 9px;}
.mr-b-10 {margin-bottom: 10px;}

.mr-r-2{margin-right: 2px;}
.mr-r-3{margin-right: 3px;}
.mr-r-4{margin-right: 4px;}
.mr-r-5 {margin-right: 5px;}
.mr-r-6 {margin-right: 6px;}
.mr-r-7 {margin-right: 7px;}
.mr-r-8 {margin-right: 8px;}
.mr-r-9 {margin-right: 9px;}
.mr-r-10 {margin-right: 10px;}

.mr-l-2{margin-left: 2px;}
.mr-l-3{margin-left: 3px;}
.mr-l-4{margin-left: 4px;}
.mr-l-5 {margin-left: 5px;}
.mr-l-6 {margin-left: 6px;}
.mr-l-7 {margin-left: 7px;}
.mr-l-8 {margin-left: 8px;}
.mr-l-9 {margin-left: 9px;}
.mr-l-10 {margin-left: 10px;}

/*pointer*/
.pointer{
  cursor: pointer;
}
/*form control*/
.form-control {
  display: block;
  width: 100%;
  padding: 5px;
  border: 1px solid #ccc;
  border-radius: 3px;
  color: #000;
  font-size: 14px;
  background-color: #fff;
  box-sizing: border-box;
     -webkit-box-sizing:border-box;
     -moz-box-sizing: border-box;
  
}

.form-control:focus {
  color: #000;
  border-color: #80bdff;
  outline: 0;
  box-shadow: inset 0 0 0 transparent, 0 0 0 0.2rem rgba(0, 123, 255, 0.25);
}

.form-control::placeholder {
  color: #ccc;
}

.form-control-md {
  display: block;
  width: 100%;
  padding: 10px;
  border: 1px solid #ccc;
  border-radius: 3px;
  color: #000;
  font-size: 14px;
  background-color: #fff;
  box-sizing: border-box;
     -webkit-box-sizing:border-box;
     -moz-box-sizing: border-box;
  
}
.form-control-md:focus {
  color: #000;
  border-color: #80bdff;
  outline: 0;
  box-shadow: inset 0 0 0 transparent, 0 0 0 0.2rem rgba(0, 123, 255, 0.25);
}

.form-control-md::placeholder {
  color: #ccc;
}

  #main{
  margin-top: 5%;
}

/* @media */
@media screen and (max-width: 800px) {
  [class*="col-"] {
        width: 100%;
    }
  body{
    padding: 10px;
  }
  #main{
    margin-top: 0;
  }  

.col-md-1 {width: 8.33%;}
.col-md-2 {width: 16.66%;}
.col-md-3 {width: 25%;}
.col-md-4 {width: 33.33%;}
.col-md-5 {width: 41.66%;}
.col-md-6 {width: 50%;}
.col-md-7 {width: 58.33%;}
.col-md-8 {width: 66.66%;}
.col-md-9 {width: 75%;}
.col-md-10 {width: 83.33%;}
.col-md-11 {width: 91.66%;}
.col-md-12 {width: 100%;}

 
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


File: /assets\js\script.js
    
    document.login.username.focus();
    //document.getElementById('title').innerHTML = window.location.hostname + " > login";
    
    // login page 2 mode by Laksamadi Guko
    var username = document.login.username;
    var password = document.login.password;
    var luser = document.getElementById("luser");
    var lpass = document.getElementById("lpass");
    var btnmem = document.getElementById("btnmem");
    var btnvcr = document.getElementById("btnvcr");
    
    // set password = username
    function setpass()
    {
        var user = username.value		
        password.value = user;
    }
    username.onchange = setpass;
    btnmem.style.backgroundColor = "#494949";
    btnvcr.style.backgroundColor = "#757575";  
    
    // change to voucher mode
    function voucher()
    {
        username.focus();
        username.onchange = setpass;
        username.placeholder = "Voucher";
        password.type = "hidden";
        password.value = username.value;  
        btnmem.style.backgroundColor = "#494949";
        btnvcr.style.backgroundColor = "#757575";  
    }
    
    // change to member mode
    function member()
    {
        username.focus();
        username.onchange = "";
        username.placeholder = "Username";
        password.type= "password";
        password.value = "";
        btnmem.style.backgroundColor = "#757575"; 
        btnvcr.style.backgroundColor = "#494949"; 
    }

File: /CHANGELOG.MD
# Change Log

All notable changes to this project will be documented in this file.
The format is based on Keep a Changelog and this project adheres to Semantic Versioning.

## SEMANTIC VERSION: Example: v1.2.3-alpha/beta
- 1 - Major version and may result to incompatibilities from previous major release.
- 2 - Minor version is when you add functionaly on the project. When you increase this, reset patch version.
- 3 - Patch version, meaning this is used mainly on change and fixing.
- alpha - An alpha release usually means a website or application is working but some functionality is likely to be missing and a number of known and unknown bugs are likely to surface.
- beta -  A pre-release of software that is given out to a large group of users to try under real conditions. Beta versions have gone through alpha testing inhouse and are generally fairly close in look, feel and function to the final product; however, design changes often occur as a result.

## [v1.2.3] - 2017-03-14 > TEMPLATE VERSION ITEM

Here we would have the update steps for 1.2.4 for people to follow.

### Added
- [Link Tag](http://example.com/submenu/target)
    Added something on the project.

### Changed
- [Link Tag](http://example.com/submenu/target)
    Change the speed of bar on foo.

### Fixed
- [Link Tag](http://example.com/submenu/target)
    Fix module foo tests.


File: /CONTRIBUTING
# Contributing

When contributing to this repository, please first discuss the change you wish to make via issue,
email, or any other method with the owners of this repository before making a change. 

Please note we have a code of conduct, please follow it in all your interactions with the project.

## Pull Request Process

1. Ensure any install or build dependencies are removed before the end of the layer when doing a 
   build.
2. Update the README.md with details of changes to the interface, this includes new environment 
   variables, exposed ports, useful file locations and container parameters.
3. Increase the version numbers in any examples files and the README.md to the new version that this
   Pull Request would represent. The versioning scheme we use is [SemVer](http://semver.org/).
4. You may merge the Pull Request in once you have the sign-off of two other developers, or if you 
   do not have permission to do that, you may request the second reviewer to merge it for you.

## Code of Conduct

### Our Pledge

In the interest of fostering an open and welcoming environment, we as
contributors and maintainers pledge to making participation in our project and
our community a harassment-free experience for everyone, regardless of age, body
size, disability, ethnicity, gender identity and expression, level of experience,
nationality, personal appearance, race, religion, or sexual identity and
orientation.

### Our Standards

Examples of behavior that contributes to creating a positive environment
include:

* Using welcoming and inclusive language
* Being respectful of differing viewpoints and experiences
* Gracefully accepting constructive criticism
* Focusing on what is best for the community
* Showing empathy towards other community members

Examples of unacceptable behavior by participants include:

* The use of sexualized language or imagery and unwelcome sexual attention or
advances
* Trolling, insulting/derogatory comments, and personal or political attacks
* Public or private harassment
* Publishing others' private information, such as a physical or electronic
  address, without explicit permission
* Other conduct which could reasonably be considered inappropriate in a
  professional setting

### Our Responsibilities

Project maintainers are responsible for clarifying the standards of acceptable
behavior and are expected to take appropriate and fair corrective action in
response to any instances of unacceptable behavior.

Project maintainers have the right and responsibility to remove, edit, or
reject comments, commits, code, wiki edits, issues, and other contributions
that are not aligned to this Code of Conduct, or to ban temporarily or
permanently any contributor for other behaviors that they deem inappropriate,
threatening, offensive, or harmful.

### Scope

This Code of Conduct applies both within project spaces and in public spaces
when an individual is representing the project or its community. Examples of
representing a project or community include using an official project e-mail
address, posting via an official social media account, or acting as an appointed
representative at an online or offline event. Representation of a project may be
further defined and clarified by project maintainers.

### Enforcement

Instances of abusive, harassing, or otherwise unacceptable behavior may be
reported by contacting the project team at [INSERT EMAIL ADDRESS]. All
complaints will be reviewed and investigated and will result in a response that
is deemed necessary and appropriate to the circumstances. The project team is
obligated to maintain confidentiality with regard to the reporter of an incident.
Further details of specific enforcement policies may be posted separately.

Project maintainers who do not follow or enforce the Code of Conduct in good
faith may face temporary or permanent repercussions as determined by other
members of the project's leadership.

### Attribution

This Code of Conduct is adapted from the [Contributor Covenant][homepage], version 1.4,
available at [http://contributor-covenant.org/version/1/4][version]

[homepage]: http://contributor-covenant.org
[version]: http://contributor-covenant.org/version/1/4/

File: /error.html
<html>
	<head>
		<title id="title">WiFi4Rent by Bytes Crafter</title>
		<meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1">
		<meta http-equiv="pragma" content="no-cache">
		<meta http-equiv="expires" content="-1">
		<style type="text/css">
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

config-error = error configuration ($(error-orig))

# not-logged-in
# Will happen, if status or logout page is requested by user,
# which actually is not logged in

not-logged-in = You're not logged in yet! (ip $(ip))

# ippool-empty
# IP address for user is to be assigned from ip pool, but there are no more
# addresses in that pool

ippool-empty = WiFi is currently busy, kindly wait for some time.

# shutting-down
# When shutdown is executed, new clients are not accepted

shutting-down = WiFi is currently shutting down.

# user-session-limit
# If user profile has limit of shared-users, then this error will be shown
# after reaching this limit

user-session-limit = $(username) is currently active or in use.

# license-session-limit
# Depending on licence number of active hotspot clients is limited to
# one or another amount. If this limit is reached, following error is displayed.

license-session-limit = Your session is now expired. Want to try weekly or monthly subscription? Talk to us now! ($(error-orig))

# wrong-mac-username
# If username looks like MAC address (12:34:56:78:9a:bc), but is not
# a MAC address of this client, login is rejected

wrong-mac-username = Your MAC addresss is not valid.

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

chap-missing = Your web browser did not send challenge response. Try again, also try to enable JavaScript.

# invalid-username
# Most general case of invalid username or password. If RADIUS server
# has sent an error string with Access-Reject message, then it will
# override this setting.

invalid-username = Your voucher or username and password combination is not incorrect.

# invalid-mac
# Local users (on hotspot server) can be bound to some MAC address. If login
# from different MAC is tried, this error message will be shown.

invalid-mac = Your device is different from the previous login. WiFi credential can't be shared through devices.

# uptime-limit, traffic-limit
# For local hotspot users in case if limits are reached

uptime-limit = Your time limit is now reached. Want to try weekly or monthly subscription? Talk to us now!
traffic-limit = Your data limit is now reached. Want to try weekly or monthly subscription? Talk to us now!

# radius-timeout
# User is authenticated by RADIUS server, but no response is received from it,
# following error will be shown.

radius-timeout = WiFi did not respond as it should be. Report this issue.

# auth-in-progress
# Authorization in progress. Client already has issued an authorization request
# which is not yet complete.

auth-in-progress = Login in progress... Please try again later.

# radius-reply
# Radius server returned some custom error message

radius-reply = $(error-orig)


File: /LICENSE
## Source

https://github.com/pascalandy/GNU-GENERAL-PUBLIC-LICENSE/blob/master/LICENSE.md

## TERMS AND CONDITIONS

#### 0\. Definitions.

“This License” refers to version 3 of the GNU General Public License.

“Copyright” also means copyright-like laws that apply to other kinds of works, such as semiconductor masks.

“The Program” refers to any copyrightable work licensed under this License. Each licensee is addressed as “you”. “Licensees” and “recipients” may be individuals or organizations.

To “modify” a work means to copy from or adapt all or part of the work in a fashion requiring copyright permission, other than the making of an exact copy. The resulting work is called a “modified version” of the earlier work or a work “based on” the earlier work.

A “covered work” means either the unmodified Program or a work based on the Program.

To “propagate” a work means to do anything with it that, without permission, would make you directly or secondarily liable for infringement under applicable copyright law, except executing it on a computer or modifying a private copy. Propagation includes copying, distribution (with or without modification), making available to the public, and in some countries other activities as well.

To “convey” a work means any kind of propagation that enables other parties to make or receive copies. Mere interaction with a user through a computer network, with no transfer of a copy, is not conveying.

An interactive user interface displays “Appropriate Legal Notices” to the extent that it includes a convenient and prominently visible feature that (1) displays an appropriate copyright notice, and (2) tells the user that there is no warranty for the work (except to the extent that warranties are provided), that licensees may convey the work under this License, and how to view a copy of this License. If the interface presents a list of user commands or options, such as a menu, a prominent item in the list meets this criterion.

#### 1\. Source Code.

The “source code” for a work means the preferred form of the work for making modifications to it. “Object code” means any non-source form of a work.

A “Standard Interface” means an interface that either is an official standard defined by a recognized standards body, or, in the case of interfaces specified for a particular programming language, one that is widely used among developers working in that language.

The “System Libraries” of an executable work include anything, other than the work as a whole, that (a) is included in the normal form of packaging a Major Component, but which is not part of that Major Component, and (b) serves only to enable use of the work with that Major Component, or to implement a Standard Interface for which an implementation is available to the public in source code form. A “Major Component”, in this context, means a major essential component (kernel, window system, and so on) of the specific operating system (if any) on which the executable work runs, or a compiler used to produce the work, or an object code interpreter used to run it.

The “Corresponding Source” for a work in object code form means all the source code needed to generate, install, and (for an executable work) run the object code and to modify the work, including scripts to control those activities. However, it does not include the work's System Libraries, or general-purpose tools or generally available free programs which are used unmodified in performing those activities but which are not part of the work. For example, Corresponding Source includes interface definition files associated with source files for the work, and the source code for shared libraries and dynamically linked subprograms that the work is specifically designed to require, such as by intimate data communication or control flow between those subprograms and other parts of the work.

The Corresponding Source need not include anything that users can regenerate automatically from other parts of the Corresponding Source.

The Corresponding Source for a work in source code form is that same work.

#### 2\. Basic Permissions.

All rights granted under this License are granted for the term of copyright on the Program, and are irrevocable provided the stated conditions are met. This License explicitly affirms your unlimited permission to run the unmodified Program. The output from running a covered work is covered by this License only if the output, given its content, constitutes a covered work. This License acknowledges your rights of fair use or other equivalent, as provided by copyright law.

You may make, run and propagate covered works that you do not convey, without conditions so long as your license otherwise remains in force. You may convey covered works to others for the sole purpose of having them make modifications exclusively for you, or provide you with facilities for running those works, provided that you comply with the terms of this License in conveying all material for which you do not control copyright. Those thus making or running the covered works for you must do so exclusively on your behalf, under your direction and control, on terms that prohibit them from making any copies of your copyrighted material outside their relationship with you.

Conveying under any other circumstances is permitted solely under the conditions stated below. Sublicensing is not allowed; section 10 makes it unnecessary.

#### 3\. Protecting Users' Legal Rights From Anti-Circumvention Law.

No covered work shall be deemed part of an effective technological measure under any applicable law fulfilling obligations under article 11 of the WIPO copyright treaty adopted on 20 December 1996, or similar laws prohibiting or restricting circumvention of such measures.

When you convey a covered work, you waive any legal power to forbid circumvention of technological measures to the extent such circumvention is effected by exercising rights under this License with respect to the covered work, and you disclaim any intention to limit operation or modification of the work as a means of enforcing, against the work's users, your or third parties' legal rights to forbid circumvention of technological measures.

#### 4\. Conveying Verbatim Copies.

You may convey verbatim copies of the Program's source code as you receive it, in any medium, provided that you conspicuously and appropriately publish on each copy an appropriate copyright notice; keep intact all notices stating that this License and any non-permissive terms added in accord with section 7 apply to the code; keep intact all notices of the absence of any warranty; and give all recipients a copy of this License along with the Program.

You may charge any price or no price for each copy that you convey, and you may offer support or warranty protection for a fee.

#### 5\. Conveying Modified Source Versions.

You may convey a work based on the Program, or the modifications to produce it from the Program, in the form of source code under the terms of section 4, provided that you also meet all of these conditions:

*   a) The work must carry prominent notices stating that you modified it, and giving a relevant date.
*   b) The work must carry prominent notices stating that it is released under this License and any conditions added under section 7. This requirement modifies the requirement in section 4 to “keep intact all notices”.
*   c) You must license the entire work, as a whole, under this License to anyone who comes into possession of a copy. This License will therefore apply, along with any applicable section 7 additional terms, to the whole of the work, and all its parts, regardless of how they are packaged. This License gives no permission to license the work in any other way, but it does not invalidate such permission if you have separately received it.
*   d) If the work has interactive user interfaces, each must display Appropriate Legal Notices; however, if the Program has interactive interfaces that do not display Appropriate Legal Notices, your work need not make them do so.

A compilation of a covered work with other separate and independent works, which are not by their nature extensions of the covered work, and which are not combined with it such as to form a larger program, in or on a volume of a storage or distribution medium, is called an “aggregate” if the compilation and its resulting copyright are not used to limit the access or legal rights of the compilation's users beyond what the individual works permit. Inclusion of a covered work in an aggregate does not cause this License to apply to the other parts of the aggregate.

#### 6\. Conveying Non-Source Forms.

You may convey a covered work in object code form under the terms of sections 4 and 5, provided that you also convey the machine-readable Corresponding Source under the terms of this License, in one of these ways:

*   a) Convey the object code in, or embodied in, a physical product (including a physical distribution medium), accompanied by the Corresponding Source fixed on a durable physical medium customarily used for software interchange.
*   b) Convey the object code in, or embodied in, a physical product (including a physical distribution medium), accompanied by a written offer, valid for at least three years and valid for as long as you offer spare parts or customer support for that product model, to give anyone who possesses the object code either (1) a copy of the Corresponding Source for all the software in the product that is covered by this License, on a durable physical medium customarily used for software interchange, for a price no more than your reasonable cost of physically performing this conveying of source, or (2) access to copy the Corresponding Source from a network server at no charge.
*   c) Convey individual copies of the object code with a copy of the written offer to provide the Corresponding Source. This alternative is allowed only occasionally and noncommercially, and only if you received the object code with such an offer, in accord with subsection 6b.
*   d) Convey the object code by offering access from a designated place (gratis or for a charge), and offer equivalent access to the Corresponding Source in the same way through the same place at no further charge. You need not require recipients to copy the Corresponding Source along with the object code. If the place to copy the object code is a network server, the Corresponding Source may be on a different server (operated by you or a third party) that supports equivalent copying facilities, provided you maintain clear directions next to the object code saying where to find the Corresponding Source. Regardless of what server hosts the Corresponding Source, you remain obligated to ensure that it is available for as long as needed to satisfy these requirements.
*   e) Convey the object code using peer-to-peer transmission, provided you inform other peers where the object code and Corresponding Source of the work are being offered to the general public at no charge under subsection 6d.

A separable portion of the object code, whose source code is excluded from the Corresponding Source as a System Library, need not be included in conveying the object code work.

A “User Product” is either (1) a “consumer product”, which means any tangible personal property which is normally used for personal, family, or household purposes, or (2) anything designed or sold for incorporation into a dwelling. In determining whether a product is a consumer product, doubtful cases shall be resolved in favor of coverage. For a particular product received by a particular user, “normally used” refers to a typical or common use of that class of product, regardless of the status of the particular user or of the way in which the particular user actually uses, or expects or is expected to use, the product. A product is a consumer product regardless of whether the product has substantial commercial, industrial or non-consumer uses, unless such uses represent the only significant mode of use of the product.

“Installation Information” for a User Product means any methods, procedures, authorization keys, or other information required to install and execute modified versions of a covered work in that User Product from a modified version of its Corresponding Source. The information must suffice to ensure that the continued functioning of the modified object code is in no case prevented or interfered with solely because modification has been made.

If you convey an object code work under this section in, or with, or specifically for use in, a User Product, and the conveying occurs as part of a transaction in which the right of possession and use of the User Product is transferred to the recipient in perpetuity or for a fixed term (regardless of how the transaction is characterized), the Corresponding Source conveyed under this section must be accompanied by the Installation Information. But this requirement does not apply if neither you nor any third party retains the ability to install modified object code on the User Product (for example, the work has been installed in ROM).

The requirement to provide Installation Information does not include a requirement to continue to provide support service, warranty, or updates for a work that has been modified or installed by the recipient, or for the User Product in which it has been modified or installed. Access to a network may be denied when the modification itself materially and adversely affects the operation of the network or violates the rules and protocols for communication across the network.

Corresponding Source conveyed, and Installation Information provided, in accord with this section must be in a format that is publicly documented (and with an implementation available to the public in source code form), and must require no special password or key for unpacking, reading or copying.

#### 7\. Additional Terms.

“Additional permissions” are terms that supplement the terms of this License by making exceptions from one or more of its conditions. Additional permissions that are applicable to the entire Program shall be treated as though they were included in this License, to the extent that they are valid under applicable law. If additional permissions apply only to part of the Program, that part may be used separately under those permissions, but the entire Program remains governed by this License without regard to the additional permissions.

When you convey a copy of a covered work, you may at your option remove any additional permissions from that copy, or from any part of it. (Additional permissions may be written to require their own removal in certain cases when you modify the work.) You may place additional permissions on material, added by you to a covered work, for which you have or can give appropriate copyright permission.

Notwithstanding any other provision of this License, for material you add to a covered work, you may (if authorized by the copyright holders of that material) supplement the terms of this License with terms:

*   a) Disclaiming warranty or limiting liability differently from the terms of sections 15 and 16 of this License; or
*   b) Requiring preservation of specified reasonable legal notices or author attributions in that material or in the Appropriate Legal Notices displayed by works containing it; or
*   c) Prohibiting misrepresentation of the origin of that material, or requiring that modified versions of such material be marked in reasonable ways as different from the original version; or
*   d) Limiting the use for publicity purposes of names of licensors or authors of the material; or
*   e) Declining to grant rights under trademark law for use of some trade names, trademarks, or service marks; or
*   f) Requiring indemnification of licensors and authors of that material by anyone who conveys the material (or modified versions of it) with contractual assumptions of liability to the recipient, for any liability that these contractual assumptions directly impose on those licensors and authors.

All other non-permissive additional terms are considered “further restrictions” within the meaning of section 10. If the Program as you received it, or any part of it, contains a notice stating that it is governed by this License along with a term that is a further restriction, you may remove that term. If a license document contains a further restriction but permits relicensing or conveying under this License, you may add to a covered work material governed by the terms of that license document, provided that the further restriction does not survive such relicensing or conveying.

If you add terms to a covered work in accord with this section, you must place, in the relevant source files, a statement of the additional terms that apply to those files, or a notice indicating where to find the applicable terms.

Additional terms, permissive or non-permissive, may be stated in the form of a separately written license, or stated as exceptions; the above requirements apply either way.

#### 8\. Termination.

You may not propagate or modify a covered work except as expressly provided under this License. Any attempt otherwise to propagate or modify it is void, and will automatically terminate your rights under this License (including any patent licenses granted under the third paragraph of section 11).

However, if you cease all violation of this License, then your license from a particular copyright holder is reinstated (a) provisionally, unless and until the copyright holder explicitly and finally terminates your license, and (b) permanently, if the copyright holder fails to notify you of the violation by some reasonable means prior to 60 days after the cessation.

Moreover, your license from a particular copyright holder is reinstated permanently if the copyright holder notifies you of the violation by some reasonable means, this is the first time you have received notice of violation of this License (for any work) from that copyright holder, and you cure the violation prior to 30 days after your receipt of the notice.

Termination of your rights under this section does not terminate the licenses of parties who have received copies or rights from you under this License. If your rights have been terminated and not permanently reinstated, you do not qualify to receive new licenses for the same material under section 10.

#### 9\. Acceptance Not Required for Having Copies.

You are not required to accept this License in order to receive or run a copy of the Program. Ancillary propagation of a covered work occurring solely as a consequence of using peer-to-peer transmission to receive a copy likewise does not require acceptance. However, nothing other than this License grants you permission to propagate or modify any covered work. These actions infringe copyright if you do not accept this License. Therefore, by modifying or propagating a covered work, you indicate your acceptance of this License to do so.

#### 10\. Automatic Licensing of Downstream Recipients.

Each time you convey a covered work, the recipient automatically receives a license from the original licensors, to run, modify and propagate that work, subject to this License. You are not responsible for enforcing compliance by third parties with this License.

An “entity transaction” is a transaction transferring control of an organization, or substantially all assets of one, or subdividing an organization, or merging organizations. If propagation of a covered work results from an entity transaction, each party to that transaction who receives a copy of the work also receives whatever licenses to the work the party's predecessor in interest had or could give under the previous paragraph, plus a right to possession of the Corresponding Source of the work from the predecessor in interest, if the predecessor has it or can get it with reasonable efforts.

You may not impose any further restrictions on the exercise of the rights granted or affirmed under this License. For example, you may not impose a license fee, royalty, or other charge for exercise of rights granted under this License, and you may not initiate litigation (including a cross-claim or counterclaim in a lawsuit) alleging that any patent claim is infringed by making, using, selling, offering for sale, or importing the Program or any portion of it.

#### 11\. Patents.

A “contributor” is a copyright holder who authorizes use under this License of the Program or a work on which the Program is based. The work thus licensed is called the contributor's “contributor version”.

A contributor's “essential patent claims” are all patent claims owned or controlled by the contributor, whether already acquired or hereafter acquired, that would be infringed by some manner, permitted by this License, of making, using, or selling its contributor version, but do not include claims that would be infringed only as a consequence of further modification of the contributor version. For purposes of this definition, “control” includes the right to grant patent sublicenses in a manner consistent with the requirements of this License.

Each contributor grants you a non-exclusive, worldwide, royalty-free patent license under the contributor's essential patent claims, to make, use, sell, offer for sale, import and otherwise run, modify and propagate the contents of its contributor version.

In the following three paragraphs, a “patent license” is any express agreement or commitment, however denominated, not to enforce a patent (such as an express permission to practice a patent or covenant not to sue for patent infringement). To “grant” such a patent license to a party means to make such an agreement or commitment not to enforce a patent against the party.

If you convey a covered work, knowingly relying on a patent license, and the Corresponding Source of the work is not available for anyone to copy, free of charge and under the terms of this License, through a publicly available network server or other readily accessible means, then you must either (1) cause the Corresponding Source to be so available, or (2) arrange to deprive yourself of the benefit of the patent license for this particular work, or (3) arrange, in a manner consistent with the requirements of this License, to extend the patent license to downstream recipients. “Knowingly relying” means you have actual knowledge that, but for the patent license, your conveying the covered work in a country, or your recipient's use of the covered work in a country, would infringe one or more identifiable patents in that country that you have reason to believe are valid.

If, pursuant to or in connection with a single transaction or arrangement, you convey, or propagate by procuring conveyance of, a covered work, and grant a patent license to some of the parties receiving the covered work authorizing them to use, propagate, modify or convey a specific copy of the covered work, then the patent license you grant is automatically extended to all recipients of the covered work and works based on it.

A patent license is “discriminatory” if it does not include within the scope of its coverage, prohibits the exercise of, or is conditioned on the non-exercise of one or more of the rights that are specifically granted under this License. You may not convey a covered work if you are a party to an arrangement with a third party that is in the business of distributing software, under which you make payment to the third party based on the extent of your activity of conveying the work, and under which the third party grants, to any of the parties who would receive the covered work from you, a discriminatory patent license (a) in connection with copies of the covered work conveyed by you (or copies made from those copies), or (b) primarily for and in connection with specific products or compilations that contain the covered work, unless you entered into that arrangement, or that patent license was granted, prior to 28 March 2007.

Nothing in this License shall be construed as excluding or limiting any implied license or other defenses to infringement that may otherwise be available to you under applicable patent law.

#### 12\. No Surrender of Others' Freedom.

If conditions are imposed on you (whether by court order, agreement or otherwise) that contradict the conditions of this License, they do not excuse you from the conditions of this License. If you cannot convey a covered work so as to satisfy simultaneously your obligations under this License and any other pertinent obligations, then as a consequence you may not convey it at all. For example, if you agree to terms that obligate you to collect a royalty for further conveying from those to whom you convey the Program, the only way you could satisfy both those terms and this License would be to refrain entirely from conveying the Program.

#### 13\. Use with the GNU Affero General Public License.

Notwithstanding any other provision of this License, you have permission to link or combine any covered work with a work licensed under version 3 of the GNU Affero General Public License into a single combined work, and to convey the resulting work. The terms of this License will continue to apply to the part which is the covered work, but the special requirements of the GNU Affero General Public License, section 13, concerning interaction through a network will apply to the combination as such.

#### 14\. Revised Versions of this License.

The Free Software Foundation may publish revised and/or new versions of the GNU General Public License from time to time. Such new versions will be similar in spirit to the present version, but may differ in detail to address new problems or concerns.

Each version is given a distinguishing version number. If the Program specifies that a certain numbered version of the GNU General Public License “or any later version” applies to it, you have the option of following the terms and conditions either of that numbered version or of any later version published by the Free Software Foundation. If the Program does not specify a version number of the GNU General Public License, you may choose any version ever published by the Free Software Foundation.

If the Program specifies that a proxy can decide which future versions of the GNU General Public License can be used, that proxy's public statement of acceptance of a version permanently authorizes you to choose that version for the Program.

Later license versions may give you additional or different permissions. However, no additional obligations are imposed on any author or copyright holder as a result of your choosing to follow a later version.

#### 15\. Disclaimer of Warranty.

THERE IS NO WARRANTY FOR THE PROGRAM, TO THE EXTENT PERMITTED BY APPLICABLE LAW. EXCEPT WHEN OTHERWISE STATED IN WRITING THE COPYRIGHT HOLDERS AND/OR OTHER PARTIES PROVIDE THE PROGRAM “AS IS” WITHOUT WARRANTY OF ANY KIND, EITHER EXPRESSED OR IMPLIED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE. THE ENTIRE RISK AS TO THE QUALITY AND PERFORMANCE OF THE PROGRAM IS WITH YOU. SHOULD THE PROGRAM PROVE DEFECTIVE, YOU ASSUME THE COST OF ALL NECESSARY SERVICING, REPAIR OR CORRECTION.

#### 16\. Limitation of Liability.

IN NO EVENT UNLESS REQUIRED BY APPLICABLE LAW OR AGREED TO IN WRITING WILL ANY COPYRIGHT HOLDER, OR ANY OTHER PARTY WHO MODIFIES AND/OR CONVEYS THE PROGRAM AS PERMITTED ABOVE, BE LIABLE TO YOU FOR DAMAGES, INCLUDING ANY GENERAL, SPECIAL, INCIDENTAL OR CONSEQUENTIAL DAMAGES ARISING OUT OF THE USE OR INABILITY TO USE THE PROGRAM (INCLUDING BUT NOT LIMITED TO LOSS OF DATA OR DATA BEING RENDERED INACCURATE OR LOSSES SUSTAINED BY YOU OR THIRD PARTIES OR A FAILURE OF THE PROGRAM TO OPERATE WITH ANY OTHER PROGRAMS), EVEN IF SUCH HOLDER OR OTHER PARTY HAS BEEN ADVISED OF THE POSSIBILITY OF SUCH DAMAGES.

#### 17\. Interpretation of Sections 15 and 16.

If the disclaimer of warranty and limitation of liability provided above cannot be given local legal effect according to their terms, reviewing courts shall apply local law that most closely approximates an absolute waiver of all civil liability in connection with the Program, unless a warranty or assumption of liability accompanies a copy of the Program in return for a fee.

END OF TERMS AND CONDITIONS


File: /login.html
<!DOCTYPE HTML>
<html>
	<head>
		<title id="title">WiFi4Rent by Bytes Crafter</title>
		<meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
		<meta http-equiv="pragma" content="no-cache" />
		<meta http-equiv="expires" content="-1" />
		<meta name="viewport" content="width=device-width initial-scale=1.0 maximum-scale=1.0"/>
		<link rel="icon" href="assets/img/favicon.png" />
		<link rel="stylesheet" href="assets/css/style.css">
	</head>
	<body class="background">
		<div class="container">
			<div class="row">
				<div class="col-8 mr-a" id="main" style="float:none;">
					<div class="row">
						<div class="col-4">	

							<!-- PRIMARY BANNER WINDOW -->
							<div class="row">
								<div class="col-12">
									<div class="box bmh-80 bg-grey-dark box-shadow text-center"><img src="assets/img/banner.png" alt="kemangi 41" style="border-radius: 5px; width:100%; max-width: 200px; height:auto;"/></div>
								</div>
							</div>

							<!-- AUTHENTICATION WINDOW-->
							<div class="row">
								<div class="col-12">
									<div class="card  box-shadow">

										<div class="card-header bg-grey">
											<h3 >Internet Gateway</h3>
										</div>

										<div class="card-body">
											$(if chap-id)
												<form name="sendin" action="$(link-login-only)" method="post">
													<input type="hidden" name="username" />
													<input type="hidden" name="password" />
													<input type="hidden" name="dst" value="$(link-orig)" />
													<input type="hidden" name="popup" value="true" />
												</form>
												<script type="text/javascript" src="assets/js/md5.js"></script>
												<script type="text/javascript">
													function doLogin() 
													{
														document.sendin.username.value = document.login.username.value;
														document.sendin.password.value = hexMD5('$(chap-id)' + document.login.password.value + '$(chap-challenge)');
														document.sendin.submit();
														return false;
													}
												</script>
											$(endif)
										<div>	

										<form autocomplete="off" name="login" action="$(link-login-only)" method="post"
											$(if chap-id) onSubmit="return doLogin()" $(endif)>
											<input type="hidden" name="dst" value="$(link-orig)" />
											<input type="hidden" name="popup" value="true" />
												<div class="row">
													<div class="col-6 col-md-6"> 
														<div class="box mr-2 pointer text-center text-light" id="btnvcr" onclick="voucher()">Voucher</div>
													</div>
													<div class="col-6 col-md-6">
														<div class="box mr-2 pointer text-center text-light" id="btnmem" onclick="member()">Member</div>
													</div>
												</div>

												<input class="form-control-md mr-t-10 plch-center" name="username" type="text" value="$(username)" placeholder="Voucher" />
												<input class="form-control-md mr-t-10 plch-center" name="password" type="hidden" placeholder="Password" />

												<div class="text-center mr-t-10">
													<button type="submit" class="w-12 btn-md bg-success pd-5">Login</button>
												</div>
										</form>

									</div>
						
					$(if error)<div class="alert bg-danger text-center mr-t-10">$(error)</div>$(endif)
				</div>
				<!--
				<div class="card-footer bg-grey mr-t-10 text-center">
					$(if trial == 'yes')Try free clicks <a class="text-pink text-bold" href="$(link-login-only)?dst=$(link-orig-esc)&amp;username=T-$(mac-esc)">HERE</a>$(endif)
				</div>
				-->
				<div class="card-footer bg-grey pd-l-10 text-center">
					<i>Copyright &copy; InterRent by <a class="text-light" href="https://www.bytes-crafter.com">Bytes Crafter</a></i>
				</div>
			</div>
		</div>

								

							</div>
						</div>

						<div class="col-8">
							<div class="row">
								
								<!-- SECOND COLUMN - 1ST WINDOW -->
								<div class="col-12">
									<div class="card box-shadow">
										<div class="card-header bg-grey"><h3>Best-Selling Offers</h3></div>
										<div class="card-body">
											<div class="row">

												<div class="col-6">
													<div class="box bg-pink bmh-60">
														<div class="box-group">
															<div class="box-group-icon">1Hour</div>
															<div class="box-group-area text-center">
															<span>
																&#8369 5.00<br>
																Walang wala ba?<br>
															</span>
															</div>
														</div>
													</div>
												</div>

												<div class="col-6">
													<div class="box bg-purple bmh-60">
														<div class="box-group">
															<div class="box-group-icon">3Hours</div>
															<div class="box-group-area text-center">
															<span>
																&#8369 10.00<br>
																Parang hotel lang no?<br>
															</span>
															</div>
														</div>
												</div>
												</div>

												<div class="col-6">
													<div class="box bg-orange bmh-60">
														<div class="box-group">
															<div class="box-group-icon">9Hours</div>
															<div class="box-group-area text-center">
															<span>
																&#8369 20.00<br>
																Internet hanggang gising.<br>
															</span>
															</div>
														</div>
													</div>
												</div>

												<div class="col-6">
													<div class="box bg-red bmh-60">
														<div class="box-group">
															<div class="box-group-icon">1Day</div>
															<div class="box-group-area text-center">
															<span>
																&#8369 30.00<br>
																Uy! mukang di papipigil.<br>
															</span>
															</div>
														</div>
													</div>
												</div>

												<div class="col-6">
													<div class="box bg-blue bmh-60">
														<div class="box-group">
															<div class="box-group-icon">1Week</div>
															<div class="box-group-area text-center">
															<span>
																&#8369 150.00<br>
																Naku, nangigil na sya.<br>
															</span>
															</div>
														</div>
													</div>
												</div>

												<div class="col-6">
													<div class="box bg-green bmh-60">
														<div class="box-group">
															<div class="box-group-icon">1Month</div>
															<div class="box-group-area text-center">
															<span>
																&#8369 500.00<br>
																Wala na! finish na.<br>
															</span>
															</div>
														</div>
													</div>
												</div>

											</div>
										</div>
									</div>
								</div>

								<!-- SECOND COLUMN - 1ST WINDOW -->
								<div class="col-12">
									<div class="col-6">
										<div class="card box-shadow">
											<div class="card-header bg-grey"><h3>Getting Started!</h3></div>
											<div class="card-body align-middle">
												<strong>STEP 1:</strong> Pay and ask for voucher or credential.<br> 
												<strong>STEP 2:</strong> Connect to wifi, Wifi4Rent Hotspot.<br>
												<strong>STEP 3:</strong> Enter your voucher or credential.<br>
											</div>
										</div>
									</div>	
									<div class="col-6">
										<div class="card box-shadow">
											<div class="card-header bg-grey"><h3>More About</h3></div>
											<div class="card-body">
												<p><strong>Speed:</strong> 3MBPS, di mo pa natype, nagsearch na.</p>
												<p><strong>Where:</strong> Block 10, Lot 18 Narra Street, hali na!</p>
												<p><strong>Landmark:</strong> 3 Storey Grey Building, tabi ng Water Element.</p>
											</div>
										</div>	
									</div>
								</div>

							</div>
						</div>

					</div>
				</div>
			</div>
		</div>
		
	</body>
	<script type="text/javascript" src="assets/js/script.js"></script>
</html>

File: /logout.html
<html>
	<head>
		<title id="title">WiFi4Rent by Bytes Crafter</title>
		<meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1">
		<meta name="viewport" content="width=device-width; initial-scale=1.0; maximum-scale=1.0;"/>
		<link rel="stylesheet" href="assets/css/style.css">
		<link rel="icon" href="assets/img/favicon.png" />
	</head>

	<body class="background">

		<script language="JavaScript">
			function openLogin() {
			if (window.name != 'hotspot_logout') return true;
			open('$(link-login)', '_blank', '');
			window.close();
			return false;
			}
			function readablizeBytes(bytes) {
				var s = ['bytes', 'kb', 'MB', 'GB', 'TB', 'PB'];
				var e = Math.floor(Math.log(bytes)/Math.log(1024));
				return (bytes/Math.pow(1024, Math.floor(e))).toFixed(2)+" "+s[e];
			}
		</script>

		<div class="container">
			<div class="row mt-10">
				<div class="col-4 mr-a" style="float:none; margin-top: 10%;">
					<div class="row">
						<div class="col-12">
							<div class="box bmh-80 bg-grey-dark box-shadow text-center"><img src="assets/img/banner.png" alt="kemangi 41" style="border-radius: 5px; width:100%; max-width: 200px; height:auto;"/></div>
							<div class="card box-shadow">
								<div class="card-header bg-grey-dark"><h3> Exit Gateway</h3></div>
								<div class="card-body">
									<div class="box w-12 text-center"><h3>Come back later!</h3></div>
									<table class="table table-bordered table-hover mr-b-10" align="center">
										<tr>
										<td align="right">User</td>
										<td>$(username)</td>
										</tr>
										<tr>
										<td align="right">IP Address</td>
										<td>$(ip)</td>
										</tr>
										<tr>
										<td align="right">MAC Address</td>
										<td>$(mac)</td>
									</tr>
									<tr>
										<td align="right">Up | Down</td>
										<td>$(bytes-in-nice) | $(bytes-out-nice)</td>
										</tr>
										<tr>
										<td align="right">Timespan</td>
										<td>$(uptime)</td>
										</tr>
										$(if remain-bytes-total)
										<tr>
										<td align="right">Quota</td>
										<td><script language="JavaScript">document.write(readablizeBytes($(remain-bytes-total)));</script></td>
										</tr>
										$(endif)
										$(if session-time-left)
										<tr>
										<td align="right">Remaining</td>
										<td>$(session-time-left)</td>
										</tr>
										$(endif)
									</table>
									<div class="mr-b-10">
									<form action="$(link-login)" name="login" onSubmit="return openLogin()">
										<button type="submit" class="btn-md w-12 bg-red pd-5">Signout</button>
									</form>
								</div>
								</div>
							</div>
						</div>
					</div>
				</div>
			</div>
		</div>

	</body>
</html>


File: /radvert.html
<html>
	<head>
		<title id="title">WiFi4Rent by Bytes Crafter</title>
		<meta http-equiv="refresh" content="2; url=$(link-orig)">
		<meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1">
		<meta http-equiv="pragma" content="no-cache">
		<meta http-equiv="expires" content="-1">
		<style type="text/css">
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
		</style>

		<script language="JavaScript">
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
# FREE WiFi Vendo Source Code with Mikrotik device.

This projects include demo uuser credential so that you can use this source asap. But you can always update each and every credential, like random password. You can find the excel file for it on config folder.

### Creating or Editing Users

IP > Hotspot > Users

- To create voucher, set same value for UN/PW.

## Deployment

Use the interent-v1.0.0.backup on config folder to configure and initialized your mikrotik device. This are the credential for this backup: Naming: interent-vX.X.X.backup
Password: bytescrafter

## Contributing

Please read [CONTRIBUTING](CONTRIBUTING) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/BytesCrafter). 

## Authors

* **Bytes Crafter** - *Initial work* - [Github](https://github.com/BytesCrafter/Mikrotik-WiFi-Vendo.git)

See also the list of [contributors](https://github.com/BytesCrafter) who participated in this project.

## License

This project is licensed under the GNU GPL License - see the [LICENSE](LICENSE) file for details

## Acknowledgments

* Mikrotik Community

File: /redirect.html
$(if http-status == 302)Hotspot redirect$(endif)
$(if http-header == "Location")$(link-redirect)$(endif)
<html>
    <head>
        <title id="title">WiFi4Rent by Bytes Crafter</title>
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
    <title id="title">WiFi4Rent by Bytes Crafter</title>
  <meta http-equiv="refresh" content="0; url=$(link-redirect)">
  <meta http-equiv="pragma" content="no-cache">
  <meta http-equiv="expires" content="-1">
  </head>
  <body>
  </body>
</html>


File: /status.html
<html>
    <head>
        <title id="title">WiFi4Rent by Bytes Crafter</title>
        $(if refresh-timeout)
        <meta http-equiv="refresh" content="5"> <!--$(refresh-timeout-secs)-->
        $(endif)
        <meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1">
        <meta name="viewport" content="width=device-width; initial-scale=1.0; maximum-scale=1.0;"/>
        <link rel="stylesheet" href="assets/css/style.css">
        <link rel="icon" href="assets/img/favicon.png" />
        <style>
            iframe  {float:left; height:22px; width:100%;}
        </style>
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
                function readablizeBytes(bytes) {
                    var s = ['bytes', 'kb', 'MB', 'GB', 'TB', 'PB'];
                    var e = Math.floor(Math.log(bytes)/Math.log(1000));
                    return (bytes/Math.pow(1000, Math.floor(e))).toFixed(2)+" "+s[e];
                }
        </script>
    </head>
    <body class="background" bottommargin="0" topmargin="0" leftmargin="0" rightmargin="0" $(if advert-pending == 'yes') onLoad="openAdvert()" $(endif) >

        <div class="container">
            <div class="row mt-10">
                <div class="col-4 mr-a" style="float:none; margin-top: 10%;">
                    <div class="row">
                        <div class="col-12">
                            <div class="box bmh-80 bg-grey-dark box-shadow text-center"><img src="assets/img/banner.png" alt="kemangi 41" style="border-radius: 5px; width:100%; max-width: 200px; height:auto;"/></div>

                            <div class="card box-shadow">
                                <div class="card-header bg-grey-dark"><h3>Status Hotspot</h3></div>
                                <div class="card-body">

                                    $(if login-by == 'trial')
                                        <div class="box w-12 text-center"><h3>Welcome! </h3></div>
                                    $(elif login-by != 'mac')
                                        <div class="box w-12 text-center"><h3>Welcome! </h3></div>
                                        <div class="box w-12 text-center"><h3 id="user">$(username)</h3></div> 
                                    $(endif) 

                                    <div style="padding:10px;"><a class="a" id="cek" href="./detail.html"></a></div>

                                    <form action="$(link-logout)" name="logout" onSubmit="return openLogout()">
                                    
                                        <table class="table table-bordered table-hover mr-b-10">
                                            <tr>
                                                <td align="right">IP Address</td>
                                                <td>$(ip)</td>
                                            </tr>
                                            <tr>
                                                <td align="right" style="width: 40%;">Up | Down</td>
                                                <td>$(bytes-in-nice) | $(bytes-out-nice)</td>
                                            </tr>
                                            <tr>
                                                <td align="right">Uptime</td>
                                                <td>$(uptime)</td>
                                            </tr>
                                            $(if remain-bytes-total)
                                            <tr>
                                                <td align="right">Quota</td>
                                                <td><script language="JavaScript">document.write(readablizeBytes($(remain-bytes-total)));</script></td>
                                            </tr>
                                            $(endif)
                                            $(if session-time-left)
                                            <tr>
                                                <td align="right">Time Left</td>
                                                <td>$(session-time-left)</td>
                                            </tr>
                                            $(endif)
                                            $(if blocked == 'yes')
                                            <tr>
                                                <td align="right">Status</td>
                                                <td><div style="color: rgb(247, 80, 80)"><a href="$(link-advert)" target="hotspot_advert">Click</a> Good</div></td>
                                            </tr>
                                            $(elif refresh-timeout)
                                            <tr>
                                                <td align="right">Refresh</td>
                                                <td>$(refresh-timeout)</td>
                                            </tr>
                                            <tr >
                                                <td align="right">Expired</td>
                                                <td style="padding-top:0px; padding-left:2px;"><iframe id="exp" frameborder="0" scrolling="no" src="about:blank"></iframe></td>
                                            </tr>
                                            $(endif)
                                        </table>

                                        $(if login-by-mac != 'yes')
                                            <button type="submit" class="btn-md w-12 bg-red pd-5">Logout</button>
                                        $(endif)
                                    
                                    </form>

                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <script type="text/javascript">
            //document.getElementById('title').innerHTML = window.location.hostname + " > status";

        //get vaidity
            var usr = document.getElementById('user').innerHTML
            var url = "https://example.com/status/status.php?name="; // http://ip-server-mikhmon/mikhmonv2/status/status.php?name=
            var SessionName = "wifijoss"
            var getvalid = url+usr+"&session="+SessionName
            document.getElementById('exp').src = getvalid;	
    </script>
    </body>
</html>


