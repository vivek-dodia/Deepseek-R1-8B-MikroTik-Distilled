# Repository Information
Name: ansible-mikrotik

# Directory Structure
Directory structure:
└── github_repos/ansible-mikrotik/
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
    │   │       ├── pack-5157f39578c88c64cb13e6cee28a99c81589e21b.idx
    │   │       └── pack-5157f39578c88c64cb13e6cee28a99c81589e21b.pack
    │   ├── packed-refs
    │   └── refs/
    │       ├── heads/
    │       │   └── master
    │       ├── remotes/
    │       │   └── origin/
    │       │       └── HEAD
    │       └── tags/
    ├── .gitignore
    ├── create_vagrant_mikrotik.sh
    ├── library/
    │   ├── mikrotik.py
    │   ├── mt_command.py
    │   ├── mt_dhcp_server.py
    │   ├── mt_facts.py
    │   ├── mt_hotspot.py
    │   ├── mt_interfaces.py
    │   ├── mt_interface_wireless.py
    │   ├── mt_ip.py
    │   ├── mt_ip_address.py
    │   ├── mt_ip_firewall.py
    │   ├── mt_ip_firewall_addresslist.py
    │   ├── mt_login_test.py
    │   ├── mt_neighbor.py
    │   ├── mt_ppp_profile.py
    │   ├── mt_ppp_secret.py
    │   ├── mt_ppp_server.py
    │   ├── mt_radius.py
    │   ├── mt_radius_backup.py
    │   ├── mt_snmp.py
    │   ├── mt_system.py
    │   ├── mt_system_scheduler.py
    │   ├── mt_tool.py
    │   ├── mt_user.py
    │   └── __init__.py
    ├── LICENSE
    ├── Pipfile
    ├── Pipfile.lock
    ├── pythonlibs/
    │   ├── mt_api/
    │   │   ├── retryloop.py
    │   │   ├── socket_utils.py
    │   │   └── __init__.py
    │   └── mt_common.py
    ├── README.md
    ├── tasks/
    │   ├── backup_recover.yml
    │   └── main.yml
    ├── tests/
    │   └── integration/
    │       ├── ansible.cfg
    │       ├── library
    │       ├── pythonlibs
    │       ├── run_tests.sh
    │       ├── tasks/
    │       │   ├── hotspot-tests.yml
    │       │   ├── radius-tests.yml
    │       │   ├── test-address-list.yml
    │       │   ├── test-bridge.yml
    │       │   ├── test-command.yml
    │       │   ├── test-dhcp-server.yml
    │       │   ├── test-facts.yml
    │       │   ├── test-firewall-filter.yml
    │       │   ├── test-firewall-nat.yml
    │       │   ├── test-interface-ethernet.yml
    │       │   ├── test-interface-vlan.yml
    │       │   ├── test-interface-wireless.yml
    │       │   ├── test-ip-address.yml
    │       │   ├── test-ip-pool.yml
    │       │   ├── test-neighbor.yml
    │       │   ├── test-ovpn-client.yml
    │       │   ├── test-scheduler.yml
    │       │   ├── test-service.yml
    │       │   ├── test-snmp.yml
    │       │   ├── test-system.yml
    │       │   ├── test-tool.yml
    │       │   └── test-user.yml
    │       ├── tests.retry
    │       └── tests.yml
    └── Vagrantfile


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
	url = https://github.com/zahodi/ansible-mikrotik.git
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
0000000000000000000000000000000000000000 fb9c4eddd74c6665237a2dd5120b7c14c3cbadff vivek-dodia <vivek.dodia@icloud.com> 1738605803 -0500	clone: from https://github.com/zahodi/ansible-mikrotik.git


File: /.git\logs\refs\heads\master
0000000000000000000000000000000000000000 fb9c4eddd74c6665237a2dd5120b7c14c3cbadff vivek-dodia <vivek.dodia@icloud.com> 1738605803 -0500	clone: from https://github.com/zahodi/ansible-mikrotik.git


File: /.git\logs\refs\remotes\origin\HEAD
0000000000000000000000000000000000000000 fb9c4eddd74c6665237a2dd5120b7c14c3cbadff vivek-dodia <vivek.dodia@icloud.com> 1738605803 -0500	clone: from https://github.com/zahodi/ansible-mikrotik.git


File: /.git\packed-refs
# pack-refs with: peeled fully-peeled sorted 
dad638fff6df414c7167dc4dde793fdc46a6d4cf refs/remotes/origin/address-list
a18aa02ad5ad4628b9bc6ec1761fa8225c941029 refs/remotes/origin/check_mode
c71fa54e53b305ab5b768f5a8a2cd2e1f548aec4 refs/remotes/origin/csv_compare
93559b8bb5cfdbacfeb1d0140135cfa37e9ed339 refs/remotes/origin/dependabot/pip/cryptography-3.3.2
7d8db10565f05171ef3586e4578d6dc5c6cf854c refs/remotes/origin/facts
d08d716ba5793405948ce4030257786a33a9b623 refs/remotes/origin/ip_address
fb9c4eddd74c6665237a2dd5120b7c14c3cbadff refs/remotes/origin/master
c9e6e420db09f4a52188a077c511a11f020a6a09 refs/remotes/origin/persistent-connection
cc6eb9b76635f1cd99f6057df6ffc3801595accc refs/remotes/origin/sample-rollback
ea6de9712b44c370e402f52a8ae7b3dced4a0487 refs/remotes/origin/sdas-1268-system-scheduler
d8e7d48b8eb4985f7a1b0a8d2adb610b3c74ea85 refs/remotes/origin/sdas-1289-bridge-module
d8cb822fa6b927e8d340473aeb62311f65240b68 refs/remotes/origin/verify_api_available


File: /.git\refs\heads\master
fb9c4eddd74c6665237a2dd5120b7c14c3cbadff


File: /.git\refs\remotes\origin\HEAD
ref: refs/remotes/origin/master


File: /.gitignore
# Byte-compiled / optimized / DLL files
File: /create_vagrant_mikrotik.sh
#!/usr/bin/env bash

dl_link='https://download.mikrotik.com/routeros/6.42.9/chr-6.42.9.vdi'
vmname='mikrotik-6-42-9'

[[ -f ./downloads/$(basename "$dl_link") ]] && {
  echo "*** vdi already exists"
} || {
  mkdir -p ./downloads/
  wget --directory-prefix=./downloads/ "$dl_link"
}


echo "*** create the vm"
VBoxManage createvm \
  --name "$vmname" \
  --ostype 'Linux_64' \
  --register

VBoxManage storagectl \
  "$vmname" \
  --name "SATA Controller" \
  --add sata

echo "*** add the hard disk"
VBoxManage storageattach \
 "$vmname" \
  --storagectl "SATA Controller" \
  --port 0 \
  --device 0 \
  --type hdd \
  --medium ./downloads/$(basename "$dl_link")

vagrant package --base "$vmname" --output ~/"$vmname".box

vagrant box add "$vmname" ~/"$vmname".box --name "$vmname"


File: /library\mikrotik.py
#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'Valentin Gurmeza'
__version__ = "0.1.1"

DOCUMENTATION = '''
module = mikrotik
'''


class MikrotikModule():
    def __init__(self, module):
        self.module = module
        # Variables
        # Init attributes
        #   Get Key name 1st from params if not check env variable
        self.user_name = self.module.params["user_name"]
        self.ip_addr = self.module.params["ip_addr"]
        self.password = self.module.params["password"]
        # self.name = self.module.params["name"]
        # self.time_out = self.module.params["time_out"]
        self.fail_on_warning = self.module.params["fail_on_warning"]

def main():
    module = AnsibleModule(
        argument_spec=dict(
            password=dict(default=None),
            user_name=dict(default=None),
            ip_addr=dict(default=None),
            # tags=dict(default=None, type="dict"),
            # fail_on_warning=dict(default=True, choices=BOOLEANS, type="bool"),
            # fire_forget=dict(default=True, choices=BOOLEANS, type="bool"),
            # time_out=dict(default=500, typ="int"),
        ),
        supports_check_mode=True
    )
    if not rosapi_found:
            module.fail_json(msg="The ansible mikrotik module requires rosapi library. use 'pip install rosapi' ")

try:
    import rosapi
except ImportError:
    rosapi_found = False
else:
    rosapi_found = True
    MikrotikModule(module).main()

from ansible.module_utils.basic import AnsibleModule
main()


File: /library\mt_command.py
# -*- coding: utf-8 -*-
DOCUMENTATION = '''
module: mt_command
author:
  - "Valentin Gurmeza"
version_added: "2.3"
short_description: Issue mikrotik command
requirements:
  - mt_api
description:
  - Issue a mikrotik command
options:
  hostname:
    description:
      - hotstname of mikrotik router
    required: True
  username:
    description:
      - username used to connect to mikrotik router
    required: True
  password:
    description:
      - password used for authentication to mikrotik router
    required: True
  command:
    description:
      -  command to be sent to the router. The command must be a command path using
      - '/' for word separation
    required: True
  command_arguments:
    description:
      - parameters to pass with the command. Must be a dictionary
'''

EXAMPLES = '''
- mt_command:
    hostname:      "{{ inventory_hostname }}"
    username:      "{{ mt_user }}"
    password:      "{{ mt_pass }}"
    command:       /system/backup/save
    command_arguments:
      name:     ansible_test
      password: 123
'''

from ansible.module_utils import mt_api
from ansible.module_utils.mt_common import clean_params
from ansible.module_utils.basic import AnsibleModule


def main():

  module = AnsibleModule(
      argument_spec=dict(
          hostname=dict(required=True),
          username=dict(required=True),
          password=dict(required=True, no_log=True),
          command=dict(required=True, type='str'),
          command_arguments=dict(required=False, type='dict'),
      )
  )

  hostname     = module.params['hostname']
  username     = module.params['username']
  password     = module.params['password']
  changed = False
  changed_message = []

  mk = mt_api.Mikrotik(hostname, username, password)
  try:
    mk.login()
  except:
    module.fail_json(
        msg="Could not log into Mikrotik device." +
        " Check the username and password.",
    )

  api_path = module.params['command']

  if module.params['command_arguments'] != None:
    response = mk.api_command(base_path=api_path, params=module.params['command_arguments'])
  else:
    response = mk.api_command(base_path=api_path)

  if response[-1][0] == '!done':
    changed = True
    changed_message.append(response)
    changed_message.append(api_path)
    if module.params['command_arguments'] != None:
      changed_message.append(module.params['command_arguments'])

  if changed:
    module.exit_json(
        failed=False,
        changed=True,
        msg=changed_message
    )
  else:
    module.exit_json(
        failed=False,
        changed=False,
        msg="Command failed"
    )
if __name__ == '__main__':
  main()


File: /library\mt_dhcp_server.py
# -*- coding: utf-8 -*-
DOCUMENTATION = '''
module: mt_dhcp_server.py
author:
  - "Valentin Gurmeza"
version_added: "2.4"
short_description: Manage mikrotik dhcp-server endpoints
requirements:
  - mt_api
description:
  - Mikrotik dhcp-server generic module
options:
  hostname:
    description:
      - hotstname of mikrotik router
    required: True
  username:
    description:
      - username used to connect to mikrotik router
    required: True
  password:
    description:
      - password used for authentication to mikrotik router
    required: True
  parameter:
    description:
      - sub endpoint for mikrotik tool
    required: True
    options:
      - netwatch
      - e-mail
  settings:
    description:
      - All Mikrotik compatible parameters for this particular endpoint.
        Any yes/no values must be enclosed in double quotes
  state:
    description:
      - absent or present
'''

EXAMPLES = '''
- mt_dhcp_server:
    hostname:    "{{ inventory_hostname }}"
    username:    "{{ mt_user }}"
    password:    "{{ mt_pass }}"
    parameter:   network
    settings:
      address: 192.168.1.0/24
      dns:     192.168.1.20
'''

from ansible.module_utils.mt_common import clean_params, MikrotikIdempotent
from ansible.module_utils.basic import AnsibleModule



def main():
    module = AnsibleModule(
        argument_spec = dict(
            hostname  = dict(required=True),
            username  = dict(required=True),
            password  = dict(required=True, no_log=True),
            settings  = dict(required=False, type='dict'),
            parameter = dict(
                required  = True,
                choices   = ['network', 'option', 'dhcp-server'],
                type      = 'str'
            ),
            state   = dict(
                required  = False,
                choices   = ['present', 'absent'],
                type      = 'str'
            ),
        ),
    supports_check_mode=True
    )

    idempotent_parameter = None
    params = module.params

    if params['parameter'] == 'network':
      idempotent_parameter = 'address'
      params['parameter'] = "dhcp-server/network"

    if params['parameter'] == 'option':
      idempotent_parameter = 'name'
      params['parameter'] = "dhcp-server/option"

    if params['parameter'] == 'dhcp-server':
      idempotent_parameter = 'name'

    mt_obj = MikrotikIdempotent(
        hostname         = params['hostname'],
        username         = params['username'],
        password         = params['password'],
        state            = params['state'],
        desired_params   = params['settings'],
        idempotent_param = idempotent_parameter,
        api_path         = '/ip/' + str(params['parameter']),
        check_mode       = module.check_mode,

    )

    mt_obj.sync_state()

    if mt_obj.failed:
        module.fail_json(
          msg = mt_obj.failed_msg
        )
    elif mt_obj.changed:
        module.exit_json(
            failed=False,
            changed=True,
            msg=mt_obj.changed_msg,
            diff={ "prepared": {
                "old": mt_obj.old_params,
                "new": mt_obj.new_params,
            }},
        )
    else:
        module.exit_json(
            failed=False,
            changed=False,
            #msg='',
            msg=params['settings'],
        )

if __name__ == '__main__':
  main()


File: /library\mt_facts.py
#!/usr/bin/python
# -*- coding: utf-8 -*-

ANSIBLE_METADATA = {'metadata_version': '1.0',
                    'status': ['preview'],
                    'supported_by': 'community'}

DOCUMENTATION = '''
---
module: mt_facts
short_description: Gather facts for mikrotik devices.
description:
     - This module fetches data from the Mikrotik API
author: "kollyma"
options:
  filter:
    description:
      - Filter for a specific fact.
    choices:
      - interface_ethernet
      - system_ntp_client
      - system_routerboard
      - ip_route
      - ip_dns
      - ip_address

requirements: [ 'yaml' ]
'''

RETURN = '''
---
interface_ethernet:
  description: Return list of Mikrotik Interfaces
  returned: success
  type: list
  sample:  interface_ethernet [ {
                "mac_address": "4C:5E:0C:F4:BF:44",
                "master_port": "none",
                "mtu": "1500",
                "name": "ether1",
                "default_name": "ether1",
                "disabled": "false",
                ...
            } ]
system_routerboard:
  description: Return Mikrotik System Information
  returned: success
  type: dict
  sample:  "system_routerboard": {
            "current_firmware": "3.19",
            "factory_firmware": "3.19",
            "firmware_type": "ar9344",
            "model": "951G-2HnD",
            "routerboard": "true",
            "serial_number": "557E04B12525",
            "upgrade_firmware": "3.41"
        }
system_ntp_client:
  description: Return NTP Client Information
  returned: success
  type: dict
  sample:  "system_ntp_client": {
            "active_server": "5.148.175.134",
            "enabled": "true",
            "last_adjustment": "1ms538us",
            "last_update_before": "6m19s560ms",
            "last_update_from": "5.148.175.134",
            "mode": "unicast",
            "poll_interval": "15m",
            "primary_ntp": "213.251.53.234",
            "secondary_ntp": "5.148.175.134",
            "server_dns_names": ""
        },
ip_route:
  description: Return Mikrotik IP Routes
  returned: success
  type: dict
  sample:  "ip_route": {
                "active": "true",
                "distance": "1",
                "dst_address": "0.0.0.0/0",
                "dynamic": "true",
                "gateway": "8.8.8.8",
                "static": "true",
                "vrf_interface": "ether1"
            }
ip_address:
  description: Return Mikrotik IP addresses
  returned: success
  type: list
  sample:  "ip_address": [
                {
                    ".id": "*1",
                    "actual-interface": "bridge",
                    "address": "192.168.88.1/24",
                    "comment": "defconf",
                    "disabled": "false",
                    "dynamic": "false",
                    "interface": "bridge",
                    "invalid": "false",
                    "network": "192.168.88.0"
                }, ]
'''


import re
from ansible.module_utils import mt_api
from ansible.module_utils.basic import AnsibleModule


class MikrotikFacts(object):

    def __init__(self, hostname, username, password):

        self.hostname = hostname
        self.username = username
        self.password = password
        self.login_success = False
        self.current_params = {}
        self.mk = None
        self.failed_msg = None
        self.login()

    def run(self):
        param = dict()
        filter = module.params.get('filter')
        self.current_params = self.mk.api_print(base_path='/' + re.sub('_', '/', filter))

        if len(self.current_params) > 2:
            param[filter] = []
            for current_param in self.current_params[:-1]:
                param[filter].append(current_param[1])
        else:
            param[filter] = dict()
            for key, value in self.current_params[0][1].items():
                key = re.sub('-', '_', key)
                param[filter][key] = value

        return param

    def login(self):
        self.mk = mt_api.Mikrotik(
            self.hostname,
            self.username,
            self.password,
          )
        try:
            self.mk.login()
            self.login_success = True
        except:
            self.failed_msg = "Could not log into Mikrotik device, check the username and password."


def main():
    global module
    module = AnsibleModule(
      argument_spec = dict(
        filter=dict(default='system_routerboard', choices=[
                'interface_ethernet',
                'system_ntp_client',
                'system_routerboard',
                'ip_route',
                'ip_dns',
                'ip_address',
        ]),
        hostname=dict(required=True),
        username=dict(required=True),
        password=dict(required=True, no_log=True),
      ),
      supports_check_mode=True
    )

    params = module.params
    device = MikrotikFacts(params['hostname'], params['username'], params['password'])
    mt_facts = device.run()
    mt_facts_result = dict(changed=False, ansible_facts=mt_facts)
    module.exit_json(**mt_facts_result)

if __name__ == '__main__':
    main()


File: /library\mt_hotspot.py
# -*- coding: utf-8 -*-
DOCUMENTATION = '''
module: mt_snmp
author:
  - "Valentin Gurmeza"
version_added: "2.4"
short_description: Manage mikrotik hotspot endpoints
requirements:
  - mt_api
description:
  - Generic mikrotik hotspot module.
options:
  hostname:
    description:
      - hotstname of mikrotik router
    required: True
  username:
    description:
      - username used to connect to mikrotik router
    required: True
  password:
    description:
      - password used for authentication to mikrotik router
    required: True
  parameter:
    description:
      - sub endpoint for mikrotik hotspot
    required: True
    options:
      - netwatch
      - e-mail
      - hotspot
  settings:
    description:
      - All Mikrotik compatible parameters for this particular endpoint.
        Any yes/no values must be enclosed in double quotes
  state:
    description:
      - absent or present
'''

EXAMPLES = '''
- mt_hotspot:
    hostname:  "{{ inventory_hostname }}"
    username:  "{{ mt_user }}"
    password:  "{{ mt_pass }}"
    parameter: profile
    settings:
      name:       Hotspot_Crew
      use-radius: yes
'''

from ansible.module_utils.mt_common import clean_params, MikrotikIdempotent
from ansible.module_utils.basic import AnsibleModule



def main():
    module = AnsibleModule(
        argument_spec = dict(
            hostname  = dict(required=True),
            username  = dict(required=True),
            password  = dict(required=True, no_log=True),
            settings  = dict(required=False, type='dict'),
            parameter = dict(
                required  = True,
                choices   = ['hotspot', 'profile', 'walled-garden'],
                type      = 'str'
            ),
            state   = dict(
                required  = False,
                choices   = ['present', 'absent'],
                type      = 'str'
            ),
        ),
    supports_check_mode=True
    )

    idempotent_parameter = None
    params = module.params
    idempotent_parameter = 'name'

    if params['parameter'] == 'profile':
      params['parameter'] = "hotspot/profile"

    if params['parameter'] == 'walled-garden':
      idempotent_parameter = 'comment'
      params['parameter'] = "hotspot/walled-garden"

    mt_obj = MikrotikIdempotent(
        hostname         = params['hostname'],
        username         = params['username'],
        password         = params['password'],
        state            = params['state'],
        desired_params   = params['settings'],
        idempotent_param = idempotent_parameter,
        api_path         = '/ip/' + str(params['parameter']),
        check_mode       = module.check_mode,

    )

    mt_obj.sync_state()

    if mt_obj.failed:
        module.fail_json(
          msg = mt_obj.failed_msg
        )
    elif mt_obj.changed:
        module.exit_json(
            failed=False,
            changed=True,
            msg=mt_obj.changed_msg,
            diff={ "prepared": {
                "old": mt_obj.old_params,
                "new": mt_obj.new_params,
            }},
        )
    else:
        module.exit_json(
            failed=False,
            changed=False,
            #msg='',
            msg=params['settings'],
        )

if __name__ == '__main__':
  main()


File: /library\mt_interfaces.py
# -*- coding: utf-8 -*-
DOCUMENTATION = '''
module: mt_interface.py
author:
  - "Shaun Smiley"
  - "Valentin Gurmeza"
version_added: "2.4"
short_description: Manage mikrotik interfaces
requirements:
  - mt_api
description:
  - manage interfaces and settings
options:
  hostname:
    description:
      - hotstname of mikrotik router
    required: True
  username:
    description:
      - username used to connect to mikrotik router
    required: True
  password:
    description:
      - password used for authentication to mikrotik router
    required: True
  parameter:
    description:
      - sub endpoint for mikrotik tool
    required: True
    options:
      - ovpn-client
      - ethernet
      - vlan
      - bridge
      - bridge port
      - bridge settings
  settings:
    description:
      - All Mikrotik compatible parameters for this particular endpoint.
        Any yes/no values must be enclosed in double quotes
    required: True
  state:
    description:
      - absent or present
    required: Flase
'''

EXAMPLES = '''
- mt_interfaces:
    hostname:      "{{ inventory_hostname }}"
    username:      "{{ mt_user }}"
    password:      "{{ mt_pass }}"
    parameter:     "ethernet"
    state:         present
    settings:
        name:     ether2
        comment:  Ansible controlled ether2
        mtu:      1501
'''

from ansible.module_utils.mt_common import clean_params, MikrotikIdempotent
from ansible.module_utils.basic import AnsibleModule


