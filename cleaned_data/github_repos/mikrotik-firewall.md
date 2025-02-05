# Repository Information
Name: mikrotik-firewall

# Directory Structure
Directory structure:
└── github_repos/mikrotik-firewall/
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
    │   │       ├── pack-5a9e19136ac0c34a4c245f460c5d242d526871c6.idx
    │   │       └── pack-5a9e19136ac0c34a4c245f460c5d242d526871c6.pack
    │   ├── packed-refs
    │   └── refs/
    │       ├── heads/
    │       │   └── master
    │       ├── remotes/
    │       │   └── origin/
    │       │       └── HEAD
    │       └── tags/
    ├── defaults/
    │   └── main.yml
    ├── docs/
    │   ├── filter.md
    │   ├── mangle.md
    │   ├── nat.md
    │   └── raw.md
    ├── files/
    │   └── tmp/
    │       └── .gitignore
    ├── handlers/
    │   └── main.yml
    ├── meta/
    │   └── main.yml
    ├── README.md
    ├── tasks/
    │   ├── address_list.yml
    │   ├── connection_tracking.yml
    │   ├── filter.yml
    │   ├── main.yml
    │   ├── mangle.yml
    │   ├── nat.yml
    │   ├── raw.yml
    │   └── services.yml
    ├── templates/
    │   ├── address_list.rsc.j2
    │   ├── filter.rsc.j2
    │   ├── mangle.rsc.j2
    │   ├── nat.rsc.j2
    │   ├── raw.rsc.j2
    │   └── services.rsc.j2
    ├── tests/
    │   ├── inventory
    │   └── test.yml
    └── vars/
        └── main.yml


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
	url = https://github.com/mikrotik-ansible/mikrotik-firewall.git
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
0000000000000000000000000000000000000000 fe67e4b708c3d3b8fd2fa176100a4f169eaf5079 vivek-dodia <vivek.dodia@icloud.com> 1738605977 -0500	clone: from https://github.com/mikrotik-ansible/mikrotik-firewall.git


File: /.git\logs\refs\heads\master
0000000000000000000000000000000000000000 fe67e4b708c3d3b8fd2fa176100a4f169eaf5079 vivek-dodia <vivek.dodia@icloud.com> 1738605977 -0500	clone: from https://github.com/mikrotik-ansible/mikrotik-firewall.git


File: /.git\logs\refs\remotes\origin\HEAD
0000000000000000000000000000000000000000 fe67e4b708c3d3b8fd2fa176100a4f169eaf5079 vivek-dodia <vivek.dodia@icloud.com> 1738605977 -0500	clone: from https://github.com/mikrotik-ansible/mikrotik-firewall.git


File: /.git\packed-refs
# pack-refs with: peeled fully-peeled sorted 
c2a132da476981889d09351732b794fe93a2f06a refs/remotes/origin/jenkins
fe67e4b708c3d3b8fd2fa176100a4f169eaf5079 refs/remotes/origin/master


File: /.git\refs\heads\master
fe67e4b708c3d3b8fd2fa176100a4f169eaf5079


File: /.git\refs\remotes\origin\HEAD
ref: refs/remotes/origin/master


File: /defaults\main.yml
mikrotik_firewall:
  connection_tracking:
    enabled: "yes"
    tcp_syn_sent_timeout: 5s
    tcp_syn_received_timeout: 5s
    tcp_established_timeout: 1d
    tcp_fin_wait_timeout: 10s
    tcp_close_wait_timeout: 10s
    tcp_last_ack_timeout: 10s
    tcp_time_wait_timeout: 10s
    tcp_close_timeout: 10s
    tcp_max_retrans_timeout: 5m
    tcp_unacked_timeout: 5m
    udp_timeout: 10s
    udp_stream_timeout: 3m
    icmp_timeout: 10s
    generic_timeout: 10m
    
  remove_old_filter_rules: false
  filter_rules: []
  remove_old_nat_rules: false
  nat_rules: []
  remove_old_mangle_rules: false
  mangle_rules: []
  remove_old_raw_rules: false
  raw_rules: []
  service_port_rules:
    # Mikrotik defaults
    - name: ftp
      ports: 21
      sip_direct_media: "no"
      disabled: "no"
    - name: h323
      sip_direct_media: "no"
      disabled: "no"
    - name: irc
      ports: 6667
      sip_direct_media: "no"
      disabled: "no"
    - name: pptp
      sip_direct_media: "no"
      disabled: "no"
    - name: sip
      ports: 5060,5061
      sip_direct_media: "yes"
      disabled: "no"
    - name: tftp
      ports: 69
      disabled: "no"
  remove_old_address_list: false
  address_list: []
  remove_old_layers7_protocols: false
  layers7_protocols: []


File: /docs\filter.md
filter_rules:
-------------
```
chain:
action:
hotspot:
out_bridge_port:
routing_mark:
address_list:
icmp_options:
out_bridge_port_list:
routing_table:
address_list_timeout:
in_bridge_port:
out_interface:
src_address:
comment:
in_bridge_port_list:
out_interface_list:
src_address_list:
connection_bytes:
connection_mark:
connection_rate:
connection_type:
connection_limit:
connection_nat_state:
connection_state:
in_interface:
p2p:
src_address_type:
content:
in_interface_list:
packet_mark:
src_mac_address:
copy_from:
ingress_priority:
packet_size:
src_port:
disabled:
ipsec_policy:
per_connection_classifier:
tcp_flags:
dscp:
ipv4_options:
place_before:
tcp_mss:
dst_address:
jump_target:
port:
time:
dst_address_list:
layer7_protocol:
priority:
ttl:
dst_address_type:
limit:
protocol:
dst_limit:
log:
psd:
dst_port:
log_prefix:
random:
fragment:
nth:
reject_with:
```

File: /docs\mangle.md
mangle_rules:
-------------
```
chain:
action:
in_bridge_port:
new_routing_mark:
random:
address_list:
in_bridge_port_list:
new_ttl:
route_dst:
address_list_timeout:
in_interface:
nth:
routing_mark:
comment:
in_interface_list:
out_bridge_port:
routing_table:
connection_bytes:
connection_mark:
connection_rate:
connection_type:
connection_limit:
connection_nat_state:
connection_state:
ingress_priority:
out_bridge_port_list:
sniff_id:
content:
ipsec_policy:
out_interface:
sniff_target:
copy_from:
ipv4_options:
out_interface_list:
sniff_target_port:
disabled:
jump_target:
p2p:
src_address:
dscp:
layer7_protocol:
packet_mark:
src_address_list:
dst_address:
limit:
packet_size:
src_address_type:
dst_address_list:
log:
passthrough:
src_mac_address:
dst_address_type:
log_prefix:
per_connection_classifier:
src_port:
dst_limit:
new_connection_mark:
place_before:
tcp_flags:
dst_port:
new_dscp:
port:
tcp_mss:
fragment:
new_mss:
priority:
time:
hotspot:
new_packet_mark:
protocol:
ttl:
icmp_options:
new_priority:
psd:
```

File: /docs\nat.md
nat_rules:
----------
```
chain:
action:
hotspot:
out_bridge_port:
same_not_by_dst:
address_list:
icmp_options:
out_bridge_port_list:
src_address:
address_list_timeout:
in_bridge_port:
out_interface:
src_address_list:
comment:
in_bridge_port_list:
out_interface_list:
src_address_type:
connection_bytes:
connection_limit:
connection_mark:
connection_rate:
connection_type:
in_interface:
packet_mark:
src_mac_address:
content:
in_interface_list:
packet_size:
src_port:
copy_from:
ingress_priority:
per_connection_classifier:
tcp_mss:
disabled:
ipsec_policy:
place_before:
time:
dscp:
ipv4_options:
port:
to_addresses:
dst_address:
jump_target:
priority:
to_ports:
dst_address_list:
layer7_protocol:
protocol:
ttl:
dst_address_type:
limit:
psd:
dst_limit:
log:
random:
dst_port:
log_prefix:
routing_mark:
fragment:
nth:
routing_table:
```

File: /docs\raw.md
raw_rules:
----------
```
chain:
action:
fragment:
log_prefix:
psd:
address_list:
hotspot:
nth:
random:
address_list_timeout:
icmp_options:
out_bridge_port:
src_address:
comment:
in_bridge_port:
out_bridge_port_list:
src_address_list:
content:
in_bridge_port_list:
out_interface:
src_address_type:
copy_from:
in_interface:
out_interface_list:
src_mac_address:
disabled:
in_interface_list:
packet_mark:
src_port:
dscp:
ingress_priority:
packet_size:
tcp_flags:
dst_address:
ipsec_policy:
per_connection_classifier:
tcp_mss:
dst_address_list:
ipv4_options:
place_before:
time:
dst_address_type:
jump_target:
port:
ttl:
dst_limit:
limit:
priority:
dst_port:
log:
protocol:
```

File: /files\tmp\.gitignore
!.gitignore
*


File: /handlers\main.yml
---
# handlers file for mikrotik-firewall

File: /meta\main.yml
galaxy_info:
  author: Martin Dulin
  description: Mikrotik firewall automation
  company: Dulin
  license: MIT

  min_ansible_version: 1.9

  platforms:
    - name: RouterOS
      versions:
        - all

  categories:
    - networking

  galaxy_tags:
    - networking
    - mikrotik
    - routeros
    - firewall


dependencies: []
  # List your role dependencies here, one per line. Be sure to remove the '[]' above,
  # if you add dependencies to this list.


File: /README.md
Role Name
=========

A brief description of the role goes here.

Requirements
------------

Any pre-requisites that may not be covered by Ansible itself or the role should be mentioned here. For instance, if the role uses the EC2 module, it may be a good idea to mention in this section that the boto package is required.

Role Variables
--------------

A description of the settable variables for this role should go here, including any variables that are in defaults/main.yml, vars/main.yml, and any variables that can/should be set via parameters to the role. Any variables that are read from other roles and/or the global scope (ie. hostvars, group vars, etc.) should be mentioned here as well.

Dependencies
------------

A list of other roles hosted on Galaxy should go here, plus any details in regards to parameters that may need to be set for other roles, or variables that are used from other roles.

Example Playbook
----------------

Including an example of how to use your role (for instance, with variables passed in as parameters) is always nice for users too:

    - hosts: servers
      roles:
         - { role: username.rolename, x: 42 }

License
-------

BSD

Author Information
------------------

An optional section for the role authors to include contact information, or a website (HTML is not allowed).


File: /tasks\address_list.yml
---
  - name: Generate firewall-address_list-{{inventory_hostname}}.rsc to check and add user
    template: src=address_list.rsc.j2 dest={{role_path}}/files/tmp/firewall-address_list-{{inventory_hostname}}.rsc
    delegate_to: localhost

  - name: Send firewall-address_list-{{inventory_hostname}}.rsc script
    command: scp -P {{ansible_port}} {{role_path}}/files/tmp/firewall-address_list-{{inventory_hostname}}.rsc {{ansible_user}}@{{ansible_host}}:/firewall-address_list-{{inventory_hostname}}.rsc
    delegate_to: localhost

  - name: Delete temporary firewall-address_list-{{inventory_hostname}}.rsc file
    file: path={{role_path}}/files/tmp/firewall-address_list-{{inventory_hostname}}.rsc state=absent
    delegate_to: localhost

  - name: Run firewall-address_list-{{inventory_hostname}}.rsc on router
    raw:  "/import firewall-address_list-{{inventory_hostname}}.rsc"
    tags: mikrotik_firewall_services

  - name: Remove firewall-address_list-{{inventory_hostname}}.rsc from router
    raw:  "/file remove firewall-address_list-{{inventory_hostname}}.rsc"


File: /tasks\connection_tracking.yml
---
- name: "Setting enabled={{ mikrotik_firewall.connection_tracking.enabled }}"
  raw: :if ([/ip firewall connection tracking get enabled] != "{{ mikrotik_firewall.connection_tracking.enabled }}") do={:put "enabled"; /ip firewall connection tracking set enabled={{ mikrotik_firewall.connection_tracking.enabled }} }
  when: mikrotik_firewall.connection_tracking.enabled is defined
  register: enabled
  changed_when: enabled.stdout_lines[0] is defined and enabled.stdout_lines[0] == "enabled"
  failed_when: enabled.stdout_lines[0] is defined and enabled.stdout_lines[0] != "enabled"

- name: "Setting tcp-syn-sent-timeout={{ mikrotik_firewall.connection_tracking.tcp_syn_sent_timeout }}"
  raw: :if ([/ip firewall connection tracking get tcp-syn-sent-timeout] != {{ mikrotik_firewall.connection_tracking.tcp_syn_sent_timeout }}) do={:put "tcp-syn-sent-timeout"; /ip firewall connection tracking set tcp-syn-sent-timeout={{ mikrotik_firewall.connection_tracking.tcp_syn_sent_timeout }} }
  when: mikrotik_firewall.connection_tracking.tcp_syn_sent_timeout is defined
  register: tcp_syn_sent_timeout
  changed_when: tcp_syn_sent_timeout.stdout_lines[0] is defined and tcp_syn_sent_timeout.stdout_lines[0] == "tcp-syn-sent-timeout"
  failed_when: tcp_syn_sent_timeout.stdout_lines[0] is defined and tcp_syn_sent_timeout.stdout_lines[0] != "tcp-syn-sent-timeout"

