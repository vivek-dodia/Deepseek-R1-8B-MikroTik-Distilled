# Repository Information
Name: mikrotik_dhcp_lease_check

# Directory Structure
Directory structure:
└── github_repos/mikrotik_dhcp_lease_check/
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
    │   │       ├── pack-d75b8e1344de646dc098441c5a3f708980e570a6.idx
    │   │       └── pack-d75b8e1344de646dc098441c5a3f708980e570a6.pack
    │   ├── packed-refs
    │   └── refs/
    │       ├── heads/
    │       │   └── master
    │       ├── remotes/
    │       │   └── origin/
    │       │       └── HEAD
    │       └── tags/
    ├── assets/
    │   ├── css/
    │   │   └── style.css
    │   └── js/
    ├── composer.json
    ├── composer.lock
    ├── index.html
    ├── server.php
    └── vendor/
        ├── autoload.php
        ├── composer/
        │   ├── autoload_classmap.php
        │   ├── autoload_namespaces.php
        │   ├── autoload_psr4.php
        │   ├── autoload_real.php
        │   ├── autoload_static.php
        │   ├── ClassLoader.php
        │   ├── installed.json
        │   └── LICENSE
        └── evilfreelancer/
            └── routeros-api-php/
                ├── .codeclimate.yml
                ├── .github/
                │   ├── FUNDING.yml
                │   └── ISSUE_TEMPLATE/
                │       └── bug_report.md
                ├── .gitignore
                ├── .scrutinizer.yml
                ├── .travis.yml
                ├── composer.json
                ├── examples/
                │   ├── bridge_hosts.php
                │   ├── different_queries.php
                │   ├── export.php
                │   ├── hotspot.php
                │   ├── interface_print.php
                │   ├── ip_address_print.php
                │   ├── ip_filrewall_address-list_print.php
                │   ├── queue_simple_print.php
                │   ├── queue_simple_print_v2.php
                │   ├── queue_simple_write.php
                │   ├── system_package_print.php
                │   ├── vlans_bridge.php
                │   ├── vlans_bridge_v2.php
                │   └── vlans_bridge_v3.php
                ├── FUNDING.yml
                ├── LICENSE
                ├── phpunit.xml
                ├── preconf.tcl
                ├── README.md
                ├── src/
                │   ├── APIConnector.php
                │   ├── APILengthCoDec.php
                │   ├── Client.php
                │   ├── Config.php
                │   ├── Exceptions/
                │   │   ├── ClientException.php
                │   │   ├── ConfigException.php
                │   │   ├── QueryException.php
                │   │   └── StreamException.php
                │   ├── Helpers/
                │   │   ├── ArrayHelper.php
                │   │   ├── BinaryStringHelper.php
                │   │   └── TypeHelper.php
                │   ├── Interfaces/
                │   │   ├── ClientInterface.php
                │   │   ├── ConfigInterface.php
                │   │   ├── QueryInterface.php
                │   │   └── StreamInterface.php
                │   ├── Query.php
                │   ├── ResponseIterator.php
                │   ├── ShortsTrait.php
                │   ├── SocketTrait.php
                │   └── Streams/
                │       ├── ResourceStream.php
                │       └── StringStream.php
                └── tests/
                    ├── APIConnectorTest.php
                    ├── APILengthCoDecTest.php
                    ├── ClientTest.php
                    ├── ConfigTest.php
                    ├── Helpers/
                    │   ├── ArrayHelperTest.php
                    │   ├── BinaryStringHelperTest.php
                    │   └── TypeHelperTest.php
                    ├── QueryTest.php
                    ├── ResponseIteratorTest.php
                    └── Streams/
                        ├── ResourceStreamTest.php
                        └── StringStreamTest.php


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
	url = https://github.com/paradoxicalx/mikrotik_dhcp_lease_check.git
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
0000000000000000000000000000000000000000 9c0499bea43dfaf6b615020c58d212c08307b122 vivek-dodia <vivek.dodia@icloud.com> 1738606363 -0500	clone: from https://github.com/paradoxicalx/mikrotik_dhcp_lease_check.git


File: /.git\logs\refs\heads\master
0000000000000000000000000000000000000000 9c0499bea43dfaf6b615020c58d212c08307b122 vivek-dodia <vivek.dodia@icloud.com> 1738606363 -0500	clone: from https://github.com/paradoxicalx/mikrotik_dhcp_lease_check.git


File: /.git\logs\refs\remotes\origin\HEAD
0000000000000000000000000000000000000000 9c0499bea43dfaf6b615020c58d212c08307b122 vivek-dodia <vivek.dodia@icloud.com> 1738606363 -0500	clone: from https://github.com/paradoxicalx/mikrotik_dhcp_lease_check.git


File: /.git\packed-refs
# pack-refs with: peeled fully-peeled sorted 
9c0499bea43dfaf6b615020c58d212c08307b122 refs/remotes/origin/master


File: /.git\refs\heads\master
9c0499bea43dfaf6b615020c58d212c08307b122


File: /.git\refs\remotes\origin\HEAD
ref: refs/remotes/origin/master


File: /assets\css\style.css
footer {
  position:absolute;
  bottom:0;
  width:100%;
  background:#6cf;
}

.jumbotron {
  background-image: linear-gradient(-60deg, #6c3 30%, #09f 30%);
}

.jumbotron {
  overflow: hidden;
  position: relative;
}

.jumbotron img {
  transform: rotate(-20deg);
  -moz-transform: rotate(-20deg);
  -webkit-transform: rotate(-20deg);
  position: absolute;
  left: 63%;
  top: 20%;
  margin: -100px 0 0 -150px;
}


File: /composer.json
{
    "name": "paradoxical/dhcp-look",
    "authors": [
        {
            "name": "paradoxicalx",
            "email": "paradoxical.attack@gmail.com"
        }
    ],
    "require": {}
}


File: /composer.lock
{
    "_readme": [
        "This file locks the dependencies of your project to a known state",
        "Read more about it at https://getcomposer.org/doc/01-basic-usage.md#installing-dependencies",
        "This file is @generated automatically"
    ],
    "content-hash": "1395b2d11efff7d69f5a5a2ddc6ccdb1",
    "packages": [
        {
            "name": "evilfreelancer/routeros-api-php",
            "version": "1.1",
            "source": {
                "type": "git",
                "url": "https://github.com/EvilFreelancer/routeros-api-php.git",
                "reference": "b0fc409ead43b11fb3c5322a38695eb728d81a5c"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/EvilFreelancer/routeros-api-php/zipball/b0fc409ead43b11fb3c5322a38695eb728d81a5c",
                "reference": "b0fc409ead43b11fb3c5322a38695eb728d81a5c",
                "shasum": ""
            },
            "require": {
                "ext-sockets": "*",
                "php": "^7.1"
            },
            "require-dev": {
                "phpunit/phpunit": "^7.0"
            },
            "type": "library",
            "autoload": {
                "psr-4": {
                    "RouterOS\\": "./src/"
                }
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "Paul Rock",
                    "email": "paul@drteam.rocks",
                    "homepage": "http://drteam.rocks/",
                    "role": "Developer"
                }
            ],
            "description": "Modern Mikrotik RouterOS API PHP7 client for your applications",
            "keywords": [
                "PSR-4",
                "mikrotik",
                "routeros",
                "socket-client"
            ],
            "time": "2019-09-24T18:11:06+00:00"
        }
    ],
    "packages-dev": [],
    "aliases": [],
    "minimum-stability": "stable",
    "stability-flags": [],
    "prefer-stable": false,
    "prefer-lowest": false,
    "platform": [],
    "platform-dev": []
}


File: /index.html
<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <link rel="stylesheet" href="assets/css/bootstrap.min.css">
    <link rel="stylesheet" href="assets/css/style.css">
    <title>DHCP Status Check</title>
  </head>
  <body>
    <div class="container">
      <button type="button" id="reload" class="btn btn-success my-4">Refresh</button>
      <div class="d-flex align-items-center mb-4">
        <strong class="loading" style="display:none;">Getting data. Please wait ...</strong>
        <div class="loading spinner-border ml-auto text-info" role="status" aria-hidden="true" style="display:none;"></div>
      </div>
      <table class="table">
        <thead class="thead-dark">
          <tr>
            <th scope="col">Address</th>
            <th scope="col">Comment</th>
            <th scope="col">Mac Address</th>
            <th scope="col">Host</th>
            <th scope="col">Status</th>
          </tr>
        </thead>
        <tbody id='tblbbody'>
        </tbody>
      </table>
    </div>

    <script src="assets/js/jquery-3.4.1.min.js" ></script>
    <script src="assets/js/bootstrap.bundle.min.js" ></script>

    <script type="text/javascript">
    $( document ).ready(function() {
      $('#reload').on('click', function() {
        $('.loading').show()
        $.get( "server.php", function( data ) {
          $('#tblbbody').html('')
          for (var i = 0; i < data.length; i++) {

            if (data[i].ping !== null) {
              var status = "<span class='badge badge-success'>Online</span>";
            } else {
              var status = "<span class='badge badge-danger'>Offline</span>";
            }

            if (data[i].comment !== null) {
              var comment = data[i].comment;
            } else {
              var comment = '';
            }

            $('#tblbbody').append("<tr> <th scope='row'>"+data[i].address+"</th> <td>"+comment+"</td> <td>"+data[i].macaddress+"</td> <td>"+data[i].host+"</td> <td>"+status+"</td> </tr>")
          }
          $('.loading').hide()
        });
      })
      $('#reload').click()
    });
    </script>

  </body>
</html>

<!-- https://api.github.com/repos/paradoxicalx/WaveApps-v1/branches -->


File: /server.php
<?php
require_once __DIR__ . '/vendor/autoload.php';

use \RouterOS\Client;
use \RouterOS\Query;

error_reporting(0);

// Initiate client with config object
$client = new Client([
    'host' => '192.168.0.1',
    'user' => 'user',
    'pass' => 'password'
]);

$lease = $client->query('/ip/dhcp-server/lease/print')->read();
$collect = [];

foreach ($lease as $key => $value) {
  $query = new Query('/ping');
  $query->equal('address', $lease[$key]['address']);
  $query->equal('count', '1');
  $response = $client->query($query)->read();

  $collect[] = [
    'address' => $lease[$key]['address'],
    'comment' => $lease[$key]['comment'],
    'macaddress' => $lease[$key]['mac-address'],
    'host' => $lease[$key]['host-name'],
    'ping' => $response[0]['time'],
  ];

}

header('Content-Type: application/json');
echo json_encode($collect);

?>


File: /vendor\autoload.php
<?php

// autoload.php @generated by Composer

require_once __DIR__ . '/composer/autoload_real.php';

return ComposerAutoloaderInit0f3389e5f3b13854db766a236bd7e2af::getLoader();


File: /vendor\composer\autoload_classmap.php
<?php

// autoload_classmap.php @generated by Composer

$vendorDir = dirname(dirname(__FILE__));
$baseDir = dirname($vendorDir);

return array(
);


File: /vendor\composer\autoload_namespaces.php
<?php

// autoload_namespaces.php @generated by Composer

$vendorDir = dirname(dirname(__FILE__));
$baseDir = dirname($vendorDir);

return array(
);


File: /vendor\composer\autoload_psr4.php
<?php

// autoload_psr4.php @generated by Composer

$vendorDir = dirname(dirname(__FILE__));
$baseDir = dirname($vendorDir);

return array(
    'RouterOS\\' => array($vendorDir . '/evilfreelancer/routeros-api-php/src'),
);


File: /vendor\composer\autoload_real.php
<?php

// autoload_real.php @generated by Composer

class ComposerAutoloaderInit0f3389e5f3b13854db766a236bd7e2af
{
    private static $loader;

    public static function loadClassLoader($class)
    {
        if ('Composer\Autoload\ClassLoader' === $class) {
            require __DIR__ . '/ClassLoader.php';
        }
    }

    public static function getLoader()
    {
        if (null !== self::$loader) {
            return self::$loader;
        }

        spl_autoload_register(array('ComposerAutoloaderInit0f3389e5f3b13854db766a236bd7e2af', 'loadClassLoader'), true, true);
        self::$loader = $loader = new \Composer\Autoload\ClassLoader();
        spl_autoload_unregister(array('ComposerAutoloaderInit0f3389e5f3b13854db766a236bd7e2af', 'loadClassLoader'));

        $useStaticLoader = PHP_VERSION_ID >= 50600 && !defined('HHVM_VERSION') && (!function_exists('zend_loader_file_encoded') || !zend_loader_file_encoded());
        if ($useStaticLoader) {
            require_once __DIR__ . '/autoload_static.php';

            call_user_func(\Composer\Autoload\ComposerStaticInit0f3389e5f3b13854db766a236bd7e2af::getInitializer($loader));
        } else {
            $map = require __DIR__ . '/autoload_namespaces.php';
            foreach ($map as $namespace => $path) {
                $loader->set($namespace, $path);
            }

            $map = require __DIR__ . '/autoload_psr4.php';
            foreach ($map as $namespace => $path) {
                $loader->setPsr4($namespace, $path);
            }

            $classMap = require __DIR__ . '/autoload_classmap.php';
            if ($classMap) {
                $loader->addClassMap($classMap);
            }
        }

        $loader->register(true);

        return $loader;
    }
}


File: /vendor\composer\autoload_static.php
<?php

// autoload_static.php @generated by Composer

namespace Composer\Autoload;

class ComposerStaticInit0f3389e5f3b13854db766a236bd7e2af
{
    public static $prefixLengthsPsr4 = array (
        'R' => 
        array (
            'RouterOS\\' => 9,
        ),
    );

    public static $prefixDirsPsr4 = array (
        'RouterOS\\' => 
        array (
            0 => __DIR__ . '/..' . '/evilfreelancer/routeros-api-php/src',
        ),
    );

    public static function getInitializer(ClassLoader $loader)
    {
        return \Closure::bind(function () use ($loader) {
            $loader->prefixLengthsPsr4 = ComposerStaticInit0f3389e5f3b13854db766a236bd7e2af::$prefixLengthsPsr4;
            $loader->prefixDirsPsr4 = ComposerStaticInit0f3389e5f3b13854db766a236bd7e2af::$prefixDirsPsr4;

        }, null, ClassLoader::class);
    }
}


File: /vendor\composer\ClassLoader.php
<?php

/*
 * This file is part of Composer.
 *
 * (c) Nils Adermann <naderman@naderman.de>
 *     Jordi Boggiano <j.boggiano@seld.be>
 *
 * For the full copyright and license information, please view the LICENSE
 * file that was distributed with this source code.
 */

namespace Composer\Autoload;

/**
 * ClassLoader implements a PSR-0, PSR-4 and classmap class loader.
 *
 *     $loader = new \Composer\Autoload\ClassLoader();
 *
 *     // register classes with namespaces
 *     $loader->add('Symfony\Component', __DIR__.'/component');
 *     $loader->add('Symfony',           __DIR__.'/framework');
 *
 *     // activate the autoloader
 *     $loader->register();
 *
 *     // to enable searching the include path (eg. for PEAR packages)
 *     $loader->setUseIncludePath(true);
 *
 * In this example, if you try to use a class in the Symfony\Component
 * namespace or one of its children (Symfony\Component\Console for instance),
 * the autoloader will first look for the class under the component/
 * directory, and it will then fallback to the framework/ directory if not
 * found before giving up.
 *
 * This class is loosely based on the Symfony UniversalClassLoader.
 *
 * @author Fabien Potencier <fabien@symfony.com>
 * @author Jordi Boggiano <j.boggiano@seld.be>
 * @see    http://www.php-fig.org/psr/psr-0/
 * @see    http://www.php-fig.org/psr/psr-4/
 */
class ClassLoader
{
    // PSR-4
    private $prefixLengthsPsr4 = array();
    private $prefixDirsPsr4 = array();
    private $fallbackDirsPsr4 = array();

    // PSR-0
    private $prefixesPsr0 = array();
    private $fallbackDirsPsr0 = array();

    private $useIncludePath = false;
    private $classMap = array();
    private $classMapAuthoritative = false;
    private $missingClasses = array();
    private $apcuPrefix;

    public function getPrefixes()
    {
        if (!empty($this->prefixesPsr0)) {
            return call_user_func_array('array_merge', $this->prefixesPsr0);
        }

        return array();
    }

    public function getPrefixesPsr4()
    {
        return $this->prefixDirsPsr4;
    }

    public function getFallbackDirs()
    {
        return $this->fallbackDirsPsr0;
    }

    public function getFallbackDirsPsr4()
    {
        return $this->fallbackDirsPsr4;
    }

    public function getClassMap()
    {
        return $this->classMap;
    }

    /**
     * @param array $classMap Class to filename map
     */
    public function addClassMap(array $classMap)
    {
        if ($this->classMap) {
            $this->classMap = array_merge($this->classMap, $classMap);
        } else {
            $this->classMap = $classMap;
        }
    }

    /**
     * Registers a set of PSR-0 directories for a given prefix, either
     * appending or prepending to the ones previously set for this prefix.
     *
     * @param string       $prefix  The prefix
     * @param array|string $paths   The PSR-0 root directories
     * @param bool         $prepend Whether to prepend the directories
     */
    public function add($prefix, $paths, $prepend = false)
    {
        if (!$prefix) {
            if ($prepend) {
                $this->fallbackDirsPsr0 = array_merge(
                    (array) $paths,
                    $this->fallbackDirsPsr0
                );
            } else {
                $this->fallbackDirsPsr0 = array_merge(
                    $this->fallbackDirsPsr0,
                    (array) $paths
                );
            }

            return;
        }

        $first = $prefix[0];
        if (!isset($this->prefixesPsr0[$first][$prefix])) {
            $this->prefixesPsr0[$first][$prefix] = (array) $paths;

            return;
        }
        if ($prepend) {
            $this->prefixesPsr0[$first][$prefix] = array_merge(
                (array) $paths,
                $this->prefixesPsr0[$first][$prefix]
            );
        } else {
            $this->prefixesPsr0[$first][$prefix] = array_merge(
                $this->prefixesPsr0[$first][$prefix],
                (array) $paths
            );
        }
    }

    /**
     * Registers a set of PSR-4 directories for a given namespace, either
     * appending or prepending to the ones previously set for this namespace.
     *
     * @param string       $prefix  The prefix/namespace, with trailing '\\'
     * @param array|string $paths   The PSR-4 base directories
     * @param bool         $prepend Whether to prepend the directories
     *
     * @throws \InvalidArgumentException
     */
    public function addPsr4($prefix, $paths, $prepend = false)
    {
        if (!$prefix) {
            // Register directories for the root namespace.
            if ($prepend) {
                $this->fallbackDirsPsr4 = array_merge(
                    (array) $paths,
                    $this->fallbackDirsPsr4
                );
            } else {
                $this->fallbackDirsPsr4 = array_merge(
                    $this->fallbackDirsPsr4,
                    (array) $paths
                );
            }
        } elseif (!isset($this->prefixDirsPsr4[$prefix])) {
            // Register directories for a new namespace.
            $length = strlen($prefix);
            if ('\\' !== $prefix[$length - 1]) {
                throw new \InvalidArgumentException("A non-empty PSR-4 prefix must end with a namespace separator.");
            }
            $this->prefixLengthsPsr4[$prefix[0]][$prefix] = $length;
            $this->prefixDirsPsr4[$prefix] = (array) $paths;
        } elseif ($prepend) {
            // Prepend directories for an already registered namespace.
            $this->prefixDirsPsr4[$prefix] = array_merge(
                (array) $paths,
                $this->prefixDirsPsr4[$prefix]
            );
        } else {
            // Append directories for an already registered namespace.
            $this->prefixDirsPsr4[$prefix] = array_merge(
                $this->prefixDirsPsr4[$prefix],
                (array) $paths
            );
        }
    }

