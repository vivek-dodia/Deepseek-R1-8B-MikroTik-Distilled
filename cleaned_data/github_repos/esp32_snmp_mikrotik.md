# Repository Information
Name: esp32_snmp_mikrotik

# Directory Structure
Directory structure:
└── github_repos/esp32_snmp_mikrotik/
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
    │   │       ├── pack-e8ea87f4e6332311d6ec0ad8d9fdd8b74061c602.idx
    │   │       └── pack-e8ea87f4e6332311d6ec0ad8d9fdd8b74061c602.pack
    │   ├── packed-refs
    │   └── refs/
    │       ├── heads/
    │       │   └── main
    │       ├── remotes/
    │       │   └── origin/
    │       │       └── HEAD
    │       └── tags/
    ├── esp32_mikrotik.ino
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
	url = https://github.com/dmytro-korzhov/esp32_snmp_mikrotik.git
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
0000000000000000000000000000000000000000 000030ed8f0f18f6cd1fea4db7c2c99450e0e23b vivek-dodia <vivek.dodia@icloud.com> 1738606363 -0500	clone: from https://github.com/dmytro-korzhov/esp32_snmp_mikrotik.git


File: /.git\logs\refs\heads\main
0000000000000000000000000000000000000000 000030ed8f0f18f6cd1fea4db7c2c99450e0e23b vivek-dodia <vivek.dodia@icloud.com> 1738606363 -0500	clone: from https://github.com/dmytro-korzhov/esp32_snmp_mikrotik.git


File: /.git\logs\refs\remotes\origin\HEAD
0000000000000000000000000000000000000000 000030ed8f0f18f6cd1fea4db7c2c99450e0e23b vivek-dodia <vivek.dodia@icloud.com> 1738606363 -0500	clone: from https://github.com/dmytro-korzhov/esp32_snmp_mikrotik.git


File: /.git\packed-refs
# pack-refs with: peeled fully-peeled sorted 
000030ed8f0f18f6cd1fea4db7c2c99450e0e23b refs/remotes/origin/main


File: /.git\refs\heads\main
000030ed8f0f18f6cd1fea4db7c2c99450e0e23b


File: /.git\refs\remotes\origin\HEAD
ref: refs/remotes/origin/main


File: /esp32_mikrotik.ino
#include <TimeLib.h>
#include <WiFi.h>
#include <Arduino_SNMP.h>
#include <ESP32Ping.h>
#include <WebServer.h>
#include <ESPmDNS.h>
#include <Update.h>
#include "OneWire.h"
#include "DallasTemperature.h"
#include "U8g2lib.h"
#include "driver/gpio.h"

// конфигурация OLED дисплея
U8G2_SSD1322_NHD_256X64_F_4W_SW_SPI u8g2(U8G2_R0, 18, 23, 5, 13, 14);

// переменные для вольтметра
int analogvalue;
float input_volt = 0.0;
float temp=0.0;
float r1=82400.0; //сопротивление резистора r1
float r2=7000.0; // сопротивление резистора r2


// Порт GPIO с кнопкой смены сим
#define PIN_BUTTON 36
// Порт GPIO c кнопкой выключения дисплея
#define PIN_DISPLAY_OFF 34
// Порт GPIO c кнопкой контраста дисплея
#define PIN_CONTRAST 16
// Порт GPIO с температурными сенсорами
#define ONE_WIRE_BUS 15
// Порт ADC для подключения вольтметра
#define voltpin 33
//кнопка брелка 1
#define starlineremote_1 27
//кнопка брелка 2
#define starlineremote_2 26
//кнопка брелка 3
#define starlineremote_3 25
// Минимальный таймаут между событиями нажатия кнопки
#define TM_BUTTON 1000



// Настраиваем экземпляр oneWire для связи с устройством OneWire
OneWire oneWire(ONE_WIRE_BUS);
DallasTemperature sensors(&oneWire);

