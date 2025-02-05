# Repository Information
Name: MIKROTIK-SCRIPT

# Directory Structure
Directory structure:
└── github_repos/MIKROTIK-SCRIPT/
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
    │   │       ├── pack-eb09efaf3991aa16931074bb4360366ec8065710.idx
    │   │       └── pack-eb09efaf3991aa16931074bb4360366ec8065710.pack
    │   ├── packed-refs
    │   └── refs/
    │       ├── heads/
    │       │   └── master
    │       ├── remotes/
    │       │   └── origin/
    │       │       └── HEAD
    │       └── tags/
    ├── 2 Cara Backup Mikrotik melalui Script.txt
    ├── ADDRESS LIST DYNAMIC TO STATIC.txt
    ├── Auto Login WMS wifi.id di Mikrotik.txt
    ├── Auto Update MaxLimit Queue Tree Berdasarkan Avg Rate.txt
    ├── AWS EC2 AMAZON IP LIST MIKROTIK FOR GAME PUBGM OR FORNITE.txt
    ├── Bandwidth yang dibutuhkan untuk Youtube atau Streaming Video.txt
    ├── Bittorrent Torrentwws Torrentwww Regexp layer 7.txt
    ├── Blokir Situs Berdasarkan Keyword pada DNS Cache Mikrotik.txt
    ├── Blokir TRACEROUTE di Mikrotik.txt
    ├── Blokir User melalui MAC address.txt
    ├── BYPASS INTERNET POSITIF DENGAN VPN PPTP.txt
    ├── Cara blokir akses ke Modem.txt
    ├── Cara Blokir Aplikasi Tiktok.txt
    ├── Cara bypass semua IP local agar tidak terlimit.txt
    ├── Cara bypass user hotspot melalui macaddress.txt
    ├── Cara clear log di Mikrotik.txt
    ├── Cara mengaktifkan IP CLOUD untuk remote diluar jaringan.txt
    ├── Cara mengganti identitas di mikrotik  Caption Winbox.txt
    ├── Cara Mengganti System Note di Terminal Mikrotik.txt
    ├── Cara Menonaktifkan Google SSL untuk keperluan Proxy.txt
    ├── Cara rebuild database di User Manager.txt
    ├── Cara reset script dari scheduler atau dari script.txt
    ├── Cara Setting NTP Network Time Protocol di Mikrotik.txt
    ├── Daftar Port Game Online Game Mobile Game Web Game FB.txt
    ├── FailOver 2 ISP dengan Recursive Gateway.txt
    ├── Melimit Bandwidth Multi Login di Simple Queue.txt
    ├── Memaksa agar semua client menggunakan DNS mikrotik.txt
    ├── Memastikan hanya 1 ID hotspot yang boleh login.txt
    ├── Memblokir Serangan Winbox Exploit di Mikrotik.txt
    ├── menampilkan password  Lupa Password User Manager.txt
    ├── Mendapatkan Nama Hari  Get Day Mikrotik.txt
    ├── Mengatasi Kesalahan Passthrough Pada Mangle Mikrotik.txt
    ├── Menghapus semua log di User Manager.txt
    ├── Mengirim IP Public Jika Ada Perubahan IP ke Email.txt
    ├── Merubah Default Admin Password User Manager.txt
    ├── Merubah Nama Interface ether Mikrotik Default.txt
    ├── Merubah path Database User Manager ke USB.txt
    ├── Mikrotik IP Address List FACEBOOK.txt
    ├── Mikrotik IP Address List TWITTER.txt
    ├── Mikrotik IP Address List WHATSAPP.txt
    ├── MIkrotik Speedtest IP Address List.txt
    ├── README.md
    ├── RESET COUNTER MIKROTIK.txt
    ├── Reset database User Manager ke default.txt
    ├── Routing Sederhana dengan FailOver 3 Gateway.txt
    ├── Safe Search Google and Restricted Mode YouTube.txt
    ├── Script Always On top di simple Queue Mikrotik.txt
    ├── SCRIPT DNS CACHE FLUSH.txt
    ├── Script Otomatis Custom Queue Tree dan Mangle Hotspot Mikroti.txt
    ├── Script Otomatis Custom Simple Queue Hotspot Mikrotik.txt
    ├── Script Otomatis Untuk membuat Queue Tree IP 1-255.txt
    ├── Script Otomatis Untuk membuat simple Queue IP 1-255.txt
    ├── Seberapa aman Jaringan Mikrotik kita dari serangan luar.txt
    ├── Speedtest Mangle  layer7 Mikrotik.txt
    ├── Speedtest Regexp Layer 7.txt
    ├── Trik Bermain NoMark Tanpa Mangle di Queue Tree.txt
    └── Trik Load Balancing PCC untuk hotspot.txt


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
	url = https://github.com/alsyundawy/MIKROTIK-SCRIPT.git
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
0000000000000000000000000000000000000000 2382406182f131208b656649141fb5ee30f3422b vivek-dodia <vivek.dodia@icloud.com> 1738605803 -0500	clone: from https://github.com/alsyundawy/MIKROTIK-SCRIPT.git


File: /.git\logs\refs\heads\master
0000000000000000000000000000000000000000 2382406182f131208b656649141fb5ee30f3422b vivek-dodia <vivek.dodia@icloud.com> 1738605803 -0500	clone: from https://github.com/alsyundawy/MIKROTIK-SCRIPT.git


File: /.git\logs\refs\remotes\origin\HEAD
0000000000000000000000000000000000000000 2382406182f131208b656649141fb5ee30f3422b vivek-dodia <vivek.dodia@icloud.com> 1738605803 -0500	clone: from https://github.com/alsyundawy/MIKROTIK-SCRIPT.git


File: /.git\packed-refs
# pack-refs with: peeled fully-peeled sorted 
2382406182f131208b656649141fb5ee30f3422b refs/remotes/origin/master
c2a48af77e1c7d853a8099f1513861a6ec2568b0 refs/remotes/origin/mikrotik
6dc5138ff1beeab8d855f5a41154ab6e00ca77e8 refs/remotes/origin/patch-1


File: /.git\refs\heads\master
2382406182f131208b656649141fb5ee30f3422b


File: /.git\refs\remotes\origin\HEAD
ref: refs/remotes/origin/master


File: /2 Cara Backup Mikrotik melalui Script.txt
# backup semua isi dalam bentuk script (file .rsc) 
/exp file=namafile

# backup semua isi dalam bentuk file terenkirpsi (file .backup) 
/system backup save name=namafile.backup

File: /ADDRESS LIST DYNAMIC TO STATIC.txt
:local list
:local address
/ip firewall address-list
:foreach a in=[find where dynamic=yes] do={
      :set list [get $a list]
      :set address [get $a address]
      remove $a
      add list=$list address=$address disabled=no
}

File: /Auto Login WMS wifi.id di Mikrotik.txt
# Cara Auto Login WMS (wifi.id) di Mikrotik
:if ([/ping address=1.1.1.1 count=5] = 0) do={
/ip dns cache flush
/ip dhcp-client release [find interface=WLAN-INTERFACE]
delay 5
log error ("WMS Down")
:local ip [/ip address get [/ip address find interface="WLAN-INTERFACE"] address];
:local mac [/interface wireless get [ find default-name="WLAN-INTERFACE" ] mac-address];
:local ip [put [:pick $ip 0 [:find $ip "/"]]];
/tool fetch http-method=post http-data="username=username@freeMS&password=password" url=("https://welcome2.wifi.id/wms/?gw_id=GWID&client_mac=xxxxxxxxxxxx&wlan=xxxxxxxxxxxxxxxxxx:SSID%20WMS") keep-result=no;
} else {
log warning ("WMS UP")
}

https://tigabelasnet.blogspot.com

File: /Auto Update MaxLimit Queue Tree Berdasarkan Avg Rate.txt
Contoh kasus:
============
Warnet si palui punya 20PC dan memiliki 5Mbps bandwidth dengan 2 prioritas yang harus dibuat seimbang yaitu antara pemakaian bandwidth game dan browsing. Biasanya saya hanya membuat kalkulasi sederhana dan sifatnya tetap yaitu 3Mbps Browsing dan sisanya 2Mbps game, ini memang dengan tujuan agar trafik bisa berjalan seimbang tanpa lag sama sekali untuk game.

Yang jadi masalah gimana kalau yang main game cuman 2 orang dan 18 lainnya browsing? tentu banyak bandwidth yang mubazir khan :) Disini saya coba selesaikan masalah warnet si palui dengan logika manusia  yang akan kita rancang kedalam logika pemrograman.

LOGIKA SEDERHANA:
==============
1. Warnet si palui saya setting mode Queue tree dengan metode PCQ
2. Dari awal saya setting 3Mbps browsing dan 2Mbps Game
3. Si palui ingin jika user yang main game semisalkan hanya 2 orang dan sisanya 18 orang browsing artinya bandwidth yang hilang untuk browsing sekitar 1500kbps, 500kbps tetap disisakan buat game agar tidak lag.
4. Palui ingin Bandwidth yang tidak digunakan sekitar 1500kbps tadi dialokasikan otomatis kepada user browsing, sayangnya mikrotik tidak ada cara untuk itu dan harus menggunakan scripting agar bisa melakukan tugas tersebut.
5. Script tidak bisa jalan tanpa bantuan scheduler jadi silahkan setting waktu pada scheduler sesuai kebutuhan jangan terlalu cepat jangan juga terlalu lambat.

LOGIKA SCRIPTING SEDERHANA:
#===========================================#
# Scripting version 1.0                                                   
# Scripting Auto Update Max-Limit Queue Tree                           
# by Agus ramadhani - oom@o-om.com    

# info:                                                                   
# sesuaikan dan ganti parent "Game Onlines" dengan parent kalian        
# sesuaikan dan ganti parent "Global Browsing" dengan parent kalian        
#===========================================#
:global SetMaxLimit;
:global BW3M 3000000;
:global BW4M 4000000;
:global BW5M 5000000;
:local avgRate [/ queue tree get "Games Onlines" rate]
:log info "Debug --> $SetMaxLimit";
:log info "Debug --> $avgRate";
:log info "Debug --> ($avgRate < 500000)";
:log info "Debug --> ($avgRate = 0 or $avgRate < 1000)";
:if ($avgRate < 500000)  do={
:if ($avgRate = 0 or $avgRate < 1000) do={
:set SetMaxLimit $BW5M;
:log info "--> Max-limit Browsing berubah ke 5Mbps";
} else={
:set SetMaxLimit $BW4M;
:log info "--> Max-limit Browsing berubah ke 4Mbps";
};
} else={
:set SetMaxLimit $BW3M;
:log info "--> Max-limit Browsing berubah ke 3Mbps";
};

/ queue tree set "Global Browsing" max-limit=$SetMaxLimit
};
#=============================================#
# jika ingin setting pada sub parent                                    
#/queue tree {set [find parent="Global Browsing"] max-limit=$SetMaxLimit
# jika ingin mengambil max-limit pada parent                           
#:local maxLimit [/ queue tree get "Nama parent" max-limit]                
#==============================================#

Ini murni script konsep dasar yang saya buat, silahkan di kembangkan sesuai kebutuhan.

Ref:
http://wiki.mikrotik.com/wiki/Manual:Scripting#Scripting_language_manual
http://wiki.mikrotik.com/wiki/Manual:Scripting-examples