    /**
     * Registers a set of PSR-0 directories for a given prefix,
     * replacing any others previously set for this prefix.
     *
     * @param string       $prefix The prefix
     * @param array|string $paths  The PSR-0 base directories
     */
    public function set($prefix, $paths)
    {
        if (!$prefix) {
            $this->fallbackDirsPsr0 = (array) $paths;
        } else {
            $this->prefixesPsr0[$prefix[0]][$prefix] = (array) $paths;
        }
    }

    /**
     * Registers a set of PSR-4 directories for a given namespace,
     * replacing any others previously set for this namespace.
     *
     * @param string       $prefix The prefix/namespace, with trailing '\\'
     * @param array|string $paths  The PSR-4 base directories
     *
     * @throws \InvalidArgumentException
     */
    public function setPsr4($prefix, $paths)
    {
        if (!$prefix) {
            $this->fallbackDirsPsr4 = (array) $paths;
        } else {
            $length = strlen($prefix);
            if ('\\' !== $prefix[$length - 1]) {
                throw new \InvalidArgumentException("A non-empty PSR-4 prefix must end with a namespace separator.");
            }
            $this->prefixLengthsPsr4[$prefix[0]][$prefix] = $length;
            $this->prefixDirsPsr4[$prefix] = (array) $paths;
        }
    }

    /**
     * Turns on searching the include path for class files.
     *
     * @param bool $useIncludePath
     */
    public function setUseIncludePath($useIncludePath)
    {
        $this->useIncludePath = $useIncludePath;
    }

    /**
     * Can be used to check if the autoloader uses the include path to check
     * for classes.
     *
     * @return bool
     */
    public function getUseIncludePath()
    {
        return $this->useIncludePath;
    }

    /**
     * Turns off searching the prefix and fallback directories for classes
     * that have not been registered with the class map.
     *
     * @param bool $classMapAuthoritative
     */
    public function setClassMapAuthoritative($classMapAuthoritative)
    {
        $this->classMapAuthoritative = $classMapAuthoritative;
    }

    /**
     * Should class lookup fail if not found in the current class map?
     *
     * @return bool
     */
    public function isClassMapAuthoritative()
    {
        return $this->classMapAuthoritative;
    }

    /**
     * APCu prefix to use to cache found/not-found classes, if the extension is enabled.
     *
     * @param string|null $apcuPrefix
     */
    public function setApcuPrefix($apcuPrefix)
    {
        $this->apcuPrefix = function_exists('apcu_fetch') && filter_var(ini_get('apc.enabled'), FILTER_VALIDATE_BOOLEAN) ? $apcuPrefix : null;
    }

    /**
     * The APCu prefix in use, or null if APCu caching is not enabled.
     *
     * @return string|null
     */
    public function getApcuPrefix()
    {
        return $this->apcuPrefix;
    }

    /**
     * Registers this instance as an autoloader.
     *
     * @param bool $prepend Whether to prepend the autoloader or not
     */
    public function register($prepend = false)
    {
        spl_autoload_register(array($this, 'loadClass'), true, $prepend);
    }

    /**
     * Unregisters this instance as an autoloader.
     */
    public function unregister()
    {
        spl_autoload_unregister(array($this, 'loadClass'));
    }

    /**
     * Loads the given class or interface.
     *
     * @param  string    $class The name of the class
     * @return bool|null True if loaded, null otherwise
     */
    public function loadClass($class)
    {
        if ($file = $this->findFile($class)) {
            includeFile($file);

            return true;
        }
    }

    /**
     * Finds the path to the file where the class is defined.
     *
     * @param string $class The name of the class
     *
     * @return string|false The path if found, false otherwise
     */
    public function findFile($class)
    {
        // class map lookup
        if (isset($this->classMap[$class])) {
            return $this->classMap[$class];
        }
        if ($this->classMapAuthoritative || isset($this->missingClasses[$class])) {
            return false;
        }
        if (null !== $this->apcuPrefix) {
            $file = apcu_fetch($this->apcuPrefix.$class, $hit);
            if ($hit) {
                return $file;
            }
        }

        $file = $this->findFileWithExtension($class, '.php');

        // Search for Hack files if we are running on HHVM
        if (false === $file && defined('HHVM_VERSION')) {
            $file = $this->findFileWithExtension($class, '.hh');
        }

        if (null !== $this->apcuPrefix) {
            apcu_add($this->apcuPrefix.$class, $file);
        }

        if (false === $file) {
            // Remember that this class does not exist.
            $this->missingClasses[$class] = true;
        }

        return $file;
    }

    private function findFileWithExtension($class, $ext)
    {
        // PSR-4 lookup
        $logicalPathPsr4 = strtr($class, '\\', DIRECTORY_SEPARATOR) . $ext;

        $first = $class[0];
        if (isset($this->prefixLengthsPsr4[$first])) {
            $subPath = $class;
            while (false !== $lastPos = strrpos($subPath, '\\')) {
                $subPath = substr($subPath, 0, $lastPos);
                $search = $subPath . '\\';
                if (isset($this->prefixDirsPsr4[$search])) {
                    $pathEnd = DIRECTORY_SEPARATOR . substr($logicalPathPsr4, $lastPos + 1);
                    foreach ($this->prefixDirsPsr4[$search] as $dir) {
                        if (file_exists($file = $dir . $pathEnd)) {
                            return $file;
                        }
                    }
                }
            }
        }

        // PSR-4 fallback dirs
        foreach ($this->fallbackDirsPsr4 as $dir) {
            if (file_exists($file = $dir . DIRECTORY_SEPARATOR . $logicalPathPsr4)) {
                return $file;
            }
        }

        // PSR-0 lookup
        if (false !== $pos = strrpos($class, '\\')) {
            // namespaced class name
            $logicalPathPsr0 = substr($logicalPathPsr4, 0, $pos + 1)
                . strtr(substr($logicalPathPsr4, $pos + 1), '_', DIRECTORY_SEPARATOR);
        } else {
            // PEAR-like class name
            $logicalPathPsr0 = strtr($class, '_', DIRECTORY_SEPARATOR) . $ext;
        }

        if (isset($this->prefixesPsr0[$first])) {
            foreach ($this->prefixesPsr0[$first] as $prefix => $dirs) {
                if (0 === strpos($class, $prefix)) {
                    foreach ($dirs as $dir) {
                        if (file_exists($file = $dir . DIRECTORY_SEPARATOR . $logicalPathPsr0)) {
                            return $file;
                        }
                    }
                }
            }
        }

        // PSR-0 fallback dirs
        foreach ($this->fallbackDirsPsr0 as $dir) {
            if (file_exists($file = $dir . DIRECTORY_SEPARATOR . $logicalPathPsr0)) {
                return $file;
            }
        }

        // PSR-0 include paths.
        if ($this->useIncludePath && $file = stream_resolve_include_path($logicalPathPsr0)) {
            return $file;
        }

        return false;
    }
}

/**
 * Scope isolated include.
 *
 * Prevents access to $this/self from included files.
 */
function includeFile($file)
{
    include $file;
}


File: /vendor\composer\installed.json
[
    {
        "name": "evilfreelancer/routeros-api-php",
        "version": "1.1",
        "version_normalized": "1.1.0.0",
        "source": {
            "type": "git",
            "url": "https://github.com/EvilFreelancer/routeros-api-php.git",
            "reference": "b0fc409ead43b11fb3c5322a38695eb728d81a5c"
        },
        "dist": {
            "type": "zip",
            "url": "https://api.github.com/repos/EvilFreelancer/routeros-api-php/zipball/b0fc409ead43b11fb3c5322a38695eb728d81a5c",
            "reference": "b0fc409ead43b11fb3c5322a38695eb728d81a5c",
            "shasum": ""
        },
        "require": {
            "ext-sockets": "*",
            "php": "^7.1"
        },
        "require-dev": {
            "phpunit/phpunit": "^7.0"
        },
        "time": "2019-09-24T18:11:06+00:00",
        "type": "library",
        "installation-source": "dist",
        "autoload": {
            "psr-4": {
                "RouterOS\\": "./src/"
            }
        },
        "notification-url": "https://packagist.org/downloads/",
        "license": [
            "MIT"
        ],
        "authors": [
            {
                "name": "Paul Rock",
                "email": "paul@drteam.rocks",
                "homepage": "http://drteam.rocks/",
                "role": "Developer"
            }
        ],
        "description": "Modern Mikrotik RouterOS API PHP7 client for your applications",
        "keywords": [
            "PSR-4",
            "mikrotik",
            "routeros",
            "socket-client"
        ]
    }
]


File: /vendor\composer\LICENSE

Copyright (c) Nils Adermann, Jordi Boggiano

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is furnished
to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.



File: /vendor\evilfreelancer\routeros-api-php\.codeclimate.yml
excluded_paths:
- "examples/"
- "tests/"


File: /vendor\evilfreelancer\routeros-api-php\.github\FUNDING.yml
# These are supported funding model platforms

patreon: efreelancer # Replace with a single Patreon username


File: /vendor\evilfreelancer\routeros-api-php\.github\ISSUE_TEMPLATE\bug_report.md
---
name: Bug report
about: Create a report to help us improve
title: ''
labels: bug
assignees: EvilFreelancer

---

**Version of RouterOS**
Please describe on which version of RouterOS your issue is occurring.

**To Reproduce**
Sample of code to reproduce the behavior.

**Expected behavior**
A clear and concise description of what you expected to happen.


File: /vendor\evilfreelancer\routeros-api-php\.gitignore
File: /vendor\evilfreelancer\routeros-api-php\.scrutinizer.yml
checks:
  php: true

filter:
  excluded_paths:
  - "examples/"
  - "tests/"

coding_style:
  php:
    spaces:
      around_operators:
        concatenation: true

tools:
  external_code_coverage: true


File: /vendor\evilfreelancer\routeros-api-php\.travis.yml
sudo: required

services:
- docker

language: php

addons:
  apt:
    packages:
    - expect

php:
- '7.1'
- '7.2'
- '7.3'

before_script:
- sudo apt-get update
- sudo apt-get install -y expect
- docker pull evilfreelancer/docker-routeros:6.42
- docker pull evilfreelancer/docker-routeros:latest
- docker run -d -p 12223:23 -p 18728:8728 -p 18729:8729 -ti evilfreelancer/docker-routeros:6.42
- docker run -d -p 22223:23 -p 8728:8728 -p 8729:8729 -ti evilfreelancer/docker-routeros:latest
- docker ps -a
- sleep 60
- ./preconf.tcl 12223 > /dev/null || true
- ./preconf.tcl 22223 > /dev/null || true
- composer self-update
- composer install --prefer-source --no-interaction --dev

script:
- vendor/bin/phpunit --coverage-clover=coverage.clover

after_script:
- wget https://scrutinizer-ci.com/ocular.phar
- php ocular.phar code-coverage:upload --format=php-clover coverage.clover


File: /vendor\evilfreelancer\routeros-api-php\composer.json
{
  "name": "evilfreelancer/routeros-api-php",
  "type": "library",
  "description": "Modern Mikrotik RouterOS API PHP7 client for your applications",
  "keywords": [
    "socket-client",
    "psr-4",
    "routeros",
    "mikrotik"
  ],
  "license": "MIT",
  "autoload": {
    "psr-4": {
      "RouterOS\\": "./src/"
    }
  },
  "autoload-dev": {
    "psr-4": { "RouterOS\\Tests\\": "./tests/" }
  },
  "authors": [
    {
      "name": "Paul Rock",
      "email": "paul@drteam.rocks",
      "homepage": "http://drteam.rocks/",
      "role": "Developer"
    }
  ],
  "require": {
    "php": "^7.1",
    "ext-sockets": "*"
  },
  "require-dev": {
    "phpunit/phpunit": "^7.0"
  }
}


File: /vendor\evilfreelancer\routeros-api-php\examples\bridge_hosts.php
<?php
require_once __DIR__ . '/../vendor/autoload.php';

error_reporting(E_ALL);

use \RouterOS\Config;
use \RouterOS\Client;
use \RouterOS\Query;

// Create config object with parameters
$config =
    (new Config())
        ->set('timeout', 1)
        ->set('host', '127.0.0.1')
        ->set('user', 'admin')
        ->set('pass', 'admin');

// Initiate client with config object
$client = new Client($config);

// Build query
$query = new Query('/interface/bridge/host/print');

// Send query to RouterOS
$response = $client->write($query)->read();
print_r($response);


File: /vendor\evilfreelancer\routeros-api-php\examples\different_queries.php
<?php
require_once __DIR__ . '/../vendor/autoload.php';

error_reporting(E_ALL);

use \RouterOS\Client;

// Initiate client with config object
$client = new Client([
    'timeout' => 1,
    'host'    => '127.0.0.1',
    'user'    => 'admin',
    'pass'    => 'admin'
]);

for ($i = 0; $i < 10; $i++) {
    $response = $client->wr('/ip/address/print');
    print_r($response);

    $response = $client->wr('/ip/arp/print');
    print_r($response);

    $response = $client->wr('/interface/print');
    print_r($response);
}


File: /vendor\evilfreelancer\routeros-api-php\examples\export.php
<?php
require_once __DIR__ . '/../vendor/autoload.php';

error_reporting(E_ALL);

use \RouterOS\Config;
use \RouterOS\Client;
use \RouterOS\Query;

// Create config object with parameters
$config =
    (new Config())
        ->set('host', '127.0.0.1')
        ->set('pass', 'admin')
        ->set('user', 'admin');

// Initiate client with config object
$client = new Client($config);

// Build query
$query = new Query('/export');

// Send query and read answer from RouterOS
$response = $client->write($query)->read(false);
print_r($response);


File: /vendor\evilfreelancer\routeros-api-php\examples\hotspot.php
<?php
require_once __DIR__ . '/../vendor/autoload.php';

use RouterOS\Client;
use RouterOS\Config;
use RouterOS\Query;

// Create config object with parameters
$config =
    (new Config())
        ->set('host', '127.0.0.1')
        ->set('port', 8728)
        ->set('pass', 'admin')
        ->set('user', 'admin');

// Initiate client with config object
$client = new Client($config);

/*
 * For the first we need to create new one user
 */

// Build query
$query =
    (new Query('/ip/hotspot/ip-binding/add'))
        ->equal('mac-address', '00:00:00:00:40:29')
        ->equal('type', 'bypassed')
        ->equal('comment', 'testcomment');

// Add user
$out = $client->query($query)->read();
print_r($out);

/*
 * Now try to remove created user from RouterOS
 */

// Remove user
$query =
    (new Query('/ip/hotspot/ip-binding/print'))
        ->where('mac-address', '00:00:00:00:40:29');

// Get user from RouterOS by query
$user = $client->query($query)->read();

if (!empty($user[0]['.id'])) {
    $userId     = $user[0]['.id'];

    // Remove MACa address
    $query =
        (new Query('/ip/hotspot/ip-binding/remove'))
            ->equal('.id', $userId);

    // Remove user from RouterOS
    $removeUser = $client->query($query)->read();
    print_r($removeUser);
}


File: /vendor\evilfreelancer\routeros-api-php\examples\interface_print.php
<?php
require_once __DIR__ . '/../vendor/autoload.php';

error_reporting(E_ALL);

use \RouterOS\Config;
use \RouterOS\Client;
use \RouterOS\Query;

// Create config object with parameters
$config =
    (new Config())
        ->set('host', '127.0.0.1')
        ->set('user', 'admin')
        ->set('pass', 'admin');

// Initiate client with config object
$client = new Client($config);

// Build query
$query = new Query('/interface/getall');

// Send query to RouterOS
$request = $client->write($query);

// Read answer from RouterOS
$response = $client->read();
print_r($response);


File: /vendor\evilfreelancer\routeros-api-php\examples\ip_address_print.php
<?php
require_once __DIR__ . '/../vendor/autoload.php';

error_reporting(E_ALL);

use \RouterOS\Client;
use \RouterOS\Query;

// Initiate client with config object
$client = new Client([
    'timeout' => 1,
    'host'    => '127.0.0.1',
    'user'    => 'admin',
    'pass'    => 'admin'
]);

// Build query
$query = new Query('/ip/address/print');

// Send query to RouterOS
$response = $client->write($query)->read();
print_r($response);


File: /vendor\evilfreelancer\routeros-api-php\examples\ip_filrewall_address-list_print.php
<?php
require_once __DIR__ . '/../vendor/autoload.php';

error_reporting(E_ALL);

use \RouterOS\Client;

// Initiate client with config object
$client = new Client([
    'timeout' => 1,
    'host'    => '127.0.0.1',
    'user'    => 'admin',
    'pass'    => 'admin'
]);

// Send query to RouterOS and parse response
$response = $client->write('/ip/firewall/address-list/print')->read();

// You could treat response as an array except using array_* function

// Export every row using foreach
foreach ($response as $row) {
    echo current($row) . PHP_EOL;
}

$item = current($response);
var_dump($item);
echo PHP_EOL;

$item = end($response);
var_dump($item);
echo PHP_EOL;

$item = current($response);
var_dump($item);
echo PHP_EOL;

$item = reset($response);
var_dump($item);
echo PHP_EOL;

$item = current($response);
var_dump($item);
echo PHP_EOL;


File: /vendor\evilfreelancer\routeros-api-php\examples\queue_simple_print.php
<?php
require_once __DIR__ . '/../vendor/autoload.php';

error_reporting(E_ALL);

use \RouterOS\Client;
use \RouterOS\Query;

// Initiate client with config object
$client = new Client([
    'timeout' => 1,
    'host'    => '127.0.0.1',
    'user'    => 'admin',
    'pass'    => 'admin'
]);

$ips = [
    '192.168.1.1',
    '192.168.1.2',
    '192.168.1.3',
    '192.168.1.4',
    '192.168.1.5',
    '192.168.1.6',
];

foreach ($ips as $ip) {
    $query    = new Query('/queue/simple/print', ['?target=' . $ip . '/32']);
    $response = $client->wr($query);
    print_r($response);
}


File: /vendor\evilfreelancer\routeros-api-php\examples\queue_simple_print_v2.php
<?php
require_once __DIR__ . '/../vendor/autoload.php';

error_reporting(E_ALL);

use \RouterOS\Client;
use \RouterOS\Query;