def main():
  module = AnsibleModule(
    argument_spec=dict(
      hostname=dict(required=True),
      username=dict(required=True),
      password=dict(required=True, no_log=True),
      settings=dict(required=True, type='dict'),
      parameter=dict(
          required=True,
          choices=[
            'ethernet',
            'vlan',
            'ovpn-client',
            'bridge',
            'bridge port',
            'bridge settings'
          ],
          type='str'
      ),
      state=dict(
          required  = False,
          choices   = ['present', 'absent'],
          type      = 'str'
      )
    ),
    supports_check_mode=True
  )

  params = module.params
  if params['parameter'] == 'bridge port':
    params['parameter'] = 'bridge/port'
    idempotent_parameter = "interface"
  elif params['parameter'] == 'bridge settings':
    params['parameter'] = 'bridge/settings'
    idempotent_parameter = None
  else:
    idempotent_parameter = 'name'

  mt_obj = MikrotikIdempotent(
    hostname         = params['hostname'],
    username         = params['username'],
    password         = params['password'],
    state            = params['state'],
    desired_params   = params['settings'],
    idempotent_param = idempotent_parameter,
    api_path         = '/interface/' + str(params['parameter']),
    check_mode       = module.check_mode
  )

  # exit if login failed
  if not mt_obj.login_success:
    module.fail_json(
      msg = mt_obj.failed_msg
    )

  # add, remove or edit things
  mt_obj.sync_state()

  if mt_obj.failed:
      module.fail_json(
        msg = mt_obj.failed_msg
      )
  elif mt_obj.changed:
    module.exit_json(
      failed=False,
      changed=True,
      msg=mt_obj.changed_msg,
      diff={ "prepared": {
          "old": mt_obj.old_params,
          "new": mt_obj.new_params,
      }},
    )
  else:
    module.exit_json(
      failed=False,
      changed=False,
      #msg='',
      msg=params['settings'],
    )

if __name__ == '__main__':
  main()


File: /library\mt_interface_wireless.py
# -*- coding: utf-8 -*-
DOCUMENTATION = '''
module: mt_interface_wireless
author:
  - "Valentin Gurmeza"
version_added: "2.4"
short_description: Manage mikrotik interface_wireless endpoints
requirements:
  - mt_api
description:
  - Generic mikrotik interface wireless module.
options:
  hostname:
    description:
      - hotstname of mikrotik router
    required: True
  username:
    description:
      - username used to connect to mikrotik router
    required: True
  password:
    description:
      - password used for authentication to mikrotik router
    required: True
  parameter:
    description:
      - sub endpoint for mikrotik interface wireless
    required: True
    options:
      - security-profiles
  settings:
    description:
      - All Mikrotik compatible parameters for this particular endpoint.
        Any yes/no values must be enclosed in double quotes
  state:
    description:
      - absent or present
'''

EXAMPLES = '''
- mt_interface_wireless:
    hostname:  "{{ inventory_hostname }}"
    username:  "{{ mt_user }}"
    password:  "{{ mt_pass }}"
    parameter: security-profiles
    state:     present
    settings:
      name:   test1
      supplicant-identity: test

'''

from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.mt_common import clean_params, MikrotikIdempotent


def main():
  module = AnsibleModule(
    argument_spec = dict(
      hostname  = dict(required=True),
      username  = dict(required=True),
      password  = dict(required=True, no_log=True),
      settings  = dict(required=False, type='dict'),
      parameter = dict(
        required  = True,
        choices   = ['security-profiles'],
        type      = 'str'
      ),
      state   = dict(
        required  = False,
        choices   = ['present', 'absent'],
        type      = 'str'
      ),
    ),
    supports_check_mode=True
  )

  idempotent_parameter = None
  params = module.params

  idempotent_parameter = 'name'

  mt_obj = MikrotikIdempotent(
    hostname         = params['hostname'],
    username         = params['username'],
    password         = params['password'],
    state            = params['state'],
    desired_params   = params['settings'],
    idempotent_param = idempotent_parameter,
    api_path         = '/interface/wireless/' + str(params['parameter']),
    check_mode       = module.check_mode
  )

  mt_obj.sync_state()

  if mt_obj.failed:
    module.fail_json(
      msg = mt_obj.failed_msg
      )
  elif mt_obj.changed:
    module.exit_json(
      failed=False,
      changed=True,
      msg=mt_obj.changed_msg,
      diff={ "prepared": {
        "old": mt_obj.old_params,
        "new": mt_obj.new_params,
      }},
    )
  else:
    module.exit_json(
      failed=False,
      changed=False,
      msg=params['settings'],
    )

if __name__ == '__main__':
  main()


File: /library\mt_ip.py
# -*- coding: utf-8 -*-
DOCUMENTATION = '''
module: mt_ip
author:
  - "Valentin Gurmeza"
  - "Shaun Smiley"
version_added: "2.3"
short_description: Manage mikrotik ip endpoints
requirements:
  - mt_api
description:
  - enable, disable, or modify a ip endpoint settings
options:
  hostname:
    description:
      - hotstname of mikrotik router
    required: True
  username:
    description:
      - username used to connect to mikrotik router
    required: True
  password:
    description:
      - password used for authentication to mikrotik router
    required: True
  parameter:
    description:
      - sub endpoint for mikrotik snmp
    required: True
    options:
      - address-list
      - netwatch
      - e-mail
  settings:
    description:
      - All Mikrotik compatible parameters for this particular endpoint.
        Any yes/no values must be enclosed in double quotes
  state:
    description:
      - absent or present
'''

EXAMPLES = '''
- mt_service:
    hostname:      "{{ inventory_hostname }}"
    username:      "{{ mt_user }}"
    password:      "{{ mt_pass }}"
    parameter:     service
    settings:
      disabled:      no
      name:          ftp
      address:       192.168.52.3
'''

from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.mt_common import clean_params, MikrotikIdempotent


def main():
  module = AnsibleModule(
    argument_spec = dict(
      hostname  = dict(required=True),
      username  = dict(required=True),
      password  = dict(required=True, no_log=True),
      settings  = dict(required=False, type='dict'),
      parameter = dict(
        required  = True,
        choices   = ['service', 'pool', 'firewall/address-list'],
        type      = 'str'
      ),
      state   = dict(
        required  = False,
        choices   = ['present', 'absent'],
        type      = 'str'
      ),
    ),
    supports_check_mode=True
  )

  params = module.params
  if params['parameter'] == 'firewall/address-list':
    idempotent_parameter = 'address'
  else:
    idempotent_parameter = 'name'

  mt_obj = MikrotikIdempotent(
    hostname         = params['hostname'],
    username         = params['username'],
    password         = params['password'],
    state            = params['state'],
    desired_params   = params['settings'],
    idempotent_param = idempotent_parameter,
    api_path         = '/ip/' + str(params['parameter']),
    check_mode       = module.check_mode
  )

  mt_obj.sync_state()

  if mt_obj.failed:
    module.fail_json(
      msg = mt_obj.failed_msg
    )
  elif mt_obj.changed:
    module.exit_json(
      failed=False,
      changed=True,
      msg=mt_obj.changed_msg,
      diff={ "prepared": {
        "old": mt_obj.old_params,
        "new": mt_obj.new_params,
      }},
    )
  else:
    module.exit_json(
      failed=False,
      changed=False,
      msg=params['settings'],
    )
if __name__ == '__main__':
  main()


File: /library\mt_ip_address.py
DOCUMENTATION = '''
module: mt_ip_address
author:
  - "Valentin Gurmeza"
  - "Shaun Smiley"
  - "Antoni Matamalas"
version_added: "2.3"
short_description: Manage mikrotik /ip/addresses
requirements:
  - mt_api
description:
  - Manage addresses on interfaces
options:
  hostname:
    description:
      - hotstname of mikrotik router
    required: True
  username:
    description:
      - username used to connect to mikrotik router
    required: True
  password:
    description:
      - password used for authentication to mikrotik router
    required: True
  idempotent:
    description:
      - parameter that will define the behavior for the ip address status.
      - If "interface" is used, only one IP will be allowed per interface.
        The "state" parameter will define if the IP is added, edited or
        removed. No settings options are required to removed the IP from an
        interface
      - If "address" is used, and interface will be able to have multiple IPs,
        but address will only be added or removed. In order to change an IP, it
        will have to be first removed and then added to the interface in two
        tasks.
    required: False
    default: address
  settings:
    description:
      - All Mikrotik compatible parameters for this particular endpoint.
        Any yes/no values must be enclosed in double quotes
    required: True
  state:
    description:
      - Depending on the idempotent option, it will define the status of the IP
        on an interface
    required: False
    default: present
'''

EXAMPLES = '''
# Add IP to an interface with a comment. If the interface has already an IP it
# will add as a sencond IP
- mt_ip_address:
    hostname:   "{{ inventory_hostname }}"
    username:   "{{ mt_user }}"
    password:   "{{ mt_pass }}"
    idempotent: "address"
    state:      "present"
    settings:
      interface:  "ether2"
      address:    "192.168.88.2/24"
      network:    "192.168.88.0/24"
      comment:    "link 3"

# Assign IP to the interface. If the interface has any previous IP, it will be
# replaced by this one.
- mt_ip_address:
    hostname:   "{{ inventory_hostname }}"
    username:   "{{ mt_user }}"
    password:   "{{ mt_pass }}"
    idempotent: "interface"
    state:      "present"
    settings:
      interface:  "ether2"
      address:    "192.168.88.2/24"
      network:    "192.168.88.0/24"
      comment:    "link 3"

# Remove any IP from an interface
- mt_ip_address:
    hostname:   "{{ inventory_hostname }}"
    username:   "{{ mt_user }}"
    password:   "{{ mt_pass }}"
    idempotent: "interface"
    state:      "absent"
    settings:
      interface:  "ether2"
'''

from ansible.module_utils.mt_common import clean_params, MikrotikIdempotent
from ansible.module_utils.basic import AnsibleModule


def main():

  module = AnsibleModule(
      argument_spec=dict(
          hostname  = dict(required=True),
          username  = dict(required=True),
          password  = dict(required=True, no_log=True),
          settings  = dict(required=True, type='dict'),
          idempotent = dict(
              required  = False,
              default   = 'address',
              choices   = ['address', 'interface'],
              type      = 'str'
          ),
          state = dict(
              required  = False,
              default   = "present",
              choices   = ['present', 'absent'],
              type      = 'str'
          ),
      ),
      supports_check_mode=True
  )

  params = module.params
  mt_obj = MikrotikIdempotent(
    hostname         = params['hostname'],
    username         = params['username'],
    password         = params['password'],
    state            = params['state'],
    desired_params   = params['settings'],
    idempotent_param = params['idempotent'],
    api_path         = '/ip/address',
    check_mode       = module.check_mode
  )

  # exit if login failed
  if not mt_obj.login_success:
    module.fail_json(
      msg = mt_obj.failed_msg
    )

  # add, remove or edit things
  mt_obj.sync_state()

  if mt_obj.failed:
      module.fail_json(
        msg = mt_obj.failed_msg
      )
  elif mt_obj.changed:
    module.exit_json(
      failed=False,
      changed=True,
      msg=mt_obj.changed_msg,
      diff={ "prepared": {
          "old": mt_obj.old_params,
          "new": mt_obj.new_params,
      }},
    )
  else:
    module.exit_json(
      failed=False,
      changed=False,
      #msg='',
      msg=params['settings'],
    )

if __name__ == '__main__':
  main()



File: /library\mt_ip_firewall.py
DOCUMENTATION = '''
module: mt_ip_firewall
author:
  - "Valentin Gurmeza"
  - "Shaun Smiley"
version_added: "2.3"
short_description: Manage mikrotik /ip/firewall/
requirements:
  - mt_api
description:
  - Generic mikrotik firewall module
options:
  hostname:
    description:
      - hotstname of mikrotik router
    required: True
  username:
    description:
      - username used to connect to mikrotik router
    required: True
  password:
    description:
      - password used for authentication to mikrotik router
    required: True
  rule:
    description:
      - a list containing dictionary parameters.
        action, chain, comment, and place-before keys are required
  parameter:
    description:
      - sub endpoint for mikrotik firewall
    required: True
    options:
      - filter
      - nat
      - mangle
  settings:
    description:
      - All Mikrotik compatible parameters for this particular endpoint.
        Any yes/no values must be enclosed in double quotes
      - if a firewall list containing dictionary parameters,
        action, chain, comment, and place-before keys are required
  state:
    description:
      - absent or present
  force:
    description:
      - True/False value to force remove the rule regardless of the position in the rule list.
'''

EXAMPLES = '''
- mt_ip_firewall:
    hostname:  "{{ inventory_hostname }}"
    username:  "{{ mt_user }}"
    password:  "{{ mt_pass }}"
    state:     present
    parameter: filter
    rule:
      action: accept
      chain: forward
      comment: controlled by ansible
      place-before: "2"
'''

from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils import mt_api
import re
from copy import copy


def main():

  module = AnsibleModule(
    argument_spec=dict(
      hostname  = dict(required=True),
      username  = dict(required=True),
      password  = dict(required=True, no_log=True),
      rule      = dict(required=False, type='dict'),
      parameter = dict(required=True, type='str'),
      state = dict(
        required  = False,
        default   = "present",
        choices   = ['present', 'absent'],
        type      = 'str'
      ),
    ),
    supports_check_mode=True
  )

  hostname     = module.params['hostname']
  username     = module.params['username']
  password     = module.params['password']
  rule = module.params['rule']
  state        = module.params['state']
  api_path     = '/ip/firewall/' + module.params['parameter']
  check_mode      = module.check_mode
# ##############################################
# Check if "place-before" is an integer
# #############################################
  try:
    desired_order = int(rule['place-before'])
  except:
    module.exit_json(
      failed=True,
      changed=False,
      msg="place-before is not set or is not set to an integer",
    )
  changed = False
  msg = ""

  mk = mt_api.Mikrotik(hostname, username, password)
  try:
    mk.login()
  except:
    module.fail_json(
        msg="Could not log into Mikrotik device." +
        " Check the username and password.",
    )

  filter_response = mk.api_print(api_path)
  current_rule = None
  current_id = None
  existing_order = None
  last_item = len(filter_response) - 2
  changed_msg = []

  # Always set the comment to the order_number
  if 'comment' in rule:
    rule['comment'] = str(desired_order) + " " + str(rule['comment'])
  else:
    rule['comment'] = str(desired_order)

  if desired_order <= last_item:
    placed_at_the_end = False
  else:
    placed_at_the_end = True
    # remove the place-before if we are placing
    # the rule at the bottom of the chain
    rule.pop('place-before', None)

  # Check rule is not present
  # find existing rule
  # current_rule is what's on mikrotik right now
  for index, current_param in enumerate(filter_response):
    if 'comment' in current_param[1]:
      if re.search(r"^" + str(desired_order) + "\s+", current_param[1]['comment']):
        current_id = current_param[1]['.id']
        existing_order = index
        current_rule = current_param[1]
        # remove the place-before since we'll be editing not moving it
        rule.pop('place-before', None)

  # ensure the rule if state is present
  if state == "present":
    # if we don't have an existing rule to match
    # the desired we create a new one
    if not current_rule:
      if not check_mode:
        mk.api_add(api_path, rule)
      changed = True,
    # if current_rule is true we need to ensure the changes
    else:
      out_params = {}
      old_params = {}
      for desired_param in rule:
        rule[desired_param] = str(rule[desired_param])
        if desired_param in current_rule:
          if current_rule[desired_param] != rule[desired_param]:
            out_params[desired_param] = rule[desired_param]
            old_params[desired_param] = current_rule[desired_param]
        else:
          out_params[desired_param] = rule[desired_param]
          if desired_param in current_rule:
            old_params[desired_param] = current_rule[desired_param]

      # When out_params has been set it means we found our diff
      # and will set it on the mikrotik
      if out_params:
        if current_id is not None:
          out_params['.id'] = current_id

          if not check_mode:
            mk.api_edit(
                base_path = api_path,
                params    = out_params
            )

          # we don't need to show the .id in the changed message
          if '.id' in out_params:
            del out_params['.id']
          changed = True

          changed_msg.append({
              "new_params": out_params,
              "old_params": old_params,
          })

    # ensure the rule is in right position
    if current_id:
      if int(existing_order) != int(desired_order):
        api_path += '/move'
        params = False
        if placed_at_the_end:
          if existing_order > last_item:
            params = {
            '.id': current_id,
            }
        else:
          params = {
          '.id': current_id,
          'destination': desired_order
          }
        if params:
          if not check_mode:
            mk.api_command(api_path, params)
          changed_msg.append({
              "moved": existing_order,
              "to": old_params,
          })
          changed = True

#####################################
# Remove the rule
#####################################
  elif state == "absent":
    if current_rule:
      if not check_mode:
        mk.api_remove(api_path, current_id)
      changed = True
      changed_msg.append("removed rule: " + str(desired_order))
  else:
    failed = True

  if changed:
    module.exit_json(
        failed=False,
        changed=True,
        msg=changed_msg
      )
  elif not changed:
    module.exit_json(
        failed=False,
        changed=False,
      )
  else:
    module.fail_json()

  ##########################################
  # To DO:
  # Clean up duplicate items
  ###########################################

if __name__ == '__main__':
  main()


File: /library\mt_ip_firewall_addresslist.py
# -*- coding: utf-8 -*-
DOCUMENTATION = '''
module: mt_ip_firewall_filter
author:
  - "Valentin Gurmeza"
  - "Shaun Smiley"
version_added: "2.3"
short_description: Manage mikrotik /ip/firewall/filter
requirements:
  - mt_api
description:
  - FILL ME OUT
options:
  hostname:
    description:
      -
  username:
    description:
      -
  password:
    description:
      -
  list-name:
    description:
      - name of the address-list
  state:
    description:
      - present or absent
  address_list:
    description:
      - A list of single IP addresses or range of IPs to add to address-list.
        Can also be a set to a hostname which will create a dynamic entry
        in the list with the proper IP address for the record (as of 6.38.1)
'''

EXAMPLES = '''
- mt_ip_firewall_addresslist:
    hostname:      "{{ inventory_hostname }}"
    username:      "{{ mt_user }}"
    password:      "{{ mt_pass }}"
    state:         "present"
    name:          "block_all"
    dynamic: false
    address_list:
      - 192.168.10.1
      - yahoo.com
      - 19.134.52.23/23
'''

from ansible.module_utils import mt_api
from ansible.module_utils.basic import AnsibleModule


def main():

  module = AnsibleModule(
    argument_spec=dict(
      hostname  = dict(required=True),
      username  = dict(required=True),
      password  = dict(required=True, no_log=True),
      list_name  = dict(required=True, type='str'),
      address_list = dict(required=False, type='list'),
      state = dict(
        required  = False,
        default   = "present",
        choices   = ['present', 'absent', 'force'],
        type      = 'str'
      ),
    ),
    supports_check_mode=True
  )

  hostname     = module.params['hostname']
  username     = module.params['username']
  password     = module.params['password']
  ansible_list_name = module.params['list_name']
  ansible_address_list = module.params['address_list']
  state        = module.params['state']
  check_mode   = module.check_mode
  changed      = False
  msg = ""

  address_list_path = '/ip/firewall/address-list'
  mk = mt_api.Mikrotik(hostname, username, password)
  try:
    mk.login()
  except:
    module.fail_json(
      msg="Could not log into Mikrotik device." +
      " Check the username and password.",
    )

  response = mk.api_print(address_list_path)
  mikrotik_address_list = []
  mikrotik_address_id = {}
  list_name = ansible_list_name
  for item in response:
    if 'list' in item[1].keys():
      address = item[1]['address']
      if item[1]['list'] == list_name:
        temp_dict = {}
        temp_dict['address'] = item[1]['address']
        if 'comment' in item[1].keys():
          temp_dict['comment'] = item[1]['comment']
        mikrotik_address_list.append(dict(temp_dict))
        mikrotik_address_id[address] = item[1]['.id']

  if state == "present":
    if ansible_address_list == mikrotik_address_list:
      module.exit_json(
        changed = False,
        failed  = False,
        msg     = "list up to date",
      )
    common_list = []
    for item in ansible_address_list:
      for item2 in mikrotik_address_list:
        if item['address'] in item2['address']:
          common_list.append(item['address'])
          if item['comment'] in item2['comment']:
            ##################
            # update comment
            #################
            pass

    #################################
    # build add_list
    # add item missing from mikrotik
    #################################
    add_list = []
    for item in ansible_address_list:
      if item['address'] not in common_list:
        temp_dict = {}
        temp_dict['address'] = item['address']
        temp_dict['comment'] = item['comment']
        add_list.append(dict(temp_dict))

    for i in add_list:
      #address = i['address']
      #comment = i['comment']
      add_dictionary = {
        "address": i['address'],
        "list": list_name,
        "comment": i['comment']
      }
      if not check_mode:
        mk.api_add(address_list_path, add_dictionary)
      changed = True

    #####################
    # build remove list
    ######################
    remove_list = []
    for item in mikrotik_address_list:
      if item['address'] not in common_list:
        remove_list.append(item['address'])
    #######################################
    # Remove every item in the address_list
    #######################################
    for i in remove_list:
      remove_id = mikrotik_address_id[i]
      if not check_mode:
        mk.api_remove(address_list_path, remove_id)
      if not changed:
        changed = True
  else:
    #######################################
    # Remove every item
    #######################################
    for remove_id in mikrotik_address_id.values():
      if not check_mode:
        mk.api_remove(address_list_path, remove_id)
      if not changed:
        changed = True

  if changed:
    module.exit_json(
      changed = True,
      failed = False,
      msg    = ansible_list_name + "has been modified",
     )
  else:
    module.exit_json(
      changed = False,
      failed = False,
      msg    = ansible_list_name + " is up to date",
    )


if __name__ == '__main__':
  main()


File: /library\mt_login_test.py
#! /usr/bin/python
import socket
from ansible.module_utils import mt_api

from ansible.module_utils.basic import AnsibleModule


