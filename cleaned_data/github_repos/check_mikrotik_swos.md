# Repository Information
Name: check_mikrotik_swos

# Directory Structure
Directory structure:
└── github_repos/check_mikrotik_swos/
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
    │   │       ├── pack-fb5ff9ea29e28c3c907539cf85c51931e03b0eb1.idx
    │   │       └── pack-fb5ff9ea29e28c3c907539cf85c51931e03b0eb1.pack
    │   ├── packed-refs
    │   └── refs/
    │       ├── heads/
    │       │   └── main
    │       ├── remotes/
    │       │   └── origin/
    │       │       └── HEAD
    │       └── tags/
    ├── check_mikrotik_swos
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
	url = https://github.com/nickjeffrey/check_mikrotik_swos.git
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
0000000000000000000000000000000000000000 90484e1501ec159325c12c453a7a85fd30c2c658 vivek-dodia <vivek.dodia@icloud.com> 1738606420 -0500	clone: from https://github.com/nickjeffrey/check_mikrotik_swos.git


File: /.git\logs\refs\heads\main
0000000000000000000000000000000000000000 90484e1501ec159325c12c453a7a85fd30c2c658 vivek-dodia <vivek.dodia@icloud.com> 1738606420 -0500	clone: from https://github.com/nickjeffrey/check_mikrotik_swos.git


File: /.git\logs\refs\remotes\origin\HEAD
0000000000000000000000000000000000000000 90484e1501ec159325c12c453a7a85fd30c2c658 vivek-dodia <vivek.dodia@icloud.com> 1738606420 -0500	clone: from https://github.com/nickjeffrey/check_mikrotik_swos.git


File: /.git\packed-refs
# pack-refs with: peeled fully-peeled sorted 
90484e1501ec159325c12c453a7a85fd30c2c658 refs/remotes/origin/main


File: /.git\refs\heads\main
90484e1501ec159325c12c453a7a85fd30c2c658


File: /.git\refs\remotes\origin\HEAD
ref: refs/remotes/origin/main


File: /check_mikrotik_swos
#!/usr/bin/perl -w

#OUTSTANDING TASKS
#-----------------
#  Add more performance data details to the output  (ie fan speeds)
#  Add port up/down status for ports specified as important


# CHANGE LOG
# ----------
# 2021/06/17	njeffrey	Script created to monitor MikroTik devices running SwitchOS (not RouterOS)
# 2021/06/18	njeffrey	Ad support for model CSS106-1G-4P-1S
# 2021/07/20	njeffrey	Ad support for model CRS305-1G-4S+


# nagios shell script to query MikroTik devices running SwitchOS (not RouterOS) via SNMP


# NOTES
# -----
#
#  This script should return one (and only one) line of ouput.  Multiple
#  lines of output are silently ignored by nagios.
#
#  The line of output will become the body of the alert message sent by nagios
#
#
#  This script queries a remote host via SNMP
#
#  You will need a section in the services.cfg
#  file on the nagios server that looks similar to the following.
#      # Define a service to check MikroTik devices running SwitchOL (not RouterOS)
#      # Parameters are SNMP community name
#      define service {
#              use                             generic-service
#              hostgroup_name                  all_mikrotik_swos
#              service_description             MikroTik SwOS
#              check_command                   check_mikrotik_swos!public
#              }
#
#
#  You will also need a command definition similar to the following in commands.cfg on the nagios server
#      # 'check_mikrotik_swos' command definition
#      # parameters are -H hostname -C snmp_community
#      define command{
#              command_name    check_mikrotik_swos
#              command_line    $USER1$/check_mikrotik_swos -H $HOSTADDRESS$ -C $ARG1$
#              }
#
#