// Initiate client with config object
$client = new Client([
    'timeout' => 1,
    'host'    => '127.0.0.1',
    'user'    => 'admin',
    'pass'    => 'admin'
]);

$ips = [
    '192.168.1.1',
    '192.168.1.2',
    '192.168.1.3',
    '192.168.1.4',
    '192.168.1.5',
    '192.168.1.6',
];

foreach ($ips as $ip) {
    $response = $client->wr([
        '/queue/simple/print',
        '?target=' . $ip . '/32'
    ]);
    print_r($response);
}


File: /vendor\evilfreelancer\routeros-api-php\examples\queue_simple_write.php
<?php
require_once __DIR__ . '/../vendor/autoload.php';

error_reporting(E_ALL);

use \RouterOS\Client;

// Initiate client with config object
$client = new Client([
    'host'    => '127.0.0.1',
    'user'    => 'admin',
    'pass'    => 'admin'
]);

$out = $client->write(['/queue/simple/add', '=name=test'])->read();
print_r($out);

$out = $client->write(['/queue/simple/add', '=name=test'])->read();
print_r($out);


File: /vendor\evilfreelancer\routeros-api-php\examples\system_package_print.php
<?php
require_once __DIR__ . '/../vendor/autoload.php';

error_reporting(E_ALL);

use \RouterOS\Config;
use \RouterOS\Client;
use \RouterOS\Query;

// Create config object with parameters
$config =
    (new Config())
        ->set('host', '127.0.0.1')
        ->set('user', 'admin')
        ->set('pass', 'admin');

// Initiate client with config object
$client = new Client($config);

// Build query
$query = new Query('/system/package/print');

// Send query to RouterOS
$request = $client->write($query);

// Read answer from RouterOS
$response = $client->read();
print_r($response);


File: /vendor\evilfreelancer\routeros-api-php\examples\vlans_bridge.php
<?php
require_once __DIR__ . '/../vendor/autoload.php';

error_reporting(E_ALL);

use \RouterOS\Config;
use \RouterOS\Client;
use \RouterOS\Query;

// Create config object with parameters
$config =
    (new Config())
        ->set('host', '192.168.5.1')
        ->set('pass', 'admin')
        ->set('user', 'admin')
        ->set('legacy', true);

// Initiate client with config object
$client = new Client($config);

/*
 * Create VLAN 100 on 3-8 ports
 *             200 on 9-16
 *             300 on 17-24
 */
$vlans = [
    100 => [3, 4, 5, 6, 7, 8],
    200 => [9, 10, 11, 12, 13, 14, 15, 16],
    300 => [17, 18, 19, 20, 21, 22, 23, 24],
];

// Run commands for each vlan
foreach ($vlans as $vlanId => $ports) {

    // Add bridges
    $query = new Query('/interface/bridge/add');
    $query->add("=name=vlan$vlanId-bridge")->add('vlan-filtering=no');
    $response = $client->write($query)->read();
    print_r($response);

    // Add ports to bridge
    foreach ($ports as $port) {
        $bridgePort = new Query('/interface/bridge/port/add');
        $bridgePort->add("=bridge=vlan$vlanId-bridge")->add("=pvid=$vlanId")->add("=interface=ether$port");
        $response = $client->write($bridgePort)->read();
        print_r($response);
    }

    // Add untagged ports to bridge with tagging
    foreach ($ports as $port) {
        $vlan = new Query('/interface/bridge/vlan/add');
        $vlan->add("=bridge=vlan$vlanId-bridge")->add("=untagged=ether$port")->add("=vlan-ids=$vlanId");
        $response = $client->write($vlan)->read(false);
        print_r($response);
    }

}


File: /vendor\evilfreelancer\routeros-api-php\examples\vlans_bridge_v2.php
<?php
require_once __DIR__ . '/../vendor/autoload.php';

error_reporting(E_ALL);

use \RouterOS\Client;
use \RouterOS\Query;

// Initiate client with config object
$client = new Client([
    'host'   => '192.168.5.1',
    'user'   => 'admin',
    'pass'   => 'admin',
    'legacy' => true
]);

/*
 * Create VLAN 100 on 3-8 ports
 *             200 on 9-16
 *             300 on 17-24
 */
$vlans = [
    100 => [3, 4, 5, 6, 7, 8],
    200 => [9, 10, 11, 12, 13, 14, 15, 16],
    300 => [17, 18, 19, 20, 21, 22, 23, 24],
];

// Run commands for each vlan
foreach ($vlans as $vlanId => $ports) {

    // Add bridges
    $query = new Query('/interface/bridge/add', [
        "=name=vlan$vlanId-bridge",
        'vlan-filtering=no'
    ]);

    $response = $client->wr($query);
    print_r($response);

    // Add ports to bridge
    foreach ($ports as $port) {
        $bridgePort = new Query('/interface/bridge/port/add', [
            "=bridge=vlan$vlanId-bridge",
            "=pvid=$vlanId",
            "=interface=ether$port"
        ]);

        $response = $client->wr($bridgePort);
        print_r($response);
    }

    // Add untagged ports to bridge with tagging
    foreach ($ports as $port) {
        $vlan = new Query('/interface/bridge/vlan/add', [
            "=bridge=vlan$vlanId-bridge",
            "=untagged=ether$port",
            "=vlan-ids=$vlanId"
        ]);

        $response = $client->wr($vlan);
        print_r($response);
    }

}


File: /vendor\evilfreelancer\routeros-api-php\examples\vlans_bridge_v3.php
<?php
require_once __DIR__ . '/../vendor/autoload.php';

error_reporting(E_ALL);

use \RouterOS\Client;

// Initiate client with config object
$client = new Client([
    'host'   => '192.168.5.1',
    'user'   => 'admin',
    'pass'   => 'admin',
    'legacy' => true
]);

/*
 * Create VLAN 100 on 3-8 ports
 *             200 on 9-16
 *             300 on 17-24
 */
$vlans = [
    100 => [3, 4, 5, 6, 7, 8],
    200 => [9, 10, 11, 12, 13, 14, 15, 16],
    300 => [17, 18, 19, 20, 21, 22, 23, 24],
];

// Run commands for each vlan
foreach ($vlans as $vlanId => $ports) {

    // Add bridges
    $response = $client->wr([
        '/interface/bridge/add',
        "=name=vlan$vlanId-bridge",
        'vlan-filtering=no'
    ]);
    print_r($response);

    // Add ports to bridge
    foreach ($ports as $port) {
        $response = $client->wr([
            '/interface/bridge/port/add',
            "=bridge=vlan$vlanId-bridge",
            "=pvid=$vlanId",
            "=interface=ether$port"
        ]);
        print_r($response);
    }

    // Add untagged ports to bridge with tagging
    foreach ($ports as $port) {
        $response = $client->wr([
            '/interface/bridge/vlan/add',
            "=bridge=vlan$vlanId-bridge",
            "=untagged=ether$port",
            "=vlan-ids=$vlanId"
        ]);
        print_r($response);
    }

}


File: /vendor\evilfreelancer\routeros-api-php\FUNDING.yml
# These are supported funding model platforms

patreon: efreelancer # Replace with a single Patreon username


File: /vendor\evilfreelancer\routeros-api-php\LICENSE
MIT License

Copyright (c) 2018 Paul Rock

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


File: /vendor\evilfreelancer\routeros-api-php\phpunit.xml
<?xml version="1.0" encoding="UTF-8"?>
<phpunit bootstrap="./vendor/autoload.php" colors="true">
    <filter>
        <whitelist processUncoveredFilesFromWhitelist="true">
            <directory suffix=".php">./src</directory>
            <exclude>
                <directory suffix=".php">./tests</directory>
            </exclude>
        </whitelist>
    </filter>
    <logging>
        <log type="coverage-text" target="php://stdout" showUncoveredFiles="false"/>
    </logging>
    <testsuites>
        <testsuite name="RouterOS API on PHP tests">
            <directory suffix=".php">./tests/</directory>
        </testsuite>
    </testsuites>
    <php>
        <env name="ROS_HOST" value="127.0.0.1"/>
        <env name="ROS_USER" value="admin"/>
        <env name="ROS_PASS" value="admin"/>
        <env name="ROS_PORT_MODERN" value="18728"/>
        <env name="ROS_PORT_LEGACY" value="28728"/>
    </php>
</phpunit>


File: /vendor\evilfreelancer\routeros-api-php\preconf.tcl
#!/usr/bin/env expect

set timeout 10

set port [lindex $argv 0]

spawn telnet localhost $port

expect "Login: "
send "admin+c\n"
expect "Password: "
send "\n"
expect "]:"
send "n\r\n"
expect ">\ "
send "?\r\n"
expect ">\ "
send "\r\n"
expect ">\ "
send "/user set admin password=admin\r\n"
expect ">"
send "quit\r\n"
expect eof