def main():

  module = AnsibleModule(
    argument_spec=dict(
      hostname=dict(required=True),
      username=dict(required=True),
      password=dict(required=True, no_log=True),
      )
    )

  hostname = module.params['hostname']
  username = module.params['username']
  password = module.params['password']
  changed = False
  msg = ""

  mk = mt_api.Mikrotik(hostname,username,password)
  sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  result = sock.connect_ex((hostname, 8728))
  if result == 0:
    try:
      mk.login()
    except:
      module.fail_json(
        msg="Could not log into Mikrotik device.  Check the username and password."
      )
  else:
      module.fail_json(
        msg="Could not access RouterOS api." + " Verify API service is enabled and not blocked by firewall."
      )


  # response = apiros.talk([b'/ip/address/add', b'=address=192.168.15.2/24', b'=interface=ether7'])
  module.exit_json(
    changed=False,
    failed=False,
  )

if __name__ == '__main__':
  main()


File: /library\mt_neighbor.py
# -*- coding: utf-8 -*-
DOCUMENTATION = '''
module: mt_snmp
author:
  - "Valentin Gurmeza"
version_added: "2.4"
short_description: Manage mikrotik neighbor endpoints
requirements:
  - mt_api
description:
  - Generic mikrotik neighbor module.
options:
  hostname:
    description:
      - hotstname of mikrotik router
    required: True
  username:
    description:
      - username used to connect to mikrotik router
    required: True
  password:
    description:
      - password used for authentication to mikrotik router
    required: True
  parameter:
    description:
      - sub endpoint for mikrotik neighbor
    required: True
    options:
      - netwatch
      - e-mail
  settings:
    description:
      - All Mikrotik compatible parameters for this particular endpoint.
        Any yes/no values must be enclosed in double quotes
  state:
    description:
      - absent or present
'''

EXAMPLES = '''
- mt_hotspot:
    hostname:  "{{ inventory_hostname }}"
    username:  "{{ mt_user }}"
    password:  "{{ mt_pass }}"
    parameter: discovery
    settings:
      name:     ether7
      discover: "yes"
'''

from ansible.module_utils.mt_common import clean_params, MikrotikIdempotent
from ansible.module_utils.basic import AnsibleModule



def main():
  module = AnsibleModule(
    argument_spec = dict(
      hostname  = dict(required=True),
      username  = dict(required=True),
      password  = dict(required=True, no_log=True),
      settings  = dict(required=False, type='dict'),
      parameter = dict(
        required  = True,
        choices   = ['discovery'],
        type      = 'str'
      ),
      state   = dict(
        required  = False,
        choices   = ['present', 'absent'],
        type      = 'str'
      ),
    ),
    supports_check_mode=True
  )

  idempotent_parameter = None
  params = module.params
  idempotent_parameter = 'name'


  mt_obj = MikrotikIdempotent(
    hostname         = params['hostname'],
    username         = params['username'],
    password         = params['password'],
    state            = params['state'],
    desired_params   = params['settings'],
    idempotent_param = idempotent_parameter,
    api_path         = '/ip/neighbor/' + str(params['parameter']),
    check_mode       = module.check_mode
  )

  mt_obj.sync_state()

  if mt_obj.failed:
    module.fail_json(
      msg = mt_obj.failed_msg
    )
  elif mt_obj.changed:
    module.exit_json(
      failed=False,
      changed=True,
      msg=mt_obj.changed_msg,
      diff={ "prepared": {
        "old": mt_obj.old_params,
        "new": mt_obj.new_params,
      }},
    )
  else:
    module.exit_json(
      failed=False,
      changed=False,
      #msg='',
      msg=params['settings'],
    )

if __name__ == '__main__':
  main()


File: /library\mt_ppp_profile.py
# -*- coding: utf-8 -*-
DOCUMENTATION = '''
module: mt_ppp_profile
author:
  - "Colin Zwiebel"
version_added: "2.4.1"
short_description: Manage mikrotik ppp profiles
requirements:
  - mt_api
description:
  - Generic mikrotik ppp profile management module.
options:
  hostname:
    description:
      - hostname of mikrotik router
    required: True
  username:
    description:
      - username used to connect to mikrotik router
    required: True
  password:
    description:
      - password used for authentication to mikrotik router
    required: True
  settings:
    description:
      - All Mikrotik compatible parameters for the ppp-profile endpoint.
        Any yes/no values must be enclosed in double quotes
  state:
    description:
      - absent or present
'''

EXAMPLES = '''
- mt_ppp_profile:
    hostname:      "{{ inventory_hostname }}"
    username:      "{{ mt_user }}"
    password:      "{{ mt_pass }}"
    state:         present
    settings:
      name:            example-profile
      local-address:   1.2.3.4
      change-tcp-mss:  "y"
      use-compression: "y"
      use-encryption:  required
'''

from ansible.module_utils.mt_common import clean_params, MikrotikIdempotent
from ansible.module_utils.basic import AnsibleModule


def main():
  module = AnsibleModule(
    argument_spec = dict(
      hostname  = dict(required=True),
      username  = dict(required=True),
      password  = dict(required=True, no_log=True),
      settings  = dict(required=False, type='dict'),
      state   = dict(
        required  = False,
        choices   = ['present', 'absent'],
        type      = 'str'
      ),
    ),
    supports_check_mode=True
  )

  params = module.params
  mt_obj = MikrotikIdempotent(
    hostname         = params['hostname'],
    username         = params['username'],
    password         = params['password'],
    state            = params['state'],
    desired_params   = params['settings'],
    idempotent_param = 'name',
    api_path         = '/ppp/profile',
    check_mode      = module.check_mode
  )

  mt_obj.sync_state()

  if mt_obj.failed:
    module.fail_json(
      msg = mt_obj.failed_msg
    )
  elif mt_obj.changed:
    module.exit_json(
      failed=False,
      changed=True,
      msg=mt_obj.changed_msg,
      diff={ "prepared": {
        "old": mt_obj.old_params,
        "new": mt_obj.new_params,
      }},
    )
  else:
    module.exit_json(
      failed=False,
      changed=False,
      #msg='',
      msg=params['settings'],
    )

if __name__ == '__main__':
  main()


File: /library\mt_ppp_secret.py
# -*- coding: utf-8 -*-
DOCUMENTATION = '''
module: mt_ppp_secret
author:
  - "Colin Zwiebel"
version_added: "2.4.1"
short_description: Manage mikrotik ppp secrets (vpn users)
requirements:
  - mt_api
description:
  - Generic mikrotik ppp secret module.
options:
  hostname:
    description:
      - hostname of mikrotik router
    required: True
  username:
    description:
      - username used to connect to mikrotik router
    required: True
  password:
    description:
      - password used for authentication to mikrotik router
    required: True
  settings:
    description:
      - All Mikrotik compatible parameters for the ppp secrets endpoint.
        Any yes/no values must be enclosed in double quotes
  state:
    description:
      - absent or present
'''

EXAMPLES = '''
- mt_ppp_secret:
    hostname:      "{{ inventory_hostname }}"
    username:      "{{ mt_user }}"
    password:      "{{ mt_pass }}"
    state:         present
    settings:
      name:     user2
      password: pass2
      service:  ovpn
      remote-address: 1.2.3.4
'''

from ansible.module_utils.mt_common import clean_params, MikrotikIdempotent
from ansible.module_utils.basic import AnsibleModule



def main():
  module = AnsibleModule(
    argument_spec = dict(
      hostname  = dict(required=True),
      username  = dict(required=True),
      password  = dict(required=True, no_log=True),
      settings  = dict(required=False, type='dict'),
      state   = dict(
        required  = False,
        choices   = ['present', 'absent'],
        type      = 'str'
      ),
    ),
    supports_check_mode=True
  )

  params = module.params
  mt_obj = MikrotikIdempotent(
    hostname         = params['hostname'],
    username         = params['username'],
    password         = params['password'],
    state            = params['state'],
    desired_params   = params['settings'],
    idempotent_param = 'name',
    api_path         = '/ppp/secret',
    check_mode      = module.check_mode
  )

  mt_obj.sync_state()

  if mt_obj.failed:
    module.fail_json(
      msg = mt_obj.failed_msg
    )
  elif mt_obj.changed:
    module.exit_json(
      failed=False,
      changed=True,
      msg=mt_obj.changed_msg,
      diff={ "prepared": {
        "old": mt_obj.old_params,
        "new": mt_obj.new_params,
      }},
    )
  else:
    module.exit_json(
      failed=False,
      changed=False,
      msg=params['settings'],
    )

if __name__ == '__main__':
  main()


File: /library\mt_ppp_server.py
# -*- coding: utf-8 -*-
DOCUMENTATION = '''
module: mt_ppp_server
author:
  - "Colin Zwiebel"
version_added: "2.3.1"
short_description: Manage mikrotik ppp servers 
requirements:
  - mt_api
description:
  - Manage ppp servers and their settings.
options:
  hostname:
    description:
      - hostname of mikrotik router
    required: True
  username:
    description:
      - username used to connect to mikrotik router
    required: True
  password:
    description:
      - password used for authentication to mikrotik router
    required: True
  server_type:
    description:
      - VPN server type to manage
    required: True
    options:
      - l2tp
      - ovpn
      - pptp
      - sstp
  settings:
    description:
      - All Mikrotik compatible parameters for this type of vpn server.
        Any yes/no values must be enclosed in double quotes
'''

EXAMPLES = '''
- mt_ppp_server:
    hostname:      "{{ inventory_hostname }}"
    username:      "{{ mt_user }}"
    password:      "{{ mt_pass }}"
    server_type:   pptp
    settings:
      disabled:        no
      max-mtu:         1420
      authentication:  mschap2
'''

from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.mt_common import clean_params, MikrotikIdempotent


def main():
  module = AnsibleModule(
    argument_spec = dict(
      hostname  = dict(required=True),
      username  = dict(required=True),
      password  = dict(required=True, no_log=True),
      settings  = dict(required=False, type='dict'),
      server_type = dict(
        required  = True,
        choices   = ['l2tp', 'ovpn', 'pptp', 'sstp'],
        type      = 'str'
      ),
    ),
    supports_check_mode=True
  )

  params = module.params
  mt_obj = MikrotikIdempotent(
    hostname         = params['hostname'],
    username         = params['username'],
    password         = params['password'],
    state            = None,
    desired_params   = params['settings'],
    idempotent_param = None,
    api_path         = '/interface/{}-server/server'.format(params['server_type']),
    check_mode       = module.check_mode
  )

  mt_obj.sync_state()

  if mt_obj.failed:
    module.fail_json(
      msg = mt_obj.failed_msg
    )
  elif mt_obj.changed:
    module.exit_json(
      failed=False,
      changed=True,
      msg=mt_obj.changed_msg,
      diff={ "prepared": {
        "old": mt_obj.old_params,
        "new": mt_obj.new_params,
      }},
    )
  else:
    module.exit_json(
      failed=False,
      changed=False,
      msg=params['settings'],
    )
if __name__ == '__main__':
  main()


File: /library\mt_radius.py
# -*- coding: utf-8 -*-
DOCUMENTATION = '''
module: mt_radius
author:
  - "Valentin Gurmeza"
  - "Shaun Smiley"
version_added: "2.3"
short_description: Manage mikrotik radius client
requirements:
  - mt_api
description:
  - Add or remove a radius client
options:
  hostname:
    description:
      - hotstname of mikrotik router
  username:
    description:
      - username used to connect to mikrotik router
  password:
    description:
      - password used for authentication to mikrotik router
  state:
    description:
      - client present or absent
    required: False
    choices:
      - present
      - absent
'''

EXAMPLES = '''
# Add a new radius entry
- mt_radius:
    hostname:    "{{ inventory_hostname }}"
    username:    "{{ mt_user }}"
    password:    "{{ mt_pass }}"
    state:         present
    parameter: radius
    settings:
      address: 192.168.230.1
      comment: ansible_test
      timeout: '2s500ms'
      secret:  'password'
      service:
        - login
        - hotspot
        - wireless
'''

from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.mt_common import MikrotikIdempotent


def main():
    module = AnsibleModule(
        argument_spec = dict(
            hostname  = dict(required=True),
            username  = dict(required=True),
            password  = dict(required=True, no_log=True),
            settings  = dict(required=False, type='dict'),
            parameter = dict(
                required  = True,
                choices   = ['radius', 'incoming'],
                type      = 'str'
            ),
            state   = dict(
                required  = False,
                choices   = ['present', 'absent'],
                type      = 'str'
            ),
        ),
    supports_check_mode=True
    )

    idempotent_parameter = None
    params = module.params

    if params['parameter'] == 'radius':
      idempotent_parameter = 'comment'
      params['parameter'] = "/radius"

    if params['parameter'] == 'incoming':
      params['parameter'] = "/radius/incoming"


    mt_obj = MikrotikIdempotent(
        hostname         = params['hostname'],
        username         = params['username'],
        password         = params['password'],
        state            = params['state'],
        desired_params   = params['settings'],
        idempotent_param = idempotent_parameter,
        api_path         = str(params['parameter']),
        check_mode       = module.check_mode,

    )

    mt_obj.sync_state()

    if mt_obj.failed:
        module.fail_json(
          msg = mt_obj.failed_msg
        )
    elif mt_obj.changed:
        module.exit_json(
            failed=False,
            changed=True,
            msg=mt_obj.changed_msg,
            diff={ "prepared": {
                "old": mt_obj.old_params,
                "new": mt_obj.new_params,
            }},
        )
    else:
        module.exit_json(
            failed=False,
            changed=False,
            #msg='',
            msg=params['settings'],
        )

if __name__ == '__main__':
  main()


File: /library\mt_radius_backup.py
# -*- coding: utf-8 -*-
DOCUMENTATION = '''
module: mt_radius
author:
  - "Valentin Gurmeza"
  - "Shaun Smiley"
version_added: "2.3"
short_description: Manage mikrotik radius client
requirements:
  - mt_api
description:
  - Add or remove a radius client
options:
  hostname:
    description:
      - hotstname of mikrotik router
    required: True
  username:
    description:
      - username used to connect to mikrotik router
    required: True
  password:
    description:
      - password used for authentication to mikrotik router
    required: True
  state:
    description:
      - client present or absent
    required: True
    choices:
      - present
      - absent
  comment:
    description:
      - This module only ensures entries that match the comment field.
        Thus, you should make unique comments for every entry.
    required: True # only if state is present
  address:
    description:
      - IPv4 or IPv6 address of RADIUS server
    required: False
  secret:
    description:
      - Shared secret used to access the RADIUS server
     required: False
     default: null
  timeout:
    description:
      - Timeout after which the request should be resend
    required: False
     default: null
  service:
    description:
      - Router services that will use this RADIUS server:
    choices:
      - 'hotspot' # HotSpot authentication service
      - 'login'   # router's local user authentication
      - 'ppp      # Point-to-Point clients authentication
      - 'wireless # wireless client authentication (client's MAC address is sent as User-Name)
      - 'dhcp     # DHCP protocol client authentication (client's MAC address is sent as User-Name)IPv4 or IPv6 address of RADIUS server
    required: False
    default: null
  incoming:
    accept:
      choices: ['true', 'false' ]
    port: "3799"
    description:
      - Whether to accept the unsolicited messages.
        Also include the port number to listen for the requests on.
        Accept and port values must be strings
    required: False
    default: null
'''

EXAMPLES = '''
# Add a new radius entry
- mt_radius:
    hostname:      "{{ inventory_hostname }}"
    username:      "{{ mt_user }}"
    password:      "{{ mt_pass }}"
    state:         present
    address:       192.168.230.1
    comment:       ansible_test
    secret:       'password'
    service:
      - login
      - hotspot
      - wireless
    timeout:        '2s500ms'
'''

from ansible.module_utils import mt_api
from ansible.module_utils.basic import AnsibleModule


def main():
  module = AnsibleModule(
    argument_spec=dict(
      hostname= dict(required=True),
      username= dict(required=True),
      password= dict(required=True, no_log=True),
      address = dict(required=False, type='str'),
      comment = dict(required=True, type='str'),
      secret  = dict(required=False, type='str'),
      service = dict(required=False, type='list'),
      timeout = dict(required=False, type='str'),
      incoming= dict(required=False, type='dict'),
      state   = dict(
        required  = True,
        choices   = ['present', 'absent'],
        type      = 'str'
      ),
    ),
    supports_check_mode=True
  )

  hostname     = module.params['hostname']
  username     = module.params['username']
  password     = module.params['password']
  state        = module.params['state']
  check_mode   = module.check_mode
  changed      = False
  msg = ""

  radius_path = '/radius'
  mk = mt_api.Mikrotik(hostname, username, password)
  try:
    mk.login()
  except:
    module.fail_json(
        msg="Could not log into Mikrotik device." +
        " Check the username and password.",
    )

  response = mk.api_print(radius_path)
  radius_params = module.params

  ########################################################
  # Check if we need to edit the incoming radius settings
  ########################################################
  if radius_params['incoming'] is not None:
    incoming_path = '/radius/incoming'
    incoming_response = mk.api_print(incoming_path)
    incoming = radius_params['incoming']
    if incoming_response[0][1]['accept'] == incoming['accept']:
      if incoming_response[0][1]['port'] == incoming['port']:
        # nothing to do
        pass
      else:
        # edit port
        if not check_mode:
          mk.api_edit(base_path=incoming_path, params=incoming)
    else:
      # edit the accept and the port
      if not check_mode:
        mk.api_edit(base_path=incoming_path, params=incoming)
  #######################################
  # Since we are grabbing all the parameters passed by the module
  # We need to remove the one that won't be used
  # as mikrotik parameters
  remove_params = ['hostname', 'username', 'password', 'state', 'incoming']
  for i in remove_params:
    radius_params.pop(i)
  #######################################
  # remove keys with empty values
  # convert service list to stings
  ######################################
  for key in radius_params.keys():
    if radius_params[key] is None:
      radius_params.pop(key)


  #################################################
  # Convert service list to comma separated string
  #################################################
  list_to_string = ""
  if 'service' in radius_params:
    list_to_string = ','.join(map(str, radius_params['service']))
    radius_params['service'] = list_to_string

  ################################################
  # mikrotik_radius is the dictionary with the parameters
  # we get from mikrotik
  #################################
  # We grab the first radius item to
  # match the comment
  #################################
  mikrotik_radius = {}
  for i in response:
    if 'comment' in i[1]:
      if i[1]['comment'] == radius_params['comment']:
         mikrotik_radius = i[1]
         break

  ##########################################################
  # Define radius_id to be used by remove and edit function
  ##########################################################
  if '.id' in mikrotik_radius:
    radius_id = mikrotik_radius['.id']
  else:
    radius_id = False

  ######################################################
  # If the state is present and we can't find matching
  # radius comment we add a new item with all the parameters
  # from Ansible
  #######################################################
  if state == "present":
    if mikrotik_radius == {}:
      if not check_mode:
        mk.api_add(base_path=radius_path, params=radius_params)
      module.exit_json(
          failed=False,
          changed=True,
          msg="Added radius item",
      )
    ###################################################
    # If an item exists we check if all the parameters
    # match what we have in ansible
    ######################################
    else:
      radius_diff_keys = {}
      for key in radius_params:
        if radius_params[key] != mikrotik_radius[key]:
          radius_diff_keys[key] = radius_params[key]
      if radius_diff_keys != {}:
        radius_diff_keys['numbers'] = radius_id
        if not check_mode:
          mk.api_edit(base_path=radius_path, params=radius_diff_keys)
        module.exit_json(
            failed=False,
            changed=True,
            msg="Changed radius item: " + radius_params['comment']
        )
      else:
        ####################
        # Already up date
        module.exit_json(
            failed=False,
            changed=False,
        )
  elif state == "absent":
    if radius_id:
      if not check_mode:
        mk.api_remove(base_path=radius_path, remove_id=radius_id)
      module.exit_json(
          failed=False,
          changed=True,
          msg=radius_params['comment'] + " removed"
      )
    #####################################################
    # if radius_id is not set there is nothing to remove
    #####################################################
    else:
      module.exit_json(
          failed=False,
          changed=False,
      )
  else:
    module.exit_json(
        failed=True,
        changed=False,
    )
if __name__ == '__main__':
  main()


File: /library\mt_snmp.py
# -*- coding: utf-8 -*-
DOCUMENTATION = '''
module: mt_snmp
author:
  - "Valentin Gurmeza"
version_added: "2.4"
short_description: Manage mikrotik snmp endpoints
requirements:
  - mt_api
description:
  - Generic mikrotik snmp module.
options:
  hostname:
    description:
      - hotstname of mikrotik router
    required: True
  username:
    description:
      - username used to connect to mikrotik router
    required: True
  password:
    description:
      - password used for authentication to mikrotik router
    required: True
  parameter:
    description:
      - sub endpoint for mikrotik snmp
    required: True
    options:
      - community
      - snmp
  settings:
    description:
      - All Mikrotik compatible parameters for this particular endpoint.
        Any yes/no values must be enclosed in double quotes
  state:
    description:
      - absent or present
'''

EXAMPLES = '''
- mt_snmp:
    hostname:    "{{ inventory_hostname }}"
    username:    "{{ mt_user }}"
    password:    "{{ mt_pass }}"
    parameter:   community
    settings:
      addresses: "192.168.1.0/24"
      name: ansible_managed
'''

from ansible.module_utils.mt_common import clean_params, MikrotikIdempotent
from ansible.module_utils.basic import AnsibleModule



def main():
  module = AnsibleModule(
    argument_spec = dict(
      hostname  = dict(required=True),
      username  = dict(required=True),
      password  = dict(required=True, no_log=True),
      settings  = dict(required=False, type='dict'),
      parameter = dict(
        required  = True,
        choices   = ['community', 'snmp'],
        type      = 'str'
      ),
      state   = dict(
        required  = False,
        choices   = ['present', 'absent'],
        type      = 'str'
      ),
    ),
    supports_check_mode=True
  )

  idempotent_parameter = None
  params = module.params


  if params['parameter'] == 'community':
    idempotent_parameter = 'name'
    params['parameter'] = "snmp/community"

  mt_obj = MikrotikIdempotent(
    hostname         = params['hostname'],
    username         = params['username'],
    password         = params['password'],
    state            = params['state'],
    desired_params   = params['settings'],
    idempotent_param = idempotent_parameter,
    api_path         = '/' + str(params['parameter']),
    check_mode       = module.check_mode
  )

  mt_obj.sync_state()

  if mt_obj.failed:
    module.fail_json(
      msg = mt_obj.failed_msg
    )
  elif mt_obj.changed:
    module.exit_json(
      failed=False,
      changed=True,
      msg=mt_obj.changed_msg,
      diff={ "prepared": {
        "old": mt_obj.old_params,
        "new": mt_obj.new_params,
      }},
    )
  else:
    module.exit_json(
      failed=False,
      changed=False,
      msg=params['settings'],
    )