// Адреса температурных датчиков
DeviceAddress sensor_out = { 0x28, 0x23, 0x2C, 0xEA, 0xC, 0x0, 0x0, 0xC1 };
DeviceAddress sensor_int = { 0x28, 0xDB, 0xE6, 0xEA, 0xC, 0x0, 0x0, 0x8D };
void gettemp();

// настройки подключения к wi-fi
const char* host = "esp32";
const char* ssid = "Waflya";
const char* password = "9032330866";

//переменные для SNMP time
const int timezone = 3;
unsigned int snmptime = 0;
void printDigits(int digits);
void getSNMPtime();

//описание массива для корректного отображения календаря
const char *calendar[2][13] = {
  {0, "января", "февраля", "марта", "апреля", "мая", "июня", "июля", "августа", "сентября", "октября", "ноября", "декабря"},
  {0, "воскресение", "понедельник", "вторник", "среда", "четверг", "пятница", "суббота"},
};


//переменные для кнопки
uint32_t ms_btn = 0;
bool state_btn  = true;
void taskButton1( void *pvParameters );
SemaphoreHandle_t btn1Semaphore;
void change_sim();
int pwrs;
int contrast;

// переменные для SNMP
unsigned int rsrp = 0; //уровень сигнала
char ChangeSim[250]; //запуск скрипта смены сим-карты
char * changesim = ChangeSim;
//unsigned int sinr = 0; //уровень SINR
unsigned long timeLast = 0;

//промежуточные переменные для корректного вывода на дисплеей
String OperatorCode;
String CountryCode;
char* Operator;
char* Country;
String PrintRSRP;
int countryIndex;
int operatorIndex;
String PrintDate;
char printdate[40];
int printdatex;
String OperCount;
char opercount[15];
int printopercount;
String PrintTemp;
char printtemp[8];
int printtempx;
int forreboot = 0;

//описание массива вида [страна][оператор] для определения и вывода на дисплей имя сотового оператора
const char *operators[3][100] = {
  {0},
  {0, "MTS", "MegaFon", "NSS", 0, "ETK", "SkyLink", "Letay", "Vainah", "SkyLink", "DTC", "YOTA", "Baikal", "KUGSM", "MegaFon", "Smarts", "Miatel", "Utel", 0, 0, "Tele2", 0, 0, "Mobikom", 0, 0, 0, "Letay", "BeeLine", 0, 0, 0, 0, 0, 0, "Motiv", 0, 0, "Tambov-GSM", "Utel", 0, 0, "MTT", 0, 0, 0, 0, 0, "V-Tell", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "Tinkoff", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "BeeLine"},
  {0, "Vodafone", "BeeLine", "KyivStar", "Intertelekom", "GoldenTelekom", "Life:)", "Trimob", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "Telesystems", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "GoldenTelekom", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "Vodafone", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "KyivStar", "BeeLine", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "Phoenix"},
};


char Imsi[250]; //IMSI для получения кода оператора и страны
char * imsi = Imsi; //указатель char, используемый для ссылки на строку
int timeDelay = 5000; //задержка snmp-запросов в миллисекундах

// инициализация объектов, необходимых для SNMP
WiFiUDP Udp; // UDP используется для отправки и приема пакетов

SNMPAgent snmp = SNMPAgent("behemo");  // SNMP стартует с коммьюнити 'behemoth'
SNMPGet GetRequestImsi = SNMPGet("behemo", 0); 
SNMPGet GetRequestRsrp = SNMPGet("behemo", 0);
SNMPGet GetRequestChangeSim = SNMPGet("behemo", 0);
SNMPGet GetRequestTime = SNMPGet("behemo", 0);
//SNMPGet GetRequestSinr = SNMPGet("behemo", 0);
ValueCallback* callbackImsi;
ValueCallback* callbackRsrp;
ValueCallback* callbackTime;
ValueCallback* callbackChangeSim;
//ValueCallback* callbackSinr;

IPAddress netAdd = IPAddress(192,168,100,24); //IP-адрес устройства, с которого вы хотите получать информацию

WebServer server(80);

/*
 * Login page
 */