File: /AWS EC2 AMAZON IP LIST MIKROTIK FOR GAME PUBGM OR FORNITE.txt
/ip firewall address-list
add list=AWS-EC2 address=13.32.0.0/15
add list=AWS-EC2 address=13.35.0.0/16
add list=AWS-EC2 address=13.52.0.0/16
add list=AWS-EC2 address=13.53.0.0/16
add list=AWS-EC2 address=13.54.0.0/15
add list=AWS-EC2 address=13.56.0.0/16
add list=AWS-EC2 address=13.57.0.0/16
add list=AWS-EC2 address=13.58.0.0/15
add list=AWS-EC2 address=13.112.0.0/14
add list=AWS-EC2 address=13.124.0.0/16
add list=AWS-EC2 address=13.125.0.0/16
add list=AWS-EC2 address=13.126.0.0/15
add list=AWS-EC2 address=13.208.0.0/16
add list=AWS-EC2 address=13.209.0.0/16
add list=AWS-EC2 address=13.210.0.0/15
add list=AWS-EC2 address=13.228.0.0/15
add list=AWS-EC2 address=13.230.0.0/15
add list=AWS-EC2 address=13.232.0.0/14
add list=AWS-EC2 address=13.236.0.0/14
add list=AWS-EC2 address=13.248.0.0/20
add list=AWS-EC2 address=13.248.16.0/21
add list=AWS-EC2 address=13.248.24.0/22
add list=AWS-EC2 address=13.248.28.0/22
add list=AWS-EC2 address=13.250.0.0/15
add list=AWS-EC2 address=18.130.0.0/16
add list=AWS-EC2 address=18.136.0.0/16
add list=AWS-EC2 address=18.144.0.0/15
add list=AWS-EC2 address=18.179.0.0/16
add list=AWS-EC2 address=18.182.0.0/16
add list=AWS-EC2 address=18.184.0.0/15
add list=AWS-EC2 address=18.188.0.0/16
add list=AWS-EC2 address=18.191.0.0/16
add list=AWS-EC2 address=18.194.0.0/15
add list=AWS-EC2 address=18.196.0.0/15
add list=AWS-EC2 address=18.200.0.0/16
add list=AWS-EC2 address=18.204.0.0/14
add list=AWS-EC2 address=18.208.0.0/13
add list=AWS-EC2 address=18.216.0.0/14
add list=AWS-EC2 address=18.220.0.0/14
add list=AWS-EC2 address=18.224.0.0/14
add list=AWS-EC2 address=18.228.0.0/16
add list=AWS-EC2 address=18.231.0.0/16
add list=AWS-EC2 address=18.232.0.0/14
add list=AWS-EC2 address=18.236.0.0/15
add list=AWS-EC2 address=18.253.0.0/16
add list=AWS-EC2 address=23.20.0.0/14
add list=AWS-EC2 address=27.0.0.0/22
add list=AWS-EC2 address=34.192.0.0/12
add list=AWS-EC2 address=34.208.0.0/12
add list=AWS-EC2 address=34.224.0.0/12
add list=AWS-EC2 address=34.240.0.0/13
add list=AWS-EC2 address=34.248.0.0/13
add list=AWS-EC2 address=35.153.0.0/16
add list=AWS-EC2 address=35.154.0.0/16
add list=AWS-EC2 address=35.155.0.0/16
add list=AWS-EC2 address=35.156.0.0/14
add list=AWS-EC2 address=35.160.0.0/13
add list=AWS-EC2 address=35.168.0.0/13
add list=AWS-EC2 address=35.176.0.0/15
add list=AWS-EC2 address=35.178.0.0/15
add list=AWS-EC2 address=35.180.0.0/16
add list=AWS-EC2 address=35.182.0.0/15
add list=AWS-EC2 address=43.250.192.0/24
add list=AWS-EC2 address=43.250.193.0/24
add list=AWS-EC2 address=46.51.128.0/18
add list=AWS-EC2 address=46.51.192.0/20
add list=AWS-EC2 address=46.51.216.0/21
add list=AWS-EC2 address=46.51.224.0/19
add list=AWS-EC2 address=46.137.0.0/17
add list=AWS-EC2 address=46.137.128.0/18
add list=AWS-EC2 address=46.137.192.0/19
add list=AWS-EC2 address=46.137.224.0/19
add list=AWS-EC2 address=50.16.0.0/15
add list=AWS-EC2 address=50.18.0.0/16
add list=AWS-EC2 address=50.19.0.0/16
add list=AWS-EC2 address=50.112.0.0/16
add list=AWS-EC2 address=52.0.0.0/15
add list=AWS-EC2 address=52.2.0.0/15
add list=AWS-EC2 address=52.4.0.0/14
add list=AWS-EC2 address=52.8.0.0/16
add list=AWS-EC2 address=52.9.0.0/16
add list=AWS-EC2 address=52.10.0.0/15
add list=AWS-EC2 address=52.12.0.0/15
add list=AWS-EC2 address=52.14.0.0/16
add list=AWS-EC2 address=52.15.0.0/16
add list=AWS-EC2 address=52.16.0.0/15
add list=AWS-EC2 address=52.18.0.0/15
add list=AWS-EC2 address=52.20.0.0/14
add list=AWS-EC2 address=52.24.0.0/14
add list=AWS-EC2 address=52.28.0.0/16
add list=AWS-EC2 address=52.29.0.0/16
add list=AWS-EC2 address=52.30.0.0/15
add list=AWS-EC2 address=52.32.0.0/14
add list=AWS-EC2 address=52.36.0.0/14
add list=AWS-EC2 address=52.40.0.0/14
add list=AWS-EC2 address=52.44.0.0/15
add list=AWS-EC2 address=52.46.0.0/18
add list=AWS-EC2 address=52.46.64.0/20
add list=AWS-EC2 address=52.46.80.0/21
add list=AWS-EC2 address=52.46.88.0/22
add list=AWS-EC2 address=52.46.92.0/22
add list=AWS-EC2 address=52.46.96.0/19
add list=AWS-EC2 address=52.46.128.0/19
add list=AWS-EC2 address=52.46.164.0/23
add list=AWS-EC2 address=52.46.168.0/23
add list=AWS-EC2 address=52.46.170.0/23
add list=AWS-EC2 address=52.46.172.0/22
add list=AWS-EC2 address=52.46.176.0/22
add list=AWS-EC2 address=52.46.180.0/22
add list=AWS-EC2 address=52.46.184.0/22
add list=AWS-EC2 address=52.46.192.0/20
add list=AWS-EC2 address=52.46.208.0/21
add list=AWS-EC2 address=52.46.220.0/22
add list=AWS-EC2 address=52.46.224.0/20
add list=AWS-EC2 address=52.46.240.0/22
add list=AWS-EC2 address=52.47.0.0/16
add list=AWS-EC2 address=52.48.0.0/14
add list=AWS-EC2 address=52.52.0.0/15
add list=AWS-EC2 address=52.54.0.0/15
add list=AWS-EC2 address=52.56.0.0/16
add list=AWS-EC2 address=52.57.0.0/16
add list=AWS-EC2 address=52.58.0.0/15
add list=AWS-EC2 address=52.60.0.0/16
add list=AWS-EC2 address=52.61.0.0/16
add list=AWS-EC2 address=52.62.0.0/15
add list=AWS-EC2 address=52.64.0.0/17
add list=AWS-EC2 address=52.64.128.0/17
add list=AWS-EC2 address=52.65.0.0/16
add list=AWS-EC2 address=52.66.0.0/16
add list=AWS-EC2 address=52.67.0.0/16
add list=AWS-EC2 address=52.68.0.0/15
add list=AWS-EC2 address=52.70.0.0/15
add list=AWS-EC2 address=52.72.0.0/15
add list=AWS-EC2 address=52.74.0.0/16
add list=AWS-EC2 address=52.75.0.0/16
add list=AWS-EC2 address=52.76.0.0/17
add list=AWS-EC2 address=52.76.128.0/17
add list=AWS-EC2 address=52.77.0.0/16
add list=AWS-EC2 address=52.78.0.0/16
add list=AWS-EC2 address=52.79.0.0/16
add list=AWS-EC2 address=52.80.0.0/16
add list=AWS-EC2 address=52.81.0.0/16
add list=AWS-EC2 address=52.82.0.0/17
add list=AWS-EC2 address=52.82.176.0/22
add list=AWS-EC2 address=52.82.180.0/22
add list=AWS-EC2 address=52.82.187.0/24
add list=AWS-EC2 address=52.82.188.0/22
add list=AWS-EC2 address=52.82.192.0/18
add list=AWS-EC2 address=52.83.0.0/16
add list=AWS-EC2 address=52.84.0.0/15
add list=AWS-EC2 address=52.86.0.0/15
add list=AWS-EC2 address=52.88.0.0/15
add list=AWS-EC2 address=52.90.0.0/15
add list=AWS-EC2 address=52.92.0.0/20
add list=AWS-EC2 address=52.92.16.0/20
add list=AWS-EC2 address=52.92.32.0/22
add list=AWS-EC2 address=52.92.39.0/24
add list=AWS-EC2 address=52.92.40.0/21
add list=AWS-EC2 address=52.92.48.0/22
add list=AWS-EC2 address=52.92.52.0/22
add list=AWS-EC2 address=52.92.56.0/22
add list=AWS-EC2 address=52.92.60.0/22
add list=AWS-EC2 address=52.92.64.0/22
add list=AWS-EC2 address=52.92.68.0/22
add list=AWS-EC2 address=52.92.72.0/22
add list=AWS-EC2 address=52.92.76.0/22
add list=AWS-EC2 address=52.92.80.0/22
add list=AWS-EC2 address=52.92.84.0/22
add list=AWS-EC2 address=52.92.88.0/22
add list=AWS-EC2 address=52.92.248.0/22
add list=AWS-EC2 address=52.92.252.0/22
add list=AWS-EC2 address=52.93.0.0/24
add list=AWS-EC2 address=52.93.1.0/24
add list=AWS-EC2 address=52.93.2.0/24
add list=AWS-EC2 address=52.93.3.0/24
add list=AWS-EC2 address=52.93.4.0/24
add list=AWS-EC2 address=52.93.5.0/24
add list=AWS-EC2 address=52.93.8.0/22
add list=AWS-EC2 address=52.93.16.0/24
add list=AWS-EC2 address=52.93.17.16/32
add list=AWS-EC2 address=52.93.17.17/32
add list=AWS-EC2 address=52.93.18.178/32
add list=AWS-EC2 address=52.93.18.179/32
add list=AWS-EC2 address=52.93.19.236/32
add list=AWS-EC2 address=52.93.19.237/32
add list=AWS-EC2 address=52.93.20.16/32
add list=AWS-EC2 address=52.93.20.17/32
add list=AWS-EC2 address=52.93.21.14/32
add list=AWS-EC2 address=52.93.21.15/32
add list=AWS-EC2 address=52.93.34.56/32
add list=AWS-EC2 address=52.93.34.57/32
add list=AWS-EC2 address=52.93.37.222/32
add list=AWS-EC2 address=52.93.37.223/32
add list=AWS-EC2 address=52.93.48.22/31
add list=AWS-EC2 address=52.93.51.28/32
add list=AWS-EC2 address=52.93.51.29/32
add list=AWS-EC2 address=52.93.112.34/32
add list=AWS-EC2 address=52.93.112.35/32
add list=AWS-EC2 address=52.93.249.0/24
add list=AWS-EC2 address=52.94.0.0/22
add list=AWS-EC2 address=52.94.4.0/24
add list=AWS-EC2 address=52.94.5.0/24
add list=AWS-EC2 address=52.94.6.0/24
add list=AWS-EC2 address=52.94.7.0/24
add list=AWS-EC2 address=52.94.8.0/24
add list=AWS-EC2 address=52.94.9.0/24
add list=AWS-EC2 address=52.94.10.0/24
add list=AWS-EC2 address=52.94.11.0/24
add list=AWS-EC2 address=52.94.12.0/24
add list=AWS-EC2 address=52.94.13.0/24
add list=AWS-EC2 address=52.94.14.0/24
add list=AWS-EC2 address=52.94.15.0/24
add list=AWS-EC2 address=52.94.16.0/24
add list=AWS-EC2 address=52.94.17.0/24
add list=AWS-EC2 address=52.94.19.0/24
add list=AWS-EC2 address=52.94.20.0/24
add list=AWS-EC2 address=52.94.22.0/24
add list=AWS-EC2 address=52.94.23.0/24
add list=AWS-EC2 address=52.94.24.0/23
add list=AWS-EC2 address=52.94.26.0/23
add list=AWS-EC2 address=52.94.28.0/23
add list=AWS-EC2 address=52.94.32.0/20
add list=AWS-EC2 address=52.94.48.0/20
add list=AWS-EC2 address=52.94.64.0/22
add list=AWS-EC2 address=52.94.68.0/24
add list=AWS-EC2 address=52.94.69.0/24
add list=AWS-EC2 address=52.94.72.0/22
add list=AWS-EC2 address=52.94.76.0/22
add list=AWS-EC2 address=52.94.80.0/20
add list=AWS-EC2 address=52.94.96.0/20
add list=AWS-EC2 address=52.94.112.0/22
add list=AWS-EC2 address=52.94.116.0/22
add list=AWS-EC2 address=52.94.120.0/22
add list=AWS-EC2 address=52.94.124.0/22
add list=AWS-EC2 address=52.94.192.0/22
add list=AWS-EC2 address=52.94.196.0/24
add list=AWS-EC2 address=52.94.197.0/24
add list=AWS-EC2 address=52.94.198.0/28
add list=AWS-EC2 address=52.94.198.16/28
add list=AWS-EC2 address=52.94.198.32/28
add list=AWS-EC2 address=52.94.198.48/28
add list=AWS-EC2 address=52.94.198.64/28
add list=AWS-EC2 address=52.94.198.80/28
add list=AWS-EC2 address=52.94.198.96/28
add list=AWS-EC2 address=52.94.198.112/28
add list=AWS-EC2 address=52.94.198.128/28
add list=AWS-EC2 address=52.94.198.144/28
add list=AWS-EC2 address=52.94.199.0/24
add list=AWS-EC2 address=52.94.200.0/24
add list=AWS-EC2 address=52.94.204.0/23
add list=AWS-EC2 address=52.94.206.0/23
add list=AWS-EC2 address=52.94.208.0/21
add list=AWS-EC2 address=52.94.216.0/21
add list=AWS-EC2 address=52.94.224.0/20
add list=AWS-EC2 address=52.94.240.0/22
add list=AWS-EC2 address=52.94.244.0/22
add list=AWS-EC2 address=52.94.248.0/28
add list=AWS-EC2 address=52.94.248.16/28
add list=AWS-EC2 address=52.94.248.32/28
add list=AWS-EC2 address=52.94.248.48/28
add list=AWS-EC2 address=52.94.248.64/28
add list=AWS-EC2 address=52.94.248.80/28
add list=AWS-EC2 address=52.94.248.96/28
add list=AWS-EC2 address=52.94.248.112/28
add list=AWS-EC2 address=52.94.248.128/28
add list=AWS-EC2 address=52.94.248.144/28
add list=AWS-EC2 address=52.94.248.160/28
add list=AWS-EC2 address=52.94.248.176/28
add list=AWS-EC2 address=52.94.248.192/28
add list=AWS-EC2 address=52.94.248.208/28
add list=AWS-EC2 address=52.94.248.224/28
add list=AWS-EC2 address=52.94.249.0/28
add list=AWS-EC2 address=52.94.249.16/28
add list=AWS-EC2 address=52.94.249.32/28
add list=AWS-EC2 address=52.94.249.64/28
add list=AWS-EC2 address=52.94.249.80/28
add list=AWS-EC2 address=52.94.249.96/28
add list=AWS-EC2 address=52.94.249.112/28
add list=AWS-EC2 address=52.94.249.128/28
add list=AWS-EC2 address=52.94.252.0/23
add list=AWS-EC2 address=52.94.254.0/23
add list=AWS-EC2 address=52.95.0.0/20
add list=AWS-EC2 address=52.95.16.0/21
add list=AWS-EC2 address=52.95.24.0/22
add list=AWS-EC2 address=52.95.28.0/24
add list=AWS-EC2 address=52.95.30.0/23
add list=AWS-EC2 address=52.95.34.0/24
add list=AWS-EC2 address=52.95.35.0/24
add list=AWS-EC2 address=52.95.36.0/22
add list=AWS-EC2 address=52.95.40.0/24
add list=AWS-EC2 address=52.95.48.0/22
add list=AWS-EC2 address=52.95.56.0/22
add list=AWS-EC2 address=52.95.60.0/24
add list=AWS-EC2 address=52.95.61.0/24
add list=AWS-EC2 address=52.95.62.0/24
add list=AWS-EC2 address=52.95.63.0/24
add list=AWS-EC2 address=52.95.64.0/20
add list=AWS-EC2 address=52.95.80.0/20
add list=AWS-EC2 address=52.95.96.0/22
add list=AWS-EC2 address=52.95.100.0/22
add list=AWS-EC2 address=52.95.104.0/22
add list=AWS-EC2 address=52.95.108.0/23
add list=AWS-EC2 address=52.95.110.0/24
add list=AWS-EC2 address=52.95.111.0/24
add list=AWS-EC2 address=52.95.112.0/20
add list=AWS-EC2 address=52.95.128.0/21
add list=AWS-EC2 address=52.95.136.0/23
add list=AWS-EC2 address=52.95.138.0/24
add list=AWS-EC2 address=52.95.142.0/23
add list=AWS-EC2 address=52.95.144.0/24
add list=AWS-EC2 address=52.95.145.0/24
add list=AWS-EC2 address=52.95.146.0/23
add list=AWS-EC2 address=52.95.148.0/23
add list=AWS-EC2 address=52.95.150.0/24
add list=AWS-EC2 address=52.95.154.0/23
add list=AWS-EC2 address=52.95.156.0/24
add list=AWS-EC2 address=52.95.157.0/24
add list=AWS-EC2 address=52.95.158.0/23
add list=AWS-EC2 address=52.95.163.0/24
add list=AWS-EC2 address=52.95.164.0/23
add list=AWS-EC2 address=52.95.166.0/23
add list=AWS-EC2 address=52.95.168.0/24
add list=AWS-EC2 address=52.95.169.0/24
add list=AWS-EC2 address=52.95.170.0/23
add list=AWS-EC2 address=52.95.192.0/20
add list=AWS-EC2 address=52.95.212.0/22
add list=AWS-EC2 address=52.95.225.0/24
add list=AWS-EC2 address=52.95.227.0/24
add list=AWS-EC2 address=52.95.240.0/24
add list=AWS-EC2 address=52.95.241.0/24
add list=AWS-EC2 address=52.95.242.0/24
add list=AWS-EC2 address=52.95.243.0/24
add list=AWS-EC2 address=52.95.244.0/24
add list=AWS-EC2 address=52.95.245.0/24
add list=AWS-EC2 address=52.95.246.0/24
add list=AWS-EC2 address=52.95.247.0/24
add list=AWS-EC2 address=52.95.248.0/24
add list=AWS-EC2 address=52.95.249.0/24
add list=AWS-EC2 address=52.95.250.0/24
add list=AWS-EC2 address=52.95.251.0/24
add list=AWS-EC2 address=52.95.252.0/24
add list=AWS-EC2 address=52.95.253.0/24
add list=AWS-EC2 address=52.95.254.0/24
add list=AWS-EC2 address=52.95.255.0/28
add list=AWS-EC2 address=52.95.255.16/28
add list=AWS-EC2 address=52.95.255.32/28
add list=AWS-EC2 address=52.95.255.48/28
add list=AWS-EC2 address=52.95.255.64/28
add list=AWS-EC2 address=52.95.255.80/28
add list=AWS-EC2 address=52.95.255.96/28
add list=AWS-EC2 address=52.95.255.112/28
add list=AWS-EC2 address=52.95.255.128/28
add list=AWS-EC2 address=52.95.255.144/28
add list=AWS-EC2 address=52.119.160.0/20
add list=AWS-EC2 address=52.119.176.0/21
add list=AWS-EC2 address=52.119.184.0/22
add list=AWS-EC2 address=52.119.188.0/22
add list=AWS-EC2 address=52.119.192.0/22
add list=AWS-EC2 address=52.119.196.0/22
add list=AWS-EC2 address=52.119.205.0/24
add list=AWS-EC2 address=52.119.206.0/23
add list=AWS-EC2 address=52.119.208.0/23
add list=AWS-EC2 address=52.119.210.0/23
add list=AWS-EC2 address=52.119.212.0/23
add list=AWS-EC2 address=52.119.214.0/23
add list=AWS-EC2 address=52.119.216.0/21
add list=AWS-EC2 address=52.119.224.0/21
add list=AWS-EC2 address=52.119.232.0/21
add list=AWS-EC2 address=52.119.240.0/21
add list=AWS-EC2 address=52.119.252.0/22
add list=AWS-EC2 address=52.144.192.0/26
add list=AWS-EC2 address=52.144.192.64/26
add list=AWS-EC2 address=52.144.192.128/26
add list=AWS-EC2 address=52.144.192.192/26
add list=AWS-EC2 address=52.144.193.0/26
add list=AWS-EC2 address=52.144.193.64/26
add list=AWS-EC2 address=52.144.193.128/26
add list=AWS-EC2 address=52.144.194.0/26
add list=AWS-EC2 address=52.144.194.64/26
add list=AWS-EC2 address=52.144.194.128/26
add list=AWS-EC2 address=52.144.194.192/26
add list=AWS-EC2 address=52.144.195.0/26
add list=AWS-EC2 address=52.144.196.192/26
add list=AWS-EC2 address=52.144.208.64/26
add list=AWS-EC2 address=52.144.208.128/26
add list=AWS-EC2 address=52.144.208.192/26
add list=AWS-EC2 address=52.144.209.0/26
add list=AWS-EC2 address=52.144.209.64/26
add list=AWS-EC2 address=52.144.209.128/26
add list=AWS-EC2 address=52.144.209.192/26
add list=AWS-EC2 address=52.144.210.0/26
add list=AWS-EC2 address=52.144.210.64/26
add list=AWS-EC2 address=52.144.210.128/26
add list=AWS-EC2 address=52.144.210.192/26
add list=AWS-EC2 address=52.144.211.0/26
add list=AWS-EC2 address=52.144.224.64/26
add list=AWS-EC2 address=52.144.224.128/26
add list=AWS-EC2 address=52.144.225.64/26
add list=AWS-EC2 address=52.144.225.128/26
add list=AWS-EC2 address=52.192.0.0/15
add list=AWS-EC2 address=52.194.0.0/15
add list=AWS-EC2 address=52.196.0.0/14
add list=AWS-EC2 address=52.200.0.0/13
add list=AWS-EC2 address=52.208.0.0/13
add list=AWS-EC2 address=52.216.0.0/15
add list=AWS-EC2 address=52.218.0.0/17
add list=AWS-EC2 address=52.218.128.0/17
add list=AWS-EC2 address=52.219.0.0/20
add list=AWS-EC2 address=52.219.16.0/22
add list=AWS-EC2 address=52.219.20.0/22
add list=AWS-EC2 address=52.219.24.0/21
add list=AWS-EC2 address=52.219.32.0/21
add list=AWS-EC2 address=52.219.40.0/22
add list=AWS-EC2 address=52.219.44.0/22
add list=AWS-EC2 address=52.219.56.0/22
add list=AWS-EC2 address=52.219.60.0/23
add list=AWS-EC2 address=52.219.62.0/23
add list=AWS-EC2 address=52.219.64.0/22
add list=AWS-EC2 address=52.219.68.0/22
add list=AWS-EC2 address=52.219.72.0/22
add list=AWS-EC2 address=52.219.76.0/22
add list=AWS-EC2 address=52.219.80.0/20
add list=AWS-EC2 address=52.219.96.0/20
add list=AWS-EC2 address=52.220.0.0/15
add list=AWS-EC2 address=52.222.0.0/17
add list=AWS-EC2 address=52.222.128.0/17
add list=AWS-EC2 address=54.64.0.0/15
add list=AWS-EC2 address=54.66.0.0/16
add list=AWS-EC2 address=54.67.0.0/16
add list=AWS-EC2 address=54.68.0.0/14
add list=AWS-EC2 address=54.72.0.0/15
add list=AWS-EC2 address=54.74.0.0/15
add list=AWS-EC2 address=54.76.0.0/15
add list=AWS-EC2 address=54.78.0.0/16
add list=AWS-EC2 address=54.79.0.0/16
add list=AWS-EC2 address=54.80.0.0/13
add list=AWS-EC2 address=54.88.0.0/14
add list=AWS-EC2 address=54.92.0.0/17
add list=AWS-EC2 address=54.92.128.0/17
add list=AWS-EC2 address=54.93.0.0/16
add list=AWS-EC2 address=54.94.0.0/16
add list=AWS-EC2 address=54.95.0.0/16
add list=AWS-EC2 address=54.144.0.0/14
add list=AWS-EC2 address=54.148.0.0/15
add list=AWS-EC2 address=54.150.0.0/16
add list=AWS-EC2 address=54.151.0.0/17
add list=AWS-EC2 address=54.151.128.0/17
add list=AWS-EC2 address=54.152.0.0/16
add list=AWS-EC2 address=54.153.0.0/17
add list=AWS-EC2 address=54.153.128.0/17
add list=AWS-EC2 address=54.154.0.0/16
add list=AWS-EC2 address=54.155.0.0/16
add list=AWS-EC2 address=54.156.0.0/14
add list=AWS-EC2 address=54.160.0.0/13
add list=AWS-EC2 address=54.168.0.0/16
add list=AWS-EC2 address=54.169.0.0/16
add list=AWS-EC2 address=54.170.0.0/15
add list=AWS-EC2 address=54.172.0.0/15
add list=AWS-EC2 address=54.174.0.0/15
add list=AWS-EC2 address=54.176.0.0/15
add list=AWS-EC2 address=54.178.0.0/16
add list=AWS-EC2 address=54.179.0.0/16
add list=AWS-EC2 address=54.180.0.0/15
add list=AWS-EC2 address=54.182.0.0/16
add list=AWS-EC2 address=54.183.0.0/16
add list=AWS-EC2 address=54.184.0.0/13
add list=AWS-EC2 address=54.192.0.0/16
add list=AWS-EC2 address=54.193.0.0/16
add list=AWS-EC2 address=54.194.0.0/15
add list=AWS-EC2 address=54.196.0.0/15
add list=AWS-EC2 address=54.198.0.0/16
add list=AWS-EC2 address=54.199.0.0/16
add list=AWS-EC2 address=54.200.0.0/15
add list=AWS-EC2 address=54.202.0.0/15
add list=AWS-EC2 address=54.204.0.0/15
add list=AWS-EC2 address=54.206.0.0/16
add list=AWS-EC2 address=54.207.0.0/16
add list=AWS-EC2 address=54.208.0.0/15
add list=AWS-EC2 address=54.210.0.0/15
add list=AWS-EC2 address=54.212.0.0/15
add list=AWS-EC2 address=54.214.0.0/16
add list=AWS-EC2 address=54.215.0.0/16
add list=AWS-EC2 address=54.216.0.0/15
add list=AWS-EC2 address=54.218.0.0/16
add list=AWS-EC2 address=54.219.0.0/16
add list=AWS-EC2 address=54.220.0.0/16
add list=AWS-EC2 address=54.221.0.0/16
add list=AWS-EC2 address=54.222.0.0/19
add list=AWS-EC2 address=54.222.32.0/22
add list=AWS-EC2 address=54.222.36.0/22
add list=AWS-EC2 address=54.222.48.0/22
add list=AWS-EC2 address=54.222.57.0/24
add list=AWS-EC2 address=54.222.58.0/28
add list=AWS-EC2 address=54.222.128.0/17
add list=AWS-EC2 address=54.223.0.0/16
add list=AWS-EC2 address=54.224.0.0/15
add list=AWS-EC2 address=54.226.0.0/15
add list=AWS-EC2 address=54.228.0.0/16
add list=AWS-EC2 address=54.229.0.0/16
add list=AWS-EC2 address=54.230.0.0/16
add list=AWS-EC2 address=54.231.0.0/17
add list=AWS-EC2 address=54.231.128.0/19
add list=AWS-EC2 address=54.231.160.0/19
add list=AWS-EC2 address=54.231.192.0/20
add list=AWS-EC2 address=54.231.224.0/21
add list=AWS-EC2 address=54.231.232.0/21
add list=AWS-EC2 address=54.231.240.0/22
add list=AWS-EC2 address=54.231.244.0/22
add list=AWS-EC2 address=54.231.248.0/22
add list=AWS-EC2 address=54.231.252.0/24
add list=AWS-EC2 address=54.231.253.0/24
add list=AWS-EC2 address=54.232.0.0/16
add list=AWS-EC2 address=54.233.0.0/18
add list=AWS-EC2 address=54.233.64.0/18
add list=AWS-EC2 address=54.233.128.0/17
add list=AWS-EC2 address=54.234.0.0/15
add list=AWS-EC2 address=54.236.0.0/15
add list=AWS-EC2 address=54.238.0.0/16
add list=AWS-EC2 address=54.239.0.0/28
add list=AWS-EC2 address=54.239.0.16/28
add list=AWS-EC2 address=54.239.0.32/28
add list=AWS-EC2 address=54.239.0.48/28
add list=AWS-EC2 address=54.239.0.64/28
add list=AWS-EC2 address=54.239.0.80/28
add list=AWS-EC2 address=54.239.0.96/28
add list=AWS-EC2 address=54.239.0.112/28
add list=AWS-EC2 address=54.239.0.128/28
add list=AWS-EC2 address=54.239.0.144/28
add list=AWS-EC2 address=54.239.0.160/28
add list=AWS-EC2 address=54.239.0.176/28
add list=AWS-EC2 address=54.239.0.192/28
add list=AWS-EC2 address=54.239.0.208/28
add list=AWS-EC2 address=54.239.0.224/28
add list=AWS-EC2 address=54.239.0.240/28
add list=AWS-EC2 address=54.239.1.0/28
add list=AWS-EC2 address=54.239.1.16/28
add list=AWS-EC2 address=54.239.1.48/28
add list=AWS-EC2 address=54.239.1.64/28
add list=AWS-EC2 address=54.239.2.0/23
add list=AWS-EC2 address=54.239.4.0/22
add list=AWS-EC2 address=54.239.8.0/21
add list=AWS-EC2 address=54.239.16.0/20
add list=AWS-EC2 address=54.239.32.0/21
add list=AWS-EC2 address=54.239.48.0/22
add list=AWS-EC2 address=54.239.52.0/23
add list=AWS-EC2 address=54.239.54.0/23
add list=AWS-EC2 address=54.239.56.0/21
add list=AWS-EC2 address=54.239.96.0/24
add list=AWS-EC2 address=54.239.98.0/24
add list=AWS-EC2 address=54.239.99.0/24
add list=AWS-EC2 address=54.239.100.0/23
add list=AWS-EC2 address=54.239.104.0/23
add list=AWS-EC2 address=54.239.106.252/32
add list=AWS-EC2 address=54.239.106.253/32
add list=AWS-EC2 address=54.239.107.252/32
add list=AWS-EC2 address=54.239.107.253/32
add list=AWS-EC2 address=54.239.108.0/22
add list=AWS-EC2 address=54.239.116.0/22
add list=AWS-EC2 address=54.239.120.0/21
add list=AWS-EC2 address=54.239.128.0/18
add list=AWS-EC2 address=54.239.192.0/19
add list=AWS-EC2 address=54.240.128.0/18
add list=AWS-EC2 address=54.240.192.0/22
add list=AWS-EC2 address=54.240.196.0/24
add list=AWS-EC2 address=54.240.197.0/24
add list=AWS-EC2 address=54.240.198.0/24
add list=AWS-EC2 address=54.240.199.0/24
add list=AWS-EC2 address=54.240.200.0/24
add list=AWS-EC2 address=54.240.202.0/24
add list=AWS-EC2 address=54.240.203.0/24
add list=AWS-EC2 address=54.240.204.0/22
add list=AWS-EC2 address=54.240.208.0/22
add list=AWS-EC2 address=54.240.212.0/22
add list=AWS-EC2 address=54.240.216.0/22
add list=AWS-EC2 address=54.240.220.0/22
add list=AWS-EC2 address=54.240.225.0/24
add list=AWS-EC2 address=54.240.226.0/24
add list=AWS-EC2 address=54.240.227.0/24
add list=AWS-EC2 address=54.240.228.0/23
add list=AWS-EC2 address=54.240.230.0/23
add list=AWS-EC2 address=54.240.232.0/22
add list=AWS-EC2 address=54.240.244.0/22
add list=AWS-EC2 address=54.240.248.0/21
add list=AWS-EC2 address=54.241.0.0/16
add list=AWS-EC2 address=54.242.0.0/15
add list=AWS-EC2 address=54.244.0.0/16
add list=AWS-EC2 address=54.245.0.0/16
add list=AWS-EC2 address=54.246.0.0/16
add list=AWS-EC2 address=54.247.0.0/16
add list=AWS-EC2 address=54.248.0.0/15
add list=AWS-EC2 address=54.250.0.0/16
add list=AWS-EC2 address=54.251.0.0/16
add list=AWS-EC2 address=54.252.0.0/16
add list=AWS-EC2 address=54.253.0.0/16
add list=AWS-EC2 address=54.254.0.0/16
add list=AWS-EC2 address=54.255.0.0/16
add list=AWS-EC2 address=67.202.0.0/18
add list=AWS-EC2 address=70.132.0.0/18
add list=AWS-EC2 address=71.152.0.0/17
add list=AWS-EC2 address=72.21.192.0/19
add list=AWS-EC2 address=72.44.32.0/19
add list=AWS-EC2 address=75.101.128.0/17
add list=AWS-EC2 address=79.125.0.0/17
add list=AWS-EC2 address=87.238.80.0/21
add list=AWS-EC2 address=96.127.0.0/17
add list=AWS-EC2 address=103.4.8.0/21
add list=AWS-EC2 address=103.8.172.0/22
add list=AWS-EC2 address=103.246.148.0/23
add list=AWS-EC2 address=103.246.150.0/23
add list=AWS-EC2 address=107.20.0.0/14
add list=AWS-EC2 address=122.248.192.0/18
add list=AWS-EC2 address=143.204.0.0/16
add list=AWS-EC2 address=172.96.97.0/24
add list=AWS-EC2 address=172.96.98.0/24
add list=AWS-EC2 address=174.129.0.0/16
add list=AWS-EC2 address=175.41.128.0/18
add list=AWS-EC2 address=175.41.192.0/18
add list=AWS-EC2 address=176.32.64.0/19
add list=AWS-EC2 address=176.32.96.0/21
add list=AWS-EC2 address=176.32.104.0/21
add list=AWS-EC2 address=176.32.112.0/21
add list=AWS-EC2 address=176.32.120.0/22
add list=AWS-EC2 address=176.32.125.0/25
add list=AWS-EC2 address=176.34.0.0/19
add list=AWS-EC2 address=176.34.32.0/19
add list=AWS-EC2 address=176.34.64.0/18
add list=AWS-EC2 address=176.34.128.0/17
add list=AWS-EC2 address=177.71.128.0/17
add list=AWS-EC2 address=177.72.240.0/21
add list=AWS-EC2 address=178.236.0.0/20
add list=AWS-EC2 address=184.72.0.0/18
add list=AWS-EC2 address=184.72.64.0/18
add list=AWS-EC2 address=184.72.128.0/17
add list=AWS-EC2 address=184.73.0.0/16
add list=AWS-EC2 address=184.169.128.0/17
add list=AWS-EC2 address=185.48.120.0/22
add list=AWS-EC2 address=185.143.16.0/24
add list=AWS-EC2 address=203.83.220.0/22
add list=AWS-EC2 address=204.236.128.0/18
add list=AWS-EC2 address=204.236.192.0/18
add list=AWS-EC2 address=204.246.160.0/22
add list=AWS-EC2 address=204.246.164.0/22
add list=AWS-EC2 address=204.246.168.0/22
add list=AWS-EC2 address=204.246.174.0/23
add list=AWS-EC2 address=204.246.176.0/20
add list=AWS-EC2 address=205.251.192.0/19
add list=AWS-EC2 address=205.251.224.0/22
add list=AWS-EC2 address=205.251.228.0/22
add list=AWS-EC2 address=205.251.232.0/22
add list=AWS-EC2 address=205.251.236.0/22
add list=AWS-EC2 address=205.251.240.0/22
add list=AWS-EC2 address=205.251.244.0/23
add list=AWS-EC2 address=205.251.246.0/24
add list=AWS-EC2 address=205.251.247.0/24
add list=AWS-EC2 address=205.251.248.0/24
add list=AWS-EC2 address=205.251.249.0/24
add list=AWS-EC2 address=205.251.250.0/23
add list=AWS-EC2 address=205.251.252.0/23
add list=AWS-EC2 address=205.251.254.0/24
add list=AWS-EC2 address=207.171.160.0/20
add list=AWS-EC2 address=207.171.176.0/20
add list=AWS-EC2 address=216.137.32.0/19
add list=AWS-EC2 address=216.182.224.0/21
add list=AWS-EC2 address=216.182.232.0/22
add list=AWS-EC2 address=216.182.236.0/23
add list=AWS-EC2 address=216.182.238.0/23
add list=AWS-EC2 address=54.183.255.128/26
add list=AWS-EC2 address=54.228.16.0/26
add list=AWS-EC2 address=54.232.40.64/26
add list=AWS-EC2 address=54.241.32.64/26
add list=AWS-EC2 address=54.243.31.192/26
add list=AWS-EC2 address=54.244.52.192/26
add list=AWS-EC2 address=54.245.168.0/26
add list=AWS-EC2 address=54.248.220.0/26
add list=AWS-EC2 address=54.250.253.192/26
add list=AWS-EC2 address=54.251.31.128/26
add list=AWS-EC2 address=54.252.79.128/26
add list=AWS-EC2 address=54.252.254.192/26
add list=AWS-EC2 address=54.255.254.192/26
add list=AWS-EC2 address=107.23.255.0/26
add list=AWS-EC2 address=176.34.159.192/26
add list=AWS-EC2 address=177.71.207.128/26
add list=AWS-EC2 address=52.82.188.0/22
add list=AWS-EC2 address=52.92.0.0/20
add list=AWS-EC2 address=52.92.16.0/20
add list=AWS-EC2 address=52.92.32.0/22
add list=AWS-EC2 address=52.92.39.0/24
add list=AWS-EC2 address=52.92.40.0/21
add list=AWS-EC2 address=52.92.48.0/22
add list=AWS-EC2 address=52.92.52.0/22
add list=AWS-EC2 address=52.92.56.0/22
add list=AWS-EC2 address=52.92.60.0/22
add list=AWS-EC2 address=52.92.64.0/22
add list=AWS-EC2 address=52.92.68.0/22
add list=AWS-EC2 address=52.92.72.0/22
add list=AWS-EC2 address=52.92.76.0/22
add list=AWS-EC2 address=52.92.80.0/22
add list=AWS-EC2 address=52.92.84.0/22
add list=AWS-EC2 address=52.92.88.0/22
add list=AWS-EC2 address=52.92.248.0/22
add list=AWS-EC2 address=52.92.252.0/22
add list=AWS-EC2 address=52.95.128.0/21
add list=AWS-EC2 address=52.95.136.0/23
add list=AWS-EC2 address=52.95.138.0/24
add list=AWS-EC2 address=52.95.142.0/23
add list=AWS-EC2 address=52.95.144.0/24
add list=AWS-EC2 address=52.95.145.0/24
add list=AWS-EC2 address=52.95.146.0/23
add list=AWS-EC2 address=52.95.148.0/23
add list=AWS-EC2 address=52.95.150.0/24
add list=AWS-EC2 address=52.95.154.0/23
add list=AWS-EC2 address=52.95.156.0/24
add list=AWS-EC2 address=52.95.157.0/24
add list=AWS-EC2 address=52.95.158.0/23
add list=AWS-EC2 address=52.95.163.0/24
add list=AWS-EC2 address=52.95.164.0/23
add list=AWS-EC2 address=52.95.166.0/23
add list=AWS-EC2 address=52.95.168.0/24
add list=AWS-EC2 address=52.95.169.0/24
add list=AWS-EC2 address=52.95.170.0/23
add list=AWS-EC2 address=52.216.0.0/15
add list=AWS-EC2 address=52.218.0.0/17
add list=AWS-EC2 address=52.218.128.0/17
add list=AWS-EC2 address=52.219.0.0/20
add list=AWS-EC2 address=52.219.16.0/22
add list=AWS-EC2 address=52.219.20.0/22
add list=AWS-EC2 address=52.219.24.0/21
add list=AWS-EC2 address=52.219.32.0/21
add list=AWS-EC2 address=52.219.40.0/22
add list=AWS-EC2 address=52.219.44.0/22
add list=AWS-EC2 address=52.219.56.0/22
add list=AWS-EC2 address=52.219.60.0/23
add list=AWS-EC2 address=52.219.62.0/23
add list=AWS-EC2 address=52.219.64.0/22
add list=AWS-EC2 address=52.219.68.0/22
add list=AWS-EC2 address=52.219.72.0/22
add list=AWS-EC2 address=52.219.76.0/22
add list=AWS-EC2 address=52.219.80.0/20
add list=AWS-EC2 address=52.219.96.0/20
add list=AWS-EC2 address=54.222.48.0/22
add list=AWS-EC2 address=54.231.0.0/17
add list=AWS-EC2 address=54.231.128.0/19
add list=AWS-EC2 address=54.231.160.0/19
add list=AWS-EC2 address=54.231.192.0/20
add list=AWS-EC2 address=54.231.224.0/21
add list=AWS-EC2 address=54.231.232.0/21
add list=AWS-EC2 address=54.231.240.0/22
add list=AWS-EC2 address=54.231.248.0/22
add list=AWS-EC2 address=54.231.252.0/24
add list=AWS-EC2 address=54.231.253.0/24
add list=AWS-EC2 address=13.52.0.0/16
add list=AWS-EC2 address=13.53.0.0/16
add list=AWS-EC2 address=13.54.0.0/15
add list=AWS-EC2 address=13.56.0.0/16
add list=AWS-EC2 address=13.57.0.0/16
add list=AWS-EC2 address=13.58.0.0/15
add list=AWS-EC2 address=13.112.0.0/14
add list=AWS-EC2 address=13.124.0.0/16
add list=AWS-EC2 address=13.125.0.0/16
add list=AWS-EC2 address=13.126.0.0/15
add list=AWS-EC2 address=13.208.0.0/16
add list=AWS-EC2 address=13.209.0.0/16
add list=AWS-EC2 address=13.210.0.0/15
add list=AWS-EC2 address=13.228.0.0/15
add list=AWS-EC2 address=13.230.0.0/15
add list=AWS-EC2 address=13.232.0.0/14
add list=AWS-EC2 address=13.236.0.0/14
add list=AWS-EC2 address=13.250.0.0/15
add list=AWS-EC2 address=18.130.0.0/16
add list=AWS-EC2 address=18.136.0.0/16
add list=AWS-EC2 address=18.144.0.0/15
add list=AWS-EC2 address=18.179.0.0/16
add list=AWS-EC2 address=18.182.0.0/16
add list=AWS-EC2 address=18.184.0.0/15
add list=AWS-EC2 address=18.188.0.0/16
add list=AWS-EC2 address=18.191.0.0/16
add list=AWS-EC2 address=18.194.0.0/15
add list=AWS-EC2 address=18.196.0.0/15
add list=AWS-EC2 address=18.200.0.0/16
add list=AWS-EC2 address=18.204.0.0/14
add list=AWS-EC2 address=18.208.0.0/13
add list=AWS-EC2 address=18.216.0.0/14
add list=AWS-EC2 address=18.220.0.0/14
add list=AWS-EC2 address=18.224.0.0/14
add list=AWS-EC2 address=18.228.0.0/16
add list=AWS-EC2 address=18.231.0.0/16
add list=AWS-EC2 address=18.232.0.0/14
add list=AWS-EC2 address=18.236.0.0/15
add list=AWS-EC2 address=18.253.0.0/16
add list=AWS-EC2 address=23.20.0.0/14
add list=AWS-EC2 address=34.192.0.0/12
add list=AWS-EC2 address=34.208.0.0/12
add list=AWS-EC2 address=34.224.0.0/12
add list=AWS-EC2 address=34.240.0.0/13
add list=AWS-EC2 address=34.248.0.0/13
add list=AWS-EC2 address=35.153.0.0/16
add list=AWS-EC2 address=35.154.0.0/16
add list=AWS-EC2 address=35.155.0.0/16
add list=AWS-EC2 address=35.156.0.0/14
add list=AWS-EC2 address=35.160.0.0/13
add list=AWS-EC2 address=35.168.0.0/13
add list=AWS-EC2 address=35.176.0.0/15
add list=AWS-EC2 address=35.178.0.0/15
add list=AWS-EC2 address=35.180.0.0/16
add list=AWS-EC2 address=35.182.0.0/15
add list=AWS-EC2 address=46.51.128.0/18
add list=AWS-EC2 address=46.51.192.0/20
add list=AWS-EC2 address=46.51.216.0/21
add list=AWS-EC2 address=46.51.224.0/19
add list=AWS-EC2 address=46.137.0.0/17
add list=AWS-EC2 address=46.137.128.0/18
add list=AWS-EC2 address=46.137.192.0/19
add list=AWS-EC2 address=46.137.224.0/19
add list=AWS-EC2 address=50.16.0.0/15
add list=AWS-EC2 address=50.18.0.0/16
add list=AWS-EC2 address=50.19.0.0/16
add list=AWS-EC2 address=50.112.0.0/16
add list=AWS-EC2 address=52.0.0.0/15
add list=AWS-EC2 address=52.2.0.0/15
add list=AWS-EC2 address=52.4.0.0/14
add list=AWS-EC2 address=52.8.0.0/16
add list=AWS-EC2 address=52.9.0.0/16
add list=AWS-EC2 address=52.10.0.0/15
add list=AWS-EC2 address=52.12.0.0/15
add list=AWS-EC2 address=52.14.0.0/16
add list=AWS-EC2 address=52.15.0.0/16
add list=AWS-EC2 address=52.16.0.0/15
add list=AWS-EC2 address=52.18.0.0/15
add list=AWS-EC2 address=52.20.0.0/14
add list=AWS-EC2 address=52.24.0.0/14
add list=AWS-EC2 address=52.28.0.0/16
add list=AWS-EC2 address=52.29.0.0/16
add list=AWS-EC2 address=52.30.0.0/15
add list=AWS-EC2 address=52.32.0.0/14
add list=AWS-EC2 address=52.36.0.0/14
add list=AWS-EC2 address=52.40.0.0/14
add list=AWS-EC2 address=52.44.0.0/15
add list=AWS-EC2 address=52.46.180.0/22
add list=AWS-EC2 address=52.46.184.0/22
add list=AWS-EC2 address=52.47.0.0/16
add list=AWS-EC2 address=52.48.0.0/14
add list=AWS-EC2 address=52.52.0.0/15
add list=AWS-EC2 address=52.54.0.0/15
add list=AWS-EC2 address=52.56.0.0/16
add list=AWS-EC2 address=52.57.0.0/16
add list=AWS-EC2 address=52.58.0.0/15
add list=AWS-EC2 address=52.60.0.0/16
add list=AWS-EC2 address=52.61.0.0/16
add list=AWS-EC2 address=52.62.0.0/15
add list=AWS-EC2 address=52.64.0.0/17
add list=AWS-EC2 address=52.64.128.0/17
add list=AWS-EC2 address=52.65.0.0/16
add list=AWS-EC2 address=52.66.0.0/16
add list=AWS-EC2 address=52.67.0.0/16
add list=AWS-EC2 address=52.68.0.0/15
add list=AWS-EC2 address=52.70.0.0/15
add list=AWS-EC2 address=52.72.0.0/15
add list=AWS-EC2 address=52.74.0.0/16
add list=AWS-EC2 address=52.75.0.0/16
add list=AWS-EC2 address=52.76.0.0/17
add list=AWS-EC2 address=52.76.128.0/17
add list=AWS-EC2 address=52.77.0.0/16
add list=AWS-EC2 address=52.78.0.0/16
add list=AWS-EC2 address=52.79.0.0/16
add list=AWS-EC2 address=52.80.0.0/16
add list=AWS-EC2 address=52.81.0.0/16
add list=AWS-EC2 address=52.82.0.0/17
add list=AWS-EC2 address=52.82.176.0/22
add list=AWS-EC2 address=52.82.180.0/22
add list=AWS-EC2 address=52.83.0.0/16
add list=AWS-EC2 address=52.86.0.0/15
add list=AWS-EC2 address=52.88.0.0/15
add list=AWS-EC2 address=52.90.0.0/15
add list=AWS-EC2 address=52.94.116.0/22
add list=AWS-EC2 address=52.94.248.0/28
add list=AWS-EC2 address=52.94.248.16/28
add list=AWS-EC2 address=52.94.248.32/28
add list=AWS-EC2 address=52.94.248.48/28
add list=AWS-EC2 address=52.94.248.64/28
add list=AWS-EC2 address=52.94.248.80/28
add list=AWS-EC2 address=52.94.248.96/28
add list=AWS-EC2 address=52.94.248.112/28
add list=AWS-EC2 address=52.94.248.128/28
add list=AWS-EC2 address=52.94.248.144/28
add list=AWS-EC2 address=52.94.248.160/28
add list=AWS-EC2 address=52.94.248.176/28
add list=AWS-EC2 address=52.94.248.192/28
add list=AWS-EC2 address=52.94.248.208/28
add list=AWS-EC2 address=52.94.248.224/28
add list=AWS-EC2 address=52.94.249.0/28
add list=AWS-EC2 address=52.94.249.16/28
add list=AWS-EC2 address=52.94.249.32/28
add list=AWS-EC2 address=52.94.249.64/28
add list=AWS-EC2 address=52.94.249.80/28
add list=AWS-EC2 address=52.94.249.96/28
add list=AWS-EC2 address=52.94.249.112/28
add list=AWS-EC2 address=52.94.249.128/28
add list=AWS-EC2 address=52.95.225.0/24
add list=AWS-EC2 address=52.95.227.0/24
add list=AWS-EC2 address=52.95.240.0/24
add list=AWS-EC2 address=52.95.241.0/24
add list=AWS-EC2 address=52.95.242.0/24
add list=AWS-EC2 address=52.95.243.0/24
add list=AWS-EC2 address=52.95.244.0/24
add list=AWS-EC2 address=52.95.245.0/24
add list=AWS-EC2 address=52.95.246.0/24
add list=AWS-EC2 address=52.95.247.0/24
add list=AWS-EC2 address=52.95.248.0/24
add list=AWS-EC2 address=52.95.249.0/24
add list=AWS-EC2 address=52.95.250.0/24
add list=AWS-EC2 address=52.95.251.0/24
add list=AWS-EC2 address=52.95.252.0/24
add list=AWS-EC2 address=52.95.253.0/24
add list=AWS-EC2 address=52.95.254.0/24
add list=AWS-EC2 address=52.95.255.0/28
add list=AWS-EC2 address=52.95.255.16/28
add list=AWS-EC2 address=52.95.255.32/28
add list=AWS-EC2 address=52.95.255.48/28
add list=AWS-EC2 address=52.95.255.64/28
add list=AWS-EC2 address=52.95.255.80/28
add list=AWS-EC2 address=52.95.255.96/28
add list=AWS-EC2 address=52.95.255.112/28
add list=AWS-EC2 address=52.95.255.128/28
add list=AWS-EC2 address=52.95.255.144/28
add list=AWS-EC2 address=52.119.205.0/24
add list=AWS-EC2 address=52.192.0.0/15
add list=AWS-EC2 address=52.194.0.0/15
add list=AWS-EC2 address=52.196.0.0/14
add list=AWS-EC2 address=52.200.0.0/13
add list=AWS-EC2 address=52.208.0.0/13
add list=AWS-EC2 address=52.220.0.0/15
add list=AWS-EC2 address=52.222.0.0/17
add list=AWS-EC2 address=54.64.0.0/15
add list=AWS-EC2 address=54.66.0.0/16
add list=AWS-EC2 address=54.67.0.0/16
add list=AWS-EC2 address=54.68.0.0/14
add list=AWS-EC2 address=54.72.0.0/15
add list=AWS-EC2 address=54.74.0.0/15
add list=AWS-EC2 address=54.76.0.0/15
add list=AWS-EC2 address=54.78.0.0/16
add list=AWS-EC2 address=54.79.0.0/16
add list=AWS-EC2 address=54.80.0.0/13
add list=AWS-EC2 address=54.88.0.0/14
add list=AWS-EC2 address=54.92.0.0/17
add list=AWS-EC2 address=54.92.128.0/17
add list=AWS-EC2 address=54.93.0.0/16
add list=AWS-EC2 address=54.94.0.0/16
add list=AWS-EC2 address=54.95.0.0/16
add list=AWS-EC2 address=54.144.0.0/14
add list=AWS-EC2 address=54.148.0.0/15
add list=AWS-EC2 address=54.150.0.0/16
add list=AWS-EC2 address=54.151.0.0/17
add list=AWS-EC2 address=54.151.128.0/17
add list=AWS-EC2 address=54.152.0.0/16
add list=AWS-EC2 address=54.153.0.0/17
add list=AWS-EC2 address=54.153.128.0/17
add list=AWS-EC2 address=54.154.0.0/16
add list=AWS-EC2 address=54.155.0.0/16
add list=AWS-EC2 address=54.156.0.0/14
add list=AWS-EC2 address=54.160.0.0/13
add list=AWS-EC2 address=54.168.0.0/16
add list=AWS-EC2 address=54.169.0.0/16
add list=AWS-EC2 address=54.170.0.0/15
add list=AWS-EC2 address=54.172.0.0/15
add list=AWS-EC2 address=54.174.0.0/15
add list=AWS-EC2 address=54.176.0.0/15
add list=AWS-EC2 address=54.178.0.0/16
add list=AWS-EC2 address=54.179.0.0/16
add list=AWS-EC2 address=54.180.0.0/15
add list=AWS-EC2 address=54.183.0.0/16
add list=AWS-EC2 address=54.184.0.0/13
add list=AWS-EC2 address=54.193.0.0/16
add list=AWS-EC2 address=54.194.0.0/15
add list=AWS-EC2 address=54.196.0.0/15
add list=AWS-EC2 address=54.198.0.0/16
add list=AWS-EC2 address=54.199.0.0/16
add list=AWS-EC2 address=54.200.0.0/15
add list=AWS-EC2 address=54.202.0.0/15
add list=AWS-EC2 address=54.204.0.0/15
add list=AWS-EC2 address=54.206.0.0/16
add list=AWS-EC2 address=54.207.0.0/16
add list=AWS-EC2 address=54.208.0.0/15
add list=AWS-EC2 address=54.210.0.0/15
add list=AWS-EC2 address=54.212.0.0/15
add list=AWS-EC2 address=54.214.0.0/16
add list=AWS-EC2 address=54.215.0.0/16
add list=AWS-EC2 address=54.216.0.0/15
add list=AWS-EC2 address=54.218.0.0/16
add list=AWS-EC2 address=54.219.0.0/16
add list=AWS-EC2 address=54.220.0.0/16
add list=AWS-EC2 address=54.221.0.0/16
add list=AWS-EC2 address=54.222.32.0/22
add list=AWS-EC2 address=54.222.36.0/22
add list=AWS-EC2 address=54.222.128.0/17
add list=AWS-EC2 address=54.223.0.0/16
add list=AWS-EC2 address=54.224.0.0/15
add list=AWS-EC2 address=54.226.0.0/15
add list=AWS-EC2 address=54.228.0.0/16
add list=AWS-EC2 address=54.229.0.0/16
add list=AWS-EC2 address=54.232.0.0/16
add list=AWS-EC2 address=54.233.0.0/18
add list=AWS-EC2 address=54.233.64.0/18
add list=AWS-EC2 address=54.233.128.0/17
add list=AWS-EC2 address=54.234.0.0/15
add list=AWS-EC2 address=54.236.0.0/15
add list=AWS-EC2 address=54.238.0.0/16
add list=AWS-EC2 address=54.241.0.0/16
add list=AWS-EC2 address=54.242.0.0/15
add list=AWS-EC2 address=54.244.0.0/16
add list=AWS-EC2 address=54.245.0.0/16
add list=AWS-EC2 address=54.246.0.0/16
add list=AWS-EC2 address=54.247.0.0/16
add list=AWS-EC2 address=54.248.0.0/15
add list=AWS-EC2 address=54.250.0.0/16
add list=AWS-EC2 address=54.251.0.0/16
add list=AWS-EC2 address=54.252.0.0/16
add list=AWS-EC2 address=54.253.0.0/16
add list=AWS-EC2 address=54.254.0.0/16
add list=AWS-EC2 address=54.255.0.0/16
add list=AWS-EC2 address=67.202.0.0/18
add list=AWS-EC2 address=72.44.32.0/19
add list=AWS-EC2 address=75.101.128.0/17
add list=AWS-EC2 address=79.125.0.0/17
add list=AWS-EC2 address=96.127.0.0/17
add list=AWS-EC2 address=103.4.8.0/21
add list=AWS-EC2 address=107.20.0.0/14
add list=AWS-EC2 address=122.248.192.0/18
add list=AWS-EC2 address=174.129.0.0/16
add list=AWS-EC2 address=175.41.128.0/18
add list=AWS-EC2 address=175.41.192.0/18
add list=AWS-EC2 address=176.32.64.0/19
add list=AWS-EC2 address=176.34.0.0/19
add list=AWS-EC2 address=176.34.32.0/19
add list=AWS-EC2 address=176.34.64.0/18
add list=AWS-EC2 address=176.34.128.0/17
add list=AWS-EC2 address=177.71.128.0/17
add list=AWS-EC2 address=184.72.0.0/18
add list=AWS-EC2 address=184.72.64.0/18
add list=AWS-EC2 address=184.72.128.0/17
add list=AWS-EC2 address=184.73.0.0/16
add list=AWS-EC2 address=184.169.128.0/17
add list=AWS-EC2 address=185.48.120.0/22
add list=AWS-EC2 address=204.236.128.0/18
add list=AWS-EC2 address=204.236.192.0/18
add list=AWS-EC2 address=216.182.224.0/21
add list=AWS-EC2 address=216.182.232.0/22
add list=AWS-EC2 address=216.182.236.0/23
add list=AWS-EC2 address=216.182.238.0/23
add list=AWS-EC2 address=52.95.110.0/24
add list=AWS-EC2 address=205.251.192.0/21
add list=AWS-EC2 address=13.32.0.0/15
add list=AWS-EC2 address=13.35.0.0/16
add list=AWS-EC2 address=13.54.63.128/26
add list=AWS-EC2 address=13.59.250.0/26
add list=AWS-EC2 address=13.113.203.0/24
add list=AWS-EC2 address=13.124.199.0/24
add list=AWS-EC2 address=13.228.69.0/24
add list=AWS-EC2 address=18.216.170.128/25
add list=AWS-EC2 address=34.195.252.0/24
add list=AWS-EC2 address=34.216.51.0/25
add list=AWS-EC2 address=34.226.14.0/24
add list=AWS-EC2 address=34.232.163.208/29
add list=AWS-EC2 address=35.158.136.0/24
add list=AWS-EC2 address=35.162.63.192/26
add list=AWS-EC2 address=35.167.191.128/26
add list=AWS-EC2 address=52.15.127.128/26
add list=AWS-EC2 address=52.46.0.0/18
add list=AWS-EC2 address=52.47.139.0/24
add list=AWS-EC2 address=52.52.191.128/26
add list=AWS-EC2 address=52.56.127.0/25
add list=AWS-EC2 address=52.57.254.0/24
add list=AWS-EC2 address=52.66.194.128/26
add list=AWS-EC2 address=52.78.247.128/26
add list=AWS-EC2 address=52.84.0.0/15
add list=AWS-EC2 address=52.199.127.192/26
add list=AWS-EC2 address=52.212.248.0/26
add list=AWS-EC2 address=52.220.191.0/26
add list=AWS-EC2 address=52.222.128.0/17
add list=AWS-EC2 address=54.182.0.0/16
add list=AWS-EC2 address=54.192.0.0/16
add list=AWS-EC2 address=54.230.0.0/16
add list=AWS-EC2 address=54.233.255.128/26
add list=AWS-EC2 address=54.239.128.0/18
add list=AWS-EC2 address=54.239.192.0/19
add list=AWS-EC2 address=54.240.128.0/18
add list=AWS-EC2 address=70.132.0.0/18
add list=AWS-EC2 address=71.152.0.0/17
add list=AWS-EC2 address=143.204.0.0/16
add list=AWS-EC2 address=204.246.164.0/22
add list=AWS-EC2 address=204.246.168.0/22
add list=AWS-EC2 address=204.246.174.0/23
add list=AWS-EC2 address=204.246.176.0/20
add list=AWS-EC2 address=205.251.192.0/19
add list=AWS-EC2 address=205.251.249.0/24
add list=AWS-EC2 address=205.251.250.0/23
add list=AWS-EC2 address=205.251.252.0/23
add list=AWS-EC2 address=205.251.254.0/24
add list=AWS-EC2 address=216.137.32.0/19
add list=AWS-EC2 address=13.55.255.216/29
add list=AWS-EC2 address=13.56.32.200/29
add list=AWS-EC2 address=13.112.191.184/29
add list=AWS-EC2 address=13.124.145.16/29
add list=AWS-EC2 address=13.127.70.136/29
add list=AWS-EC2 address=18.231.194.8/29
add list=AWS-EC2 address=34.228.4.208/28
add list=AWS-EC2 address=34.250.63.248/29
add list=AWS-EC2 address=35.157.127.248/29
add list=AWS-EC2 address=35.176.92.32/29
add list=AWS-EC2 address=35.182.14.48/29
add list=AWS-EC2 address=52.15.247.208/29
add list=AWS-EC2 address=52.43.76.88/29
add list=AWS-EC2 address=52.47.73.72/29
add list=AWS-EC2 address=52.221.221.128/29
add list=AWS-EC2 address=177.71.207.16/29

