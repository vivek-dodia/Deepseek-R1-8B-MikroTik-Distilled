# Repository Information
Name: homeassistant-mikrotik_router

# Directory Structure
Directory structure:
└── github_repos/homeassistant-mikrotik_router/
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
    │   │       ├── pack-101e253c528d48a82e0932be6cb81b48d4c0ec36.idx
    │   │       └── pack-101e253c528d48a82e0932be6cb81b48d4c0ec36.pack
    │   ├── packed-refs
    │   └── refs/
    │       ├── heads/
    │       │   └── master
    │       ├── remotes/
    │       │   └── origin/
    │       │       └── HEAD
    │       └── tags/
    ├── .gitattributes
    ├── .github/
    │   ├── delete-merged-branch-config.yml
    │   ├── FUNDING.yml
    │   ├── generate_releasenotes.py
    │   ├── generate_requirements.py
    │   ├── issue_label_bot.yaml
    │   ├── ISSUE_TEMPLATE/
    │   │   ├── bug_report.md
    │   │   ├── config.yml
    │   │   ├── feature_request.md
    │   │   └── question.md
    │   ├── PULL_REQUEST_TEMPLATE.md
    │   └── workflows/
    │       ├── ci.yml
    │       ├── conflicts.yml
    │       ├── hacs.yml
    │       ├── lock.yml
    │       ├── release.yml
    │       ├── sonarcloud.yml
    │       └── stale.yml
    ├── custom_components/
    │   └── mikrotik_router/
    │       ├── apiparser.py
    │       ├── binary_sensor.py
    │       ├── binary_sensor_types.py
    │       ├── button.py
    │       ├── button_types.py
    │       ├── config_flow.py
    │       ├── const.py
    │       ├── coordinator.py
    │       ├── device_tracker.py
    │       ├── device_tracker_types.py
    │       ├── diagnostics.py
    │       ├── entity.py
    │       ├── exceptions.py
    │       ├── helper.py
    │       ├── manifest.json
    │       ├── mikrotikapi.py
    │       ├── sensor.py
    │       ├── sensor_types.py
    │       ├── services.yaml
    │       ├── strings.json
    │       ├── switch.py
    │       ├── switch_types.py
    │       ├── translations/
    │       │   ├── ar.json
    │       │   ├── cs.json
    │       │   ├── de.json
    │       │   ├── el.json
    │       │   ├── en.json
    │       │   ├── es.json
    │       │   ├── es_ES.json
    │       │   ├── fr.json
    │       │   ├── hi_IN.json
    │       │   ├── hu.json
    │       │   ├── is_IS.json
    │       │   ├── it.json
    │       │   ├── ja.json
    │       │   ├── ko.json
    │       │   ├── lv.json
    │       │   ├── nl.json
    │       │   ├── no.json
    │       │   ├── pl.json
    │       │   ├── pt.json
    │       │   ├── pt_BR.json
    │       │   ├── ru.json
    │       │   ├── sk.json
    │       │   ├── tr.json
    │       │   ├── uk.json
    │       │   ├── vi.json
    │       │   └── zh_CN.json
    │       ├── update.py
    │       ├── update_types.py
    │       └── __init__.py
    ├── docs/
    │   └── assets/
    │       └── images/
    │           ├── flags/
    │           └── ui/
    ├── hacs.json
    ├── info.md
    ├── LICENSE
    ├── Pipfile
    ├── README.md
    ├── requirements.txt
    ├── setup.cfg
    └── sonar-project.properties


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
	url = https://github.com/tomaae/homeassistant-mikrotik_router.git
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
0000000000000000000000000000000000000000 07f81b887eea4bcf9f7ea4da939437d659dddacf vivek-dodia <vivek.dodia@icloud.com> 1738605785 -0500	clone: from https://github.com/tomaae/homeassistant-mikrotik_router.git


File: /.git\logs\refs\heads\master
0000000000000000000000000000000000000000 07f81b887eea4bcf9f7ea4da939437d659dddacf vivek-dodia <vivek.dodia@icloud.com> 1738605785 -0500	clone: from https://github.com/tomaae/homeassistant-mikrotik_router.git


File: /.git\logs\refs\remotes\origin\HEAD
0000000000000000000000000000000000000000 07f81b887eea4bcf9f7ea4da939437d659dddacf vivek-dodia <vivek.dodia@icloud.com> 1738605785 -0500	clone: from https://github.com/tomaae/homeassistant-mikrotik_router.git


File: /.git\packed-refs
# pack-refs with: peeled fully-peeled sorted 
07f81b887eea4bcf9f7ea4da939437d659dddacf refs/remotes/origin/master
8bfc64d4c8cccd95c3caf438d7f3e61564e5d173 refs/tags/1.6
c8e1e807294196800fbcfe74ab217c6069935345 refs/tags/1.6.1
cc381dcaa7189ac7bc7ceb49c5b526eadd09f750 refs/tags/1.7
95bf989f444fd076e2eb70350fb5112b3ba92926 refs/tags/1.7.1
84e8046943f068b0b592a4feb30200ee934e1719 refs/tags/1.7.2
72f8f1bc64d79d0c753f87db2e328429faec58d5 refs/tags/1.7.3
f1268ad1b7819a90da7b4da602de42e09409568c refs/tags/1.7.4
c29fc8dab5e62754cab12515c3be3de7289c2602 refs/tags/2.0
355d16ff4f3a34f9600d2bd3427ccb289f2b3a9f refs/tags/v.2.1.4
119110c09dc7acd9a7606e2b33c89fc0eb3ea6d4 refs/tags/v1.0
99feb4e76ad286c871dc96c9ae8c96b67cc12bfc refs/tags/v1.0.1
a088d41eb247cb19b1a5e171056ba861b6ce4053 refs/tags/v1.0.2
96bbbfc86e3ea1ecd62a1830f95f9b2fed2d0d2e refs/tags/v1.0.3
fa1394efbe50be555b131affc4781e9e3ed62a1d refs/tags/v1.0.4
d1f8a7f56bdf5e67f1295348bf6f482c79c830d4 refs/tags/v1.1
6467673dcef9824d31c236240408b1db1976c328 refs/tags/v1.1.1
10898768e32ced4d5eadf3c30880fab18d7d13ef refs/tags/v1.1.2
3534215a48fa144661a0efbfb575bfac8c26a191 refs/tags/v1.1.3
58ef81d840859a93e889664b1532cc25887f277c refs/tags/v1.1.4
2a9585a4b3278612453877e83cb669c87a46c285 refs/tags/v1.2
d68ffbdc4615d1bfead8044b5baaf114516e2268 refs/tags/v1.2.1
0f7ad23e3c2ff362f0794702d7e0697db0afc23e refs/tags/v1.2.2
1010a8aa3a6874f1133810d950b920f3dedbad94 refs/tags/v1.3
0a58db40cd0e4feb761cb31d267a817e0c45b896 refs/tags/v1.3.1
1ec4e13eb85eee9b219d6b53bd027a3ee22d5e43 refs/tags/v1.4
03d1162e7d951050789450b3001aed5878920eb0 refs/tags/v1.4.1
a1a407ca3c13b02a6243fdd91d1a77667334f2b2 refs/tags/v1.5
897d5dc0c4b25329a0c00b57016d4430e95dd42b refs/tags/v1.5.1
6cd04e7afd8cc6446afaa925af26ae235dc9c665 refs/tags/v1.5.10
f5f8608cb979a31b32da1a1b1573e29509ec316a refs/tags/v1.5.2
cd4d0a09ee456b10308055e0f4b5737a643ddbd5 refs/tags/v1.5.3
846b487810327db48491bdf38d5b82a6b81787fa refs/tags/v1.5.4
78e8af6ade09566cc38318ce7b11a43881bee1e6 refs/tags/v1.5.5
55f8ad2fb4f82154272ed6d3d9920865739bd704 refs/tags/v1.5.6
b53c346dc6330963ee959c18304708bef36eef08 refs/tags/v1.5.7
9eff45426913f581f822532a9c5693d1f7adfbc5 refs/tags/v1.5.8
42fc922b8fae483f03fc402c6ca8e2e6ee3661fe refs/tags/v1.5.9
5db1c78de74ac06fe454cfb6c9c5b2f0ca352764 refs/tags/v1.8
f8b8dd075b84274debc51a20ff26e70280a63a12 refs/tags/v2.1
d420a8ad0676cf7f670259894f696d148c9ee66b refs/tags/v2.1.1
c45eff65e0e54816a5140d55d48817c43a515d54 refs/tags/v2.1.2
380884d60a9a7cd1e8aab05dfa390303f442caa9 refs/tags/v2.1.3


File: /.git\refs\heads\master
07f81b887eea4bcf9f7ea4da939437d659dddacf


File: /.git\refs\remotes\origin\HEAD
ref: refs/remotes/origin/master


File: /.gitattributes
.gitattributes export-ignore
.gitignore export-ignore
.github export-ignore
docs export-ignore

File: /.github\delete-merged-branch-config.yml
exclude: 
  - master
delete_closed_pr: false


File: /.github\FUNDING.yml
ko_fi: tomaae


File: /.github\generate_releasenotes.py
# MIT License
#
# Copyright (c) 2019 Joakim Sørensen @ludeeus
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import re
import sys
from github import Github

BODY = """
[![Downloads for this release](https://img.shields.io/github/downloads/tomaae/homeassistant-mikrotik_router/{version}/total.svg)](https://github.com/tomaae/homeassistant-mikrotik_router/releases/{version})

{changes}
"""

CHANGES = """
## Changes

{integration_changes}

"""

CHANGE = "- [{line}]({link}) @{author}\n"
NOCHANGE = "_No changes in this release._"

GITHUB = Github(sys.argv[2])


def new_commits(repo, sha):
    """Get new commits in repo."""
    from datetime import datetime

    dateformat = "%a, %d %b %Y %H:%M:%S GMT"
    release_commit = repo.get_commit(sha)
    since = datetime.strptime(release_commit.last_modified, dateformat)
    commits = repo.get_commits(since=since)
    if len(list(commits)) == 1:
        return False
    return reversed(list(commits)[:-1])


def last_integration_release(github, skip=True):
    """Return last release."""
    repo = github.get_repo("tomaae/homeassistant-mikrotik_router")
    tag_sha = None
    data = {}
    tags = list(repo.get_tags())
    reg = "(v|^)?(\\d+\\.)?(\\d+\\.)?(\\*|\\d+)$"
    if tags:
        for tag in tags:
            tag_name = tag.name
            if re.match(reg, tag_name):
                tag_sha = tag.commit.sha
                if skip:
                    skip = False
                    continue
                break
    data["tag_name"] = tag_name
    data["tag_sha"] = tag_sha
    return data


def get_integration_commits(github, skip=True):
    changes = ""
    repo = github.get_repo("tomaae/homeassistant-mikrotik_router")
    commits = new_commits(repo, last_integration_release(github, skip)["tag_sha"])

    if not commits:
        changes = NOCHANGE
    else:
        for commit in commits:
            msg = repo.get_git_commit(commit.sha).message
            if "flake" in msg:
                continue
            if " workflow" in msg:
                continue
            if " test" in msg:
                continue
            if "docs" in msg:
                continue
            if "dev debug" in msg:
                continue
            if "Merge branch " in msg:
                continue
            if "Merge pull request " in msg:
                continue
            if "\n" in msg:
                msg = msg.split("\n")[0]
            if commit.author:
                ath = commit.author
            else:
                ath = "Unknown"
            changes += CHANGE.format(line=msg, link=commit.html_url, author=ath)

    return changes


# Update release notes:
UPDATERELEASE = str(sys.argv[4])
REPO = GITHUB.get_repo("tomaae/homeassistant-mikrotik_router")
if UPDATERELEASE == "yes":
    VERSION = str(sys.argv[6]).replace("refs/tags/", "")
    RELEASE = REPO.get_release(VERSION)
    RELEASE.update_release(
        name=f"Mikrotik Router {VERSION}",
        message=BODY.format(
            version=VERSION,
            changes=CHANGES.format(
                integration_changes=get_integration_commits(GITHUB),
            ),
        ),
    )
else:
    integration_changes = get_integration_commits(GITHUB, False)
    if integration_changes != NOCHANGE:
        VERSION = last_integration_release(GITHUB, False)["tag_name"]
        VERSION = f"{VERSION[:-1]}{int(VERSION[-1])+1}"
        REPO.create_issue(
            title=f"Create release {VERSION}?",
            labels=["New release"],
            assignee="tomaae",
            body=CHANGES.format(
                integration_changes=integration_changes,
            ),
        )
    else:
        print("Not enough changes for a release.")


File: /.github\generate_requirements.py
import configparser


def main():
    parser = configparser.ConfigParser()
    parser.read("Pipfile")

    packages = "packages"
    with open("requirements.txt", "w") as f:
        for key in parser[packages]:
            value = parser[packages][key]
            f.write(key + value.replace('"', "") + "\n")

    devpackages = "dev-packages"
    with open("requirements_tests.txt", "w") as f:
        for key in parser[devpackages]:
            value = parser[devpackages][key]
            f.write(key + value.replace('"', "") + "\n")


if __name__ == "__main__":
    main()


File: /.github\issue_label_bot.yaml
label-alias:
  bug: 'bug'
  feature_request: 'enhancement'
  question: 'question'


File: /.github\ISSUE_TEMPLATE\bug_report.md
---
name: Bug report
about: Create a report to help us improve
title: "[Bug]"
labels: bug
assignees: ''

---

## Describe the issue
<!--
A clear and concise description of what the issue is.
-->


## How to reproduce the issue
<!--
Steps to reproduce the behavior:
1. Go to '...'
2. Click on '....'
3. See error
-->


## Expected behavior
<!--
A clear and concise description of what you expected to happen.
-->


## Screenshots
<!--
If applicable, add screenshots to help explain your problem.
-->


## Software versions
<!--
All fields in this sections are required.
-->
 - Home Assistant version: <!-- e.g. HA 2022.2.0 -->
 - Mikrotik Router integration version: <!-- e.g. v1.0.0 -->
 - Mikrotik Hardware: <!-- e.g. RB4011iGS+ -->
 - RouterOS version: <!-- e.g. v6.45 -->


## Diagnostics data
<!--
  If you are seing incorrect data through the integration, please upload integration diagnostics data.
-->


## Traceback/Error logs
<!--
  If you come across any trace or error logs, please provide them.
-->


## Additional context
<!--
Add any other context about the problem here.
-->


File: /.github\ISSUE_TEMPLATE\config.yml
blank_issues_enabled: false

File: /.github\ISSUE_TEMPLATE\feature_request.md
---
name: Feature request
about: Suggest an idea for this project
title: "[Feature]"
labels: enhancement
assignees: ''

---

## Is your feature request related to a problem? Please describe.
<!--
A clear and concise description of what the problem is. Ex. I'm always frustrated when [...]
-->


## Describe the solution you'd like
<!--
A clear and concise description of what you want to happen.
-->


## Describe alternatives you've considered
<!--
A clear and concise description of any alternative solutions or features you've considered.
-->


## Additional context
<!--
Add any other context or screenshots about the feature request here.
-->


File: /.github\ISSUE_TEMPLATE\question.md
---
name: Question
about: Ask a question
title: "[Question]"
labels: question
assignees: ''

---



File: /.github\PULL_REQUEST_TEMPLATE.md
## Proposed change
<!--
  Describe the big picture of your changes here. If it fixes a bug
  or resolves a feature request, be sure to link to that issue.
-->


## Type of change
<!--
  What type of change does your PR introduces?
-->
- [ ] Bugfix
- [ ] New feature
- [ ] Code quality improvements to existing code or addition of tests
- [ ] Documentation

## Additional information
<!--
  Add any other context about your PR here.
-->

## Checklist
<!--
  Put an `x` in the boxes that apply. You can also fill these out after
  creating the PR. If you're unsure about any of them, don't hesitate to ask.
-->
- [ ] The code change is tested and works locally.
- [ ] The code has been formatted using Black.
- [ ] Tests have been added to verify that the new code works.
- [ ] Documentation added/updated if required.


File: /.github\workflows\ci.yml
name: CI

on:
  push:
    paths:
      - 'custom_components/**'
      - 'tests/**'
  pull_request:
    types: [opened, synchronize, reopened]
    paths:
      - 'custom_components/**'
      - 'tests/**'
  workflow_dispatch:

jobs:

  black:
    name: Python Code Format Check
    runs-on: ubuntu-latest
    steps:
      - name: Check out code from GitHub
        uses: "actions/checkout@v3"
      - name: Black Code Format Check
        uses: lgeiger/black-action@master
        with:
          args: ". --check --fast --diff"

  tests:
    name: Python Tests
    runs-on: ubuntu-latest
    steps:
      - name: Check out code from GitHub
        uses: "actions/checkout@v3"
      - name: Set up Python 3.10
        uses: actions/setup-python@v4
        with:
          python-version: '3.10'
      - name: Generate Requirements lists
        run: |
          python3 .github/generate_requirements.py
      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install -r requirements.txt
          pip install -r requirements_tests.txt
      - name: Lint with flake8
        run: |
          pip install flake8
          flake8 . --count --select=E9,F63,F7,F82 --ignore W503,E722,F722  --show-source --statistics
          flake8 . --count --exit-zero --max-complexity=15 --max-line-length=127 --statistics
  #     - name: Test with pytest
  #       run: |
  #         pip install pytest
  #         pytest

  security:
    name: Security check - Bandit
    needs: [tests]
    runs-on: ubuntu-latest
    steps:
      - name: Check out code from GitHub
        uses: "actions/checkout@v3"
      - name: Security check - Bandit
        uses: ioggstream/bandit-report-artifacts@v0.0.2
        with:
          project_path: custom_components/mikrotik_router
          config_file: .github/bandit.yaml
          ignore_failure: false
      - name: Security check report artifacts
        uses: actions/upload-artifact@v3
        with:
          name: Security report
          path: output/security_report.txt

  validate:
    name: Check hassfest
    needs: [tests]
    runs-on: "ubuntu-latest"
    steps:
      - name: Check out code from GitHub
        uses: "actions/checkout@v3"
      - name: Run hassfest
        uses: home-assistant/actions/hassfest@master


File: /.github\workflows\conflicts.yml
name: Check for PR merge conflicts

on:
  push:
  pull_request:
      types: [opened, synchronize, reopened]
jobs:
  check_conflicts:
    name: Check for PR merge conflicts
    runs-on: ubuntu-latest
    steps:
      - uses: mschilde/auto-label-merge-conflicts@master
        with:
          CONFLICT_LABEL_NAME: "conflict"
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}


File: /.github\workflows\hacs.yml
name: HACS Action

on:
  push:
  pull_request:
  schedule:
    - cron: "0 0 * * *"

jobs:
  hacs:
    name: HACS Action
    runs-on: "ubuntu-latest"
    steps:
      - uses: "actions/checkout@v2"
      - name: HACS Action
        uses: "hacs/action@main"
        with:
          category: "integration"

File: /.github\workflows\lock.yml
name: Lock

on:
  schedule:
    - cron: "0 0 * * *"
  workflow_dispatch:

permissions:
  issues: write
  pull-requests: write

concurrency:
  group: lock

jobs:
  lock:
    runs-on: ubuntu-latest
    steps:
      - uses: dessant/lock-threads@v3.0.0
        with:
          github-token: ${{ github.token }}
          exclude-any-issue-labels: 'planned, help-wanted'
          exclude-any-pr-labels: 'wip'
          issue-inactive-days: "30"
          issue-lock-reason: ""
          pr-inactive-days: "7"
          pr-lock-reason: ""


File: /.github\workflows\release.yml
name: Release

on:
  release:
    types: [published]

jobs:

  release_zip:
    name: Prepare release
    runs-on: ubuntu-latest
    steps:
      - name: Check out repository
        uses: actions/checkout@v2

      - name: Zip mikrotik_router dir
        run: |
          cd /home/runner/work/homeassistant-mikrotik_router/homeassistant-mikrotik_router/custom_components/mikrotik_router
          zip mikrotik_router.zip -r ./
      - name: Upload zip to release
        uses: svenstaro/upload-release-action@v1-release

        with:
          repo_token: ${{ secrets.GITHUB_TOKEN }}
          file: /home/runner/work/homeassistant-mikrotik_router/homeassistant-mikrotik_router/custom_components/mikrotik_router/mikrotik_router.zip
          asset_name: mikrotik_router.zip
          tag: ${{ github.ref }}
          overwrite: true

  releasenotes:
    name: Prepare releasenotes
    runs-on: ubuntu-latest
    steps:
      - name: Check out repository
        uses: actions/checkout@v2

      - name: Set up Python 3.8
        uses: actions/setup-python@v1
        with:
          python-version: 3.8

      - name: Install requirements
        run: |
          python3 -m pip install setuptools wheel PyGithub

      - name: Update release notes
        run: |
          python3 /home/runner/work/homeassistant-mikrotik_router/homeassistant-mikrotik_router/.github/generate_releasenotes.py --token ${{ secrets.GITHUB_TOKEN }} --release yes --tag ${{ github.ref }}


File: /.github\workflows\sonarcloud.yml
name: SonarCloud

on:
  push:
    paths:
      - 'custom_components/**'
      - 'tests/**'

jobs:

  sonarcloud:
    name: SonarCloud
    runs-on: ubuntu-latest
    steps:
      - name: Check out code from GitHub
        uses: "actions/checkout@v2"
      - name: SonarCloud Code Analysis
        uses: sonarsource/sonarcloud-github-action@master
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
          SONAR_TOKEN: ${{ secrets.SONAR_TOKEN }}


File: /.github\workflows\stale.yml
name: 'Stale'
on:
  schedule:
    - cron: '30 1 * * *'
  workflow_dispatch:

jobs:
  stale:
    name: Stale
    runs-on: ubuntu-latest
    steps:
      - uses: "actions/stale@v9"
        with:
          stale-issue-message: 'This issue has been automatically marked as stale because it has not had recent activity. It will be closed if no further activity occurs.'
          stale-pr-message: 'This PR has been automatically marked as stale because it has not had recent activity. It will be closed if no further activity occurs.'
          close-issue-message: 'This issue was closed because it has been stalled for 5 days with no activity.'
          days-before-stale: 14
          days-before-close: 7
          exempt-issue-labels: 'pinned,security,planned,help wanted'
          exempt-pr-labels: 'pinned,security,planned,help wanted'


File: /custom_components\mikrotik_router\apiparser.py
"""API parser for JSON APIs."""
from datetime import datetime
from logging import getLogger

from pytz import utc
from voluptuous import Optional

from homeassistant.components.diagnostics import async_redact_data

from .const import TO_REDACT

_LOGGER = getLogger(__name__)


# ---------------------------
#   utc_from_timestamp
# ---------------------------
def utc_from_timestamp(timestamp: float) -> datetime:
    """Return a UTC time from a timestamp."""
    return utc.localize(datetime.utcfromtimestamp(timestamp))


# ---------------------------
#   from_entry
# ---------------------------
def from_entry(entry, param, default="") -> str:
    """Validate and return str value an API dict."""
    if "/" in param:
        for tmp_param in param.split("/"):
            if isinstance(entry, dict) and tmp_param in entry:
                entry = entry[tmp_param]
            else:
                return default

        ret = entry
    elif param in entry:
        ret = entry[param]
    else:
        return default

    if default != "":
        if isinstance(ret, str):
            ret = str(ret)
        elif isinstance(ret, int):
            ret = int(ret)
        elif isinstance(ret, float):
            ret = round(float(ret), 2)

    return ret[:255] if isinstance(ret, str) and len(ret) > 255 else ret


# ---------------------------
#   from_entry_bool
# ---------------------------
def from_entry_bool(entry, param, default=False, reverse=False) -> bool:
    """Validate and return a bool value from an API dict."""
    if "/" in param:
        for tmp_param in param.split("/"):
            if isinstance(entry, dict) and tmp_param in entry:
                entry = entry[tmp_param]
            else:
                return default

        ret = entry
    elif param in entry:
        ret = entry[param]
    else:
        return default

    if isinstance(ret, str):
        if ret in ("on", "On", "ON", "yes", "Yes", "YES", "up", "Up", "UP"):
            ret = True
        elif ret in ("off", "Off", "OFF", "no", "No", "NO", "down", "Down", "DOWN"):
            ret = False

    if not isinstance(ret, bool):
        ret = default

    return not ret if reverse else ret


# ---------------------------
#   parse_api
# ---------------------------
def parse_api(
    data=None,
    source=None,
    key=None,
    key_secondary=None,
    key_search=None,
    vals=None,
    val_proc=None,
    ensure_vals=None,
    only=None,
    skip=None,
) -> dict:
    """Get data from API."""
    debug = _LOGGER.getEffectiveLevel() == 10
    if type(source) == dict:
        tmp = source
        source = [tmp]

    if not source:
        if not key and not key_search:
            data = fill_defaults(data, vals)
        return data

    if debug:
        _LOGGER.debug("Processing source %s", async_redact_data(source, TO_REDACT))

    keymap = generate_keymap(data, key_search)
    for entry in source:
        if only and not matches_only(entry, only):
            continue

        if skip and can_skip(entry, skip):
            continue

        uid = None
        if key or key_search:
            uid = get_uid(entry, key, key_secondary, key_search, keymap)
            if not uid:
                continue

            if uid not in data:
                data[uid] = {}

        if debug:
            _LOGGER.debug("Processing entry %s", async_redact_data(entry, TO_REDACT))

        if vals:
            data = fill_vals(data, entry, uid, vals)

        if ensure_vals:
            data = fill_ensure_vals(data, uid, ensure_vals)

        if val_proc:
            data = fill_vals_proc(data, uid, val_proc)

    return data


# ---------------------------
#   get_uid
# ---------------------------
def get_uid(entry, key, key_secondary, key_search, keymap) -> Optional(str):
    """Get UID for data list."""
    uid = None
    if not key_search:
        key_primary_found = key in entry
        if key_primary_found and key not in entry and not entry[key]:
            return None

        if key_primary_found:
            uid = entry[key]
        elif key_secondary:
            if key_secondary not in entry:
                return None

            if not entry[key_secondary]:
                return None

            uid = entry[key_secondary]
    elif keymap and key_search in entry and entry[key_search] in keymap:
        uid = keymap[entry[key_search]]
    else:
        return None

    return uid or None


# ---------------------------
#   generate_keymap
# ---------------------------
def generate_keymap(data, key_search) -> Optional(dict):
    """Generate keymap."""
    return (
        {data[uid][key_search]: uid for uid in data if key_search in data[uid]}
        if key_search
        else None
    )


# ---------------------------
#   matches_only
# ---------------------------
def matches_only(entry, only) -> bool:
    """Return True if all variables are matched."""
    ret = False
    for val in only:
        if val["key"] in entry and entry[val["key"]] == val["value"]:
            ret = True
        else:
            ret = False
            break

    return ret


# ---------------------------
#   can_skip
# ---------------------------
def can_skip(entry, skip) -> bool:
    """Return True if at least one variable matches."""
    ret = False
    for val in skip:
        if val["name"] in entry and entry[val["name"]] == val["value"]:
            ret = True
            break

        if val["value"] == "" and val["name"] not in entry:
            ret = True
            break

    return ret


# ---------------------------
#   fill_defaults
# ---------------------------
def fill_defaults(data, vals) -> dict:
    """Fill defaults if source is not present."""
    for val in vals:
        _name = val["name"]
        _type = val["type"] if "type" in val else "str"
        _source = val["source"] if "source" in val else _name

        if _type == "str":
            _default = val["default"] if "default" in val else ""
            if "default_val" in val and val["default_val"] in val:
                _default = val[val["default_val"]]

            if _name not in data:
                data[_name] = from_entry([], _source, default=_default)

        elif _type == "bool":
            _default = val["default"] if "default" in val else False
            _reverse = val["reverse"] if "reverse" in val else False
            if _name not in data:
                data[_name] = from_entry_bool(
                    [], _source, default=_default, reverse=_reverse
                )

    return data


# ---------------------------
#   fill_vals
# ---------------------------
def fill_vals(data, entry, uid, vals) -> dict:
    """Fill all data."""
    for val in vals:
        _name = val["name"]
        _type = val["type"] if "type" in val else "str"
        _source = val["source"] if "source" in val else _name
        _convert = val["convert"] if "convert" in val else None

        if _type == "str":
            _default = val["default"] if "default" in val else ""
            if "default_val" in val and val["default_val"] in val:
                _default = val[val["default_val"]]

            if uid:
                data[uid][_name] = from_entry(entry, _source, default=_default)
            else:
                data[_name] = from_entry(entry, _source, default=_default)

        elif _type == "bool":
            _default = val["default"] if "default" in val else False
            _reverse = val["reverse"] if "reverse" in val else False

            if uid:
                data[uid][_name] = from_entry_bool(
                    entry, _source, default=_default, reverse=_reverse
                )
            else:
                data[_name] = from_entry_bool(
                    entry, _source, default=_default, reverse=_reverse
                )

        if _convert == "utc_from_timestamp":
            if uid:
                if isinstance(data[uid][_name], int) and data[uid][_name] > 0:
                    if data[uid][_name] > 100000000000:
                        data[uid][_name] = data[uid][_name] / 1000

                    data[uid][_name] = utc_from_timestamp(data[uid][_name])
            elif isinstance(data[_name], int) and data[_name] > 0:
                if data[_name] > 100000000000:
                    data[_name] = data[_name] / 1000

                data[_name] = utc_from_timestamp(data[_name])

    return data


# ---------------------------
#   fill_ensure_vals
# ---------------------------
def fill_ensure_vals(data, uid, ensure_vals) -> dict:
    """Add required keys which are not available in data."""
    for val in ensure_vals:
        if uid:
            if val["name"] not in data[uid]:
                _default = val["default"] if "default" in val else ""
                data[uid][val["name"]] = _default

        elif val["name"] not in data:
            _default = val["default"] if "default" in val else ""
            data[val["name"]] = _default

    return data


# ---------------------------
#   fill_vals_proc
# ---------------------------
def fill_vals_proc(data, uid, vals_proc) -> dict:
    """Add custom keys."""
    _data = data[uid] if uid else data
    for val_sub in vals_proc:
        _name = None
        _action = None
        _value = None
        for val in val_sub:
            if "name" in val:
                _name = val["name"]
                continue

            if "action" in val:
                _action = val["action"]
                continue

            if not _name and not _action:
                break

            if _action == "combine":
                if "key" in val:
                    tmp = _data[val["key"]] if val["key"] in _data else "unknown"
                    _value = f"{_value}{tmp}" if _value else tmp

                if "text" in val:
                    tmp = val["text"]
                    _value = f"{_value}{tmp}" if _value else tmp

        if _name and _value:
            if uid:
                data[uid][_name] = _value
            else:
                data[_name] = _value

    return data


File: /custom_components\mikrotik_router\binary_sensor.py
"""Support for the Mikrotik Router binary sensor service."""
from __future__ import annotations

from logging import getLogger
from collections.abc import Mapping
from typing import Any

from homeassistant.components.binary_sensor import BinarySensorEntity
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback

from .binary_sensor_types import (
    SENSOR_TYPES,
    SENSOR_SERVICES,
    DEVICE_ATTRIBUTES_IFACE_ETHER,
    DEVICE_ATTRIBUTES_IFACE_SFP,
    DEVICE_ATTRIBUTES_IFACE_WIRELESS,
    DEVICE_ATTRIBUTES_NETWATCH,
)
from .const import (
    CONF_SENSOR_PPP,
    DEFAULT_SENSOR_PPP,
    CONF_SENSOR_PORT_TRACKER,
    DEFAULT_SENSOR_PORT_TRACKER,
    CONF_SENSOR_NETWATCH_TRACKER,
    DEFAULT_SENSOR_NETWATCH_TRACKER,
)
from .entity import MikrotikEntity, async_add_entities
from .helper import format_attribute

_LOGGER = getLogger(__name__)


# ---------------------------
#   async_setup_entry
# ---------------------------
async def async_setup_entry(
    hass: HomeAssistant,
    config_entry: ConfigEntry,
    _async_add_entities: AddEntitiesCallback,
) -> None:
    """Set up entry for component"""
    dispatcher = {
        "MikrotikBinarySensor": MikrotikBinarySensor,
        "MikrotikPPPSecretBinarySensor": MikrotikPPPSecretBinarySensor,
        "MikrotikPortBinarySensor": MikrotikPortBinarySensor,
    }
    await async_add_entities(hass, config_entry, dispatcher)


# ---------------------------
#   MikrotikBinarySensor
# ---------------------------
class MikrotikBinarySensor(MikrotikEntity, BinarySensorEntity):
    """Define an Mikrotik Controller Binary Sensor."""

    @property
    def is_on(self) -> bool:
        """Return true if device is on."""
        return self._data[self.entity_description.data_attribute]

    @property
    def icon(self) -> str:
        """Return the icon."""
        if self.entity_description.icon_enabled:
            if self._data[self.entity_description.data_attribute]:
                return self.entity_description.icon_enabled
            else:
                return self.entity_description.icon_disabled


# ---------------------------
#   MikrotikPPPSecretBinarySensor
# ---------------------------
class MikrotikPPPSecretBinarySensor(MikrotikBinarySensor):
    """Representation of a network device."""

    @property
    def option_sensor_ppp(self) -> bool:
        """Config entry option."""
        return self._config_entry.options.get(CONF_SENSOR_PPP, DEFAULT_SENSOR_PPP)

    @property
    def is_on(self) -> bool:
        """Return true if device is on."""
        return (
            self._data[self.entity_description.data_attribute]
            if self.option_sensor_ppp
            else False
        )

    # @property
    # def available(self) -> bool:
    #     """Return if controller is available."""
    #     return self._ctrl.connected() if self.option_sensor_ppp else False


# ---------------------------
#   MikrotikPortBinarySensor
# ---------------------------
class MikrotikPortBinarySensor(MikrotikBinarySensor):
    """Representation of a network port."""

    @property
    def option_sensor_port_tracker(self) -> bool:
        """Config entry option to not track ARP."""
        return self._config_entry.options.get(
            CONF_SENSOR_PORT_TRACKER, DEFAULT_SENSOR_PORT_TRACKER
        )

    # @property
    # def available(self) -> bool:
    #     """Return if controller is available."""
    #     return self._ctrl.connected() if self.option_sensor_port_tracker else False

    @property
    def icon(self) -> str:
        """Return the icon."""
        if self._data[self.entity_description.data_attribute]:
            icon = self.entity_description.icon_enabled
        else:
            icon = self.entity_description.icon_disabled

        if not self._data["enabled"]:
            icon = "mdi:lan-disconnect"

        return icon

    @property
    def extra_state_attributes(self) -> Mapping[str, Any]:
        """Return the state attributes."""
        attributes = super().extra_state_attributes

        if self._data["type"] == "ether":
            for variable in DEVICE_ATTRIBUTES_IFACE_ETHER:
                if variable in self._data:
                    attributes[format_attribute(variable)] = self._data[variable]

            if "sfp-shutdown-temperature" in self._data:
                for variable in DEVICE_ATTRIBUTES_IFACE_SFP:
                    if variable in self._data:
                        attributes[format_attribute(variable)] = self._data[variable]

        elif self._data["type"] == "wlan":
            for variable in DEVICE_ATTRIBUTES_IFACE_WIRELESS:
                if variable in self._data:
                    attributes[format_attribute(variable)] = self._data[variable]

        return attributes


File: /custom_components\mikrotik_router\binary_sensor_types.py
"""Definitions for Mikrotik Router binary sensor entities."""
from __future__ import annotations

from dataclasses import dataclass, field
from typing import List
from homeassistant.helpers.device_registry import CONNECTION_NETWORK_MAC
from homeassistant.helpers.entity import EntityCategory
from homeassistant.components.binary_sensor import (
    BinarySensorDeviceClass,
    BinarySensorEntityDescription,
)

from .const import DOMAIN

DEVICE_ATTRIBUTES_PPP_SECRET = [
    "connected",
    "service",
    "profile",
    "comment",
    "caller-id",
    "encoding",
]

DEVICE_ATTRIBUTES_IFACE = [
    "running",
    "enabled",
    "comment",
    "client-ip-address",
    "client-mac-address",
    "port-mac-address",
    "last-link-down-time",
    "last-link-up-time",
    "link-downs",
    "actual-mtu",
    "type",
    "name",
]

DEVICE_ATTRIBUTES_IFACE_ETHER = [
    "status",
    "auto-negotiation",
    "rate",
    "full-duplex",
    "default-name",
    "poe-out",
]

DEVICE_ATTRIBUTES_IFACE_SFP = [
    "status",
    "auto-negotiation",
    "advertising",
    "link-partner-advertising",
    "sfp-temperature",
    "sfp-supply-voltage",
    "sfp-module-present",
    "sfp-tx-bias-current",
    "sfp-tx-power",
    "sfp-rx-power",
    "sfp-rx-loss",
    "sfp-tx-fault",
    "sfp-type",
    "sfp-connector-type",
    "sfp-vendor-name",
    "sfp-vendor-part-number",
    "sfp-vendor-revision",
    "sfp-vendor-serial",
    "sfp-manufacturing-date",
    "eeprom-checksum",
]

DEVICE_ATTRIBUTES_IFACE_WIRELESS = [
    "ssid",
    "mode",
    "radio-name",
    "interface-type",
    "country",
    "installation",
    "antenna-gain",
    "frequency",
    "band",
    "channel-width",
    "secondary-frequency",
    "wireless-protocol",
    "rate-set",
    "distance",
    "tx-power-mode",
    "vlan-id",
    "wds-mode",
    "wds-default-bridge",
    "bridge-mode",
    "hide-ssid",
]

DEVICE_ATTRIBUTES_UPS = [
    "name",
    "offline-time",
    "min-runtime",
    "alarm-setting",
    "model",
    "serial",
    "manufacture-date",
    "nominal-battery-voltage",
    "runtime-left",
    "battery-charge",
    "battery-voltage",
    "line-voltage",
    "load",
    "hid-self-test",
]

DEVICE_ATTRIBUTES_NETWATCH = [
    "host",
    "type",
    "interval",
    "port",
    "http-codes",
    "status",
    "comment",
]


@dataclass
class MikrotikBinarySensorEntityDescription(BinarySensorEntityDescription):
    """Class describing mikrotik entities."""

    icon_enabled: str | None = None
    icon_disabled: str | None = None
    ha_group: str | None = None
    ha_connection: str | None = None
    ha_connection_value: str | None = None
    data_path: str | None = None
    data_attribute: str = "available"
    data_name: str | None = None
    data_name_comment: bool = False
    data_uid: str | None = None
    data_reference: str | None = None
    data_attributes_list: List = field(default_factory=lambda: [])
    func: str = "MikrotikBinarySensor"


