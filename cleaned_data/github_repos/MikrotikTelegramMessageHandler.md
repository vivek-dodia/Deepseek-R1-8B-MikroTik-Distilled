# Repository Information
Name: MikrotikTelegramMessageHandler

# Directory Structure
Directory structure:
└── github_repos/MikrotikTelegramMessageHandler/
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
    │   │       ├── pack-b9176d1dcc8717cf1432e94ea96c9ded6ea3e313.idx
    │   │       └── pack-b9176d1dcc8717cf1432e94ea96c9ded6ea3e313.pack
    │   ├── packed-refs
    │   └── refs/
    │       ├── heads/
    │       │   └── main
    │       ├── remotes/
    │       │   └── origin/
    │       │       └── HEAD
    │       └── tags/
    ├── README.md
    └── telegram.rsc


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
	url = https://github.com/drpioneer/MikrotikTelegramMessageHandler.git
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
0000000000000000000000000000000000000000 3414e67c7acb76ff2c684eeda9ef8e42c400bd13 vivek-dodia <vivek.dodia@icloud.com> 1738605964 -0500	clone: from https://github.com/drpioneer/MikrotikTelegramMessageHandler.git


File: /.git\logs\refs\heads\main
0000000000000000000000000000000000000000 3414e67c7acb76ff2c684eeda9ef8e42c400bd13 vivek-dodia <vivek.dodia@icloud.com> 1738605964 -0500	clone: from https://github.com/drpioneer/MikrotikTelegramMessageHandler.git


File: /.git\logs\refs\remotes\origin\HEAD
0000000000000000000000000000000000000000 3414e67c7acb76ff2c684eeda9ef8e42c400bd13 vivek-dodia <vivek.dodia@icloud.com> 1738605964 -0500	clone: from https://github.com/drpioneer/MikrotikTelegramMessageHandler.git


File: /.git\packed-refs
# pack-refs with: peeled fully-peeled sorted 
3414e67c7acb76ff2c684eeda9ef8e42c400bd13 refs/remotes/origin/main


File: /.git\refs\heads\main
3414e67c7acb76ff2c684eeda9ef8e42c400bd13


File: /.git\refs\remotes\origin\HEAD
ref: refs/remotes/origin/main


File: /README.md
# TLGRM - скрипт оповещения в Телеграм и удалённого запуска функций, скриптов и команд RouterOS.

Скрипт обеспечивает отправку (трансляцию) записей журнала устройств Mikrotik в заданную Telegram-группу и удалённый запуск скриптов/ функций/ команд RouterOS. В скрипте использованы идеи разных авторов, найденные на просторах интернета. Код скрипта не имеет зависимостей от сторонних функций и скриптов. Работосопособность скрипта проверялась на актуальных версиях RouterOS 6.49.++ и 7.16.++. Тело скрипта необходимо закинуть в 'System/Scripts' и настроить запуск по расписанию 'System/Scheduler' с периодом 1 минуту.

Во время работы скрипт взаимодействует с заданной Телеграм-группой и при этом:
- реагирует на принятые команды из сообщений в группе
- транслирует в группу потенциально интересные записи журнала устройства

## Особенности работы скрипта:
- формируемые скриптом сообщения дробятся по 4096 байтов
- поддерживается отправка сообщений с кириллическими символами (CP1251)
- сообщения, неотправленные из-за проблем с интернет-каналом, отсылаются после восстановления связи
- обрабатывается только ПОСЛЕДНЯЯ команда, отправленная пользователем в ТГ-группу
- поддерживается индивидуальная и групповая адресация команд пользователя
- трансляция единственной записи журнала производится одной строкой с ID роутера (без разделителя) для возможности чтения сообщения в шторке уведомлений без разблокировки мобильного устройства
- трансляция сообщений о подключении/отключении беспроводных клиентов производится в случаях, только когда для МАС-адреса из строки журнала:
    - отсутствует соответствующий IP-адрес в списке DHCP/Leases
    - назначен динамический IP-адрес в списке DHCP/Leases
    - назначен статический IP-адрес в списке DHCP/Leases и при этом комментарий к нему отсутствует
- контроль работы скрипта доступен в терминале по команде: /system script run tlgrm (где 'tlgrm' - имя скрипта)
- ID устройства должно состоять только из маленьких латинских букв и цифр

Отправка команды всем или одному конкретному роутеру, находящемуся в ТГ-группе, подразумевает отправку сообщения, подготовленного специальным образом. При этом скрипт должен быть запущен на всех роутерах, которым может быть адресовано сообщение. Для отправки команды необходимо сформировать сообщение в виде текстовой строки специального формата: 
 - начало сообщения обозначается символом "/"
 - затем указывается ID устройства, которому адресовано сообщение (соответствует /system identity устройства). Отправка всем роутерам в ТГ-группе подразумевает указание в качестве адресата: forall. Для корректной работы имя устройства должно содержать ТОЛЬКО маленькие латинские буквы и цифры (!!!).
 - далее через символ подчеркивания или пробел указывается непосредственно команда. В качестве команды могут выступать: имя глобальной функции, имя скрипта или команда RouterOS.