File: /Bandwidth yang dibutuhkan untuk Youtube atau Streaming Video.txt
Berapa besaran Bandwidth yang dibutuhkan untuk Youtube atau Streaming Video?

144p = ±200Kbps (0.2Mbps)
240p = ±300Kbps (0.3Mbps)
360p = ±400Kbps (0.4Mbps)
480p = ±500Kbps (0.5Mbps)
720p @30fps = ±1.500Kbps (1.5Mbps)
720p @60fps = ±2.250Kbps (2.2Mbps)
1080p @30fps = ±3.000Kbps (3Mbps)
1080p @60fps = ±4.500Kbps (4.5Mbps)
1440p @30fps = ±6.000Kbps (6Mbps)
1440p @60fps = ±9.000Kbps (9Mbps)
4k / 2160p @30fps = ±13.000Kbps (13Mbps)
4K/2160p @60fps = ±20.000Kbps (20Mbps)

Disini kita bisa dengan mudah menentukan nilai PCQ terbaik untuk kebutuhan Bandwidth Streaming yang layak diterapkan pada setingan Mikrotik agar bisa di tonton lancar tanpa Buffering.

File: /Bittorrent Torrentwws Torrentwww Regexp layer 7.txt
# Bittorrent, Torrent-wws, Torrent-www Regexp layer 7
/ip firewall layer7-protocol
add name=bittorrent regexp="^(bittorrent protocol|azver1\$|get /scrape\\\?info\
    _hash=)|d1:ad2:id20:|8'7P\\)[RP]"