SENSOR_TYPES: tuple[BinarySensorEntityDescription, ...] = (
    MikrotikBinarySensorEntityDescription(
        key="system_ups",
        name="UPS",
        icon_enabled="",
        icon_disabled="",
        device_class=BinarySensorDeviceClass.POWER,
        entity_category=EntityCategory.DIAGNOSTIC,
        ha_group="System",
        data_path="ups",
        data_attribute="on-line",
        data_uid="",
        data_reference="",
        data_attributes_list=DEVICE_ATTRIBUTES_UPS,
    ),
    MikrotikBinarySensorEntityDescription(
        key="ppp_tracker",
        name="PPP",
        icon_enabled="mdi:account-network-outline",
        icon_disabled="mdi:account-off-outline",
        device_class=BinarySensorDeviceClass.CONNECTIVITY,
        ha_group="PPP",
        ha_connection=DOMAIN,
        ha_connection_value="PPP",
        data_path="ppp_secret",
        data_attribute="connected",
        data_name="name",
        data_uid="name",
        data_reference="name",
        data_attributes_list=DEVICE_ATTRIBUTES_PPP_SECRET,
        func="MikrotikPPPSecretBinarySensor",
    ),
    MikrotikBinarySensorEntityDescription(
        key="interface",
        name="Connection",
        icon_enabled="mdi:lan-connect",
        icon_disabled="mdi:lan-pending",
        device_class=BinarySensorDeviceClass.CONNECTIVITY,
        ha_group="data__default-name",
        ha_connection=CONNECTION_NETWORK_MAC,
        ha_connection_value="data__port-mac-address",
        data_path="interface",
        data_attribute="running",
        data_name="default-name",
        data_uid="default-name",
        data_reference="default-name",
        data_attributes_list=DEVICE_ATTRIBUTES_IFACE,
        func="MikrotikPortBinarySensor",
    ),
    MikrotikBinarySensorEntityDescription(
        key="netwatch",
        name="Netwatch",
        icon_enabled="mdi:lan-connect",
        icon_disabled="mdi:lan-pending",
        device_class=BinarySensorDeviceClass.CONNECTIVITY,
        ha_group="Netwatch",
        ha_connection=DOMAIN,
        ha_connection_value="Netwatch",
        data_path="netwatch",
        data_attribute="status",
        data_name="host",
        data_name_comment=True,
        data_uid="host",
        data_reference="host",
        data_attributes_list=DEVICE_ATTRIBUTES_NETWATCH,
        func="MikrotikBinarySensor",
    ),
)

SENSOR_SERVICES = {}


File: /custom_components\mikrotik_router\button.py
"""Support for the Mikrotik Router buttons."""
from __future__ import annotations

from logging import getLogger

from homeassistant.components.button import ButtonEntity
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback

from .entity import MikrotikEntity, async_add_entities
from .button_types import (
    SENSOR_TYPES,
    SENSOR_SERVICES,
)

_LOGGER = getLogger(__name__)


# ---------------------------
#   async_setup_entry
# ---------------------------
async def async_setup_entry(
    hass: HomeAssistant,
    config_entry: ConfigEntry,
    _async_add_entities: AddEntitiesCallback,
) -> None:
    """Set up entry for component"""
    dispatcher = {
        "MikrotikButton": MikrotikButton,
        "MikrotikScriptButton": MikrotikScriptButton,
    }
    await async_add_entities(hass, config_entry, dispatcher)


# ---------------------------
#   MikrotikButton
# ---------------------------
class MikrotikButton(MikrotikEntity, ButtonEntity):
    """Representation of a button."""

    async def async_update(self):
        """Synchronize state with controller."""

    async def async_press(self) -> None:
        pass


# ---------------------------
#   MikrotikScriptButton
# ---------------------------
class MikrotikScriptButton(MikrotikButton):
    """Representation of a script button."""

    async def async_press(self) -> None:
        """Process the button press."""
        self.coordinator.run_script(self._data["name"])


File: /custom_components\mikrotik_router\button_types.py
"""Definitions for Mikrotik Router button entities."""
from __future__ import annotations

from dataclasses import dataclass, field
from typing import List

from homeassistant.components.sensor import (
    SensorEntityDescription,
)

from .const import DOMAIN

DEVICE_ATTRIBUTES_SCRIPT = [
    "last-started",
    "run-count",
]


@dataclass
class MikrotikButtonEntityDescription(SensorEntityDescription):
    """Class describing mikrotik entities."""

    ha_group: str | None = None
    ha_connection: str | None = None
    ha_connection_value: str | None = None
    data_path: str | None = None
    data_attribute: str | None = None
    data_name: str | None = None
    data_name_comment: bool = False
    data_uid: str | None = None
    data_reference: str | None = None
    data_attributes_list: List = field(default_factory=lambda: [])
    func: str = "MikrotikButton"


SENSOR_TYPES: tuple[MikrotikButtonEntityDescription, ...] = (
    MikrotikButtonEntityDescription(
        key="script",
        name="",
        icon="mdi:script-text-outline",
        device_class=None,
        entity_category=None,
        ha_group="Script",
        ha_connection=DOMAIN,
        ha_connection_value="Script",
        data_path="script",
        data_name="name",
        data_uid="name",
        data_reference="name",
        data_attributes_list=DEVICE_ATTRIBUTES_SCRIPT,
        func="MikrotikScriptButton",
    ),
)

SENSOR_SERVICES = {}


File: /custom_components\mikrotik_router\config_flow.py
"""Config flow to configure Mikrotik Router."""

import logging

import voluptuous as vol
from homeassistant.config_entries import (
    CONN_CLASS_LOCAL_POLL,
    ConfigFlow,
    OptionsFlow,
)
from homeassistant.const import (
    CONF_NAME,
    CONF_HOST,
    CONF_PORT,
    CONF_USERNAME,
    CONF_PASSWORD,
    CONF_SSL,
    CONF_ZONE,
    STATE_HOME,
)
from homeassistant.core import callback

from .const import (
    DOMAIN,
    CONF_TRACK_IFACE_CLIENTS,
    DEFAULT_TRACK_IFACE_CLIENTS,
    CONF_SCAN_INTERVAL,
    DEFAULT_SCAN_INTERVAL,
    CONF_TRACK_HOSTS,
    DEFAULT_TRACK_HOSTS,
    CONF_SENSOR_PORT_TRACKER,
    DEFAULT_SENSOR_PORT_TRACKER,
    CONF_SENSOR_PORT_TRAFFIC,
    DEFAULT_SENSOR_PORT_TRAFFIC,
    CONF_SENSOR_CLIENT_TRAFFIC,
    DEFAULT_SENSOR_CLIENT_TRAFFIC,
    CONF_SENSOR_CLIENT_CAPTIVE,
    DEFAULT_SENSOR_CLIENT_CAPTIVE,
    CONF_SENSOR_SIMPLE_QUEUES,
    DEFAULT_SENSOR_SIMPLE_QUEUES,
    CONF_SENSOR_NAT,
    DEFAULT_SENSOR_NAT,
    CONF_SENSOR_MANGLE,
    DEFAULT_SENSOR_MANGLE,
    CONF_SENSOR_FILTER,
    DEFAULT_SENSOR_FILTER,
    CONF_SENSOR_KIDCONTROL,
    DEFAULT_SENSOR_KIDCONTROL,
    CONF_SENSOR_PPP,
    DEFAULT_SENSOR_PPP,
    CONF_SENSOR_SCRIPTS,
    DEFAULT_SENSOR_SCRIPTS,
    CONF_SENSOR_ENVIRONMENT,
    DEFAULT_SENSOR_ENVIRONMENT,
    CONF_TRACK_HOSTS_TIMEOUT,
    DEFAULT_TRACK_HOST_TIMEOUT,
    DEFAULT_HOST,
    DEFAULT_USERNAME,
    DEFAULT_PORT,
    DEFAULT_DEVICE_NAME,
    DEFAULT_SSL,
    DEFAULT_SENSOR_NETWATCH_TRACKER,
    CONF_SENSOR_NETWATCH_TRACKER,
)
from .mikrotikapi import MikrotikAPI

_LOGGER = logging.getLogger(__name__)


# ---------------------------
#   configured_instances
# ---------------------------
@callback
def configured_instances(hass):
    """Return a set of configured instances."""
    return set(
        entry.data[CONF_NAME] for entry in hass.config_entries.async_entries(DOMAIN)
    )


# ---------------------------
#   MikrotikControllerConfigFlow
# ---------------------------
class MikrotikControllerConfigFlow(ConfigFlow, domain=DOMAIN):
    """MikrotikControllerConfigFlow class"""

    VERSION = 1
    CONNECTION_CLASS = CONN_CLASS_LOCAL_POLL

    def __init__(self):
        """Initialize MikrotikControllerConfigFlow."""

    @staticmethod
    @callback
    def async_get_options_flow(config_entry):
        """Get the options flow for this handler."""
        return MikrotikControllerOptionsFlowHandler(config_entry)

    async def async_step_import(self, user_input=None):
        """Occurs when a previously entry setup fails and is re-initiated."""
        return await self.async_step_user(user_input)

    async def async_step_user(self, user_input=None):
        """Handle a flow initialized by the user."""
        errors = {}
        if user_input is not None:
            # Check if instance with this name already exists
            if user_input[CONF_NAME] in configured_instances(self.hass):
                errors["base"] = "name_exists"

            # Test connection
            api = MikrotikAPI(
                host=user_input[CONF_HOST],
                username=user_input[CONF_USERNAME],
                password=user_input[CONF_PASSWORD],
                port=user_input[CONF_PORT],
                use_ssl=user_input[CONF_SSL],
            )
            if not api.connect():
                errors[CONF_HOST] = api.error

            # Save instance
            if not errors:
                return self.async_create_entry(
                    title=user_input[CONF_NAME], data=user_input
                )

            return self._show_config_form(user_input=user_input, errors=errors)

        return self._show_config_form(
            user_input={
                CONF_NAME: DEFAULT_DEVICE_NAME,
                CONF_HOST: DEFAULT_HOST,
                CONF_USERNAME: DEFAULT_USERNAME,
                CONF_PASSWORD: DEFAULT_USERNAME,
                CONF_PORT: DEFAULT_PORT,
                CONF_SSL: DEFAULT_SSL,
            },
            errors=errors,
        )

    # ---------------------------
    #   _show_config_form
    # ---------------------------
    def _show_config_form(self, user_input, errors=None):
        """Show the configuration form to edit data."""
        return self.async_show_form(
            step_id="user",
            data_schema=vol.Schema(
                {
                    vol.Required(CONF_NAME, default=user_input[CONF_NAME]): str,
                    vol.Required(CONF_HOST, default=user_input[CONF_HOST]): str,
                    vol.Required(CONF_USERNAME, default=user_input[CONF_USERNAME]): str,
                    vol.Required(CONF_PASSWORD, default=user_input[CONF_PASSWORD]): str,
                    vol.Optional(CONF_PORT, default=user_input[CONF_PORT]): int,
                    vol.Optional(CONF_SSL, default=user_input[CONF_SSL]): bool,
                }
            ),
            errors=errors,
        )


# ---------------------------
#   MikrotikControllerOptionsFlowHandler
# ---------------------------
class MikrotikControllerOptionsFlowHandler(OptionsFlow):
    """Handle options."""

    def __init__(self, config_entry):
        """Initialize options flow."""
        self.config_entry = config_entry
        self.options = dict(config_entry.options)

    async def async_step_init(self, user_input=None):
        """Manage the options."""
        return await self.async_step_basic_options(user_input)

    async def async_step_basic_options(self, user_input=None):
        """Manage the basic options options."""
        if user_input is not None:
            self.options.update(user_input)
            return await self.async_step_sensor_select()

        return self.async_show_form(
            step_id="basic_options",
            last_step=False,
            data_schema=vol.Schema(
                {
                    vol.Optional(
                        CONF_SCAN_INTERVAL,
                        default=self.config_entry.options.get(
                            CONF_SCAN_INTERVAL, DEFAULT_SCAN_INTERVAL
                        ),
                    ): int,
                    vol.Optional(
                        CONF_TRACK_IFACE_CLIENTS,
                        default=self.config_entry.options.get(
                            CONF_TRACK_IFACE_CLIENTS, DEFAULT_TRACK_IFACE_CLIENTS
                        ),
                    ): bool,
                    vol.Optional(
                        CONF_TRACK_HOSTS_TIMEOUT,
                        default=self.config_entry.options.get(
                            CONF_TRACK_HOSTS_TIMEOUT, DEFAULT_TRACK_HOST_TIMEOUT
                        ),
                    ): int,
                    vol.Optional(
                        CONF_ZONE,
                        default=self.config_entry.options.get(CONF_ZONE, STATE_HOME),
                    ): str,
                }
            ),
        )

    async def async_step_sensor_select(self, user_input=None):
        """Manage the sensor select options."""
        if user_input is not None:
            self.options.update(user_input)
            return self.async_create_entry(title="", data=self.options)

        return self.async_show_form(
            step_id="sensor_select",
            data_schema=vol.Schema(
                {
                    vol.Optional(
                        CONF_SENSOR_PORT_TRACKER,
                        default=self.config_entry.options.get(
                            CONF_SENSOR_PORT_TRACKER, DEFAULT_SENSOR_PORT_TRACKER
                        ),
                    ): bool,
                    vol.Optional(
                        CONF_SENSOR_PORT_TRAFFIC,
                        default=self.config_entry.options.get(
                            CONF_SENSOR_PORT_TRAFFIC, DEFAULT_SENSOR_PORT_TRAFFIC
                        ),
                    ): bool,
                    vol.Optional(
                        CONF_TRACK_HOSTS,
                        default=self.config_entry.options.get(
                            CONF_TRACK_HOSTS, DEFAULT_TRACK_HOSTS
                        ),
                    ): bool,
                    vol.Optional(
                        CONF_SENSOR_CLIENT_TRAFFIC,
                        default=self.config_entry.options.get(
                            CONF_SENSOR_CLIENT_TRAFFIC, DEFAULT_SENSOR_CLIENT_TRAFFIC
                        ),
                    ): bool,
                    vol.Optional(
                        CONF_SENSOR_CLIENT_CAPTIVE,
                        default=self.config_entry.options.get(
                            CONF_SENSOR_CLIENT_CAPTIVE, DEFAULT_SENSOR_CLIENT_CAPTIVE
                        ),
                    ): bool,
                    vol.Optional(
                        CONF_SENSOR_SIMPLE_QUEUES,
                        default=self.config_entry.options.get(
                            CONF_SENSOR_SIMPLE_QUEUES, DEFAULT_SENSOR_SIMPLE_QUEUES
                        ),
                    ): bool,
                    vol.Optional(
                        CONF_SENSOR_NAT,
                        default=self.config_entry.options.get(
                            CONF_SENSOR_NAT, DEFAULT_SENSOR_NAT
                        ),
                    ): bool,
                    vol.Optional(
                        CONF_SENSOR_MANGLE,
                        default=self.config_entry.options.get(
                            CONF_SENSOR_MANGLE, DEFAULT_SENSOR_MANGLE
                        ),
                    ): bool,
                    vol.Optional(
                        CONF_SENSOR_FILTER,
                        default=self.config_entry.options.get(
                            CONF_SENSOR_FILTER, DEFAULT_SENSOR_FILTER
                        ),
                    ): bool,
                    vol.Optional(
                        CONF_SENSOR_KIDCONTROL,
                        default=self.config_entry.options.get(
                            CONF_SENSOR_KIDCONTROL, DEFAULT_SENSOR_KIDCONTROL
                        ),
                    ): bool,
                    vol.Optional(
                        CONF_SENSOR_NETWATCH_TRACKER,
                        default=self.config_entry.options.get(
                            CONF_SENSOR_NETWATCH_TRACKER,
                            DEFAULT_SENSOR_NETWATCH_TRACKER,
                        ),
                    ): bool,
                    vol.Optional(
                        CONF_SENSOR_PPP,
                        default=self.config_entry.options.get(
                            CONF_SENSOR_PPP, DEFAULT_SENSOR_PPP
                        ),
                    ): bool,
                    vol.Optional(
                        CONF_SENSOR_SCRIPTS,
                        default=self.config_entry.options.get(
                            CONF_SENSOR_SCRIPTS, DEFAULT_SENSOR_SCRIPTS
                        ),
                    ): bool,
                    vol.Optional(
                        CONF_SENSOR_ENVIRONMENT,
                        default=self.config_entry.options.get(
                            CONF_SENSOR_ENVIRONMENT, DEFAULT_SENSOR_ENVIRONMENT
                        ),
                    ): bool,
                },
            ),
        )


File: /custom_components\mikrotik_router\const.py
"""Constants used by the Mikrotik Router component and platforms."""
from homeassistant.const import Platform

PLATFORMS = [
    Platform.SENSOR,
    Platform.BINARY_SENSOR,
    Platform.DEVICE_TRACKER,
    Platform.SWITCH,
    Platform.BUTTON,
    Platform.UPDATE,
]

DOMAIN = "mikrotik_router"
DEFAULT_NAME = "Mikrotik Router"
ATTRIBUTION = "Data provided by Mikrotik"

RUN_SCRIPT_COMMAND = "run_script"

DEFAULT_ENCODING = "ISO-8859-1"
DEFAULT_LOGIN_METHOD = "plain"

DEFAULT_HOST = "10.0.0.1"
DEFAULT_USERNAME = "admin"
DEFAULT_PORT = 0
DEFAULT_DEVICE_NAME = "Mikrotik"
DEFAULT_SSL = False

CONF_SCAN_INTERVAL = "scan_interval"
DEFAULT_SCAN_INTERVAL = 30
CONF_TRACK_IFACE_CLIENTS = "track_iface_clients"
DEFAULT_TRACK_IFACE_CLIENTS = True
CONF_TRACK_HOSTS = "track_network_hosts"
DEFAULT_TRACK_HOSTS = False
CONF_TRACK_HOSTS_TIMEOUT = "track_network_hosts_timeout"
DEFAULT_TRACK_HOST_TIMEOUT = 180

CONF_SENSOR_PORT_TRACKER = "sensor_port_tracker"
DEFAULT_SENSOR_PORT_TRACKER = False
CONF_SENSOR_PORT_TRAFFIC = "sensor_port_traffic"
DEFAULT_SENSOR_PORT_TRAFFIC = False
CONF_SENSOR_CLIENT_TRAFFIC = "sensor_client_traffic"
DEFAULT_SENSOR_CLIENT_TRAFFIC = False
CONF_SENSOR_CLIENT_CAPTIVE = "sensor_client_captive"
DEFAULT_SENSOR_CLIENT_CAPTIVE = False
CONF_SENSOR_SIMPLE_QUEUES = "sensor_simple_queues"
DEFAULT_SENSOR_SIMPLE_QUEUES = False
CONF_SENSOR_NAT = "sensor_nat"
DEFAULT_SENSOR_NAT = False
CONF_SENSOR_MANGLE = "sensor_mangle"
DEFAULT_SENSOR_MANGLE = False
CONF_SENSOR_FILTER = "sensor_filter"
DEFAULT_SENSOR_FILTER = False
CONF_SENSOR_PPP = "sensor_ppp"
DEFAULT_SENSOR_PPP = False
CONF_SENSOR_KIDCONTROL = "sensor_kidcontrol"
DEFAULT_SENSOR_KIDCONTROL = False
CONF_SENSOR_SCRIPTS = "sensor_scripts"
DEFAULT_SENSOR_SCRIPTS = False
CONF_SENSOR_ENVIRONMENT = "sensor_environment"
DEFAULT_SENSOR_ENVIRONMENT = False
CONF_SENSOR_NETWATCH_TRACKER = "sensor_netwatch_tracker"
DEFAULT_SENSOR_NETWATCH_TRACKER = False

TO_REDACT = {
    "ip-address",
    "client-ip-address",
    "address",
    "active-address",
    "mac-address",
    "active-mac-address",
    "orig-mac-address",
    "port-mac-address",
    "client-mac-address",
    "client-id",
    "active-client-id",
    "eeprom",
    "sfp-vendor-serial",
    "gateway",
    "dns-server",
    "wins-server",
    "ntp-server",
    "caps-manager",
    "serial-number",
    "source",
    "from-addresses",
    "to-addresses",
    "src-address",
    "dst-address",
    "username",
    "password",
    "caller-id",
    "target",
    "ssid",
}


File: /custom_components\mikrotik_router\coordinator.py
"""Mikrotik coordinator."""

from __future__ import annotations

import ipaddress
import logging
import re
import pytz

from datetime import datetime, timedelta
from dataclasses import dataclass
from ipaddress import ip_address, IPv4Network
from mac_vendor_lookup import AsyncMacLookup

from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers import entity_registry
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator, UpdateFailed
from homeassistant.util.dt import utcnow


from homeassistant.const import (
    CONF_NAME,
    CONF_HOST,
    CONF_PORT,
    CONF_USERNAME,
    CONF_PASSWORD,
    CONF_SSL,
    CONF_ZONE,
    STATE_HOME,
)

from .const import (
    DOMAIN,
    CONF_TRACK_IFACE_CLIENTS,
    DEFAULT_TRACK_IFACE_CLIENTS,
    CONF_TRACK_HOSTS,
    DEFAULT_TRACK_HOSTS,
    CONF_SCAN_INTERVAL,
    DEFAULT_SCAN_INTERVAL,
    CONF_SENSOR_PORT_TRAFFIC,
    DEFAULT_SENSOR_PORT_TRAFFIC,
    CONF_SENSOR_CLIENT_TRAFFIC,
    DEFAULT_SENSOR_CLIENT_TRAFFIC,
    CONF_SENSOR_CLIENT_CAPTIVE,
    DEFAULT_SENSOR_CLIENT_CAPTIVE,
    CONF_SENSOR_SIMPLE_QUEUES,
    DEFAULT_SENSOR_SIMPLE_QUEUES,
    CONF_SENSOR_NAT,
    DEFAULT_SENSOR_NAT,
    CONF_SENSOR_MANGLE,
    DEFAULT_SENSOR_MANGLE,
    CONF_SENSOR_FILTER,
    DEFAULT_SENSOR_FILTER,
    CONF_SENSOR_KIDCONTROL,
    DEFAULT_SENSOR_KIDCONTROL,
    CONF_SENSOR_PPP,
    DEFAULT_SENSOR_PPP,
    CONF_SENSOR_SCRIPTS,
    DEFAULT_SENSOR_SCRIPTS,
    CONF_SENSOR_ENVIRONMENT,
    DEFAULT_SENSOR_ENVIRONMENT,
    CONF_SENSOR_NETWATCH_TRACKER,
    DEFAULT_SENSOR_NETWATCH_TRACKER,
)
from .exceptions import ApiEntryNotFound
from .apiparser import parse_api
from .mikrotikapi import MikrotikAPI

_LOGGER = logging.getLogger(__name__)

DEFAULT_TIME_ZONE = None


def is_valid_ip(address):
    try:
        ipaddress.ip_address(address)
        return True
    except ValueError:
        return False


def utc_from_timestamp(timestamp: float) -> datetime:
    """Return a UTC time from a timestamp."""
    return pytz.utc.localize(datetime.utcfromtimestamp(timestamp))


def as_local(dattim: datetime) -> datetime:
    """Convert a UTC datetime object to local time zone."""
    if dattim.tzinfo == DEFAULT_TIME_ZONE:
        return dattim
    if dattim.tzinfo is None:
        dattim = pytz.utc.localize(dattim)

    return dattim.astimezone(DEFAULT_TIME_ZONE)


@dataclass
class MikrotikData:
    """Data for the mikrotik integration."""

    data_coordinator: MikrotikCoordinator
    tracker_coordinator: MikrotikTrackerCoordinator


class MikrotikTrackerCoordinator(DataUpdateCoordinator[None]):
    def __init__(
        self,
        hass: HomeAssistant,
        config_entry: ConfigEntry,
        coordinator: MikrotikCoordinator,
    ):
        """Initialize MikrotikTrackerCoordinator."""
        self.hass = hass
        self.config_entry: ConfigEntry = config_entry
        self.coordinator = coordinator

        super().__init__(
            self.hass,
            _LOGGER,
            name=DOMAIN,
            update_interval=timedelta(seconds=10),
        )
        self.name = config_entry.data[CONF_NAME]
        self.host = config_entry.data[CONF_HOST]

        self.api = MikrotikAPI(
            config_entry.data[CONF_HOST],
            config_entry.data[CONF_USERNAME],
            config_entry.data[CONF_PASSWORD],
            config_entry.data[CONF_PORT],
            config_entry.data[CONF_SSL],
        )

    # ---------------------------
    #   option_zone
    # ---------------------------
    @property
    def option_zone(self):
        """Config entry option zones."""
        return self.config_entry.options.get(CONF_ZONE, STATE_HOME)

    # ---------------------------
    #   _async_update_data
    # ---------------------------
    async def _async_update_data(self):
        """Trigger update by timer"""
        if not self.coordinator.option_track_network_hosts:
            return

        if "test" not in self.coordinator.ds["access"]:
            return

        for uid in list(self.coordinator.ds["host"]):
            if not self.coordinator.host_tracking_initialized:
                # Add missing default values
                for key, default in zip(
                    [
                        "address",
                        "mac-address",
                        "interface",
                        "host-name",
                        "last-seen",
                        "available",
                    ],
                    ["unknown", "unknown", "unknown", "unknown", False, False],
                ):
                    if key not in self.coordinator.ds["host"][uid]:
                        self.coordinator.ds["host"][uid][key] = default

            # Check host availability
            if (
                self.coordinator.ds["host"][uid]["source"]
                not in ["capsman", "wireless"]
                and self.coordinator.ds["host"][uid]["address"] not in ["unknown", ""]
                and self.coordinator.ds["host"][uid]["interface"] not in ["unknown", ""]
            ):
                tmp_interface = self.coordinator.ds["host"][uid]["interface"]
                if (
                    uid in self.coordinator.ds["arp"]
                    and self.coordinator.ds["arp"][uid]["bridge"] != ""
                ):
                    tmp_interface = self.coordinator.ds["arp"][uid]["bridge"]

                _LOGGER.debug(
                    "Ping host: %s", self.coordinator.ds["host"][uid]["address"]
                )

                self.coordinator.ds["host"][uid][
                    "available"
                ] = await self.hass.async_add_executor_job(
                    self.api.arp_ping,
                    self.coordinator.ds["host"][uid]["address"],
                    tmp_interface,
                )

            # Update last seen
            if self.coordinator.ds["host"][uid]["available"]:
                self.coordinator.ds["host"][uid]["last-seen"] = utcnow()

        self.coordinator.host_tracking_initialized = True

        await self.coordinator.async_process_host()
        return {
            "host": self.coordinator.ds["host"],
            "routerboard": self.coordinator.ds["routerboard"],
        }