- name: "Setting tcp-syn-received-timeout={{ mikrotik_firewall.connection_tracking.tcp_syn_received_timeout }}"
  raw: :if ([/ip firewall connection tracking get tcp-syn-received-timeout] != {{ mikrotik_firewall.connection_tracking.tcp_syn_received_timeout }}) do={:put "tcp-syn-received-timeout"; /ip firewall connection tracking set tcp-syn-received-timeout={{ mikrotik_firewall.connection_tracking.tcp_syn_received_timeout }} }
  when: mikrotik_firewall.connection_tracking.tcp_syn_received_timeout is defined
  register: tcp_syn_received_timeout
  changed_when: tcp_syn_received_timeout.stdout_lines[0] is defined and tcp_syn_received_timeout.stdout_lines[0] == "tcp-syn-received-timeout"
  failed_when: tcp_syn_received_timeout.stdout_lines[0] is defined and tcp_syn_received_timeout.stdout_lines[0] != "tcp-syn-received-timeout"

- name: "Setting tcp-established-timeout={{ mikrotik_firewall.connection_tracking.tcp_established_timeout }}"
  raw: :if ([/ip firewall connection tracking get tcp-established-timeout] != {{ mikrotik_firewall.connection_tracking.tcp_established_timeout }}) do={:put "tcp-established-timeout"; /ip firewall connection tracking set tcp-established-timeout={{ mikrotik_firewall.connection_tracking.tcp_established_timeout }} }
  when: mikrotik_firewall.connection_tracking.tcp_established_timeout is defined
  register: tcp_established_timeout
  changed_when: tcp_established_timeout.stdout_lines[0] is defined and tcp_established_timeout.stdout_lines[0] == "tcp-established-timeout"
  failed_when: tcp_established_timeout.stdout_lines[0] is defined and tcp_established_timeout.stdout_lines[0] != "tcp-established-timeout"

- name: "Setting tcp-fin-wait-timeout={{ mikrotik_firewall.connection_tracking.tcp_fin_wait_timeout }}"
  raw: :if ([/ip firewall connection tracking get tcp-fin-wait-timeout] != {{ mikrotik_firewall.connection_tracking.tcp_fin_wait_timeout }}) do={:put "tcp-fin-wait-timeout"; /ip firewall connection tracking set tcp-fin-wait-timeout={{ mikrotik_firewall.connection_tracking.tcp_fin_wait_timeout }} }
  when: mikrotik_firewall.connection_tracking.tcp_fin_wait_timeout is defined
  register: tcp_fin_wait_timeout
  changed_when: tcp_fin_wait_timeout.stdout_lines[0] is defined and tcp_fin_wait_timeout.stdout_lines[0] == "tcp-fin-wait-timeout"
  failed_when: tcp_fin_wait_timeout.stdout_lines[0] is defined and tcp_fin_wait_timeout.stdout_lines[0] != "tcp-fin-wait-timeout"

- name: "Setting tcp-close-wait-timeout={{ mikrotik_firewall.connection_tracking.tcp_close_wait_timeout }}"
  raw: :if ([/ip firewall connection tracking get tcp-close-wait-timeout] != {{ mikrotik_firewall.connection_tracking.tcp_close_wait_timeout }}) do={:put "tcp-close-wait-timeout"; /ip firewall connection tracking set tcp-close-wait-timeout={{ mikrotik_firewall.connection_tracking.tcp_close_wait_timeout }} }
  when: mikrotik_firewall.connection_tracking.tcp_close_wait_timeout is defined
  register: tcp_close_wait_timeout
  changed_when: tcp_close_wait_timeout.stdout_lines[0] is defined and tcp_close_wait_timeout.stdout_lines[0] == "tcp-close-wait-timeout"
  failed_when: tcp_close_wait_timeout.stdout_lines[0] is defined and tcp_close_wait_timeout.stdout_lines[0] != "tcp-close-wait-timeout"

- name: "Setting tcp-last-ack-timeout={{ mikrotik_firewall.connection_tracking.tcp_last_ack_timeout }}"
  raw: :if ([/ip firewall connection tracking get tcp-last-ack-timeout] != {{ mikrotik_firewall.connection_tracking.tcp_last_ack_timeout }}) do={:put "tcp-last-ack-timeout"; /ip firewall connection tracking set tcp-last-ack-timeout={{ mikrotik_firewall.connection_tracking.tcp_last_ack_timeout }} }
  when: mikrotik_firewall.connection_tracking.tcp_last_ack_timeout is defined
  register: tcp_last_ack_timeout
  changed_when: tcp_last_ack_timeout.stdout_lines[0] is defined and tcp_last_ack_timeout.stdout_lines[0] == "tcp-last-ack-timeout"
  failed_when: tcp_last_ack_timeout.stdout_lines[0] is defined and tcp_last_ack_timeout.stdout_lines[0] != "tcp-last-ack-timeout"

- name: "Setting tcp-time-wait-timeout={{ mikrotik_firewall.connection_tracking.tcp_time_wait_timeout }}"
  raw: :if ([/ip firewall connection tracking get tcp-time-wait-timeout] != {{ mikrotik_firewall.connection_tracking.tcp_time_wait_timeout }}) do={:put "tcp-time-wait-timeout"; /ip firewall connection tracking set tcp-time-wait-timeout={{ mikrotik_firewall.connection_tracking.tcp_time_wait_timeout }} }
  when: mikrotik_firewall.connection_tracking.tcp_time_wait_timeout is defined
  register: tcp_time_wait_timeout
  changed_when: tcp_time_wait_timeout.stdout_lines[0] is defined and tcp_time_wait_timeout.stdout_lines[0] == "tcp-time-wait-timeout"
  failed_when: tcp_time_wait_timeout.stdout_lines[0] is defined and tcp_time_wait_timeout.stdout_lines[0] != "tcp-time-wait-timeout"

- name: "Setting tcp-close-timeout={{ mikrotik_firewall.connection_tracking.tcp_close_timeout }}"
  raw: :if ([/ip firewall connection tracking get tcp-close-timeout] != {{ mikrotik_firewall.connection_tracking.tcp_close_timeout }}) do={:put "tcp-close-timeout"; /ip firewall connection tracking set tcp-close-timeout={{ mikrotik_firewall.connection_tracking.tcp_close_timeout }} }
  when: mikrotik_firewall.connection_tracking.tcp_close_timeout is defined
  register: tcp_close_timeout
  changed_when: tcp_close_timeout.stdout_lines[0] is defined and tcp_close_timeout.stdout_lines[0] == "tcp-close-timeout"
  failed_when: tcp_close_timeout.stdout_lines[0] is defined and tcp_close_timeout.stdout_lines[0] != "tcp-close-timeout"

- name: "Setting tcp-max-retrans-timeout={{ mikrotik_firewall.connection_tracking.tcp_max_retrans_timeout }}"
  raw: :if ([/ip firewall connection tracking get tcp-max-retrans-timeout] != {{ mikrotik_firewall.connection_tracking.tcp_max_retrans_timeout }}) do={:put "tcp-max-retrans-timeout"; /ip firewall connection tracking set tcp-max-retrans-timeout={{ mikrotik_firewall.connection_tracking.tcp_max_retrans_timeout }} }
  when: mikrotik_firewall.connection_tracking.tcp_max_retrans_timeout is defined
  register: tcp_max_retrans_timeout
  changed_when: tcp_max_retrans_timeout.stdout_lines[0] is defined and tcp_max_retrans_timeout.stdout_lines[0] == "tcp-max-retrans-timeout"
  failed_when: tcp_max_retrans_timeout.stdout_lines[0] is defined and tcp_max_retrans_timeout.stdout_lines[0] != "tcp-max-retrans-timeout"

- name: "Setting tcp-unacked-timeout={{ mikrotik_firewall.connection_tracking.tcp_unacked_timeout }}"
  raw: :if ([/ip firewall connection tracking get tcp-unacked-timeout] != {{ mikrotik_firewall.connection_tracking.tcp_unacked_timeout }}) do={:put "tcp-unacked-timeout"; /ip firewall connection tracking set tcp-unacked-timeout={{ mikrotik_firewall.connection_tracking.tcp_unacked_timeout }} }
  when: mikrotik_firewall.connection_tracking.tcp_unacked_timeout is defined
  register: tcp_unacked_timeout
  changed_when: tcp_unacked_timeout.stdout_lines[0] is defined and tcp_unacked_timeout.stdout_lines[0] == "tcp-unacked-timeout"
  failed_when: tcp_unacked_timeout.stdout_lines[0] is defined and tcp_unacked_timeout.stdout_lines[0] != "tcp-unacked-timeout"

- name: "Setting udp-timeout={{ mikrotik_firewall.connection_tracking.udp_timeout }}"
  raw: :if ([/ip firewall connection tracking get udp-timeout] != {{ mikrotik_firewall.connection_tracking.udp_timeout }}) do={:put "udp-timeout"; /ip firewall connection tracking set udp-timeout={{ mikrotik_firewall.connection_tracking.udp_timeout }} }
  when: mikrotik_firewall.connection_tracking.udp_timeout is defined
  register: udp_timeout
  changed_when: udp_timeout.stdout_lines[0] is defined and udp_timeout.stdout_lines[0] == "udp-timeout"
  failed_when: udp_timeout.stdout_lines[0] is defined and udp_timeout.stdout_lines[0] != "udp-timeout"

- name: "Setting udp-stream-timeout={{ mikrotik_firewall.connection_tracking.udp_stream_timeout }}"
  raw: :if ([/ip firewall connection tracking get udp-stream-timeout] != {{ mikrotik_firewall.connection_tracking.udp_stream_timeout }}) do={:put "udp-stream-timeout"; /ip firewall connection tracking set udp-stream-timeout={{ mikrotik_firewall.connection_tracking.udp_stream_timeout }} }
  when: mikrotik_firewall.connection_tracking.udp_stream_timeout is defined
  register: udp_stream_timeout
  changed_when: udp_stream_timeout.stdout_lines[0] is defined and udp_stream_timeout.stdout_lines[0] == "udp-stream-timeout"
  failed_when: udp_stream_timeout.stdout_lines[0] is defined and udp_stream_timeout.stdout_lines[0] != "udp-stream-timeout"

- name: "Setting icmp-timeout={{ mikrotik_firewall.connection_tracking.icmp_timeout }}"
  raw: :if ([/ip firewall connection tracking get icmp-timeout] != {{ mikrotik_firewall.connection_tracking.icmp_timeout }}) do={:put "icmp-timeout"; /ip firewall connection tracking set icmp-timeout={{ mikrotik_firewall.connection_tracking.icmp_timeout }} }
  when: mikrotik_firewall.connection_tracking.icmp_timeout is defined
  register: icmp_timeout
  changed_when: icmp_timeout.stdout_lines[0] is defined and icmp_timeout.stdout_lines[0] == "icmp-timeout"
  failed_when: icmp_timeout.stdout_lines[0] is defined and icmp_timeout.stdout_lines[0] != "icmp-timeout"

- name: "Setting generic-timeout={{ mikrotik_firewall.connection_tracking.generic_timeout }}"
  raw: :if ([/ip firewall connection tracking get generic-timeout] != {{ mikrotik_firewall.connection_tracking.generic_timeout }}) do={:put "generic-timeout"; /ip firewall connection tracking set generic-timeout={{ mikrotik_firewall.connection_tracking.generic_timeout }} }
  when: mikrotik_firewall.connection_tracking.generic_timeout is defined
  register: generic_timeout
  changed_when: generic_timeout.stdout_lines[0] is defined and generic_timeout.stdout_lines[0] == "generic-timeout"
  failed_when: generic_timeout.stdout_lines[0] is defined and generic_timeout.stdout_lines[0] != "generic-timeout"


File: /tasks\filter.yml
---
  - name: Generate firewall-filter-{{inventory_hostname}}.rsc to check and add user
    template: src=filter.rsc.j2 dest={{role_path}}/files/tmp/firewall-filter-{{inventory_hostname}}.rsc
    delegate_to: localhost

  - name: Send firewall-filter-{{inventory_hostname}}.rsc script
    command: scp -P {{ansible_port}} {{role_path}}/files/tmp/firewall-filter-{{inventory_hostname}}.rsc {{ansible_user}}@{{ansible_host}}:/firewall-filter-{{inventory_hostname}}.rsc
    delegate_to: localhost

  - name: Delete temporary firewall-filter-{{inventory_hostname}}.rsc file
    file: path={{role_path}}/files/tmp/firewall-filter-{{inventory_hostname}}.rsc state=absent
    delegate_to: localhost

  - name: Run firewall-filter-{{inventory_hostname}}.rsc on router
    raw: "/import firewall-filter-{{inventory_hostname}}.rsc"
    tags: mikrotik_firewall_services

  - name: Remove firewall-filter-{{inventory_hostname}}.rsc from router
    raw: "/file remove firewall-filter-{{inventory_hostname}}.rsc"


File: /tasks\main.yml
---
- include: connection_tracking.yml
  tags: [ 'role::mikrotik_firewall::connection_tracking']
  
- include: services.yml
  tags: [ 'role::mikrotik_firewall:services' ]

- include: address_list.yml
  tags: [ 'role::mikrotik_firewall:address_list' ]

- include: raw.yml
  tags: [ 'role::mikrotik_firewall:raw' ]

- include: mangle.yml
  tags: [ 'role::mikrotik_firewall:mangle' ]

- include: nat.yml
  tags: [ 'role::mikrotik_firewall:nat' ]

- include: filter.yml
  tags: [ 'role::mikrotik_firewall:filter' ]