add name=torrent-wws regexp="^.*(get|GET).+(torrent|info_hash|thepiratebay|iso\
    hunt|entertane|demonoid|btjunkie|mininova|flixflux|vertor|h33t|zoozle|bitn\
    ova|bitsoup|meganova|fulldls|btbot|fenopy|gpirate|commonbits).*\$"
add name=torrent-www regexp="^.+(torrent|thepiratebay|isohunt|entertane|demono\
    id|btjunkie|mininova|flixflux|vertor|h33t|zoozle|bitnova|bitsoup|meganova|\
    fulldls|btbot|fenopy|gpirate|commonbits).*\$"

File: /Blokir Situs Berdasarkan Keyword pada DNS Cache Mikrotik.txt
#################################################
#pastekan dulu ini diterminal
/system scheduler add interval="00:05:00" name="BLACK-LIST" start-time=startup
 
#pastekan script ini dalam schuler yg sudah dibuat
#################################################
# Url Blocked From DNS Static
#################################################
# Find all entry on dns cache
:foreach iDNS in=[/ip dns cache all find where (name~"porn" ||  name~"xvideos" ||  name~"ngentot" ||  name~"tube8" || name~"sex") && (type="A") ] do={
# find and filtering keyword and only find record for type A
# for keyword just add keyword || name~"KEYWORD") before && (type="A")
#################################################
:local tmpDNSsite [/ip dns cache get $iDNS name] ;
:local tmpDNSip [/ip dns cache get $iDNS address];
:local nameList "BLOCK_SITE";
# save to local cache by string
#################################################
delay delay-time=10ms
# wait for 10ms
#################################################
:if ( [/ip firewall address-list find where address=$tmpDNSip] = "") do={
# chek for no more duplicate site on cache
#################################################
:log warning ("Added site to block on dns: $tmpDNSsite : $tmpDNSip");
# show info on warning log
#################################################
/ip firewall address-list add address=$tmpDNSsite list=$nameList comment=$tmpDNSsite;
# add site to add list entry.
#################################################
}
}
# End Script
#################################################

