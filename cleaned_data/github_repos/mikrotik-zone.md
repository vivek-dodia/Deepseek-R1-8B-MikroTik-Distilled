# Repository Information
Name: mikrotik-zone

# Directory Structure
Directory structure:
└── github_repos/mikrotik-zone/
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
    │   │       │   └── Development
    │   │       └── remotes/
    │   │           └── origin/
    │   │               └── HEAD
    │   ├── objects/
    │   │   ├── info/
    │   │   └── pack/
    │   │       ├── pack-ec415bc06d4213282b086147f57eff9207e298e0.idx
    │   │       └── pack-ec415bc06d4213282b086147f57eff9207e298e0.pack
    │   ├── packed-refs
    │   └── refs/
    │       ├── heads/
    │       │   └── Development
    │       ├── remotes/
    │       │   └── origin/
    │       │       └── HEAD
    │       └── tags/
    ├── .gitattributes
    ├── ajax_adduser.php
    ├── ajax_addusers.php
    ├── ajax_add_profile.php
    ├── ajax_add_sysuser.php
    ├── ajax_change_syspass.php
    ├── ajax_del_profile.php
    ├── ajax_del_sysuser.php
    ├── ajax_edit_profile.php
    ├── ajax_edit_sysuser.php
    ├── ajax_expired.php
    ├── ajax_get_profiles.php
    ├── ajax_get_sysuser.php
    ├── ajax_rem_selected.php
    ├── ajax_rem_user.php
    ├── ajax_reset_pass.php
    ├── ajax_uninitiated.php
    ├── backup.php
    ├── config.php
    ├── css/
    │   ├── animate.css
    │   ├── awesome-bootstrap-checkbox.css
    │   ├── customModal.css
    │   ├── print.css
    │   └── style.css
    ├── database.php
    ├── dbconfig.php
    ├── db_backup_20_09_2016_14_11_47.sql
    ├── fonts/
    │   ├── fontawesome-webfont.eot
    │   ├── fontawesome-webfont.ttf
    │   ├── fontawesome-webfont.woff
    │   ├── FontAwesome.otf
    │   ├── glyphicons-halflings-regular.eot
    │   ├── glyphicons-halflings-regular.ttf
    │   └── glyphicons-halflings-regular.woff
    ├── header.php
    ├── home.php
    ├── hotsoft.php
    ├── images/
    ├── index.php
    ├── info.php
    ├── js/
    │   └── customModal.js
    ├── login.php
    ├── logme.php
    ├── logout.php
    ├── modal_change_pass.php
    ├── modal_delete_guest.php
    ├── modal_get_profiles.php
    ├── modal_get_user.php
    ├── PEAR2/
    │   ├── Autoload.php
    │   ├── Cache/
    │   │   ├── SHM/
    │   │   │   ├── Adapter/
    │   │   │   │   ├── APC.php
    │   │   │   │   ├── Placebo.php
    │   │   │   │   └── Wincache.php
    │   │   │   ├── Exception.php
    │   │   │   └── InvalidArgumentException.php
    │   │   └── SHM.php
    │   ├── Console/
    │   │   ├── Color/
    │   │   │   ├── Backgrounds.php
    │   │   │   ├── Exception.php
    │   │   │   ├── Flags.php
    │   │   │   ├── Fonts.php
    │   │   │   ├── Styles.php
    │   │   │   └── UnexpectedValueException.php
    │   │   ├── Color.php
    │   │   ├── CommandLine/
    │   │   │   ├── Action/
    │   │   │   │   ├── Callback.php
    │   │   │   │   ├── Counter.php
    │   │   │   │   ├── Help.php
    │   │   │   │   ├── List.php
    │   │   │   │   ├── Password.php
    │   │   │   │   ├── StoreArray.php
    │   │   │   │   ├── StoreFalse.php
    │   │   │   │   ├── StoreFloat.php
    │   │   │   │   ├── StoreInt.php
    │   │   │   │   ├── StoreString.php
    │   │   │   │   ├── StoreTrue.php
    │   │   │   │   └── Version.php
    │   │   │   ├── Action.php
    │   │   │   ├── Argument.php
    │   │   │   ├── Command.php
    │   │   │   ├── CustomMessageProvider.php
    │   │   │   ├── Element.php
    │   │   │   ├── Exception.php
    │   │   │   ├── MessageProvider/
    │   │   │   │   └── Default.php
    │   │   │   ├── MessageProvider.php
    │   │   │   ├── Option.php
    │   │   │   ├── Outputter/
    │   │   │   │   └── Default.php
    │   │   │   ├── Outputter.php
    │   │   │   ├── Renderer/
    │   │   │   │   └── Default.php
    │   │   │   ├── Renderer.php
    │   │   │   ├── Result.php
    │   │   │   └── XmlParser.php
    │   │   └── CommandLine.php
    │   └── Net/
    │       ├── RouterOS/
    │       │   ├── Client.php
    │       │   ├── Communicator.php
    │       │   ├── DataFlowException.php
    │       │   ├── Exception.php
    │       │   ├── InvalidArgumentException.php
    │       │   ├── LengthException.php
    │       │   ├── Message.php
    │       │   ├── NotSupportedException.php
    │       │   ├── Query.php
    │       │   ├── Registry.php
    │       │   ├── Request.php
    │       │   ├── Response.php
    │       │   ├── ResponseCollection.php
    │       │   ├── SocketException.php
    │       │   ├── UnexpectedValueException.php
    │       │   └── Util.php
    │       └── Transmitter/
    │           ├── Exception.php
    │           ├── FilterCollection.php
    │           ├── LockException.php
    │           ├── NetworkStream.php
    │           ├── SocketException.php
    │           ├── Stream.php
    │           ├── StreamException.php
    │           ├── TcpClient.php
    │           └── TcpServerConnection.php
    ├── readme.txt
    ├── settings.php
    └── voucher.php


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
	url = https://github.com/lupael/mikrotik-zone.git
	fetch = +refs/heads/*:refs/remotes/origin/*
[branch "Development"]
	remote = origin
	merge = refs/heads/Development


File: /.git\description
Unnamed repository; edit this file 'description' to name the repository.


File: /.git\HEAD
ref: refs/heads/Development


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
0000000000000000000000000000000000000000 e8509575a552df36ecb9f2908bccb2aaf691bd8d vivek-dodia <vivek.dodia@icloud.com> 1738606404 -0500	clone: from https://github.com/lupael/mikrotik-zone.git


File: /.git\logs\refs\heads\Development
0000000000000000000000000000000000000000 e8509575a552df36ecb9f2908bccb2aaf691bd8d vivek-dodia <vivek.dodia@icloud.com> 1738606404 -0500	clone: from https://github.com/lupael/mikrotik-zone.git


File: /.git\logs\refs\remotes\origin\HEAD
0000000000000000000000000000000000000000 e8509575a552df36ecb9f2908bccb2aaf691bd8d vivek-dodia <vivek.dodia@icloud.com> 1738606404 -0500	clone: from https://github.com/lupael/mikrotik-zone.git


File: /.git\packed-refs
# pack-refs with: peeled fully-peeled sorted 
e8509575a552df36ecb9f2908bccb2aaf691bd8d refs/remotes/origin/Development


File: /.git\refs\heads\Development
e8509575a552df36ecb9f2908bccb2aaf691bd8d


File: /.git\refs\remotes\origin\HEAD
ref: refs/remotes/origin/Development


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


File: /ajax_adduser.php
<?php
//require_once 'settings.php';

use PEAR2\Net\RouterOS;
require_once 'PEAR2/Autoload.php';
require_once 'config.php';
$util = new RouterOS\Util($client = new RouterOS\Client("$host", "$user", "$pass"));

if (isset($_GET['name'])) $username = $_GET['name'];
if (isset($_GET['psd'])) $password = $_GET['psd'];
if (isset($_GET['limit_uptime'])) $limit_uptime = $_GET['limit_uptime'];
if (isset($_GET['limit_bytes'])) $limit_bytes = $_GET['limit_bytes'];
if (isset($_GET['profile'])) $profile = $_GET['profile'];
if ( !isset($_SESSION) ) session_start();

$util->setMenu('/ip hotspot user');
$iv = count($util);

if ((!empty($username)) and (!empty($password)) and (!empty($profile))) {
	if (intval($limit_bytes) != 0) {
		$limit_bytes_total = (intval($limit_bytes) * 1024 * 1024 * 1024 );
		$util->add(
			array(
				'name' => "$username",
				'password' => "$password",
				'disabled' => "no",
				'limit-uptime' => "$limit_uptime",
				'limit-bytes-total' => "$limit_bytes_total",
				'profile' => "$profile",
				'comment' => "Zetozone",
			)
		);
	}
	else
		{
			$util->add(
			array(
				'name' => "$username",
				'password' => "$password",
				'disabled' => "no",
				'limit-uptime' => "$limit_uptime",
				'profile' => "$profile",
				'comment' => "Zetozone",
			)
		);
		$limit_bytes = 0; // For Adding it to Local database
	}		

	if ($iv != count($util)) {
		include('dbconfig.php');
		$stmt = $DB_con->prepare("SELECT booking_id from hotspot_vouchers ORDER BY booking_id DESC LIMIT 1");
		$stmt->execute(array());
		$row = $stmt->fetch(PDO::FETCH_ASSOC);
		$booking_id = $row['booking_id'];
		$booking_id++;
		$uid = $booking_id.'-1-'.date('dmY');
		//$creator = $_SESSION['username'].'['.$_SESSION['id'].']';
		$stmt = $DB_con->prepare("UPDATE hotspot_vouchers set status=:status WHERE 1");
		$stmt->execute(array(':status' => 'Over'));
			$stmt = $DB_con->prepare("insert into hotspot_vouchers (created_on, created_by, creator, user_name, password, printed_times,
			printed_last, status, group_of, booking_id, limit_uptime, limit_bytes, profile, uid)
			values(NOW(), :created_by, :creator, :user_name, :password, :printed_times, :printed_last, :status, :group_of, 
			:booking_id, :limit_uptime, :limit_bytes, :profile, :uid)");
		$stmt->execute(array(':created_by' => $_SESSION['username'], ':creator' => $_SESSION['id'], ':user_name' => $username, ':password' => $password,
			':printed_times' => 0, ':printed_last' => '', ':status' => 'Active', ':group_of' => 1,
			':booking_id' => $booking_id, ':limit_uptime' => $limit_uptime, ':limit_bytes' => $limit_bytes,
			':profile' => $profile, ':uid' => $uid));	
			
		// here starts Echo String
		$echo_text ='			
			<div class="container">
				<div class="row" style="padding-top:20px;">	
					<div class="col-sm-12 col-md-12">
						<div class="panel panel-primary">
							<div class="panel-heading"><h3 class="text-center">Hotspot User Voucher</h3></div>
							<div class="panel-body">
								<form id="userForm" class="form-horizontal" method="GET" action="" enctype="multipart/form-data">
									<div class="col-sm-12 col-md-12">
										<table cellpadding="0" cellspacing="0" border="0" class="table table-bordered" id="example">
											<thead>
												<tr>
													<th width="10%"></th>
													<th colspan="2">Username</th>                                 
													<th colspan="2">Password</th>
												</tr>
											</thead>
											<tbody>';
											$echo_text .= '<tr>
													<td width="10%" style="margin:0px; border: 0px; padding: 2px;"><img src="images/logo.png" width="250" height="50"></td>
													<td colspan="2"><input type="text" name="username" class="form-control" value="Username : '.$username.'" placeholder="User Name" readonly></td>
													<td colspan="2"><input type="text" name="password" class="form-control" value="Password : '.$password.'" placeholder="Password"  readonly></td>
												</tr>
												<tr>';
												if (intval($limit_bytes) != 0) {
													$echo_text .= '<td colspan="5">Validity : '.$limit_uptime.'ays; Counts from First login;  Data usage Maximum : '.$limit_bytes_total.' Bytes; Bandwidth : '.$profile.'; HAPPY BROWSING...</td>';
													}
												else
													{
													$echo_text .= '<td colspan="5">Validity : '.$limit_uptime.'ays; Counts from First login; Bandwidth/Profile : '.$profile.'; HAPPY BROWSING...</td>';
													}
												$echo_text .= '
												</tr>
											</tbody>
										</table>
									</div>
								</form>
							</div>
						</div>
					</div>
					<div class="col-sm-3 col-sm-offset-5">
						<button onclick="window.print();" class="btn btn-primary" ><i class="icon-save icon-large"></i></a>&nbsp;PRINT</button>&nbsp;&nbsp;
						<button onclick="document.getElementById("single").style.display="none !important;" type="reset" class="btn btn-danger"><i class="icon-save icon-large"></i></a>&nbsp;Reset</button>&nbsp;&nbsp;
						<button data-dismiss="modal" class="btn btn-info" ><i class="icon-save icon-large"></i></a>&nbsp;BACK</button>&nbsp;&nbsp;
					</div>
				</div>
			</div>';
				echo $echo_text;
		}
	else
		{
		echo '<script>cmodalOkCancel("ERROR/DUPLICATE", " Username '.$username.' is not added, Found as Duplicate. Try some other name", "error");</script>';
	}	
}
//End Adding a Guest User
?>

File: /ajax_addusers.php
<?php  error_reporting(E_ALL);
ini_set('display_errors', 1);

//require_once 'settings.php';
use PEAR2\Net\RouterOS;
require_once 'PEAR2/Autoload.php';
require_once 'config.php';
$util = new RouterOS\Util($client = new RouterOS\Client("$host", "$user", "$pass"));

if (isset($_GET['no_of_users'])) $no_of_users = $_GET['no_of_users'];
if (isset($_GET['pass_length'])) $passLength = $_GET['pass_length'];
if (isset($_GET['user_prefix'])) $user_prefix = $_GET['user_prefix'];
if (isset($_GET['limit_uptime'])) $limit_uptime = $_GET['limit_uptime'];
if (isset($_GET['limit_bytes'])) $limit_bytes = $_GET['limit_bytes'];
if (isset($_GET['profile'])) $profile = $_GET['profile'];
if (isset($_GET['same_pass'])) $same_pass = $_GET['same_pass'];
if (isset($_GET['pass_type'])) $pass_type = $_GET['pass_type'];

if ( !isset($_SESSION) ) session_start();

switch ($pass_type) {
	case "s":
		$passAlphabet = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz";
		$user_prefix = strtolower($user_prefix);
		break;
	case "c":
		$passAlphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ";
		$user_prefix = strtoupper($user_prefix);
		break;
	case "n":
		$passAlphabet = "123456789123456789123456789123456789123456789123456789";
		break;
	case "sc":
		$passAlphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ";
		break;
	case "sn":
		$passAlphabet = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz123456789123456789123456789";
		$user_prefix = strtolower($user_prefix);
		break;
	case "cn":
		$passAlphabet = "123456789123456789123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ123456789123456789123456789";
		$user_prefix = strtoupper($user_prefix);
		break;
	case "scn":
		$passAlphabet = "abcdefghijklmnopqrstuvwxyz123456789123456789123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ123456789";
		break;
}

$passAlphabetLimit = strlen($passAlphabet)-1;
	
if($_SESSION['user_level'] >= 1 and $_SESSION['user_level'] <= 3) {
	include('dbconfig.php');
	$stmt = $DB_con->prepare("SELECT booking_id from hotspot_vouchers ORDER BY booking_id DESC LIMIT 1");
	$stmt->execute(array());
	$row = $stmt->fetch(PDO::FETCH_ASSOC);
	$booking_id = $row['booking_id'];
	$booking_id++;
	
	$stmt = $DB_con->prepare("UPDATE hotspot_vouchers set status=:status WHERE 1");
	$stmt->execute(array(':status' => 'Over'));

	$stmt = $DB_con->prepare("insert into hotspot_vouchers (created_on, created_by, creator, user_name, password, printed_times,
		printed_last, status, group_of, booking_id, limit_uptime, limit_bytes, profile, uid)
		values(NOW(), :created_by, :creator,  :user_name, :password, :printed_times, :printed_last, :status, :group_of, 
		:booking_id, :limit_uptime, :limit_bytes, :profile, :uid)");
		
	$k = 1;
	for($i=0; $i < $no_of_users; $i++){
		//$passAlphabet = 'abcdefghikmnpqrstuvxyz23456789';
		//$passAlphabetLimit = strlen($passAlphabet)-1;
		$pass = '';
		$uid = '';
		//Password generation
		for ($j = 0; $j < $passLength; ++$j) {
			$pass .= $passAlphabet[mt_rand(0, $passAlphabetLimit)];
		}
		$pass = str_shuffle($pass);
		//Username generation
		for ($j = 0; $j < $passLength; ++$j) {
			$uid .= $passAlphabet[mt_rand(0, $passAlphabetLimit)];
		}
		//Adding prefix to username
		$user_name = $user_prefix.$uid;
		
		//username & password same or different
		if ($same_pass == 2) {	$pass_word = $pass; } else { $pass_word = $user_name; }
		
		$util->setMenu('/ip hotspot user');
		$iv = count($util);
		
		if (intval($limit_bytes) != 0) {
			$limit_bytes_total = (intval($limit_bytes) * 1024 * 1024 * 1024 );
			$util->add(
				array(
					'name' => "$username",
					'password' => "$password",
					'disabled' => "no",
					'limit-uptime' => "$limit_uptime",
					'limit-bytes-total' => "$limit_bytes_total",
					'profile' => "$profile",
					'comment' => "Zetozone",
				)
			);
		}
		else
			{
			$util->add(
				array(
					'name' => "$username",
					'password' => "$password",
					'disabled' => "no",
					'limit-uptime' => "$limit_uptime",
					'profile' => "$profile",
					'comment' => "Zetozone",
				)
			);
			$limit_bytes = 0; // For Adding it to Local database
		}	

		if ($iv != count($util)) {
			$uid = $booking_id.'-'.$k.'-'.$no_of_users.date('dmY');
			//$creator = $_SESSION['username'].'['.$_SESSION['id'].']';
			$stmt->execute(array(':created_by' => $_SESSION['username'], ':creator' => $_SESSION['id'], ':user_name' => $user_name, ':password' => $pass_word,
				':printed_times' => 0, ':printed_last' => '', ':status' => 'Active', ':group_of' => $no_of_users,
				':booking_id' => $booking_id, ':limit_uptime' => $limit_uptime, ':limit_bytes' => $limit_bytes,
				':profile' => $profile, ':uid' => $uid));			
			$k++;	
		} 	
	}
	echo $k - 1; //Successful
}
else
	{
	echo 0; // Not an Authorised User
}
?>

File: /ajax_add_profile.php
<?php
header('Content-Type: application/json');
use PEAR2\Net\RouterOS;
require_once 'PEAR2/Autoload.php';
require_once 'config.php';
if ( !isset($_SESSION) ) session_start();
if ($_SESSION['user_level'] == 1) {
	$util = new RouterOS\Util($client = new RouterOS\Client("$host", "$user", "$pass"));

	$profile_name=strtolower($_GET['profile_name']);
	$session_timeout=$_GET['session_timeout'];
	$shared_users=$_GET['shared_users'];
	$mac_cookie_timeout=$_GET['mac_cookie_timeout'];
	$keepalive_timeout=$_GET['keepalive_timeout'];
	$rx_rate_limit=$_GET['rx_rate_limit'];
	$tx_rate_limit=$_GET['tx_rate_limit'];

	$validity = $_GET['validity'];
	$grace_period = $_GET['grace_period'];
	$on_expiry = $_GET['on_expiry'];
	$price = $_GET['price'];
	$lock_user = $_GET['lock_user'];

	$rate_limit = $rx_rate_limit.'/'.$tx_rate_limit;
	/*
	if (empty($session_timeout)) $session_timeout = '3d 00:00:00';
	if (empty($mac_cookie_timeout)) $mac_cookie_timeout = '3d 00:00:00';
	if (empty($keepalive_timeout)) $keepalive_timeout = '00:02:00'; 
	*/
	if ($price == "") {$price = "0";}
	if($lock_user == Enable){$mac_bind = ';[:local mac $"mac-address"; /ip hotspot user set mac-address=$mac [find where name=$user]]';} else {$mac_bind = "";}

	$login_script = "";

	switch ($on_expiry) {
		case "rem":
			$login_script = ':put (",rem,'.$price.','.$validity.','.$grace_period.',,'.$lock_user.',");{:local date [/system clock get date ];:local time [/system clock get time ];:local uptime ('.$validity.');[/system scheduler add disabled=no interval=$uptime name=$user on-event="[/ip hotspot active remove [find where user=$user]];[/ip hotspot user set limit-uptime=1s [find where name=$user]];[/sys sch re [find where name=$user]];[/sys script run [find where name=$user]];[/sys script re [find where name=$user]]" start-date=$date start-time=$time];[/system script add name=$user source=":local date [/system clock get date ];:local time [/system clock get time ];:local uptime ('.$grace_period.');[/system scheduler add disabled=no interval=\$uptime name=$user on-event= \"[/ip hotspot user remove [find where name=$user]];[/ip hotspot active remove [find where user=$user]];[/sys sch re [find where name=$user]]\"]"]';
			break;
		case "ntf":
			$login_script = ':put (",ntf,'.$price.','.$validity.',,,'.$lock_user.',"); {:local date [/system clock get date ];:local time [/system clock get time ];:local uptime ('.$validity.');[/system scheduler add disabled=no interval=$uptime name=$user on-event= "[/ip hotspot user set limit-uptime=1s [find where name=$user]];[/ip hotspot active remove [find where user=$user]];[/sys sch re [find where name=$user]]" start-date=$date start-time=$time]';
			break;
		case "remc":
			$login_script = ':put (",remc,'.$price.','.$validity.','.$grace_period.',,'.$lock_user.',"); {:local price ('.$price.');:local date [/system clock get date ];:local time [/system clock get time ];:local uptime ('.$validity.');[/system scheduler add disabled=no interval=$uptime name=$user on-event="[/ip hotspot active remove [find where user=$user]];[/ip hotspot user set limit-uptime=1s [find where name=$user]];[/sys sch re [find where name=$user]];[/sys script run [find where name=$user]];[/sys script re [find where name=$user]]" start-date=$date start-time=$time];[/system script add name=$user source=":local date [/system clock get date ];:local time [/system clock get time ];:local uptime ('.$grace_period.');[/system scheduler add disabled=no interval=\$uptime name=$user on-event= \"[/ip hotspot user remove [find where name=$user]];[/ip hotspot active remove [find where user=$user]];[/sys sch re [find where name=$user]]\"]"];:local bln [:pick $date 0 3]; :local thn [:pick $date 7 11];[:local mac $"mac-address"; /system script add name="$date-|-$time-|-$user-|-$price-|-$address-|-$mac-|-'.$validity.'" owner="$bln$thn" source=$date comment=Zetozone]';
			break;
		case "ntfc":
			$login_script = ':put (",ntfc,'.$price.','.$validity.',,,'.$lock_user.',"); {:local price ('.$price.');:local date [/system clock get date ];:local time [/system clock get time ];:local uptime ('.$validity.');[/system scheduler add disabled=no interval=$uptime name=$user on-event= "[/ip hotspot user set limit-uptime=1s [find where name=$user]];[/ip hotspot active remove [find where user=$user]];[/sys sch re [find where name=$user]]" start-date=$date start-time=$time];:local bln [:pick $date 0 3]; :local thn [:pick $date 7 11];[:local mac $"mac-address"; /system script add name="$date-|-$time-|-$user-|-$price-|-$address-|-$mac-|-'.$validity.'" owner="$bln$thn" source=$date comment=Zetozone]';
			break;
		case "0":
			if ($price != "" ){
				$login_script = ':put (",,'.$price.',,,noexp,'.$lock_user.',")';
			}	
			break;
	}
	$login_script .= $mac_bind;

	if (!empty($profile_name)) {
		
			$util->setMenu('/ip hotspot user profile');
			if(strtolower($session_timeout) == 'none') $session_timeout = '00:00:00';
			$util->add(
				array(
					'name' => "$profile_name",
					'rate-limit' => "$rate_limit",
					'shared-users' => "$shared_users",
					'status-autorefresh' => "1m",
					'transparent-proxy' => "yes",
					'on-login' => "$login_script",
				)
			);
			/* Old version
			array(
					'name' => "$profile_name",
					'rate-limit' => "$rate_limit",
					'session-timeout' => "$session_timeout",
					'shared-users' => "$shared_users",
					'mac-cookie-timeout' => "$mac_cookie_timeout",
					'keepalive-timeout' => "$keepalive_timeout",
					'status-autorefresh' => "1m",
					'transparent-proxy' => "yes",
					'on-login' => "$login_script",
				)
			*/	
			/*
			if(strtolower($session_timeout) == 'none') {
				$id = $client->sendSync(new Request('/ip/hotspot/user/profile/print .proplist=.id', null, Query::where('name', $profile_name)))->getArgument('.id');
				$util->setMenu('/ip hotspot user profile');
				$util->unsetValue($id, 'session-timeout');
			} */
			echo 2; //Success
		}
	else
		{
		echo 1; //Profile name/Session Timeout Empty
	}
}
else
	{
		echo 0; //Not Authorised
}
?>

File: /ajax_add_sysuser.php
<?php 
if ( !isset($_SESSION) ) session_start();
if (($_SESSION['user_level'] == 1) and (!empty($_GET['username']))) { 
	include('dbconfig.php');
	$password='password';
	$password=sha1($password);
	$username=strtolower($_GET['username']);
	$firstname=$_GET['firstname'];
	$lastname=$_GET['lastname'];
	$user_level=$_GET['user_level'];
	$status=$_GET['status'];
	
	
	$stmt = $DB_con->prepare("SELECT * FROM hotspot_users WHERE username =:username");
	$stmt->execute(array(':username' => $username));
	$count = $stmt->rowCount();
	
	if ($count != 0) {
		echo 1;
	}
 else
	{
		$stmt = $DB_con->prepare("insert into hotspot_users (username, password, firstname, lastname, date_added, user_level, status)
			values(:username, :password, :firstname, :lastname, CURDATE(), :user_level, :status)");
		$stmt->execute(array(':username' => $username, ':password' => $password, ':firstname' => $firstname,
			':lastname' => $lastname, ':user_level' => $user_level, ':status' => $status));
		echo 2;
	}
}
else {
	echo 0;
}	
// End Adding a new System User Details, Returned from modal_add_user.php
?>

File: /ajax_change_syspass.php
<?php 
if ( !isset($_SESSION) ) session_start();
include('dbconfig.php');

$np = $_GET['np'];
If ($_SESSION['user_level'] <= 3) {
	$np = sha1($np);
	$stmt = $DB_con->prepare("update hotspot_users set password = :np where user_id = :session_id");
	$stmt->execute(array(':np' => $np, ':session_id' => $_SESSION['id']));
	echo 1;
	}
else
	{
		echo 0;
}
?>

File: /ajax_del_profile.php
<?php
header('Content-Type: application/json');
use PEAR2\Net\RouterOS;
require_once 'PEAR2/Autoload.php';
require_once 'config.php';
if ( !isset($_SESSION) ) session_start();
$util = new RouterOS\Util($client = new RouterOS\Client("$host", "$user", "$pass"));

$profile_name=strtolower($_GET['profile_name']);

if ($_SESSION['user_level'] == 1) {
	
	if (!empty($profile_name)) {
		
		$printRequest = new RouterOS\Request('/ip hotspot user profile print');
		$printRequest->setArgument('.proplist', '.id,name');
		$printRequest->setQuery(RouterOS\Query::where('name', $profile_name)); 

		$idList = '';
		foreach ($client->sendSync($printRequest)->getAllOfType(RouterOS\Response::TYPE_DATA) as $item) {
			$idList .= ',' . $item->getProperty('.id');
		}
		$idList = substr($idList, 1);
		//$idList now contains a comma separated list of all IDs.

		$removeRequest = new RouterOS\Request('/ip hotspot user profile remove');
		$removeRequest->setArgument('numbers', $idList);
		$client->sendSync($removeRequest); 
		echo 2; //Success
		}
	else
		{
		echo 1; //Profile name Empty
	}
}
else
	{
		echo 0; //Not Authorised
}
?>

File: /ajax_del_sysuser.php
<?php 
if ( !isset($_SESSION) ) session_start();
if (($_SESSION['user_level'] == 1) and (!empty($_GET['user_id']))) { 
	include('dbconfig.php');
	$id=$_GET['user_id'];
	$myself = $_SESSION['id'];
	$stmt = $DB_con->prepare("delete from hotspot_users where user_id=:id and user_id != :myself");
	$stmt->execute(array(':id' => $id, ':myself' => $myself));
	echo 1;
	}
else
	{
		echo 0;
	}
// End Adding a new System User Details, Returned from modal_add_user.php
?>

File: /ajax_edit_profile.php
<?php
header('Content-Type: application/json');
use PEAR2\Net\RouterOS;
require_once 'PEAR2/Autoload.php';
require_once 'config.php';
if ( !isset($_SESSION) ) session_start();
if ($_SESSION['user_level'] == 1) {
	$util = new RouterOS\Util($client = new RouterOS\Client("$host", "$user", "$pass"));

	$profile_name=strtolower($_GET['profile_name']);
	$session_timeout=$_GET['session_timeout'];
	$shared_users=$_GET['shared_users'];
	$mac_cookie_timeout=$_GET['mac_cookie_timeout'];
	$keepalive_timeout=$_GET['keepalive_timeout'];
	$rx_rate_limit=$_GET['rx_rate_limit'];
	$tx_rate_limit=$_GET['tx_rate_limit'];

	$validity = $_GET['validity'];
	$grace_period = $_GET['grace_period'];
	$on_expiry = $_GET['on_expiry'];
	$price = $_GET['price'];
	$lock_user = $_GET['lock_user'];
	
	$rate_limit = $rx_rate_limit.'/'.$tx_rate_limit;
	if (empty($rx_rate_limit))  $rx_rate_limit = "256k";
	if (empty($tx_rate_limit))  $tx_rate_limit = "128k";
	if (empty($shared_users))  $shared_users = 1;
/*	
	if (empty($session_timeout))  $session_timeout = "1d 00:00:00";
	if (empty($mac_cookie_timeout))  $mac_cookie_timeout = "1d 00:00:00";
	if (empty($keepalive_timeout))  $keepalive_timeout = "00:02:00";
*/
	if ($price == "") {$price = "0";}
	if($lock_user == Enable){$mac_bind = ';[:local mac $"mac-address"; /ip hotspot user set mac-address=$mac [find where name=$user]]';} else {$mac_bind = "";}

	$login_script = "";

	switch ($on_expiry) {
		case "rem":
			$login_script = ':put (",rem,'.$price.','.$validity.','.$grace_period.',,'.$lock_user.',");{:local date [/system clock get date ];:local time [/system clock get time ];:local uptime ('.$validity.');[/system scheduler add disabled=no interval=$uptime name=$user on-event="[/ip hotspot active remove [find where user=$user]];[/ip hotspot user set limit-uptime=1s [find where name=$user]];[/sys sch re [find where name=$user]];[/sys script run [find where name=$user]];[/sys script re [find where name=$user]]" start-date=$date start-time=$time];[/system script add name=$user source=":local date [/system clock get date ];:local time [/system clock get time ];:local uptime ('.$grace_period.');[/system scheduler add disabled=no interval=\$uptime name=$user on-event= \"[/ip hotspot user remove [find where name=$user]];[/ip hotspot active remove [find where user=$user]];[/sys sch re [find where name=$user]]\"]"]';
			break;
		case "ntf":
			$login_script = ':put (",ntf,'.$price.','.$validity.',,,'.$lock_user.',"); {:local date [/system clock get date ];:local time [/system clock get time ];:local uptime ('.$validity.');[/system scheduler add disabled=no interval=$uptime name=$user on-event= "[/ip hotspot user set limit-uptime=1s [find where name=$user]];[/ip hotspot active remove [find where user=$user]];[/sys sch re [find where name=$user]]" start-date=$date start-time=$time]';
			break;
		case "remc":
			$login_script = ':put (",remc,'.$price.','.$validity.','.$grace_period.',,'.$lock_user.',"); {:local price ('.$price.');:local date [/system clock get date ];:local time [/system clock get time ];:local uptime ('.$validity.');[/system scheduler add disabled=no interval=$uptime name=$user on-event="[/ip hotspot active remove [find where user=$user]];[/ip hotspot user set limit-uptime=1s [find where name=$user]];[/sys sch re [find where name=$user]];[/sys script run [find where name=$user]];[/sys script re [find where name=$user]]" start-date=$date start-time=$time];[/system script add name=$user source=":local date [/system clock get date ];:local time [/system clock get time ];:local uptime ('.$grace_period.');[/system scheduler add disabled=no interval=\$uptime name=$user on-event= \"[/ip hotspot user remove [find where name=$user]];[/ip hotspot active remove [find where user=$user]];[/sys sch re [find where name=$user]]\"]"];:local bln [:pick $date 0 3]; :local thn [:pick $date 7 11];[:local mac $"mac-address"; /system script add name="$date-|-$time-|-$user-|-$price-|-$address-|-$mac-|-'.$validity.'" owner="$bln$thn" source=$date comment=Zetozone]';
			break;
		case "ntfc":
			$login_script = ':put (",ntfc,'.$price.','.$validity.',,,'.$lock_user.',"); {:local price ('.$price.');:local date [/system clock get date ];:local time [/system clock get time ];:local uptime ('.$validity.');[/system scheduler add disabled=no interval=$uptime name=$user on-event= "[/ip hotspot user set limit-uptime=1s [find where name=$user]];[/ip hotspot active remove [find where user=$user]];[/sys sch re [find where name=$user]]" start-date=$date start-time=$time];:local bln [:pick $date 0 3]; :local thn [:pick $date 7 11];[:local mac $"mac-address"; /system script add name="$date-|-$time-|-$user-|-$price-|-$address-|-$mac-|-'.$validity.'" owner="$bln$thn" source=$date comment=Zetozone]';
			break;
		case "0":
			if ($price != "" ){
				$login_script = ':put (",,'.$price.',,,noexp,'.$lock_user.',")';
			}	
			break;
	}
	$login_script .= $mac_bind;
	
	if (!empty($profile_name)) {
		
		$printRequest = new RouterOS\Request('/ip/hotspot/user/profile/print');
		$printRequest->setArgument('.proplist', '.id');
		$printRequest->setQuery(RouterOS\Query::where('name', $profile_name));
		$id = $client->sendSync($printRequest)->getProperty('.id');

		$setRequest = new RouterOS\Request('/ip/hotspot/user/profile/set');
		$setRequest->setArgument('numbers', $id);
		$setRequest->setArgument('rate-limit', $rate_limit);
/*
		if(strtolower($session_timeout) != 'none') { 
			$setRequest->setArgument('session-timeout', $session_timeout);
		}
		else
			{
			$setRequest->setArgument('session-timeout', '00:00:00');
		}
		$setRequest->setArgument('mac-cookie-timeout', $mac_cookie_timeout);
		$setRequest->setArgument('keepalive-timeout', $keepalive_timeout);
*/
		$setRequest->setArgument('shared-users', $shared_users);		
		$setRequest->setArgument('status-autorefresh', "1m");
		$setRequest->setArgument('transparent-proxy', "yes");
		$setRequest->setArgument('on-login', "$login_script");
		
		$client->sendSync($setRequest);
		/*
		if(strtolower($session_timeout) == 'none') {
			$id = $client->sendSync(new Request('/ip/hotspot/user/profile/print .proplist=.id', null, Query::where('name', $profile_name)))->getArgument('.id');
			$util->setMenu('/ip hotspot user profile');
			$util->unsetValue($id, 'session-timeout');
		} */
		echo 2; //Success
	}
	else
		{
		echo 1; //Profile name Improper
	}
}
else
	{
		echo 0; //Not Authorised
}
?>

File: /ajax_edit_sysuser.php
<?php 
if ( !isset($_SESSION) ) session_start();

if (($_SESSION['user_level'] == 1) and (!empty($_GET['user_id']))) { 
	include('dbconfig.php');

	$user_id=$_GET['user_id'];
	$username=strtolower($_GET['username']);
	$stmt = $DB_con->prepare("SELECT * FROM hotspot_users WHERE username = :username AND user_id != :user_id");
	$stmt->execute(array(':username' => $username, ':user_id' => $user_id));
	$count = $stmt->rowCount();

	if ($count != 0) {
		echo 1;
		}
	else
		{
		$firstname=$_GET['firstname'];
		$lastname=$_GET['lastname'];
		$user_level=$_GET['user_level'];
		$status=$_GET['status'];

		$stmt = $DB_con->prepare("update hotspot_users set username=:username, firstname = :firstname , lastname = :lastname,
			user_level = :user_level, status = :status where user_id= :user_id");
		$stmt->execute(array(':username' => $username, ':firstname' => $firstname, ':lastname' => $lastname,
			':user_level' => $user_level, ':user_id' => $user_id, ':status' => $status));
		echo 2;
	}
}
else
	{
	echo 0;
}	
// End Adding a new System User Details, Returned from modal_add_user.php
?>

File: /ajax_expired.php
<?php
//Start Removing All Validity Expired Guest User Accounts
use PEAR2\Net\RouterOS;
require_once 'PEAR2/Autoload.php';
require_once 'config.php';
$util = new RouterOS\Util($client = new RouterOS\Client("$host", "$user", "$pass"));
if ( !isset($_SESSION) ) session_start();
if ($_SESSION['user_level'] <= 3) {	
	
	$printRequest = new RouterOS\Request('/ip hotspot user print');
	$printRequest->setArgument('.proplist', '.id,limit-uptime,uptime,name');
	//$printRequest->setQuery(RouterOS\Query::where('name', 'admin', RouterOS\Query::OP_EQ) ->not()); 
	$printRequest->setQuery(RouterOS\Query::where('.id', '*0', RouterOS\Query::OP_EQ) ->not()); 

	$idList = '';
	foreach ($client->sendSync($printRequest)->getAllOfType(RouterOS\Response::TYPE_DATA) as $item) {
		if (!empty($item->getProperty('limit-uptime'))) {
			if (!($item->getProperty('uptime') < $item->getProperty('limit-uptime'))) {
				$idList .= ',' . $item->getProperty('.id');
			}
		}	
	}
	$idList = substr($idList, 1);
	//$idList now contains a comma separated list of all IDs.

	$removeRequest = new RouterOS\Request('/ip hotspot user remove');
	$removeRequest->setArgument('numbers', $idList);
	$client->sendSync($removeRequest); 
}
//End Removing All Validity Expired Guest User Accounts
?>


File: /ajax_get_profiles.php
<?php
header('Content-Type: application/json');
use PEAR2\Net\RouterOS;
require_once 'PEAR2/Autoload.php';
require_once 'config.php';

$util = new RouterOS\Util($client = new RouterOS\Client("$host", "$user", "$pass"));
if ( !isset($_SESSION) ) session_start();
if ($_SESSION['user_level'] == 1) {
	$util->setMenu('/ip hotspot user profile print');
	$profile_name=$_GET['profile_name'];
	
	$printRequest = new RouterOS\Request('/ip hotspot user profile print');
	$printRequest->setArgument('.proplist', '.id,name,address-pool,rate-limit,session-timeout,shared-users,mac-cookie-timeout,keepalive-timeout,on-login');
	$printRequest->setQuery(RouterOS\Query::where('name', $profile_name)); 

	foreach ($client->sendSync($printRequest)->getAllOfType(RouterOS\Response::TYPE_DATA) as $item) {

	$tname =  $item->getProperty("name");
	$taddress_pool =  $item->getProperty("address-pool");
	$tshared_users =  $item->getProperty("shared-users");
	$trate_limit =  $item->getProperty("rate-limit");
	$tsession_timeout =  $item->getProperty("session-timeout");
	$ton_login =  $item->getProperty("on-login");
	$tmac_cookie_timeout =  $item->getProperty("mac-cookie-timeout");
	$tkeepalive_timeout =  $item->getProperty("keepalive-timeout");
	
	$exploded = explode(",",$ton_login);
	
	$ton_expiry = $exploded[1];
	$tprice = $exploded[2];	
	$tvalidity = $exploded[3];
	$tgrace_period = $exploded[4];
	$tlock_user = $exploded[6];
	
	if($ton_expiry == "rem"){ $tton_expiry = "Remove"; }
		elseif ($ton_expiry == "ntf"){ $tton_expiry = "Notice"; }
		elseif ($ton_expiry == "remc") { $tton_expiry = "Remove & Record"; }
		elseif ($ton_expiry == "ntfc") { $tton_expiry = "Notice & Record"; }
		else $tton_expiry = "0";
		

	$arr = array('name' => $tname, 'address_pool' => $taddress_pool, 'rate_limit' => $trate_limit, 'session_timeout' => $tsession_timeout,
		'shared_users' => $tshared_users, 'mac_cookie_timeout' => $tmac_cookie_timeout,
		'keepalive_timeout' => $tkeepalive_timeout, 'on_expiry' => $ton_expiry, 'price' => $tprice, 'validity' => $tvalidity,
		'grace_period' => $tgrace_period, 'lock_user' => $tlock_user );

	echo json_encode($arr); 
	}
}	
?>

File: /ajax_get_sysuser.php
<?php
header('Content-Type: application/json');
if ( !isset($_SESSION) ) session_start();
if (($_SESSION['user_level'] == 1) and (!empty($_GET['user_id']))) { 
	include('dbconfig.php');
	$user_id=$_GET['user_id'];
	
	$stmt = $DB_con->prepare("SELECT * FROM hotspot_users WHERE user_id =:user_id");
	$stmt->execute(array(':user_id' => $user_id));

	$row=$stmt->fetch(PDO::FETCH_ASSOC);
	echo json_encode($row);
}
// End Getting Sysuser details
?>

File: /ajax_rem_selected.php
<?php
use PEAR2\Net\RouterOS;
require_once 'PEAR2/Autoload.php';
require_once 'config.php';
$util = new RouterOS\Util($client = new RouterOS\Client("$host", "$user", "$pass"));
if ( !isset($_SESSION) ) session_start();
$i = 0;

if ($_SESSION['user_level'] <= 3) {	

	$guest_list=$_GET['removal_list'];
	if (count($guest_list) != 0) {
		$printRequest = new RouterOS\Request('/ip/hotspot/user/print');
		$printRequest->setArgument('.proplist', '.id,name');
		$removeRequest = new RouterOS\Request('/ip/hotspot/user/remove');
		foreach ($guest_list as $guest) {
			$i++;
			//$printRequest->setArgument('.proplist', '.id,name');
			$printRequest->setQuery(RouterOS\Query::where('name', $guest));
			$id = $client->sendSync($printRequest)->getProperty('.id');

			//$removeRequest = new RouterOS\Request('/ip/hotspot/user/remove');
			$removeRequest->setArgument('numbers', $id);
			$client->sendSync($removeRequest);
		}
		echo $i;
	}
	else
	{
		echo -1;
	}
}	
else
	{
	echo 0; 
}
//$id = $client->sendSync(new Request('/ip/hotspot/user/profile/print .proplist=.id', null, Query::where('name', $profile_name)))->getArgument('.id');
?>

File: /ajax_rem_user.php
<?php
use PEAR2\Net\RouterOS;
require_once 'PEAR2/Autoload.php';
require_once 'config.php';
$util = new RouterOS\Util($client = new RouterOS\Client("$host", "$user", "$pass"));
if ( !isset($_SESSION) ) session_start();

$guest_name=trim($_GET['username']);

$printRequest = new RouterOS\Request('/ip/hotspot/user/print');
$printRequest->setArgument('.proplist', '.id,name');
$printRequest->setQuery(RouterOS\Query::where('name', $guest_name));
$id = $client->sendSync($printRequest)->getProperty('.id');

$removeRequest = new RouterOS\Request('/ip/hotspot/user/remove');
$removeRequest->setArgument('numbers', $id);
$client->sendSync($removeRequest);
?>

File: /ajax_reset_pass.php
<?php 
if ( !isset($_SESSION) ) session_start();
if ($_SESSION['user_level'] == 1) { 
	include('dbconfig.php');
	$user_id= $_GET['user_id'];
	$password='password';
	$password=sha1($password);
	$stmt = $DB_con->prepare("SELECT * FROM hotspot_users WHERE user_id = :user_id");
	$stmt->execute(array(':user_id' => $user_id));
	$count = $stmt->rowCount();
	if ($count == 0){
		echo 1;
		}
	else
		{
		$stmt = $DB_con->prepare("update hotspot_users set password=:password where user_id= :user_id");
		$stmt->execute(array(':password' => $password, ':user_id' => $user_id));
		echo 2;
	}	
}
else
	{
	echo 0;
}
//End Resetting a System User Password, called from modal_reset_psd.php Modal
?>

File: /ajax_uninitiated.php
<?php
//Start Removing All Un-initiated Guest User Accounts
use PEAR2\Net\RouterOS;
require_once 'PEAR2/Autoload.php';
require_once 'config.php';
$util = new RouterOS\Util($client = new RouterOS\Client("$host", "$user", "$pass"));
if ( !isset($_SESSION) ) session_start();
if ($_SESSION['user_level'] <= 2) {
	$printRequest = new RouterOS\Request('/ip hotspot user print');
	$printRequest->setArgument('.proplist', '.id,limit-uptime,uptime,name');
	//$printRequest->setQuery(RouterOS\Query::where('name', 'default-trial', RouterOS\Query::OP_EQ) ->not()); 
	$printRequest->setQuery(RouterOS\Query::where('.id', '*0', RouterOS\Query::OP_EQ) ->not()); 

	$idList = '';
	foreach ($client->sendSync($printRequest)->getAllOfType(RouterOS\Response::TYPE_DATA) as $item) {
		if ($item->getProperty('uptime') == 0) {
			$idList .= ',' . $item->getProperty('.id');
		}
	}
	$idList = substr($idList, 1);
	//$idList now contains a comma separated list of all IDs.

	$removeRequest = new RouterOS\Request('/ip hotspot user remove');
	$removeRequest->setArgument('numbers', $idList);
	$client->sendSync($removeRequest); 
}
//End Removing All Un-initiated Guest User Accounts
?>


File: /backup.php
<?php include('session.php'); ?>
<?php header( 'Content-Type: text/plain' ); ?>
<?php include('header.php'); ?>
<?php include('navbar.php'); ?>
<?php
$progress_val = 100; ?>
<div class="progress">
  <div class="progress-bar progress-bar-striped active" role="progressbar"
  aria-valuenow="<?php echo $progress_val; ?>" aria-valuemin="0" aria-valuemax="100" style="width:<?php echo $progress_val; ?>%">
    <?php echo $progress_val.'%'; ?>
  </div>
</div>
<?php
$folder = $_SESSION['backup_folder'];
if (!is_dir($folder)) { mkdir($folder, 0777, true); }
chmod($folder, 0777);
$date = date('d-m-Y-H-i-s', time()); 
$filename = $folder."db-backup-".$date; 
include('dbconfig.php'); 
define( 'DUMPFILE', $filename . '.sql' );
 
try {
    //$DB_con = new PDO( 'mysql:host=' . DBHOST . ';dbname=' . DBNAME, DBUSER, DBPASS );
    $f = fopen( DUMPFILE, 'wt' );
 
    $tables = $DB_con->query( 'SHOW TABLES' );
    foreach ( $tables as $table ) {
		//echo   $table[0] . ' ... ';
		flush();
        $sql = '-- TABLE: ' . $table[0] . PHP_EOL;
        $create = $DB_con->query( 'SHOW CREATE TABLE `' . $table[0] . '`' )->fetch();
        $sql .= $create['Create Table'] . ';' . PHP_EOL;
        fwrite( $f, $sql );
 
        $rows = $DB_con->query( 'SELECT * FROM `' . $table[0] . '`' );
        $rows->setFetchMode( PDO::FETCH_ASSOC );
        foreach ( $rows as $row ) {
            $row = array_map( array( $DB_con, 'quote' ), $row );
            $sql = 'INSERT INTO `' . $table[0] . '` (`' . implode( '`, `', array_keys( $row ) ) . '`) VALUES (' . implode( ', ', $row ) . ');' . PHP_EOL;
            fwrite( $f, $sql );
        }
 
        $sql = PHP_EOL;
        $result = fwrite( $f, $sql );
        if ( $result !== FALSE ) {
           echo '';
        } else {
         //   echo 'ERROR!!' . PHP_EOL;
        }
        flush();
    }
    fclose( $f );
} catch (Exception $e) {
    echo 'Damn it! ' . $e->getMessage() . PHP_EOL;
}
?>
<a id="dlink" href=<?php echo '"'.$filename.'.sql"'?> download>

<script>
	var btnDownload = function() {
		document.getElementById("dlink").click();
		window.location = "admin.php";
	}
	btns = [{text:"No",action:"admin.php",style:"cmodal-cancel"}, {text:"Yes",action:btnDownload,style:"cmodal-ok"}];
	cmodalOkCancel("Backup Complete", "Backing-up of Database Tables to the Selected Path Completed Successfully. Do you want to download the backup ?", "information", btns);
</script>

File: /config.php
<?php 
$host = "192.168.1.123";
$user = "admin";
$pass = "admin";
?>

File: /css\animate.css
.animated.delay-01 {
	animation-delay: 0s;
	-webkit-animation-delay: 0s;
	-moz-animation-delay: 0s;
	-o-animation-delay: 0s;
}

.animated.delay-02 {
	animation-delay: 0.5s;
	-webkit-animation-delay: 0.5s;
	-moz-animation-delay: 0.5s;
	-o-animation-delay: 0.5s;
}

.animated.delay-03 {
	animation-delay: 1s;
	-webkit-animation-delay: 1s;
	-moz-animation-delay: 1s;
	-o-animation-delay: 1s;
}

.animated.delay-04 {
	animation-delay: 1.5s;
	-webkit-animation-delay: 1.5s;
	-moz-animation-delay: 1.5s;
	-o-animation-delay: 1.5s;
}

.animated.delay-05 {
	animation-delay: 2s;
	-webkit-animation-delay: 2s;
	-moz-animation-delay: 2s;
	-o-animation-delay: 2s;
}

.animated.delay-06 {
	animation-delay: 2.5s;
	-webkit-animation-delay: 2.5s;
	-moz-animation-delay: 2.5s;
	-o-animation-delay: 2.5s;
}

.animated.delay-07 {
	animation-delay: 3s;
	-webkit-animation-delay: 3s;
	-moz-animation-delay: 3s;
	-o-animation-delay: 3s;
}

.animated.delay-08 {
	animation-delay: 3.5s;
	-webkit-animation-delay: 3.5s;
	-moz-animation-delay: 3.5s;
	-o-animation-delay: 3.5s;
}

.animated.delay-09 {
	animation-delay: 4s;
	-webkit-animation-delay: 4s;
	-moz-animation-delay: 4s;
	-o-animation-delay: 4s;
}

.animated.delay-10 {
	animation-delay: 4.5s;
	-webkit-animation-delay: 4.5s;
	-moz-animation-delay: 4.5s;
	-o-animation-delay: 4.5s;
}

.animated.delay-11 {
	animation-delay: 5s;
	-webkit-animation-delay: 5s;
	-moz-animation-delay: 5s;
	-o-animation-delay: 5s;
}

.animated.delay-12 {
	animation-delay: 5.5s;
	-webkit-animation-delay: 5.5s;
	-moz-animation-delay: 5.5s;
	-o-animation-delay: 5.5s;
}

.animated.delay-13 {
	animation-delay: 6s;
	-webkit-animation-delay: 6s;
	-moz-animation-delay: 6s;
	-o-animation-delay: 6s;
}

.animated.delay-14 {
	animation-delay: 6.5s;
	-webkit-animation-delay: 6.5s;
	-moz-animation-delay: 6.5s;
	-o-animation-delay: 6.5s;
}

.animated.delay-15 {
	animation-delay: 7s;
	-webkit-animation-delay: 7s;
	-moz-animation-delay: 7s;
	-o-animation-delay: 7s;
}

.animated.delay-16 {
	animation-delay: 7.5s;
	-webkit-animation-delay: 7.5s;
	-moz-animation-delay: 7.5s;
	-o-animation-delay: 7.5s;
}

.animated.delay-17 {
	animation-delay: 8s;
	-webkit-animation-delay: 8s;
	-moz-animation-delay: 8s;
	-o-animation-delay: 8s;
}

.animated.delay-18 {
	animation-delay: 8.5s;
	-webkit-animation-delay: 8.5s;
	-moz-animation-delay: 8.5s;
	-o-animation-delay: 8.5s;
}

.animated.delay-19 {
	animation-delay: 9s;
	-webkit-animation-delay: 9s;
	-moz-animation-delay: 9s;
	-o-animation-delay: 9s;
}

.animated.delay-20 {
	animation-delay: 9.5s;
	-webkit-animation-delay: 9.5s;
	-moz-animation-delay: 9.5s;
	-o-animation-delay: 9.5s;
}

.animated {
	-webkit-animation-duration: 1s;
	-moz-animation-duration: 1s;
	-o-animation-duration: 1s;
	animation-duration: 1s;
	-webkit-animation-fill-mode: both;
	   -moz-animation-fill-mode: both;
	     -o-animation-fill-mode: both;
	        animation-fill-mode: both;
}

.animated.hinge{
	-webkit-animation-duration:2s;
	-moz-animation-duration:2s;
	-ms-animation-duration:2s;
	-o-animation-duration:2s;
	animation-duration:2s;
}

@-webkit-keyframes flash {
	0%, 50%, 100% {opacity: 1;}	25%, 75% {opacity: 0;}
}

@-moz-keyframes flash {
	0%, 50%, 100% {opacity: 1;}	
	25%, 75% {opacity: 0;}
}

@-o-keyframes flash {
	0%, 50%, 100% {opacity: 1;}	
	25%, 75% {opacity: 0;}
}

@keyframes flash {
	0%, 50%, 100% {opacity: 1;}	
	25%, 75% {opacity: 0;}
}

.flash {
	-webkit-animation-name: flash;
	-moz-animation-name: flash;
	-o-animation-name: flash;
	animation-name: flash;
}
@-webkit-keyframes shake {
	0%, 100% {-webkit-transform: translateX(0);}
	10%, 30%, 50%, 70%, 90% {-webkit-transform: translateX(-10px);}
	20%, 40%, 60%, 80% {-webkit-transform: translateX(10px);}
}

@-moz-keyframes shake {
	0%, 100% {-moz-transform: translateX(0);}
	10%, 30%, 50%, 70%, 90% {-moz-transform: translateX(-10px);}
	20%, 40%, 60%, 80% {-moz-transform: translateX(10px);}
}

@-o-keyframes shake {
	0%, 100% {-o-transform: translateX(0);}
	10%, 30%, 50%, 70%, 90% {-o-transform: translateX(-10px);}
	20%, 40%, 60%, 80% {-o-transform: translateX(10px);}
}

@keyframes shake {
	0%, 100% {transform: translateX(0);}
	10%, 30%, 50%, 70%, 90% {transform: translateX(-10px);}
	20%, 40%, 60%, 80% {transform: translateX(10px);}
}

.shake {
	-webkit-animation-name: shake;
	-moz-animation-name: shake;
	-o-animation-name: shake;
	animation-name: shake;
}
@-webkit-keyframes bounce {
	0%, 20%, 50%, 80%, 100% {-webkit-transform: translateY(0);}
	40% {-webkit-transform: translateY(-30px);}
	60% {-webkit-transform: translateY(-15px);}
}

@-moz-keyframes bounce {
	0%, 20%, 50%, 80%, 100% {-moz-transform: translateY(0);}
	40% {-moz-transform: translateY(-30px);}
	60% {-moz-transform: translateY(-15px);}
}

@-o-keyframes bounce {
	0%, 20%, 50%, 80%, 100% {-o-transform: translateY(0);}
	40% {-o-transform: translateY(-30px);}
	60% {-o-transform: translateY(-15px);}
}
@keyframes bounce {
	0%, 20%, 50%, 80%, 100% {transform: translateY(0);}
	40% {transform: translateY(-30px);}
	60% {transform: translateY(-15px);}
}

.bounce {
	-webkit-animation-name: bounce;
	-moz-animation-name: bounce;
	-o-animation-name: bounce;
	animation-name: bounce;
}
@-webkit-keyframes tada {
	0% {-webkit-transform: scale(1);}	
	10%, 20% {-webkit-transform: scale(0.9) rotate(-3deg);}
	30%, 50%, 70%, 90% {-webkit-transform: scale(1.1) rotate(3deg);}
	40%, 60%, 80% {-webkit-transform: scale(1.1) rotate(-3deg);}
	100% {-webkit-transform: scale(1) rotate(0);}
}

@-moz-keyframes tada {
	0% {-moz-transform: scale(1);}	
	10%, 20% {-moz-transform: scale(0.9) rotate(-3deg);}
	30%, 50%, 70%, 90% {-moz-transform: scale(1.1) rotate(3deg);}
	40%, 60%, 80% {-moz-transform: scale(1.1) rotate(-3deg);}
	100% {-moz-transform: scale(1) rotate(0);}
}

@-o-keyframes tada {
	0% {-o-transform: scale(1);}	
	10%, 20% {-o-transform: scale(0.9) rotate(-3deg);}
	30%, 50%, 70%, 90% {-o-transform: scale(1.1) rotate(3deg);}
	40%, 60%, 80% {-o-transform: scale(1.1) rotate(-3deg);}
	100% {-o-transform: scale(1) rotate(0);}
}

@keyframes tada {
	0% {transform: scale(1);}	
	10%, 20% {transform: scale(0.9) rotate(-3deg);}
	30%, 50%, 70%, 90% {transform: scale(1.1) rotate(3deg);}
	40%, 60%, 80% {transform: scale(1.1) rotate(-3deg);}
	100% {transform: scale(1) rotate(0);}
}

.tada {
	-webkit-animation-name: tada;
	-moz-animation-name: tada;
	-o-animation-name: tada;
	animation-name: tada;
}
@-webkit-keyframes swing {
	20%, 40%, 60%, 80%, 100% { -webkit-transform-origin: top center; }
	20% { -webkit-transform: rotate(15deg); }	
	40% { -webkit-transform: rotate(-10deg); }
	60% { -webkit-transform: rotate(5deg); }	
	80% { -webkit-transform: rotate(-5deg); }	
	100% { -webkit-transform: rotate(0deg); }
}

@-moz-keyframes swing {
	20% { -moz-transform: rotate(15deg); }	
	40% { -moz-transform: rotate(-10deg); }
	60% { -moz-transform: rotate(5deg); }	
	80% { -moz-transform: rotate(-5deg); }	
	100% { -moz-transform: rotate(0deg); }
}

@-o-keyframes swing {
	20% { -o-transform: rotate(15deg); }	
	40% { -o-transform: rotate(-10deg); }
	60% { -o-transform: rotate(5deg); }	
	80% { -o-transform: rotate(-5deg); }	
	100% { -o-transform: rotate(0deg); }
}

@keyframes swing {
	20% { transform: rotate(15deg); }	
	40% { transform: rotate(-10deg); }
	60% { transform: rotate(5deg); }	
	80% { transform: rotate(-5deg); }	
	100% { transform: rotate(0deg); }
}

.swing {
	-webkit-transform-origin: top center;
	-moz-transform-origin: top center;
	-o-transform-origin: top center;
	transform-origin: top center;
	-webkit-animation-name: swing;
	-moz-animation-name: swing;
	-o-animation-name: swing;
	animation-name: swing;
}
/* originally authored by Nick Pettit - https://github.com/nickpettit/glide */

@-webkit-keyframes wobble {
  0% { -webkit-transform: translateX(0%); }
  15% { -webkit-transform: translateX(-25%) rotate(-5deg); }
  30% { -webkit-transform: translateX(20%) rotate(3deg); }
  45% { -webkit-transform: translateX(-15%) rotate(-3deg); }
  60% { -webkit-transform: translateX(10%) rotate(2deg); }
  75% { -webkit-transform: translateX(-5%) rotate(-1deg); }
  100% { -webkit-transform: translateX(0%); }
}

@-moz-keyframes wobble {
  0% { -moz-transform: translateX(0%); }
  15% { -moz-transform: translateX(-25%) rotate(-5deg); }
  30% { -moz-transform: translateX(20%) rotate(3deg); }
  45% { -moz-transform: translateX(-15%) rotate(-3deg); }
  60% { -moz-transform: translateX(10%) rotate(2deg); }
  75% { -moz-transform: translateX(-5%) rotate(-1deg); }
  100% { -moz-transform: translateX(0%); }
}

@-o-keyframes wobble {
  0% { -o-transform: translateX(0%); }
  15% { -o-transform: translateX(-25%) rotate(-5deg); }
  30% { -o-transform: translateX(20%) rotate(3deg); }
  45% { -o-transform: translateX(-15%) rotate(-3deg); }
  60% { -o-transform: translateX(10%) rotate(2deg); }
  75% { -o-transform: translateX(-5%) rotate(-1deg); }
  100% { -o-transform: translateX(0%); }
}

@keyframes wobble {
  0% { transform: translateX(0%); }
  15% { transform: translateX(-25%) rotate(-5deg); }
  30% { transform: translateX(20%) rotate(3deg); }
  45% { transform: translateX(-15%) rotate(-3deg); }
  60% { transform: translateX(10%) rotate(2deg); }
  75% { transform: translateX(-5%) rotate(-1deg); }
  100% { transform: translateX(0%); }
}

.wobble {
	-webkit-animation-name: wobble;
	-moz-animation-name: wobble;
	-o-animation-name: wobble;
	animation-name: wobble;
}
/* originally authored by Nick Pettit - https://github.com/nickpettit/glide */

@-webkit-keyframes pulse {
    0% { -webkit-transform: scale(1); }	
	50% { -webkit-transform: scale(1.1); }
    100% { -webkit-transform: scale(1); }
}
@-moz-keyframes pulse {
    0% { -moz-transform: scale(1); }	
	50% { -moz-transform: scale(1.1); }
    100% { -moz-transform: scale(1); }
}
@-o-keyframes pulse {
    0% { -o-transform: scale(1); }	
	50% { -o-transform: scale(1.1); }
    100% { -o-transform: scale(1); }
}
@keyframes pulse {
    0% { transform: scale(1); }	
	50% { transform: scale(1.1); }
    100% { transform: scale(1); }
}

.pulse {
	-webkit-animation-name: pulse;
	-moz-animation-name: pulse;
	-o-animation-name: pulse;
	animation-name: pulse;
}
@-webkit-keyframes flip {
	0% {
		-webkit-transform: perspective(400px) translateZ(0) rotateY(0) scale(1);
		-webkit-animation-timing-function: ease-out;
	}
	40% {
		-webkit-transform: perspective(400px) translateZ(150px) rotateY(170deg) scale(1);
		-webkit-animation-timing-function: ease-out;
	}
	50% {
		-webkit-transform: perspective(400px) translateZ(150px) rotateY(190deg) scale(1);
		-webkit-animation-timing-function: ease-in;
	}
	80% {
		-webkit-transform: perspective(400px) translateZ(0) rotateY(360deg) scale(.95);
		-webkit-animation-timing-function: ease-in;
	}
	100% {
		-webkit-transform: perspective(400px) translateZ(0) rotateY(360deg) scale(1);
		-webkit-animation-timing-function: ease-in;
	}
}
@-moz-keyframes flip {
	0% {
		-moz-transform: perspective(400px) translateZ(0) rotateY(0) scale(1);
		-moz-animation-timing-function: ease-out;
	}
	40% {
		-moz-transform: perspective(400px) translateZ(150px) rotateY(170deg) scale(1);
		-moz-animation-timing-function: ease-out;
	}
	50% {
		-moz-transform: perspective(400px) translateZ(150px) rotateY(190deg) scale(1);
		-moz-animation-timing-function: ease-in;
	}
	80% {
		-moz-transform: perspective(400px) translateZ(0) rotateY(360deg) scale(.95);
		-moz-animation-timing-function: ease-in;
	}
	100% {
		-moz-transform: perspective(400px) translateZ(0) rotateY(360deg) scale(1);
		-moz-animation-timing-function: ease-in;
	}
}
@-o-keyframes flip {
	0% {
		-o-transform: perspective(400px) translateZ(0) rotateY(0) scale(1);
		-o-animation-timing-function: ease-out;
	}
	40% {
		-o-transform: perspective(400px) translateZ(150px) rotateY(170deg) scale(1);
		-o-animation-timing-function: ease-out;
	}
	50% {
		-o-transform: perspective(400px) translateZ(150px) rotateY(190deg) scale(1);
		-o-animation-timing-function: ease-in;
	}
	80% {
		-o-transform: perspective(400px) translateZ(0) rotateY(360deg) scale(.95);
		-o-animation-timing-function: ease-in;
	}
	100% {
		-o-transform: perspective(400px) translateZ(0) rotateY(360deg) scale(1);
		-o-animation-timing-function: ease-in;
	}
}
@keyframes flip {
	0% {
		transform: perspective(400px) translateZ(0) rotateY(0) scale(1);
		animation-timing-function: ease-out;
	}
	40% {
		transform: perspective(400px) translateZ(150px) rotateY(170deg) scale(1);
		animation-timing-function: ease-out;
	}
	50% {
		transform: perspective(400px) translateZ(150px) rotateY(190deg) scale(1);
		animation-timing-function: ease-in;
	}
	80% {
		transform: perspective(400px) translateZ(0) rotateY(360deg) scale(.95);
		animation-timing-function: ease-in;
	}
	100% {
		transform: perspective(400px) translateZ(0) rotateY(360deg) scale(1);
		animation-timing-function: ease-in;
	}
}

.animated.flip {
	-webkit-backface-visibility: visible !important;
	-webkit-animation-name: flip;
	-moz-backface-visibility: visible !important;
	-moz-animation-name: flip;
	-o-backface-visibility: visible !important;
	-o-animation-name: flip;
	backface-visibility: visible !important;
	animation-name: flip;
}

@-webkit-keyframes flipInX {
    0% {
        -webkit-transform: perspective(400px) rotateX(90deg);
        opacity: 0;
    }
    
    40% {
        -webkit-transform: perspective(400px) rotateX(-10deg);
    }
    
    70% {
        -webkit-transform: perspective(400px) rotateX(10deg);
    }
    
    100% {
        -webkit-transform: perspective(400px) rotateX(0deg);
        opacity: 1;
    }
}
@-moz-keyframes flipInX {
    0% {
        -moz-transform: perspective(400px) rotateX(90deg);
        opacity: 0;
    }
    
    40% {
        -moz-transform: perspective(400px) rotateX(-10deg);
    }
    
    70% {
        -moz-transform: perspective(400px) rotateX(10deg);
    }
    
    100% {
        -moz-transform: perspective(400px) rotateX(0deg);
        opacity: 1;
    }
}
@-o-keyframes flipInX {
    0% {
        -o-transform: perspective(400px) rotateX(90deg);
        opacity: 0;
    }
    
    40% {
        -o-transform: perspective(400px) rotateX(-10deg);
    }
    
    70% {
        -o-transform: perspective(400px) rotateX(10deg);
    }
    
    100% {
        -o-transform: perspective(400px) rotateX(0deg);
        opacity: 1;
    }
}
@keyframes flipInX {
    0% {
        transform: perspective(400px) rotateX(90deg);
        opacity: 0;
    }
    
    40% {
        transform: perspective(400px) rotateX(-10deg);
    }
    
    70% {
        transform: perspective(400px) rotateX(10deg);
    }
    
    100% {
        transform: perspective(400px) rotateX(0deg);
        opacity: 1;
    }
}

.flipInX {
	-webkit-backface-visibility: visible !important;
	-webkit-animation-name: flipInX;
	-moz-backface-visibility: visible !important;
	-moz-animation-name: flipInX;
	-o-backface-visibility: visible !important;
	-o-animation-name: flipInX;
	backface-visibility: visible !important;
	animation-name: flipInX;
}
@-webkit-keyframes flipOutX {
    0% {
        -webkit-transform: perspective(400px) rotateX(0deg);
        opacity: 1;
    }
	100% {
        -webkit-transform: perspective(400px) rotateX(90deg);
        opacity: 0;
    }
}

@-moz-keyframes flipOutX {
    0% {
        -moz-transform: perspective(400px) rotateX(0deg);
        opacity: 1;
    }
	100% {
        -moz-transform: perspective(400px) rotateX(90deg);
        opacity: 0;
    }
}

@-o-keyframes flipOutX {
    0% {
        -o-transform: perspective(400px) rotateX(0deg);
        opacity: 1;
    }
	100% {
        -o-transform: perspective(400px) rotateX(90deg);
        opacity: 0;
    }
}

@keyframes flipOutX {
    0% {
        transform: perspective(400px) rotateX(0deg);
        opacity: 1;
    }
	100% {
        transform: perspective(400px) rotateX(90deg);
        opacity: 0;
    }
}

.flipOutX {
	-webkit-animation-name: flipOutX;
	-webkit-backface-visibility: visible !important;
	-moz-animation-name: flipOutX;
	-moz-backface-visibility: visible !important;
	-o-animation-name: flipOutX;
	-o-backface-visibility: visible !important;
	animation-name: flipOutX;
	backface-visibility: visible !important;
}
@-webkit-keyframes flipInY {
    0% {
        -webkit-transform: perspective(400px) rotateY(90deg);
        opacity: 0;
    }
    
    40% {
        -webkit-transform: perspective(400px) rotateY(-10deg);
    }
    
    70% {
        -webkit-transform: perspective(400px) rotateY(10deg);
    }
    
    100% {
        -webkit-transform: perspective(400px) rotateY(0deg);
        opacity: 1;
    }
}
@-moz-keyframes flipInY {
    0% {
        -moz-transform: perspective(400px) rotateY(90deg);
        opacity: 0;
    }
    
    40% {
        -moz-transform: perspective(400px) rotateY(-10deg);
    }
    
    70% {
        -moz-transform: perspective(400px) rotateY(10deg);
    }
    
    100% {
        -moz-transform: perspective(400px) rotateY(0deg);
        opacity: 1;
    }
}
@-o-keyframes flipInY {
    0% {
        -o-transform: perspective(400px) rotateY(90deg);
        opacity: 0;
    }
    
    40% {
        -o-transform: perspective(400px) rotateY(-10deg);
    }
    
    70% {
        -o-transform: perspective(400px) rotateY(10deg);
    }
    
    100% {
        -o-transform: perspective(400px) rotateY(0deg);
        opacity: 1;
    }
}
@keyframes flipInY {
    0% {
        transform: perspective(400px) rotateY(90deg);
        opacity: 0;
    }
    
    40% {
        transform: perspective(400px) rotateY(-10deg);
    }
    
    70% {
        transform: perspective(400px) rotateY(10deg);
    }
    
    100% {
        transform: perspective(400px) rotateY(0deg);
        opacity: 1;
    }
}

.flipInY {
	-webkit-backface-visibility: visible !important;
	-webkit-animation-name: flipInY;
	-moz-backface-visibility: visible !important;
	-moz-animation-name: flipInY;
	-o-backface-visibility: visible !important;
	-o-animation-name: flipInY;
	backface-visibility: visible !important;
	animation-name: flipInY;
}
@-webkit-keyframes flipOutY {
    0% {
        -webkit-transform: perspective(400px) rotateY(0deg);
        opacity: 1;
    }
	100% {
        -webkit-transform: perspective(400px) rotateY(90deg);
        opacity: 0;
    }
}
@-moz-keyframes flipOutY {
    0% {
        -moz-transform: perspective(400px) rotateY(0deg);
        opacity: 1;
    }
	100% {
        -moz-transform: perspective(400px) rotateY(90deg);
        opacity: 0;
    }
}
@-o-keyframes flipOutY {
    0% {
        -o-transform: perspective(400px) rotateY(0deg);
        opacity: 1;
    }
	100% {
        -o-transform: perspective(400px) rotateY(90deg);
        opacity: 0;
    }
}
@keyframes flipOutY {
    0% {
        transform: perspective(400px) rotateY(0deg);
        opacity: 1;
    }
	100% {
        transform: perspective(400px) rotateY(90deg);
        opacity: 0;
    }
}

.flipOutY {
	-webkit-backface-visibility: visible !important;
	-webkit-animation-name: flipOutY;
	-moz-backface-visibility: visible !important;
	-moz-animation-name: flipOutY;
	-o-backface-visibility: visible !important;
	-o-animation-name: flipOutY;
	backface-visibility: visible !important;
	animation-name: flipOutY;
}
@-webkit-keyframes fadeIn {
	0% {opacity: 0;}	
	100% {opacity: 1;}
}

@-moz-keyframes fadeIn {
	0% {opacity: 0;}	
	100% {opacity: 1;}
}

@-o-keyframes fadeIn {
	0% {opacity: 0;}	
	100% {opacity: 1;}
}

@keyframes fadeIn {
	0% {opacity: 0;}	
	100% {opacity: 1;}
}

.fadeIn {
	-webkit-animation-name: fadeIn;
	-moz-animation-name: fadeIn;
	-o-animation-name: fadeIn;
	animation-name: fadeIn;
}
@-webkit-keyframes fadeInUp {
	0% {
		opacity: 0;
		-webkit-transform: translateY(20px);
	}
	
	100% {
		opacity: 1;
		-webkit-transform: translateY(0);
	}
}

@-moz-keyframes fadeInUp {
	0% {
		opacity: 0;
		-moz-transform: translateY(20px);
	}
	
	100% {
		opacity: 1;
		-moz-transform: translateY(0);
	}
}

@-o-keyframes fadeInUp {
	0% {
		opacity: 0;
		-o-transform: translateY(20px);
	}
	
	100% {
		opacity: 1;
		-o-transform: translateY(0);
	}
}

@keyframes fadeInUp {
	0% {
		opacity: 0;
		transform: translateY(20px);
	}
	
	100% {
		opacity: 1;
		transform: translateY(0);
	}
}

.fadeInUp {
	-webkit-animation-name: fadeInUp;
	-moz-animation-name: fadeInUp;
	-o-animation-name: fadeInUp;
	animation-name: fadeInUp;
}
@-webkit-keyframes fadeInDown {
	0% {
		opacity: 0;
		-webkit-transform: translateY(-20px);
	}
	
	100% {
		opacity: 1;
		-webkit-transform: translateY(0);
	}
}

@-moz-keyframes fadeInDown {
	0% {
		opacity: 0;
		-moz-transform: translateY(-20px);
	}
	
	100% {
		opacity: 1;
		-moz-transform: translateY(0);
	}
}

@-o-keyframes fadeInDown {
	0% {
		opacity: 0;
		-o-transform: translateY(-20px);
	}
	
	100% {
		opacity: 1;
		-o-transform: translateY(0);
	}
}

@keyframes fadeInDown {
	0% {
		opacity: 0;
		transform: translateY(-20px);
	}
	
	100% {
		opacity: 1;
		transform: translateY(0);
	}
}

.fadeInDown {
	-webkit-animation-name: fadeInDown;
	-moz-animation-name: fadeInDown;
	-o-animation-name: fadeInDown;
	animation-name: fadeInDown;
}
@-webkit-keyframes fadeInLeft {
	0% {
		opacity: 0;
		-webkit-transform: translateX(-20px);
	}
	
	100% {
		opacity: 1;
		-webkit-transform: translateX(0);
	}
}

@-moz-keyframes fadeInLeft {
	0% {
		opacity: 0;
		-moz-transform: translateX(-20px);
	}
	
	100% {
		opacity: 1;
		-moz-transform: translateX(0);
	}
}

@-o-keyframes fadeInLeft {
	0% {
		opacity: 0;
		-o-transform: translateX(-20px);
	}
	
	100% {
		opacity: 1;
		-o-transform: translateX(0);
	}
}

@keyframes fadeInLeft {
	0% {
		opacity: 0;
		transform: translateX(-20px);
	}
	
	100% {
		opacity: 1;
		transform: translateX(0);
	}
}

.fadeInLeft {
	-webkit-animation-name: fadeInLeft;
	-moz-animation-name: fadeInLeft;
	-o-animation-name: fadeInLeft;
	animation-name: fadeInLeft;
}
@-webkit-keyframes fadeInRight {
	0% {
		opacity: 0;
		-webkit-transform: translateX(20px);
	}
	
	100% {
		opacity: 1;
		-webkit-transform: translateX(0);
	}
}

@-moz-keyframes fadeInRight {
	0% {
		opacity: 0;
		-moz-transform: translateX(20px);
	}
	
	100% {
		opacity: 1;
		-moz-transform: translateX(0);
	}
}

@-o-keyframes fadeInRight {
	0% {
		opacity: 0;
		-o-transform: translateX(20px);
	}
	
	100% {
		opacity: 1;
		-o-transform: translateX(0);
	}
}

@keyframes fadeInRight {
	0% {
		opacity: 0;
		transform: translateX(20px);
	}
	
	100% {
		opacity: 1;
		transform: translateX(0);
	}
}

.fadeInRight {
	-webkit-animation-name: fadeInRight;
	-moz-animation-name: fadeInRight;
	-o-animation-name: fadeInRight;
	animation-name: fadeInRight;
}
@-webkit-keyframes fadeInUpBig {
	0% {
		opacity: 0;
		-webkit-transform: translateY(2000px);
	}
	
	100% {
		opacity: 1;
		-webkit-transform: translateY(0);
	}
}

@-moz-keyframes fadeInUpBig {
	0% {
		opacity: 0;
		-moz-transform: translateY(2000px);
	}
	
	100% {
		opacity: 1;
		-moz-transform: translateY(0);
	}
}

@-o-keyframes fadeInUpBig {
	0% {
		opacity: 0;
		-o-transform: translateY(2000px);
	}
	
	100% {
		opacity: 1;
		-o-transform: translateY(0);
	}
}

@keyframes fadeInUpBig {
	0% {
		opacity: 0;
		transform: translateY(2000px);
	}
	
	100% {
		opacity: 1;
		transform: translateY(0);
	}
}

.fadeInUpBig {
	-webkit-animation-name: fadeInUpBig;
	-moz-animation-name: fadeInUpBig;
	-o-animation-name: fadeInUpBig;
	animation-name: fadeInUpBig;
}
@-webkit-keyframes fadeInDownBig {
	0% {
		opacity: 0;
		-webkit-transform: translateY(-2000px);
	}
	
	100% {
		opacity: 1;
		-webkit-transform: translateY(0);
	}
}

@-moz-keyframes fadeInDownBig {
	0% {
		opacity: 0;
		-moz-transform: translateY(-2000px);
	}
	
	100% {
		opacity: 1;
		-moz-transform: translateY(0);
	}
}

@-o-keyframes fadeInDownBig {
	0% {
		opacity: 0;
		-o-transform: translateY(-2000px);
	}
	
	100% {
		opacity: 1;
		-o-transform: translateY(0);
	}
}

@keyframes fadeInDownBig {
	0% {
		opacity: 0;
		transform: translateY(-2000px);
	}
	
	100% {
		opacity: 1;
		transform: translateY(0);
	}
}

.fadeInDownBig {
	-webkit-animation-name: fadeInDownBig;
	-moz-animation-name: fadeInDownBig;
	-o-animation-name: fadeInDownBig;
	animation-name: fadeInDownBig;
}
@-webkit-keyframes fadeInLeftBig {
	0% {
		opacity: 0;
		-webkit-transform: translateX(-2000px);
	}
	
	100% {
		opacity: 1;
		-webkit-transform: translateX(0);
	}
}
@-moz-keyframes fadeInLeftBig {
	0% {
		opacity: 0;
		-moz-transform: translateX(-2000px);
	}
	
	100% {
		opacity: 1;
		-moz-transform: translateX(0);
	}
}
@-o-keyframes fadeInLeftBig {
	0% {
		opacity: 0;
		-o-transform: translateX(-2000px);
	}
	
	100% {
		opacity: 1;
		-o-transform: translateX(0);
	}
}
@keyframes fadeInLeftBig {
	0% {
		opacity: 0;
		transform: translateX(-2000px);
	}
	
	100% {
		opacity: 1;
		transform: translateX(0);
	}
}

.fadeInLeftBig {
	-webkit-animation-name: fadeInLeftBig;
	-moz-animation-name: fadeInLeftBig;
	-o-animation-name: fadeInLeftBig;
	animation-name: fadeInLeftBig;
}
@-webkit-keyframes fadeInRightBig {
	0% {
		opacity: 0;
		-webkit-transform: translateX(2000px);
	}
	
	100% {
		opacity: 1;
		-webkit-transform: translateX(0);
	}
}

@-moz-keyframes fadeInRightBig {
	0% {
		opacity: 0;
		-moz-transform: translateX(2000px);
	}
	
	100% {
		opacity: 1;
		-moz-transform: translateX(0);
	}
}

@-o-keyframes fadeInRightBig {
	0% {
		opacity: 0;
		-o-transform: translateX(2000px);
	}
	
	100% {
		opacity: 1;
		-o-transform: translateX(0);
	}
}

@keyframes fadeInRightBig {
	0% {
		opacity: 0;
		transform: translateX(2000px);
	}
	
	100% {
		opacity: 1;
		transform: translateX(0);
	}
}

.fadeInRightBig {
	-webkit-animation-name: fadeInRightBig;
	-moz-animation-name: fadeInRightBig;
	-o-animation-name: fadeInRightBig;
	animation-name: fadeInRightBig;
}
@-webkit-keyframes fadeOut {
	0% {opacity: 1;}
	100% {opacity: 0;}
}

@-moz-keyframes fadeOut {
	0% {opacity: 1;}
	100% {opacity: 0;}
}

@-o-keyframes fadeOut {
	0% {opacity: 1;}
	100% {opacity: 0;}
}

@keyframes fadeOut {
	0% {opacity: 1;}
	100% {opacity: 0;}
}

.fadeOut {
	-webkit-animation-name: fadeOut;
	-moz-animation-name: fadeOut;
	-o-animation-name: fadeOut;
	animation-name: fadeOut;
}
@-webkit-keyframes fadeOutUp {
	0% {
		opacity: 1;
		-webkit-transform: translateY(0);
	}
	
	100% {
		opacity: 0;
		-webkit-transform: translateY(-20px);
	}
}
@-moz-keyframes fadeOutUp {
	0% {
		opacity: 1;
		-moz-transform: translateY(0);
	}
	
	100% {
		opacity: 0;
		-moz-transform: translateY(-20px);
	}
}
@-o-keyframes fadeOutUp {
	0% {
		opacity: 1;
		-o-transform: translateY(0);
	}
	
	100% {
		opacity: 0;
		-o-transform: translateY(-20px);
	}
}
@keyframes fadeOutUp {
	0% {
		opacity: 1;
		transform: translateY(0);
	}
	
	100% {
		opacity: 0;
		transform: translateY(-20px);
	}
}

.fadeOutUp {
	-webkit-animation-name: fadeOutUp;
	-moz-animation-name: fadeOutUp;
	-o-animation-name: fadeOutUp;
	animation-name: fadeOutUp;
}
@-webkit-keyframes fadeOutDown {
	0% {
		opacity: 1;
		-webkit-transform: translateY(0);
	}
	
	100% {
		opacity: 0;
		-webkit-transform: translateY(20px);
	}
}

@-moz-keyframes fadeOutDown {
	0% {
		opacity: 1;
		-moz-transform: translateY(0);
	}
	
	100% {
		opacity: 0;
		-moz-transform: translateY(20px);
	}
}

@-o-keyframes fadeOutDown {
	0% {
		opacity: 1;
		-o-transform: translateY(0);
	}
	
	100% {
		opacity: 0;
		-o-transform: translateY(20px);
	}
}

@keyframes fadeOutDown {
	0% {
		opacity: 1;
		transform: translateY(0);
	}
	
	100% {
		opacity: 0;
		transform: translateY(20px);
	}
}

.fadeOutDown {
	-webkit-animation-name: fadeOutDown;
	-moz-animation-name: fadeOutDown;
	-o-animation-name: fadeOutDown;
	animation-name: fadeOutDown;
}
@-webkit-keyframes fadeOutLeft {
	0% {
		opacity: 1;
		-webkit-transform: translateX(0);
	}
	
	100% {
		opacity: 0;
		-webkit-transform: translateX(-20px);
	}
}

@-moz-keyframes fadeOutLeft {
	0% {
		opacity: 1;
		-moz-transform: translateX(0);
	}
	
	100% {
		opacity: 0;
		-moz-transform: translateX(-20px);
	}
}

@-o-keyframes fadeOutLeft {
	0% {
		opacity: 1;
		-o-transform: translateX(0);
	}
	
	100% {
		opacity: 0;
		-o-transform: translateX(-20px);
	}
}

@keyframes fadeOutLeft {
	0% {
		opacity: 1;
		transform: translateX(0);
	}
	
	100% {
		opacity: 0;
		transform: translateX(-20px);
	}
}

.fadeOutLeft {
	-webkit-animation-name: fadeOutLeft;
	-moz-animation-name: fadeOutLeft;
	-o-animation-name: fadeOutLeft;
	animation-name: fadeOutLeft;
}
@-webkit-keyframes fadeOutRight {
	0% {
		opacity: 1;
		-webkit-transform: translateX(0);
	}
	
	100% {
		opacity: 0;
		-webkit-transform: translateX(20px);
	}
}

@-moz-keyframes fadeOutRight {
	0% {
		opacity: 1;
		-moz-transform: translateX(0);
	}
	
	100% {
		opacity: 0;
		-moz-transform: translateX(20px);
	}
}

@-o-keyframes fadeOutRight {
	0% {
		opacity: 1;
		-o-transform: translateX(0);
	}
	
	100% {
		opacity: 0;
		-o-transform: translateX(20px);
	}
}

@keyframes fadeOutRight {
	0% {
		opacity: 1;
		transform: translateX(0);
	}
	
	100% {
		opacity: 0;
		transform: translateX(20px);
	}
}

.fadeOutRight {
	-webkit-animation-name: fadeOutRight;
	-moz-animation-name: fadeOutRight;
	-o-animation-name: fadeOutRight;
	animation-name: fadeOutRight;
}
@-webkit-keyframes fadeOutUpBig {
	0% {
		opacity: 1;
		-webkit-transform: translateY(0);
	}
	
	100% {
		opacity: 0;
		-webkit-transform: translateY(-2000px);
	}
}

@-moz-keyframes fadeOutUpBig {
	0% {
		opacity: 1;
		-moz-transform: translateY(0);
	}
	
	100% {
		opacity: 0;
		-moz-transform: translateY(-2000px);
	}
}

@-o-keyframes fadeOutUpBig {
	0% {
		opacity: 1;
		-o-transform: translateY(0);
	}
	
	100% {
		opacity: 0;
		-o-transform: translateY(-2000px);
	}
}

@keyframes fadeOutUpBig {
	0% {
		opacity: 1;
		transform: translateY(0);
	}
	
	100% {
		opacity: 0;
		transform: translateY(-2000px);
	}
}

.fadeOutUpBig {
	-webkit-animation-name: fadeOutUpBig;
	-moz-animation-name: fadeOutUpBig;
	-o-animation-name: fadeOutUpBig;
	animation-name: fadeOutUpBig;
}
@-webkit-keyframes fadeOutDownBig {
	0% {
		opacity: 1;
		-webkit-transform: translateY(0);
	}
	
	100% {
		opacity: 0;
		-webkit-transform: translateY(2000px);
	}
}

@-moz-keyframes fadeOutDownBig {
	0% {
		opacity: 1;
		-moz-transform: translateY(0);
	}
	
	100% {
		opacity: 0;
		-moz-transform: translateY(2000px);
	}
}

@-o-keyframes fadeOutDownBig {
	0% {
		opacity: 1;
		-o-transform: translateY(0);
	}
	
	100% {
		opacity: 0;
		-o-transform: translateY(2000px);
	}
}

@keyframes fadeOutDownBig {
	0% {
		opacity: 1;
		transform: translateY(0);
	}
	
	100% {
		opacity: 0;
		transform: translateY(2000px);
	}
}

.fadeOutDownBig {
	-webkit-animation-name: fadeOutDownBig;
	-moz-animation-name: fadeOutDownBig;
	-o-animation-name: fadeOutDownBig;
	animation-name: fadeOutDownBig;
}
@-webkit-keyframes fadeOutLeftBig {
	0% {
		opacity: 1;
		-webkit-transform: translateX(0);
	}
	
	100% {
		opacity: 0;
		-webkit-transform: translateX(-2000px);
	}
}

@-moz-keyframes fadeOutLeftBig {
	0% {
		opacity: 1;
		-moz-transform: translateX(0);
	}
	
	100% {
		opacity: 0;
		-moz-transform: translateX(-2000px);
	}
}

@-o-keyframes fadeOutLeftBig {
	0% {
		opacity: 1;
		-o-transform: translateX(0);
	}
	
	100% {
		opacity: 0;
		-o-transform: translateX(-2000px);
	}
}

@keyframes fadeOutLeftBig {
	0% {
		opacity: 1;
		transform: translateX(0);
	}
	
	100% {
		opacity: 0;
		transform: translateX(-2000px);
	}
}

.fadeOutLeftBig {
	-webkit-animation-name: fadeOutLeftBig;
	-moz-animation-name: fadeOutLeftBig;
	-o-animation-name: fadeOutLeftBig;
	animation-name: fadeOutLeftBig;
}
@-webkit-keyframes fadeOutRightBig {
	0% {
		opacity: 1;
		-webkit-transform: translateX(0);
	}
	
	100% {
		opacity: 0;
		-webkit-transform: translateX(2000px);
	}
}
@-moz-keyframes fadeOutRightBig {
	0% {
		opacity: 1;
		-moz-transform: translateX(0);
	}
	
	100% {
		opacity: 0;
		-moz-transform: translateX(2000px);
	}
}
@-o-keyframes fadeOutRightBig {
	0% {
		opacity: 1;
		-o-transform: translateX(0);
	}
	
	100% {
		opacity: 0;
		-o-transform: translateX(2000px);
	}
}
@keyframes fadeOutRightBig {
	0% {
		opacity: 1;
		transform: translateX(0);
	}
	
	100% {
		opacity: 0;
		transform: translateX(2000px);
	}
}

.fadeOutRightBig {
	-webkit-animation-name: fadeOutRightBig;
	-moz-animation-name: fadeOutRightBig;
	-o-animation-name: fadeOutRightBig;
	animation-name: fadeOutRightBig;
}
@-webkit-keyframes slideInDown {
	0% {
		opacity: 0;
		-webkit-transform: translateY(-2000px);
	}

	100% {
		-webkit-transform: translateY(0);
	}
}

@-moz-keyframes slideInDown {
	0% {
		opacity: 0;
		-moz-transform: translateY(-2000px);
	}

	100% {
		-moz-transform: translateY(0);
	}
}

@-o-keyframes slideInDown {
	0% {
		opacity: 0;
		-o-transform: translateY(-2000px);
	}

	100% {
		-o-transform: translateY(0);
	}
}

@keyframes slideInDown {
	0% {
		opacity: 0;
		transform: translateY(-2000px);
	}

	100% {
		transform: translateY(0);
	}
}

.slideInDown {
	-webkit-animation-name: slideInDown;
	-moz-animation-name: slideInDown;
	-o-animation-name: slideInDown;
	animation-name: slideInDown;
}
@-webkit-keyframes slideInLeft {
	0% {
		opacity: 0;
		-webkit-transform: translateX(-2000px);
	}
	
	100% {
		-webkit-transform: translateX(0);
	}
}

@-moz-keyframes slideInLeft {
	0% {
		opacity: 0;
		-moz-transform: translateX(-2000px);
	}
	
	100% {
		-moz-transform: translateX(0);
	}
}

@-o-keyframes slideInLeft {
	0% {
		opacity: 0;
		-o-transform: translateX(-2000px);
	}
	
	100% {
		-o-transform: translateX(0);
	}
}

@keyframes slideInLeft {
	0% {
		opacity: 0;
		transform: translateX(-2000px);
	}
	
	100% {
		transform: translateX(0);
	}
}

.slideInLeft {
	-webkit-animation-name: slideInLeft;
	-moz-animation-name: slideInLeft;
	-o-animation-name: slideInLeft;
	animation-name: slideInLeft;
}
@-webkit-keyframes slideInRight {
	0% {
		opacity: 0;
		-webkit-transform: translateX(2000px);
	}
	
	100% {
		-webkit-transform: translateX(0);
	}
}

@-moz-keyframes slideInRight {
	0% {
		opacity: 0;
		-moz-transform: translateX(2000px);
	}
	
	100% {
		-moz-transform: translateX(0);
	}
}

@-o-keyframes slideInRight {
	0% {
		opacity: 0;
		-o-transform: translateX(2000px);
	}
	
	100% {
		-o-transform: translateX(0);
	}
}

@keyframes slideInRight {
	0% {
		opacity: 0;
		transform: translateX(2000px);
	}
	
	100% {
		transform: translateX(0);
	}
}

.slideInRight {
	-webkit-animation-name: slideInRight;
	-moz-animation-name: slideInRight;
	-o-animation-name: slideInRight;
	animation-name: slideInRight;
}
@-webkit-keyframes slideOutUp {
	0% {
		-webkit-transform: translateY(0);
	}

	100% {
		opacity: 0;
		-webkit-transform: translateY(-2000px);
	}
}

@-moz-keyframes slideOutUp {
	0% {
		-moz-transform: translateY(0);
	}

	100% {
		opacity: 0;
		-moz-transform: translateY(-2000px);
	}
}

@-o-keyframes slideOutUp {
	0% {
		-o-transform: translateY(0);
	}

	100% {
		opacity: 0;
		-o-transform: translateY(-2000px);
	}
}

@keyframes slideOutUp {
	0% {
		transform: translateY(0);
	}

	100% {
		opacity: 0;
		transform: translateY(-2000px);
	}
}

.slideOutUp {
	-webkit-animation-name: slideOutUp;
	-moz-animation-name: slideOutUp;
	-o-animation-name: slideOutUp;
	animation-name: slideOutUp;
}
@-webkit-keyframes slideOutLeft {
	0% {
		-webkit-transform: translateX(0);
	}
	
	100% {
		opacity: 0;
		-webkit-transform: translateX(-2000px);
	}
}

@-moz-keyframes slideOutLeft {
	0% {
		-moz-transform: translateX(0);
	}
	
	100% {
		opacity: 0;
		-moz-transform: translateX(-2000px);
	}
}

@-o-keyframes slideOutLeft {
	0% {
		-o-transform: translateX(0);
	}
	
	100% {
		opacity: 0;
		-o-transform: translateX(-2000px);
	}
}

@keyframes slideOutLeft {
	0% {
		transform: translateX(0);
	}
	
	100% {
		opacity: 0;
		transform: translateX(-2000px);
	}
}

.slideOutLeft {
	-webkit-animation-name: slideOutLeft;
	-moz-animation-name: slideOutLeft;
	-o-animation-name: slideOutLeft;
	animation-name: slideOutLeft;
}
@-webkit-keyframes slideOutRight {
	0% {
		-webkit-transform: translateX(0);
	}
	
	100% {
		opacity: 0;
		-webkit-transform: translateX(2000px);
	}
}

@-moz-keyframes slideOutRight {
	0% {
		-moz-transform: translateX(0);
	}
	
	100% {
		opacity: 0;
		-moz-transform: translateX(2000px);
	}
}

@-o-keyframes slideOutRight {
	0% {
		-o-transform: translateX(0);
	}
	
	100% {
		opacity: 0;
		-o-transform: translateX(2000px);
	}
}

@keyframes slideOutRight {
	0% {
		transform: translateX(0);
	}
	
	100% {
		opacity: 0;
		transform: translateX(2000px);
	}
}

.slideOutRight {
	-webkit-animation-name: slideOutRight;
	-moz-animation-name: slideOutRight;
	-o-animation-name: slideOutRight;
	animation-name: slideOutRight;
}
@-webkit-keyframes bounceIn {
	0% {
		opacity: 0;
		-webkit-transform: scale(.3);
	}
	
	50% {
		opacity: 1;
		-webkit-transform: scale(1.05);
	}
	
	70% {
		-webkit-transform: scale(.9);
	}
	
	100% {
		-webkit-transform: scale(1);
	}
}

@-moz-keyframes bounceIn {
	0% {
		opacity: 0;
		-moz-transform: scale(.3);
	}
	
	50% {
		opacity: 1;
		-moz-transform: scale(1.05);
	}
	
	70% {
		-moz-transform: scale(.9);
	}
	
	100% {
		-moz-transform: scale(1);
	}
}

@-o-keyframes bounceIn {
	0% {
		opacity: 0;
		-o-transform: scale(.3);
	}
	
	50% {
		opacity: 1;
		-o-transform: scale(1.05);
	}
	
	70% {
		-o-transform: scale(.9);
	}
	
	100% {
		-o-transform: scale(1);
	}
}

@keyframes bounceIn {
	0% {
		opacity: 0;
		transform: scale(.3);
	}
	
	50% {
		opacity: 1;
		transform: scale(1.05);
	}
	
	70% {
		transform: scale(.9);
	}
	
	100% {
		transform: scale(1);
	}
}

.bounceIn {
	-webkit-animation-name: bounceIn;
	-moz-animation-name: bounceIn;
	-o-animation-name: bounceIn;
	animation-name: bounceIn;
}
@-webkit-keyframes bounceInUp {
	0% {
		opacity: 0;
		-webkit-transform: translateY(2000px);
	}
	
	60% {
		opacity: 1;
		-webkit-transform: translateY(-30px);
	}
	
	80% {
		-webkit-transform: translateY(10px);
	}
	
	100% {
		-webkit-transform: translateY(0);
	}
}
@-moz-keyframes bounceInUp {
	0% {
		opacity: 0;
		-moz-transform: translateY(2000px);
	}
	
	60% {
		opacity: 1;
		-moz-transform: translateY(-30px);
	}
	
	80% {
		-moz-transform: translateY(10px);
	}
	
	100% {
		-moz-transform: translateY(0);
	}
}

@-o-keyframes bounceInUp {
	0% {
		opacity: 0;
		-o-transform: translateY(2000px);
	}
	
	60% {
		opacity: 1;
		-o-transform: translateY(-30px);
	}
	
	80% {
		-o-transform: translateY(10px);
	}
	
	100% {
		-o-transform: translateY(0);
	}
}

@keyframes bounceInUp {
	0% {
		opacity: 0;
		transform: translateY(2000px);
	}
	
	60% {
		opacity: 1;
		transform: translateY(-30px);
	}
	
	80% {
		transform: translateY(10px);
	}
	
	100% {
		transform: translateY(0);
	}
}

.bounceInUp {
	-webkit-animation-name: bounceInUp;
	-moz-animation-name: bounceInUp;
	-o-animation-name: bounceInUp;
	animation-name: bounceInUp;
}
@-webkit-keyframes bounceInDown {
	0% {
		opacity: 0;
		-webkit-transform: translateY(-2000px);
	}
	
	60% {
		opacity: 1;
		-webkit-transform: translateY(30px);
	}
	
	80% {
		-webkit-transform: translateY(-10px);
	}
	
	100% {
		-webkit-transform: translateY(0);
	}
}

@-moz-keyframes bounceInDown {
	0% {
		opacity: 0;
		-moz-transform: translateY(-2000px);
	}
	
	60% {
		opacity: 1;
		-moz-transform: translateY(30px);
	}
	
	80% {
		-moz-transform: translateY(-10px);
	}
	
	100% {
		-moz-transform: translateY(0);
	}
}

@-o-keyframes bounceInDown {
	0% {
		opacity: 0;
		-o-transform: translateY(-2000px);
	}
	
	60% {
		opacity: 1;
		-o-transform: translateY(30px);
	}
	
	80% {
		-o-transform: translateY(-10px);
	}
	
	100% {
		-o-transform: translateY(0);
	}
}

@keyframes bounceInDown {
	0% {
		opacity: 0;
		transform: translateY(-2000px);
	}
	
	60% {
		opacity: 1;
		transform: translateY(30px);
	}
	
	80% {
		transform: translateY(-10px);
	}
	
	100% {
		transform: translateY(0);
	}
}

.bounceInDown {
	-webkit-animation-name: bounceInDown;
	-moz-animation-name: bounceInDown;
	-o-animation-name: bounceInDown;
	animation-name: bounceInDown;
}
@-webkit-keyframes bounceInLeft {
	0% {
		opacity: 0;
		-webkit-transform: translateX(-2000px);
	}
	
	60% {
		opacity: 1;
		-webkit-transform: translateX(30px);
	}
	
	80% {
		-webkit-transform: translateX(-10px);
	}
	
	100% {
		-webkit-transform: translateX(0);
	}
}

@-moz-keyframes bounceInLeft {
	0% {
		opacity: 0;
		-moz-transform: translateX(-2000px);
	}
	
	60% {
		opacity: 1;
		-moz-transform: translateX(30px);
	}
	
	80% {
		-moz-transform: translateX(-10px);
	}
	
	100% {
		-moz-transform: translateX(0);
	}
}

@-o-keyframes bounceInLeft {
	0% {
		opacity: 0;
		-o-transform: translateX(-2000px);
	}
	
	60% {
		opacity: 1;
		-o-transform: translateX(30px);
	}
	
	80% {
		-o-transform: translateX(-10px);
	}
	
	100% {
		-o-transform: translateX(0);
	}
}

@keyframes bounceInLeft {
	0% {
		opacity: 0;
		transform: translateX(-2000px);
	}
	
	60% {
		opacity: 1;
		transform: translateX(30px);
	}
	
	80% {
		transform: translateX(-10px);
	}
	
	100% {
		transform: translateX(0);
	}
}

.bounceInLeft {
	-webkit-animation-name: bounceInLeft;
	-moz-animation-name: bounceInLeft;
	-o-animation-name: bounceInLeft;
	animation-name: bounceInLeft;
}
@-webkit-keyframes bounceInRight {
	0% {
		opacity: 0;
		-webkit-transform: translateX(2000px);
	}
	
	60% {
		opacity: 1;
		-webkit-transform: translateX(-30px);
	}
	
	80% {
		-webkit-transform: translateX(10px);
	}
	
	100% {
		-webkit-transform: translateX(0);
	}
}

@-moz-keyframes bounceInRight {
	0% {
		opacity: 0;
		-moz-transform: translateX(2000px);
	}
	
	60% {
		opacity: 1;
		-moz-transform: translateX(-30px);
	}
	
	80% {
		-moz-transform: translateX(10px);
	}
	
	100% {
		-moz-transform: translateX(0);
	}
}

@-o-keyframes bounceInRight {
	0% {
		opacity: 0;
		-o-transform: translateX(2000px);
	}
	
	60% {
		opacity: 1;
		-o-transform: translateX(-30px);
	}
	
	80% {
		-o-transform: translateX(10px);
	}
	
	100% {
		-o-transform: translateX(0);
	}
}

@keyframes bounceInRight {
	0% {
		opacity: 0;
		transform: translateX(2000px);
	}
	
	60% {
		opacity: 1;
		transform: translateX(-30px);
	}
	
	80% {
		transform: translateX(10px);
	}
	
	100% {
		transform: translateX(0);
	}
}

.bounceInRight {
	-webkit-animation-name: bounceInRight;
	-moz-animation-name: bounceInRight;
	-o-animation-name: bounceInRight;
	animation-name: bounceInRight;
}
@-webkit-keyframes bounceOut {
	0% {
		-webkit-transform: scale(1);
	}
	
	25% {
		-webkit-transform: scale(.95);
	}
	
	50% {
		opacity: 1;
		-webkit-transform: scale(1.1);
	}
	
	100% {
		opacity: 0;
		-webkit-transform: scale(.3);
	}	
}

@-moz-keyframes bounceOut {
	0% {
		-moz-transform: scale(1);
	}
	
	25% {
		-moz-transform: scale(.95);
	}
	
	50% {
		opacity: 1;
		-moz-transform: scale(1.1);
	}
	
	100% {
		opacity: 0;
		-moz-transform: scale(.3);
	}	
}

@-o-keyframes bounceOut {
	0% {
		-o-transform: scale(1);
	}
	
	25% {
		-o-transform: scale(.95);
	}
	
	50% {
		opacity: 1;
		-o-transform: scale(1.1);
	}
	
	100% {
		opacity: 0;
		-o-transform: scale(.3);
	}	
}

@keyframes bounceOut {
	0% {
		transform: scale(1);
	}
	
	25% {
		transform: scale(.95);
	}
	
	50% {
		opacity: 1;
		transform: scale(1.1);
	}
	
	100% {
		opacity: 0;
		transform: scale(.3);
	}	
}

.bounceOut {
	-webkit-animation-name: bounceOut;
	-moz-animation-name: bounceOut;
	-o-animation-name: bounceOut;
	animation-name: bounceOut;
}
@-webkit-keyframes bounceOutUp {
	0% {
		-webkit-transform: translateY(0);
	}
	
	20% {
		opacity: 1;
		-webkit-transform: translateY(20px);
	}
	
	100% {
		opacity: 0;
		-webkit-transform: translateY(-2000px);
	}
}

@-moz-keyframes bounceOutUp {
	0% {
		-moz-transform: translateY(0);
	}
	
	20% {
		opacity: 1;
		-moz-transform: translateY(20px);
	}
	
	100% {
		opacity: 0;
		-moz-transform: translateY(-2000px);
	}
}

@-o-keyframes bounceOutUp {
	0% {
		-o-transform: translateY(0);
	}
	
	20% {
		opacity: 1;
		-o-transform: translateY(20px);
	}
	
	100% {
		opacity: 0;
		-o-transform: translateY(-2000px);
	}
}

@keyframes bounceOutUp {
	0% {
		transform: translateY(0);
	}
	
	20% {
		opacity: 1;
		transform: translateY(20px);
	}
	
	100% {
		opacity: 0;
		transform: translateY(-2000px);
	}
}

.bounceOutUp {
	-webkit-animation-name: bounceOutUp;
	-moz-animation-name: bounceOutUp;
	-o-animation-name: bounceOutUp;
	animation-name: bounceOutUp;
}
@-webkit-keyframes bounceOutDown {
	0% {
		-webkit-transform: translateY(0);
	}
	
	20% {
		opacity: 1;
		-webkit-transform: translateY(-20px);
	}
	
	100% {
		opacity: 0;
		-webkit-transform: translateY(2000px);
	}
}

@-moz-keyframes bounceOutDown {
	0% {
		-moz-transform: translateY(0);
	}
	
	20% {
		opacity: 1;
		-moz-transform: translateY(-20px);
	}
	
	100% {
		opacity: 0;
		-moz-transform: translateY(2000px);
	}
}

@-o-keyframes bounceOutDown {
	0% {
		-o-transform: translateY(0);
	}
	
	20% {
		opacity: 1;
		-o-transform: translateY(-20px);
	}
	
	100% {
		opacity: 0;
		-o-transform: translateY(2000px);
	}
}

@keyframes bounceOutDown {
	0% {
		transform: translateY(0);
	}
	
	20% {
		opacity: 1;
		transform: translateY(-20px);
	}
	
	100% {
		opacity: 0;
		transform: translateY(2000px);
	}
}

.bounceOutDown {
	-webkit-animation-name: bounceOutDown;
	-moz-animation-name: bounceOutDown;
	-o-animation-name: bounceOutDown;
	animation-name: bounceOutDown;
}
@-webkit-keyframes bounceOutLeft {
	0% {
		-webkit-transform: translateX(0);
	}
	
	20% {
		opacity: 1;
		-webkit-transform: translateX(20px);
	}
	
	100% {
		opacity: 0;
		-webkit-transform: translateX(-2000px);
	}
}

@-moz-keyframes bounceOutLeft {
	0% {
		-moz-transform: translateX(0);
	}
	
	20% {
		opacity: 1;
		-moz-transform: translateX(20px);
	}
	
	100% {
		opacity: 0;
		-moz-transform: translateX(-2000px);
	}
}

@-o-keyframes bounceOutLeft {
	0% {
		-o-transform: translateX(0);
	}
	
	20% {
		opacity: 1;
		-o-transform: translateX(20px);
	}
	
	100% {
		opacity: 0;
		-o-transform: translateX(-2000px);
	}
}

@keyframes bounceOutLeft {
	0% {
		transform: translateX(0);
	}
	
	20% {
		opacity: 1;
		transform: translateX(20px);
	}
	
	100% {
		opacity: 0;
		transform: translateX(-2000px);
	}
}

.bounceOutLeft {
	-webkit-animation-name: bounceOutLeft;
	-moz-animation-name: bounceOutLeft;
	-o-animation-name: bounceOutLeft;
	animation-name: bounceOutLeft;
}
@-webkit-keyframes bounceOutRight {
	0% {
		-webkit-transform: translateX(0);
	}
	
	20% {
		opacity: 1;
		-webkit-transform: translateX(-20px);
	}
	
	100% {
		opacity: 0;
		-webkit-transform: translateX(2000px);
	}
}

@-moz-keyframes bounceOutRight {
	0% {
		-moz-transform: translateX(0);
	}
	
	20% {
		opacity: 1;
		-moz-transform: translateX(-20px);
	}
	
	100% {
		opacity: 0;
		-moz-transform: translateX(2000px);
	}
}

@-o-keyframes bounceOutRight {
	0% {
		-o-transform: translateX(0);
	}
	
	20% {
		opacity: 1;
		-o-transform: translateX(-20px);
	}
	
	100% {
		opacity: 0;
		-o-transform: translateX(2000px);
	}
}

@keyframes bounceOutRight {
	0% {
		transform: translateX(0);
	}
	
	20% {
		opacity: 1;
		transform: translateX(-20px);
	}
	
	100% {
		opacity: 0;
		transform: translateX(2000px);
	}
}

.bounceOutRight {
	-webkit-animation-name: bounceOutRight;
	-moz-animation-name: bounceOutRight;
	-o-animation-name: bounceOutRight;
	animation-name: bounceOutRight;
}
@-webkit-keyframes rotateIn {
	0% {
		-webkit-transform-origin: center center;
		-webkit-transform: rotate(-200deg);
		opacity: 0;
	}
	
	100% {
		-webkit-transform-origin: center center;
		-webkit-transform: rotate(0);
		opacity: 1;
	}
}
@-moz-keyframes rotateIn {
	0% {
		-moz-transform-origin: center center;
		-moz-transform: rotate(-200deg);
		opacity: 0;
	}
	
	100% {
		-moz-transform-origin: center center;
		-moz-transform: rotate(0);
		opacity: 1;
	}
}
@-o-keyframes rotateIn {
	0% {
		-o-transform-origin: center center;
		-o-transform: rotate(-200deg);
		opacity: 0;
	}
	
	100% {
		-o-transform-origin: center center;
		-o-transform: rotate(0);
		opacity: 1;
	}
}
@keyframes rotateIn {
	0% {
		transform-origin: center center;
		transform: rotate(-200deg);
		opacity: 0;
	}
	
	100% {
		transform-origin: center center;
		transform: rotate(0);
		opacity: 1;
	}
}

.rotateIn {
	-webkit-animation-name: rotateIn;
	-moz-animation-name: rotateIn;
	-o-animation-name: rotateIn;
	animation-name: rotateIn;
}
@-webkit-keyframes rotateInUpLeft {
	0% {
		-webkit-transform-origin: left bottom;
		-webkit-transform: rotate(90deg);
		opacity: 0;
	}
	
	100% {
		-webkit-transform-origin: left bottom;
		-webkit-transform: rotate(0);
		opacity: 1;
	}
}

@-moz-keyframes rotateInUpLeft {
	0% {
		-moz-transform-origin: left bottom;
		-moz-transform: rotate(90deg);
		opacity: 0;
	}
	
	100% {
		-moz-transform-origin: left bottom;
		-moz-transform: rotate(0);
		opacity: 1;
	}
}

@-o-keyframes rotateInUpLeft {
	0% {
		-o-transform-origin: left bottom;
		-o-transform: rotate(90deg);
		opacity: 0;
	}
	
	100% {
		-o-transform-origin: left bottom;
		-o-transform: rotate(0);
		opacity: 1;
	}
}

@keyframes rotateInUpLeft {
	0% {
		transform-origin: left bottom;
		transform: rotate(90deg);
		opacity: 0;
	}
	
	100% {
		transform-origin: left bottom;
		transform: rotate(0);
		opacity: 1;
	}
}

.rotateInUpLeft {
	-webkit-animation-name: rotateInUpLeft;
	-moz-animation-name: rotateInUpLeft;
	-o-animation-name: rotateInUpLeft;
	animation-name: rotateInUpLeft;
}
@-webkit-keyframes rotateInDownLeft {
	0% {
		-webkit-transform-origin: left bottom;
		-webkit-transform: rotate(-90deg);
		opacity: 0;
	}
	
	100% {
		-webkit-transform-origin: left bottom;
		-webkit-transform: rotate(0);
		opacity: 1;
	}
}

@-moz-keyframes rotateInDownLeft {
	0% {
		-moz-transform-origin: left bottom;
		-moz-transform: rotate(-90deg);
		opacity: 0;
	}
	
	100% {
		-moz-transform-origin: left bottom;
		-moz-transform: rotate(0);
		opacity: 1;
	}
}

@-o-keyframes rotateInDownLeft {
	0% {
		-o-transform-origin: left bottom;
		-o-transform: rotate(-90deg);
		opacity: 0;
	}
	
	100% {
		-o-transform-origin: left bottom;
		-o-transform: rotate(0);
		opacity: 1;
	}
}

@keyframes rotateInDownLeft {
	0% {
		transform-origin: left bottom;
		transform: rotate(-90deg);
		opacity: 0;
	}
	
	100% {
		transform-origin: left bottom;
		transform: rotate(0);
		opacity: 1;
	}
}

.rotateInDownLeft {
	-webkit-animation-name: rotateInDownLeft;
	-moz-animation-name: rotateInDownLeft;
	-o-animation-name: rotateInDownLeft;
	animation-name: rotateInDownLeft;
}
@-webkit-keyframes rotateInUpRight {
	0% {
		-webkit-transform-origin: right bottom;
		-webkit-transform: rotate(-90deg);
		opacity: 0;
	}
	
	100% {
		-webkit-transform-origin: right bottom;
		-webkit-transform: rotate(0);
		opacity: 1;
	}
}

@-moz-keyframes rotateInUpRight {
	0% {
		-moz-transform-origin: right bottom;
		-moz-transform: rotate(-90deg);
		opacity: 0;
	}
	
	100% {
		-moz-transform-origin: right bottom;
		-moz-transform: rotate(0);
		opacity: 1;
	}
}

@-o-keyframes rotateInUpRight {
	0% {
		-o-transform-origin: right bottom;
		-o-transform: rotate(-90deg);
		opacity: 0;
	}
	
	100% {
		-o-transform-origin: right bottom;
		-o-transform: rotate(0);
		opacity: 1;
	}
}

@keyframes rotateInUpRight {
	0% {
		transform-origin: right bottom;
		transform: rotate(-90deg);
		opacity: 0;
	}
	
	100% {
		transform-origin: right bottom;
		transform: rotate(0);
		opacity: 1;
	}
}

.rotateInUpRight {
	-webkit-animation-name: rotateInUpRight;
	-moz-animation-name: rotateInUpRight;
	-o-animation-name: rotateInUpRight;
	animation-name: rotateInUpRight;
}
@-webkit-keyframes rotateInDownRight {
	0% {
		-webkit-transform-origin: right bottom;
		-webkit-transform: rotate(90deg);
		opacity: 0;
	}
	
	100% {
		-webkit-transform-origin: right bottom;
		-webkit-transform: rotate(0);
		opacity: 1;
	}
}

@-moz-keyframes rotateInDownRight {
	0% {
		-moz-transform-origin: right bottom;
		-moz-transform: rotate(90deg);
		opacity: 0;
	}
	
	100% {
		-moz-transform-origin: right bottom;
		-moz-transform: rotate(0);
		opacity: 1;
	}
}

@-o-keyframes rotateInDownRight {
	0% {
		-o-transform-origin: right bottom;
		-o-transform: rotate(90deg);
		opacity: 0;
	}
	
	100% {
		-o-transform-origin: right bottom;
		-o-transform: rotate(0);
		opacity: 1;
	}
}

@keyframes rotateInDownRight {
	0% {
		transform-origin: right bottom;
		transform: rotate(90deg);
		opacity: 0;
	}
	
	100% {
		transform-origin: right bottom;
		transform: rotate(0);
		opacity: 1;
	}
}

.rotateInDownRight {
	-webkit-animation-name: rotateInDownRight;
	-moz-animation-name: rotateInDownRight;
	-o-animation-name: rotateInDownRight;
	animation-name: rotateInDownRight;
}
@-webkit-keyframes rotateOut {
	0% {
		-webkit-transform-origin: center center;
		-webkit-transform: rotate(0);
		opacity: 1;
	}
	
	100% {
		-webkit-transform-origin: center center;
		-webkit-transform: rotate(200deg);
		opacity: 0;
	}
}

@-moz-keyframes rotateOut {
	0% {
		-moz-transform-origin: center center;
		-moz-transform: rotate(0);
		opacity: 1;
	}
	
	100% {
		-moz-transform-origin: center center;
		-moz-transform: rotate(200deg);
		opacity: 0;
	}
}

@-o-keyframes rotateOut {
	0% {
		-o-transform-origin: center center;
		-o-transform: rotate(0);
		opacity: 1;
	}
	
	100% {
		-o-transform-origin: center center;
		-o-transform: rotate(200deg);
		opacity: 0;
	}
}

@keyframes rotateOut {
	0% {
		transform-origin: center center;
		transform: rotate(0);
		opacity: 1;
	}
	
	100% {
		transform-origin: center center;
		transform: rotate(200deg);
		opacity: 0;
	}
}

.rotateOut {
	-webkit-animation-name: rotateOut;
	-moz-animation-name: rotateOut;
	-o-animation-name: rotateOut;
	animation-name: rotateOut;
}
@-webkit-keyframes rotateOutUpLeft {
	0% {
		-webkit-transform-origin: left bottom;
		-webkit-transform: rotate(0);
		opacity: 1;
	}
	
	100% {
		-webkit-transform-origin: left bottom;
		-webkit-transform: rotate(-90deg);
		opacity: 0;
	}
}

@-moz-keyframes rotateOutUpLeft {
	0% {
		-moz-transform-origin: left bottom;
		-moz-transform: rotate(0);
		opacity: 1;
	}
	
	100% {
		-moz-transform-origin: left bottom;
		-moz-transform: rotate(-90deg);
		opacity: 0;
	}
}

@-o-keyframes rotateOutUpLeft {
	0% {
		-o-transform-origin: left bottom;
		-o-transform: rotate(0);
		opacity: 1;
	}
	
	100% {
		-o-transform-origin: left bottom;
		-o-transform: rotate(-90deg);
		opacity: 0;
	}
}

@keyframes rotateOutUpLeft {
	0% {
		transform-origin: left bottom;
		transform: rotate(0);
		opacity: 1;
	}
	
	100% {
		-transform-origin: left bottom;
		-transform: rotate(-90deg);
		opacity: 0;
	}
}

.rotateOutUpLeft {
	-webkit-animation-name: rotateOutUpLeft;
	-moz-animation-name: rotateOutUpLeft;
	-o-animation-name: rotateOutUpLeft;
	animation-name: rotateOutUpLeft;
}
@-webkit-keyframes rotateOutDownLeft {
	0% {
		-webkit-transform-origin: left bottom;
		-webkit-transform: rotate(0);
		opacity: 1;
	}
	
	100% {
		-webkit-transform-origin: left bottom;
		-webkit-transform: rotate(90deg);
		opacity: 0;
	}
}

@-moz-keyframes rotateOutDownLeft {
	0% {
		-moz-transform-origin: left bottom;
		-moz-transform: rotate(0);
		opacity: 1;
	}
	
	100% {
		-moz-transform-origin: left bottom;
		-moz-transform: rotate(90deg);
		opacity: 0;
	}
}

@-o-keyframes rotateOutDownLeft {
	0% {
		-o-transform-origin: left bottom;
		-o-transform: rotate(0);
		opacity: 1;
	}
	
	100% {
		-o-transform-origin: left bottom;
		-o-transform: rotate(90deg);
		opacity: 0;
	}
}

@keyframes rotateOutDownLeft {
	0% {
		transform-origin: left bottom;
		transform: rotate(0);
		opacity: 1;
	}
	
	100% {
		transform-origin: left bottom;
		transform: rotate(90deg);
		opacity: 0;
	}
}

.rotateOutDownLeft {
	-webkit-animation-name: rotateOutDownLeft;
	-moz-animation-name: rotateOutDownLeft;
	-o-animation-name: rotateOutDownLeft;
	animation-name: rotateOutDownLeft;
}
@-webkit-keyframes rotateOutUpRight {
	0% {
		-webkit-transform-origin: right bottom;
		-webkit-transform: rotate(0);
		opacity: 1;
	}
	
	100% {
		-webkit-transform-origin: right bottom;
		-webkit-transform: rotate(90deg);
		opacity: 0;
	}
}

@-moz-keyframes rotateOutUpRight {
	0% {
		-moz-transform-origin: right bottom;
		-moz-transform: rotate(0);
		opacity: 1;
	}
	
	100% {
		-moz-transform-origin: right bottom;
		-moz-transform: rotate(90deg);
		opacity: 0;
	}
}

@-o-keyframes rotateOutUpRight {
	0% {
		-o-transform-origin: right bottom;
		-o-transform: rotate(0);
		opacity: 1;
	}
	
	100% {
		-o-transform-origin: right bottom;
		-o-transform: rotate(90deg);
		opacity: 0;
	}
}

@keyframes rotateOutUpRight {
	0% {
		transform-origin: right bottom;
		transform: rotate(0);
		opacity: 1;
	}
	
	100% {
		transform-origin: right bottom;
		transform: rotate(90deg);
		opacity: 0;
	}
}

.rotateOutUpRight {
	-webkit-animation-name: rotateOutUpRight;
	-moz-animation-name: rotateOutUpRight;
	-o-animation-name: rotateOutUpRight;
	animation-name: rotateOutUpRight;
}
@-webkit-keyframes rotateOutDownRight {
	0% {
		-webkit-transform-origin: right bottom;
		-webkit-transform: rotate(0);
		opacity: 1;
	}
	
	100% {
		-webkit-transform-origin: right bottom;
		-webkit-transform: rotate(-90deg);
		opacity: 0;
	}
}

@-moz-keyframes rotateOutDownRight {
	0% {
		-moz-transform-origin: right bottom;
		-moz-transform: rotate(0);
		opacity: 1;
	}
	
	100% {
		-moz-transform-origin: right bottom;
		-moz-transform: rotate(-90deg);
		opacity: 0;
	}
}

@-o-keyframes rotateOutDownRight {
	0% {
		-o-transform-origin: right bottom;
		-o-transform: rotate(0);
		opacity: 1;
	}
	
	100% {
		-o-transform-origin: right bottom;
		-o-transform: rotate(-90deg);
		opacity: 0;
	}
}

@keyframes rotateOutDownRight {
	0% {
		transform-origin: right bottom;
		transform: rotate(0);
		opacity: 1;
	}
	
	100% {
		transform-origin: right bottom;
		transform: rotate(-90deg);
		opacity: 0;
	}
}

.rotateOutDownRight {
	-webkit-animation-name: rotateOutDownRight;
	-moz-animation-name: rotateOutDownRight;
	-o-animation-name: rotateOutDownRight;
	animation-name: rotateOutDownRight;
}
@-webkit-keyframes lightSpeedIn {
	0% { -webkit-transform: translateX(100%) skewX(-30deg); opacity: 0; }
	60% { -webkit-transform: translateX(-20%) skewX(30deg); opacity: 1; }
	80% { -webkit-transform: translateX(0%) skewX(-15deg); opacity: 1; }
	100% { -webkit-transform: translateX(0%) skewX(0deg); opacity: 1; }
}

@-moz-keyframes lightSpeedIn {
	0% { -moz-transform: translateX(100%) skewX(-30deg); opacity: 0; }
	60% { -moz-transform: translateX(-20%) skewX(30deg); opacity: 1; }
	80% { -moz-transform: translateX(0%) skewX(-15deg); opacity: 1; }
	100% { -moz-transform: translateX(0%) skewX(0deg); opacity: 1; }
}

@-o-keyframes lightSpeedIn {
	0% { -o-transform: translateX(100%) skewX(-30deg); opacity: 0; }
	60% { -o-transform: translateX(-20%) skewX(30deg); opacity: 1; }
	80% { -o-transform: translateX(0%) skewX(-15deg); opacity: 1; }
	100% { -o-transform: translateX(0%) skewX(0deg); opacity: 1; }
}

@keyframes lightSpeedIn {
	0% { transform: translateX(100%) skewX(-30deg); opacity: 0; }
	60% { transform: translateX(-20%) skewX(30deg); opacity: 1; }
	80% { transform: translateX(0%) skewX(-15deg); opacity: 1; }
	100% { transform: translateX(0%) skewX(0deg); opacity: 1; }
}

.lightSpeedIn {
    -webkit-animation-name: lightSpeedIn;
    -moz-animation-name: lightSpeedIn;
    -o-animation-name: lightSpeedIn;
    animation-name: lightSpeedIn;

    -webkit-animation-timing-function: ease-out;
    -moz-animation-timing-function: ease-out;
    -o-animation-timing-function: ease-out;
    animation-timing-function: ease-out;
}
@-webkit-keyframes lightSpeedOut {
    0% { -webkit-transform: translateX(0%) skewX(0deg); opacity: 1; }
	100% { -webkit-transform: translateX(100%) skewX(-30deg); opacity: 0; }
}

@-moz-keyframes lightSpeedOut {
	0% { -moz-transform: translateX(0%) skewX(0deg); opacity: 1; }
	100% { -moz-transform: translateX(100%) skewX(-30deg); opacity: 0; }
}

@-o-keyframes lightSpeedOut {
	0% { -o-transform: translateX(0%) skewX(0deg); opacity: 1; }
	100% { -o-transform: translateX(100%) skewX(-30deg); opacity: 0; }
}

@keyframes lightSpeedOut {
	0% { transform: translateX(0%) skewX(0deg); opacity: 1; }
	100% { transform: translateX(100%) skewX(-30deg); opacity: 0; }
}

.lightSpeedOut {
    -webkit-animation-name: lightSpeedOut;
    -moz-animation-name: lightSpeedOut;
    -o-animation-name: lightSpeedOut;
    animation-name: lightSpeedOut;

    -webkit-animation-timing-function: ease-in;
    -moz-animation-timing-function: ease-in;
    -o-animation-timing-function: ease-in;
    animation-timing-function: ease-in;
}
@-webkit-keyframes hinge {
	0% { -webkit-transform: rotate(0); -webkit-transform-origin: top left; -webkit-animation-timing-function: ease-in-out; }	
	20%, 60% { -webkit-transform: rotate(80deg); -webkit-transform-origin: top left; -webkit-animation-timing-function: ease-in-out; }	
	40% { -webkit-transform: rotate(60deg); -webkit-transform-origin: top left; -webkit-animation-timing-function: ease-in-out; }	
	80% { -webkit-transform: rotate(60deg) translateY(0); opacity: 1; -webkit-transform-origin: top left; -webkit-animation-timing-function: ease-in-out; }	
	100% { -webkit-transform: translateY(700px); opacity: 0; }
}

@-moz-keyframes hinge {
	0% { -moz-transform: rotate(0); -moz-transform-origin: top left; -moz-animation-timing-function: ease-in-out; }	
	20%, 60% { -moz-transform: rotate(80deg); -moz-transform-origin: top left; -moz-animation-timing-function: ease-in-out; }	
	40% { -moz-transform: rotate(60deg); -moz-transform-origin: top left; -moz-animation-timing-function: ease-in-out; }	
	80% { -moz-transform: rotate(60deg) translateY(0); opacity: 1; -moz-transform-origin: top left; -moz-animation-timing-function: ease-in-out; }	
	100% { -moz-transform: translateY(700px); opacity: 0; }
}

@-o-keyframes hinge {
	0% { -o-transform: rotate(0); -o-transform-origin: top left; -o-animation-timing-function: ease-in-out; }	
	20%, 60% { -o-transform: rotate(80deg); -o-transform-origin: top left; -o-animation-timing-function: ease-in-out; }	
	40% { -o-transform: rotate(60deg); -o-transform-origin: top left; -o-animation-timing-function: ease-in-out; }	
	80% { -o-transform: rotate(60deg) translateY(0); opacity: 1; -o-transform-origin: top left; -o-animation-timing-function: ease-in-out; }	
	100% { -o-transform: translateY(700px); opacity: 0; }
}

@keyframes hinge {
	0% { transform: rotate(0); transform-origin: top left; animation-timing-function: ease-in-out; }	
	20%, 60% { transform: rotate(80deg); transform-origin: top left; animation-timing-function: ease-in-out; }	
	40% { transform: rotate(60deg); transform-origin: top left; animation-timing-function: ease-in-out; }	
	80% { transform: rotate(60deg) translateY(0); opacity: 1; transform-origin: top left; animation-timing-function: ease-in-out; }	
	100% { transform: translateY(700px); opacity: 0; }
}

.hinge {
	-webkit-animation-name: hinge;
	-moz-animation-name: hinge;
	-o-animation-name: hinge;
	animation-name: hinge;
}
/* originally authored by Nick Pettit - https://github.com/nickpettit/glide */

@-webkit-keyframes rollIn {
	0% { opacity: 0; -webkit-transform: translateX(-100%) rotate(-120deg); }
	100% { opacity: 1; -webkit-transform: translateX(0px) rotate(0deg); }
}

@-moz-keyframes rollIn {
	0% { opacity: 0; -moz-transform: translateX(-100%) rotate(-120deg); }
	100% { opacity: 1; -moz-transform: translateX(0px) rotate(0deg); }
}

@-o-keyframes rollIn {
	0% { opacity: 0; -o-transform: translateX(-100%) rotate(-120deg); }
	100% { opacity: 1; -o-transform: translateX(0px) rotate(0deg); }
}

@keyframes rollIn {
	0% { opacity: 0; transform: translateX(-100%) rotate(-120deg); }
	100% { opacity: 1; transform: translateX(0px) rotate(0deg); }
}

.rollIn {
	-webkit-animation-name: rollIn;
	-moz-animation-name: rollIn;
	-o-animation-name: rollIn;
	animation-name: rollIn;
}
/* originally authored by Nick Pettit - https://github.com/nickpettit/glide */

@-webkit-keyframes rollOut {
    0% {
		opacity: 1;
		-webkit-transform: translateX(0px) rotate(0deg);
	}

    100% {
		opacity: 0;
		-webkit-transform: translateX(100%) rotate(120deg);
	}
}

@-moz-keyframes rollOut {
    0% {
		opacity: 1;
		-moz-transform: translateX(0px) rotate(0deg);
	}

    100% {
		opacity: 0;
		-moz-transform: translateX(100%) rotate(120deg);
	}
}

@-o-keyframes rollOut {
    0% {
		opacity: 1;
		-o-transform: translateX(0px) rotate(0deg);
	}

    100% {
		opacity: 0;
		-o-transform: translateX(100%) rotate(120deg);
	}
}

@keyframes rollOut {
    0% {
		opacity: 1;
		transform: translateX(0px) rotate(0deg);
	}

    100% {
		opacity: 0;
		transform: translateX(100%) rotate(120deg);
	}
}

.rollOut {
	-webkit-animation-name: rollOut;
	-moz-animation-name: rollOut;
	-o-animation-name: rollOut;
	animation-name: rollOut;
}


File: /css\awesome-bootstrap-checkbox.css
.checkbox {
  padding-left: 20px;
}
.checkbox label {
  display: inline-block;
  vertical-align: middle;
  position: relative;
  padding-left: 5px;
}
.checkbox label::before {
  content: "";
  display: inline-block;
  position: absolute;
  width: 17px;
  height: 17px;
  left: 0;
  margin-left: -20px;
  border: 1px solid #cccccc;
  border-radius: 3px;
  background-color: #fff;
  -webkit-transition: border 0.15s ease-in-out, color 0.15s ease-in-out;
  -o-transition: border 0.15s ease-in-out, color 0.15s ease-in-out;
  transition: border 0.15s ease-in-out, color 0.15s ease-in-out;
}
.checkbox label::after {
  display: inline-block;
  position: absolute;
  width: 16px;
  height: 16px;
  left: 0;
  top: 0;
  margin-left: -20px;
  padding-left: 3px;
  padding-top: 1px;
  font-size: 11px;
  color: #555555;
}
.checkbox input[type="checkbox"],
.checkbox input[type="radio"] {
  opacity: 0;
  z-index: 1;
}
.checkbox input[type="checkbox"]:focus + label::before,
.checkbox input[type="radio"]:focus + label::before {
  outline: thin dotted;
  outline: 5px auto -webkit-focus-ring-color;
  outline-offset: -2px;
}
.checkbox input[type="checkbox"]:checked + label::after,
.checkbox input[type="radio"]:checked + label::after {
  font-family: "FontAwesome";
  content: "\f00c";
}
.checkbox input[type="checkbox"]:indeterminate + label::after,
.checkbox input[type="radio"]:indeterminate + label::after {
  display: block;
  content: "";
  width: 10px;
  height: 3px;
  background-color: #555555;
  border-radius: 2px;
  margin-left: -16.5px;
  margin-top: 7px;
}
.checkbox input[type="checkbox"]:disabled + label,
.checkbox input[type="radio"]:disabled + label {
  opacity: 0.65;
}
.checkbox input[type="checkbox"]:disabled + label::before,
.checkbox input[type="radio"]:disabled + label::before {
  background-color: #eeeeee;
  cursor: not-allowed;
}
.checkbox.checkbox-circle label::before {
  border-radius: 50%;
}
.checkbox.checkbox-inline {
  margin-top: 0;
}

.checkbox-primary input[type="checkbox"]:checked + label::before,
.checkbox-primary input[type="radio"]:checked + label::before {
  background-color: #337ab7;
  border-color: #337ab7;
}
.checkbox-primary input[type="checkbox"]:checked + label::after,
.checkbox-primary input[type="radio"]:checked + label::after {
  color: #fff;
}

.checkbox-danger input[type="checkbox"]:checked + label::before,
.checkbox-danger input[type="radio"]:checked + label::before {
  background-color: #d9534f;
  border-color: #d9534f;
}
.checkbox-danger input[type="checkbox"]:checked + label::after,
.checkbox-danger input[type="radio"]:checked + label::after {
  color: #fff;
}

.checkbox-info input[type="checkbox"]:checked + label::before,
.checkbox-info input[type="radio"]:checked + label::before {
  background-color: #5bc0de;
  border-color: #5bc0de;
}
.checkbox-info input[type="checkbox"]:checked + label::after,
.checkbox-info input[type="radio"]:checked + label::after {
  color: #fff;
}

.checkbox-warning input[type="checkbox"]:checked + label::before,
.checkbox-warning input[type="radio"]:checked + label::before {
  background-color: #f0ad4e;
  border-color: #f0ad4e;
}
.checkbox-warning input[type="checkbox"]:checked + label::after,
.checkbox-warning input[type="radio"]:checked + label::after {
  color: #fff;
}

.checkbox-success input[type="checkbox"]:checked + label::before,
.checkbox-success input[type="radio"]:checked + label::before {
  background-color: #5cb85c;
  border-color: #5cb85c;
}
.checkbox-success input[type="checkbox"]:checked + label::after,
.checkbox-success input[type="radio"]:checked + label::after {
  color: #fff;
}

.checkbox-primary input[type="checkbox"]:indeterminate + label::before,
.checkbox-primary input[type="radio"]:indeterminate + label::before {
  background-color: #337ab7;
  border-color: #337ab7;
}

.checkbox-primary input[type="checkbox"]:indeterminate + label::after,
.checkbox-primary input[type="radio"]:indeterminate + label::after {
  background-color: #fff;
}

.checkbox-danger input[type="checkbox"]:indeterminate + label::before,
.checkbox-danger input[type="radio"]:indeterminate + label::before {
  background-color: #d9534f;
  border-color: #d9534f;
}

.checkbox-danger input[type="checkbox"]:indeterminate + label::after,
.checkbox-danger input[type="radio"]:indeterminate + label::after {
  background-color: #fff;
}

.checkbox-info input[type="checkbox"]:indeterminate + label::before,
.checkbox-info input[type="radio"]:indeterminate + label::before {
  background-color: #5bc0de;
  border-color: #5bc0de;
}

.checkbox-info input[type="checkbox"]:indeterminate + label::after,
.checkbox-info input[type="radio"]:indeterminate + label::after {
  background-color: #fff;
}

.checkbox-warning input[type="checkbox"]:indeterminate + label::before,
.checkbox-warning input[type="radio"]:indeterminate + label::before {
  background-color: #f0ad4e;
  border-color: #f0ad4e;
}

.checkbox-warning input[type="checkbox"]:indeterminate + label::after,
.checkbox-warning input[type="radio"]:indeterminate + label::after {
  background-color: #fff;
}

.checkbox-success input[type="checkbox"]:indeterminate + label::before,
.checkbox-success input[type="radio"]:indeterminate + label::before {
  background-color: #5cb85c;
  border-color: #5cb85c;
}

.checkbox-success input[type="checkbox"]:indeterminate + label::after,
.checkbox-success input[type="radio"]:indeterminate + label::after {
  background-color: #fff;
}

.radio {
  padding-left: 20px;
}
.radio label {
  display: inline-block;
  vertical-align: middle;
  position: relative;
  padding-left: 5px;
}
.radio label::before {
  content: "";
  display: inline-block;
  position: absolute;
  width: 17px;
  height: 17px;
  left: 0;
  margin-left: -20px;
  border: 1px solid #cccccc;
  border-radius: 50%;
  background-color: #fff;
  -webkit-transition: border 0.15s ease-in-out;
  -o-transition: border 0.15s ease-in-out;
  transition: border 0.15s ease-in-out;
}
.radio label::after {
  display: inline-block;
  position: absolute;
  content: " ";
  width: 11px;
  height: 11px;
  left: 3px;
  top: 3px;
  margin-left: -20px;
  border-radius: 50%;
  background-color: #555555;
  -webkit-transform: scale(0, 0);
  -ms-transform: scale(0, 0);
  -o-transform: scale(0, 0);
  transform: scale(0, 0);
  -webkit-transition: -webkit-transform 0.1s cubic-bezier(0.8, -0.33, 0.2, 1.33);
  -moz-transition: -moz-transform 0.1s cubic-bezier(0.8, -0.33, 0.2, 1.33);
  -o-transition: -o-transform 0.1s cubic-bezier(0.8, -0.33, 0.2, 1.33);
  transition: transform 0.1s cubic-bezier(0.8, -0.33, 0.2, 1.33);
}
.radio input[type="radio"] {
  opacity: 0;
  z-index: 1;
}
.radio input[type="radio"]:focus + label::before {
  outline: thin dotted;
  outline: 5px auto -webkit-focus-ring-color;
  outline-offset: -2px;
}
.radio input[type="radio"]:checked + label::after {
  -webkit-transform: scale(1, 1);
  -ms-transform: scale(1, 1);
  -o-transform: scale(1, 1);
  transform: scale(1, 1);
}
.radio input[type="radio"]:disabled + label {
  opacity: 0.65;
}
.radio input[type="radio"]:disabled + label::before {
  cursor: not-allowed;
}
.radio.radio-inline {
  margin-top: 0;
}

.radio-primary input[type="radio"] + label::after {
  background-color: #337ab7;
}
.radio-primary input[type="radio"]:checked + label::before {
  border-color: #337ab7;
}
.radio-primary input[type="radio"]:checked + label::after {
  background-color: #337ab7;
}

.radio-danger input[type="radio"] + label::after {
  background-color: #d9534f;
}
.radio-danger input[type="radio"]:checked + label::before {
  border-color: #d9534f;
}
.radio-danger input[type="radio"]:checked + label::after {
  background-color: #d9534f;
}

.radio-info input[type="radio"] + label::after {
  background-color: #5bc0de;
}
.radio-info input[type="radio"]:checked + label::before {
  border-color: #5bc0de;
}
.radio-info input[type="radio"]:checked + label::after {
  background-color: #5bc0de;
}

.radio-warning input[type="radio"] + label::after {
  background-color: #f0ad4e;
}
.radio-warning input[type="radio"]:checked + label::before {
  border-color: #f0ad4e;
}
.radio-warning input[type="radio"]:checked + label::after {
  background-color: #f0ad4e;
}

.radio-success input[type="radio"] + label::after {
  background-color: #5cb85c;
}
.radio-success input[type="radio"]:checked + label::before {
  border-color: #5cb85c;
}
.radio-success input[type="radio"]:checked + label::after {
  background-color: #5cb85c;
}

input[type="checkbox"].styled:checked + label:after,
input[type="radio"].styled:checked + label:after {
  font-family: 'FontAwesome';
  content: "\f00c";
}
input[type="checkbox"] .styled:checked + label::before,
input[type="radio"] .styled:checked + label::before {
  color: #fff;
}
input[type="checkbox"] .styled:checked + label::after,
input[type="radio"] .styled:checked + label::after {
  color: #fff;
}

File: /css\customModal.css
.custom-modal {
    display: none;
    position: fixed;
    z-index: 1053;
    left: 0;
    top: 0;
    width: 100%;
    height: 100%;
    overflow: auto;
    background-color: rgb(0,0,0);
    background-color: rgba(0,0,0,0.5);
}

.cmodal-content {
    position: relative;
    margin: 10% auto;
    border: 1px solid #888;
    border-radius: 10px;
    width: 40%;
    box-shadow: 0 4px 8px 0 rgba(0,0,0,0.2),0 6px 20px 0 rgba(0,0,0,0.19);
    -webkit-animation: cmodalmove .4s ;
    -o-animation: cmodalmove .4s;
    -moz-animation: cmodalmove .4s;
    animation: cmodalmove .4s;
}

@-webkit-keyframes cmodalmove {
    0%   {top:-400px;}
    100% {top:0px;}
}

@keyframes cmodalmove {
    0%   {top:-400px;}
    100% {top:0px;}
}

.cmodal-header {
    display: block;
    height: fit-content;
    width: 100%;
    border-radius: 10px 10px 0px 0px;
    background-color: rgb(0,0,0);
    background-color: rgba(0,0,0,0.25);
    color: white;
    padding: -30px;
}

.cmodal-title {
    font-size: 1.08em;
    display: inline;
    padding: 10px;
    font-weight: 500;
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
}

.cmodal-close:hover {
    background-color: orangered;
}

.cmodal-close {
    float: right;
    height: 100%;
    border-color: rgba(0,0,0,0);
    border-radius: 5px 5px 0px 5px;
    text-align: center;
    font-weight: bold;
    box-shadow: none;
    background: lightgrey;
    cursor: pointer;
}

.cmodal-body {
    display: inline;
}

.cmodal-message {
    display: block;
    padding: 20px 10px;
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
}

.cmodal-icon {
    float: right;
}

.cmodal-footer {
    display: block;
    z-index: -1;
    border-radius: 0px 0px 10px 10px;
    background-color: rgb(255,255,255);
    background-color: rgba(255,255,255,.4);
    text-align: right;
}

.cmodal-button {
    display: inline;
    margin: 3px 3px;
    padding: 3px;
    color: white;
    min-width: 70px;
    cursor: pointer;
    border-radius: 6px;
    border-color: black;
    border-color: rgba(0,0,0,0);
    -webkit-transition: all .2s; 
    -moz-transition: all .2s; 
    transition: all .2s;
    text-decoration: none;
    text-align: center;
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; 
}

.cmodal-button:hover {
    opacity: .95;
    box-shadow: 2px 2px 1px black;
}

.cmodal-ok {
    background: green;
    background:  linear-gradient( green, mediumseagreen);
}

.cmodal-cancel { 
    background: red;
    background: linear-gradient( red, indianred);
}

.cmodal-generic { 
    background: purple;
    background: linear-gradient( purple, mediumpurple);
}

.cmodal-blue {
    background-color: skyblue;
    background: linear-gradient( dodgerblue, deepskyblue);
}

.error {
    background: red;
	background: -moz-linear-gradient(red, indianred);
	background: -webkit-linear-gradient(red, indianred);
	background: -o-linear-gradient(red, indianred);
    background: linear-gradient(red, indianred);
}

.information {
    background: dodgerblue;
	background: -moz-linear-gradient(dodgerblue, lightblue);
	background: -webkit-linear-gradient(dodgerblue, lightblue);
	background: -o-linear-gradient(dodgerblue, lightblue);
    background: linear-gradient(dodgerblue, lightblue);
}

.success {
    background: green;
	background: -moz-linear-gradient(green, mediumseagreen);
	background: -webkit-linear-gradient(green, mediumseagreen);
	background: -o-linear-gradient(green, mediumseagreen);
    background: linear-gradient(green, mediumseagreen);
}

.warning {
    background: darkorange;
	background: -moz-linear-gradient(orangered, darkorange);
	background: -webkit-linear-gradient(orangered, darkorange);
	background: -o-linear-gradient(orangered, darkorange);
    background: linear-gradient(orangered, darkorange);
}

File: /css\print.css
.navbar{
display:none;
}
.modal{
	display:none;
}
.action{
	display:none;
}
h1{
	text-transform:uppercase;
}
.title, img {
	display:visible;
}
th{
	text-align:left;
}
td{
	text-align:left;
	border-top:1px solid;
	padding:2px;
}
.btn{
	display:none;
}
.alert{
	display:none;
}
body{
	font-family:arial;
	font-size:13px;
}
.no_print{
	display:none;
}
.printable{
display:visible;
}
span{
text-transform:uppercase;
}
/*
.name span{
display:block;
}
.name span strong{
margin-left:10px;
}
.add_grade{
display:none;
}
.act{
display:none;
}
.logout{
display:none;
}
#add{
display:none;
}
.dataTables_filter{
display:none;
}
.nav{
display:none;
}
.dataTables_paginate {
display:none;
}
#example_length{
display:none;
}
.dataTables_info{
	display:none;
}
*/

File: /css\style.css
@import url(http://fonts.googleapis.com/css?family=Open+Sans:400,300,700,600);
@import url(http://fonts.googleapis.com/css?family=Oswald:400,300);

body {
    background: url(../images/bg.jpg);
    background-attachment: fixed;
    background-size: cover;
    background-position: 50% 50%;
    font-family: 'Open Sans', sans-serif;
}

a,
a:hover,
a:focus,
a:active,
a.active {
    outline: 0;
}

ul,ol {
    margin: 0;
    padding: 0;
}

li {
    list-style: none;
}

a {
    color: #FF432E;
    text-decoration: none;
}

a:hover {
    text-decoration: none;
}

p {
    font-family: 'Open Sans', sans-serif;
    font-size: 13px;
    line-height: 21px;
}

/**** Start Logo Section ****/

#logo-section {
    
}

.logo h1 {
    font-family: 'Lobster', cursive;
    color: #fff;
    font-size: 60px;
}

.logo span {
    color: #999;
}



/**** Start Background Color ****/

.blue {
    background: #28ABE3;
}

.green {
    background: #72bf48;
}

.red {
    background: #FF432E;
}

.olive {
    background: #808000;
}

.purple {
    background: #800080;
}
.fuchsia {
    background: #FF00FF;
}
.navy {
    background: #000080;
}
.bisque {
    background: #FFE4C4;
}
.gold {
    background: #FFD700;
}
.skyblue {
    background: #87CEEB;
}
.lavender {
    background: #E6E6FA;
}
.coral {
    background: #FB7F50; /* wrong code for color */
}


/**** Start Main Body Section ****/
.mainbody-section {
    padding-top: 50px;
    padding-bottom: 30px;
}

.menu-item {
    color: #fff;
    padding-top: 20px;
    padding-bottom: 20px;
    margin-bottom: 30px;
	-webkit-transition: all 0.3s;
	transition: all 0.3s;
	
}

.menu-item a {
    color: #fff;
    display: block;
	-webkit-transition: all 0.3s;
	transition: all 0.3s;
}

.menu-item a p {
    font-family: 'Oswald', sans-serif;
    font-weight: 300;
    font-size: 20px;
}

.menu-item a i {
    font-size: 50px;
    padding-bottom: 20px;
}

.menu-item:hover a {
    text-decoration: none;
    //color: #333;
	animation: wobble;
	-webkit-animation: wobble;
	animation-duration: 1000ms;
	-webkit-animation-duration: 1000ms;
}

@media only screen 
and (min-width : 600px) 
and (max-width : 991px) {
    
    .menu-item {
        display: inline-block;
        width: 32.8%;
    }
    
    .menu-item.responsive {
        width: 49.5%;
        float: left;
        margin-right: 3px;
    }
    
    .menu-item.responsive-2 {
        width: 49.5%;
        float: right;
    }
    
}

@media only screen 
and (min-width : 992px) 
and (max-width : 1199px) {
    
    .menu-item {
        padding-top: 15px;
        padding-bottom: 15px;
    }
    
    .menu-item a i {
        font-size: 32px;
    }
    
    .menu-item a p {
        font-size: 16px;
    }
    
}

/**** Start Modal Section ****/

.modal-content {
	overflow:visible !important;
}
.child-modal .modal-content {
	padding: 50px 0 !important;
	margin-top: 120px !important;
	margin-right: 20px !important;
	margin-left: 20px !important;
	margin-bottom: 80px !important;
	min-height: auto !important;
    border: 2 !important;
    border-radius: 6 !important;
    background-clip: border-box;
    -webkit-box-shadow: none !important;
    -moz-box-shadow: none !important;
    box-shadow: 10px 10px 5px 3px #888888 !important;
    font-weight: 200;
	color: #666 !important;
    font-family: 'Oswald', sans-serif;
    text-transform: none;
}

.modal-footer {
	padding: 1px !important;
}	

table#table-01 {
    width:100%;
	border-radius: 10 !important;
	border-spacing: 5px !important;
}
table, th, td {
    border: 1px solid black;
    border-collapse: collapse;
	border-spacing: 5px !important;
}
th, td {
    padding: 5px;
    text-align: left;
}
table#table-01 tr:nth-child(even) {
    background-color: #eee;
}
table#table-01 tr:nth-child(odd) {
   background-color:#fff;
}
table#table-01 th {
    background-color: black;
    color: white;
}
.card-columns {

 @include media-breakpoint-only(lg) {
    column-count: 4;
  }
  @include media-breakpoint-only(xl) {
    column-count: 5;
  }
 @include media-breakpoint-only(sm) {
    column-count: 3;
 }
	@include media-breakpoint-only(xs) {
    column-count: 3;	
}
}
img.center {
    display: block;
    margin: 0 auto;
}
.center-element {
width: 100%;
margin: 0px auto 0px auto;
}
/*
@media print {
  *,
  *:before,enter code here
  *:after {
    color: #000 !important;
    text-shadow: none !important;
    background: transparent !important;
    -webkit-box-shadow: none !important;
            box-shadow: none !important;
  }
  a,
  a:visited {
    text-decoration: underline;
  }
  a[href]:after {
    content: " (" attr(href) ")";
  }
  abbr[title]:after {
    content: " (" attr(title) ")";
  }
  a[href^="#"]:after,
  a[href^="javascript:"]:after {
    content: "";
  }
  pre,
  blockquote {
    border: 1px solid #999;

    page-break-inside: avoid;
  }
  thead {
    display: table-header-group;
  }
  tr,
  img {
    page-break-inside: avoid;
  }
  img {
    max-width: 100% !important;
  }
  p,
  h2,
  h3 {
    orphans: 3;
    widows: 3;
  }
  h2,
  h3 {
    page-break-after: avoid;
  }
  select {
    background: #fff !important;
  }
  .navbar {
    display: none;
  }
  .btn > .caret,
  .dropup > .btn > .caret {
    border-top-color: #000 !important;
  }
  .label {
    border: 1px solid #000;
  }
  .table {
    border-collapse: collapse !important;
  }
  .table td,
  .table th {
    background-color: #fff !important;
  }
  .table-bordered th,
  .table-bordered td {
    border: 1px solid #ddd !important;
  }
}
*/

File: /database.php
<?php
$stmt = $DB_con->prepare("SET SQL_MODE = 'NO_AUTO_VALUE_ON_ZERO'");
$stmt->execute(array());

$stmt = $DB_con->prepare("SET time_zone = '+05:30'");
$stmt->execute(array());

$stmt = $DB_con->prepare("CREATE TABLE IF NOT EXISTS `hotspot_users` (
  `user_id` int(11) NOT NULL,
  `email` varchar(200) NOT NULL,
  `date_added` date NOT NULL,
  `firstname` varchar(30) NOT NULL,
  `lastname` varchar(30) NOT NULL,
  `password` varchar(60) NOT NULL,
  `created_at` datetime NOT NULL,
  `username` varchar(30) NOT NULL,
  `user_level` int(11) NOT NULL DEFAULT '3',
  `user_group` int(1) NOT NULL,
  `image_path` varchar(50) NOT NULL,
  `thumb_path` varchar(50) NOT NULL,
  `status` varchar(20) NOT NULL
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8");
$stmt->execute(array());

$stmt = $DB_con->prepare("ALTER TABLE `hotspot_users`
  ADD PRIMARY KEY (`user_id`),
  ADD KEY `username` (`username`)");
$stmt->execute(array());

$stmt = $DB_con->prepare("ALTER TABLE `hotspot_users`
  MODIFY `user_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=1");
$stmt->execute(array());

$stmt = $DB_con->prepare("CREATE TABLE IF NOT EXISTS `hotspot_vouchers` (
  `id` int(11) NOT NULL,
  `created_on` datetime DEFAULT NULL,
  `created_by` varchar(30) DEFAULT NULL,
  `creator` int(3) DEFAULT NULL,
  `user_name` varchar(30) DEFAULT NULL,
  `password` varchar(30) DEFAULT NULL,
  `printed_times` int(3) DEFAULT NULL,
  `printed_last` varchar(30) DEFAULT NULL,
  `status` varchar(10) DEFAULT NULL,
  `group_of` int(4) DEFAULT NULL,
  `booking_id` int(11) DEFAULT NULL,
  `limit_uptime` varchar(30) DEFAULT NULL,
  `limit_bytes` varchar(30) DEFAULT NULL,
  `profile` varchar(30) DEFAULT NULL,
  `uid` VARCHAR(30) NOT NULL
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8");
$stmt->execute(array());

$stmt = $DB_con->prepare("ALTER TABLE `hotspot_vouchers`
  ADD PRIMARY KEY (`id`)");
$stmt->execute(array());

$stmt = $DB_con->prepare("ALTER TABLE `hotspot_vouchers`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT");
$stmt->execute(array());
?>

File: /dbconfig.php
<?php
	$DB_host = "localhost";
	$DB_user = "root";
	$DB_pass = "root123";
	$DB_name = "mikrotik";

	try
		{
			$DB_con = new PDO("mysql:host={$DB_host}",$DB_user,$DB_pass);
			$DB_con->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
			
			$dbname = "`".str_replace("`","``",$DB_name)."`";
			$DB_con->query("CREATE DATABASE IF NOT EXISTS $dbname");
			$DB_con->query("use $dbname");
		}
		catch(PDOException $e) {
			echo "Error: " . $e->getMessage();
	}
	
	/* Old Version, NOT creating DB if NOT Exist
	$DB_con = new PDO("mysql:host={$DB_host};dbname={$DB_name}",$DB_user,$DB_pass);
	$DB_con->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
	*/
?>

File: /db_backup_20_09_2016_14_11_47.sql
-- TABLE: hotspot_customers

CREATE TABLE `hotspot_customers` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `customer_id` varchar(30) NOT NULL,
  `company` varchar(64) NOT NULL,
  `address` varchar(128) NOT NULL,
  `telephone` varchar(30) NOT NULL,
  `mobile` varchar(30) NOT NULL,
  `email` varchar(30) NOT NULL,
  `state` varchar(30) NOT NULL,
  `country` varchar(30) NOT NULL,
  `validity` varchar(10) NOT NULL,
  `created_on` datetime DEFAULT NULL,
  `valid_till` datetime DEFAULT NULL,
  `pub_key` varchar(30) NOT NULL,
  `priv_key` varchar(30) NOT NULL,
  `hits` int(11) DEFAULT '0',
  `error_hit` int(11) DEFAULT '0',
  `comment` varchar(50) NOT NULL,
  `ip` varchar(15) NOT NULL,
  `mac_id` varchar(30) NOT NULL,
  `status` varchar(15) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;

INSERT INTO `hotspot_customers` (`id`, `customer_id`, `company`, `address`, `telephone`, `mobile`, `email`, `state`, `country`, `validity`, `created_on`, `valid_till`, `pub_key`, `priv_key`, `hits`, `error_hit`, `comment`, `ip`, `mac_id`, `status`) VALUES ('1', 'jaison123', 'Inspire Digital Solutions', 'Karippayil Building, NH 183, Kumily - 685 509', 'telephone', 'mobile', 'mail@zetone.com', 'Tamilnadu', 'Pakistan', '1 Month', '2016-09-16 00:00:00', '2016-10-20 00:00:00', 'J3NZY-L9NAW-52MY2-I5P9H-L2U3L', 'WKTQN-P359T-NP7EO-DXXY2-S3ZMD', '7', '4', '00-16-EA-7C-10-38', '', '00-16-EA-7C-10-38', 'Active');

INSERT INTO `hotspot_customers` (`id`, `customer_id`, `company`, `address`, `telephone`, `mobile`, `email`, `state`, `country`, `validity`, `created_on`, `valid_till`, `pub_key`, `priv_key`, `hits`, `error_hit`, `comment`, `ip`, `mac_id`, `status`) VALUES ('2', 'Jinu Devasia', 'Zetozone Technologies', 'Karippayil Building, NH 183, Kumily - 685 509', '9961144235', '9656224691', 'jinu@live.in', 'Kerala', 'India', 'Lifetime', '2016-09-20 00:00:00', '2019-06-16 00:00:00', 'JF94O-YBA7B-ZSHHF-KFABI-JUWP2', 'UUY5G-QZB7L-59HDW-SSE9L-TFIJF', '0', '0', '', '', '18:10:18', 'Deleted');



-- TABLE: hotspot_users

CREATE TABLE `hotspot_users` (
  `user_id` int(11) NOT NULL AUTO_INCREMENT,
  `email` varchar(200) NOT NULL,
  `date_added` date NOT NULL,
  `firstname` varchar(30) NOT NULL,
  `lastname` varchar(30) NOT NULL,
  `password` varchar(60) NOT NULL,
  `created_at` datetime NOT NULL,
  `username` varchar(30) NOT NULL,
  `user_level` int(11) NOT NULL DEFAULT '3',
  `user_group` int(1) NOT NULL,
  `image_path` varchar(50) NOT NULL,
  `thumb_path` varchar(50) NOT NULL,
  `status` varchar(20) NOT NULL,
  PRIMARY KEY (`user_id`),
  KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;

INSERT INTO `hotspot_users` (`user_id`, `email`, `date_added`, `firstname`, `lastname`, `password`, `created_at`, `username`, `user_level`, `user_group`, `image_path`, `thumb_path`, `status`) VALUES ('1', '', '2016-09-20', 'Administrator', '', 'd033e22ae348aeb5660fc2140aec35850c4da997', '2016-09-20 11:49:31', 'admin', '1', '1', '', '', 'Active');

INSERT INTO `hotspot_users` (`user_id`, `email`, `date_added`, `firstname`, `lastname`, `password`, `created_at`, `username`, `user_level`, `user_group`, `image_path`, `thumb_path`, `status`) VALUES ('3', '', '2016-09-20', 'Head User', 'Master', '5baa61e4c9b93f3f0682250b6cf8331b7ee68fd8', '0000-00-00 00:00:00', 'admin2', '3', '0', '', '', 'Active');


File: /header.php
<head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta name="description" content="Easy HotSpot - A Simple Hotspot user management utility by Team Zetozone">
    <meta name="author" content="Siby P Varkey, Team Zetozone">
<!--	
	<meta http-equiv='cache-control' content='no-cache'>
	<meta http-equiv='expires' content='0'>
	<meta http-equiv='pragma' content='no-cache'> -->

    <title>Easy HotSpot - A Simple Hotspot user management utility by Team Zetozone</title>

    
    <link href="css/bootstrap.min.css" rel="stylesheet" media="all"> 
	<!--  Bootstrap Core CSS 
	<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css" integrity="sha384-BVYiiSIFeK1dGmJRAkycuHAHRg32OmUcww7on3RYdg4Va+PmSTsz/K68vbdEjh4u" crossorigin="anonymous">
	-->
	
	<!-- Menu Items Animation CSS -->	
    <link href="css/animate.css" rel="stylesheet">

	<!-- Custom CSS -->
    <link href="css/style.css" rel="stylesheet"  media="screen" >
	<link href="css/awesome-bootstrap-checkbox.css" rel="stylesheet"  media="screen" >

    <!-- Custom Fonts -->
    <link href='http://fonts.googleapis.com/css?family=Lobster' rel='stylesheet' type='text/css'>

    <!-- Template js -->
	<link href="css/print.css" rel="stylesheet" type="text/css" media="print">
	<link href="css/customModal.css" rel="stylesheet" type="text/css" media="screen">
	
	<!--
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.6.3/css/font-awesome.min.css" rel="stylesheet">
	-->
	<link href="css/font-awesome.min.css" rel="stylesheet"> 
	<!--
	<script src="https://use.fontawesome.com/a45bcd3e7b.js"></script>  -->

	<script src="js/jquery-2.1.1.min.js"></script> 
	<!--<script src="https://ajax.googleapis.com/ajax/libs/jquery/2.2.4/jquery.min.js"></script> -->
	
	<!-- Latest compiled and minified JavaScript -->
	<script src="js/bootstrap.min.js"></script> 
	<!--<script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js" integrity="sha384-Tc5IQib027qvyjSMfHjOMaLkfuWVxZxUPnCJA7l2mCWNIpG9mGCD8wGNIcPD7Txa" crossorigin="anonymous"></script>
	-->	
	<!--<script src="printThis.js"></script> -->
	<script src="js/customModal.js"></script>
	<!--	<script src="js/gen_validatorv4.js" type="text/javascript"></script> -->

   <!--[if lt IE 9]>
        <script src="https://oss.maxcdn.com/libs/html5shiv/3.7.0/html5shiv.js"></script>
        <script src="https://oss.maxcdn.com/libs/respond.js/1.4.2/respond.min.js"></script>
    <![endif]-->
<script type="text/javascript">
	function log_out() {
		btns = [{text:"No",action:"cmodalClose",style:"cmodal-cancel"}, {text:"Yes",action:"logout.php",style:"cmodal-ok"}];
		cmodalOkCancel("Logout System?", "Logout Selected.. Do you want to Logout ?", "information", btns);	
	return false;
    }
</script> 
<script type="text/javascript">
//Guest User - Removal
function removeAjax(username){
   var ajaxRequest;  // The variable that makes Ajax possible!
   try{
   
      // Opera 8.0+, Firefox, Safari
      ajaxRequest = new XMLHttpRequest();
   }catch (e){
      
      // Internet Explorer Browsers
      try{
         ajaxRequest = new ActiveXObject("Msxml2.XMLHTTP");
      }catch (e) {
         
         try{
            ajaxRequest = new ActiveXObject("Microsoft.XMLHTTP");
         }catch (e){
         
            // Something went wrong
            alert("Your browser broke!");
            return false;
         }
      }
   }
   

   var queryString = "?username=" + username ;

   ajaxRequest.open("GET", "ajax_rem_user.php" + queryString, true);
   ajaxRequest.send(null);
   cmodal("User Removal Success", "User " + username + " Removed Successfully", "success");
}

</script>
	
<script>
//Guest User - Add Multiple Nos
function ajaxMultiple(){ 
   var no_of_users = document.getElementById('no_of_users').value;
   var pass_length = document.getElementById('pass_length').value;
   var user_prefix = document.getElementById('user_prefix').value;
   var limit_uptime = document.getElementById('limit_uptime').value;
   var limit_bytes = document.getElementById('limit_bytes').value;
   var profile = document.getElementById('profile').value;
   var same_pass = document.getElementById('same_pass').value;
   var Pass_type = document.getElementById('pass_type').value;

//   btns = [{text:"No",action:"cmodalClose",style:"cmodal-cancel"}, {text:"Yes",action:"test.php",style:"cmodal-ok"}];
   
   var ajaxRequest;  // The variable that makes Ajax possible!
   try{
   
      // Opera 8.0+, Firefox, Safari
      ajaxRequest = new XMLHttpRequest();
   }catch (e){
      
      // Internet Explorer Browsers
      try{
         ajaxRequest = new ActiveXObject("Msxml2.XMLHTTP");
      }catch (e) {
         
         try{
            ajaxRequest = new ActiveXObject("Microsoft.XMLHTTP");
         }catch (e){
         
            // Something went wrong
            alert("Your browser broke!");
            return false;
         }
      }
   }
   
      ajaxRequest.onreadystatechange = function(){
   
      if(ajaxRequest.readyState == 4){
			var ajaxResult = ajaxRequest.responseText;
			btns = [{text:"No",action:"cmodalClose",style:"cmodal-cancel"}, {text:"Yes",action:"test.php",style:"cmodal-ok"}];
			if (ajaxResult == 0) {
				cmodal("User Rights Issue",  "User Rights Problem/Empty Username.  Contact Admin for details", "error");
			}
			else {
				//btns = [{text:"No",action:"cmodalClose",style:"cmodal-cancel"}, {text:"Yes",action:"js:print_modal();",style:"cmodal-ok"}];
				//cmodalOkCancel("User Creation Success", ajaxResult + " Users Added Successfully. Print the Vouchers now ?", "success", btns);
				cmodal("Multiple Users Created", ajaxResult + " Users Accounts Added Successfully. Print the Vouchers from Voucher Printing Menu", "success");
			}
		}
	  }
  
   var queryString = "?no_of_users=" + no_of_users ;
   queryString +=  "&pass_length=" + pass_length + "&user_prefix=" + user_prefix ;
   queryString += "&limit_uptime=" + limit_uptime + "&profile=" + profile + "&same_pass=" + same_pass;
   queryString += "&limit_bytes=" + limit_bytes + "&pass_type=" + Pass_type;
   ajaxRequest.open("GET", "ajax_addusers.php" + queryString, true);
   ajaxRequest.send(null);
}
</script>
<script>
//Guest User - Add Multiple Nos
function ajaxVoucher1(){ 

   var ajaxRequest;  // The variable that makes Ajax possible!
   try{
   
      // Opera 8.0+, Firefox, Safari
      ajaxRequest = new XMLHttpRequest();
   }catch (e){
      
      // Internet Explorer Browsers
      try{
         ajaxRequest = new ActiveXObject("Msxml2.XMLHTTP");
      }catch (e) {
         
         try{
            ajaxRequest = new ActiveXObject("Microsoft.XMLHTTP");
         }catch (e){
         
            // Something went wrong
            alert("Your browser broke!");
            return false;
         }
      }
   }
   
   ajaxRequest.open("GET", "test.php", true);
   ajaxRequest.send(null);

  // cmodal("User Creation Success", no_of_users + " Users Added Successfully. You may Print the Vouchers now", "success");
}
</script>

<script>
//Guest User - Start of Creation of a Single Guest User; Ajax Call
function ajaxSingle() { //Guest User Add Single User
   var ajaxRequest;  // The variable that makes Ajax possible!
   try{
   
      // Opera 8.0+, Firefox, Safari
      ajaxRequest = new XMLHttpRequest();
   }catch (e){
      
      // Internet Explorer Browsers
      try{
         ajaxRequest = new ActiveXObject("Msxml2.XMLHTTP");
      }catch (e) {
         
         try{
            ajaxRequest = new ActiveXObject("Microsoft.XMLHTTP");
         }catch (e){
         
            // Something went wrong
            alert("Your browser broke!");
            return false;
         }
      }
   }

   ajaxRequest.onreadystatechange = function(){
   
      if(ajaxRequest.readyState == 4){
         var ajaxDisplay = document.getElementById('single');
         ajaxDisplay.innerHTML = ajaxRequest.responseText;
      }
   }
   
   var username = document.getElementById('uname').value;
   var password = document.getElementById('psw').value;
   var profile = document.getElementById('sprofile').value;
   var limit_uptime = document.getElementById('slimit_uptime').value;
   var limit_bytes = document.getElementById('slimit_bytes').value;
 
   var queryString = "?name=" + username ;

   queryString +=  "&psd=" + password + "&profile=" + profile + "&limit_uptime=" + limit_uptime + "&limit_bytes=" + limit_bytes;
   ajaxRequest.open("GET", "ajax_adduser.php" + queryString, true);
   ajaxRequest.send(null);

 // cmodal("User Creation Success", username + "  Added Successfully. You may Print the Vouchers now", "success");
}
// End of Creation of a Single Guest User; Ajax Call
</script> 
<script>
//Guest User - Start of Removing All Un-initiated Guest User Accounts
function ajaxUninitiated() { //Guest User
   var ajaxRequest;  // The variable that makes Ajax possible!
   try{
   
      // Opera 8.0+, Firefox, Safari
      ajaxRequest = new XMLHttpRequest();
   }catch (e){
      
      // Internet Explorer Browsers
      try{
         ajaxRequest = new ActiveXObject("Msxml2.XMLHTTP");
      }catch (e) {
         
         try{
            ajaxRequest = new ActiveXObject("Microsoft.XMLHTTP");
         }catch (e){
         
            // Something went wrong
            alert("Your browser broke!");
            return false;
         }
      }
   }
   
   ajaxRequest.open("GET", "ajax_uninitiated.php", true);
   ajaxRequest.send(null);

  cmodal("User Removal Success", "Removed all Un-Initiated Guest User Accounts from the Registry Successfully.", "success");
}
// End of Removing All Un-initiated Guest User Accounts
</script>

<script>
//Guest User - Start of Removing All Expired Guest User Accounts
function ajaxExpired() {
   var ajaxRequest;  // The variable that makes Ajax possible!
   try{
   
      // Opera 8.0+, Firefox, Safari
      ajaxRequest = new XMLHttpRequest();
   }catch (e){
      
      // Internet Explorer Browsers
      try{
         ajaxRequest = new ActiveXObject("Msxml2.XMLHTTP");
      }catch (e) {
         
         try{
            ajaxRequest = new ActiveXObject("Microsoft.XMLHTTP");
         }catch (e){
         
            // Something went wrong
            alert("Your browser broke!");
            return false;
         }
      }
   }
   
   ajaxRequest.open("GET", "ajax_expired.php", true);
   ajaxRequest.send(null);

   cmodal("User Removal Success", "Removed all Validity Expired Guest User Accounts from the Registry Successfully.", "success");
}
// End of Removing All Expired Guest User Accounts
</script> 
<script>
//System User - Password reset option for System Users, Calling From Menu option SYSTEM USERS
function resetpass(oForm){ 
	user_id = oForm.elements["user_id"].value;
  
   var ajaxRequest;  // The variable that makes Ajax possible!
   try{
   
      // Opera 8.0+, Firefox, Safari
      ajaxRequest = new XMLHttpRequest();
   }catch (e){
      
      // Internet Explorer Browsers
      try{
         ajaxRequest = new ActiveXObject("Msxml2.XMLHTTP");
      }catch (e) {
         
         try{
            ajaxRequest = new ActiveXObject("Microsoft.XMLHTTP");
         }catch (e){
         
            // Something went wrong
            alert("Your browser broke!");
            return false;
         }
      }
   }
      ajaxRequest.onreadystatechange = function(){
   
      if(ajaxRequest.readyState == 4){
         var ajaxResult = ajaxRequest.responseText;
        
		if (ajaxResult == 0) {
			cmodal("User Rights Issue",  "User Rights Problem.  Contact Admin for details", "error"); }
		else if (ajaxResult == 1) {
			cmodal("NOT EXIST..",  "No such User Exist,  Please re-check ..!", "warning"); }
		 else if (ajaxResult == 2) {
			cmodal("User Password Reset Success", "System User Password Reset Successfully", "success"); }
	  }

   }
 
   var queryString = "?user_id=" + user_id ;

   ajaxRequest.open("GET", "ajax_reset_pass.php" + queryString, true);
   ajaxRequest.send(null);
   
}
</script>

<script>
//System User - Start of Adding a New System User;
function addsysuser(oForm) { 
	//$('#system-user').modal('hide');

	var username = oForm.elements["username"].value;
	var firstname = oForm.elements["firstname"].value;
	var lastname = oForm.elements["lastname"].value;
	var user_level = oForm.elements["user_level"].value;
	var status = oForm.elements["status"].value;
	
   var ajaxRequest;  // The variable that makes Ajax possible!
   try{
   
      // Opera 8.0+, Firefox, Safari
      ajaxRequest = new XMLHttpRequest();
   }catch (e){
      
      // Internet Explorer Browsers
      try{
         ajaxRequest = new ActiveXObject("Msxml2.XMLHTTP");
      }catch (e) {
         
         try{
            ajaxRequest = new ActiveXObject("Microsoft.XMLHTTP");
         }catch (e){
         
            // Something went wrong
            alert("Your browser broke!");
            return false;
         }
      }
   }
   
      ajaxRequest.onreadystatechange = function(){
   
      if(ajaxRequest.readyState == 4){
         var ajaxResult = ajaxRequest.responseText;
        
		if (ajaxResult == 0) {
			cmodal("User Rights Issue",  "User Rights Problem/Empty Username.  Contact Admin for details", "error"); }
		else if (ajaxResult == 1) {
			cmodal("Already Exist..",  "Username Already Exist,  Please select another Name..!", "warning"); }
		 else if (ajaxResult == 2) {
			cmodal("Success..",  "New System User Created Successfully..!", "success"); }
	  }

   }

	var queryString = "?username=" + username ;
   
	queryString +=  "&username=" + username + "&firstname=" + firstname + "&lastname=" + lastname + "&user_level=" + user_level + "&status=" + status;
	ajaxRequest.open("GET", "ajax_add_sysuser.php" + queryString, true);
	ajaxRequest.send(null);
   
}
//System User - End of Adding a New System User;
</script>
<script>
//System User - Removes a System User
function deleteuser(oForm) { 
	user_id = oForm.elements["user_id"].value;
   var ajaxRequest;  // The variable that makes Ajax possible!
   try{
   
      // Opera 8.0+, Firefox, Safari
      ajaxRequest = new XMLHttpRequest();
   }catch (e){
      
      // Internet Explorer Browsers
      try{
         ajaxRequest = new ActiveXObject("Msxml2.XMLHTTP");
      }catch (e) {
         
         try{
            ajaxRequest = new ActiveXObject("Microsoft.XMLHTTP");
         }catch (e){
         
            // Something went wrong
            alert("Your browser broke!");
            return false;
         }
      }
   }
   
         ajaxRequest.onreadystatechange = function(){
   
      if(ajaxRequest.readyState == 4){
         var ajaxResult = ajaxRequest.responseText;
        
		if (ajaxResult == 0) {
			cmodal("User Rights Issue",  "User Rights Problem.  Contact Admin for details", "error"); }
		else if (ajaxResult == 1) {
			cmodal("Removed User..",  "User details removed Successfully..!", "success"); }
	  }

   }

   var queryString = "?user_id=" + user_id ;

   ajaxRequest.open("GET", "ajax_del_sysuser.php" + queryString, true);
   ajaxRequest.send(null);
}
</script>

<script>
//System User - Edit details of System User;
function edituser(oForm) { 
	var	user_id = oForm.elements["user_id"].value;
	var username = oForm.elements["username"].value;
	var firstname = oForm.elements["firstname"].value;
	var lastname = oForm.elements["lastname"].value;
	var user_level = oForm.elements["user_level"].value;
	var status = oForm.elements["status"].value;
	
   var ajaxRequest;  // The variable that makes Ajax possible!
   try{
   
      // Opera 8.0+, Firefox, Safari
      ajaxRequest = new XMLHttpRequest();
   }catch (e){
      
      // Internet Explorer Browsers
      try{
         ajaxRequest = new ActiveXObject("Msxml2.XMLHTTP");
      }catch (e) {
         
         try{
            ajaxRequest = new ActiveXObject("Microsoft.XMLHTTP");
         }catch (e){
         
            // Something went wrong
            alert("Your browser broke!");
            return false;
         }
      }
   }
   
     ajaxRequest.onreadystatechange = function(){
   
      if(ajaxRequest.readyState == 4){
         var ajaxResult = ajaxRequest.responseText;
        
		if (ajaxResult == 0) {
			cmodal("User Rights Issue",  "User Rights Problem/Empty Username.  Contact Admin for details", "error"); }
		else if (ajaxResult == 1) {
			cmodal("Already Exist..",  "Username Already Exist,  Please select another Name..!", "warning"); }
		 else if (ajaxResult == 2) {
			cmodal("Success..",  "Updated System User details Successfully..!", "success"); }
	  }

   }

   var queryString = "?user_id=" + user_id ;
   
   queryString +=  "&username=" + username + "&firstname=" + firstname + "&lastname=" + lastname + "&user_level=" + user_level + "&status=" + status;
   ajaxRequest.open("GET", "ajax_edit_sysuser.php" + queryString, true);
   ajaxRequest.send(null);
   
}
</script>
<script>
//System User - Changes Password for the current logged-in user
function changePass(oForm) { 
	//$('#system-user').modal('hide');
	var	np = oForm.elements["newpassword"].value;
	var	rp = oForm.elements["retypepassword"].value;
	
	var passReg = /^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$%^&*-]).{8,}$/;
	
	if (np != rp) {
		cmodal("Warning"," Passwords do not Match...", "warning");
		return false;
	}
	else if ((np == '') || (rp == '')) {
		cmodal("Warning"," Blank Password not allowed...", "warning");
		return false;
	} else if(!(np).match(passReg)){
		cmodal("Password Change Fail", "Your password is not Complex enough;, 1 Capital, 1 small, 1 Number, 1 symbol and 8 chars minimum", "error");
		return false;
	} else {
     
		var ajaxRequest;  // The variable that makes Ajax possible! change-password
		try{
   
		// Opera 8.0+, Firefox, Safari
			ajaxRequest = new XMLHttpRequest();
		}catch (e){
      
			// Internet Explorer Browsers
			try{
				ajaxRequest = new ActiveXObject("Msxml2.XMLHTTP");
			}catch (e) {
			
				try{
					ajaxRequest = new ActiveXObject("Microsoft.XMLHTTP");
				}catch (e){
			
					// Something went wrong
					alert("Your browser broke!");
					return false;
				}
			}
		}
		
		ajaxRequest.onreadystatechange = function(){
   
      if(ajaxRequest.readyState == 4){
         var ajaxResult = ajaxRequest.responseText;
        
		if (ajaxResult == 0) {
			cmodal("User Rights Issue",  "Authorisation Problem/Password Change Failed.  Contact Admin for details", "error"); }
		else if (ajaxResult == 1) {
			cmodal("Password Changed", "Your password has been changed Successfully", "success"); }
	  }

   }
  
		var queryString = "?np=" + np ;
		queryString +=  "&rp=" + rp;
		ajaxRequest.open("GET", "ajax_change_syspass.php" + queryString, true);
		ajaxRequest.send(null);
	}
	
}	
</script>

<script>
function genClicks(event) { // Called by all Input Elements to Set Focus to next TabItem when pressing the ENTER key.
    var key = event.keyCode;
	var cti = document.activeElement.tabIndex;
	if (key == 13) {
		event.preventDefault();
		$('[tabindex=' + (cti + 1) + ']').focus();
	}
}
</script>
<script>
function genClick(event) { // Called by all Input Elements to Set Focus to next TabItem when pressing the ENTER key.
	var cti = document.activeElement.tabIndex;
	$('[tabindex=' + (cti + 1) + ']').focus();
}
</script>
<script>
//Jquery Functions Start Here
$(document).ready(function() {

function print_modal() { 
	$('#voucher_print').modal('show');
};

$('#change-password').bind('keypress',function (event){
  if (event.keyCode === 13){
	event.preventDefault();
    $("#update_pass").trigger('click');
  }
});

$('#add_sysuser').bind('keypress',function (event){
  if (event.keyCode === 13){
	event.preventDefault();
    $("#add_user").trigger('click');
  }
});

//Activates the common User Modal for System users,
// which retrieves data related to that user and facilitiates editing, removal, reset pass etc in the modal
$('#getUserModal').on('show.bs.modal', function (event)   {
    var button = $(event.relatedTarget)
    var recipient = button.data('id')
    var modal = $(this)
    modal.find('.modal-title').text('System User # ' + recipient + "'s details.")
    $(function () 
          {
            $.ajax(
            {  
                type: 'GET',
                url: "ajax_get_sysuser.php?user_id=" + recipient,             
                data: 'recipient',
                dataType: "json",
                success: function(data) 
                {
                    
                    var firstName = data.firstname;       
                    var lastName = data.lastname;
                    var userName = data.username;
					var userId = data.user_id;       
                    var userLevel = data.user_level;
					var userStatus = data.status;
						 
					modal.find('.modal-body #firstname').val(firstName)
					modal.find('.modal-body #lastname').val(lastName)
					modal.find('.modal-body #username').val(userName) 
					modal.find('.modal-body #user_level').val(userLevel)
					modal.find('.modal-body #status').val(userStatus)
					modal.find('.modal-body #user_id').val(userId) 
                }
            })
 
        })
    } )

//Activates the common User Modal for System users,
// which retrieves data related to that user and facilitiates editing, removal, reset pass etc in the modal

$('#getProfileModal').on('show.bs.modal', function (event)   {
    var button = $(event.relatedTarget)
    var profile_name = button.data('id')
    var modal = $(this)
    modal.find('.modal-title').text('Hotspot User Profile ' + profile_name + "'s details.")
    $(function () 
          {
            $.ajax(
            {  
                type: 'GET',
                url: "ajax_get_profiles.php?profile_name=" + profile_name,             
                //data: profile_name,
                dataType: "json",
                success: function(data) 
                {
					//console.log(data);
                    var Name = data.name;  
					var Address_pool = data.address_pool;					
                    var Rate_limit = data.rate_limit;
					if (Rate_limit) {
						var Limits = Rate_limit.split("/");
						var Rx_rate_limit = Limits.slice(0,1);
						var Tx_rate_limit = Limits.slice(1,2);
					}	
                    var Session_timeout = data.session_timeout;
					var Shared_users = data.shared_users;       
                    var Mac_cookie_timeout = data.mac_cookie_timeout;
					var Keepalive_timeout = data.keepalive_timeout;
					
					var Validity = data.validity;
					var Grace_period = data.grace_period;
					var On_expiry = data.on_expiry;
					var Price = data.price;
					var Lock_user = data.lock_user;
					
					modal.find('.modal-body #profile_name').val(Name)
					modal.find('.modal-body #address_pool').val(Address_pool)
					modal.find('.modal-body #rx_rate_limit').val(Rx_rate_limit)
					modal.find('.modal-body #tx_rate_limit').val(Tx_rate_limit)
					modal.find('.modal-body #session_timeout').val(Session_timeout) 
					modal.find('.modal-body #shared_users').val(Shared_users)
					modal.find('.modal-body #mac_cookie_timeout').val(Mac_cookie_timeout)
					modal.find('.modal-body #keepalive_timeout').val(Keepalive_timeout)

					modal.find('.modal-body #validity').val(Validity)
					modal.find('.modal-body #grace_period').val(Grace_period)
					modal.find('.modal-body #on_expiry').val(On_expiry)					
					modal.find('.modal-body #price').val(Price)
					modal.find('.modal-body #lock_user').val(Lock_user)
                }
            })
        })
    } )    
    

} );
</script>
<script>

//Guest User Profile - Start of Adding a New User profile;
function addprofile(oForm) { 
	//$('#system-user').modal('hide');

	var Profile_name = oForm.elements["profile_name"].value;
	var Rx_rate_limit = oForm.elements["rx_rate_limit"].value;
	var Tx_rate_limit = oForm.elements["tx_rate_limit"].value;
	var Session_timeout = oForm.elements["session_timeout"].value;
	var Shared_users = oForm.elements["shared_users"].value;
	var Mac_cookie_timeout = oForm.elements["mac_cookie_timeout"].value;
	var Keepalive_timeout = oForm.elements["keepalive_timeout"].value;
	
	var Validity = oForm.elements["validity"].value;
	var Grace_period = oForm.elements["grace_period"].value;
	var On_expiry = oForm.elements["on_expiry"].value;
	var Price = oForm.elements["price"].value;
	var Lock_user = oForm.elements["lock_user"].value;
	
   var ajaxRequest;  // The variable that makes Ajax possible!
   try{
   
      // Opera 8.0+, Firefox, Safari
      ajaxRequest = new XMLHttpRequest();
   }catch (e){
      
      // Internet Explorer Browsers
      try{
         ajaxRequest = new ActiveXObject("Msxml2.XMLHTTP");
      }catch (e) {
         
         try{
            ajaxRequest = new ActiveXObject("Microsoft.XMLHTTP");
         }catch (e){
         
            // Something went wrong
            alert("Your browser broke!");
            return false;
         }
      }
   }
   
      ajaxRequest.onreadystatechange = function(){
   
      if(ajaxRequest.readyState == 4){
         var ajaxResult = ajaxRequest.responseText;
        //console.log ("Log = " + ajaxResult);
		
		if (ajaxResult == 0) {
			cmodal("User Rights Issue",  "User Rights Problem, Not Authorised to.  Contact Admin for details", "error"); }
		else if (ajaxResult == 1) {
			cmodal("Empty Values",  "Blank Profile Name Not Permitted,  Please Fill required Fields and Proceed..!", "warning"); }
		 else if (ajaxResult == 2) {
			cmodal("Completed..",  "New Hotspot User Profile Creation Attempt Completed..!", "success"); }
	  }

   }

	var queryString = "?profile_name=" + Profile_name ;
   
	queryString += "&session_timeout=" + Session_timeout;
	queryString +=  "&shared_users=" + Shared_users + "&mac_cookie_timeout=" + Mac_cookie_timeout + "&keepalive_timeout=" + Keepalive_timeout;
	queryString += "&rx_rate_limit=" + Rx_rate_limit + "&tx_rate_limit=" + Tx_rate_limit;
	queryString += "&validity=" + Validity + "&grace_period=" + Grace_period;
	queryString += "&on_expiry=" + On_expiry + "&price=" + Price + "&lock_user=" + Lock_user;
	ajaxRequest.open("GET", "ajax_add_profile.php" + queryString, true);
	ajaxRequest.send(null);
   
}
//Guest User Profile - End of Adding a New User profile;
</script>
<script>
//Guest User Profile - Start of Deleting a Guest User profile;
function deleteprofile(oForm) { 
	//$('#system-user').modal('hide');

	var Profile_name = oForm.elements["profile_name"].value;
	
   var ajaxRequest;  // The variable that makes Ajax possible!
   try{
   
      // Opera 8.0+, Firefox, Safari
      ajaxRequest = new XMLHttpRequest();
   }catch (e){
      
      // Internet Explorer Browsers
      try{
         ajaxRequest = new ActiveXObject("Msxml2.XMLHTTP");
      }catch (e) {
         
         try{
            ajaxRequest = new ActiveXObject("Microsoft.XMLHTTP");
         }catch (e){
         
            // Something went wrong
            alert("Your browser broke!");
            return false;
         }
      }
   }
   
      ajaxRequest.onreadystatechange = function(){
   
      if(ajaxRequest.readyState == 4){
         var ajaxResult = ajaxRequest.responseText;
        //console.log ("Log = " + ajaxResult);
		
		if (ajaxResult == 0) {
			cmodal("User Rights Issue",  "User Rights Problem, Not Authorised to.  Contact Admin for details", "error"); }
		else if (ajaxResult == 1) {
			cmodal("Empty Values",  "Blank Profile Name Not Permitted,  Please Select any proper Profile and try..!", "warning"); }
		 else if (ajaxResult == 2) {
			cmodal("Completed..",  "Hotspot User Profile Removal attempt Attempt Completed..!", "success"); }
	  }

   }

	var queryString = "?profile_name=" + Profile_name ;
   
	ajaxRequest.open("GET", "ajax_del_profile.php" + queryString, true);
	ajaxRequest.send(null);
   
}
//Guest User Profile - End of Deleting a Guest User profile;
</script>
<script>
//Guest User Profile - Start of Updating a User profile;
function editprofile(oForm) { 
	//$('#system-user').modal('hide');

	var Profile_name = oForm.elements["profile_name"].value;
	var Rx_rate_limit = oForm.elements["rx_rate_limit"].value;
	var Tx_rate_limit = oForm.elements["tx_rate_limit"].value;
	var Session_timeout = oForm.elements["session_timeout"].value;
	var Shared_users = oForm.elements["shared_users"].value;
	var Mac_cookie_timeout = oForm.elements["mac_cookie_timeout"].value;
	var Keepalive_timeout = oForm.elements["keepalive_timeout"].value;
	
	var Validity = oForm.elements["validity"].value;
	var Grace_period = oForm.elements["grace_period"].value;
	var On_expiry = oForm.elements["on_expiry"].value;
	var Price = oForm.elements["price"].value;
	var Lock_user = oForm.elements["lock_user"].value;
	
   var ajaxRequest;  // The variable that makes Ajax possible!
   try{
   
      // Opera 8.0+, Firefox, Safari
      ajaxRequest = new XMLHttpRequest();
   }catch (e){
      
      // Internet Explorer Browsers
      try{
         ajaxRequest = new ActiveXObject("Msxml2.XMLHTTP");
      }catch (e) {
         
         try{
            ajaxRequest = new ActiveXObject("Microsoft.XMLHTTP");
         }catch (e){
         
            // Something went wrong
            alert("Your browser broke!");
            return false;
         }
      }
   }
   
      ajaxRequest.onreadystatechange = function(){
   
      if(ajaxRequest.readyState == 4){
         var ajaxResult = ajaxRequest.responseText;
       // console.log ("Log = " + ajaxResult);
		
		if (ajaxResult == 0) {
			cmodal("User Rights Issue",  "User Rights Problem, Not Authorised to.  Contact Admin for details", "error"); }
		else if (ajaxResult == 1) {
			cmodal("Improper Values",  "Profile Name Not Proper,  Please Select Proper Profile and Proceed..!", "warning"); }
		 else if (ajaxResult == 2) {
			cmodal("Completed..",  "Updation of Hotspot User Profile Completed..!", "success"); }
	  }

   }

	var queryString = "?profile_name=" + Profile_name ;
   
	queryString += "&session_timeout=" + Session_timeout;
	queryString +=  "&shared_users=" + Shared_users + "&mac_cookie_timeout=" + Mac_cookie_timeout + "&keepalive_timeout=" + Keepalive_timeout;
	queryString += "&rx_rate_limit=" + Rx_rate_limit + "&tx_rate_limit=" + Tx_rate_limit;
	queryString += "&validity=" + Validity + "&grace_period=" + Grace_period;
	queryString += "&on_expiry=" + On_expiry + "&price=" + Price + "&lock_user=" + Lock_user;
	ajaxRequest.open("GET", "ajax_edit_profile.php" + queryString, true);
	ajaxRequest.send(null);
   
}
//Guest User Profile - End of Updating a User profile;
</script>
<script>
//Guest User Account - Start of Removing Selected User accounts
function removeSelected(oForm) { 
	var Removal1 = oForm.elements['removal_list[]'];
	var Removal_list = new Array();
	var queryString = "";
	var k = 0;
	//var queryString = "?removal_list[]=";
   for (var i = 0; i < Removal1.length; i++) {
    var aControl = Removal1[i].checked;
	var bControl = Removal1[i].value;
	if (aControl == true) {
		Removal_list.push(bControl);
		if (k == 0) { queryString += "?removal_list[]=" + bControl ; } else { queryString += "&removal_list[]=" + bControl; }
		k = k + 1;
	}	
	//alert("Success : " + aControl + ", : " + bControl);
   }
   //alert("Final List : " + Removal_list);
   
   
   var ajaxRequest;  // The variable that makes Ajax possible!
   try{
   
      // Opera 8.0+, Firefox, Safari
      ajaxRequest = new XMLHttpRequest();
   }catch (e){
      
      // Internet Explorer Browsers
      try{
         ajaxRequest = new ActiveXObject("Msxml2.XMLHTTP");
      }catch (e) {
         
         try{
            ajaxRequest = new ActiveXObject("Microsoft.XMLHTTP");
         }catch (e){
         
            // Something went wrong
            alert("Your browser broke!");
            return false;
         }
      }
   }
   
      ajaxRequest.onreadystatechange = function(){
   
      if(ajaxRequest.readyState == 4){
         var ajaxResult = ajaxRequest.responseText;
		
		if (ajaxResult == 0) {
			cmodal("User Rights Issue",  "User Rights Problem, Not Authorised....  Contact Admin for details", "error"); }
		else if (ajaxResult == -1) {
			cmodal("No Proper Selections",   "No Guest user accounts selected for removal", "warning"); }
		else {
			cmodal("Removal Completed..",  ajaxResult + " Guest user accounts removed successfully", "success"); }
	  }
   }
	//var queryString = "?removal_list[]=array(" + Removal_list + ")";
	ajaxRequest.open("GET", "ajax_rem_selected.php" + queryString, true);
	ajaxRequest.send(null);
   
}
</script>
</head>

File: /home.php
<body>
	<div class="container">
	<div class="no_print">
        <!-- Start Logo Section -->
        <section id="logo-section" class="text-center">
            <div class="container">
                <div class="row">
                    <div class="col-md-12">
                        <div class="logo text-center">
                            <h1>Easy HotSpot</h1>
                            <span style="color:#333333;font-size:20px;font-weight:bold">WiFi Hotspot User Management Utility</span>
							<span style="color:#888888;font-size:20px;font-weight:bold">By Team Zetozone, Ph:+91 9020 150 150</span>
                        </div>
                    </div>
                </div>
            </div>
        </section>
        <!-- End Logo Section -->
		
		<!-- Start Main Body Section -->
        <div class="mainbody-section text-center">
            <div class="container">
                <div class="row">
                    <div class="col-md-2">
                        <div class="menu-item blue">
                            <a href="#single-user" data-toggle="modal">
                                <i class="fa fa-child"></i>
                                <p>Add Single User</p>
                            </a>
                        </div>
						<div class="menu-item red">
                            <a href="#multi-user" data-toggle="modal">
                                <i class="fa fa-users"></i>
                                <p>Add Multiple Users</p>
                            </a>
                        </div>
                    </div>
                    <div class="col-md-2">
                        <div class="menu-item skyblue">
                            <a href="#active-users" data-toggle="modal">
                                <i class="fa fa-signal"></i>
                                <p>List Active Users</p>
                            </a>
                        </div>
                        <div class="menu-item purple">
                            <a href="#remove-selected" data-toggle="modal">
                                <i class="fa fa-ban"></i>
                                <p>Remove Selected Users</p>
                            </a>
                        </div>

                    </div>
                    <div class="col-md-2">
                        <div class="menu-item coral">
                            <a href="#server-log" data-toggle="modal">
                                <i class="fa fa-paw"></i>
                                <p>Server Log</p>
                            </a>
                        </div>
                        <div class="menu-item navy">
                            <a href="voucher.php">
                                <i class="fa fa-bars"></i>
                                <p>Voucher Printing</p>
                            </a>
                        </div>

                    </div>
					<div class="col-md-2">
                        <div class="menu-item fuchsia">
                            <a href="#remove-uninitiated" data-toggle="modal">
                                <i class="fa fa-gears"></i>
                                <p>Remove Un-Initiated</p>
                            </a>
                        </div>
                        <div class="menu-item gold">
                            <a href="#profiler" data-toggle="modal">
                                <i class="fa fa-user"></i>
                                <p>HotSpot User Profiles</p>
                            </a>
                        </div>
                    </div>
					<div class="col-md-2">
                        <div class="menu-item olive">
							<a href="#remove-expired" data-toggle="modal">
                                <i class="fa fa-bug"></i>
                                <p>Remove All Expired</p>
                            </a>
                        </div>					
                        <div class="menu-item purple">
                            <a href="#system-user" data-toggle="modal">
                                <i class="fa fa-user-md"></i>
                                <p>System Users</p>
                            </a>
                        </div>
					</div>	
					<div class="col-md-2">						
                        <div class="menu-item green">
                            <a href="#list-users" data-toggle="modal">
                                <i class="fa fa-ambulance"></i>
                                <p>List Inactive Users</p>
                            </a>
                        </div>						
                        <div class="menu-item blue">
							<a href="index.php" >
                                <i class="fa fa-refresh fa-spin fa-3x fa-fw"></i>
                                <p>Refresh</p>
                            </a>
                        </div>
                    </div>
                </div>
				<input type="button" style="background-color: #f0ff0a;" onclick="log_out()" value="<?php echo 'Logout ('.$_SESSION['username'].')'; ?>"/>
            </div>
        </div>
	</div>	
	
        <!-- End Main Body Section -->

		<!-- 1. End Single Guest User Creation Experiment Section -->
		<div class="child-modal modal fade" id="single-user" tabindex="-1" role="dialog" aria-hidden="true">
            <div class="modal-content">
                <div class="close-modal" data-dismiss="modal">
                    <div class="lr">
                        <div class="rl">
                        </div>
                    </div>
                </div>
                <div class="container">
                    <div class="no_print">
						<div class="row">
							<div class="col-sm-12 col-md-12 thumbnail" style="box-shadow: 10px 10px 5px #888888;">
								<div class="panel panel-primary">
									<div class="panel-heading"><h3 class="text-center">Single User Creation</h3></div>
									<div class="panel-body">
										<div class="form-horizontal">
											<div class="form-group form-group-sm">
												<div class="col-sm-4">
													<label class="col-sm-6 control-label" >User Name</label>
													<div class="col-sm-6">
														<input type="text" placeholder="Required Username *" name="uname" id="uname" required >
													</div>
												</div>
												<div class="col-sm-4">
													<label class="col-sm-6 control-label" >Password</label>
													<div class="col-sm-6">
														<input type="text" placeholder="required password *" name="psw" id="psw" required>
													</div>
												</div>
												<div class="col-sm-4">						
													<label class="col-sm-6 control-label" >Uptime Limit(wdhms format)</label>
													<div class="col-sm-6">
														<input type="text" placeholder="10m" title="eg.5h30m [w(Weeks) d(days) h(hours) m(minutes) s(seconds) format]" name="slimit_uptime" id="slimit_uptime" >
													<!--	<select class="myCombo" id="slimit_uptime" name="slimit_uptime">
															<option value="2d">2 Days</option>									
															<option value="1d">1 Day</option>
															<option value="2d">2 Days</option>
															<option value="3d">3 Days</option>
															<option value="4d">4 Days</option>
															<option value="5d">5 Days</option>
														</select> -->
													</div>
												</div>
											</div>	
											<div class="form-group form-group-sm">
												<div class="col-sm-4">						
													<label class="col-sm-6 control-label" for="slimit_bytes">Maximum Usage Limit(GB), 0 for NO Limit</label>
													<div class="col-sm-6">
														<input type="number" title="Maximum usable data in GB" name="slimit_bytes" id="slimit_bytes" min="0" value="0" required >
														<!--<select class="myCombo" id="slimit_bytes" name="slimit_bytes">
															<option value="0">NONE</option>									
															<option value="1">1 GB</option>
															<option value="5">5 GB</option>
															<option value="10">10 GB</option>
															<option value="20">20 GB</option>
															<option value="50">50 GB</option>
														</select> -->
													</div>
												</div>
												<div class="col-sm-4">						
													<label class="col-sm-6 control-label" >Bandwidth (Mbps) Profile</label>
													<div class="col-sm-6">
														<?php
														$util->setMenu('/ip hotspot user profile');
														echo '<select class="myCombo" id="sprofile" name="sprofile" required>';
														foreach ($util->getAll() as $item) {
															echo '<option>', $item->getProperty('name'), '</option>';
														}
														echo '</select>'; ?>
													</div>
												</div>
												<div class="col-sm-4">
													<div class="col-sm-3 col-sm-offset-3">
														<div class="pull-right">
															<button name="issuing" id="issuing" onClick="ajaxSingle()" class="btn btn-success"><i class="icon-save icon-large"></i></a>&nbsp;Issue</button>
														</div>
													</div>
													<div class="col-sm-3">
														<div class="pull-left">
															<button  data-dismiss="modal" class="btn btn-warning" ><i class="icon-save icon-large"></i></a>&nbsp;BACK</button>
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
					<div id="single"></div>
				</div>
			</div>
		</div>	
        <!-- 1. End Single Guest User Creation Experiment Section -->
		
		<!-- 2. Start Multi Guest User Creation Section -->
		<div class="child-modal modal fade" id="multi-user" tabindex="-1" role="dialog" aria-hidden="true">
            <div class="modal-content">
                <div class="close-modal" data-dismiss="modal">
                    <div class="lr">
                        <div class="rl">
                        </div>
                    </div>
                </div>
                <div class="container">
                    <div class="no_print">
						<div class="row">
							<div class="col-sm-12 col-md-12 thumbnail" style="box-shadow: 10px 10px 5px #888888;">
								<div class="panel panel-primary">
									<div class="panel-heading"><h3 class="text-center">Create Multiple Users</h3></div>
									<div class="panel-body">
										<div class="form-horizontal">
											<div class="form-group form-group-sm">
												<div class="col-sm-4">
													<label class="col-sm-6 control-label" for="no_of_users">How many Users</label>
													<div class="col-sm-6">
														<input type="number" min="2" max="150" id="no_of_users" name="no_of_users" value="2" autofocus >
													</div>
												</div>
												<div class="col-sm-4">
													<label class="col-sm-6 control-label" for="user_prefix">User name Prefix</label>
													<div class="col-sm-6">
														<input type="text" id="user_prefix" name="user_prefix">
													</div>
												</div>
												<div class="col-sm-4">						
													<label class="col-sm-6 control-label" for="pass_length">Password length</label>
													<div class="col-sm-6">
														<input type="number" min="4" max="10" id="pass_length" name="pass_length" value="5">
													</div>
												</div>
											</div>	
											<div class="form-group form-group-sm">
												<div class="col-sm-4">
													<label class="col-sm-6 control-label" for="limit_uptime">Uptime Limit(wdhms format)</label>
													<div class="col-sm-6">
														<input type="text" placeholder="1d1h" title="eg.5h30m [w(Weeks) d(days) h(hours) m(minutes) s(seconds) format]" name="limit_uptime" id="limit_uptime" >
														<!--<input type="number" placeholder="No of days" name="limit_uptime" id="limit_uptime" min="1" value="2" required >
														<select class="myCombo" id="limit_uptime" name="limit_uptime">
															<option value="2d">2 Days</option>									
															<option value="1d">1 Day</option>
															<option value="2d">2 Days</option>
															<option value="3d">3 Days</option>
															<option value="4d">4 Days</option>
															<option value="5d">5 Days</option>
														</select> -->
													</div>
												</div>
												<div class="col-sm-4">						
													<label class="col-sm-6 control-label" for="profile">Bandwidth (Mbps) Profile</label>
													<div class="col-sm-6">
														<?php
														$util->setMenu('/ip hotspot user profile');
														echo '<select class="myCombo" id="profile" name="profile">';
														foreach ($util->getAll() as $item) {
															echo '<option>', $item->getProperty('name'), '</option>';
														}
														echo '</select>'; ?>
													</div>
												</div>
												<div class="col-sm-4">						
													<label class="col-sm-6 control-label">Username & Password</label>
													<div class="col-sm-6">
														<select class="myCombo" id="same_pass" name="same_pass">
															<option value="1">Same</option>									
															<option value="2">Different</option>
														</select>
													</div>
												</div>
											</div>	
											<div class="form-group form-group-sm">
												<div class="col-sm-4">
												<label class="col-sm-6 control-label" for="limit_bytes">Maximum Usage Limit(GB), 0 for NO Limit</label>
													<div class="col-sm-6">
														<input type="number" placeholder="Maximum usable data in GB" name="limit_bytes" id="limit_bytes" min="0" value="0" required >
													</div>
													<!--<label class="col-sm-6 control-label" for="limit_bytes">Maximum Usage Limit(GB)</label>
													<div class="col-sm-6">
														<select class="myCombo" id="limit_bytes" name="limit_bytes">
															<option value="0">NONE</option>									
															<option value="1">1 GB</option>
															<option value="5">5 GB</option>
															<option value="10">10 GB</option>
															<option value="20">20 GB</option>
															<option value="50">50 GB</option>
														</select>
													</div> -->
												</div>
												<div class="col-sm-4">						
													<label class="col-sm-6 control-label" for="pass_type">Password Type</label>
													<div class="col-sm-6">
														<select class="myCombo" id="pass_type" name="pass_type" value="sn" required>
															<option value="sn">abcd1234</option>
															<option value="s">abcd</option>
															<option value="c">DCBA</option>
															<option value="sc">BaCd</option>
															<option value="cn">1342ABCD</option>
															<option value="scn">1423aBcD</option>
															<option value="n">1234</option>															
														</select>
													</div>
												</div>													
												<div class="col-sm-2">
													<div class="pull-right">
														<button name="missuing" id="missuing" onClick="ajaxMultiple()" class="btn btn-success">&nbsp; Issue</button>
													</div>
												</div>
												<div class="col-sm-2">
													<div class="pull-left">
														<button data-dismiss="modal" class="btn btn-warning"><i class="icon-save icon-large"></i>&nbsp; BACK </button>
													</div>
												</div>
											</div>	
										</div>
									</div>	
								</div>
							</div>
						</div>
					</div>
					<div id="multiple"></div>					
				</div>
			</div>
		</div>	

        <!-- 2. End Multi Guest User Creation Section -->
		
		<!-- 3. Start List All Inactive Users Section -->
        <div class="child-modal modal fade" id="list-users" tabindex="-1" role="dialog" aria-hidden="true">
            <div class="modal-content">
                <div class="close-modal" data-dismiss="modal">
                    <div class="lr">
                        <div class="rl">
                        </div>
                    </div>
                </div>
                <div class="container">
					<div class="col-sm-2 col-sm-offset-5">
						<button data-dismiss="modal" class="btn btn-info center-element" ><i class="icon-save icon-large"></i>&nbsp;BACK</button>
					</div>	
                    <div class="col-sm-12 col-md-12 thumbnail" style="box-shadow: 10px 10px 5px #888888;">
						<?php $util->setMenu('/ip hotspot user'); ?>
						<table cellpadding="0" cellspacing="0" border="0" class="table  table-bordered" id="table-01">
							<div class="alert alert-info">
								<strong><i class="icon-user icon-large"></i><h3 class="text-center">Users Not active at the moment</h3></strong>
							</div>
							<thead>
								<tr>
									<th>#</th>
									<th>User</th>
									<th>Profile</th>
									<th>Bytes In</th>
									<th>Bytes Out</th>
									<th>Total Permitted Usage</th>
									<th>Time Used</th>
									<th>Validity Limit</th>
								</tr>
							</thead>
							<tbody>
								<?php
								$i = 0;
								foreach ($util->getAll() as $item) {
									$i++;
									if ($item->getProperty('limit-bytes-total')) {
										$limit_bytes_total = $item->getProperty('limit-bytes-total').' Bytes';
									}
									else { $limit_bytes_total = 'Unlimited'; }
									
									if ($item->getProperty('limit-uptime')) {
										$limit_uptime = $item->getProperty('limit-uptime');
									}
									else { $limit_uptime = 'Not Limited'; }
									if ($item->getProperty('uptime') == "0s") {
										echo '<tr>';
											echo '<td>'.$i.'</td>';
											echo '<td>', $item->getProperty('name'),'</td>';
											echo '<td>', $item->getProperty('profile'), '</td>';
											echo '<td>', $item->getProperty('bytes-in'), '</td>';
											echo '<td>', $item->getProperty('bytes-out'), '</td>';
											echo '<td>', $limit_bytes_total, '</td>';
											echo '<td>', $item->getProperty('uptime'), '</td>';
											echo '<td>', $limit_uptime, '</td>';
										echo '</tr>';
									}
								}?>
							</tbody>
						</table>
                    </div>
					<div class="col-sm-2 col-sm-offset-5">
						<button data-dismiss="modal" class="btn btn-info center-element" ><i class="icon-save icon-large"></i>&nbsp;BACK</button>
					</div>
                </div>
            </div>
        </div>
        <!-- 3. End List All Inactive Users Section -->

		<!-- 4. Start List Active Users Section -->
        <div class="child-modal modal fade" id="active-users" tabindex="-1" role="dialog" aria-hidden="true">
            <div class="modal-content">
                <div class="close-modal" data-dismiss="modal">
                    <div class="lr">
                        <div class="rl">
                        </div>
                    </div>
                </div>
                <div class="container">
					<div class="col-sm-2 col-sm-offset-5">
						<button data-dismiss="modal" class="btn btn-info center-element" ><i class="icon-save icon-large"></i>&nbsp;BACK</button>
					</div>
                    <div class="col-sm-12 col-md-12 thumbnail" style="box-shadow: 10px 10px 5px #888888;">
						<?php $util->setMenu('/ip hotspot active'); ?>
						<table cellpadding="0" cellspacing="0" border="0" class="table  table-bordered" id="table-01">
							<div class="alert alert-info">
								<strong><i class="icon-user icon-large"></i><h3 class="text-center">List of Users Active at the moment</h3></strong>
							</div>
							<thead>
								<tr>
									<th>#</th>
									<th>Server</th>
									<th>Domain</th>
									<th>User</th>
									<th>IP Address</th>
									<th>Uptime</th>
									<th>Session Time left</th>
								</tr>
							</thead>
							<tbody>
								<?php
								$i = 0;
								foreach ($util->getAll() as $item) {
									$i++;	
									echo '<tr>';
										echo '<td>'.$i.'</td>';
										echo '<td>', $item->getProperty('server'),'</td>';
										echo '<td>', $item->getProperty('domain'), '</td>';
										echo '<td>', $item->getProperty('user'),'</td>';
										echo '<td>', $item->getProperty('address'), '</td>';
										echo '<td>', $item->getProperty('uptime'), '</td>';
										echo '<td>', $item->getProperty('session-time-left'), '</td>';
									echo '</tr>';
								} ?>
							</tbody>
						</table>
                    </div>
					<div class="col-sm-2 col-sm-offset-5">
						<button data-dismiss="modal" class="btn btn-info center-element" ><i class="icon-save icon-large"></i>&nbsp;BACK</button>
					</div>
                </div>
            </div>
        </div>
        <!-- 4. End List Active Users Section -->

		<!-- 5. Start Remove Selected users Section -->
        <div class="child-modal modal fade" id="remove-selected" tabindex="-1" role="dialog" aria-hidden="true">
            <div class="modal-content">
                <div class="close-modal" data-dismiss="modal">
                    <div class="lr">
                        <div class="rl">
                        </div>
                    </div>
                </div>
                <div class="container">
					<div class="col-sm-2 col-sm-offset-5">
						<button data-dismiss="modal" class="btn btn-info center-element" ><i class="icon-save icon-large"></i>&nbsp;BACK</button>
					</div>
					<form id="checkboxForm" class="form-horizontal">
						<div class="form-group">
							<div class="col-sm-12 col-md-12 thumbnail" style="box-shadow: 10px 10px 5px #888888;">
								<?php $util->setMenu('/ip hotspot user'); ?>
								<table cellpadding="0" cellspacing="0" border="0" class="table  table-bordered" id="table-01">
									<div class="alert alert-info">
										<strong><i class="icon-user icon-large"></i><h3 class="text-center">List of users accounts</h3></strong>
									</div>
									<thead>
										<tr>
											<th>#</th>
											<th>User</th>
											<th>Profile</th>
											<th>Bytes In</th>
											<th>Bytes Out</th>
											<th>Total Permitted Usage</th>
											<th>Time Used</th>
											<th>Validity Limit</th>
											<?php if($_SESSION['user_level'] <= 2) { //Administrator/Unit Head Only
												echo '<th>Remove</th>';
											} ?>
										</tr>
									</thead>
									<tbody>
										<?php
										$i = 0;
										foreach ($util->getAll() as $item) {
											$i++;
											if ($item->getProperty('limit-bytes-total')) {
												$limit_bytes_total = $item->getProperty('limit-bytes-total').' Bytes';
											}
											else { $limit_bytes_total = 'Unlimited'; }
										
											if ($item->getProperty('limit-uptime')) {
												$limit_uptime = $item->getProperty('limit-uptime');
											}
											else { $limit_uptime = 'Not Limited'; }
										echo '<tr>';
											echo '<td>'.$i.'</td>';
											$rid = $item->getProperty('name');
											echo '<td>', $rid,'</td>';
											echo '<td>', $item->getProperty('profile'), '</td>';
											echo '<td>', $item->getProperty('bytes-in'), '</td>';
											echo '<td>', $item->getProperty('bytes-out'), '</td>';
											echo '<td>', $limit_bytes_total, '</td>';
											echo '<td>', $item->getProperty('uptime'), '</td>';
											echo '<td>', $limit_uptime, '</td>';
											if($_SESSION['user_level'] <= 2) { //Administrator/Unit Head Only
												echo '<td>';
												$chktrue = "";
												if (!empty($item->getProperty('limit-uptime'))) {
													if (!($item->getProperty('uptime') < $item->getProperty('limit-uptime'))) {
														$chktrue = "checked";
													}
												}
												//if (!($item->getProperty('uptime') < $item->getProperty('limit-uptime'))) $chktrue = "checked"; else $chktrue = "";
												echo '<label for="'.$rid.'"></label>
													<input type="checkbox" name="removal_list[]" value="'.$rid.'" id="'.$rid.'" '.$chktrue.' class="styled" /> &nbsp;&nbsp;&nbsp; ';
													echo '<a title="Delete the Guest User Account" id="id'.$i.'"  href="#delete'.$item->getProperty('name').'" data-toggle="modal"  class="btn btn-danger btn-lg"><span class="glyphicon glyphicon-trash" aria-hidden="true"></span></a>&nbsp;&nbsp;';
													include('modal_delete_guest.php'); ?>
													<?php
												echo '</td>';
											}
										echo '</tr>';
										} ?>
									</tbody>
								</table>
								<!--<div class="col-sm-2 col-sm-offset-3">
									<button name="removal" id="removeall" data-dismiss="modal" onClick="removeAllSelected(this.form);" class="btn btn-danger"><i class="icon-save icon-large"></i></a>&nbsp;Remove All</button>&nbsp;&nbsp;&nbsp;
								</div>
								<div class="col-sm-2"> -->
								<div class="col-sm-2 col-sm-offset-4">
									<button name="removal" id="removal" data-dismiss="modal" onClick="removeSelected(this.form);" class="btn btn-success"><i class="icon-save icon-large"></i></a>&nbsp;Remove Selected</button>&nbsp;&nbsp;&nbsp;
								</div>	
								<div class="col-sm-2">
									<button data-dismiss="modal" class="btn btn-info center-element" ><i class="icon-save icon-large"></i>&nbsp;BACK</button>
								</div>
							</div>
						</div>
					</form>
				</div>
			</div>
		</div>
        <!-- 5. End Remove Selected users Section -->		

		<!-- 6. Start Remove All Expired Guest Users Section -->
        <div class="child-modal modal fade" id="remove-expired" tabindex="-1" role="dialog" aria-hidden="true">
            <div class="modal-content">
                <div class="close-modal" data-dismiss="modal">
                    <div class="lr">
                        <div class="rl">
                        </div>
                    </div>
                </div>
                <div class="container">
					<div class="col-sm-2 col-sm-offset-5">
						<button data-dismiss="modal" class="btn btn-info center-element" ><i class="icon-save icon-large"></i>&nbsp;BACK</button>
					</div>
                    <div class="col-sm-12 col-md-12 thumbnail" style="box-shadow: 10px 10px 5px #888888;">
						<table cellpadding="0" cellspacing="0" border="0" class="table  table-bordered" id="table-01">
							<div class="alert alert-info">
								<strong><i class="icon-user icon-large"></i><h3 class="text-center">Validity expired users available in System</h3></strong>
							</div>
							<thead>
								<tr>
									<th>#</th>
									<th>Server</th>
									<th>User</th>
									<th>Profile</th>
									<th>Limit Uptime</th>
									<th>Uptime</th>
									<th>Limit Bytes Total</th>
									<th>Bytes In</th>
									<th>Bytes Out</th>
								</tr>
							</thead>
							<tbody>
								<?php
								try
									{
									//use PEAR2\Net\RouterOS;
									require_once 'PEAR2/Autoload.php';
									require_once 'config.php';
									$util = new RouterOS\Util($client = new RouterOS\Client("$host", "$user", "$pass"));
									//$client = new RouterOS\Client("$host", "$user", "$pass");
									$printRequest = new RouterOS\Request('/ip hotspot user print');
									$printRequest->setArgument('.proplist','.id,server,name,profile,limit-uptime,limit-bytes-total,uptime,bytes-in,bytes-out');
									$printRequest->setQuery(RouterOS\Query::where('.id','*0', RouterOS\Query::OP_EQ) ->not()); 

									$idList = '';
									$i = 0;
									foreach ($client->sendSync($printRequest)->getAllOfType(RouterOS\Response::TYPE_DATA) as $item) {
										if (!empty($item->getProperty('limit-uptime'))) {
											if (!($item->getProperty('uptime') < $item->getProperty('limit-uptime'))) {
												$i++;
												echo '<tr>';
													echo '<td>'.$i.'</td>';
													echo '<td>', $item->getProperty('server'),'</td>';
													echo '<td>', $item->getProperty('name'), '</td>';
													echo '<td>', $item->getProperty('profile'), '</td>';
													echo '<td>', $item->getProperty('limit-uptime'), '</td>';
													echo '<td>', $item->getProperty('uptime'),'</td>';
													echo '<td>', $item->getProperty('limit-bytes-total'), '</td>';
													echo '<td>', $item->getProperty('bytes-in'), '</td>';
													echo '<td>', $item->getProperty('bytes-out'), '</td>';
												echo '</tr>';
											}
										}	
									}
								}
								catch (Exception $e) {
									echo '<script>cmodal("Access Denied!", "Error accessing validity expired users!'.$e->getMessage().'", "error", "index.php")</script>';
								}
								?>
							</tbody>
						</table>
                    </div>
					<div class="col-sm-3 col-sm-offset-5">
						<button name="uissuing" id="uissuing" onClick="ajaxExpired();" class="btn btn-success"><i class="icon-save icon-large"></i></a>&nbsp;Remove All</button>&nbsp;&nbsp;&nbsp;
						<button data-dismiss="modal" class="btn btn-info" ><i class="icon-save icon-large"></i></a>&nbsp;BACK</button>
					</div>
                </div>
            </div>
        </div>
        <!-- 6. Start Remove All Expired Guest Users Section -->		
	
		<!-- 7. Start Server Log Section -->
        <div class="child-modal modal fade" id="server-log" tabindex="-1" role="dialog" aria-hidden="true">
            <div class="modal-content">
                <div class="close-modal" data-dismiss="modal">
                    <div class="lr">
                        <div class="rl">
                        </div>
                    </div>
                </div>
                <div class="container">
                    <div class="row">
						<div class="col-sm-2 col-sm-offset-5">
							<button data-dismiss="modal" class="btn btn-info center-element" ><i class="icon-save icon-large"></i>&nbsp;BACK</button>
						</div>
						<div class="col-sm-12 col-md-12 thumbnail" style="box-shadow: 10px 10px 5px #888888;">
							<table cellpadding="0" cellspacing="0" border="0" class="table table-bordered" id="table-01">
								<div class="alert alert-info">
									<strong><i class="icon-user icon-large"></i><h3 class="text-center">Server Event Log - Last 1000 activities</h3></strong>
								</div>
								<thead>
									<tr>
										<th>#</th>
										<th>Time</th>
										<th>Topic</th>
										<th>Description</th>
									</tr>
								</thead>
								<tbody>
									<?php
									$i = 0;
									foreach ($util->setMenu('/log')->getAll() as $entry) {
										$i++;	
										echo '<tr>';
											echo '<td>'.$i.'</td>';
											echo '<td>', $entry('time'),'</td>';
											echo '<td>', $entry('topics'), '</td>';
											echo '<td>', $entry('message'), '</td>';
										echo '</tr>';
									}
									?>
								</tbody>
							</table>
						</div>
						<div class="col-sm-2 col-sm-offset-5">
							<button data-dismiss="modal" class="btn btn-info center-element" ><i class="icon-save icon-large"></i>&nbsp;BACK</button>
						</div>						
					</div>
				<!--</div>-->
				</div>
			</div>
		</div>
        <!-- 7. End Server Log Section -->		

		<!-- 9. Start System User Management Section -->
		<div class="child-modal modal fade" id="system-user" tabindex="-1" role="dialog" aria-hidden="true">
            <div class="modal-content">
                <div class="close-modal" data-dismiss="modal">
                    <div class="lr">
                        <div class="rl"></div>
                    </div>
                </div>
                <div class="container">
                    <div class="no_print">
						<div class="row">
							<div class="col-sm-4 col-sm-offset-4">
								<a href="#change-password" data-toggle="modal" class="btn btn-primary btn-lg center-element"><span class="glyphicon glyphicon-edit" aria-hidden="true"></span>Change My Password</a>&nbsp;&nbsp;
							</div>
							<div class="col-sm-12 col-md-12 thumbnail" style="box-shadow: 10px 10px 5px #888888;">
								<table cellpadding="0" cellspacing="0" border="0" class="table table-bordered" id="table-01">
									<div class="alert alert-info">
										<strong><i class="icon-user icon-large"></i><h3 class="text-center">System Users managing Hotspot Activities</h3></strong>
									</div>
									<thead>
										<tr>
											<th>Username</th>
											<th>Password</th>                                 
											<th>Firstname</th>                                 
											<th>Lastname</th>
											<th>Level</th>
											<?php if($_SESSION['user_level'] == 1) { //Administrator Only
												echo '<th>Actions</th>';
											} ?>	
										</tr>
									</thead>
									<tbody>
										<?php 
										$stmt = $DB_con->prepare("SELECT * FROM hotspot_users WHERE 1");
										$stmt->execute(array());
										while($row=$stmt->fetch(PDO::FETCH_ASSOC)) {
											$id=$row['user_id'];
											if ($row['status'] == 'Active') { echo '<tr class="alert-info">'; } else { echo '<tr class="alert-danger">'; }
											?>
												<td><?php echo $row['username']; ?></td> 
												<td><?php echo '..............'; ?></td> 
												<td><?php echo $row['firstname']; ?></td> 
												<td><?php echo $row['lastname']; ?></td>
												<?php 
												switch ($row['user_level']) {
													case 1 :
														echo '<td>Administrator</td>';
														break;
													case 2 :
														echo '<td>Unit Head</td>';
														break;
													case 3 :
														echo '<td>System User</td>';
														break;
												} 
												if($_SESSION['user_level'] == 1) { //Administrator Only
													echo '<td>';
														echo '<a title="Get Details of User & More Actions" id="'.$id.'" data-id="'.$id.'" name="'.$id.'"  href="#getUserModal" data-toggle="modal" class="btn btn-primary btn-lg"><i class="fa fa-caret-square-o-down" aria-hidden="true"></i></a>&nbsp;&nbsp;';
													echo '</td>';
												} ?>
											</tr>
											<?php
										} ?>
									</tbody>
								</table>
							</div>
							<div class="col-sm-2 col-sm-offset-5">
								<button data-dismiss="modal" class="btn btn-info center-element" ><i class="icon-save icon-large"></i>&nbsp;BACK</button>
							</div>
						</div>
					</div>
				</div>
			</div>
		</div>	
		<!-- 9. End System User Management Section -->		
		
		<!-- 10. Start Remove All Un-Initiated Guest Users Section -->
        <div class="child-modal modal fade" id="remove-uninitiated" tabindex="-1" role="dialog" aria-hidden="true">
            <div class="modal-content">
                <div class="close-modal" data-dismiss="modal">
                    <div class="lr">
                        <div class="rl">
                        </div>
                    </div>
                </div>
                <div class="container">
					<div class="col-sm-2 col-sm-offset-5">
						<button data-dismiss="modal" class="btn btn-info center-element" ><i class="icon-save icon-large"></i>&nbsp;BACK</button>
					</div>
                    <div class="col-sm-12 col-md-12 thumbnail" style="box-shadow: 10px 10px 5px #888888;">
						<?php $util->setMenu('/ip hotspot user'); ?>
						<table cellpadding="0" cellspacing="0" border="0" class="table  table-bordered" id="table-01">
							<div class="alert alert-info">
								<strong><i class="icon-user icon-large"></i><h3 class="text-center">User accounts not yet initiated any activities, ie. accounts inactive at the moment</h3></strong>
							</div>
							<thead>
								<tr>
									<th>#</th>
									<th>Server</th>
									<th>User</th>
									<th>Profile</th>
									<th>Uptime Limit</th>
								</tr>
							</thead>
							<tbody>
								<?php
								$i = 0;
								foreach ($util->getAll() as $item) {
									if ($item->getProperty('uptime') == 0) {
									$i++;										
										echo '<tr>';
											echo '<td>'.$i.'</td>';
											echo '<td>', $item->getProperty('server'),'</td>';
											echo '<td>', $item->getProperty('name'),'</td>';
											echo '<td>', $item->getProperty('profile'),'</td>';
											echo '<td>', $item->getProperty('limit-uptime'), '</td>';
										echo '</tr>';
									}
								} ?>
							</tbody>
						</table>
                    </div>
					<div class="col-sm-3 col-sm-offset-5">
						<?php if($_SESSION['user_level'] <= 2) {
							echo '<button name="uissuing" id="uissuing" onClick="ajaxUninitiated();" class="btn btn-success"><i class="icon-save icon-large"></i></a>&nbsp;Remove All</button>&nbsp;&nbsp;&nbsp;';
						} ?>	
						<button data-dismiss="modal" class="btn btn-info" ><i class="icon-save icon-large"></i></a>&nbsp;CANCEL</button>
					</div>
                </div>
            </div>
        </div>
        <!-- 10. Start Remove All Un-Initiated Guest Users Section -->
		
		<!-- 11. Start HotSpot User Profiles Management Section -->
		<div class="child-modal modal fade" id="profiler" tabindex="-1" role="dialog" aria-hidden="true">
            <div class="modal-content">
                <div class="close-modal" data-dismiss="modal">
                    <div class="lr">
                        <div class="rl"></div>
                    </div>
                </div>
                <div class="container">
                    <div class="no_print">
						<div class="row">
							<div class="col-sm-2 col-sm-offset-5">
								<button data-dismiss="modal" class="btn btn-info center-element" ><i class="icon-save icon-large"></i>&nbsp;BACK</button>
							</div>
							<div class="col-sm-12 col-md-12 thumbnail" style="box-shadow: 10px 10px 5px #888888;">
								<?php $util->setMenu('/ip hotspot user profile'); ?>								
								<table cellpadding="0" cellspacing="0" border="0" class="table table-bordered" id="table-01">
									<div class="alert alert-info">
										<strong><i class="icon-user icon-large"></i><h3 class="text-center">HotSpot User Profiles Available</h3></strong>
									</div>
									<thead>
										<tr>
											<th>#</th>
											<th>Name</th>
											<th>Session Timeout</th>                                 
											<th>Keepalive Timeout</th>
											<th>Shared Users</th>
											<th>Rate Limit(Rx/Tx)</th>
											<th>MAC Cookie Timeout</th>
											<?php if($_SESSION['user_level'] == 1) { //Administrator Only
												echo '<th>Actions</th>';
											} ?>	
										</tr>
									</thead>
									<tbody>
										<?php
										$i = 0;
										foreach ($util->getAll() as $item) {
											$i++;										
											echo '<tr>';
												echo '<td>'.$i.'</td>';
												echo '<td>', $item->getProperty('name'),'</td>';
												echo '<td>', $item->getProperty('session-timeout'), '</td>';
												echo '<td>', $item->getProperty('keepalive-timeout'), '</td>';
												echo '<td>', $item->getProperty('shared-users'), '</td>';
												echo '<td>', $item->getProperty('rate-limit'), '</td>';
												echo '<td>', $item->getProperty('mac-cookie-timeout'), '</td>';

												if($_SESSION['user_level'] == 1) { //Administrator Only
													echo '<td>';
													echo '<a title="Get Details of the Profile & More Actions" id="'.$id.'" data-id="'.$item->getProperty('name').'" name="'.$id.'"  href="#getProfileModal" data-toggle="modal" class="btn btn-primary btn-lg"><i class="fa fa-caret-square-o-down" aria-hidden="true"></i></a>';
												echo '</td>';
												} ?>
											</tr>
											<?php
										} ?>
									</tbody>
								</table>
							</div>
							<div class="col-sm-2 col-sm-offset-5">
								<button data-dismiss="modal" class="btn btn-info center-element" ><i class="icon-save icon-large"></i>&nbsp;BACK</button>
							</div>
						</div>
					</div>
				</div>
			</div>
		</div>
		<!-- 11. End HotSpot User Profiles Management Section -->
	</div>		
</body>
<?php
include('modal_change_pass.php');
include('modal_delete_guest.php');
include('modal_get_profiles.php');
include('modal_get_user.php');
?>

File: /hotsoft.php
<?php
use PEAR2\Net\RouterOS;
require_once 'PEAR2/Autoload.php';
require_once 'config.php';
$util = new RouterOS\Util($client = new RouterOS\Client("$host", "$user", "$pass"));

if (isset($_GET['action'])) { $action = $_GET['action']; } else { $action = 'checkout'; }
if (isset($_GET['username'])) $username = $_GET['username'];
/*Sample Call
	FORMAT: localhost/hotsoft.php?action=checkin&username=101&password=spice&limit_uptime=10d&limit_bytes=10&profile=default
	action & username are REQUIRED, all other fields are optional
	action can be 'checkin' or 'checkout'.  if action is 'checkout', only user name need to be specified
	username can be room number or any username
	password - if password is not given, the given username will be the password
	limit_uptime - if given in the format '10d' for 10 days, '1d 10:30:00' for 1 day 10 hours and 30 minutes
	limit_bytes - if given the total upload/download bytes in GB, eg '10' means 10Gb
	profile - if given any user profile name available in the Wifi hotspot
	
	sample call:
	192.168.100.10/hotsoft.php?action=checkin&username=101&password=spice  - While checking in a room
	192.168.100.10/hotsoft.php?action=checkout&username=101 - While checking out a room
	
	Return Values
	0 - Success (Successfully created user account or Successfully removed User account)
	1 - Wrong action verb
	2 - Invalid or blank username
	3 - Call with an already existing/Duplicate username
	4 - 
 
*/
if (strtolower($action) == 'checkin')) {
	if (!empty($username)) {
		if (isset($_GET['password'])) { $password = $_GET['password']; } else { $password = $username; } 
		if (isset($_GET['limit_uptime'])) $limit_uptime = $_GET['limit_uptime'];
		if (isset($_GET['limit_bytes'])) $limit_bytes = $_GET['limit_bytes'];
		if (isset($_GET['profile'])) { $profile = $_GET['profile']; } else { $profile = 'default'; } 
	
		$util->setMenu('/ip hotspot user');
		$iv = count($util);

		if ((intval($limit_bytes) != 0) and (!empty($limit_uptime))) {
			$limit_bytes_total = (intval($limit_bytes) * 1024 * 1024 * 1024 );
			$util->add(
				array(
					'name' => "$username",
					'password' => "$password",
					'limit-uptime' => "$limit_uptime",
					'limit-bytes-total' => "$limit_bytes_total",
					'profile' => "$profile"
				)
			);
		}
		elseif (intval($limit_bytes) != 0) {
			$limit_bytes_total = (intval($limit_bytes) * 1024 * 1024 * 1024 );
			$util->add(
				array(
					'name' => "$username",
					'password' => "$password",
					'limit-bytes-total' => "$limit_bytes_total",
					'profile' => "$profile"
				)
			);	
			}
		else
			{
			$util->add(
				array(
					'name' => "$username",
					'password' => "$password",
					'limit-uptime' => "$limit_uptime",
					'profile' => "$profile"
				)
			);
			$limit_bytes = 0; // For Adding it to Local database
		}		

		if ($iv != count($util)) {
			include('dbconfig.php');
			$stmt = $DB_con->prepare("SELECT booking_id from hotspot_vouchers ORDER BY booking_id DESC LIMIT 1");
			$stmt->execute(array());
			$row = $stmt->fetch(PDO::FETCH_ASSOC);
			$booking_id = $row['booking_id'];
			$booking_id++;
			$uid = $booking_id.'-1-'.date('dmY');
			$creator = 999;
			$created_by = 'Hotsoft';
			$stmt = $DB_con->prepare("UPDATE hotspot_vouchers set status=:status WHERE 1");
			$stmt->execute(array(':status' => 'Over'));
				$stmt = $DB_con->prepare("insert into hotspot_vouchers (created_on, created_by, creator, user_name, password, printed_times,
				printed_last, status, group_of, booking_id, limit_uptime, limit_bytes, profile, uid)
				values(NOW(), :created_by, :creator, :user_name, :password, :printed_times, :printed_last, :status, :group_of, 
				:booking_id, :limit_uptime, :limit_bytes, :profile, :uid)");
			$stmt->execute(array(':created_by' => $created_by, ':creator' => $creator, ':user_name' => $username, ':password' => $password,
				':printed_times' => 0, ':printed_last' => '', ':status' => 'Active', ':group_of' => 1,
				':booking_id' => $booking_id, ':limit_uptime' => $limit_uptime, ':limit_bytes' => $limit_bytes,
				':profile' => $profile, ':uid' => $uid));
			echo 0; //Success
			}
		else
			{
				echo 3; // Duplicate/Existing username
		}	
	}
else
	{
		echo 2; //Blank Username
	}	
	//End Adding a Guest User
}
elseif (strtolower($action) == 'checkout'))  {
	//Removal
	$username=trim($_GET['username']);
	if (!empty($username)) {
		$printRequest = new RouterOS\Request('/ip/hotspot/user/print');
		$printRequest->setArgument('.proplist', '.id,name');
		$printRequest->setQuery(RouterOS\Query::where('name', $username));
		$id = $client->sendSync($printRequest)->getProperty('.id');

		$removeRequest = new RouterOS\Request('/ip/hotspot/user/remove');
		$removeRequest->setArgument('numbers', $id);
		$client->sendSync($removeRequest);
		echo 0; //Success
	}
	else
		{
		echo 2; //Blank Username
	}
}
else
{
	echo 1; //Wrong Action Verb
}
?>

File: /index.php
<!DOCTYPE html>
<html lang="en">
<link rel="icon" href="favicon.ico" type="image/x-icon"/>
<?php
//Start session
if ( !isset($_SESSION) ) session_start();
//Check whether the session variables present or not, and assign them to Ordinary variables, if present.
if (!isset($_SESSION['user_level']) || (trim($_SESSION['user_level']) == '' || (trim($_SESSION['user_level']) >= 4))) {
    header("location:login.php");
}
?>

<?php if ( !isset($_SESSION) ) session_start(); ?>
<?php  error_reporting(E_ALL);
ini_set('display_errors', 1); ?>

<?php include('header.php'); ?>
<?php include('dbconfig.php'); ?>
<?php 
use PEAR2\Net\RouterOS;
require_once 'PEAR2/Autoload.php';
require_once 'config.php';
try {
	$util = new RouterOS\Util($client = new RouterOS\Client("$host", "$user", "$pass"));
	include_once('home.php');
}
catch (Exception $e) {
	echo "Error Accessing Data: " . $e->getMessage();
	include_once('settings.php');
}
?>

File: /info.php
<?php
echo '<br><h1>PHP Info of this Machine</h1><br><br>';
echo phpinfo();
/*
* Md. Nazmul Basher


ob_start(); // Turn on output buffering
system(‘ipconfig /all’); //Execute external program to display output
$mycom=ob_get_contents(); // Capture the output into a variable
ob_clean(); // Clean (erase) the output buffer

$findme = “Physical”;
$pmac = strpos($mycom, $findme); // Find the position of Physical text
$mac=substr($mycom,($pmac+36),17); // Get Physical Address



echo "MAC ID: ";
echo $pmac;
echo $mac;

function getMacLinux() {
  exec('netstat -ie', $result);
  if(is_array($result)) {
    $iface = array();
    foreach($result as $key => $line) {
      if($key > 0) {
        $tmp = str_replace(" ", "", substr($line, 0, 10));
        if($tmp <> "") {
          $macpos = strpos($line, "HWaddr");
          if($macpos !== false) {
            $iface[] = array('iface' => $tmp, 'mac' => strtolower(substr($line, $macpos+7, 17)));
          }
        }
      }
    }
    return $iface[0]['mac'];
  } else {
    return "notfound";
  }
}

echo 'Linux Mac ID : '.getMaclinux();


$ip=$_SERVER['SERVER_ADDR'];
echo "Server IP: {$ip}<br />
Server Mac: ";
$conf=exec('netstat -ie');
$prots=explode("\n\n",$conf);
if($ip=='127.0.0.1')$ip='192.168.';
foreach($prots as $prot){
    if(strpos($prot,' addr:'.$ip) && preg_match('/(?:\s+)HWaddr(?:\s+)(?P<mac>[a-f0-9\:]+)/',$prot,$match)){
    echo $match['mac'];
    }
}


$ipAddress=$_SERVER['REMOTE_ADDR'];
$macAddr=false;

#run the external command, break output into lines
$arp=`arp -a $ipAddress`;
$lines=explode("\n", $arp);

#look for the output line describing our IP address
foreach($lines as $line)
{
   $cols=preg_split('/\s+/', trim($line));
   if ($cols[0]==$ipAddress)
   {
       $macAddr=$cols[1];
   }
}
echo $lines[1];
echo $cols[1];
echo $macAddr;
*/
//===========================================
ob_start();
$cmd = system("getmac"); 
ob_end_clean();
echo 'Your MAC ID : '. substr($cmd,0,17);
/*
echo '<br><br><br>';
echo '<br>New Get Mac: '.substr($cmd,0,17).'<br>';
echo 'Location: '.strstr($cmd, '{');
$cmd = system("nbtstat -a ip.of.remote.machine");
echo '<br>Another ID New Get Mac: '.$cmd; */
?>

File: /js\customModal.js
//Simple redirect function
function redirect_(url) {
    window.location = url;
}

//Determine if a value is present in an array
function is_value_in_array(value, arry) {
    for (var i=0; i<arry.length; i++) {
        if (arry[i] == value){
            return true;
        }
    }
    return false;
}

//Backbone of the modal
//Creates the basic layout and elements of the modal
//This is called by other wrapper function with necessary arguments
function BaseModal (title, message, type, redirect_url,
                    close_on_click, close_on_key, close_keys,
                    buttons) {

    //Actual close function
    var cModalClose = function () {
        cmodal.style.display = "none";
        //Redirect only if URL provided
        if (redirect_url != null) {
            redirect_(redirect_url);
        }
        //Implies the cancel/close button was pressed
        return 0;
    }
   
    //Close event trigger from other click events
    var cModalCloseTrigger = function (event) {
        if (close_on_click == true) {
            if ((event.target == cmodal) || (event.target == cclose)) {
                cModalClose();
            }
        }
    }
   
    //Capture keypress and check for exit keys (close_keys)
    var cModalKeypress = function (event) {
        if (close_on_key == true) {
            //Close only if the pressed key was being expected 
            if (is_value_in_array(event.keyCode,close_keys)) {
                cModalClose();
            }
        }
    }
    
    //Create base modal container div
    var cmodal = document.createElement("div");
    cmodal.className = "custom-modal";
    cmodal.onclick = cModalCloseTrigger;
    //Register keypress event callback
    window.onkeyup = cModalKeypress;
    
    //Add content div
    var ccontent = document.createElement("div");
    ccontent.className = "cmodal-content " + type;
    cmodal.appendChild(ccontent);
    
    //Add header div
    var cheader = document.createElement("div");
    cheader.className = "cmodal-header";
    ccontent.appendChild(cheader);
    
    //Add title-text and close-button;
    //Title text
    var ctitle = document.createElement("span");
    ctitle.className = "cmodal-title";
    ctitle.innerHTML = title;
    //Close button
    var cclose = document.createElement("button");
    cclose.className = "cmodal-close";
    cclose.innerHTML = "x";
    cclose.onclick = cModalClose;
    cheader.appendChild(ctitle);
    cheader.appendChild(cclose);
    
    //Add modal-body div
    var cbody = document.createElement("div");
    cbody.className = "cmodal-body";
    ccontent.appendChild(cbody);
    
    //Add message element to the modal body
    var cmessage = document.createElement("span");
    cmessage.className = "cmodal-message";
    cmessage.innerHTML = message;
    cbody.appendChild(cmessage);
    
    //Add icon after message
    var cicon = document.createElement("img");
    cicon.className = "cmodal-icon"
    cicon.src = "images/"+type+".png";
    cmessage.appendChild(cicon);
    
    //If this a dialog with buttons, the list "buttons" with
    //the buttons to be added to the modal will be provided
    if (buttons != []) {
        //Create footer 
        var cfooter = document.createElement("div");
        cfooter.className = "cmodal-footer";
        //Populate footer with buttons from the list
        //Set properties of buttons
        for (var i=0; i<buttons.length; i++) {
            var buttn = document.createElement("button");
            buttn.appendChild(document.createTextNode(buttons[i].text));
            buttn.id = i.toString();
            // Default close button
            if (buttons[i].action == "cmodalClose") {
                buttn.onclick = cModalClose;
                buttn.className = "cmodal-button";
                //Style button with default style if not provided
                if ("style" in buttons[i]) {
                    buttn.className = "cmodal-button " + buttons[i].style;
                }
			// JS function
			} else if ((buttons[i].action != "") && (typeof(buttons[i].action) == "function")) {
				buttn.className = "cmodal-button cmodal-ok";
                //The id of this button is its index in "buttons" list
                buttn.onclick = buttons[i].action;
                //Style button with default style if not provided
                if ("style" in buttons[i]) {
                    buttn.className = "cmodal-button " + buttons[i].style;
                }
            // Some URL
            } else if ((buttons[i].action != "") && (typeof(buttons[i].action) != "function")) {
                buttn.className = "cmodal-button cmodal-ok";
                //The id of this button is its index in "buttons" list
                buttn.onclick = function () {
                                redirect_(buttons[this.id].action);
                }
                //Style button with default style if not provided
                if ("style" in buttons[i]) {
                    buttn.className = "cmodal-button " + buttons[i].style;
                }
            // No action was specified. Just return the index of the button pressed
            } else {
                buttn.className = "cmodal-button cmodal-generic";
                buttn.onclick = function () {
                                return this.id;
                }
                //Style button with default style if not provided
                if ("style" in buttons[i]) {
                    buttn.className = "cmodal-button " + buttons[i].style;
                }
            }
            // Append button to the footer
            cfooter.appendChild(buttn);            
        }
        // Add footer to modal content. Happens only if buttons provided
        ccontent.appendChild(cfooter);
    }

    //Enable display of modal
    cmodal.style.display = "block";
    //Append cModal to the document
    document.body.appendChild(cmodal);
    ccontent.focus();
}

//Base modal function call skeleton for reference
//Update this if you change the argument list of BaseModal function
//BaseModal(title, message, type, redirect_url, close_on_click, close_on_key, close_keys, buttons)


//Usual modal dialog
function cmodal (title, message, type, redirect_url=null) {
    return BaseModal(title, message, type, redirect_url, close_on_click=true,
                        close_on_key=true, close_keys=[13,27], buttons=[]);
}

//Modal dialog with buttons
function cmodalOkCancel (title, message, type, buttons=[]) {
    return BaseModal(title, message, type, redirect_url=null, close_on_click=false,
                        close_on_key=true, close_keys=[27,], buttons=buttons);
}

File: /login.php
<?php include('header.php'); ?>
<?php if ( !isset($_SESSION) ) session_start(); ?>
<?php  error_reporting(E_ALL);
ini_set('display_errors', 1); ?>
<div class="container">
	<header>
		<h1 style="text-align:center;">Easy Hotspot</h1>	
		<h2 style="text-align:center;">Simple HotSpot User Management Utility</h2>
		<h3 style="text-align:center;">By TEAM ZETOZONE</h3>
	</header>
	<div class="row">
		<div class="col-sm-6 col-sm-offset-3 well" style="box-shadow: 10px 10px 5px #888888;">
			<div class="panel panel-primary">
				<div class="panel panel-heading">
					<p><strong>Login using Registered Credentials</strong></p>
				</div>
				<div class="panel-body">		
					<form class="form-horizontal" id="loginform" action="" method="POST">
						<div class="form-group form-group-sm">
							<label class="col-sm-2 control-label" for="txt_user_name">Username</label>
							<div class="col-sm-8">
								<input type="text" id="txt_user_name" name="username" placeholder="Registered Username" required class="form-control" autofocus>
							</div>
						</div>
						<div class="form-group form-group-sm">
							<label class="col-sm-2 control-label" for="txt_password">Password</label>
							<div class="col-sm-8">
								<input type="password" id="password" name="password" placeholder="Password" placeholder="Password" required class="form-control">
							</div>
						</div>
						<div class="form-group form-group-sm">
							<div class="col-sm-2 col-sm-offset-4">
								<button id="btn_login" name="btn_login" type="submit" class="btn btn-primary">&nbsp;Submit</button>
							</div>
							<div class="col-sm-2">
								<button id="btn_cancel" name="btn_cancel" type="reset" class="btn btn-success">&nbsp;Cancel</button>
							</div>
						</div>
					</form>
					<?php
					if (isset($_POST['btn_login'])){
						$username = $_POST['username'];
						$password = $_POST['password'];
						$password= sha1($password);
						include('dbconfig.php');
						
						try {
							$stmt = $DB_con->prepare("SELECT user_id FROM hotspot_users WHERE 1");
							$stmt->execute(array());
						}
						catch(PDOException $e) {
							try {
								include('database.php');
								$stmt = $DB_con->prepare("SELECT user_id FROM hotspot_users WHERE 1");
								$stmt->execute(array());
							}
							catch(PDOException $e) {
								echo "Error Accessing Data: " . $e->getMessage();
							}
						}
						
						$count = $stmt->rowCount();
						if( $count == 0 ) {
							$password = sha1('admin');
							$stmt = $DB_con->prepare("insert into hotspot_users (date_added, firstname, username, password, user_level, status, user_group, created_at)
								values(CURDATE(), 'Administrator', :username, :password, :level, 'Active', 1, NOW())");
							$stmt->execute(array(':username' => 'admin', ':password' => $password, ':level' => 1));
						}
						try
							{
							$stmt = $DB_con->prepare("SELECT * FROM hotspot_users WHERE username=:username AND password =:password AND status =:status");
							$stmt->execute(array(':username' => $username, ':password' => $password, ':status' => 'Active'));
							$count = $stmt->rowCount();
						}
						catch(PDOException $e) {
							echo "Error: " . $e->getMessage();
						}
	
						if( $count == 1 ) {
							$row=$stmt->fetch(PDO::FETCH_ASSOC);
			
							$_SESSION['id']=$row['user_id'];
							$_SESSION['username']=$row['firstname'].' '.$row['lastname'];
							$_SESSION['user_level']= $row['user_level'];
							echo '<script language="javascript">window.location.href ="index.php";</script>';
						}
						else
							{
							echo '<script>cmodal("Access Denied!", "No Active User account with the given Username/Password Combination!", "error", "index.php")</script>';
						}
					}
					?>
				</div>
			</div>
		</div>
	</div>
</div>

File: /logme.php
<?php
/*
 *  Copyright (C) 2018 Laksamadi Guko.
 *
 *  This program is free software; you can redistribute it and/or modify
 *  it under the terms of the GNU General Public License as published by
 *  the Free Software Foundation; either version 2 of the License, or
 *  (at your option) any later version.
 *
 *  This program is distributed in the hope that it will be useful,
 *  but WITHOUT ANY WARRANTY; without even the implied warranty of
 *  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 *  GNU General Public License for more details.
 *
 *  You should have received a copy of the GNU General Public License
 *  along with this program.  If not, see <http://www.gnu.org/licenses/>.
 */
session_start();
?>

<div style="padding-top: 5%;"  class="login-box">
  <div class="card">
    <div class="card-body login-card-body">
      <div class="text-center">
        <img class="img-fluid" src="img/favicon.png" alt="User profile picture">
      </div>
      <h3 style="margin: 30px;" class="text-center">MIKHMON</h3>
      <form autocomplete="off" action="" method="post">
        <div class="form-group has-feedback">
          <input class="form-control form-control-sm" type="text" name="user" placeholder="User" required="1" autofocus>
        </div>
        <div class="form-group has-feedback">
          <input class="form-control form-control-sm" type="password" name="pass" placeholder="Password" required="1">
        </div>
        <div class="row">
          <div class="col-12">
		        <input class="btn btn-primary btn-block" type="submit" name="login" value="Login">
          </div>
        </div>

      </form>
    <div style="margin-top: 10px;" class="block">
    <?php echo $error; ?>
    </div>
    </div>
  </div>
</div>
</body>
</html>

File: /logout.php
<?php
session_start();
session_unset(); 
session_destroy();
//echo '<script>window.open("backup.php", "_self").close(); top.close(); window.open("backup.php", "_self", ""); window.close();</script>';
header('location:index.php');
?>

File: /modal_change_pass.php
<div class="child-modal modal fade" id="change-password" tabindex="-1" role="dialog" aria-hidden="true">
    <div class="modal-dialog">
		<div class="modal-content">
			<form class="form-horizontal" id="chPassword" method="post">
				<div class="modal-body">
					<div class="alert alert-info text-center"><strong>Welcome <?php echo $_SESSION['username'].', '; ?> Change Your Login Password</strong></div>
					<div class="form-group">
						<label class="control-label col-sm-6">Type-in New Password</label>
						<div class="col-sm-6">
							<div class="input-group">
								<input type="password" pattern="(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{8,}" title="Must contain at least one number, one uppercase letter, one lowercase letter and at least 8 characters length" name="np" id="newpassword" placeholder="New Password" required="true" autofocus tabindex="1">
								<div id='chPassword_np_errorloc' class="error_strings"></div>
							</div>
						</div>	
					</div>
					<div class="form-group">
						<label class="control-label col-sm-6">Re-type New Password</label>
						<div class="col-sm-6">
							<input type="password" pattern="(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{8,}" title="Must contain at least one number, one uppercase letter, one lowercase letter and at least 8 characters length" name="rp" id="retypepassword" placeholder="Re-type New Password" required="true" tabindex="2">
							<div id='chPassword_rp_errorloc' class="error_strings"></div>
						</div>
					</div>
				</div>	
				<div class="modal-footer">
					<div class="col-sm-12">
						<div class="col-sm-3 col-sm-offset-3">
							<div class="pull-right">
								<button name="update_pass" id="update_pass" type="submit" onClick="changePass(this.form);" class="btn btn-success" data-dismiss="modal" tabindex="3"><i class="icon-save icon-large"></i>&nbsp;Update</button>
							</div>
						</div>
						<div class="col-sm-6">
							<div class="pull-left">	
								<a href="index.php" data-dismiss="modal" class="btn btn-info" tabindex="4"><i class="icon-arrow-left icon-large"></i>&nbsp;Cancel</a>
							</div>
						</div>
					</div>
				</div>
			</form>
		<!--	<script type="text/javascript">
				var frmvalidator  = new Validator("chPassword");
				frmvalidator.EnableOnPageErrorDisplay();
				frmvalidator.EnableMsgsTogether();
				
				frmvalidator.addValidation("np","req","Please enter your New Password");
				frmvalidator.addValidation("np","regexp=^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$%^&*-]).{8,}$",
                                          "Must contain at least one number, one uppercase letter, one lowercase letter and at least 8 characters length");
				frmvalidator.addValidation("rp","req","Please retype your New Password");
				frmvalidator.addValidation("rp","regexp=^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$%^&*-]).{8,}$",
                                          "Must contain at least one number, one uppercase letter, one lowercase letter and at least 8 characters length");						  
				frmvalidator.addValidation("np","eqelmnt=rp", "Both Passwords should be same");						  
			</script> 
			<script type="text/javascript">
				window.onload = function (){
				eventHandler = function (e){
				if (e.keyCode === 13 ) //Enter key to Trap
					{
					event.preventDefault();
					$("#update_pass").trigger('click'); /*
					var cti = document.activeElement.tabIndex;
					if (cti == 1 ) 
						$('[tabindex=' + (cti + 1) + ']').focus();
					else
						$('[tabindex=' + (cti - 1) + ']').focus();
					return false; */
					}
				}
			window.addEventListener('keydown', eventHandler, false);
			} ;
			</script> -->
		</div>	
	</div>
</div>

File: /modal_delete_guest.php
<div id="delete<?php echo $item->getProperty('name'); ?>" class="child-modal modal fade"  tabindex="-1" role="dialog" aria-hidden="true">
    <div class="modal-dialog">
		<div class="modal-content">	
			<form class="form-horizontal" method="post">
				<div class="modal-body">
					<div class="alert alert-info text-center"><strong>Delete Guest User</strong></div>
					<div class="form-group">
						<label class="control-label col-xs-3">Username</label>
						<div class="col-xs-7">
							<div class="input-group">
								<span class="input-group-addon"><i class="fa fa-envelope-o fa-fw"></i></span>
								<input type="text" size="40" name="username" value="<?php echo $item->getProperty('name'); ?>" readonly>
							</div>
						</div>	
					</div>
					<div class="form-group">
						<label class="control-label col-xs-3" for="uptime">Limit Uptime</label>
						<div class="col-xs-7">
							<div class="input-group">
								<span class="input-group-addon"><i class="fa fa-key fa-fw"></i></span>
								<input type="text" name="uptime" value="<?php echo $item->getProperty('limit-uptime'); ?>" readonly>
							</div>
						</div>	
					</div>
					<div class="form-group">
						<label class="control-label col-xs-3">Address</label>
						<div class="col-xs-7">
							<input type="text" name="firstname" value="<?php echo $item->getProperty('address'); ?>" readonly>
						</div>	
					</div>
					<div class="form-group">
						<label class="control-label col-xs-3" for="lastname">Uptime</label>
						<div class="col-xs-7">
							<input type="text" name="lastname" value="<?php echo $item->getProperty('uptime'); ?>" readonly>
						</div>
					</div>
					<div class="form-group">
						<label class="control-label col-xs-3" for="session-time-left">Session time Left</label>
						<div class="col-xs-7">
							<input type="text" name="session-time-left" value="<?php echo $item->getProperty('session-time-left'); ?>" readonly>
						</div>
					</div>
				</div>	
				<div class="modal-footer">
					<div class="col-sm-12">
						<div class="col-sm-3 col-sm-offset-3">
							<div class="pull-right">
								<button name="issuing" onClick="removeAjax('<?php echo $item->getProperty('name'); ?>')" class="btn btn-success" data-dismiss="modal"><i class="icon-save icon-large"></i></a>&nbsp;Remove</button>
							</div>
						</div>
						<div class="col-sm-6">
							<div class="pull-left">
								<button class="btn btn-error" data-dismiss="modal" ><i class="icon-save icon-large"></i></a>&nbsp;BACK</button>
							</div>
						</div>
					</div>
				</div>
			</form>
		</div>	
	</div>
</div>

File: /modal_get_profiles.php
<div id="getProfileModal" class="child-modal modal fade" tabindex="-1" role="dialog" aria-hidden="true">
	<div class="modal-dialog">
		<div class="modal-content">	
			<form class="form-horizontal" method="post">
				<div class="modal-body">
					<div class="alert alert-info text-center"><strong>HotSpot User Profiles for Guest Users</strong></div>
					<div class="form-group">
						<label class="control-label col-xs-2">Profile Name</label>
						<div class="col-xs-3">
							<div class="input-group">
								<input type="hidden" id="profile_id" name="id" >
								<input type="text" id="profile_name" size="20" onChange="genClick();" required tabindex="1" autofocus>
							</div>
						</div>
						<label class="control-label col-xs-2">Validity</label>
						<div class="col-xs-3 pull-left">
							<div class="input-group">
								<input type="text" id="validity" size="20"  title="Validity can be in days ( 3d), hours (4h) or weeks (1w) etc or like 3d 10:30:00" onChange="genClick();" required tabindex="2">
							</div>
						</div>						
					</div>
					<div class="form-group">
						<label class="control-label col-xs-2">Grace Period</label>
						<div class="col-xs-3">
							<input type="text" id="grace_period" title="Grace period, if any in wdhms format" onChange="genClick();" tabindex="3">
						</div>
						<label class="control-label col-xs-2 pull-left">On Expiry</label>
						<div class="col-xs-3 pull-left">
							<select class="myCombo" id="on_expiry" title="What to do on expiry of accounts created using this profile, Remove account or Just keep disabled" onChange="genClick();" required tabindex="4">
								<!-- <option></option> -->
								<option value="">Select...</option>
								<option value="0">None</option>								
								<option value="rem">Remove</option>
								<option value="ntf">Notice</option>
								<option value="remc">Remove & Record</option>
								<option value="ntfc">Notice & Record</option>
							</select>
						</div>						
					</div>
					<div class="form-group">
						<label class="control-label col-xs-2">Usage Price</label>
						<div class="col-xs-3">
							<input type="number" id="price" min="0" title="Usage price if any" onChange="genClick();" tabindex="5">
						</div>
						<label class="control-label col-xs-2 pull-left">Lock User</label>
						<div class="col-xs-3 pull-left">
							<select class="myCombo" id="lock_user" title="Lock user to any single device at a time?" onChange="genClick();" required tabindex="6">
								<option></option>
								<option value="Enable">Enable</option>								
								<option value="Disable">Disable</option>
							</select>
						</div>
					</div>					
					<div class="form-group">
						<label class="control-label col-xs-2">Rate limit - Download(Rx)</label>
						<div class="col-xs-3">
							<select class="myCombo" id="rx_rate_limit" title="Select the maximum Download speed limit allowed for the profile from the list" onChange="genClick();"  required tabindex="7">
								<option></option>		
								<option value="256k">256 Kbps</option>
								<option value="512k">512 Kbps</option>
								<option value="1M">1 Mbps</option>
								<option value="2M">2 Mbps</option>
								<option value="3M">3 Mbps</option>
								<option value="4M">4 Mbps</option>
								<option value="5M">5 Mbps</option>
								<option value="6M">6 Mbps</option>
								<option value="7M">7 Mbps</option>
								<option value="8M">8 Mbps</option>
								<option value="10M">10 Mbps</option>
								<option value="25M">25 Mbps</option>
								<option value="50M">50 Mbps</option>
								<option value="100M">100 Mbps</option>
								<option value="500M">500 Mbps</option>
								<option value="800M">800 Mbps</option>
								<option value="1024M">1 Gbps</option>
								<option value="10240M">10 Gbps</option>
								<option value="20480M">20 Gbps</option>
								<option value="102400M">100 Gbps</option>
							</select>
						</div>
						<label class="control-label col-xs-2 pull-left">Rate limit - Upload(Tx)</label>
						<div class="col-xs-3 pull-left">
							<select class="myCombo" id="tx_rate_limit" title="Select the maximum Upload speed limit allowed for the profile from the list" onChange="genClick();" name="status" required tabindex="8">
								<option></option>		
								<option value="256k">256 Kbps</option>
								<option value="512k">512 Kbps</option>
								<option value="1M">1 Mbps</option>
								<option value="2M">2 Mbps</option>
								<option value="3M">3 Mbps</option>
								<option value="4M">4 Mbps</option>
								<option value="5M">5 Mbps</option>
								<option value="6M">6 Mbps</option>
								<option value="7M">7 Mbps</option>
								<option value="8M">8 Mbps</option>
								<option value="10M">10 Mbps</option>
								<option value="25M">25 Mbps</option>
								<option value="50M">50 Mbps</option>
								<option value="100M">100 Mbps</option>
								<option value="500M">500 Mbps</option>
								<option value="800M">800 Mbps</option>
								<option value="1024M">1 Gbps</option>
								<option value="10240M">10 Gbps</option>
								<option value="20480M">20 Gbps</option>
								<option value="102400M">100 Gbps</option>
							</select>
						</div>
					</div>

					<div class="form-group">
						<label class="control-label col-xs-2">Shared Users</label>
						<div class="col-xs-3">
							<input type="number" id="shared_users" title="Select No of users allowed to share a connection ( 1- 5 )" min=1  max=5 onChange="genClick();" tabindex="9">
						</div>
						<label class="control-label col-xs-2">Session Timeout</label>
						<div class="col-xs-3 pull-left">
							<input type="text" id="session_timeout" title="Session Timeout Value in the format 3d 00:00:00, Give 00:00:00 or none for No Limits" onChange="genClick();" tabindex="10" >
						</div>						
					</div>
					<div class="form-group">
						<label class="control-label col-xs-2">MAC Cookie Timeout</label>
						<div class="col-xs-3">
							<input type="text" id="mac_cookie_timeout" size="12" title="MAC Cookie Timeout Value in the format 1d 00:00:00" onChange="genClick();" tabindex="11">
						</div>
						<label class="control-label col-xs-2 pull-left">Keep Alive Timeout</label>
						<div class="col-xs-3 pull-left">
							<input type="text" id="keepalive_timeout" size="12" title="Keepalive Timeout Value in the format 00:00:00" onChange="genClick();" tabindex="12">
						</div>
					</div>
				</div>
				<div class="modal-footer">
					<div class="col-sm-10 col-sm-offset-1">
						<?php
						echo '<button name="add_profile" id="add_profile" onClick="addprofile(this.form);" class="btn btn-info" data-dismiss="modal" tabindex="13"><span class="glyphicon glyphicon-plus" aria-hidden="true"></span>Add New</button>';
						echo '<button name="edit_profile" id="edit_profile" onChange="genClick();" onClick="editprofile(this.form);" class="btn btn-success" data-dismiss="modal" tabindex="14"><i class="fa fa-pencil-square-o" aria-hidden="true"></i>Update</button>';
						echo '<button name="delete_profile" id="delete_profile" onClick="deleteprofile(this.form);" class="btn btn-danger" data-dismiss="modal" tabindex="15"><i class="fa fa-trash" aria-hidden="true"></i>Delete Profile</button>';
						echo '<button name="close_btn" id="close_btn" class="btn btn-warning" data-dismiss="modal" aria-hidden="true" tabindex="16"><i class="fa fa-times" aria-hidden="true"></i>Close</button>';
						?>
					</div>
				</div>
			</form>
		</div>	
	</div>
</div>

File: /modal_get_user.php
<div id="getUserModal" class="child-modal modal fade" tabindex="-1" role="dialog" aria-hidden="true">
	<div class="modal-dialog">
		<div class="modal-content">	
			<form class="form-horizontal" method="post">
				<div class="modal-body">
					<div class="alert alert-info text-center"><strong>Edit System User</strong></div>
					<div class="form-group">
						<label class="control-label col-xs-3">Username</label>
						<div class="col-xs-7">
							<div class="input-group">
								<span class="input-group-addon"><i class="fa fa-envelope-o fa-fw"></i></span>
								<input type="hidden" id="user_id" name="id" >
								<input type="text" id="username" size="40" onChange="genClick();" name="username" required tabindex="1" autofocus>
							</div>
						</div>	
					</div>
					<div class="form-group">
						<label class="control-label col-xs-3">Firstname</label>
						<div class="col-xs-7">
							<input type="text" id="firstname" onChange="genClick();" name="firstname"  required tabindex="2">
						</div>
					</div>
					<div class="form-group">
						<label class="control-label col-xs-3">Lastname</label>
						<div class="col-xs-7">
							<input type="text" id="lastname" onChange="genClick();" name="lastname" tabindex="3">
						</div>
					</div>
					<div class="form-group">
						<label class="control-label col-xs-3">User Level</label>
						<div class="col-xs-7">
							<select id="user_level" onChange="genClick();" name="user_level" required tabindex="4">
								<?php
								switch ($row['user_level']) {
									case 1 :
										echo '<option value="1">Administrator</option>';
										break;
									case 2 :
										echo '<option value="2">Unit Head</option>';
										break;
									case 3 :
										echo '<option value="3">System User</option>';
										break;
								} ?>
								<option value="3">System User</option>
								<option value="2">Unit Head</option>
								<option value="1">Administrator</option>
							</select>
						</div>
					</div>
					<div class="form-group">
						<label class="control-label col-xs-3">User Status</label>
						<div class="col-xs-3">
							<select class="myCombo" id="status" onChange="genClick();" name="user_status" required tabindex="5">
								<option></option>		
								<option value="Active">Active</option>
								<option value="Disabled">Disabled</option>
							</select>
						</div>
					</div>
				</div>
				<div class="modal-footer">
					<div class="col-sm-12">
						<?php
						echo '<button name="add_user" id="add_user" onClick="addsysuser(this.form)" class="btn btn-primary" data-dismiss="modal"><i class="icon-save icon-large"></i>Add User</button>';
						echo '<button name="edit_user" id="edit_user" onChange="genClick();" onClick="edituser(this.form);" class="btn btn-success" data-dismiss="modal" tabindex="6"><i class="fa fa-pencil-square-o" aria-hidden="true"></i>Update</button>';
						echo '<button name="delete_user" id="delete_user" onClick="deleteuser(this.form);" class="btn btn-danger" data-dismiss="modal" tabindex="7"><i class="fa fa-trash" aria-hidden="true"></i>Remove User</button>';
						echo '<button name="reset_psd" id="reset_psd" onClick="resetpass(this.form);" class="btn btn-info" data-dismiss="modal" tabindex="8"><i class="fa fa-bolt" aria-hidden="true"></i>Reset Pass</button>';
						echo '<button name="close_button" id="close_button" class="btn btn-warning" data-dismiss="modal" aria-hidden="true" tabindex="9"><i class="fa fa-times" aria-hidden="true"></i>Close</button>';
						?>
					</div>
				</div>
			</form>
		</div>	
	</div>
</div>

File: /PEAR2\Autoload.php
<?php
namespace PEAR2;
if (!class_exists('\PEAR2\Autoload', false)) {
    class Autoload
    {
        /**
         * Whether the autoload class has been spl_autoload_register-ed
         * 
         * @var bool
         */
        protected static $registered = false;

        /**
         * Array of PEAR2 autoload paths registered
         * 
         * @var array
         */
        protected static $paths = array();
        
        /**
         * Array of classname-to-file mapping
         *
         * @var array
         */
        protected static $map = array();

        /**
         * Array of class maps loaded
         *
         * @var array
         */
        protected static $maps = array();

        /**
         * Last classmap specified
         *
         * @var array
         */
        protected static $mapfile = null;

        /**
         * Array of classes loaded automatically not in the map
         *
         * @var array
         */
        protected static $unmapped = array();

        /**
         * Initialize the PEAR2 autoloader
         * 
         * @param string $path Directory path to register
         * 
         * @return void
         */
        static function initialize($path, $mapfile = null)
        {
            self::register();
            self::addPath($path);
            self::addMap($mapfile);
        }

        /**
         * Register the PEAR2 autoload class with spl_autoload_register
         * 
         * @return void
         */
        protected static function register()
        {
            if (!self::$registered) {
                // set up __autoload
                $autoload = spl_autoload_functions();
                spl_autoload_register('PEAR2\Autoload::load');
                if (function_exists('__autoload') && ($autoload === false)) {
                    // __autoload() was being used, but now would be ignored, add
                    // it to the autoload stack
                    spl_autoload_register('__autoload');
                }
            }
            self::$registered = true;
        }

        /**
         * Add a path
         * 
         * @param string $path The directory to add to the set of PEAR2 paths
         * 
         * @return void
         */
        protected static function addPath($path)
        {
            if (!in_array($path, self::$paths)) {
                self::$paths[] = $path;
            }
        }

        /**
         * Add a classname-to-file map
         *
         * @param string $mapfile The filename of the classmap
         *
         * @return void
         */
        protected static function addMap($mapfile)
        {
            if (! in_array($mapfile, self::$maps)) {
                
                // keep track of specific map file loaded in this
                // instance so we can update it if necessary                
                self::$mapfile = $mapfile;
                
                if (file_exists($mapfile)) {
                    $map = include $mapfile;
                    if (is_array($map)) {
                        // mapfile contains a valid map, so we'll keep it
                        self::$maps[] = $mapfile;                        
                        self::$map = array_merge(self::$map, $map);
                    }
                }
                
            }
        }

        /**
         * Check if the class is already defined in a classmap
         * 
         * @param string $class The class to look for
         * 
         * @return bool
         */
        protected static function isMapped($class)
        {
            if (isset(self::$map[$class])) {
                return true;
            }
            if (isset(self::$mapfile) && ! isset(self::$map[$class])) {
                self::$unmapped[] = $class;
                return false;
            }
            return false;
        }

        /**
         * Load a PEAR2 class
         * 
         * @param string $class The class to load
         * 
         * @return bool
         */
        static function load($class)
        {
            // need to check if there's a current map file specified ALSO.
            // this could be the first time writing it.
            $mapped = self::isMapped($class);
            if ($mapped) {
                require self::$map[$class];
                if (!self::loadSuccessful($class)) {
                    // record this failure & keep going, we may still find it
                    self::$unmapped[] = $class;
                } else {
                    return true;
                }
            }

            $file = str_replace(array('_', '\\'), DIRECTORY_SEPARATOR, $class) . '.php';
            foreach (self::$paths as $path) {
                if (file_exists($path . DIRECTORY_SEPARATOR . $file)) {
                    require $path . DIRECTORY_SEPARATOR . $file;
                    if (!self::loadSuccessful($class)) {
                        throw new \Exception('Class ' . $class . ' was not present in ' .
                            $path . DIRECTORY_SEPARATOR . $file .
                            '") [PEAR2_Autoload-0.2.4]');
                    }
                    
                    if (in_array($class, self::$unmapped)) {
                        self::updateMap($class, $path . DIRECTORY_SEPARATOR . $file);
                    }
                    return true;
                }
            }
            
            $e = new \Exception('Class ' . $class . ' could not be loaded from ' .
                $file . ', file does not exist (registered paths="' .
                implode(PATH_SEPARATOR, self::$paths) .
                '") [PEAR2_Autoload-0.2.4]');
            $trace = $e->getTrace();
            if (isset($trace[2]) && isset($trace[2]['function']) &&
                  in_array($trace[2]['function'], array('class_exists', 'interface_exists'))) {
                return false;
            }
            if (isset($trace[1]) && isset($trace[1]['function']) &&
                  in_array($trace[1]['function'], array('class_exists', 'interface_exists'))) {
                return false;
            }
            throw $e;
        }

        /**
         * Check if the requested class was loaded from the specified path
         * 
         * @return bool
         */
        protected static function loadSuccessful($class)
        {
            if (!class_exists($class, false) && !interface_exists($class, false)) {
                return false;
            }
            return true;
        }
        
        /**
         * If possible, update the classmap file with newly-discovered 
         * mapping.
         * 
         * @param string $class Class name discovered
         * 
         * @param string $origin File where class was found
         * 
         */
        protected static function updateMap($class, $origin)
        {
            if (is_writable(self::$mapfile) || is_writable(dirname(self::$mapfile))) {
                self::$map[$class] = $origin;
                file_put_contents(self::$mapfile, 
                    '<'."?php\n"
                    . "// PEAR2\Autoload auto-generated classmap\n"
                    . "return " . var_export(self::$map, true) . ';',
                    LOCK_EX
                );
            }
        }
        
        /**
         * return the array of paths PEAR2 autoload has registered
         * 
         * @return array
         */
        static function getPaths()
        {
            return self::$paths;
        }
    }
}
Autoload::initialize(dirname(__DIR__));

File: /PEAR2\Cache\SHM\Adapter\APC.php
<?php

/**
 * ~~summary~~
 * 
 * ~~description~~
 * 
 * PHP version 5
 * 
 * @category  Caching
 * @package   PEAR2_Cache_SHM
 * @author    Vasil Rangelov <boen.robot@gmail.com>
 * @copyright 2011 Vasil Rangelov
 * @license   http://www.gnu.org/copyleft/lesser.html LGPL License 2.1
 * @version   0.1.3
 * @link      http://pear2.php.net/PEAR2_Cache_SHM
 */
/**
 * The namespace declaration.
 */
namespace PEAR2\Cache\SHM\Adapter;

/**
 * Throws exceptions from this namespace, and extends from this class.
 */
use PEAR2\Cache\SHM;

/**
 * {@link APC::getIterator()} returns this object.
 */
use ArrayObject;

/**
 * Shared memory adapter for the APC extension.
 * 
 * @category Caching
 * @package  PEAR2_Cache_SHM
 * @author   Vasil Rangelov <boen.robot@gmail.com>
 * @license  http://www.gnu.org/copyleft/lesser.html LGPL License 2.1
 * @link     http://pear2.php.net/PEAR2_Cache_SHM
 */
class APC extends SHM
{
    /**
     * @var string ID of the current storage. 
     */
    protected $persistentId;
    
    /**
     * List of persistent IDs.
     * 
     * A list of persistent IDs within the current request (as keys) with an int
     * (as a value) specifying the number of instances in the current request.
     * Used as an attempt to ensure implicit lock releases even on errors in the
     * critical sections, since APC doesn't have an actual locking function.
     * @var array 
     */
    protected static $requestInstances = array();
    
    /**
     * @var array Array of lock names (as values) for each persistent ID (as
     *     key) obtained during the current request.
     */
    protected static $locksBackup = array();

    /**
     * Creates a new shared memory storage.
     * 
     * Estabilishes a separate persistent storage.
     * 
     * @param string $persistentId The ID for the storage. The storage will be
     *     reused if it exists, or created if it doesn't exist. Data and locks
     *     are namespaced by this ID.
     */
    public function __construct($persistentId)
    {
        $this->persistentId = __CLASS__ . ' ' . $persistentId;
        if (isset(static::$requestInstances[$this->persistentId])) {
            static::$requestInstances[$this->persistentId]++;
        } else {
            static::$requestInstances[$this->persistentId] = 1;
            static::$locksBackup[$this->persistentId] = array();
        }
        register_shutdown_function(
            get_called_class() . '::releaseLocks',
            $this->persistentId,
            true
        );
    }
    
    /**
     * Checks if the adapter meets its requirements.
     * 
     * @return bool TRUE on success, FALSE on failure.
     */
    public static function isMeetingRequirements()
    {
        return extension_loaded('apc')
            && version_compare(phpversion('apc'), '3.0.13', '>=')
            && ini_get('apc.enabled')
            && ('cli' !== PHP_SAPI || ini_get('apc.enable_cli'));
    }
    
    /**
     * Releases all locks in a storage.
     * 
     * This function is not meant to be used directly. It is implicitly called
     * by the the destructor and as a shutdown function when the request ends.
     * One of these calls ends up releasing any unreleased locks obtained
     * during the request. A lock is also implicitly released as soon as there
     * are no objects left in the current request using the same persistent ID.
     * 
     * @param string $internalPersistentId The internal persistent ID, the locks
     *     of which are being released.
     * @param bool   $isAtShutdown         Whether the function was executed at
     *     shutdown.
     * 
     * @return void
     * @internal
     */
    public static function releaseLocks($internalPersistentId, $isAtShutdown)
    {
        $hasInstances = 0 !== static::$requestInstances[$internalPersistentId];
        if ($isAtShutdown === $hasInstances) {
            foreach (static::$locksBackup[$internalPersistentId] as $key) {
                apc_delete($internalPersistentId . 'l ' . $key);
            }
        }
    }
    
    /**
     * Releases any locks obtained by this instance as soon as there are no more
     * references to the object's persistent ID.
     */
    public function __destruct()
    {
        static::$requestInstances[$this->persistentId]--;
        static::releaseLocks($this->persistentId, false);
    }
    
    
    /**
     * Obtains a named lock.
     * 
     * @param string $key     Name of the key to obtain. Note that $key may
     *     repeat for each distinct $persistentId.
     * @param double $timeout If the lock can't be immediatly obtained, the
     *     script will block for at most the specified amount of seconds.
     *     Setting this to 0 makes lock obtaining non blocking, and setting it
     *     to NULL makes it block without a time limit.
     * 
     * @return bool TRUE on success, FALSE on failure.
     */
    public function lock($key, $timeout = null)
    {
        $lock = $this->persistentId . 'l ' . $key;
        $hasTimeout = $timeout !== null;
        $start = microtime(true);
        while (!apc_add($lock, 1)) {
            if ($hasTimeout && (microtime(true) - $start) > $timeout) {
                return false;
            }
        }
        static::$locksBackup[$this->persistentId] = $key;
        return true;
    }
    
    /**
     * Releases a named lock.
     * 
     * @param string $key Name of the key to release. Note that $key may
     *     repeat for each distinct $persistentId.
     * 
     * @return bool TRUE on success, FALSE on failure.
     */
    public function unlock($key)
    {
        $lock = $this->persistentId . 'l ' . $key;
        $success = apc_delete($lock);
        if ($success) {
            unset(static::$locksBackup[$this->persistentId][array_search(
                $key,
                static::$locksBackup[$this->persistentId],
                true
            )]);
            return true;
        }
        return false;
    }
    
    /**
     * Checks if a specified key is in the storage.
     * 
     * @param string $key Name of key to check.
     * 
     * @return bool TRUE if the key is in the storage, FALSE otherwise. 
     */
    public function exists($key)
    {
        return apc_exists($this->persistentId . 'd ' . $key);
    }
    
    /**
     * Adds a value to the shared memory storage.
     * 
     * Adds a value to the storage if it doesn't exist, or fails if it does.
     * 
     * @param string $key   Name of key to associate the value with.
     * @param mixed  $value Value for the specified key.
     * @param int    $ttl   Seconds to store the value. If set to 0 indicates no
     *     time limit.
     * 
     * @return bool TRUE on success, FALSE on failure.
     */
    public function add($key, $value, $ttl = 0)
    {
        return apc_add($this->persistentId . 'd ' . $key, $value, $ttl);
    }
    
    /**
     * Sets a value in the shared memory storage.
     * 
     * Adds a value to the storage if it doesn't exist, overwrites it otherwise.
     * 
     * @param string $key   Name of key to associate the value with.
     * @param mixed  $value Value for the specified key.
     * @param int    $ttl   Seconds to store the value. If set to 0 indicates no
     *     time limit.
     * 
     * @return bool TRUE on success, FALSE on failure.
     */
    public function set($key, $value, $ttl = 0)
    {
        return apc_store($this->persistentId . 'd ' . $key, $value, $ttl);
    }
    
    /**
     * Gets a value from the shared memory storage.
     * 
     * Gets the current value, or throws an exception if it's not stored.
     * 
     * @param string $key Name of key to get the value of.
     * 
     * @return mixed The current value of the specified key.
     */
    public function get($key)
    {
        $fullKey = $this->persistentId . 'd ' . $key;
        if (apc_exists($fullKey)) {
            $value = apc_fetch($fullKey, $success);
            if (!$success) {
                throw new SHM\InvalidArgumentException(
                    'Unable to fetch key. ' .
                    'Key has either just now expired or (if no TTL was set) ' .
                    'is possibly in a race condition with another request.',
                    100
                );
            }
            return $value;
        }
        throw new SHM\InvalidArgumentException('No such key in cache', 101);
    }
    
    /**
     * Deletes a value from the shared memory storage.
     * 
     * @param string $key Name of key to delete.
     * 
     * @return bool TRUE on success, FALSE on failure.
     */
    public function delete($key)
    {
        return apc_delete($this->persistentId . 'd ' . $key);
    }
    
    /**
     * Increases a value from the shared memory storage.
     * 
     * Increases a value from the shared memory storage. Unlike a plain
     * set($key, get($key)+$step) combination, this function also implicitly
     * performs locking.
     * 
     * @param string $key  Name of key to increase.
     * @param int    $step Value to increase the key by.
     * 
     * @return int The new value.
     */
    public function inc($key, $step = 1)
    {
        $newValue = apc_inc(
            $this->persistentId . 'd ' . $key,
            (int) $step,
            $success
        );
        if (!$success) {
            throw new SHM\InvalidArgumentException(
                'Unable to increase the value. Are you sure the value is int?',
                102
            );
        }
        return $newValue;
    }
    
    /**
     * Decreases a value from the shared memory storage.
     * 
     * Decreases a value from the shared memory storage. Unlike a plain
     * set($key, get($key)-$step) combination, this function also implicitly
     * performs locking.
     * 
     * @param string $key  Name of key to decrease.
     * @param int    $step Value to decrease the key by.
     * 
     * @return int The new value.
     */
    public function dec($key, $step = 1)
    {
        $newValue = apc_dec(
            $this->persistentId . 'd ' . $key,
            (int) $step,
            $success
        );
        if (!$success) {
            throw new SHM\InvalidArgumentException(
                'Unable to decrease the value. Are you sure the value is int?',
                103
            );
        }
        return $newValue;
    }

    /**
     * Sets a new value if a key has a certain value.
     * 
     * Sets a new value if a key has a certain value. This function only works
     * when $old and $new are longs.
     * 
     * @param string $key Key of the value to compare and set.
     * @param int    $old The value to compare the key against.
     * @param int    $new The value to set the key to.
     * 
     * @return bool TRUE on success, FALSE on failure. 
     */
    public function cas($key, $old, $new)
    {
        return apc_cas($this->persistentId . 'd ' . $key, $old, $new);
    }
    
    /**
     * Clears the persistent storage.
     * 
     * Clears the persistent storage, i.e. removes all keys. Locks are left
     * intact.
     * 
     * @return void
     */
    public function clear()
    {
        foreach (new APCIterator(
            'user',
            '/^' . preg_quote($this->persistentId, '/') . 'd /',
            APC_ITER_KEY,
            100,
            APC_LIST_ACTIVE
        ) as $key) {
            apc_delete($key);
        }
    }
    
    /**
     * Retrieve an external iterator
     * 
     * Returns an external iterator.
     * 
     * @param string|null $filter   A PCRE regular expression.
     *     Only matching keys will be iterated over.
     *     Setting this to NULL matches all keys of this instance.
     * @param bool        $keysOnly Whether to return only the keys,
     *     or return both the keys and values.
     * 
     * @return ArrayObject An array with all matching keys as array keys,
     *     and values as array values. If $keysOnly is TRUE, the array keys are
     *     numeric, and the array values are key names.
     */
    public function getIterator($filter = null, $keysOnly = false)
    {
        $result = array();
        foreach (new APCIterator(
            'user',
            '/^' . preg_quote($this->persistentId, '/') . 'd /',
            APC_ITER_KEY,
            100,
            APC_LIST_ACTIVE
        ) as $key) {
            $localKey = strstr($key, $this->persistentId . 'd ');
            if (null === $filter || preg_match($filter, $localKey)) {
                if ($keysOnly) {
                    $result[] = $localKey;
                } else {
                    $result[$localKey] = apc_fetch($key);
                }
            }
        }
        return new ArrayObject($result);
    }
}


File: /PEAR2\Cache\SHM\Adapter\Placebo.php
<?php

/**
 * ~~summary~~
 * 
 * ~~description~~
 * 
 * PHP version 5
 * 
 * @category  Caching
 * @package   PEAR2_Cache_SHM
 * @author    Vasil Rangelov <boen.robot@gmail.com>
 * @copyright 2011 Vasil Rangelov
 * @license   http://www.gnu.org/copyleft/lesser.html LGPL License 2.1
 * @version   0.1.3
 * @link      http://pear2.php.net/PEAR2_Cache_SHM
 */
/**
 * The namespace declaration.
 */
namespace PEAR2\Cache\SHM\Adapter;

/**
 * Throws exceptions from this namespace, and extends from this class.
 */
use PEAR2\Cache\SHM;

/**
 * {@link Placebo::getIterator()} returns this object.
 */
use ArrayObject;

/**
 * This adapter is not truly persistent. It is intended to emulate persistency
 * in non persistent environments, so that upper level applications can use a
 * single code path for persistent and non persistent code.
 * 
 * @category Caching
 * @package  PEAR2_Cache_SHM
 * @author   Vasil Rangelov <boen.robot@gmail.com>
 * @license  http://www.gnu.org/copyleft/lesser.html LGPL License 2.1
 * @link     http://pear2.php.net/PEAR2_Cache_SHM
 */
class Placebo extends SHM
{
    /**
     * @var string ID of the current storage. 
     */
    protected $persistentId;
    
    /**
     * List of persistent IDs.
     * 
     * A list of persistent IDs within the current request (as keys) with an int
     * (as a value) specifying the number of instances in the current request.
     * Used as an attempt to ensure implicit lock releases on destruction.
     * @var array 
     */
    protected static $requestInstances = array();
    
    /**
     * @var array Array of lock names (as values) for each persistent ID (as
     *     key) obtained during the current request.
     */
    protected static $locksBackup = array();
    
    /**
     * The data storage.
     * 
     * Each persistent ID is a key, and the value is an array.
     * Each such array has data keys as its keys, and an array as a value.
     * Each such array has as its elements the value, the timeout and the time
     * the data was set.
     * @var array 
     */
    protected static $data = array();
    
    /**
     * Creates a new shared memory storage.
     * 
     * Estabilishes a separate persistent storage.
     * 
     * @param string $persistentId The ID for the storage. The storage will be
     *     reused if it exists, or created if it doesn't exist. Data and locks
     *     are namespaced by this ID.
     */
    public function __construct($persistentId)
    {
        if (isset(static::$requestInstances[$persistentId])) {
            ++static::$requestInstances[$persistentId];
        } else {
            static::$requestInstances[$persistentId] = 1;
            static::$locksBackup[$persistentId] = array();
            static::$data[$persistentId] = array();
        }
        $this->persistentId = $persistentId;
    }
    
    /**
     * Releases any unreleased locks. 
     */
    public function __destruct()
    {
        if (0 === --static::$requestInstances[$this->persistentId]) {
            static::$locksBackup[$this->persistentId] = array();
        }
    }
    
    /**
     * Checks if the adapter meets its requirements.
     * 
     * @return bool TRUE on success, FALSE on failure.
     */
    public static function isMeetingRequirements()
    {
        return 'cli' === PHP_SAPI;
    }
    
    /**
     * Pretends to obtain a lock.
     * 
     * @param string $key     Ignored.
     * @param double $timeout Ignored.
     * 
     * @return bool TRUE on success, FALSE on failure.
     */
    public function lock($key, $timeout = null)
    {
        $key = (string) $key;
        if (in_array($key, static::$locksBackup[$this->persistentId], true)) {
            return false;
        }
        static::$locksBackup[$this->persistentId][] = $key;
        return true;
    }
    
    /**
     * Pretends to release a lock.
     * 
     * @param string $key Ignored
     * 
     * @return bool TRUE on success, FALSE on failure.
     */
    public function unlock($key)
    {
        $key = (string) $key;
        if (!in_array($key, static::$locksBackup[$this->persistentId], true)) {
            return false;
        }
        unset(static::$locksBackup[$this->persistentId][array_search(
            $key,
            static::$locksBackup[$this->persistentId],
            true
        )]);
        return true;
    }
    
    /**
     * Checks if a specified key is in the storage.
     * 
     * @param string $key Name of key to check.
     * 
     * @return bool TRUE if the key is in the storage, FALSE otherwise. 
     */
    public function exists($key)
    {
        return array_key_exists($key, static::$data[$this->persistentId]);
    }
    
    /**
     * Adds a value to the shared memory storage.
     * 
     * Adds a value to the storage if it doesn't exist, or fails if it does.
     * 
     * @param string $key   Name of key to associate the value with.
     * @param mixed  $value Value for the specified key.
     * @param int    $ttl   Because "true" adapters purge the cache at the next
     *     request, this setting is ignored.
     * 
     * @return bool TRUE on success, FALSE on failure.
     */
    public function add($key, $value, $ttl = 0)
    {
        if ($this->exists($key)) {
            return false;
        }
        return $this->set($key, $value, $ttl);
    }
    
    /**
     * Sets a value in the shared memory storage.
     * 
     * Adds a value to the storage if it doesn't exist, overwrites it otherwise.
     * 
     * @param string $key   Name of key to associate the value with.
     * @param mixed  $value Value for the specified key.
     * @param int    $ttl   Because "true" adapters purge the cache at the next
     *     request, this setting is ignored.
     * 
     * @return bool TRUE on success, FALSE on failure.
     */
    public function set($key, $value, $ttl = 0)
    {
        static::$data[$this->persistentId][$key] = $value;
        return true;
    }
    
    /**
     * Gets a value from the shared memory storage.
     * 
     * Gets the current value, or throws an exception if it's not stored.
     * 
     * @param string $key Name of key to get the value of.
     * 
     * @return mixed The current value of the specified key.
     */
    public function get($key)
    {
        if ($this->exists($key)) {
            return static::$data[$this->persistentId][$key];
        }
        throw new SHM\InvalidArgumentException(
            'Unable to fetch key. No such key.',
            200
        );
    }
    
    /**
     * Deletes a value from the shared memory storage.
     * 
     * @param string $key Name of key to delete.
     * 
     * @return bool TRUE on success, FALSE on failure.
     */
    public function delete($key)
    {
        if ($this->exists($key)) {
            unset(static::$data[$this->persistentId][$key]);
            return true;
        }
        return false;
    }
    
    /**
     * Increases a value from the shared memory storage.
     * 
     * Increases a value from the shared memory storage. Unlike a plain
     * set($key, get($key)+$step) combination, this function also implicitly
     * performs locking.
     * 
     * @param string $key  Name of key to increase.
     * @param int    $step Value to increase the key by.
     * 
     * @return int The new value.
     */
    public function inc($key, $step = 1)
    {
        if (!$this->exists($key) || !is_int($value = $this->get($key))
            || !$this->set($key, $value + (int) $step)
        ) {
            throw new SHM\InvalidArgumentException(
                'Unable to increase the value. Are you sure the value is int?',
                201
            );
        }
        return $this->get($key);
    }
    
    /**
     * Decreases a value from the shared memory storage.
     * 
     * Decreases a value from the shared memory storage. Unlike a plain
     * set($key, get($key)-$step) combination, this function also implicitly
     * performs locking.
     * 
     * @param string $key  Name of key to decrease.
     * @param int    $step Value to decrease the key by.
     * 
     * @return int The new value.
     */
    public function dec($key, $step = 1)
    {
        if (!$this->exists($key) || !is_int($value = $this->get($key))
            || !$this->set($key, $value - (int) $step)
        ) {
            throw new SHM\InvalidArgumentException(
                'Unable to increase the value. Are you sure the value is int?',
                202
            );
        }
        return $this->get($key);
    }

    /**
     * Sets a new value if a key has a certain value.
     * 
     * Sets a new value if a key has a certain value. This function only works
     * when $old and $new are longs.
     * 
     * @param string $key Key of the value to compare and set.
     * @param int    $old The value to compare the key against.
     * @param int    $new The value to set the key to.
     * 
     * @return bool TRUE on success, FALSE on failure. 
     */
    public function cas($key, $old, $new)
    {
        return $this->exists($key) && ($this->get($key) === $old)
            && is_int($new) && $this->set($key, $new);
    }
    
    /**
     * Clears the persistent storage.
     * 
     * Clears the persistent storage, i.e. removes all keys. Locks are left
     * intact.
     * 
     * @return void
     */
    public function clear()
    {
        static::$data[$this->persistentId] = array();
    }
    
    /**
     * Retrieve an external iterator
     * 
     * Returns an external iterator.
     * 
     * @param string|null $filter   A PCRE regular expression.
     *     Only matching keys will be iterated over.
     *     Setting this to NULL matches all keys of this instance.
     * @param bool        $keysOnly Whether to return only the keys,
     *     or return both the keys and values.
     * 
     * @return ArrayObject An array with all matching keys as array keys,
     *     and values as array values. If $keysOnly is TRUE, the array keys are
     *     numeric, and the array values are key names.
     */
    public function getIterator($filter = null, $keysOnly = false)
    {
        if (null === $filter) {
            return new ArrayObject(
                $keysOnly
                ? array_keys(static::$data[$this->persistentId])
                : static::$data[$this->persistentId]
            );
        }
        
        $result = array();
        foreach (static::$data[$this->persistentId] as $key => $value) {
            if (preg_match($filter, $key)) {
                $result[$key] = $value;
            }
        }
        return new ArrayObject($keysOnly ? array_keys($result) : $result);
    }
}


File: /PEAR2\Cache\SHM\Adapter\Wincache.php
<?php

/**
 * ~~summary~~
 * 
 * ~~description~~
 * 
 * PHP version 5
 * 
 * @category  Caching
 * @package   PEAR2_Cache_SHM
 * @author    Vasil Rangelov <boen.robot@gmail.com>
 * @copyright 2011 Vasil Rangelov
 * @license   http://www.gnu.org/copyleft/lesser.html LGPL License 2.1
 * @version   0.1.3
 * @link      http://pear2.php.net/PEAR2_Cache_SHM
 */
/**
 * The namespace declaration.
 */
namespace PEAR2\Cache\SHM\Adapter;

/**
 * Throws exceptions from this namespace, and extends from this class.
 */
use PEAR2\Cache\SHM;

/**
 * {@link Wincache::getIterator()} returns this object.
 */
use ArrayObject;

/**
 * Shared memory adapter for the WinCache extension.
 * 
 * @category Caching
 * @package  PEAR2_Cache_SHM
 * @author   Vasil Rangelov <boen.robot@gmail.com>
 * @license  http://www.gnu.org/copyleft/lesser.html LGPL License 2.1
 * @link     http://pear2.php.net/PEAR2_Cache_SHM
 */
class Wincache extends SHM
{
    /**
     * @var string ID of the current storage. 
     */
    protected $persistentId;
    
    /**
     * List of persistent IDs.
     * 
     * A list of persistent IDs within the current request (as keys) with an int
     * (as a value) specifying the number of instances in the current request.
     * Used as an attempt to ensure implicit lock releases on destruction.
     * @var array 
     */
    protected static $requestInstances = array();
    
    /**
     * @var array Array of lock names obtained during the current request.
     */
    protected static $locksBackup = array();
    
    /**
     * Creates a new shared memory storage.
     * 
     * Estabilishes a separate persistent storage.
     * 
     * @param string $persistentId The ID for the storage. The storage will be
     *     reused if it exists, or created if it doesn't exist. Data and locks
     *     are namespaced by this ID.
     */
    public function __construct($persistentId)
    {
        $this->persistentId
            = static::encodeLockName(__CLASS__ . ' ' . $persistentId) . ' ';
        if (isset(static::$requestInstances[$this->persistentId])) {
            static::$requestInstances[$this->persistentId]++;
        } else {
            static::$requestInstances[$this->persistentId] = 1;
            static::$locksBackup[$this->persistentId] = array();
        }
    }
    
    /**
     * Encodes a lock name
     * 
     * Encodes a lock name, so that it can be properly obtained. The scheme used
     * is a subset of URL encoding, with only the "%" and "\" characters being
     * escaped. The encoding itself is necessary, since lock names can't contain
     * the "\" character.
     * 
     * @param string $name The lock name to encode.
     * 
     * @return string The encoded name.
     * @link http://msdn.microsoft.com/en-us/library/ms682411(VS.85).aspx
     */
    protected static function encodeLockName($name)
    {
        return str_replace(array('%', '\\'), array('%25', '%5C'), $name);
    }
    
    /**
     * Checks if the adapter meets its requirements.
     * 
     * @return bool TRUE on success, FALSE on failure.
     */
    public static function isMeetingRequirements()
    {
        return extension_loaded('wincache')
            && version_compare(phpversion('wincache'), '1.1.0', '>=')
            && ini_get('wincache.ucenabled')
            && ('cli' !== PHP_SAPI || ini_get('wincache.enablecli'));
    }
    
    /**
     * Releases any locks obtained by this instance as soon as there are no more
     * references to the object's persistent ID.
     */
    public function __destruct()
    {
        if (0 === --static::$requestInstances[$this->persistentId]) {
            foreach (static::$locksBackup[$this->persistentId] as $key) {
                wincache_unlock(
                    $this->persistentId . static::encodeLockName($key)
                );
            }
        }
    }

    
    /**
     * Obtains a named lock.
     * 
     * @param string $key     Name of the key to obtain. Note that $key may
     *     repeat for each distinct $persistentId.
     * @param double $timeout Ignored with WinCache. Script will always block if
     *     the lock can't be immediatly obtained.
     * 
     * @return bool TRUE on success, FALSE on failure.
     */
    public function lock($key, $timeout = null)
    {
        $result = wincache_lock(
            $this->persistentId . static::encodeLockName($key)
        );
        if ($result) {
            static::$locksBackup[$this->persistentId] = $key;
        }
        return $result;
    }
    
    /**
     * Releases a named lock.
     * 
     * @param string $key Name of the key to release. Note that $key may
     *     repeat for each distinct $persistentId.
     * 
     * @return bool TRUE on success, FALSE on failure.
     */
    public function unlock($key)
    {
        $result = wincache_unlock(
            $this->persistentId . static::encodeLockName($key)
        );
        if ($result) {
            unset(static::$locksBackup[$this->persistentId][array_search(
                $key,
                static::$locksBackup[$this->persistentId],
                true
            )]);
        }
        return $result;
    }
    
    /**
     * Checks if a specified key is in the storage.
     * 
     * @param string $key Name of key to check.
     * 
     * @return bool TRUE if the key is in the storage, FALSE otherwise. 
     */
    public function exists($key)
    {
        return wincache_ucache_exists($this->persistentId . $key);
    }
    
    /**
     * Adds a value to the shared memory storage.
     * 
     * Sets a value to the storage if it doesn't exist, or fails if it does.
     * 
     * @param string $key   Name of key to associate the value with.
     * @param mixed  $value Value for the specified key.
     * @param int    $ttl   Seconds to store the value. If set to 0 indicates no
     *     time limit.
     * 
     * @return bool TRUE on success, FALSE on failure.
     */
    public function add($key, $value, $ttl = 0)
    {
        return wincache_ucache_add($this->persistentId . $key, $value, $ttl);
    }
    
    /**
     * Sets a value in the shared memory storage.
     * 
     * Adds a value to the storage if it doesn't exist, overwrites it otherwise.
     * 
     * @param string $key   Name of key to associate the value with.
     * @param mixed  $value Value for the specified key.
     * @param int    $ttl   Seconds to store the value. If set to 0 indicates no
     *     time limit.
     * 
     * @return bool TRUE on success, FALSE on failure.
     */
    public function set($key, $value, $ttl = 0)
    {
        return wincache_ucache_set($this->persistentId . $key, $value, $ttl);
    }
    
    /**
     * Gets a value from the shared memory storage.
     * 
     * Gets the current value, or throws an exception if it's not stored.
     * 
     * @param string $key Name of key to get the value of.
     * 
     * @return mixed The current value of the specified key.
     */
    public function get($key)
    {
        $value = wincache_ucache_get($this->persistentId . $key, $success);
        if (!$success) {
            throw new SHM\InvalidArgumentException(
                'Unable to fetch key. No such key, or key has expired.',
                300
            );
        }
        return $value;
    }
    
    /**
     * Deletes a value from the shared memory storage.
     * 
     * @param string $key Name of key to delete.
     * 
     * @return bool TRUE on success, FALSE on failure.
     */
    public function delete($key)
    {
        return wincache_ucache_delete($this->persistentId . $key);
    }
    
    /**
     * Increases a value from the shared memory storage.
     * 
     * Increases a value from the shared memory storage. Unlike a plain
     * set($key, get($key)+$step) combination, this function also implicitly
     * performs locking.
     * 
     * @param string $key  Name of key to increase.
     * @param int    $step Value to increase the key by.
     * 
     * @return int The new value.
     */
    public function inc($key, $step = 1)
    {
        $newValue = wincache_ucache_inc(
            $this->persistentId . $key,
            (int) $step,
            $success
        );
        if (!$success) {
            throw new SHM\InvalidArgumentException(
                'Unable to increase the value. Are you sure the value is int?',
                301
            );
        }
        return $newValue;
    }
    
    /**
     * Decreases a value from the shared memory storage.
     * 
     * Decreases a value from the shared memory storage. Unlike a plain
     * set($key, get($key)-$step) combination, this function also implicitly
     * performs locking.
     * 
     * @param string $key  Name of key to decrease.
     * @param int    $step Value to decrease the key by.
     * 
     * @return int The new value.
     */
    public function dec($key, $step = 1)
    {
        $newValue = wincache_ucache_dec(
            $this->persistentId . $key,
            (int) $step,
            $success
        );
        if (!$success) {
            throw new SHM\InvalidArgumentException(
                'Unable to decrease the value. Are you sure the value is int?',
                302
            );
        }
        return $newValue;
    }

    /**
     * Sets a new value if a key has a certain value.
     * 
     * Sets a new value if a key has a certain value. This function only works
     * when $old and $new are longs.
     * 
     * @param string $key Key of the value to compare and set.
     * @param int    $old The value to compare the key against.
     * @param int    $new The value to set the key to.
     * 
     * @return bool TRUE on success, FALSE on failure. 
     */
    public function cas($key, $old, $new)
    {
        return wincache_ucache_cas($this->persistentId . $key, $old, $new);
    }
    
    /**
     * Clears the persistent storage.
     * 
     * Clears the persistent storage, i.e. removes all keys. Locks are left
     * intact.
     * 
     * @return void
     */
    public function clear()
    {
        $info = wincache_ucache_info();
        foreach ($info['ucache_entries'] as $entry) {
            if (!$entry['is_session']
                && 0 === strpos($entry['key_name'], $this->persistentId)
            ) {
                wincache_ucache_delete($entry['key_name']);
            }
        }
    }
    
    /**
     * Retrieve an external iterator
     * 
     * Returns an external iterator.
     * 
     * @param string|null $filter   A PCRE regular expression.
     *     Only matching keys will be iterated over.
     *     Setting this to NULL matches all keys of this instance.
     * @param bool        $keysOnly Whether to return only the keys,
     *     or return both the keys and values.
     * 
     * @return ArrayObject An array with all matching keys as array keys,
     *     and values as array values. If $keysOnly is TRUE, the array keys are
     *     numeric, and the array values are key names.
     */
    public function getIterator($filter = null, $keysOnly = false)
    {
        $info = wincache_ucache_info();
        $result = array();
        foreach ($info['ucache_entries'] as $entry) {
            if (!$entry['is_session']
                && 0 === strpos($entry['key_name'], $this->persistentId)
            ) {
                $localKey = strstr($entry['key_name'], $this->persistentId);
                if (null === $filter || preg_match($filter, $localKey)) {
                    if ($keysOnly) {
                        $result[] = $localKey;
                    } else {
                        $result[$localKey] = apc_fetch($localKey);
                    }
                }
            }
        }
        return new ArrayObject($result);
    }
}


File: /PEAR2\Cache\SHM\Exception.php
<?php

/**
 * ~~summary~~
 * 
 * ~~description~~
 * 
 * PHP version 5
 * 
 * @category  Caching
 * @package   PEAR2_Cache_SHM
 * @author    Vasil Rangelov <boen.robot@gmail.com>
 * @copyright 2011 Vasil Rangelov
 * @license   http://www.gnu.org/copyleft/lesser.html LGPL License 2.1
 * @version   0.1.3
 * @link      http://pear2.php.net/PEAR2_Cache_SHM
 */
/**
 * The namespace declaration.
 */
namespace PEAR2\Cache\SHM;

/**
 * Generic exception class of this package.
 * 
 * @category Caching
 * @package  PEAR2_Cache_SHM
 * @author   Vasil Rangelov <boen.robot@gmail.com>
 * @license  http://www.gnu.org/copyleft/lesser.html LGPL License 2.1
 * @link     http://pear2.php.net/PEAR2_Cache_SHM
 */
interface Exception
{
}


File: /PEAR2\Cache\SHM\InvalidArgumentException.php
<?php

/**
 * ~~summary~~
 * 
 * ~~description~~
 * 
 * PHP version 5
 * 
 * @category  Caching
 * @package   PEAR2_Cache_SHM
 * @author    Vasil Rangelov <boen.robot@gmail.com>
 * @copyright 2011 Vasil Rangelov
 * @license   http://www.gnu.org/copyleft/lesser.html LGPL License 2.1
 * @version   0.1.3
 * @link      http://pear2.php.net/PEAR2_Cache_SHM
 */
/**
 * The namespace declaration.
 */
namespace PEAR2\Cache\SHM;

/**
 * Exception thrown when there's something wrong with an argument.
 * 
 * @category Caching
 * @package  PEAR2_Cache_SHM
 * @author   Vasil Rangelov <boen.robot@gmail.com>
 * @license  http://www.gnu.org/copyleft/lesser.html LGPL License 2.1
 * @link     http://pear2.php.net/PEAR2_Cache_SHM
 */
class InvalidArgumentException extends \InvalidArgumentException
    implements Exception
{
}


File: /PEAR2\Cache\SHM.php
<?php

/**
 * ~~summary~~
 * 
 * ~~description~~
 * 
 * PHP version 5
 * 
 * @category  Caching
 * @package   PEAR2_Cache_SHM
 * @author    Vasil Rangelov <boen.robot@gmail.com>
 * @copyright 2011 Vasil Rangelov
 * @license   http://www.gnu.org/copyleft/lesser.html LGPL License 2.1
 * @version   0.1.3
 * @link      http://pear2.php.net/PEAR2_Cache_SHM
 */

/**
 * The namespace declaration.
 */
namespace PEAR2\Cache;

/**
 * Used as a catch-all for adapter initialization.
 */
use Exception as E;

/**
 * Implements this class.
 */
use IteratorAggregate;

/**
 * Used on failures by this class.
 */
use PEAR2\Cache\SHM\InvalidArgumentException;

/**
 * Main class for this package.
 * 
 * Automatically chooses an adapter based on the available extensions.
 * 
 * @category Caching
 * @package  PEAR2_Cache_SHM
 * @author   Vasil Rangelov <boen.robot@gmail.com>
 * @license  http://www.gnu.org/copyleft/lesser.html LGPL License 2.1
 * @link     http://pear2.php.net/PEAR2_Cache_SHM
 */
abstract class SHM implements IteratorAggregate
{
    /**
     * @var array An array of adapter names that meet their requirements.
     */
    private static $_adapters = array();
    
    /**
     * Creates a new shared memory storage.
     * 
     * Estabilishes a separate persistent storage. Adapter is automatically
     * chosen based on the available extensions.
     * 
     * @param string $persistentId The ID for the storage.
     * 
     * @return static|SHM A new instance of an SHM adapter (child of this
     * class).
     */
    final public static function factory($persistentId)
    {
        foreach (self::$_adapters as $adapter) {
            try {
                return new $adapter($persistentId);
            } catch (E $e) {
                //In case of a runtime error, try to fallback to other adapters.
            }
        }
        throw new InvalidArgumentException(
            'No appropriate adapter available',
            1
        );
    }
    
    /**
     * Checks if the adapter meets its requirements.
     * 
     * @return bool TRUE on success, FALSE on failure.
     */
    public static function isMeetingRequirements()
    {
        return true;
    }
    
    /**
     * Registers an adapter.
     * 
     * Registers an SHM adapter, allowing you to call it with {@link factory()}.
     * 
     * @param string $adapter FQCN of adapter. A valid adapter is one that
     *     extends this class. The class will be autoloaded if not already
     *     present.
     * @param bool   $prepend Whether to prepend this adapter into the list of
     *     possible adapters, instead of appending to it.
     * 
     * @return bool TRUE on success, FALSE on failure.
     */
    final public static function registerAdapter($adapter, $prepend = false)
    {
        if (class_exists($adapter, true)
            && is_subclass_of($adapter, '\\' . __CLASS__)
            && $adapter::isMeetingRequirements()
        ) {
            if ($prepend) {
                self::$_adapters = array_merge(
                    array($adapter),
                    self::$_adapters
                );
            } else {
                self::$_adapters[] = $adapter;
            }
            return true;
        }
        return false;
    }
    
    /**
     * Adds a value to the shared memory storage.
     * 
     * Adds a value to the storage if it doesn't exist, or fails if it does.
     * 
     * @param string $key   Name of key to associate the value with.
     * @param mixed  $value Value for the specified key.
     * @param int    $ttl   Seconds to store the value. If set to 0 indicates no
     *     time limit.
     * 
     * @return bool TRUE on success, FALSE on failure.
     */
    public function __invoke($key, $value, $ttl = 0)
    {
        return $this->add($key, $value, $ttl);
    }
    
    /**
     * Gets a value from the shared memory storage.
     * 
     * This is a magic method, thanks to which any property you attempt to get
     * the value of will be fetched from the adapter, treating the property name
     * as the key of the value to get.
     * 
     * @param string $key Name of key to get.
     * 
     * @return mixed The current value of the specified key.
     */
    public function __get($key)
    {
        return $this->get($key);
    }
    
    /**
     * Sets a value in the shared memory storage.
     * 
     * This is a magic method, thanks to which any property you attempt to set
     * the value of will be set by the adapter, treating the property name as
     * the key of the value to set. The value is set without a TTL.
     * 
     * @param string $key   Name of key to associate the value with.
     * @param mixed  $value Value for the specified key.
     * 
     * @return bool TRUE on success, FALSE on failure.
     */
    public function __set($key, $value)
    {
        return $this->set($key, $value);
    }
    
    /**
     * Checks if a specified key is in the storage.
     * 
     * This is a magic method, thanks to which any property you call isset() on
     * will be checked by the adapter, treating the property name as the key
     * of the value to check.
     * 
     * @param string $key Name of key to check.
     * 
     * @return bool TRUE if the key is in the storage, FALSE otherwise. 
     */
    public function __isset($key)
    {
        return $this->exists($key);
    }
    
    /**
     * Deletes a value from the shared memory storage.
     * 
     * This is a magic method, thanks to which any property you attempt to unset
     * the value of will be unset by the adapter, treating the property name as
     * the key of the value to delete.
     * 
     * @param string $key Name of key to delete.
     * 
     * @return bool TRUE on success, FALSE on failure.
     */
    public function __unset($key)
    {
        return $this->delete($key);
    }
    
    /**
     * Creates a new shared memory storage.
     * 
     * Estabilishes a separate persistent storage.
     * 
     * @param string $persistentId The ID for the storage. The storage will be
     *     reused if it exists, or created if it doesn't exist. Data and locks
     *     are namespaced by this ID.
     */
    abstract public function __construct($persistentId);
    
    /**
     * Obtains a named lock.
     * 
     * @param string $key     Name of the key to obtain. Note that $key may
     *     repeat for each distinct $persistentId.
     * @param double $timeout If the lock can't be immediatly obtained, the
     *     script will block for at most the specified amount of seconds.
     *     Setting this to 0 makes lock obtaining non blocking, and setting it
     *     to NULL makes it block without a time limit.
     * 
     * @return bool TRUE on success, FALSE on failure.
     */
    abstract public function lock($key, $timeout = null);
    
    /**
     * Releases a named lock.
     * 
     * @param string $key Name of the key to release. Note that $key may
     *     repeat for each distinct $persistentId.
     * 
     * @return bool TRUE on success, FALSE on failure.
     */
    abstract public function unlock($key);
    
    /**
     * Checks if a specified key is in the storage.
     * 
     * @param string $key Name of key to check.
     * 
     * @return bool TRUE if the key is in the storage, FALSE otherwise. 
     */
    abstract public function exists($key);
    
    /**
     * Adds a value to the shared memory storage.
     * 
     * Adds a value to the storage if it doesn't exist, or fails if it does.
     * 
     * @param string $key   Name of key to associate the value with.
     * @param mixed  $value Value for the specified key.
     * @param int    $ttl   Seconds to store the value. If set to 0 indicates no
     *     time limit.
     * 
     * @return bool TRUE on success, FALSE on failure.
     */
    abstract public function add($key, $value, $ttl = 0);
    
    /**
     * Sets a value in the shared memory storage.
     * 
     * Adds a value to the storage if it doesn't exist, overwrites it otherwise.
     * 
     * @param string $key   Name of key to associate the value with.
     * @param mixed  $value Value for the specified key.
     * @param int    $ttl   Seconds to store the value. If set to 0 indicates no
     *     time limit.
     * 
     * @return bool TRUE on success, FALSE on failure.
     */
    abstract public function set($key, $value, $ttl = 0);
    
    /**
     * Gets a value from the shared memory storage.
     * 
     * Gets the current value, or throws an exception if it's not stored.
     * 
     * @param string $key Name of key to get the value of.
     * 
     * @return mixed The current value of the specified key.
     */
    abstract public function get($key);
    
    /**
     * Deletes a value from the shared memory storage.
     * 
     * @param string $key Name of key to delete.
     * 
     * @return bool TRUE on success, FALSE on failure.
     */
    abstract public function delete($key);
    
    /**
     * Increases a value from the shared memory storage.
     * 
     * Increases a value from the shared memory storage. Unlike a plain
     * set($key, get($key)+$step) combination, this function also implicitly
     * performs locking.
     * 
     * @param string $key  Name of key to increase.
     * @param int    $step Value to increase the key by.
     * 
     * @return int The new value.
     */
    abstract public function inc($key, $step = 1);
    
    /**
     * Decreases a value from the shared memory storage.
     * 
     * Decreases a value from the shared memory storage. Unlike a plain
     * set($key, get($key)-$step) combination, this function also implicitly
     * performs locking.
     * 
     * @param string $key  Name of key to decrease.
     * @param int    $step Value to decrease the key by.
     * 
     * @return int The new value.
     */
    abstract public function dec($key, $step = 1);

    /**
     * Sets a new value if a key has a certain value.
     * 
     * Sets a new value if a key has a certain value. This function only works
     * when $old and $new are longs.
     * 
     * @param string $key Key of the value to compare and set.
     * @param int    $old The value to compare the key against.
     * @param int    $new The value to set the key to.
     * 
     * @return bool TRUE on success, FALSE on failure. 
     */
    abstract public function cas($key, $old, $new);
    
    /**
     * Clears the persistent storage.
     * 
     * Clears the persistent storage, i.e. removes all keys. Locks are left
     * intact.
     * 
     * @return void
     */
    abstract public function clear();
    
    /**
     * Retrieve an external iterator
     * 
     * Returns an external iterator.
     * 
     * @param string|null $filter   A PCRE regular expression.
     *     Only matching keys will be iterated over.
     *     Setting this to NULL matches all keys of this instance.
     * @param bool        $keysOnly Whether to return only the keys,
     *     or return both the keys and values.
     * 
     * @return \Traversable An array with all matching keys as array keys,
     *     and values as array values. If $keysOnly is TRUE, the array keys are
     *     numeric, and the array values are key names.
     */
    abstract public function getIterator($filter = null, $keysOnly = false);
}

SHM::registerAdapter('\\' . __NAMESPACE__ . '\SHM\Adapter\Placebo');
SHM::registerAdapter('\\' . __NAMESPACE__ . '\SHM\Adapter\Wincache');
SHM::registerAdapter('\\' . __NAMESPACE__ . '\SHM\Adapter\APC');


File: /PEAR2\Console\Color\Backgrounds.php
<?php

/**
 * Backgrounds class for PEAR2_Console_Color.
 * 
 * PHP version 5.3
 *
 * @category  Console
 * @package   PEAR2_Console_Color
 * @author    Ivo Nascimento <ivo@o8o.com.br>
 * @license   http://www.gnu.org/copyleft/lesser.html LGPL License 2.1
 * @version   1.0.0
 * @link      http://pear2.php.net/PEAR2_Console_Color
 */
namespace PEAR2\Console\Color;

/**
 * This class has the possibles values to a Background Color.
 *
 * @category  Console
 * @package   PEAR2_Console_Color
 * @author    Ivo Nascimento <ivo@o8o.com.br>
 * @copyright 2011 Ivo Nascimento
 * @license   http://www.gnu.org/copyleft/lesser.html LGPL License 2.1
 * @link      http://pear2.php.net/PEAR2_Console_Color
 */
abstract class Backgrounds
{
    /**
     * Used at {@link \PEAR2\Console\Color::setBackground()} to specify that
     * the background color already in effect should be kept.
     */
    const KEEP    = null;

    /**
     * Used at {@link \PEAR2\Console\Color::setBackground()} to set the
     * background color to black/grey (implmementation defined).
     */
    const BLACK   = 40;

    /**
     * Used at {@link \PEAR2\Console\Color::setBackground()} to set the
     * background color to black/grey (implementation defined).
     */
    const GREY    = 40;

    /**
     * Used at {@link \PEAR2\Console\Color::setBackground()} to set the
     * background color to maroon/red (implementation defined).
     */
    const MAROON  = 41;

    /**
     * Used at {@link \PEAR2\Console\Color::setBackground()} to set the
     * background color to maroon/red (implementation defined).
     */
    const RED     = 41;

    /**
     * Used at {@link \PEAR2\Console\Color::setBackground()} to set the
     * background color to green/lime (implementation defined).
     */
    const GREEN   = 42;

    /**
     * Used at {@link \PEAR2\Console\Color::setBackground()} to set the
     * background color to green/lime (implementation defined).
     */
    const LIME    = 42;

    /**
     * Used at {@link \PEAR2\Console\Color::setBackground()} to set the
     * background color to brown/yellow (implementation defined).
     */
    const BROWN   = 43;

    /**
     * Used at {@link \PEAR2\Console\Color::setBackground()} to set the
     * background color to brown/yellow (implementation defined).
     */
    const YELLOW  = 43;

    /**
     * Used at {@link \PEAR2\Console\Color::setBackground()} to set the
     * background color to navy/blue (implementation defined).
     */
    const NAVY    = 44;

    /**
     * Used at {@link \PEAR2\Console\Color::setBackground()} to set the
     * background color to navy/blue (implementation defined).
     */
    const BLUE    = 44;

    /**
     * Used at {@link \PEAR2\Console\Color::setBackground()} to set the
     * background color to purple/magenta (implementation defined).
     */
    const PURPLE  = 45;

    /**
     * Used at {@link \PEAR2\Console\Color::setBackground()} to set the
     * background color to purple/magenta (implementation defined).
     */
    const MAGENTA = 45;

    /**
     * Used at {@link \PEAR2\Console\Color::setBackground()} to set the
     * background color to teal/cyan (implementation defined).
     */
    const TEAL    = 46;

    /**
     * Used at {@link \PEAR2\Console\Color::setBackground()} to set the
     * background color to teal/cyan (implementation defined).
     */
    const CYAN    = 46;

    /**
     * Used at {@link \PEAR2\Console\Color::setBackground()} to set the
     * background color to silver/white (implementation defined).
     */
    const SILVER  = 47;

    /**
     * Used at {@link \PEAR2\Console\Color::setBackground()} to set the
     * background color to silver/white (implementation defined).
     */
    const WHITE   = 47;

    /**
     * Used at {@link \PEAR2\Console\Color::setBackground()} to set the
     * background color to whatever the default one is.
     */
    const RESET   = 49;
}


File: /PEAR2\Console\Color\Exception.php
<?php

/**
 * Exception class for PEAR2_Console_Color.
 * 
 * PHP version 5.3
 *
 * @category Console
 * @package  PEAR2_Console_Color
 * @author   Vasil Rangelov <boen.robot@gmail.com>
 * @license  http://www.gnu.org/copyleft/lesser.html LGPL License 2.1
 * @version  1.0.0
 * @link     http://pear2.php.net/PEAR2_Console_Color
 */
namespace PEAR2\Console\Color;

/**
 * Exception class for PEAR2_Console_Color.
 *
 * @category Console
 * @package  PEAR2_Console_Color
 * @author   Vasil Rangelov <boen.robot@gmail.com>
 * @license  http://www.gnu.org/copyleft/lesser.html LGPL License 2.1
 * @link     http://pear2.php.net/PEAR2_Console_Color
 */
interface Exception
{
}


File: /PEAR2\Console\Color\Flags.php
<?php

/**
 * Flags class for PEAR2_Console_Color
 * Mappping the names of Font Style to your values.
 * 
 * PHP version 5.3
 *
 * @category Console
 * @package  PEAR2_Console_Color
 * @author   Vasil Rangelov <boen.robot@gmail.com>
 * @license  http://www.gnu.org/copyleft/lesser.html LGPL License 2.1
 * @version  1.0.0
 * @link     http://pear2.php.net/PEAR2_Console_Color
 */
namespace PEAR2\Console\Color;

use ReflectionClass;

/**
 * This class has the possibles flags to a color setting.
 * 
 * @category Console
 * @package  PEAR2_Console_Color
 * @author   Vasil Rangelov <boen.robot@gmail.com>
 * @license  http://www.gnu.org/copyleft/lesser.html LGPL License 2.1
 * @link     http://pear2.php.net/PEAR2_Console_Color
 */
abstract class Flags
{
    /**
     * Used at {@link \PEAR2\Console\Color::setFlags()} to specify that no
     * flags should be applied.
     */
    const NONE    = 0;

    /**
     * Used at {@link \PEAR2\Console\Color::setFlags()} as part of a bitmask.
     * If specified, resets all color and style information before applying
     * everything else.
     */
    const RESET   = 1;

    /**
     * Used at {@link \PEAR2\Console\Color::setFlags()} as part of a bitmask.
     * If specified, inverses the font and background colors, before letting
     * the remaining settings further modify things.
     * If specified together with {@link self::RESET}, takes effect AFTER the
     * reset.
     */
    const INVERSE = 2;

    /**
     * @var int[] Array with the flag as a key, and the corresponding code as a
     *     value.
     */
    protected static $flagCodes = array(
        self::RESET   => 0,
        self::INVERSE => 7
    );

    /**
     * Gets the codes for a flag set.
     * 
     * @param int $flags The flags to get the codes for.
     * 
     * @return int[] The codes for the flags specified, in ascending order,
     *     based on the flag constants' values.
     */
    final public static function getCodes($flags)
    {
        if (self::NONE === $flags) {
            return array();
        }

        $result = array();
        $flagsClass = new ReflectionClass(get_called_class());
        $validFlags = array_values(
            array_unique($flagsClass->getConstants(), SORT_NUMERIC)
        );
        foreach ($validFlags as $flag) {
            if ($flags & $flag) {
                $result[] = static::$flagCodes[$flag];
            }
        }
        return $result;
    }
}


File: /PEAR2\Console\Color\Fonts.php
<?php

/**
 * Font class for PEAR2_Console_Color
 * 
 * PHP version 5.3
 *
 * @category  Console
 * @package   PEAR2_Console_Color
 * @author    Ivo Nascimento <ivo@o8o.com.br>
 * @license   http://www.gnu.org/copyleft/lesser.html LGPL License 2.1
 * @version   1.0.0
 * @link      http://pear2.php.net/PEAR2_Console_Color
 */
namespace PEAR2\Console\Color;

/**
 * This class has the possibles values to a Font Color.
 *
 * @category  Console
 * @package   PEAR2_Console_Color
 * @author    Ivo Nascimento <ivo@o8o.com.br>
 * @copyright 2011 Ivo Nascimento
 * @license   http://www.gnu.org/copyleft/lesser.html LGPL License 2.1
 * @link      http://pear2.php.net/PEAR2_Console_Color
 */
abstract class Fonts
{
    /**
     * Used at {@link \PEAR2\Console\Color::setFont()} to specify that
     * the font color already in effect should be kept.
     */
    const KEEP    = null;

    /**
     * Used at {@link \PEAR2\Console\Color::setFont()} to set the
     * font color to black/grey (implementation defined).
     */
    const BLACK   = 30;

    /**
     * Used at {@link \PEAR2\Console\Color::setFont()} to set the
     * font color to black/grey (implementation defined).
     */
    const GREY    = 30;

    /**
     * Used at {@link \PEAR2\Console\Color::setFont()} to set the
     * font color to maroon/red (implementation defined).
     */
    const MAROON  = 31;

    /**
     * Used at {@link \PEAR2\Console\Color::setFont()} to set the
     * font color to maroon/red (implementation defined).
     */
    const RED     = 31;

    /**
     * Used at {@link \PEAR2\Console\Color::setFont()} to set the
     * font color to green/lime (implementation defined).
     */
    const LIME    = 32;

    /**
     * Used at {@link \PEAR2\Console\Color::setFont()} to set the
     * font color to green/lime (implementation defined).
     */
    const GREEN   = 32;

    /**
     * Used at {@link \PEAR2\Console\Color::setFont()} to set the
     * font color to brown/yellow (implementation defined).
     */
    const BROWN   = 33;

    /**
     * Used at {@link \PEAR2\Console\Color::setFont()} to set the
     * font color to brown/yellow (implementation defined).
     */
    const YELLOW  = 33;

    /**
     * Used at {@link \PEAR2\Console\Color::setFont()} to set the
     * font color to navy/blue (implementation defined).
     */
    const NAVY    = 34;

    /**
     * Used at {@link \PEAR2\Console\Color::setFont()} to set the
     * font color to navy/blue (implementation defined).
     */
    const BLUE    = 34;

    /**
     * Used at {@link \PEAR2\Console\Color::setFont()} to set the
     * font color to purple/magenta (implementation defined).
     */
    const PURPLE  = 35;

    /**
     * Used at {@link \PEAR2\Console\Color::setFont()} to set the
     * font color to purple/magenta (implementation defined).
     */
    const MAGENTA = 35;

    /**
     * Used at {@link \PEAR2\Console\Color::setFont()} to set the
     * font color to teal/cyan (implementation defined).
     */
    const TEAL    = 36;

    /**
     * Used at {@link \PEAR2\Console\Color::setFont()} to set the
     * font color to teal/cyan (implementation defined).
     */
    const CYAN    = 36;

    /**
     * Used at {@link \PEAR2\Console\Color::setFont()} to set the
     * font color to silver/white (implementation defined).
     */
    const SILVER  = 37;

    /**
     * Used at {@link \PEAR2\Console\Color::setFont()} to set the
     * font color to silver/white (implementation defined).
     */
    const WHITE   = 37;

    /**
     * Used at {@link \PEAR2\Console\Color::setFont()} to set the
     * font color to whatever the default one is.
     */
    const RESET   = 39;
}


File: /PEAR2\Console\Color\Styles.php
<?php

/**
 * Styles class for PEAR2_Console_Color.
 * 
 * PHP version 5.3
 *
 * @category Console
 * @package  PEAR2_Console_Color
 * @author   Vasil Rangelov <boen.robot@gmail.com>
 * @license  http://www.gnu.org/copyleft/lesser.html LGPL License 2.1
 * @version  1.0.0
 * @link     http://pear2.php.net/PEAR2_Console_Color
 */
namespace PEAR2\Console\Color;

use ReflectionClass;

/**
 * This class has the possibles values to a Font Style.
 * 
 * @category Console
 * @package  PEAR2_Console_Color
 * @author   Vasil Rangelov <boen.robot@gmail.com>
 * @license  http://www.gnu.org/copyleft/lesser.html LGPL License 2.1
 * @link     http://pear2.php.net/PEAR2_Console_Color
 */
abstract class Styles
{
    /**
     * Used in {@link \PEAR2\Console\Color::setStyles()} to match all styles.
     */
    const ALL       = null;

    /**
     * Used in {@link \PEAR2\Console\Color::setStyles()} as part of a bitmask.
     * If specified, matches the bold style.
     * When this style is enabled, the font is bolder.
     * With ANSICON, the font color becomes more intense (but not bolder).
     */
    const BOLD      = 1;

    /**
     * Used in {@link \PEAR2\Console\Color::setStyles()} as part of a bitmask.
     * If specified, matches the underline style.
     * When this style is enabled, the font is underlined.
     * With ANSICON, the background color becomes more intense
     * (and the font is not underlined), same as {@link self::BLINK}.
     */
    const UNDERLINE = 2;

    /**
     * Used in {@link \PEAR2\Console\Color::setStyles()} as part of a bitmask.
     * If specified, matches the blink style.
     * When this style is enabled, the font color switches between its regular
     * color and the background color at regular (implementation defined)
     * intervals, creating the illusion of a blinking text.
     * With ANSICON, the background color becomes more intense
     * (and the font is not blinking), same as with {@link self::UNDERLINE}.
     */
    const BLINK     = 4;

    /**
     * Used in {@link \PEAR2\Console\Color::setStyles()} as part of a bitmask.
     * If specified, matches the concealed style.
     * When this style is enabled, the font color becomes the background color,
     * rendering the text invisible. This style is particularly useful for
     * implementations where simply setting the same color and background color
     * would not necesarily provide a fully invisibile text (e.g. ANSICON).
     */
    const CONCEALED = 8;

    /**
     * @var (int[])[] An array describing the codes for the styles.
     *     Each array key is the style's constant, and each value is an array
     *     where the first member is the disable code, and the second is the
     *     enable code.
     */
    protected static $styleCodes = array(
        self::BOLD      => array(22, 1),
        self::UNDERLINE => array(24, 4),
        self::BLINK     => array(25, 5),
        self::CONCEALED => array(28, 8)
    );

    /**
     * Get style constants.
     * 
     * @param int|null $styles Bitmask of styles to match.
     *     You can also use {@link self::ALL} (only) to get all styles.
     * 
     * @return int[] Matching style constants.
     */
    final public static function match($styles)
    {
        $flagsClass = new ReflectionClass(get_called_class());
        $validStyles = array_values(
            array_unique($flagsClass->getConstants(), SORT_NUMERIC)
        );
        unset($validStyles[array_search(self::ALL, $validStyles, true)]);

        if (self::ALL === $styles) {
            return $validStyles;
        }
        $styles = (int)$styles;

        $result = array();
        foreach ($validStyles as $flag) {
            if ($styles & $flag) {
                $result[] = $flag;
            }
        }
        return $result;
    }

    /**
     * Gets the code for a style.
     * 
     * @param int  $style The style to get the code for.
     * @param bool $state The state to get code for.
     *     TRUE for the enabled state codes,
     *     FALSE for the disabled state codes.
     * 
     * @return int The code for the flag specified.
     */
    final public static function getCode($style, $state)
    {
        return static::$styleCodes[$style][(int)(bool)$state];
    }
}


File: /PEAR2\Console\Color\UnexpectedValueException.php
<?php

/**
 * Exception class for PEAR2_Console_Color.
 * 
 * PHP version 5.3
 *
 * @category Console
 * @package  PEAR2_Console_Color
 * @author   Vasil Rangelov <boen.robot@gmail.com>
 * @license  http://www.gnu.org/copyleft/lesser.html LGPL License 2.1
 * @version  1.0.0
 * @link     http://pear2.php.net/PEAR2_Console_Color
 */
namespace PEAR2\Console\Color;

use UnexpectedValueException as U;

/**
 * Exception class for PEAR2_Console_Color.
 *
 * @category  Console
 * @package   PEAR2_Console_Color
 * @author    Vasil Rangelov <boen.robot@gmail.com>
 * @copyright 2011 Ivo Nascimento
 * @license   http://www.gnu.org/copyleft/lesser.html LGPL License 2.1
 * @link      http://pear2.php.net/PEAR2_Console_Color
 */
class UnexpectedValueException extends U implements Exception
{
    /**
     * Used when an unexpected font value is supplied.
     */
    const CODE_FONT       = 1;

    /**
     * Used when an unexpected background value is supplied.
     */
    const CODE_BACKGROUND = 2;
}


File: /PEAR2\Console\Color.php
<?php

/**
 * Main class for Console_Color
 *
 * PHP version 5.3
 *
 * @category Console
 * @package  Console_Color
 * @author   Vasil Rangelov <boen.robot@gmail.com>
 * @author   Ivo Nascimento <ivo@o8o.com.br>
 * @license  http://www.gnu.org/copyleft/lesser.html LGPL License 2.1
 * @version  1.0.0
 * @link     http://pear.php.net/package/Console_Color
 */
namespace PEAR2\Console;

use PEAR2\Console\Color\Backgrounds;
use PEAR2\Console\Color\Flags;
use PEAR2\Console\Color\Fonts;
use PEAR2\Console\Color\Styles;
use PEAR2\Console\Color\UnexpectedValueException;
use ReflectionClass;

/**
 * Main class for Console_Color.
 *
 * @category Console
 * @package  Console_Color
 * @author   Ivo Nascimento <ivo@o8o.com.br>
 * @author   Vasil Rangelov <boen.robot@gmail.com>
 * @license  http://www.gnu.org/copyleft/lesser.html LGPL License 2.1
 * @link     http://pear2.php.net/PEAR2_Console_Color
 */
class Color
{
    /**
     * @var array List of valid font colors.
     *     Filled by {@link fillValidators()}.
     */
    protected static $validFonts = array();

    /**
     * @var array List of valid background colors.
     *     Filled by {@link fillValidators()}.
     */
    protected static $validBackgorunds = array();

    /**
     * @var string Name of a class that is used to resolve flags to codes.
     */
    protected static $flagsResolver = '';

    /**
     * @var string Name of a class that is used to resolve styles to codes.
     */
    protected static $stylesResolver = '';

    /**
     * @var int Flags to set.
     */
    protected $flags = 0;

    /**
     * @var int|null The code for the currently specified font color.
     */
    protected $font = null;

    /**
     * @var int|null The code for the currently specified background color.
     */
    protected $backgorund = null;

    /**
     * @var bool[] Array with the status of each style.
     */
    protected $styles = array();

    /**
     * @var string|null The string to write to console to get the specified
     *     styling. NULL when the string needs to be regenerated.
     */
    protected $sequence = null;

    /**
     * Fills the list of valid fonts and backgrounds.
     * 
     * Classes extending this one that wish to add additional valid colors,
     * flags or styles should call this method in their own constructor BEFORE
     * calling the parent constructor.
     * 
     * @param string $fonts       Name of class, the constants of which are
     *     valid font colors.
     * @param string $backgrounds Name of class, the constants of which are
     *     valid background colors.
     * @param string $flags       Name of class that resolves flags to codes.
     *     Must inheirt from {@link Flags}. Constants of this
     *     class are considered the valid flags, and the coresponding codes must
     *     be overriden at the static $flagCodes property.
     * @param string $styles      Name of class that resolves styles to codes.
     *     Must inherit from {@link Styles}. Constants of this class are
     *     considered the valid styles, and the corresponding off/on codes must
     *     be overriden at the static $styleCodes property.
     * 
     * @return void
     */
    protected static function fillVlidators(
        $fonts,
        $backgrounds,
        $flags,
        $styles
    ) {
        if (empty(static::$validFonts)) {
            $fonts = new ReflectionClass($fonts);
            static::$validFonts = array_values(
                array_unique($fonts->getConstants(), SORT_REGULAR)
            );
        }

        if (empty(static::$validBackgorunds)) {
            $bgs = new ReflectionClass($backgrounds);
            static::$validBackgorunds = array_values(
                array_unique($bgs->getConstants(), SORT_REGULAR)
            );
        }

        if ('' === static::$flagsResolver) {
            $base = __CLASS__ . '\Flags';
            if ($base === $flags || is_subclass_of($flags, $base)) {
                static::$flagsResolver = $flags;
            }
        }

        if ('' === static::$stylesResolver) {
            $base = __CLASS__ . '\Styles';
            if ($base === $styles || is_subclass_of($styles, $base)) {
                static::$stylesResolver = $styles;
            }
        }
    }

    /**
     * Creates a new color.
     * 
     * Note that leaving all arguments with their default values (and not
     * applying styles) would result in a sequence that resets all settings to
     * the console's defaults.
     * 
     * @param int|null $font       Initial font color.
     * @param int|null $background Initial backgorund color.
     * @param int      $flags      Initial flags.
     * 
     * @see setFlags()
     * @see setStyles()
     * @see __toString()
     */
    public function __construct(
        $font = Fonts::KEEP,
        $background = Backgrounds::KEEP,
        $flags = Flags::NONE
    ) {
        static::fillVlidators(
            __CLASS__ . '\Fonts',
            __CLASS__ . '\Backgrounds',
            __CLASS__ . '\Flags',
            __CLASS__ . '\Styles'
        );
        $this->setFont($font);
        $this->setBackground($background);
        $this->setFlags($flags);
    }

    /**
     * Gets the font color.
     * 
     * @return int|null $color The font color.
     */
    public function getFont()
    {
        return $this->font;
    }

    /**
     * Sets the font color.
     * 
     * @param int|null $color The font color.
     * 
     * @return $this
     */
    public function setFont($color)
    {
        if (!in_array($color, static::$validFonts, true)) {
            throw new UnexpectedValueException(
                'Invalid font supplied.',
                UnexpectedValueException::CODE_FONT
            );
        }
        $this->font = $color;

        $this->sequence = null;
        return $this;
    }

    /**
     * Gets the background color.
     * 
     * @return int|null $color The background color.
     */
    public function getBackground()
    {
        return $this->backgorund;
    }

    /**
     * Sets the background color.
     * 
     * @param int|null $color The background color.
     * 
     * @return $this
     */
    public function setBackground($color)
    {
        if (!in_array($color, static::$validBackgorunds, true)) {
            throw new UnexpectedValueException(
                'Invalid background supplied.',
                UnexpectedValueException::CODE_BACKGROUND
            );
        }
        $this->backgorund = $color;

        $this->sequence = null;
        return $this;
    }

    /**
     * Gets the flags.
     * 
     * @return int The currently set flags.
     */
    public function getFlags()
    {
        return $this->flags;
    }

    /**
     * Sets the flags.
     * 
     * Sets the flags to apply in the sequence. Note that flags are applied
     * before all other settings, in ascending order of the constant values.
     * 
     * @param int $flags The new flags to set. Unknown flags will be ignored
     *     when forming the sequence, but will be visible with
     *     {@link getFlags()} non the less.
     * 
     * @return $this
     */
    public function setFlags($flags)
    {
        $this->flags = (int)$flags;

        $this->sequence = null;
        return $this;
    }

    /**
     * Gets styles.
     * 
     * @param int|null $style A single style to get the status of,
     *     or {@link Styles::ALL} to get all styles in an array.
     * 
     * @return bool|null|bool[] A single style status, or
     *     an array of status if $style is {@link Styles::ALL}.
     */
    public function getStyles($style = Styles::ALL)
    {
        if (Styles::ALL === $style) {
            return $this->styles;
        }
        return isset($this->styles[$style]) ? $this->styles[$style] : null;
    }

    /**
     * Sets styles.
     * 
     * Sets styles matched to a specified state.
     * 
     * @param int|null  $styles Bitmask of styles to set. You can also use the
     *     constant {@link Styles::ALL} (only) to set all known styles.
     *     Unknown styles will be ignored.
     * @param bool|null $state  The state to set the matched styles in.
     *     TRUE to enable them,
     *     FLASE to disable them,
     *     NULL to remove the setting for them (in effect using whatever the
     *     console had before the sequence was applied).
     * 
     * @return $this
     */
    public function setStyles($styles, $state)
    {
        $matchingStyles = call_user_func(
            array(static::$stylesResolver, 'match'),
            $styles
        );
        if (null === $state) {
            foreach ($matchingStyles as $style) {
                unset($this->styles[$style]);
            }
        } else {
            $state = (bool)$state;
            foreach ($matchingStyles as $style) {
                $this->styles[$style] = $state;
            }
            ksort($this->styles);
        }

        $this->sequence = null;
        return $this;
    }

    /**
     * Get the console escaping sequence.
     * 
     * This is a magic PHP method that will be called when you use the object in
     * a string context or otherwise explicitly cast it to a string.
     * 
     * It generates the escape sequence and returns it.
     * For the sake of performance, the escape sequence is cached, and is only
     * regenerated when a setter has been previously called.
     * 
     * @return string The string to write to console to get the specified
     *     styling.
     */
    public function __toString()
    {
        if (null === $this->sequence) {
            $seq = "\033[";

            $flags = implode(
                ';',
                call_user_func(
                    array(static::$flagsResolver, 'getCodes'),
                    $this->flags
                )
            );
            if ('' !== $flags) {
                $seq .= $flags . ';';
            }

            if (Fonts::KEEP !== $this->font) {
                $seq .= "{$this->font};";
            }
            if (Backgrounds::KEEP !== $this->backgorund) {
                $seq .= "{$this->backgorund};";
            }

            foreach ($this->styles as $style => $state) {
                $seq .= call_user_func(
                    array(static::$stylesResolver, 'getCode'),
                    $style,
                    $state
                ) . ';';
            }

            $this->sequence = rtrim($seq, ';') . 'm';
        }

        return $this->sequence;
    }
}


File: /PEAR2\Console\CommandLine\Action\Callback.php
<?php

/* vim: set expandtab tabstop=4 shiftwidth=4 softtabstop=4: */

/**
 * This file is part of the PEAR2\Console\CommandLine package.
 *
 * PHP version 5
 *
 * LICENSE: This source file is subject to the MIT license that is available
 * through the world-wide-web at the following URI:
 * http://opensource.org/licenses/mit-license.php
 *
 * @category  Console 
 * @package   PEAR2\Console\CommandLine
 * @author    David JEAN LOUIS <izimobil@gmail.com>
 * @copyright 2007-2009 David JEAN LOUIS
 * @license   http://opensource.org/licenses/mit-license.php MIT License 
 * @version   0.2.1
 * @link      http://pear2.php.net/PEAR2_Console_CommandLine
 * @since     File available since release 0.1.0
 * @filesource
 */
namespace PEAR2\Console\CommandLine\Action;

use PEAR2\Console\CommandLine;


/**
 * Class that represent the Callback action.
 *
 * The result option array entry value is set to the return value of the
 * callback defined in the option.
 *
 * There are two steps to defining a callback option:
 *   - define the option itself using the callback action
 *   - write the callback; this is a function (or method) that takes five
 *     arguments, as described below.
 *
 * All callbacks are called as follows:
 * <code>
 * callable_func(
 *     $value,           // the value of the option
 *     $option_instance, // the option instance
 *     $result_instance, // the result instance
 *     $parser_instance, // the parser instance
 *     $params           // an array of params as specified in the option
 * );
 * </code>
 * and *must* return the option value.
 *
 * @category  Console
 * @package   PEAR2\Console\CommandLine
 * @author    David JEAN LOUIS <izimobil@gmail.com>
 * @copyright 2007-2009 David JEAN LOUIS
 * @license   http://opensource.org/licenses/mit-license.php MIT License
 * @link      http://pear2.php.net/PEAR2_Console_CommandLine
 * @since     Class available since release 0.1.0
 */
class Callback extends CommandLine\Action
{
    // execute() {{{

    /**
     * Executes the action with the value entered by the user.
     *
     * @param mixed $value  The value of the option
     * @param array $params An optional array of parameters
     *
     * @return string
     */
    public function execute($value = false, $params = array())
    {
        $this->setResult(
            call_user_func(
                $this->option->callback,
                $value,
                $this->option,
                $this->result,
                $this->parser,
                $params
            )
        );
    }
    // }}}
}


File: /PEAR2\Console\CommandLine\Action\Counter.php
<?php

/* vim: set expandtab tabstop=4 shiftwidth=4 softtabstop=4: */

/**
 * This file is part of the PEAR2\Console\CommandLine package.
 *
 * PHP version 5
 *
 * LICENSE: This source file is subject to the MIT license that is available
 * through the world-wide-web at the following URI:
 * http://opensource.org/licenses/mit-license.php
 *
 * @category  Console 
 * @package   PEAR2\Console\CommandLine
 * @author    David JEAN LOUIS <izimobil@gmail.com>
 * @copyright 2007-2009 David JEAN LOUIS
 * @license   http://opensource.org/licenses/mit-license.php MIT License 
 * @version   0.2.1
 * @link      http://pear2.php.net/PEAR2_Console_CommandLine
 * @since     File available since release 0.1.0
 * @filesource
 */

namespace PEAR2\Console\CommandLine\Action;

use PEAR2\Console\CommandLine;

/**
 * Class that represent the Version action.
 *
 * The execute methode add 1 to the value of the result option array entry.
 * The value is incremented each time the option is found, for example
 * with an option defined like that:
 *
 * <code>
 * $parser->addOption(
 *     'verbose',
 *     array(
 *         'short_name' => '-v',
 *         'action'     => 'Counter'
 *     )
 * );
 * </code>
 * If the user type:
 * <code>
 * $ script.php -v -v -v
 * </code>
 * or: 
 * <code>
 * $ script.php -vvv
 * </code>
 * the verbose variable will be set to to 3.
 *
 * @category  Console
 * @package   PEAR2\Console\CommandLine
 * @author    David JEAN LOUIS <izimobil@gmail.com>
 * @copyright 2007-2009 David JEAN LOUIS
 * @license   http://opensource.org/licenses/mit-license.php MIT License
 * @link      http://pear2.php.net/PEAR2_Console_CommandLine
 * @since     Class available since release 0.1.0
 */
class Counter extends CommandLine\Action
{
    // execute() {{{

    /**
     * Executes the action with the value entered by the user.
     *
     * @param mixed $value  The option value
     * @param array $params An optional array of parameters
     *
     * @return string
     */
    public function execute($value = false, $params = array())
    {
        $result = $this->getResult();
        if ($result === null) {
            $result = 0;
        }
        $this->setResult(++$result);
    }
    // }}}
}


File: /PEAR2\Console\CommandLine\Action\Help.php
<?php

/* vim: set expandtab tabstop=4 shiftwidth=4 softtabstop=4: */

/**
 * This file is part of the PEAR2\Console\CommandLine package.
 *
 * PHP version 5
 *
 * LICENSE: This source file is subject to the MIT license that is available
 * through the world-wide-web at the following URI:
 * http://opensource.org/licenses/mit-license.php
 *
 * @category  Console 
 * @package   PEAR2\Console\CommandLine
 * @author    David JEAN LOUIS <izimobil@gmail.com>
 * @copyright 2007-2009 David JEAN LOUIS
 * @license   http://opensource.org/licenses/mit-license.php MIT License 
 * @version   0.2.1
 * @link      http://pear2.php.net/PEAR2_Console_CommandLine
 * @since     File available since release 0.1.0
 * @filesource
 */

namespace PEAR2\Console\CommandLine\Action;

use PEAR2\Console\CommandLine;

/**
 * Class that represent the Help action, a special action that displays the
 * help message, telling the user how to use the program.
 *
 * @category  Console
 * @package   PEAR2\Console\CommandLine
 * @author    David JEAN LOUIS <izimobil@gmail.com>
 * @copyright 2007-2009 David JEAN LOUIS
 * @license   http://opensource.org/licenses/mit-license.php MIT License
 * @link      http://pear2.php.net/PEAR2_Console_CommandLine
 * @since     Class available since release 0.1.0
 */
class Help extends CommandLine\Action
{
    // execute() {{{

    /**
     * Executes the action with the value entered by the user.
     *
     * @param mixed $value  The option value
     * @param array $params An optional array of parameters
     *
     * @return string
     */
    public function execute($value = false, $params = array())
    {
        return $this->parser->displayUsage();
    }
    // }}}
}


File: /PEAR2\Console\CommandLine\Action\List.php
<?php

/* vim: set expandtab tabstop=4 shiftwidth=4 softtabstop=4: */

/**
 * This file is part of the PEAR2\Console\CommandLine package.
 *
 * PHP version 5
 *
 * LICENSE: This source file is subject to the MIT license that is available
 * through the world-wide-web at the following URI:
 * http://opensource.org/licenses/mit-license.php
 *
 * @category  Console 
 * @package   PEAR2\Console\CommandLine
 * @author    David JEAN LOUIS <izimobil@gmail.com>
 * @copyright 2007-2009 David JEAN LOUIS
 * @license   http://opensource.org/licenses/mit-license.php MIT License 
 * @version   CVS: $Id: List.php,v 1.2 2009/02/27 08:03:17 izi Exp $
 * @link      http://pear2.php.net/PEAR2_Console_CommandLine
 * @since     File available since release 0.1.0
 * @filesource
 */

namespace PEAR2\Console\CommandLine;

/**
 * Class that represent the List action, a special action that simply output an 
 * array as a list.
 *
 * @category  Console
 * @package   PEAR2\Console\CommandLine
 * @author    David JEAN LOUIS <izimobil@gmail.com>
 * @copyright 2007-2009 David JEAN LOUIS
 * @license   http://opensource.org/licenses/mit-license.php MIT License
 * @link      http://pear2.php.net/PEAR2_Console_CommandLine
 * @since     Class available since release 0.1.0
 */
class Action_List extends Action
{
    // execute() {{{

    /**
     * Executes the action with the value entered by the user.
     * Possible parameters are:
     * - message: an alternative message to display instead of the default 
     *   message,
     * - delimiter: an alternative delimiter instead of the comma,
     * - post: a string to append after the message (default is the new line 
     *   char).
     *
     * @param mixed $value  The option value
     * @param array $params An optional array of parameters
     *
     * @return string
     */
    public function execute($value = false, $params = array())
    {
        $list = isset($params['list']) ? $params['list'] : array();
        $msg  = isset($params['message']) 
            ? $params['message'] 
            : $this->parser->message_provider->get('LIST_DISPLAYED_MESSAGE');
        $del  = isset($params['delimiter']) ? $params['delimiter'] : ', ';
        $post = isset($params['post']) ? $params['post'] : "\n";
        $this->parser->outputter->stdout($msg . implode($del, $list) . $post);
        exit(0);
    }
    // }}}
}


File: /PEAR2\Console\CommandLine\Action\Password.php
<?php

/* vim: set expandtab tabstop=4 shiftwidth=4 softtabstop=4: */

/**
 * This file is part of the PEAR2\Console\CommandLine package.
 *
 * PHP version 5
 *
 * LICENSE: This source file is subject to the MIT license that is available
 * through the world-wide-web at the following URI:
 * http://opensource.org/licenses/mit-license.php
 *
 * @category  Console 
 * @package   PEAR2\Console\CommandLine
 * @author    David JEAN LOUIS <izimobil@gmail.com>
 * @copyright 2007-2009 David JEAN LOUIS
 * @license   http://opensource.org/licenses/mit-license.php MIT License 
 * @version   0.2.1
 * @link      http://pear2.php.net/PEAR2_Console_CommandLine
 * @since     File available since release 0.1.0
 * @filesource
 */

namespace PEAR2\Console\CommandLine\Action;

use PEAR2\Console\CommandLine;

/**
 * Class that represent the Password action, a special action that allow the 
 * user to specify the password on the commandline or to be prompted for 
 * entering it.
 *
 * @category  Console
 * @package   PEAR2\Console\CommandLine
 * @author    David JEAN LOUIS <izimobil@gmail.com>
 * @copyright 2007-2009 David JEAN LOUIS
 * @license   http://opensource.org/licenses/mit-license.php MIT License
 * @link      http://pear2.php.net/PEAR2_Console_CommandLine
 * @since     Class available since release 0.1.0
 */
class Password extends CommandLine\Action
{
    // execute() {{{

    /**
     * Executes the action with the value entered by the user.
     *
     * @param mixed $value  The option value
     * @param array $params An array of optional parameters
     *
     * @return string
     */
    public function execute($value = false, $params = array())
    {
        $this->setResult(empty($value) ? $this->_promptPassword() : $value);
    }
    // }}}
    // _promptPassword() {{{

    /**
     * Prompts the password to the user without echoing it.
     *
     * @return string
     * @todo not echo-ing the password does not work on windows is there a way 
     *       to make this work ?
     */
    private function _promptPassword()
    {
        if (strtoupper(substr(PHP_OS, 0, 3)) === 'WIN') {
            fwrite(
                STDOUT,
                $this->parser->message_provider->get('PASSWORD_PROMPT_ECHO')
            );
            @flock(STDIN, LOCK_EX);
            $passwd = fgets(STDIN);
            @flock(STDIN, LOCK_UN);
        } else {
            fwrite(STDOUT, $this->parser->message_provider->get('PASSWORD_PROMPT'));
            // disable echoing
            system('stty -echo');
            @flock(STDIN, LOCK_EX);
            $passwd = fgets(STDIN);
            @flock(STDIN, LOCK_UN);
            system('stty echo');
        }
        return trim($passwd);
    }
    // }}}
}


File: /PEAR2\Console\CommandLine\Action\StoreArray.php
<?php

/* vim: set expandtab tabstop=4 shiftwidth=4 softtabstop=4: */

/**
 * This file is part of the PEAR2\Console\CommandLine package.
 *
 * PHP version 5
 *
 * LICENSE: This source file is subject to the MIT license that is available
 * through the world-wide-web at the following URI:
 * http://opensource.org/licenses/mit-license.php
 *
 * @category  Console 
 * @package   PEAR2\Console\CommandLine
 * @author    David JEAN LOUIS <izimobil@gmail.com>
 * @copyright 2007-2009 David JEAN LOUIS
 * @license   http://opensource.org/licenses/mit-license.php MIT License 
 * @version   0.2.1
 * @link      http://pear2.php.net/PEAR2_Console_CommandLine
 * @since     File available since release 0.1.0
 * @filesource
 */

namespace PEAR2\Console\CommandLine\Action;

use PEAR2\Console\CommandLine;

/**
 * Class that represent the StoreArray action.
 *
 * The execute method appends the value of the option entered by the user to 
 * the result option array entry.
 *
 * @category  Console
 * @package   PEAR2\Console\CommandLine
 * @author    David JEAN LOUIS <izimobil@gmail.com>
 * @copyright 2007-2009 David JEAN LOUIS
 * @license   http://opensource.org/licenses/mit-license.php MIT License
 * @link      http://pear2.php.net/PEAR2_Console_CommandLine
 * @since     Class available since release 0.1.0
 */
class StoreArray extends CommandLine\Action
{
    // Protected properties {{{

    /**
     * Force a clean result when first called, overriding any defaults assigned.
     *
     * @var object $firstPass First time this action has been called.
     */
    protected $firstPass = true;

    // }}}
    // execute() {{{

    /**
     * Executes the action with the value entered by the user.
     *
     * @param mixed $value  The option value
     * @param array $params An optional array of parameters
     *
     * @return string
     */
    public function execute($value = false, $params = array())
    {
        $result = $this->getResult();
        if (null === $result || $this->firstPass) {
            $result          = array();
            $this->firstPass = false;
        }
        $result[] = $value;
        $this->setResult($result);
    }
    // }}}
}


File: /PEAR2\Console\CommandLine\Action\StoreFalse.php
<?php

/* vim: set expandtab tabstop=4 shiftwidth=4 softtabstop=4: */

/**
 * This file is part of the PEAR2\Console\CommandLine package.
 *
 * PHP version 5
 *
 * LICENSE: This source file is subject to the MIT license that is available
 * through the world-wide-web at the following URI:
 * http://opensource.org/licenses/mit-license.php
 *
 * @category  Console 
 * @package   PEAR2\Console\CommandLine
 * @author    David JEAN LOUIS <izimobil@gmail.com>
 * @copyright 2007-2009 David JEAN LOUIS
 * @license   http://opensource.org/licenses/mit-license.php MIT License 
 * @version   0.2.1
 * @link      http://pear2.php.net/PEAR2_Console_CommandLine
 * @since     File available since release 0.1.0
 * @filesource
 */

namespace PEAR2\Console\CommandLine\Action;

use PEAR2\Console\CommandLine;

/**
 * Class that represent the StoreFalse action.
 *
 * The execute method store the boolean 'false' in the corrsponding result
 * option array entry (the value is true if the option is not present in the 
 * command line entered by the user).
 *
 * @category  Console
 * @package   PEAR2\Console\CommandLine
 * @author    David JEAN LOUIS <izimobil@gmail.com>
 * @copyright 2007-2009 David JEAN LOUIS
 * @license   http://opensource.org/licenses/mit-license.php MIT License
 * @link      http://pear2.php.net/PEAR2_Console_CommandLine
 * @since     Class available since release 0.1.0
 */
class StoreFalse extends CommandLine\Action
{
    // execute() {{{

    /**
     * Executes the action with the value entered by the user.
     *
     * @param mixed $value  The option value
     * @param array $params An array of optional parameters
     *
     * @return string
     */
    public function execute($value = false, $params = array())
    {
        $this->setResult(false);
    }

    // }}}
}


File: /PEAR2\Console\CommandLine\Action\StoreFloat.php
<?php

/* vim: set expandtab tabstop=4 shiftwidth=4 softtabstop=4: */

/**
 * This file is part of the PEAR2\Console\CommandLine package.
 *
 * PHP version 5
 *
 * LICENSE: This source file is subject to the MIT license that is available
 * through the world-wide-web at the following URI:
 * http://opensource.org/licenses/mit-license.php
 *
 * @category  Console 
 * @package   PEAR2\Console\CommandLine
 * @author    David JEAN LOUIS <izimobil@gmail.com>
 * @copyright 2007-2009 David JEAN LOUIS
 * @license   http://opensource.org/licenses/mit-license.php MIT License 
 * @version   0.2.1
 * @link      http://pear2.php.net/PEAR2_Console_CommandLine
 * @since     File available since release 0.1.0
 * @filesource
 */

namespace PEAR2\Console\CommandLine\Action;

use PEAR2\Console\CommandLine;

/**
 * Class that represent the StoreFloat action.
 *
 * The execute method store the value of the option entered by the user as a
 * float in the result option array entry, if the value passed is not a float
 * an Exception is raised.
 *
 * @category  Console
 * @package   PEAR2\Console\CommandLine
 * @author    David JEAN LOUIS <izimobil@gmail.com>
 * @copyright 2007-2009 David JEAN LOUIS
 * @license   http://opensource.org/licenses/mit-license.php MIT License
 * @link      http://pear2.php.net/PEAR2_Console_CommandLine
 * @since     Class available since release 0.1.0
 */
class StoreFloat extends CommandLine\Action
{
    // execute() {{{

    /**
     * Executes the action with the value entered by the user.
     *
     * @param mixed $value  The option value
     * @param array $params An array of optional parameters
     *
     * @return string
     * @throws PEAR2\Console\CommandLine\Exception
     */
    public function execute($value = false, $params = array())
    {
        if (!is_numeric($value)) {
            throw CommandLine\Exception::factory(
                'OPTION_VALUE_TYPE_ERROR',
                array(
                    'name'  => $this->option->name,
                    'type'  => 'float',
                    'value' => $value
                ),
                $this->parser
            );
        }
        $this->setResult((float)$value);
    }
    // }}}
}


File: /PEAR2\Console\CommandLine\Action\StoreInt.php
<?php

/* vim: set expandtab tabstop=4 shiftwidth=4 softtabstop=4: */

/**
 * This file is part of the PEAR2\Console\CommandLine package.
 *
 * PHP version 5
 *
 * LICENSE: This source file is subject to the MIT license that is available
 * through the world-wide-web at the following URI:
 * http://opensource.org/licenses/mit-license.php
 *
 * @category  Console 
 * @package   PEAR2\Console\CommandLine
 * @author    David JEAN LOUIS <izimobil@gmail.com>
 * @copyright 2007-2009 David JEAN LOUIS
 * @license   http://opensource.org/licenses/mit-license.php MIT License 
 * @version   0.2.1
 * @link      http://pear2.php.net/PEAR2_Console_CommandLine
 * @since     File available since release 0.1.0
 * @filesource
 */

namespace PEAR2\Console\CommandLine\Action;

use PEAR2\Console\CommandLine;

/**
 * Class that represent the StoreInt action.
 *
 * The execute method store the value of the option entered by the user as an
 * integer in the result option array entry, if the value passed is not an 
 * integer an Exception is raised.
 *
 * @category  Console
 * @package   PEAR2\Console\CommandLine
 * @author    David JEAN LOUIS <izimobil@gmail.com>
 * @copyright 2007-2009 David JEAN LOUIS
 * @license   http://opensource.org/licenses/mit-license.php MIT License
 * @link      http://pear2.php.net/PEAR2_Console_CommandLine
 * @since     Class available since release 0.1.0
 */
class StoreInt extends CommandLine\Action
{
    // execute() {{{

    /**
     * Executes the action with the value entered by the user.
     *
     * @param mixed $value  The option value
     * @param array $params An array of optional parameters
     *
     * @return string
     * @throws PEAR2\Console\CommandLine\Exception
     */
    public function execute($value = false, $params = array())
    {
        if (!is_numeric($value)) {
            throw CommandLine\Exception::factory(
                'OPTION_VALUE_TYPE_ERROR',
                array(
                    'name'  => $this->option->name,
                    'type'  => 'int',
                    'value' => $value
                ),
                $this->parser
            );
        }
        $this->setResult((int)$value);
    }
    // }}}
}


File: /PEAR2\Console\CommandLine\Action\StoreString.php
<?php

/* vim: set expandtab tabstop=4 shiftwidth=4 softtabstop=4: */

/**
 * This file is part of the PEAR2\Console\CommandLine package.
 *
 * PHP version 5
 *
 * LICENSE: This source file is subject to the MIT license that is available
 * through the world-wide-web at the following URI:
 * http://opensource.org/licenses/mit-license.php
 *
 * @category  Console 
 * @package   PEAR2\Console\CommandLine
 * @author    David JEAN LOUIS <izimobil@gmail.com>
 * @copyright 2007-2009 David JEAN LOUIS
 * @license   http://opensource.org/licenses/mit-license.php MIT License 
 * @version   0.2.1
 * @link      http://pear2.php.net/PEAR2_Console_CommandLine
 * @since     File available since release 0.1.0
 * @filesource
 */

namespace PEAR2\Console\CommandLine\Action;

use PEAR2\Console\CommandLine;

/**
 * Class that represent the StoreString action.
 *
 * The execute method store the value of the option entered by the user as a 
 * string in the result option array entry.
 *
 * @category  Console
 * @package   PEAR2\Console\CommandLine
 * @author    David JEAN LOUIS <izimobil@gmail.com>
 * @copyright 2007-2009 David JEAN LOUIS
 * @license   http://opensource.org/licenses/mit-license.php MIT License
 * @link      http://pear2.php.net/PEAR2_Console_CommandLine
 * @since     Class available since release 0.1.0
 */
class StoreString extends CommandLine\Action
{
    // execute() {{{

    /**
     * Executes the action with the value entered by the user.
     *
     * @param mixed $value  The option value
     * @param array $params An array of optional parameters
     *
     * @return string
     */
    public function execute($value = false, $params = array())
    {
        $this->setResult((string)$value);
    }
    // }}}
}


File: /PEAR2\Console\CommandLine\Action\StoreTrue.php
<?php

/* vim: set expandtab tabstop=4 shiftwidth=4 softtabstop=4: */

/**
 * This file is part of the PEAR2\Console\CommandLine package.
 *
 * PHP version 5
 *
 * LICENSE: This source file is subject to the MIT license that is available
 * through the world-wide-web at the following URI:
 * http://opensource.org/licenses/mit-license.php
 *
 * @category  Console 
 * @package   PEAR2\Console\CommandLine
 * @author    David JEAN LOUIS <izimobil@gmail.com>
 * @copyright 2007-2009 David JEAN LOUIS
 * @license   http://opensource.org/licenses/mit-license.php MIT License 
 * @version   0.2.1
 * @link      http://pear2.php.net/PEAR2_Console_CommandLine
 * @since     File available since release 0.1.0
 * @filesource
 */

namespace PEAR2\Console\CommandLine\Action;

use PEAR2\Console\CommandLine;

/**
 * Class that represent the StoreTrue action.
 *
 * The execute method store the boolean 'true' in the corrsponding result
 * option array entry (the value is false if the option is not present in the 
 * command line entered by the user).
 *
 * @category  Console
 * @package   PEAR2\Console\CommandLine
 * @author    David JEAN LOUIS <izimobil@gmail.com>
 * @copyright 2007-2009 David JEAN LOUIS
 * @license   http://opensource.org/licenses/mit-license.php MIT License
 * @link      http://pear2.php.net/PEAR2_Console_CommandLine
 * @since     Class available since release 0.1.0
 */
class StoreTrue extends CommandLine\Action
{
    // execute() {{{

    /**
     * Executes the action with the value entered by the user.
     *
     * @param mixed $value  The option value
     * @param array $params An array of optional parameters
     *
     * @return string
     */
    public function execute($value = false, $params = array())
    {
        $this->setResult(true);
    }
    // }}}
}


File: /PEAR2\Console\CommandLine\Action\Version.php
<?php

/* vim: set expandtab tabstop=4 shiftwidth=4 softtabstop=4: */

/**
 * This file is part of the PEAR2\Console\CommandLine package.
 *
 * PHP version 5
 *
 * LICENSE: This source file is subject to the MIT license that is available
 * through the world-wide-web at the following URI:
 * http://opensource.org/licenses/mit-license.php
 *
 * @category  Console 
 * @package   PEAR2\Console\CommandLine
 * @author    David JEAN LOUIS <izimobil@gmail.com>
 * @copyright 2007-2009 David JEAN LOUIS
 * @license   http://opensource.org/licenses/mit-license.php MIT License 
 * @version   0.2.1
 * @link      http://pear2.php.net/PEAR2_Console_CommandLine
 * @since     File available since release 0.1.0
 * @filesource
 */

namespace PEAR2\Console\CommandLine\Action;

use PEAR2\Console\CommandLine;

/**
 * Class that represent the Version action, a special action that displays the
 * version string of the program.
 *
 * @category  Console
 * @package   PEAR2\Console\CommandLine
 * @author    David JEAN LOUIS <izimobil@gmail.com>
 * @copyright 2007-2009 David JEAN LOUIS
 * @license   http://opensource.org/licenses/mit-license.php MIT License
 * @link      http://pear2.php.net/PEAR2_Console_CommandLine
 * @since     Class available since release 0.1.0
 */
class Version extends CommandLine\Action
{
    // execute() {{{

    /**
     * Executes the action with the value entered by the user.
     *
     * @param mixed $value  The option value
     * @param array $params An array of optional parameters
     *
     * @return string
     */
    public function execute($value = false, $params = array())
    {
        return $this->parser->displayVersion();
    }
    // }}}
}


File: /PEAR2\Console\CommandLine\Action.php
<?php

/* vim: set expandtab tabstop=4 shiftwidth=4 softtabstop=4: */

/**
 * This file is part of the PEAR2\Console\CommandLine package.
 *
 * PHP version 5
 *
 * LICENSE: This source file is subject to the MIT license that is available
 * through the world-wide-web at the following URI:
 * http://opensource.org/licenses/mit-license.php
 *
 * @category  Console 
 * @package   PEAR2\Console\CommandLine
 * @author    David JEAN LOUIS <izimobil@gmail.com>
 * @copyright 2007-2009 David JEAN LOUIS
 * @license   http://opensource.org/licenses/mit-license.php MIT License 
 * @version   0.2.1
 * @link      http://pear2.php.net/PEAR2_Console_CommandLine
 * @since     File available since release 0.1.0
 * @filesource
 */
namespace PEAR2\Console\CommandLine;

/**
 * Class that represent an option action.
 *
 * @category  Console
 * @package   PEAR2\Console\CommandLine
 * @author    David JEAN LOUIS <izimobil@gmail.com>
 * @copyright 2007-2009 David JEAN LOUIS
 * @license   http://opensource.org/licenses/mit-license.php MIT License
 * @link      http://pear2.php.net/PEAR2_Console_CommandLine
 * @since     Class available since release 0.1.0
 */
abstract class Action
{
    // Properties {{{

    /**
     * A reference to the result instance.
     *
     * @var PEAR2\Console\CommandLine_Result $result The result instance
     */
    protected $result;

    /**
     * A reference to the option instance.
     *
     * @var PEAR2\Console\CommandLine_Option $option The action option
     */
    protected $option;

    /**
     * A reference to the parser instance.
     *
     * @var PEAR2\Console\CommandLine $parser The parser
     */
    protected $parser;

    // }}}
    // __construct() {{{

    /**
     * Constructor
     *
     * @param PEAR2\Console\CommandLine_Result $result The result instance
     * @param PEAR2\Console\CommandLine_Option $option The action option
     * @param PEAR2\Console\CommandLine        $parser The current parser
     *
     * @return void
     */
    public function __construct($result, $option, $parser)
    {
        $this->result = $result;
        $this->option = $option;
        $this->parser = $parser;
    }

    // }}}
    // getResult() {{{

    /**
     * Convenience method to retrieve the value of result->options[name].
     *
     * @return mixed The result value or null
     */
    public function getResult()
    {
        if (isset($this->result->options[$this->option->name])) {
            return $this->result->options[$this->option->name];
        }
        return null;
    }

    // }}}
    // format() {{{

    /**
     * Allow a value to be pre-formatted prior to being used in a choices test.
     * Setting $value to the new format will keep the formatting.
     *
     * @param mixed &$value The value to format
     *
     * @return mixed The formatted value
     */
    public function format(&$value)
    {
        return $value;
    }

    // }}}
    // setResult() {{{

    /**
     * Convenience method to assign the result->options[name] value.
     *
     * @param mixed $result The result value
     *
     * @return void
     */
    public function setResult($result)
    {
        $this->result->options[$this->option->name] = $result;
    }

    // }}}
    // execute() {{{

    /**
     * Executes the action with the value entered by the user.
     * All children actions must implement this method.
     *
     * @param mixed $value  The option value
     * @param array $params An optional array of parameters
     *
     * @return string
     */
    abstract public function execute($value = false, $params = array());
    // }}}
}


File: /PEAR2\Console\CommandLine\Argument.php
<?php

/* vim: set expandtab tabstop=4 shiftwidth=4 softtabstop=4: */

/**
 * This file is part of the PEAR2\Console\CommandLine package.
 *
 * PHP version 5
 *
 * LICENSE: This source file is subject to the MIT license that is available
 * through the world-wide-web at the following URI:
 * http://opensource.org/licenses/mit-license.php
 *
 * @category  Console
 * @package   PEAR2\Console\CommandLine
 * @author    David JEAN LOUIS <izimobil@gmail.com>
 * @copyright 2007-2009 David JEAN LOUIS
 * @license   http://opensource.org/licenses/mit-license.php MIT License
 * @version   0.2.1
 * @link      http://pear2.php.net/PEAR2_Console_CommandLine
 * @since     File available since release 0.1.0
 * @filesource
 */

namespace PEAR2\Console\CommandLine;

/**
 * Class that represent a command line argument.
 *
 * @category  Console
 * @package   PEAR2\Console\CommandLine
 * @author    David JEAN LOUIS <izimobil@gmail.com>
 * @copyright 2007-2009 David JEAN LOUIS
 * @license   http://opensource.org/licenses/mit-license.php MIT License
 * @link      http://pear2.php.net/PEAR2_Console_CommandLine
 * @since     Class available since release 0.1.0
 */
class Argument extends Element
{
    // Public properties {{{

    /**
     * Setting this to true will tell the parser that the argument expects more
     * than one argument and that argument values should be stored in an array.
     *
     * @var boolean $multiple Whether the argument expects multiple values
     */
    public $multiple = false;

    /**
     * Setting this to true will tell the parser that the argument is optional
     * and can be ommited.
     * Note that it is not a good practice to make arguments optional, it is
     * the role of the options to be optional, by essence.
     *
     * @var boolean $optional Whether the argument is optional or not.
     */
    public $optional = false;

    // }}}
    // validate() {{{

    /**
     * Validates the argument instance.
     *
     * @return void
     * @throws PEAR2\Console\CommandLine\Exception
     * @todo use exceptions
     */
    public function validate()
    {
        // check if the argument name is valid
        if (!preg_match(
            '/^[a-zA-Z_\x7f-\xff]+[a-zA-Z0-9_\x7f-\xff]*$/',
            $this->name
        )
        ) {
            \PEAR2\Console\CommandLine::triggerError(
                'argument_bad_name',
                E_USER_ERROR,
                array('{$name}' => $this->name)
            );
        }
        if (!$this->optional && $this->default !== null) {
            \PEAR2\Console\CommandLine::triggerError(
                'argument_no_default',
                E_USER_ERROR
            );
        }
        parent::validate();
    }

    // }}}
}


File: /PEAR2\Console\CommandLine\Command.php
<?php

/* vim: set expandtab tabstop=4 shiftwidth=4 softtabstop=4: */

/**
 * This file is part of the PEAR2\Console\CommandLine package.
 *
 * PHP version 5
 *
 * LICENSE: This source file is subject to the MIT license that is available
 * through the world-wide-web at the following URI:
 * http://opensource.org/licenses/mit-license.php
 *
 * @category  Console 
 * @package   PEAR2\Console\CommandLine
 * @author    David JEAN LOUIS <izimobil@gmail.com>
 * @copyright 2007-2009 David JEAN LOUIS
 * @license   http://opensource.org/licenses/mit-license.php MIT License 
 * @version   0.2.1
 * @link      http://pear2.php.net/PEAR2_Console_CommandLine
 * @since     File available since release 0.1.0
 * @filesource
 */

namespace PEAR2\Console\CommandLine;

/**
 * Class that represent a command with option and arguments.
 *
 * This class exist just to clarify the interface but at the moment it is 
 * strictly identical to PEAR2\Console\CommandLine class, it could change in the
 * future though.
 *
 * @category  Console
 * @package   PEAR2\Console\CommandLine
 * @author    David JEAN LOUIS <izimobil@gmail.com>
 * @copyright 2007-2009 David JEAN LOUIS
 * @license   http://opensource.org/licenses/mit-license.php MIT License
 * @link      http://pear2.php.net/PEAR2_Console_CommandLine
 * @since     Class available since release 0.1.0
 */
class Command extends \PEAR2\Console\CommandLine
{
    // Public properties {{{

    /**
     * An array of aliases for the subcommand.
     *
     * @var array $aliases Aliases for the subcommand.
     */
    public $aliases = array();

    // }}}
    // __construct() {{{

    /**
     * Constructor.
     *
     * @param array $params An optional array of parameters
     *
     * @return void
     */
    public function __construct($params = array()) 
    {
        if (isset($params['aliases'])) {
            $this->aliases = $params['aliases'];
        }
        parent::__construct($params);
    }

    // }}}
}


File: /PEAR2\Console\CommandLine\CustomMessageProvider.php
<?php

/* vim: set expandtab tabstop=4 shiftwidth=4 softtabstop=4: */

/**
 * This file is part of the PEAR2\Console\CommandLine package.
 *
 * PHP version 5
 *
 * LICENSE: This source file is subject to the MIT license that is available
 * through the world-wide-web at the following URI:
 * http://opensource.org/licenses/mit-license.php
 *
 * @category  Console
 * @package   PEAR2\Console\CommandLine
 * @author    David JEAN LOUIS <izimobil@gmail.com>
 * @author    Michael Gauthier <mike@silverorange.com>
 * @copyright 2007 David JEAN LOUIS, 2009 silverorange
 * @license   http://opensource.org/licenses/mit-license.php MIT License
 * @version   CVS: $Id: CustomMessageProvider.php 282427 2009-06-19 10:22:48Z izi $
 * @link      http://pear2.php.net/PEAR2_Console_CommandLine
 * @since     File available since release 1.1.0
 * @filesource
 */

namespace PEAR2\Console\CommandLine;

/**
 * Common interfacefor message providers that allow overriding with custom
 * messages
 *
 * Message providers may optionally implement this interface.
 *
 * @category  Console
 * @package   PEAR2\Console\CommandLine
 * @author    David JEAN LOUIS <izimobil@gmail.com>
 * @author    Michael Gauthier <mike@silverorange.com>
 * @copyright 2007 David JEAN LOUIS, 2009 silverorange
 * @license   http://opensource.org/licenses/mit-license.php MIT License
 * @link      http://pear2.php.net/PEAR2_Console_CommandLine
 * @since     Interface available since release 1.1.0
 */
interface CustomMessageProvider
{
    // getWithCustomMesssages() {{{

    /**
     * Retrieves the given string identifier corresponding message.
     *
     * For a list of identifiers please see the provided default message
     * provider.
     *
     * @param string $code     The string identifier of the message
     * @param array  $vars     An array of template variables
     * @param array  $messages An optional array of messages to use. Array
     *                         indexes are message codes.
     *
     * @return string
     * @see PEAR2\Console\CommandLine_MessageProvider
     * @see PEAR2\Console\CommandLine_MessageProvider_Default
     */
    public function getWithCustomMessages(
        $code, $vars = array(), $messages = array()
    );

    // }}}
}


File: /PEAR2\Console\CommandLine\Element.php
<?php

/* vim: set expandtab tabstop=4 shiftwidth=4 softtabstop=4: */

/**
 * This file is part of the PEAR2\Console\CommandLine package.
 *
 * PHP version 5
 *
 * LICENSE: This source file is subject to the MIT license that is available
 * through the world-wide-web at the following URI:
 * http://opensource.org/licenses/mit-license.php
 *
 * @category  Console
 * @package   PEAR2\Console\CommandLine
 * @author    David JEAN LOUIS <izimobil@gmail.com>
 * @copyright 2007-2009 David JEAN LOUIS
 * @license   http://opensource.org/licenses/mit-license.php MIT License
 * @version   0.2.1
 * @link      http://pear2.php.net/PEAR2_Console_CommandLine
 * @since     File available since release 0.1.0
 * @filesource
 */

namespace PEAR2\Console\CommandLine;

/**
 * Class that represent a command line element (an option, or an argument).
 *
 * @category  Console
 * @package   PEAR2\Console\CommandLine
 * @author    David JEAN LOUIS <izimobil@gmail.com>
 * @copyright 2007-2009 David JEAN LOUIS
 * @license   http://opensource.org/licenses/mit-license.php MIT License
 * @link      http://pear2.php.net/PEAR2_Console_CommandLine
 * @since     Class available since release 0.1.0
 */
abstract class Element
{
    // Public properties {{{

    /**
     * The element name.
     *
     * @var string $name Element name
     */
    public $name;

    /**
     * The name of variable displayed in the usage message, if no set it
     * defaults to the "name" property.
     *
     * @var string $help_name Element "help" variable name
     */
    public $help_name;

    /**
     * The element description.
     *
     * @var string $description Element description
     */
    public $description;
     /**
     * The default value of the element if not provided on the command line.
     *
     * @var mixed $default Default value of the option.
     */
    public $default;

    /**
     * Custom errors messages for this element
     *
     * This array is of the form:
     * <code>
     * <?php
     * array(
     *     $messageName => $messageText,
     *     $messageName => $messageText,
     *     ...
     * );
     * ?>
     * </code>
     *
     * If specified, these messages override the messages provided by the
     * default message provider. For example:
     * <code>
     * <?php
     * $messages = array(
     *     'ARGUMENT_REQUIRED' => 'The argument foo is required.',
     * );
     * ?>
     * </code>
     *
     * @var array
     * @see PEAR2\Console\CommandLine_MessageProvider_Default
     */
    public $messages = array();

    // }}}
    // __construct() {{{

    /**
     * Constructor.
     *
     * @param string $name   The name of the element
     * @param array  $params An optional array of parameters
     *
     * @return void
     */
    public function __construct($name = null, $params = array())
    {
        $this->name = $name;
        foreach ($params as $attr => $value) {
            if (property_exists($this, $attr)) {
                $this->$attr = $value;
            }
        }
    }

    // }}}
    // toString() {{{

    /**
     * Returns the string representation of the element.
     *
     * @return string The string representation of the element
     * @todo use __toString() instead
     */
    public function toString()
    {
        return $this->help_name;
    }
    // }}}
    // validate() {{{

    /**
     * Validates the element instance and set it's default values.
     *
     * @return void
     * @throws PEAR2\Console\CommandLine\Exception
     */
    public function validate()
    {
        // if no help_name passed, default to name
        if ($this->help_name == null) {
            $this->help_name = $this->name;
        }
    }

    // }}}
}


File: /PEAR2\Console\CommandLine\Exception.php
<?php

/* vim: set expandtab tabstop=4 shiftwidth=4 softtabstop=4: */

/**
 * This file is part of the PEAR2\Console\CommandLine package.
 *
 * PHP version 5
 *
 * LICENSE: This source file is subject to the MIT license that is available
 * through the world-wide-web at the following URI:
 * http://opensource.org/licenses/mit-license.php
 *
 * @category  Console 
 * @package   PEAR2\Console\CommandLine
 * @author    David JEAN LOUIS <izimobil@gmail.com>
 * @copyright 2007-2009 David JEAN LOUIS
 * @license   http://opensource.org/licenses/mit-license.php MIT License 
 * @version   0.2.1
 * @link      http://pear2.php.net/PEAR2_Console_CommandLine
 * @since     File available since release 0.1.0
 * @filesource
 */

namespace PEAR2\Console\CommandLine;

use Exception as E;

/**
 * Class for exceptions raised by the PEAR2\Console\CommandLine package.
 *
 * @category  Console
 * @package   PEAR2\Console\CommandLine
 * @author    David JEAN LOUIS <izimobil@gmail.com>
 * @copyright 2007-2009 David JEAN LOUIS
 * @license   http://opensource.org/licenses/mit-license.php MIT License
 * @link      http://pear2.php.net/PEAR2_Console_CommandLine
 * @since     Class available since release 0.1.0
 */
class Exception extends E
{
    // Codes constants {{{

    /**#@+
     * Exception code constants.
     */
    const OPTION_VALUE_REQUIRED   = 1;
    const OPTION_VALUE_UNEXPECTED = 2;
    const OPTION_VALUE_TYPE_ERROR = 3;
    const OPTION_UNKNOWN          = 4;
    const ARGUMENT_REQUIRED       = 5;
    const INVALID_SUBCOMMAND      = 6;
    /**#@-*/

    // }}}
    // factory() {{{

    /**
     * Convenience method that builds the exception with the array of params by
     * calling the message provider class.
     *
     * @param string                    $code     The string identifier of the
     *                                            exception.
     * @param array                     $params   Array of template vars/values
     * @param PEAR2\Console\CommandLine $parser   An instance of the parser
     * @param array                     $messages An optional array of messages
     *                                            passed to the message provider.
     *
     * @return PEAR2\Console\CommandLine\Exception The exception instance
     */
    public static function factory(
        $code, $params, $parser, array $messages = array()
    ) {
        $provider = $parser->message_provider;
        if ($provider instanceof CommandLine\CustomMessageProvider) {
            $msg = $provider->getWithCustomMessages(
                $code,
                $params,
                $messages
            );
        } else {
            $msg = $provider->get($code, $params);
        }
        $const = '\PEAR2\Console\CommandLine\Exception::' . $code;
        $code  = defined($const) ? constant($const) : 0;
        return new static($msg, $code);
    }

    // }}}
}


File: /PEAR2\Console\CommandLine\MessageProvider\Default.php
<?php

/* vim: set expandtab tabstop=4 shiftwidth=4 softtabstop=4: */

/**
 * This file is part of the PEAR2\Console\CommandLine package.
 *
 * PHP version 5
 *
 * LICENSE: This source file is subject to the MIT license that is available
 * through the world-wide-web at the following URI:
 * http://opensource.org/licenses/mit-license.php
 *
 * @category  Console
 * @package   PEAR2\Console\CommandLine
 * @author    David JEAN LOUIS <izimobil@gmail.com>
 * @copyright 2007-2009 David JEAN LOUIS
 * @license   http://opensource.org/licenses/mit-license.php MIT License
 * @version   0.2.1
 * @link      http://pear2.php.net/PEAR2_Console_CommandLine
 * @since     File available since release 0.1.0
 * @filesource
 */

namespace PEAR2\Console\CommandLine;

/**
 * Lightweight class that manages messages used by PEAR2\Console\CommandLine package,
 * allowing the developper to customize these messages, for example to
 * internationalize a command line frontend.
 *
 * @category  Console
 * @package   PEAR2\Console\CommandLine
 * @author    David JEAN LOUIS <izimobil@gmail.com>
 * @copyright 2007-2009 David JEAN LOUIS
 * @license   http://opensource.org/licenses/mit-license.php MIT License
 * @link      http://pear2.php.net/PEAR2_Console_CommandLine
 * @since     Class available since release 0.1.0
 */
class MessageProvider_Default
    implements MessageProvider,
    CustomMessageProvider
{
    // Properties {{{

    /**
     * Associative array of messages
     *
     * @var array $messages
     */
    protected $messages = array(
        'OPTION_VALUE_REQUIRED'   => 'Option "{$name}" requires a value.',
        'OPTION_VALUE_UNEXPECTED' => 'Option "{$name}" does not expect a value (got "{$value}").',
        'OPTION_VALUE_NOT_VALID'  => 'Option "{$name}" must be one of the following: "{$choices}" (got "{$value}").',
        'OPTION_VALUE_TYPE_ERROR' => 'Option "{$name}" requires a value of type {$type} (got "{$value}").',
        'OPTION_AMBIGUOUS'        => 'Ambiguous option "{$name}", can be one of the following: {$matches}.',
        'OPTION_UNKNOWN'          => 'Unknown option "{$name}".',
        'ARGUMENT_REQUIRED'       => 'You must provide at least {$argnum} argument{$plural}.',
        'PROG_HELP_LINE'          => 'Type "{$progname} --help" to get help.',
        'PROG_VERSION_LINE'       => '{$progname} version {$version}.',
        'COMMAND_HELP_LINE'       => 'Type "{$progname} <command> --help" to get help on specific command.',
        'USAGE_WORD'              => 'Usage',
        'OPTION_WORD'             => 'Options',
        'ARGUMENT_WORD'           => 'Arguments',
        'COMMAND_WORD'            => 'Commands',
        'PASSWORD_PROMPT'         => 'Password: ',
        'PASSWORD_PROMPT_ECHO'    => 'Password (warning: will echo): ',
        'INVALID_CUSTOM_INSTANCE' => 'Instance does not implement the required interface',
        'LIST_OPTION_MESSAGE'     => 'lists valid choices for option {$name}',
        'LIST_DISPLAYED_MESSAGE'  => 'Valid choices are: ',
        'INVALID_SUBCOMMAND'      => 'Command "{$command}" is not valid.',
        'SUBCOMMAND_REQUIRED'     => 'Please enter one of the following command: {$commands}.',
    );

    // }}}
    // get() {{{

    /**
     * Retrieve the given string identifier corresponding message.
     *
     * @param string $code The string identifier of the message
     * @param array  $vars An array of template variables
     *
     * @return string
     */
    public function get($code, $vars = array())
    {
        if (!isset($this->messages[$code])) {
            return 'UNKNOWN';
        }
        return $this->replaceTemplateVars($this->messages[$code], $vars);
    }

    // }}}
    // getWithCustomMessages() {{{

    /**
     * Retrieve the given string identifier corresponding message.
     *
     * @param string $code     The string identifier of the message
     * @param array  $vars     An array of template variables
     * @param array  $messages An optional array of messages to use. Array
     *                         indexes are message codes.
     *
     * @return string
     */
    public function getWithCustomMessages(
        $code, $vars = array(), $messages = array()
    ) {
        // get message
        if (isset($messages[$code])) {
            $message = $messages[$code];
        } elseif (isset($this->messages[$code])) {
            $message = $this->messages[$code];
        } else {
            $message = 'UNKNOWN';
        }
        return $this->replaceTemplateVars($message, $vars);
    }

    // }}}
    // replaceTemplateVars() {{{

    /**
     * Replaces template vars in a message
     *
     * @param string $message The message
     * @param array  $vars    An array of template variables
     *
     * @return string
     */
    protected function replaceTemplateVars($message, $vars = array())
    {
        $tmpkeys = array_keys($vars);
        $keys    = array();
        foreach ($tmpkeys as $key) {
            $keys[] = '{$' . $key . '}';
        }
        return str_replace($keys, array_values($vars), $message);
    }

    // }}}
}


File: /PEAR2\Console\CommandLine\MessageProvider.php
<?php

/* vim: set expandtab tabstop=4 shiftwidth=4 softtabstop=4: */

/**
 * This file is part of the PEAR2\Console\CommandLine package.
 *
 * PHP version 5
 *
 * LICENSE: This source file is subject to the MIT license that is available
 * through the world-wide-web at the following URI:
 * http://opensource.org/licenses/mit-license.php
 *
 * @category  Console 
 * @package   PEAR2\Console\CommandLine
 * @author    David JEAN LOUIS <izimobil@gmail.com>
 * @copyright 2007-2009 David JEAN LOUIS
 * @license   http://opensource.org/licenses/mit-license.php MIT License 
 * @version   0.2.1
 * @link      http://pear2.php.net/PEAR2_Console_CommandLine
 * @since     File available since release 0.1.0
 * @filesource
 */

namespace PEAR2\Console\CommandLine;

/**
 * Message providers common interface, all message providers must implement
 * this interface.
 *
 * @category  Console
 * @package   PEAR2\Console\CommandLine
 * @author    David JEAN LOUIS <izimobil@gmail.com>
 * @copyright 2007-2009 David JEAN LOUIS
 * @license   http://opensource.org/licenses/mit-license.php MIT License
 * @link      http://pear2.php.net/PEAR2_Console_CommandLine
 * @since     Class available since release 0.1.0
 */
interface MessageProvider
{
    // get() {{{

    /**
     * Retrieves the given string identifier corresponding message.
     * For a list of identifiers please see the provided default message 
     * provider.
     *
     * @param string $code The string identifier of the message
     * @param array  $vars An array of template variables
     *
     * @return string
     * @see PEAR2\Console\CommandLine_MessageProvider_Default
     */
    public function get($code, $vars=array());

    // }}}
}


File: /PEAR2\Console\CommandLine\Option.php
<?php

/* vim: set expandtab tabstop=4 shiftwidth=4 softtabstop=4: */

/**
 * This file is part of the PEAR2\Console\CommandLine package.
 *
 * PHP version 5
 *
 * LICENSE: This source file is subject to the MIT license that is available
 * through the world-wide-web at the following URI:
 * http://opensource.org/licenses/mit-license.php
 *
 * @category  Console
 * @package   PEAR2\Console\CommandLine
 * @author    David JEAN LOUIS <izimobil@gmail.com>
 * @copyright 2007-2009 David JEAN LOUIS
 * @license   http://opensource.org/licenses/mit-license.php MIT License
 * @version   0.2.1
 * @link      http://pear2.php.net/PEAR2_Console_CommandLine
 * @since     File available since release 0.1.0
 * @filesource
 */

namespace PEAR2\Console\CommandLine;

use PEAR2\Console;

/**
 * Class that represent a commandline option.
 *
 * @category  Console
 * @package   PEAR2\Console\CommandLine
 * @author    David JEAN LOUIS <izimobil@gmail.com>
 * @copyright 2007-2009 David JEAN LOUIS
 * @license   http://opensource.org/licenses/mit-license.php MIT License
 * @link      http://pear2.php.net/PEAR2_Console_CommandLine
 * @since     Class available since release 0.1.0
 */
class Option extends Element
{
    // Public properties {{{

    /**
     * The option short name (ex: -v).
     *
     * @var string $short_name Short name of the option
     */
    public $short_name;

    /**
     * The option long name (ex: --verbose).
     *
     * @var string $long_name Long name of the option
     */
    public $long_name;

    /**
     * The option action, defaults to "StoreString".
     *
     * @var string $action Option action
     */
    public $action = 'StoreString';

    /**
     * An array of possible values for the option. If this array is not empty
     * and the value passed is not in the array an exception is raised.
     * This only make sense for actions that accept values of course.
     *
     * @var array $choices Valid choices for the option
     */
    public $choices = array();

    /**
     * The callback function (or method) to call for an action of type
     * Callback, this can be any callable supported by the php function
     * call_user_func.
     *
     * Example:
     *
     * <code>
     * $parser->addOption('myoption', array(
     *     'short_name' => '-m',
     *     'long_name'  => '--myoption',
     *     'action'     => 'Callback',
     *     'callback'   => 'myCallbackFunction'
     * ));
     * </code>
     *
     * @var callable $callback The option callback
     */
    public $callback;

    /**
     * An associative array of additional params to pass to the class
     * corresponding to the action, this array will also be passed to the
     * callback defined for an action of type Callback, Example:
     *
     * <code>
     * // for a custom action
     * $parser->addOption('myoption', array(
     *     'short_name'    => '-m',
     *     'long_name'     => '--myoption',
     *     'action'        => 'MyCustomAction',
     *     'action_params' => array('foo'=>true, 'bar'=>false)
     * ));
     *
     * // if the user type:
     * // $ <yourprogram> -m spam
     * // in your MyCustomAction class the execute() method will be called
     * // with the value 'spam' as first parameter and
     * // array('foo'=>true, 'bar'=>false) as second parameter
     * </code>
     *
     * @var array $action_params Additional parameters to pass to the action
     */
    public $action_params = array();

    /**
     * For options that expect an argument, this property tells the parser if
     * the option argument is optional and can be ommited.
     *
     * @var bool $argumentOptional Whether the option arg is optional or not
     */
    public $argument_optional = false;

    /**
     * For options that uses the "choice" property only.
     * Adds a --list-<choice> option to the parser that displays the list of
     * choices for the option.
     *
     * @var bool $add_list_option Whether to add a list option or not
     */
    public $add_list_option = false;

    // }}}
    // Private properties {{{

    /**
     * When an action is called remember it to allow for multiple calls.
     *
     * @var object $action_instance Placeholder for action
     */
    private $_action_instance = null;

    // }}}
    // __construct() {{{

    /**
     * Constructor.
     *
     * @param string $name   The name of the option
     * @param array  $params An optional array of parameters
     *
     * @return void
     */
    public function __construct($name = null, $params = array())
    {
        parent::__construct($name, $params);
        if ($this->action == 'Password') {
            // special case for Password action, password can be passed to the
            // commandline or prompted by the parser
            $this->argument_optional = true;
        }
    }

    // }}}
    // toString() {{{

    /**
     * Returns the string representation of the option.
     *
     * @param string $delim Delimiter to use between short and long option
     *
     * @return string The string representation of the option
     * @todo use __toString() instead
     */
    public function toString($delim = ", ")
    {
        $ret     = '';
        $padding = '';
        if ($this->short_name != null) {
            $ret .= $this->short_name;
            if ($this->expectsArgument()) {
                $ret .= ' ' . $this->help_name;
            }
            $padding = $delim;
        }
        if ($this->long_name != null) {
            $ret .= $padding . $this->long_name;
            if ($this->expectsArgument()) {
                $ret .= '=' . $this->help_name;
            }
        }
        return $ret;
    }

    // }}}
    // expectsArgument() {{{

    /**
     * Returns true if the option requires one or more argument and false
     * otherwise.
     *
     * @return bool Whether the option expects an argument or not
     */
    public function expectsArgument()
    {
        if ($this->action == 'StoreTrue'
            || $this->action == 'StoreFalse'
            || $this->action == 'Help'
            || $this->action == 'Version'
            || $this->action == 'Counter'
            || $this->action == 'List'
        ) {
            return false;
        }
        return true;
    }

    // }}}
    // dispatchAction() {{{

    /**
     * Formats the value $value according to the action of the option and
     * updates the passed PEAR2\Console\CommandLine_Result object.
     *
     * @param mixed                            $value  The value to format
     * @param PEAR2\Console\CommandLine_Result $result The result instance
     * @param PEAR2\Console\CommandLine        $parser The parser instance
     *
     * @return void
     * @throws PEAR2\Console\CommandLine\Exception
     */
    public function dispatchAction($value, $result, $parser)
    {
        $actionInfo = Console\CommandLine::$actions[$this->action];
        $clsname    = $actionInfo[0];
        if ($this->_action_instance === null) {
            $this->_action_instance  = new $clsname($result, $this, $parser);
        }

        // check value is in option choices
        if (!empty($this->choices)
            && !in_array(
                $this->_action_instance->format($value),
                $this->choices
            )
        ) {
            throw Console\CommandLine\Exception::factory(
                'OPTION_VALUE_NOT_VALID',
                array(
                    'name'    => $this->name,
                    'choices' => implode('", "', $this->choices),
                    'value'   => $value,
                ),
                $parser,
                $this->messages
            );
        }
        $this->_action_instance->execute($value, $this->action_params);
    }

    // }}}
    // validate() {{{

    /**
     * Validates the option instance.
     *
     * @return void
     * @throws PEAR2\Console\CommandLine\Exception
     * @todo use exceptions instead
     */
    public function validate()
    {
        // check if the option name is valid
        if (!preg_match(
            '/^[a-zA-Z_\x7f-\xff]+[a-zA-Z0-9_\x7f-\xff]*$/',
            $this->name
        )
        ) {
            Console\CommandLine::triggerError(
                'option_bad_name',
                E_USER_ERROR,
                array('{$name}' => $this->name)
            );
        }
        // call the parent validate method
        parent::validate();
        // a short_name or a long_name must be provided
        if ($this->short_name == null && $this->long_name == null) {
            Console\CommandLine::triggerError(
                'option_long_and_short_name_missing',
                E_USER_ERROR,
                array('{$name}' => $this->name)
            );
        }
        // check if the option short_name is valid
        if ($this->short_name != null
            && !(preg_match('/^\-[a-zA-Z]{1}$/', $this->short_name))
        ) {
            Console\CommandLine::triggerError(
                'option_bad_short_name',
                E_USER_ERROR,
                array(
                    '{$name}' => $this->name,
                    '{$short_name}' => $this->short_name
                )
            );
        }
        // check if the option long_name is valid
        if ($this->long_name != null
            && !preg_match('/^\-\-[a-zA-Z]+[a-zA-Z0-9_\-]*$/', $this->long_name)
        ) {
            Console\CommandLine::triggerError(
                'option_bad_long_name',
                E_USER_ERROR,
                array(
                    '{$name}' => $this->name,
                    '{$long_name}' => $this->long_name
                )
            );
        }
        // check if we have a valid action
        if (!is_string($this->action)) {
            Console\CommandLine::triggerError(
                'option_bad_action',
                E_USER_ERROR,
                array('{$name}' => $this->name)
            );
        }
        if (!isset(Console\CommandLine::$actions[$this->action])) {
            Console\CommandLine::triggerError(
                'option_unregistered_action',
                E_USER_ERROR,
                array(
                    '{$action}' => $this->action,
                    '{$name}' => $this->name
                )
            );
        }
        // if the action is a callback, check that we have a valid callback
        if ($this->action == 'Callback' && !is_callable($this->callback)) {
            Console\CommandLine::triggerError(
                'option_invalid_callback',
                E_USER_ERROR,
                array('{$name}' => $this->name)
            );
        }
    }

    // }}}
    // setDefaults() {{{

    /**
     * Set the default value according to the configured action.
     *
     * Note that for backward compatibility issues this method is only called
     * when the 'force_options_defaults' is set to true, it will become the
     * default behaviour in the next major release of PEAR2\Console\CommandLine.
     *
     * @return void
     */
    public function setDefaults()
    {
        if ($this->default !== null) {
            // already set
            return;
        }
        switch ($this->action) {
        case 'Counter':
        case 'StoreInt':
            $this->default = 0;
            break;
        case 'StoreFloat':
            $this->default = 0.0;
            break;
        case 'StoreArray':
            $this->default = array();
            break;
        case 'StoreTrue':
            $this->default = false;
            break;
        case 'StoreFalse':
            $this->default = true;
            break;
        default:
            return;
        }
    }

    // }}}
}


File: /PEAR2\Console\CommandLine\Outputter\Default.php
<?php

/* vim: set expandtab tabstop=4 shiftwidth=4 softtabstop=4: */

/**
 * This file is part of the PEAR2\Console\CommandLine package.
 *
 * PHP version 5
 *
 * LICENSE: This source file is subject to the MIT license that is available
 * through the world-wide-web at the following URI:
 * http://opensource.org/licenses/mit-license.php
 *
 * @category  Console 
 * @package   PEAR2\Console\CommandLine
 * @author    David JEAN LOUIS <izimobil@gmail.com>
 * @copyright 2007-2009 David JEAN LOUIS
 * @license   http://opensource.org/licenses/mit-license.php MIT License 
 * @version   0.2.1
 * @link      http://pear2.php.net/PEAR2_Console_CommandLine
 * @since     File available since release 0.1.0
 * @filesource
 */

namespace PEAR2\Console\CommandLine;

/**
 * PEAR2\Console\CommandLine default Outputter.
 *
 * @category  Console
 * @package   PEAR2\Console\CommandLine
 * @author    David JEAN LOUIS <izimobil@gmail.com>
 * @copyright 2007-2009 David JEAN LOUIS
 * @license   http://opensource.org/licenses/mit-license.php MIT License
 * @link      http://pear2.php.net/PEAR2_Console_CommandLine
 * @since     Class available since release 0.1.0
 */
class Outputter_Default implements Outputter
{
    // stdout() {{{

    /**
     * Writes the message $msg to STDOUT.
     *
     * @param string $msg The message to output
     *
     * @return void
     */
    public function stdout($msg)
    {
        if (defined('STDOUT')) {
            fwrite(STDOUT, $msg);
        } else {
            echo $msg;
        }
    }

    // }}}
    // stderr() {{{

    /**
     * Writes the message $msg to STDERR.
     *
     * @param string $msg The message to output
     *
     * @return void
     */
    public function stderr($msg)
    {
        if (defined('STDERR')) {
            fwrite(STDERR, $msg);
        } else {
            echo $msg;
        }
    }

    // }}}
}


File: /PEAR2\Console\CommandLine\Outputter.php
<?php

/* vim: set expandtab tabstop=4 shiftwidth=4 softtabstop=4: */

/**
 * This file is part of the PEAR2\Console\CommandLine package.
 *
 * PHP version 5
 *
 * LICENSE: This source file is subject to the MIT license that is available
 * through the world-wide-web at the following URI:
 * http://opensource.org/licenses/mit-license.php
 *
 * @category  Console 
 * @package   PEAR2\Console\CommandLine
 * @author    David JEAN LOUIS <izimobil@gmail.com>
 * @copyright 2007-2009 David JEAN LOUIS
 * @license   http://opensource.org/licenses/mit-license.php MIT License 
 * @version   0.2.1
 * @link      http://pear2.php.net/PEAR2_Console_CommandLine
 * @since     File available since release 0.1.0
 * @filesource
 */

namespace PEAR2\Console\CommandLine;

/**
 * Outputters common interface, all outputters must implement this interface.
 *
 * @category  Console
 * @package   PEAR2\Console\CommandLine
 * @author    David JEAN LOUIS <izimobil@gmail.com>
 * @copyright 2007-2009 David JEAN LOUIS
 * @license   http://opensource.org/licenses/mit-license.php MIT License
 * @link      http://pear2.php.net/PEAR2_Console_CommandLine
 * @since     Class available since release 0.1.0
 */
interface Outputter
{
    // stdout() {{{

    /**
     * Processes the output for a message that should be displayed on STDOUT.
     *
     * @param string $msg The message to output
     *
     * @return void
     */
    public function stdout($msg);

    // }}}
    // stderr() {{{

    /**
     * Processes the output for a message that should be displayed on STDERR.
     *
     * @param string $msg The message to output
     *
     * @return void
     */
    public function stderr($msg);

    // }}}
}


File: /PEAR2\Console\CommandLine\Renderer\Default.php
<?php

/* vim: set expandtab tabstop=4 shiftwidth=4 softtabstop=4: */

/**
 * This file is part of the PEAR2\Console\CommandLine package.
 *
 * PHP version 5
 *
 * LICENSE: This source file is subject to the MIT license that is available
 * through the world-wide-web at the following URI:
 * http://opensource.org/licenses/mit-license.php
 *
 * @category  Console
 * @package   PEAR2\Console\CommandLine
 * @author    David JEAN LOUIS <izimobil@gmail.com>
 * @copyright 2007-2009 David JEAN LOUIS
 * @license   http://opensource.org/licenses/mit-license.php MIT License
 * @version   0.2.1
 * @link      http://pear2.php.net/PEAR2_Console_CommandLine
 * @since     File available since release 0.1.0
 */

namespace PEAR2\Console\CommandLine;

/**
 * PEAR2\Console\CommandLine default renderer.
 *
 * @category  Console
 * @package   PEAR2\Console\CommandLine
 * @author    David JEAN LOUIS <izimobil@gmail.com>
 * @copyright 2007-2009 David JEAN LOUIS
 * @license   http://opensource.org/licenses/mit-license.php MIT License
 * @link      http://pear2.php.net/PEAR2_Console_CommandLine
 * @since     Class available since release 0.1.0
 */
class Renderer_Default implements Renderer
{
    // Properties {{{

    /**
     * Integer that define the max width of the help text.
     *
     * @var integer $line_width Line width
     */
    public $line_width = 75;

    /**
     * Integer that define the max width of the help text.
     *
     * @var integer $line_width Line width
     */
    public $options_on_different_lines = false;

    /**
     * An instance of PEAR2\Console\CommandLine.
     *
     * @var PEAR2\Console\CommandLine $parser The parser
     */
    public $parser = false;

    // }}}
    // __construct() {{{

    /**
     * Constructor.
     *
     * @param object $parser A PEAR2\Console\CommandLine instance
     *
     * @return void
     */
    public function __construct($parser = false)
    {
        $this->parser = $parser;
    }

    // }}}
    // usage() {{{

    /**
     * Returns the full usage message.
     *
     * @return string The usage message
     */
    public function usage()
    {
        $ret = '';
        if (!empty($this->parser->description)) {
            $ret .= $this->description() . "\n\n";
        }
        $ret .= $this->usageLine() . "\n";
        if (count($this->parser->commands) > 0) {
            $ret .= $this->commandUsageLine() . "\n";
        }
        if (count($this->parser->options) > 0) {
            $ret .= "\n" . $this->optionList() . "\n";
        }
        if (count($this->parser->args) > 0) {
            $ret .= "\n" . $this->argumentList() . "\n";
        }
        if (count($this->parser->commands) > 0) {
            $ret .= "\n" . $this->commandList() . "\n";
        }
        $ret .= "\n";
        return $ret;
    }
    // }}}
    // error() {{{

    /**
     * Returns a formatted error message.
     *
     * @param string $error The error message to format
     *
     * @return string The error string
     */
    public function error($error)
    {
        $ret = 'Error: ' . $error . "\n";
        if ($this->parser->add_help_option) {
            $name = $this->name();
            $ret .= $this->wrap(
                $this->parser->message_provider->get(
                    'PROG_HELP_LINE',
                    array('progname' => $name)
                )
            ) . "\n";
            if (count($this->parser->commands) > 0) {
                $ret .= $this->wrap(
                    $this->parser->message_provider->get(
                        'COMMAND_HELP_LINE',
                        array('progname' => $name)
                    )
                ) . "\n";
            }
        }
        return $ret;
    }

    // }}}
    // version() {{{

    /**
     * Returns the program version string.
     *
     * @return string The version string
     */
    public function version()
    {
        return $this->parser->message_provider->get(
            'PROG_VERSION_LINE',
            array(
                'progname' => $this->name(),
                'version'  => $this->parser->version
            )
        ) . "\n";
    }

    // }}}
    // name() {{{

    /**
     * Returns the full name of the program or the sub command
     *
     * @return string The name of the program
     */
    protected function name()
    {
        $name   = $this->parser->name;
        $parent = $this->parser->parent;
        while ($parent) {
            if (count($parent->options) > 0) {
                $name = '['
                    . strtolower(
                        $this->parser->message_provider->get(
                            'OPTION_WORD',
                            array('plural' => 's')
                        )
                    ) . '] ' . $name;
            }
            $name = $parent->name . ' ' . $name;
            $parent = $parent->parent;
        }
        return $this->wrap($name);
    }

    // }}}
    // description() {{{

    /**
     * Returns the command line description message.
     *
     * @return string The description message
     */
    protected function description()
    {
        return $this->wrap($this->parser->description);
    }

    // }}}
    // usageLine() {{{

    /**
     * Returns the command line usage message
     *
     * @return string the usage message
     */
    protected function usageLine()
    {
        $usage = $this->parser->message_provider->get('USAGE_WORD') . ":\n";
        $ret   = $usage . '  ' . $this->name();
        if (count($this->parser->options) > 0) {
            $ret .= ' ['
                . strtolower($this->parser->message_provider->get('OPTION_WORD'))
                . ']';
        }
        if (count($this->parser->args) > 0) {
            foreach ($this->parser->args as $name=>$arg) {
                $arg_str = $arg->help_name;
                if ($arg->multiple) {
                    $arg_str .= '1 ' . $arg->help_name . '2 ...';
                }
                if ($arg->optional) {
                    $arg_str = '[' . $arg_str . ']';
                }
                $ret .= ' ' . $arg_str;
            }
        }
        return $this->columnWrap($ret, 2);
    }

    // }}}
    // commandUsageLine() {{{

    /**
     * Returns the command line usage message for subcommands.
     *
     * @return string The usage line
     */
    protected function commandUsageLine()
    {
        if (count($this->parser->commands) == 0) {
            return '';
        }
        $ret = '  ' . $this->name();
        if (count($this->parser->options) > 0) {
            $ret .= ' ['
                . strtolower($this->parser->message_provider->get('OPTION_WORD'))
                . ']';
        }
        $ret       .= " <command>";
        $hasArgs    = false;
        $hasOptions = false;
        foreach ($this->parser->commands as $command) {
            if (!$hasArgs && count($command->args) > 0) {
                $hasArgs = true;
            }
            if (!$hasOptions && ($command->add_help_option
                || $command->add_version_option
                || count($command->options) > 0)
            ) {
                $hasOptions = true;
            }
        }
        if ($hasOptions) {
            $ret .= ' [options]';
        }
        if ($hasArgs) {
            $ret .= ' [args]';
        }
        return $this->columnWrap($ret, 2);
    }

    // }}}
    // argumentList() {{{

    /**
     * Render the arguments list that will be displayed to the user, you can
     * override this method if you want to change the look of the list.
     *
     * @return string The formatted argument list
     */
    protected function argumentList()
    {
        $col  = 0;
        $args = array();
        foreach ($this->parser->args as $arg) {
            $argstr = '  ' . $arg->toString();
            $args[] = array($argstr, $arg->description);
            $ln     = strlen($argstr);
            if ($col < $ln) {
                $col = $ln;
            }
        }
        $ret = $this->parser->message_provider->get('ARGUMENT_WORD') . ":";
        foreach ($args as $arg) {
            $text = str_pad($arg[0], $col) . '  ' . $arg[1];
            $ret .= "\n" . $this->columnWrap($text, $col+2);
        }
        return $ret;
    }

    // }}}
    // optionList() {{{

    /**
     * Render the options list that will be displayed to the user, you can
     * override this method if you want to change the look of the list.
     *
     * @return string The formatted option list
     */
    protected function optionList()
    {
        $col     = 0;
        $options = array();
        foreach ($this->parser->options as $option) {
            $delim    = $this->options_on_different_lines ? "\n" : ', ';
            $optstr   = $option->toString($delim);
            $lines    = explode("\n", $optstr);
            $lines[0] = '  ' . $lines[0];
            if (count($lines) > 1) {
                $lines[1] = '  ' . $lines[1];
                $ln       = strlen($lines[1]);
            } else {
                $ln = strlen($lines[0]);
            }
            $options[] = array($lines, $option->description);
            if ($col < $ln) {
                $col = $ln;
            }
        }
        $ret = $this->parser->message_provider->get('OPTION_WORD') . ":";
        foreach ($options as $option) {
            if (count($option[0]) > 1) {
                $text = str_pad($option[0][1], $col) . '  ' . $option[1];
                $pre  = $option[0][0] . "\n";
            } else {
                $text = str_pad($option[0][0], $col) . '  ' . $option[1];
                $pre  = '';
            }
            $ret .= "\n" . $pre . $this->columnWrap($text, $col+2);
        }
        return $ret;
    }

    // }}}
    // commandList() {{{

    /**
     * Render the command list that will be displayed to the user, you can
     * override this method if you want to change the look of the list.
     *
     * @return string The formatted subcommand list
     */
    protected function commandList()
    {

        $commands = array();
        $col      = 0;
        foreach ($this->parser->commands as $cmdname=>$command) {
            $cmdname    = '  ' . $cmdname;
            $commands[] = array($cmdname, $command->description, $command->aliases);
            $ln         = strlen($cmdname);
            if ($col < $ln) {
                $col = $ln;
            }
        }
        $ret = $this->parser->message_provider->get('COMMAND_WORD') . ":";
        foreach ($commands as $command) {
            $text = str_pad($command[0], $col) . '  ' . $command[1];
            if ($aliasesCount = count($command[2])) {
                $pad = '';
                $text .= ' (';
                $text .= $aliasesCount > 1 ? 'aliases: ' : 'alias: ';
                foreach ($command[2] as $alias) {
                    $text .= $pad . $alias;
                    $pad   = ', ';
                }
                $text .= ')';
            }
            $ret .= "\n" . $this->columnWrap($text, $col+2);
        }
        return $ret;
    }

    // }}}
    // wrap() {{{

    /**
     * Wraps the text passed to the method.
     *
     * @param string $text The text to wrap
     * @param int    $lw   The column width (defaults to line_width property)
     *
     * @return string The wrapped text
     */
    protected function wrap($text, $lw=null)
    {
        if ($this->line_width > 0) {
            if ($lw === null) {
                $lw = $this->line_width;
            }
            return wordwrap($text, $lw, "\n", false);
        }
        return $text;
    }

    // }}}
    // columnWrap() {{{

    /**
     * Wraps the text passed to the method at the specified width.
     *
     * @param string $text The text to wrap
     * @param int    $cw   The wrap width
     *
     * @return string The wrapped text
     */
    protected function columnWrap($text, $cw)
    {
        $tokens = explode("\n", $this->wrap($text));
        $ret    = $tokens[0];
        $text   = trim(substr($text, strlen($ret)));
        if (empty($text)) {
            return $ret;
        }

        $chunks = $this->wrap($text, $this->line_width - $cw);
        $tokens = explode("\n", $chunks);
        foreach ($tokens as $token) {
            if (!empty($token)) {
                $ret .= "\n" . str_repeat(' ', $cw) . $token;
            } else {
                $ret .= "\n";
            }
        }
        return $ret;
    }

    // }}}
}


File: /PEAR2\Console\CommandLine\Renderer.php
<?php

/* vim: set expandtab tabstop=4 shiftwidth=4 softtabstop=4: */

/**
 * This file is part of the PEAR2\Console\CommandLine package.
 *
 * PHP version 5
 *
 * LICENSE: This source file is subject to the MIT license that is available
 * through the world-wide-web at the following URI:
 * http://opensource.org/licenses/mit-license.php
 *
 * @category  Console 
 * @package   PEAR2\Console\CommandLine
 * @author    David JEAN LOUIS <izimobil@gmail.com>
 * @copyright 2007-2009 David JEAN LOUIS
 * @license   http://opensource.org/licenses/mit-license.php MIT License 
 * @version   0.2.1
 * @link      http://pear2.php.net/PEAR2_Console_CommandLine
 * @since     File available since release 0.1.0
 * @filesource
 */

namespace PEAR2\Console\CommandLine;

/**
 * Renderers common interface, all renderers must implement this interface.
 *
 * @category  Console
 * @package   PEAR2\Console\CommandLine
 * @author    David JEAN LOUIS <izimobil@gmail.com>
 * @copyright 2007-2009 David JEAN LOUIS
 * @license   http://opensource.org/licenses/mit-license.php MIT License
 * @link      http://pear2.php.net/PEAR2_Console_CommandLine
 * @since     Class available since release 0.1.0
 */
interface Renderer
{
    // usage() {{{

    /**
     * Returns the full usage message.
     *
     * @return string The usage message
     */
    public function usage();

    // }}}
    // error() {{{

    /**
     * Returns a formatted error message.
     *
     * @param string $error The error message to format
     *
     * @return string The error string
     */
    public function error($error);

    // }}}
    // version() {{{

    /**
     * Returns the program version string.
     *
     * @return string The version string
     */
    public function version();

    // }}}
}


File: /PEAR2\Console\CommandLine\Result.php
<?php

/* vim: set expandtab tabstop=4 shiftwidth=4 softtabstop=4: */

/**
 * This file is part of the PEAR2\Console\CommandLine package.
 *
 * PHP version 5
 *
 * LICENSE: This source file is subject to the MIT license that is available
 * through the world-wide-web at the following URI:
 * http://opensource.org/licenses/mit-license.php
 *
 * @category  Console 
 * @package   PEAR2\Console\CommandLine
 * @author    David JEAN LOUIS <izimobil@gmail.com>
 * @copyright 2007-2009 David JEAN LOUIS
 * @license   http://opensource.org/licenses/mit-license.php MIT License 
 * @version   0.2.1
 * @link      http://pear2.php.net/PEAR2_Console_CommandLine
 * @since     File available since release 0.1.0
 * @filesource
 */

namespace PEAR2\Console\CommandLine;

/**
 * A lightweight class to store the result of the command line parsing.
 *
 * @category  Console
 * @package   PEAR2\Console\CommandLine
 * @author    David JEAN LOUIS <izimobil@gmail.com>
 * @copyright 2007-2009 David JEAN LOUIS
 * @license   http://opensource.org/licenses/mit-license.php MIT License
 * @link      http://pear2.php.net/PEAR2_Console_CommandLine
 * @since     Class available since release 0.1.0
 */
class Result
{
    // Public properties {{{

    /**
     * The result options associative array.
     * Key is the name of the option and value its value.
     *
     * @var array $options Result options array
     */
    public $options = array();

    /**
     * The result arguments array.
     *
     * @var array $args Result arguments array
     */
    public $args = array();

    /**
     * Name of the command invoked by the user, false if no command invoked.
     *
     * @var string $command_name Result command name
     */
    public $command_name = false;

    /**
     * A result instance for the subcommand.
     *
     * @var static $command Result instance for the subcommand
     */
    public $command = false;

    // }}}
}


File: /PEAR2\Console\CommandLine\XmlParser.php
<?php

/* vim: set expandtab tabstop=4 shiftwidth=4 softtabstop=4: */

/**
 * This file is part of the PEAR2\Console\CommandLine package.
 *
 * PHP version 5
 *
 * LICENSE: This source file is subject to the MIT license that is available
 * through the world-wide-web at the following URI:
 * http://opensource.org/licenses/mit-license.php
 *
 * @category  Console 
 * @package   PEAR2\Console\CommandLine
 * @author    David JEAN LOUIS <izimobil@gmail.com>
 * @copyright 2007-2009 David JEAN LOUIS
 * @license   http://opensource.org/licenses/mit-license.php MIT License 
 * @version   0.2.1
 * @link      http://pear2.php.net/PEAR2_Console_CommandLine
 * @since     File available since release 0.1.0
 * @filesource
 */

namespace PEAR2\Console\CommandLine;

use PEAR2\Console\CommandLine;

/**
 * Parser for command line xml definitions.
 *
 * @category  Console
 * @package   PEAR2\Console\CommandLine
 * @author    David JEAN LOUIS <izimobil@gmail.com>
 * @copyright 2007-2009 David JEAN LOUIS
 * @license   http://opensource.org/licenses/mit-license.php MIT License
 * @link      http://pear2.php.net/PEAR2_Console_CommandLine
 * @since     Class available since release 0.1.0
 */
class XmlParser
{
    // parse() {{{

    /**
     * Parses the given xml definition file and returns a
     * PEAR2\Console\CommandLine instance constructed with the xml data.
     *
     * @param string $xmlfile The xml file to parse
     *
     * @return PEAR2\Console\CommandLine A parser instance
     */
    public static function parse($xmlfile) 
    {
        if (!is_readable($xmlfile)) {
            CommandLine::triggerError(
                'invalid_xml_file',
                E_USER_ERROR,
                array('{$file}' => $xmlfile)
            );
        }
        $doc = new \DomDocument();
        $doc->load($xmlfile);
        self::validate($doc);
        $nodes = $doc->getElementsByTagName('command');
        $root  = $nodes->item(0);
        return self::_parseCommandNode($root, true);
    }

    // }}}
    // parseString() {{{

    /**
     * Parses the given xml definition string and returns a
     * PEAR2\Console\CommandLine instance constructed with the xml data.
     *
     * @param string $xmlstr The xml string to parse
     *
     * @return PEAR2\Console\CommandLine A parser instance
     */
    public static function parseString($xmlstr) 
    {
        $doc = new \DomDocument();
        $doc->loadXml($xmlstr);
        self::validate($doc);
        $nodes = $doc->getElementsByTagName('command');
        $root  = $nodes->item(0);
        return self::_parseCommandNode($root, true);
    }

    // }}}
    // validate() {{{

    /**
     * Validates the xml definition using Relax NG.
     *
     * @param DomDocument $doc The document to validate
     *
     * @return boolean Whether the xml data is valid or not.
     * @throws PEAR2\Console\CommandLine\Exception
     * @todo use exceptions only
     */
    public static function validate($doc) 
    {
        $rngfile = __DIR__
            . '/../../../../data/pear2.php.net/PEAR2_Console_CommandLine/xmlschema.rng';
        if (!is_file($rngfile)) {
            $rngfile = __DIR__ . '/../../../../data/xmlschema.rng'; 
        }
        if (!is_readable($rngfile)) {
            CommandLine::triggerError(
                'invalid_xml_file',
                E_USER_ERROR, 
                array('{$file}' => $rngfile)
            );
        }
        return $doc->relaxNGValidate($rngfile);
    }

    // }}}
    // _parseCommandNode() {{{

    /**
     * Parses the root command node or a command node and returns the
     * constructed PEAR2\Console\CommandLine or PEAR2\Console\CommandLine_Command
     * instance.
     *
     * @param DomDocumentNode $node       The node to parse
     * @param bool            $isRootNode Whether it is a root node or not
     *
     * @return mixed PEAR2\Console\CommandLine or PEAR2\Console\CommandLine_Command
     */
    private static function _parseCommandNode($node, $isRootNode = false) 
    {
        if ($isRootNode) { 
            $obj = new CommandLine();
        } else {
            $obj = new CommandLine\Command();
        }
        foreach ($node->childNodes as $cNode) {
            $cNodeName = $cNode->nodeName;
            switch ($cNodeName) {
            case 'name':
            case 'description':
            case 'version':
                $obj->$cNodeName = trim($cNode->nodeValue);
                break;
            case 'add_help_option':
            case 'add_version_option':
            case 'force_posix':
                $obj->$cNodeName = self::_bool(trim($cNode->nodeValue));
                break;
            case 'option':
                $obj->addOption(self::_parseOptionNode($cNode));
                break;
            case 'argument':
                $obj->addArgument(self::_parseArgumentNode($cNode));
                break;
            case 'command':
                $obj->addCommand(self::_parseCommandNode($cNode));
                break;
            case 'aliases':
                if (!$isRootNode) {
                    foreach ($cNode->childNodes as $subChildNode) {
                        if ($subChildNode->nodeName == 'alias') {
                            $obj->aliases[] = trim($subChildNode->nodeValue);
                        }
                    }
                }
                break;
            case 'messages':
                $obj->messages = self::_messages($cNode);
                break;
            default:
                break;
            }
        }
        return $obj;
    }

    // }}}
    // _parseOptionNode() {{{

    /**
     * Parses an option node and returns the constructed
     * PEAR2\Console\CommandLine_Option instance.
     *
     * @param DomDocumentNode $node The node to parse
     *
     * @return PEAR2\Console\CommandLine\Option The built option
     */
    private static function _parseOptionNode($node) 
    {
        $obj = new CommandLine\Option($node->getAttribute('name'));
        foreach ($node->childNodes as $cNode) {
            $cNodeName = $cNode->nodeName;
            switch ($cNodeName) {
            case 'choices':
                foreach ($cNode->childNodes as $subChildNode) {
                    if ($subChildNode->nodeName == 'choice') {
                        $obj->choices[] = trim($subChildNode->nodeValue);
                    }
                }
                break;
            case 'messages':
                $obj->messages = self::_messages($cNode);
                break;
            default:
                if (property_exists($obj, $cNodeName)) {
                    $obj->$cNodeName = trim($cNode->nodeValue);
                }
                break;
            }
        }
        if ($obj->action == 'Password') {
            $obj->argument_optional = true;
        }
        return $obj;
    }

    // }}}
    // _parseArgumentNode() {{{

    /**
     * Parses an argument node and returns the constructed 
     * PEAR2\Console\CommandLine_Argument instance.
     *
     * @param DomDocumentNode $node The node to parse
     *
     * @return PEAR2\Console\CommandLine\Argument The built argument
     */
    private static function _parseArgumentNode($node) 
    {
        $obj = new CommandLine\Argument($node->getAttribute('name'));
        foreach ($node->childNodes as $cNode) {
            $cNodeName = $cNode->nodeName;
            switch ($cNodeName) {
            case 'description':
            case 'help_name':
            case 'default':
                $obj->$cNodeName = trim($cNode->nodeValue);
                break;
            case 'multiple':
                $obj->multiple = self::_bool(trim($cNode->nodeValue));
                break;
            case 'optional':
                $obj->optional = self::_bool(trim($cNode->nodeValue));
                break;
            case 'messages':
                $obj->messages = self::_messages($cNode);
                break;
            default:
                break;
            }
        }
        return $obj;
    }

    // }}}
    // _bool() {{{

    /**
     * Returns a boolean according to true/false possible strings.
     * 
     * @param string $str The string to process
     *
     * @return boolean
     */
    private static function _bool($str)
    {
        return in_array((string)$str, array('true', '1', 'on', 'yes'));
    }

    // }}}
    // _messages() {{{

    /**
     * Returns an array of custom messages for the element
     *
     * @param DOMNode $node The messages node to process
     *
     * @return array an array of messages
     *
     * @see PEAR2\Console\CommandLine::$messages
     * @see PEAR2\Console\CommandLine_Element::$messages
     */
    private static function _messages(DOMNode $node)
    {
        $messages = array();

        foreach ($node->childNodes as $cNode) {
            if ($cNode->nodeType == XML_ELEMENT_NODE) {
                $name  = $cNode->getAttribute('name');
                $value = trim($cNode->nodeValue);

                $messages[$name] = $value;
            }
        }

        return $messages;
    }

    // }}}
}


File: /PEAR2\Console\CommandLine.php
<?php

/* vim: set expandtab tabstop=4 shiftwidth=4 softtabstop=4: */

/**
 * This file is part of the PEAR2\Console\CommandLine package.
 *
 * A full featured package for managing command-line options and arguments
 * hightly inspired from python optparse module, it allows the developper to
 * easily build complex command line interfaces.
 *
 * PHP version 5
 *
 * LICENSE: This source file is subject to the MIT license that is available
 * through the world-wide-web at the following URI:
 * http://opensource.org/licenses/mit-license.php
 *
 * @category  Console
 * @package   PEAR2\Console\CommandLine
 * @author    David JEAN LOUIS <izimobil@gmail.com>
 * @copyright 2007-2009 David JEAN LOUIS
 * @license   http://opensource.org/licenses/mit-license.php MIT License
 * @link      http://pear2.php.net/PEAR2_Console_CommandLine
 * @since     Class available since release 0.1.0
 */
namespace PEAR2\Console;

/**
 * Main class for parsing command line options and arguments.
 *
 * There are three ways to create parsers with this class:
 * <code>
 * // direct usage
 * $parser = new PEAR2\Console\CommandLine();
 *
 * // with an xml definition file
 * $parser = PEAR2\Console\CommandLine::fromXmlFile('path/to/file.xml');
 *
 * // with an xml definition string
 * $validXmlString = '..your xml string...';
 * $parser = PEAR2\Console\CommandLine::fromXmlString($validXmlString);
 * </code>
 *
 * @category  Console
 * @package   PEAR2\Console\CommandLine
 * @author    David JEAN LOUIS <izimobil@gmail.com>
 * @copyright 2007-2009 David JEAN LOUIS
 * @license   http://opensource.org/licenses/mit-license.php MIT License
 * @link      http://pear2.php.net/PEAR2_Console_CommandLine
 * @since     File available since release 0.1.0
 * @example   docs/examples/ex1.php
 * @example   docs/examples/ex2.php
 */
class CommandLine
{
    // Public properties {{{

    /**
     * Error messages.
     *
     * @var array $errors Error messages
     * @todo move this to PEAR2\Console\CommandLine\MessageProvider
     */
    public static $errors = array(
        'option_bad_name'                    => 'option name must be a valid php variable name (got: {$name})',
        'argument_bad_name'                  => 'argument name must be a valid php variable name (got: {$name})',
        'argument_no_default'                => 'only optional arguments can have a default value',
        'option_long_and_short_name_missing' => 'you must provide at least an option short name or long name for option "{$name}"',
        'option_bad_short_name'              => 'option "{$name}" short name must be a dash followed by a letter (got: "{$short_name}")',
        'option_bad_long_name'               => 'option "{$name}" long name must be 2 dashes followed by a word (got: "{$long_name}")',
        'option_unregistered_action'         => 'unregistered action "{$action}" for option "{$name}".',
        'option_bad_action'                  => 'invalid action for option "{$name}".',
        'option_invalid_callback'            => 'you must provide a valid callback for option "{$name}"',
        'action_class_does_not_exists'       => 'action "{$name}" class "{$class}" not found, make sure that your class is available before calling PEAR2\Console\CommandLine::registerAction()',
        'invalid_xml_file'                   => 'XML definition file "{$file}" does not exists or is not readable',
        'invalid_rng_file'                   => 'RNG file "{$file}" does not exists or is not readable'
    );

    /**
     * The name of the program, if not given it defaults to argv[0].
     *
     * @var string $name Name of your program
     */
    public $name;

    /**
     * A description text that will be displayed in the help message.
     *
     * @var string $description Description of your program
     */
    public $description = '';

    /**
     * A string that represents the version of the program, if this property is
     * not empty and property add_version_option is not set to false, the
     * command line parser will add a --version option, that will display the
     * property content.
     *
     * @var    string $version
     * @access public
     */
    public $version = '';

    /**
     * Boolean that determine if the command line parser should add the help
     * (-h, --help) option automatically.
     *
     * @var bool $add_help_option Whether to add a help option or not
     */
    public $add_help_option = true;

    /**
     * Boolean that determine if the command line parser should add the version
     * (-v, --version) option automatically.
     * Note that the version option is also generated only if the version
     * property is not empty, it's up to you to provide a version string of
     * course.
     *
     * @var bool $add_version_option Whether to add a version option or not
     */
    public $add_version_option = true;

    /**
     * Boolean that determine if providing a subcommand is mandatory.
     *
     * @var bool $subcommand_required Whether a subcommand is required or not
     */
    public $subcommand_required = false;

    /**
     * The command line parser renderer instance.
     *
     * @var    object that implements PEAR2\Console\CommandLine\Renderer interface
     */
    public $renderer = false;

    /**
     * The command line parser outputter instance.
     *
     * @var PEAR2\Console\CommandLine\Outputter An outputter
     */
    public $outputter = false;

    /**
     * The command line message provider instance.
     *
     * @var PEAR2\Console\CommandLine\MessageProvider A message provider instance
     */
    public $message_provider = false;

    /**
     * Boolean that tells the parser to be POSIX compliant, POSIX demands the
     * following behavior: the first non-option stops option processing.
     *
     * @var bool $force_posix Whether to force posix compliance or not
     */
    public $force_posix = false;

    /**
     * Boolean that tells the parser to set relevant options default values,
     * according to the option action.
     *
     * @see PEAR2\Console\CommandLine\Option::setDefaults()
     * @var bool $force_options_defaults Whether to force option default values
     */
    public $force_options_defaults = false;

    /**
     * An array of PEAR2\Console\CommandLine\Option objects.
     *
     * @var array $options The options array
     */
    public $options = array();

    /**
     * An array of PEAR2\Console\CommandLine\Argument objects.
     *
     * @var array $args The arguments array
     */
    public $args = array();

    /**
     * An array of PEAR2\Console\CommandLine\Command objects (sub commands).
     *
     * @var array $commands The commands array
     */
    public $commands = array();

    /**
     * Parent, only relevant in Command objects but left here for interface
     * convenience.
     *
     * @var PEAR2\Console\CommandLine The parent instance
     * @todo move CommandLine::parent to CommandLine\Command
     */
    public $parent = false;

    /**
     * Array of valid actions for an option, this array will also store user
     * registered actions.
     *
     * The array format is:
     * <pre>
     * array(
     *     <ActionName:string> => array(<ActionClass:string>, <builtin:bool>)
     * )
     * </pre>
     *
     * @var array $actions List of valid actions
     */
    public static $actions = array(
        'StoreTrue'   => array(
            'PEAR2\\Console\\CommandLine\\Action\\StoreTrue', true
        ),
        'StoreFalse'  => array(
            'PEAR2\\Console\\CommandLine\\Action\\StoreFalse', true
        ),
        'StoreString' => array(
            'PEAR2\\Console\\CommandLine\\Action\\StoreString', true
        ),
        'StoreInt'    => array(
            'PEAR2\\Console\\CommandLine\\Action\\StoreInt', true
        ),
        'StoreFloat'  => array(
            'PEAR2\\Console\\CommandLine\\Action\\StoreFloat', true
        ),
        'StoreArray'  => array(
            'PEAR2\\Console\\CommandLine\\Action\\StoreArray', true
        ),
        'Callback'    => array(
            'PEAR2\\Console\\CommandLine\\Action\\Callback', true
        ),
        'Counter'     => array(
            'PEAR2\\Console\\CommandLine\\Action\\Counter', true
        ),
        'Help'        => array(
            'PEAR2\\Console\\CommandLine\\Action\\Help', true
        ),
        'Version'     => array(
            'PEAR2\\Console\\CommandLine\\Action\\Version', true
        ),
        'Password'    => array(
            'PEAR2\\Console\\CommandLine\\Action\\Password', true
        ),
        'List'        => array(
            'PEAR2\\Console\\CommandLine\\Action_List', true
        ),
    );

    /**
     * Custom errors messages for this command
     *
     * This array is of the form:
     * <code>
     * <?php
     * array(
     *     $messageName => $messageText,
     *     $messageName => $messageText,
     *     ...
     * );
     * ?>
     * </code>
     *
     * If specified, these messages override the messages provided by the
     * default message provider. For example:
     * <code>
     * <?php
     * $messages = array(
     *     'ARGUMENT_REQUIRED' => 'The argument foo is required.',
     * );
     * ?>
     * </code>
     *
     * @var array
     * @see PEAR2\Console\CommandLine\MessageProvider_Default
     */
    public $messages = array();

    // }}}
    // {{{ Private properties

    /**
     * Array of options that must be dispatched at the end.
     *
     * @var array $_dispatchLater Options to be dispatched
     */
    private $_dispatchLater = array();

    // }}}
    // __construct() {{{

    /**
     * Constructor.
     * Example:
     *
     * <code>
     * $parser = new PEAR2\Console\CommandLine(array(
     *     'name'               => 'yourprogram', // defaults to argv[0]
     *     'description'        => 'Description of your program',
     *     'version'            => '0.0.1', // your program version
     *     'add_help_option'    => true, // or false to disable --help option
     *     'add_version_option' => true, // or false to disable --version option
     *     'force_posix'        => false // or true to force posix compliance
     * ));
     * </code>
     *
     * @param array $params An optional array of parameters
     *
     * @return void
     */
    public function __construct(array $params = array())
    {
        if (isset($params['name'])) {
            $this->name = $params['name'];
        } else if (isset($argv) && count($argv) > 0) {
            $this->name = $argv[0];
        } else if (isset($_SERVER['argv']) && count($_SERVER['argv']) > 0) {
            $this->name = $_SERVER['argv'][0];
        } else if (isset($_SERVER['SCRIPT_NAME'])) {
            $this->name = basename($_SERVER['SCRIPT_NAME']);
        }
        if (isset($params['description'])) {
            $this->description = $params['description'];
        }
        if (isset($params['version'])) {
            $this->version = $params['version'];
        }
        if (isset($params['add_version_option'])) {
            $this->add_version_option = $params['add_version_option'];
        }
        if (isset($params['add_help_option'])) {
            $this->add_help_option = $params['add_help_option'];
        }
        if (isset($params['subcommand_required'])) {
            $this->subcommand_required = $params['subcommand_required'];
        }
        if (isset($params['force_posix'])) {
            $this->force_posix = $params['force_posix'];
        } else if (getenv('POSIXLY_CORRECT')) {
            $this->force_posix = true;
        }
        if (isset($params['messages']) && is_array($params['messages'])) {
            $this->messages = $params['messages'];
        }
        // set default instances
        $this->renderer         = new CommandLine\Renderer_Default($this);
        $this->outputter        = new CommandLine\Outputter_Default();
        $this->message_provider = new CommandLine\MessageProvider_Default();
    }

    // }}}
    // accept() {{{

    /**
     * Method to allow PEAR2\Console\CommandLine to accept either:
     *  + a custom renderer,
     *  + a custom outputter,
     *  + or a custom message provider
     *
     * @param mixed $instance The custom instance
     *
     * @return void
     * @throws PEAR2\Console\CommandLine\Exception if wrong argument passed
     */
    public function accept($instance)
    {
        if ($instance instanceof CommandLine\Renderer) {
            if (property_exists($instance, 'parser') && !$instance->parser) {
                $instance->parser = $this;
            }
            $this->renderer = $instance;
        } else if ($instance instanceof CommandLine\Outputter) {
            $this->outputter = $instance;
        } else if ($instance instanceof CommandLine\MessageProvider) {
            $this->message_provider = $instance;
        } else {
            throw CommandLine\Exception::factory(
                'INVALID_CUSTOM_INSTANCE',
                array(),
                $this,
                $this->messages
            );
        }
    }

    // }}}
    // fromXmlFile() {{{

    /**
     * Returns a command line parser instance built from an xml file.
     *
     * Example:
     * <code>
     * $parser = PEAR2\Console\CommandLine::fromXmlFile('path/to/file.xml');
     * $result = $parser->parse();
     * </code>
     *
     * @param string $file Path to the xml file
     *
     * @return PEAR2\Console\CommandLine The parser instance
     */
    public static function fromXmlFile($file)
    {
        return CommandLine\XmlParser::parse($file);
    }

    // }}}
    // fromXmlString() {{{

    /**
     * Returns a command line parser instance built from an xml string.
     *
     * Example:
     * <code>
     * $xmldata = '<?xml version="1.0" encoding="utf-8" standalone="yes"?>
     * <command>
     *   <description>Compress files</description>
     *   <option name="quiet">
     *     <short_name>-q</short_name>
     *     <long_name>--quiet</long_name>
     *     <description>be quiet when run</description>
     *     <action>StoreTrue/action>
     *   </option>
     *   <argument name="files">
     *     <description>a list of files</description>
     *     <multiple>true</multiple>
     *   </argument>
     * </command>';
     * $parser = PEAR2\Console\CommandLine::fromXmlString($xmldata);
     * $result = $parser->parse();
     * </code>
     *
     * @param string $string The xml data
     *
     * @return PEAR2\Console\CommandLine The parser instance
     */
    public static function fromXmlString($string)
    {
        return CommandLine\XmlParser::parseString($string);
    }

    // }}}
    // addArgument() {{{

    /**
     * Adds an argument to the command line parser and returns it.
     *
     * Adds an argument with the name $name and set its attributes with the
     * array $params, then return the PEAR2\Console\CommandLine\Argument instance
     * created.
     * The method accepts another form: you can directly pass a
     * PEAR2\Console\CommandLine\Argument object as the sole argument, this allows
     * you to contruct the argument separately, in order to reuse it in
     * different command line parsers or commands for example.
     *
     * Example:
     * <code>
     * $parser = new PEAR2\Console\CommandLine();
     * // add an array argument
     * $parser->addArgument('input_files', array('multiple'=>true));
     * // add a simple argument
     * $parser->addArgument('output_file');
     * $result = $parser->parse();
     * print_r($result->args['input_files']);
     * print_r($result->args['output_file']);
     * // will print:
     * // array('file1', 'file2')
     * // 'file3'
     * // if the command line was:
     * // myscript.php file1 file2 file3
     * </code>
     *
     * In a terminal, the help will be displayed like this:
     * <code>
     * $ myscript.php install -h
     * Usage: myscript.php <input_files...> <output_file>
     * </code>
     *
     * @param mixed $name   A string containing the argument name or an
     *                      instance of PEAR2\Console\CommandLine\Argument
     * @param array $params An array containing the argument attributes
     *
     * @return PEAR2\Console\CommandLine\Argument the added argument
     * @see PEAR2\Console\CommandLine\Argument
     */
    public function addArgument($name, $params = array())
    {
        if ($name instanceof CommandLine\Argument) {
            $argument = $name;
        } else {
            $argument = new CommandLine\Argument($name, $params);
        }
        $argument->validate();
        $this->args[$argument->name] = $argument;
        return $argument;
    }

    // }}}
    // addCommand() {{{

    /**
     * Adds a sub-command to the command line parser.
     *
     * Adds a command with the given $name to the parser and returns the
     * PEAR2\Console\CommandLine\Command instance, you can then populate the command
     * with options, configure it, etc... like you would do for the main parser
     * because the class PEAR2\Console\CommandLine\Command inherits from
     * PEAR2\Console\CommandLine.
     *
     * An example:
     * <code>
     * $parser = new PEAR2\Console\CommandLine();
     * $install_cmd = $parser->addCommand('install');
     * $install_cmd->addOption(
     *     'verbose',
     *     array(
     *         'short_name'  => '-v',
     *         'long_name'   => '--verbose',
     *         'description' => 'be noisy when installing stuff',
     *         'action'      => 'StoreTrue'
     *      )
     * );
     * $parser->parse();
     * </code>
     * Then in a terminal:
     * <code>
     * $ myscript.php install -h
     * Usage: myscript.php install [options]
     *
     * Options:
     *   -h, --help     display this help message and exit
     *   -v, --verbose  be noisy when installing stuff
     *
     * $ myscript.php install --verbose
     * Installing whatever...
     * $
     * </code>
     *
     * @param mixed $name   A string containing the command name or an
     *                      instance of PEAR2\Console\CommandLine\Command
     * @param array $params An array containing the command attributes
     *
     * @return PEAR2\Console\CommandLine\Command The added subcommand
     * @see    PEAR2\Console\CommandLine\Command
     */
    public function addCommand($name, $params = array())
    {
        if ($name instanceof CommandLine\Command) {
            $command = $name;
        } else {
            $params['name'] = $name;
            $command        = new CommandLine\Command($params);
            // some properties must cascade to the child command if not
            // passed explicitely. This is done only in this case, because if
            // we have a Command object we have no way to determine if theses
            // properties have already been set
            $cascade = array(
                'add_help_option',
                'add_version_option',
                'outputter',
                'message_provider',
                'force_posix',
                'force_options_defaults'
            );
            foreach ($cascade as $property) {
                if (!isset($params[$property])) {
                    $command->$property = $this->$property;
                }
            }
            if (!isset($params['renderer'])) {
                $renderer          = clone $this->renderer;
                $renderer->parser  = $command;
                $command->renderer = $renderer;
            }
        }
        $command->parent = $this;
        $this->commands[$command->name] = $command;
        return $command;
    }

    // }}}
    // addOption() {{{

    /**
     * Adds an option to the command line parser and returns it.
     *
     * Adds an option with the name $name and set its attributes with the
     * array $params, then return the PEAR2\Console\CommandLine\Option instance
     * created.
     * The method accepts another form: you can directly pass a
     * PEAR2\Console\CommandLine\Option object as the sole argument, this allows
     * you to contruct the option separately, in order to reuse it in different
     * command line parsers or commands for example.
     *
     * Example:
     * <code>
     * $parser = new PEAR2\Console\CommandLine();
     * $parser->addOption('path', array(
     *     'short_name'  => '-p',  // a short name
     *     'long_name'   => '--path', // a long name
     *     'description' => 'path to the dir', // a description msg
     *     'action'      => 'StoreString',
     *     'default'     => '/tmp' // a default value
     * ));
     * $parser->parse();
     * </code>
     *
     * In a terminal, the help will be displayed like this:
     * <code>
     * $ myscript.php --help
     * Usage: myscript.php [options]
     *
     * Options:
     *   -h, --help  display this help message and exit
     *   -p, --path  path to the dir
     *
     * </code>
     *
     * Various methods to specify an option, these 3 commands are equivalent:
     * <code>
     * $ myscript.php --path=some/path
     * $ myscript.php -p some/path
     * $ myscript.php -psome/path
     * </code>
     *
     * @param mixed $name   A string containing the option name or an
     *                      instance of PEAR2\Console\CommandLine\Option
     * @param array $params An array containing the option attributes
     *
     * @return PEAR2\Console\CommandLine\Option The added option
     * @see    PEAR2\Console\CommandLine\Option
     */
    public function addOption($name, $params = array())
    {
        if ($name instanceof CommandLine\Option) {
            $opt = $name;
        } else {
            $opt = new CommandLine\Option($name, $params);
        }
        $opt->validate();
        if ($this->force_options_defaults) {
            $opt->setDefaults();
        }
        $this->options[$opt->name] = $opt;
        if (!empty($opt->choices) && $opt->add_list_option) {
            $this->addOption(
                'list_' . $opt->name,
                array(
                    'long_name'     => '--list-' . $opt->name,
                    'description'   => $this->message_provider->get(
                        'LIST_OPTION_MESSAGE',
                        array('name' => $opt->name)
                    ),
                    'action'        => 'List',
                    'action_params' => array('list' => $opt->choices),
                )
            );
        }
        return $opt;
    }

    // }}}
    // displayError() {{{

    /**
     * Displays an error to the user via stderr and exit with $exitCode if its
     * value is not equals to false.
     *
     * @param string $error    The error message
     * @param int    $exitCode The exit code number (default: 1). If set to
     *                         false, the exit() function will not be called
     *
     * @return void
     */
    public function displayError($error, $exitCode = 1)
    {
        $this->outputter->stderr($this->renderer->error($error));
        if ($exitCode !== false) {
            exit($exitCode);
        }
    }

    // }}}
    // displayUsage() {{{

    /**
     * Displays the usage help message to the user via stdout and exit with
     * $exitCode if its value is not equals to false.
     *
     * @param int $exitCode The exit code number (default: 0). If set to
     *                      false, the exit() function will not be called
     *
     * @return void
     */
    public function displayUsage($exitCode = 0)
    {
        $this->outputter->stdout($this->renderer->usage());
        if ($exitCode !== false) {
            exit($exitCode);
        }
    }

    // }}}
    // displayVersion() {{{

    /**
     * Displays the program version to the user via stdout and exit with
     * $exitCode if its value is not equals to false.
     *
     * @param int $exitCode The exit code number (default: 0). If set to
     *                      false, the exit() function will not be called
     *
     * @return void
     */
    public function displayVersion($exitCode = 0)
    {
        $this->outputter->stdout($this->renderer->version());
        if ($exitCode !== false) {
            exit($exitCode);
        }
    }

    // }}}
    // findOption() {{{

    /**
     * Finds the option that matches the given short_name (ex: -v), long_name
     * (ex: --verbose) or name (ex: verbose).
     *
     * @param string $str The option identifier
     *
     * @return mixed A PEAR2\Console\CommandLine\Option instance or false
     */
    public function findOption($str)
    {
        $str = trim($str);
        if ($str === '') {
            return false;
        }
        $matches = array();
        foreach ($this->options as $opt) {
            if ($opt->short_name == $str
                || $opt->long_name == $str
                || $opt->name == $str
            ) {
                // exact match
                return $opt;
            }
            if (substr($opt->long_name, 0, strlen($str)) === $str) {
                // abbreviated long option
                $matches[] = $opt;
            }
        }
        if ($count = count($matches)) {
            if ($count > 1) {
                $matches_str = '';
                $padding     = '';
                foreach ($matches as $opt) {
                    $matches_str .= $padding . $opt->long_name;
                    $padding      = ', ';
                }
                throw CommandLine\Exception::factory(
                    'OPTION_AMBIGUOUS',
                    array('name' => $str, 'matches' => $matches_str),
                    $this,
                    $this->messages
                );
            }
            return $matches[0];
        }
        return false;
    }
    // }}}
    // registerAction() {{{

    /**
     * Registers a custom action for the parser, an example:
     *
     * <code>
     *
     * // in this example we create a "range" action:
     * // the user will be able to enter something like:
     * // $ <program> -r 1,5
     * // and in the result we will have:
     * // $result->options['range']: array(1, 5)
     *
     * class ActionRange extends PEAR2\Console\CommandLine\Action
     * {
     *     public function execute($value=false, $params=array())
     *     {
     *         $range = explode(',', str_replace(' ', '', $value));
     *         if (count($range) != 2) {
     *             throw new Exception(sprintf(
     *                 'Option "%s" must be 2 integers separated by a comma',
     *                 $this->option->name
     *             ));
     *         }
     *         $this->setResult($range);
     *     }
     * }
     * // then we can register our action
     * PEAR2\Console\CommandLine::registerAction('Range', 'ActionRange');
     * // and now our action is available !
     * $parser = new PEAR2\Console\CommandLine();
     * $parser->addOption('range', array(
     *     'short_name'  => '-r',
     *     'long_name'   => '--range',
     *     'action'      => 'Range', // note our custom action
     *     'description' => 'A range of two integers separated by a comma'
     * ));
     * // etc...
     *
     * </code>
     *
     * @param string $name  The name of the custom action
     * @param string $class The class name of the custom action
     *
     * @return void
     */
    public static function registerAction($name, $class)
    {
        if (!isset(self::$actions[$name])) {
            if (!class_exists($class)) {
                self::triggerError(
                    'action_class_does_not_exists',
                    E_USER_ERROR,
                    array('{$name}' => $name, '{$class}' => $class)
                );
            }
            self::$actions[$name] = array($class, false);
        }
    }

    // }}}
    // triggerError() {{{

    /**
     * A wrapper for programming errors triggering.
     *
     * @param string $msgId  Identifier of the message
     * @param int    $level  The php error level
     * @param array  $params An array of search=>replaces entries
     *
     * @return void
     * @todo remove Console::triggerError() and use exceptions only
     */
    public static function triggerError($msgId, $level, $params=array())
    {
        if (isset(self::$errors[$msgId])) {
            $msg = str_replace(
                array_keys($params),
                array_values($params),
                self::$errors[$msgId]
            );
            trigger_error($msg, $level);
        } else {
            trigger_error('unknown error', $level);
        }
    }

    // }}}
    // parse() {{{

    /**
     * Parses the command line arguments and returns a
     * PEAR2\Console\CommandLine\Result instance.
     *
     * @param integer $userArgc Number of arguments (optional)
     * @param array   $userArgv Array containing arguments (optional)
     *
     * @return PEAR2\Console\CommandLine\Result The result instance
     * @throws Exception on user errors
     */
    public function parse($userArgc=null, $userArgv=null)
    {
        $this->addBuiltinOptions();
        if ($userArgc !== null && $userArgv !== null) {
            $argc = $userArgc;
            $argv = $userArgv;
        } else {
            list($argc, $argv) = $this->getArgcArgv();
        }
        // build an empty result
        $result = new CommandLine\Result();
        if (!($this instanceof CommandLine\Command)) {
            // remove script name if we're not in a subcommand
            array_shift($argv);
            $argc--;
        }
        // will contain arguments
        $args = array();
        foreach ($this->options as $name=>$option) {
            $result->options[$name] = $option->default;
        }
        // parse command line tokens
        while ($argc--) {
            $token = array_shift($argv);
            try {
                if ($cmd = $this->_getSubCommand($token)) {
                    $result->command_name = $cmd->name;
                    $result->command      = $cmd->parse($argc, $argv);
                    break;
                } else {
                    $this->parseToken($token, $result, $args, $argc);
                }
            } catch (Exception $exc) {
                throw $exc;
            }
        }
        // Parse a null token to allow any undespatched actions to be despatched.
        $this->parseToken(null, $result, $args, 0);
        // Check if an invalid subcommand was specified. If there are
        // subcommands and no arguments, but an argument was provided, it is
        // an invalid subcommand.
        if (   count($this->commands) > 0
            && count($this->args) === 0
            && count($args) > 0
        ) {
            throw CommandLine\Exception::factory(
                'INVALID_SUBCOMMAND',
                array('command' => $args[0]),
                $this,
                $this->messages
            );
        }
        // if subcommand_required is set to true we must check that we have a
        // subcommand.
        if (   count($this->commands)
            && $this->subcommand_required
            && !$result->command_name
        ) {
            throw CommandLine\Exception::factory(
                'SUBCOMMAND_REQUIRED',
                array('commands' => implode(array_keys($this->commands), ', ')),
                $this,
                $this->messages
            );
        }
        // minimum argument number check
        $argnum = 0;
        foreach ($this->args as $name=>$arg) {
            if (!$arg->optional) {
                $argnum++;
            }
        }
        if (count($args) < $argnum) {
            throw CommandLine\Exception::factory(
                'ARGUMENT_REQUIRED',
                array('argnum' => $argnum, 'plural' => $argnum>1 ? 's': ''),
                $this,
                $this->messages
            );
        }
        // handle arguments
        $c = count($this->args);
        foreach ($this->args as $name=>$arg) {
            $c--;
            if ($arg->multiple) {
                $result->args[$name] = $c ? array_splice($args, 0, -$c) : $args;
            } else {
                $result->args[$name] = array_shift($args);
            }
            if (!$result->args[$name] && $arg->optional && $arg->default) {
                $result->args[$name] = $arg->default;
            }
        }
        // dispatch deferred options
        foreach ($this->_dispatchLater as $optArray) {
            $optArray[0]->dispatchAction($optArray[1], $optArray[2], $this);
        }
        return $result;
    }

    // }}}
    // parseToken() {{{

    /**
     * Parses the command line token and modifies *by reference* the $options
     * and $args arrays.
     *
     * @param string $token  The command line token to parse
     * @param object $result The PEAR2\Console\CommandLine\Result instance
     * @param array  &$args  The argv array
     * @param int    $argc   Number of lasting args
     *
     * @return void
     * @access protected
     * @throws Exception on user errors
     */
    protected function parseToken($token, $result, &$args, $argc)
    {
        static $lastopt  = false;
        static $stopflag = false;
        $last  = $argc === 0;
        if (!$stopflag && $lastopt) {
            if (substr($token, 0, 1) == '-') {
                if ($lastopt->argument_optional) {
                    $this->_dispatchAction($lastopt, '', $result);
                    if ($lastopt->action != 'StoreArray') {
                        $lastopt = false;
                    }
                } else if (isset($result->options[$lastopt->name])) {
                    // case of an option that expect a list of args
                    $lastopt = false;
                } else {
                    throw CommandLine\Exception::factory(
                        'OPTION_VALUE_REQUIRED',
                        array('name' => $lastopt->name),
                        $this,
                        $this->messages
                    );
                }
            } else {
                // when a StoreArray option is positioned last, the behavior
                // is to consider that if there's already an element in the
                // array, and the commandline expects one or more args, we
                // leave last tokens to arguments
                if ($lastopt->action == 'StoreArray'
                    && !empty($result->options[$lastopt->name])
                    && count($this->args) > ($argc + count($args))
                ) {
                    if (!is_null($token)) {
                        $args[] = $token;
                    }
                    return;
                }
                if (!is_null($token) || $lastopt->action == 'Password') {
                    $this->_dispatchAction($lastopt, $token, $result);
                }
                if ($lastopt->action != 'StoreArray') {
                    $lastopt = false;
                }
                return;
            }
        }
        if (!$stopflag && substr($token, 0, 2) == '--') {
            // a long option
            $optkv = explode('=', $token, 2);
            if (trim($optkv[0]) == '--') {
                // the special argument "--" forces in all cases the end of
                // option scanning.
                $stopflag = true;
                return;
            }
            $opt = $this->findOption($optkv[0]);
            if (!$opt) {
                throw CommandLine\Exception::factory(
                    'OPTION_UNKNOWN',
                    array('name' => $optkv[0]),
                    $this,
                    $this->messages
                );
            }
            $value = isset($optkv[1]) ? $optkv[1] : false;
            if (!$opt->expectsArgument() && $value !== false) {
                throw CommandLine\Exception::factory(
                    'OPTION_VALUE_UNEXPECTED',
                    array('name' => $opt->name, 'value' => $value),
                    $this,
                    $this->messages
                );
            }
            if ($opt->expectsArgument() && $value === false) {
                // maybe the long option argument is separated by a space, if
                // this is the case it will be the next arg
                if ($last && !$opt->argument_optional) {
                    throw CommandLine\Exception::factory(
                        'OPTION_VALUE_REQUIRED',
                        array('name' => $opt->name),
                        $this,
                        $this->messages
                    );
                }
                // we will have a value next time
                $lastopt = $opt;
                return;
            }
            if ($opt->action == 'StoreArray') {
                $lastopt = $opt;
            }
            $this->_dispatchAction($opt, $value, $result);
        } else if (!$stopflag && substr($token, 0, 1) == '-') {
            // a short option
            $optname = substr($token, 0, 2);
            if ($optname == '-') {
                // special case of "-": try to read stdin
                $args[] = file_get_contents('php://stdin');
                return;
            }
            $opt = $this->findOption($optname);
            if (!$opt) {
                throw CommandLine\Exception::factory(
                    'OPTION_UNKNOWN',
                    array('name' => $optname),
                    $this,
                    $this->messages
                );
            }
            // parse other options or set the value
            // in short: handle -f<value> and -f <value>
            $next = substr($token, 2, 1);
            // check if we must wait for a value
            if ($next === false) {
                if ($opt->expectsArgument()) {
                    if ($last && !$opt->argument_optional) {
                        throw CommandLine\Exception::factory(
                            'OPTION_VALUE_REQUIRED',
                            array('name' => $opt->name),
                            $this,
                            $this->messages
                        );
                    }
                    // we will have a value next time
                    $lastopt = $opt;
                    return;
                }
                $value = false;
            } else {
                if (!$opt->expectsArgument()) {
                    if ($nextopt = $this->findOption('-' . $next)) {
                        $this->_dispatchAction($opt, false, $result);
                        $this->parseToken(
                            '-' . substr($token, 2),
                            $result,
                            $args,
                            $last
                        );
                        return;
                    } else {
                        throw CommandLine\Exception::factory(
                            'OPTION_UNKNOWN',
                            array('name' => $next),
                            $this,
                            $this->messages
                        );
                    }
                }
                if ($opt->action == 'StoreArray') {
                    $lastopt = $opt;
                }
                $value = substr($token, 2);
            }
            $this->_dispatchAction($opt, $value, $result);
        } else {
            // We have an argument.
            // if we are in POSIX compliant mode, we must set the stop flag to
            // true in order to stop option parsing.
            if (!$stopflag && $this->force_posix) {
                $stopflag = true;
            }
            if (!is_null($token)) {
                $args[] = $token;
            }
        }
    }

    // }}}
    // addBuiltinOptions() {{{

    /**
     * Adds the builtin "Help" and "Version" options if needed.
     *
     * @return void
     */
    public function addBuiltinOptions()
    {
        if ($this->add_help_option) {
            $helpOptionParams = array(
                'long_name'   => '--help',
                'description' => 'show this help message and exit',
                'action'      => 'Help'
            );
            if (!($option = $this->findOption('-h')) || $option->action == 'Help') {
                // short name is available, take it
                $helpOptionParams['short_name'] = '-h';
            }
            $this->addOption('help', $helpOptionParams);
        }
        if ($this->add_version_option && !empty($this->version)) {
            $versionOptionParams = array(
                'long_name'   => '--version',
                'description' => 'show the program version and exit',
                'action'      => 'Version'
            );
            if (!$this->findOption('-v')) {
                // short name is available, take it
                $versionOptionParams['short_name'] = '-v';
            }
            $this->addOption('version', $versionOptionParams);
        }
    }

    // }}}
    // getArgcArgv() {{{

    /**
     * Tries to return an array containing argc and argv, or trigger an error
     * if it fails to get them.
     *
     * @return array The argc/argv array
     * @throws PEAR2\Console\CommandLine\Exception
     */
    protected function getArgcArgv()
    {
        if (php_sapi_name() != 'cli') {
            // we have a web request
            $argv = array($this->name);
            if (isset($_REQUEST)) {
                foreach ($_REQUEST as $key => $value) {
                    if (!is_array($value)) {
                        $value = array($value);
                    }
                    $opt = $this->findOption($key);
                    if ($opt instanceof CommandLine\Option) {
                        // match a configured option
                        $argv[] = $opt->short_name ?
                            $opt->short_name : $opt->long_name;
                        foreach ($value as $v) {
                            if ($opt->expectsArgument()) {
                                $argv[] = isset($_REQUEST[$key])
                                    ? urldecode($v)
                                    : $v;
                            } else if ($v == '0' || $v == 'false') {
                                array_pop($argv);
                            }
                        }
                    } else if (isset($this->args[$key])) {
                        // match a configured argument
                        foreach ($value as $v) {
                            $argv[] = isset($_REQUEST[$key]) ? urldecode($v) : $v;
                        }
                    }
                }
            }
            return array(count($argv), $argv);
        }
        if (isset($argc) && isset($argv)) {
            // case of register_argv_argc = 1
            return array($argc, $argv);
        }
        if (isset($_SERVER['argc']) && isset($_SERVER['argv'])) {
            return array($_SERVER['argc'], $_SERVER['argv']);
        }
        return array(0, array());
    }

    // }}}
    // _dispatchAction() {{{

    /**
     * Dispatches the given option or store the option to dispatch it later.
     *
     * @param PEAR2\Console\CommandLine\Option $option The option instance
     * @param string                           $token  Command line token to parse
     * @param PEAR2\Console\CommandLine\Result $result The result instance
     *
     * @return void
     */
    private function _dispatchAction($option, $token, $result)
    {
        if ($option->action == 'Password') {
            $this->_dispatchLater[] = array($option, $token, $result);
        } else {
            $option->dispatchAction($token, $result, $this);
        }
    }
    // }}}
    // _getSubCommand() {{{

    /**
     * Tries to return the subcommand that matches the given token or returns
     * false if no subcommand was found.
     *
     * @param string $token Current command line token
     *
     * @return mixed An instance of PEAR2\Console\CommandLine\Command or false
     */
    private function _getSubCommand($token)
    {
        foreach ($this->commands as $cmd) {
            if ($cmd->name == $token || in_array($token, $cmd->aliases)) {
                return $cmd;
            }
        }
        return false;
    }

    // }}}
}


File: /PEAR2\Net\RouterOS\Client.php
<?php

/**
 * RouterOS API client implementation.
 * 
 * RouterOS is the flag product of the company MikroTik and is a powerful router software. One of its many abilities is to allow control over it via an API. This package provides a client for that API, in turn allowing you to use PHP to control RouterOS hosts.
 * 
 * PHP version 5
 * 
 * @category  Net
 * @package   PEAR2_Net_RouterOS
 * @author    Vasil Rangelov <boen.robot@gmail.com>
 * @copyright 2011 Vasil Rangelov
 * @license   http://www.gnu.org/copyleft/lesser.html LGPL License 2.1
 * @version   1.0.0b5
 * @link      http://pear2.php.net/PEAR2_Net_RouterOS
 */
/**
 * The namespace declaration.
 */
namespace PEAR2\Net\RouterOS;

/**
 * Refers to transmitter direction constants.
 */
use PEAR2\Net\Transmitter\Stream as S;

/**
 * Refers to the cryptography constants.
 */
use PEAR2\Net\Transmitter\NetworkStream as N;

/**
 * Catches arbitrary exceptions at some points.
 */
use Exception as E;

/**
 * A RouterOS client.
 * 
 * Provides functionality for easily communicating with a RouterOS host.
 * 
 * @category Net
 * @package  PEAR2_Net_RouterOS
 * @author   Vasil Rangelov <boen.robot@gmail.com>
 * @license  http://www.gnu.org/copyleft/lesser.html LGPL License 2.1
 * @link     http://pear2.php.net/PEAR2_Net_RouterOS
 */
class Client
{
    /**
     * Used in {@link static::isRequestActive()} to limit search only to
     * requests that have a callback.
     */
    const FILTER_CALLBACK = 1;
    /**
     * Used in {@link static::isRequestActive()} to limit search only to
     * requests that use the buffer.
     */
    const FILTER_BUFFER = 2;
    /**
     * Used in {@link static::isRequestActive()} to indicate no limit in search.
     */
    const FILTER_ALL = 3;

    /**
     * @var Communicator The communicator for this client.
     */
    protected $com;

    /**
     * @var int The number of currently pending requests.
     */
    protected $pendingRequestsCount = 0;

    /**
     * @var array An array of responses that have not yet been extracted or
     *     passed to a callback. Key is the tag of the request, and the value
     *     is an array of associated responses.
     */
    protected $responseBuffer = array();

    /**
     * @var array An array of callbacks to be executed as responses come.
     *     Key is the tag of the request, and the value is the callback for it.
     */
    protected $callbacks = array();
    
    /**
     * @var Registry A registry for the operations. Particularly helpful at
     *     persistent connections.
     */
    protected $registry = null;

    /**
     * @var bool Whether to stream future responses.
     */
    private $_streamingResponses = false;

    /**
     * Creates a new instance of a RouterOS API client.
     * 
     * Creates a new instance of a RouterOS API client with the specified
     * settings.
     * 
     * @param string   $host     Hostname (IP or domain) of the RouterOS server.
     * @param string   $username The RouterOS username.
     * @param string   $password The RouterOS password.
     * @param int|null $port     The port on which the RouterOS server provides
     *     the API service. You can also specify NULL, in which case the port
     *     will automatically be chosen between 8728 and 8729, depending on the
     *     value of $crypto.
     * @param bool     $persist  Whether or not the connection should be a
     *     persistent one.
     * @param float    $timeout  The timeout for the connection.
     * @param string   $crypto   The encryption for this connection. Must be one
     *     of the PEAR2\Net\Transmitter\NetworkStream::CRYPTO_* constants. Off
     *     by default. RouterOS currently supports only TLS, but the setting is
     *     provided in this fashion for forward compatibility's sake. And for
     *     the sake of simplicity, if you specify an encryption, don't specify a
     *     context and your default context uses the value "DEFAULT" for
     *     ciphers, "ADH" will be automatically added to the list of ciphers.
     * @param resource $context  A context for the socket.
     * 
     * @see sendSync()
     * @see sendAsync()
     */
    public function __construct(
        $host,
        $username,
        $password = '',
        $port = 8728,
        $persist = false,
        $timeout = null,
        $crypto = N::CRYPTO_OFF,
        $context = null
    ) {
        $this->com = new Communicator(
            $host,
            $port,
            $persist,
            $timeout,
            $username . '/' . $password,
            $crypto,
            $context
        );
        $timeout = null == $timeout
            ? ini_get('default_socket_timeout')
            : (int) $timeout;
        //Login the user if necessary
        if ((!$persist
            || !($old = $this->com->getTransmitter()->lock(S::DIRECTION_ALL)))
            && $this->com->getTransmitter()->isFresh()
        ) {
            if (!static::login($this->com, $username, $password, $timeout)) {
                $this->com->close();
                throw new DataFlowException(
                    'Invalid username or password supplied.',
                    DataFlowException::CODE_INVALID_CREDENTIALS
                );
            }
        }
        
        if (isset($old)) {
            $this->com->getTransmitter()->lock($old, true);
        }
        
        if ($persist) {
            $this->registry = new Registry("{$host}:{$port}/{$username}");
        }
    }
    
    /**
     * A shorthand gateway.
     * 
     * This is a magic PHP method that allows you to call the object as a
     * function. Depending on the argument given, one of the other functions in
     * the class is invoked and its returned value is returned by this function.
     * 
     * @param mixed $arg Value can be either a {@link Request} to send, which
     *     would be sent asynchoniously if it has a tag, and synchroniously if
     *     not, a number to loop with or NULL to complete all pending requests.
     *     Any other value is converted to string and treated as the tag of a
     *     request to complete.
     * 
     * @return mixed Whatever the long form function would have returned.
     */
    public function __invoke($arg = null)
    {
        if (is_int($arg) || is_double($arg)) {
            return $this->loop($arg);
        } elseif ($arg instanceof Request) {
            return '' == $arg->getTag() ? $this->sendSync($arg)
                : $this->sendAsync($arg);
        } elseif (null === $arg) {
            return $this->completeRequest();
        }
        return $this->completeRequest((string) $arg);
    }

    /**
     * Login to a RouterOS connection.
     * 
     * @param Communicator $com      The communicator to attempt to login to.
     * @param string       $username The RouterOS username.
     * @param string       $password The RouterOS password.
     * @param int|null     $timeout  The time to wait for each response. NULL
     *     waits indefinetly.
     * 
     * @return bool TRUE on success, FALSE on failure.
     */
    public static function login(
        Communicator $com,
        $username,
        $password = '',
        $timeout = null
    ) {
        if (null !== ($remoteCharset = $com->getCharset($com::CHARSET_REMOTE))
            && null !== ($localCharset = $com->getCharset($com::CHARSET_LOCAL))
        ) {
            $password = iconv(
                $localCharset,
                $remoteCharset . '//IGNORE//TRANSLIT',
                $password
            );
        }
        $old = null;
        try {
            if ($com->getTransmitter()->isPersistent()) {
                $old = $com->getTransmitter()->lock(S::DIRECTION_ALL);
                $result = self::_login($com, $username, $password, $timeout);
                $com->getTransmitter()->lock($old, true);
                return $result;
            }
            return self::_login($com, $username, $password, $timeout);
        } catch (E $e) {
            if ($com->getTransmitter()->isPersistent() && null !== $old) {
                $com->getTransmitter()->lock($old, true);
            }
            throw ($e instanceof NotSupportedException
            || $e instanceof UnexpectedValueException
            || !$com->getTransmitter()->isDataAwaiting()) ? new SocketException(
                'This is not a compatible RouterOS service',
                SocketException::CODE_SERVICE_INCOMPATIBLE,
                $e
            ) : $e;
        }
    }

    /**
     * Login to a RouterOS connection.
     * 
     * This is the actual login procedure, applied regardless of persistence and
     * charset settings.
     * 
     * @param Communicator $com      The communicator to attempt to login to.
     * @param string       $username The RouterOS username.
     * @param string       $password The RouterOS password. Potentially parsed
     *     already by iconv.
     * @param int|null     $timeout  The time to wait for each response. NULL
     *     waits indefinetly.
     * 
     * @return bool TRUE on success, FALSE on failure.
     */
    private static function _login(
        Communicator $com,
        $username,
        $password = '',
        $timeout = null
    ) {
        $request = new Request('/login');
        $request->send($com);
        $response = new Response($com, false, $timeout);
        $request->setArgument('name', $username);
        $request->setArgument(
            'response',
            '00' . md5(
                chr(0) . $password
                . pack('H*', $response->getProperty('ret'))
            )
        );
        $request->send($com);
        $response = new Response($com, false, $timeout);
        return $response->getType() === Response::TYPE_FINAL
            && null === $response->getProperty('ret');
    }
    
    /**
     * Sets the charset(s) for this connection.
     * 
     * Sets the charset(s) for this connection. The specified charset(s) will be
     * used for all future requests and responses. When sending,
     * {@link Communicator::CHARSET_LOCAL} is converted to
     * {@link Communicator::CHARSET_REMOTE}, and when receiving,
     * {@link Communicator::CHARSET_REMOTE} is converted to
     * {@link Communicator::CHARSET_LOCAL}. Setting NULL to either charset will
     * disable charset convertion, and data will be both sent and received "as
     * is".
     * 
     * @param mixed $charset     The charset to set. If $charsetType is
     *     {@link Communicator::CHARSET_ALL}, you can supply either a string to
     *     use for all charsets, or an array with the charset types as keys, and
     *     the charsets as values.
     * @param int   $charsetType Which charset to set. Valid values are the
     *     Communicator::CHARSET_* constants. Any other value is treated as
     *     {@link Communicator::CHARSET_ALL}.
     * 
     * @return string|array The old charset. If $charsetType is
     *     {@link Communicator::CHARSET_ALL}, the old values will be returned as
     *     an array with the types as keys, and charsets as values.
     * @see Communicator::setDefaultCharset()
     */
    public function setCharset(
        $charset,
        $charsetType = Communicator::CHARSET_ALL
    ) {
        return $this->com->setCharset($charset, $charsetType);
    }
    
    /**
     * Gets the charset(s) for this connection.
     * 
     * @param int $charsetType Which charset to get. Valid values are the
     *     Communicator::CHARSET_* constants. Any other value is treated as
     *     {@link Communicator::CHARSET_ALL}.
     * 
     * @return string|array The current charset. If $charsetType is
     *     {@link Communicator::CHARSET_ALL}, the current values will be
     *     returned as an array with the types as keys, and charsets as values.
     * @see setCharset()
     */
    public function getCharset($charsetType)
    {
        return $this->com->getCharset($charsetType);
    }

    /**
     * Sends a request and waits for responses.
     * 
     * @param Request  $request  The request to send.
     * @param callback $callback Optional. A function that is to be executed
     *     when new responses for this request are available. The callback takes
     *     two parameters. The {@link Response} object as the first, and the
     *     {@link Client} object as the second one. If the function returns
     *     TRUE, the request is canceled. Note that the callback may be executed
     *     one last time after that with a response that notifies about the
     *     canceling.
     * 
     * @return $this The client object.
     * @see completeRequest()
     * @see loop()
     * @see cancelRequest()
     */
    public function sendAsync(Request $request, $callback = null)
    {
        //Error checking
        $tag = $request->getTag();
        if ('' == $tag) {
            throw new DataFlowException(
                'Asynchonous commands must have a tag.',
                DataFlowException::CODE_TAG_REQUIRED
            );
        }
        if ($this->isRequestActive($tag)) {
            throw new DataFlowException(
                'There must not be multiple active requests sharing a tag.',
                DataFlowException::CODE_TAG_UNIQUE
            );
        }
        if (null !== $callback && !is_callable($callback, true)) {
            throw new UnexpectedValueException(
                'Invalid callback provided.',
                UnexpectedValueException::CODE_CALLBACK_INVALID
            );
        }
        
        $this->send($request);

        if (null === $callback) {
            //Register the request at the buffer
            $this->responseBuffer[$tag] = array();
        } else {
            //Prepare the callback
            $this->callbacks[$tag] = $callback;
        }
        return $this;
    }

    /**
     * Checks if a request is active.
     * 
     * Checks if a request is active. A request is considered active if it's a
     * pending request and/or has responses that are not yet extracted.
     * 
     * @param string $tag    The tag of the request to look for.
     * @param int    $filter One of the FILTER_* consntants. Limits the search
     *     to the specified places.
     * 
     * @return bool TRUE if the request is active, FALSE otherwise.
     * @see getPendingRequestsCount()
     * @see completeRequest()
     */
    public function isRequestActive($tag, $filter = self::FILTER_ALL)
    {
        $result = 0;
        if ($filter & self::FILTER_CALLBACK) {
            $result |= (int) array_key_exists($tag, $this->callbacks);
        }
        if ($filter & self::FILTER_BUFFER) {
            $result |= (int) array_key_exists($tag, $this->responseBuffer);
        }
        return 0 !== $result;
    }

    /**
     * Sends a request and gets the full response.
     * 
     * @param Request $request The request to send.
     * 
     * @return ResponseCollection The received responses as a collection.
     * @see sendAsync()
     * @see close()
     */
    public function sendSync(Request $request)
    {
        $tag = $request->getTag();
        if ('' == $tag) {
            $this->send($request);
        } else {
            $this->sendAsync($request);
        }
        return $this->completeRequest($tag);
    }

    /**
     * Completes a specified request.
     * 
     * Starts an event loop for the RouterOS callbacks and finishes when a
     * specified request is completed.
     * 
     * @param string $tag The tag of the request to complete. Setting NULL
     *     completes all requests.
     * 
     * @return ResponseCollection A collection of {@link Response} objects that
     *     haven't been passed to a callback function or previously extracted
     *     with {@link static::extractNewResponses()}. Returns an empty
     *     collection when $tag is set to NULL (responses can still be
     *     extracted).
     */
    public function completeRequest($tag = null)
    {
        $hasNoTag = '' == $tag;
        $result = $hasNoTag ? array()
            : $this->extractNewResponses($tag)->toArray();
        while ((!$hasNoTag && $this->isRequestActive($tag))
        || ($hasNoTag && 0 !== $this->getPendingRequestsCount())
        ) {
            $newReply = $this->dispatchNextResponse(null);
            if ($newReply->getTag() === $tag) {
                if ($hasNoTag) {
                    $result[] = $newReply;
                }
                if ($newReply->getType() === Response::TYPE_FINAL) {
                    if (!$hasNoTag) {
                        $result = array_merge(
                            $result,
                            $this->isRequestActive($tag)
                            ? $this->extractNewResponses($tag)->toArray()
                            : array()
                        );
                    }
                    break;
                }
            }
        }
        return new ResponseCollection($result);
    }

    /**
     * Extracts responses for a request.
     * 
     * Gets all new responses for a request that haven't been passed to a
     * callback and clears the buffer from them.
     * 
     * @param string $tag The tag of the request to extract new responses for.
     *     Specifying NULL with extract new responses for all requests.
     * 
     * @return ResponseCollection A collection of {@link Response} objects for
     *     the specified request.
     * @see loop()
     */
    public function extractNewResponses($tag = null)
    {
        if (null === $tag) {
            $result = array();
            foreach (array_keys($this->responseBuffer) as $tag) {
                $result = array_merge(
                    $result,
                    $this->extractNewResponses($tag)->toArray()
                );
            }
            return new ResponseCollection($result);
        } elseif ($this->isRequestActive($tag, self::FILTER_CALLBACK)) {
            return new ResponseCollection(array());
        } elseif ($this->isRequestActive($tag, self::FILTER_BUFFER)) {
            $result = $this->responseBuffer[$tag];
            if (!empty($result)) {
                if (end($result)->getType() === Response::TYPE_FINAL) {
                    unset($this->responseBuffer[$tag]);
                } else {
                    $this->responseBuffer[$tag] = array();
                }
            }
            return new ResponseCollection($result);
        } else {
            throw new DataFlowException(
                'No such request, or the request has already finished.',
                DataFlowException::CODE_UNKNOWN_REQUEST
            );
        }
    }

    /**
     * Starts an event loop for the RouterOS callbacks.
     * 
     * Starts an event loop for the RouterOS callbacks and finishes when there
     * are no more pending requests or when a specified timeout has passed
     * (whichever comes first).
     * 
     * @param int $sTimeout  Timeout for the loop. If NULL, there is no time
     *     limit.
     * @param int $usTimeout Microseconds to add to the time limit.
     * 
     * @return bool TRUE when there are any more pending requests, FALSE
     *     otherwise.
     * @see extractNewResponses()
     * @see getPendingRequestsCount()
     */
    public function loop($sTimeout = null, $usTimeout = 0)
    {
        try {
            if (null === $sTimeout) {
                while ($this->getPendingRequestsCount() !== 0) {
                    $this->dispatchNextResponse(null);
                }
            } else {
                list($usStart, $sStart) = explode(' ', microtime());
                while ($this->getPendingRequestsCount() !== 0
                    && ($sTimeout >= 0 || $usTimeout >= 0)
                ) {
                    $this->dispatchNextResponse($sTimeout, $usTimeout);
                    list($usEnd, $sEnd) = explode(' ', microtime());

                    $sTimeout -= $sEnd - $sStart;
                    $usTimeout -= $usEnd - $usStart;
                    if ($usTimeout <= 0) {
                        if ($sTimeout > 0) {
                            $usTimeout = 1000000 + $usTimeout;
                            $sTimeout--;
                        }
                    }

                    $sStart = $sEnd;
                    $usStart = $usEnd;
                }
            }
        } catch (SocketException $e) {
            if ($e->getCode() !== SocketException::CODE_NO_DATA) {
                // @codeCoverageIgnoreStart
                // It's impossible to reliably cause any other SocketException.
                // This line is only here in case the unthinkable happens:
                // The connection terminates just after it was supposedly
                // about to send back some data.
                throw $e;
                // @codeCoverageIgnoreEnd
            }
        }
        return $this->getPendingRequestsCount() !== 0;
    }

    /**
     * Gets the number of pending requests.
     * 
     * @return int The number of pending requests.
     * @see isRequestActive()
     */
    public function getPendingRequestsCount()
    {
        return $this->pendingRequestsCount;
    }

    /**
     * Cancels a request.
     * 
     * Cancels an active request. Using this function in favor of a plain call
     * to the "/cancel" command is highly reccomended, as it also updates the
     * counter of pending requests properly. Note that canceling a request also
     * removes any responses for it that were not previously extracted with
     * {@link static::extractNewResponses()}.
     * 
     * @param string $tag Tag of the request to cancel. Setting NULL will cancel
     *     all requests.
     * 
     * @return $this The client object.
     * @see sendAsync()
     * @see close()
     */
    public function cancelRequest($tag = null)
    {
        $cancelRequest = new Request('/cancel');
        $hasTag = !('' == $tag);
        $hasReg = null !== $this->registry;
        if ($hasReg && !$hasTag) {
            $tags = array_merge(
                array_keys($this->responseBuffer),
                array_keys($this->callbacks)
            );
            $this->registry->setTaglessMode(true);
            foreach ($tags as $t) {
                $cancelRequest->setArgument(
                    'tag',
                    $this->registry->getOwnershipTag() . $t
                );
                $this->sendSync($cancelRequest);
            }
            $this->registry->setTaglessMode(false);
        } else {
            if ($hasTag) {
                if ($this->isRequestActive($tag)) {
                    if ($hasReg) {
                        $this->registry->setTaglessMode(true);
                        $cancelRequest->setArgument(
                            'tag',
                            $this->registry->getOwnershipTag() . $tag
                        );
                    } else {
                        $cancelRequest->setArgument('tag', $tag);
                    }
                } else {
                    throw new DataFlowException(
                        'No such request. Canceling aborted.',
                        DataFlowException::CODE_CANCEL_FAIL
                    );
                }
            }
            $this->sendSync($cancelRequest);
            if ($hasReg) {
                $this->registry->setTaglessMode(false);
            }
        }

        if ($hasTag) {
            if ($this->isRequestActive($tag, self::FILTER_BUFFER)) {
                $this->responseBuffer[$tag] = $this->completeRequest($tag);
            } else {
                $this->completeRequest($tag);
            }
        } else {
            $this->loop();
        }
        return $this;
    }

    /**
     * Sets response streaming setting.
     * 
     * Sets whether future responses are streamed. If responses are streamed,
     * the argument values are returned as streams instead of strings. This is
     * particularly useful if you expect a response that may contain one or more
     * very large words.
     * 
     * @param bool $streamingResponses Whether to stream future responses.
     * 
     * @return bool The previous value of the setting.
     * @see isStreamingResponses()
     */
    public function setStreamingResponses($streamingResponses)
    {
        $oldValue = $this->_streamingResponses;
        $this->_streamingResponses = (bool) $streamingResponses;
        return $oldValue;
    }

    /**
     * Gets response streaming setting.
     * 
     * Gets whether future responses are streamed.
     * 
     * @return bool The value of the setting.
     * @see setStreamingResponses()
     */
    public function isStreamingResponses()
    {
        return $this->_streamingResponses;
    }

    /**
     * Closes the opened connection, even if it is a persistent one.
     * 
     * Closes the opened connection, even if it is a persistent one. Note that
     * {@link static::extractNewResponses()} can still be used to extract
     * responses collected prior to the closing.
     * 
     * @return bool TRUE on success, FALSE on failure.
     */
    public function close()
    {
        $result = true;
        /*
         * The check below is done because for some unknown reason
         * (either a PHP or a RouterOS bug) calling "/quit" on an encrypted
         * connection makes one end hang.
         * 
         * Since encrypted connections only appeared in RouterOS 6.1, and
         * the "/quit" call is needed for all <6.0 versions, problems due
         * to its absence should be limited to some earlier 6.* versions
         * on some RouterBOARD devices.
         */
        if ($this->com->getTransmitter()->getCrypto() === N::CRYPTO_OFF) {
            if (null !== $this->registry) {
                $this->registry->setTaglessMode(true);
            }
            try {
                $response = $this->sendSync(new Request('/quit'));
                $result = $response[0]->getType() === Response::TYPE_FATAL;
            } catch (SocketException $e) {
                $result
                    = $e->getCode() === SocketException::CODE_REQUEST_SEND_FAIL;
            } catch (E $e) {
                //Ignore unknown errors.
            }
            if (null !== $this->registry) {
                $this->registry->setTaglessMode(false);
            }
        }
        $result = $result && $this->com->close();
        $this->callbacks = array();
        $this->pendingRequestsCount = 0;
        return $result;
    }
    
    /**
     * Closes the connection, unless it's a persistent one.
     */
    public function __destruct()
    {
        if ($this->com->getTransmitter()->isPersistent()) {
            if (0 !== $this->pendingRequestsCount) {
                $this->cancelRequest();
            }
        } else {
            $this->close();
        }
    }

    /**
     * Sends a request to RouterOS.
     * 
     * @param Request $request The request to send.
     * 
     * @return $this The client object.
     * @see sendSync()
     * @see sendAsync()
     */
    protected function send(Request $request)
    {
        $request->send($this->com, $this->registry);
        $this->pendingRequestsCount++;
        return $this;
    }

    /**
     * Dispatches the next response in queue.
     * 
     * Dispatches the next response in queue, i.e. it executes the associated
     * callback if there is one, or places the response in the response buffer.
     * 
     * @param int $sTimeout  If a response is not immediatly available, wait
     *     this many seconds. If NULL, wait indefinetly.
     * @param int $usTimeout Microseconds to add to the waiting time.
     * 
     * @throws SocketException When there's no response within the time limit.
     * @return Response The dispatched response.
     */
    protected function dispatchNextResponse($sTimeout = 0, $usTimeout = 0)
    {
        $response = new Response(
            $this->com,
            $this->_streamingResponses,
            $sTimeout,
            $usTimeout,
            $this->registry
        );
        if ($response->getType() === Response::TYPE_FATAL) {
            $this->pendingRequestsCount = 0;
            $this->com->close();
            return $response;
        }

        $tag = $response->getTag();
        $isLastForRequest = $response->getType() === Response::TYPE_FINAL;
        if ($isLastForRequest) {
            $this->pendingRequestsCount--;
        }

        if ('' != $tag) {
            if ($this->isRequestActive($tag, self::FILTER_CALLBACK)) {
                if ($this->callbacks[$tag]($response, $this)) {
                    $this->cancelRequest($tag);
                } elseif ($isLastForRequest) {
                    unset($this->callbacks[$tag]);
                }
            } else {
                $this->responseBuffer[$tag][] = $response;
            }
        }
        return $response;
    }
}


File: /PEAR2\Net\RouterOS\Communicator.php
<?php

/**
 * RouterOS API client implementation.
 * 
 * RouterOS is the flag product of the company MikroTik and is a powerful router software. One of its many abilities is to allow control over it via an API. This package provides a client for that API, in turn allowing you to use PHP to control RouterOS hosts.
 * 
 * PHP version 5
 * 
 * @category  Net
 * @package   PEAR2_Net_RouterOS
 * @author    Vasil Rangelov <boen.robot@gmail.com>
 * @copyright 2011 Vasil Rangelov
 * @license   http://www.gnu.org/copyleft/lesser.html LGPL License 2.1
 * @version   1.0.0b5
 * @link      http://pear2.php.net/PEAR2_Net_RouterOS
 */
/**
 * The namespace declaration.
 */
namespace PEAR2\Net\RouterOS;

/**
 * Using transmitters.
 */
use PEAR2\Net\Transmitter as T;

/**
 * A RouterOS communicator.
 * 
 * Implementation of the RouterOS API protocol. Unlike the other classes in this
 * package, this class doesn't provide any conviniences beyond the low level
 * implementation details (automatic word length encoding/decoding, charset
 * translation and data integrity), and because of that, its direct usage is
 * strongly discouraged.
 * 
 * @category Net
 * @package  PEAR2_Net_RouterOS
 * @author   Vasil Rangelov <boen.robot@gmail.com>
 * @license  http://www.gnu.org/copyleft/lesser.html LGPL License 2.1
 * @link     http://pear2.php.net/PEAR2_Net_RouterOS
 * @see      Client
 */
class Communicator
{
    /**
     * Used when getting/setting all (default) charsets.
     */
    const CHARSET_ALL = -1;
    
    /**
     * Used when getting/setting the (default) remote charset.
     * 
     * The remote charset is the charset in which RouterOS stores its data.
     * If you want to keep compatibility with your Winbox, this charset should
     * match the default charset from your Windows' regional settings.
     */
    const CHARSET_REMOTE = 0;
    
    /**
     * Used when getting/setting the (default) local charset.
     * 
     * The local charset is the charset in which the data from RouterOS will be
     * returned as. This charset should match the charset of the place the data
     * will eventually be written to.
     */
    const CHARSET_LOCAL = 1;
    
    /**
     * @var array An array with the default charset types as keys, and the
     *     default charsets as values.
     */
    protected static $defaultCharsets = array(
        self::CHARSET_REMOTE => null,
        self::CHARSET_LOCAL  => null
    );
    
    /**
     * @var array An array with the current charset types as keys, and the
     * current charsets as values.
     */
    protected $charsets = array();

    /**
     * @var T\TcpClient The transmitter for the connection.
     */
    protected $trans;

    /**
     * Creates a new connection with the specified options.
     * 
     * @param string   $host    Hostname (IP or domain) of the RouterOS server.
     * @param int|null $port    The port on which the RouterOS server provides
     *     the API service. You can also specify NULL, in which case the port
     *     will automatically be chosen between 8728 and 8729, depending on the
     *     value of $crypto.
     * @param bool     $persist Whether or not the connection should be a
     *     persistent one.
     * @param float    $timeout The timeout for the connection.
     * @param string   $key     A string that uniquely identifies the
     *     connection.
     * @param string   $crypto  The encryption for this connection. Must be one
     *     of the PEAR2\Net\Transmitter\NetworkStream::CRYPTO_* constants. Off
     *     by default. RouterOS currently supports only TLS, but the setting is
     *     provided in this fashion for forward compatibility's sake. And for
     *     the sake of simplicity, if you specify an encryption, don't specify a
     *     context and your default context uses the value "DEFAULT" for
     *     ciphers, "ADH" will be automatically added to the list of ciphers.
     * @param resource $context A context for the socket.
     * 
     * @see sendWord()
     */
    public function __construct(
        $host,
        $port = 8728,
        $persist = false,
        $timeout = null,
        $key = '',
        $crypto = T\NetworkStream::CRYPTO_OFF,
        $context = null
    ) {
        $isUnencrypted = T\NetworkStream::CRYPTO_OFF === $crypto;
        if (($context === null) && !$isUnencrypted) {
            $context = stream_context_get_default();
            $opts = stream_context_get_options($context);
            if (!isset($opts['ssl']['ciphers'])
                || 'DEFAULT' === $opts['ssl']['ciphers']
            ) {
                stream_context_set_option($context, 'ssl', 'ciphers', 'ADH');
            }
        }
        // @codeCoverageIgnoreStart
        // The $port is customizable in testing.
        if (null === $port) {
            $port = $isUnencrypted ? 8728 : 8729;
        }
        // @codeCoverageIgnoreEnd

        try {
            $this->trans = new T\TcpClient(
                $host,
                $port,
                $persist,
                $timeout,
                $key,
                $crypto,
                $context
            );
        } catch (T\Exception $e) {
            throw new SocketException(
                'Error connecting to RouterOS',
                SocketException::CODE_CONNECTION_FAIL,
                $e
            );
        }
        $this->setCharset(
            self::getDefaultCharset(self::CHARSET_ALL),
            self::CHARSET_ALL
        );
    }
    
    /**
     * A shorthand gateway.
     * 
     * This is a magic PHP method that allows you to call the object as a
     * function. Depending on the argument given, one of the other functions in
     * the class is invoked and its returned value is returned by this function.
     * 
     * @param string $string A string of the word to send, or NULL to get the
     *     next word as a string.
     * 
     * @return int|string If a string is provided, returns the number of bytes
     *     sent, otherwise retuns the next word as a string.
     */
    public function __invoke($string = null)
    {
        return null === $string ? $this->getNextWord()
            : $this->sendWord($string);
    }
    
    /**
     * Checks whether a variable is a seekable stream resource.
     * 
     * @param mixed $var The value to check.
     * 
     * @return bool TRUE if $var is a seekable stream, FALSE otherwise.
     */
    public static function isSeekableStream($var)
    {
        if (T\Stream::isStream($var)) {
            $meta = stream_get_meta_data($var);
            return $meta['seekable'];
        }
        return false;
    }
    
    /**
     * Uses iconv to convert a stream from one charset to another.
     * 
     * @param string   $inCharset  The charset of the stream.
     * @param string   $outCharset The desired resulting charset.
     * @param resource $stream     The stream to convert. The stream is assumed
     *     to be seekable, and is read from its current position to its end,
     *     after which, it is seeked back to its starting position.
     * 
     * @return resource A new stream that uses the $out_charset. The stream is a
     *     subset from the original stream, from its current position to its
     *     end, seeked at its start.
     */
    public static function iconvStream($inCharset, $outCharset, $stream)
    {
        $bytes = 0;
        $result = fopen('php://temp', 'r+b');
        $iconvFilter = stream_filter_append(
            $result,
            'convert.iconv.' . $inCharset . '.' . $outCharset,
            STREAM_FILTER_WRITE
        );
        
        flock($stream, LOCK_SH);
        while (!feof($stream)) {
            $bytes += stream_copy_to_stream($stream, $result, 0xFFFFF);
        }
        fseek($stream, -$bytes, SEEK_CUR);
        flock($stream, LOCK_UN);
        
        stream_filter_remove($iconvFilter);
        rewind($result);
        return $result;
    }
    
    /**
     * Sets the default charset(s) for new connections.
     * 
     * @param mixed $charset     The charset to set. If $charsetType is
     *     {@link self::CHARSET_ALL}, you can supply either a string to use for
     *     all charsets, or an array with the charset types as keys, and the
     *     charsets as values.
     * @param int   $charsetType Which charset to set. Valid values are the
     *     CHARSET_* constants. Any other value is treated as
     *     {@link self::CHARSET_ALL}.
     * 
     * @return string|array The old charset. If $charsetType is
     *     {@link self::CHARSET_ALL}, the old values will be returned as an
     *     array with the types as keys, and charsets as values.
     * @see setCharset()
     */
    public static function setDefaultCharset(
        $charset,
        $charsetType = self::CHARSET_ALL
    ) {
        if (array_key_exists($charsetType, self::$defaultCharsets)) {
             $oldCharset = self::$defaultCharsets[$charsetType];
             self::$defaultCharsets[$charsetType] = $charset;
             return $oldCharset;
        } else {
            $oldCharsets = self::$defaultCharsets;
            self::$defaultCharsets = is_array($charset) ? $charset : array_fill(
                0,
                count(self::$defaultCharsets),
                $charset
            );
            return $oldCharsets;
        }
    }
    
    /**
     * Gets the default charset(s).
     * 
     * @param int $charsetType Which charset to get. Valid values are the
     *     CHARSET_* constants. Any other value is treated as
     *     {@link self::CHARSET_ALL}.
     * 
     * @return string|array The current charset. If $charsetType is
     *     {@link self::CHARSET_ALL}, the current values will be returned as an
     *     array with the types as keys, and charsets as values.
     * @see setDefaultCharset()
     */
    public static function getDefaultCharset($charsetType)
    {
        return array_key_exists($charsetType, self::$defaultCharsets)
            ? self::$defaultCharsets[$charsetType] : self::$defaultCharsets;
    }

    /**
     * Gets the length of a seekable stream.
     * 
     * Gets the length of a seekable stream.
     * 
     * @param resource $stream The stream to check. The stream is assumed to be
     *     seekable.
     * 
     * @return double The number of bytes in the stream between its current
     *     position and its end.
     */
    public static function seekableStreamLength($stream)
    {
        $streamPosition = (double) sprintf('%u', ftell($stream));
        fseek($stream, 0, SEEK_END);
        $streamLength = ((double) sprintf('%u', ftell($stream)))
            - $streamPosition;
        fseek($stream, $streamPosition, SEEK_SET);
        return $streamLength;
    }
    
    /**
     * Sets the charset(s) for this connection.
     * 
     * Sets the charset(s) for this connection. The specified charset(s) will be
     * used for all future words. When sending, {@link self::CHARSET_LOCAL} is
     * converted to {@link self::CHARSET_REMOTE}, and when receiving,
     * {@link self::CHARSET_REMOTE} is converted to {@link self::CHARSET_LOCAL}.
     * Setting  NULL to either charset will disable charset convertion, and data
     * will be both sent and received "as is".
     * 
     * @param mixed $charset     The charset to set. If $charsetType is
     *     {@link self::CHARSET_ALL}, you can supply either a string to use for
     *     all charsets, or an array with the charset types as keys, and the
     *     charsets as values.
     * @param int   $charsetType Which charset to set. Valid values are the
     *     CHARSET_* constants. Any other value is treated as
     *     {@link self::CHARSET_ALL}.
     * 
     * @return string|array The old charset. If $charsetType is
     *     {@link self::CHARSET_ALL}, the old values will be returned as an
     *     array with the types as keys, and charsets as values.
     * @see setDefaultCharset()
     */
    public function setCharset($charset, $charsetType = self::CHARSET_ALL)
    {
        if (array_key_exists($charsetType, $this->charsets)) {
             $oldCharset = $this->charsets[$charsetType];
             $this->charsets[$charsetType] = $charset;
             return $oldCharset;
        } else {
            $oldCharsets = $this->charsets;
            $this->charsets = is_array($charset) ? $charset : array_fill(
                0,
                count($this->charsets),
                $charset
            );
            return $oldCharsets;
        }
    }
    
    /**
     * Gets the charset(s) for this connection.
     * 
     * @param int $charsetType Which charset to get. Valid values are the
     *     CHARSET_* constants. Any other value is treated as
     *     {@link self::CHARSET_ALL}.
     * 
     * @return string|array The current charset. If $charsetType is
     *     {@link self::CHARSET_ALL}, the current values will be returned as an
     *     array with the types as keys, and charsets as values.
     * @see getDefaultCharset()
     * @see setCharset()
     */
    public function getCharset($charsetType)
    {
        return array_key_exists($charsetType, $this->charsets)
            ? $this->charsets[$charsetType] : $this->charsets;
    }

    /**
     * Gets the transmitter for this connection.
     * 
     * @return T\TcpClient The transmitter for this connection.
     */
    public function getTransmitter()
    {
        return $this->trans;
    }

    /**
     * Sends a word.
     * 
     * Sends a word and automatically encodes its length when doing so.
     * 
     * @param string $word The word to send.
     * 
     * @return int The number of bytes sent.
     * @see sendWordFromStream()
     * @see getNextWord()
     */
    public function sendWord($word)
    {
        if (null !== ($remoteCharset = $this->getCharset(self::CHARSET_REMOTE))
            && null !== ($localCharset = $this->getCharset(self::CHARSET_LOCAL))
        ) {
            $word = iconv(
                $localCharset,
                $remoteCharset . '//IGNORE//TRANSLIT',
                $word
            );
        }
        $length = strlen($word);
        static::verifyLengthSupport($length);
        if ($this->trans->isPersistent()) {
            $old = $this->trans->lock(T\Stream::DIRECTION_SEND);
            $bytes = $this->trans->send(self::encodeLength($length) . $word);
            $this->trans->lock($old, true);
            return $bytes;
        }
        return $this->trans->send(self::encodeLength($length) . $word);
    }

    /**
     * Sends a word based on a stream.
     * 
     * Sends a word based on a stream and automatically encodes its length when
     * doing so. The stream is read from its current position to its end, and
     * then returned to its current position. Because of those operations, the
     * supplied stream must be seekable.
     * 
     * @param string   $prefix A string to prepend before the stream contents.
     * @param resource $stream The seekable stream to send.
     * 
     * @return int The number of bytes sent.
     * @see sendWord()
     */
    public function sendWordFromStream($prefix, $stream)
    {
        if (!self::isSeekableStream($stream)) {
            throw new InvalidArgumentException(
                'The stream must be seekable.',
                InvalidArgumentException::CODE_SEEKABLE_REQUIRED
            );
        }
        if (null !== ($remoteCharset = $this->getCharset(self::CHARSET_REMOTE))
            && null !== ($localCharset = $this->getCharset(self::CHARSET_LOCAL))
        ) {
            $prefix = iconv(
                $localCharset,
                $remoteCharset . '//IGNORE//TRANSLIT',
                $prefix
            );
            $stream = self::iconvStream(
                $localCharset,
                $remoteCharset . '//IGNORE//TRANSLIT',
                $stream
            );
        }
        
        flock($stream, LOCK_SH);
        $totalLength = strlen($prefix) + self::seekableStreamLength($stream);
        static::verifyLengthSupport($totalLength);

        $bytes = $this->trans->send(self::encodeLength($totalLength) . $prefix);
        $bytes += $this->trans->send($stream);
        
        flock($stream, LOCK_UN);
        return $bytes;
    }

    /**
     * Verifies that the length is supported.
     * 
     * Verifies if the specified length is supported by the API. Throws a
     * {@link LengthException} if that's not the case. Currently, RouterOS
     * supports words up to 0xFFFFFFFF in length, so that's the only check
     * performed.
     * 
     * @param int $length The length to verify.
     * 
     * @return void
     */
    protected static function verifyLengthSupport($length)
    {
        if ($length > 0xFFFFFFFF) {
            throw new LengthException(
                'Words with length above 0xFFFFFFFF are not supported.',
                LengthException::CODE_UNSUPPORTED,
                null,
                $length
            );
        }
    }

    /**
     * Encodes the length as requred by the RouterOS API.
     * 
     * @param int $length The length to encode.
     * 
     * @return string The encoded length.
     */
    public static function encodeLength($length)
    {
        if ($length < 0) {
            throw new LengthException(
                'Length must not be negative.',
                LengthException::CODE_INVALID,
                null,
                $length
            );
        } elseif ($length < 0x80) {
            return chr($length);
        } elseif ($length < 0x4000) {
            return pack('n', $length |= 0x8000);
        } elseif ($length < 0x200000) {
            $length |= 0xC00000;
            return pack('n', $length >> 8) . chr($length & 0xFF);
        } elseif ($length < 0x10000000) {
            return pack('N', $length |= 0xE0000000);
        } elseif ($length <= 0xFFFFFFFF) {
            return chr(0xF0) . pack('N', $length);
        } elseif ($length <= 0x7FFFFFFFF) {
            $length = 'f' . base_convert($length, 10, 16);
            return chr(hexdec(substr($length, 0, 2))) .
                pack('N', hexdec(substr($length, 2)));
        }
        throw new LengthException(
            'Length must not be above 0x7FFFFFFFF.',
            LengthException::CODE_BEYOND_SHEME,
            null,
            $length
        );
    }

    /**
     * Get the next word in queue as a string.
     * 
     * Get the next word in queue as a string, after automatically decoding its
     * length.
     * 
     * @return string The word.
     * @see close()
     */
    public function getNextWord()
    {
        if ($this->trans->isPersistent()) {
            $old = $this->trans->lock(T\Stream::DIRECTION_RECEIVE);
            $word = $this->trans->receive(
                self::decodeLength($this->trans),
                'word'
            );
            $this->trans->lock($old, true);
        } else {
            $word = $this->trans->receive(
                self::decodeLength($this->trans),
                'word'
            );
        }
        
        if (null !== ($remoteCharset = $this->getCharset(self::CHARSET_REMOTE))
            && null !== ($localCharset = $this->getCharset(self::CHARSET_LOCAL))
        ) {
            $word = iconv(
                $remoteCharset,
                $localCharset . '//IGNORE//TRANSLIT',
                $word
            );
        }
        
        return $word;
    }

    /**
     * Get the next word in queue as a stream.
     * 
     * Get the next word in queue as a stream, after automatically decoding its
     * length.
     * 
     * @return resource The word, as a stream.
     * @see close()
     */
    public function getNextWordAsStream()
    {
        $filters = new T\FilterCollection();
        if (null !== ($remoteCharset = $this->getCharset(self::CHARSET_REMOTE))
            && null !== ($localCharset = $this->getCharset(self::CHARSET_LOCAL))
        ) {
            $filters->append(
                'convert.iconv.' .
                $remoteCharset . '.' . $localCharset . '//IGNORE//TRANSLIT'
            );
        }
        
        if ($this->trans->isPersistent()) {
            $old = $this->trans->lock(T\Stream::DIRECTION_RECEIVE);
            $stream = $this->trans->receiveStream(
                self::decodeLength($this->trans),
                $filters,
                'stream word'
            );
            $this->trans->lock($old, true);
        } else {
            $stream = $this->trans->receiveStream(
                self::decodeLength($this->trans),
                $filters,
                'stream word'
            );
        }
        
        return $stream;
    }

    /**
     * Decodes the lenght of the incoming message.
     * 
     * Decodes the lenght of the incoming message, as specified by the RouterOS
     * API.
     * 
     * @param T\Stream $trans The transmitter from which to decode the length of
     * the incoming message.
     * 
     * @return int The decoded length.
     */
    public static function decodeLength(T\Stream $trans)
    {
        if ($trans->isPersistent() && $trans instanceof T\TcpClient) {
            $old = $trans->lock($trans::DIRECTION_RECEIVE);
            $length = self::_decodeLength($trans);
            $trans->lock($old, true);
            return $length;
        }
        return self::_decodeLength($trans);
    }

    /**
     * Decodes the lenght of the incoming message.
     * 
     * Decodes the lenght of the incoming message, as specified by the RouterOS
     * API.
     * 
     * Difference with the non private function is that this one doesn't perform
     * locking if the connection is a persistent one.
     * 
     * @param T\Stream $trans The transmitter from which to decode the length of
     *     the incoming message.
     * 
     * @return int The decoded length.
     */
    private static function _decodeLength(T\Stream $trans)
    {
        $byte = ord($trans->receive(1, 'initial length byte'));
        if ($byte & 0x80) {
            if (($byte & 0xC0) === 0x80) {
                return (($byte & 077) << 8 ) + ord($trans->receive(1));
            } elseif (($byte & 0xE0) === 0xC0) {
                $rem = unpack('n~', $trans->receive(2));
                return (($byte & 037) << 16 ) + $rem['~'];
            } elseif (($byte & 0xF0) === 0xE0) {
                $rem = unpack('n~/C~~', $trans->receive(3));
                return (($byte & 017) << 24 ) + ($rem['~'] << 8) + $rem['~~'];
            } elseif (($byte & 0xF8) === 0xF0) {
                $rem = unpack('N~', $trans->receive(4));
                return (($byte & 007) * 0x100000000/* '<< 32' or '2^32' */)
                    + (double) sprintf('%u', $rem['~']);
            }
            throw new NotSupportedException(
                'Unknown control byte encountered.',
                NotSupportedException::CODE_CONTROL_BYTE,
                null,
                $byte
            );
        } else {
            return $byte;
        }
    }

    /**
     * Closes the opened connection, even if it is a persistent one.
     * 
     * @return bool TRUE on success, FALSE on failure.
     */
    public function close()
    {
        return $this->trans->close();
    }
}


File: /PEAR2\Net\RouterOS\DataFlowException.php
<?php

/**
 * RouterOS API client implementation.
 * 
 * RouterOS is the flag product of the company MikroTik and is a powerful router software. One of its many abilities is to allow control over it via an API. This package provides a client for that API, in turn allowing you to use PHP to control RouterOS hosts.
 * 
 * PHP version 5
 * 
 * @category  Net
 * @package   PEAR2_Net_RouterOS
 * @author    Vasil Rangelov <boen.robot@gmail.com>
 * @copyright 2011 Vasil Rangelov
 * @license   http://www.gnu.org/copyleft/lesser.html LGPL License 2.1
 * @version   1.0.0b5
 * @link      http://pear2.php.net/PEAR2_Net_RouterOS
 */
/**
 * The namespace declaration.
 */
namespace PEAR2\Net\RouterOS;

/**
 * Base of this class.
 */
use RuntimeException;

/**
 * Exception thrown when the request/response cycle goes an unexpected way.
 * 
 * @category Net
 * @package  PEAR2_Net_RouterOS
 * @author   Vasil Rangelov <boen.robot@gmail.com>
 * @license  http://www.gnu.org/copyleft/lesser.html LGPL License 2.1
 * @link     http://pear2.php.net/PEAR2_Net_RouterOS
 */
class DataFlowException extends RuntimeException implements Exception
{
    const CODE_INVALID_CREDENTIALS = 10000;
    const CODE_TAG_REQUIRED = 10500;
    const CODE_TAG_UNIQUE = 10501;
    const CODE_UNKNOWN_REQUEST = 10900;
    const CODE_CANCEL_FAIL = 11200;
}


File: /PEAR2\Net\RouterOS\Exception.php
<?php

/**
 * RouterOS API client implementation.
 * 
 * RouterOS is the flag product of the company MikroTik and is a powerful router software. One of its many abilities is to allow control over it via an API. This package provides a client for that API, in turn allowing you to use PHP to control RouterOS hosts.
 * 
 * PHP version 5
 * 
 * @category  Net
 * @package   PEAR2_Net_RouterOS
 * @author    Vasil Rangelov <boen.robot@gmail.com>
 * @copyright 2011 Vasil Rangelov
 * @license   http://www.gnu.org/copyleft/lesser.html LGPL License 2.1
 * @version   1.0.0b5
 * @link      http://pear2.php.net/PEAR2_Net_RouterOS
 */
/**
 * The namespace declaration.
 */
namespace PEAR2\Net\RouterOS;

/**
 * Generic exception class of this package.
 * 
 * @category Net
 * @package  PEAR2_Net_RouterOS
 * @author   Vasil Rangelov <boen.robot@gmail.com>
 * @license  http://www.gnu.org/copyleft/lesser.html LGPL License 2.1
 * @link     http://pear2.php.net/PEAR2_Net_RouterOS
 */
interface Exception
{
}


File: /PEAR2\Net\RouterOS\InvalidArgumentException.php
<?php

/**
 * RouterOS API client implementation.
 * 
 * RouterOS is the flag product of the company MikroTik and is a powerful router software. One of its many abilities is to allow control over it via an API. This package provides a client for that API, in turn allowing you to use PHP to control RouterOS hosts.
 * 
 * PHP version 5
 * 
 * @category  Net
 * @package   PEAR2_Net_RouterOS
 * @author    Vasil Rangelov <boen.robot@gmail.com>
 * @copyright 2011 Vasil Rangelov
 * @license   http://www.gnu.org/copyleft/lesser.html LGPL License 2.1
 * @version   1.0.0b5
 * @link      http://pear2.php.net/PEAR2_Net_RouterOS
 */
/**
 * The namespace declaration.
 */
namespace PEAR2\Net\RouterOS;

use InvalidArgumentException as I;

/**
 * Exception thrown when there's something wrong with message arguments.
 * 
 * @category Net
 * @package  PEAR2_Net_RouterOS
 * @author   Vasil Rangelov <boen.robot@gmail.com>
 * @license  http://www.gnu.org/copyleft/lesser.html LGPL License 2.1
 * @link     http://pear2.php.net/PEAR2_Net_RouterOS
 */
class InvalidArgumentException extends I implements Exception
{
    const CODE_SEEKABLE_REQUIRED = 1100;
    const CODE_NAME_INVALID = 20100;
    const CODE_ABSOLUTE_REQUIRED = 40200;
    const CODE_CMD_UNRESOLVABLE = 40201;
    const CODE_CMD_INVALID = 40202;
    const CODE_NAME_UNPARSABLE = 41000;
    const CODE_VALUE_UNPARSABLE = 41001;
}


File: /PEAR2\Net\RouterOS\LengthException.php
<?php

/**
 * RouterOS API client implementation.
 * 
 * RouterOS is the flag product of the company MikroTik and is a powerful router software. One of its many abilities is to allow control over it via an API. This package provides a client for that API, in turn allowing you to use PHP to control RouterOS hosts.
 * 
 * PHP version 5
 * 
 * @category  Net
 * @package   PEAR2_Net_RouterOS
 * @author    Vasil Rangelov <boen.robot@gmail.com>
 * @copyright 2011 Vasil Rangelov
 * @license   http://www.gnu.org/copyleft/lesser.html LGPL License 2.1
 * @version   1.0.0b5
 * @link      http://pear2.php.net/PEAR2_Net_RouterOS
 */
/**
 * The namespace declaration.
 */
namespace PEAR2\Net\RouterOS;

/**
 * Base of this class.
 */
use LengthException as L;

/**
 * Exception thrown when there is a problem with a word's length.
 * 
 * @category Net
 * @package  PEAR2_Net_RouterOS
 * @author   Vasil Rangelov <boen.robot@gmail.com>
 * @license  http://www.gnu.org/copyleft/lesser.html LGPL License 2.1
 * @link     http://pear2.php.net/PEAR2_Net_RouterOS
 */
class LengthException extends L implements Exception
{
    
    const CODE_UNSUPPORTED = 1200;
    const CODE_INVALID = 1300;
    const CODE_BEYOND_SHEME = 1301;

    /**
     *
     * @var mixed The problematic length.
     */
    private $_length;

    /**
     * Creates a new LengthException.
     * 
     * @param string     $message  The Exception message to throw.
     * @param int        $code     The Exception code.
     * @param \Exception $previous The previous exception used for the exception
     *     chaining.
     * @param number     $length   The length.
     */
    public function __construct(
        $message,
        $code = 0,
        $previous = null,
        $length = null
    ) {
        parent::__construct($message, $code, $previous);
        $this->_length = $length;
    }

    /**
     * Gets the length.
     * 
     * @return number The length.
     */
    public function getLength()
    {
        return $this->_length;
    }

    // @codeCoverageIgnoreStart
    // String representation is not reliable in testing

    /**
     * Returns a string representation of the exception.
     * 
     * @return string The exception as a string.
     */
    public function __toString()
    {
        return parent::__toString() . "\nLength:{$this->_length}";
    }

    // @codeCoverageIgnoreEnd
}


File: /PEAR2\Net\RouterOS\Message.php
<?php

/**
 * RouterOS API client implementation.
 * 
 * RouterOS is the flag product of the company MikroTik and is a powerful router software. One of its many abilities is to allow control over it via an API. This package provides a client for that API, in turn allowing you to use PHP to control RouterOS hosts.
 * 
 * PHP version 5
 * 
 * @category  Net
 * @package   PEAR2_Net_RouterOS
 * @author    Vasil Rangelov <boen.robot@gmail.com>
 * @copyright 2011 Vasil Rangelov
 * @license   http://www.gnu.org/copyleft/lesser.html LGPL License 2.1
 * @version   1.0.0b5
 * @link      http://pear2.php.net/PEAR2_Net_RouterOS
 */
/**
 * The namespace declaration.
 */
namespace PEAR2\Net\RouterOS;

/**
 * Implements this interface.
 */
use Countable;

/**
 * Implements this interface.
 */
use IteratorAggregate;

/**
 * Requred for IteratorAggregate::getIterator() to work properly with foreach.
 */
use ArrayObject;

/**
 * Represents a RouterOS message.
 * 
 * @category Net
 * @package  PEAR2_Net_RouterOS
 * @author   Vasil Rangelov <boen.robot@gmail.com>
 * @license  http://www.gnu.org/copyleft/lesser.html LGPL License 2.1
 * @link     http://pear2.php.net/PEAR2_Net_RouterOS
 */
abstract class Message implements IteratorAggregate, Countable
{

    /**
     * @var array An array with message attributes. Each array key is the the
     *     name of an attribute, and the correspding array value is the value
     *     for that attribute.
     */
    protected $attributes = array();

    /**
     * @var string An optional tag to associate the message with.
     */
    private $_tag = null;
    
    /**
     * A shorthand gateway.
     * 
     * This is a magic PHP method that allows you to call the object as a
     * function. Depending on the argument given, one of the other functions in
     * the class is invoked and its returned value is returned by this function.
     * 
     * @param string $name The name of an attribute to get the value of, or NULL
     *     to get the tag.
     * 
     * @return string|resource The value of the specified attribute,
     *     or the tag if NULL is provided.
     */
    public function __invoke($name = null)
    {
        if (null === $name) {
            return $this->getTag();
        }
        return $this->getAttribute($name);
    }

    /**
     * Sanitizes a name of an attribute (message or query one).
     * 
     * @param mixed $name The name to sanitize.
     * 
     * @return string The sanitized name.
     */
    public static function sanitizeAttributeName($name)
    {
        $name = (string) $name;
        if ((empty($name) && $name !== '0')
            || preg_match('/[=\s]/s', $name)
        ) {
            throw new InvalidArgumentException(
                'Invalid name of argument supplied.',
                InvalidArgumentException::CODE_NAME_INVALID
            );
        }
        return $name;
    }

    /**
     * Sanitizes a value of an attribute (message or query one).
     * 
     * @param mixed $value The value to sanitize.
     * 
     * @return string The sanitized value.
     */
    public static function sanitizeAttributeValue($value)
    {
        if (Communicator::isSeekableStream($value)) {
            return $value;
        } else {
            return (string) $value;
        }
    }

    /**
     * Gets the tag that the message is associated with.
     * 
     * @return string The current tag or NULL if there isn't a tag.
     * @see setTag()
     */
    public function getTag()
    {
        return $this->_tag;
    }

    /**
     * Sets the tag to associate the request with.
     * 
     * Sets the tag to associate the message with. Setting NULL erases the
     * currently set tag.
     * 
     * @param string $tag The tag to set.
     * 
     * @return $this The message object.
     * @see getTag()
     */
    protected function setTag($tag)
    {
        $this->_tag = (null === $tag) ? null : (string) $tag;
        return $this;
    }

    /**
     * Gets the value of an attribute.
     * 
     * @param string $name The name of the attribute.
     * 
     * @return string|resource|null The value of the specified attribute.
     *     Returns NULL if such an attribute is not set.
     * @see setAttribute()
     */
    protected function getAttribute($name)
    {
        $name = self::sanitizeAttributeName($name);
        if (array_key_exists($name, $this->attributes)) {
            return $this->attributes[$name];
        }
        return null;
    }

    /**
     * Gets all arguments in an array.
     * 
     * @return ArrayObject An ArrayObject with the keys being argument names,
     *     and the array values being argument values.
     * @see getArgument()
     * @see setArgument()
     */
    public function getIterator()
    {
        return new ArrayObject($this->attributes);
    }

    /**
     * Counts the number of arguments.
     * 
     * @param int $mode The counter mode.
     *     Either COUNT_NORMAL or COUNT_RECURSIVE.
     *     When in normal mode, counts the number of arguments.
     *     When in recursive mode, counts the number of API words
     *     (including the empty word at the end).
     * 
     * @return int The number of arguments/words.
     */
    public function count($mode = COUNT_NORMAL)
    {
        $result = count($this->attributes);
        if ($mode !== COUNT_NORMAL) {
            $result += 2/*first+last word*/
                + (int)(null !== $this->getTag());
        }
        return $result;
    }

    /**
     * Sets an attribute for the message.
     * 
     * @param string               $name  Name of the attribute.
     * @param string|resource|null $value Value of the attribute as a string or
     *     seekable stream.
     *     Setting the value to NULL removes an argument of this name.
     *     If a seekable stream is provided, it is sent from its current
     *     posistion to its end, and the pointer is seeked back to its current
     *     position after sending.
     *     Non seekable streams, as well as all other types, are casted to a
     *     string.
     * 
     * @return $this The message object.
     * @see getArgument()
     */
    protected function setAttribute($name, $value = '')
    {
        if (null === $value) {
            unset($this->attributes[self::sanitizeAttributeName($name)]);
        } else {
            $this->attributes[self::sanitizeAttributeName($name)]
                = self::sanitizeAttributeValue($value);
        }
        return $this;
    }

    /**
     * Removes all attributes from the message.
     * 
     * @return $this The message object.
     */
    protected function removeAllAttributes()
    {
        $this->attributes = array();
        return $this;
    }
}


File: /PEAR2\Net\RouterOS\NotSupportedException.php
<?php

/**
 * RouterOS API client implementation.
 * 
 * RouterOS is the flag product of the company MikroTik and is a powerful router software. One of its many abilities is to allow control over it via an API. This package provides a client for that API, in turn allowing you to use PHP to control RouterOS hosts.
 * 
 * PHP version 5
 * 
 * @category  Net
 * @package   PEAR2_Net_RouterOS
 * @author    Vasil Rangelov <boen.robot@gmail.com>
 * @copyright 2011 Vasil Rangelov
 * @license   http://www.gnu.org/copyleft/lesser.html LGPL License 2.1
 * @version   1.0.0b5
 * @link      http://pear2.php.net/PEAR2_Net_RouterOS
 */
/**
 * The namespace declaration.
 */
namespace PEAR2\Net\RouterOS;

/**
 * Base of this class.
 */
use Exception as E;

/**
 * Exception thrown when encountering something not supported by RouterOS or
 * this package.
 * 
 * @category Net
 * @package  PEAR2_Net_RouterOS
 * @author   Vasil Rangelov <boen.robot@gmail.com>
 * @license  http://www.gnu.org/copyleft/lesser.html LGPL License 2.1
 * @link     http://pear2.php.net/PEAR2_Net_RouterOS
 */
class NotSupportedException extends E implements Exception
{

    const CODE_CONTROL_BYTE = 1601;

    /**
     * @var mixed The unsuppported value.
     */
    private $_value;

    /**
     * Creates a new NotSupportedException.
     * 
     * @param string     $message  The Exception message to throw.
     * @param int        $code     The Exception code.
     * @param \Exception $previous The previous exception used for the exception
     *     chaining.
     * @param mixed      $value    The unsupported value.
     */
    public function __construct(
        $message,
        $code = 0,
        $previous = null,
        $value = null
    ) {
        parent::__construct($message, $code, $previous);
        $this->_value = $value;
    }

    /**
     * Gets the unsupported value.
     * 
     * @return mixed The unsupported value.
     */
    public function getValue()
    {
        return $this->_value;
    }

    // @codeCoverageIgnoreStart
    // String representation is not reliable in testing

    /**
     * Returns a string representation of the exception.
     * 
     * @return string The exception as a string.
     */
    public function __toString()
    {
        return parent::__toString() . "\nValue:{$this->_value}";
    }

    // @codeCoverageIgnoreEnd
}


File: /PEAR2\Net\RouterOS\Query.php
<?php

/**
 * RouterOS API client implementation.
 * 
 * RouterOS is the flag product of the company MikroTik and is a powerful router software. One of its many abilities is to allow control over it via an API. This package provides a client for that API, in turn allowing you to use PHP to control RouterOS hosts.
 * 
 * PHP version 5
 * 
 * @category  Net
 * @package   PEAR2_Net_RouterOS
 * @author    Vasil Rangelov <boen.robot@gmail.com>
 * @copyright 2011 Vasil Rangelov
 * @license   http://www.gnu.org/copyleft/lesser.html LGPL License 2.1
 * @version   1.0.0b5
 * @link      http://pear2.php.net/PEAR2_Net_RouterOS
 */
/**
 * The namespace declaration.
 */
namespace PEAR2\Net\RouterOS;

/**
 * Refers to transmitter direction constants.
 */
use PEAR2\Net\Transmitter as T;

/**
 * Represents a query for RouterOS requests.
 * 
 * @category Net
 * @package  PEAR2_Net_RouterOS
 * @author   Vasil Rangelov <boen.robot@gmail.com>
 * @license  http://www.gnu.org/copyleft/lesser.html LGPL License 2.1
 * @link     http://pear2.php.net/PEAR2_Net_RouterOS
 */
class Query
{

    /**
     * Checks if the property exists.
     */
    const OP_EX = '';
    
    /**
     * Checks if the property does not exist.
     */
    const OP_NEX = '-';
    
    /**
     * Checks if the property equals a certain value.
     */
    const OP_EQ = '=';
    
    /**
     * Checks if the property is less than a certain value.
     */
    const OP_LT = '<';
    
    /**
     * Checks if the property is greather than a certain value.
     */
    const OP_GT = '>';

    /**
     * @var array An array of the words forming the query. Each value is an
     *     array with the first member being the predicate (operator and name),
     *     and the second member being the value for the predicate.
     */
    protected $words = array();

    /**
     * This class is not to be instantiated normally, but by static methods
     * instead. Use {@link static::where()} to create an instance of it.
     */
    private function __construct()
    {
        
    }

    /**
     * Sanitizes the operator of a condition.
     * 
     * @param string $operator The operator to sanitize.
     * 
     * @return string The sanitized operator.
     */
    protected static function sanitizeOperator($operator)
    {
        $operator = (string) $operator;
        switch ($operator) {
        case Query::OP_EX:
        case Query::OP_NEX:
        case Query::OP_EQ:
        case Query::OP_LT:
        case Query::OP_GT:
            return $operator;
        default:
            throw new UnexpectedValueException(
                'Unknown operator specified',
                UnexpectedValueException::CODE_ACTION_UNKNOWN,
                null,
                $operator
            );
        }
    }

    /**
     * Creates a new query with an initial condition.
     * 
     * @param string               $name     The name of the property to test.
     * @param string|resource|null $value    Value of the property as a string
     *     or seekable stream. Not required for existence tests.
     *     If a seekable stream is provided, it is sent from its current
     *     posistion to its end, and the pointer is seeked back to its current
     *     position after sending.
     *     Non seekable streams, as well as all other types, are casted to a
     *     string.
     * @param string               $operator One of the OP_* constants.
     *     Describes the operation to perform.
     * 
     * @return static A new query object.
     */
    public static function where(
        $name,
        $value = null,
        $operator = self::OP_EX
    ) {
        $query = new static;
        return $query->addWhere($name, $value, $operator);
    }

    /**
     * Negates the query.
     * 
     * @return $this The query object.
     */
    public function not()
    {
        $this->words[] = array('#!', null);
        return $this;
    }

    /**
     * Adds a condition as an alternative to the query.
     * 
     * @param string               $name     The name of the property to test.
     * @param string|resource|null $value    Value of the property as a string
     *     or seekable stream. Not required for existence tests.
     *     If a seekable stream is provided, it is sent from its current
     *     posistion to its end, and the pointer is seeked back to its current
     *     position after sending.
     *     Non seekable streams, as well as all other types, are casted to a
     *     string.
     * @param string               $operator One of the OP_* constants.
     *     Describes the operation to perform.
     * 
     * @return $this The query object.
     */
    public function orWhere($name, $value = null, $operator = self::OP_EX)
    {
        $this->addWhere($name, $value, $operator)->words[] = array('#|', null);
        return $this;
    }

    /**
     * Adds a condition in addition to the query.
     * 
     * @param string               $name     The name of the property to test.
     * @param string|resource|null $value    Value of the property as a string
     *     or seekable stream. Not required for existence tests.
     *     If a seekable stream is provided, it is sent from its current
     *     posistion to its end, and the pointer is seeked back to its current
     *     position after sending.
     *     Non seekable streams, as well as all other types, are casted to a
     *     string.
     * @param string               $operator One of the OP_* constants.
     *     Describes the operation to perform.
     * 
     * @return $this The query object.
     */
    public function andWhere($name, $value = null, $operator = self::OP_EX)
    {
        $this->addWhere($name, $value, $operator)->words[] = array('#&', null);
        return $this;
    }

    /**
     * Sends the query over a communicator.
     * 
     * @param Communicator $com The communicator to send the query over.
     * 
     * @return int The number of bytes sent.
     */
    public function send(Communicator $com)
    {
        if ($com->getTransmitter()->isPersistent()) {
            $old = $com->getTransmitter()->lock(T\Stream::DIRECTION_SEND);
            $bytes = $this->_send($com);
            $com->getTransmitter()->lock($old, true);
            return $bytes;
        }
        return $this->_send($com);
    }

    /**
     * Sends the query over a communicator.
     * 
     * The only difference with the non private equivalent is that this one does
     * not do locking.
     * 
     * @param Communicator $com The communicator to send the query over.
     * 
     * @return int The number of bytes sent.
     */
    private function _send(Communicator $com)
    {
        if (!$com->getTransmitter()->isAcceptingData()) {
            throw new SocketException(
                'Transmitter is invalid. Sending aborted.',
                SocketException::CODE_QUERY_SEND_FAIL
            );
        }
        $bytes = 0;
        foreach ($this->words as $queryWord) {
            list($predicate, $value) = $queryWord;
            $prefix = '?' . $predicate;
            if (null === $value) {
                $bytes += $com->sendWord($prefix);
            } else {
                $prefix .= '=';
                if (is_string($value)) {
                    $bytes += $com->sendWord($prefix . $value);
                } else {
                    $bytes += $com->sendWordFromStream($prefix, $value);
                }
            }
        }
        return $bytes;
    }

    /**
     * Adds a condition.
     * 
     * @param string               $name     The name of the property to test.
     * @param string|resource|null $value    Value of the property as a string
     *     or seekable stream. Not required for existence tests.
     *     If a seekable stream is provided, it is sent from its current
     *     posistion to its end, and the pointer is seeked back to its current
     *     position after sending.
     *     Non seekable streams, as well as all other types, are casted to a
     *     string.
     * @param string               $operator One of the ACTION_* constants.
     *     Describes the operation to perform.
     * 
     * @return $this The query object.
     */
    protected function addWhere($name, $value, $operator)
    {
        $this->words[] = array(
            static::sanitizeOperator($operator)
            . Message::sanitizeAttributeName($name),
            (null === $value ? null : Message::sanitizeAttributeValue($value))
        );
        return $this;
    }
}


File: /PEAR2\Net\RouterOS\Registry.php
<?php

/**
 * RouterOS API client implementation.
 * 
 * RouterOS is the flag product of the company MikroTik and is a powerful router software. One of its many abilities is to allow control over it via an API. This package provides a client for that API, in turn allowing you to use PHP to control RouterOS hosts.
 * 
 * PHP version 5
 * 
 * @category  Net
 * @package   PEAR2_Net_RouterOS
 * @author    Vasil Rangelov <boen.robot@gmail.com>
 * @copyright 2011 Vasil Rangelov
 * @license   http://www.gnu.org/copyleft/lesser.html LGPL License 2.1
 * @version   1.0.0b5
 * @link      http://pear2.php.net/PEAR2_Net_RouterOS
 */
/**
 * The namespace declaration.
 */
namespace PEAR2\Net\RouterOS;

/**
 * Uses shared memory to keep responses in.
 */
use PEAR2\Cache\SHM;

/**
 * A RouterOS registry.
 * 
 * Provides functionality for managing the request/response flow. Particularly
 * useful in persistent connections.
 * 
 * Note that this class is not meant to be called directly.
 * 
 * @category Net
 * @package  PEAR2_Net_RouterOS
 * @author   Vasil Rangelov <boen.robot@gmail.com>
 * @license  http://www.gnu.org/copyleft/lesser.html LGPL License 2.1
 * @link     http://pear2.php.net/PEAR2_Net_RouterOS
 */
class Registry
{
    /**
     * @var SHM The storage. 
     */
    protected $shm;
    
    /**
     * @var int ID of request. Populated at first instance in request.
     */
    protected static $requestId = -1;
    
    /**
     * @var int ID to be given to next instance, after incrementing it.
     */
    protected static $instanceIdSeed = -1;
    
    /**
     * @var int ID of instance within the request.
     */
    protected $instanceId;
    
    /**
     * Creates a registry.
     * 
     * @param string $uri An URI to bind the registry to.
     */
    public function __construct($uri)
    {
        $this->shm = SHM::factory(__CLASS__ . ' ' . $uri);
        if (-1 === self::$requestId) {
            self::$requestId = $this->shm->add('requestId', 0)
                ? 0 : $this->shm->inc('requestId');
        }
        $this->instanceId = ++self::$instanceIdSeed;
        $this->shm->add('responseBuffer_' . $this->getOwnershipTag(), array());
    }
    
    /**
     * Parses a tag.
     * 
     * Parses a tag to reveal the ownership part of it, and the original tag.
     * 
     * @param string $tag The tag (as received) to parse.
     * 
     * @return array An array with the first member being the ownership tag, and
     *     the second one being the original tag. 
     */
    public static function parseTag($tag)
    {
        if (null === $tag) {
            return array(null, null);
        }
        $result = explode('__', $tag, 2);
        $result[0] .= '__';
        if ('' === $result[1]) {
            $result[1] = null;
        }
        return $result;
    }
    
    /**
     * Checks if this instance is the tagless mode owner.
     * 
     * @return bool TRUE if this instance is the tagless mode owner, FALSE
     *     otherwise.
     */
    public function isTaglessModeOwner()
    {
        $this->shm->lock('taglessModeOwner');
        $result = $this->shm->exists('taglessModeOwner')
            && $this->getOwnershipTag() === $this->shm->get('taglessModeOwner');
        $this->shm->unlock('taglessModeOwner');
        return $result;
    }
    
    /**
     * Sets the "tagless mode" setting.
     * 
     * While in tagless mode, this instance will claim owhership of any
     * responses without a tag. While not in this mode, any requests without a
     * tag will be given to all instances.
     * 
     * Regardless of mode, if the type of the response is
     * {@link Response::TYPE_FATAL}, it will be given to all instances.
     * 
     * @param bool $taglessMode TRUE to claim tagless ownership, FALSE to
     *     release such ownership, if taken.
     * 
     * @return bool TRUE on success, FALSE on failure. 
     */
    public function setTaglessMode($taglessMode)
    {
        return $taglessMode
            ?   ($this->shm->lock('taglessMode')
                && $this->shm->lock('taglessModeOwner')
                && $this->shm->add('taglessModeOwner', $this->getOwnershipTag())
                && $this->shm->unlock('taglessModeOwner'))
            :   ($this->isTaglessModeOwner()
                && $this->shm->lock('taglessModeOwner')
                && $this->shm->delete('taglessModeOwner')
                && $this->shm->unlock('taglessModeOwner')
                && $this->shm->unlock('taglessMode'));
    }
    
    /**
     * Get the ownership tag for this instance.
     * 
     * @return string The ownership tag for this registry instance. 
     */
    public function getOwnershipTag()
    {
        return self::$requestId . '_' . $this->instanceId . '__';
    }
    
    /**
     * Add a response to the registry.
     * 
     * @param Response $response     The response to add. The caller of this
     *     function is responsible for ensuring that the ownership tag and the
     *     original tag are separated, so that only the original one remains in
     *     the response.
     * @param string   $ownershipTag The ownership tag that the response had.
     * 
     * @return bool TRUE if the request was added to its buffer, FALSE if
     *     this instance owns the response, and therefore doesn't need to add
     *     the response to its buffer.
     */
    public function add(Response $response, $ownershipTag)
    {
        if ($this->getOwnershipTag() === $ownershipTag
            || ($this->isTaglessModeOwner()
            && $response->getType() !== Response::TYPE_FATAL)
        ) {
            return false;
        }
        
        if (null === $ownershipTag) {
            $this->shm->lock('taglessModeOwner');
            if ($this->shm->exists('taglessModeOwner')
                && $response->getType() !== Response::TYPE_FATAL
            ) {
                $ownershipTag = $this->shm->get('taglessModeOwner');
                $this->shm->unlock('taglessModeOwner');
            } else {
                $this->shm->unlock('taglessModeOwner');
                foreach ($this->shm->getIterator(
                    '/^(responseBuffer\_)/',
                    true
                ) as $targetBufferName) {
                    $this->_add($response, $targetBufferName);
                }
                return true;
            }
        }
        
        $this->_add($response, 'responseBuffer_' . $ownershipTag);
        return true;
    }
    
    /**
     * Adds a response to a buffer.
     * 
     * @param Response $response         The response to add.
     * @param string   $targetBufferName The name of the buffer to add the
     *     response to.
     * 
     * @return void
     */
    private function _add(Response $response, $targetBufferName)
    {
        if ($this->shm->lock($targetBufferName)) {
            $targetBuffer = $this->shm->get($targetBufferName);
            $targetBuffer[] = $response;
            $this->shm->set($targetBufferName, $targetBuffer);
            $this->shm->unlock($targetBufferName);
        }
    }
    
    /**
     * Gets the next response from this instance's buffer.
     * 
     * @return Response|null The next response, or NULL if there isn't one. 
     */
    public function getNextResponse()
    {
        $response = null;
        $targetBufferName = 'responseBuffer_' . $this->getOwnershipTag();
        if ($this->shm->exists($targetBufferName)
            && $this->shm->lock($targetBufferName)
        ) {
            $targetBuffer = $this->shm->get($targetBufferName);
            if (!empty($targetBuffer)) {
                $response = array_shift($targetBuffer);
                $this->shm->set($targetBufferName, $targetBuffer);
            }
            $this->shm->unlock($targetBufferName);
        }
        return $response;
    }
    
    /**
     * Closes the registry.
     * 
     * Closes the registry, meaning that all buffers are cleared.
     * 
     * @return void 
     */
    public function close()
    {
        self::$requestId = -1;
        self::$instanceIdSeed = -1;
        $this->shm->clear();
    }
    
    /**
     * Removes a buffer.
     * 
     * @param string $targetBufferName The buffer to remove.
     * 
     * @return void
     */
    private function _close($targetBufferName)
    {
        if ($this->shm->lock($targetBufferName)) {
            $this->shm->delete($targetBufferName);
            $this->shm->unlock($targetBufferName);
        }
    }
    
    /**
     * Removes this instance's buffer. 
     */
    public function __destruct()
    {
        $this->_close('responseBuffer_' . $this->getOwnershipTag());
    }
}


File: /PEAR2\Net\RouterOS\Request.php
<?php

/**
 * RouterOS API client implementation.
 * 
 * RouterOS is the flag product of the company MikroTik and is a powerful router software. One of its many abilities is to allow control over it via an API. This package provides a client for that API, in turn allowing you to use PHP to control RouterOS hosts.
 * 
 * PHP version 5
 * 
 * @category  Net
 * @package   PEAR2_Net_RouterOS
 * @author    Vasil Rangelov <boen.robot@gmail.com>
 * @copyright 2011 Vasil Rangelov
 * @license   http://www.gnu.org/copyleft/lesser.html LGPL License 2.1
 * @version   1.0.0b5
 * @link      http://pear2.php.net/PEAR2_Net_RouterOS
 */
/**
 * The namespace declaration.
 */
namespace PEAR2\Net\RouterOS;

/**
 * Refers to transmitter direction constants.
 */
use PEAR2\Net\Transmitter as T;

/**
 * Represents a RouterOS request.
 * 
 * @category Net
 * @package  PEAR2_Net_RouterOS
 * @author   Vasil Rangelov <boen.robot@gmail.com>
 * @license  http://www.gnu.org/copyleft/lesser.html LGPL License 2.1
 * @link     http://pear2.php.net/PEAR2_Net_RouterOS
 */
class Request extends Message
{

    /**
     * @var string The command to be executed.
     */
    private $_command;

    /**
     * @var Query A query for the command.
     */
    private $_query;

    /**
     * Creates a request to send to RouterOS.
     * 
     * @param string $command The command to send. Can also contain arguments
     *     expressed in a shell-like syntax.
     * @param Query  $query   A query to associate with the request.
     * @param string $tag     The tag for the request.
     * 
     * @see setCommand()
     * @see setArgument()
     * @see setTag()
     * @see setQuery()
     */
    public function __construct($command, Query $query = null, $tag = null)
    {
        if (false !== strpos($command, '=')
            && false !== ($spaceBeforeEquals = strrpos(
                strstr($command, '=', true),
                ' '
            ))
        ) {
            $this->parseArgumentString(substr($command, $spaceBeforeEquals));
            $command = rtrim(substr($command, 0, $spaceBeforeEquals));
        }
        $this->setCommand($command);
        $this->setQuery($query);
        $this->setTag($tag);
    }
    
    /**
     * A shorthand gateway.
     * 
     * This is a magic PHP method that allows you to call the object as a
     * function. Depending on the argument given, one of the other functions in
     * the class is invoked and its returned value is returned by this function.
     * 
     * @param Query|Communicator|string|null $arg A {@link Query} to associate
     *     the request with, a {@link Communicator} to send the request over,
     *     an argument to get the value of, or NULL to get the tag. If a
     *     second argument is provided, this becomes the name of the argument to
     *     set the value of, and the second argument is the value to set.
     * 
     * @return string|resource|int|$this Whatever the long form
     *     function returns.
     */
    public function __invoke($arg = null)
    {
        if (func_num_args() > 1) {
            return $this->setArgument(func_get_arg(0), func_get_arg(1));
        }
        if ($arg instanceof Query) {
            return $this->setQuery($arg);
        }
        if ($arg instanceof Communicator) {
            return $this->send($arg);
        }
        return parent::__invoke($arg);
    }

    /**
     * Sets the command to send to RouterOS.
     * 
     * Sets the command to send to RouterOS. The command can use the API or CLI
     * syntax of RouterOS, but either way, it must be absolute (begin  with a
     * "/") and without arguments.
     * 
     * @param string $command The command to send.
     * 
     * @return $this The request object.
     * @see getCommand()
     * @see setArgument()
     */
    public function setCommand($command)
    {
        $command = (string) $command;
        if (strpos($command, '/') !== 0) {
            throw new InvalidArgumentException(
                'Commands must be absolute.',
                InvalidArgumentException::CODE_ABSOLUTE_REQUIRED
            );
        }
        if (substr_count($command, '/') === 1) {
            //Command line syntax convertion
            $cmdParts = preg_split('#[\s/]+#sm', $command);
            $cmdRes = array($cmdParts[0]);
            for ($i = 1, $n = count($cmdParts); $i < $n; $i++) {
                if ('..' === $cmdParts[$i]) {
                    $delIndex = count($cmdRes) - 1;
                    if ($delIndex < 1) {
                        throw new InvalidArgumentException(
                            'Unable to resolve command',
                            InvalidArgumentException::CODE_CMD_UNRESOLVABLE
                        );
                    }
                    unset($cmdRes[$delIndex]);
                    $cmdRes = array_values($cmdRes);
                } else {
                    $cmdRes[] = $cmdParts[$i];
                }
            }
            $command = implode('/', $cmdRes);
        }
        if (!preg_match('#^/\S+$#sm', $command)) {
            throw new InvalidArgumentException(
                'Invalid command supplied.',
                InvalidArgumentException::CODE_CMD_INVALID
            );
        }
        $this->_command = $command;
        return $this;
    }

    /**
     * Gets the command that will be send to RouterOS.
     * 
     * Gets the command that will be send to RouterOS in its API syntax.
     * 
     * @return string The command to send.
     * @see setCommand()
     */
    public function getCommand()
    {
        return $this->_command;
    }

    /**
     * Sets the query to send with the command.
     * 
     * @param Query $query The query to be set. Setting NULL will remove the
     *     currently associated query.
     * 
     * @return $this The request object.
     * @see getQuery()
     */
    public function setQuery(Query $query = null)
    {
        $this->_query = $query;
        return $this;
    }

    /**
     * Gets the currently associated query
     * 
     * @return Query The currently associated query.
     * @see setQuery()
     */
    public function getQuery()
    {
        return $this->_query;
    }

    /**
     * Sets the tag to associate the request with.
     * 
     * Sets the tag to associate the request with. Setting NULL erases the
     * currently set tag.
     * 
     * @param string $tag The tag to set.
     * 
     * @return $this The request object.
     * @see getTag()
     */
    public function setTag($tag)
    {
        return parent::setTag($tag);
    }

    /**
     * Sets an argument for the request.
     * 
     * @param string               $name  Name of the argument.
     * @param string|resource|null $value Value of the argument as a string or
     *     seekable stream.
     *     Setting the value to NULL removes an argument of this name.
     *     If a seekable stream is provided, it is sent from its current
     *     posistion to its end, and the pointer is seeked back to its current
     *     position after sending.
     *     Non seekable streams, as well as all other types, are casted to a
     *     string.
     * 
     * @return $this The request object.
     * @see getArgument()
     */
    public function setArgument($name, $value = '')
    {
        return parent::setAttribute($name, $value);
    }

    /**
     * Gets the value of an argument.
     * 
     * @param string $name The name of the argument.
     * 
     * @return string|resource|null The value of the specified argument.
     *     Returns NULL if such an argument is not set.
     * @see setAttribute()
     */
    public function getArgument($name)
    {
        return parent::getAttribute($name);
    }

    /**
     * Removes all arguments from the request.
     * 
     * @return $this The request object.
     */
    public function removeAllArguments()
    {
        return parent::removeAllAttributes();
    }

    /**
     * Sends a request over a communicator.
     * 
     * @param Communicator $com The communicator to send the request over.
     * @param Registry     $reg An optional registry to sync the request with.
     * 
     * @return int The number of bytes sent.
     * @see Client::sendSync()
     * @see Client::sendAsync()
     */
    public function send(Communicator $com, Registry $reg = null)
    {
        if (null !== $reg
            && (null != $this->getTag() || !$reg->isTaglessModeOwner())
        ) {
            $originalTag = $this->getTag();
            $this->setTag($reg->getOwnershipTag() . $originalTag);
            $bytes = $this->send($com);
            $this->setTag($originalTag);
            return $bytes;
        }
        if ($com->getTransmitter()->isPersistent()) {
            $old = $com->getTransmitter()->lock(T\Stream::DIRECTION_SEND);
            $bytes = $this->_send($com);
            $com->getTransmitter()->lock($old, true);
            return $bytes;
        }
        return $this->_send($com);
    }

    /**
     * Sends a request over a communicator.
     * 
     * The only difference with the non private equivalent is that this one does
     * not do locking.
     * 
     * @param Communicator $com The communicator to send the request over.
     * 
     * @return int The number of bytes sent.
     * @see Client::sendSync()
     * @see Client::sendAsync()
     */
    private function _send(Communicator $com)
    {
        if (!$com->getTransmitter()->isAcceptingData()) {
            throw new SocketException(
                'Transmitter is invalid. Sending aborted.',
                SocketException::CODE_REQUEST_SEND_FAIL
            );
        }
        $bytes = 0;
        $bytes += $com->sendWord($this->getCommand());
        if (null !== ($tag = $this->getTag())) {
            $bytes += $com->sendWord('.tag=' . $tag);
        }
        foreach ($this->attributes as $name => $value) {
            $prefix = '=' . $name . '=';
            if (is_string($value)) {
                $bytes += $com->sendWord($prefix . $value);
            } else {
                $bytes += $com->sendWordFromStream($prefix, $value);
            }
        }
        $query = $this->getQuery();
        if ($query instanceof Query) {
            $bytes += $query->send($com);
        }
        $bytes += $com->sendWord('');
        return $bytes;
    }
    
    /**
     * Parses the arguments of a command.
     * 
     * @param string $string The argument string to parse.
     * 
     * @return void
     */
    protected function parseArgumentString($string)
    {
        /*
         * Grammar:
         * 
         * <arguments> := (<<\s+>>, <argument>)*,
         * <argument> := <name>, <value>?
         * <name> := <<[^\=\s]+>>
         * <value> := "=", (<quoted string> | <unquoted string>)
         * <quotedString> := <<">>, <<([^"]|\\"|\\\\)*>>, <<">>
         * <unquotedString> := <<\S+>>
         */
        
        $token = '';
        $name = null;
        while ($string = substr($string, strlen($token))) {
            if (null === $name) {
                if (preg_match('/^\s+([^\s=]+)/sS', $string, $matches)) {
                    $token = $matches[0];
                    $name = $matches[1];
                } else {
                    throw new InvalidArgumentException(
                        "Parsing of argument name failed near '{$string}'",
                        InvalidArgumentException::CODE_NAME_UNPARSABLE
                    );
                }
            } elseif (preg_match('/^\s/s', $string, $matches)) {
                //Empty argument
                $token = '';
                $this->setArgument($name);
                $name = null;
            } elseif (preg_match(
                '/^="(([^\\\"]|\\\"|\\\\)*)"/sS',
                $string,
                $matches
            )) {
                $token = $matches[0];
                $this->setArgument(
                    $name,
                    str_replace(
                        array('\\"', '\\\\'),
                        array('"', '\\'),
                        $matches[1]
                    )
                );
                $name = null;
            } elseif (preg_match('/^=(\S+)/sS', $string, $matches)) {
                $token = $matches[0];
                $this->setArgument($name, $matches[1]);
                $name = null;
            } else {
                throw new InvalidArgumentException(
                    "Parsing of argument value failed near '{$string}'",
                    InvalidArgumentException::CODE_VALUE_UNPARSABLE
                );
            }
        }
        
        if (null !== $name && ('' !== ($name = trim($name)))) {
            $this->setArgument($name, '');
        }
        
    }
}


File: /PEAR2\Net\RouterOS\Response.php
<?php

/**
 * RouterOS API client implementation.
 * 
 * RouterOS is the flag product of the company MikroTik and is a powerful router software. One of its many abilities is to allow control over it via an API. This package provides a client for that API, in turn allowing you to use PHP to control RouterOS hosts.
 * 
 * PHP version 5
 * 
 * @category  Net
 * @package   PEAR2_Net_RouterOS
 * @author    Vasil Rangelov <boen.robot@gmail.com>
 * @copyright 2011 Vasil Rangelov
 * @license   http://www.gnu.org/copyleft/lesser.html LGPL License 2.1
 * @version   1.0.0b5
 * @link      http://pear2.php.net/PEAR2_Net_RouterOS
 */
/**
 * The namespace declaration.
 */
namespace PEAR2\Net\RouterOS;

/**
 * Refers to transmitter direction constants.
 */
use PEAR2\Net\Transmitter as T;

/**
 * Locks are released upon any exception from anywhere.
 */
use Exception as E;

/**
 * Represents a RouterOS response.
 * 
 * @category Net
 * @package  PEAR2_Net_RouterOS
 * @author   Vasil Rangelov <boen.robot@gmail.com>
 * @license  http://www.gnu.org/copyleft/lesser.html LGPL License 2.1
 * @link     http://pear2.php.net/PEAR2_Net_RouterOS
 */
class Response extends Message
{
    
    /**
     * The last response for a request.
     */
    const TYPE_FINAL = '!done';
    
    /**
     * A response with data.
     */
    const TYPE_DATA = '!re';
    
    /**
     * A response signifying error.
     */
    const TYPE_ERROR = '!trap';
    
    /**
     * A response signifying a fatal error, due to which the connection would be
     * terminated.
     */
    const TYPE_FATAL = '!fatal';

    /**
     * @var array An array of unrecognized words in network order.
     */
    protected $unrecognizedWords = array();

    /**
     * @var string The response type.
     */
    private $_type;

    /**
     * Extracts a new response from a communicator.
     * 
     * @param Communicator $com       The communicator from which to extract
     *     the new response.
     * @param bool         $asStream  Whether to populate the argument values
     *     with streams instead of strings.
     * @param int          $sTimeout  If a response is not immediatly
     *     available, wait this many seconds. If NULL, wait indefinetly.
     * @param int          $usTimeout Microseconds to add to the waiting time.
     * @param Registry     $reg       An optional registry to sync the
     *     response with.
     * 
     * @see getType()
     * @see getArgument()
     */
    public function __construct(
        Communicator $com,
        $asStream = false,
        $sTimeout = 0,
        $usTimeout = null,
        Registry $reg = null
    ) {
        if (null === $reg) {
            if ($com->getTransmitter()->isPersistent()) {
                $old = $com->getTransmitter()
                    ->lock(T\Stream::DIRECTION_RECEIVE);
                try {
                    $this->_receive($com, $asStream, $sTimeout, $usTimeout);
                } catch (E $e) {
                    $com->getTransmitter()->lock($old, true);
                    throw $e;
                }
                $com->getTransmitter()->lock($old, true);
            } else {
                $this->_receive($com, $asStream, $sTimeout, $usTimeout);
            }
        } else {
            while (null === ($response = $reg->getNextResponse())) {
                $newResponse = new self($com, true, $sTimeout, $usTimeout);
                $tagInfo = $reg::parseTag($newResponse->getTag());
                $newResponse->setTag($tagInfo[1]);
                if (!$reg->add($newResponse, $tagInfo[0])) {
                    $response = $newResponse;
                    break;
                }
            }
            
            $this->_type = $response->_type;
            $this->attributes = $response->attributes;
            $this->unrecognizedWords = $response->unrecognizedWords;
            $this->setTag($response->getTag());
            
            if (!$asStream) {
                foreach ($this->attributes as $name => $value) {
                    $this->setAttribute(
                        $name,
                        stream_get_contents($value)
                    );
                }
                foreach ($response->unrecognizedWords as $i => $value) {
                    $this->unrecognizedWords[$i] = stream_get_contents($value);
                }
            }
        }
    }
    
    /**
     * Extracts a new response from a communicator.
     * 
     * This is the function that performs the actual receiving, while the
     * constructor is also involved in locks and registry sync.
     * 
     * @param Communicator $com       The communicator from which to extract
     *     the new response.
     * @param bool         $asStream  Whether to populate the argument values
     *     with streams instead of strings.
     * @param int          $sTimeout  If a response is not immediatly
     *     available, wait this many seconds. If NULL, wait indefinetly.
     *     Note that if an empty sentence is received, the timeout will be
     *     reset for another sentence receiving.
     * @param int          $usTimeout Microseconds to add to the waiting time.
     * 
     * @return void
     */
    private function _receive(
        Communicator $com,
        $asStream = false,
        $sTimeout = 0,
        $usTimeout = null
    ) {
        do {
            if (!$com->getTransmitter()->isDataAwaiting(
                $sTimeout,
                $usTimeout
            )) {
                throw new SocketException(
                    'No data within the time limit',
                    SocketException::CODE_NO_DATA
                );
            }
            $type = $com->getNextWord();
        } while ('' === $type);
        $this->setType($type);
        if ($asStream) {
            for ($word = $com->getNextWordAsStream(), fseek($word, 0, SEEK_END);
                ftell($word) !== 0;
                $word = $com->getNextWordAsStream(), fseek(
                    $word,
                    0,
                    SEEK_END
                )) {
                rewind($word);
                $ind = fread($word, 1);
                if ('=' === $ind || '.' === $ind) {
                    $prefix = stream_get_line($word, null, '=');
                }
                if ('=' === $ind) {
                    $value = fopen('php://temp', 'r+b');
                    $bytesCopied = ftell($word);
                    while (!feof($word)) {
                        $bytesCopied += stream_copy_to_stream(
                            $word,
                            $value,
                            0xFFFFF,
                            $bytesCopied
                        );
                    }
                    rewind($value);
                    $this->setAttribute($prefix, $value);
                    continue;
                }
                if ('.' === $ind && 'tag' === $prefix) {
                    $this->setTag(stream_get_contents($word, -1, -1));
                    continue;
                }
                rewind($word);
                $this->unrecognizedWords[] = $word;
            }
        } else {
            for ($word = $com->getNextWord(); '' !== $word;
                $word = $com->getNextWord()) {
                if (preg_match('/^=([^=]+)=(.*)$/sS', $word, $matches)) {
                    $this->setAttribute($matches[1], $matches[2]);
                } elseif (preg_match('/^\.tag=(.*)$/sS', $word, $matches)) {
                    $this->setTag($matches[1]);
                } else {
                    $this->unrecognizedWords[] = $word;
                }
            }
        }
    }

    /**
     * Sets the response type.
     * 
     * Sets the response type. Valid values are the TYPE_* constants.
     * 
     * @param string $type The new response type.
     * 
     * @return $this The response object.
     * @see getType()
     */
    protected function setType($type)
    {
        switch ($type) {
        case self::TYPE_FINAL:
        case self::TYPE_DATA:
        case self::TYPE_ERROR:
        case self::TYPE_FATAL:
            $this->_type = $type;
            return $this;
        default:
            throw new UnexpectedValueException(
                'Unrecognized response type.',
                UnexpectedValueException::CODE_RESPONSE_TYPE_UNKNOWN,
                null,
                $type
            );
        }
    }

    /**
     * Gets the response type.
     * 
     * @return string The response type.
     * @see setType()
     */
    public function getType()
    {
        return $this->_type;
    }

    /**
     * Gets the value of an argument.
     * 
     * @param string $name The name of the argument.
     * 
     * @return string|resource|null The value of the specified argument.
     *     Returns NULL if such an argument is not set.
     * @deprecated 1.0.0b5 Use {@link static::getProperty()} instead.
     *     This method will be removed upon final release, and is currently
     *     left standing merely because it can't be easily search&replaced in
     *     existing code, due to the fact the name "getArgument()" is shared
     *     with {@link Request::getArgument()}, which is still valid.
     * @codeCoverageIgnore
     */
    public function getArgument($name)
    {
        trigger_error(
            'Response::getArgument() is deprecated in favor of ' .
            'Response::getProperty() (but note that Request::getArgument() ' .
            'is still valid)',
            E_USER_DEPRECATED
        );
        return $this->getAttribute($name);
    }

    /**
     * Gets the value of a property.
     * 
     * @param string $name The name of the property.
     * 
     * @return string|resource|null The value of the specified property.
     *     Returns NULL if such a property is not set.
     */
    public function getProperty($name)
    {
        return parent::getAttribute($name);
    }

    /**
     * Gets a list of unrecognized words.
     * 
     * @return array The list of unrecognized words.
     */
    public function getUnrecognizedWords()
    {
        return $this->unrecognizedWords;
    }

    /**
     * Counts the number of arguments or words.
     * 
     * @param int $mode The counter mode.
     *     Either COUNT_NORMAL or COUNT_RECURSIVE.
     *     When in normal mode, counts the number of arguments.
     *     When in recursive mode, counts the number of API words.
     * 
     * @return int The number of arguments/words.
     */
    public function count($mode = COUNT_NORMAL)
    {
        $result = parent::count($mode);
        if ($mode !== COUNT_NORMAL) {
            $result += count($this->unrecognizedWords);
        }
        return $result;
    }
}


File: /PEAR2\Net\RouterOS\ResponseCollection.php
<?php

/**
 * RouterOS API client implementation.
 * 
 * RouterOS is the flag product of the company MikroTik and is a powerful router software. One of its many abilities is to allow control over it via an API. This package provides a client for that API, in turn allowing you to use PHP to control RouterOS hosts.
 * 
 * PHP version 5
 * 
 * @category  Net
 * @package   PEAR2_Net_RouterOS
 * @author    Vasil Rangelov <boen.robot@gmail.com>
 * @copyright 2011 Vasil Rangelov
 * @license   http://www.gnu.org/copyleft/lesser.html LGPL License 2.1
 * @version   1.0.0b5
 * @link      http://pear2.php.net/PEAR2_Net_RouterOS
 */
/**
 * The namespace declaration.
 */
namespace PEAR2\Net\RouterOS;

/**
 * Implemented by this class.
 */
use ArrayAccess;

/**
 * Implemented by this class.
 */
use Countable;

/**
 * Implemented by this class.
 */
use SeekableIterator;

/**
 * Represents a collection of RouterOS responses.
 * 
 * @category Net
 * @package  PEAR2_Net_RouterOS
 * @author   Vasil Rangelov <boen.robot@gmail.com>
 * @license  http://www.gnu.org/copyleft/lesser.html LGPL License 2.1
 * @link     http://pear2.php.net/PEAR2_Net_RouterOS
 * 
 * @method string getType()
 *     Calls {@link Response::getType()}
 *     on the response pointed by the pointer.
 * @method string[] getUnrecognizedWords()
 *     Calls {@link Response::getUnrecognizedWords()}
 *     on the response pointed by the pointer.
 * @method string|resource|null getProperty(string $name)
 *     Calls {@link Response::getProperty()}
 *     on the response pointed by the pointer.
 * @method string getTag()
 *     Calls {@link Response::getTag()}
 *     on the response pointed by the pointer.
 */
class ResponseCollection implements ArrayAccess, SeekableIterator, Countable
{
    
    /**
     * @var array An array with all {@link Response} objects.
     */
    protected $responses = array();
    
    /**
     * @var array An array with each {@link Response} object's type.
     */
    protected $responseTypes = array();
    
    /**
     * @var array An array with each {@link Response} object's tag.
     */
    protected $responseTags = array();

    /**
     * @var array An array with positions of responses, based on an property
     *     name. The name of each property is the array key, and the array value
     *     is another array where the key is the value for that property, and
     *     the value is the posistion of the response. For performance reasons,
     *     each key is built only when {@link static::setIndex()} is called with
     *     that property, and remains available for the lifetime of this
     *     collection.
     */
    protected $responsesIndex = array();
    
    /**
     * @var array An array with all distinct properties across all
     *     {@link Response} objects. Created at the first call of
     *     {@link static::getPropertyMap()}.
     */
    protected $propertyMap = null;
    
    /**
     * @var int A pointer, as required by SeekableIterator.
     */
    protected $position = 0;

    /**
     * @var string|null Name of property to use as index. NULL when disabled.
     */
    protected $index = null;

    /**
     * @var array Criterias used by {@link compare()} to determine the order
     *     between two respones. See {@link orderBy()} for a detailed
     *     description of this array's format.
     */
    protected $compareBy = array();
    
    /**
     * Creates a new collection.
     * 
     * @param array $responses An array of responses, in network order.
     */
    public function __construct(array $responses)
    {
        $pos = 0;
        foreach ($responses as $response) {
            if ($response instanceof Response) {
                $this->responseTypes[$pos] = $response->getType();
                $this->responseTags[$pos] = $response->getTag();
                $this->responses[$pos++] = $response;
            }
        }
    }

    /**
     * A shorthand gateway.
     * 
     * This is a magic PHP method that allows you to call the object as a
     * function. Depending on the argument given, one of the other functions in
     * the class is invoked and its returned value is returned by this function.
     * 
     * @param int|string|null $offset The offset of the response to seek to.
     *     If the offset is negative, seek to that relative to the end.
     *     If the collection is indexed, you can also supply a value to seek to.
     *     Setting NULL will get the current response's interator.
     * 
     * @return Response|ArrayObject The {@link Response} at the specified
     *     offset, the current response's iterator (which is an ArrayObject)
     *     when NULL is given, or FALSE if the offset is invalid
     *     or the collection is empty.
     */
    public function __invoke($offset = null)
    {
        return null === $offset
            ? $this->current()->getIterator()
            : $this->seek($offset);
    }

    /**
     * Sets a property to be usable as a key in the collection.
     * 
     * @param string|null $name The name of the property to use. Future calls
     *     that accept a position will then also be able to search values of
     *     that property for a matching value.
     *     Specifying NULL will disable such lookups (as is by default).
     *     Note that in case this value occures multiple times within the
     *     collection, only the last matching response will be accessible by
     *     that value.
     * 
     * @return $this The object itself.
     */
    public function setIndex($name)
    {
        if (null !== $name) {
            $name = (string)$name;
            if (!isset($this->responsesIndex[$name])) {
                $this->responsesIndex[$name] = array();
                foreach ($this->responses as $pos => $response) {
                    $val = $response->getProperty($name);
                    if (null !== $val) {
                        $this->responsesIndex[$name][$val] = $pos;
                    }
                }
            }
        }
        $this->index = $name;
        return $this;
    }

    /**
     * Gets the name of the property used as an index.
     * 
     * @return string|null Name of property used as index. NULL when disabled.
     */
    public function getIndex()
    {
        return $this->index;
    }

    /**
     * Gets the whole collection as an array.
     * 
     * @param bool $useIndex Whether to use the index values as keys for the
     *     resulting array.
     * 
     * @return array An array with all responses, in network order.
     */
    public function toArray($useIndex = false)
    {
        if ($useIndex) {
            $positions = $this->responsesIndex[$this->index];
            asort($positions, SORT_NUMERIC);
            $positions = array_flip($positions);
            return array_combine(
                $positions,
                array_intersect_key($this->responses, $positions)
            );
        }
        return $this->responses;
    }

    /**
     * Counts the responses/words in the collection.
     * 
     * @param int $mode The counter mode.
     *     Either COUNT_NORMAL or COUNT_RECURSIVE.
     *     When in normal mode, counts the number of responses.
     *     When in recursive mode, counts the total number of API words.
     * 
     * @return int The number of responses in the collection.
     */
    public function count($mode = COUNT_NORMAL)
    {
        if ($mode !== COUNT_NORMAL) {
            $result = 0;
            foreach ($this->responses as $response) {
                $result += $response->count($mode);
            }
            return $result;
        } else {
            return count($this->responses);
        }
    }

    /**
     * Checks if an offset exists.
     * 
     * @param int|string $offset The offset to check. If the
     *     collection is indexed, you can also supply a value to check.
     *     Note that negative numeric offsets are NOT accepted.
     * 
     * @return bool TRUE if the offset exists, FALSE otherwise.
     */
    public function offsetExists($offset)
    {
        return is_int($offset)
            ? array_key_exists($offset, $this->responses)
            : array_key_exists($offset, $this->responsesIndex[$this->index]);
    }

    /**
     * Gets a {@link Response} from a specified offset.
     * 
     * @param int|string $offset The offset of the desired response. If the
     *     collection is indexed, you can also supply the value to search for.
     * 
     * @return Response The response at the specified offset.
     */
    public function offsetGet($offset)
    {
        return is_int($offset)
            ? $this->responses[$offset >= 0
            ? $offset
            : count($this->responses) + $offset]
            : $this->responses[$this->responsesIndex[$this->index][$offset]];
    }

    /**
     * N/A
     * 
     * This method exists only because it is required for ArrayAccess. The
     * collection is read only.
     * 
     * @param int|string $offset N/A
     * @param Response   $value  N/A
     * 
     * @return void
     * @SuppressWarnings(PHPMD.UnusedFormalParameter)
     */
    public function offsetSet($offset, $value)
    {
        
    }

    /**
     * N/A
     * 
     * This method exists only because it is required for ArrayAccess. The
     * collection is read only.
     * 
     * @param int|string $offset N/A
     * 
     * @return void
     * @SuppressWarnings(PHPMD.UnusedFormalParameter)
     */
    public function offsetUnset($offset)
    {
        
    }

    /**
     * Resets the pointer to 0, and returns the first response.
     * 
     * @return Response The first response in the collection, or FALSE if the
     *     collection is empty.
     */
    public function rewind()
    {
        return $this->seek(0);
    }

    /**
     * Moves the position pointer to a specified position.
     * 
     * @param int|string $position The position to move to. If the collection is
     *     indexed, you can also supply a value to move the pointer to.
     *     A non-existent index will move the pointer to "-1".
     * 
     * @return Response The {@link Response} at the specified position, or FALSE
     *     if the specified position is not valid.
     */
    public function seek($position)
    {
        $this->position = is_int($position)
            ? ($position >= 0
            ? $position
            : count($this->responses) + $position)
            : ($this->offsetExists($position)
            ? $this->responsesIndex[$this->index][$position]
            : -1);
        return $this->current();
    }

    /**
     * Moves the pointer forward by 1, and gets the next response.
     * 
     * @return Response The next {@link Response} object, or FALSE if the
     *     position is not valid.
     */
    public function next()
    {
        ++$this->position;
        return $this->current();
    }

    /**
     * Gets the response at the current pointer position.
     * 
     * @return Response The response at the current pointer position, or FALSE
     *     if the position is not valid.
     */
    public function current()
    {
        return $this->valid() ? $this->responses[$this->position] : false;
    }

    /**
     * Moves the pointer backwards by 1, and gets the previous response.
     * 
     * @return Response The next {@link Response} object, or FALSE if the
     *     position is not valid.
     */
    public function prev()
    {
        --$this->position;
        return $this->current();
    }

    /**
     * Moves the pointer to the last valid position, and returns the last
     * response.
     * 
     * @return Response The last response in the collection, or FALSE if the
     *     collection is empty.
     */
    public function end()
    {
        $this->position = count($this->responses) - 1;
        return $this->current();
    }

    /**
     * Gets the key at the current pointer position.
     * 
     * @return int The key at the current pointer position, i.e. the pointer
     *     position itself, or FALSE if the position is not valid.
     */
    public function key()
    {
        return $this->valid() ? $this->position : false;
    }

    /**
     * Checks if the pointer is still pointing to an existing offset.
     * 
     * @return bool TRUE if the pointer is valid, FALSE otherwise.
     */
    public function valid()
    {
        return $this->offsetExists($this->position);
    }

    /**
     * Gets all distinct property names.
     * 
     * Gets all distinct property names across all responses.
     * 
     * @return array An array with all distinct property names as keys, and the
     *     indexes at which they occur as values.
     */
    public function getPropertyMap()
    {
        if (null === $this->propertyMap) {
            $properties = array();
            foreach ($this->responses as $index => $response) {
                $names = array_keys($response->getIterator()->getArrayCopy());
                foreach ($names as $name) {
                    if (!isset($properties[$name])) {
                        $properties[$name] = array();
                    }
                    $properties[$name][] = $index;
                }
            }
            $this->propertyMap = $properties;
        }
        return $this->propertyMap;
    }

    /**
     * Gets all responses of a specified type.
     * 
     * @param string $type The response type to filter by. Valid values are the
     *     Response::TYPE_* constants.
     * 
     * @return static A new collection with responses of the
     *     specified type.
     */
    public function getAllOfType($type)
    {
        $result = array();
        foreach (array_keys($this->responseTypes, $type, true) as $index) {
            $result[] = $this->responses[$index];
        }
        return new static($result);
    }

    /**
     * Gets all responses with a specified tag.
     * 
     * @param string $tag The tag to filter by.
     * 
     * @return static A new collection with responses having the
     *     specified tag.
     */
    public function getAllTagged($tag)
    {
        $result = array();
        foreach (array_keys($this->responseTags, $tag, true) as $index) {
            $result[] = $this->responses[$index];
        }
        return new static($result);
    }

    /**
     * Order resones by criteria.
     * 
     * @param mixed[] $criteria The criteria to order respones by. It takes the
     *     form of an array where each key is the name of the property to use
     *     as (N+1)th sorting key. The value of each member can be either NULL
     *     (for that property, sort normally in ascending order), a single sort
     *     order constant (SORT_ASC or SORT_DESC) to sort normally in the
     *     specified order, an array where the first member is an order
     *     constant, and the second one is sorting flags (same as built in PHP
     *     array functions) or a callback.
     *     If a callback is provided, it must accept two arguments
     *     (the two values to be compared), and return -1, 0 or 1 if the first
     *     value is respectively less than, equal to or greather than the second
     *     one.
     *     Each key of $criteria can also be numeric, in which case the
     *     value is the name of the property, and sorting is done normally in
     *     ascending order.
     * 
     * @return static A new collection with the responses sorted in the
     *     specified order.
     */
    public function orderBy(array $criteria)
    {
        $this->compareBy = $criteria;
        $sortedResponses = $this->responses;
        usort($sortedResponses, array($this, 'compare'));
        return new static($sortedResponses);
    }

    /**
     * Calls a method of the response pointed by the pointer.
     * 
     * Calls a method of the response pointed by the pointer. This is a magic
     * PHP method, thanks to which any function you call on the collection that
     * is not defined will be redirected to the response.
     * 
     * @param string $method The name of the method to call.
     * @param array  $args   The arguments to pass to the method.
     * 
     * @return mixed Whatever the called function returns.
     */
    public function __call($method, array $args)
    {
        return call_user_func_array(
            array($this->current(), $method),
            $args
        );
    }

    /**
     * Compares two respones.
     * 
     * Compares two respones, based on criteria defined in
     * {@link static::$compareBy}.
     * 
     * @param Response $itemA The response to compare.
     * @param Response $itemB The response to compare $a against.
     * 
     * @return int Returns 0 if the two respones are equal according to every
     *     criteria specified, -1 if $a should be placed before $b, and 1 if $b
     *     should be placed before $a.
     */
    protected function compare(Response $itemA, Response $itemB)
    {
        foreach ($this->compareBy as $name => $spec) {
            if (!is_string($name)) {
                $name = $spec;
                $spec = null;
            }

            $members = array(
                0 => $itemA->getProperty($name),
                1 => $itemB->getProperty($name)
            );

            if (is_callable($spec)) {
                uasort($members, $spec);
            } elseif ($members[0] === $members[1]) {
                continue;
            } else {
                $flags = SORT_REGULAR;
                $order = SORT_ASC;
                if (is_array($spec)) {
                    list($order, $flags) = $spec;
                } elseif (null !== $spec) {
                    $order = $spec;
                }

                if (SORT_ASC === $order) {
                    asort($members, $flags);
                } else {
                    arsort($members, $flags);
                }
            }
            return (key($members) === 0) ? -1 : 1;
        }

        return 0;
    }
}


File: /PEAR2\Net\RouterOS\SocketException.php
<?php

/**
 * RouterOS API client implementation.
 * 
 * RouterOS is the flag product of the company MikroTik and is a powerful router software. One of its many abilities is to allow control over it via an API. This package provides a client for that API, in turn allowing you to use PHP to control RouterOS hosts.
 * 
 * PHP version 5
 * 
 * @category  Net
 * @package   PEAR2_Net_RouterOS
 * @author    Vasil Rangelov <boen.robot@gmail.com>
 * @copyright 2011 Vasil Rangelov
 * @license   http://www.gnu.org/copyleft/lesser.html LGPL License 2.1
 * @version   1.0.0b5
 * @link      http://pear2.php.net/PEAR2_Net_RouterOS
 */
/**
 * The namespace declaration.
 */
namespace PEAR2\Net\RouterOS;

/**
 * Base of this class.
 */
use RuntimeException;

/**
 * Exception thrown when something goes wrong with the connection.
 * 
 * @category Net
 * @package  PEAR2_Net_RouterOS
 * @author   Vasil Rangelov <boen.robot@gmail.com>
 * @license  http://www.gnu.org/copyleft/lesser.html LGPL License 2.1
 * @link     http://pear2.php.net/PEAR2_Net_RouterOS
 */
class SocketException extends RuntimeException implements Exception
{
    const CODE_SERVICE_INCOMPATIBLE = 10200;
    const CODE_CONNECTION_FAIL = 100;
    const CODE_QUERY_SEND_FAIL = 30600;
    const CODE_REQUEST_SEND_FAIL = 40900;
    const CODE_NO_DATA = 50000;
}


File: /PEAR2\Net\RouterOS\UnexpectedValueException.php
<?php

/**
 * RouterOS API client implementation.
 * 
 * RouterOS is the flag product of the company MikroTik and is a powerful router software. One of its many abilities is to allow control over it via an API. This package provides a client for that API, in turn allowing you to use PHP to control RouterOS hosts.
 * 
 * PHP version 5
 * 
 * @category  Net
 * @package   PEAR2_Net_RouterOS
 * @author    Vasil Rangelov <boen.robot@gmail.com>
 * @copyright 2011 Vasil Rangelov
 * @license   http://www.gnu.org/copyleft/lesser.html LGPL License 2.1
 * @version   1.0.0b5
 * @link      http://pear2.php.net/PEAR2_Net_RouterOS
 */
/**
 * The namespace declaration.
 */
namespace PEAR2\Net\RouterOS;

use UnexpectedValueException as U;

/**
 * Exception thrown when encountering an invalid value in a function argument.
 * 
 * @category Net
 * @package  PEAR2_Net_RouterOS
 * @author   Vasil Rangelov <boen.robot@gmail.com>
 * @license  http://www.gnu.org/copyleft/lesser.html LGPL License 2.1
 * @link     http://pear2.php.net/PEAR2_Net_RouterOS
 */
class UnexpectedValueException extends U implements Exception
{
    const CODE_CALLBACK_INVALID = 10502;
    const CODE_ACTION_UNKNOWN = 30100;
    const CODE_RESPONSE_TYPE_UNKNOWN = 50100;

    /**
     * @var mixed The unexpected value.
     */
    private $_value;

    /**
     * Creates a new UnexpectedValueException.
     * 
     * @param string     $message  The Exception message to throw.
     * @param int        $code     The Exception code.
     * @param \Exception $previous The previous exception used for the exception
     *     chaining.
     * @param mixed      $value    The unexpected value.
     */
    public function __construct(
        $message,
        $code = 0,
        $previous = null,
        $value = null
    ) {
        parent::__construct($message, $code, $previous);
        $this->_value = $value;
    }

    /**
     * Gets the unexpected value.
     * 
     * @return mixed The unexpected value.
     */
    public function getValue()
    {
        return $this->_value;
    }

    // @codeCoverageIgnoreStart
    // String representation is not reliable in testing

    /**
     * Returns a string representation of the exception.
     * 
     * @return string The exception as a string.
     */
    public function __toString()
    {
        return parent::__toString() . "\nValue:{$this->_value}";
    }

    // @codeCoverageIgnoreEnd
}


File: /PEAR2\Net\RouterOS\Util.php
<?php

/**
 * RouterOS API client implementation.
 * 
 * RouterOS is the flag product of the company MikroTik and is a powerful router software. One of its many abilities is to allow control over it via an API. This package provides a client for that API, in turn allowing you to use PHP to control RouterOS hosts.
 * 
 * PHP version 5
 * 
 * @category  Net
 * @package   PEAR2_Net_RouterOS
 * @author    Vasil Rangelov <boen.robot@gmail.com>
 * @copyright 2011 Vasil Rangelov
 * @license   http://www.gnu.org/copyleft/lesser.html LGPL License 2.1
 * @version   1.0.0b5
 * @link      http://pear2.php.net/PEAR2_Net_RouterOS
 */
/**
 * The namespace declaration.
 */
namespace PEAR2\Net\RouterOS;

/**
 * Values at {@link Util::exec()} can be casted from this type.
 */
use DateTime;

/**
 * Values at {@link Util::exec()} can be casted from this type.
 */
use DateInterval;

/**
 * Implemented by this class.
 */
use Countable;

/**
 * Used to reliably write to streams at {@link static::prepareScript()}.
 */
use PEAR2\Net\Transmitter\Stream;

/**
 * Utility class.
 * 
 * Abstracts away frequently used functionality (particularly CRUD operations)
 * in convinient to use methods by wrapping around a connection.
 * 
 * @category Net
 * @package  PEAR2_Net_RouterOS
 * @author   Vasil Rangelov <boen.robot@gmail.com>
 * @license  http://www.gnu.org/copyleft/lesser.html LGPL License 2.1
 * @link     http://pear2.php.net/PEAR2_Net_RouterOS
 */
class Util implements Countable
{
    /**
     * @var Client The connection to wrap around.
     */
    protected $client;

    /**
     * @var string The current menu.
     */
    protected $menu = '/';

    /**
     * @var array|null An array with the numbers of items in the current menu as
     *     keys, and the corresponding IDs as values. NULL when the cache needs
     *     regenerating.
     */
    protected $idCache = null;

    /**
     * Parses a value from a RouterOS scripting context.
     * 
     * Turns a value from RouterOS into an equivalent PHP value, based on
     * determining the type in the same way RouterOS would determine it for a
     * literal.
     * 
     * This method is intended to be the very opposite of
     * {@link static::escapeValue()}. hat is, results from that method, if
     * given to this method, should produce equivalent results.
     * 
     * @param string $value The value to be parsed. Must be a literal of a
     *     value, e.g. what {@link static::escapeValue()} will give you.
     * 
     * @return mixed Depending on RouterOS type detected:
     *     - "nil" or "nothing" - NULL.
     *     - "number" - int or double for large values.
     *     - "bool" - a boolean.
     *     - "time" - a {@link DateInterval} object.
     *     - "array" - an array, with the values processed recursively.
     *     - "str" - a string.
     *     - Unrecognized type - treated as an unquoted string.
     */
    public static function parseValue($value)
    {
        $value = (string)$value;
        
        if (in_array($value, array('', 'nil'), true)) {
            return null;
        } elseif (in_array($value, array('true', 'false', 'yes', 'no'), true)) {
            return $value === 'true' || $value === 'yes';
        } elseif ($value === (string)($num = (int)$value)
            || $value === (string)($num = (double)$value)
        ) {
            return $num;
        } elseif (preg_match(
            '/^
               (?:(\d+)w)?
               (?:(\d+)d)?
               (?:(\d\d)\:)?
               (\d\d)\:
               (\d\d(:\.\d{1,6})?)
            $/x',
            $value,
            $time
        )) {
            $days = isset($time[2]) ? (int)$time[2] : 0;
            if (isset($time[1])) {
                $days += 7 * (int)$time[1];
            }
            if ('' === $time[3]) {
                $time[3] = 0;
            }
            return new DateInterval(
                "P{$days}DT{$time[3]}H{$time[4]}M{$time[5]}S"
            );
        } elseif (('"' === $value[0]) && substr(strrev($value), 0, 1) === '"') {
            return str_replace(
                array('\"', '\\\\', "\\\n", "\\\r\n", "\\\r"),
                array('"', '\\'),
                substr($value, 1, -1)
            );
        } elseif ('{' === $value[0]) {
            $len = strlen($value);
            if ($value[$len - 1] === '}') {
                $value = substr($value, 1, -1);
                if ('' === $value) {
                    return array();
                }
                $parsedValue = preg_split(
                    '/
                        (\"(?:\\\\\\\\|\\\\"|[^"])*\")
                        |
                        (\{[^{}]*(?2)?\})
                        |
                        ([^;=]+)
                    /sx',
                    $value,
                    null,
                    PREG_SPLIT_DELIM_CAPTURE
                );
                $result = array();
                $newVal = null;
                $newKey = null;
                for ($i = 0, $l = count($parsedValue); $i < $l; ++$i) {
                    switch ($parsedValue[$i]) {
                    case '':
                        break;
                    case ';':
                        if (null === $newKey) {
                            $result[] = $newVal;
                        } else {
                            $result[$newKey] = $newVal;
                        }
                        $newKey = $newVal = null;
                        break;
                    case '=':
                        $newKey = static::parseValue($parsedValue[$i - 1]);
                        $newVal = static::parseValue($parsedValue[++$i]);
                        break;
                    default:
                        $newVal = static::parseValue($parsedValue[$i]);
                    }
                }
                if (null === $newKey) {
                    $result[] = $newVal;
                } else {
                    $result[$newKey] = $newVal;
                }
                return $result;
            }
        }
        return $value;
    }

    /**
     * Prepares a script.
     * 
     * Prepares a script for eventual execution by prepending parameters as
     * variables to it.
     * 
     * This is particularly useful when you're creating scripts that you don't
     * want to execute right now (as with {@link static::exec()}, but instead
     * you want to store it for later execution, perhaps by supplying it to
     * "/system scheduler".
     * 
     * @param string|resource $source The source of the script, as a string
     *     or stream. If a stream is provided, reading starts from the current
     *     position to the end of the stream, and the pointer stays at the end
     *     after reading is done.
     * @param array           $params An array of parameters to make available
     *     in the script as local variables.
     *     Variable names are array keys, and variable values are array values.
     *     Array values are automatically processed with
     *     {@link static::escapeValue()}. Streams are also supported, and are
     *     processed in chunks, each with
     *     {@link static::escapeString()}. Processing starts from the current
     *     position to the end of the stream, and the stream's pointer stays at
     *     the end after reading is done.
     * 
     * @return resource A new PHP temporary stream with the script as contents,
     *     with the pointer back at the start.
     * @see static::appendScript()
     */
    public static function prepareScript(
        $source,
        array $params = array()
    ) {
        $resultStream = fopen('php://temp', 'r+b');
        self::appendScript($resultStream, $source, $params);
        rewind($resultStream);
        return $resultStream;
    }

    /**
     * Appends a script.
     * 
     * Appends a script to an existing stream.
     * 
     * @param resource        $stream An existing stream to write the resulting
     *     script to.
     * @param string|resource $source The source of the script, as a string
     *     or stream. If a stream is provided, reading starts from the current
     *     position to the end of the stream, and the pointer stays at the end
     *     after reading is done.
     * @param array           $params An array of parameters to make available
     *     in the script as local variables.
     *     Variable names are array keys, and variable values are array values.
     *     Array values are automatically processed with
     *     {@link static::escapeValue()}. Streams are also supported, and are
     *     processed in chunks, each with
     *     {@link static::escapeString()}. Processing starts from the current
     *     position to the end of the stream, and the stream's pointer stays at
     *     the end after reading is done.
     * 
     * @return int The number of bytes written to $stream is returned,
     *     and the pointer remains where it was after the write
     *     (i.e. it is not seeked back, even if seeking is supported).
     */
    public static function appendScript(
        $stream,
        $source,
        array $params = array()
    ) {
        $writer = new Stream($stream, false);
        $bytes = 0;

        foreach ($params as $pname => $pvalue) {
            $pname = static::escapeString($pname);
            $bytes += $writer->send(":local \"{$pname}\" ");
            if (Stream::isStream($pvalue)) {
                $reader = new Stream($pvalue, false);
                $chunkSize = $reader->getChunk(Stream::DIRECTION_RECEIVE);
                $bytes += $writer->send('"');
                while ($reader->isAvailable() && $reader->isDataAwaiting()) {
                    $bytes += $writer->send(
                        static::escapeString(fread($pvalue, $chunkSize))
                    );
                }
                $bytes += $writer->send("\";\n");
            } else {
                $bytes += $writer->send(static::escapeValue($pvalue) . ";\n");
            }
        }

        $bytes += $writer->send($source);
        return $bytes;
    }
    
    /**
     * Escapes a value for a RouterOS scripting context.
     * 
     * Turns any native PHP value into an equivalent whole value that can be
     * inserted as part of a RouterOS script.
     * 
     * DateTime and DateInterval objects will be casted to RouterOS' "time"
     * type. A DateTime object will be converted to a time relative to the UNIX
     * epoch time. Note that if a DateInterval does not have the "days" property
     * ("a" in formatting), then its months and years will be ignored, because
     * they can't be unambigiously converted to a "time" value.
     * 
     * Unrecognized types (i.e. resources and other objects) are casted to
     * strings.
     * 
     * @param mixed $value The value to be escaped.
     * 
     * @return string A string representation that can be directly inserted in a
     *     script as a whole value.
     */
    public static function escapeValue($value)
    {
        switch(gettype($value)) {
        case 'NULL':
            $value = '';
            break;
        case 'integer':
            $value = (string)$value;
            break;
        case 'boolean':
            $value = $value ? 'true' : 'false';
            break;
        case 'array':
            if (0 === count($value)) {
                $value = '({})';
                break;
            }
            $result = '';
            foreach ($value as $key => $val) {
                $result .= ';';
                if (!is_int($key)) {
                    $result .= static::escapeValue($key) . '=';
                }
                $result .= static::escapeValue($val);
            }
            $value = '{' . substr($result, 1) . '}';
            break;
        case 'object':
            if ($value instanceof DateTime) {
                $usec = $value->format('u');
                if ('000000' === $usec) {
                    unset($usec);
                }
                $unixEpoch = new DateTime('@0');
                $value = $unixEpoch->diff($value);
            }
            if ($value instanceof DateInterval) {
                if (false === $value->days || $value->days < 0) {
                    $value = $value->format('%r%dd%H:%I:%S');
                } else {
                    $value = $value->format('%r%ad%H:%I:%S');
                }
                if (strpos('.', $value) === false && isset($usec)) {
                    $value .= '.' . $usec;
                }
                break;
            }
            //break; intentionally omitted
        default:
            $value = '"' . static::escapeString((string)$value) . '"';
            break;
        }
        return $value;
    }

    /**
     * Escapes a string for a RouterOS scripting context.
     * 
     * Escapes a string for a RouterOS scripting context. The value can then be
     * surrounded with quotes at a RouterOS script (or concatenated onto a
     * larger string first), and you can be sure there won't be any code
     * injections coming from it.
     * 
     * @param string $value Value to be escaped.
     * 
     * @return string The escaped value.
     */
    public static function escapeString($value)
    {
        return preg_replace_callback(
            '/[^\\_A-Za-z0-9]+/S',
            array(__CLASS__, '_escapeCharacters'),
            $value
        );
    }
    
    /**
     * Escapes a character for a RouterOS scripting context.
     * 
     * Escapes a character for a RouterOS scripting context. Intended to only be
     * called for non-alphanumeric characters.
     * 
     * @param string $chars The matches array, expected to contain exactly one
     *     member, in which is the whole string to be escaped.
     * 
     * @return string The escaped characters.
     */
    private static function _escapeCharacters($chars)
    {
        $result = '';
        for ($i = 0, $l = strlen($chars[0]); $i < $l; ++$i) {
            $result .= '\\' . str_pad(
                strtoupper(dechex(ord($chars[0][$i]))),
                2,
                '0',
                STR_PAD_LEFT
            );
        }
        return $result;
    }

    /**
     * Creates a new Util instance.
     * 
     * Wraps around a connection to provide convinience methods.
     * 
     * @param Client $client The connection to wrap around.
     */
    public function __construct(Client $client)
    {
        $this->client = $client;
    }

    /**
     * Gets the current menu.
     * 
     * @return string The current menu.
     */
    public function getMenu()
    {
        return $this->menu;
    }
    
    /**
     * Sets the current menu.
     * 
     * Sets the current menu.
     * 
     * @param string $newMenu The menu to change to. Can be specified with API
     *     or CLI syntax and can be either absolute or relative. If relative,
     *     it's relative to the current menu, which by default is the root.
     * 
     * @return $this The object itself. If an empty string is given for
     *     a new menu, no change is performed,
     *     but the ID cache is cleared anyway.
     * 
     * @see static::clearIdCache()
     */
    public function setMenu($newMenu)
    {
        $newMenu = (string)$newMenu;
        if ('' !== $newMenu) {
            $menuRequest = new Request('/menu');
            if ('/' === $newMenu[0]) {
                $this->menu = $menuRequest->setCommand($newMenu)->getCommand();
            } else {
                $this->menu = $menuRequest->setCommand(
                    '/' . str_replace('/', ' ', substr($this->menu, 1)) . ' ' .
                    str_replace('/', ' ', $newMenu)
                )->getCommand();
            }
        }
        $this->clearIdCache();
        return $this;
    }

    /**
     * Executes a RouterOS script.
     * 
     * Executes a RouterOS script, written as a string or a stream.
     * Note that in cases of errors, the line numbers will be off, because the
     * script is executed at the current menu as context, with the specified
     * variables pre declared. This is achieved by prepending 1+count($params)
     * lines before your actual script.
     * 
     * @param string|resource $source The source of the script, as a string or
     *     stream. If a stream is provided, reading starts from the current
     *     position to the end of the stream, and the pointer stays at the end
     *     after reading is done.
     * @param array           $params An array of parameters to make available
     *     in the script as local variables.
     *     Variable names are array keys, and variable values are array values.
     *     Array values are automatically processed with
     *     {@link static::escapeValue()}. Streams are also supported, and are
     *     processed in chunks, each processed with
     *     {@link static::escapeString()}. Processing starts from the current
     *     position to the end of the stream, and the stream's pointer is left
     *     untouched after the reading is done.
     *     Note that the script's (generated) name is always added as the
     *     variable "_", which will be inadvertently lost if you overwrite it
     *     from here.
     * @param string          $policy Allows you to specify a policy the script
     *     must follow. Has the same format as in terminal.
     *     If left NULL, the script has no restrictions beyond those imposed by
     *     the username.
     * @param string          $name   The script is executed after being saved
     *     in "/system script" under a random name (prefixed with the computer's
     *     name), and is removed after execution. To eliminate any possibility
     *     of name clashes, you can specify your own name.
     * 
     * @return ResponseCollection Returns the response collection of the
     *     run, allowing you to inspect errors, if any.
     *     If the script was not added successfully before execution, the
     *     ResponseCollection from the add attempt is going to be returned.
     */
    public function exec(
        $source,
        array $params = array(),
        $policy = null,
        $name = null
    ) {
        return $this->_exec($source, $params, $policy, $name);
    }
    
    /**
     * Clears the ID cache.
     * 
     * Normally, the ID cache improves performance when targeting items by a
     * number. If you're using both Util's methods and other means (e.g.
     * {@link Client} or {@link Util::exec()}) to add/move/remove items, the
     * cache may end up being out of date. By calling this method right before
     * targeting an item with a number, you can ensure number accuracy.
     * 
     * Note that Util's {@link static::move()} and {@link static::remove()}
     * methods automatically clear the cache before returning, while
     * {@link static::add()} adds the new item's ID to the cache as the next
     * number. A change in the menu also clears the cache.
     * 
     * Note also that the cache is being rebuilt unconditionally every time you
     * use {@link static::find()} with a callback.
     * 
     * @return $this The Util object itself.
     */
    public function clearIdCache()
    {
        $this->idCache = null;
        return $this;
    }

    /**
     * Finds the IDs of items at the current menu.
     * 
     * Finds the IDs of items based on specified criteria, and returns them as
     * a comma separated string, ready for insertion at a "numbers" argument.
     * 
     * Accepts zero or more criteria as arguments. If zero arguments are
     * specified, returns all items' IDs. The value of each criteria can be a
     * number (just as in Winbox), a literal ID to be included, a {@link Query}
     * object, or a callback. If a callback is specified, it is called for each
     * item, with the item as an argument. If it returns a true value, the
     * item's ID is included in the result. Every other value is casted to a
     * string. A string is treated as a comma separated values of IDs, numbers
     * or callback names. Non-existent callback names are instead placed in the
     * result, which may be useful in menus that accept identifiers other than
     * IDs, but note that it can cause errors on other menus.
     * 
     * @return string A comma separated list of all items matching the
     *     specified criteria.
     */
    public function find()
    {
        if (func_num_args() === 0) {
            if (null === $this->idCache) {
                $idCache = str_replace(
                    ';',
                    ',',
                    $this->client->sendSync(
                        new Request($this->menu . '/find')
                    )->getProperty('ret')
                );
                $this->idCache = explode(',', $idCache);
                return $idCache;
            }
            return implode(',', $this->idCache);
        }
        $idList = '';
        foreach (func_get_args() as $criteria) {
            if ($criteria instanceof Query) {
                foreach ($this->client->sendSync(
                    new Request($this->menu . '/print .proplist=.id', $criteria)
                ) as $response) {
                    $idList .= $response->getProperty('.id') . ',';
                }
            } elseif (is_callable($criteria)) {
                $idCache = array();
                foreach ($this->client->sendSync(
                    new Request($this->menu . '/print')
                ) as $response) {
                    if ($criteria($response)) {
                        $idList .= $response->getProperty('.id') . ',';
                    }
                    $idCache[] = $response->getProperty('.id');
                }
                $this->idCache = $idCache;
            } else {
                $this->find();
                if (is_int($criteria)) {
                    if (isset($this->idCache[$criteria])) {
                        $idList = $this->idCache[$criteria] . ',';
                    }
                } else {
                    $criteria = (string)$criteria;
                    if ($criteria === (string)(int)$criteria) {
                        if (isset($this->idCache[(int)$criteria])) {
                            $idList .= $this->idCache[(int)$criteria] . ',';
                        }
                    } elseif (false === strpos($criteria, ',')) {
                        $idList .= $criteria . ',';
                    } else {
                        $criteriaArr = explode(',', $criteria);
                        for ($i = count($criteriaArr) - 1; $i >= 0; --$i) {
                            if ('' === $criteriaArr[$i]) {
                                unset($criteriaArr[$i]);
                            } elseif ('*' === $criteriaArr[$i][0]) {
                                $idList .= $criteriaArr[$i] . ',';
                                unset($criteriaArr[$i]);
                            }
                        }
                        if (!empty($criteriaArr)) {
                            $idList .= call_user_func_array(
                                array($this, 'find'),
                                $criteriaArr
                            ) . ',';
                        }
                    }
                }
            }
        }
        return rtrim($idList, ',');
    }

    /**
     * Gets a value of a specified item at the current menu.
     * 
     * @param int|string|null $number    A number identifying the item you're
     *     targeting. Can also be an ID or (in some menus) name. For menus where
     *     there are no items (e.g. "/system identity"), you can specify NULL.
     * @param string          $valueName The name of the value you want to get.
     * 
     * @return string|null|bool The value of the specified property. If the
     *     property is not set, NULL will be returned. FALSE on failure
     *     (e.g. no such item, invalid property, etc.).
     */
    public function get($number, $valueName)
    {
        if (is_int($number) || ((string)$number === (string)(int)$number)) {
            $this->find();
            if (isset($this->idCache[(int)$number])) {
                $number = $this->idCache[(int)$number];
            } else {
                return false;
            }
        }

        //For new RouterOS versions
        $request = new Request($this->menu . '/get');
        $request->setArgument('number', $number);
        $request->setArgument('value-name', $valueName);
        $responses = $this->client->sendSync($request);
        if (Response::TYPE_ERROR === $responses->getType()) {
            return false;
        }
        $result = $responses->getProperty('ret');
        if (null !== $result) {
            return $result;
        }

        // The "get" of old RouterOS versions returns an empty !done response.
        // New versions return such only when the property is not set.
        // This is a backup for old versions' sake.
        $query = null;
        if (null !== $number) {
            $number = (string)$number;
            $query = Query::where('.id', $number)->orWhere('name', $number);
        }
        $responses = $this->getAll(
            array('.proplist' => $valueName, 'detail'),
            $query
        );

        if (0 === count($responses)) {
            // @codeCoverageIgnoreStart
            // New versions of RouterOS can't possibly reach this section.
            return false;
            // @codeCoverageIgnoreEnd
        }
        return $responses->getProperty($valueName);
    }

    /**
     * Enables all items at the current menu matching certain criteria.
     * 
     * Zero or more arguments can be specified, each being a criteria.
     * If zero arguments are specified, enables all items.
     * See {@link static::find()} for a description of what criteria are
     * accepted.
     * 
     * @return ResponseCollection returns the response collection, allowing you
     *     to inspect errors, if any.
     */
    public function enable()
    {
        return $this->doBulk('enable', func_get_args());
    }

    /**
     * Disables all items at the current menu matching certain criteria.
     * 
     * Zero or more arguments can be specified, each being a criteria.
     * If zero arguments are specified, disables all items.
     * See {@link static::find()} for a description of what criteria are
     * accepted.
     * 
     * @return ResponseCollection Returns the response collection, allowing you
     *     to inspect errors, if any.
     */
    public function disable()
    {
        return $this->doBulk('disable', func_get_args());
    }

    /**
     * Removes all items at the current menu matching certain criteria.
     * 
     * Zero or more arguments can be specified, each being a criteria.
     * If zero arguments are specified, removes all items.
     * See {@link static::find()} for a description of what criteria are
     * accepted.
     * 
     * @return ResponseCollection Returns the response collection, allowing you
     *     to inspect errors, if any.
     */
    public function remove()
    {
        $result = $this->doBulk('remove', func_get_args());
        $this->clearIdCache();
        return $result;
    }

    /**
     * Sets new values.
     * 
     * Sets new values on certain properties on all items at the current menu
     * which match certain criteria.
     * 
     * @param mixed $numbers   Targeted items. Can be any criteria accepted by
     *     {@link static::find()} or NULL in case the menu is one without items
     *     (e.g. "/system identity").
     * @param array $newValues An array with the names of each property to set
     *     as an array key, and the new value as an array value.
     *     Flags (properties with a value "true" that is interpreted as
     *     equivalent of "yes" from CLI) can also be specified with a numeric
     *     index as the array key, and the name of the flag as the array value.
     * 
     * @return ResponseCollection Returns the response collection, allowing you
     *     to inspect errors, if any.
     */
    public function set($numbers, array $newValues)
    {
        $setRequest = new Request($this->menu . '/set');
        foreach ($newValues as $name => $value) {
            if (is_int($name)) {
                $setRequest->setArgument($value, 'true');
            } else {
                $setRequest->setArgument($name, $value);
            }
        }
        if (null !== $numbers) {
            $setRequest->setArgument('numbers', $this->find($numbers));
        }
        return $this->client->sendSync($setRequest);
    }

    /**
     * Alias of {@link static::set()}
     * 
     * @param mixed $numbers   Targeted items. Can be any criteria accepted by
     *     {@link static::find()}.
     * @param array $newValues An array with the names of each changed property
     *     as an array key, and the new value as an array value.
     *     Flags (properties with a value "true" that is interpreted as
     *     equivalent of "yes" from CLI) can also be specified with a numeric
     *     index as the array key, and the name of the flag as the array value.
     * 
     * @return ResponseCollection Returns the response collection, allowing you
     *     to inspect errors, if any.
     */
    public function edit($numbers, array $newValues)
    {
        return $this->set($numbers, $newValues);
    }

    /**
     * Unsets a value of a specified item at the current menu.
     * 
     * Equivalent of scripting's "unset" command. The "Value" part in the method
     * name is added because "unset" is a language construct, and thus a
     * reserved word.
     * 
     * @param mixed  $numbers   Targeted items. Can be any criteria accepted
     *     by {@link static::find()}.
     * @param string $valueName The name of the value you want to unset.
     * 
     * @return ResponseCollection Returns the response collection, allowing you
     *     to inspect errors, if any.
     */
    public function unsetValue($numbers, $valueName)
    {
        $unsetRequest = new Request($this->menu . '/unset');
        return $this->client->sendSync(
            $unsetRequest->setArgument('numbers', $this->find($numbers))
                ->setArgument('value-name', $valueName)
        );
    }

    /**
     * Adds a new item at the current menu.
     * 
     * @param array $values Accepts one or more items to add to the
     *     current menu. The data about each item is specified as an array with
     *     the names of each property as an array key, and the value as an array
     *     value.
     *     Flags (properties with a value "true" that is interpreted as
     *     equivalent of "yes" from CLI) can also be specified with a numeric
     *     index as the array key, and the name of the flag as the array value.
     * @param array $...    Additional items.
     * 
     * @return string A comma separated list of the new items' IDs. If a
     *     particular item was not added, this will be indicated by an empty
     *     string in its spot on the list. e.g. "*1D,,*1E" means that
     *     you supplied three items to be added, of which the second one was
     *     not added for some reason.
     */
    public function add(array $values)
    {
        $addRequest = new Request($this->menu . '/add');
        $idList = '';
        foreach (func_get_args() as $values) {
            $idList .= ',';
            if (!is_array($values)) {
                continue;
            }
            foreach ($values as $name => $value) {
                if (is_int($name)) {
                    $addRequest->setArgument($value, 'true');
                } else {
                    $addRequest->setArgument($name, $value);
                }
            }
            $id = $this->client->sendSync($addRequest)->getProperty('ret');
            if (null !== $this->idCache) {
                $this->idCache[] = $id;
            }
            $idList .= $id;
            $addRequest->removeAllArguments();
        }
        return substr($idList, 1);
    }

    /**
     * Moves items at the current menu before a certain other item.
     * 
     * Moves items before a certain other item. Note that the "move"
     * command is not available on all menus. As a rule of thumb, if the order
     * of items in a menu is irrelevant to their interpretation, there won't
     * be a move command on that menu. If in doubt, check from a terminal.
     * 
     * @param mixed $numbers     Targeted items. Can be any criteria accepted
     *     by {@link static::find()}.
     * @param mixed $destination item before which the targeted items will be
     *     moved to. Can be any criteria accepted by {@link static::find()}.
     *     If multiple items match the criteria, the targeted items will move
     *     above the first match.
     * 
     * @return ResponseCollection Returns the response collection, allowing you
     *     to inspect errors, if any.
     */
    public function move($numbers, $destination)
    {
        $moveRequest = new Request($this->menu . '/move');
        $moveRequest->setArgument('numbers', $this->find($numbers));
        $destination = $this->find($destination);
        if (false !== strpos($destination, ',')) {
            $destination = strstr($destination, ',', true);
        }
        $moveRequest->setArgument('destination', $destination);
        $this->clearIdCache();
        return $this->client->sendSync($moveRequest);
    }

    /**
     * Counts items at the current menu.
     * 
     * Counts items at the current menu. This executes a dedicated command
     * ("print" with a "count-only" argument) on RouterOS, which is why only
     * queries are allowed as a criteria, in contrast with
     * {@link static::find()}, where numbers and callbacks are allowed also.
     * 
     * @param int   $mode  The counter mode.
     *     Currently ignored, but present for compatiblity with PHP 5.6+.
     * @param Query $query A query to filter items by. Without it, all items
     *     are included in the count.
     * 
     * @return int The number of items, or -1 on failure (e.g. if the
     *     current menu does not have a "print" command or items to be counted).
     */
    public function count($mode = COUNT_NORMAL, Query $query = null)
    {
        $result = $this->client->sendSync(
            new Request($this->menu . '/print count-only=""', $query)
        )->end()->getProperty('ret');

        if (null === $result) {
            return -1;
        }
        if (Stream::isStream($result)) {
            $result = stream_get_contents($result);
        }
        return (int)$result;
    }

    /**
     * Gets all items in the current menu.
     * 
     * Gets all items in the current menu, using a print request.
     * 
     * @param array<int|string,string> $args  Additional arguments to pass
     *     to the request.
     *     Each array key is the name of the argument, and each array value is
     *     the value of the argument to be passed.
     *     Arguments without a value (i.e. empty arguments) can also be
     *     specified using a numeric key, and the name of the argument as the
     *     array value.
     * @param Query|null               $query A query to filter items by.
     *     NULL to get all items.
     * 
     * @return ResponseCollection|false A response collection with all
     *     {@link Response::TYPE_DATA} responses. The collection will be empty
     *     when there are no matching items. FALSE on failure.
     */
    public function getAll(array $args = array(), Query $query = null)
    {
        $printRequest = new Request($this->menu . '/print', $query);
        foreach ($args as $name => $value) {
            if (is_int($name)) {
                $printRequest->setArgument($value);
            } else {
                $printRequest->setArgument($name, $value);
            }
        }
        $responses = $this->client->sendSync($printRequest);

        if (count($responses->getAllOfType(Response::TYPE_ERROR)) > 0) {
            return false;
        }
        return $responses->getAllOfType(Response::TYPE_DATA);
    }

    /**
     * Puts a file on RouterOS's file system.
     * 
     * Puts a file on RouterOS's file system, regardless of the current menu.
     * Note that this is a **VERY VERY VERY** time consuming method - it takes a
     * minimum of a little over 4 seconds, most of which are in sleep. It waits
     * 2 seconds after a file is first created (required to actually start
     * writing to the file), and another 2 seconds after its contents is written
     * (performed in order to verify success afterwards).
     * Similarly for removal (when $data is NULL) - there are two seconds in
     * sleep, used to verify the file was really deleted.
     * 
     * If you want an efficient way of transferring files, use (T)FTP.
     * If you want an efficient way of removing files, use
     * {@link static::setMenu()} to move to the "/file" menu, and call
     * {@link static::remove()} without performing verification afterwards.
     * 
     * @param string               $filename  The filename to write data in.
     * @param string|resource|null $data      The data the file is going to have
     *     as a string or a seekable stream.
     *     Setting the value to NULL removes a file of this name.
     *     If a seekable stream is provided, it is sent from its current
     *     posistion to its end, and the pointer is seeked back to its current
     *     position after sending.
     *     Non seekable streams, as well as all other types, are casted to a
     *     string.
     * @param bool                 $overwrite Whether to overwrite the file if
     *     it exists.
     * 
     * @return bool TRUE on success, FALSE on failure.
     */
    public function filePutContents($filename, $data, $overwrite = false)
    {
        $printRequest = new Request(
            '/file/print .proplist=""',
            Query::where('name', $filename)
        );
        $fileExists = count($this->client->sendSync($printRequest)) > 1;

        if (null === $data) {
            if (!$fileExists) {
                return false;
            }
            $removeRequest = new Request('/file/remove');
            $this->client->sendSync(
                $removeRequest->setArgument('numbers', $filename)
            );
            //Required for RouterOS to REALLY remove the file.
            sleep(2);
            return !(count($this->client->sendSync($printRequest)) > 1);
        }

        if (!$overwrite && $fileExists) {
            return false;
        }
        $result = $this->client->sendSync(
            $printRequest->setArgument('file', $filename)
        );
        if (count($result->getAllOfType(Response::TYPE_ERROR)) > 0) {
            return false;
        }
        //Required for RouterOS to write the initial file.
        sleep(2);
        $setRequest = new Request('/file/set contents=""');
        $setRequest->setArgument('numbers', $filename);
        $this->client->sendSync($setRequest);
        $this->client->sendSync($setRequest->setArgument('contents', $data));
        //Required for RouterOS to write the file's new contents.
        sleep(2);

        $fileSize = $this->client->sendSync(
            $printRequest->setArgument('file', null)
                ->setArgument('.proplist', 'size')
        )->getProperty('size');
        if (Stream::isStream($fileSize)) {
            $fileSize = stream_get_contents($fileSize);
        }
        if (Communicator::isSeekableStream($data)) {
            return Communicator::seekableStreamLength($data) == $fileSize;
        } else {
            return sprintf('%u', strlen((string)$data)) === $fileSize;
        };
    }

    /**
     * Gets the contents of a specified file.
     * 
     * @param string $filename      The name of the file to get the contents of.
     * @param string $tmpScriptName In order to get the file's contents, a
     *     script is created at "/system script" with a random name, the
     *     source of which is then overwriten with the file's contents, and
     *     finally retrieved. To eliminate any possibility of name clashes, you
     *     can specify your own name for the script.
     * 
     * @return string|resource|false The contents of the file as a string or as
     *     new PHP temp stream if the underliying
     *     {@link Client::isStreamingResponses()} is set to TRUE.
     *     FALSE is returned if there is no such file.
     */
    public function fileGetContents($filename, $tmpScriptName = null)
    {
        $checkRequest = new Request(
            '/file/print',
            Query::where('name', $filename)
        );
        if (1 === count($this->client->sendSync($checkRequest))) {
            return false;
        }
        $contents = $this->_exec(
            '/system script set $"_" source=[/file get $filename contents]',
            array('filename' => $filename),
            null,
            $tmpScriptName,
            true
        );
        return $contents;
    }

    /**
     * Performs an action on a bulk of items at the current menu.
     * 
     * @param string $what What action to perform.
     * @param array  $args Zero or more arguments can be specified, each being
     *     a criteria. If zero arguments are specified, removes all items.
     *     See {@link static::find()} for a description of what criteria are
     *     accepted.
     * 
     * @return ResponseCollection Returns the response collection, allowing you
     *     to inspect errors, if any.
     */
    protected function doBulk($what, array $args = array())
    {
        $bulkRequest = new Request($this->menu . '/' . $what);
        $bulkRequest->setArgument(
            'numbers',
            call_user_func_array(array($this, 'find'), $args)
        );
        return $this->client->sendSync($bulkRequest);
    }

    /**
     * Executes a RouterOS script.
     * 
     * Same as the public equivalent, with the addition of allowing you to get
     * the contents of the script post execution, instead of removing it.
     * 
     * @param string|resource $source The source of the script, as a string or
     *     stream. If a stream is provided, reading starts from the current
     *     position to the end of the stream, and the pointer stays at the end
     *     after reading is done.
     * @param array           $params An array of parameters to make available
     *     in the script as local variables.
     *     Variable names are array keys, and variable values are array values.
     *     Array values are automatically processed with
     *     {@link static::escapeValue()}. Streams are also supported, and are
     *     processed in chunks, each processed with
     *     {@link static::escapeString()}. Processing starts from the current
     *     position to the end of the stream, and the stream's pointer is left
     *     untouched after the reading is done.
     *     Note that the script's (generated) name is always added as the
     *     variable "_", which will be inadvertently lost if you overwrite it
     *     from here.
     * @param string          $policy Allows you to specify a policy the script
     *     must follow. Has the same format as in terminal.
     *     If left NULL, the script has no restrictions beyond those imposed by
     *     the username.
     * @param string          $name   The script is executed after being saved
     *     in "/system script" under a random name (prefixed with the computer's
     *     name), and is removed after execution. To eliminate any possibility
     *     of name clashes, you can specify your own name.
     * @param bool            $get    Whether to get the source of the script.
     * 
     * @return ResponseCollection|string Returns the response collection of the
     *     run, allowing you to inspect errors, if any.
     *     If the script was not added successfully before execution, the
     *     ResponseCollection from the add attempt is going to be returned.
     *     If $get is TRUE, returns the source of the script on success.
     */
    private function _exec(
        $source,
        array $params = array(),
        $policy = null,
        $name = null,
        $get = false
    ) {
        $request = new Request('/system/script/add');
        if (null === $name) {
            $name = uniqid(gethostname(), true);
        }
        $request->setArgument('name', $name);
        $request->setArgument('policy', $policy);

        $params += array('_' => $name);

        $finalSource = fopen('php://temp', 'r+b');
        fwrite(
            $finalSource,
            '/' . str_replace('/', ' ', substr($this->menu, 1)). "\n"
        );
        static::appendScript($finalSource, $source, $params);
        fwrite($finalSource, "\n");
        rewind($finalSource);

        $request->setArgument('source', $finalSource);
        $result = $this->client->sendSync($request);

        if (0 === count($result->getAllOfType(Response::TYPE_ERROR))) {
            $request = new Request('/system/script/run');
            $request->setArgument('number', $name);
            $result = $this->client->sendSync($request);

            if ($get) {
                $result = $this->client->sendSync(
                    new Request(
                        '/system/script/print .proplist="source"',
                        Query::where('name', $name)
                    )
                )->getProperty('source');
            }
            $request = new Request('/system/script/remove');
            $request->setArgument('numbers', $name);
            $this->client->sendSync($request);
        }

        return $result;
    }
}


File: /PEAR2\Net\Transmitter\Exception.php
<?php

/**
 * Wrapper for network stream functionality.
 * 
 * PHP has built in support for various types of network streams, such as HTTP and TCP sockets. One problem that arises with them is the fact that a single fread/fwrite call might not read/write all the data you intended, regardless of whether you're in blocking mode or not. While the PHP manual offers a workaround in the form of a loop with a few variables, using it every single time you want to read/write can be tedious.

This package abstracts this away, so that when you want to get exactly N amount of bytes, you can be sure the upper levels of your app will be dealing with N bytes. Oh, and the functionality is nicely wrapped in an object (but that's just the icing on the cake).
 * 
 * PHP version 5
 * 
 * @category  Net
 * @package   PEAR2_Net_Transmitter
 * @author    Vasil Rangelov <boen.robot@gmail.com>
 * @copyright 2011 Vasil Rangelov
 * @license   http://www.gnu.org/copyleft/lesser.html LGPL License 2.1
 * @version   1.0.0a5
 * @link      http://pear2.php.net/PEAR2_Net_Transmitter
 */
/**
 * The namespace declaration.
 */
namespace PEAR2\Net\Transmitter;

/**
 * Generic exception class of this package.
 * 
 * @category Net
 * @package  PEAR2_Net_Transmitter
 * @author   Vasil Rangelov <boen.robot@gmail.com>
 * @license  http://www.gnu.org/copyleft/lesser.html LGPL License 2.1
 * @link     http://pear2.php.net/PEAR2_Net_Transmitter
 */
interface Exception
{
}


File: /PEAR2\Net\Transmitter\FilterCollection.php
<?php

/**
 * Wrapper for network stream functionality.
 * 
 * PHP has built in support for various types of network streams, such as HTTP and TCP sockets. One problem that arises with them is the fact that a single fread/fwrite call might not read/write all the data you intended, regardless of whether you're in blocking mode or not. While the PHP manual offers a workaround in the form of a loop with a few variables, using it every single time you want to read/write can be tedious.

This package abstracts this away, so that when you want to get exactly N amount of bytes, you can be sure the upper levels of your app will be dealing with N bytes. Oh, and the functionality is nicely wrapped in an object (but that's just the icing on the cake).
 * 
 * PHP version 5
 * 
 * @category  Net
 * @package   PEAR2_Net_Transmitter
 * @author    Vasil Rangelov <boen.robot@gmail.com>
 * @copyright 2011 Vasil Rangelov
 * @license   http://www.gnu.org/copyleft/lesser.html LGPL License 2.1
 * @version   1.0.0a5
 * @link      http://pear2.php.net/PEAR2_Net_Transmitter
 */
/**
 * The namespace declaration.
 */
namespace PEAR2\Net\Transmitter;

/**
 * A filter collection.
 * 
 * Represents a collection of stream filters.
 * 
 * @category Net
 * @package  PEAR2_Net_Transmitter
 * @author   Vasil Rangelov <boen.robot@gmail.com>
 * @license  http://www.gnu.org/copyleft/lesser.html LGPL License 2.1
 * @link     http://pear2.php.net/PEAR2_Net_Transmitter
 * @see      Client
 */
class FilterCollection implements \SeekableIterator, \Countable
{
    /**
     * @var array The filter collection itself.
     */
    protected $filters = array();
    
    /**
     * @var int A pointer, as required by SeekableIterator.
     */
    protected $position = 0;
    
    /**
     * Appends a filter to the collection
     * 
     * @param string $name   The name of the filter.
     * @param array  $params An array of parameters for the filter.
     * 
     * @return $this The collection itself.
     */
    public function append($name, array $params = array())
    {
        $this->filters[] = array((string) $name, $params);
        return $this;
    }
    
    /**
     * Inserts the filter before a position.
     * 
     * Inserts the specified filter before a filter at a specified position. The
     * new filter takes the specified position, while previous filters are moved
     * forward by one.
     * 
     * @param int    $position The position before which the filter will be
     *     inserted.
     * @param string $name     The name of the filter.
     * @param array  $params   An array of parameters for the filter.
     * 
     * @return $this The collection itself.
     */
    public function insertBefore($position, $name, array $params = array())
    {
        $position = (int) $position;
        if ($position <= 0) {
            $this->filters = array_merge(
                array(0 => array((string) $name, $params)),
                $this->filters
            );
            return $this;
        }
        if ($position > count($this->filters)) {
            return $this->append($name, $params);
        }
        $this->filters = array_merge(
            array_slice($this->filters, 0, $position),
            array(0 => array((string) $name, $params)),
            array_slice($this->filters, $position)
        );
        return $this;
    }
    
    /**
     * Removes a filter at a specified position.
     * 
     * @param int $position The position from which to remove a filter.
     * 
     * @return $this The collection itself.
     */
    public function removeAt($position)
    {
        unset($this->filters[$position]);
        $this->filters = array_values($this->filters);
        return $this;
    }
    
    /**
     * Clears the collection
     * 
     * @return $this The collection itself.
     */
    public function clear()
    {
        $this->filters = array();
        return $this;
    }

    /**
     * Gets the number of filters in the collection.
     * 
     * @return int The number of filters in the collection.
     */
    public function count()
    {
        return count($this->filters);
    }

    /**
     * Resets the pointer to 0.
     * 
     * @return bool TRUE if the collection is not empty, FALSE otherwise.
     */
    public function rewind()
    {
        return $this->seek(0);
    }

    /**
     * Moves the pointer to a specified position.
     * 
     * @param int $position The position to move to.
     * 
     * @return bool TRUE if the specified position is valid, FALSE otherwise.
     */
    public function seek($position)
    {
        $this->position = $position;
        return $this->valid();
    }
    
    /**
     * Gets the current position.
     * 
     * @return int The current position.
     */
    public function getCurrentPosition()
    {
        return $this->position;
    }

    /**
     * Moves the pointer forward by 1.
     * 
     * @return bool TRUE if the new position is valid, FALSE otherwise.
     */
    public function next()
    {
        ++$this->position;
        return $this->valid();
    }

    /**
     * Gets the filter name at the current pointer position.
     * 
     * @return string The name of the filter at the current position.
     */
    public function key()
    {
        return $this->valid() ? $this->filters[$this->position][0] : false;
    }

    /**
     * Gets the filter parameters at the current pointer position.
     * 
     * @return array An array of parameters for the filter at the current
     *     position.
     */
    public function current()
    {
        return $this->valid() ? $this->filters[$this->position][1] : false;
    }

    /**
     * Moves the pointer backwards by 1.
     * 
     * @return bool TRUE if the new position is valid, FALSE otherwise.
     */
    public function prev()
    {
        --$this->position;
        return $this->valid();
    }

    /**
     * Moves the pointer to the last valid position.
     * 
     * @return bool TRUE if the collection is not empty, FALSE otherwise.
     */
    public function end()
    {
        $this->position = count($this->filters) - 1;
        return $this->valid();
    }

    /**
     * Checks if the pointer is still pointing to an existing offset.
     * 
     * @return bool TRUE if the pointer is valid, FALSE otherwise.
     */
    public function valid()
    {
        return array_key_exists($this->position, $this->filters);
    }
}


File: /PEAR2\Net\Transmitter\LockException.php
<?php

/**
 * Wrapper for network stream functionality.
 * 
 * PHP has built in support for various types of network streams, such as HTTP and TCP sockets. One problem that arises with them is the fact that a single fread/fwrite call might not read/write all the data you intended, regardless of whether you're in blocking mode or not. While the PHP manual offers a workaround in the form of a loop with a few variables, using it every single time you want to read/write can be tedious.

This package abstracts this away, so that when you want to get exactly N amount of bytes, you can be sure the upper levels of your app will be dealing with N bytes. Oh, and the functionality is nicely wrapped in an object (but that's just the icing on the cake).
 * 
 * PHP version 5
 * 
 * @category  Net
 * @package   PEAR2_Net_Transmitter
 * @author    Vasil Rangelov <boen.robot@gmail.com>
 * @copyright 2011 Vasil Rangelov
 * @license   http://www.gnu.org/copyleft/lesser.html LGPL License 2.1
 * @version   1.0.0a5
 * @link      http://pear2.php.net/PEAR2_Net_Transmitter
 */
/**
 * The namespace declaration.
 */
namespace PEAR2\Net\Transmitter;

/**
 * Exception thrown when something goes wrong when dealing with locks.
 * 
 * @category Net
 * @package  PEAR2_Net_Transmitter
 * @author   Vasil Rangelov <boen.robot@gmail.com>
 * @license  http://www.gnu.org/copyleft/lesser.html LGPL License 2.1
 * @link     http://pear2.php.net/PEAR2_Net_Transmitter
 */
class LockException extends \RuntimeException implements Exception
{
}


File: /PEAR2\Net\Transmitter\NetworkStream.php
<?php

/**
 * Wrapper for network stream functionality.
 * 
 * PHP has built in support for various types of network streams, such as HTTP and TCP sockets. One problem that arises with them is the fact that a single fread/fwrite call might not read/write all the data you intended, regardless of whether you're in blocking mode or not. While the PHP manual offers a workaround in the form of a loop with a few variables, using it every single time you want to read/write can be tedious.

This package abstracts this away, so that when you want to get exactly N amount of bytes, you can be sure the upper levels of your app will be dealing with N bytes. Oh, and the functionality is nicely wrapped in an object (but that's just the icing on the cake).
 * 
 * PHP version 5
 * 
 * @category  Net
 * @package   PEAR2_Net_Transmitter
 * @author    Vasil Rangelov <boen.robot@gmail.com>
 * @copyright 2011 Vasil Rangelov
 * @license   http://www.gnu.org/copyleft/lesser.html LGPL License 2.1
 * @version   1.0.0a5
 * @link      http://pear2.php.net/PEAR2_Net_Transmitter
 */
/**
 * The namespace declaration.
 */
namespace PEAR2\Net\Transmitter;

/**
 * A network transmitter.
 * 
 * This is a convinience wrapper for network streams. Used to ensure data
 * integrity.
 * 
 * @category Net
 * @package  PEAR2_Net_Transmitter
 * @author   Vasil Rangelov <boen.robot@gmail.com>
 * @license  http://www.gnu.org/copyleft/lesser.html LGPL License 2.1
 * @link     http://pear2.php.net/PEAR2_Net_Transmitter
 */
abstract class NetworkStream extends Stream
{
    /**
     * Used in {@link setCrypto()} to disable encryption.
     */
    const CRYPTO_OFF = '';

    /**
     * Used in {@link setCrypto()} to set encryption to either SSLv2 or SSLv3,
     * depending on what the other end supports.
     */
    const CRYPTO_SSL = 'SSLv23';

    /**
     * Used in {@link setCrypto()} to set encryption to SSLv2.
     */
    const CRYPTO_SSL2 = 'SSLv2';

    /**
     * Used in {@link setCrypto()} to set encryption to SSLv3.
     */
    const CRYPTO_SSL3 = 'SSLv3';

    /**
     * Used in {@link setCrypto()} to set encryption to TLS (exact version
     * negotiated between 1.0 and 1.2).
     */
    const CRYPTO_TLS = 'TLS';
    
    /**
     * @var string The type of stream. Can be either "_CLIENT" or "_SERVER".
     *     Used to complement the encryption type. Must be set by child classes
     *     for {@link setCrypto()} to work properly.
     */
    protected $streamType = '';

    /**
     * @var string The current cryptography setting.
     */
    protected $crypto = '';

    /**
     * Wraps around the specified stream.
     * 
     * @param resource $stream The stream to wrap around.
     */
    public function __construct($stream)
    {
        parent::__construct($stream, true);
    }

    /**
     * Gets the current cryptography setting.
     * 
     * @return string One of this class' CRYPTO_* constants.
     */
    public function getCrypto()
    {
        return $this->crypto;
    }

    /**
     * Sets the current connection's cryptography setting.
     * 
     * @param string $type The encryption type to set. Must be one of this
     *     class' CRYPTO_* constants.
     * 
     * @return boolean TRUE on success, FALSE on failure.
     */
    public function setCrypto($type)
    {
        if (self::CRYPTO_OFF === $type) {
            $result = stream_socket_enable_crypto($this->stream, false);
        } else {
            $result = stream_socket_enable_crypto(
                $this->stream,
                true,
                constant("STREAM_CRYPTO_METHOD_{$type}{$this->streamType}")
            );
        }

        if ($result) {
            $this->crypto = $type;
        }
        return $result;
    }

    /**
     * Checks whether the stream is available for operations.
     * 
     * @return bool TRUE if the stream is available, FALSE otherwise.
     */
    public function isAvailable()
    {
        if (parent::isStream($this->stream)) {
            if ($this->isBlocking && feof($this->stream)) {
                return false;
            }
            $meta = stream_get_meta_data($this->stream);
            return !$meta['eof'];
        }
        return false;
    }
    
    /**
     * Sets the size of a stream's buffer.
     * 
     * @param int    $size      The desired size of the buffer, in bytes.
     * @param string $direction The buffer of which direction to set. Valid
     *     values are the DIRECTION_* constants.
     * 
     * @return bool TRUE on success, FALSE on failure.
     */
    public function setBuffer($size, $direction = self::DIRECTION_ALL)
    {
        $result = parent::setBuffer($size, $direction);
        if (self::DIRECTION_SEND === $direction
            && function_exists('stream_set_chunk_size') && !$result
        ) {
            return false !== @stream_set_chunk_size($this->stream, $size);
        }
        return $result;
    }
    
    /**
     * Shutdown a full-duplex connection
     * 
     * Shutdowns (partially or not) a full-duplex connection.
     * 
     * @param string $direction The direction for which to disable further
     *     communications.
     * 
     * @return bool TRUE on success, FALSE on failure.
     */
    public function shutdown($direction = self::DIRECTION_ALL)
    {
        $directionMap = array(
            self::DIRECTION_ALL => STREAM_SHUT_RDWR,
            self::DIRECTION_SEND => STREAM_SHUT_WR,
            self::DIRECTION_RECEIVE => STREAM_SHUT_RD
        );
        return array_key_exists($direction, $directionMap)
            && stream_socket_shutdown($this->stream, $directionMap[$direction]);
    }
}


File: /PEAR2\Net\Transmitter\SocketException.php
<?php

/**
 * Wrapper for network stream functionality.
 * 
 * PHP has built in support for various types of network streams, such as HTTP and TCP sockets. One problem that arises with them is the fact that a single fread/fwrite call might not read/write all the data you intended, regardless of whether you're in blocking mode or not. While the PHP manual offers a workaround in the form of a loop with a few variables, using it every single time you want to read/write can be tedious.

This package abstracts this away, so that when you want to get exactly N amount of bytes, you can be sure the upper levels of your app will be dealing with N bytes. Oh, and the functionality is nicely wrapped in an object (but that's just the icing on the cake).
 * 
 * PHP version 5
 * 
 * @category  Net
 * @package   PEAR2_Net_Transmitter
 * @author    Vasil Rangelov <boen.robot@gmail.com>
 * @copyright 2011 Vasil Rangelov
 * @license   http://www.gnu.org/copyleft/lesser.html LGPL License 2.1
 * @version   1.0.0a5
 * @link      http://pear2.php.net/PEAR2_Net_Transmitter
 */
/**
 * The namespace declaration.
 */
namespace PEAR2\Net\Transmitter;

/**
 * Used to enable any exception in chaining.
 */
use Exception as E;

/**
 * Exception thrown when something goes wrong with the connection.
 * 
 * @category Net
 * @package  PEAR2_Net_Transmitter
 * @author   Vasil Rangelov <boen.robot@gmail.com>
 * @license  http://www.gnu.org/copyleft/lesser.html LGPL License 2.1
 * @link     http://pear2.php.net/PEAR2_Net_Transmitter
 */
class SocketException extends StreamException
{

    /**
     * @var int The system level error code.
     */
    protected $errorNo;

    /**
     * @var string The system level error message.
     */
    protected $errorStr;

    /**
     * Creates a new socket exception.
     * 
     * @param string                   $message  The Exception message to throw.
     * @param int                      $code     The Exception code.
     * @param E|null                   $previous Previous exception thrown,
     *     or NULL if there is none.
     * @param int|string|resource|null $fragment The fragment up until the
     *     point of failure.
     *     On failure with sending, this is the number of bytes sent
     *     successfully before the failure.
     *     On failure when receiving, this is a string/stream holding
     *     the contents received successfully before the failure.
     *     NULL if the failure occured before the operation started.
     * @param int                      $errorNo  The system level error number.
     * @param string                   $errorStr The system level
     *     error message.
     */
    public function __construct(
        $message = '',
        $code = 0,
        E $previous = null,
        $fragment = null,
        $errorNo = null,
        $errorStr = null
    ) {
        parent::__construct($message, $code, $previous, $fragment);
        $this->errorNo = $errorNo;
        $this->errorStr = $errorStr;
    }

    /**
     * Gets the system level error code on the socket.
     * 
     * @return int The system level error number.
     */
    public function getSocketErrorNumber()
    {
        return $this->errorNo;
    }

    // @codeCoverageIgnoreStart
    // Unreliable in testing.

    /**
     * Gets the system level error message on the socket.
     * 
     * @return string The system level error message.
     */
    public function getSocketErrorMessage()
    {
        return $this->errorStr;
    }

    /**
     * Returns a string representation of the exception.
     * 
     * @return string The exception as a string.
     */
    public function __toString()
    {
        $result = parent::__toString();
        if (null !== $this->getSocketErrorNumber()) {
            $result .= "\nSocket error number:" . $this->getSocketErrorNumber();
        }
        if (null !== $this->getSocketErrorMessage()) {
            $result .= "\nSocket error message:"
                . $this->getSocketErrorMessage();
        }
        return $result;
    }
    // @codeCoverageIgnoreEnd
}


File: /PEAR2\Net\Transmitter\Stream.php
<?php

/**
 * Wrapper for network stream functionality.
 * 
 * PHP has built in support for various types of network streams, such as HTTP and TCP sockets. One problem that arises with them is the fact that a single fread/fwrite call might not read/write all the data you intended, regardless of whether you're in blocking mode or not. While the PHP manual offers a workaround in the form of a loop with a few variables, using it every single time you want to read/write can be tedious.

This package abstracts this away, so that when you want to get exactly N amount of bytes, you can be sure the upper levels of your app will be dealing with N bytes. Oh, and the functionality is nicely wrapped in an object (but that's just the icing on the cake).
 * 
 * PHP version 5
 * 
 * @category  Net
 * @package   PEAR2_Net_Transmitter
 * @author    Vasil Rangelov <boen.robot@gmail.com>
 * @copyright 2011 Vasil Rangelov
 * @license   http://www.gnu.org/copyleft/lesser.html LGPL License 2.1
 * @version   1.0.0a5
 * @link      http://pear2.php.net/PEAR2_Net_Transmitter
 */
/**
 * The namespace declaration.
 */
namespace PEAR2\Net\Transmitter;

use Exception as E;

/**
 * A stream transmitter.
 * 
 * This is a convinience wrapper for stream functionality. Used to ensure data
 * integrity. Designed for TCP sockets, but it has intentionally been made to
 * accept any stream.
 * 
 * @category Net
 * @package  PEAR2_Net_Transmitter
 * @author   Vasil Rangelov <boen.robot@gmail.com>
 * @license  http://www.gnu.org/copyleft/lesser.html LGPL License 2.1
 * @link     http://pear2.php.net/PEAR2_Net_Transmitter
 */
class Stream
{
    /**
     * Used to stop settings in either direction being applied.
     */
    const DIRECTION_NONE = 0;
    /**
     * Used to apply settings only to receiving.
     */
    const DIRECTION_RECEIVE = 1;
    /**
     * Used to apply settings only to sending.
     */
    const DIRECTION_SEND = 2;
    /**
     * Used to apply settings to both sending and receiving.
     */
    const DIRECTION_ALL = 3;

    /**
     * @var resource The stream to wrap around.
     */
    protected $stream;

    /**
     * @var bool Whether to automaticaly close the stream on
     *     object destruction if it's not a persistent one. Setting this to
     *     FALSE may be useful if you're only using this class "part time",
     *     while setting it to TRUE might be useful if you're doing some
     *     "on offs".
     */
    protected $autoClose = false;

    /**
     * @var bool A flag that tells whether or not the stream is persistent.
     */
    protected $persist;

    /**
     * @var bool Whether the wrapped stream is in blocking mode or not.
     */
    protected $isBlocking = true;
    
    /**
     * @var array An associative array with the chunk size of each direction.
     *     Key is the direction, value is the size in bytes as integer.
     */
    protected $chunkSize = array(
        self::DIRECTION_SEND => 0xFFFFF, self::DIRECTION_RECEIVE => 0xFFFFF
    );

    /**
     * Wraps around the specified stream.
     * 
     * @param resource $stream    The stream to wrap around.
     * @param bool     $autoClose Whether to automaticaly close the stream on
     *     object destruction if it's not a persistent one. Setting this to
     *     FALSE may be useful if you're only using this class "part time",
     *     while setting it to TRUE might be useful if you're doing some
     *     "on offs".
     * 
     * @see static::isFresh()
     */
    public function __construct($stream, $autoClose = false)
    {
        if (!self::isStream($stream)) {
            throw $this->createException('Invalid stream supplied.', 1);
        }
        $this->stream = $stream;
        $this->autoClose = (bool) $autoClose;
        $this->persist = (bool) preg_match(
            '#\s?persistent\s?#sm',
            get_resource_type($stream)
        );
        $meta = stream_get_meta_data($stream);
        $this->isBlocking = isset($meta['blocked']) ? $meta['blocked'] : true;
    }

    /**
     * PHP error handler for connection errors.
     * 
     * @param string $level   Level of PHP error raised. Ignored.
     * @param string $message Message raised by PHP.
     * 
     * @return void
     * @throws SocketException That's how the error is handled.
     * @SuppressWarnings(PHPMD.UnusedFormalParameter)
     */
    protected function handleError($level, $message)
    {
        throw $this->createException($message, 0);
    }

    /**
     * Checks if a given variable is a stream resource.
     * 
     * @param mixed $var The variable to check.
     * 
     * @return bool TRUE on success, FALSE on failure.
     */
    public static function isStream($var)
    {
        return is_resource($var)
            && (bool) preg_match('#\s?stream$#sm', get_resource_type($var));
    }

    /**
     * Checks whether the wrapped stream is fresh.
     * 
     * Checks whether the wrapped stream is fresh. A stream is considered fresh
     * if there hasn't been any activity on it. Particularly useful for
     * detecting reused persistent connections.
     * 
     * @return bool TRUE if the socket is fresh, FALSE otherwise.
     */
    public function isFresh()
    {
        return ftell($this->stream) === 0;
    }

    /**
     * Checks whether the wrapped stream is a persistent one.
     * 
     * @return bool TRUE if the stream is a persistent one, FALSE otherwise. 
     */
    public function isPersistent()
    {
        return $this->persist;
    }

    /**
     * Checks whether the wrapped stream is a blocking one.
     * 
     * @return bool TRUE if the stream is a blocking one, FALSE otherwise. 
     */
    public function isBlocking()
    {
        return $this->isBlocking;
    }

    /**
     * Sets blocking mode.
     * 
     * @param bool $block Sets whether the stream is in blocking mode.
     * 
     * @return bool TRUE on success, FALSE on failure.
     */
    public function setIsBlocking($block)
    {
        $block = (bool)$block;
        if (stream_set_blocking($this->stream, (int)$block)) {
            $this->isBlocking = $block;
            return true;
        }
        return false;
    }
    
    /**
     * Sets the timeout for the stream.
     * 
     * @param int $seconds      Timeout in seconds.
     * @param int $microseconds Timeout in microseconds to be added to the
     *     seconds.
     * 
     * @return bool TRUE on success, FALSE on failure.
     */
    public function setTimeout($seconds, $microseconds = 0)
    {
        return stream_set_timeout($this->stream, $seconds, $microseconds);
    }
    
    /**
     * Sets the size of a stream's buffer.
     * 
     * @param int    $size      The desired size of the buffer, in bytes.
     * @param string $direction The buffer of which direction to set. Valid
     *     values are the DIRECTION_* constants.
     * 
     * @return bool TRUE on success, FALSE on failure.
     */
    public function setBuffer($size, $direction = self::DIRECTION_ALL)
    {
        switch($direction) {
        case self::DIRECTION_SEND:
            return stream_set_write_buffer($this->stream, $size) === 0;
        case self::DIRECTION_RECEIVE:
            return stream_set_read_buffer($this->stream, $size) === 0;
        case self::DIRECTION_ALL:
            return $this->setBuffer($size, self::DIRECTION_RECEIVE)
                && $this->setBuffer($size, self::DIRECTION_SEND);
        }
        return false;
    }
    
    /**
     * Sets the size of the chunk.
     * 
     * To ensure data integrity, as well as to allow for lower memory
     * consumption, data is sent/received in chunks. This function
     * allows you to set the size of each chunk. The default is 0xFFFFF.
     * 
     * @param int    $size      The desired size of the chunk, in bytes.
     * @param string $direction The chunk of which direction to set. Valid
     *     values are the DIRECTION_* constants.
     * 
     * @return bool TRUE on success, FALSE on failure.
     */
    public function setChunk($size, $direction = self::DIRECTION_ALL)
    {
        $size = (int) $size;
        if ($size <= 0) {
            return false;
        }
        switch($direction) {
        case self::DIRECTION_SEND:
        case self::DIRECTION_RECEIVE:
            $this->chunkSize[$direction] = $size;
            return true;
        case self::DIRECTION_ALL:
            $this->chunkSize[self::DIRECTION_SEND]
                = $this->chunkSize[self::DIRECTION_RECEIVE] = $size;
            return true;
        }
        return false;
    }
    
    /**
     * Gets the size of the chunk.
     * 
     * @param string $direction The chunk of which direction to get. Valid
     *     values are the DIRECTION_* constants.
     * 
     * @return int|array|false The chunk size in bytes,
     *     or an array of chunk sizes with the directions as keys.
     *     FALSE on invalid direction.
     */
    public function getChunk($direction = self::DIRECTION_ALL)
    {
        switch($direction) {
        case self::DIRECTION_SEND:
        case self::DIRECTION_RECEIVE:
            return $this->chunkSize[$direction];
        case self::DIRECTION_ALL:
            return $this->chunkSize;
        }
        return false;
    }

    /**
     * Sends a string or stream over the wrapped stream.
     * 
     * Sends a string or stream over the wrapped stream. If a seekable stream is
     * provided, it will be seeked back to the same position it was passed as,
     * regardless of the $offset parameter.
     * 
     * @param string|resource $contents The string or stream to send.
     * @param int             $offset   The offset from which to start sending.
     *     If a stream is provided, and this is set to NULL, sending will start
     *     from the current stream position.
     * @param int             $length   The maximum length to send. If omitted,
     *     the string/stream will be sent to its end.
     * 
     * @return int The number of bytes sent.
     */
    public function send($contents, $offset = null, $length = null)
    {
        $bytes = 0;
        $chunkSize = $this->chunkSize[self::DIRECTION_SEND];
        $lengthIsNotNull = null !== $length;
        $offsetIsNotNull = null !== $offset;
        if (self::isStream($contents)) {
            if ($offsetIsNotNull) {
                $oldPos = ftell($contents);
                fseek($contents, $offset, SEEK_SET);
            }
            while (!feof($contents)) {
                if ($lengthIsNotNull
                    && 0 === $chunkSize = min($chunkSize, $length - $bytes)
                ) {
                    break;
                }
                $bytesNow = @fwrite(
                    $this->stream,
                    fread($contents, $chunkSize)
                );
                if (0 != $bytesNow) {
                    $bytes += $bytesNow;
                } elseif ($this->isBlocking || false === $bytesNow) {
                    throw $this->createException(
                        'Failed while sending stream.',
                        2,
                        null,
                        $bytes
                    );
                } else {
                    usleep(300000);
                }
                $this->isAcceptingData(null);
            }
            if ($offsetIsNotNull) {
                fseek($contents, $oldPos, SEEK_SET);
            } else {
                fseek($contents, -$bytes, SEEK_CUR);
            }
        } else {
            $contents = (string) $contents;
            if ($offsetIsNotNull) {
                $contents = substr($contents, $offset);
            }
            if ($lengthIsNotNull) {
                $contents = substr($contents, 0, $length);
            }
            $bytesToSend = (double) sprintf('%u', strlen($contents));
            while ($bytes < $bytesToSend) {
                $bytesNow = @fwrite(
                    $this->stream,
                    substr($contents, $bytes, $chunkSize)
                );
                if (0 != $bytesNow) {
                    $bytes += $bytesNow;
                } elseif ($this->isBlocking || false === $bytesNow) {
                    throw $this->createException(
                        'Failed while sending string.',
                        3,
                        null,
                        $bytes
                    );
                } else {
                    usleep(300000);
                }
                $this->isAcceptingData(null);
            }
        }
        return $bytes;
    }

    /**
     * Reads from the wrapped stream to receive.
     * 
     * Reads from the wrapped stream to receive content as a string.
     * 
     * @param int    $length The number of bytes to receive.
     * @param string $what   Descriptive string about what is being received
     *     (used in exception messages).
     * 
     * @return string The received content.
     */
    public function receive($length, $what = 'data')
    {
        $result = '';
        $chunkSize = $this->chunkSize[self::DIRECTION_RECEIVE];
        while ($length > 0) {
            while ($this->isAvailable()) {
                $fragment = fread($this->stream, min($length, $chunkSize));
                if ('' != $fragment) {
                    $length -= strlen($fragment);
                    $result .= $fragment;
                    continue 2;
                } elseif (!$this->isBlocking && !(false === $fragment)) {
                    usleep(3000);
                    continue 2;
                }
            }
            throw $this->createException(
                "Failed while receiving {$what}",
                4,
                null,
                $result
            );
        }
        return $result;
    }

    /**
     * Reads from the wrapped stream to receive.
     * 
     * Reads from the wrapped stream to receive content as a stream.
     * 
     * @param int              $length  The number of bytes to receive.
     * @param FilterCollection $filters A collection of filters to apply to the
     *     stream while receiving. Note that the filters will not be present on
     *     the stream after receiving is done.
     * @param string           $what    Descriptive string about what is being
     *     received (used in exception messages).
     * 
     * @return resource The received content.
     */
    public function receiveStream(
        $length,
        FilterCollection $filters = null,
        $what = 'stream data'
    ) {
        $result = fopen('php://temp', 'r+b');
        $appliedFilters = array();
        if (null !== $filters) {
            foreach ($filters as $filtername => $params) {
                $appliedFilters[] = stream_filter_append(
                    $result,
                    $filtername,
                    STREAM_FILTER_WRITE,
                    $params
                );
            }
        }
        
        $chunkSize = $this->chunkSize[self::DIRECTION_RECEIVE];
        while ($length > 0) {
            while ($this->isAvailable()) {
                $fragment = fread($this->stream, min($length, $chunkSize));
                if ('' != $fragment) {
                    $length -= strlen($fragment);
                    fwrite($result, $fragment);
                    continue 2;
                } elseif (!$this->isBlocking && !(false === $fragment)) {
                    usleep(3000);
                    continue 2;
                }
            }

            foreach ($appliedFilters as $filter) {
                stream_filter_remove($filter);
            }
            rewind($result);
            throw $this->createException(
                "Failed while receiving {$what}",
                5,
                null,
                $result
            );
        }

        foreach ($appliedFilters as $filter) {
            stream_filter_remove($filter);
        }
        rewind($result);
        return $result;
    }

    /**
     * Checks whether the stream is available for operations.
     * 
     * For network streams, this means whether the other end has closed the
     * connection.
     * 
     * @return bool TRUE if the stream is available, FALSE otherwise.
     */
    public function isAvailable()
    {
        return self::isStream($this->stream) && !feof($this->stream);
    }

    /**
     * Checks whether there is data to be read from the wrapped stream.
     * 
     * @param int|null $sTimeout  If theere isn't data awaiting currently,
     *     wait for it this many seconds for data to arrive. If NULL is
     *     specified, wait indefinetly for that.
     * @param int      $usTimeout Microseconds to add to the waiting time.
     * 
     * @return bool TRUE if there is data to be read, FALSE otherwise.
     * @SuppressWarnings(PHPMD.ShortVariable)
     */
    public function isDataAwaiting($sTimeout = 0, $usTimeout = 0)
    {
        if (self::isStream($this->stream)) {
            if (null === $sTimeout && !$this->isBlocking) {
                $meta = stream_get_meta_data($this->stream);
                return !$meta['eof'];
            }

            $w = $e = null;
            $r = array($this->stream);
            return 1 === @/* due to PHP bug #54563 */stream_select(
                $r,
                $w,
                $e,
                $sTimeout,
                $usTimeout
            );
        }
        return false;
    }

    /**
     * Checks whether the wrapped stream can be written to without a block.
     * 
     * @param int|null $sTimeout  If the stream isn't currently accepting data,
     *     wait for it this many seconds to start accepting data. If NULL is
     *     specified, wait indefinetly for that.
     * @param int      $usTimeout Microseconds to add to the waiting time.
     * 
     * @return bool TRUE if the wrapped stream would not block on a write, FALSE
     *     otherwise.
     * @SuppressWarnings(PHPMD.ShortVariable)
     */
    public function isAcceptingData($sTimeout = 0, $usTimeout = 0)
    {
        if (self::isStream($this->stream)) {
            if (!$this->isBlocking) {
                $meta = stream_get_meta_data($this->stream);
                return !$meta['eof'];
            } elseif (feof($this->stream)) {
                return false;
            }

            $r = $e = null;
            $w = array($this->stream);
            return 1 === @/* due to PHP bug #54563 */stream_select(
                $r,
                $w,
                $e,
                $sTimeout,
                $usTimeout
            );
        }
        return false;
    }

    /**
     * Closes the opened stream, unless it's a persistent one.
     */
    public function __destruct()
    {
        if ((!$this->persist) && $this->autoClose) {
            $this->close();
        }
    }

    /**
     * Closes the opened stream, even if it is a persistent one.
     * 
     * @return bool TRUE on success, FALSE on failure.
     */
    public function close()
    {
        return self::isStream($this->stream) && fclose($this->stream);
    }

    /**
     * Creates a new exception.
     * 
     * Creates a new exception. Used by the rest of the functions in this class.
     * Override in derived classes for custom exception handling.
     * 
     * @param string                   $message  The exception message.
     * @param int                      $code     The exception code.
     * @param E|null                   $previous Previous exception thrown,
     *     or NULL if there is none.
     * @param int|string|resource|null $fragment The fragment up until the
     *     point of failure.
     *     On failure with sending, this is the number of bytes sent
     *     successfully before the failure.
     *     On failure when receiving, this is a string/stream holding
     *     the contents received successfully before the failure.
     * 
     * @return StreamException The exception to then be thrown.
     */
    protected function createException(
        $message,
        $code = 0,
        E $previous = null,
        $fragment = null
    ) {
        return new StreamException($message, $code, $previous, $fragment);
    }
}


File: /PEAR2\Net\Transmitter\StreamException.php
<?php

/**
 * Wrapper for network stream functionality.
 * 
 * PHP has built in support for various types of network streams, such as HTTP and TCP sockets. One problem that arises with them is the fact that a single fread/fwrite call might not read/write all the data you intended, regardless of whether you're in blocking mode or not. While the PHP manual offers a workaround in the form of a loop with a few variables, using it every single time you want to read/write can be tedious.

This package abstracts this away, so that when you want to get exactly N amount of bytes, you can be sure the upper levels of your app will be dealing with N bytes. Oh, and the functionality is nicely wrapped in an object (but that's just the icing on the cake).
 * 
 * PHP version 5
 * 
 * @category  Net
 * @package   PEAR2_Net_Transmitter
 * @author    Vasil Rangelov <boen.robot@gmail.com>
 * @copyright 2011 Vasil Rangelov
 * @license   http://www.gnu.org/copyleft/lesser.html LGPL License 2.1
 * @version   1.0.0a5
 * @link      http://pear2.php.net/PEAR2_Net_Transmitter
 */
/**
 * The namespace declaration.
 */
namespace PEAR2\Net\Transmitter;

/**
 * Base for this exception.
 */
use RuntimeException;

/**
 * Used to enable any exception in chaining.
 */
use Exception as E;

/**
 * Exception thrown when something goes wrong with the connection.
 * 
 * @category Net
 * @package  PEAR2_Net_Transmitter
 * @author   Vasil Rangelov <boen.robot@gmail.com>
 * @license  http://www.gnu.org/copyleft/lesser.html LGPL License 2.1
 * @link     http://pear2.php.net/PEAR2_Net_Transmitter
 */
class StreamException extends RuntimeException implements Exception
{
    /**
     * @var int|string|resource|null The fragment up until the point of failure.
     *     On failure with sending, this is the number of bytes sent
     *     successfully before the failure.
     *     On failure when receiving, this is a string/stream holding
     *     the contents received successfully before the failure.
     *     NULL if the failure occured before the operation started.
     */
    protected $fragment = null;

    /**
     * Creates a new stream exception.
     * 
     * @param string                   $message  The Exception message to throw.
     * @param int                      $code     The Exception code.
     * @param E|null                   $previous Previous exception thrown,
     *     or NULL if there is none.
     * @param int|string|resource|null $fragment The fragment up until the
     *     point of failure.
     *     On failure with sending, this is the number of bytes sent
     *     successfully before the failure.
     *     On failure when receiving, this is a string/stream holding
     *     the contents received successfully before the failure.
     *     NULL if the failure occured before the operation started.
     */
    public function __construct(
        $message,
        $code,
        E $previous = null,
        $fragment = null
    ) {
        parent::__construct($message, $code, $previous);
        $this->fragment = $fragment;
    }

    /**
     * Gets the stream fragment.
     * 
     * @return int|string|resource|null The fragment up until the
     *     point of failure.
     *     On failure with sending, this is the number of bytes sent
     *     successfully before the failure.
     *     On failure when receiving, this is a string/stream holding
     *     the contents received successfully before the failure.
     *     NULL if the failure occured before the operation started.
     */
    public function getFragment()
    {
        return $this->fragment;
    }

    // @codeCoverageIgnoreStart
    // Unreliable in testing.

    /**
     * Returns a string representation of the exception.
     * 
     * @return string The exception as a string.
     */
    public function __toString()
    {
        $result = parent::__toString();
        if (null !== $this->fragment) {
            $result .= "\nFragment: ";
            if (is_scalar($this->fragment)) {
                $result .= (string)$this->fragment;
            } else {
                $result .= stream_get_contents($this->fragment);
            }
        }
        return $result;
    }
    // @codeCoverageIgnoreEnd
}


File: /PEAR2\Net\Transmitter\TcpClient.php
<?php

/**
 * Wrapper for network stream functionality.
 * 
 * PHP has built in support for various types of network streams, such as HTTP and TCP sockets. One problem that arises with them is the fact that a single fread/fwrite call might not read/write all the data you intended, regardless of whether you're in blocking mode or not. While the PHP manual offers a workaround in the form of a loop with a few variables, using it every single time you want to read/write can be tedious.

This package abstracts this away, so that when you want to get exactly N amount of bytes, you can be sure the upper levels of your app will be dealing with N bytes. Oh, and the functionality is nicely wrapped in an object (but that's just the icing on the cake).
 * 
 * PHP version 5
 * 
 * @category  Net
 * @package   PEAR2_Net_Transmitter
 * @author    Vasil Rangelov <boen.robot@gmail.com>
 * @copyright 2011 Vasil Rangelov
 * @license   http://www.gnu.org/copyleft/lesser.html LGPL License 2.1
 * @version   1.0.0a5
 * @link      http://pear2.php.net/PEAR2_Net_Transmitter
 */
/**
 * The namespace declaration.
 */
namespace PEAR2\Net\Transmitter;

/**
 * Used for managing persistent connections.
 */
use PEAR2\Cache\SHM;

/**
 * Used for matching arbitrary exceptions in
 * {@link TcpClient::createException()} and releasing locks properly.
 */
use Exception as E;

/**
 * A socket transmitter.
 * 
 * This is a convinience wrapper for socket functionality. Used to ensure data
 * integrity.
 * 
 * @category Net
 * @package  PEAR2_Net_Transmitter
 * @author   Vasil Rangelov <boen.robot@gmail.com>
 * @license  http://www.gnu.org/copyleft/lesser.html LGPL License 2.1
 * @link     http://pear2.php.net/PEAR2_Net_Transmitter
 */
class TcpClient extends NetworkStream
{

    /**
     * @var int The error code of the last error on the socket.
     */
    protected $errorNo = 0;

    /**
     * @var string The error message of the last error on the socket.
     */
    protected $errorStr = null;
    
    /**
     * @var SHM Persistent connection handler. Remains NULL for non-persistent
     *     connections. 
     */
    protected $shmHandler = null;
    
    /**
     * @var array An array with all connections from this PHP request (as keys)
     *     and their lock state (as a value). 
     */
    protected static $lockState = array();
    
    protected static $cryptoScheme = array(
        parent::CRYPTO_OFF => 'tcp',
        parent::CRYPTO_SSL2 => 'sslv2',
        parent::CRYPTO_SSL3 => 'sslv3',
        parent::CRYPTO_SSL => 'ssl',
        parent::CRYPTO_TLS => 'tls'
    );
    
    /**
     * @var string The URI of this connection.
     */
    protected $uri;

    /**
     * Creates a new connection with the specified options.
     * 
     * @param string   $host    Hostname (IP or domain) of the server.
     * @param int      $port    The port on the server.
     * @param bool     $persist Whether or not the connection should be a
     *     persistent one.
     * @param float    $timeout The timeout for the connection.
     * @param string   $key     A string that uniquely identifies the
     *     connection.
     * @param string   $crypto  Encryption setting. Must be one of the
     *     NetworkStream::CRYPTO_* constants. By default, encryption is
     *     disabled. If the setting has an associated scheme for it, it will be
     *     used, and if not, the setting will be adjusted right after the
     *     connection is estabilished.
     * @param resource $context A context for the socket.
     */
    public function __construct(
        $host,
        $port,
        $persist = false,
        $timeout = null,
        $key = '',
        $crypto = parent::CRYPTO_OFF,
        $context = null
    ) {
        $this->streamType = '_CLIENT';

        if (strpos($host, ':') !== false) {
            $host = "[{$host}]";
        }
        $flags = STREAM_CLIENT_CONNECT;
        if ($persist) {
            $flags |= STREAM_CLIENT_PERSISTENT;
        }

        $timeout
            = null == $timeout ? ini_get('default_socket_timeout') : $timeout;

        $key = rawurlencode($key);

        if (null === $context) {
            $context = stream_context_get_default();
        } elseif ((!is_resource($context))
            || ('stream-context' !== get_resource_type($context))
        ) {
            throw $this->createException('Invalid context supplied.', 6);
        }
        $hasCryptoScheme = array_key_exists($crypto, static::$cryptoScheme);
        $scheme = $hasCryptoScheme ? static::$cryptoScheme[$crypto] : 'tcp';
        $this->uri = "{$scheme}://{$host}:{$port}/{$key}";
        set_error_handler(array($this, 'handleError'));
        try {
            parent::__construct(
                stream_socket_client(
                    $this->uri,
                    $this->errorNo,
                    $this->errorStr,
                    $timeout,
                    $flags,
                    $context
                )
            );
            restore_error_handler();
        } catch (E $e) {
            restore_error_handler();
            if (0 === $this->errorNo) {
                throw $this->createException(
                    'Failed to initialize socket.',
                    7,
                    $e
                );
            }
            throw $this->createException(
                'Failed to connect with socket.',
                8,
                $e
            );
        }

        if ($hasCryptoScheme) {
            $this->crypto = $crypto;
        } elseif (parent::CRYPTO_OFF !== $crypto) {
            $this->setCrypto($crypto);
        }
        $this->setIsBlocking(parent::CRYPTO_OFF === $crypto);

        if ($persist) {
            $this->shmHandler = SHM::factory(
                __CLASS__ . ' ' . $this->uri . ' '
            );
            self::$lockState[$this->uri] = self::DIRECTION_NONE;
        }
    }

    /**
     * Creates a new exception.
     * 
     * Creates a new exception. Used by the rest of the functions in this class.
     * 
     * @param string                   $message  The exception message.
     * @param int                      $code     The exception code.
     * @param E|null                   $previous Previous exception thrown,
     *     or NULL if there is none.
     * @param int|string|resource|null $fragment The fragment up until the
     *     point of failure.
     *     On failure with sending, this is the number of bytes sent
     *     successfully before the failure.
     *     On failure when receiving, this is a string/stream holding
     *     the contents received successfully before the failure.
     * 
     * @return SocketException The exception to then be thrown.
     */
    protected function createException(
        $message,
        $code = 0,
        E $previous = null,
        $fragment = null
    ) {
        return new SocketException(
            $message,
            $code,
            $previous,
            $fragment,
            $this->errorNo,
            $this->errorStr
        );
    }
    
    /**
     * Locks transmission.
     * 
     * Locks transmission in one or more directions. Useful when dealing with
     * persistent connections. Note that every send/receive call implicitly
     * calls this function and then restores it to the previous state. You only
     * need to call this function if you need to do an uninterrputed sequence of
     * such calls.
     * 
     * @param int  $direction The direction(s) to have locked. Acceptable values
     *     are the DIRECTION_* constants. If a lock for a direction can't be
     *     obtained immediatly, the function will block until one is aquired.
     *     Note that if you specify {@link DIRECTION_ALL}, the sending lock will
     *     be obtained before the receiving one, and if obtaining the receiving
     *     lock afterwards fails, the sending lock will be released too.
     * @param bool $replace   Whether to replace all locks with the specified
     *     ones. Setting this to FALSE will make the function only obtain the
     *     locks which are not already obtained.
     * 
     * @return int|false The previous state or FALSE if the connection is not
     *     persistent or arguments are invalid.
     */
    public function lock($direction = self::DIRECTION_ALL, $replace = false)
    {
        if ($this->persist && is_int($direction)) {
            $old = self::$lockState[$this->uri];

            if ($direction & self::DIRECTION_SEND) {
                if (($old & self::DIRECTION_SEND)
                    || $this->shmHandler->lock(self::DIRECTION_SEND)
                ) {
                    self::$lockState[$this->uri] |= self::DIRECTION_SEND;
                } else {
                    throw new LockException('Unable to obtain sending lock.');
                }
            } elseif ($replace) {
                if (!($old & self::DIRECTION_SEND)
                    || $this->shmHandler->unlock(self::DIRECTION_SEND)
                ) {
                    self::$lockState[$this->uri] &= ~self::DIRECTION_SEND;
                } else {
                    throw new LockException('Unable to release sending lock.');
                }
            }
            
            try {
                if ($direction & self::DIRECTION_RECEIVE) {
                    if (($old & self::DIRECTION_RECEIVE)
                        || $this->shmHandler->lock(self::DIRECTION_RECEIVE)
                    ) {
                        self::$lockState[$this->uri] |= self::DIRECTION_RECEIVE;
                    } else {
                        throw new LockException(
                            'Unable to obtain receiving lock.'
                        );
                    }
                } elseif ($replace) {
                    if (!($old & self::DIRECTION_RECEIVE)
                        || $this->shmHandler->unlock(self::DIRECTION_RECEIVE)
                    ) {
                        self::$lockState[$this->uri]
                            &= ~self::DIRECTION_RECEIVE;
                    } else {
                        throw new LockException(
                            'Unable to release receiving lock.'
                        );
                    }
                }
            } catch (LockException $e) {
                if ($direction & self::DIRECTION_SEND
                    && !($old & self::DIRECTION_SEND)
                ) {
                    $this->shmHandler->unlock(self::DIRECTION_SEND);
                }
                throw $e;
            }
            return $old;
        }
        return false;
    }
    

    /**
     * Sends a string or stream to the server.
     * 
     * Sends a string or stream to the server. If a seekable stream is
     * provided, it will be seeked back to the same position it was passed as,
     * regardless of the $offset parameter.
     * 
     * @param string|resource $contents The string or stream to send.
     * @param int             $offset   The offset from which to start sending.
     *     If a stream is provided, and this is set to NULL, sending will start
     *     from the current stream position.
     * @param int             $length   The maximum length to send. If omitted,
     *     the string/stream will be sent to its end.
     * 
     * @return int The number of bytes sent.
     */
    public function send($contents, $offset = null, $length = null)
    {
        if (false === ($previousState = $this->lock(self::DIRECTION_SEND))
            && $this->persist
        ) {
            throw $this->createException(
                'Unable to obtain sending lock',
                10
            );
        }
        try {
            $result = parent::send($contents, $offset, $length);
        } catch (E $e) {
            $this->lock($previousState, true);
            throw $e;
        }
        $this->lock($previousState, true);
        return $result;
    }

    /**
     * Receives data from the server.
     * 
     * Receives data from the server as a string.
     * 
     * @param int    $length The number of bytes to receive.
     * @param string $what   Descriptive string about what is being received
     *     (used in exception messages).
     * 
     * @return string The received content.
     */
    public function receive($length, $what = 'data')
    {
        if (false === ($previousState = $this->lock(self::DIRECTION_RECEIVE))
            && $this->persist
        ) {
            throw $this->createException(
                'Unable to obtain receiving lock',
                9
            );
        }
        try {
            $result = parent::receive($length, $what);
        } catch (E $e) {
            $this->lock($previousState, true);
            throw $e;
        }
        $this->lock($previousState, true);
        return $result;
    }

    /**
     * Receives data from the server.
     * 
     * Receives data from the server as a stream.
     * 
     * @param int              $length  The number of bytes to receive.
     * @param FilterCollection $filters A collection of filters to apply to the
     *     stream while receiving. Note that the filters will not be present on
     *     the stream after receiving is done.
     * @param string           $what    Descriptive string about what is being
     *     received (used in exception messages).
     * 
     * @return resource The received content.
     */
    public function receiveStream(
        $length,
        FilterCollection $filters = null,
        $what = 'stream data'
    ) {
        if (false === ($previousState = $this->lock(self::DIRECTION_RECEIVE))
            && $this->persist
        ) {
            throw $this->createException(
                'Unable to obtain receiving lock',
                9
            );
        }
        try {
            $result = parent::receiveStream($length, $filters, $what);
        } catch (E $e) {
            $this->lock($previousState, true);
            throw $e;
        }
        $this->lock($previousState, true);
        return $result;
    }
}


File: /PEAR2\Net\Transmitter\TcpServerConnection.php
<?php

/**
 * Wrapper for network stream functionality.
 * 
 * PHP has built in support for various types of network streams, such as HTTP and TCP sockets. One problem that arises with them is the fact that a single fread/fwrite call might not read/write all the data you intended, regardless of whether you're in blocking mode or not. While the PHP manual offers a workaround in the form of a loop with a few variables, using it every single time you want to read/write can be tedious.

This package abstracts this away, so that when you want to get exactly N amount of bytes, you can be sure the upper levels of your app will be dealing with N bytes. Oh, and the functionality is nicely wrapped in an object (but that's just the icing on the cake).
 * 
 * PHP version 5
 * 
 * @category  Net
 * @package   PEAR2_Net_Transmitter
 * @author    Vasil Rangelov <boen.robot@gmail.com>
 * @copyright 2011 Vasil Rangelov
 * @license   http://www.gnu.org/copyleft/lesser.html LGPL License 2.1
 * @version   1.0.0a5
 * @link      http://pear2.php.net/PEAR2_Net_Transmitter
 */
/**
 * The namespace declaration.
 */
namespace PEAR2\Net\Transmitter;

use Exception as E;

/**
 * A transmitter for connections to a socket server.
 * 
 * This is a convinience wrapper for functionality of socket server connections.
 * Used to ensure data integrity. Server handling is not part of the class in
 * order to allow its usage as part of various server implementations (e.g. fork
 * and/or sequential).
 * 
 * @category Net
 * @package  PEAR2_Net_Transmitter
 * @author   Vasil Rangelov <boen.robot@gmail.com>
 * @license  http://www.gnu.org/copyleft/lesser.html LGPL License 2.1
 * @link     http://pear2.php.net/PEAR2_Net_Transmitter
 */
class TcpServerConnection extends NetworkStream
{

    /**
     * @var string The IP address of the connected client.
     */
    protected $peerIP;

    /**
     * @var int The port of the connected client.
     */
    protected $peerPort;

    /**
     * Creates a new connection with the specified options.
     * 
     * @param resource $server  A socket server, created with
     * {@link stream_socket_server()}.
     * @param float    $timeout The timeout for the connection.
     */
    public function __construct($server, $timeout = null)
    {
        $this->streamType = '_SERVER';

        if (!self::isStream($server)) {
            throw $this->createException('Invalid server supplied.', 9);
        }
        $timeout
            = null == $timeout ? ini_get('default_socket_timeout') : $timeout;

        set_error_handler(array($this, 'handleError'));
        try {
            parent::__construct(
                stream_socket_accept($server, $timeout, $peername)
            );
            restore_error_handler();
            $portString = strrchr($peername, ':');
            $this->peerPort = (int) substr($portString, 1);
            $ipString = substr(
                $peername,
                0,
                strlen($peername) - strlen($portString)
            );
            if (strpos($ipString, '[') === 0
                && strpos(strrev($ipString), ']') === 0
            ) {
                $ipString = substr($ipString, 1, strlen($ipString) - 2);
            }
            $this->peerIP = $ipString;
        } catch (E $e) {
            restore_error_handler();
            throw $this->createException(
                'Failed to initialize connection.',
                10,
                $e
            );
        }
    }
    
    /**
     * Gets the IP address of the connected client.
     * 
     * @return string The IP address of the connected client.
     */
    public function getPeerIP()
    {
        return $this->peerIP;
    }
    
    /**
     * Gets the port of the connected client.
     * 
     * @return int The port of the connected client.
     */
    public function getPeerPort()
    {
        return $this->peerPort;
    }

    /**
     * Creates a new exception.
     * 
     * Creates a new exception. Used by the rest of the functions in this class.
     * 
     * @param string      $message  The exception message.
     * @param int         $code     The exception code.
     * @param E|null      $previous Previous exception thrown, or NULL if there
     *     is none.
     * @param string|null $fragment The fragment up until the point of failure.
     *     NULL if the failure occured before the operation started.
     * 
     * @return SocketException The exception to then be thrown.
     */
    protected function createException(
        $message,
        $code = 0,
        E $previous = null,
        $fragment = null
    ) {
        return new SocketException(
            $message,
            $code,
            $previous,
            $fragment
        );
    }
}


File: /readme.txt
Components/Packages/Scripts used in this project
-------------------------------------------------
Elevator  Metro UI Inspired Free Bootstrap HTML5 Template by graygrids.com
https://graygrids.com/item/elevator-metro-ui-inspired-responsive-bootstrap-template/

Twitter Bootstrap (& Jquery) http://getbootstrap.com/, https://jquery.com/
Font Awesome http://fontawesome.io/

Google Fonts http://fonts.googleapis.com/

Pear2 PHP API Client by boenrobot [Vasil Rangelov, a.k.a. boen_robot (boen [dot] robot [at] gmail [dot] com)]
https://github.com/pear2/Net_RouterOS
https://github.com/pear2/Net_RouterOS/wiki
https://wiki.mikrotik.com/wiki/API_PHP_package
http://pear2.php.net/support/
-------------------------------------------------
Developed by: Siby P Varkey, sibyperiyar@gmail.com
Assistance: Sonal Siby, sonusiby@gmail.com
-------------------------------------------------
Visual Documentation at : http://hotspot.zetozone.com
-------------------------------------------------
Software and Hardware

HTML, CSS, JavaScript, PHP, MySql, PDO, Javascript/Ajax, Font Awesome, JQuery, Twitter Bootstrap ... &  PEAR2_Net_RouterOS API are the major software component parts of the utility.  Above all the Mikrotik Router OS Based router or PC working with Router OS configured to an IP is the most important Hardware part involved.  

Requirements: Any web server supports PHP 5.x and all the above.
-------------------------------------------------
Prerequisites
A MySql database need to be created prior to operation, if it doesn't exist will be created automatically on initialization in most cases.

The details of the database need to be updated in the file 'dbconfig.php' file before operation. (Host, DB name, DB Username and DB Password)

The Details of the Router has to be entered in the 'config.php' file before operation, like Host IP, username and password.  If they are not correct or the system is not able to connect to the Hotspot router, will ask for correct credentials in the first screen.
-------------------------------------------------
System Users: Who are operating this utility.
3 User levels: Administrator, Unit Head and System users.
Any number of users can be created by the system Admin.  They can be enabled/disabled, edited, deleted and can reset the password also by the admin. A default system admin with username 'admin' and password 'admin' will be created automatically on initialisation. Admin user can reset passwords of all other users.  On resetting a password, it will be reset to 'password' for that user. All users can change their own password using the change password option available in the system users section.
-------------------------------------------------
Documentation and Help
For more details of the operations and features of the utility please refer the visual documentation available at http://hotspot.zetozone.com
-------------------------------------------------
Major features:

Creation of vouchers for Single person. (Guest User Accounts/Hotspot users)
Creation of vouchers for Multiple persons.
Listing Active Users
Listing inactive Users
Remove Selected/All User Accounts
Remove all validity expired User Accounts
Server Log of Recent Activities
Removal of uninitiated guest accounts.  Accounts created earlier but no one has started using it yet.
Voucher Management and Printing.  6 Different Voucher modes are available for Printing vouchers satisfying the needs of all.
Management of System user Accounts by Admin: Creation, Listing, Activation/Deactivation, Updating details and deletion of System users.
Hotspot User Profiles Management:  Creation/Updation/Deletion of User profiles in the router. Options like Session Timeout, MAC binding of Account, Expiry mode, grace period, price, MAC Cookie Timeout, Keepalive Timeout, Download and Upload Speed Limits, Number of simultaneous user logins allowed per user account etc can be set for each profile.
Re-printing of Last Voucher/Vouchers List.
and many more...
Please visit http://hotspot.zetozone.com for a detailed visual documentation of the project.
-------------------------------------------------
How to Install in different OS based PCs
Linux / Unix variations
................
..................
Windows Based PCs
................
..................
MAC OSX based MACs
................
..................
................
..................


File: /settings.php
<?php
	if (isset($_POST['btn_update'])){
		$newhost = $_POST['newhost'];
		$newuser = $_POST['newuser'];
		$newpass = $_POST['newpass'];
						
		$file = 'config.php';
		$message = '<?php '."\n";
		$message = $message.'$host = "'.$newhost.'";'."\n";
		$message = $message.'$user = "'.$newuser.'";'."\n";
		$message = $message.'$pass = "'.$newpass.'";'."\n";
		$message = $message."?>";
		try {
			file_put_contents($file, $message);
				echo '<script>cmodal("Success!", "Successfully saved the new settings!", "success", "index.php")</script>';
			}
		catch(PDOException $e) {
				echo '<script>cmodal("Access Denied!", "Error while updating settings!", "error", "index.php")</script>';
			}										
	}
?>
<div class="container">
	<header>
		<h1 style="text-align:center;">Easy Hotspot</h1>	
		<h2 style="text-align:center;">Simple HotSpot User Management Utility</h2>
		<h3 style="text-align:center;">By TEAM ZETOZONE</h3>
	</header>
	<div class="row">
		<div class="col-sm-6 col-sm-offset-3 well" style="box-shadow: 10px 10px 5px #888888;">
			<div class="panel panel-primary">
				<div class="panel panel-heading">
					<p><strong>Please update the below settings</strong></p>
				</div>
				<div class="panel-body">		
					<form class="form-horizontal" id="loginform" action="" method="POST">
						<div class="form-group form-group-sm">
							<label class="col-sm-2 control-label" for="txt_hostname">Host IP</label>
							<div class="col-sm-8">
								<input type="text" id="txt_hostname" name="newhost" placeholder="IP address of host" value="<?php echo $host; ?>" required class="form-control" autofocus>
							</div>
						</div>
						<div class="form-group form-group-sm">
							<label class="col-sm-2 control-label" for="txt_username">Username</label>
							<div class="col-sm-8">
								<input type="text" id="txt_username" name="newuser" placeholder="Registered Username" value="<?php echo $user; ?>" required class="form-control" autofocus>
							</div>
						</div>						
						<div class="form-group form-group-sm">
							<label class="col-sm-2 control-label" for="newpass">Password</label>
							<div class="col-sm-8">
								<input type="password" id="newpass" name="newpass" placeholder="Password" placeholder="Password" value="<?php echo $pass; ?>" required class="form-control">
							</div>
						</div>
						<div class="form-group form-group-sm">
							<div class="col-sm-2 col-sm-offset-4">
								<button id="btn_update" name="btn_update" type="submit" class="btn btn-primary">&nbsp;Submit</button>
							</div>
							<div class="col-sm-2">
								<button id="btn_cancel" name="btn_cancel" type="close" class="btn btn-success">&nbsp;Cancel</button>
							</div>
						</div>
					</form>
				</div>
			</div>
		</div>
	</div>
</div>

File: /voucher.php
<!DOCTYPE html>
<html lang="en">
<?php
include ('header.php');
if ( !isset($_SESSION) ) session_start(); ?>
<body>
	<div class="container" style="margin-top:50px;">
		<div class="no_print">
		<div class="row">
			<div class="col-sm-12 col-md-12 thumbnail" style="box-shadow: 10px 10px 5px #888888;">
				<div class="panel panel-primary">
					<div class="panel-heading"><h3 class="text-center">HotSpot User Voucher Printing</h3></div>
					<div class="panel-body">
						<form class="form-horizontal" method="post">
							<div class="alert alert-info text-center"><strong>Printing of last set of vouchers</strong></div>
							<div class="form-group">
								<div class="col-xs-4">
									<img src="images/shot1.png" width="240" height="100" class="center">
									<button name="voucher1" id="voucher1" class="btn btn-success center-element"  tabindex="1" title="Single Account Per Row(Plain List)">Single Account Per Row(Plain List)</button></a>
								</div>
								<div class="col-xs-4">
									<img src="images/shot2.png" width="240" height="100" class="center">
									<button name="voucher2" id="voucher2" class="btn btn-primary center-element"  tabindex="2" title="2 Accounts per Row(Plain List)">2 Accounts per Row(Plain List)</button>
								</div>
								<div class="col-xs-4">
									<img src="images/shot3.png" width="240" height="100" class="center">
									<button name="voucher3" id="voucher3"  class="btn btn-info center-element" title="Only use with Accounts having same username and password" tabindex="3">3 Accounts per Row(Plain List)</button>
								</div>
							</div>
							<div class="form-group">
								<div class="col-xs-4">
									<img src="images/shot4.png" width="240" height="100" class="center">
									<button name="voucher4" id="voucher4" class="btn btn-danger center-element" tabindex="4" title="2 Rows for Single Account(Plain List)">2 Rows for Single Account(Plain List)</button>
								</div>
								<div class="col-xs-4">
									<img src="images/shot5.png" width="240" height="100" class="center">
									<button name="voucher5" id="voucher5" class="btn btn-warning center-element" tabindex="5" title="Single Voucher/row - ID Card Format, Suitable for printing on envelope type sheets">Single Voucher/row - ID Card Format</button>
								</div>
								<div class="col-xs-4">
									<img src="images/shot6.png" width="240" height="100" class="center">
									<button name="voucher6" id="voucher6" class="btn btn-primary center-element" tabindex="5" title="3 Vouchers/row - ID Card Format, Suitable for printing on A4/similar size Sheets">3 Vouchers/row - ID Card Format</button>
								</div>
							</div>	
							<div class="form-group">
								<div class="col-xs-4 col-xs-offset-4">
									<button name="submit" type="submit" class="btn btn-success" tabindex="6"><i class="icon-save icon-large"></i>Reset</button>
									<button name="submit" type="submit" class="btn btn-primary" tabindex="7"><i class="icon-save icon-large"></i>Refresh Page</button>
									<a href="index.php" class="btn btn-danger" tabindex="8"><i class="icon-arrow-left icon-large"></i>Main Menu</a>
								</div>	
							</div>							
						</form>
					</div>
				</div>	
			</div>
		</div>
		</div>
<?php
if (isset($_POST['voucher1'])) {
	if (!(($_SESSION['user_level'] <= 3) AND ($_SESSION['user_level'] >= 1))) {
		echo '<script>cmodalOkCancel("Access Denied", "User Rights Issue,  Consult Administrator", "information", "index.php");</script>';
	}
else
	{
	include('dbconfig.php');
	$stmt = $DB_con->prepare("SELECT * FROM hotspot_vouchers WHERE status = :status");
	$stmt->execute(array(':status' => 'Active'));
	if ($stmt->rowCount() == 0) {
		echo '<script>cmodal("No Data Found","NO entries available meeting the current options, Try Selecting a different period", "error")</script>';
	}
	?>
	<div class="child-modal">
	<div class="row">
		<div class="col-sm-2 col-sm-offset-6"><button onclick="window.print();" class="btn btn-primary"><i class="icon-save icon-large"></i></a>&nbsp;PRINT</button></div>
		<div class="col-sm-12 col-md-12 thumbnail" style="box-shadow: 10px 10px 5px #888888;">
			<table cellpadding="0" cellspacing="0" border="1" class="table table-bordered" id="example">
				<caption class="text-center">HOTSPOT USER LIST - <?php echo date('d-m-Y'); ?></caption>
				<div class="alert alert-info">
					<h1 class="text-center"><strong>HotSpot User Voucher</strong></h1>
				</div>
				<thead>
					<tr>
						<th>#</th>
						<th></th>
						<th>Username</th>
						<th>Password</th>
						<th>Limit Uptime</th>
						<th>Limit Bytes</th>
						<th>Bandwidth Profile</th>
						
					</tr>
				</thead>
				<tbody>
					<?php
					$sn = 0;
					while($row = $stmt->fetch(PDO::FETCH_ASSOC)) {
						$sn += 1;
						$id = $row['id'];
						$limit_bytes = ($row['limit_bytes'] == 0) ? 'None' : $row['limit_bytes'].' Gb';
						echo '<tr>';
							echo '<td>'.$sn.'</td>';
							echo '<td><img src="images/success.png" width="50px" height="50px"></td>';
							echo '<td>Username: '.$row['user_name'].'</td>';
							echo '<td>Password: '.$row['password'].'</td>';
							echo '<td>Uptime Limit: '.$row['limit_uptime'].'ays</td>';
							echo '<td>Usage Limit: '.$limit_bytes.'</td>';
							echo '<td>Bandwidth Profile: '.$row['profile'].'</td>';
						echo '</tr>';
					}
					?>
				</tbody>
			</table>
		</div>
		<div class="col-sm-3 col-sm-offset-5">
			<button onclick="window.print();" class="btn btn-danger"><i class="icon-save icon-large"></i>PRINT</button>&nbsp;&nbsp;&nbsp;
			<button name="submit" type="submit" class="btn btn-success" tabindex="6"><i class="icon-save icon-large"></i>Reset</button>&nbsp;&nbsp;&nbsp;
			<a href="index.php" class="btn btn-info" tabindex="7"><i class="icon-arrow-left icon-large"></i>Main Menu</a>
		</div>						
	</div>
	</div>
	<?php
	}
}	?>
<?php 
if (isset($_POST['voucher2'])) {
	if (!(($_SESSION['user_level'] <= 3) AND ($_SESSION['user_level'] >= 1))) {
		echo '<script>cmodalOkCancel("Access Denied", "User Rights Issue,  Consult Administrator", "information", "index.php");</script>';
		}
	else
	{
	include('dbconfig.php');
	$stmt = $DB_con->prepare("SELECT * FROM hotspot_vouchers WHERE status = :status");
	$stmt->execute(array(':status' => 'Active'));
	if ($stmt->rowCount() == 0) {
		echo '<script>cmodal("No Data Found","NO entries available for Printing, Create Vouchers First from the Main menu, Add Multiple Users", "error")</script>';
	}
	?>
	<div class="child-modal">
	<div class="row">
		<div class="col-sm-2 col-sm-offset-6"><button onclick="window.print();" class="btn btn-primary"><i class="icon-save icon-large"></i></a>&nbsp;PRINT</button></div>
		<div class="col-sm-12 col-md-12 thumbnail" style="box-shadow: 10px 10px 5px #888888;">
			<table cellpadding="0" cellspacing="0" border="0" class="table table-bordered" id="example">
				<caption class="text-center">HOTSPOT USER LIST - <?php echo date('d-m-Y'); ?></caption>
				<div class="alert alert-info">
					<h1 class="text-center"><strong>HotSpot User Voucher - 2 in 1 Row(Plain)</strong></h1>
				</div>
				<thead>
					<tr>
						<th>#</th>
						<th></th>
						<th>Username</th>
						<th>Password</th>
						<th></th>
						<th>#</th>
						<th></th>
						<th>Username</th>
						<th>Password</th>
					</tr>
				</thead>
				<tbody>
					<?php 
					$sn = 0;
					while($row = $stmt->fetch(PDO::FETCH_ASSOC)) {
						$sn += 1;
						$id = $row['id'];
						$limit_bytes = ($row['limit_bytes'] == 0) ? 'None' : $row['limit_bytes'].' Gb';
						echo '<tr>';
							echo '<td>'.$sn.'</td>';
							echo '<td><img src="images/success.png" width="50px" height="50px"></td>';
							echo '<td>Username: '.$row['user_name'].'</td>';
							echo '<td>Password: '.$row['password'].'</td>';
							echo '<td></td>';
							if ($row = $stmt->fetch(PDO::FETCH_ASSOC)) {
								$sn += 1;
								$limit_bytes = ($row['limit_bytes'] == 0) ? 'None' : $row['limit_bytes'].' Gb';
								echo '<td>'.$sn.'</td>';
								echo '<td><img src="images/success.png" width="50px" height="50px"></td>';
								echo '<td>Username: '.$row['user_name'].'</td>';
								echo '<td>Password: '.$row['password'].'</td>';
							}	
						echo '</tr>';
					}
					?>
				</tbody>
			</table>
		</div>
		<div class="col-sm-3 col-sm-offset-5">
			<button onclick="window.print();" class="btn btn-danger"><i class="icon-save icon-large"></i>PRINT</button>&nbsp;&nbsp;&nbsp;
			<button name="submit" type="submit" class="btn btn-success" tabindex="6"><i class="icon-save icon-large"></i>Reset</button>&nbsp;&nbsp;&nbsp;
			<a href="index.php" class="btn btn-info" tabindex="7"><i class="icon-arrow-left icon-large"></i>Main Menu</a>
		</div>						
	</div>
	</div>
	<?php
	}
}
?>
<?php 
if (isset($_POST['voucher3'])) { //3 Units per Line, For Same Username and Password Accounts
	if (!(($_SESSION['user_level'] <= 3) AND ($_SESSION['user_level'] >= 1))) {
		echo '<script>cmodalOkCancel("Access Denied", "User Rights Issue,  Consult Administrator", "information", "index.php");</script>';
		}
	else
	{
	include('dbconfig.php');
	$stmt = $DB_con->prepare("SELECT * FROM hotspot_vouchers WHERE status = :status");
	$stmt->execute(array(':status' => 'Active'));
	if ($stmt->rowCount() == 0) {
		echo '<script>cmodal("No Data Found","NO entries available for Printing, Create Vouchers First from the Main menu, Add Multiple Users", "error")</script>';
	}
	?>
	<div class="child-modal">
	<div class="row">
		<div class="col-sm-2 col-sm-offset-6"><button onclick="window.print();" class="btn btn-primary"><i class="icon-save icon-large"></i></a>&nbsp;PRINT</button></div>
		<div class="col-sm-12 col-md-12 thumbnail" style="box-shadow: 10px 10px 5px #888888;">
			<table cellpadding="0" cellspacing="0" border="0" class="table table-bordered" id="example">
				<caption class="text-center">HOTSPOT USER LIST - <?php echo date('d-m-Y'); ?></caption>
				<div class="alert alert-info">
					<h1 class="text-center"><strong>HotSpot User Voucher - 3 in 1 Row(Plain, For Same Username & Password Accounts)</strong></h1>
				</div>
				<thead>
					<tr>
						<th>#</th>
						<th></th>
						<th>Details</th>
						<th></th>
						<th>#</th>
						<th></th>
						<th>Details</th>
						<th></th>
						<th>#</th>
						<th></th>
						<th>Details</th>
					</tr>
				</thead>
				<tbody>
					<?php 
					$sn = 0;
					while($row = $stmt->fetch(PDO::FETCH_ASSOC)) {
						$sn += 1;
						$id = $row['id'];
						$limit_bytes = ($row['limit_bytes'] == 0) ? 'None' : $row['limit_bytes'].' Gb';
						echo '<tr>';
							echo '<td>'.$sn.'</td>';
							echo '<td><img src="images/success.png" width="50px" height="50px"></td>';
							echo '<td>ID & Psd: '.$row['user_name'].'</td>';
							echo '<td></td>';
							if ($row = $stmt->fetch(PDO::FETCH_ASSOC)) {
								$sn += 1;
								$limit_bytes = ($row['limit_bytes'] == 0) ? 'None' : $row['limit_bytes'].' Gb';
								echo '<td>'.$sn.'</td>';
								echo '<td><img src="images/success.png" width="50px" height="50px"></td>';
								echo '<td>ID & Psd: '.$row['user_name'].'</td>';
								echo '<td></td>';
							}	
							if ($row = $stmt->fetch(PDO::FETCH_ASSOC)) {
								$sn += 1;
								$limit_bytes = ($row['limit_bytes'] == 0) ? 'None' : $row['limit_bytes'].' Gb';
								echo '<td>'.$sn.'</td>';
								echo '<td><img src="images/success.png" width="50px" height="50px"></td>';
								echo '<td>ID & Psd: '.$row['user_name'].'</td>';
							}	
						echo '</tr>';
					}
					?>
				</tbody>
			</table>
		</div>
		<div class="col-sm-3 col-sm-offset-5">
			<button onclick="window.print();" class="btn btn-danger"><i class="icon-save icon-large"></i>PRINT</button>&nbsp;&nbsp;&nbsp;
			<button name="submit" type="submit" class="btn btn-success" tabindex="6"><i class="icon-save icon-large"></i>Reset</button>&nbsp;&nbsp;&nbsp;
			<a href="index.php" class="btn btn-info" tabindex="7"><i class="icon-arrow-left icon-large"></i>Main Menu</a>
		</div>						
	</div>
	</div>
	<?php
	}
}
?>
<?php
if (isset($_POST['voucher4'])) { //1 Account per 2 Rows; Little decorative
	if (!(($_SESSION['user_level'] <= 3) AND ($_SESSION['user_level'] >= 1))) {
		echo '<script>cmodalOkCancel("Access Denied", "User Rights Issue,  Consult Administrator", "information", "index.php");</script>';
	}
else
	{
	include('dbconfig.php');
	$stmt = $DB_con->prepare("SELECT * FROM hotspot_vouchers WHERE status = :status");
	$stmt->execute(array(':status' => 'Active'));
	if ($stmt->rowCount() == 0) {
		echo '<script>cmodal("No Data Found","NO entries available meeting the current options, Try Selecting a different period", "error")</script>';
	}
	?>
	<div class="child-modal">
	<div class="row">
		<div class="col-sm-2 col-sm-offset-6"><button onclick="window.print();" class="btn btn-primary"><i class="icon-save icon-large"></i></a>&nbsp;PRINT</button></div>
		<div class="col-sm-12 col-md-12 thumbnail" style="box-shadow: 10px 10px 5px #888888;">
			<table cellpadding="0" cellspacing="0" border="2" class="table table-bordered" id="table-01">
				<caption class="text-center">HOTSPOT USER LIST - <?php echo date('d-m-Y'); ?></caption>
				<div class="alert alert-info">
					<h1 class="text-center"><strong>HotSpot User Voucher - 1 Account spanning 2 rows</strong></h1>
				</div>
				<thead>
					<tr>
						<th>#</th>
						<th></th>
						<th>Username</th>
						<th>Password</th>
						<th>Description</th>
					</tr>
				</thead>
				<tbody>
					<?php
					$sn = 0;
					while($row = $stmt->fetch(PDO::FETCH_ASSOC)) {
						$sn += 1;
						$id = $row['id'];
						$limit_bytes = ($row['limit_bytes'] == 0) ? 'None' : $row['limit_bytes'].' Gb';
						echo '<tr>';
							echo '<td rowspan="2">'.$sn.'</td>';
							echo '<td rowspan="2"><img src="images/success.png" width="50px" height="50px"></td>';
							echo '<td>Username: '.$row['user_name'].'</td>';
							echo '<td>Password: '.$row['password'].'</td>';
							echo '<td><strong>Counting Starts from 1st Login</strong></td>';
							echo '</tr>';
							echo '<tr>';
							echo '<td>Uptime Limit: '.$row['limit_uptime'].'ays</td>';
							echo '<td>Usage Limit: '.$limit_bytes.'</td>';
							echo '<td>Bandwidth Profile: '.$row['profile'].'</td>';
						echo '</tr>';
					}
					?>
				</tbody>
			</table>
		</div>
		<div class="col-sm-3 col-sm-offset-5">
			<button onclick="window.print();" class="btn btn-danger"><i class="icon-save icon-large"></i>PRINT</button>&nbsp;&nbsp;&nbsp;
			<button name="submit" type="submit" class="btn btn-success" tabindex="6"><i class="icon-save icon-large"></i>Reset</button>&nbsp;&nbsp;&nbsp;
			<a href="index.php" class="btn btn-info" tabindex="7"><i class="icon-arrow-left icon-large"></i>Main Menu</a>
		</div>						
	</div>
	</div>
	<?php
	}
}	?>

<?php
if (isset($_POST['voucher5'])) { //1 Account per Card Format; Little decorative
	if (!(($_SESSION['user_level'] <= 3) AND ($_SESSION['user_level'] >= 1))) {
		echo '<script>cmodalOkCancel("Access Denied", "User Rights Issue,  Consult Administrator", "information", "index.php");</script>';
	}
else
	{
	include('dbconfig.php');
	$stmt = $DB_con->prepare("SELECT * FROM hotspot_vouchers WHERE status = :status");
	$stmt->execute(array(':status' => 'Active'));
	if ($stmt->rowCount() == 0) {
		echo '<script>cmodal("No Data Found","NO entries available meeting the current options, Try Selecting a different period", "error")</script>';
	}
	echo '<div class="col-sm-6 col-sm-offset-5">
			<button onclick="window.print();" class="btn btn-danger"><i class="icon-save icon-large"></i>PRINT</button>&nbsp;&nbsp;&nbsp;
			<button name="submit" type="submit" class="btn btn-success" tabindex="6"><i class="icon-save icon-large"></i>Reset</button>&nbsp;&nbsp;&nbsp;
			<a href="index.php" class="btn btn-info" tabindex="7"><i class="icon-arrow-left icon-large"></i>Main Menu</a>
		</div>';
		
	$sn = 0;
	echo '<div class="card-deck">';
	while($row = $stmt->fetch(PDO::FETCH_ASSOC)) {
		$sn += 1;
		$id = $row['id'];
		$limit_bytes = ($row['limit_bytes'] == 0) ? 'None' : $row['limit_bytes'].' Gb';
		?>
		<div class="row">
			<div class="col-sm-4">
				<div class="card card-inverse">
					<img class="card-img-top" src="images/logo.png" style="background-origin: content-box; background-size: cover; border-radius: 10px 10px 0px 0px;" alt="Card image/Logo">
					<div class="card-img-overlay">
						<h6 class="card-title text-center">WIFI HOTSPOT</h6>
						<ul class="list-group list-group-flush">
							<li class="list-group-item">ID: <?php echo $sn.' ['.$row['uid'].']'; ?></li>
							<li class="list-group-item">User Name: <?php echo $row['user_name']; ?></li>
							<li class="list-group-item">Password : <?php echo $row['password']; ?></li>
							<li class="list-group-item">Uptime Limit : <?php echo $row['limit_uptime']; ?>ays</li>
							<li class="list-group-item">Usage Limit  : <?php echo $limit_bytes; ?></li>
							<li class="list-group-item">Bandwidth Profile  : <?php echo $row['profile']; ?></li>
						</ul>
					</div>
				</div>	
			</div>
		</div>	
		<?php
		}
		?>
		</div>
		<div class="col-sm-6 col-sm-offset-5">
			<button onclick="window.print();" class="btn btn-danger"><i class="icon-save icon-large"></i>PRINT</button>&nbsp;&nbsp;&nbsp;
			<button name="submit" type="submit" class="btn btn-success" tabindex="6"><i class="icon-save icon-large"></i>Reset</button>&nbsp;&nbsp;&nbsp;
			<a href="index.php" class="btn btn-info" tabindex="7"><i class="icon-arrow-left icon-large"></i>Main Menu</a>
		</div>						
	</div>
	<?php
	}
}	?>


<?php
if (isset($_POST['voucher6'])) { //Card Format;
	if (!(($_SESSION['user_level'] <= 3) AND ($_SESSION['user_level'] >= 1))) {
		echo '<script>cmodalOkCancel("Access Denied", "User Rights Issue,  Consult Administrator", "information", "index.php");</script>';
	}
else
	{
	include('dbconfig.php');
	$stmt = $DB_con->prepare("SELECT * FROM hotspot_vouchers WHERE status = :status");
	$stmt->execute(array(':status' => 'Active'));
	if ($stmt->rowCount() == 0) {
		echo '<script>cmodal("No Data Found","NO entries available meeting the current options, Try Selecting a different period", "error")</script>';
	}
	echo '<div class="col-xs-6 col-xs-offset-5">
			<button onclick="window.print();" class="btn btn-danger"><i class="icon-save icon-large"></i>PRINT</button>&nbsp;&nbsp;&nbsp;
			<button name="submit" type="submit" class="btn btn-success" tabindex="6"><i class="icon-save icon-large"></i>Reset</button>&nbsp;&nbsp;&nbsp;
			<a href="index.php" class="btn btn-info" tabindex="7"><i class="icon-arrow-left icon-large"></i>Main Menu</a>
		</div>';
		
	$sn = 0;
	echo '<div class="card-deck-wrapper">
	<div class="card-deck">';
	while($row = $stmt->fetch(PDO::FETCH_ASSOC)) {
		$sn += 1;
		$id = $row['id'];
		$limit_bytes = ($row['limit_bytes'] == 0) ? 'None' : $row['limit_bytes'].' Gb';
		?>
		<div class="row">
			<div class="col-xs-4">
				<div class="card card-inverse">
					<img class="card-img-top" src="images/logo.png" style="background-origin: content-box; background-size: cover; border-radius: 10px 10px 0px 0px;" alt="Card image/Logo">
					<div class="card-img-overlay">
						<h6 class="card-title text-center">WIFI HOTSPOT</h6>
						<div class="card-block">
							<ul class="list-group list-group-flush">
								<li class="list-group-item">ID: <?php echo $sn.' ['.$row['uid'].']'; ?></li>
								<li class="list-group-item">User Name: <?php echo $row['user_name']; ?></li>
								<li class="list-group-item">Password : <?php echo $row['password']; ?></li>
								<li class="list-group-item">Uptime Limit : <?php echo $row['limit_uptime']; ?>ays</li>
								<li class="list-group-item">Usage Limit  : <?php echo $limit_bytes; ?></li>
								<li class="list-group-item">Bandwidth Profile  : <?php echo $row['profile']; ?></li>
							</ul>
						</div>
					</div>	
				</div>
			</div>		
			<?php if($row = $stmt->fetch(PDO::FETCH_ASSOC)) {
			$sn += 1;
			$limit_bytes = ($row['limit_bytes'] == 0) ? 'None' : $row['limit_bytes'].' Gb';
			?>
			<div class="col-xs-4">
				<div class="card card-inverse">
					<img class="card-img-top" src="images/logo.png" style="background-origin: content-box; background-size: cover; border-radius: 10px 10px 0px 0px;" alt="Card image/Logo">
					<div class="card-img-overlay">
						<h6 class="card-title text-center">WIFI HOTSPOT</h6>
						<div class="card-block">
							<ul class="list-group list-group-flush">
								<li class="list-group-item">ID: <?php echo $sn.' ['.$row['uid'].']'; ?></li>
								<li class="list-group-item">User Name: <?php echo $row['user_name']; ?></li>
								<li class="list-group-item">Password : <?php echo $row['password']; ?></li>
								<li class="list-group-item">Uptime Limit : <?php echo $row['limit_uptime']; ?>ays</li>
								<li class="list-group-item">Usage Limit  : <?php echo $limit_bytes; ?></li>
								<li class="list-group-item">Bandwidth Profile  : <?php echo $row['profile']; ?></li>
							</ul>
						</div>
					</div>	
				</div>
			</div>
			<?php } ?>
			<?php  if($row = $stmt->fetch(PDO::FETCH_ASSOC)) {
			$sn += 1;
			$limit_bytes = ($row['limit_bytes'] == 0) ? 'None' : $row['limit_bytes'].' Gb';
			?>			
			<div class="col-xs-4">
				<div class="card card-inverse">
					<img class="card-img-top" src="images/logo.png" style="background-origin: content-box; background-size: cover; border-radius: 10px 10px 0px 0px;" alt="Card image/Logo">
					<div class="card-img-overlay">
						<h6 class="card-title text-center">WIFI HOTSPOT</h6>
						<div class="card-block">
							<ul class="list-group list-group-flush">
								<li class="list-group-item">ID: <?php echo $sn.' ['.$row['uid'].']'; ?></li>
								<li class="list-group-item">User Name: <?php echo $row['user_name']; ?></li>
								<li class="list-group-item">Password : <?php echo $row['password']; ?></li>
								<li class="list-group-item">Uptime Limit : <?php echo $row['limit_uptime']; ?>ays</li>
								<li class="list-group-item">Usage Limit  : <?php echo $limit_bytes; ?></li>
								<li class="list-group-item">Bandwidth Profile  : <?php echo $row['profile']; ?></li>
							</ul>
						</div>
					</div>	
				</div>
			</div>
		</div>	
		<?php
			}
	}
	echo '</div>';
	echo '</div>';
	?>
	<div class="col-xs-6 col-xs-offset-5">
		<button onclick="window.print();" class="btn btn-danger"><i class="icon-save icon-large"></i>PRINT</button>&nbsp;&nbsp;&nbsp;
		<button name="submit" type="submit" class="btn btn-success" tabindex="6"><i class="icon-save icon-large"></i>Reset</button>&nbsp;&nbsp;&nbsp;
		<a href="index.php" class="btn btn-info" tabindex="7"><i class="icon-arrow-left icon-large"></i>Main Menu</a>
	</div>						
</div>
<?php
}
}	?>
	</div>
</body>

