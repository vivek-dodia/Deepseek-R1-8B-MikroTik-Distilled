# Repository Information
Name: ansible-mikrotik-bachelor

# Directory Structure
Directory structure:
└── github_repos/ansible-mikrotik-bachelor/
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
    │   │       │   └── ansible-mikrotik-bachelor
    │   │       └── remotes/
    │   │           └── origin/
    │   │               └── HEAD
    │   ├── objects/
    │   │   ├── info/
    │   │   └── pack/
    │   │       ├── pack-0079232cb2a4619fbe836eae8adbfd4f3f7fc987.idx
    │   │       └── pack-0079232cb2a4619fbe836eae8adbfd4f3f7fc987.pack
    │   ├── packed-refs
    │   └── refs/
    │       ├── heads/
    │       │   └── ansible-mikrotik-bachelor
    │       ├── remotes/
    │       │   └── origin/
    │       │       └── HEAD
    │       └── tags/
    ├── .gitattributes
    ├── .gitignore
    ├── bachelor/
    ├── changes.txt
    └── Mikrotik_devel/
        │   └── vcs.xml
        ├── backup/
        │   ├── mk_test.py.backup.v1
        │   └── RosAPI_backup.py
        ├── cdp_discovery.py
        ├── dyn_to_sta.py
        ├── group_vars/
        │   └── .gitkeep
        ├── hosts
        ├── host_vars/
        │   ├── .gitkeep
        │   └── Router3
        ├── inint.yml
        ├── library/
        │   ├── mtbash_clean.sh
        │   ├── mtbash_default.sh
        │   ├── mt_brctl.py
        │   ├── mt_dhcp.py
        │   ├── mt_dhcp_net.py
        │   ├── mt_dhcp_srv.py
        │   ├── mt_dns.py
        │   ├── mt_fetch.py
        │   ├── mt_firewall.py
        │   ├── mt_ip.py
        │   ├── mt_ip_pool.py
        │   ├── mt_nat.py
        │   ├── mt_nat2.py
        │   ├── mt_raw.py
        │   ├── mt_rip.py
        │   ├── mt_static_route.py
        │   ├── RosAPI.py
        │   ├── RosAPI2.py
        │   ├── RosCore.py
        │   ├── RosRaw.py
        │   ├── test.py
        │   └── __init__.py
        ├── roles/
        │   ├── .gitkeep
        │   ├── default/
        │   │   ├── handlers/
        │   │   │   └── handlers.yml
        │   │   └── tasks/
        │   │       ├── dhcp_server.yml
        │   │       ├── firewall.yml
        │   │       └── main.yml
        │   └── init/
        │       ├── files/
        │       │   ├── mtbash_clean.sh
        │       │   └── mtbash_default.sh
        │       └── tasks/
        │           ├── clear.yml
        │           ├── default.yml
        │           └── main.yml
        ├── site.yml
        ├── testik.yml
        ├── test_playbook.yml
        ├── test_playbook01.yml
        ├── test_playbook02.yml
        └── test_playbook_show.yml


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
	url = https://github.com/mihudec/ansible-mikrotik-bachelor.git
	fetch = +refs/heads/*:refs/remotes/origin/*
[branch "ansible-mikrotik-bachelor"]
	remote = origin
	merge = refs/heads/ansible-mikrotik-bachelor


File: /.git\description
Unnamed repository; edit this file 'description' to name the repository.


File: /.git\HEAD
ref: refs/heads/ansible-mikrotik-bachelor


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
0000000000000000000000000000000000000000 0b9b258de1b7c8e513dda2ac87e65818b85334da vivek-dodia <vivek.dodia@icloud.com> 1738606057 -0500	clone: from https://github.com/mihudec/ansible-mikrotik-bachelor.git


File: /.git\logs\refs\heads\ansible-mikrotik-bachelor
0000000000000000000000000000000000000000 0b9b258de1b7c8e513dda2ac87e65818b85334da vivek-dodia <vivek.dodia@icloud.com> 1738606057 -0500	clone: from https://github.com/mihudec/ansible-mikrotik-bachelor.git


File: /.git\logs\refs\remotes\origin\HEAD
0000000000000000000000000000000000000000 0b9b258de1b7c8e513dda2ac87e65818b85334da vivek-dodia <vivek.dodia@icloud.com> 1738606057 -0500	clone: from https://github.com/mihudec/ansible-mikrotik-bachelor.git


File: /.git\packed-refs
# pack-refs with: peeled fully-peeled sorted 
0b9b258de1b7c8e513dda2ac87e65818b85334da refs/remotes/origin/ansible-mikrotik-bachelor
3c183c69f32949e1814351ff0edbfcdbf46c9ca1 refs/remotes/origin/ansible-mikrotik-devel


File: /.git\refs\heads\ansible-mikrotik-bachelor
0b9b258de1b7c8e513dda2ac87e65818b85334da


File: /.git\refs\remotes\origin\HEAD
ref: refs/remotes/origin/ansible-mikrotik-bachelor


File: /.gitattributes
# Auto detect text files and perform LF normalization
* text=auto

# Custom for Visual Studio
*.cs     diff=csharp

# Standard to msysgit
*.doc	 diff=astextplain
*.DOC	 diff=astextplain
*.docx diff=astextplain
*.DOCX diff=astextplain
*.dot  diff=astextplain
*.DOT  diff=astextplain
*.pdf  diff=astextplain
*.PDF	 diff=astextplain
*.rtf	 diff=astextplain
*.RTF	 diff=astextplain


File: /.gitignore
# Windows image file caches
Thumbs.db
ehthumbs.db

# Folder config file
Desktop.ini

# Recycle Bin used on file shares
$RECYCLE.BIN/

# Windows Installer files
*.cab
*.msi
*.msm
*.msp

# Windows shortcuts
*.lnk

# =========================
# Operating System Files
# =========================

# OSX
# =========================

File: /changes.txt
25.3.2016 16:20
	-Vytvoen projektu na GitHubu
	-Nstin 1. kapitoly (Potaov st) - teoretick st

File: /Mikrotik_devel\.idea\vcs.xml
<?xml version="1.0" encoding="UTF-8"?>
<project version="4">
  <component name="VcsDirectoryMappings">
    <mapping directory="$PROJECT_DIR$/.." vcs="Git" />
  </component>
</project>

File: /Mikrotik_devel\backup\mk_test.py.backup.v1
#!/usr/bin/python
# -*- coding: UTF-8 -*-
# THIS IS ANSIBLE MODULE USED FOR CONFIGUTING MIKROTIK ROUTEROS DEVICES

DOCUMENTATION = '''
---
module: mk_test
author: Miroslav Hudec
version_added: "0.2"
short_description: Manage Mikrotik Routers
requirements: [ RosAPI ]
description:
    - Manage Mikrotik RouterOS devices.
options:

'''

from ansible.module_utils.basic import *
from ansible.modules.RosAPI import Core

# Import Ansible module parameters
ansible = AnsibleModule(
    argument_spec=dict(
        hostname=dict(required=True, type='str'),
        username=dict(required=True, type='str'),
        password=dict(required=True, type='str'),
        remote_requests=dict(required=False, type='str'),
        servers=dict(required=False, type='str'),

    ),
    supports_check_mode=False
)


def main(): # main logic
    # Initialize phase
    output = {"changed": True, "failed": True, "msg": "Everything is OK :-)"}
    hostname = ansible.params['hostname']
    username = ansible.params['username']
    password = ansible.params['password']

    args = {}

    if "servers" in ansible.params.keys():
        args["servers"] = ansible.params['servers']



    lst = ["/ip/dns/set"]
    # Connect
    mikrotik = Core(hostname, DEBUG=False)
    mikrotik.login(username, password)

    # Check if there's need to change anything
    response = mikrotik.talk(["/ip/dns/print"])
    isSame = True
    for key in args.keys():
       if args[key] != response[0][1]["="+key]:
           isSame = False


    if isSame:
        ansible.exit_json(changed=False, msg="Already in desired state")

    else:
        # Create list for arguments
        for a in args.keys():
            lst.append("="+a+"="+str(args[a]))
        mikrotik.talk(lst)
        ansible.exit_json(changed=True, msg="Configured to desired state by Ansible")

from ansible.module_utils.basic import *
main()


File: /Mikrotik_devel\backup\RosAPI_backup.py
#!/usr/bin/python
# -*- coding: utf-8 -*-
#
#
from ansible.module_utils.RosCore import *


class Auth:

    def __init__(self, host, hostsfile="/etc/ansible/hosts", DEBUG=False):
        hostsfile = open(hostsfile, mode='r')
        DEBUG = False
        # Determine number of lines in the file
        num_lines = sum(1 for line in hostsfile)
        if DEBUG: print num_lines
        hostsfile.seek(0)


        hostsdict = {}
        # Create dictionary from file lines
        for i in range(0, num_lines):
            workline = hostsfile.readline()
            if DEBUG: print workline
            # If line isn't empty
            if workline and workline[0] != '[':

                linearray = workline.split(' ')
                if DEBUG: print linearray
                linedict = dict(host=linearray[0].strip())
                linearray.remove(linearray[0])
                for i in range(0, len(linearray)):
                    if DEBUG: print linearray[i].split('=')
                    linedict[linearray[i].split('=')[0].strip()] = linearray[i].split('=')[1].strip()
                    hostsdict[linedict['host']] = linedict

                if DEBUG: print linedict
                if host in hostsdict.keys():
                    if 'hostname' in hostsdict[host].keys():
                        self.hostname = hostsdict[host]['hostname']
                    if 'username' in hostsdict[host].keys():
                        self.username = hostsdict[host]['username']
                    if 'password' in hostsdict[host].keys():
                        self.password = hostsdict[host]['password']

def changeCheck(response, command, DEBUG=False):
    priv_params = ["name", "comment"]
    while True:
        r = {"exists": "", "isSame": True}
        decision = []
        if len(response) > 1:
            decision = [0] * (len(response) - 1)
            # Decide which response has most common arguments
            for i in range(0, len(decision), 1):
                for key in command.keys():
                    if str("=" + key) in response[i][1].keys():
                        if (command[key] == response[i][1]["=" + key]):
                            decision[i] += 1
                            if key in priv_params:
                                decision[i] += 9

            if DEBUG == True: print decision, response

        elif len(response) == 1:
            r["exists"] = False
            r["isSame"] = False
            return r

        """Check if object with most common values is truly unique, otherwise
          object does not yet exist and will be created with ADD"""
        # If there is more than 1 object
        if len(decision) > 1:

            if sorted(decision)[-1] > sorted(decision)[-2]:
                r["exists"] = True
                # Get ID of object with most common values for SET option
                r["id"] = response[decision.index(max(decision))][1]["=.id"]
            else:
                r["exists"] = False
        # If there are no objects
        # If there is exactly 1 object
        elif len(decision) == 1:
            if decision[0] == 0:
                r["exists"] = False
            else:
                r["exists"] = True

            if "=.id" in response[0][1].keys():
                r["id"] = response[0][1]["=.id"]

        """If at least one value doesn't match command, it is NOT the same
         - we'll either ADD new or SET existing to match all values """
        for key in command.keys():
            if str("=" + key) in response[decision.index(max(decision))][1].keys():
                if command[key] != response[decision.index(max(decision))][1]["=" + key]:
                    r["isSame"] = False

        return r

def replyCheck(r):
    reply = {"success": True}
    for i in range(0,len(r)-1):
        if r[i][0] == "!trap":
            if '=message' in r[i][1].keys():
                reply["message"] = r[i][1]['=message']
            reply["success"] = False
            break
    return reply

def intCheck(interface_name, hostname, username, password, port=8728):
    # Checks if desired interface exists

    while True:
        # Check if interface exists
        response = API("/interface/", "print", hostname, username=username, password=password)

        if response["msg"] == "Login failed":
            return {"msg": "Login Failed", "Exists": "Unknown"}

        interfaces = [0] * (len(response["response"]) - 1)

        for i in range(0, len(interfaces)):
            interfaces[i] = response["response"][i][1]["=name"]

        if interface_name in interfaces:
            interfaceExists = True
            return {"msg": "Interface with specified name exists.", "Exists": True}

        else:
            interfaceExists = False
            return {"msg": "Interface with specified name does not exists.", "Exists": False}


def digestArg(argument, backwards=False):
    l = list(argument)
    if backwards:
        # Hyphens to underscores
        for i in range(0, len(argument) - 1):
            if l[i] == "-":  # Find
                l[i] = "_"  # Replace with
    else:
        # Underscores to hyphens
        for i in range(0, len(argument) - 1):
            if l[i] == "_":  # Find
                l[i] = "-"  # Replace with
    newarg = "".join(l)
    return newarg

def digestArgs(arguments):
    newargs = {}
    for key in arguments.keys():
        if arguments[key] is not None:
            newargs[digestArg(key)] = arguments[key]
    return newargs

def stripResponse(response):
    strippedresponse = {}
    for key in response.keys():
        strippedresponse[key[1:]] = response[key]
    return strippedresponse

def API(path, action, hostname="", username="admin", password="", command=None, port=8728, DEBUG=False):
    changed = False
    lst = []

    while True:

        # Connect
        mikrotik = Core(hostname, DEBUG=DEBUG)
        login = mikrotik.login(username, password)
        # Check if login is correct
        if login[0][0] == '!trap':
            if DEBUG == True:
                print login

            return {"failed": True, "changed": False, "msg": "Login failed"}

        else:
            if DEBUG == True:
                print login



        response = mikrotik.talk([path + "print"])
        if DEBUG == True: print response



        if action == "print":
            return {"failed": False, "changed": changed, "msg": "No changes were made", "response": response, "isSame": None}

        r = changeCheck(response, command, DEBUG=DEBUG)
        if r["isSame"]:
            mikrotik.close_connection()
            return {"failed": False, "changed": changed, "msg": "Already in desired state."}

        else:
            # In case that similar object already exists
            if r["exists"] == True:

                # Create list for arguments
                if "id" in r.keys():
                    namematch = True
                    if "name" in command.keys():
                        for i in range(0, len(response)-1):
                            if response[i][1]["=.id"] == r["id"]:
                                namematch = (command["name"] == response[i][1]["=name"])

                                break
                        if namematch:
                            lst = [path + "set", "=.id=" + r["id"]]
                        else:
                            lst = [path + "add"]
                        del command["name"]
                    else:
                        lst = [path + "set", "=.id=" + r["id"]]
                else:
                    lst = [path + "set"]

            # In case there's no similar object
            elif r["exists"] == False:
                # Create list for arguments
                # Allow force set by module
                if action == "set":
                    lst = [path + "set"]
                else:
                    lst = [path + "add"]


        # Add commands to argument string
        for key in command.keys():
            lst.append("=" + key + "=" + str(command[key]))




        # Apply changes
        mikrotik.talk(lst)
        # Check if changes were actually applied
        if changeCheck(mikrotik.talk([path + "print"]), command, DEBUG=DEBUG)["isSame"]:
            changed = True

            mikrotik.close_connection()
            return {"failed": False, "changed": changed, "msg": "Configured to desired state by Ansible"}

        else:
            mikrotik.close_connection()
            return {"failed": True, "changed": changed, "msg": "Something went wrong..."}



File: /Mikrotik_devel\cdp_discovery.py
#! /usr/bin/env python
# A small script for cdp devices discovery

import sys
import pcapy
import socket
import getopt
import binascii
import simplejson


from dpkt import ethernet
from dpkt import cdp




def discover_neighbors(interface, timeout=100, DEBUG=False):
    global escape

    try:
        pcap = pcapy.open_live(interface, 65535, 1, timeout)
        pcap.setfilter('ether[20:2] == 0x2000')  # CDP filter

        try:
            while not escape:
                # this is more responsive to  keyboard interrupts
                pcap.dispatch(1, on_cdp_packet)
        except KeyboardInterrupt, e:
            pass
    except Exception, e:
        print e


def on_cdp_packet(header, data):
    global inventory
    global escape
    global numpackets
    global debug

    numpackets += 1
    if debug: print "Captured %d packets" % numpackets
    ether_frame = ethernet.Ethernet(data)
    cdp_packet = ether_frame["cdp"]


    src = binascii.hexlify(ether_frame["src"])
    src_mac = ':'.join(src[i:i+2] for i in range(0,12,2))


    cdp_info = {}
    for info in cdp_packet.data:
        cdp_info.update({info['type']: info['data']})


    if cdp.CDP_ADDRESS in cdp_info.keys():
        addresses = [socket.inet_ntoa(x.data) for x in cdp_info[cdp.CDP_ADDRESS]]
        if len(addresses) < 2:
            address = addresses[0]
    else:
        address = ""

    output = {'ID': cdp_info[cdp.CDP_DEVID], 'IP': address, 'Port': cdp_info[cdp.CDP_PORTID], \
              'Version': cdp_info[cdp.CDP_VERSION], \
              'Platform':cdp_info[cdp.CDP_PLATFORM], "Source_MAC": src_mac}
    if debug: print output

    if output["Source_MAC"] in inventory.keys(): # if there is record in inventory
        if output == inventory[output["Source_MAC"]]: # if records are identical
            escape = True
            if debug: print "Captured duplicate packet. Exiting."
    else:
        inventory[output["Source_MAC"]] = output



inventory = {}
escape = False
numpackets = 0
debug = False
interface = "eth0" # try default interface if no supplied
option = ""



def main():
    global interface
    global option
    global debug
    global inventory

    args = sys.argv
    if "--list" in args:
        option = "list"
    if "-D" in args:
        debug = True
    if "-i" in args:
        interface = args[args.index("-i")+1]
    if debug: print "Waiting for CDP packets..."
    if debug: print args
    discover_neighbors(interface=interface,\
                       DEBUG=debug, timeout=100)
    # Decide if output should be sorted by ID or Src-MAC
    duplicate = False

    ids = []
    for key in inventory.keys():
        if inventory[key]["ID"] not in ids:
            ids.append(inventory[key]["ID"])
            if debug: print ids
        else:
            if debug: print "\n Duplicate ID detected, sorting by Src-MAC instead..."
            duplicate = True
            break


    # Generate inventory for JSON output
    raw_inventory = {"_meta":{"hostvars":{}}, "mikrotiks":{"hosts":[], "vars": {}}}
    if duplicate:
        for key in inventory.keys():
            raw_inventory["_meta"]["hostvars"][key] = inventory[key]
            raw_inventory["mikrotiks"]["hosts"].append(key)

    else:
        for key in inventory.keys():
            raw_inventory["_meta"]["hostvars"][inventory[key]["ID"]] = inventory[key]
            raw_inventory["mikrotiks"]["hosts"].append(inventory[key]["ID"])

    # Add default variables
    raw_inventory["mikrotiks"]["vars"]["default_user"] = "admin"
    raw_inventory["mikrotiks"]["vars"]["default_password"] = ""
    output =  simplejson.dumps(raw_inventory, separators=("," , ":"), indent=2, sort_keys=True)
    print output

if __name__ == '__main__':
    main()

File: /Mikrotik_devel\dyn_to_sta.py
#!/usr/bin/env python

# Converts Ansible dynamic inventory sources to static files
# Input is received via stdin from the dynamic inventory file
#   ex:
#     ec2.py --list | ansible-dynamic-inventory-converter.py

import json
import os
import sys

import pyaml

def add_vars(_type, _id, variables):
    assert _type == "group" or _type == "host"
    dir_name = "./%s_vars" % _type
    if not os.path.isdir(dir_name):
        os.mkdir(dir_name)
    with open('%s/%s' % (dir_name, _id), 'w') as fh:
        fh.write(pyaml.dump(variables))

def add_host_vars(host, variables):
    add_vars('host', host, variables)

def add_group_vars(group, variables):
    add_vars('group', group, variables)

def main():
    raw_json = sys.stdin.read()
    inventory = json.loads(raw_json)
    inventory_filename = "./hosts"

    with open(inventory_filename, 'w') as fh:
        for group in inventory:
            if group == "_meta":
                for host, variables in inventory[group]["hostvars"].iteritems():
                    add_host_vars(host, variables)
            if "vars" in inventory[group]:
                add_group_vars(group, inventory[group]["vars"])
            if "hosts" in inventory[group]:
                fh.write("[%s]\n" % group)
                for host in inventory[group]["hosts"]:
                    fh.write("%s\n" % host)
                fh.write("\n")
            if "children" in inventory[group]:
                fh.write("[%s:children]\n" % group)
                for child in inventory[group]["children"]:
                    fh.write("%s\n" % child)
                fh.write("\n")
if __name__ == '__main__':
    main()

File: /Mikrotik_devel\hosts
[mikrotiks]
Router1
Router2
Router3



File: /Mikrotik_devel\host_vars\Router3
ID: Router3
IP: 192.168.116.120
Platform: MikroTik
Port: ether1
Source_MAC: 00:0C:29:64:90:36
Version: 6.32.3
et1addr: "192.168.116.120/24"
et2addr: "192.168.3.1/24"
pool_ranges: "192.168.3.10 - 192.168.3.200"
pool_name: POOL3
dhcp_address: "192.168.3.0/24"
rip_interfaces: ether1
net_comment: NET3



File: /Mikrotik_devel\inint.yml
- name: Mikrotik TEST
  hosts: all
  connection: local
  gather_facts: no
  vars:
    username: ansible
    password: ansible
  tasks:
  - name: Clear MikroTik Configuration
    mt_clean: username={{username}} mac_addr={{Source-MAC}} password={{password}}


File: /Mikrotik_devel\library\mtbash_clean.sh
#!/usr/bin/expect


set mac [lindex $argv 0]
set user [lindex $argv 1]
set pass [lindex $argv 2]

#Init phase
set ses 1

#set $::env(TERM) xterm
spawn "mactelnet" "$mac"
set ses $spawn_id
set timeout 200
expect -i $ses "Login:"
send -i $ses "$user\r"
expect -i $ses "Password:"
send -i $ses "$pass\r"
sleep 5
send -i $ses "\r"


#Reset configuration with no default settings
expect "*>*"
send -i $ses "/system reset-configuration no-defaults=yes\r"
sleep 1
send -i $ses "y\r"
sleep 1

exit 0



File: /Mikrotik_devel\library\mtbash_default.sh
#!/usr/bin/expect


#Destination MAC Address
set mac [lindex $argv 0]
#Username used for connection
set user [lindex $argv 1]
#Password used for connection
set pass [lindex $argv 2]
#Set Mikrotik's Identity
set identity [lindex $argv 3]
#Username for new user
set new_user [lindex $argv 4]
#Password for new user
set new_pass [lindex $argv 5]
#Interface used for management
set interface [lindex $argv 6]
#IP address used for management
set ip [lindex $argv 7]



set ses 1
set $::env(TERM) xterm
spawn "mactelnet" "$mac"
set ses $spawn_id
set timeout 200
expect -i $ses "Login:"
exp_send -i $ses "$user\r"
expect -i $ses "Password:"
exp_send -i $ses "$pass\r"
sleep 5
exp_send -i $ses "\r"


#Set identity
expect -i $ses "*>*"
exp_send -i $ses "/system identity set name=$identity\r"
sleep 1

#Create new user for management
expect -i $ses "*>*"
exp_send -i $ses "/user add name=$new_user password=$new_pass group=full\r"
sleep 1

#Set IP address on connected interface
expect -i $ses "*>*"
exp_send -i $ses "/ip address add address=$ip interface=$interface\r"
sleep 1

#END
expect -i $ses "*>*"
exp_send -i $ses "^D"
exit


File: /Mikrotik_devel\library\mt_brctl.py
#!/usr/bin/python
# -*- coding: UTF-8 -*-
# THIS IS ANSIBLE MODULE USED FOR CONFIGUTING MIKROTIK ROUTEROS DEVICES

DOCUMENTATION = '''
---
module: mt_brctl
author: Miroslav Hudec
version_added: ""
short_description: Manage Mikrotik Routers
requirements: [ RosAPI ]
description:
    - Manage Mikrotik RouterOS devices.
options:
    hostname:
        required: True
        aliases: ["host"]
        description:
        - Hostname or IP address of Mikrotik device
    username:
        required: True
        aliases: ["user"]
        description:
        - Username used to login to Mikrotik's API
    password:
        required: True
        aliases: ["pass"]
        description:
        - Password used to login to Mikrotik's API


'''

from ansible.module_utils.basic import *
from ansible.module_utils.RosAPI import *
from ansible.module_utils.RosRaw import *



# Import Ansible module parameters
ansible = AnsibleModule(
        argument_spec=dict(
                hostname=dict(required=False, type='str', aliases=["host"]),
                username=dict(required=False, type='str', aliases=["user"]),
                password=dict(required=False, type='str', aliases=["pass"]),
                port=dict(required=False, type='int', default=8728),

                names=dict(required=True, type='list'),
                admin_mac=dict(required=False, type='str', choices=["true", "false"]),
                disabled=dict(required=False, type='str', choices=["true", "false"]),
                mtu=dict(required=False, type='int'),
                priority=dict(required=False, type='int'),
                comment=dict(required=False, type='str'),

                interfaces=dict(required=False, type='list'),
                auto_isolate=dict(required=False, type='str', choices=["true", "false"]),
                point_to_point=dict(required=False, type='str', choices=["true", "false", "auto"]),
                path_cost=dict(required=False, type='int'),



        ),

        supports_check_mode=False,

)
"""


# Debugging Section
class AnsibleModule:  # Provides Ansible-like parameters
    params = {"username": "admin", "hostname": "192.168.116.100", "password": "", \
              "names": ["bridge-local"], "port": 8728, "disabled": "false", "interfaces": ["!ether2", "!ether3"]}


ansible = AnsibleModule
"""
# Global Variables
privkeys = ["hostname", "username", "password", "port", "path", "action"]
# Initialize phase
# Required parameters
hostname = ansible.params['hostname']
username = ansible.params['username']
password = ansible.params['password']
port = ansible.params['port']
DEBUG = False  # This is only for debugging, if set to True Ansible will crash
switch = True  # Global switch


def toRawCommand(params):
    rawcmd = []
    for key in params.keys():
        if (key not in privkeys) and (params[key] is not None):
            rawcmd.append("=" + digestArg(key) + "=" + str(params[key]))


def main():  # main logic
    moduleparams=digestArgs(ansible.params)
    if DEBUG: print "moduleparams: " + str(moduleparams)
    exitmessage = []

    while True:
        changed = False
        # Required params
        privkeys = ["hostname", "username", "password", "port", "path", "action"]

        # Section for Bridge management
        brparams = ["admin_mac", "disabled", "mtu", "priority", "comment"]

        # For each bridge name
        if moduleparams["names"] is not None:
            # Create common command
            brcommand = {}
            for key in moduleparams.keys():
                if (key not in privkeys) and (key in brparams) and (moduleparams[key] is not None):
                    brcommand[digestArg(key)] = str(moduleparams[key])
            if DEBUG: print brcommand

            for bridge in moduleparams["names"]:
                brcommand["name"] = bridge
                response = API(path="/interface/bridge/", action="add", username=username, password=password, \
                               hostname=hostname, port=port, command=brcommand)
                if response['failed']:
                    if DEBUG: print bridge + " failed."
                    if response["msg"] == "Login failed":
                        ansible.fail_json(failed=True, changed=False, msg=response["msg"])
                    else:
                        ansible.fail_json(failed=True, changed=False, msg=["Configuring " + bridge + " failed.", \
                                                                           exitmessage])
                if response['changed']:
                    if DEBUG: print bridge + " was configured to desired state."
                    exitmessage.append(bridge + " was configured to desired state;")
                    changed = True
                else:
                    if DEBUG: print bridge + " is already in desired state."
                    exitmessage.append(bridge + " is already in desired state;")

        # Section for ports management

        intparams = ["auto_isolate", "point_to_point", "path_cost"]

        if (moduleparams["interfaces"] is not None) and (len(moduleparams["interfaces"]) > 0):

            # Remove interface if requested:
            remove = {"remove": False, "interfaces": {}}
            # Check which interfaces should be removed
            for interface in moduleparams["interfaces"]:
                if interface[0] == "!":
                    interface = interface[1:]
                    remove["remove"] = True
                    remove["interfaces"][interface] = {}

            # Remove "to-be-removed" interfaces from interface list
            for interface in remove["interfaces"].keys():
                moduleparams["interfaces"].remove("!" + interface)


            if DEBUG: print "Remove: " + str(remove)

            if remove["remove"]:
                response = RosRaw(path="/interface/bridge/port/", action="print", username=username, password=password, \
                                  hostname=hostname, port=port, command=["=.proplist=bridge,interface,.id"])
                if DEBUG: print "Remove section PRINT response: " + str(response)
                response = response["response"][:-1]
                for interface in remove["interfaces"].keys():

                    for i in range(0, len(response)):

                        if (response[i][1]["=interface"] == interface) and (response[i][1]["=bridge"] == moduleparams["names"][0]):
                            remove["interfaces"][interface]["id"] = response[i][1]["=.id"]
                            # Remove interface
                            if DEBUG: print "Removing " + interface + " from bridge " + \
                                            response[i][1][
                                                "=bridge"]
                            rep = RosRaw(path="/interface/bridge/port/", action="remove", username=username,
                                         password=password, \
                                         hostname=hostname, port=port,
                                         command=["=.id=" + remove["interfaces"][interface]["id"]])
                            if DEBUG: print "Remove reply: " + str(rep)
                            if rep["response"][0][0] == "!done":
                                exitmessage.append(
                                    "Interface " + interface + " successfully removed from " +
                                    response[i][1]["=bridge"])
                                remove["interfaces"][interface]["removed"] = True
                                changed = True
                                if DEBUG:
                                    print "Interface " + response[i][1]["=interface"] + " successfully removed from " + \
                                          response[i][1]["=bridge"]
                            else:
                                if DEBUG: print "Unhandled exception, failed to remove " + interface
                                exitmessage.append(
                                    "Unhandled exception, failed to remove " + interface)
                                ansible.fail_json(failed=True, msg=exitmessage)
                    if "removed" not in remove["interfaces"][interface].keys():
                        if DEBUG: print "Interface " + interface + " is not port of " + moduleparams["names"][0]
                        exitmessage.append("Interface " + interface + " is not port of " + moduleparams["names"][0])


        if len(moduleparams["interfaces"]) > 0:
            # Create common command
            intcommand = {}
            intrawcommand = []
            intproplist = []
            for key in moduleparams.keys():
                if (key not in privkeys) and (key in intparams) and (moduleparams[key] is not None):
                    intcommand[digestArg(key)] = str(moduleparams[key])
                    intrawcommand.append("=" + digestArg(key) + "=" + str(moduleparams[key]))
                    intproplist.append(digestArg(key))
            if DEBUG: print intcommand, intproplist

            propstr = ""
            for item in intproplist:
                propstr = propstr + item + ","

            for interface in moduleparams["interfaces"]:
                intcommand["interface"] = interface
                intcommand["bridge"] = moduleparams["names"][0]  # Add ports to first specified bridge
                intrawcommandfull = intrawcommand[:]
                intrawcommandfull.append("=interface=" + interface)
                intrawcommandfull.append("=bridge=" + moduleparams["names"][0])

                response = RosRaw(path="/interface/bridge/port/", action="add", username=username, password=password, \
                                  hostname=hostname, port=port, command=intrawcommandfull)

                response = response["response"][0]
                if DEBUG: print "Response for " + interface + " :" + str(response)
                if response[0] == "!trap":
                    if response[1]["=message"] == "failure: device already added as bridge port":
                        # Port is already added, check it's properties...
                        propstrfull = propstr[:] + "bridge,.id"

                        response = RosRaw(path="/interface/bridge/port/", action="print", username=username,
                                          password=password, \
                                          hostname=hostname, port=port,
                                          command=['?interface=' + interface, '=.proplist=' + propstrfull])
                        if DEBUG: print "Interface " + interface + " PRINT output: " + str(response)
                        response = stripResponse(response["response"][:-1][0][1])
                        id = response[".id"]

                        isSame = True
                        for prop in intproplist:
                            if moduleparams[digestArg(prop, True)] != response[prop]:
                                isSame = False

                        if DEBUG: print interface + " properties: " + str(response), " isSame=" + str(isSame)
                        if isSame:
                            exitmessage.append(
                                    "Interface " + interface + " with ID " + id + " is already in desired state.")
                            if DEBUG: print "Interface " + interface + " with ID " + id + " is already in desired state."

                        else:
                            intrawcommandfull.append("=.id=" + id)
                            response = RosRaw(path="/interface/bridge/port/", action="set", username=username,
                                              password=password, \
                                              hostname=hostname, port=port, command=intrawcommandfull)
                            if DEBUG: print "Response for interface " + interface + " SET commnad: " + str(response)
                            if response["response"][0][0] == "!done":
                                if DEBUG: print "Interface " + interface + " with ID " + id + " already existed, Ansible changed it's properties."
                                changed = True
                                exitmessage.append(
                                        "Interface " + interface + " with ID " + id + " already existed, Ansible changed it's properties.")
                            else:
                                if DEBUG: print "Failed to SET interface " + interface + " with ID " + id + " to desired state."
                                exitmessage.append(
                                        "Failed to SET interface " + interface + " with ID " + id + " to desired state.")
                                ansible.fail_json(failed=True, message=exitmessage)
                                changed = True
                    else:
                        if DEBUG: "Unhandled exception, RosRaw returned: " + str(response)
                        exitmessage.append("Unhandled exception." + str(response) + str(len(moduleparams["interfaces"])))
                        ansible.fail_json(failed=True, msg=exitmessage)

                elif response[0] == "!done":
                    if DEBUG: print "Interface " + interface + " added as " + moduleparams["names"][0] + " port."
                    exitmessage.append("Interface " + interface + " added as " + moduleparams["names"][0] + " port.")
                    changed = True

        message = "Already in desired state." + str(exitmessage)
        if changed: message = "Configured to desired state by Ansible." + str(exitmessage)

        ansible.exit_json(failed=False, changed=changed, msg=message)


from ansible.module_utils.basic import *

main()


File: /Mikrotik_devel\library\mt_dhcp.py
#!/usr/bin/python
# -*- coding: UTF-8 -*-


DOCUMENTATION = '''
---
module: mt_ip
author: Miroslav Hudec
version_added: ""
short_description: Sets IP addresses on Mikrotik's interfaces
requirements: [ RosAPI ]
description:
    - Sets IP addresses on Mikrotik's interfaces
options:
    hostname:
        required: True
        aliases: ["host"]
        description:
        - Hostname or IP address of Mikrotik device
    username:
        required: True
        aliases: ["user"]
        description:
        - Username used to login to Mikrotik's API
    password:
        required: True
        aliases: ["pass"]
        description:
        - Password used to login to Mikrotik's API
    address:
        required: True
        aliases: ["ip", "addr"]
    interface:
        aliases: ["int"]
        required: True
    disabled:
        required: True
        choices: ['yes', 'no']

'''

from ansible.module_utils.basic import *
from ansible.module_utils.RosAPI import *




# Import Ansible module parameters
ansible = AnsibleModule(
        argument_spec=dict(
                hostname=dict(required=False, type='str', aliases=["host"]),
                username=dict(required=False, type='str', aliases=["user"]),
                password=dict(required=False, type='str', aliases=["pass"]),
                port=dict(required=False, type='int', default=8728),

                network_address=dict(required=False, type='str'),
                gateway=dict(required=False, type='str'),
                dns_server=dict(required=False, type='str'),
                domain=dict(required=False, type='str'),
                ntp_server=dict(required=False, type='str'),
                network_comment=dict(required=False, type='str'),

                pool_name=dict(required=False, type='str'),
                pool_ranges=dict(required=False, type='str'),

                disabled=dict(required=True, type='str', choices=['true', 'false']),
                address_pool=dict(required=True, type='str'),
                interface=dict(required=True, type='str'),
                name=dict(required=True, type='str'),


        ),
        supports_check_mode=False,

)



"""
# Debugging Section
class AnsibleModule:  # Provides Ansible-like parameters
    params = {"username": "admin", "hostname": "192.168.116.100", "password": "", "port": 8728,\
              "network_address": "192.168.50.0/24", "gateway": "192.168.50.1", "dns_server": "192.168.60.1",\
              "network_comment": "NET1", "pool_name": "POOL1",\
              "pool_ranges": "192.168.50.100-192.168.50.220",\
              "address_pool": "POOL1", "interface": "bridge-local", "name": "SRV1", "srv_comment": "SRV1",\
              }

ansible = AnsibleModule

"""

# Global Variables
privkeys = ["hostname", "username", "password", "port", "path", "action"]
# Initialize phase
# Required parameters
hostname = ansible.params['hostname']
username = ansible.params['username']
password = ansible.params['password']
port = ansible.params['port']
DEBUG = False  # This is only for debugging, if set to True Ansible will crash
moduleparams = digestArgs(ansible.params)
exitmessage = []
changed = False


def cutParams(beggining, command):
    newcommand = {}
    length = len(beggining)
    for key in command.keys():
        if key[:length] == beggining:
            newcommand[key[length:]] = command[key]
        else:
            newcommand[key] = command[key]
    return newcommand


def main():

    #IP Pool Section
    poolcommands = ["pool-name", "pool-ranges"]
    poolcommand = {}
    for key in moduleparams:
        if key not in privkeys and key in poolcommands:
            poolcommand[key] = moduleparams[key]
    poolcommand = cutParams("pool-", poolcommand)

    response = API(hostname=hostname, username=username, password=password, port=port,\
                   path="/ip/pool/", command=poolcommand, DEBUG=DEBUG)
    if DEBUG: print response
    exitmessage.append(response["msg"])
    if response["failed"]:
        ansible.fail_json(failed=response["failed"], changed=response["changed"], msg=exitmessage)

    # Network Section
    netcommands = ["network-address", "gateway", "dns-server",\
                   "domain", "ntp-server", "network-comment"]
    netcommand = {}
    for key in moduleparams:
        if key not in privkeys and key in netcommands:
            netcommand[key] = moduleparams[key]
    print "Netcommand: "+str(netcommand)
    netcommand = cutParams("network-", netcommand)
    print "Netcommand: "+str(netcommand)


    response = API(hostname=hostname, username=username, password=password, port=port,\
                   path="/ip/dhcp-server/network/", command=netcommand, DEBUG=DEBUG)
    exitmessage.append(response["msg"])
    if response["failed"]:
        ansible.fail_json(failed=response["failed"], changed=response["changed"], msg=exitmessage)

    # Server Section
    srvcommands = ["disabled", "address-pool", "interface", "name"]
    srvcommand = {}
    for key in moduleparams:
        if key not in privkeys and key in srvcommands:
            srvcommand[key] = moduleparams[key]
    srvcommand = cutParams("srv-", srvcommand)

    response = API(hostname=hostname, username=username, password=password, port=port,\
                   path="/ip/dhcp-server/", command=srvcommand, DEBUG=DEBUG)
    exitmessage.append(response["msg"])
    if response["failed"]:
        ansible.fail_json(failed=response["failed"], changed=response["changed"], msg=exitmessage)



    ansible.exit_json(failed=response["failed"], changed=response["changed"], msg=exitmessage)

from ansible.module_utils.basic import *
if __name__ == '__main__':
    main()

File: /Mikrotik_devel\library\mt_dhcp_net.py
#!/usr/bin/python
# -*- coding: UTF-8 -*-
# THIS IS ANSIBLE MODULE USED FOR CONFIGUTING MIKROTIK ROUTEROS DEVICES

DOCUMENTATION = '''
---
module: mt_dhcp_net
author: Miroslav Hudec
version_added: ""
short_description: Sets information provided by DHCP server
requirements: [ RosAPI ]
description:
    - Sets information provided by DHCP server, such as default gateway, DNS servers, domain name etc...
options:
    hostname:
        required: True
        aliases: ["host"]
        description:
        - Hostname or IP address of Mikrotik device
    username:
        required: True
        aliases: ["user"]
        description:
        - Username used to login to Mikrotik's API
    password:
        required: True
        aliases: ["pass"]
        description:
        - Password used to login to Mikrotik's API
    port:
        required: False
        description:
        - Port used to connect to MikroTik's API, default 8728


'''

from ansible.module_utils.basic import *

# Import Ansible module parameters
ansible = AnsibleModule(
        argument_spec=dict(
                hostname=dict(required=False, type='str', aliases=["host"]),
                username=dict(required=False, type='str', aliases=["user"]),
                password=dict(required=False, type='str', aliases=["pass"]),
                port=dict(required=False, type='int', default=8728),
                network_address=dict(required=False, type='str'),
                gateway=dict(required=False, type='str'),
                dns_server=dict(required=False, type='str'),
                netmask=dict(required=False, type='str'),
                domain=dict(required=False, type='str'),
                ntp_server=dict(required=False, type='str'),

        ),
        supports_check_mode=False,

)


def main():  # main logic

    from ansible.module_utils.RosAPI import *

    # Initialize phase
    # Required parameters

    hostname = ansible.params['hostname']
    username = ansible.params['username']
    password = ansible.params['password']
    port = ansible.params['port']

    while True:

        # DHCP Server
        path = "/ip/dhcp-server/network/"
        action = ""

        command = {}

        if ("hostname" in ansible.params.keys()) and (ansible.params['hostname'] != None):
            hostname = ansible.params['hostname']
        if ("username" in ansible.params.keys()) and (ansible.params['username'] != None):
            username = ansible.params['username']
        if ("password" in ansible.params.keys()) and (ansible.params['password'] != None):
            password = ansible.params['password']
        if ("network_address" in ansible.params.keys()) and (ansible.params['network_address'] != None):
            command["address"] = ansible.params['network_address']
        if ("gateway" in ansible.params.keys()) and (ansible.params['gateway'] != None):
            command["gateway"] = ansible.params['gateway']
        if ("dns_server" in ansible.params.keys()) and (ansible.params['dns_server'] != None):
            command["dns-server"] = ansible.params['dns_server']
        if ("netmask" in ansible.params.keys()) and (ansible.params['netmask'] != None):
            command["netmask"] = ansible.params['netmask']
        if ("domain" in ansible.params.keys()) and (ansible.params['domain'] != None):
            command["domain"] = ansible.params['domain']
        if ("ntp_server" in ansible.params.keys()) and (ansible.params['ntp_server'] != None):
            command["ntp-server"] = ansible.params['ntp_server']

        # Let RosAPI do the rest
        response = API(path, action, hostname, username, password, command=command, port=port)
        ansible.exit_json(failed=response['failed'], changed=response['changed'], msg=response['msg'])


from ansible.module_utils.basic import *
main()

File: /Mikrotik_devel\library\mt_dhcp_srv.py
#!/usr/bin/python
# -*- coding: UTF-8 -*-
# THIS IS ANSIBLE MODULE USED FOR CONFIGUTING MIKROTIK ROUTEROS DEVICES

DOCUMENTATION = '''
---
module: mt_dhcp_srv
author: Miroslav Hudec
version_added: ""
short_description: Sets DHCP server on interface
requirements: [ RosAPI ]
description:
    - Sets DHCP server on desired interface. This requires having IP pool defined.
options:
    hostname:
        required: True
        aliases: ["host"]
        description:
        - Hostname or IP address of Mikrotik device
    username:
        required: True
        aliases: ["user"]
        description:
        - Username used to login to Mikrotik's API
    password:
        required: True
        aliases: ["pass"]
        description:
        - Password used to login to Mikrotik's API


'''

from ansible.module_utils.basic import *

# Import Ansible module parameters
ansible = AnsibleModule(
        argument_spec=dict(
                hostname=dict(required=False, type='str', aliases=["host"]),
                username=dict(required=False, type='str', aliases=["user"]),
                password=dict(required=False, type='str', aliases=["pass"]),
                port=dict(required=False, type='int', default=8728),
                disabled=dict(required=True, type='str', choices=['true', 'false']),
                address_pool=dict(required=True, type='str'),
                interface=dict(required=True, type='str'),
                name=dict(required=True, type='str'),


        ),
        supports_check_mode=False,

)


def main():  # main logic

    from ansible.module_utils.RosAPI import API
    from ansible.module_utils.RosAPI import intCheck
    # Initialize phase
    # Required parameters

    hostname = ansible.params['hostname']
    username = ansible.params['username']
    password = ansible.params['password']
    port = ansible.params['port']

    while True:

        # DHCP Server
        path = "/ip/dhcp-server/"
        action = ""
        command = {"name": ansible.params['name'], "address-pool": ansible.params['address_pool'], "interface": ansible.params['interface'], "disabled": ansible.params["disabled"]}


        # Check if interface exists
        response = intCheck(command["interface"], hostname, username, password, port)
        interfaceExists = response["Exists"]
        if not interfaceExists:
            ansible.fail_json(failed=True, changed=False, msg=response["msg"])
            break

        response = API(path, action, hostname, username, password, command=command, port=port)
        ansible.exit_json(failed=response['failed'], changed=response['changed'], msg=response['msg'])



from ansible.module_utils.basic import *
main()

File: /Mikrotik_devel\library\mt_dns.py
#!/usr/bin/python
# -*- coding: UTF-8 -*-
# THIS IS ANSIBLE MODULE USED FOR CONFIGUTING MIKROTIK ROUTEROS DEVICES

DOCUMENTATION = '''
---
module: mt_dns
author: Miroslav Hudec
version_added: ""
short_description: Manage Mikrotik Routers
requirements: [ RosAPI ]
description:
    - Manage Mikrotik RouterOS devices.
options:
    hostname:
        required: True
        aliases: ["host"]
        description:
        - Hostname or IP address of Mikrotik device
    username:
        required: True
        aliases: ["user"]
        description:
        - Username used to login to Mikrotik's API
    password:
        required: True
        aliases: ["pass"]
        description:
        - Password used to login to Mikrotik's API

'''

from ansible.module_utils.basic import *

# Import Ansible module parameters
ansible = AnsibleModule(
        argument_spec=dict(
                hostname=dict(required=False, type='str', aliases=["host"]),
                username=dict(required=False, type='str', aliases=["user"]),
                password=dict(required=False, type='str', aliases=["pass"]),
                port=dict(required=False, type='int', default=8728),
                remote_requests=dict(required=False, type='str'),
                servers=dict(required=False, type='str'),

        ),
        supports_check_mode=False,

)


def main():  # main logic
    from ansible.module_utils.RosAPI import API
    # Initialize phase
    # Required parameters

    hostname = ansible.params['hostname']
    username = ansible.params['username']
    password = ansible.params['password']
    port = ansible.params['port']

    path = "/ip/dns/"
    # This module forces SET option
    action = ""

    command = {}

    if ("servers" in ansible.params.keys()) and (ansible.params['servers'] != None):
        command["servers"] = ansible.params['servers']

    if ("remote_requests" in ansible.params.keys()) and (ansible.params['remote_requests'] != None):
        command["allow-remote-requests"] = ansible.params['remote_requests']



    while True:
        response = API(path=path, action=None, hostname=hostname, port=port, username=username, password=password, command=command)
        ansible.exit_json(failed=response['failed'], changed=response['changed'], msg=response['msg'])
        break

from ansible.module_utils.basic import *

main()


File: /Mikrotik_devel\library\mt_fetch.py
#!/usr/bin/python
# -*- coding: UTF-8 -*-
# THIS IS ANSIBLE MODULE USED FOR CONFIGUTING MIKROTIK ROUTEROS DEVICES

DOCUMENTATION = '''
---
module: mt_dhcp_server
author: Miroslav Hudec
version_added: ""
short_description: Sets information provided by DHCP server
requirements: [ RosAPI ]
description:
    - Sets information provided by DHCP server, such as default gateway, DNS servers, domain name etc...
options:
    hostname:
        required: True
        aliases: ["host"]
        description:
        - Hostname or IP address of Mikrotik device
    username:
        required: True
        aliases: ["user"]
        description:
        - Username used to login to Mikrotik's API
    password:
        required: True
        aliases: ["pass"]
        description:
        - Password used to login to Mikrotik's API
    port:
        required: False
        description:
        - Port used to connect to MikroTik's API, default 8728


'''

from ansible.module_utils.basic import *

# Import Ansible module parameters
ansible = AnsibleModule(
        argument_spec=dict(
                hostname=dict(required=False, type='str', aliases=["host"]),
                username=dict(required=False, type='str', aliases=["user"]),
                password=dict(required=False, type='str', aliases=["pass"]),
                port=dict(required=False, type='int', default=8728),
                mode=dict(required=False, type='str', choices=["ftp", "http", "https"]),
                src_path=dict(required=False, type='str'),
                dst_path=dict(required=False, type='str'),
                keep_result=dict(required=False, type='str', choices=["True", "False"]),
                connection_username=dict(required=False, type='str', aliases=["con_user"]),
                connection_password=dict(required=False, type='str', aliases=["con_pass"]),
                upload=dict(required=False, type='str', choices=["True", "False"]),
                url=dict(required=False, type='str'),
                address=dict(required=False, type='str', aliases=["addr"])
        ),
        supports_check_mode=False,

)

def main():  # main logic

    from ansible.module_utils.RosAPI import *

    # Initialize phase
    # Required parameters

    hostname = ansible.params['hostname']
    username = ansible.params['username']
    password = ansible.params['password']
    port = ansible.params['port']

    while True:

        # DHCP Server
        path = "/tool/fetch"
        action = "raw"

        command = {}

        if ("hostname" in ansible.params.keys()) and (ansible.params['hostname'] != None):
            hostname = ansible.params['hostname']
        if ("username" in ansible.params.keys()) and (ansible.params['username'] != None):
            username = ansible.params['username']
        if ("password" in ansible.params.keys()) and (ansible.params['password'] != None):
            password = ansible.params['password']
        if ("mode" in ansible.params.keys()) and (ansible.params['mode'] != None):
            command["mode"] = ansible.params['mode']
        if ("src_path" in ansible.params.keys()) and (ansible.params['src_path'] != None):
            command["src-path"] = ansible.params['src_path']
        if ("dst_path" in ansible.params.keys()) and (ansible.params['dst_path'] != None):
            command["dst-path"] = ansible.params['dst_path']
        if ("keep_result" in ansible.params.keys()) and (ansible.params['keep_result'] != None):
            command["keep-result"] = ansible.params['keep_result']
        if ("domain" in ansible.params.keys()) and (ansible.params['domain'] != None):
            command["domain"] = ansible.params['domain']
        if ("connection_username" in ansible.params.keys()) and (ansible.params['connection_username'] != None):
            command["user"] = ansible.params['connection_username']
        if ("connection_password" in ansible.params.keys()) and (ansible.params['connection_password'] != None):
            command["password"] = ansible.params['connection_password']
        if ("url" in ansible.params.keys()) and (ansible.params['url'] != None):
            command["url"] = ansible.params['url']
        if ("address" in ansible.params.keys()) and (ansible.params['address'] != None):
            command["address"] = ansible.params['address']

        # Let RosAPI do the rest
        response = API(path, action, hostname, username, password, command=command, port=port)
        ansible.exit_json(failed=response['failed'], changed=response['changed'], msg=response['msg'])


from ansible.module_utils.basic import *
main()

File: /Mikrotik_devel\library\mt_firewall.py
#!/usr/bin/python
# -*- coding: UTF-8 -*-
# THIS IS ANSIBLE MODULE USED FOR CONFIGUTING MIKROTIK ROUTEROS DEVICES

DOCUMENTATION = '''
---
module: mt_firewall
author: Miroslav Hudec
version_added: ""
short_description: Manage Mikrotik Routers
requirements: [ RosAPI ]
description:
    - Manage Mikrotik RouterOS devices.
options:
    hostname:
        required: True
        aliases: ["host"]
        description:
        - Hostname or IP address of Mikrotik device
    username:
        required: True
        aliases: ["user"]
        description:
        - Username used to login to Mikrotik's API
    password:
        required: True
        aliases: ["pass"]
        description:
        - Password used to login to Mikrotik's API


'''

from ansible.module_utils.basic import *
from ansible.module_utils.RosAPI import *
from ansible.module_utils.RosRaw import *


# Import Ansible module parameters
ansible = AnsibleModule(
        argument_spec=dict(
                hostname=dict(required=False, type='str', aliases=["host"]),
                username=dict(required=False, type='str', aliases=["user"]),
                password=dict(required=False, type='str', aliases=["pass"]),
                port=dict(required=False, type='int', default=8728),

                chain=dict(required=True, type='str', choices=["input", "output", "forward"]),
                action=dict(required=True, type='str', choices=["accept", "reject", "drop"]),
                disabled=dict(required=False, type='str', choices=["true", "false"]),
                in_interface=dict(required=False, type='str'),
                out_interface=dict(required=False, type='str'),
                connection_state=dict(required=False, type='str'),
                connection_nat_state=dict(required=False, type='str'),
                protocol=dict(required=False, type='str'),
                src_address=dict(required=False, type='str'),
                dst_address=dict(required=False, type='str'),
                src_port=dict(required=False, type='str'),
                dst_port=dict(required=False, type='str'),
                log=dict(required=False, type='str', choices=["true", "false"]),
                log_prefix=dict(required=False, type='str'),
                comment=dict(required=True, type='str'),



        ),

        supports_check_mode=False,

)
"""


# Debugging Section
class AnsibleModule:
    params = {"username": "admin", "hostname": "192.168.116.100", "password": "", \
              "in_interface": "ether1", "port": 8728, "disabled": "false", "chain": "forward",\
              "connection_state": "established,related", "log": "false", "action": "accept", "comment": "rule1"}


ansible = AnsibleModule
"""
# Global Variables
privkeys = ["hostname", "username", "password", "port", "path", "action"]
# Initialize phase
# Required parameters
hostname = ansible.params['hostname']
username = ansible.params['username']
password = ansible.params['password']
port = ansible.params['port']
DEBUG = False # This is only for debugging, if set to True Ansible will crash



def main():  # main logic

    moduleparams = digestArgs(ansible.params)
    exitmessage = []

    while True:
        changed = False
        # Required params
        privkeys = ["hostname", "username", "password", "port", "path", "action"]
        rawcommand = []
        command = {}
        proplist = []
        propstr = ""

        for key in moduleparams.keys():
            if key not in privkeys:
                command[key] = moduleparams[key]
                proplist.append(key)
                propstr = propstr + key + ","
                rawcommand.append("=" + key + "=" + moduleparams[key])
        propstr = propstr + ".id"
        printcommand = ["=.proplist=" + propstr]


        # Call print
        response = RosRaw(path="/ip/firewall/filter/", action="print", username=username, hostname=hostname, \
                       password=password, command=printcommand, port=port, DEBUG=DEBUG)
        response = digestResponse(response["response"])
        if DEBUG: print "Print response: " + str(response)
        newresponse = {}
        # checkresponse
        isSame = True
        hascomment = False
        matchingresponse = {}
        id = ""

        if response != "noObjects":

            for i in range(0, len(response)):
                if command["comment"] == response[i]["comment"]:
                    if not hascomment:
                        hascomment = True
                        id = response[i][".id"]
                        matchingresponse = response[i]
                        info = "Found matching comment at ID "+ id
                        if DEBUG: print info
                        exitmessage.append(info)
                    else:
                        info = "Found multiple matching comments, cannot continue..."
                        if DEBUG: print info
                        exitmessage.append(info)
                        ansible.fail_json(failed=True, changed=False, msg="Module failed" + str(exitmessage))

        if hascomment:
            for item in proplist:
                if command[item] != matchingresponse[item]:
                    isSame = False
            if isSame:
                # Already in desired state
                info = "Matching rule with specified parameters already exists with ID: " + id
                exitmessage.append(info)
                if DEBUG: print info
                ansible.exit_json(failed=False, changed=False, msg="Already in desired state" + str(exitmessage))
            else:
                # SET
                rawcommand.append("=.id=" + id)
                response = RosRaw(path="/ip/firewall/filter/", action="set", username=username, hostname=hostname, \
                       password=password, command=rawcommand, port=port, DEBUG=DEBUG)
                if DEBUG: print "SET response: " + str(response)
                if response["response"][0][0] == "!done":
                    info = "Specified rule was SET by Ansible with ID "+id
                    if DEBUG: print info
                    exitmessage.append(info)
                    ansible.exit_json(Failed=False, changed=True, msg="Configured to desired state by Ansible." + str(exitmessage))
                else:
                    info = "Failed to SET rule."
                    if DEBUG: print info
                    exitmessage.append(info)
                    ansible.exit_json(Failed=True, changed=False, msg="Something went wrong." + str(exitmessage))

        else:
            # ADD
            response = RosRaw(path="/ip/firewall/filter/", action="add", username=username, hostname=hostname, \
                       password=password, command=rawcommand, port=port, DEBUG=DEBUG)
            if DEBUG: print "ADD response: "+str(response)
            if response["response"][0][0] == "!done":
                info = "Specified rule was ADDed by Ansible with ID "+response["response"][0][1]["=ret"]
                if DEBUG: print info
                exitmessage.append(info)
                ansible.exit_json(Failed=False, changed=True, msg="Configured to desired state by Ansible." + str(exitmessage))
            else:
                info = "Failed to ADD rule."
                if DEBUG: print info
                exitmessage.append(info)
                ansible.exit_json(Failed=True, changed=False, msg="Something went wrong." + str(exitmessage))



















from ansible.module_utils.basic import *

main()


File: /Mikrotik_devel\library\mt_ip.py
#!/usr/bin/python
# -*- coding: UTF-8 -*-


DOCUMENTATION = '''
---
module: mt_ip
author: Miroslav Hudec
version_added: ""
short_description: Sets IP addresses on Mikrotik's interfaces
requirements: [ RosAPI ]
description:
    - Sets IP addresses on Mikrotik's interfaces
options:
    hostname:
        required: True
        aliases: ["host"]
        description:
        - Hostname or IP address of Mikrotik device
    username:
        required: True
        aliases: ["user"]
        description:
        - Username used to login to Mikrotik's API
    password:
        required: True
        aliases: ["pass"]
        description:
        - Password used to login to Mikrotik's API
    address:
        required: True
        aliases: ["ip", "addr"]
    interface:
        aliases: ["int"]
        required: True
    disabled:
        required: True
        choices: ['yes', 'no']

'''

from ansible.module_utils.basic import *
from ansible.module_utils.RosAPI import *
from ansible.module_utils.RosRaw import *



# Import Ansible module parameters
ansible = AnsibleModule(
        argument_spec=dict(
                hostname=dict(required=False, type='str', aliases=["host"]),
                username=dict(required=False, type='str', aliases=["user"]),
                password=dict(required=False, type='str', aliases=["pass"]),
                port=dict(required=False, type='int', default=8728),
                address=dict(required=False, type='str', aliases=['ip', 'addr']),
                interface=dict(required=True, type='str', aliases=['int']),
                comment=dict(required=False, type='str'),


        ),
        supports_check_mode=False,
)

"""
# Debugging Section
class AnsibleModule:  # Provides Ansible-like parameters
    params = {"username": "admin", "hostname": "192.168.116.100", "password": "", \
              "interface": "bridge-local", "port": 8728, "address": "192.168.201.1/24"}

ansible = AnsibleModule
"""


# Global Variables
privkeys = ["hostname", "username", "password", "port", "path", "action"]
# Initialize phase
# Required parameters
hostname = ansible.params['hostname']
username = ansible.params['username']
password = ansible.params['password']
port = ansible.params['port']
DEBUG = False  # This is only for debugging, if set to True Ansible will crash
moduleparams = digestArgs(ansible.params)
exitmessage = []
changed = False


def main():


    moduleparams = digestArgs(ansible.params)
    exitmessage = []
    changed = False
    path = "/ip/address/"
    action = "add"
    command = {}
    commandstr = []
    proplist = []
    propstr = ""

    for key in moduleparams.keys():
        if key not in privkeys:
            if moduleparams[key][0] == "!":
                command[key] = moduleparams[key][1:]
                commandstr.append("="+key+"="+moduleparams[key][1:])
            else:
                command[key] = moduleparams[key]
                commandstr.append("="+key+"="+moduleparams[key])
            proplist.append(key)

    for item in proplist:
        propstr = propstr + item + ","
    propstr = propstr + ".id"



    if DEBUG: print "Command: " + str(command) +"\nCommandstr: " + str(commandstr) + "\n"

    while True:

        # Check if interface exists
        response = RosRaw(hostname=hostname, username=username, password=password, port=port,\
                          path="/interface/", action="print", command=["=.proplist=name,.id,type"])
        response = response["response"][:-1]
        interfacelist = {}

        for i in range(0, len(response)):
            interfacelist[response[i][1]["=name"]] = [response[i][1]["=.id"], response[i][1]["=type"]]
        if DEBUG: print str(response) + "\nInterfacelist: " + str(interfacelist)
        intExists = False
        if (moduleparams["interface"] in interfacelist.keys()) or (moduleparams["interface"][1:] in interfacelist.keys()):
            intExists = True
        if intExists:
            exitmessage.append("Interface "+ moduleparams["interface"] + " exists.")
            if DEBUG: print "Interface "+ moduleparams["interface"] + " exists."
        else:
            exitmessage.append("Interface "+ moduleparams["interface"] + " does not exist.")
            if DEBUG: print "Interface "+ moduleparams["interface"] + " does not exist."
            ansible.fail_json(failed=True, msg=exitmessage)




        # Check current IP addresses


        response = RosRaw(hostname=hostname, username=username, password=password, port=port,\
                          path="/ip/address/", action="print", command=["=.proplist=interface,address,.id,network,netmask"])
        response = response["response"][:-1]
        if DEBUG: print "IP address PRINT: " + str(response)
        addresslist = {}
        ipinterfacelist = {}
        for i in range(0, len(response)):
            addresslist[response[i][1]["=address"]] = response[i][1]["=interface"]
            ipinterfacelist[response[i][1]["=interface"]] = [response[i][1]["=address"], response[i][1]["=.id"]]
        if DEBUG: print "Addresslist: " + str(addresslist) + "\nIPinterfacelist: " + str(ipinterfacelist)

        #Remove interface address
        remove = {"remove": False, "interface": {}}



        if (moduleparams["interface"][0] == "!"):
            remove["remove"] = True

            if (moduleparams["interface"][1:] in ipinterfacelist):



                interface = moduleparams["interface"][1:]
                if DEBUG: print "Removing interface: " + interface
                moduleparams["interface"] = moduleparams["interface"][1:]

                remove["interface"][interface] = {}
                remove["interface"][interface][".id"] = ipinterfacelist[interface][1]
                if DEBUG: print "Remove: " + str(remove)
                # Talk
                response = RosRaw(hostname=hostname, username=username, password=password, port=port,\
                          path="/ip/address/", action="remove", command=["=.id="+ remove["interface"][interface][".id"]])
                response = response["response"]
                if DEBUG: print "Remove response: " + str(response)
                if response[0][0] == "!done":
                    changed = True
                    if DEBUG: print "Interface IP address of " + interface + " was removed by Ansible"
                    exitmessage.append("Interface IP address of " + interface + " was removed by Ansible")
                    break



            else:
                exitmessage.append("Iterface " + moduleparams["interface"][1:] + " does not have IP address, cannot remove.")
                if DEBUG: print "Iterface " + moduleparams["interface"][1:] + " does not have IP address, cannot remove."
                ansible.fail_json(failed=True, msg=exitmessage)






        if remove["remove"] == False:
            if moduleparams["address"] in addresslist.keys():
                if addresslist[moduleparams["address"]] == moduleparams["interface"]:
                    # Already in desired state
                    if DEBUG: print "Specified IP address " + moduleparams["address"] + \
                                    " is already configured at " + addresslist[moduleparams["address"]]
                    exitmessage.append("Specified IP address " + moduleparams["address"] + " is already configured at " + addresslist[moduleparams["address"]])
                    break
                else:
                    if DEBUG: print "Specified IP address " + moduleparams["address"] + \
                                    " is already configured at " + addresslist[moduleparams["address"]]
                    exitmessage.append("Specified IP address " + moduleparams["address"] + " is already configured at " + addresslist[moduleparams["address"]])
                    ansible.fail_json(failed=True, msg=["Configuring IP address failed", exitmessage])

            if moduleparams["interface"] in ipinterfacelist.keys():
                # SET IP address
                commandstr.append("=.id="+ipinterfacelist[moduleparams["interface"]][1])
                response = RosRaw(hostname=hostname, username=username, password=password, port=port,\
                              path="/ip/address/", action="set",\
                              command=commandstr)
                if response["response"][0][0] == "!done":
                    if DEBUG: print "IP address " + moduleparams["address"] + \
                                " was SET by Ansible on interface " + moduleparams["interface"]
                    exitmessage.append("IP address " + moduleparams["address"] + " was SET by Ansible on interface " + moduleparams["interface"])
                    changed = True
                    break
                else:
                    if DEBUG: print "Failed to SET IP address " + moduleparams["address"] + " on " + moduleparams["interface"]
                    exitmessage.append("Failed to SET IP address " + moduleparams["address"] + " on " + moduleparams["interface"])
                    ansible.fail_json(failed=True, msg=exitmessage)


            else:
                # ADD IP interface

                response = RosRaw(hostname=hostname, username=username, password=password, port=port,\
                              path="/ip/address/", action="add", command=commandstr)
                if DEBUG: print "ADD response: " + str(response)
                if response["response"][0][0] == "!done":
                    #Success, added
                    if DEBUG: print "IP address " + moduleparams["address"] + \
                                " was ADDed by Ansible on interface " + moduleparams["interface"]
                    exitmessage.append("IP address " + moduleparams["address"] + " was ADDed by Ansible on interface " + moduleparams["interface"])
                    changed = True
                    break
                else:
                    if DEBUG: print "Failed to ADD IP address " + moduleparams["address"] + " on " + moduleparams["interface"]
                    exitmessage.append("Failed to ADD IP address " + moduleparams["address"] + " on " + moduleparams["interface"])
                    ansible.fail_json(failed=True, msg=[exitmessage, response])

    message = "Already in desired state."
    if changed: message = "Configured to desired state by Ansible."
    ansible.exit_json(failed=False, changed=changed, msg=[message, exitmessage])



from ansible.module_utils.basic import *
main()

File: /Mikrotik_devel\library\mt_ip_pool.py
#!/usr/bin/python
# -*- coding: UTF-8 -*-
# THIS IS ANSIBLE MODULE USED FOR CONFIGUTING MIKROTIK ROUTEROS DEVICES

DOCUMENTATION = '''
---
module: mt_ip_pool
author: Miroslav Hudec
version_added: ""
short_description: Manage Mikrotik Routers
requirements: [ RosAPI ]
description:
    - Manage Mikrotik RouterOS devices.
options:
    hostname:
        required: True
        aliases: ["host"]
        description:
        - Hostname or IP address of Mikrotik device
    username:
        required: True
        aliases: ["user"]
        description:
        - Username used to login to Mikrotik's API
    password:
        required: True
        aliases: ["pass"]
        description:
        - Password used to login to Mikrotik's API


'''

from ansible.module_utils.basic import *

# Import Ansible module parameters
ansible = AnsibleModule(
        argument_spec=dict(
                hostname=dict(required=False, type='str', aliases=["host"]),
                username=dict(required=False, type='str', aliases=["user"]),
                password=dict(required=False, type='str', aliases=["pass"]),
                port=dict(required=False, type='int', default=8728),
                pool_name=dict(required=False, type='str'),
                pool_range=dict(required=False, type='str')

        ),
        supports_check_mode=False,

)


def main():  # main logic

    from ansible.module_utils.RosAPI import API
    # Initialize phase
    # Required parameters

    hostname = ansible.params['hostname']
    username = ansible.params['username']
    password = ansible.params['password']
    port = ansible.params['port']

    # IP pool
    path = "/ip/pool/"
    action = ""
    command = {"name": ansible.params['pool_name'], "ranges": ansible.params['pool_range']}
    response = API(path, action, hostname, username, password, command, port)
    ansible.exit_json(failed=response['failed'], changed=response['changed'], msg=response['msg'])


from ansible.module_utils.basic import *
main()

File: /Mikrotik_devel\library\mt_nat.py
#!/usr/bin/python
# -*- coding: UTF-8 -*-
# THIS IS ANSIBLE MODULE USED FOR CONFIGUTING MIKROTIK ROUTEROS DEVICES

DOCUMENTATION = '''
---
module: mt_nat
author: Miroslav Hudec
version_added: ""
short_description: Manage Mikrotik Routers
requirements: [ RosAPI ]
description:
    - Manage Mikrotik RouterOS devices.
options:
    hostname:
        required: True
        aliases: ["host"]
        description:
        - Hostname or IP address of Mikrotik device
    username:
        required: True
        aliases: ["user"]
        description:
        - Username used to login to Mikrotik's API
    password:
        required: True
        aliases: ["pass"]
        description:
        - Password used to login to Mikrotik's API


'''

from ansible.module_utils.basic import *

# Import Ansible module parameters
ansible = AnsibleModule(
        argument_spec=dict(
                hostname=dict(required=False, type='str', aliases=["host"]),
                username=dict(required=False, type='str', aliases=["user"]),
                password=dict(required=False, type='str', aliases=["pass"]),
                port=dict(required=False, type='int', default=8728),
                out_interface=dict(required=False, type='str'),
                chain=dict(required=True, type='str', choices=["srcnat", "dstnat"]),
                disabled=dict(required=False, type='str', choices=["true", "false"]),
                comment=dict(required=False, type='str'),
                action=dict(required=True, type='str', choices=["masquerade", "dst-nat"]),
                dst_port=dict(required=False, type='str'),
                dst_address=dict(required=False, type='str'),
                to_addresses=dict(required=False, type='str'),
                protocol=dict(required=False, type='str', choices=["tcp", "udp"]),
                to_ports=dict(required=False, type='str')

        ),
        supports_check_mode=False,

)


def main():  # main logic

    from ansible.module_utils.RosAPI import API
    # Initialize phase
    # Required parameters

    hostname = ansible.params['hostname']
    username = ansible.params['username']
    password = ansible.params['password']
    port = ansible.params['port']

    while True:

        # DHCP Server
        path = "/ip/firewall/nat/"
        action = ""
        # Required params
        command = {"action": ansible.params['action'], "chain": ansible.params['chain']}
        # Optional params
        if ("disabled" in ansible.params.keys()) and (ansible.params['disabled'] != None):
            command["disabled"] = ansible.params['disabled']
        if ("comment" in ansible.params.keys()) and (ansible.params['comment'] != None):
            command["comment"] = ansible.params['comment']
        if ("out_interface" in ansible.params.keys()) and (ansible.params['out_interface'] != None):
            command["out-interface"] = ansible.params['out_interface']
        if ("to_addresses" in ansible.params.keys()) and (ansible.params['to_addresses'] != None):
            command["to-addresses"] = ansible.params['to_addresses']
        if ("protocol" in ansible.params.keys()) and (ansible.params['protocol'] != None):
            command["protocol"] = ansible.params['protocol']
        if ("to_ports" in ansible.params.keys()) and (ansible.params['to_ports'] != None):
            command["to-ports"] = ansible.params['to_ports']
        if ("dst_address" in ansible.params.keys()) and (ansible.params['dst_address'] != None):
            command["dst-address"] = ansible.params['dst_address']
        if ("dst_port" in ansible.params.keys()) and (ansible.params['dst_port'] != None):
            command["dst-port"] = ansible.params['dst_port']


        # Let RosAPI do the rest
        response = API(path, action, hostname, username, password, command=command, port=port)
        ansible.exit_json(failed=response['failed'], changed=response['changed'], msg=response['msg'])



from ansible.module_utils.basic import *
main()

File: /Mikrotik_devel\library\mt_nat2.py
#!/usr/bin/python
# -*- coding: UTF-8 -*-


DOCUMENTATION = '''
---
module: mt_ip
author: Miroslav Hudec
version_added: ""
short_description: Sets IP addresses on Mikrotik's interfaces
requirements: [ RosAPI ]
description:
    - Sets IP addresses on Mikrotik's interfaces
options:
    hostname:
        required: True
        aliases: ["host"]
        description:
        - Hostname or IP address of Mikrotik device
    username:
        required: True
        aliases: ["user"]
        description:
        - Username used to login to Mikrotik's API
    password:
        required: True
        aliases: ["pass"]
        description:
        - Password used to login to Mikrotik's API
    address:
        required: True
        aliases: ["ip", "addr"]
    interface:
        aliases: ["int"]
        required: True
    disabled:
        required: True
        choices: ['yes', 'no']

'''

from ansible.module_utils.basic import *
from ansible.module_utils.RosAPI import *




# Import Ansible module parameters
ansible = AnsibleModule(
        argument_spec=dict(
                hostname=dict(required=False, type='str', aliases=["host"]),
                username=dict(required=False, type='str', aliases=["user"]),
                password=dict(required=False, type='str', aliases=["pass"]),
                port=dict(required=False, type='int', default=8728),
                out_interface=dict(required=False, type='str'),
                chain=dict(required=True, type='str', choices=["srcnat", "dstnat"]),
                disabled=dict(required=False, type='str', choices=["true", "false"]),
                comment=dict(required=False, type='str'),
                action=dict(required=True, type='str', choices=["masquerade", "dst-nat"]),
                dst_port=dict(required=False, type='str'),
                dst_address=dict(required=False, type='str'),
                to_addresses=dict(required=False, type='str'),
                protocol=dict(required=False, type='str', choices=["tcp", "udp"]),
                to_ports=dict(required=False, type='str')

        ),
        supports_check_mode=False,

)



"""
# Debugging Section
class AnsibleModule:  # Provides Ansible-like parameters
    params = {"username": "admin", "hostname": "192.168.116.100", "password": "", "port": 8728,\
              "chain": "dstnat",  "action": "dst-nat", "comment": "SSH", "dst-port": 2022,\
            "to-addresses": "192.168.200.112", "to-ports": 22, "protocol": "tcp"}

ansible = AnsibleModule

"""

# Global Variables
privkeys = ["hostname", "username", "password", "port", "path", "action"]
# Initialize phase
# Required parameters
hostname = ansible.params['hostname']
username = ansible.params['username']
password = ansible.params['password']
port = ansible.params['port']
DEBUG = False  # This is only for debugging, if set to True Ansible will crash
moduleparams = digestArgs(ansible.params)
exitmessage = []
changed = False


def main():

    command = {}
    for key in moduleparams:
        if key not in privkeys:
            command[key] = moduleparams[key]

    response = API(hostname=hostname, username=username, password=password, port=port,\
                   path="/ip/firewall/nat/", command=command, DEBUG=DEBUG)
    if DEBUG: print response
    ansible.exit_json(failed=response["failed"], changed=response["changed"], msg=response["msg"])

from ansible.module_utils.basic import *
if __name__ == '__main__':
    main()

File: /Mikrotik_devel\library\mt_raw.py
#!/usr/bin/python
# -*- coding: utf-8 -*-
#
#

DOCUMENTATION = '''
---
module: mt_raw
author: Miroslav Hudec
version_added: ""
short_description: Sets information provided by DHCP server
requirements: [ RosAPI ]
description:
    - Sets information provided by DHCP server, such as default gateway, DNS servers, domain name etc...
options:
    hostname:
        required: True
        aliases: ["host"]
        description:
        - Hostname or IP address of Mikrotik device
    username:
        required: True
        aliases: ["user"]
        description:
        - Username used to login to Mikrotik's API
    password:
        required: True
        aliases: ["pass"]
        description:
        - Password used to login to Mikrotik's API
    port:
        required: False
        description:
        - Port used to connect to MikroTik's API, default 8728


'''






from ansible.module_utils.basic import *
from ansible.module_utils.RosRaw import *
from ansible.module_utils.RosAPI import *

# Import Ansible module parameters
ansible = AnsibleModule(
        argument_spec=dict(
                hostname=dict(required=False, type='str', aliases=["host"]),
                username=dict(required=False, type='str', aliases=["user"]),
                password=dict(required=False, type='str', aliases=["pass"]),
                port=dict(required=False, type='int', default=8728),
                path=dict(required=True, type='str'),
                action=dict(required=True, type='str', ),
                command=dict(required=False, type='list'),
                query=dict(required=False, type='str'),

        ),
        supports_check_mode=False,

)
"""

# Debugging Section
class AnsibleModule:
    params = {"username": "admin", "hostname": "192.168.116.100", "password": "", "port": 8728, \
              "command": [], "path": "/system/", "action": "reboot"}


ansible = AnsibleModule
"""


# Global Variables
privkeys = ["hostname", "username", "password", "port", "path", "action"]
# Initialize phase
# Required parameters
hostname = ansible.params['hostname']
username = ansible.params['username']
password = ansible.params['password']
port = ansible.params['port']
DEBUG = False # This is only for debugging, if set to True Ansible will crash
switch = True  # Glabal switch

def main():  # main logic

    # Initialize phase
    # Required parameters
    privkeys = ["hostname", "username", "password", "port", "path", "action"]
    command = []
    path = ansible.params["path"]
    action = ansible.params["action"]
    while True:
        if ansible.params["command"] is not None:

            for item in ansible.params["command"]:
                command.append("=" + item)



        response = RosRaw(path, action, hostname, username, password, command=command, port=port, DEBUG=DEBUG)
        creply = replyCheck(response)
        if not creply["success"]:
            ansible.fail_json(failed=True, changed=False, msg=str(response))
        else:
            ansible.exit_json(failed=False, changed=True, msg=str(response))


from ansible.module_utils.basic import *

main()


File: /Mikrotik_devel\library\mt_rip.py
#!/usr/bin/python
# -*- coding: UTF-8 -*-
# THIS IS ANSIBLE MODULE USED FOR CONFIGUTING MIKROTIK ROUTEROS DEVICES

DOCUMENTATION = '''
---
module: mt_rip
author: Miroslav Hudec
version_added: ""
short_description: Manage Mikrotik Routers
requirements: [ RosAPI ]
description:
    - Manage Mikrotik RouterOS devices.
options:
    hostname:
        required: True
        aliases: ["host"]
        description:
        - Hostname or IP address of Mikrotik device
    username:
        required: True
        aliases: ["user"]
        description:
        - Username used to login to Mikrotik's API
    password:
        required: True
        aliases: ["pass"]
        description:
        - Password used to login to Mikrotik's API


'''

from ansible.module_utils.basic import *
from ansible.module_utils.RosAPI import *
from ansible.module_utils.RosRaw import *


# Import Ansible module parameters
ansible = AnsibleModule(
        argument_spec=dict(
                hostname=dict(required=False, type='str', aliases=["host"]),
                username=dict(required=False, type='str', aliases=["user"]),
                password=dict(required=False, type='str', aliases=["pass"]),
                port=dict(required=False, type='int', default=8728),
                distribute_default=dict(required=False, type='str', choices=["always", "never", "if-installed"]),
                redistribute_static=dict(required=False, type='str', choices=["true", "false"]),
                redistribute_connected=dict(required=False, type='str', choices=["true", "false"]),
                redistribute_ospf=dict(required=False, type='str', choices=["true", "false"]),
                redistribute_bgp=dict(required=False, type='str', choices=["true", "false"]),
                metric_default=dict(required=False, type='int'),
                metric_static=dict(required=False, type='int'),
                metric_connected=dict(required=False, type='int'),
                metric_ospf=dict(required=False, type='int'),
                metric_bgp=dict(required=False, type='int'),
                timeout_timer=dict(required=False, type='str'),
                garbage_timer=dict(required=False, type='str'),
                update_timer=dict(required=False, type='str'),
                networks=dict(required=False, type='list'),
                interfaces=dict(required=False, type='list'),
                send=dict(required=False, type='str', choices=["v1", "v1-2", "v2"]),
                receive=dict(required=False, type='str', choices=["v1", "v1-2", "v2"]),
                authentication=dict(required=False, type='str', choices=["none", "md5", "simple"]),
                authentication_key=dict(required=False, type='str'),
                comment=dict(required=False, type='str'),
                disabled=dict(required=False, type='str', choices=["true", "false"]),
                passive=dict(required=False, type='str', choices=["true", "false"]),


        ),

        supports_check_mode=False,

)
"""


# Debugging Section
class AnsibleModule:
    params = {"username": "admin", "hostname": "192.168.116.100", "password": "", \
              "interfaces": ["ether1", "ether2"], "networks": ["192.168.116.0/24"], \
              "send": "v2", "receive": "v2", "authentication": "md5", "authentication_key": "mikrotik", "port": 8728}


ansible = AnsibleModule
"""
# Global Variables
privkeys = ["hostname", "username", "password", "port", "path", "action"]
# Initialize phase
# Required parameters
hostname = ansible.params['hostname']
username = ansible.params['username']
password = ansible.params['password']
port = ansible.params['port']
DEBUG = False # This is only for debugging, if set to True Ansible will crash
switch = True  # Glabal switch


def toRawCommand(params):
    rawcmd = []
    for key in params.keys():
        if (key not in privkeys) and (params[key] is not None):
            rawcmd.append("=" + digestArg(key) + "=" + str(params[key]))



def main():  # main logic



    while True:

        path = "/routing/rip/"
        action = "set"
        changed = False
        # Required params
        privkeys = ["hostname", "username", "password", "port", "path", "action"]

        # Commands for RIP global setup
        ripglparams = ["distribute_default", "redistribute_static", "redistribute_connected", "redistribute_ospf", \
                       "redistribute_bgp", "metric_static", "metric_connected", "metric_ospf", "metric_bgp", ""]
        switch = False
        for key in ansible.params.keys():  # Determine if this section should be configured
            if key in ripglparams: switch = True

        if DEBUG:
            if switch:
                print "RIP global setup will now be checked..."
            else:
                print "No arguments for RIP global setup, skipping..."

        if switch:
            ripcmd = {}
            for key in ansible.params.keys():
                if (key not in privkeys) and (key in ripglparams) and (ansible.params[key] is not None):
                    ripcmd[digestArg(key)] = str(ansible.params[key])

            if len(ripcmd) > 0:
                response = API(path, action, hostname, username, password, command=ripcmd, port=port)
                if response['failed']:
                    ansible.fail_json(failed=True, msg="Failed to set RIP global parameters.")
                    if DEBUG: print "Failed to set RIP global parameters."
                if response["changed"] or changed: changed = True
                if DEBUG:
                    if response["changed"]:
                        print "Global RIP configuration has been changed."
                    else:
                        print "Global RIP configuration is already in desired state."

        # Commands for RIP Network setup
        if ansible.params["networks"] is not None:
            if DEBUG: print "RIP network setup will now be checked..."
            path = "/routing/rip/network/"
            action = "add"
            for network in ansible.params["networks"]:
                ripnetcmd = {"network": network}
                response = API(path, action, hostname, username, password, command=ripnetcmd, port=port)
                if response['failed']:
                    ansible.fail_json(failed=True, msg="Failed to add RIP network.")
                    if DEBUG: print "Failed to add RIP network."
                elif DEBUG:
                    if response["changed"]:
                        print "RIP Network added."
                    else:
                        print "RIP network already configured..."

                if response["changed"] or changed: changed = True

        else:
            print "No arguments for RIP network setup, skipping..."

        # Command for RIP interface setup
        ripintparams = ["send", "receive", "authentication", "authentication_key", \
                        "comment", "disabled", "passive"]

        switch = False
        for key in ansible.params.keys():  # Determine if this section should be configured
            if key in ripintparams: switch = True
        if DEBUG:
            if switch:
                print "RIP interface setup will now be checked..."
            else:
                print "No arguments for RIP interface setup, skipping..."
        # Separate sentence for each interface:

        if ansible.params["interfaces"] is not None:
            # Execute call for each interface
            proplist = []
            ripintcmd = []
            for key in ansible.params.keys():
                if (key not in privkeys) and (key in ripintparams) and (ansible.params[key] is not None):
                    ripintcmd.append("=" + digestArg(key) + "=" + str(ansible.params[key]))
                    proplist.append(digestArg(key))
            if DEBUG: print ripintcmd

            for interface in ansible.params["interfaces"]:
                ripintcmdfull = ripintcmd[:]
                ripintcmdfull.append("=interface=" + interface)

                response = RosRaw("/routing/rip/interface/", "add", hostname, username, password, command=ripintcmdfull,
                                  port=port)
                if DEBUG: print "Interface " + interface + " response: " + str(response)
                if response["response"][0][0] == "!trap":
                    if response["response"][0][1]["=message"] == "failure: only one config per interface allowed":
                        if DEBUG: print "Interface " + interface + " exists, checking it's configuration..."
                        # This means that interface exists, but might not be configured in desired way
                        # Time to do print and check
                        propstr = ""
                        isSame = True
                        for prop in proplist:  # Build proplist
                            propstr = propstr + prop + ","
                        propstr = propstr + ".id"
                        response = RosRaw("/routing/rip/interface/", "print", hostname, username, password, \
                                          command=['?interface=' + interface, '=.proplist=' + propstr], port=port)
                        response = stripResponse(response["response"][:-1][0][1])
                        if DEBUG: print response
                        id = response[".id"]
                        for prop in proplist:
                            if ansible.params[digestArg(prop, True)] != response[prop]:
                                isSame = False
                        if not isSame:
                            if DEBUG: print "Interface " + interface + " has different configuration, using SET..."
                            changed = True
                            ripintcmdfull = ripintcmd[:]
                            ripintcmdfull.append("=.id=" + id)
                            response = RosRaw("/routing/rip/interface/", "set", \
                                              hostname, username, password, command=ripintcmdfull, port=port)
                            if DEBUG: print response
                        else:
                            if DEBUG: print "Interface " + interface + " is already in desired state"





                    else:
                        if DEBUG: print "Unhandled exception, configuring interface " + interface + " failed."
                        ansible.fail_json(failed=True, msg="Failed to setup RIP interface.")
                elif response["response"][0][0] == "!done":
                    # This means interface was succefully added
                    changed = True

        message = "Already in desired state."
        if changed: message = "Configured to desired state by Ansible."

        ansible.exit_json(failed=False, changed=changed, msg=message)


from ansible.module_utils.basic import *

main()


File: /Mikrotik_devel\library\mt_static_route.py
#!/usr/bin/python
# -*- coding: UTF-8 -*-
# THIS IS ANSIBLE MODULE USED FOR CONFIGUTING MIKROTIK ROUTEROS DEVICES

DOCUMENTATION = '''
---
module: mt_static_route
author: Miroslav Hudec
version_added: ""
short_description: Manage Mikrotik Routers
requirements: [ RosAPI ]
description:
    - Manage Mikrotik RouterOS devices.
options:
    hostname:
        required: True
        aliases: ["host"]
        description:
        - Hostname or IP address of Mikrotik device
    username:
        required: True
        aliases: ["user"]
        description:
        - Username used to login to Mikrotik's API
    password:
        required: True
        aliases: ["pass"]
        description:
        - Password used to login to Mikrotik's API


'''

from ansible.module_utils.basic import *

# Import Ansible module parameters
ansible = AnsibleModule(
        argument_spec=dict(
                hostname=dict(required=False, type='str', aliases=["host"]),
                username=dict(required=False, type='str', aliases=["user"]),
                password=dict(required=False, type='str', aliases=["pass"]),
                port=dict(required=False, type='int', default=8728),
                dst_address=dict(required=True, type='str'),
                gateway=dict(required=True, type='str'),
                disabled=dict(required=False, type='str', choices=["true", "false"]),
                comment=dict(required=False, type='str'),

        ),
        supports_check_mode=False,

)


def main():  # main logic

    from ansible.module_utils.RosAPI import API
    # Initialize phase
    # Required parameters

    hostname = ansible.params['hostname']
    username = ansible.params['username']
    password = ansible.params['password']
    port = ansible.params['port']

    while True:

        # DHCP Server
        path = "/ip/route/"
        action = ""

        command = {}

        if ("dst_address" in ansible.params.keys()) and (ansible.params['dst_address'] != None):
            command["dst-address"] = ansible.params['dst_address']
        if ("gateway" in ansible.params.keys()) and (ansible.params['gateway'] != None):
            command["gateway"] = ansible.params['gateway']


        # Let RosAPI do the rest
        response = API(path, action, hostname, username, password, command=command, port=port)
        ansible.exit_json(failed=response['failed'], changed=response['changed'], msg=response['msg'])



from ansible.module_utils.basic import *
main()

File: /Mikrotik_devel\library\RosAPI.py
#!/usr/bin/python
# -*- coding: utf-8 -*-
#
#
from ansible.module_utils.RosCore import *


class Auth:

    def __init__(self, host, hostsfile="/etc/ansible/hosts", DEBUG=False):
        hostsfile = open(hostsfile, mode='r')
        DEBUG = False
        # Determine number of lines in the file
        num_lines = sum(1 for line in hostsfile)
        if DEBUG: print num_lines
        hostsfile.seek(0)


        hostsdict = {}
        # Create dictionary from file lines
        for i in range(0, num_lines):
            workline = hostsfile.readline()
            if DEBUG: print workline
            # If line isn't empty
            if workline and workline[0] != '[':

                linearray = workline.split(' ')
                if DEBUG: print linearray
                linedict = dict(host=linearray[0].strip())
                linearray.remove(linearray[0])
                for i in range(0, len(linearray)):
                    if DEBUG: print linearray[i].split('=')
                    linedict[linearray[i].split('=')[0].strip()] = linearray[i].split('=')[1].strip()
                    hostsdict[linedict['host']] = linedict

                if DEBUG: print linedict
                if host in hostsdict.keys():
                    if 'hostname' in hostsdict[host].keys():
                        self.hostname = hostsdict[host]['hostname']
                    if 'username' in hostsdict[host].keys():
                        self.username = hostsdict[host]['username']
                    if 'password' in hostsdict[host].keys():
                        self.password = hostsdict[host]['password']

def changeCheck(response, command, DEBUG=False):
    priv_params = ["name", "comment"]
    while True:
        r = {"exists": "", "isSame": True}
        decision = []
        if len(response) > 1:
            decision = [0] * (len(response) - 1)
            # Decide which response has most common arguments
            for i in range(0, len(decision), 1):
                for key in command.keys():
                    if str("=" + key) in response[i][1].keys():
                        if (command[key] == response[i][1]["=" + key]):
                            decision[i] += 1
                            if key in priv_params:
                                decision[i] += 9

            if DEBUG == True: print decision, response

        elif len(response) == 1:
            r["exists"] = False
            r["isSame"] = False
            return r

        """Check if object with most common values is truly unique, otherwise
          object does not yet exist and will be created with ADD"""
        # If there is more than 1 object
        if len(decision) > 1:

            if sorted(decision)[-1] > sorted(decision)[-2]:
                r["exists"] = True
                # Get ID of object with most common values for SET option
                r["id"] = response[decision.index(max(decision))][1]["=.id"]
            else:
                r["exists"] = False
        # If there are no objects
        # If there is exactly 1 object
        elif len(decision) == 1:
            if decision[0] == 0:
                r["exists"] = False
            else:
                r["exists"] = True

            if "=.id" in response[0][1].keys():
                r["id"] = response[0][1]["=.id"]

        """If at least one value doesn't match command, it is NOT the same
         - we'll either ADD new or SET existing to match all values """
        for key in command.keys():
            if str("=" + key) in response[decision.index(max(decision))][1].keys():
                if command[key] != response[decision.index(max(decision))][1]["=" + key]:
                    r["isSame"] = False

        return r

def replyCheck(r):
    reply = {"success": True}
    for i in range(0,len(r)-1):
        if r[i][0] == "!trap":
            if '=message' in r[i][1].keys():
                reply["message"] = r[i][1]['=message']
            reply["success"] = False
            break
    return reply

def intCheck(interface_name, hostname, username, password, port=8728):
    # Checks if desired interface exists

    while True:
        # Check if interface exists
        response = API("/interface/", "print", hostname, username=username, password=password)

        if response["msg"] == "Login failed":
            return {"msg": "Login Failed", "Exists": "Unknown"}

        interfaces = [0] * (len(response["response"]) - 1)

        for i in range(0, len(interfaces)):
            interfaces[i] = response["response"][i][1]["=name"]

        if interface_name in interfaces:
            interfaceExists = True
            return {"msg": "Interface with specified name exists.", "Exists": True}

        else:
            interfaceExists = False
            return {"msg": "Interface with specified name does not exists.", "Exists": False}


def digestArg(argument, backwards=False):
    l = list(argument)
    if backwards:
        # Hyphens to underscores
        for i in range(0, len(argument) - 1):
            if l[i] == "-":  # Find
                l[i] = "_"  # Replace with
    else:
        # Underscores to hyphens
        for i in range(0, len(argument) - 1):
            if l[i] == "_":  # Find
                l[i] = "-"  # Replace with
    newarg = "".join(l)
    return newarg

def digestArgs(arguments):
    newargs = {}
    for key in arguments.keys():
        if arguments[key] is not None:
            newargs[digestArg(key)] = arguments[key]
    return newargs

def digestResponse(response):
    newresponse = {}
    if len(response) > 1:
        response = response[:-1]
        for i in range(0, len(response)):
            newresponse[i] = {}
            for key in response[i][1].keys():
                newresponse[i][key[1:]] = response[i][1][key]
        return newresponse
    return "noObjects"

def stripResponse(response):
    strippedresponse = {}
    for key in response.keys():
        strippedresponse[key[1:]] = response[key]
    return strippedresponse

def API(path, action, hostname="", username="admin", password="", command=None, port=8728, DEBUG=False):
    changed = False
    lst = []

    while True:

        # Connect
        mikrotik = Core(hostname, DEBUG=DEBUG)
        login = mikrotik.login(username, password)
        # Check if login is correct
        if login[0][0] == '!trap':
            if DEBUG == True:
                print login

            return {"failed": True, "changed": False, "msg": "Login failed"}

        else:
            if DEBUG == True:
                print login



        response = mikrotik.talk([path + "print"])
        if DEBUG == True: print response



        if action == "print":
            return {"failed": False, "changed": changed, "msg": "No changes were made", "response": response, "isSame": None}

        r = changeCheck(response, command, DEBUG=DEBUG)
        if r["isSame"]:
            mikrotik.close_connection()
            return {"failed": False, "changed": changed, "msg": "Already in desired state."}

        else:
            # In case that similar object already exists
            if r["exists"] == True:

                # Create list for arguments
                if "id" in r.keys():
                    namematch = True
                    if "name" in command.keys():
                        for i in range(0, len(response)-1):
                            if response[i][1]["=.id"] == r["id"]:
                                namematch = (command["name"] == response[i][1]["=name"])

                                break
                        if namematch:
                            lst = [path + "set", "=.id=" + r["id"]]
                        else:
                            lst = [path + "add"]
                        del command["name"]
                    else:
                        lst = [path + "set", "=.id=" + r["id"]]
                else:
                    lst = [path + "set"]

            # In case there's no similar object
            elif r["exists"] == False:
                # Create list for arguments
                # Allow force set by module
                if action == "set":
                    lst = [path + "set"]
                else:
                    lst = [path + "add"]


        # Add commands to argument string
        for key in command.keys():
            lst.append("=" + key + "=" + str(command[key]))




        # Apply changes
        mikrotik.talk(lst)
        # Check if changes were actually applied
        if changeCheck(mikrotik.talk([path + "print"]), command, DEBUG=DEBUG)["isSame"]:
            changed = True

            mikrotik.close_connection()
            return {"failed": False, "changed": changed, "msg": "Configured to desired state by Ansible"}

        else:
            mikrotik.close_connection()
            return {"failed": True, "changed": changed, "msg": "Something went wrong..."}



File: /Mikrotik_devel\library\RosAPI2.py
#!/bin/usr/python
from ansible.module_utils.RosCore import *

# Global Variables
privkeys = ["hostname", "username", "password", "port" "path"]
# Initialize phase
# Required parameters
hostname = "192.168.116.100"
username = "admin"
password = ""
port = 8728
DEBUG = False  # This is only for debugging, if set to True Ansible will crash
switch = True  # Global switch

def API(path="/", action=None, hostname="", username="admin", password="", command=None, port=8728, DEBUG=DEBUG):

    while True:
        failed = False
        changed = True
        sentence = [path + "print"]
        reply = {"failed": False, "changed": False, "msg": []}
        exitmsg = []
        info = ""




        # Connect
        mikrotik = Core(hostname, DEBUG=DEBUG)
        login = mikrotik.login(username, password)
        # Check if login is correct
        if login[0][0] == '!trap':
            if DEBUG: print login

            return {"failed": True, "changed": False, "msg": "Login failed"}

        else:
            if DEBUG: print login

        # Create command, proplist and propstring
        rawcommand = []
        proplist = []
        propstr = ""
        if (command is not None) and (len(command) > 0):
            for key in command.keys():
                if key not in privkeys:
                    rawcommand.append("="+key+"="+str(command[key]))
                    proplist.append(key)
                    propstr = propstr + key + ","
            propstr = propstr + ".id"

        if DEBUG: print "Rawcommand: "+str(rawcommand)+" \nProplist: "+str(proplist)+" \nPropstr: "+propstr
        printsentence = sentence[:]
        printsentence.append("=.proplist="+propstr)
        if DEBUG: print "Printsentence: "+str(printsentence)
        # Get response
        response = mikrotik.talk(printsentence)
        if DEBUG: print "PRINT response: "+str(response)
        response = digestResponse(response)
        if DEBUG: print "Digested PRINT response: "+str(response)
        if response != "noObjects":

            common = commonParams(response, command)
            if DEBUG: print "Common: "+ str(common)

            # Decide if SET or add
            if common["max"]["hasmax"]:
                maxno = common["max"]["maxno"]
                maxpos = common["max"]["maxpos"]
                if maxno == len(command):
                    # All specified attributes match, do nothing
                    info = "All desired atributes are already present."

                    reply["failed"] = False
                    reply["changed"] = False
                    reply["msg"].append(info)


                    if DEBUG: print info
                    exitmsg.append(info)
                    if DEBUG: print reply
                    mikrotik.close_connection()
                    return reply

                else:
                    # Some atributes are incorrect, use SET
                    if ("comment" in proplist):

                        if ("comment" in response[maxpos].keys()):

                            if (response[maxpos]["comment"] == command["comment"]):
                                # Comments match, use SET ID
                                id = common["max"]["maxid"]
                                action = "set"
                                sentence = [path + action, "=.id="+id]
                                # Has ID use set with ID
                                info = "Maximum with ID and matching comment exists, using SET ID..."
                                if DEBUG: print info
                                exitmsg.append(info)

                                reply["failed"] = False
                                reply["changed"] = True
                                reply["msg"].append(info)

                            else:
                                # Comments don't match, use ADD
                                action = "add"
                                info = "Comments don't match, using ADD..."
                                if DEBUG: print info
                                exitmsg.append(info)
                                sentence = [path + action]

                                reply["failed"] = False
                                reply["changed"] = True
                                reply["msg"].append(info)
                        else:
                            # Exists, but has no ID. Use SET without ID
                            action = "set"
                            sentence = [path + action]
                            info = "Maximum exists without comment, using SET..."
                            if DEBUG: print info
                            exitmsg.append(info)

                            reply["failed"] = False
                            reply["changed"] = True
                            reply["msg"].append(info)
                    else:
                        # No comment in proplist
                        if maxno == len(command):
                            info = "Already in desired state."
                            if DEBUG: print info
                            exitmsg.append(info)
                            reply["changed"] = False
                            reply["msg"] = exitmsg
                            reply["failed"] = False
                            return reply
                        else:
                            action = "set"
                            info = "No comment supplied, found max, using SET." + str(response) + str(common) + str(command)
                            reply["changed"] = True
                            exitmsg.append(info)
                            reply["msg"] = exitmsg
                            if DEBUG: print info





            else:
                if len(response) >= 1:
                    if ".id" in response[0].keys():
                        action = "add"
                        info = "Maximum does not exist, using ADD..."
                    else:
                        action = "set"
                        info = "Object wit no ID, using SET..."
                reply["changed"] = True
                if DEBUG: print info
                exitmsg.append(info)
                sentence = [path + action]

                reply["failed"] = False
                reply["changed"] = True
                reply["msg"].append(info)
        else:
            # No objects exist, use ADD
            action = "add"
            info = "No objects exist, using ADD..."
            if DEBUG: print info
            exitmsg.append(info)
            sentence = [path + action]

            reply["failed"] = False
            reply["changed"] = True
            reply["msg"].append(info)



        sentence = [path + action]
        if DEBUG: print "Sentence: " + str(sentence)
        if DEBUG: print rawcommand

        for item in rawcommand:
            sentence.append(item)
        if DEBUG: print "Full sentence: " + str(sentence)
        response = mikrotik.talk(sentence)
        if DEBUG: print "Response: "+str(response)
        if response[0][0] == "!done":
            reply["failed"] = False
        else:
            reply["failed"] = True
        if DEBUG: print reply
        mikrotik.close_connection()
        return reply















def digestResponse(response):
    newresponse = {}
    if len(response) > 1:
        response = response[:-1]
        for i in range(0, len(response)):
            newresponse[i] = {}
            for key in response[i][1].keys():
                newresponse[i][key[1:]] = response[i][1][key]
        return newresponse
    return "noObjects"

def commonParams(digresponse, command):

    common = {}
    num = 0
    for i in range(0, len(digresponse)):
        for key in command.keys():
            if (key in digresponse[i].keys()) and (str(command[key]) == digresponse[i][key]):
                num += 1
        common[i] = num
        num = 0
    maxi = {"hasmax": True}
    maximum = []
    for j in range(0, len(common)):
        maximum.append(common[j])


    if maximum.count(max(maximum)) != 1:
        # Has no true maximum
        maxi["hasmax"] = False
    elif maximum.count(max(maximum)) == 1:
        maxi["hasmax"] = True
        maxi["maxno"] = max(maximum)
        maxi["maxpos"] = maximum.index(max(maximum))
        if ".id" in digresponse[maxi["maxpos"]].keys():
            maxi["maxid"] = digresponse[maxi["maxpos"]][".id"]
        if maxi["maxno"] == 0:
            maxi["hasmax"] = False

    common["max"] = maxi
    return common

def digestArg(argument, backwards=False):
    l = list(argument)
    if backwards:
        # Hyphens to underscores
        for i in range(0, len(argument) - 1):
            if l[i] == "-":  # Find
                l[i] = "_"  # Replace with
    else:
        # Underscores to hyphens
        for i in range(0, len(argument) - 1):
            if l[i] == "_":  # Find
                l[i] = "-"  # Replace with
    newarg = "".join(l)
    return newarg

def digestArgs(arguments):
    newargs = {}
    for key in arguments.keys():
        if arguments[key] is not None:
            newargs[digestArg(key)] = arguments[key]
    return newargs

def stripResponse(response):
    strippedresponse = {}
    for key in response.keys():
        strippedresponse[key[1:]] = response[key]
    return strippedresponse



if __name__ == '__main__':

    path = "/ip/pool/"
    command = {"ranges": "192.168.100.1-192.168.100.100", "name": "pool1"}

    API(path=path, command=command, hostname=hostname)

File: /Mikrotik_devel\library\RosCore.py
#!/usr/bin/python
# -*- coding: utf-8 -*-
#
#


class Core:
    """Core part of Router OS API It contains methods necessary to extract raw data from the router.
    If object is instanced with DEBUG = True parameter, it runs in verbosity mode.
    Core part is taken mostly from http://wiki.mikrotik.com/wiki/Manual:API#Example_client."""

    def __init__(self, hostname, port=8728, DEBUG=False):
        import socket
        self.DEBUG = DEBUG
        self.hostname = hostname
        self.port = port
        self.currenttag = 0
        self.sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sk.settimeout(5)
        self.sk.connect((self.hostname, self.port))

    def login(self, username, pwd):
        import binascii
        from hashlib import md5

        for repl, attrs in self.talk(["/login"]):
            chal = binascii.unhexlify(attrs['=ret'])
        md = md5()
        md.update('\x00')
        md.update(pwd)
        md.update(chal)
        r = self.talk(["/login", "=name=" + username, "=response=00" + binascii.hexlify(md.digest())])
        return r

    def talk(self, words):
        if self.writeSentence(words) == 0: return
        r = []
        while 1:
            i = self.readSentence()
            if len(i) == 0: continue
            reply = i[0]
            attrs = {}
            for w in i[1:]:
                j = w.find('=', 1)
                if (j == -1):
                    attrs[w] = ''
                else:
                    attrs[w[:j]] = w[j + 1:]
            r.append((reply, attrs))
            if reply == '!done': return r

    def writeSentence(self, words):
        ret = 0
        for w in words:
            self.writeWord(w)
            ret += 1
        self.writeWord('')
        return ret

    def readSentence(self):
        r = []
        while 1:
            w = self.readWord()
            if w == '':
                return r
            r.append(w)

    def writeWord(self, w):
        if self.DEBUG:
            print "<<< " + w
        self.writeLen(len(w))
        self.writeStr(w)

    def readWord(self):
        ret = self.readStr(self.readLen())
        if self.DEBUG:
            print ">>> " + ret
        return ret

    def writeLen(self, l):
        if l < 0x80:
            self.writeStr(chr(l))
        elif l < 0x4000:
            l |= 0x8000
            self.writeStr(chr((l >> 8) & 0xFF))
            self.writeStr(chr(l & 0xFF))
        elif l < 0x200000:
            l |= 0xC00000
            self.writeStr(chr((l >> 16) & 0xFF))
            self.writeStr(chr((l >> 8) & 0xFF))
            self.writeStr(chr(l & 0xFF))
        elif l < 0x10000000:
            l |= 0xE0000000
            self.writeStr(chr((l >> 24) & 0xFF))
            self.writeStr(chr((l >> 16) & 0xFF))
            self.writeStr(chr((l >> 8) & 0xFF))
            self.writeStr(chr(l & 0xFF))
        else:
            self.writeStr(chr(0xF0))
            self.writeStr(chr((l >> 24) & 0xFF))
            self.writeStr(chr((l >> 16) & 0xFF))
            self.writeStr(chr((l >> 8) & 0xFF))
            self.writeStr(chr(l & 0xFF))

    def readLen(self):
        c = ord(self.readStr(1))
        if (c & 0x80) == 0x00:
            pass
        elif (c & 0xC0) == 0x80:
            c &= ~0xC0
            c <<= 8
            c += ord(self.readStr(1))
        elif (c & 0xE0) == 0xC0:
            c &= ~0xE0
            c <<= 8
            c += ord(self.readStr(1))
            c <<= 8
            c += ord(self.readStr(1))
        elif (c & 0xF0) == 0xE0:
            c &= ~0xF0
            c <<= 8
            c += ord(self.readStr(1))
            c <<= 8
            c += ord(self.readStr(1))
            c <<= 8
            c += ord(self.readStr(1))
        elif (c & 0xF8) == 0xF0:
            c = ord(self.readStr(1))
            c <<= 8
            c += ord(self.readStr(1))
            c <<= 8
            c += ord(self.readStr(1))
            c <<= 8
            c += ord(self.readStr(1))
        return c

    def writeStr(self, str):
        n = 0;
        while n < len(str):
            r = self.sk.send(str[n:])
            if r == 0: raise RuntimeError, "connection closed by remote end"
            n += r

    def readStr(self, length):
        ret = ''
        while len(ret) < length:
            s = self.sk.recv(length - len(ret))
            if s == '': raise RuntimeError, "connection closed by remote end"
            ret += s
        return ret

    def response_handler(self, response):
        """Handles API response and remove unnessesary data"""

        # if respons end up successfully
        if response[-1][0] == "!done":
            r = []
            # for each returned element
            for elem in response[:-1]:
                # if response is valid Mikrotik returns !re, if error !trap
                # before each valid element, there is !re
                if elem[0] == "!re":
                    # take whole dictionary of single element
                    element = elem[1]
                    # with this loop we strip equals in front of each keyword
                    for att in element.keys():
                        element[att[1:]] = element[att]
                        element.pop(att)
                    # collect modified data in new array
                    r.append(element)
        return r

    def run_interpreter(self):
        import select, sys
        inputsentence = []

        while 1:
            r = select.select([self.sk, sys.stdin], [], [], None)
            if self.sk in r[0]:
                # something to read in socket, read sentence
                x = self.readSentence()

            if sys.stdin in r[0]:
                # read line from input and strip off newline
                l = sys.stdin.readline()
                l = l[:-1]

                # if empty line, send sentence and start with new
                # otherwise append to input sentence
                if l == '':
                    self.writeSentence(inputsentence)
                    inputsentence = []
                else:
                    inputsentence.append(l)
        return 0

    def close_connection(self):
        self.sk.close()


def prettify(data):
    for x in data:
        for y in x.keys():
            print "%-20s: %50s" % (y, x[y])



File: /Mikrotik_devel\library\RosRaw.py
#!/usr/bin/python
# -*- coding: utf-8 -*-
#
#

from ansible.module_utils.RosCore import *


def RosRaw(path, action, hostname="", username="admin", password="", command="", port=8728, DEBUG=False):

    lst = [path + action]
    while True:
    # Connect
        mikrotik = Core(hostname, DEBUG=DEBUG)
        login = mikrotik.login(username, password)
        # Check if login is correct
        if login[0][0] == '!trap':
            if DEBUG == True:
                print login

            return {"failed": True, "changed": False, "msg": "Login failed"}

        else:
            if DEBUG == True:
                print login

        if len(command) != 0:
            for i in range(0, len(command)):
                lst.append(command[i])

        raw_response = mikrotik.talk(lst)
        mikrotik.close_connection()
        return {"response": raw_response}



File: /Mikrotik_devel\library\test.py
#!/usr/bin/python
# -*- coding: UTF-8 -*-

from RosRaw import *

if __name__ == '__main__':
    response = RosRaw(path="/system/package/", action="print", hostname="192.168.1.100", \
        username="admin", password="Epuak3578@", DEBUG=True, command=["?name=ipv6"])

    print response





File: /Mikrotik_devel\roles\default\handlers\handlers.yml
---
  - name: Reboot device
    mt_raw: username={{username}} hostname={{IP}} password={{password}} path="/system/" action=reboot
  - name: Reboot to default
    mt_raw: username={{username}} hostname={{IP}} password={{password}} path="/system/" action=reset-configuration
  - name: Flush settings
    mt_raw: username={{username}} hostname={{IP}} password={{password}} path="/system/" action=reset-configuration command="no-defaults=true"



File: /Mikrotik_devel\roles\default\tasks\dhcp_server.yml
---
  - name: Create IP pool
    mt_ip_pool: username={{username}} hostname={{IP}} password={{password}}
      pool_name=pool1
      pool_range=192.168.200.100-192.168.200.200
  - name: DHCP Server Setup
    mt_dhcp_srv: username={{username}} hostname={{IP}} password={{password}}
      name=server1
      address_pool=pool1
      disabled="false"
      interface=ether2
  - name: DHCP Options Setup
    mt_dhcp_net: username={{username}} hostname={{IP}} password={{password}}
      network_address=192.168.116.0/24
      gateway=192.168.200.1
      dns_server=192.168.200.1


File: /Mikrotik_devel\roles\default\tasks\firewall.yml
---
  - name: Allow established and related connection
    mt_firewall: username={{username}} hostname={{IP}} password={{password}}
      chain=forward
      action=accept
      connection_state="established,related"
  - name: Allow outside connection only for dstnat
    mt_firewall: username={{username}} hostname={{IP}} password={{password}}
      chain=forward
      action=drop
      connection_state=new
      connection_nat_state="!nat"
  - name: Drop invalid traffic
    mt_firewall: username={{username}} hostname={{IP}} password={{password}}
      chain=forward
      action=drop
      connection_state=invalid

File: /Mikrotik_devel\roles\default\tasks\main.yml
---
  - name: Create Bridge
    mt_brctl: username={{username}} hostname={{IP}} password={{password}}
      interfaces=ether2,ether3
      names=bridge-local
      disabled="false"
      auto_isolate="false"
  - name: Set IP address on bridge interface
    mt_ip: username={{username}} hostname={{IP}} password={{password}}
      interface="bridge-local"
      address={{br_address}}
  - name: Source NAT
    mt_nat: username={{username}} hostname={{IP}} password={{password}}
      chain=srcnat
      action=masquerade
      out_interface=ether1



File: /Mikrotik_devel\roles\init\files\mtbash_clean.sh
#!/usr/bin/expect


set mac [lindex $argv 0]
set user [lindex $argv 1]
set pass [lindex $argv 2]

#Init phase
set ses 1

set $::env(TERM) xterm
spawn "mactelnet" "$mac"
set ses $spawn_id
set timeout 200
expect -i $ses "Login:"
send -i $ses "$user\r"
expect -i $ses "Password:"
send -i $ses "$pass\r"
sleep 5
send -i $ses "\r"


#Reset configuration with no default settings
expect "*>*"
send -i $ses "/system reset-configuration no-defaults=yes\r"
sleep 1
send -i $ses "y\r"
sleep 1

exit 0



File: /Mikrotik_devel\roles\init\files\mtbash_default.sh
#!/usr/bin/expect


#Destination MAC Address
set mac [lindex $argv 0]
#Username used for connection
set user [lindex $argv 1]
#Password used for connection
set pass [lindex $argv 2]
#Set Mikrotik's Identity
set identity [lindex $argv 3]
#Username for new user
set new_user [lindex $argv 4]
#Password for new user
set new_pass [lindex $argv 5]
#Interface used for management
set interface [lindex $argv 6]
#IP address used for management
set ip [lindex $argv 7]



set ses 1
set $::env(TERM) xterm
spawn "mactelnet" "$mac"
set ses $spawn_id
set timeout 200
expect -i $ses "Login:"
exp_send -i $ses "$user\r"
expect -i $ses "Password:"
exp_send -i $ses "$pass\r"
sleep 5
exp_send -i $ses "\r"


#Set identity
expect -i $ses "*>*"
exp_send -i $ses "/system identity set name=$identity\r"
sleep 1

#Create new user for management
expect -i $ses "*>*"
exp_send -i $ses "/user add name=$new_user password=$new_pass group=full\r"
sleep 1

#Set IP address on connected interface
expect -i $ses "*>*"
exp_send -i $ses "/ip address add address=$ip interface=$interface\r"
sleep 1

#END
expect -i $ses "*>*"
exp_send -i $ses "^D"
exit 0


File: /Mikrotik_devel\roles\init\tasks\clear.yml
---
  - name: Clear MikroTik Configuration
    local_action: script mtbash_clean.sh {{Source_MAC}} {{default_user}} {{default_password}}


File: /Mikrotik_devel\roles\init\tasks\default.yml
---
  - name: Add Default Configuration
    local_action: script mtbash_default.sh {{Source_MAC}} {{default_user}} {{default_password}} {{ID}} {{new_user}} {{new_password}} {{Port}} {{et1addr}}

File: /Mikrotik_devel\roles\init\tasks\main.yml
---
  - include: clear.yml
  - pause: minutes=1
  - include: default.yml

File: /Mikrotik_devel\site.yml
- name: Init Playbook # This playbook resets MikroTik devices and assingns IP addresses to connected ports
  hosts: mikrotiks
  connection: local
  gather_facts: no
  vars:
    default_user: admin
    default_password: "''"
    new_user: ansible
    new_password: ansible
    username: admin
    password: ""
  roles:
    - default

File: /Mikrotik_devel\testik.yml
- name: Testik playbook
  hosts: Router1
  connection: local
  gather_facts: no
  vars:
    username: admin
    password: ""
  tasks:
  - name: Ether2 IP address setup
    mt_firewall: username={{username}} hostname={{IP}} password={{password}}
      in_interface="ether1"
      disabled=true
      chain=forward
      connection_state="invalid"
      action=drop
      comment=rule2

File: /Mikrotik_devel\test_playbook.yml
- name: Mikrotik TEST
  hosts: Router1
  connection: local
  gather_facts: no
  vars:
    dhcp_pool: testpool
    username: admin
    password: ""

  tasks:
  - name: DNS Setup
    mt_dns: username={{username}} hostname={{IP}} password={{password}}
      servers="192.168.50.1"
      remote_requests="false"
  - name: IP address setup
    mt_ip: username={{username}} hostname={{IP}} password={{password}}
      address={{et2addr}}
      interface=ether2
      comment="et2-ip"
  - name: Add bridge interface
    mt_brctl: username={{username}} hostname={{IP}} password={{password}}
      names=bridge-local
      interfaces=ether2
  - name: Set static route
    mt_static_route: username={{username}} hostname={{IP}} password={{password}}
      dst_address=192.168.10.0/24
      gateway=192.168.10.10
      comment="Some network"
  - name: Source NAT
    mt_nat: username={{username}} hostname={{IP}} password={{password}}
      out_interface=ether1
      chain=srcnat
      action=masquerade
  - name: Port Forwarding to machine SSH
    mt_nat: username={{username}} hostname={{IP}} password={{password}}
      chain=dstnat
      action=dst-nat
      dst_port=8023
      to_addresses="192.168.116.22"
      to_ports=23
      protocol=tcp
      comment=Telnet
  - name: Enable RIP protocol
    mt_rip: username={{username}} hostname={{IP}} password={{password}}
      interfaces=ether1,bridge0
      redistribute_connected="true"


File: /Mikrotik_devel\test_playbook01.yml
- name: Mikrotik TEST
  hosts: mikrotik
  connection: local
  gather_facts: no
  vars:
    dhcp_pool: testpool
  tasks:
     - name: Fetch script
       mt_fetch: username={{username}} hostname={{hostname}} password={{password}} mode=ftp connection_username=mikrotik connection_password=mikrotik address="192.168.1.110" src_path=/fetch_6.34.4.rsc
     - name: Raw module test
       mt_raw: username={{username}} hostname={{hostname}} password={{password}} path=/

File: /Mikrotik_devel\test_playbook02.yml
- name: Mikrotik TEST
  hosts: Router1
  connection: local
  gather_facts: no
  vars:
    username: admin
    password: ""
  tasks:
  - name: RIP setup
    mt_rip: username={{username}} hostname={{IP}} password={{password}}
      interfaces=ether1,ether2
      networks="192.168.116.0/24"
      send=v2 receive=v2
      authentication=md5
      authentication_key=mikrotik
  - name: Configure brigde
    mt_brctl: username={{username}} hostname={{IP}} password={{password}}
      interfaces=!ether2,!ether3
      names=bridge0
      disabled="false"
      auto_isolate="false"

  handlers:
    - name: Reboot device
      mt_raw: username={{username}} hostname={{IP}} password={{password}} path="/system/" action=reboot
    - name: Reboot to default
      mt_raw: username={{username}} hostname={{IP}} password={{password}} path="/system/" action=reset-configuration
    - name: Flush settings
      mt_raw: username={{username}} hostname={{IP}} password={{password}} path="/system/" action=reset-configuration command="no-defaults=true"



File: /Mikrotik_devel\test_playbook_show.yml
- name: Mikrotik Network Playbook
  hosts: mikrotiks
  connection: local
  gather_facts: no
  vars:

  tasks:
  - name: Ether2 IP address setup
    mt_ip: username={{username}} hostname={{IP}} password={{password}}
      address={{et2addr}}
      interface=ether2
      comment="et2-ip"
  - include: roles/default/tasks/dhcp_server.yml
  - name: Enable RIP protocol
    mt_rip: username={{username}} hostname={{IP}} password={{password}}
      interfaces={{rip_interfaces}}
      redistribute_connected="true"
      send=v2
      receive=v2