+++++++++++++++++++++++++++++++++++++++++++++++ 
#################################################
#Pastikan hanya menggunakan DNS Mikrotik:
/ip firewall nat
add action=redirect chain=dstnat comment=DNS dst-port=53 protocol=tcp to-ports=53
add action=redirect chain=dstnat dst-port=53 protocol=udp to-ports=53
#################################################
 
#################################################
#Block dengan cara drop di Filter rules
/ip firewall filter
add chain=forward dst-address-list=BLOCK_SITE action=drop
#################################################
 
#################################################
#Atau bisa Block dengan cara redirect IP dan Port
/ip firewall nat
add action=dst-nat chain=dstnat comment="BLOCK WEBSITE" dst-address-list=
BLOCK_SITE dst-port=80,81,8181,443 protocol=tcp to-addresses=36.86.63.185 to-ports=80
#################################################S

File: /Blokir TRACEROUTE di Mikrotik.txt
# Cara Blokir TRACEROUTE di Mikrotik

/ip firewall filter
add action=drop chain=forward icmp-options=11:0 protocol=icmp
add action=drop chain=forward icmp-options=3:3 protocol=icmp

File: /Blokir User melalui MAC address.txt
# Cara Blokir User melalui MAC address

/ip fir fi
add chain=input action=drop src-mac-address=74:EA:3A:xx:xx:xx
add chain=forward action=drop src-mac-address=74:EA:3A:xx:xx:xx

File: /BYPASS INTERNET POSITIF DENGAN VPN PPTP.txt
Tinggal cari yang jual VPN biasanya harga kisaran 50rb/100rb perbulan

Routing bisa ke DNS Google atau OpenDNS
Google:
8.8.8.8
8.8.4.4
OpenDNS:
208.67.222.222
208.67.220.220

# Contoh Routing Ke DNS Google

/interface pptp-client
add add-default-route=no allow=pap,chap,mschap1,mschap2 connect-to=(IP VPN) dial-on-demand=no disabled=no max-mru=1460 max-mtu=1460 mrru=disabled name=MY-PPTPVPN password=xxxxx profile=default-encryption user=MYPPTPVPN

/ip route
add check-gateway=ping disabled=no distance=1 dst-address=8.8.8.8 gateway=MY-PPTPVPN scope=30 target-scope=10
add check-gateway=ping disabled=no distance=1 dst-address=8.8.4.4 gateway=MY-PPTPVPN scope=30 target-scope=10
add check-gateway=ping disabled=no distance=1 dst-address=208.67.222.222 gateway=MY-PPTPVPN scope=30 target-scope=10
add check-gateway=ping disabled=no distance=1 dst-address=208.67.220.220 gateway=MY-PPTPVPN scope=30 target-scope=10

/ip firewall nat
add action=redirect chain=dstnat dst-port=53 protocol=udp

/ip dns
set allow-remote-requests=yes cache-max-ttl=1w cache-size=2048KiB max-udp-packet-size=4096 servers=8.8.8.8,8.8.4.4,208.67.222.222,208.67.220.220
 
#Jangan Lupa Clear DNS
/ip dns cache flush

Semoga Membantu :)

File: /Cara blokir akses ke Modem.txt
# cara blokir akses ke modem

/ip firewall address-list
add address=192.168.1.1 list=IP-MODEM
add address=192.168.2.1 list=IP-MODEM

/ip firewall filter
add action=drop chain=forward comment="PROTEKSI MODEM" dst-address-list=IP-MODEM

File: /Cara Blokir Aplikasi Tiktok.txt
# Cara Blokir Aplikasi Tiktok

/ip firewall filter
add action=drop chain=forward protocol=tcp tls-host=*.musical.ly
add action=drop chain=forward content=tiktokv.com 
add action=drop chain=forward content=musical.ly
add action=drop chain=forward content=tiktok

File: /Cara bypass semua IP local agar tidak terlimit.txt
# Cara bypass semua IP local agar tidak terlimit

# paste script addlist local ke terminal
/ip firewall address-list
add address=0.0.0.0/8 list=LOCAL-IP
add address=10.0.0.0/8 list=LOCAL-IP
add address=100.64.0.0/10 list=LOCAL-IP
add address=127.0.0.0/8 list=LOCAL-IP
add address=169.254.0.0/16 list=LOCAL-IP
add address=172.16.0.0/12 list=LOCAL-IP
add address=192.0.0.0/24 list=LOCAL-IP
add address=192.0.2.0/24 list=LOCAL-IP
add address=192.168.0.0/16 list=LOCAL-IP
add address=198.18.0.0/15 list=LOCAL-IP
add address=198.51.100.0/24 list=LOCAL-IP
add address=203.0.113.0/24 list=LOCAL-IP
add address=224.0.0.0/4 list=LOCAL-IP
add address=240.0.0.0/4 list=LOCAL-IP

# Pastikan script ini berada pada mangle paling atas
/ip fi ma
add action=accept chain=prerouting dst-address-list=LOCAL-IP  src-address-list=LOCAL-IP
add action=accept chain=postrouting dst-address-list=LOCAL-IP  src-address-list=LOCAL-IP
add action=accept chain=forward dst-address-list=LOCAL-IP  src-address-list=LOCAL-IP
add action=accept chain=input dst-address-list=LOCAL-IP  src-address-list=LOCAL-IP
add action=accept chain=output dst-address-list=LOCAL-IP  src-address-list=LOCAL-IP

File: /Cara bypass user hotspot melalui macaddress.txt
#cara bypass user hotspot melalui mac-address
/ip hotspot ip-binding add mac-address=xx:xx:xx:xx:xx:xx type=bypassed

# masukan xx:xx:xx:xx:xx:xx sesuai dengan mac-address yang ingin di bypass

File: /Cara clear log di Mikrotik.txt
#cara clear log di Mikrotik

#pertama paste script dibawah ini di terminal
/system logging action set memory memory-lines=1

#kemudian paste kembali script dibawah ini
/system logging action set memory memory-lines=100

File: /Cara mengaktifkan IP CLOUD untuk remote diluar jaringan.txt
# Cara mengaktifkan IP CLOUD, ini cara lain masuk kedalam router selain menggunakan ip public atau vpn port forwarding, jangan lupa mengaktifkan DMZ pada modem agar router bisa diakses dari luar.

/ip cloud set ddns-enabled=yes
/ip cloud print

jangan lupa catat dns-name: 
2f2c012xxxxxx.sn.mynetname.net

File: /Cara mengganti identitas di mikrotik  Caption Winbox.txt
# cara mengganti identitas di mikrotik / Caption Winbox

/system identity
set name="BuanaNET By BNT"

File: /Cara Mengganti System Note di Terminal Mikrotik.txt
#cara mengganti system note di terminal
#sesuaikan dengan tulisan anda sendiri

/system note
set note=" ______  _     _        ______         ______  _______ _______ \
    \n(____  \\| |   | |  /\\  |  ___ \\   /\\  |  ___ \\(_______|_______)\
    \n ____)  ) |   | | /  \\ | |   | | /  \\ | |   | |_____   _       \
    \n|  __  (| |   | |/ /\\ \\| |   | |/ /\\ \\| |   | |  ___) | |      \
    \n| |__)  ) |___| | |__| | |   | | |__| | |   | | |_____| |_____ \
    \n|______/ \\______|______|_|   |_|______|_|   |_|_______)\\______)\
    \nProtected by BuanaNET SECURE!\
    \n"

File: /Cara Menonaktifkan Google SSL untuk keperluan Proxy.txt
Disini saya share cara menonaktifkan pencarian aman google yaitu dengan cara menonaktifkan Google SSL secara langsung dari Mikrotik. Cara ini berguna untuk mengubah HTTPS ke HTTP dengan harapan agar content bisa ter Cache untuk keperluan Proxy Internal atau Proxy  External (umumnya Squid/Lusca).

Caranya sangat mudah yaitu dengan memaksa DNS Static langsung dari mikrotik.

/ip dns static 
add address=216.239.32.20 name=www.google.com 
add address=216.239.32.20 name=www.google.co.id

Google memiliki IP dinamic yang sangat banyak dengan top level domain hampir disetiap negara, karena kita di indonesia jadi paling akan diredirect ke google.co.id dan google.com

Selengkapnya lihat Gambar dikomentar :)

File: /Cara rebuild database di User Manager.txt
#Cara rebuild database di User Manager
/tool user-manager database rebuild

File: /Cara reset script dari scheduler atau dari script.txt
#cara reset melalui script dari scheduler atau dari scriptar atau terminal
/system reset-configuration

File: /Cara Setting NTP Network Time Protocol di Mikrotik.txt
#NTP adalah Network Time Protocol, suatu protocol yang digunakan untuk melakukan sinkronisasi waktu dalam jaringan.

/system ntp client
set enabled=yes primary-ntp=111.92.175.248 secondary-ntp=130.54.208.201 server-dns-names=asia.pool.ntp.org

File: /Daftar Port Game Online Game Mobile Game Web Game FB.txt
PORT FORWARDING GAME ONLINE
==============================================

Port forward Game: Origin APEX Legends
TCP: 9960-9969,1024-1124,3216,18000,18120,18060,27900,28910,29900 
UDP: 1024-1124,18000,29900,37000-40000

Port forward Game: PUBG PLAYERUNKNOWN’S BATTLEGROUNDS
UDP : 7080-8000

Port forward Game: ROE Ring of Elysium
TCP : 9002,10000-10015

Port forward Game: RULES OF SURVIVAL
UDP : 24000-24100

Port forward Game: FORTNITE EPICGAMES
Udp : 9000-9100

Counter-Strike: Global Offensive - Steam
TCP: 27015-27030,27036-27037
UDP: 4380,27000-27031,27036

Counter-Strike: Global Offensive - Xbox 360
TCP: 3074
UDP: 88,3074

Counter-Strike: Global Offensive - Playstation 3
TCP: 3478-3480,5223,8080
UDP: 3074,3478-3479,3658

Port forward Game: Atlantica Port Game:
TCP : 4300

Port forward Game: Aura Kingdom Port Game:
TCP :5540-5580

Port forward Game: Ayodance Port Game:
TCP : 18900-18910

Port forward Game: World in Ayodance Port Game:
TCP : 52510,53100-53110,54100,55100

Port forward Game: Blackretribution Steam Port Game:
UDP : 7020-7050,8200-8220,9000-9020

Port forward Game: Bounty Hound Port Game:
TCP : 9810-9860

Port forward Game: Clash of God Port Game:
TCP : 9430-9450,5220-5230

Port forward Game: Cabal Indonesia Port Game:
TCP : 63000-64000,38101,38110-38130

Port forward Game: Cabal Extreme Private Port Game:
TCP : 60170-60180,63000-64000,38101,38110-38600

Port forward Game: Cross Fire indonesia Port Game:
TCP : 10009,13008,16666,28012
UDP : 12020-12080,13000-13080

Port forward Game: Dragon Nest Indo Port Game:
TCP : 14300-15512
UDP : 15000-15500

Port forward Game: Dragona Port Game:
TCP : 10000-10030

----------------------------------------------------------------------------------------
Port forward Game: Dota 2 Steam Port Game:
TCP : 9100-9200,8230-8250,8110-8120
UDP : 28010-28200,27010-27200,39000

Tambahan:
Steam Client
UDP 27000 to 27015 inclusive (Game client traffic)
UDP 27015 to 27030 inclusive (Typically Matchmaking and HLTV)
TCP 27014 to 27050 inclusive (Steam downloads)
UDP 4380
Dedicated or Listen Servers
TCP 27015 (SRCDS Rcon port)
Steamworks P2P Networking and Steam Voice Chat
UDP 3478 (Outbound)
UDP 4379 (Outbound)
UDP 4380 (Outbound)
------------------------------------------------------------------

Port forward Game: Grand Chase Port Game:
TCP : 9300,9400,9700
UDP : 9401,9600,16440-16450

Port forward Game: Garena League of Legend (LOL) Port Game:
TCP : 2080-2099
UDP : 5100

Port forward Game: Fifa Online 3 Garena (FOL3) Port Game:
TCP: 7770-7790
UDP: 16300-16350 

Port forward Game: Hon Port Game:
UDP : 9100-9200,11200-11500

Port forward Game: Heroes of Atarsia Port Game:
TCP : 7777,9400

Port forward Game: Idol Street Port Game:
TCP : 2001-2010

Port forward Game: Left4Dead 2 Steam Port Game:
UDP : 4360-4390

Port forward Game: Lineage 2 Port Game:
TCP : 7777,10000,11000,13000

Port forward Game: Lost Saga Port Game:
TCP : 14000-14010 
UDP : 14000-14010

Port forward Game: Lune of eden Port Game:
TCP : 8400

Port forward Game: Mircovolt Port Game:
TCP : 13000

Port forward Game: Mercenary ops Port Game:
TCP : 6000-6125

Port forward Game: Modo marble Port Game:
TCP : 28900-28914

Port forward Game: Paradins Hi-Rez (steam) games ports:
TCP : 9000-9999
UDP : 9002-9999

Port forward Game: Point blank Indonesia Port Game:
TCP : 39190-39200
UDP : 40000-40010

Port forward Game: Ragnarok 2 Port Game:
TCP : 7201-7210,7401-7410

Port forward Game: Seal Online :
TCP : 1818

Port forward Game: RF Online Port Game:
TCP : 27780

Port forward Game: Special Force Port Game:
TCP : 27920-27940
UDP : 30000-30030

Port forward Game: WARFRAME (steam) games ports: 
UDP : 4950-4955 
TCP : 6695-6699

Port forward Game: World of Tanks games ports:
UDP Range 12000-29999, 32801-32825, and UDP 5060, 5062, 3478, 3479, 20014
TCP Range 20000-25000, and TCP 53, 80, 443, 3128, 8081, 8088, 32801, 32803.

Port forward Game: X-shot Indonesia Port Game:
TCP : 7320-7350
UDP : 7800-7850, 30000


PORT GAME MOBILE / GAME HP / GAME SMARTPHONE
==============================================

Port forward Game: FREE FIRE (GARENA) MOBILE 
TCP:39003,39698,39779
UDP:10001,10003,10012

Port forward Game: PUBG MOBILE / PUBGM 
TCP:10012,17500 
UDP: 10010,10013,10039,10096,10491,10612,11455,12235,13748,13894,13972,20000-20002

Port forward Game: MOBILE LEGENDS: BANG BANG (ML) 
TCP:5001,5003,9001,30000-30200

Port forward Game: LINE LETS GET RICH MOBILE 
TCP:10500-10515

Port forward Game: RULES OF SURVIVAL MOBILE 
UDP: 24000-24050

Port forward Game: COC (CLASH OF CLANS) MOBILE 
TCP: 9330-9340

Port forward Game: DRAGON NEST MOBILE 
TCP:10514

Port forward Game: DOMINO QQ MOBILE 
TCP:9122, 11000-11150

Port forward Game: SEVEN KNIGHTS (NETMARBLE) MOBILE 
TCP: 12000-12010 

Port forward Game: CLASH ROYALE (CRY) MOBILE 
TCP: 9330-9340 
UDP: 9330-9340

Port forward Game: LAST EMPIRE WAR Z MOBILE 
TCP:9930-9940 

Port forward Game: MOSTLY MOBILE 
TCP:9933

Port forward Game: DREAM LEAGUE SOCCER MOBILE 
UDP: 60970-60980

Port forward Game: SHINOBI HEROES MOBILE 
TCP:10005-10020

Port forward Game: NARUTO LITTLE NINJA (CHINA) MOBILE 
TCP:6170-6180

Port forward Game: RPG TORAM ONLINE MOBILE 
UDP:30100-30110

Port forward Game: POINT BLANK MOBILE / PB MOBILE 
TCP:44590-44610 

Port forward Game: ARENA OF VALOR (AOV) - GARENA MOBILE 
TCP:10001-10094 
UDP:10080,17000

