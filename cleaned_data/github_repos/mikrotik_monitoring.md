# Repository Information
Name: mikrotik_monitoring

# Directory Structure
Directory structure:
└── github_repos/mikrotik_monitoring/
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
    │   │       │   └── main
    │   │       └── remotes/
    │   │           └── origin/
    │   │               └── HEAD
    │   ├── objects/
    │   │   ├── info/
    │   │   └── pack/
    │   │       ├── pack-7a3010fb7c7285303dca6104c6c1de9b526a0afd.idx
    │   │       └── pack-7a3010fb7c7285303dca6104c6c1de9b526a0afd.pack
    │   ├── packed-refs
    │   └── refs/
    │       ├── heads/
    │       │   └── main
    │       ├── remotes/
    │       │   └── origin/
    │       │       └── HEAD
    │       └── tags/
    ├── .gitignore
    │   └── settings.json
    ├── blackbox/
    │   └── blackbox.yml
    ├── doc/
    ├── docker-armor
    ├── docker-compose-armored.yml
    ├── docker-compose.yml
    ├── grafana/
    │   └── provisioning/
    │       ├── dashboards/
    │       │   ├── dashboard.yml
    │       │   └── mikrotik/
    │       │       └── monitor.json
    │       └── datasources/
    │           └── datasource.yml
    ├── LICENSE
    ├── Makefile
    ├── mktxp/
    │   ├── mktxp.conf
    │   └── _mktxp.conf
    ├── nginx/
    │   ├── nginx-selfsigned.crt
    │   ├── nginx-selfsigned.key
    │   ├── nginx.conf
    │   └── self-signed.conf
    ├── prometheus/
    │   └── prometheus.yml
    └── README.md


# Content
File: /.env
CONFIG_FILE=/config/config.yml


File: /.git\config
[core]
	repositoryformatversion = 0
	filemode = false
	bare = false
	logallrefupdates = true
	symlinks = false
	ignorecase = true
[remote "origin"]
	url = https://github.com/M0r13n/mikrotik_monitoring.git
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
0000000000000000000000000000000000000000 b9e0bd8681efc01495dd75d37a3d843d13b6b5ed vivek-dodia <vivek.dodia@icloud.com> 1738605786 -0500	clone: from https://github.com/M0r13n/mikrotik_monitoring.git


File: /.git\logs\refs\heads\main
0000000000000000000000000000000000000000 b9e0bd8681efc01495dd75d37a3d843d13b6b5ed vivek-dodia <vivek.dodia@icloud.com> 1738605786 -0500	clone: from https://github.com/M0r13n/mikrotik_monitoring.git


File: /.git\logs\refs\remotes\origin\HEAD
0000000000000000000000000000000000000000 b9e0bd8681efc01495dd75d37a3d843d13b6b5ed vivek-dodia <vivek.dodia@icloud.com> 1738605786 -0500	clone: from https://github.com/M0r13n/mikrotik_monitoring.git


File: /.git\packed-refs
# pack-refs with: peeled fully-peeled sorted 
3d3e37cc45196bc250d7984ca12053655502f1ce refs/remotes/origin/adds-python-exporter-metrics
b9e0bd8681efc01495dd75d37a3d843d13b6b5ed refs/remotes/origin/main
915cbba8359eabb54d9aa8200e775a979f1e982e refs/remotes/origin/quality-of-life
4cefd2b7b2353c565bdc6dda14a3b18b892d794e refs/remotes/origin/repeating-interface-graphs
e2e8265aab7b4d206f70435565d42dd08dc1eb43 refs/remotes/origin/update-model-with-ipv6-firewall
379ca19bfbb86fa3375c2c3ff4c2a11aac8162c2 refs/remotes/origin/updates
a8fb62411145be6eca6b648ef28c1ea719b64421 refs/remotes/origin/use-blackbox-exporter


File: /.git\refs\heads\main
b9e0bd8681efc01495dd75d37a3d843d13b6b5ed


File: /.git\refs\remotes\origin\HEAD
ref: refs/remotes/origin/main


File: /.gitignore
tmp
File: /.vscode\settings.json
{
    "cSpell.words": [
        "grafana",
        "mikrotik"
    ]
}

File: /blackbox\blackbox.yml
modules:
  icmp_ttl5:
    prober: icmp
    timeout: 5s
    icmp:
      ttl: 10


File: /docker-armor

#include <tunables/global>