const char* loginIndex =
 "<form name='loginForm'>"
    "<table width='20%' bgcolor='A09F9F' align='center'>"
        "<tr>"
            "<td colspan=2>"
                "<center><font size=4><b>ESP32 Login Page</b></font></center>"
                "<br>"
            "</td>"
            "<br>"
            "<br>"
        "</tr>"
        "<tr>"
             "<td>Username:</td>"
             "<td><input type='text' size=25 name='userid'><br></td>"
        "</tr>"
        "<br>"
        "<br>"
        "<tr>"
            "<td>Password:</td>"
            "<td><input type='Password' size=25 name='pwd'><br></td>"
            "<br>"
            "<br>"
        "</tr>"
        "<tr>"
            "<td><input type='submit' onclick='check(this.form)' value='Login'></td>"
        "</tr>"
    "</table>"
"</form>"
"<script>"
    "function check(form)"
    "{"
    "if(form.userid.value=='admin' && form.pwd.value=='admin')"
    "{"
    "window.open('/serverIndex')"
    "}"
    "else"
    "{"
    " alert('Error Password or Username')/*displays error message*/"
    "}"
    "}"
"</script>";

/*
 * 
 * Server Index Page
 */
char* serverIndex =
"<div id='metrics' style='height: 400px;font-size: 500%;'></div>"
  "<form action='/startengine' method='get'>"
    "<input style='width: 99.5%;height: 80px;background:#8d95f3;cursor:pointer;border-radius: 5px;font-size:60px;font-weight:bold;margin: 5px' type='submit' value='Start Engine'>"
  "</form>"
  "<form action='/open' method='get'>"
    "<input style='width: 45%;height: 80px;background:#f38d8d;cursor:pointer;border-radius: 5px;float: left;font-size:40px;font-weight:bold;margin: 5px' type='submit' value='Open Behemoth'>"
  "</form>"
  "<form action='/close' method='get'>"
    "<input style='width: 45%;height: 80px;background:#8df39e;cursor:pointer;border-radius: 5px;float: right;font-size:40px;font-weight:bold;margin: 5px' type='submit' value='Close Behemoth'><br>"
  "</form>"
  "<form action='/find' method='get'>"
    "<input style='width: 45%;height: 80px;background:#f2ff33;cursor:pointer;border-radius: 5px;float: left;font-size:40px;font-weight:bold;margin: 5px' type='submit' value='Find Behemoth'>"
  "</form>"
  "<form action='/changesim' method='get'>"
    "<input style='width: 45%;height: 80px;background:#18d4ff;cursor:pointer;border-radius: 5px;float: right;font-size:40px;font-weight:bold;margin: 5px' type='submit' value='Change SIM'>"
  "</form>"
  "<form action='/stopengine' method='get'>"
    "<input style='width: 99.5%;height: 80px;background:#ff0000;cursor:pointer;border-radius: 5px;font-size:60px;font-weight:bold;margin: 5px' type='submit' value='Stop Engine'>"
  "</form>"
  "<script src='https://ajax.googleapis.com/ajax/libs/jquery/3.2.1/jquery.min.js'></script>"
  "<form method='POST' action='#' enctype='multipart/form-data' id='upload_form'>"
    "<input type='file' style='margin-top: 50px;width: 40%;height: 40px; font-size:20px' name='update'><br>"
    "<input type='submit' style='margin-top: 50px;width: 20%;height: 40px; font-size:20px' value='Update'>"
  "</form>"
  "<div id='prg' style='margin-top: 50px;font-size: 200%;float: bottom;'>progress: 0%</div><br>"
  "<script>"
  "$('#upload_form').submit(function(e){"
  "e.preventDefault();"
  "var form = $('#upload_form')[0];"
  "var data = new FormData(form);"
  " $.ajax({"
  "url: '/update',"
  "type: 'POST',"
  "data: data,"
  "contentType: false,"
  "processData:false,"
  "xhr: function() {"
  "var xhr = new window.XMLHttpRequest();"
  "xhr.upload.addEventListener('progress', function(evt) {"
  "if (evt.lengthComputable) {"
  "var per = evt.loaded / evt.total;"
  "$('#prg').html('progress: ' + Math.round(per*100) + '%');"
  "}"
  "}, false);"
  "return xhr;"
  "},"
  "success:function(d, s) {"
  "console.log('success!')"
 "},"
 "error: function (a, b, c) {"
 "}"
 "});"
 "});"
 ""
 "setInterval(function() { "
   "$.ajax({"
     "url: '/metrics',"
     "type: 'GET',"
     "success: function(data) { $('#metrics').html(data); },"
     "error: function() { $('#metrics').html('no connection!!!'); },"
   "});"
 " }, 5000);"
 "</script>";