File: /tasks\mangle.yml
---
  - name: Generate firewall-mangle-{{inventory_hostname}}.rsc to check and add user
    template: src=mangle.rsc.j2 dest={{role_path}}/files/tmp/firewall-mangle-{{inventory_hostname}}.rsc
    delegate_to: localhost

  - name: Send firewall-mangle-{{inventory_hostname}}.rsc script
    command: scp -P {{ansible_port}} {{role_path}}/files/tmp/firewall-mangle-{{inventory_hostname}}.rsc {{ansible_user}}@{{ansible_host}}:/firewall-mangle-{{inventory_hostname}}.rsc
    delegate_to: localhost

  - name: Delete temporary firewall-mangle-{{inventory_hostname}}.rsc file
    file: path={{role_path}}/files/tmp/firewall-mangle-{{inventory_hostname}}.rsc state=absent
    delegate_to: localhost

  - name: Run firewall-mangle-{{inventory_hostname}}.rsc on router
    raw:  "/import firewall-mangle-{{inventory_hostname}}.rsc"
    tags: mikrotik_firewall_services

  - name: Remove firewall-mangle-{{inventory_hostname}}.rsc from router
    raw:  "/file remove firewall-mangle-{{inventory_hostname}}.rsc"


File: /tasks\nat.yml
---
  - name: Generate firewall-nat-{{inventory_hostname}}.rsc to check and add user
    template: src=nat.rsc.j2 dest={{role_path}}/files/tmp/firewall-nat-{{inventory_hostname}}.rsc
    delegate_to: localhost

  - name: Send firewall-nat-{{inventory_hostname}}.rsc script
    command: scp -P {{ansible_port}} {{role_path}}/files/tmp/firewall-nat-{{inventory_hostname}}.rsc {{ansible_user}}@{{ansible_host}}:/firewall-nat-{{inventory_hostname}}.rsc
    delegate_to: localhost

  - name: Delete temporary firewall-nat-{{inventory_hostname}}.rsc file
    file: path={{role_path}}/files/tmp/firewall-nat-{{inventory_hostname}}.rsc state=absent
    delegate_to: localhost

  - name: Run firewall-nat-{{inventory_hostname}}.rsc on router
    raw: "/import firewall-nat-{{inventory_hostname}}.rsc"
    tags: mikrotik_firewall_services

  - name: Remove firewall-nat-{{inventory_hostname}}.rsc from router
    raw: "/file remove firewall-nat-{{inventory_hostname}}.rsc"


File: /tasks\raw.yml
---
  - name: Generate firewall-raw-{{inventory_hostname}}.rsc to check and add user
    template: src=raw.rsc.j2 dest={{role_path}}/files/tmp/firewall-raw-{{inventory_hostname}}.rsc
    delegate_to: localhost

  - name: Send firewall-raw-{{inventory_hostname}}.rsc script
    command: scp -P {{ansible_port}} {{role_path}}/files/tmp/firewall-raw-{{inventory_hostname}}.rsc {{ansible_user}}@{{ansible_host}}:/firewall-raw-{{inventory_hostname}}.rsc
    delegate_to: localhost

  - name: Delete temporary firewall-raw-{{inventory_hostname}}.rsc file
    file: path={{role_path}}/files/tmp/firewall-raw-{{inventory_hostname}}.rsc state=absent
    delegate_to: localhost

  - name: Run firewall-raw-{{inventory_hostname}}.rsc on router
    raw:  "/import firewall-raw-{{inventory_hostname}}.rsc"
    tags: mikrotik_firewall_services

  - name: Remove firewall-raw-{{inventory_hostname}}.rsc from router
    raw:  "/file remove firewall-raw-{{inventory_hostname}}.rsc"


File: /tasks\services.yml
---
  - name: Generate firewall-services-{{inventory_hostname}}.rsc to check and add user
    template: src=services.rsc.j2 dest={{role_path}}/files/tmp/firewall-services-{{inventory_hostname}}.rsc
    delegate_to: localhost

  - name: Send firewall-services-{{inventory_hostname}}.rsc script
    command: scp -P {{ansible_port}} {{role_path}}/files/tmp/firewall-services-{{inventory_hostname}}.rsc {{ansible_user}}@{{ansible_host}}:/firewall-services-{{inventory_hostname}}.rsc
    delegate_to: localhost

  - name: Delete temporary firewall-services-{{inventory_hostname}}.rsc file
    file: path={{role_path}}/files/tmp/firewall-services-{{inventory_hostname}}.rsc state=absent
    delegate_to: localhost

  - name: Run firewall-services-{{inventory_hostname}}.rsc on router
    raw:  "/import firewall-services-{{inventory_hostname}}.rsc"

  - name: Remove firewall-services-{{inventory_hostname}}.rsc from router
    raw:  "/file remove firewall-services-{{inventory_hostname}}.rsc"


File: /templates\address_list.rsc.j2
{% if  mikrotik_firewall.remove_old_address_list == true %}
/ip firewall address-list remove [/ip firewall address-list find where dynamic=no]
{% endif %}
# Remove not defined
/ip firewall address-list remove [/ip firewall address-list find where !(\
{% for list in mikrotik_firewall.address_list %}
{% if iter is defined %} or {% endif %}(list={{list.list}} and disabled={{list.disabled}} and address={{list.address}} and comment="Ansible managed: [{{list.comment}}]") \
{% set iter = true %}
{% endfor %}
) and dynamic=no]
# Add all values
{% for list in mikrotik_firewall.address_list %}
:if ([/ip firewall address-list find list={{list.list}} disabled={{list.disabled}} address={{list.address}} comment="Ansible managed: [{{list.comment}}]"] = "") do={
:log info "Add address: {{list.address}} to address-list: {{list.list}}..."
/ip firewall address-list add list={{list.list}} {% if list.disabled is defined %}disabled={{list.disabled}} {%endif%}address={{list.address}}\
{% if list.comment is defined %}
 comment="Ansible managed: [{{list.comment}}]"
{% endif %}
}
{% endfor %}


File: /templates\filter.rsc.j2
{% if  mikrotik_firewall.remove_old_filter_rules == true %}
/ip firewall filter remove [/ip firewall filter find where dynamic=no]
{% endif %}
# Remove not defined
/ip firewall filter remove [/ip firewall filter find where !(\
{% for filter in mikrotik_firewall.filter_rules %}
{% if iter is defined %} or {% endif %}(chain="{{filter.chain}}" \
{% if filter.action is defined %}and action="{{filter.action}}" {%endif%}
{% if filter.hotspot is defined %}and hotspot="{{filter.hotspot}}" {%endif%}
{% if filter.out_bridge_port is defined %}and out-bridge-port="{{filter.out_bridge_port}}" {%endif%}
{% if filter.routing_mark is defined %}and routing-mark="{{filter.routing_mark}}" {%endif%}
{% if filter.address_list is defined %}and address-list="{{filter.address_list}}" {%endif%}
{% if filter.icmp_options is defined %}and icmp-options="{{filter.icmp_options}}" {%endif%}
{% if filter.out_bridge_port_list is defined %}and out-bridge-port-list="{{filter.out_bridge_port_list}}" {%endif%}
{% if filter.routing_table is defined %}and routing-table="{{filter.routing_table}}" {%endif%}
{% if filter.address_list_timeout is defined %}and address-list-timeout="{{filter.address_list_timeout}}" {%endif%}
{% if filter.in_bridge_port is defined %}and in-bridge-port="{{filter.in_bridge_port}}" {%endif%}
{% if filter.out_interface is defined %}and out-interface="{{filter.out_interface}}" {%endif%}
{% if filter.src_address is defined %}and src-address="{{filter.src_address}}" {%endif%}
{% if filter.comment is defined %}and comment="Ansible managed: [{{filter.comment}}]" {%endif%}
{% if filter.in_bridge_port_list is defined %}and in-bridge-port-list="{{filter.in_bridge_port_list}}" {%endif%}
{% if filter.out_interface_list is defined %}and out-interface-list="{{filter.out_interface_list}}" {%endif%}
{% if filter.src_address_list is defined %}and src-address-list="{{filter.src_address_list}}" {%endif%}
{% if filter.connection_bytes is defined %}and connection-bytes="{{filter.connection_bytes}}" {%endif%}
{% if filter.connection_mark is defined %}and connection-mark="{{filter.connection_mark}}" {%endif%}
{% if filter.connection_rate is defined %}and connection-rate="{{filter.connection_rate}}" {%endif%}
{% if filter.connection_type is defined %}and connection-type="{{filter.connection_type}}" {%endif%}
{% if filter.connection_limit is defined %}and connection-limit="{{filter.connection_limit}}" {%endif%}
{% if filter.connection_nat_state is defined %}and connection-nat-state="{{filter.connection_nat_state}}" {%endif%}
{% if filter.connection_state is defined %}and connection-state="{{filter.connection_state}}" {%endif%}
{% if filter.in_interface is defined %}and in-interface="{{filter.in_interface}}" {%endif%}
{% if filter.p2p is defined %}and p2p="{{filter.p2p}}" {%endif%}
{% if filter.src_address_type is defined %}and src-address-type="{{filter.src_address_type}}" {%endif%}
{% if filter.content is defined %}and content="{{filter.content}}" {%endif%}
{% if filter.in_interface_list is defined %}and in-interface-list="{{filter.in_interface_list}}" {%endif%}
{% if filter.packet_mark is defined %}and packet-mark="{{filter.packet_mark}}" {%endif%}
{% if filter.src_mac_address is defined %}and src-mac-address="{{filter.src_mac_address}}" {%endif%}
{% if filter.copy_from is defined %}and copy-from="{{filter.copy_from}}" {%endif%}
{% if filter.ingress_priority is defined %}and ingress-priority="{{filter.ingress_priority}}" {%endif%}
{% if filter.packet_size is defined %}and packet-size="{{filter.packet_size}}" {%endif%}
{% if filter.src_port is defined %}and src-port="{{filter.src_port}}" {%endif%}
{% if filter.disabled is defined %}and disabled={{filter.disabled}} {%endif%}
{% if filter.ipsec_policy is defined %}and ipsec-policy="{{filter.ipsec_policy}}" {%endif%}
{% if filter.per_connection_classifier is defined %}and per-connection-classifier="{{filter.per_connection_classifier}}" {%endif%}
{% if filter.tcp_flags is defined %}and tcp-flags="{{filter.tcp_flags}}" {%endif%}
{% if filter.dscp is defined %}and dscp="{{filter.dscp}}" {%endif%}
{% if filter.ipv4_options is defined %}and ipv4-options="{{filter.ipv4_options}}" {%endif%}
{% if filter.place_before is defined %}and place-before="{{filter.place_before}}" {%endif%}
{% if filter.tcp_mss is defined %}and tcp-mss="{{filter.tcp_mss}}" {%endif%}
{% if filter.dst_address is defined %}and dst-address="{{filter.dst_address}}" {%endif%}
{% if filter.jump_target is defined %}and jump-target="{{filter.jump_target}}" {%endif%}
{% if filter.port is defined %}and port="{{filter.port}}" {%endif%}
{% if filter.time is defined %}and time="{{filter.time}}" {%endif%}
{% if filter.dst_address_list is defined %}and dst-address-list="{{filter.dst_address_list}}" {%endif%}
{% if filter.layer7_protocol is defined %}and layer7-protocol="{{filter.layer7_protocol}}" {%endif%}
{% if filter.priority is defined %}and priority="{{filter.priority}}" {%endif%}
{% if filter.ttl is defined %}and ttl="{{filter.ttl}}" {%endif%}
{% if filter.dst_address_type is defined %}and dst-address-type="{{filter.dst_address_type}}" {%endif%}
{% if filter.limit is defined %}and limit="{{filter.limit}}" {%endif%}
{% if filter.protocol is defined %}and protocol="{{filter.protocol}}" {%endif%}
{% if filter.dst_limit is defined %}and dst-limit="{{filter.dst_limit}}" {%endif%}
{% if filter.log is defined %}and log="{{filter.log}}" {%endif%}
{% if filter.psd is defined %}and psd="{{filter.psd}}" {%endif%}
{% if filter.dst_port is defined %}and dst-port="{{filter.dst_port}}" {%endif%}
{% if filter.log_prefix is defined %}and log-prefix="{{filter.log_prefix}}" {%endif%}
{% if filter.random is defined %}and random="{{filter.random}}" {%endif%}
{% if filter.fragment is defined %}and fragment="{{filter.fragment}}" {%endif%}
{% if filter.nth is defined %}and nth="{{filter.nth}}" {%endif%}
{% if filter.reject_with is defined %}and reject-with="{{filter.reject_with}}" {%endif%}) \
{% set iter = true %}
{%endfor%}
) and dynamic=no]