profile docker-nginx flags=(attach_disconnected,mediate_deleted) {
  #include <abstractions/base>

  # allow basic network services
  network inet tcp,
  network inet udp,
  network inet icmp,

  # block raw sockets
  deny network raw,
  deny network packet,

  file,
  umount,

  # make paths read only <=> deny write/link permission
  deny /bin/** wl,
  deny /boot/** wl,
  deny /dev/** wl,
  deny /etc/** wl,
  deny /home/** wl,
  deny /lib/** wl,
  deny /lib64/** wl,
  deny /media/** wl,
  deny /mnt/** wl,
  deny /opt/** wl,
  deny /proc/** wl,
  deny /root/** wl,
  deny /sbin/** wl,
  deny /srv/** wl,
  deny /tmp/** wl,
  deny /sys/** wl,
  deny /usr/** wl,
  
  # allowed process(es)
  /usr/sbin/nginx ix,

  # allowed capabilities
  capability chown,
  capability dac_override,
  capability setuid,
  capability setgid,
  capability net_bind_service,

  # Default docker stuff
  deny @{PROC}/* w,   # deny write for all files directly in /proc (not in a subdir)
  deny @{PROC}/{[^1-9],[^1-9][^0-9],[^1-9s][^0-9y][^0-9s],[^1-9][^0-9][^0-9][^0-9]*}/** w,
  deny @{PROC}/sys/[^k]** w,  # deny /proc/sys except /proc/sys/k* (effectively /proc/sys/kernel)
  deny @{PROC}/sys/kernel/{?,??,[^s][^h][^m]**} w,  # deny everything except shm* in /proc/sys/kernel/
  deny @{PROC}/sysrq-trigger rwklx,
  deny @{PROC}/mem rwklx,
  deny @{PROC}/kmem rwklx,
  deny @{PROC}/kcore rwklx,
  deny mount,
  deny /sys/[^f]*/** wklx,
  deny /sys/f[^s]*/** wklx,
  deny /sys/fs/[^c]*/** wklx,
  deny /sys/fs/c[^g]*/** wklx,
  deny /sys/fs/cg[^r]*/** wklx,
  deny /sys/firmware/efi/efivars/** rwklx,
  deny /sys/kernel/security/** rwklx,
}

profile docker-mikrotik-monitoring flags=(attach_disconnected,mediate_deleted) {
  #include <abstractions/base>

  # allow basic network services
  network inet tcp,
  network inet udp,

  # block raw sockets
  deny network raw,
  deny network packet,

  file,
  umount,

  /tmp/** wl,

  # make paths read only <=> deny write/link permission
  deny /bin/** wl,
  deny /boot/** wl,
  deny /dev/[^shm]** wl,
  deny /etc/** wl,
  deny /home/** wl,
  deny /lib/** wl,
  deny /lib64/** wl,
  deny /media/** wl,
  deny /mnt/** wl,
  deny /opt/** wl,
  deny /proc/** wl,
  deny /root/** wl,
  deny /sbin/** wl,
  deny /srv/** wl,
  deny /sys/** wl,
  deny /usr/** wl,
  
  # Default docker stuff
  deny @{PROC}/* w,   # deny write for all files directly in /proc (not in a subdir)
  deny @{PROC}/{[^1-9],[^1-9][^0-9],[^1-9s][^0-9y][^0-9s],[^1-9][^0-9][^0-9][^0-9]*}/** w,
  deny @{PROC}/sys/[^k]** w,  # deny /proc/sys except /proc/sys/k* (effectively /proc/sys/kernel)
  deny @{PROC}/sys/kernel/{?,??,[^s][^h][^m]**} w,  # deny everything except shm* in /proc/sys/kernel/
  deny @{PROC}/sysrq-trigger rwklx,
  deny @{PROC}/mem rwklx,
  deny @{PROC}/kmem rwklx,
  deny @{PROC}/kcore rwklx,
  deny mount,
  deny /sys/[^f]*/** wklx,
  deny /sys/f[^s]*/** wklx,
  deny /sys/fs/[^c]*/** wklx,
  deny /sys/fs/c[^g]*/** wklx,
  deny /sys/fs/cg[^r]*/** wklx,
  deny /sys/firmware/efi/efivars/** rwklx,
  deny /sys/kernel/security/** rwklx,
}


File: /docker-compose-armored.yml
version: "3.9"

volumes:
    prometheus_data: {}
    grafana_data: {}

services:
  # Prometheus
  # https://github.com/stefanprodan/dockprom
  prometheus:
    image: prom/prometheus:v2.42.0
    container_name: prometheus
    security_opt:
      - apparmor:docker-mikrotik-monitoring
    volumes:
      - ./prometheus:/etc/prometheus
      - prometheus_data:/prometheus
    command:
      - '--config.file=/etc/prometheus/prometheus.yml'
      - '--storage.tsdb.path=/prometheus'
    restart: unless-stopped
    networks:
      - default
    labels:
      org.label-schema.group: "monitoring"

  # Grafana
  # https://github.com/stefanprodan/dockprom
  grafana:
    image: grafana/grafana:9.3.6
    security_opt:
      - apparmor:docker-mikrotik-monitoring
    container_name: grafana
    volumes:
      - grafana_data:/var/lib/grafana
      - ./grafana/provisioning/dashboards:/etc/grafana/provisioning/dashboards:ro
      - ./grafana/provisioning/datasources:/etc/grafana/provisioning/datasources:ro
    environment:
      - GF_SECURITY_ADMIN_USER=${ADMIN_USER:-admin}
      - GF_SECURITY_ADMIN_PASSWORD=${ADMIN_PASSWORD:-admin}
      - GF_USERS_ALLOW_SIGN_UP=false
      - GF_INSTALL_PLUGINS=flant-statusmap-panel
      - GF_DASHBOARDS_DEFAULT_HOME_DASHBOARD_PATH=/etc/grafana/provisioning/dashboards/mikrotik/monitor.json
    restart: unless-stopped
    networks:
      - default
    labels:
      org.label-schema.group: "monitoring"

  # MKTXP
  # https://github.com/akpw/mktxp
  mktxp:
    image: ghcr.io/akpw/mktxp:gha-4093170275
    security_opt:
      - apparmor:docker-mikrotik-monitoring
    volumes:
      # Since Version v0.37 mktxp runs as single user
      # Prior it was root
      - './mktxp/:/home/mktxp/mktxp/'
    networks:
      - default
    restart: unless-stopped

  nginx:
    image: nginx:latest
    container_name: nginx
    security_opt:
      - apparmor:docker-nginx
    volumes:
      - ./nginx/nginx.conf:/etc/nginx/conf.d/default.conf
      - ./nginx/nginx-selfsigned.key:/etc/nginx/ssl/nginx-selfsigned.key
      - ./nginx/nginx-selfsigned.crt:/etc/nginx/ssl/nginx-selfsigned.crt
      - ./nginx/self-signed.conf:/etc/nginx/ssl/self-signed.conf
    ports:
      - 80:80  # You may adjust to some unprivileged ports
      - 443:443
    networks:
      - default
    restart: unless-stopped

  blackbox:
    image: quay.io/prometheus/blackbox-exporter:latest
    container_name: mikrotik-blackbox-exporter
    command: --config.file=/config/blackbox.yml
    volumes:
      - ./blackbox/blackbox.yml:/config/blackbox.yml
    networks:
      - default
    restart: unless-stopped
    security_opt:
      - apparmor:docker-mikrotik-monitoring


File: /docker-compose.yml
version: "3.9"

volumes:
  prometheus_data: {}
  grafana_data: {}

services:
  # Prometheus
  # https://github.com/stefanprodan/dockprom
  prometheus:
    image: prom/prometheus:v2.54.1
    container_name: mikrotik-prometheus
    volumes:
      - ./prometheus:/etc/prometheus
      - prometheus_data:/prometheus
    command:
      - "--config.file=/etc/prometheus/prometheus.yml"
      - "--storage.tsdb.path=/prometheus"
      - "--storage.tsdb.retention.time=1y" # <= adjust the storage retention period of Prometheus
    restart: unless-stopped
    networks:
      - default
    labels:
      org.label-schema.group: "monitoring"

  # Grafana
  # https://github.com/stefanprodan/dockprom
  grafana:
    image: grafana/grafana:11.2.0
    container_name: mikrotik-grafana
    volumes:
      - grafana_data:/var/lib/grafana
      - ./grafana/provisioning/dashboards:/etc/grafana/provisioning/dashboards:ro
      - ./grafana/provisioning/datasources:/etc/grafana/provisioning/datasources:ro
    environment:
      - GF_SECURITY_ADMIN_USER=${ADMIN_USER:-admin}
      - GF_SECURITY_ADMIN_PASSWORD=${ADMIN_PASSWORD:-admin}
      - GF_USERS_ALLOW_SIGN_UP=false
      - GF_INSTALL_PLUGINS=flant-statusmap-panel
      - GF_DASHBOARDS_DEFAULT_HOME_DASHBOARD_PATH=/etc/grafana/provisioning/dashboards/mikrotik/monitor.json
    restart: unless-stopped
    networks:
      - default
    labels:
      org.label-schema.group: "monitoring"

  # MKTXP
  # https://github.com/akpw/mktxp
  mktxp:
    image: ghcr.io/akpw/mktxp:gha-10485178964
    container_name: mikrotik-mktxp
    volumes:
      # Since Version v0.37 mktxp runs as single user
      # Prior it was root
      - "./mktxp/:/home/mktxp/mktxp/"
    networks:
      - default
    restart: unless-stopped

  nginx:
    image: nginx:latest
    container_name: mikrotik-nginx
    volumes:
      - ./nginx/nginx.conf:/etc/nginx/conf.d/default.conf
      - ./nginx/nginx-selfsigned.key:/etc/nginx/ssl/nginx-selfsigned.key
      - ./nginx/nginx-selfsigned.crt:/etc/nginx/ssl/nginx-selfsigned.crt
      - ./nginx/self-signed.conf:/etc/nginx/ssl/self-signed.conf
    ports:
      - 80:80 # You may adjust to some unprivileged ports
      - 443:443
    networks:
      - default
    restart: unless-stopped

  # https://github.com/prometheus/blackbox_exporter/blob/master/example.yml
  blackbox:
    image: quay.io/prometheus/blackbox-exporter:latest
    container_name: mikrotik-blackbox-exporter
    command: --config.file=/config/blackbox.yml
    volumes:
      - ./blackbox/blackbox.yml:/config/blackbox.yml
    networks:
      - default
    restart: unless-stopped


File: /grafana\provisioning\dashboards\dashboard.yml

apiVersion: 1

providers:
  - name: 'Prometheus'
    orgId: 1
    folder: 'Mikrotik Monitoring'
    type: file
    disableDeletion: true
    editable: true
    allowUiUpdates: true
    options:
      path: /etc/grafana/provisioning/dashboards/mikrotik


File: /grafana\provisioning\dashboards\mikrotik\monitor.json
{
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
  "description": "Mikrotik MKTXP Exporter metrics",
  "editable": true,
  "fiscalYearStartMonth": 0,
  "gnetId": 13679,
  "graphTooltip": 0,
  "id": 2,
  "links": [],
  "liveNow": false,
  "panels": [
    {
      "collapsed": false,
      "datasource": {
        "type": "prometheus"
      },
      "gridPos": {
        "h": 1,
        "w": 24,
        "x": 0,
        "y": 0
      },
      "id": 10,
      "panels": [],
      "targets": [
        {
          "datasource": {
            "type": "prometheus"
          },
          "refId": "A"
        }
      ],
      "title": "System",
      "type": "row"
    },
    {
      "datasource": {
        "type": "prometheus"
      },
      "description": "",
      "fieldConfig": {
        "defaults": {
          "color": {
            "fixedColor": "green",
            "mode": "fixed"
          },
          "mappings": [
            {
              "options": {
                "result": {
                  "text": "N/A"
                }
              },
              "type": "special"
            }
          ],
          "thresholds": {
            "mode": "absolute",
            "steps": [
              {
                "color": "green",
                "value": null
              }
            ]
          },
          "unit": "none"
        },
        "overrides": []
      },
      "gridPos": {
        "h": 2,
        "w": 3,
        "x": 0,
        "y": 1
      },
      "id": 72,
      "maxDataPoints": 100,
      "options": {
        "colorMode": "value",
        "graphMode": "none",
        "justifyMode": "center",
        "orientation": "auto",
        "percentChangeColorMode": "standard",
        "reduceOptions": {
          "calcs": ["lastNotNull"],
          "fields": "",
          "values": false
        },
        "showPercentChange": false,
        "text": {},
        "textMode": "name",
        "wideLayout": true
      },
      "pluginVersion": "11.2.0",
      "targets": [
        {
          "datasource": {
            "type": "prometheus"
          },
          "expr": "mktxp_system_identity_info{routerboard_address=\"$node\"}",
          "instant": true,
          "interval": "",
          "legendFormat": "{{name}}",
          "refId": "B"
        }
      ],
      "title": "Identity",
      "type": "stat"
    },
    {
      "datasource": {
        "type": "prometheus"
      },
      "description": "Public IP address of the networking device.",
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
                "color": "green",
                "value": null
              },
              {
                "color": "red",
                "value": 80
              }
            ]
          }
        },
        "overrides": []
      },
      "gridPos": {
        "h": 2,
        "w": 3,
        "x": 3,
        "y": 1
      },
      "id": 96,
      "options": {
        "colorMode": "value",
        "graphMode": "none",
        "justifyMode": "auto",
        "orientation": "auto",
        "percentChangeColorMode": "standard",
        "reduceOptions": {
          "calcs": ["lastNotNull"],
          "fields": "",
          "values": false
        },
        "showPercentChange": false,
        "textMode": "name",
        "wideLayout": true
      },
      "pluginVersion": "11.2.0",
      "targets": [
        {
          "datasource": {
            "type": "prometheus"
          },
          "editorMode": "code",
          "expr": "mktxp_public_ip_address_info{routerboard_address=\"$node\"}",
          "legendFormat": "{{public_address}}",
          "range": true,
          "refId": "A"
        }
      ],
      "title": "Public IP",
      "type": "stat"
    },
    {
      "datasource": {
        "type": "prometheus"
      },
      "description": "",
      "fieldConfig": {
        "defaults": {
          "color": {
            "fixedColor": "green",
            "mode": "fixed"
          },
          "mappings": [
            {
              "options": {
                "result": {
                  "text": "N/A"
                }
              },
              "type": "special"
            }
          ],
          "thresholds": {
            "mode": "absolute",
            "steps": [
              {
                "color": "green",
                "value": null
              }
            ]
          },
          "unit": "none"
        },
        "overrides": []
      },
      "gridPos": {
        "h": 2,
        "w": 3,
        "x": 6,
        "y": 1
      },
      "id": 6,
      "maxDataPoints": 100,
      "options": {
        "colorMode": "value",
        "graphMode": "none",
        "justifyMode": "center",
        "orientation": "auto",
        "percentChangeColorMode": "standard",
        "reduceOptions": {
          "calcs": ["lastNotNull"],
          "fields": "",
          "values": false
        },
        "showPercentChange": false,
        "text": {},
        "textMode": "name",
        "wideLayout": true
      },
      "pluginVersion": "11.2.0",
      "targets": [
        {
          "datasource": {
            "type": "prometheus"
          },
          "expr": "mktxp_system_uptime{routerboard_address=\"$node\"}",
          "instant": true,
          "interval": "",
          "legendFormat": "{{board_name}}",
          "refId": "B"
        }
      ],
      "title": "Routerboard HW",
      "type": "stat"
    },
    {
      "datasource": {
        "type": "prometheus"
      },
      "fieldConfig": {
        "defaults": {
          "color": {
            "fixedColor": "green",
            "mode": "fixed"
          },
          "mappings": [
            {
              "options": {
                "result": {
                  "text": "N/A"
                }
              },
              "type": "special"
            }
          ],
          "thresholds": {
            "mode": "absolute",
            "steps": [
              {
                "color": "green",
                "value": null
              }
            ]
          },
          "unit": "dtdurations"
        },
        "overrides": []
      },
      "gridPos": {
        "h": 2,
        "w": 3,
        "x": 9,
        "y": 1
      },
      "id": 12,
      "maxDataPoints": 100,
      "options": {
        "colorMode": "value",
        "graphMode": "none",
        "justifyMode": "auto",
        "orientation": "auto",
        "percentChangeColorMode": "standard",
        "reduceOptions": {
          "calcs": ["lastNotNull"],
          "fields": "",
          "values": false
        },
        "showPercentChange": false,
        "text": {},
        "textMode": "auto",
        "wideLayout": true
      },
      "pluginVersion": "11.2.0",
      "targets": [
        {
          "application": {
            "filter": "General"
          },
          "datasource": {
            "type": "prometheus"
          },
          "expr": "mktxp_system_uptime{routerboard_address=\"$node\"}",
          "format": "time_series",
          "functions": [],
          "group": {
            "filter": "Network"
          },
          "hide": false,
          "host": {
            "filter": "MikroTik Router"
          },
          "instant": true,
          "interval": "",
          "intervalFactor": 1,
          "item": {
            "filter": "System uptime"
          },
          "legendFormat": "",
          "mode": 0,
          "options": {
            "showDisabledItems": false
          },
          "refId": "A"
        }
      ],
      "title": "System uptime",
      "type": "stat"
    },
    {
      "datasource": {
        "type": "prometheus"
      },
      "fieldConfig": {
        "defaults": {
          "color": {
            "fixedColor": "green",
            "mode": "fixed"
          },
          "mappings": [
            {
              "options": {
                "result": {
                  "text": "N/A"
                }
              },
              "type": "special"
            }
          ],
          "thresholds": {
            "mode": "absolute",
            "steps": [
              {
                "color": "green",
                "value": null
              }
            ]
          },
          "unit": "none"
        },
        "overrides": []
      },
      "gridPos": {
        "h": 2,
        "w": 3,
        "x": 12,
        "y": 1
      },
      "id": 8,
      "maxDataPoints": 100,
      "options": {
        "colorMode": "value",
        "graphMode": "none",
        "justifyMode": "center",
        "orientation": "auto",
        "percentChangeColorMode": "standard",
        "reduceOptions": {
          "calcs": ["lastNotNull"],
          "fields": "",
          "values": false
        },
        "showPercentChange": false,
        "text": {},
        "textMode": "name",
        "wideLayout": true
      },
      "pluginVersion": "11.2.0",
      "targets": [
        {
          "application": {
            "filter": "General"
          },
          "datasource": {
            "type": "prometheus"
          },
          "expr": "mktxp_system_uptime{routerboard_address=\"$node\"}",
          "format": "time_series",
          "functions": [],
          "group": {
            "filter": "Network"
          },
          "hide": false,
          "host": {
            "filter": "MikroTik Router"
          },
          "instant": true,
          "interval": "",
          "intervalFactor": 1,
          "item": {
            "filter": "System version and hw"
          },
          "legendFormat": "{{version}} ",
          "mode": 2,
          "options": {
            "showDisabledItems": false
          },
          "refId": "A"
        }
      ],
      "title": "System version",
      "type": "stat"
    },
    {
      "datasource": {
        "type": "prometheus",
        "uid": "PBFA97CFB590B2093"
      },
      "description": "The newest available version",
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
                "color": "green",
                "value": null
              },
              {
                "color": "orange",
                "value": 1
              }
            ]
          }
        },
        "overrides": []
      },
      "gridPos": {
        "h": 2,
        "w": 3,
        "x": 15,
        "y": 1
      },
      "id": 137,
      "options": {
        "colorMode": "value",
        "graphMode": "area",
        "justifyMode": "auto",
        "orientation": "auto",
        "percentChangeColorMode": "standard",
        "reduceOptions": {
          "calcs": ["lastNotNull"],
          "fields": "",
          "values": true
        },
        "showPercentChange": false,
        "textMode": "name",
        "wideLayout": true
      },
      "pluginVersion": "11.2.0",
      "targets": [
        {
          "datasource": {
            "type": "prometheus",
            "uid": "PBFA97CFB590B2093"
          },
          "editorMode": "code",
          "exemplar": false,
          "expr": "mktxp_system_update_available{routerboard_address=\"$node\"}",
          "instant": true,
          "legendFormat": "{{newest_version}}",
          "range": false,
          "refId": "A"
        }
      ],
      "title": "Newest Version",
      "type": "stat"
    },
    {
      "datasource": {
        "type": "prometheus"
      },
      "description": "",
      "fieldConfig": {
        "defaults": {
          "color": {
            "fixedColor": "green",
            "mode": "fixed"
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
          "unit": "volt"
        },
        "overrides": []
      },
      "gridPos": {
        "h": 2,
        "w": 3,
        "x": 18,
        "y": 1
      },
      "id": 57,
      "maxDataPoints": 100,
      "options": {
        "colorMode": "value",
        "graphMode": "none",
        "justifyMode": "center",
        "orientation": "horizontal",
        "percentChangeColorMode": "standard",
        "reduceOptions": {
          "calcs": ["lastNotNull"],
          "fields": "",
          "values": false
        },
        "showPercentChange": false,
        "text": {},
        "textMode": "value",
        "wideLayout": true
      },
      "pluginVersion": "11.2.0",
      "targets": [
        {
          "application": {
            "filter": "General"
          },
          "datasource": {
            "type": "prometheus"
          },
          "expr": "mktxp_system_routerboard_voltage{routerboard_address=\"$node\"}",
          "format": "time_series",
          "functions": [],
          "group": {
            "filter": "Network"
          },
          "hide": false,
          "host": {
            "filter": "MikroTik Router"
          },
          "instant": true,
          "interval": "",
          "intervalFactor": 1,
          "item": {
            "filter": "System version and hw"
          },
          "legendFormat": "",
          "mode": 2,
          "options": {
            "showDisabledItems": false
          },
          "refId": "A"
        }
      ],
      "title": "Voltage",
      "type": "stat"
    },
    {
      "datasource": {
        "type": "prometheus",
        "uid": "PBFA97CFB590B2093"
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
                "color": "green",
                "value": null
              },
              {
                "color": "red",
                "value": 80
              }
            ]
          }
        },
        "overrides": []
      },
      "gridPos": {
        "h": 2,
        "w": 3,
        "x": 21,
        "y": 1
      },
      "id": 139,
      "options": {
        "colorMode": "value",
        "graphMode": "area",
        "justifyMode": "auto",
        "orientation": "auto",
        "percentChangeColorMode": "standard",
        "reduceOptions": {
          "calcs": ["lastNotNull"],
          "fields": "",
          "values": false
        },
        "showPercentChange": false,
        "textMode": "auto",
        "wideLayout": true
      },
      "pluginVersion": "11.2.0",
      "targets": [
        {
          "datasource": {
            "type": "prometheus",
            "uid": "PBFA97CFB590B2093"
          },
          "editorMode": "code",
          "exemplar": false,
          "expr": "mktxp_active_users_info{routerboard_address=\"$node\"}",
          "format": "table",
          "instant": true,
          "legendFormat": "__auto",
          "range": false,
          "refId": "A"
        }
      ],
      "title": "Active Users",
      "type": "stat"
    },
    {
      "datasource": {
        "type": "prometheus"
      },
      "fieldConfig": {
        "defaults": {
          "decimals": 1,
          "mappings": [
            {
              "options": {
                "result": {
                  "text": "N/A"
                }
              },
              "type": "special"
            }
          ],
          "max": 100,
          "min": 0.1,
          "thresholds": {
            "mode": "absolute",
            "steps": [
              {
                "color": "rgba(50, 172, 45, 0.97)",
                "value": null
              },
              {
                "color": "rgba(237, 129, 40, 0.89)",
                "value": 70
              },
              {
                "color": "rgba(245, 54, 54, 0.9)",
                "value": 90
              }
            ]
          },
          "unit": "percent"
        },
        "overrides": []
      },
      "gridPos": {
        "h": 6,
        "w": 4,
        "x": 0,
        "y": 3
      },
      "id": 14,
      "maxDataPoints": 100,
      "options": {
        "displayMode": "lcd",
        "maxVizHeight": 300,
        "minVizHeight": 10,
        "minVizWidth": 0,
        "namePlacement": "auto",
        "orientation": "horizontal",
        "reduceOptions": {
          "calcs": ["mean"],
          "fields": "",
          "values": false
        },
        "showUnfilled": true,
        "sizing": "auto",
        "text": {},
        "valueMode": "color"
      },
      "pluginVersion": "11.2.0",
      "targets": [
        {
          "application": {
            "filter": "Memory"
          },
          "datasource": {
            "type": "prometheus"
          },
          "expr": "(1 - mktxp_system_free_memory{routerboard_address=\"$node\"} / mktxp_system_total_memory{routerboard_address=\"$node\"})*100",
          "format": "time_series",
          "functions": [],
          "group": {
            "filter": "Network"
          },
          "hide": false,
          "host": {
            "filter": "MikroTik Router"
          },
          "instant": true,
          "interval": "",
          "intervalFactor": 1,
          "item": {
            "filter": "Used memory"
          },
          "legendFormat": "Used RAM Memory",
          "mode": 0,
          "options": {
            "showDisabledItems": false
          },
          "refId": "A"
        },
        {
          "datasource": {
            "type": "prometheus"
          },
          "expr": "mktxp_system_cpu_load{routerboard_address=\"$node\"}",
          "instant": true,
          "interval": "",
          "legendFormat": "CPU Load",
          "refId": "C"
        },
        {
          "datasource": {
            "type": "prometheus"
          },
          "expr": "(1 - mktxp_system_free_hdd_space{routerboard_address=\"$node\"} / mktxp_system_total_hdd_space{routerboard_address=\"$node\"})*100",
          "instant": true,
          "interval": "",
          "legendFormat": "HDD Utilization",
          "refId": "B"
        }
      ],
      "type": "bargauge"
    },
    {
      "datasource": {
        "type": "prometheus",
        "uid": "PBFA97CFB590B2093"
      },
      "fieldConfig": {
        "defaults": {
          "mappings": [],
          "max": 100,
          "min": 0,
          "thresholds": {
            "mode": "absolute",
            "steps": [
              {
                "color": "green",
                "value": null
              },
              {
                "color": "green",
                "value": 30
              },
              {
                "color": "yellow",
                "value": 40
              },
              {
                "color": "orange",
                "value": 60
              },
              {
                "color": "red",
                "value": 70
              }
            ]
          },
          "unit": "celsius"
        },
        "overrides": []
      },
      "gridPos": {
        "h": 6,
        "w": 4,
        "x": 4,
        "y": 3
      },
      "id": 59,
      "options": {
        "minVizHeight": 75,
        "minVizWidth": 75,
        "orientation": "auto",
        "reduceOptions": {
          "calcs": ["mean"],
          "fields": "",
          "values": false
        },
        "showThresholdLabels": false,
        "showThresholdMarkers": true,
        "sizing": "auto",
        "text": {}
      },
      "pluginVersion": "11.2.0",
      "targets": [
        {
          "datasource": {
            "type": "prometheus"
          },
          "expr": "mktxp_system_routerboard_temperature{routerboard_address=\"$node\"} or mktxp_system_cpu_temperature{routerboard_address=\"$node\"}",
          "instant": true,
          "interval": "",
          "legendFormat": "",
          "refId": "A"
        }
      ],
      "title": "Temperature",
      "type": "gauge"
    },
    {
      "datasource": {
        "type": "prometheus",
        "uid": "PBFA97CFB590B2093"
      },
      "fieldConfig": {
        "defaults": {
          "color": {
            "fixedColor": "semi-dark-green",
            "mode": "fixed"
          },
          "mappings": [],
          "thresholds": {
            "mode": "absolute",
            "steps": [
              {
                "color": "green",
                "value": null
              },
              {
                "color": "semi-dark-green",
                "value": ""
              },
              {
                "color": "dark-green",
                "value": ""
              }
            ]
          },
          "unit": "bps"
        },
        "overrides": []
      },
      "gridPos": {
        "h": 6,
        "w": 4,
        "x": 8,
        "y": 3
      },
      "id": 141,
      "options": {
        "minVizHeight": 75,
        "minVizWidth": 85,
        "orientation": "auto",
        "reduceOptions": {
          "calcs": ["lastNotNull"],
          "fields": "",
          "values": false
        },
        "showThresholdLabels": false,
        "showThresholdMarkers": false,
        "sizing": "auto"
      },
      "pluginVersion": "11.2.0",
      "targets": [
        {
          "datasource": {
            "type": "prometheus",
            "uid": "PBFA97CFB590B2093"
          },
          "editorMode": "code",
          "exemplar": false,
          "expr": "sum(rate(mktxp_interface_rx_byte_total{routerboard_address=\"$node\"}[$__rate_interval]) * 8)",
          "instant": false,
          "legendFormat": "{{name}}",
          "range": true,
          "refId": "A"
        }
      ],
      "title": "Total Network Inbound",
      "type": "gauge"
    },
    {
      "datasource": {
        "type": "prometheus",
        "uid": "PBFA97CFB590B2093"
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
                "color": "orange",
                "value": null
              }
            ]
          },
          "unit": "bps"
        },
        "overrides": []
      },
      "gridPos": {
        "h": 6,
        "w": 4,
        "x": 12,
        "y": 3
      },
      "id": 142,
      "options": {
        "minVizHeight": 75,
        "minVizWidth": 75,
        "orientation": "auto",
        "reduceOptions": {
          "calcs": ["lastNotNull"],
          "fields": "",
          "values": false
        },
        "showThresholdLabels": false,
        "showThresholdMarkers": false,
        "sizing": "auto"
      },
      "pluginVersion": "11.2.0",
      "targets": [
        {
          "datasource": {
            "type": "prometheus",
            "uid": "PBFA97CFB590B2093"
          },
          "editorMode": "code",
          "exemplar": false,
          "expr": "sum(rate(mktxp_interface_tx_byte_total{routerboard_address=\"$node\"}[$__rate_interval]) * 8)",
          "instant": false,
          "legendFormat": "__auto",
          "range": true,
          "refId": "A"
        }
      ],
      "title": "Total Network Outbound",
      "type": "gauge"
    },
    {
      "datasource": {
        "type": "prometheus",
        "uid": "PBFA97CFB590B2093"
      },
      "fieldConfig": {
        "defaults": {
          "color": {
            "fixedColor": "blue",
            "mode": "shades"
          },
          "mappings": [],
          "thresholds": {
            "mode": "absolute",
            "steps": [
              {
                "color": "green",
                "value": null
              },
              {
                "color": "red",
                "value": 80
              }
            ]
          },
          "unit": "decbytes"
        },
        "overrides": []
      },
      "gridPos": {
        "h": 6,
        "w": 8,
        "x": 16,
        "y": 3
      },
      "id": 140,
      "options": {
        "displayMode": "lcd",
        "maxVizHeight": 300,
        "minVizHeight": 16,
        "minVizWidth": 8,
        "namePlacement": "auto",
        "orientation": "horizontal",
        "reduceOptions": {
          "calcs": ["lastNotNull"],
          "fields": "",
          "values": false
        },
        "showUnfilled": true,
        "sizing": "auto",
        "valueMode": "color"
      },
      "pluginVersion": "11.2.0",
      "targets": [
        {
          "datasource": {
            "type": "prometheus",
            "uid": "PBFA97CFB590B2093"
          },
          "editorMode": "code",
          "exemplar": false,
          "expr": " sort_desc(mktxp_interface_rx_byte_total{routerboard_address=\"$node\"})",
          "instant": true,
          "legendFormat": "{{name}}",
          "range": false,
          "refId": "A"
        }
      ],
      "title": "Rx Bytes Total",
      "type": "bargauge"
    },
    {
      "datasource": {
        "type": "prometheus"
      },
      "fieldConfig": {
        "defaults": {
          "color": {
            "mode": "palette-classic"
          },
          "custom": {
            "axisBorderShow": false,
            "axisCenteredZero": false,
            "axisColorMode": "text",
            "axisLabel": "",
            "axisPlacement": "auto",
            "barAlignment": 0,
            "barWidthFactor": 0.6,
            "drawStyle": "line",
            "fillOpacity": 50,
            "gradientMode": "none",
            "hideFrom": {
              "legend": false,
              "tooltip": false,
              "viz": false
            },
            "insertNulls": false,
            "lineInterpolation": "linear",
            "lineWidth": 1,
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
              "mode": "off"
            }
          },
          "links": [],
          "mappings": [],
          "min": 0,
          "thresholds": {
            "mode": "absolute",
            "steps": [
              {
                "color": "green",
                "value": null
              },
              {
                "color": "red",
                "value": 80
              }
            ]
          },
          "unit": "decbytes"
        },
        "overrides": [
          {
            "matcher": {
              "id": "byName",
              "options": "Total memory"
            },
            "properties": [
              {
                "id": "color",
                "value": {
                  "fixedColor": "#E24D42",
                  "mode": "fixed"
                }
              }
            ]
          },
          {
            "matcher": {
              "id": "byName",
              "options": "Used memory"
            },
            "properties": [
              {
                "id": "color",
                "value": {
                  "fixedColor": "#1F78C1",
                  "mode": "fixed"
                }
              }
            ]
          },
          {
            "matcher": {
              "id": "byName",
              "options": "Total memory"
            },
            "properties": [
              {
                "id": "color",
                "value": {
                  "fixedColor": "#E24D42",
                  "mode": "fixed"
                }
              },
              {
                "id": "custom.fillOpacity",
                "value": 20
              },
              {
                "id": "custom.lineWidth",
                "value": 0
              }
            ]
          },
          {
            "matcher": {
              "id": "byName",
              "options": "Used memory"
            },
            "properties": [
              {
                "id": "color",
                "value": {
                  "fixedColor": "#1F78C1",
                  "mode": "fixed"
                }
              }
            ]
          }
        ]
      },
      "gridPos": {
        "h": 8,
        "w": 12,
        "x": 0,
        "y": 9
      },
      "id": 18,
      "options": {
        "legend": {
          "calcs": ["mean", "lastNotNull", "max", "min"],
          "displayMode": "table",
          "placement": "bottom",
          "showLegend": true
        },
        "tooltip": {
          "mode": "multi",
          "sort": "none"
        }
      },
      "pluginVersion": "10.3.1",
      "targets": [
        {
          "application": {
            "filter": "Memory"
          },
          "datasource": {
            "type": "prometheus"
          },
          "expr": "mktxp_system_total_hdd_space{routerboard_address=\"$node\"} - mktxp_system_free_hdd_space{routerboard_address=\"$node\"}",
          "format": "time_series",
          "functions": [],
          "group": {
            "filter": "Network"
          },
          "host": {
            "filter": "MikroTik Router"
          },
          "instant": false,
          "interval": "",
          "intervalFactor": 1,
          "item": {
            "filter": "Used memory"
          },
          "legendFormat": "Used memory",
          "mode": 0,
          "options": {
            "showDisabledItems": false
          },
          "refId": "A"
        },
        {
          "application": {
            "filter": "Memory"
          },
          "datasource": {
            "type": "prometheus"
          },
          "expr": "mktxp_system_total_hdd_space{routerboard_address=\"$node\"}",
          "format": "time_series",
          "functions": [],
          "group": {
            "filter": "Network"
          },
          "host": {
            "filter": "MikroTik Router"
          },
          "instant": false,
          "interval": "",
          "intervalFactor": 1,
          "item": {
            "filter": "Total memory"
          },
          "legendFormat": "Total memory",
          "mode": 0,
          "options": {
            "showDisabledItems": false
          },
          "refId": "B"
        }
      ],
      "title": "HDD Utilization",
      "type": "timeseries"
    },
    {
      "datasource": {
        "type": "prometheus"
      },
      "fieldConfig": {
        "defaults": {
          "color": {
            "mode": "palette-classic"
          },
          "custom": {
            "axisBorderShow": false,
            "axisCenteredZero": false,
            "axisColorMode": "text",
            "axisLabel": "",
            "axisPlacement": "auto",
            "barAlignment": 0,
            "barWidthFactor": 0.6,
            "drawStyle": "line",
            "fillOpacity": 10,
            "gradientMode": "none",
            "hideFrom": {
              "legend": false,
              "tooltip": false,
              "viz": false
            },
            "insertNulls": false,
            "lineInterpolation": "linear",
            "lineWidth": 1,
            "pointSize": 5,
            "scaleDistribution": {
              "log": 10,
              "type": "log"
            },
            "showPoints": "never",
            "spanNulls": true,
            "stacking": {
              "group": "A",
              "mode": "none"
            },
            "thresholdsStyle": {
              "mode": "off"
            }
          },
          "links": [],
          "mappings": [],
          "max": 100,
          "min": 0,
          "thresholds": {
            "mode": "absolute",
            "steps": [
              {
                "color": "green",
                "value": null
              },
              {
                "color": "red",
                "value": 80
              }
            ]
          },
          "unit": "percent"
        },
        "overrides": [
          {
            "matcher": {
              "id": "byName",
              "options": "ARM"
            },
            "properties": [
              {
                "id": "color",
                "value": {
                  "fixedColor": "green",
                  "mode": "fixed"
                }
              }
            ]
          }
        ]
      },
      "gridPos": {
        "h": 8,
        "w": 12,
        "x": 12,
        "y": 9
      },
      "id": 16,
      "options": {
        "legend": {
          "calcs": ["mean", "lastNotNull", "max", "min"],
          "displayMode": "table",
          "placement": "bottom",
          "showLegend": true
        },
        "tooltip": {
          "mode": "multi",
          "sort": "none"
        }
      },
      "pluginVersion": "10.3.1",
      "targets": [
        {
          "application": {
            "filter": "CPU"
          },
          "datasource": {
            "type": "prometheus"
          },
          "exemplar": true,
          "expr": "mktxp_system_cpu_load{routerboard_address=\"$node\"}",
          "format": "time_series",
          "functions": [],
          "group": {
            "filter": "Network"
          },
          "host": {
            "filter": "MikroTik Router"
          },
          "instant": false,
          "interval": "",
          "intervalFactor": 1,
          "item": {
            "filter": "CPU 1 load"
          },
          "legendFormat": "{{cpu}}",
          "mode": 0,
          "options": {
            "showDisabledItems": false
          },
          "refId": "A"
        }
      ],
      "title": "CPU load",
      "type": "timeseries"
    },
    {
      "datasource": {
        "type": "prometheus",
        "uid": "PBFA97CFB590B2093"
      },
      "description": "",
      "fieldConfig": {
        "defaults": {
          "color": {
            "mode": "palette-classic"
          },
          "custom": {
            "axisBorderShow": false,
            "axisCenteredZero": false,
            "axisColorMode": "text",
            "axisLabel": "",
            "axisPlacement": "auto",
            "barAlignment": 0,
            "barWidthFactor": 0.6,
            "drawStyle": "line",
            "fillOpacity": 30,
            "gradientMode": "hue",
            "hideFrom": {
              "legend": false,
              "tooltip": false,
              "viz": false
            },
            "insertNulls": false,
            "lineInterpolation": "smooth",
            "lineWidth": 1,
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
          "links": [],
          "mappings": [],
          "thresholds": {
            "mode": "absolute",
            "steps": [
              {
                "color": "green",
                "value": null
              },
              {
                "color": "red",
                "value": 80
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
        "y": 17
      },
      "id": 75,
      "options": {
        "legend": {
          "calcs": ["min", "max", "mean"],
          "displayMode": "table",
          "placement": "bottom",
          "showLegend": true
        },
        "tooltip": {
          "mode": "single",
          "sort": "none"
        }
      },
      "pluginVersion": "8.0.4",
      "targets": [
        {
          "application": {
            "filter": "Network"
          },
          "datasource": {
            "type": "prometheus"
          },
          "editorMode": "code",
          "exemplar": true,
          "expr": " rate(mktxp_interface_rx_byte_total{routerboard_address=\"$node\"}[$__rate_interval]) * 8 != 0",
          "format": "time_series",
          "functions": [],
          "group": {
            "filter": "Network"
          },
          "hide": false,
          "host": {
            "filter": "MikroTik Router"
          },
          "instant": false,
          "interval": "",
          "intervalFactor": 1,
          "item": {
            "filter": "Incoming traffic on interface ether1-gateway"
          },
          "legendFormat": "In | {{ name }}",
          "mode": 0,
          "options": {
            "showDisabledItems": false
          },
          "refId": "A"
        },
        {
          "application": {
            "filter": "Network"
          },
          "datasource": {
            "type": "prometheus"
          },
          "exemplar": true,
          "expr": "- rate(mktxp_interface_tx_byte_total{routerboard_address=\"$node\"}[$__rate_interval]) * 8 != 0",
          "format": "time_series",
          "functions": [],
          "group": {
            "filter": "Network"
          },
          "hide": false,
          "host": {
            "filter": "MikroTik Router"
          },
          "interval": "",
          "intervalFactor": 1,
          "item": {
            "filter": "Outgoing traffic on interface ether1-gateway"
          },
          "legendFormat": "Out | {{ name }}",
          "mode": 0,
          "options": {
            "showDisabledItems": false
          },
          "refId": "B"
        }
      ],
      "title": "Interface traffic ",
      "type": "timeseries"
    },
    {
      "datasource": {
        "type": "prometheus",
        "uid": "PBFA97CFB590B2093"
      },
      "fieldConfig": {
        "defaults": {
          "color": {
            "mode": "palette-classic"
          },
          "custom": {
            "axisBorderShow": false,
            "axisCenteredZero": false,
            "axisColorMode": "text",
            "axisLabel": "",
            "axisPlacement": "left",
            "barAlignment": 0,
            "barWidthFactor": 0.6,
            "drawStyle": "line",
            "fillOpacity": 100,
            "gradientMode": "opacity",
            "hideFrom": {
              "legend": false,
              "tooltip": false,
              "viz": false
            },
            "insertNulls": false,
            "lineInterpolation": "linear",
            "lineStyle": {
              "fill": "solid"
            },
            "lineWidth": 1,
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
              },
              {
                "color": "red",
                "value": 80
              }
            ]
          },
          "unit": "pps"
        },
        "overrides": []
      },
      "gridPos": {
        "h": 8,
        "w": 12,
        "x": 0,
        "y": 25
      },
      "id": 92,
      "options": {
        "legend": {
          "calcs": [],
          "displayMode": "list",
          "placement": "right",
          "showLegend": true
        },
        "tooltip": {
          "mode": "single",
          "sort": "none"
        }
      },
      "targets": [
        {
          "datasource": {
            "type": "prometheus"
          },
          "exemplar": true,
          "expr": "rate(mktxp_interface_rx_packet_total{routerboard_address=\"$node\"}[$__rate_interval]) != 0",
          "interval": "",
          "legendFormat": "{{ name }}",
          "refId": "A"
        }
      ],
      "title": "Incoming Packets",
      "type": "timeseries"
    },
    {
      "datasource": {
        "type": "prometheus",
        "uid": "PBFA97CFB590B2093"
      },
      "fieldConfig": {
        "defaults": {
          "color": {
            "mode": "palette-classic"
          },
          "custom": {
            "axisBorderShow": false,
            "axisCenteredZero": false,
            "axisColorMode": "text",
            "axisLabel": "",
            "axisPlacement": "auto",
            "barAlignment": 0,
            "barWidthFactor": 0.6,
            "drawStyle": "line",
            "fillOpacity": 100,
            "gradientMode": "opacity",
            "hideFrom": {
              "legend": false,
              "tooltip": false,
              "viz": false
            },
            "insertNulls": false,
            "lineInterpolation": "linear",
            "lineWidth": 1,
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
              },
              {
                "color": "red",
                "value": 80
              }
            ]
          },
          "unit": "pps"
        },
        "overrides": []
      },
      "gridPos": {
        "h": 8,
        "w": 12,
        "x": 12,
        "y": 25
      },
      "id": 94,
      "options": {
        "legend": {
          "calcs": [],
          "displayMode": "list",
          "placement": "right",
          "showLegend": true
        },
        "tooltip": {
          "mode": "single",
          "sort": "none"
        }
      },
      "targets": [
        {
          "datasource": {
            "type": "prometheus"
          },
          "exemplar": true,
          "expr": "rate(mktxp_interface_tx_packet_total{routerboard_address=\"$node\"}[$__rate_interval]) != 0",
          "interval": "",
          "legendFormat": "{{name}}",
          "refId": "A"
        }
      ],
      "title": "Outgoing packets",
      "type": "timeseries"
    },
    {
      "collapsed": true,
      "gridPos": {
        "h": 1,
        "w": 24,
        "x": 0,
        "y": 33
      },
      "id": 131,
      "panels": [
        {
          "datasource": {
            "type": "prometheus",
            "uid": "PBFA97CFB590B2093"
          },
          "fieldConfig": {
            "defaults": {
              "color": {
                "mode": "palette-classic",
                "seriesBy": "last"
              },
              "custom": {
                "axisBorderShow": false,
                "axisCenteredZero": false,
                "axisColorMode": "text",
                "axisLabel": "",
                "axisPlacement": "auto",
                "barAlignment": 0,
                "drawStyle": "bars",
                "fillOpacity": 100,
                "gradientMode": "hue",
                "hideFrom": {
                  "legend": false,
                  "tooltip": false,
                  "viz": false
                },
                "insertNulls": false,
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
                  "mode": "normal"
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
                  },
                  {
                    "color": "red",
                    "value": 80
                  }
                ]
              },
              "unit": "s",
              "unitScale": true
            },
            "overrides": []
          },
          "gridPos": {
            "h": 8,
            "w": 12,
            "x": 0,
            "y": 82
          },
          "id": 129,
          "options": {
            "legend": {
              "calcs": ["min", "max", "mean"],
              "displayMode": "table",
              "placement": "bottom",
              "showLegend": true
            },
            "tooltip": {
              "mode": "single",
              "sort": "none"
            }
          },
          "pluginVersion": "9.3.6",
          "targets": [
            {
              "datasource": {
                "type": "prometheus",
                "uid": "PBFA97CFB590B2093"
              },
              "editorMode": "code",
              "expr": "sum(rate(probe_icmp_duration_seconds{phase=\"rtt\"}[$__rate_interval])) by (instance)\n",
              "format": "time_series",
              "legendFormat": "{{ instance }}",
              "range": true,
              "refId": "A"
            }
          ],
          "title": "Latency (RTT)",
          "type": "timeseries"
        },
        {
          "datasource": {
            "type": "prometheus",
            "uid": "PBFA97CFB590B2093"
          },
          "fieldConfig": {
            "defaults": {
              "color": {
                "mode": "palette-classic"
              },
              "custom": {
                "axisBorderShow": false,
                "axisCenteredZero": false,
                "axisColorMode": "text",
                "axisLabel": "",
                "axisPlacement": "auto",
                "barAlignment": 0,
                "drawStyle": "bars",
                "fillOpacity": 100,
                "gradientMode": "hue",
                "hideFrom": {
                  "legend": false,
                  "tooltip": false,
                  "viz": false
                },
                "insertNulls": false,
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
                  "mode": "normal"
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
                  },
                  {
                    "color": "red",
                    "value": 80
                  }
                ]
              },
              "unit": "s",
              "unitScale": true
            },
            "overrides": []
          },
          "gridPos": {
            "h": 8,
            "w": 12,
            "x": 12,
            "y": 82
          },
          "id": 135,
          "options": {
            "legend": {
              "calcs": [],
              "displayMode": "list",
              "placement": "bottom",
              "showLegend": true
            },
            "tooltip": {
              "mode": "single",
              "sort": "none"
            }
          },
          "targets": [
            {
              "datasource": {
                "type": "prometheus",
                "uid": "PBFA97CFB590B2093"
              },
              "editorMode": "code",
              "expr": "sum(rate(probe_icmp_duration_seconds{phase=\"resolve\"}[$__rate_interval])) by (instance)",
              "instant": false,
              "legendFormat": "{{host}}",
              "range": true,
              "refId": "A"
            }
          ],
          "title": "Latency (DNS resolution)",
          "type": "timeseries"
        },
        {
          "datasource": {
            "type": "prometheus",
            "uid": "PBFA97CFB590B2093"
          },
          "fieldConfig": {
            "defaults": {
              "color": {
                "mode": "palette-classic"
              },
              "custom": {
                "axisBorderShow": false,
                "axisCenteredZero": false,
                "axisColorMode": "text",
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
                "insertNulls": false,
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
                    "color": "green"
                  },
                  {
                    "color": "red",
                    "value": 80
                  }
                ]
              },
              "unit": "percent",
              "unitScale": true
            },
            "overrides": []
          },
          "gridPos": {
            "h": 6,
            "w": 24,
            "x": 0,
            "y": 90
          },
          "id": 133,
          "options": {
            "legend": {
              "calcs": [],
              "displayMode": "list",
              "placement": "bottom",
              "showLegend": true
            },
            "tooltip": {
              "mode": "single",
              "sort": "none"
            }
          },
          "targets": [
            {
              "datasource": {
                "type": "prometheus",
                "uid": "PBFA97CFB590B2093"
              },
              "editorMode": "code",
              "exemplar": false,
              "expr": "100 * avg_over_time(probe_success[$__rate_interval]) ",
              "hide": false,
              "instant": false,
              "legendFormat": "{{instance}}",
              "range": true,
              "refId": "A"
            }
          ],
          "title": "Availability",
          "type": "timeseries"
        }
      ],
      "title": "Latency",
      "type": "row"
    },
    {
      "collapsed": true,
      "datasource": {
        "type": "prometheus"
      },
      "gridPos": {
        "h": 1,
        "w": 24,
        "x": 0,
        "y": 34
      },
      "id": 2,
      "panels": [
        {
          "datasource": {
            "type": "prometheus"
          },
          "description": "",
          "fieldConfig": {
            "defaults": {
              "decimals": 0,
              "links": [],
              "mappings": [],
              "min": 1,
              "thresholds": {
                "mode": "absolute",
                "steps": [
                  {
                    "color": "green"
                  },
                  {
                    "color": "#EAB839",
                    "value": 30
                  },
                  {
                    "color": "red",
                    "value": 80
                  }
                ]
              },
              "unitScale": true
            },
            "overrides": []
          },
          "gridPos": {
            "h": 8,
            "w": 5,
            "x": 0,
            "y": 83
          },
          "id": 20,
          "links": [],
          "options": {
            "displayMode": "lcd",
            "maxVizHeight": 300,
            "minVizHeight": 10,
            "minVizWidth": 0,
            "namePlacement": "auto",
            "orientation": "horizontal",
            "reduceOptions": {
              "calcs": ["mean"],
              "fields": "",
              "values": false
            },
            "showUnfilled": true,
            "sizing": "auto",
            "text": {},
            "valueMode": "color"
          },
          "pluginVersion": "10.3.1",
          "targets": [
            {
              "application": {
                "filter": "Network"
              },
              "datasource": {
                "type": "prometheus"
              },
              "expr": "mktxp_dhcp_lease_active_count{routerboard_address=\"$node\"}",
              "format": "time_series",
              "functions": [],
              "group": {
                "filter": "Network"
              },
              "hide": false,
              "host": {
                "filter": "MikroTik Router"
              },
              "instant": true,
              "interval": "",
              "intervalFactor": 1,
              "item": {
                "filter": "Incoming traffic on interface ether1-gateway"
              },
              "legendFormat": "{{ server }}",
              "mode": 0,
              "options": {
                "showDisabledItems": false
              },
              "refId": "A"
            }
          ],
          "title": "DHCP Leases by Server",
          "type": "bargauge"
        },
        {
          "datasource": {
            "type": "prometheus"
          },
          "fieldConfig": {
            "defaults": {
              "color": {
                "mode": "fixed"
              },
              "custom": {
                "align": "center",
                "cellOptions": {
                  "type": "auto"
                },
                "filterable": false,
                "inspect": false
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
              },
              "unitScale": true
            },
            "overrides": [
              {
                "matcher": {
                  "id": "byName",
                  "options": "__name__"
                },
                "properties": [
                  {
                    "id": "displayName"
                  }
                ]
              },
              {
                "matcher": {
                  "id": "byName",
                  "options": "mac_address"
                },
                "properties": [
                  {
                    "id": "custom.width",
                    "value": 231
                  }
                ]
              },
              {
                "matcher": {
                  "id": "byName",
                  "options": "DHCP VLAN"
                },
                "properties": [
                  {
                    "id": "custom.width",
                    "value": 227
                  }
                ]
              },
              {
                "matcher": {
                  "id": "byName",
                  "options": "active_address"
                },
                "properties": [
                  {
                    "id": "custom.width",
                    "value": 240
                  }
                ]
              },
              {
                "matcher": {
                  "id": "byName",
                  "options": "Host Name"
                },
                "properties": [
                  {
                    "id": "custom.width",
                    "value": 383
                  }
                ]
              },
              {
                "matcher": {
                  "id": "byName",
                  "options": "Comment"
                },
                "properties": [
                  {
                    "id": "custom.width",
                    "value": 360
                  }
                ]
              }
            ]
          },
          "gridPos": {
            "h": 11,
            "w": 19,
            "x": 5,
            "y": 83
          },
          "id": 25,
          "options": {
            "cellHeight": "sm",
            "footer": {
              "countRows": false,
              "fields": "",
              "reducer": ["sum"],
              "show": false
            },
            "showHeader": true,
            "sortBy": [
              {
                "desc": true,
                "displayName": "active_address"
              }
            ]
          },
          "pluginVersion": "10.3.1",
          "targets": [
            {
              "datasource": {
                "type": "prometheus"
              },
              "expr": "mktxp_dhcp_lease_info{routerboard_address=\"$node\"}",
              "format": "table",
              "instant": true,
              "interval": "",
              "legendFormat": "",
              "refId": "A"
            }
          ],
          "title": "DHCP Leases",
          "transformations": [
            {
              "id": "organize",
              "options": {
                "excludeByName": {
                  "Time": true,
                  "Value": true,
                  "__name__": true,
                  "instance": true,
                  "job": true,
                  "routerboard_address": true,
                  "routerboard_name": true
                },
                "indexByName": {
                  "Time": 9,
                  "Value": 13,
                  "__name__": 8,
                  "active_address": 5,
                  "address": 4,
                  "comment": 1,
                  "expires_after": 6,
                  "host_name": 0,
                  "instance": 7,
                  "job": 10,
                  "mac_address": 3,
                  "routerboard_address": 11,
                  "routerboard_name": 12,
                  "server": 2
                },
                "renameByName": {
                  "comment": "Comment",
                  "host_name": "Host Name",
                  "server": "DHCP Server"
                }
              }
            }
          ],
          "type": "table"
        },
        {
          "datasource": {
            "type": "prometheus"
          },
          "description": "",
          "fieldConfig": {
            "defaults": {
              "decimals": 0,
              "links": [],
              "mappings": [],
              "min": 1,
              "thresholds": {
                "mode": "absolute",
                "steps": [
                  {
                    "color": "green"
                  },
                  {
                    "color": "#EAB839",
                    "value": 30
                  },
                  {
                    "color": "red",
                    "value": 80
                  }
                ]
              }
            },
            "overrides": []
          },
          "gridPos": {
            "h": 3,
            "w": 5,
            "x": 0,
            "y": 91
          },
          "id": 23,
          "links": [],
          "options": {
            "displayMode": "lcd",
            "minVizHeight": 10,
            "minVizWidth": 0,
            "orientation": "horizontal",
            "reduceOptions": {
              "calcs": ["mean"],
              "fields": "",
              "values": false
            },
            "showUnfilled": true,
            "text": {}
          },
          "pluginVersion": "9.0.6",
          "targets": [
            {
              "application": {
                "filter": "Network"
              },
              "datasource": {
                "type": "prometheus"
              },
              "expr": "sum(mktxp_dhcp_lease_active_count{routerboard_address=\"$node\"})",
              "format": "time_series",
              "functions": [],
              "group": {
                "filter": "Network"
              },
              "hide": false,
              "host": {
                "filter": "MikroTik Router"
              },
              "instant": true,
              "interval": "",
              "intervalFactor": 1,
              "item": {
                "filter": "Incoming traffic on interface ether1-gateway"
              },
              "legendFormat": "In - {{ server }}",
              "mode": 0,
              "options": {
                "showDisabledItems": false
              },
              "refId": "A"
            }
          ],
          "title": "Total DHCP Leases",
          "type": "bargauge"
        }
      ],
      "targets": [
        {
          "datasource": {
            "type": "prometheus"
          },
          "refId": "A"
        }
      ],
      "title": "DHCP",
      "type": "row"
    },
    {
      "collapsed": true,
      "datasource": {
        "type": "prometheus"
      },
      "gridPos": {
        "h": 1,
        "w": 24,
        "x": 0,
        "y": 35
      },
      "id": 45,
      "panels": [
        {
          "datasource": {
            "type": "prometheus"
          },
          "description": "",
          "fieldConfig": {
            "defaults": {
              "mappings": [
                {
                  "options": {
                    "0": {
                      "text": "Unplugged"
                    },
                    "1": {
                      "text": ""
                    }
                  },
                  "type": "value"
                }
              ],
              "min": 1,
              "thresholds": {
                "mode": "absolute",
                "steps": [
                  {
                    "color": "green"
                  },
                  {
                    "color": "yellow",
                    "value": 0
                  },
                  {
                    "color": "green",
                    "value": 1
                  }
                ]
              }
            },
            "overrides": []
          },
          "gridPos": {
            "h": 5,
            "w": 2,
            "x": 0,
            "y": 36
          },
          "id": 70,
          "options": {
            "minVizHeight": 75,
            "minVizWidth": 75,
            "orientation": "horizontal",
            "reduceOptions": {
              "calcs": ["lastNotNull"],
              "fields": "",
              "values": false
            },
            "showThresholdLabels": false,
            "showThresholdMarkers": true,
            "sizing": "auto",
            "text": {}
          },
          "pluginVersion": "11.2.0",
          "targets": [
            {
              "datasource": {
                "type": "prometheus"
              },
              "expr": "mktxp_routes_total_routes{routerboard_address=\"$node\"}",
              "format": "time_series",
              "instant": true,
              "interval": "",
              "legendFormat": "",
              "refId": "A"
            }
          ],
          "title": "Total Routes",
          "type": "gauge"
        },
        {
          "datasource": {
            "type": "prometheus"
          },
          "fieldConfig": {
            "defaults": {
              "links": [],
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
            "overrides": []
          },
          "gridPos": {
            "h": 5,
            "w": 4,
            "x": 2,
            "y": 36
          },
          "id": 71,
          "options": {
            "displayMode": "lcd",
            "maxVizHeight": 300,
            "minVizHeight": 10,
            "minVizWidth": 0,
            "namePlacement": "auto",
            "orientation": "horizontal",
            "reduceOptions": {
              "calcs": ["mean"],
              "fields": "",
              "values": false
            },
            "showUnfilled": true,
            "sizing": "auto",
            "text": {},
            "valueMode": "color"
          },
          "pluginVersion": "11.2.0",
          "targets": [
            {
              "application": {
                "filter": "Network"
              },
              "datasource": {
                "type": "prometheus"
              },
              "expr": "mktxp_routes_protocol_count{routerboard_address=\"$node\"}",
              "format": "time_series",
              "functions": [],
              "group": {
                "filter": "Network"
              },
              "hide": false,
              "host": {
                "filter": "MikroTik Router"
              },
              "instant": true,
              "interval": "",
              "intervalFactor": 1,
              "item": {
                "filter": "/errors on interface/"
              },
              "legendFormat": "{{protocol}}",
              "mode": 0,
              "options": {
                "showDisabledItems": false
              },
              "refId": "A"
            }
          ],
          "title": "Routes per protocol",
          "type": "bargauge"
        },
        {
          "datasource": {
            "type": "prometheus"
          },
          "description": "",
          "fieldConfig": {
            "defaults": {
              "mappings": [
                {
                  "options": {
                    "0": {
                      "text": "No"
                    },
                    "1": {
                      "text": "Yes"
                    }
                  },
                  "type": "value"
                }
              ],
              "min": 1,
              "thresholds": {
                "mode": "absolute",
                "steps": [
                  {
                    "color": "green"
                  },
                  {
                    "color": "yellow",
                    "value": 0
                  },
                  {
                    "color": "green",
                    "value": 1
                  }
                ]
              }
            },
            "overrides": []
          },
          "gridPos": {
            "h": 5,
            "w": 6,
            "x": 6,
            "y": 36
          },
          "id": 69,
          "options": {
            "displayMode": "lcd",
            "maxVizHeight": 300,
            "minVizHeight": 10,
            "minVizWidth": 0,
            "namePlacement": "auto",
            "orientation": "horizontal",
            "reduceOptions": {
              "calcs": ["lastNotNull"],
              "fields": "",
              "values": false
            },
            "showUnfilled": true,
            "sizing": "auto",
            "text": {},
            "valueMode": "color"
          },
          "pluginVersion": "11.2.0",
          "targets": [
            {
              "datasource": {
                "type": "prometheus"
              },
              "expr": "mktxp_interface_full_duplex{routerboard_address=\"$node\"}",
              "format": "time_series",
              "instant": true,
              "interval": "",
              "legendFormat": "{{name}}",
              "refId": "A"
            }
          ],
          "title": "Ethernet Ports: Full Duplex",
          "type": "bargauge"
        },
        {
          "datasource": {
            "type": "prometheus",
            "uid": "PBFA97CFB590B2093"
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
                    "color": "green"
                  },
                  {
                    "color": "red",
                    "value": 80
                  }
                ]
              }
            },
            "overrides": []
          },
          "gridPos": {
            "h": 2,
            "w": 12,
            "x": 12,
            "y": 36
          },
          "id": 143,
          "options": {
            "colorMode": "value",
            "graphMode": "area",
            "justifyMode": "auto",
            "orientation": "auto",
            "percentChangeColorMode": "standard",
            "reduceOptions": {
              "calcs": ["lastNotNull"],
              "fields": "",
              "values": false
            },
            "showPercentChange": false,
            "textMode": "auto",
            "wideLayout": true
          },
          "pluginVersion": "11.2.0",
          "targets": [
            {
              "datasource": {
                "type": "prometheus",
                "uid": "PBFA97CFB590B2093"
              },
              "editorMode": "code",
              "exemplar": false,
              "expr": "sum(mktxp_interface_rx_error_total{routerboard_address=\"$node\"}) + sum(mktxp_interface_tx_error_total{routerboard_address=\"$node\"})",
              "instant": false,
              "legendFormat": "__auto",
              "range": true,
              "refId": "A"
            }
          ],
          "title": "Total Interface Errors",
          "type": "stat"
        },
        {
          "datasource": {
            "type": "prometheus"
          },
          "fieldConfig": {
            "defaults": {
              "color": {
                "mode": "palette-classic"
              },
              "custom": {
                "axisBorderShow": false,
                "axisCenteredZero": false,
                "axisColorMode": "text",
                "axisLabel": "",
                "axisPlacement": "auto",
                "barAlignment": 0,
                "barWidthFactor": 0.6,
                "drawStyle": "line",
                "fillOpacity": 10,
                "gradientMode": "none",
                "hideFrom": {
                  "legend": false,
                  "tooltip": false,
                  "viz": false
                },
                "insertNulls": false,
                "lineInterpolation": "linear",
                "lineWidth": 1,
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
                  "mode": "off"
                }
              },
              "links": [],
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
            "overrides": []
          },
          "gridPos": {
            "h": 14,
            "w": 12,
            "x": 12,
            "y": 38
          },
          "id": 55,
          "options": {
            "legend": {
              "calcs": ["mean", "sum"],
              "displayMode": "table",
              "placement": "right",
              "showLegend": true
            },
            "tooltip": {
              "mode": "multi",
              "sort": "none"
            }
          },
          "pluginVersion": "10.3.1",
          "targets": [
            {
              "application": {
                "filter": "Network"
              },
              "datasource": {
                "type": "prometheus"
              },
              "expr": "mktxp_interface_rx_error_total{routerboard_address=\"$node\"}",
              "format": "time_series",
              "functions": [],
              "group": {
                "filter": "Network"
              },
              "hide": false,
              "host": {
                "filter": "MikroTik Router"
              },
              "interval": "",
              "intervalFactor": 1,
              "item": {
                "filter": "/errors on interface/"
              },
              "legendFormat": "In Errors | {{name}}",
              "mode": 0,
              "options": {
                "showDisabledItems": false
              },
              "refId": "A"
            },
            {
              "datasource": {
                "type": "prometheus"
              },
              "expr": "mktxp_interface_tx_error_total{routerboard_address=\"$node\"}",
              "format": "time_series",
              "hide": false,
              "interval": "",
              "intervalFactor": 1,
              "legendFormat": "Out Errors | {{name}}",
              "refId": "B"
            }
          ],
          "title": "Interface Errors",
          "type": "timeseries"
        },
        {
          "datasource": {
            "type": "prometheus"
          },
          "description": "",
          "fieldConfig": {
            "defaults": {
              "mappings": [
                {
                  "options": {
                    "0": {
                      "text": "Unplugged"
                    },
                    "1": {
                      "text": "Plugged-In"
                    }
                  },
                  "type": "value"
                }
              ],
              "min": 1,
              "thresholds": {
                "mode": "absolute",
                "steps": [
                  {
                    "color": "green"
                  },
                  {
                    "color": "yellow",
                    "value": 0
                  },
                  {
                    "color": "green",
                    "value": 1
                  }
                ]
              }
            },
            "overrides": []
          },
          "gridPos": {
            "h": 7,
            "w": 6,
            "x": 0,
            "y": 41
          },
          "id": 51,
          "options": {
            "displayMode": "lcd",
            "maxVizHeight": 300,
            "minVizHeight": 10,
            "minVizWidth": 0,
            "namePlacement": "auto",
            "orientation": "horizontal",
            "reduceOptions": {
              "calcs": ["last"],
              "fields": "",
              "values": false
            },
            "showUnfilled": true,
            "sizing": "auto",
            "text": {},
            "valueMode": "color"
          },
          "pluginVersion": "11.2.0",
          "targets": [
            {
              "datasource": {
                "type": "prometheus"
              },
              "expr": "mktxp_interface_status{routerboard_address=\"$node\"}",
              "format": "time_series",
              "instant": true,
              "interval": "",
              "legendFormat": "{{name}}",
              "refId": "A"
            }
          ],
          "title": "Ethernet Ports: Status",
          "type": "bargauge"
        },
        {
          "datasource": {
            "type": "prometheus"
          },
          "fieldConfig": {
            "defaults": {
              "custom": {
                "align": "auto",
                "cellOptions": {
                  "type": "auto"
                },
                "filterable": false,
                "inspect": false
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
              },
              "unit": "Mbits"
            },
            "overrides": []
          },
          "gridPos": {
            "h": 7,
            "w": 6,
            "x": 6,
            "y": 41
          },
          "id": 53,
          "options": {
            "cellHeight": "sm",
            "footer": {
              "countRows": false,
              "fields": "",
              "reducer": ["sum"],
              "show": false
            },
            "showHeader": true
          },
          "pluginVersion": "11.2.0",
          "targets": [
            {
              "datasource": {
                "type": "prometheus"
              },
              "expr": "mktxp_interface_rate{routerboard_address=\"$node\"}",
              "format": "table",
              "instant": true,
              "interval": "",
              "legendFormat": "{{name}}",
              "refId": "A"
            }
          ],
          "title": "Rates",
          "transformations": [
            {
              "id": "organize",
              "options": {
                "excludeByName": {
                  "Time": true,
                  "__name__": true,
                  "address": true,
                  "env": true,
                  "instance": true,
                  "job": true,
                  "name": false,
                  "routerboard_address": true,
                  "routerboard_name": true
                },
                "indexByName": {},
                "renameByName": {
                  "Value": "Rate",
                  "name": "Interface",
                  "routerboard_name": ""
                }
              }
            }
          ],
          "type": "table"
        },
        {
          "datasource": {
            "type": "prometheus"
          },
          "fieldConfig": {
            "defaults": {
              "color": {
                "mode": "fixed"
              },
              "custom": {
                "align": "center",
                "cellOptions": {
                  "type": "auto"
                },
                "filterable": false,
                "inspect": false
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
                  "options": "__name__"
                },
                "properties": [
                  {
                    "id": "displayName"
                  }
                ]
              },
              {
                "matcher": {
                  "id": "byName",
                  "options": "mac_address"
                },
                "properties": [
                  {
                    "id": "custom.width",
                    "value": 231
                  }
                ]
              },
              {
                "matcher": {
                  "id": "byName",
                  "options": "DHCP VLAN"
                },
                "properties": [
                  {
                    "id": "custom.width",
                    "value": 227
                  }
                ]
              },
              {
                "matcher": {
                  "id": "byName",
                  "options": "active_address"
                },
                "properties": [
                  {
                    "id": "custom.width",
                    "value": 240
                  }
                ]
              },
              {
                "matcher": {
                  "id": "byName",
                  "options": "Host Name"
                },
                "properties": [
                  {
                    "id": "custom.width",
                    "value": 383
                  }
                ]
              },
              {
                "matcher": {
                  "id": "byName",
                  "options": "Comment"
                },
                "properties": [
                  {
                    "id": "custom.width",
                    "value": 360
                  }
                ]
              }
            ]
          },
          "gridPos": {
            "h": 4,
            "w": 12,
            "x": 0,
            "y": 48
          },
          "id": 85,
          "options": {
            "cellHeight": "sm",
            "footer": {
              "countRows": false,
              "fields": "",
              "reducer": ["sum"],
              "show": false
            },
            "showHeader": true,
            "sortBy": [
              {
                "desc": true,
                "displayName": "active_address"
              }
            ]
          },
          "pluginVersion": "11.2.0",
          "targets": [
            {
              "datasource": {
                "type": "prometheus"
              },
              "expr": "mktxp_poe_info{routerboard_address=\"$node\"}",
              "format": "table",
              "instant": true,
              "interval": "",
              "legendFormat": "",
              "refId": "A"
            }
          ],
          "title": "POE",
          "transformations": [
            {
              "id": "organize",
              "options": {
                "excludeByName": {
                  "Time": true,
                  "Value": true,
                  "__name__": true,
                  "instance": true,
                  "job": true,
                  "routerboard_address": true,
                  "routerboard_name": true
                },
                "indexByName": {
                  "Time": 9,
                  "Value": 13,
                  "__name__": 8,
                  "active_address": 5,
                  "address": 4,
                  "comment": 1,
                  "expires_after": 6,
                  "host_name": 0,
                  "instance": 7,
                  "job": 10,
                  "mac_address": 3,
                  "routerboard_address": 11,
                  "routerboard_name": 12,
                  "server": 2
                },
                "renameByName": {
                  "comment": "Comment",
                  "host_name": "Host Name",
                  "name": "Interface",
                  "poe_out": "State",
                  "poe_out_status": "Status",
                  "poe_priority": "Priority",
                  "server": "DHCP Server"
                }
              }
            }
          ],
          "type": "table"
        }
      ],
      "targets": [
        {
          "datasource": {
            "type": "prometheus"
          },
          "refId": "A"
        }
      ],
      "title": "Network",
      "type": "row"
    },
    {
      "collapsed": true,
      "datasource": {
        "type": "prometheus"
      },
      "gridPos": {
        "h": 1,
        "w": 24,
        "x": 0,
        "y": 36
      },
      "id": 84,
      "panels": [
        {
          "aliasColors": {
            "Incoming traffic on interface ether1-gateway": "#1F78C1",
            "Outgoing traffic on interface ether1-gateway": "#EAB839"
          },
          "bars": false,
          "dashLength": 10,
          "dashes": false,
          "datasource": {
            "type": "prometheus"
          },
          "description": "",
          "editable": true,
          "error": false,
          "fieldConfig": {
            "defaults": {
              "links": [],
              "unit": "decbytes"
            },
            "overrides": []
          },
          "fill": 3,
          "fillGradient": 0,
          "gridPos": {
            "h": 7,
            "w": 12,
            "x": 0,
            "y": 171
          },
          "hiddenSeries": false,
          "id": 81,
          "legend": {
            "alignAsTable": true,
            "avg": true,
            "current": false,
            "hideEmpty": false,
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
          "nullPointMode": "connected",
          "options": {
            "alertThreshold": true
          },
          "paceLength": 10,
          "percentage": false,
          "pluginVersion": "9.3.6",
          "pointradius": 5,
          "points": false,
          "renderer": "flot",
          "seriesOverrides": [],
          "spaceLength": 10,
          "stack": false,
          "steppedLine": false,
          "targets": [
            {
              "application": {
                "filter": "Network"
              },
              "datasource": {
                "type": "prometheus"
              },
              "expr": "rate(mktxp_firewall_filter_total{routerboard_address=\"$node\", log=\"1\"}[4m])",
              "format": "time_series",
              "functions": [],
              "group": {
                "filter": "Network"
              },
              "hide": false,
              "host": {
                "filter": "MikroTik Router"
              },
              "instant": false,
              "interval": "",
              "intervalFactor": 1,
              "item": {
                "filter": "Incoming traffic on interface ether1-gateway"
              },
              "legendFormat": "{{ name }}",
              "mode": 0,
              "options": {
                "showDisabledItems": false
              },
              "refId": "A"
            }
          ],
          "thresholds": [],
          "timeRegions": [],
          "title": "Logged Firewall Rules Traffic ",
          "tooltip": {
            "msResolution": false,
            "shared": true,
            "sort": 2,
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
              "$$hashKey": "object:706",
              "format": "decbytes",
              "label": "",
              "logBase": 2,
              "show": true
            },
            {
              "$$hashKey": "object:707",
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
            "Incoming traffic on interface ether1-gateway": "#1F78C1",
            "Outgoing traffic on interface ether1-gateway": "#EAB839"
          },
          "bars": false,
          "dashLength": 10,
          "dashes": false,
          "datasource": {
            "type": "prometheus"
          },
          "description": "",
          "editable": true,
          "error": false,
          "fieldConfig": {
            "defaults": {
              "links": [],
              "unit": "decbytes"
            },
            "overrides": []
          },
          "fill": 3,
          "fillGradient": 0,
          "gridPos": {
            "h": 7,
            "w": 12,
            "x": 12,
            "y": 171
          },
          "hiddenSeries": false,
          "id": 82,
          "legend": {
            "alignAsTable": true,
            "avg": true,
            "current": false,
            "hideEmpty": false,
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
          "nullPointMode": "connected",
          "options": {
            "alertThreshold": true
          },
          "paceLength": 10,
          "percentage": false,
          "pluginVersion": "9.3.6",
          "pointradius": 5,
          "points": false,
          "renderer": "flot",
          "seriesOverrides": [],
          "spaceLength": 10,
          "stack": false,
          "steppedLine": false,
          "targets": [
            {
              "application": {
                "filter": "Network"
              },
              "datasource": {
                "type": "prometheus"
              },
              "expr": "rate(mktxp_firewall_raw_total{routerboard_address=\"$node\", log=\"1\"}[4m])",
              "format": "time_series",
              "functions": [],
              "group": {
                "filter": "Network"
              },
              "hide": false,
              "host": {
                "filter": "MikroTik Router"
              },
              "instant": false,
              "interval": "",
              "intervalFactor": 1,
              "item": {
                "filter": "Incoming traffic on interface ether1-gateway"
              },
              "legendFormat": "{{ name }}",
              "mode": 0,
              "options": {
                "showDisabledItems": false
              },
              "refId": "A"
            }
          ],
          "thresholds": [],
          "timeRegions": [],
          "title": "Logged Raw Firewall Rules Traffic ",
          "tooltip": {
            "msResolution": false,
            "shared": true,
            "sort": 2,
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
              "$$hashKey": "object:706",
              "format": "decbytes",
              "label": "",
              "logBase": 2,
              "show": true
            },
            {
              "$$hashKey": "object:707",
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
            "uid": "PBFA97CFB590B2093"
          },
          "fieldConfig": {
            "defaults": {
              "color": {
                "mode": "palette-classic"
              },
              "custom": {
                "axisCenteredZero": false,
                "axisColorMode": "text",
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
                "lineWidth": 1,
                "pointSize": 5,
                "scaleDistribution": {
                  "log": 2,
                  "type": "log"
                },
                "showPoints": "never",
                "spanNulls": true,
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
            "h": 15,
            "w": 12,
            "x": 0,
            "y": 178
          },
          "id": 106,
          "options": {
            "legend": {
              "calcs": ["min", "max", "mean"],
              "displayMode": "table",
              "placement": "bottom",
              "showLegend": true,
              "sortBy": "Mean",
              "sortDesc": true
            },
            "tooltip": {
              "mode": "single",
              "sort": "none"
            }
          },
          "targets": [
            {
              "datasource": {
                "type": "prometheus",
                "uid": "PBFA97CFB590B2093"
              },
              "editorMode": "code",
              "expr": "rate(mktxp_firewall_filter_ipv6_total{routerboard_address=\"$node\"}[$__rate_interval])",
              "legendFormat": "{{name}}",
              "range": true,
              "refId": "A"
            }
          ],
          "title": "Firewall Rules Traffic (IPv6)",
          "type": "timeseries"
        },
        {
          "datasource": {
            "type": "prometheus",
            "uid": "PBFA97CFB590B2093"
          },
          "description": "",
          "fieldConfig": {
            "defaults": {
              "color": {
                "mode": "palette-classic"
              },
              "custom": {
                "axisCenteredZero": false,
                "axisColorMode": "text",
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
                "lineWidth": 1,
                "pointSize": 5,
                "scaleDistribution": {
                  "log": 2,
                  "type": "log"
                },
                "showPoints": "never",
                "spanNulls": true,
                "stacking": {
                  "group": "A",
                  "mode": "none"
                },
                "thresholdsStyle": {
                  "mode": "off"
                }
              },
              "links": [],
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
              "unit": "Bps"
            },
            "overrides": []
          },
          "gridPos": {
            "h": 15,
            "w": 12,
            "x": 12,
            "y": 178
          },
          "id": 43,
          "links": [],
          "options": {
            "legend": {
              "calcs": ["mean", "max", "min"],
              "displayMode": "table",
              "placement": "bottom",
              "showLegend": true,
              "sortBy": "Mean",
              "sortDesc": true
            },
            "tooltip": {
              "mode": "multi",
              "sort": "desc"
            }
          },
          "pluginVersion": "9.0.6",
          "targets": [
            {
              "application": {
                "filter": "Network"
              },
              "datasource": {
                "type": "prometheus"
              },
              "expr": "rate(mktxp_firewall_filter_total{routerboard_address=\"$node\"}[$__rate_interval])",
              "format": "time_series",
              "functions": [],
              "group": {
                "filter": "Network"
              },
              "hide": false,
              "host": {
                "filter": "MikroTik Router"
              },
              "instant": false,
              "interval": "",
              "intervalFactor": 1,
              "item": {
                "filter": "Incoming traffic on interface ether1-gateway"
              },
              "legendFormat": "{{ name }}",
              "mode": 0,
              "options": {
                "showDisabledItems": false
              },
              "refId": "A"
            }
          ],
          "title": "Firewall Rules Traffic (IPv4)",
          "type": "timeseries"
        },
        {
          "datasource": {
            "type": "prometheus",
            "uid": "PBFA97CFB590B2093"
          },
          "description": "",
          "fieldConfig": {
            "defaults": {
              "color": {
                "mode": "palette-classic"
              },
              "custom": {
                "axisCenteredZero": false,
                "axisColorMode": "text",
                "axisLabel": "",
                "axisPlacement": "auto",
                "barAlignment": 0,
                "drawStyle": "line",
                "fillOpacity": 30,
                "gradientMode": "hue",
                "hideFrom": {
                  "legend": false,
                  "tooltip": false,
                  "viz": false
                },
                "lineInterpolation": "smooth",
                "lineWidth": 1,
                "pointSize": 5,
                "scaleDistribution": {
                  "log": 2,
                  "type": "log"
                },
                "showPoints": "never",
                "spanNulls": true,
                "stacking": {
                  "group": "A",
                  "mode": "none"
                },
                "thresholdsStyle": {
                  "mode": "off"
                }
              },
              "links": [],
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
              "unit": "Bps"
            },
            "overrides": [
              {
                "matcher": {
                  "id": "byName",
                  "options": "| prerouting | passthrough | special dummy rule to show fasttrack counters"
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
              }
            ]
          },
          "gridPos": {
            "h": 6,
            "w": 24,
            "x": 0,
            "y": 193
          },
          "id": 76,
          "links": [],
          "options": {
            "legend": {
              "calcs": ["mean", "max", "min"],
              "displayMode": "table",
              "placement": "bottom",
              "showLegend": true
            },
            "tooltip": {
              "mode": "multi",
              "sort": "desc"
            }
          },
          "pluginVersion": "9.0.6",
          "targets": [
            {
              "application": {
                "filter": "Network"
              },
              "datasource": {
                "type": "prometheus"
              },
              "expr": "rate(mktxp_firewall_raw_total{routerboard_address=\"$node\"}[$__rate_interval])",
              "format": "time_series",
              "functions": [],
              "group": {
                "filter": "Network"
              },
              "hide": false,
              "host": {
                "filter": "MikroTik Router"
              },
              "instant": false,
              "interval": "",
              "intervalFactor": 1,
              "item": {
                "filter": "Incoming traffic on interface ether1-gateway"
              },
              "legendFormat": "{{ name }}",
              "mode": 0,
              "options": {
                "showDisabledItems": false
              },
              "refId": "A"
            }
          ],
          "title": "Raw Firewall Rules Traffic (IPv4)",
          "type": "timeseries"
        },
        {
          "aliasColors": {
            "download": "dark-green",
            "upload": "dark-blue"
          },
          "bars": false,
          "dashLength": 10,
          "dashes": false,
          "datasource": {
            "type": "prometheus"
          },
          "decimals": 0,
          "fieldConfig": {
            "defaults": {
              "links": [],
              "unit": "binbps"
            },
            "overrides": []
          },
          "fill": 1,
          "fillGradient": 0,
          "gridPos": {
            "h": 7,
            "w": 12,
            "x": 0,
            "y": 199
          },
          "hiddenSeries": false,
          "id": 27,
          "legend": {
            "alignAsTable": true,
            "avg": true,
            "current": true,
            "hideEmpty": true,
            "hideZero": true,
            "max": true,
            "min": false,
            "show": true,
            "total": false,
            "values": true
          },
          "lines": true,
          "linewidth": 1,
          "nullPointMode": "null",
          "options": {
            "alertThreshold": false
          },
          "percentage": false,
          "pluginVersion": "9.3.6",
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
                "type": "prometheus"
              },
              "expr": "mktxp_internet_bandwidth",
              "instant": false,
              "interval": "",
              "legendFormat": "{{direction}}",
              "refId": "A"
            }
          ],
          "thresholds": [],
          "timeRegions": [],
          "title": "Internet Bandwidth",
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
              "$$hashKey": "object:54",
              "decimals": 0,
              "format": "binbps",
              "label": "",
              "logBase": 1,
              "show": true
            },
            {
              "$$hashKey": "object:55",
              "format": "short",
              "logBase": 1,
              "show": true
            }
          ],
          "yaxis": {
            "align": false
          }
        },
        {
          "aliasColors": {
            "latency": "dark-green"
          },
          "bars": false,
          "dashLength": 10,
          "dashes": false,
          "datasource": {
            "type": "prometheus"
          },
          "decimals": 0,
          "fieldConfig": {
            "defaults": {
              "links": [],
              "unit": "ms"
            },
            "overrides": []
          },
          "fill": 1,
          "fillGradient": 0,
          "gridPos": {
            "h": 7,
            "w": 12,
            "x": 12,
            "y": 199
          },
          "hiddenSeries": false,
          "id": 74,
          "legend": {
            "alignAsTable": true,
            "avg": true,
            "current": true,
            "hideEmpty": true,
            "hideZero": true,
            "max": true,
            "min": false,
            "show": true,
            "total": false,
            "values": true
          },
          "lines": true,
          "linewidth": 1,
          "nullPointMode": "null",
          "options": {
            "alertThreshold": false
          },
          "percentage": false,
          "pluginVersion": "9.3.6",
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
                "type": "prometheus"
              },
              "expr": "mktxp_internet_latency",
              "instant": false,
              "interval": "",
              "legendFormat": "latency",
              "refId": "A"
            }
          ],
          "thresholds": [],
          "timeRegions": [],
          "title": "Internet Latency",
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
              "$$hashKey": "object:54",
              "decimals": 0,
              "format": "ms",
              "label": "",
              "logBase": 1,
              "show": true
            },
            {
              "$$hashKey": "object:55",
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
            "uid": "PBFA97CFB590B2093"
          },
          "description": "Shows active users on all monitored devices.",
          "fieldConfig": {
            "defaults": {
              "color": {
                "mode": "thresholds"
              },
              "custom": {
                "align": "auto",
                "cellOptions": {
                  "type": "auto"
                },
                "inspect": false
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
            "overrides": []
          },
          "gridPos": {
            "h": 7,
            "w": 24,
            "x": 0,
            "y": 206
          },
          "id": 127,
          "options": {
            "footer": {
              "enablePagination": true,
              "fields": "",
              "reducer": ["sum"],
              "show": false
            },
            "frameIndex": 2,
            "showHeader": true,
            "sortBy": [
              {
                "desc": false,
                "displayName": "routerboard_name"
              }
            ]
          },
          "pluginVersion": "9.3.6",
          "targets": [
            {
              "datasource": {
                "type": "prometheus",
                "uid": "PBFA97CFB590B2093"
              },
              "editorMode": "code",
              "exemplar": false,
              "expr": "mktxp_active_users_info",
              "format": "table",
              "hide": false,
              "instant": true,
              "legendFormat": "__auto",
              "range": false,
              "refId": "B"
            }
          ],
          "title": "Global Active Users",
          "transformations": [
            {
              "id": "organize",
              "options": {
                "excludeByName": {
                  "Time": true,
                  "Value": true,
                  "__name__": true,
                  "instance": true,
                  "job": true
                },
                "indexByName": {
                  "Time": 9,
                  "Value": 11,
                  "__name__": 8,
                  "address": 2,
                  "group": 3,
                  "instance": 7,
                  "job": 10,
                  "name": 4,
                  "routerboard_address": 1,
                  "routerboard_name": 0,
                  "via": 5,
                  "when": 6
                },
                "renameByName": {
                  "routerboard_address": "",
                  "routerboard_name": ""
                }
              }
            }
          ],
          "type": "table"
        }
      ],
      "targets": [
        {
          "datasource": {
            "type": "prometheus"
          },
          "refId": "A"
        }
      ],
      "title": "Firewall",
      "type": "row"
    },
    {
      "collapsed": true,
      "datasource": {
        "type": "prometheus"
      },
      "gridPos": {
        "h": 1,
        "w": 24,
        "x": 0,
        "y": 37
      },
      "id": 90,
      "panels": [
        {
          "datasource": {
            "default": true,
            "type": "prometheus",
            "uid": "PBFA97CFB590B2093"
          },
          "description": "",
          "fieldConfig": {
            "defaults": {
              "color": {
                "mode": "continuous-GrYlRd"
              },
              "custom": {
                "fillOpacity": 70,
                "hideFrom": {
                  "legend": false,
                  "tooltip": false,
                  "viz": false
                },
                "insertNulls": false,
                "lineWidth": 0,
                "spanNulls": false
              },
              "mappings": [],
              "thresholds": {
                "mode": "absolute",
                "steps": [
                  {
                    "color": "green",
                    "value": null
                  },
                  {
                    "color": "red",
                    "value": 80
                  }
                ]
              }
            },
            "overrides": []
          },
          "gridPos": {
            "h": 8,
            "w": 12,
            "x": 0,
            "y": 38
          },
          "id": 87,
          "options": {
            "alignValue": "left",
            "legend": {
              "displayMode": "list",
              "placement": "bottom",
              "showLegend": true
            },
            "mergeValues": true,
            "rowHeight": 0.9,
            "showValue": "auto",
            "tooltip": {
              "mode": "single",
              "sort": "none"
            }
          },
          "pluginVersion": "7.4.5",
          "targets": [
            {
              "application": {
                "filter": "Network"
              },
              "datasource": {
                "type": "prometheus"
              },
              "editorMode": "code",
              "expr": "max(max_over_time(mktxp_netwatch_status{routerboard_address=\"$node\"}[1m])) by (name)\n",
              "format": "time_series",
              "functions": [],
              "group": {
                "filter": "Network"
              },
              "hide": false,
              "host": {
                "filter": "MikroTik Router"
              },
              "instant": false,
              "interval": "",
              "intervalFactor": 1,
              "item": {
                "filter": "Incoming traffic on interface ether1-gateway"
              },
              "legendFormat": "{{ name }}",
              "mode": 0,
              "options": {
                "showDisabledItems": false
              },
              "refId": "A"
            }
          ],
          "title": "Status over time",
          "type": "state-timeline"
        },
        {
          "datasource": {
            "type": "prometheus"
          },
          "fieldConfig": {
            "defaults": {
              "color": {
                "mode": "fixed"
              },
              "custom": {
                "align": "center",
                "cellOptions": {
                  "type": "color-text"
                },
                "filterable": false,
                "inspect": false
              },
              "mappings": [],
              "thresholds": {
                "mode": "absolute",
                "steps": [
                  {
                    "color": "green",
                    "value": null
                  },
                  {
                    "color": "red",
                    "value": 0
                  },
                  {
                    "color": "green",
                    "value": 1
                  }
                ]
              }
            },
            "overrides": [
              {
                "matcher": {
                  "id": "byName",
                  "options": "Status"
                },
                "properties": [
                  {
                    "id": "mappings",
                    "value": [
                      {
                        "options": {
                          "0": {
                            "text": "Down"
                          },
                          "1": {
                            "text": "Up"
                          }
                        },
                        "type": "value"
                      }
                    ]
                  },
                  {
                    "id": "color",
                    "value": {
                      "mode": "fixed"
                    }
                  },
                  {
                    "id": "color"
                  }
                ]
              }
            ]
          },
          "gridPos": {
            "h": 8,
            "w": 12,
            "x": 12,
            "y": 38
          },
          "id": 88,
          "options": {
            "cellHeight": "sm",
            "footer": {
              "countRows": false,
              "fields": "",
              "reducer": ["sum"],
              "show": false
            },
            "showHeader": true,
            "sortBy": []
          },
          "pluginVersion": "11.2.0",
          "targets": [
            {
              "datasource": {
                "type": "prometheus"
              },
              "expr": "mktxp_netwatch_info{routerboard_address=\"$node\"}",
              "format": "table",
              "instant": true,
              "interval": "",
              "legendFormat": "",
              "refId": "A"
            }
          ],
          "title": "Netwatch Info",
          "transformations": [
            {
              "id": "organize",
              "options": {
                "excludeByName": {
                  "Time": true,
                  "Value": true,
                  "__name__": true,
                  "disabled": true,
                  "instance": true,
                  "job": true,
                  "name": true,
                  "routerboard_address": true,
                  "routerboard_name": true,
                  "timeout": true
                },
                "indexByName": {
                  "Time": 5,
                  "Value": 9,
                  "__name__": 4,
                  "comment": 1,
                  "host": 0,
                  "instance": 3,
                  "interval": 11,
                  "job": 6,
                  "name": 12,
                  "routerboard_address": 7,
                  "routerboard_name": 8,
                  "since": 10,
                  "status": 2,
                  "timeout": 13
                },
                "renameByName": {
                  "comment": "Comment",
                  "host": "Host",
                  "host_name": "Host Name",
                  "interval": "Interval",
                  "server": "DHCP Server",
                  "since": "Since",
                  "status": "Status"
                }
              }
            }
          ],
          "type": "table"
        }
      ],
      "targets": [
        {
          "datasource": {
            "type": "prometheus"
          },
          "refId": "A"
        }
      ],
      "title": "Netwatch",
      "type": "row"
    },
    {
      "collapsed": true,
      "datasource": {
        "type": "prometheus"
      },
      "gridPos": {
        "h": 1,
        "w": 24,
        "x": 0,
        "y": 38
      },
      "id": 29,
      "panels": [
        {
          "datasource": {
            "type": "prometheus"
          },
          "fieldConfig": {
            "defaults": {
              "color": {
                "mode": "palette-classic"
              },
              "custom": {
                "axisBorderShow": false,
                "axisCenteredZero": false,
                "axisColorMode": "text",
                "axisLabel": "",
                "axisPlacement": "auto",
                "barAlignment": 0,
                "barWidthFactor": 0.6,
                "drawStyle": "line",
                "fillOpacity": 10,
                "gradientMode": "none",
                "hideFrom": {
                  "legend": false,
                  "tooltip": false,
                  "viz": false
                },
                "insertNulls": false,
                "lineInterpolation": "linear",
                "lineWidth": 1,
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
              "decimals": 1,
              "links": [],
              "mappings": [],
              "thresholds": {
                "mode": "absolute",
                "steps": [
                  {
                    "color": "green",
                    "value": null
                  },
                  {
                    "color": "red",
                    "value": 80
                  }
                ]
              },
              "unit": "dB"
            },
            "overrides": [
              {
                "matcher": {
                  "id": "byValue",
                  "options": {
                    "op": "gte",
                    "reducer": "allIsZero",
                    "value": 0
                  }
                },
                "properties": [
                  {
                    "id": "custom.hideFrom",
                    "value": {
                      "legend": true,
                      "tooltip": true,
                      "viz": false
                    }
                  }
                ]
              },
              {
                "matcher": {
                  "id": "byValue",
                  "options": {
                    "op": "gte",
                    "reducer": "allIsNull",
                    "value": 0
                  }
                },
                "properties": [
                  {
                    "id": "custom.hideFrom",
                    "value": {
                      "legend": true,
                      "tooltip": true,
                      "viz": false
                    }
                  }
                ]
              }
            ]
          },
          "gridPos": {
            "h": 8,
            "w": 12,
            "x": 0,
            "y": 39
          },
          "id": 31,
          "options": {
            "legend": {
              "calcs": ["mean", "lastNotNull", "max", "min"],
              "displayMode": "table",
              "placement": "bottom",
              "showLegend": true
            },
            "tooltip": {
              "mode": "multi",
              "sort": "none"
            }
          },
          "pluginVersion": "9.0.6",
          "targets": [
            {
              "datasource": {
                "type": "prometheus"
              },
              "expr": "mktxp_wlan_noise_floor{routerboard_address=\"$node\"}",
              "interval": "",
              "legendFormat": "{{channel}}",
              "refId": "A"
            }
          ],
          "title": "Noise Floor",
          "type": "timeseries"
        },
        {
          "datasource": {
            "type": "prometheus"
          },
          "fieldConfig": {
            "defaults": {
              "color": {
                "mode": "palette-classic"
              },
              "custom": {
                "axisBorderShow": false,
                "axisCenteredZero": false,
                "axisColorMode": "text",
                "axisLabel": "",
                "axisPlacement": "auto",
                "barAlignment": 0,
                "barWidthFactor": 0.6,
                "drawStyle": "line",
                "fillOpacity": 10,
                "gradientMode": "none",
                "hideFrom": {
                  "legend": false,
                  "tooltip": false,
                  "viz": false
                },
                "insertNulls": false,
                "lineInterpolation": "linear",
                "lineWidth": 1,
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
              "decimals": 2,
              "links": [],
              "mappings": [],
              "max": 100,
              "thresholds": {
                "mode": "absolute",
                "steps": [
                  {
                    "color": "green",
                    "value": null
                  },
                  {
                    "color": "red",
                    "value": 80
                  }
                ]
              },
              "unit": "percent"
            },
            "overrides": [
              {
                "matcher": {
                  "id": "byValue",
                  "options": {
                    "op": "gte",
                    "reducer": "allIsZero",
                    "value": 0
                  }
                },
                "properties": [
                  {
                    "id": "custom.hideFrom",
                    "value": {
                      "legend": true,
                      "tooltip": true,
                      "viz": false
                    }
                  }
                ]
              },
              {
                "matcher": {
                  "id": "byValue",
                  "options": {
                    "op": "gte",
                    "reducer": "allIsNull",
                    "value": 0
                  }
                },
                "properties": [
                  {
                    "id": "custom.hideFrom",
                    "value": {
                      "legend": true,
                      "tooltip": true,
                      "viz": false
                    }
                  }
                ]
              }
            ]
          },
          "gridPos": {
            "h": 8,
            "w": 12,
            "x": 12,
            "y": 39
          },
          "id": 73,
          "options": {
            "legend": {
              "calcs": ["mean", "lastNotNull", "max", "min"],
              "displayMode": "table",
              "placement": "bottom",
              "showLegend": true
            },
            "tooltip": {
              "mode": "multi",
              "sort": "none"
            }
          },
          "pluginVersion": "9.0.6",
          "targets": [
            {
              "datasource": {
                "type": "prometheus"
              },
              "expr": "mktxp_wlan_overall_tx_ccq{routerboard_address=\"$node\"}",
              "instant": false,
              "interval": "",
              "legendFormat": "{{channel}}",
              "refId": "A"
            }
          ],
          "title": "Overall Tx CCQ",
          "type": "timeseries"
        },
        {
          "datasource": {
            "type": "prometheus"
          },
          "fieldConfig": {
            "defaults": {
              "color": {
                "mode": "fixed"
              },
              "custom": {
                "align": "center",
                "cellOptions": {
                  "type": "auto"
                },
                "filterable": false,
                "inspect": false
              },
              "mappings": [],
              "thresholds": {
                "mode": "absolute",
                "steps": [
                  {
                    "color": "green",
                    "value": null
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
                  "options": "__name__"
                },
                "properties": [
                  {
                    "id": "displayName"
                  }
                ]
              },
              {
                "matcher": {
                  "id": "byName",
                  "options": "rx_signal"
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
                  "options": "name"
                },
                "properties": [
                  {
                    "id": "custom.width",
                    "value": 267
                  }
                ]
              },
              {
                "matcher": {
                  "id": "byName",
                  "options": "mac_address"
                },
                "properties": [
                  {
                    "id": "custom.width",
                    "value": 165
                  }
                ]
              },
              {
                "matcher": {
                  "id": "byName",
                  "options": "ssid"
                },
                "properties": [
                  {
                    "id": "custom.width",
                    "value": 140
                  }
                ]
              }
            ]
          },
          "gridPos": {
            "h": 8,
            "w": 12,
            "x": 0,
            "y": 47
          },
          "id": 68,
          "options": {
            "cellHeight": "sm",
            "footer": {
              "countRows": false,
              "fields": "",
              "reducer": ["sum"],
              "show": false
            },
            "showHeader": true,
            "sortBy": [
              {
                "desc": true,
                "displayName": "rx_signal"
              }
            ]
          },
          "pluginVersion": "11.2.0",
          "targets": [
            {
              "datasource": {
                "type": "prometheus"
              },
              "expr": "mktxp_wlan_clients_devices_info{routerboard_address=\"$node\"}",
              "format": "table",
              "instant": true,
              "interval": "",
              "legendFormat": "",
              "refId": "A"
            }
          ],
          "title": "Client Devices",
          "transformations": [
            {
              "id": "organize",
              "options": {
                "excludeByName": {
                  "Time": true,
                  "Value": true,
                  "__name__": true,
                  "instance": true,
                  "job": true,
                  "routerboard_address": true,
                  "routerboard_name": true
                },
                "indexByName": {
                  "Time": 0,
                  "Value": 13,
                  "__name__": 1,
                  "dhcp_address": 3,
                  "dhcp_name": 2,
                  "instance": 12,
                  "interface": 11,
                  "job": 5,
                  "mac_address": 4,
                  "routerboard_address": 6,
                  "routerboard_name": 7,
                  "rx_rate": 8,
                  "tx_rate": 9,
                  "uptime": 10
                },
                "renameByName": {}
              }
            }
          ],
          "type": "table"
        },
        {
          "datasource": {
            "type": "prometheus"
          },
          "fieldConfig": {
            "defaults": {
              "color": {
                "mode": "palette-classic"
              },
              "custom": {
                "axisBorderShow": false,
                "axisCenteredZero": false,
                "axisColorMode": "text",
                "axisLabel": "",
                "axisPlacement": "auto",
                "barAlignment": 0,
                "barWidthFactor": 0.6,
                "drawStyle": "line",
                "fillOpacity": 10,
                "gradientMode": "none",
                "hideFrom": {
                  "legend": false,
                  "tooltip": false,
                  "viz": false
                },
                "insertNulls": false,
                "lineInterpolation": "linear",
                "lineWidth": 1,
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
              "links": [],
              "mappings": [],
              "thresholds": {
                "mode": "absolute",
                "steps": [
                  {
                    "color": "green",
                    "value": null
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
                  "id": "byValue",
                  "options": {
                    "op": "gte",
                    "reducer": "allIsZero",
                    "value": 0
                  }
                },
                "properties": [
                  {
                    "id": "custom.hideFrom",
                    "value": {
                      "legend": true,
                      "tooltip": true,
                      "viz": false
                    }
                  }
                ]
              },
              {
                "matcher": {
                  "id": "byValue",
                  "options": {
                    "op": "gte",
                    "reducer": "allIsNull",
                    "value": 0
                  }
                },
                "properties": [
                  {
                    "id": "custom.hideFrom",
                    "value": {
                      "legend": true,
                      "tooltip": true,
                      "viz": false
                    }
                  }
                ]
              }
            ]
          },
          "gridPos": {
            "h": 8,
            "w": 12,
            "x": 12,
            "y": 47
          },
          "id": 37,
          "options": {
            "legend": {
              "calcs": ["mean", "lastNotNull", "max", "min"],
              "displayMode": "table",
              "placement": "bottom",
              "showLegend": true
            },
            "tooltip": {
              "mode": "multi",
              "sort": "none"
            }
          },
          "pluginVersion": "9.0.6",
          "targets": [
            {
              "datasource": {
                "type": "prometheus"
              },
              "expr": "mktxp_wlan_registered_clients{routerboard_address=\"$node\"}",
              "interval": "",
              "legendFormat": "{{channel}}",
              "refId": "A"
            }
          ],
          "title": "Number of clients",
          "type": "timeseries"
        },
        {
          "datasource": {
            "type": "prometheus"
          },
          "description": "",
          "fieldConfig": {
            "defaults": {
              "color": {
                "mode": "palette-classic"
              },
              "custom": {
                "axisBorderShow": false,
                "axisCenteredZero": false,
                "axisColorMode": "text",
                "axisLabel": "",
                "axisPlacement": "auto",
                "barAlignment": 0,
                "barWidthFactor": 0.6,
                "drawStyle": "line",
                "fillOpacity": 10,
                "gradientMode": "none",
                "hideFrom": {
                  "legend": false,
                  "tooltip": false,
                  "viz": false
                },
                "insertNulls": false,
                "lineInterpolation": "linear",
                "lineWidth": 1,
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
              "links": [],
              "mappings": [],
              "max": 100,
              "thresholds": {
                "mode": "absolute",
                "steps": [
                  {
                    "color": "green",
                    "value": null
                  },
                  {
                    "color": "red",
                    "value": 80
                  }
                ]
              },
              "unit": "percent"
            },
            "overrides": [
              {
                "matcher": {
                  "id": "byValue",
                  "options": {
                    "op": "gte",
                    "reducer": "allIsNull",
                    "value": 0
                  }
                },
                "properties": [
                  {
                    "id": "custom.hideFrom",
                    "value": {
                      "legend": true,
                      "tooltip": true,
                      "viz": false
                    }
                  }
                ]
              }
            ]
          },
          "gridPos": {
            "h": 8,
            "w": 12,
            "x": 0,
            "y": 55
          },
          "id": 61,
          "options": {
            "legend": {
              "calcs": ["mean"],
              "displayMode": "table",
              "placement": "right",
              "showLegend": true
            },
            "tooltip": {
              "mode": "multi",
              "sort": "none"
            }
          },
          "pluginVersion": "9.0.6",
          "targets": [
            {
              "datasource": {
                "type": "prometheus"
              },
              "expr": "mktxp_wlan_clients_tx_ccq{routerboard_address=\"$node\"}",
              "instant": false,
              "interval": "",
              "legendFormat": "{{dhcp_name}}",
              "refId": "A"
            }
          ],
          "title": "WLAN Clients Tx CCQ",
          "type": "timeseries"
        },
        {
          "datasource": {
            "default": true,
            "type": "prometheus",
            "uid": "PBFA97CFB590B2093"
          },
          "description": "",
          "fieldConfig": {
            "defaults": {
              "color": {
                "mode": "palette-classic"
              },
              "custom": {
                "axisBorderShow": false,
                "axisCenteredZero": false,
                "axisColorMode": "text",
                "axisLabel": "",
                "axisPlacement": "auto",
                "barAlignment": 0,
                "barWidthFactor": 0.6,
                "drawStyle": "line",
                "fillOpacity": 30,
                "gradientMode": "none",
                "hideFrom": {
                  "legend": false,
                  "tooltip": false,
                  "viz": false
                },
                "insertNulls": false,
                "lineInterpolation": "linear",
                "lineWidth": 1,
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
                  "mode": "off"
                }
              },
              "links": [],
              "mappings": [],
              "thresholds": {
                "mode": "absolute",
                "steps": [
                  {
                    "color": "green",
                    "value": null
                  },
                  {
                    "color": "red",
                    "value": 80
                  }
                ]
              },
              "unit": "bps"
            },
            "overrides": [
              {
                "matcher": {
                  "id": "byName",
                  "options": "Incoming traffic on interface ether1-gateway"
                },
                "properties": [
                  {
                    "id": "color",
                    "value": {
                      "fixedColor": "#1F78C1",
                      "mode": "fixed"
                    }
                  }
                ]
              },
              {
                "matcher": {
                  "id": "byName",
                  "options": "Outgoing traffic on interface ether1-gateway"
                },
                "properties": [
                  {
                    "id": "color",
                    "value": {
                      "fixedColor": "#EAB839",
                      "mode": "fixed"
                    }
                  }
                ]
              },
              {
                "matcher": {
                  "id": "byRegexp",
                  "options": "/Out/"
                },
                "properties": [
                  {
                    "id": "color",
                    "value": {
                      "fixedColor": "#EAB839",
                      "mode": "fixed"
                    }
                  },
                  {
                    "id": "custom.transform",
                    "value": "negative-Y"
                  }
                ]
              },
              {
                "matcher": {
                  "id": "byValue",
                  "options": {
                    "op": "gte",
                    "reducer": "allIsZero",
                    "value": 0
                  }
                },
                "properties": [
                  {
                    "id": "custom.hideFrom",
                    "value": {
                      "legend": true,
                      "tooltip": true,
                      "viz": false
                    }
                  }
                ]
              }
            ]
          },
          "gridPos": {
            "h": 8,
            "w": 12,
            "x": 12,
            "y": 55
          },
          "id": 63,
          "options": {
            "legend": {
              "calcs": [],
              "displayMode": "table",
              "placement": "right",
              "showLegend": true
            },
            "tooltip": {
              "mode": "multi",
              "sort": "desc"
            }
          },
          "pluginVersion": "9.0.6",
          "targets": [
            {
              "application": {
                "filter": "Network"
              },
              "datasource": {
                "type": "prometheus"
              },
              "editorMode": "code",
              "expr": "rate(mktxp_wlan_clients_tx_bytes_total{routerboard_address=\"$node\"}[$__rate_interval]) * 8",
              "format": "time_series",
              "functions": [],
              "group": {
                "filter": "Network"
              },
              "hide": false,
              "host": {
                "filter": "MikroTik Router"
              },
              "instant": false,
              "interval": "",
              "intervalFactor": 1,
              "item": {
                "filter": "Incoming traffic on interface ether1-gateway"
              },
              "legendFormat": "In - {{ dhcp_name }}",
              "mode": 0,
              "options": {
                "showDisabledItems": false
              },
              "refId": "A"
            },
            {
              "application": {
                "filter": "Network"
              },
              "datasource": {
                "type": "prometheus"
              },
              "editorMode": "code",
              "expr": "rate(mktxp_wlan_clients_rx_bytes_total{routerboard_address=\"$node\"}[$__rate_interval]) * 8",
              "format": "time_series",
              "functions": [],
              "group": {
                "filter": "Network"
              },
              "hide": false,
              "host": {
                "filter": "MikroTik Router"
              },
              "interval": "",
              "intervalFactor": 1,
              "item": {
                "filter": "Outgoing traffic on interface ether1-gateway"
              },
              "legendFormat": "Out - {{ dhcp_name }}",
              "mode": 0,
              "options": {
                "showDisabledItems": false
              },
              "range": true,
              "refId": "B"
            }
          ],
          "title": "Clients Traffic",
          "type": "timeseries"
        },
        {
          "datasource": {
            "type": "prometheus"
          },
          "fieldConfig": {
            "defaults": {
              "color": {
                "mode": "palette-classic"
              },
              "custom": {
                "axisBorderShow": false,
                "axisCenteredZero": false,
                "axisColorMode": "text",
                "axisLabel": "",
                "axisPlacement": "auto",
                "barAlignment": 0,
                "barWidthFactor": 0.6,
                "drawStyle": "line",
                "fillOpacity": 0,
                "gradientMode": "none",
                "hideFrom": {
                  "legend": false,
                  "tooltip": false,
                  "viz": false
                },
                "insertNulls": false,
                "lineInterpolation": "linear",
                "lineWidth": 1,
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
              "links": [],
              "mappings": [],
              "thresholds": {
                "mode": "absolute",
                "steps": [
                  {
                    "color": "green",
                    "value": null
                  },
                  {
                    "color": "red",
                    "value": 80
                  }
                ]
              },
              "unit": "dB"
            },
            "overrides": []
          },
          "gridPos": {
            "h": 7,
            "w": 12,
            "x": 0,
            "y": 63
          },
          "id": 65,
          "options": {
            "legend": {
              "calcs": ["mean"],
              "displayMode": "list",
              "placement": "right",
              "showLegend": true
            },
            "tooltip": {
              "mode": "multi",
              "sort": "desc"
            }
          },
          "pluginVersion": "9.0.6",
          "targets": [
            {
              "application": {
                "filter": "Network"
              },
              "datasource": {
                "type": "prometheus"
              },
              "expr": "mktxp_wlan_clients_signal_strength{routerboard_address=\"$node\"}",
              "format": "time_series",
              "functions": [],
              "group": {
                "filter": "Network"
              },
              "hide": false,
              "host": {
                "filter": "MikroTik Router"
              },
              "instant": false,
              "interval": "",
              "intervalFactor": 1,
              "item": {
                "filter": "Incoming traffic on interface ether1-gateway"
              },
              "legendFormat": "{{ dhcp_name }}",
              "mode": 0,
              "options": {
                "showDisabledItems": false
              },
              "refId": "A"
            }
          ],
          "title": "Clients Signal Strength",
          "type": "timeseries"
        },
        {
          "datasource": {
            "type": "prometheus"
          },
          "fieldConfig": {
            "defaults": {
              "color": {
                "mode": "palette-classic"
              },
              "custom": {
                "axisBorderShow": false,
                "axisCenteredZero": false,
                "axisColorMode": "text",
                "axisLabel": "",
                "axisPlacement": "auto",
                "barAlignment": 0,
                "barWidthFactor": 0.6,
                "drawStyle": "line",
                "fillOpacity": 0,
                "gradientMode": "none",
                "hideFrom": {
                  "legend": false,
                  "tooltip": false,
                  "viz": false
                },
                "insertNulls": false,
                "lineInterpolation": "linear",
                "lineWidth": 1,
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
              "links": [],
              "mappings": [],
              "thresholds": {
                "mode": "absolute",
                "steps": [
                  {
                    "color": "green",
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
            "h": 7,
            "w": 12,
            "x": 12,
            "y": 63
          },
          "id": 66,
          "options": {
            "legend": {
              "calcs": ["mean"],
              "displayMode": "table",
              "placement": "right",
              "showLegend": true
            },
            "tooltip": {
              "mode": "multi",
              "sort": "desc"
            }
          },
          "pluginVersion": "9.0.6",
          "targets": [
            {
              "application": {
                "filter": "Network"
              },
              "datasource": {
                "type": "prometheus"
              },
              "expr": "mktxp_wlan_clients_signal_to_noise{routerboard_address=\"$node\"}",
              "format": "time_series",
              "functions": [],
              "group": {
                "filter": "Network"
              },
              "hide": false,
              "host": {
                "filter": "MikroTik Router"
              },
              "instant": false,
              "interval": "",
              "intervalFactor": 1,
              "item": {
                "filter": "Incoming traffic on interface ether1-gateway"
              },
              "legendFormat": "{{ dhcp_name }}",
              "mode": 0,
              "options": {
                "showDisabledItems": false
              },
              "refId": "A"
            }
          ],
          "title": "Clients  Signal-to-Noise ",
          "type": "timeseries"
        }
      ],
      "targets": [
        {
          "datasource": {
            "type": "prometheus"
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
        "type": "prometheus"
      },
      "gridPos": {
        "h": 1,
        "w": 24,
        "x": 0,
        "y": 39
      },
      "id": 33,
      "panels": [
        {
          "datasource": {
            "type": "prometheus"
          },
          "fieldConfig": {
            "defaults": {
              "custom": {
                "align": "center",
                "cellOptions": {
                  "type": "auto"
                },
                "filterable": false,
                "inspect": false
              },
              "decimals": 2,
              "mappings": [],
              "thresholds": {
                "mode": "absolute",
                "steps": [
                  {
                    "color": "green",
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
            "overrides": [
              {
                "matcher": {
                  "id": "byName",
                  "options": "board"
                },
                "properties": [
                  {
                    "id": "custom.width",
                    "value": 189
                  }
                ]
              },
              {
                "matcher": {
                  "id": "byName",
                  "options": "identity"
                },
                "properties": [
                  {
                    "id": "custom.width",
                    "value": 103
                  }
                ]
              },
              {
                "matcher": {
                  "id": "byName",
                  "options": "version"
                },
                "properties": [
                  {
                    "id": "custom.width",
                    "value": 110
                  }
                ]
              }
            ]
          },
          "gridPos": {
            "h": 7,
            "w": 6,
            "x": 0,
            "y": 40
          },
          "id": 35,
          "options": {
            "cellHeight": "sm",
            "footer": {
              "countRows": false,
              "fields": "",
              "reducer": ["sum"],
              "show": false
            },
            "showHeader": true,
            "sortBy": []
          },
          "pluginVersion": "11.2.0",
          "targets": [
            {
              "datasource": {
                "type": "prometheus"
              },
              "expr": "mktxp_capsman_remote_caps_info{routerboard_address=\"$node\"}",
              "format": "table",
              "instant": true,
              "interval": "",
              "legendFormat": "{{identity}}",
              "refId": "A"
            }
          ],
          "title": "Remote Caps",
          "transformations": [
            {
              "id": "organize",
              "options": {
                "excludeByName": {
                  "Time": true,
                  "Value": true,
                  "__name__": true,
                  "instance": true,
                  "job": true,
                  "routerboard_address": true,
                  "routerboard_name": true
                },
                "indexByName": {
                  "Time": 0,
                  "Value": 10,
                  "__name__": 1,
                  "base_mac": 4,
                  "board": 3,
                  "identity": 2,
                  "instance": 5,
                  "job": 6,
                  "routerboard_address": 7,
                  "routerboard_name": 8,
                  "version": 9
                },
                "renameByName": {}
              }
            }
          ],
          "type": "table"
        },
        {
          "datasource": {
            "type": "prometheus"
          },
          "fieldConfig": {
            "defaults": {
              "color": {
                "mode": "fixed"
              },
              "custom": {
                "align": "center",
                "cellOptions": {
                  "type": "auto"
                },
                "filterable": false,
                "inspect": false
              },
              "mappings": [],
              "thresholds": {
                "mode": "absolute",
                "steps": [
                  {
                    "color": "green",
                    "value": null
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
                  "options": "__name__"
                },
                "properties": [
                  {
                    "id": "displayName"
                  }
                ]
              },
              {
                "matcher": {
                  "id": "byName",
                  "options": "rx_signal"
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
                  "options": "name"
                },
                "properties": [
                  {
                    "id": "custom.width",
                    "value": 267
                  }
                ]
              },
              {
                "matcher": {
                  "id": "byName",
                  "options": "mac_address"
                },
                "properties": [
                  {
                    "id": "custom.width",
                    "value": 165
                  }
                ]
              },
              {
                "matcher": {
                  "id": "byName",
                  "options": "ssid"
                },
                "properties": [
                  {
                    "id": "custom.width",
                    "value": 140
                  }
                ]
              }
            ]
          },
          "gridPos": {
            "h": 15,
            "w": 18,
            "x": 6,
            "y": 40
          },
          "id": 41,
          "options": {
            "cellHeight": "sm",
            "footer": {
              "countRows": false,
              "fields": "",
              "reducer": ["sum"],
              "show": false
            },
            "showHeader": true,
            "sortBy": [
              {
                "desc": true,
                "displayName": "rx_signal"
              }
            ]
          },
          "pluginVersion": "11.2.0",
          "targets": [
            {
              "datasource": {
                "type": "prometheus"
              },
              "expr": "mktxp_capsman_clients_devices_info{routerboard_address=\"$node\"}",
              "format": "table",
              "instant": true,
              "interval": "",
              "legendFormat": "",
              "refId": "A"
            }
          ],
          "title": "CAPsMAN Clients",
          "transformations": [
            {
              "id": "organize",
              "options": {
                "excludeByName": {
                  "Time": true,
                  "Value": true,
                  "__name__": true,
                  "instance": true,
                  "job": true,
                  "routerboard_address": true,
                  "routerboard_name": true
                },
                "indexByName": {
                  "Time": 0,
                  "Value": 15,
                  "__name__": 1,
                  "dhcp_address": 3,
                  "dhcp_name": 2,
                  "instance": 9,
                  "interface": 10,
                  "job": 12,
                  "mac_address": 4,
                  "routerboard_address": 13,
                  "routerboard_name": 14,
                  "rx_rate": 6,
                  "rx_signal": 5,
                  "ssid": 11,
                  "tx_rate": 7,
                  "uptime": 8
                },
                "renameByName": {}
              }
            }
          ],
          "type": "table"
        },
        {
          "datasource": {
            "type": "prometheus"
          },
          "description": "",
          "fieldConfig": {
            "defaults": {
              "decimals": 0,
              "links": [],
              "mappings": [],
              "min": 1,
              "thresholds": {
                "mode": "absolute",
                "steps": [
                  {
                    "color": "green"
                  },
                  {
                    "color": "#EAB839",
                    "value": 30
                  },
                  {
                    "color": "red",
                    "value": 80
                  }
                ]
              }
            },
            "overrides": []
          },
          "gridPos": {
            "h": 9,
            "w": 6,
            "x": 0,
            "y": 47
          },
          "id": 47,
          "options": {
            "displayMode": "lcd",
            "minVizHeight": 10,
            "minVizWidth": 0,
            "orientation": "horizontal",
            "reduceOptions": {
              "calcs": ["mean"],
              "fields": "",
              "values": false
            },
            "showUnfilled": true,
            "text": {}
          },
          "pluginVersion": "9.0.6",
          "targets": [
            {
              "application": {
                "filter": "Network"
              },
              "datasource": {
                "type": "prometheus"
              },
              "expr": "mktxp_capsman_registrations_count{routerboard_address=\"$node\"}",
              "format": "time_series",
              "functions": [],
              "group": {
                "filter": "Network"
              },
              "hide": false,
              "host": {
                "filter": "MikroTik Router"
              },
              "instant": true,
              "interval": "",
              "intervalFactor": 1,
              "item": {
                "filter": "Incoming traffic on interface ether1-gateway"
              },
              "legendFormat": "{{ interface }}",
              "mode": 0,
              "options": {
                "showDisabledItems": false
              },
              "refId": "A"
            },
            {
              "datasource": {
                "type": "prometheus"
              },
              "expr": "sum(mktxp_capsman_registrations_count{routerboard_address=\"$node\"})",
              "instant": true,
              "interval": "",
              "legendFormat": "Total",
              "refId": "B"
            }
          ],
          "title": "CAPsMAN Registrations",
          "type": "bargauge"
        },
        {
          "datasource": {
            "type": "prometheus",
            "uid": "PBFA97CFB590B2093"
          },
          "fieldConfig": {
            "defaults": {
              "color": {
                "mode": "thresholds"
              },
              "custom": {
                "align": "auto",
                "cellOptions": {
                  "type": "auto"
                },
                "inspect": false
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
            "overrides": []
          },
          "gridPos": {
            "h": 8,
            "w": 18,
            "x": 6,
            "y": 55
          },
          "id": 104,
          "options": {
            "footer": {
              "fields": "",
              "reducer": ["sum"],
              "show": false
            },
            "showHeader": true
          },
          "pluginVersion": "9.0.6",
          "targets": [
            {
              "datasource": {
                "type": "prometheus",
                "uid": "PBFA97CFB590B2093"
              },
              "editorMode": "code",
              "exemplar": false,
              "expr": "mktxp_capsman_interfaces_info{routerboard_address=\"$node\"}",
              "format": "table",
              "instant": true,
              "legendFormat": "",
              "range": false,
              "refId": "A"
            }
          ],
          "title": "CAPsMAN Frequencies",
          "transformations": [
            {
              "id": "organize",
              "options": {
                "excludeByName": {
                  "Time": true,
                  "Value": true,
                  "__name__": true,
                  "instance": true,
                  "job": true,
                  "routerboard_address": true,
                  "routerboard_name": true
                },
                "indexByName": {
                  "Time": 6,
                  "Value": 12,
                  "__name__": 8,
                  "configuration": 5,
                  "current_channel": 1,
                  "current_registered_clients": 2,
                  "current_state": 3,
                  "instance": 7,
                  "job": 9,
                  "mac_address": 4,
                  "name": 0,
                  "routerboard_address": 10,
                  "routerboard_name": 11
                },
                "renameByName": {
                  "configuration": "",
                  "current_registered_clients": "registered_clients",
                  "current_state": "state",
                  "mac_address": ""
                }
              }
            }
          ],
          "type": "table"
        },
        {
          "datasource": {
            "type": "prometheus"
          },
          "fieldConfig": {
            "defaults": {
              "color": {
                "mode": "thresholds"
              },
              "links": [],
              "mappings": [],
              "thresholds": {
                "mode": "absolute",
                "steps": [
                  {
                    "color": "red"
                  },
                  {
                    "color": "orange",
                    "value": -80
                  },
                  {
                    "color": "purple",
                    "value": -70
                  },
                  {
                    "color": "green",
                    "value": -60
                  },
                  {
                    "color": "rgb(20, 104, 9)",
                    "value": -40
                  }
                ]
              },
              "unit": "dB"
            },
            "overrides": []
          },
          "gridPos": {
            "h": 16,
            "w": 6,
            "x": 0,
            "y": 56
          },
          "id": 48,
          "options": {
            "displayMode": "gradient",
            "minVizHeight": 10,
            "minVizWidth": 0,
            "orientation": "horizontal",
            "reduceOptions": {
              "calcs": ["lastNotNull"],
              "fields": "",
              "values": false
            },
            "showUnfilled": true,
            "text": {}
          },
          "pluginVersion": "9.0.6",
          "targets": [
            {
              "application": {
                "filter": "Network"
              },
              "datasource": {
                "type": "prometheus"
              },
              "expr": "mktxp_capsman_clients_signal_strength{routerboard_address=\"$node\"}",
              "format": "time_series",
              "functions": [],
              "group": {
                "filter": "Network"
              },
              "hide": false,
              "host": {
                "filter": "MikroTik Router"
              },
              "instant": true,
              "interval": "",
              "intervalFactor": 1,
              "item": {
                "filter": "Incoming traffic on interface ether1-gateway"
              },
              "legendFormat": "{{ dhcp_name }}",
              "mode": 0,
              "options": {
                "showDisabledItems": false
              },
              "refId": "A"
            }
          ],
          "title": "Registered Client Signal Strength",
          "type": "bargauge"
        },
        {
          "aliasColors": {},
          "autoMigrateFrom": "graph",
          "bars": false,
          "dashLength": 10,
          "dashes": false,
          "datasource": {
            "type": "prometheus"
          },
          "fieldConfig": {
            "defaults": {
              "links": [],
              "unit": "dB"
            },
            "overrides": []
          },
          "fill": 0,
          "fillGradient": 0,
          "gridPos": {
            "h": 9,
            "w": 18,
            "x": 6,
            "y": 63
          },
          "hiddenSeries": false,
          "id": 49,
          "legend": {
            "alignAsTable": true,
            "avg": true,
            "current": false,
            "hideEmpty": false,
            "hideZero": false,
            "max": false,
            "min": false,
            "rightSide": true,
            "show": true,
            "total": false,
            "values": true
          },
          "lines": true,
          "linewidth": 1,
          "nullPointMode": "null",
          "options": {
            "alertThreshold": true
          },
          "percentage": false,
          "pluginVersion": "9.0.6",
          "pointradius": 2,
          "points": false,
          "renderer": "flot",
          "seriesOverrides": [],
          "spaceLength": 10,
          "stack": false,
          "steppedLine": false,
          "targets": [
            {
              "application": {
                "filter": "Network"
              },
              "datasource": {
                "type": "prometheus"
              },
              "expr": "mktxp_capsman_clients_signal_strength{routerboard_address=\"$node\"}",
              "format": "time_series",
              "functions": [],
              "group": {
                "filter": "Network"
              },
              "hide": false,
              "host": {
                "filter": "MikroTik Router"
              },
              "instant": false,
              "interval": "",
              "intervalFactor": 1,
              "item": {
                "filter": "Incoming traffic on interface ether1-gateway"
              },
              "legendFormat": "{{ dhcp_name }}",
              "mode": 0,
              "options": {
                "showDisabledItems": false
              },
              "refId": "A"
            }
          ],
          "thresholds": [],
          "timeRegions": [],
          "title": "CAPsMan Clients Signal Strength",
          "tooltip": {
            "shared": true,
            "sort": 2,
            "value_type": "individual"
          },
          "type": "timeseries",
          "xaxis": {
            "mode": "time",
            "show": true,
            "values": []
          },
          "yaxes": [
            {
              "$$hashKey": "object:788",
              "format": "dB",
              "logBase": 1,
              "max": "-16",
              "min": "-80",
              "show": true
            },
            {
              "$$hashKey": "object:789",
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
            "Incoming traffic on interface ether1-gateway": "#1F78C1",
            "Outgoing traffic on interface ether1-gateway": "#EAB839"
          },
          "autoMigrateFrom": "graph",
          "bars": false,
          "dashLength": 10,
          "dashes": false,
          "datasource": {
            "type": "prometheus",
            "uid": "PBFA97CFB590B2093"
          },
          "editable": true,
          "error": false,
          "fieldConfig": {
            "defaults": {
              "links": []
            },
            "overrides": []
          },
          "fill": 3,
          "fillGradient": 0,
          "gridPos": {
            "h": 10,
            "w": 24,
            "x": 0,
            "y": 72
          },
          "hiddenSeries": false,
          "id": 39,
          "legend": {
            "alignAsTable": true,
            "avg": true,
            "current": false,
            "hideEmpty": false,
            "hideZero": true,
            "max": false,
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
          "paceLength": 10,
          "percentage": false,
          "pluginVersion": "9.0.6",
          "pointradius": 5,
          "points": false,
          "renderer": "flot",
          "seriesOverrides": [
            {
              "$$hashKey": "object:176",
              "alias": "/In/"
            },
            {
              "$$hashKey": "object:177",
              "alias": "/Out/",
              "color": "#EAB839",
              "transform": "negative-Y"
            }
          ],
          "spaceLength": 10,
          "stack": false,
          "steppedLine": false,
          "targets": [
            {
              "application": {
                "filter": "Network"
              },
              "datasource": {
                "type": "prometheus"
              },
              "expr": "rate(mktxp_capsman_clients_tx_bytes_total{routerboard_address=\"$node\"}[$__rate_interval]) * 8",
              "format": "time_series",
              "functions": [],
              "group": {
                "filter": "Network"
              },
              "hide": false,
              "host": {
                "filter": "MikroTik Router"
              },
              "instant": false,
              "interval": "",
              "intervalFactor": 1,
              "item": {
                "filter": "Incoming traffic on interface ether1-gateway"
              },
              "legendFormat": "In | {{ dhcp_name }}",
              "mode": 0,
              "options": {
                "showDisabledItems": false
              },
              "refId": "A"
            },
            {
              "application": {
                "filter": "Network"
              },
              "datasource": {
                "type": "prometheus"
              },
              "expr": "rate(mktxp_capsman_clients_rx_bytes_total{routerboard_address=\"$node\"}[$__rate_interval]) * 8",
              "format": "time_series",
              "functions": [],
              "group": {
                "filter": "Network"
              },
              "hide": false,
              "host": {
                "filter": "MikroTik Router"
              },
              "interval": "",
              "intervalFactor": 1,
              "item": {
                "filter": "Outgoing traffic on interface ether1-gateway"
              },
              "legendFormat": "Out | {{ dhcp_name }}",
              "mode": 0,
              "options": {
                "showDisabledItems": false
              },
              "refId": "B"
            }
          ],
          "thresholds": [],
          "timeRegions": [],
          "title": "CAPsMAN Clients Traffic",
          "tooltip": {
            "msResolution": false,
            "shared": true,
            "sort": 2,
            "value_type": "individual"
          },
          "type": "timeseries",
          "xaxis": {
            "mode": "time",
            "show": true,
            "values": []
          },
          "yaxes": [
            {
              "$$hashKey": "object:706",
              "format": "bps",
              "logBase": 1,
              "show": true
            },
            {
              "$$hashKey": "object:707",
              "format": "short",
              "logBase": 1,
              "show": false
            }
          ],
          "yaxis": {
            "align": false
          }
        }
      ],
      "targets": [
        {
          "datasource": {
            "type": "prometheus"
          },
          "refId": "A"
        }
      ],
      "title": "CAPsMAN",
      "type": "row"
    },
    {
      "collapsed": true,
      "gridPos": {
        "h": 1,
        "w": 24,
        "x": 0,
        "y": 40
      },
      "id": 148,
      "panels": [
        {
          "datasource": {
            "type": "prometheus",
            "uid": "PBFA97CFB590B2093"
          },
          "fieldConfig": {
            "defaults": {
              "color": {
                "mode": "palette-classic"
              },
              "custom": {
                "axisBorderShow": false,
                "axisCenteredZero": false,
                "axisColorMode": "text",
                "axisLabel": "",
                "axisPlacement": "auto",
                "barAlignment": 0,
                "drawStyle": "bars",
                "fillOpacity": 50,
                "gradientMode": "hue",
                "hideFrom": {
                  "legend": false,
                  "tooltip": false,
                  "viz": false
                },
                "insertNulls": false,
                "lineInterpolation": "smooth",
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
                    "color": "green"
                  },
                  {
                    "color": "red",
                    "value": 80
                  }
                ]
              },
              "unit": "bps",
              "unitScale": true
            },
            "overrides": []
          },
          "gridPos": {
            "h": 6,
            "w": 24,
            "x": 0,
            "y": 57
          },
          "id": 145,
          "options": {
            "legend": {
              "calcs": [],
              "displayMode": "list",
              "placement": "right",
              "showLegend": true
            },
            "tooltip": {
              "mode": "single",
              "sort": "none"
            }
          },
          "targets": [
            {
              "datasource": {
                "type": "prometheus",
                "uid": "PBFA97CFB590B2093"
              },
              "editorMode": "code",
              "expr": "mktxp_queue_simple_rates_download_total{routerboard_address=\"$node\"}",
              "instant": false,
              "legendFormat": "{{name}} (in)",
              "range": true,
              "refId": "A"
            },
            {
              "datasource": {
                "type": "prometheus",
                "uid": "PBFA97CFB590B2093"
              },
              "editorMode": "code",
              "expr": "-mktxp_queue_simple_rates_upload_total{routerboard_address=\"$node\"}",
              "hide": false,
              "instant": false,
              "legendFormat": "{{name}} (out)",
              "range": true,
              "refId": "B"
            }
          ],
          "title": "Data Rate",
          "type": "timeseries"
        },
        {
          "datasource": {
            "type": "prometheus",
            "uid": "PBFA97CFB590B2093"
          },
          "fieldConfig": {
            "defaults": {
              "color": {
                "mode": "palette-classic"
              },
              "custom": {
                "axisBorderShow": false,
                "axisCenteredZero": false,
                "axisColorMode": "text",
                "axisLabel": "",
                "axisPlacement": "auto",
                "barAlignment": 0,
                "drawStyle": "bars",
                "fillOpacity": 50,
                "gradientMode": "opacity",
                "hideFrom": {
                  "legend": false,
                  "tooltip": false,
                  "viz": false
                },
                "insertNulls": false,
                "lineInterpolation": "smooth",
                "lineStyle": {
                  "fill": "solid"
                },
                "lineWidth": 1,
                "pointSize": 5,
                "scaleDistribution": {
                  "type": "linear"
                },
                "showPoints": "auto",
                "spanNulls": true,
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
              "unit": "decbytes",
              "unitScale": true
            },
            "overrides": []
          },
          "gridPos": {
            "h": 6,
            "w": 24,
            "x": 0,
            "y": 63
          },
          "id": 144,
          "options": {
            "legend": {
              "calcs": [],
              "displayMode": "list",
              "placement": "right",
              "showLegend": true
            },
            "tooltip": {
              "mode": "single",
              "sort": "none"
            }
          },
          "targets": [
            {
              "datasource": {
                "type": "prometheus",
                "uid": "PBFA97CFB590B2093"
              },
              "editorMode": "code",
              "expr": "mktxp_queue_simple_bytes_download_total{routerboard_address=\"$node\"}",
              "instant": false,
              "legendFormat": "{{name}} (in)",
              "range": true,
              "refId": "A"
            },
            {
              "datasource": {
                "type": "prometheus",
                "uid": "PBFA97CFB590B2093"
              },
              "editorMode": "code",
              "expr": "- mktxp_queue_simple_bytes_upload_total{routerboard_address=\"$node\"}",
              "hide": false,
              "instant": false,
              "legendFormat": "{{name}} (out)",
              "range": true,
              "refId": "B"
            }
          ],
          "title": "Processed Bytes",
          "type": "timeseries"
        },
        {
          "datasource": {
            "type": "prometheus",
            "uid": "PBFA97CFB590B2093"
          },
          "fieldConfig": {
            "defaults": {
              "color": {
                "mode": "palette-classic"
              },
              "custom": {
                "axisBorderShow": false,
                "axisCenteredZero": false,
                "axisColorMode": "text",
                "axisLabel": "",
                "axisPlacement": "auto",
                "barAlignment": 0,
                "drawStyle": "bars",
                "fillOpacity": 50,
                "gradientMode": "hue",
                "hideFrom": {
                  "legend": false,
                  "tooltip": false,
                  "viz": false
                },
                "insertNulls": false,
                "lineInterpolation": "smooth",
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
                    "color": "green"
                  },
                  {
                    "color": "red",
                    "value": 80
                  }
                ]
              },
              "unit": "pps",
              "unitScale": true
            },
            "overrides": []
          },
          "gridPos": {
            "h": 6,
            "w": 24,
            "x": 0,
            "y": 69
          },
          "id": 147,
          "options": {
            "legend": {
              "calcs": [],
              "displayMode": "list",
              "placement": "right",
              "showLegend": true
            },
            "tooltip": {
              "mode": "single",
              "sort": "none"
            }
          },
          "targets": [
            {
              "datasource": {
                "type": "prometheus",
                "uid": "PBFA97CFB590B2093"
              },
              "editorMode": "code",
              "expr": "rate(mktxp_queue_simple_dropped_download_total{routerboard_address=\"$node\"}[$__rate_interval])",
              "instant": false,
              "legendFormat": "{{name}} (in)",
              "range": true,
              "refId": "A"
            },
            {
              "datasource": {
                "type": "prometheus",
                "uid": "PBFA97CFB590B2093"
              },
              "editorMode": "code",
              "expr": "- rate(mktxp_queue_simple_dropped_upload_total{routerboard_address=\"$node\"}[$__rate_interval])",
              "hide": false,
              "instant": false,
              "legendFormat": "{{name}} (out)",
              "range": true,
              "refId": "B"
            }
          ],
          "title": "Drop Rate",
          "type": "timeseries"
        },
        {
          "datasource": {
            "type": "prometheus",
            "uid": "PBFA97CFB590B2093"
          },
          "fieldConfig": {
            "defaults": {
              "color": {
                "mode": "palette-classic"
              },
              "custom": {
                "axisBorderShow": false,
                "axisCenteredZero": false,
                "axisColorMode": "text",
                "axisLabel": "",
                "axisPlacement": "auto",
                "barAlignment": 0,
                "drawStyle": "bars",
                "fillOpacity": 50,
                "gradientMode": "hue",
                "hideFrom": {
                  "legend": false,
                  "tooltip": false,
                  "viz": false
                },
                "insertNulls": false,
                "lineInterpolation": "smooth",
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
                    "color": "green"
                  },
                  {
                    "color": "red",
                    "value": 80
                  }
                ]
              },
              "unit": "bps",
              "unitScale": true
            },
            "overrides": []
          },
          "gridPos": {
            "h": 6,
            "w": 24,
            "x": 0,
            "y": 75
          },
          "id": 146,
          "options": {
            "legend": {
              "calcs": [],
              "displayMode": "list",
              "placement": "right",
              "showLegend": true
            },
            "tooltip": {
              "mode": "single",
              "sort": "none"
            }
          },
          "targets": [
            {
              "datasource": {
                "type": "prometheus",
                "uid": "PBFA97CFB590B2093"
              },
              "editorMode": "code",
              "expr": "rate(mktxp_queue_simple_queued_bytes_downloadd_total{routerboard_address=\"$node\"}[$__rate_interval]) * 8",
              "instant": false,
              "legendFormat": "{{name}} (in)",
              "range": true,
              "refId": "A"
            },
            {
              "datasource": {
                "type": "prometheus",
                "uid": "PBFA97CFB590B2093"
              },
              "editorMode": "code",
              "expr": "- rate(mktxp_queue_simple_queued_bytes_upload_total{routerboard_address=\"$node\"}[$__rate_interval]) * 8",
              "hide": false,
              "instant": false,
              "legendFormat": "{{name}} (out)",
              "range": true,
              "refId": "B"
            }
          ],
          "title": "Queue Rate",
          "type": "timeseries"
        }
      ],
      "title": "Simple Queues",
      "type": "row"
    },
    {
      "collapsed": true,
      "gridPos": {
        "h": 1,
        "w": 24,
        "x": 0,
        "y": 41
      },
      "id": 125,
      "panels": [
        {
          "datasource": {
            "type": "prometheus",
            "uid": "PBFA97CFB590B2093"
          },
          "fieldConfig": {
            "defaults": {
              "color": {
                "fixedColor": "dark-purple",
                "mode": "palette-classic"
              },
              "custom": {
                "axisLabel": "",
                "axisPlacement": "auto",
                "barAlignment": 0,
                "drawStyle": "line",
                "fillOpacity": 30,
                "gradientMode": "hue",
                "hideFrom": {
                  "legend": false,
                  "tooltip": false,
                  "viz": false
                },
                "lineInterpolation": "smooth",
                "lineWidth": 1,
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
                  "mode": "off"
                }
              },
              "mappings": [],
              "min": 0,
              "noValue": "-",
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
              "unit": "bps"
            },
            "overrides": [
              {
                "matcher": {
                  "id": "byName",
                  "options": "tx"
                },
                "properties": [
                  {
                    "id": "color",
                    "value": {
                      "fixedColor": "dark-purple",
                      "mode": "fixed"
                    }
                  }
                ]
              },
              {
                "matcher": {
                  "id": "byName",
                  "options": "rx"
                },
                "properties": [
                  {
                    "id": "color",
                    "value": {
                      "fixedColor": "dark-blue",
                      "mode": "fixed"
                    }
                  }
                ]
              }
            ]
          },
          "gridPos": {
            "h": 8,
            "w": 6,
            "x": 0,
            "y": 295
          },
          "id": 108,
          "options": {
            "legend": {
              "calcs": [],
              "displayMode": "list",
              "placement": "bottom",
              "showLegend": true
            },
            "tooltip": {
              "mode": "single",
              "sort": "none"
            }
          },
          "repeat": "interface_name",
          "repeatDirection": "h",
          "targets": [
            {
              "datasource": {
                "type": "prometheus",
                "uid": "PBFA97CFB590B2093"
              },
              "editorMode": "code",
              "expr": "(rate(mktxp_interface_rx_byte_total{routerboard_address=\"$node\", name=\"$interface_name\"}[$__rate_interval]) * 8)",
              "legendFormat": "rx",
              "range": true,
              "refId": "A"
            },
            {
              "datasource": {
                "type": "prometheus",
                "uid": "PBFA97CFB590B2093"
              },
              "editorMode": "code",
              "expr": "(rate(mktxp_interface_tx_byte_total{routerboard_address=\"$node\", name=\"$interface_name\"}[$__rate_interval]) * 8)",
              "hide": false,
              "legendFormat": "tx",
              "range": true,
              "refId": "D"
            }
          ],
          "title": "$interface_name",
          "type": "timeseries"
        }
      ],
      "title": "Interface Details",
      "type": "row"
    },
    {
      "collapsed": true,
      "datasource": {
        "type": "prometheus"
      },
      "gridPos": {
        "h": 1,
        "w": 24,
        "x": 0,
        "y": 42
      },
      "id": 80,
      "panels": [
        {
          "datasource": {
            "type": "prometheus",
            "uid": "PBFA97CFB590B2093"
          },
          "description": "The version of Python running the Prometheus exporter.",
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
                    "color": "green"
                  },
                  {
                    "color": "red",
                    "value": 80
                  }
                ]
              }
            },
            "overrides": []
          },
          "gridPos": {
            "h": 3,
            "w": 6,
            "x": 0,
            "y": 184
          },
          "id": 102,
          "options": {
            "colorMode": "value",
            "graphMode": "none",
            "justifyMode": "auto",
            "orientation": "auto",
            "reduceOptions": {
              "calcs": ["lastNotNull"],
              "fields": "",
              "values": false
            },
            "textMode": "name"
          },
          "pluginVersion": "9.0.6",
          "targets": [
            {
              "datasource": {
                "type": "prometheus",
                "uid": "PBFA97CFB590B2093"
              },
              "editorMode": "builder",
              "expr": "python_info",
              "legendFormat": "{{implementation}} {{version}}",
              "range": true,
              "refId": "A"
            }
          ],
          "title": "Python Version",
          "type": "stat"
        },
        {
          "aliasColors": {
            "Incoming traffic on interface ether1-gateway": "#1F78C1",
            "Outgoing traffic on interface ether1-gateway": "#EAB839"
          },
          "bars": false,
          "dashLength": 10,
          "dashes": false,
          "datasource": {
            "type": "prometheus"
          },
          "editable": true,
          "error": false,
          "fieldConfig": {
            "defaults": {
              "links": []
            },
            "overrides": []
          },
          "fill": 3,
          "fillGradient": 0,
          "gridPos": {
            "h": 8,
            "w": 18,
            "x": 6,
            "y": 184
          },
          "hiddenSeries": false,
          "id": 77,
          "legend": {
            "alignAsTable": true,
            "avg": true,
            "current": false,
            "hideEmpty": false,
            "hideZero": true,
            "max": false,
            "min": false,
            "rightSide": true,
            "show": true,
            "total": false,
            "values": true
          },
          "lines": true,
          "linewidth": 1,
          "links": [],
          "nullPointMode": "connected",
          "options": {
            "alertThreshold": true
          },
          "paceLength": 10,
          "percentage": false,
          "pluginVersion": "9.0.6",
          "pointradius": 5,
          "points": false,
          "renderer": "flot",
          "seriesOverrides": [
            {
              "$$hashKey": "object:176",
              "alias": "/In/"
            },
            {
              "$$hashKey": "object:177",
              "alias": "/Out/",
              "color": "#EAB839",
              "transform": "negative-Y"
            }
          ],
          "spaceLength": 10,
          "stack": false,
          "steppedLine": false,
          "targets": [
            {
              "application": {
                "filter": "Network"
              },
              "datasource": {
                "type": "prometheus"
              },
              "expr": "rate(mktxp_collection_time_total{routerboard_address=\"$node\"}[4m])",
              "format": "time_series",
              "functions": [],
              "group": {
                "filter": "Network"
              },
              "hide": false,
              "host": {
                "filter": "MikroTik Router"
              },
              "instant": false,
              "interval": "",
              "intervalFactor": 1,
              "item": {
                "filter": "Incoming traffic on interface ether1-gateway"
              },
              "legendFormat": "{{ name }}",
              "mode": 0,
              "options": {
                "showDisabledItems": false
              },
              "refId": "A"
            },
            {
              "datasource": {
                "type": "prometheus"
              },
              "expr": "sum(rate(mktxp_collection_time_total{routerboard_address=\"$node\"}[4m]))",
              "interval": "",
              "legendFormat": "Total",
              "refId": "B"
            }
          ],
          "thresholds": [],
          "timeRegions": [],
          "title": "MKTXP Collection Times",
          "tooltip": {
            "msResolution": false,
            "shared": true,
            "sort": 2,
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
              "$$hashKey": "object:706",
              "format": "ms",
              "logBase": 2,
              "show": true
            },
            {
              "$$hashKey": "object:707",
              "format": "short",
              "logBase": 2,
              "show": true
            }
          ],
          "yaxis": {
            "align": false
          }
        },
        {
          "datasource": {
            "type": "prometheus"
          },
          "fieldConfig": {
            "defaults": {
              "color": {
                "mode": "thresholds"
              },
              "links": [],
              "mappings": [],
              "thresholds": {
                "mode": "absolute",
                "steps": [
                  {
                    "color": "green"
                  },
                  {
                    "color": "yellow",
                    "value": 10
                  },
                  {
                    "color": "purple",
                    "value": 20
                  },
                  {
                    "color": "orange",
                    "value": 50
                  }
                ]
              },
              "unit": "ms"
            },
            "overrides": []
          },
          "gridPos": {
            "h": 13,
            "w": 6,
            "x": 0,
            "y": 187
          },
          "id": 78,
          "links": [],
          "options": {
            "displayMode": "gradient",
            "minVizHeight": 10,
            "minVizWidth": 0,
            "orientation": "horizontal",
            "reduceOptions": {
              "calcs": ["lastNotNull"],
              "fields": "",
              "values": false
            },
            "showUnfilled": true,
            "text": {}
          },
          "pluginVersion": "9.0.6",
          "targets": [
            {
              "application": {
                "filter": "Network"
              },
              "datasource": {
                "type": "prometheus"
              },
              "expr": "rate(mktxp_collection_time_total{routerboard_address=\"$node\"}[4m])  ",
              "format": "time_series",
              "functions": [],
              "group": {
                "filter": "Network"
              },
              "hide": false,
              "host": {
                "filter": "MikroTik Router"
              },
              "instant": true,
              "interval": "",
              "intervalFactor": 1,
              "item": {
                "filter": "Incoming traffic on interface ether1-gateway"
              },
              "legendFormat": "{{ name }}",
              "mode": 0,
              "options": {
                "showDisabledItems": false
              },
              "refId": "A"
            }
          ],
          "title": "MKTXP Collection Times",
          "type": "bargauge"
        },
        {
          "datasource": {
            "type": "prometheus",
            "uid": "PBFA97CFB590B2093"
          },
          "description": "Memory metrics about the Mikrotik Metric Exporter for Prometheus.",
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
                "lineInterpolation": "linear",
                "lineWidth": 1,
                "pointSize": 5,
                "scaleDistribution": {
                  "type": "linear"
                },
                "showPoints": "auto",
                "spanNulls": true,
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
              "unit": "decbytes"
            },
            "overrides": []
          },
          "gridPos": {
            "h": 8,
            "w": 9,
            "x": 6,
            "y": 192
          },
          "id": 98,
          "options": {
            "legend": {
              "calcs": [],
              "displayMode": "list",
              "placement": "bottom",
              "showLegend": true
            },
            "tooltip": {
              "mode": "single",
              "sort": "none"
            }
          },
          "targets": [
            {
              "datasource": {
                "type": "prometheus",
                "uid": "PBFA97CFB590B2093"
              },
              "editorMode": "builder",
              "expr": "process_resident_memory_bytes",
              "legendFormat": "{{__name__}}",
              "range": true,
              "refId": "A"
            },
            {
              "datasource": {
                "type": "prometheus",
                "uid": "PBFA97CFB590B2093"
              },
              "editorMode": "builder",
              "expr": "process_virtual_memory_bytes",
              "hide": false,
              "legendFormat": "{{__name__}}",
              "range": true,
              "refId": "B"
            }
          ],
          "title": "Memory Footprint",
          "type": "timeseries"
        },
        {
          "datasource": {
            "type": "prometheus",
            "uid": "PBFA97CFB590B2093"
          },
          "description": "The CPU usage caused by the Prometheus exporter process. This is NOT the overall CPU usage.",
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
                "lineInterpolation": "linear",
                "lineWidth": 1,
                "pointSize": 5,
                "scaleDistribution": {
                  "type": "linear"
                },
                "showPoints": "auto",
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
                    "color": "green"
                  },
                  {
                    "color": "yellow",
                    "value": 10
                  },
                  {
                    "color": "orange",
                    "value": 20
                  },
                  {
                    "color": "red",
                    "value": 30
                  }
                ]
              },
              "unit": "percent"
            },
            "overrides": []
          },
          "gridPos": {
            "h": 8,
            "w": 9,
            "x": 15,
            "y": 192
          },
          "id": 100,
          "options": {
            "legend": {
              "calcs": [],
              "displayMode": "list",
              "placement": "bottom",
              "showLegend": true
            },
            "tooltip": {
              "mode": "single",
              "sort": "none"
            }
          },
          "targets": [
            {
              "datasource": {
                "type": "prometheus",
                "uid": "PBFA97CFB590B2093"
              },
              "editorMode": "code",
              "expr": "rate(process_cpu_seconds_total[30s]) * 100",
              "legendFormat": "cpu_usage",
              "range": true,
              "refId": "A"
            }
          ],
          "title": "CPU Usage (%)",
          "type": "timeseries"
        }
      ],
      "targets": [
        {
          "datasource": {
            "type": "prometheus"
          },
          "refId": "A"
        }
      ],
      "title": "MKTXP Metrics",
      "type": "row"
    }
  ],
  "refresh": "5s",
  "schemaVersion": 39,
  "tags": ["mikrotik", "dashboard", "mktxp"],
  "templating": {
    "list": [
      {
        "current": {
          "selected": false,
          "text": "10.0.0.1",
          "value": "10.0.0.1"
        },
        "datasource": {
          "type": "prometheus",
          "uid": "PBFA97CFB590B2093"
        },
        "definition": "label_values(mktxp_system_identity_info, routerboard_address)",
        "hide": 0,
        "includeAll": false,
        "label": "node",
        "multi": false,
        "name": "node",
        "options": [],
        "query": {
          "query": "label_values(mktxp_system_identity_info, routerboard_address)",
          "refId": "Prometheus-node-Variable-Query"
        },
        "refresh": 1,
        "regex": "",
        "skipUrlSync": false,
        "sort": 1,
        "tagValuesQuery": "",
        "tagsQuery": "",
        "type": "query",
        "useTags": false
      },
      {
        "current": {
          "selected": true,
          "text": ["All"],
          "value": ["$__all"]
        },
        "datasource": {
          "type": "prometheus",
          "uid": "PBFA97CFB590B2093"
        },
        "definition": "mktxp_interface_rx_byte_total{routerboard_address=\"$node\"}",
        "hide": 0,
        "includeAll": true,
        "multi": true,
        "name": "interface_name",
        "options": [],
        "query": {
          "query": "mktxp_interface_rx_byte_total{routerboard_address=\"$node\"}",
          "refId": "StandardVariableQuery"
        },
        "refresh": 1,
        "regex": "/.*,name=\"([^\"]*).*/",
        "skipUrlSync": false,
        "sort": 1,
        "type": "query"
      }
    ]
  },
  "time": {
    "from": "now-1h",
    "to": "now"
  },
  "timepicker": {},
  "timezone": "",
  "title": "Mikrotik MKTXP Exporter",
  "uid": "0j4sdLm7z",
  "version": 12,
  "weekStart": ""
}