Port forward Game: Booya Capsa Susun 
TCP 7090-7100

Port forward Game: Booya Domino QiuQiu 
TCP 7020-7030



PORT GAME WEB / PORT GAME FACEBOOK
==============================================

Port forward Game: Roblox
UDP 49152 - 65535

Port forward Game: League of Angels 2 
TCP 51700 - 51715

Port forward Game: Sword of Angels
TCP 15490-15510

Port forward Game: Wild Ones 
TCP : 8000

Port forward Game: Warflare
TCP 64990-65010

Port forward Game: 8 Ball Pool (Miniclips) 
TCP 4000

Port forward Game: Megarealm: Rise Of Chaos
TCP 26590 - 26600

Port forward Game: eadshot 
TCP 1800-1810
UDP1845-1860

Port forward Game: Empire & Allies
TCP 8890


Port forward Game: Texas HoldEm Poker 
TCP 9339

Port forward Game: CastleVille 
TCP 8890

Perjuangan Semut
TCP 7200-7210,7450-7460

Untuk IP masih menyusul.

File: /FailOver 2 ISP dengan Recursive Gateway.txt
# Contoh Fail Over 2 ISP dengan Recursive Gateway
WAN-1 = IP: 192.168.2.2/24
WAN-2 = IP: 192.168.3.2/24

/ip route
add check-gateway=ping distance=2 gateway=8.8.8.8 target-scope=30
add check-gateway=ping distance=1 gateway=8.8.4.4 target-scope=30
add check-gateway=ping distance=1 dst-address=8.8.8.8/32 gateway=192.168.3.1 target-scope=10
add check-gateway=ping distance=1 dst-address=8.8.4.4/32 gateway=192.168.2.1 target-scope=10

File: /Melimit Bandwidth Multi Login di Simple Queue.txt
Membatasi Profile Hotspot menggunakan Multi Login (1 profile diperkosa rame2) terkadang memusingkan, karena Bandwidth yang di share biasanya tidak menggunakan Total Limit Bandwidth tapi justru malah diberikan bandwidth dengan kecepatan yang sama kepada setiap IP. Sebenarnya ini gak masalah kalau kita menggunakan Mangle dan Queue Tree tapi akan beda cerita jika menggunakan simple Queue. 

Sebenarnya cara ini cukup menarik bagi pemain hotspot yang ingin memberikan tambahan akses gratis buat user di cafe atau warnet miliknya dan tentu saja tidak mengganggu user hotspot yang berbayar, karena sudah di limit apa adanya :)

Buat IP Address baru = 10.5.10.1/24 (bebas aja)
IP Pool = 10.5.10.2-10.5.10.254
Interface hotspot [wlan-hotspot] = ganti dengan nama interface hotspot masing2 jika sudah ada yang lama tidak masalah karena memang itu tujuan kita sebenarnya, khan untuk satu interface bisa di set untuk multi IP :)

/ip address
add address=10.5.10.1/24 comment="Login Multi User" interface=[wlan-hotspot] network=10.5.10.0

/ip pool
add name=hs_multi_user ranges=10.5.10.2-10.5.10.254

/ip firewall nat
add action=masquerade chain=srcnat comment="masquerade hotspot network multi login" src-address=10.5.10.0/24

/ip hotspot user profile
add address-pool=hs_multi_user name=multi-user shared-users=10

/ip hotspot user
add name=muser password=12345 profile=multi-user

/queue simple
add max-limit=256k/512k name="Multi User" target=10.5.10.0/24 total-queue=download

Jangan lupa untuk drag posisinya paling atas diatas queue hs

File: /Memaksa agar semua client menggunakan DNS mikrotik.txt
#Memaksa agar semua client menggunakan DNS mikrotik

/ip dns
set allow-remote-requests=yes cache-max-ttl=3h cache-size=10240KiB servers=8.8.8.8,8.8.4.4,208.67.222.222,208.67.220.220,1.1.1.1,9.9.9.9

/ip firewall nat
add action=redirect chain=dstnat dst-port=53 protocol=udp to-ports=53
add action=redirect chain=dstnat dst-port=53 protocol=tcp to-ports=53

File: /Memastikan hanya 1 ID hotspot yang boleh login.txt
Memastikan hanya 1 ID hotspot yang boleh login bersamaan, jika ada 2 ID yang login otomatis akan mematikan ID yang pertama (catatan: bukan untuk multi shared user). Script ini juga bagus jika kita ingin pindah login ke perangkat lainnya tanpa harus logout dan menunggu session timeout pada perangkat sebelumnya. 
Sebelum dipasang paling tidak dipahami dulu konsep kerja script ya jangan asal comot dan copas tar malah error hotspotnya :)
Silahkan pasang langsung pada IP -> hotspot -> User Profile -> pilih nama profile -> Script -> On Login