/*
 * setup function
 */

void setup() 
{
  u8g2.begin(); // инициализация OLED дисплея
  u8g2.enableUTF8Print();
  u8g2.setFont(u8g2_font_cu12_t_cyrillic);

  // put your setup code here, to run once:
  Serial.begin(115200);
  sensors.begin();
  delay(1000); //для стабилизации
  //lcd.init(); // Инициализация дисплея
  //lcd.backlight(); // Включение подсветки дисплея
  WiFi.begin(ssid, password);
  Serial.println("");
  // Ожидание подключения к сети
  while (WiFi.status() != WL_CONNECTED) 
    {
      delay(500);
      Serial.print(".");
      u8g2.setCursor(0, 15);
      u8g2.print(".");
      u8g2.sendBuffer();
      forreboot=forreboot + 1;
      if (forreboot > 20) {
        ESP.restart();
      }
      
    }
  Serial.println("");
  Serial.print("Connected to ");
//  lcd.clear();lcd.print("Connected to ");lcd.setCursor(0,1);
  u8g2.clear();u8g2.setCursor(0, 15);
  u8g2.print("Connected to ");
  Serial.println(ssid);
  u8g2.print(ssid);u8g2.setCursor(0,30);
  Serial.print("my IP address: ");
  u8g2.print("IP: ");
  Serial.println(WiFi.localIP());
  u8g2.print(WiFi.localIP());
  u8g2.sendBuffer();
  delay(2000);

    /*use mdns for host name resolution*/
  if (!MDNS.begin(host)) { //http://esp32.local
    Serial.println("Error setting up MDNS responder!");
    while (1) {
      delay(1000);
    }
  }
  Serial.println("mDNS responder started");
  /*return index page which is stored in serverIndex */
  /*
   * 
  server.on("/", HTTP_GET, []() {
    server.sendHeader("Connection", "close");
    server.send(200, "text/html", loginIndex);
  });
  */
  server.on("/", HTTP_GET, []() {
    server.sendHeader("Connection", "close");
    server.send(200, "text/html", serverIndex);
  });
  /*handling uploading firmware file */
  server.on("/update", HTTP_POST, []() {
    server.sendHeader("Connection", "close");
    server.send(200, "text/plain", (Update.hasError()) ? "FAIL" : "OK");
    ESP.restart();
  }, []() {
    HTTPUpload& upload = server.upload();
    if (upload.status == UPLOAD_FILE_START) {
      Serial.printf("Update: %s\n", upload.filename.c_str());
      if (!Update.begin(UPDATE_SIZE_UNKNOWN)) { //start with max available size
        Update.printError(Serial);
      }
    } else if (upload.status == UPLOAD_FILE_WRITE) {
      /* flashing firmware to ESP*/
      if (Update.write(upload.buf, upload.currentSize) != upload.currentSize) {
        Update.printError(Serial);
      }
    } else if (upload.status == UPLOAD_FILE_END) {
      if (Update.end(true)) { //true to set the size to the current progress
        Serial.printf("Update Success: %u\nRebooting...\n", upload.totalSize);
      } else {
        Update.printError(Serial);
      }
    }
  });
  server.on("/changesim", HTTP_GET, []() {
    change_sim();
    server.sendHeader("Location", "/",true);
    server.send(302, "text/plane",""); 
  });
  server.on("/metrics", HTTP_GET, []() {
    server.send(200, "text/html", metrics());  
  });
  server.on("/startengine", HTTP_GET, []() {
    pinMode(starlineremote_1, OUTPUT);
    digitalWrite(starlineremote_1, LOW);
    delay(3000);
    pinMode(starlineremote_1, INPUT);
    server.sendHeader("Location", "/",true);
    server.send(302, "text/plane",""); 
  });
  server.on("/close", HTTP_GET, []() {
    pinMode(starlineremote_1, OUTPUT);
    digitalWrite(starlineremote_1, LOW);
    delay(500);
    pinMode(starlineremote_1, INPUT);
    server.sendHeader("Location", "/",true);
    server.send(302, "text/plane",""); 
  });
  server.on("/open", HTTP_GET, []() {
    pinMode(starlineremote_2, OUTPUT);
    digitalWrite(starlineremote_2, LOW);
    delay(500);
     pinMode(starlineremote_2, INPUT);
    server.sendHeader("Location", "/",true);
    server.send(302, "text/plane","");
  });
  server.on("/find", HTTP_GET, []() {
    pinMode(starlineremote_3, OUTPUT);
    digitalWrite(starlineremote_3, LOW);
    delay(500);
    pinMode(starlineremote_3, INPUT);
    server.sendHeader("Location", "/",true);
    server.send(302, "text/plane",""); 
  });
  server.on("/stopengine", HTTP_GET, []() {
    pinMode(starlineremote_1, OUTPUT);
    digitalWrite(starlineremote_1, LOW);
    delay(1500);
    pinMode(starlineremote_1, INPUT);
    delay(500);
    pinMode(starlineremote_2, OUTPUT);
    digitalWrite(starlineremote_2, LOW);
    delay(500);
    pinMode(starlineremote_2, INPUT);
    server.sendHeader("Location", "/",true);
    server.send(302, "text/plane",""); 
  });
  
  server.begin();

  snmp.setUDP(&Udp);// дать snmp указатель на объект UDP
  snmp.begin();// запустить прослушиватель SNMP
  snmp.beginMaster(); // запустить отправителя SNMP

  
  

snmp.addIntegerHandler(".1.3.6.1.4.1.14988.1.1.16.1.1.4.2", &rsrp, true); // OID для получения RSRP
callbackRsrp = snmp.findCallback(".1.3.6.1.4.1.14988.1.1.16.1.1.4.2", false);
snmp.addStringHandler(".1.3.6.1.4.1.14988.1.1.16.1.1.12.2", &imsi, true);  // OID для получения IMSI
callbackImsi = snmp.findCallback(".1.3.6.1.4.1.14988.1.1.16.1.1.12.2", false);
snmp.addStringHandler(".1.3.6.1.4.1.14988.1.1.18.1.1.2.4", &changesim, true);  // OID для запуска скрипта смены сим-слота
callbackChangeSim = snmp.findCallback(".1.3.6.1.4.1.14988.1.1.18.1.1.2.4", false);
snmp.addIntegerHandler(".1.3.6.1.4.1.14988.1.1.12.1.0", &snmptime, true); // OID для получения времени
callbackTime = snmp.findCallback(".1.3.6.1.4.1.14988.1.1.12.1.0", false);

//snmp.addIntegerHandler(".1.3.6.1.4.1.14988.1.1.16.1.1.7.2", &sinr, true); // OID для получения SINR
//callbackSinr = snmp.findCallback(".1.3.6.1.4.1.14988.1.1.16.1.1.7.2", false);

// Запускается задача работы с кнопкой   
   xTaskCreateUniversal(taskButton1, "btn1", 4096, NULL, 5, NULL,1);

  // установка системного времени, полученного по SNMP
while (snmptime < 60){ // ждем минуту для установки времени, если время не устанавливается, идем дальше
  snmptime = snmptime + 1;
  getSNMPtime();
  delay(1000);
  }
snmptime = snmptime + (3600 * timezone);
setTime(snmptime);
//lcd.clear();
}