# ---------------------------
#   MikrotikControllerData
# ---------------------------
class MikrotikCoordinator(DataUpdateCoordinator[None]):
    """MikrotikCoordinator Class"""

    def __init__(self, hass: HomeAssistant, config_entry: ConfigEntry):
        """Initialize MikrotikCoordinator."""
        self.hass = hass
        self.config_entry: ConfigEntry = config_entry
        super().__init__(
            self.hass,
            _LOGGER,
            name=DOMAIN,
            update_interval=self.option_scan_interval,
        )
        self.name = config_entry.data[CONF_NAME]
        self.host = config_entry.data[CONF_HOST]

        self.ds = {
            "access": {},
            "routerboard": {},
            "resource": {},
            "health": {},
            "health7": {},
            "interface": {},
            "bridge": {},
            "bridge_host": {},
            "arp": {},
            "nat": {},
            "kid-control": {},
            "mangle": {},
            "filter": {},
            "ppp_secret": {},
            "ppp_active": {},
            "fw-update": {},
            "script": {},
            "queue": {},
            "dns": {},
            "dhcp-server": {},
            "dhcp-client": {},
            "dhcp-network": {},
            "dhcp": {},
            "capsman_hosts": {},
            "wireless": {},
            "wireless_hosts": {},
            "host": {},
            "host_hass": {},
            "hostspot_host": {},
            "client_traffic": {},
            "environment": {},
            "ups": {},
            "gps": {},
            "netwatch": {},
        }

        self.notified_flags = []

        self.api = MikrotikAPI(
            config_entry.data[CONF_HOST],
            config_entry.data[CONF_USERNAME],
            config_entry.data[CONF_PASSWORD],
            config_entry.data[CONF_PORT],
            config_entry.data[CONF_SSL],
        )

        self.debug = False
        if _LOGGER.getEffectiveLevel() == 10:
            self.debug = True

        self.nat_removed = {}
        self.mangle_removed = {}
        self.filter_removed = {}
        self.host_hass_recovered = False
        self.host_tracking_initialized = False

        self.support_capsman = False
        self.support_wireless = False
        self.support_ppp = False
        self.support_ups = False
        self.support_gps = False
        self._wifimodule = "wireless"

        self.major_fw_version = 0
        self.minor_fw_version = 0

        self.async_mac_lookup = AsyncMacLookup()
        self.accessrights_reported = False

        self.last_hwinfo_update = datetime(1970, 1, 1)

    # ---------------------------
    #   option_track_iface_clients
    # ---------------------------
    @property
    def option_track_iface_clients(self):
        """Config entry option to not track ARP."""
        return self.config_entry.options.get(
            CONF_TRACK_IFACE_CLIENTS, DEFAULT_TRACK_IFACE_CLIENTS
        )

    # ---------------------------
    #   option_track_network_hosts
    # ---------------------------
    @property
    def option_track_network_hosts(self):
        """Config entry option to not track ARP."""
        return self.config_entry.options.get(CONF_TRACK_HOSTS, DEFAULT_TRACK_HOSTS)

    # ---------------------------
    #   option_sensor_port_traffic
    # ---------------------------
    @property
    def option_sensor_port_traffic(self):
        """Config entry option to not track ARP."""
        return self.config_entry.options.get(
            CONF_SENSOR_PORT_TRAFFIC, DEFAULT_SENSOR_PORT_TRAFFIC
        )

    # ---------------------------
    #   option_sensor_client_traffic
    # ---------------------------
    @property
    def option_sensor_client_traffic(self):
        """Config entry option to not track ARP."""
        return self.config_entry.options.get(
            CONF_SENSOR_CLIENT_TRAFFIC, DEFAULT_SENSOR_CLIENT_TRAFFIC
        )

    # ---------------------------
    #   option_sensor_client_captive
    # ---------------------------
    @property
    def option_sensor_client_captive(self):
        """Config entry option to not track ARP."""
        return self.config_entry.options.get(
            CONF_SENSOR_CLIENT_CAPTIVE, DEFAULT_SENSOR_CLIENT_CAPTIVE
        )

    # ---------------------------
    #   option_sensor_simple_queues
    # ---------------------------
    @property
    def option_sensor_simple_queues(self):
        """Config entry option to not track ARP."""
        return self.config_entry.options.get(
            CONF_SENSOR_SIMPLE_QUEUES, DEFAULT_SENSOR_SIMPLE_QUEUES
        )

    # ---------------------------
    #   option_sensor_nat
    # ---------------------------
    @property
    def option_sensor_nat(self):
        """Config entry option to not track ARP."""
        return self.config_entry.options.get(CONF_SENSOR_NAT, DEFAULT_SENSOR_NAT)

    # ---------------------------
    #   option_sensor_mangle
    # ---------------------------
    @property
    def option_sensor_mangle(self):
        """Config entry option to not track ARP."""
        return self.config_entry.options.get(CONF_SENSOR_MANGLE, DEFAULT_SENSOR_MANGLE)

    # ---------------------------
    #   option_sensor_filter
    # ---------------------------
    @property
    def option_sensor_filter(self):
        """Config entry option to not track ARP."""
        return self.config_entry.options.get(CONF_SENSOR_FILTER, DEFAULT_SENSOR_FILTER)

    # ---------------------------
    #   option_sensor_kidcontrol
    # ---------------------------
    @property
    def option_sensor_kidcontrol(self):
        """Config entry option to not track ARP."""
        return self.config_entry.options.get(
            CONF_SENSOR_KIDCONTROL, DEFAULT_SENSOR_KIDCONTROL
        )

    # ---------------------------
    #   option_sensor_netwatch
    # ---------------------------
    @property
    def option_sensor_netwatch(self):
        """Config entry option to not track ARP."""
        return self.config_entry.options.get(
            CONF_SENSOR_NETWATCH_TRACKER, DEFAULT_SENSOR_NETWATCH_TRACKER
        )

    # ---------------------------
    #   option_sensor_ppp
    # ---------------------------
    @property
    def option_sensor_ppp(self):
        """Config entry option to not track ARP."""
        return self.config_entry.options.get(CONF_SENSOR_PPP, DEFAULT_SENSOR_PPP)

    # ---------------------------
    #   option_sensor_scripts
    # ---------------------------
    @property
    def option_sensor_scripts(self):
        """Config entry option to not track ARP."""
        return self.config_entry.options.get(
            CONF_SENSOR_SCRIPTS, DEFAULT_SENSOR_SCRIPTS
        )

    # ---------------------------
    #   option_sensor_environment
    # ---------------------------
    @property
    def option_sensor_environment(self):
        """Config entry option to not track ARP."""
        return self.config_entry.options.get(
            CONF_SENSOR_ENVIRONMENT, DEFAULT_SENSOR_ENVIRONMENT
        )

    # ---------------------------
    #   option_scan_interval
    # ---------------------------
    @property
    def option_scan_interval(self):
        """Config entry option scan interval."""
        scan_interval = self.config_entry.options.get(
            CONF_SCAN_INTERVAL, DEFAULT_SCAN_INTERVAL
        )
        return timedelta(seconds=scan_interval)

    # ---------------------------
    #   connected
    # ---------------------------
    def connected(self):
        """Return connected state"""
        return self.api.connected()

    # ---------------------------
    #   set_value
    # ---------------------------
    def set_value(self, path, param, value, mod_param, mod_value):
        """Change value using Mikrotik API"""
        return self.api.set_value(path, param, value, mod_param, mod_value)

    # ---------------------------
    #   execute
    # ---------------------------
    def execute(self, path, command, param, value, attributes=None):
        """Change value using Mikrotik API"""
        return self.api.execute(path, command, param, value, attributes)

    # ---------------------------
    #   run_script
    # ---------------------------
    def run_script(self, name):
        """Run script using Mikrotik API"""
        if type(name) != str:
            if "router" not in name.data:
                return

            if self.config_entry.data["name"] != name.data.get("router"):
                return

            if "script" in name.data:
                name = name.data.get("script")
            else:
                return

        try:
            self.api.run_script(name)
        except ApiEntryNotFound as error:
            _LOGGER.error("Failed to run script: %s", error)

    # ---------------------------
    #   get_capabilities
    # ---------------------------
    def get_capabilities(self):
        """Update Mikrotik data"""
        packages = parse_api(
            data={},
            source=self.api.query("/system/package"),
            key="name",
            vals=[
                {"name": "name"},
                {
                    "name": "enabled",
                    "source": "disabled",
                    "type": "bool",
                    "reverse": True,
                },
            ],
        )

        if 0 < self.major_fw_version < 7:
            if "ppp" in packages:
                self.support_ppp = packages["ppp"]["enabled"]

            if "wireless" in packages:
                self.support_capsman = packages["wireless"]["enabled"]
                self.support_wireless = packages["wireless"]["enabled"]
            else:
                self.support_capsman = False
                self.support_wireless = False

        elif 0 < self.major_fw_version >= 7:
            self.support_ppp = True
            self.support_wireless = True
            if "wifiwave2" in packages and packages["wifiwave2"]["enabled"]:
                self.support_capsman = False
                self._wifimodule = "wifiwave2"
                
            elif "wifi" in packages and packages["wifi"]["enabled"]:
                self.support_capsman = False
                self._wifimodule = "wifi"
                
            elif "wifi-qcom" in packages and packages["wifi-qcom"]["enabled"]:
                self.support_capsman = False
                self._wifimodule = "wifi"
                
            elif "wifi-qcom-ac" in packages and packages["wifi-qcom-ac"]["enabled"]:
                self.support_capsman = False
                self._wifimodule = "wifi"
                
            elif (self.major_fw_version == 7 and self.minor_fw_version >= 13) or self.major_fw_version > 7:
                self.support_capsman = False
                self._wifimodule = "wifi"
                
            else:
                self.support_capsman = True
                self.support_wireless = bool(self.minor_fw_version < 13)
                
            _LOGGER.debug("Mikrotik %s wifi module=%s",
                    self.host,
                    self._wifimodule,
                    )

        if "ups" in packages and packages["ups"]["enabled"]:
            self.support_ups = True

        if "gps" in packages and packages["gps"]["enabled"]:
            self.support_gps = True

    # ---------------------------
    #   async_get_host_hass
    # ---------------------------
    async def async_get_host_hass(self):
        """Get host data from HA entity registry"""
        registry = entity_registry.async_get(self.hass)
        for entity in registry.entities.values():
            if (
                entity.config_entry_id == self.config_entry.entry_id
                and entity.entity_id.startswith("device_tracker.")
            ):
                tmp = entity.unique_id.split("-")
                if tmp[0] != self.name.lower():
                    continue

                if tmp[1] != "host":
                    continue

                if ":" not in tmp[2]:
                    continue

                self.ds["host_hass"][tmp[2].upper()] = entity.original_name

    # ---------------------------
    #   _async_update_data
    # ---------------------------
    async def _async_update_data(self):
        """Update Mikrotik data"""
        delta = datetime.now().replace(microsecond=0) - self.last_hwinfo_update
        if self.api.has_reconnected() or delta.total_seconds() > 60 * 60 * 4:
            await self.hass.async_add_executor_job(self.get_access)

            if self.api.connected():
                await self.hass.async_add_executor_job(self.get_firmware_update)

            if self.api.connected():
                await self.hass.async_add_executor_job(self.get_system_resource)

            if self.api.connected():
                await self.hass.async_add_executor_job(self.get_capabilities)

            if self.api.connected():
                await self.hass.async_add_executor_job(self.get_system_routerboard)

            if self.api.connected() and self.option_sensor_scripts:
                await self.hass.async_add_executor_job(self.get_script)

            if self.api.connected():
                await self.hass.async_add_executor_job(self.get_dhcp_network)

            if self.api.connected():
                await self.hass.async_add_executor_job(self.get_dns)

            if not self.api.connected():
                raise UpdateFailed("Mikrotik Disconnected")

            if self.api.connected():
                self.last_hwinfo_update = datetime.now().replace(microsecond=0)

        await self.hass.async_add_executor_job(self.get_system_resource)

        # if self.api.connected() and "available" not in self.ds["fw-update"]:
        #     await self.hass.async_add_executor_job(self.get_firmware_update)

        if self.api.connected():
            await self.hass.async_add_executor_job(self.get_system_health)

        if self.api.connected():
            await self.hass.async_add_executor_job(self.get_dhcp_client)

        if self.api.connected():
            await self.hass.async_add_executor_job(self.get_interface)

        if self.api.connected() and not self.ds["host_hass"]:
            await self.async_get_host_hass()

        if self.api.connected() and self.support_capsman:
            await self.hass.async_add_executor_job(self.get_capsman_hosts)

        if self.api.connected() and self.support_wireless:
            await self.hass.async_add_executor_job(self.get_wireless)

        if self.api.connected() and self.support_wireless:
            await self.hass.async_add_executor_job(self.get_wireless_hosts)

        if self.api.connected():
            await self.hass.async_add_executor_job(self.get_bridge)

        if self.api.connected():
            await self.hass.async_add_executor_job(self.get_arp)

        if self.api.connected():
            await self.hass.async_add_executor_job(self.get_dhcp)

        if self.api.connected():
            await self.async_process_host()

        if self.api.connected():
            await self.hass.async_add_executor_job(self.process_interface_client)

        if self.api.connected() and self.option_sensor_nat:
            await self.hass.async_add_executor_job(self.get_nat)

        if self.api.connected() and self.option_sensor_kidcontrol:
            await self.hass.async_add_executor_job(self.get_kidcontrol)

        if self.api.connected() and self.option_sensor_mangle:
            await self.hass.async_add_executor_job(self.get_mangle)

        if self.api.connected() and self.option_sensor_filter:
            await self.hass.async_add_executor_job(self.get_filter)

        if self.api.connected() and self.option_sensor_netwatch:
            await self.hass.async_add_executor_job(self.get_netwatch)

        if self.api.connected() and self.support_ppp and self.option_sensor_ppp:
            await self.hass.async_add_executor_job(self.get_ppp)

        if self.api.connected() and self.option_sensor_client_traffic:
            if 0 < self.major_fw_version < 7:
                await self.hass.async_add_executor_job(self.process_accounting)
            elif 0 < self.major_fw_version >= 7:
                await self.hass.async_add_executor_job(self.process_kid_control_devices)

        if self.api.connected() and self.option_sensor_client_captive:
            await self.hass.async_add_executor_job(self.get_captive)

        if self.api.connected() and self.option_sensor_simple_queues:
            await self.hass.async_add_executor_job(self.get_queue)

        if self.api.connected() and self.option_sensor_environment:
            await self.hass.async_add_executor_job(self.get_environment)

        if self.api.connected() and self.support_ups:
            await self.hass.async_add_executor_job(self.get_ups)

        if self.api.connected() and self.support_gps:
            await self.hass.async_add_executor_job(self.get_gps)

        if not self.api.connected():
            raise UpdateFailed("Mikrotik Disconnected")

        # async_dispatcher_send(self.hass, "update_sensors", self)
        return self.ds

    # ---------------------------
    #   get_access
    # ---------------------------
    def get_access(self) -> None:
        """Get access rights from Mikrotik"""
        tmp_user = parse_api(
            data={},
            source=self.api.query("/user"),
            key="name",
            vals=[
                {"name": "name"},
                {"name": "group"},
            ],
        )

        tmp_group = parse_api(
            data={},
            source=self.api.query("/user/group"),
            key="name",
            vals=[
                {"name": "name"},
                {"name": "policy"},
            ],
        )

        self.ds["access"] = tmp_group[
            tmp_user[self.config_entry.data[CONF_USERNAME]]["group"]
        ]["policy"].split(",")

        if not self.accessrights_reported:
            self.accessrights_reported = True
            if (
                "write" not in self.ds["access"]
                or "policy" not in self.ds["access"]
                or "reboot" not in self.ds["access"]
                or "test" not in self.ds["access"]
            ):
                _LOGGER.warning(
                    "Mikrotik %s user %s does not have sufficient access rights. Integration functionality will be limited.",
                    self.host,
                    self.config_entry.data[CONF_USERNAME],
                )

    # ---------------------------
    #   get_interface
    # ---------------------------
    def get_interface(self) -> None:
        """Get all interfaces data from Mikrotik"""
        self.ds["interface"] = parse_api(
            data=self.ds["interface"],
            source=self.api.query("/interface"),
            key="default-name",
            key_secondary="name",
            vals=[
                {"name": "default-name"},
                {"name": ".id"},
                {"name": "name", "default_val": "default-name"},
                {"name": "type", "default": "unknown"},
                {"name": "running", "type": "bool"},
                {
                    "name": "enabled",
                    "source": "disabled",
                    "type": "bool",
                    "reverse": True,
                },
                {"name": "port-mac-address", "source": "mac-address"},
                {"name": "comment"},
                {"name": "last-link-down-time"},
                {"name": "last-link-up-time"},
                {"name": "link-downs"},
                {"name": "tx-queue-drop"},
                {"name": "actual-mtu"},
                {"name": "about", "source": ".about", "default": ""},
                {"name": "rx-current", "source": "rx-byte", "default": 0.0},
                {"name": "tx-current", "source": "tx-byte", "default": 0.0},
            ],
            ensure_vals=[
                {"name": "client-ip-address"},
                {"name": "client-mac-address"},
                {"name": "rx-previous", "default": 0.0},
                {"name": "tx-previous", "default": 0.0},
                {"name": "rx", "default": 0.0},
                {"name": "tx", "default": 0.0},
                {"name": "rx-total", "default": 0.0},
                {"name": "tx-total", "default": 0.0},
            ],
            skip=[
                {"name": "type", "value": "bridge"},
                {"name": "type", "value": "ppp-in"},
                {"name": "type", "value": "pptp-in"},
                {"name": "type", "value": "sstp-in"},
                {"name": "type", "value": "l2tp-in"},
                {"name": "type", "value": "pppoe-in"},
                {"name": "type", "value": "ovpn-in"},
            ],
        )

        if self.option_sensor_port_traffic:
            for uid, vals in self.ds["interface"].items():
                current_tx = vals["tx-current"]
                previous_tx = vals["tx-previous"] or current_tx

                delta_tx = max(0, current_tx - previous_tx)
                self.ds["interface"][uid]["tx"] = round(
                    delta_tx / self.option_scan_interval.seconds
                )
                self.ds["interface"][uid]["tx-previous"] = current_tx

                current_rx = vals["rx-current"]
                previous_rx = vals["rx-previous"] or current_rx

                delta_rx = max(0, current_rx - previous_rx)
                self.ds["interface"][uid]["rx"] = round(
                    delta_rx / self.option_scan_interval.seconds
                )
                self.ds["interface"][uid]["rx-previous"] = current_rx

                self.ds["interface"][uid]["tx-total"] = current_tx
                self.ds["interface"][uid]["rx-total"] = current_rx

        self.ds["interface"] = parse_api(
            data=self.ds["interface"],
            source=self.api.query("/interface/ethernet"),
            key="default-name",
            key_secondary="name",
            vals=[
                {"name": "default-name"},
                {"name": "name", "default_val": "default-name"},
                {"name": "poe-out", "default": "N/A"},
                {"name": "sfp-shutdown-temperature", "default": 0},
            ],
            skip=[
                {"name": "type", "value": "bridge"},
                {"name": "type", "value": "ppp-in"},
                {"name": "type", "value": "pptp-in"},
                {"name": "type", "value": "sstp-in"},
                {"name": "type", "value": "l2tp-in"},
                {"name": "type", "value": "pppoe-in"},
                {"name": "type", "value": "ovpn-in"},
            ],
        )

        # Udpate virtual interfaces
        for uid, vals in self.ds["interface"].items():
            self.ds["interface"][uid]["comment"] = str(
                self.ds["interface"][uid]["comment"]
            )

            if vals["default-name"] == "":
                self.ds["interface"][uid]["default-name"] = vals["name"]
                self.ds["interface"][uid][
                    "port-mac-address"
                ] = f"{vals['port-mac-address']}-{vals['name']}"

            if self.ds["interface"][uid]["type"] == "ether":
                if (
                    "sfp-shutdown-temperature" in vals
                    and vals["sfp-shutdown-temperature"] != ""
                ):
                    self.ds["interface"] = parse_api(
                        data=self.ds["interface"],
                        source=self.api.query(
                            "/interface/ethernet",
                            command="monitor",
                            args={".id": vals[".id"], "once": True},
                        ),
                        key_search="name",
                        vals=[
                            {"name": "status", "default": "unknown"},
                            {"name": "auto-negotiation", "default": "unknown"},
                            {"name": "advertising", "default": "unknown"},
                            {"name": "link-partner-advertising", "default": "unknown"},
                            {"name": "sfp-temperature", "default": 0},
                            {"name": "sfp-supply-voltage", "default": "unknown"},
                            {"name": "sfp-module-present", "default": "unknown"},
                            {"name": "sfp-tx-bias-current", "default": "unknown"},
                            {"name": "sfp-tx-power", "default": "unknown"},
                            {"name": "sfp-rx-power", "default": "unknown"},
                            {"name": "sfp-rx-loss", "default": "unknown"},
                            {"name": "sfp-tx-fault", "default": "unknown"},
                            {"name": "sfp-type", "default": "unknown"},
                            {"name": "sfp-connector-type", "default": "unknown"},
                            {"name": "sfp-vendor-name", "default": "unknown"},
                            {"name": "sfp-vendor-part-number", "default": "unknown"},
                            {"name": "sfp-vendor-revision", "default": "unknown"},
                            {"name": "sfp-vendor-serial", "default": "unknown"},
                            {"name": "sfp-manufacturing-date", "default": "unknown"},
                            {"name": "eeprom-checksum", "default": "unknown"},
                        ],
                    )
                else:
                    self.ds["interface"] = parse_api(
                        data=self.ds["interface"],
                        source=self.api.query(
                            "/interface/ethernet",
                            command="monitor",
                            args={".id": vals[".id"], "once": True},
                        ),
                        key_search="name",
                        vals=[
                            {"name": "status", "default": "unknown"},
                            {"name": "rate", "default": "unknown"},
                            {"name": "full-duplex", "default": "unknown"},
                            {"name": "auto-negotiation", "default": "unknown"},
                        ],
                    )

    # ---------------------------
    #   get_bridge
    # ---------------------------
    def get_bridge(self) -> None:
        """Get system resources data from Mikrotik"""
        self.ds["bridge_host"] = parse_api(
            data=self.ds["bridge_host"],
            source=self.api.query("/interface/bridge/host"),
            key="mac-address",
            vals=[
                {"name": "mac-address"},
                {"name": "interface", "default": "unknown"},
                {"name": "bridge", "default": "unknown"},
                {
                    "name": "enabled",
                    "source": "disabled",
                    "type": "bool",
                    "reverse": True,
                },
            ],
            only=[{"key": "local", "value": False}],
        )

        for uid, vals in self.ds["bridge_host"].items():
            self.ds["bridge"][vals["bridge"]] = True

    # ---------------------------
    #   process_interface_client
    # ---------------------------
    def process_interface_client(self) -> None:
        # Remove data if disabled
        if not self.option_track_iface_clients:
            for uid in self.ds["interface"]:
                self.ds["interface"][uid]["client-ip-address"] = "disabled"
                self.ds["interface"][uid]["client-mac-address"] = "disabled"
            return

        for uid, vals in self.ds["interface"].items():
            self.ds["interface"][uid]["client-ip-address"] = ""
            self.ds["interface"][uid]["client-mac-address"] = ""
            for arp_uid, arp_vals in self.ds["arp"].items():
                if arp_vals["interface"] != vals["name"]:
                    continue

                if self.ds["interface"][uid]["client-ip-address"] == "":
                    self.ds["interface"][uid]["client-ip-address"] = arp_vals["address"]
                else:
                    self.ds["interface"][uid]["client-ip-address"] = "multiple"

                if self.ds["interface"][uid]["client-mac-address"] == "":
                    self.ds["interface"][uid]["client-mac-address"] = arp_vals[
                        "mac-address"
                    ]
                else:
                    self.ds["interface"][uid]["client-mac-address"] = "multiple"

            if self.ds["interface"][uid]["client-ip-address"] == "":
                self.ds["interface"][uid]["client-ip-address"] = "none"

            if self.ds["interface"][uid]["client-mac-address"] == "":
                self.ds["interface"][uid]["client-mac-address"] = "none"

    # ---------------------------
    #   get_nat
    # ---------------------------
    def get_nat(self) -> None:
        """Get NAT data from Mikrotik"""
        self.ds["nat"] = parse_api(
            data=self.ds["nat"],
            source=self.api.query("/ip/firewall/nat"),
            key=".id",
            vals=[
                {"name": ".id"},
                {"name": "chain", "default": "unknown"},
                {"name": "action", "default": "unknown"},
                {"name": "protocol", "default": "any"},
                {"name": "dst-port", "default": "any"},
                {"name": "in-interface", "default": "any"},
                {"name": "out-interface", "default": "any"},
                {"name": "to-addresses"},
                {"name": "to-ports", "default": "any"},
                {"name": "comment"},
                {
                    "name": "enabled",
                    "source": "disabled",
                    "type": "bool",
                    "reverse": True,
                },
            ],
            val_proc=[
                [
                    {"name": "uniq-id"},
                    {"action": "combine"},
                    {"key": "chain"},
                    {"text": ","},
                    {"key": "action"},
                    {"text": ","},
                    {"key": "protocol"},
                    {"text": ","},
                    {"key": "in-interface"},
                    {"text": ":"},
                    {"key": "dst-port"},
                    {"text": "-"},
                    {"key": "out-interface"},
                    {"text": ":"},
                    {"key": "to-addresses"},
                    {"text": ":"},
                    {"key": "to-ports"},
                ],
                [
                    {"name": "name"},
                    {"action": "combine"},
                    {"key": "protocol"},
                    {"text": ":"},
                    {"key": "dst-port"},
                ],
            ],
            only=[{"key": "action", "value": "dst-nat"}],
        )

        # Remove duplicate NAT entries to prevent crash
        nat_uniq = {}
        nat_del = {}
        for uid in self.ds["nat"]:
            self.ds["nat"][uid]["comment"] = str(self.ds["nat"][uid]["comment"])

            tmp_name = self.ds["nat"][uid]["uniq-id"]
            if tmp_name not in nat_uniq:
                nat_uniq[tmp_name] = uid
            else:
                nat_del[uid] = 1
                nat_del[nat_uniq[tmp_name]] = 1

        for uid in nat_del:
            if self.ds["nat"][uid]["uniq-id"] not in self.nat_removed:
                self.nat_removed[self.ds["nat"][uid]["uniq-id"]] = 1
                _LOGGER.error(
                    "Mikrotik %s duplicate NAT rule %s, entity will be unavailable.",
                    self.host,
                    self.ds["nat"][uid]["name"],
                )

            del self.ds["nat"][uid]

    # ---------------------------
    #   get_mangle
    # ---------------------------
    def get_mangle(self) -> None:
        """Get Mangle data from Mikrotik"""
        self.ds["mangle"] = parse_api(
            data=self.ds["mangle"],
            source=self.api.query("/ip/firewall/mangle"),
            key=".id",
            vals=[
                {"name": ".id"},
                {"name": "chain"},
                {"name": "action"},
                {"name": "comment"},
                {"name": "address-list"},
                {"name": "passthrough", "type": "bool", "default": False},
                {"name": "protocol", "default": "any"},
                {"name": "src-address", "default": "any"},
                {"name": "src-port", "default": "any"},
                {"name": "dst-address", "default": "any"},
                {"name": "dst-port", "default": "any"},
                {"name": "src-address-list", "default": "any"},
                {"name": "dst-address-list", "default": "any"},
                {
                    "name": "enabled",
                    "source": "disabled",
                    "type": "bool",
                    "reverse": True,
                },
            ],
            val_proc=[
                [
                    {"name": "uniq-id"},
                    {"action": "combine"},
                    {"key": "chain"},
                    {"text": ","},
                    {"key": "action"},
                    {"text": ","},
                    {"key": "protocol"},
                    {"text": ","},
                    {"key": "src-address"},
                    {"text": ":"},
                    {"key": "src-port"},
                    {"text": "-"},
                    {"key": "dst-address"},
                    {"text": ":"},
                    {"key": "dst-port"},
                    {"text": ","},
                    {"key": "src-address-list"},
                    {"text": "-"},
                    {"key": "dst-address-list"},
                ],
                [
                    {"name": "name"},
                    {"action": "combine"},
                    {"key": "action"},
                    {"text": ","},
                    {"key": "protocol"},
                    {"text": ":"},
                    {"key": "dst-port"},
                ],
            ],
            skip=[
                {"name": "dynamic", "value": True},
                {"name": "action", "value": "jump"},
            ],
        )

        # Remove duplicate Mangle entries to prevent crash
        mangle_uniq = {}
        mangle_del = {}
        for uid in self.ds["mangle"]:
            self.ds["mangle"][uid]["comment"] = str(self.ds["mangle"][uid]["comment"])

            tmp_name = self.ds["mangle"][uid]["uniq-id"]
            if tmp_name not in mangle_uniq:
                mangle_uniq[tmp_name] = uid
            else:
                mangle_del[uid] = 1
                mangle_del[mangle_uniq[tmp_name]] = 1

        for uid in mangle_del:
            if self.ds["mangle"][uid]["uniq-id"] not in self.mangle_removed:
                self.mangle_removed[self.ds["mangle"][uid]["uniq-id"]] = 1
                _LOGGER.error(
                    "Mikrotik %s duplicate Mangle rule %s, entity will be unavailable.",
                    self.host,
                    self.ds["mangle"][uid]["name"],
                )

            del self.ds["mangle"][uid]

    # ---------------------------
    #   get_filter
    # ---------------------------
    def get_filter(self) -> None:
        """Get Filter data from Mikrotik"""
        self.ds["filter"] = parse_api(
            data=self.ds["filter"],
            source=self.api.query("/ip/firewall/filter"),
            key=".id",
            vals=[
                {"name": ".id"},
                {"name": "chain"},
                {"name": "action"},
                {"name": "comment"},
                {"name": "address-list"},
                {"name": "protocol", "default": "any"},
                {"name": "in-interface", "default": "any"},
                {"name": "in-interface-list", "default": "any"},
                {"name": "out-interface", "default": "any"},
                {"name": "out-interface-list", "default": "any"},
                {"name": "src-address", "default": "any"},
                {"name": "src-address-list", "default": "any"},
                {"name": "src-port", "default": "any"},
                {"name": "dst-address", "default": "any"},
                {"name": "dst-address-list", "default": "any"},
                {"name": "dst-port", "default": "any"},
                {"name": "layer7-protocol", "default": "any"},
                {"name": "connection-state", "default": "any"},
                {"name": "tcp-flags", "default": "any"},
                {
                    "name": "enabled",
                    "source": "disabled",
                    "type": "bool",
                    "reverse": True,
                    "default": True,
                },
            ],
            val_proc=[
                [
                    {"name": "uniq-id"},
                    {"action": "combine"},
                    {"key": "chain"},
                    {"text": ","},
                    {"key": "action"},
                    {"text": ","},
                    {"key": "protocol"},
                    {"text": ","},
                    {"key": "layer7-protocol"},
                    {"text": ","},
                    {"key": "in-interface"},
                    {"text": ","},
                    {"key": "in-interface-list"},
                    {"text": ":"},
                    {"key": "src-address"},
                    {"text": ","},
                    {"key": "src-address-list"},
                    {"text": ":"},
                    {"key": "src-port"},
                    {"text": "-"},
                    {"key": "out-interface"},
                    {"text": ","},
                    {"key": "out-interface-list"},
                    {"text": ":"},
                    {"key": "dst-address"},
                    {"text": ","},
                    {"key": "dst-address-list"},
                    {"text": ":"},
                    {"key": "dst-port"},
                ],
                [
                    {"name": "name"},
                    {"action": "combine"},
                    {"key": "action"},
                    {"text": ","},
                    {"key": "protocol"},
                    {"text": ":"},
                    {"key": "dst-port"},
                ],
            ],
            skip=[
                {"name": "dynamic", "value": True},
                {"name": "action", "value": "jump"},
            ],
        )

        # Remove duplicate filter entries to prevent crash
        filter_uniq = {}
        filter_del = {}
        for uid in self.ds["filter"]:
            self.ds["filter"][uid]["comment"] = str(self.ds["filter"][uid]["comment"])

            tmp_name = self.ds["filter"][uid]["uniq-id"]
            if tmp_name not in filter_uniq:
                filter_uniq[tmp_name] = uid
            else:
                filter_del[uid] = 1
                filter_del[filter_uniq[tmp_name]] = 1

        for uid in filter_del:
            if self.ds["filter"][uid]["uniq-id"] not in self.filter_removed:
                self.filter_removed[self.ds["filter"][uid]["uniq-id"]] = 1
                _LOGGER.error(
                    "Mikrotik %s duplicate Filter rule %s (ID %s), entity will be unavailable.",
                    self.host,
                    self.ds["filter"][uid]["name"],
                    self.ds["filter"][uid][".id"],
                )

            del self.ds["filter"][uid]

    # ---------------------------
    #   get_kidcontrol
    # ---------------------------
    def get_kidcontrol(self) -> None:
        """Get Kid-control data from Mikrotik"""
        self.ds["kid-control"] = parse_api(
            data=self.ds["kid-control"],
            source=self.api.query("/ip/kid-control"),
            key="name",
            vals=[
                {"name": "name"},
                {"name": "rate-limit"},
                {"name": "mon", "default": "None"},
                {"name": "tue", "default": "None"},
                {"name": "wed", "default": "None"},
                {"name": "thu", "default": "None"},
                {"name": "fri", "default": "None"},
                {"name": "sat", "default": "None"},
                {"name": "sun", "default": "None"},
                {"name": "comment"},
                {"name": "blocked", "type": "bool", "default": False},
                {"name": "paused", "type": "bool", "reverse": True},
                {
                    "name": "enabled",
                    "source": "disabled",
                    "type": "bool",
                    "reverse": True,
                },
            ],
        )

        for uid in self.ds["kid-control"]:
            self.ds["kid-control"][uid]["comment"] = str(
                self.ds["kid-control"][uid]["comment"]
            )

    # ---------------------------
    #   get_ppp
    # ---------------------------
    def get_ppp(self) -> None:
        """Get PPP data from Mikrotik"""
        self.ds["ppp_secret"] = parse_api(
            data=self.ds["ppp_secret"],
            source=self.api.query("/ppp/secret"),
            key="name",
            vals=[
                {"name": "name"},
                {"name": "service"},
                {"name": "profile"},
                {"name": "comment"},
                {
                    "name": "enabled",
                    "source": "disabled",
                    "type": "bool",
                    "reverse": True,
                },
            ],
            ensure_vals=[
                {"name": "caller-id", "default": ""},
                {"name": "address", "default": ""},
                {"name": "encoding", "default": ""},
                {"name": "connected", "default": False},
            ],
        )

        self.ds["ppp_active"] = parse_api(
            data={},
            source=self.api.query("/ppp/active"),
            key="name",
            vals=[
                {"name": "name"},
                {"name": "service"},
                {"name": "caller-id"},
                {"name": "address"},
                {"name": "encoding"},
            ],
        )

        for uid in self.ds["ppp_secret"]:
            self.ds["ppp_secret"][uid]["comment"] = str(
                self.ds["ppp_secret"][uid]["comment"]
            )

            if self.ds["ppp_secret"][uid]["name"] in self.ds["ppp_active"]:
                self.ds["ppp_secret"][uid]["connected"] = True
                self.ds["ppp_secret"][uid]["caller-id"] = self.ds["ppp_active"][uid][
                    "caller-id"
                ]
                self.ds["ppp_secret"][uid]["address"] = self.ds["ppp_active"][uid][
                    "address"
                ]
                self.ds["ppp_secret"][uid]["encoding"] = self.ds["ppp_active"][uid][
                    "encoding"
                ]
            else:
                self.ds["ppp_secret"][uid]["connected"] = False
                self.ds["ppp_secret"][uid]["caller-id"] = "not connected"
                self.ds["ppp_secret"][uid]["address"] = "not connected"
                self.ds["ppp_secret"][uid]["encoding"] = "not connected"

    # ---------------------------
    #   get_netwatch
    # ---------------------------
    def get_netwatch(self) -> None:
        """Get netwatch data from Mikrotik"""
        self.ds["netwatch"] = parse_api(
            data=self.ds["netwatch"],
            source=self.api.query("/tool/netwatch"),
            key="host",
            vals=[
                {"name": "host"},
                {"name": "type"},
                {"name": "interval"},
                {"name": "port"},
                {"name": "http-codes"},
                {"name": "status", "type": "bool", "default": "unknown"},
                {"name": "comment"},
                {
                    "name": "enabled",
                    "source": "disabled",
                    "type": "bool",
                    "reverse": True,
                },
            ],
        )

    # ---------------------------
    #   get_system_routerboard
    # ---------------------------
    def get_system_routerboard(self) -> None:
        """Get routerboard data from Mikrotik"""
        if self.ds["resource"]["board-name"].startswith("x86") or self.ds["resource"][
            "board-name"
        ].startswith("CHR"):
            self.ds["routerboard"]["routerboard"] = False
            self.ds["routerboard"]["model"] = self.ds["resource"]["board-name"]
            self.ds["routerboard"]["serial-number"] = "N/A"
        else:
            self.ds["routerboard"] = parse_api(
                data=self.ds["routerboard"],
                source=self.api.query("/system/routerboard"),
                vals=[
                    {"name": "routerboard", "type": "bool"},
                    {"name": "model", "default": "unknown"},
                    {"name": "serial-number", "default": "unknown"},
                    {"name": "current-firmware", "default": "unknown"},
                    {"name": "upgrade-firmware", "default": "unknown"},
                ],
            )

            if (
                "write" not in self.ds["access"]
                or "policy" not in self.ds["access"]
                or "reboot" not in self.ds["access"]
            ):
                self.ds["routerboard"].pop("current-firmware")
                self.ds["routerboard"].pop("upgrade-firmware")

    # ---------------------------
    #   get_system_health
    # ---------------------------
    def get_system_health(self) -> None:
        """Get routerboard data from Mikrotik"""
        if (
            "write" not in self.ds["access"]
            or "policy" not in self.ds["access"]
            or "reboot" not in self.ds["access"]
        ):
            return

        if 0 < self.major_fw_version < 7:
            self.ds["health"] = parse_api(
                data=self.ds["health"],
                source=self.api.query("/system/health"),
                vals=[
                    {"name": "temperature", "default": 0},
                    {"name": "voltage", "default": 0},
                    {"name": "cpu-temperature", "default": 0},
                    {"name": "power-consumption", "default": 0},
                    {"name": "board-temperature1", "default": 0},
                    {"name": "phy-temperature", "default": 0},
                    {"name": "fan1-speed", "default": 0},
                    {"name": "fan2-speed", "default": 0},
                ],
            )
        elif 0 < self.major_fw_version >= 7:
            self.ds["health7"] = parse_api(
                data=self.ds["health7"],
                source=self.api.query("/system/health"),
                key="name",
                vals=[
                    {"name": "value", "default": "unknown"},
                ],
            )
            for uid, vals in self.ds["health7"].items():
                self.ds["health"][uid] = vals["value"]

    # ---------------------------
    #   get_system_resource
    # ---------------------------
    def get_system_resource(self) -> None:
        """Get system resources data from Mikrotik"""
        tmp_rebootcheck = 0
        if "uptime_epoch" in self.ds["resource"]:
            tmp_rebootcheck = self.ds["resource"]["uptime_epoch"]

        self.ds["resource"] = parse_api(
            data=self.ds["resource"],
            source=self.api.query("/system/resource"),
            vals=[
                {"name": "platform", "default": "unknown"},
                {"name": "board-name", "default": "unknown"},
                {"name": "version", "default": "unknown"},
                {"name": "uptime_str", "source": "uptime", "default": "unknown"},
                {"name": "cpu-load", "default": "unknown"},
                {"name": "free-memory", "default": 0},
                {"name": "total-memory", "default": 0},
                {"name": "free-hdd-space", "default": 0},
                {"name": "total-hdd-space", "default": 0},
            ],
            ensure_vals=[
                {"name": "uptime", "default": 0},
                {"name": "uptime_epoch", "default": 0},
                {"name": "clients_wired", "default": 0},
                {"name": "clients_wireless", "default": 0},
                {"name": "captive_authorized", "default": 0},
            ],
        )

        tmp_uptime = 0
        tmp = re.split(r"(\d+)[s]", self.ds["resource"]["uptime_str"])
        if len(tmp) > 1:
            tmp_uptime += int(tmp[1])
        tmp = re.split(r"(\d+)[m]", self.ds["resource"]["uptime_str"])
        if len(tmp) > 1:
            tmp_uptime += int(tmp[1]) * 60
        tmp = re.split(r"(\d+)[h]", self.ds["resource"]["uptime_str"])
        if len(tmp) > 1:
            tmp_uptime += int(tmp[1]) * 3600
        tmp = re.split(r"(\d+)[d]", self.ds["resource"]["uptime_str"])
        if len(tmp) > 1:
            tmp_uptime += int(tmp[1]) * 86400
        tmp = re.split(r"(\d+)[w]", self.ds["resource"]["uptime_str"])
        if len(tmp) > 1:
            tmp_uptime += int(tmp[1]) * 604800

        self.ds["resource"]["uptime_epoch"] = tmp_uptime
        now = datetime.now().replace(microsecond=0)
        uptime_tm = datetime.timestamp(now - timedelta(seconds=tmp_uptime))
        update_uptime = False
        if not self.ds["resource"]["uptime"]:
            update_uptime = True
        else:
            uptime_old = datetime.timestamp(self.ds["resource"]["uptime"])
            if uptime_tm > uptime_old + 10:
                update_uptime = True

        if update_uptime:
            self.ds["resource"]["uptime"] = utc_from_timestamp(uptime_tm)

        if self.ds["resource"]["total-memory"] > 0:
            self.ds["resource"]["memory-usage"] = round(
                (
                    (
                        self.ds["resource"]["total-memory"]
                        - self.ds["resource"]["free-memory"]
                    )
                    / self.ds["resource"]["total-memory"]
                )
                * 100
            )
        else:
            self.ds["resource"]["memory-usage"] = "unknown"

        if self.ds["resource"]["total-hdd-space"] > 0:
            self.ds["resource"]["hdd-usage"] = round(
                (
                    (
                        self.ds["resource"]["total-hdd-space"]
                        - self.ds["resource"]["free-hdd-space"]
                    )
                    / self.ds["resource"]["total-hdd-space"]
                )
                * 100
            )
        else:
            self.ds["resource"]["hdd-usage"] = "unknown"

        if (
            "uptime_epoch" in self.ds["resource"]
            and 0 < tmp_rebootcheck < self.ds["resource"]["uptime_epoch"]
        ):
            self.get_firmware_update()

    # ---------------------------
    #   get_firmware_update
    # ---------------------------
    def get_firmware_update(self) -> None:
        """Check for firmware update on Mikrotik"""
        if (
            "write" not in self.ds["access"]
            or "policy" not in self.ds["access"]
            or "reboot" not in self.ds["access"]
        ):
            return

        self.execute(
            "/system/package/update", "check-for-updates", None, None, {"duration": 10}
        )
        self.ds["fw-update"] = parse_api(
            data=self.ds["fw-update"],
            source=self.api.query("/system/package/update"),
            vals=[
                {"name": "status"},
                {"name": "channel", "default": "unknown"},
                {"name": "installed-version", "default": "unknown"},
                {"name": "latest-version", "default": "unknown"},
            ],
        )

        if "status" in self.ds["fw-update"]:
            self.ds["fw-update"]["available"] = (
                self.ds["fw-update"]["status"] == "New version is available"
            )

        else:
            self.ds["fw-update"]["available"] = False

        if self.ds["fw-update"]["installed-version"] != "unknown":
            try:
                full_version = self.ds["fw-update"].get("installed-version")
                split_end = min(len(full_version),4)
                version = re.sub("[^0-9\.]", "", full_version[0:split_end])
                self.major_fw_version = int(version.split(".")[0])
                self.minor_fw_version = int(version.split(".")[1])
                _LOGGER.debug(
                    "Mikrotik %s FW version major=%s minor=%s (%s)",
                    self.host,
                    self.major_fw_version,
                    self.minor_fw_version,
                    full_version
                )
            except Exception:
                _LOGGER.error(
                    "Mikrotik %s unable to determine major FW version (%s).",
                    self.host,
                    full_version,
                )

    # ---------------------------
    #   get_ups
    # ---------------------------
    def get_ups(self) -> None:
        """Get UPS info from Mikrotik"""
        self.ds["ups"] = parse_api(
            data=self.ds["ups"],
            source=self.api.query("/system/ups"),
            vals=[
                {"name": "name", "default": "unknown"},
                {"name": "offline-time", "default": "unknown"},
                {"name": "min-runtime", "default": "unknown"},
                {"name": "alarm-setting", "default": "unknown"},
                {"name": "model", "default": "unknown"},
                {"name": "serial", "default": "unknown"},
                {"name": "manufacture-date", "default": "unknown"},
                {"name": "nominal-battery-voltage", "default": "unknown"},
                {
                    "name": "enabled",
                    "source": "disabled",
                    "type": "bool",
                    "reverse": True,
                },
            ],
            ensure_vals=[
                {"name": "on-line", "type": "bool"},
                {"name": "runtime-left", "default": "unknown"},
                {"name": "battery-charge", "default": 0},
                {"name": "battery-voltage", "default": 0.0},
                {"name": "line-voltage", "default": 0},
                {"name": "load", "default": 0},
                {"name": "hid-self-test", "default": "unknown"},
            ],
        )
        if self.ds["ups"]["enabled"]:
            self.ds["ups"] = parse_api(
                data=self.ds["ups"],
                source=self.api.query(
                    "/system/ups",
                    command="monitor",
                    args={".id": 0, "once": True},
                ),
                vals=[
                    {"name": "on-line", "type": "bool"},
                    {"name": "runtime-left", "default": 0},
                    {"name": "battery-charge", "default": 0},
                    {"name": "battery-voltage", "default": 0.0},
                    {"name": "line-voltage", "default": 0},
                    {"name": "load", "default": 0},
                    {"name": "hid-self-test", "default": "unknown"},
                ],
            )

    # ---------------------------
    #   get_gps
    # ---------------------------
    def get_gps(self) -> None:
        """Get GPS data from Mikrotik"""
        self.ds["gps"] = parse_api(
            data=self.ds["gps"],
            source=self.api.query(
                "/system/gps",
                command="monitor",
                args={"once": True},
            ),
            vals=[
                {"name": "valid", "type": "bool"},
                {"name": "latitude", "default": "unknown"},
                {"name": "longitude", "default": "unknown"},
                {"name": "altitude", "default": "unknown"},
                {"name": "speed", "default": "unknown"},
                {"name": "destination-bearing", "default": "unknown"},
                {"name": "true-bearing", "default": "unknown"},
                {"name": "magnetic-bearing", "default": "unknown"},
                {"name": "satellites", "default": 0},
                {"name": "fix-quality", "default": 0},
                {"name": "horizontal-dilution", "default": "unknown"},
            ],
        )

    # ---------------------------
    #   get_script
    # ---------------------------
    def get_script(self) -> None:
        """Get list of all scripts from Mikrotik"""
        self.ds["script"] = parse_api(
            data=self.ds["script"],
            source=self.api.query("/system/script"),
            key="name",
            vals=[
                {"name": "name"},
                {"name": "last-started", "default": "unknown"},
                {"name": "run-count", "default": "unknown"},
            ],
        )

    # ---------------------------
    #   get_environment
    # ---------------------------
    def get_environment(self) -> None:
        """Get list of all environment variables from Mikrotik"""
        self.ds["environment"] = parse_api(
            data=self.ds["environment"],
            source=self.api.query("/system/script/environment"),
            key="name",
            vals=[
                {"name": "name"},
                {"name": "value"},
            ],
        )

    # ---------------------------
    #   get_captive
    # ---------------------------
    def get_captive(self) -> None:
        """Get list of all environment variables from Mikrotik"""
        self.ds["hostspot_host"] = parse_api(
            data={},
            source=self.api.query("/ip/hotspot/host"),
            key="mac-address",
            vals=[
                {"name": "mac-address"},
                {"name": "authorized", "type": "bool"},
                {"name": "bypassed", "type": "bool"},
            ],
        )

        auth_hosts = sum(
            1
            for uid in self.ds["hostspot_host"]
            if self.ds["hostspot_host"][uid]["authorized"]
        )
        self.ds["resource"]["captive_authorized"] = auth_hosts

    # ---------------------------
    #   get_queue
    # ---------------------------
    def get_queue(self) -> None:
        """Get Queue data from Mikrotik"""
        self.ds["queue"] = parse_api(
            data=self.ds["queue"],
            source=self.api.query("/queue/simple"),
            key="name",
            vals=[
                {"name": ".id"},
                {"name": "name", "default": "unknown"},
                {"name": "target", "default": "unknown"},
                {"name": "rate", "default": "0/0"},
                {"name": "max-limit", "default": "0/0"},
                {"name": "limit-at", "default": "0/0"},
                {"name": "burst-limit", "default": "0/0"},
                {"name": "burst-threshold", "default": "0/0"},
                {"name": "burst-time", "default": "0s/0s"},
                {"name": "packet-marks", "default": "none"},
                {"name": "parent", "default": "none"},
                {"name": "comment"},
                {
                    "name": "enabled",
                    "source": "disabled",
                    "type": "bool",
                    "reverse": True,
                },
            ],
        )

        for uid, vals in self.ds["queue"].items():
            self.ds["queue"][uid]["comment"] = str(self.ds["queue"][uid]["comment"])

            upload_max_limit_bps, download_max_limit_bps = [
                int(x) for x in vals["max-limit"].split("/")
            ]
            self.ds["queue"][uid]["upload-max-limit"] = f"{upload_max_limit_bps} bps"
            self.ds["queue"][uid][
                "download-max-limit"
            ] = f"{download_max_limit_bps} bps"

            upload_rate_bps, download_rate_bps = [
                int(x) for x in vals["rate"].split("/")
            ]
            self.ds["queue"][uid]["upload-rate"] = f"{upload_rate_bps} bps"
            self.ds["queue"][uid]["download-rate"] = f"{download_rate_bps} bps"

            upload_limit_at_bps, download_limit_at_bps = [
                int(x) for x in vals["limit-at"].split("/")
            ]
            self.ds["queue"][uid]["upload-limit-at"] = f"{upload_limit_at_bps} bps"
            self.ds["queue"][uid]["download-limit-at"] = f"{download_limit_at_bps} bps"

            upload_burst_limit_bps, download_burst_limit_bps = [
                int(x) for x in vals["burst-limit"].split("/")
            ]
            self.ds["queue"][uid][
                "upload-burst-limit"
            ] = f"{upload_burst_limit_bps} bps"
            self.ds["queue"][uid][
                "download-burst-limit"
            ] = f"{download_burst_limit_bps} bps"

            upload_burst_threshold_bps, download_burst_threshold_bps = [
                int(x) for x in vals["burst-threshold"].split("/")
            ]
            self.ds["queue"][uid][
                "upload-burst-threshold"
            ] = f"{upload_burst_threshold_bps} bps"
            self.ds["queue"][uid][
                "download-burst-threshold"
            ] = f"{download_burst_threshold_bps} bps"

            upload_burst_time, download_burst_time = vals["burst-time"].split("/")
            self.ds["queue"][uid]["upload-burst-time"] = upload_burst_time
            self.ds["queue"][uid]["download-burst-time"] = download_burst_time

    # ---------------------------
    #   get_arp
    # ---------------------------
    def get_arp(self) -> None:
        """Get ARP data from Mikrotik"""
        self.ds["arp"] = parse_api(
            data=self.ds["arp"],
            source=self.api.query("/ip/arp"),
            key="mac-address",
            vals=[{"name": "mac-address"}, {"name": "address"}, {"name": "interface"}],
            ensure_vals=[{"name": "bridge", "default": ""}],
        )

        for uid, vals in self.ds["arp"].items():
            if vals["interface"] in self.ds["bridge"] and uid in self.ds["bridge_host"]:
                self.ds["arp"][uid]["bridge"] = vals["interface"]
                self.ds["arp"][uid]["interface"] = self.ds["bridge_host"][uid][
                    "interface"
                ]

        if self.ds["dhcp-client"]:
            to_remove = [
                uid
                for uid, vals in self.ds["arp"].items()
                if vals["interface"] in self.ds["dhcp-client"]
            ]

            for uid in to_remove:
                self.ds["arp"].pop(uid)

    # ---------------------------
    #   get_dns
    # ---------------------------
    def get_dns(self) -> None:
        """Get static DNS data from Mikrotik"""
        self.ds["dns"] = parse_api(
            data=self.ds["dns"],
            source=self.api.query("/ip/dns/static"),
            key="name",
            vals=[{"name": "name"}, {"name": "address"}, {"name": "comment"}],
        )

        for uid, vals in self.ds["dns"].items():
            self.ds["dns"][uid]["comment"] = str(self.ds["dns"][uid]["comment"])

    # ---------------------------
    #   get_dhcp
    # ---------------------------
    def get_dhcp(self) -> None:
        """Get DHCP data from Mikrotik"""
        self.ds["dhcp"] = parse_api(
            data=self.ds["dhcp"],
            source=self.api.query("/ip/dhcp-server/lease"),
            key="mac-address",
            vals=[
                {"name": "mac-address"},
                {"name": "active-mac-address", "default": "unknown"},
                {"name": "address", "default": "unknown"},
                {"name": "active-address", "default": "unknown"},
                {"name": "host-name", "default": "unknown"},
                {"name": "status", "default": "unknown"},
                {"name": "last-seen", "default": "unknown"},
                {"name": "server", "default": "unknown"},
                {"name": "comment", "default": ""},
                {
                    "name": "enabled",
                    "source": "disabled",
                    "type": "bool",
                    "reverse": True,
                },
            ],
            ensure_vals=[{"name": "interface", "default": "unknown"}],
        )

        dhcpserver_query = False
        for uid in self.ds["dhcp"]:
            self.ds["dhcp"][uid]["comment"] = str(self.ds["dhcp"][uid]["comment"])

            # is_valid_ip
            if self.ds["dhcp"][uid]["address"] != "unknown":
                if not is_valid_ip(self.ds["dhcp"][uid]["address"]):
                    self.ds["dhcp"][uid]["address"] = "unknown"

                if self.ds["dhcp"][uid]["active-address"] not in [
                    self.ds["dhcp"][uid]["address"],
                    "unknown",
                ]:
                    self.ds["dhcp"][uid]["address"] = self.ds["dhcp"][uid][
                        "active-address"
                    ]

                if (
                    self.ds["dhcp"][uid]["mac-address"]
                    != self.ds["dhcp"][uid]["active-mac-address"]
                    != "unknown"
                ):
                    self.ds["dhcp"][uid]["mac-address"] = self.ds["dhcp"][uid][
                        "active-mac-address"
                    ]

            if (
                not dhcpserver_query
                and self.ds["dhcp"][uid]["server"] not in self.ds["dhcp-server"]
            ):
                self.get_dhcp_server()
                dhcpserver_query = True

            if self.ds["dhcp"][uid]["server"] in self.ds["dhcp-server"]:
                self.ds["dhcp"][uid]["interface"] = self.ds["dhcp-server"][
                    self.ds["dhcp"][uid]["server"]
                ]["interface"]
            elif uid in self.ds["arp"]:
                if self.ds["arp"][uid]["bridge"] != "unknown":
                    self.ds["dhcp"][uid]["interface"] = self.ds["arp"][uid]["bridge"]
                else:
                    self.ds["dhcp"][uid]["interface"] = self.ds["arp"][uid]["interface"]

    # ---------------------------
    #   get_dhcp_server
    # ---------------------------
    def get_dhcp_server(self) -> None:
        """Get DHCP server data from Mikrotik"""
        self.ds["dhcp-server"] = parse_api(
            data=self.ds["dhcp-server"],
            source=self.api.query("/ip/dhcp-server"),
            key="name",
            vals=[
                {"name": "name"},
                {"name": "interface", "default": "unknown"},
            ],
        )

    # ---------------------------
    #   get_dhcp_client
    # ---------------------------
    def get_dhcp_client(self) -> None:
        """Get DHCP client data from Mikrotik"""
        self.ds["dhcp-client"] = parse_api(
            data=self.ds["dhcp-client"],
            source=self.api.query("/ip/dhcp-client"),
            key="interface",
            vals=[
                {"name": "interface", "default": "unknown"},
                {"name": "status", "default": "unknown"},
            ],
        )

    # ---------------------------
    #   get_dhcp_network
    # ---------------------------
    def get_dhcp_network(self) -> None:
        """Get DHCP network data from Mikrotik"""
        self.ds["dhcp-network"] = parse_api(
            data=self.ds["dhcp-network"],
            source=self.api.query("/ip/dhcp-server/network"),
            key="address",
            vals=[
                {"name": "address"},
                {"name": "gateway", "default": ""},
                {"name": "netmask", "default": ""},
                {"name": "dns-server", "default": ""},
                {"name": "domain", "default": ""},
            ],
            ensure_vals=[{"name": "address"}, {"name": "IPv4Network", "default": ""}],
        )

        for uid, vals in self.ds["dhcp-network"].items():
            if vals["IPv4Network"] == "":
                self.ds["dhcp-network"][uid]["IPv4Network"] = IPv4Network(
                    vals["address"]
                )

    # ---------------------------
    #   get_capsman_hosts
    # ---------------------------
    def get_capsman_hosts(self) -> None:
        """Get CAPS-MAN hosts data from Mikrotik"""
        
        if self.major_fw_version > 7 or (self.major_fw_version == 7 and self.minor_fw_version >= 13):
            registration_path = "/interface/wifi/registration-table"
            
        else:
            registration_path= "/caps-man/registration-table"
            
        self.ds["capsman_hosts"] = parse_api(
            data={},
            source=self.api.query(registration_path),
            key="mac-address",
            vals=[
                {"name": "mac-address"},
                {"name": "interface", "default": "unknown"},
                {"name": "ssid", "default": "unknown"},
            ],
        )

    # ---------------------------
    #   get_wireless
    # ---------------------------
    def get_wireless(self) -> None:
        """Get wireless data from Mikrotik"""

        self.ds["wireless"] = parse_api(
            data=self.ds["wireless"],
            source=self.api.query(f"/interface/{self._wifimodule}"),
            key="name",
            vals=[
                {"name": "master-interface", "default": ""},
                {"name": "mac-address", "default": "unknown"},
                {"name": "ssid", "default": "unknown"},
                {"name": "mode", "default": "unknown"},
                {"name": "radio-name", "default": "unknown"},
                {"name": "interface-type", "default": "unknown"},
                {"name": "country", "default": "unknown"},
                {"name": "installation", "default": "unknown"},
                {"name": "antenna-gain", "default": "unknown"},
                {"name": "frequency", "default": "unknown"},
                {"name": "band", "default": "unknown"},
                {"name": "channel-width", "default": "unknown"},
                {"name": "secondary-frequency", "default": "unknown"},
                {"name": "wireless-protocol", "default": "unknown"},
                {"name": "rate-set", "default": "unknown"},
                {"name": "distance", "default": "unknown"},
                {"name": "tx-power-mode", "default": "unknown"},
                {"name": "vlan-id", "default": "unknown"},
                {"name": "wds-mode", "default": "unknown"},
                {"name": "wds-default-bridge", "default": "unknown"},
                {"name": "bridge-mode", "default": "unknown"},
                {"name": "hide-ssid", "type": "bool"},
                {"name": "running", "type": "bool"},
                {"name": "disabled", "type": "bool"},
            ],
        )

        for uid in self.ds["wireless"]:
            if self.ds["wireless"][uid]["master-interface"]:
                for tmp in self.ds["wireless"][uid]:
                    if self.ds["wireless"][uid][tmp] == "unknown":
                        self.ds["wireless"][uid][tmp] = self.ds["wireless"][
                            self.ds["wireless"][uid]["master-interface"]
                        ][tmp]

            if uid in self.ds["interface"]:
                for tmp in self.ds["wireless"][uid]:
                    self.ds["interface"][uid][tmp] = self.ds["wireless"][uid][tmp]

    # ---------------------------
    #   get_wireless_hosts
    # ---------------------------
    def get_wireless_hosts(self) -> None:
        """Get wireless hosts data from Mikrotik"""
        self.ds["wireless_hosts"] = parse_api(
            data={},
            source=self.api.query(f"/interface/{self._wifimodule}/registration-table"),
            key="mac-address",
            vals=[
                {"name": "mac-address"},
                {"name": "interface", "default": "unknown"},
                {"name": "ap", "type": "bool"},
                {"name": "uptime"},
            ],
        )

    # ---------------------------
    #   async_process_host
    # ---------------------------
    async def async_process_host(self) -> None:
        """Get host tracking data"""
        # Add hosts from CAPS-MAN
        capsman_detected = {}
        if self.support_capsman:
            for uid, vals in self.ds["capsman_hosts"].items():
                if uid not in self.ds["host"]:
                    self.ds["host"][uid] = {"source": "capsman"}
                elif self.ds["host"][uid]["source"] != "capsman":
                    continue

                capsman_detected[uid] = True
                self.ds["host"][uid]["available"] = True
                self.ds["host"][uid]["last-seen"] = utcnow()
                for key in ["mac-address", "interface"]:
                    self.ds["host"][uid][key] = vals[key]

        # Add hosts from wireless
        wireless_detected = {}
        if self.support_wireless:
            for uid, vals in self.ds["wireless_hosts"].items():
                if vals["ap"]:
                    continue

                if uid not in self.ds["host"]:
                    self.ds["host"][uid] = {"source": "wireless"}
                elif self.ds["host"][uid]["source"] != "wireless":
                    continue

                wireless_detected[uid] = True
                self.ds["host"][uid]["available"] = True
                self.ds["host"][uid]["last-seen"] = utcnow()
                for key in ["mac-address", "interface"]:
                    self.ds["host"][uid][key] = vals[key]

        # Add hosts from DHCP
        for uid, vals in self.ds["dhcp"].items():
            if not vals["enabled"]:
                continue

            if uid not in self.ds["host"]:
                self.ds["host"][uid] = {"source": "dhcp"}
            elif self.ds["host"][uid]["source"] != "dhcp":
                continue

            for key in ["address", "mac-address", "interface"]:
                self.ds["host"][uid][key] = vals[key]

        # Add hosts from ARP
        for uid, vals in self.ds["arp"].items():
            if uid not in self.ds["host"]:
                self.ds["host"][uid] = {"source": "arp"}
            elif self.ds["host"][uid]["source"] != "arp":
                continue

            for key in ["address", "mac-address", "interface"]:
                self.ds["host"][uid][key] = vals[key]

        # Add restored hosts from hass registry
        if not self.host_hass_recovered:
            self.host_hass_recovered = True
            for uid in self.ds["host_hass"]:
                if uid not in self.ds["host"]:
                    self.ds["host"][uid] = {"source": "restored"}
                    self.ds["host"][uid]["mac-address"] = uid
                    self.ds["host"][uid]["host-name"] = self.ds["host_hass"][uid]

        for uid, vals in self.ds["host"].items():
            # Add missing default values
            for key, default in zip(
                [
                    "address",
                    "mac-address",
                    "interface",
                    "host-name",
                    "manufacturer",
                    "last-seen",
                    "available",
                ],
                ["unknown", "unknown", "unknown", "unknown", "detect", False, False],
            ):
                if key not in self.ds["host"][uid]:
                    self.ds["host"][uid][key] = default

        # if not self.host_tracking_initialized:
        #     await self.async_ping_tracked_hosts()

        # Process hosts
        self.ds["resource"]["clients_wired"] = 0
        self.ds["resource"]["clients_wireless"] = 0
        for uid, vals in self.ds["host"].items():
            # Captive portal data
            if self.option_sensor_client_captive:
                if uid in self.ds["hostspot_host"]:
                    self.ds["host"][uid]["authorized"] = self.ds["hostspot_host"][uid][
                        "authorized"
                    ]
                    self.ds["host"][uid]["bypassed"] = self.ds["hostspot_host"][uid][
                        "bypassed"
                    ]
                elif "authorized" in self.ds["host"][uid]:
                    del self.ds["host"][uid]["authorized"]
                    del self.ds["host"][uid]["bypassed"]

            # CAPS-MAN availability
            if vals["source"] == "capsman" and uid not in capsman_detected:
                self.ds["host"][uid]["available"] = False

            # Wireless availability
            if vals["source"] == "wireless" and uid not in wireless_detected:
                self.ds["host"][uid]["available"] = False

            # Update IP and interface (DHCP/returned host)
            if (
                uid in self.ds["dhcp"]
                and self.ds["dhcp"][uid]["enabled"]
                and "." in self.ds["dhcp"][uid]["address"]
            ):
                if self.ds["dhcp"][uid]["address"] != self.ds["host"][uid]["address"]:
                    self.ds["host"][uid]["address"] = self.ds["dhcp"][uid]["address"]
                    if vals["source"] not in ["capsman", "wireless"]:
                        self.ds["host"][uid]["source"] = "dhcp"
                        self.ds["host"][uid]["interface"] = self.ds["dhcp"][uid][
                            "interface"
                        ]

            elif (
                uid in self.ds["arp"]
                and "." in self.ds["arp"][uid]["address"]
                and self.ds["arp"][uid]["address"] != self.ds["host"][uid]["address"]
            ):
                self.ds["host"][uid]["address"] = self.ds["arp"][uid]["address"]
                if vals["source"] not in ["capsman", "wireless"]:
                    self.ds["host"][uid]["source"] = "arp"
                    self.ds["host"][uid]["interface"] = self.ds["arp"][uid]["interface"]

            if vals["host-name"] == "unknown":
                # Resolve hostname from static DNS
                if vals["address"] != "unknown":
                    for dns_uid, dns_vals in self.ds["dns"].items():
                        if dns_vals["address"] == vals["address"]:
                            if dns_vals["comment"].split("#", 1)[0] != "":
                                self.ds["host"][uid]["host-name"] = dns_vals[
                                    "comment"
                                ].split("#", 1)[0]
                            elif (
                                uid in self.ds["dhcp"]
                                and self.ds["dhcp"][uid]["enabled"]
                                and self.ds["dhcp"][uid]["comment"].split("#", 1)[0]
                                != ""
                            ):
                                # Override name if DHCP comment exists
                                self.ds["host"][uid]["host-name"] = self.ds["dhcp"][
                                    uid
                                ]["comment"].split("#", 1)[0]
                            else:
                                self.ds["host"][uid]["host-name"] = dns_vals[
                                    "name"
                                ].split(".")[0]
                            break

                if self.ds["host"][uid]["host-name"] == "unknown":
                    # Resolve hostname from DHCP comment
                    if (
                        uid in self.ds["dhcp"]
                        and self.ds["dhcp"][uid]["enabled"]
                        and self.ds["dhcp"][uid]["comment"].split("#", 1)[0] != ""
                    ):
                        self.ds["host"][uid]["host-name"] = self.ds["dhcp"][uid][
                            "comment"
                        ].split("#", 1)[0]
                    # Resolve hostname from DHCP hostname
                    elif (
                        uid in self.ds["dhcp"]
                        and self.ds["dhcp"][uid]["enabled"]
                        and self.ds["dhcp"][uid]["host-name"] != "unknown"
                    ):
                        self.ds["host"][uid]["host-name"] = self.ds["dhcp"][uid][
                            "host-name"
                        ]
                    # Fallback to mac address for hostname
                    else:
                        self.ds["host"][uid]["host-name"] = uid

            # Resolve manufacturer
            if vals["manufacturer"] == "detect" and vals["mac-address"] != "unknown":
                try:
                    self.ds["host"][uid][
                        "manufacturer"
                    ] = await self.async_mac_lookup.lookup(vals["mac-address"])
                except Exception:
                    self.ds["host"][uid]["manufacturer"] = ""

            if vals["manufacturer"] == "detect":
                self.ds["host"][uid]["manufacturer"] = ""

            # Count hosts
            if self.ds["host"][uid]["available"]:
                if vals["source"] in ["capsman", "wireless"]:
                    self.ds["resource"]["clients_wireless"] += 1
                else:
                    self.ds["resource"]["clients_wired"] += 1

    # ---------------------------
    #   process_accounting
    # ---------------------------
    def process_accounting(self) -> None:
        """Get Accounting data from Mikrotik"""
        # Check if accounting and account-local-traffic is enabled
        (
            accounting_enabled,
            local_traffic_enabled,
        ) = self.api.is_accounting_and_local_traffic_enabled()

        # Build missing hosts from main hosts dict
        for uid, vals in self.ds["host"].items():
            if uid not in self.ds["client_traffic"]:
                self.ds["client_traffic"][uid] = {
                    "address": vals["address"],
                    "mac-address": vals["mac-address"],
                    "host-name": vals["host-name"],
                    "available": False,
                    "local_accounting": False,
                }

        _LOGGER.debug(
            f"Working with {len(self.ds['client_traffic'])} accounting devices"
        )

        # Build temp accounting values dict with ip address as key
        tmp_accounting_values = {
            vals["address"]: {
                "wan-tx": 0,
                "wan-rx": 0,
                "lan-tx": 0,
                "lan-rx": 0,
            }
            for uid, vals in self.ds["client_traffic"].items()
        }

        time_diff = self.api.take_client_traffic_snapshot(True)
        if time_diff:
            accounting_data = parse_api(
                data={},
                source=self.api.query("/ip/accounting/snapshot"),
                key=".id",
                vals=[
                    {"name": ".id"},
                    {"name": "src-address"},
                    {"name": "dst-address"},
                    {"name": "bytes", "default": 0},
                ],
            )

            threshold = self.api.query("/ip/accounting")[0].get("threshold")
            entry_count = len(accounting_data)

            if entry_count == threshold:
                _LOGGER.warning(
                    f"Accounting entries count reached the threshold of {threshold}!"
                    " Some entries were not saved by Mikrotik so accounting calculation won't be correct."
                    " Consider shortening update interval or"
                    " increasing the accounting threshold value in Mikrotik."
                )
            elif entry_count > threshold * 0.9:
                _LOGGER.info(
                    f"Accounting entries count ({entry_count} reached 90% of the threshold,"
                    f" currently set to {threshold}! Consider shortening update interval or"
                    " increasing the accounting threshold value in Mikrotik."
                )

            for item in accounting_data.values():
                source_ip = str(item.get("src-address")).strip()
                destination_ip = str(item.get("dst-address")).strip()
                bits_count = int(str(item.get("bytes")).strip())

                if self._address_part_of_local_network(
                    source_ip
                ) and self._address_part_of_local_network(destination_ip):
                    # LAN TX/RX
                    if source_ip in tmp_accounting_values:
                        tmp_accounting_values[source_ip]["lan-tx"] += bits_count
                    if destination_ip in tmp_accounting_values:
                        tmp_accounting_values[destination_ip]["lan-rx"] += bits_count
                elif self._address_part_of_local_network(
                    source_ip
                ) and not self._address_part_of_local_network(destination_ip):
                    # WAN TX
                    if source_ip in tmp_accounting_values:
                        tmp_accounting_values[source_ip]["wan-tx"] += bits_count
                elif (
                    not self._address_part_of_local_network(source_ip)
                    and self._address_part_of_local_network(destination_ip)
                    and destination_ip in tmp_accounting_values
                ):
                    # WAN RX
                    tmp_accounting_values[destination_ip]["wan-rx"] += bits_count

        # Calculate real throughput and transform it to appropriate unit
        # Also handle availability of accounting and local_accounting from Mikrotik
        for addr, vals in tmp_accounting_values.items():
            uid = self._get_accounting_uid_by_ip(addr)
            if not uid:
                _LOGGER.warning(
                    f"Address {addr} not found in accounting data, skipping update"
                )
                continue

            self.ds["client_traffic"][uid]["available"] = accounting_enabled
            self.ds["client_traffic"][uid]["local_accounting"] = local_traffic_enabled

            if not accounting_enabled:
                # Skip calculation for WAN and LAN if accounting is disabled
                continue

            self.ds["client_traffic"][uid]["wan-tx"] = (
                round(vals["wan-tx"] / time_diff) if vals["wan-tx"] else 0.0
            )
            self.ds["client_traffic"][uid]["wan-rx"] = (
                round(vals["wan-rx"] / time_diff) if vals["wan-rx"] else 0.0
            )

            if not local_traffic_enabled:
                # Skip calculation for LAN if LAN accounting is disabled
                continue

            self.ds["client_traffic"][uid]["lan-tx"] = (
                round(vals["lan-tx"] / time_diff) if vals["lan-tx"] else 0.0
            )
            self.ds["client_traffic"][uid]["lan-rx"] = (
                round(vals["lan-rx"] / time_diff) if vals["lan-rx"] else 0.0
            )

    # ---------------------------
    #   _address_part_of_local_network
    # ---------------------------
    def _address_part_of_local_network(self, address) -> bool:
        address = ip_address(address)
        for vals in self.ds["dhcp-network"].values():
            if address in vals["IPv4Network"]:
                return True
        return False

    # ---------------------------
    #   _get_accounting_uid_by_ip
    # ---------------------------
    def _get_accounting_uid_by_ip(self, requested_ip):
        for mac, vals in self.ds["client_traffic"].items():
            if vals.get("address") is requested_ip:
                return mac
        return None

    # ---------------------------
    #   _get_iface_from_entry
    # ---------------------------
    def _get_iface_from_entry(self, entry):
        """Get interface default-name using name from interface dict"""
        uid = None
        for ifacename in self.ds["interface"]:
            if self.ds["interface"][ifacename]["name"] == entry["interface"]:
                uid = ifacename
                break

        return uid

    # ---------------------------
    #   process_kid_control
    # ---------------------------
    def process_kid_control_devices(self) -> None:
        """Get Kid Control Device data from Mikrotik"""

        # Build missing hosts from main hosts dict
        for uid, vals in self.ds["host"].items():
            if uid not in self.ds["client_traffic"]:
                self.ds["client_traffic"][uid] = {
                    "address": vals["address"],
                    "mac-address": vals["mac-address"],
                    "host-name": vals["host-name"],
                    "previous-bytes-up": 0.0,
                    "previous-bytes-down": 0.0,
                    "tx": 0.0,
                    "rx": 0.0,
                    "available": False,
                    "local_accounting": False,
                }

        _LOGGER.debug(
            f"Working with {len(self.ds['client_traffic'])} kid control devices"
        )

        kid_control_devices_data = parse_api(
            data={},
            source=self.api.query("/ip/kid-control/device"),
            key="mac-address",
            vals=[
                {"name": "mac-address"},
                {"name": "bytes-down"},
                {"name": "bytes-up"},
                {
                    "name": "enabled",
                    "source": "disabled",
                    "type": "bool",
                    "reverse": True,
                },
            ],
        )

        time_diff = self.api.take_client_traffic_snapshot(False)

        if not kid_control_devices_data:
            if "kid-control-devices" not in self.notified_flags:
                _LOGGER.error(
                    "No kid control devices found on your Mikrotik device, make sure kid-control feature is configured"
                )
                self.notified_flags.append("kid-control-devices")
            return
        elif "kid-control-devices" in self.notified_flags:
            self.notified_flags.remove("kid-control-devices")

        for uid, vals in kid_control_devices_data.items():
            if uid not in self.ds["client_traffic"]:
                _LOGGER.debug(f"Skipping unknown device {uid}")
                continue

            self.ds["client_traffic"][uid]["available"] = vals["enabled"]

            current_tx = vals["bytes-up"]
            previous_tx = self.ds["client_traffic"][uid]["previous-bytes-up"]
            if time_diff:
                delta_tx = max(0, current_tx - previous_tx)
                self.ds["client_traffic"][uid]["tx"] = round(delta_tx / time_diff)
            self.ds["client_traffic"][uid]["previous-bytes-up"] = current_tx

            current_rx = vals["bytes-down"]
            previous_rx = self.ds["client_traffic"][uid]["previous-bytes-down"]
            if time_diff:
                delta_rx = max(0, current_rx - previous_rx)
                self.ds["client_traffic"][uid]["rx"] = round(delta_rx / time_diff)
            self.ds["client_traffic"][uid]["previous-bytes-down"] = current_rx