# Modifikasi Oleh Agus Ramadhani (BuanaNET)
# Local Variables Section
:local uname $user;
:local usercount 0;
:local usertime "00:00:00";
# Variabel untuk pengguna yang sebelumnya login
:local kickable;
# Variabel untuk sesi max user yang diperbolehkan, jika 2 berarti hanya satu sesi diperbolehkan pada suatu waktu
:local maxuser 2;
# Memuat semua user aktif di hotspot
:foreach i in=[/ip hotspot active find user=$uname] do= {
# Beban UPTIME untuk semua user dan untuk dicocokkan kemudian
:local curup [/ip hotspot active get $i uptime];
# Jika pengguna sama sebelumnya cocok menggunakan UPTIME [above then 0] kemudian menetapkan variabel global untuk pemutusan
:if ( $curup > $usertime ) do={
:set usertime $curup;
:set kickable $i;
}
:set usercount ($usercount+1);
}
# IF Function Fungsi bagi pengguna yang sudah login,
:if ($usercount = $maxuser) do={
:log info "Login user: $uname ($usercount/$maxuser) - Oldest $usertime will be logout!";
# Menendang pengguna login sebelumnya (jika ID yang sama)
/ip hotspot active remove numbers=$kickable;
# Jika tidak, melakukan apa-apa ,hanya login , Anda dapat memodifikasi fungsi ini juga
} else {
:log info "Login user: $uname ($usercount/$maxuser)";

File: /Memblokir Serangan Winbox Exploit di Mikrotik.txt
Untuk membentengi Exploit mencuri password Mikrotik seperti PoC*py, WinboxExploit*py dan sejenisnya gak perlu firewall yang canggih dan bejibun, cukup tiga baris ini aja sudah bisa menghandle semuanya dari serangan Exploit, karena tujuan Winbox Exploit cuman satu yaitu mengambil "user.dat" aja :D

silahkan ganti WAN dengan Intefface ke arah modem atau internet.

/ip firewall filter
add chain=input in-interface=WAN protocol=tcp dst-port=8291 action=drop
add action=reject chain=input comment="PROTEKSI ROUTER" in-interface=WAN content=user.dat reject-with=icmp-network-unreachable
add action=drop chain=input in-interface=WAN content="user.dat"

File: /menampilkan password  Lupa Password User Manager.txt
#Cara menampilkan password atau Lupa Password User Manager
/tool user-manager customer print;

File: /Mendapatkan Nama Hari  Get Day Mikrotik.txt
# Calculates day of the week for a givien date
# Month: jan,feb ... nov,dec   (must be lower-case)
# Day: 1 - 31
# Year: 1583 - ...
# mmm/dd/yyyy   same format as [/system clock get date]
# (ex. feb/19/2012)
# by melboyscout (melboyscout [at] gmail.com)

:local date [/system clock get date]

# Math Calculation here
:local result ""
:local months [:toarray "jan,feb,mar,apr,may,jun,jul,aug,sep,oct,nov,dec"]
:local daytbl [:toarray "sun,mon,tue,wed,thu,fri,sat"]

:local month [:pick $date 0 3]
:local day [:pick $date 4 6]
:local dayc [:pick $date 5 6]
:local year [:pick $date 7 11]

# if the first char is a 0 (zero) only read last char, else script fails
:if ([:pick $date 4 5] = 0) do={ :set day ($dayc)}

:local sum 0
:local aaa 0
:local yyy 0
:local mmm 0
:local nmonth 1

:for mindex from=0 to=[:len $months] do={
  :if ([:pick $months $mindex] = $month) do={:set nmonth ($mindex + 1) }
}

:set aaa ((14 - $nmonth) / 12)
:set yyy ($year - $aaa)
:set mmm ($nmonth + 12 * $aaa - 2)
:set sum (7000 + $day + $yyy + ($yyy / 4) - ($yyy / 100) + ($yyy / 400) + ((31 * $mmm) / 12))
:set sum ($sum - (($sum / 7) * 7))
:set result [:pick $daytbl $sum]
:log info "Today is $result"

File: /Mengatasi Kesalahan Passthrough Pada Mangle Mikrotik.txt
foreach mrk in=("packet","connection", "routing") do={
foreach i in=([/ip firewall mangle find where action=("mark-" . $mrk)]) do={
:if ($mrk = "packet") do={ 
local cmd ("ip firewall mangle set " . $i . " passthrough=no")
:execute $cmd
}
:if ($mrk = "connection") do={ 
local cmd ("ip firewall mangle set " . $i . " passthrough=yes")
:execute $cmd
}
:if ($mrk = "routing") do={ 
local cmd ("ip firewall mangle set " . $i . " passthrough=yes")
:execute $cmd
}
}
}

File: /Menghapus semua log di User Manager.txt
#Cara untuk menghapus semua log di User Manager
/tool user-manager database clear-log

File: /Mengirim IP Public Jika Ada Perubahan IP ke Email.txt
##### SCRIPT GET IP PUBLIC ######
# Mengirim IP Public Jika Ada Perubahan IP ke Email. Tidak bekerja pada mikrotik dibelakang NAT. hanya berjalan di PPPOE Bridge Mikrotik
# 1.nama-interface = Ganti dengan interface PPPoE Speedy
# 2.to-mail@gmail.com = email tujuan
# 3.from-mail@gmail.com = email Pengirim
# 4.Contoh saya menggunakan Server Gmail
#############################
:global CekKoneksi
/interface pppoe-client monitor nama-interface once do={
:set CekKoneksi $status
}
:if ($CekKoneksi = "connected") do={
:log info "->> Status Koneksi: $CekKoneksi ";
:global LogIP;
:local IPBaru [/ip address get [find interface="nama-interface"] address];
:if ($IPBaru = $LogIP) do={
:log info "->> IP Speedy Anda Tidak Berubah";
};
:if ($IPBaru != $LogIP) do={
:log info "->> IP Speedy Anda Berubah $IPBaru";
:set LogIP $IPBaru;
:delay 5s;
/tool e-mail send to="to-mail@gmail.com" from=from-mail@gmail.com server=74.125.129.108 start-tls=yes subject="IP Speedy Anda Berubah" body="IP interface Speedy Anda Yang Baru :[ $LogIP ]";
};
}
:if ($s != "connected") do={
:log info message="->> Status Koneksi: Terminating..";
}

/system scheduler
add disabled=no interval=10m name=IP-PUBLIC on-event=GET-IP-PUBLIC policy=ftp,read,write,policy,test,winbox,password,sniff,sensitive,api

File: /Merubah Default Admin Password User Manager.txt
#secara default password admin di user manager adalah "dikosongan"

#pertama cek dulu
/tool user-manager customer print

#tulis nomor id admin biasanya defaultnya 0

#untuk merubah password bisa gunakan script dibawah ini
/tool user-manager customer set password=12345 numbers=0

File: /Merubah Nama Interface ether Mikrotik Default.txt
#####################################
# Script by Agus Ramadhani
# fb.com/buananet.pangkalanbun
# http://www.o-om.com
# SCRIPT name interface to default
######################################
:foreach i in=[/interface ethernet find ] do={ 
:local y [/interface ethernet get $i name] ;
:local x [/interface ethernet get $i default-name];
:log warning "Change interface Name $y => $x"
/interface set $y name=$x;
}

File: /Merubah path Database User Manager ke USB.txt
# cara merubah path Database User Manager ke USB
/tool user-manager database set db-path=disk1/user-manager3

File: /Mikrotik IP Address List FACEBOOK.txt
/ip firewall address-list
add address=31.13.24.0/21  list=facebook
add address=31.13.64.0/18  list=facebook
add address=31.13.64.0/19  list=facebook
add address=31.13.64.0/24  list=facebook
add address=31.13.65.0/24  list=facebook
add address=31.13.66.0/24  list=facebook
add address=31.13.67.0/24  list=facebook
add address=31.13.68.0/24  list=facebook
add address=31.13.69.0/24  list=facebook
add address=31.13.70.0/24  list=facebook
add address=31.13.71.0/24  list=facebook
add address=31.13.72.0/24  list=facebook
add address=31.13.73.0/24  list=facebook
add address=31.13.74.0/24  list=facebook
add address=31.13.75.0/24  list=facebook
add address=31.13.76.0/24  list=facebook
add address=31.13.78.0/24  list=facebook
add address=31.13.80.0/24  list=facebook
add address=31.13.81.0/24  list=facebook
add address=31.13.82.0/24  list=facebook
add address=31.13.83.0/24  list=facebook
add address=31.13.84.0/24  list=facebook
add address=31.13.85.0/24  list=facebook
add address=31.13.86.0/24  list=facebook
add address=31.13.87.0/24  list=facebook
add address=31.13.90.0/24  list=facebook
add address=31.13.91.0/24  list=facebook
add address=31.13.92.0/24  list=facebook
add address=31.13.94.0/24  list=facebook
add address=31.13.95.0/24  list=facebook
add address=31.13.96.0/19  list=facebook
add address=45.64.40.0/22 list=facebook
add address=66.220.144.0/20  list=facebook
add address=66.220.144.0/21  list=facebook
add address=66.220.152.0/21  list=facebook
add address=69.63.176.0/20  list=facebook
add address=69.63.176.0/21  list=facebook
add address=69.63.184.0/21  list=facebook
add address=69.171.224.0/19  list=facebook
add address=69.171.224.0/20  list=facebook
add address=69.171.239.0/24  list=facebook
add address=69.171.240.0/20  list=facebook
add address=69.171.255.0/24  list=facebook
add address=74.119.76.0/22  list=facebook
add address=157.240.0.0/17  list=facebook
add address=157.240.1.0/24  list=facebook
add address=157.240.2.0/24  list=facebook
add address=157.240.3.0/24  list=facebook
add address=157.240.6.0/24  list=facebook
add address=157.240.7.0/24  list=facebook
add address=157.240.8.0/24  list=facebook
add address=157.240.9.0/24  list=facebook
add address=157.240.10.0/24  list=facebook
add address=157.240.11.0/24  list=facebook
add address=157.240.12.0/24  list=facebook
add address=157.240.13.0/24  list=facebook
add address=157.240.14.0/24  list=facebook
add address=157.240.15.0/24  list=facebook
add address=157.240.16.0/24  list=facebook
add address=157.240.18.0/24  list=facebook
add address=157.240.20.0/24  list=facebook
add address=157.240.21.0/24  list=facebook
add address=157.240.22.0/24  list=facebook
add address=173.252.64.0/19  list=facebook
add address=173.252.88.0/21  list=facebook
add address=173.252.96.0/19  list=facebook
add address=185.60.216.0/22  list=facebook
add address=185.60.216.0/24  list=facebook
add address=185.60.218.0/24  list=facebook
add address=185.60.219.0/24  list=facebook
add address=204.15.20.0/22  list=facebook


File: /Mikrotik IP Address List TWITTER.txt
/ip firewall address-list
add address=69.195.160.0/24  list=twitter
add address=69.195.162.0/24  list=twitter
add address=69.195.163.0/24  list=twitter
add address=69.195.164.0/24  list=twitter
add address=69.195.165.0/24  list=twitter
add address=69.195.166.0/24  list=twitter
add address=69.195.168.0/24  list=twitter
add address=69.195.169.0/24  list=twitter
add address=69.195.171.0/24  list=twitter
add address=69.195.172.0/24  list=twitter
add address=69.195.173.0/24  list=twitter
add address=69.195.175.0/24  list=twitter
add address=69.195.176.0/24  list=twitter
add address=69.195.177.0/24  list=twitter
add address=69.195.178.0/24  list=twitter
add address=69.195.179.0/24  list=twitter
add address=69.195.180.0/24  list=twitter
add address=69.195.181.0/24  list=twitter
add address=69.195.182.0/24  list=twitter
add address=69.195.184.0/24  list=twitter
add address=69.195.185.0/24  list=twitter
add address=69.195.186.0/24  list=twitter
add address=69.195.187.0/24  list=twitter
add address=69.195.188.0/24  list=twitter
add address=69.195.189.0/24  list=twitter
add address=69.195.190.0/24  list=twitter
add address=69.195.191.0/24  list=twitter
add address=104.244.40.0/24  list=twitter
add address=104.244.41.0/24  list=twitter
add address=104.244.42.0/24  list=twitter
add address=104.244.43.0/24  list=twitter
add address=104.244.44.0/24  list=twitter
add address=104.244.45.0/24  list=twitter
add address=104.244.46.0/24  list=twitter
add address=104.244.47.0/24  list=twitter
add address=185.45.5.0/24  list=twitter
add address=185.45.6.0/23  list=twitter
add address=192.133.76.0/22  list=twitter
add address=192.133.76.0/23  list=twitter
add address=199.16.156.0/22  list=twitter
add address=199.16.156.0/23  list=twitter
add address=199.59.148.0/22  list=twitter
add address=199.96.56.0/23  list=twitter
add address=199.96.56.0/24  list=twitter
add address=199.96.57.0/24  list=twitter
add address=199.96.58.0/23  list=twitter
add address=199.96.60.0/23  list=twitter
add address=199.96.60.0/24  list=twitter
add address=199.96.61.0/24  list=twitter
add address=199.96.62.0/23  list=twitter
add address=202.160.128.0/24  list=twitter
add address=202.160.129.0/24  list=twitter
add address=202.160.130.0/24  list=twitter
add address=202.160.131.0/24  list=twitter
add address=209.237.192.0/24  list=twitter
add address=209.237.193.0/24  list=twitter
add address=209.237.194.0/24  list=twitter
add address=209.237.195.0/24  list=twitter
add address=209.237.196.0/24  list=twitter
add address=209.237.197.0/24  list=twitter
add address=209.237.198.0/24  list=twitter
add address=209.237.199.0/24  list=twitter
add address=209.237.200.0/24  list=twitter
add address=209.237.201.0/24  list=twitter
add address=209.237.204.0/24  list=twitter
add address=209.237.205.0/24  list=twitter
add address=209.237.206.0/24  list=twitter
add address=209.237.207.0/24  list=twitter
add address=209.237.208.0/24  list=twitter
add address=209.237.209.0/24  list=twitter
add address=209.237.210.0/24  list=twitter
add address=209.237.211.0/24  list=twitter
add address=209.237.212.0/24  list=twitter
add address=209.237.213.0/24  list=twitter
add address=209.237.214.0/24  list=twitter
add address=209.237.215.0/24  list=twitter
add address=209.237.216.0/24  list=twitter
add address=209.237.217.0/24  list=twitter
add address=209.237.218.0/24  list=twitter
add address=209.237.219.0/24  list=twitter
add address=209.237.220.0/24  list=twitter
add address=209.237.221.0/24  list=twitter
add address=209.237.222.0/24  list=twitter
add address=209.237.223.0/24  list=twitter


File: /Mikrotik IP Address List WHATSAPP.txt
/ip firewall address-list
add address=31.13.64.51 list=whatsapp_list
add address=31.13.65.49 list=whatsapp_list
add address=31.13.66.49 list=whatsapp_list
add address=31.13.68.52 list=whatsapp_list
add address=31.13.69.240 list=whatsapp_list
add address=31.13.70.49 list=whatsapp_list
add address=31.13.71.49 list=whatsapp_list
add address=31.13.72.52 list=whatsapp_list
add address=31.13.73.49 list=whatsapp_list
add address=31.13.74.49 list=whatsapp_list
add address=31.13.75.52 list=whatsapp_list
add address=31.13.76.81 list=whatsapp_list
add address=31.13.77.49 list=whatsapp_list
add address=31.13.78.53 list=whatsapp_list
add address=31.13.80.53 list=whatsapp_list
add address=31.13.81.53 list=whatsapp_list
add address=31.13.82.51 list=whatsapp_list
add address=31.13.83.51 list=whatsapp_list
add address=31.13.84.51 list=whatsapp_list
add address=31.13.85.51 list=whatsapp_list
add address=31.13.86.51 list=whatsapp_list
add address=31.13.87.51 list=whatsapp_list
add address=31.13.88.49 list=whatsapp_list
add address=31.13.90.51 list=whatsapp_list
add address=31.13.91.51 list=whatsapp_list
add address=31.13.92.52 list=whatsapp_list
add address=31.13.93.51 list=whatsapp_list
add address=31.13.94.52 list=whatsapp_list
add address=31.13.95.63 list=whatsapp_list
add address=50.22.198.204/30 list=whatsapp_list
add address=50.22.210.32/30 list=whatsapp_list
add address=50.22.210.128/27 list=whatsapp_list
add address=50.22.225.64/27 list=whatsapp_list
add address=50.22.235.248/30 list=whatsapp_list
add address=50.22.240.160/27 list=whatsapp_list
add address=50.23.90.128/27 list=whatsapp_list
add address=50.97.57.128/27 list=whatsapp_list
add address=75.126.39.32/27 list=whatsapp_list
add address=108.168.174.0/27 list=whatsapp_list
add address=108.168.176.192/26 list=whatsapp_list
add address=108.168.177.0/27 list=whatsapp_list
add address=108.168.180.96/27 list=whatsapp_list
add address=108.168.254.65 list=whatsapp_list
add address=108.168.255.224 list=whatsapp_list
add address=108.168.255.227 list=whatsapp_list
add address=157.240.0.53 list=whatsapp_list
add address=157.240.1.53 list=whatsapp_list
add address=157.240.2.53 list=whatsapp_list
add address=157.240.3.53 list=whatsapp_list
add address=157.240.6.53 list=whatsapp_list
add address=157.240.7.54 list=whatsapp_list
add address=157.240.8.53 list=whatsapp_list
add address=157.240.9.53 list=whatsapp_list
add address=157.240.10.53 list=whatsapp_list
add address=157.240.11.53 list=whatsapp_list
add address=157.240.12.53 list=whatsapp_list
add address=157.240.13.54 list=whatsapp_list
add address=158.85.0.96/27 list=whatsapp_list
add address=158.85.5.192/27 list=whatsapp_list
add address=158.85.46.128/27 list=whatsapp_list
add address=158.85.48.224/27 list=whatsapp_list
add address=158.85.58.0/25 list=whatsapp_list
add address=158.85.61.192/27 list=whatsapp_list
add address=158.85.224.160/27 list=whatsapp_list
add address=158.85.233.32/27 list=whatsapp_list
add address=158.85.249.128/27 list=whatsapp_list
add address=158.85.254.64/27 list=whatsapp_list
add address=169.44.23.192/27 list=whatsapp_list
add address=169.44.36.0/25 list=whatsapp_list
add address=169.44.57.64/27 list=whatsapp_list
add address=169.44.58.64/27 list=whatsapp_list
add address=169.44.80.0/26 list=whatsapp_list
add address=169.44.82.96/27 list=whatsapp_list
add address=169.44.82.128/27 list=whatsapp_list
add address=169.44.82.192/26 list=whatsapp_list
add address=169.44.83.0/26 list=whatsapp_list
add address=169.44.83.96/27 list=whatsapp_list
add address=169.44.83.128/27 list=whatsapp_list
add address=169.44.83.192/26 list=whatsapp_list
add address=169.44.84.0/24 list=whatsapp_list
add address=169.44.85.64/27 list=whatsapp_list
add address=169.44.87.160/27 list=whatsapp_list
add address=169.44.167.0/27 list=whatsapp_list
add address=169.45.71.32/27 list=whatsapp_list
add address=169.45.71.96/27 list=whatsapp_list
add address=169.45.87.128/26 list=whatsapp_list
add address=169.45.169.192/27 list=whatsapp_list
add address=169.45.182.96/27 list=whatsapp_list
add address=169.45.210.64/27 list=whatsapp_list
add address=169.45.214.224/27 list=whatsapp_list
add address=169.45.219.224/27 list=whatsapp_list
add address=169.45.237.192/27 list=whatsapp_list
add address=169.45.238.32/27 list=whatsapp_list
add address=169.45.248.96/27 list=whatsapp_list
add address=169.45.248.160/27 list=whatsapp_list
add address=169.46.52.224/27 list=whatsapp_list
add address=169.46.111.144/28 list=whatsapp_list
add address=169.47.5.192/26 list=whatsapp_list
add address=169.47.6.64/27 list=whatsapp_list
add address=169.47.33.128/27 list=whatsapp_list
add address=169.47.35.32/27 list=whatsapp_list
add address=169.47.37.128/27 list=whatsapp_list
add address=169.47.40.128/27 list=whatsapp_list
add address=169.47.42.96/27 list=whatsapp_list
add address=169.47.42.160/27 list=whatsapp_list
add address=169.47.42.192/26 list=whatsapp_list
add address=169.47.47.160/27 list=whatsapp_list
add address=169.47.130.96/27 list=whatsapp_list
add address=169.47.192.192/27 list=whatsapp_list
add address=169.47.194.128/27 list=whatsapp_list
add address=169.47.198.128/27 list=whatsapp_list
add address=169.47.212.160/27 list=whatsapp_list
add address=169.53.29.128/27 list=whatsapp_list
add address=169.53.48.32/27 list=whatsapp_list
add address=169.53.71.224/27 list=whatsapp_list
add address=169.53.81.64/27 list=whatsapp_list
add address=169.53.250.128/26 list=whatsapp_list
add address=169.53.252.64/27 list=whatsapp_list
add address=169.53.255.64/27 list=whatsapp_list
add address=169.54.2.160/27 list=whatsapp_list
add address=169.54.44.224/27 list=whatsapp_list
add address=169.54.51.32/27 list=whatsapp_list
add address=169.54.55.192/27 list=whatsapp_list
add address=169.54.193.160/27 list=whatsapp_list
add address=169.54.210.0/27 list=whatsapp_list
add address=169.54.222.128/27 list=whatsapp_list
add address=169.55.67.224/27 list=whatsapp_list
add address=169.55.69.128/26 list=whatsapp_list
add address=169.55.74.32/27 list=whatsapp_list
add address=169.55.75.96/27 list=whatsapp_list
add address=169.55.100.160/27 list=whatsapp_list
add address=169.55.126.64/26 list=whatsapp_list
add address=169.55.210.96/27 list=whatsapp_list
add address=169.55.235.160/27 list=whatsapp_list
add address=173.192.162.32/27 list=whatsapp_list
add address=173.192.219.128/27 list=whatsapp_list
add address=173.192.222.160/27 list=whatsapp_list
add address=173.192.231.32/27 list=whatsapp_list
add address=173.193.205.0/27 list=whatsapp_list
add address=173.193.230.96/27 list=whatsapp_list
add address=173.193.230.128/27 list=whatsapp_list
add address=173.193.230.192/27 list=whatsapp_list
add address=173.193.239.0/27 list=whatsapp_list
add address=174.36.208.128/27 list=whatsapp_list
add address=174.36.210.32/27 list=whatsapp_list
add address=174.36.251.192/27 list=whatsapp_list
add address=174.37.199.192/27 list=whatsapp_list
add address=174.37.217.64/27 list=whatsapp_list
add address=174.37.243.64/27 list=whatsapp_list
add address=174.37.251.0/27 list=whatsapp_list
add address=179.60.192.51 list=whatsapp_list
add address=179.60.195.51 list=whatsapp_list
add address=184.173.136.64/27 list=whatsapp_list
add address=184.173.147.32/27 list=whatsapp_list
add address=184.173.161.64 list=whatsapp_list
add address=184.173.173.116 list=whatsapp_list
add address=184.173.179.32/27 list=whatsapp_list
add address=185.60.216.53 list=whatsapp_list
add address=185.60.218.53 list=whatsapp_list
add address=185.60.219.53 list=whatsapp_list
add address=192.155.212.192/27 list=whatsapp_list
add address=198.11.193.182/31 list=whatsapp_list
add address=198.11.251.32/27 list=whatsapp_list
add address=198.23.80.0/27 list=whatsapp_list
add address=208.43.115.192/27 list=whatsapp_list
add address=208.43.117.79 list=whatsapp_list
add address=208.43.122.128/27 list=whatsapp_list

https://aacable.wordpress.com/tag/whatsapp-address-list/

File: /MIkrotik Speedtest IP Address List.txt
/ip firewall address-list
add address=yougetsignal.com list=speedtest
add address=xmyip.com list=speedtest
add address=www.yougetsignal.com list=speedtest
add address=expressvpn.com list=speedtest
add address=www.expressvpn.com list=speedtest
add address=whatismyip.net list=speedtest
add address=speedtestcustom.com list=speedtest
add address=income.speedtestcustom.com  list=speedtest
add address=iplocation.net  list=speedtest
add address=www.iplocation.net  list=speedtest
add address=www.astrill.com  list=speedtest
add address=www.privateinternetaccess.com  list=speedtest
add address=mxtoolbox.com list=speedtest
add address=ifconfig.co  list=speedtest
add address=whatismyip.org  list=speedtest
add address=www.goldenfrog.com list=speedtest
add address=www.mxtoolbox.com  list=speedtest
add address=www.ultratools.com  list=speedtest
add address=www.ip-adress.eu list=speedtest
add address=www.vermiip.es list=speedtest
add address=www.purevpn.com list=speedtest
add address=www.whatismybrowser.com list=speedtest
add address=zenmate.com list=speedtest
add address=www.ipchicken.com list=speedtest
add address=bittrex.com list=speedtest
add address=whatismyip.li list=speedtest
add address=www.ipburger.com list=speedtest
add address=cbn.net.id list=speedtest
add address=whatismyip4.com list=speedtest
add address=www.inmotionhosting.com list=speedtest
add address=nordvpn.com list=speedtest
add address=wolframalpha.com list=speedtest
add address=cactusvpn.com list=speedtest
add address=www.cactusvpn.com list=speedtest
add address=m.wolframalpha.com list=speedtest
add address=ipcow.com list=speedtest
add address=whatismycountry.com list=speedtest
add address=passwordsgenerator.net list=speedtest
add address=att-services.net list=speedtest
add address=wtfismyip.com list=speedtest
add address=whatismyip.network list=speedtest
add address=ipinfo.info list=speedtest
add address=encodable.com list=speedtest
add address=www.overplay.net list=speedtest
add address=myipaddress.com list=speedtest
add address=www.myipaddress.com list=speedtest
add address=whoer.net list=speedtest
add address=whatismyip.com list=speedtest
add address=www.speedtest.net list=speedtest
add address=c.speedtest.net list=speedtest
add address=whatismyipaddress.com list=speedtest
add address=whatismyip.host list=speedtest
add address=bearsmyip.com list=speedtest
add address=check-host.net list=speedtest
add address=hide.me list=speedtest
add address=ipv6test.hide.me list=speedtest
add address=www.perfect-privacy.com list=speedtest
add address=perfect-privacy.com list=speedtest
add address=www.whatsmyip.org list=speedtest
add address=whatsmyip.org list=speedtest
add address=speedtest.cbn.net.id list=speedtest
add address=speedtest.co.id list=speedtest
add address=speedtest.googlefiber.net list=speedtest
add address=speedtest.net list=speedtest
add address=speedtest.biznetnetworks.com list=speedtest
add address=speedtest.com.sg list=speedtest
add address=speedtest-sgp1.digitalocean.com list=speedtest
add address=speedtest.unsyiah.ac.id list=speedtest
add address=ambon.speedtest.telkom.net.id list=speedtest
add address=balikpapan.speedtest.telkom.net.id list=speedtest
add address=bandung.speedtest.telkom.net.id list=speedtest
add address=sp1-sby.wowrack.co.id list=speedtest
add address=speedtest.sby.dnet.net.id list=speedtest
add address=speedtest-sby.hyper.net.id list=speedtest
add address=coresub1.tri.co.id list=speedtest
add address=speedtest.sby.datautama.net.id list=speedtest
add address=surabaya.speedtest.telkom.net.id list=speedtest
add address=sby-speedtest.link.net.id list=speedtest
add address=speedtest-sby.moratelindo.co.id list=speedtest
add address=debianx.petra.ac.id list=speedtest
add address=www.padi.net.id list=speedtest
add address=coresoc1.tri.co.id list=speedtest
add address=speedtest.solo.citra.net.id list=speedtest
add address=speedtest1.moratelindo.co.id list=speedtest
add address=kuta.speedtest.gratis.net.id list=speedtest
add address=speedtest.ugm.ac.id list=speedtest
add address=speedtest.citra.net.id list=speedtest
add address=speedtest1.oss.myrepublic.co.id list=speedtest
add address=speedinternet.varnion.com list=speedtest
add address=speedtest.channel-11.net list=speedtest
add address=bdl.lampungmonitor.com list=speedtest
add address=speedtest-lampung.hypernet.co.id list=speedtest
add address=43.254.127.234 list=speedtest
add address=speedtest.verd.co.id list=speedtest
add address=speedtest.starnet.net.id list=speedtest
add address=corebdo1.tri.co.id list=speedtest
add address=bdg-speedtest.link.net.id list=speedtest
add address=speedtest-bdg.hyper.net.id list=speedtest
add address=st1.unpad.ac.id list=speedtest
add address=nms-bdg.neuviz.net.id list=speedtest
add address=sp1.unlam.ac.id list=speedtest
add address=banjarmasin.speedtest.telkom.net.id list=speedtest
add address=sp1.solnet.net.id list=speedtest
add address=speedtest.nap.net.id list=speedtest
add address=speedtest.ipungpurbaya.net list=speedtest
add address=speedtest-btm.moratelindo.co.id list=speedtest
add address=batam.speedtest.telkom.net.id list=speedtest
add address=sg.ipungpurbaya.net list=speedtest
add address=corebth4.tri.co.id list=speedtest
add address=st-btm1.mlink.net.id list=speedtest
add address=speedtest.cyberplus.net.id list=speedtest
add address=speedtest.king.net.id list=speedtest
add address=speedtest1.telkomsel.com list=speedtest
add address=speedtest.pesat.net.id list=speedtest
add address=speedtest2.starnet.net.id list=speedtest
add address=speedtest.bits.net.id list=speedtest
add address=speedtest.smartconnect.id list=speedtest
add address=coredps1.tri.co.id list=speedtest
add address=denpasar.speedtest.telkom.net.id list=speedtest
add address=speedtestdps1.gmedia.net.id list=speedtest
add address=speedtest.dps.dnet.net.id list=speedtest
add address=speedtest-bali.hyper.net.id list=speedtest
add address=speedtest2.gunadarma.net list=speedtest
add address=st-dumai1.mlink.net.id list=speedtest
add address=speedtest.sumberdata.co.id list=speedtest
add address=speedtest.ats-com.net list=speedtest
add address=speedtest.qiandra.net.id list=speedtest
add address=speedtest.tachyon.net.id list=speedtest
add address=st1.mlink.net.id list=speedtest
add address=jkt1.speedtest.tri.co.id list=speedtest
add address=s1.ikamisa96.id list=speedtest
add address=speedtest.primacom.co.id list=speedtest
add address=speedtest.angkasa.id list=speedtest
add address=speedtest-ix.idola.net.id list=speedtest
add address=speedtest.circleone.net.id list=speedtest
add address=speedtest-jkt1.skyline.net.id list=speedtest
add address=speedtest.idola.net.id list=speedtest
add address=speedtest1.inet.net.id list=speedtest
add address=speedtest-iix.xl.net.id list=speedtest
add address=sp1-jkt.wowrack.co.id list=speedtest
add address=support.naftalie.net list=speedtest
add address=www.vstream.id list=speedtest
add address=speedone.maduroo.com list=speedtest
add address=speedtest.gig.id list=speedtest
add address=speedtest.nes.co.id list=speedtest
add address=speedtest.maxindo.net.id list=speedtest
add address=speedtest.balifiber.id list=speedtest
add address=jkt1-speedtest.smartfren.com list=speedtest
add address=speedtest.vjn.co.id list=speedtest
add address=58.147.188.41 list=speedtest
add address=speedtest-noc.moratelindo.co.id list=speedtest
add address=speedtest-jkt.hypernet.co.id list=speedtest
add address=speedtest.houtos.com list=speedtest
add address=speed.mncplay.id list=speedtest
add address=speedtest-jkt01.bit-teknologi.com list=speedtest
add address=speedtest.biznetgiocloud.com list=speedtest
add address=mainspeedtest.nap.net.id list=speedtest
add address=speedtest1.jlm.net.id list=speedtest
add address=sp1.swin.co.id list=speedtest
add address=speedtest.varnion.com list=speedtest
add address=speedtest.sdi.net.id list=speedtest
add address=speedtest.telin.co.id list=speedtest
add address=103.197.188.181 list=speedtest
add address=speedtest.rndlabbankmandiri.co.id list=speedtest
add address=speedtest.indosat.com list=speedtest
add address=jakarta.speedtest.telkom.net.id list=speedtest
add address=speedtest.net1.co.id list=speedtest
add address=ooklaspeed.axarva.id list=speedtest
add address=speedtest.dtp.net.id list=speedtest
add address=hfs.cni.net.id list=speedtest
add address=speedtest.zettagrid.id list=speedtest
add address=ookla-id1.buana.net list=speedtest
add address=jkt-speedtest.fast.net.id list=speedtest
add address=speedtest.bitek.net.id list=speedtest
add address=iperf-1.ntt.net.id list=speedtest
add address=speedtest-iix.xl.co.id list=speedtest
add address=speedtest1.boltsuper4g.com list=speedtest
add address=speedtest.orion.net.id list=speedtest
add address=corecgk2.tri.co.id list=speedtest
add address=speedtest.smartmedia.net.id list=speedtest
add address=jayapura.speedtest.telkom.net.id list=speedtest
add address=speedtest-bali.biznetgiocloud.com list=speedtest
add address=sp1.jogjamedianet.com list=speedtest
add address=speedtest.lungit.com list=speedtest
add address=speedtest.jogja.citra.net.id list=speedtest
add address=kalianda.lampungmonitor.com list=speedtest
add address=test.neuviz.net.id list=speedtest
add address=speedtest.mtmbali.com list=speedtest
add address=speedtest.blueline.co.id list=speedtest
add address=makasar.speedtest.telkom.net.id list=speedtest
add address=coreupg1.tri.co.id list=speedtest
add address=speedtestmlg1.gmedia.net.id list=speedtest
add address=speedtest.ub.ac.id list=speedtest
add address=sp1.infotek.net.id list=speedtest
add address=noc.unsrat.ac.id list=speedtest
add address=manado.speedtest.telkom.net.id list=speedtest
add address=mataram.speedtest.telkom.net.id list=speedtest
add address=speedtest.nusa.net.id list=speedtest
add address=medan.speedtest.telkom.net.id list=speedtest
add address=speedtest-mdn.moratelindo.co.id list=speedtest
add address=metro.lampungmonitor.com list=speedtest
add address=st-pdg1.mlink.net.id list=speedtest
add address=coreplm1.tri.co.id list=speedtest
add address=palembang.speedtest.telkom.net.id list=speedtest
add address=palu.kailiglobal.com list=speedtest
add address=speedtest-1.wanxp.id list=speedtest
add address=st-riau1.mlink.net.id list=speedtest
add address=speedtest.dash.net.id list=speedtest
add address=pekanbaru.speedtest.telkom.net.id list=speedtest
add address=corepku1.tri.co.id list=speedtest
add address=speedtest1.bali.ldp.net.id list=speedtest
add address=speed.undip.ac.id list=speedtest
add address=speedtest-smg.hypernet.co.id list=speedtest
add address=semarang.speedtest.telkom.net.id list=speedtest
add address=mm1.unnes.ac.id list=speedtest
add address=speedtestsmg1.gmedia.net.id list=speedtest
add address=corecgk1.tri.co.id list=speedtest
add address=sorong.speedtest.telkom.net.id list=speedtest
add address=speedtest.crypto.net.id list=speedtest
add address=sby1-speedtest.smartfren.com list=speedtest
add address=203.6.148.212 list=speedtest
add address=speed1.wds.co.id list=speedtest
add address=speedtest.link.net.id list=speedtest
add address=speedtest2.telkomsel.com list=speedtest
add address=ternate.speedtest.telkom.co.id list=speedtest
add address=timika.speedtest.telkom.net.id list=speedtest
add address=sp.uny.ac.id list=speedtest
add address=speedtestyk1.gmedia.net.id list=speedtest
add address=ookla.uii.ac.id list=speedtest
add address=www.speedtestserver.com list=speedtest
add address=speedtest10.vqbn.com list=speedtest
add address=speedtest-intl.xl.co.id list=speedtest
add address=speedtest.lovelivesupport.com list=speedtest
add address=speedtest.myrepublic.com.sg list=speedtest
add address=speedtest2.indosat.com list=speedtest
add address=speedtest-intl.xl.net.id list=speedtest
add address=sgspeedtest.nap.net.id list=speedtest
add address=ookla.usonyx.net list=speedtest
add address=speedtest.singnet.com.sg list=speedtest
add address=speedtest.telin.sg list=speedtest
add address=sin.speedtest.interoute.net list=speedtest
add address=speedtest.super.net.sg list=speedtest
add address=apac-sg-ookla1.offsitedatasync.com list=speedtest
add address=ookla-singapore.renaissance.com list=speedtest
add address=sg-speedtest.fast.net.id list=speedtest
add address=speedtest07.fpt.vn list=speedtest
add address=co2speedtest1.starhub.com list=speedtest
add address=m1speedtest1.m1net.com.sg list=speedtest
add address=speedtest.sg.bgp.net list=speedtest
add address=202.3.78.3 list=speedtest
add address=speedtest.vodien.com list=speedtest
add address=speedtest-sg.moratelindo.co.id list=speedtest
add address=speedtest.sng01.softlayer.com list=speedtest
add address=speedtest-sg01.bit-teknologi.com list=speedtest
add address=speedtest08.fpt.vn list=speedtest
add address=speedtest.apac.aptilon.com list=speedtest
add address=vps5.vianet.com.np list=speedtest
add address=speedtest-sgp.apac-tools.ovh list=speedtest
add address=speedtest.netpluz.asia list=speedtest
add address=test-ipv6.com list=speedtest
add address=speedtest.net.in list=speedtest
add address=speedtest.unud.ac.id list=speedtest
add address=speedtest-bali.smartconnect.id list=speedtest
add address=speedtest.bali.gerbangakses.net.id list=speedtest
add address=speedtest.cifo.co.id list=speedtest
add address=testspeed.melsa.net.id list=speedtest
add address=speedtest.acenet.net.id list=speedtest
add address=speedtest-bali.hypernet.co.id list=speedtest
add address=speedtest2.unud.ac.id list=speedtest
add address=speedtest.jinom.net.id list=speedtest
add address=speedtest.faznet.co.id list=speedtest
add address=speedtest.sti-group.co.id list=speedtest
add address=speedtest2.centrin.net.id list=speedtest
add address=stest.ltn.net.id list=speedtest
add address=speedtest.iconpln.net.id list=speedtest
add address=speedtest.jagat.net.id list=speedtest
add address=test.ads.net.id list=speedtest
add address=speedtest.powertel.co.id list=speedtest
add address=ookla.gigacommunity.id list=speedtest
add address=speedtest.upg.crypto.net.id list=speedtest
add address=speedtest.jatengprov.go.id list=speedtest
add address=spd1.inti.net.id list=speedtest
add address=speedtest.turbo.net.id list=speedtest
add address=bwtest.tanahbumbukab.go.id list=speedtest
add address=speedtest.umn.ac.id list=speedtest
add address=speedtest.routelink.net.id list=speedtest
add address=www.speedtest.com.sg list=speedtest
add address=speed.sng.host.co.ug list=speedtest

File: /README.md
https://github.com/alsyundawy/mikrotik-blacklist


File: /RESET COUNTER MIKROTIK.txt
Script untuk mereset counter di mikrotik

/ip firewall filter reset-counters-all
/ip firewall nat reset-counters-all
/ip firewall mangle reset-counters-all
/queues simple reset-counters-all
/queues tree reset-counters-all

File: /Reset database User Manager ke default.txt
# Cara Reset atau membersikan database User Manager ke default
/tool user-manager database clear

File: /Routing Sederhana dengan FailOver 3 Gateway.txt
#Contoh Routing Sederhana dengan FailOver 3 Gateway
WAN-1 = IP 192.168.2.2/24
WAN-2 = IP 192.168.3.2/24
WAN-2 = IP 192.168.4.2/24

/ip route
add check-gateway=ping distance=1 gateway=192.168.2.1 target-scope=10
add check-gateway=ping distance=2 gateway=192.168.3.1 target-scope=10
add check-gateway=ping distance=3 gateway=192.168.4.1 target-scope=10

File: /Safe Search Google and Restricted Mode YouTube.txt
/ip firewall nat
add action=redirect chain=dstnat dst-port=53 protocol=udp

/ip dns set allow-remote-requests=yes

/ip dns static
add address=216.239.38.120 name=google.com comment="Pencarian Mode Aman"
add address=216.239.38.120 name=www.google.com comment="Pencarian Mode Aman"
add address=216.239.38.120 name=https://google.com comment="Pencarian Mode Aman"
add address=216.239.38.120 name=https://www.google.com comment="Pencarian Mode Aman"
add address=216.239.38.120 name=google.com.mx comment="Pencarian Mode Aman"
add address=216.239.38.120 name=www.google.com.mx comment="Pencarian Mode Aman"
add address=216.239.38.120 name=https://google.com.mx comment="Pencarian Mode Aman"
add address=216.239.38.120 name=https://www.google.com.mx comment="Pencarian Mode Aman"

/ip dns static
add address=216.239.38.119 name=youtube.com comment="Mode Youtube Aman"
add address=216.239.38.119 name=www.youtube.com comment="Mode Youtube Aman"
add address=216.239.38.119 name=https://www.youtube.com comment="Mode Youtube Aman"
add address=216.239.38.119 name=m.youtube.com comment="Mode Youtube Aman"
add address=216.239.38.119 name=https://m.youtube.com comment="Mode Youtube Aman"
add address=216.239.38.119 name=youtubei.googleapis.com comment="Mode Youtube Aman"
add address=216.239.38.119 name=https://youtubei.googleapis.com comment="Mode Youtube Aman"
add address=216.239.38.119 name=youtube.googleapis.com comment="Mode Youtube Aman"
add address=216.239.38.119 name=https://youtube.googleapis.com comment="Mode Youtube Aman"
add address=216.239.38.119 name=www.youtube-nocookie.com comment="Mode Youtube Aman"

File: /Script Always On top di simple Queue Mikrotik.txt
# script ini agar QUEUE utama selalu berada di urutan paling atas
/queue simple move [find name="NAMA-QUEUE"] [:pick [find] 0]

File: /SCRIPT DNS CACHE FLUSH.txt
Bisa di coba di terminal, script atau di schedular

/ip dns cache flush

File: /Script Otomatis Custom Queue Tree dan Mangle Hotspot Mikroti.txt
1.Syarat Rate Limit (rx/tx) dikosongin
2.Jika menggunakan user manager tinggal masukin nama profile hotspot ke dalam Group name pada usermanager, jangan lupa Rate limit di kosongin
3. Sesuaikan nama parent, di contoh saya menggunakan "7.ALL HTSPOT"
Saat user login Script ini akan otomatis menambahkan input baru pada queue tree dan mangle, dan akan menghapus kembali ketika user logout. kekurangan script ini saya membuat upload dan download dalam satu paket, kalau mau terpisah silahkan dimodifikasi sesuai kebutuhan kebutuhan :)