void loop() {
  // put your main code here, to run repeatedly:
  voltmeter();
  snmp.loop();
  getSNMP();
  server.handleClient();
  sensors.requestTemperatures();
  delay(500);
}

void getSNMP(){
  //проверяем, не пора ли отправить запрос SNMP
  //слишком частые запросы могут вызвать проблемы
  if((timeLast + timeDelay) <= millis()){
    intermediateCalc (); // производим промежуточные вычисления
    //проверяем mikrotik на доступность
    bool success = Ping.ping("192.168.100.24", 2);
    if(!success){
      headerNotConnect();    
    }
    else {
//    SerialPrint (); // Вывод данных в COM-port
    //LcdPrint (); // Вывод данных на LCD-дисплей
    OledPrint (); // Вывод данных на OLED-дисплей
    }

    GetRequestRsrp.addOIDPointer(callbackRsrp);                
    GetRequestRsrp.setIP(WiFi.localIP());                 
    GetRequestRsrp.setUDP(&Udp);
    GetRequestRsrp.setRequestID(rand() % 5555);                
    GetRequestRsrp.sendTo(netAdd);               
    GetRequestRsrp.clearOIDList();
    snmp.resetSetOccurred();


    
/*    GetRequestSinr.addOIDPointer(callbackSinr);                
    GetRequestSinr.setIP(WiFi.localIP());                 
    GetRequestSinr.setUDP(&udp);
    GetRequestSinr.setRequestID(rand() % 5555);                
    GetRequestSinr.sendTo(netAdd);               
    GetRequestSinr.clearOIDList();
    snmp.resetSetOccurred();
*/      
    GetRequestImsi.addOIDPointer(callbackImsi);                
    GetRequestImsi.setIP(WiFi.localIP());                 
    GetRequestImsi.setUDP(&Udp);
    GetRequestImsi.setRequestID(rand() % 5555);                
    GetRequestImsi.sendTo(netAdd);               
    GetRequestImsi.clearOIDList();
    snmp.resetSetOccurred();

    timeLast = millis();
  }  
  
}