File: /grafana\provisioning\datasources\datasource.yml
  
apiVersion: 1

datasources:
  - name: Prometheus
    type: prometheus
    access: proxy
    orgId: 1
    url: http://prometheus:9090
    basicAuth: false
    isDefault: true
    editable: true


File: /LICENSE
MIT License

Copyright (c) 2021 Leon Morten Richter

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


File: /Makefile
.DEFAULT_GOAL := run

clean:
	docker compose down
	docker rm -f $(docker ps -a -q)
	docker volume rm "$(docker volume ls -q)"

run:
	docker compose up


File: /mktxp\mktxp.conf
## Copyright (c) 2020 Arseniy Kuznetsov
##
## This program is free software; you can redistribute it and/or
## modify it under the terms of the GNU General Public License
## as published by the Free Software Foundation; either version 2
## of the License, or (at your option) any later version.
##
## This program is distributed in the hope that it will be useful,
## but WITHOUT ANY WARRANTY; without even the implied warranty of
## MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
## GNU General Public License for more details.


[Sample-Router]
    # for specific configuration on the router level, change here the defaults values from below
    hostname = 192.168.88.1

[default]
    # this affects configuration of all routers, unless overloaded on their specific levels

    enabled = True          # turns metrics collection for this RouterOS device on / off
    hostname = localhost    # RouterOS IP address
    port = 8728             # RouterOS IP Port

    username = username     # RouterOS user, needs to have 'read' and 'api' permissions
    password = password

    use_ssl = False                 # enables connection via API-SSL servis
    no_ssl_certificate = False      # enables API_SSL connect without router SSL certificate
    ssl_certificate_verify = False  # turns SSL certificate verification on / off
    plaintext_login = True          # for legacy RouterOS versions below 6.43 use False

    installed_packages = True       # Installed packages
    dhcp = True                     # DHCP general metrics
    dhcp_lease = True               # DHCP lease metrics

    connections = True              # IP connections metrics
    connection_stats = False        # Open IP connections metrics

    interface = True                # Interfaces traffic metrics

    route = True                    # IPv4 Routes metrics
    pool = True                     # IPv4 Pool metrics
    firewall = True                 # IPv4 Firewall rules traffic metrics
    neighbor = True                 # IPv4 Reachable Neighbors

    ipv6_route = False              # IPv6 Routes metrics
    ipv6_pool = False               # IPv6 Pool metrics
    ipv6_firewall = False           # IPv6 Firewall rules traffic metrics
    ipv6_neighbor = False           # IPv6 Reachable Neighbors

    poe = True                      # POE metrics
    monitor = True                  # Interface monitor metrics
    netwatch = True                 # Netwatch metrics
    public_ip = True                # Public IP metrics
    wireless = True                 # WLAN general metrics
    wireless_clients = True         # WLAN clients metrics
    capsman = True                  # CAPsMAN general metrics
    capsman_clients = True          # CAPsMAN clients metrics

    lte = False                     # LTE signal and status metrics (requires additional 'test' permission policy on RouterOS v6)
    ipsec = False                   # IPSec active peer metrics
    switch_port = False             # Switch Port metrics

    kid_control_assigned = False    # Allow Kid Control metrics for connected devices with assigned users
    kid_control_dynamic = False     # Allow Kid Control metrics for all connected devices, including those without assigned user

    user = True                     # Active Users metrics
    queue = True                    # Queues metrics

    bgp = False                     # BGP sessions metrics

    remote_dhcp_entry = None        # An MKTXP entry to provide for remote DHCP info / resolution
    remote_capsman_entry = None     # An MKTXP entry to provide for remote capsman info

    use_comments_over_names = True  # when available, forces using comments over the interfaces names
    check_for_updates = False       # check for available ROS updates