{% for filter in mikrotik_firewall.filter_rules %}
:if ([/ip firewall filter find chain={{filter.chain}} \
{% if filter.action is defined %}action="{{filter.action}}" {%endif%}
{% if filter.hotspot is defined %}hotspot="{{filter.hotspot}}" {%endif%}
{% if filter.out_bridge_port is defined %}out-bridge-port="{{filter.out_bridge_port}}" {%endif%}
{% if filter.routing_mark is defined %}routing-mark="{{filter.routing_mark}}" {%endif%}
{% if filter.address_list is defined %}address-list="{{filter.address_list}}" {%endif%}
{% if filter.icmp_options is defined %}icmp-options="{{filter.icmp_options}}" {%endif%}
{% if filter.out_bridge_port_list is defined %}out-bridge-port-list="{{filter.out_bridge_port_list}}" {%endif%}
{% if filter.routing_table is defined %}routing-table="{{filter.routing_table}}" {%endif%}
{% if filter.address_list_timeout is defined %}address-list-timeout="{{filter.address_list_timeout}}" {%endif%}
{% if filter.in_bridge_port is defined %}in-bridge-port="{{filter.in_bridge_port}}" {%endif%}
{% if filter.out_interface is defined %}out-interface="{{filter.out_interface}}" {%endif%}
{% if filter.src_address is defined %}src-address="{{filter.src_address}}" {%endif%}
{% if filter.comment is defined %}comment="Ansible managed: [{{filter.comment}}]" {%endif%}
{% if filter.in_bridge_port_list is defined %}in-bridge-port-list="{{filter.in_bridge_port_list}}" {%endif%}
{% if filter.out_interface_list is defined %}out-interface-list="{{filter.out_interface_list}}" {%endif%}
{% if filter.src_address_list is defined %}src-address-list="{{filter.src_address_list}}" {%endif%}
{% if filter.connection_bytes is defined %}connection-bytes="{{filter.connection_bytes}}" {%endif%}
{% if filter.connection_mark is defined %}connection-mark="{{filter.connection_mark}}" {%endif%}
{% if filter.connection_rate is defined %}connection-rate="{{filter.connection_rate}}" {%endif%}
{% if filter.connection_type is defined %}connection-type="{{filter.connection_type}}" {%endif%}
{% if filter.connection_limit is defined %}connection-limit="{{filter.connection_limit}}" {%endif%}
{% if filter.connection_nat_state is defined %}connection-nat-state="{{filter.connection_nat_state}}" {%endif%}
{% if filter.connection_state is defined %}connection-state="{{filter.connection_state}}" {%endif%}
{% if filter.in_interface is defined %}in-interface="{{filter.in_interface}}" {%endif%}
{% if filter.p2p is defined %}p2p="{{filter.p2p}}" {%endif%}
{% if filter.src_address_type is defined %}src-address-type="{{filter.src_address_type}}" {%endif%}
{% if filter.content is defined %}content="{{filter.content}}" {%endif%}
{% if filter.in_interface_list is defined %}in-interface-list="{{filter.in_interface_list}}" {%endif%}
{% if filter.packet_mark is defined %}packet-mark="{{filter.packet_mark}}" {%endif%}
{% if filter.src_mac_address is defined %}src-mac-address="{{filter.src_mac_address}}" {%endif%}
{% if filter.copy_from is defined %}copy-from="{{filter.copy_from}}" {%endif%}
{% if filter.ingress_priority is defined %}ingress-priority="{{filter.ingress_priority}}" {%endif%}
{% if filter.packet_size is defined %}packet-size="{{filter.packet_size}}" {%endif%}
{% if filter.src_port is defined %}src-port="{{filter.src_port}}" {%endif%}
{% if filter.disabled is defined %}disabled={{filter.disabled}} {%endif%}
{% if filter.ipsec_policy is defined %}ipsec-policy="{{filter.ipsec_policy}}" {%endif%}
{% if filter.per_connection_classifier is defined %}per-connection-classifier="{{filter.per_connection_classifier}}" {%endif%}
{% if filter.tcp_flags is defined %}tcp-flags="{{filter.tcp_flags}}" {%endif%}
{% if filter.dscp is defined %}dscp="{{filter.dscp}}" {%endif%}
{% if filter.ipv4_options is defined %}ipv4-options="{{filter.ipv4_options}}" {%endif%}
{% if filter.place_before is defined %}place-before="{{filter.place_before}}" {%endif%}
{% if filter.tcp_mss is defined %}tcp-mss="{{filter.tcp_mss}}" {%endif%}
{% if filter.dst_address is defined %}dst-address="{{filter.dst_address}}" {%endif%}
{% if filter.jump_target is defined %}jump-target="{{filter.jump_target}}" {%endif%}
{% if filter.port is defined %}port="{{filter.port}}" {%endif%}
{% if filter.time is defined %}time="{{filter.time}}" {%endif%}
{% if filter.dst_address_list is defined %}dst-address-list="{{filter.dst_address_list}}" {%endif%}
{% if filter.layer7_protocol is defined %}layer7-protocol="{{filter.layer7_protocol}}" {%endif%}
{% if filter.priority is defined %}priority="{{filter.priority}}" {%endif%}
{% if filter.ttl is defined %}ttl="{{filter.ttl}}" {%endif%}
{% if filter.dst_address_type is defined %}dst-address-type="{{filter.dst_address_type}}" {%endif%}
{% if filter.limit is defined %}limit="{{filter.limit}}" {%endif%}
{% if filter.protocol is defined %}protocol="{{filter.protocol}}" {%endif%}
{% if filter.dst_limit is defined %}dst-limit="{{filter.dst_limit}}" {%endif%}
{% if filter.log is defined %}log="{{filter.log}}" {%endif%}
{% if filter.psd is defined %}psd="{{filter.psd}}" {%endif%}
{% if filter.dst_port is defined %}dst-port="{{filter.dst_port}}" {%endif%}
{% if filter.log_prefix is defined %}log-prefix="{{filter.log_prefix}}" {%endif%}
{% if filter.random is defined %}random="{{filter.random}}" {%endif%}
{% if filter.fragment is defined %}fragment="{{filter.fragment}}" {%endif%}
{% if filter.nth is defined %}nth="{{filter.nth}}" {%endif%}
{% if filter.reject_with is defined %}reject-with="{{filter.reject_with}}" {%endif%}] = "") do={
/ip firewall filter add chain={{filter.chain}} \
{% if filter.action is defined %}action={{filter.action}} {%endif%}
{% if filter.hotspot is defined %}hotspot={{filter.hotspot}} {%endif%}
{% if filter.out_bridge_port is defined %}out-bridge-port={{filter.out_bridge_port}} {%endif%}
{% if filter.routing_mark is defined %}routing-mark={{filter.routing_mark}} {%endif%}
{% if filter.address_list is defined %}address-list={{filter.address_list}} {%endif%}
{% if filter.icmp_options is defined %}icmp-options={{filter.icmp_options}} {%endif%}
{% if filter.out_bridge_port_list is defined %}out-bridge-port-list={{filter.out_bridge_port_list}} {%endif%}
{% if filter.routing_table is defined %}routing-table={{filter.routing_table}} {%endif%}
{% if filter.address_list_timeout is defined %}address-list-timeout={{filter.address_list_timeout}} {%endif%}
{% if filter.in_bridge_port is defined %}in-bridge-port={{filter.in_bridge_port}} {%endif%}
{% if filter.out_interface is defined %}out-interface={{filter.out_interface}} {%endif%}
{% if filter.src_address is defined %}src-address={{filter.src_address}} {%endif%}
{% if filter.comment is defined %}comment="Ansible managed: [{{filter.comment}}]" {%endif%}
{% if filter.in_bridge_port_list is defined %}in-bridge-port-list={{filter.in_bridge_port_list}} {%endif%}
{% if filter.out_interface_list is defined %}out-interface-list={{filter.out_interface_list}} {%endif%}
{% if filter.src_address_list is defined %}src-address-list={{filter.src_address_list}} {%endif%}
{% if filter.connection_bytes is defined %}connection-bytes={{filter.connection_bytes}} {%endif%}
{% if filter.connection_mark is defined %}connection-mark={{filter.connection_mark}} {%endif%}
{% if filter.connection_rate is defined %}connection-rate={{filter.connection_rate}} {%endif%}
{% if filter.connection_type is defined %}connection-type={{filter.connection_type}} {%endif%}
{% if filter.connection_limit is defined %}connection-limit={{filter.connection_limit}} {%endif%}
{% if filter.connection_nat_state is defined %}connection-nat-state={{filter.connection_nat_state}} {%endif%}
{% if filter.connection_state is defined %}connection-state={{filter.connection_state}} {%endif%}
{% if filter.in_interface is defined %}in-interface={{filter.in_interface}} {%endif%}
{% if filter.p2p is defined %}p2p={{filter.p2p}} {%endif%}
{% if filter.src_address_type is defined %}src-address-type={{filter.src_address_type}} {%endif%}
{% if filter.content is defined %}content={{filter.content}} {%endif%}
{% if filter.in_interface_list is defined %}in-interface-list={{filter.in_interface_list}} {%endif%}
{% if filter.packet_mark is defined %}packet-mark={{filter.packet_mark}} {%endif%}
{% if filter.src_mac_address is defined %}src-mac-address={{filter.src_mac_address}} {%endif%}
{% if filter.copy_from is defined %}copy-from={{filter.copy_from}} {%endif%}
{% if filter.ingress_priority is defined %}ingress-priority={{filter.ingress_priority}} {%endif%}
{% if filter.packet_size is defined %}packet-size={{filter.packet_size}} {%endif%}
{% if filter.src_port is defined %}src-port={{filter.src_port}} {%endif%}
{% if filter.disabled is defined %}disabled={{filter.disabled}} {%endif%}
{% if filter.ipsec_policy is defined %}ipsec-policy={{filter.ipsec_policy}} {%endif%}
{% if filter.per_connection_classifier is defined %}per-connection-classifier={{filter.per_connection_classifier}} {%endif%}
{% if filter.tcp_flags is defined %}tcp-flags={{filter.tcp_flags}} {%endif%}
{% if filter.dscp is defined %}dscp={{filter.dscp}} {%endif%}
{% if filter.ipv4_options is defined %}ipv4-options={{filter.ipv4_options}} {%endif%}
{% if filter.place_before is defined %}place-before={{filter.place_before}} {%endif%}
{% if filter.tcp_mss is defined %}tcp-mss={{filter.tcp_mss}} {%endif%}
{% if filter.dst_address is defined %}dst-address={{filter.dst_address}} {%endif%}
{% if filter.jump_target is defined %}jump-target={{filter.jump_target}} {%endif%}
{% if filter.port is defined %}port={{filter.port}} {%endif%}
{% if filter.time is defined %}time={{filter.time}} {%endif%}
{% if filter.dst_address_list is defined %}dst-address-list={{filter.dst_address_list}} {%endif%}
{% if filter.layer7_protocol is defined %}layer7-protocol={{filter.layer7_protocol}} {%endif%}
{% if filter.priority is defined %}priority={{filter.priority}} {%endif%}
{% if filter.ttl is defined %}ttl={{filter.ttl}} {%endif%}
{% if filter.dst_address_type is defined %}dst-address-type={{filter.dst_address_type}} {%endif%}
{% if filter.limit is defined %}limit={{filter.limit}} {%endif%}
{% if filter.protocol is defined %}protocol={{filter.protocol}} {%endif%}
{% if filter.dst_limit is defined %}dst-limit={{filter.dst_limit}} {%endif%}
{% if filter.log is defined %}log={{filter.log}} {%endif%}
{% if filter.psd is defined %}psd={{filter.psd}} {%endif%}
{% if filter.dst_port is defined %}dst-port={{filter.dst_port}} {%endif%}
{% if filter.log_prefix is defined %}log-prefix={{filter.log_prefix}} {%endif%}
{% if filter.random is defined %}random={{filter.random}} {%endif%}
{% if filter.fragment is defined %}fragment={{filter.fragment}} {%endif%}
{% if filter.nth is defined %}nth={{filter.nth}} {%endif%}
{% if filter.reject_with is defined %}reject-with={{filter.reject_with}} {%endif%}
}
{%endfor%}