File: /custom_components\mikrotik_router\device_tracker.py
"""Support for the Mikrotik Router device tracker."""
from __future__ import annotations

from logging import getLogger
from collections.abc import Mapping
from datetime import timedelta
from typing import Any, Callable

from homeassistant.components.device_tracker.config_entry import ScannerEntity
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant, callback
from homeassistant.const import STATE_NOT_HOME
from homeassistant.helpers import (
    entity_platform as ep,
    entity_registry as er,
)
from homeassistant.helpers.dispatcher import async_dispatcher_connect
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.util import slugify
from homeassistant.util.dt import utcnow

from homeassistant.components.device_tracker.const import SourceType

from .device_tracker_types import SENSOR_TYPES, SENSOR_SERVICES
from .coordinator import MikrotikCoordinator
from .entity import _skip_sensor, MikrotikEntity
from .helper import format_attribute
from .const import (
    DOMAIN,
    CONF_TRACK_HOSTS,
    DEFAULT_TRACK_HOSTS,
    CONF_TRACK_HOSTS_TIMEOUT,
    DEFAULT_TRACK_HOST_TIMEOUT,
)

_LOGGER = getLogger(__name__)


async def async_add_entities(
    hass: HomeAssistant, config_entry: ConfigEntry, dispatcher: dict[str, Callable]
):
    """Add entities."""
    platform = ep.async_get_current_platform()
    services = platform.platform.SENSOR_SERVICES
    descriptions = platform.platform.SENSOR_TYPES

    for service in services:
        platform.async_register_entity_service(service[0], service[1], service[2])

    @callback
    async def async_update_controller(coordinator):
        """Update the values of the controller."""
        if coordinator.data is None:
            return

        async def async_check_exist(obj, coordinator, uid: None) -> None:
            """Check entity exists."""
            entity_registry = er.async_get(hass)
            if uid:
                unique_id = f"{obj._inst.lower()}-{obj.entity_description.key}-{slugify(str(obj._data[obj.entity_description.data_reference]).lower())}"
            else:
                unique_id = f"{obj._inst.lower()}-{obj.entity_description.key}"

            entity_id = entity_registry.async_get_entity_id(
                platform.domain, DOMAIN, unique_id
            )
            entity = entity_registry.async_get(entity_id)
            if entity is None or (
                (entity_id not in platform.entities) and (entity.disabled is False)
            ):
                _LOGGER.debug("Add entity %s", entity_id)
                await platform.async_add_entities([obj])

        for entity_description in descriptions:
            data = coordinator.data[entity_description.data_path]
            if not entity_description.data_reference:
                if data.get(entity_description.data_attribute) is None:
                    continue
                obj = dispatcher[entity_description.func](
                    coordinator, entity_description
                )
                await async_check_exist(obj, coordinator, None)
            else:
                for uid in data:
                    if _skip_sensor(config_entry, entity_description, data, uid):
                        continue
                    obj = dispatcher[entity_description.func](
                        coordinator, entity_description, uid
                    )
                    await async_check_exist(obj, coordinator, uid)

    await async_update_controller(
        hass.data[DOMAIN][config_entry.entry_id].tracker_coordinator
    )

    unsub = async_dispatcher_connect(hass, "update_sensors", async_update_controller)
    config_entry.async_on_unload(unsub)


# ---------------------------
#   async_setup_entry
# ---------------------------
async def async_setup_entry(
    hass: HomeAssistant,
    config_entry: ConfigEntry,
    _async_add_entities: AddEntitiesCallback,
) -> None:
    """Set up entry for component"""
    dispatcher = {
        "MikrotikDeviceTracker": MikrotikDeviceTracker,
        "MikrotikHostDeviceTracker": MikrotikHostDeviceTracker,
    }
    await async_add_entities(hass, config_entry, dispatcher)


# ---------------------------
#   MikrotikDeviceTracker
# ---------------------------
class MikrotikDeviceTracker(MikrotikEntity, ScannerEntity):
    """Representation of a device tracker."""

    def __init__(
        self,
        coordinator: MikrotikCoordinator,
        entity_description,
        uid: str | None = None,
    ):
        """Initialize entity"""
        super().__init__(coordinator, entity_description, uid)
        self._attr_name = None

    @property
    def ip_address(self) -> str:
        """Return the primary ip address of the device."""
        return self._data["address"] if "address" in self._data else None

    @property
    def mac_address(self) -> str:
        """Return the mac address of the device."""
        if self.entity_description.data_reference in self._data:
            return self._data[self.entity_description.data_reference]

        return ""

    @property
    def hostname(self) -> str:
        """Return hostname of the device."""
        if self.entity_description.data_name in self._data:
            return self._data[self.entity_description.data_name]

        return ""

    @property
    def is_connected(self) -> bool:
        """Return true if device is connected."""
        return self._data[self.entity_description.data_attribute]

    @property
    def source_type(self) -> str:
        """Return the source type of the port."""
        return SourceType.ROUTER


# ---------------------------
#   MikrotikHostDeviceTracker
# ---------------------------
class MikrotikHostDeviceTracker(MikrotikDeviceTracker):
    """Representation of a network device."""

    @property
    def option_track_network_hosts(self):
        """Config entry option to not track ARP."""
        return self._config_entry.options.get(CONF_TRACK_HOSTS, DEFAULT_TRACK_HOSTS)

    @property
    def option_track_network_hosts_timeout(self):
        """Config entry option scan interval."""
        track_network_hosts_timeout = self._config_entry.options.get(
            CONF_TRACK_HOSTS_TIMEOUT, DEFAULT_TRACK_HOST_TIMEOUT
        )
        return timedelta(seconds=track_network_hosts_timeout)

    @property
    def is_connected(self) -> bool:
        """Return true if the host is connected to the network."""
        if not self.option_track_network_hosts:
            return False

        if self._data["source"] in ["capsman", "wireless"]:
            return self._data[self.entity_description.data_attribute]

        return bool(
            self._data["last-seen"]
            and utcnow() - self._data["last-seen"]
            < self.option_track_network_hosts_timeout
        )

    @property
    def icon(self) -> str:
        """Return the icon."""
        if self._data["source"] in ["capsman", "wireless"]:
            if self._data[self.entity_description.data_attribute]:
                return self.entity_description.icon_enabled
            else:
                return self.entity_description.icon_disabled

        if (
            self._data["last-seen"]
            and (utcnow() - self._data["last-seen"])
            < self.option_track_network_hosts_timeout
        ):
            return self.entity_description.icon_enabled
        return self.entity_description.icon_disabled

    @property
    def state(self) -> str:
        """Return the state of the device."""
        return self.coordinator.option_zone if self.is_connected else STATE_NOT_HOME

    @property
    def extra_state_attributes(self) -> Mapping[str, Any]:
        """Return the state attributes."""
        attributes = super().extra_state_attributes
        if self.is_connected:
            attributes[format_attribute("last-seen")] = "Now"

        if not attributes[format_attribute("last-seen")]:
            attributes[format_attribute("last-seen")] = "Unknown"

        return attributes


File: /custom_components\mikrotik_router\device_tracker_types.py
"""Definitions for Mikrotik Router device tracker entities."""
from __future__ import annotations

from dataclasses import dataclass, field
from typing import List

from homeassistant.helpers.device_registry import CONNECTION_NETWORK_MAC
from homeassistant.components.switch import (
    SwitchEntityDescription,
)

DEVICE_ATTRIBUTES_HOST = [
    "interface",
    "source",
    "authorized",
    "bypassed",
    "last-seen",
]


@dataclass
class MikrotikDeviceTrackerEntityDescription(SwitchEntityDescription):
    """Class describing mikrotik entities."""

    key: str | None = None
    name: str | None = None
    device_class = None
    icon_enabled: str | None = None
    icon_disabled: str | None = None
    ha_group: str | None = None
    ha_connection: str | None = None
    ha_connection_value: str | None = None
    data_path: str | None = None
    data_attribute: str = "available"
    data_name: str | None = None
    data_name_comment: bool = False
    data_uid: str | None = None
    data_reference: str | None = None
    data_attributes_list: List = field(default_factory=lambda: [])
    func: str = "MikrotikDeviceTracker"


SENSOR_TYPES: tuple[MikrotikDeviceTrackerEntityDescription, ...] = (
    MikrotikDeviceTrackerEntityDescription(
        key="host",
        name="",
        icon_enabled="mdi:lan-connect",
        icon_disabled="mdi:lan-disconnect",
        ha_group="",
        ha_connection=CONNECTION_NETWORK_MAC,
        ha_connection_value="data__mac-address",
        data_path="host",
        data_name="host-name",
        data_uid="mac-address",
        data_reference="mac-address",
        data_attributes_list=DEVICE_ATTRIBUTES_HOST,
        func="MikrotikHostDeviceTracker",
    ),
)

SENSOR_SERVICES = {}


File: /custom_components\mikrotik_router\diagnostics.py
"""Diagnostics support for Mikrotik Router."""
from __future__ import annotations
from typing import Any
from homeassistant.components.diagnostics import async_redact_data
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from .const import DOMAIN, TO_REDACT


async def async_get_config_entry_diagnostics(
    hass: HomeAssistant, config_entry: ConfigEntry
) -> dict[str, Any]:
    """Return diagnostics for a config entry."""
    data_coordinator = hass.data[DOMAIN][config_entry.entry_id].data_coordinator
    tracker_coordinator = hass.data[DOMAIN][config_entry.entry_id].data_coordinator

    return {
        "entry": {
            "data": async_redact_data(config_entry.data, TO_REDACT),
            "options": async_redact_data(config_entry.options, TO_REDACT),
        },
        "data": async_redact_data(data_coordinator.data, TO_REDACT),
        "tracker": async_redact_data(tracker_coordinator.data, TO_REDACT),
    }


File: /custom_components\mikrotik_router\entity.py
"""Mikrotik HA shared entity model"""
from __future__ import annotations

from collections.abc import Mapping
from logging import getLogger
from typing import Any, Callable, TypeVar

from homeassistant.config_entries import ConfigEntry
from homeassistant.const import ATTR_ATTRIBUTION, CONF_NAME, CONF_HOST
from homeassistant.core import HomeAssistant, callback
from homeassistant.helpers import (
    entity_platform as ep,
    entity_registry as er,
)
from homeassistant.helpers.dispatcher import async_dispatcher_connect
from homeassistant.helpers.entity import DeviceInfo, Entity
from homeassistant.helpers.update_coordinator import CoordinatorEntity
from homeassistant.util import slugify

from .const import (
    DOMAIN,
    ATTRIBUTION,
    CONF_SENSOR_PORT_TRAFFIC,
    DEFAULT_SENSOR_PORT_TRAFFIC,
    CONF_TRACK_HOSTS,
    DEFAULT_TRACK_HOSTS,
    CONF_SENSOR_PORT_TRACKER,
    DEFAULT_SENSOR_PORT_TRACKER,
    CONF_SENSOR_NETWATCH_TRACKER,
    DEFAULT_SENSOR_NETWATCH_TRACKER,
)
from .coordinator import MikrotikCoordinator, MikrotikTrackerCoordinator
from .helper import format_attribute

_LOGGER = getLogger(__name__)


def _skip_sensor(config_entry, entity_description, data, uid) -> bool:
    # Sensors
    if (
        entity_description.func == "MikrotikInterfaceTrafficSensor"
        and not config_entry.options.get(
            CONF_SENSOR_PORT_TRAFFIC, DEFAULT_SENSOR_PORT_TRAFFIC
        )
    ):
        return True

    if (
        entity_description.func == "MikrotikInterfaceTrafficSensor"
        and data[uid]["type"] == "bridge"
    ):
        return True

    if (
        entity_description.data_path == "client_traffic"
        and entity_description.data_attribute not in data[uid].keys()
    ):
        return True

    # Binary sensors
    if (
        entity_description.func == "MikrotikPortBinarySensor"
        and data[uid]["type"] == "wlan"
    ):
        return True

    if (
        entity_description.func == "MikrotikPortBinarySensor"
        and not config_entry.options.get(
            CONF_SENSOR_PORT_TRACKER, DEFAULT_SENSOR_PORT_TRACKER
        )
    ):
        return True

    if entity_description.data_path == "netwatch" and not config_entry.options.get(
        CONF_SENSOR_NETWATCH_TRACKER, DEFAULT_SENSOR_NETWATCH_TRACKER
    ):
        return True

    # Device Tracker
    if (
        # Skip if host tracking is disabled
        entity_description.func == "MikrotikHostDeviceTracker"
        and not config_entry.options.get(CONF_TRACK_HOSTS, DEFAULT_TRACK_HOSTS)
    ):
        return True

    return False


# ---------------------------
#   async_add_entities
# ---------------------------
async def async_add_entities(
    hass: HomeAssistant, config_entry: ConfigEntry, dispatcher: dict[str, Callable]
):
    """Add entities."""
    platform = ep.async_get_current_platform()
    services = platform.platform.SENSOR_SERVICES
    descriptions = platform.platform.SENSOR_TYPES

    for service in services:
        platform.async_register_entity_service(service[0], service[1], service[2])

    @callback
    async def async_update_controller(coordinator):
        """Update the values of the controller."""

        async def async_check_exist(obj, coordinator, uid: None) -> None:
            """Check entity exists."""
            entity_registry = er.async_get(hass)
            if uid:
                unique_id = f"{obj._inst.lower()}-{obj.entity_description.key}-{slugify(str(obj._data[obj.entity_description.data_reference]).lower())}"
            else:
                unique_id = f"{obj._inst.lower()}-{obj.entity_description.key}"

            entity_id = entity_registry.async_get_entity_id(
                platform.domain, DOMAIN, unique_id
            )
            entity = entity_registry.async_get(entity_id)
            if entity is None or (
                (entity_id not in platform.entities) and (entity.disabled is False)
            ):
                _LOGGER.debug("Add entity %s", entity_id)
                await platform.async_add_entities([obj])

        for entity_description in descriptions:
            data = coordinator.data[entity_description.data_path]
            if not entity_description.data_reference:
                if data.get(entity_description.data_attribute) is None:
                    continue
                obj = dispatcher[entity_description.func](
                    coordinator, entity_description
                )
                await async_check_exist(obj, coordinator, None)
            else:
                for uid in data:
                    if _skip_sensor(config_entry, entity_description, data, uid):
                        continue
                    obj = dispatcher[entity_description.func](
                        coordinator, entity_description, uid
                    )
                    await async_check_exist(obj, coordinator, uid)

    await async_update_controller(
        hass.data[DOMAIN][config_entry.entry_id].data_coordinator
    )

    unsub = async_dispatcher_connect(hass, "update_sensors", async_update_controller)
    config_entry.async_on_unload(unsub)


_MikrotikCoordinatorT = TypeVar(
    "_MikrotikCoordinatorT",
    bound=MikrotikCoordinator | MikrotikTrackerCoordinator,
)