# Different MikroTik devices may use slightly different OID values because they differ in number of ports, fans, power supplies, etc.
#
# .1.3.6.1.2.1.1.1.0 = STRING: CSS106-1G-4P-1S SwOS v2.13	Model number and firmware level
# .1.3.6.1.2.1.1.3.0 = Timeticks: (5218548) 14:29:45.48`	Uptime.  Value in brackets is inhundredths of seconds, followed by hh:mm:ss.##
# .1.3.6.1.2.1.1.5.0 = STRING: switch2				Hostname
#
# Number of ports and port descriptions
# .1.3.6.1.2.1.2.2.1.1.1 = INTEGER: 1
# .1.3.6.1.2.1.2.2.1.1.2 = INTEGER: 2
# .1.3.6.1.2.1.2.2.1.1.3 = INTEGER: 3
# .1.3.6.1.2.1.2.2.1.1.4 = INTEGER: 4
# .1.3.6.1.2.1.2.2.1.1.5 = INTEGER: 5
# .1.3.6.1.2.1.2.2.1.1.6 = INTEGER: 6
# .1.3.6.1.2.1.2.2.1.2.1 = STRING: Port1
# .1.3.6.1.2.1.2.2.1.2.2 = STRING: Port2
# .1.3.6.1.2.1.2.2.1.2.3 = STRING: Port3
# .1.3.6.1.2.1.2.2.1.2.4 = STRING: Port4
# .1.3.6.1.2.1.2.2.1.2.5 = STRING: Port5
# .1.3.6.1.2.1.2.2.1.2.6 = STRING: SFP
#
# Interface administrative status
# .1.3.6.1.2.1.2.2.1.7.1 = INTEGER: up(1)
# .1.3.6.1.2.1.2.2.1.7.2 = INTEGER: up(1)
# .1.3.6.1.2.1.2.2.1.7.3 = INTEGER: up(1)
# .1.3.6.1.2.1.2.2.1.7.4 = INTEGER: up(1)
# .1.3.6.1.2.1.2.2.1.7.5 = INTEGER: up(1)
# .1.3.6.1.2.1.2.2.1.7.6 = INTEGER: up(1)
#
# Interface operational status
# .1.3.6.1.2.1.2.2.1.8.1 = INTEGER: up(1)
# .1.3.6.1.2.1.2.2.1.8.2 = INTEGER: up(1)
# .1.3.6.1.2.1.2.2.1.8.3 = INTEGER: up(1)
# .1.3.6.1.2.1.2.2.1.8.4 = INTEGER: up(1)
# .1.3.6.1.2.1.2.2.1.8.5 = INTEGER: up(1)
# .1.3.6.1.2.1.2.2.1.8.6 = INTEGER: down(2)
#
#.1.3.6.1.4.1.14988.1.1.3.8.0 = INTEGER: 236 			Voltage from power supply in tenths of volts
#.1.3.6.1.4.1.14988.1.1.3.10.0 = INTEGER: 430			Board temperature in tenths of degrees Celsius for model CSS106-1G-4P-1S
#.1.3.6.1.4.1.14988.1.1.3.11.0 = INTEGER: 430			Board temperature in tenths of degrees Celsius for model CRS305-1G-4S+
#
#
# Milliamps of current draw from PoE devices on each port
# .1.3.6.1.4.1.14988.1.1.15.1.1.5.2 = INTEGER: 0
# .1.3.6.1.4.1.14988.1.1.15.1.1.5.3 = INTEGER: 158
# .1.3.6.1.4.1.14988.1.1.15.1.1.5.4 = INTEGER: 150
# .1.3.6.1.4.1.14988.1.1.15.1.1.5.5 = INTEGER: 0
#
# Tenths of Watts of power draw from PoE devices on each port
# .1.3.6.1.4.1.14988.1.1.15.1.1.6.2 = INTEGER: 0
# .1.3.6.1.4.1.14988.1.1.15.1.1.6.3 = INTEGER: 37
# .1.3.6.1.4.1.14988.1.1.15.1.1.6.4 = INTEGER: 35
# .1.3.6.1.4.1.14988.1.1.15.1.1.6.5 = INTEGER: 0


use strict;				#enforce good coding practices
use Getopt::Long;                       #allow --long-switches to be used as parameters.  Install with: perl -MCPAN -e 'install Getopt::Long'