File: /mktxp\_mktxp.conf
## Copyright (c) 2020 Arseniy Kuznetsov
##
## This program is free software; you can redistribute it and/or
## modify it under the terms of the GNU General Public License
## as published by the Free Software Foundation; either version 2
## of the License, or (at your option) any later version.
##
## This program is distributed in the hope that it will be useful,
## but WITHOUT ANY WARRANTY; without even the implied warranty of
## MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
## GNU General Public License for more details.


[MKTXP]
    listen = '0.0.0.0:49090'         # Space separated list of socket addresses to listen to, both IPV4 and IPV6
    socket_timeout = 5

    initial_delay_on_failure = 120
    max_delay_on_failure = 900
    delay_inc_div = 5

    bandwidth = False                # Turns metrics bandwidth metrics collection on / off
    bandwidth_test_interval = 600    # Interval for collecting bandwidth metrics
    minimal_collect_interval = 5     # Minimal metric collection interval

    verbose_mode = False             # Set it on for troubleshooting

    fetch_routers_in_parallel = False   # Fetch metrics from multiple routers in parallel / sequentially
    max_worker_threads = 5              # Max number of worker threads that can fetch routers (parallel fetch only)
    max_scrape_duration = 30            # Max duration of individual routers' metrics collection (parallel fetch only)
    total_max_scrape_duration = 90      # Max overall duration of all metrics collection (parallel fetch only)

    compact_default_conf_values = False  # Compact mktxp.conf, so only specific values are kept on the individual routers' level