File: /templates\mangle.rsc.j2
{% if  mikrotik_firewall.remove_old_mangle_rules == true %}
/ip firewall mangle remove [/ip firewall mangle find where dynamic=no]
{% endif %}
# Remove not defined
/ip firewall mangle remove [/ip firewall mangle find where !(\
{% for mangle in mikrotik_firewall.mangle_rules %}
{% if iter is defined %} or {% endif %}(chain={{mangle.chain}} \
{% if mangle.action is defined %}and action={{mangle.action}} {%endif%}
{% if mangle.in_bridge_port is defined %}and in-bridge-port={{mangle.in_bridge_port}} {%endif%}
{% if mangle.new_routing_mark is defined %}and new-routing-mark={{mangle.new_routing_mark}} {%endif%}
{% if mangle.random is defined %}and random={{mangle.random}} {%endif%}
{% if mangle.address_list is defined %}and address-list={{mangle.address_list}} {%endif%}
{% if mangle.in_bridge_port_list is defined %}and in-bridge-port-list={{mangle.in_bridge_port_list}} {%endif%}
{% if mangle.new_ttl is defined %}and new-ttl={{mangle.new_ttl}} {%endif%}
{% if mangle.route_dst is defined %}and route-dst={{mangle.route_dst}} {%endif%}
{% if mangle.address_list_timeout is defined %}and address-list-timeout={{mangle.address_list_timeout}} {%endif%}
{% if mangle.in_interface is defined %}and in-interface={{mangle.in_interface}} {%endif%}
{% if mangle.nth is defined %}and nth={{mangle.nth}} {%endif%}
{% if mangle.routing_mark is defined %}and routing-mark={{mangle.routing_mark}} {%endif%}
{% if mangle.comment is defined %}and comment="Ansible managed: [{{mangle.comment}}]" {%endif%}
{% if mangle.in_interface_list is defined %}and in-interface-list={{mangle.in_interface_list}} {%endif%}
{% if mangle.out_bridge_port is defined %}and out-bridge-port={{mangle.out_bridge_port}} {%endif%}
{% if mangle.routing_table is defined %}and routing-table={{mangle.routing_table}} {%endif%}
{% if mangle.connection_bytes is defined %}and connection-bytes={{mangle.connection_bytes}} {%endif%}
{% if mangle.connection_mark is defined %}and connection-mark={{mangle.connection_mark}} {%endif%}
{% if mangle.connection_rate is defined %}and connection-rate={{mangle.connection_rate}} {%endif%}
{% if mangle.connection_type is defined %}and connection-type={{mangle.connection_type}} {%endif%}
{% if mangle.connection_limit is defined %}and connection-limit={{mangle.connection_limit}} {%endif%}
{% if mangle.connection_nat_state is defined %}and connection-nat-state={{mangle.connection_nat_state}} {%endif%}
{% if mangle.connection_state is defined %}and connection-state={{mangle.connection_state}} {%endif%}
{% if mangle.ingress_priority is defined %}and ingress-priority={{mangle.ingress_priority}} {%endif%}
{% if mangle.out_bridge_port_list is defined %}and out-bridge-port-list={{mangle.out_bridge_port_list}} {%endif%}
{% if mangle.sniff_id is defined %}and sniff-id={{mangle.sniff_id}} {%endif%}
{% if mangle.content is defined %}and content={{mangle.content}} {%endif%}
{% if mangle.ipsec_policy is defined %}and ipsec-policy={{mangle.ipsec_policy}} {%endif%}
{% if mangle.out_interface is defined %}and out-interface={{mangle.out_interface}} {%endif%}
{% if mangle.sniff_target is defined %}and sniff-target={{mangle.sniff_target}} {%endif%}
{% if mangle.copy_from is defined %}and copy-from={{mangle.copy_from}} {%endif%}
{% if mangle.ipv4_options is defined %}and ipv4-options={{mangle.ipv4_options}} {%endif%}
{% if mangle.out_interface_list is defined %}and out-interface-list={{mangle.out_interface_list}} {%endif%}
{% if mangle.sniff_target_port is defined %}and sniff-target-port={{mangle.sniff_target_port}} {%endif%}
{% if mangle.disabled is defined %}and disabled={{mangle.disabled}} {%endif%}
{% if mangle.jump_target is defined %}and jump-target={{mangle.jump_target}} {%endif%}
{% if mangle.p2p is defined %}and p2p={{mangle.p2p}} {%endif%}
{% if mangle.src_address is defined %}and src-address={{mangle.src_address}} {%endif%}
{% if mangle.dscp is defined %}and dscp={{mangle.dscp}} {%endif%}
{% if mangle.layer7_protocol is defined %}and layer7-protocol={{mangle.layer7_protocol}} {%endif%}
{% if mangle.packet_mark is defined %}and packet-mark={{mangle.packet_mark}} {%endif%}
{% if mangle.src_address_list is defined %}and src-address-list={{mangle.src_address_list}} {%endif%}
{% if mangle.dst_address is defined %}and dst-address={{mangle.dst_address}} {%endif%}
{% if mangle.limit is defined %}and limit={{mangle.limit}} {%endif%}
{% if mangle.packet_size is defined %}and packet-size={{mangle.packet_size}} {%endif%}
{% if mangle.src_address_type is defined %}and src-address-type={{mangle.src_address_type}} {%endif%}
{% if mangle.dst_address_list is defined %}and dst-address-list={{mangle.dst_address_list}} {%endif%}
{% if mangle.log is defined %}and log={{mangle.log}} {%endif%}
{% if mangle.passthrough is defined %}and passthrough={{mangle.passthrough}} {%endif%}
{% if mangle.src_mac_address is defined %}and src-mac-address={{mangle.src_mac_address}} {%endif%}
{% if mangle.dst_address_type is defined %}and dst-address-type={{mangle.dst_address_type}} {%endif%}
{% if mangle.log_prefix is defined %}and log-prefix={{mangle.log_prefix}} {%endif%}
{% if mangle.per_connection_classifier is defined %}and per-connection-classifier={{mangle.per_connection_classifier}} {%endif%}
{% if mangle.src_port is defined %}and src-port={{mangle.src_port}} {%endif%}
{% if mangle.dst_limit is defined %}and dst-limit={{mangle.dst_limit}} {%endif%}
{% if mangle.new_connection_mark is defined %}and new-connection-mark={{mangle.new_connection_mark}} {%endif%}
{% if mangle.place_before is defined %}and place-before={{mangle.place_before}} {%endif%}
{% if mangle.tcp_flags is defined %}and tcp-flags={{mangle.tcp_flags}} {%endif%}
{% if mangle.dst_port is defined %}and dst-port={{mangle.dst_port}} {%endif%}
{% if mangle.new_dscp is defined %}and new-dscp={{mangle.new_dscp}} {%endif%}
{% if mangle.port is defined %}and port={{mangle.port}} {%endif%}
{% if mangle.tcp_mss is defined %}and tcp-mss={{mangle.tcp_mss}} {%endif%}
{% if mangle.fragment is defined %}and fragment={{mangle.fragment}} {%endif%}
{% if mangle.new_mss is defined %}and new-mss={{mangle.new_mss}} {%endif%}
{% if mangle.priority is defined %}and priority={{mangle.priority}} {%endif%}
{% if mangle.time is defined %}and time={{mangle.time}} {%endif%}
{% if mangle.hotspot is defined %}and hotspot={{mangle.hotspot}} {%endif%}
{% if mangle.new_packet_mark is defined %}and new-packet-mark={{mangle.new_packet_mark}} {%endif%}
{% if mangle.protocol is defined %}and protocol={{mangle.protocol}} {%endif%}
{% if mangle.ttl is defined %}and ttl={{mangle.ttl}} {%endif%}
{% if mangle.icmp_options is defined %}and icmp-options={{mangle.icmp_options}} {%endif%}
{% if mangle.new_priority is defined %}and new-priority={{mangle.new_priority}} {%endif%}
{% if mangle.psd is defined %}and psd={{mangle.psd}} {%endif%}
{% set iter = true %}) \
{%endfor%}
) and dynamic=no]
# Add
{% for mangle in mikrotik_firewall.mangle_rules %}
:if ([/ip firewall mangle find chain={{mangle.chain}} \
{% if mangle.action is defined %}action={{mangle.action}} {%endif%}
{% if mangle.in_bridge_port is defined %}in-bridge-port={{mangle.in_bridge_port}} {%endif%}
{% if mangle.new_routing_mark is defined %}new-routing-mark={{mangle.new_routing_mark}} {%endif%}
{% if mangle.random is defined %}random={{mangle.random}} {%endif%}
{% if mangle.address_list is defined %}address-list={{mangle.address_list}} {%endif%}
{% if mangle.in_bridge_port_list is defined %}in-bridge-port-list={{mangle.in_bridge_port_list}} {%endif%}
{% if mangle.new_ttl is defined %}new-ttl={{mangle.new_ttl}} {%endif%}
{% if mangle.route_dst is defined %}route-dst={{mangle.route_dst}} {%endif%}
{% if mangle.address_list_timeout is defined %}address-list-timeout={{mangle.address_list_timeout}} {%endif%}
{% if mangle.in_interface is defined %}in-interface={{mangle.in_interface}} {%endif%}
{% if mangle.nth is defined %}nth={{mangle.nth}} {%endif%}
{% if mangle.routing_mark is defined %}routing-mark={{mangle.routing_mark}} {%endif%}
{% if mangle.comment is defined %}comment="Ansible managed: [{{mangle.comment}}]" {%endif%}
{% if mangle.in_interface_list is defined %}in-interface-list={{mangle.in_interface_list}} {%endif%}
{% if mangle.out_bridge_port is defined %}out-bridge-port={{mangle.out_bridge_port}} {%endif%}
{% if mangle.routing_table is defined %}routing-table={{mangle.routing_table}} {%endif%}
{% if mangle.connection_bytes is defined %}connection-bytes={{mangle.connection_bytes}} {%endif%}
{% if mangle.connection_mark is defined %}connection-mark={{mangle.connection_mark}} {%endif%}
{% if mangle.connection_rate is defined %}connection-rate={{mangle.connection_rate}} {%endif%}
{% if mangle.connection_type is defined %}connection-type={{mangle.connection_type}} {%endif%}
{% if mangle.connection_limit is defined %}connection-limit={{mangle.connection_limit}} {%endif%}
{% if mangle.connection_nat_state is defined %}connection-nat-state={{mangle.connection_nat_state}} {%endif%}
{% if mangle.connection_state is defined %}connection-state={{mangle.connection_state}} {%endif%}
{% if mangle.ingress_priority is defined %}ingress-priority={{mangle.ingress_priority}} {%endif%}
{% if mangle.out_bridge_port_list is defined %}out-bridge-port-list={{mangle.out_bridge_port_list}} {%endif%}
{% if mangle.sniff_id is defined %}sniff-id={{mangle.sniff_id}} {%endif%}
{% if mangle.content is defined %}content={{mangle.content}} {%endif%}
{% if mangle.ipsec_policy is defined %}ipsec-policy={{mangle.ipsec_policy}} {%endif%}
{% if mangle.out_interface is defined %}out-interface={{mangle.out_interface}} {%endif%}
{% if mangle.sniff_target is defined %}sniff-target={{mangle.sniff_target}} {%endif%}
{% if mangle.copy_from is defined %}copy-from={{mangle.copy_from}} {%endif%}
{% if mangle.ipv4_options is defined %}ipv4-options={{mangle.ipv4_options}} {%endif%}
{% if mangle.out_interface_list is defined %}out-interface-list={{mangle.out_interface_list}} {%endif%}
{% if mangle.sniff_target_port is defined %}sniff-target-port={{mangle.sniff_target_port}} {%endif%}
{% if mangle.disabled is defined %}disabled={{mangle.disabled}} {%endif%}
{% if mangle.jump_target is defined %}jump-target={{mangle.jump_target}} {%endif%}
{% if mangle.p2p is defined %}p2p={{mangle.p2p}} {%endif%}
{% if mangle.src_address is defined %}src-address={{mangle.src_address}} {%endif%}
{% if mangle.dscp is defined %}dscp={{mangle.dscp}} {%endif%}
{% if mangle.layer7_protocol is defined %}layer7-protocol={{mangle.layer7_protocol}} {%endif%}
{% if mangle.packet_mark is defined %}packet-mark={{mangle.packet_mark}} {%endif%}
{% if mangle.src_address_list is defined %}src-address-list={{mangle.src_address_list}} {%endif%}
{% if mangle.dst_address is defined %}dst-address={{mangle.dst_address}} {%endif%}
{% if mangle.limit is defined %}limit={{mangle.limit}} {%endif%}
{% if mangle.packet_size is defined %}packet-size={{mangle.packet_size}} {%endif%}
{% if mangle.src_address_type is defined %}src-address-type={{mangle.src_address_type}} {%endif%}
{% if mangle.dst_address_list is defined %}dst-address-list={{mangle.dst_address_list}} {%endif%}
{% if mangle.log is defined %}log={{mangle.log}} {%endif%}
{% if mangle.passthrough is defined %}passthrough={{mangle.passthrough}} {%endif%}
{% if mangle.src_mac_address is defined %}src-mac-address={{mangle.src_mac_address}} {%endif%}
{% if mangle.dst_address_type is defined %}dst-address-type={{mangle.dst_address_type}} {%endif%}
{% if mangle.log_prefix is defined %}log-prefix={{mangle.log_prefix}} {%endif%}
{% if mangle.per_connection_classifier is defined %}per-connection-classifier={{mangle.per_connection_classifier}} {%endif%}
{% if mangle.src_port is defined %}src-port={{mangle.src_port}} {%endif%}
{% if mangle.dst_limit is defined %}dst-limit={{mangle.dst_limit}} {%endif%}
{% if mangle.new_connection_mark is defined %}new-connection-mark={{mangle.new_connection_mark}} {%endif%}
{% if mangle.place_before is defined %}place-before={{mangle.place_before}} {%endif%}
{% if mangle.tcp_flags is defined %}tcp-flags={{mangle.tcp_flags}} {%endif%}
{% if mangle.dst_port is defined %}dst-port={{mangle.dst_port}} {%endif%}
{% if mangle.new_dscp is defined %}new-dscp={{mangle.new_dscp}} {%endif%}
{% if mangle.port is defined %}port={{mangle.port}} {%endif%}
{% if mangle.tcp_mss is defined %}tcp-mss={{mangle.tcp_mss}} {%endif%}
{% if mangle.fragment is defined %}fragment={{mangle.fragment}} {%endif%}
{% if mangle.new_mss is defined %}new-mss={{mangle.new_mss}} {%endif%}
{% if mangle.priority is defined %}priority={{mangle.priority}} {%endif%}
{% if mangle.time is defined %}time={{mangle.time}} {%endif%}
{% if mangle.hotspot is defined %}hotspot={{mangle.hotspot}} {%endif%}
{% if mangle.new_packet_mark is defined %}new-packet-mark={{mangle.new_packet_mark}} {%endif%}
{% if mangle.protocol is defined %}protocol={{mangle.protocol}} {%endif%}
{% if mangle.ttl is defined %}ttl={{mangle.ttl}} {%endif%}
{% if mangle.icmp_options is defined %}icmp-options={{mangle.icmp_options}} {%endif%}
{% if mangle.new_priority is defined %}new-priority={{mangle.new_priority}} {%endif%}
{% if mangle.psd is defined %}psd={{mangle.psd}} {%endif%}] = "") do={
/ip firewall mangle add chain={{mangle.chain}} \
{% if mangle.action is defined %}action={{mangle.action}} {%endif%}
{% if mangle.in_bridge_port is defined %}in-bridge-port={{mangle.in_bridge_port}} {%endif%}
{% if mangle.new_routing_mark is defined %}new-routing-mark={{mangle.new_routing_mark}} {%endif%}
{% if mangle.random is defined %}random={{mangle.random}} {%endif%}
{% if mangle.address_list is defined %}address-list={{mangle.address_list}} {%endif%}
{% if mangle.in_bridge_port_list is defined %}in-bridge-port-list={{mangle.in_bridge_port_list}} {%endif%}
{% if mangle.new_ttl is defined %}new-ttl={{mangle.new_ttl}} {%endif%}
{% if mangle.route_dst is defined %}route-dst={{mangle.route_dst}} {%endif%}
{% if mangle.address_list_timeout is defined %}address-list-timeout={{mangle.address_list_timeout}} {%endif%}
{% if mangle.in_interface is defined %}in-interface={{mangle.in_interface}} {%endif%}
{% if mangle.nth is defined %}nth={{mangle.nth}} {%endif%}
{% if mangle.routing_mark is defined %}routing-mark={{mangle.routing_mark}} {%endif%}
{% if mangle.comment is defined %}comment="Ansible managed: [{{mangle.comment}}]" {%endif%}
{% if mangle.in_interface_list is defined %}in-interface-list={{mangle.in_interface_list}} {%endif%}
{% if mangle.out_bridge_port is defined %}out-bridge-port={{mangle.out_bridge_port}} {%endif%}
{% if mangle.routing_table is defined %}routing-table={{mangle.routing_table}} {%endif%}
{% if mangle.connection_bytes is defined %}connection-bytes={{mangle.connection_bytes}} {%endif%}
{% if mangle.connection_mark is defined %}connection-mark={{mangle.connection_mark}} {%endif%}
{% if mangle.connection_rate is defined %}connection-rate={{mangle.connection_rate}} {%endif%}
{% if mangle.connection_type is defined %}connection-type={{mangle.connection_type}} {%endif%}
{% if mangle.connection_limit is defined %}connection-limit={{mangle.connection_limit}} {%endif%}
{% if mangle.connection_nat_state is defined %}connection-nat-state={{mangle.connection_nat_state}} {%endif%}
{% if mangle.connection_state is defined %}connection-state={{mangle.connection_state}} {%endif%}
{% if mangle.ingress_priority is defined %}ingress-priority={{mangle.ingress_priority}} {%endif%}
{% if mangle.out_bridge_port_list is defined %}out-bridge-port-list={{mangle.out_bridge_port_list}} {%endif%}
{% if mangle.sniff_id is defined %}sniff-id={{mangle.sniff_id}} {%endif%}
{% if mangle.content is defined %}content={{mangle.content}} {%endif%}
{% if mangle.ipsec_policy is defined %}ipsec-policy={{mangle.ipsec_policy}} {%endif%}
{% if mangle.out_interface is defined %}out-interface={{mangle.out_interface}} {%endif%}
{% if mangle.sniff_target is defined %}sniff-target={{mangle.sniff_target}} {%endif%}
{% if mangle.copy_from is defined %}copy-from={{mangle.copy_from}} {%endif%}
{% if mangle.ipv4_options is defined %}ipv4-options={{mangle.ipv4_options}} {%endif%}
{% if mangle.out_interface_list is defined %}out-interface-list={{mangle.out_interface_list}} {%endif%}
{% if mangle.sniff_target_port is defined %}sniff-target-port={{mangle.sniff_target_port}} {%endif%}
{% if mangle.disabled is defined %}disabled={{mangle.disabled}} {%endif%}
{% if mangle.jump_target is defined %}jump-target={{mangle.jump_target}} {%endif%}
{% if mangle.p2p is defined %}p2p={{mangle.p2p}} {%endif%}
{% if mangle.src_address is defined %}src-address={{mangle.src_address}} {%endif%}
{% if mangle.dscp is defined %}dscp={{mangle.dscp}} {%endif%}
{% if mangle.layer7_protocol is defined %}layer7-protocol={{mangle.layer7_protocol}} {%endif%}
{% if mangle.packet_mark is defined %}packet-mark={{mangle.packet_mark}} {%endif%}
{% if mangle.src_address_list is defined %}src-address-list={{mangle.src_address_list}} {%endif%}
{% if mangle.dst_address is defined %}dst-address={{mangle.dst_address}} {%endif%}
{% if mangle.limit is defined %}limit={{mangle.limit}} {%endif%}
{% if mangle.packet_size is defined %}packet-size={{mangle.packet_size}} {%endif%}
{% if mangle.src_address_type is defined %}src-address-type={{mangle.src_address_type}} {%endif%}
{% if mangle.dst_address_list is defined %}dst-address-list={{mangle.dst_address_list}} {%endif%}
{% if mangle.log is defined %}log={{mangle.log}} {%endif%}
{% if mangle.passthrough is defined %}passthrough={{mangle.passthrough}} {%endif%}
{% if mangle.src_mac_address is defined %}src-mac-address={{mangle.src_mac_address}} {%endif%}
{% if mangle.dst_address_type is defined %}dst-address-type={{mangle.dst_address_type}} {%endif%}
{% if mangle.log_prefix is defined %}log-prefix={{mangle.log_prefix}} {%endif%}
{% if mangle.per_connection_classifier is defined %}per-connection-classifier={{mangle.per_connection_classifier}} {%endif%}
{% if mangle.src_port is defined %}src-port={{mangle.src_port}} {%endif%}
{% if mangle.dst_limit is defined %}dst-limit={{mangle.dst_limit}} {%endif%}
{% if mangle.new_connection_mark is defined %}new-connection-mark={{mangle.new_connection_mark}} {%endif%}
{% if mangle.place_before is defined %}place-before={{mangle.place_before}} {%endif%}
{% if mangle.tcp_flags is defined %}tcp-flags={{mangle.tcp_flags}} {%endif%}
{% if mangle.dst_port is defined %}dst-port={{mangle.dst_port}} {%endif%}
{% if mangle.new_dscp is defined %}new-dscp={{mangle.new_dscp}} {%endif%}
{% if mangle.port is defined %}port={{mangle.port}} {%endif%}
{% if mangle.tcp_mss is defined %}tcp-mss={{mangle.tcp_mss}} {%endif%}
{% if mangle.fragment is defined %}fragment={{mangle.fragment}} {%endif%}
{% if mangle.new_mss is defined %}new-mss={{mangle.new_mss}} {%endif%}
{% if mangle.priority is defined %}priority={{mangle.priority}} {%endif%}
{% if mangle.time is defined %}time={{mangle.time}} {%endif%}
{% if mangle.hotspot is defined %}hotspot={{mangle.hotspot}} {%endif%}
{% if mangle.new_packet_mark is defined %}new-packet-mark={{mangle.new_packet_mark}} {%endif%}
{% if mangle.protocol is defined %}protocol={{mangle.protocol}} {%endif%}
{% if mangle.ttl is defined %}ttl={{mangle.ttl}} {%endif%}
{% if mangle.icmp_options is defined %}icmp-options={{mangle.icmp_options}} {%endif%}
{% if mangle.new_priority is defined %}new-priority={{mangle.new_priority}} {%endif%}
{% if mangle.psd is defined %}psd={{mangle.psd}} {%endif%}
}
{%endfor%}