void getSNMPtime() {
  snmp.loop();
    GetRequestRsrp.addOIDPointer(callbackTime);                
    GetRequestRsrp.setIP(WiFi.localIP());                 
    GetRequestRsrp.setUDP(&Udp);
    GetRequestRsrp.setRequestID(rand() % 5555);                
    GetRequestRsrp.sendTo(netAdd);               
    GetRequestRsrp.clearOIDList();
    snmp.resetSetOccurred();
}

void intermediateCalc () { // промежуточные вычисления для корректного вывода

  OperatorCode = (imsi[3]);OperatorCode += (imsi[4]); // выделение из IMSI код оператора
  operatorIndex = OperatorCode.toInt();
  CountryCode = (imsi[0]);CountryCode += (imsi[1]);CountryCode += (imsi[2]); // выделение из IMSI код страны
  
  if (CountryCode == "250") {
    Country = "RU";
    countryIndex = 1; // строка в массиве operators
  }
  else if (CountryCode == "255"){
    Country = "UA";
    countryIndex = 2;
  }
  else {
    Country = "No Country";
    countryIndex = 0;
  }
  if ((UINT16_MAX-rsrp+1) > 125) {
      PrintRSRP = ("Low RSRP");
  }
  else {
   PrintRSRP = ("-");PrintRSRP += (String(UINT16_MAX-rsrp+1));PrintRSRP += (" dBm");
   }
  
}

void SerialPrint () {
  Serial.print("IMSI: ");Serial.print(imsi);Serial.println(); 
  Serial.print("RSRP: ");Serial.print(PrintRSRP);Serial.println();
  Serial.print("Operator Code: ");Serial.print(OperatorCode);Serial.println();
  Serial.print("Country Code: ");Serial.print(CountryCode);Serial.println();
  Serial.print("Country: ");Serial.print(Country);Serial.println();
  Serial.print("Operator: ");Serial.print(operators[countryIndex][operatorIndex]);Serial.println();
//  Serial.print("SINR: ");Serial.print(sinr);;Serial.println();
  Serial.println("----------------------");
}