# SCRIPT ON LOGIN
:local datetime [/system clock get date];
:local timedate [/system clock get time];
[/ip firewall mangle add action=mark-packet chain=prerouting dst-address="$address" new-packet-mark=("paket-"."$address") passthrough=no comment=("paket-"."$address")];
[/ip firewall mangle add action=mark-packet chain=forward dst-address="$address" new-packet-mark=("paket-"."$address") passthrough=no comment=("paket-"."$address")];
[/queue tree add max-limit=2M name=("$user"." -> "."$address") comment=("Login at: [ $timedate - $datetime ] From: [ $interface ] Mac: [ ".$"mac-address"." ]") packet-mark=("paket-"."$address") queue="HS-Down" parent="7.ALL HOTSPOT"];
:log warning ("--> [ $user ] Login at: [ $timedate - $datetime ] From: [ $interface ] Mac: [ ".$"mac-address"." ]")

# SCRIPT ON LOGOUT
/queue tree remove [find packet-mark=("paket-"."$address")] ;
/ip firewall mangle remove [find where comment=("paket-"."$address")]
:log warning ("--> [ $user ] Logout at: [ $timedate - $datetime ] From: [ $interface ] Mac: [ ".$"mac-address"." ]")

File: /Script Otomatis Custom Simple Queue Hotspot Mikrotik.txt
Siapa tau berguna buat otomatis custom simple queue untuk hotspot
1.Syarat Rate Limit (rx/tx) dikosongin
2.Jika ada parent tinggal tambahkan script untuk parent contoh parent="3.PREMIUM"
3.Jika menggunakan user manager tinggal masukin nama profile hotspot ke dalam Group name pada usermanager, jangan lupa Rate limit di kosongin

# Script Pada On Login:
:local datetime [/system clock get date];
:local timedate [/system clock get time];
/queue simple add name="$user -> $address" comment=("Login at: [ $timedate - $datetime ] From: [ $interface ] Mac: [ ".$"mac-address"." ]") target="$address" max-limit=1M/1M
:log warning ("--> [ $user ] Login at: [ $timedate - $datetime ] From: [ $interface ] Mac: [ ".$"mac-address"." ]")

# Script Pada On Logout:
/queue simple remove [find name="$user -> $address"] ;
:log warning ("--> [ $user ] Logout at: [ $timedate - $datetime ] From: [ $interface ] Mac: [ ".$"mac-address"." ]")

File: /Script Otomatis Untuk membuat Queue Tree IP 1-255.txt
:for e from 1  to 254 do={/queue tree add name="CLIENT-$e" packet-mark="mark-pc$e" parent="GLOBAL" max-limit=2M}

File: /Script Otomatis Untuk membuat simple Queue IP 1-255.txt
:for e from 1  to 254 do={ /queue simple add name="CLIENT-$e" target="192.168.1.$e" max-limit=1M/2M}

File: /Seberapa aman Jaringan Mikrotik kita dari serangan luar.txt
Jaringan Warnet atau Hotspot tidak peduli menggunakan router Mikrotik atau Cisco sebenarnya tidak aman 100%, dengan hanya melihat beberapa celah yang terbuka sebenarnya bisa saja seseorang mencoba menyusup kedalamam jaringan kita.

Untuk memastikan aman tidaknya jaringan Router kita,silahkan ditest aja langsung dengan menggunakan tool ini.

1. Buka site https://www.grc.com
2. Pilih tab "Services"
3. Pilih "ShildsUP!"
4. Tekan tombol "Proceed"
5. pilih Tab "All Service Port"
6. Biarkan Proses scaning port berjalan

Hasil Scan Port Jaringan BuanaNET saat ini.
GRC Port Authority Report created on UTC: 2015-03-28 at 16:22:33
Results from scan of ports: 0-1055
0 Ports Open
1055 Ports Closed
1 Ports Stealth
---------------------
1056 Ports Tested
NO PORTS were found to be OPEN.
The port found to be STEALTH was: 53
Other than what is listed above, all ports are CLOSED.
TruStealth: FAILED - NOT all tested ports were STEALTH,
                   - NO unsolicited packets were received,
                   - A PING REPLY (ICMP Echo) WAS RECEIVED.
Diatas adalah hasil scanning port milik saya dan bisa dipastikan hanya ada satu celah yang terbuka yaitu di port 53 (DNS). Jika milik rekan semua banyak port yang terbuka dan memang tidak digunakan sebaiknya ditutup saja terutama untuk koneksi port SSH, Telnet dan FTP karena serangan banyak terjadi di arena ini.

Sedikit masukan port yang rentang terhadap serangan yang sebaiknya di perhatikan:
Telnet (23)
SSH (22)
FTP (21)
WINBOX (8291)
WWW (80)
WWW-SSL (443)
API (8728)
API-SSL (8729)
DNS (53, 5353, 443)
PROXY (3128)
PROXY (8080)

Salam - BuanaNET

File: /Speedtest Mangle  layer7 Mikrotik.txt
/queue tree
add limit-at=100M max-limit=100M name=SPEEDTEST parent=global priority=1 queue=default
add limit-at=100M max-limit=100M name="1.SpeedTest UP" packet-mark=speedtest_pkt-up parent=SPEEDTEST priority=1 queue=default
add limit-at=100M max-limit=100M name="2.SpeedTest DOWN" packet-mark=speedtest_pkt-down parent=SPEEDTEST priority=1 queue=default

/ip firewall layer7-protocol
add name=speedtest regexp="^.+(speedtest).*\$"

/ip firewall Mangle
add action=mark-connection chain=prerouting layer7-protocol=speedtest new-connection-mark=speedtest_conn
add action=mark-connection chain=prerouting dst-port=8080 new-connection-mark=speedtest_conn protocol=tcp
add action=mark-connection chain=postrouting new-connection-mark=speedtest_conn protocol=tcp src-port=8080
add action=mark-packet chain=prerouting connection-mark=speedtest_conn new-packet-mark=speedtest_pkt-up passthrough=no src-address=192.168.1.0/24
add action=mark-packet chain=prerouting connection-mark=speedtest_conn dst-address=192.168.1.0/24 new-packet-mark=speedtest_pkt-down passthrough=no
add action=mark-packet chain=postrouting connection-mark=speedtest_conn new-packet-mark=speedtest_pkt-up passthrough=no src-address=192.168.1.0/24
add action=mark-packet chain=postrouting connection-mark=speedtest_conn dst-address=192.168.1.0/24 new-packet-mark=speedtest_pkt-down passthrough=no

File: /Speedtest Regexp Layer 7.txt
# Speedtest Regexp Layer 7
/ip firewall layer7-protocol
add name=speedtest regexp="^.+(speedtest).*\$"

File: /Trik Bermain NoMark Tanpa Mangle di Queue Tree.txt
Bermain no-mark tanpa mangle di Queue Tree lumayan meringankan beban router bagus digunakan untuk hotspot yang gak mau ribet dimangle, trik ini juga bisa digunakan untuk memfilter paket dimangle yang bocor.

/queue tree
add max-limit=10M name=2.Upload packet-mark=no-mark parent=E1-WAN queue= default
add max-limit=10M name=3.Download packet-mark=no-mark parent=E4-LAN queue=default
add max-limit=20M name="1.Total No-mark" packet-mark=no-mark parent=global queue=default

File: /Trik Load Balancing PCC untuk hotspot.txt
#cara load balancing PCC untuk hotspot 
#untuk hotspot kita hanya perlu menambahkan "hotspot=auth"

/ip fi man
add action=mark-connection chain=prerouting disabled=no dst-address-type=!local hotspot=auth in-interface=LAN new-connection-mark=WAN1_conn passthrough=yes per-connection-classifier=both-addresses-and-ports:2/0
add action=mark-connection chain=prerouting disabled=no dst-address-type=!local hotspot=auth in-interface=LAN new-connection-mark=WAN2_conn passthrough=yes per-connection-classifier=both-addresses-and-ports:2/1