File: /templates\nat.rsc.j2
{% if  mikrotik_firewall.remove_old_nat_rules == true %}
/ip firewall nat remove [/ip firewall nat find where dynamic=no]
{% endif %}
# Remove not defined
/ip firewall nat remove [/ip firewall nat find where !(\
{% for nat in mikrotik_firewall.nat_rules %}{% if iter is defined %} or {% endif %}(chain="{{nat.chain}}" \
{% if nat.action is defined %}and action="{{nat.action}}" {%endif%}
{% if nat.hotspot is defined %}and hotspot="{{nat.hotspot}}" {%endif%}
{% if nat.out_bridge_port is defined %}and out-bridge-port="{{nat.out_bridge_port}}" {%endif%}
{% if nat.same_not_by_dst is defined %}and same-not-by-dst="{{nat.same_not_by_dst}}" {%endif%}
{% if nat.address_list is defined %}and address-list="{{nat.address_list}}" {%endif%}
{% if nat.icmp_options is defined %}and icmp-options="{{nat.icmp_options}}" {%endif%}
{% if nat.out_bridge_port_list is defined %}and out-bridge-port-list="{{nat.out_bridge_port_list}}" {%endif%}
{% if nat.src_address is defined %}and src-address="{{nat.src_address}}" {%endif%}
{% if nat.address_list_timeout is defined %}and address-list-timeout="{{nat.address_list_timeout}}" {%endif%}
{% if nat.in_bridge_port is defined %}and in-bridge-port="{{nat.in_bridge_port}}" {%endif%}
{% if nat.out_interface is defined %}and out-interface="{{nat.out_interface}}" {%endif%}
{% if nat.src_address_list is defined %}and src-address-list="{{nat.src_address_list}}" {%endif%}
{% if nat.comment is defined %}and comment="Ansible managed: [{{nat.comment}}]" {%endif%}
{% if nat.in_bridge_port_list is defined %}and in-bridge-port-list="{{nat.in_bridge_port_list}}" {%endif%}
{% if nat.out_interface_list is defined %}and out-interface-list="{{nat.out_interface_list}}" {%endif%}
{% if nat.src_address_type is defined %}and src-address-type="{{nat.src_address_type}}" {%endif%}
{% if nat.connection_bytes is defined %}and connection-bytes="{{nat.connection_bytes}}" {%endif%}
{% if nat.connection_limit is defined %}and connection-limit="{{nat.connection_limit}}" {%endif%}
{% if nat.connection_mark is defined %}and connection-mark="{{nat.connection_mark}}" {%endif%}
{% if nat.connection_rate is defined %}and connection-rate="{{nat.connection_rate}}" {%endif%}
{% if nat.connection_type is defined %}and connection-type="{{nat.connection_type}}" {%endif%}
{% if nat.in_interface is defined %}and in-interface="{{nat.in_interface}}" {%endif%}
{% if nat.packet_mark is defined %}and packet-mark="{{nat.packet_mark}}" {%endif%}
{% if nat.src_mac_address is defined %}and src-mac-address="{{nat.src_mac_address}}" {%endif%}
{% if nat.content is defined %}and content="{{nat.content}}" {%endif%}
{% if nat.in_interface_list is defined %}and in-interface-list="{{nat.in_interface_list}}" {%endif%}
{% if nat.packet_size is defined %}and packet-size="{{nat.packet_size}}" {%endif%}
{% if nat.src_port is defined %}and src-port="{{nat.src_port}}" {%endif%}
{% if nat.copy_from is defined %}and copy-from="{{nat.copy_from}}" {%endif%}
{% if nat.ingress_priority is defined %}and ingress-priority="{{nat.ingress_priority}}" {%endif%}
{% if nat.per_connection_classifier is defined %}and per-connection-classifier="{{nat.per_connection_classifier}}" {%endif%}
{% if nat.tcp_mss is defined %}and tcp-mss="{{nat.tcp_mss}}" {%endif%}
{% if nat.disabled is defined %}and disabled={{nat.disabled}} {%endif%}
{% if nat.ipsec_policy is defined %}and ipsec-policy="{{nat.ipsec_policy}}" {%endif%}
{% if nat.place_before is defined %}and place-before="{{nat.place_before}}" {%endif%}
{% if nat.time is defined %}and time="{{nat.time}}" {%endif%}
{% if nat.dscp is defined %}and dscp="{{nat.dscp}}" {%endif%}
{% if nat.ipv4_options is defined %}and ipv4-options="{{nat.ipv4_options}}" {%endif%}
{% if nat.port is defined %}and port="{{nat.port}}" {%endif%}
{% if nat.to_addresses is defined %}and to-addresses="{{nat.to_addresses}}" {%endif%}
{% if nat.dst_address is defined %}and dst-address="{{nat.dst_address}}" {%endif%}
{% if nat.jump_target is defined %}and jump-target="{{nat.jump_target}}" {%endif%}
{% if nat.priority is defined %}and priority="{{nat.priority}}" {%endif%}
{% if nat.to_ports is defined %}and to-ports="{{nat.to_ports}}" {%endif%}
{% if nat.dst_address_list is defined %}and dst-address-list="{{nat.dst_address_list}}" {%endif%}
{% if nat.layer7_protocol is defined %}and layer7-protocol="{{nat.layer7_protocol}}" {%endif%}
{% if nat.protocol is defined %}and protocol="{{nat.protocol}}" {%endif%}
{% if nat.ttl is defined %}and ttl="{{nat.ttl}}" {%endif%}
{% if nat.dst_address_type is defined %}and dst-address-type="{{nat.dst_address_type}}" {%endif%}
{% if nat.limit is defined %}and limit="{{nat.limit}}" {%endif%}
{% if nat.psd is defined %}and psd="{{nat.psd}}" {%endif%}
{% if nat.dst_limit is defined %}and dst-limit="{{nat.dst_limit}}" {%endif%}
{% if nat.log is defined %}and log="{{nat.log}}" {%endif%}
{% if nat.random is defined %}and random="{{nat.random}}" {%endif%}
{% if nat.dst_port is defined %}and dst-port="{{nat.dst_port}}" {%endif%}
{% if nat.log_prefix is defined %}and log-prefix="{{nat.log_prefix}}" {%endif%}
{% if nat.routing_mark is defined %}and routing-mark="{{nat.routing_mark}}" {%endif%}
{% if nat.fragment is defined %}and fragment="{{nat.fragment}}" {%endif%}
{% if nat.nth is defined %}and nth="{{nat.nth}}" {%endif%}
{% if nat.routing_table is defined %}and routing-table="{{nat.routing_table}}" {%endif%}) \
{% set iter = true %}
{%endfor%}
) and dynamic=no]
# ADD
{% for nat in mikrotik_firewall.nat_rules %}
:if ([/ip firewall nat find chain="{{nat.chain}}" {% if nat.action is defined %}action="{{nat.action}}" {%endif%}
{% if nat.hotspot is defined %}hotspot="{{nat.hotspot}}" {%endif%}
{% if nat.out_bridge_port is defined %}out-bridge-port="{{nat.out_bridge_port}}" {%endif%}
{% if nat.same_not_by_dst is defined %}same-not-by-dst="{{nat.same_not_by_dst}}" {%endif%}
{% if nat.address_list is defined %}address-list="{{nat.address_list}}" {%endif%}
{% if nat.icmp_options is defined %}icmp-options="{{nat.icmp_options}}" {%endif%}
{% if nat.out_bridge_port_list is defined %}out-bridge-port-list="{{nat.out_bridge_port_list}}" {%endif%}
{% if nat.src_address is defined %}src-address="{{nat.src_address}}" {%endif%}
{% if nat.address_list_timeout is defined %}address-list-timeout="{{nat.address_list_timeout}}" {%endif%}
{% if nat.in_bridge_port is defined %}in-bridge-port="{{nat.in_bridge_port}}" {%endif%}
{% if nat.out_interface is defined %}out-interface="{{nat.out_interface}}" {%endif%}
{% if nat.src_address_list is defined %}src-address-list="{{nat.src_address_list}}" {%endif%}
{% if nat.comment is defined %}comment="Ansible managed: [{{nat.comment}}]" {%endif%}
{% if nat.in_bridge_port_list is defined %}in-bridge-port-list="{{nat.in_bridge_port_list}}" {%endif%}
{% if nat.out_interface_list is defined %}out-interface-list="{{nat.out_interface_list}}" {%endif%}
{% if nat.src_address_type is defined %}src-address-type="{{nat.src_address_type}}" {%endif%}
{% if nat.connection_bytes is defined %}connection-bytes="{{nat.connection_bytes}}" {%endif%}
{% if nat.connection_limit is defined %}connection-limit="{{nat.connection_limit}}" {%endif%}
{% if nat.connection_mark is defined %}connection-mark="{{nat.connection_mark}}" {%endif%}
{% if nat.connection_rate is defined %}connection-rate="{{nat.connection_rate}}" {%endif%}
{% if nat.connection_type is defined %}connection-type="{{nat.connection_type}}" {%endif%}
{% if nat.in_interface is defined %}in-interface="{{nat.in_interface}}" {%endif%}
{% if nat.packet_mark is defined %}packet-mark="{{nat.packet_mark}}" {%endif%}
{% if nat.src_mac_address is defined %}src-mac-address="{{nat.src_mac_address}}" {%endif%}
{% if nat.content is defined %}content="{{nat.content}}" {%endif%}
{% if nat.in_interface_list is defined %}in-interface-list="{{nat.in_interface_list}}" {%endif%}
{% if nat.packet_size is defined %}packet-size="{{nat.packet_size}}" {%endif%}
{% if nat.src_port is defined %}src-port="{{nat.src_port}}" {%endif%}
{% if nat.copy_from is defined %}copy-from="{{nat.copy_from}}" {%endif%}
{% if nat.ingress_priority is defined %}ingress-priority="{{nat.ingress_priority}}" {%endif%}
{% if nat.per_connection_classifier is defined %}per-connection-classifier="{{nat.per_connection_classifier}}" {%endif%}
{% if nat.tcp_mss is defined %}tcp-mss="{{nat.tcp_mss}}" {%endif%}
{% if nat.disabled is defined %}disabled={{nat.disabled}} {%endif%}
{% if nat.ipsec_policy is defined %}ipsec-policy="{{nat.ipsec_policy}}" {%endif%}
{% if nat.place_before is defined %}place-before="{{nat.place_before}}" {%endif%}
{% if nat.time is defined %}time="{{nat.time}}" {%endif%}
{% if nat.dscp is defined %}dscp="{{nat.dscp}}" {%endif%}
{% if nat.ipv4_options is defined %}ipv4-options="{{nat.ipv4_options}}" {%endif%}
{% if nat.port is defined %}port="{{nat.port}}" {%endif%}
{% if nat.to_addresses is defined %}to-addresses="{{nat.to_addresses}}" {%endif%}
{% if nat.dst_address is defined %}dst-address="{{nat.dst_address}}" {%endif%}
{% if nat.jump_target is defined %}jump-target="{{nat.jump_target}}" {%endif%}
{% if nat.priority is defined %}priority="{{nat.priority}}" {%endif%}
{% if nat.to_ports is defined %}to-ports="{{nat.to_ports}}" {%endif%}
{% if nat.dst_address_list is defined %}dst-address-list="{{nat.dst_address_list}}" {%endif%}
{% if nat.layer7_protocol is defined %}layer7-protocol="{{nat.layer7_protocol}}" {%endif%}
{% if nat.protocol is defined %}protocol="{{nat.protocol}}" {%endif%}
{% if nat.ttl is defined %}ttl="{{nat.ttl}}" {%endif%}
{% if nat.dst_address_type is defined %}dst-address-type="{{nat.dst_address_type}}" {%endif%}
{% if nat.limit is defined %}limit="{{nat.limit}}" {%endif%}
{% if nat.psd is defined %}psd="{{nat.psd}}" {%endif%}
{% if nat.dst_limit is defined %}dst-limit="{{nat.dst_limit}}" {%endif%}
{% if nat.log is defined %}log="{{nat.log}}" {%endif%}
{% if nat.random is defined %}random="{{nat.random}}" {%endif%}
{% if nat.dst_port is defined %}dst-port="{{nat.dst_port}}" {%endif%}
{% if nat.log_prefix is defined %}log-prefix="{{nat.log_prefix}}" {%endif%}
{% if nat.routing_mark is defined %}routing-mark="{{nat.routing_mark}}" {%endif%}
{% if nat.fragment is defined %}fragment="{{nat.fragment}}" {%endif%}
{% if nat.nth is defined %}nth="{{nat.nth}}" {%endif%}
{% if nat.routing_table is defined %}routing-table="{{nat.routing_table}}" {%endif%}] = "") do={
/ip firewall nat add chain={{nat.chain}} {% if nat.action is defined %}action={{nat.action}} {%endif%}
{% if nat.hotspot is defined %}hotspot={{nat.hotspot}} {%endif%}
{% if nat.out_bridge_port is defined %}out-bridge-port={{nat.out_bridge_port}} {%endif%}
{% if nat.same_not_by_dst is defined %}same-not-by-dst={{nat.same_not_by_dst}} {%endif%}
{% if nat.address_list is defined %}address-list={{nat.address_list}} {%endif%}
{% if nat.icmp_options is defined %}icmp-options={{nat.icmp_options}} {%endif%}
{% if nat.out_bridge_port_list is defined %}out-bridge-port-list={{nat.out_bridge_port_list}} {%endif%}
{% if nat.src_address is defined %}src-address={{nat.src_address}} {%endif%}
{% if nat.address_list_timeout is defined %}address-list-timeout={{nat.address_list_timeout}} {%endif%}
{% if nat.in_bridge_port is defined %}in-bridge-port={{nat.in_bridge_port}} {%endif%}
{% if nat.out_interface is defined %}out-interface={{nat.out_interface}} {%endif%}
{% if nat.src_address_list is defined %}src-address-list={{nat.src_address_list}} {%endif%}
{% if nat.comment is defined %}comment="Ansible managed: [{{nat.comment}}]" {%endif%}
{% if nat.in_bridge_port_list is defined %}in-bridge-port-list={{nat.in_bridge_port_list}} {%endif%}
{% if nat.out_interface_list is defined %}out-interface-list={{nat.out_interface_list}} {%endif%}
{% if nat.src_address_type is defined %}src-address-type={{nat.src_address_type}} {%endif%}
{% if nat.connection_bytes is defined %}connection-bytes={{nat.connection_bytes}} {%endif%}
{% if nat.connection_limit is defined %}connection-limit={{nat.connection_limit}} {%endif%}
{% if nat.connection_mark is defined %}connection-mark={{nat.connection_mark}} {%endif%}
{% if nat.connection_rate is defined %}connection-rate={{nat.connection_rate}} {%endif%}
{% if nat.connection_type is defined %}connection-type={{nat.connection_type}} {%endif%}
{% if nat.in_interface is defined %}in-interface={{nat.in_interface}} {%endif%}
{% if nat.packet_mark is defined %}packet-mark={{nat.packet_mark}} {%endif%}
{% if nat.src_mac_address is defined %}src-mac-address={{nat.src_mac_address}} {%endif%}
{% if nat.content is defined %}content={{nat.content}} {%endif%}
{% if nat.in_interface_list is defined %}in-interface-list={{nat.in_interface_list}} {%endif%}
{% if nat.packet_size is defined %}packet-size={{nat.packet_size}} {%endif%}
{% if nat.src_port is defined %}src-port={{nat.src_port}} {%endif%}
{% if nat.copy_from is defined %}copy-from={{nat.copy_from}} {%endif%}
{% if nat.ingress_priority is defined %}ingress-priority={{nat.ingress_priority}} {%endif%}
{% if nat.per_connection_classifier is defined %}per-connection-classifier={{nat.per_connection_classifier}} {%endif%}
{% if nat.tcp_mss is defined %}tcp-mss={{nat.tcp_mss}} {%endif%}
{% if nat.disabled is defined %}disabled={{nat.disabled}} {%endif%}
{% if nat.ipsec_policy is defined %}ipsec-policy={{nat.ipsec_policy}} {%endif%}
{% if nat.place_before is defined %}place-before={{nat.place_before}} {%endif%}
{% if nat.time is defined %}time={{nat.time}} {%endif%}
{% if nat.dscp is defined %}dscp={{nat.dscp}} {%endif%}
{% if nat.ipv4_options is defined %}ipv4-options={{nat.ipv4_options}} {%endif%}
{% if nat.port is defined %}port={{nat.port}} {%endif%}
{% if nat.to_addresses is defined %}to-addresses={{nat.to_addresses}} {%endif%}
{% if nat.dst_address is defined %}dst-address={{nat.dst_address}} {%endif%}
{% if nat.jump_target is defined %}jump-target={{nat.jump_target}} {%endif%}
{% if nat.priority is defined %}priority={{nat.priority}} {%endif%}
{% if nat.to_ports is defined %}to-ports={{nat.to_ports}} {%endif%}
{% if nat.dst_address_list is defined %}dst-address-list={{nat.dst_address_list}} {%endif%}
{% if nat.layer7_protocol is defined %}layer7-protocol={{nat.layer7_protocol}} {%endif%}
{% if nat.protocol is defined %}protocol={{nat.protocol}} {%endif%}
{% if nat.ttl is defined %}ttl={{nat.ttl}} {%endif%}
{% if nat.dst_address_type is defined %}dst-address-type={{nat.dst_address_type}} {%endif%}
{% if nat.limit is defined %}limit={{nat.limit}} {%endif%}
{% if nat.psd is defined %}psd={{nat.psd}} {%endif%}
{% if nat.dst_limit is defined %}dst-limit={{nat.dst_limit}} {%endif%}
{% if nat.log is defined %}log={{nat.log}} {%endif%}
{% if nat.random is defined %}random={{nat.random}} {%endif%}
{% if nat.dst_port is defined %}dst-port={{nat.dst_port}} {%endif%}
{% if nat.log_prefix is defined %}log-prefix={{nat.log_prefix}} {%endif%}
{% if nat.routing_mark is defined %}routing-mark={{nat.routing_mark}} {%endif%}
{% if nat.fragment is defined %}fragment={{nat.fragment}} {%endif%}
{% if nat.nth is defined %}nth={{nat.nth}} {%endif%}
{% if nat.routing_table is defined %}routing-table={{nat.routing_table}} {%endif%}
}
{%endfor%}