# ---------------------------
#   MikrotikEntity
# ---------------------------
class MikrotikEntity(CoordinatorEntity[_MikrotikCoordinatorT], Entity):
    """Define entity"""

    _attr_has_entity_name = True

    def __init__(
        self,
        coordinator: MikrotikCoordinator,
        entity_description,
        uid: str | None = None,
    ):
        """Initialize entity"""
        super().__init__(coordinator)
        self.entity_description = entity_description
        self._inst = coordinator.config_entry.data[CONF_NAME]
        self._config_entry = self.coordinator.config_entry
        self._attr_extra_state_attributes = {ATTR_ATTRIBUTION: ATTRIBUTION}
        self._uid = uid
        self._data = coordinator.data[self.entity_description.data_path]
        if self._uid:
            self._data = coordinator.data[self.entity_description.data_path][self._uid]

        self._attr_name = self.custom_name

    @callback
    def _handle_coordinator_update(self) -> None:
        self._data = self.coordinator.data[self.entity_description.data_path]
        if self._uid:
            self._data = self.coordinator.data[self.entity_description.data_path][
                self._uid
            ]
        super()._handle_coordinator_update()

    @property
    def custom_name(self) -> str:
        """Return the name for this entity"""
        if not self._uid:
            if self.entity_description.data_name_comment and self._data["comment"]:
                return f"{self._data['comment']}"

            return f"{self.entity_description.name}"

        if self.entity_description.data_name_comment and self._data["comment"]:
            return f"{self._data['comment']}"

        if self.entity_description.name:
            if (
                self._data[self.entity_description.data_reference]
                == self._data[self.entity_description.data_name]
            ):
                return f"{self.entity_description.name}"

            return f"{self._data[self.entity_description.data_name]} {self.entity_description.name}"

        return f"{self._data[self.entity_description.data_name]}"

    @property
    def unique_id(self) -> str:
        """Return a unique id for this entity"""
        if self._uid:
            return f"{self._inst.lower()}-{self.entity_description.key}-{slugify(str(self._data[self.entity_description.data_reference]).lower())}"
        else:
            return f"{self._inst.lower()}-{self.entity_description.key}"

    # @property
    # def available(self) -> bool:
    #     """Return if controller is available"""
    #     return self.coordinator.connected()

    @property
    def device_info(self) -> DeviceInfo:
        """Return a description for device registry."""
        dev_connection = DOMAIN
        dev_connection_value = self.entity_description.data_reference
        dev_group = self.entity_description.ha_group
        if self.entity_description.ha_group == "System":
            dev_group = self.coordinator.data["resource"]["board-name"]
            dev_connection_value = self.coordinator.data["routerboard"]["serial-number"]

        if self.entity_description.ha_group.startswith("data__"):
            dev_group = self.entity_description.ha_group[6:]
            if dev_group in self._data:
                dev_group = self._data[dev_group]
                dev_connection_value = dev_group

        if self.entity_description.ha_connection:
            dev_connection = self.entity_description.ha_connection

        if self.entity_description.ha_connection_value:
            dev_connection_value = self.entity_description.ha_connection_value
            if dev_connection_value.startswith("data__"):
                dev_connection_value = dev_connection_value[6:]
                dev_connection_value = self._data[dev_connection_value]

        if self.entity_description.ha_group == "System":
            return DeviceInfo(
                connections={(dev_connection, f"{dev_connection_value}")},
                identifiers={(dev_connection, f"{dev_connection_value}")},
                name=f"{self._inst} {dev_group}",
                model=f"{self.coordinator.data['resource']['board-name']}",
                manufacturer=f"{self.coordinator.data['resource']['platform']}",
                sw_version=f"{self.coordinator.data['resource']['version']}",
                configuration_url=f"http://{self.coordinator.config_entry.data[CONF_HOST]}",
            )
        elif "mac-address" in self.entity_description.data_reference:
            dev_group = self._data[self.entity_description.data_name]
            dev_manufacturer = ""
            if dev_connection_value in self.coordinator.data["host"]:
                dev_group = self.coordinator.data["host"][dev_connection_value][
                    "host-name"
                ]
                dev_manufacturer = self.coordinator.data["host"][dev_connection_value][
                    "manufacturer"
                ]

            return DeviceInfo(
                connections={(dev_connection, f"{dev_connection_value}")},
                default_name=f"{dev_group}",
                default_manufacturer=f"{dev_manufacturer}",
                via_device=(
                    DOMAIN,
                    f"{self.coordinator.data['routerboard']['serial-number']}",
                ),
            )
        else:
            return DeviceInfo(
                connections={(dev_connection, f"{dev_connection_value}")},
                default_name=f"{self._inst} {dev_group}",
                default_model=f"{self.coordinator.data['resource']['board-name']}",
                default_manufacturer=f"{self.coordinator.data['resource']['platform']}",
                via_device=(
                    DOMAIN,
                    f"{self.coordinator.data['routerboard']['serial-number']}",
                ),
            )

    @property
    def extra_state_attributes(self) -> Mapping[str, Any]:
        """Return the state attributes."""
        attributes = super().extra_state_attributes
        for variable in self.entity_description.data_attributes_list:
            if variable in self._data:
                attributes[format_attribute(variable)] = self._data[variable]

        return attributes

    async def start(self):
        """Dummy run function"""
        raise NotImplementedError()

    async def stop(self):
        """Dummy stop function"""
        raise NotImplementedError()

    async def restart(self):
        """Dummy restart function"""
        raise NotImplementedError()

    async def reload(self):
        """Dummy reload function"""
        raise NotImplementedError()


File: /custom_components\mikrotik_router\exceptions.py
"""Exceptions for Mikrotik Router."""


class ApiEntryNotFound(Exception):
    """Api entry not found."""


File: /custom_components\mikrotik_router\helper.py
"""Helper functions for Mikrotik Router."""


# ---------------------------
#   format_attribute
# ---------------------------
def format_attribute(attr):
    res = attr.replace("-", "_")
    res = res.replace(" ", "_")
    res = res.lower()
    return res


# ---------------------------
#   format_value
# ---------------------------
def format_value(res):
    res = res.replace("dhcp", "DHCP")
    res = res.replace("dns", "DNS")
    res = res.replace("capsman", "CAPsMAN")
    res = res.replace("wireless", "Wireless")
    res = res.replace("restored", "Restored")
    return res


File: /custom_components\mikrotik_router\manifest.json
{
    "domain": "mikrotik_router",
    "name": "Mikrotik Router",
    "config_flow": true,
    "iot_class": "local_polling",
    "documentation": "https://github.com/tomaae/homeassistant-mikrotik_router",
    "issue_tracker": "https://github.com/tomaae/homeassistant-mikrotik_router/issues",
    "dependencies": [],
    "requirements": [
        "librouteros>=3.4.1",
        "mac-vendor-lookup>=0.1.12"
    ],
    "codeowners": [
        "@tomaae"
    ],
    "version": "0.0.0"
}

File: /custom_components\mikrotik_router\mikrotikapi.py
"""Mikrotik API for Mikrotik Router."""

import logging
import ssl
from time import time
from threading import Lock
from voluptuous import Optional
from .const import (
    DEFAULT_LOGIN_METHOD,
    DEFAULT_ENCODING,
)

import librouteros

_LOGGER = logging.getLogger(__name__)


# ---------------------------
#   MikrotikAPI
# ---------------------------
class MikrotikAPI:
    """Handle all communication with the Mikrotik API."""

    def __init__(
        self,
        host,
        username,
        password,
        port=0,
        use_ssl=True,
        login_method=DEFAULT_LOGIN_METHOD,
        encoding=DEFAULT_ENCODING,
    ):
        """Initialize the Mikrotik Client."""
        self._host = host
        self._use_ssl = use_ssl
        self._port = port
        self._username = username
        self._password = password
        self._login_method = login_method
        self._encoding = encoding
        self._ssl_wrapper = None
        self.lock = Lock()

        self._connection = None
        self._connected = False
        self._reconnected = True
        self._connection_epoch = 0
        self._connection_retry_sec = 58
        self.error = None
        self.connection_error_reported = False
        self.client_traffic_last_run = None

        # Default ports
        if not self._port:
            self._port = 8729 if self._use_ssl else 8728

    # ---------------------------
    #   has_reconnected
    # ---------------------------
    def has_reconnected(self) -> bool:
        """Check if mikrotik has reconnected"""
        if self._reconnected:
            self._reconnected = False
            return True

        return False

    # ---------------------------
    #   connection_check
    # ---------------------------
    def connection_check(self) -> bool:
        """Check if mikrotik is connected"""
        if not self._connected or not self._connection:
            if self._connection_epoch > time() - self._connection_retry_sec:
                return False

            if not self.connect():
                return False

        return True

    # ---------------------------
    #   disconnect
    # ---------------------------
    def disconnect(self, location="unknown", error=None):
        """Disconnect from Mikrotik device."""
        if not error:
            error = "unknown"

        if not self.connection_error_reported:
            if location == "unknown":
                _LOGGER.error("Mikrotik %s connection closed", self._host)
            else:
                _LOGGER.error(
                    "Mikrotik %s error while %s : %s", self._host, location, error
                )

            self.connection_error_reported = True

        self._reconnected = False
        self._connected = False
        self._connection = None
        self._connection_epoch = 0

    # ---------------------------
    #   connect
    # ---------------------------
    def connect(self) -> bool:
        """Connect to Mikrotik device."""
        self.error = ""
        self._connected = False
        self._connection_epoch = time()

        kwargs = {
            "encoding": self._encoding,
            "login_methods": self._login_method,
            "port": self._port,
        }

        if self._use_ssl:
            if self._ssl_wrapper is None:
                ssl_context = ssl.create_default_context()
                ssl_context.check_hostname = False
                ssl_context.verify_mode = ssl.CERT_NONE
                self._ssl_wrapper = ssl_context.wrap_socket
            kwargs["ssl_wrapper"] = self._ssl_wrapper
        self.lock.acquire()
        try:
            self._connection = librouteros.connect(
                self._host, self._username, self._password, **kwargs
            )
        except Exception as e:
            if not self.connection_error_reported:
                _LOGGER.error("Mikrotik %s error while connecting: %s", self._host, e)
                self.connection_error_reported = True

            self.error_to_strings(f"{e}")
            self._connection = None
            self.lock.release()
            return False
        else:
            if self.connection_error_reported:
                _LOGGER.warning("Mikrotik Reconnected to %s", self._host)
                self.connection_error_reported = False
            else:
                _LOGGER.debug("Mikrotik Connected to %s", self._host)

            self._connected = True
            self._reconnected = True
            self.lock.release()

        return self._connected

    # ---------------------------
    #   error_to_strings
    # ---------------------------
    def error_to_strings(self, error):
        """Translate error output to error string."""
        self.error = "cannot_connect"
        if error == "invalid user name or password (6)":
            self.error = "wrong_login"

        if "ALERT_HANDSHAKE_FAILURE" in error:
            self.error = "ssl_handshake_failure"

    # ---------------------------
    #   connected
    # ---------------------------
    def connected(self) -> bool:
        """Return connected boolean."""
        return self._connected

    # ---------------------------
    #   query
    # ---------------------------
    def query(self, path, command=None, args=None, return_list=True) -> Optional(list):
        """Retrieve data from Mikrotik API."""
        """Returns generator object, unless return_list passed as True"""
        if args is None:
            args = {}

        if not self.connection_check():
            return None

        self.lock.acquire()
        try:
            _LOGGER.debug("API query: %s", path)
            response = self._connection.path(path)
        except Exception as e:
            self.disconnect("path", e)
            self.lock.release()
            return None

        if response and return_list and not command:
            try:
                response = list(response)
            except Exception as e:
                self.disconnect(f"building list for path {path}", e)
                self.lock.release()
                return None
        elif response and command:
            _LOGGER.debug("API query: %s, %s, %s", path, command, args)
            try:
                response = list(response(command, **args))
            except Exception as e:
                self.disconnect("path", e)
                self.lock.release()
                return None

        self.lock.release()
        return response or None

    # ---------------------------
    #   set_value
    # ---------------------------
    def set_value(self, path, param, value, mod_param, mod_value) -> bool:
        """Modify a parameter"""
        entry_found = None

        if not self.connection_check():
            return False

        response = self.query(path, return_list=False)
        if response is None:
            return False

        for tmp in response:
            if param not in tmp:
                continue

            if tmp[param] != value:
                continue

            entry_found = tmp[".id"]

        if not entry_found:
            _LOGGER.error(
                "Mikrotik %s set_value parameter %s with value %s not found",
                self._host,
                param,
                value,
            )
            return True

        params = {".id": entry_found, mod_param: mod_value}
        self.lock.acquire()
        try:
            response.update(**params)
        except Exception as e:
            self.disconnect("set_value", e)
            self.lock.release()
            return False

        self.lock.release()
        return True

    # ---------------------------
    #   execute
    # ---------------------------
    def execute(self, path, command, param, value, attributes=None) -> bool:
        """Execute a command"""
        entry_found = None
        params = {}

        if not self.connection_check():
            return False

        response = self.query(path, return_list=False)
        if response is None:
            return False

        if param:
            for tmp in response:
                if param not in tmp:
                    continue

                if tmp[param] != value:
                    continue

                entry_found = tmp[".id"]

            if not entry_found:
                _LOGGER.error(
                    "Mikrotik %s Execute %s parameter %s with value %s not found",
                    self._host,
                    command,
                    param,
                    value,
                )
                return True

            params = {".id": entry_found}

        if attributes:
            params.update(attributes)

        self.lock.acquire()
        try:
            tuple(response(command, **params))
        except Exception as e:
            self.disconnect("execute", e)
            self.lock.release()
            return False

        self.lock.release()
        return True

    # ---------------------------
    #   run_script
    # ---------------------------
    def run_script(self, name) -> bool:
        """Run script"""
        entry_found = None
        if not self.connection_check():
            return False

        response = self.query("/system/script", return_list=False)
        if response is None:
            return False

        self.lock.acquire()
        for tmp in response:
            if "name" not in tmp:
                continue

            if tmp["name"] != name:
                continue

            entry_found = tmp[".id"]

        if not entry_found:
            _LOGGER.error("Mikrotik %s Script %s not found", self._host, name)
            return True

        try:
            run = response("run", **{".id": entry_found})
            tuple(run)
        except Exception as e:
            self.disconnect("run_script", e)
            self.lock.release()
            return False

        self.lock.release()
        return True

    # ---------------------------
    #   arp_ping
    # ---------------------------
    def arp_ping(self, address, interface) -> bool:
        """Check arp ping response traffic stats"""
        if not self.connection_check():
            return False

        response = self.query("/ping", return_list=False)
        if response is None:
            return False

        args = {
            "arp-ping": "no",
            "interval": "100ms",
            "count": 3,
            "interface": interface,
            "address": address,
        }
        self.lock.acquire()
        try:
            # _LOGGER.debug("Ping host query: %s", args["address"])
            ping = response("/ping", **args)
        except Exception as e:
            self.disconnect("arp_ping", e)
            self.lock.release()
            return False

        try:
            ping = list(ping)
        except Exception as e:
            self.disconnect("arp_ping", e)
            self.lock.release()
            return False

        self.lock.release()

        for tmp in ping:
            if "received" in tmp and tmp["received"] > 0:
                _LOGGER.debug("Ping host success: %s", args["address"])
                return True

        _LOGGER.debug("Ping host failure: %s", args["address"])
        return False

    @staticmethod
    def _current_milliseconds():
        return int(round(time() * 1000))

    def is_accounting_and_local_traffic_enabled(self) -> (bool, bool):
        # Returns:
        #   1st bool: Is accounting enabled
        #   2nd bool: Is account-local-traffic enabled

        if not self.connection_check():
            return False, False

        response = self.query("/ip/accounting")
        if response is None:
            return False, False

        for item in response:
            if "enabled" not in item:
                continue
            if not item["enabled"]:
                return False, False

        for item in response:
            if "account-local-traffic" not in item:
                continue
            if not item["account-local-traffic"]:
                return True, False

        return True, True

    # ---------------------------
    #   take_client_traffic_snapshot
    #   Returns float -> period in seconds between last and current run
    # ---------------------------
    def take_client_traffic_snapshot(self, use_accounting) -> float:
        """Tako accounting snapshot and return time diff"""
        if not self.connection_check():
            return 0

        if use_accounting:
            accounting = self.query("/ip/accounting", return_list=False)

            self.lock.acquire()
            try:
                # Prepare command
                take = accounting("snapshot/take")
            except Exception as e:
                self.disconnect("accounting_snapshot", e)
                self.lock.release()
                return 0

            try:
                list(take)
            except Exception as e:
                self.disconnect("accounting_snapshot", e)
                self.lock.release()
                return 0

            self.lock.release()

        # First request will be discarded because we cannot know when the last data was retrieved
        # prevents spikes in data
        if not self.client_traffic_last_run:
            self.client_traffic_last_run = self._current_milliseconds()
            return 0

        # Calculate time difference in seconds and return
        time_diff = self._current_milliseconds() - self.client_traffic_last_run
        self.client_traffic_last_run = self._current_milliseconds()
        return time_diff / 1000


File: /custom_components\mikrotik_router\sensor.py
"""Mikrotik sensor platform."""
from __future__ import annotations

from logging import getLogger
from collections.abc import Mapping
from datetime import date, datetime
from decimal import Decimal
from typing import Any

from homeassistant.components.sensor import SensorEntity
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers.typing import StateType
from homeassistant.helpers.entity_platform import AddEntitiesCallback

from .coordinator import MikrotikCoordinator
from .entity import MikrotikEntity, async_add_entities
from .helper import format_attribute
from .sensor_types import (
    SENSOR_TYPES,
    SENSOR_SERVICES,
    DEVICE_ATTRIBUTES_IFACE_ETHER,
    DEVICE_ATTRIBUTES_IFACE_SFP,
    DEVICE_ATTRIBUTES_IFACE_WIRELESS,
)

_LOGGER = getLogger(__name__)


# ---------------------------
#   async_setup_entry
# ---------------------------
async def async_setup_entry(
    hass: HomeAssistant,
    config_entry: ConfigEntry,
    _async_add_entities: AddEntitiesCallback,
) -> None:
    """Set up entry for component"""
    dispatcher = {
        "MikrotikSensor": MikrotikSensor,
        "MikrotikInterfaceTrafficSensor": MikrotikInterfaceTrafficSensor,
        "MikrotikClientTrafficSensor": MikrotikClientTrafficSensor,
    }
    await async_add_entities(hass, config_entry, dispatcher)


# ---------------------------
#   MikrotikSensor
# ---------------------------
class MikrotikSensor(MikrotikEntity, SensorEntity):
    """Define an Mikrotik sensor."""

    def __init__(
        self,
        coordinator: MikrotikCoordinator,
        entity_description,
        uid: str | None = None,
    ):
        super().__init__(coordinator, entity_description, uid)
        self._attr_suggested_unit_of_measurement = (
            self.entity_description.suggested_unit_of_measurement
        )

    @property
    def native_value(self) -> StateType | date | datetime | Decimal:
        """Return the value reported by the sensor."""
        return self._data[self.entity_description.data_attribute]

    @property
    def native_unit_of_measurement(self) -> str | None:
        """Return the unit the value is expressed in."""
        if self.entity_description.native_unit_of_measurement:
            if self.entity_description.native_unit_of_measurement.startswith("data__"):
                uom = self.entity_description.native_unit_of_measurement[6:]
                if uom in self._data:
                    return self._data[uom]

            return self.entity_description.native_unit_of_measurement

        return None


# ---------------------------
#   MikrotikInterfaceTrafficSensor
# ---------------------------
class MikrotikInterfaceTrafficSensor(MikrotikSensor):
    """Define an Mikrotik MikrotikInterfaceTrafficSensor sensor."""

    @property
    def extra_state_attributes(self) -> Mapping[str, Any]:
        """Return the state attributes."""
        attributes = super().extra_state_attributes

        if self._data["type"] == "ether":
            for variable in DEVICE_ATTRIBUTES_IFACE_ETHER:
                if variable in self._data:
                    attributes[format_attribute(variable)] = self._data[variable]

            if "sfp-shutdown-temperature" in self._data:
                for variable in DEVICE_ATTRIBUTES_IFACE_SFP:
                    if variable in self._data:
                        attributes[format_attribute(variable)] = self._data[variable]

        elif self._data["type"] == "wlan":
            for variable in DEVICE_ATTRIBUTES_IFACE_WIRELESS:
                if variable in self._data:
                    attributes[format_attribute(variable)] = self._data[variable]

        return attributes


# ---------------------------
#   MikrotikClientTrafficSensor
# ---------------------------
class MikrotikClientTrafficSensor(MikrotikSensor):
    """Define an Mikrotik MikrotikClientTrafficSensor sensor."""

    @property
    def custom_name(self) -> str:
        """Return the name for this entity"""
        return f"{self.entity_description.name}"

    # @property
    # def available(self) -> bool:
    #     """Return if controller and accounting feature in Mikrotik is available.
    #     Additional check for lan-tx/rx sensors
    #     """
    #     if self.entity_description.data_attribute in ["lan-tx", "lan-rx"]:
    #         return (
    #             self.coordinator.connected()
    #             and self._data["available"]
    #             and self._data["local_accounting"]
    #         )
    #     else:
    #         return self.coordinator.connected() and self._data["available"]


File: /custom_components\mikrotik_router\sensor_types.py
"""Definitions for sensor entities."""
from __future__ import annotations

from dataclasses import dataclass, field
from typing import List

from homeassistant.helpers.device_registry import CONNECTION_NETWORK_MAC
from homeassistant.helpers.entity import EntityCategory
from homeassistant.components.sensor import (
    SensorDeviceClass,
    SensorStateClass,
    SensorEntityDescription,
)
from homeassistant.const import (
    PERCENTAGE,
    REVOLUTIONS_PER_MINUTE,
    UnitOfTemperature,
    UnitOfDataRate,
    UnitOfInformation,
    UnitOfElectricPotential,
    UnitOfPower,
)

from .const import DOMAIN

DEVICE_ATTRIBUTES_IFACE = [
    "running",
    "enabled",
    "comment",
    "client-ip-address",
    "client-mac-address",
    "port-mac-address",
    "last-link-down-time",
    "last-link-up-time",
    "link-downs",
    "actual-mtu",
    "type",
    "name",
]

DEVICE_ATTRIBUTES_IFACE_ETHER = [
    "status",
    "auto-negotiation",
    "rate",
    "full-duplex",
    "default-name",
    "poe-out",
]

DEVICE_ATTRIBUTES_IFACE_SFP = [
    "status",
    "auto-negotiation",
    "advertising",
    "link-partner-advertising",
    "sfp-temperature",
    "sfp-supply-voltage",
    "sfp-module-present",
    "sfp-tx-bias-current",
    "sfp-tx-power",
    "sfp-rx-power",
    "sfp-rx-loss",
    "sfp-tx-fault",
    "sfp-type",
    "sfp-connector-type",
    "sfp-vendor-name",
    "sfp-vendor-part-number",
    "sfp-vendor-revision",
    "sfp-vendor-serial",
    "sfp-manufacturing-date",
    "eeprom-checksum",
]

DEVICE_ATTRIBUTES_IFACE_WIRELESS = [
    "ssid",
    "mode",
    "radio-name",
    "interface-type",
    "country",
    "installation",
    "antenna-gain",
    "frequency",
    "band",
    "channel-width",
    "secondary-frequency",
    "wireless-protocol",
    "rate-set",
    "distance",
    "tx-power-mode",
    "vlan-id",
    "wds-mode",
    "wds-default-bridge",
    "bridge-mode",
    "hide-ssid",
]

DEVICE_ATTRIBUTES_CLIENT_TRAFFIC = [
    "address",
    "mac-address",
    "host-name",
    "authorized",
    "bypassed",
]
DEVICE_ATTRIBUTES_GPS = [
    "valid",
    "latitude",
    "longitude",
    "altitude",
    "speed",
    "destination-bearing",
    "true-bearing",
    "magnetic-bearing",
    "satellites",
    "fix-quality",
    "horizontal-dilution",
]


@dataclass
class MikrotikSensorEntityDescription(SensorEntityDescription):
    """Class describing mikrotik entities."""

    ha_group: str | None = None
    ha_connection: str | None = None
    ha_connection_value: str | None = None
    data_path: str | None = None
    data_attribute: str | None = None
    data_name: str | None = None
    data_name_comment: bool = False
    data_uid: str | None = None
    data_reference: str | None = None
    data_attributes_list: List = field(default_factory=lambda: [])
    func: str = "MikrotikSensor"


SENSOR_TYPES: tuple[MikrotikSensorEntityDescription, ...] = (
    MikrotikSensorEntityDescription(
        key="system_temperature",
        name="Temperature",
        icon="mdi:thermometer",
        native_unit_of_measurement=UnitOfTemperature.CELSIUS,
        suggested_unit_of_measurement=UnitOfTemperature.CELSIUS,
        suggested_display_precision=0,
        device_class=SensorDeviceClass.TEMPERATURE,
        state_class=SensorStateClass.MEASUREMENT,
        entity_category=EntityCategory.DIAGNOSTIC,
        ha_group="System",
        data_path="health",
        data_attribute="temperature",
        data_name="",
        data_uid="",
        data_reference="",
    ),
    MikrotikSensorEntityDescription(
        key="system_voltage",
        name="Voltage",
        icon="mdi:lightning-bolt",
        native_unit_of_measurement=UnitOfElectricPotential.VOLT,
        suggested_unit_of_measurement=UnitOfElectricPotential.VOLT,
        suggested_display_precision=1,
        device_class=SensorDeviceClass.VOLTAGE,
        state_class=SensorStateClass.MEASUREMENT,
        entity_category=EntityCategory.DIAGNOSTIC,
        ha_group="System",
        data_path="health",
        data_attribute="voltage",
        data_name="",
        data_uid="",
        data_reference="",
    ),
    MikrotikSensorEntityDescription(
        key="system_cpu-temperature",
        name="CPU temperature",
        icon="mdi:thermometer",
        native_unit_of_measurement=UnitOfTemperature.CELSIUS,
        suggested_unit_of_measurement=UnitOfTemperature.CELSIUS,
        suggested_display_precision=0,
        device_class=SensorDeviceClass.TEMPERATURE,
        state_class=SensorStateClass.MEASUREMENT,
        entity_category=EntityCategory.DIAGNOSTIC,
        ha_group="System",
        data_path="health",
        data_attribute="cpu-temperature",
        data_name="",
        data_uid="",
        data_reference="",
    ),
    MikrotikSensorEntityDescription(
        key="system_switch-temperature",
        name="Switch temperature",
        icon="mdi:thermometer",
        native_unit_of_measurement=UnitOfTemperature.CELSIUS,
        suggested_unit_of_measurement=UnitOfTemperature.CELSIUS,
        suggested_display_precision=0,
        device_class=SensorDeviceClass.TEMPERATURE,
        state_class=SensorStateClass.MEASUREMENT,
        entity_category=EntityCategory.DIAGNOSTIC,
        ha_group="System",
        data_path="health",
        data_attribute="switch-temperature",
        data_name="",
        data_uid="",
        data_reference="",
    ),
    MikrotikSensorEntityDescription(
        key="system_board-temperature1",
        name="Board temperature",
        icon="mdi:thermometer",
        native_unit_of_measurement=UnitOfTemperature.CELSIUS,
        suggested_unit_of_measurement=UnitOfTemperature.CELSIUS,
        suggested_display_precision=0,
        device_class=SensorDeviceClass.TEMPERATURE,
        state_class=SensorStateClass.MEASUREMENT,
        entity_category=EntityCategory.DIAGNOSTIC,
        ha_group="System",
        data_path="health",
        data_attribute="board-temperature1",
        data_name="",
        data_uid="",
        data_reference="",
    ),
    MikrotikSensorEntityDescription(
        key="system_phy-temperature",
        name="PHY temperature",
        icon="mdi:thermometer",
        native_unit_of_measurement=UnitOfTemperature.CELSIUS,
        suggested_unit_of_measurement=UnitOfTemperature.CELSIUS,
        suggested_display_precision=0,
        device_class=SensorDeviceClass.TEMPERATURE,
        state_class=SensorStateClass.MEASUREMENT,
        entity_category=EntityCategory.DIAGNOSTIC,
        ha_group="System",
        data_path="health",
        data_attribute="phy-temperature",
        data_name="",
        data_uid="",
        data_reference="",
    ),
    MikrotikSensorEntityDescription(
        key="system_power-consumption",
        name="Power consumption",
        icon="mdi:transmission-tower",
        native_unit_of_measurement=UnitOfPower.WATT,
        suggested_unit_of_measurement=UnitOfPower.WATT,
        suggested_display_precision=0,
        device_class=SensorDeviceClass.POWER,
        state_class=SensorStateClass.MEASUREMENT,
        entity_category=EntityCategory.DIAGNOSTIC,
        ha_group="System",
        data_path="health",
        data_attribute="power-consumption",
        data_name="",
        data_uid="",
        data_reference="",
    ),
    MikrotikSensorEntityDescription(
        key="system_poe_out_consumption",
        name="PoE out power consumption",
        icon="mdi:flash",
        native_unit_of_measurement=UnitOfPower.WATT,
        suggested_unit_of_measurement=UnitOfPower.WATT,
        suggested_display_precision=1,
        device_class=SensorDeviceClass.POWER,
        state_class=SensorStateClass.MEASUREMENT,
        entity_category=EntityCategory.DIAGNOSTIC,
        ha_group="System",
        data_path="health",
        data_attribute="poe-out-consumption",
        data_name="",
        data_uid="",
        data_reference="",
    ),
    MikrotikSensorEntityDescription(
        key="system_fan1-speed",
        name="Fan1 speed",
        icon="mdi:fan",
        native_unit_of_measurement=REVOLUTIONS_PER_MINUTE,
        device_class=None,
        state_class=SensorStateClass.MEASUREMENT,
        entity_category=EntityCategory.DIAGNOSTIC,
        ha_group="System",
        data_path="health",
        data_attribute="fan1-speed",
        data_name="",
        data_uid="",
        data_reference="",
    ),
    MikrotikSensorEntityDescription(
        key="system_fan2-speed",
        name="Fan2 speed",
        icon="mdi:fan",
        native_unit_of_measurement=REVOLUTIONS_PER_MINUTE,
        device_class=None,
        state_class=SensorStateClass.MEASUREMENT,
        entity_category=EntityCategory.DIAGNOSTIC,
        ha_group="System",
        data_path="health",
        data_attribute="fan2-speed",
        data_name="",
        data_uid="",
        data_reference="",
    ),
    MikrotikSensorEntityDescription(
        key="system_uptime",
        name="Uptime",
        icon=None,
        native_unit_of_measurement=None,
        device_class=SensorDeviceClass.TIMESTAMP,
        state_class=None,
        entity_category=EntityCategory.DIAGNOSTIC,
        ha_group="System",
        data_path="resource",
        data_attribute="uptime",
        data_name="",
        data_uid="",
        data_reference="",
    ),
    MikrotikSensorEntityDescription(
        key="system_cpu-load",
        name="CPU load",
        icon="mdi:speedometer",
        native_unit_of_measurement=PERCENTAGE,
        device_class=None,
        state_class=SensorStateClass.MEASUREMENT,
        entity_category=None,
        ha_group="System",
        data_path="resource",
        data_attribute="cpu-load",
        data_name="",
        data_uid="",
        data_reference="",
    ),
    MikrotikSensorEntityDescription(
        key="system_memory-usage",
        name="Memory usage",
        icon="mdi:memory",
        native_unit_of_measurement=PERCENTAGE,
        device_class=None,
        state_class=SensorStateClass.MEASUREMENT,
        entity_category=None,
        ha_group="System",
        data_path="resource",
        data_attribute="memory-usage",
        data_name="",
        data_uid="",
        data_reference="",
    ),
    MikrotikSensorEntityDescription(
        key="system_hdd-usage",
        name="HDD usage",
        icon="mdi:harddisk",
        native_unit_of_measurement=PERCENTAGE,
        device_class=None,
        state_class=SensorStateClass.MEASUREMENT,
        entity_category=None,
        ha_group="System",
        data_path="resource",
        data_attribute="hdd-usage",
        data_name="",
        data_uid="",
        data_reference="",
    ),
    MikrotikSensorEntityDescription(
        key="system_clients-wired",
        name="Wired clients",
        icon="mdi:lan",
        native_unit_of_measurement=None,
        device_class=None,
        state_class=SensorStateClass.MEASUREMENT,
        entity_category=None,
        ha_group="System",
        data_path="resource",
        data_attribute="clients_wired",
        data_name="",
        data_uid="",
        data_reference="",
    ),
    MikrotikSensorEntityDescription(
        key="system_clients-wireless",
        name="Wireless clients",
        icon="mdi:wifi",
        native_unit_of_measurement=None,
        device_class=None,
        state_class=SensorStateClass.MEASUREMENT,
        entity_category=None,
        ha_group="System",
        data_path="resource",
        data_attribute="clients_wireless",
        data_name="",
        data_uid="",
        data_reference="",
    ),
    MikrotikSensorEntityDescription(
        key="system_captive-authorized",
        name="Captive portal clients",
        icon="mdi:key-wireless",
        native_unit_of_measurement=None,
        device_class=None,
        state_class=SensorStateClass.MEASUREMENT,
        entity_category=None,
        ha_group="System",
        data_path="resource",
        data_attribute="captive_authorized",
        data_name="",
        data_uid="",
        data_reference="",
    ),
    MikrotikSensorEntityDescription(
        key="system_gps-latitude",
        name="Latitude",
        icon="mdi:latitude",
        native_unit_of_measurement=None,
        device_class=None,
        state_class=None,
        entity_category=EntityCategory.DIAGNOSTIC,
        ha_group="System",
        data_path="gps",
        data_attribute="latitude",
        data_name="",
        data_uid="",
        data_reference="",
        data_attributes_list=DEVICE_ATTRIBUTES_GPS,
    ),
    MikrotikSensorEntityDescription(
        key="system_gps-longitude",
        name="Longitude",
        icon="mdi:longitude",
        native_unit_of_measurement=None,
        device_class=None,
        state_class=None,
        entity_category=EntityCategory.DIAGNOSTIC,
        ha_group="System",
        data_path="gps",
        data_attribute="longitude",
        data_name="",
        data_uid="",
        data_reference="",
        data_attributes_list=DEVICE_ATTRIBUTES_GPS,
    ),
    MikrotikSensorEntityDescription(
        key="traffic_tx",
        name="TX",
        icon="mdi:upload-network-outline",
        native_unit_of_measurement=UnitOfDataRate.BYTES_PER_SECOND,
        suggested_unit_of_measurement=UnitOfDataRate.KILOBYTES_PER_SECOND,
        suggested_display_precision=1,
        device_class=SensorDeviceClass.DATA_RATE,
        state_class=SensorStateClass.MEASUREMENT,
        entity_category=None,
        ha_group="data__default-name",
        ha_connection=CONNECTION_NETWORK_MAC,
        ha_connection_value="data__port-mac-address",
        data_path="interface",
        data_attribute="tx",
        data_name="default-name",
        data_uid="",
        data_reference="default-name",
        data_attributes_list=DEVICE_ATTRIBUTES_IFACE,
        func="MikrotikInterfaceTrafficSensor",
    ),
    MikrotikSensorEntityDescription(
        key="traffic_rx",
        name="RX",
        icon="mdi:download-network-outline",
        native_unit_of_measurement=UnitOfDataRate.BYTES_PER_SECOND,
        suggested_unit_of_measurement=UnitOfDataRate.KILOBYTES_PER_SECOND,
        suggested_display_precision=1,
        device_class=SensorDeviceClass.DATA_RATE,
        state_class=SensorStateClass.MEASUREMENT,
        entity_category=None,
        ha_group="data__default-name",
        ha_connection=CONNECTION_NETWORK_MAC,
        ha_connection_value="data__port-mac-address",
        data_path="interface",
        data_attribute="rx",
        data_name="default-name",
        data_uid="",
        data_reference="default-name",
        data_attributes_list=DEVICE_ATTRIBUTES_IFACE,
        func="MikrotikInterfaceTrafficSensor",
    ),
    MikrotikSensorEntityDescription(
        key="tx-total",
        name="TX total",
        icon="mdi:upload-network",
        native_unit_of_measurement=UnitOfInformation.BYTES,
        suggested_unit_of_measurement=UnitOfInformation.GIGABYTES,
        suggested_display_precision=1,
        device_class=SensorDeviceClass.DATA_SIZE,
        state_class=SensorStateClass.TOTAL_INCREASING,
        entity_category=None,
        ha_group="data__default-name",
        ha_connection=CONNECTION_NETWORK_MAC,
        ha_connection_value="data__port-mac-address",
        data_path="interface",
        data_attribute="tx-current",
        data_name="default-name",
        data_uid="",
        data_reference="default-name",
        data_attributes_list=DEVICE_ATTRIBUTES_IFACE,
        func="MikrotikInterfaceTrafficSensor",
    ),
    MikrotikSensorEntityDescription(
        key="rx-total",
        name="RX total",
        icon="mdi:download-network",
        native_unit_of_measurement=UnitOfInformation.BYTES,
        suggested_unit_of_measurement=UnitOfInformation.GIGABYTES,
        suggested_display_precision=1,
        device_class=SensorDeviceClass.DATA_SIZE,
        state_class=SensorStateClass.TOTAL_INCREASING,
        entity_category=None,
        ha_group="data__default-name",
        ha_connection=CONNECTION_NETWORK_MAC,
        ha_connection_value="data__port-mac-address",
        data_path="interface",
        data_attribute="rx-current",
        data_name="default-name",
        data_uid="",
        data_reference="default-name",
        data_attributes_list=DEVICE_ATTRIBUTES_IFACE,
        func="MikrotikInterfaceTrafficSensor",
    ),
    MikrotikSensorEntityDescription(
        key="client_traffic_lan_tx",
        name="LAN TX",
        icon="mdi:upload-network",
        native_unit_of_measurement=UnitOfDataRate.BYTES_PER_SECOND,
        suggested_unit_of_measurement=UnitOfDataRate.KILOBYTES_PER_SECOND,
        suggested_display_precision=1,
        device_class=SensorDeviceClass.DATA_RATE,
        state_class=SensorStateClass.MEASUREMENT,
        entity_category=None,
        ha_group="",
        ha_connection=CONNECTION_NETWORK_MAC,
        ha_connection_value="data__mac-address",
        data_path="client_traffic",
        data_attribute="lan-tx",
        data_name="host-name",
        data_uid="",
        data_reference="mac-address",
        data_attributes_list=DEVICE_ATTRIBUTES_CLIENT_TRAFFIC,
        func="MikrotikClientTrafficSensor",
    ),
    MikrotikSensorEntityDescription(
        key="client_traffic_lan_rx",
        name="LAN RX",
        icon="mdi:download-network",
        native_unit_of_measurement=UnitOfDataRate.BYTES_PER_SECOND,
        suggested_unit_of_measurement=UnitOfDataRate.KILOBYTES_PER_SECOND,
        suggested_display_precision=1,
        device_class=SensorDeviceClass.DATA_RATE,
        state_class=SensorStateClass.MEASUREMENT,
        entity_category=None,
        ha_group="",
        ha_connection=CONNECTION_NETWORK_MAC,
        ha_connection_value="data__mac-address",
        data_path="client_traffic",
        data_attribute="lan-rx",
        data_name="host-name",
        data_uid="",
        data_reference="mac-address",
        data_attributes_list=DEVICE_ATTRIBUTES_CLIENT_TRAFFIC,
        func="MikrotikClientTrafficSensor",
    ),
    MikrotikSensorEntityDescription(
        key="client_traffic_wan_tx",
        name="WAN TX",
        icon="mdi:upload-network",
        native_unit_of_measurement=UnitOfDataRate.BYTES_PER_SECOND,
        suggested_unit_of_measurement=UnitOfDataRate.KILOBYTES_PER_SECOND,
        suggested_display_precision=1,
        device_class=SensorDeviceClass.DATA_RATE,
        state_class=SensorStateClass.MEASUREMENT,
        entity_category=None,
        ha_group="",
        ha_connection=CONNECTION_NETWORK_MAC,
        ha_connection_value="data__mac-address",
        data_path="client_traffic",
        data_attribute="wan-tx",
        data_name="host-name",
        data_uid="",
        data_reference="mac-address",
        data_attributes_list=DEVICE_ATTRIBUTES_CLIENT_TRAFFIC,
        func="MikrotikClientTrafficSensor",
    ),
    MikrotikSensorEntityDescription(
        key="client_traffic_wan_rx",
        name="WAN RX",
        icon="mdi:download-network",
        native_unit_of_measurement=UnitOfDataRate.BYTES_PER_SECOND,
        suggested_unit_of_measurement=UnitOfDataRate.KILOBYTES_PER_SECOND,
        suggested_display_precision=1,
        device_class=SensorDeviceClass.DATA_RATE,
        state_class=SensorStateClass.MEASUREMENT,
        entity_category=None,
        ha_group="",
        ha_connection=CONNECTION_NETWORK_MAC,
        ha_connection_value="data__mac-address",
        data_path="client_traffic",
        data_attribute="wan-rx",
        data_name="host-name",
        data_uid="",
        data_reference="mac-address",
        data_attributes_list=DEVICE_ATTRIBUTES_CLIENT_TRAFFIC,
        func="MikrotikClientTrafficSensor",
    ),
    MikrotikSensorEntityDescription(
        key="client_traffic_tx",
        name="TX",
        icon="mdi:upload-network",
        native_unit_of_measurement=UnitOfDataRate.BYTES_PER_SECOND,
        suggested_unit_of_measurement=UnitOfDataRate.KILOBYTES_PER_SECOND,
        suggested_display_precision=1,
        device_class=SensorDeviceClass.DATA_RATE,
        state_class=SensorStateClass.MEASUREMENT,
        entity_category=None,
        ha_group="",
        ha_connection=CONNECTION_NETWORK_MAC,
        ha_connection_value="data__mac-address",
        data_path="client_traffic",
        data_attribute="tx",
        data_name="host-name",
        data_uid="",
        data_reference="mac-address",
        data_attributes_list=DEVICE_ATTRIBUTES_CLIENT_TRAFFIC,
        func="MikrotikClientTrafficSensor",
    ),
    MikrotikSensorEntityDescription(
        key="client_traffic_rx",
        name="RX",
        icon="mdi:download-network",
        native_unit_of_measurement=UnitOfDataRate.BYTES_PER_SECOND,
        suggested_unit_of_measurement=UnitOfDataRate.KILOBYTES_PER_SECOND,
        suggested_display_precision=1,
        device_class=SensorDeviceClass.DATA_RATE,
        state_class=SensorStateClass.MEASUREMENT,
        entity_category=None,
        ha_group="",
        ha_connection=CONNECTION_NETWORK_MAC,
        ha_connection_value="data__mac-address",
        data_path="client_traffic",
        data_attribute="rx",
        data_name="host-name",
        data_uid="",
        data_reference="mac-address",
        data_attributes_list=DEVICE_ATTRIBUTES_CLIENT_TRAFFIC,
        func="MikrotikClientTrafficSensor",
    ),
    MikrotikSensorEntityDescription(
        key="environment",
        name="",
        icon="mdi:clipboard-list",
        native_unit_of_measurement="",
        device_class=None,
        state_class=None,
        entity_category=None,
        ha_group="Environment",
        ha_connection=DOMAIN,
        ha_connection_value="Environment",
        data_path="environment",
        data_attribute="value",
        data_name="name",
        data_uid="name",
        data_reference="name",
    ),
)