//void LcdPrint () {
//  lcd.clear();
//  lcd.print(PrintRSRP);
//  lcd.setCursor(9,0);
//  lcd.print(operators[countryIndex][operatorIndex]);lcd.print(" ");lcd.print(Country);
//  lcd.setCursor(0,1);
//  printDigits(hour());lcd.print(":");printDigits(minute());lcd.print("  ");printDigits(day());lcd.print("  ");lcd.print(calendar[0][month()]);lcd.print("  ");lcd.print(calendar[1][weekday()]);
//  lcd.setCursor(0,3);
//  lcd.print(int(round(sensors.getTempC(sensor_int))));lcd.print(" C");
//  lcd.setCursor(15,3);
//  lcd.print(int(round(sensors.getTempC(sensor_out))));lcd.print(" C");
//}

void OledPrint () {
  u8g2.clearBuffer();
  u8g2.setFont(u8g2_font_cu12_t_cyrillic);
  u8g2.setCursor(0,15); u8g2.print(PrintRSRP);
    OperCount = (operators[countryIndex][operatorIndex]);OperCount += (" ");OperCount += (Country);
    OperCount.toCharArray(opercount, 15);
    printopercount = (256 - (u8g2.getUTF8Width(opercount)));
  u8g2.setCursor(printopercount, 15);
  u8g2.print(OperCount);
    PrintDate = (day());PrintDate += (" ");PrintDate += (calendar[0][month()]);PrintDate += (", ");PrintDate += (calendar[1][weekday()]);
    PrintDate.toCharArray(printdate,40);
    printdatex=((256 - (u8g2.getUTF8Width(printdate)))/2);
  u8g2.setCursor(printdatex, 60);
  u8g2.print(PrintDate);
  u8g2.setCursor(0,37);
  u8g2.setFont(u8g2_font_cu12_tf);
  u8g2.print(int(round(sensors.getTempC(sensor_out))));u8g2.print("°C");
  PrintTemp = (int(round(sensors.getTempC(sensor_int))));PrintTemp += ("°C");
  PrintTemp.toCharArray(printtemp,15);
  printtempx=(256-u8g2.getUTF8Width(printtemp));
  u8g2.setCursor(printtempx,37);
  u8g2.print(PrintTemp);
  u8g2.setFont(u8g2_font_cu12_t_cyrillic);
  u8g2.setCursor(0,60);
  u8g2.print(input_volt);
  u8g2.print(" V");
  //u8g2.print(analogvalue);
//  u8g2.drawUTF8(0, 30, "Как заебала эта хуйня!");
  u8g2.setFont(u8g2_font_timB24_tn);
  u8g2.setCursor(90, 45);
  printDigits(hour());u8g2.print(":");printDigits(minute());
  u8g2.sendBuffer();
}

void headerNotConnect() {
  u8g2.clearBuffer();
  u8g2.setFont(u8g2_font_cu12_t_cyrillic);
  u8g2.setCursor(81,15);
  u8g2.print("Not Connected");
  u8g2.sendBuffer();
  forreboot=forreboot + 1;
      if (forreboot > 10) {
        ESP.restart();
      }
  delay(2000);
}

void printDigits(int digits) {
  // вспомогательная функция для печати данных о времени 
  // на монитор порта; добавляет в начале двоеточие и ноль:
    if (digits < 10)
    u8g2.print('0');
  u8g2.print(digits);
}

void IRAM_ATTR ISR_btn1(){
// Прерывание по кнопке, отпускаем семафор  
   xSemaphoreGiveFromISR( btn1Semaphore, NULL );
}
 