File: /templates\raw.rsc.j2
{% if mikrotik_firewall.remove_old_raw_rules == true %}
/ip firewall raw remove [/ip firewall raw find where dynamic=no]
{% endif %}


/ip firewall raw remove [/ip firewall raw find where !(\
{% for raw in mikrotik_firewall.raw_rules %}
{% if iter is defined %} or {% endif %}(chain="{{raw.chain}}" \
{% if raw.action is defined %}and action="{{raw.action}}" {%endif%}
{% if raw.fragment is defined %}and fragment="{{raw.fragment}}" {%endif%}
{% if raw.log_prefix is defined %}and log-prefix="{{raw.log_prefix}}" {%endif%}
{% if raw.psd is defined %}and psd="{{raw.psd}}" {%endif%}
{% if raw.address_list is defined %}and address-list="{{raw.address_list}}" {%endif%}
{% if raw.hotspot is defined %}and hotspot="{{raw.hotspot}}" {%endif%}
{% if raw.nth is defined %}and nth="{{raw.nth}}" {%endif%}
{% if raw.random is defined %}and random="{{raw.random}}" {%endif%}
{% if raw.address_list_timeout is defined %}and address-list-timeout="{{raw.address_list_timeout}}" {%endif%}
{% if raw.icmp_options is defined %}and icmp-options="{{raw.icmp_options}}" {%endif%}
{% if raw.out_bridge_port is defined %}and out-bridge-port="{{raw.out_bridge_port}}" {%endif%}
{% if raw.src_address is defined %}and src-address="{{raw.src_address}}" {%endif%}
{% if raw.comment is defined %}and comment="Ansible managed: [{{raw.comment}}]" {%endif%}
{% if raw.in_bridge_port is defined %}and in-bridge-port="{{raw.in_bridge_port}}" {%endif%}
{% if raw.out_bridge_port_list is defined %}and out-bridge-port-list="{{raw.out_bridge_port_list}}" {%endif%}
{% if raw.src_address_list is defined %}and src-address-list="{{raw.src_address_list}}" {%endif%}
{% if raw.content is defined %}and content="{{raw.content}}" {%endif%}
{% if raw.in_bridge_port_list is defined %}and in-bridge-port-list="{{raw.in_bridge_port_list}}" {%endif%}
{% if raw.out_interface is defined %}and out-interface="{{raw.out_interface}}" {%endif%}
{% if raw.src_address_type is defined %}and src-address-type="{{raw.src_address_type}}" {%endif%}
{% if raw.copy_from is defined %}and copy-from="{{raw.copy_from}}" {%endif%}
{% if raw.in_interface is defined %}and in-interface="{{raw.in_interface}}" {%endif%}
{% if raw.out_interface_list is defined %}and out-interface-list="{{raw.out_interface_list}}" {%endif%}
{% if raw.src_mac_address is defined %}and src-mac-address="{{raw.src_mac_address}}" {%endif%}
{% if raw.disabled is defined %}and disabled={{raw.disabled}} {%endif%}
{% if raw.in_interface_list is defined %}and in-interface-list="{{raw.in_interface_list}}" {%endif%}
{% if raw.packet_mark is defined %}and packet-mark="{{raw.packet_mark}}" {%endif%}
{% if raw.src_port is defined %}and src-port="{{raw.src_port}}" {%endif%}
{% if raw.dscp is defined %}and dscp="{{raw.dscp}}" {%endif%}
{% if raw.ingress_priority is defined %}and ingress-priority="{{raw.ingress_priority}}" {%endif%}
{% if raw.packet_size is defined %}and packet-size="{{raw.packet_size}}" {%endif%}
{% if raw.tcp_flags is defined %}and tcp-flags="{{raw.tcp_flags}}" {%endif%}
{% if raw.dst_address is defined %}and dst-address="{{raw.dst_address}}" {%endif%}
{% if raw.ipsec_policy is defined %}and ipsec-policy="{{raw.ipsec_policy}}" {%endif%}
{% if raw.per_connection_classifier is defined %}and per-connection-classifier="{{raw.per_connection_classifier}}" {%endif%}
{% if raw.tcp_mss is defined %}and tcp-mss="{{raw.tcp_mss}}" {%endif%}
{% if raw.dst_address_list is defined %}and dst-address-list="{{raw.dst_address_list}}" {%endif%}
{% if raw.ipv4_options is defined %}and ipv4-options="{{raw.ipv4_options}}" {%endif%}
{% if raw.place_before is defined %}and place-before="{{raw.place_before}}" {%endif%}
{% if raw.time is defined %}and time="{{raw.time}}" {%endif%}
{% if raw.dst_address_type is defined %}and dst-address-type="{{raw.dst_address_type}}" {%endif%}
{% if raw.jump_target is defined %}and jump-target="{{raw.jump_target}}" {%endif%}
{% if raw.port is defined %}and port="{{raw.port}}" {%endif%}
{% if raw.ttl is defined %}and ttl="{{raw.ttl}}" {%endif%}
{% if raw.dst_limit is defined %}and dst-limit="{{raw.dst_limit}}" {%endif%}
{% if raw.limit is defined %}and limit="{{raw.limit}}" {%endif%}
{% if raw.priority is defined %}and priority="{{raw.priority}}" {%endif%}
{% if raw.dst_port is defined %}and dst-port="{{raw.dst_port}}" {%endif%}
{% if raw.log is defined %}and log="{{raw.log}}" {%endif%}
{% if raw.protocol is defined %}and protocol="{{raw.protocol}}" {%endif%}) \
{% set iter = true %}
{%endfor%}
) and dynamic=no]