# declare variables
my ($OK,$WARN,$CRITICAL,$UNKNOWN);
my ($CHECK_NAME,$cmd,$snmpwalk,$snmpget);
my ($host,$oid,$key,%mikrotik,$community);
my ($cpu_temp_crit,$cpu_temp_warn,$pingstatus);
my ($opt_h,$opt_v,$opt_w,$opt_c,$opt_C,$opt_H);
my ($verbose,$output_details,$perf_data);
$cmd = "";                                              #initialize variable
$CHECK_NAME                 = "MikroTik SwOS";		#name of nagios check
$verbose                    = "no";                    	#yes/no variable to increase output for debugging
$cpu_temp_warn              = 60;			#warn if CPU temperature reaches this value in degrees celsius
$cpu_temp_crit              = 65;			#critical if CPU temperature reaches this value in degrees celsius
$community                  = "public";  		#default SNMP community name
$output_details             = "";			#initialize variable to hold details of script output
$snmpwalk                   = "/usr/bin/snmpwalk";	#location of binary
$snmpget                    = "/usr/bin/snmpget";	#location of binary
#
# Nagios return codes
#
$OK=            0;
$WARN=          1;
$CRITICAL=      2;
$UNKNOWN=       3;




sub get_options {
   #
   # this gets the command line parameters provided by the users
   #
   print "running get_options subroutine \n" if ($verbose eq "yes");
   #
   Getopt::Long::Configure('bundling');
   GetOptions(
      "h"   => \$opt_h, "help"        => \$opt_h,
      "v"   => \$opt_v, "verbose"     => \$opt_v,
      "C=s" => \$opt_C, "community=s" => \$opt_C, "comm=s" => \$opt_C,
      "H=s" => \$opt_H, "hostname=s"  => \$opt_H, "host=s" => \$opt_H,
   );
   #
   #
   #
   # If the user supplied -h or --help, generate the help messages
   #
   if( defined( $opt_h ) ) {
      print "Nagios plugin for determining filesystem usage. \n";
      print "Examples: \n";
      print "   $0 --host=myhost --community=public \n";
      print "   $0     -H myhost          -C public \n";
      print "\n\n";
      exit $UNKNOWN;
   }
   #
   # If the user supplied -v or --verbose, increase verbosity for debugging
   if( defined( $opt_v ) ) {
      $verbose = "yes";
   } 
   #
   #
   # If the user did not supply a --community SNMP community string, use "public"
   #
   if( defined( $opt_C ) ) {
      $community = $opt_C;
   } else {
      $community = "public";
   }
   #
   # If the user did not supply a --host=??? , generate a warning
   #
   if( defined( $opt_H ) ) {
      $host = $opt_H;
   } else {
      print "$CHECK_NAME UNKNOWN - a remote host to check was not provided. Use this syntax: $0 -H hostname -C snmp_community\n";
      exit $CRITICAL;                                           #exit script
   }
   #
   print "host=$host community=$community \n" if ($verbose eq "yes");
}                       #end of subroutine





sub sanity_checks {
   #
   print "running sanity_checks subroutine \n" if ($verbose eq "yes");
   #
   if ( ! -f "$snmpwalk" ) {
      print "ERROR: Cannot find $snmpwalk \n";
      exit;
   }
   if ( ! -x "$snmpwalk" ) {
      print "ERROR: $snmpwalk is not executable by the current user\n";
      exit;
   }
   if ( ! -f "$snmpget" ) {
      print "ERROR: Cannot find $snmpget \n";
      exit;
   }
   if ( ! -x "$snmpget" ) {
      print "ERROR: $snmpget is not executable by the current user\n";
      exit;
   }
   #
   #
   # confirm a remote host is defined
   if( ! defined( $host ) ) {
      print "$CHECK_NAME Unknown - missing name of remote host to check.  Use $0 -h for help\n";
      exit $UNKNOWN;                                    #exit script
   }
   #
   #
   #
   # Confirm the remote host is up
   #
   print "   trying to ping $host \n" if ($verbose eq "yes");
   open(IN,"ping -c 1 -w 1 $host 2>&1 |");     #send a single ping to the remote host and wait 1 second for a reply
   while (<IN>) {                                  #read a line from STDIN
      if ( /100% packet loss/ ) {                  #check for ping timeouts (indicates host may be down)
         $pingstatus = "$CHECK_NAME UNKNOWN -- no ping reply from $host \n";
         print $pingstatus;                            #print error message
         exit $UNKNOWN;                            #exit script
      }                                            #end of if block
      if ( /NOT FOUND/ ) {                         #check for invalid hostname (using AIX ping)
         $pingstatus = "$CHECK_NAME UNKNOWN -- could not resolve hostname $host \n";
         print $pingstatus;                            #print error message
         exit $UNKNOWN;                            #exit script
      }                                            #end of if block
      if ( /unknown host/ ) {                      #check for invalid hostname (using Linux ping)
         $pingstatus = "$CHECK_NAME UNKNOWN -- could not resolve hostname $host \n";
         print $pingstatus;                            #print error message
         exit $UNKNOWN;                            #exit script
      }                                            #end of if block
      if ( /no route to host/ ) {                  #check for routing problems
         $pingstatus = "$CHECK_NAME UNKNOWN -- could not find a route to $host - check routing tables \n";
         print $pingstatus;                            #print error message
         exit $UNKNOWN;                            #exit script
      }                                            #end of if block
   }                                               #end of while loop
   close IN;                                       #close filehandle


}                                                       #end of subroutine