Примеры строк с командами:
~~~ 
  /forall log warning [/system resource get uptime]
  /mikrotik system reboot
  /mikrotik1_wol
  /mikrot_ip_fir_fil_dis_[find_comment~"LAN"]
~~~
Настройки хранятся вначале скрипта и представляют собой преднастроенные переменные:
- **botID** "XXXXXXXXXX:XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX" - идентификатор бота
- **myChatID** "-XXXXXXXXX"  идентификатор чата
- **broadCast**, где false = реакция на команды, предназначенные только этому устройству; true = реакция на все принятые команды
- **launchScr**, где true = разрешение исполнения скриптов; false = запрет исполнения скриптов
- **launchFnc**, где true = разрешение использования глобальных функций; false = запрет использования функций
- **launchCmd**, где true = разрешение выполнения команд RouterOS; false = запрет выполнения команд RouterOS
- **sysInfo**,   где true = разрешение трансляции в ТГ-чат подозрительных событий журнала устройства; false = запрет трансляции событий журнала устройства
- **userInfo**,  где true = разрешение трансляции в ТГ-чат сообщений, сформированных по условиям пользователя; false = запрет трансляции пользовательских сообщений

Минимальная настройка скрипта сводится к указанию идентификаторов бота и группы: [botID и myChatID](https://1spla.ru/blog/telegram_bot_for_mikrotik)

-----
Для формирования списка команд в Телеграм-группе через бота BotFather необходимо выполнить ряд действий с BotFather -> 
ввести и отправить команду: /setcommands, указать целевого бота, после чего появится подсказка:
~~~
    command1 - Description
    command2 - Another description
~~~
По сути это шаблон с указанием формата ввода команд, в котором каждая команда должна быть оформлена отдельной строкой. В каждой строке слева от дефиса находится команда в виде слова, которое будет отправлено в ТГ-группу при выборе этой команды. В каждой строке справа от дефиса обязательно должно присутствовать краткое описание команды. Необходимо обратить внимание на важные детали при формировании текстовых строк с командами:
- текст команды (слева от дефиса) может состоять ТОЛЬКО из цифр, маленьких латинских букв и знака подчёркивания (заглавные буквы, пробелы, спецсимволы и кириллица недопустимы).
- текст описания (справа от дефиса) может содержать любые символы. Текст обязательно должен быть.
- при добавлении новых команд, старые команды нужно вбивать вновь... Другими словами: все команды нужно вводить одним списком.

Ввести и отправить команду по шаблону: 'имямикротик_имяскрипта - текст с описанием.'
Если всё сделано правильно, будет получен ответ: 'Success! Command list updated.'

Обратите внимание! При вводе списка предустановленных команд BotFather требует, чтобы слева от дефиса находилось только одно слово - сама команда, а для работы TLGRM необходимо, чтобы команда содержала в себе ID устройства и имя скрипта/функции/команды ROS разделённые пробелом. Для обхода этой нестыковки TLGRM считает тождественными пробелы (' ') и знаки подчёркивания ('_'). В таком варианте получается, что строка 'имямикротик_имяскрипта' для BotFather выглядит как одно слово, а для TLGRM выглядит как разные слова. Таким образом BotFather тянет за собой зависимость -> ID устройств и названия скриптов **ОБЯЗАНЫ** состоять только из маленьких латинских букв и цифр (заглавные буквы, пробелы, знаки подчёркивания, спецсимволы и кириллица недопустимы!!!).
После формирования списка предустановленных команд BotFather, нажав на кнопку "/" в своём чате с ботом можно видеть этот список, и при желании выбрать нужную команду на исполнение.

-----
Для корректного отображения скриптом 'username' отправителя, в настройках Телеграм должно быть заполнено поле "Имя пользователя", бот должен быть подключен к ГРУППЕ (групповому чату), а не к КАНАЛУ. Опытным путём выяснено, что предпочтителен групповой чат Телеграм с id БЕЗ префикса '-100', в таком чате сообщения от ГРУППЫ роутеров не теряются.

## Список литературы:
- https://forummikrotik.ru/viewtopic.php?p=89956#p89956
- https://forum.mikrotik.com/viewtopic.php?p=1012951#p1012951
- https://habr.com/ru/post/650563

**Используете скрипт - отметьте это звездочкой, Вам не сложно, а мне приятно!**


File: /telegram.rsc
# TLGRM - combined notifications script & launch of commands (scripts & functions) via Telegram
# Script uses ideas by Sertik, Virtue, Dimonw, -13-, Mk51, Alice Tails, Chupaka, rextended, sebastia, drPioneer
# https://github.com/drpioneer/MikrotikTelegramMessageHandler
# https://forummikrotik.ru/viewtopic.php?p=78085#p78085
# tested on ROS 6.49.17 & 7.16.2
# updated 2025/01/01

:global scriptTlgrm; # flag of running script: false=in progress, true=idle
:do {
  :local botID    "XXXXXXXXXX:XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
  :local myChatID "-XXXXXXXXX"
  :local broadCast false; # non-addressed reception mode
  :local launchScr true;  # permission to execute scripts
  :local launchFnc true;  # permission to perform functions
  :local launchCmd true;  # permission to execute commands
  :local sysInfo   true;  # system information broadcast to Telegram
  :local userInfo  false; # user information broadcast to Telegram
  :local emoList {
    "cherry"="%F0%9F%8D%92";"smile"="%F0%9F%98%8E";"bell"="%F0%9F%94%94"}
    # emoji list: https://apps.timwhitlock.info/emoji/tables/unicode
  :local emoDev ($emoList->"cherry"); # device emoji in chat
  :global timeAct; # time when the last command was executed
  :global timeLog; # time when the log entries were last sent

  # function of converting CP1251 to UTF8 in URN # https://forum.mikrotik.com/viewtopic.php?p=967513#p967513
  :local ConvCP1251 do={
    :if ([:typeof $1]!="str" or [:len $1]=0) do={:return ""}
    :local cp1251 {
      "\00";"\01";"\02";"\03";"\04";"\05";"\06";"\07";"\08";"\09";"\0A";"\0B";"\0C";"\0D";"\0E";"\0F";
      "\10";"\11";"\12";"\13";"\14";"\15";"\16";"\17";"\18";"\19";"\1A";"\1B";"\1C";"\1D";"\1E";"\1F";
      "\20";"\22";"\26";"\2B";"\3C";"\3E";"\5B";"\5C";"\5D";"\5E";"\60";"\7B";"\7C";"\7D";"\7E";"\7F";
      "\80";"\81";"\82";"\83";"\84";"\85";"\86";"\87";"\88";"\89";"\8A";"\8B";"\8C";"\8D";"\8E";"\8F";
      "\90";"\91";"\92";"\93";"\94";"\95";"\96";"\97";"\98";"\99";"\9A";"\9B";"\9C";"\9D";"\9E";"\9F";
      "\A0";"\A1";"\A2";"\A3";"\A4";"\A5";"\A6";"\A7";"\A8";"\A9";"\AA";"\AB";"\AC";"\AD";"\AE";"\AF";
      "\B0";"\B1";"\B2";"\B3";"\B4";"\B5";"\B6";"\B7";"\B8";"\B9";"\BA";"\BB";"\BC";"\BD";"\BE";"\BF";
      "\C0";"\C1";"\C2";"\C3";"\C4";"\C5";"\C6";"\C7";"\C8";"\C9";"\CA";"\CB";"\CC";"\CD";"\CE";"\CF";
      "\D0";"\D1";"\D2";"\D3";"\D4";"\D5";"\D6";"\D7";"\D8";"\D9";"\DA";"\DB";"\DC";"\DD";"\DE";"\DF";
      "\E0";"\E1";"\E2";"\E3";"\E4";"\E5";"\E6";"\E7";"\E8";"\E9";"\EA";"\EB";"\EC";"\ED";"\EE";"\EF";
      "\F0";"\F1";"\F2";"\F3";"\F4";"\F5";"\F6";"\F7";"\F8";"\F9";"\FA";"\FB";"\FC";"\FD";"\FE";"\FF"}
    :local utf8 {
      "00";"01";"02";"03";"04";"05";"06";"07";"08";"09";"0A";"0B";"0C";"0D";"0E";"0F";
      "10";"11";"12";"13";"14";"15";"16";"17";"18";"19";"1A";"1B";"1C";"1D";"1E";"1F";
      "20";"22";"26";"2B";"3C";"3E";"5B";"5C";"5D";"5E";"60";"7B";"7C";"7D";"7E";"7F";
      "D082";"D083";"E2809A";"D193";"E2809E";"E280A6";"E280A0";"E280A1";"E282AC";"E280B0";"D089";"E280B9";"D08A";"D08C";"D08B";"D08F";
      "D192";"E28098";"E28099";"E2809C";"E2809D";"E280A2";"E28093";"E28094";"EFBFBD";"E284A2";"D199";"E280BA";"D19A";"D19C";"D19B";"D19F";
      "C2A0";"D08E";"D19E";"D088";"C2A4";"D290";"C2A6";"C2A7";"D081";"C2A9";"D084";"C2AB";"C2AC";"534859";"C2AE";"D087";
      "C2B0";"C2B1";"D086";"D196";"D291";"C2B5";"C2B6";"C2B7";"D191";"E28496";"D194";"C2BB";"D198";"D085";"D195";"D197";
      "D090";"D091";"D092";"D093";"D094";"D095";"D096";"D097";"D098";"D099";"D09A";"D09B";"D09C";"D09D";"D09E";"D09F";
      "D0A0";"D0A1";"D0A2";"D0A3";"D0A4";"D0A5";"D0A6";"D0A7";"D0A8";"D0A9";"D0AA";"D0AB";"D0AC";"D0AD";"D0AE";"D0AF";
      "D0B0";"D0B1";"D0B2";"D0B3";"D0B4";"D0B5";"D0B6";"D0B7";"D0B8";"D0B9";"D0BA";"D0BB";"D0BC";"D0BD";"D0BE";"D0BF";
      "D180";"D181";"D182";"D183";"D184";"D185";"D186";"D187";"D188";"D189";"D18A";"D18B";"D18C";"D18D";"D18E";"D18F"}
    :local res ""; :local urn ""
    :for i from=0 to=([:len $1]-1) do={
      :local sym [:pick $1 $i ($i+1)]; :local idx [:find $cp1251 $sym]; :local utf ($utf8->$idx)
      :if ([:len $utf]=0) do={:set urn $sym}
      :if ([:len $utf]=2) do={:set urn "%$[:pick $utf 0 2]"}
      :if ([:len $utf]=4) do={:set urn "%$[:pick $utf 0 2]%$[:pick $utf 2 4]"}
      :if ([:len $utf]=6) do={:set urn "%$[:pick $utf 0 2]%$[:pick $utf 2 4]%$[:pick $utf 4 6]"}
      :set res ($res.$urn)}
    :return $res}

  # function of converting to lowercase letters and cutting out unprintable chars # https://forum.mikrotik.com/viewtopic.php?p=714396#p714396
  :local ConvSymb do={
    :if ([:typeof $1]!="str" or [:len $1]=0) do={:return ""}
    :local unprn "\00\01\02\03\04\05\06\07\08\09\0A\0B\0C\0D\0E\0F\10\11\12\13\14\15\16\17\18\19\1A\1B\1C\1D\1E\1F"
    :local upper "ABCDEFGHIJKLMNOPQRSTUVWXYZ"; :local lower "abcdefghijklmnopqrstuvwxyz"; :local res ""
    :for i from=0 to=([:len $1]-1) do={
      :local chr [:pick $1 $i]
      :if ([:len $2]=0) do={
        :local pos [:find $upper $chr]; :if ($pos>-1) do={:set chr [:pick $lower $pos]}
      } else={:local pos [:find $unprn $chr]; :if ($pos>-1) do={:set chr ""}}
      :set res ($res.$chr)}
    :return $res}

  # telegram messenger response parsing function # https://habr.com/ru/post/482802/
  :local MsgParser do={
    :if ([:typeof $1]!="str" or [:len $1]=0) do={:return ""}
    :local variaMod ("\"$2\"")
    :if ([:len [:find $1 $variaMod -1]]=0) do={:return "unknown"}
    :local startLoc ([:find $1 $variaMod -1]+[:len $variaMod]+1)
    :local commaLoc [:find $1 "," $startLoc]; :local brakeLoc [:find $1 "}" $startLoc]
    :local endLoc $commaLoc; :local startSymbol [:pick $1 $startLoc]
    :if ($brakeLoc!=0 && ($commaLoc=0 or $brakeLoc<$commaLoc)) do={:set endLoc $brakeLoc}
    :if ($startSymbol="{") do={:set endLoc ($brakeLoc+1)}
    :if ($3=true) do={:set startLoc ($startLoc+1); :set endLoc ($endLoc-1)}
    :if ($endLoc<$startLoc) do={:set endLoc ($startLoc+1)}
    :return [:pick $1 $startLoc $endLoc]}

  # time translation function to UNIX time # https://forum.mikrotik.com/viewtopic.php?t=75555#p994849
  :local T2U do={ # $1-date/time in any format: "hh:mm:ss","mmm/dd hh:mm:ss","mmm/dd/yyyy hh:mm:ss","yyyy-mm-dd hh:mm:ss","mm-dd hh:mm:ss"
    :local dTime [:tostr $1]; :local yesterDay false; /system clock
    :local cYear [get date]; :if ($cYear~"....-..-..") do={:set cYear [:pick $cYear 0 4]} else={:set cYear [:pick $cYear 7 11]}
    :if ([:len $dTime]=10 or [:len $dTime]=11) do={:set dTime "$dTime 00:00:00"}
    :if ([:len $dTime]=15) do={:set dTime "$[:pick $dTime 0 6]/$cYear $[:pick $dTime 7 15]"}
    :if ([:len $dTime]=14) do={:set dTime "$cYear-$[:pick $dTime 0 5] $[:pick $dTime 6 14]"}
    :if ([:len $dTime]=8) do={:if ([:totime $1]>[get time]) do={:set yesterDay true}; :set dTime "$[get date] $dTime"}
    :if ([:tostr $1]="") do={:set dTime ("$[get date] $[get time]")}
    :local vDate [:pick $dTime 0 [:find $dTime " " -1]]; :local vTime [:pick $dTime ([:find $dTime " " -1]+1) [:len $dTime]]
    :local vGmt [get gmt-offset]; :if ($vGmt>0x7FFFFFFF) do={:set vGmt ($vGmt-0x100000000)}; :if ($vGmt<0) do={:set vGmt ($vGmt*-1)}
    :local arrMn [:toarray "0,0,31,59,90,120,151,181,212,243,273,304,334"]; :local vdOff [:toarray "0,4,5,7,8,10"]
    :local month [:tonum [:pick $vDate ($vdOff->2) ($vdOff->3)]]
    :if ($vDate~".../../....") do={
      :set vdOff [:toarray "7,11,1,3,4,6"]
      :set month ([:find "xxanebarprayunulugepctovecANEBARPRAYUNULUGEPCTOVEC" [:pick $vDate ($vdOff->2) ($vdOff->3)] -1]/2)
      :if ($month>12) do={:set month ($month-12)}}
    :local year [:pick $vDate ($vdOff->0) ($vdOff->1)]
    :if ((($year-1968)%4)=0) do={:set ($arrMn->1) -1; :set ($arrMn->2) 30}
    :local toTd ((($year-1970)*365)+(($year-1968)>>2)+($arrMn->$month)+([:pick $vDate ($vdOff->4) ($vdOff->5)]-1))
    :if ($yesterDay) do={:set toTd ($toTd-1)};   # bypassing ROS6.xx time format problem after 00:00:00
    :return (((((($toTd*24)+[:pick $vTime 0 2])*60)+[:pick $vTime 3 5])*60)+[:pick $vTime 6 8]-$vGmt)}

  # time conversion function from UNIX time # https://forum.mikrotik.com/viewtopic.php?p=977170#p977170
  :local U2T do={ # $1-UnixTime $2-OnlyTime
    :local ZeroFill do={:return [:pick (100+$1) 1 3]}
    :local prMntDays [:toarray "0,0,31,59,90,120,151,181,212,243,273,304,334"]
    :local vGmt [:tonum [/system clock get gmt-offset]]
    :if ($vGmt>0x7FFFFFFF) do={:set vGmt ($vGmt-0x100000000)}
    :if ($vGmt<0) do={:set vGmt (-$vGmt)}
    :local tzEpoch ($vGmt+[:tonum $1])
    :if ($tzEpoch<0) do={:set tzEpoch 0}; # unsupported negative unix epoch
    :local yearStamp (1970+($tzEpoch/31536000))
    :local tmpLeap (($yearStamp-1968)>>2)
    :if ((($yearStamp-1968)%4)=0) do={:set ($prMntDays->1) -1; :set ($prMntDays->2) 30}
    :local tmpSec ($tzEpoch%31536000)
    :local tmpDays (($tmpSec/86400)-$tmpLeap)
    :if ($tmpSec<(86400*$tmpLeap) && (($yearStamp-1968)%4)=0) do={
      :set tmpLeap ($tmpLeap-1); :set ($prMntDays->1) 0; :set ($prMntDays->2) 31; :set tmpDays ($tmpDays+1)}
    :if ($tmpSec<(86400*$tmpLeap)) do={:set yearStamp ($yearStamp-1); :set tmpDays ($tmpDays+365)}
    :local mnthStamp 12; :while (($prMntDays->$mnthStamp)>$tmpDays) do={:set mnthStamp ($mnthStamp-1)}
    :local dayStamp [$ZeroFill (($tmpDays+1)-($prMntDays->$mnthStamp))]
    :local timeStamp (00:00:00+[:totime ($tmpSec%86400)])
    :if ([:len $2]=0) do={:return "$yearStamp/$[$ZeroFill $mnthStamp]/$[$ZeroFill $dayStamp] $timeStamp"} else={:return "$timeStamp"}}

  # system information collection function
  :local SysInfo do={
    :if ([:len $1]=0) do={:return ""}
    :local fndMac ""; :local tmpMac ""; :local tmpAdr ""; :local tmpCmt ""; :local tmpHst ""; :local tmpDyn ""
    :if ($1~"([0-9A-F]{2}[:]){5}[0-9A-F]{2}") do={:set fndMac [:pick $1 ([:find $1 ":"]-2) ([:find $1 ":"]+15)]}
    :if ($fndMac!="") do={ # when any MAC address is detected
      :do {
        /ip dhcp-server lease
        :set tmpMac [get [find mac-address=$fndMac] mac-address]
        :set tmpCmt [get [find mac-address=$fndMac] comment]
        :set tmpHst [get [find mac-address=$fndMac] host-name]
        :set tmpDyn [get [find mac-address=$fndMac status="bound"] dynamic]
        :set tmpAdr [get [find mac-address=$fndMac status="bound"] address]} on-error={}
      :if ($tmpMac="") do={:return "$2 $1 [unfamil MAC]"; # when unfamiliar MAC address
      } else={ # when DHCP-server lease client is actual & with static IP & no comment about DHCP lease
        :if ($tmpDyn!="" && !$tmpDyn && $tmpCmt="") do={:return "$2 $1 $tmpHst $tmpAdr [no comment about DHCP lease]"}}
    } else={:return "$2 $1"}; # when message without MAC address
    :return ""}

  # user information collection function
  :local UsrInfo do={
    :if ([:len $1]=0) do={:return ""}
    :local tmpMac ""; :local tmpAdr ""; :local tmpCmt ""; :local tmpHst ""; :local tmpDyn ""; :local tmpIfc "none"; :local tmpStg ""
    :if ($1~" assigned ((25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)[.]){3}(25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)") do={
      :if ($1~" to ") do={:set tmpAdr [:pick $1 ([:find $1 " assigned "]+10) ([:find $1 "to"]-1)]}; # specificity of ROS6
      :if ($1~" for ") do={:set tmpAdr [:pick $1 ([:find $1 " assigned "]+10) ([:find $1 "for"]-1)]}}; # specificity of ROS7
    :if ($tmpAdr!="") do={ # when address leasing DHCP server ->
      :do {
        /ip dhcp-server lease
        :set tmpCmt [get [find address=$tmpAdr] comment]; :set tmpHst [get [find address=$tmpAdr] host-name]
        :set tmpDyn [get [find address=$tmpAdr] dynamic]; :set tmpMac [get [find address=$tmpAdr] mac-address]
        :set tmpIfc [/interface bridge host get [find mac-address=$tmpMac] on-interface]
        :set tmpStg [[:parse "[/interface wireless registration-table get [find last-ip=$tmpAdr] signal-strength-ch0]"]]
        :if ([:len $tmpStg]=0) do={
          :set tmpStg [[:parse "[/interface wifiwave2 registration-table get [find last-ip=$tmpAdr] signal-strength-ch0]"]]}
      } on-error={}
      :if ($tmpStg!="") do={:set tmpStg ($tmpStg."dBm")}
      :local user1 "User1"; :local user2 "User2"; :local whereUser "PLACENAME"
      :if ($tmpDyn!="") do={
        :if ($tmpDyn) do={:return "$[($emoList->"smile")] $2 +$tmpIfc $tmpStg $tmpAdr $tmpHst"; # output when dynamic client
        } else={:return "$tmpCmt $2 +$tmpIfc $tmpStg $tmpAdr $tmpHst"}}; # output when static client
      :if ($tmpCmt=$user1) do={:return "$[($emoList->"bell")] $2 $user1 at $whereUser"}; # output when user1
      :if ($tmpCmt=$user2) do={:return "$[($emoList->"smile")] $2 $user2 at $whereUser"}}; # output when user2
    :return ""}

  # main body
  :local nameID [$ConvSymb [/system identity get name]]; # text ID of router
  :local startTime [$U2T [$T2U]]; # start time in nice format
  :put "$startTime\tStart of TLGRM on router:\t$nameID"
  :if ([:len $scriptTlgrm]=0) do={:set scriptTlgrm true}; # creating a script running flag
  :if ($scriptTlgrm) do={ # when script is active ->
    :set scriptTlgrm false; # script running flag is active 
    :if ([:len $timeAct]>0) do={:put "$[$U2T [$T2U]]\tTime executed last command:\t$[$U2T $timeAct]"}
    :if ([:len $timeLog]>0) do={:put "$[$U2T [$T2U]]\tTime sent last log entries:\t$[$U2T $timeLog]"}

    # part of script body to execute via Telegram # https://forummikrotik.ru/viewtopic.php?p=78085
    :put "$[$U2T [$T2U]]\t*** Stage of launch via Telegram ***"
    :local timeStmp [$T2U]; :local httpResp ""
    :local urlStr "https://api.telegram.org/bot$botID/getUpdates\?offset=-1&limit=1&allowed_updates=message"
    :if ([:len $timeAct]=0) do={:put "$[$U2T [$T2U]]\tTime of last launch not found"; :set timeAct $timeStmp}
    :do {:set httpResp [/tool fetch mode=https http-method=post url=$urlStr as-value output=user]} on-error={}
    :if ([:len $httpResp]!=0) do={ # when Telegram server responded to request ->
      :local content ($httpResp->"data")
      :if ([:len $content]>30) do={
        :local msgTxt [$MsgParser $content "text" true]
        :set msgTxt [:pick $msgTxt ([:find $msgTxt "/" -1]+1) [:len $msgTxt]]
        :if ($msgTxt~"@") do={:set msgTxt [:pick $msgTxt 0 [:find $msgTxt "@"]]}
        :local newStr ""; :local change ""; :local msgAdr ""
        :for i from=0 to=([:len $msgTxt]-1) do={ # cyclic replacement of character '_' by ' '
          :local symb [:pick $msgTxt $i ($i+1)]
          :if ($symb="_") do={:set change " "} else={:set change $symb} 
          :set newStr ($newStr.$change)}
        :set msgTxt $newStr
        :if ($broadCast) do={:set msgAdr $nameID} else={
          :set msgAdr [$ConvSymb [:pick $msgTxt 0 [:find $msgTxt " " -1]]]
          :if ([:len [:find $msgTxt " "]]=0) do={:set msgAdr ($msgTxt." ")}
          :put "$[$U2T [$T2U]]\tRecipient of Telegram message:\t$msgAdr"
          :set msgTxt [:pick $msgTxt ([:find $msgTxt $msgAdr -1]+[:len $msgAdr]+1) [:len $msgTxt]]}
        :if ([:pick $msgTxt 0 1]="\$") do={:set msgTxt [:pick $msgTxt 1 [:len $msgTxt]]}
        :if ([:pick $msgTxt 0 2]="[\$" && [:pick $msgTxt ([:len $msgTxt]-1) [:len $msgTxt]]="]") do={
          :set msgTxt [:pick $msgTxt 2 ([:len $msgTxt]-1)]}; # skipping prefix "$" or [$ .....]
        :if ($msgAdr=$nameID or $msgAdr="forall") do={
          :local chatID [$MsgParser [$MsgParser $content "chat"] "id"]
          :local userNm [$MsgParser $content "username"]
          :set timeStmp [$MsgParser $content "date"]
          :put "$[$U2T [$T2U]]\tSender of Telegram message:\t$userNm \tCommand to execute:\t$msgTxt"
          :local restline []
          :if ([:len [:find $msgTxt " "]]!=0) do={
            :set restline [:pick $msgTxt ([:find $msgTxt " "]+1) [:len $msgTxt]]; :set msgTxt [:pick $msgTxt 0 [:find $msgTxt " "]]}
          :if ($chatID=$myChatID && $timeAct<$timeStmp) do={
            :set timeAct $timeStmp
            /system script
            :if ([environment find name=$msgTxt]!="" && $launchFnc) do={
              :if (([environment get [find name=$msgTxt] value]="(code)")\
                or [:len [:find [environment get [find name=$msgTxt] value] "(eval"]]>0) do={
                :put "$[$U2T [$T2U]]\tRight time to launch function"
                /log warning "Telegram user $userNm launches function: $msgTxt"
                :execute script="[:parse [\$$msgTxt $restline]]"
              } else={
                :put "$[$U2T [$T2U]]\t'$msgTxt' is a global variable and is not launched"
                /log warning "'$msgTxt' is a global variable and is not launched"}}
            :if ([:pick $msgTxt 0 1]="\5C") do={ # allow to perform emoji
              :set msgTxt [:pick $msgTxt 1 [:len $msgTxt]]
              :if ([:find $msgTxt "\5C"]!=0) do={
                :local first [:pick $msgTxt 0 [:find $msgTxt "\5C"]]
                :local after [:pick $msgTxt ([:find $msgTxt "\5C"]+1) [:len $msgTxt]]
                :set msgTxt ($first.$after)}}
            :if ([find name=$msgTxt]!="" && $launchScr) do={
              :put "$[$U2T [$T2U]]\tRight time to activate script"
              /log warning "Telegram user $userNm activates script: $msgTxt"
              :execute script="[[:parse \"[:parse [/system script get $msgTxt source]] $restline\"]]"}
            :if ([find name=$msgTxt]="" && [environment find name=$msgTxt]="" && $launchCmd) do={
              :put "$[$U2T [$T2U]]\tRight time to execute command"
              /log warning "Telegram user $userNm is trying to execute command: $msgTxt"
              :do {:execute script="[:parse \"/$msgTxt $restline\"]"} on-error={}}
          } else={:put "$[$U2T [$T2U]]\tWrong time to launch"}
        } else={:put "$[$U2T [$T2U]]\tNo command found for this device"}
      } else={:put "$[$U2T [$T2U]]\tCompletion of response from Telegram"}
    } else={:put "$[$U2T [$T2U]]\tNot response from Telegram"}
    :delay 1s; # time difference between command execution and log broadcast

    # part of script body for notifications in Telegram # https://www.reddit.com/r/mikrotik/comments/onusoj/sending_log_alerts_to_telegram/
    :put "$[$U2T [$T2U]]\t*** Stage of broadcasting to Telegram ***"
    :local logIDs [/log find topics~"warning" or topics~"error" or topics~"critical" or topics~"caps" or\
      topics~"wireless" or topics~"dhcp" or topics~"firewall" or message~" logged "]; # list of potentially interesting log entries
    :local outMsg ""; :local strCnt 0; :local logCnt [:len $logIDs]; # counter of suitable log entries
    :if ([:len $timeLog]=0) do={ # when time of last broadcast in Telegram not found ->
      :put "$[$U2T [$T2U]]\tTime of the last log entry was not found"
      :set outMsg "$[$U2T [$T2U] "time"]\tTelegram notification started"; :set strCnt ($strCnt+1)}
    :if ($timeLog>[$T2U]) do={:set timeLog [$T2U]}; # correction when time of last broadcast to Telegram turned out to be from future
    :if ($logCnt>0) do={ # when log entries are available ->
      :set logCnt ($logCnt-1); # index of last log entry
      :local unxTim ""; :local lstTim [$T2U [/log get [:pick $logIDs $logCnt] time]]; # time of last log entry
      :do {
        :local tmpTim [/log get [:pick $logIDs $logCnt] time]; # message time in router format
        :set unxTim [$T2U $tmpTim]; :set tmpTim [$U2T $unxTim "time"]; # message time
        :if ($unxTim>$timeLog) do={ # selection of actualing log entries ->
          :local tmpMsg [/log get [:pick $logIDs $logCnt] message]; # message body
          :if ($sysInfo) do={
            :local preMsg [$ConvSymb [$SysInfo $tmpMsg $tmpTim] "unprint"]; # broadcast SYSTEM information
            :if ($preMsg!="") do={
              :set strCnt ($strCnt+1); :set outMsg "$preMsg\n$outMsg"; :set preMsg [:pick $preMsg 0 50]
              :put "$[$U2T [$T2U]]\tAdded entry: $preMsg"}}
          :if ($userInfo) do={
            :local preMsg [$ConvSymb [$UsrInfo $tmpMsg $tmpTim] "unprint"]; # broadcast USER information
            :if ($preMsg!="") do={
              :set strCnt ($strCnt+1); :set outMsg "$preMsg\n$outMsg"; :set preMsg [:pick $preMsg 0 50]
              :put "$[$U2T [$T2U]]\tAdded entry: $preMsg"}}}
        :set logCnt ($logCnt-1)
      } while=($unxTim>$timeLog && $logCnt>-1 && [:len $outMsg]<40000); # iterating through list of messages
      :if ([:len $timeLog]=0 or [:len $timeLog]>0 && $timeLog!=$lstTim && [:len $outMsg]>8) do={
        :set outMsg [$ConvCP1251 $outMsg]; # converting message to URN format
        :if ([:len $emoDev]!=0) do={:set emoDev ("$emoDev%20$nameID:")} else={:set emoDev ("$nameID:")}
        :local msgCnt 0; :local lenMsg 4095; # length of Telegram message
        :do {
          :if ($strCnt=1) do={:set outMsg "$emoDev%20$outMsg"} else={:set outMsg "$emoDev%0A$outMsg"}; # solitary message for pop-up notification on phone
          :local bufTxt $outMsg
          :if ([:len $bufTxt]>$lenMsg) do={
            :set bufTxt [:pick $bufTxt 0 $lenMsg]; :set outMsg [:pick $outMsg $lenMsg [:len $outMsg]];
          } else={:set outMsg ""}
          :set urlStr "https://api.telegram.org/bot$botID/sendmessage\?chat_id=$myChatID&text=$bufTxt"
          :do {
            :set httpResp [/tool fetch mode=https http-method=post url=$urlStr as-value output=user];
            :set timeLog $lstTim; :set msgCnt ($msgCnt+1)
          } on-error={:put "$[$U2T [$T2U]]\tUnsuccessful sending of message to Telegram"}
        } while ([:len $outMsg]>$lenMsg) 
        :if ($msgCnt>0) do={:put "$[$U2T [$T2U]]\t$msgCnt Telegram messages have been sent"}
      } else={:put "$[$U2T [$T2U]]\tThere are no log entries to send"}
    } else={:put "$[$U2T [$T2U]]\tNecessary log entries were not found"}
    :put "$[$U2T [$T2U]]\tEnd of TLGRM-script"
    :set scriptTlgrm true
  } else={:put "$startTime\tScript already being executed"; :put "$startTime\tEnd of TLGRM-script"}
} on-error={
  :set scriptTlgrm true; :put "Script error: It may be worth checking correctness values of variables botID & myChatID"
  /log warning "Problem in work TLGRM script"}