SENSOR_SERVICES = []


File: /custom_components\mikrotik_router\services.yaml
run_script:
  description: Run script on Mikrotik
  fields:
    router:
      description: Name of the router
      example: "Mikrotik"
    script:
      description: Name of the script
      example: "MyScript"

File: /custom_components\mikrotik_router\strings.json
{
    "config": {
        "step": {
            "user": {
                "title": "Set up Mikrotik Router",
                "description": "Set up Mikrotik Router integration.",
                "data": {
                    "name": "Name of the integration",
                    "host": "Host",
                    "port": "Port",
                    "username": "Username",
                    "password": "Password",
                    "ssl": "Use SSL"
                }
            }
        },
        "error": {
            "name_exists": "Name already exists.",
            "cannot_connect": "Cannot connect to Mikrotik.",
            "ssl_handshake_failure": "SSL handshake failure",
            "connection_timeout": "Mikrotik connection timeout.",
            "wrong_login": "Invalid user name or password."
        }
    },
    "options": {
        "step": {
            "basic_options": {
                "data": {
                    "scan_interval": "Scan interval (requires HA restart)",
                    "track_iface_clients": "Show client MAC and IP on interfaces",
                    "unit_of_measurement": "Unit of measurement",
                    "track_network_hosts_timeout": "Track network devices timeout (seconds)",
                    "zone": "Zone for device tracker"
                },
                "title": "Mikrotik Router options (1/2)",
                "description": "Configure integration"
            },
            "sensor_select": {
                "data": {
                    "track_network_hosts": "Track network devices",
                    "sensor_port_tracker": "Port tracker sensors",
                    "sensor_netwatch_tracker": "Netwatch tracker sensors",
                    "sensor_port_traffic": "Port traffic sensors",
                    "sensor_client_traffic": "Client traffic sensors",
                    "sensor_client_captive": "Captive portal data",
                    "sensor_simple_queues": "Simple queues switches",
                    "sensor_nat": "NAT switches",
                    "sensor_scripts": "Script switches",
                    "sensor_environment": "Environment variable sensors",
                    "sensor_kidcontrol": "Kid control",
                    "sensor_mangle": "Mangle switches",
                    "sensor_ppp": "PPP users",
                    "sensor_filter": "Filter switches"
                },
                "title": "Mikrotik Router options (2/2)",
                "description": "Enable sensors and switches"
            }
        }
    }
}

File: /custom_components\mikrotik_router\switch.py
"""Support for the Mikrotik Router switches."""
from __future__ import annotations

from logging import getLogger
from collections.abc import Mapping
from typing import Any, Optional

from homeassistant.components.switch import SwitchEntity
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.helpers.restore_state import RestoreEntity

from .entity import MikrotikEntity, async_add_entities
from .helper import format_attribute
from .switch_types import (
    SENSOR_TYPES,
    SENSOR_SERVICES,
    DEVICE_ATTRIBUTES_IFACE_ETHER,
    DEVICE_ATTRIBUTES_IFACE_SFP,
    DEVICE_ATTRIBUTES_IFACE_WIRELESS,
)

_LOGGER = getLogger(__name__)


# ---------------------------
#   async_setup_entry
# ---------------------------
async def async_setup_entry(
    hass: HomeAssistant,
    config_entry: ConfigEntry,
    _async_add_entities: AddEntitiesCallback,
) -> None:
    """Set up entry for component"""
    dispatcher = {
        "MikrotikSwitch": MikrotikSwitch,
        "MikrotikPortSwitch": MikrotikPortSwitch,
        "MikrotikNATSwitch": MikrotikNATSwitch,
        "MikrotikMangleSwitch": MikrotikMangleSwitch,
        "MikrotikFilterSwitch": MikrotikFilterSwitch,
        "MikrotikQueueSwitch": MikrotikQueueSwitch,
        "MikrotikKidcontrolPauseSwitch": MikrotikKidcontrolPauseSwitch,
    }
    await async_add_entities(hass, config_entry, dispatcher)


# ---------------------------
#   MikrotikSwitch
# ---------------------------
class MikrotikSwitch(MikrotikEntity, SwitchEntity, RestoreEntity):
    """Representation of a switch."""

    @property
    def is_on(self) -> bool:
        """Return true if device is on."""
        return self._data[self.entity_description.data_attribute]

    @property
    def icon(self) -> str:
        """Return the icon."""
        if self._data[self.entity_description.data_attribute]:
            return self.entity_description.icon_enabled
        else:
            return self.entity_description.icon_disabled

    def turn_on(self, **kwargs: Any) -> None:
        """Required abstract method."""
        pass

    def turn_off(self, **kwargs: Any) -> None:
        """Required abstract method."""
        pass

    async def async_turn_on(self) -> None:
        """Turn on the switch."""
        if "write" not in self.coordinator.data["access"]:
            return

        path = self.entity_description.data_switch_path
        param = self.entity_description.data_reference
        value = self._data[self.entity_description.data_reference]
        mod_param = self.entity_description.data_switch_parameter
        self.coordinator.set_value(path, param, value, mod_param, False)
        await self.coordinator.async_refresh()

    async def async_turn_off(self) -> None:
        """Turn off the switch."""
        if "write" not in self.coordinator.data["access"]:
            return

        path = self.entity_description.data_switch_path
        param = self.entity_description.data_reference
        value = self._data[self.entity_description.data_reference]
        mod_param = self.entity_description.data_switch_parameter
        self.coordinator.set_value(path, param, value, mod_param, True)
        await self.coordinator.async_refresh()


# ---------------------------
#   MikrotikPortSwitch
# ---------------------------
class MikrotikPortSwitch(MikrotikSwitch):
    """Representation of a network port switch."""

    @property
    def extra_state_attributes(self) -> Mapping[str, Any]:
        """Return the state attributes."""
        attributes = super().extra_state_attributes

        if self._data["type"] == "ether":
            for variable in DEVICE_ATTRIBUTES_IFACE_ETHER:
                if variable in self._data:
                    attributes[format_attribute(variable)] = self._data[variable]

            if "sfp-shutdown-temperature" in self._data:
                for variable in DEVICE_ATTRIBUTES_IFACE_SFP:
                    if variable in self._data:
                        attributes[format_attribute(variable)] = self._data[variable]

        elif self._data["type"] == "wlan":
            for variable in DEVICE_ATTRIBUTES_IFACE_WIRELESS:
                if variable in self._data:
                    attributes[format_attribute(variable)] = self._data[variable]

        return attributes

    @property
    def icon(self) -> str:
        """Return the icon."""
        if self._data["running"]:
            icon = self.entity_description.icon_enabled
        else:
            icon = self.entity_description.icon_disabled

        if not self._data["enabled"]:
            icon = "mdi:lan-disconnect"

        return icon

    async def async_turn_on(self) -> Optional[str]:
        """Turn on the switch."""
        if "write" not in self.coordinator.data["access"]:
            return

        path = self.entity_description.data_switch_path
        param = self.entity_description.data_reference
        if self._data["about"] == "managed by CAPsMAN":
            _LOGGER.error("Unable to enable %s, managed by CAPsMAN", self._data[param])
            return "managed by CAPsMAN"
        if "-" in self._data["port-mac-address"]:
            param = "name"
        value = self._data[self.entity_description.data_reference]
        mod_param = self.entity_description.data_switch_parameter
        self.coordinator.set_value(path, param, value, mod_param, False)

        if "poe-out" in self._data and self._data["poe-out"] == "off":
            path = "/interface/ethernet"
            self.coordinator.set_value(path, param, value, "poe-out", "auto-on")

        await self.coordinator.async_refresh()

    async def async_turn_off(self) -> Optional[str]:
        """Turn off the switch."""
        if "write" not in self.coordinator.data["access"]:
            return

        path = self.entity_description.data_switch_path
        param = self.entity_description.data_reference
        if self._data["about"] == "managed by CAPsMAN":
            _LOGGER.error("Unable to disable %s, managed by CAPsMAN", self._data[param])
            return "managed by CAPsMAN"
        if "-" in self._data["port-mac-address"]:
            param = "name"
        value = self._data[self.entity_description.data_reference]
        mod_param = self.entity_description.data_switch_parameter
        self.coordinator.set_value(path, param, value, mod_param, True)

        if "poe-out" in self._data and self._data["poe-out"] == "auto-on":
            path = "/interface/ethernet"
            self.coordinator.set_value(path, param, value, "poe-out", "off")

        await self.coordinator.async_refresh()


# ---------------------------
#   MikrotikNATSwitch
# ---------------------------
class MikrotikNATSwitch(MikrotikSwitch):
    """Representation of a NAT switch."""

    async def async_turn_on(self) -> None:
        """Turn on the switch."""
        if "write" not in self.coordinator.data["access"]:
            return

        path = self.entity_description.data_switch_path
        param = ".id"
        value = None
        for uid in self.coordinator.data["nat"]:
            if self.coordinator.data["nat"][uid]["uniq-id"] == (
                f"{self._data['chain']},{self._data['action']},{self._data['protocol']},"
                f"{self._data['in-interface']}:{self._data['dst-port']}-"
                f"{self._data['out-interface']}:{self._data['to-addresses']}:{self._data['to-ports']}"
            ):
                value = self.coordinator.data["nat"][uid][".id"]

        mod_param = self.entity_description.data_switch_parameter
        self.coordinator.set_value(path, param, value, mod_param, False)
        await self.coordinator.async_refresh()

    async def async_turn_off(self) -> None:
        """Turn off the switch."""
        if "write" not in self.coordinator.data["access"]:
            return

        path = self.entity_description.data_switch_path
        param = ".id"
        value = None
        for uid in self.coordinator.data["nat"]:
            if self.coordinator.data["nat"][uid]["uniq-id"] == (
                f"{self._data['chain']},{self._data['action']},{self._data['protocol']},"
                f"{self._data['in-interface']}:{self._data['dst-port']}-"
                f"{self._data['out-interface']}:{self._data['to-addresses']}:{self._data['to-ports']}"
            ):
                value = self.coordinator.data["nat"][uid][".id"]

        mod_param = self.entity_description.data_switch_parameter
        self.coordinator.set_value(path, param, value, mod_param, True)
        await self.coordinator.async_refresh()


# ---------------------------
#   MikrotikMangleSwitch
# ---------------------------
class MikrotikMangleSwitch(MikrotikSwitch):
    """Representation of a Mangle switch."""

    async def async_turn_on(self) -> None:
        """Turn on the switch."""
        if "write" not in self.coordinator.data["access"]:
            return

        path = self.entity_description.data_switch_path
        param = ".id"
        value = None
        for uid in self.coordinator.data["mangle"]:
            if self.coordinator.data["mangle"][uid]["uniq-id"] == (
                f"{self._data['chain']},{self._data['action']},{self._data['protocol']},"
                f"{self._data['src-address']}:{self._data['src-port']}-"
                f"{self._data['dst-address']}:{self._data['dst-port']},"
                f"{self._data['src-address-list']}-{self._data['dst-address-list']}"
            ):
                value = self.coordinator.data["mangle"][uid][".id"]

        mod_param = self.entity_description.data_switch_parameter
        self.coordinator.set_value(path, param, value, mod_param, False)
        await self.coordinator.async_refresh()

    async def async_turn_off(self) -> None:
        """Turn off the switch."""
        if "write" not in self.coordinator.data["access"]:
            return

        path = self.entity_description.data_switch_path
        param = ".id"
        value = None
        for uid in self.coordinator.data["mangle"]:
            if self.coordinator.data["mangle"][uid]["uniq-id"] == (
                f"{self._data['chain']},{self._data['action']},{self._data['protocol']},"
                f"{self._data['src-address']}:{self._data['src-port']}-"
                f"{self._data['dst-address']}:{self._data['dst-port']},"
                f"{self._data['src-address-list']}-{self._data['dst-address-list']}"
            ):
                value = self.coordinator.data["mangle"][uid][".id"]

        mod_param = self.entity_description.data_switch_parameter
        self.coordinator.set_value(path, param, value, mod_param, True)
        await self.coordinator.async_refresh()


# ---------------------------
#   MikrotikFilterSwitch
# ---------------------------
class MikrotikFilterSwitch(MikrotikSwitch):
    """Representation of a Filter switch."""

    async def async_turn_on(self) -> None:
        """Turn on the switch."""
        if "write" not in self.coordinator.data["access"]:
            return

        path = self.entity_description.data_switch_path
        param = ".id"
        value = None
        for uid in self.coordinator.data["filter"]:
            if self.coordinator.data["filter"][uid]["uniq-id"] == (
                f"{self._data['chain']},{self._data['action']},{self._data['protocol']},{self._data['layer7-protocol']},"
                f"{self._data['in-interface']},{self._data['in-interface-list']}:{self._data['src-address']},{self._data['src-address-list']}:{self._data['src-port']}-"
                f"{self._data['out-interface']},{self._data['out-interface-list']}:{self._data['dst-address']},{self._data['dst-address-list']}:{self._data['dst-port']}"
            ):
                value = self.coordinator.data["filter"][uid][".id"]

        mod_param = self.entity_description.data_switch_parameter
        self.coordinator.set_value(path, param, value, mod_param, False)
        await self.coordinator.async_refresh()

    async def async_turn_off(self) -> None:
        """Turn off the switch."""
        if "write" not in self.coordinator.data["access"]:
            return

        path = self.entity_description.data_switch_path
        param = ".id"
        value = None
        for uid in self.coordinator.data["filter"]:
            if self.coordinator.data["filter"][uid]["uniq-id"] == (
                f"{self._data['chain']},{self._data['action']},{self._data['protocol']},{self._data['layer7-protocol']},"
                f"{self._data['in-interface']},{self._data['in-interface-list']}:{self._data['src-address']},{self._data['src-address-list']}:{self._data['src-port']}-"
                f"{self._data['out-interface']},{self._data['out-interface-list']}:{self._data['dst-address']},{self._data['dst-address-list']}:{self._data['dst-port']}"
            ):
                value = self.coordinator.data["filter"][uid][".id"]

        mod_param = self.entity_description.data_switch_parameter
        self.coordinator.set_value(path, param, value, mod_param, True)
        await self.coordinator.async_refresh()


# ---------------------------
#   MikrotikQueueSwitch
# ---------------------------
class MikrotikQueueSwitch(MikrotikSwitch):
    """Representation of a queue switch."""

    async def async_turn_on(self) -> None:
        """Turn on the switch."""
        if "write" not in self.coordinator.data["access"]:
            return

        path = self.entity_description.data_switch_path
        param = ".id"
        value = None
        for uid in self.coordinator.data["queue"]:
            if self.coordinator.data["queue"][uid]["name"] == f"{self._data['name']}":
                value = self.coordinator.data["queue"][uid][".id"]

        mod_param = self.entity_description.data_switch_parameter
        self.coordinator.set_value(path, param, value, mod_param, False)
        await self.coordinator.async_refresh()

    async def async_turn_off(self) -> None:
        """Turn off the switch."""
        if "write" not in self.coordinator.data["access"]:
            return

        path = self.entity_description.data_switch_path
        param = ".id"
        value = None
        for uid in self.coordinator.data["queue"]:
            if self.coordinator.data["queue"][uid]["name"] == f"{self._data['name']}":
                value = self.coordinator.data["queue"][uid][".id"]

        mod_param = self.entity_description.data_switch_parameter
        self.coordinator.set_value(path, param, value, mod_param, True)
        await self.coordinator.async_refresh()


# ---------------------------
#   MikrotikKidcontrolPauseSwitch
# ---------------------------
class MikrotikKidcontrolPauseSwitch(MikrotikSwitch):
    """Representation of a queue switch."""

    async def async_turn_on(self) -> None:
        """Turn on the switch."""
        if "write" not in self.coordinator.data["access"]:
            return

        path = self.entity_description.data_switch_path
        param = self.entity_description.data_reference
        value = self._data[self.entity_description.data_reference]
        command = "resume"
        self.coordinator.execute(path, command, param, value)
        await self.coordinator.async_refresh()

    async def async_turn_off(self) -> None:
        """Turn off the switch."""
        if "write" not in self.coordinator.data["access"]:
            return

        path = self.entity_description.data_switch_path
        param = self.entity_description.data_reference
        value = self._data[self.entity_description.data_reference]
        command = "pause"
        self.coordinator.execute(path, command, param, value)
        await self.coordinator.async_refresh()


File: /custom_components\mikrotik_router\switch_types.py
"""Definitions for Mikrotik Router switch entities."""
from __future__ import annotations

from dataclasses import dataclass, field
from typing import List
from homeassistant.helpers.device_registry import CONNECTION_NETWORK_MAC
from homeassistant.components.switch import (
    SwitchDeviceClass,
    SwitchEntityDescription,
)

from .const import DOMAIN

DEVICE_ATTRIBUTES_IFACE = [
    "running",
    "enabled",
    "comment",
    "client-ip-address",
    "client-mac-address",
    "port-mac-address",
    "last-link-down-time",
    "last-link-up-time",
    "link-downs",
    "actual-mtu",
    "type",
    "name",
]

DEVICE_ATTRIBUTES_IFACE_ETHER = [
    "status",
    "auto-negotiation",
    "rate",
    "full-duplex",
    "default-name",
    "poe-out",
]

DEVICE_ATTRIBUTES_IFACE_SFP = [
    "status",
    "auto-negotiation",
    "advertising",
    "link-partner-advertising",
    "sfp-temperature",
    "sfp-supply-voltage",
    "sfp-module-present",
    "sfp-tx-bias-current",
    "sfp-tx-power",
    "sfp-rx-power",
    "sfp-rx-loss",
    "sfp-tx-fault",
    "sfp-type",
    "sfp-connector-type",
    "sfp-vendor-name",
    "sfp-vendor-part-number",
    "sfp-vendor-revision",
    "sfp-vendor-serial",
    "sfp-manufacturing-date",
    "eeprom-checksum",
]

DEVICE_ATTRIBUTES_IFACE_WIRELESS = [
    "ssid",
    "mode",
    "radio-name",
    "interface-type",
    "country",
    "installation",
    "antenna-gain",
    "frequency",
    "band",
    "channel-width",
    "secondary-frequency",
    "wireless-protocol",
    "rate-set",
    "distance",
    "tx-power-mode",
    "vlan-id",
    "wds-mode",
    "wds-default-bridge",
    "bridge-mode",
    "hide-ssid",
]

DEVICE_ATTRIBUTES_NAT = [
    "protocol",
    "dst-port",
    "in-interface",
    "to-addresses",
    "to-ports",
    "comment",
]

DEVICE_ATTRIBUTES_MANGLE = [
    "chain",
    "action",
    "passthrough",
    "protocol",
    "src-address",
    "src-port",
    "dst-address",
    "dst-port",
    "comment",
]

DEVICE_ATTRIBUTES_FILTER = [
    "chain",
    "action",
    "address-list",
    "protocol",
    "layer7-protocol",
    "tcp-flags",
    "connection-state",
    "in-interface",
    "src-address",
    "src-port",
    "out-interface",
    "dst-address",
    "dst-port",
    "comment",
]

DEVICE_ATTRIBUTES_PPP_SECRET = [
    "connected",
    "service",
    "profile",
    "comment",
    "caller-id",
    "encoding",
]

DEVICE_ATTRIBUTES_KIDCONTROL = [
    "blocked",
    "rate-limit",
    "mon",
    "tue",
    "wed",
    "thu",
    "fri",
    "sat",
    "sun",
]

DEVICE_ATTRIBUTES_QUEUE = [
    "target",
    "download-rate",
    "upload-rate",
    "download-max-limit",
    "upload-max-limit",
    "upload-limit-at",
    "download-limit-at",
    "upload-burst-limit",
    "download-burst-limit",
    "upload-burst-threshold",
    "download-burst-threshold",
    "upload-burst-time",
    "download-burst-time",
    "packet-marks",
    "parent",
    "comment",
]


@dataclass
class MikrotikSwitchEntityDescription(SwitchEntityDescription):
    """Class describing mikrotik entities."""

    device_class: str = SwitchDeviceClass.SWITCH

    icon_enabled: str | None = None
    icon_disabled: str | None = None
    ha_group: str | None = None
    ha_connection: str | None = None
    ha_connection_value: str | None = None
    data_path: str | None = None
    data_attribute: str = "enabled"
    data_switch_path: str | None = None
    data_switch_parameter: str = "disabled"
    data_name: str | None = None
    data_name_comment: bool = False
    data_uid: str | None = None
    data_reference: str | None = None
    data_attributes_list: List = field(default_factory=lambda: [])
    func: str = "MikrotikSwitch"


SENSOR_TYPES: tuple[MikrotikSensorEntityDescription, ...] = (
    MikrotikSwitchEntityDescription(
        key="interface",
        name="Port",
        icon_enabled="mdi:lan-connect",
        icon_disabled="mdi:lan-pending",
        entity_category=None,
        ha_group="data__default-name",
        ha_connection=CONNECTION_NETWORK_MAC,
        ha_connection_value="data__port-mac-address",
        data_path="interface",
        data_switch_path="/interface",
        data_name="default-name",
        data_uid="name",
        data_reference="default-name",
        data_attributes_list=DEVICE_ATTRIBUTES_IFACE,
        func="MikrotikPortSwitch",
    ),
    MikrotikSwitchEntityDescription(
        key="nat",
        name="",
        icon_enabled="mdi:network-outline",
        icon_disabled="mdi:network-off-outline",
        entity_category=None,
        ha_group="NAT",
        ha_connection=DOMAIN,
        ha_connection_value="NAT",
        data_path="nat",
        data_switch_path="/ip/firewall/nat",
        data_name="name",
        data_name_comment=True,
        data_uid="uniq-id",
        data_reference="uniq-id",
        data_attributes_list=DEVICE_ATTRIBUTES_NAT,
        func="MikrotikNATSwitch",
    ),
    MikrotikSwitchEntityDescription(
        key="mangle",
        name="",
        icon_enabled="mdi:bookmark-outline",
        icon_disabled="mdi:bookmark-off-outline",
        entity_category=None,
        ha_group="Mangle",
        ha_connection=DOMAIN,
        ha_connection_value="Mangle",
        data_path="mangle",
        data_switch_path="/ip/firewall/mangle",
        data_name="name",
        data_name_comment=True,
        data_uid="uniq-id",
        data_reference="uniq-id",
        data_attributes_list=DEVICE_ATTRIBUTES_MANGLE,
        func="MikrotikMangleSwitch",
    ),
    MikrotikSwitchEntityDescription(
        key="filter",
        name="",
        icon_enabled="mdi:filter-variant",
        icon_disabled="mdi:filter-variant-remove",
        entity_category=None,
        ha_group="Filter",
        ha_connection=DOMAIN,
        ha_connection_value="Filter",
        data_path="filter",
        data_switch_path="/ip/firewall/filter",
        data_name="name",
        data_name_comment=True,
        data_uid="uniq-id",
        data_reference="uniq-id",
        data_attributes_list=DEVICE_ATTRIBUTES_FILTER,
        func="MikrotikFilterSwitch",
    ),
    MikrotikSwitchEntityDescription(
        key="ppp_secret",
        name="PPP Secret",
        icon_enabled="mdi:account-outline",
        icon_disabled="mdi:account-off-outline",
        entity_category=None,
        ha_group="PPP",
        ha_connection=DOMAIN,
        ha_connection_value="PPP",
        data_path="ppp_secret",
        data_switch_path="/ppp/secret",
        data_name="name",
        data_uid="name",
        data_reference="name",
        data_attributes_list=DEVICE_ATTRIBUTES_PPP_SECRET,
    ),
    MikrotikSwitchEntityDescription(
        key="queue",
        name="",
        icon_enabled="mdi:leaf",
        icon_disabled="mdi:leaf-off",
        entity_category=None,
        ha_group="Queue",
        ha_connection=DOMAIN,
        ha_connection_value="Queue",
        data_path="queue",
        data_switch_path="/queue/simple",
        data_name="name",
        data_uid="name",
        data_reference="name",
        data_attributes_list=DEVICE_ATTRIBUTES_QUEUE,
        func="MikrotikQueueSwitch",
    ),
    MikrotikSwitchEntityDescription(
        key="kidcontrol_enable",
        name="",
        icon_enabled="mdi:account",
        icon_disabled="mdi:account-off",
        entity_category=None,
        ha_group="Kidcontrol",
        ha_connection=DOMAIN,
        ha_connection_value="Kidcontrol",
        data_path="kid-control",
        data_switch_path="/ip/kid-control",
        data_name="name",
        data_uid="name",
        data_reference="name",
        data_attributes_list=DEVICE_ATTRIBUTES_KIDCONTROL,
    ),
    MikrotikSwitchEntityDescription(
        key="kidcontrol_paused",
        name="paused",
        icon_enabled="mdi:account-outline",
        icon_disabled="mdi:account-off-outline",
        entity_category=None,
        ha_group="Kidcontrol",
        ha_connection=DOMAIN,
        ha_connection_value="Kidcontrol",
        data_path="kid-control",
        data_attribute="paused",
        data_switch_path="/ip/kid-control",
        data_name="name",
        data_uid="name",
        data_reference="name",
        data_attributes_list=DEVICE_ATTRIBUTES_KIDCONTROL,
        func="MikrotikKidcontrolPauseSwitch",
    ),
)

SENSOR_SERVICES = {}


File: /custom_components\mikrotik_router\translations\ar.json
{
    "config": {
        "step": {
            "user": {
                "title": "ضبط جهاز Mikrotik Router",
                "description": "إعداد دمج موجِّه (Mikrotik).",
                "data": {
                    "name": "اسم الدّمج",
                    "host": "المُضيف",
                    "port": "منفذ",
                    "username": "اسم المستخدم",
                    "password": "كلمة المرور",
                    "ssl": "استعمل طبقة الوصلات الآمنة (SSL)"
                }
            }
        },
        "error": {
            "name_exists": "الاسم موجود بالفعل.",
            "cannot_connect": "لا يمكن الاتصال بـ (Mikrotik).",
            "ssl_handshake_failure": "فشل تأكيد الاتصال (SSL)",
            "connection_timeout": "مهلة اتصال (Mikrotik).",
            "wrong_login": "خطأ في اسم المستخدم أو كلمة مرور."
        }
    },
    "options": {
        "step": {
            "basic_options": {
                "data": {
                    "scan_interval": "الفاصل الزمني للمسح الضوئي (يتطلب إعادة تشغيل HA)",
                    "track_iface_clients": "إظهار  عنوان التحكّم في الوسائط (MAC)  و بروتوكول الإنترنت (IP) للعميل على الواجهات",
                    "unit_of_measurement": "وحدة قياس",
                    "track_network_hosts_timeout": "مهلة تتبّع أجهزة الشبكة (بالثواني)",
                    "zone": "منطقة لتعقُّب الجهاز"
                },
                "title": "خيارات جهاز Mikrotik Router (1\/2)",
                "description": "تهيئة التكامل"
            },
            "sensor_select": {
                "data": {
                    "track_network_hosts": "تتبّع أجهزة الشبكة",
                    "sensor_port_tracker": "مُستشعرات تعقُب منفذ الشبكة",
                    "sensor_port_traffic": "مُستشعرات حركة المرور عبر منفذ الشبكة",
                    "sensor_client_traffic": "مُستشعرات حركة المرور على شبكات العميل",
                    "sensor_simple_queues": "مُبدِّل الاِصْطِفاف البسيط",
                    "sensor_nat": "مُبدِّلات ترجمة عنوان الشبكة",
                    "sensor_scripts": "مُبدِّلات النصوص",
                    "sensor_environment": "مُستشعرات متغير البيئة",
                    "sensor_kidcontrol": "مراقبة الأطفال",
                    "sensor_mangle": "مفاتيح المِكواة الأُسطوانية",
                    "sensor_ppp": "مستخدمي PPP",
                    "sensor_filter": "مفاتيح الترشيح",
                    "sensor_client_captive": "Captive portal data"
                },
                "title": "خيارات جهاز Mikrotik Router (2\/2)",
                "description": "تمكين أجهزة الاستشعار والمفاتيح"
            }
        }
    }
}

File: /custom_components\mikrotik_router\translations\cs.json
{
    "config": {
        "step": {
            "user": {
                "title": "Nastavit Mikrotik Router",
                "description": "Nastavte integraci Mikrotik Router.",
                "data": {
                    "name": "Název integrace",
                    "host": "Zařízení",
                    "port": "Port",
                    "username": "Uživatel",
                    "password": "Heslo",
                    "ssl": "Použití SSL"
                }
            }
        },
        "error": {
            "name_exists": "Název již existuje.",
            "cannot_connect": "Nelze se připojit k Mikrotiku.",
            "ssl_handshake_failure": "Selhání handshake SSL",
            "connection_timeout": "Časový limit připojení vypršel.",
            "wrong_login": "Neplatné uživatelské jméno nebo heslo."
        }
    },
    "options": {
        "step": {
            "basic_options": {
                "data": {
                    "scan_interval": "Interval skenování (vyžaduje restartování HA)",
                    "track_iface_clients": "Zobrazit klientské MAC a IP na rozhraních",
                    "unit_of_measurement": "Jednotka měření",
                    "track_network_hosts_timeout": "Časový limit sledování síťových zařízení (v sekundách)",
                    "zone": "Zóna pro sledování zařízení"
                },
                "title": "Nastavení Mikrotik Router (1\/2)",
                "description": "Konfigurovat integraci"
            },
            "sensor_select": {
                "data": {
                    "track_network_hosts": "Sledování síťových zařízení",
                    "sensor_port_tracker": "Senzory pro sledování portů",
                    "sensor_port_traffic": "Senzory provozu portu",
                    "sensor_client_traffic": "Senzory provozu klienta",
                    "sensor_simple_queues": "Přepínače jednoduchých front",
                    "sensor_nat": "Přepínače NAT",
                    "sensor_scripts": "Přepínače skriptů",
                    "sensor_environment": "Senzory prostředí",
                    "sensor_kidcontrol": "Dětská kontrola",
                    "sensor_mangle": "Mangle spínače",
                    "sensor_ppp": "Uživatelé PPP",
                    "sensor_filter": "Přepínače filtrů",
                    "sensor_client_captive": "Captive portál data"
                },
                "title": "Nastavení Mikrotik Router (2\/2)",
                "description": "Povolit senzory a přepínače"
            }
        }
    }
}

File: /custom_components\mikrotik_router\translations\de.json
{
    "config": {
        "step": {
            "user": {
                "title": "Mikrotik-Router einrichten",
                "description": "Mikrotik-Router-Integration einstellen",
                "data": {
                    "name": "Name der Integration",
                    "host": "Host",
                    "port": "Port",
                    "username": "Benutzername",
                    "password": "Passwort",
                    "ssl": "SSL benutzen"
                }
            }
        },
        "error": {
            "name_exists": "Name existiert bereits",
            "cannot_connect": "Verbindung zum MikroTik fehlgeschlagen.",
            "ssl_handshake_failure": "SSL Handshake Fehler",
            "connection_timeout": "Mikrotik-Verbindungstimeout.",
            "wrong_login": "Ungültiger Benutzername oder Passwort."
        }
    },
    "options": {
        "step": {
            "basic_options": {
                "data": {
                    "scan_interval": "Scan-Intervall (erfordert HA-Neustart)",
                    "track_iface_clients": "Client MAC und IP auf dem Interface anzeigen",
                    "unit_of_measurement": "Maßeinheit",
                    "track_network_hosts_timeout": "Zeitlimit für Netzwerkgeräte verfolgen (Sekunden)",
                    "zone": "Zone für Gerätetracker"
                },
                "title": "Mikrotik-Router-Optionen (1\/2)",
                "description": "Integration konfigurieren"
            },
            "sensor_select": {
                "data": {
                    "track_network_hosts": "Netzwerkgeräte verfolgen",
                    "sensor_port_tracker": "Port-Statussensoren",
                    "sensor_port_traffic": "Port-Durchsatz Sensoren",
                    "sensor_client_traffic": "Client-Durchsatz Sensoren",
                    "sensor_simple_queues": "Einfache Endschalter",
                    "sensor_nat": "NAT-Schalter",
                    "sensor_scripts": "Skript-Schalter",
                    "sensor_environment": "Umgebungsvariablen-Sensoren",
                    "sensor_kidcontrol": "Kindersicherung",
                    "sensor_mangle": "Mangle-Schalter",
                    "sensor_ppp": "PPP-Nutzer",
                    "sensor_filter": "Schalter für Filterregeln",
                    "sensor_client_captive": "Captive-Portal Daten"
                },
                "title": "Mikrotik-Router-Optionen (2\/2)",
                "description": "Sensoren und Schalter aktivieren"
            }
        }
    }
}

File: /custom_components\mikrotik_router\translations\el.json
{
    "config": {
        "step": {
            "user": {
                "title": "Ρύθμιση του Mikrotik Router",
                "description": "Ολοκλήρωση εγκατάστασης Mikrotik Router.",
                "data": {
                    "name": "Όνομα ολοκλήρωσης",
                    "host": "Εξυπηρετητής",
                    "port": "Θύρα",
                    "username": "Όνομα χρήστη",
                    "password": "Κωδικός πρόσβασης",
                    "ssl": "Χρήση SSL"
                }
            }
        },
        "error": {
            "name_exists": "Το όνομα υπάρχει ήδη.",
            "cannot_connect": "Αδυναμία σύνδεσης στον Mikrotik.",
            "ssl_handshake_failure": "Αποτυχίας χειραψίας SSL",
            "connection_timeout": "Διακοπή σύνδεσης με Mikrotik.",
            "wrong_login": "Το όνομα χρήστη και ο κωδικός πρόσβασης δεν είναι έγκυρα."
        }
    },
    "options": {
        "step": {
            "basic_options": {
                "data": {
                    "scan_interval": "Διάστημα σάρωσης (απαιτείται επανεκκίνηση του HA)",
                    "track_iface_clients": "Προβολή IP και MAC πελάτη στη διεπαφή",
                    "unit_of_measurement": "Μονάδα μέτρησης",
                    "track_network_hosts_timeout": "Εξωχρονισμός ανίχνευσης συσκευών διαδικτύου (δευτερόλεπτα)",
                    "zone": "Ζώνη για παρακολούθηση συσκευής"
                },
                "title": "Επιλογές Mikrotik Router (1\/2)",
                "description": "Διαμόρφωση ολοκλήρωσης"
            },
            "sensor_select": {
                "data": {
                    "track_network_hosts": "Ανίχνευση των συσκευών δικτύου",
                    "sensor_port_tracker": "Αισθητήρες παρακολούθησης θυρών",
                    "sensor_port_traffic": "Αισθητήρες κίνησης θυρών",
                    "sensor_client_traffic": "Αισθητήρες κίνησης πελατών",
                    "sensor_simple_queues": "Διακόπτες απλών ουρών",
                    "sensor_nat": "Διακόπτες NAT",
                    "sensor_scripts": "Διακόπτες δέσμης ενεργειών",
                    "sensor_environment": "Αισθητήρες μεταβολών περιβάλλοντος",
                    "sensor_kidcontrol": "Παιδικός έλεγχος",
                    "sensor_mangle": "Επιλογικοί διακόπτες",
                    "sensor_ppp": "Χρήστες PPP",
                    "sensor_filter": "Διακόπτες φίλτρου",
                    "sensor_client_captive": "Captive portal data"
                },
                "title": "Επιλογές Mikrotik Router (2\/2)",
                "description": "Ενεργοποίηση αισθητήρων και διακοπτών"
            }
        }
    }
}

File: /custom_components\mikrotik_router\translations\en.json
{
    "config": {
        "step": {
            "user": {
                "title": "Set up Mikrotik Router",
                "description": "Set up Mikrotik Router integration.",
                "data": {
                    "name": "Name of the integration",
                    "host": "Host",
                    "port": "Port",
                    "username": "Username",
                    "password": "Password",
                    "ssl": "Use SSL"
                }
            }
        },
        "error": {
            "name_exists": "Name already exists.",
            "cannot_connect": "Cannot connect to Mikrotik.",
            "ssl_handshake_failure": "SSL handshake failure",
            "connection_timeout": "Mikrotik connection timeout.",
            "wrong_login": "Invalid user name or password."
        }
    },
    "options": {
        "step": {
            "basic_options": {
                "data": {
                    "scan_interval": "Scan interval (requires HA restart)",
                    "track_iface_clients": "Show client MAC and IP on interfaces",
                    "unit_of_measurement": "Unit of measurement",
                    "track_network_hosts_timeout": "Track network devices timeout (seconds)",
                    "zone": "Zone for device tracker"
                },
                "title": "Mikrotik Router options (1\/2)",
                "description": "Configure integration"
            },
            "sensor_select": {
                "data": {
                    "track_network_hosts": "Track network devices",
                    "sensor_port_tracker": "Port tracker sensors",
                    "sensor_port_traffic": "Port traffic sensors",
                    "sensor_client_traffic": "Client traffic sensors",
                    "sensor_simple_queues": "Simple queues switches",
                    "sensor_nat": "NAT switches",
                    "sensor_scripts": "Script switches",
                    "sensor_environment": "Environment variable sensors",
                    "sensor_kidcontrol": "Kid control",
                    "sensor_mangle": "Mangle switches",
                    "sensor_ppp": "PPP users",
                    "sensor_filter": "Filter switches",
                    "sensor_client_captive": "Captive portal data"
                },
                "title": "Mikrotik Router options (2\/2)",
                "description": "Enable sensors and switches"
            }
        }
    }
}