void taskButton1( void *pvParameters ){
// Определяем режим работы GPIO с кнопкой   
   pinMode(PIN_BUTTON,INPUT_PULLUP);
   pinMode(PIN_DISPLAY_OFF,INPUT_PULLUP);
   pinMode(PIN_CONTRAST,INPUT_PULLUP);
   // Создаем семафор     
   btn1Semaphore = xSemaphoreCreateBinary();
// Сразу "берем" семафор чтобы не было первого ложного срабатывания кнопки   
   xSemaphoreTake( btn1Semaphore, 100 );
   while(true){
// Запускаем обработчик прерывания (кнопка замыкает GPIO на землю)
      attachInterrupt(PIN_BUTTON, ISR_btn1, CHANGE);
      attachInterrupt(PIN_DISPLAY_OFF, ISR_btn1, CHANGE);
      attachInterrupt(PIN_CONTRAST, ISR_btn1, CHANGE);
// Ждем "отпускание" семафора
      xSemaphoreTake( btn1Semaphore, portMAX_DELAY );
// Отключаем прерывание для устранения повторного срабатывания прерывания во время обработки
      detachInterrupt(PIN_BUTTON);
      detachInterrupt(PIN_DISPLAY_OFF);
      detachInterrupt(PIN_CONTRAST);
      bool st = digitalRead(PIN_BUTTON);
      bool st1 = digitalRead(PIN_DISPLAY_OFF);
      bool st2 = digitalRead(PIN_CONTRAST);
      uint32_t ms = millis();
// Проверка изменения состояния кнопки или превышение таймаута      
      if( st != state_btn || ms - ms_btn > TM_BUTTON){
          state_btn = st;
          ms_btn    = ms;
          if( st == LOW ){
           change_sim();           
         }
      }
      if( st1 != state_btn || ms - ms_btn > TM_BUTTON){
          state_btn = st1;
          ms_btn    = ms;
          if( st1 == LOW ){
           poweroffdisplay();           
         }
      }
      if( st2 != state_btn || ms - ms_btn > TM_BUTTON){
          state_btn = st1;
          ms_btn    = ms;
          if( st2 == LOW ){
           dayornight();           
         }
      }
         
// Задержка для устранения дребезга контактов
          vTaskDelay(TM_BUTTON);
   }
}


void change_sim() {
  u8g2.clearBuffer();
  u8g2.setFont(u8g2_font_cu12_t_cyrillic);
  u8g2.setCursor(75,15);
  u8g2.print("Change Sim-slot");
  u8g2.sendBuffer();
  delay(2000);
  
  GetRequestChangeSim.addOIDPointer(callbackChangeSim);                
  GetRequestChangeSim.setIP(WiFi.localIP());                 
  GetRequestChangeSim.setUDP(&Udp);
  GetRequestChangeSim.setRequestID(rand() % 5555);                
  GetRequestChangeSim.sendTo(netAdd);               
  GetRequestChangeSim.clearOIDList();
  snmp.resetSetOccurred();
}

String metrics() {
  String result;
  result += "Temp in : " + String(int(round(sensors.getTempC(sensor_int))));result += " С";result += "<br>";
  result += "Temp out: " + String(int(round(sensors.getTempC(sensor_out))));result += " С";result += "<br>";
  result += "RSSI: " + PrintRSRP;result += "    ";result += operators[countryIndex][operatorIndex];result += " ";result += Country;result += "<br>";
  result += "Voltage : " + String(input_volt);result += " V";result += "<br>";
  return result;
}

void voltmeter() {
  analogvalue = analogRead(voltpin);
  input_volt = (((analogvalue * 3.3 ) / 4095) / (r2/(r1+r2)));
  if (input_volt < 0.1)
{
input_volt=0.0;
}
}

void poweroffdisplay() {
  if (pwrs == 0) {
    pwrs = 1;
  }
  else {
    pwrs = 0;
  }
  Serial.print(pwrs);
  u8g2.setPowerSave(pwrs);
 }

void dayornight() {
  if (contrast == 0) {
    contrast = 255;
  }
  else {
    contrast = 0;
  }
  u8g2.setContrast(contrast);
}


File: /README.md
# esp32_snmp_mikrotik
SNMP-Client for ESP32
Data collection (RSSI, Country code, operator code, date and time) from the router Mikrotik ltap mini and output to the display.
Launching the script for changing SIM-card on Mikrotik by pressing a button on ESP32