{% for raw in mikrotik_firewall.raw_rules %}
:if ([/ip firewall raw find chain="{{raw.chain}}" {% if raw.action is defined %}action="{{raw.action}}" {%endif%}
{% if raw.fragment is defined %}fragment="{{raw.fragment}}" {%endif%}
{% if raw.log_prefix is defined %}log-prefix="{{raw.log_prefix}}" {%endif%}
{% if raw.psd is defined %}psd="{{raw.psd}}" {%endif%}
{% if raw.address_list is defined %}address-list="{{raw.address_list}}" {%endif%}
{% if raw.hotspot is defined %}hotspot="{{raw.hotspot}}" {%endif%}
{% if raw.nth is defined %}nth="{{raw.nth}}" {%endif%}
{% if raw.random is defined %}random="{{raw.random}}" {%endif%}
{% if raw.address_list_timeout is defined %}address-list-timeout="{{raw.address_list_timeout}}" {%endif%}
{% if raw.icmp_options is defined %}icmp-options="{{raw.icmp_options}}" {%endif%}
{% if raw.out_bridge_port is defined %}out-bridge-port="{{raw.out_bridge_port}}" {%endif%}
{% if raw.src_address is defined %}src-address="{{raw.src_address}}" {%endif%}
{% if raw.comment is defined %}comment="Ansible managed: [{{raw.comment}}]" {%endif%}
{% if raw.in_bridge_port is defined %}in-bridge-port="{{raw.in_bridge_port}}" {%endif%}
{% if raw.out_bridge_port_list is defined %}out-bridge-port-list="{{raw.out_bridge_port_list}}" {%endif%}
{% if raw.src_address_list is defined %}src-address-list="{{raw.src_address_list}}" {%endif%}
{% if raw.content is defined %}content="{{raw.content}}" {%endif%}
{% if raw.in_bridge_port_list is defined %}in-bridge-port-list="{{raw.in_bridge_port_list}}" {%endif%}
{% if raw.out_interface is defined %}out-interface="{{raw.out_interface}}" {%endif%}
{% if raw.src_address_type is defined %}src-address-type="{{raw.src_address_type}}" {%endif%}
{% if raw.copy_from is defined %}copy-from="{{raw.copy_from}}" {%endif%}
{% if raw.in_interface is defined %}in-interface="{{raw.in_interface}}" {%endif%}
{% if raw.out_interface_list is defined %}out-interface-list="{{raw.out_interface_list}}" {%endif%}
{% if raw.src_mac_address is defined %}src-mac-address="{{raw.src_mac_address}}" {%endif%}
{% if raw.disabled is defined %}disabled={{raw.disabled}} {%endif%}
{% if raw.in_interface_list is defined %}in-interface-list="{{raw.in_interface_list}}" {%endif%}
{% if raw.packet_mark is defined %}packet-mark="{{raw.packet_mark}}" {%endif%}
{% if raw.src_port is defined %}src-port="{{raw.src_port}}" {%endif%}
{% if raw.dscp is defined %}dscp="{{raw.dscp}}" {%endif%}
{% if raw.ingress_priority is defined %}ingress-priority="{{raw.ingress_priority}}" {%endif%}
{% if raw.packet_size is defined %}packet-size="{{raw.packet_size}}" {%endif%}
{% if raw.tcp_flags is defined %}tcp-flags="{{raw.tcp_flags}}" {%endif%}
{% if raw.dst_address is defined %}dst-address="{{raw.dst_address}}" {%endif%}
{% if raw.ipsec_policy is defined %}ipsec-policy="{{raw.ipsec_policy}}" {%endif%}
{% if raw.per_connection_classifier is defined %}per-connection-classifier="{{raw.per_connection_classifier}}" {%endif%}
{% if raw.tcp_mss is defined %}tcp-mss="{{raw.tcp_mss}}" {%endif%}
{% if raw.dst_address_list is defined %}dst-address-list="{{raw.dst_address_list}}" {%endif%}
{% if raw.ipv4_options is defined %}ipv4-options="{{raw.ipv4_options}}" {%endif%}
{% if raw.place_before is defined %}place-before="{{raw.place_before}}" {%endif%}
{% if raw.time is defined %}time="{{raw.time}}" {%endif%}
{% if raw.dst_address_type is defined %}dst-address-type="{{raw.dst_address_type}}" {%endif%}
{% if raw.jump_target is defined %}jump-target="{{raw.jump_target}}" {%endif%}
{% if raw.port is defined %}port="{{raw.port}}" {%endif%}
{% if raw.ttl is defined %}ttl="{{raw.ttl}}" {%endif%}
{% if raw.dst_limit is defined %}dst-limit="{{raw.dst_limit}}" {%endif%}
{% if raw.limit is defined %}limit="{{raw.limit}}" {%endif%}
{% if raw.priority is defined %}priority="{{raw.priority}}" {%endif%}
{% if raw.dst_port is defined %}dst-port="{{raw.dst_port}}" {%endif%}
{% if raw.log is defined %}log="{{raw.log}}" {%endif%}
{% if raw.protocol is defined %}protocol="{{raw.protocol}}" {%endif%}] = "") do={
/ip firewall raw add chain={{raw.chain}} {% if raw.action is defined %}action={{raw.action}} {%endif%}
{% if raw.fragment is defined %}fragment={{raw.fragment}} {%endif%}
{% if raw.log_prefix is defined %}log-prefix="{{raw.log_prefix}}" {%endif%}
{% if raw.psd is defined %}psd={{raw.psd}} {%endif%}
{% if raw.address_list is defined %}address-list={{raw.address_list}} {%endif%}
{% if raw.hotspot is defined %}hotspot={{raw.hotspot}} {%endif%}
{% if raw.nth is defined %}nth={{raw.nth}} {%endif%}
{% if raw.random is defined %}random={{raw.random}} {%endif%}
{% if raw.address_list_timeout is defined %}address-list-timeout={{raw.address_list_timeout}} {%endif%}
{% if raw.icmp_options is defined %}icmp-options={{raw.icmp_options}} {%endif%}
{% if raw.out_bridge_port is defined %}out-bridge-port={{raw.out_bridge_port}} {%endif%}
{% if raw.src_address is defined %}src-address={{raw.src_address}} {%endif%}
{% if raw.comment is defined %}comment="Ansible managed: [{{raw.comment}}]" {%endif%}
{% if raw.in_bridge_port is defined %}in-bridge-port={{raw.in_bridge_port}} {%endif%}
{% if raw.out_bridge_port_list is defined %}out-bridge-port-list={{raw.out_bridge_port_list}} {%endif%}
{% if raw.src_address_list is defined %}src-address-list={{raw.src_address_list}} {%endif%}
{% if raw.content is defined %}content={{raw.content}} {%endif%}
{% if raw.in_bridge_port_list is defined %}in-bridge-port-list={{raw.in_bridge_port_list}} {%endif%}
{% if raw.out_interface is defined %}out-interface={{raw.out_interface}} {%endif%}
{% if raw.src_address_type is defined %}src-address-type={{raw.src_address_type}} {%endif%}
{% if raw.copy_from is defined %}copy-from={{raw.copy_from}} {%endif%}
{% if raw.in_interface is defined %}in-interface={{raw.in_interface}} {%endif%}
{% if raw.out_interface_list is defined %}out-interface-list={{raw.out_interface_list}} {%endif%}
{% if raw.src_mac_address is defined %}src-mac-address={{raw.src_mac_address}} {%endif%}
{% if raw.disabled is defined %}disabled={{raw.disabled}} {%endif%}
{% if raw.in_interface_list is defined %}in-interface-list={{raw.in_interface_list}} {%endif%}
{% if raw.packet_mark is defined %}packet-mark={{raw.packet_mark}} {%endif%}
{% if raw.src_port is defined %}src-port={{raw.src_port}} {%endif%}
{% if raw.dscp is defined %}dscp={{raw.dscp}} {%endif%}
{% if raw.ingress_priority is defined %}ingress-priority={{raw.ingress_priority}} {%endif%}
{% if raw.packet_size is defined %}packet-size={{raw.packet_size}} {%endif%}
{% if raw.tcp_flags is defined %}tcp-flags={{raw.tcp_flags}} {%endif%}
{% if raw.dst_address is defined %}dst-address={{raw.dst_address}} {%endif%}
{% if raw.ipsec_policy is defined %}ipsec-policy={{raw.ipsec_policy}} {%endif%}
{% if raw.per_connection_classifier is defined %}per-connection-classifier={{raw.per_connection_classifier}} {%endif%}
{% if raw.tcp_mss is defined %}tcp-mss={{raw.tcp_mss}} {%endif%}
{% if raw.dst_address_list is defined %}dst-address-list={{raw.dst_address_list}} {%endif%}
{% if raw.ipv4_options is defined %}ipv4-options={{raw.ipv4_options}} {%endif%}
{% if raw.place_before is defined %}place-before={{raw.place_before}} {%endif%}
{% if raw.time is defined %}time={{raw.time}} {%endif%}
{% if raw.dst_address_type is defined %}dst-address-type={{raw.dst_address_type}} {%endif%}
{% if raw.jump_target is defined %}jump-target={{raw.jump_target}} {%endif%}
{% if raw.port is defined %}port={{raw.port}} {%endif%}
{% if raw.ttl is defined %}ttl={{raw.ttl}} {%endif%}
{% if raw.dst_limit is defined %}dst-limit={{raw.dst_limit}} {%endif%}
{% if raw.limit is defined %}limit={{raw.limit}} {%endif%}
{% if raw.priority is defined %}priority={{raw.priority}} {%endif%}
{% if raw.dst_port is defined %}dst-port={{raw.dst_port}} {%endif%}
{% if raw.log is defined %}log={{raw.log}} {%endif%}
{% if raw.protocol is defined %}protocol={{raw.protocol}} {%endif%}
}
{%endfor%}


File: /templates\services.rsc.j2
{% for service in mikrotik_firewall.service_port_rules %}
:if ([/ip firewall service-port find name={{service.name}} disabled={{service.disabled}}\
{% if service.sip_direct_media is defined %}
 sip-direct-media={{service.sip_direct_media}}\
{% endif %}
{% if service.ports is defined %}
 ports={{service.ports}}\
{% endif %}
] ="") do={
/ip firewall service-port set {{service.name}} disabled={{service.disabled}} \
{% if service.sip_direct_media is defined %}sip-direct-media={{service.sip_direct_media}} \{% endif %}
{% if service.ports is defined %}ports={{service.ports}}{% endif %}
}
{% endfor %}



File: /tests\inventory
localhost



File: /tests\test.yml
---
- hosts: localhost
  remote_user: root
  roles:
    - mikrotik-firewall

File: /vars\main.yml
---
# vars file for mikrotik-firewall