File: /custom_components\mikrotik_router\translations\es.json
{
    "config": {
        "step": {
            "user": {
                "title": "Configurar un Mikrotik Router",
                "description": "Configura la integración del Mikrotik Router.",
                "data": {
                    "name": "Nombre de la integración",
                    "host": "Servidor",
                    "port": "Puerto",
                    "username": "Nombre de usuario",
                    "password": "Contraseña",
                    "ssl": "Usar SSL"
                }
            }
        },
        "error": {
            "name_exists": "El nombre ya existe.",
            "cannot_connect": "No es posible conectar con el Mikrotik.",
            "ssl_handshake_failure": "Fallo en el establecimiento de la comunicación SSL",
            "connection_timeout": "Conexión con Mikrotik sin respuesta.",
            "wrong_login": "Nombre de usuario o contraseña no válidos."
        }
    },
    "options": {
        "step": {
            "basic_options": {
                "data": {
                    "scan_interval": "Intervalo de escaneo (requiere reinicio de HA)",
                    "track_iface_clients": "Mostrar MAC e IP del cliente en las interfaces",
                    "unit_of_measurement": "Unidad de medida",
                    "track_network_hosts_timeout": "Monitorizar tiempo hasta desconexión automática de dispositivos de red (segundos)",
                    "zone": "Zona para seguimiento de dispositivo"
                },
                "title": "Opciones del Mikrotik Router (1\/2)",
                "description": "Configurar la integración"
            },
            "sensor_select": {
                "data": {
                    "track_network_hosts": "Monitorizar dispositivos de red",
                    "sensor_port_tracker": "Sensores de seguimiento de puertos",
                    "sensor_port_traffic": "Sensores de tráfico de puertos",
                    "sensor_client_traffic": "Sensores de tráfico de clientes",
                    "sensor_simple_queues": "Interruptores de cola sencillos",
                    "sensor_nat": "Interruptores NAT",
                    "sensor_scripts": "Interruptores de script",
                    "sensor_environment": "Sensores variables de entorno",
                    "sensor_kidcontrol": "Control de niños",
                    "sensor_mangle": "Interruptor Mangle",
                    "sensor_ppp": "Usuarios PPP",
                    "sensor_filter": "Filtros de interruptores",
                    "sensor_client_captive": "Captive portal data"
                },
                "title": "Opciones del Mikrotik Router 2\/2)",
                "description": "Activar sensores e interruptores"
            }
        }
    }
}

File: /custom_components\mikrotik_router\translations\es_ES.json
{
    "config": {
        "step": {
            "user": {
                "title": "Configurar un Mikrotik Router",
                "description": "Configura la integración del Mikrotik Router.",
                "data": {
                    "name": "Nombre de la integración",
                    "host": "Proveedor",
                    "port": "Puerto",
                    "username": "Nombre de usuario",
                    "password": "Contraseña",
                    "ssl": "Utilizar SSL"
                }
            }
        },
        "error": {
            "name_exists": "El nombre ya existe.",
            "cannot_connect": "No puede conectarse a Mikrotik.",
            "ssl_handshake_failure": "Fallo del \"handshake\" SSL",
            "connection_timeout": "Tiempo de espera de la conexión a Mikrotik.",
            "wrong_login": "Nombre de usuario o contraseña no válida"
        }
    },
    "options": {
        "step": {
            "basic_options": {
                "data": {
                    "scan_interval": "Escanear intervalo (requiere reinicio de HA)",
                    "track_iface_clients": "Mostrar MAC e IP de cliente en las interfaces",
                    "unit_of_measurement": "Unidad de medida",
                    "track_network_hosts_timeout": "Rastrear el tiempo de espera de los dispositivos de red (segundos)",
                    "zone": "Zona para rastreador de dispositivos"
                },
                "title": "Opciones del Mikrotik Router (1\/2)",
                "description": "Configurar la integración"
            },
            "sensor_select": {
                "data": {
                    "track_network_hosts": "Rastrear dispositivos de red",
                    "sensor_port_tracker": "Sensores de seguimiento portuario",
                    "sensor_port_traffic": "Sensores de tráfico portuario",
                    "sensor_client_traffic": "Sensores de tráfico de clientes",
                    "sensor_simple_queues": "Interruptores de cola sencillos",
                    "sensor_nat": "Interruptores NAT",
                    "sensor_scripts": "Interruptores de script",
                    "sensor_environment": "Sensores de variable de entorno",
                    "sensor_kidcontrol": "Control parental",
                    "sensor_mangle": "Conmutadores de mangle",
                    "sensor_ppp": "Usuarios PPP",
                    "sensor_filter": "Conmutadores de filtro",
                    "sensor_client_captive": "Datos portal cautivo"
                },
                "title": "Opciones del Mikrotik Router (2\/2)",
                "description": "Activar sensores e interruptores"
            }
        }
    }
}

File: /custom_components\mikrotik_router\translations\fr.json
{
    "config": {
        "step": {
            "user": {
                "title": "Configurer Mikrotik Router",
                "description": "Configurer l'intégration de Mikrotik Router.",
                "data": {
                    "name": "Nom de l'intégration",
                    "host": "Hôte",
                    "port": "Port",
                    "username": "Identifiant",
                    "password": "Mot de passe",
                    "ssl": "Utiliser SSL"
                }
            }
        },
        "error": {
            "name_exists": "Le nom existe déjà.",
            "cannot_connect": "Impossible de se connecter à Mikrotik.",
            "ssl_handshake_failure": "Échec de la négociation SSL",
            "connection_timeout": "Expiration de connexion Mikrotik.",
            "wrong_login": "Identifiant ou mot de passe invalide."
        }
    },
    "options": {
        "step": {
            "basic_options": {
                "data": {
                    "scan_interval": "Intervalle d'analyse (nécessite le redémarrage HA)",
                    "track_iface_clients": "Afficher l'IP et le MAC du client sur les interfaces",
                    "unit_of_measurement": "Unité de mesure",
                    "track_network_hosts_timeout": "Suivre l'expiration des appareils du réseau (secondes)",
                    "zone": "Zone pour le traceur d'appareil"
                },
                "title": "Options Mikrotik Router (1\/2)",
                "description": "Configurer l'intégration"
            },
            "sensor_select": {
                "data": {
                    "track_network_hosts": "Suivre les appareils du réseau",
                    "sensor_port_tracker": "Capteurs de suivi de ports",
                    "sensor_port_traffic": "Capteurs de trafic par ports",
                    "sensor_client_traffic": "Capteurs de trafic de clients",
                    "sensor_simple_queues": "Commutateurs de files d'attente simples",
                    "sensor_nat": "Commutateurs NAT",
                    "sensor_scripts": "Commutation de scripts",
                    "sensor_environment": "Capteurs de variables d'environnement",
                    "sensor_kidcontrol": "Contrôle parental",
                    "sensor_mangle": "Commutateurs Mangle",
                    "sensor_ppp": "Utilisateurs PPP",
                    "sensor_filter": "Sélecteurs de filtre",
                    "sensor_client_captive": "Captive portal data"
                },
                "title": "Options Mikrotik Router (2\/2)",
                "description": "Activer les capteurs et les interrupteurs"
            }
        }
    }
}

File: /custom_components\mikrotik_router\translations\hi_IN.json
{
    "config": {
        "step": {
            "user": {
                "title": "मिकरोटिक राउटर सेट करें",
                "description": "Mikrotik राउटर इन्टीग्रेशन सेट अप करें।",
                "data": {
                    "name": "इन्टीग्रेशन का नाम",
                    "host": "होस्ट",
                    "port": "पोर्ट",
                    "username": "उपयोगकर्ता नाम",
                    "password": "पासवर्ड",
                    "ssl": "SSL का उपयोग करें"
                }
            }
        },
        "error": {
            "name_exists": "नाम पहले से मौजूद है।",
            "cannot_connect": "Mikrotik से कनेक्ट नही कर सकते।",
            "ssl_handshake_failure": "SSL हैन्डशेक विफ़ल हो गया",
            "connection_timeout": "Mikrotik कनेक्शन टाइम आउट हो गया।",
            "wrong_login": "अमान्य उपयोगकर्ता नाम या पासवर्ड।"
        }
    },
    "options": {
        "step": {
            "basic_options": {
                "data": {
                    "scan_interval": "स्कैन अन्तराल (HA रिस्टार्ट आवश्यक है)",
                    "track_iface_clients": "ग्राहक का MAC और IP इन्टरफ़ेस पर दिखाएं",
                    "unit_of_measurement": "माप का युनीट",
                    "track_network_hosts_timeout": "नेटवर्क डिवाइस ट्रैक टाइम आउट (सेकन्ड)",
                    "zone": "डिवाइस ट्रैकर के लिए ज़ोन"
                },
                "title": "Mikrotik Router के विकल्प (1\/2)",
                "description": "इंटीग्रेशन को कॉन्फ़िगर करें"
            },
            "sensor_select": {
                "data": {
                    "track_network_hosts": "नेटवर्क डिवाइस को ट्रैक करें",
                    "sensor_port_tracker": "पोर्ट ट्रैकर सेंसर",
                    "sensor_port_traffic": "पोर्ट ट्रैफ़िक सेंसर",
                    "sensor_client_traffic": "क्लाइंट ट्रैफ़िक सेंसर",
                    "sensor_simple_queues": "सामान्य कतार स्विच",
                    "sensor_nat": "NAT स्विच",
                    "sensor_scripts": "स्क्रिप्ट स्विच",
                    "sensor_environment": "पारिस्थितिक वेरिएबल सेंसर",
                    "sensor_kidcontrol": "बच्चे के लिए कंट्रोल",
                    "sensor_mangle": "मैंगल स्विच",
                    "sensor_ppp": "PPP यूज़र",
                    "sensor_filter": "फ़िल्टर स्विच",
                    "sensor_client_captive": "Captive portal data"
                },
                "title": "Mikrotik Router के विकल्प (2\/2)",
                "description": "सेंसर और स्विच को एनेबल करें"
            }
        }
    }
}

File: /custom_components\mikrotik_router\translations\hu.json
{
    "config": {
        "step": {
            "user": {
                "title": "Állítsa fel a Mikrotik Router",
                "description": "Állítsd be a Mikrotik Router integrációt.",
                "data": {
                    "name": "Integráció neve",
                    "host": "Hoszt",
                    "port": "Port",
                    "username": "Felhasználónév",
                    "password": "Jelszó",
                    "ssl": "SSL használata"
                }
            }
        },
        "error": {
            "name_exists": "A név már létezik.",
            "cannot_connect": "Nem lehet csatlakozni a Mikrotikhez.",
            "ssl_handshake_failure": "SSL-kézfogás sikertelen",
            "connection_timeout": "Mikrotik kapcsolat időtúllépés.",
            "wrong_login": "Érvénytelen felhasználónév vagy jelszó."
        }
    },
    "options": {
        "step": {
            "basic_options": {
                "data": {
                    "scan_interval": "Felderítési időköz (HA újraindítása szükséges)",
                    "track_iface_clients": "Ügyfél MAC- és IP-címének mutatása az interfészeken",
                    "unit_of_measurement": "Mértékegység",
                    "track_network_hosts_timeout": "Hálózati eszközök követésének időtúllépése (másodperc)",
                    "zone": "Zóna az eszközkövető számára"
                },
                "title": "Mikrotik Router opciók (1\/2)",
                "description": "Az integráció konfigurálása"
            },
            "sensor_select": {
                "data": {
                    "track_network_hosts": "Hálózati eszközök követése",
                    "sensor_port_tracker": "Portfigyelő érzékelők",
                    "sensor_port_traffic": "Portforgalom érzékelők",
                    "sensor_client_traffic": "Kliensforgalom érzékelők",
                    "sensor_simple_queues": "Simple queue kapcsolók",
                    "sensor_nat": "NAT kapcsolók",
                    "sensor_scripts": "Szkript kapcsolók",
                    "sensor_environment": "Környezeti változó érzékelők",
                    "sensor_kidcontrol": "Szülői felügyelet",
                    "sensor_mangle": "Mangle kapcsolók",
                    "sensor_ppp": "PPP felhasználók",
                    "sensor_filter": "Szűrő kapcsolók",
                    "sensor_client_captive": "Captive portal data"
                },
                "title": "Mikrotik Router opciók (2\/2)",
                "description": "Érzékelők és kapcsolók engedélyezése"
            }
        }
    }
}

File: /custom_components\mikrotik_router\translations\is_IS.json
{
    "config": {
        "step": {
            "user": {
                "title": "Setja upp Mikrotik Router",
                "description": "Setja upp Mikrotik Router samþættingu.",
                "data": {
                    "name": "Heiti samþættingar",
                    "host": "Hýsill",
                    "port": "Port",
                    "username": "Notandanafn",
                    "password": "Lykilorð",
                    "ssl": "Nota SSL"
                }
            }
        },
        "error": {
            "name_exists": "Nafn er þegar til.",
            "cannot_connect": "Get ekki tengst Mikrotik.",
            "ssl_handshake_failure": "Villa við að koma á SSL samskiptum",
            "connection_timeout": "Tengin við Mikrotik rann út á tíma.",
            "wrong_login": "Ógilt notendanafn eða lykilorð."
        }
    },
    "options": {
        "step": {
            "basic_options": {
                "data": {
                    "scan_interval": "Tíðni skönnunar ( krefst endurræsingar á HA )",
                    "track_iface_clients": "Sýna MAC og IP vistfang fyrir biðlara á netkortum",
                    "unit_of_measurement": "Mælieining",
                    "track_network_hosts_timeout": "Tímamörk við rakningu á netbúnaði ( sekúndur )",
                    "zone": "Svæði fyrir tækjarakningu"
                },
                "title": "Mikrotik Router valkostir (1\/2)",
                "description": "Stilla samþættingu"
            },
            "sensor_select": {
                "data": {
                    "track_network_hosts": "Rekja netbúnað",
                    "sensor_port_tracker": "Port rakningarskynjarar",
                    "sensor_port_traffic": "Port umferðarskynjarar",
                    "sensor_client_traffic": "Biðlaraumferð skynjarar",
                    "sensor_simple_queues": "Einfaldir biðraðir rofar",
                    "sensor_nat": "NAT rofar",
                    "sensor_scripts": "Skrifturofar",
                    "sensor_environment": "Umhverfisbreytu skynjarar",
                    "sensor_kidcontrol": "Krakkastjórnun",
                    "sensor_mangle": "Bjögunarrofi",
                    "sensor_ppp": "PPP notendur",
                    "sensor_filter": "Síurofar",
                    "sensor_client_captive": "Captive portal data"
                },
                "title": "Mikrotik Router valkostir (2\/2)",
                "description": "Virkja skynjara og rofa"
            }
        }
    }
}

File: /custom_components\mikrotik_router\translations\it.json
{
    "config": {
        "step": {
            "user": {
                "title": "Configurare il Mikrotik Router",
                "description": "Imposta integrazione Mikrotik Router",
                "data": {
                    "name": "Nome integrazione",
                    "host": "Host",
                    "port": "Porta",
                    "username": "Nome utente",
                    "password": "Password",
                    "ssl": "Usa SSL"
                }
            }
        },
        "error": {
            "name_exists": "Nome già esistente.",
            "cannot_connect": "Impossibile connettersi a Mikrotik.",
            "ssl_handshake_failure": "Errore SSL handshake",
            "connection_timeout": "Timeout connessione Mikrotik.",
            "wrong_login": "Nome utente o password non validi."
        }
    },
    "options": {
        "step": {
            "basic_options": {
                "data": {
                    "scan_interval": "Intervallo scansione (richiede riavvio HA)",
                    "track_iface_clients": "Mostra client MAC e IP sulle interfacce",
                    "unit_of_measurement": "Unità di misura",
                    "track_network_hosts_timeout": "Traccia timeout dei dispositivi di rete (secondi)",
                    "zone": "Zona per localizzatore dispositivo"
                },
                "title": "Opzioni Mikrotik Router (1\/2)",
                "description": "Configura integrazione"
            },
            "sensor_select": {
                "data": {
                    "track_network_hosts": "Traccia dispositivi di rete",
                    "sensor_port_tracker": "Sensori di tracciamento della porta",
                    "sensor_port_traffic": "Sensori di traffico della porta",
                    "sensor_client_traffic": "Sensori di traffico del client",
                    "sensor_simple_queues": "Commutatori di code semplici",
                    "sensor_nat": "Commutatori NAT",
                    "sensor_scripts": "Commutatori di script",
                    "sensor_environment": "Sensori di variabili ambientali",
                    "sensor_kidcontrol": "Controllo bambini",
                    "sensor_mangle": "Interruttori a manganello",
                    "sensor_ppp": "Utenti PPP",
                    "sensor_filter": "Interruttori del filtro",
                    "sensor_client_captive": "Captive portal data"
                },
                "title": "Opzioni Mikrotik Router (2\/2)",
                "description": "Abilita sensori e interruttori"
            }
        }
    }
}

File: /custom_components\mikrotik_router\translations\ja.json
{
    "config": {
        "step": {
            "user": {
                "title": "Mikrotik Routerのセットアップ",
                "description": "Mikrotikルータ統合をセットアップします。",
                "data": {
                    "name": "統合名",
                    "host": "ホスト",
                    "port": "ポート",
                    "username": "ユーザ名",
                    "password": "パスワード",
                    "ssl": "SSLを使用します"
                }
            }
        },
        "error": {
            "name_exists": "名前は既に存在します。",
            "cannot_connect": "Mikrotikに接続できません。",
            "ssl_handshake_failure": "SSLハンドシェイクに失敗しました",
            "connection_timeout": "Mikrotik接続がタイムアウトしました。",
            "wrong_login": "ユーザ名またはパスワードが無効です。"
        }
    },
    "options": {
        "step": {
            "basic_options": {
                "data": {
                    "scan_interval": "スキャン間隔（HAの再起動が必要）",
                    "track_iface_clients": "クライアントのMACとインターフェイスのIPを表示します",
                    "unit_of_measurement": "測定単位",
                    "track_network_hosts_timeout": "ネットワーク デバイスのタイムアウト（秒）をトラッキングします",
                    "zone": "デバイス追跡装置用ゾーン"
                },
                "title": "Mikrotik Router オプション (1\/2)",
                "description": "インテグレーションを設定する"
            },
            "sensor_select": {
                "data": {
                    "track_network_hosts": "ネットワーク デバイスをトラッキングします",
                    "sensor_port_tracker": "ポートトラッカーセンサー",
                    "sensor_port_traffic": "ポートトラフィックセンサー",
                    "sensor_client_traffic": "クライアントトラフィックセンサー",
                    "sensor_simple_queues": "単純キュースイッチ",
                    "sensor_nat": "NAT スイッチ",
                    "sensor_scripts": "スクリプトスイッチ",
                    "sensor_environment": "環境変数センサー",
                    "sensor_kidcontrol": "キッドコントロール",
                    "sensor_mangle": "マングルスイッチ",
                    "sensor_ppp": "PPPユーザー",
                    "sensor_filter": "フィルタースイッチ",
                    "sensor_client_captive": "Captive portal data"
                },
                "title": "Mikrotik Router オプション (2\/2)",
                "description": "センサーとスイッチを有効にする"
            }
        }
    }
}

File: /custom_components\mikrotik_router\translations\ko.json
{
    "config": {
        "step": {
            "user": {
                "title": "Mikrotik Router 설정",
                "description": "Mikrotik 라우터 통합을 설정합니다.",
                "data": {
                    "name": "통합 이름",
                    "host": "호스트",
                    "port": "포트",
                    "username": "사용자 이름",
                    "password": "비밀번호",
                    "ssl": "SSL 사용"
                }
            }
        },
        "error": {
            "name_exists": "존재하는 이름입니다.",
            "cannot_connect": "Mikrotik에 연결할 수 없습니다.",
            "ssl_handshake_failure": "SSL 핸드셰이크 실패",
            "connection_timeout": "Mikrotik 연결 시간이 초과되었습니다.",
            "wrong_login": "사용자 이름 또는 비밀번호가 유효하지 않습니다."
        }
    },
    "options": {
        "step": {
            "basic_options": {
                "data": {
                    "scan_interval": "스캔 간격(HA 재시작 필요)",
                    "track_iface_clients": "인터페이스에 클라이언트 MAC 및 IP 표시",
                    "unit_of_measurement": "측정 단위",
                    "track_network_hosts_timeout": "네트워크 기기 시간 초과 추적(초)",
                    "zone": "기기 추적기용 지역"
                },
                "title": "Mikrotik Router 옵션(1\/2)",
                "description": "통합 환경설정"
            },
            "sensor_select": {
                "data": {
                    "track_network_hosts": "네트워크 기기 추적",
                    "sensor_port_tracker": "트래커 센서 복사",
                    "sensor_port_traffic": "트래픽 센서 복사",
                    "sensor_client_traffic": "클라이언트 트래픽 센서",
                    "sensor_simple_queues": "단순 대기열 스위치",
                    "sensor_nat": "내트 스위치",
                    "sensor_scripts": "스크립트 스위치",
                    "sensor_environment": "환경 변수 센서",
                    "sensor_kidcontrol": "어린이 이용 제어",
                    "sensor_mangle": "맹글 스위치",
                    "sensor_ppp": "PPP 사용자",
                    "sensor_filter": "필터 스위치",
                    "sensor_client_captive": "Captive portal data"
                },
                "title": "Mikrotik Router 옵션(2\/2)",
                "description": "센서 및 스위치 활성화"
            }
        }
    }
}

File: /custom_components\mikrotik_router\translations\lv.json
{
    "config": {
        "step": {
            "user": {
                "title": "Lestatiet Mikrotik Router",
                "description": "Mikrotik maršrutētāja integrācijas konfigurēšana.",
                "data": {
                    "name": "Integrācijas nosaukums",
                    "host": "Maršrutētāja adrese",
                    "port": "Ports",
                    "username": "Lietotājvārds",
                    "password": "Parole",
                    "ssl": "Izmantot SSL"
                }
            }
        },
        "error": {
            "name_exists": "Nosaukums jau eksistē.",
            "cannot_connect": "Neizdodas savienoties ar Mikrotik.",
            "ssl_handshake_failure": "SSL savienojuma kļūda",
            "connection_timeout": "Mikrotik savienojuma noilgums.",
            "wrong_login": "Nederīgs lietotājvārds vai parole."
        }
    },
    "options": {
        "step": {
            "basic_options": {
                "data": {
                    "scan_interval": "Skenēšanas periods (nepieciešama HA restartēšana)",
                    "track_iface_clients": "Rādīt klienta MAC un IP interfeisā",
                    "unit_of_measurement": "Mērvienības",
                    "track_network_hosts_timeout": "Tīkla ierīces uzraudzības noilgums (sekundēs)",
                    "zone": "Lerīces izsekotāja zona"
                },
                "title": "Mikrotik Router opcijas (1\/2)",
                "description": "Konfigurēt integrāciju"
            },
            "sensor_select": {
                "data": {
                    "track_network_hosts": "Tīkla ierīču izsekošana",
                    "sensor_port_tracker": "Porta izsekošanas sensori",
                    "sensor_port_traffic": "Porta datu plūsmas sensori",
                    "sensor_client_traffic": "Klientu datu plūsmas sensori",
                    "sensor_simple_queues": "Vienkāršo rindu slēdži",
                    "sensor_nat": "NAT kārtulu slēdži",
                    "sensor_scripts": "Skriptu slēdži",
                    "sensor_environment": "Mainīgie vides sensori",
                    "sensor_kidcontrol": "Bērnu kontrole",
                    "sensor_mangle": "Manglu slēdži",
                    "sensor_ppp": "PPP lietotāji",
                    "sensor_filter": "Filtra slēdži",
                    "sensor_client_captive": "Captive portal data"
                },
                "title": "Mikrotik Router opcijas (2\/2)",
                "description": "Sensoru un slēdžu aktivizēšana"
            }
        }
    }
}

File: /custom_components\mikrotik_router\translations\nl.json
{
    "config": {
        "step": {
            "user": {
                "title": "Mikrotik Router instellen",
                "description": "Stel Mikrotik Router-integratie in.",
                "data": {
                    "name": "Naam van de integratie",
                    "host": "Host",
                    "port": "Poort",
                    "username": "Gebruikersnaam",
                    "password": "Wachtwoord",
                    "ssl": "Gebruik SSL"
                }
            }
        },
        "error": {
            "name_exists": "Naam al in gebruik",
            "cannot_connect": "Kan geen verbinding maken met Mikrotik.",
            "ssl_handshake_failure": "SSL overeenkomings-storing",
            "connection_timeout": "Mikrotik verbinding time-out.",
            "wrong_login": "Ongeldige gebruikersnaam of wachtwoord."
        }
    },
    "options": {
        "step": {
            "basic_options": {
                "data": {
                    "scan_interval": "Scaninterval (vereist opnieuw opstarten van HA)",
                    "track_iface_clients": "Mac en IP van client weergeven op interfaces",
                    "unit_of_measurement": "Meet eenheid",
                    "track_network_hosts_timeout": "Volg de time-out van netwerkapparaten (seconden)",
                    "zone": "Zone voor apparaattracker"
                },
                "title": "Opties Mikrotik Router (1\/2)",
                "description": "Integratie configureren"
            },
            "sensor_select": {
                "data": {
                    "track_network_hosts": "Volg netwerkapparaten",
                    "sensor_port_tracker": "Poorttrackersensors",
                    "sensor_port_traffic": "Poortverkeersensors",
                    "sensor_client_traffic": "Clientverkeersensors",
                    "sensor_simple_queues": "Eenvoudige wachtrijswitches",
                    "sensor_nat": "NAT-switches",
                    "sensor_scripts": "Script-switches",
                    "sensor_environment": "Omgevingsvariabelesensors",
                    "sensor_kidcontrol": "Kindercontrole",
                    "sensor_mangle": "Mangelschakelaars",
                    "sensor_ppp": "PPP-gebruikers",
                    "sensor_filter": "Filterschakelaars",
                    "sensor_client_captive": "Captive portal data"
                },
                "title": "Opties Mikrotik Router (2\/2)",
                "description": "Sensoren en schakelaars inschakelen"
            }
        }
    }
}

File: /custom_components\mikrotik_router\translations\no.json
{
    "config": {
        "step": {
            "user": {
                "title": "Sett opp Mikrotik router",
                "description": "Sett opp Mikrotik Router integrasjon",
                "data": {
                    "name": "Navn på integreringen",
                    "host": "Adresse",
                    "port": "Port",
                    "username": "Brukernavn",
                    "password": "Passord",
                    "ssl": "Bruk SSL"
                }
            }
        },
        "error": {
            "name_exists": "Navnet eksisterer allerede",
            "cannot_connect": "Kunne ikke koble til Mikrotik",
            "ssl_handshake_failure": "SSH håndtrykkfeil",
            "connection_timeout": "Mikrotik tilkoblingen fikk tidsavbrudd",
            "wrong_login": "Feil brukernavn og\/eller passord"
        }
    },
    "options": {
        "step": {
            "basic_options": {
                "data": {
                    "scan_interval": "Søke interval (krever HA omstart)",
                    "track_iface_clients": "Vis klient MAC og IP på grensesnittet",
                    "unit_of_measurement": "Måleenhet",
                    "track_network_hosts_timeout": "Spor nettverks enhet tidsavbrudd (sekunder)",
                    "zone": "Sone for enhetssporer"
                },
                "title": "Mikrotik Router alternativer",
                "description": "Konfigurer integrasjon"
            },
            "sensor_select": {
                "data": {
                    "track_network_hosts": "Spor nettverksenheter",
                    "sensor_port_tracker": "Port sporings sensorer",
                    "sensor_port_traffic": "Port trafikk sensorer",
                    "sensor_client_traffic": "Klient trafikk sensorer",
                    "sensor_simple_queues": "Enklel kø brytere",
                    "sensor_nat": "NAT Brytere",
                    "sensor_scripts": "Script brytere",
                    "sensor_environment": "Miljøvariabel sensorer",
                    "sensor_kidcontrol": "Barnekontroll",
                    "sensor_mangle": "Mangle brytere",
                    "sensor_ppp": "PPP Brukere",
                    "sensor_filter": "Filter brytere",
                    "sensor_client_captive": "Captive portal data"
                },
                "title": "Mikrotik Router options (2\/2)",
                "description": "Skru på sensorer og brytere"
            }
        }
    }
}

File: /custom_components\mikrotik_router\translations\pl.json
{
    "config": {
        "step": {
            "user": {
                "title": "Skonfiguruj Mikrotik Router",
                "description": "Skonfiguruj integrację z Mikrotik Router.",
                "data": {
                    "name": "Nazwa integracji",
                    "host": "Host",
                    "port": "Port",
                    "username": "Nazwa użytkownika",
                    "password": "Hasło",
                    "ssl": "Użyj SSL"
                }
            }
        },
        "error": {
            "name_exists": "Nazwa już istnieje",
            "cannot_connect": "Nie można połączyć się z Mikrotik.",
            "ssl_handshake_failure": "Błąd uzgadniania SSL",
            "connection_timeout": "Limit czasu dla połączenia Mikrotik został przekroczony.",
            "wrong_login": "Nieprawidłowa nazwa użytkownika lub hasło."
        }
    },
    "options": {
        "step": {
            "basic_options": {
                "data": {
                    "scan_interval": "Częstotliwość skanowania (wymaga ponownego uruchomienia HA)",
                    "track_iface_clients": "Pokaż w interfejsach adres MAC i IP klienta",
                    "unit_of_measurement": "Jednostka miary",
                    "track_network_hosts_timeout": "Śledź limity czasu dla urządzeń sieciowych (sekundy)",
                    "zone": "Strefa programu do śledzenia urządzeń"
                },
                "title": "Opcje Mikrotik Router (1\/2)",
                "description": "Skonfiguruj integrację"
            },
            "sensor_select": {
                "data": {
                    "track_network_hosts": "Śledź urządzenia sieciowe",
                    "sensor_port_tracker": "Czujniki monitora portu",
                    "sensor_port_traffic": "Czujniki ruchu portowego",
                    "sensor_client_traffic": "Czujniki ruchu klienta",
                    "sensor_simple_queues": "Przełączniki prostych kolejek",
                    "sensor_nat": "Przełączniki NAT",
                    "sensor_scripts": "Przełączniki skryptów",
                    "sensor_environment": "Czujniki zmiennych środowiskowych",
                    "sensor_kidcontrol": "Kontrola rodzicielska",
                    "sensor_mangle": "Przełączniki mangle",
                    "sensor_ppp": "Użytkownicy PPP",
                    "sensor_filter": "Przełączniki filtrów",
                    "sensor_client_captive": "Captive portal data"
                },
                "title": "Opcje Mikrotik Router (2\/2)",
                "description": "Włącz czujniki i przełączniki"
            }
        }
    }
}

File: /custom_components\mikrotik_router\translations\pt.json
{
    "config": {
        "step": {
            "user": {
                "title": "Configurar o Mikrotik Router",
                "description": "Configurar a integração do Mikrotik Router.",
                "data": {
                    "name": "Nome da integração",
                    "host": "Anfitrião",
                    "port": "Porta",
                    "username": "Nome de utilizador",
                    "password": "Palavra-passe",
                    "ssl": "Usar SSL"
                }
            }
        },
        "error": {
            "name_exists": "O nome já existe.",
            "cannot_connect": "Não é possível ligar à Mikrotik.",
            "ssl_handshake_failure": "Falha no reconhecimento SSL",
            "connection_timeout": "Tempo limite da ligação à Mikrotik.",
            "wrong_login": "Nome de utilizador ou palavra-passe inválidos."
        }
    },
    "options": {
        "step": {
            "basic_options": {
                "data": {
                    "scan_interval": "Intervalo de verificação (requer reinicialização de HA)",
                    "track_iface_clients": "Mostrar MAC e IP do cliente nas interfaces",
                    "unit_of_measurement": "Unidade de medida",
                    "track_network_hosts_timeout": "Rastrear o tempo limite dos dispositivos de rede (segundos)",
                    "zone": "Zona para o rastreador do dispositivo"
                },
                "title": "Opções do Mikrotik Router (1\/2)",
                "description": "Configurar integração"
            },
            "sensor_select": {
                "data": {
                    "track_network_hosts": "Rastrear dispositivos de rede",
                    "sensor_port_tracker": "Sensores de rastreamento das portas",
                    "sensor_port_traffic": "Sensores de tráfego das portas",
                    "sensor_client_traffic": "Sensores de tráfego do cliente",
                    "sensor_simple_queues": "Comutadores simples de filas de espera",
                    "sensor_nat": "Comutadores NAT",
                    "sensor_scripts": "Comutadores de script",
                    "sensor_environment": "Sensores de variáveis de ambiente",
                    "sensor_kidcontrol": "Controlo de crianças",
                    "sensor_mangle": "Interruptores mangle",
                    "sensor_ppp": "Utilizadores PPP",
                    "sensor_filter": "Interruptores de filtro",
                    "sensor_client_captive": "Captive portal data"
                },
                "title": "Opções do Mikrotik Router (2\/2)",
                "description": "Ativar sensores e interruptores"
            }
        }
    }
}

File: /custom_components\mikrotik_router\translations\pt_BR.json
{
    "config": {
        "step": {
            "user": {
                "title": "Configuração do Mikrotik Router",
                "description": "Configurando uma integração de roteador (Mikrotik).",
                "data": {
                    "name": "Nome da mesclagem",
                    "host": "Host",
                    "port": "Porta",
                    "username": "Nome de usuário",
                    "password": "Senha",
                    "ssl": "Usar SSL"
                }
            }
        },
        "error": {
            "name_exists": "O nome já existe.",
            "cannot_connect": "Não consigo conectar ao Mikrotik.",
            "ssl_handshake_failure": "Falha no handshake SSL",
            "connection_timeout": "Tempo limite de conexão do Mikrotik.",
            "wrong_login": "Nome de usuário ou senha inválidos."
        }
    },
    "options": {
        "step": {
            "basic_options": {
                "data": {
                    "scan_interval": "Intervalo de escaneamento (requer reinicialização do HA)",
                    "track_iface_clients": "Mostrar MAC e IP do cliente nas interfaces",
                    "unit_of_measurement": "Unidade de medida",
                    "track_network_hosts_timeout": "Rastrear o tempo limite dos dispositivos de rede (segundos)",
                    "zone": "Zona para rastreador de dispositivos"
                },
                "title": "Opções de roteador Mikrotik (1\/2)",
                "description": "Inicialize a integração"
            },
            "sensor_select": {
                "data": {
                    "track_network_hosts": "Rastrear dispositivos de rede",
                    "sensor_port_tracker": "Sensores do rastreador de porta",
                    "sensor_port_traffic": "Sensores de tráfego de porta",
                    "sensor_client_traffic": "Sensores de tráfego do cliente",
                    "sensor_simple_queues": "Interruptores de filas simples",
                    "sensor_nat": "Interruptores NAT",
                    "sensor_scripts": "Interruptores de script",
                    "sensor_environment": "Sensores de variáveis de ambiente",
                    "sensor_kidcontrol": "Controle infantil",
                    "sensor_mangle": "Interruptores Mangle",
                    "sensor_ppp": "Usuários de PPP",
                    "sensor_filter": "Interruptores de filtro",
                    "sensor_client_captive": "sensores de cliente cativo"
                },
                "title": "Opções de roteador Mikrotik (2\/2)",
                "description": "Ativar sensores e interruptores"
            }
        }
    }
}

File: /custom_components\mikrotik_router\translations\ru.json
{
    "config": {
        "step": {
            "user": {
                "title": "Настроить Mikrotik Router",
                "description": "Настройка Home Assistant для интеграции с Mikrotik.",
                "data": {
                    "name": "Название интеграции",
                    "host": "Адрес хоста",
                    "port": "Порт",
                    "username": "Имя пользователя",
                    "password": "Пароль",
                    "ssl": "Использовать SSL"
                }
            }
        },
        "error": {
            "name_exists": "Это название уже используется.",
            "cannot_connect": "Не удалось подключиться.",
            "ssl_handshake_failure": "Ошибка SSL-соединения.",
            "connection_timeout": "Истекло время подключения к Mikrotik.",
            "wrong_login": "Неверное имя пользователя или пароль."
        }
    },
    "options": {
        "step": {
            "basic_options": {
                "data": {
                    "scan_interval": "Интервал сканирования (требуется перезагрузка HA)",
                    "track_iface_clients": "Показывать в интерфейсе MAC и IP клиентов",
                    "unit_of_measurement": "Единицы измерения",
                    "track_network_hosts_timeout": "Таймаут отслеживания сетевых устройств (в секундах)",
                    "zone": "Зона для отслеживания устройств"
                },
                "title": "Параметры Mikrotik Router (1\/2)",
                "description": "Настроить интеграцию"
            },
            "sensor_select": {
                "data": {
                    "track_network_hosts": "Отслеживание сетевых устройств",
                    "sensor_port_tracker": "Сенсоры отслеживания порта",
                    "sensor_port_traffic": "Сенсоры трафика порта",
                    "sensor_client_traffic": "Сенсоры клиентского трафика",
                    "sensor_simple_queues": "Переключатели простых очередей",
                    "sensor_nat": "Переключатели NAT правил",
                    "sensor_scripts": "Переключатели скриптов",
                    "sensor_environment": "Сенсоры переменных окружения",
                    "sensor_kidcontrol": "Родительский контроль",
                    "sensor_mangle": "Переключатели Mangle",
                    "sensor_ppp": "PPP-пользователи",
                    "sensor_filter": "Переключатели фильтров",
                    "sensor_client_captive": "Данные портала авторизации"
                },
                "title": "Параметры Mikrotik Router (2\/2)",
                "description": "Включить датчики и переключатели"
            }
        }
    }
}

File: /custom_components\mikrotik_router\translations\sk.json
{
    "config": {
        "step": {
            "user": {
                "title": "Nastaviť Mikrotik Router",
                "description": "Nastaviť integráciu Mikrotik Router.",
                "data": {
                    "name": "Názov integrácie",
                    "host": "Zariadenie",
                    "port": "Port",
                    "username": "Užívateľ",
                    "password": "Heslo",
                    "ssl": "Použiť SSL"
                }
            }
        },
        "error": {
            "name_exists": "Názov už existuje.",
            "cannot_connect": "Nedá sa pripojiť k Mikrotiku.",
            "ssl_handshake_failure": "Zlyhanie nadviazania spojenia SSL.",
            "connection_timeout": "Časový limit pripojenia vypršal.",
            "wrong_login": "Nesprávne užívateľské meno alebo heslo."
        }
    },
    "options": {
        "step": {
            "basic_options": {
                "data": {
                    "scan_interval": "Interval skenovania (vyžaduje sa reštart HA)",
                    "track_iface_clients": "Zobraziť klientske MAC a IP na rozhraniach",
                    "unit_of_measurement": "Merná jednotka",
                    "track_network_hosts_timeout": "Časový limit sledovania sieťových zariadení (sekundy)",
                    "zone": "Zóna pre sledované zariadenia"
                },
                "title": "Možnosti Mikrotik Router (1\/2)",
                "description": "Nakonfigurovať integráciu"
            },
            "sensor_select": {
                "data": {
                    "track_network_hosts": "Sledovanie sieťových zariadení",
                    "sensor_port_tracker": "Senzory sledovania portov",
                    "sensor_port_traffic": "Senzory prenosu v porte",
                    "sensor_client_traffic": "Senzory prenosu klientov",
                    "sensor_simple_queues": "Jednoduché prepínače radov",
                    "sensor_nat": "Prepínače NAT",
                    "sensor_scripts": "Prepínače skriptov",
                    "sensor_environment": "Snímače prostredia",
                    "sensor_kidcontrol": "Detská kontrola",
                    "sensor_mangle": "Mangle prepínače",
                    "sensor_ppp": "PPP používatelia",
                    "sensor_filter": "Prepínače filtrov",
                    "sensor_client_captive": "Captive portal data"
                },
                "title": "Možnosti Mikrotik Router (2\/2)",
                "description": "Povoliť senzory a spínače"
            }
        }
    }
}