File: /vendor\evilfreelancer\routeros-api-php\README.md
[![Latest Stable Version](https://poser.pugx.org/evilfreelancer/routeros-api-php/v/stable)](https://packagist.org/packages/evilfreelancer/routeros-api-php)
[![Build Status](https://travis-ci.org/EvilFreelancer/routeros-api-php.svg?branch=master)](https://travis-ci.org/EvilFreelancer/routeros-api-php)
[![Total Downloads](https://poser.pugx.org/evilfreelancer/routeros-api-php/downloads)](https://packagist.org/packages/evilfreelancer/routeros-api-php)
[![License](https://poser.pugx.org/evilfreelancer/routeros-api-php/license)](https://packagist.org/packages/evilfreelancer/routeros-api-php)
[![Code Climate](https://codeclimate.com/github/EvilFreelancer/routeros-api-php/badges/gpa.svg)](https://codeclimate.com/github/EvilFreelancer/routeros-api-php)
[![Code Coverage](https://scrutinizer-ci.com/g/EvilFreelancer/routeros-api-php/badges/coverage.png?b=master)](https://scrutinizer-ci.com/g/EvilFreelancer/routeros-api-php/?branch=master)
[![Scrutinizer CQ](https://scrutinizer-ci.com/g/evilfreelancer/routeros-api-php/badges/quality-score.png?b=master)](https://scrutinizer-ci.com/g/evilfreelancer/routeros-api-php/)

# RouterOS PHP7 API Client

    composer require evilfreelancer/routeros-api-php

This library is partly based on [this old project](https://github.com/BenMenking/routeros-api), but unlike it has many
innovations to ease development. In addition, the project is designed
to work with PHP7 in accordance with the PSR standards.

You can use this library with pre-6.43 and post-6.43 versions of
RouterOS firmware, it will be detected automatically on connection stage.

## How to use

Basic example, analogue via command line is `/ip address print`:

```php
use \RouterOS\Client;

// Initiate client with config object
$client = new Client([
    'host' => '192.168.1.3',
    'user' => 'admin',
    'pass' => 'admin'
]);

// Send query to RouterOS and read response from it
$response = $client->query('/ip/address/print')->read();
var_dump($response);
```

Examples with "where" conditions, "operations" and "tag":

```php
use \RouterOS\Query;

/**
 * Send advanced query with parameters to RouterOS 
 */

// If only one "where" condition
$client->query('/queue/simple/print', ['target', '192.168.1.1/32']);

// If multiple "where" conditions and need merge (operation "|") results
$client->query('/interface/print', [
    ['type', 'ether'],  // same as ['type', '=', 'ether']
    ['type', 'vlan'],   // same as ['type', '=', 'vlan']
], '|');

/**
 * Or in OOP style
 */

// If multiple "where" conditions and need merge (operation "|") results
$query = new Query('/interface/print');
$query->where('type', 'ether');
$query->where('type', 'vlan');
$query->operations('|');

// If multiple "where" conditions and need append tag
$query = new Query('/interface/set');
$query->where('disabled', 'no');
$query->where('.id', 'ether1');
$query->tag(4);

/**
 * Write Query object to RouterOS and read response from it
 */

$response = $client->query($query)->read();
```

> All available examples you can find [here](https://github.com/EvilFreelancer/routeros-api-php/tree/master/examples).

## How to configure the client

You just need create object of Client class with required
parameters in array format:

```php
use \RouterOS\Client;

$client = new Client([
    'host' => '192.168.1.3',
    'user' => 'admin',
    'pass' => 'admin'
]);
```

<details>
<summary>
<i>ℹ️ Advanced examples of Config and Client classes usage</i>
</summary>

```php
use \RouterOS\Config;
use \RouterOS\Client;

/**
 * You can create object of Config class
 */

$config = new Config();

// Then set parameters of config
$config->set('host', '192.168.1.3');
$config->set('user', 'admin');
$config->set('pass', 'admin');

// By the way, `->set()` method is support inline style of syntax
$config
    ->set('host', '192.168.1.3')
    ->set('user', 'admin')
    ->set('pass', 'admin');

/**
 * Or just create preconfigured Config object
 */

$config = new Config([
    'host' => '192.168.1.3',
    'user' => 'admin',
    'pass' => 'admin'
]);

/**
 * Then send Config object to Client constructor
 */

$client = new Client($config);
```

</details>

### List of available configuration parameters

| Parameter | Type   | Default | Description |
|-----------|--------|---------|-------------|
| host      | string |         | (required) Address of Mikrotik RouterOS |
| user      | string |         | (required) Username |
| pass      | string |         | (required) Password |
| port      | int    |         | RouterOS API port number for access (if not set use 8728 or 8729 if SSL enabled) |
| ssl       | bool   | false   | Enable ssl support (if port is not set this parameter must change default port to ssl port) |
| legacy    | bool   | false   | Support of legacy login scheme (true - pre 6.43, false - post 6.43) |
| timeout   | int    | 10      | Max timeout for answer from RouterOS |
| attempts  | int    | 10      | Count of attempts to establish TCP session |
| delay     | int    | 1       | Delay between attempts in seconds |

### How to enable support of legacy login schema (RouterOS pre-6.43)

> From 0.8.1 this is not important, version of firmware will be detected automatically.

```php
<?php
require_once __DIR__ . '/vendor/autoload.php';

use \RouterOS\Client;

// Initiate client with config object
$client = new Client([
    'host'   => '192.168.1.3',
    'user'   => 'admin',
    'pass'   => 'admin',
    'legacy' => true // you need set `legacy` parameter with `true` value
]);

// Your code below...
```

## How to write queries

You can write absolutely any queries to your router, for this you
need to create a "Query" object whose first argument is the
required command, after this you can add the attributes of the
command to "Query" object.

More about attributes and "words" from which this attributes
should be created [here](https://wiki.mikrotik.com/wiki/Manual:API#Command_word). 

More about "expressions", "where" and other filters/modificators
of your query you can find [here](https://wiki.mikrotik.com/wiki/Manual:API#Queries).

Simple usage examples of Query class:

```php
use \RouterOS\Query;

// Get all installed packages (it may be enabled or disabled)
$query = new Query('/system/package/getall');

// Set where interface is disabled and ID is ether1 (with tag 4)
$query = 
    (new Query('/interface/set'))
        ->where('disabled', 'no')
        ->where('.id', 'ether1')
        ->tag(4);

// Get all ethernet and VLAN interfaces
$query = 
    (new Query('/interface/print'))
        ->where('type', 'ether')
        ->where('type', 'vlan')
        ->operations('|');

/// Get all routes that have non-empty comment
$query =
    (new Query('/ip/route/print'))
        ->where('comment', '>', null);
```

<details>
<summary>
<i>ℹ️ Advanced examples of Query class usage</i>
</summary>

```php
use \RouterOS\Query;
use \RouterOS\Client;

// Initiate connection to RouterOS
$client = new Client([
    'host'   => '192.168.1.3',
    'user'   => 'admin',
    'pass'   => 'admin'
]);

/**
 * Execute query directly through "->query()" method of Client class 
 */

// If your query has no "where" conditions
$client->query('/ip/arp/print');

// If you have only one where condition, you may use one dimensional array as second parameter of query method
$client->query('/queue/simple/print', ['target', '192.168.1.250/32']);

// If you need set few where conditions then need use multi dimensional array
$client->query('/interface/bridge/add', [
    ['name', 'vlan100-bridge'],
    ['vlan-filtering', 'no']
]);

/**
 * By some reason you may need restrict scope of RouterOS response,
 * for this need to use third attribute of "->query()" method
 */

// Get all ethernet and VLAN interfaces
$client->query('/interface/print', [
    ['type', 'ether'],
    ['type', 'vlan']
], '|');

/** 
 * If you want set tag of your query then you need to use fourth 
 * attribute of "->query()" method, but third attribute may be null
 */

// Enable interface (tag is 4)
$client->query('/interface/set', [
    ['disabled', 'no'],
    ['.id', 'ether1']
], null, 4);

/**
 * Or in OOP style  
 */

// Get all ethernet and VLAN interfaces
$query = new Query('/interface/print');
$query->where('type', 'ether');
$query->where('type', 'vlan');
$query->operations('|');

// Enable interface (tag is 4)
$query = new Query('/interface/set');
$query->where('disabled', 'no');
$query->where('.id', 'ether1');
$query->tag(4);

// Or

$query = new Query('/interface/set');
$query->add('=disabled=no');
$query->add('=.id=ether1');
$query->add('.tag=4');

// Or
    
$query = new Query('/interface/set', [
    '=disabled=no',
    '=.id=ether1',
    '.tag=4'
]);

// Or

$query = new Query([
    '/interface/set',
    '=disabled=no',
    '=.id=ether1',
    '.tag=4'
]);

/**
 * Write Query object to RouterOS and read response from it
 */

$response = $client->query($query)->read();
```

</details>

## Read response as Iterator

By default original solution of this client is not optimized for
work with large amount of results, only for small count of lines
in response from RouterOS API.

But some routers may have (for example) 30000+ records in
their firewall list. Specifically for such tasks, a method
`readAsIterator` has been added that converts the results
obtained from the router into a resource, with which it will
later be possible to work.

> You could treat response as an array except using any array_* functions

```php
$response = $client->query($query)->readAsIterator();
var_dump($response);

// The following for loop allows you to skip elements for which
// $iterator->current() throws an exception, rather than breaking
// the loop.
for ($response->rewind(); $response->valid(); $response->next()) {
    try {
        $value = $response->current();
    } catch (Exception $exception) {
        continue;
    }

    # ...
}
```

## Short methods

You can simplify your code and send then read from socket in one line:

```php
/** 
 * Execute query and read response in ordinary mode 
 */
$response = $client->query($query)->read();
var_dump($response);

// Or
$response = $client->q($query)->r();
var_dump($response);

// Single method analog of lines above is
$response = $client->qr($query);
var_dump($response);

/**
 * Execute query and read response as Iterator 
 */
$response = $client->query($query)->readAsIterator();
var_dump($response);

// Or
$response = $client->q($query)->ri();
var_dump($response);

// Single method analog of lines above is
$response = $client->qri($query);
var_dump($response);

/**
 * By the way, you can send few queries to your router without result: 
 */
$client->query($query1)->query($query2)->query($query3);

// Or
$client->q($query1)->q($query2)->q($query3);
```

## Testing

You can use my [other project](https://github.com/EvilFreelancer/docker-routeros)
with RouterOS in Docker container for running unit testing on your
computer, for this you just need to have [Expect](https://wiki.debian.org/Expect),
[Docker](https://docs.docker.com/install/) and [Docker Compose](https://docs.docker.com/compose/install/).

Next clone the repo with RouterOS in Docker and exec
`docker-compose up -d`, then you need preconfigure virtual routers
via [preconf.tcl](https://github.com/EvilFreelancer/routeros-api-php/blob/master/preconf.tcl)
script from root of routeros-api-php:

```
./preconf.tcl 12223
./preconf.tcl 22223
```

And after this you can run tests:

```
./vendor/bin/phpunit
```

## Links

* [Cloud Hosted Router](https://mikrotik.com/download#chr) - Virtual images of RouterOS for your hypervisor 
* [RouterOS Manual:API](https://wiki.mikrotik.com/wiki/Manual:API) - In case if you are wondering what is insane


File: /vendor\evilfreelancer\routeros-api-php\src\APIConnector.php
<?php

namespace RouterOS;

use RouterOS\Interfaces\StreamInterface;

/**
 * Class APIConnector
 *
 * Implement middle level dialog with router by masking word dialog implementation to client class
 *
 * @package RouterOS
 * @since   0.9
 */
class APIConnector
{
    /**
     * @var StreamInterface $stream The stream used to communicate with the router
     */
    protected $stream;

    /**
     * Constructor
     *
     * @param StreamInterface $stream
     */

    public function __construct(StreamInterface $stream)
    {
        $this->stream = $stream;
    }

    /**
     * Reads a WORD from the stream
     *
     * WORDs are part of SENTENCE. Each WORD has to be encoded in certain way - length of the WORD followed by WORD content.
     * Length of the WORD should be given as count of bytes that are going to be sent
     *
     * @return string The word content, en empty string for end of SENTENCE
     */
    public function readWord(): string
    {
        // Get length of next word
        $length = APILengthCoDec::decodeLength($this->stream);
        return ($length > 0) ? $this->stream->read($length) : '';
    }

    /**
     * Write word to stream
     *
     * @param   string $word
     * @return  int return number of written bytes
     */
    public function writeWord(string $word): int
    {
        $encodedLength = APILengthCoDec::encodeLength(strlen($word));
        return $this->stream->write($encodedLength . $word);
    }
}


File: /vendor\evilfreelancer\routeros-api-php\src\APILengthCoDec.php
<?php

namespace RouterOS;

use RouterOS\Interfaces\StreamInterface;
use RouterOS\Helpers\BinaryStringHelper;

/**
 * class APILengthCoDec
 *
 * Coder / Decoder for length field in mikrotik API communication protocol
 *
 * @package RouterOS
 * @since   0.9
 */
class APILengthCoDec
{
    /**
     * Encode string to length of string
     *
     * @param   int|float $length
     * @return  string
     */
    public static function encodeLength($length): string
    {
        // Encode the length :
        // - if length <= 0x7F (binary : 01111111 => 7 bits set to 1)
        //      - encode length with one byte
        //      - set the byte to length value, as length maximal value is 7 bits set to 1, the most significant bit is always 0
        //      - end
        // - length <= 0x3FFF (binary : 00111111 11111111 => 14 bits set to 1)
        //      - encode length with two bytes
        //      - set length value to 0x8000 (=> 10000000 00000000)
        //      - add length : as length maximumal value is 14 bits to 1, this does not modify the 2 most significance bits (10)
        //      - end
        //      => minimal encoded value is 10000000 10000000
        // - length <= 0x1FFFFF (binary : 00011111 11111111 11111111 => 21 bits set to 1)
        //      - encode length with three bytes
        //      - set length value to 0xC00000 (binary : 11000000 00000000 00000000)
        //      - add length : as length maximal vlaue is 21 bits to 1, this does not modify the 3 most significance bits (110)
        //      - end
        //      => minimal encoded value is 11000000 01000000 00000000
        // - length <= 0x0FFFFFFF (binary : 00001111 11111111 11111111 11111111 => 28 bits set to 1)
        //      - encode length with four bytes
        //      - set length value to 0xE0000000 (binary : 11100000 00000000 00000000 00000000)
        //      - add length : as length maximal vlaue is 28 bits to 1, this does not modify the 4 most significance bits (1110)
        //      - end
        //      => minimal encoded value is 11100000 00100000 00000000 00000000
        // - length <= 0x7FFFFFFFFF (binary : 00000111 11111111 11111111 11111111 11111111 => 35 bits set to 1)
        //      - encode length with five bytes
        //      - set length value to 0xF000000000 (binary : 11110000 00000000 00000000 00000000 00000000)
        //      - add length : as length maximal vlaue is 35 bits to 1, this does not modify the 5 most significance bits (11110)
        //      - end
        // - length > 0x7FFFFFFFFF : not supported

        if ($length < 0) {
            throw new \DomainException("Length of word could not to be negative ($length)");
        }

        if ($length <= 0x7F) {
            return BinaryStringHelper::IntegerToNBOBinaryString($length);
        }

        if ($length <= 0x3FFF) {
            return BinaryStringHelper::IntegerToNBOBinaryString(0x8000 + $length);
        }

        if ($length <= 0x1FFFFF) {
            return BinaryStringHelper::IntegerToNBOBinaryString(0xC00000 + $length);
        }

        if ($length <= 0x0FFFFFFF) {
            return BinaryStringHelper::IntegerToNBOBinaryString(0xE0000000 + $length);
        }

        // https://wiki.mikrotik.com/wiki/Manual:API#API_words
        // If len >= 0x10000000 then 0xF0 and len as four bytes
        return BinaryStringHelper::IntegerToNBOBinaryString(0xF000000000 + $length);
    }

    // Decode length of data when reading :
    // The 5 firsts bits of the first byte specify how the length is encoded.
    // The position of the first 0 value bit, starting from the most significant postion. 
    // - 0xxxxxxx => The 7 remainings bits of the first byte is the length : 
    //            => min value of length is 0x00 
    //            => max value of length is 0x7F (127 bytes)
    // - 10xxxxxx => The 6 remainings bits of the first byte plus the next byte represent the lenght
    //            NOTE : the next byte MUST be at least 0x80 !!
    //            => min value of length is 0x80 
    //            => max value of length is 0x3FFF (16,383 bytes, near 16 KB)
    // - 110xxxxx => The 5 remainings bits of th first byte and the two next bytes represent the length
    //             => max value of length is 0x1FFFFF (2,097,151 bytes, near 2 MB)
    // - 1110xxxx => The 4 remainings bits of the first byte and the three next bytes represent the length
    //            => max value of length is 0xFFFFFFF (268,435,455 bytes, near 270 MB)
    // - 11110xxx => The 3 remainings bits of the first byte and the four next bytes represent the length
    //            => max value of length is 0x7FFFFFFF (2,147,483,647 byes, 2GB)
    // - 11111xxx => This byte is not a length-encoded word but a control byte.
    //          =>  Extracted from Mikrotik API doc : 
    //              it is a reserved control byte. 
    //              After receiving unknown control byte API client cannot proceed, because it cannot know how to interpret following bytes
    //              Currently control bytes are not used

    public static function decodeLength(StreamInterface $stream): int
    {
        // if (false === is_resource($stream)) {
        //     throw new \InvalidArgumentException(
        //         sprintf(
        //             'Argument must be a stream resource type. %s given.',
        //             gettype($stream)
        //         )
        //     );
        // }

        // Read first byte
        $firstByte = ord($stream->read(1));

        // If first byte is not set, length is the value of the byte
        if (0 === ($firstByte & 0x80)) {
            return $firstByte;
        }

        // if 10xxxxxx, length is 2 bytes encoded
        if (0x80 === ($firstByte & 0xC0)) {
            // Set 2 most significands bits to 0
            $result = $firstByte & 0x3F;

            // shift left 8 bits to have 2 bytes
            $result <<= 8;

            // read next byte and use it as least significant
            $result |= ord($stream->read(1));
            return $result;
        }

        // if 110xxxxx, length is 3 bytes encoded
        if (0xC0 === ($firstByte & 0xE0)) {
            // Set 3 most significands bits to 0
            $result = $firstByte & 0x1F;

            // shift left 16 bits to have 3 bytes
            $result <<= 16;

            // read next 2 bytes as value and use it as least significant position
            $result |= (ord($stream->read(1)) << 8);
            $result |= ord($stream->read(1));
            return $result;
        }

        // if 1110xxxx, length is 4 bytes encoded
        if (0xE0 === ($firstByte & 0xF0)) {
            // Set 4 most significance bits to 0
            $result = $firstByte & 0x0F;

            // shift left 24 bits to have 4 bytes
            $result <<= 24;

            // read next 3 bytes as value and use it as least significant position
            $result |= (ord($stream->read(1)) << 16);
            $result |= (ord($stream->read(1)) << 8);
            $result |= ord($stream->read(1));
            return $result;
        }

        // if 11110xxx, length is 5 bytes encoded
        if (0xF0 === ($firstByte & 0xF8)) {
            // Not possible on 32 bits systems
            if (PHP_INT_SIZE < 8) {
                // Cannot be done on 32 bits systems
                // PHP5 windows versions of php, even on 64 bits systems was impacted
                // see : https://stackoverflow.com/questions/27865340/php-int-size-returns-4-but-my-operating-system-is-64-bit
                // How can we test it ?

                // @codeCoverageIgnoreStart
                throw new \OverflowException("Your system is using 32 bits integers, cannot decode this value ($firstByte) on this system");
                // @codeCoverageIgnoreEnd
            }

            // Set 5 most significance bits to 0
            $result = $firstByte & 0x07;

            // shift left 232 bits to have 5 bytes
            $result <<= 32;

            // read next 4 bytes as value and use it as least significant position
            $result |= (ord($stream->read(1)) << 24);
            $result |= (ord($stream->read(1)) << 16);
            $result |= (ord($stream->read(1)) << 8);
            $result |= ord($stream->read(1));
            return $result;
        }

        // Now the only solution is 5 most significance bits are set to 1 (11111xxx)
        // This is a control word, not implemented by Mikrotik for the moment 
        throw new \UnexpectedValueException('Control Word found');
    }
}


File: /vendor\evilfreelancer\routeros-api-php\src\Client.php
<?php

namespace RouterOS;

use RouterOS\Exceptions\ClientException;
use RouterOS\Exceptions\ConfigException;
use RouterOS\Exceptions\QueryException;
use RouterOS\Helpers\ArrayHelper;

/**
 * Class Client for RouterOS management
 *
 * @package RouterOS
 * @since   0.1
 */
class Client implements Interfaces\ClientInterface
{
    use SocketTrait, ShortsTrait;

    /**
     * Configuration of connection
     *
     * @var \RouterOS\Config
     */
    private $_config;

    /**
     * API communication object
     *
     * @var \RouterOS\APIConnector
     */

    private $_connector;

    /**
     * Client constructor.
     *
     * @param array|\RouterOS\Config $config
     *
     * @throws \RouterOS\Exceptions\ClientException
     * @throws \RouterOS\Exceptions\ConfigException
     * @throws \RouterOS\Exceptions\QueryException
     */
    public function __construct($config)
    {
        // If array then need create object
        if (\is_array($config)) {
            $config = new Config($config);
        }

        // Check for important keys
        if (true !== $key = ArrayHelper::checkIfKeysNotExist(['host', 'user', 'pass'], $config->getParameters())) {
            throw new ConfigException("One or few parameters '$key' of Config is not set or empty");
        }

        // Save config if everything is okay
        $this->_config = $config;

        // Throw error if cannot to connect
        if (false === $this->connect()) {
            throw new ClientException('Unable to connect to ' . $config->get('host') . ':' . $config->get('port'));
        }
    }

    /**
     * Get some parameter from config
     *
     * @param string $parameter Name of required parameter
     *
     * @return mixed
     * @throws \RouterOS\Exceptions\ConfigException
     */
    private function config(string $parameter)
    {
        return $this->_config->get($parameter);
    }

    /**
     * Send write query to RouterOS
     *
     * @param string|array|\RouterOS\Query $query
     *
     * @return \RouterOS\Client
     * @throws \RouterOS\Exceptions\QueryException
     * @deprecated
     * @codeCoverageIgnore
     */
    public function write($query): Client
    {
        if (\is_string($query)) {
            $query = new Query($query);
        } elseif (\is_array($query)) {
            $endpoint = array_shift($query);
            $query    = new Query($endpoint, $query);
        }

        if (!$query instanceof Query) {
            throw new QueryException('Parameters cannot be processed');
        }

        // Submit query to RouterOS
        return $this->writeRAW($query);
    }

    /**
     * Send write query to RouterOS (modern version of write)
     *
     * @param string|Query $endpoint   Path of API query or Query object
     * @param array|null   $where      List of where filters
     * @param string|null  $operations Some operations which need make on response
     * @param string|null  $tag        Mark query with tag
     *
     * @return \RouterOS\Client
     * @throws \RouterOS\Exceptions\QueryException
     * @throws \RouterOS\Exceptions\ClientException
     * @since 1.0.0
     */
    public function query($endpoint, array $where = null, string $operations = null, string $tag = null): Client
    {
        // If endpoint is string then build Query object
        $query = ($endpoint instanceof Query)
            ? $endpoint
            : new Query($endpoint);

        // Parse where array
        if (!empty($where)) {

            // If array is multidimensional, then parse each line
            if (is_array($where[0])) {
                foreach ($where as $item) {

                    // Null by default
                    $key      = null;
                    $operator = null;
                    $value    = null;

                    switch (\count($item)) {
                        case 1:
                            list($key) = $item;
                            break;
                        case 2:
                            list($key, $operator) = $item;
                            break;
                        case 3:
                            list($key, $operator, $value) = $item;
                            break;
                        default:
                            throw new ClientException('From 1 to 3 parameters of "where" condition is allowed');
                    }
                    $query->where($key, $operator, $value);
                }
            } else {
                // Null by default
                $key      = null;
                $operator = null;
                $value    = null;

                switch (\count($where)) {
                    case 1:
                        list($key) = $where;
                        break;
                    case 2:
                        list($key, $operator) = $where;
                        break;
                    case 3:
                        list($key, $operator, $value) = $where;
                        break;
                    default:
                        throw new ClientException('From 1 to 3 parameters of "where" condition is allowed');
                }

                $query->where($key, $operator, $value);
            }

        }

        // Append operations if set
        if (!empty($operations)) {
            $query->operations($operations);
        }

        // Append tag if set
        if (!empty($tag)) {
            $query->tag($tag);
        }

        // Submit query to RouterOS
        return $this->writeRAW($query);
    }

    /**
     * Send write query object to RouterOS
     *
     * @param \RouterOS\Query $query
     *
     * @return \RouterOS\Client
     * @throws \RouterOS\Exceptions\QueryException
     * @since 1.0.0
     */
    private function writeRAW(Query $query): Client
    {
        // Send commands via loop to router
        foreach ($query->getQuery() as $command) {
            $this->_connector->writeWord(trim($command));
        }

        // Write zero-terminator (empty string)
        $this->_connector->writeWord('');

        return $this;
    }

    /**
     * Read RAW response from RouterOS
     *
     * @return array
     * @since 1.0.0
     */
    private function readRAW(): array
    {
        // By default response is empty
        $response = [];
        // We have to wait a !done or !fatal
        $lastReply = false;

        // Read answer from socket in loop
        while (true) {
            $word = $this->_connector->readWord();

            if ('' === $word) {
                if ($lastReply) {
                    // We received a !done or !fatal message in a precedent loop
                    // response is complete
                    break;
                }
                // We did not receive the !done or !fatal message
                // This 0 length message is the end of a reply !re or !trap
                // We have to wait the router to send a !done or !fatal reply followed by optionals values and a 0 length message
                continue;
            }

            // Save output line to response array
            $response[] = $word;

            // If we get a !done or !fatal line in response, we are now ready to finish the read
            // but we need to wait a 0 length message, switch the flag
            if ('!done' === $word || '!fatal' === $word) {
                $lastReply = true;
            }
        }

        // Parse results and return
        return $response;
    }

    /**
     * Read answer from server after query was executed
     *
     * A Mikrotik reply is formed of blocks
     * Each block starts with a word, one of ('!re', '!trap', '!done', '!fatal')
     * Each block end with an zero byte (empty line)
     * Reply ends with a complete !done or !fatal block (ended with 'empty line')
     * A !fatal block precedes TCP connexion close
     *
     * @param bool $parse
     *
     * @return mixed
     */
    public function read(bool $parse = true)
    {
        // Read RAW response
        $response = $this->readRAW();

        // Parse results and return
        return $parse ? $this->rosario($response) : $response;
    }

    /**
     * Read using Iterators to improve performance on large dataset
     *
     * @return \RouterOS\ResponseIterator
     * @since 1.0.0
     */
    public function readAsIterator(): ResponseIterator
    {
        return new ResponseIterator($this);
    }

    /**
     * This method was created by memory save reasons, it convert response
     * from RouterOS to readable array in safe way.
     *
     * @param array $raw Array RAW response from server
     *
     * @return mixed
     *
     * Based on RouterOSResponseArray solution by @arily
     *
     * @link    https://github.com/arily/RouterOSResponseArray
     * @since   1.0.0
     */
    private function rosario(array $raw): array
    {
        // This RAW should't be an error
        $positions = array_keys($raw, '!re');
        $count     = count($raw);
        $result    = [];

        if (isset($positions[1])) {

            foreach ($positions as $key => $position) {
                // Get length of future block
                $length = isset($positions[$key + 1])
                    ? $positions[$key + 1] - $position + 1
                    : $count - $position;

                // Convert array to simple items
                $item = [];
                for ($i = 1; $i < $length; $i++) {
                    $item[] = array_shift($raw);
                }

                // Save as result
                $result[] = $this->parseResponse($item)[0];
            }

        } else {
            $result = $this->parseResponse($raw);
        }

        return $result;
    }

    /**
     * Parse response from Router OS
     *
     * @param array $response Response data
     *
     * @return array Array with parsed data
     */
    public function parseResponse(array $response): array
    {
        $result = [];
        $i      = -1;
        $lines  = \count($response);
        foreach ($response as $key => $value) {
            switch ($value) {
                case '!re':
                    $i++;
                    break;
                case '!fatal':
                    $result = $response;
                    break 2;
                case '!trap':
                case '!done':
                    // Check for =ret=, .tag and any other following messages
                    for ($j = $key + 1; $j <= $lines; $j++) {
                        // If we have lines after current one
                        if (isset($response[$j])) {
                            $this->pregResponse($response[$j], $matches);
                            if (isset($matches[1][0], $matches[2][0])) {
                                $result['after'][$matches[1][0]] = $matches[2][0];
                            }
                        }
                    }
                    break 2;
                default:
                    $this->pregResponse($value, $matches);
                    if (isset($matches[1][0], $matches[2][0])) {
                        $result[$i][$matches[1][0]] = $matches[2][0];
                    }
                    break;
            }
        }
        return $result;
    }

    /**
     * Parse result from RouterOS by regular expression
     *
     * @param string $value
     * @param array  $matches
     */
    private function pregResponse(string $value, &$matches)
    {
        preg_match_all('/^[=|\.](.*)=(.*)/', $value, $matches);
    }

    /**
     * Authorization logic
     *
     * @param bool $legacyRetry Retry login if we detect legacy version of RouterOS
     *
     * @return bool
     * @throws \RouterOS\Exceptions\ClientException
     * @throws \RouterOS\Exceptions\ConfigException
     * @throws \RouterOS\Exceptions\QueryException
     */
    private function login(bool $legacyRetry = false): bool
    {
        // If legacy login scheme is enabled
        if ($this->config('legacy')) {
            // For the first we need get hash with salt
            $response = $this->query('/login')->read();

            // Now need use this hash for authorization
            $query = new Query('/login', [
                '=name=' . $this->config('user'),
                '=response=00' . md5(\chr(0) . $this->config('pass') . pack('H*', $response['after']['ret']))
            ]);
        } else {
            // Just login with our credentials
            $query = new Query('/login', [
                '=name=' . $this->config('user'),
                '=password=' . $this->config('pass')
            ]);

            // If we set modern auth scheme but router with legacy firmware then need to retry query,
            // but need to prevent endless loop
            $legacyRetry = true;
        }

        // Execute query and get response
        $response = $this->query($query)->read(false);

        // if:
        //  - we have more than one response
        //  - response is '!done'
        // => problem with legacy version, swap it and retry
        // Only tested with ROS pre 6.43, will test with post 6.43 => this could make legacy parameter obsolete?
        if ($legacyRetry && $this->isLegacy($response)) {
            $this->_config->set('legacy', true);
            return $this->login();
        }

        // If RouterOS answered with invalid credentials then throw error
        if (!empty($response[0]) && $response[0] === '!trap') {
            throw new ClientException('Invalid user name or password');
        }

        // Return true if we have only one line from server and this line is !done
        return (1 === count($response)) && isset($response[0]) && ($response[0] === '!done');
    }

    /**
     * Detect by login request if firmware is legacy
     *
     * @param array $response
     *
     * @return bool
     * @throws ConfigException
     */
    private function isLegacy(array &$response): bool
    {
        return \count($response) > 1 && $response[0] === '!done' && !$this->config('legacy');
    }

    /**
     * Connect to socket server
     *
     * @return bool
     * @throws \RouterOS\Exceptions\ClientException
     * @throws \RouterOS\Exceptions\ConfigException
     * @throws \RouterOS\Exceptions\QueryException
     */
    private function connect(): bool
    {
        // By default we not connected
        $connected = false;

        // Few attempts in loop
        for ($attempt = 1; $attempt <= $this->config('attempts'); $attempt++) {

            // Initiate socket session
            $this->openSocket();

            // If socket is active
            if (null !== $this->getSocket()) {
                $this->_connector = new APIConnector(new Streams\ResourceStream($this->getSocket()));
                // If we logged in then exit from loop
                if (true === $this->login()) {
                    $connected = true;
                    break;
                }

                // Else close socket and start from begin
                $this->closeSocket();
            }

            // Sleep some time between tries
            sleep($this->config('delay'));
        }

        // Return status of connection
        return $connected;
    }
}


File: /vendor\evilfreelancer\routeros-api-php\src\Config.php
<?php

namespace RouterOS;

use RouterOS\Exceptions\ConfigException;
use RouterOS\Helpers\ArrayHelper;
use RouterOS\Helpers\TypeHelper;
use RouterOS\Interfaces\ConfigInterface;

/**
 * Class Config with array of parameters
 *
 * @package RouterOS
 * @since   0.1
 */
class Config implements ConfigInterface
{
    /**
     * Array of parameters (with some default values)
     *
     * @var array
     */
    private $_parameters = [
        'legacy'   => Client::LEGACY,
        'ssl'      => Client::SSL,
        'timeout'  => Client::TIMEOUT,
        'attempts' => Client::ATTEMPTS,
        'delay'    => Client::ATTEMPTS_DELAY
    ];

    /**
     * Config constructor.
     *
     * @param   array $parameters List of parameters which can be set on object creation stage
     * @throws  ConfigException
     * @since   0.6
     */
    public function __construct(array $parameters = [])
    {
        foreach ($parameters as $key => $value) {
            $this->set($key, $value);
        }
    }

    /**
     * Set parameter into array
     *
     * @param   string $name
     * @param   mixed  $value
     * @return  \RouterOS\Config
     * @throws  ConfigException
     */
    public function set(string $name, $value): Config
    {
        // Check of key in array
        if (ArrayHelper::checkIfKeyNotExist($name, self::ALLOWED)) {
            throw new ConfigException("Requested parameter '$name' not found in list [" . implode(',', array_keys(self::ALLOWED)) . ']');
        }

        // Check what type has this value
        if (TypeHelper::checkIfTypeMismatch(\gettype($value), self::ALLOWED[$name])) {
            throw new ConfigException("Parameter '$name' has wrong type '" . \gettype($value) . "' but should be '" . self::ALLOWED[$name] . "'");
        }

        // Save value to array
        $this->_parameters[$name] = $value;

        return $this;
    }

    /**
     * Return port number (get from defaults if port is not set by user)
     *
     * @param   string $parameter
     * @return  bool|int
     */
    private function getPort(string $parameter)
    {
        // If client need port number and port is not set
        if ($parameter === 'port' && !isset($this->_parameters['port'])) {
            // then use default with or without ssl encryption
            return (isset($this->_parameters['ssl']) && $this->_parameters['ssl'])
                ? Client::PORT_SSL
                : Client::PORT;
        }
        return null;
    }

    /**
     * Remove parameter from array by name
     *
     * @param   string $name
     * @return  \RouterOS\Config
     * @throws  \RouterOS\Exceptions\ConfigException
     */
    public function delete(string $name): Config
    {
        // Check of key in array
        if (ArrayHelper::checkIfKeyNotExist($name, self::ALLOWED)) {
            throw new ConfigException("Requested parameter '$name' not found in list [" . implode(',', array_keys(self::ALLOWED)) . ']');
        }

        // Save value to array
        unset($this->_parameters[$name]);

        return $this;
    }

    /**
     * Return parameter of current config by name
     *
     * @param   string $name
     * @return  mixed
     * @throws  \RouterOS\Exceptions\ConfigException
     */
    public function get(string $name)
    {
        // Check of key in array
        if (ArrayHelper::checkIfKeyNotExist($name, self::ALLOWED)) {
            throw new ConfigException("Requested parameter '$name' not found in list [" . implode(',', array_keys(self::ALLOWED)) . ']');
        }

        return $this->getPort($name) ?? $this->_parameters[$name];
    }

    /**
     * Return array with all parameters of configuration
     *
     * @return  array
     */
    public function getParameters(): array
    {
        return $this->_parameters;
    }
}


File: /vendor\evilfreelancer\routeros-api-php\src\Exceptions\ClientException.php
<?php

namespace RouterOS\Exceptions;

/**
 * Class ClientException
 *
 * @package RouterOS\Exceptions
 * @since   0.4
 */
class ClientException extends \Exception
{
}


File: /vendor\evilfreelancer\routeros-api-php\src\Exceptions\ConfigException.php
<?php

namespace RouterOS\Exceptions;

/**
 * Class ConfigException
 *
 * @package RouterOS\Exceptions
 * @since   0.4
 */
class ConfigException extends \Exception
{
}


File: /vendor\evilfreelancer\routeros-api-php\src\Exceptions\QueryException.php
<?php

namespace RouterOS\Exceptions;

/**
 * Class QueryException
 *
 * @package RouterOS\Exceptions
 * @since   0.7
 */
class QueryException extends \Exception
{
}


File: /vendor\evilfreelancer\routeros-api-php\src\Exceptions\StreamException.php
<?php

namespace RouterOS\Exceptions;

/**
 * Class StreamException
 *
 * @package RouterOS\Exceptions
 * @since   0.9
 */

class StreamException extends \Exception
{
}


File: /vendor\evilfreelancer\routeros-api-php\src\Helpers\ArrayHelper.php
<?php

namespace RouterOS\Helpers;

/**
 * Class ArrayHelper
 *
 * @package RouterOS\Helpers
 * @since   0.7
 */
class ArrayHelper
{
    /**
     * Check if required single key in array of parameters
     *
     * @param   string $key
     * @param   array  $array
     * @return  bool
     */
    public static function checkIfKeyNotExist(string $key, array $array): bool
    {
        return (!array_key_exists($key, $array) && empty($array[$key]));
    }

    /**
     * Check if required keys in array of parameters
     *
     * @param   array $keys
     * @param   array $array
     * @return  array|bool Return true if all fine, and string with name of key which was not found
     */
    public static function checkIfKeysNotExist(array $keys, array $array)
    {
        $output = [];
        foreach ($keys as $key) {
            if (self::checkIfKeyNotExist($key, $array)) {
                $output[] = $key;
            }
        }
        return !empty($output) ? implode(',', $output) : true;
    }
}


File: /vendor\evilfreelancer\routeros-api-php\src\Helpers\BinaryStringHelper.php
<?php

namespace RouterOS\Helpers;

/**
 * class BinaryStringHelper
 *
 * Strings and binary data manipulations
 *
 * @package RouterOS\Helpers
 * @since   0.9
 */
class BinaryStringHelper
{
    /**
     * Convert an integer value in a "Network Byte Ordered" binary string (most significant value first)
     *
     * Reads the integer, starting from the most significant byte, one byte a time.
     * Once reach a non 0 byte, construct a binary string representing this values
     * ex :
     *   0xFF7 => chr(0x0F).chr(0xF7)
     *   0x12345678 => chr(0x12).chr(0x34).chr(0x56).chr(0x76)
     * Compatible with 8, 16, 32, 64 etc.. bits systems
     *
     * @see https://en.wikipedia.org/wiki/Endianness
     * @param   int|float $value the integer value to be converted
     * @return  string the binary string
     */
    public static function IntegerToNBOBinaryString($value): string
    {
        // Initialize an empty string
        $buffer = '';

        // Lets start from the most significant byte
        for ($i = (PHP_INT_SIZE - 1); $i >= 0; $i--) {
            // Prepare a mask to keep only the most significant byte of $value
            $mask = 0xFF << ($i * 8);

            // If the most significant byte is not 0, the final string must contain it
            // If we have already started to construct the string (i.e. there are more signficant digits)
            //   we must set the byte, even if it is a 0.
            //   0xFF00FF, for example, require to set the second byte byte with a 0 value
            if (($value & $mask) || $buffer !== '') {
                // Get the current byte by shifting it to least significant position and add it to the string
                // 0xFF12345678 => 0xFF
                $byte   = $value >> (8 * $i);
                $buffer .= chr($byte);

                // Set the most significant byte to 0 so we can restart the process being shure
                // that the value is left padded with 0
                // 0xFF12345678 => 0x12345678
                // -1 = 0xFFFFF.... (number of F depend of PHP_INT_SIZE )
                $mask  = -1 >> ((PHP_INT_SIZE - $i) * 8);
                $value &= $mask;
            }
        }

        // Special case, 0 will not fill the buffer, have to construct it manualy
        if (0 === $value) {
            $buffer = chr(0);
        }

        return $buffer;
    }
}


File: /vendor\evilfreelancer\routeros-api-php\src\Helpers\TypeHelper.php
<?php

namespace RouterOS\Helpers;

/**
 * Class TypeHelper
 *
 * @package RouterOS\Helpers
 * @since   0.7
 */
class TypeHelper
{
    /**
     * Compare data types of some value
     *
     * @param   mixed  $whatType What type has value
     * @param   mixed  $isType   What type should be
     * @return  bool
     */
    public static function checkIfTypeMismatch($whatType, $isType): bool
    {
        return ($whatType !== $isType);
    }
}


File: /vendor\evilfreelancer\routeros-api-php\src\Interfaces\ClientInterface.php
<?php

namespace RouterOS\Interfaces;

use RouterOS\Client;
use RouterOS\Query;

/**
 * Interface ClientInterface
 *
 * @package RouterOS\Interfaces
 * @since   0.1
 */
interface ClientInterface
{
    /**
     * By default legacy login on RouterOS pre-6.43 is not supported
     */
    const LEGACY = false;

    /**
     * Default port number
     */
    const PORT = 8728;

    /**
     * Default ssl port number
     */
    const PORT_SSL = 8729;

    /**
     * Do not use SSL by default
     */
    const SSL = false;

    /**
     * Max timeout for answer from router
     */
    const TIMEOUT = 10;

    /**
     * Count of reconnect attempts
     */
    const ATTEMPTS = 10;

    /**
     * Delay between attempts in seconds
     */
    const ATTEMPTS_DELAY = 1;

    /**
     * Return socket resource if is exist
     *
     * @return resource
     */
    public function getSocket();

    /**
     * Read answer from server after query was executed
     *
     * @param bool $parse
     * @return mixed
     */
    public function read(bool $parse);

    /**
     * Send write query to RouterOS
     *
     * @param string|array|\RouterOS\Query $query
     * @return \RouterOS\Client
     */
    public function write($query): Client;

    /**
     * Send write query to RouterOS (modern version of write)
     *
     * @param string|Query $endpoint   Path of API query or Query object
     * @param array|null   $where      List of where filters
     * @param string|null  $operations Some operations which need make on response
     * @param string|null  $tag        Mark query with tag
     * @return \RouterOS\Client
     * @throws \RouterOS\Exceptions\QueryException
     * @since 1.0.0
     */
    public function query($endpoint, array $where, string $operations, string $tag): Client;
}


File: /vendor\evilfreelancer\routeros-api-php\src\Interfaces\ConfigInterface.php
<?php

namespace RouterOS\Interfaces;

use RouterOS\Config;

/**
 * Interface ConfigInterface
 *
 * @package RouterOS\Interfaces
 * @since   0.2
 */
interface ConfigInterface
{
    /**
     * List of allowed parameters of config
     */
    const ALLOWED = [
        // Address of Mikrotik RouterOS
        'host'     => 'string',
        // Username
        'user'     => 'string',
        // Password
        'pass'     => 'string',
        // RouterOS API port number for access (if not set use default or default with SSL if SSL enabled)
        'port'     => 'integer',
        // Enable ssl support (if port is not set this parameter must change default port to ssl port)
        'ssl'      => 'boolean',
        // Support of legacy login scheme (true - pre 6.43, false - post 6.43)
        'legacy'   => 'boolean',
        // Max timeout for answer from RouterOS
        'timeout'  => 'integer',
        // Count of attempts to establish TCP session
        'attempts' => 'integer',
        // Delay between attempts in seconds
        'delay'    => 'integer',
    ];

    /**
     * Set parameter into array
     *
     * @param   string $name
     * @param   mixed  $value
     * @return  Config
     */
    public function set(string $name, $value): Config;

    /**
     * Remove parameter from array by name
     *
     * @param   string $parameter
     * @return  Config
     */
    public function delete(string $parameter): Config;

    /**
     * Return parameter of current config by name
     *
     * @param   string $parameter
     * @return  mixed
     */
    public function get(string $parameter);

    /**
     * Return array with all parameters of configuration
     *
     * @return  array
     */
    public function getParameters(): array;
}


File: /vendor\evilfreelancer\routeros-api-php\src\Interfaces\QueryInterface.php
<?php

namespace RouterOS\Interfaces;

use RouterOS\Query;

/**
 * Interface QueryInterface
 *
 * @package RouterOS\Interfaces
 * @since   0.2
 */
interface QueryInterface
{
    /**
     * Where logic of query
     *
     * @param string          $key      Key which need to find
     * @param bool|string|int $value    Value which need to check (by default true)
     * @param bool|string|int $operator It may be one from list [-,=,>,<]
     * @return \RouterOS\Query
     * @throws \RouterOS\Exceptions\ClientException
     * @since 1.0.0
     */
    public function where(string $key, $operator = '=', $value = null);

    /**
     * Append additional operations
     *
     * @param string $operations
     * @since 1.0.0
     */
    public function operations(string $operations);

    /**
     * Append tag to query (it should be at end)
     *
     * @param string $name
     * @since 1.0.0
     */
    public function tag(string $name);

    /**
     * Append to array yet another attribute of query
     *
     * @param string $word
     * @return \RouterOS\Query
     */
    public function add(string $word): Query;

    /**
     * Get attributes array of current query
     *
     * @return array
     */
    public function getAttributes(): array;

    /**
     * Set array of attributes
     *
     * @param array $attributes
     * @return \RouterOS\Query
     * @since 0.7
     */
    public function setAttributes(array $attributes): Query;

    /**
     * Get endpoint of current query
     *
     * @return string|null
     */
    public function getEndpoint();

    /**
     * Set endpoint of query
     *
     * @param string $endpoint
     * @return \RouterOS\Query
     * @since 0.7
     */
    public function setEndpoint(string $endpoint): Query;

    /**
     * Build body of query
     *
     * @return array
     * @throws \RouterOS\Exceptions\QueryException
     */
    public function getQuery(): array;
}


File: /vendor\evilfreelancer\routeros-api-php\src\Interfaces\StreamInterface.php
<?php

namespace RouterOS\Interfaces;

/**
 * Interface QueryInterface
 *
 * Stream abstraction
 *
 * @package RouterOS\Interfaces
 * @since   0.9
 */
interface StreamInterface
{
    /**
     * Reads a stream
     *
     * Reads $length bytes from the stream, returns the bytes into a string
     * Must be binary safe (as fread).
     *
     * @param   int $length the numer of bytes to read
     * @return  string a binary string containing the readed byes
     */
    public function read(int $length): string;

    /**
     * Writes a string to a stream
     *
     * Write $length bytes of string, if not mentioned, write all the string
     * Must be binary safe (as fread).
     * if $length is greater than string length, write all string and return number of writen bytes
     * if $length os smaller than string length, remaining bytes are losts.
     *
     * @param   string $string
     * @param   int    $length the number of bytes to read
     * @return  int return number of written bytes
     */
    public function write(string $string, int $length = -1): int;

    /**
     * Close stream connection
     *
     * @return void
     */
    public function close();
}


File: /vendor\evilfreelancer\routeros-api-php\src\Query.php
<?php

namespace RouterOS;

use RouterOS\Exceptions\ClientException;
use RouterOS\Exceptions\QueryException;
use RouterOS\Interfaces\QueryInterface;

/**
 * Class Query for building queries
 *
 * @package RouterOS
 * @since   0.1
 */
class Query implements QueryInterface
{
    /**
     * Array of query attributes
     *
     * @var array
     */
    private $_attributes = [];

    /**
     * Some additional operations
     *
     * @var string
     */
    private $_operations;

    /**
     * Tag of query
     *
     * @var string
     */
    private $_tag;

    /**
     * Endpoint of query
     *
     * @var string
     */
    private $_endpoint;

    /**
     * List of available operators for "->where()" method
     */
    public const AVAILABLE_OPERATORS = [
        '-',  // Does not have
        '=',  // Equal
        '>',  // More than
        '<'   // Less than
    ];

    /**
     * Query constructor.
     *
     * @param array|string $endpoint   Path of endpoint
     * @param array        $attributes List of attributes which should be set
     *
     * @throws \RouterOS\Exceptions\QueryException
     */
    public function __construct($endpoint, array $attributes = [])
    {
        if (\is_string($endpoint)) {
            $this->setEndpoint($endpoint);
            $this->setAttributes($attributes);
        } elseif (\is_array($endpoint)) {
            $query = array_shift($endpoint);
            $this->setEndpoint($query);
            $this->setAttributes($endpoint);
        } else {
            throw new QueryException('Specified endpoint is incorrect');
        }
    }

    /**
     * Where logic of query
     *
     * @param string          $key      Key which need to find
     * @param bool|string|int $value    Value which need to check (by default true)
     * @param bool|string|int $operator It may be one from list [-,=,>,<]
     *
     * @return \RouterOS\Query
     * @throws \RouterOS\Exceptions\QueryException
     * @since 1.0.0
     */
    public function where(string $key, $operator = null, $value = null): self
    {
        return $this->world('?' . $key, $operator, $value);
    }

    /**
     * Setter for write/update queries
     *
     * @param string          $key   Key which need to find
     * @param bool|string|int $value Value which need to check (by default true)
     *
     * @return \RouterOS\Query
     * @throws \RouterOS\Exceptions\QueryException
     * @since 1.1
     */
    public function equal(string $key, $value = null): self
    {
        return $this->world('=' . $key, null, $value);
    }

    /**
     * Write world to RouterOS (the work is mine)
     *
     * @param string          $key      Key which need to find
     * @param bool|string|int $value    Value which need to check (by default true)
     * @param bool|string|int $operator It may be one from list [-,=,>,<]
     *
     * @return \RouterOS\Query
     * @throws \RouterOS\Exceptions\QueryException
     */
    private function world(string $key, $operator = null, $value = null): self
    {
        if (null !== $operator && null === $value) {

            // Client may set only two parameters, that mean what $operator is $value
            $value = $operator;

            // And operator should be "="
            $operator = null;
        }

        if (null !== $operator && null !== $value) {
            // If operator is available in list
            if (\in_array($operator, self::AVAILABLE_OPERATORS, true)) {
                $key = $operator . $key;
            } else {
                throw new QueryException('Operator "' . $operator . '" in not in allowed list [' . implode(',', self::AVAILABLE_OPERATORS) . ']');
            }
        }

        if (null !== $value) {
            $value = '=' . $value;
        }

        $this->add($key . $value);
        return $this;
    }

    /**
     * Append additional operations
     *
     * @param string $operations
     *
     * @return \RouterOS\Query
     * @since 1.0.0
     */
    public function operations(string $operations): self
    {
        $this->_operations = '?#' . $operations;
        return $this;
    }

    /**
     * Append tag to query (it should be at end)
     *
     * @param string $name
     *
     * @return \RouterOS\Query
     * @since 1.0.0
     */
    public function tag(string $name): self
    {
        $this->_tag = '.tag=' . $name;
        return $this;
    }

    /**
     * Append to array yet another attribute of query
     *
     * @param string $word
     *
     * @return \RouterOS\Query
     */
    public function add(string $word): Query
    {
        $this->_attributes[] = $word;
        return $this;
    }

    /**
     * Get attributes array of current query
     *
     * @return array
     */
    public function getAttributes(): array
    {
        return $this->_attributes;
    }

    /**
     * Set array of attributes
     *
     * @param array $attributes
     *
     * @return \RouterOS\Query
     * @since 0.7
     */
    public function setAttributes(array $attributes): Query
    {
        $this->_attributes = $attributes;
        return $this;
    }

    /**
     * Get endpoint of current query
     *
     * @return string|null
     */
    public function getEndpoint()
    {
        return $this->_endpoint;
    }

    /**
     * Set endpoint of query
     *
     * @param string|null $endpoint
     *
     * @return \RouterOS\Query
     * @since 0.7
     */
    public function setEndpoint(string $endpoint = null): Query
    {
        $this->_endpoint = $endpoint;
        return $this;
    }

    /**
     * Build body of query
     *
     * @return array
     * @throws \RouterOS\Exceptions\QueryException
     */
    public function getQuery(): array
    {
        if ($this->_endpoint === null) {
            throw new QueryException('Endpoint of query is not set');
        }

        // Get all attributes and prepend endpoint to this list
        $attributes = $this->getAttributes();
        array_unshift($attributes, $this->_endpoint);

        // If operations is set then add to query
        if (is_string($this->_operations) && !empty($this->_operations)) {
            $attributes[] = $this->_operations;
        }

        // If tag is set then added to query
        if (is_string($this->_tag) && !empty($this->_tag)) {
            $attributes[] = $this->_tag;
        }

        return $attributes;
    }
}


File: /vendor\evilfreelancer\routeros-api-php\src\ResponseIterator.php
<?php

namespace RouterOS;

use \Iterator,
    \ArrayAccess,
    \Countable,
    \Serializable;

/**
 * This class was created by memory save reasons, it convert response
 * from RouterOS to readable array in safe way.
 *
 * @param array $raw Array RAW response from server
 * @return mixed
 *
 * Based on RouterOSResponseArray solution by @arily
 *
 * @package RouterOS\Iterators
 * @link    https://github.com/arily/RouterOSResponseArray
 * @since   1.0.0
 */
class ResponseIterator implements Iterator, ArrayAccess, Countable, Serializable
{
    /**
     * List of parser results from array
     *
     * @var array
     */
    private $parsed = [];

    /**
     * List of RAW results from RouterOS
     *
     * @var array
     */
    private $raw = [];

    /**
     * Initial value of array position
     *
     * @var int
     */
    private $current = 0;

    /**
     * Object of main client
     *
     * @var \RouterOS\Client
     */
    private $client;

    /**
     * ResponseIterator constructor.
     *
     * @param Client $client
     */
    public function __construct(Client $client)
    {
        // Set current to default
        $this->rewind();

        // Save client as parameter of object
        $this->client = $client;

        // Read RAW data from client
        $raw = $client->read(false);

        // This RAW should't be an error
        $positions = array_keys($raw, '!re');
        $count     = count($raw);
        $result    = [];

        if (isset($positions[1])) {

            foreach ($positions as $key => $position) {

                // Get length of future block
                $length = isset($positions[$key + 1])
                    ? $positions[$key + 1] - $position + 1
                    : $count - $position;

                // Convert array to simple items, save as result
                $result[] = array_slice($raw, $position, $length);
            }

        } else {
            $result = [$raw];
        }

        $this->raw = $result;
    }

    /**
     * Move forward to next element
     */
    public function next()
    {
        ++$this->current;
    }

    /**
     * Previous value
     */
    public function prev()
    {
        --$this->current;
    }

    /**
     * Return the current element
     *
     * @return mixed
     */
    public function current()
    {
        if (isset($this->parsed[$this->current])) {
            return $this->parsed[$this->current];
        }

        if ($this->valid()) {

            if (!isset($this->parsed[$this->current])) {
                $value = $this->client->parseResponse($this->raw[$this->current])[0];
                $this->offsetSet($this->current, $value);
            }

            return $this->parsed[$this->current];
        }

        return null;
    }

    /**
     * Return the key of the current element
     *
     * @return mixed
     */
    public function key()
    {
        return $this->current;
    }

    /**
     * Checks if current position is valid
     *
     * @return bool
     */
    public function valid(): bool
    {
        return isset($this->raw[$this->current]);
    }

    /**
     * Count elements of an object
     *
     * @return int
     */
    public function count(): int
    {
        return count($this->raw);
    }

    /**
     * Rewind the Iterator to the first element
     */
    public function rewind()
    {
        $this->current = 0;
    }

    /**
     * Offset to set
     *
     * @param mixed $offset
     * @param mixed $value
     */
    public function offsetSet($offset, $value)
    {
        if (null === $offset) {
            $this->parsed[] = $value;
        } else {
            $this->parsed[$offset] = $value;
        }
    }

    /**
     * Whether a offset exists
     *
     * @param mixed $offset
     * @return bool
     */
    public function offsetExists($offset): bool
    {
        return isset($this->raw[$offset]) && $this->raw[$offset] !== ['!re'];
    }

    /**
     * Offset to unset
     *
     * @param mixed $offset
     */
    public function offsetUnset($offset)
    {
        unset($this->parsed[$offset], $this->raw[$offset]);
    }

    /**
     * Offset to retrieve
     *
     * @param mixed $offset
     * @return bool|mixed
     */
    public function offsetGet($offset)
    {
        if (isset($this->parsed[$offset])) {
            return $this->parsed[$offset];
        }

        if (isset($this->raw[$offset]) && $this->raw[$offset] !== null) {
            $f = $this->client->parseResponse($this->raw[$offset]);
            if ($f !== []) {
                return $this->parsed[$offset] = $f[0];
            }
        }

        return false;
    }

    /**
     * String representation of object
     *
     * @return string
     */
    public function serialize(): string
    {
        return serialize($this->raw);
    }

    /**
     * Constructs the object
     *
     * @param string $serialized
     */
    public function unserialize($serialized)
    {
        $this->raw = unserialize($serialized, null);
    }
}


File: /vendor\evilfreelancer\routeros-api-php\src\ShortsTrait.php
<?php

namespace RouterOS;

/**
 * Trait ShortsTrait
 *
 * All shortcuts was moved to this class
 *
 * @package RouterOS
 * @since   1.0.0
 * @codeCoverageIgnore
 */
trait ShortsTrait
{
    /**
     * Alias for ->write() method
     *
     * @param string|array|\RouterOS\Query $query
     * @return \RouterOS\Client
     * @throws \RouterOS\Exceptions\QueryException
     * @deprecated
     */
    public function w($query): Client
    {
        return $this->write($query);
    }

    /**
     * Alias for ->query() method
     *
     * @param string      $endpoint   Path of API query
     * @param array|null  $where      List of where filters
     * @param string|null $operations Some operations which need make on response
     * @param string|null $tag        Mark query with tag
     * @return \RouterOS\Client
     * @throws \RouterOS\Exceptions\QueryException
     * @since 1.0.0
     */
    public function q(string $endpoint, array $where = null, string $operations = null, string $tag = null): Client
    {
        return $this->query($endpoint, $where, $operations, $tag);
    }

    /**
     * Alias for ->read() method
     *
     * @param bool $parse
     * @return mixed
     * @since 0.7
     */
    public function r(bool $parse = true)
    {
        return $this->read($parse);
    }

    /**
     * Alias for ->readAsIterator() method
     *
     * @return \RouterOS\ResponseIterator
     * @since 1.0.0
     */
    public function ri(): ResponseIterator
    {
        return $this->readAsIterator();
    }

    /**
     * Alias for ->write()->read() combination of methods
     *
     * @param string|array|\RouterOS\Query $query
     * @param bool                         $parse
     * @return array
     * @throws \RouterOS\Exceptions\ClientException
     * @throws \RouterOS\Exceptions\QueryException
     * @since 0.6
     * @deprecated
     */
    public function wr($query, bool $parse = true): array
    {
        return $this->write($query)->read($parse);
    }

    /**
     * Alias for ->write()->read() combination of methods
     *
     * @param string      $endpoint   Path of API query
     * @param array|null  $where      List of where filters
     * @param string|null $operations Some operations which need make on response
     * @param string|null $tag        Mark query with tag
     * @param bool        $parse
     * @return \RouterOS\Client
     * @throws \RouterOS\Exceptions\QueryException
     * @since 1.0.0
     */
    public function qr(string $endpoint, array $where = null, string $operations = null, string $tag = null, bool $parse = true): array
    {
        return $this->query($endpoint, $where, $operations, $tag)->read($parse);
    }

    /**
     * Alias for ->write()->readAsIterator() combination of methods
     *
     * @param string|array|\RouterOS\Query $query
     * @return \RouterOS\ResponseIterator
     * @throws \RouterOS\Exceptions\ClientException
     * @throws \RouterOS\Exceptions\QueryException
     * @since 1.0.0
     * @deprecated
     */
    public function wri($query): ResponseIterator
    {
        return $this->write($query)->readAsIterator();
    }

    /**
     * Alias for ->write()->read() combination of methods
     *
     * @param string      $endpoint   Path of API query
     * @param array|null  $where      List of where filters
     * @param string|null $operations Some operations which need make on response
     * @param string|null $tag        Mark query with tag
     * @return \RouterOS\ResponseIterator
     * @throws \RouterOS\Exceptions\QueryException
     * @since 1.0.0
     */
    public function qri(string $endpoint, array $where = null, string $operations = null, string $tag = null): ResponseIterator
    {
        return $this->query($endpoint, $where, $operations, $tag)->readAsIterator();
    }
}


File: /vendor\evilfreelancer\routeros-api-php\src\SocketTrait.php
<?php

namespace RouterOS;

use RouterOS\Exceptions\ClientException;

trait SocketTrait
{
    /**
     * Socket resource
     *
     * @var resource|null
     */
    private $_socket;

    /**
     * Code of error
     *
     * @var int
     */
    private $_socket_err_num;

    /**
     * Description of socket error
     *
     * @var string
     */
    private $_socket_err_str;

    /**
     * Initiate socket session
     *
     * @return  void
     * @throws  \RouterOS\Exceptions\ClientException
     * @throws  \RouterOS\Exceptions\ConfigException
     */
    private function openSocket()
    {
        // Default: Context for ssl
        $context = stream_context_create([
            'ssl' => [
                'ciphers'          => 'ADH:ALL',
                'verify_peer'      => false,
                'verify_peer_name' => false
            ]
        ]);

        // Default: Proto tcp:// but for ssl we need ssl://
        $proto = $this->config('ssl') ? 'ssl://' : '';

        // Initiate socket client
        $socket = @stream_socket_client(
            $proto . $this->config('host') . ':' . $this->config('port'),
            $this->_socket_err_num,
            $this->_socket_err_str,
            $this->config('timeout'),
            STREAM_CLIENT_CONNECT,
            $context
        );

        // Throw error is socket is not initiated
        if (false === $socket) {
            throw new ClientException('Unable to establish socket session, ' . $this->_socket_err_str);
        }

        // Save socket to static variable
        $this->setSocket($socket);
    }

    /**
     * Close socket session
     *
     * @return bool
     */
    private function closeSocket(): bool
    {
        return fclose($this->_socket);
    }

    /**
     * Save socket resource to static variable
     *
     * @param   resource $socket
     * @return  void
     */
    private function setSocket($socket)
    {
        $this->_socket = $socket;
    }

    /**
     * Return socket resource if is exist
     *
     * @return  resource
     */
    public function getSocket()
    {
        return $this->_socket;
    }
}


File: /vendor\evilfreelancer\routeros-api-php\src\Streams\ResourceStream.php
<?php

namespace RouterOS\Streams;

use RouterOS\Interfaces\StreamInterface;
use RouterOS\Exceptions\StreamException;

/**
 * class ResourceStream
 *
 * Stream using a resource (socket, file, pipe etc.)
 *
 * @package RouterOS
 * @since   0.9
 */
class ResourceStream implements StreamInterface
{
    protected $stream;

    /**
     * ResourceStream constructor.
     *
     * @param $stream
     */
    public function __construct($stream)
    {
        if (!is_resource($stream)) {
            throw new \InvalidArgumentException(
                sprintf(
                    'Argument must be a valid resource type. %s given.',
                    gettype($stream)
                )
            );
        }

        // TODO: Should we verify the resource type?
        $this->stream = $stream;
    }

    /**
     * @param   int $length
     * @return  string
     * @throws  \RouterOS\Exceptions\StreamException
     * @throws  \InvalidArgumentException
     */
    public function read(int $length): string
    {
        if ($length <= 0) {
            throw new \InvalidArgumentException('Cannot read zero ot negative count of bytes from a stream');
        }

        // TODO: Ignore errors here, but why?
        $result = @fread($this->stream, $length);

        if (false === $result) {
            throw new StreamException("Error reading $length bytes");
        }

        return $result;
    }

    /**
     * Writes a string to a stream
     *
     * Write $length bytes of string, if not mentioned, write all the string
     * Must be binary safe (as fread).
     * if $length is greater than string length, write all string and return number of writen bytes
     * if $length os smaller than string length, remaining bytes are losts.
     *
     * @param   string   $string
     * @param   int|null $length the numer of bytes to read
     * @return  int the number of written bytes
     * @throws  \RouterOS\Exceptions\StreamException
     */
    public function write(string $string, int $length = null): int
    {
        if (null === $length) {
            $length = strlen($string);
        }

        // TODO: Ignore errors here, but why?
        $result = @fwrite($this->stream, $string, $length);

        if (false === $result) {
            throw new StreamException("Error writing $length bytes");
        }

        return $result;
    }

    /**
     * Close stream connection
     *
     * @return  void
     * @throws  \RouterOS\Exceptions\StreamException
     */
    public function close()
    {
        $hasBeenClosed = false;

        if (null !== $this->stream) {
            $hasBeenClosed = @fclose($this->stream);
            $this->stream  = null;
        }

        if (false === $hasBeenClosed) {
            throw new StreamException('Error closing stream');
        }
    }
}


File: /vendor\evilfreelancer\routeros-api-php\src\Streams\StringStream.php
<?php

namespace RouterOS\Streams;

use RouterOS\Interfaces\StreamInterface;
use RouterOS\Exceptions\StreamException;

/**
 * class StringStream
 *
 * Initialized with a string, the read method retreive it as done with fread, consuming the buffer.
 * When all the string has been read, exception is thrown when try to read again.
 *
 * @package RouterOS\Streams
 * @since   0.9
 */
class StringStream implements StreamInterface
{
    /**
     * @var string $buffer Stores the string to use
     */
    protected $buffer;

    /**
     * StringStream constructor.
     *
     * @param string $string
     */
    public function __construct(string $string)
    {
        $this->buffer = $string;
    }

    /**
     * {@inheritDoc}
     *
     * @throws \InvalidArgumentException when length parameter is invalid
     * @throws StreamException when the stream have been tatly red and read methd is called again
     */
    public function read(int $length): string
    {
        $remaining = strlen($this->buffer);

        if ($length < 0) {
            throw new \InvalidArgumentException('Cannot read a negative count of bytes from a stream');
        }

        if (0 === $remaining) {
            throw new StreamException('End of stream');
        }

        if ($length >= $remaining) {
            // returns all 
            $result = $this->buffer;
            // No more in the buffer
            $this->buffer = '';
        } else {
            // acquire $length characters from the buffer
            $result = substr($this->buffer, 0, $length);
            // remove $length characters from the buffer
            $this->buffer = substr_replace($this->buffer, '', 0, $length);
        }

        return $result;
    }

    /**
     * Fake write method, do nothing except return the "writen" length
     *
     * @param   string   $string The string to write
     * @param   int|null $length the number of characters to write
     * @return  int number of "writen" bytes
     * @throws  \InvalidArgumentException on invalid length
     */
    public function write(string $string, int $length = null): int
    {
        if (null === $length) {
            $length = strlen($string);
        }

        if ($length < 0) {
            throw new \InvalidArgumentException('Cannot write a negative count of bytes');
        }

        return min($length, strlen($string));
    }

    /**
     * Close stream connection
     *
     * @return  void
     */
    public function close()
    {
        $this->buffer = '';
    }
}


File: /vendor\evilfreelancer\routeros-api-php\tests\APIConnectorTest.php
<?php

namespace RouterOS\Tests;

use PHPUnit\Framework\TestCase;
use RouterOS\APIConnector;
use RouterOS\Streams\StringStream;
use RouterOS\Streams\ResourceStream;
use RouterOS\APILengthCoDec;
use RouterOS\Interfaces\StreamInterface;

/**
 * Limit code coverage to the class RouterOS\APIStream
 *
 * @coversDefaultClass \RouterOS\APIConnector
 */
class APIConnectorTest extends TestCase
{
    /**
     * Test that constructor is OK with different kinds of resources
     *
     * @covers ::__construct
     * @dataProvider constructProvider
     *
     * @param StreamInterface $stream        Cannot typehint, PHP refuse it
     * @param bool            $closeResource shall we close the resource ?
     */
    public function test_construct(StreamInterface $stream, bool $closeResource = false)
    {
        $apiStream = new APIConnector($stream);
        $this->assertInstanceOf(APIConnector::class, $apiStream);
        if ($closeResource) {
            $apiStream->close();
        }
    }

    public function constructProvider(): array
    {
        return [
            [new ResourceStream(fopen(__FILE__, 'rb')),], // Myself, sure I exists
            [new ResourceStream(fsockopen('tcp://' . getenv('ROS_HOST'), getenv('ROS_PORT_MODERN'))),], // Socket
            [new ResourceStream(STDIN), false], // Try it, but do not close STDIN please !!!
            [new StringStream('Hello World !!!')], // Try it, but do not close STDIN please !!!
            [new StringStream('')], // Try it, but do not close STDIN please !!!
            // What else ?
        ];
    }

    /**
     * @covers ::readWord
     * @dataProvider readWordProvider
     *
     * @param APIConnector $connector
     * @param string       $expected
     */
    public function test__readWord(APIConnector $connector, string $expected)
    {
        $this->assertSame($expected, $connector->readWord());
    }

    public function readWordProvider(): array
    {
        $longString = '=comment=' . str_repeat('a', 10000);
        $length     = strlen($longString);

        return [
            [new APIConnector(new StringStream(chr(0))), ''],
            [new APIConnector(new StringStream(chr(3) . '!re')), '!re'],
            [new APIConnector(new StringStream(chr(5) . '!done')), '!done'],
            [new APIConnector(new StringStream(APILengthCoDec::encodeLength($length) . $longString)), $longString],
        ];
    }

    /**
     * @covers ::writeWord
     * @dataProvider writeWordProvider
     *
     * @param APIConnector $connector
     * @param string       $toWrite
     * @param int          $expected
     */
    public function test_writeWord(APIConnector $connector, string $toWrite, int $expected)
    {
        $this->assertEquals($expected, $connector->writeWord($toWrite));
    }

    public function writeWordProvider(): array
    {
        return [
            [new APIConnector(new StringStream('Have FUN !!!')), '', 1], // length is 0, but have to write it on 1 byte, minimum
            [new APIConnector(new StringStream('Have FUN !!!')), str_repeat(' ', 54), 55],  // arbitrary value
            [new APIConnector(new StringStream('Have FUN !!!')), str_repeat(' ', 127), 128], // maximum value for 1 byte encoding lentgth
            [new APIConnector(new StringStream('Have FUN !!!')), str_repeat(' ', 128), 130], // minimum value for 2 bytes encoding lentgth
            [new APIConnector(new StringStream('Have FUN !!!')), str_repeat(' ', 254), 256], // special value isn't it ?
            [new APIConnector(new StringStream('Have FUN !!!')), str_repeat(' ', 255), 257], // special value isn't it ?
        ];
    }
}


File: /vendor\evilfreelancer\routeros-api-php\tests\APILengthCoDecTest.php
<?php

namespace RouterOS\Tests;

use PHPUnit\Framework\TestCase;
use PHPUnit\Framework\Constraint\IsType;

use RouterOS\APILengthCoDec;
use RouterOS\Streams\StringStream;
use RouterOS\Helpers\BinaryStringHelper;

/**
 * Limit code coverage to the class
 *
 * @coversDefaultClass \RouterOS\APILengthCoDec
 */
class APILengthCoDecTest extends TestCase
{
    /**
     * @dataProvider encodeLengthNegativeProvider
     * @expectedException \DomainException
     * @covers ::encodeLength
     */
    public function test__encodeLengthNegative($length)
    {
        APILengthCoDec::encodeLength($length);
    }

    public function encodeLengthNegativeProvider(): array
    {
        return [
            [-1],
            [PHP_INT_MIN],
        ];
    }

    /**
     * @dataProvider encodedLengthProvider
     * @covers ::encodeLength
     */
    public function test__encodeLength($expected, $length)
    {
        $this->assertEquals(BinaryStringHelper::IntegerToNBOBinaryString((int) $expected), APILengthCoDec::encodeLength($length));
    }

    public function encodedLengthProvider(): array
    {
        // [encoded length value, length value] 
        $result = [
            [0, 0],        // Low limit value for 1 byte encoded length
            [0x39, 0x39],  // Arbitrary median value for 1 byte encoded length
            [0x7f, 0x7F],  // High limit value for 1 byte encoded length

            [0x8080, 0x80],   // Low limit value for 2 bytes encoded length
            [0x9C42, 0x1C42], // Arbitrary median value for 2 bytes encoded length
            [0xBFFF, 0x3FFF], // High limit value for 2 bytes encoded length

            [0xC04000, 0x4000],   // Low limit value for 3 bytes
            [0xCAD73B, 0xAD73B],  // Arbitrary median value for 3 bytes encoded length
            [0xDFFFFF, 0x1FFFFF], // High limit value for 3 bytes encoded length

            [0xE0200000, 0x200000],   // Low limit value for 4 bytes encoded length
            [0xE5AD736B, 0x5AD736B],  // Arbitrary median value for 4 bytes encoded length
            [0xEFFFFFFF, 0xFFFFFFF],  // High limit value for 4 bytes encoded length
        ];

        if (PHP_INT_SIZE > 4) {
            $result[] = [0xF010000000, 0x10000000];  // Low limit value for 5 bytes encoded length
            $result[] = [0xF10D4EF9C3, 0x10D4EF9C3]; // Arbitrary median value for 5 bytes encoded length
            $result[] = [0xF7FFFFFFFF, 0x7FFFFFFFF]; // High limit value for 5 bytes encoded length
        }

        return $result;
    }

    /**
     * @dataProvider encodedLengthProvider
     * @covers ::decodeLength
     */
    public function test__decodeLength($encodedLength, $expected)
    {
        // We have to provide $encodedLength as a "bytes" stream
        $stream = new StringStream(BinaryStringHelper::IntegerToNBOBinaryString($encodedLength));
        $this->assertEquals($expected, APILengthCoDec::decodeLength($stream));
    }

    /**
     * @dataProvider decodeLengthControlWordProvider
     * @covers ::decodeLength
     * @expectedException \UnexpectedValueException
     */
    public function test_decodeLengthControlWord(string $encodedLength)
    {
        APILengthCoDec::decodeLength(new StringStream($encodedLength));
    }

    public function decodeLengthControlWordProvider(): array
    {
        // Control bytes: 5 most significance its sets to 1
        return [
            [chr(0xF8)], // minimum
            [chr(0xFC)], // arbitrary value
            [chr(0xFF)], // maximum
        ];
    }
}


File: /vendor\evilfreelancer\routeros-api-php\tests\ClientTest.php
<?php

namespace RouterOS\Tests;

use PHPUnit\Framework\TestCase;
use RouterOS\Client;
use RouterOS\Exceptions\ConfigException;
use RouterOS\Exceptions\QueryException;
use RouterOS\Query;
use RouterOS\Config;
use RouterOS\Exceptions\ClientException;

class ClientTest extends TestCase
{
    public function test__construct(): void
    {
        try {
            $config = new Config();
            $config->set('user', getenv('ROS_USER'))->set('pass', getenv('ROS_PASS'))->set('host', getenv('ROS_HOST'));
            $obj = new Client($config);
            $this->assertIsObject($obj);
            $socket = $obj->getSocket();
            $this->assertIsResource($socket);
        } catch (\Exception $e) {
            $this->assertContains('Must be initialized ', $e->getMessage());
        }
    }

    public function test__construct2(): void
    {
        try {
            $config = new Config([
                'user' => getenv('ROS_USER'),
                'pass' => getenv('ROS_PASS'),
                'host' => getenv('ROS_HOST')
            ]);
            $obj    = new Client($config);
            $this->assertIsObject($obj);
            $socket = $obj->getSocket();
            $this->assertIsResource($socket);
        } catch (\Exception $e) {
            $this->assertContains('Must be initialized ', $e->getMessage());
        }
    }

    public function test__construct3(): void
    {
        try {
            $obj = new Client([
                'user' => getenv('ROS_USER'),
                'pass' => getenv('ROS_PASS'),
                'host' => getenv('ROS_HOST')
            ]);
            $this->assertIsObject($obj);
            $socket = $obj->getSocket();
            $this->assertIsResource($socket);
        } catch (\Exception $e) {
            $this->assertContains('Must be initialized ', $e->getMessage());
        }
    }

    public function test__constructEx(): void
    {
        $this->expectException(ConfigException::class);

        $obj = new Client([
            'user' => getenv('ROS_USER'),
            'pass' => getenv('ROS_PASS'),
        ]);
    }

    public function test__constructLegacy(): void
    {
        try {
            $obj = new Client([
                'user'   => getenv('ROS_USER'),
                'pass'   => getenv('ROS_PASS'),
                'host'   => getenv('ROS_HOST'),
                'port'   => (int) getenv('ROS_PORT_MODERN'),
                'legacy' => true
            ]);
            $this->assertIsObject($obj);
        } catch (\Exception $e) {
            $this->assertContains('Must be initialized ', $e->getMessage());
        }
    }

    /**
     * Test non legacy connection on legacy router (pre 6.43)
     *
     * login() method recognise legacy router response and swap to legacy mode
     */
    public function test__constructLegacy2(): void
    {
        try {
            $obj = new Client([
                'user'   => getenv('ROS_USER'),
                'pass'   => getenv('ROS_PASS'),
                'host'   => getenv('ROS_HOST'),
                'port'   => (int) getenv('ROS_PORT_MODERN'),
                'legacy' => false
            ]);
            $this->assertIsObject($obj);
        } catch (\Exception $e) {
            $this->assertContains('Must be initialized ', $e->getMessage());
        }
    }


    public function test__constructWrongPass(): void
    {
        $this->expectException(ClientException::class);

        $obj = new Client([
            'user'     => getenv('ROS_USER'),
            'pass'     => 'admin2',
            'host'     => getenv('ROS_HOST'),
            'attempts' => 2
        ]);
    }

    /**
     * @expectedException ClientException
     */
    public function test__constructWrongNet(): void
    {
        $this->expectException(ClientException::class);

        $obj = new Client([
            'user'     => getenv('ROS_USER'),
            'pass'     => getenv('ROS_PASS'),
            'host'     => getenv('ROS_HOST'),
            'port'     => 11111,
            'attempts' => 2
        ]);
    }

    public function testQueryRead(): void
    {
        $config = new Config();
        $config->set('user', getenv('ROS_USER'))->set('pass', getenv('ROS_PASS'))->set('host', getenv('ROS_HOST'));
        $obj = new Client($config);

        /*
         * Build query with where
         */

        $read = $obj->query('/system/package/print', ['name'])->read();
        $this->assertCount(13, $read);

        $read = $obj->query('/system/package/print', ['.id', '*1'])->read();
        $this->assertCount(1, $read);

        $read = $obj->query('/system/package/print', ['.id', '=', '*1'])->read();
        $this->assertCount(1, $read);

        $read = $obj->query('/system/package/print', [['name']])->read();
        $this->assertCount(13, $read);

        $read = $obj->query('/system/package/print', [['.id', '*1']])->read();
        $this->assertCount(1, $read);

        $read = $obj->query('/system/package/print', [['.id', '=', '*1']])->read();
        $this->assertCount(1, $read);

        /*
         * Build query with operations
         */

        $read = $obj->query('/interface/print', [
            ['type', 'ether'],
            ['type', 'vlan']
        ], '|')->read();
        $this->assertCount(1, $read);
        $this->assertEquals('*1', $read[0]['.id']);

        /*
         * Build query with tag
         */

        $read = $obj->query('/system/package/print', null, null, 'zzzz')->read();
        $this->assertCount(13, $read);
        $this->assertEquals('zzzz', $read[0]['tag']);
    }

    public function testReadAsIterator(): void
    {
        $obj = new Client([
            'user' => getenv('ROS_USER'),
            'pass' => getenv('ROS_PASS'),
            'host' => getenv('ROS_HOST'),
        ]);

        $obj = $obj->write('/system/package/print')->readAsIterator();
        $this->assertIsObject($obj);
    }

    public function testWriteReadString(): void
    {
        $obj = new Client([
            'user' => getenv('ROS_USER'),
            'pass' => getenv('ROS_PASS'),
            'host' => getenv('ROS_HOST'),
        ]);

        $readTrap = $obj->wr('/interface', false);
        $this->assertCount(3, $readTrap);
        $this->assertEquals('!trap', $readTrap[0]);
    }

    public function testFatal(): void
    {
        $obj = new Client([
            'user' => getenv('ROS_USER'),
            'pass' => getenv('ROS_PASS'),
            'host' => getenv('ROS_HOST'),
        ]);

        $readTrap = $obj->query('/quit')->read();
        $this->assertCount(2, $readTrap);
        $this->assertEquals('!fatal', $readTrap[0]);
    }

    public function testQueryEx1(): void
    {
        $this->expectException(ClientException::class);

        $obj = new Client([
            'user' => getenv('ROS_USER'),
            'pass' => getenv('ROS_PASS'),
            'host' => getenv('ROS_HOST'),
        ]);

        $obj->query('/quiet', ['a', 'b', 'c', 'd']);
    }

    public function testQueryEx2(): void
    {
        $this->expectException(ClientException::class);

        $obj = new Client([
            'user' => getenv('ROS_USER'),
            'pass' => getenv('ROS_PASS'),
            'host' => getenv('ROS_HOST'),
        ]);

        $obj->query('/quiet', [[]]);
    }
}


File: /vendor\evilfreelancer\routeros-api-php\tests\ConfigTest.php
<?php

namespace RouterOS\Tests;

use PHPUnit\Framework\TestCase;
use RouterOS\Config;
use RouterOS\Exceptions\ConfigException;

class ConfigTest extends TestCase
{
    public function test__construct()
    {
        try {
            $obj = new Config();
            $this->assertInternalType('object', $obj);
        } catch (\Exception $e) {
            $this->assertContains('Must be initialized ', $e->getMessage());
        }
    }

    public function testGetParameters()
    {
        $obj    = new Config();
        $params = $obj->getParameters();

        $this->assertCount(5, $params);
        $this->assertEquals($params['legacy'], false);
        $this->assertEquals($params['ssl'], false);
        $this->assertEquals($params['timeout'], 10);
        $this->assertEquals($params['attempts'], 10);
        $this->assertEquals($params['delay'], 1);
    }

    public function testGetParameters2()
    {
        $obj    = new Config(['timeout' => 100]);
        $params = $obj->getParameters();

        $this->assertCount(5, $params);
        $this->assertEquals($params['timeout'], 100);
    }

    public function testSet()
    {
        $obj = new Config();
        $obj->set('timeout', 111);
        $params = $obj->getParameters();

        $this->assertEquals($params['timeout'], 111);
    }

    public function testSetArr()
    {
        $obj    = new Config([
            'timeout' => 111
        ]);
        $params = $obj->getParameters();

        $this->assertEquals($params['timeout'], 111);
    }

    public function testDelete()
    {
        $obj = new Config();
        $obj->delete('timeout');
        $params = $obj->getParameters();

        $this->assertArrayNotHasKey('timeout', $params);
    }

    public function testDeleteEx()
    {
        $this->expectException(ConfigException::class);

        $obj = new Config();
        $obj->delete('wrong');
    }

    public function testSetEx1()
    {
        $this->expectException(ConfigException::class);

        $obj = new Config();
        $obj->set('delay', 'some string');
    }

    public function testSetEx2()
    {
        $this->expectException(ConfigException::class);

        $obj = new Config();
        $obj->set('wrong', 'some string');
    }

    public function testGet()
    {
        $obj   = new Config();
        $test1 = $obj->get('legacy');
        $this->assertEquals($test1, false);

        $test2 = $obj->get('port');
        $this->assertEquals($test2, 8728);

        $obj->set('port', 10000);
        $test3 = $obj->get('port');
        $this->assertEquals($test3, 10000);


        $obj->delete('port');
        $obj->set('ssl', true);
        $test3 = $obj->get('port');
        $this->assertEquals($test3, 8729);
    }

    public function testGetEx()
    {
        $this->expectException(ConfigException::class);

        $obj = new Config();
        $obj->get('wrong');
    }
}


File: /vendor\evilfreelancer\routeros-api-php\tests\Helpers\ArrayHelperTest.php
<?php

namespace RouterOS\Tests\Helpers;

use PHPUnit\Framework\TestCase;
use RouterOS\Helpers\ArrayHelper;

class ArrayHelperTest extends TestCase
{
    public function testCheckIfKeyNotExist()
    {
        $test1 = ArrayHelper::checkIfKeyNotExist(1, [0 => 'a', 1 => 'b', 2 => 'c']);
        $this->assertFalse($test1);

        $test2 = ArrayHelper::checkIfKeyNotExist('a', [1 => 'a', 2 => 'b', 3 => 'c']);
        $this->assertTrue($test2);
    }

    public function testCheckIfKeysNotExist()
    {
        $test1 = ArrayHelper::checkIfKeysNotExist([1, 2], [0 => 'a', 1 => 'b', 2 => 'c']);
        $this->assertTrue($test1);

        $test2 = ArrayHelper::checkIfKeysNotExist([3, 4], [0 => 'a', 1 => 'b', 2 => 'c']);
        $this->assertNotTrue($test2);
    }
}


File: /vendor\evilfreelancer\routeros-api-php\tests\Helpers\BinaryStringHelperTest.php
<?php

namespace RouterOS\Tests\Helpers;

use PHPUnit\Framework\TestCase;

use RouterOS\Helpers\BinaryStringHelper;

/**
 * Limit code coverage to the class
 *
 * @coversDefaultClass \RouterOS\Helpers\BinaryStringHelper
 */
class BinaryStringHelperTest extends TestCase
{
    /**
     * @dataProvider IntegerToNBOBinaryStringProvider
     * @covers ::IntegerToNBOBinaryString
     */
    public function test__IntegerToNBOBinaryString($value, $expected)
    {
        $this->assertEquals($expected, BinaryStringHelper::IntegerToNBOBinaryString($value));
    }

    public function IntegerToNBOBinaryStringProvider(): array
    {
        $result = [
            [0, chr(0)], // lower boundary value
            [0xFFFFFFFF, chr(0xFF) . chr(0xFF) . chr(0xFF) . chr(0xFF)], // 32 bits maximal value

            // strange behaviour :
            //   TypeError: Argument 1 passed to RouterOS\Tests\Helpers\BinaryStringHelperTest::test__IntegerToNBOBinaryString() must be of the type integer, float given
            //   Seems that php auto convert to float 0xFFF.... 
            // 
            // [0xFFFFFFFFFFFFFFFF, chr(0xFF).chr(0xFF).chr(0xFF).chr(0xFF).chr(0xFF).chr(0xFF).chr(0xFF).chr(0xFF)],

            // Let's try random value
            [0x390DDD99, chr(0x39) . chr(0x0D) . chr(0xDD) . chr(0x99)],
        ];

        if (PHP_INT_SIZE > 4) {
            // -1 is encoded with 0xFFFFFFF.....
            // 64 bits maximal value (on a 64 bits system only)
            $result[] = [-1, chr(0xFF) . chr(0xFF) . chr(0xFF) . chr(0xFF) . chr(0xFF) . chr(0xFF) . chr(0xFF) . chr(0xFF)]; // 64 bits upper boundary value
        }

        return $result;
    }
}


File: /vendor\evilfreelancer\routeros-api-php\tests\Helpers\TypeHelperTest.php
<?php

namespace RouterOS\Tests\Helpers;

use PHPUnit\Framework\TestCase;
use RouterOS\Helpers\TypeHelper;

class TypeHelperTest extends TestCase
{
    public function testCheckIfTypeMismatch()
    {
        $test1 = TypeHelper::checkIfTypeMismatch(gettype(true), gettype(false));
        $this->assertFalse($test1);

        $test2 = TypeHelper::checkIfTypeMismatch(gettype(true), gettype('false'));
        $this->assertTrue($test2);
    }
}


File: /vendor\evilfreelancer\routeros-api-php\tests\QueryTest.php
<?php

namespace RouterOS\Tests;

use PHPUnit\Framework\TestCase;
use RouterOS\Exceptions\QueryException;
use RouterOS\Query;

class QueryTest extends TestCase
{
    public function test__construct(): void
    {
        try {
            $obj = new Query('test');
            $this->assertIsObject($obj);
        } catch (\Exception $e) {
            $this->assertContains('Must be initialized ', $e->getMessage());
        }
    }

    public function test__construct_arr(): void
    {
        try {
            $obj = new Query('test', ['line1', 'line2', 'line3']);
            $this->assertIsObject($obj);
        } catch (\Exception $e) {
            $this->assertContains('Must be initialized ', $e->getMessage());
        }
    }

    public function test__construct_arr2(): void
    {
        try {
            $obj = new Query(['test', 'line1', 'line2', 'line3']);
            $this->assertIsObject($obj);
        } catch (\Exception $e) {
            $this->assertContains('Must be initialized ', $e->getMessage());
        }
    }

    public function testGetEndpoint(): void
    {
        $obj  = new Query('test');
        $test = $obj->getEndpoint();
        $this->assertEquals($test, 'test');
    }

    public function testGetEndpoint2(): void
    {
        $obj  = new Query(['zzz', 'line1', 'line2', 'line3']);
        $test = $obj->getEndpoint();
        $this->assertEquals($test, 'zzz');
    }

    public function testGetEndpointEx(): void
    {
        $this->expectException(QueryException::class);

        $obj  = new Query(null);
        $test = $obj->getEndpoint();
    }

    public function testSetEndpoint(): void
    {
        $obj = new Query('test');
        $obj->setEndpoint('zzz');
        $test = $obj->getEndpoint();
        $this->assertEquals($test, 'zzz');
    }

    public function testGetAttributes(): void
    {
        $obj  = new Query('test');
        $test = $obj->getAttributes();
        $this->assertCount(0, $test);
    }

    public function testSetAttributes(): void
    {
        $obj = new Query('test');
        $obj->setAttributes(['line1', 'line2', 'line3']);
        $test = $obj->getAttributes();
        $this->assertCount(3, $test);
    }

    public function testAdd(): void
    {
        $obj = new Query('test');
        $obj->add('line');

        $attrs = $obj->getAttributes();
        $this->assertCount(1, $attrs);
        $this->assertEquals($attrs[0], 'line');
    }

    public function testWhere(): void
    {
        $obj = new Query('test');
        $obj->where('key1', 'value1');
        $obj->where('key2', 'value2');

        $attrs = $obj->getAttributes();
        $this->assertCount(2, $attrs);
        $this->assertEquals($attrs[1], '?key2=value2');
    }

    public function testTag(): void
    {
        $obj = new Query('/test/test');
        $obj->where('key1', 'value1');
        $obj->tag('test');

        $query = $obj->getQuery();
        $this->assertCount(3, $query);
        $this->assertEquals($query[2], '.tag=test');
    }

    public function testOperator(): void
    {
        $obj = new Query('/test/test');
        $obj->where('key1', 'value1');
        $obj->operations('|');

        $query = $obj->getQuery();
        $this->assertCount(3, $query);
        $this->assertEquals($query[2], '?#|');
    }

    public function testWhereEx(): void
    {
        $this->expectException(QueryException::class);

        $obj = new Query('/richard/cheese');
        $obj->where('people', 'equals', 'shit');
    }

    public function testGetQuery(): void
    {
        $obj = new Query('test');
        $obj->add('line');

        $query = $obj->getQuery();
        $this->assertCount(2, $query);
        $this->assertEquals($query[0], 'test');
        $this->assertEquals($query[1], 'line');
    }

    public function testGetQueryEx(): void
    {
        $this->expectException(QueryException::class);

        $obj = new Query([null]);
        $obj->getQuery();
    }
}


File: /vendor\evilfreelancer\routeros-api-php\tests\ResponseIteratorTest.php
<?php

namespace RouterOS\Tests;

use PHPUnit\Framework\TestCase;
use RouterOS\Client;

class ResponseIteratorTest extends TestCase
{
    public function test__construct()
    {
        $obj = new Client([
            'user' => getenv('ROS_USER'),
            'pass' => getenv('ROS_PASS'),
            'host' => getenv('ROS_HOST'),
        ]);

        $obj = $obj->write('/system/package/print')->readAsIterator();
        $this->assertIsObject($obj);
    }

    public function testReadWrite()
    {
        $obj = new Client([
            'user' => getenv('ROS_USER'),
            'pass' => getenv('ROS_PASS'),
            'host' => getenv('ROS_HOST'),
        ]);

        $readTrap = $obj->write('/system/package/print')->readAsIterator();
        // Read from RAW
        $this->assertCount(13, $readTrap);

        $readTrap = $obj->write('/ip/address/print')->readAsIterator();
        $this->assertCount(1, $readTrap);
        $this->assertEquals('ether1', $readTrap[0]['interface']);

        $readTrap = $obj->write('/system/package/print')->readAsIterator();
        $key      = $readTrap->key();
        $this->assertEquals(0, $key);
        $current = $readTrap->current();
        $this->assertEquals('*1', $current['.id']);

        $readTrap->next();
        $key = $readTrap->key();
        $this->assertEquals(1, $key);
        $current = $readTrap->current();
        $this->assertEquals('*2', $current['.id']);

        $readTrap->prev();
        $key = $readTrap->key();
        $this->assertEquals(0, $key);
        $current = $readTrap->current();
        $this->assertEquals('*1', $current['.id']);

        $readTrap->prev(); // Check if key is not exist
        $key = $readTrap->key();
        $this->assertEquals(-1, $key);
        $current = $readTrap->current();
        $this->assertNull($current);
    }

    public function testSerialize(): void
    {
        $obj = new Client([
            'user' => getenv('ROS_USER'),
            'pass' => getenv('ROS_PASS'),
            'host' => getenv('ROS_HOST'),
        ]);

        $read = $obj->write('/queue/simple/print')->readAsIterator();
        $serialize = $read->serialize();
        $this->assertEquals('a:1:{i:0;a:1:{i:0;s:5:"!done";}}', $serialize);
    }

}


File: /vendor\evilfreelancer\routeros-api-php\tests\Streams\ResourceStreamTest.php
<?php

namespace RouterOS\Tests\Streams;

use PHPUnit\Framework\TestCase;
use PHPUnit\Framework\Constraint\IsType;
use RouterOS\Streams\ResourceStream;

/**
 * Limit code coverage to the class RouterOS\APIStream
 *
 * @coversDefaultClass \RouterOS\Streams\ResourceStream
 */
class ResourceStreamTest extends TestCase
{
    /**
     * Test that constructor throws an InvalidArgumentException on bad parameter type
     *
     * @covers ::__construct
     * @expectedException \InvalidArgumentException
     * @dataProvider constructNotResourceProvider
     *
     * @param $notResource
     */

    public function test__constructNotResource($notResource)
    {
        new ResourceStream($notResource);
    }

    /**
     * Data provider for test__constructNotResource
     *
     * returns data not of type resource
     */
    public function constructNotResourceProvider(): array
    {
        return [
            [0],          // integer
            [3.14],       // float
            ['a string'], // string
            [
                [0, 3.14]   // Array
            ],
            [new \stdClass()], // Object
            // What else ?
        ];
    }

    /**
     * Test that constructor is OK with different kinds of resources
     *
     * @covers ::__construct
     * @dataProvider constructProvider
     *
     * @param resource $resource      Cannot typehint, PHP refuse it
     * @param bool     $closeResource shall we close the resource ?
     */
    public function test_construct($resource, bool $closeResource = true)
    {
        $resourceStream = new ResourceStream($resource);

        $stream = $this->getObjectAttribute($resourceStream, 'stream');
        $this->assertInternalType(IsType::TYPE_RESOURCE, $stream);

        if ($closeResource) {
            fclose($resource);
        }
    }

    /**
     * Data provider for test__construct
     *
     * @return array data of type resource
     */
    public function constructProvider(): array
    {
        return [
            [fopen(__FILE__, 'rb'),], // Myself, sure I exists
            [fsockopen('tcp://' . getenv('ROS_HOST'), getenv('ROS_PORT_MODERN')),], // Socket
            [STDIN, false], // Try it, but do not close STDIN please !!!
            // What else ?
        ];
    }

    /**
     * Test that read function return expected values, and that consecutive reads return data
     *
     * @covers ::read
     * @dataProvider readProvider
     *
     * @param   ResourceStream $stream   Cannot typehint, PHP refuse it
     * @param   string         $expected the result we should have
     * @throws  \RouterOS\Exceptions\StreamException
     * @throws  \InvalidArgumentException
     */
    public function test__read(ResourceStream $stream, string $expected)
    {
        $this->assertSame($expected, $stream->read(strlen($expected)));
    }

    public function readProvider(): array
    {
        $resource = fopen(__FILE__, 'rb');
        $me       = new ResourceStream($resource);

        return [
            [$me, '<'],  // Read for byte
            [$me, '?php'], // Read following bytes. File statrts with "<php"
        ];
    }

    /**
     * Test that read invalid lengths
     *
     * @covers ::read
     * @dataProvider readBadLengthProvider
     * @expectedException \InvalidArgumentException
     *
     * @param   ResourceStream $stream Cannot typehint, PHP refuse it
     * @param   int            $length
     * @throws  \RouterOS\Exceptions\StreamException
     * @throws  \InvalidArgumentException
     */
    public function test__readBadLength(ResourceStream $stream, int $length)
    {
        $stream->read($length);
    }

    public function readBadLengthProvider(): array
    {
        $resource = fopen(__FILE__, 'rb');
        $me       = new ResourceStream($resource);

        return [
            [$me, 0],
            [$me, -1],
        ];
    }

    /**
     * Test read to invalid resource
     *
     * @covers ::read
     * @dataProvider readBadResourceProvider
     * @expectedException \RouterOS\Exceptions\StreamException
     *
     * @param   ResourceStream $stream Cannot typehint, PHP refuse it
     * @param   int            $length
     */
    public function test__readBadResource(ResourceStream $stream, int $length)
    {
        $stream->read($length);
    }

    public function readBadResourceProvider(): array
    {
        $resource = fopen(__FILE__, 'rb');
        $me       = new ResourceStream($resource);
        fclose($resource);
        return [
            [$me, 1],
        ];
    }

    /**
     * Test that write function returns writen length
     *
     * @covers ::write
     * @dataProvider writeProvider
     *
     * @param   ResourceStream $stream  to test
     * @param   string         $toWrite the writed string
     * @throws  \RouterOS\Exceptions\StreamException
     */
    public function test__write(ResourceStream $stream, string $toWrite)
    {
        $this->assertEquals(strlen($toWrite), $stream->write($toWrite));
    }

    public function writeProvider(): array
    {
        $resource = fopen('/dev/null', 'wb');
        $null     = new ResourceStream($resource);

        return [
            [$null, 'yyaagagagag'],  // Take that
        ];
    }

    /**
     * Test write to invalid resource
     *
     * @covers ::write
     * @dataProvider writeBadResourceProvider
     * @expectedException \RouterOS\Exceptions\StreamException
     *
     * @param ResourceStream $stream  to test
     * @param string         $toWrite the written string
     */
    public function test__writeBadResource(ResourceStream $stream, string $toWrite)
    {
        $stream->write($toWrite);
    }

    public function writeBadResourceProvider(): array
    {
        $resource = fopen('/dev/null', 'wb');
        $me       = new ResourceStream($resource);
        fclose($resource);

        return [
            [$me, 'sasasaas'],  // Take that
        ];
    }

    /**
     * Test double close resource
     *
     * @covers ::close
     * @dataProvider doubleCloseProvider
     * @expectedException \RouterOS\Exceptions\StreamException
     *
     * @param ResourceStream $stream to test
     */
    public function test_doubleClose(ResourceStream $stream)
    {
        $stream->close();
        $stream->close();
    }

    public function doubleCloseProvider(): array
    {
        return [
            [new ResourceStream(fopen('/dev/null', 'wb')), 'sasasaas'],  // Take that
        ];
    }

    /**
     * Test write to closed resource
     *
     * @covers ::close
     * @covers ::write
     * @dataProvider writeClosedResourceProvider
     * @expectedException \RouterOS\Exceptions\StreamException
     *
     * @param ResourceStream $stream  to test
     * @param string         $toWrite the written string
     */
    public function test_close(ResourceStream $stream, string $toWrite)
    {
        $stream->close();
        $stream->write($toWrite);
    }

    public function writeClosedResourceProvider(): array
    {
        return [
            [new ResourceStream(fopen('/dev/null', 'wb')), 'sasasaas'],  // Take that
        ];
    }

}


File: /vendor\evilfreelancer\routeros-api-php\tests\Streams\StringStreamTest.php
<?php

namespace RouterOS\Tests\Streams;

use PHPUnit\Framework\TestCase;
use PHPUnit\Framework\Constraint\IsType;

use RouterOS\Streams\StringStream;
use RouterOS\Exceptions\StreamException;

/**
 * Limit code coverage to the class RouterOS\APIStream
 *
 * @coversDefaultClass \RouterOS\Streams\StringStream
 */
class StringStreamTest extends TestCase
{
    /**
     * @covers ::__construct
     * @dataProvider constructProvider
     *
     * @param   string $string
     */
    public function test__construct(string $string)
    {
        $this->assertInstanceOf(StringStream::class, new StringStream($string));
    }

    public function constructProvider(): array
    {
        return [
            [chr(0)],
            [''],
            ['1'],
            ['lkjl' . chr(0) . 'kjkljllkjkljljklkjkljlkjljlkjkljkljlkjjll'],
        ];
    }


    /**
     * Test that write function returns the effective written bytes
     *
     * @covers ::write
     * @dataProvider writeProvider
     *
     * @param   string   $string   the string to write
     * @param   int|null $length   the count if bytes to write
     * @param   int      $expected the number of bytes that must be writen
     */

    public function test__write(string $string, $length, int $expected)
    {
        $stream = new StringStream('Does not matters');
        if (null === $length) {
            $this->assertEquals($expected, $stream->write($string));
        } else {
            $this->assertEquals($expected, $stream->write($string, $length));
        }

    }

    public function writeProvider(): array
    {
        return [
            ['', 0, 0],
            ['', 10, 0],
            ['', null, 0],
            ['Yabala', 0, 0],
            ['Yabala', 1, 1],
            ['Yabala', 6, 6],
            ['Yabala', 100, 6],
            ['Yabala', null, 6],
            [chr(0), 0, 0],
            [chr(0), 1, 1],
            [chr(0), 100, 1],
            [chr(0), null, 1],
        ];
    }

    /**
     * @covers ::write
     * @expectedException \InvalidArgumentException
     */
    public function test__writeWithNegativeLength()
    {
        $stream = new StringStream('Does not matters');
        $stream->write('PLOP', -1);
    }

    /**
     * Test read function
     *
     * @throws \RouterOS\Exceptions\StreamException
     */
    public function test__read()
    {
        $stream = new StringStream('123456789');

        $this->assertEquals('', $stream->read(0));
        $this->assertEquals('1', $stream->read(1));
        $this->assertEquals('23', $stream->read(2));
        $this->assertEquals('456', $stream->read(3));
        $this->assertEquals('', $stream->read(0));
        $this->assertEquals('789', $stream->read(4));
    }

    /**
     * @expectedException \InvalidArgumentException
     *
     * @throws \RouterOS\Exceptions\StreamException
     */
    public function test__readBadLength()
    {
        $stream = new StringStream('123456789');
        $stream->read(-1);
    }

    /**
     * @covers ::read
     * @dataProvider readWhileEmptyProvider
     * @expectedException \RouterOS\Exceptions\StreamException
     *
     * @param   StringStream $stream
     * @param   int          $length
     * @throws  \RouterOS\Exceptions\StreamException
     */
    public function test__readWhileEmpty(StringStream $stream, int $length)
    {
        $stream->read($length);
    }

    /**
     * @return \Generator
     * @throws StreamException
     */
    public function readWhileEmptyProvider()
    {
        $stream = new StringStream('123456789');
        $stream->read(9);
        yield [$stream, 1];

        $stream = new StringStream('123456789');
        $stream->read(5);
        $stream->read(4);
        yield [$stream, 1];

        $stream = new StringStream('');
        yield [$stream, 1];
    }

    /**
     * @expectedException \RouterOS\Exceptions\StreamException
     */
    public function testReadClosed()
    {
        $stream = new StringStream('123456789');
        $stream->close();
        $stream->read(1);
    }
}