if __name__ == '__main__':
  main()


File: /library\mt_system.py
# -*- coding: utf-8 -*-
DOCUMENTATION = '''
module: mt_system.py
author:
  - "Valentin Gurmeza"
version_added: "2.4"
short_description: Manage mikrotik system endpoints
requirements:
  - mt_api
description:
  - manage mikrotik system parameters
options:
  hostname:
    description:
      - hotstname of mikrotik router
    required: True
  username:
    description:
      - username used to connect to mikrotik router
    required: True
  password:
    description:
      - password used for authentication to mikrotik router
    required: True
  parameter:
    description:
      - sub enpoint for mikrotik system
    required: True
    options:
      - ntp_client
      - clock
      - logging
      - routerboard
      - identity
  settings:
    description:
      - All Mikrotik compatible parameters for this particular endpoint.
        Any yes/no values must be enclosed in double quotes
  state:
    description:
      - absent or present
'''

EXAMPLES = '''
- mt_system:
    hostname:    "{{ inventory_hostname }}"
    username:    "{{ mt_user }}"
    password:    "{{ mt_pass }}"
    parameter:   identity
    settings:
        name:    test_ansible
'''

from ansible.module_utils.mt_common import clean_params, MikrotikIdempotent
from ansible.module_utils.basic import AnsibleModule



def main():
  module = AnsibleModule(
    argument_spec = dict(
      hostname  = dict(required=True),
      username  = dict(required=True),
      password  = dict(required=True, no_log=True),
      settings  = dict(required=False, type='dict'),
      parameter = dict(
        required  = True,
        choices   = ['ntp_client', 'clock', 'identity', 'logging', 'routerboard_settings'],
        type      = 'str'
      ),
      state   = dict(
        required  = False,
        choices   = ['present', 'absent'],
        type      = 'str'
      ),
    ),
    supports_check_mode=True
  )

  params = module.params

  if params['parameter'] == 'routerboard_settings':
    params['parameter'] = 'routerboard/settings'

  if params['parameter'] == 'ntp_client':
    params['parameter'] = 'ntp/client'

  clean_params(params['settings'])
  mt_obj = MikrotikIdempotent(
    hostname        = params['hostname'],
    username        = params['username'],
    password        = params['password'],
    state           = params['state'],
    desired_params  = params['settings'],
    idempotent_param= None,
    api_path        = '/system/' + params['parameter'],
    check_mode      = module.check_mode
  )

  mt_obj.sync_state()

  if mt_obj.failed:
    module.fail_json(
      msg = mt_obj.failed_msg
    )
  elif mt_obj.changed:
    module.exit_json(
      failed=False,
      changed=True,
      msg=mt_obj.changed_msg,
      diff={ "prepared": {
        "old": mt_obj.old_params,
        "new": mt_obj.new_params,
      }},
    )
  else:
    module.exit_json(
      failed=False,
      changed=False,
      #msg='',
      msg=params['settings'],
    )

if __name__ == '__main__':
  main()


File: /library\mt_system_scheduler.py
# -*- coding: utf-8 -*-
DOCUMENTATION = '''
module: mt_system_scheduler
author:
  - "Valentin Gurmeza"
version_added: "2.3"
short_description: Manage mikrotik system scheduler
requirements:
  - mt_api
description:
  - add, remove, or modify a system scheduler task
options:
  hostname:
    description:
      - hotstname of mikrotik router
    required: True
  username:
    description:
      - username used to connect to mikrotik router
    required: True
  password:
    description:
      - password used for authentication to mikrotik router
    required: True
  parameter:
    description:
      - sub endpoint for mikrotik system
    required: True
    options:
      - scheduler
  settings:
    description:
      - All Mikrotik compatible parameters for this particular endpoint.
        Any yes/no values must be enclosed in double quotes
    required: True
  state:
    description:
      - absent or present
    required: True
'''

EXAMPLES = '''
- mt_system_scheduler:
    hostname:      "{{ inventory_hostname }}"
    username:      "{{ mt_user }}"
    password:      "{{ mt_pass }}"
    state:         present
    parameter:     scheduler
      name:          test_by_ansible
      comment:       ansible_test
      on_event:      put "hello"
'''

from ansible.module_utils.mt_common import clean_params, MikrotikIdempotent
from ansible.module_utils.basic import AnsibleModule


def main():
  module = AnsibleModule(
    argument_spec=dict(
      hostname=dict(required=True),
      username=dict(required=True),
      password=dict(required=True, no_log=True),
      settings=dict(required=True, type='dict'),
      parameter = dict(
          required  = True,
          choices   = ['scheduler'],
          type      = 'str'
      ),
      state   = dict(
          required  = True,
          choices   = ['present', 'absent'],
          type      = 'str'
      )
    ),
    supports_check_mode=True
  )

  params = module.params
  idempotent_parameter = 'name'

  mt_obj = MikrotikIdempotent(
    hostname         = params['hostname'],
    username         = params['username'],
    password         = params['password'],
    state            = params['state'],
    desired_params   = params['settings'],
    idempotent_param = idempotent_parameter,
    api_path         = '/system/' + str(params['parameter']),
    check_mode       = module.check_mode
  )

  # exit if login failed
  if not mt_obj.login_success:
    module.fail_json(
      msg = mt_obj.failed_msg
    )

  # add, remove or edit things
  mt_obj.sync_state()

  if mt_obj.failed:
      module.fail_json(
        msg = mt_obj.failed_msg
      )
  elif mt_obj.changed:
    module.exit_json(
      failed=False,
      changed=True,
      msg=mt_obj.changed_msg,
      diff={ "prepared": {
          "old": mt_obj.old_params,
          "new": mt_obj.new_params,
      }},
    )
  else:
    module.exit_json(
      failed=False,
      changed=False,

      msg=params['settings'],
    )

if __name__ == '__main__':
  main()


File: /library\mt_tool.py
# -*- coding: utf-8 -*-
DOCUMENTATION = '''
module: mt_tool
author:
  - "Valentin Gurmeza"
version_added: "2.4"
short_description: Manage mikrotik tool endpoints
requirements:
  - mt_api
description:
  - Generic mikrotik tool module.
options:
  hostname:
    description:
      - hotstname of mikrotik router
    required: True
  username:
    description:
      - username used to connect to mikrotik router
    required: True
  password:
    description:
      - password used for authentication to mikrotik router
    required: True
  parameter:
    description:
      - sub endpoint for mikrotik tool
    required: True
    options:
      - netwatch
      - e-mail
  settings:
    description:
      - All Mikrotik compatible parameters for this particular endpoint.
        Any yes/no values must be enclosed in double quotes
  state:
    description:
      - absent or present
'''

EXAMPLES = '''
- mt_tool:
    hostname:    "{{ inventory_hostname }}"
    username:    "{{ mt_user }}"
    password:    "{{ mt_pass }}"
    parameter:   e-mail
    settings:
      address: 192.168.1.1
      from:    foo@bar.com
'''

from ansible.module_utils.mt_common import clean_params, MikrotikIdempotent
from ansible.module_utils.basic import AnsibleModule


def main():
  module = AnsibleModule(
    argument_spec = dict(
      hostname  = dict(required=True),
      username  = dict(required=True),
      password  = dict(required=True, no_log=True),
      settings  = dict(required=False, type='dict'),
      parameter = dict(
        required  = True,
        choices   = ['e-mail', 'netwatch'],
        type      = 'str'
      ),
      state   = dict(
        required  = False,
        choices   = ['present', 'absent'],
        type      = 'str'
      ),
    ),
    supports_check_mode=True
  )

  idempotent_parameter = None
  params = module.params

  if params['parameter'] == 'netwatch':
    idempotent_parameter = 'host'

#    clean_params(params['settings'])

  mt_obj = MikrotikIdempotent(
    hostname         = params['hostname'],
    username         = params['username'],
    password         = params['password'],
    state            = params['state'],
    desired_params   = params['settings'],
    idempotent_param = idempotent_parameter,
    api_path         = '/tool/' + str(params['parameter']),
    check_mode       = module.check_mode

  )

  mt_obj.sync_state()

  if mt_obj.failed:
    module.fail_json(
      msg=mt_obj.failed_msg
    )
  elif mt_obj.changed:
    module.exit_json(
      failed=False,
      changed=True,
      msg=mt_obj.changed_msg,
      diff={"prepared": {
        "old": mt_obj.old_params,
        "new": mt_obj.new_params,
      }},
    )
  else:
      module.exit_json(
          failed=False,
          changed=False,
          msg=params['settings'],
      )

if __name__ == '__main__':
  main()


File: /library\mt_user.py
# -*- coding: utf-8 -*-
DOCUMENTATION = '''
module: mt_user
author:
  - "Valentin Gurmeza"
version_added: "2.4"
short_description: Manage mikrotik user endpoints
requirements:
  - mt_api
description:
  - Generic mikrotik user module.
options:
  hostname:
    description:
      - hotstname of mikrotik router
    required: True
  username:
    description:
      - username used to connect to mikrotik router
    required: True
  password:
    description:
      - password used for authentication to mikrotik router
    required: True
  parameter:
    description:
      - sub endpoint for mikrotik user
    required: True
    options:
      - user
      - active
      - aaa
  settings:
    description:
      - All Mikrotik compatible parameters for this particular endpoint.
        Any yes/no values must be enclosed in double quotes
  state:
    description:
      - absent or present
'''

EXAMPLES = '''
- mt_user:
    hostname:    "{{ inventory_hostname }}"
    username:    "{{ mt_user }}"
    password:    "{{ mt_pass }}"
    parameter:   user
    settings:
      name:  test1
      group: read
'''

from ansible.module_utils.mt_common import clean_params, MikrotikIdempotent
from ansible.module_utils.basic import AnsibleModule



def main():
  module = AnsibleModule(
    argument_spec = dict(
      hostname  = dict(required=True),
      username  = dict(required=True),
      password  = dict(required=True, no_log=True),
      settings  = dict(required=False, type='dict'),
      parameter = dict(
        required  = True,
        choices   = ['user', 'active', 'aaa'],
        type      = 'str'
      ),
      state   = dict(
        required  = False,
        choices   = ['present', 'absent'],
        type      = 'str'
      ),
    ),
    supports_check_mode=True
  )

  idempotent_parameter = None
  params = module.params
  idempotent_parameter = 'name'

  if params['parameter'] == 'group':
    params['parameter'] = 'user/group'
  mt_obj = MikrotikIdempotent(
    hostname         = params['hostname'],
    username         = params['username'],
    password         = params['password'],
    state            = params['state'],
    desired_params   = params['settings'],
    idempotent_param = idempotent_parameter,
    api_path         = '/' + str(params['parameter']),
    check_mode      = module.check_mode
  )

  mt_obj.sync_state()

  if mt_obj.failed:
    module.fail_json(
      msg = mt_obj.failed_msg
    )
  elif mt_obj.changed:
    module.exit_json(
      failed=False,
      changed=True,
      msg=mt_obj.changed_msg,
      diff={ "prepared": {
        "old": mt_obj.old_params,
        "new": mt_obj.new_params,
      }},
    )
  else:
    module.exit_json(
      failed=False,
      changed=False,
      #msg='',
      msg=params['settings'],
    )

if __name__ == '__main__':
  main()


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
      boilerplate notice, with the fields enclosed by brackets "{}"
      replaced with your own identifying information. (Don't include
      the brackets!)  The text should be enclosed in the appropriate
      comment syntax for the file format. We also recommend that a
      file or class name and description of purpose be included on the
      same "printed page" as the copyright notice for easier
      identification within third-party archives.

   Copyright {yyyy} {name of copyright owner}

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
url = "https://pypi.python.org/simple"
verify_ssl = true

[packages]
ansible = "2.4.2.0"


File: /Pipfile.lock
{
    "_meta": {
        "hash": {
            "sha256": "1973d9e9e2050096ddc5b35f2633f9d83cecb5d93937c9ee1d2d9948e832fc8c"
        },
        "requires": {},
        "sources": [
            {
                "url": "https://pypi.python.org/simple",
                "verify_ssl": true
            }
        ]
    },
    "default": {
        "Jinja2": {
            "hash": "sha256:74c935a1b8bb9a3947c50a54766a969d4846290e1e788ea44c1392163723c3bd",
            "version": "==2.10"
        },
        "MarkupSafe": {
            "hash": "sha256:a6be69091dac236ea9c6bc7d012beab42010fa914c459791d627dad4910eb665",
            "version": "==1.0"
        },
        "PyNaCl": {
            "hash": "sha256:0bfa0d94d2be6874e40f896e0a67e290749151e7de767c5aefbad1121cad7512",
            "version": "==1.2.1"
        },
        "PyYAML": {
            "hash": "sha256:592766c6303207a20efc445587778322d7f73b161bd994f227adaa341ba212ab",
            "version": "==3.12"
        },
        "ansible": {
            "hash": "sha256:315f1580b20bbc2c2f1104f8b5e548c6b4cac943b88711639c5e0d4dfc4d7658",
            "version": "==2.4.2.0"
        },
        "asn1crypto": {
            "hash": "sha256:2f1adbb7546ed199e3c90ef23ec95c5cf3585bac7d11fb7eb562a3fe89c64e87",
            "version": "==0.24.0"
        },
        "bcrypt": {
            "hash": "sha256:0f317e4ffbdd15c3c0f8ab5fbd86aa9aabc7bea18b5cc5951b456fe39e9f738c",
            "version": "==3.1.4"
        },
        "cffi": {
            "hash": "sha256:248198cb714fe09f5c60b6acba3675d52199c6142641536796cdf89dd45e5590",
            "version": "==1.11.2"
        },
        "cryptography": {
            "hash": "sha256:69285f5615507b6625f89ea1048addd1d9218585fb886eb90bdebb1d2b2d26f5",
            "version": "==2.1.4"
        },
        "enum34": {
            "hash": "sha256:6bd0f6ad48ec2aa117d3d141940d484deccda84d4fcd884f5c3d93c23ecd8c79",
            "version": "==1.1.6"
        },
        "idna": {
            "hash": "sha256:8c7309c718f94b3a625cb648ace320157ad16ff131ae0af362c9f21b80ef6ec4",
            "version": "==2.6"
        },
        "ipaddress": {
            "hash": "sha256:200d8686011d470b5e4de207d803445deee427455cd0cb7c982b68cf82524f81",
            "version": "==1.0.19"
        },
        "paramiko": {
            "hash": "sha256:8851e728e8b7590989e68e3936c48ee3ca4dad91d29e3d7ff0305b6c5fc582db",
            "version": "==2.4.0"
        },
        "pyasn1": {
            "hash": "sha256:d5cd6ed995dba16fad0c521cfe31cd2d68400b53fcc2bce93326829be73ab6d1",
            "version": "==0.4.2"
        },
        "pycparser": {
            "hash": "sha256:99a8ca03e29851d96616ad0404b4aad7d9ee16f25c9f9708a11faf2810f7b226",
            "version": "==2.18"
        },
        "setuptools": {
            "hash": "sha256:155c2ec9fdcc00c3973d966b416e1cf3a1e7ce75f4c09fb760b23f94b935926e",
            "version": "==38.4.0"
        },
        "six": {
            "hash": "sha256:832dc0e10feb1aa2c68dcc57dbb658f1c7e65b9b61af69048abc87a2db00a0eb",
            "version": "==1.11.0"
        }
    },
    "develop": {}
}

File: /pythonlibs\mt_api\retryloop.py
# retry loop from http://code.activestate.com/recipes/578163-retry-loop/
import time
import sys


class RetryError(Exception):
    pass


def retryloop(attempts, timeout=None, delay=0, backoff=1):
    starttime = time.time()
    success = set()
    for i in range(attempts): 
        success.add(True)
        yield success.clear
        if success:
            return
        duration = time.time() - starttime
        if timeout is not None and duration > timeout:
            break
        if delay:
            time.sleep(delay)
            delay *= backoff

    e = sys.exc_info()[1]

    # No pending exception? Make one
    if e is None:
        try:
            raise RetryError
        except RetryError as exc:
            e = exc

    # Decorate exception with retry information:
    e.args = e.args + ("on attempt {0} of {1} after {2:.3f} seconds".format(
        i + 1, attempts, duration), )

    raise e


File: /pythonlibs\mt_api\socket_utils.py
import socket


# http://stackoverflow.com/a/14855726
def set_keepalive(sock, after_idle_sec=1, interval_sec=3, max_fails=5):
    """Set TCP keepalive on an open socket.

    It activates after 1 second (after_idle_sec) of idleness,
    then sends a keepalive ping once every 3 seconds (interval_sec),
    and closes the connection after 5 failed ping (max_fails), or 15 seconds
    """
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_KEEPALIVE, 1)
    sock.setsockopt(socket.IPPROTO_TCP, socket.TCP_KEEPIDLE, after_idle_sec)
    sock.setsockopt(socket.IPPROTO_TCP, socket.TCP_KEEPINTVL, interval_sec)
    sock.setsockopt(socket.IPPROTO_TCP, socket.TCP_KEEPCNT, max_fails)


File: /pythonlibs\mt_api\__init__.py
from __future__ import unicode_literals

import binascii
import hashlib
import logging
import socket
import ssl
import sys

from ansible.module_utils.mt_api.retryloop import RetryError
from ansible.module_utils.mt_api.retryloop import retryloop
from ansible.module_utils.mt_api.socket_utils import set_keepalive

PY2 = sys.version_info[0] < 3
logger = logging.getLogger(__name__)


