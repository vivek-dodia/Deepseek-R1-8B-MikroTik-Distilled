# Repository Information
Name: Grafana-Mikrotik

# Directory Structure
Directory structure:
└── github_repos/Grafana-Mikrotik/
    ├── .env
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
    │   │       ├── pack-764b18f1da4133dde9ad1d2cc7ea20bb4d1653b9.idx
    │   │       └── pack-764b18f1da4133dde9ad1d2cc7ea20bb4d1653b9.pack
    │   ├── packed-refs
    │   └── refs/
    │       ├── heads/
    │       │   └── master
    │       ├── remotes/
    │       │   └── origin/
    │       │       └── HEAD
    │       └── tags/
    ├── .github/
    │   └── workflows/
    │       └── action.yml
    ├── .grafana
    ├── .prometheus
    ├── docker-compose.yml
    ├── grafana/
    │   └── provisioning/
    │       ├── dashboards/
    │       │   ├── dashboard.yml
    │       │   └── Mikrotik-snmp-prometheus.json
    │       └── datasources/
    │           └── datasource.yml
    ├── LICENSE
    ├── Mikrotik-snmp-prometheus.json
    ├── prometheus/
    │   ├── data/
    │   │   └── .gitignore
    │   └── prometheus.yml
    ├── readme/
    ├── README.md
    ├── run.sh
    └── snmp/
        ├── Dockerfile
        ├── LICENSE
        ├── NOTICE
        ├── snmp.yml
        └── snmp_exporter


# Content
File: /.env
CURRENT_USER=1000:1000


File: /.git\config
[core]
	repositoryformatversion = 0
	filemode = false
	bare = false
	logallrefupdates = true
	symlinks = false
	ignorecase = true
[remote "origin"]
	url = https://github.com/IgorKha/Grafana-Mikrotik.git
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
0000000000000000000000000000000000000000 da35426cfddf3ce0a664fe6adc79d9d2e6766a4e vivek-dodia <vivek.dodia@icloud.com> 1738605786 -0500	clone: from https://github.com/IgorKha/Grafana-Mikrotik.git


File: /.git\logs\refs\heads\master
0000000000000000000000000000000000000000 da35426cfddf3ce0a664fe6adc79d9d2e6766a4e vivek-dodia <vivek.dodia@icloud.com> 1738605786 -0500	clone: from https://github.com/IgorKha/Grafana-Mikrotik.git


File: /.git\logs\refs\remotes\origin\HEAD
0000000000000000000000000000000000000000 da35426cfddf3ce0a664fe6adc79d9d2e6766a4e vivek-dodia <vivek.dodia@icloud.com> 1738605786 -0500	clone: from https://github.com/IgorKha/Grafana-Mikrotik.git


File: /.git\packed-refs
# pack-refs with: peeled fully-peeled sorted 
da35426cfddf3ce0a664fe6adc79d9d2e6766a4e refs/remotes/origin/master
7aba11db31715768582f1bdaded694ad60f53369 refs/tags/8.1.7.01
14dfc12bc7c16121d1ef0ba227c317a4be83faf0 refs/tags/8.1.7.02
101c1342eed8784c5fc2c2648203a509c91a511a refs/tags/8.1.7.03
142fb78e24f2d7e23915c492924b11ecd77597fa refs/tags/8.2.1.01


File: /.git\refs\heads\master
da35426cfddf3ce0a664fe6adc79d9d2e6766a4e


File: /.git\refs\remotes\origin\HEAD
ref: refs/remotes/origin/master


File: /.github\workflows\action.yml
name: deploy

on: [push, pull_request]

jobs:

  lint:
    name: lint
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - name: Run Shellcheck
        uses: azohra/shell-linter@latest
        with:
          path: "run.sh"
          severity: "warning, error"

  test:
    name: test
    needs: lint
    runs-on: ubuntu-latest
    steps:
      - name: deploy with sh script
        run: curl -fsSL https://raw.githubusercontent.com/IgorKha/Grafana-Mikrotik/master/run.sh | bash -s --

      - name: Test Grafana
        run: sleep 10 && curl -GLsS --retry 5 --retry-connrefused --retry-delay 2 'http://localhost:3000/api/health'

      - name: Test Prometheus
        run: curl -GLsS --retry 5 --retry-delay 2 "http://localhost:9090/-/ready"

      - name: Test snmp_exporter
        run: curl -ILsS --retry 5 --retry-delay 2 "http://localhost:9116"


File: /.grafana
GF_SECURITY_ADMIN_USER=admin
GF_SECURITY_ADMIN_PASSWORD=mikrotik
GF_USERS_ALLOW_SIGN_UP=false


File: /.prometheus
MIKROTIK_IP=192.168.88.1


File: /docker-compose.yml
version: '3.9'

services:
  grafana:
    image: grafana/grafana:9.0.5
    env_file:
      - .grafana
    container_name: mk_grafana
    restart: always
    volumes:
      - ./grafana/provisioning/:/etc/grafana/provisioning/
    ports:
      - "3000:3000"
  
  prometheus:
    image: prom/prometheus
    env_file:
      - .prometheus
    user: ${CURRENT_USER}
    container_name: mk_prometheus
    restart: always
    volumes:
      - ./prometheus/:/etc/prometheus
      - ./prometheus/data/:/prometheus
    ports:
      - "9090:9090"

  snmp_exporter:
    image: prom/snmp-exporter
    container_name: mk_snmp_exporter
    restart: always
    volumes:
      - ./snmp/:/etc/snmp_exporter/
    ports:
      - "9116:9116"
    depends_on:
      - prometheus


File: /grafana\provisioning\dashboards\dashboard.yml
apiVersion: 1

providers:
- name: 'Prometheus'
  orgId: 1
  folder: ''
  type: file
  disableDeletion: false
  editable: true
  options:
    path: /etc/grafana/provisioning/dashboards

File: /grafana\provisioning\dashboards\Mikrotik-snmp-prometheus.json
{
  "__inputs": [
    {
      "name": "DS_PROMETHEUS",
      "label": "Prometheus",
      "description": "",
      "type": "datasource",
      "pluginId": "prometheus",
      "pluginName": "Prometheus"
    }
  ],
  "__elements": {},
  "__requires": [
    {
      "type": "panel",
      "id": "gauge",
      "name": "Gauge",
      "version": ""
    },
    {
      "type": "grafana",
      "id": "grafana",
      "name": "Grafana",
      "version": "9.0.5"
    },
    {
      "type": "panel",
      "id": "graph",
      "name": "Graph (old)",
      "version": ""
    },
    {
      "type": "panel",
      "id": "heatmap",
      "name": "Heatmap",
      "version": ""
    },
    {
      "type": "datasource",
      "id": "prometheus",
      "name": "Prometheus",
      "version": "1.0.0"
    },
    {
      "type": "panel",
      "id": "stat",
      "name": "Stat",
      "version": ""
    },
    {
      "type": "panel",
      "id": "table",
      "name": "Table",
      "version": ""
    },
    {
      "type": "panel",
      "id": "timeseries",
      "name": "Time series",
      "version": ""
    }
  ],
  "annotations": {
    "list": [
      {
        "builtIn": 1,
        "datasource": {
          "type": "datasource",
          "uid": "grafana"
        },
        "enable": true,
        "hide": true,
        "iconColor": "rgba(0, 211, 255, 1)",
        "name": "Annotations & Alerts",
        "target": {
          "limit": 100,
          "matchAny": false,
          "tags": [],
          "type": "dashboard"
        },
        "type": "dashboard"
      }
    ]
  },
  "description": "Mikrotik snmp monitoring (prometheus) 9.0.5",
  "editable": true,
  "fiscalYearStartMonth": 0,
  "gnetId": 14420,
  "graphTooltip": 1,
  "id": null,
  "links": [
    {
      "asDropdown": false,
      "icon": "external link",
      "includeVars": false,
      "keepTime": false,
      "tags": [],
      "targetBlank": true,
      "title": "Github",
      "tooltip": "Open project on Github",
      "type": "link",
      "url": "https://github.com/IgorKha/Grafana-Mikrotik"
    },
    {
      "asDropdown": false,
      "icon": "dashboard",
      "includeVars": false,
      "keepTime": false,
      "tags": [],
      "targetBlank": true,
      "title": "dashboard",
      "tooltip": "Open dashboard",
      "type": "link",
      "url": "https://grafana.com/grafana/dashboards/14420"
    }
  ],
  "liveNow": false,
  "panels": [
    {
      "collapsed": true,
      "datasource": {
        "type": "prometheus",
        "uid": "PBFA97CFB590B2093"
      },
      "gridPos": {
        "h": 1,
        "w": 24,
        "x": 0,
        "y": 0
      },
      "id": 1655,
      "panels": [
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${DS_PROMETHEUS}"
          },
          "description": "Total SNMP time scrape took (walk and processing)",
          "fieldConfig": {
            "defaults": {
              "color": {
                "mode": "thresholds"
              },
              "mappings": [
                {
                  "options": {
                    "result": {
                      "text": ""
                    },
                    "to": 0
                  },
                  "type": "range"
                }
              ],
              "min": 0,
              "thresholds": {
                "mode": "absolute",
                "steps": [
                  {
                    "color": "#299c46",
                    "value": null
                  },
                  {
                    "color": "yellow",
                    "value": 1
                  },
                  {
                    "color": "#EF843C",
                    "value": 1.5
                  },
                  {
                    "color": "red",
                    "value": 2
                  }
                ]
              },
              "unit": "s"
            },
            "overrides": []
          },
          "gridPos": {
            "h": 4,
            "w": 4,
            "x": 0,
            "y": 1
          },
          "id": 1656,
          "links": [],
          "maxDataPoints": 100,
          "options": {
            "colorMode": "value",
            "graphMode": "none",
            "justifyMode": "auto",
            "orientation": "horizontal",
            "reduceOptions": {
              "calcs": [
                "lastNotNull"
              ],
              "fields": "",
              "values": false
            },
            "text": {},
            "textMode": "auto"
          },
          "pluginVersion": "9.0.5",
          "targets": [
            {
              "datasource": {
                "type": "prometheus",
                "uid": "${DS_PROMETHEUS}"
              },
              "exemplar": true,
              "expr": "snmp_scrape_duration_seconds{instance='$instance'}",
              "instant": true,
              "interval": "",
              "legendFormat": "",
              "refId": "A"
            }
          ],
          "title": "Total SNMP time (walk and processing)",
          "type": "stat"
        },
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${DS_PROMETHEUS}"
          },
          "description": "Time SNMP walk/bulkwalk took",
          "fieldConfig": {
            "defaults": {
              "color": {
                "mode": "thresholds"
              },
              "mappings": [
                {
                  "options": {
                    "result": {
                      "text": ""
                    },
                    "to": 0
                  },
                  "type": "range"
                }
              ],
              "min": 0,
              "thresholds": {
                "mode": "absolute",
                "steps": [
                  {
                    "color": "#299c46",
                    "value": null
                  },
                  {
                    "color": "yellow",
                    "value": 1
                  },
                  {
                    "color": "#EF843C",
                    "value": 1.5
                  },
                  {
                    "color": "red",
                    "value": 2
                  }
                ]
              },
              "unit": "s"
            },
            "overrides": []
          },
          "gridPos": {
            "h": 4,
            "w": 4,
            "x": 4,
            "y": 1
          },
          "id": 1657,
          "links": [],
          "maxDataPoints": 100,
          "options": {
            "colorMode": "value",
            "graphMode": "none",
            "justifyMode": "auto",
            "orientation": "horizontal",
            "reduceOptions": {
              "calcs": [
                "lastNotNull"
              ],
              "fields": "",
              "values": false
            },
            "text": {},
            "textMode": "auto"
          },
          "pluginVersion": "9.0.5",
          "targets": [
            {
              "datasource": {
                "type": "prometheus",
                "uid": "${DS_PROMETHEUS}"
              },
              "exemplar": true,
              "expr": "snmp_scrape_walk_duration_seconds{instance='$instance'}",
              "instant": true,
              "interval": "",
              "legendFormat": "",
              "refId": "A"
            }
          ],
          "title": "Time SNMP walk/bulkwalk took",
          "type": "stat"
        },
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${DS_PROMETHEUS}"
          },
          "description": "",
          "fieldConfig": {
            "defaults": {
              "color": {
                "mode": "thresholds"
              },
              "mappings": [
                {
                  "options": {
                    "result": {
                      "text": ""
                    },
                    "to": 0
                  },
                  "type": "range"
                }
              ],
              "min": 0,
              "thresholds": {
                "mode": "absolute",
                "steps": [
                  {
                    "color": "text",
                    "value": null
                  }
                ]
              },
              "unit": "none"
            },
            "overrides": []
          },
          "gridPos": {
            "h": 4,
            "w": 4,
            "x": 8,
            "y": 1
          },
          "id": 1658,
          "links": [],
          "maxDataPoints": 100,
          "options": {
            "colorMode": "value",
            "graphMode": "none",
            "justifyMode": "auto",
            "orientation": "horizontal",
            "reduceOptions": {
              "calcs": [
                "lastNotNull"
              ],
              "fields": "",
              "values": false
            },
            "text": {},
            "textMode": "auto"
          },
          "pluginVersion": "9.0.5",
          "targets": [
            {
              "datasource": {
                "type": "prometheus",
                "uid": "${DS_PROMETHEUS}"
              },
              "exemplar": true,
              "expr": "snmp_scrape_pdus_returned{instance='$instance'}",
              "instant": true,
              "interval": "",
              "legendFormat": "",
              "refId": "A"
            }
          ],
          "title": "scrape pdus returned",
          "type": "stat"
        }
      ],
      "targets": [
        {
          "datasource": {
            "type": "prometheus",
            "uid": "PBFA97CFB590B2093"
          },
          "refId": "A"
        }
      ],
      "title": "SNMP",
      "type": "row"
    },
    {
      "collapsed": false,
      "datasource": {
        "type": "prometheus",
        "uid": "PBFA97CFB590B2093"
      },
      "gridPos": {
        "h": 1,
        "w": 24,
        "x": 0,
        "y": 1
      },
      "id": 1218,
      "panels": [],
      "targets": [
        {
          "datasource": {
            "type": "prometheus",
            "uid": "PBFA97CFB590B2093"
          },
          "refId": "A"
        }
      ],
      "title": "System",
      "type": "row"
    },
    {
      "datasource": {
        "type": "prometheus",
        "uid": "${DS_PROMETHEUS}"
      },
      "fieldConfig": {
        "defaults": {
          "color": {
            "mode": "thresholds"
          },
          "decimals": 2,
          "mappings": [
            {
              "options": {
                "result": {
                  "text": ""
                },
                "to": 0
              },
              "type": "range"
            }
          ],
          "min": 0,
          "thresholds": {
            "mode": "absolute",
            "steps": [
              {
                "color": "green",
                "value": null
              },
              {
                "color": "dark-red",
                "value": 0
              },
              {
                "color": "dark-orange",
                "value": 86400
              },
              {
                "color": "dark-yellow",
                "value": 604800
              },
              {
                "color": "#299c46",
                "value": 2628000
              }
            ]
          },
          "unit": "dtdurations"
        },
        "overrides": []
      },
      "gridPos": {
        "h": 2,
        "w": 4,
        "x": 0,
        "y": 2
      },
      "id": 476,
      "links": [],
      "maxDataPoints": 100,
      "options": {
        "colorMode": "value",
        "graphMode": "none",
        "justifyMode": "auto",
        "orientation": "horizontal",
        "reduceOptions": {
          "calcs": [
            "lastNotNull"
          ],
          "fields": "",
          "values": false
        },
        "text": {},
        "textMode": "auto"
      },
      "pluginVersion": "9.0.5",
      "targets": [
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${DS_PROMETHEUS}"
          },
          "exemplar": true,
          "expr": "sysUpTime{instance='$instance'}/100",
          "interval": "",
          "legendFormat": "",
          "refId": "A"
        }
      ],
      "title": "Uptime",
      "type": "stat"
    },
    {
      "datasource": {
        "type": "prometheus",
        "uid": "${DS_PROMETHEUS}"
      },
      "description": "The current operational state of the device described by this row of the table. A value unknown(1) indicates that the current state of the device is unknown. running(2) indicates that the device is up and running and that no unusual error conditions are known. The warning(3) state indicates that agent has been informed of an unusual error condition by the operational software (e.g., a disk device driver) but that the device is still 'operational'. An example would be a high number of soft errors on a disk. A value of testing(4), indicates that the device is not available for use because it is in the testing state. The state of down(5) is used only when the agent has been informed that the device is not available for any use.",
      "fieldConfig": {
        "defaults": {
          "color": {
            "mode": "thresholds"
          },
          "mappings": [
            {
              "options": {
                "1": {
                  "text": "Unknown"
                },
                "2": {
                  "text": "Running"
                },
                "3": {
                  "text": "Warning!"
                },
                "4": {
                  "text": "Testing"
                },
                "5": {
                  "text": "Down"
                }
              },
              "type": "value"
            }
          ],
          "thresholds": {
            "mode": "absolute",
            "steps": [
              {
                "color": "#299c46",
                "value": null
              },
              {
                "color": "#EAB839",
                "value": 1
              },
              {
                "color": "#299c46",
                "value": 2
              },
              {
                "color": "dark-red",
                "value": 3
              },
              {
                "color": "light-blue",
                "value": 4
              },
              {
                "color": "rgb(69, 69, 71)",
                "value": 5
              }
            ]
          },
          "unit": "none"
        },
        "overrides": []
      },
      "gridPos": {
        "h": 2,
        "w": 2,
        "x": 4,
        "y": 2
      },
      "id": 1220,
      "options": {
        "colorMode": "value",
        "graphMode": "none",
        "justifyMode": "auto",
        "orientation": "auto",
        "reduceOptions": {
          "calcs": [
            "lastNotNull"
          ],
          "fields": "",
          "values": false
        },
        "text": {},
        "textMode": "auto"
      },
      "pluginVersion": "9.0.5",
      "targets": [
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${DS_PROMETHEUS}"
          },
          "exemplar": true,
          "expr": "hrDeviceStatus{instance='$instance', hrDeviceIndex=\"1\"}",
          "instant": true,
          "interval": "",
          "legendFormat": "",
          "refId": "A"
        }
      ],
      "title": "Status device",
      "type": "stat"
    },
    {
      "datasource": {
        "type": "prometheus",
        "uid": "${DS_PROMETHEUS}"
      },
      "description": "The number of errors detected on this device",
      "fieldConfig": {
        "defaults": {
          "color": {
            "mode": "thresholds"
          },
          "mappings": [],
          "thresholds": {
            "mode": "absolute",
            "steps": [
              {
                "color": "#299c46",
                "value": null
              },
              {
                "color": "dark-orange",
                "value": 1
              }
            ]
          }
        },
        "overrides": []
      },
      "gridPos": {
        "h": 2,
        "w": 2,
        "x": 6,
        "y": 2
      },
      "id": 1614,
      "options": {
        "colorMode": "value",
        "graphMode": "none",
        "justifyMode": "auto",
        "orientation": "auto",
        "reduceOptions": {
          "calcs": [
            "lastNotNull"
          ],
          "fields": "",
          "values": false
        },
        "text": {},
        "textMode": "auto"
      },
      "pluginVersion": "9.0.5",
      "targets": [
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${DS_PROMETHEUS}"
          },
          "exemplar": true,
          "expr": "hrDeviceErrors{instance='$instance', hrDeviceIndex=\"1\"}",
          "hide": false,
          "instant": true,
          "interval": "",
          "legendFormat": "",
          "refId": "A"
        }
      ],
      "title": "Device Errors",
      "type": "stat"
    },
    {
      "datasource": {
        "type": "prometheus",
        "uid": "${DS_PROMETHEUS}"
      },
      "description": "",
      "fieldConfig": {
        "defaults": {
          "color": {
            "mode": "thresholds"
          },
          "mappings": [],
          "thresholds": {
            "mode": "absolute",
            "steps": [
              {
                "color": "#fff899",
                "value": null
              }
            ]
          }
        },
        "overrides": []
      },
      "gridPos": {
        "h": 2,
        "w": 4,
        "x": 8,
        "y": 2
      },
      "id": 1264,
      "options": {
        "colorMode": "value",
        "graphMode": "none",
        "justifyMode": "auto",
        "orientation": "auto",
        "reduceOptions": {
          "calcs": [
            "lastNotNull"
          ],
          "fields": "",
          "values": false
        },
        "text": {},
        "textMode": "name"
      },
      "pluginVersion": "9.0.5",
      "targets": [
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${DS_PROMETHEUS}"
          },
          "exemplar": true,
          "expr": "sysIdentity{instance='$instance'}",
          "hide": false,
          "instant": true,
          "interval": "",
          "legendFormat": "{{sysIdentity}}",
          "refId": "A"
        }
      ],
      "title": "System identity",
      "type": "stat"
    },
    {
      "datasource": {
        "type": "prometheus",
        "uid": "${DS_PROMETHEUS}"
      },
      "description": "",
      "fieldConfig": {
        "defaults": {
          "color": {
            "mode": "thresholds"
          },
          "mappings": [],
          "thresholds": {
            "mode": "absolute",
            "steps": [
              {
                "color": "#fff899",
                "value": null
              }
            ]
          }
        },
        "overrides": []
      },
      "gridPos": {
        "h": 2,
        "w": 4,
        "x": 12,
        "y": 2
      },
      "id": 1311,
      "options": {
        "colorMode": "value",
        "graphMode": "none",
        "justifyMode": "auto",
        "orientation": "auto",
        "reduceOptions": {
          "calcs": [
            "lastNotNull"
          ],
          "fields": "",
          "values": false
        },
        "text": {},
        "textMode": "name"
      },
      "pluginVersion": "9.0.5",
      "targets": [
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${DS_PROMETHEUS}"
          },
          "exemplar": true,
          "expr": "mtxrSerialNumber{instance='$instance'}",
          "hide": false,
          "instant": false,
          "interval": "",
          "legendFormat": "{{mtxrSerialNumber}}",
          "refId": "A"
        }
      ],
      "title": "Serial Number",
      "type": "stat"
    },
    {
      "datasource": {
        "type": "prometheus",
        "uid": "${DS_PROMETHEUS}"
      },
      "description": "",
      "fieldConfig": {
        "defaults": {
          "color": {
            "mode": "thresholds"
          },
          "mappings": [],
          "thresholds": {
            "mode": "absolute",
            "steps": [
              {
                "color": "super-light-yellow",
                "value": null
              }
            ]
          }
        },
        "overrides": []
      },
      "gridPos": {
        "h": 2,
        "w": 8,
        "x": 16,
        "y": 2
      },
      "id": 1241,
      "options": {
        "colorMode": "value",
        "graphMode": "none",
        "justifyMode": "auto",
        "orientation": "auto",
        "reduceOptions": {
          "calcs": [
            "lastNotNull"
          ],
          "fields": "",
          "values": false
        },
        "text": {},
        "textMode": "name"
      },
      "pluginVersion": "9.0.5",
      "targets": [
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${DS_PROMETHEUS}"
          },
          "exemplar": true,
          "expr": "sysDescr{instance='$instance'}",
          "hide": false,
          "instant": true,
          "interval": "",
          "legendFormat": "{{sysDescr}}",
          "refId": "A"
        }
      ],
      "title": "Model",
      "type": "stat"
    },
    {
      "datasource": {
        "type": "prometheus",
        "uid": "${DS_PROMETHEUS}"
      },
      "description": "",
      "fieldConfig": {
        "defaults": {
          "color": {
            "mode": "thresholds"
          },
          "mappings": [],
          "thresholds": {
            "mode": "absolute",
            "steps": [
              {
                "color": "#299c46",
                "value": null
              }
            ]
          },
          "unit": "dateTimeAsLocal"
        },
        "overrides": []
      },
      "gridPos": {
        "h": 2,
        "w": 4,
        "x": 0,
        "y": 4
      },
      "id": 1325,
      "links": [],
      "maxDataPoints": 100,
      "options": {
        "colorMode": "value",
        "graphMode": "area",
        "justifyMode": "center",
        "orientation": "auto",
        "reduceOptions": {
          "calcs": [
            "lastNotNull"
          ],
          "fields": "/^Time$/",
          "values": false
        },
        "text": {},
        "textMode": "auto"
      },
      "pluginVersion": "9.0.5",
      "targets": [
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${DS_PROMETHEUS}"
          },
          "exemplar": true,
          "expr": "time()-(hrSystemDate{instance='$instance'})",
          "instant": true,
          "interval": "",
          "legendFormat": "",
          "refId": "A"
        }
      ],
      "title": "System date",
      "type": "stat"
    },
    {
      "datasource": {
        "type": "prometheus",
        "uid": "${DS_PROMETHEUS}"
      },
      "fieldConfig": {
        "defaults": {
          "color": {
            "mode": "thresholds"
          },
          "mappings": [],
          "thresholds": {
            "mode": "absolute",
            "steps": [
              {
                "color": "#299c46",
                "value": null
              }
            ]
          }
        },
        "overrides": []
      },
      "gridPos": {
        "h": 2,
        "w": 2,
        "x": 4,
        "y": 4
      },
      "id": 1222,
      "options": {
        "colorMode": "value",
        "graphMode": "none",
        "justifyMode": "auto",
        "orientation": "auto",
        "reduceOptions": {
          "calcs": [
            "last"
          ],
          "fields": "",
          "values": false
        },
        "text": {},
        "textMode": "name"
      },
      "pluginVersion": "9.0.5",
      "targets": [
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${DS_PROMETHEUS}"
          },
          "exemplar": true,
          "expr": "mtxrFirmwareVersion{instance='$instance'}",
          "format": "time_series",
          "hide": false,
          "instant": true,
          "interval": "",
          "legendFormat": "{{mtxrFirmwareVersion}}",
          "refId": "A"
        }
      ],
      "title": "Board ver",
      "type": "stat"
    },
    {
      "datasource": {
        "type": "prometheus",
        "uid": "${DS_PROMETHEUS}"
      },
      "description": "",
      "fieldConfig": {
        "defaults": {
          "color": {
            "mode": "thresholds"
          },
          "mappings": [],
          "thresholds": {
            "mode": "absolute",
            "steps": [
              {
                "color": "#299c46",
                "value": null
              }
            ]
          }
        },
        "overrides": []
      },
      "gridPos": {
        "h": 2,
        "w": 2,
        "x": 6,
        "y": 4
      },
      "id": 1650,
      "options": {
        "colorMode": "value",
        "graphMode": "none",
        "justifyMode": "auto",
        "orientation": "auto",
        "reduceOptions": {
          "calcs": [
            "last"
          ],
          "fields": "",
          "values": false
        },
        "text": {},
        "textMode": "name"
      },
      "pluginVersion": "9.0.5",
      "targets": [
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${DS_PROMETHEUS}"
          },
          "exemplar": true,
          "expr": "mtxrLicVersion{instance='$instance'}",
          "format": "time_series",
          "hide": false,
          "instant": true,
          "interval": "",
          "legendFormat": "{{mtxrLicVersion}}",
          "refId": "A"
        }
      ],
      "title": "Package ver",
      "type": "stat"
    },
    {
      "datasource": {
        "type": "prometheus",
        "uid": "${DS_PROMETHEUS}"
      },
      "description": "",
      "fieldConfig": {
        "defaults": {
          "color": {
            "mode": "thresholds"
          },
          "mappings": [],
          "thresholds": {
            "mode": "absolute",
            "steps": [
              {
                "color": "super-light-yellow",
                "value": null
              }
            ]
          }
        },
        "overrides": []
      },
      "gridPos": {
        "h": 2,
        "w": 4,
        "x": 8,
        "y": 4
      },
      "id": 1248,
      "options": {
        "colorMode": "value",
        "graphMode": "none",
        "justifyMode": "auto",
        "orientation": "auto",
        "reduceOptions": {
          "calcs": [
            "lastNotNull"
          ],
          "fields": "",
          "values": false
        },
        "text": {},
        "textMode": "name"
      },
      "pluginVersion": "9.0.5",
      "targets": [
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${DS_PROMETHEUS}"
          },
          "exemplar": true,
          "expr": "mtxrBoardName{instance='$instance'}",
          "hide": false,
          "instant": true,
          "interval": "",
          "legendFormat": "{{mtxrBoardName}}",
          "refId": "A"
        }
      ],
      "title": "Board Name",
      "type": "stat"
    },
    {
      "datasource": {
        "type": "prometheus",
        "uid": "${DS_PROMETHEUS}"
      },
      "description": "",
      "fieldConfig": {
        "defaults": {
          "color": {
            "mode": "thresholds"
          },
          "mappings": [],
          "thresholds": {
            "mode": "absolute",
            "steps": [
              {
                "color": "super-light-yellow",
                "value": null
              }
            ]
          }
        },
        "overrides": []
      },
      "gridPos": {
        "h": 2,
        "w": 4,
        "x": 12,
        "y": 4
      },
      "id": 1649,
      "options": {
        "colorMode": "value",
        "graphMode": "none",
        "justifyMode": "auto",
        "orientation": "auto",
        "reduceOptions": {
          "calcs": [
            "lastNotNull"
          ],
          "fields": "",
          "values": false
        },
        "text": {},
        "textMode": "name"
      },
      "pluginVersion": "9.0.5",
      "targets": [
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${DS_PROMETHEUS}"
          },
          "exemplar": true,
          "expr": "mtxrLicSoftwareId{instance='$instance'}",
          "hide": false,
          "instant": false,
          "interval": "",
          "legendFormat": "{{mtxrLicSoftwareId}}",
          "refId": "A"
        }
      ],
      "title": "Software ID",
      "type": "stat"
    },
    {
      "datasource": {
        "type": "prometheus",
        "uid": "${DS_PROMETHEUS}"
      },
      "description": "",
      "fieldConfig": {
        "defaults": {
          "color": {
            "mode": "thresholds"
          },
          "mappings": [
            {
              "options": {
                "": {
                  "index": 0,
                  "text": "N/A"
                }
              },
              "type": "value"
            }
          ],
          "thresholds": {
            "mode": "absolute",
            "steps": [
              {
                "color": "#299c46",
                "value": null
              }
            ]
          },
          "unit": "string"
        },
        "overrides": []
      },
      "gridPos": {
        "h": 2,
        "w": 8,
        "x": 16,
        "y": 4
      },
      "id": 1653,
      "links": [],
      "maxDataPoints": 100,
      "options": {
        "colorMode": "value",
        "graphMode": "none",
        "justifyMode": "center",
        "orientation": "auto",
        "reduceOptions": {
          "calcs": [
            "last"
          ],
          "fields": "",
          "values": false
        },
        "text": {},
        "textMode": "name"
      },
      "pluginVersion": "9.0.5",
      "targets": [
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${DS_PROMETHEUS}"
          },
          "exemplar": true,
          "expr": "mtxrNote{instance='$instance'}",
          "instant": true,
          "interval": "",
          "legendFormat": " {{mtxrNote}}",
          "refId": "A"
        }
      ],
      "title": "Note",
      "type": "stat"
    },
    {
      "datasource": {
        "type": "prometheus",
        "uid": "${DS_PROMETHEUS}"
      },
      "fieldConfig": {
        "defaults": {
          "color": {
            "mode": "thresholds"
          },
          "decimals": 1,
          "mappings": [],
          "max": 100,
          "min": 1,
          "thresholds": {
            "mode": "percentage",
            "steps": [
              {
                "color": "#299c46",
                "value": null
              },
              {
                "color": "dark-orange",
                "value": 80
              },
              {
                "color": "dark-red",
                "value": 90
              }
            ]
          },
          "unit": "percent"
        },
        "overrides": []
      },
      "gridPos": {
        "h": 5,
        "w": 4,
        "x": 0,
        "y": 6
      },
      "id": 1703,
      "options": {
        "orientation": "auto",
        "reduceOptions": {
          "calcs": [
            "lastNotNull"
          ],
          "fields": "",
          "values": false
        },
        "showThresholdLabels": true,
        "showThresholdMarkers": true,
        "text": {}
      },
      "pluginVersion": "9.0.5",
      "targets": [
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${DS_PROMETHEUS}"
          },
          "exemplar": true,
          "expr": "avg(hrProcessorLoad{instance='$instance'})",
          "instant": true,
          "interval": "",
          "legendFormat": "",
          "refId": "A"
        }
      ],
      "title": "CPU Load",
      "type": "gauge"
    },
    {
      "datasource": {
        "type": "prometheus",
        "uid": "${DS_PROMETHEUS}"
      },
      "fieldConfig": {
        "defaults": {
          "color": {
            "mode": "thresholds"
          },
          "decimals": 1,
          "mappings": [
            {
              "options": {
                "match": "null",
                "result": {
                  "text": "N/A"
                }
              },
              "type": "special"
            }
          ],
          "max": 100,
          "min": 0,
          "thresholds": {
            "mode": "percentage",
            "steps": [
              {
                "color": "#299c46",
                "value": null
              },
              {
                "color": "dark-orange",
                "value": 60
              },
              {
                "color": "dark-red",
                "value": 80
              }
            ]
          },
          "unit": "percent"
        },
        "overrides": []
      },
      "gridPos": {
        "h": 5,
        "w": 4,
        "x": 4,
        "y": 6
      },
      "id": 482,
      "links": [],
      "maxDataPoints": 100,
      "options": {
        "orientation": "horizontal",
        "reduceOptions": {
          "calcs": [
            "mean"
          ],
          "fields": "",
          "values": false
        },
        "showThresholdLabels": true,
        "showThresholdMarkers": true,
        "text": {}
      },
      "pluginVersion": "9.0.5",
      "targets": [
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${DS_PROMETHEUS}"
          },
          "exemplar": true,
          "expr": "(hrStorageUsed{hrStorageIndex='65536',instance='$instance'} * 100 )/(hrStorageSize{hrStorageIndex='65536',instance='$instance'})",
          "instant": true,
          "interval": "",
          "legendFormat": "",
          "refId": "A"
        }
      ],
      "title": "RAM load ",
      "type": "gauge"
    },
    {
      "datasource": {
        "type": "prometheus",
        "uid": "${DS_PROMETHEUS}"
      },
      "fieldConfig": {
        "defaults": {
          "color": {
            "mode": "thresholds"
          },
          "decimals": 1,
          "mappings": [
            {
              "options": {
                "match": "null",
                "result": {
                  "text": "N/A"
                }
              },
              "type": "special"
            }
          ],
          "max": 100,
          "min": 0,
          "thresholds": {
            "mode": "absolute",
            "steps": [
              {
                "color": "#299c46",
                "value": null
              },
              {
                "color": "dark-orange",
                "value": 80
              },
              {
                "color": "dark-red",
                "value": 90
              }
            ]
          },
          "unit": "percent"
        },
        "overrides": []
      },
      "gridPos": {
        "h": 5,
        "w": 4,
        "x": 8,
        "y": 6
      },
      "id": 480,
      "links": [],
      "maxDataPoints": 100,
      "options": {
        "orientation": "horizontal",
        "reduceOptions": {
          "calcs": [
            "mean"
          ],
          "fields": "",
          "values": false
        },
        "showThresholdLabels": true,
        "showThresholdMarkers": true,
        "text": {}
      },
      "pluginVersion": "9.0.5",
      "targets": [
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${DS_PROMETHEUS}"
          },
          "exemplar": true,
          "expr": "(hrStorageUsed{hrStorageIndex='131072',instance='$instance'} * 100 )/(hrStorageSize{hrStorageIndex='131072',instance='$instance'})",
          "instant": true,
          "interval": "",
          "legendFormat": "",
          "refId": "A"
        }
      ],
      "title": "system disk load",
      "type": "gauge"
    },
    {
      "datasource": {
        "type": "prometheus",
        "uid": "${DS_PROMETHEUS}"
      },
      "description": "",
      "fieldConfig": {
        "defaults": {
          "color": {
            "mode": "thresholds"
          },
          "decimals": 1,
          "mappings": [],
          "max": 80,
          "min": 1,
          "noValue": "N/A",
          "thresholds": {
            "mode": "absolute",
            "steps": [
              {
                "color": "light-blue",
                "value": null
              },
              {
                "color": "#299c46",
                "value": 20
              },
              {
                "color": "dark-orange",
                "value": 55
              },
              {
                "color": "dark-red",
                "value": 65
              }
            ]
          },
          "unit": "celsius"
        },
        "overrides": []
      },
      "gridPos": {
        "h": 5,
        "w": 4,
        "x": 12,
        "y": 6
      },
      "id": 1237,
      "options": {
        "orientation": "auto",
        "reduceOptions": {
          "calcs": [
            "lastNotNull"
          ],
          "fields": "",
          "values": false
        },
        "showThresholdLabels": true,
        "showThresholdMarkers": true,
        "text": {}
      },
      "pluginVersion": "9.0.5",
      "targets": [
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${DS_PROMETHEUS}"
          },
          "exemplar": true,
          "expr": "mtxrHlProcessorTemperature{instance='$instance'}/10 or mtxrHlTemperature{instance='$instance'}/10",
          "instant": true,
          "interval": "",
          "legendFormat": "",
          "refId": "A"
        }
      ],
      "title": "CPU Temp",
      "type": "gauge"
    },
    {
      "datasource": {
        "type": "prometheus",
        "uid": "${DS_PROMETHEUS}"
      },
      "description": "",
      "fieldConfig": {
        "defaults": {
          "color": {
            "mode": "palette-classic"
          },
          "custom": {
            "axisLabel": "",
            "axisPlacement": "auto",
            "barAlignment": 0,
            "drawStyle": "line",
            "fillOpacity": 30,
            "gradientMode": "opacity",
            "hideFrom": {
              "legend": false,
              "tooltip": false,
              "viz": false
            },
            "lineInterpolation": "smooth",
            "lineStyle": {
              "fill": "solid"
            },
            "lineWidth": 2,
            "pointSize": 5,
            "scaleDistribution": {
              "type": "linear"
            },
            "showPoints": "never",
            "spanNulls": true,
            "stacking": {
              "group": "A",
              "mode": "none"
            },
            "thresholdsStyle": {
              "mode": "line"
            }
          },
          "mappings": [],
          "thresholds": {
            "mode": "absolute",
            "steps": [
              {
                "color": "green",
                "value": null
              }
            ]
          },
          "unit": "percent"
        },
        "overrides": []
      },
      "gridPos": {
        "h": 13,
        "w": 8,
        "x": 16,
        "y": 6
      },
      "id": 1262,
      "links": [],
      "maxDataPoints": 100,
      "options": {
        "legend": {
          "calcs": [],
          "displayMode": "list",
          "placement": "bottom"
        },
        "tooltip": {
          "mode": "multi",
          "sort": "none"
        }
      },
      "pluginVersion": "8.2.1",
      "repeatDirection": "h",
      "targets": [
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${DS_PROMETHEUS}"
          },
          "exemplar": true,
          "expr": "hrProcessorLoad{instance='$instance'}",
          "interval": "",
          "legendFormat": "CPU {{hrDeviceIndex}}  load",
          "refId": "A"
        },
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${DS_PROMETHEUS}"
          },
          "exemplar": true,
          "expr": "mtxrHlTemperature{instance='$instance'}/10",
          "format": "time_series",
          "hide": false,
          "instant": false,
          "interval": "",
          "legendFormat": "CPU temp",
          "refId": "B"
        },
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${DS_PROMETHEUS}"
          },
          "exemplar": true,
          "expr": "(hrStorageUsed{hrStorageIndex='65536',instance='$instance'} * 100 )/(hrStorageSize{hrStorageIndex='65536',instance='$instance'})",
          "hide": false,
          "interval": "",
          "legendFormat": "RAM usage",
          "refId": "C"
        },
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${DS_PROMETHEUS}"
          },
          "exemplar": true,
          "expr": "(hrStorageUsed{hrStorageIndex='131072',instance='$instance'} * 100 )/(hrStorageSize{hrStorageIndex='131072',instance='$instance'})",
          "hide": false,
          "interval": "",
          "legendFormat": "System disk",
          "refId": "D"
        },
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${DS_PROMETHEUS}"
          },
          "exemplar": true,
          "expr": "mtxrHlVoltage{instance='$instance'}/10",
          "hide": false,
          "interval": "",
          "legendFormat": "Voltage",
          "refId": "E"
        }
      ],
      "title": "System",
      "type": "timeseries"
    },
    {
      "datasource": {
        "type": "prometheus",
        "uid": "${DS_PROMETHEUS}"
      },
      "description": "",
      "fieldConfig": {
        "defaults": {
          "color": {
            "mode": "thresholds"
          },
          "mappings": [],
          "thresholds": {
            "mode": "absolute",
            "steps": [
              {
                "color": "#299c46",
                "value": null
              }
            ]
          },
          "unit": "MHz"
        },
        "overrides": []
      },
      "gridPos": {
        "h": 4,
        "w": 4,
        "x": 0,
        "y": 11
      },
      "id": 1240,
      "options": {
        "colorMode": "value",
        "graphMode": "none",
        "justifyMode": "auto",
        "orientation": "auto",
        "reduceOptions": {
          "calcs": [
            "lastNotNull"
          ],
          "fields": "",
          "values": false
        },
        "text": {},
        "textMode": "auto"
      },
      "pluginVersion": "9.0.5",
      "targets": [
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${DS_PROMETHEUS}"
          },
          "exemplar": true,
          "expr": "mtxrHlProcessorFrequency{instance='$instance'}",
          "hide": false,
          "instant": true,
          "interval": "",
          "legendFormat": "",
          "refId": "A"
        }
      ],
      "title": "CPU frequency",
      "type": "stat"
    },
    {
      "datasource": {
        "type": "prometheus",
        "uid": "${DS_PROMETHEUS}"
      },
      "description": "",
      "fieldConfig": {
        "defaults": {
          "color": {
            "mode": "thresholds"
          },
          "mappings": [],
          "thresholds": {
            "mode": "absolute",
            "steps": [
              {
                "color": "#299c46",
                "value": null
              }
            ]
          }
        },
        "overrides": []
      },
      "gridPos": {
        "h": 4,
        "w": 4,
        "x": 4,
        "y": 11
      },
      "id": 1242,
      "options": {
        "colorMode": "value",
        "graphMode": "none",
        "justifyMode": "auto",
        "orientation": "auto",
        "reduceOptions": {
          "calcs": [
            "last"
          ],
          "fields": "/^n/a$/",
          "values": false
        },
        "text": {},
        "textMode": "name"
      },
      "pluginVersion": "9.0.5",
      "targets": [
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${DS_PROMETHEUS}"
          },
          "exemplar": true,
          "expr": "mtxrHlActiveFan{instance='$instance'}",
          "hide": false,
          "instant": true,
          "interval": "",
          "legendFormat": "{{mtxrHlActiveFan}}",
          "refId": "A"
        }
      ],
      "title": "Active Fan",
      "type": "stat"
    },
    {
      "datasource": {
        "type": "prometheus",
        "uid": "${DS_PROMETHEUS}"
      },
      "description": "Wireless registration table entry count",
      "fieldConfig": {
        "defaults": {
          "color": {
            "mode": "thresholds"
          },
          "mappings": [],
          "thresholds": {
            "mode": "absolute",
            "steps": [
              {
                "color": "#299c46",
                "value": null
              }
            ]
          }
        },
        "overrides": []
      },
      "gridPos": {
        "h": 4,
        "w": 4,
        "x": 8,
        "y": 11
      },
      "id": 1645,
      "options": {
        "colorMode": "value",
        "graphMode": "none",
        "justifyMode": "auto",
        "orientation": "auto",
        "reduceOptions": {
          "calcs": [
            "lastNotNull"
          ],
          "fields": "",
          "values": false
        },
        "text": {},
        "textMode": "auto"
      },
      "pluginVersion": "9.0.5",
      "targets": [
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${DS_PROMETHEUS}"
          },
          "exemplar": true,
          "expr": "mtxrWlRtabEntryCount{instance='$instance'}",
          "format": "time_series",
          "hide": false,
          "instant": true,
          "interval": "",
          "legendFormat": "",
          "refId": "A"
        }
      ],
      "title": "Wi-Fi client count",
      "type": "stat"
    },
    {
      "datasource": {
        "type": "prometheus",
        "uid": "${DS_PROMETHEUS}"
      },
      "description": "",
      "fieldConfig": {
        "defaults": {
          "color": {
            "mode": "thresholds"
          },
          "mappings": [
            {
              "options": {
                "result": {
                  "text": ""
                },
                "to": 0
              },
              "type": "range"
            }
          ],
          "thresholds": {
            "mode": "absolute",
            "steps": [
              {
                "color": "#299c46",
                "value": null
              },
              {
                "color": "red",
                "value": 80
              }
            ]
          },
          "unit": "none"
        },
        "overrides": []
      },
      "gridPos": {
        "h": 4,
        "w": 4,
        "x": 12,
        "y": 11
      },
      "id": 1260,
      "links": [],
      "maxDataPoints": 100,
      "options": {
        "colorMode": "value",
        "graphMode": "none",
        "justifyMode": "center",
        "orientation": "auto",
        "reduceOptions": {
          "calcs": [
            "lastNotNull"
          ],
          "fields": "",
          "values": false
        },
        "text": {},
        "textMode": "value_and_name"
      },
      "pluginVersion": "9.0.5",
      "targets": [
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${DS_PROMETHEUS}"
          },
          "exemplar": true,
          "expr": "mtxrLicLevel{instance='$instance'}",
          "interval": "",
          "legendFormat": "Lic",
          "refId": "A"
        },
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${DS_PROMETHEUS}"
          },
          "exemplar": true,
          "expr": "mtxrLicUpgradableTo{instance='$instance'}",
          "hide": false,
          "interval": "",
          "legendFormat": "Upgradable to",
          "refId": "B"
        }
      ],
      "title": "License level",
      "type": "stat"
    },
    {
      "datasource": {
        "type": "prometheus",
        "uid": "${DS_PROMETHEUS}"
      },
      "fieldConfig": {
        "defaults": {
          "color": {
            "mode": "thresholds"
          },
          "mappings": [
            {
              "options": {
                "1": {
                  "text": "Disabled"
                },
                "2": {
                  "text": "Waiting"
                },
                "3": {
                  "text": "Powered On"
                },
                "4": {
                  "text": "Overload"
                }
              },
              "type": "value"
            }
          ],
          "max": 4,
          "min": 1,
          "thresholds": {
            "mode": "absolute",
            "steps": [
              {
                "color": "blue",
                "value": null
              },
              {
                "color": "dark-yellow",
                "value": 2
              },
              {
                "color": "#299c46",
                "value": 3
              },
              {
                "color": "dark-red",
                "value": 4
              }
            ]
          }
        },
        "overrides": []
      },
      "gridPos": {
        "h": 4,
        "w": 4,
        "x": 0,
        "y": 15
      },
      "id": 1276,
      "options": {
        "colorMode": "value",
        "graphMode": "none",
        "justifyMode": "center",
        "orientation": "auto",
        "reduceOptions": {
          "calcs": [
            "lastNotNull"
          ],
          "fields": "",
          "values": false
        },
        "text": {},
        "textMode": "value"
      },
      "pluginVersion": "9.0.5",
      "targets": [
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${DS_PROMETHEUS}"
          },
          "exemplar": true,
          "expr": "mtxrPOEStatus{instance='$instance'}",
          "format": "time_series",
          "hide": false,
          "instant": true,
          "interval": "",
          "legendFormat": "",
          "refId": "A"
        }
      ],
      "title": "POE Status",
      "type": "stat"
    },
    {
      "datasource": {
        "type": "prometheus",
        "uid": "${DS_PROMETHEUS}"
      },
      "description": "",
      "fieldConfig": {
        "defaults": {
          "color": {
            "mode": "thresholds"
          },
          "mappings": [],
          "thresholds": {
            "mode": "absolute",
            "steps": [
              {
                "color": "#299c46",
                "value": null
              }
            ]
          },
          "unit": "watt"
        },
        "overrides": []
      },
      "gridPos": {
        "h": 4,
        "w": 4,
        "x": 4,
        "y": 15
      },
      "id": 1279,
      "options": {
        "colorMode": "value",
        "graphMode": "none",
        "justifyMode": "center",
        "orientation": "auto",
        "reduceOptions": {
          "calcs": [
            "lastNotNull"
          ],
          "fields": "",
          "values": false
        },
        "text": {},
        "textMode": "auto"
      },
      "pluginVersion": "9.0.5",
      "targets": [
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${DS_PROMETHEUS}"
          },
          "exemplar": true,
          "expr": "mtxrPOEPower{instance='$instance'}",
          "format": "time_series",
          "hide": false,
          "instant": true,
          "interval": "",
          "legendFormat": "POE Power",
          "refId": "A"
        }
      ],
      "title": "POE Power",
      "type": "stat"
    },
    {
      "datasource": {
        "type": "prometheus",
        "uid": "${DS_PROMETHEUS}"
      },
      "fieldConfig": {
        "defaults": {
          "color": {
            "mode": "thresholds"
          },
          "mappings": [],
          "thresholds": {
            "mode": "absolute",
            "steps": [
              {
                "color": "#299c46",
                "value": null
              }
            ]
          },
          "unit": "mamp"
        },
        "overrides": []
      },
      "gridPos": {
        "h": 4,
        "w": 4,
        "x": 8,
        "y": 15
      },
      "id": 1277,
      "options": {
        "colorMode": "value",
        "graphMode": "none",
        "justifyMode": "center",
        "orientation": "auto",
        "reduceOptions": {
          "calcs": [
            "lastNotNull"
          ],
          "fields": "",
          "values": false
        },
        "text": {},
        "textMode": "value"
      },
      "pluginVersion": "9.0.5",
      "targets": [
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${DS_PROMETHEUS}"
          },
          "exemplar": true,
          "expr": "mtxrPOECurrent{instance='$instance'}",
          "format": "time_series",
          "hide": false,
          "instant": true,
          "interval": "",
          "legendFormat": "POE Current",
          "refId": "A"
        }
      ],
      "title": "POE Current",
      "type": "stat"
    },
    {
      "datasource": {
        "type": "prometheus",
        "uid": "${DS_PROMETHEUS}"
      },
      "fieldConfig": {
        "defaults": {
          "color": {
            "mode": "thresholds"
          },
          "mappings": [],
          "thresholds": {
            "mode": "absolute",
            "steps": [
              {
                "color": "#299c46",
                "value": null
              }
            ]
          },
          "unit": "volt"
        },
        "overrides": []
      },
      "gridPos": {
        "h": 4,
        "w": 4,
        "x": 12,
        "y": 15
      },
      "id": 1278,
      "options": {
        "colorMode": "value",
        "graphMode": "none",
        "justifyMode": "center",
        "orientation": "auto",
        "reduceOptions": {
          "calcs": [
            "lastNotNull"
          ],
          "fields": "",
          "values": false
        },
        "text": {},
        "textMode": "auto"
      },
      "pluginVersion": "9.0.5",
      "targets": [
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${DS_PROMETHEUS}"
          },
          "exemplar": true,
          "expr": "mtxrPOEVoltage{instance='$instance'}",
          "format": "time_series",
          "hide": false,
          "instant": true,
          "interval": "",
          "legendFormat": "POE Voltage",
          "refId": "A"
        }
      ],
      "title": "POE Voltage",
      "type": "stat"
    },
    {
      "datasource": {
        "type": "prometheus",
        "uid": "${DS_PROMETHEUS}"
      },
      "description": "",
      "fieldConfig": {
        "defaults": {
          "color": {
            "mode": "palette-classic"
          },
          "custom": {
            "axisLabel": "",
            "axisPlacement": "auto",
            "barAlignment": 0,
            "drawStyle": "line",
            "fillOpacity": 10,
            "gradientMode": "hue",
            "hideFrom": {
              "legend": false,
              "tooltip": false,
              "viz": false
            },
            "lineInterpolation": "smooth",
            "lineWidth": 2,
            "pointSize": 5,
            "scaleDistribution": {
              "type": "linear"
            },
            "showPoints": "never",
            "spanNulls": false,
            "stacking": {
              "group": "A",
              "mode": "none"
            },
            "thresholdsStyle": {
              "mode": "off"
            }
          },
          "mappings": [],
          "thresholds": {
            "mode": "absolute",
            "steps": [
              {
                "color": "green",
                "value": null
              }
            ]
          },
          "unit": "bps"
        },
        "overrides": []
      },
      "gridPos": {
        "h": 8,
        "w": 24,
        "x": 0,
        "y": 19
      },
      "id": 1239,
      "options": {
        "legend": {
          "calcs": [
            "mean",
            "lastNotNull",
            "max"
          ],
          "displayMode": "table",
          "placement": "right"
        },
        "tooltip": {
          "mode": "multi",
          "sort": "none"
        }
      },
      "pluginVersion": "8.2.1",
      "targets": [
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${DS_PROMETHEUS}"
          },
          "exemplar": true,
          "expr": "irate(ifHCInOctets{ifName=~'$Interface',instance='$instance'}[$__rate_interval])*8",
          "format": "time_series",
          "hide": false,
          "interval": "",
          "intervalFactor": 1,
          "legendFormat": "In - {{ifName}}",
          "refId": "C"
        },
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${DS_PROMETHEUS}"
          },
          "exemplar": true,
          "expr": "-irate(ifHCOutOctets{ifName=~'$Interface',instance='$instance'}[$__rate_interval])*8",
          "hide": false,
          "interval": "",
          "intervalFactor": 1,
          "legendFormat": "Out - {{ifName}}",
          "refId": "A"
        }
      ],
      "title": "Network Traffic Basic",
      "type": "timeseries"
    },
    {
      "datasource": {
        "type": "prometheus",
        "uid": "${DS_PROMETHEUS}"
      },
      "description": "Status link/states: The current operational state of the interface",
      "fieldConfig": {
        "defaults": {
          "color": {
            "mode": "thresholds"
          },
          "custom": {
            "align": "auto",
            "displayMode": "color-text",
            "filterable": false,
            "inspect": false
          },
          "mappings": [],
          "thresholds": {
            "mode": "absolute",
            "steps": [
              {
                "color": "super-light-yellow",
                "value": null
              }
            ]
          },
          "unit": "short"
        },
        "overrides": [
          {
            "matcher": {
              "id": "byType",
              "options": "string"
            },
            "properties": [
              {
                "id": "custom.align",
                "value": "center"
              }
            ]
          },
          {
            "matcher": {
              "id": "byType",
              "options": "number"
            },
            "properties": [
              {
                "id": "custom.align",
                "value": "center"
              }
            ]
          },
          {
            "matcher": {
              "id": "byName",
              "options": "Status link/states"
            },
            "properties": [
              {
                "id": "thresholds",
                "value": {
                  "mode": "absolute",
                  "steps": [
                    {
                      "color": "green",
                      "value": null
                    },
                    {
                      "color": "#299c46",
                      "value": 1
                    },
                    {
                      "color": "semi-dark-red",
                      "value": 2
                    },
                    {
                      "color": "#EAB839",
                      "value": 3
                    },
                    {
                      "color": "#6a6a6a",
                      "value": 4
                    },
                    {
                      "color": "#6ED0E0",
                      "value": 5
                    },
                    {
                      "color": "#EF843C",
                      "value": 6
                    },
                    {
                      "color": "dark-purple",
                      "value": 7
                    }
                  ]
                }
              },
              {
                "id": "mappings",
                "value": [
                  {
                    "options": {
                      "1": {
                        "index": 6,
                        "text": "UP"
                      },
                      "2": {
                        "index": 5,
                        "text": "DOWN"
                      },
                      "3": {
                        "index": 4,
                        "text": "Testing"
                      },
                      "4": {
                        "index": 3,
                        "text": "Unknown"
                      },
                      "5": {
                        "index": 2,
                        "text": "Dormant"
                      },
                      "6": {
                        "index": 1,
                        "text": "Not present"
                      },
                      "7": {
                        "index": 0,
                        "text": "lowerLayerDown"
                      }
                    },
                    "type": "value"
                  }
                ]
              },
              {
                "id": "custom.width",
                "value": 130
              },
              {
                "id": "custom.displayMode",
                "value": "color-background"
              }
            ]
          },
          {
            "matcher": {
              "id": "byName",
              "options": "Rate"
            },
            "properties": [
              {
                "id": "unit",
                "value": "bps"
              },
              {
                "id": "thresholds",
                "value": {
                  "mode": "absolute",
                  "steps": [
                    {
                      "color": "rgb(77, 79, 79)",
                      "value": null
                    },
                    {
                      "color": "#EAB839",
                      "value": 50000000
                    },
                    {
                      "color": "#6ED0E0",
                      "value": 100000000
                    },
                    {
                      "color": "#299c46",
                      "value": 1000000000
                    },
                    {
                      "color": "semi-dark-purple",
                      "value": 1000000010
                    }
                  ]
                }
              },
              {
                "id": "custom.width",
                "value": 119
              }
            ]
          },
          {
            "matcher": {
              "id": "byName",
              "options": "TX Sum"
            },
            "properties": [
              {
                "id": "unit",
                "value": "bytes"
              },
              {
                "id": "thresholds",
                "value": {
                  "mode": "absolute",
                  "steps": [
                    {
                      "color": "rgb(77, 79, 79)",
                      "value": null
                    },
                    {
                      "color": "super-light-yellow",
                      "value": 1
                    }
                  ]
                }
              },
              {
                "id": "custom.width",
                "value": 118
              }
            ]
          },
          {
            "matcher": {
              "id": "byName",
              "options": "RX Sum"
            },
            "properties": [
              {
                "id": "unit",
                "value": "bytes"
              },
              {
                "id": "thresholds",
                "value": {
                  "mode": "absolute",
                  "steps": [
                    {
                      "color": "rgb(77, 79, 79)",
                      "value": null
                    },
                    {
                      "color": "super-light-yellow",
                      "value": 1
                    }
                  ]
                }
              },
              {
                "id": "custom.width",
                "value": 118
              }
            ]
          },
          {
            "matcher": {
              "id": "byName",
              "options": "MAC"
            },
            "properties": [
              {
                "id": "custom.width",
                "value": 152
              }
            ]
          },
          {
            "matcher": {
              "id": "byName",
              "options": "Link down count"
            },
            "properties": [
              {
                "id": "custom.width",
                "value": 118
              },
              {
                "id": "thresholds",
                "value": {
                  "mode": "absolute",
                  "steps": [
                    {
                      "color": "rgb(77, 79, 79)",
                      "value": null
                    },
                    {
                      "color": "super-light-yellow",
                      "value": 1
                    }
                  ]
                }
              }
            ]
          },
          {
            "matcher": {
              "id": "byName",
              "options": "Int. index"
            },
            "properties": [
              {
                "id": "custom.width",
                "value": 88
              }
            ]
          },
          {
            "matcher": {
              "id": "byName",
              "options": "MTU"
            },
            "properties": [
              {
                "id": "custom.width",
                "value": 118
              },
              {
                "id": "unit",
                "value": "none"
              }
            ]
          },
          {
            "matcher": {
              "id": "byName",
              "options": "Type of interface"
            },
            "properties": [
              {
                "id": "custom.width",
                "value": 140
              },
              {
                "id": "mappings",
                "value": [
                  {
                    "options": {
                      "ethernetCsmacd": {
                        "text": "Physical"
                      },
                      "ieee80211": {
                        "text": "Wireless"
                      }
                    },
                    "type": "value"
                  }
                ]
              },
              {
                "id": "custom.filterable",
                "value": true
              }
            ]
          },
          {
            "matcher": {
              "id": "byName",
              "options": "Name"
            },
            "properties": [
              {
                "id": "custom.width"
              }
            ]
          }
        ]
      },
      "gridPos": {
        "h": 12,
        "w": 24,
        "x": 0,
        "y": 27
      },
      "id": 1275,
      "options": {
        "footer": {
          "fields": "",
          "reducer": [
            "sum"
          ],
          "show": false
        },
        "frameIndex": 0,
        "showHeader": true,
        "sortBy": [
          {
            "desc": false,
            "displayName": "MAC"
          }
        ]
      },
      "pluginVersion": "9.0.5",
      "targets": [
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${DS_PROMETHEUS}"
          },
          "exemplar": true,
          "expr": "ifPhysAddress{instance='$instance'}",
          "format": "table",
          "instant": true,
          "interval": "",
          "legendFormat": "",
          "refId": "A"
        },
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${DS_PROMETHEUS}"
          },
          "exemplar": true,
          "expr": "ifOperStatus{instance='$instance'}",
          "format": "table",
          "hide": false,
          "instant": true,
          "interval": "",
          "legendFormat": "",
          "refId": "B"
        },
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${DS_PROMETHEUS}"
          },
          "exemplar": true,
          "expr": "mtxrInterfaceStatsRxBytes{instance='$instance'}",
          "format": "table",
          "hide": false,
          "instant": true,
          "interval": "",
          "legendFormat": "",
          "refId": "C"
        },
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${DS_PROMETHEUS}"
          },
          "exemplar": true,
          "expr": "mtxrInterfaceStatsTxBytes{instance='$instance'}",
          "format": "table",
          "hide": false,
          "instant": true,
          "interval": "",
          "legendFormat": "",
          "refId": "D"
        },
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${DS_PROMETHEUS}"
          },
          "exemplar": true,
          "expr": "ifSpeed{instance='$instance'}",
          "format": "table",
          "hide": false,
          "instant": true,
          "interval": "",
          "legendFormat": "",
          "refId": "E"
        },
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${DS_PROMETHEUS}"
          },
          "exemplar": true,
          "expr": "mtxrInterfaceStatsLinkDowns{instance='$instance'}",
          "format": "table",
          "hide": false,
          "instant": true,
          "interval": "",
          "legendFormat": "",
          "refId": "F"
        },
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${DS_PROMETHEUS}"
          },
          "exemplar": true,
          "expr": "ifMtu{instance='$instance'}",
          "format": "table",
          "hide": false,
          "instant": true,
          "interval": "",
          "legendFormat": "",
          "refId": "G"
        },
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${DS_PROMETHEUS}"
          },
          "exemplar": true,
          "expr": "ifType_info{instance='$instance'}",
          "format": "table",
          "hide": false,
          "instant": true,
          "interval": "",
          "legendFormat": "",
          "refId": "H"
        },
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${DS_PROMETHEUS}"
          },
          "exemplar": true,
          "expr": "mtxrPOEInterfaceIndex{instance='$instance'}",
          "format": "table",
          "hide": false,
          "instant": true,
          "interval": "",
          "legendFormat": "",
          "refId": "I"
        },
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${DS_PROMETHEUS}"
          },
          "exemplar": true,
          "expr": "ifAlias{instance='$instance'}",
          "format": "table",
          "hide": false,
          "instant": true,
          "interval": "",
          "legendFormat": "",
          "refId": "J"
        }
      ],
      "title": "Interfaces",
      "transformations": [
        {
          "id": "seriesToColumns",
          "options": {
            "byField": "ifName"
          }
        },
        {
          "id": "organize",
          "options": {
            "excludeByName": {
              "Time": true,
              "Time 1": true,
              "Time 2": true,
              "Time 3": true,
              "Time 4": true,
              "Time 5": true,
              "Time 6": true,
              "Time 7": true,
              "Time 8": true,
              "Time 9": true,
              "Value #A": true,
              "Value #H": true,
              "Value #J": true,
              "__name__": true,
              "__name__ 1": true,
              "__name__ 2": true,
              "__name__ 3": true,
              "__name__ 4": true,
              "__name__ 5": true,
              "__name__ 6": true,
              "__name__ 7": true,
              "__name__ 8": true,
              "__name__ 9": true,
              "ifIndex": false,
              "ifIndex 1": true,
              "ifIndex 2": true,
              "ifIndex 3": true,
              "ifIndex 4": true,
              "ifIndex 5": true,
              "ifIndex 6": true,
              "instance": true,
              "instance 1": true,
              "instance 2": true,
              "instance 3": true,
              "instance 4": true,
              "instance 5": true,
              "instance 6": true,
              "instance 7": true,
              "instance 8": true,
              "instance 9": true,
              "job": true,
              "job 1": true,
              "job 2": true,
              "job 3": true,
              "job 4": true,
              "job 5": true,
              "job 6": true,
              "job 7": true,
              "job 8": true,
              "job 9": true,
              "mtxrInterfaceStatsIndex": true,
              "mtxrInterfaceStatsIndex 1": true,
              "mtxrInterfaceStatsIndex 2": true,
              "mtxrInterfaceStatsIndex 3": true
            },
            "indexByName": {
              "Time": 12,
              "Value #A": 16,
              "Value #B": 3,
              "Value #C": 8,
              "Value #D": 9,
              "Value #E": 6,
              "Value #F": 4,
              "Value #G": 7,
              "Value #H": 11,
              "Value #J": 18,
              "__name__": 13,
              "ifAlias": 10,
              "ifIndex": 0,
              "ifName": 2,
              "ifPhysAddress": 5,
              "ifType": 1,
              "instance": 14,
              "job": 15,
              "mtxrInterfaceStatsIndex": 17
            },
            "renameByName": {
              "Time": "",
              "Value #A": "",
              "Value #B": "Status link/states",
              "Value #C": "RX Sum",
              "Value #D": "TX Sum",
              "Value #E": "Rate",
              "Value #F": "Link down count",
              "Value #G": "MTU",
              "Value #H": "",
              "Value #J": "",
              "__name__": "",
              "ifAlias": "Comment",
              "ifIndex": "Int. index",
              "ifName": "Name",
              "ifPhysAddress": "MAC",
              "ifType": "Type of interface",
              "instance": "",
              "mtxrInterfaceStatsIndex": "",
              "mtxrInterfaceStatsIndex 1": ""
            }
          }
        }
      ],
      "type": "table"
    },
    {
      "aliasColors": {
        "In - wlan1": "#ff2e63"
      },
      "bars": false,
      "dashLength": 10,
      "dashes": false,
      "datasource": {
        "type": "prometheus",
        "uid": "${DS_PROMETHEUS}"
      },
      "description": "Showing values > 0",
      "fill": 1,
      "fillGradient": 0,
      "gridPos": {
        "h": 6,
        "w": 12,
        "x": 0,
        "y": 39
      },
      "hiddenSeries": false,
      "id": 1659,
      "legend": {
        "alignAsTable": true,
        "avg": true,
        "current": true,
        "hideEmpty": false,
        "hideZero": true,
        "max": true,
        "min": false,
        "rightSide": true,
        "show": true,
        "total": false,
        "values": true
      },
      "lines": true,
      "linewidth": 1,
      "nullPointMode": "connected",
      "options": {
        "alertThreshold": true
      },
      "percentage": false,
      "pluginVersion": "9.0.5",
      "pointradius": 2,
      "points": false,
      "renderer": "flot",
      "seriesOverrides": [],
      "spaceLength": 10,
      "stack": false,
      "steppedLine": false,
      "targets": [
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${DS_PROMETHEUS}"
          },
          "exemplar": true,
          "expr": "irate(mtxrInterfaceStatsTxControl{ifName=~'$Interface',instance='$instance'}[$__rate_interval])",
          "hide": false,
          "interval": "",
          "intervalFactor": 1,
          "legendFormat": "Tx Control - {{ifName}}",
          "refId": "A"
        },
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${DS_PROMETHEUS}"
          },
          "exemplar": true,
          "expr": "irate(mtxrInterfaceStatsTxDeferred{ifName=~'$Interface',instance='$instance'}[$__rate_interval])",
          "hide": false,
          "interval": "",
          "intervalFactor": 1,
          "legendFormat": "Tx Deferred - {{ifName}}",
          "refId": "B"
        },
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${DS_PROMETHEUS}"
          },
          "exemplar": true,
          "expr": "irate(mtxrInterfaceStatsTxCollision{ifName=~'$Interface',instance='$instance'}[$__rate_interval])",
          "format": "time_series",
          "hide": false,
          "instant": false,
          "interval": "",
          "intervalFactor": 1,
          "legendFormat": "Tx Collision - {{ifName}}",
          "refId": "C"
        },
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${DS_PROMETHEUS}"
          },
          "exemplar": true,
          "expr": "irate(mtxrInterfaceStatsTxDrop{ifName=~'$Interface',instance='$instance'}[$__rate_interval])",
          "format": "time_series",
          "hide": false,
          "instant": false,
          "interval": "",
          "intervalFactor": 1,
          "legendFormat": "Tx Drop - {{ifName}}",
          "refId": "D"
        },
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${DS_PROMETHEUS}"
          },
          "exemplar": true,
          "expr": "irate(mtxrInterfaceStatsTxExcessiveCollision{ifName=~'$Interface',instance='$instance'}[$__rate_interval])",
          "format": "time_series",
          "hide": false,
          "instant": false,
          "interval": "",
          "intervalFactor": 1,
          "legendFormat": "Tx Excessive Collision - {{ifName}}",
          "refId": "E"
        },
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${DS_PROMETHEUS}"
          },
          "exemplar": true,
          "expr": "irate(mtxrInterfaceStatsTxExcessiveDeferred{ifName=~'$Interface',instance='$instance'}[$__rate_interval])",
          "format": "time_series",
          "hide": false,
          "instant": false,
          "interval": "",
          "intervalFactor": 1,
          "legendFormat": "Tx Excessive Deferred - {{ifName}}",
          "refId": "F"
        },
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${DS_PROMETHEUS}"
          },
          "exemplar": true,
          "expr": "irate(mtxrInterfaceStatsTxFCSError{ifName=~'$Interface',instance='$instance'}[$__rate_interval])",
          "format": "time_series",
          "hide": false,
          "instant": false,
          "interval": "",
          "intervalFactor": 1,
          "legendFormat": "Tx FCS Error - {{ifName}}",
          "refId": "G"
        },
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${DS_PROMETHEUS}"
          },
          "exemplar": true,
          "expr": "irate(mtxrInterfaceStatsTxFragment{ifName=~'$Interface',instance='$instance'}[$__rate_interval])",
          "format": "time_series",
          "hide": false,
          "instant": false,
          "interval": "",
          "intervalFactor": 1,
          "legendFormat": "Tx Fragment - {{ifName}}",
          "refId": "H"
        },
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${DS_PROMETHEUS}"
          },
          "exemplar": true,
          "expr": "irate(mtxrInterfaceStatsTxJabber{ifName=~'$Interface',instance='$instance'}[$__rate_interval])",
          "format": "time_series",
          "hide": false,
          "instant": false,
          "interval": "",
          "intervalFactor": 1,
          "legendFormat": "Tx Jabber - {{ifName}}",
          "refId": "I"
        },
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${DS_PROMETHEUS}"
          },
          "exemplar": true,
          "expr": "irate(mtxrInterfaceStatsTxLateCollision{ifName=~'$Interface',instance='$instance'}[$__rate_interval])",
          "format": "time_series",
          "hide": false,
          "instant": false,
          "interval": "",
          "intervalFactor": 1,
          "legendFormat": "Tx Late Collision - {{ifName}}",
          "refId": "J"
        },
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${DS_PROMETHEUS}"
          },
          "exemplar": true,
          "expr": "irate(mtxrInterfaceStatsTxMultipleCollision{ifName=~'$Interface',instance='$instance'}[$__rate_interval])",
          "format": "time_series",
          "hide": false,
          "instant": false,
          "interval": "",
          "intervalFactor": 1,
          "legendFormat": "Tx Multiple Collision - {{ifName}}",
          "refId": "K"
        },
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${DS_PROMETHEUS}"
          },
          "exemplar": true,
          "expr": "irate(mtxrInterfaceStatsTxPause{ifName=~'$Interface',instance='$instance'}[$__rate_interval])",
          "format": "time_series",
          "hide": false,
          "instant": false,
          "interval": "",
          "intervalFactor": 1,
          "legendFormat": "Tx Pause - {{ifName}}",
          "refId": "L"
        },
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${DS_PROMETHEUS}"
          },
          "exemplar": true,
          "expr": "irate(mtxrInterfaceStatsTxPauseHonored{ifName=~'$Interface',instance='$instance'}[$__rate_interval])",
          "format": "time_series",
          "hide": false,
          "instant": false,
          "interval": "",
          "intervalFactor": 1,
          "legendFormat": "Tx Pause Honored - {{ifName}}",
          "refId": "M"
        },
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${DS_PROMETHEUS}"
          },
          "exemplar": true,
          "expr": "irate(mtxrInterfaceStatsTxSingleCollision{ifName=~'$Interface',instance='$instance'}[$__rate_interval])",
          "format": "time_series",
          "hide": false,
          "instant": false,
          "interval": "",
          "intervalFactor": 1,
          "legendFormat": "Tx Single Collision - {{ifName}}",
          "refId": "N"
        },
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${DS_PROMETHEUS}"
          },
          "exemplar": true,
          "expr": "irate(mtxrInterfaceStatsTxTooLong{ifName=~'$Interface',instance='$instance'}[$__rate_interval])",
          "format": "time_series",
          "hide": false,
          "instant": false,
          "interval": "",
          "intervalFactor": 1,
          "legendFormat": "Tx Too Long - {{ifName}}",
          "refId": "O"
        },
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${DS_PROMETHEUS}"
          },
          "exemplar": true,
          "expr": "irate(mtxrInterfaceStatsTxTooShort{ifName=~'$Interface',instance='$instance'}[$__rate_interval])",
          "format": "time_series",
          "hide": false,
          "instant": false,
          "interval": "",
          "intervalFactor": 1,
          "legendFormat": "Tx Too Short - {{ifName}}",
          "refId": "P"
        },
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${DS_PROMETHEUS}"
          },
          "exemplar": true,
          "expr": "irate(mtxrInterfaceStatsTxTotalCollision{ifName=~'$Interface',instance='$instance'}[$__rate_interval])",
          "format": "time_series",
          "hide": false,
          "instant": false,
          "interval": "",
          "intervalFactor": 1,
          "legendFormat": "Tx Total Collision - {{ifName}}",
          "refId": "Q"
        },
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${DS_PROMETHEUS}"
          },
          "exemplar": true,
          "expr": "irate(mtxrInterfaceStatsTxUnderrun{ifName=~'$Interface',instance='$instance'}[$__rate_interval])",
          "format": "time_series",
          "hide": false,
          "instant": false,
          "interval": "",
          "intervalFactor": 1,
          "legendFormat": "Tx Under run - {{ifName}}",
          "refId": "R"
        }
      ],
      "thresholds": [],
      "timeRegions": [],
      "title": "Tx Eth errors, etc",
      "tooltip": {
        "shared": true,
        "sort": 0,
        "value_type": "individual"
      },
      "type": "graph",
      "xaxis": {
        "mode": "time",
        "show": true,
        "values": []
      },
      "yaxes": [
        {
          "format": "bps",
          "label": "",
          "logBase": 1,
          "show": true
        },
        {
          "format": "short",
          "logBase": 1,
          "show": false
        }
      ],
      "yaxis": {
        "align": false
      }
    },
    {
      "aliasColors": {
        "In - wlan1": "#ff2e63"
      },
      "bars": false,
      "dashLength": 10,
      "dashes": false,
      "datasource": {
        "type": "prometheus",
        "uid": "${DS_PROMETHEUS}"
      },
      "description": "Showing values > 0",
      "fill": 1,
      "fillGradient": 0,
      "gridPos": {
        "h": 6,
        "w": 12,
        "x": 12,
        "y": 39
      },
      "hiddenSeries": false,
      "id": 1671,
      "legend": {
        "alignAsTable": true,
        "avg": true,
        "current": true,
        "hideEmpty": false,
        "hideZero": true,
        "max": true,
        "min": false,
        "rightSide": true,
        "show": true,
        "total": false,
        "values": true
      },
      "lines": true,
      "linewidth": 1,
      "nullPointMode": "connected",
      "options": {
        "alertThreshold": true
      },
      "percentage": false,
      "pluginVersion": "9.0.5",
      "pointradius": 2,
      "points": false,
      "renderer": "flot",
      "seriesOverrides": [],
      "spaceLength": 10,
      "stack": false,
      "steppedLine": false,
      "targets": [
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${DS_PROMETHEUS}"
          },
          "exemplar": true,
          "expr": "irate(mtxrInterfaceStatsRxAlignError{ifName=~'$Interface',instance='$instance'}[$__rate_interval])",
          "hide": false,
          "interval": "",
          "intervalFactor": 1,
          "legendFormat": "Rx Align Error - {{ifName}}",
          "refId": "A"
        },
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${DS_PROMETHEUS}"
          },
          "exemplar": true,
          "expr": "irate(mtxrInterfaceStatsRxCarrierError{ifName=~'$Interface',instance='$instance'}[$__rate_interval])",
          "hide": false,
          "interval": "",
          "intervalFactor": 1,
          "legendFormat": "Rx Carrier Error - {{ifName}}",
          "refId": "B"
        },
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${DS_PROMETHEUS}"
          },
          "exemplar": true,
          "expr": "irate(mtxrInterfaceStatsRxControl{ifName=~'$Interface',instance='$instance'}[$__rate_interval])",
          "hide": false,
          "interval": "",
          "intervalFactor": 1,
          "legendFormat": "Rx Control - {{ifName}}",
          "refId": "C"
        },
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${DS_PROMETHEUS}"
          },
          "exemplar": true,
          "expr": "irate(mtxrInterfaceStatsRxDrop{ifName=~'$Interface',instance='$instance'}[$__rate_interval])",
          "hide": false,
          "interval": "",
          "intervalFactor": 1,
          "legendFormat": "Rx Drop - {{ifName}}",
          "refId": "D"
        },
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${DS_PROMETHEUS}"
          },
          "exemplar": true,
          "expr": "irate(mtxrInterfaceStatsRxFCSError{ifName=~'$Interface',instance='$instance'}[$__rate_interval])",
          "hide": false,
          "interval": "",
          "intervalFactor": 1,
          "legendFormat": "FCS Error - {{ifName}}",
          "refId": "E"
        },
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${DS_PROMETHEUS}"
          },
          "exemplar": true,
          "expr": "irate(mtxrInterfaceStatsRxFragment{ifName=~'$Interface',instance='$instance'}[$__rate_interval])",
          "hide": false,
          "interval": "",
          "intervalFactor": 1,
          "legendFormat": "Rx Fragment - {{ifName}}",
          "refId": "F"
        },
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${DS_PROMETHEUS}"
          },
          "exemplar": true,
          "expr": "irate(mtxrInterfaceStatsRxJabber{ifName=~'$Interface',instance='$instance'}[$__rate_interval])",
          "hide": false,
          "interval": "",
          "intervalFactor": 1,
          "legendFormat": "Rx Jabber - {{ifName}}",
          "refId": "G"
        },
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${DS_PROMETHEUS}"
          },
          "exemplar": true,
          "expr": "irate(mtxrInterfaceStatsRxLengthError{ifName=~'$Interface',instance='$instance'}[$__rate_interval])",
          "hide": false,
          "interval": "",
          "intervalFactor": 1,
          "legendFormat": "Rx Length Error - {{ifName}}",
          "refId": "H"
        },
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${DS_PROMETHEUS}"
          },
          "exemplar": true,
          "expr": "irate(mtxrInterfaceStatsRxOverflow{ifName=~'$Interface',instance='$instance'}[$__rate_interval])",
          "hide": false,
          "interval": "",
          "intervalFactor": 1,
          "legendFormat": "Rx Overflow - {{ifName}}",
          "refId": "I"
        },
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${DS_PROMETHEUS}"
          },
          "exemplar": true,
          "expr": "irate(mtxrInterfaceStatsRxPause{ifName=~'$Interface',instance='$instance'}[$__rate_interval])",
          "hide": false,
          "interval": "",
          "intervalFactor": 1,
          "legendFormat": "Rx Pause - {{ifName}}",
          "refId": "J"
        },
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${DS_PROMETHEUS}"
          },
          "exemplar": true,
          "expr": "irate(mtxrInterfaceStatsRxTooLong{ifName=~'$Interface',instance='$instance'}[$__rate_interval])",
          "hide": false,
          "interval": "",
          "intervalFactor": 1,
          "legendFormat": "Rx Too Long - {{ifName}}",
          "refId": "K"
        },
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${DS_PROMETHEUS}"
          },
          "exemplar": true,
          "expr": "irate(mtxrInterfaceStatsRxTooShort{ifName=~'$Interface',instance='$instance'}[$__rate_interval])",
          "hide": false,
          "interval": "",
          "intervalFactor": 1,
          "legendFormat": "Rx Too Short - {{ifName}}",
          "refId": "L"
        },
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${DS_PROMETHEUS}"
          },
          "exemplar": true,
          "expr": "irate(mtxrInterfaceStatsRxUnknownOp{ifName=~'$Interface',instance='$instance'}[$__rate_interval])",
          "hide": false,
          "interval": "",
          "intervalFactor": 1,
          "legendFormat": "Rx Unknown Op - {{ifName}}",
          "refId": "M"
        }
      ],
      "thresholds": [],
      "timeRegions": [],
      "title": "Rx Eth errors, etc",
      "tooltip": {
        "shared": true,
        "sort": 0,
        "value_type": "individual"
      },
      "type": "graph",
      "xaxis": {
        "mode": "time",
        "show": true,
        "values": []
      },
      "yaxes": [
        {
          "format": "bps",
          "label": "",
          "logBase": 1,
          "show": true
        },
        {
          "format": "short",
          "logBase": 1,
          "show": false
        }
      ],
      "yaxis": {
        "align": false
      }
    },
    {
      "datasource": {
        "type": "prometheus",
        "uid": "${DS_PROMETHEUS}"
      },
      "description": "",
      "fieldConfig": {
        "defaults": {
          "color": {
            "mode": "thresholds"
          },
          "custom": {
            "align": "auto",
            "displayMode": "color-text",
            "filterable": false,
            "inspect": false
          },
          "mappings": [],
          "thresholds": {
            "mode": "absolute",
            "steps": [
              {
                "color": "super-light-yellow",
                "value": null
              }
            ]
          },
          "unit": "short"
        },
        "overrides": [
          {
            "matcher": {
              "id": "byName",
              "options": "Neighbor index"
            },
            "properties": [
              {
                "id": "custom.align",
                "value": "center"
              },
              {
                "id": "custom.width",
                "value": 134
              }
            ]
          },
          {
            "matcher": {
              "id": "byName",
              "options": "IP"
            },
            "properties": [
              {
                "id": "custom.width",
                "value": 111
              }
            ]
          },
          {
            "matcher": {
              "id": "byName",
              "options": "MAC"
            },
            "properties": [
              {
                "id": "custom.width",
                "value": 142
              }
            ]
          },
          {
            "matcher": {
              "id": "byName",
              "options": "Platform"
            },
            "properties": [
              {
                "id": "custom.width",
                "value": 127
              }
            ]
          },
          {
            "matcher": {
              "id": "byName",
              "options": "Software ID"
            },
            "properties": [
              {
                "id": "custom.width",
                "value": 136
              }
            ]
          }
        ]
      },
      "gridPos": {
        "h": 6,
        "w": 24,
        "x": 0,
        "y": 45
      },
      "id": 1652,
      "options": {
        "footer": {
          "fields": "",
          "reducer": [
            "sum"
          ],
          "show": false
        },
        "frameIndex": 0,
        "showHeader": true,
        "sortBy": [
          {
            "desc": true,
            "displayName": "Neighbor index"
          }
        ]
      },
      "pluginVersion": "9.0.5",
      "targets": [
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${DS_PROMETHEUS}"
          },
          "exemplar": true,
          "expr": "mtxrNeighborInterfaceID{instance='$instance'}",
          "format": "table",
          "instant": true,
          "interval": "",
          "legendFormat": "",
          "refId": "A"
        },
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${DS_PROMETHEUS}"
          },
          "exemplar": true,
          "expr": "mtxrNeighborIdentity{instance='$instance'}",
          "format": "table",
          "hide": false,
          "instant": true,
          "interval": "",
          "legendFormat": "",
          "refId": "B"
        },
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${DS_PROMETHEUS}"
          },
          "exemplar": true,
          "expr": "mtxrNeighborIpAddress{instance='$instance'}",
          "format": "table",
          "hide": false,
          "instant": true,
          "interval": "",
          "legendFormat": "",
          "refId": "C"
        },
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${DS_PROMETHEUS}"
          },
          "exemplar": true,
          "expr": "mtxrNeighborMacAddress{instance='$instance'}",
          "format": "table",
          "hide": false,
          "instant": true,
          "interval": "",
          "legendFormat": "",
          "refId": "D"
        },
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${DS_PROMETHEUS}"
          },
          "exemplar": true,
          "expr": "mtxrNeighborPlatform{instance='$instance'}",
          "format": "table",
          "hide": false,
          "instant": true,
          "interval": "",
          "legendFormat": "",
          "refId": "E"
        },
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${DS_PROMETHEUS}"
          },
          "exemplar": true,
          "expr": "mtxrNeighborSoftwareID{instance='$instance'}",
          "format": "table",
          "hide": false,
          "instant": true,
          "interval": "",
          "legendFormat": "",
          "refId": "F"
        },
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${DS_PROMETHEUS}"
          },
          "exemplar": true,
          "expr": "mtxrNeighborVersion{instance='$instance'}",
          "format": "table",
          "hide": false,
          "instant": true,
          "interval": "",
          "legendFormat": "",
          "refId": "G"
        }
      ],
      "title": "Neighbors",
      "transformations": [
        {
          "id": "seriesToColumns",
          "options": {
            "byField": "mtxrNeighborIndex"
          }
        },
        {
          "id": "merge",
          "options": {}
        },
        {
          "id": "organize",
          "options": {
            "excludeByName": {
              "Time": true,
              "Value #A": true,
              "Value #B": true,
              "Value #C": true,
              "Value #D": true,
              "Value #E": true,
              "Value #F": true,
              "Value #G": true,
              "__name__": true,
              "instance": true,
              "job": true,
              "mtxrNeighborIndex": false
            },
            "indexByName": {},
            "renameByName": {
              "Time": "",
              "Value #A": "",
              "Value #B": "",
              "Value #C": "",
              "Value #D": "",
              "Value #E": "",
              "Value #F": "",
              "job": "",
              "mtxrNeighborIdentity": "identity",
              "mtxrNeighborIndex": "Neighbor index",
              "mtxrNeighborIpAddress": "IP",
              "mtxrNeighborMacAddress": "MAC",
              "mtxrNeighborPlatform": "Platform",
              "mtxrNeighborSoftwareID": "Software ID",
              "mtxrNeighborVersion": "Firmware version"
            }
          }
        }
      ],
      "type": "table"
    },
    {
      "collapsed": true,
      "datasource": {
        "type": "prometheus",
        "uid": "PBFA97CFB590B2093"
      },
      "gridPos": {
        "h": 1,
        "w": 24,
        "x": 0,
        "y": 51
      },
      "id": 1642,
      "panels": [
        {
          "aliasColors": {
            "CCQ - 1": "#ff2e63",
            "CCQ - 2": "#08d9d6",
            "CCQ - Tilda": "#ff2e63",
            "Noise - 1": "#ff2e63",
            "Noise - 2": "#08d9d6",
            "Noise - Tilda": "light-blue",
            "Noise - Tilda_5": "dark-purple",
            "TX CCQ - Tilda": "#ff2e63"
          },
          "bars": false,
          "dashLength": 10,
          "dashes": false,
          "datasource": {
            "type": "prometheus",
            "uid": "${DS_PROMETHEUS}"
          },
          "description": "",
          "fill": 1,
          "fillGradient": 0,
          "gridPos": {
            "h": 9,
            "w": 8,
            "x": 0,
            "y": 3
          },
          "hiddenSeries": false,
          "id": 1270,
          "legend": {
            "alignAsTable": true,
            "avg": true,
            "current": true,
            "hideZero": true,
            "max": false,
            "min": false,
            "rightSide": false,
            "show": true,
            "total": false,
            "values": true
          },
          "lines": true,
          "linewidth": 1,
          "links": [],
          "maxPerRow": 2,
          "nullPointMode": "connected",
          "options": {
            "alertThreshold": true
          },
          "percentage": false,
          "pluginVersion": "8.3.4",
          "pointradius": 2,
          "points": false,
          "renderer": "flot",
          "repeatDirection": "h",
          "seriesOverrides": [
            {
              "alias": "2",
              "yaxis": 1
            },
            {
              "alias": "mtxrWlApNoiseFloor{instance=\"192.168.5.1\", job=\"Mikrotik\", mtxrWlApIndex=\"2\"}",
              "yaxis": 2
            },
            {
              "alias": "mtxrWlApNoiseFloor{instance=\"192.168.5.1\", job=\"Mikrotik\", mtxrWlApIndex=\"11\"}",
              "yaxis": 2
            },
            {
              "alias": "mtxrWlApNoiseFloor{instance=\"192.168.5.1\", job=\"Mikrotik\", mtxrWlApIndex=\"1\"}",
              "yaxis": 2
            },
            {
              "alias": "Noise 1",
              "yaxis": 2
            },
            {
              "alias": "Noise 11",
              "yaxis": 2
            },
            {
              "alias": "Noise 2",
              "yaxis": 2
            },
            {
              "alias": "Noise - 2",
              "yaxis": 2
            },
            {
              "alias": "Noise - 11",
              "yaxis": 2
            },
            {
              "alias": "Noise - 1",
              "yaxis": 2
            },
            {
              "alias": "Noise - Tilda",
              "yaxis": 2
            },
            {
              "alias": "Noise - Tilda_5",
              "yaxis": 2
            }
          ],
          "spaceLength": 10,
          "stack": false,
          "steppedLine": false,
          "targets": [
            {
              "datasource": {
                "type": "prometheus",
                "uid": "${DS_PROMETHEUS}"
              },
              "exemplar": true,
              "expr": "(mtxrWlApOverallTxCCQ{instance='$instance'}*on(mtxrWlApIndex)group_left(mtxrWlApSsid)mtxrWlApSsid{instance='$instance'})",
              "hide": false,
              "interval": "",
              "legendFormat": "TX CCQ - {{mtxrWlApSsid}}",
              "refId": "A"
            },
            {
              "datasource": {
                "type": "prometheus",
                "uid": "${DS_PROMETHEUS}"
              },
              "exemplar": true,
              "expr": "(mtxrWlApNoiseFloor{instance='$instance'}*on(mtxrWlApIndex)group_left(mtxrWlApSsid)mtxrWlApSsid{instance='$instance'})",
              "format": "time_series",
              "hide": false,
              "instant": false,
              "interval": "",
              "intervalFactor": 1,
              "legendFormat": "Noise - {{mtxrWlApSsid}}",
              "refId": "B"
            }
          ],
          "thresholds": [],
          "timeRegions": [],
          "title": "Wi-Fi Overall Tx CCQ & Noise",
          "tooltip": {
            "shared": true,
            "sort": 0,
            "value_type": "individual"
          },
          "type": "graph",
          "xaxis": {
            "mode": "time",
            "show": true,
            "values": []
          },
          "yaxes": [
            {
              "format": "percent",
              "label": "",
              "logBase": 1,
              "show": true
            },
            {
              "format": "dBm",
              "label": "",
              "logBase": 1,
              "show": true
            }
          ],
          "yaxis": {
            "align": true,
            "alignLevel": 0
          }
        },
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${DS_PROMETHEUS}"
          },
          "description": "",
          "fieldConfig": {
            "defaults": {
              "color": {
                "mode": "palette-classic"
              },
              "custom": {
                "axisLabel": "",
                "axisPlacement": "auto",
                "barAlignment": 0,
                "drawStyle": "line",
                "fillOpacity": 10,
                "gradientMode": "none",
                "hideFrom": {
                  "legend": false,
                  "tooltip": false,
                  "viz": false
                },
                "lineInterpolation": "smooth",
                "lineWidth": 2,
                "pointSize": 5,
                "scaleDistribution": {
                  "type": "linear"
                },
                "showPoints": "never",
                "spanNulls": false,
                "stacking": {
                  "group": "A",
                  "mode": "none"
                },
                "thresholdsStyle": {
                  "mode": "off"
                }
              },
              "decimals": 0,
              "mappings": [],
              "thresholds": {
                "mode": "absolute",
                "steps": [
                  {
                    "color": "green"
                  },
                  {
                    "color": "red",
                    "value": 80
                  }
                ]
              },
              "unit": "short"
            },
            "overrides": [
              {
                "matcher": {
                  "id": "byName",
                  "options": "1"
                },
                "properties": [
                  {
                    "id": "color",
                    "value": {
                      "fixedColor": "#ff2e63",
                      "mode": "fixed"
                    }
                  }
                ]
              },
              {
                "matcher": {
                  "id": "byName",
                  "options": "2"
                },
                "properties": [
                  {
                    "id": "color",
                    "value": {
                      "fixedColor": "#08d9d6",
                      "mode": "fixed"
                    }
                  }
                ]
              },
              {
                "matcher": {
                  "id": "byName",
                  "options": "DHCP Leases count"
                },
                "properties": [
                  {
                    "id": "color",
                    "value": {
                      "fixedColor": "dark-green",
                      "mode": "fixed"
                    }
                  }
                ]
              },
              {
                "matcher": {
                  "id": "byName",
                  "options": "Tilda"
                },
                "properties": [
                  {
                    "id": "color",
                    "value": {
                      "fixedColor": "#ff2e63",
                      "mode": "fixed"
                    }
                  }
                ]
              }
            ]
          },
          "gridPos": {
            "h": 9,
            "w": 8,
            "x": 8,
            "y": 3
          },
          "id": 1261,
          "options": {
            "legend": {
              "calcs": [
                "mean",
                "lastNotNull",
                "max",
                "min"
              ],
              "displayMode": "table",
              "placement": "bottom"
            },
            "tooltip": {
              "mode": "single"
            }
          },
          "pluginVersion": "8.2.1",
          "targets": [
            {
              "datasource": {
                "type": "prometheus",
                "uid": "${DS_PROMETHEUS}"
              },
              "exemplar": true,
              "expr": "(mtxrWlApAuthClientCount{instance='$instance'}*on(mtxrWlApIndex)group_left(mtxrWlApSsid)mtxrWlApSsid{instance='$instance'})",
              "hide": false,
              "interval": "",
              "legendFormat": "{{mtxrWlApSsid}}",
              "refId": "A"
            },
            {
              "datasource": {
                "type": "prometheus",
                "uid": "${DS_PROMETHEUS}"
              },
              "exemplar": true,
              "expr": "mtxrDHCPLeaseCount{instance='$instance'}",
              "hide": false,
              "interval": "",
              "legendFormat": "DHCP Leases",
              "refId": "B"
            }
          ],
          "title": "Wi-Fi Client count",
          "type": "timeseries"
        },
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${DS_PROMETHEUS}"
          },
          "description": "",
          "fieldConfig": {
            "defaults": {
              "color": {
                "mode": "palette-classic"
              },
              "custom": {
                "axisLabel": "",
                "axisPlacement": "auto",
                "barAlignment": 0,
                "drawStyle": "line",
                "fillOpacity": 10,
                "gradientMode": "none",
                "hideFrom": {
                  "legend": false,
                  "tooltip": false,
                  "viz": false
                },
                "lineInterpolation": "smooth",
                "lineWidth": 2,
                "pointSize": 5,
                "scaleDistribution": {
                  "type": "linear"
                },
                "showPoints": "never",
                "spanNulls": false,
                "stacking": {
                  "group": "A",
                  "mode": "none"
                },
                "thresholdsStyle": {
                  "mode": "off"
                }
              },
              "decimals": 0,
              "mappings": [],
              "thresholds": {
                "mode": "absolute",
                "steps": [
                  {
                    "color": "green"
                  },
                  {
                    "color": "red",
                    "value": 80
                  }
                ]
              },
              "unit": "MHz"
            },
            "overrides": [
              {
                "matcher": {
                  "id": "byName",
                  "options": "1"
                },
                "properties": [
                  {
                    "id": "color",
                    "value": {
                      "fixedColor": "#ff2e63",
                      "mode": "fixed"
                    }
                  }
                ]
              },
              {
                "matcher": {
                  "id": "byName",
                  "options": "2"
                },
                "properties": [
                  {
                    "id": "color",
                    "value": {
                      "fixedColor": "#08d9d6",
                      "mode": "fixed"
                    }
                  }
                ]
              },
              {
                "matcher": {
                  "id": "byName",
                  "options": "DHCP Leases count"
                },
                "properties": [
                  {
                    "id": "color",
                    "value": {
                      "fixedColor": "dark-green",
                      "mode": "fixed"
                    }
                  }
                ]
              },
              {
                "matcher": {
                  "id": "byName",
                  "options": "Tilda"
                },
                "properties": [
                  {
                    "id": "color",
                    "value": {
                      "fixedColor": "#ff2e63",
                      "mode": "fixed"
                    }
                  }
                ]
              }
            ]
          },
          "gridPos": {
            "h": 9,
            "w": 8,
            "x": 16,
            "y": 3
          },
          "id": 1613,
          "options": {
            "legend": {
              "calcs": [
                "lastNotNull"
              ],
              "displayMode": "list",
              "placement": "bottom"
            },
            "tooltip": {
              "mode": "single"
            }
          },
          "pluginVersion": "8.2.1",
          "targets": [
            {
              "datasource": {
                "type": "prometheus",
                "uid": "${DS_PROMETHEUS}"
              },
              "exemplar": true,
              "expr": "mtxrWlApFreq{instance='$instance'}*on(mtxrWlApIndex)group_left(mtxrWlApSsid)mtxrWlApSsid{instance='$instance'}",
              "hide": false,
              "instant": false,
              "interval": "",
              "legendFormat": "{{mtxrWlApSsid}}",
              "refId": "A"
            }
          ],
          "title": "Wi-Fi frequency",
          "type": "timeseries"
        },
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${DS_PROMETHEUS}"
          },
          "description": "Wireless registration table. It is indexed by remote mac-address and local interface index.\n\nMeasured in dB, if value does not exist it is indicated with 0",
          "fieldConfig": {
            "defaults": {
              "color": {
                "mode": "thresholds"
              },
              "custom": {
                "displayMode": "auto",
                "filterable": false
              },
              "mappings": [],
              "thresholds": {
                "mode": "absolute",
                "steps": [
                  {
                    "color": "green"
                  }
                ]
              }
            },
            "overrides": [
              {
                "matcher": {
                  "id": "byName",
                  "options": "mac address"
                },
                "properties": [
                  {
                    "id": "custom.width"
                  }
                ]
              },
              {
                "matcher": {
                  "id": "byName",
                  "options": "Interface"
                },
                "properties": [
                  {
                    "id": "custom.width",
                    "value": 90
                  }
                ]
              },
              {
                "matcher": {
                  "id": "byName",
                  "options": "Signal-to-Noise"
                },
                "properties": [
                  {
                    "id": "custom.width",
                    "value": 200
                  },
                  {
                    "id": "unit",
                    "value": "dB"
                  },
                  {
                    "id": "custom.displayMode",
                    "value": "lcd-gauge"
                  },
                  {
                    "id": "min",
                    "value": 5
                  },
                  {
                    "id": "max",
                    "value": 50
                  },
                  {
                    "id": "color",
                    "value": {
                      "mode": "continuous-RdYlGr"
                    }
                  }
                ]
              },
              {
                "matcher": {
                  "id": "byName",
                  "options": "Strength"
                },
                "properties": [
                  {
                    "id": "custom.width",
                    "value": 200
                  },
                  {
                    "id": "unit",
                    "value": "dBm"
                  },
                  {
                    "id": "custom.displayMode",
                    "value": "lcd-gauge"
                  },
                  {
                    "id": "min",
                    "value": -85
                  },
                  {
                    "id": "max",
                    "value": -30
                  },
                  {
                    "id": "color",
                    "value": {
                      "mode": "continuous-RdYlGr"
                    }
                  }
                ]
              },
              {
                "matcher": {
                  "id": "byType",
                  "options": "number"
                },
                "properties": [
                  {
                    "id": "custom.align",
                    "value": "center"
                  }
                ]
              },
              {
                "matcher": {
                  "id": "byType",
                  "options": "string"
                },
                "properties": [
                  {
                    "id": "custom.align",
                    "value": "center"
                  }
                ]
              },
              {
                "matcher": {
                  "id": "byName",
                  "options": "Tx"
                },
                "properties": [
                  {
                    "id": "custom.width",
                    "value": 90
                  },
                  {
                    "id": "unit",
                    "value": "bytes"
                  }
                ]
              },
              {
                "matcher": {
                  "id": "byName",
                  "options": "Rx"
                },
                "properties": [
                  {
                    "id": "custom.width",
                    "value": 90
                  },
                  {
                    "id": "unit",
                    "value": "bytes"
                  }
                ]
              },
              {
                "matcher": {
                  "id": "byName",
                  "options": "Tx rate"
                },
                "properties": [
                  {
                    "id": "custom.width",
                    "value": 90
                  },
                  {
                    "id": "unit",
                    "value": "bps"
                  }
                ]
              },
              {
                "matcher": {
                  "id": "byName",
                  "options": "Rx rate"
                },
                "properties": [
                  {
                    "id": "custom.width"
                  },
                  {
                    "id": "unit",
                    "value": "bps"
                  }
                ]
              },
              {
                "matcher": {
                  "id": "byName",
                  "options": "Uptime"
                },
                "properties": [
                  {
                    "id": "custom.width",
                    "value": 90
                  },
                  {
                    "id": "decimals",
                    "value": 1
                  },
                  {
                    "id": "unit",
                    "value": "timeticks"
                  }
                ]
              },
              {
                "matcher": {
                  "id": "byName",
                  "options": "Value #I"
                },
                "properties": [
                  {
                    "id": "custom.width",
                    "value": 263
                  }
                ]
              }
            ]
          },
          "gridPos": {
            "h": 8,
            "w": 24,
            "x": 0,
            "y": 12
          },
          "id": 1643,
          "links": [],
          "options": {
            "footer": {
              "fields": "",
              "reducer": [
                "sum"
              ],
              "show": false
            },
            "showHeader": true,
            "sortBy": []
          },
          "pluginVersion": "8.3.4",
          "targets": [
            {
              "datasource": {
                "type": "prometheus",
                "uid": "${DS_PROMETHEUS}"
              },
              "exemplar": true,
              "expr": "mtxrWlRtabAddr{instance='$instance'}",
              "format": "table",
              "hide": false,
              "instant": true,
              "interval": "",
              "legendFormat": "",
              "refId": "A"
            },
            {
              "datasource": {
                "type": "prometheus",
                "uid": "${DS_PROMETHEUS}"
              },
              "exemplar": true,
              "expr": "mtxrWlRtabSignalToNoise{instance='$instance'}",
              "format": "table",
              "hide": false,
              "instant": true,
              "interval": "",
              "legendFormat": "",
              "refId": "B"
            },
            {
              "datasource": {
                "type": "prometheus",
                "uid": "${DS_PROMETHEUS}"
              },
              "exemplar": true,
              "expr": "mtxrWlRtabStrength{instance='$instance'}",
              "format": "table",
              "hide": false,
              "instant": true,
              "interval": "",
              "legendFormat": "",
              "refId": "C"
            },
            {
              "datasource": {
                "type": "prometheus",
                "uid": "${DS_PROMETHEUS}"
              },
              "exemplar": true,
              "expr": "mtxrWlRtabTxBytes{instance='$instance'}",
              "format": "table",
              "hide": false,
              "instant": true,
              "interval": "",
              "legendFormat": "",
              "refId": "D"
            },
            {
              "datasource": {
                "type": "prometheus",
                "uid": "${DS_PROMETHEUS}"
              },
              "exemplar": true,
              "expr": "mtxrWlRtabRxBytes{instance='$instance'}",
              "format": "table",
              "hide": false,
              "instant": true,
              "interval": "",
              "legendFormat": "",
              "refId": "E"
            },
            {
              "datasource": {
                "type": "prometheus",
                "uid": "${DS_PROMETHEUS}"
              },
              "exemplar": true,
              "expr": "mtxrWlRtabTxRate{instance='$instance'}",
              "format": "table",
              "hide": false,
              "instant": true,
              "interval": "",
              "legendFormat": "",
              "refId": "F"
            },
            {
              "datasource": {
                "type": "prometheus",
                "uid": "${DS_PROMETHEUS}"
              },
              "exemplar": true,
              "expr": "mtxrWlRtabRxRate{instance='$instance'}",
              "format": "table",
              "hide": false,
              "instant": true,
              "interval": "",
              "legendFormat": "",
              "refId": "G"
            },
            {
              "datasource": {
                "type": "prometheus",
                "uid": "${DS_PROMETHEUS}"
              },
              "exemplar": true,
              "expr": "mtxrWlRtabUptime{instance='$instance'}",
              "format": "table",
              "hide": false,
              "instant": true,
              "interval": "",
              "legendFormat": "",
              "refId": "H"
            }
          ],
          "title": "Wi-Fi Clients",
          "transformations": [
            {
              "id": "seriesToColumns",
              "options": {
                "byField": "mtxrWlRtabAddr"
              }
            },
            {
              "id": "organize",
              "options": {
                "excludeByName": {
                  "Time": true,
                  "Time 1": true,
                  "Time 2": true,
                  "Time 3": true,
                  "Time 4": true,
                  "Time 5": true,
                  "Time 6": true,
                  "Time 7": true,
                  "Time 8": true,
                  "Value #A": true,
                  "__name__": true,
                  "__name__ 1": true,
                  "__name__ 2": true,
                  "__name__ 3": true,
                  "__name__ 4": true,
                  "__name__ 5": true,
                  "__name__ 6": true,
                  "__name__ 7": true,
                  "__name__ 8": true,
                  "instance": true,
                  "instance 1": true,
                  "instance 2": true,
                  "instance 3": true,
                  "instance 4": true,
                  "instance 5": true,
                  "instance 6": true,
                  "instance 7": true,
                  "instance 8": true,
                  "job": true,
                  "job 1": true,
                  "job 2": true,
                  "job 3": true,
                  "job 4": true,
                  "job 5": true,
                  "job 6": true,
                  "job 7": true,
                  "job 8": true,
                  "mtxrWlRtabIface 1": false,
                  "mtxrWlRtabIface 2": true,
                  "mtxrWlRtabIface 3": true,
                  "mtxrWlRtabIface 4": true,
                  "mtxrWlRtabIface 5": true,
                  "mtxrWlRtabIface 6": true,
                  "mtxrWlRtabIface 7": true,
                  "mtxrWlRtabIface 8": true
                },
                "indexByName": {
                  "Time": 5,
                  "Value #A": 9,
                  "Value #B": 4,
                  "Value #C": 3,
                  "Value #D": 12,
                  "Value #E": 13,
                  "Value #F": 10,
                  "Value #G": 11,
                  "Value #H": 0,
                  "__name__": 6,
                  "instance": 7,
                  "job": 8,
                  "mtxrWlRtabAddr": 1,
                  "mtxrWlRtabIface": 2
                },
                "renameByName": {
                  "Time": "",
                  "Value #A": "",
                  "Value #B": "Signal-to-Noise",
                  "Value #C": "Strength",
                  "Value #D": "Tx",
                  "Value #E": "Rx",
                  "Value #F": "Tx rate",
                  "Value #G": "Rx rate",
                  "Value #H": "Uptime",
                  "job": "",
                  "mtxrWlRtabAddr": "Mac address",
                  "mtxrWlRtabIface": "Interface",
                  "mtxrWlRtabIface 1": "wifi interface id"
                }
              }
            }
          ],
          "type": "table"
        },
        {
          "cards": {},
          "color": {
            "cardColor": "#C4162A",
            "colorScale": "sqrt",
            "colorScheme": "interpolateRdYlGn",
            "exponent": 0.5,
            "max": -85,
            "min": -30,
            "mode": "spectrum"
          },
          "dataFormat": "tsbuckets",
          "datasource": {
            "type": "prometheus",
            "uid": "${DS_PROMETHEUS}"
          },
          "description": "Signal Strength: signal strength in dBm (if first ppp-client modem supports)",
          "gridPos": {
            "h": 8,
            "w": 12,
            "x": 0,
            "y": 20
          },
          "heatmap": {},
          "hideZeroBuckets": false,
          "highlightCards": true,
          "id": 1647,
          "legend": {
            "show": false
          },
          "links": [],
          "pluginVersion": "7.5.5",
          "repeatDirection": "h",
          "reverseYBuckets": false,
          "targets": [
            {
              "datasource": {
                "type": "prometheus",
                "uid": "${DS_PROMETHEUS}"
              },
              "exemplar": true,
              "expr": "mtxrWlRtabStrength{instance='$instance'}",
              "hide": false,
              "interval": "",
              "legendFormat": "{{mtxrWlRtabAddr}}",
              "refId": "A"
            }
          ],
          "title": "History Wi-Fi Strength",
          "tooltip": {
            "show": true,
            "showHistogram": true
          },
          "type": "heatmap",
          "xAxis": {
            "show": true
          },
          "xBucketSize": "2m",
          "yAxis": {
            "format": "dBm",
            "logBase": 1,
            "show": true
          },
          "yBucketBound": "auto",
          "yBucketSize": 2
        },
        {
          "cards": {},
          "color": {
            "cardColor": "#C4162A",
            "colorScale": "sqrt",
            "colorScheme": "interpolateRdYlGn",
            "exponent": 0.5,
            "max": 5,
            "min": 50,
            "mode": "spectrum"
          },
          "dataFormat": "tsbuckets",
          "datasource": {
            "type": "prometheus",
            "uid": "${DS_PROMETHEUS}"
          },
          "description": "Measured in dB, if value does not exist it is indicated with 0",
          "gridPos": {
            "h": 8,
            "w": 12,
            "x": 12,
            "y": 20
          },
          "heatmap": {},
          "hideZeroBuckets": false,
          "highlightCards": true,
          "id": 1648,
          "legend": {
            "show": false
          },
          "links": [],
          "pluginVersion": "7.5.5",
          "repeatDirection": "h",
          "reverseYBuckets": false,
          "targets": [
            {
              "datasource": {
                "type": "prometheus",
                "uid": "${DS_PROMETHEUS}"
              },
              "exemplar": true,
              "expr": "mtxrWlRtabSignalToNoise{instance='$instance'}",
              "hide": false,
              "interval": "",
              "legendFormat": "{{mtxrWlRtabAddr}}",
              "refId": "A"
            }
          ],
          "title": "History Wi-Fi Signal-to-Noise",
          "tooltip": {
            "show": true,
            "showHistogram": true
          },
          "type": "heatmap",
          "xAxis": {
            "show": true
          },
          "xBucketSize": "2m",
          "yAxis": {
            "format": "dB",
            "logBase": 1,
            "show": true
          },
          "yBucketBound": "auto",
          "yBucketSize": 2
        }
      ],
      "targets": [
        {
          "datasource": {
            "type": "prometheus",
            "uid": "PBFA97CFB590B2093"
          },
          "refId": "A"
        }
      ],
      "title": "Wireless",
      "type": "row"
    },
    {
      "collapsed": true,
      "datasource": {
        "type": "prometheus",
        "uid": "PBFA97CFB590B2093"
      },
      "gridPos": {
        "h": 1,
        "w": 24,
        "x": 0,
        "y": 52
      },
      "id": 1676,
      "panels": [
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${DS_PROMETHEUS}"
          },
          "description": "Wireless registration table entry count",
          "fieldConfig": {
            "defaults": {
              "color": {
                "mode": "thresholds"
              },
              "mappings": [],
              "thresholds": {
                "mode": "absolute",
                "steps": [
                  {
                    "color": "#299c46"
                  }
                ]
              }
            },
            "overrides": []
          },
          "gridPos": {
            "h": 4,
            "w": 3,
            "x": 0,
            "y": 4
          },
          "id": 1646,
          "options": {
            "colorMode": "value",
            "graphMode": "none",
            "justifyMode": "auto",
            "orientation": "auto",
            "reduceOptions": {
              "calcs": [
                "lastNotNull"
              ],
              "fields": "",
              "values": false
            },
            "text": {},
            "textMode": "auto"
          },
          "pluginVersion": "8.3.4",
          "targets": [
            {
              "datasource": {
                "type": "prometheus",
                "uid": "${DS_PROMETHEUS}"
              },
              "exemplar": true,
              "expr": "mtxrWlCMRtabEntryCount{instance='$instance'}",
              "format": "time_series",
              "hide": false,
              "instant": true,
              "interval": "",
              "legendFormat": "",
              "refId": "A"
            }
          ],
          "title": "CAPsMAN client count",
          "type": "stat"
        },
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${DS_PROMETHEUS}"
          },
          "description": "",
          "fieldConfig": {
            "defaults": {
              "color": {
                "mode": "thresholds"
              },
              "custom": {
                "align": "auto",
                "displayMode": "auto"
              },
              "mappings": [],
              "thresholds": {
                "mode": "absolute",
                "steps": [
                  {
                    "color": "green"
                  },
                  {
                    "color": "red",
                    "value": 80
                  }
                ]
              }
            },
            "overrides": [
              {
                "matcher": {
                  "id": "byName",
                  "options": "Remote address"
                },
                "properties": [
                  {
                    "id": "custom.width",
                    "value": 187
                  },
                  {
                    "id": "custom.align",
                    "value": "center"
                  }
                ]
              },
              {
                "matcher": {
                  "id": "byName",
                  "options": "remote index"
                },
                "properties": [
                  {
                    "id": "custom.width",
                    "value": 110
                  },
                  {
                    "id": "custom.align",
                    "value": "center"
                  }
                ]
              },
              {
                "matcher": {
                  "id": "byName",
                  "options": "Remote name"
                },
                "properties": [
                  {
                    "id": "custom.width"
                  },
                  {
                    "id": "custom.align",
                    "value": "center"
                  }
                ]
              },
              {
                "matcher": {
                  "id": "byName",
                  "options": "Remote address/port"
                },
                "properties": [
                  {
                    "id": "custom.width",
                    "value": 199
                  },
                  {
                    "id": "custom.align",
                    "value": "center"
                  }
                ]
              },
              {
                "matcher": {
                  "id": "byName",
                  "options": "state"
                },
                "properties": [
                  {
                    "id": "custom.width",
                    "value": 74
                  },
                  {
                    "id": "custom.align",
                    "value": "center"
                  }
                ]
              },
              {
                "matcher": {
                  "id": "byName",
                  "options": "Remote Radios"
                },
                "properties": [
                  {
                    "id": "custom.width",
                    "value": 122
                  },
                  {
                    "id": "custom.align",
                    "value": "center"
                  }
                ]
              }
            ]
          },
          "gridPos": {
            "h": 8,
            "w": 11,
            "x": 3,
            "y": 4
          },
          "id": 1681,
          "options": {
            "footer": {
              "fields": "",
              "reducer": [
                "sum"
              ],
              "show": false
            },
            "showHeader": true,
            "sortBy": [
              {
                "desc": true,
                "displayName": "state"
              }
            ]
          },
          "pluginVersion": "8.3.4",
          "targets": [
            {
              "datasource": {
                "type": "prometheus",
                "uid": "${DS_PROMETHEUS}"
              },
              "exemplar": true,
              "expr": "mtxrWlCMRemoteAddress{instance='$instance'}",
              "format": "table",
              "hide": false,
              "instant": true,
              "interval": "",
              "legendFormat": "",
              "refId": "A"
            },
            {
              "datasource": {
                "type": "prometheus",
                "uid": "${DS_PROMETHEUS}"
              },
              "exemplar": true,
              "expr": "mtxrWlCMRemoteName{instance='$instance'}",
              "format": "table",
              "hide": false,
              "instant": true,
              "interval": "",
              "legendFormat": "",
              "refId": "B"
            },
            {
              "datasource": {
                "type": "prometheus",
                "uid": "${DS_PROMETHEUS}"
              },
              "exemplar": true,
              "expr": "mtxrWlCMRemoteRadios{instance='$instance'}",
              "format": "table",
              "hide": false,
              "instant": true,
              "interval": "",
              "legendFormat": "",
              "refId": "C"
            },
            {
              "datasource": {
                "type": "prometheus",
                "uid": "${DS_PROMETHEUS}"
              },
              "exemplar": true,
              "expr": "mtxrWlCMRemoteState{instance='$instance'}",
              "format": "table",
              "hide": false,
              "instant": true,
              "interval": "",
              "legendFormat": "",
              "refId": "D"
            }
          ],
          "title": "Remote CAP",
          "transformations": [
            {
              "id": "seriesToColumns",
              "options": {
                "byField": "mtxrWlCMRemoteIndex"
              }
            },
            {
              "id": "organize",
              "options": {
                "excludeByName": {
                  "Time 1": true,
                  "Time 2": true,
                  "Time 3": true,
                  "Time 4": true,
                  "Value #A": true,
                  "Value #B": true,
                  "Value #D": true,
                  "__name__ 1": true,
                  "__name__ 2": true,
                  "__name__ 3": true,
                  "__name__ 4": true,
                  "instance 1": true,
                  "instance 2": true,
                  "instance 3": true,
                  "instance 4": true,
                  "job 1": true,
                  "job 2": true,
                  "job 3": true,
                  "job 4": true
                },
                "indexByName": {
                  "Time 1": 5,
                  "Time 2": 10,
                  "Time 3": 15,
                  "Time 4": 19,
                  "Value #A": 9,
                  "Value #B": 14,
                  "Value #C": 4,
                  "Value #D": 23,
                  "__name__ 1": 6,
                  "__name__ 2": 11,
                  "__name__ 3": 16,
                  "__name__ 4": 20,
                  "instance 1": 7,
                  "instance 2": 12,
                  "instance 3": 17,
                  "instance 4": 21,
                  "job 1": 8,
                  "job 2": 13,
                  "job 3": 18,
                  "job 4": 22,
                  "mtxrWlCMRemoteAddress": 3,
                  "mtxrWlCMRemoteIndex": 1,
                  "mtxrWlCMRemoteName": 2,
                  "mtxrWlCMRemoteState": 0
                },
                "renameByName": {
                  "Time 1": "",
                  "Time 4": "",
                  "Value #C": "Remote Radios",
                  "instance 4": "",
                  "mtxrWlCMRemoteAddress": "Remote address/port",
                  "mtxrWlCMRemoteIndex": "remote index",
                  "mtxrWlCMRemoteName": "Remote name",
                  "mtxrWlCMRemoteState": "state"
                }
              }
            }
          ],
          "type": "table"
        },
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${DS_PROMETHEUS}"
          },
          "description": "",
          "fieldConfig": {
            "defaults": {
              "color": {
                "mode": "thresholds"
              },
              "custom": {
                "align": "auto",
                "displayMode": "auto"
              },
              "mappings": [],
              "thresholds": {
                "mode": "absolute",
                "steps": [
                  {
                    "color": "green"
                  },
                  {
                    "color": "red",
                    "value": 80
                  }
                ]
              }
            },
            "overrides": [
              {
                "matcher": {
                  "id": "byName",
                  "options": "Index"
                },
                "properties": [
                  {
                    "id": "custom.width",
                    "value": 70
                  }
                ]
              },
              {
                "matcher": {
                  "id": "byName",
                  "options": "Reg Client Count"
                },
                "properties": [
                  {
                    "id": "custom.width",
                    "value": 132
                  }
                ]
              },
              {
                "matcher": {
                  "id": "byName",
                  "options": "Auth clients count"
                },
                "properties": [
                  {
                    "id": "custom.width",
                    "value": 133
                  }
                ]
              },
              {
                "matcher": {
                  "id": "byName",
                  "options": "Interface state"
                },
                "properties": [
                  {
                    "id": "custom.width",
                    "value": 120
                  }
                ]
              }
            ]
          },
          "gridPos": {
            "h": 8,
            "w": 10,
            "x": 14,
            "y": 4
          },
          "id": 1679,
          "options": {
            "footer": {
              "fields": "",
              "reducer": [
                "sum"
              ],
              "show": false
            },
            "showHeader": true,
            "sortBy": []
          },
          "pluginVersion": "8.3.4",
          "targets": [
            {
              "datasource": {
                "type": "prometheus",
                "uid": "${DS_PROMETHEUS}"
              },
              "exemplar": true,
              "expr": "mtxrWlCMState{instance='$instance'}",
              "format": "table",
              "hide": false,
              "instant": true,
              "interval": "",
              "legendFormat": "",
              "refId": "A"
            },
            {
              "datasource": {
                "type": "prometheus",
                "uid": "${DS_PROMETHEUS}"
              },
              "exemplar": true,
              "expr": "mtxrWlCMRegClientCount{instance='$instance'}",
              "format": "table",
              "hide": false,
              "instant": true,
              "interval": "",
              "legendFormat": "",
              "refId": "B"
            },
            {
              "datasource": {
                "type": "prometheus",
                "uid": "${DS_PROMETHEUS}"
              },
              "exemplar": true,
              "expr": "mtxrWlCMChannel{instance='$instance'}",
              "format": "table",
              "hide": false,
              "instant": true,
              "interval": "",
              "legendFormat": "",
              "refId": "C"
            },
            {
              "datasource": {
                "type": "prometheus",
                "uid": "${DS_PROMETHEUS}"
              },
              "exemplar": true,
              "expr": "mtxrWlCMAuthClientCount{instance='$instance'}",
              "format": "table",
              "hide": false,
              "instant": true,
              "interval": "",
              "legendFormat": "",
              "refId": "D"
            },
            {
              "datasource": {
                "type": "prometheus",
                "uid": "${DS_PROMETHEUS}"
              },
              "exemplar": true,
              "expr": "mtxrWlCMRtabSsid{instance='$instance'}",
              "format": "table",
              "hide": false,
              "instant": true,
              "interval": "",
              "legendFormat": "",
              "refId": "E"
            }
          ],
          "title": "CAP interface",
          "transformations": [
            {
              "id": "seriesToColumns",
              "options": {
                "byField": "mtxrWlCMIndex"
              }
            },
            {
              "id": "organize",
              "options": {
                "excludeByName": {
                  "Time 1": true,
                  "Time 2": true,
                  "Time 3": true,
                  "Time 4": true,
                  "Value #A": true,
                  "Value #B": false,
                  "Value #C": true,
                  "__name__ 1": true,
                  "__name__ 2": true,
                  "__name__ 3": true,
                  "__name__ 4": true,
                  "instance 1": true,
                  "instance 2": true,
                  "instance 3": true,
                  "instance 4": true,
                  "job 1": true,
                  "job 2": true,
                  "job 3": true,
                  "job 4": true
                },
                "indexByName": {
                  "Time 1": 1,
                  "Time 2": 7,
                  "Time 3": 13,
                  "Time 4": 19,
                  "Value #A": 6,
                  "Value #B": 11,
                  "Value #C": 18,
                  "Value #D": 12,
                  "__name__ 1": 2,
                  "__name__ 2": 8,
                  "__name__ 3": 14,
                  "__name__ 4": 20,
                  "instance 1": 3,
                  "instance 2": 9,
                  "instance 3": 15,
                  "instance 4": 21,
                  "job 1": 4,
                  "job 2": 10,
                  "job 3": 16,
                  "job 4": 22,
                  "mtxrWlCMChannel": 17,
                  "mtxrWlCMIndex": 0,
                  "mtxrWlCMState": 5
                },
                "renameByName": {
                  "Time 1": "",
                  "Time 4": "",
                  "Value #A": "",
                  "Value #B": "Reg Client Count",
                  "Value #C": "",
                  "Value #D": "Auth clients count",
                  "__name__ 4": "",
                  "instance 4": "",
                  "job 1": "",
                  "job 2": "",
                  "job 4": "",
                  "mtxrWlCMChannel": "Channel for master only",
                  "mtxrWlCMIndex": "Index",
                  "mtxrWlCMState": "Interface state"
                }
              }
            }
          ],
          "type": "table"
        },
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${DS_PROMETHEUS}"
          },
          "description": "Wireless CAPSMAN remote-cap entry count",
          "fieldConfig": {
            "defaults": {
              "color": {
                "mode": "thresholds"
              },
              "mappings": [],
              "thresholds": {
                "mode": "absolute",
                "steps": [
                  {
                    "color": "#299c46"
                  }
                ]
              }
            },
            "overrides": []
          },
          "gridPos": {
            "h": 4,
            "w": 3,
            "x": 0,
            "y": 8
          },
          "id": 1680,
          "options": {
            "colorMode": "value",
            "graphMode": "none",
            "justifyMode": "auto",
            "orientation": "auto",
            "reduceOptions": {
              "calcs": [
                "lastNotNull"
              ],
              "fields": "",
              "values": false
            },
            "text": {},
            "textMode": "auto"
          },
          "pluginVersion": "8.3.4",
          "targets": [
            {
              "datasource": {
                "type": "prometheus",
                "uid": "${DS_PROMETHEUS}"
              },
              "exemplar": true,
              "expr": "mtxrWlCMREntryCount{instance='$instance'}",
              "format": "time_series",
              "hide": false,
              "instant": true,
              "interval": "",
              "legendFormat": "",
              "refId": "A"
            }
          ],
          "title": "remote-cap entry count",
          "type": "stat"
        },
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${DS_PROMETHEUS}"
          },
          "description": "",
          "fieldConfig": {
            "defaults": {
              "color": {
                "mode": "thresholds"
              },
              "custom": {
                "align": "auto",
                "displayMode": "auto"
              },
              "mappings": [],
              "thresholds": {
                "mode": "absolute",
                "steps": [
                  {
                    "color": "green"
                  },
                  {
                    "color": "red",
                    "value": 80
                  }
                ]
              }
            },
            "overrides": [
              {
                "matcher": {
                  "id": "byName",
                  "options": "Mac address"
                },
                "properties": [
                  {
                    "id": "custom.width",
                    "value": 130
                  },
                  {
                    "id": "custom.align",
                    "value": "center"
                  }
                ]
              },
              {
                "matcher": {
                  "id": "byName",
                  "options": "Uptime"
                },
                "properties": [
                  {
                    "id": "custom.align",
                    "value": "center"
                  },
                  {
                    "id": "unit",
                    "value": "timeticks"
                  },
                  {
                    "id": "custom.width",
                    "value": 106
                  }
                ]
              },
              {
                "matcher": {
                  "id": "byName",
                  "options": "Strength"
                },
                "properties": [
                  {
                    "id": "unit",
                    "value": "dBm"
                  },
                  {
                    "id": "custom.displayMode",
                    "value": "lcd-gauge"
                  },
                  {
                    "id": "min",
                    "value": -85
                  },
                  {
                    "id": "max",
                    "value": -30
                  },
                  {
                    "id": "color",
                    "value": {
                      "mode": "continuous-RdYlGr"
                    }
                  },
                  {
                    "id": "custom.width",
                    "value": 250
                  },
                  {
                    "id": "custom.align",
                    "value": "center"
                  }
                ]
              },
              {
                "matcher": {
                  "id": "byName",
                  "options": "Rx Rate"
                },
                "properties": [
                  {
                    "id": "custom.width",
                    "value": 100
                  },
                  {
                    "id": "unit",
                    "value": "bps"
                  },
                  {
                    "id": "custom.align",
                    "value": "center"
                  }
                ]
              },
              {
                "matcher": {
                  "id": "byName",
                  "options": "Rx Bytes"
                },
                "properties": [
                  {
                    "id": "custom.width",
                    "value": 100
                  },
                  {
                    "id": "unit",
                    "value": "bytes"
                  }
                ]
              },
              {
                "matcher": {
                  "id": "byName",
                  "options": "Rx Packets"
                },
                "properties": [
                  {
                    "id": "custom.width",
                    "value": 145
                  }
                ]
              },
              {
                "matcher": {
                  "id": "byName",
                  "options": "Tx Rate"
                },
                "properties": [
                  {
                    "id": "custom.width",
                    "value": 100
                  },
                  {
                    "id": "unit",
                    "value": "bps"
                  },
                  {
                    "id": "custom.align",
                    "value": "center"
                  }
                ]
              },
              {
                "matcher": {
                  "id": "byName",
                  "options": "Tx Bytes"
                },
                "properties": [
                  {
                    "id": "custom.width",
                    "value": 100
                  },
                  {
                    "id": "unit",
                    "value": "bytes"
                  }
                ]
              },
              {
                "matcher": {
                  "id": "byName",
                  "options": "SSID"
                },
                "properties": [
                  {
                    "id": "custom.width"
                  },
                  {
                    "id": "custom.align",
                    "value": "center"
                  }
                ]
              },
              {
                "matcher": {
                  "id": "byName",
                  "options": "interface index"
                },
                "properties": [
                  {
                    "id": "custom.width",
                    "value": 115
                  },
                  {
                    "id": "custom.align",
                    "value": "center"
                  }
                ]
              }
            ]
          },
          "gridPos": {
            "h": 7,
            "w": 24,
            "x": 0,
            "y": 12
          },
          "id": 1678,
          "options": {
            "footer": {
              "fields": "",
              "reducer": [
                "sum"
              ],
              "show": false
            },
            "showHeader": true,
            "sortBy": [
              {
                "desc": true,
                "displayName": "SSID"
              }
            ]
          },
          "pluginVersion": "8.3.4",
          "targets": [
            {
              "datasource": {
                "type": "prometheus",
                "uid": "${DS_PROMETHEUS}"
              },
              "exemplar": true,
              "expr": "mtxrWlCMRtabAddr{instance='$instance'}",
              "format": "table",
              "hide": false,
              "instant": true,
              "interval": "",
              "legendFormat": "",
              "refId": "A"
            },
            {
              "datasource": {
                "type": "prometheus",
                "uid": "${DS_PROMETHEUS}"
              },
              "exemplar": true,
              "expr": "mtxrWlCMRtabEapIdent{instance='$instance'}",
              "format": "table",
              "hide": false,
              "instant": true,
              "interval": "",
              "legendFormat": "",
              "refId": "B"
            },
            {
              "datasource": {
                "type": "prometheus",
                "uid": "${DS_PROMETHEUS}"
              },
              "exemplar": true,
              "expr": "mtxrWlCMRtabRxBytes{instance='$instance'}",
              "format": "table",
              "hide": false,
              "instant": true,
              "interval": "",
              "legendFormat": "",
              "refId": "C"
            },
            {
              "datasource": {
                "type": "prometheus",
                "uid": "${DS_PROMETHEUS}"
              },
              "exemplar": true,
              "expr": "mtxrWlCMRtabRxPackets{instance='$instance'}",
              "format": "table",
              "hide": false,
              "instant": true,
              "interval": "",
              "legendFormat": "",
              "refId": "D"
            },
            {
              "datasource": {
                "type": "prometheus",
                "uid": "${DS_PROMETHEUS}"
              },
              "exemplar": true,
              "expr": "mtxrWlCMRtabRxRate{instance='$instance'}",
              "format": "table",
              "hide": false,
              "instant": true,
              "interval": "",
              "legendFormat": "",
              "refId": "E"
            },
            {
              "datasource": {
                "type": "prometheus",
                "uid": "${DS_PROMETHEUS}"
              },
              "exemplar": true,
              "expr": "mtxrWlCMRtabRxStrength{instance='$instance'}",
              "format": "table",
              "hide": false,
              "instant": true,
              "interval": "",
              "legendFormat": "",
              "refId": "F"
            },
            {
              "datasource": {
                "type": "prometheus",
                "uid": "${DS_PROMETHEUS}"
              },
              "exemplar": true,
              "expr": "mtxrWlCMRtabSsid{instance='$instance'}",
              "format": "table",
              "hide": false,
              "instant": true,
              "interval": "",
              "legendFormat": "",
              "refId": "G"
            },
            {
              "datasource": {
                "type": "prometheus",
                "uid": "${DS_PROMETHEUS}"
              },
              "exemplar": true,
              "expr": "mtxrWlCMRtabTxBytes{instance='$instance'}",
              "format": "table",
              "hide": false,
              "instant": true,
              "interval": "",
              "legendFormat": "",
              "refId": "H"
            },
            {
              "datasource": {
                "type": "prometheus",
                "uid": "${DS_PROMETHEUS}"
              },
              "exemplar": true,
              "expr": "mtxrWlCMRtabTxPackets{instance='$instance'}",
              "format": "table",
              "hide": false,
              "instant": true,
              "interval": "",
              "legendFormat": "",
              "refId": "I"
            },
            {
              "datasource": {
                "type": "prometheus",
                "uid": "${DS_PROMETHEUS}"
              },
              "exemplar": true,
              "expr": "mtxrWlCMRtabTxRate{instance='$instance'}",
              "format": "table",
              "hide": false,
              "instant": true,
              "interval": "",
              "legendFormat": "",
              "refId": "J"
            },
            {
              "datasource": {
                "type": "prometheus",
                "uid": "${DS_PROMETHEUS}"
              },
              "exemplar": true,
              "expr": "mtxrWlCMRtabTxStrength{instance='$instance'}",
              "format": "table",
              "hide": false,
              "instant": true,
              "interval": "",
              "legendFormat": "",
              "refId": "K"
            },
            {
              "datasource": {
                "type": "prometheus",
                "uid": "${DS_PROMETHEUS}"
              },
              "exemplar": true,
              "expr": "mtxrWlCMRtabUptime{instance='$instance'}",
              "format": "table",
              "hide": false,
              "instant": true,
              "interval": "",
              "legendFormat": "",
              "refId": "L"
            }
          ],
          "title": "Clients",
          "transformations": [
            {
              "id": "seriesToColumns",
              "options": {
                "byField": "mtxrWlCMRtabAddr"
              }
            },
            {
              "id": "organize",
              "options": {
                "excludeByName": {
                  "Time 1": true,
                  "Time 10": true,
                  "Time 11": true,
                  "Time 12": true,
                  "Time 2": true,
                  "Time 3": true,
                  "Time 4": true,
                  "Time 5": true,
                  "Time 6": true,
                  "Time 7": true,
                  "Time 8": true,
                  "Time 9": true,
                  "Value #A": true,
                  "Value #B": true,
                  "Value #G": true,
                  "Value #I": false,
                  "Value #J": false,
                  "Value #K": true,
                  "__name__ 1": true,
                  "__name__ 10": true,
                  "__name__ 11": true,
                  "__name__ 12": true,
                  "__name__ 2": true,
                  "__name__ 3": true,
                  "__name__ 4": true,
                  "__name__ 5": true,
                  "__name__ 6": true,
                  "__name__ 7": true,
                  "__name__ 8": true,
                  "__name__ 9": true,
                  "instance 1": true,
                  "instance 10": true,
                  "instance 11": true,
                  "instance 12": true,
                  "instance 2": true,
                  "instance 3": true,
                  "instance 4": true,
                  "instance 5": true,
                  "instance 6": true,
                  "instance 7": true,
                  "instance 8": true,
                  "instance 9": true,
                  "job 1": true,
                  "job 10": true,
                  "job 11": true,
                  "job 12": true,
                  "job 2": true,
                  "job 3": true,
                  "job 4": true,
                  "job 5": true,
                  "job 6": true,
                  "job 7": true,
                  "job 8": true,
                  "job 9": true,
                  "mtxrWlCMRtabAddr": false,
                  "mtxrWlCMRtabIface 10": true,
                  "mtxrWlCMRtabIface 11": true,
                  "mtxrWlCMRtabIface 12": true,
                  "mtxrWlCMRtabIface 2": true,
                  "mtxrWlCMRtabIface 3": true,
                  "mtxrWlCMRtabIface 4": true,
                  "mtxrWlCMRtabIface 5": true,
                  "mtxrWlCMRtabIface 6": true,
                  "mtxrWlCMRtabIface 7": true,
                  "mtxrWlCMRtabIface 8": true,
                  "mtxrWlCMRtabIface 9": true,
                  "mtxrWlCMRtabSsid": false
                },
                "indexByName": {
                  "Time 1": 12,
                  "Time 10": 59,
                  "Time 11": 64,
                  "Time 12": 69,
                  "Time 2": 17,
                  "Time 3": 23,
                  "Time 4": 28,
                  "Time 5": 33,
                  "Time 6": 38,
                  "Time 7": 43,
                  "Time 8": 49,
                  "Time 9": 54,
                  "Value #A": 16,
                  "Value #B": 22,
                  "Value #C": 7,
                  "Value #D": 9,
                  "Value #E": 5,
                  "Value #F": 4,
                  "Value #G": 48,
                  "Value #H": 8,
                  "Value #I": 10,
                  "Value #J": 6,
                  "Value #K": 11,
                  "Value #L": 3,
                  "__name__ 1": 13,
                  "__name__ 10": 60,
                  "__name__ 11": 65,
                  "__name__ 12": 70,
                  "__name__ 2": 18,
                  "__name__ 3": 24,
                  "__name__ 4": 29,
                  "__name__ 5": 34,
                  "__name__ 6": 39,
                  "__name__ 7": 44,
                  "__name__ 8": 50,
                  "__name__ 9": 55,
                  "instance 1": 14,
                  "instance 10": 61,
                  "instance 11": 66,
                  "instance 12": 71,
                  "instance 2": 19,
                  "instance 3": 25,
                  "instance 4": 30,
                  "instance 5": 35,
                  "instance 6": 40,
                  "instance 7": 45,
                  "instance 8": 51,
                  "instance 9": 56,
                  "job 1": 15,
                  "job 10": 62,
                  "job 11": 67,
                  "job 12": 72,
                  "job 2": 20,
                  "job 3": 26,
                  "job 4": 31,
                  "job 5": 36,
                  "job 6": 41,
                  "job 7": 46,
                  "job 8": 52,
                  "job 9": 57,
                  "mtxrWlCMRtabAddr": 2,
                  "mtxrWlCMRtabIface 1": 1,
                  "mtxrWlCMRtabIface 10": 63,
                  "mtxrWlCMRtabIface 11": 68,
                  "mtxrWlCMRtabIface 12": 73,
                  "mtxrWlCMRtabIface 2": 21,
                  "mtxrWlCMRtabIface 3": 27,
                  "mtxrWlCMRtabIface 4": 32,
                  "mtxrWlCMRtabIface 5": 37,
                  "mtxrWlCMRtabIface 6": 42,
                  "mtxrWlCMRtabIface 7": 47,
                  "mtxrWlCMRtabIface 8": 53,
                  "mtxrWlCMRtabIface 9": 58,
                  "mtxrWlCMRtabSsid": 0
                },
                "renameByName": {
                  "Time 1": "",
                  "Value #C": "Rx Bytes",
                  "Value #D": "Rx Packets",
                  "Value #E": "Rx Rate",
                  "Value #F": "Strength",
                  "Value #H": "Tx Bytes",
                  "Value #I": "Tx Packets",
                  "Value #J": "Tx Rate",
                  "Value #K": "Tx Strength",
                  "Value #L": "Uptime",
                  "mtxrWlCMRtabAddr": "Mac address",
                  "mtxrWlCMRtabIface 1": "interface index",
                  "mtxrWlCMRtabSsid": "SSID"
                }
              }
            },
            {
              "id": "sortBy",
              "options": {
                "fields": {},
                "sort": [
                  {
                    "field": "SSID"
                  }
                ]
              }
            }
          ],
          "type": "table"
        }
      ],
      "targets": [
        {
          "datasource": {
            "type": "prometheus",
            "uid": "PBFA97CFB590B2093"
          },
          "refId": "A"
        }
      ],
      "title": "CAPsMAN",
      "type": "row"
    },
    {
      "collapsed": true,
      "datasource": {
        "type": "prometheus",
        "uid": "PBFA97CFB590B2093"
      },
      "gridPos": {
        "h": 1,
        "w": 24,
        "x": 0,
        "y": 53
      },
      "id": 1705,
      "panels": [
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${DS_PROMETHEUS}"
          },
          "description": "",
          "fieldConfig": {
            "defaults": {
              "color": {
                "mode": "thresholds"
              },
              "mappings": [],
              "thresholds": {
                "mode": "absolute",
                "steps": [
                  {
                    "color": "#299c46"
                  }
                ]
              },
              "unit": "none"
            },
            "overrides": []
          },
          "gridPos": {
            "h": 4,
            "w": 4,
            "x": 0,
            "y": 5
          },
          "id": 1713,
          "options": {
            "colorMode": "value",
            "graphMode": "none",
            "justifyMode": "center",
            "orientation": "auto",
            "reduceOptions": {
              "calcs": [
                "lastNotNull"
              ],
              "fields": "",
              "values": false
            },
            "text": {},
            "textMode": "name"
          },
          "pluginVersion": "8.3.4",
          "targets": [
            {
              "datasource": {
                "type": "prometheus",
                "uid": "${DS_PROMETHEUS}"
              },
              "exemplar": true,
              "expr": "mtxrWl60GSsid{instance='$instance'}",
              "format": "time_series",
              "hide": false,
              "instant": true,
              "interval": "",
              "legendFormat": "{{mtxrWl60GSsid}}",
              "refId": "A"
            }
          ],
          "title": "ssid",
          "type": "stat"
        },
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${DS_PROMETHEUS}"
          },
          "description": "",
          "fieldConfig": {
            "defaults": {
              "color": {
                "mode": "thresholds"
              },
              "mappings": [],
              "thresholds": {
                "mode": "absolute",
                "steps": [
                  {
                    "color": "#299c46"
                  }
                ]
              },
              "unit": "none"
            },
            "overrides": []
          },
          "gridPos": {
            "h": 4,
            "w": 4,
            "x": 4,
            "y": 5
          },
          "id": 1706,
          "options": {
            "colorMode": "value",
            "graphMode": "none",
            "justifyMode": "center",
            "orientation": "auto",
            "reduceOptions": {
              "calcs": [
                "lastNotNull"
              ],
              "fields": "",
              "values": false
            },
            "text": {},
            "textMode": "auto"
          },
          "pluginVersion": "8.3.4",
          "targets": [
            {
              "datasource": {
                "type": "prometheus",
                "uid": "${DS_PROMETHEUS}"
              },
              "exemplar": true,
              "expr": "mtxrWl60GFreq{instance='$instance'}",
              "format": "time_series",
              "hide": false,
              "instant": true,
              "interval": "",
              "legendFormat": "",
              "refId": "A"
            }
          ],
          "title": "Frequency",
          "type": "stat"
        },
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${DS_PROMETHEUS}"
          },
          "description": "",
          "fieldConfig": {
            "defaults": {
              "color": {
                "mode": "thresholds"
              },
              "mappings": [
                {
                  "options": {
                    "0": {
                      "index": 0,
                      "text": "disconnected"
                    },
                    "1": {
                      "index": 1,
                      "text": "connected"
                    }
                  },
                  "type": "value"
                }
              ],
              "thresholds": {
                "mode": "absolute",
                "steps": [
                  {
                    "color": "dark-red"
                  },
                  {
                    "color": "#299c46",
                    "value": 1
                  }
                ]
              },
              "unit": "none"
            },
            "overrides": []
          },
          "gridPos": {
            "h": 4,
            "w": 4,
            "x": 8,
            "y": 5
          },
          "id": 1707,
          "options": {
            "colorMode": "value",
            "graphMode": "none",
            "justifyMode": "center",
            "orientation": "auto",
            "reduceOptions": {
              "calcs": [
                "lastNotNull"
              ],
              "fields": "",
              "values": false
            },
            "text": {},
            "textMode": "auto"
          },
          "pluginVersion": "8.3.4",
          "targets": [
            {
              "datasource": {
                "type": "prometheus",
                "uid": "${DS_PROMETHEUS}"
              },
              "exemplar": true,
              "expr": "mtxrWl60GConnected{instance='$instance'}",
              "format": "time_series",
              "hide": false,
              "instant": true,
              "interval": "",
              "legendFormat": "",
              "refId": "A"
            }
          ],
          "title": "Connected",
          "type": "stat"
        },
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${DS_PROMETHEUS}"
          },
          "description": "",
          "fieldConfig": {
            "defaults": {
              "color": {
                "mode": "thresholds"
              },
              "mappings": [
                {
                  "options": {
                    "0": {
                      "index": 0,
                      "text": "AP Bridge"
                    },
                    "1": {
                      "index": 1,
                      "text": "Station Bridge"
                    },
                    "2": {
                      "index": 2,
                      "text": "Sniff"
                    },
                    "3": {
                      "index": 3,
                      "text": "Bridge"
                    }
                  },
                  "type": "value"
                }
              ],
              "thresholds": {
                "mode": "absolute",
                "steps": [
                  {
                    "color": "#299c46"
                  }
                ]
              },
              "unit": "none"
            },
            "overrides": []
          },
          "gridPos": {
            "h": 4,
            "w": 4,
            "x": 12,
            "y": 5
          },
          "id": 1709,
          "options": {
            "colorMode": "value",
            "graphMode": "none",
            "justifyMode": "center",
            "orientation": "auto",
            "reduceOptions": {
              "calcs": [
                "lastNotNull"
              ],
              "fields": "",
              "values": false
            },
            "text": {},
            "textMode": "auto"
          },
          "pluginVersion": "8.3.4",
          "targets": [
            {
              "datasource": {
                "type": "prometheus",
                "uid": "${DS_PROMETHEUS}"
              },
              "exemplar": true,
              "expr": "mtxrWl60GMode{instance='$instance'}",
              "format": "time_series",
              "hide": false,
              "instant": true,
              "interval": "",
              "legendFormat": "",
              "refId": "A"
            }
          ],
          "title": "Mode",
          "type": "stat"
        },
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${DS_PROMETHEUS}"
          },
          "description": "",
          "fieldConfig": {
            "defaults": {
              "color": {
                "mode": "palette-classic"
              },
              "custom": {
                "axisLabel": "",
                "axisPlacement": "auto",
                "barAlignment": 0,
                "drawStyle": "line",
                "fillOpacity": 0,
                "gradientMode": "none",
                "hideFrom": {
                  "legend": false,
                  "tooltip": false,
                  "viz": false
                },
                "lineInterpolation": "linear",
                "lineWidth": 1,
                "pointSize": 5,
                "scaleDistribution": {
                  "type": "linear"
                },
                "showPoints": "auto",
                "spanNulls": false,
                "stacking": {
                  "group": "A",
                  "mode": "none"
                },
                "thresholdsStyle": {
                  "mode": "off"
                }
              },
              "mappings": [],
              "thresholds": {
                "mode": "absolute",
                "steps": [
                  {
                    "color": "#299c46"
                  }
                ]
              },
              "unit": "none"
            },
            "overrides": []
          },
          "gridPos": {
            "h": 8,
            "w": 8,
            "x": 16,
            "y": 5
          },
          "id": 1712,
          "options": {
            "legend": {
              "calcs": [
                "lastNotNull",
                "min",
                "max",
                "mean"
              ],
              "displayMode": "table",
              "placement": "bottom"
            },
            "tooltip": {
              "mode": "single"
            }
          },
          "pluginVersion": "8.2.1",
          "targets": [
            {
              "datasource": {
                "type": "prometheus",
                "uid": "${DS_PROMETHEUS}"
              },
              "exemplar": true,
              "expr": "mtxrWl60GRssi{instance='$instance'}",
              "format": "time_series",
              "hide": false,
              "instant": true,
              "interval": "",
              "legendFormat": "RSSI",
              "refId": "A"
            }
          ],
          "title": "RSSI",
          "type": "timeseries"
        },
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${DS_PROMETHEUS}"
          },
          "description": "",
          "fieldConfig": {
            "defaults": {
              "color": {
                "mode": "thresholds"
              },
              "mappings": [],
              "thresholds": {
                "mode": "absolute",
                "steps": [
                  {
                    "color": "#299c46"
                  }
                ]
              },
              "unit": "none"
            },
            "overrides": []
          },
          "gridPos": {
            "h": 4,
            "w": 2,
            "x": 0,
            "y": 9
          },
          "id": 1710,
          "options": {
            "colorMode": "value",
            "graphMode": "none",
            "justifyMode": "center",
            "orientation": "auto",
            "reduceOptions": {
              "calcs": [
                "lastNotNull"
              ],
              "fields": "",
              "values": false
            },
            "text": {},
            "textMode": "auto"
          },
          "pluginVersion": "8.3.4",
          "targets": [
            {
              "datasource": {
                "type": "prometheus",
                "uid": "${DS_PROMETHEUS}"
              },
              "exemplar": true,
              "expr": "mtxrWl60GPhyRate{instance='$instance'}",
              "format": "time_series",
              "hide": false,
              "instant": true,
              "interval": "",
              "legendFormat": "",
              "refId": "A"
            }
          ],
          "title": "PhyRate",
          "type": "stat"
        },
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${DS_PROMETHEUS}"
          },
          "description": "",
          "fieldConfig": {
            "defaults": {
              "color": {
                "mode": "thresholds"
              },
              "mappings": [],
              "thresholds": {
                "mode": "absolute",
                "steps": [
                  {
                    "color": "#299c46"
                  }
                ]
              },
              "unit": "none"
            },
            "overrides": []
          },
          "gridPos": {
            "h": 4,
            "w": 2,
            "x": 2,
            "y": 9
          },
          "id": 1714,
          "options": {
            "colorMode": "value",
            "graphMode": "none",
            "justifyMode": "center",
            "orientation": "auto",
            "reduceOptions": {
              "calcs": [
                "lastNotNull"
              ],
              "fields": "",
              "values": false
            },
            "text": {},
            "textMode": "auto"
          },
          "pluginVersion": "8.3.4",
          "targets": [
            {
              "datasource": {
                "type": "prometheus",
                "uid": "${DS_PROMETHEUS}"
              },
              "exemplar": true,
              "expr": "mtxrWl60GTxSector{instance='$instance'}",
              "format": "time_series",
              "hide": false,
              "instant": true,
              "interval": "",
              "legendFormat": "",
              "refId": "A"
            }
          ],
          "title": "TxSector",
          "type": "stat"
        },
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${DS_PROMETHEUS}"
          },
          "description": "",
          "fieldConfig": {
            "defaults": {
              "color": {
                "mode": "thresholds"
              },
              "mappings": [],
              "thresholds": {
                "mode": "absolute",
                "steps": [
                  {
                    "color": "#299c46"
                  }
                ]
              },
              "unit": "none"
            },
            "overrides": []
          },
          "gridPos": {
            "h": 4,
            "w": 2,
            "x": 4,
            "y": 9
          },
          "id": 1716,
          "options": {
            "colorMode": "value",
            "graphMode": "none",
            "justifyMode": "center",
            "orientation": "auto",
            "reduceOptions": {
              "calcs": [
                "lastNotNull"
              ],
              "fields": "",
              "values": false
            },
            "text": {},
            "textMode": "auto"
          },
          "pluginVersion": "8.3.4",
          "targets": [
            {
              "datasource": {
                "type": "prometheus",
                "uid": "${DS_PROMETHEUS}"
              },
              "exemplar": true,
              "expr": "mtxrWl60GSignal{instance='$instance'}",
              "format": "time_series",
              "hide": false,
              "instant": true,
              "interval": "",
              "legendFormat": "",
              "refId": "A"
            }
          ],
          "title": "Signal",
          "type": "stat"
        },
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${DS_PROMETHEUS}"
          },
          "description": "",
          "fieldConfig": {
            "defaults": {
              "color": {
                "mode": "thresholds"
              },
              "mappings": [],
              "thresholds": {
                "mode": "absolute",
                "steps": [
                  {
                    "color": "#299c46"
                  }
                ]
              },
              "unit": "none"
            },
            "overrides": []
          },
          "gridPos": {
            "h": 4,
            "w": 2,
            "x": 6,
            "y": 9
          },
          "id": 1715,
          "options": {
            "colorMode": "value",
            "graphMode": "none",
            "justifyMode": "center",
            "orientation": "auto",
            "reduceOptions": {
              "calcs": [
                "lastNotNull"
              ],
              "fields": "/.*/",
              "values": false
            },
            "text": {},
            "textMode": "value_and_name"
          },
          "pluginVersion": "8.3.4",
          "targets": [
            {
              "datasource": {
                "type": "prometheus",
                "uid": "${DS_PROMETHEUS}"
              },
              "exemplar": true,
              "expr": "mtxrWl60GTxSectorInfo{instance='$instance'}",
              "format": "time_series",
              "hide": false,
              "instant": true,
              "interval": "",
              "legendFormat": "",
              "refId": "A"
            }
          ],
          "title": "TxSectorInfo",
          "type": "stat"
        },
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${DS_PROMETHEUS}"
          },
          "description": "Modulation and Coding Scheme",
          "fieldConfig": {
            "defaults": {
              "color": {
                "mode": "thresholds"
              },
              "mappings": [],
              "thresholds": {
                "mode": "absolute",
                "steps": [
                  {
                    "color": "#299c46"
                  }
                ]
              },
              "unit": "none"
            },
            "overrides": []
          },
          "gridPos": {
            "h": 4,
            "w": 4,
            "x": 8,
            "y": 9
          },
          "id": 1708,
          "options": {
            "colorMode": "value",
            "graphMode": "none",
            "justifyMode": "center",
            "orientation": "auto",
            "reduceOptions": {
              "calcs": [
                "lastNotNull"
              ],
              "fields": "",
              "values": false
            },
            "text": {},
            "textMode": "auto"
          },
          "pluginVersion": "8.3.4",
          "targets": [
            {
              "datasource": {
                "type": "prometheus",
                "uid": "${DS_PROMETHEUS}"
              },
              "exemplar": true,
              "expr": "mtxrWl60GMcs{instance='$instance'}",
              "format": "time_series",
              "hide": false,
              "instant": true,
              "interval": "",
              "legendFormat": "",
              "refId": "A"
            }
          ],
          "title": "MCS (Modulation and Coding Scheme)",
          "type": "stat"
        },
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${DS_PROMETHEUS}"
          },
          "description": "",
          "fieldConfig": {
            "defaults": {
              "color": {
                "mode": "thresholds"
              },
              "mappings": [],
              "thresholds": {
                "mode": "absolute",
                "steps": [
                  {
                    "color": "#299c46"
                  }
                ]
              },
              "unit": "none"
            },
            "overrides": []
          },
          "gridPos": {
            "h": 4,
            "w": 4,
            "x": 12,
            "y": 9
          },
          "id": 1711,
          "options": {
            "colorMode": "value",
            "graphMode": "none",
            "justifyMode": "center",
            "orientation": "auto",
            "reduceOptions": {
              "calcs": [
                "lastNotNull"
              ],
              "fields": "",
              "values": false
            },
            "text": {},
            "textMode": "name"
          },
          "pluginVersion": "8.3.4",
          "targets": [
            {
              "datasource": {
                "type": "prometheus",
                "uid": "${DS_PROMETHEUS}"
              },
              "exemplar": true,
              "expr": "mtxrWl60GRemote{instance='$instance'}",
              "format": "time_series",
              "hide": false,
              "instant": true,
              "interval": "",
              "legendFormat": "{{mtxrWl60GRemote}}",
              "refId": "A"
            }
          ],
          "title": "Remote MAC",
          "type": "stat"
        }
      ],
      "targets": [
        {
          "datasource": {
            "type": "prometheus",
            "uid": "PBFA97CFB590B2093"
          },
          "refId": "A"
        }
      ],
      "title": "W60G",
      "type": "row"
    },
    {
      "collapsed": true,
      "datasource": {
        "type": "prometheus",
        "uid": "PBFA97CFB590B2093"
      },
      "gridPos": {
        "h": 1,
        "w": 24,
        "x": 0,
        "y": 54
      },
      "id": 1673,
      "panels": [
        {
          "aliasColors": {
            "CCQ - 1": "#ff2e63",
            "CCQ - 2": "#08d9d6",
            "CCQ - Tilda": "#ff2e63",
            "Noise - 1": "#ff2e63",
            "Noise - 2": "#08d9d6",
            "Noise - Tilda": "light-blue",
            "Noise - Tilda_5": "dark-purple",
            "TX CCQ - Tilda": "#ff2e63"
          },
          "bars": false,
          "dashLength": 10,
          "dashes": false,
          "datasource": {
            "type": "prometheus",
            "uid": "${DS_PROMETHEUS}"
          },
          "description": "Signal Strength: signal strength in dBm (if first ppp-client modem supports)\n\nModem Signal: signal EC/IO in dB (if first ppp-client modem supports)",
          "fill": 1,
          "fillGradient": 0,
          "gridPos": {
            "h": 7,
            "w": 6,
            "x": 0,
            "y": 6
          },
          "hiddenSeries": false,
          "id": 1640,
          "legend": {
            "alignAsTable": true,
            "avg": true,
            "current": true,
            "hideZero": true,
            "max": true,
            "min": true,
            "rightSide": false,
            "show": true,
            "total": false,
            "values": true
          },
          "lines": true,
          "linewidth": 1,
          "links": [],
          "maxPerRow": 2,
          "nullPointMode": "connected",
          "options": {
            "alertThreshold": true
          },
          "percentage": false,
          "pluginVersion": "8.3.4",
          "pointradius": 2,
          "points": false,
          "renderer": "flot",
          "repeatDirection": "h",
          "seriesOverrides": [
            {
              "alias": "2",
              "yaxis": 1
            },
            {
              "alias": "mtxrWlApNoiseFloor{instance=\"192.168.5.1\", job=\"Mikrotik\", mtxrWlApIndex=\"2\"}",
              "yaxis": 2
            },
            {
              "alias": "mtxrWlApNoiseFloor{instance=\"192.168.5.1\", job=\"Mikrotik\", mtxrWlApIndex=\"11\"}",
              "yaxis": 2
            },
            {
              "alias": "mtxrWlApNoiseFloor{instance=\"192.168.5.1\", job=\"Mikrotik\", mtxrWlApIndex=\"1\"}",
              "yaxis": 2
            },
            {
              "alias": "Noise 1",
              "yaxis": 2
            },
            {
              "alias": "Noise 11",
              "yaxis": 2
            },
            {
              "alias": "Noise 2",
              "yaxis": 2
            },
            {
              "alias": "Noise - 2",
              "yaxis": 2
            },
            {
              "alias": "Noise - 11",
              "yaxis": 2
            },
            {
              "alias": "Noise - 1",
              "yaxis": 2
            },
            {
              "alias": "Noise - Tilda",
              "yaxis": 2
            },
            {
              "alias": "Noise - Tilda_5",
              "yaxis": 2
            },
            {
              "alias": "Modem Signal",
              "yaxis": 2
            }
          ],
          "spaceLength": 10,
          "stack": false,
          "steppedLine": false,
          "targets": [
            {
              "datasource": {
                "type": "prometheus",
                "uid": "${DS_PROMETHEUS}"
              },
              "exemplar": true,
              "expr": "mtxrWirelessModemSignalStrength{instance='$instance'}",
              "hide": false,
              "interval": "",
              "legendFormat": "Signal Strength",
              "refId": "A"
            },
            {
              "datasource": {
                "type": "prometheus",
                "uid": "${DS_PROMETHEUS}"
              },
              "exemplar": true,
              "expr": "mtxrWirelessModemSignalECIO{instance='$instance'}",
              "hide": false,
              "interval": "",
              "legendFormat": "Modem Signal",
              "refId": "B"
            }
          ],
          "thresholds": [],
          "timeRegions": [],
          "title": "Modem",
          "tooltip": {
            "shared": true,
            "sort": 0,
            "value_type": "individual"
          },
          "type": "graph",
          "xaxis": {
            "mode": "time",
            "show": true,
            "values": []
          },
          "yaxes": [
            {
              "format": "dBm",
              "label": "",
              "logBase": 1,
              "show": true
            },
            {
              "format": "dB",
              "label": "",
              "logBase": 1,
              "show": true
            }
          ],
          "yaxis": {
            "align": true,
            "alignLevel": 0
          }
        },
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${DS_PROMETHEUS}"
          },
          "description": "",
          "fieldConfig": {
            "defaults": {
              "color": {
                "mode": "thresholds"
              },
              "mappings": [],
              "thresholds": {
                "mode": "absolute",
                "steps": [
                  {
                    "color": "#299c46"
                  }
                ]
              },
              "unit": "s"
            },
            "overrides": []
          },
          "gridPos": {
            "h": 7,
            "w": 4,
            "x": 6,
            "y": 6
          },
          "id": 1674,
          "options": {
            "colorMode": "value",
            "graphMode": "none",
            "justifyMode": "auto",
            "orientation": "auto",
            "reduceOptions": {
              "calcs": [
                "lastNotNull"
              ],
              "fields": "",
              "values": false
            },
            "text": {},
            "textMode": "auto"
          },
          "pluginVersion": "8.3.4",
          "targets": [
            {
              "datasource": {
                "type": "prometheus",
                "uid": "${DS_PROMETHEUS}"
              },
              "exemplar": true,
              "expr": "mtxrUSBPowerReset{instance='$instance'}",
              "hide": false,
              "instant": true,
              "interval": "",
              "legendFormat": "",
              "refId": "A"
            }
          ],
          "title": "USB Power Reset",
          "type": "stat"
        }
      ],
      "targets": [
        {
          "datasource": {
            "type": "prometheus",
            "uid": "PBFA97CFB590B2093"
          },
          "refId": "A"
        }
      ],
      "title": "Modem",
      "type": "row"
    },
    {
      "collapsed": true,
      "datasource": {
        "type": "prometheus",
        "uid": "PBFA97CFB590B2093"
      },
      "gridPos": {
        "h": 1,
        "w": 24,
        "x": 0,
        "y": 55
      },
      "id": 1281,
      "panels": [
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${DS_PROMETHEUS}"
          },
          "description": "",
          "fieldConfig": {
            "defaults": {
              "color": {
                "mode": "palette-classic"
              },
              "custom": {
                "axisLabel": "",
                "axisPlacement": "auto",
                "barAlignment": 0,
                "drawStyle": "line",
                "fillOpacity": 50,
                "gradientMode": "opacity",
                "hideFrom": {
                  "legend": false,
                  "tooltip": false,
                  "viz": false
                },
                "lineInterpolation": "smooth",
                "lineWidth": 2,
                "pointSize": 5,
                "scaleDistribution": {
                  "type": "linear"
                },
                "showPoints": "never",
                "spanNulls": false,
                "stacking": {
                  "group": "A",
                  "mode": "none"
                },
                "thresholdsStyle": {
                  "mode": "off"
                }
              },
              "mappings": [],
              "min": 0,
              "thresholds": {
                "mode": "absolute",
                "steps": [
                  {
                    "color": "green"
                  }
                ]
              },
              "unit": "Bps"
            },
            "overrides": []
          },
          "gridPos": {
            "h": 6,
            "w": 12,
            "x": 0,
            "y": 7
          },
          "id": 1268,
          "links": [],
          "options": {
            "legend": {
              "calcs": [
                "mean",
                "lastNotNull",
                "max"
              ],
              "displayMode": "table",
              "placement": "right"
            },
            "tooltip": {
              "mode": "multi"
            }
          },
          "pluginVersion": "8.2.1",
          "repeatDirection": "h",
          "targets": [
            {
              "datasource": {
                "type": "prometheus",
                "uid": "${DS_PROMETHEUS}"
              },
              "exemplar": true,
              "expr": "(irate(mtxrQueueSimpleBytesIn{instance='$instance'}[$__rate_interval])*on(mtxrQueueSimpleIndex)group_left(mtxrQueueSimpleName)mtxrQueueSimpleName{instance='$instance'})*8 ",
              "instant": false,
              "interval": "",
              "legendFormat": "In - {{mtxrQueueSimpleName}}",
              "refId": "A"
            },
            {
              "datasource": {
                "type": "prometheus",
                "uid": "${DS_PROMETHEUS}"
              },
              "exemplar": true,
              "expr": "(irate(mtxrQueueSimpleBytesOut{instance='$instance'}[$__rate_interval])*on(mtxrQueueSimpleIndex)group_left(mtxrQueueSimpleName)mtxrQueueSimpleName{instance='$instance'})*8",
              "instant": false,
              "interval": "",
              "legendFormat": "Out - {{mtxrQueueSimpleName}}",
              "refId": "B"
            },
            {
              "datasource": {
                "type": "prometheus",
                "uid": "${DS_PROMETHEUS}"
              },
              "exemplar": true,
              "expr": "(mtxrQueueSimplePCQQueuesIn{instance='$instance'}*on(mtxrQueueSimpleIndex)group_left(mtxrQueueSimpleName)mtxrQueueSimpleName{instance='$instance'})",
              "hide": false,
              "instant": false,
              "interval": "",
              "intervalFactor": 1,
              "legendFormat": "PCQ In - {{mtxrQueueSimpleName}}",
              "refId": "D"
            },
            {
              "datasource": {
                "type": "prometheus",
                "uid": "${DS_PROMETHEUS}"
              },
              "exemplar": true,
              "expr": "(mtxrQueueSimplePCQQueuesOut{instance='$instance'}*on(mtxrQueueSimpleIndex)group_left(mtxrQueueSimpleName)mtxrQueueSimpleName{instance='$instance'})",
              "hide": false,
              "instant": false,
              "interval": "",
              "intervalFactor": 1,
              "legendFormat": "PCQ Out - {{mtxrQueueSimpleName}}",
              "refId": "C"
            }
          ],
          "title": "All Simple Queue",
          "type": "timeseries"
        },
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${DS_PROMETHEUS}"
          },
          "description": "Showing values > 0",
          "fieldConfig": {
            "defaults": {
              "color": {
                "mode": "palette-classic"
              },
              "custom": {
                "axisLabel": "",
                "axisPlacement": "auto",
                "barAlignment": 0,
                "drawStyle": "line",
                "fillOpacity": 50,
                "gradientMode": "opacity",
                "hideFrom": {
                  "legend": false,
                  "tooltip": false,
                  "viz": false
                },
                "lineInterpolation": "smooth",
                "lineWidth": 2,
                "pointSize": 5,
                "scaleDistribution": {
                  "type": "linear"
                },
                "showPoints": "never",
                "spanNulls": false,
                "stacking": {
                  "group": "A",
                  "mode": "none"
                },
                "thresholdsStyle": {
                  "mode": "off"
                }
              },
              "mappings": [],
              "min": 0,
              "thresholds": {
                "mode": "absolute",
                "steps": [
                  {
                    "color": "green"
                  },
                  {
                    "color": "red",
                    "value": 80
                  }
                ]
              },
              "unit": "Bps"
            },
            "overrides": []
          },
          "gridPos": {
            "h": 6,
            "w": 12,
            "x": 0,
            "y": 13
          },
          "id": 1282,
          "links": [],
          "options": {
            "legend": {
              "calcs": [
                "mean",
                "lastNotNull",
                "max"
              ],
              "displayMode": "table",
              "placement": "right"
            },
            "tooltip": {
              "mode": "single"
            }
          },
          "pluginVersion": "8.2.1",
          "repeat": "queuesimple_name",
          "repeatDirection": "h",
          "targets": [
            {
              "datasource": {
                "type": "prometheus",
                "uid": "${DS_PROMETHEUS}"
              },
              "exemplar": true,
              "expr": "(irate(mtxrQueueSimpleBytesIn{instance='$instance'}[$__rate_interval])*on(mtxrQueueSimpleIndex)group_left(mtxrQueueSimpleName)mtxrQueueSimpleName{mtxrQueueSimpleName='$queuesimple_name', instance='$instance'})*8",
              "instant": false,
              "interval": "",
              "legendFormat": "In",
              "refId": "A"
            },
            {
              "datasource": {
                "type": "prometheus",
                "uid": "${DS_PROMETHEUS}"
              },
              "exemplar": true,
              "expr": "(irate(mtxrQueueSimpleBytesOut{instance='$instance'}[$__rate_interval])*on(mtxrQueueSimpleIndex)group_left(mtxrQueueSimpleName)mtxrQueueSimpleName{mtxrQueueSimpleName='$queuesimple_name', instance='$instance'})*8",
              "instant": false,
              "interval": "",
              "legendFormat": "Out",
              "refId": "B"
            },
            {
              "datasource": {
                "type": "prometheus",
                "uid": "${DS_PROMETHEUS}"
              },
              "exemplar": true,
              "expr": "(irate(mtxrQueueSimpleDroppedIn{instance='$instance'}[$__rate_interval])*on(mtxrQueueSimpleIndex)group_left(mtxrQueueSimpleName)mtxrQueueSimpleName{mtxrQueueSimpleName='$queuesimple_name', instance='$instance'})",
              "format": "time_series",
              "hide": false,
              "interval": "",
              "legendFormat": "Dropped In",
              "refId": "C"
            },
            {
              "datasource": {
                "type": "prometheus",
                "uid": "${DS_PROMETHEUS}"
              },
              "exemplar": true,
              "expr": "(irate(mtxrQueueSimpleDroppedOut{instance='$instance'}[$__rate_interval])*on(mtxrQueueSimpleIndex)group_left(mtxrQueueSimpleName)mtxrQueueSimpleName{mtxrQueueSimpleName='$queuesimple_name', instance='$instance'})",
              "hide": false,
              "interval": "",
              "legendFormat": "Dropped Out ",
              "refId": "D"
            },
            {
              "datasource": {
                "type": "prometheus",
                "uid": "${DS_PROMETHEUS}"
              },
              "exemplar": true,
              "expr": "(mtxrQueueSimplePCQQueuesIn{instance='$instance'}*on(mtxrQueueSimpleIndex)group_left(mtxrQueueSimpleName)mtxrQueueSimpleName{mtxrQueueSimpleName='$queuesimple_name',instance='$instance'})",
              "hide": false,
              "interval": "",
              "legendFormat": "PCQ-In",
              "refId": "E"
            },
            {
              "datasource": {
                "type": "prometheus",
                "uid": "${DS_PROMETHEUS}"
              },
              "exemplar": true,
              "expr": "(mtxrQueueSimplePCQQueuesOut{instance='$instance'}*on(mtxrQueueSimpleIndex)group_left(mtxrQueueSimpleName)mtxrQueueSimpleName{mtxrQueueSimpleName='$queuesimple_name',instance='$instance'})",
              "hide": false,
              "interval": "",
              "legendFormat": "PCQ-Out",
              "refId": "F"
            }
          ],
          "title": "Queue $queuesimple_name",
          "type": "timeseries"
        }
      ],
      "targets": [
        {
          "datasource": {
            "type": "prometheus",
            "uid": "PBFA97CFB590B2093"
          },
          "refId": "A"
        }
      ],
      "title": "Simple Queue (In/Out/Dropped/PCQ)",
      "type": "row"
    },
    {
      "collapsed": true,
      "datasource": {
        "type": "prometheus",
        "uid": "PBFA97CFB590B2093"
      },
      "gridPos": {
        "h": 1,
        "w": 24,
        "x": 0,
        "y": 56
      },
      "id": 1548,
      "panels": [
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${DS_PROMETHEUS}"
          },
          "description": "",
          "fieldConfig": {
            "defaults": {
              "color": {
                "mode": "palette-classic"
              },
              "custom": {
                "axisLabel": "",
                "axisPlacement": "auto",
                "barAlignment": 0,
                "drawStyle": "line",
                "fillOpacity": 50,
                "gradientMode": "opacity",
                "hideFrom": {
                  "legend": false,
                  "tooltip": false,
                  "viz": false
                },
                "lineInterpolation": "smooth",
                "lineWidth": 2,
                "pointSize": 5,
                "scaleDistribution": {
                  "type": "linear"
                },
                "showPoints": "never",
                "spanNulls": false,
                "stacking": {
                  "group": "A",
                  "mode": "none"
                },
                "thresholdsStyle": {
                  "mode": "off"
                }
              },
              "mappings": [],
              "thresholds": {
                "mode": "absolute",
                "steps": [
                  {
                    "color": "green"
                  }
                ]
              },
              "unit": "binBps"
            },
            "overrides": []
          },
          "gridPos": {
            "h": 6,
            "w": 12,
            "x": 0,
            "y": 8
          },
          "id": 1510,
          "links": [],
          "options": {
            "legend": {
              "calcs": [
                "mean",
                "lastNotNull",
                "max"
              ],
              "displayMode": "table",
              "placement": "right"
            },
            "tooltip": {
              "mode": "multi"
            }
          },
          "pluginVersion": "8.2.1",
          "repeatDirection": "h",
          "targets": [
            {
              "datasource": {
                "type": "prometheus",
                "uid": "${DS_PROMETHEUS}"
              },
              "exemplar": true,
              "expr": "(irate(mtxrQueueTreeHCBytes{instance='$instance'}[$__rate_interval])*on(mtxrQueueTreeIndex)group_left(mtxrQueueTreeName)mtxrQueueTreeName{instance='$instance'})*8",
              "instant": false,
              "interval": "",
              "intervalFactor": 1,
              "legendFormat": "Bytes - {{mtxrQueueTreeName}}",
              "refId": "A"
            },
            {
              "datasource": {
                "type": "prometheus",
                "uid": "${DS_PROMETHEUS}"
              },
              "exemplar": true,
              "expr": "(irate(mtxrQueueTreePCQQueues{instance='$instance'}[$__rate_interval])*on(mtxrQueueTreeIndex)group_left(mtxrQueueTreeName)mtxrQueueTreeName{instance='$instance'})",
              "hide": false,
              "instant": false,
              "interval": "",
              "intervalFactor": 1,
              "legendFormat": "PCQ - {{mtxrQueueTreeName}}",
              "refId": "B"
            },
            {
              "datasource": {
                "type": "prometheus",
                "uid": "${DS_PROMETHEUS}"
              },
              "exemplar": true,
              "expr": "(irate(mtxrQueueTreeDropped{instance='$instance'}[$__rate_interval])*on(mtxrQueueTreeIndex)group_left(mtxrQueueTreeName)mtxrQueueTreeName{instance='$instance'})",
              "hide": false,
              "instant": false,
              "interval": "",
              "intervalFactor": 1,
              "legendFormat": "Dropped - {{mtxrQueueTreeName}}",
              "refId": "C"
            },
            {
              "datasource": {
                "type": "prometheus",
                "uid": "${DS_PROMETHEUS}"
              },
              "exemplar": true,
              "expr": "(irate(mtxrQueueTreePackets{instance='$instance'}[$__rate_interval])*on(mtxrQueueTreeIndex)group_left(mtxrQueueTreeName)mtxrQueueTreeName{instance='$instance'})",
              "hide": false,
              "instant": false,
              "interval": "",
              "intervalFactor": 1,
              "legendFormat": "Packets - {{mtxrQueueTreeName}}",
              "refId": "D"
            }
          ],
          "title": "All Tree Queue",
          "type": "timeseries"
        },
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${DS_PROMETHEUS}"
          },
          "description": "",
          "fieldConfig": {
            "defaults": {
              "color": {
                "mode": "palette-classic"
              },
              "custom": {
                "axisLabel": "",
                "axisPlacement": "auto",
                "barAlignment": 0,
                "drawStyle": "line",
                "fillOpacity": 50,
                "gradientMode": "opacity",
                "hideFrom": {
                  "legend": false,
                  "tooltip": false,
                  "viz": false
                },
                "lineInterpolation": "smooth",
                "lineWidth": 2,
                "pointSize": 5,
                "scaleDistribution": {
                  "type": "linear"
                },
                "showPoints": "never",
                "spanNulls": false,
                "stacking": {
                  "group": "A",
                  "mode": "none"
                },
                "thresholdsStyle": {
                  "mode": "off"
                }
              },
              "mappings": [],
              "thresholds": {
                "mode": "absolute",
                "steps": [
                  {
                    "color": "green"
                  }
                ]
              },
              "unit": "binBps"
            },
            "overrides": []
          },
          "gridPos": {
            "h": 6,
            "w": 12,
            "x": 12,
            "y": 8
          },
          "id": 1549,
          "links": [],
          "options": {
            "legend": {
              "calcs": [
                "mean",
                "lastNotNull",
                "max"
              ],
              "displayMode": "table",
              "placement": "right"
            },
            "tooltip": {
              "mode": "single"
            }
          },
          "pluginVersion": "8.2.1",
          "repeat": "queuetree_name",
          "repeatDirection": "h",
          "targets": [
            {
              "datasource": {
                "type": "prometheus",
                "uid": "${DS_PROMETHEUS}"
              },
              "exemplar": true,
              "expr": "(irate(mtxrQueueTreeHCBytes{instance='$instance'}[$__rate_interval])*on(mtxrQueueTreeIndex)group_left(mtxrQueueTreeName)mtxrQueueTreeName{mtxrQueueTreeName='$queuetree_name',instance='$instance'})*8",
              "instant": false,
              "interval": "",
              "intervalFactor": 1,
              "legendFormat": "Bytes",
              "refId": "A"
            },
            {
              "datasource": {
                "type": "prometheus",
                "uid": "${DS_PROMETHEUS}"
              },
              "exemplar": true,
              "expr": "(irate(mtxrQueueTreePCQQueues{instance='$instance'}[$__rate_interval])*on(mtxrQueueTreeIndex)group_left(mtxrQueueTreeName)mtxrQueueTreeName{mtxrQueueTreeName='$queuetree_name',instance='$instance'})",
              "hide": false,
              "instant": false,
              "interval": "",
              "intervalFactor": 1,
              "legendFormat": "PCQ",
              "refId": "B"
            },
            {
              "datasource": {
                "type": "prometheus",
                "uid": "${DS_PROMETHEUS}"
              },
              "exemplar": true,
              "expr": "(irate(mtxrQueueTreeDropped{instance='$instance'}[$__rate_interval])*on(mtxrQueueTreeIndex)group_left(mtxrQueueTreeName)mtxrQueueTreeName{mtxrQueueTreeName='$queuetree_name',instance='$instance'})",
              "hide": false,
              "instant": false,
              "interval": "",
              "intervalFactor": 1,
              "legendFormat": "Dropped",
              "refId": "C"
            },
            {
              "datasource": {
                "type": "prometheus",
                "uid": "${DS_PROMETHEUS}"
              },
              "exemplar": true,
              "expr": "(irate(mtxrQueueTreePackets{instance='$instance'}[$__rate_interval])*on(mtxrQueueTreeIndex)group_left(mtxrQueueTreeName)mtxrQueueTreeName{mtxrQueueTreeName='$queuetree_name',instance='$instance'})",
              "hide": false,
              "instant": false,
              "interval": "",
              "legendFormat": "Packets",
              "refId": "E"
            }
          ],
          "title": "Tree Queue $queuetree_name / $queuetree_parent / $queuetree_flow",
          "type": "timeseries"
        }
      ],
      "targets": [
        {
          "datasource": {
            "type": "prometheus",
            "uid": "PBFA97CFB590B2093"
          },
          "refId": "A"
        }
      ],
      "title": "Tree Queue (Bytes/PCQ/Dropped/Packets)",
      "type": "row"
    },
    {
      "collapsed": true,
      "datasource": {
        "type": "prometheus",
        "uid": "PBFA97CFB590B2093"
      },
      "gridPos": {
        "h": 1,
        "w": 24,
        "x": 0,
        "y": 57
      },
      "id": 1338,
      "panels": [
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${DS_PROMETHEUS}"
          },
          "description": "",
          "fieldConfig": {
            "defaults": {
              "color": {
                "mode": "palette-classic"
              },
              "custom": {
                "axisLabel": "",
                "axisPlacement": "auto",
                "barAlignment": 0,
                "drawStyle": "line",
                "fillOpacity": 50,
                "gradientMode": "opacity",
                "hideFrom": {
                  "legend": false,
                  "tooltip": false,
                  "viz": false
                },
                "lineInterpolation": "smooth",
                "lineWidth": 2,
                "pointSize": 5,
                "scaleDistribution": {
                  "type": "linear"
                },
                "showPoints": "never",
                "spanNulls": false,
                "stacking": {
                  "group": "A",
                  "mode": "none"
                },
                "thresholdsStyle": {
                  "mode": "off"
                }
              },
              "mappings": [],
              "thresholds": {
                "mode": "absolute",
                "steps": [
                  {
                    "color": "green"
                  }
                ]
              },
              "unit": "pps"
            },
            "overrides": []
          },
          "gridPos": {
            "h": 11,
            "w": 8,
            "x": 0,
            "y": 9
          },
          "id": 1339,
          "options": {
            "legend": {
              "calcs": [
                "mean",
                "lastNotNull",
                "max",
                "min"
              ],
              "displayMode": "table",
              "placement": "bottom"
            },
            "tooltip": {
              "mode": "multi"
            }
          },
          "pluginVersion": "8.2.1",
          "repeat": "Interface",
          "repeatDirection": "h",
          "targets": [
            {
              "datasource": {
                "type": "prometheus",
                "uid": "${DS_PROMETHEUS}"
              },
              "exemplar": true,
              "expr": "irate(ifHCInMulticastPkts{ifName=~'$Interface',instance='$instance'}[$__rate_interval])",
              "hide": false,
              "interval": "",
              "legendFormat": "In Multicast",
              "refId": "K"
            },
            {
              "datasource": {
                "type": "prometheus",
                "uid": "${DS_PROMETHEUS}"
              },
              "exemplar": true,
              "expr": "-irate(ifHCOutMulticastPkts{ifName=~'$Interface',instance='$instance'}[$__rate_interval])",
              "hide": false,
              "interval": "",
              "legendFormat": "Out Multicast",
              "refId": "L"
            },
            {
              "datasource": {
                "type": "prometheus",
                "uid": "${DS_PROMETHEUS}"
              },
              "exemplar": true,
              "expr": "irate(ifHCInBroadcastPkts{ifName=~'$Interface',instance='$instance'}[$__rate_interval])",
              "hide": false,
              "interval": "",
              "legendFormat": "In Broadcast",
              "refId": "C"
            },
            {
              "datasource": {
                "type": "prometheus",
                "uid": "${DS_PROMETHEUS}"
              },
              "exemplar": true,
              "expr": "-irate(ifHCOutBroadcastPkts{ifName=~'$Interface',instance='$instance'}[$__rate_interval])",
              "hide": false,
              "interval": "",
              "legendFormat": "Out Broadcast",
              "refId": "A"
            },
            {
              "datasource": {
                "type": "prometheus",
                "uid": "${DS_PROMETHEUS}"
              },
              "exemplar": true,
              "expr": "irate(ifHCInUcastPkts{ifName=~'$Interface',instance='$instance'}[$__rate_interval])",
              "hide": false,
              "interval": "",
              "legendFormat": "In Unicast",
              "refId": "B"
            },
            {
              "datasource": {
                "type": "prometheus",
                "uid": "${DS_PROMETHEUS}"
              },
              "exemplar": true,
              "expr": "-irate(ifHCOutUcastPkts{ifName=~'$Interface',instance='$instance'}[$__rate_interval])",
              "hide": false,
              "interval": "",
              "legendFormat": "Out Unicast",
              "refId": "D"
            },
            {
              "datasource": {
                "type": "prometheus",
                "uid": "${DS_PROMETHEUS}"
              },
              "exemplar": true,
              "expr": "irate(ifInDiscards{ifName=~'$Interface',instance='$instance'}[$__rate_interval])",
              "hide": false,
              "interval": "",
              "legendFormat": "In Discard",
              "refId": "E"
            },
            {
              "datasource": {
                "type": "prometheus",
                "uid": "${DS_PROMETHEUS}"
              },
              "exemplar": true,
              "expr": "irate(ifOutDiscards{ifName=~'$Interface',instance='$instance'}[$__rate_interval])",
              "hide": false,
              "interval": "",
              "legendFormat": "Out Discard",
              "refId": "F"
            },
            {
              "datasource": {
                "type": "prometheus",
                "uid": "${DS_PROMETHEUS}"
              },
              "exemplar": true,
              "expr": "irate(ifInErrors{ifName=~'$Interface',instance='$instance'}[$__rate_interval])",
              "hide": false,
              "interval": "",
              "legendFormat": "In Errors",
              "refId": "G"
            },
            {
              "datasource": {
                "type": "prometheus",
                "uid": "${DS_PROMETHEUS}"
              },
              "exemplar": true,
              "expr": "irate(ifOutErrors{ifName=~'$Interface',instance='$instance'}[$__rate_interval])",
              "hide": false,
              "interval": "",
              "legendFormat": "Out Errors",
              "refId": "H"
            },
            {
              "datasource": {
                "type": "prometheus",
                "uid": "${DS_PROMETHEUS}"
              },
              "exemplar": true,
              "expr": "irate(ifInUnknownProtos{ifName=~'$Interface',instance='$instance'}[$__rate_interval])",
              "hide": false,
              "interval": "",
              "legendFormat": "In Unknown Protos",
              "refId": "I"
            },
            {
              "datasource": {
                "type": "prometheus",
                "uid": "${DS_PROMETHEUS}"
              },
              "exemplar": true,
              "expr": "-irate(ifOutQLen{ifName=~'$Interface',instance='$instance'}[$__rate_interval])",
              "hide": false,
              "interval": "",
              "legendFormat": "Out queue length",
              "refId": "J"
            }
          ],
          "title": "Interface \"$Interface\"",
          "type": "timeseries"
        }
      ],
      "targets": [
        {
          "datasource": {
            "type": "prometheus",
            "uid": "PBFA97CFB590B2093"
          },
          "refId": "A"
        }
      ],
      "title": "*cast/Dascard/Errors/Unknown Protos/Queue length",
      "type": "row"
    },
    {
      "collapsed": true,
      "datasource": {
        "type": "prometheus",
        "uid": "PBFA97CFB590B2093"
      },
      "gridPos": {
        "h": 1,
        "w": 24,
        "x": 0,
        "y": 58
      },
      "id": 1285,
      "panels": [
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${DS_PROMETHEUS}"
          },
          "description": "",
          "fieldConfig": {
            "defaults": {
              "color": {
                "mode": "palette-classic"
              },
              "custom": {
                "axisLabel": "",
                "axisPlacement": "auto",
                "barAlignment": 0,
                "drawStyle": "line",
                "fillOpacity": 100,
                "gradientMode": "opacity",
                "hideFrom": {
                  "legend": false,
                  "tooltip": false,
                  "viz": false
                },
                "lineInterpolation": "smooth",
                "lineWidth": 2,
                "pointSize": 5,
                "scaleDistribution": {
                  "type": "linear"
                },
                "showPoints": "never",
                "spanNulls": false,
                "stacking": {
                  "group": "A",
                  "mode": "none"
                },
                "thresholdsStyle": {
                  "mode": "off"
                }
              },
              "mappings": [],
              "thresholds": {
                "mode": "absolute",
                "steps": [
                  {
                    "color": "green"
                  }
                ]
              },
              "unit": "bps"
            },
            "overrides": [
              {
                "matcher": {
                  "id": "byName",
                  "options": "In"
                },
                "properties": [
                  {
                    "id": "color",
                    "value": {
                      "fixedColor": "#6afff3",
                      "mode": "fixed"
                    }
                  }
                ]
              },
              {
                "matcher": {
                  "id": "byName",
                  "options": "Out"
                },
                "properties": [
                  {
                    "id": "color",
                    "value": {
                      "fixedColor": "#bf71ff",
                      "mode": "fixed"
                    }
                  }
                ]
              }
            ]
          },
          "gridPos": {
            "h": 7,
            "w": 8,
            "x": 0,
            "y": 10
          },
          "id": 1286,
          "options": {
            "legend": {
              "calcs": [
                "mean",
                "lastNotNull",
                "max",
                "min"
              ],
              "displayMode": "table",
              "placement": "bottom"
            },
            "tooltip": {
              "mode": "multi"
            }
          },
          "pluginVersion": "8.2.1",
          "repeat": "Interface",
          "repeatDirection": "h",
          "targets": [
            {
              "datasource": {
                "type": "prometheus",
                "uid": "${DS_PROMETHEUS}"
              },
              "exemplar": true,
              "expr": "irate(ifHCInOctets{ifName=~'$Interface',instance='$instance'}[$__rate_interval])*8",
              "format": "time_series",
              "hide": false,
              "interval": "",
              "intervalFactor": 1,
              "legendFormat": "In",
              "refId": "A"
            },
            {
              "datasource": {
                "type": "prometheus",
                "uid": "${DS_PROMETHEUS}"
              },
              "exemplar": true,
              "expr": "-irate(ifHCOutOctets{ifName=~'$Interface',instance='$instance'}[$__rate_interval])*8",
              "hide": false,
              "interval": "",
              "intervalFactor": 1,
              "legendFormat": "Out",
              "refId": "B"
            }
          ],
          "title": "Traffic \"$Interface\"",
          "type": "timeseries"
        }
      ],
      "targets": [
        {
          "datasource": {
            "type": "prometheus",
            "uid": "PBFA97CFB590B2093"
          },
          "refId": "A"
        }
      ],
      "title": "Interfaces Traffic",
      "type": "row"
    }
  ],
  "refresh": "10s",
  "schemaVersion": 36,
  "style": "dark",
  "tags": [
    "prometheus",
    "Mikrotik",
    "snmp",
    "snmp v3",
    "snmp_exporter"
  ],
  "templating": {
    "list": [
      {
        "current": {
          "selected": false,
          "text": "Prometheus",
          "value": "Prometheus"
        },
        "hide": 2,
        "includeAll": false,
        "label": "datasource",
        "multi": false,
        "name": "DS_PROMETHEUS",
        "options": [],
        "query": "prometheus",
        "refresh": 1,
        "regex": "",
        "skipUrlSync": false,
        "type": "datasource"
      },
      {
        "current": {},
        "datasource": {
          "type": "prometheus",
          "uid": "${DS_PROMETHEUS}"
        },
        "definition": "label_values(ifHCInOctets,  job)",
        "hide": 2,
        "includeAll": false,
        "multi": false,
        "name": "Job",
        "options": [],
        "query": {
          "query": "label_values(ifHCInOctets,  job)",
          "refId": "Prometheus-Job-Variable-Query"
        },
        "refresh": 1,
        "regex": "",
        "skipUrlSync": false,
        "sort": 0,
        "tagValuesQuery": "",
        "tagsQuery": "",
        "type": "query",
        "useTags": false
      },
      {
        "current": {},
        "datasource": {
          "type": "prometheus",
          "uid": "${DS_PROMETHEUS}"
        },
        "definition": "query_result(ifInOctets{job=\"snmp-exporter\"})",
        "hide": 0,
        "includeAll": false,
        "multi": false,
        "name": "instance",
        "options": [],
        "query": {
          "query": "label_values(ifHCInOctets,  instance)",
          "refId": "Prometheus-instance-Variable-Query"
        },
        "refresh": 1,
        "regex": "",
        "skipUrlSync": false,
        "sort": 3,
        "tagValuesQuery": "",
        "tagsQuery": "",
        "type": "query",
        "useTags": false
      },
      {
        "current": {},
        "datasource": {
          "type": "prometheus",
          "uid": "${DS_PROMETHEUS}"
        },
        "definition": "label_values(ifHighSpeed{instance='$instance'},ifIndex)",
        "hide": 2,
        "includeAll": false,
        "label": "",
        "multi": false,
        "name": "index",
        "options": [],
        "query": {
          "query": "label_values(ifHighSpeed{instance='$instance'},ifIndex)",
          "refId": "Prometheus-index-Variable-Query"
        },
        "refresh": 1,
        "regex": "",
        "skipUrlSync": false,
        "sort": 3,
        "tagValuesQuery": "",
        "tagsQuery": "",
        "type": "query",
        "useTags": false
      },
      {
        "allValue": "",
        "current": {},
        "datasource": {
          "type": "prometheus",
          "uid": "${DS_PROMETHEUS}"
        },
        "definition": "query_result(sort(ifIndex{ifName=~'^(ether).+',instance='$instance'}) or sort(ifIndex{ifName=~'^(sfp|wlan).+',instance='$instance'}) or sort(ifIndex{ifName=~'^bridge.+',instance='$instance'}) or  sort(ifIndex{ifName!~'^(ether|bridge).+',instance='$instance'}) )",
        "hide": 0,
        "includeAll": true,
        "multi": false,
        "name": "Interface",
        "options": [],
        "query": {
          "query": "query_result(sort(ifIndex{ifName=~'^(ether).+',instance='$instance'}) or sort(ifIndex{ifName=~'^(sfp|wlan).+',instance='$instance'}) or sort(ifIndex{ifName=~'^bridge.+',instance='$instance'}) or  sort(ifIndex{ifName!~'^(ether|bridge).+',instance='$instance'}) )",
          "refId": "Prometheus-Interface-Variable-Query"
        },
        "refresh": 1,
        "regex": "/ifName=\"(.*?)\"/",
        "skipUrlSync": false,
        "sort": 0,
        "tagValuesQuery": "",
        "tagsQuery": "",
        "type": "query",
        "useTags": false
      },
      {
        "current": {},
        "datasource": {
          "type": "prometheus",
          "uid": "${DS_PROMETHEUS}"
        },
        "definition": "query_result(ifHCInOctets{ifName=\"$Interface\",instance=\"$instance\"})",
        "hide": 2,
        "includeAll": false,
        "multi": false,
        "name": "desc",
        "options": [],
        "query": {
          "query": "query_result(ifHCInOctets{ifName=\"$Interface\",instance=\"$instance\"})",
          "refId": "Prometheus-desc-Variable-Query"
        },
        "refresh": 1,
        "regex": "/ifAlias=\"(.*)\",ifDescr/",
        "skipUrlSync": false,
        "sort": 4,
        "tagValuesQuery": "",
        "tagsQuery": "",
        "type": "query",
        "useTags": false
      },
      {
        "allValue": "Null",
        "current": {},
        "datasource": {
          "type": "prometheus",
          "uid": "${DS_PROMETHEUS}"
        },
        "definition": "query_result((mtxrQueueSimplePacketsIn * on (mtxrQueueSimpleIndex) group_left(mtxrQueueSimpleName) mtxrQueueSimpleName{instance='$instance',}))",
        "hide": 2,
        "includeAll": true,
        "label": "",
        "multi": false,
        "name": "queuesimple_name",
        "options": [],
        "query": {
          "query": "query_result((mtxrQueueSimplePacketsIn * on (mtxrQueueSimpleIndex) group_left(mtxrQueueSimpleName) mtxrQueueSimpleName{instance='$instance',}))",
          "refId": "StandardVariableQuery"
        },
        "refresh": 1,
        "regex": "/mtxrQueueSimpleName=\"(.*)\"/",
        "skipUrlSync": false,
        "sort": 0,
        "tagValuesQuery": "",
        "tagsQuery": "",
        "type": "query",
        "useTags": false
      },
      {
        "allValue": "Null",
        "current": {},
        "datasource": {
          "type": "prometheus",
          "uid": "${DS_PROMETHEUS}"
        },
        "definition": "query_result((mtxrQueueTreePackets * on (mtxrQueueTreeIndex) group_left(mtxrQueueTreeName) mtxrQueueTreeName{instance='$instance',}))",
        "hide": 1,
        "includeAll": true,
        "label": "",
        "multi": false,
        "name": "queuetree_name",
        "options": [],
        "query": {
          "query": "query_result((mtxrQueueTreePackets * on (mtxrQueueTreeIndex) group_left(mtxrQueueTreeName) mtxrQueueTreeName{instance='$instance',}))",
          "refId": "StandardVariableQuery"
        },
        "refresh": 1,
        "regex": "/mtxrQueueTreeName=\"(.*)\"/",
        "skipUrlSync": false,
        "sort": 0,
        "tagValuesQuery": "",
        "tagsQuery": "",
        "type": "query",
        "useTags": false
      },
      {
        "allValue": "Null",
        "current": {},
        "datasource": {
          "type": "prometheus",
          "uid": "${DS_PROMETHEUS}"
        },
        "definition": "query_result((mtxrQueueTreeParentIndex * on (mtxrQueueTreeIndex) group_left(mtxrQueueTreeName) mtxrQueueTreeName{instance='$instance',}))",
        "hide": 1,
        "includeAll": true,
        "label": "",
        "multi": false,
        "name": "queuetree_parent",
        "options": [],
        "query": {
          "query": "query_result((mtxrQueueTreeParentIndex * on (mtxrQueueTreeIndex) group_left(mtxrQueueTreeName) mtxrQueueTreeName{instance='$instance',}))",
          "refId": "StandardVariableQuery"
        },
        "refresh": 1,
        "regex": "/mtxrQueueTreeName=\"(.*)\"/",
        "skipUrlSync": false,
        "sort": 0,
        "tagValuesQuery": "",
        "tagsQuery": "",
        "type": "query",
        "useTags": false
      },
      {
        "allValue": "",
        "current": {},
        "datasource": {
          "type": "prometheus",
          "uid": "${DS_PROMETHEUS}"
        },
        "definition": "query_result((mtxrQueueTreeParentIndex * on (mtxrQueueTreeName) group_left(mtxrQueueTreeIndex) mtxrQueueTreeIndex{instance='$instance',}))",
        "hide": 1,
        "includeAll": true,
        "label": "",
        "multi": false,
        "name": "queuetree_flow",
        "options": [],
        "query": {
          "query": "query_result((mtxrQueueTreeParentIndex * on (mtxrQueueTreeName) group_left(mtxrQueueTreeIndex) mtxrQueueTreeIndex{instance='$instance',}))",
          "refId": "StandardVariableQuery"
        },
        "refresh": 1,
        "regex": "/mtxrQueueTreeIndex=\"(.*)\",instance/",
        "skipUrlSync": false,
        "sort": 0,
        "tagValuesQuery": "",
        "tagsQuery": "",
        "type": "query",
        "useTags": false
      }
    ]
  },
  "time": {
    "from": "now-30m",
    "to": "now"
  },
  "timepicker": {
    "refresh_intervals": [
      "5s",
      "10s",
      "30s",
      "1m",
      "5m",
      "15m",
      "30m",
      "1h",
      "2h",
      "1d"
    ],
    "time_options": [
      "5m",
      "15m",
      "1h",
      "6h",
      "12h",
      "24h",
      "2d",
      "7d",
      "30d"
    ]
  },
  "timezone": "",
  "title": "Mikrotik monitoring",
  "uid": "nR3NRDGaz",
  "version": 1,
  "weekStart": ""
}


File: /grafana\provisioning\datasources\datasource.yml
# config file version
apiVersion: 1

# list of datasources that should be deleted from the database
deleteDatasources:
  - name: Prometheus
    orgId: 1

# list of datasources to insert/update depending
# whats available in the database
datasources:
  # <string, required> name of the datasource. Required
- name: Prometheus
  # <string, required> datasource type. Required
  type: prometheus
  # <string, required> access mode. direct or proxy. Required
  access: proxy
  # <int> org id. will default to orgId 1 if not specified
  orgId: 1
  # <string> url
  url: http://mk_prometheus:9090
  # <string> database password, if used
  password:
  # <string> database user, if used
  user:
  # <string> database name, if used
  database:
  # <bool> enable/disable basic auth
  basicAuth: false
  # <string> basic auth username, if used
  basicAuthUser:
  # <string> basic auth password, if used
  basicAuthPassword:
  # <bool> enable/disable with credentials headers
  withCredentials:
  # <bool> mark as default datasource. Max one per org
  isDefault: true
  # <map> fields that will be converted to json and stored in json_data
  jsonData:
     graphiteVersion: "1.1"
     tlsAuth: false
     tlsAuthWithCACert: false
  # <string> json object of data that will be encrypted.
  secureJsonData:
    tlsCACert: "..."
    tlsClientCert: "..."
    tlsClientKey: "..."
  version: 1
  # <bool> allow users to edit datasources from the UI.
  editable: true

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


File: /Mikrotik-snmp-prometheus.json
{
  "__inputs": [
    {
      "name": "DS_PROMETHEUS",
      "label": "Prometheus",
      "description": "",
      "type": "datasource",
      "pluginId": "prometheus",
      "pluginName": "Prometheus"
    }
  ],
  "__elements": {},
  "__requires": [
    {
      "type": "panel",
      "id": "gauge",
      "name": "Gauge",
      "version": ""
    },
    {
      "type": "grafana",
      "id": "grafana",
      "name": "Grafana",
      "version": "9.0.5"
    },
    {
      "type": "panel",
      "id": "graph",
      "name": "Graph (old)",
      "version": ""
    },
    {
      "type": "panel",
      "id": "heatmap",
      "name": "Heatmap",
      "version": ""
    },
    {
      "type": "datasource",
      "id": "prometheus",
      "name": "Prometheus",
      "version": "1.0.0"
    },
    {
      "type": "panel",
      "id": "stat",
      "name": "Stat",
      "version": ""
    },
    {
      "type": "panel",
      "id": "table",
      "name": "Table",
      "version": ""
    },
    {
      "type": "panel",
      "id": "timeseries",
      "name": "Time series",
      "version": ""
    }
  ],
  "annotations": {
    "list": [
      {
        "builtIn": 1,
        "datasource": {
          "type": "datasource",
          "uid": "grafana"
        },
        "enable": true,
        "hide": true,
        "iconColor": "rgba(0, 211, 255, 1)",
        "name": "Annotations & Alerts",
        "target": {
          "limit": 100,
          "matchAny": false,
          "tags": [],
          "type": "dashboard"
        },
        "type": "dashboard"
      }
    ]
  },
  "description": "Mikrotik snmp monitoring (prometheus) 9.0.5",
  "editable": true,
  "fiscalYearStartMonth": 0,
  "gnetId": 14420,
  "graphTooltip": 1,
  "id": null,
  "links": [
    {
      "asDropdown": false,
      "icon": "external link",
      "includeVars": false,
      "keepTime": false,
      "tags": [],
      "targetBlank": true,
      "title": "Github",
      "tooltip": "Open project on Github",
      "type": "link",
      "url": "https://github.com/IgorKha/Grafana-Mikrotik"
    },
    {
      "asDropdown": false,
      "icon": "dashboard",
      "includeVars": false,
      "keepTime": false,
      "tags": [],
      "targetBlank": true,
      "title": "dashboard",
      "tooltip": "Open dashboard",
      "type": "link",
      "url": "https://grafana.com/grafana/dashboards/14420"
    }
  ],
  "liveNow": false,
  "panels": [
    {
      "collapsed": true,
      "datasource": {
        "type": "prometheus",
        "uid": "PBFA97CFB590B2093"
      },
      "gridPos": {
        "h": 1,
        "w": 24,
        "x": 0,
        "y": 0
      },
      "id": 1655,
      "panels": [
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${DS_PROMETHEUS}"
          },
          "description": "Total SNMP time scrape took (walk and processing)",
          "fieldConfig": {
            "defaults": {
              "color": {
                "mode": "thresholds"
              },
              "mappings": [
                {
                  "options": {
                    "result": {
                      "text": ""
                    },
                    "to": 0
                  },
                  "type": "range"
                }
              ],
              "min": 0,
              "thresholds": {
                "mode": "absolute",
                "steps": [
                  {
                    "color": "#299c46",
                    "value": null
                  },
                  {
                    "color": "yellow",
                    "value": 1
                  },
                  {
                    "color": "#EF843C",
                    "value": 1.5
                  },
                  {
                    "color": "red",
                    "value": 2
                  }
                ]
              },
              "unit": "s"
            },
            "overrides": []
          },
          "gridPos": {
            "h": 4,
            "w": 4,
            "x": 0,
            "y": 1
          },
          "id": 1656,
          "links": [],
          "maxDataPoints": 100,
          "options": {
            "colorMode": "value",
            "graphMode": "none",
            "justifyMode": "auto",
            "orientation": "horizontal",
            "reduceOptions": {
              "calcs": [
                "lastNotNull"
              ],
              "fields": "",
              "values": false
            },
            "text": {},
            "textMode": "auto"
          },
          "pluginVersion": "9.0.5",
          "targets": [
            {
              "datasource": {
                "type": "prometheus",
                "uid": "${DS_PROMETHEUS}"
              },
              "exemplar": true,
              "expr": "snmp_scrape_duration_seconds{instance='$instance'}",
              "instant": true,
              "interval": "",
              "legendFormat": "",
              "refId": "A"
            }
          ],
          "title": "Total SNMP time (walk and processing)",
          "type": "stat"
        },
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${DS_PROMETHEUS}"
          },
          "description": "Time SNMP walk/bulkwalk took",
          "fieldConfig": {
            "defaults": {
              "color": {
                "mode": "thresholds"
              },
              "mappings": [
                {
                  "options": {
                    "result": {
                      "text": ""
                    },
                    "to": 0
                  },
                  "type": "range"
                }
              ],
              "min": 0,
              "thresholds": {
                "mode": "absolute",
                "steps": [
                  {
                    "color": "#299c46",
                    "value": null
                  },
                  {
                    "color": "yellow",
                    "value": 1
                  },
                  {
                    "color": "#EF843C",
                    "value": 1.5
                  },
                  {
                    "color": "red",
                    "value": 2
                  }
                ]
              },
              "unit": "s"
            },
            "overrides": []
          },
          "gridPos": {
            "h": 4,
            "w": 4,
            "x": 4,
            "y": 1
          },
          "id": 1657,
          "links": [],
          "maxDataPoints": 100,
          "options": {
            "colorMode": "value",
            "graphMode": "none",
            "justifyMode": "auto",
            "orientation": "horizontal",
            "reduceOptions": {
              "calcs": [
                "lastNotNull"
              ],
              "fields": "",
              "values": false
            },
            "text": {},
            "textMode": "auto"
          },
          "pluginVersion": "9.0.5",
          "targets": [
            {
              "datasource": {
                "type": "prometheus",
                "uid": "${DS_PROMETHEUS}"
              },
              "exemplar": true,
              "expr": "snmp_scrape_walk_duration_seconds{instance='$instance'}",
              "instant": true,
              "interval": "",
              "legendFormat": "",
              "refId": "A"
            }
          ],
          "title": "Time SNMP walk/bulkwalk took",
          "type": "stat"
        },
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${DS_PROMETHEUS}"
          },
          "description": "",
          "fieldConfig": {
            "defaults": {
              "color": {
                "mode": "thresholds"
              },
              "mappings": [
                {
                  "options": {
                    "result": {
                      "text": ""
                    },
                    "to": 0
                  },
                  "type": "range"
                }
              ],
              "min": 0,
              "thresholds": {
                "mode": "absolute",
                "steps": [
                  {
                    "color": "text",
                    "value": null
                  }
                ]
              },
              "unit": "none"
            },
            "overrides": []
          },
          "gridPos": {
            "h": 4,
            "w": 4,
            "x": 8,
            "y": 1
          },
          "id": 1658,
          "links": [],
          "maxDataPoints": 100,
          "options": {
            "colorMode": "value",
            "graphMode": "none",
            "justifyMode": "auto",
            "orientation": "horizontal",
            "reduceOptions": {
              "calcs": [
                "lastNotNull"
              ],
              "fields": "",
              "values": false
            },
            "text": {},
            "textMode": "auto"
          },
          "pluginVersion": "9.0.5",
          "targets": [
            {
              "datasource": {
                "type": "prometheus",
                "uid": "${DS_PROMETHEUS}"
              },
              "exemplar": true,
              "expr": "snmp_scrape_pdus_returned{instance='$instance'}",
              "instant": true,
              "interval": "",
              "legendFormat": "",
              "refId": "A"
            }
          ],
          "title": "scrape pdus returned",
          "type": "stat"
        }
      ],
      "targets": [
        {
          "datasource": {
            "type": "prometheus",
            "uid": "PBFA97CFB590B2093"
          },
          "refId": "A"
        }
      ],
      "title": "SNMP",
      "type": "row"
    },
    {
      "collapsed": false,
      "datasource": {
        "type": "prometheus",
        "uid": "PBFA97CFB590B2093"
      },
      "gridPos": {
        "h": 1,
        "w": 24,
        "x": 0,
        "y": 1
      },
      "id": 1218,
      "panels": [],
      "targets": [
        {
          "datasource": {
            "type": "prometheus",
            "uid": "PBFA97CFB590B2093"
          },
          "refId": "A"
        }
      ],
      "title": "System",
      "type": "row"
    },
    {
      "datasource": {
        "type": "prometheus",
        "uid": "${DS_PROMETHEUS}"
      },
      "fieldConfig": {
        "defaults": {
          "color": {
            "mode": "thresholds"
          },
          "decimals": 2,
          "mappings": [
            {
              "options": {
                "result": {
                  "text": ""
                },
                "to": 0
              },
              "type": "range"
            }
          ],
          "min": 0,
          "thresholds": {
            "mode": "absolute",
            "steps": [
              {
                "color": "green",
                "value": null
              },
              {
                "color": "dark-red",
                "value": 0
              },
              {
                "color": "dark-orange",
                "value": 86400
              },
              {
                "color": "dark-yellow",
                "value": 604800
              },
              {
                "color": "#299c46",
                "value": 2628000
              }
            ]
          },
          "unit": "dtdurations"
        },
        "overrides": []
      },
      "gridPos": {
        "h": 2,
        "w": 4,
        "x": 0,
        "y": 2
      },
      "id": 476,
      "links": [],
      "maxDataPoints": 100,
      "options": {
        "colorMode": "value",
        "graphMode": "none",
        "justifyMode": "auto",
        "orientation": "horizontal",
        "reduceOptions": {
          "calcs": [
            "lastNotNull"
          ],
          "fields": "",
          "values": false
        },
        "text": {},
        "textMode": "auto"
      },
      "pluginVersion": "9.0.5",
      "targets": [
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${DS_PROMETHEUS}"
          },
          "exemplar": true,
          "expr": "sysUpTime{instance='$instance'}/100",
          "interval": "",
          "legendFormat": "",
          "refId": "A"
        }
      ],
      "title": "Uptime",
      "type": "stat"
    },
    {
      "datasource": {
        "type": "prometheus",
        "uid": "${DS_PROMETHEUS}"
      },
      "description": "The current operational state of the device described by this row of the table. A value unknown(1) indicates that the current state of the device is unknown. running(2) indicates that the device is up and running and that no unusual error conditions are known. The warning(3) state indicates that agent has been informed of an unusual error condition by the operational software (e.g., a disk device driver) but that the device is still 'operational'. An example would be a high number of soft errors on a disk. A value of testing(4), indicates that the device is not available for use because it is in the testing state. The state of down(5) is used only when the agent has been informed that the device is not available for any use.",
      "fieldConfig": {
        "defaults": {
          "color": {
            "mode": "thresholds"
          },
          "mappings": [
            {
              "options": {
                "1": {
                  "text": "Unknown"
                },
                "2": {
                  "text": "Running"
                },
                "3": {
                  "text": "Warning!"
                },
                "4": {
                  "text": "Testing"
                },
                "5": {
                  "text": "Down"
                }
              },
              "type": "value"
            }
          ],
          "thresholds": {
            "mode": "absolute",
            "steps": [
              {
                "color": "#299c46",
                "value": null
              },
              {
                "color": "#EAB839",
                "value": 1
              },
              {
                "color": "#299c46",
                "value": 2
              },
              {
                "color": "dark-red",
                "value": 3
              },
              {
                "color": "light-blue",
                "value": 4
              },
              {
                "color": "rgb(69, 69, 71)",
                "value": 5
              }
            ]
          },
          "unit": "none"
        },
        "overrides": []
      },
      "gridPos": {
        "h": 2,
        "w": 2,
        "x": 4,
        "y": 2
      },
      "id": 1220,
      "options": {
        "colorMode": "value",
        "graphMode": "none",
        "justifyMode": "auto",
        "orientation": "auto",
        "reduceOptions": {
          "calcs": [
            "lastNotNull"
          ],
          "fields": "",
          "values": false
        },
        "text": {},
        "textMode": "auto"
      },
      "pluginVersion": "9.0.5",
      "targets": [
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${DS_PROMETHEUS}"
          },
          "exemplar": true,
          "expr": "hrDeviceStatus{instance='$instance', hrDeviceIndex=\"1\"}",
          "instant": true,
          "interval": "",
          "legendFormat": "",
          "refId": "A"
        }
      ],
      "title": "Status device",
      "type": "stat"
    },
    {
      "datasource": {
        "type": "prometheus",
        "uid": "${DS_PROMETHEUS}"
      },
      "description": "The number of errors detected on this device",
      "fieldConfig": {
        "defaults": {
          "color": {
            "mode": "thresholds"
          },
          "mappings": [],
          "thresholds": {
            "mode": "absolute",
            "steps": [
              {
                "color": "#299c46",
                "value": null
              },
              {
                "color": "dark-orange",
                "value": 1
              }
            ]
          }
        },
        "overrides": []
      },
      "gridPos": {
        "h": 2,
        "w": 2,
        "x": 6,
        "y": 2
      },
      "id": 1614,
      "options": {
        "colorMode": "value",
        "graphMode": "none",
        "justifyMode": "auto",
        "orientation": "auto",
        "reduceOptions": {
          "calcs": [
            "lastNotNull"
          ],
          "fields": "",
          "values": false
        },
        "text": {},
        "textMode": "auto"
      },
      "pluginVersion": "9.0.5",
      "targets": [
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${DS_PROMETHEUS}"
          },
          "exemplar": true,
          "expr": "hrDeviceErrors{instance='$instance', hrDeviceIndex=\"1\"}",
          "hide": false,
          "instant": true,
          "interval": "",
          "legendFormat": "",
          "refId": "A"
        }
      ],
      "title": "Device Errors",
      "type": "stat"
    },
    {
      "datasource": {
        "type": "prometheus",
        "uid": "${DS_PROMETHEUS}"
      },
      "description": "",
      "fieldConfig": {
        "defaults": {
          "color": {
            "mode": "thresholds"
          },
          "mappings": [],
          "thresholds": {
            "mode": "absolute",
            "steps": [
              {
                "color": "#fff899",
                "value": null
              }
            ]
          }
        },
        "overrides": []
      },
      "gridPos": {
        "h": 2,
        "w": 4,
        "x": 8,
        "y": 2
      },
      "id": 1264,
      "options": {
        "colorMode": "value",
        "graphMode": "none",
        "justifyMode": "auto",
        "orientation": "auto",
        "reduceOptions": {
          "calcs": [
            "lastNotNull"
          ],
          "fields": "",
          "values": false
        },
        "text": {},
        "textMode": "name"
      },
      "pluginVersion": "9.0.5",
      "targets": [
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${DS_PROMETHEUS}"
          },
          "exemplar": true,
          "expr": "sysIdentity{instance='$instance'}",
          "hide": false,
          "instant": true,
          "interval": "",
          "legendFormat": "{{sysIdentity}}",
          "refId": "A"
        }
      ],
      "title": "System identity",
      "type": "stat"
    },
    {
      "datasource": {
        "type": "prometheus",
        "uid": "${DS_PROMETHEUS}"
      },
      "description": "",
      "fieldConfig": {
        "defaults": {
          "color": {
            "mode": "thresholds"
          },
          "mappings": [],
          "thresholds": {
            "mode": "absolute",
            "steps": [
              {
                "color": "#fff899",
                "value": null
              }
            ]
          }
        },
        "overrides": []
      },
      "gridPos": {
        "h": 2,
        "w": 4,
        "x": 12,
        "y": 2
      },
      "id": 1311,
      "options": {
        "colorMode": "value",
        "graphMode": "none",
        "justifyMode": "auto",
        "orientation": "auto",
        "reduceOptions": {
          "calcs": [
            "lastNotNull"
          ],
          "fields": "",
          "values": false
        },
        "text": {},
        "textMode": "name"
      },
      "pluginVersion": "9.0.5",
      "targets": [
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${DS_PROMETHEUS}"
          },
          "exemplar": true,
          "expr": "mtxrSerialNumber{instance='$instance'}",
          "hide": false,
          "instant": false,
          "interval": "",
          "legendFormat": "{{mtxrSerialNumber}}",
          "refId": "A"
        }
      ],
      "title": "Serial Number",
      "type": "stat"
    },
    {
      "datasource": {
        "type": "prometheus",
        "uid": "${DS_PROMETHEUS}"
      },
      "description": "",
      "fieldConfig": {
        "defaults": {
          "color": {
            "mode": "thresholds"
          },
          "mappings": [],
          "thresholds": {
            "mode": "absolute",
            "steps": [
              {
                "color": "super-light-yellow",
                "value": null
              }
            ]
          }
        },
        "overrides": []
      },
      "gridPos": {
        "h": 2,
        "w": 8,
        "x": 16,
        "y": 2
      },
      "id": 1241,
      "options": {
        "colorMode": "value",
        "graphMode": "none",
        "justifyMode": "auto",
        "orientation": "auto",
        "reduceOptions": {
          "calcs": [
            "lastNotNull"
          ],
          "fields": "",
          "values": false
        },
        "text": {},
        "textMode": "name"
      },
      "pluginVersion": "9.0.5",
      "targets": [
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${DS_PROMETHEUS}"
          },
          "exemplar": true,
          "expr": "sysDescr{instance='$instance'}",
          "hide": false,
          "instant": true,
          "interval": "",
          "legendFormat": "{{sysDescr}}",
          "refId": "A"
        }
      ],
      "title": "Model",
      "type": "stat"
    },
    {
      "datasource": {
        "type": "prometheus",
        "uid": "${DS_PROMETHEUS}"
      },
      "description": "",
      "fieldConfig": {
        "defaults": {
          "color": {
            "mode": "thresholds"
          },
          "mappings": [],
          "thresholds": {
            "mode": "absolute",
            "steps": [
              {
                "color": "#299c46",
                "value": null
              }
            ]
          },
          "unit": "dateTimeAsLocal"
        },
        "overrides": []
      },
      "gridPos": {
        "h": 2,
        "w": 4,
        "x": 0,
        "y": 4
      },
      "id": 1325,
      "links": [],
      "maxDataPoints": 100,
      "options": {
        "colorMode": "value",
        "graphMode": "area",
        "justifyMode": "center",
        "orientation": "auto",
        "reduceOptions": {
          "calcs": [
            "lastNotNull"
          ],
          "fields": "/^Time$/",
          "values": false
        },
        "text": {},
        "textMode": "auto"
      },
      "pluginVersion": "9.0.5",
      "targets": [
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${DS_PROMETHEUS}"
          },
          "exemplar": true,
          "expr": "time()-(hrSystemDate{instance='$instance'})",
          "instant": true,
          "interval": "",
          "legendFormat": "",
          "refId": "A"
        }
      ],
      "title": "System date",
      "type": "stat"
    },
    {
      "datasource": {
        "type": "prometheus",
        "uid": "${DS_PROMETHEUS}"
      },
      "fieldConfig": {
        "defaults": {
          "color": {
            "mode": "thresholds"
          },
          "mappings": [],
          "thresholds": {
            "mode": "absolute",
            "steps": [
              {
                "color": "#299c46",
                "value": null
              }
            ]
          }
        },
        "overrides": []
      },
      "gridPos": {
        "h": 2,
        "w": 2,
        "x": 4,
        "y": 4
      },
      "id": 1222,
      "options": {
        "colorMode": "value",
        "graphMode": "none",
        "justifyMode": "auto",
        "orientation": "auto",
        "reduceOptions": {
          "calcs": [
            "last"
          ],
          "fields": "",
          "values": false
        },
        "text": {},
        "textMode": "name"
      },
      "pluginVersion": "9.0.5",
      "targets": [
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${DS_PROMETHEUS}"
          },
          "exemplar": true,
          "expr": "mtxrFirmwareVersion{instance='$instance'}",
          "format": "time_series",
          "hide": false,
          "instant": true,
          "interval": "",
          "legendFormat": "{{mtxrFirmwareVersion}}",
          "refId": "A"
        }
      ],
      "title": "Board ver",
      "type": "stat"
    },
    {
      "datasource": {
        "type": "prometheus",
        "uid": "${DS_PROMETHEUS}"
      },
      "description": "",
      "fieldConfig": {
        "defaults": {
          "color": {
            "mode": "thresholds"
          },
          "mappings": [],
          "thresholds": {
            "mode": "absolute",
            "steps": [
              {
                "color": "#299c46",
                "value": null
              }
            ]
          }
        },
        "overrides": []
      },
      "gridPos": {
        "h": 2,
        "w": 2,
        "x": 6,
        "y": 4
      },
      "id": 1650,
      "options": {
        "colorMode": "value",
        "graphMode": "none",
        "justifyMode": "auto",
        "orientation": "auto",
        "reduceOptions": {
          "calcs": [
            "last"
          ],
          "fields": "",
          "values": false
        },
        "text": {},
        "textMode": "name"
      },
      "pluginVersion": "9.0.5",
      "targets": [
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${DS_PROMETHEUS}"
          },
          "exemplar": true,
          "expr": "mtxrLicVersion{instance='$instance'}",
          "format": "time_series",
          "hide": false,
          "instant": true,
          "interval": "",
          "legendFormat": "{{mtxrLicVersion}}",
          "refId": "A"
        }
      ],
      "title": "Package ver",
      "type": "stat"
    },
    {
      "datasource": {
        "type": "prometheus",
        "uid": "${DS_PROMETHEUS}"
      },
      "description": "",
      "fieldConfig": {
        "defaults": {
          "color": {
            "mode": "thresholds"
          },
          "mappings": [],
          "thresholds": {
            "mode": "absolute",
            "steps": [
              {
                "color": "super-light-yellow",
                "value": null
              }
            ]
          }
        },
        "overrides": []
      },
      "gridPos": {
        "h": 2,
        "w": 4,
        "x": 8,
        "y": 4
      },
      "id": 1248,
      "options": {
        "colorMode": "value",
        "graphMode": "none",
        "justifyMode": "auto",
        "orientation": "auto",
        "reduceOptions": {
          "calcs": [
            "lastNotNull"
          ],
          "fields": "",
          "values": false
        },
        "text": {},
        "textMode": "name"
      },
      "pluginVersion": "9.0.5",
      "targets": [
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${DS_PROMETHEUS}"
          },
          "exemplar": true,
          "expr": "mtxrBoardName{instance='$instance'}",
          "hide": false,
          "instant": true,
          "interval": "",
          "legendFormat": "{{mtxrBoardName}}",
          "refId": "A"
        }
      ],
      "title": "Board Name",
      "type": "stat"
    },
    {
      "datasource": {
        "type": "prometheus",
        "uid": "${DS_PROMETHEUS}"
      },
      "description": "",
      "fieldConfig": {
        "defaults": {
          "color": {
            "mode": "thresholds"
          },
          "mappings": [],
          "thresholds": {
            "mode": "absolute",
            "steps": [
              {
                "color": "super-light-yellow",
                "value": null
              }
            ]
          }
        },
        "overrides": []
      },
      "gridPos": {
        "h": 2,
        "w": 4,
        "x": 12,
        "y": 4
      },
      "id": 1649,
      "options": {
        "colorMode": "value",
        "graphMode": "none",
        "justifyMode": "auto",
        "orientation": "auto",
        "reduceOptions": {
          "calcs": [
            "lastNotNull"
          ],
          "fields": "",
          "values": false
        },
        "text": {},
        "textMode": "name"
      },
      "pluginVersion": "9.0.5",
      "targets": [
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${DS_PROMETHEUS}"
          },
          "exemplar": true,
          "expr": "mtxrLicSoftwareId{instance='$instance'}",
          "hide": false,
          "instant": false,
          "interval": "",
          "legendFormat": "{{mtxrLicSoftwareId}}",
          "refId": "A"
        }
      ],
      "title": "Software ID",
      "type": "stat"
    },
    {
      "datasource": {
        "type": "prometheus",
        "uid": "${DS_PROMETHEUS}"
      },
      "description": "",
      "fieldConfig": {
        "defaults": {
          "color": {
            "mode": "thresholds"
          },
          "mappings": [
            {
              "options": {
                "": {
                  "index": 0,
                  "text": "N/A"
                }
              },
              "type": "value"
            }
          ],
          "thresholds": {
            "mode": "absolute",
            "steps": [
              {
                "color": "#299c46",
                "value": null
              }
            ]
          },
          "unit": "string"
        },
        "overrides": []
      },
      "gridPos": {
        "h": 2,
        "w": 8,
        "x": 16,
        "y": 4
      },
      "id": 1653,
      "links": [],
      "maxDataPoints": 100,
      "options": {
        "colorMode": "value",
        "graphMode": "none",
        "justifyMode": "center",
        "orientation": "auto",
        "reduceOptions": {
          "calcs": [
            "last"
          ],
          "fields": "",
          "values": false
        },
        "text": {},
        "textMode": "name"
      },
      "pluginVersion": "9.0.5",
      "targets": [
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${DS_PROMETHEUS}"
          },
          "exemplar": true,
          "expr": "mtxrNote{instance='$instance'}",
          "instant": true,
          "interval": "",
          "legendFormat": " {{mtxrNote}}",
          "refId": "A"
        }
      ],
      "title": "Note",
      "type": "stat"
    },
    {
      "datasource": {
        "type": "prometheus",
        "uid": "${DS_PROMETHEUS}"
      },
      "fieldConfig": {
        "defaults": {
          "color": {
            "mode": "thresholds"
          },
          "decimals": 1,
          "mappings": [],
          "max": 100,
          "min": 1,
          "thresholds": {
            "mode": "percentage",
            "steps": [
              {
                "color": "#299c46",
                "value": null
              },
              {
                "color": "dark-orange",
                "value": 80
              },
              {
                "color": "dark-red",
                "value": 90
              }
            ]
          },
          "unit": "percent"
        },
        "overrides": []
      },
      "gridPos": {
        "h": 5,
        "w": 4,
        "x": 0,
        "y": 6
      },
      "id": 1703,
      "options": {
        "orientation": "auto",
        "reduceOptions": {
          "calcs": [
            "lastNotNull"
          ],
          "fields": "",
          "values": false
        },
        "showThresholdLabels": true,
        "showThresholdMarkers": true,
        "text": {}
      },
      "pluginVersion": "9.0.5",
      "targets": [
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${DS_PROMETHEUS}"
          },
          "exemplar": true,
          "expr": "avg(hrProcessorLoad{instance='$instance'})",
          "instant": true,
          "interval": "",
          "legendFormat": "",
          "refId": "A"
        }
      ],
      "title": "CPU Load",
      "type": "gauge"
    },
    {
      "datasource": {
        "type": "prometheus",
        "uid": "${DS_PROMETHEUS}"
      },
      "fieldConfig": {
        "defaults": {
          "color": {
            "mode": "thresholds"
          },
          "decimals": 1,
          "mappings": [
            {
              "options": {
                "match": "null",
                "result": {
                  "text": "N/A"
                }
              },
              "type": "special"
            }
          ],
          "max": 100,
          "min": 0,
          "thresholds": {
            "mode": "percentage",
            "steps": [
              {
                "color": "#299c46",
                "value": null
              },
              {
                "color": "dark-orange",
                "value": 60
              },
              {
                "color": "dark-red",
                "value": 80
              }
            ]
          },
          "unit": "percent"
        },
        "overrides": []
      },
      "gridPos": {
        "h": 5,
        "w": 4,
        "x": 4,
        "y": 6
      },
      "id": 482,
      "links": [],
      "maxDataPoints": 100,
      "options": {
        "orientation": "horizontal",
        "reduceOptions": {
          "calcs": [
            "mean"
          ],
          "fields": "",
          "values": false
        },
        "showThresholdLabels": true,
        "showThresholdMarkers": true,
        "text": {}
      },
      "pluginVersion": "9.0.5",
      "targets": [
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${DS_PROMETHEUS}"
          },
          "exemplar": true,
          "expr": "(hrStorageUsed{hrStorageIndex='65536',instance='$instance'} * 100 )/(hrStorageSize{hrStorageIndex='65536',instance='$instance'})",
          "instant": true,
          "interval": "",
          "legendFormat": "",
          "refId": "A"
        }
      ],
      "title": "RAM load ",
      "type": "gauge"
    },
    {
      "datasource": {
        "type": "prometheus",
        "uid": "${DS_PROMETHEUS}"
      },
      "fieldConfig": {
        "defaults": {
          "color": {
            "mode": "thresholds"
          },
          "decimals": 1,
          "mappings": [
            {
              "options": {
                "match": "null",
                "result": {
                  "text": "N/A"
                }
              },
              "type": "special"
            }
          ],
          "max": 100,
          "min": 0,
          "thresholds": {
            "mode": "absolute",
            "steps": [
              {
                "color": "#299c46",
                "value": null
              },
              {
                "color": "dark-orange",
                "value": 80
              },
              {
                "color": "dark-red",
                "value": 90
              }
            ]
          },
          "unit": "percent"
        },
        "overrides": []
      },
      "gridPos": {
        "h": 5,
        "w": 4,
        "x": 8,
        "y": 6
      },
      "id": 480,
      "links": [],
      "maxDataPoints": 100,
      "options": {
        "orientation": "horizontal",
        "reduceOptions": {
          "calcs": [
            "mean"
          ],
          "fields": "",
          "values": false
        },
        "showThresholdLabels": true,
        "showThresholdMarkers": true,
        "text": {}
      },
      "pluginVersion": "9.0.5",
      "targets": [
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${DS_PROMETHEUS}"
          },
          "exemplar": true,
          "expr": "(hrStorageUsed{hrStorageIndex='131072',instance='$instance'} * 100 )/(hrStorageSize{hrStorageIndex='131072',instance='$instance'})",
          "instant": true,
          "interval": "",
          "legendFormat": "",
          "refId": "A"
        }
      ],
      "title": "system disk load",
      "type": "gauge"
    },
    {
      "datasource": {
        "type": "prometheus",
        "uid": "${DS_PROMETHEUS}"
      },
      "description": "",
      "fieldConfig": {
        "defaults": {
          "color": {
            "mode": "thresholds"
          },
          "decimals": 1,
          "mappings": [],
          "max": 80,
          "min": 1,
          "noValue": "N/A",
          "thresholds": {
            "mode": "absolute",
            "steps": [
              {
                "color": "light-blue",
                "value": null
              },
              {
                "color": "#299c46",
                "value": 20
              },
              {
                "color": "dark-orange",
                "value": 55
              },
              {
                "color": "dark-red",
                "value": 65
              }
            ]
          },
          "unit": "celsius"
        },
        "overrides": []
      },
      "gridPos": {
        "h": 5,
        "w": 4,
        "x": 12,
        "y": 6
      },
      "id": 1237,
      "options": {
        "orientation": "auto",
        "reduceOptions": {
          "calcs": [
            "lastNotNull"
          ],
          "fields": "",
          "values": false
        },
        "showThresholdLabels": true,
        "showThresholdMarkers": true,
        "text": {}
      },
      "pluginVersion": "9.0.5",
      "targets": [
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${DS_PROMETHEUS}"
          },
          "exemplar": true,
          "expr": "mtxrHlProcessorTemperature{instance='$instance'}/10 or mtxrHlTemperature{instance='$instance'}/10",
          "instant": true,
          "interval": "",
          "legendFormat": "",
          "refId": "A"
        }
      ],
      "title": "CPU Temp",
      "type": "gauge"
    },
    {
      "datasource": {
        "type": "prometheus",
        "uid": "${DS_PROMETHEUS}"
      },
      "description": "",
      "fieldConfig": {
        "defaults": {
          "color": {
            "mode": "palette-classic"
          },
          "custom": {
            "axisLabel": "",
            "axisPlacement": "auto",
            "barAlignment": 0,
            "drawStyle": "line",
            "fillOpacity": 30,
            "gradientMode": "opacity",
            "hideFrom": {
              "legend": false,
              "tooltip": false,
              "viz": false
            },
            "lineInterpolation": "smooth",
            "lineStyle": {
              "fill": "solid"
            },
            "lineWidth": 2,
            "pointSize": 5,
            "scaleDistribution": {
              "type": "linear"
            },
            "showPoints": "never",
            "spanNulls": true,
            "stacking": {
              "group": "A",
              "mode": "none"
            },
            "thresholdsStyle": {
              "mode": "line"
            }
          },
          "mappings": [],
          "thresholds": {
            "mode": "absolute",
            "steps": [
              {
                "color": "green",
                "value": null
              }
            ]
          },
          "unit": "percent"
        },
        "overrides": []
      },
      "gridPos": {
        "h": 13,
        "w": 8,
        "x": 16,
        "y": 6
      },
      "id": 1262,
      "links": [],
      "maxDataPoints": 100,
      "options": {
        "legend": {
          "calcs": [],
          "displayMode": "list",
          "placement": "bottom"
        },
        "tooltip": {
          "mode": "multi",
          "sort": "none"
        }
      },
      "pluginVersion": "8.2.1",
      "repeatDirection": "h",
      "targets": [
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${DS_PROMETHEUS}"
          },
          "exemplar": true,
          "expr": "hrProcessorLoad{instance='$instance'}",
          "interval": "",
          "legendFormat": "CPU {{hrDeviceIndex}}  load",
          "refId": "A"
        },
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${DS_PROMETHEUS}"
          },
          "exemplar": true,
          "expr": "mtxrHlTemperature{instance='$instance'}/10",
          "format": "time_series",
          "hide": false,
          "instant": false,
          "interval": "",
          "legendFormat": "CPU temp",
          "refId": "B"
        },
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${DS_PROMETHEUS}"
          },
          "exemplar": true,
          "expr": "(hrStorageUsed{hrStorageIndex='65536',instance='$instance'} * 100 )/(hrStorageSize{hrStorageIndex='65536',instance='$instance'})",
          "hide": false,
          "interval": "",
          "legendFormat": "RAM usage",
          "refId": "C"
        },
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${DS_PROMETHEUS}"
          },
          "exemplar": true,
          "expr": "(hrStorageUsed{hrStorageIndex='131072',instance='$instance'} * 100 )/(hrStorageSize{hrStorageIndex='131072',instance='$instance'})",
          "hide": false,
          "interval": "",
          "legendFormat": "System disk",
          "refId": "D"
        },
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${DS_PROMETHEUS}"
          },
          "exemplar": true,
          "expr": "mtxrHlVoltage{instance='$instance'}/10",
          "hide": false,
          "interval": "",
          "legendFormat": "Voltage",
          "refId": "E"
        }
      ],
      "title": "System",
      "type": "timeseries"
    },
    {
      "datasource": {
        "type": "prometheus",
        "uid": "${DS_PROMETHEUS}"
      },
      "description": "",
      "fieldConfig": {
        "defaults": {
          "color": {
            "mode": "thresholds"
          },
          "mappings": [],
          "thresholds": {
            "mode": "absolute",
            "steps": [
              {
                "color": "#299c46",
                "value": null
              }
            ]
          },
          "unit": "MHz"
        },
        "overrides": []
      },
      "gridPos": {
        "h": 4,
        "w": 4,
        "x": 0,
        "y": 11
      },
      "id": 1240,
      "options": {
        "colorMode": "value",
        "graphMode": "none",
        "justifyMode": "auto",
        "orientation": "auto",
        "reduceOptions": {
          "calcs": [
            "lastNotNull"
          ],
          "fields": "",
          "values": false
        },
        "text": {},
        "textMode": "auto"
      },
      "pluginVersion": "9.0.5",
      "targets": [
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${DS_PROMETHEUS}"
          },
          "exemplar": true,
          "expr": "mtxrHlProcessorFrequency{instance='$instance'}",
          "hide": false,
          "instant": true,
          "interval": "",
          "legendFormat": "",
          "refId": "A"
        }
      ],
      "title": "CPU frequency",
      "type": "stat"
    },
    {
      "datasource": {
        "type": "prometheus",
        "uid": "${DS_PROMETHEUS}"
      },
      "description": "",
      "fieldConfig": {
        "defaults": {
          "color": {
            "mode": "thresholds"
          },
          "mappings": [],
          "thresholds": {
            "mode": "absolute",
            "steps": [
              {
                "color": "#299c46",
                "value": null
              }
            ]
          }
        },
        "overrides": []
      },
      "gridPos": {
        "h": 4,
        "w": 4,
        "x": 4,
        "y": 11
      },
      "id": 1242,
      "options": {
        "colorMode": "value",
        "graphMode": "none",
        "justifyMode": "auto",
        "orientation": "auto",
        "reduceOptions": {
          "calcs": [
            "last"
          ],
          "fields": "/^n/a$/",
          "values": false
        },
        "text": {},
        "textMode": "name"
      },
      "pluginVersion": "9.0.5",
      "targets": [
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${DS_PROMETHEUS}"
          },
          "exemplar": true,
          "expr": "mtxrHlActiveFan{instance='$instance'}",
          "hide": false,
          "instant": true,
          "interval": "",
          "legendFormat": "{{mtxrHlActiveFan}}",
          "refId": "A"
        }
      ],
      "title": "Active Fan",
      "type": "stat"
    },
    {
      "datasource": {
        "type": "prometheus",
        "uid": "${DS_PROMETHEUS}"
      },
      "description": "Wireless registration table entry count",
      "fieldConfig": {
        "defaults": {
          "color": {
            "mode": "thresholds"
          },
          "mappings": [],
          "thresholds": {
            "mode": "absolute",
            "steps": [
              {
                "color": "#299c46",
                "value": null
              }
            ]
          }
        },
        "overrides": []
      },
      "gridPos": {
        "h": 4,
        "w": 4,
        "x": 8,
        "y": 11
      },
      "id": 1645,
      "options": {
        "colorMode": "value",
        "graphMode": "none",
        "justifyMode": "auto",
        "orientation": "auto",
        "reduceOptions": {
          "calcs": [
            "lastNotNull"
          ],
          "fields": "",
          "values": false
        },
        "text": {},
        "textMode": "auto"
      },
      "pluginVersion": "9.0.5",
      "targets": [
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${DS_PROMETHEUS}"
          },
          "exemplar": true,
          "expr": "mtxrWlRtabEntryCount{instance='$instance'}",
          "format": "time_series",
          "hide": false,
          "instant": true,
          "interval": "",
          "legendFormat": "",
          "refId": "A"
        }
      ],
      "title": "Wi-Fi client count",
      "type": "stat"
    },
    {
      "datasource": {
        "type": "prometheus",
        "uid": "${DS_PROMETHEUS}"
      },
      "description": "",
      "fieldConfig": {
        "defaults": {
          "color": {
            "mode": "thresholds"
          },
          "mappings": [
            {
              "options": {
                "result": {
                  "text": ""
                },
                "to": 0
              },
              "type": "range"
            }
          ],
          "thresholds": {
            "mode": "absolute",
            "steps": [
              {
                "color": "#299c46",
                "value": null
              },
              {
                "color": "red",
                "value": 80
              }
            ]
          },
          "unit": "none"
        },
        "overrides": []
      },
      "gridPos": {
        "h": 4,
        "w": 4,
        "x": 12,
        "y": 11
      },
      "id": 1260,
      "links": [],
      "maxDataPoints": 100,
      "options": {
        "colorMode": "value",
        "graphMode": "none",
        "justifyMode": "center",
        "orientation": "auto",
        "reduceOptions": {
          "calcs": [
            "lastNotNull"
          ],
          "fields": "",
          "values": false
        },
        "text": {},
        "textMode": "value_and_name"
      },
      "pluginVersion": "9.0.5",
      "targets": [
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${DS_PROMETHEUS}"
          },
          "exemplar": true,
          "expr": "mtxrLicLevel{instance='$instance'}",
          "interval": "",
          "legendFormat": "Lic",
          "refId": "A"
        },
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${DS_PROMETHEUS}"
          },
          "exemplar": true,
          "expr": "mtxrLicUpgradableTo{instance='$instance'}",
          "hide": false,
          "interval": "",
          "legendFormat": "Upgradable to",
          "refId": "B"
        }
      ],
      "title": "License level",
      "type": "stat"
    },
    {
      "datasource": {
        "type": "prometheus",
        "uid": "${DS_PROMETHEUS}"
      },
      "fieldConfig": {
        "defaults": {
          "color": {
            "mode": "thresholds"
          },
          "mappings": [
            {
              "options": {
                "1": {
                  "text": "Disabled"
                },
                "2": {
                  "text": "Waiting"
                },
                "3": {
                  "text": "Powered On"
                },
                "4": {
                  "text": "Overload"
                }
              },
              "type": "value"
            }
          ],
          "max": 4,
          "min": 1,
          "thresholds": {
            "mode": "absolute",
            "steps": [
              {
                "color": "blue",
                "value": null
              },
              {
                "color": "dark-yellow",
                "value": 2
              },
              {
                "color": "#299c46",
                "value": 3
              },
              {
                "color": "dark-red",
                "value": 4
              }
            ]
          }
        },
        "overrides": []
      },
      "gridPos": {
        "h": 4,
        "w": 4,
        "x": 0,
        "y": 15
      },
      "id": 1276,
      "options": {
        "colorMode": "value",
        "graphMode": "none",
        "justifyMode": "center",
        "orientation": "auto",
        "reduceOptions": {
          "calcs": [
            "lastNotNull"
          ],
          "fields": "",
          "values": false
        },
        "text": {},
        "textMode": "value"
      },
      "pluginVersion": "9.0.5",
      "targets": [
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${DS_PROMETHEUS}"
          },
          "exemplar": true,
          "expr": "mtxrPOEStatus{instance='$instance'}",
          "format": "time_series",
          "hide": false,
          "instant": true,
          "interval": "",
          "legendFormat": "",
          "refId": "A"
        }
      ],
      "title": "POE Status",
      "type": "stat"
    },
    {
      "datasource": {
        "type": "prometheus",
        "uid": "${DS_PROMETHEUS}"
      },
      "description": "",
      "fieldConfig": {
        "defaults": {
          "color": {
            "mode": "thresholds"
          },
          "mappings": [],
          "thresholds": {
            "mode": "absolute",
            "steps": [
              {
                "color": "#299c46",
                "value": null
              }
            ]
          },
          "unit": "watt"
        },
        "overrides": []
      },
      "gridPos": {
        "h": 4,
        "w": 4,
        "x": 4,
        "y": 15
      },
      "id": 1279,
      "options": {
        "colorMode": "value",
        "graphMode": "none",
        "justifyMode": "center",
        "orientation": "auto",
        "reduceOptions": {
          "calcs": [
            "lastNotNull"
          ],
          "fields": "",
          "values": false
        },
        "text": {},
        "textMode": "auto"
      },
      "pluginVersion": "9.0.5",
      "targets": [
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${DS_PROMETHEUS}"
          },
          "exemplar": true,
          "expr": "mtxrPOEPower{instance='$instance'}",
          "format": "time_series",
          "hide": false,
          "instant": true,
          "interval": "",
          "legendFormat": "POE Power",
          "refId": "A"
        }
      ],
      "title": "POE Power",
      "type": "stat"
    },
    {
      "datasource": {
        "type": "prometheus",
        "uid": "${DS_PROMETHEUS}"
      },
      "fieldConfig": {
        "defaults": {
          "color": {
            "mode": "thresholds"
          },
          "mappings": [],
          "thresholds": {
            "mode": "absolute",
            "steps": [
              {
                "color": "#299c46",
                "value": null
              }
            ]
          },
          "unit": "mamp"
        },
        "overrides": []
      },
      "gridPos": {
        "h": 4,
        "w": 4,
        "x": 8,
        "y": 15
      },
      "id": 1277,
      "options": {
        "colorMode": "value",
        "graphMode": "none",
        "justifyMode": "center",
        "orientation": "auto",
        "reduceOptions": {
          "calcs": [
            "lastNotNull"
          ],
          "fields": "",
          "values": false
        },
        "text": {},
        "textMode": "value"
      },
      "pluginVersion": "9.0.5",
      "targets": [
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${DS_PROMETHEUS}"
          },
          "exemplar": true,
          "expr": "mtxrPOECurrent{instance='$instance'}",
          "format": "time_series",
          "hide": false,
          "instant": true,
          "interval": "",
          "legendFormat": "POE Current",
          "refId": "A"
        }
      ],
      "title": "POE Current",
      "type": "stat"
    },
    {
      "datasource": {
        "type": "prometheus",
        "uid": "${DS_PROMETHEUS}"
      },
      "fieldConfig": {
        "defaults": {
          "color": {
            "mode": "thresholds"
          },
          "mappings": [],
          "thresholds": {
            "mode": "absolute",
            "steps": [
              {
                "color": "#299c46",
                "value": null
              }
            ]
          },
          "unit": "volt"
        },
        "overrides": []
      },
      "gridPos": {
        "h": 4,
        "w": 4,
        "x": 12,
        "y": 15
      },
      "id": 1278,
      "options": {
        "colorMode": "value",
        "graphMode": "none",
        "justifyMode": "center",
        "orientation": "auto",
        "reduceOptions": {
          "calcs": [
            "lastNotNull"
          ],
          "fields": "",
          "values": false
        },
        "text": {},
        "textMode": "auto"
      },
      "pluginVersion": "9.0.5",
      "targets": [
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${DS_PROMETHEUS}"
          },
          "exemplar": true,
          "expr": "mtxrPOEVoltage{instance='$instance'}",
          "format": "time_series",
          "hide": false,
          "instant": true,
          "interval": "",
          "legendFormat": "POE Voltage",
          "refId": "A"
        }
      ],
      "title": "POE Voltage",
      "type": "stat"
    },
    {
      "datasource": {
        "type": "prometheus",
        "uid": "${DS_PROMETHEUS}"
      },
      "description": "",
      "fieldConfig": {
        "defaults": {
          "color": {
            "mode": "palette-classic"
          },
          "custom": {
            "axisLabel": "",
            "axisPlacement": "auto",
            "barAlignment": 0,
            "drawStyle": "line",
            "fillOpacity": 10,
            "gradientMode": "hue",
            "hideFrom": {
              "legend": false,
              "tooltip": false,
              "viz": false
            },
            "lineInterpolation": "smooth",
            "lineWidth": 2,
            "pointSize": 5,
            "scaleDistribution": {
              "type": "linear"
            },
            "showPoints": "never",
            "spanNulls": false,
            "stacking": {
              "group": "A",
              "mode": "none"
            },
            "thresholdsStyle": {
              "mode": "off"
            }
          },
          "mappings": [],
          "thresholds": {
            "mode": "absolute",
            "steps": [
              {
                "color": "green",
                "value": null
              }
            ]
          },
          "unit": "bps"
        },
        "overrides": []
      },
      "gridPos": {
        "h": 8,
        "w": 24,
        "x": 0,
        "y": 19
      },
      "id": 1239,
      "options": {
        "legend": {
          "calcs": [
            "mean",
            "lastNotNull",
            "max"
          ],
          "displayMode": "table",
          "placement": "right"
        },
        "tooltip": {
          "mode": "multi",
          "sort": "none"
        }
      },
      "pluginVersion": "8.2.1",
      "targets": [
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${DS_PROMETHEUS}"
          },
          "exemplar": true,
          "expr": "irate(ifHCInOctets{ifName=~'$Interface',instance='$instance'}[$__rate_interval])*8",
          "format": "time_series",
          "hide": false,
          "interval": "",
          "intervalFactor": 1,
          "legendFormat": "In - {{ifName}}",
          "refId": "C"
        },
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${DS_PROMETHEUS}"
          },
          "exemplar": true,
          "expr": "-irate(ifHCOutOctets{ifName=~'$Interface',instance='$instance'}[$__rate_interval])*8",
          "hide": false,
          "interval": "",
          "intervalFactor": 1,
          "legendFormat": "Out - {{ifName}}",
          "refId": "A"
        }
      ],
      "title": "Network Traffic Basic",
      "type": "timeseries"
    },
    {
      "datasource": {
        "type": "prometheus",
        "uid": "${DS_PROMETHEUS}"
      },
      "description": "Status link/states: The current operational state of the interface",
      "fieldConfig": {
        "defaults": {
          "color": {
            "mode": "thresholds"
          },
          "custom": {
            "align": "auto",
            "displayMode": "color-text",
            "filterable": false,
            "inspect": false
          },
          "mappings": [],
          "thresholds": {
            "mode": "absolute",
            "steps": [
              {
                "color": "super-light-yellow",
                "value": null
              }
            ]
          },
          "unit": "short"
        },
        "overrides": [
          {
            "matcher": {
              "id": "byType",
              "options": "string"
            },
            "properties": [
              {
                "id": "custom.align",
                "value": "center"
              }
            ]
          },
          {
            "matcher": {
              "id": "byType",
              "options": "number"
            },
            "properties": [
              {
                "id": "custom.align",
                "value": "center"
              }
            ]
          },
          {
            "matcher": {
              "id": "byName",
              "options": "Status link/states"
            },
            "properties": [
              {
                "id": "thresholds",
                "value": {
                  "mode": "absolute",
                  "steps": [
                    {
                      "color": "green",
                      "value": null
                    },
                    {
                      "color": "#299c46",
                      "value": 1
                    },
                    {
                      "color": "semi-dark-red",
                      "value": 2
                    },
                    {
                      "color": "#EAB839",
                      "value": 3
                    },
                    {
                      "color": "#6a6a6a",
                      "value": 4
                    },
                    {
                      "color": "#6ED0E0",
                      "value": 5
                    },
                    {
                      "color": "#EF843C",
                      "value": 6
                    },
                    {
                      "color": "dark-purple",
                      "value": 7
                    }
                  ]
                }
              },
              {
                "id": "mappings",
                "value": [
                  {
                    "options": {
                      "1": {
                        "index": 6,
                        "text": "UP"
                      },
                      "2": {
                        "index": 5,
                        "text": "DOWN"
                      },
                      "3": {
                        "index": 4,
                        "text": "Testing"
                      },
                      "4": {
                        "index": 3,
                        "text": "Unknown"
                      },
                      "5": {
                        "index": 2,
                        "text": "Dormant"
                      },
                      "6": {
                        "index": 1,
                        "text": "Not present"
                      },
                      "7": {
                        "index": 0,
                        "text": "lowerLayerDown"
                      }
                    },
                    "type": "value"
                  }
                ]
              },
              {
                "id": "custom.width",
                "value": 130
              },
              {
                "id": "custom.displayMode",
                "value": "color-background"
              }
            ]
          },
          {
            "matcher": {
              "id": "byName",
              "options": "Rate"
            },
            "properties": [
              {
                "id": "unit",
                "value": "bps"
              },
              {
                "id": "thresholds",
                "value": {
                  "mode": "absolute",
                  "steps": [
                    {
                      "color": "rgb(77, 79, 79)",
                      "value": null
                    },
                    {
                      "color": "#EAB839",
                      "value": 50000000
                    },
                    {
                      "color": "#6ED0E0",
                      "value": 100000000
                    },
                    {
                      "color": "#299c46",
                      "value": 1000000000
                    },
                    {
                      "color": "semi-dark-purple",
                      "value": 1000000010
                    }
                  ]
                }
              },
              {
                "id": "custom.width",
                "value": 119
              }
            ]
          },
          {
            "matcher": {
              "id": "byName",
              "options": "TX Sum"
            },
            "properties": [
              {
                "id": "unit",
                "value": "bytes"
              },
              {
                "id": "thresholds",
                "value": {
                  "mode": "absolute",
                  "steps": [
                    {
                      "color": "rgb(77, 79, 79)",
                      "value": null
                    },
                    {
                      "color": "super-light-yellow",
                      "value": 1
                    }
                  ]
                }
              },
              {
                "id": "custom.width",
                "value": 118
              }
            ]
          },
          {
            "matcher": {
              "id": "byName",
              "options": "RX Sum"
            },
            "properties": [
              {
                "id": "unit",
                "value": "bytes"
              },
              {
                "id": "thresholds",
                "value": {
                  "mode": "absolute",
                  "steps": [
                    {
                      "color": "rgb(77, 79, 79)",
                      "value": null
                    },
                    {
                      "color": "super-light-yellow",
                      "value": 1
                    }
                  ]
                }
              },
              {
                "id": "custom.width",
                "value": 118
              }
            ]
          },
          {
            "matcher": {
              "id": "byName",
              "options": "MAC"
            },
            "properties": [
              {
                "id": "custom.width",
                "value": 152
              }
            ]
          },
          {
            "matcher": {
              "id": "byName",
              "options": "Link down count"
            },
            "properties": [
              {
                "id": "custom.width",
                "value": 118
              },
              {
                "id": "thresholds",
                "value": {
                  "mode": "absolute",
                  "steps": [
                    {
                      "color": "rgb(77, 79, 79)",
                      "value": null
                    },
                    {
                      "color": "super-light-yellow",
                      "value": 1
                    }
                  ]
                }
              }
            ]
          },
          {
            "matcher": {
              "id": "byName",
              "options": "Int. index"
            },
            "properties": [
              {
                "id": "custom.width",
                "value": 88
              }
            ]
          },
          {
            "matcher": {
              "id": "byName",
              "options": "MTU"
            },
            "properties": [
              {
                "id": "custom.width",
                "value": 118
              },
              {
                "id": "unit",
                "value": "none"
              }
            ]
          },
          {
            "matcher": {
              "id": "byName",
              "options": "Type of interface"
            },
            "properties": [
              {
                "id": "custom.width",
                "value": 140
              },
              {
                "id": "mappings",
                "value": [
                  {
                    "options": {
                      "ethernetCsmacd": {
                        "text": "Physical"
                      },
                      "ieee80211": {
                        "text": "Wireless"
                      }
                    },
                    "type": "value"
                  }
                ]
              },
              {
                "id": "custom.filterable",
                "value": true
              }
            ]
          },
          {
            "matcher": {
              "id": "byName",
              "options": "Name"
            },
            "properties": [
              {
                "id": "custom.width"
              }
            ]
          }
        ]
      },
      "gridPos": {
        "h": 12,
        "w": 24,
        "x": 0,
        "y": 27
      },
      "id": 1275,
      "options": {
        "footer": {
          "fields": "",
          "reducer": [
            "sum"
          ],
          "show": false
        },
        "frameIndex": 0,
        "showHeader": true,
        "sortBy": [
          {
            "desc": false,
            "displayName": "MAC"
          }
        ]
      },
      "pluginVersion": "9.0.5",
      "targets": [
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${DS_PROMETHEUS}"
          },
          "exemplar": true,
          "expr": "ifPhysAddress{instance='$instance'}",
          "format": "table",
          "instant": true,
          "interval": "",
          "legendFormat": "",
          "refId": "A"
        },
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${DS_PROMETHEUS}"
          },
          "exemplar": true,
          "expr": "ifOperStatus{instance='$instance'}",
          "format": "table",
          "hide": false,
          "instant": true,
          "interval": "",
          "legendFormat": "",
          "refId": "B"
        },
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${DS_PROMETHEUS}"
          },
          "exemplar": true,
          "expr": "mtxrInterfaceStatsRxBytes{instance='$instance'}",
          "format": "table",
          "hide": false,
          "instant": true,
          "interval": "",
          "legendFormat": "",
          "refId": "C"
        },
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${DS_PROMETHEUS}"
          },
          "exemplar": true,
          "expr": "mtxrInterfaceStatsTxBytes{instance='$instance'}",
          "format": "table",
          "hide": false,
          "instant": true,
          "interval": "",
          "legendFormat": "",
          "refId": "D"
        },
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${DS_PROMETHEUS}"
          },
          "exemplar": true,
          "expr": "ifSpeed{instance='$instance'}",
          "format": "table",
          "hide": false,
          "instant": true,
          "interval": "",
          "legendFormat": "",
          "refId": "E"
        },
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${DS_PROMETHEUS}"
          },
          "exemplar": true,
          "expr": "mtxrInterfaceStatsLinkDowns{instance='$instance'}",
          "format": "table",
          "hide": false,
          "instant": true,
          "interval": "",
          "legendFormat": "",
          "refId": "F"
        },
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${DS_PROMETHEUS}"
          },
          "exemplar": true,
          "expr": "ifMtu{instance='$instance'}",
          "format": "table",
          "hide": false,
          "instant": true,
          "interval": "",
          "legendFormat": "",
          "refId": "G"
        },
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${DS_PROMETHEUS}"
          },
          "exemplar": true,
          "expr": "ifType_info{instance='$instance'}",
          "format": "table",
          "hide": false,
          "instant": true,
          "interval": "",
          "legendFormat": "",
          "refId": "H"
        },
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${DS_PROMETHEUS}"
          },
          "exemplar": true,
          "expr": "mtxrPOEInterfaceIndex{instance='$instance'}",
          "format": "table",
          "hide": false,
          "instant": true,
          "interval": "",
          "legendFormat": "",
          "refId": "I"
        },
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${DS_PROMETHEUS}"
          },
          "exemplar": true,
          "expr": "ifAlias{instance='$instance'}",
          "format": "table",
          "hide": false,
          "instant": true,
          "interval": "",
          "legendFormat": "",
          "refId": "J"
        }
      ],
      "title": "Interfaces",
      "transformations": [
        {
          "id": "seriesToColumns",
          "options": {
            "byField": "ifName"
          }
        },
        {
          "id": "organize",
          "options": {
            "excludeByName": {
              "Time": true,
              "Time 1": true,
              "Time 2": true,
              "Time 3": true,
              "Time 4": true,
              "Time 5": true,
              "Time 6": true,
              "Time 7": true,
              "Time 8": true,
              "Time 9": true,
              "Value #A": true,
              "Value #H": true,
              "Value #J": true,
              "__name__": true,
              "__name__ 1": true,
              "__name__ 2": true,
              "__name__ 3": true,
              "__name__ 4": true,
              "__name__ 5": true,
              "__name__ 6": true,
              "__name__ 7": true,
              "__name__ 8": true,
              "__name__ 9": true,
              "ifIndex": false,
              "ifIndex 1": true,
              "ifIndex 2": true,
              "ifIndex 3": true,
              "ifIndex 4": true,
              "ifIndex 5": true,
              "ifIndex 6": true,
              "instance": true,
              "instance 1": true,
              "instance 2": true,
              "instance 3": true,
              "instance 4": true,
              "instance 5": true,
              "instance 6": true,
              "instance 7": true,
              "instance 8": true,
              "instance 9": true,
              "job": true,
              "job 1": true,
              "job 2": true,
              "job 3": true,
              "job 4": true,
              "job 5": true,
              "job 6": true,
              "job 7": true,
              "job 8": true,
              "job 9": true,
              "mtxrInterfaceStatsIndex": true,
              "mtxrInterfaceStatsIndex 1": true,
              "mtxrInterfaceStatsIndex 2": true,
              "mtxrInterfaceStatsIndex 3": true
            },
            "indexByName": {
              "Time": 12,
              "Value #A": 16,
              "Value #B": 3,
              "Value #C": 8,
              "Value #D": 9,
              "Value #E": 6,
              "Value #F": 4,
              "Value #G": 7,
              "Value #H": 11,
              "Value #J": 18,
              "__name__": 13,
              "ifAlias": 10,
              "ifIndex": 0,
              "ifName": 2,
              "ifPhysAddress": 5,
              "ifType": 1,
              "instance": 14,
              "job": 15,
              "mtxrInterfaceStatsIndex": 17
            },
            "renameByName": {
              "Time": "",
              "Value #A": "",
              "Value #B": "Status link/states",
              "Value #C": "RX Sum",
              "Value #D": "TX Sum",
              "Value #E": "Rate",
              "Value #F": "Link down count",
              "Value #G": "MTU",
              "Value #H": "",
              "Value #J": "",
              "__name__": "",
              "ifAlias": "Comment",
              "ifIndex": "Int. index",
              "ifName": "Name",
              "ifPhysAddress": "MAC",
              "ifType": "Type of interface",
              "instance": "",
              "mtxrInterfaceStatsIndex": "",
              "mtxrInterfaceStatsIndex 1": ""
            }
          }
        }
      ],
      "type": "table"
    },
    {
      "aliasColors": {
        "In - wlan1": "#ff2e63"
      },
      "bars": false,
      "dashLength": 10,
      "dashes": false,
      "datasource": {
        "type": "prometheus",
        "uid": "${DS_PROMETHEUS}"
      },
      "description": "Showing values > 0",
      "fill": 1,
      "fillGradient": 0,
      "gridPos": {
        "h": 6,
        "w": 12,
        "x": 0,
        "y": 39
      },
      "hiddenSeries": false,
      "id": 1659,
      "legend": {
        "alignAsTable": true,
        "avg": true,
        "current": true,
        "hideEmpty": false,
        "hideZero": true,
        "max": true,
        "min": false,
        "rightSide": true,
        "show": true,
        "total": false,
        "values": true
      },
      "lines": true,
      "linewidth": 1,
      "nullPointMode": "connected",
      "options": {
        "alertThreshold": true
      },
      "percentage": false,
      "pluginVersion": "9.0.5",
      "pointradius": 2,
      "points": false,
      "renderer": "flot",
      "seriesOverrides": [],
      "spaceLength": 10,
      "stack": false,
      "steppedLine": false,
      "targets": [
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${DS_PROMETHEUS}"
          },
          "exemplar": true,
          "expr": "irate(mtxrInterfaceStatsTxControl{ifName=~'$Interface',instance='$instance'}[$__rate_interval])",
          "hide": false,
          "interval": "",
          "intervalFactor": 1,
          "legendFormat": "Tx Control - {{ifName}}",
          "refId": "A"
        },
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${DS_PROMETHEUS}"
          },
          "exemplar": true,
          "expr": "irate(mtxrInterfaceStatsTxDeferred{ifName=~'$Interface',instance='$instance'}[$__rate_interval])",
          "hide": false,
          "interval": "",
          "intervalFactor": 1,
          "legendFormat": "Tx Deferred - {{ifName}}",
          "refId": "B"
        },
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${DS_PROMETHEUS}"
          },
          "exemplar": true,
          "expr": "irate(mtxrInterfaceStatsTxCollision{ifName=~'$Interface',instance='$instance'}[$__rate_interval])",
          "format": "time_series",
          "hide": false,
          "instant": false,
          "interval": "",
          "intervalFactor": 1,
          "legendFormat": "Tx Collision - {{ifName}}",
          "refId": "C"
        },
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${DS_PROMETHEUS}"
          },
          "exemplar": true,
          "expr": "irate(mtxrInterfaceStatsTxDrop{ifName=~'$Interface',instance='$instance'}[$__rate_interval])",
          "format": "time_series",
          "hide": false,
          "instant": false,
          "interval": "",
          "intervalFactor": 1,
          "legendFormat": "Tx Drop - {{ifName}}",
          "refId": "D"
        },
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${DS_PROMETHEUS}"
          },
          "exemplar": true,
          "expr": "irate(mtxrInterfaceStatsTxExcessiveCollision{ifName=~'$Interface',instance='$instance'}[$__rate_interval])",
          "format": "time_series",
          "hide": false,
          "instant": false,
          "interval": "",
          "intervalFactor": 1,
          "legendFormat": "Tx Excessive Collision - {{ifName}}",
          "refId": "E"
        },
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${DS_PROMETHEUS}"
          },
          "exemplar": true,
          "expr": "irate(mtxrInterfaceStatsTxExcessiveDeferred{ifName=~'$Interface',instance='$instance'}[$__rate_interval])",
          "format": "time_series",
          "hide": false,
          "instant": false,
          "interval": "",
          "intervalFactor": 1,
          "legendFormat": "Tx Excessive Deferred - {{ifName}}",
          "refId": "F"
        },
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${DS_PROMETHEUS}"
          },
          "exemplar": true,
          "expr": "irate(mtxrInterfaceStatsTxFCSError{ifName=~'$Interface',instance='$instance'}[$__rate_interval])",
          "format": "time_series",
          "hide": false,
          "instant": false,
          "interval": "",
          "intervalFactor": 1,
          "legendFormat": "Tx FCS Error - {{ifName}}",
          "refId": "G"
        },
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${DS_PROMETHEUS}"
          },
          "exemplar": true,
          "expr": "irate(mtxrInterfaceStatsTxFragment{ifName=~'$Interface',instance='$instance'}[$__rate_interval])",
          "format": "time_series",
          "hide": false,
          "instant": false,
          "interval": "",
          "intervalFactor": 1,
          "legendFormat": "Tx Fragment - {{ifName}}",
          "refId": "H"
        },
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${DS_PROMETHEUS}"
          },
          "exemplar": true,
          "expr": "irate(mtxrInterfaceStatsTxJabber{ifName=~'$Interface',instance='$instance'}[$__rate_interval])",
          "format": "time_series",
          "hide": false,
          "instant": false,
          "interval": "",
          "intervalFactor": 1,
          "legendFormat": "Tx Jabber - {{ifName}}",
          "refId": "I"
        },
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${DS_PROMETHEUS}"
          },
          "exemplar": true,
          "expr": "irate(mtxrInterfaceStatsTxLateCollision{ifName=~'$Interface',instance='$instance'}[$__rate_interval])",
          "format": "time_series",
          "hide": false,
          "instant": false,
          "interval": "",
          "intervalFactor": 1,
          "legendFormat": "Tx Late Collision - {{ifName}}",
          "refId": "J"
        },
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${DS_PROMETHEUS}"
          },
          "exemplar": true,
          "expr": "irate(mtxrInterfaceStatsTxMultipleCollision{ifName=~'$Interface',instance='$instance'}[$__rate_interval])",
          "format": "time_series",
          "hide": false,
          "instant": false,
          "interval": "",
          "intervalFactor": 1,
          "legendFormat": "Tx Multiple Collision - {{ifName}}",
          "refId": "K"
        },
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${DS_PROMETHEUS}"
          },
          "exemplar": true,
          "expr": "irate(mtxrInterfaceStatsTxPause{ifName=~'$Interface',instance='$instance'}[$__rate_interval])",
          "format": "time_series",
          "hide": false,
          "instant": false,
          "interval": "",
          "intervalFactor": 1,
          "legendFormat": "Tx Pause - {{ifName}}",
          "refId": "L"
        },
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${DS_PROMETHEUS}"
          },
          "exemplar": true,
          "expr": "irate(mtxrInterfaceStatsTxPauseHonored{ifName=~'$Interface',instance='$instance'}[$__rate_interval])",
          "format": "time_series",
          "hide": false,
          "instant": false,
          "interval": "",
          "intervalFactor": 1,
          "legendFormat": "Tx Pause Honored - {{ifName}}",
          "refId": "M"
        },
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${DS_PROMETHEUS}"
          },
          "exemplar": true,
          "expr": "irate(mtxrInterfaceStatsTxSingleCollision{ifName=~'$Interface',instance='$instance'}[$__rate_interval])",
          "format": "time_series",
          "hide": false,
          "instant": false,
          "interval": "",
          "intervalFactor": 1,
          "legendFormat": "Tx Single Collision - {{ifName}}",
          "refId": "N"
        },
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${DS_PROMETHEUS}"
          },
          "exemplar": true,
          "expr": "irate(mtxrInterfaceStatsTxTooLong{ifName=~'$Interface',instance='$instance'}[$__rate_interval])",
          "format": "time_series",
          "hide": false,
          "instant": false,
          "interval": "",
          "intervalFactor": 1,
          "legendFormat": "Tx Too Long - {{ifName}}",
          "refId": "O"
        },
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${DS_PROMETHEUS}"
          },
          "exemplar": true,
          "expr": "irate(mtxrInterfaceStatsTxTooShort{ifName=~'$Interface',instance='$instance'}[$__rate_interval])",
          "format": "time_series",
          "hide": false,
          "instant": false,
          "interval": "",
          "intervalFactor": 1,
          "legendFormat": "Tx Too Short - {{ifName}}",
          "refId": "P"
        },
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${DS_PROMETHEUS}"
          },
          "exemplar": true,
          "expr": "irate(mtxrInterfaceStatsTxTotalCollision{ifName=~'$Interface',instance='$instance'}[$__rate_interval])",
          "format": "time_series",
          "hide": false,
          "instant": false,
          "interval": "",
          "intervalFactor": 1,
          "legendFormat": "Tx Total Collision - {{ifName}}",
          "refId": "Q"
        },
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${DS_PROMETHEUS}"
          },
          "exemplar": true,
          "expr": "irate(mtxrInterfaceStatsTxUnderrun{ifName=~'$Interface',instance='$instance'}[$__rate_interval])",
          "format": "time_series",
          "hide": false,
          "instant": false,
          "interval": "",
          "intervalFactor": 1,
          "legendFormat": "Tx Under run - {{ifName}}",
          "refId": "R"
        }
      ],
      "thresholds": [],
      "timeRegions": [],
      "title": "Tx Eth errors, etc",
      "tooltip": {
        "shared": true,
        "sort": 0,
        "value_type": "individual"
      },
      "type": "graph",
      "xaxis": {
        "mode": "time",
        "show": true,
        "values": []
      },
      "yaxes": [
        {
          "format": "bps",
          "label": "",
          "logBase": 1,
          "show": true
        },
        {
          "format": "short",
          "logBase": 1,
          "show": false
        }
      ],
      "yaxis": {
        "align": false
      }
    },
    {
      "aliasColors": {
        "In - wlan1": "#ff2e63"
      },
      "bars": false,
      "dashLength": 10,
      "dashes": false,
      "datasource": {
        "type": "prometheus",
        "uid": "${DS_PROMETHEUS}"
      },
      "description": "Showing values > 0",
      "fill": 1,
      "fillGradient": 0,
      "gridPos": {
        "h": 6,
        "w": 12,
        "x": 12,
        "y": 39
      },
      "hiddenSeries": false,
      "id": 1671,
      "legend": {
        "alignAsTable": true,
        "avg": true,
        "current": true,
        "hideEmpty": false,
        "hideZero": true,
        "max": true,
        "min": false,
        "rightSide": true,
        "show": true,
        "total": false,
        "values": true
      },
      "lines": true,
      "linewidth": 1,
      "nullPointMode": "connected",
      "options": {
        "alertThreshold": true
      },
      "percentage": false,
      "pluginVersion": "9.0.5",
      "pointradius": 2,
      "points": false,
      "renderer": "flot",
      "seriesOverrides": [],
      "spaceLength": 10,
      "stack": false,
      "steppedLine": false,
      "targets": [
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${DS_PROMETHEUS}"
          },
          "exemplar": true,
          "expr": "irate(mtxrInterfaceStatsRxAlignError{ifName=~'$Interface',instance='$instance'}[$__rate_interval])",
          "hide": false,
          "interval": "",
          "intervalFactor": 1,
          "legendFormat": "Rx Align Error - {{ifName}}",
          "refId": "A"
        },
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${DS_PROMETHEUS}"
          },
          "exemplar": true,
          "expr": "irate(mtxrInterfaceStatsRxCarrierError{ifName=~'$Interface',instance='$instance'}[$__rate_interval])",
          "hide": false,
          "interval": "",
          "intervalFactor": 1,
          "legendFormat": "Rx Carrier Error - {{ifName}}",
          "refId": "B"
        },
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${DS_PROMETHEUS}"
          },
          "exemplar": true,
          "expr": "irate(mtxrInterfaceStatsRxControl{ifName=~'$Interface',instance='$instance'}[$__rate_interval])",
          "hide": false,
          "interval": "",
          "intervalFactor": 1,
          "legendFormat": "Rx Control - {{ifName}}",
          "refId": "C"
        },
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${DS_PROMETHEUS}"
          },
          "exemplar": true,
          "expr": "irate(mtxrInterfaceStatsRxDrop{ifName=~'$Interface',instance='$instance'}[$__rate_interval])",
          "hide": false,
          "interval": "",
          "intervalFactor": 1,
          "legendFormat": "Rx Drop - {{ifName}}",
          "refId": "D"
        },
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${DS_PROMETHEUS}"
          },
          "exemplar": true,
          "expr": "irate(mtxrInterfaceStatsRxFCSError{ifName=~'$Interface',instance='$instance'}[$__rate_interval])",
          "hide": false,
          "interval": "",
          "intervalFactor": 1,
          "legendFormat": "FCS Error - {{ifName}}",
          "refId": "E"
        },
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${DS_PROMETHEUS}"
          },
          "exemplar": true,
          "expr": "irate(mtxrInterfaceStatsRxFragment{ifName=~'$Interface',instance='$instance'}[$__rate_interval])",
          "hide": false,
          "interval": "",
          "intervalFactor": 1,
          "legendFormat": "Rx Fragment - {{ifName}}",
          "refId": "F"
        },
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${DS_PROMETHEUS}"
          },
          "exemplar": true,
          "expr": "irate(mtxrInterfaceStatsRxJabber{ifName=~'$Interface',instance='$instance'}[$__rate_interval])",
          "hide": false,
          "interval": "",
          "intervalFactor": 1,
          "legendFormat": "Rx Jabber - {{ifName}}",
          "refId": "G"
        },
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${DS_PROMETHEUS}"
          },
          "exemplar": true,
          "expr": "irate(mtxrInterfaceStatsRxLengthError{ifName=~'$Interface',instance='$instance'}[$__rate_interval])",
          "hide": false,
          "interval": "",
          "intervalFactor": 1,
          "legendFormat": "Rx Length Error - {{ifName}}",
          "refId": "H"
        },
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${DS_PROMETHEUS}"
          },
          "exemplar": true,
          "expr": "irate(mtxrInterfaceStatsRxOverflow{ifName=~'$Interface',instance='$instance'}[$__rate_interval])",
          "hide": false,
          "interval": "",
          "intervalFactor": 1,
          "legendFormat": "Rx Overflow - {{ifName}}",
          "refId": "I"
        },
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${DS_PROMETHEUS}"
          },
          "exemplar": true,
          "expr": "irate(mtxrInterfaceStatsRxPause{ifName=~'$Interface',instance='$instance'}[$__rate_interval])",
          "hide": false,
          "interval": "",
          "intervalFactor": 1,
          "legendFormat": "Rx Pause - {{ifName}}",
          "refId": "J"
        },
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${DS_PROMETHEUS}"
          },
          "exemplar": true,
          "expr": "irate(mtxrInterfaceStatsRxTooLong{ifName=~'$Interface',instance='$instance'}[$__rate_interval])",
          "hide": false,
          "interval": "",
          "intervalFactor": 1,
          "legendFormat": "Rx Too Long - {{ifName}}",
          "refId": "K"
        },
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${DS_PROMETHEUS}"
          },
          "exemplar": true,
          "expr": "irate(mtxrInterfaceStatsRxTooShort{ifName=~'$Interface',instance='$instance'}[$__rate_interval])",
          "hide": false,
          "interval": "",
          "intervalFactor": 1,
          "legendFormat": "Rx Too Short - {{ifName}}",
          "refId": "L"
        },
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${DS_PROMETHEUS}"
          },
          "exemplar": true,
          "expr": "irate(mtxrInterfaceStatsRxUnknownOp{ifName=~'$Interface',instance='$instance'}[$__rate_interval])",
          "hide": false,
          "interval": "",
          "intervalFactor": 1,
          "legendFormat": "Rx Unknown Op - {{ifName}}",
          "refId": "M"
        }
      ],
      "thresholds": [],
      "timeRegions": [],
      "title": "Rx Eth errors, etc",
      "tooltip": {
        "shared": true,
        "sort": 0,
        "value_type": "individual"
      },
      "type": "graph",
      "xaxis": {
        "mode": "time",
        "show": true,
        "values": []
      },
      "yaxes": [
        {
          "format": "bps",
          "label": "",
          "logBase": 1,
          "show": true
        },
        {
          "format": "short",
          "logBase": 1,
          "show": false
        }
      ],
      "yaxis": {
        "align": false
      }
    },
    {
      "datasource": {
        "type": "prometheus",
        "uid": "${DS_PROMETHEUS}"
      },
      "description": "",
      "fieldConfig": {
        "defaults": {
          "color": {
            "mode": "thresholds"
          },
          "custom": {
            "align": "auto",
            "displayMode": "color-text",
            "filterable": false,
            "inspect": false
          },
          "mappings": [],
          "thresholds": {
            "mode": "absolute",
            "steps": [
              {
                "color": "super-light-yellow",
                "value": null
              }
            ]
          },
          "unit": "short"
        },
        "overrides": [
          {
            "matcher": {
              "id": "byName",
              "options": "Neighbor index"
            },
            "properties": [
              {
                "id": "custom.align",
                "value": "center"
              },
              {
                "id": "custom.width",
                "value": 134
              }
            ]
          },
          {
            "matcher": {
              "id": "byName",
              "options": "IP"
            },
            "properties": [
              {
                "id": "custom.width",
                "value": 111
              }
            ]
          },
          {
            "matcher": {
              "id": "byName",
              "options": "MAC"
            },
            "properties": [
              {
                "id": "custom.width",
                "value": 142
              }
            ]
          },
          {
            "matcher": {
              "id": "byName",
              "options": "Platform"
            },
            "properties": [
              {
                "id": "custom.width",
                "value": 127
              }
            ]
          },
          {
            "matcher": {
              "id": "byName",
              "options": "Software ID"
            },
            "properties": [
              {
                "id": "custom.width",
                "value": 136
              }
            ]
          }
        ]
      },
      "gridPos": {
        "h": 6,
        "w": 24,
        "x": 0,
        "y": 45
      },
      "id": 1652,
      "options": {
        "footer": {
          "fields": "",
          "reducer": [
            "sum"
          ],
          "show": false
        },
        "frameIndex": 0,
        "showHeader": true,
        "sortBy": [
          {
            "desc": true,
            "displayName": "Neighbor index"
          }
        ]
      },
      "pluginVersion": "9.0.5",
      "targets": [
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${DS_PROMETHEUS}"
          },
          "exemplar": true,
          "expr": "mtxrNeighborInterfaceID{instance='$instance'}",
          "format": "table",
          "instant": true,
          "interval": "",
          "legendFormat": "",
          "refId": "A"
        },
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${DS_PROMETHEUS}"
          },
          "exemplar": true,
          "expr": "mtxrNeighborIdentity{instance='$instance'}",
          "format": "table",
          "hide": false,
          "instant": true,
          "interval": "",
          "legendFormat": "",
          "refId": "B"
        },
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${DS_PROMETHEUS}"
          },
          "exemplar": true,
          "expr": "mtxrNeighborIpAddress{instance='$instance'}",
          "format": "table",
          "hide": false,
          "instant": true,
          "interval": "",
          "legendFormat": "",
          "refId": "C"
        },
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${DS_PROMETHEUS}"
          },
          "exemplar": true,
          "expr": "mtxrNeighborMacAddress{instance='$instance'}",
          "format": "table",
          "hide": false,
          "instant": true,
          "interval": "",
          "legendFormat": "",
          "refId": "D"
        },
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${DS_PROMETHEUS}"
          },
          "exemplar": true,
          "expr": "mtxrNeighborPlatform{instance='$instance'}",
          "format": "table",
          "hide": false,
          "instant": true,
          "interval": "",
          "legendFormat": "",
          "refId": "E"
        },
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${DS_PROMETHEUS}"
          },
          "exemplar": true,
          "expr": "mtxrNeighborSoftwareID{instance='$instance'}",
          "format": "table",
          "hide": false,
          "instant": true,
          "interval": "",
          "legendFormat": "",
          "refId": "F"
        },
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${DS_PROMETHEUS}"
          },
          "exemplar": true,
          "expr": "mtxrNeighborVersion{instance='$instance'}",
          "format": "table",
          "hide": false,
          "instant": true,
          "interval": "",
          "legendFormat": "",
          "refId": "G"
        }
      ],
      "title": "Neighbors",
      "transformations": [
        {
          "id": "seriesToColumns",
          "options": {
            "byField": "mtxrNeighborIndex"
          }
        },
        {
          "id": "merge",
          "options": {}
        },
        {
          "id": "organize",
          "options": {
            "excludeByName": {
              "Time": true,
              "Value #A": true,
              "Value #B": true,
              "Value #C": true,
              "Value #D": true,
              "Value #E": true,
              "Value #F": true,
              "Value #G": true,
              "__name__": true,
              "instance": true,
              "job": true,
              "mtxrNeighborIndex": false
            },
            "indexByName": {},
            "renameByName": {
              "Time": "",
              "Value #A": "",
              "Value #B": "",
              "Value #C": "",
              "Value #D": "",
              "Value #E": "",
              "Value #F": "",
              "job": "",
              "mtxrNeighborIdentity": "identity",
              "mtxrNeighborIndex": "Neighbor index",
              "mtxrNeighborIpAddress": "IP",
              "mtxrNeighborMacAddress": "MAC",
              "mtxrNeighborPlatform": "Platform",
              "mtxrNeighborSoftwareID": "Software ID",
              "mtxrNeighborVersion": "Firmware version"
            }
          }
        }
      ],
      "type": "table"
    },
    {
      "collapsed": true,
      "datasource": {
        "type": "prometheus",
        "uid": "PBFA97CFB590B2093"
      },
      "gridPos": {
        "h": 1,
        "w": 24,
        "x": 0,
        "y": 51
      },
      "id": 1642,
      "panels": [
        {
          "aliasColors": {
            "CCQ - 1": "#ff2e63",
            "CCQ - 2": "#08d9d6",
            "CCQ - Tilda": "#ff2e63",
            "Noise - 1": "#ff2e63",
            "Noise - 2": "#08d9d6",
            "Noise - Tilda": "light-blue",
            "Noise - Tilda_5": "dark-purple",
            "TX CCQ - Tilda": "#ff2e63"
          },
          "bars": false,
          "dashLength": 10,
          "dashes": false,
          "datasource": {
            "type": "prometheus",
            "uid": "${DS_PROMETHEUS}"
          },
          "description": "",
          "fill": 1,
          "fillGradient": 0,
          "gridPos": {
            "h": 9,
            "w": 8,
            "x": 0,
            "y": 3
          },
          "hiddenSeries": false,
          "id": 1270,
          "legend": {
            "alignAsTable": true,
            "avg": true,
            "current": true,
            "hideZero": true,
            "max": false,
            "min": false,
            "rightSide": false,
            "show": true,
            "total": false,
            "values": true
          },
          "lines": true,
          "linewidth": 1,
          "links": [],
          "maxPerRow": 2,
          "nullPointMode": "connected",
          "options": {
            "alertThreshold": true
          },
          "percentage": false,
          "pluginVersion": "8.3.4",
          "pointradius": 2,
          "points": false,
          "renderer": "flot",
          "repeatDirection": "h",
          "seriesOverrides": [
            {
              "alias": "2",
              "yaxis": 1
            },
            {
              "alias": "mtxrWlApNoiseFloor{instance=\"192.168.5.1\", job=\"Mikrotik\", mtxrWlApIndex=\"2\"}",
              "yaxis": 2
            },
            {
              "alias": "mtxrWlApNoiseFloor{instance=\"192.168.5.1\", job=\"Mikrotik\", mtxrWlApIndex=\"11\"}",
              "yaxis": 2
            },
            {
              "alias": "mtxrWlApNoiseFloor{instance=\"192.168.5.1\", job=\"Mikrotik\", mtxrWlApIndex=\"1\"}",
              "yaxis": 2
            },
            {
              "alias": "Noise 1",
              "yaxis": 2
            },
            {
              "alias": "Noise 11",
              "yaxis": 2
            },
            {
              "alias": "Noise 2",
              "yaxis": 2
            },
            {
              "alias": "Noise - 2",
              "yaxis": 2
            },
            {
              "alias": "Noise - 11",
              "yaxis": 2
            },
            {
              "alias": "Noise - 1",
              "yaxis": 2
            },
            {
              "alias": "Noise - Tilda",
              "yaxis": 2
            },
            {
              "alias": "Noise - Tilda_5",
              "yaxis": 2
            }
          ],
          "spaceLength": 10,
          "stack": false,
          "steppedLine": false,
          "targets": [
            {
              "datasource": {
                "type": "prometheus",
                "uid": "${DS_PROMETHEUS}"
              },
              "exemplar": true,
              "expr": "(mtxrWlApOverallTxCCQ{instance='$instance'}*on(mtxrWlApIndex)group_left(mtxrWlApSsid)mtxrWlApSsid{instance='$instance'})",
              "hide": false,
              "interval": "",
              "legendFormat": "TX CCQ - {{mtxrWlApSsid}}",
              "refId": "A"
            },
            {
              "datasource": {
                "type": "prometheus",
                "uid": "${DS_PROMETHEUS}"
              },
              "exemplar": true,
              "expr": "(mtxrWlApNoiseFloor{instance='$instance'}*on(mtxrWlApIndex)group_left(mtxrWlApSsid)mtxrWlApSsid{instance='$instance'})",
              "format": "time_series",
              "hide": false,
              "instant": false,
              "interval": "",
              "intervalFactor": 1,
              "legendFormat": "Noise - {{mtxrWlApSsid}}",
              "refId": "B"
            }
          ],
          "thresholds": [],
          "timeRegions": [],
          "title": "Wi-Fi Overall Tx CCQ & Noise",
          "tooltip": {
            "shared": true,
            "sort": 0,
            "value_type": "individual"
          },
          "type": "graph",
          "xaxis": {
            "mode": "time",
            "show": true,
            "values": []
          },
          "yaxes": [
            {
              "format": "percent",
              "label": "",
              "logBase": 1,
              "show": true
            },
            {
              "format": "dBm",
              "label": "",
              "logBase": 1,
              "show": true
            }
          ],
          "yaxis": {
            "align": true,
            "alignLevel": 0
          }
        },
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${DS_PROMETHEUS}"
          },
          "description": "",
          "fieldConfig": {
            "defaults": {
              "color": {
                "mode": "palette-classic"
              },
              "custom": {
                "axisLabel": "",
                "axisPlacement": "auto",
                "barAlignment": 0,
                "drawStyle": "line",
                "fillOpacity": 10,
                "gradientMode": "none",
                "hideFrom": {
                  "legend": false,
                  "tooltip": false,
                  "viz": false
                },
                "lineInterpolation": "smooth",
                "lineWidth": 2,
                "pointSize": 5,
                "scaleDistribution": {
                  "type": "linear"
                },
                "showPoints": "never",
                "spanNulls": false,
                "stacking": {
                  "group": "A",
                  "mode": "none"
                },
                "thresholdsStyle": {
                  "mode": "off"
                }
              },
              "decimals": 0,
              "mappings": [],
              "thresholds": {
                "mode": "absolute",
                "steps": [
                  {
                    "color": "green"
                  },
                  {
                    "color": "red",
                    "value": 80
                  }
                ]
              },
              "unit": "short"
            },
            "overrides": [
              {
                "matcher": {
                  "id": "byName",
                  "options": "1"
                },
                "properties": [
                  {
                    "id": "color",
                    "value": {
                      "fixedColor": "#ff2e63",
                      "mode": "fixed"
                    }
                  }
                ]
              },
              {
                "matcher": {
                  "id": "byName",
                  "options": "2"
                },
                "properties": [
                  {
                    "id": "color",
                    "value": {
                      "fixedColor": "#08d9d6",
                      "mode": "fixed"
                    }
                  }
                ]
              },
              {
                "matcher": {
                  "id": "byName",
                  "options": "DHCP Leases count"
                },
                "properties": [
                  {
                    "id": "color",
                    "value": {
                      "fixedColor": "dark-green",
                      "mode": "fixed"
                    }
                  }
                ]
              },
              {
                "matcher": {
                  "id": "byName",
                  "options": "Tilda"
                },
                "properties": [
                  {
                    "id": "color",
                    "value": {
                      "fixedColor": "#ff2e63",
                      "mode": "fixed"
                    }
                  }
                ]
              }
            ]
          },
          "gridPos": {
            "h": 9,
            "w": 8,
            "x": 8,
            "y": 3
          },
          "id": 1261,
          "options": {
            "legend": {
              "calcs": [
                "mean",
                "lastNotNull",
                "max",
                "min"
              ],
              "displayMode": "table",
              "placement": "bottom"
            },
            "tooltip": {
              "mode": "single"
            }
          },
          "pluginVersion": "8.2.1",
          "targets": [
            {
              "datasource": {
                "type": "prometheus",
                "uid": "${DS_PROMETHEUS}"
              },
              "exemplar": true,
              "expr": "(mtxrWlApAuthClientCount{instance='$instance'}*on(mtxrWlApIndex)group_left(mtxrWlApSsid)mtxrWlApSsid{instance='$instance'})",
              "hide": false,
              "interval": "",
              "legendFormat": "{{mtxrWlApSsid}}",
              "refId": "A"
            },
            {
              "datasource": {
                "type": "prometheus",
                "uid": "${DS_PROMETHEUS}"
              },
              "exemplar": true,
              "expr": "mtxrDHCPLeaseCount{instance='$instance'}",
              "hide": false,
              "interval": "",
              "legendFormat": "DHCP Leases",
              "refId": "B"
            }
          ],
          "title": "Wi-Fi Client count",
          "type": "timeseries"
        },
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${DS_PROMETHEUS}"
          },
          "description": "",
          "fieldConfig": {
            "defaults": {
              "color": {
                "mode": "palette-classic"
              },
              "custom": {
                "axisLabel": "",
                "axisPlacement": "auto",
                "barAlignment": 0,
                "drawStyle": "line",
                "fillOpacity": 10,
                "gradientMode": "none",
                "hideFrom": {
                  "legend": false,
                  "tooltip": false,
                  "viz": false
                },
                "lineInterpolation": "smooth",
                "lineWidth": 2,
                "pointSize": 5,
                "scaleDistribution": {
                  "type": "linear"
                },
                "showPoints": "never",
                "spanNulls": false,
                "stacking": {
                  "group": "A",
                  "mode": "none"
                },
                "thresholdsStyle": {
                  "mode": "off"
                }
              },
              "decimals": 0,
              "mappings": [],
              "thresholds": {
                "mode": "absolute",
                "steps": [
                  {
                    "color": "green"
                  },
                  {
                    "color": "red",
                    "value": 80
                  }
                ]
              },
              "unit": "MHz"
            },
            "overrides": [
              {
                "matcher": {
                  "id": "byName",
                  "options": "1"
                },
                "properties": [
                  {
                    "id": "color",
                    "value": {
                      "fixedColor": "#ff2e63",
                      "mode": "fixed"
                    }
                  }
                ]
              },
              {
                "matcher": {
                  "id": "byName",
                  "options": "2"
                },
                "properties": [
                  {
                    "id": "color",
                    "value": {
                      "fixedColor": "#08d9d6",
                      "mode": "fixed"
                    }
                  }
                ]
              },
              {
                "matcher": {
                  "id": "byName",
                  "options": "DHCP Leases count"
                },
                "properties": [
                  {
                    "id": "color",
                    "value": {
                      "fixedColor": "dark-green",
                      "mode": "fixed"
                    }
                  }
                ]
              },
              {
                "matcher": {
                  "id": "byName",
                  "options": "Tilda"
                },
                "properties": [
                  {
                    "id": "color",
                    "value": {
                      "fixedColor": "#ff2e63",
                      "mode": "fixed"
                    }
                  }
                ]
              }
            ]
          },
          "gridPos": {
            "h": 9,
            "w": 8,
            "x": 16,
            "y": 3
          },
          "id": 1613,
          "options": {
            "legend": {
              "calcs": [
                "lastNotNull"
              ],
              "displayMode": "list",
              "placement": "bottom"
            },
            "tooltip": {
              "mode": "single"
            }
          },
          "pluginVersion": "8.2.1",
          "targets": [
            {
              "datasource": {
                "type": "prometheus",
                "uid": "${DS_PROMETHEUS}"
              },
              "exemplar": true,
              "expr": "mtxrWlApFreq{instance='$instance'}*on(mtxrWlApIndex)group_left(mtxrWlApSsid)mtxrWlApSsid{instance='$instance'}",
              "hide": false,
              "instant": false,
              "interval": "",
              "legendFormat": "{{mtxrWlApSsid}}",
              "refId": "A"
            }
          ],
          "title": "Wi-Fi frequency",
          "type": "timeseries"
        },
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${DS_PROMETHEUS}"
          },
          "description": "Wireless registration table. It is indexed by remote mac-address and local interface index.\n\nMeasured in dB, if value does not exist it is indicated with 0",
          "fieldConfig": {
            "defaults": {
              "color": {
                "mode": "thresholds"
              },
              "custom": {
                "displayMode": "auto",
                "filterable": false
              },
              "mappings": [],
              "thresholds": {
                "mode": "absolute",
                "steps": [
                  {
                    "color": "green"
                  }
                ]
              }
            },
            "overrides": [
              {
                "matcher": {
                  "id": "byName",
                  "options": "mac address"
                },
                "properties": [
                  {
                    "id": "custom.width"
                  }
                ]
              },
              {
                "matcher": {
                  "id": "byName",
                  "options": "Interface"
                },
                "properties": [
                  {
                    "id": "custom.width",
                    "value": 90
                  }
                ]
              },
              {
                "matcher": {
                  "id": "byName",
                  "options": "Signal-to-Noise"
                },
                "properties": [
                  {
                    "id": "custom.width",
                    "value": 200
                  },
                  {
                    "id": "unit",
                    "value": "dB"
                  },
                  {
                    "id": "custom.displayMode",
                    "value": "lcd-gauge"
                  },
                  {
                    "id": "min",
                    "value": 5
                  },
                  {
                    "id": "max",
                    "value": 50
                  },
                  {
                    "id": "color",
                    "value": {
                      "mode": "continuous-RdYlGr"
                    }
                  }
                ]
              },
              {
                "matcher": {
                  "id": "byName",
                  "options": "Strength"
                },
                "properties": [
                  {
                    "id": "custom.width",
                    "value": 200
                  },
                  {
                    "id": "unit",
                    "value": "dBm"
                  },
                  {
                    "id": "custom.displayMode",
                    "value": "lcd-gauge"
                  },
                  {
                    "id": "min",
                    "value": -85
                  },
                  {
                    "id": "max",
                    "value": -30
                  },
                  {
                    "id": "color",
                    "value": {
                      "mode": "continuous-RdYlGr"
                    }
                  }
                ]
              },
              {
                "matcher": {
                  "id": "byType",
                  "options": "number"
                },
                "properties": [
                  {
                    "id": "custom.align",
                    "value": "center"
                  }
                ]
              },
              {
                "matcher": {
                  "id": "byType",
                  "options": "string"
                },
                "properties": [
                  {
                    "id": "custom.align",
                    "value": "center"
                  }
                ]
              },
              {
                "matcher": {
                  "id": "byName",
                  "options": "Tx"
                },
                "properties": [
                  {
                    "id": "custom.width",
                    "value": 90
                  },
                  {
                    "id": "unit",
                    "value": "bytes"
                  }
                ]
              },
              {
                "matcher": {
                  "id": "byName",
                  "options": "Rx"
                },
                "properties": [
                  {
                    "id": "custom.width",
                    "value": 90
                  },
                  {
                    "id": "unit",
                    "value": "bytes"
                  }
                ]
              },
              {
                "matcher": {
                  "id": "byName",
                  "options": "Tx rate"
                },
                "properties": [
                  {
                    "id": "custom.width",
                    "value": 90
                  },
                  {
                    "id": "unit",
                    "value": "bps"
                  }
                ]
              },
              {
                "matcher": {
                  "id": "byName",
                  "options": "Rx rate"
                },
                "properties": [
                  {
                    "id": "custom.width"
                  },
                  {
                    "id": "unit",
                    "value": "bps"
                  }
                ]
              },
              {
                "matcher": {
                  "id": "byName",
                  "options": "Uptime"
                },
                "properties": [
                  {
                    "id": "custom.width",
                    "value": 90
                  },
                  {
                    "id": "decimals",
                    "value": 1
                  },
                  {
                    "id": "unit",
                    "value": "timeticks"
                  }
                ]
              },
              {
                "matcher": {
                  "id": "byName",
                  "options": "Value #I"
                },
                "properties": [
                  {
                    "id": "custom.width",
                    "value": 263
                  }
                ]
              }
            ]
          },
          "gridPos": {
            "h": 8,
            "w": 24,
            "x": 0,
            "y": 12
          },
          "id": 1643,
          "links": [],
          "options": {
            "footer": {
              "fields": "",
              "reducer": [
                "sum"
              ],
              "show": false
            },
            "showHeader": true,
            "sortBy": []
          },
          "pluginVersion": "8.3.4",
          "targets": [
            {
              "datasource": {
                "type": "prometheus",
                "uid": "${DS_PROMETHEUS}"
              },
              "exemplar": true,
              "expr": "mtxrWlRtabAddr{instance='$instance'}",
              "format": "table",
              "hide": false,
              "instant": true,
              "interval": "",
              "legendFormat": "",
              "refId": "A"
            },
            {
              "datasource": {
                "type": "prometheus",
                "uid": "${DS_PROMETHEUS}"
              },
              "exemplar": true,
              "expr": "mtxrWlRtabSignalToNoise{instance='$instance'}",
              "format": "table",
              "hide": false,
              "instant": true,
              "interval": "",
              "legendFormat": "",
              "refId": "B"
            },
            {
              "datasource": {
                "type": "prometheus",
                "uid": "${DS_PROMETHEUS}"
              },
              "exemplar": true,
              "expr": "mtxrWlRtabStrength{instance='$instance'}",
              "format": "table",
              "hide": false,
              "instant": true,
              "interval": "",
              "legendFormat": "",
              "refId": "C"
            },
            {
              "datasource": {
                "type": "prometheus",
                "uid": "${DS_PROMETHEUS}"
              },
              "exemplar": true,
              "expr": "mtxrWlRtabTxBytes{instance='$instance'}",
              "format": "table",
              "hide": false,
              "instant": true,
              "interval": "",
              "legendFormat": "",
              "refId": "D"
            },
            {
              "datasource": {
                "type": "prometheus",
                "uid": "${DS_PROMETHEUS}"
              },
              "exemplar": true,
              "expr": "mtxrWlRtabRxBytes{instance='$instance'}",
              "format": "table",
              "hide": false,
              "instant": true,
              "interval": "",
              "legendFormat": "",
              "refId": "E"
            },
            {
              "datasource": {
                "type": "prometheus",
                "uid": "${DS_PROMETHEUS}"
              },
              "exemplar": true,
              "expr": "mtxrWlRtabTxRate{instance='$instance'}",
              "format": "table",
              "hide": false,
              "instant": true,
              "interval": "",
              "legendFormat": "",
              "refId": "F"
            },
            {
              "datasource": {
                "type": "prometheus",
                "uid": "${DS_PROMETHEUS}"
              },
              "exemplar": true,
              "expr": "mtxrWlRtabRxRate{instance='$instance'}",
              "format": "table",
              "hide": false,
              "instant": true,
              "interval": "",
              "legendFormat": "",
              "refId": "G"
            },
            {
              "datasource": {
                "type": "prometheus",
                "uid": "${DS_PROMETHEUS}"
              },
              "exemplar": true,
              "expr": "mtxrWlRtabUptime{instance='$instance'}",
              "format": "table",
              "hide": false,
              "instant": true,
              "interval": "",
              "legendFormat": "",
              "refId": "H"
            }
          ],
          "title": "Wi-Fi Clients",
          "transformations": [
            {
              "id": "seriesToColumns",
              "options": {
                "byField": "mtxrWlRtabAddr"
              }
            },
            {
              "id": "organize",
              "options": {
                "excludeByName": {
                  "Time": true,
                  "Time 1": true,
                  "Time 2": true,
                  "Time 3": true,
                  "Time 4": true,
                  "Time 5": true,
                  "Time 6": true,
                  "Time 7": true,
                  "Time 8": true,
                  "Value #A": true,
                  "__name__": true,
                  "__name__ 1": true,
                  "__name__ 2": true,
                  "__name__ 3": true,
                  "__name__ 4": true,
                  "__name__ 5": true,
                  "__name__ 6": true,
                  "__name__ 7": true,
                  "__name__ 8": true,
                  "instance": true,
                  "instance 1": true,
                  "instance 2": true,
                  "instance 3": true,
                  "instance 4": true,
                  "instance 5": true,
                  "instance 6": true,
                  "instance 7": true,
                  "instance 8": true,
                  "job": true,
                  "job 1": true,
                  "job 2": true,
                  "job 3": true,
                  "job 4": true,
                  "job 5": true,
                  "job 6": true,
                  "job 7": true,
                  "job 8": true,
                  "mtxrWlRtabIface 1": false,
                  "mtxrWlRtabIface 2": true,
                  "mtxrWlRtabIface 3": true,
                  "mtxrWlRtabIface 4": true,
                  "mtxrWlRtabIface 5": true,
                  "mtxrWlRtabIface 6": true,
                  "mtxrWlRtabIface 7": true,
                  "mtxrWlRtabIface 8": true
                },
                "indexByName": {
                  "Time": 5,
                  "Value #A": 9,
                  "Value #B": 4,
                  "Value #C": 3,
                  "Value #D": 12,
                  "Value #E": 13,
                  "Value #F": 10,
                  "Value #G": 11,
                  "Value #H": 0,
                  "__name__": 6,
                  "instance": 7,
                  "job": 8,
                  "mtxrWlRtabAddr": 1,
                  "mtxrWlRtabIface": 2
                },
                "renameByName": {
                  "Time": "",
                  "Value #A": "",
                  "Value #B": "Signal-to-Noise",
                  "Value #C": "Strength",
                  "Value #D": "Tx",
                  "Value #E": "Rx",
                  "Value #F": "Tx rate",
                  "Value #G": "Rx rate",
                  "Value #H": "Uptime",
                  "job": "",
                  "mtxrWlRtabAddr": "Mac address",
                  "mtxrWlRtabIface": "Interface",
                  "mtxrWlRtabIface 1": "wifi interface id"
                }
              }
            }
          ],
          "type": "table"
        },
        {
          "cards": {},
          "color": {
            "cardColor": "#C4162A",
            "colorScale": "sqrt",
            "colorScheme": "interpolateRdYlGn",
            "exponent": 0.5,
            "max": -85,
            "min": -30,
            "mode": "spectrum"
          },
          "dataFormat": "tsbuckets",
          "datasource": {
            "type": "prometheus",
            "uid": "${DS_PROMETHEUS}"
          },
          "description": "Signal Strength: signal strength in dBm (if first ppp-client modem supports)",
          "gridPos": {
            "h": 8,
            "w": 12,
            "x": 0,
            "y": 20
          },
          "heatmap": {},
          "hideZeroBuckets": false,
          "highlightCards": true,
          "id": 1647,
          "legend": {
            "show": false
          },
          "links": [],
          "pluginVersion": "7.5.5",
          "repeatDirection": "h",
          "reverseYBuckets": false,
          "targets": [
            {
              "datasource": {
                "type": "prometheus",
                "uid": "${DS_PROMETHEUS}"
              },
              "exemplar": true,
              "expr": "mtxrWlRtabStrength{instance='$instance'}",
              "hide": false,
              "interval": "",
              "legendFormat": "{{mtxrWlRtabAddr}}",
              "refId": "A"
            }
          ],
          "title": "History Wi-Fi Strength",
          "tooltip": {
            "show": true,
            "showHistogram": true
          },
          "type": "heatmap",
          "xAxis": {
            "show": true
          },
          "xBucketSize": "2m",
          "yAxis": {
            "format": "dBm",
            "logBase": 1,
            "show": true
          },
          "yBucketBound": "auto",
          "yBucketSize": 2
        },
        {
          "cards": {},
          "color": {
            "cardColor": "#C4162A",
            "colorScale": "sqrt",
            "colorScheme": "interpolateRdYlGn",
            "exponent": 0.5,
            "max": 5,
            "min": 50,
            "mode": "spectrum"
          },
          "dataFormat": "tsbuckets",
          "datasource": {
            "type": "prometheus",
            "uid": "${DS_PROMETHEUS}"
          },
          "description": "Measured in dB, if value does not exist it is indicated with 0",
          "gridPos": {
            "h": 8,
            "w": 12,
            "x": 12,
            "y": 20
          },
          "heatmap": {},
          "hideZeroBuckets": false,
          "highlightCards": true,
          "id": 1648,
          "legend": {
            "show": false
          },
          "links": [],
          "pluginVersion": "7.5.5",
          "repeatDirection": "h",
          "reverseYBuckets": false,
          "targets": [
            {
              "datasource": {
                "type": "prometheus",
                "uid": "${DS_PROMETHEUS}"
              },
              "exemplar": true,
              "expr": "mtxrWlRtabSignalToNoise{instance='$instance'}",
              "hide": false,
              "interval": "",
              "legendFormat": "{{mtxrWlRtabAddr}}",
              "refId": "A"
            }
          ],
          "title": "History Wi-Fi Signal-to-Noise",
          "tooltip": {
            "show": true,
            "showHistogram": true
          },
          "type": "heatmap",
          "xAxis": {
            "show": true
          },
          "xBucketSize": "2m",
          "yAxis": {
            "format": "dB",
            "logBase": 1,
            "show": true
          },
          "yBucketBound": "auto",
          "yBucketSize": 2
        }
      ],
      "targets": [
        {
          "datasource": {
            "type": "prometheus",
            "uid": "PBFA97CFB590B2093"
          },
          "refId": "A"
        }
      ],
      "title": "Wireless",
      "type": "row"
    },
    {
      "collapsed": true,
      "datasource": {
        "type": "prometheus",
        "uid": "PBFA97CFB590B2093"
      },
      "gridPos": {
        "h": 1,
        "w": 24,
        "x": 0,
        "y": 52
      },
      "id": 1676,
      "panels": [
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${DS_PROMETHEUS}"
          },
          "description": "Wireless registration table entry count",
          "fieldConfig": {
            "defaults": {
              "color": {
                "mode": "thresholds"
              },
              "mappings": [],
              "thresholds": {
                "mode": "absolute",
                "steps": [
                  {
                    "color": "#299c46"
                  }
                ]
              }
            },
            "overrides": []
          },
          "gridPos": {
            "h": 4,
            "w": 3,
            "x": 0,
            "y": 4
          },
          "id": 1646,
          "options": {
            "colorMode": "value",
            "graphMode": "none",
            "justifyMode": "auto",
            "orientation": "auto",
            "reduceOptions": {
              "calcs": [
                "lastNotNull"
              ],
              "fields": "",
              "values": false
            },
            "text": {},
            "textMode": "auto"
          },
          "pluginVersion": "8.3.4",
          "targets": [
            {
              "datasource": {
                "type": "prometheus",
                "uid": "${DS_PROMETHEUS}"
              },
              "exemplar": true,
              "expr": "mtxrWlCMRtabEntryCount{instance='$instance'}",
              "format": "time_series",
              "hide": false,
              "instant": true,
              "interval": "",
              "legendFormat": "",
              "refId": "A"
            }
          ],
          "title": "CAPsMAN client count",
          "type": "stat"
        },
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${DS_PROMETHEUS}"
          },
          "description": "",
          "fieldConfig": {
            "defaults": {
              "color": {
                "mode": "thresholds"
              },
              "custom": {
                "align": "auto",
                "displayMode": "auto"
              },
              "mappings": [],
              "thresholds": {
                "mode": "absolute",
                "steps": [
                  {
                    "color": "green"
                  },
                  {
                    "color": "red",
                    "value": 80
                  }
                ]
              }
            },
            "overrides": [
              {
                "matcher": {
                  "id": "byName",
                  "options": "Remote address"
                },
                "properties": [
                  {
                    "id": "custom.width",
                    "value": 187
                  },
                  {
                    "id": "custom.align",
                    "value": "center"
                  }
                ]
              },
              {
                "matcher": {
                  "id": "byName",
                  "options": "remote index"
                },
                "properties": [
                  {
                    "id": "custom.width",
                    "value": 110
                  },
                  {
                    "id": "custom.align",
                    "value": "center"
                  }
                ]
              },
              {
                "matcher": {
                  "id": "byName",
                  "options": "Remote name"
                },
                "properties": [
                  {
                    "id": "custom.width"
                  },
                  {
                    "id": "custom.align",
                    "value": "center"
                  }
                ]
              },
              {
                "matcher": {
                  "id": "byName",
                  "options": "Remote address/port"
                },
                "properties": [
                  {
                    "id": "custom.width",
                    "value": 199
                  },
                  {
                    "id": "custom.align",
                    "value": "center"
                  }
                ]
              },
              {
                "matcher": {
                  "id": "byName",
                  "options": "state"
                },
                "properties": [
                  {
                    "id": "custom.width",
                    "value": 74
                  },
                  {
                    "id": "custom.align",
                    "value": "center"
                  }
                ]
              },
              {
                "matcher": {
                  "id": "byName",
                  "options": "Remote Radios"
                },
                "properties": [
                  {
                    "id": "custom.width",
                    "value": 122
                  },
                  {
                    "id": "custom.align",
                    "value": "center"
                  }
                ]
              }
            ]
          },
          "gridPos": {
            "h": 8,
            "w": 11,
            "x": 3,
            "y": 4
          },
          "id": 1681,
          "options": {
            "footer": {
              "fields": "",
              "reducer": [
                "sum"
              ],
              "show": false
            },
            "showHeader": true,
            "sortBy": [
              {
                "desc": true,
                "displayName": "state"
              }
            ]
          },
          "pluginVersion": "8.3.4",
          "targets": [
            {
              "datasource": {
                "type": "prometheus",
                "uid": "${DS_PROMETHEUS}"
              },
              "exemplar": true,
              "expr": "mtxrWlCMRemoteAddress{instance='$instance'}",
              "format": "table",
              "hide": false,
              "instant": true,
              "interval": "",
              "legendFormat": "",
              "refId": "A"
            },
            {
              "datasource": {
                "type": "prometheus",
                "uid": "${DS_PROMETHEUS}"
              },
              "exemplar": true,
              "expr": "mtxrWlCMRemoteName{instance='$instance'}",
              "format": "table",
              "hide": false,
              "instant": true,
              "interval": "",
              "legendFormat": "",
              "refId": "B"
            },
            {
              "datasource": {
                "type": "prometheus",
                "uid": "${DS_PROMETHEUS}"
              },
              "exemplar": true,
              "expr": "mtxrWlCMRemoteRadios{instance='$instance'}",
              "format": "table",
              "hide": false,
              "instant": true,
              "interval": "",
              "legendFormat": "",
              "refId": "C"
            },
            {
              "datasource": {
                "type": "prometheus",
                "uid": "${DS_PROMETHEUS}"
              },
              "exemplar": true,
              "expr": "mtxrWlCMRemoteState{instance='$instance'}",
              "format": "table",
              "hide": false,
              "instant": true,
              "interval": "",
              "legendFormat": "",
              "refId": "D"
            }
          ],
          "title": "Remote CAP",
          "transformations": [
            {
              "id": "seriesToColumns",
              "options": {
                "byField": "mtxrWlCMRemoteIndex"
              }
            },
            {
              "id": "organize",
              "options": {
                "excludeByName": {
                  "Time 1": true,
                  "Time 2": true,
                  "Time 3": true,
                  "Time 4": true,
                  "Value #A": true,
                  "Value #B": true,
                  "Value #D": true,
                  "__name__ 1": true,
                  "__name__ 2": true,
                  "__name__ 3": true,
                  "__name__ 4": true,
                  "instance 1": true,
                  "instance 2": true,
                  "instance 3": true,
                  "instance 4": true,
                  "job 1": true,
                  "job 2": true,
                  "job 3": true,
                  "job 4": true
                },
                "indexByName": {
                  "Time 1": 5,
                  "Time 2": 10,
                  "Time 3": 15,
                  "Time 4": 19,
                  "Value #A": 9,
                  "Value #B": 14,
                  "Value #C": 4,
                  "Value #D": 23,
                  "__name__ 1": 6,
                  "__name__ 2": 11,
                  "__name__ 3": 16,
                  "__name__ 4": 20,
                  "instance 1": 7,
                  "instance 2": 12,
                  "instance 3": 17,
                  "instance 4": 21,
                  "job 1": 8,
                  "job 2": 13,
                  "job 3": 18,
                  "job 4": 22,
                  "mtxrWlCMRemoteAddress": 3,
                  "mtxrWlCMRemoteIndex": 1,
                  "mtxrWlCMRemoteName": 2,
                  "mtxrWlCMRemoteState": 0
                },
                "renameByName": {
                  "Time 1": "",
                  "Time 4": "",
                  "Value #C": "Remote Radios",
                  "instance 4": "",
                  "mtxrWlCMRemoteAddress": "Remote address/port",
                  "mtxrWlCMRemoteIndex": "remote index",
                  "mtxrWlCMRemoteName": "Remote name",
                  "mtxrWlCMRemoteState": "state"
                }
              }
            }
          ],
          "type": "table"
        },
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${DS_PROMETHEUS}"
          },
          "description": "",
          "fieldConfig": {
            "defaults": {
              "color": {
                "mode": "thresholds"
              },
              "custom": {
                "align": "auto",
                "displayMode": "auto"
              },
              "mappings": [],
              "thresholds": {
                "mode": "absolute",
                "steps": [
                  {
                    "color": "green"
                  },
                  {
                    "color": "red",
                    "value": 80
                  }
                ]
              }
            },
            "overrides": [
              {
                "matcher": {
                  "id": "byName",
                  "options": "Index"
                },
                "properties": [
                  {
                    "id": "custom.width",
                    "value": 70
                  }
                ]
              },
              {
                "matcher": {
                  "id": "byName",
                  "options": "Reg Client Count"
                },
                "properties": [
                  {
                    "id": "custom.width",
                    "value": 132
                  }
                ]
              },
              {
                "matcher": {
                  "id": "byName",
                  "options": "Auth clients count"
                },
                "properties": [
                  {
                    "id": "custom.width",
                    "value": 133
                  }
                ]
              },
              {
                "matcher": {
                  "id": "byName",
                  "options": "Interface state"
                },
                "properties": [
                  {
                    "id": "custom.width",
                    "value": 120
                  }
                ]
              }
            ]
          },
          "gridPos": {
            "h": 8,
            "w": 10,
            "x": 14,
            "y": 4
          },
          "id": 1679,
          "options": {
            "footer": {
              "fields": "",
              "reducer": [
                "sum"
              ],
              "show": false
            },
            "showHeader": true,
            "sortBy": []
          },
          "pluginVersion": "8.3.4",
          "targets": [
            {
              "datasource": {
                "type": "prometheus",
                "uid": "${DS_PROMETHEUS}"
              },
              "exemplar": true,
              "expr": "mtxrWlCMState{instance='$instance'}",
              "format": "table",
              "hide": false,
              "instant": true,
              "interval": "",
              "legendFormat": "",
              "refId": "A"
            },
            {
              "datasource": {
                "type": "prometheus",
                "uid": "${DS_PROMETHEUS}"
              },
              "exemplar": true,
              "expr": "mtxrWlCMRegClientCount{instance='$instance'}",
              "format": "table",
              "hide": false,
              "instant": true,
              "interval": "",
              "legendFormat": "",
              "refId": "B"
            },
            {
              "datasource": {
                "type": "prometheus",
                "uid": "${DS_PROMETHEUS}"
              },
              "exemplar": true,
              "expr": "mtxrWlCMChannel{instance='$instance'}",
              "format": "table",
              "hide": false,
              "instant": true,
              "interval": "",
              "legendFormat": "",
              "refId": "C"
            },
            {
              "datasource": {
                "type": "prometheus",
                "uid": "${DS_PROMETHEUS}"
              },
              "exemplar": true,
              "expr": "mtxrWlCMAuthClientCount{instance='$instance'}",
              "format": "table",
              "hide": false,
              "instant": true,
              "interval": "",
              "legendFormat": "",
              "refId": "D"
            },
            {
              "datasource": {
                "type": "prometheus",
                "uid": "${DS_PROMETHEUS}"
              },
              "exemplar": true,
              "expr": "mtxrWlCMRtabSsid{instance='$instance'}",
              "format": "table",
              "hide": false,
              "instant": true,
              "interval": "",
              "legendFormat": "",
              "refId": "E"
            }
          ],
          "title": "CAP interface",
          "transformations": [
            {
              "id": "seriesToColumns",
              "options": {
                "byField": "mtxrWlCMIndex"
              }
            },
            {
              "id": "organize",
              "options": {
                "excludeByName": {
                  "Time 1": true,
                  "Time 2": true,
                  "Time 3": true,
                  "Time 4": true,
                  "Value #A": true,
                  "Value #B": false,
                  "Value #C": true,
                  "__name__ 1": true,
                  "__name__ 2": true,
                  "__name__ 3": true,
                  "__name__ 4": true,
                  "instance 1": true,
                  "instance 2": true,
                  "instance 3": true,
                  "instance 4": true,
                  "job 1": true,
                  "job 2": true,
                  "job 3": true,
                  "job 4": true
                },
                "indexByName": {
                  "Time 1": 1,
                  "Time 2": 7,
                  "Time 3": 13,
                  "Time 4": 19,
                  "Value #A": 6,
                  "Value #B": 11,
                  "Value #C": 18,
                  "Value #D": 12,
                  "__name__ 1": 2,
                  "__name__ 2": 8,
                  "__name__ 3": 14,
                  "__name__ 4": 20,
                  "instance 1": 3,
                  "instance 2": 9,
                  "instance 3": 15,
                  "instance 4": 21,
                  "job 1": 4,
                  "job 2": 10,
                  "job 3": 16,
                  "job 4": 22,
                  "mtxrWlCMChannel": 17,
                  "mtxrWlCMIndex": 0,
                  "mtxrWlCMState": 5
                },
                "renameByName": {
                  "Time 1": "",
                  "Time 4": "",
                  "Value #A": "",
                  "Value #B": "Reg Client Count",
                  "Value #C": "",
                  "Value #D": "Auth clients count",
                  "__name__ 4": "",
                  "instance 4": "",
                  "job 1": "",
                  "job 2": "",
                  "job 4": "",
                  "mtxrWlCMChannel": "Channel for master only",
                  "mtxrWlCMIndex": "Index",
                  "mtxrWlCMState": "Interface state"
                }
              }
            }
          ],
          "type": "table"
        },
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${DS_PROMETHEUS}"
          },
          "description": "Wireless CAPSMAN remote-cap entry count",
          "fieldConfig": {
            "defaults": {
              "color": {
                "mode": "thresholds"
              },
              "mappings": [],
              "thresholds": {
                "mode": "absolute",
                "steps": [
                  {
                    "color": "#299c46"
                  }
                ]
              }
            },
            "overrides": []
          },
          "gridPos": {
            "h": 4,
            "w": 3,
            "x": 0,
            "y": 8
          },
          "id": 1680,
          "options": {
            "colorMode": "value",
            "graphMode": "none",
            "justifyMode": "auto",
            "orientation": "auto",
            "reduceOptions": {
              "calcs": [
                "lastNotNull"
              ],
              "fields": "",
              "values": false
            },
            "text": {},
            "textMode": "auto"
          },
          "pluginVersion": "8.3.4",
          "targets": [
            {
              "datasource": {
                "type": "prometheus",
                "uid": "${DS_PROMETHEUS}"
              },
              "exemplar": true,
              "expr": "mtxrWlCMREntryCount{instance='$instance'}",
              "format": "time_series",
              "hide": false,
              "instant": true,
              "interval": "",
              "legendFormat": "",
              "refId": "A"
            }
          ],
          "title": "remote-cap entry count",
          "type": "stat"
        },
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${DS_PROMETHEUS}"
          },
          "description": "",
          "fieldConfig": {
            "defaults": {
              "color": {
                "mode": "thresholds"
              },
              "custom": {
                "align": "auto",
                "displayMode": "auto"
              },
              "mappings": [],
              "thresholds": {
                "mode": "absolute",
                "steps": [
                  {
                    "color": "green"
                  },
                  {
                    "color": "red",
                    "value": 80
                  }
                ]
              }
            },
            "overrides": [
              {
                "matcher": {
                  "id": "byName",
                  "options": "Mac address"
                },
                "properties": [
                  {
                    "id": "custom.width",
                    "value": 130
                  },
                  {
                    "id": "custom.align",
                    "value": "center"
                  }
                ]
              },
              {
                "matcher": {
                  "id": "byName",
                  "options": "Uptime"
                },
                "properties": [
                  {
                    "id": "custom.align",
                    "value": "center"
                  },
                  {
                    "id": "unit",
                    "value": "timeticks"
                  },
                  {
                    "id": "custom.width",
                    "value": 106
                  }
                ]
              },
              {
                "matcher": {
                  "id": "byName",
                  "options": "Strength"
                },
                "properties": [
                  {
                    "id": "unit",
                    "value": "dBm"
                  },
                  {
                    "id": "custom.displayMode",
                    "value": "lcd-gauge"
                  },
                  {
                    "id": "min",
                    "value": -85
                  },
                  {
                    "id": "max",
                    "value": -30
                  },
                  {
                    "id": "color",
                    "value": {
                      "mode": "continuous-RdYlGr"
                    }
                  },
                  {
                    "id": "custom.width",
                    "value": 250
                  },
                  {
                    "id": "custom.align",
                    "value": "center"
                  }
                ]
              },
              {
                "matcher": {
                  "id": "byName",
                  "options": "Rx Rate"
                },
                "properties": [
                  {
                    "id": "custom.width",
                    "value": 100
                  },
                  {
                    "id": "unit",
                    "value": "bps"
                  },
                  {
                    "id": "custom.align",
                    "value": "center"
                  }
                ]
              },
              {
                "matcher": {
                  "id": "byName",
                  "options": "Rx Bytes"
                },
                "properties": [
                  {
                    "id": "custom.width",
                    "value": 100
                  },
                  {
                    "id": "unit",
                    "value": "bytes"
                  }
                ]
              },
              {
                "matcher": {
                  "id": "byName",
                  "options": "Rx Packets"
                },
                "properties": [
                  {
                    "id": "custom.width",
                    "value": 145
                  }
                ]
              },
              {
                "matcher": {
                  "id": "byName",
                  "options": "Tx Rate"
                },
                "properties": [
                  {
                    "id": "custom.width",
                    "value": 100
                  },
                  {
                    "id": "unit",
                    "value": "bps"
                  },
                  {
                    "id": "custom.align",
                    "value": "center"
                  }
                ]
              },
              {
                "matcher": {
                  "id": "byName",
                  "options": "Tx Bytes"
                },
                "properties": [
                  {
                    "id": "custom.width",
                    "value": 100
                  },
                  {
                    "id": "unit",
                    "value": "bytes"
                  }
                ]
              },
              {
                "matcher": {
                  "id": "byName",
                  "options": "SSID"
                },
                "properties": [
                  {
                    "id": "custom.width"
                  },
                  {
                    "id": "custom.align",
                    "value": "center"
                  }
                ]
              },
              {
                "matcher": {
                  "id": "byName",
                  "options": "interface index"
                },
                "properties": [
                  {
                    "id": "custom.width",
                    "value": 115
                  },
                  {
                    "id": "custom.align",
                    "value": "center"
                  }
                ]
              }
            ]
          },
          "gridPos": {
            "h": 7,
            "w": 24,
            "x": 0,
            "y": 12
          },
          "id": 1678,
          "options": {
            "footer": {
              "fields": "",
              "reducer": [
                "sum"
              ],
              "show": false
            },
            "showHeader": true,
            "sortBy": [
              {
                "desc": true,
                "displayName": "SSID"
              }
            ]
          },
          "pluginVersion": "8.3.4",
          "targets": [
            {
              "datasource": {
                "type": "prometheus",
                "uid": "${DS_PROMETHEUS}"
              },
              "exemplar": true,
              "expr": "mtxrWlCMRtabAddr{instance='$instance'}",
              "format": "table",
              "hide": false,
              "instant": true,
              "interval": "",
              "legendFormat": "",
              "refId": "A"
            },
            {
              "datasource": {
                "type": "prometheus",
                "uid": "${DS_PROMETHEUS}"
              },
              "exemplar": true,
              "expr": "mtxrWlCMRtabEapIdent{instance='$instance'}",
              "format": "table",
              "hide": false,
              "instant": true,
              "interval": "",
              "legendFormat": "",
              "refId": "B"
            },
            {
              "datasource": {
                "type": "prometheus",
                "uid": "${DS_PROMETHEUS}"
              },
              "exemplar": true,
              "expr": "mtxrWlCMRtabRxBytes{instance='$instance'}",
              "format": "table",
              "hide": false,
              "instant": true,
              "interval": "",
              "legendFormat": "",
              "refId": "C"
            },
            {
              "datasource": {
                "type": "prometheus",
                "uid": "${DS_PROMETHEUS}"
              },
              "exemplar": true,
              "expr": "mtxrWlCMRtabRxPackets{instance='$instance'}",
              "format": "table",
              "hide": false,
              "instant": true,
              "interval": "",
              "legendFormat": "",
              "refId": "D"
            },
            {
              "datasource": {
                "type": "prometheus",
                "uid": "${DS_PROMETHEUS}"
              },
              "exemplar": true,
              "expr": "mtxrWlCMRtabRxRate{instance='$instance'}",
              "format": "table",
              "hide": false,
              "instant": true,
              "interval": "",
              "legendFormat": "",
              "refId": "E"
            },
            {
              "datasource": {
                "type": "prometheus",
                "uid": "${DS_PROMETHEUS}"
              },
              "exemplar": true,
              "expr": "mtxrWlCMRtabRxStrength{instance='$instance'}",
              "format": "table",
              "hide": false,
              "instant": true,
              "interval": "",
              "legendFormat": "",
              "refId": "F"
            },
            {
              "datasource": {
                "type": "prometheus",
                "uid": "${DS_PROMETHEUS}"
              },
              "exemplar": true,
              "expr": "mtxrWlCMRtabSsid{instance='$instance'}",
              "format": "table",
              "hide": false,
              "instant": true,
              "interval": "",
              "legendFormat": "",
              "refId": "G"
            },
            {
              "datasource": {
                "type": "prometheus",
                "uid": "${DS_PROMETHEUS}"
              },
              "exemplar": true,
              "expr": "mtxrWlCMRtabTxBytes{instance='$instance'}",
              "format": "table",
              "hide": false,
              "instant": true,
              "interval": "",
              "legendFormat": "",
              "refId": "H"
            },
            {
              "datasource": {
                "type": "prometheus",
                "uid": "${DS_PROMETHEUS}"
              },
              "exemplar": true,
              "expr": "mtxrWlCMRtabTxPackets{instance='$instance'}",
              "format": "table",
              "hide": false,
              "instant": true,
              "interval": "",
              "legendFormat": "",
              "refId": "I"
            },
            {
              "datasource": {
                "type": "prometheus",
                "uid": "${DS_PROMETHEUS}"
              },
              "exemplar": true,
              "expr": "mtxrWlCMRtabTxRate{instance='$instance'}",
              "format": "table",
              "hide": false,
              "instant": true,
              "interval": "",
              "legendFormat": "",
              "refId": "J"
            },
            {
              "datasource": {
                "type": "prometheus",
                "uid": "${DS_PROMETHEUS}"
              },
              "exemplar": true,
              "expr": "mtxrWlCMRtabTxStrength{instance='$instance'}",
              "format": "table",
              "hide": false,
              "instant": true,
              "interval": "",
              "legendFormat": "",
              "refId": "K"
            },
            {
              "datasource": {
                "type": "prometheus",
                "uid": "${DS_PROMETHEUS}"
              },
              "exemplar": true,
              "expr": "mtxrWlCMRtabUptime{instance='$instance'}",
              "format": "table",
              "hide": false,
              "instant": true,
              "interval": "",
              "legendFormat": "",
              "refId": "L"
            }
          ],
          "title": "Clients",
          "transformations": [
            {
              "id": "seriesToColumns",
              "options": {
                "byField": "mtxrWlCMRtabAddr"
              }
            },
            {
              "id": "organize",
              "options": {
                "excludeByName": {
                  "Time 1": true,
                  "Time 10": true,
                  "Time 11": true,
                  "Time 12": true,
                  "Time 2": true,
                  "Time 3": true,
                  "Time 4": true,
                  "Time 5": true,
                  "Time 6": true,
                  "Time 7": true,
                  "Time 8": true,
                  "Time 9": true,
                  "Value #A": true,
                  "Value #B": true,
                  "Value #G": true,
                  "Value #I": false,
                  "Value #J": false,
                  "Value #K": true,
                  "__name__ 1": true,
                  "__name__ 10": true,
                  "__name__ 11": true,
                  "__name__ 12": true,
                  "__name__ 2": true,
                  "__name__ 3": true,
                  "__name__ 4": true,
                  "__name__ 5": true,
                  "__name__ 6": true,
                  "__name__ 7": true,
                  "__name__ 8": true,
                  "__name__ 9": true,
                  "instance 1": true,
                  "instance 10": true,
                  "instance 11": true,
                  "instance 12": true,
                  "instance 2": true,
                  "instance 3": true,
                  "instance 4": true,
                  "instance 5": true,
                  "instance 6": true,
                  "instance 7": true,
                  "instance 8": true,
                  "instance 9": true,
                  "job 1": true,
                  "job 10": true,
                  "job 11": true,
                  "job 12": true,
                  "job 2": true,
                  "job 3": true,
                  "job 4": true,
                  "job 5": true,
                  "job 6": true,
                  "job 7": true,
                  "job 8": true,
                  "job 9": true,
                  "mtxrWlCMRtabAddr": false,
                  "mtxrWlCMRtabIface 10": true,
                  "mtxrWlCMRtabIface 11": true,
                  "mtxrWlCMRtabIface 12": true,
                  "mtxrWlCMRtabIface 2": true,
                  "mtxrWlCMRtabIface 3": true,
                  "mtxrWlCMRtabIface 4": true,
                  "mtxrWlCMRtabIface 5": true,
                  "mtxrWlCMRtabIface 6": true,
                  "mtxrWlCMRtabIface 7": true,
                  "mtxrWlCMRtabIface 8": true,
                  "mtxrWlCMRtabIface 9": true,
                  "mtxrWlCMRtabSsid": false
                },
                "indexByName": {
                  "Time 1": 12,
                  "Time 10": 59,
                  "Time 11": 64,
                  "Time 12": 69,
                  "Time 2": 17,
                  "Time 3": 23,
                  "Time 4": 28,
                  "Time 5": 33,
                  "Time 6": 38,
                  "Time 7": 43,
                  "Time 8": 49,
                  "Time 9": 54,
                  "Value #A": 16,
                  "Value #B": 22,
                  "Value #C": 7,
                  "Value #D": 9,
                  "Value #E": 5,
                  "Value #F": 4,
                  "Value #G": 48,
                  "Value #H": 8,
                  "Value #I": 10,
                  "Value #J": 6,
                  "Value #K": 11,
                  "Value #L": 3,
                  "__name__ 1": 13,
                  "__name__ 10": 60,
                  "__name__ 11": 65,
                  "__name__ 12": 70,
                  "__name__ 2": 18,
                  "__name__ 3": 24,
                  "__name__ 4": 29,
                  "__name__ 5": 34,
                  "__name__ 6": 39,
                  "__name__ 7": 44,
                  "__name__ 8": 50,
                  "__name__ 9": 55,
                  "instance 1": 14,
                  "instance 10": 61,
                  "instance 11": 66,
                  "instance 12": 71,
                  "instance 2": 19,
                  "instance 3": 25,
                  "instance 4": 30,
                  "instance 5": 35,
                  "instance 6": 40,
                  "instance 7": 45,
                  "instance 8": 51,
                  "instance 9": 56,
                  "job 1": 15,
                  "job 10": 62,
                  "job 11": 67,
                  "job 12": 72,
                  "job 2": 20,
                  "job 3": 26,
                  "job 4": 31,
                  "job 5": 36,
                  "job 6": 41,
                  "job 7": 46,
                  "job 8": 52,
                  "job 9": 57,
                  "mtxrWlCMRtabAddr": 2,
                  "mtxrWlCMRtabIface 1": 1,
                  "mtxrWlCMRtabIface 10": 63,
                  "mtxrWlCMRtabIface 11": 68,
                  "mtxrWlCMRtabIface 12": 73,
                  "mtxrWlCMRtabIface 2": 21,
                  "mtxrWlCMRtabIface 3": 27,
                  "mtxrWlCMRtabIface 4": 32,
                  "mtxrWlCMRtabIface 5": 37,
                  "mtxrWlCMRtabIface 6": 42,
                  "mtxrWlCMRtabIface 7": 47,
                  "mtxrWlCMRtabIface 8": 53,
                  "mtxrWlCMRtabIface 9": 58,
                  "mtxrWlCMRtabSsid": 0
                },
                "renameByName": {
                  "Time 1": "",
                  "Value #C": "Rx Bytes",
                  "Value #D": "Rx Packets",
                  "Value #E": "Rx Rate",
                  "Value #F": "Strength",
                  "Value #H": "Tx Bytes",
                  "Value #I": "Tx Packets",
                  "Value #J": "Tx Rate",
                  "Value #K": "Tx Strength",
                  "Value #L": "Uptime",
                  "mtxrWlCMRtabAddr": "Mac address",
                  "mtxrWlCMRtabIface 1": "interface index",
                  "mtxrWlCMRtabSsid": "SSID"
                }
              }
            },
            {
              "id": "sortBy",
              "options": {
                "fields": {},
                "sort": [
                  {
                    "field": "SSID"
                  }
                ]
              }
            }
          ],
          "type": "table"
        }
      ],
      "targets": [
        {
          "datasource": {
            "type": "prometheus",
            "uid": "PBFA97CFB590B2093"
          },
          "refId": "A"
        }
      ],
      "title": "CAPsMAN",
      "type": "row"
    },
    {
      "collapsed": true,
      "datasource": {
        "type": "prometheus",
        "uid": "PBFA97CFB590B2093"
      },
      "gridPos": {
        "h": 1,
        "w": 24,
        "x": 0,
        "y": 53
      },
      "id": 1705,
      "panels": [
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${DS_PROMETHEUS}"
          },
          "description": "",
          "fieldConfig": {
            "defaults": {
              "color": {
                "mode": "thresholds"
              },
              "mappings": [],
              "thresholds": {
                "mode": "absolute",
                "steps": [
                  {
                    "color": "#299c46"
                  }
                ]
              },
              "unit": "none"
            },
            "overrides": []
          },
          "gridPos": {
            "h": 4,
            "w": 4,
            "x": 0,
            "y": 5
          },
          "id": 1713,
          "options": {
            "colorMode": "value",
            "graphMode": "none",
            "justifyMode": "center",
            "orientation": "auto",
            "reduceOptions": {
              "calcs": [
                "lastNotNull"
              ],
              "fields": "",
              "values": false
            },
            "text": {},
            "textMode": "name"
          },
          "pluginVersion": "8.3.4",
          "targets": [
            {
              "datasource": {
                "type": "prometheus",
                "uid": "${DS_PROMETHEUS}"
              },
              "exemplar": true,
              "expr": "mtxrWl60GSsid{instance='$instance'}",
              "format": "time_series",
              "hide": false,
              "instant": true,
              "interval": "",
              "legendFormat": "{{mtxrWl60GSsid}}",
              "refId": "A"
            }
          ],
          "title": "ssid",
          "type": "stat"
        },
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${DS_PROMETHEUS}"
          },
          "description": "",
          "fieldConfig": {
            "defaults": {
              "color": {
                "mode": "thresholds"
              },
              "mappings": [],
              "thresholds": {
                "mode": "absolute",
                "steps": [
                  {
                    "color": "#299c46"
                  }
                ]
              },
              "unit": "none"
            },
            "overrides": []
          },
          "gridPos": {
            "h": 4,
            "w": 4,
            "x": 4,
            "y": 5
          },
          "id": 1706,
          "options": {
            "colorMode": "value",
            "graphMode": "none",
            "justifyMode": "center",
            "orientation": "auto",
            "reduceOptions": {
              "calcs": [
                "lastNotNull"
              ],
              "fields": "",
              "values": false
            },
            "text": {},
            "textMode": "auto"
          },
          "pluginVersion": "8.3.4",
          "targets": [
            {
              "datasource": {
                "type": "prometheus",
                "uid": "${DS_PROMETHEUS}"
              },
              "exemplar": true,
              "expr": "mtxrWl60GFreq{instance='$instance'}",
              "format": "time_series",
              "hide": false,
              "instant": true,
              "interval": "",
              "legendFormat": "",
              "refId": "A"
            }
          ],
          "title": "Frequency",
          "type": "stat"
        },
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${DS_PROMETHEUS}"
          },
          "description": "",
          "fieldConfig": {
            "defaults": {
              "color": {
                "mode": "thresholds"
              },
              "mappings": [
                {
                  "options": {
                    "0": {
                      "index": 0,
                      "text": "disconnected"
                    },
                    "1": {
                      "index": 1,
                      "text": "connected"
                    }
                  },
                  "type": "value"
                }
              ],
              "thresholds": {
                "mode": "absolute",
                "steps": [
                  {
                    "color": "dark-red"
                  },
                  {
                    "color": "#299c46",
                    "value": 1
                  }
                ]
              },
              "unit": "none"
            },
            "overrides": []
          },
          "gridPos": {
            "h": 4,
            "w": 4,
            "x": 8,
            "y": 5
          },
          "id": 1707,
          "options": {
            "colorMode": "value",
            "graphMode": "none",
            "justifyMode": "center",
            "orientation": "auto",
            "reduceOptions": {
              "calcs": [
                "lastNotNull"
              ],
              "fields": "",
              "values": false
            },
            "text": {},
            "textMode": "auto"
          },
          "pluginVersion": "8.3.4",
          "targets": [
            {
              "datasource": {
                "type": "prometheus",
                "uid": "${DS_PROMETHEUS}"
              },
              "exemplar": true,
              "expr": "mtxrWl60GConnected{instance='$instance'}",
              "format": "time_series",
              "hide": false,
              "instant": true,
              "interval": "",
              "legendFormat": "",
              "refId": "A"
            }
          ],
          "title": "Connected",
          "type": "stat"
        },
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${DS_PROMETHEUS}"
          },
          "description": "",
          "fieldConfig": {
            "defaults": {
              "color": {
                "mode": "thresholds"
              },
              "mappings": [
                {
                  "options": {
                    "0": {
                      "index": 0,
                      "text": "AP Bridge"
                    },
                    "1": {
                      "index": 1,
                      "text": "Station Bridge"
                    },
                    "2": {
                      "index": 2,
                      "text": "Sniff"
                    },
                    "3": {
                      "index": 3,
                      "text": "Bridge"
                    }
                  },
                  "type": "value"
                }
              ],
              "thresholds": {
                "mode": "absolute",
                "steps": [
                  {
                    "color": "#299c46"
                  }
                ]
              },
              "unit": "none"
            },
            "overrides": []
          },
          "gridPos": {
            "h": 4,
            "w": 4,
            "x": 12,
            "y": 5
          },
          "id": 1709,
          "options": {
            "colorMode": "value",
            "graphMode": "none",
            "justifyMode": "center",
            "orientation": "auto",
            "reduceOptions": {
              "calcs": [
                "lastNotNull"
              ],
              "fields": "",
              "values": false
            },
            "text": {},
            "textMode": "auto"
          },
          "pluginVersion": "8.3.4",
          "targets": [
            {
              "datasource": {
                "type": "prometheus",
                "uid": "${DS_PROMETHEUS}"
              },
              "exemplar": true,
              "expr": "mtxrWl60GMode{instance='$instance'}",
              "format": "time_series",
              "hide": false,
              "instant": true,
              "interval": "",
              "legendFormat": "",
              "refId": "A"
            }
          ],
          "title": "Mode",
          "type": "stat"
        },
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${DS_PROMETHEUS}"
          },
          "description": "",
          "fieldConfig": {
            "defaults": {
              "color": {
                "mode": "palette-classic"
              },
              "custom": {
                "axisLabel": "",
                "axisPlacement": "auto",
                "barAlignment": 0,
                "drawStyle": "line",
                "fillOpacity": 0,
                "gradientMode": "none",
                "hideFrom": {
                  "legend": false,
                  "tooltip": false,
                  "viz": false
                },
                "lineInterpolation": "linear",
                "lineWidth": 1,
                "pointSize": 5,
                "scaleDistribution": {
                  "type": "linear"
                },
                "showPoints": "auto",
                "spanNulls": false,
                "stacking": {
                  "group": "A",
                  "mode": "none"
                },
                "thresholdsStyle": {
                  "mode": "off"
                }
              },
              "mappings": [],
              "thresholds": {
                "mode": "absolute",
                "steps": [
                  {
                    "color": "#299c46"
                  }
                ]
              },
              "unit": "none"
            },
            "overrides": []
          },
          "gridPos": {
            "h": 8,
            "w": 8,
            "x": 16,
            "y": 5
          },
          "id": 1712,
          "options": {
            "legend": {
              "calcs": [
                "lastNotNull",
                "min",
                "max",
                "mean"
              ],
              "displayMode": "table",
              "placement": "bottom"
            },
            "tooltip": {
              "mode": "single"
            }
          },
          "pluginVersion": "8.2.1",
          "targets": [
            {
              "datasource": {
                "type": "prometheus",
                "uid": "${DS_PROMETHEUS}"
              },
              "exemplar": true,
              "expr": "mtxrWl60GRssi{instance='$instance'}",
              "format": "time_series",
              "hide": false,
              "instant": true,
              "interval": "",
              "legendFormat": "RSSI",
              "refId": "A"
            }
          ],
          "title": "RSSI",
          "type": "timeseries"
        },
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${DS_PROMETHEUS}"
          },
          "description": "",
          "fieldConfig": {
            "defaults": {
              "color": {
                "mode": "thresholds"
              },
              "mappings": [],
              "thresholds": {
                "mode": "absolute",
                "steps": [
                  {
                    "color": "#299c46"
                  }
                ]
              },
              "unit": "none"
            },
            "overrides": []
          },
          "gridPos": {
            "h": 4,
            "w": 2,
            "x": 0,
            "y": 9
          },
          "id": 1710,
          "options": {
            "colorMode": "value",
            "graphMode": "none",
            "justifyMode": "center",
            "orientation": "auto",
            "reduceOptions": {
              "calcs": [
                "lastNotNull"
              ],
              "fields": "",
              "values": false
            },
            "text": {},
            "textMode": "auto"
          },
          "pluginVersion": "8.3.4",
          "targets": [
            {
              "datasource": {
                "type": "prometheus",
                "uid": "${DS_PROMETHEUS}"
              },
              "exemplar": true,
              "expr": "mtxrWl60GPhyRate{instance='$instance'}",
              "format": "time_series",
              "hide": false,
              "instant": true,
              "interval": "",
              "legendFormat": "",
              "refId": "A"
            }
          ],
          "title": "PhyRate",
          "type": "stat"
        },
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${DS_PROMETHEUS}"
          },
          "description": "",
          "fieldConfig": {
            "defaults": {
              "color": {
                "mode": "thresholds"
              },
              "mappings": [],
              "thresholds": {
                "mode": "absolute",
                "steps": [
                  {
                    "color": "#299c46"
                  }
                ]
              },
              "unit": "none"
            },
            "overrides": []
          },
          "gridPos": {
            "h": 4,
            "w": 2,
            "x": 2,
            "y": 9
          },
          "id": 1714,
          "options": {
            "colorMode": "value",
            "graphMode": "none",
            "justifyMode": "center",
            "orientation": "auto",
            "reduceOptions": {
              "calcs": [
                "lastNotNull"
              ],
              "fields": "",
              "values": false
            },
            "text": {},
            "textMode": "auto"
          },
          "pluginVersion": "8.3.4",
          "targets": [
            {
              "datasource": {
                "type": "prometheus",
                "uid": "${DS_PROMETHEUS}"
              },
              "exemplar": true,
              "expr": "mtxrWl60GTxSector{instance='$instance'}",
              "format": "time_series",
              "hide": false,
              "instant": true,
              "interval": "",
              "legendFormat": "",
              "refId": "A"
            }
          ],
          "title": "TxSector",
          "type": "stat"
        },
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${DS_PROMETHEUS}"
          },
          "description": "",
          "fieldConfig": {
            "defaults": {
              "color": {
                "mode": "thresholds"
              },
              "mappings": [],
              "thresholds": {
                "mode": "absolute",
                "steps": [
                  {
                    "color": "#299c46"
                  }
                ]
              },
              "unit": "none"
            },
            "overrides": []
          },
          "gridPos": {
            "h": 4,
            "w": 2,
            "x": 4,
            "y": 9
          },
          "id": 1716,
          "options": {
            "colorMode": "value",
            "graphMode": "none",
            "justifyMode": "center",
            "orientation": "auto",
            "reduceOptions": {
              "calcs": [
                "lastNotNull"
              ],
              "fields": "",
              "values": false
            },
            "text": {},
            "textMode": "auto"
          },
          "pluginVersion": "8.3.4",
          "targets": [
            {
              "datasource": {
                "type": "prometheus",
                "uid": "${DS_PROMETHEUS}"
              },
              "exemplar": true,
              "expr": "mtxrWl60GSignal{instance='$instance'}",
              "format": "time_series",
              "hide": false,
              "instant": true,
              "interval": "",
              "legendFormat": "",
              "refId": "A"
            }
          ],
          "title": "Signal",
          "type": "stat"
        },
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${DS_PROMETHEUS}"
          },
          "description": "",
          "fieldConfig": {
            "defaults": {
              "color": {
                "mode": "thresholds"
              },
              "mappings": [],
              "thresholds": {
                "mode": "absolute",
                "steps": [
                  {
                    "color": "#299c46"
                  }
                ]
              },
              "unit": "none"
            },
            "overrides": []
          },
          "gridPos": {
            "h": 4,
            "w": 2,
            "x": 6,
            "y": 9
          },
          "id": 1715,
          "options": {
            "colorMode": "value",
            "graphMode": "none",
            "justifyMode": "center",
            "orientation": "auto",
            "reduceOptions": {
              "calcs": [
                "lastNotNull"
              ],
              "fields": "/.*/",
              "values": false
            },
            "text": {},
            "textMode": "value_and_name"
          },
          "pluginVersion": "8.3.4",
          "targets": [
            {
              "datasource": {
                "type": "prometheus",
                "uid": "${DS_PROMETHEUS}"
              },
              "exemplar": true,
              "expr": "mtxrWl60GTxSectorInfo{instance='$instance'}",
              "format": "time_series",
              "hide": false,
              "instant": true,
              "interval": "",
              "legendFormat": "",
              "refId": "A"
            }
          ],
          "title": "TxSectorInfo",
          "type": "stat"
        },
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${DS_PROMETHEUS}"
          },
          "description": "Modulation and Coding Scheme",
          "fieldConfig": {
            "defaults": {
              "color": {
                "mode": "thresholds"
              },
              "mappings": [],
              "thresholds": {
                "mode": "absolute",
                "steps": [
                  {
                    "color": "#299c46"
                  }
                ]
              },
              "unit": "none"
            },
            "overrides": []
          },
          "gridPos": {
            "h": 4,
            "w": 4,
            "x": 8,
            "y": 9
          },
          "id": 1708,
          "options": {
            "colorMode": "value",
            "graphMode": "none",
            "justifyMode": "center",
            "orientation": "auto",
            "reduceOptions": {
              "calcs": [
                "lastNotNull"
              ],
              "fields": "",
              "values": false
            },
            "text": {},
            "textMode": "auto"
          },
          "pluginVersion": "8.3.4",
          "targets": [
            {
              "datasource": {
                "type": "prometheus",
                "uid": "${DS_PROMETHEUS}"
              },
              "exemplar": true,
              "expr": "mtxrWl60GMcs{instance='$instance'}",
              "format": "time_series",
              "hide": false,
              "instant": true,
              "interval": "",
              "legendFormat": "",
              "refId": "A"
            }
          ],
          "title": "MCS (Modulation and Coding Scheme)",
          "type": "stat"
        },
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${DS_PROMETHEUS}"
          },
          "description": "",
          "fieldConfig": {
            "defaults": {
              "color": {
                "mode": "thresholds"
              },
              "mappings": [],
              "thresholds": {
                "mode": "absolute",
                "steps": [
                  {
                    "color": "#299c46"
                  }
                ]
              },
              "unit": "none"
            },
            "overrides": []
          },
          "gridPos": {
            "h": 4,
            "w": 4,
            "x": 12,
            "y": 9
          },
          "id": 1711,
          "options": {
            "colorMode": "value",
            "graphMode": "none",
            "justifyMode": "center",
            "orientation": "auto",
            "reduceOptions": {
              "calcs": [
                "lastNotNull"
              ],
              "fields": "",
              "values": false
            },
            "text": {},
            "textMode": "name"
          },
          "pluginVersion": "8.3.4",
          "targets": [
            {
              "datasource": {
                "type": "prometheus",
                "uid": "${DS_PROMETHEUS}"
              },
              "exemplar": true,
              "expr": "mtxrWl60GRemote{instance='$instance'}",
              "format": "time_series",
              "hide": false,
              "instant": true,
              "interval": "",
              "legendFormat": "{{mtxrWl60GRemote}}",
              "refId": "A"
            }
          ],
          "title": "Remote MAC",
          "type": "stat"
        }
      ],
      "targets": [
        {
          "datasource": {
            "type": "prometheus",
            "uid": "PBFA97CFB590B2093"
          },
          "refId": "A"
        }
      ],
      "title": "W60G",
      "type": "row"
    },
    {
      "collapsed": true,
      "datasource": {
        "type": "prometheus",
        "uid": "PBFA97CFB590B2093"
      },
      "gridPos": {
        "h": 1,
        "w": 24,
        "x": 0,
        "y": 54
      },
      "id": 1673,
      "panels": [
        {
          "aliasColors": {
            "CCQ - 1": "#ff2e63",
            "CCQ - 2": "#08d9d6",
            "CCQ - Tilda": "#ff2e63",
            "Noise - 1": "#ff2e63",
            "Noise - 2": "#08d9d6",
            "Noise - Tilda": "light-blue",
            "Noise - Tilda_5": "dark-purple",
            "TX CCQ - Tilda": "#ff2e63"
          },
          "bars": false,
          "dashLength": 10,
          "dashes": false,
          "datasource": {
            "type": "prometheus",
            "uid": "${DS_PROMETHEUS}"
          },
          "description": "Signal Strength: signal strength in dBm (if first ppp-client modem supports)\n\nModem Signal: signal EC/IO in dB (if first ppp-client modem supports)",
          "fill": 1,
          "fillGradient": 0,
          "gridPos": {
            "h": 7,
            "w": 6,
            "x": 0,
            "y": 6
          },
          "hiddenSeries": false,
          "id": 1640,
          "legend": {
            "alignAsTable": true,
            "avg": true,
            "current": true,
            "hideZero": true,
            "max": true,
            "min": true,
            "rightSide": false,
            "show": true,
            "total": false,
            "values": true
          },
          "lines": true,
          "linewidth": 1,
          "links": [],
          "maxPerRow": 2,
          "nullPointMode": "connected",
          "options": {
            "alertThreshold": true
          },
          "percentage": false,
          "pluginVersion": "8.3.4",
          "pointradius": 2,
          "points": false,
          "renderer": "flot",
          "repeatDirection": "h",
          "seriesOverrides": [
            {
              "alias": "2",
              "yaxis": 1
            },
            {
              "alias": "mtxrWlApNoiseFloor{instance=\"192.168.5.1\", job=\"Mikrotik\", mtxrWlApIndex=\"2\"}",
              "yaxis": 2
            },
            {
              "alias": "mtxrWlApNoiseFloor{instance=\"192.168.5.1\", job=\"Mikrotik\", mtxrWlApIndex=\"11\"}",
              "yaxis": 2
            },
            {
              "alias": "mtxrWlApNoiseFloor{instance=\"192.168.5.1\", job=\"Mikrotik\", mtxrWlApIndex=\"1\"}",
              "yaxis": 2
            },
            {
              "alias": "Noise 1",
              "yaxis": 2
            },
            {
              "alias": "Noise 11",
              "yaxis": 2
            },
            {
              "alias": "Noise 2",
              "yaxis": 2
            },
            {
              "alias": "Noise - 2",
              "yaxis": 2
            },
            {
              "alias": "Noise - 11",
              "yaxis": 2
            },
            {
              "alias": "Noise - 1",
              "yaxis": 2
            },
            {
              "alias": "Noise - Tilda",
              "yaxis": 2
            },
            {
              "alias": "Noise - Tilda_5",
              "yaxis": 2
            },
            {
              "alias": "Modem Signal",
              "yaxis": 2
            }
          ],
          "spaceLength": 10,
          "stack": false,
          "steppedLine": false,
          "targets": [
            {
              "datasource": {
                "type": "prometheus",
                "uid": "${DS_PROMETHEUS}"
              },
              "exemplar": true,
              "expr": "mtxrWirelessModemSignalStrength{instance='$instance'}",
              "hide": false,
              "interval": "",
              "legendFormat": "Signal Strength",
              "refId": "A"
            },
            {
              "datasource": {
                "type": "prometheus",
                "uid": "${DS_PROMETHEUS}"
              },
              "exemplar": true,
              "expr": "mtxrWirelessModemSignalECIO{instance='$instance'}",
              "hide": false,
              "interval": "",
              "legendFormat": "Modem Signal",
              "refId": "B"
            }
          ],
          "thresholds": [],
          "timeRegions": [],
          "title": "Modem",
          "tooltip": {
            "shared": true,
            "sort": 0,
            "value_type": "individual"
          },
          "type": "graph",
          "xaxis": {
            "mode": "time",
            "show": true,
            "values": []
          },
          "yaxes": [
            {
              "format": "dBm",
              "label": "",
              "logBase": 1,
              "show": true
            },
            {
              "format": "dB",
              "label": "",
              "logBase": 1,
              "show": true
            }
          ],
          "yaxis": {
            "align": true,
            "alignLevel": 0
          }
        },
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${DS_PROMETHEUS}"
          },
          "description": "",
          "fieldConfig": {
            "defaults": {
              "color": {
                "mode": "thresholds"
              },
              "mappings": [],
              "thresholds": {
                "mode": "absolute",
                "steps": [
                  {
                    "color": "#299c46"
                  }
                ]
              },
              "unit": "s"
            },
            "overrides": []
          },
          "gridPos": {
            "h": 7,
            "w": 4,
            "x": 6,
            "y": 6
          },
          "id": 1674,
          "options": {
            "colorMode": "value",
            "graphMode": "none",
            "justifyMode": "auto",
            "orientation": "auto",
            "reduceOptions": {
              "calcs": [
                "lastNotNull"
              ],
              "fields": "",
              "values": false
            },
            "text": {},
            "textMode": "auto"
          },
          "pluginVersion": "8.3.4",
          "targets": [
            {
              "datasource": {
                "type": "prometheus",
                "uid": "${DS_PROMETHEUS}"
              },
              "exemplar": true,
              "expr": "mtxrUSBPowerReset{instance='$instance'}",
              "hide": false,
              "instant": true,
              "interval": "",
              "legendFormat": "",
              "refId": "A"
            }
          ],
          "title": "USB Power Reset",
          "type": "stat"
        }
      ],
      "targets": [
        {
          "datasource": {
            "type": "prometheus",
            "uid": "PBFA97CFB590B2093"
          },
          "refId": "A"
        }
      ],
      "title": "Modem",
      "type": "row"
    },
    {
      "collapsed": true,
      "datasource": {
        "type": "prometheus",
        "uid": "PBFA97CFB590B2093"
      },
      "gridPos": {
        "h": 1,
        "w": 24,
        "x": 0,
        "y": 55
      },
      "id": 1281,
      "panels": [
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${DS_PROMETHEUS}"
          },
          "description": "",
          "fieldConfig": {
            "defaults": {
              "color": {
                "mode": "palette-classic"
              },
              "custom": {
                "axisLabel": "",
                "axisPlacement": "auto",
                "barAlignment": 0,
                "drawStyle": "line",
                "fillOpacity": 50,
                "gradientMode": "opacity",
                "hideFrom": {
                  "legend": false,
                  "tooltip": false,
                  "viz": false
                },
                "lineInterpolation": "smooth",
                "lineWidth": 2,
                "pointSize": 5,
                "scaleDistribution": {
                  "type": "linear"
                },
                "showPoints": "never",
                "spanNulls": false,
                "stacking": {
                  "group": "A",
                  "mode": "none"
                },
                "thresholdsStyle": {
                  "mode": "off"
                }
              },
              "mappings": [],
              "min": 0,
              "thresholds": {
                "mode": "absolute",
                "steps": [
                  {
                    "color": "green"
                  }
                ]
              },
              "unit": "Bps"
            },
            "overrides": []
          },
          "gridPos": {
            "h": 6,
            "w": 12,
            "x": 0,
            "y": 7
          },
          "id": 1268,
          "links": [],
          "options": {
            "legend": {
              "calcs": [
                "mean",
                "lastNotNull",
                "max"
              ],
              "displayMode": "table",
              "placement": "right"
            },
            "tooltip": {
              "mode": "multi"
            }
          },
          "pluginVersion": "8.2.1",
          "repeatDirection": "h",
          "targets": [
            {
              "datasource": {
                "type": "prometheus",
                "uid": "${DS_PROMETHEUS}"
              },
              "exemplar": true,
              "expr": "(irate(mtxrQueueSimpleBytesIn{instance='$instance'}[$__rate_interval])*on(mtxrQueueSimpleIndex)group_left(mtxrQueueSimpleName)mtxrQueueSimpleName{instance='$instance'})*8 ",
              "instant": false,
              "interval": "",
              "legendFormat": "In - {{mtxrQueueSimpleName}}",
              "refId": "A"
            },
            {
              "datasource": {
                "type": "prometheus",
                "uid": "${DS_PROMETHEUS}"
              },
              "exemplar": true,
              "expr": "(irate(mtxrQueueSimpleBytesOut{instance='$instance'}[$__rate_interval])*on(mtxrQueueSimpleIndex)group_left(mtxrQueueSimpleName)mtxrQueueSimpleName{instance='$instance'})*8",
              "instant": false,
              "interval": "",
              "legendFormat": "Out - {{mtxrQueueSimpleName}}",
              "refId": "B"
            },
            {
              "datasource": {
                "type": "prometheus",
                "uid": "${DS_PROMETHEUS}"
              },
              "exemplar": true,
              "expr": "(mtxrQueueSimplePCQQueuesIn{instance='$instance'}*on(mtxrQueueSimpleIndex)group_left(mtxrQueueSimpleName)mtxrQueueSimpleName{instance='$instance'})",
              "hide": false,
              "instant": false,
              "interval": "",
              "intervalFactor": 1,
              "legendFormat": "PCQ In - {{mtxrQueueSimpleName}}",
              "refId": "D"
            },
            {
              "datasource": {
                "type": "prometheus",
                "uid": "${DS_PROMETHEUS}"
              },
              "exemplar": true,
              "expr": "(mtxrQueueSimplePCQQueuesOut{instance='$instance'}*on(mtxrQueueSimpleIndex)group_left(mtxrQueueSimpleName)mtxrQueueSimpleName{instance='$instance'})",
              "hide": false,
              "instant": false,
              "interval": "",
              "intervalFactor": 1,
              "legendFormat": "PCQ Out - {{mtxrQueueSimpleName}}",
              "refId": "C"
            }
          ],
          "title": "All Simple Queue",
          "type": "timeseries"
        },
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${DS_PROMETHEUS}"
          },
          "description": "Showing values > 0",
          "fieldConfig": {
            "defaults": {
              "color": {
                "mode": "palette-classic"
              },
              "custom": {
                "axisLabel": "",
                "axisPlacement": "auto",
                "barAlignment": 0,
                "drawStyle": "line",
                "fillOpacity": 50,
                "gradientMode": "opacity",
                "hideFrom": {
                  "legend": false,
                  "tooltip": false,
                  "viz": false
                },
                "lineInterpolation": "smooth",
                "lineWidth": 2,
                "pointSize": 5,
                "scaleDistribution": {
                  "type": "linear"
                },
                "showPoints": "never",
                "spanNulls": false,
                "stacking": {
                  "group": "A",
                  "mode": "none"
                },
                "thresholdsStyle": {
                  "mode": "off"
                }
              },
              "mappings": [],
              "min": 0,
              "thresholds": {
                "mode": "absolute",
                "steps": [
                  {
                    "color": "green"
                  },
                  {
                    "color": "red",
                    "value": 80
                  }
                ]
              },
              "unit": "Bps"
            },
            "overrides": []
          },
          "gridPos": {
            "h": 6,
            "w": 12,
            "x": 0,
            "y": 13
          },
          "id": 1282,
          "links": [],
          "options": {
            "legend": {
              "calcs": [
                "mean",
                "lastNotNull",
                "max"
              ],
              "displayMode": "table",
              "placement": "right"
            },
            "tooltip": {
              "mode": "single"
            }
          },
          "pluginVersion": "8.2.1",
          "repeat": "queuesimple_name",
          "repeatDirection": "h",
          "targets": [
            {
              "datasource": {
                "type": "prometheus",
                "uid": "${DS_PROMETHEUS}"
              },
              "exemplar": true,
              "expr": "(irate(mtxrQueueSimpleBytesIn{instance='$instance'}[$__rate_interval])*on(mtxrQueueSimpleIndex)group_left(mtxrQueueSimpleName)mtxrQueueSimpleName{mtxrQueueSimpleName='$queuesimple_name', instance='$instance'})*8",
              "instant": false,
              "interval": "",
              "legendFormat": "In",
              "refId": "A"
            },
            {
              "datasource": {
                "type": "prometheus",
                "uid": "${DS_PROMETHEUS}"
              },
              "exemplar": true,
              "expr": "(irate(mtxrQueueSimpleBytesOut{instance='$instance'}[$__rate_interval])*on(mtxrQueueSimpleIndex)group_left(mtxrQueueSimpleName)mtxrQueueSimpleName{mtxrQueueSimpleName='$queuesimple_name', instance='$instance'})*8",
              "instant": false,
              "interval": "",
              "legendFormat": "Out",
              "refId": "B"
            },
            {
              "datasource": {
                "type": "prometheus",
                "uid": "${DS_PROMETHEUS}"
              },
              "exemplar": true,
              "expr": "(irate(mtxrQueueSimpleDroppedIn{instance='$instance'}[$__rate_interval])*on(mtxrQueueSimpleIndex)group_left(mtxrQueueSimpleName)mtxrQueueSimpleName{mtxrQueueSimpleName='$queuesimple_name', instance='$instance'})",
              "format": "time_series",
              "hide": false,
              "interval": "",
              "legendFormat": "Dropped In",
              "refId": "C"
            },
            {
              "datasource": {
                "type": "prometheus",
                "uid": "${DS_PROMETHEUS}"
              },
              "exemplar": true,
              "expr": "(irate(mtxrQueueSimpleDroppedOut{instance='$instance'}[$__rate_interval])*on(mtxrQueueSimpleIndex)group_left(mtxrQueueSimpleName)mtxrQueueSimpleName{mtxrQueueSimpleName='$queuesimple_name', instance='$instance'})",
              "hide": false,
              "interval": "",
              "legendFormat": "Dropped Out ",
              "refId": "D"
            },
            {
              "datasource": {
                "type": "prometheus",
                "uid": "${DS_PROMETHEUS}"
              },
              "exemplar": true,
              "expr": "(mtxrQueueSimplePCQQueuesIn{instance='$instance'}*on(mtxrQueueSimpleIndex)group_left(mtxrQueueSimpleName)mtxrQueueSimpleName{mtxrQueueSimpleName='$queuesimple_name',instance='$instance'})",
              "hide": false,
              "interval": "",
              "legendFormat": "PCQ-In",
              "refId": "E"
            },
            {
              "datasource": {
                "type": "prometheus",
                "uid": "${DS_PROMETHEUS}"
              },
              "exemplar": true,
              "expr": "(mtxrQueueSimplePCQQueuesOut{instance='$instance'}*on(mtxrQueueSimpleIndex)group_left(mtxrQueueSimpleName)mtxrQueueSimpleName{mtxrQueueSimpleName='$queuesimple_name',instance='$instance'})",
              "hide": false,
              "interval": "",
              "legendFormat": "PCQ-Out",
              "refId": "F"
            }
          ],
          "title": "Queue $queuesimple_name",
          "type": "timeseries"
        }
      ],
      "targets": [
        {
          "datasource": {
            "type": "prometheus",
            "uid": "PBFA97CFB590B2093"
          },
          "refId": "A"
        }
      ],
      "title": "Simple Queue (In/Out/Dropped/PCQ)",
      "type": "row"
    },
    {
      "collapsed": true,
      "datasource": {
        "type": "prometheus",
        "uid": "PBFA97CFB590B2093"
      },
      "gridPos": {
        "h": 1,
        "w": 24,
        "x": 0,
        "y": 56
      },
      "id": 1548,
      "panels": [
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${DS_PROMETHEUS}"
          },
          "description": "",
          "fieldConfig": {
            "defaults": {
              "color": {
                "mode": "palette-classic"
              },
              "custom": {
                "axisLabel": "",
                "axisPlacement": "auto",
                "barAlignment": 0,
                "drawStyle": "line",
                "fillOpacity": 50,
                "gradientMode": "opacity",
                "hideFrom": {
                  "legend": false,
                  "tooltip": false,
                  "viz": false
                },
                "lineInterpolation": "smooth",
                "lineWidth": 2,
                "pointSize": 5,
                "scaleDistribution": {
                  "type": "linear"
                },
                "showPoints": "never",
                "spanNulls": false,
                "stacking": {
                  "group": "A",
                  "mode": "none"
                },
                "thresholdsStyle": {
                  "mode": "off"
                }
              },
              "mappings": [],
              "thresholds": {
                "mode": "absolute",
                "steps": [
                  {
                    "color": "green"
                  }
                ]
              },
              "unit": "binBps"
            },
            "overrides": []
          },
          "gridPos": {
            "h": 6,
            "w": 12,
            "x": 0,
            "y": 8
          },
          "id": 1510,
          "links": [],
          "options": {
            "legend": {
              "calcs": [
                "mean",
                "lastNotNull",
                "max"
              ],
              "displayMode": "table",
              "placement": "right"
            },
            "tooltip": {
              "mode": "multi"
            }
          },
          "pluginVersion": "8.2.1",
          "repeatDirection": "h",
          "targets": [
            {
              "datasource": {
                "type": "prometheus",
                "uid": "${DS_PROMETHEUS}"
              },
              "exemplar": true,
              "expr": "(irate(mtxrQueueTreeHCBytes{instance='$instance'}[$__rate_interval])*on(mtxrQueueTreeIndex)group_left(mtxrQueueTreeName)mtxrQueueTreeName{instance='$instance'})*8",
              "instant": false,
              "interval": "",
              "intervalFactor": 1,
              "legendFormat": "Bytes - {{mtxrQueueTreeName}}",
              "refId": "A"
            },
            {
              "datasource": {
                "type": "prometheus",
                "uid": "${DS_PROMETHEUS}"
              },
              "exemplar": true,
              "expr": "(irate(mtxrQueueTreePCQQueues{instance='$instance'}[$__rate_interval])*on(mtxrQueueTreeIndex)group_left(mtxrQueueTreeName)mtxrQueueTreeName{instance='$instance'})",
              "hide": false,
              "instant": false,
              "interval": "",
              "intervalFactor": 1,
              "legendFormat": "PCQ - {{mtxrQueueTreeName}}",
              "refId": "B"
            },
            {
              "datasource": {
                "type": "prometheus",
                "uid": "${DS_PROMETHEUS}"
              },
              "exemplar": true,
              "expr": "(irate(mtxrQueueTreeDropped{instance='$instance'}[$__rate_interval])*on(mtxrQueueTreeIndex)group_left(mtxrQueueTreeName)mtxrQueueTreeName{instance='$instance'})",
              "hide": false,
              "instant": false,
              "interval": "",
              "intervalFactor": 1,
              "legendFormat": "Dropped - {{mtxrQueueTreeName}}",
              "refId": "C"
            },
            {
              "datasource": {
                "type": "prometheus",
                "uid": "${DS_PROMETHEUS}"
              },
              "exemplar": true,
              "expr": "(irate(mtxrQueueTreePackets{instance='$instance'}[$__rate_interval])*on(mtxrQueueTreeIndex)group_left(mtxrQueueTreeName)mtxrQueueTreeName{instance='$instance'})",
              "hide": false,
              "instant": false,
              "interval": "",
              "intervalFactor": 1,
              "legendFormat": "Packets - {{mtxrQueueTreeName}}",
              "refId": "D"
            }
          ],
          "title": "All Tree Queue",
          "type": "timeseries"
        },
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${DS_PROMETHEUS}"
          },
          "description": "",
          "fieldConfig": {
            "defaults": {
              "color": {
                "mode": "palette-classic"
              },
              "custom": {
                "axisLabel": "",
                "axisPlacement": "auto",
                "barAlignment": 0,
                "drawStyle": "line",
                "fillOpacity": 50,
                "gradientMode": "opacity",
                "hideFrom": {
                  "legend": false,
                  "tooltip": false,
                  "viz": false
                },
                "lineInterpolation": "smooth",
                "lineWidth": 2,
                "pointSize": 5,
                "scaleDistribution": {
                  "type": "linear"
                },
                "showPoints": "never",
                "spanNulls": false,
                "stacking": {
                  "group": "A",
                  "mode": "none"
                },
                "thresholdsStyle": {
                  "mode": "off"
                }
              },
              "mappings": [],
              "thresholds": {
                "mode": "absolute",
                "steps": [
                  {
                    "color": "green"
                  }
                ]
              },
              "unit": "binBps"
            },
            "overrides": []
          },
          "gridPos": {
            "h": 6,
            "w": 12,
            "x": 12,
            "y": 8
          },
          "id": 1549,
          "links": [],
          "options": {
            "legend": {
              "calcs": [
                "mean",
                "lastNotNull",
                "max"
              ],
              "displayMode": "table",
              "placement": "right"
            },
            "tooltip": {
              "mode": "single"
            }
          },
          "pluginVersion": "8.2.1",
          "repeat": "queuetree_name",
          "repeatDirection": "h",
          "targets": [
            {
              "datasource": {
                "type": "prometheus",
                "uid": "${DS_PROMETHEUS}"
              },
              "exemplar": true,
              "expr": "(irate(mtxrQueueTreeHCBytes{instance='$instance'}[$__rate_interval])*on(mtxrQueueTreeIndex)group_left(mtxrQueueTreeName)mtxrQueueTreeName{mtxrQueueTreeName='$queuetree_name',instance='$instance'})*8",
              "instant": false,
              "interval": "",
              "intervalFactor": 1,
              "legendFormat": "Bytes",
              "refId": "A"
            },
            {
              "datasource": {
                "type": "prometheus",
                "uid": "${DS_PROMETHEUS}"
              },
              "exemplar": true,
              "expr": "(irate(mtxrQueueTreePCQQueues{instance='$instance'}[$__rate_interval])*on(mtxrQueueTreeIndex)group_left(mtxrQueueTreeName)mtxrQueueTreeName{mtxrQueueTreeName='$queuetree_name',instance='$instance'})",
              "hide": false,
              "instant": false,
              "interval": "",
              "intervalFactor": 1,
              "legendFormat": "PCQ",
              "refId": "B"
            },
            {
              "datasource": {
                "type": "prometheus",
                "uid": "${DS_PROMETHEUS}"
              },
              "exemplar": true,
              "expr": "(irate(mtxrQueueTreeDropped{instance='$instance'}[$__rate_interval])*on(mtxrQueueTreeIndex)group_left(mtxrQueueTreeName)mtxrQueueTreeName{mtxrQueueTreeName='$queuetree_name',instance='$instance'})",
              "hide": false,
              "instant": false,
              "interval": "",
              "intervalFactor": 1,
              "legendFormat": "Dropped",
              "refId": "C"
            },
            {
              "datasource": {
                "type": "prometheus",
                "uid": "${DS_PROMETHEUS}"
              },
              "exemplar": true,
              "expr": "(irate(mtxrQueueTreePackets{instance='$instance'}[$__rate_interval])*on(mtxrQueueTreeIndex)group_left(mtxrQueueTreeName)mtxrQueueTreeName{mtxrQueueTreeName='$queuetree_name',instance='$instance'})",
              "hide": false,
              "instant": false,
              "interval": "",
              "legendFormat": "Packets",
              "refId": "E"
            }
          ],
          "title": "Tree Queue $queuetree_name / $queuetree_parent / $queuetree_flow",
          "type": "timeseries"
        }
      ],
      "targets": [
        {
          "datasource": {
            "type": "prometheus",
            "uid": "PBFA97CFB590B2093"
          },
          "refId": "A"
        }
      ],
      "title": "Tree Queue (Bytes/PCQ/Dropped/Packets)",
      "type": "row"
    },
    {
      "collapsed": true,
      "datasource": {
        "type": "prometheus",
        "uid": "PBFA97CFB590B2093"
      },
      "gridPos": {
        "h": 1,
        "w": 24,
        "x": 0,
        "y": 57
      },
      "id": 1338,
      "panels": [
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${DS_PROMETHEUS}"
          },
          "description": "",
          "fieldConfig": {
            "defaults": {
              "color": {
                "mode": "palette-classic"
              },
              "custom": {
                "axisLabel": "",
                "axisPlacement": "auto",
                "barAlignment": 0,
                "drawStyle": "line",
                "fillOpacity": 50,
                "gradientMode": "opacity",
                "hideFrom": {
                  "legend": false,
                  "tooltip": false,
                  "viz": false
                },
                "lineInterpolation": "smooth",
                "lineWidth": 2,
                "pointSize": 5,
                "scaleDistribution": {
                  "type": "linear"
                },
                "showPoints": "never",
                "spanNulls": false,
                "stacking": {
                  "group": "A",
                  "mode": "none"
                },
                "thresholdsStyle": {
                  "mode": "off"
                }
              },
              "mappings": [],
              "thresholds": {
                "mode": "absolute",
                "steps": [
                  {
                    "color": "green"
                  }
                ]
              },
              "unit": "pps"
            },
            "overrides": []
          },
          "gridPos": {
            "h": 11,
            "w": 8,
            "x": 0,
            "y": 9
          },
          "id": 1339,
          "options": {
            "legend": {
              "calcs": [
                "mean",
                "lastNotNull",
                "max",
                "min"
              ],
              "displayMode": "table",
              "placement": "bottom"
            },
            "tooltip": {
              "mode": "multi"
            }
          },
          "pluginVersion": "8.2.1",
          "repeat": "Interface",
          "repeatDirection": "h",
          "targets": [
            {
              "datasource": {
                "type": "prometheus",
                "uid": "${DS_PROMETHEUS}"
              },
              "exemplar": true,
              "expr": "irate(ifHCInMulticastPkts{ifName=~'$Interface',instance='$instance'}[$__rate_interval])",
              "hide": false,
              "interval": "",
              "legendFormat": "In Multicast",
              "refId": "K"
            },
            {
              "datasource": {
                "type": "prometheus",
                "uid": "${DS_PROMETHEUS}"
              },
              "exemplar": true,
              "expr": "-irate(ifHCOutMulticastPkts{ifName=~'$Interface',instance='$instance'}[$__rate_interval])",
              "hide": false,
              "interval": "",
              "legendFormat": "Out Multicast",
              "refId": "L"
            },
            {
              "datasource": {
                "type": "prometheus",
                "uid": "${DS_PROMETHEUS}"
              },
              "exemplar": true,
              "expr": "irate(ifHCInBroadcastPkts{ifName=~'$Interface',instance='$instance'}[$__rate_interval])",
              "hide": false,
              "interval": "",
              "legendFormat": "In Broadcast",
              "refId": "C"
            },
            {
              "datasource": {
                "type": "prometheus",
                "uid": "${DS_PROMETHEUS}"
              },
              "exemplar": true,
              "expr": "-irate(ifHCOutBroadcastPkts{ifName=~'$Interface',instance='$instance'}[$__rate_interval])",
              "hide": false,
              "interval": "",
              "legendFormat": "Out Broadcast",
              "refId": "A"
            },
            {
              "datasource": {
                "type": "prometheus",
                "uid": "${DS_PROMETHEUS}"
              },
              "exemplar": true,
              "expr": "irate(ifHCInUcastPkts{ifName=~'$Interface',instance='$instance'}[$__rate_interval])",
              "hide": false,
              "interval": "",
              "legendFormat": "In Unicast",
              "refId": "B"
            },
            {
              "datasource": {
                "type": "prometheus",
                "uid": "${DS_PROMETHEUS}"
              },
              "exemplar": true,
              "expr": "-irate(ifHCOutUcastPkts{ifName=~'$Interface',instance='$instance'}[$__rate_interval])",
              "hide": false,
              "interval": "",
              "legendFormat": "Out Unicast",
              "refId": "D"
            },
            {
              "datasource": {
                "type": "prometheus",
                "uid": "${DS_PROMETHEUS}"
              },
              "exemplar": true,
              "expr": "irate(ifInDiscards{ifName=~'$Interface',instance='$instance'}[$__rate_interval])",
              "hide": false,
              "interval": "",
              "legendFormat": "In Discard",
              "refId": "E"
            },
            {
              "datasource": {
                "type": "prometheus",
                "uid": "${DS_PROMETHEUS}"
              },
              "exemplar": true,
              "expr": "irate(ifOutDiscards{ifName=~'$Interface',instance='$instance'}[$__rate_interval])",
              "hide": false,
              "interval": "",
              "legendFormat": "Out Discard",
              "refId": "F"
            },
            {
              "datasource": {
                "type": "prometheus",
                "uid": "${DS_PROMETHEUS}"
              },
              "exemplar": true,
              "expr": "irate(ifInErrors{ifName=~'$Interface',instance='$instance'}[$__rate_interval])",
              "hide": false,
              "interval": "",
              "legendFormat": "In Errors",
              "refId": "G"
            },
            {
              "datasource": {
                "type": "prometheus",
                "uid": "${DS_PROMETHEUS}"
              },
              "exemplar": true,
              "expr": "irate(ifOutErrors{ifName=~'$Interface',instance='$instance'}[$__rate_interval])",
              "hide": false,
              "interval": "",
              "legendFormat": "Out Errors",
              "refId": "H"
            },
            {
              "datasource": {
                "type": "prometheus",
                "uid": "${DS_PROMETHEUS}"
              },
              "exemplar": true,
              "expr": "irate(ifInUnknownProtos{ifName=~'$Interface',instance='$instance'}[$__rate_interval])",
              "hide": false,
              "interval": "",
              "legendFormat": "In Unknown Protos",
              "refId": "I"
            },
            {
              "datasource": {
                "type": "prometheus",
                "uid": "${DS_PROMETHEUS}"
              },
              "exemplar": true,
              "expr": "-irate(ifOutQLen{ifName=~'$Interface',instance='$instance'}[$__rate_interval])",
              "hide": false,
              "interval": "",
              "legendFormat": "Out queue length",
              "refId": "J"
            }
          ],
          "title": "Interface \"$Interface\"",
          "type": "timeseries"
        }
      ],
      "targets": [
        {
          "datasource": {
            "type": "prometheus",
            "uid": "PBFA97CFB590B2093"
          },
          "refId": "A"
        }
      ],
      "title": "*cast/Dascard/Errors/Unknown Protos/Queue length",
      "type": "row"
    },
    {
      "collapsed": true,
      "datasource": {
        "type": "prometheus",
        "uid": "PBFA97CFB590B2093"
      },
      "gridPos": {
        "h": 1,
        "w": 24,
        "x": 0,
        "y": 58
      },
      "id": 1285,
      "panels": [
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${DS_PROMETHEUS}"
          },
          "description": "",
          "fieldConfig": {
            "defaults": {
              "color": {
                "mode": "palette-classic"
              },
              "custom": {
                "axisLabel": "",
                "axisPlacement": "auto",
                "barAlignment": 0,
                "drawStyle": "line",
                "fillOpacity": 100,
                "gradientMode": "opacity",
                "hideFrom": {
                  "legend": false,
                  "tooltip": false,
                  "viz": false
                },
                "lineInterpolation": "smooth",
                "lineWidth": 2,
                "pointSize": 5,
                "scaleDistribution": {
                  "type": "linear"
                },
                "showPoints": "never",
                "spanNulls": false,
                "stacking": {
                  "group": "A",
                  "mode": "none"
                },
                "thresholdsStyle": {
                  "mode": "off"
                }
              },
              "mappings": [],
              "thresholds": {
                "mode": "absolute",
                "steps": [
                  {
                    "color": "green"
                  }
                ]
              },
              "unit": "bps"
            },
            "overrides": [
              {
                "matcher": {
                  "id": "byName",
                  "options": "In"
                },
                "properties": [
                  {
                    "id": "color",
                    "value": {
                      "fixedColor": "#6afff3",
                      "mode": "fixed"
                    }
                  }
                ]
              },
              {
                "matcher": {
                  "id": "byName",
                  "options": "Out"
                },
                "properties": [
                  {
                    "id": "color",
                    "value": {
                      "fixedColor": "#bf71ff",
                      "mode": "fixed"
                    }
                  }
                ]
              }
            ]
          },
          "gridPos": {
            "h": 7,
            "w": 8,
            "x": 0,
            "y": 10
          },
          "id": 1286,
          "options": {
            "legend": {
              "calcs": [
                "mean",
                "lastNotNull",
                "max",
                "min"
              ],
              "displayMode": "table",
              "placement": "bottom"
            },
            "tooltip": {
              "mode": "multi"
            }
          },
          "pluginVersion": "8.2.1",
          "repeat": "Interface",
          "repeatDirection": "h",
          "targets": [
            {
              "datasource": {
                "type": "prometheus",
                "uid": "${DS_PROMETHEUS}"
              },
              "exemplar": true,
              "expr": "irate(ifHCInOctets{ifName=~'$Interface',instance='$instance'}[$__rate_interval])*8",
              "format": "time_series",
              "hide": false,
              "interval": "",
              "intervalFactor": 1,
              "legendFormat": "In",
              "refId": "A"
            },
            {
              "datasource": {
                "type": "prometheus",
                "uid": "${DS_PROMETHEUS}"
              },
              "exemplar": true,
              "expr": "-irate(ifHCOutOctets{ifName=~'$Interface',instance='$instance'}[$__rate_interval])*8",
              "hide": false,
              "interval": "",
              "intervalFactor": 1,
              "legendFormat": "Out",
              "refId": "B"
            }
          ],
          "title": "Traffic \"$Interface\"",
          "type": "timeseries"
        }
      ],
      "targets": [
        {
          "datasource": {
            "type": "prometheus",
            "uid": "PBFA97CFB590B2093"
          },
          "refId": "A"
        }
      ],
      "title": "Interfaces Traffic",
      "type": "row"
    }
  ],
  "refresh": "10s",
  "schemaVersion": 36,
  "style": "dark",
  "tags": [
    "prometheus",
    "Mikrotik",
    "snmp",
    "snmp v3",
    "snmp_exporter"
  ],
  "templating": {
    "list": [
      {
        "current": {
          "selected": false,
          "text": "Prometheus",
          "value": "Prometheus"
        },
        "hide": 2,
        "includeAll": false,
        "label": "datasource",
        "multi": false,
        "name": "DS_PROMETHEUS",
        "options": [],
        "query": "prometheus",
        "refresh": 1,
        "regex": "",
        "skipUrlSync": false,
        "type": "datasource"
      },
      {
        "current": {},
        "datasource": {
          "type": "prometheus",
          "uid": "${DS_PROMETHEUS}"
        },
        "definition": "label_values(ifHCInOctets,  job)",
        "hide": 2,
        "includeAll": false,
        "multi": false,
        "name": "Job",
        "options": [],
        "query": {
          "query": "label_values(ifHCInOctets,  job)",
          "refId": "Prometheus-Job-Variable-Query"
        },
        "refresh": 1,
        "regex": "",
        "skipUrlSync": false,
        "sort": 0,
        "tagValuesQuery": "",
        "tagsQuery": "",
        "type": "query",
        "useTags": false
      },
      {
        "current": {},
        "datasource": {
          "type": "prometheus",
          "uid": "${DS_PROMETHEUS}"
        },
        "definition": "query_result(ifInOctets{job=\"snmp-exporter\"})",
        "hide": 0,
        "includeAll": false,
        "multi": false,
        "name": "instance",
        "options": [],
        "query": {
          "query": "label_values(ifHCInOctets,  instance)",
          "refId": "Prometheus-instance-Variable-Query"
        },
        "refresh": 1,
        "regex": "",
        "skipUrlSync": false,
        "sort": 3,
        "tagValuesQuery": "",
        "tagsQuery": "",
        "type": "query",
        "useTags": false
      },
      {
        "current": {},
        "datasource": {
          "type": "prometheus",
          "uid": "${DS_PROMETHEUS}"
        },
        "definition": "label_values(ifHighSpeed{instance='$instance'},ifIndex)",
        "hide": 2,
        "includeAll": false,
        "label": "",
        "multi": false,
        "name": "index",
        "options": [],
        "query": {
          "query": "label_values(ifHighSpeed{instance='$instance'},ifIndex)",
          "refId": "Prometheus-index-Variable-Query"
        },
        "refresh": 1,
        "regex": "",
        "skipUrlSync": false,
        "sort": 3,
        "tagValuesQuery": "",
        "tagsQuery": "",
        "type": "query",
        "useTags": false
      },
      {
        "allValue": "",
        "current": {},
        "datasource": {
          "type": "prometheus",
          "uid": "${DS_PROMETHEUS}"
        },
        "definition": "query_result(sort(ifIndex{ifName=~'^(ether).+',instance='$instance'}) or sort(ifIndex{ifName=~'^(sfp|wlan).+',instance='$instance'}) or sort(ifIndex{ifName=~'^bridge.+',instance='$instance'}) or  sort(ifIndex{ifName!~'^(ether|bridge).+',instance='$instance'}) )",
        "hide": 0,
        "includeAll": true,
        "multi": false,
        "name": "Interface",
        "options": [],
        "query": {
          "query": "query_result(sort(ifIndex{ifName=~'^(ether).+',instance='$instance'}) or sort(ifIndex{ifName=~'^(sfp|wlan).+',instance='$instance'}) or sort(ifIndex{ifName=~'^bridge.+',instance='$instance'}) or  sort(ifIndex{ifName!~'^(ether|bridge).+',instance='$instance'}) )",
          "refId": "Prometheus-Interface-Variable-Query"
        },
        "refresh": 1,
        "regex": "/ifName=\"(.*)\",instance/",
        "skipUrlSync": false,
        "sort": 0,
        "tagValuesQuery": "",
        "tagsQuery": "",
        "type": "query",
        "useTags": false
      },
      {
        "current": {},
        "datasource": {
          "type": "prometheus",
          "uid": "${DS_PROMETHEUS}"
        },
        "definition": "query_result(ifHCInOctets{ifName=\"$Interface\",instance=\"$instance\"})",
        "hide": 2,
        "includeAll": false,
        "multi": false,
        "name": "desc",
        "options": [],
        "query": {
          "query": "query_result(ifHCInOctets{ifName=\"$Interface\",instance=\"$instance\"})",
          "refId": "Prometheus-desc-Variable-Query"
        },
        "refresh": 1,
        "regex": "/ifAlias=\"(.*)\",ifDescr/",
        "skipUrlSync": false,
        "sort": 4,
        "tagValuesQuery": "",
        "tagsQuery": "",
        "type": "query",
        "useTags": false
      },
      {
        "allValue": "Null",
        "current": {},
        "datasource": {
          "type": "prometheus",
          "uid": "${DS_PROMETHEUS}"
        },
        "definition": "query_result((mtxrQueueSimplePacketsIn * on (mtxrQueueSimpleIndex) group_left(mtxrQueueSimpleName) mtxrQueueSimpleName{instance='$instance',}))",
        "hide": 2,
        "includeAll": true,
        "label": "",
        "multi": false,
        "name": "queuesimple_name",
        "options": [],
        "query": {
          "query": "query_result((mtxrQueueSimplePacketsIn * on (mtxrQueueSimpleIndex) group_left(mtxrQueueSimpleName) mtxrQueueSimpleName{instance='$instance',}))",
          "refId": "StandardVariableQuery"
        },
        "refresh": 1,
        "regex": "/mtxrQueueSimpleName=\"(.*)\"/",
        "skipUrlSync": false,
        "sort": 0,
        "tagValuesQuery": "",
        "tagsQuery": "",
        "type": "query",
        "useTags": false
      },
      {
        "allValue": "Null",
        "current": {},
        "datasource": {
          "type": "prometheus",
          "uid": "${DS_PROMETHEUS}"
        },
        "definition": "query_result((mtxrQueueTreePackets * on (mtxrQueueTreeIndex) group_left(mtxrQueueTreeName) mtxrQueueTreeName{instance='$instance',}))",
        "hide": 1,
        "includeAll": true,
        "label": "",
        "multi": false,
        "name": "queuetree_name",
        "options": [],
        "query": {
          "query": "query_result((mtxrQueueTreePackets * on (mtxrQueueTreeIndex) group_left(mtxrQueueTreeName) mtxrQueueTreeName{instance='$instance',}))",
          "refId": "StandardVariableQuery"
        },
        "refresh": 1,
        "regex": "/mtxrQueueTreeName=\"(.*)\"/",
        "skipUrlSync": false,
        "sort": 0,
        "tagValuesQuery": "",
        "tagsQuery": "",
        "type": "query",
        "useTags": false
      },
      {
        "allValue": "Null",
        "current": {},
        "datasource": {
          "type": "prometheus",
          "uid": "${DS_PROMETHEUS}"
        },
        "definition": "query_result((mtxrQueueTreeParentIndex * on (mtxrQueueTreeIndex) group_left(mtxrQueueTreeName) mtxrQueueTreeName{instance='$instance',}))",
        "hide": 1,
        "includeAll": true,
        "label": "",
        "multi": false,
        "name": "queuetree_parent",
        "options": [],
        "query": {
          "query": "query_result((mtxrQueueTreeParentIndex * on (mtxrQueueTreeIndex) group_left(mtxrQueueTreeName) mtxrQueueTreeName{instance='$instance',}))",
          "refId": "StandardVariableQuery"
        },
        "refresh": 1,
        "regex": "/mtxrQueueTreeName=\"(.*)\"/",
        "skipUrlSync": false,
        "sort": 0,
        "tagValuesQuery": "",
        "tagsQuery": "",
        "type": "query",
        "useTags": false
      },
      {
        "allValue": "",
        "current": {},
        "datasource": {
          "type": "prometheus",
          "uid": "${DS_PROMETHEUS}"
        },
        "definition": "query_result((mtxrQueueTreeParentIndex * on (mtxrQueueTreeName) group_left(mtxrQueueTreeIndex) mtxrQueueTreeIndex{instance='$instance',}))",
        "hide": 1,
        "includeAll": true,
        "label": "",
        "multi": false,
        "name": "queuetree_flow",
        "options": [],
        "query": {
          "query": "query_result((mtxrQueueTreeParentIndex * on (mtxrQueueTreeName) group_left(mtxrQueueTreeIndex) mtxrQueueTreeIndex{instance='$instance',}))",
          "refId": "StandardVariableQuery"
        },
        "refresh": 1,
        "regex": "/mtxrQueueTreeIndex=\"(.*)\",instance/",
        "skipUrlSync": false,
        "sort": 0,
        "tagValuesQuery": "",
        "tagsQuery": "",
        "type": "query",
        "useTags": false
      }
    ]
  },
  "time": {
    "from": "now-30m",
    "to": "now"
  },
  "timepicker": {
    "refresh_intervals": [
      "5s",
      "10s",
      "30s",
      "1m",
      "5m",
      "15m",
      "30m",
      "1h",
      "2h",
      "1d"
    ],
    "time_options": [
      "5m",
      "15m",
      "1h",
      "6h",
      "12h",
      "24h",
      "2d",
      "7d",
      "30d"
    ]
  },
  "timezone": "",
  "title": "Mikrotik monitoring",
  "uid": "nR3NRDGaz",
  "version": 1,
  "weekStart": ""
}


File: /prometheus\data\.gitignore
# Ignore everything in this directory
*
# Except this file
!.gitignore

File: /prometheus\prometheus.yml
# Sample config for Prometheus.

global:
  scrape_interval:     15s # Set the scrape interval to every 15 seconds. Default is every 1 minute.
  evaluation_interval: 15s # Evaluate rules every 15 seconds. The default is every 1 minute.
  # scrape_timeout is set to the global default (10s).

  # Attach these labels to any time series or alerts when communicating with
  # external systems (federation, remote storage, Alertmanager).
  external_labels:
      monitor: 'Mikrotik'

# Alertmanager configuration
alerting:
  alertmanagers:
  - static_configs:
    - targets: ['localhost:9093']

# Load rules once and periodically evaluate them according to the global 'evaluation_interval'.
rule_files:
  # - "first_rules.yml"
  # - "second_rules.yml"

# A scrape configuration containing exactly one endpoint to scrape:
# Here it's Prometheus itself.
scrape_configs:
  # The job name is added as a label `job=<job_name>` to any timeseries scraped from this config.
  - job_name: 'prometheus'

    # Override the global default and scrape targets from this job every 5 seconds.
    scrape_interval: 10s
    scrape_timeout: 10s
    tls_config:
      insecure_skip_verify: true
    # metrics_path defaults to '/metrics'
    # scheme defaults to 'http'.

    #static_configs:
      #- targets: ['localhost:9090']

  - job_name: Mikrotik
    static_configs:
      - targets:
        - 192.168.88.1 # mikrotik_ip
    metrics_path: /snmp
    params:
      module: [mikrotik]
    relabel_configs:
      - source_labels: [__address__]
        target_label: __param_target
      - source_labels: [__param_target]
        target_label: instance
      - target_label: __address__
        replacement: mk_snmp_exporter:9116  # The SNMP exporter's real hostname:port.


File: /README.md
# Grafana-Mikrotik

![logo](https://repository-images.githubusercontent.com/366494855/c62052b8-17c2-47f2-a3ae-0e397a3ef074)

![visitors](https://visitor-badge.laobi.icu/badge?page_id=IgorKha.Grafana-Mikrotik)
![example branch parameter](https://github.com/IgorKha/Grafana-Mikrotik/actions/workflows/action.yml/badge.svg?branch=master)
![mikrotikOS](https://img.shields.io/badge/Mikrotik_ROS-v7.4-blue)
![Grafana](https://img.shields.io/badge/Grafana-v9.0.5-orange?logo=grafana)
![Prometheus](https://img.shields.io/badge/Prometheus-v2.37.0-red?logo=prometheus)
![snmp_exporter](https://img.shields.io/badge/snmp__exporter-v0.20.0-red?logo=prometheus)

[![Donate using Liberapay](https://liberapay.com/assets/widgets/donate.svg)](https://liberapay.com/~1772367/donate)

---

## 🐳 Deploy with docker-compose

### Deploy with bash script

```console
git clone https://github.com/IgorKha/Grafana-Mikrotik.git
cd ./Grafana-Mikrotik
bash ./run.sh --config
```

```console
  You can also pass some arguments to script to set some these options:

    --config: change the user and password to grafana and specify the mikrotik IP address

    --stop: stop docker containers

    --help
```

For example:

```console
    bash run.sh --config
```

[![asciicast](https://asciinema.org/a/nOhuc7LvI6bRWbg7dcvqFQ4Kc.png)](https://asciinema.org/a/nOhuc7LvI6bRWbg7dcvqFQ4Kc)

### deploy with docker-compose manual

1.Change targets ip (192.168.88.1) into file prometheus/prometheus.yml

2.Run

```console
docker-compose up -d
```

3.Open [localhost:3000](http://localhost:3000)

* Grafana login: `admin`

* Password: `mikrotik`

If you want to change the credentials, then edit the ".env" file

---

## Manual deploy

1.add into prometheus.yml

```yml
  - job_name: Mikrotik
    static_configs:
      - targets:
        - 192.168.88.1  # SNMP device IP.
    metrics_path: /snmp
    params:
      module: [mikrotik]
    relabel_configs:
      - source_labels: [__address__]
        target_label: __param_target
      - source_labels: [__param_target]
        target_label: instance
      - target_label: __address__
        replacement: localhost:9116  # The SNMP exporter's real hostname:port.
```

2.Configure Prometheus and run /snmp/snmp_exporter

3.Add dashboard <https://grafana.com/grafana/dashboards/14420>

---

### Docker snmp_exporter (deprecated)

[![Docker Pulls](https://img.shields.io/docker/pulls/mashinkopochinko/snmp_exporter_mikrotik?logo=docker)](https://hub.docker.com/repository/docker/mashinkopochinko/snmp_exporter_mikrotik)

> amd64-linux container

```console
sudo docker run -d -p 9116:9116 mashinkopochinko/snmp_exporter_mikrotik:latest
```

---
![img1](/readme/screen.png)


File: /run.sh
#!/bin/bash

############################################################################
#   You can also pass some arguments to script to set some these options:
#   
#       --config: change the user and password to grafana and specify the mikrotik IP address
#       --stop: stop docker containers
#   
#   For example:
#       bash run.sh --config
#   
############################################################################

set -e

REPO=Grafana-Mikrotik
ENV_FILE=${ENV_FILE:-.env}
ENV_FILE_GF=${ENV_FILE_GF:-.grafana}
ENV_FILE_PROMETHEUS=${ENV_FILE_PROMETHEU:-.prometheus}

#? Colors
RED='\033[31m'
GREEN='\033[32m'
YELLOW='\033[33m'
BLUE='\033[34m'
BOLD='\033[1m'
RESET='\033[m' #? No Color

BOLD='\033[1m'

ask() {
    local prompt default reply

    if [[ ${2} = 'Y' ]]; then
        prompt='Y/n'
        default='Y'
    elif [[ ${2} = 'N' ]]; then
        prompt='y/N'
        default='N'
    else
        prompt='y/n'
        default=''
    fi

    while true; do

        #? Ask the question (not using "read -p" as it uses stderr not stdout)
        echo -n "$1 [${prompt}] "

        #? Read the answer (use /dev/tty in case stdin is redirected from somewhere else)
        read -r reply </dev/tty

        #? Default?
        if [[ -z ${reply} ]]; then
            reply=${default}
        fi

        #? Check if the reply is valid
        case "${reply}" in
        Y* | y*) return 0 ;;
        N* | n*) return 1 ;;
        esac
    done
}

command_exists() {
    command -v "$@" >/dev/null 2>&1 || {
        fmt_error "$* is not installed. Please install $* first."
        exit 1
    }
}

fmt_error() {
    echo -e "\n${BOLD}${RED}Error: $*${RESET}\n" >&2
}

help() {
    if [ "${HELP}" = yes ]; then
        sed -n -e 's/^#   //' -e '3,12p;' "$0"
        exit 1
        return
    fi
}

clone_git() {

    echo -e "${BLUE}Git cloning ${REPO}...${RESET}"
    git clone --depth=1 https://github.com/IgorKha/${REPO}.git ||
        {
            fmt_error "git clone of ${REPO} repo failed"
            exit 1
        }

    echo
}

router_ip() {
    if [[ "${CONFIG}" = yes ]]; then
        IP=$(grep -R 'MIKROTIK_IP' "${ENV_FILE_PROMETHEUS}" 2>&1 | cut -d= -f2)
        echo -e "\n${BLUE}===================================="
        echo -e "\n${BOLD}Prometheus${RESET}\n"
        if ask "Change target mikrotik IP address ? (current ${IP})" Y; then
            read -rp 'Enter target mikrotik IP address: ' IP
            if [ -d "./${REPO}" ]; then
                sed -ri -e '/mikrotik_ip/s/(- ).*( #.*)/\1'"${IP}"'\2/g' \
                    ${REPO}/prometheus/prometheus.yml
                sed -ri -e 's/^(MIKROTIK_IP=)(.*)$/\1'"$IP"'/g' "${ENV_FILE_PROMETHEUS}"
                echo -e "\n${GREEN}... Prometheus target IP changed to ${IP}"
            else
                sed -ri -e '/mikrotik_ip/s/(- ).*( #.*)/\1'"${IP}"'\2/g' \
                    ./prometheus/prometheus.yml
                sed -ri -e 's/^(MIKROTIK_IP=)(.*)$/\1'"${IP}"'/g' "${ENV_FILE_PROMETHEUS}"
                echo -e "\n${GREEN}... Prometheus target IP changed to ${IP}"
            fi
            return
        fi
        echo -e "\n${BLUE}...Skipped step"
        return
    fi
}

# snmp_on() {
#     if [ "$CONFIG" = yes ]; then
#         echo -e "\n${BLUE}===================================="
#         echo -e "${BOLD}Mikrotik SNMP ACTIVATION${RESET}"
#         if ask "Activate snmp mikrotik using ssh?" N; then
#             read -rp 'Enter login: ' MK_LOGIN
#             # read -rsp 'Enter password: ' MK_PASSWD

#             COMM="
#             snmp
#             "
#             ssh ${MK_LOGIN}@$IP "${COMM}"

#         else
#             echo "skipped"
#         fi
#         return
#     fi
# }

grafana_credentials() {
    if [[ "${CONFIG}" = yes ]]; then
        echo -e "\n${YELLOW}===================================="
        echo -e "\n${BOLD}Grafana${RESET}\n"
        if ask "Change default credentials Grafana ?" N; then
            read -rp 'Enter grafana Username: ' GF_USER
            read -rsp 'Enter grafana Password: ' GF_PASSWD

            sed -ri -e 's/^(GF_SECURITY_ADMIN_USER=)(.*)$/\1'"${GF_USER}"'/g' "${ENV_FILE_GF}"
            sed -ri -e 's/^(GF_SECURITY_ADMIN_PASSWORD=)(.*)$/\1'"${GF_PASSWD}"'/g' "${ENV_FILE_GF}"
        else
            echo -e "Default Grafana:
            User: ${YELLOW}admin${RESET}
            Password: ${YELLOW}mikrotik${RESET}"
        fi
        return
    fi
}

docker-cmd() {
    if [[ "${STOP}" = yes ]]; then
        if [ -d "./${REPO}" ]; then
            cd ${REPO} && docker compose down
        else
            docker compose down
        fi
    else
        if [[ -d "./${REPO}" ]]; then
            cd ${REPO} && docker compose up -d
            print_success
        else
            docker compose up -d
            print_success
        fi
    fi
}

print_success() {
    echo "============================================="
    echo -e "${GREEN}Grafana http://localhost:3000"
    echo -e "Prometheus http://localhost:9090/targets${RESET}"
}

main() {

    #? Parse arguments
    while [[ $# -gt 0 ]]; do
        case $1 in
        --help) HELP=yes ;;
        --config) CONFIG=yes ;;
        --stop) STOP=yes ;;
        esac
        shift
    done

    help

    command_exists git
    command_exists docker

    #? init
    if [[ -d "./${REPO}" ]]; then
        ENV_FILE=${REPO}/.env
        ENV_FILE_GF=${REPO}/.grafana
        ENV_FILE_PROMETHEUS=${REPO}/.prometheus
    elif [[ ! -e ${ENV_FILE} ]]; then
        clone_git
        ENV_FILE=${REPO}/.env
        ENV_FILE_GF=${REPO}/.grafana
        ENV_FILE_PROMETHEUS=${REPO}/.prometheus
    fi

    router_ip
    # snmp_on
    grafana_credentials

    # Change UID:GID prometheus container to current user
    sed -ri -e 's/^(CURRENT_USER=)(.*)$/\1'"$(id -u)\:$(id -g)"'/g' "${ENV_FILE}"

    docker-cmd
}

main "$@"


File: /snmp\Dockerfile
ARG ARCH="amd64"
ARG OS="linux"
FROM quay.io/prometheus/busybox-${OS}-${ARCH}:latest
LABEL maintainer="The Prometheus Authors <prometheus-developers@googlegroups.com>"
LABEL Software="snmp_exporter prometheus for mikrotik"
LABEL Author="IgorKha"

ARG ARCH="amd64"
ARG OS="linux"
COPY snmp_exporter  /bin/snmp_exporter
COPY snmp.yml       /etc/snmp_exporter/snmp.yml

EXPOSE      9116
ENTRYPOINT  [ "/bin/snmp_exporter" ]
CMD         [ "--config.file=/etc/snmp_exporter/snmp.yml" ]

File: /snmp\LICENSE
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


File: /snmp\NOTICE
Prometheus SNMP exporter
Copyright 2016 The Prometheus Authors


File: /snmp\snmp.yml
    # WARNING: This file was auto-generated using snmp_exporter generator, manual changes will be lost.
auths:
    public_v2:
        community: public
        security_level: noAuthNoPriv
        auth_protocol: MD5
        priv_protocol: DES
        version: 2
modules:
    mikrotik:
      walk:
      - 1.3.6.1.2.1.2
      - 1.3.6.1.2.1.25
      - 1.3.6.1.2.1.31
      - 1.3.6.1.4.1.14988
      - 1.3.6.1.4.1.2021.10.1.1
      - 1.3.6.1.4.1.2021.10.1.2
      - 1.3.6.1.2.1.1.5.0
      get:
      - 1.3.6.1.2.1.1.1.0
      - 1.3.6.1.2.1.1.3.0
      metrics:
      - name: sysDescr
        oid: 1.3.6.1.2.1.1.1
        type: DisplayString
        help: A textual description of the entity - 1.3.6.1.2.1.1.1
      - name: sysIdentity
        oid: 1.3.6.1.2.1.1.5.0
        type: DisplayString
        help: A textual description of the system identity - 1.3.6.1.2.1.1.5.0
      - name: sysUpTime
        oid: 1.3.6.1.2.1.1.3
        type: gauge
        help: The time (in hundredths of a second) since the network management portion
          of the system was last re-initialized. - 1.3.6.1.2.1.1.3
      - name: ifNumber
        oid: 1.3.6.1.2.1.2.1
        type: gauge
        help: The number of network interfaces (regardless of their current state) present
          on this system. - 1.3.6.1.2.1.2.1
      - name: ifIndex
        oid: 1.3.6.1.2.1.2.2.1.1
        type: gauge
        help: A unique value, greater than zero, for each interface - 1.3.6.1.2.1.2.2.1.1
        indexes:
        - labelname: ifIndex
          type: gauge
        lookups:
        - labels:
          - ifIndex
          labelname: ifName
          oid: 1.3.6.1.2.1.31.1.1.1.1
          type: DisplayString
      - name: ifDescr
        oid: 1.3.6.1.2.1.2.2.1.2
        type: DisplayString
        help: A textual string containing information about the interface - 1.3.6.1.2.1.2.2.1.2
        indexes:
        - labelname: ifIndex
          type: gauge
        lookups:
        - labels:
          - ifIndex
          labelname: ifName
          oid: 1.3.6.1.2.1.31.1.1.1.1
          type: DisplayString
      - name: ifType
        oid: 1.3.6.1.2.1.2.2.1.3
        type: EnumAsInfo
        help: The type of interface - 1.3.6.1.2.1.2.2.1.3
        indexes:
        - labelname: ifIndex
          type: gauge
        lookups:
        - labels:
          - ifIndex
          labelname: ifName
          oid: 1.3.6.1.2.1.31.1.1.1.1
          type: DisplayString
        enum_values:
          1: other
          2: regular1822
          3: hdh1822
          4: ddnX25
          5: rfc877x25
          6: ethernetCsmacd
          7: iso88023Csmacd
          8: iso88024TokenBus
          9: iso88025TokenRing
          10: iso88026Man
          11: starLan
          12: proteon10Mbit
          13: proteon80Mbit
          14: hyperchannel
          15: fddi
          16: lapb
          17: sdlc
          18: ds1
          19: e1
          20: basicISDN
          21: primaryISDN
          22: propPointToPointSerial
          23: ppp
          24: softwareLoopback
          25: eon
          26: ethernet3Mbit
          27: nsip
          28: slip
          29: ultra
          30: ds3
          31: sip
          32: frameRelay
          33: rs232
          34: para
          35: arcnet
          36: arcnetPlus
          37: atm
          38: miox25
          39: sonet
          40: x25ple
          41: iso88022llc
          42: localTalk
          43: smdsDxi
          44: frameRelayService
          45: v35
          46: hssi
          47: hippi
          48: modem
          49: aal5
          50: sonetPath
          51: sonetVT
          52: smdsIcip
          53: propVirtual
          54: propMultiplexor
          55: ieee80212
          56: fibreChannel
          57: hippiInterface
          58: frameRelayInterconnect
          59: aflane8023
          60: aflane8025
          61: cctEmul
          62: fastEther
          63: isdn
          64: v11
          65: v36
          66: g703at64k
          67: g703at2mb
          68: qllc
          69: fastEtherFX
          70: channel
          71: ieee80211
          72: ibm370parChan
          73: escon
          74: dlsw
          75: isdns
          76: isdnu
          77: lapd
          78: ipSwitch
          79: rsrb
          80: atmLogical
          81: ds0
          82: ds0Bundle
          83: bsc
          84: async
          85: cnr
          86: iso88025Dtr
          87: eplrs
          88: arap
          89: propCnls
          90: hostPad
          91: termPad
          92: frameRelayMPI
          93: x213
          94: adsl
          95: radsl
          96: sdsl
          97: vdsl
          98: iso88025CRFPInt
          99: myrinet
          100: voiceEM
          101: voiceFXO
          102: voiceFXS
          103: voiceEncap
          104: voiceOverIp
          105: atmDxi
          106: atmFuni
          107: atmIma
          108: pppMultilinkBundle
          109: ipOverCdlc
          110: ipOverClaw
          111: stackToStack
          112: virtualIpAddress
          113: mpc
          114: ipOverAtm
          115: iso88025Fiber
          116: tdlc
          117: gigabitEthernet
          118: hdlc
          119: lapf
          120: v37
          121: x25mlp
          122: x25huntGroup
          123: transpHdlc
          124: interleave
          125: fast
          126: ip
          127: docsCableMaclayer
          128: docsCableDownstream
          129: docsCableUpstream
          130: a12MppSwitch
          131: tunnel
          132: coffee
          133: ces
          134: atmSubInterface
          135: l2vlan
          136: l3ipvlan
          137: l3ipxvlan
          138: digitalPowerline
          139: mediaMailOverIp
          140: dtm
          141: dcn
          142: ipForward
          143: msdsl
          144: ieee1394
          145: if-gsn
          146: dvbRccMacLayer
          147: dvbRccDownstream
          148: dvbRccUpstream
          149: atmVirtual
          150: mplsTunnel
          151: srp
          152: voiceOverAtm
          153: voiceOverFrameRelay
          154: idsl
          155: compositeLink
          156: ss7SigLink
          157: propWirelessP2P
          158: frForward
          159: rfc1483
          160: usb
          161: ieee8023adLag
          162: bgppolicyaccounting
          163: frf16MfrBundle
          164: h323Gatekeeper
          165: h323Proxy
          166: mpls
          167: mfSigLink
          168: hdsl2
          169: shdsl
          170: ds1FDL
          171: pos
          172: dvbAsiIn
          173: dvbAsiOut
          174: plc
          175: nfas
          176: tr008
          177: gr303RDT
          178: gr303IDT
          179: isup
          180: propDocsWirelessMaclayer
          181: propDocsWirelessDownstream
          182: propDocsWirelessUpstream
          183: hiperlan2
          184: propBWAp2Mp
          185: sonetOverheadChannel
          186: digitalWrapperOverheadChannel
          187: aal2
          188: radioMAC
          189: atmRadio
          190: imt
          191: mvl
          192: reachDSL
          193: frDlciEndPt
          194: atmVciEndPt
          195: opticalChannel
          196: opticalTransport
          197: propAtm
          198: voiceOverCable
          199: infiniband
          200: teLink
          201: q2931
          202: virtualTg
          203: sipTg
          204: sipSig
          205: docsCableUpstreamChannel
          206: econet
          207: pon155
          208: pon622
          209: bridge
          210: linegroup
          211: voiceEMFGD
          212: voiceFGDEANA
          213: voiceDID
          214: mpegTransport
          215: sixToFour
          216: gtp
          217: pdnEtherLoop1
          218: pdnEtherLoop2
          219: opticalChannelGroup
          220: homepna
          221: gfp
          222: ciscoISLvlan
          223: actelisMetaLOOP
          224: fcipLink
          225: rpr
          226: qam
          227: lmp
          228: cblVectaStar
          229: docsCableMCmtsDownstream
          230: adsl2
          231: macSecControlledIF
          232: macSecUncontrolledIF
          233: aviciOpticalEther
          234: atmbond
          235: voiceFGDOS
          236: mocaVersion1
          237: ieee80216WMAN
          238: adsl2plus
          239: dvbRcsMacLayer
          240: dvbTdm
          241: dvbRcsTdma
          242: x86Laps
          243: wwanPP
          244: wwanPP2
          245: voiceEBS
          246: ifPwType
          247: ilan
          248: pip
          249: aluELP
          250: gpon
          251: vdsl2
          252: capwapDot11Profile
          253: capwapDot11Bss
          254: capwapWtpVirtualRadio
          255: bits
          256: docsCableUpstreamRfPort
          257: cableDownstreamRfPort
          258: vmwareVirtualNic
          259: ieee802154
          260: otnOdu
          261: otnOtu
          262: ifVfiType
          263: g9981
          264: g9982
          265: g9983
          266: aluEpon
          267: aluEponOnu
          268: aluEponPhysicalUni
          269: aluEponLogicalLink
          270: aluGponOnu
          271: aluGponPhysicalUni
          272: vmwareNicTeam
          277: docsOfdmDownstream
          278: docsOfdmaUpstream
          279: gfast
          280: sdci
          281: xboxWireless
          282: fastdsl
          283: docsCableScte55d1FwdOob
          284: docsCableScte55d1RetOob
          285: docsCableScte55d2DsOob
          286: docsCableScte55d2UsOob
          287: docsCableNdf
          288: docsCableNdr
          289: ptm
          290: ghn
          291: otnOtsi
          292: otnOtuc
          293: otnOduc
          294: otnOtsig
          295: microwaveCarrierTermination
          296: microwaveRadioLinkTerminal
          297: ieee8021axDrni
          298: ax25
          299: ieee19061nanocom
          300: cpri
          301: omni
          302: roe
      - name: ifMtu
        oid: 1.3.6.1.2.1.2.2.1.4
        type: gauge
        help: The size of the largest packet which can be sent/received on the interface,
          specified in octets - 1.3.6.1.2.1.2.2.1.4
        indexes:
        - labelname: ifIndex
          type: gauge
        lookups:
        - labels:
          - ifIndex
          labelname: ifName
          oid: 1.3.6.1.2.1.31.1.1.1.1
          type: DisplayString
      - name: ifSpeed
        oid: 1.3.6.1.2.1.2.2.1.5
        type: gauge
        help: An estimate of the interface's current bandwidth in bits per second - 1.3.6.1.2.1.2.2.1.5
        indexes:
        - labelname: ifIndex
          type: gauge
        lookups:
        - labels:
          - ifIndex
          labelname: ifName
          oid: 1.3.6.1.2.1.31.1.1.1.1
          type: DisplayString
      - name: ifPhysAddress
        oid: 1.3.6.1.2.1.2.2.1.6
        type: PhysAddress48
        help: The interface's address at its protocol sub-layer - 1.3.6.1.2.1.2.2.1.6
        indexes:
        - labelname: ifIndex
          type: gauge
        lookups:
        - labels:
          - ifIndex
          labelname: ifName
          oid: 1.3.6.1.2.1.31.1.1.1.1
          type: DisplayString
      - name: ifAdminStatus
        oid: 1.3.6.1.2.1.2.2.1.7
        type: gauge
        help: The desired state of the interface - 1.3.6.1.2.1.2.2.1.7
        indexes:
        - labelname: ifIndex
          type: gauge
        lookups:
        - labels:
          - ifIndex
          labelname: ifName
          oid: 1.3.6.1.2.1.31.1.1.1.1
          type: DisplayString
        enum_values:
          1: up
          2: down
          3: testing
      - name: ifOperStatus
        oid: 1.3.6.1.2.1.2.2.1.8
        type: gauge
        help: The current operational state of the interface - 1.3.6.1.2.1.2.2.1.8
        indexes:
        - labelname: ifIndex
          type: gauge
        lookups:
        - labels:
          - ifIndex
          labelname: ifName
          oid: 1.3.6.1.2.1.31.1.1.1.1
          type: DisplayString
        enum_values:
          1: up
          2: down
          3: testing
          4: unknown
          5: dormant
          6: notPresent
          7: lowerLayerDown
      - name: ifLastChange
        oid: 1.3.6.1.2.1.2.2.1.9
        type: gauge
        help: The value of sysUpTime at the time the interface entered its current operational
          state - 1.3.6.1.2.1.2.2.1.9
        indexes:
        - labelname: ifIndex
          type: gauge
        lookups:
        - labels:
          - ifIndex
          labelname: ifName
          oid: 1.3.6.1.2.1.31.1.1.1.1
          type: DisplayString
      - name: ifInOctets
        oid: 1.3.6.1.2.1.2.2.1.10
        type: counter
        help: The total number of octets received on the interface, including framing
          characters - 1.3.6.1.2.1.2.2.1.10
        indexes:
        - labelname: ifIndex
          type: gauge
        lookups:
        - labels:
          - ifIndex
          labelname: ifName
          oid: 1.3.6.1.2.1.31.1.1.1.1
          type: DisplayString
      - name: ifInUcastPkts
        oid: 1.3.6.1.2.1.2.2.1.11
        type: counter
        help: The number of packets, delivered by this sub-layer to a higher (sub-)layer,
          which were not addressed to a multicast or broadcast address at this sub-layer
          - 1.3.6.1.2.1.2.2.1.11
        indexes:
        - labelname: ifIndex
          type: gauge
        lookups:
        - labels:
          - ifIndex
          labelname: ifName
          oid: 1.3.6.1.2.1.31.1.1.1.1
          type: DisplayString
      - name: ifInNUcastPkts
        oid: 1.3.6.1.2.1.2.2.1.12
        type: counter
        help: The number of packets, delivered by this sub-layer to a higher (sub-)layer,
          which were addressed to a multicast or broadcast address at this sub-layer -
          1.3.6.1.2.1.2.2.1.12
        indexes:
        - labelname: ifIndex
          type: gauge
        lookups:
        - labels:
          - ifIndex
          labelname: ifName
          oid: 1.3.6.1.2.1.31.1.1.1.1
          type: DisplayString
      - name: ifInDiscards
        oid: 1.3.6.1.2.1.2.2.1.13
        type: counter
        help: The number of inbound packets which were chosen to be discarded even though
          no errors had been detected to prevent their being deliverable to a higher-layer
          protocol - 1.3.6.1.2.1.2.2.1.13
        indexes:
        - labelname: ifIndex
          type: gauge
        lookups:
        - labels:
          - ifIndex
          labelname: ifName
          oid: 1.3.6.1.2.1.31.1.1.1.1
          type: DisplayString
      - name: ifInErrors
        oid: 1.3.6.1.2.1.2.2.1.14
        type: counter
        help: For packet-oriented interfaces, the number of inbound packets that contained
          errors preventing them from being deliverable to a higher-layer protocol - 1.3.6.1.2.1.2.2.1.14
        indexes:
        - labelname: ifIndex
          type: gauge
        lookups:
        - labels:
          - ifIndex
          labelname: ifName
          oid: 1.3.6.1.2.1.31.1.1.1.1
          type: DisplayString
      - name: ifInUnknownProtos
        oid: 1.3.6.1.2.1.2.2.1.15
        type: counter
        help: For packet-oriented interfaces, the number of packets received via the interface
          which were discarded because of an unknown or unsupported protocol - 1.3.6.1.2.1.2.2.1.15
        indexes:
        - labelname: ifIndex
          type: gauge
        lookups:
        - labels:
          - ifIndex
          labelname: ifName
          oid: 1.3.6.1.2.1.31.1.1.1.1
          type: DisplayString
      - name: ifOutOctets
        oid: 1.3.6.1.2.1.2.2.1.16
        type: counter
        help: The total number of octets transmitted out of the interface, including framing
          characters - 1.3.6.1.2.1.2.2.1.16
        indexes:
        - labelname: ifIndex
          type: gauge
        lookups:
        - labels:
          - ifIndex
          labelname: ifName
          oid: 1.3.6.1.2.1.31.1.1.1.1
          type: DisplayString
      - name: ifOutUcastPkts
        oid: 1.3.6.1.2.1.2.2.1.17
        type: counter
        help: The total number of packets that higher-level protocols requested be transmitted,
          and which were not addressed to a multicast or broadcast address at this sub-layer,
          including those that were discarded or not sent - 1.3.6.1.2.1.2.2.1.17
        indexes:
        - labelname: ifIndex
          type: gauge
        lookups:
        - labels:
          - ifIndex
          labelname: ifName
          oid: 1.3.6.1.2.1.31.1.1.1.1
          type: DisplayString
      - name: ifOutNUcastPkts
        oid: 1.3.6.1.2.1.2.2.1.18
        type: counter
        help: The total number of packets that higher-level protocols requested be transmitted,
          and which were addressed to a multicast or broadcast address at this sub-layer,
          including those that were discarded or not sent - 1.3.6.1.2.1.2.2.1.18
        indexes:
        - labelname: ifIndex
          type: gauge
        lookups:
        - labels:
          - ifIndex
          labelname: ifName
          oid: 1.3.6.1.2.1.31.1.1.1.1
          type: DisplayString
      - name: ifOutDiscards
        oid: 1.3.6.1.2.1.2.2.1.19
        type: counter
        help: The number of outbound packets which were chosen to be discarded even though
          no errors had been detected to prevent their being transmitted - 1.3.6.1.2.1.2.2.1.19
        indexes:
        - labelname: ifIndex
          type: gauge
        lookups:
        - labels:
          - ifIndex
          labelname: ifName
          oid: 1.3.6.1.2.1.31.1.1.1.1
          type: DisplayString
      - name: ifOutErrors
        oid: 1.3.6.1.2.1.2.2.1.20
        type: counter
        help: For packet-oriented interfaces, the number of outbound packets that could
          not be transmitted because of errors - 1.3.6.1.2.1.2.2.1.20
        indexes:
        - labelname: ifIndex
          type: gauge
        lookups:
        - labels:
          - ifIndex
          labelname: ifName
          oid: 1.3.6.1.2.1.31.1.1.1.1
          type: DisplayString
      - name: ifOutQLen
        oid: 1.3.6.1.2.1.2.2.1.21
        type: gauge
        help: The length of the output packet queue (in packets). - 1.3.6.1.2.1.2.2.1.21
        indexes:
        - labelname: ifIndex
          type: gauge
        lookups:
        - labels:
          - ifIndex
          labelname: ifName
          oid: 1.3.6.1.2.1.31.1.1.1.1
          type: DisplayString
      - name: ifSpecific
        oid: 1.3.6.1.2.1.2.2.1.22
        type: OctetString
        help: A reference to MIB definitions specific to the particular media being used
          to realize the interface - 1.3.6.1.2.1.2.2.1.22
        indexes:
        - labelname: ifIndex
          type: gauge
        lookups:
        - labels:
          - ifIndex
          labelname: ifName
          oid: 1.3.6.1.2.1.31.1.1.1.1
          type: DisplayString
      - name: hrSystemUptime
        oid: 1.3.6.1.2.1.25.1.1
        type: gauge
        help: The amount of time since this host was last initialized - 1.3.6.1.2.1.25.1.1
      - name: hrSystemDate
        oid: 1.3.6.1.2.1.25.1.2
        type: DateAndTime
        help: The host's notion of the local date and time of day. - 1.3.6.1.2.1.25.1.2
      - name: hrSystemInitialLoadDevice
        oid: 1.3.6.1.2.1.25.1.3
        type: gauge
        help: The index of the hrDeviceEntry for the device from which this host is configured
          to load its initial operating system configuration (i.e., which operating system
          code and/or boot parameters) - 1.3.6.1.2.1.25.1.3
      - name: hrSystemInitialLoadParameters
        oid: 1.3.6.1.2.1.25.1.4
        type: OctetString
        help: This object contains the parameters (e.g - 1.3.6.1.2.1.25.1.4
      - name: hrSystemNumUsers
        oid: 1.3.6.1.2.1.25.1.5
        type: gauge
        help: The number of user sessions for which this host is storing state information
          - 1.3.6.1.2.1.25.1.5
      - name: hrSystemProcesses
        oid: 1.3.6.1.2.1.25.1.6
        type: gauge
        help: The number of process contexts currently loaded or running on this system.
          - 1.3.6.1.2.1.25.1.6
      - name: hrSystemMaxProcesses
        oid: 1.3.6.1.2.1.25.1.7
        type: gauge
        help: The maximum number of process contexts this system can support - 1.3.6.1.2.1.25.1.7
      - name: hrMemorySize
        oid: 1.3.6.1.2.1.25.2.2
        type: gauge
        help: The amount of physical read-write main memory, typically RAM, contained
          by the host. - 1.3.6.1.2.1.25.2.2
      - name: hrStorageIndex
        oid: 1.3.6.1.2.1.25.2.3.1.1
        type: gauge
        help: A unique value for each logical storage area contained by the host. - 1.3.6.1.2.1.25.2.3.1.1
        indexes:
        - labelname: hrStorageIndex
          type: gauge
        lookups:
        - labels:
          - hrStorageIndex
          labelname: hrStorageDescr
          oid: 1.3.6.1.2.1.25.2.3.1.3
          type: DisplayString
      - name: hrStorageType
        oid: 1.3.6.1.2.1.25.2.3.1.2
        type: OctetString
        help: The type of storage represented by this entry. - 1.3.6.1.2.1.25.2.3.1.2
        indexes:
        - labelname: hrStorageIndex
          type: gauge
        lookups:
        - labels:
          - hrStorageIndex
          labelname: hrStorageDescr
          oid: 1.3.6.1.2.1.25.2.3.1.3
          type: DisplayString
      - name: hrStorageDescr
        oid: 1.3.6.1.2.1.25.2.3.1.3
        type: DisplayString
        help: A description of the type and instance of the storage described by this
          entry. - 1.3.6.1.2.1.25.2.3.1.3
        indexes:
        - labelname: hrStorageIndex
          type: gauge
        lookups:
        - labels:
          - hrStorageIndex
          labelname: hrStorageDescr
          oid: 1.3.6.1.2.1.25.2.3.1.3
          type: DisplayString
      - name: hrStorageAllocationUnits
        oid: 1.3.6.1.2.1.25.2.3.1.4
        type: gauge
        help: The size, in bytes, of the data objects allocated from this pool - 1.3.6.1.2.1.25.2.3.1.4
        indexes:
        - labelname: hrStorageIndex
          type: gauge
        lookups:
        - labels:
          - hrStorageIndex
          labelname: hrStorageDescr
          oid: 1.3.6.1.2.1.25.2.3.1.3
          type: DisplayString
      - name: hrStorageSize
        oid: 1.3.6.1.2.1.25.2.3.1.5
        type: gauge
        help: The size of the storage represented by this entry, in units of hrStorageAllocationUnits
          - 1.3.6.1.2.1.25.2.3.1.5
        indexes:
        - labelname: hrStorageIndex
          type: gauge
        lookups:
        - labels:
          - hrStorageIndex
          labelname: hrStorageDescr
          oid: 1.3.6.1.2.1.25.2.3.1.3
          type: DisplayString
      - name: hrStorageUsed
        oid: 1.3.6.1.2.1.25.2.3.1.6
        type: gauge
        help: The amount of the storage represented by this entry that is allocated, in
          units of hrStorageAllocationUnits. - 1.3.6.1.2.1.25.2.3.1.6
        indexes:
        - labelname: hrStorageIndex
          type: gauge
        lookups:
        - labels:
          - hrStorageIndex
          labelname: hrStorageDescr
          oid: 1.3.6.1.2.1.25.2.3.1.3
          type: DisplayString
      - name: hrStorageAllocationFailures
        oid: 1.3.6.1.2.1.25.2.3.1.7
        type: counter
        help: The number of requests for storage represented by this entry that could
          not be honored due to not enough storage - 1.3.6.1.2.1.25.2.3.1.7
        indexes:
        - labelname: hrStorageIndex
          type: gauge
        lookups:
        - labels:
          - hrStorageIndex
          labelname: hrStorageDescr
          oid: 1.3.6.1.2.1.25.2.3.1.3
          type: DisplayString
      - name: hrDeviceIndex
        oid: 1.3.6.1.2.1.25.3.2.1.1
        type: gauge
        help: A unique value for each device contained by the host - 1.3.6.1.2.1.25.3.2.1.1
        indexes:
        - labelname: hrDeviceIndex
          type: gauge
      - name: hrDeviceType
        oid: 1.3.6.1.2.1.25.3.2.1.2
        type: OctetString
        help: An indication of the type of device - 1.3.6.1.2.1.25.3.2.1.2
        indexes:
        - labelname: hrDeviceIndex
          type: gauge
      - name: hrDeviceDescr
        oid: 1.3.6.1.2.1.25.3.2.1.3
        type: DisplayString
        help: A textual description of this device, including the device's manufacturer
          and revision, and optionally, its serial number. - 1.3.6.1.2.1.25.3.2.1.3
        indexes:
        - labelname: hrDeviceIndex
          type: gauge
      - name: hrDeviceID
        oid: 1.3.6.1.2.1.25.3.2.1.4
        type: OctetString
        help: The product ID for this device. - 1.3.6.1.2.1.25.3.2.1.4
        indexes:
        - labelname: hrDeviceIndex
          type: gauge
      - name: hrDeviceStatus
        oid: 1.3.6.1.2.1.25.3.2.1.5
        type: gauge
        help: The current operational state of the device described by this row of the
          table - 1.3.6.1.2.1.25.3.2.1.5
        indexes:
        - labelname: hrDeviceIndex
          type: gauge
        enum_values:
          1: unknown
          2: running
          3: warning
          4: testing
          5: down
      - name: hrDeviceErrors
        oid: 1.3.6.1.2.1.25.3.2.1.6
        type: counter
        help: The number of errors detected on this device - 1.3.6.1.2.1.25.3.2.1.6
        indexes:
        - labelname: hrDeviceIndex
          type: gauge
      - name: hrProcessorFrwID
        oid: 1.3.6.1.2.1.25.3.3.1.1
        type: OctetString
        help: The product ID of the firmware associated with the processor. - 1.3.6.1.2.1.25.3.3.1.1
        indexes:
        - labelname: hrDeviceIndex
          type: gauge
      - name: hrProcessorLoad
        oid: 1.3.6.1.2.1.25.3.3.1.2
        type: gauge
        help: The average, over the last minute, of the percentage of time that this processor
          was not idle - 1.3.6.1.2.1.25.3.3.1.2
        indexes:
        - labelname: hrDeviceIndex
          type: gauge
      - name: hrNetworkIfIndex
        oid: 1.3.6.1.2.1.25.3.4.1.1
        type: gauge
        help: The value of ifIndex which corresponds to this network device - 1.3.6.1.2.1.25.3.4.1.1
        indexes:
        - labelname: hrDeviceIndex
          type: gauge
      - name: hrPrinterStatus
        oid: 1.3.6.1.2.1.25.3.5.1.1
        type: gauge
        help: The current status of this printer device. - 1.3.6.1.2.1.25.3.5.1.1
        indexes:
        - labelname: hrDeviceIndex
          type: gauge
        enum_values:
          1: other
          2: unknown
          3: idle
          4: printing
          5: warmup
      - name: hrPrinterDetectedErrorState
        oid: 1.3.6.1.2.1.25.3.5.1.2
        type: OctetString
        help: This object represents any error conditions detected by the printer - 1.3.6.1.2.1.25.3.5.1.2
        indexes:
        - labelname: hrDeviceIndex
          type: gauge
      - name: hrDiskStorageAccess
        oid: 1.3.6.1.2.1.25.3.6.1.1
        type: gauge
        help: An indication if this long-term storage device is readable and writable
          or only readable - 1.3.6.1.2.1.25.3.6.1.1
        indexes:
        - labelname: hrDeviceIndex
          type: gauge
        enum_values:
          1: readWrite
          2: readOnly
      - name: hrDiskStorageMedia
        oid: 1.3.6.1.2.1.25.3.6.1.2
        type: gauge
        help: An indication of the type of media used in this long- term storage device.
          - 1.3.6.1.2.1.25.3.6.1.2
        indexes:
        - labelname: hrDeviceIndex
          type: gauge
        enum_values:
          1: other
          2: unknown
          3: hardDisk
          4: floppyDisk
          5: opticalDiskROM
          6: opticalDiskWORM
          7: opticalDiskRW
          8: ramDisk
      - name: hrDiskStorageRemoveble
        oid: 1.3.6.1.2.1.25.3.6.1.3
        type: gauge
        help: Denotes whether or not the disk media may be removed from the drive. - 1.3.6.1.2.1.25.3.6.1.3
        indexes:
        - labelname: hrDeviceIndex
          type: gauge
        enum_values:
          1: "true"
          2: "false"
      - name: hrDiskStorageCapacity
        oid: 1.3.6.1.2.1.25.3.6.1.4
        type: gauge
        help: The total size for this long-term storage device - 1.3.6.1.2.1.25.3.6.1.4
        indexes:
        - labelname: hrDeviceIndex
          type: gauge
      - name: hrPartitionIndex
        oid: 1.3.6.1.2.1.25.3.7.1.1
        type: gauge
        help: A unique value for each partition on this long-term storage device - 1.3.6.1.2.1.25.3.7.1.1
        indexes:
        - labelname: hrDeviceIndex
          type: gauge
        - labelname: hrPartitionIndex
          type: gauge
      - name: hrPartitionLabel
        oid: 1.3.6.1.2.1.25.3.7.1.2
        type: OctetString
        help: A textual description of this partition. - 1.3.6.1.2.1.25.3.7.1.2
        indexes:
        - labelname: hrDeviceIndex
          type: gauge
        - labelname: hrPartitionIndex
          type: gauge
      - name: hrPartitionID
        oid: 1.3.6.1.2.1.25.3.7.1.3
        type: OctetString
        help: A descriptor which uniquely represents this partition to the responsible
          operating system - 1.3.6.1.2.1.25.3.7.1.3
        indexes:
        - labelname: hrDeviceIndex
          type: gauge
        - labelname: hrPartitionIndex
          type: gauge
      - name: hrPartitionSize
        oid: 1.3.6.1.2.1.25.3.7.1.4
        type: gauge
        help: The size of this partition. - 1.3.6.1.2.1.25.3.7.1.4
        indexes:
        - labelname: hrDeviceIndex
          type: gauge
        - labelname: hrPartitionIndex
          type: gauge
      - name: hrPartitionFSIndex
        oid: 1.3.6.1.2.1.25.3.7.1.5
        type: gauge
        help: The index of the file system mounted on this partition - 1.3.6.1.2.1.25.3.7.1.5
        indexes:
        - labelname: hrDeviceIndex
          type: gauge
        - labelname: hrPartitionIndex
          type: gauge
      - name: hrFSIndex
        oid: 1.3.6.1.2.1.25.3.8.1.1
        type: gauge
        help: A unique value for each file system local to this host - 1.3.6.1.2.1.25.3.8.1.1
        indexes:
        - labelname: hrFSIndex
          type: gauge
      - name: hrFSMountPoint
        oid: 1.3.6.1.2.1.25.3.8.1.2
        type: OctetString
        help: The path name of the root of this file system. - 1.3.6.1.2.1.25.3.8.1.2
        indexes:
        - labelname: hrFSIndex
          type: gauge
      - name: hrFSRemoteMountPoint
        oid: 1.3.6.1.2.1.25.3.8.1.3
        type: OctetString
        help: A description of the name and/or address of the server that this file system
          is mounted from - 1.3.6.1.2.1.25.3.8.1.3
        indexes:
        - labelname: hrFSIndex
          type: gauge
      - name: hrFSType
        oid: 1.3.6.1.2.1.25.3.8.1.4
        type: OctetString
        help: The value of this object identifies the type of this file system. - 1.3.6.1.2.1.25.3.8.1.4
        indexes:
        - labelname: hrFSIndex
          type: gauge
      - name: hrFSAccess
        oid: 1.3.6.1.2.1.25.3.8.1.5
        type: gauge
        help: An indication if this file system is logically configured by the operating
          system to be readable and writable or only readable - 1.3.6.1.2.1.25.3.8.1.5
        indexes:
        - labelname: hrFSIndex
          type: gauge
        enum_values:
          1: readWrite
          2: readOnly
      - name: hrFSBootable
        oid: 1.3.6.1.2.1.25.3.8.1.6
        type: gauge
        help: A flag indicating whether this file system is bootable. - 1.3.6.1.2.1.25.3.8.1.6
        indexes:
        - labelname: hrFSIndex
          type: gauge
        enum_values:
          1: "true"
          2: "false"
      - name: hrFSStorageIndex
        oid: 1.3.6.1.2.1.25.3.8.1.7
        type: gauge
        help: The index of the hrStorageEntry that represents information about this file
          system - 1.3.6.1.2.1.25.3.8.1.7
        indexes:
        - labelname: hrFSIndex
          type: gauge
      - name: hrFSLastFullBackupDate
        oid: 1.3.6.1.2.1.25.3.8.1.8
        type: DateAndTime
        help: The last date at which this complete file system was copied to another storage
          device for backup - 1.3.6.1.2.1.25.3.8.1.8
        indexes:
        - labelname: hrFSIndex
          type: gauge
      - name: hrFSLastPartialBackupDate
        oid: 1.3.6.1.2.1.25.3.8.1.9
        type: DateAndTime
        help: The last date at which a portion of this file system was copied to another
          storage device for backup - 1.3.6.1.2.1.25.3.8.1.9
        indexes:
        - labelname: hrFSIndex
          type: gauge
      - name: hrSWOSIndex
        oid: 1.3.6.1.2.1.25.4.1
        type: gauge
        help: The value of the hrSWRunIndex for the hrSWRunEntry that represents the primary
          operating system running on this host - 1.3.6.1.2.1.25.4.1
      - name: hrSWRunIndex
        oid: 1.3.6.1.2.1.25.4.2.1.1
        type: gauge
        help: A unique value for each piece of software running on the host - 1.3.6.1.2.1.25.4.2.1.1
        indexes:
        - labelname: hrSWRunIndex
          type: gauge
      - name: hrSWRunName
        oid: 1.3.6.1.2.1.25.4.2.1.2
        type: OctetString
        help: A textual description of this running piece of software, including the manufacturer,
          revision, and the name by which it is commonly known - 1.3.6.1.2.1.25.4.2.1.2
        indexes:
        - labelname: hrSWRunIndex
          type: gauge
      - name: hrSWRunID
        oid: 1.3.6.1.2.1.25.4.2.1.3
        type: OctetString
        help: The product ID of this running piece of software. - 1.3.6.1.2.1.25.4.2.1.3
        indexes:
        - labelname: hrSWRunIndex
          type: gauge
      - name: hrSWRunPath
        oid: 1.3.6.1.2.1.25.4.2.1.4
        type: OctetString
        help: A description of the location on long-term storage (e.g - 1.3.6.1.2.1.25.4.2.1.4
        indexes:
        - labelname: hrSWRunIndex
          type: gauge
      - name: hrSWRunParameters
        oid: 1.3.6.1.2.1.25.4.2.1.5
        type: OctetString
        help: A description of the parameters supplied to this software when it was initially
          loaded. - 1.3.6.1.2.1.25.4.2.1.5
        indexes:
        - labelname: hrSWRunIndex
          type: gauge
      - name: hrSWRunType
        oid: 1.3.6.1.2.1.25.4.2.1.6
        type: gauge
        help: The type of this software. - 1.3.6.1.2.1.25.4.2.1.6
        indexes:
        - labelname: hrSWRunIndex
          type: gauge
        enum_values:
          1: unknown
          2: operatingSystem
          3: deviceDriver
          4: application
      - name: hrSWRunStatus
        oid: 1.3.6.1.2.1.25.4.2.1.7
        type: gauge
        help: The status of this running piece of software - 1.3.6.1.2.1.25.4.2.1.7
        indexes:
        - labelname: hrSWRunIndex
          type: gauge
        enum_values:
          1: running
          2: runnable
          3: notRunnable
          4: invalid
      - name: hrSWRunPerfCPU
        oid: 1.3.6.1.2.1.25.5.1.1.1
        type: gauge
        help: The number of centi-seconds of the total system's CPU resources consumed
          by this process - 1.3.6.1.2.1.25.5.1.1.1
        indexes:
        - labelname: hrSWRunIndex
          type: gauge
      - name: hrSWRunPerfMem
        oid: 1.3.6.1.2.1.25.5.1.1.2
        type: gauge
        help: The total amount of real system memory allocated to this process. - 1.3.6.1.2.1.25.5.1.1.2
        indexes:
        - labelname: hrSWRunIndex
          type: gauge
      - name: hrSWInstalledLastChange
        oid: 1.3.6.1.2.1.25.6.1
        type: gauge
        help: The value of sysUpTime when an entry in the hrSWInstalledTable was last
          added, renamed, or deleted - 1.3.6.1.2.1.25.6.1
      - name: hrSWInstalledLastUpdateTime
        oid: 1.3.6.1.2.1.25.6.2
        type: gauge
        help: The value of sysUpTime when the hrSWInstalledTable was last completely updated
          - 1.3.6.1.2.1.25.6.2
      - name: hrSWInstalledIndex
        oid: 1.3.6.1.2.1.25.6.3.1.1
        type: gauge
        help: A unique value for each piece of software installed on the host - 1.3.6.1.2.1.25.6.3.1.1
        indexes:
        - labelname: hrSWInstalledIndex
          type: gauge
      - name: hrSWInstalledName
        oid: 1.3.6.1.2.1.25.6.3.1.2
        type: OctetString
        help: A textual description of this installed piece of software, including the
          manufacturer, revision, the name by which it is commonly known, and optionally,
          its serial number. - 1.3.6.1.2.1.25.6.3.1.2
        indexes:
        - labelname: hrSWInstalledIndex
          type: gauge
      - name: hrSWInstalledID
        oid: 1.3.6.1.2.1.25.6.3.1.3
        type: OctetString
        help: The product ID of this installed piece of software. - 1.3.6.1.2.1.25.6.3.1.3
        indexes:
        - labelname: hrSWInstalledIndex
          type: gauge
      - name: hrSWInstalledType
        oid: 1.3.6.1.2.1.25.6.3.1.4
        type: gauge
        help: The type of this software. - 1.3.6.1.2.1.25.6.3.1.4
        indexes:
        - labelname: hrSWInstalledIndex
          type: gauge
        enum_values:
          1: unknown
          2: operatingSystem
          3: deviceDriver
          4: application
      - name: hrSWInstalledDate
        oid: 1.3.6.1.2.1.25.6.3.1.5
        type: DateAndTime
        help: The last-modification date of this application as it would appear in a directory
          listing - 1.3.6.1.2.1.25.6.3.1.5
        indexes:
        - labelname: hrSWInstalledIndex
          type: gauge
      - name: ifInMulticastPkts
        oid: 1.3.6.1.2.1.31.1.1.1.2
        type: counter
        help: The number of packets, delivered by this sub-layer to a higher (sub-)layer,
          which were addressed to a multicast address at this sub-layer - 1.3.6.1.2.1.31.1.1.1.2
        indexes:
        - labelname: ifIndex
          type: gauge
        lookups:
        - labels:
          - ifIndex
          labelname: ifName
          oid: 1.3.6.1.2.1.31.1.1.1.1
          type: DisplayString
      - name: ifInBroadcastPkts
        oid: 1.3.6.1.2.1.31.1.1.1.3
        type: counter
        help: The number of packets, delivered by this sub-layer to a higher (sub-)layer,
          which were addressed to a broadcast address at this sub-layer - 1.3.6.1.2.1.31.1.1.1.3
        indexes:
        - labelname: ifIndex
          type: gauge
        lookups:
        - labels:
          - ifIndex
          labelname: ifName
          oid: 1.3.6.1.2.1.31.1.1.1.1
          type: DisplayString
      - name: ifOutMulticastPkts
        oid: 1.3.6.1.2.1.31.1.1.1.4
        type: counter
        help: The total number of packets that higher-level protocols requested be transmitted,
          and which were addressed to a multicast address at this sub-layer, including
          those that were discarded or not sent - 1.3.6.1.2.1.31.1.1.1.4
        indexes:
        - labelname: ifIndex
          type: gauge
        lookups:
        - labels:
          - ifIndex
          labelname: ifName
          oid: 1.3.6.1.2.1.31.1.1.1.1
          type: DisplayString
      - name: ifOutBroadcastPkts
        oid: 1.3.6.1.2.1.31.1.1.1.5
        type: counter
        help: The total number of packets that higher-level protocols requested be transmitted,
          and which were addressed to a broadcast address at this sub-layer, including
          those that were discarded or not sent - 1.3.6.1.2.1.31.1.1.1.5
        indexes:
        - labelname: ifIndex
          type: gauge
        lookups:
        - labels:
          - ifIndex
          labelname: ifName
          oid: 1.3.6.1.2.1.31.1.1.1.1
          type: DisplayString
      - name: ifHCInOctets
        oid: 1.3.6.1.2.1.31.1.1.1.6
        type: counter
        help: The total number of octets received on the interface, including framing
          characters - 1.3.6.1.2.1.31.1.1.1.6
        indexes:
        - labelname: ifIndex
          type: gauge
        lookups:
        - labels:
          - ifIndex
          labelname: ifName
          oid: 1.3.6.1.2.1.31.1.1.1.1
          type: DisplayString
      - name: ifHCInUcastPkts
        oid: 1.3.6.1.2.1.31.1.1.1.7
        type: counter
        help: The number of packets, delivered by this sub-layer to a higher (sub-)layer,
          which were not addressed to a multicast or broadcast address at this sub-layer
          - 1.3.6.1.2.1.31.1.1.1.7
        indexes:
        - labelname: ifIndex
          type: gauge
        lookups:
        - labels:
          - ifIndex
          labelname: ifName
          oid: 1.3.6.1.2.1.31.1.1.1.1
          type: DisplayString
      - name: ifHCInMulticastPkts
        oid: 1.3.6.1.2.1.31.1.1.1.8
        type: counter
        help: The number of packets, delivered by this sub-layer to a higher (sub-)layer,
          which were addressed to a multicast address at this sub-layer - 1.3.6.1.2.1.31.1.1.1.8
        indexes:
        - labelname: ifIndex
          type: gauge
        lookups:
        - labels:
          - ifIndex
          labelname: ifName
          oid: 1.3.6.1.2.1.31.1.1.1.1
          type: DisplayString
      - name: ifHCInBroadcastPkts
        oid: 1.3.6.1.2.1.31.1.1.1.9
        type: counter
        help: The number of packets, delivered by this sub-layer to a higher (sub-)layer,
          which were addressed to a broadcast address at this sub-layer - 1.3.6.1.2.1.31.1.1.1.9
        indexes:
        - labelname: ifIndex
          type: gauge
        lookups:
        - labels:
          - ifIndex
          labelname: ifName
          oid: 1.3.6.1.2.1.31.1.1.1.1
          type: DisplayString
      - name: ifHCOutOctets
        oid: 1.3.6.1.2.1.31.1.1.1.10
        type: counter
        help: The total number of octets transmitted out of the interface, including framing
          characters - 1.3.6.1.2.1.31.1.1.1.10
        indexes:
        - labelname: ifIndex
          type: gauge
        lookups:
        - labels:
          - ifIndex
          labelname: ifName
          oid: 1.3.6.1.2.1.31.1.1.1.1
          type: DisplayString
      - name: ifHCOutUcastPkts
        oid: 1.3.6.1.2.1.31.1.1.1.11
        type: counter
        help: The total number of packets that higher-level protocols requested be transmitted,
          and which were not addressed to a multicast or broadcast address at this sub-layer,
          including those that were discarded or not sent - 1.3.6.1.2.1.31.1.1.1.11
        indexes:
        - labelname: ifIndex
          type: gauge
        lookups:
        - labels:
          - ifIndex
          labelname: ifName
          oid: 1.3.6.1.2.1.31.1.1.1.1
          type: DisplayString
      - name: ifHCOutMulticastPkts
        oid: 1.3.6.1.2.1.31.1.1.1.12
        type: counter
        help: The total number of packets that higher-level protocols requested be transmitted,
          and which were addressed to a multicast address at this sub-layer, including
          those that were discarded or not sent - 1.3.6.1.2.1.31.1.1.1.12
        indexes:
        - labelname: ifIndex
          type: gauge
        lookups:
        - labels:
          - ifIndex
          labelname: ifName
          oid: 1.3.6.1.2.1.31.1.1.1.1
          type: DisplayString
      - name: ifHCOutBroadcastPkts
        oid: 1.3.6.1.2.1.31.1.1.1.13
        type: counter
        help: The total number of packets that higher-level protocols requested be transmitted,
          and which were addressed to a broadcast address at this sub-layer, including
          those that were discarded or not sent - 1.3.6.1.2.1.31.1.1.1.13
        indexes:
        - labelname: ifIndex
          type: gauge
        lookups:
        - labels:
          - ifIndex
          labelname: ifName
          oid: 1.3.6.1.2.1.31.1.1.1.1
          type: DisplayString
      - name: ifLinkUpDownTrapEnable
        oid: 1.3.6.1.2.1.31.1.1.1.14
        type: gauge
        help: Indicates whether linkUp/linkDown traps should be generated for this interface
          - 1.3.6.1.2.1.31.1.1.1.14
        indexes:
        - labelname: ifIndex
          type: gauge
        lookups:
        - labels:
          - ifIndex
          labelname: ifName
          oid: 1.3.6.1.2.1.31.1.1.1.1
          type: DisplayString
        enum_values:
          1: enabled
          2: disabled
      - name: ifHighSpeed
        oid: 1.3.6.1.2.1.31.1.1.1.15
        type: gauge
        help: An estimate of the interface's current bandwidth in units of 1,000,000 bits
          per second - 1.3.6.1.2.1.31.1.1.1.15
        indexes:
        - labelname: ifIndex
          type: gauge
        lookups:
        - labels:
          - ifIndex
          labelname: ifName
          oid: 1.3.6.1.2.1.31.1.1.1.1
          type: DisplayString
      - name: ifPromiscuousMode
        oid: 1.3.6.1.2.1.31.1.1.1.16
        type: gauge
        help: This object has a value of false(2) if this interface only accepts packets/frames
          that are addressed to this station - 1.3.6.1.2.1.31.1.1.1.16
        indexes:
        - labelname: ifIndex
          type: gauge
        lookups:
        - labels:
          - ifIndex
          labelname: ifName
          oid: 1.3.6.1.2.1.31.1.1.1.1
          type: DisplayString
        enum_values:
          1: "true"
          2: "false"
      - name: ifConnectorPresent
        oid: 1.3.6.1.2.1.31.1.1.1.17
        type: gauge
        help: This object has the value 'true(1)' if the interface sublayer has a physical
          connector and the value 'false(2)' otherwise. - 1.3.6.1.2.1.31.1.1.1.17
        indexes:
        - labelname: ifIndex
          type: gauge
        lookups:
        - labels:
          - ifIndex
          labelname: ifName
          oid: 1.3.6.1.2.1.31.1.1.1.1
          type: DisplayString
        enum_values:
          1: "true"
          2: "false"
      - name: ifAlias
        oid: 1.3.6.1.2.1.31.1.1.1.18
        type: DisplayString
        help: This object is an 'alias' name for the interface as specified by a network
          manager, and provides a non-volatile 'handle' for the interface - 1.3.6.1.2.1.31.1.1.1.18
        indexes:
        - labelname: ifIndex
          type: gauge
        lookups:
        - labels:
          - ifIndex
          labelname: ifName
          oid: 1.3.6.1.2.1.31.1.1.1.1
          type: DisplayString
      - name: ifCounterDiscontinuityTime
        oid: 1.3.6.1.2.1.31.1.1.1.19
        type: gauge
        help: The value of sysUpTime on the most recent occasion at which any one or more
          of this interface's counters suffered a discontinuity - 1.3.6.1.2.1.31.1.1.1.19
        indexes:
        - labelname: ifIndex
          type: gauge
        lookups:
        - labels:
          - ifIndex
          labelname: ifName
          oid: 1.3.6.1.2.1.31.1.1.1.1
          type: DisplayString
      - name: ifStackHigherLayer
        oid: 1.3.6.1.2.1.31.1.2.1.1
        type: gauge
        help: The value of ifIndex corresponding to the higher sub-layer of the relationship,
          i.e., the sub-layer which runs on 'top' of the sub-layer identified by the corresponding
          instance of ifStackLowerLayer - 1.3.6.1.2.1.31.1.2.1.1
        indexes:
        - labelname: ifStackHigherLayer
          type: gauge
        - labelname: ifStackLowerLayer
          type: gauge
      - name: ifStackLowerLayer
        oid: 1.3.6.1.2.1.31.1.2.1.2
        type: gauge
        help: The value of ifIndex corresponding to the lower sub-layer of the relationship,
          i.e., the sub-layer which runs 'below' the sub-layer identified by the corresponding
          instance of ifStackHigherLayer - 1.3.6.1.2.1.31.1.2.1.2
        indexes:
        - labelname: ifStackHigherLayer
          type: gauge
        - labelname: ifStackLowerLayer
          type: gauge
      - name: ifStackStatus
        oid: 1.3.6.1.2.1.31.1.2.1.3
        type: gauge
        help: The status of the relationship between two sub-layers - 1.3.6.1.2.1.31.1.2.1.3
        indexes:
        - labelname: ifStackHigherLayer
          type: gauge
        - labelname: ifStackLowerLayer
          type: gauge
        enum_values:
          1: active
          2: notInService
          3: notReady
          4: createAndGo
          5: createAndWait
          6: destroy
      - name: ifTestId
        oid: 1.3.6.1.2.1.31.1.3.1.1
        type: gauge
        help: This object identifies the current invocation of the interface's test. -
          1.3.6.1.2.1.31.1.3.1.1
        indexes:
        - labelname: ifIndex
          type: gauge
        lookups:
        - labels:
          - ifIndex
          labelname: ifName
          oid: 1.3.6.1.2.1.31.1.1.1.1
          type: DisplayString
      - name: ifTestStatus
        oid: 1.3.6.1.2.1.31.1.3.1.2
        type: gauge
        help: This object indicates whether or not some manager currently has the necessary
          'ownership' required to invoke a test on this interface - 1.3.6.1.2.1.31.1.3.1.2
        indexes:
        - labelname: ifIndex
          type: gauge
        lookups:
        - labels:
          - ifIndex
          labelname: ifName
          oid: 1.3.6.1.2.1.31.1.1.1.1
          type: DisplayString
        enum_values:
          1: notInUse
          2: inUse
      - name: ifTestType
        oid: 1.3.6.1.2.1.31.1.3.1.3
        type: OctetString
        help: A control variable used to start and stop operator- initiated interface
          tests - 1.3.6.1.2.1.31.1.3.1.3
        indexes:
        - labelname: ifIndex
          type: gauge
        lookups:
        - labels:
          - ifIndex
          labelname: ifName
          oid: 1.3.6.1.2.1.31.1.1.1.1
          type: DisplayString
      - name: ifTestResult
        oid: 1.3.6.1.2.1.31.1.3.1.4
        type: gauge
        help: This object contains the result of the most recently requested test, or
          the value none(1) if no tests have been requested since the last reset - 1.3.6.1.2.1.31.1.3.1.4
        indexes:
        - labelname: ifIndex
          type: gauge
        lookups:
        - labels:
          - ifIndex
          labelname: ifName
          oid: 1.3.6.1.2.1.31.1.1.1.1
          type: DisplayString
        enum_values:
          1: none
          2: success
          3: inProgress
          4: notSupported
          5: unAbleToRun
          6: aborted
          7: failed
      - name: ifTestCode
        oid: 1.3.6.1.2.1.31.1.3.1.5
        type: OctetString
        help: This object contains a code which contains more specific information on
          the test result, for example an error-code after a failed test - 1.3.6.1.2.1.31.1.3.1.5
        indexes:
        - labelname: ifIndex
          type: gauge
        lookups:
        - labels:
          - ifIndex
          labelname: ifName
          oid: 1.3.6.1.2.1.31.1.1.1.1
          type: DisplayString
      - name: ifTestOwner
        oid: 1.3.6.1.2.1.31.1.3.1.6
        type: DisplayString
        help: The entity which currently has the 'ownership' required to invoke a test
          on this interface. - 1.3.6.1.2.1.31.1.3.1.6
        indexes:
        - labelname: ifIndex
          type: gauge
        lookups:
        - labels:
          - ifIndex
          labelname: ifName
          oid: 1.3.6.1.2.1.31.1.1.1.1
          type: DisplayString
      - name: ifRcvAddressAddress
        oid: 1.3.6.1.2.1.31.1.4.1.1
        type: PhysAddress48
        help: An address for which the system will accept packets/frames on this entry's
          interface. - 1.3.6.1.2.1.31.1.4.1.1
        indexes:
        - labelname: ifIndex
          type: gauge
        - labelname: ifRcvAddressAddress
          type: PhysAddress48
        lookups:
        - labels:
          - ifIndex
          labelname: ifName
          oid: 1.3.6.1.2.1.31.1.1.1.1
          type: DisplayString
      - name: ifRcvAddressStatus
        oid: 1.3.6.1.2.1.31.1.4.1.2
        type: gauge
        help: This object is used to create and delete rows in the ifRcvAddressTable.
          - 1.3.6.1.2.1.31.1.4.1.2
        indexes:
        - labelname: ifIndex
          type: gauge
        - labelname: ifRcvAddressAddress
          type: PhysAddress48
        lookups:
        - labels:
          - ifIndex
          labelname: ifName
          oid: 1.3.6.1.2.1.31.1.1.1.1
          type: DisplayString
        enum_values:
          1: active
          2: notInService
          3: notReady
          4: createAndGo
          5: createAndWait
          6: destroy
      - name: ifRcvAddressType
        oid: 1.3.6.1.2.1.31.1.4.1.3
        type: gauge
        help: This object has the value nonVolatile(3) for those entries in the table
          which are valid and will not be deleted by the next restart of the managed system
          - 1.3.6.1.2.1.31.1.4.1.3
        indexes:
        - labelname: ifIndex
          type: gauge
        - labelname: ifRcvAddressAddress
          type: PhysAddress48
        lookups:
        - labels:
          - ifIndex
          labelname: ifName
          oid: 1.3.6.1.2.1.31.1.1.1.1
          type: DisplayString
        enum_values:
          1: other
          2: volatile
          3: nonVolatile
      - name: ifTableLastChange
        oid: 1.3.6.1.2.1.31.1.5
        type: gauge
        help: The value of sysUpTime at the time of the last creation or deletion of an
          entry in the ifTable - 1.3.6.1.2.1.31.1.5
      - name: ifStackLastChange
        oid: 1.3.6.1.2.1.31.1.6
        type: gauge
        help: The value of sysUpTime at the time of the last change of the (whole) interface
          stack - 1.3.6.1.2.1.31.1.6
      - name: mtxrWlStatIndex
        oid: 1.3.6.1.4.1.14988.1.1.1.1.1.1
        type: gauge
        help: ' - 1.3.6.1.4.1.14988.1.1.1.1.1.1'
        indexes:
        - labelname: mtxrWlStatIndex
          type: gauge
      - name: mtxrWlStatTxRate
        oid: 1.3.6.1.4.1.14988.1.1.1.1.1.2
        type: gauge
        help: bits per second - 1.3.6.1.4.1.14988.1.1.1.1.1.2
        indexes:
        - labelname: mtxrWlStatIndex
          type: gauge
      - name: mtxrWlStatRxRate
        oid: 1.3.6.1.4.1.14988.1.1.1.1.1.3
        type: gauge
        help: bits per second - 1.3.6.1.4.1.14988.1.1.1.1.1.3
        indexes:
        - labelname: mtxrWlStatIndex
          type: gauge
      - name: mtxrWlStatStrength
        oid: 1.3.6.1.4.1.14988.1.1.1.1.1.4
        type: gauge
        help: dBm - 1.3.6.1.4.1.14988.1.1.1.1.1.4
        indexes:
        - labelname: mtxrWlStatIndex
          type: gauge
      - name: mtxrWlStatSsid
        oid: 1.3.6.1.4.1.14988.1.1.1.1.1.5
        type: DisplayString
        help: ' - 1.3.6.1.4.1.14988.1.1.1.1.1.5'
        indexes:
        - labelname: mtxrWlStatIndex
          type: gauge
      - name: mtxrWlStatBssid
        oid: 1.3.6.1.4.1.14988.1.1.1.1.1.6
        type: PhysAddress48
        help: ' - 1.3.6.1.4.1.14988.1.1.1.1.1.6'
        indexes:
        - labelname: mtxrWlStatIndex
          type: gauge
      - name: mtxrWlStatFreq
        oid: 1.3.6.1.4.1.14988.1.1.1.1.1.7
        type: gauge
        help: megahertz - 1.3.6.1.4.1.14988.1.1.1.1.1.7
        indexes:
        - labelname: mtxrWlStatIndex
          type: gauge
      - name: mtxrWlStatBand
        oid: 1.3.6.1.4.1.14988.1.1.1.1.1.8
        type: DisplayString
        help: ' - 1.3.6.1.4.1.14988.1.1.1.1.1.8'
        indexes:
        - labelname: mtxrWlStatIndex
          type: gauge
      - name: mtxrWlStatTxCCQ
        oid: 1.3.6.1.4.1.14988.1.1.1.1.1.9
        type: counter
        help: ' - 1.3.6.1.4.1.14988.1.1.1.1.1.9'
        indexes:
        - labelname: mtxrWlStatIndex
          type: gauge
      - name: mtxrWlStatRxCCQ
        oid: 1.3.6.1.4.1.14988.1.1.1.1.1.10
        type: counter
        help: ' - 1.3.6.1.4.1.14988.1.1.1.1.1.10'
        indexes:
        - labelname: mtxrWlStatIndex
          type: gauge
      - name: mtxrWlRtabAddr
        oid: 1.3.6.1.4.1.14988.1.1.1.2.1.1
        type: PhysAddress48
        help: ' - 1.3.6.1.4.1.14988.1.1.1.2.1.1'
        indexes:
        - labelname: mtxrWlRtabAddr
          type: PhysAddress48
          fixed_size: 6
        - labelname: mtxrWlRtabIface
          type: gauge
      - name: mtxrWlRtabIface
        oid: 1.3.6.1.4.1.14988.1.1.1.2.1.2
        type: gauge
        help: ' - 1.3.6.1.4.1.14988.1.1.1.2.1.2'
        indexes:
        - labelname: mtxrWlRtabAddr
          type: PhysAddress48
          fixed_size: 6
        - labelname: mtxrWlRtabIface
          type: gauge
      - name: mtxrWlRtabStrength
        oid: 1.3.6.1.4.1.14988.1.1.1.2.1.3
        type: gauge
        help: dBm - 1.3.6.1.4.1.14988.1.1.1.2.1.3
        indexes:
        - labelname: mtxrWlRtabAddr
          type: PhysAddress48
          fixed_size: 6
        - labelname: mtxrWlRtabIface
          type: gauge
      - name: mtxrWlRtabTxBytes
        oid: 1.3.6.1.4.1.14988.1.1.1.2.1.4
        type: counter
        help: ' - 1.3.6.1.4.1.14988.1.1.1.2.1.4'
        indexes:
        - labelname: mtxrWlRtabAddr
          type: PhysAddress48
          fixed_size: 6
        - labelname: mtxrWlRtabIface
          type: gauge
      - name: mtxrWlRtabRxBytes
        oid: 1.3.6.1.4.1.14988.1.1.1.2.1.5
        type: counter
        help: ' - 1.3.6.1.4.1.14988.1.1.1.2.1.5'
        indexes:
        - labelname: mtxrWlRtabAddr
          type: PhysAddress48
          fixed_size: 6
        - labelname: mtxrWlRtabIface
          type: gauge
      - name: mtxrWlRtabTxPackets
        oid: 1.3.6.1.4.1.14988.1.1.1.2.1.6
        type: counter
        help: ' - 1.3.6.1.4.1.14988.1.1.1.2.1.6'
        indexes:
        - labelname: mtxrWlRtabAddr
          type: PhysAddress48
          fixed_size: 6
        - labelname: mtxrWlRtabIface
          type: gauge
      - name: mtxrWlRtabRxPackets
        oid: 1.3.6.1.4.1.14988.1.1.1.2.1.7
        type: counter
        help: ' - 1.3.6.1.4.1.14988.1.1.1.2.1.7'
        indexes:
        - labelname: mtxrWlRtabAddr
          type: PhysAddress48
          fixed_size: 6
        - labelname: mtxrWlRtabIface
          type: gauge
      - name: mtxrWlRtabTxRate
        oid: 1.3.6.1.4.1.14988.1.1.1.2.1.8
        type: gauge
        help: bits per second - 1.3.6.1.4.1.14988.1.1.1.2.1.8
        indexes:
        - labelname: mtxrWlRtabAddr
          type: PhysAddress48
          fixed_size: 6
        - labelname: mtxrWlRtabIface
          type: gauge
      - name: mtxrWlRtabRxRate
        oid: 1.3.6.1.4.1.14988.1.1.1.2.1.9
        type: gauge
        help: bits per second - 1.3.6.1.4.1.14988.1.1.1.2.1.9
        indexes:
        - labelname: mtxrWlRtabAddr
          type: PhysAddress48
          fixed_size: 6
        - labelname: mtxrWlRtabIface
          type: gauge
      - name: mtxrWlRtabRouterOSVersion
        oid: 1.3.6.1.4.1.14988.1.1.1.2.1.10
        type: DisplayString
        help: RouterOS version - 1.3.6.1.4.1.14988.1.1.1.2.1.10
        indexes:
        - labelname: mtxrWlRtabAddr
          type: PhysAddress48
          fixed_size: 6
        - labelname: mtxrWlRtabIface
          type: gauge
      - name: mtxrWlRtabUptime
        oid: 1.3.6.1.4.1.14988.1.1.1.2.1.11
        type: gauge
        help: uptime - 1.3.6.1.4.1.14988.1.1.1.2.1.11
        indexes:
        - labelname: mtxrWlRtabAddr
          type: PhysAddress48
          fixed_size: 6
        - labelname: mtxrWlRtabIface
          type: gauge
      - name: mtxrWlRtabSignalToNoise
        oid: 1.3.6.1.4.1.14988.1.1.1.2.1.12
        type: gauge
        help: Measured in dB, if value does not exist it is indicated with 0 - 1.3.6.1.4.1.14988.1.1.1.2.1.12
        indexes:
        - labelname: mtxrWlRtabAddr
          type: PhysAddress48
          fixed_size: 6
        - labelname: mtxrWlRtabIface
          type: gauge
      - name: mtxrWlRtabTxStrengthCh0
        oid: 1.3.6.1.4.1.14988.1.1.1.2.1.13
        type: gauge
        help: ' - 1.3.6.1.4.1.14988.1.1.1.2.1.13'
        indexes:
        - labelname: mtxrWlRtabAddr
          type: PhysAddress48
          fixed_size: 6
        - labelname: mtxrWlRtabIface
          type: gauge
      - name: mtxrWlRtabRxStrengthCh0
        oid: 1.3.6.1.4.1.14988.1.1.1.2.1.14
        type: gauge
        help: ' - 1.3.6.1.4.1.14988.1.1.1.2.1.14'
        indexes:
        - labelname: mtxrWlRtabAddr
          type: PhysAddress48
          fixed_size: 6
        - labelname: mtxrWlRtabIface
          type: gauge
      - name: mtxrWlRtabTxStrengthCh1
        oid: 1.3.6.1.4.1.14988.1.1.1.2.1.15
        type: gauge
        help: ' - 1.3.6.1.4.1.14988.1.1.1.2.1.15'
        indexes:
        - labelname: mtxrWlRtabAddr
          type: PhysAddress48
          fixed_size: 6
        - labelname: mtxrWlRtabIface
          type: gauge
      - name: mtxrWlRtabRxStrengthCh1
        oid: 1.3.6.1.4.1.14988.1.1.1.2.1.16
        type: gauge
        help: ' - 1.3.6.1.4.1.14988.1.1.1.2.1.16'
        indexes:
        - labelname: mtxrWlRtabAddr
          type: PhysAddress48
          fixed_size: 6
        - labelname: mtxrWlRtabIface
          type: gauge
      - name: mtxrWlRtabTxStrengthCh2
        oid: 1.3.6.1.4.1.14988.1.1.1.2.1.17
        type: gauge
        help: ' - 1.3.6.1.4.1.14988.1.1.1.2.1.17'
        indexes:
        - labelname: mtxrWlRtabAddr
          type: PhysAddress48
          fixed_size: 6
        - labelname: mtxrWlRtabIface
          type: gauge
      - name: mtxrWlRtabRxStrengthCh2
        oid: 1.3.6.1.4.1.14988.1.1.1.2.1.18
        type: gauge
        help: ' - 1.3.6.1.4.1.14988.1.1.1.2.1.18'
        indexes:
        - labelname: mtxrWlRtabAddr
          type: PhysAddress48
          fixed_size: 6
        - labelname: mtxrWlRtabIface
          type: gauge
      - name: mtxrWlRtabTxStrength
        oid: 1.3.6.1.4.1.14988.1.1.1.2.1.19
        type: gauge
        help: ' - 1.3.6.1.4.1.14988.1.1.1.2.1.19'
        indexes:
        - labelname: mtxrWlRtabAddr
          type: PhysAddress48
          fixed_size: 6
        - labelname: mtxrWlRtabIface
          type: gauge
      - name: mtxrWlRtabRadioName
        oid: 1.3.6.1.4.1.14988.1.1.1.2.1.20
        type: DisplayString
        help: ' - 1.3.6.1.4.1.14988.1.1.1.2.1.20'
        indexes:
        - labelname: mtxrWlRtabAddr
          type: PhysAddress48
          fixed_size: 6
        - labelname: mtxrWlRtabIface
          type: gauge
      - name: mtxrWlApIndex
        oid: 1.3.6.1.4.1.14988.1.1.1.3.1.1
        type: gauge
        help: ' - 1.3.6.1.4.1.14988.1.1.1.3.1.1'
        indexes:
        - labelname: mtxrWlApIndex
          type: gauge
      - name: mtxrWlApTxRate
        oid: 1.3.6.1.4.1.14988.1.1.1.3.1.2
        type: gauge
        help: bits per second - 1.3.6.1.4.1.14988.1.1.1.3.1.2
        indexes:
        - labelname: mtxrWlApIndex
          type: gauge
      - name: mtxrWlApRxRate
        oid: 1.3.6.1.4.1.14988.1.1.1.3.1.3
        type: gauge
        help: bits per second - 1.3.6.1.4.1.14988.1.1.1.3.1.3
        indexes:
        - labelname: mtxrWlApIndex
          type: gauge
      - name: mtxrWlApSsid
        oid: 1.3.6.1.4.1.14988.1.1.1.3.1.4
        type: DisplayString
        help: ' - 1.3.6.1.4.1.14988.1.1.1.3.1.4'
        indexes:
        - labelname: mtxrWlApIndex
          type: gauge
      - name: mtxrWlApBssid
        oid: 1.3.6.1.4.1.14988.1.1.1.3.1.5
        type: PhysAddress48
        help: ' - 1.3.6.1.4.1.14988.1.1.1.3.1.5'
        indexes:
        - labelname: mtxrWlApIndex
          type: gauge
      - name: mtxrWlApClientCount
        oid: 1.3.6.1.4.1.14988.1.1.1.3.1.6
        type: counter
        help: ' - 1.3.6.1.4.1.14988.1.1.1.3.1.6'
        indexes:
        - labelname: mtxrWlApIndex
          type: gauge
      - name: mtxrWlApFreq
        oid: 1.3.6.1.4.1.14988.1.1.1.3.1.7
        type: gauge
        help: megahertz - 1.3.6.1.4.1.14988.1.1.1.3.1.7
        indexes:
        - labelname: mtxrWlApIndex
          type: gauge
      - name: mtxrWlApBand
        oid: 1.3.6.1.4.1.14988.1.1.1.3.1.8
        type: DisplayString
        help: ' - 1.3.6.1.4.1.14988.1.1.1.3.1.8'
        indexes:
        - labelname: mtxrWlApIndex
          type: gauge
      - name: mtxrWlApNoiseFloor
        oid: 1.3.6.1.4.1.14988.1.1.1.3.1.9
        type: gauge
        help: ' - 1.3.6.1.4.1.14988.1.1.1.3.1.9'
        indexes:
        - labelname: mtxrWlApIndex
          type: gauge
      - name: mtxrWlApOverallTxCCQ
        oid: 1.3.6.1.4.1.14988.1.1.1.3.1.10
        type: counter
        help: ' - 1.3.6.1.4.1.14988.1.1.1.3.1.10'
        indexes:
        - labelname: mtxrWlApIndex
          type: gauge
      - name: mtxrWlApAuthClientCount
        oid: 1.3.6.1.4.1.14988.1.1.1.3.1.11
        type: counter
        help: ' - 1.3.6.1.4.1.14988.1.1.1.3.1.11'
        indexes:
        - labelname: mtxrWlApIndex
          type: gauge
      - name: mtxrWlRtabEntryCount
        oid: 1.3.6.1.4.1.14988.1.1.1.4
        type: gauge
        help: Wireless registration table entry count - 1.3.6.1.4.1.14988.1.1.1.4
      - name: mtxrWlCMRtabAddr
        oid: 1.3.6.1.4.1.14988.1.1.1.5.1.1
        type: PhysAddress48
        help: ' - 1.3.6.1.4.1.14988.1.1.1.5.1.1'
        indexes:
        - labelname: mtxrWlCMRtabAddr
          type: PhysAddress48
          fixed_size: 6
        - labelname: mtxrWlCMRtabIface
          type: gauge
      - name: mtxrWlCMRtabIface
        oid: 1.3.6.1.4.1.14988.1.1.1.5.1.2
        type: gauge
        help: ' - 1.3.6.1.4.1.14988.1.1.1.5.1.2'
        indexes:
        - labelname: mtxrWlCMRtabAddr
          type: PhysAddress48
          fixed_size: 6
        - labelname: mtxrWlCMRtabIface
          type: gauge
      - name: mtxrWlCMRtabUptime
        oid: 1.3.6.1.4.1.14988.1.1.1.5.1.3
        type: gauge
        help: uptime - 1.3.6.1.4.1.14988.1.1.1.5.1.3
        indexes:
        - labelname: mtxrWlCMRtabAddr
          type: PhysAddress48
          fixed_size: 6
        - labelname: mtxrWlCMRtabIface
          type: gauge
      - name: mtxrWlCMRtabTxBytes
        oid: 1.3.6.1.4.1.14988.1.1.1.5.1.4
        type: counter
        help: ' - 1.3.6.1.4.1.14988.1.1.1.5.1.4'
        indexes:
        - labelname: mtxrWlCMRtabAddr
          type: PhysAddress48
          fixed_size: 6
        - labelname: mtxrWlCMRtabIface
          type: gauge
      - name: mtxrWlCMRtabRxBytes
        oid: 1.3.6.1.4.1.14988.1.1.1.5.1.5
        type: counter
        help: ' - 1.3.6.1.4.1.14988.1.1.1.5.1.5'
        indexes:
        - labelname: mtxrWlCMRtabAddr
          type: PhysAddress48
          fixed_size: 6
        - labelname: mtxrWlCMRtabIface
          type: gauge
      - name: mtxrWlCMRtabTxPackets
        oid: 1.3.6.1.4.1.14988.1.1.1.5.1.6
        type: counter
        help: ' - 1.3.6.1.4.1.14988.1.1.1.5.1.6'
        indexes:
        - labelname: mtxrWlCMRtabAddr
          type: PhysAddress48
          fixed_size: 6
        - labelname: mtxrWlCMRtabIface
          type: gauge
      - name: mtxrWlCMRtabRxPackets
        oid: 1.3.6.1.4.1.14988.1.1.1.5.1.7
        type: counter
        help: ' - 1.3.6.1.4.1.14988.1.1.1.5.1.7'
        indexes:
        - labelname: mtxrWlCMRtabAddr
          type: PhysAddress48
          fixed_size: 6
        - labelname: mtxrWlCMRtabIface
          type: gauge
      - name: mtxrWlCMRtabTxRate
        oid: 1.3.6.1.4.1.14988.1.1.1.5.1.8
        type: gauge
        help: bits per second - 1.3.6.1.4.1.14988.1.1.1.5.1.8
        indexes:
        - labelname: mtxrWlCMRtabAddr
          type: PhysAddress48
          fixed_size: 6
        - labelname: mtxrWlCMRtabIface
          type: gauge
      - name: mtxrWlCMRtabRxRate
        oid: 1.3.6.1.4.1.14988.1.1.1.5.1.9
        type: gauge
        help: bits per second - 1.3.6.1.4.1.14988.1.1.1.5.1.9
        indexes:
        - labelname: mtxrWlCMRtabAddr
          type: PhysAddress48
          fixed_size: 6
        - labelname: mtxrWlCMRtabIface
          type: gauge
      - name: mtxrWlCMRtabTxStrength
        oid: 1.3.6.1.4.1.14988.1.1.1.5.1.10
        type: gauge
        help: ' - 1.3.6.1.4.1.14988.1.1.1.5.1.10'
        indexes:
        - labelname: mtxrWlCMRtabAddr
          type: PhysAddress48
          fixed_size: 6
        - labelname: mtxrWlCMRtabIface
          type: gauge
      - name: mtxrWlCMRtabRxStrength
        oid: 1.3.6.1.4.1.14988.1.1.1.5.1.11
        type: gauge
        help: ' - 1.3.6.1.4.1.14988.1.1.1.5.1.11'
        indexes:
        - labelname: mtxrWlCMRtabAddr
          type: PhysAddress48
          fixed_size: 6
        - labelname: mtxrWlCMRtabIface
          type: gauge
      - name: mtxrWlCMRtabSsid
        oid: 1.3.6.1.4.1.14988.1.1.1.5.1.12
        type: DisplayString
        help: ' - 1.3.6.1.4.1.14988.1.1.1.5.1.12'
        indexes:
        - labelname: mtxrWlCMRtabAddr
          type: PhysAddress48
          fixed_size: 6
        - labelname: mtxrWlCMRtabIface
          type: gauge
      - name: mtxrWlCMRtabEapIdent
        oid: 1.3.6.1.4.1.14988.1.1.1.5.1.13
        type: DisplayString
        help: ' - 1.3.6.1.4.1.14988.1.1.1.5.1.13'
        indexes:
        - labelname: mtxrWlCMRtabAddr
          type: PhysAddress48
          fixed_size: 6
        - labelname: mtxrWlCMRtabIface
          type: gauge
      - name: mtxrWlCMRtabEntryCount
        oid: 1.3.6.1.4.1.14988.1.1.1.6
        type: gauge
        help: Wireless CAPSMAN registration table entry count - 1.3.6.1.4.1.14988.1.1.1.6
      - name: mtxrWlCMIndex
        oid: 1.3.6.1.4.1.14988.1.1.1.7.1.1
        type: gauge
        help: ' - 1.3.6.1.4.1.14988.1.1.1.7.1.1'
        indexes:
        - labelname: mtxrWlCMIndex
          type: gauge
      - name: mtxrWlCMRegClientCount
        oid: 1.3.6.1.4.1.14988.1.1.1.7.1.2
        type: counter
        help: ' - 1.3.6.1.4.1.14988.1.1.1.7.1.2'
        indexes:
        - labelname: mtxrWlCMIndex
          type: gauge
      - name: mtxrWlCMAuthClientCount
        oid: 1.3.6.1.4.1.14988.1.1.1.7.1.3
        type: counter
        help: ' - 1.3.6.1.4.1.14988.1.1.1.7.1.3'
        indexes:
        - labelname: mtxrWlCMIndex
          type: gauge
      - name: mtxrWlCMState
        oid: 1.3.6.1.4.1.14988.1.1.1.7.1.4
        type: DisplayString
        help: ' - 1.3.6.1.4.1.14988.1.1.1.7.1.4'
        indexes:
        - labelname: mtxrWlCMIndex
          type: gauge
      - name: mtxrWlCMChannel
        oid: 1.3.6.1.4.1.14988.1.1.1.7.1.5
        type: DisplayString
        help: for master only - 1.3.6.1.4.1.14988.1.1.1.7.1.5
        indexes:
        - labelname: mtxrWlCMIndex
          type: gauge
      - name: mtxrWl60GIndex
        oid: 1.3.6.1.4.1.14988.1.1.1.8.1.1
        type: gauge
        help: ' - 1.3.6.1.4.1.14988.1.1.1.8.1.1'
        indexes:
        - labelname: mtxrWl60GIndex
          type: gauge
      - name: mtxrWl60GMode
        oid: 1.3.6.1.4.1.14988.1.1.1.8.1.2
        type: gauge
        help: ' - 1.3.6.1.4.1.14988.1.1.1.8.1.2'
        indexes:
        - labelname: mtxrWl60GIndex
          type: gauge
        enum_values:
          0: apBridge
          1: stationBridge
          2: sniff
          3: bridge
      - name: mtxrWl60GSsid
        oid: 1.3.6.1.4.1.14988.1.1.1.8.1.3
        type: DisplayString
        help: ' - 1.3.6.1.4.1.14988.1.1.1.8.1.3'
        indexes:
        - labelname: mtxrWl60GIndex
          type: gauge
      - name: mtxrWl60GConnected
        oid: 1.3.6.1.4.1.14988.1.1.1.8.1.4
        type: gauge
        help: ' - 1.3.6.1.4.1.14988.1.1.1.8.1.4'
        indexes:
        - labelname: mtxrWl60GIndex
          type: gauge
        enum_values:
          0: "false"
          1: "true"
      - name: mtxrWl60GRemote
        oid: 1.3.6.1.4.1.14988.1.1.1.8.1.5
        type: PhysAddress48
        help: ' - 1.3.6.1.4.1.14988.1.1.1.8.1.5'
        indexes:
        - labelname: mtxrWl60GIndex
          type: gauge
      - name: mtxrWl60GFreq
        oid: 1.3.6.1.4.1.14988.1.1.1.8.1.6
        type: gauge
        help: Mhz - 1.3.6.1.4.1.14988.1.1.1.8.1.6
        indexes:
        - labelname: mtxrWl60GIndex
          type: gauge
      - name: mtxrWl60GMcs
        oid: 1.3.6.1.4.1.14988.1.1.1.8.1.7
        type: gauge
        help: ' - 1.3.6.1.4.1.14988.1.1.1.8.1.7'
        indexes:
        - labelname: mtxrWl60GIndex
          type: gauge
      - name: mtxrWl60GSignal
        oid: 1.3.6.1.4.1.14988.1.1.1.8.1.8
        type: gauge
        help: ' - 1.3.6.1.4.1.14988.1.1.1.8.1.8'
        indexes:
        - labelname: mtxrWl60GIndex
          type: gauge
      - name: mtxrWl60GTxSector
        oid: 1.3.6.1.4.1.14988.1.1.1.8.1.9
        type: gauge
        help: ' - 1.3.6.1.4.1.14988.1.1.1.8.1.9'
        indexes:
        - labelname: mtxrWl60GIndex
          type: gauge
      - name: mtxrWl60GTxSectorInfo
        oid: 1.3.6.1.4.1.14988.1.1.1.8.1.11
        type: DisplayString
        help: ' - 1.3.6.1.4.1.14988.1.1.1.8.1.11'
        indexes:
        - labelname: mtxrWl60GIndex
          type: gauge
      - name: mtxrWl60GRssi
        oid: 1.3.6.1.4.1.14988.1.1.1.8.1.12
        type: gauge
        help: ' - 1.3.6.1.4.1.14988.1.1.1.8.1.12'
        indexes:
        - labelname: mtxrWl60GIndex
          type: gauge
      - name: mtxrWl60GPhyRate
        oid: 1.3.6.1.4.1.14988.1.1.1.8.1.13
        type: gauge
        help: ' - 1.3.6.1.4.1.14988.1.1.1.8.1.13'
        indexes:
        - labelname: mtxrWl60GIndex
          type: gauge
      - name: mtxrWl60GStaIndex
        oid: 1.3.6.1.4.1.14988.1.1.1.9.1.1
        type: gauge
        help: ' - 1.3.6.1.4.1.14988.1.1.1.9.1.1'
        indexes:
        - labelname: mtxrWl60GStaIndex
          type: gauge
      - name: mtxrWl60GStaConnected
        oid: 1.3.6.1.4.1.14988.1.1.1.9.1.2
        type: gauge
        help: ' - 1.3.6.1.4.1.14988.1.1.1.9.1.2'
        indexes:
        - labelname: mtxrWl60GStaIndex
          type: gauge
        enum_values:
          0: "false"
          1: "true"
      - name: mtxrWl60GStaRemote
        oid: 1.3.6.1.4.1.14988.1.1.1.9.1.3
        type: PhysAddress48
        help: ' - 1.3.6.1.4.1.14988.1.1.1.9.1.3'
        indexes:
        - labelname: mtxrWl60GStaIndex
          type: gauge
      - name: mtxrWl60GStaMcs
        oid: 1.3.6.1.4.1.14988.1.1.1.9.1.4
        type: gauge
        help: ' - 1.3.6.1.4.1.14988.1.1.1.9.1.4'
        indexes:
        - labelname: mtxrWl60GStaIndex
          type: gauge
      - name: mtxrWl60GStaSignal
        oid: 1.3.6.1.4.1.14988.1.1.1.9.1.5
        type: gauge
        help: ' - 1.3.6.1.4.1.14988.1.1.1.9.1.5'
        indexes:
        - labelname: mtxrWl60GStaIndex
          type: gauge
      - name: mtxrWl60GStaTxSector
        oid: 1.3.6.1.4.1.14988.1.1.1.9.1.6
        type: gauge
        help: ' - 1.3.6.1.4.1.14988.1.1.1.9.1.6'
        indexes:
        - labelname: mtxrWl60GStaIndex
          type: gauge
      - name: mtxrWl60GStaPhyRate
        oid: 1.3.6.1.4.1.14988.1.1.1.9.1.8
        type: gauge
        help: Mbits per second - 1.3.6.1.4.1.14988.1.1.1.9.1.8
        indexes:
        - labelname: mtxrWl60GStaIndex
          type: gauge
      - name: mtxrWl60GStaRssi
        oid: 1.3.6.1.4.1.14988.1.1.1.9.1.9
        type: gauge
        help: ' - 1.3.6.1.4.1.14988.1.1.1.9.1.9'
        indexes:
        - labelname: mtxrWl60GStaIndex
          type: gauge
      - name: mtxrWl60GStaDistance
        oid: 1.3.6.1.4.1.14988.1.1.1.9.1.10
        type: gauge
        help: meters - 1.3.6.1.4.1.14988.1.1.1.9.1.10
        indexes:
        - labelname: mtxrWl60GStaIndex
          type: gauge
      - name: mtxrWlCMREntryCount
        oid: 1.3.6.1.4.1.14988.1.1.1.10
        type: gauge
        help: Wireless CAPSMAN remote-cap entry count - 1.3.6.1.4.1.14988.1.1.1.10
      - name: mtxrWlCMRemoteIndex
        oid: 1.3.6.1.4.1.14988.1.1.1.11.1.1
        type: gauge
        help: ' - 1.3.6.1.4.1.14988.1.1.1.11.1.1'
        indexes:
        - labelname: mtxrWlCMRemoteIndex
          type: gauge
      - name: mtxrWlCMRemoteName
        oid: 1.3.6.1.4.1.14988.1.1.1.11.1.2
        type: DisplayString
        help: ' - 1.3.6.1.4.1.14988.1.1.1.11.1.2'
        indexes:
        - labelname: mtxrWlCMRemoteIndex
          type: gauge
      - name: mtxrWlCMRemoteState
        oid: 1.3.6.1.4.1.14988.1.1.1.11.1.3
        type: DisplayString
        help: ' - 1.3.6.1.4.1.14988.1.1.1.11.1.3'
        indexes:
        - labelname: mtxrWlCMRemoteIndex
          type: gauge
      - name: mtxrWlCMRemoteAddress
        oid: 1.3.6.1.4.1.14988.1.1.1.11.1.4
        type: DisplayString
        help: ' - 1.3.6.1.4.1.14988.1.1.1.11.1.4'
        indexes:
        - labelname: mtxrWlCMRemoteIndex
          type: gauge
      - name: mtxrWlCMRemoteRadios
        oid: 1.3.6.1.4.1.14988.1.1.1.11.1.5
        type: counter
        help: ' - 1.3.6.1.4.1.14988.1.1.1.11.1.5'
        indexes:
        - labelname: mtxrWlCMRemoteIndex
          type: gauge
      - name: mtxrQueueSimpleIndex
        oid: 1.3.6.1.4.1.14988.1.1.2.1.1.1
        type: gauge
        help: ' - 1.3.6.1.4.1.14988.1.1.2.1.1.1'
        indexes:
        - labelname: mtxrQueueSimpleIndex
          type: gauge
      - name: mtxrQueueSimpleName
        oid: 1.3.6.1.4.1.14988.1.1.2.1.1.2
        type: DisplayString
        help: ' - 1.3.6.1.4.1.14988.1.1.2.1.1.2'
        indexes:
        - labelname: mtxrQueueSimpleIndex
          type: gauge
      - name: mtxrQueueSimpleSrcAddr
        oid: 1.3.6.1.4.1.14988.1.1.2.1.1.3
        type: InetAddressIPv4
        help: ' - 1.3.6.1.4.1.14988.1.1.2.1.1.3'
        indexes:
        - labelname: mtxrQueueSimpleIndex
          type: gauge
      - name: mtxrQueueSimpleSrcMask
        oid: 1.3.6.1.4.1.14988.1.1.2.1.1.4
        type: InetAddressIPv4
        help: ' - 1.3.6.1.4.1.14988.1.1.2.1.1.4'
        indexes:
        - labelname: mtxrQueueSimpleIndex
          type: gauge
      - name: mtxrQueueSimpleDstAddr
        oid: 1.3.6.1.4.1.14988.1.1.2.1.1.5
        type: InetAddressIPv4
        help: ' - 1.3.6.1.4.1.14988.1.1.2.1.1.5'
        indexes:
        - labelname: mtxrQueueSimpleIndex
          type: gauge
      - name: mtxrQueueSimpleDstMask
        oid: 1.3.6.1.4.1.14988.1.1.2.1.1.6
        type: InetAddressIPv4
        help: ' - 1.3.6.1.4.1.14988.1.1.2.1.1.6'
        indexes:
        - labelname: mtxrQueueSimpleIndex
          type: gauge
      - name: mtxrQueueSimpleIface
        oid: 1.3.6.1.4.1.14988.1.1.2.1.1.7
        type: gauge
        help: interface index - 1.3.6.1.4.1.14988.1.1.2.1.1.7
        indexes:
        - labelname: mtxrQueueSimpleIndex
          type: gauge
      - name: mtxrQueueSimpleBytesIn
        oid: 1.3.6.1.4.1.14988.1.1.2.1.1.8
        type: counter
        help: ' - 1.3.6.1.4.1.14988.1.1.2.1.1.8'
        indexes:
        - labelname: mtxrQueueSimpleIndex
          type: gauge
      - name: mtxrQueueSimpleBytesOut
        oid: 1.3.6.1.4.1.14988.1.1.2.1.1.9
        type: counter
        help: ' - 1.3.6.1.4.1.14988.1.1.2.1.1.9'
        indexes:
        - labelname: mtxrQueueSimpleIndex
          type: gauge
      - name: mtxrQueueSimplePacketsIn
        oid: 1.3.6.1.4.1.14988.1.1.2.1.1.10
        type: counter
        help: ' - 1.3.6.1.4.1.14988.1.1.2.1.1.10'
        indexes:
        - labelname: mtxrQueueSimpleIndex
          type: gauge
      - name: mtxrQueueSimplePacketsOut
        oid: 1.3.6.1.4.1.14988.1.1.2.1.1.11
        type: counter
        help: ' - 1.3.6.1.4.1.14988.1.1.2.1.1.11'
        indexes:
        - labelname: mtxrQueueSimpleIndex
          type: gauge
      - name: mtxrQueueSimplePCQQueuesIn
        oid: 1.3.6.1.4.1.14988.1.1.2.1.1.12
        type: counter
        help: ' - 1.3.6.1.4.1.14988.1.1.2.1.1.12'
        indexes:
        - labelname: mtxrQueueSimpleIndex
          type: gauge
      - name: mtxrQueueSimplePCQQueuesOut
        oid: 1.3.6.1.4.1.14988.1.1.2.1.1.13
        type: counter
        help: ' - 1.3.6.1.4.1.14988.1.1.2.1.1.13'
        indexes:
        - labelname: mtxrQueueSimpleIndex
          type: gauge
      - name: mtxrQueueSimpleDroppedIn
        oid: 1.3.6.1.4.1.14988.1.1.2.1.1.14
        type: counter
        help: ' - 1.3.6.1.4.1.14988.1.1.2.1.1.14'
        indexes:
        - labelname: mtxrQueueSimpleIndex
          type: gauge
      - name: mtxrQueueSimpleDroppedOut
        oid: 1.3.6.1.4.1.14988.1.1.2.1.1.15
        type: counter
        help: ' - 1.3.6.1.4.1.14988.1.1.2.1.1.15'
        indexes:
        - labelname: mtxrQueueSimpleIndex
          type: gauge
      - name: mtxrQueueTreeIndex
        oid: 1.3.6.1.4.1.14988.1.1.2.2.1.1
        type: gauge
        help: ' - 1.3.6.1.4.1.14988.1.1.2.2.1.1'
        indexes:
        - labelname: mtxrQueueTreeIndex
          type: gauge
      - name: mtxrQueueTreeName
        oid: 1.3.6.1.4.1.14988.1.1.2.2.1.2
        type: DisplayString
        help: ' - 1.3.6.1.4.1.14988.1.1.2.2.1.2'
        indexes:
        - labelname: mtxrQueueTreeIndex
          type: gauge
      - name: mtxrQueueTreeFlow
        oid: 1.3.6.1.4.1.14988.1.1.2.2.1.3
        type: DisplayString
        help: flowmark - 1.3.6.1.4.1.14988.1.1.2.2.1.3
        indexes:
        - labelname: mtxrQueueTreeIndex
          type: gauge
      - name: mtxrQueueTreeParentIndex
        oid: 1.3.6.1.4.1.14988.1.1.2.2.1.4
        type: gauge
        help: index of parent tree queue or parent interface - 1.3.6.1.4.1.14988.1.1.2.2.1.4
        indexes:
        - labelname: mtxrQueueTreeIndex
          type: gauge
      - name: mtxrQueueTreeBytes
        oid: 1.3.6.1.4.1.14988.1.1.2.2.1.5
        type: counter
        help: ' - 1.3.6.1.4.1.14988.1.1.2.2.1.5'
        indexes:
        - labelname: mtxrQueueTreeIndex
          type: gauge
      - name: mtxrQueueTreePackets
        oid: 1.3.6.1.4.1.14988.1.1.2.2.1.6
        type: counter
        help: ' - 1.3.6.1.4.1.14988.1.1.2.2.1.6'
        indexes:
        - labelname: mtxrQueueTreeIndex
          type: gauge
      - name: mtxrQueueTreeHCBytes
        oid: 1.3.6.1.4.1.14988.1.1.2.2.1.7
        type: counter
        help: ' - 1.3.6.1.4.1.14988.1.1.2.2.1.7'
        indexes:
        - labelname: mtxrQueueTreeIndex
          type: gauge
      - name: mtxrQueueTreePCQQueues
        oid: 1.3.6.1.4.1.14988.1.1.2.2.1.8
        type: counter
        help: ' - 1.3.6.1.4.1.14988.1.1.2.2.1.8'
        indexes:
        - labelname: mtxrQueueTreeIndex
          type: gauge
      - name: mtxrQueueTreeDropped
        oid: 1.3.6.1.4.1.14988.1.1.2.2.1.9
        type: counter
        help: ' - 1.3.6.1.4.1.14988.1.1.2.2.1.9'
        indexes:
        - labelname: mtxrQueueTreeIndex
          type: gauge
      - name: mtxrHlCoreVoltage
        oid: 1.3.6.1.4.1.14988.1.1.3.1
        type: gauge
        help: core voltage - 1.3.6.1.4.1.14988.1.1.3.1
      - name: mtxrHlThreeDotThreeVoltage
        oid: 1.3.6.1.4.1.14988.1.1.3.2
        type: gauge
        help: 3.3V voltage - 1.3.6.1.4.1.14988.1.1.3.2
      - name: mtxrHlFiveVoltage
        oid: 1.3.6.1.4.1.14988.1.1.3.3
        type: gauge
        help: 5V voltage - 1.3.6.1.4.1.14988.1.1.3.3
      - name: mtxrHlTwelveVoltage
        oid: 1.3.6.1.4.1.14988.1.1.3.4
        type: gauge
        help: 12V voltage - 1.3.6.1.4.1.14988.1.1.3.4
      - name: mtxrHlSensorTemperature
        oid: 1.3.6.1.4.1.14988.1.1.3.5
        type: gauge
        help: temperature at sensor chip - 1.3.6.1.4.1.14988.1.1.3.5
      - name: mtxrHlCpuTemperature
        oid: 1.3.6.1.4.1.14988.1.1.3.6
        type: gauge
        help: temperature near cpu - 1.3.6.1.4.1.14988.1.1.3.6
      - name: mtxrHlBoardTemperature
        oid: 1.3.6.1.4.1.14988.1.1.3.7
        type: gauge
        help: ' - 1.3.6.1.4.1.14988.1.1.3.7'
      - name: mtxrHlVoltage
        oid: 1.3.6.1.4.1.14988.1.1.3.8
        type: gauge
        help: ' - 1.3.6.1.4.1.14988.1.1.3.8'
      - name: mtxrHlActiveFan
        oid: 1.3.6.1.4.1.14988.1.1.3.9
        type: DisplayString
        help: ' - 1.3.6.1.4.1.14988.1.1.3.9'
      - name: mtxrHlTemperature
        oid: 1.3.6.1.4.1.14988.1.1.3.10
        type: gauge
        help: ' - 1.3.6.1.4.1.14988.1.1.3.10'
      - name: mtxrHlProcessorTemperature
        oid: 1.3.6.1.4.1.14988.1.1.3.11
        type: gauge
        help: ' - 1.3.6.1.4.1.14988.1.1.3.11'
      - name: mtxrHlPower
        oid: 1.3.6.1.4.1.14988.1.1.3.12
        type: gauge
        help: Watts - 1.3.6.1.4.1.14988.1.1.3.12
      - name: mtxrHlCurrent
        oid: 1.3.6.1.4.1.14988.1.1.3.13
        type: gauge
        help: mA - 1.3.6.1.4.1.14988.1.1.3.13
      - name: mtxrHlProcessorFrequency
        oid: 1.3.6.1.4.1.14988.1.1.3.14
        type: gauge
        help: Mhz - 1.3.6.1.4.1.14988.1.1.3.14
      - name: mtxrHlPowerSupplyState
        oid: 1.3.6.1.4.1.14988.1.1.3.15
        type: gauge
        help: PSU state ok - 1.3.6.1.4.1.14988.1.1.3.15
        enum_values:
          0: "false"
          1: "true"
      - name: mtxrHlBackupPowerSupplyState
        oid: 1.3.6.1.4.1.14988.1.1.3.16
        type: gauge
        help: backup PSU state ok - 1.3.6.1.4.1.14988.1.1.3.16
        enum_values:
          0: "false"
          1: "true"
      - name: mtxrHlFanSpeed1
        oid: 1.3.6.1.4.1.14988.1.1.3.17
        type: gauge
        help: rpm - 1.3.6.1.4.1.14988.1.1.3.17
      - name: mtxrHlFanSpeed2
        oid: 1.3.6.1.4.1.14988.1.1.3.18
        type: gauge
        help: rpm - 1.3.6.1.4.1.14988.1.1.3.18
      - name: mtxrGaugeIndex
        oid: 1.3.6.1.4.1.14988.1.1.3.100.1.1
        type: gauge
        help: ' - 1.3.6.1.4.1.14988.1.1.3.100.1.1'
        indexes:
        - labelname: mtxrGaugeIndex
          type: gauge
      - name: mtxrGaugeName
        oid: 1.3.6.1.4.1.14988.1.1.3.100.1.2
        type: DisplayString
        help: ' - 1.3.6.1.4.1.14988.1.1.3.100.1.2'
        indexes:
        - labelname: mtxrGaugeIndex
          type: gauge
      - name: mtxrGaugeValue
        oid: 1.3.6.1.4.1.14988.1.1.3.100.1.3
        type: gauge
        help: ' - 1.3.6.1.4.1.14988.1.1.3.100.1.3'
        indexes:
        - labelname: mtxrGaugeIndex
          type: gauge
      - name: mtxrGaugeUnit
        oid: 1.3.6.1.4.1.14988.1.1.3.100.1.4
        type: gauge
        help: units - 1.3.6.1.4.1.14988.1.1.3.100.1.4
        indexes:
        - labelname: mtxrGaugeIndex
          type: gauge
        enum_values:
          1: celsius
          2: rpm
          3: dV
          4: dA
          5: dW
          6: status
      - name: mtxrLicSoftwareId
        oid: 1.3.6.1.4.1.14988.1.1.4.1
        type: DisplayString
        help: software id - 1.3.6.1.4.1.14988.1.1.4.1
      - name: mtxrLicUpgrUntil
        oid: 1.3.6.1.4.1.14988.1.1.4.2
        type: DateAndTime
        help: current key allows upgrading until this date - 1.3.6.1.4.1.14988.1.1.4.2
      - name: mtxrLicLevel
        oid: 1.3.6.1.4.1.14988.1.1.4.3
        type: gauge
        help: current key level - 1.3.6.1.4.1.14988.1.1.4.3
      - name: mtxrLicVersion
        oid: 1.3.6.1.4.1.14988.1.1.4.4
        type: DisplayString
        help: software version - 1.3.6.1.4.1.14988.1.1.4.4
      - name: mtxrLicUpgradableTo
        oid: 1.3.6.1.4.1.14988.1.1.4.5
        type: gauge
        help: upgradable to - 1.3.6.1.4.1.14988.1.1.4.5
      - name: mtxrHotspotActiveUserIndex
        oid: 1.3.6.1.4.1.14988.1.1.5.1.1.1
        type: gauge
        help: ' - 1.3.6.1.4.1.14988.1.1.5.1.1.1'
        indexes:
        - labelname: mtxrHotspotActiveUserIndex
          type: gauge
      - name: mtxrHotspotActiveUserServerID
        oid: 1.3.6.1.4.1.14988.1.1.5.1.1.2
        type: gauge
        help: ' - 1.3.6.1.4.1.14988.1.1.5.1.1.2'
        indexes:
        - labelname: mtxrHotspotActiveUserIndex
          type: gauge
      - name: mtxrHotspotActiveUserName
        oid: 1.3.6.1.4.1.14988.1.1.5.1.1.3
        type: DisplayString
        help: ' - 1.3.6.1.4.1.14988.1.1.5.1.1.3'
        indexes:
        - labelname: mtxrHotspotActiveUserIndex
          type: gauge
      - name: mtxrHotspotActiveUserDomain
        oid: 1.3.6.1.4.1.14988.1.1.5.1.1.4
        type: DisplayString
        help: ' - 1.3.6.1.4.1.14988.1.1.5.1.1.4'
        indexes:
        - labelname: mtxrHotspotActiveUserIndex
          type: gauge
      - name: mtxrHotspotActiveUserIP
        oid: 1.3.6.1.4.1.14988.1.1.5.1.1.5
        type: InetAddressIPv4
        help: ' - 1.3.6.1.4.1.14988.1.1.5.1.1.5'
        indexes:
        - labelname: mtxrHotspotActiveUserIndex
          type: gauge
      - name: mtxrHotspotActiveUserMAC
        oid: 1.3.6.1.4.1.14988.1.1.5.1.1.6
        type: PhysAddress48
        help: ' - 1.3.6.1.4.1.14988.1.1.5.1.1.6'
        indexes:
        - labelname: mtxrHotspotActiveUserIndex
          type: gauge
      - name: mtxrHotspotActiveUserConnectTime
        oid: 1.3.6.1.4.1.14988.1.1.5.1.1.7
        type: gauge
        help: ' - 1.3.6.1.4.1.14988.1.1.5.1.1.7'
        indexes:
        - labelname: mtxrHotspotActiveUserIndex
          type: gauge
      - name: mtxrHotspotActiveUserValidTillTime
        oid: 1.3.6.1.4.1.14988.1.1.5.1.1.8
        type: gauge
        help: ' - 1.3.6.1.4.1.14988.1.1.5.1.1.8'
        indexes:
        - labelname: mtxrHotspotActiveUserIndex
          type: gauge
      - name: mtxrHotspotActiveUserIdleStartTime
        oid: 1.3.6.1.4.1.14988.1.1.5.1.1.9
        type: gauge
        help: ' - 1.3.6.1.4.1.14988.1.1.5.1.1.9'
        indexes:
        - labelname: mtxrHotspotActiveUserIndex
          type: gauge
      - name: mtxrHotspotActiveUserIdleTimeout
        oid: 1.3.6.1.4.1.14988.1.1.5.1.1.10
        type: gauge
        help: ' - 1.3.6.1.4.1.14988.1.1.5.1.1.10'
        indexes:
        - labelname: mtxrHotspotActiveUserIndex
          type: gauge
      - name: mtxrHotspotActiveUserPingTimeout
        oid: 1.3.6.1.4.1.14988.1.1.5.1.1.11
        type: gauge
        help: ' - 1.3.6.1.4.1.14988.1.1.5.1.1.11'
        indexes:
        - labelname: mtxrHotspotActiveUserIndex
          type: gauge
      - name: mtxrHotspotActiveUserBytesIn
        oid: 1.3.6.1.4.1.14988.1.1.5.1.1.12
        type: counter
        help: ' - 1.3.6.1.4.1.14988.1.1.5.1.1.12'
        indexes:
        - labelname: mtxrHotspotActiveUserIndex
          type: gauge
      - name: mtxrHotspotActiveUserBytesOut
        oid: 1.3.6.1.4.1.14988.1.1.5.1.1.13
        type: counter
        help: ' - 1.3.6.1.4.1.14988.1.1.5.1.1.13'
        indexes:
        - labelname: mtxrHotspotActiveUserIndex
          type: gauge
      - name: mtxrHotspotActiveUserPacketsIn
        oid: 1.3.6.1.4.1.14988.1.1.5.1.1.14
        type: counter
        help: ' - 1.3.6.1.4.1.14988.1.1.5.1.1.14'
        indexes:
        - labelname: mtxrHotspotActiveUserIndex
          type: gauge
      - name: mtxrHotspotActiveUserPacketsOut
        oid: 1.3.6.1.4.1.14988.1.1.5.1.1.15
        type: counter
        help: ' - 1.3.6.1.4.1.14988.1.1.5.1.1.15'
        indexes:
        - labelname: mtxrHotspotActiveUserIndex
          type: gauge
      - name: mtxrHotspotActiveUserLimitBytesIn
        oid: 1.3.6.1.4.1.14988.1.1.5.1.1.16
        type: counter
        help: ' - 1.3.6.1.4.1.14988.1.1.5.1.1.16'
        indexes:
        - labelname: mtxrHotspotActiveUserIndex
          type: gauge
      - name: mtxrHotspotActiveUserLimitBytesOut
        oid: 1.3.6.1.4.1.14988.1.1.5.1.1.17
        type: counter
        help: ' - 1.3.6.1.4.1.14988.1.1.5.1.1.17'
        indexes:
        - labelname: mtxrHotspotActiveUserIndex
          type: gauge
      - name: mtxrHotspotActiveUserAdvertStatus
        oid: 1.3.6.1.4.1.14988.1.1.5.1.1.18
        type: gauge
        help: ' - 1.3.6.1.4.1.14988.1.1.5.1.1.18'
        indexes:
        - labelname: mtxrHotspotActiveUserIndex
          type: gauge
      - name: mtxrHotspotActiveUserRadius
        oid: 1.3.6.1.4.1.14988.1.1.5.1.1.19
        type: gauge
        help: ' - 1.3.6.1.4.1.14988.1.1.5.1.1.19'
        indexes:
        - labelname: mtxrHotspotActiveUserIndex
          type: gauge
      - name: mtxrHotspotActiveUserBlockedByAdvert
        oid: 1.3.6.1.4.1.14988.1.1.5.1.1.20
        type: gauge
        help: ' - 1.3.6.1.4.1.14988.1.1.5.1.1.20'
        indexes:
        - labelname: mtxrHotspotActiveUserIndex
          type: gauge
      - name: mtxrDHCPLeaseCount
        oid: 1.3.6.1.4.1.14988.1.1.6.1
        type: gauge
        help: ' - 1.3.6.1.4.1.14988.1.1.6.1'
      - name: mtxrSystemReboot
        oid: 1.3.6.1.4.1.14988.1.1.7.1
        type: gauge
        help: set non zero to reboot - 1.3.6.1.4.1.14988.1.1.7.1
      - name: mtxrUSBPowerReset
        oid: 1.3.6.1.4.1.14988.1.1.7.2
        type: gauge
        help: switches off usb power for specified amout of seconds - 1.3.6.1.4.1.14988.1.1.7.2
      - name: mtxrSerialNumber
        oid: 1.3.6.1.4.1.14988.1.1.7.3
        type: DisplayString
        help: RouterBOARD serial number - 1.3.6.1.4.1.14988.1.1.7.3
      - name: mtxrFirmwareVersion
        oid: 1.3.6.1.4.1.14988.1.1.7.4
        type: DisplayString
        help: Current firmware version - 1.3.6.1.4.1.14988.1.1.7.4
      - name: mtxrNote
        oid: 1.3.6.1.4.1.14988.1.1.7.5
        type: DisplayString
        help: note - 1.3.6.1.4.1.14988.1.1.7.5
      - name: mtxrBuildTime
        oid: 1.3.6.1.4.1.14988.1.1.7.6
        type: DisplayString
        help: build time - 1.3.6.1.4.1.14988.1.1.7.6
      - name: mtxrFirmwareUpgradeVersion
        oid: 1.3.6.1.4.1.14988.1.1.7.7
        type: DisplayString
        help: Upgrade firmware version - 1.3.6.1.4.1.14988.1.1.7.7
      - name: mtxrBoardName
        oid: 1.3.6.1.4.1.14988.1.1.7.8
        type: DisplayString
        help: board name - 1.3.6.1.4.1.14988.1.1.7.8
      - name: mtxrScriptIndex
        oid: 1.3.6.1.4.1.14988.1.1.8.1.1.1
        type: gauge
        help: ' - 1.3.6.1.4.1.14988.1.1.8.1.1.1'
        indexes:
        - labelname: mtxrScriptIndex
          type: gauge
      - name: mtxrScriptName
        oid: 1.3.6.1.4.1.14988.1.1.8.1.1.2
        type: DisplayString
        help: ' - 1.3.6.1.4.1.14988.1.1.8.1.1.2'
        indexes:
        - labelname: mtxrScriptIndex
          type: gauge
      - name: mtxrScriptRunCmd
        oid: 1.3.6.1.4.1.14988.1.1.8.1.1.3
        type: gauge
        help: set non zero to run - 1.3.6.1.4.1.14988.1.1.8.1.1.3
        indexes:
        - labelname: mtxrScriptIndex
          type: gauge
      - name: mtxrDnStatIndex
        oid: 1.3.6.1.4.1.14988.1.1.10.1.1.1
        type: gauge
        help: ' - 1.3.6.1.4.1.14988.1.1.10.1.1.1'
        indexes:
        - labelname: mtxrDnStatIndex
          type: gauge
      - name: mtxrDnStatTxRate
        oid: 1.3.6.1.4.1.14988.1.1.10.1.1.2
        type: gauge
        help: bits per second - 1.3.6.1.4.1.14988.1.1.10.1.1.2
        indexes:
        - labelname: mtxrDnStatIndex
          type: gauge
      - name: mtxrDnStatRxRate
        oid: 1.3.6.1.4.1.14988.1.1.10.1.1.3
        type: gauge
        help: bits per second - 1.3.6.1.4.1.14988.1.1.10.1.1.3
        indexes:
        - labelname: mtxrDnStatIndex
          type: gauge
      - name: mtxrDnStatTxStrength
        oid: 1.3.6.1.4.1.14988.1.1.10.1.1.4
        type: gauge
        help: dBm - 1.3.6.1.4.1.14988.1.1.10.1.1.4
        indexes:
        - labelname: mtxrDnStatIndex
          type: gauge
      - name: mtxrDnStatRxStrength
        oid: 1.3.6.1.4.1.14988.1.1.10.1.1.5
        type: gauge
        help: dBm - 1.3.6.1.4.1.14988.1.1.10.1.1.5
        indexes:
        - labelname: mtxrDnStatIndex
          type: gauge
      - name: mtxrDnConnected
        oid: 1.3.6.1.4.1.14988.1.1.10.1.1.6
        type: gauge
        help: 0 - not connected, connected otherwise - 1.3.6.1.4.1.14988.1.1.10.1.1.6
        indexes:
        - labelname: mtxrDnStatIndex
          type: gauge
      - name: mtxrNeighborIndex
        oid: 1.3.6.1.4.1.14988.1.1.11.1.1.1
        type: gauge
        help: ' - 1.3.6.1.4.1.14988.1.1.11.1.1.1'
        indexes:
        - labelname: mtxrNeighborIndex
          type: gauge
      - name: mtxrNeighborIpAddress
        oid: 1.3.6.1.4.1.14988.1.1.11.1.1.2
        type: InetAddressIPv4
        help: ' - 1.3.6.1.4.1.14988.1.1.11.1.1.2'
        indexes:
        - labelname: mtxrNeighborIndex
          type: gauge
      - name: mtxrNeighborMacAddress
        oid: 1.3.6.1.4.1.14988.1.1.11.1.1.3
        type: PhysAddress48
        help: ' - 1.3.6.1.4.1.14988.1.1.11.1.1.3'
        indexes:
        - labelname: mtxrNeighborIndex
          type: gauge
      - name: mtxrNeighborVersion
        oid: 1.3.6.1.4.1.14988.1.1.11.1.1.4
        type: DisplayString
        help: ' - 1.3.6.1.4.1.14988.1.1.11.1.1.4'
        indexes:
        - labelname: mtxrNeighborIndex
          type: gauge
      - name: mtxrNeighborPlatform
        oid: 1.3.6.1.4.1.14988.1.1.11.1.1.5
        type: DisplayString
        help: ' - 1.3.6.1.4.1.14988.1.1.11.1.1.5'
        indexes:
        - labelname: mtxrNeighborIndex
          type: gauge
      - name: mtxrNeighborIdentity
        oid: 1.3.6.1.4.1.14988.1.1.11.1.1.6
        type: DisplayString
        help: ' - 1.3.6.1.4.1.14988.1.1.11.1.1.6'
        indexes:
        - labelname: mtxrNeighborIndex
          type: gauge
      - name: mtxrNeighborSoftwareID
        oid: 1.3.6.1.4.1.14988.1.1.11.1.1.7
        type: DisplayString
        help: ' - 1.3.6.1.4.1.14988.1.1.11.1.1.7'
        indexes:
        - labelname: mtxrNeighborIndex
          type: gauge
      - name: mtxrNeighborInterfaceID
        oid: 1.3.6.1.4.1.14988.1.1.11.1.1.8
        type: gauge
        help: ' - 1.3.6.1.4.1.14988.1.1.11.1.1.8'
        indexes:
        - labelname: mtxrNeighborIndex
          type: gauge
      - name: mtxrDate
        oid: 1.3.6.1.4.1.14988.1.1.12.1
        type: gauge
        help: UNIX time - 1.3.6.1.4.1.14988.1.1.12.1
      - name: mtxrLongtitude
        oid: 1.3.6.1.4.1.14988.1.1.12.2
        type: DisplayString
        help: longtitude - 1.3.6.1.4.1.14988.1.1.12.2
      - name: mtxrLatitude
        oid: 1.3.6.1.4.1.14988.1.1.12.3
        type: DisplayString
        help: latitude - 1.3.6.1.4.1.14988.1.1.12.3
      - name: mtxrAltitude
        oid: 1.3.6.1.4.1.14988.1.1.12.4
        type: DisplayString
        help: altitude - 1.3.6.1.4.1.14988.1.1.12.4
      - name: mtxrSpeed
        oid: 1.3.6.1.4.1.14988.1.1.12.5
        type: DisplayString
        help: speed - 1.3.6.1.4.1.14988.1.1.12.5
      - name: mtxrSattelites
        oid: 1.3.6.1.4.1.14988.1.1.12.6
        type: gauge
        help: visible sattelite count - 1.3.6.1.4.1.14988.1.1.12.6
      - name: mtxrValid
        oid: 1.3.6.1.4.1.14988.1.1.12.7
        type: gauge
        help: is the data valid - 1.3.6.1.4.1.14988.1.1.12.7
      - name: mtxrWirelessModemSignalStrength
        oid: 1.3.6.1.4.1.14988.1.1.13.1
        type: gauge
        help: signal strength in dBm (if first ppp-client modem supports) - 1.3.6.1.4.1.14988.1.1.13.1
      - name: mtxrWirelessModemSignalECIO
        oid: 1.3.6.1.4.1.14988.1.1.13.2
        type: gauge
        help: signal EC/IO in dB (if first ppp-client modem supports) - 1.3.6.1.4.1.14988.1.1.13.2
      - name: mtxrInterfaceStatsIndex
        oid: 1.3.6.1.4.1.14988.1.1.14.1.1.1
        type: gauge
        help: ' - 1.3.6.1.4.1.14988.1.1.14.1.1.1'
        indexes:
        - labelname: mtxrInterfaceStatsIndex
          type: gauge
        lookups:
        - labels:
          - mtxrInterfaceStatsIndex
          labelname: ifName
          oid: 1.3.6.1.2.1.31.1.1.1.1
          type: DisplayString
      - name: mtxrInterfaceStatsName
        oid: 1.3.6.1.4.1.14988.1.1.14.1.1.2
        type: DisplayString
        help: ' - 1.3.6.1.4.1.14988.1.1.14.1.1.2'
        indexes:
        - labelname: mtxrInterfaceStatsIndex
          type: gauge
        lookups:
        - labels:
          - mtxrInterfaceStatsIndex
          labelname: ifName
          oid: 1.3.6.1.2.1.31.1.1.1.1
          type: DisplayString
      - name: mtxrInterfaceStatsDriverRxBytes
        oid: 1.3.6.1.4.1.14988.1.1.14.1.1.11
        type: counter
        help: ' - 1.3.6.1.4.1.14988.1.1.14.1.1.11'
        indexes:
        - labelname: mtxrInterfaceStatsIndex
          type: gauge
        lookups:
        - labels:
          - mtxrInterfaceStatsIndex
          labelname: ifName
          oid: 1.3.6.1.2.1.31.1.1.1.1
          type: DisplayString
      - name: mtxrInterfaceStatsDriverRxPackets
        oid: 1.3.6.1.4.1.14988.1.1.14.1.1.12
        type: counter
        help: ' - 1.3.6.1.4.1.14988.1.1.14.1.1.12'
        indexes:
        - labelname: mtxrInterfaceStatsIndex
          type: gauge
        lookups:
        - labels:
          - mtxrInterfaceStatsIndex
          labelname: ifName
          oid: 1.3.6.1.2.1.31.1.1.1.1
          type: DisplayString
      - name: mtxrInterfaceStatsDriverTxBytes
        oid: 1.3.6.1.4.1.14988.1.1.14.1.1.13
        type: counter
        help: ' - 1.3.6.1.4.1.14988.1.1.14.1.1.13'
        indexes:
        - labelname: mtxrInterfaceStatsIndex
          type: gauge
        lookups:
        - labels:
          - mtxrInterfaceStatsIndex
          labelname: ifName
          oid: 1.3.6.1.2.1.31.1.1.1.1
          type: DisplayString
      - name: mtxrInterfaceStatsDriverTxPackets
        oid: 1.3.6.1.4.1.14988.1.1.14.1.1.14
        type: counter
        help: ' - 1.3.6.1.4.1.14988.1.1.14.1.1.14'
        indexes:
        - labelname: mtxrInterfaceStatsIndex
          type: gauge
        lookups:
        - labels:
          - mtxrInterfaceStatsIndex
          labelname: ifName
          oid: 1.3.6.1.2.1.31.1.1.1.1
          type: DisplayString
      - name: mtxrInterfaceStatsTxRx64
        oid: 1.3.6.1.4.1.14988.1.1.14.1.1.15
        type: counter
        help: ' - 1.3.6.1.4.1.14988.1.1.14.1.1.15'
        indexes:
        - labelname: mtxrInterfaceStatsIndex
          type: gauge
        lookups:
        - labels:
          - mtxrInterfaceStatsIndex
          labelname: ifName
          oid: 1.3.6.1.2.1.31.1.1.1.1
          type: DisplayString
      - name: mtxrInterfaceStatsTxRx65To127
        oid: 1.3.6.1.4.1.14988.1.1.14.1.1.16
        type: counter
        help: ' - 1.3.6.1.4.1.14988.1.1.14.1.1.16'
        indexes:
        - labelname: mtxrInterfaceStatsIndex
          type: gauge
        lookups:
        - labels:
          - mtxrInterfaceStatsIndex
          labelname: ifName
          oid: 1.3.6.1.2.1.31.1.1.1.1
          type: DisplayString
      - name: mtxrInterfaceStatsTxRx128To255
        oid: 1.3.6.1.4.1.14988.1.1.14.1.1.17
        type: counter
        help: ' - 1.3.6.1.4.1.14988.1.1.14.1.1.17'
        indexes:
        - labelname: mtxrInterfaceStatsIndex
          type: gauge
        lookups:
        - labels:
          - mtxrInterfaceStatsIndex
          labelname: ifName
          oid: 1.3.6.1.2.1.31.1.1.1.1
          type: DisplayString
      - name: mtxrInterfaceStatsTxRx256To511
        oid: 1.3.6.1.4.1.14988.1.1.14.1.1.18
        type: counter
        help: ' - 1.3.6.1.4.1.14988.1.1.14.1.1.18'
        indexes:
        - labelname: mtxrInterfaceStatsIndex
          type: gauge
        lookups:
        - labels:
          - mtxrInterfaceStatsIndex
          labelname: ifName
          oid: 1.3.6.1.2.1.31.1.1.1.1
          type: DisplayString
      - name: mtxrInterfaceStatsTxRx512To1023
        oid: 1.3.6.1.4.1.14988.1.1.14.1.1.19
        type: counter
        help: ' - 1.3.6.1.4.1.14988.1.1.14.1.1.19'
        indexes:
        - labelname: mtxrInterfaceStatsIndex
          type: gauge
        lookups:
        - labels:
          - mtxrInterfaceStatsIndex
          labelname: ifName
          oid: 1.3.6.1.2.1.31.1.1.1.1
          type: DisplayString
      - name: mtxrInterfaceStatsTxRx1024To1518
        oid: 1.3.6.1.4.1.14988.1.1.14.1.1.20
        type: counter
        help: ' - 1.3.6.1.4.1.14988.1.1.14.1.1.20'
        indexes:
        - labelname: mtxrInterfaceStatsIndex
          type: gauge
        lookups:
        - labels:
          - mtxrInterfaceStatsIndex
          labelname: ifName
          oid: 1.3.6.1.2.1.31.1.1.1.1
          type: DisplayString
      - name: mtxrInterfaceStatsTxRx1519ToMax
        oid: 1.3.6.1.4.1.14988.1.1.14.1.1.21
        type: counter
        help: ' - 1.3.6.1.4.1.14988.1.1.14.1.1.21'
        indexes:
        - labelname: mtxrInterfaceStatsIndex
          type: gauge
        lookups:
        - labels:
          - mtxrInterfaceStatsIndex
          labelname: ifName
          oid: 1.3.6.1.2.1.31.1.1.1.1
          type: DisplayString
      - name: mtxrInterfaceStatsRxBytes
        oid: 1.3.6.1.4.1.14988.1.1.14.1.1.31
        type: counter
        help: ' - 1.3.6.1.4.1.14988.1.1.14.1.1.31'
        indexes:
        - labelname: mtxrInterfaceStatsIndex
          type: gauge
        lookups:
        - labels:
          - mtxrInterfaceStatsIndex
          labelname: ifName
          oid: 1.3.6.1.2.1.31.1.1.1.1
          type: DisplayString
      - name: mtxrInterfaceStatsRxPackets
        oid: 1.3.6.1.4.1.14988.1.1.14.1.1.32
        type: counter
        help: ' - 1.3.6.1.4.1.14988.1.1.14.1.1.32'
        indexes:
        - labelname: mtxrInterfaceStatsIndex
          type: gauge
        lookups:
        - labels:
          - mtxrInterfaceStatsIndex
          labelname: ifName
          oid: 1.3.6.1.2.1.31.1.1.1.1
          type: DisplayString
      - name: mtxrInterfaceStatsRxTooShort
        oid: 1.3.6.1.4.1.14988.1.1.14.1.1.33
        type: counter
        help: ' - 1.3.6.1.4.1.14988.1.1.14.1.1.33'
        indexes:
        - labelname: mtxrInterfaceStatsIndex
          type: gauge
        lookups:
        - labels:
          - mtxrInterfaceStatsIndex
          labelname: ifName
          oid: 1.3.6.1.2.1.31.1.1.1.1
          type: DisplayString
      - name: mtxrInterfaceStatsRx64
        oid: 1.3.6.1.4.1.14988.1.1.14.1.1.34
        type: counter
        help: ' - 1.3.6.1.4.1.14988.1.1.14.1.1.34'
        indexes:
        - labelname: mtxrInterfaceStatsIndex
          type: gauge
        lookups:
        - labels:
          - mtxrInterfaceStatsIndex
          labelname: ifName
          oid: 1.3.6.1.2.1.31.1.1.1.1
          type: DisplayString
      - name: mtxrInterfaceStatsRx65To127
        oid: 1.3.6.1.4.1.14988.1.1.14.1.1.35
        type: counter
        help: ' - 1.3.6.1.4.1.14988.1.1.14.1.1.35'
        indexes:
        - labelname: mtxrInterfaceStatsIndex
          type: gauge
        lookups:
        - labels:
          - mtxrInterfaceStatsIndex
          labelname: ifName
          oid: 1.3.6.1.2.1.31.1.1.1.1
          type: DisplayString
      - name: mtxrInterfaceStatsRx128To255
        oid: 1.3.6.1.4.1.14988.1.1.14.1.1.36
        type: counter
        help: ' - 1.3.6.1.4.1.14988.1.1.14.1.1.36'
        indexes:
        - labelname: mtxrInterfaceStatsIndex
          type: gauge
        lookups:
        - labels:
          - mtxrInterfaceStatsIndex
          labelname: ifName
          oid: 1.3.6.1.2.1.31.1.1.1.1
          type: DisplayString
      - name: mtxrInterfaceStatsRx256To511
        oid: 1.3.6.1.4.1.14988.1.1.14.1.1.37
        type: counter
        help: ' - 1.3.6.1.4.1.14988.1.1.14.1.1.37'
        indexes:
        - labelname: mtxrInterfaceStatsIndex
          type: gauge
        lookups:
        - labels:
          - mtxrInterfaceStatsIndex
          labelname: ifName
          oid: 1.3.6.1.2.1.31.1.1.1.1
          type: DisplayString
      - name: mtxrInterfaceStatsRx512To1023
        oid: 1.3.6.1.4.1.14988.1.1.14.1.1.38
        type: counter
        help: ' - 1.3.6.1.4.1.14988.1.1.14.1.1.38'
        indexes:
        - labelname: mtxrInterfaceStatsIndex
          type: gauge
        lookups:
        - labels:
          - mtxrInterfaceStatsIndex
          labelname: ifName
          oid: 1.3.6.1.2.1.31.1.1.1.1
          type: DisplayString
      - name: mtxrInterfaceStatsRx1024To1518
        oid: 1.3.6.1.4.1.14988.1.1.14.1.1.39
        type: counter
        help: ' - 1.3.6.1.4.1.14988.1.1.14.1.1.39'
        indexes:
        - labelname: mtxrInterfaceStatsIndex
          type: gauge
        lookups:
        - labels:
          - mtxrInterfaceStatsIndex
          labelname: ifName
          oid: 1.3.6.1.2.1.31.1.1.1.1
          type: DisplayString
      - name: mtxrInterfaceStatsRx1519ToMax
        oid: 1.3.6.1.4.1.14988.1.1.14.1.1.40
        type: counter
        help: ' - 1.3.6.1.4.1.14988.1.1.14.1.1.40'
        indexes:
        - labelname: mtxrInterfaceStatsIndex
          type: gauge
        lookups:
        - labels:
          - mtxrInterfaceStatsIndex
          labelname: ifName
          oid: 1.3.6.1.2.1.31.1.1.1.1
          type: DisplayString
      - name: mtxrInterfaceStatsRxTooLong
        oid: 1.3.6.1.4.1.14988.1.1.14.1.1.41
        type: counter
        help: ' - 1.3.6.1.4.1.14988.1.1.14.1.1.41'
        indexes:
        - labelname: mtxrInterfaceStatsIndex
          type: gauge
        lookups:
        - labels:
          - mtxrInterfaceStatsIndex
          labelname: ifName
          oid: 1.3.6.1.2.1.31.1.1.1.1
          type: DisplayString
      - name: mtxrInterfaceStatsRxBroadcast
        oid: 1.3.6.1.4.1.14988.1.1.14.1.1.42
        type: counter
        help: ' - 1.3.6.1.4.1.14988.1.1.14.1.1.42'
        indexes:
        - labelname: mtxrInterfaceStatsIndex
          type: gauge
        lookups:
        - labels:
          - mtxrInterfaceStatsIndex
          labelname: ifName
          oid: 1.3.6.1.2.1.31.1.1.1.1
          type: DisplayString
      - name: mtxrInterfaceStatsRxPause
        oid: 1.3.6.1.4.1.14988.1.1.14.1.1.43
        type: counter
        help: ' - 1.3.6.1.4.1.14988.1.1.14.1.1.43'
        indexes:
        - labelname: mtxrInterfaceStatsIndex
          type: gauge
        lookups:
        - labels:
          - mtxrInterfaceStatsIndex
          labelname: ifName
          oid: 1.3.6.1.2.1.31.1.1.1.1
          type: DisplayString
      - name: mtxrInterfaceStatsRxMulticast
        oid: 1.3.6.1.4.1.14988.1.1.14.1.1.44
        type: counter
        help: ' - 1.3.6.1.4.1.14988.1.1.14.1.1.44'
        indexes:
        - labelname: mtxrInterfaceStatsIndex
          type: gauge
        lookups:
        - labels:
          - mtxrInterfaceStatsIndex
          labelname: ifName
          oid: 1.3.6.1.2.1.31.1.1.1.1
          type: DisplayString
      - name: mtxrInterfaceStatsRxFCSError
        oid: 1.3.6.1.4.1.14988.1.1.14.1.1.45
        type: counter
        help: ' - 1.3.6.1.4.1.14988.1.1.14.1.1.45'
        indexes:
        - labelname: mtxrInterfaceStatsIndex
          type: gauge
        lookups:
        - labels:
          - mtxrInterfaceStatsIndex
          labelname: ifName
          oid: 1.3.6.1.2.1.31.1.1.1.1
          type: DisplayString
      - name: mtxrInterfaceStatsRxAlignError
        oid: 1.3.6.1.4.1.14988.1.1.14.1.1.46
        type: counter
        help: ' - 1.3.6.1.4.1.14988.1.1.14.1.1.46'
        indexes:
        - labelname: mtxrInterfaceStatsIndex
          type: gauge
        lookups:
        - labels:
          - mtxrInterfaceStatsIndex
          labelname: ifName
          oid: 1.3.6.1.2.1.31.1.1.1.1
          type: DisplayString
      - name: mtxrInterfaceStatsRxFragment
        oid: 1.3.6.1.4.1.14988.1.1.14.1.1.47
        type: counter
        help: ' - 1.3.6.1.4.1.14988.1.1.14.1.1.47'
        indexes:
        - labelname: mtxrInterfaceStatsIndex
          type: gauge
        lookups:
        - labels:
          - mtxrInterfaceStatsIndex
          labelname: ifName
          oid: 1.3.6.1.2.1.31.1.1.1.1
          type: DisplayString
      - name: mtxrInterfaceStatsRxOverflow
        oid: 1.3.6.1.4.1.14988.1.1.14.1.1.48
        type: counter
        help: ' - 1.3.6.1.4.1.14988.1.1.14.1.1.48'
        indexes:
        - labelname: mtxrInterfaceStatsIndex
          type: gauge
        lookups:
        - labels:
          - mtxrInterfaceStatsIndex
          labelname: ifName
          oid: 1.3.6.1.2.1.31.1.1.1.1
          type: DisplayString
      - name: mtxrInterfaceStatsRxControl
        oid: 1.3.6.1.4.1.14988.1.1.14.1.1.49
        type: counter
        help: ' - 1.3.6.1.4.1.14988.1.1.14.1.1.49'
        indexes:
        - labelname: mtxrInterfaceStatsIndex
          type: gauge
        lookups:
        - labels:
          - mtxrInterfaceStatsIndex
          labelname: ifName
          oid: 1.3.6.1.2.1.31.1.1.1.1
          type: DisplayString
      - name: mtxrInterfaceStatsRxUnknownOp
        oid: 1.3.6.1.4.1.14988.1.1.14.1.1.50
        type: counter
        help: ' - 1.3.6.1.4.1.14988.1.1.14.1.1.50'
        indexes:
        - labelname: mtxrInterfaceStatsIndex
          type: gauge
        lookups:
        - labels:
          - mtxrInterfaceStatsIndex
          labelname: ifName
          oid: 1.3.6.1.2.1.31.1.1.1.1
          type: DisplayString
      - name: mtxrInterfaceStatsRxLengthError
        oid: 1.3.6.1.4.1.14988.1.1.14.1.1.51
        type: counter
        help: ' - 1.3.6.1.4.1.14988.1.1.14.1.1.51'
        indexes:
        - labelname: mtxrInterfaceStatsIndex
          type: gauge
        lookups:
        - labels:
          - mtxrInterfaceStatsIndex
          labelname: ifName
          oid: 1.3.6.1.2.1.31.1.1.1.1
          type: DisplayString
      - name: mtxrInterfaceStatsRxCodeError
        oid: 1.3.6.1.4.1.14988.1.1.14.1.1.52
        type: counter
        help: ' - 1.3.6.1.4.1.14988.1.1.14.1.1.52'
        indexes:
        - labelname: mtxrInterfaceStatsIndex
          type: gauge
        lookups:
        - labels:
          - mtxrInterfaceStatsIndex
          labelname: ifName
          oid: 1.3.6.1.2.1.31.1.1.1.1
          type: DisplayString
      - name: mtxrInterfaceStatsRxCarrierError
        oid: 1.3.6.1.4.1.14988.1.1.14.1.1.53
        type: counter
        help: ' - 1.3.6.1.4.1.14988.1.1.14.1.1.53'
        indexes:
        - labelname: mtxrInterfaceStatsIndex
          type: gauge
        lookups:
        - labels:
          - mtxrInterfaceStatsIndex
          labelname: ifName
          oid: 1.3.6.1.2.1.31.1.1.1.1
          type: DisplayString
      - name: mtxrInterfaceStatsRxJabber
        oid: 1.3.6.1.4.1.14988.1.1.14.1.1.54
        type: counter
        help: ' - 1.3.6.1.4.1.14988.1.1.14.1.1.54'
        indexes:
        - labelname: mtxrInterfaceStatsIndex
          type: gauge
        lookups:
        - labels:
          - mtxrInterfaceStatsIndex
          labelname: ifName
          oid: 1.3.6.1.2.1.31.1.1.1.1
          type: DisplayString
      - name: mtxrInterfaceStatsRxDrop
        oid: 1.3.6.1.4.1.14988.1.1.14.1.1.55
        type: counter
        help: ' - 1.3.6.1.4.1.14988.1.1.14.1.1.55'
        indexes:
        - labelname: mtxrInterfaceStatsIndex
          type: gauge
        lookups:
        - labels:
          - mtxrInterfaceStatsIndex
          labelname: ifName
          oid: 1.3.6.1.2.1.31.1.1.1.1
          type: DisplayString
      - name: mtxrInterfaceStatsTxBytes
        oid: 1.3.6.1.4.1.14988.1.1.14.1.1.61
        type: counter
        help: ' - 1.3.6.1.4.1.14988.1.1.14.1.1.61'
        indexes:
        - labelname: mtxrInterfaceStatsIndex
          type: gauge
        lookups:
        - labels:
          - mtxrInterfaceStatsIndex
          labelname: ifName
          oid: 1.3.6.1.2.1.31.1.1.1.1
          type: DisplayString
      - name: mtxrInterfaceStatsTxPackets
        oid: 1.3.6.1.4.1.14988.1.1.14.1.1.62
        type: counter
        help: ' - 1.3.6.1.4.1.14988.1.1.14.1.1.62'
        indexes:
        - labelname: mtxrInterfaceStatsIndex
          type: gauge
        lookups:
        - labels:
          - mtxrInterfaceStatsIndex
          labelname: ifName
          oid: 1.3.6.1.2.1.31.1.1.1.1
          type: DisplayString
      - name: mtxrInterfaceStatsTxTooShort
        oid: 1.3.6.1.4.1.14988.1.1.14.1.1.63
        type: counter
        help: ' - 1.3.6.1.4.1.14988.1.1.14.1.1.63'
        indexes:
        - labelname: mtxrInterfaceStatsIndex
          type: gauge
        lookups:
        - labels:
          - mtxrInterfaceStatsIndex
          labelname: ifName
          oid: 1.3.6.1.2.1.31.1.1.1.1
          type: DisplayString
      - name: mtxrInterfaceStatsTx64
        oid: 1.3.6.1.4.1.14988.1.1.14.1.1.64
        type: counter
        help: ' - 1.3.6.1.4.1.14988.1.1.14.1.1.64'
        indexes:
        - labelname: mtxrInterfaceStatsIndex
          type: gauge
        lookups:
        - labels:
          - mtxrInterfaceStatsIndex
          labelname: ifName
          oid: 1.3.6.1.2.1.31.1.1.1.1
          type: DisplayString
      - name: mtxrInterfaceStatsTx65To127
        oid: 1.3.6.1.4.1.14988.1.1.14.1.1.65
        type: counter
        help: ' - 1.3.6.1.4.1.14988.1.1.14.1.1.65'
        indexes:
        - labelname: mtxrInterfaceStatsIndex
          type: gauge
        lookups:
        - labels:
          - mtxrInterfaceStatsIndex
          labelname: ifName
          oid: 1.3.6.1.2.1.31.1.1.1.1
          type: DisplayString
      - name: mtxrInterfaceStatsTx128To255
        oid: 1.3.6.1.4.1.14988.1.1.14.1.1.66
        type: counter
        help: ' - 1.3.6.1.4.1.14988.1.1.14.1.1.66'
        indexes:
        - labelname: mtxrInterfaceStatsIndex
          type: gauge
        lookups:
        - labels:
          - mtxrInterfaceStatsIndex
          labelname: ifName
          oid: 1.3.6.1.2.1.31.1.1.1.1
          type: DisplayString
      - name: mtxrInterfaceStatsTx256To511
        oid: 1.3.6.1.4.1.14988.1.1.14.1.1.67
        type: counter
        help: ' - 1.3.6.1.4.1.14988.1.1.14.1.1.67'
        indexes:
        - labelname: mtxrInterfaceStatsIndex
          type: gauge
        lookups:
        - labels:
          - mtxrInterfaceStatsIndex
          labelname: ifName
          oid: 1.3.6.1.2.1.31.1.1.1.1
          type: DisplayString
      - name: mtxrInterfaceStatsTx512To1023
        oid: 1.3.6.1.4.1.14988.1.1.14.1.1.68
        type: counter
        help: ' - 1.3.6.1.4.1.14988.1.1.14.1.1.68'
        indexes:
        - labelname: mtxrInterfaceStatsIndex
          type: gauge
        lookups:
        - labels:
          - mtxrInterfaceStatsIndex
          labelname: ifName
          oid: 1.3.6.1.2.1.31.1.1.1.1
          type: DisplayString
      - name: mtxrInterfaceStatsTx1024To1518
        oid: 1.3.6.1.4.1.14988.1.1.14.1.1.69
        type: counter
        help: ' - 1.3.6.1.4.1.14988.1.1.14.1.1.69'
        indexes:
        - labelname: mtxrInterfaceStatsIndex
          type: gauge
        lookups:
        - labels:
          - mtxrInterfaceStatsIndex
          labelname: ifName
          oid: 1.3.6.1.2.1.31.1.1.1.1
          type: DisplayString
      - name: mtxrInterfaceStatsTx1519ToMax
        oid: 1.3.6.1.4.1.14988.1.1.14.1.1.70
        type: counter
        help: ' - 1.3.6.1.4.1.14988.1.1.14.1.1.70'
        indexes:
        - labelname: mtxrInterfaceStatsIndex
          type: gauge
        lookups:
        - labels:
          - mtxrInterfaceStatsIndex
          labelname: ifName
          oid: 1.3.6.1.2.1.31.1.1.1.1
          type: DisplayString
      - name: mtxrInterfaceStatsTxTooLong
        oid: 1.3.6.1.4.1.14988.1.1.14.1.1.71
        type: counter
        help: ' - 1.3.6.1.4.1.14988.1.1.14.1.1.71'
        indexes:
        - labelname: mtxrInterfaceStatsIndex
          type: gauge
        lookups:
        - labels:
          - mtxrInterfaceStatsIndex
          labelname: ifName
          oid: 1.3.6.1.2.1.31.1.1.1.1
          type: DisplayString
      - name: mtxrInterfaceStatsTxBroadcast
        oid: 1.3.6.1.4.1.14988.1.1.14.1.1.72
        type: counter
        help: ' - 1.3.6.1.4.1.14988.1.1.14.1.1.72'
        indexes:
        - labelname: mtxrInterfaceStatsIndex
          type: gauge
        lookups:
        - labels:
          - mtxrInterfaceStatsIndex
          labelname: ifName
          oid: 1.3.6.1.2.1.31.1.1.1.1
          type: DisplayString
      - name: mtxrInterfaceStatsTxPause
        oid: 1.3.6.1.4.1.14988.1.1.14.1.1.73
        type: counter
        help: ' - 1.3.6.1.4.1.14988.1.1.14.1.1.73'
        indexes:
        - labelname: mtxrInterfaceStatsIndex
          type: gauge
        lookups:
        - labels:
          - mtxrInterfaceStatsIndex
          labelname: ifName
          oid: 1.3.6.1.2.1.31.1.1.1.1
          type: DisplayString
      - name: mtxrInterfaceStatsTxMulticast
        oid: 1.3.6.1.4.1.14988.1.1.14.1.1.74
        type: counter
        help: ' - 1.3.6.1.4.1.14988.1.1.14.1.1.74'
        indexes:
        - labelname: mtxrInterfaceStatsIndex
          type: gauge
        lookups:
        - labels:
          - mtxrInterfaceStatsIndex
          labelname: ifName
          oid: 1.3.6.1.2.1.31.1.1.1.1
          type: DisplayString
      - name: mtxrInterfaceStatsTxUnderrun
        oid: 1.3.6.1.4.1.14988.1.1.14.1.1.75
        type: counter
        help: ' - 1.3.6.1.4.1.14988.1.1.14.1.1.75'
        indexes:
        - labelname: mtxrInterfaceStatsIndex
          type: gauge
        lookups:
        - labels:
          - mtxrInterfaceStatsIndex
          labelname: ifName
          oid: 1.3.6.1.2.1.31.1.1.1.1
          type: DisplayString
      - name: mtxrInterfaceStatsTxCollision
        oid: 1.3.6.1.4.1.14988.1.1.14.1.1.76
        type: counter
        help: ' - 1.3.6.1.4.1.14988.1.1.14.1.1.76'
        indexes:
        - labelname: mtxrInterfaceStatsIndex
          type: gauge
        lookups:
        - labels:
          - mtxrInterfaceStatsIndex
          labelname: ifName
          oid: 1.3.6.1.2.1.31.1.1.1.1
          type: DisplayString
      - name: mtxrInterfaceStatsTxExcessiveCollision
        oid: 1.3.6.1.4.1.14988.1.1.14.1.1.77
        type: counter
        help: ' - 1.3.6.1.4.1.14988.1.1.14.1.1.77'
        indexes:
        - labelname: mtxrInterfaceStatsIndex
          type: gauge
        lookups:
        - labels:
          - mtxrInterfaceStatsIndex
          labelname: ifName
          oid: 1.3.6.1.2.1.31.1.1.1.1
          type: DisplayString
      - name: mtxrInterfaceStatsTxMultipleCollision
        oid: 1.3.6.1.4.1.14988.1.1.14.1.1.78
        type: counter
        help: ' - 1.3.6.1.4.1.14988.1.1.14.1.1.78'
        indexes:
        - labelname: mtxrInterfaceStatsIndex
          type: gauge
        lookups:
        - labels:
          - mtxrInterfaceStatsIndex
          labelname: ifName
          oid: 1.3.6.1.2.1.31.1.1.1.1
          type: DisplayString
      - name: mtxrInterfaceStatsTxSingleCollision
        oid: 1.3.6.1.4.1.14988.1.1.14.1.1.79
        type: counter
        help: ' - 1.3.6.1.4.1.14988.1.1.14.1.1.79'
        indexes:
        - labelname: mtxrInterfaceStatsIndex
          type: gauge
        lookups:
        - labels:
          - mtxrInterfaceStatsIndex
          labelname: ifName
          oid: 1.3.6.1.2.1.31.1.1.1.1
          type: DisplayString
      - name: mtxrInterfaceStatsTxExcessiveDeferred
        oid: 1.3.6.1.4.1.14988.1.1.14.1.1.80
        type: counter
        help: ' - 1.3.6.1.4.1.14988.1.1.14.1.1.80'
        indexes:
        - labelname: mtxrInterfaceStatsIndex
          type: gauge
        lookups:
        - labels:
          - mtxrInterfaceStatsIndex
          labelname: ifName
          oid: 1.3.6.1.2.1.31.1.1.1.1
          type: DisplayString
      - name: mtxrInterfaceStatsTxDeferred
        oid: 1.3.6.1.4.1.14988.1.1.14.1.1.81
        type: counter
        help: ' - 1.3.6.1.4.1.14988.1.1.14.1.1.81'
        indexes:
        - labelname: mtxrInterfaceStatsIndex
          type: gauge
        lookups:
        - labels:
          - mtxrInterfaceStatsIndex
          labelname: ifName
          oid: 1.3.6.1.2.1.31.1.1.1.1
          type: DisplayString
      - name: mtxrInterfaceStatsTxLateCollision
        oid: 1.3.6.1.4.1.14988.1.1.14.1.1.82
        type: counter
        help: ' - 1.3.6.1.4.1.14988.1.1.14.1.1.82'
        indexes:
        - labelname: mtxrInterfaceStatsIndex
          type: gauge
        lookups:
        - labels:
          - mtxrInterfaceStatsIndex
          labelname: ifName
          oid: 1.3.6.1.2.1.31.1.1.1.1
          type: DisplayString
      - name: mtxrInterfaceStatsTxTotalCollision
        oid: 1.3.6.1.4.1.14988.1.1.14.1.1.83
        type: counter
        help: ' - 1.3.6.1.4.1.14988.1.1.14.1.1.83'
        indexes:
        - labelname: mtxrInterfaceStatsIndex
          type: gauge
        lookups:
        - labels:
          - mtxrInterfaceStatsIndex
          labelname: ifName
          oid: 1.3.6.1.2.1.31.1.1.1.1
          type: DisplayString
      - name: mtxrInterfaceStatsTxPauseHonored
        oid: 1.3.6.1.4.1.14988.1.1.14.1.1.84
        type: counter
        help: ' - 1.3.6.1.4.1.14988.1.1.14.1.1.84'
        indexes:
        - labelname: mtxrInterfaceStatsIndex
          type: gauge
        lookups:
        - labels:
          - mtxrInterfaceStatsIndex
          labelname: ifName
          oid: 1.3.6.1.2.1.31.1.1.1.1
          type: DisplayString
      - name: mtxrInterfaceStatsTxDrop
        oid: 1.3.6.1.4.1.14988.1.1.14.1.1.85
        type: counter
        help: ' - 1.3.6.1.4.1.14988.1.1.14.1.1.85'
        indexes:
        - labelname: mtxrInterfaceStatsIndex
          type: gauge
        lookups:
        - labels:
          - mtxrInterfaceStatsIndex
          labelname: ifName
          oid: 1.3.6.1.2.1.31.1.1.1.1
          type: DisplayString
      - name: mtxrInterfaceStatsTxJabber
        oid: 1.3.6.1.4.1.14988.1.1.14.1.1.86
        type: counter
        help: ' - 1.3.6.1.4.1.14988.1.1.14.1.1.86'
        indexes:
        - labelname: mtxrInterfaceStatsIndex
          type: gauge
        lookups:
        - labels:
          - mtxrInterfaceStatsIndex
          labelname: ifName
          oid: 1.3.6.1.2.1.31.1.1.1.1
          type: DisplayString
      - name: mtxrInterfaceStatsTxFCSError
        oid: 1.3.6.1.4.1.14988.1.1.14.1.1.87
        type: counter
        help: ' - 1.3.6.1.4.1.14988.1.1.14.1.1.87'
        indexes:
        - labelname: mtxrInterfaceStatsIndex
          type: gauge
        lookups:
        - labels:
          - mtxrInterfaceStatsIndex
          labelname: ifName
          oid: 1.3.6.1.2.1.31.1.1.1.1
          type: DisplayString
      - name: mtxrInterfaceStatsTxControl
        oid: 1.3.6.1.4.1.14988.1.1.14.1.1.88
        type: counter
        help: ' - 1.3.6.1.4.1.14988.1.1.14.1.1.88'
        indexes:
        - labelname: mtxrInterfaceStatsIndex
          type: gauge
        lookups:
        - labels:
          - mtxrInterfaceStatsIndex
          labelname: ifName
          oid: 1.3.6.1.2.1.31.1.1.1.1
          type: DisplayString
      - name: mtxrInterfaceStatsTxFragment
        oid: 1.3.6.1.4.1.14988.1.1.14.1.1.89
        type: counter
        help: ' - 1.3.6.1.4.1.14988.1.1.14.1.1.89'
        indexes:
        - labelname: mtxrInterfaceStatsIndex
          type: gauge
        lookups:
        - labels:
          - mtxrInterfaceStatsIndex
          labelname: ifName
          oid: 1.3.6.1.2.1.31.1.1.1.1
          type: DisplayString
      - name: mtxrInterfaceStatsLinkDowns
        oid: 1.3.6.1.4.1.14988.1.1.14.1.1.90
        type: counter
        help: ' - 1.3.6.1.4.1.14988.1.1.14.1.1.90'
        indexes:
        - labelname: mtxrInterfaceStatsIndex
          type: gauge
        lookups:
        - labels:
          - mtxrInterfaceStatsIndex
          labelname: ifName
          oid: 1.3.6.1.2.1.31.1.1.1.1
          type: DisplayString
      - name: mtxrPOEInterfaceIndex
        oid: 1.3.6.1.4.1.14988.1.1.15.1.1.1
        type: gauge
        help: ' - 1.3.6.1.4.1.14988.1.1.15.1.1.1'
        indexes:
        - labelname: mtxrPOEInterfaceIndex
          type: gauge
      - name: mtxrPOEName
        oid: 1.3.6.1.4.1.14988.1.1.15.1.1.2
        type: DisplayString
        help: ' - 1.3.6.1.4.1.14988.1.1.15.1.1.2'
        indexes:
        - labelname: mtxrPOEInterfaceIndex
          type: gauge
      - name: mtxrPOEStatus
        oid: 1.3.6.1.4.1.14988.1.1.15.1.1.3
        type: gauge
        help: ' - 1.3.6.1.4.1.14988.1.1.15.1.1.3'
        indexes:
        - labelname: mtxrPOEInterfaceIndex
          type: gauge
        enum_values:
          1: disabled
          2: waitingForLoad
          3: poweredOn
          4: overload
      - name: mtxrPOEVoltage
        oid: 1.3.6.1.4.1.14988.1.1.15.1.1.4
        type: gauge
        help: V - 1.3.6.1.4.1.14988.1.1.15.1.1.4
        indexes:
        - labelname: mtxrPOEInterfaceIndex
          type: gauge
      - name: mtxrPOECurrent
        oid: 1.3.6.1.4.1.14988.1.1.15.1.1.5
        type: gauge
        help: mA - 1.3.6.1.4.1.14988.1.1.15.1.1.5
        indexes:
        - labelname: mtxrPOEInterfaceIndex
          type: gauge
      - name: mtxrPOEPower
        oid: 1.3.6.1.4.1.14988.1.1.15.1.1.6
        type: gauge
        help: W - 1.3.6.1.4.1.14988.1.1.15.1.1.6
        indexes:
        - labelname: mtxrPOEInterfaceIndex
          type: gauge
      - name: mtxrLTEModemInterfaceIndex
        oid: 1.3.6.1.4.1.14988.1.1.16.1.1.1
        type: gauge
        help: ' - 1.3.6.1.4.1.14988.1.1.16.1.1.1'
        indexes:
        - labelname: mtxrLTEModemInterfaceIndex
          type: gauge
      - name: mtxrLTEModemSignalRSSI
        oid: 1.3.6.1.4.1.14988.1.1.16.1.1.2
        type: gauge
        help: dBm - 1.3.6.1.4.1.14988.1.1.16.1.1.2
        indexes:
        - labelname: mtxrLTEModemInterfaceIndex
          type: gauge
      - name: mtxrLTEModemSignalRSRQ
        oid: 1.3.6.1.4.1.14988.1.1.16.1.1.3
        type: gauge
        help: dB - 1.3.6.1.4.1.14988.1.1.16.1.1.3
        indexes:
        - labelname: mtxrLTEModemInterfaceIndex
          type: gauge
      - name: mtxrLTEModemSignalRSRP
        oid: 1.3.6.1.4.1.14988.1.1.16.1.1.4
        type: gauge
        help: dBm - 1.3.6.1.4.1.14988.1.1.16.1.1.4
        indexes:
        - labelname: mtxrLTEModemInterfaceIndex
          type: gauge
      - name: mtxrLTEModemCellId
        oid: 1.3.6.1.4.1.14988.1.1.16.1.1.5
        type: gauge
        help: current cell ID - 1.3.6.1.4.1.14988.1.1.16.1.1.5
        indexes:
        - labelname: mtxrLTEModemInterfaceIndex
          type: gauge
      - name: mtxrLTEModemAccessTechnology
        oid: 1.3.6.1.4.1.14988.1.1.16.1.1.6
        type: gauge
        help: as reported by +CREG - 1.3.6.1.4.1.14988.1.1.16.1.1.6
        indexes:
        - labelname: mtxrLTEModemInterfaceIndex
          type: gauge
        enum_values:
          -1: unknown
          0: gsmcompact
          1: gsm
          2: utran
          3: egprs
          4: hsdpa
          5: hsupa
          6: hsdpahsupa
          7: eutran
      - name: mtxrLTEModemSignalSINR
        oid: 1.3.6.1.4.1.14988.1.1.16.1.1.7
        type: gauge
        help: dB - 1.3.6.1.4.1.14988.1.1.16.1.1.7
        indexes:
        - labelname: mtxrLTEModemInterfaceIndex
          type: gauge
      - name: mtxrLTEModemEnbId
        oid: 1.3.6.1.4.1.14988.1.1.16.1.1.8
        type: gauge
        help: ' - 1.3.6.1.4.1.14988.1.1.16.1.1.8'
        indexes:
        - labelname: mtxrLTEModemInterfaceIndex
          type: gauge
      - name: mtxrLTEModemSectorId
        oid: 1.3.6.1.4.1.14988.1.1.16.1.1.9
        type: gauge
        help: ' - 1.3.6.1.4.1.14988.1.1.16.1.1.9'
        indexes:
        - labelname: mtxrLTEModemInterfaceIndex
          type: gauge
      - name: mtxrLTEModemLac
        oid: 1.3.6.1.4.1.14988.1.1.16.1.1.10
        type: gauge
        help: ' - 1.3.6.1.4.1.14988.1.1.16.1.1.10'
        indexes:
        - labelname: mtxrLTEModemInterfaceIndex
          type: gauge
      - name: mtxrLTEModemIMEI
        oid: 1.3.6.1.4.1.14988.1.1.16.1.1.11
        type: DisplayString
        help: ' - 1.3.6.1.4.1.14988.1.1.16.1.1.11'
        indexes:
        - labelname: mtxrLTEModemInterfaceIndex
          type: gauge
      - name: mtxrLTEModemIMSI
        oid: 1.3.6.1.4.1.14988.1.1.16.1.1.12
        type: DisplayString
        help: ' - 1.3.6.1.4.1.14988.1.1.16.1.1.12'
        indexes:
        - labelname: mtxrLTEModemInterfaceIndex
          type: gauge
      - name: mtxrLTEModemUICC
        oid: 1.3.6.1.4.1.14988.1.1.16.1.1.13
        type: DisplayString
        help: ' - 1.3.6.1.4.1.14988.1.1.16.1.1.13'
        indexes:
        - labelname: mtxrLTEModemInterfaceIndex
          type: gauge
      - name: mtxrLTEModemRAT
        oid: 1.3.6.1.4.1.14988.1.1.16.1.1.14
        type: DisplayString
        help: ' - 1.3.6.1.4.1.14988.1.1.16.1.1.14'
        indexes:
        - labelname: mtxrLTEModemInterfaceIndex
          type: gauge
      - name: mtxrPartitionIndex
        oid: 1.3.6.1.4.1.14988.1.1.17.1.1.1
        type: gauge
        help: ' - 1.3.6.1.4.1.14988.1.1.17.1.1.1'
        indexes:
        - labelname: mtxrPartitionIndex
          type: gauge
      - name: mtxrPartitionName
        oid: 1.3.6.1.4.1.14988.1.1.17.1.1.2
        type: DisplayString
        help: ' - 1.3.6.1.4.1.14988.1.1.17.1.1.2'
        indexes:
        - labelname: mtxrPartitionIndex
          type: gauge
      - name: mtxrPartitionSize
        oid: 1.3.6.1.4.1.14988.1.1.17.1.1.3
        type: gauge
        help: MB - 1.3.6.1.4.1.14988.1.1.17.1.1.3
        indexes:
        - labelname: mtxrPartitionIndex
          type: gauge
      - name: mtxrPartitionVersion
        oid: 1.3.6.1.4.1.14988.1.1.17.1.1.4
        type: DisplayString
        help: ' - 1.3.6.1.4.1.14988.1.1.17.1.1.4'
        indexes:
        - labelname: mtxrPartitionIndex
          type: gauge
      - name: mtxrPartitionActive
        oid: 1.3.6.1.4.1.14988.1.1.17.1.1.5
        type: gauge
        help: ' - 1.3.6.1.4.1.14988.1.1.17.1.1.5'
        indexes:
        - labelname: mtxrPartitionIndex
          type: gauge
        enum_values:
          0: "false"
          1: "true"
      - name: mtxrPartitionRunning
        oid: 1.3.6.1.4.1.14988.1.1.17.1.1.6
        type: gauge
        help: ' - 1.3.6.1.4.1.14988.1.1.17.1.1.6'
        indexes:
        - labelname: mtxrPartitionIndex
          type: gauge
        enum_values:
          0: "false"
          1: "true"
      - name: mtxrScriptRunIndex
        oid: 1.3.6.1.4.1.14988.1.1.18.1.1.1
        type: gauge
        help: ' - 1.3.6.1.4.1.14988.1.1.18.1.1.1'
        indexes:
        - labelname: mtxrScriptRunIndex
          type: gauge
      - name: mtxrScriptRunOutput
        oid: 1.3.6.1.4.1.14988.1.1.18.1.1.2
        type: DisplayString
        help: this oid on get request will run script and return it's output - 1.3.6.1.4.1.14988.1.1.18.1.1.2
        indexes:
        - labelname: mtxrScriptRunIndex
          type: gauge
      - name: mtxrOpticalIndex
        oid: 1.3.6.1.4.1.14988.1.1.19.1.1.1
        type: gauge
        help: ' - 1.3.6.1.4.1.14988.1.1.19.1.1.1'
        indexes:
        - labelname: mtxrOpticalIndex
          type: gauge
      - name: mtxrOpticalName
        oid: 1.3.6.1.4.1.14988.1.1.19.1.1.2
        type: DisplayString
        help: ' - 1.3.6.1.4.1.14988.1.1.19.1.1.2'
        indexes:
        - labelname: mtxrOpticalIndex
          type: gauge
      - name: mtxrOpticalRxLoss
        oid: 1.3.6.1.4.1.14988.1.1.19.1.1.3
        type: gauge
        help: ' - 1.3.6.1.4.1.14988.1.1.19.1.1.3'
        indexes:
        - labelname: mtxrOpticalIndex
          type: gauge
        enum_values:
          0: "false"
          1: "true"
      - name: mtxrOpticalTxFault
        oid: 1.3.6.1.4.1.14988.1.1.19.1.1.4
        type: gauge
        help: ' - 1.3.6.1.4.1.14988.1.1.19.1.1.4'
        indexes:
        - labelname: mtxrOpticalIndex
          type: gauge
        enum_values:
          0: "false"
          1: "true"
      - name: mtxrOpticalWavelength
        oid: 1.3.6.1.4.1.14988.1.1.19.1.1.5
        type: gauge
        help: ' - 1.3.6.1.4.1.14988.1.1.19.1.1.5'
        indexes:
        - labelname: mtxrOpticalIndex
          type: gauge
      - name: mtxrOpticalTemperature
        oid: 1.3.6.1.4.1.14988.1.1.19.1.1.6
        type: gauge
        help: ' - 1.3.6.1.4.1.14988.1.1.19.1.1.6'
        indexes:
        - labelname: mtxrOpticalIndex
          type: gauge
      - name: mtxrOpticalSupplyVoltage
        oid: 1.3.6.1.4.1.14988.1.1.19.1.1.7
        type: gauge
        help: ' - 1.3.6.1.4.1.14988.1.1.19.1.1.7'
        indexes:
        - labelname: mtxrOpticalIndex
          type: gauge
      - name: mtxrOpticalTxBiasCurrent
        oid: 1.3.6.1.4.1.14988.1.1.19.1.1.8
        type: gauge
        help: ' - 1.3.6.1.4.1.14988.1.1.19.1.1.8'
        indexes:
        - labelname: mtxrOpticalIndex
          type: gauge
      - name: mtxrOpticalTxPower
        oid: 1.3.6.1.4.1.14988.1.1.19.1.1.9
        type: gauge
        help: ' - 1.3.6.1.4.1.14988.1.1.19.1.1.9'
        indexes:
        - labelname: mtxrOpticalIndex
          type: gauge
      - name: mtxrOpticalRxPower
        oid: 1.3.6.1.4.1.14988.1.1.19.1.1.10
        type: gauge
        help: ' - 1.3.6.1.4.1.14988.1.1.19.1.1.10'
        indexes:
        - labelname: mtxrOpticalIndex
          type: gauge
      - name: mtxrIkeSACount
        oid: 1.3.6.1.4.1.14988.1.1.20.1
        type: gauge
        help: IKE SA count - 1.3.6.1.4.1.14988.1.1.20.1
      - name: mtxrIkeSAIndex
        oid: 1.3.6.1.4.1.14988.1.1.20.2.1.1
        type: gauge
        help: ' - 1.3.6.1.4.1.14988.1.1.20.2.1.1'
        indexes:
        - labelname: mtxrIkeSAIndex
          type: gauge
      - name: mtxrIkeSAInitiatorCookie
        oid: 1.3.6.1.4.1.14988.1.1.20.2.1.2
        type: DisplayString
        help: initiator SPI - 1.3.6.1.4.1.14988.1.1.20.2.1.2
        indexes:
        - labelname: mtxrIkeSAIndex
          type: gauge
      - name: mtxrIkeSAResponderCookie
        oid: 1.3.6.1.4.1.14988.1.1.20.2.1.3
        type: DisplayString
        help: responder SPI - 1.3.6.1.4.1.14988.1.1.20.2.1.3
        indexes:
        - labelname: mtxrIkeSAIndex
          type: gauge
      - name: mtxrIkeSAResponder
        oid: 1.3.6.1.4.1.14988.1.1.20.2.1.4
        type: gauge
        help: IKE side - 1.3.6.1.4.1.14988.1.1.20.2.1.4
        indexes:
        - labelname: mtxrIkeSAIndex
          type: gauge
        enum_values:
          0: "false"
          1: "true"
      - name: mtxrIkeSANatt
        oid: 1.3.6.1.4.1.14988.1.1.20.2.1.5
        type: gauge
        help: NAT is detected - 1.3.6.1.4.1.14988.1.1.20.2.1.5
        indexes:
        - labelname: mtxrIkeSAIndex
          type: gauge
        enum_values:
          0: "false"
          1: "true"
      - name: mtxrIkeSAVersion
        oid: 1.3.6.1.4.1.14988.1.1.20.2.1.6
        type: gauge
        help: protocol version - 1.3.6.1.4.1.14988.1.1.20.2.1.6
        indexes:
        - labelname: mtxrIkeSAIndex
          type: gauge
      - name: mtxrIkeSAState
        oid: 1.3.6.1.4.1.14988.1.1.20.2.1.7
        type: gauge
        help: ' - 1.3.6.1.4.1.14988.1.1.20.2.1.7'
        indexes:
        - labelname: mtxrIkeSAIndex
          type: gauge
        enum_values:
          1: exchange
          2: established
          3: expired
          4: eap
      - name: mtxrIkeSAUptime
        oid: 1.3.6.1.4.1.14988.1.1.20.2.1.8
        type: gauge
        help: ' - 1.3.6.1.4.1.14988.1.1.20.2.1.8'
        indexes:
        - labelname: mtxrIkeSAIndex
          type: gauge
      - name: mtxrIkeSASeen
        oid: 1.3.6.1.4.1.14988.1.1.20.2.1.9
        type: gauge
        help: time elapsed since last valid IKE packet - 1.3.6.1.4.1.14988.1.1.20.2.1.9
        indexes:
        - labelname: mtxrIkeSAIndex
          type: gauge
      - name: mtxrIkeSAIdentity
        oid: 1.3.6.1.4.1.14988.1.1.20.2.1.10
        type: DisplayString
        help: peer identity - 1.3.6.1.4.1.14988.1.1.20.2.1.10
        indexes:
        - labelname: mtxrIkeSAIndex
          type: gauge
      - name: mtxrIkeSAPh2Count
        oid: 1.3.6.1.4.1.14988.1.1.20.2.1.11
        type: gauge
        help: total ph2 SA pairs - 1.3.6.1.4.1.14988.1.1.20.2.1.11
        indexes:
        - labelname: mtxrIkeSAIndex
          type: gauge
      - name: mtxrIkeSALocalAddressType
        oid: 1.3.6.1.4.1.14988.1.1.20.2.1.12
        type: gauge
        help: ' - 1.3.6.1.4.1.14988.1.1.20.2.1.12'
        indexes:
        - labelname: mtxrIkeSAIndex
          type: gauge
        enum_values:
          0: unknown
          1: ipv4
          2: ipv6
          3: ipv4z
          4: ipv6z
          16: dns
      - name: mtxrIkeSALocalAddress
        oid: 1.3.6.1.4.1.14988.1.1.20.2.1.13
        type: InetAddress
        help: ' - 1.3.6.1.4.1.14988.1.1.20.2.1.13'
        indexes:
        - labelname: mtxrIkeSAIndex
          type: gauge
      - name: mtxrIkeSALocalPort
        oid: 1.3.6.1.4.1.14988.1.1.20.2.1.14
        type: gauge
        help: ' - 1.3.6.1.4.1.14988.1.1.20.2.1.14'
        indexes:
        - labelname: mtxrIkeSAIndex
          type: gauge
      - name: mtxrIkeSAPeerAddressType
        oid: 1.3.6.1.4.1.14988.1.1.20.2.1.15
        type: gauge
        help: ' - 1.3.6.1.4.1.14988.1.1.20.2.1.15'
        indexes:
        - labelname: mtxrIkeSAIndex
          type: gauge
        enum_values:
          0: unknown
          1: ipv4
          2: ipv6
          3: ipv4z
          4: ipv6z
          16: dns
      - name: mtxrIkeSAPeerAddress
        oid: 1.3.6.1.4.1.14988.1.1.20.2.1.16
        type: InetAddress
        help: ' - 1.3.6.1.4.1.14988.1.1.20.2.1.16'
        indexes:
        - labelname: mtxrIkeSAIndex
          type: gauge
      - name: mtxrIkeSAPeerPort
        oid: 1.3.6.1.4.1.14988.1.1.20.2.1.17
        type: gauge
        help: ' - 1.3.6.1.4.1.14988.1.1.20.2.1.17'
        indexes:
        - labelname: mtxrIkeSAIndex
          type: gauge
      - name: mtxrIkeSADynamicAddressType
        oid: 1.3.6.1.4.1.14988.1.1.20.2.1.18
        type: gauge
        help: ' - 1.3.6.1.4.1.14988.1.1.20.2.1.18'
        indexes:
        - labelname: mtxrIkeSAIndex
          type: gauge
        enum_values:
          0: unknown
          1: ipv4
          2: ipv6
          3: ipv4z
          4: ipv6z
          16: dns
      - name: mtxrIkeSADynamicAddress
        oid: 1.3.6.1.4.1.14988.1.1.20.2.1.19
        type: InetAddress
        help: dynamic address allocated by mode config - 1.3.6.1.4.1.14988.1.1.20.2.1.19
        indexes:
        - labelname: mtxrIkeSAIndex
          type: gauge
      - name: mtxrIkeSATxBytes
        oid: 1.3.6.1.4.1.14988.1.1.20.2.1.20
        type: counter
        help: ph2 SA tx bytes - 1.3.6.1.4.1.14988.1.1.20.2.1.20
        indexes:
        - labelname: mtxrIkeSAIndex
          type: gauge
      - name: mtxrIkeSARxBytes
        oid: 1.3.6.1.4.1.14988.1.1.20.2.1.21
        type: counter
        help: ph2 SA rx bytes - 1.3.6.1.4.1.14988.1.1.20.2.1.21
        indexes:
        - labelname: mtxrIkeSAIndex
          type: gauge
      - name: mtxrIkeSATxPackets
        oid: 1.3.6.1.4.1.14988.1.1.20.2.1.22
        type: counter
        help: ph2 SA tx packets - 1.3.6.1.4.1.14988.1.1.20.2.1.22
        indexes:
        - labelname: mtxrIkeSAIndex
          type: gauge
      - name: mtxrIkeSARxPackets
        oid: 1.3.6.1.4.1.14988.1.1.20.2.1.23
        type: counter
        help: ph2 SA rx packets - 1.3.6.1.4.1.14988.1.1.20.2.1.23
        indexes:
        - labelname: mtxrIkeSAIndex
          type: gauge
      - name: laIndex
        oid: 1.3.6.1.4.1.2021.10.1.1
        type: gauge
        help: reference index/row number for each observed loadave. - 1.3.6.1.4.1.2021.10.1.1
        indexes:
        - labelname: laIndex
          type: gauge
        lookups:
        - labels:
          - laIndex
          labelname: laNames
          oid: 1.3.6.1.4.1.2021.10.1.2
          type: DisplayString
        - labels: []
          labelname: laIndex