File: /nginx\nginx.conf
server {
  listen 80;
	listen [::]:80;

  location / {
   proxy_set_header Host $http_host; 
   proxy_pass http://grafana:3000/;
  }
}


File: /nginx\self-signed.conf
ssl_certificate /etc/nginx/ssl/nginx-selfsigned.crt;
ssl_certificate_key /etc/nginx/ssl/nginx-selfsigned.key;


File: /prometheus\prometheus.yml
# my global config
global:
  scrape_interval:     120s # By default, scrape targets every 15 seconds.
  evaluation_interval: 120s # By default, scrape targets every 15 seconds.
  # scrape_timeout is set to the global default (10s).

  # Attach these labels to any time series or alerts when communicating with
  # external systems (federation, remote storage, Alertmanager).
  external_labels:
      monitor: 'mikrotik-monitoring'

# Load and evaluate rules in this file every 'evaluation_interval' seconds.
rule_files:
  # - "alert.rules"
  # - "first.rules"
  # - "second.rules"

# A scrape configuration containing exactly one endpoint to scrape:
# Here it's Prometheus itself.
scrape_configs:
  # The job name is added as a label `job=<job_name>` to any timeseries scraped from this config.
  - job_name: 'mikrotik'

    # Override the global default and scrape targets from this job every 5 seconds.
    scrape_interval: 15s

    # metrics_path defaults to '/metrics'
    # scheme defaults to 'http'.

    static_configs:
         - targets:
            - 'mktxp:49090'

  - job_name: 'blackbox'
    scrape_interval: 1s
    metrics_path: /probe
    params:
      module: [icmp_ttl5]  # use ICMP as the ping protocol
    static_configs:
      - targets:
        - 1.1.1.1
        - 8.8.8.8
        - 9.9.9.9
    relabel_configs:
      - source_labels: [__address__]
        target_label: __param_target
      - source_labels: [__param_target]
        target_label: instance
      - target_label: __address__
        replacement: blackbox:9115  # The blackbox exporter's real hostname:port.