sub confirm_snmp_working {
   #
   # This section confirms the remote host will respond to SNMP queries
   #
   print "Running confirm_snmp_working subroutine \n" if ($verbose eq "yes");
   # Get the system description via SNMP
   # SNMPv2-MIB::sysDescr.0
   #
   my $sysdescr = "";                              #initialize variable
   $oid = ".1.3.6.1.2.1.1.1.0";
   $cmd = "$snmpget -On -v 1 -c $community $host $oid 2>&1";                 #define command to be run
   print "   running command: $cmd \n" if ($verbose eq "yes");
   open(IN,"$cmd |");           #open a filehandle for reading
   while (<IN>) {                               #read a line from STDIN
      if ( /STRING: ([a-zA-Z0-9\.\"?]+)/ ) {    #look for a response to the snmp query
         $sysdescr = $1;                        #assign more mnemonic variable name
      }                                         #end of if block
   }                                            #end of while loop
   close IN;                                    #close filehandle
   unless ( $sysdescr =~ /[a-zA-Z0-9\.]+/ ) {
      print "$CHECK_NAME CRITICAL -- could not query $host via SNMP.  Confirm you have the correct SNMP community string and the remote host $host has a working SNMP daemon.\n";
      exit $UNKNOWN;                            #exit script
   }                                            #end of unless block
}                                               #end of subroutine



sub get_system_info {
   #
   print "running get_system_info subroutine \n" if ($verbose eq "yes");
   #
   #
   # query the SNMP counters to read model number, firmware, uptime, hostname
   #
   #
   #
   #  Get the model number and firmware level
   # .1.3.6.1.2.1.1.1.0 = STRING: CSS106-1G-4P-1S SwOS v2.13	Model number and firmware level
   # .1.3.6.1.2.1.1.1.0 = STRING: CRS305-1G-4S+ SwOS v2.8.1
   #
   #
   $mikrotik{model}    = "unknown";					#initialize hash element to avoid undef errors
   $mikrotik{firmware} = "unknown";					#initialize hash element to avoid undef errors
   $oid = ".1.3.6.1.2.1.1.1.0";                            		#model number and firmware level
   $cmd = "$snmpget -On -v 1 -c $community $host $oid";        	#
   print "   running command to find model number: $cmd \n" if ($verbose eq "yes");
   open(IN,"$cmd |");                                                   #get the index numbers of the LUNs
   while (<IN>) {                                                       #read a line from the command output
      if (/$oid = STRING: \"?([a-zA-Z0-9\-\+]+) (SwOS v[0-9]+\.[0-9]+)\"?/) {	#regex to parse out model number and firmware level
         $mikrotik{model}    = $1;					#add value to hash
         $mikrotik{firmware} = $2;					#add value to hash
         print "   model:$mikrotik{model} firmware:$mikrotik{firmware} \n" if ($verbose eq "yes");
      }									#end of if block
   }                                                       		#end of while loop
   close IN;								#
   #
   # This check is for devices running MikroTik SwitchOS, not MikroTik RouterOS.  Confirm the firmware contains "SwOS"
   unless ( $mikrotik{firmware} =~ /SwOS/ ) {
      print "$CHECK_NAME UNKNOWN - this check is for devices running Mikrotik SwitchOS.  Detected firmware $mikrotik{firmware} \n";
      exit $UNKNOWN;
   }									#end of unless block
   #
   #  Get the hostname
   # .1.3.6.1.2.1.1.5.0 = STRING: switch2				Hostname
   #
   $mikrotik{hostname} = "unknown";					#initialize hash element to avoid undef errors
   $oid = ".1.3.6.1.2.1.1.5.0";                            		#model number and firmware level
   $cmd = "$snmpget -On -v 1 -c $community $host $oid";        		#
   print "   running command to find hostname: $cmd \n" if ($verbose eq "yes");
   open(IN,"$cmd |");                                                   #get the index numbers of the LUNs
   while (<IN>) {                                                       #read a line from the command output
      if (/$oid = STRING: \"?([a-zA-Z0-9\-\.]+)\"?/) {			#regex to parse out model number and firmware level
         $mikrotik{hostname} = $1;					#add value to hash
         print "   hostname:$mikrotik{hostname} \n" if ($verbose eq "yes");
      }									#end of if block
   }                                                       		#end of while loop
   close IN;								#
   #
   #  Get the uptime
   # .1.3.6.1.2.1.1.3.0 = Timeticks: (5218548) 14:29:45.48	Uptime.  Value in brackets is in hundredths of seconds, followed by hh:mm:ss.##
   # .1.3.6.1.2.1.1.3.0 = Timeticks: (5218548) 0:29:45.48	Value of hours may only be a single digit if less than 10 hours
   # .1.3.6.1.2.1.1.3.0 = 5218548				Simplified output by using -Ont parameter.  Helps avoid escaping brackets in regex
   #
   $oid = ".1.3.6.1.2.1.1.3.0";                            		#model number and firmware level
   $cmd = "$snmpget -Ont -v 1 -c $community $host $oid";        	#Use -Ont parameter to output in hundreths of seconds without brackets or hh:mm:ss.
   print "   running command to find uptime: $cmd \n" if ($verbose eq "yes");
   open(IN,"$cmd |");                                                   #get the index numbers of the LUNs
   while (<IN>) {                                                       #read a line from the command output
      if (/$oid = ([0-9]+)/) {						#regex to parse out the hundredths of seconds of uptime.  NOTE: use the -Ont parameter
         $mikrotik{uptime_seconds} = $1/100;				#divide by 100 to convert to seconds
         $mikrotik{uptime_seconds}  = sprintf("%.0f",$mikrotik{uptime_seconds});                     #truncate to 0 decimal places
         # convert seconds to a more human readable value
         if ( $mikrotik{uptime_seconds} <= 60 ) {			
            $mikrotik{uptime} = "$mikrotik{uptime_seconds} seconds";	#display in human readable format
         }								#end of if block
         if ( $mikrotik{uptime_seconds} > 60 ) {			
            $mikrotik{uptime} = $mikrotik{uptime_seconds} /60;		#convert seconds to minutes
            $mikrotik{uptime} = sprintf("%.0f",$mikrotik{uptime});      #truncate to 0 decimal places
            $mikrotik{uptime} = "$mikrotik{uptime} minutes";		#display in human readable format
         }								#end of if block
         if ( $mikrotik{uptime_seconds} > 3600 ) {
            $mikrotik{uptime} = $mikrotik{uptime_seconds} /3600;	#convert seconds to minutes
            $mikrotik{uptime} = sprintf("%.0f",$mikrotik{uptime});      #truncate to 0 decimal places
            $mikrotik{uptime} = "$mikrotik{uptime} hours";		#display in human readable format
         }								#end of if block
         if ( $mikrotik{uptime_seconds} > 86400 ) {
            $mikrotik{uptime} = $mikrotik{uptime_seconds} /86400;	#convert seconds to minutes
            $mikrotik{uptime} = sprintf("%.0f",$mikrotik{uptime});      #truncate to 0 decimal places
            $mikrotik{uptime} = "$mikrotik{uptime} days";		#display in human readable format
         }								#end of if block
         print "   uptime:$mikrotik{uptime} ($mikrotik{uptime_seconds} seconds) \n" if ($verbose eq "yes");
      }									#end of if block
   }									#end of while loop
   close IN;								#close filehandle
}                                                       		#end of subroutine




sub get_system_temperature {
   #
   # query the SNMP counters to read temperature sensors, fan speeds, etc.
   #
   print "running get_system_temperature subroutine \n" if ($verbose eq "yes");
   #
   #.1.3.6.1.4.1.14988.1.1.3.10.0 = INTEGER: 430			Board temperature in tenths of degrees Celsius
   #
   $mikrotik{cpu_temp} = "unknown";					#initialize hash element to avoid undef errors
   #
   #
   #
   if ( $mikrotik{cpu_temp} eq "unknown" ) {				#different switch models use different SNMP OID's for the temperature sensors
      $oid = ".1.3.6.1.4.1.14988.1.1.3.10.0";                          	#OID used for temperature on model CSS106-1G-4P-1S running SwOS 2.13 or later
      $cmd = "$snmpget -On -v 1 -c $community $host $oid";        	
      print "   running command to find temperature: $cmd \n" if ($verbose eq "yes");
      open(IN,"$cmd 2>&1 |");                                           #open filehandle from command output
      while (<IN>) {                                                    #read a line from the command output
         if (/$oid = INTEGER: ([0-9]+)/) {				#regex to parse out tmperature
            $mikrotik{cpu_temp} = $1;					#add value to hash
            $mikrotik{cpu_temp} = $mikrotik{cpu_temp}/10;		#convert from tenths of degrees to degrees Celsius
            $mikrotik{cpu_temp} = sprintf("%.1f",$mikrotik{cpu_temp});     #truncate to 1 decimal places
            print "   CPU temperature:$mikrotik{cpu_temp} Celsius \n" if ($verbose eq "yes");
         }								#end of if block
      }                                                       		#end of while loop
      close IN;								#close filehandle
   }									#end of if block
   #
   if ( $mikrotik{cpu_temp} eq "unknown" ) {				#different switch models use different SNMP OID's for the temperature sensors
      $oid = ".1.3.6.1.4.1.14988.1.1.3.11.0";                          	#OID used for temperature on model CRS305-1G-4S+ running SwOS 2.13 or later
      $cmd = "$snmpget -On -v 1 -c $community $host $oid";        	
      print "   running command to find temperature: $cmd \n" if ($verbose eq "yes");
      open(IN,"$cmd 2>&1 |");                                           #open filehandle from command output
      while (<IN>) {                                                    #read a line from the command output
         if (/$oid = INTEGER: ([0-9]+)/) {				#regex to parse out tmperature
            $mikrotik{cpu_temp} = $1;					#add value to hash
            $mikrotik{cpu_temp} = $mikrotik{cpu_temp}/10;		#convert from tenths of degrees to degrees Celsius
            $mikrotik{cpu_temp} = sprintf("%.1f",$mikrotik{cpu_temp});     #truncate to 1 decimal places
            print "   CPU temperature:$mikrotik{cpu_temp} Celsius \n" if ($verbose eq "yes");
         }								#end of if block
      }                                                       		#end of while loop
      close IN;								#close filehandle
   }									#end of if block
}									#end of subroutine 




sub get_fan_speeds {
   #
   # query the SNMP counters to read temperature sensors, fan speeds, etc.
   #
   print "running get_fan_speeds subroutine \n" if ($verbose eq "yes");
   #
   # to be written... need a MikroTik device with fans first....
   #
   $mikrotik{fan1speed} = 0;					#initialize variable, placeholder until a model with fans can be tested
   $mikrotik{fan2speed} = 0;					#initialize variable, placeholder until a model with fans can be tested
   $mikrotik{fan3speed} = 0;					#initialize variable, placeholder until a model with fans can be tested
   $mikrotik{fan4speed} = 0;					#initialize variable, placeholder until a model with fans can be tested
}								#end of subroutine 




sub print_output {
   #
   # print output in the format expected by nagios
   #
   print "running print_output subroutine \n" if ($verbose eq "yes");
   #
   #
   # The nagios performance data will be the same for all the outputs, so just put it in a variable that can be use by all the output options
   #
   # The format is:  label=value[UOM];[warn];[crit];[min];[max]
   # On the "label=value" section is required.  The warn|crit|min|max entries are optional.
   # You can have multiple items of perf data, just separate each section with a space
   # UOM is Units Of Measurement.    Can be s=seconds B=bytes MB=megabytes %=percent c=counter
   # You can use the standard nagios ranges and thresholds formats (examples below)
   # Range definition   Generate an alert if x...
   # ----------------   -------------------------
   # 10                 < 0 or > 10, (outside the range of {0 .. 10})
   # 10:                < 10, (outside {10 .. ∞})
   # ~:10               > 10, (outside the range of {-∞ .. 10})
   # 10:20              < 10 or > 20, (outside the range of {10 .. 20})
   # @10:20             ≥ 10 and ≤ 20, (inside the range of {10 .. 20})
   #
   $perf_data = "cpu_temperature=$mikrotik{cpu_temp};$cpu_temp_crit;$cpu_temp_warn;; ";
   #
   #
   # Much of the text of the output will be the same.  Put the common stuff in a variable so we can simplify the outputs
   $output_details = "CPU temperature:$mikrotik{cpu_temp}C  Uptime:$mikrotik{uptime} Hostname:$mikrotik{hostname} Model:$mikrotik{model} Firmware:$mikrotik{firmware} ";
   #
   # Different systems have different numbers of cooling fans.  Only include the cooling fan details if the fan is spinning at >0 RPM
   $output_details = "$output_details Fan1:$mikrotik{fan1speed}rpm" if ($mikrotik{fan1speed} > 0);
   $output_details = "$output_details Fan2:$mikrotik{fan2speed}rpm" if ($mikrotik{fan2speed} > 0);
   $output_details = "$output_details Fan3:$mikrotik{fan3speed}rpm" if ($mikrotik{fan3speed} > 0);
   $output_details = "$output_details Fan4:$mikrotik{fan4speed}rpm" if ($mikrotik{fan4speed} > 0);
   #
   if ( $mikrotik{cpu_temp} eq "unknown" ) {
      print "$CHECK_NAME UNKNOWN - could not determine CPU temperature.  $output_details | $perf_data \n";
      exit $WARN;
   }
   if ( $mikrotik{fan1speed} eq "unknown" ) {
      print "$CHECK_NAME UNKNOWN - could not determine speed of fan1.  $output_details | $perf_data \n";
      exit $WARN;
   }
   if ( $mikrotik{cpu_temp} > $cpu_temp_crit ) {
      print "$CHECK_NAME CRITICAL - CPU temperature is $mikrotik{cpu_temp}C.  The air conditioning or fans may have failed.   $output_details | $perf_data \n";
      exit $CRITICAL;
   }
   if ( $mikrotik{cpu_temp} > $cpu_temp_warn ) {
      print "$CHECK_NAME WARN - CPU temperature is $mikrotik{cpu_temp}C.  The air conditioning or fans may have failed.   $output_details | $perf_data \n";
      exit $WARN;
   }
   if ( $mikrotik{uptime_seconds} < 3600 ) {
      print "$CHECK_NAME WARN - Recent reboot detected.  Uptime is $mikrotik{uptime}.  $output_details | $perf_data \n";
      exit $WARN;
   }
   #
   # This message gets sent if everything is ok
   print "$CHECK_NAME OK - $output_details | $perf_data \n";
   exit $OK;
}                                                                       #end of subroutine



# --------------------------- main body of program ----------------------
get_options;
sanity_checks;
confirm_snmp_working;
get_system_info; 
get_system_temperature; 
get_fan_speeds;
print_output;



File: /LICENSE
MIT License

Copyright (c) 2021 nickjeffrey

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
# check_mikrotik_swos
nagios check for MikroTik devices running SwitchOS (not RouterOS)

# Requirements
perl, snmpwalk, snmpget on nagios server
IP address configured on MikroTik device with SNMP enabled

# Configuration
You will need a section in the services.cfg file on the nagios server that looks similar to the following.
````
    # Define a service to check MikroTik devices running SwitchOL (not RouterOS)
    # Parameters are SNMP community name
    define service {
        use                             generic-service
        hostgroup_name                  all_mikrotik_swos
        service_description             MikroTik SwOS
        check_command                   check_mikrotik_swos!public
        }
````

You will need a section in the commands.cfg file on the nagios server that looks similar to the following.
````
# 'check_mikrotik_swos' command definition
    # parameters are -H hostname -C snmp_community
    define command{
        command_name    check_mikrotik_swos
        command_line    $USER1$/check_mikrotik_swos -H $HOSTADDRESS$ -C $ARG1$
        }
````

# Output
Output will look similar to the following:
````    
    MikroTik SwOS OK - CPU temperature:43.0C  Uptime:2 days Hostname:switch2 Model:CSS106-1G-4P-1S Firmware:SwOS v2.13  | cpu_temperature=43.0;65;60;; 
````