File: /custom_components\mikrotik_router\translations\tr.json
{
    "config": {
        "step": {
            "user": {
                "title": "Mikrotik Router'ı Kur",
                "description": "Mikrotik yönlendirici entegrasyonunu kur",
                "data": {
                    "name": "Entegrasyon adı",
                    "host": "Sunucu",
                    "port": "Port",
                    "username": "Kullanıcı adı",
                    "password": "Şifre",
                    "ssl": "SSL kullan"
                }
            }
        },
        "error": {
            "name_exists": "Bu ad zaten var.",
            "cannot_connect": "Mikrotik'e bağlanılamıyor.",
            "ssl_handshake_failure": "SSL uyuşma hatası",
            "connection_timeout": "Mikrotik bağlantısı zaman aşımı.",
            "wrong_login": "Geçersiz kullanıcı adı veya şifresi."
        }
    },
    "options": {
        "step": {
            "basic_options": {
                "data": {
                    "scan_interval": "Aralığı tara (HA yeniden başlatma gerektirir)",
                    "track_iface_clients": "Müşteri MAC'ini ve IP'sini arayüzlerde göster",
                    "unit_of_measurement": "Ölçü birimi",
                    "track_network_hosts_timeout": "Ağ cihazı izleme zaman aşımı (saniyeler)",
                    "zone": "Cihaz izleyici için alan"
                },
                "title": "Mikrotik Router seçenekleri (1\/2)",
                "description": "Entegrasyonu yapılandır"
            },
            "sensor_select": {
                "data": {
                    "track_network_hosts": "Ağ cihazlarını izle",
                    "sensor_port_tracker": "Port izleme sensörleri",
                    "sensor_port_traffic": "Port trafiği sensörleri",
                    "sensor_client_traffic": "İstemci trafik sensörleri",
                    "sensor_simple_queues": "Basit kuyruk switchleri",
                    "sensor_nat": "NAT switchler",
                    "sensor_scripts": "Betik switchleri",
                    "sensor_environment": "Çevre değişkeni sensörleri",
                    "sensor_kidcontrol": "Çocuk denetimi",
                    "sensor_mangle": "Mangle anahtarları",
                    "sensor_ppp": "PPP kullanıcıları",
                    "sensor_filter": "Filtre anahtarları",
                    "sensor_client_captive": "Captive portal data"
                },
                "title": "Mikrotik Router seçenekleri (2\/2)",
                "description": "Sensör ve anahtarları etkinleştir"
            }
        }
    }
}

File: /custom_components\mikrotik_router\translations\uk.json
{
    "config": {
        "step": {
            "user": {
                "title": "Налаштувати Mikrotik Router",
                "description": "Налаштувати Mikrotik Router інтеграцію",
                "data": {
                    "name": "Назва інтеграції",
                    "host": "Хост",
                    "port": "Порт",
                    "username": "Користувач",
                    "password": "Пароль",
                    "ssl": "Використовувати SSL"
                }
            }
        },
        "error": {
            "name_exists": "Назва вже існує.",
            "cannot_connect": "Не можу з'єднатися з Mikrotik.",
            "ssl_handshake_failure": "Помилка SSH протоколу",
            "connection_timeout": "Тайм-аут з'єднання з Mikrotik",
            "wrong_login": "Невірне ім'я або пароль"
        }
    },
    "options": {
        "step": {
            "basic_options": {
                "data": {
                    "scan_interval": "Інтервал сканування (вимагає перезавантаження HA)",
                    "track_iface_clients": "Показувати MAC і IP адреси клієнта",
                    "unit_of_measurement": "Одиниці вимірювання",
                    "track_network_hosts_timeout": "Тайм-аут відстеження мережевих пристроїв (секунди)",
                    "zone": "Зона для трекера пристроїв"
                },
                "title": "Налаштування Mikrotik роутера (1\/2)",
                "description": "Налаштувати інтеграцію"
            },
            "sensor_select": {
                "data": {
                    "track_network_hosts": "Відстежувати мережеві пристрої",
                    "sensor_port_tracker": "Сенсори трекерів портів",
                    "sensor_port_traffic": "Сенсори трафіку портів",
                    "sensor_client_traffic": "Сенсори трафіку клієнтів",
                    "sensor_simple_queues": "Прості черги і перемикачі",
                    "sensor_nat": "Перемикачі NAT",
                    "sensor_scripts": "Перемикачі скриптів",
                    "sensor_environment": "Сенсори змінних оточення",
                    "sensor_kidcontrol": "Дитячий контроль",
                    "sensor_mangle": "Керувати перемикачами",
                    "sensor_ppp": "Користувачі PPP",
                    "sensor_filter": "Фільтрувати перемикачі",
                    "sensor_client_captive": "Дані Captive portal"
                },
                "title": "Mikrotik Router options (2\/2)",
                "description": "Увімкнути сенсори і перемикачі"
            }
        }
    }
}

File: /custom_components\mikrotik_router\translations\vi.json
{
    "config": {
        "step": {
            "user": {
                "title": "Thiết lập Mikrotik Router",
                "description": "Thiết lập tích hợp Bộ định tuyến Mikrotik.",
                "data": {
                    "name": "Tên của tích hợp",
                    "host": "Máy chủ",
                    "port": "Cổng",
                    "username": "Tên người dùng",
                    "password": "Mật khẩu",
                    "ssl": "Sử dụng SSL"
                }
            }
        },
        "error": {
            "name_exists": "Tên người dùng đã tồn tại.",
            "cannot_connect": "Không thể kết nối với Mikrotik.",
            "ssl_handshake_failure": "Lỗi kết nối SSL",
            "connection_timeout": "Hết thời gian chờ kết nối Mikrotik.",
            "wrong_login": "Tên người dùng hoặc mật khẩu không hợp lệ."
        }
    },
    "options": {
        "step": {
            "basic_options": {
                "data": {
                    "scan_interval": "Khoảng thời gian quét (yêu cầu khởi động lại HA)",
                    "track_iface_clients": "Hiển thị MAC và IP của máy khách trên giao diện",
                    "unit_of_measurement": "Đơn vị đo",
                    "track_network_hosts_timeout": "Theo dõi thời gian chờ thiết bị mạng (giây)",
                    "zone": "Khu vực cho trình theo dõi thiết bị"
                },
                "title": "Cài đặt Mikrotik Router (1\/2)",
                "description": "Đặt cấu hình tích hợp"
            },
            "sensor_select": {
                "data": {
                    "track_network_hosts": "Theo dõi thiết bị mạng",
                    "sensor_port_tracker": "Cảm biến theo dõi cổng",
                    "sensor_port_traffic": "Cảm biến lưu lượng cổng",
                    "sensor_client_traffic": "Cảm biến lưu lượng máy khách",
                    "sensor_simple_queues": "Bộ chuyển đổi hàng đợi đơn giản",
                    "sensor_nat": "Bộ chuyển đổi NAT",
                    "sensor_scripts": "Bộ chuyển đổi mã lệnh",
                    "sensor_environment": "Cảm biến biến số môi trường",
                    "sensor_kidcontrol": "Kiểm soát trẻ em",
                    "sensor_mangle": "Công tắc Mangle",
                    "sensor_ppp": "Người dùng PPP",
                    "sensor_filter": "Công tắc bộ lọc",
                    "sensor_client_captive": "Captive portal data"
                },
                "title": "Cài đặt Mikrotik Router (2\/2)",
                "description": "Bật cảm biến và công tắc"
            }
        }
    }
}

File: /custom_components\mikrotik_router\translations\zh_CN.json
{
    "config": {
        "step": {
            "user": {
                "title": "设置Mikrotik Router",
                "description": "设置 Mikrotik 路由器集成。",
                "data": {
                    "name": "集成名称",
                    "host": "主机",
                    "port": "端口",
                    "username": "用户名",
                    "password": "密码",
                    "ssl": "使用 SSL"
                }
            }
        },
        "error": {
            "name_exists": "名称已存在。",
            "cannot_connect": "无法连接到 Mikrotik。",
            "ssl_handshake_failure": "SSL 交握失败",
            "connection_timeout": "Mikrotik 连接超时。",
            "wrong_login": "无效的用户名或密码。"
        }
    },
    "options": {
        "step": {
            "basic_options": {
                "data": {
                    "scan_interval": "扫描间隔（需要重新启动 HA）",
                    "track_iface_clients": "显示接口上的客户端 MAC 和 IP",
                    "unit_of_measurement": "测量单位",
                    "track_network_hosts_timeout": "跟踪网络设备超时（秒）",
                    "zone": "设备跟踪器的区域"
                },
                "title": "Mikrotik Router 选项 (1\/2)",
                "description": "配置集成"
            },
            "sensor_select": {
                "data": {
                    "track_network_hosts": "跟踪网络设备",
                    "sensor_port_tracker": "端口跟踪传感器",
                    "sensor_port_traffic": "端口流量传感器",
                    "sensor_client_traffic": "客户端流量传感器",
                    "sensor_simple_queues": "简单队列交换机",
                    "sensor_nat": "NAT 交换机",
                    "sensor_scripts": "脚本交换机",
                    "sensor_environment": "环境变量传感器",
                    "sensor_kidcontrol": "儿童控制",
                    "sensor_mangle": "标记开关",
                    "sensor_ppp": "PPP 用户",
                    "sensor_filter": "过滤器开关",
                    "sensor_client_captive": "Captive portal data"
                },
                "title": "Mikrotik Router 选项 (2\/2)",
                "description": "启动传感器和开关"
            }
        }
    }
}

File: /custom_components\mikrotik_router\update.py
"""Support for the Mikrotik Router update service."""

from __future__ import annotations

import asyncio
from logging import getLogger
from typing import Any

from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.helpers.aiohttp_client import async_get_clientsession

from homeassistant.components.update import (
    UpdateEntity,
    UpdateDeviceClass,
    UpdateEntityFeature,
)

from .coordinator import MikrotikCoordinator
from .entity import MikrotikEntity, async_add_entities
from .update_types import (
    SENSOR_TYPES,
    SENSOR_SERVICES,
)
from packaging.version import Version

_LOGGER = getLogger(__name__)
DEVICE_UPDATE = "device_update"


# ---------------------------
#   async_setup_entry
# ---------------------------
async def async_setup_entry(
    hass: HomeAssistant,
    config_entry: ConfigEntry,
    _async_add_entities: AddEntitiesCallback,
) -> None:
    """Set up entry for component"""
    dispatcher = {
        "MikrotikRouterOSUpdate": MikrotikRouterOSUpdate,
        "MikrotikRouterBoardFWUpdate": MikrotikRouterBoardFWUpdate,
    }
    await async_add_entities(hass, config_entry, dispatcher)


# ---------------------------
#   MikrotikRouterOSUpdate
# ---------------------------
class MikrotikRouterOSUpdate(MikrotikEntity, UpdateEntity):
    """Define an Mikrotik Controller Update entity."""

    def __init__(
        self,
        coordinator: MikrotikCoordinator,
        entity_description,
        uid: str | None = None,
    ):
        """Set up device update entity."""
        super().__init__(coordinator, entity_description, uid)

        self._attr_supported_features = UpdateEntityFeature.INSTALL
        self._attr_supported_features |= UpdateEntityFeature.BACKUP
        self._attr_supported_features |= UpdateEntityFeature.RELEASE_NOTES
        self._attr_title = self.entity_description.title

    @property
    def is_on(self) -> bool:
        """Return true if device is on."""
        return self._data[self.entity_description.data_attribute]

    @property
    def installed_version(self) -> str:
        """Version installed and in use."""
        return self._data["installed-version"]

    @property
    def latest_version(self) -> str:
        """Latest version available for install."""
        return self._data["latest-version"]

    async def options_updated(self) -> None:
        """No action needed."""

    async def async_install(self, version: str, backup: bool, **kwargs: Any) -> None:
        """Install an update."""
        if backup:
            self.coordinator.execute("/system/backup", "save", None, None)

        self.coordinator.execute("/system/package/update", "install", None, None)

    async def async_release_notes(self) -> str:
        """Return the release notes."""
        try:
            session = async_get_clientsession(self.hass)
            """Get concatenated changelogs from installed_version to latest_version in reverse order."""
            versions_to_fetch = generate_version_list(
                self._data["installed-version"], self._data["latest-version"]
            )

            tasks = [fetch_changelog(session, version) for version in versions_to_fetch]
            changelogs = await asyncio.gather(*tasks)

            # Combine all non-empty changelogs, maintaining reverse order
            combined_changelogs = "\n\n".join(filter(None, changelogs))
            return combined_changelogs.replace("*) ", "- ")

        except Exception as e:
            _LOGGER.warning("Failed to download release notes (%s)", e)

        return "Error fetching release notes."

    @property
    def release_url(self) -> str:
        """URL to the full release notes of the latest version available."""
        return "https://mikrotik.com/download/changelogs"


# ---------------------------
#   MikrotikRouterBoardFWUpdate
# ---------------------------
class MikrotikRouterBoardFWUpdate(MikrotikEntity, UpdateEntity):
    """Define an Mikrotik Controller Update entity."""

    TYPE = DEVICE_UPDATE
    _attr_device_class = UpdateDeviceClass.FIRMWARE

    def __init__(
        self,
        coordinator: MikrotikCoordinator,
        entity_description,
        uid: str | None = None,
    ):
        """Set up device update entity."""
        super().__init__(coordinator, entity_description, uid)

        self._attr_supported_features = UpdateEntityFeature.INSTALL
        self._attr_title = self.entity_description.title

    @property
    def is_on(self) -> bool:
        """Return true if device is on."""
        return (
            self.data["routerboard"]["current-firmware"]
            != self.data["routerboard"]["upgrade-firmware"]
        )

    @property
    def installed_version(self) -> str:
        """Version installed and in use."""
        return self._data["current-firmware"]

    @property
    def latest_version(self) -> str:
        """Latest version available for install."""
        return self._data["upgrade-firmware"]

    async def options_updated(self) -> None:
        """No action needed."""

    async def async_install(self, version: str, backup: bool, **kwargs: Any) -> None:
        """Install an update."""
        self.coordinator.execute("/system/routerboard", "upgrade", None, None)
        self.coordinator.execute("/system", "reboot", None, None)


async def fetch_changelog(session, version: str) -> str:
    """Asynchronously fetch the changelog for a given version."""
    url = f"https://cdn.mikrotik.com/routeros/{version}/CHANGELOG"
    try:
        async with session.get(url) as response:
            if response.status == 200:
                text = await response.text()
                return text.replace("*) ", "- ")
    except Exception as e:
        pass
    return ""


def generate_version_list(start_version: str, end_version: str) -> list:
    """Generate a list of version strings from start_version to end_version in reverse order."""
    start = Version(start_version)
    end = Version(end_version)
    versions = []

    current = end
    while current >= start:
        versions.append(str(current))
        current = decrement_version(current, start)

    return versions


def decrement_version(version: Version, start_version: Version) -> Version:
    """Decrement version by the smallest possible step without going below start_version."""
    if version.micro > 0:
        next_patch = version.micro - 1
        return Version(f"{version.major}.{version.minor}.{next_patch}")
    elif version.minor > 0:
        next_minor = version.minor - 1
        return Version(
            f"{version.major}.{next_minor}.999"
        )  # Assuming .999 as max patch version
    else:
        next_major = version.major - 1
        return Version(
            f"{next_major}.999.999"
        )  # Assuming .999 as max minor and patch version


File: /custom_components\mikrotik_router\update_types.py
"""Definitions for Mikrotik Router update entities."""
from __future__ import annotations

from dataclasses import dataclass, field
from typing import List

from homeassistant.components.update import UpdateEntityDescription


@dataclass
class MikrotikUpdateEntityDescription(UpdateEntityDescription):
    """Class describing mikrotik entities."""

    ha_group: str | None = None
    ha_connection: str | None = None
    ha_connection_value: str | None = None
    title: str | None = None
    data_path: str | None = None
    data_attribute: str = "available"
    data_name: str | None = None
    data_name_comment: bool = False
    data_uid: str | None = None
    data_reference: str | None = None
    data_attributes_list: List = field(default_factory=lambda: [])
    func: str = "MikrotikRouterOSUpdate"


SENSOR_TYPES: tuple[MikrotikUpdateEntityDescription, ...] = (
    MikrotikUpdateEntityDescription(
        key="system_rosupdate",
        name="RouterOS update",
        ha_group="System",
        title="Mikrotik RouterOS",
        data_path="fw-update",
        data_name="",
        data_uid="",
        data_reference="",
        func="MikrotikRouterOSUpdate",
    ),
    MikrotikUpdateEntityDescription(
        key="system_rbfwupdate",
        name="RouterBOARD firmware update",
        ha_group="System",
        title="Mikrotik RouterBOARD",
        data_path="routerboard",
        data_attribute="current-firmware",
        data_name="",
        data_uid="",
        data_reference="",
        func="MikrotikRouterBoardFWUpdate",
    ),
)


SENSOR_SERVICES = {}


File: /custom_components\mikrotik_router\__init__.py
"""Mikrotik Router integration."""
from __future__ import annotations

import voluptuous as vol

from homeassistant.core import HomeAssistant
from homeassistant.helpers import config_validation as cv
from homeassistant.helpers import device_registry
from homeassistant.config_entries import ConfigEntry

from .const import (
    PLATFORMS,
    DOMAIN,
    RUN_SCRIPT_COMMAND,
)
from .coordinator import MikrotikData, MikrotikCoordinator, MikrotikTrackerCoordinator

SCRIPT_SCHEMA = vol.Schema(
    {vol.Required("router"): cv.string, vol.Required("script"): cv.string}
)


# ---------------------------
#   async_setup_entry
# ---------------------------
async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry) -> bool:
    """Set up a config entry."""
    coordinator = MikrotikCoordinator(hass, config_entry)
    await coordinator.async_config_entry_first_refresh()
    coordinatorTracker = MikrotikTrackerCoordinator(hass, config_entry, coordinator)
    await coordinatorTracker.async_config_entry_first_refresh()
    hass.data.setdefault(DOMAIN, {})[config_entry.entry_id] = MikrotikData(
        data_coordinator=coordinator,
        tracker_coordinator=coordinatorTracker,
    )

    await hass.config_entries.async_forward_entry_setups(config_entry, PLATFORMS)

    config_entry.async_on_unload(config_entry.add_update_listener(async_reload_entry))

    hass.services.async_register(
        DOMAIN, RUN_SCRIPT_COMMAND, coordinator.run_script, schema=SCRIPT_SCHEMA
    )

    return True


# ---------------------------
#   async_reload_entry
# ---------------------------
async def async_reload_entry(hass: HomeAssistant, config_entry: ConfigEntry) -> None:
    """Reload the config entry when it changed."""
    await hass.config_entries.async_reload(config_entry.entry_id)


# ---------------------------
#   async_unload_entry
# ---------------------------
async def async_unload_entry(hass: HomeAssistant, config_entry: ConfigEntry) -> bool:
    """Unload a config entry."""

    if unload_ok := await hass.config_entries.async_unload_platforms(
        config_entry, PLATFORMS
    ):
        hass.services.async_remove(DOMAIN, RUN_SCRIPT_COMMAND)
        hass.data[DOMAIN].pop(config_entry.entry_id)

    return unload_ok


# ---------------------------
#   async_remove_config_entry_device
# ---------------------------
async def async_remove_config_entry_device(
    hass, config_entry: ConfigEntry, device_entry: device_registry.DeviceEntry
) -> bool:
    """Remove a config entry from a device."""
    return True


File: /hacs.json
{
    "name": "Mikrotik Router",
    "homeassistant": "2023.8.0",
    "render_readme": false
}


File: /info.md
Monitor and control your Mikrotik device from Home Assistant.

![Mikrotik Logo](https://raw.githubusercontent.com/tomaae/homeassistant-mikrotik_router/master/docs/assets/images/ui/header.png)
 * Interfaces:
   * Enable/disable interfaces
   * SFP status and information
   * POE status, control and information
   * Monitor RX/TX traffic per interface
   * Monitor device presence per interface
   * IP, MAC, Link information per an interface for connected devices
 * Enable/disable NAT rule switches
 * Enable/disable Simple Queue switches
 * Enable/disable Mangle switches
 * Enable/disable Filter switches
 * Monitor and control PPP users
 * Kid Control
 * Mikrotik Accounting traffic sensors per hosts for RX/TX WAN/LAN
 * Device tracker for hosts in network
 * System sensors (CPU, Memory, HDD, Temperature)
 * Check firmware update
 * Execute scripts
 * View environment variables
 * Configurable update interval
 * Configurable traffic unit (bps, Kbps, Mbps, B/s, KB/s, MB/s)
 * Supports monitoring of multiple mikrotik devices simultaneously

## Links
- [Documentation](https://github.com/tomaae/homeassistant-mikrotik_router/tree/master)
- [Configuration](https://github.com/tomaae/homeassistant-mikrotik_router/tree/master#setup-integration)
- [Report a Bug](https://github.com/tomaae/homeassistant-mikrotik_router/issues/new?labels=bug&template=bug_report.md&title=%5BBug%5D)
- [Suggest an idea](https://github.com/tomaae/homeassistant-mikrotik_router/issues/new?labels=enhancement&template=feature_request.md&title=%5BFeature%5D)

[![ko-fi](https://www.ko-fi.com/img/githubbutton_sm.svg)](https://ko-fi.com/G2G71MKZG)


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


File: /Pipfile
[[source]]
name = "pypi"
url = "https://pypi.org/simple"
verify_ssl = true

[dev-packages]
wheel = ">=0.34"
pygithub = ">=1.47"
homeassistant = ">=2021.4.6"
sqlalchemy = "==1.3.16"
codecov = "==2.0.15"
mock-open = "==1.3.1"
mypy = "==0.770"
pre-commit = "==2.2.0"
pylint = "==2.4.4"
astroid = "==2.3.3"
pylint-strict-informational = "==0.1"
pytest-aiohttp = "==0.3.0"
pytest-cov = "==2.8.1"
pytest-sugar = "==0.9.2"
pytest-timeout = "==1.3.3"
pytest = "==5.3.5"
requests_mock = "==1.7.0"
responses = "==0.10.6"

[packages]
librouteros = ">=3.4.1"
mac-vendor-lookup = ">=0.1.12"

File: /README.md
# Mikrotik Router
![GitHub release (latest by date)](https://img.shields.io/github/v/release/tomaae/homeassistant-mikrotik_router?style=plastic)
[![hacs_badge](https://img.shields.io/badge/HACS-Default-41BDF5.svg?style=plastic)](https://github.com/hacs/integration)
![Project Stage](https://img.shields.io/badge/project%20stage-Production%20Ready-green.svg?style=plastic)
![GitHub all releases](https://img.shields.io/github/downloads/tomaae/homeassistant-mikrotik_router/total?style=plastic)

![GitHub commits since latest release](https://img.shields.io/github/commits-since/tomaae/homeassistant-mikrotik_router/latest?style=plastic)
![GitHub commit activity](https://img.shields.io/github/commit-activity/m/tomaae/homeassistant-mikrotik_router?style=plastic)
![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/tomaae/homeassistant-mikrotik_router/ci.yml?style=plastic)

[![Help localize](https://img.shields.io/badge/lokalise-join-green?style=plastic&logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAA4AAAAOCAYAAAAfSC3RAAAAGXRFWHRTb2Z0d2FyZQBBZG9iZSBJbWFnZVJlYWR5ccllPAAAAyhpVFh0WE1MOmNvbS5hZG9iZS54bXAAAAAAADw/eHBhY2tldCBiZWdpbj0i77u/IiBpZD0iVzVNME1wQ2VoaUh6cmVTek5UY3prYzlkIj8+IDx4OnhtcG1ldGEgeG1sbnM6eD0iYWRvYmU6bnM6bWV0YS8iIHg6eG1wdGs9IkFkb2JlIFhNUCBDb3JlIDUuNi1jMTQ1IDc5LjE2MzQ5OSwgMjAxOC8wOC8xMy0xNjo0MDoyMiAgICAgICAgIj4gPHJkZjpSREYgeG1sbnM6cmRmPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5LzAyLzIyLXJkZi1zeW50YXgtbnMjIj4gPHJkZjpEZXNjcmlwdGlvbiByZGY6YWJvdXQ9IiIgeG1sbnM6eG1wTU09Imh0dHA6Ly9ucy5hZG9iZS5jb20veGFwLzEuMC9tbS8iIHhtbG5zOnN0UmVmPSJodHRwOi8vbnMuYWRvYmUuY29tL3hhcC8xLjAvc1R5cGUvUmVzb3VyY2VSZWYjIiB4bWxuczp4bXA9Imh0dHA6Ly9ucy5hZG9iZS5jb20veGFwLzEuMC8iIHhtcE1NOkRvY3VtZW50SUQ9InhtcC5kaWQ6REVCNzgzOEY4NDYxMTFFQUIyMEY4Njc0NzVDOUZFMkMiIHhtcE1NOkluc3RhbmNlSUQ9InhtcC5paWQ6REVCNzgzOEU4NDYxMTFFQUIyMEY4Njc0NzVDOUZFMkMiIHhtcDpDcmVhdG9yVG9vbD0iQWRvYmUgUGhvdG9zaG9wIENDIDIwMTcgKE1hY2ludG9zaCkiPiA8eG1wTU06RGVyaXZlZEZyb20gc3RSZWY6aW5zdGFuY2VJRD0ieG1wLmlpZDozN0ZDRUY4Rjc0M0UxMUU3QUQ2MDg4M0Q0MkE0NjNCNSIgc3RSZWY6ZG9jdW1lbnRJRD0ieG1wLmRpZDozN0ZDRUY5MDc0M0UxMUU3QUQ2MDg4M0Q0MkE0NjNCNSIvPiA8L3JkZjpEZXNjcmlwdGlvbj4gPC9yZGY6UkRGPiA8L3g6eG1wbWV0YT4gPD94cGFja2V0IGVuZD0iciI/Pjs1zyIAAABVSURBVHjaYvz//z8DOYCJgUxAtkYW9+mXyXIrI7l+ZGHc0k5nGxkupdHZxve1yQR1CjbPZURXh9dGoGJZIPUI2QC4JEgjIfyuJuk/uhgj3dMqQIABAPEGTZ/+h0kEAAAAAElFTkSuQmCC)](https://app.lokalise.com/public/581188395e9778a6060128.17699416/)

![English](https://raw.githubusercontent.com/tomaae/homeassistant-mikrotik_router/master/docs/assets/images/flags/us.png)
![Arabic](https://raw.githubusercontent.com/tomaae/homeassistant-mikrotik_router/master/docs/assets/images/flags/eg.png)
![Chinese](https://raw.githubusercontent.com/tomaae/homeassistant-mikrotik_router/master/docs/assets/images/flags/cn.png)
![Czech](https://raw.githubusercontent.com/tomaae/homeassistant-mikrotik_router/master/docs/assets/images/flags/cz.png)
![Dutch](https://raw.githubusercontent.com/tomaae/homeassistant-mikrotik_router/master/docs/assets/images/flags/nl.png)
![French](https://raw.githubusercontent.com/tomaae/homeassistant-mikrotik_router/master/docs/assets/images/flags/fr.png)
![German](https://raw.githubusercontent.com/tomaae/homeassistant-mikrotik_router/master/docs/assets/images/flags/de.png)
![Greek](https://raw.githubusercontent.com/tomaae/homeassistant-mikrotik_router/master/docs/assets/images/flags/gr.png)
![Hindi](https://raw.githubusercontent.com/tomaae/homeassistant-mikrotik_router/master/docs/assets/images/flags/in.png)
![Hungarian](https://raw.githubusercontent.com/tomaae/homeassistant-mikrotik_router/master/docs/assets/images/flags/hu.png)
![Icelandic](https://raw.githubusercontent.com/tomaae/homeassistant-mikrotik_router/master/docs/assets/images/flags/is.png)
![Italian](https://raw.githubusercontent.com/tomaae/homeassistant-mikrotik_router/master/docs/assets/images/flags/it.png)
![Japanese](https://raw.githubusercontent.com/tomaae/homeassistant-mikrotik_router/master/docs/assets/images/flags/jp.png)
![Korean](https://raw.githubusercontent.com/tomaae/homeassistant-mikrotik_router/master/docs/assets/images/flags/kr.png)
![Latvian](https://raw.githubusercontent.com/tomaae/homeassistant-mikrotik_router/master/docs/assets/images/flags/lv.png)
![Polish](https://raw.githubusercontent.com/tomaae/homeassistant-mikrotik_router/master/docs/assets/images/flags/pl.png)
![Portuguese](https://raw.githubusercontent.com/tomaae/homeassistant-mikrotik_router/master/docs/assets/images/flags/pt.png)
![Russian](https://raw.githubusercontent.com/tomaae/homeassistant-mikrotik_router/master/docs/assets/images/flags/ru.png)
![Slovak](https://raw.githubusercontent.com/tomaae/homeassistant-mikrotik_router/master/docs/assets/images/flags/sk.png)
![Spanish](https://raw.githubusercontent.com/tomaae/homeassistant-mikrotik_router/master/docs/assets/images/flags/es.png)
![Turkish](https://raw.githubusercontent.com/tomaae/homeassistant-mikrotik_router/master/docs/assets/images/flags/tr.png)
![Vietnamese](https://raw.githubusercontent.com/tomaae/homeassistant-mikrotik_router/master/docs/assets/images/flags/vn.png)

![Mikrotik Logo](https://raw.githubusercontent.com/tomaae/homeassistant-mikrotik_router/master/docs/assets/images/ui/header.png)

Monitor and control your Mikrotik device from Home Assistant.
 * Interfaces:
   * Enable/disable interfaces
   * SFP status and information
   * POE status, control and information
   * Monitor RX/TX traffic per interface
   * Monitor device presence per interface
   * IP, MAC, Link information per an interface for connected devices
 * Enable/disable NAT rule switches
 * Enable/disable Simple Queue switches
 * Enable/disable Mangle switches
 * Enable/disable Filter switches
 * Monitor and control PPP users
 * Monitor UPS
 * Monitor GPS coordinates
 * Captive Portal
 * Kid Control
 * Client Traffic RX/TX WAN/LAN monitoring though Accounting or Kid Control Devices (depending on RouterOS FW version)
 * Device tracker for hosts in network
 * System sensors (CPU, Memory, HDD, Temperature)
 * Check and update RouterOS and RouterBOARD firmware
 * Execute scripts
 * View environment variables
 * Configurable update interval
 * Configurable traffic unit (bps, Kbps, Mbps, B/s, KB/s, MB/s)
 * Supports monitoring of multiple mikrotik devices simultaneously

# Features
## Interfaces
Monitor and control status on each Mikrotik interface, both lan and wlan. Both physical and virtual.

![Interface Info](https://raw.githubusercontent.com/tomaae/homeassistant-mikrotik_router/master/docs/assets/images/ui/interface.png)
![Interface Switch](https://raw.githubusercontent.com/tomaae/homeassistant-mikrotik_router/master/docs/assets/images/ui/interface_switch.png)
![Interface Sensor](https://raw.githubusercontent.com/tomaae/homeassistant-mikrotik_router/master/docs/assets/images/ui/interface_sensor.png)

## NAT
Monitor and control individual NAT rules.

More information about NAT rules can be found on [Mikrotik support page](https://help.mikrotik.com/docs/display/ROS/NAT).

![NAT switch](https://raw.githubusercontent.com/tomaae/homeassistant-mikrotik_router/master/docs/assets/images/ui/nat.png)

## Mangle
Monitor and control individual Mangle rules.

More information about Mangle rules can be found on [Mikrotik support page](https://help.mikrotik.com/docs/display/ROS/Mangle).

![Mangle switch](https://raw.githubusercontent.com/tomaae/homeassistant-mikrotik_router/master/docs/assets/images/ui/mangle_switch.png)


## Simple Queue
Control simple queues.

More information about simple queues can be found on [Mikrotik support page](https://help.mikrotik.com/docs/display/ROS/Queues#heading-SimpleQueue).

NOTE: FastTracked packets are not processed by Simple Queues.

![Queue switch](https://raw.githubusercontent.com/tomaae/homeassistant-mikrotik_router/master/docs/assets/images/ui/queue_switch.png)


## PPP
Control and monitor PPP users.

![PPP switch](https://raw.githubusercontent.com/tomaae/homeassistant-mikrotik_router/master/docs/assets/images/ui/ppp_switch.png)
![PPP tracker](https://raw.githubusercontent.com/tomaae/homeassistant-mikrotik_router/master/docs/assets/images/ui/ppp_tracker.png)

## Host Tracking
Track availability of all network devices. All devices visible to Mikrotik device can be tracked, including: LAN connected devices and both Wireless and CAPsMAN from Mikrotik wireless package.

![Host tracker](https://raw.githubusercontent.com/tomaae/homeassistant-mikrotik_router/master/docs/assets/images/ui/host_tracker.png)

## Netwatch Tracking
Track netwatch status.

![Netwatch](https://raw.githubusercontent.com/tomaae/homeassistant-mikrotik_router/master/docs/assets/images/ui/netwatch_tracker.png)

## Scripts
Execute Mikrotik Router scripts.
You can execute scripts by automatically created switches or using services.

![Script Switch](https://raw.githubusercontent.com/tomaae/homeassistant-mikrotik_router/master/docs/assets/images/ui/script_switch.png)

## Kid Control
Monitor and control Kid Control.

![Kid Control Enable](https://raw.githubusercontent.com/tomaae/homeassistant-mikrotik_router/master/docs/assets/images/ui/kidcontrol_switch.png)
![Kid Control Pause](https://raw.githubusercontent.com/tomaae/homeassistant-mikrotik_router/master/docs/assets/images/ui/kidcontrol_pause_switch.png)

## Client Traffic

### Client Traffic for RouterOS v6
Monitor per-IP throughput tracking based on Mikrotik Accounting.

Feature is present in Winbox IP-Accounting. Make sure that threshold is set to reasonable value to store all connections between user defined scan interval. Max value is 8192 so for piece of mind I recommend setting that value.

More information about Accounting can be found on [Mikrotik support page](https://wiki.mikrotik.com/wiki/Manual:IP/Accounting).

NOTE: Accounting does not count in FastTracked packets.


### Client Traffic for RouterOS v7+
In RouterOS v7 Accounting feature is deprecated so alternative approach for is to use 
Kid Control Devices feature (IP - Kid Control - Devices).

This feature requires at least one 'kid' to be defined, 
after that Mikrotik will dynamically start tracking bandwidth usage of all known devices.

Simple dummy Kid entry can be defined with

```/ip kid-control add name=Monitor mon=0s-1d tue=0s-1d wed=0s-1d thu=0s-1d fri=0s-1d sat=0s-1d sun=0s-1d```

![Accounting sensor](https://raw.githubusercontent.com/tomaae/homeassistant-mikrotik_router/master/docs/assets/images/ui/accounting_sensor.png)

## UPS sensor
Monitor your UPS.

![UPS sensor](https://raw.githubusercontent.com/tomaae/homeassistant-mikrotik_router/master/docs/assets/images/ui/ups.png)

## GPS sensors
Monitor your GPS coordinates.

![GPS sensor](https://raw.githubusercontent.com/tomaae/homeassistant-mikrotik_router/master/docs/assets/images/ui/gps.png)

## Update sensor
Update Mikrotik OS and firmare directly from Home Assistant.

![RouterOS update](https://raw.githubusercontent.com/tomaae/homeassistant-mikrotik_router/master/docs/assets/images/ui/routeros_update.png)
![Firmware update](https://raw.githubusercontent.com/tomaae/homeassistant-mikrotik_router/master/docs/assets/images/ui/firmware_update.png)

# Install integration
This integration is distributed using [HACS](https://hacs.xyz/).

You can find it under "Integrations", named "Mikrotik Router"

Minimum requirements:
* RouterOS v6.43/v7.1
* Home Assistant 0.114.0

## Using Mikrotik development branch
If you are using development branch for mikrotik, some features may stop working due to major changes in RouterOS.
Use integration master branch instead of latest release to keep up with RouterOS beta adjustments.

## Setup integration
1. Create user for homeassistant on your mikrotik router with following permissions:
   * read, write, api, reboot, policy, test
   * lower permissions are supported, but it will limit functionality (read and api permissions are mandatory).
   * system health sensors won't be available without write & reboot permissions. this limitation is on mikrotik side.
2. If you want to be able to execute scripts on your mikrotik router from HA, script needs to have only following policies:
   * read, write
or check "Don't Require Permissions" option
3. Setup this integration for your Mikrotik device in Home Assistant via `Configuration -> Integrations -> Add -> Mikrotik Router`.
You can add this integration several times for different devices.

NOTES: 
- Do not mistake "Mikrotik Router" integration with HA build-in integration named "Mikrotik".
- If you dont see "Mikrotik Router" integration, clear your browser cache.

![Add Integration](https://raw.githubusercontent.com/tomaae/homeassistant-mikrotik_router/master/docs/assets/images/ui/setup_integration.png)
* "Name of the integration" - Friendly name for this router
* "Host" - Use hostname or IP
* "Port" - Leave at 0 for defaults

## Configuration
First options page:

![Integration options](https://raw.githubusercontent.com/tomaae/homeassistant-mikrotik_router/master/docs/assets/images/ui/integration_options.png)
* "Scan interval" - Scan/refresh time in seconds. HA needs to be reloaded for scan interval change to be applied
* "Unit of measurement" - Traffic sensor measurement (bps, Kbps, Mbps, B/s, KB/s, MB/s)
* "Show client MAC and IP on interfaces" - Display connected IP and MAC address for devices connected to ports on router
* "Track network devices timeout" - Tracked devices will be marked as away after timeout (does not apply to Mikrotik wireless and caps-man)
* "Zone for device tracker" - Add new tracked devices to a specified Home Assistant zone

Second options page:

![Integration sensors](https://raw.githubusercontent.com/tomaae/homeassistant-mikrotik_router/master/docs/assets/images/ui/integration_options_sensors.png)

Select sensors you want to use in Home Assistant.

# Development

## Translation
To help out with the translation you need an account on Lokalise, the easiest way to get one is to [click here](https://lokalise.com/login/) then select "Log in with GitHub".
After you have created your account [click here to join Mikrotik Router project on Lokalise](https://app.lokalise.com/public/581188395e9778a6060128.17699416/).

If you want to add translations for a language that is not listed please [open a Feature request](https://github.com/tomaae/homeassistant-mikrotik_router/issues/new?labels=enhancement&title=%5BLokalise%5D%20Add%20new%20translations%20language).

## Diagnostics
Download diagnostics data for investigation:

![Diagnostics](https://raw.githubusercontent.com/tomaae/homeassistant-mikrotik_router/master/docs/assets/images/ui/diagnostics.png)

## Enabling debug
To enable debug for Mikrotik router integration, add following to your configuration.yaml:
```
logger:
  default: info
  logs:
    custom_components.mikrotik_router: debug
```


File: /requirements.txt
librouteros>=3.4.1
mac-vendor-lookup>=0.1.12

File: /setup.cfg
[flake8]
ignore = W293

max-line-length = 220
max-complexity = 10
exclude = ./.git,
          ./tests,
          ./.github,
          __pycache__,
          ./docs,
          ./custom_components/mikrotik_router/librouteros_custom

# Run with: pylint --rcfile=setup.cfg --load-plugins=pylint.extensions.mccabe custom_components
[pylint]
disable = duplicate-code,
          too-many-public-methods,
          useless-return,
          import-error,
          too-many-arguments,
          too-many-instance-attributes,
          simplifiable-if-expression,
          bare-except


File: /sonar-project.properties
sonar.organization=tomaae
sonar.projectKey=tomaae_homeassistant-mikrotik_router

# relative paths to source directories. More details and properties are described
# in https://sonarcloud.io/documentation/project-administration/narrowing-the-focus/
sonar.sources=.