File: /README.md
# Monitor your Mikrotik router with Prometheus and Grafana

Use Grafana & Prometheus to monitor Mikrotik devices. This projects serves as a ready to use blueprint for monitoring based on Docker. It is designed and tested to be run on Raspberry Pis.

## Features

- System Health Monitoring
  - disk usage
  - CPU load
  - memory usage
  - public IP address (IPv4 & IPv6)
  - system uptime
  - temperature
  - voltage monitoring
- Interface Monitoring
  - traffic (bit/s)
  - traffic (packets/s)
  - per interface graphs
- Latency Monitoring
  - customizable ICMP and/or UDP pings
  - packet loss
- DHCP Monitoring
  - active leases
  - MAC addresses, host names, addresses
- Network Monitoring
  - routes
  - interfaces errors
  - interface states
  - PoE states
- Firewall Monitoring
  - rules traffic
  - logged rules traffic
  - Ipv4 & IPv6
  - bandwidth
  - active users
- Wireless Monitoring
  - noise floor
  - TxCCQ
  - client devices
  - number of clients
  - traffic
  - signal strength
  - signal to noise ratio
- Netwatch
- CAPsMAN Monitoring
  - remote CAPS
  - registrations
  - clients
  - frequencies
  - signal strength
  - traffic

## Setup