class RosAPIError(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        if isinstance(self.value, dict) and self.value.get('message'):
            return self.value['message']
        elif isinstance(self.value, list):
            elements = (
                '%s: %s' %
                (element.__class__, str(element)) for element in self.value
            )
            return '[%s]' % (', '.join(element for element in elements))
        else:
            return str(self.value)


class RosAPIConnectionError(RosAPIError):
    pass


class RosAPIFatalError(RosAPIError):
    pass


class RosApiLengthUtils(object):
    def __init__(self, api):
        self.api = api

    def write_lenght(self, length):
        self.api.write_bytes(self.length_to_bytes(length))

    def length_to_bytes(self, length):
        if length < 0x80:
            return self.to_bytes(length)
        elif length < 0x4000:
            length |= 0x8000
            return self.to_bytes(length, 2)
        elif length < 0x200000:
            length |= 0xC00000
            return self.to_bytes(length, 3)
        elif length < 0x10000000:
            length |= 0xE0000000
            return self.to_bytes(length, 4)
        else:
            return self.to_bytes(0xF0) + self.to_bytes(length, 4)

    def read_length(self):
        b = self.api.read_bytes(1)
        i = self.from_bytes(b)
        if (i & 0x80) == 0x00:
            return i
        elif (i & 0xC0) == 0x80:
            return self._unpack(1, i & ~0xC0)
        elif (i & 0xE0) == 0xC0:
            return self._unpack(2, i & ~0xE0)
        elif (i & 0xF0) == 0xE0:
            return self._unpack(3, i & ~0xF0)
        elif (i & 0xF8) == 0xF0:
            return self.from_bytes(self.api.read_bytes(1))
        else:
            raise RosAPIFatalError('Unknown value: %x' % i)

    def _unpack(self, times, i):
        temp1 = self.to_bytes(i)
        temp2 = self.api.read_bytes(times)
        try:
            temp3 = temp2.decode('utf-8')
        except:
            try:
                temp3 = temp2.decode('windows-1252')
            except Exception:
                print("Cannot decode response properly:", temp2)
                print(Exception)
                exit(1)

        res = temp1 + temp3
        return self.from_bytes(res)

    if PY2:
        def from_bytes(self, data):
            data_values = [ord(char) for char in data]
            value = 0
            for byte_value in data_values:
                value <<= 8
                value += byte_value
            return value

        def to_bytes(self, i, size=1):
            data = []
            for _ in xrange(size):
                data.append(chr(i & 0xff))
                i >>= 8
            return b''.join(reversed(data))
    else:
        def from_bytes(self, data):
            return int.from_bytes(data, 'big')

        def to_bytes(self, i, size=1):
            return i.to_bytes(size, 'big')


class RosAPI(object):
    """Routeros api"""

    def __init__(self, socket):
        self.socket = socket
        self.length_utils = RosApiLengthUtils(self)

    def login(self, username, pwd):
        for _, attrs in self.talk([b'/login']):
            token = binascii.unhexlify(attrs[b'ret'])
        hasher = hashlib.md5()
        hasher.update(b'\x00')
        hasher.update(pwd)
        hasher.update(token)
        self.talk([b'/login', b'=name=' + username,
                   b'=response=00' + hasher.hexdigest().encode('ascii')])

    def talk(self, words):
        if self.write_sentence(words) == 0:
            return
        output = []
        while True:
            input_sentence = self.read_sentence()
            if not len(input_sentence):
                continue
            attrs = {}
            reply = input_sentence.pop(0)
            for line in input_sentence:
                try:
                    second_eq_pos = line.index(b'=', 1)
                except IndexError:
                    attrs[line[1:]] = b''
                else:
                    attrs[line[1:second_eq_pos]] = line[second_eq_pos + 1:]
            output.append((reply, attrs))
            if reply == b'!done':
                if output[0][0] == b'!trap':
                    raise RosAPIError(output[0][1])
                if output[0][0] == b'!fatal':
                    self.socket.close()
                    raise RosAPIFatalError(output[0][1])
                return output

    def write_sentence(self, words):
        words_written = 0
        for word in words:
            self.write_word(word)
            words_written += 1
        self.write_word(b'')
        return words_written

    def read_sentence(self):
        sentence = []
        while True:
            word = self.read_word()
            if not len(word):
                return sentence
            sentence.append(word)

    def write_word(self, word):
        logger.debug('>>> %s' % word)
        self.length_utils.write_lenght(len(word))
        self.write_bytes(word)

    def read_word(self):
        word = self.read_bytes(self.length_utils.read_length())
        logger.debug('<<< %s' % word)
        return word

    def write_bytes(self, data):
        sent_overal = 0
        while sent_overal < len(data):
            try:
                sent = self.socket.send(data[sent_overal:])
            except socket.error as e:
                raise RosAPIConnectionError(str(e))
            if sent == 0:
                raise RosAPIConnectionError('Connection closed by remote end.')
            sent_overal += sent

    def read_bytes(self, length):
        received_overal = b''
        while len(received_overal) < length:
            try:
                received = self.socket.recv(
                    length - len(received_overal))
            except socket.error as e:
                raise RosAPIConnectionError(str(e))
            if len(received) == 0:
                raise RosAPIConnectionError('Connection closed by remote end.')
            received_overal += received
        return received_overal




class BaseRouterboardResource(object):
    def __init__(self, api, namespace):
        self.api = api
        self.namespace = namespace

    def call(self, command, set_kwargs, query_kwargs=None):
        query_kwargs = query_kwargs or {}
        query_arguments = self._prepare_arguments(True, **query_kwargs)
        set_arguments = self._prepare_arguments(False, **set_kwargs)
        query = ([('%s/%s' % (self.namespace, command)).encode('ascii')] +
                 query_arguments + set_arguments)
        response = self.api.api_client.talk(query)

        output = []
        for response_type, attributes in response:
            if response_type == b'!re':
                output.append(self._remove_first_char_from_keys(attributes))

        return output

    @staticmethod
    def _prepare_arguments(is_query, **kwargs):
        command_arguments = []
        for key, value in kwargs.items():
            if key in ['id', 'proplist']:
                key = '.%s' % key
            key = key.replace('_', '-')
            selector_char = '?' if is_query else '='
            command_arguments.append(
                ('%s%s=' % (selector_char, key)).encode('ascii') + value)

        return command_arguments

    @staticmethod
    def _remove_first_char_from_keys(dictionary):
        elements = []
        for key, value in dictionary.items():
            key = key.decode('ascii')
            if key in ['.id', '.proplist']:
                key = key[1:]
            elements.append((key, value))
        return dict(elements)

    def get(self, **kwargs):
        return self.call('print', {}, kwargs)

    def detailed_get(self, **kwargs):
        return self.call('print', {'detail': b''}, kwargs)

    def set(self, **kwargs):
        return self.call('set', kwargs)

    def add(self, **kwargs):
        return self.call('add', kwargs)

    def remove(self, **kwargs):
        return self.call('remove', kwargs)


class RouterboardResource(BaseRouterboardResource):
    def detailed_get(self, **kwargs):
        return self.call('print', {'detail': ''}, kwargs)

    def call(self, command, set_kwargs, query_kwargs=None):
        query_kwargs = query_kwargs or {}
        result = super(RouterboardResource, self).call(
            command, self._encode_kwargs(set_kwargs),
            self._encode_kwargs(query_kwargs))
        for item in result:
            for k in item:
                item[k] = item[k].decode('ascii')
        return result

    def _encode_kwargs(self, kwargs):
        return dict((k, v.encode('ascii')) for k, v in kwargs.items())


class RouterboardAPI(object):
    def __init__(self, host, username='api', password='', port=8728, ssl=False):
        self.host = host
        self.username = username
        self.password = password
        self.socket = None
        self.port = port
        self.ssl = ssl
        self.reconnect()

    def __enter__(self):
        return self

    def __exit__(self, _, __, ___):
        self.close_connection()

    def reconnect(self):
        if self.socket:
            self.close_connection()
        try:
            for retry in retryloop(10, delay=0.1, timeout=30):
                try:
                    self.connect()
                    self.login()
                except socket.error:
                    retry()
        except (socket.error, RetryError) as e:
            raise RosAPIConnectionError(str(e))

    def connect(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(15.0)
        sock.connect((self.host, self.port))
        set_keepalive(sock, after_idle_sec=10)
        if self.ssl:
            try:
                self.socket = ssl.wrap_socket(sock)
            except ssl.SSLError as e:
                raise RosAPIConnectionError(str(e))
        else:
            self.socket = sock
        self.api_client = RosAPI(self.socket)

    def login(self):
        self.api_client.login(self.username.encode('ascii'),
                              self.password.encode('ascii'))

    def get_resource(self, namespace):
        return RouterboardResource(self, namespace)

    def get_base_resource(self, namespace):
        return BaseRouterboardResource(self, namespace)

    def close_connection(self):
        self.socket.close()


class Mikrotik(object):

  def __init__(self, hostname, username, password):
    self.hostname = hostname
    self.username = username
    self.password = password

  def login(self):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((self.hostname, 8728))
    mt = RosAPI(s)
    mt.login(self.username, self.password)
    return mt

  def talk(self, talk_command):
    r = self.login()
    response = r.talk(talk_command)
    return(response)

  def api_print(self, base_path, params=None):
    command = [base_path + '/print']
    if params is not None:
      for key, value in params.iteritems():
        item = b'=' + key + '=' + str(value)
        command.append(item)

    return self.talk(command)

  def api_add(self, base_path, params):
    command = [base_path + '/add']
    for key, value in params.iteritems():
      item = b'=' + key + '=' + str(value)
      command.append(item)

    return self.talk(command)

  def api_edit(self, base_path, params):
    command = [base_path + '/set']
    for key, value in params.iteritems():
      item = b'=' + key + '=' + str(value)
      command.append(item)

    return self.talk(command)

  def api_remove(self, base_path, remove_id):
    command = [
        base_path + '/remove',
        b'=.id=' + remove_id
    ]

    return self.talk(command)

  def api_command(self, base_path, params=None):
    command = [base_path]
    if params is not None:
      for key, value in params.iteritems():
        item = b'=' + key + '=' + str(value)
        command.append(item)

    return self.talk(command)


File: /pythonlibs\mt_common.py
#!/usr/bin/env python
from ansible.module_utils import mt_api
import re
import sys
import socket


def list_to_string(list):
  list_string = ""
  list_string = ','.join(map(str, list))
  return list_string


def clean_params(params):
  '''
  remove keys with empty values
  modify keys with '_' to match mikrotik parameters
  convert yes/no to true/false
  '''
  if isinstance(params, dict):
    for key in list(params):
      if params[key] is None:
        del params[key]
        continue

      new_key = re.sub('_', '-', key)
      if new_key != key:
        params[new_key] = str(params[key])
        del params[key]
        continue

      if params[key] == "yes":
        params[key] = "true"
      if params[key] == "no":
        params[key] = "false"
  else:
    print("Must be a dictionary")


class MikrotikIdempotent():
  '''
  MikrotikIdempotent Class
    - A helper class for Ansible modules to abstract common functions.

  Example Usage:
    mt_obj = MikrotikIdempotent(
      hostname        = params['hostname'],
      username        = params['username'],
      password        = params['password'],
      state           = None,
      desired_params  = params['settings'],
      idempotent_param= 'name',
      api_path        = '/interface/ethernet',
    )

    mt_obj.sync_state()
  '''

  def __init__(
   self, hostname, username, password, desired_params, api_path,
   state, idempotent_param, check_mode=False):

    self.hostname         = hostname
    self.username         = username
    self.password         = password
    self.state            = state
    self.desired_params   = desired_params
    self.idempotent_param = idempotent_param
    self.current_params   = {}
    self.api_path         = api_path
    self.check_mode       = check_mode

    self.login_success    = False
    self.changed          = False
    self.changed_msg      = []
    self.failed           = False
    self.failed_msg       = []

    self.login()

  def login(self):
    self.mk = mt_api.Mikrotik(
      self.hostname,
      self.username,
      self.password,
    )
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = sock.connect_ex((self.hostname, 8728))
    if result == 0:
      try:
        self.mk.login()
        self.login_success = True
      except Exception as e:
        self.failed_msg = "Could not log into Mikrotik device." + " Check the username and password. Exception {} - {}".format(type(e), e),
    else:
        self.failed_msg = "Could not access RouterOS api." + " Verify API service is enabled and not blocked by firewall.",


  def get_current_params(self):
    clean_params(self.desired_params)
    self.param_id = None
    self.current_param = None
    self.current_params = self.mk.api_print(base_path=self.api_path)

    # When state and idempotent_param is None we are working
    # on editable params only and we are grabbing the only item from response
    if self.state is None and self.idempotent_param is None:
      self.current_param = self.current_params[0][1]

    # Else we iterate over every item in the list until we find the matching
    # params
    # We also set the param_id here to reference later for editing or removal
    else:
      for current_param in self.current_params:
        if self.idempotent_param in current_param[1]:
          if self.desired_params[self.idempotent_param] == current_param[1][self.idempotent_param]:
            self.current_param = current_param[1]
            self.param_id = current_param[1]['.id']
            # current_param now is a dict, something like:
            # {
            #    ".id": "*1",
            #    "full-duplex": "true",
            #    "mac-address": "08:00:27:6F:4C:22",
            #    "mtu": "1500",
            #    "name": "ether1",
            #    ...
            # }

  def add(self):
    # When current_param is empty we need to call api_add method to add
    # all the parameters in the desired_params
    if self.current_param is None:
      # check if we have a list within the dictionary
      # convert the list to string to pass to mikrotik
      for i in self.desired_params:
        if isinstance(self.desired_params[i], list):
          self.desired_params[i] = list_to_string(self.desired_params[i])
      self.new_params = self.desired_params
      self.old_params = ""
      if not self.check_mode:
          self.mk.api_add(
              base_path = self.api_path,
              params    = self.desired_params,
          )
      self.changed = True

    # Else we need to determing what the difference between the currently
    # and the desired
    else:
      self.edit()

  def rem(self):
    # if param_id is set this means there is currently a matching item
    # which we will remove
    if self.param_id:
      self.new_params = "item removed"
      self.old_params = self.desired_params
      if not self.check_mode:
        self.mk.api_remove(
            base_path=self.api_path,
            remove_id=self.param_id,
        )
      self.changed = True

  def edit(self):
    # out_params is used to pass to api_edit() to make changes
    # to a mikrotik device
    out_params = {}
    # old_params used storing old values that are going to be changed
    # to aid in the diff output
    old_params = {}  # used to store values of params we change

    # iterate over items in desired params and
    # match against items in current_param
    # to figure out the difference
    for desired_param in self.desired_params:
      # check if a desired item is already set in mikrotik
      if desired_param in self.current_param:
        # check if we have a list within the dictionary
        # convert mikrotik string to list to get a diff
        if isinstance(self.desired_params[desired_param], list):
          if desired_param in self.current_param:
            current_param_list = self.current_param[desired_param].split(',')
            if set(self.desired_params[desired_param]) != set(current_param_list):
              out_params[desired_param] = list_to_string(self.desired_params[desired_param])
              old_params[desired_param] = str(self.current_param[desired_param])
          else:
            out_params[desired_param] = list_to_string(self.desired_params[desired_param])
        # value is not a list, move on and identify difference
        else:
          if self.current_param[desired_param] != str(self.desired_params[desired_param]):
            out_params[desired_param] = str(self.desired_params[desired_param])
            old_params[desired_param] = str(self.current_param[desired_param])
      # since we didn't get a matching key from mikrotik settings
      # we'll it the out_params to whatever is desired_param
      else:
        if isinstance(desired_param, list):
          out_params[desired_param] = list_to_string(self.desired_params[desired_param])
        else:
          out_params[desired_param] = str(self.desired_params[desired_param])

    # When out_params has been set it means we found our diff
    # and will set it on the mikrotik
    if out_params:
      if self.param_id is not None:
        out_params['.id'] = self.current_param['.id']

      if not self.check_mode:
        self.mk.api_edit(
            base_path = self.api_path,
            params    = out_params,
        )

      # we don't need to show the .id in the changed message
      if '.id' in out_params:
        del out_params['.id']

      self.changed_msg.append({
          "new_params":   out_params,
          "old_params":   old_params,
      })

      self.new_params = out_params
      self.old_params = old_params
      self.changed = True

  def sync_state(self):
    self.get_current_params()

    # When state and idempotent_param are not set we are working
    # on editable parameters only that we can't add or remove
    if self.state is None and self.idempotent_param is None:
      self.edit()
    elif self.state == "absent":
      self.rem()
    elif self.state == "present" or self.idempotent_param:
      self.add()


File: /README.md
Ansible MikroTik modules
========================

Introduction
------------

This repository provides Ansible modules to manage MikroTik RouterOS-based
devices.

Requirements
------------

Ansible=2.4.2.0

At this time there are no external dependencies. However, there are additional
Python modules that are required by the Ansible modules. You may find these in
`pythonlibs`. Before using Ansible you should add these libraries to your
Python path:
`export PYTHONPATH="$PYTHONPATH:$PWD/pythonlibs"`

Development
-----------
-----------

In order to test this module, you'll need a RouterOS instance to target. If you
have an existing RouterOS-based MikroTik device, you need only make sure the
API service is enabled.

AWS EC2
-------
You can use an ec2 CHR image for testing. Keep in mind that as of right now we can only set up two interfaces on most ec2 instances.
https://aws.amazon.com/marketplace/pp/B01E00PU50?qid=1517274040207&sr=0-1&ref_=srh_res_product_title

Vagrant
-------
This repository provides a Vagrantfile for setting up the x86 build
of RouterOS for testing. To use it, you must first ensure Vagrant and
VirtualBox are installed. Then, run `./create_vagrant_mikrotik.sh` to download
the official MikroTik Cloud Hosted Router (CHR) image from MikroTik, package
it as a Vagrant .box file, and register the .box with Vagrant.

Then, you need only run `vagrant up` in the repository root to start the CHR.

Ansible setup
------------

To use pipenv ensure pipenv is installed:

`pip install pipenv`

Then enable virtualenv and install dependencies:

`pipenv shell`

`pipenv install`

Installing
----------

These modules are still in a very early stage of development; stay tuned for
installation instructions later! :)


File: /tasks\backup_recover.yml
---
################################################################
# TEMPORARY PLAYBOOK TO STORE THE ROLLBACK PROCEDURE
#######################################################################

###################################################################
# create a backup and add a scheduler to rollback if we lose connection
# to the a mikrotik device during the ansible run.
# Place this in the begging of your playbook
#####################################################################
- name: run command module to create a backup
  mt_command:
    hostname: "{{ mt_hostname }}"
    username: "{{ mt_user }}"
    password: "{{ mt_pass }}"
    command: /system/backup/save
    command_arguments:
      name: pre_deploy
      password: 123

- name: add rollback scheduler task
  mt_system_scheduler:
    hostname: "{{ mt_hostname }}"
    username: "{{ mt_user }}"
    password: "{{ mt_pass }}"
    state:    present
    name:     rollback
    on_event: /system backup load name=pre_deploy.backup password=123
    interval: 30m
    policy:
      - password
      - reboot
      - write
      - sensitive
      - test
      - read
      - policy

###################################################################
# Place this in the end of your mikrotik playbook this will remove the
# rollback scheduler task if the playbook runs successfully
#####################################################################
- name: remove rollback scheduler task if run succesfull
  hosts: govsat
  gather_facts: no
  connection: local
  tasks:
    - mt_system_scheduler:
        hostname: "{{ mt_hostname }}"
        username: "{{ mt_user }}"
        password: "{{ mt_pass }}"
        state:    absent
        name:     rollback


File: /tasks\main.yml
---
- name: set ip
  mikrotik:
    interface: "ether6-master"
    ip_addr: "192.168.50.1"


File: /tests\integration\ansible.cfg
[defaults]
module_utils   = ./pythonlibs/


File: /tests\integration\library
../../library/

File: /tests\integration\pythonlibs
../../pythonlibs/

File: /tests\integration\run_tests.sh
#!/usr/bin/env bash

ABSOLUTE_PATH="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
pushd .

cd "$ABSOLUTE_PATH"
ansible-playbook tests.yml --diff -i 127.0.0.1, $@

popd  >/dev/null


File: /tests\integration\tasks\hotspot-tests.yml
- name: add a hotspot profile
  mt_hotspot:
    hostname: "{{ mt_hostname }}"
    username: "{{ mt_user }}"
    password: "{{ mt_pass }}"
    state:    present
    parameter: profile
    settings:
      dns-name: internet.com
      login-by: http-pap
      name: Hotspot1
      radius-interim-update: 3m
      use-radius: "yes"

- name: NEVER_CHANGES add a hotspot profile, check idempotency
  mt_hotspot:
    hostname: "{{ mt_hostname }}"
    username: "{{ mt_user }}"
    password: "{{ mt_pass }}"
    parameter: profile
    state:    present
    settings:
      dns-name: internet.com
      login-by: http-pap
      name: Hotspot1
      radius-interim-update: 3m
      use-radius: "yes"
  register: profile_add
  failed_when: (
      not ansible_check_mode
    ) and (
      ( profile_add | changed )
    )

- name: ALWAYS_CHANGES edit a hotspot profile, check changes
  mt_hotspot:
    hostname: "{{ mt_hostname }}"
    username: "{{ mt_user }}"
    password: "{{ mt_pass }}"
    parameter: profile
    state:    present
    settings:
      dns-name: internet.com
      login-by: http-pap
      name: Hotspot1
      radius-interim-update: 4m
      use-radius: "yes"
  register: profile_edit
  failed_when: not  ( profile_edit | changed )

- name: add a hotspot
  mt_hotspot:
    hostname: "{{ mt_hostname }}"
    username: "{{ mt_user }}"
    password: "{{ mt_pass }}"
    parameter: hotspot
    state:    present
    settings:
      address-pool: pool1
      disabled: "no"
      interface: ether2
      name: NETACCESS1
      profile: Hotspot1
      idle-timeout: 3s

- name: NEVER_CHANGES add a hotspot again, check idempotency
  mt_hotspot:
    hostname: "{{ mt_hostname }}"
    username: "{{ mt_user }}"
    password: "{{ mt_pass }}"
    state:    present
    parameter: hotspot
    settings:
      address-pool: pool1
      disabled: "no"
      interface: ether2
      name: NETACCESS1
      profile: Hotspot1
      idle-timeout: 3s
  register: hotspot_add
  failed_when: (
      not ansible_check_mode
    ) and (
      ( hotspot_add | changed )
    )

- name: ALWAYS_CHANGES edit a hotspot, check changes
  mt_hotspot:
    hostname: "{{ mt_hostname }}"
    username: "{{ mt_user }}"
    password: "{{ mt_pass }}"
    state:    present
    parameter: hotspot
    settings:
      address-pool: pool1
      disabled: "no"
      interface: ether2
      name: NETACCESS1
      profile: Hotspot1
      idle-timeout: 4s
  register: hotspot_edit
  failed_when: not ( hotspot_edit | changed )

- name: add a walled-garden
  mt_hotspot:
    hostname: "{{ mt_hostname }}"
    username: "{{ mt_user }}"
    password: "{{ mt_pass }}"
    state:    present
    parameter: walled-garden
    settings:
      comment: "Allow Personal Web Portal"
      dst-host: google.com
      server: NETACCESS1
      method: PUT

- name: NEVER_CHANGES add a walled-garden, check idempotency
  mt_hotspot:
    hostname: "{{ mt_hostname }}"
    username: "{{ mt_user }}"
    password: "{{ mt_pass }}"
    state:    present
    parameter: walled-garden
    settings:
      comment: "Allow Personal Web Portal"
      dst-host: google.com
      server: NETACCESS1
      method: PUT
  register: walled_garden_add
  failed_when: (
      not ansible_check_mode
    ) and (
      ( walled_garden_add | changed )
    )

- name: ALWAYS_CHANGES edit walled-garden settings, check changes
  mt_hotspot:
    hostname: "{{ mt_hostname }}"
    username: "{{ mt_user }}"
    password: "{{ mt_pass }}"
    state:    present
    parameter: walled-garden
    settings:
      comment: "Allow Personal Web Portal"
      dst-host: google.com
      server: NETACCESS1
      method: TRACE
  register: walled_garden_edit
  failed_when: not ( walled_garden_edit | changed )

- name: ALWAYS_CHANGES remove walled-garden
  mt_hotspot:
    hostname: "{{ mt_hostname }}"
    username: "{{ mt_user }}"
    password: "{{ mt_pass }}"
    state:    absent
    parameter: walled-garden
    settings:
      comment: "Allow Personal Web Portal"
  register: walled_garden_rem
  failed_when: (
      not ansible_check_mode
    ) and (
      not ( walled_garden_rem | changed )
    )

- name: ALWAYS_CHANGES remove a hotspot
  mt_hotspot:
    hostname: "{{ mt_hostname }}"
    username: "{{ mt_user }}"
    password: "{{ mt_pass }}"
    parameter: hotspot
    state:    absent
    settings:
      name: NETACCESS1
  register: hotspot_rem
  failed_when: (
      not ansible_check_mode
    ) and (
      not ( hotspot_rem | changed )
    )

- name: ALWAYS_CHANGES remove a hotspot profile
  mt_hotspot:
    hostname: "{{ mt_hostname }}"
    username: "{{ mt_user }}"
    password: "{{ mt_pass }}"
    parameter: profile
    state:    absent
    settings:
      name: Hotspot1
  register: profile_rem
  failed_when: (
      not ansible_check_mode
    ) and (
      not ( profile_rem | changed )
    )


File: /tests\integration\tasks\radius-tests.yml
- name: Test adding a radius item
  mt_radius:
    hostname:   "{{ mt_hostname }}"
    username:   "{{ mt_user }}"
    password:   "{{ mt_pass }}"
    state:      "present"
    parameter:  radius
    settings:
      address:     "192.168.12.2"
      comment:    'Ansible - radius test 1'
      secret:     'password'
      service:
        - login
        - hotspot
        - wireless
      timeout:        '2s500ms'

- name: ALWAYS_CHANGES Test editing an existing radius item (edit service item)
  mt_radius:
    hostname:   "{{ mt_hostname }}"
    username:   "{{ mt_user }}"
    password:   "{{ mt_pass }}"
    state:      "present"
    parameter:  radius
    settings:
      address:     "192.168.12.2"
      comment:    'Ansible - radius test 1'
      secret:     'password'
      service:
        - login
        - hotspot
        - wireless
        - dhcp
      timeout:        '2s500ms'
  register: radius_test_1_edit
  failed_when: (
      not ansible_check_mode
    ) and (
      not ( radius_test_1_edit | changed )
    )

- name: ALWAYS_CHANGES Test editing an existing radius item (change service list)
  mt_radius:
    hostname:   "{{ mt_hostname }}"
    username:   "{{ mt_user }}"
    password:   "{{ mt_pass }}"
    state:      "present"
    parameter:  radius
    settings:
      address:     "192.168.12.2"
      comment:    'Ansible - radius test 1'
      secret:     'password'
      service:
        - login
        - hotspot
        - wireless
      timeout:        '2s500ms'
  register: radius_test_1_edit
  failed_when: (
      not ansible_check_mode
    ) and (
      not ( radius_test_1_edit | changed )
    )

- name: Test adding a duplicate of the first radius item
  mt_radius:
    hostname:   "{{ mt_hostname }}"
    username:   "{{ mt_user }}"
    password:   "{{ mt_pass }}"
    state:      "present"
    parameter:  radius
    settings:
      address:     "192.168.12.2"
      comment:    'Ansible - radius test 1'
      secret:     'password'
      service:
        - login
        - hotspot
        - wireless
      timeout:        '2s500ms'
  register: radius_test_1_duplicate
  failed_when: (
      not ansible_check_mode
    ) and (
      ( radius_test_1_duplicate|changed )
    )

- name: ALWAYS_CHANGES Test adding another radius item to later remove
  mt_radius:
    hostname:   "{{ mt_hostname }}"
    username:   "{{ mt_user }}"
    password:   "{{ mt_pass }}"
    state:      "present"
    parameter:  radius
    settings:
      address:     "192.168.12.2"
      comment:    'Ansible - radius test 2'
      secret:     'password'
      service:
        - login
        - hotspot
        - wireless
      timeout:        '2s500ms'
  register: radius_test_2
  failed_when: (
      not ansible_check_mode
    ) and (
      not ( radius_test_2 | changed )
    )

- name: ALWAYS_CHANGES Test removing a radius item
  mt_radius:
    hostname:   "{{ mt_hostname }}"
    username:   "{{ mt_user }}"
    password:   "{{ mt_pass }}"
    state:      "absent"
    parameter:  radius
    settings:
      comment:    'Ansible - radius test 2'
  register: radius_test_2_rem
  failed_when: (
      not ansible_check_mode
    ) and (
      not ( radius_test_2_rem | changed )
    )

- name: Change incoming settings
  mt_radius:
    hostname:   "{{ mt_hostname }}"
    username:   "{{ mt_user }}"
    password:   "{{ mt_pass }}"
    parameter:  incoming
    settings:
      accept: "true"
      port: "37988"

- name: ALWAYS_CHANGES Change incoming settings
  mt_radius:
    hostname:   "{{ mt_hostname }}"
    username:   "{{ mt_user }}"
    password:   "{{ mt_pass }}"
    parameter:  incoming
    settings:
      accept: "true"
      port: "37955"
  register: change_incoming
  failed_when: (
      not ansible_check_mode
    ) and (
      not ( change_incoming | changed )
    )

- name: NEVER_CHANGES check idempotency of incoming settings
  mt_radius:
    hostname:   "{{ mt_hostname }}"
    username:   "{{ mt_user }}"
    password:   "{{ mt_pass }}"
    parameter:  incoming
    settings:
      accept: "true"
      port: "37955"
  register: idem_incoming
  failed_when: (
      not ansible_check_mode
    ) and (
      ( idem_incoming | changed )
    )


File: /tests\integration\tasks\test-address-list.yml
---
- name: Test adding a firewall address-list
  mt_ip:
    hostname:   "{{ mt_hostname }}"
    username:   "{{ mt_user }}"
    password:   "{{ mt_pass }}"
    state:      "present"
    parameter: 'firewall/address-list'
    settings: "{{ item }}"
  with_items:
    - address: 192.168.1.2
      comment: dns1
      list:    test_list
    - address: 192.168.1.3
      comment: dns2
      list:    test_list
    - address: 192.168.1.6
      comment: test_comment3
      list:    test_list

- name: ALWAYS_CHANGES Test editing a firewall address-list
  mt_ip:
    hostname:   "{{ mt_hostname }}"
    username:   "{{ mt_user }}"
    password:   "{{ mt_pass }}"
    state:      "present"
    parameter: 'firewall/address-list'
    settings:
        address: 192.168.1.2
        comment: dns1
        list: test_list2
  register: address_list_edit_1
  failed_when: (
      not ansible_check_mode
    ) and (
      not ( address_list_edit_1 | changed )
    )

- name: NEVER_CHANGES Test adding a duplicate address-list
  mt_ip:
    hostname:   "{{ mt_hostname }}"
    username:   "{{ mt_user }}"
    password:   "{{ mt_pass }}"
    state:      "present"
    parameter: 'firewall/address-list'
    settings:
        address: 192.168.1.3
        comment: dns2
        list: test_list
  register: add_address_list_add_dup_1
  failed_when: (
      not ansible_check_mode
    ) and (
      ( add_address_list_add_dup_1 | changed )
    )

- name: ALWAYS_CHANGES Test removing a firewall address-list
  mt_ip:
    hostname:   "{{ mt_hostname }}"
    username:   "{{ mt_user }}"
    password:   "{{ mt_pass }}"
    state:      "absent"
    parameter: 'firewall/address-list'
    settings:
        address: 192.168.1.2
        comment: dns1
        list: test_list
  register: address_list_rem_1
  failed_when: (
      not ansible_check_mode
    ) and (
      not ( address_list_rem_1 | changed )
    )


File: /tests\integration\tasks\test-bridge.yml
---
- name: add eoip interface
  mt_command:
    hostname: "{{ mt_hostname }}"
    username: "{{ mt_user }}"
    password: "{{ mt_pass }}"
    command: /interface/eoip/add
    command_arguments:
      name: eoip-interface1
  ignore_errors: yes

- name: Add bridge1
  mt_interfaces:
    hostname: "{{ mt_hostname }}"
    username: "{{ mt_user }}"
    password: "{{ mt_pass }}"
    state:    present
    parameter: bridge
    settings:
      name:     "{{ item }}"
      arp:      proxy-arp
  with_items:
    - "bridge1"

- name: Add bridge1 again (idempotency test)
  mt_interfaces:
    hostname: "{{ mt_hostname }}"
    username: "{{ mt_user }}"
    password: "{{ mt_pass }}"
    state:    present
    parameter: bridge
    settings:
      name:     "{{ item }}"
      arp:      proxy-arp
  with_items:
    - "bridge1"
  register: mod_bridge1
  failed_when: (
      not ansible_check_mode
    ) and (
      ( mod_bridge1 | changed )
    )

# bridge ports depend on bridge being created first

- name: Add interface to bridge1 (port)
  mt_interfaces:
    hostname:   "{{ mt_hostname }}"
    username:   "{{ mt_user }}"
    password:   "{{ mt_pass }}"
    parameter:  "bridge port"
    state:      present
    settings:
      bridge:     "{{ item[0] }}"
      interface:  "{{ item[1] }}"
  with_nested:
    - [ "bridge1" ]
    - [ "ether2" ]

- name: Add interface to bridge1 (port) again (idempotency test)
  mt_interfaces:
    hostname:   "{{ mt_hostname }}"
    username:   "{{ mt_user }}"
    password:   "{{ mt_pass }}"
    parameter:  "bridge port"
    state:      present
    settings:
      bridge:     "{{ item[0] }}"
      interface:  "{{ item[1] }}"
  with_nested:
    - [ "bridge1" ]
    - [ "ether2" ]
  register: mod_bridge1_port
  failed_when: (
      not ansible_check_mode
    ) and (
      ( mod_bridge1_port | changed )
    )

- name: Add additional param to bridge port
  mt_interfaces:
    hostname:   "{{ mt_hostname }}"
    username:   "{{ mt_user }}"
    password:   "{{ mt_pass }}"
    parameter:  "bridge port"
    state:      present
    settings:
      bridge:     "{{ item[0] }}"
      interface:  "{{ item[1] }}"
      edge:       "{{ item[2] }}"
  with_nested:
    - [ "bridge1" ]
    - [ "ether2" ]
    - [ "yes-discover" ]

- name: ALWAYS_CHANGES Add 2nd interface to bridge1 port
  mt_interfaces:
    hostname: "{{ mt_hostname }}"
    username: "{{ mt_user }}"
    password: "{{ mt_pass }}"
    parameter:  "bridge port"
    state:      present
    settings:
      bridge:    bridge1
      interface: eoip-tunnel1
  register: bridge1_add_2nd_inter
  failed_when: (
      not ansible_check_mode
    ) and (
      not ( bridge1_add_2nd_inter | changed )
    )

- name: ALWAYS_CHANGES Remove 2nd interface to bridge1 port
  mt_interfaces:
    hostname: "{{ mt_hostname }}"
    username: "{{ mt_user }}"
    password: "{{ mt_pass }}"
    parameter:  "bridge port"
    state:      absent
    settings:
      bridge:     bridge1
      interface:  "eoip-tunnel1"
  register: bridge1_rem_2nd_inter
  failed_when: (
      not ansible_check_mode
    ) and (
      not ( bridge1_rem_2nd_inter | changed )
    )

- name: Add bridge2
  mt_interfaces:
    hostname: "{{ mt_hostname }}"
    username: "{{ mt_user }}"
    password: "{{ mt_pass }}"
    parameter:  "bridge"
    state:      present
    settings:
      name:     "bridge2"
      arp:      "reply-only"

- name: Adjust settings
  mt_interfaces:
    hostname: "{{ mt_hostname }}"
    username: "{{ mt_user }}"
    password: "{{ mt_pass }}"
    parameter:  "bridge settings"
    settings:
      allow-fast-path: "yes"
      use-ip-firewall: "yes"
      use-ip-firewall-for-vlan: "yes"
      use-ip-firewall-for-pppoe: "no"

- name: Adjust settings (test changes)
  mt_interfaces:
    hostname: "{{ mt_hostname }}"
    username: "{{ mt_user }}"
    password: "{{ mt_pass }}"
    parameter:  "bridge settings"
    settings:
      allow-fast-path: "yes"
      use-ip-firewall-for-vlan: "no"
      use-ip-firewall-for-pppoe: "no"
  register: bridge_settings_1
  failed_when: (
      not ansible_check_mode
    ) and (
      not ( bridge_settings_1 | changed )
    )

- name: Adjust settings again (idempotency test)
  mt_interfaces:
    hostname: "{{ mt_hostname }}"
    username: "{{ mt_user }}"
    password: "{{ mt_pass }}"
    parameter:  "bridge settings"
    settings:
      allow-fast-path: "yes"
      use-ip-firewall-for-vlan: "no"
      use-ip-firewall-for-pppoe: "no"
  register: bridge_settings_2
  failed_when: (
      not ansible_check_mode
    ) and (
      ( bridge_settings_2 | changed )
    )


File: /tests\integration\tasks\test-command.yml
---
- name: add scheduler
  mt_system_scheduler:
    hostname: "{{ mt_hostname }}"
    username: "{{ mt_user }}"
    password: "{{ mt_pass }}"
    state:    present
    name:     ansible_test
    on_event: 'put "test"'
    interval: 1s

- name: run command to disable system scheduler task
  mt_command:
    hostname: "{{ mt_hostname }}"
    username: "{{ mt_user }}"
    password: "{{ mt_pass }}"
    command:   /system/scheduler/disable
    command_arguments:
      numbers: ansible_test

- name: run command
  mt_command:
    hostname: "{{ mt_hostname }}"
    username: "{{ mt_user }}"
    password: "{{ mt_pass }}"
    command:  "/interface/print"
  tags: print


File: /tests\integration\tasks\test-dhcp-server.yml
---
- name: Test adding ip pool to be used by dhcp_server
  mt_ip:
    hostname: "{{ mt_hostname }}"
    username: "{{ mt_user }}"
    password: "{{ mt_pass }}"
    state:    present
    parameter: pool
    settings:
      name:     pool1
      ranges:   102.3.4.5

- name: Test adding a dhcp_server
  mt_dhcp_server:
    hostname:   "{{ mt_hostname }}"
    username:   "{{ mt_user }}"
    password:   "{{ mt_pass }}"
    state:         "present"
    parameter: dhcp-server
    settings:
      name:          ansible_test
      address-pool:  'pool1'
      interface:     ether2
      always-broadcast:    "yes"
      authoritative: after-2sec-delay

- name: ALWAYS_CHANGES Test editing an existing dhcp server (change authoritative)
  mt_dhcp_server:
    hostname:   "{{ mt_hostname }}"
    username:   "{{ mt_user }}"
    password:   "{{ mt_pass }}"
    state:      "present"
    parameter:  dhcp-server
    settings:
      name:          ansible_test
      address-pool:  'pool1'
      interface:     ether1
      always-broadcast:    "yes"
      authoritative: after-10sec-delay
  register: dhcp_server_test_1_edit
  failed_when: (
      not ansible_check_mode
    ) and (
      not ( dhcp_server_test_1_edit | changed )
    )

- name: NEVER_CHANGES Test adding a duplicate of the first dhcp server
  mt_dhcp_server:
    hostname:  "{{ mt_hostname }}"
    username:  "{{ mt_user }}"
    password:  "{{ mt_pass }}"
    state:     "present"
    parameter: dhcp-server
    settings:
      name:         ansible_test
      address-pool: 'pool1'
      interface:    ether1
      always-broadcast:   "yes"
  register: dhcp_server_test_1_duplicate
  failed_when: (
      not ansible_check_mode
    ) and (
      ( dhcp_server_test_1_duplicate|changed )
    )

- name: ALWAYS_CHANGES Test adding another dhcp server to later remove
  mt_dhcp_server:
    hostname:   "{{ mt_hostname }}"
    username:   "{{ mt_user }}"
    password:   "{{ mt_pass }}"
    state:      "present"
    parameter: dhcp-server
    settings:
      interface:  "ether2"
      name:       "ansible_test_2"
  register: dhcp_server_test_2
  failed_when: (
      not ansible_check_mode
    ) and (
      not ( dhcp_server_test_2 | changed )
    )

- name: ALWAYS_CHANGES Test removing a dhcp server
  mt_dhcp_server:
    hostname:  "{{ mt_hostname }}"
    username:  "{{ mt_user }}"
    password:  "{{ mt_pass }}"
    state:     "absent"
    parameter: dhcp-server
    settings:
      name:       "ansible_test_2"
  register: dhcp_server_test_2_rem
  failed_when: (
      not ansible_check_mode
    ) and (
      not ( dhcp_server_test_2_rem | changed )
    )

- name: add a dhcp-server network
  mt_dhcp_server:
    hostname:   "{{ mt_hostname }}"
    username:   "{{ mt_user }}"
    password:   "{{ mt_pass }}"
    state:      "present"
    parameter:  network
    settings:
      address: '192.168.10.0/24'

- name: add a second dhcp-server network
  mt_dhcp_server:
    hostname:   "{{ mt_hostname }}"
    username:   "{{ mt_user }}"
    password:   "{{ mt_pass }}"
    state:      "present"
    parameter:  network
    settings:
      address: 10.147.172.0/24
      comment: "Phones network"
      dns-server: 10.147.172.2
      gateway: 10.147.172.1

- name: ALWAYS_CHANGES modify a second dhcp-server network
  mt_dhcp_server:
    hostname:   "{{ mt_hostname }}"
    username:   "{{ mt_user }}"
    password:   "{{ mt_pass }}"
    state:      "present"
    parameter:  network
    settings:
      address: 10.147.172.0/24
      comment: "Phones network"
      dns-server: 10.147.172.20
      gateway: 10.147.172.1
  register: dhcp_network_mod
  failed_when: (
      not ansible_check_mode
    ) and (
      not ( dhcp_network_mod | changed )
    )

- name: ALWAYS_CHANGES remove first dhcp-server network
  mt_dhcp_server:
    hostname:   "{{ mt_hostname }}"
    username:   "{{ mt_user }}"
    password:   "{{ mt_pass }}"
    state:      "absent"
    parameter:  network
    settings:
      address: '192.168.10.0/24'
  register: dhcp_network_rem
  failed_when: (
      not ansible_check_mode
    ) and (
      not ( dhcp_network_rem | changed )
    )

- name: Test adding an item to dhcp-server options
  mt_dhcp_server:
    hostname:   "{{ mt_hostname }}"
    username:   "{{ mt_user }}"
    password:   "{{ mt_pass }}"
    state:      "present"
    parameter:  option
    settings:
      name: ansible_test
      code: "251"


File: /tests\integration\tasks\test-facts.yml
---
- name: Get mikrotik system facts
  mt_facts:
    hostname: "{{ mt_hostname }}"
    username: "{{ mt_user }}"
    password: "{{ mt_pass }}"
    filter: "{{ item }}"
  with_items:
    - interface_ethernet
    - system_ntp_client
    - system_routerboard
    - ip_route
    - ip_dns
    - ip_address


File: /tests\integration\tasks\test-firewall-filter.yml
---
- name: Test adding firewall filter rules
  mt_ip_firewall:
    hostname:   "{{ mt_hostname }}"
    username:   "{{ mt_user }}"
    password:   "{{ mt_pass }}"
    state:      "present"
    parameter: filter
    rule: "{{ item }}"
  with_items:
    - action: accept
      chain: forward
      comment: 'Ansible - fw filter rule1'
      place-before: '0'
    - action: accept
      chain: input
      comment: 'Ansible - fw filter rule2'
      place-before: '1'
    - action: passthrough
      chain: input
      comment: 'Ansible - fw filter rule3'
      place-before: '2'
    - action: reject
      chain: forward
      comment: 'Ansible - fw filter rule4'
      place-before: '3'
      src-address: 192.168.0.0/16
    - action: accept
      chain: forward
      comment: 'Ansible - fw filter rule5'
      place-before: '4'

- name: add some manual rules to simulate chaos, command module
  mt_command:
    hostname: "{{ mt_hostname }}"
    username: "{{ mt_user }}"
    password: "{{ mt_pass }}"
    command:  /ip/firewall/filter/add
    command_arguments: "{{ item }}"
  with_items:
    - action: accept
      chain: output
      comment: 'manual test rules'
      place-before: '3'
    - action: accept
      chain: output
      comment: 'manual test rules'
      place-before: '1'
    - action: accept
      chain: output
      comment: 'manual test rules'
      place-before: '0'

- name: Fix firewall state
  mt_ip_firewall:
    hostname:   "{{ mt_hostname }}"
    username:   "{{ mt_user }}"
    password:   "{{ mt_pass }}"
    state:      "present"
    parameter: filter
    rule: "{{ item }}"
  with_items:
    - action: accept
      chain: forward
      comment: 'Ansible - fw filter rule1'
      place-before: '0'
    - action: accept
      chain: input
      comment: 'Ansible - fw filter rule2'
      place-before: '1'
    - action: passthrough
      chain: input
      comment: 'Ansible - fw filter rule3'
      place-before: '2'
    - action: reject
      chain: forward
      comment: 'Ansible - fw filter rule4'
      place-before: '3'
      src-address: 192.168.0.0/16
    - action: accept
      chain: forward
      comment: 'Ansible - fw filter rule5'
      place-before: '4'

- name: NEVER_CHANGES, check idempotency
  mt_ip_firewall:
    hostname:   "{{ mt_hostname }}"
    username:   "{{ mt_user }}"
    password:   "{{ mt_pass }}"
    state:      "present"
    parameter: filter
    rule: "{{ item }}"
  with_items:
    - action: accept
      chain: forward
      comment: 'Ansible - fw filter rule1'
      place-before: '0'
    - action: accept
      chain: input
      comment: 'Ansible - fw filter rule2'
      place-before: '1'
    - action: passthrough
      chain: input
      comment: 'Ansible - fw filter rule3'
      place-before: '2'
    - action: reject
      chain: forward
      comment: 'Ansible - fw filter rule4'
      place-before: '3'
      src-address: 192.168.0.0/16
    - action: accept
      chain: forward
      comment: 'Ansible - fw filter rule5'
      place-before: '4'
  register: check_idem
  failed_when: (
      not ansible_check_mode
    ) and (
      ( check_idem | changed )
    )
  tags: test-firewall

- name: ALWAYS_CHANGES Test editing existing rule
  mt_ip_firewall:
    hostname:   "{{ mt_hostname }}"
    username:   "{{ mt_user }}"
    password:   "{{ mt_pass }}"
    state:      "present"
    parameter: filter
    rule: "{{ item }}"
  with_items:
    - action: accept
      chain: forward
      comment: 'Ansible - fw filter rule4'
      src-address: 192.168.0.0/16
      place-before: '3'
  register: edit_filter_rule
  failed_when: (
      not ansible_check_mode
    ) and (
      not ( edit_filter_rule | changed )
    )

- name: NEVER_CHANGES Test editing existing rule check idempotency again
  mt_ip_firewall:
    hostname:   "{{ mt_hostname }}"
    username:   "{{ mt_user }}"
    password:   "{{ mt_pass }}"
    state:      "present"
    parameter: filter
    rule: "{{ item }}"
  with_items:
    - action: accept
      chain: forward
      comment: 'Ansible - fw filter rule4'
      src-address: 192.168.0.0/16
      place-before: '3'
  register: edit_filter_rule_2
  failed_when: (
      not ansible_check_mode
    ) and (
      ( edit_filter_rule_2 | changed )
    )
  tags: test-firewall

- name: add a rule to the bottom of the chain
  mt_ip_firewall:
    hostname:   "{{ mt_hostname }}"
    username:   "{{ mt_user }}"
    password:   "{{ mt_pass }}"
    state:      "present"
    parameter: filter
    rule: "{{ item }}"
  with_items:
    - action: accept
      chain: forward
      comment: 'Ansible - fw filter rule20'
      src-address: 192.150.0.0/16
      place-before: '20'

- name: ALWAYS_CHANGES, ensure that rule at the bottom changes
  mt_ip_firewall:
    hostname:   "{{ mt_hostname }}"
    username:   "{{ mt_user }}"
    password:   "{{ mt_pass }}"
    state:      "present"
    parameter: filter
    rule: "{{ item }}"
  with_items:
    - action: reject
      chain: forward
      comment: 'Ansible - fw filter rule20'
      src-address: 192.150.0.0/16
      place-before: '20'
  register: edit_filter_rule_3
  failed_when: (
      not ansible_check_mode
    ) and (
      not ( edit_filter_rule_3 | changed )
    )

- name: NEVER_CHANGES add a rule to the bottom of the chain, check_idempotency
  mt_ip_firewall:
    hostname:   "{{ mt_hostname }}"
    username:   "{{ mt_user }}"
    password:   "{{ mt_pass }}"
    state:      "present"
    parameter: filter
    rule: "{{ item }}"
  with_items:
    - action: reject
      chain: forward
      comment: 'Ansible - fw filter rule20'
      src-address: 192.150.0.0/16
      place-before: '20'
  register: edit_filter_rule_4
  failed_when: (
      not ansible_check_mode
    ) and (
      ( edit_filter_rule_4 | changed )
    )

- name: ALWAYS_CHANGES Test removing existing rule
  mt_ip_firewall:
    hostname:   "{{ mt_hostname }}"
    username:   "{{ mt_user }}"
    password:   "{{ mt_pass }}"
    state:      "absent"
    parameter: filter
    rule: "{{ item }}"
  with_items:
    - place-before: '4'
  register: rem_filter_rule
  failed_when: (
      not ansible_check_mode
    ) and (
      not ( rem_filter_rule | changed )
    )


File: /tests\integration\tasks\test-firewall-nat.yml
---
- name: Test adding firewall nat rules
  mt_ip_firewall:
    hostname:   "{{ mt_hostname }}"
    username:   "{{ mt_user }}"
    password:   "{{ mt_pass }}"
    state:      "present"
    parameter: nat
    rule: "{{ item }}"
  with_items:
    - action: accept
      chain: srcnat
      comment: 'Ansible - fw filter rule1'
      place-before: '0'
    - action: accept
      chain: dstnat
      comment: 'Ansible - fw filter rule2'
      place-before: '1'
    - action: passthrough
      chain: srcnat
      comment: 'Ansible - fw filter rule3'
      place-before: '2'
    - action: return
      chain: dstnat
      comment: 'Ansible - fw filter rule4'
      place-before: '3'
      src-address: 192.168.0.0/16
    - action: redirect
      chain: dstnat
      comment: 'Ansible - fw filter rule5'
      place-before: '4'
    - action: redirect
      chain: dstnat
      comment: 'Ansible - fw filter rule20'
      place-before: '19'

- name: add some manual rules to simulate chaos, command module
  mt_command:
    hostname: "{{ mt_hostname }}"
    username: "{{ mt_user }}"
    password: "{{ mt_pass }}"
    command:  /ip/firewall/nat/add
    command_arguments: "{{ item }}"
  with_items:
    - action: passthrough
      chain: srcnat
      comment: 'manual test rules'
      place-before: '3'
    - action: passthrough
      chain: srcnat
      comment: 'manual test rules'
      place-before: '1'
    - action: passthrough
      chain: srcnat
      comment: 'manual test rules'
      place-before: '0'

- name: fix nat state
  mt_ip_firewall:
    hostname:   "{{ mt_hostname }}"
    username:   "{{ mt_user }}"
    password:   "{{ mt_pass }}"
    state:      "present"
    parameter: nat
    rule: "{{ item }}"
  with_items:
    - action: accept
      chain: srcnat
      comment: 'Ansible - fw filter rule1'
      place-before: '0'
    - action: accept
      chain: dstnat
      comment: 'Ansible - fw filter rule2'
      place-before: '1'
    - action: passthrough
      chain: srcnat
      comment: 'Ansible - fw filter rule3'
      place-before: '2'
    - action: return
      chain: dstnat
      comment: 'Ansible - fw filter rule4'
      place-before: '3'
      src-address: 192.168.0.0/16
    - action: redirect
      chain: dstnat
      comment: 'Ansible - fw filter rule5'
      place-before: '4'
    - action: redirect
      chain: dstnat
      comment: 'Ansible - fw filter rule20'
      place-before: '19'

- name: NEVER_CHANGES check_idempotency
  mt_ip_firewall:
    hostname:   "{{ mt_hostname }}"
    username:   "{{ mt_user }}"
    password:   "{{ mt_pass }}"
    state:      "present"
    parameter: nat
    rule: "{{ item }}"
  with_items:
    - action: accept
      chain: srcnat
      comment: 'Ansible - fw filter rule1'
      place-before: '0'
    - action: accept
      chain: dstnat
      comment: 'Ansible - fw filter rule2'
      place-before: '1'
    - action: passthrough
      chain: srcnat
      comment: 'Ansible - fw filter rule3'
      place-before: '2'
    - action: return
      chain: dstnat
      comment: 'Ansible - fw filter rule4'
      place-before: '3'
      src-address: 192.168.0.0/16
    - action: redirect
      chain: dstnat
      comment: 'Ansible - fw filter rule5'
      place-before: '4'
    - action: redirect
      chain: dstnat
      comment: 'Ansible - fw filter rule20'
      place-before: '19'
  register: nat_idem
  failed_when: (
      not ansible_check_mode
    ) and (
      ( nat_idem | changed )
    )

- name: ALWAYS_CHANGES, change rule
  mt_ip_firewall:
    hostname:   "{{ mt_hostname }}"
    username:   "{{ mt_user }}"
    password:   "{{ mt_pass }}"
    state:      "present"
    parameter: nat
    rule: "{{ item }}"
  with_items:
    - action: return
      chain: dstnat
      comment: 'Ansible - fw filter rule4'
      place-before: '3'
      src-address: 192.165.0.0/16
  register: nat_change
  failed_when: (
      not ansible_check_mode
    ) and (
      not ( nat_change | changed )
    )

- name: ALWAYS_CHANGES, remove rule
  mt_ip_firewall:
    hostname:   "{{ mt_hostname }}"
    username:   "{{ mt_user }}"
    password:   "{{ mt_pass }}"
    state:      "absent"
    parameter: nat
    rule: "{{ item }}"
  with_items:
    - place-before: '4'
  register: nat_rem
  failed_when: (
      not ansible_check_mode
    ) and (
      not ( nat_rem | changed )
    )


File: /tests\integration\tasks\test-interface-ethernet.yml
---
- name: Add comment to ether1
  mt_interfaces:
    hostname: "{{ mt_hostname }}"
    username: "{{ mt_user }}"
    password: "{{ mt_pass }}"
    settings: "{{ item.settings }}"
    parameter: "ethernet"
  with_items:
    - settings:
        name:     ether1
        comment:  Ansible controlled ether1

- name: Add comment to ether1 again (idempotency test)
  mt_interfaces:
    hostname: "{{ mt_hostname }}"
    username: "{{ mt_user }}"
    password: "{{ mt_pass }}"
    settings: "{{ item.settings }}"
    parameter: "ethernet"
  with_items:
    - settings:
        name:     ether1
        comment:  Ansible controlled ether1
  register: ether1_comment
  failed_when: (
      not ansible_check_mode
    ) and (
      ( ether1_comment | changed )
    )

- name: USUALLY_CHANGES Modify mtu of ether2
  mt_interfaces:
    hostname: "{{ mt_hostname }}"
    username: "{{ mt_user }}"
    password: "{{ mt_pass }}"
    settings: "{{ item.settings }}"
    parameter: "ethernet"
  with_items:
    - settings:
        name:     ether2
        mtu:      1500

- name: ALWAYS_CHANGES Modify mtu of ether2
  mt_interfaces:
    hostname: "{{ mt_hostname }}"
    username: "{{ mt_user }}"
    password: "{{ mt_pass }}"
    settings: "{{ item.settings }}"
    parameter: "ethernet"
  with_items:
    - settings:
        name:     ether2
        mtu:      1501
  register: ether2_mtu
  failed_when: (
      not ansible_check_mode
    ) and (
      not ( ether2_mtu | changed )
    )


File: /tests\integration\tasks\test-interface-vlan.yml
---
- name: Test adding vlan
  mt_interfaces:
    hostname:  "{{ mt_hostname }}"
    username:  "{{ mt_user }}"
    password:  "{{ mt_pass }}"
    state:     present
    parameter: vlan
    settings:
      name:     vlan_test1
      vlan_id:  30
      interface: ether1
      comment:   Testing vlan1

- name: NEVER_CHANGES Test adding duplicate vlan interface
  mt_interfaces:
    hostname: "{{ mt_hostname }}"
    username: "{{ mt_user }}"
    password: "{{ mt_pass }}"
    state:       present
    parameter: vlan
    settings:
      name:     vlan_test1
      vlan_id:  30
      interface: ether1
  register: vlan_test_1_add
  failed_when: (
      not ansible_check_mode
    ) and (
      ( vlan_test_1_add | changed )
    )

- name: ALWAYS_CHANGES Test adding second vlan to be removed later
  mt_interfaces:
    hostname: "{{ mt_hostname }}"
    username: "{{ mt_user }}"
    password: "{{ mt_pass }}"
    state:       present
    parameter: vlan
    settings:
      name:     vlan_test2
      vlan_id:  32
      interface: ether2
  register: vlan_test_2_add
  failed_when: (
      not ansible_check_mode
    ) and (
      not ( vlan_test_2_add | changed )
    )

- name: ALWAYS_CHANGES Test editing an existing vlan (change vlan_id)
  mt_interfaces:
    hostname: "{{ mt_hostname }}"
    username: "{{ mt_user }}"
    password: "{{ mt_pass }}"
    state:       present
    parameter: vlan
    settings:
      name:     vlan_test1
      vlan_id:  36
      interface: ether1
      comment:    "testing ansible stuff"
  register: vlan_test_1_edit
  failed_when: (
      not ansible_check_mode
    ) and (
      not ( vlan_test_1_edit | changed )
    )

- name: ALWAYS_CHANGES Test remove vlan
  mt_interfaces:
    hostname: "{{ mt_hostname }}"
    username: "{{ mt_user }}"
    password: "{{ mt_pass }}"
    state:    absent
    parameter: vlan
    settings:
      name:     vlan_test2
  register: vlan_test_2_rem
  failed_when: (
      not ansible_check_mode
      ) and (
       not (
       vlan_test_2_rem | changed )
      )


File: /tests\integration\tasks\test-interface-wireless.yml
---
- name: edit default security-profiles item
  mt_interface_wireless:
    hostname: "{{ mt_hostname }}"
    username: "{{ mt_user }}"
    password: "{{ mt_pass }}"
    parameter: security-profiles
    state:     present
    settings:
      name: test1
      supplicant-identity: test

- name: add security-profiles item
  mt_interface_wireless:
    hostname: "{{ mt_hostname }}"
    username: "{{ mt_user }}"
    password: "{{ mt_pass }}"
    parameter: security-profiles
    state:     present
    settings:
      name: test1
      supplicant-identity: test
      management-protection: required

- name: NEVER_CHANGES add security-profiles item, check idempotency
  mt_interface_wireless:
    hostname: "{{ mt_hostname }}"
    username: "{{ mt_user }}"
    password: "{{ mt_pass }}"
    parameter: security-profiles
    state:     present
    settings:
      name: test1
      supplicant-identity: test
  register: security_prof_idem
  failed_when: (
      not ansible_check_mode
    ) and (
      ( security_prof_idem | changed )
    )

- name: ALWAYS_CHANGES add security-profiles item, check idempotency
  mt_interface_wireless:
    hostname: "{{ mt_hostname }}"
    username: "{{ mt_user }}"
    password: "{{ mt_pass }}"
    parameter: security-profiles
    state:     present
    settings:
      name: test1
      supplicant-identity: test
      management-protection: allowed
  register: security_prof_edit
  failed_when: (
      not ansible_check_mode
    ) and (
      not ( security_prof_edit | changed )
    )

- name: ALWAYS_CHANGES rem security-profiles item
  mt_interface_wireless:
    hostname: "{{ mt_hostname }}"
    username: "{{ mt_user }}"
    password: "{{ mt_pass }}"
    parameter: security-profiles
    state:     absent
    settings:
      name: test1
  register: security_prof_rem
  failed_when: (
      not ansible_check_mode
    ) and (
      not ( security_prof_rem | changed )
    )


File: /tests\integration\tasks\test-ip-address.yml
---

- name: generate bridge interfaces for testing ip addresses
  mt_interfaces:
    hostname: "{{ mt_hostname }}"
    username: "{{ mt_user }}"
    password: "{{ mt_pass }}"
    state:    present
    parameter: bridge
    settings:
      name:     "{{ item }}"
      arp:      proxy-arp
  with_items:
    - "bridge1"
    - "bridge2"
    - "bridge3"
    - "bridge4"

- name: Remove any ip from bridge interfaces
  mt_ip_address:
    hostname: "{{ mt_hostname }}"
    username: "{{ mt_user }}"
    password: "{{ mt_pass }}"
    state:    absent
    idempotent: interface
    settings:
      interface:     "{{ item }}"
  with_items:
    - "bridge1"
    - "bridge2"
    - "bridge3"
    - "bridge4"

- name: ALWAYS_CHANGES Test adding an ip addr bridge2
  mt_ip_address:
    hostname:   "{{ mt_hostname }}"
    username:   "{{ mt_user }}"
    password:   "{{ mt_pass }}"
    state:      "present"
    settings:
      interface:  "bridge2"
      address:    "192.168.88.2/24"
      network:    "192.168.88.0"
  register: ip_addr_add_2
  failed_when: not ( ip_addr_add_2 | changed )

- name: NEVER_CHANGES Test adding the same ip addr again to bridge2
  mt_ip_address:
    hostname:   "{{ mt_hostname }}"
    username:   "{{ mt_user }}"
    password:   "{{ mt_pass }}"
    state:      "present"
    settings:
      interface:  "bridge2"
      address:    "192.168.88.2/24"
      network:    "192.168.88.0"
  register: ip_addr_add_2
  failed_when: ip_addr_add_2 | changed

- name: Test adding an ip addr with comment bridge3
  mt_ip_address:
    hostname:   "{{ mt_hostname }}"
    username:   "{{ mt_user }}"
    password:   "{{ mt_pass }}"
    state:      "present"
    settings:
      interface:  "bridge3"
      address:    "192.168.88.3/24"
      comment:    "bridge #3!!!"

- name: Test adding an ip addr with comment and network bridge4
  mt_ip_address:
    hostname:   "{{ mt_hostname }}"
    username:   "{{ mt_user }}"
    password:   "{{ mt_pass }}"
    state:      "present"
    settings:
      interface:  "bridge4"
      address:    "192.168.88.4/24"
      network:    "192.168.88.0"
      comment:    "bridge4 first addition"

- name: Test adding a second ip addr with comment and network bridge4
  mt_ip_address:
    hostname:   "{{ mt_hostname }}"
    username:   "{{ mt_user }}"
    password:   "{{ mt_pass }}"
    state:      "present"
    settings:
      interface:  "bridge4"
      address:    "192.168.88.5/24"
      network:    "192.168.88.0"
      comment:    "bridge #4 second addition"

- name: ALWAYS_CHANGES Test removing ip addr bridge2
  mt_ip_address:
    hostname:   "{{ mt_hostname }}"
    username:   "{{ mt_user }}"
    password:   "{{ mt_pass }}"
    state:      "absent"
    settings:
      interface:  "bridge2"
      address:    "192.168.88.2/24"
  register: ip_addr_rem_2
  failed_when: not ( ip_addr_rem_2 | changed )

- name: NEVER_CHANGES Test removing ip addr bridge2 again
  mt_ip_address:
    hostname:   "{{ mt_hostname }}"
    username:   "{{ mt_user }}"
    password:   "{{ mt_pass }}"
    state:      "absent"
    settings:
      interface:  "bridge2"
      address:    "192.168.88.2/24"
  register: ip_addr_rem_2
  failed_when: ip_addr_rem_2 | changed

- name: ALWAYS_CHANGES Test removing an ip addr from bridge4
  mt_ip_address:
    hostname:   "{{ mt_hostname }}"
    username:   "{{ mt_user }}"
    password:   "{{ mt_pass }}"
    state:      "absent"
    settings:
      interface:  "bridge4"
      address:    "192.168.88.4/24"
  register: ip_addr_rem_4
  failed_when: not (ip_addr_rem_4 | changed )

- name: NEVER_CHANGES Verify ip addr from bridge4 has been removed
  mt_ip_address:
    hostname:   "{{ mt_hostname }}"
    username:   "{{ mt_user }}"
    password:   "{{ mt_pass }}"
    state:      "absent"
    settings:
      interface:  "bridge4"
      address:    "192.168.88.4/24"
  register: ip_addr_rem_4
  failed_when: ip_addr_rem_4 | changed

- name: NEVER_CHANGES Verify that we have the right ip address in bridge4
  mt_ip_address:
    hostname:   "{{ mt_hostname }}"
    username:   "{{ mt_user }}"
    password:   "{{ mt_pass }}"
    state:      "present"
    settings:
      interface:  "bridge4"
      address:    "192.168.88.5/24"
  register: ip_addr_rem_4
  failed_when: ip_addr_rem_4 | changed 

- name: Remove any IP from bridge interfaces
  mt_ip_address:
    hostname: "{{ mt_hostname }}"
    username: "{{ mt_user }}"
    password: "{{ mt_pass }}"
    state:    absent
    idempotent: interface
    settings:
      interface: "{{ item }}"
  with_items:
    - "bridge1"
    - "bridge2"
    - "bridge3"
    - "bridge4"

- name: ALWAYS_CHANGES Add ip using idempotent interface on bridge2
  mt_ip_address:
    hostname:   "{{ mt_hostname }}"
    username:   "{{ mt_user }}"
    password:   "{{ mt_pass }}"
    state:      "present"
    idempotent: "interface"
    settings:
      interface:  "bridge2"
      address:    "192.168.89.2/24"
  register: ip_addr_rem_2
  failed_when: not (ip_addr_rem_2 | changed)

- name: NEVER_CHANGES Add AGAIN ip using idempotent interface on bridge2
  mt_ip_address:
    hostname:   "{{ mt_hostname }}"
    username:   "{{ mt_user }}"
    password:   "{{ mt_pass }}"
    state:      "present"
    idempotent: "interface"
    settings:
      interface:  "bridge2"
      address:    "192.168.89.2/24"
  register: ip_addr_rem_2
  failed_when: ip_addr_rem_2 | changed

- name: ALWAYS_CHANGES Add ip using idempotent interface on bridge3
  mt_ip_address:
    hostname:   "{{ mt_hostname }}"
    username:   "{{ mt_user }}"
    password:   "{{ mt_pass }}"
    state:      "present"
    idempotent: "interface"
    settings:
      interface:  "bridge3"
      address:    "192.168.89.3/24"
  register: ip_addr_rem_3
  failed_when: not (ip_addr_rem_3 | changed)

- name: ALWAYS_CHANGES Remove ip using idempotent interface on bridge3
  mt_ip_address:
    hostname:   "{{ mt_hostname }}"
    username:   "{{ mt_user }}"
    password:   "{{ mt_pass }}"
    state:      "absent"
    idempotent: "interface"
    settings:
      interface: "bridge3"
  register: ip_addr_rem_3
  failed_when: not (ip_addr_rem_3 | changed)

- name: NEVER_CHANGES Remove ip AGAIN using idempotent interface on bridge3
  mt_ip_address:
    hostname:   "{{ mt_hostname }}"
    username:   "{{ mt_user }}"
    password:   "{{ mt_pass }}"
    state:      "absent"
    idempotent: "interface"
    settings:
      interface: "bridge3" 
  register: ip_addr_rem_3
  failed_when: ip_addr_rem_3 | changed

- name: ALWAYS_CHANGES Add ip using idempotent interface on bridge4
  mt_ip_address:
    hostname:   "{{ mt_hostname }}"
    username:   "{{ mt_user }}"
    password:   "{{ mt_pass }}"
    state:      "present"
    idempotent: "interface"
    settings:
      interface:  "bridge4"
      address:    "192.168.89.4/24"
  register: ip_addr_rem_4
  failed_when: not (ip_addr_rem_4 | changed)

- name: ALWAYS_CHANGES Edit ip using idempotent interface on bridge4
  mt_ip_address:
    hostname:   "{{ mt_hostname }}"
    username:   "{{ mt_user }}"
    password:   "{{ mt_pass }}"
    state:      "present"
    idempotent: "interface"
    settings:
      interface:  "bridge4"
      address:    "192.168.89.5/24"
  register: ip_addr_rem_4
  failed_when: not (ip_addr_rem_4 | changed)

- name: ALWAYS_CHANGES Add comment using idempotent interface on bridge4
  mt_ip_address:
    hostname:   "{{ mt_hostname }}"
    username:   "{{ mt_user }}"
    password:   "{{ mt_pass }}"
    state:      "present"
    idempotent: "interface"
    settings:
      interface:  "bridge4"
      comment: "This is a final comment"
  register: ip_addr_rem_4
  failed_when: not (ip_addr_rem_4 | changed)


File: /tests\integration\tasks\test-ip-pool.yml
---
- name: Test adding ip pool
  mt_ip:
    hostname: "{{ mt_hostname }}"
    username: "{{ mt_user }}"
    password: "{{ mt_pass }}"
    state:       present
    parameter: pool
    settings:
      name: ansible_test
      ranges: 102.3.4.5

- name: NEVER_CHANGES Test adding duplicate ip pool
  mt_ip:
    hostname: "{{ mt_hostname }}"
    username: "{{ mt_user }}"
    password: "{{ mt_pass }}"
    state:       present
    parameter: pool
    settings:
      name: ansible_test
      ranges: 102.3.4.5
  register: ip_pool_test_1_add
  failed_when: (
      not ansible_check_mode
    ) and (
      ( ip_pool_test_1_add | changed )
    )

- name: ALWAYS_CHANGES Test adding second ip pool to be removed later
  mt_ip:
    hostname: "{{ mt_hostname }}"
    username: "{{ mt_user }}"
    password: "{{ mt_pass }}"
    state:       present
    parameter: pool
    settings:
      name: ansible_test2
      ranges: 102.3.4.22
  register: ip_pool_test_2_add
  failed_when: (
      not ansible_check_mode
    ) and (
      not ( ip_pool_test_2_add | changed )
    )

- name: Test adding ip pool to be used as next_pool
  mt_ip:
    hostname: "{{ mt_hostname }}"
    username: "{{ mt_user }}"
    password: "{{ mt_pass }}"
    state:       present
    parameter: pool
    settings:
      name: next_pool1
      ranges: 10.1.2.30-10.2.3.40

- name: ALWAYS_CHANGES Test editing an existing ip-pool item (change ranges add next_pool)
  mt_ip:
    hostname: "{{ mt_hostname }}"
    username: "{{ mt_user }}"
    password: "{{ mt_pass }}"
    state:       present
    parameter: pool
    settings:
      name: ansible_test
      ranges: 102.3.4.6
      next_pool: next_pool1
  register: ip_pool_test_1_edit
  failed_when: (
      not ansible_check_mode
    ) and (
      not ( ip_pool_test_1_edit | changed )
    )

- name: ALWAYS_CHANGES Test remove ip pool
  mt_ip:
    hostname: "{{ mt_hostname }}"
    username: "{{ mt_user }}"
    password: "{{ mt_pass }}"
    state:       absent
    parameter: pool
    settings:
      name: ansible_test2
  register: ip_pool_test_2_rem
  failed_when: (
      not ansible_check_mode
    ) and (
      not ( ip_pool_test_2_rem | changed )
    )


File: /tests\integration\tasks\test-neighbor.yml
---
- name: edit a interface discovery option
  mt_neighbor:
    hostname: "{{ mt_hostname }}"
    username: "{{ mt_user }}"
    password: "{{ mt_pass }}"
    parameter: discovery
    settings:
      name: ether2
      discover: "no"

- name: NEVER_CHANGES edit a interface discovery option
  mt_neighbor:
    hostname: "{{ mt_hostname }}"
    username: "{{ mt_user }}"
    password: "{{ mt_pass }}"
    parameter: discovery
    settings:
      name: ether2
      discover: "no"
  register: discovery_edit
  failed_when: (
      not ansible_check_mode
    ) and (
     ( discovery_edit | changed )
    )

- name: ALWAYS_CHANGES edit a interface discovery option
  mt_neighbor:
    hostname: "{{ mt_hostname }}"
    username: "{{ mt_user }}"
    password: "{{ mt_pass }}"
    parameter: discovery
    settings:
      name: ether2
      discover: "yes"
  register: discovery_edit
  failed_when: (
      not ansible_check_mode
    ) and (
     not ( discovery_edit | changed )
    )


File: /tests\integration\tasks\test-ovpn-client.yml
---
- name: Test adding ovpn-client
  mt_interfaces:
    hostname:  "{{ mt_hostname }}"
    username:  "{{ mt_user }}"
    password:  "{{ mt_pass }}"
    state:     present
    parameter: ovpn-client
    settings:
      comment: "ansible test 1"
      user:    ansible_admin
      connect-to:  192.168.50.170
      name: ansible_test
      password: 'blablabla'
  tags: vpn-client-test

- name: NEVER_CHANGES Test adding duplicate ovpn-client
  mt_interfaces:
    hostname:  "{{ mt_hostname }}"
    username:  "{{ mt_user }}"
    password:  "{{ mt_pass }}"
    state:     present
    parameter: ovpn-client
    settings:
      comment: "ansible test 1"
      user:    ansible_admin
      connect-to:  192.168.50.170
      name: ansible_test
      password: 'blablabla'
  register: ovpn_client_test_1_add
  failed_when: (
      not ansible_check_mode
    ) and (
      ( ovpn_client_test_1_add | changed )
    )
  tags: vpn-client-test

- name: ALWAYS_CHANGES Test editing an existing ovpn-client item (change address)
  mt_interfaces:
    hostname:  "{{ mt_hostname }}"
    username:  "{{ mt_user }}"
    password:  "{{ mt_pass }}"
    state:     present
    parameter: ovpn-client
    settings:
      comment: "ansible test 1"
      user:    ansible_admin
      connect-to:  192.168.50.171
      auth: "null"
      name: ansible_test
      password: 'bar'
  register: ovpn_client_test_1_edit
  failed_when: (
      not ansible_check_mode
    ) and (
      not ( ovpn_client_test_1_edit | changed )
    )
  tags: vpn-client-test

- name: ALWAYS_CHANGES Test adding a second ovpn-client to later remove
  mt_interfaces:
    hostname:  "{{ mt_hostname }}"
    username:  "{{ mt_user }}"
    password:  "{{ mt_pass }}"
    state:     present
    parameter: ovpn-client
    settings:
      user:    ansible_admin
      comment: "ansible test 2"
      connect_to:  192.168.52.111
      name: ansible_test2
  register: ovpn_client_test_2_add
  failed_when: (
      not ansible_check_mode
    ) and (
      not ( ovpn_client_test_2_add | changed )
    )

- name: ALWAYS_CHANGES Test remove ovpn-client
  mt_interfaces:
    hostname:  "{{ mt_hostname }}"
    username:  "{{ mt_user }}"
    password:  "{{ mt_pass }}"
    state:     absent
    parameter: ovpn-client
    settings:
      name: ansible_test2
  register: ovpn_client_test_2_rem
  failed_when: (
      not ansible_check_mode
    ) and (
      not ( ovpn_client_test_2_rem | changed )
    )


File: /tests\integration\tasks\test-scheduler.yml
---
- name: add scheduler
  mt_system_scheduler:
    hostname: "{{ mt_hostname }}"
    username: "{{ mt_user }}"
    password: "{{ mt_pass }}"
    state:    present
    parameter: scheduler
    settings:
      name:     ansible_test
      on_event: 'put "test"'
      interval: 1s
  tags: test1

- name: ALWAYS_CHANGES modify existing scheduler
  mt_system_scheduler:
    hostname: "{{ mt_hostname }}"
    username: "{{ mt_user }}"
    password: "{{ mt_pass }}"
    state:    present
    parameter: scheduler
    settings:
      name:     ansible_test
      on_event: 'put "test"'
      interval: 5s
      policy:
        - password
        - sniff
        - write
  register: scheduler_mod
  failed_when: (
      not ansible_check_mode
    ) and (
      not ( scheduler_mod | changed )
    )
  tags: test1

- name: NEVER_CHANGES add duplicate scheduler
  mt_system_scheduler:
    hostname: "{{ mt_hostname }}"
    username: "{{ mt_user }}"
    password: "{{ mt_pass }}"
    state:    present
    parameter: scheduler
    settings:
      name:     ansible_test
      on_event: 'put "test"'
      interval: 5s
      policy:
        - password
        - sniff
        - write
  register: scheduler_dup
  failed_when: (
      not ansible_check_mode
    ) and (
      ( scheduler_dup | changed )
    )
  tags: test1

- name: ALWAYS_CHANGES remove duplicate scheduler
  mt_system_scheduler:
    hostname: "{{ mt_hostname }}"
    username: "{{ mt_user }}"
    password: "{{ mt_pass }}"
    state:    absent
    parameter: scheduler
    settings:
      name:     ansible_test
  register: scheduler_rem
  failed_when: (
      not ansible_check_mode
    ) and (
      not ( scheduler_rem | changed )
    )
  tags: test1


File: /tests\integration\tasks\test-service.yml
---
- name: Test enabling ftp service
  mt_ip:
    hostname: "{{ mt_hostname }}"
    username: "{{ mt_user }}"
    password: "{{ mt_pass }}"
    parameter: service
    settings:
      disabled: "no"
      name:     ftp
      address:  192.168.50.1/32

- name: Test disabling services
  mt_ip:
    hostname: "{{ mt_hostname }}"
    username: "{{ mt_user }}"
    password: "{{ mt_pass }}"
    parameter: service
    settings:
      disabled: "yes"
      name: "{{ item }}"
  with_items:
    - ftp
    - telnet
    - api-ssl

- name: ALWAYS_CHANGES Test re-enabling telnet service
  mt_ip:
    hostname: "{{ mt_hostname }}"
    username: "{{ mt_user }}"
    password: "{{ mt_pass }}"
    parameter: service
    settings:
      disabled: "no"
      name:     telnet
  register: enable_telnet
  failed_when: (
      not ansible_check_mode
    ) and (
      not ( enable_telnet | changed )
    )


File: /tests\integration\tasks\test-snmp.yml
---
- name: add snmp community
  mt_snmp:
    hostname: "{{ mt_hostname }}"
    username: "{{ mt_user }}"
    password: "{{ mt_pass }}"
    state:     present
    parameter: community
    settings:
      addresses: "0.0.0.0/0"
      name: icghol

- name: add second snmp community to remove later
  mt_snmp:
    hostname: "{{ mt_hostname }}"
    username: "{{ mt_user }}"
    password: "{{ mt_pass }}"
    state:     present
    parameter: community
    settings:
      addresses: "192.168.1.0/24"
      name: to_remove

- name: ALWAYS_CHANGES remove second snmp community
  mt_snmp:
    hostname: "{{ mt_hostname }}"
    username: "{{ mt_user }}"
    password: "{{ mt_pass }}"
    state:     absent
    parameter: community
    settings:
      name: to_remove
  register: snmp_community_rem
  failed_when: (
      not ansible_check_mode
    ) and (
      not ( snmp_community_rem | changed )
    )

- name: ALWAYS_CHANGES modify existing snmp community
  mt_snmp:
    hostname: "{{ mt_hostname }}"
    username: "{{ mt_user }}"
    password: "{{ mt_pass }}"
    state:     present
    parameter: community
    settings:
      addresses: "10.0.0.0/8"
      name: icghol
  register: snmp_community
  failed_when: (
      not ansible_check_mode
    ) and (
      not ( snmp_community | changed )
    )

- name: NEVER_CHANGES check idempotency on snmp community
  mt_snmp:
    hostname: "{{ mt_hostname }}"
    username: "{{ mt_user }}"
    password: "{{ mt_pass }}"
    state:     present
    parameter: community
    settings:
      addresses: "10.0.0.0/8"
      name: icghol
  register: snmp_community_idem
  failed_when: (
      not ansible_check_mode
    ) and (
      ( snmp_community_idem | changed )
    )

- name: edit snmp settings
  mt_snmp:
    hostname: "{{ mt_hostname }}"
    username: "{{ mt_user }}"
    password: "{{ mt_pass }}"
    parameter: snmp
    settings:
      enabled: "yes"
      trap-community: icghol
      trap-version: 2

- name: NEVER_CHANGES edit snmp settings again check idempotency
  mt_snmp:
    hostname: "{{ mt_hostname }}"
    username: "{{ mt_user }}"
    password: "{{ mt_pass }}"
    parameter: snmp
    settings:
      enabled: "yes"
      trap-community: icghol
      trap-version: 2
  register: snmp_idem
  failed_when: (
      not ansible_check_mode
    ) and (
      ( snmp_idem | changed )
    )

- name: ALWAYS_CHANGES check editing snmp
  mt_snmp:
    hostname: "{{ mt_hostname }}"
    username: "{{ mt_user }}"
    password: "{{ mt_pass }}"
    parameter: snmp
    settings:
      enabled: "yes"
      trap-community: icghol
      trap-version: 3
  register: snmp_edit
  failed_when: (
      not ansible_check_mode
    ) and (
      not ( snmp_edit | changed )
    )


File: /tests\integration\tasks\test-system.yml
---
- name: set identity
  mt_system:
    hostname: "{{ mt_hostname }}"
    username: "{{ mt_user }}"
    password: "{{ mt_pass }}"
    parameter: identity
    settings:
      name: Test_mikrotik

- name: check if physical hardware
  mt_command:
    hostname: "{{ mt_hostname }}"
    username: "{{ mt_user }}"
    password: "{{ mt_pass }}"
    command: /system/routerboard/print
  register: routerboard
  tags: routerboard

- name: set routerboard settings on physical device
  mt_system:
    hostname: "{{ mt_hostname }}"
    username: "{{ mt_user }}"
    password: "{{ mt_pass }}"
    parameter: routerboard_settings
    settings:
      protected-routerboot: disabled
      boot-protocol: dhcp
  when: routerboard['msg'][0][0][1]['routerboard'] != "false"

- name: set clock
  mt_system:
    hostname: "{{ mt_hostname }}"
    username: "{{ mt_user }}"
    password: "{{ mt_pass }}"
    parameter: clock
    settings:
      time-zone-autodetect: "no"
      time-zone-name: Greenwich

- name: ALWAYS_CHANGES modify clock, change time-zone-name
  mt_system:
    hostname: "{{ mt_hostname }}"
    username: "{{ mt_user }}"
    password: "{{ mt_pass }}"
    parameter: clock
    settings:
      time-zone-name: GMT
  register: mt_clock
  failed_when: (
      not ansible_check_mode
    ) and (
      not ( mt_clock | changed )
    )

- name: set ntp client
  mt_system:
    hostname: "{{ mt_hostname }}"
    username: "{{ mt_user }}"
    password: "{{ mt_pass }}"
    parameter: ntp_client
    settings:
      enabled: "yes"
      primary-ntp: 199.182.221.11
      secondary-ntp: 67.215.197.149

- name: NEVER_CHANGES set ntp client, check idempotency
  mt_system:
    hostname: "{{ mt_hostname }}"
    username: "{{ mt_user }}"
    password: "{{ mt_pass }}"
    parameter: ntp_client
    settings:
      enabled: "yes"
      primary-ntp: 199.182.221.11
      secondary-ntp: 67.215.197.149
  register: mt_ntp_client
  failed_when: (
      not ansible_check_mode
    ) and (
      ( mt_ntp_client | changed )
    )

- name: ALWAYS_CHANGES modify ntp client
  mt_system:
    hostname: "{{ mt_hostname }}"
    username: "{{ mt_user }}"
    password: "{{ mt_pass }}"
    parameter: ntp_client
    settings:
      enabled: "no"
      primary-ntp: 199.182.221.11
      secondary-ntp: 67.215.197.149
  register: mt_ntp_client_change
  failed_when: (
      not ansible_check_mode
    ) and (
      not ( mt_ntp_client_change | changed )
    )

##############################################
# WIP
###############################################
- name: modify logging
  mt_system:
    hostname: "{{ mt_hostname }}"
    username: "{{ mt_user }}"
    password: "{{ mt_pass }}"
    parameter: logging
    settings: "{{ item }}"
  with_items:
    - numbers: "0"
      action: disk
      disabled: "yes"
    - numbers: "1"
      action: memory
      disabled: "yes"


File: /tests\integration\tasks\test-tool.yml
---
- name: set email settings
  mt_tool:
    hostname: "{{ mt_hostname }}"
    username: "{{ mt_user }}"
    password: "{{ mt_pass }}"
    parameter: e-mail
    settings:
      address: 192.168.1.2
      from: email@localhost.com

- name: ALWAYS_CHANGES set email settings
  mt_tool:
    hostname: "{{ mt_hostname }}"
    username: "{{ mt_user }}"
    password: "{{ mt_pass }}"
    parameter: e-mail
    settings:
      address: 192.168.1.3
      from: email@localhost.com
  register: email_edit
  failed_when: (
      not ansible_check_mode
    ) and (
      not ( email_edit | changed )
    )

- name: add netwatch item
  mt_tool:
    hostname: "{{ mt_hostname }}"
    username: "{{ mt_user }}"
    password: "{{ mt_pass }}"
    parameter: netwatch
    state:     present
    settings:
      host: '192.168.10.1'
      up-script: test

- name: NEVER_CHANGES add netwatch item, idempotency check
  mt_tool:
    hostname: "{{ mt_hostname }}"
    username: "{{ mt_user }}"
    password: "{{ mt_pass }}"
    parameter: netwatch
    state:     present
    settings:
      host: '192.168.10.1'
      up-script: test
  register: netwatch_idem
  failed_when: (
      not ansible_check_mode
    ) and (
      ( netwatch_idem | changed )
    )

- name: ALWAYS_CHANGES edit netwatch item, change up-script
  mt_tool:
    hostname: "{{ mt_hostname }}"
    username: "{{ mt_user }}"
    password: "{{ mt_pass }}"
    parameter: netwatch
    state:     present
    settings:
      host: '192.168.10.1'
      up-script: test2
  register: netwatch_edit
  failed_when: (
      not ansible_check_mode
    ) and (
      not ( netwatch_edit | changed )
    )

- name: ALWAYS_CHANGES remove netwatch item
  mt_tool:
    hostname: "{{ mt_hostname }}"
    username: "{{ mt_user }}"
    password: "{{ mt_pass }}"
    parameter: netwatch
    state:     absent
    settings:
      host: '192.168.10.1'
  register: netwatch_rem
  failed_when: (
      not ansible_check_mode
    ) and (
      not ( netwatch_rem | changed )
    )


File: /tests\integration\tasks\test-user.yml
---
- name: add a group
  mt_command:
    hostname: "{{ mt_hostname }}"
    username: "{{ mt_user }}"
    password: "{{ mt_pass }}"
    command:   /user/group/add
    command_arguments:
      name: group_test1
      policy: read,write,web,!local,!telnet,!ssh
      comment: ansible_test
  failed_when: false

- name: edit group
  mt_command:
    hostname: "{{ mt_hostname }}"
    username: "{{ mt_user }}"
    password: "{{ mt_pass }}"
    command:   /user/group/set
    command_arguments:
      numbers: 3
      name: group_test1
      comment: ansible_test2

- name: edit group
  mt_command:
    hostname: "{{ mt_hostname }}"
    username: "{{ mt_user }}"
    password: "{{ mt_pass }}"
    command:   /user/group/set
    command_arguments:
      name: group_test1
      policy: read,write,web,winbox

- name: add a test user to mikrotik
  mt_user:
    hostname: "{{ mt_hostname }}"
    username: "{{ mt_user }}"
    password: "{{ mt_pass }}"
    parameter: user
    state:    present
    settings:
      name: user_test1
      group: read
      password: 123
  changed_when: False

- name: NEVER_CHANGES, check idempotency add a user
  mt_user:
    hostname: "{{ mt_hostname }}"
    username: "{{ mt_user }}"
    password: "{{ mt_pass }}"
    parameter: user
    state:    present
    settings:
      name: user_test1
      group: read
  register: user_add
  failed_when: (
      not ansible_check_mode
    ) and (
     ( user_add | changed )
    )

- name: ALWAYS_CHANGES modify user
  mt_user:
    hostname: "{{ mt_hostname }}"
    username: "{{ mt_user }}"
    password: "{{ mt_pass }}"
    parameter: user
    state:    present
    settings:
      name: user_test1
      group: group_test1
  register: user_edit
  failed_when: (
      not ansible_check_mode
    ) and (
      not ( user_edit | changed )
    )

- name: ALWAYS_CHANGES remove user
  mt_user:
    hostname: "{{ mt_hostname }}"
    username: "{{ mt_user }}"
    password: "{{ mt_pass }}"
    parameter: user
    state:    absent
    settings:
      name: user_test1
  register: user_rem
  failed_when: (
      not ansible_check_mode
    ) and (
      not ( user_rem | changed )
    )


File: /tests\integration\tests.retry
127.0.0.1


File: /tests\integration\tests.yml
---
- name: Tests
  hosts: all
  gather_facts: no
  connection: local
  vars:
    # these should be defined at the inventory level
    # but must be here until the action plugin is working
    mt_hostname: '127.0.0.1'
    mt_user: 'admin'
    mt_pass: ''

  tasks:
    - name: Test login
      mt_login_test:
        hostname: "{{ mt_hostname }}"
        username: "{{ mt_user }}"
        password: "{{ mt_pass }}"
      tags: test_login

    ###############################
    # Interfaces
    #################################
    - block:
      ###################
      ### vlan block
      ###################
      - include: tasks/test-interface-vlan.yml
        tags: interfaces-vlan

      ########################
      ###  ethernet block
      ########################
      - include: tasks/test-interface-ethernet.yml
        tags: interfaces-ethernet

      tags: interfaces

    ###################
    ### ip-pool
    ###################
    - include: tasks/test-ip-pool.yml
      tags: ip-pool

    ##################
    ### dhcp-server
    ###################
    - include: tasks/test-dhcp-server.yml
      tags: dhcp-server

    ###################
    ### ovpn-client
    ###################
    - include: tasks/test-ovpn-client.yml
      tags: ovpn-client

    ###################
    ### radius
    ###################
    - include: tasks/radius-tests.yml
      tags: radius

    ###################
    ### address-list
    ###################
    - include: tasks/test-address-list.yml
      tags: address-list

    ###################
    ### ip_address
    ###################
    - include: tasks/test-ip-address.yml
      tags: ip-address

    ###################
    ### firewall block
    ###################
    - block:
      # filter block
      - include: tasks/test-firewall-filter.yml
        tags: firewall-filter

      # nat
      - include: tasks/test-firewall-nat.yml
        tags: firewall-nat

      tags: firewall

    ###################
    ### end firewall block
    ###################

    ###################
    ### ip service
    ###################
    - include: tasks/test-service.yml
      tags: service

    ###################
    ### interface bridge
    ###################
    - include: tasks/test-bridge.yml
      tags: bridge

    ###########################
    ### system scheduler
    ##########################

    - include: tasks/test-scheduler.yml
      tags: scheduler

    ###########################
    ### system command
    ##########################
    - include: tasks/test-command.yml
      tags: command

    ###################
    ### system
    ###################
    - include: tasks/test-system.yml
      tags: system

    ###################
    ### tool
    ###################
    - include: tasks/test-tool.yml
      tags: tool

    ###################
    ### snmp
    ###################
    - include: tasks/test-snmp.yml
      tags: snmp

    ###################
    ### hotspot
    ###################
    - include: tasks/hotspot-tests.yml
      tags: hotspot

    ###################
    ### neighbor
    ###################
    - include: tasks/test-neighbor.yml
      tags: neighbor

    ###################
    ### user
    ###################
    - include: tasks/test-user.yml
      tags: user
    ###################
    ### interface wireless
    ###################
    - include: tasks/test-interface-wireless.yml
      tags: interface-wireless

    - include: tasks/test-facts.yml
      tags: get-facts


File: /Vagrantfile
# -*- mode: ruby -*-
# vi: set ft=ruby :

vmname = 'mikrotik-6-38-1'

# Specify minimum Vagrant version and Vagrant API version
Vagrant.require_version ">= 1.6.0"
VAGRANTFILE_API_VERSION = "2"


Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|

  #config.vm.box = 'mikrotik-6-38-1'
  config.vm.box = vmname
  config.vm.hostname = 'mikrotik01'
  config.vm.network "private_network", ip: '192.168.60.202'
  config.vm.network "private_network", ip: '192.168.60.203'
  config.vm.network "private_network", ip: '192.168.60.204'
  config.vm.network "private_network", ip: '192.168.60.205'
  config.vm.network "private_network", ip: '192.168.60.206'
  config.vm.network "private_network", ip: '192.168.60.207'
  config.vm.network "private_network", ip: '192.168.60.208'
  config.vm.network "private_network", ip: '192.168.60.209'
  config.vm.network "private_network", ip: '192.168.60.210'
  config.vm.network "private_network", ip: '192.168.60.211'
  config.vm.network "private_network", ip: '192.168.60.212'
  config.vm.network :forwarded_port, guest: 22, host: 2301, id: 'ssh'
  config.vm.network :forwarded_port, guest: 8728, host: 8728, id: 'api'
  config.vm.network :forwarded_port, guest: 80, host: 8080, id: 'web'

  config.vm.provider :virtualbox do |vb|
      vb.name = vmname + '_test'
  end
end