- Router running RouterOS 7.x.x
- Raspberry Pi 4 with 2 gb RAM (other PIs may also work, but I wanted ARM 64 bit)
- before opening a new issue, please take a look at the [FAQ](#FAQ)

## Demo pictures

![General system stats](./doc/system.png)

<details><summary>Show more images</summary>

![Network](./doc/network.png)
![Latency](./doc/latency.png)
![Netwatch](./doc/netwatch.png)
![Firewall](./doc/firewall.png)
![WiFi](./doc/wifi.png)
![Interfaces](./doc/interfaces.png)

</details>

## Installation

## Mikrotik Router

At first you need to prepare your router.

Create a group on the device that has API and read-only access:

`/user group add name=prometheus policy=api,read,winbox,test`

Create a user that is part of the group:

`/user add name=prometheus group=prometheus password=TOP_SECRET`

## Prepare Raspi

You need Ubuntu Server for ARM 64 bit in order to use this setup. You may also use Raspian, but then you are limited to 32bit ARM executables. This would mean, that you need to compile the `mikrotik-exporter` by hand, because there are no pre built 32-bit Docker images.

You need to execute the following steps on the target machine itself (e.g. Raspberry Pi).

Install Docker ([official docs](https://docs.docker.com/engine/install/debian/)):

`sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin`

**:warning: Note:** `docker-compose` was originally written in Python, but it was deprecated some time ago. [Migrate to Compose V2](https://docs.docker.com/compose/migrate/).

<details>
<summary>Optional: Build the Docker Image for mktxp</summary>

It might be necessary to build the Docker Image for: https://github.com/akpw/mktxp.
This is especially the case, if your architecture is not:
- linux/amd64
- linux/arm/v7
- linux/arm64

```bash
# Get the mktxp repository
git clone https://github.com/akpw/mktxp.git

# Go into the newly downloaded repo
cd mktxp

# Build the docker image
docker build . -t leonmorten/mktxp:latest
```

</details>

Now get this repo and install all services:

```bash
# Clone this repo
git clone https://github.com/M0r13n/mikrotik_monitoring.git


# Go into the cloned directory
cd mikrotik_monitoring

# Let docker-compose do it's job
docker compose up -d
```

You may need to adjust the following configuration files and add your own credentials for your router:

- `mktxp/mktxp.conf`


Done. You should now be able to open the Grafana dashboard on Port 3000 of your Raspberry Pi.

## Latency Monitoring

This projects uses the Prometheus Blackbox exporter to measure network latency. By default three targets are configured:

- 1.1.1.1 (Cloudflare)
- 8.8.8.8 (Google)
- 9.9.9.9 (IBM)

You may adjust **blackbox/blackbox.yml** according to your needs.

## Multiple Nodes

It is possible to monitor multiple (Mikrotik) devices. Just change add as many devices to `mktxp/mktxp.conf` as you want.

## HTTPS

It is also possible to access the Grafana Dashboard over HTTPS.
Depending on your security requirements and/or threat model it might be a good idea to enable HTTPS.

Generate a self signed certificate for your domain:

`sudo openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout ./nginx/nginx-selfsigned.key -out ./nginx/nginx-selfsigned.crt`

Replace the content of `./nginx/nginx.conf` with:

```txt
server {
  listen 80;
	listen [::]:80;
	server_name _;
	return 301 https://$host$request_uri;
}

server {
  listen 443 ssl;
  listen [::]:443 ssl;
  include ssl/self-signed.conf;

  location / {
   proxy_set_header Host $http_host;
   proxy_pass http://grafana:3000/;
  }
}

```

## AppArmor

Under `./docker-armor` you can find an AppArmor profile for this stack. To use it, do the following:

```
cp ./docker-armor /etc/apparmor.d/docker-armor
apparmor_parser -r -W /etc/apparmor.d/docker-armor
docker compose -f docker-compose-armored.yml  up -d
```

## Resources

- [A blog post by Devin Smith that first got me interested](https://blog.devinsmith.co.za/home-internet-grafana-lockdown/)
- [A somewhat useable Grafana Dashboard](https://grafana.com/grafana/dashboards/10950)
- [A Prometheus exporter for Mikrotik devices written in Python](https://github.com/akpw/mktxp).
- [A Prometheus exporter for Mikrotik devices written in Go](https://github.com/nshttpd/mikrotik-exporter)
- [Prometheus Blackbox exporter](https://github.com/prometheus/blackbox_exporter/blob/master/example.yml)

## FAQ

### Why are my graphs empty?

It might happen that the Grafana dashboard loads, but the graphs remain empty. If the dashboard loads, but no data is shown, this may be caused by any of the following reasons:

- invalid credentials for the monitored RouterOS device
    - verify with: `/user/print detail`
- invalid host and port for the monitored RouterOS device
    - check that the IP or host name of the monitored device is correct
- API service disabled on the RouterOS device
    - verify with `/ip/service/print detail`

### What distinguishes this project from other similar projects?

This project is only a personal hobby.
It do it mainly to learn something and to improve my skills.
Therefore, the project does not compete with other projects.
Nor do I aim for completeness or perfection.
The goal of this project is to develop a monitoring solution for multiple RouterOS devices simultaneously that is resource-efficient and scalable.

### Why you don't use the SNMP for monitoring?

Firstly SNMP based monitoring is painfully slow.
In my experience SNMP walks are slow and CPU heavy.
And I am not [alone with this](https://forum.mikrotik.com/viewtopic.php?t=132304).
In my experience the API is much faster and produces less stress on the CPU of the monitored device.

Secondly I never really got used to the way that SNMP metrics and queries are structured.
I find them very hard to read.

In addition, the API offers a lot of flexibility.
Any command can be executed on RouterOS via the API.
Thus it is possible to collect complex metrics.

### I get a PermissionError when running docker-compose up

When bind-mounting a directory from the host into a container, files and directories
maintain the permissions they **have on the host**. These can not be changed by Docker.
Typically, a bind-mounted directory has permissions like these: `rwxrwxr-x`.
This means that the container can read from the bind-mounted directory. But it can not
write or modify the mounted files.

This mostly works fine. But the Prometheus exporter mktxp has a specialty:
It may update it's configuration if some keys are missing from the configuration file.
Imagine, that the key `ipv6_firewall` is missing from the **mktxp.conf**. In this case
mktxp will add `ipv6_firewall=false` to the configuration file instead of failing.
This is a helpful feature, but can cause the container to crash, if the user inside
the container lacks write permissions.

In order to resolve this issue, make sure that all keys that mktxp currently supports
are listed in your **mktxp.conf** file.


