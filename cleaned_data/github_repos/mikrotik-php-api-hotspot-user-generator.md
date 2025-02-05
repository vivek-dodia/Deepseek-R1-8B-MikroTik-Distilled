# Repository Information
Name: mikrotik-php-api-hotspot-user-generator

# Directory Structure
Directory structure:
└── github_repos/mikrotik-php-api-hotspot-user-generator/
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
    │   │       ├── pack-0d5b132b36dd45199e7dca8b8a35548867f785e9.idx
    │   │       └── pack-0d5b132b36dd45199e7dca8b8a35548867f785e9.pack
    │   ├── packed-refs
    │   └── refs/
    │       ├── heads/
    │       │   └── master
    │       ├── remotes/
    │       │   └── origin/
    │       │       └── HEAD
    │       └── tags/
    ├── .htaccess
    ├── aksi/
    │   ├── js/
    │   │   ├── editiden/
    │   │   │   └── editiden.js
    │   │   ├── editpass/
    │   │   │   └── editpass.js
    │   │   ├── limitasi/
    │   │   │   ├── hapus.js
    │   │   │   └── save.js
    │   │   ├── login/
    │   │   │   └── aksi_login.js
    │   │   ├── profile/
    │   │   │   └── update.js
    │   │   ├── reboot/
    │   │   │   └── reboot.js
    │   │   ├── userhotspot/
    │   │   │   ├── generate.js
    │   │   │   ├── hapus.js
    │   │   │   └── save.js
    │   │   └── usermikrotik/
    │   │       ├── hapus.js
    │   │       └── save.js
    │   └── php/
    │       ├── editiden/
    │       │   └── editiden.php
    │       ├── editpass/
    │       │   └── editpass.php
    │       ├── limitasi/
    │       │   ├── hapus.php
    │       │   └── save.php
    │       ├── login/
    │       │   └── aksi_login.php
    │       ├── profile/
    │       │   └── update.php
    │       ├── reboot/
    │       │   └── reboot.php
    │       ├── userhotspot/
    │       │   ├── cek_data.php
    │       │   ├── generate.php
    │       │   ├── hapus.php
    │       │   └── save.php
    │       └── usermikrotik/
    │           ├── hapus.php
    │           └── save.php
    ├── css/
    │   └── theme.css
    ├── fpdf/
    │   ├── font/
    │   │   ├── courier.php
    │   │   ├── courierb.php
    │   │   ├── courierbi.php
    │   │   ├── courieri.php
    │   │   ├── helvetica.php
    │   │   ├── helveticab.php
    │   │   ├── helveticabi.php
    │   │   ├── helveticai.php
    │   │   ├── symbol.php
    │   │   ├── times.php
    │   │   ├── timesb.php
    │   │   ├── timesbi.php
    │   │   ├── timesi.php
    │   │   └── zapfdingbats.php
    │   ├── fpdf.css
    │   └── fpdf.php
    ├── halaman/
    │   ├── data_limitasi.php
    │   ├── data_user_aktif.php
    │   ├── data_user_hotspot.php
    │   ├── data_user_mikrotik.php
    │   ├── edit_identity_mikrotik.php
    │   ├── edit_password_mikrotik.php
    │   ├── generate_user_hotspot.php
    │   ├── profile.php
    │   ├── tambah_group_limitasi.php
    │   ├── tambah_user_hotspot.php
    │   ├── tambah_user_mikrotik.php
    │   └── utama.php
    ├── images/
    ├── index.php
    ├── lib/
    │   ├── bootstrap/
    │   │   ├── css/
    │   │   │   └── bootstrap.css
    │   │   ├── img/
    │   │   └── js/
    │   │       └── bootstrap.js
    │   └── font-awesome/
    │       ├── .gitignore
    │       ├── css/
    │       │   ├── font-awesome-ie7.css
    │       │   └── font-awesome.css
    │       ├── font/
    │       │   ├── fontawesome-webfont.eot
    │       │   ├── fontawesome-webfont.ttf
    │       │   └── fontawesome-webfont.woff
    │       ├── FontAwesome.ttf
    │       ├── less/
    │       │   ├── font-awesome-ie7.less
    │       │   └── font-awesome.less
    │       ├── README.md
    │       └── sass/
    │           ├── font-awesome.sass
    │           └── font-awesome.scss
    ├── login.php
    ├── logout.php
    ├── penting/
    │   ├── excel_export.php
    │   ├── koneksi.php
    │   ├── pdf_export.php
    │   └── routeros_api.php
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
	url = https://github.com/tauhidcp/mikrotik-php-api-hotspot-user-generator.git
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
0000000000000000000000000000000000000000 18e154d9e43ba722d0df4463f662ffde3e17d567 vivek-dodia <vivek.dodia@icloud.com> 1738606036 -0500	clone: from https://github.com/tauhidcp/mikrotik-php-api-hotspot-user-generator.git


File: /.git\logs\refs\heads\master
0000000000000000000000000000000000000000 18e154d9e43ba722d0df4463f662ffde3e17d567 vivek-dodia <vivek.dodia@icloud.com> 1738606036 -0500	clone: from https://github.com/tauhidcp/mikrotik-php-api-hotspot-user-generator.git


File: /.git\logs\refs\remotes\origin\HEAD
0000000000000000000000000000000000000000 18e154d9e43ba722d0df4463f662ffde3e17d567 vivek-dodia <vivek.dodia@icloud.com> 1738606036 -0500	clone: from https://github.com/tauhidcp/mikrotik-php-api-hotspot-user-generator.git


File: /.git\packed-refs
# pack-refs with: peeled fully-peeled sorted 
18e154d9e43ba722d0df4463f662ffde3e17d567 refs/remotes/origin/master


File: /.git\refs\heads\master
18e154d9e43ba722d0df4463f662ffde3e17d567


File: /.git\refs\remotes\origin\HEAD
ref: refs/remotes/origin/master


File: /.htaccess
Options All -Indexes

File: /aksi\js\editiden\editiden.js
$jnoc(document).ready(function(){
	$jnoc('#giden').validate({
				rules: {
					iden: {
						required: true
					}
					},
				messages: {
				    iden: {
						required : "Identity Harus diisi"
					}    
				},
				submitHandler: function(form) {
				
				$jnoc("#lproses").show();
				var iden = $jnoc("#iden").val();
				
				$jnoc.ajax({
					url: "aksi/php/editiden/editiden.php", 
					type:"POST",
					data: { aksi:"editiden",iden:iden },
					dataType:"json",
					chache: false,
					success : function(respon){
					if (respon==1){
					$jnoc("#lproses").hide();
					$jnoc('.error-text').text("Identity Mikrotik SUKSES diganti");  
					$jnoc("#myModal").modal("show");
					} else if (respon==0) {
					$jnoc("#lproses").hide();
					$jnoc('.error-text').text("Identity Mikrotik GAGAL diganti");  
					$jnoc("#myModal").modal("show");
					
					}
					}
				});      
				}
	});		
	
	$jnoc('.tutup').click(function(){
		window.location.href="index.php?halaman=edit_identity_mikrotik";
	});
});

File: /aksi\js\editpass\editpass.js
$jnoc(document).ready(function(){
	$jnoc('#gpass').validate({
				rules: {
					passb: {
						required: true
					}
					},
				messages: {
				    passb: {
						required : "Password Baru Harus diisi"
					}    
				},
				submitHandler: function(form) {
				
				$jnoc("#lproses").show();
				var passb = $jnoc("#passb").val();
				var passl = $jnoc("#passl").val();
				
				$jnoc.ajax({
					url: "aksi/php/editpass/editpass.php", 
					type:"POST",
					data: { aksi:"editpass",passl:passl,passb:passb },
					dataType:"json",
					chache: false,
					success : function(respon){
					if (respon==1){
					$jnoc("#lproses").hide();
					$jnoc('.error-text').text("Password Mikrotik SUKSES diganti");  
					$jnoc("#myModal").modal("show");
					} else if (respon==0) {
					$jnoc("#lproses").hide();
					$jnoc('.error-text').text("Password Mikrotik GAGAL diganti");  
					$jnoc("#myModal").modal("show");
					
					}
					}
				});      
				}
	});		
});

File: /aksi\js\limitasi\hapus.js
$jnoc(document).ready(function(){
    // Hapus
	$jnoc("#hapus").click(function(){
		$jnoc("#lproses").show();
		var id = $jnoc("#idnya").val();
			$jnoc.ajax({
				url: "aksi/php/limitasi/hapus.php",
				type:"POST",						
				data: {aksi:"hapus",idh:id},
				dataType:"json",
				chache: false,
				success : function(respon){
				if (respon==1){
					location.reload();
				} else {
					$jnoc("#lproses").hide();
					$jnoc('.error-text').text("ada kesalahan saat proses hapus. cobalah beberapa saat lagi!"); 
					exit();	
				}
				}
			});
	});
	
	$jnoc(".hapus").click(function(){
		$jnoc("#lproses").hide();
		var isi = $jnoc(this);
		var id = isi.attr("id");
		var nama = isi.attr("svn");
		if (id=="*0"){ 
		$jnoc('.error-text').text("Maaf, group limitasi '"+nama+"' tidak boleh dihapus"); 
		$jnoc("#hapus").hide(); 
		} else { 
		$jnoc('.error-text').text("anda yakin akan menghapus group limitasi '"+nama+"' ini?"); 
		$jnoc("#hapus").show(); 
		}
		$jnoc("#idnya").val(id);  			
		$jnoc("#myModal").modal("show");	
	});
	
});

File: /aksi\js\limitasi\save.js
$jnoc(document).ready(function(){
	$jnoc('#glimitasi').validate({
				rules: {
					nama: {
						required: true
					},
					share: {
						required: true,
						digits:true
					},					
					limit: {
						required: true,
						digits:true
					},
					satuan: {
						required: true
					}
					},
				messages: {
				    nama: {
						required : "Nama Harus diisi"
					},
				    share: {
						required : "Shared User Harus diisi",
						digits : "Shared user harus angka"
					},				    
					limit: {
						required : "Limit Bandwidth Harus diisi",
						digits : "Limit Bandwidth Harus angka misal : 128/256/512"
					},
				    satuan: {
						required : "Satuan Harus dipilih"
					}					
				},
				submitHandler: function(form) {
				
				$jnoc("#lproses").show();
				var share = $jnoc("#share").val();
				var nama = $jnoc("#nama").val();
				var limit = $jnoc("#limit").val();
				var satuan = $jnoc("#satuan").val();
				var aksi = $jnoc("#aksi").val();
				var id = $jnoc("#idnya").val();
				$jnoc.ajax({
					url: "aksi/php/limitasi/save.php", 
					type:"POST",
					data: { aksi:aksi,share:share,nama:nama,limit:limit,satuan:satuan,id:id },
					dataType:"json",
					chache: false,
					success : function(respon){
					if (respon==1){
					$jnoc("#share").val("");
					$jnoc("#nama").val("");
					$jnoc("#satuan").val("-- Pilih --");
					$jnoc("#limit").val("");
					$jnoc("#lproses").hide();
					$jnoc('.error-text').text("Data Group Limitasi Berhasil disimpan.");  
					$jnoc("#myModal").modal("show");
					} else if (respon==0) {
					$jnoc("#lproses").hide();
					$jnoc('.error-text').text("Group Limitasi GAGAL disimpan");  
					$jnoc("#myModal").modal("show");
					
					}
					}
				});      
				}
	});	
});

File: /aksi\js\login\aksi_login.js
$jnoc(document).ready(function(){
	$jnoc('#loginform').validate({
				rules: {
					ip: {
						required: true
					},
					user: {
						required: true
					}
					},
				messages: {
				    ip: {
						required : "IP Address Harus diisi!"
					},
					user: {
						required : "Nama User Harus diisi!"
					}    
				},
				submitHandler: function(form) {
				
				$jnoc("#lproses").show();
				var ip = $jnoc("#ip").val();
				var user = $jnoc("#user").val();
				var pass = $jnoc("#pass").val();
				
				$jnoc.ajax({
					url: "aksi/php/login/aksi_login.php", 
					type:"POST",
					data: { aksi:"login",ip:ip,pass:pass,user:user },
					dataType:"json",
					chache: false,
					success : function(respon){
					if (respon==1){
					$jnoc("#lproses").hide();
					window.location.href="index.php";
					} else if (respon==0) {
					$jnoc("#lproses").hide();
					$jnoc('.error-text').text("Koneksi Ke Mikrotik GAGAL! Periksa Koneksi dengan Router atau Username/Password Mungkin Kurang Tepat!");  
					$jnoc("#myModal").modal("show");
					
					}
					}
				});      
				}
	});		
});

File: /aksi\js\profile\update.js
$jnoc(document).ready(function(){
	$jnoc('#profile').validate({
				rules: {
					nama: {
						required: true
					},
					group: {
						required: true
					},
					ket: {
						required: true
					}
					},
				messages: {
				    nama: {
						required : "Nama Harus diisi"
					},
				    group: {
						required : "Group Harus dipilih"
					},
				    ket: {
						required : "Keterangan Harus diisi"
					}					
				},
				submitHandler: function(form) {
				
				$jnoc("#lproses").show();
				var id = $jnoc("#id").val();
				var nama = $jnoc("#nama").val();
				var group = $jnoc("#group").val();
				var ket = $jnoc("#ket").val();
				
				$jnoc.ajax({
					url: "aksi/php/profile/update.php", 
					type:"POST",
					data: { aksi:"update",id:id,nama:nama,group:group,ket:ket },
					dataType:"json",
					chache: false,
					success : function(respon){
					if (respon==1){
					$jnoc("#lproses").hide();
					$jnoc('.error-text').text("Profile Berhasil diperbarui.");  
					$jnoc("#myModal").modal("show");
					} else if (respon==0) {
					$jnoc("#lproses").hide();
					$jnoc('.error-text').text("Profile GAGAL diperbarui");  
					$jnoc("#myModal").modal("show");
					
					}
					}
				});      
				}
	});		
});

File: /aksi\js\reboot\reboot.js
$jnoc(document).ready(function(){
	$jnoc('#reboot').click(function(){
				$jnoc.ajax({
					url: "aksi/php/reboot/reboot.php", 
					type:"POST",
					data: { aksi:"reboot" },
					dataType:"json",
					chache: false,
					success : function(respon){
					if (respon==1){
					window.location.href="login.php";
					} else if (respon==0) {
					exit();
					}
					}
				});      
			
	});		
});

File: /aksi\js\userhotspot\generate.js
$jnoc(document).ready(function(){
	$jnoc('#guserhotspot').validate({
				rules: {
					puser: {
						required: true
					},
					glimit: {
						required: true
					},					
					ppass: {
						required: true
					},
					lwaktu: {
						required: true,
						digits:true
					},
					satuan: {
						required: true
					},
					juser: {
						required: true
					},
					ket: {
						required: true
					}
					},
				messages: {
				    puser: {
						required : "Panjang Nama User Harus dipilih"
					},
				    glimit: {
						required : "Group Limit Bandwidth Harus dipilih"
					},				    
					ppass: {
						required : "Panjang Password Harus dipilih"
					},					
					lwaktu: {
						required : "Limit Waktu Harus diisi",
						digits : "Limit Waktu Harus angka"
					},
					satuan: {
						required : "Satuan Harus dipilih"
					},
					juser: {
						required : "Jumlah User Harus dipilih"
					},
				    ket: {
						required : "Keterangan Harus diisi"
					}					
				},
				submitHandler: function(form) {
				
				$jnoc("#lproses").show();
				var ppass = $jnoc("#ppass").val();
				var puser = $jnoc("#puser").val();
				var glimit = $jnoc("#glimit").val();
				var lwaktu = $jnoc("#lwaktu").val();
				var satuan = $jnoc("#satuan").val();
				var ket = $jnoc("#ket").val();
				var juser = $jnoc("#juser").val();
				
				$jnoc.ajax({
					url: "aksi/php/userhotspot/generate.php", 
					type:"POST",
					data: { aksi:"generate",satuan:satuan,lwaktu:lwaktu,ppass:ppass,puser:puser,glimit:glimit,ket:ket,juser:juser },
					dataType:"json",
					chache: false,
					success : function(respon){
					if (respon==1){
					$jnoc("#puser").val("-- Pilih --");
					$jnoc("#ppass").val("-- Pilih --");
					$jnoc("#glimit").val("-- Pilih --");
					$jnoc("#juser").val("-- Pilih --");
					$jnoc("#satuan").val("-- Pilih --");
					$jnoc("#ket").val("");
					$jnoc("#lwaktu").val("");
					$jnoc("#lproses").hide();
					$jnoc('.error-text').text("Data User Hotspot Sebanyak "+juser+" Buah Berhasil DIGENERATE.");  
					$jnoc("#myModal").modal("show");
					} else if (respon==0) {
					$jnoc("#lproses").hide();
					$jnoc('.error-text').text("User Hotspot GAGAL digenerate");  
					$jnoc("#myModal").modal("show");
					
					}
					}
				});      
			}
	});	
});

File: /aksi\js\userhotspot\hapus.js
$jnoc(document).ready(function(){
    // Hapus
	$jnoc("#hapus").click(function(){
		$jnoc("#lprosesh").show();
		var id = $jnoc("#idnya").val();
			$jnoc.ajax({
				url: "aksi/php/userhotspot/hapus.php",
				type:"POST",						
				data: {aksi:"hapus",idh:id},
				dataType:"json",
				chache: false,
				success : function(respon){
				if (respon==1){
					location.reload();
				} else {
					$jnoc("#lprosesh").hide();
					$jnoc('.error-text').text("ada kesalahan saat proses hapus. cobalah beberapa saat lagi!"); 
					exit();	
				}
				}
			});
	});
	
	$jnoc(".hapus").click(function(){
		$jnoc("#lprosesh").hide();
		$jnoc("#hapuss").hide();
		$jnoc("#resetc").hide();
		$jnoc("#cc").hide();
		var isi = $jnoc(this);
		var id = isi.attr("id");
		var nama = isi.attr("svn");
		$jnoc('.error-text').text("anda yakin akan menghapus user '"+nama+"' ini?"); 
		$jnoc("#hapus").show(); 
		$jnoc("#idnya").val(id);  			
		$jnoc("#myModal").modal("show");	
	});
	
	$jnoc(".hapussuser").click(function(){
		$jnoc("#lprosesh").hide();
		$jnoc("#hapus").hide();
		$jnoc("#resetc").hide();
		$jnoc("#cc").hide();
		$jnoc('.error-text').text("anda yakin akan menghapus semua data user hotspot? jika data lebih dari 500 Buah akan dilakukan secara bertahap."); 
		$jnoc("#hapuss").show(); 		
		$jnoc("#myModal").modal("show");	
	});
	
	    // Hapus
	$jnoc("#hapuss").click(function(){
		$jnoc("#lprosesh").show();
			$jnoc.ajax({
				url: "aksi/php/userhotspot/hapus.php",
				type:"POST",						
				data: {aksi:"hapussuser"},
				dataType:"json",
				chache: false,
				success : function(respon){
				if (respon==1){
					location.reload();
				} else {
					$jnoc("#lprosesh").hide();
					$jnoc('.error-text').text("ada kesalahan saat proses hapus. cobalah beberapa saat lagi!"); 
					exit();	
				}
				}
			});
	});
	
	// Clear Counter
	$jnoc(".resetc").click(function(){
		$jnoc("#lprosesh").hide();
		$jnoc("#hapus").hide();
		$jnoc("#hapuss").hide();
		$jnoc("#cc").hide();
		$jnoc('.error-text').text("anda yakin akan menghapus counter user hotspot? jika anda menghapus counter, user yg sudah sampai limit waktu dapat login kembali"); 
		$jnoc("#resetc").show(); 		
		$jnoc("#myModal").modal("show");	
	});
	
	$jnoc("#resetc").click(function(){
		$jnoc("#lprosesh").show();
			$jnoc.ajax({
				url: "aksi/php/userhotspot/hapus.php",
				type:"POST",						
				data: {aksi:"resetc"},
				dataType:"json",
				chache: false,
				success : function(respon){
				if (respon==1){
					location.reload();
				} else {
					$jnoc("#lprosesh").hide();
					$jnoc('.error-text').text("ada kesalahan saat proses Reset Counter. cobalah beberapa saat lagi!"); 
					exit();	
				}
				}
			});
	});
	// Cetak PDF 
	$jnoc(".cetak").click(function(){
		$jnoc("#lprosese").show();
			$jnoc.ajax({
				url: "aksi/php/userhotspot/cek_data.php",
				type:"POST",						
				data: {aksi:"export"},
				dataType:"json",
				chache: false,
				success : function(respon){
				if (respon==1){
					var win = window.open('penting/pdf_export.php', '_blank');
					if(win){
					win.focus();
					}else{
					document.getElementById("popup").click();
					}
				} else {
					$jnoc("#lprosese").hide();
					$jnoc("#lprosesh").hide();
					$jnoc("#hapus").hide();
					$jnoc("#hapuss").hide();
					$jnoc("#resetc").hide();
					$jnoc("#cc").hide();
					$jnoc('.error-text').text("ada kesalahan saat proses export. cobalah beberapa saat lagi");  		
					$jnoc("#myModal").modal("show");
				}
				}
			});
	});
	// Export Excel
	$jnoc(".export").click(function(){
		$jnoc("#lprosese").show();
			$jnoc.ajax({
				url: "aksi/php/userhotspot/cek_data.php",
				type:"POST",						
				data: {aksi:"export"},
				dataType:"json",
				chache: false,
				success : function(respon){
				if (respon==1){
					var win = window.open('penting/excel_export.php', '_blank');
					if(win){
					win.focus();
					}else{
					document.getElementById("popup").click();
					}
				} else {
					$jnoc("#lprosese").hide();
					$jnoc("#lprosesh").hide();
					$jnoc("#hapus").hide();
					$jnoc("#hapuss").hide();
					$jnoc("#resetc").hide();
					$jnoc("#cc").hide();
					$jnoc('.error-text').text("ada kesalahan saat proses export. cobalah beberapa saat lagi");  		
					$jnoc("#myModal").modal("show");
				}
				}
			});
	});
	// Clear Counter
	$jnoc(".ccounter").click(function(){
		$jnoc("#lprosesh").hide();
		$jnoc("#hapus").hide();
		$jnoc("#resetc").hide();
		$jnoc("#hapuss").hide();
		var isi = $jnoc(this);
		var id = isi.attr("id");
		var nama = isi.attr("svn");
		$jnoc('.error-text').text("anda yakin akan mereset counter user '"+nama+"' ini? jika anda menghapus counter, user dapat login kembali jika limit waktu telah habis"); 
		$jnoc("#cc").show(); 
		$jnoc("#idc").val(id);  
		$jnoc("#myModal").modal("show");
	});
	
	$jnoc("#cc").click(function(){
		$jnoc("#lprosesh").show();
		    var idh = $jnoc("#idc").val();
			$jnoc.ajax({
				url: "aksi/php/userhotspot/hapus.php",
				type:"POST",						
				data: {aksi:"cc",idh:idh},
				dataType:"json",
				chache: false,
				success : function(respon){
				if (respon==1){
					location.reload();
				} else {
					$jnoc("#lprosesh").hide();
					$jnoc('.error-text').text("ada kesalahan saat proses Reset Counter. cobalah beberapa saat lagi!"); 
					exit();	
				}
				}
			});
	});
});

File: /aksi\js\userhotspot\save.js
$jnoc(document).ready(function(){
	$jnoc('#tuserhotspot').validate({
				rules: {
					user: {
						required: true
					},
					glimit: {
						required: true
					},					
					pass: {
						required: true
					},
				//	lwaktu: {
				//		required: true,
				//		digits:true
				//	},
				//	satuan: {
				//		required: true
				//	},
					ket: {
						required: true
					}
					},
				messages: {
				    user: {
						required : "Nama User Harus diisi"
					},
				    glimit: {
						required : "Group Limit Bandwidth Harus dipilih"
					},				    
					pass: {
						required : "Password Harus diisi"
					},					
				//	lwaktu: {
				//		required : "Limit Waktu Harus diisi",
				//		digits : "Limit Waktu Harus angka"
				//	}
				//	satuan: {
				//		required : "Satuan Harus dipilih"
				//	},
				    ket: {
						required : "Keterangan Harus diisi"
					}					
				},
				submitHandler: function(form) {
				
				$jnoc("#lproses").show();
				var pass = $jnoc("#pass").val();
				var user = $jnoc("#user").val();
				var glimit = $jnoc("#glimit").val();
			//	var lwaktu = $jnoc("#lwaktu").val();
			//	var satuan = $jnoc("#satuan").val();
				var ket = $jnoc("#ket").val();
				var aksi = $jnoc("#aksi").val();
				var id = $jnoc("#idnya").val();
				
				$jnoc.ajax({
					url: "aksi/php/userhotspot/save.php", 
					type:"POST",
					//data: { aksi:aksi,id:id,satuan:satuan,lwaktu:lwaktu,pass:pass,user:user,glimit:glimit,ket:ket },
					data: { aksi:aksi,id:id,pass:pass,user:user,glimit:glimit,ket:ket },
					dataType:"json",
					chache: false,
					success : function(respon){
					if (respon==1){
					$jnoc("#pass").val("");
					$jnoc("#user").val("");
					$jnoc("#glimit").val("-- Pilih --");
				//	$jnoc("#satuan").val("-- Pilih --");
					$jnoc("#ket").val("");
				//	$jnoc("#lwaktu").val("");
					$jnoc("#lproses").hide();
					$jnoc('.error-text').text("Data User Hotspot Berhasil disimpan.");  
					$jnoc("#myModal").modal("show");
					} else if (respon==0) {
					$jnoc("#lproses").hide();
					$jnoc('.error-text').text("User Hotspot GAGAL disimpan");  
					$jnoc("#myModal").modal("show");
					
					}
					}
				});      
				}
	});	
});

File: /aksi\js\usermikrotik\hapus.js
$jnoc(document).ready(function(){
    // Hapus
	$jnoc("#hapus").click(function(){
		$jnoc("#lproses").show();
		var id = $jnoc("#idnya").val();
			$jnoc.ajax({
				url: "aksi/php/usermikrotik/hapus.php",
				type:"POST",						
				data: {aksi:"hapus",idh:id},
				dataType:"json",
				chache: false,
				success : function(respon){
				if (respon==1){
					location.reload();
				} else {
					$jnoc("#lproses").hide();
					$jnoc('.error-text').text("ada kesalahan saat proses hapus. cobalah beberapa saat lagi!"); 
					exit();	
				}
				}
			});
	});
	
	$jnoc(".hapus").click(function(){
		$jnoc("#lproses").hide();
		var isi = $jnoc(this);
		var id = isi.attr("id");
		var nama = isi.attr("svn");
		if (id=="*1"){ 
		$jnoc('.error-text').text("Maaf, user '"+nama+"' tidak boleh dihapus"); 
		$jnoc("#hapus").hide(); 
		} else { 
		$jnoc('.error-text').text("anda yakin akan menghapus user '"+nama+"' ini?"); 
		$jnoc("#hapus").show(); 
		}
		$jnoc("#idnya").val(id);  			
		$jnoc("#myModal").modal("show");	
	});
	
});

File: /aksi\js\usermikrotik\save.js
$jnoc(document).ready(function(){
	$jnoc('#user').validate({
				rules: {
					nama: {
						required: true
					},
					group: {
						required: true
					},					
					pass: {
						required: true
					},
					ket: {
						required: true
					}
					},
				messages: {
				    nama: {
						required : "Nama Harus diisi"
					},
				    group: {
						required : "Group Harus dipilih"
					},				    
					pass: {
						required : "Password Harus diisi"
					},
				    ket: {
						required : "Keterangan Harus diisi"
					}					
				},
				submitHandler: function(form) {
				
				$jnoc("#lproses").show();
				var pass = $jnoc("#pass").val();
				var nama = $jnoc("#nama").val();
				var group = $jnoc("#group").val();
				var ket = $jnoc("#ket").val();
				
				$jnoc.ajax({
					url: "aksi/php/usermikrotik/save.php", 
					type:"POST",
					data: { aksi:"save",pass:pass,nama:nama,group:group,ket:ket },
					dataType:"json",
					chache: false,
					success : function(respon){
					if (respon==1){
					$jnoc("#pass").val("");
					$jnoc("#nama").val("");
					$jnoc("#group").val("-- Pilih --");
					$jnoc("#ket").val("");
					$jnoc("#lproses").hide();
					$jnoc('.error-text').text("Data User Berhasil disimpan.");  
					$jnoc("#myModal").modal("show");
					} else if (respon==0) {
					$jnoc("#lproses").hide();
					$jnoc('.error-text').text("User GAGAL disimpan");  
					$jnoc("#myModal").modal("show");
					
					}
					}
				});      
				}
	});	
});

File: /aksi\php\editiden\editiden.php
<?php
    require_once("../../../penting/koneksi.php");
	
	if ($_POST['aksi']=="editiden"){
	
	$iden = $_POST['iden'];
	
	$API->write("/system/identity/set",false);	
	$API->write("=name=".$iden,true);

	$API->read();
	
	echo "1";
	
	}

?>


File: /aksi\php\editpass\editpass.php
<?php
    require_once("../../../penting/koneksi.php");
	
	if ($_POST['aksi']=="editpass"){
	
	$passl = $_POST['passl'];
	$passb = $_POST['passb'];
	
	$API->write("/password",false);	
	$API->write("=old-password=".$passl,false);	
	$API->write("=new-password=".$passb,false);	
	$API->write("=confirm-new-password=".$passb,true);

	$API->read();
	
	echo "1";
	
	}

?>


File: /aksi\php\limitasi\hapus.php
<?php
    require_once("../../../penting/koneksi.php");
	
	if ($_POST['aksi']=="hapus"){
	
	$id = $_POST['idh'];
	
	$API->write("/ip/hotspot/user/profile/remove",false);	
	$API->write("=.id=".$id,true);

	$API->read();
	
	echo "1";
	
	} 

?>


File: /aksi\php\limitasi\save.php
<?php
    require_once("../../../penting/koneksi.php");
	
	if ($_POST['aksi']=="save"){
	
	$share = $_POST['share'];
	$nama = $_POST['nama'];
	$limit = $_POST['limit'];
	$satuan = $_POST['satuan'];
	$rate = $limit."".$satuan."/".$limit."".$satuan;
	
	$API->write("/ip/hotspot/user/profile/add",false);	
	$API->write("=name=".$nama,false);	
	$API->write("=shared-users=".$share,false);	
	$API->write("=rate-limit=".$rate,true);	

	$API->read();
	
	echo "1";
	
	} else if ($_POST['aksi']=="update"){
	
	$share = $_POST['share'];
	$nama = $_POST['nama'];
	$limit = $_POST['limit'];
	$satuan = $_POST['satuan'];
	$rate = $limit."".$satuan."/".$limit."".$satuan;
	$id = $_POST['id'];
	
	$API->write("/ip/hotspot/user/profile/set",false);	
	$API->write("=name=".$nama,false);	
	$API->write("=shared-users=".$share,false);	
	$API->write("=rate-limit=".$rate,false);		
	$API->write("=.id=".$id,true);

	$API->read();
	
	echo "1";
	
	}

?>


File: /aksi\php\login\aksi_login.php
<?php session_start();
    
	if ($_POST['aksi']=="login"){
	
	include("../../../penting/routeros_api.php");

	$API = new routeros_api();
	 
	$ip = $_POST['ip'];
	$user = $_POST['user'];
	$pass = $_POST['pass'];
 
	if (!$API->connect($ip, $user, $pass)){
		
		echo "0";
		
	} else {	
	$_SESSION['user']=$user;
	$konek = 'koneksi.php';
	$handle = fopen("../../../penting/".$konek, 'w') or die('Tidak Bisa Membuka File '.$konek);
	$data = '
	<?php 
		 include("routeros_api.php");
		 $API = new routeros_api();
		 if (!$API->connect("'.$ip.'","'.$user.'","'.$pass.'")){
			 unset($_SESSION["'.'user'.'"]);
			 header("location:login.php");
		 }
	?>';
	fwrite($handle, $data);
	fclose($handle);	
	
	echo "1";
	
	}
	
	}

?>


File: /aksi\php\profile\update.php
<?php
    require_once("../../../penting/koneksi.php");
	
	if ($_POST['aksi']=="update"){
	
	$id = $_POST['id'];
	$nama = $_POST['nama'];
	$group = $_POST['group'];
	$ket = $_POST['ket'];
	
	$API->write("/user/set",false);	
	$API->write("=name=".$nama,false);	
	$API->write("=group=".$group,false);	
	$API->write("=comment=".$ket,false);	
	$API->write("=.id=".$id,true);

	$API->read();
	
	echo "1";
	
	}

?>


File: /aksi\php\reboot\reboot.php
<?php session_start();

    require_once("../../../penting/koneksi.php");
	
	if ($_POST['aksi']=="reboot"){
	
	$API->write("/system/reboot",true);	

	$API->read();
	
	unset($_SESSION['user']);
	
	echo "1";
	
	}

?>


File: /aksi\php\userhotspot\cek_data.php
<?php
    require_once("../../../penting/koneksi.php");
	
	if ($_POST['aksi']=="export"){
	
	$API->write("/ip/hotspot/user/print");   
	$uh = $API->read();
	
	if (count($uh)>=1){
	
	echo "1";
	
	} else {
		
		echo "0";
	
	}
	
	} 

?>


File: /aksi\php\userhotspot\generate.php
<?php
    require_once("../../../penting/koneksi.php");
	
	$characters = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ';
    $charactersLength = strlen($characters);

    $randomUser = '';
    $randomPass = '';
 
	if ($_POST['aksi']=="generate"){
	
	$ppass = $_POST['ppass'];
	$puser = $_POST['puser'];
	$glimit = $_POST['glimit'];
	$lwaktu = $_POST['lwaktu'];
	$satuan = $_POST['satuan'];
	$ket = $_POST['ket'];
	$juser = $_POST['juser'];
	
	if ($satuan=="menit"){
			
		$uptime ="00:".$lwaktu.":00";
		
	} else if ($satuan=="jam"){
		
		$uptime = $lwaktu.":00:00";
		
	} else if ($satuan=="hari"){
		
		$total = $lwaktu*24;
		
		$uptime = $total.":00:00";
	}
	 
	// Generate User Hotspot Secara Random
	
	// For Jumlah
	for ($j = 0; $j < $juser; $j++) {
  
	   // For Random Username
	   for ($i = 0; $i < $puser; $i++) {
		$randomUser .= $characters[rand(0, $charactersLength - 1)];
	   }
   
	   // For Random Password
	   for ($k = 0; $k < $ppass; $k++) {
		$randomPass .= $characters[rand(0, $charactersLength - 1)];
	   }
  
	  $API->write("/ip/hotspot/user/add",false);	
	  $API->write("=name=".$randomUser,false);	
	  $API->write("=password=".$randomPass,false);	
	  $API->write("=profile=".$glimit,false);	
	  $API->write("=limit-uptime=".$uptime,false);		
	  $API->write("=comment=".$ket,true);	
	  $API->read();
	  
	  $randomUser = '';
	  $randomPass = '';
  
	}
	
	echo "1";
	
	}
?>


File: /aksi\php\userhotspot\hapus.php
<?php
    require_once("../../../penting/koneksi.php");
	
	if ($_POST['aksi']=="hapus"){
	
	$id = $_POST['idh'];
	
	$API->write("/ip/hotspot/user/remove",false);	
	$API->write("=.id=".$id,true);

	$API->read();
	
	echo "1";
	
	} 
	
	if ($_POST['aksi']=="cc"){
	
	$id = $_POST['idh'];
	
	$API->write("/ip/hotspot/user/reset-counters",false);	
	$API->write("=.id=".$id,true);

	$API->read();
	
	echo "1";
	
	} 

	if ($_POST['aksi']=="resetc"){
	
	$API->write("/ip/hotspot/user/reset-counters");	

	$API->read();
	
	echo "1";
	
	}
	
	if ($_POST['aksi']=="hapussuser"){
	
	$API->write("/ip/hotspot/user/print");   
	$uh = $API->read();
	
	if (count($uh)>500){	
        $j=1;	
		foreach($uh as $tampil){
		$API->write("/ip/hotspot/user/remove",false);	
		$API->write("=.id=".$tampil['.id'],true);
		$API->read();
		if ($j == 500){ break; }
		$j++;
		}
		
		echo "1";
		
	} else {
		foreach($uh as $tampil){
		$API->write("/ip/hotspot/user/remove",false);	
		$API->write("=.id=".$tampil['.id'],true);
		$API->read();
		}
		
	   	echo "1";
	}
	
	} 

?>


File: /aksi\php\userhotspot\save.php
<?php
    require_once("../../../penting/koneksi.php");
	
	if ($_POST['aksi']=="save"){
	
	$pass = $_POST['pass'];
	$user = $_POST['user'];
	$glimit = $_POST['glimit'];
	//$lwaktu = $_POST['lwaktu'];
	//$satuan = $_POST['satuan'];
	$ket = $_POST['ket'];
	
//	if ($satuan=="menit"){
			
//		$uptime ="00:".$lwaktu.":00";
		
//	} else if ($satuan=="jam"){
		
//		$uptime = $lwaktu.":00:00";
		
//	} else if ($satuan=="hari"){
		
//		$total = $lwaktu*24;
		
//		$uptime = $total.":00:00";
//	}
	 
	
	$API->write("/ip/hotspot/user/add",false);	
	$API->write("=name=".$user,false);	
	$API->write("=password=".$pass,false);	
	$API->write("=profile=".$glimit,false);	
//	$API->write("=limit-uptime=".$uptime,false);		
	$API->write("=comment=".$ket,true);	

	$API->read();
	
	echo "1";
	
	} else if ($_POST['aksi']=="update"){
	
	$pass = $_POST['pass'];
	$user = $_POST['user'];
	$glimit = $_POST['glimit'];
//	$lwaktu = $_POST['lwaktu'];
//	$satuan = $_POST['satuan'];
	$ket = $_POST['ket'];
	
//	if ($satuan=="menit"){
			
//		$uptime ="00:".$lwaktu.":00";
		
//	} else if ($satuan=="jam"){
		
//		$uptime = $lwaktu.":00:00";
		
//	} else if ($satuan=="hari"){
		
//		$total = $lwaktu*24;
		
//		$uptime = $total.":00:00";
//	}
	
	$id = $_POST['id'];
	
	$API->write("/ip/hotspot/user/set",false);	
	$API->write("=name=".$user,false);	
	$API->write("=password=".$pass,false);	
	$API->write("=profile=".$glimit,false);	
//	$API->write("=limit-uptime=".$uptime,false);		
	$API->write("=comment=".$ket,false);		
	$API->write("=.id=".$id,true);

	$API->read();
	
	echo "1";
	
	}

?>


File: /aksi\php\usermikrotik\hapus.php
<?php
    require_once("../../../penting/koneksi.php");
	
	if ($_POST['aksi']=="hapus"){
	
	$id = $_POST['idh'];
	
	$API->write("/user/remove",false);	
	$API->write("=.id=".$id,true);

	$API->read();
	
	echo "1";
	
	} 

?>


File: /aksi\php\usermikrotik\save.php
<?php
    require_once("../../../penting/koneksi.php");
	
	if ($_POST['aksi']=="save"){
	
	$pass = $_POST['pass'];
	$nama = $_POST['nama'];
	$group = $_POST['group'];
	$ket = $_POST['ket'];
	
	$API->write("/user/add",false);	
	$API->write("=name=".$nama,false);	
	$API->write("=group=".$group,false);	
	$API->write("=comment=".$ket,false);	
	$API->write("=password=".$pass,true);

	$API->read();
	
	echo "1";
	
	} 

?>


File: /css\theme.css
     #container{
	   	background: #f2f2f2;
	   	padding: 20px;
	   }
       
       .page {
        display: inline-block;
        padding: 4px 9px;
        margin-right: 4px;
        margin-bottom: 4px;
        border-radius: 3px;
        border: solid 1px #c0c0c0;
        background: #e9e9e9;
        font-size: 11px;
        text-decoration: none;
        color: #717171;
        text-transform: capitalize;
        }
 
        .page:hover{
          background:#FAF7F7;
        }
 
        .active, .active:hover{
            background: #757272;
            border-color: #403C3C;
            color: #e9e9e9;
            cursor: default;
        }
 
        p{
            font-family: helvetica;
 
        }
		

.load{
	display:none;
}
	.error {
			font-size:small;
			color:red;
	}
		.warna{
		color:#000000;
	}
     #line-chart {
            height:300px;
            width:800px;
            margin: 0px auto;
            margin-top: 1em;
        }
        .brand { font-family: georgia, serif; }
        .brand .first {
            color: #ccc;
            font-style: italic;
        }
        .brand .second {
            color: #fff;
            font-weight: bold;
   }
.block-m {
  margin-bottom: 1em;
  border: 1px solid #ccc;
  background: white;
  -webkit-border-radius: 3px;
  -moz-border-radius: 3px;
  border-radius: 3px;
  -moz-background-clip: padding;
  -webkit-background-clip: padding-box;
  background-clip: padding-box;
  -webkit-box-shadow: 0px 1px 0px #ffffff;
  -moz-box-shadow: 0px 1px 0px #ffffff;
  box-shadow: 0px 1px 0px #ffffff;
}
/*Standard Elements*/
body {
  background: #eee;
  background-image: url(../images/furley_bg.png);
  background-position: initial initial;
  background-repeat: initial initial;
  margin: 0px;
  padding: 0px;
}
a:hover {
  text-decoration: none;
}
h1 {
  margin-top: 0px;
}
h2 {
  font-size: 1.75em;
}
h3 {
  font-size: 1.25em;
}
hr {
  border-top: 1px solid #ddd;
  border-bottom: 1px solid #fff;
}
/*Navbar*/
.navbar {
  margin: 0px 0px 1em 0px;
  padding: 0px;
}
.navbar .brand {
  text-shadow: none;
}
.navbar .nav > li > a {
  color: #fff;
  text-shadow: none;
}
.navbar .nav > li:hover {
  background-color: #444;
}
.navbar .nav > li > a:hover {
  color: #fff;
}
.navbar .navbar-inner {
  background: #555555;
  background: -webkit-gradient(linear, left bottom, left top, color-stop(0, #444444), color-stop(1, #555555));
  background: -ms-linear-gradient(bottom, #444444, #555555);
  background: -moz-linear-gradient(center bottom, #444444 0%, #555555 100%);
  background: -o-linear-gradient(bottom, #444444, #555555);
  filter: none;
  filter: progid:dximagetransform.microsoft.gradient(startColorStr='#444444', EndColorStr='#555555');
  -ms-filter: "progid:DXImageTransform.Microsoft.gradient(startColorStr='#555555',EndColorStr='#444444')";
  margin: 0px;
  -webkit-border-radius: 0px;
  -moz-border-radius: 0px;
  border-radius: 0px;
  -moz-background-clip: padding;
  -webkit-background-clip: padding-box;
  background-clip: padding-box;
  border: 0px;
  border-bottom: 1px solid #222;
  -webkit-box-shadow: 0px 1px 0px #f0f0f0;
  -moz-box-shadow: 0px 1px 0px #f0f0f0;
  box-shadow: 0px 1px 0px #f0f0f0;
}
.navbar .nav li.dropdown.open > .dropdown-toggle {
  background-color: #444;
  color: #fff;
}
footer {
  padding: 1em;
  margin-top: -3em;
  color: #666;
  font-size: .85em;
  line-height: 0.5em;
}
footer hr {
  margin: 2em -2em;
}
/*Quick Toolbar*/
.btn-toolbar.quick-toolbar {
  float: right;
}
.btn-toolbar.quick-toolbar .btn {
  width: 60px;
  height: 60px;
  display: inline-block;
}
.stats .stat {
  margin-left: 1em;
  float: right;
  line-height: 40px;
}
.stats .stat .number {
  font-weight: bold;
  margin-right: .5em;
  padding: .5em;
  border: 1px solid #ccc;
  -webkit-border-radius: 3px;
  -moz-border-radius: 3px;
  border-radius: 3px;
  -moz-background-clip: padding;
  -webkit-background-clip: padding-box;
  background-clip: padding-box;
  background: #eeeeee;
  background: -webkit-gradient(linear, left bottom, left top, color-stop(0, #e0e0e0), color-stop(1, #ffffff));
  background: -ms-linear-gradient(bottom, #e0e0e0, #ffffff);
  background: -moz-linear-gradient(center bottom, #e0e0e0 0%, #ffffff 100%);
  background: -o-linear-gradient(bottom, #e0e0e0, #ffffff);
  filter: none;
  filter: progid:dximagetransform.microsoft.gradient(startColorStr='#444444', EndColorStr='#555555');
  -ms-filter: "progid:DXImageTransform.Microsoft.gradient(startColorStr='#ffffff',EndColorStr='#e0e0e0')";
  -webkit-box-shadow: 1px 1px 0px #ffffff;
  -moz-box-shadow: 1px 1px 0px #ffffff;
  box-shadow: 1px 1px 0px #ffffff;
  text-shadow: 1px 1px 1px #fff;
}
/*Blocks*/
.block {
  margin-bottom: 1em;
  border: 1px solid #ccc;
  background: white;
  -webkit-border-radius: 3px;
  -moz-border-radius: 3px;
  border-radius: 3px;
  -moz-background-clip: padding;
  -webkit-background-clip: padding-box;
  background-clip: padding-box;
  -webkit-box-shadow: 0px 1px 0px #ffffff;
  -moz-box-shadow: 0px 1px 0px #ffffff;
  box-shadow: 0px 1px 0px #ffffff;
}
.block-heading[data-toggle="collapse"] {
  cursor: pointer;
}
.block-heading[data-toggle="collapse"]:hover {
  background: #d0d0d0;
  background: -webkit-gradient(linear, left bottom, left top, color-stop(0, #d0d0d0), color-stop(1, #ffffff));
  background: -ms-linear-gradient(bottom, #d0d0d0, #ffffff);
  background: -moz-linear-gradient(center bottom, #d0d0d0 0%, #ffffff 100%);
  background: -o-linear-gradient(bottom, #d0d0d0, #ffffff);
  filter: none;
  filter: progid:dximagetransform.microsoft.gradient(startColorStr='#444444', EndColorStr='#555555');
  -ms-filter: "progid:DXImageTransform.Microsoft.gradient(startColorStr='#ffffff',EndColorStr='#d0d0d0')";
}
.block-heading {
  display: block;
  font-weight: bold;
  color: #333;
  text-shadow: 1px 1px 1px #fff;
  background: #dddddd;
  background: -webkit-gradient(linear, left bottom, left top, color-stop(0, #dddddd), color-stop(1, #ffffff));
  background: -ms-linear-gradient(bottom, #dddddd, #ffffff);
  background: -moz-linear-gradient(center bottom, #dddddd 0%, #ffffff 100%);
  background: -o-linear-gradient(bottom, #dddddd, #ffffff);
  filter: none;
  filter: progid:dximagetransform.microsoft.gradient(startColorStr='#444444', EndColorStr='#555555');
  -ms-filter: "progid:DXImageTransform.Microsoft.gradient(startColorStr='#ffffff',EndColorStr='#dddddd')";
  -webkit-border-top-right-radius: 3px;
  -webkit-border-bottom-right-radius: 0px;
  -webkit-border-bottom-left-radius: 0px;
  -webkit-border-top-left-radius: 3px;
  -moz-border-radius-topright: 3px;
  -moz-border-radius-bottomright: 0px;
  -moz-border-radius-bottomleft: 0px;
  -moz-border-radius-topleft: 3px;
  border-top-right-radius: 3px;
  border-bottom-right-radius: 0px;
  border-bottom-left-radius: 0px;
  border-top-left-radius: 3px;
  -moz-background-clip: padding;
  -webkit-background-clip: padding-box;
  background-clip: padding-box;
  border-bottom: 1px solid #aaa;
  font-size: 1em;
  line-height: 3em;
  text-transform: none;
  padding: 0em .75em;
  margin-bottom: 0px;
}
.block-heading .label {
  float: right;
  margin-top: 1em;
  line-height: 1.5em;
}
.block-body {
  margin: 1em;
  min-height: .25em;
}
.block-body h1,
.block-body h2,
.block-body h3,
.block-body h4,
.block-body h5,
.block-body h6,
.block-body table {
  margin-top: 12px;
}
.block-body.collapse {
  margin-top: 0em;
  margin-bottom: 0em;
}
/*Navigation*/
.sidebar-nav {
  padding: 0px;
}
.sidebar-nav .nav-header {
  display: block;
  font-weight: bold;
  color: #333;
  text-shadow: 1px 1px 1px #fff;
  background: #dddddd;
  background: -webkit-gradient(linear, left bottom, left top, color-stop(0, #dddddd), color-stop(1, #ffffff));
  background: -ms-linear-gradient(bottom, #dddddd, #ffffff);
  background: -moz-linear-gradient(center bottom, #dddddd 0%, #ffffff 100%);
  background: -o-linear-gradient(bottom, #dddddd, #ffffff);
  filter: none;
  filter: progid:dximagetransform.microsoft.gradient(startColorStr='#444444', EndColorStr='#555555');
  -ms-filter: "progid:DXImageTransform.Microsoft.gradient(startColorStr='#ffffff',EndColorStr='#dddddd')";
  -webkit-border-top-right-radius: 3px;
  -webkit-border-bottom-right-radius: 0px;
  -webkit-border-bottom-left-radius: 0px;
  -webkit-border-top-left-radius: 3px;
  -moz-border-radius-topright: 3px;
  -moz-border-radius-bottomright: 0px;
  -moz-border-radius-bottomleft: 0px;
  -moz-border-radius-topleft: 3px;
  border-top-right-radius: 3px;
  border-bottom-right-radius: 0px;
  border-bottom-left-radius: 0px;
  border-top-left-radius: 3px;
  -moz-background-clip: padding;
  -webkit-background-clip: padding-box;
  background-clip: padding-box;
  border-bottom: 1px solid #aaa;
  font-size: 1em;
  line-height: 3em;
  text-transform: none;
  padding: 0em .75em;
  margin-bottom: 0px;
  cursor: pointer;
  border: 1px solid #ccc;
  border-bottom: 1px solid #aaa;
}
.sidebar-nav .nav-header .label {
  float: right;
  margin-top: 1em;
  line-height: 1.5em;
}
.sidebar-nav .nav-header:hover {
  background: #cecece;
  background: -webkit-gradient(linear, left bottom, left top, color-stop(0, #cecece), color-stop(1, #ffffff));
  background: -ms-linear-gradient(bottom, #cecece, #ffffff);
  background: -moz-linear-gradient(center bottom, #cecece 0%, #ffffff 100%);
  background: -o-linear-gradient(bottom, #cecece, #ffffff);
  filter: none;
  filter: progid:dximagetransform.microsoft.gradient(startColorStr='#444444', EndColorStr='#555555');
  -ms-filter: "progid:DXImageTransform.Microsoft.gradient(startColorStr='#ffffff',EndColorStr='#cecece')";
}
.sidebar-nav .nav-header .label {
  float: right;
  margin-top: 1em;
  line-height: 1.5em;
}
.sidebar-nav .nav-header.collapsed {
  -webkit-border-radius: 3px;
  -moz-border-radius: 3px;
  border-radius: 3px;
  -moz-background-clip: padding;
  -webkit-background-clip: padding-box;
  background-clip: padding-box;
}
.sidebar-nav .nav-header i[class^="icon-"] {
  margin-right: .75em;
}
.sidebar-nav .nav-list {
  margin-bottom: 1em;
  border: 1px solid #ccc;
  background: white;
  -webkit-border-radius: 3px;
  -moz-border-radius: 3px;
  border-radius: 3px;
  -moz-background-clip: padding;
  -webkit-background-clip: padding-box;
  background-clip: padding-box;
  -webkit-box-shadow: 0px 1px 0px #ffffff;
  -moz-box-shadow: 0px 1px 0px #ffffff;
  box-shadow: 0px 1px 0px #ffffff;
  margin: 1em;
  margin: 0px;
  -webkit-border-top-right-radius: 0px;
  -webkit-border-bottom-right-radius: 3px;
  -webkit-border-bottom-left-radius: 3px;
  -webkit-border-top-left-radius: 0px;
  -moz-border-radius-topright: 0px;
  -moz-border-radius-bottomright: 3px;
  -moz-border-radius-bottomleft: 3px;
  -moz-border-radius-topleft: 0px;
  border-top-right-radius: 0px;
  border-bottom-right-radius: 3px;
  border-bottom-left-radius: 3px;
  border-top-left-radius: 0px;
  -moz-background-clip: padding;
  -webkit-background-clip: padding-box;
  background-clip: padding-box;
  border-top: 0px;
}
.sidebar-nav .nav-list h1,
.sidebar-nav .nav-list h2,
.sidebar-nav .nav-list h3,
.sidebar-nav .nav-list h4,
.sidebar-nav .nav-list h5,
.sidebar-nav .nav-list h6,
.sidebar-nav .nav-list table {
  margin-top: 12px;
}
.sidebar-nav .nav-list.collapse {
  margin-top: 0em;
  margin-bottom: 0em;
}
.sidebar-nav .nav-list li:last-child a {
  -webkit-border-top-right-radius: 0px;
  -webkit-border-bottom-right-radius: 3px;
  -webkit-border-bottom-left-radius: 3px;
  -webkit-border-top-left-radius: 0px;
  -moz-border-radius-topright: 0px;
  -moz-border-radius-bottomright: 3px;
  -moz-border-radius-bottomleft: 3px;
  -moz-border-radius-topleft: 0px;
  border-top-right-radius: 0px;
  border-bottom-right-radius: 3px;
  border-bottom-left-radius: 3px;
  border-top-left-radius: 0px;
  -moz-background-clip: padding;
  -webkit-background-clip: padding-box;
  background-clip: padding-box;
}
.sidebar-nav .nav-list.collapse {
  margin-bottom: 1em;
}
.sidebar-nav .nav-list  > li > a:hover {
  border-bottom: 1px solid #ddd;
  border-top: 1px solid #ddd;
}
.sidebar-nav .nav-list  > .active > a,
.sidebar-nav .nav-list  > .active > a:hover {
  background: #1e5995;
  background: #1e5995;
  background: -webkit-gradient(linear, left bottom, left top, color-stop(0, #1e5995), color-stop(1, #2266aa));
  background: -ms-linear-gradient(bottom, #1e5995, #2266aa);
  background: -moz-linear-gradient(center bottom, #1e5995 0%, #2266aa 100%);
  background: -o-linear-gradient(bottom, #1e5995, #2266aa);
  filter: none;
  filter: progid:dximagetransform.microsoft.gradient(startColorStr='#444444', EndColorStr='#555555');
  -ms-filter: "progid:DXImageTransform.Microsoft.gradient(startColorStr='#2266aa',EndColorStr='#1e5995')";
  border-bottom: 1px solid #194c80;
  border-top: 1px solid #194c80;
}
.sidebar-nav .nav-list  > li > a {
  padding: .5em 1em;
  border-top: 1px solid #fff;
  border-bottom: 1px solid #fff;
}
.sidebar-nav .nav-list.collapse {
  border-bottom: 0px;
}
.sidebar-nav .nav-list.collapse.in {
  border-bottom: 1px solid #ccc;
}
.sidebar-nav .nav-list .nav-header:first-child {
  -webkit-border-top-right-radius: 3px;
  -webkit-border-bottom-right-radius: 0px;
  -webkit-border-bottom-left-radius: 0px;
  -webkit-border-top-left-radius: 3px;
  -moz-border-radius-topright: 3px;
  -moz-border-radius-bottomright: 0px;
  -moz-border-radius-bottomleft: 0px;
  -moz-border-radius-topleft: 3px;
  border-top-right-radius: 3px;
  border-bottom-right-radius: 0px;
  border-bottom-left-radius: 0px;
  border-top-left-radius: 3px;
  -moz-background-clip: padding;
  -webkit-background-clip: padding-box;
  background-clip: padding-box;
}
/*Buttons*/
.btn-primary {
  background-color: #113355;
  background-image: -webkit-gradient(linear, 0 0, 0 100%, from(#446688), to(#113355));
  background-image: -webkit-linear-gradient(top, #446688, #113355);
  background-image: -o-linear-gradient(top, #446688, #113355);
  background-image: linear-gradient(to bottom, #446688, #113355);
  background-image: -moz-linear-gradient(top, #446688, #113355);
}
.btn-primary:hover {
  background-color: #113355;
  *background-color: #113355;
}
.btn-danger {
  background-color: #553333;
  background-image: -webkit-gradient(linear, 0 0, 0 100%, from(#886666), to(#553333));
  background-image: -webkit-linear-gradient(top, #886666, #553333);
  background-image: -o-linear-gradient(top, #886666, #553333);
  background-image: linear-gradient(to bottom, #886666, #553333);
  background-image: -moz-linear-gradient(top, #886666, #553333);
}
.btn-danger:hover {
  background-color: #553333;
  *background-color: #553333;
}
.btn-success {
  background-color: #556665;
  background-image: -webkit-gradient(linear, 0 0, 0 100%, from(#88aa88), to(#556665));
  background-image: -webkit-linear-gradient(top, #88aa88, #556665);
  background-image: -o-linear-gradient(top, #88aa88, #556665);
  background-image: linear-gradient(to bottom, #88aa88, #556665);
  background-image: -moz-linear-gradient(top, #88aa88, #556665);
}
.btn-success:hover {
  background-color: #556665;
  *background-color: #556665;
}
.btn-warning {
  background-color: #aaaa55;
  background-image: -webkit-gradient(linear, 0 0, 0 100%, from(#dddd77), to(#aaaa55));
  background-image: -webkit-linear-gradient(top, #dddd77, #aaaa55);
  background-image: -o-linear-gradient(top, #dddd77, #aaaa55);
  background-image: linear-gradient(to bottom, #dddd77, #aaaa55);
  background-image: -moz-linear-gradient(top, #dddd77, #aaaa55);
}
.btn-warning:hover {
  background-color: #aaaa55;
  *background-color: #aaaa55;
}
.navbar .dropdown-menu a:hover {
  background: none;
  color: #000;
}
.well {
  background-color: #fff;
  border: 1px solid #ccc;
  -webkit-box-shadow: 1px 1px 0px #ffffff;
  -moz-box-shadow: 1px 1px 0px #ffffff;
  box-shadow: 1px 1px 0px #ffffff;
}
/*Faq*/
.faq-content ul,
.faq-content ol {
  padding-left: 1em;
}
.faq-content ul .top,
.faq-content ol .top {
  float: right;
  line-height: 1.25em;
  padding: .75em 0em;
}
/*Gallery*/
.gallery {
  text-align: center;
}
.gallery  > img {
  margin: .5em .5em .5em .5em;
}
.img-polaroid {
  -webkit-box-shadow: none;
  -moz-box-shadow: none;
  box-shadow: none;
  border: 1px solid #ddd;
}
.dialog,
.row .dialog,
.row-fluid .dialog,
.row-fluid [class*="span"].dialog:first-child {
  margin: 0px auto;
  margin-top: 5em;
  float: none;
}
.dialog input[type="checkbox"],
.row .dialog input[type="checkbox"],
.row-fluid .dialog input[type="checkbox"],
.row-fluid [class*="span"].dialog:first-child input[type="checkbox"] {
  margin: 0px;
}
.dialog .alert,
.row .dialog .alert,
.row-fluid .dialog .alert,
.row-fluid [class*="span"].dialog:first-child .alert {
  margin-bottom: 1em;
}
.dialog form,
.row .dialog form,
.row-fluid .dialog form,
.row-fluid [class*="span"].dialog:first-child form {
  margin-bottom: 0px;
}
.dialog .remember-me,
.row .dialog .remember-me,
.row-fluid .dialog .remember-me,
.row-fluid [class*="span"].dialog:first-child .remember-me {
  padding: .5em 0em 0em 0em;
}
input[type="text"],
input[type="password"] {
  -webkit-border-radius: 0px;
  -moz-border-radius: 0px;
  border-radius: 0px;
  -moz-background-clip: padding;
  -webkit-background-clip: padding-box;
  background-clip: padding-box;
}
/*Alerts*/
.alert {
  -webkit-border-radius: 0px;
  -moz-border-radius: 0px;
  border-radius: 0px;
  -moz-background-clip: padding;
  -webkit-background-clip: padding-box;
  background-clip: padding-box;
  padding: .25em 1em;
  border: 1px solid #f2e187;
  background: #f7ecb5;
  background: -webkit-gradient(linear, left bottom, left top, color-stop(0, #f7ecb5), color-stop(1, #fcf8e3));
  background: -ms-linear-gradient(bottom, #f7ecb5, #fcf8e3);
  background: -moz-linear-gradient(center bottom, #f7ecb5 0%, #fcf8e3 100%);
  background: -o-linear-gradient(bottom, #f7ecb5, #fcf8e3);
  filter: none;
  filter: progid:dximagetransform.microsoft.gradient(startColorStr='#444444', EndColorStr='#555555');
  -ms-filter: "progid:DXImageTransform.Microsoft.gradient(startColorStr='#fcf8e3',EndColorStr='#f7ecb5')";
}
.alert .close {
  right: -0.25em;
}
.alert.alert-error {
  border: 1px solid #c77070;
  background: #d59595;
  background: -webkit-gradient(linear, left bottom, left top, color-stop(0, #d59595), color-stop(1, #e4b9b9));
  background: -ms-linear-gradient(bottom, #d59595, #e4b9b9);
  background: -moz-linear-gradient(center bottom, #d59595 0%, #e4b9b9 100%);
  background: -o-linear-gradient(bottom, #d59595, #e4b9b9);
  filter: none;
  filter: progid:dximagetransform.microsoft.gradient(startColorStr='#444444', EndColorStr='#555555');
  -ms-filter: "progid:DXImageTransform.Microsoft.gradient(startColorStr='#e4b9b9',EndColorStr='#d59595')";
}
.alert.alert-info {
  border: 1px solid #85c5e5;
  background: #afd9ee;
  background: -webkit-gradient(linear, left bottom, left top, color-stop(0, #afd9ee), color-stop(1, #d9edf7));
  background: -ms-linear-gradient(bottom, #afd9ee, #d9edf7);
  background: -moz-linear-gradient(center bottom, #afd9ee 0%, #d9edf7 100%);
  background: -o-linear-gradient(bottom, #afd9ee, #d9edf7);
  filter: none;
  filter: progid:dximagetransform.microsoft.gradient(startColorStr='#444444', EndColorStr='#555555');
  -ms-filter: "progid:DXImageTransform.Microsoft.gradient(startColorStr='#d9edf7',EndColorStr='#afd9ee')";
}
.alert.alert-success {
  border: 1px solid #a3d48e;
  background: #c1e2b3;
  background: -webkit-gradient(linear, left bottom, left top, color-stop(0, #c1e2b3), color-stop(1, #dff0d8));
  background: -ms-linear-gradient(bottom, #c1e2b3, #dff0d8);
  background: -moz-linear-gradient(center bottom, #c1e2b3 0%, #dff0d8 100%);
  background: -o-linear-gradient(bottom, #c1e2b3, #dff0d8);
  filter: none;
  filter: progid:dximagetransform.microsoft.gradient(startColorStr='#444444', EndColorStr='#555555');
  -ms-filter: "progid:DXImageTransform.Microsoft.gradient(startColorStr='#dff0d8',EndColorStr='#c1e2b3')";
}
/*Error Pages*/
.http-error {
  margin-top: 5em;
  text-align: center;
  color: #444;
}
.http-error h1 {
  font-size: 5em;
  line-height: 1em;
  text-shadow: 1px 1px 0px #fff;
}
.http-error p {
  margin: 0px;
}
.http-error .info {
  font-size: 2em;
  line-height: 1.5em;
  margin-bottom: 1em;
}
.http-error i {
  font-size: 3em;
  line-height: .75em;
  text-shadow: 1px 1px 0px #fff;
}
/*Tabs*/
.nav-tabs  > li {
  margin-left: .5em;
}
.nav-tabs  > li  > a {
  -webkit-border-top-right-radius: 0px;
  -webkit-border-bottom-right-radius: 0;
  -webkit-border-bottom-left-radius: 0;
  -webkit-border-top-left-radius: 0;
  -moz-border-radius-topright: 0px;
  -moz-border-radius-bottomright: 0;
  -moz-border-radius-bottomleft: 0;
  -moz-border-radius-topleft: 0;
  border-top-right-radius: 0px;
  border-bottom-right-radius: 0;
  border-bottom-left-radius: 0;
  border-top-left-radius: 0;
  -moz-background-clip: padding;
  -webkit-background-clip: padding-box;
  background-clip: padding-box;
}
.breadcrumb {
  border: 1px solid #ccc;
  background: #ffffff;
  background: -webkit-gradient(linear, left bottom, left top, color-stop(0, #f0f0f0), color-stop(1, #ffffff));
  background: -ms-linear-gradient(bottom, #f0f0f0, #ffffff);
  background: -moz-linear-gradient(center bottom, #f0f0f0 0%, #ffffff 100%);
  background: -o-linear-gradient(bottom, #f0f0f0, #ffffff);
  filter: none;
  filter: progid:dximagetransform.microsoft.gradient(startColorStr='#444444', EndColorStr='#555555');
  -ms-filter: "progid:DXImageTransform.Microsoft.gradient(startColorStr='#ffffff',EndColorStr='#f0f0f0')";
  -webkit-box-shadow: 1px 1px 0px #ffffff;
  -moz-box-shadow: 1px 1px 0px #ffffff;
  box-shadow: 1px 1px 0px #ffffff;
}
/*Model*/
.modal.small {
  width: 400px;
  margin: -170px 0 0 -200px;
}
.modal .modal-icon {
  vertical-align: middle;
  font-size: 4em;
  float: left;
  margin-right: .25em;
}
.modal:focus {
  outline: none;
}
.modal .modal-header {
  display: block;
  font-weight: bold;
  color: #333;
  text-shadow: 1px 1px 1px #fff;
  background: #dddddd;
  background: -webkit-gradient(linear, left bottom, left top, color-stop(0, #dddddd), color-stop(1, #ffffff));
  background: -ms-linear-gradient(bottom, #dddddd, #ffffff);
  background: -moz-linear-gradient(center bottom, #dddddd 0%, #ffffff 100%);
  background: -o-linear-gradient(bottom, #dddddd, #ffffff);
  filter: none;
  filter: progid:dximagetransform.microsoft.gradient(startColorStr='#444444', EndColorStr='#555555');
  -ms-filter: "progid:DXImageTransform.Microsoft.gradient(startColorStr='#ffffff',EndColorStr='#dddddd')";
  -webkit-border-top-right-radius: 3px;
  -webkit-border-bottom-right-radius: 0px;
  -webkit-border-bottom-left-radius: 0px;
  -webkit-border-top-left-radius: 3px;
  -moz-border-radius-topright: 3px;
  -moz-border-radius-bottomright: 0px;
  -moz-border-radius-bottomleft: 0px;
  -moz-border-radius-topleft: 3px;
  border-top-right-radius: 3px;
  border-bottom-right-radius: 0px;
  border-bottom-left-radius: 0px;
  border-top-left-radius: 3px;
  -moz-background-clip: padding;
  -webkit-background-clip: padding-box;
  background-clip: padding-box;
  border-bottom: 1px solid #aaa;
  font-size: 1em;
  line-height: 3em;
  text-transform: none;
  padding: 0em .75em;
  margin-bottom: 0px;
}
.modal .modal-header .label {
  float: right;
  margin-top: 1em;
  line-height: 1.5em;
}
.modal .modal-header h3 {
  font-size: .95em;
}
.modal .modal-footer {
  padding: .5em;
}
.modal .modal-body {
  padding: 2em;
}
.modal p {
  margin: 0em;
  line-height: 1.5em;
}
/*Search*/
.well.search-well {
  text-align: center;
}
.well.search-well form {
  margin-bottom: 0px;
}
.well.search-well label {
  margin-bottom: 0px;
  vertical-align: middle;
}
/*Table of Contents*/
.well.toc h3 {
  font-size: 1em;
  margin-top: 0em;
  padding-top: 0em;
  line-height: 1.4em;
}
.well.toc h4 {
  color: #555;
  font-size: 1em;
  margin-top: 0em;
  padding-top: 0em;
  line-height: 1.4em;
  margin-bottom: 0em;
  padding-bottom: 0em;
}
/* Tweaks for mobile */
@media (max-width: 480px) {
  h1 {
    text-align: center;
  }
  .stats {
    text-align: center;
  }
  .stats .stat {
    float: none;
    display: inline;
  }
}


File: /fpdf\font\courier.php
<?php
$type = 'Core';
$name = 'Courier';
$up = -100;
$ut = 50;
for($i=0;$i<=255;$i++)
	$cw[chr($i)] = 600;
?>


File: /fpdf\font\courierb.php
<?php
$type = 'Core';
$name = 'Courier-Bold';
$up = -100;
$ut = 50;
for($i=0;$i<=255;$i++)
	$cw[chr($i)] = 600;
?>


File: /fpdf\font\courierbi.php
<?php
$type = 'Core';
$name = 'Courier-BoldOblique';
$up = -100;
$ut = 50;
for($i=0;$i<=255;$i++)
	$cw[chr($i)] = 600;
?>


File: /fpdf\font\courieri.php
<?php
$type = 'Core';
$name = 'Courier-Oblique';
$up = -100;
$ut = 50;
for($i=0;$i<=255;$i++)
	$cw[chr($i)] = 600;
?>


File: /fpdf\font\helvetica.php
<?php
$type = 'Core';
$name = 'Helvetica';
$up = -100;
$ut = 50;
$cw = array(
	chr(0)=>278,chr(1)=>278,chr(2)=>278,chr(3)=>278,chr(4)=>278,chr(5)=>278,chr(6)=>278,chr(7)=>278,chr(8)=>278,chr(9)=>278,chr(10)=>278,chr(11)=>278,chr(12)=>278,chr(13)=>278,chr(14)=>278,chr(15)=>278,chr(16)=>278,chr(17)=>278,chr(18)=>278,chr(19)=>278,chr(20)=>278,chr(21)=>278,
	chr(22)=>278,chr(23)=>278,chr(24)=>278,chr(25)=>278,chr(26)=>278,chr(27)=>278,chr(28)=>278,chr(29)=>278,chr(30)=>278,chr(31)=>278,' '=>278,'!'=>278,'"'=>355,'#'=>556,'$'=>556,'%'=>889,'&'=>667,'\''=>191,'('=>333,')'=>333,'*'=>389,'+'=>584,
	','=>278,'-'=>333,'.'=>278,'/'=>278,'0'=>556,'1'=>556,'2'=>556,'3'=>556,'4'=>556,'5'=>556,'6'=>556,'7'=>556,'8'=>556,'9'=>556,':'=>278,';'=>278,'<'=>584,'='=>584,'>'=>584,'?'=>556,'@'=>1015,'A'=>667,
	'B'=>667,'C'=>722,'D'=>722,'E'=>667,'F'=>611,'G'=>778,'H'=>722,'I'=>278,'J'=>500,'K'=>667,'L'=>556,'M'=>833,'N'=>722,'O'=>778,'P'=>667,'Q'=>778,'R'=>722,'S'=>667,'T'=>611,'U'=>722,'V'=>667,'W'=>944,
	'X'=>667,'Y'=>667,'Z'=>611,'['=>278,'\\'=>278,']'=>278,'^'=>469,'_'=>556,'`'=>333,'a'=>556,'b'=>556,'c'=>500,'d'=>556,'e'=>556,'f'=>278,'g'=>556,'h'=>556,'i'=>222,'j'=>222,'k'=>500,'l'=>222,'m'=>833,
	'n'=>556,'o'=>556,'p'=>556,'q'=>556,'r'=>333,'s'=>500,'t'=>278,'u'=>556,'v'=>500,'w'=>722,'x'=>500,'y'=>500,'z'=>500,'{'=>334,'|'=>260,'}'=>334,'~'=>584,chr(127)=>350,chr(128)=>556,chr(129)=>350,chr(130)=>222,chr(131)=>556,
	chr(132)=>333,chr(133)=>1000,chr(134)=>556,chr(135)=>556,chr(136)=>333,chr(137)=>1000,chr(138)=>667,chr(139)=>333,chr(140)=>1000,chr(141)=>350,chr(142)=>611,chr(143)=>350,chr(144)=>350,chr(145)=>222,chr(146)=>222,chr(147)=>333,chr(148)=>333,chr(149)=>350,chr(150)=>556,chr(151)=>1000,chr(152)=>333,chr(153)=>1000,
	chr(154)=>500,chr(155)=>333,chr(156)=>944,chr(157)=>350,chr(158)=>500,chr(159)=>667,chr(160)=>278,chr(161)=>333,chr(162)=>556,chr(163)=>556,chr(164)=>556,chr(165)=>556,chr(166)=>260,chr(167)=>556,chr(168)=>333,chr(169)=>737,chr(170)=>370,chr(171)=>556,chr(172)=>584,chr(173)=>333,chr(174)=>737,chr(175)=>333,
	chr(176)=>400,chr(177)=>584,chr(178)=>333,chr(179)=>333,chr(180)=>333,chr(181)=>556,chr(182)=>537,chr(183)=>278,chr(184)=>333,chr(185)=>333,chr(186)=>365,chr(187)=>556,chr(188)=>834,chr(189)=>834,chr(190)=>834,chr(191)=>611,chr(192)=>667,chr(193)=>667,chr(194)=>667,chr(195)=>667,chr(196)=>667,chr(197)=>667,
	chr(198)=>1000,chr(199)=>722,chr(200)=>667,chr(201)=>667,chr(202)=>667,chr(203)=>667,chr(204)=>278,chr(205)=>278,chr(206)=>278,chr(207)=>278,chr(208)=>722,chr(209)=>722,chr(210)=>778,chr(211)=>778,chr(212)=>778,chr(213)=>778,chr(214)=>778,chr(215)=>584,chr(216)=>778,chr(217)=>722,chr(218)=>722,chr(219)=>722,
	chr(220)=>722,chr(221)=>667,chr(222)=>667,chr(223)=>611,chr(224)=>556,chr(225)=>556,chr(226)=>556,chr(227)=>556,chr(228)=>556,chr(229)=>556,chr(230)=>889,chr(231)=>500,chr(232)=>556,chr(233)=>556,chr(234)=>556,chr(235)=>556,chr(236)=>278,chr(237)=>278,chr(238)=>278,chr(239)=>278,chr(240)=>556,chr(241)=>556,
	chr(242)=>556,chr(243)=>556,chr(244)=>556,chr(245)=>556,chr(246)=>556,chr(247)=>584,chr(248)=>611,chr(249)=>556,chr(250)=>556,chr(251)=>556,chr(252)=>556,chr(253)=>500,chr(254)=>556,chr(255)=>500);
?>


File: /fpdf\font\helveticab.php
<?php
$type = 'Core';
$name = 'Helvetica-Bold';
$up = -100;
$ut = 50;
$cw = array(
	chr(0)=>278,chr(1)=>278,chr(2)=>278,chr(3)=>278,chr(4)=>278,chr(5)=>278,chr(6)=>278,chr(7)=>278,chr(8)=>278,chr(9)=>278,chr(10)=>278,chr(11)=>278,chr(12)=>278,chr(13)=>278,chr(14)=>278,chr(15)=>278,chr(16)=>278,chr(17)=>278,chr(18)=>278,chr(19)=>278,chr(20)=>278,chr(21)=>278,
	chr(22)=>278,chr(23)=>278,chr(24)=>278,chr(25)=>278,chr(26)=>278,chr(27)=>278,chr(28)=>278,chr(29)=>278,chr(30)=>278,chr(31)=>278,' '=>278,'!'=>333,'"'=>474,'#'=>556,'$'=>556,'%'=>889,'&'=>722,'\''=>238,'('=>333,')'=>333,'*'=>389,'+'=>584,
	','=>278,'-'=>333,'.'=>278,'/'=>278,'0'=>556,'1'=>556,'2'=>556,'3'=>556,'4'=>556,'5'=>556,'6'=>556,'7'=>556,'8'=>556,'9'=>556,':'=>333,';'=>333,'<'=>584,'='=>584,'>'=>584,'?'=>611,'@'=>975,'A'=>722,
	'B'=>722,'C'=>722,'D'=>722,'E'=>667,'F'=>611,'G'=>778,'H'=>722,'I'=>278,'J'=>556,'K'=>722,'L'=>611,'M'=>833,'N'=>722,'O'=>778,'P'=>667,'Q'=>778,'R'=>722,'S'=>667,'T'=>611,'U'=>722,'V'=>667,'W'=>944,
	'X'=>667,'Y'=>667,'Z'=>611,'['=>333,'\\'=>278,']'=>333,'^'=>584,'_'=>556,'`'=>333,'a'=>556,'b'=>611,'c'=>556,'d'=>611,'e'=>556,'f'=>333,'g'=>611,'h'=>611,'i'=>278,'j'=>278,'k'=>556,'l'=>278,'m'=>889,
	'n'=>611,'o'=>611,'p'=>611,'q'=>611,'r'=>389,'s'=>556,'t'=>333,'u'=>611,'v'=>556,'w'=>778,'x'=>556,'y'=>556,'z'=>500,'{'=>389,'|'=>280,'}'=>389,'~'=>584,chr(127)=>350,chr(128)=>556,chr(129)=>350,chr(130)=>278,chr(131)=>556,
	chr(132)=>500,chr(133)=>1000,chr(134)=>556,chr(135)=>556,chr(136)=>333,chr(137)=>1000,chr(138)=>667,chr(139)=>333,chr(140)=>1000,chr(141)=>350,chr(142)=>611,chr(143)=>350,chr(144)=>350,chr(145)=>278,chr(146)=>278,chr(147)=>500,chr(148)=>500,chr(149)=>350,chr(150)=>556,chr(151)=>1000,chr(152)=>333,chr(153)=>1000,
	chr(154)=>556,chr(155)=>333,chr(156)=>944,chr(157)=>350,chr(158)=>500,chr(159)=>667,chr(160)=>278,chr(161)=>333,chr(162)=>556,chr(163)=>556,chr(164)=>556,chr(165)=>556,chr(166)=>280,chr(167)=>556,chr(168)=>333,chr(169)=>737,chr(170)=>370,chr(171)=>556,chr(172)=>584,chr(173)=>333,chr(174)=>737,chr(175)=>333,
	chr(176)=>400,chr(177)=>584,chr(178)=>333,chr(179)=>333,chr(180)=>333,chr(181)=>611,chr(182)=>556,chr(183)=>278,chr(184)=>333,chr(185)=>333,chr(186)=>365,chr(187)=>556,chr(188)=>834,chr(189)=>834,chr(190)=>834,chr(191)=>611,chr(192)=>722,chr(193)=>722,chr(194)=>722,chr(195)=>722,chr(196)=>722,chr(197)=>722,
	chr(198)=>1000,chr(199)=>722,chr(200)=>667,chr(201)=>667,chr(202)=>667,chr(203)=>667,chr(204)=>278,chr(205)=>278,chr(206)=>278,chr(207)=>278,chr(208)=>722,chr(209)=>722,chr(210)=>778,chr(211)=>778,chr(212)=>778,chr(213)=>778,chr(214)=>778,chr(215)=>584,chr(216)=>778,chr(217)=>722,chr(218)=>722,chr(219)=>722,
	chr(220)=>722,chr(221)=>667,chr(222)=>667,chr(223)=>611,chr(224)=>556,chr(225)=>556,chr(226)=>556,chr(227)=>556,chr(228)=>556,chr(229)=>556,chr(230)=>889,chr(231)=>556,chr(232)=>556,chr(233)=>556,chr(234)=>556,chr(235)=>556,chr(236)=>278,chr(237)=>278,chr(238)=>278,chr(239)=>278,chr(240)=>611,chr(241)=>611,
	chr(242)=>611,chr(243)=>611,chr(244)=>611,chr(245)=>611,chr(246)=>611,chr(247)=>584,chr(248)=>611,chr(249)=>611,chr(250)=>611,chr(251)=>611,chr(252)=>611,chr(253)=>556,chr(254)=>611,chr(255)=>556);
?>


File: /fpdf\font\helveticabi.php
<?php
$type = 'Core';
$name = 'Helvetica-BoldOblique';
$up = -100;
$ut = 50;
$cw = array(
	chr(0)=>278,chr(1)=>278,chr(2)=>278,chr(3)=>278,chr(4)=>278,chr(5)=>278,chr(6)=>278,chr(7)=>278,chr(8)=>278,chr(9)=>278,chr(10)=>278,chr(11)=>278,chr(12)=>278,chr(13)=>278,chr(14)=>278,chr(15)=>278,chr(16)=>278,chr(17)=>278,chr(18)=>278,chr(19)=>278,chr(20)=>278,chr(21)=>278,
	chr(22)=>278,chr(23)=>278,chr(24)=>278,chr(25)=>278,chr(26)=>278,chr(27)=>278,chr(28)=>278,chr(29)=>278,chr(30)=>278,chr(31)=>278,' '=>278,'!'=>333,'"'=>474,'#'=>556,'$'=>556,'%'=>889,'&'=>722,'\''=>238,'('=>333,')'=>333,'*'=>389,'+'=>584,
	','=>278,'-'=>333,'.'=>278,'/'=>278,'0'=>556,'1'=>556,'2'=>556,'3'=>556,'4'=>556,'5'=>556,'6'=>556,'7'=>556,'8'=>556,'9'=>556,':'=>333,';'=>333,'<'=>584,'='=>584,'>'=>584,'?'=>611,'@'=>975,'A'=>722,
	'B'=>722,'C'=>722,'D'=>722,'E'=>667,'F'=>611,'G'=>778,'H'=>722,'I'=>278,'J'=>556,'K'=>722,'L'=>611,'M'=>833,'N'=>722,'O'=>778,'P'=>667,'Q'=>778,'R'=>722,'S'=>667,'T'=>611,'U'=>722,'V'=>667,'W'=>944,
	'X'=>667,'Y'=>667,'Z'=>611,'['=>333,'\\'=>278,']'=>333,'^'=>584,'_'=>556,'`'=>333,'a'=>556,'b'=>611,'c'=>556,'d'=>611,'e'=>556,'f'=>333,'g'=>611,'h'=>611,'i'=>278,'j'=>278,'k'=>556,'l'=>278,'m'=>889,
	'n'=>611,'o'=>611,'p'=>611,'q'=>611,'r'=>389,'s'=>556,'t'=>333,'u'=>611,'v'=>556,'w'=>778,'x'=>556,'y'=>556,'z'=>500,'{'=>389,'|'=>280,'}'=>389,'~'=>584,chr(127)=>350,chr(128)=>556,chr(129)=>350,chr(130)=>278,chr(131)=>556,
	chr(132)=>500,chr(133)=>1000,chr(134)=>556,chr(135)=>556,chr(136)=>333,chr(137)=>1000,chr(138)=>667,chr(139)=>333,chr(140)=>1000,chr(141)=>350,chr(142)=>611,chr(143)=>350,chr(144)=>350,chr(145)=>278,chr(146)=>278,chr(147)=>500,chr(148)=>500,chr(149)=>350,chr(150)=>556,chr(151)=>1000,chr(152)=>333,chr(153)=>1000,
	chr(154)=>556,chr(155)=>333,chr(156)=>944,chr(157)=>350,chr(158)=>500,chr(159)=>667,chr(160)=>278,chr(161)=>333,chr(162)=>556,chr(163)=>556,chr(164)=>556,chr(165)=>556,chr(166)=>280,chr(167)=>556,chr(168)=>333,chr(169)=>737,chr(170)=>370,chr(171)=>556,chr(172)=>584,chr(173)=>333,chr(174)=>737,chr(175)=>333,
	chr(176)=>400,chr(177)=>584,chr(178)=>333,chr(179)=>333,chr(180)=>333,chr(181)=>611,chr(182)=>556,chr(183)=>278,chr(184)=>333,chr(185)=>333,chr(186)=>365,chr(187)=>556,chr(188)=>834,chr(189)=>834,chr(190)=>834,chr(191)=>611,chr(192)=>722,chr(193)=>722,chr(194)=>722,chr(195)=>722,chr(196)=>722,chr(197)=>722,
	chr(198)=>1000,chr(199)=>722,chr(200)=>667,chr(201)=>667,chr(202)=>667,chr(203)=>667,chr(204)=>278,chr(205)=>278,chr(206)=>278,chr(207)=>278,chr(208)=>722,chr(209)=>722,chr(210)=>778,chr(211)=>778,chr(212)=>778,chr(213)=>778,chr(214)=>778,chr(215)=>584,chr(216)=>778,chr(217)=>722,chr(218)=>722,chr(219)=>722,
	chr(220)=>722,chr(221)=>667,chr(222)=>667,chr(223)=>611,chr(224)=>556,chr(225)=>556,chr(226)=>556,chr(227)=>556,chr(228)=>556,chr(229)=>556,chr(230)=>889,chr(231)=>556,chr(232)=>556,chr(233)=>556,chr(234)=>556,chr(235)=>556,chr(236)=>278,chr(237)=>278,chr(238)=>278,chr(239)=>278,chr(240)=>611,chr(241)=>611,
	chr(242)=>611,chr(243)=>611,chr(244)=>611,chr(245)=>611,chr(246)=>611,chr(247)=>584,chr(248)=>611,chr(249)=>611,chr(250)=>611,chr(251)=>611,chr(252)=>611,chr(253)=>556,chr(254)=>611,chr(255)=>556);
?>


File: /fpdf\font\helveticai.php
<?php
$type = 'Core';
$name = 'Helvetica-Oblique';
$up = -100;
$ut = 50;
$cw = array(
	chr(0)=>278,chr(1)=>278,chr(2)=>278,chr(3)=>278,chr(4)=>278,chr(5)=>278,chr(6)=>278,chr(7)=>278,chr(8)=>278,chr(9)=>278,chr(10)=>278,chr(11)=>278,chr(12)=>278,chr(13)=>278,chr(14)=>278,chr(15)=>278,chr(16)=>278,chr(17)=>278,chr(18)=>278,chr(19)=>278,chr(20)=>278,chr(21)=>278,
	chr(22)=>278,chr(23)=>278,chr(24)=>278,chr(25)=>278,chr(26)=>278,chr(27)=>278,chr(28)=>278,chr(29)=>278,chr(30)=>278,chr(31)=>278,' '=>278,'!'=>278,'"'=>355,'#'=>556,'$'=>556,'%'=>889,'&'=>667,'\''=>191,'('=>333,')'=>333,'*'=>389,'+'=>584,
	','=>278,'-'=>333,'.'=>278,'/'=>278,'0'=>556,'1'=>556,'2'=>556,'3'=>556,'4'=>556,'5'=>556,'6'=>556,'7'=>556,'8'=>556,'9'=>556,':'=>278,';'=>278,'<'=>584,'='=>584,'>'=>584,'?'=>556,'@'=>1015,'A'=>667,
	'B'=>667,'C'=>722,'D'=>722,'E'=>667,'F'=>611,'G'=>778,'H'=>722,'I'=>278,'J'=>500,'K'=>667,'L'=>556,'M'=>833,'N'=>722,'O'=>778,'P'=>667,'Q'=>778,'R'=>722,'S'=>667,'T'=>611,'U'=>722,'V'=>667,'W'=>944,
	'X'=>667,'Y'=>667,'Z'=>611,'['=>278,'\\'=>278,']'=>278,'^'=>469,'_'=>556,'`'=>333,'a'=>556,'b'=>556,'c'=>500,'d'=>556,'e'=>556,'f'=>278,'g'=>556,'h'=>556,'i'=>222,'j'=>222,'k'=>500,'l'=>222,'m'=>833,
	'n'=>556,'o'=>556,'p'=>556,'q'=>556,'r'=>333,'s'=>500,'t'=>278,'u'=>556,'v'=>500,'w'=>722,'x'=>500,'y'=>500,'z'=>500,'{'=>334,'|'=>260,'}'=>334,'~'=>584,chr(127)=>350,chr(128)=>556,chr(129)=>350,chr(130)=>222,chr(131)=>556,
	chr(132)=>333,chr(133)=>1000,chr(134)=>556,chr(135)=>556,chr(136)=>333,chr(137)=>1000,chr(138)=>667,chr(139)=>333,chr(140)=>1000,chr(141)=>350,chr(142)=>611,chr(143)=>350,chr(144)=>350,chr(145)=>222,chr(146)=>222,chr(147)=>333,chr(148)=>333,chr(149)=>350,chr(150)=>556,chr(151)=>1000,chr(152)=>333,chr(153)=>1000,
	chr(154)=>500,chr(155)=>333,chr(156)=>944,chr(157)=>350,chr(158)=>500,chr(159)=>667,chr(160)=>278,chr(161)=>333,chr(162)=>556,chr(163)=>556,chr(164)=>556,chr(165)=>556,chr(166)=>260,chr(167)=>556,chr(168)=>333,chr(169)=>737,chr(170)=>370,chr(171)=>556,chr(172)=>584,chr(173)=>333,chr(174)=>737,chr(175)=>333,
	chr(176)=>400,chr(177)=>584,chr(178)=>333,chr(179)=>333,chr(180)=>333,chr(181)=>556,chr(182)=>537,chr(183)=>278,chr(184)=>333,chr(185)=>333,chr(186)=>365,chr(187)=>556,chr(188)=>834,chr(189)=>834,chr(190)=>834,chr(191)=>611,chr(192)=>667,chr(193)=>667,chr(194)=>667,chr(195)=>667,chr(196)=>667,chr(197)=>667,
	chr(198)=>1000,chr(199)=>722,chr(200)=>667,chr(201)=>667,chr(202)=>667,chr(203)=>667,chr(204)=>278,chr(205)=>278,chr(206)=>278,chr(207)=>278,chr(208)=>722,chr(209)=>722,chr(210)=>778,chr(211)=>778,chr(212)=>778,chr(213)=>778,chr(214)=>778,chr(215)=>584,chr(216)=>778,chr(217)=>722,chr(218)=>722,chr(219)=>722,
	chr(220)=>722,chr(221)=>667,chr(222)=>667,chr(223)=>611,chr(224)=>556,chr(225)=>556,chr(226)=>556,chr(227)=>556,chr(228)=>556,chr(229)=>556,chr(230)=>889,chr(231)=>500,chr(232)=>556,chr(233)=>556,chr(234)=>556,chr(235)=>556,chr(236)=>278,chr(237)=>278,chr(238)=>278,chr(239)=>278,chr(240)=>556,chr(241)=>556,
	chr(242)=>556,chr(243)=>556,chr(244)=>556,chr(245)=>556,chr(246)=>556,chr(247)=>584,chr(248)=>611,chr(249)=>556,chr(250)=>556,chr(251)=>556,chr(252)=>556,chr(253)=>500,chr(254)=>556,chr(255)=>500);
?>


File: /fpdf\font\symbol.php
<?php
$type = 'Core';
$name = 'Symbol';
$up = -100;
$ut = 50;
$cw = array(
	chr(0)=>250,chr(1)=>250,chr(2)=>250,chr(3)=>250,chr(4)=>250,chr(5)=>250,chr(6)=>250,chr(7)=>250,chr(8)=>250,chr(9)=>250,chr(10)=>250,chr(11)=>250,chr(12)=>250,chr(13)=>250,chr(14)=>250,chr(15)=>250,chr(16)=>250,chr(17)=>250,chr(18)=>250,chr(19)=>250,chr(20)=>250,chr(21)=>250,
	chr(22)=>250,chr(23)=>250,chr(24)=>250,chr(25)=>250,chr(26)=>250,chr(27)=>250,chr(28)=>250,chr(29)=>250,chr(30)=>250,chr(31)=>250,' '=>250,'!'=>333,'"'=>713,'#'=>500,'$'=>549,'%'=>833,'&'=>778,'\''=>439,'('=>333,')'=>333,'*'=>500,'+'=>549,
	','=>250,'-'=>549,'.'=>250,'/'=>278,'0'=>500,'1'=>500,'2'=>500,'3'=>500,'4'=>500,'5'=>500,'6'=>500,'7'=>500,'8'=>500,'9'=>500,':'=>278,';'=>278,'<'=>549,'='=>549,'>'=>549,'?'=>444,'@'=>549,'A'=>722,
	'B'=>667,'C'=>722,'D'=>612,'E'=>611,'F'=>763,'G'=>603,'H'=>722,'I'=>333,'J'=>631,'K'=>722,'L'=>686,'M'=>889,'N'=>722,'O'=>722,'P'=>768,'Q'=>741,'R'=>556,'S'=>592,'T'=>611,'U'=>690,'V'=>439,'W'=>768,
	'X'=>645,'Y'=>795,'Z'=>611,'['=>333,'\\'=>863,']'=>333,'^'=>658,'_'=>500,'`'=>500,'a'=>631,'b'=>549,'c'=>549,'d'=>494,'e'=>439,'f'=>521,'g'=>411,'h'=>603,'i'=>329,'j'=>603,'k'=>549,'l'=>549,'m'=>576,
	'n'=>521,'o'=>549,'p'=>549,'q'=>521,'r'=>549,'s'=>603,'t'=>439,'u'=>576,'v'=>713,'w'=>686,'x'=>493,'y'=>686,'z'=>494,'{'=>480,'|'=>200,'}'=>480,'~'=>549,chr(127)=>0,chr(128)=>0,chr(129)=>0,chr(130)=>0,chr(131)=>0,
	chr(132)=>0,chr(133)=>0,chr(134)=>0,chr(135)=>0,chr(136)=>0,chr(137)=>0,chr(138)=>0,chr(139)=>0,chr(140)=>0,chr(141)=>0,chr(142)=>0,chr(143)=>0,chr(144)=>0,chr(145)=>0,chr(146)=>0,chr(147)=>0,chr(148)=>0,chr(149)=>0,chr(150)=>0,chr(151)=>0,chr(152)=>0,chr(153)=>0,
	chr(154)=>0,chr(155)=>0,chr(156)=>0,chr(157)=>0,chr(158)=>0,chr(159)=>0,chr(160)=>750,chr(161)=>620,chr(162)=>247,chr(163)=>549,chr(164)=>167,chr(165)=>713,chr(166)=>500,chr(167)=>753,chr(168)=>753,chr(169)=>753,chr(170)=>753,chr(171)=>1042,chr(172)=>987,chr(173)=>603,chr(174)=>987,chr(175)=>603,
	chr(176)=>400,chr(177)=>549,chr(178)=>411,chr(179)=>549,chr(180)=>549,chr(181)=>713,chr(182)=>494,chr(183)=>460,chr(184)=>549,chr(185)=>549,chr(186)=>549,chr(187)=>549,chr(188)=>1000,chr(189)=>603,chr(190)=>1000,chr(191)=>658,chr(192)=>823,chr(193)=>686,chr(194)=>795,chr(195)=>987,chr(196)=>768,chr(197)=>768,
	chr(198)=>823,chr(199)=>768,chr(200)=>768,chr(201)=>713,chr(202)=>713,chr(203)=>713,chr(204)=>713,chr(205)=>713,chr(206)=>713,chr(207)=>713,chr(208)=>768,chr(209)=>713,chr(210)=>790,chr(211)=>790,chr(212)=>890,chr(213)=>823,chr(214)=>549,chr(215)=>250,chr(216)=>713,chr(217)=>603,chr(218)=>603,chr(219)=>1042,
	chr(220)=>987,chr(221)=>603,chr(222)=>987,chr(223)=>603,chr(224)=>494,chr(225)=>329,chr(226)=>790,chr(227)=>790,chr(228)=>786,chr(229)=>713,chr(230)=>384,chr(231)=>384,chr(232)=>384,chr(233)=>384,chr(234)=>384,chr(235)=>384,chr(236)=>494,chr(237)=>494,chr(238)=>494,chr(239)=>494,chr(240)=>0,chr(241)=>329,
	chr(242)=>274,chr(243)=>686,chr(244)=>686,chr(245)=>686,chr(246)=>384,chr(247)=>384,chr(248)=>384,chr(249)=>384,chr(250)=>384,chr(251)=>384,chr(252)=>494,chr(253)=>494,chr(254)=>494,chr(255)=>0);
?>


File: /fpdf\font\times.php
<?php
$type = 'Core';
$name = 'Times-Roman';
$up = -100;
$ut = 50;
$cw = array(
	chr(0)=>250,chr(1)=>250,chr(2)=>250,chr(3)=>250,chr(4)=>250,chr(5)=>250,chr(6)=>250,chr(7)=>250,chr(8)=>250,chr(9)=>250,chr(10)=>250,chr(11)=>250,chr(12)=>250,chr(13)=>250,chr(14)=>250,chr(15)=>250,chr(16)=>250,chr(17)=>250,chr(18)=>250,chr(19)=>250,chr(20)=>250,chr(21)=>250,
	chr(22)=>250,chr(23)=>250,chr(24)=>250,chr(25)=>250,chr(26)=>250,chr(27)=>250,chr(28)=>250,chr(29)=>250,chr(30)=>250,chr(31)=>250,' '=>250,'!'=>333,'"'=>408,'#'=>500,'$'=>500,'%'=>833,'&'=>778,'\''=>180,'('=>333,')'=>333,'*'=>500,'+'=>564,
	','=>250,'-'=>333,'.'=>250,'/'=>278,'0'=>500,'1'=>500,'2'=>500,'3'=>500,'4'=>500,'5'=>500,'6'=>500,'7'=>500,'8'=>500,'9'=>500,':'=>278,';'=>278,'<'=>564,'='=>564,'>'=>564,'?'=>444,'@'=>921,'A'=>722,
	'B'=>667,'C'=>667,'D'=>722,'E'=>611,'F'=>556,'G'=>722,'H'=>722,'I'=>333,'J'=>389,'K'=>722,'L'=>611,'M'=>889,'N'=>722,'O'=>722,'P'=>556,'Q'=>722,'R'=>667,'S'=>556,'T'=>611,'U'=>722,'V'=>722,'W'=>944,
	'X'=>722,'Y'=>722,'Z'=>611,'['=>333,'\\'=>278,']'=>333,'^'=>469,'_'=>500,'`'=>333,'a'=>444,'b'=>500,'c'=>444,'d'=>500,'e'=>444,'f'=>333,'g'=>500,'h'=>500,'i'=>278,'j'=>278,'k'=>500,'l'=>278,'m'=>778,
	'n'=>500,'o'=>500,'p'=>500,'q'=>500,'r'=>333,'s'=>389,'t'=>278,'u'=>500,'v'=>500,'w'=>722,'x'=>500,'y'=>500,'z'=>444,'{'=>480,'|'=>200,'}'=>480,'~'=>541,chr(127)=>350,chr(128)=>500,chr(129)=>350,chr(130)=>333,chr(131)=>500,
	chr(132)=>444,chr(133)=>1000,chr(134)=>500,chr(135)=>500,chr(136)=>333,chr(137)=>1000,chr(138)=>556,chr(139)=>333,chr(140)=>889,chr(141)=>350,chr(142)=>611,chr(143)=>350,chr(144)=>350,chr(145)=>333,chr(146)=>333,chr(147)=>444,chr(148)=>444,chr(149)=>350,chr(150)=>500,chr(151)=>1000,chr(152)=>333,chr(153)=>980,
	chr(154)=>389,chr(155)=>333,chr(156)=>722,chr(157)=>350,chr(158)=>444,chr(159)=>722,chr(160)=>250,chr(161)=>333,chr(162)=>500,chr(163)=>500,chr(164)=>500,chr(165)=>500,chr(166)=>200,chr(167)=>500,chr(168)=>333,chr(169)=>760,chr(170)=>276,chr(171)=>500,chr(172)=>564,chr(173)=>333,chr(174)=>760,chr(175)=>333,
	chr(176)=>400,chr(177)=>564,chr(178)=>300,chr(179)=>300,chr(180)=>333,chr(181)=>500,chr(182)=>453,chr(183)=>250,chr(184)=>333,chr(185)=>300,chr(186)=>310,chr(187)=>500,chr(188)=>750,chr(189)=>750,chr(190)=>750,chr(191)=>444,chr(192)=>722,chr(193)=>722,chr(194)=>722,chr(195)=>722,chr(196)=>722,chr(197)=>722,
	chr(198)=>889,chr(199)=>667,chr(200)=>611,chr(201)=>611,chr(202)=>611,chr(203)=>611,chr(204)=>333,chr(205)=>333,chr(206)=>333,chr(207)=>333,chr(208)=>722,chr(209)=>722,chr(210)=>722,chr(211)=>722,chr(212)=>722,chr(213)=>722,chr(214)=>722,chr(215)=>564,chr(216)=>722,chr(217)=>722,chr(218)=>722,chr(219)=>722,
	chr(220)=>722,chr(221)=>722,chr(222)=>556,chr(223)=>500,chr(224)=>444,chr(225)=>444,chr(226)=>444,chr(227)=>444,chr(228)=>444,chr(229)=>444,chr(230)=>667,chr(231)=>444,chr(232)=>444,chr(233)=>444,chr(234)=>444,chr(235)=>444,chr(236)=>278,chr(237)=>278,chr(238)=>278,chr(239)=>278,chr(240)=>500,chr(241)=>500,
	chr(242)=>500,chr(243)=>500,chr(244)=>500,chr(245)=>500,chr(246)=>500,chr(247)=>564,chr(248)=>500,chr(249)=>500,chr(250)=>500,chr(251)=>500,chr(252)=>500,chr(253)=>500,chr(254)=>500,chr(255)=>500);
?>


File: /fpdf\font\timesb.php
<?php
$type = 'Core';
$name = 'Times-Bold';
$up = -100;
$ut = 50;
$cw = array(
	chr(0)=>250,chr(1)=>250,chr(2)=>250,chr(3)=>250,chr(4)=>250,chr(5)=>250,chr(6)=>250,chr(7)=>250,chr(8)=>250,chr(9)=>250,chr(10)=>250,chr(11)=>250,chr(12)=>250,chr(13)=>250,chr(14)=>250,chr(15)=>250,chr(16)=>250,chr(17)=>250,chr(18)=>250,chr(19)=>250,chr(20)=>250,chr(21)=>250,
	chr(22)=>250,chr(23)=>250,chr(24)=>250,chr(25)=>250,chr(26)=>250,chr(27)=>250,chr(28)=>250,chr(29)=>250,chr(30)=>250,chr(31)=>250,' '=>250,'!'=>333,'"'=>555,'#'=>500,'$'=>500,'%'=>1000,'&'=>833,'\''=>278,'('=>333,')'=>333,'*'=>500,'+'=>570,
	','=>250,'-'=>333,'.'=>250,'/'=>278,'0'=>500,'1'=>500,'2'=>500,'3'=>500,'4'=>500,'5'=>500,'6'=>500,'7'=>500,'8'=>500,'9'=>500,':'=>333,';'=>333,'<'=>570,'='=>570,'>'=>570,'?'=>500,'@'=>930,'A'=>722,
	'B'=>667,'C'=>722,'D'=>722,'E'=>667,'F'=>611,'G'=>778,'H'=>778,'I'=>389,'J'=>500,'K'=>778,'L'=>667,'M'=>944,'N'=>722,'O'=>778,'P'=>611,'Q'=>778,'R'=>722,'S'=>556,'T'=>667,'U'=>722,'V'=>722,'W'=>1000,
	'X'=>722,'Y'=>722,'Z'=>667,'['=>333,'\\'=>278,']'=>333,'^'=>581,'_'=>500,'`'=>333,'a'=>500,'b'=>556,'c'=>444,'d'=>556,'e'=>444,'f'=>333,'g'=>500,'h'=>556,'i'=>278,'j'=>333,'k'=>556,'l'=>278,'m'=>833,
	'n'=>556,'o'=>500,'p'=>556,'q'=>556,'r'=>444,'s'=>389,'t'=>333,'u'=>556,'v'=>500,'w'=>722,'x'=>500,'y'=>500,'z'=>444,'{'=>394,'|'=>220,'}'=>394,'~'=>520,chr(127)=>350,chr(128)=>500,chr(129)=>350,chr(130)=>333,chr(131)=>500,
	chr(132)=>500,chr(133)=>1000,chr(134)=>500,chr(135)=>500,chr(136)=>333,chr(137)=>1000,chr(138)=>556,chr(139)=>333,chr(140)=>1000,chr(141)=>350,chr(142)=>667,chr(143)=>350,chr(144)=>350,chr(145)=>333,chr(146)=>333,chr(147)=>500,chr(148)=>500,chr(149)=>350,chr(150)=>500,chr(151)=>1000,chr(152)=>333,chr(153)=>1000,
	chr(154)=>389,chr(155)=>333,chr(156)=>722,chr(157)=>350,chr(158)=>444,chr(159)=>722,chr(160)=>250,chr(161)=>333,chr(162)=>500,chr(163)=>500,chr(164)=>500,chr(165)=>500,chr(166)=>220,chr(167)=>500,chr(168)=>333,chr(169)=>747,chr(170)=>300,chr(171)=>500,chr(172)=>570,chr(173)=>333,chr(174)=>747,chr(175)=>333,
	chr(176)=>400,chr(177)=>570,chr(178)=>300,chr(179)=>300,chr(180)=>333,chr(181)=>556,chr(182)=>540,chr(183)=>250,chr(184)=>333,chr(185)=>300,chr(186)=>330,chr(187)=>500,chr(188)=>750,chr(189)=>750,chr(190)=>750,chr(191)=>500,chr(192)=>722,chr(193)=>722,chr(194)=>722,chr(195)=>722,chr(196)=>722,chr(197)=>722,
	chr(198)=>1000,chr(199)=>722,chr(200)=>667,chr(201)=>667,chr(202)=>667,chr(203)=>667,chr(204)=>389,chr(205)=>389,chr(206)=>389,chr(207)=>389,chr(208)=>722,chr(209)=>722,chr(210)=>778,chr(211)=>778,chr(212)=>778,chr(213)=>778,chr(214)=>778,chr(215)=>570,chr(216)=>778,chr(217)=>722,chr(218)=>722,chr(219)=>722,
	chr(220)=>722,chr(221)=>722,chr(222)=>611,chr(223)=>556,chr(224)=>500,chr(225)=>500,chr(226)=>500,chr(227)=>500,chr(228)=>500,chr(229)=>500,chr(230)=>722,chr(231)=>444,chr(232)=>444,chr(233)=>444,chr(234)=>444,chr(235)=>444,chr(236)=>278,chr(237)=>278,chr(238)=>278,chr(239)=>278,chr(240)=>500,chr(241)=>556,
	chr(242)=>500,chr(243)=>500,chr(244)=>500,chr(245)=>500,chr(246)=>500,chr(247)=>570,chr(248)=>500,chr(249)=>556,chr(250)=>556,chr(251)=>556,chr(252)=>556,chr(253)=>500,chr(254)=>556,chr(255)=>500);
?>


File: /fpdf\font\timesbi.php
<?php
$type = 'Core';
$name = 'Times-BoldItalic';
$up = -100;
$ut = 50;
$cw = array(
	chr(0)=>250,chr(1)=>250,chr(2)=>250,chr(3)=>250,chr(4)=>250,chr(5)=>250,chr(6)=>250,chr(7)=>250,chr(8)=>250,chr(9)=>250,chr(10)=>250,chr(11)=>250,chr(12)=>250,chr(13)=>250,chr(14)=>250,chr(15)=>250,chr(16)=>250,chr(17)=>250,chr(18)=>250,chr(19)=>250,chr(20)=>250,chr(21)=>250,
	chr(22)=>250,chr(23)=>250,chr(24)=>250,chr(25)=>250,chr(26)=>250,chr(27)=>250,chr(28)=>250,chr(29)=>250,chr(30)=>250,chr(31)=>250,' '=>250,'!'=>389,'"'=>555,'#'=>500,'$'=>500,'%'=>833,'&'=>778,'\''=>278,'('=>333,')'=>333,'*'=>500,'+'=>570,
	','=>250,'-'=>333,'.'=>250,'/'=>278,'0'=>500,'1'=>500,'2'=>500,'3'=>500,'4'=>500,'5'=>500,'6'=>500,'7'=>500,'8'=>500,'9'=>500,':'=>333,';'=>333,'<'=>570,'='=>570,'>'=>570,'?'=>500,'@'=>832,'A'=>667,
	'B'=>667,'C'=>667,'D'=>722,'E'=>667,'F'=>667,'G'=>722,'H'=>778,'I'=>389,'J'=>500,'K'=>667,'L'=>611,'M'=>889,'N'=>722,'O'=>722,'P'=>611,'Q'=>722,'R'=>667,'S'=>556,'T'=>611,'U'=>722,'V'=>667,'W'=>889,
	'X'=>667,'Y'=>611,'Z'=>611,'['=>333,'\\'=>278,']'=>333,'^'=>570,'_'=>500,'`'=>333,'a'=>500,'b'=>500,'c'=>444,'d'=>500,'e'=>444,'f'=>333,'g'=>500,'h'=>556,'i'=>278,'j'=>278,'k'=>500,'l'=>278,'m'=>778,
	'n'=>556,'o'=>500,'p'=>500,'q'=>500,'r'=>389,'s'=>389,'t'=>278,'u'=>556,'v'=>444,'w'=>667,'x'=>500,'y'=>444,'z'=>389,'{'=>348,'|'=>220,'}'=>348,'~'=>570,chr(127)=>350,chr(128)=>500,chr(129)=>350,chr(130)=>333,chr(131)=>500,
	chr(132)=>500,chr(133)=>1000,chr(134)=>500,chr(135)=>500,chr(136)=>333,chr(137)=>1000,chr(138)=>556,chr(139)=>333,chr(140)=>944,chr(141)=>350,chr(142)=>611,chr(143)=>350,chr(144)=>350,chr(145)=>333,chr(146)=>333,chr(147)=>500,chr(148)=>500,chr(149)=>350,chr(150)=>500,chr(151)=>1000,chr(152)=>333,chr(153)=>1000,
	chr(154)=>389,chr(155)=>333,chr(156)=>722,chr(157)=>350,chr(158)=>389,chr(159)=>611,chr(160)=>250,chr(161)=>389,chr(162)=>500,chr(163)=>500,chr(164)=>500,chr(165)=>500,chr(166)=>220,chr(167)=>500,chr(168)=>333,chr(169)=>747,chr(170)=>266,chr(171)=>500,chr(172)=>606,chr(173)=>333,chr(174)=>747,chr(175)=>333,
	chr(176)=>400,chr(177)=>570,chr(178)=>300,chr(179)=>300,chr(180)=>333,chr(181)=>576,chr(182)=>500,chr(183)=>250,chr(184)=>333,chr(185)=>300,chr(186)=>300,chr(187)=>500,chr(188)=>750,chr(189)=>750,chr(190)=>750,chr(191)=>500,chr(192)=>667,chr(193)=>667,chr(194)=>667,chr(195)=>667,chr(196)=>667,chr(197)=>667,
	chr(198)=>944,chr(199)=>667,chr(200)=>667,chr(201)=>667,chr(202)=>667,chr(203)=>667,chr(204)=>389,chr(205)=>389,chr(206)=>389,chr(207)=>389,chr(208)=>722,chr(209)=>722,chr(210)=>722,chr(211)=>722,chr(212)=>722,chr(213)=>722,chr(214)=>722,chr(215)=>570,chr(216)=>722,chr(217)=>722,chr(218)=>722,chr(219)=>722,
	chr(220)=>722,chr(221)=>611,chr(222)=>611,chr(223)=>500,chr(224)=>500,chr(225)=>500,chr(226)=>500,chr(227)=>500,chr(228)=>500,chr(229)=>500,chr(230)=>722,chr(231)=>444,chr(232)=>444,chr(233)=>444,chr(234)=>444,chr(235)=>444,chr(236)=>278,chr(237)=>278,chr(238)=>278,chr(239)=>278,chr(240)=>500,chr(241)=>556,
	chr(242)=>500,chr(243)=>500,chr(244)=>500,chr(245)=>500,chr(246)=>500,chr(247)=>570,chr(248)=>500,chr(249)=>556,chr(250)=>556,chr(251)=>556,chr(252)=>556,chr(253)=>444,chr(254)=>500,chr(255)=>444);
?>


File: /fpdf\font\timesi.php
<?php
$type = 'Core';
$name = 'Times-Italic';
$up = -100;
$ut = 50;
$cw = array(
	chr(0)=>250,chr(1)=>250,chr(2)=>250,chr(3)=>250,chr(4)=>250,chr(5)=>250,chr(6)=>250,chr(7)=>250,chr(8)=>250,chr(9)=>250,chr(10)=>250,chr(11)=>250,chr(12)=>250,chr(13)=>250,chr(14)=>250,chr(15)=>250,chr(16)=>250,chr(17)=>250,chr(18)=>250,chr(19)=>250,chr(20)=>250,chr(21)=>250,
	chr(22)=>250,chr(23)=>250,chr(24)=>250,chr(25)=>250,chr(26)=>250,chr(27)=>250,chr(28)=>250,chr(29)=>250,chr(30)=>250,chr(31)=>250,' '=>250,'!'=>333,'"'=>420,'#'=>500,'$'=>500,'%'=>833,'&'=>778,'\''=>214,'('=>333,')'=>333,'*'=>500,'+'=>675,
	','=>250,'-'=>333,'.'=>250,'/'=>278,'0'=>500,'1'=>500,'2'=>500,'3'=>500,'4'=>500,'5'=>500,'6'=>500,'7'=>500,'8'=>500,'9'=>500,':'=>333,';'=>333,'<'=>675,'='=>675,'>'=>675,'?'=>500,'@'=>920,'A'=>611,
	'B'=>611,'C'=>667,'D'=>722,'E'=>611,'F'=>611,'G'=>722,'H'=>722,'I'=>333,'J'=>444,'K'=>667,'L'=>556,'M'=>833,'N'=>667,'O'=>722,'P'=>611,'Q'=>722,'R'=>611,'S'=>500,'T'=>556,'U'=>722,'V'=>611,'W'=>833,
	'X'=>611,'Y'=>556,'Z'=>556,'['=>389,'\\'=>278,']'=>389,'^'=>422,'_'=>500,'`'=>333,'a'=>500,'b'=>500,'c'=>444,'d'=>500,'e'=>444,'f'=>278,'g'=>500,'h'=>500,'i'=>278,'j'=>278,'k'=>444,'l'=>278,'m'=>722,
	'n'=>500,'o'=>500,'p'=>500,'q'=>500,'r'=>389,'s'=>389,'t'=>278,'u'=>500,'v'=>444,'w'=>667,'x'=>444,'y'=>444,'z'=>389,'{'=>400,'|'=>275,'}'=>400,'~'=>541,chr(127)=>350,chr(128)=>500,chr(129)=>350,chr(130)=>333,chr(131)=>500,
	chr(132)=>556,chr(133)=>889,chr(134)=>500,chr(135)=>500,chr(136)=>333,chr(137)=>1000,chr(138)=>500,chr(139)=>333,chr(140)=>944,chr(141)=>350,chr(142)=>556,chr(143)=>350,chr(144)=>350,chr(145)=>333,chr(146)=>333,chr(147)=>556,chr(148)=>556,chr(149)=>350,chr(150)=>500,chr(151)=>889,chr(152)=>333,chr(153)=>980,
	chr(154)=>389,chr(155)=>333,chr(156)=>667,chr(157)=>350,chr(158)=>389,chr(159)=>556,chr(160)=>250,chr(161)=>389,chr(162)=>500,chr(163)=>500,chr(164)=>500,chr(165)=>500,chr(166)=>275,chr(167)=>500,chr(168)=>333,chr(169)=>760,chr(170)=>276,chr(171)=>500,chr(172)=>675,chr(173)=>333,chr(174)=>760,chr(175)=>333,
	chr(176)=>400,chr(177)=>675,chr(178)=>300,chr(179)=>300,chr(180)=>333,chr(181)=>500,chr(182)=>523,chr(183)=>250,chr(184)=>333,chr(185)=>300,chr(186)=>310,chr(187)=>500,chr(188)=>750,chr(189)=>750,chr(190)=>750,chr(191)=>500,chr(192)=>611,chr(193)=>611,chr(194)=>611,chr(195)=>611,chr(196)=>611,chr(197)=>611,
	chr(198)=>889,chr(199)=>667,chr(200)=>611,chr(201)=>611,chr(202)=>611,chr(203)=>611,chr(204)=>333,chr(205)=>333,chr(206)=>333,chr(207)=>333,chr(208)=>722,chr(209)=>667,chr(210)=>722,chr(211)=>722,chr(212)=>722,chr(213)=>722,chr(214)=>722,chr(215)=>675,chr(216)=>722,chr(217)=>722,chr(218)=>722,chr(219)=>722,
	chr(220)=>722,chr(221)=>556,chr(222)=>611,chr(223)=>500,chr(224)=>500,chr(225)=>500,chr(226)=>500,chr(227)=>500,chr(228)=>500,chr(229)=>500,chr(230)=>667,chr(231)=>444,chr(232)=>444,chr(233)=>444,chr(234)=>444,chr(235)=>444,chr(236)=>278,chr(237)=>278,chr(238)=>278,chr(239)=>278,chr(240)=>500,chr(241)=>500,
	chr(242)=>500,chr(243)=>500,chr(244)=>500,chr(245)=>500,chr(246)=>500,chr(247)=>675,chr(248)=>500,chr(249)=>500,chr(250)=>500,chr(251)=>500,chr(252)=>500,chr(253)=>444,chr(254)=>500,chr(255)=>444);
?>


File: /fpdf\font\zapfdingbats.php
<?php
$type = 'Core';
$name = 'ZapfDingbats';
$up = -100;
$ut = 50;
$cw = array(
	chr(0)=>0,chr(1)=>0,chr(2)=>0,chr(3)=>0,chr(4)=>0,chr(5)=>0,chr(6)=>0,chr(7)=>0,chr(8)=>0,chr(9)=>0,chr(10)=>0,chr(11)=>0,chr(12)=>0,chr(13)=>0,chr(14)=>0,chr(15)=>0,chr(16)=>0,chr(17)=>0,chr(18)=>0,chr(19)=>0,chr(20)=>0,chr(21)=>0,
	chr(22)=>0,chr(23)=>0,chr(24)=>0,chr(25)=>0,chr(26)=>0,chr(27)=>0,chr(28)=>0,chr(29)=>0,chr(30)=>0,chr(31)=>0,' '=>278,'!'=>974,'"'=>961,'#'=>974,'$'=>980,'%'=>719,'&'=>789,'\''=>790,'('=>791,')'=>690,'*'=>960,'+'=>939,
	','=>549,'-'=>855,'.'=>911,'/'=>933,'0'=>911,'1'=>945,'2'=>974,'3'=>755,'4'=>846,'5'=>762,'6'=>761,'7'=>571,'8'=>677,'9'=>763,':'=>760,';'=>759,'<'=>754,'='=>494,'>'=>552,'?'=>537,'@'=>577,'A'=>692,
	'B'=>786,'C'=>788,'D'=>788,'E'=>790,'F'=>793,'G'=>794,'H'=>816,'I'=>823,'J'=>789,'K'=>841,'L'=>823,'M'=>833,'N'=>816,'O'=>831,'P'=>923,'Q'=>744,'R'=>723,'S'=>749,'T'=>790,'U'=>792,'V'=>695,'W'=>776,
	'X'=>768,'Y'=>792,'Z'=>759,'['=>707,'\\'=>708,']'=>682,'^'=>701,'_'=>826,'`'=>815,'a'=>789,'b'=>789,'c'=>707,'d'=>687,'e'=>696,'f'=>689,'g'=>786,'h'=>787,'i'=>713,'j'=>791,'k'=>785,'l'=>791,'m'=>873,
	'n'=>761,'o'=>762,'p'=>762,'q'=>759,'r'=>759,'s'=>892,'t'=>892,'u'=>788,'v'=>784,'w'=>438,'x'=>138,'y'=>277,'z'=>415,'{'=>392,'|'=>392,'}'=>668,'~'=>668,chr(127)=>0,chr(128)=>390,chr(129)=>390,chr(130)=>317,chr(131)=>317,
	chr(132)=>276,chr(133)=>276,chr(134)=>509,chr(135)=>509,chr(136)=>410,chr(137)=>410,chr(138)=>234,chr(139)=>234,chr(140)=>334,chr(141)=>334,chr(142)=>0,chr(143)=>0,chr(144)=>0,chr(145)=>0,chr(146)=>0,chr(147)=>0,chr(148)=>0,chr(149)=>0,chr(150)=>0,chr(151)=>0,chr(152)=>0,chr(153)=>0,
	chr(154)=>0,chr(155)=>0,chr(156)=>0,chr(157)=>0,chr(158)=>0,chr(159)=>0,chr(160)=>0,chr(161)=>732,chr(162)=>544,chr(163)=>544,chr(164)=>910,chr(165)=>667,chr(166)=>760,chr(167)=>760,chr(168)=>776,chr(169)=>595,chr(170)=>694,chr(171)=>626,chr(172)=>788,chr(173)=>788,chr(174)=>788,chr(175)=>788,
	chr(176)=>788,chr(177)=>788,chr(178)=>788,chr(179)=>788,chr(180)=>788,chr(181)=>788,chr(182)=>788,chr(183)=>788,chr(184)=>788,chr(185)=>788,chr(186)=>788,chr(187)=>788,chr(188)=>788,chr(189)=>788,chr(190)=>788,chr(191)=>788,chr(192)=>788,chr(193)=>788,chr(194)=>788,chr(195)=>788,chr(196)=>788,chr(197)=>788,
	chr(198)=>788,chr(199)=>788,chr(200)=>788,chr(201)=>788,chr(202)=>788,chr(203)=>788,chr(204)=>788,chr(205)=>788,chr(206)=>788,chr(207)=>788,chr(208)=>788,chr(209)=>788,chr(210)=>788,chr(211)=>788,chr(212)=>894,chr(213)=>838,chr(214)=>1016,chr(215)=>458,chr(216)=>748,chr(217)=>924,chr(218)=>748,chr(219)=>918,
	chr(220)=>927,chr(221)=>928,chr(222)=>928,chr(223)=>834,chr(224)=>873,chr(225)=>828,chr(226)=>924,chr(227)=>924,chr(228)=>917,chr(229)=>930,chr(230)=>931,chr(231)=>463,chr(232)=>883,chr(233)=>836,chr(234)=>836,chr(235)=>867,chr(236)=>867,chr(237)=>696,chr(238)=>696,chr(239)=>874,chr(240)=>0,chr(241)=>874,
	chr(242)=>760,chr(243)=>946,chr(244)=>771,chr(245)=>865,chr(246)=>771,chr(247)=>888,chr(248)=>967,chr(249)=>888,chr(250)=>831,chr(251)=>873,chr(252)=>927,chr(253)=>970,chr(254)=>918,chr(255)=>0);
?>


File: /fpdf\fpdf.css
body {font-family:"Times New Roman",serif}
h1 {font:bold 135% Arial,sans-serif; color:#4000A0; margin-bottom:0.9em}
h2 {font:bold 100% Arial,sans-serif; color:#900000; margin-top:1.5em}
dl.param dt {text-decoration:underline}
dl.param dd {margin-top:1em; margin-bottom:1em}
dl.param ul {margin-top:1em; margin-bottom:1em}
tt, code, kbd {font-family:"Courier New",Courier,monospace; font-size:82%}
div.source {margin-top:1.4em; margin-bottom:1.3em}
div.source pre {display:table; border:1px solid #24246A; width:100%; margin:0em; font-family:inherit; font-size:100%}
div.source code {display:block; border:1px solid #C5C5EC; background-color:#F0F5FF; padding:6px; color:#000000}
div.doc-source {margin-top:1.4em; margin-bottom:1.3em}
div.doc-source pre {display:table; width:100%; margin:0em; font-family:inherit; font-size:100%}
div.doc-source code {display:block; background-color:#E0E0E0; padding:4px}
.kw {color:#000080; font-weight:bold}
.str {color:#CC0000}
.cmt {color:#008000}
p.demo {text-align:center; margin-top:-0.9em}
a.demo {text-decoration:none; font-weight:bold; color:#0000CC}
a.demo:link {text-decoration:none; font-weight:bold; color:#0000CC}
a.demo:hover {text-decoration:none; font-weight:bold; color:#0000FF}
a.demo:active {text-decoration:none; font-weight:bold; color:#0000FF}


File: /fpdf\fpdf.php
<?php
/*******************************************************************************
* FPDF                                                                         *
*                                                                              *
* Version: 1.7                                                                 *
* Date:    2011-06-18                                                          *
* Author:  Olivier PLATHEY                                                     *
*******************************************************************************/

define('FPDF_VERSION','1.7');

class FPDF
{
var $page;               // current page number
var $n;                  // current object number
var $offsets;            // array of object offsets
var $buffer;             // buffer holding in-memory PDF
var $pages;              // array containing pages
var $state;              // current document state
var $compress;           // compression flag
var $k;                  // scale factor (number of points in user unit)
var $DefOrientation;     // default orientation
var $CurOrientation;     // current orientation
var $StdPageSizes;       // standard page sizes
var $DefPageSize;        // default page size
var $CurPageSize;        // current page size
var $PageSizes;          // used for pages with non default sizes or orientations
var $wPt, $hPt;          // dimensions of current page in points
var $w, $h;              // dimensions of current page in user unit
var $lMargin;            // left margin
var $tMargin;            // top margin
var $rMargin;            // right margin
var $bMargin;            // page break margin
var $cMargin;            // cell margin
var $x, $y;              // current position in user unit
var $lasth;              // height of last printed cell
var $LineWidth;          // line width in user unit
var $fontpath;           // path containing fonts
var $CoreFonts;          // array of core font names
var $fonts;              // array of used fonts
var $FontFiles;          // array of font files
var $diffs;              // array of encoding differences
var $FontFamily;         // current font family
var $FontStyle;          // current font style
var $underline;          // underlining flag
var $CurrentFont;        // current font info
var $FontSizePt;         // current font size in points
var $FontSize;           // current font size in user unit
var $DrawColor;          // commands for drawing color
var $FillColor;          // commands for filling color
var $TextColor;          // commands for text color
var $ColorFlag;          // indicates whether fill and text colors are different
var $ws;                 // word spacing
var $images;             // array of used images
var $PageLinks;          // array of links in pages
var $links;              // array of internal links
var $AutoPageBreak;      // automatic page breaking
var $PageBreakTrigger;   // threshold used to trigger page breaks
var $InHeader;           // flag set when processing header
var $InFooter;           // flag set when processing footer
var $ZoomMode;           // zoom display mode
var $LayoutMode;         // layout display mode
var $title;              // title
var $subject;            // subject
var $author;             // author
var $keywords;           // keywords
var $creator;            // creator
var $AliasNbPages;       // alias for total number of pages
var $PDFVersion;         // PDF version number

/*******************************************************************************
*                                                                              *
*                               Public methods                                 *
*                                                                              *
*******************************************************************************/
function FPDF($orientation='P', $unit='mm', $size='A4')
{
	// Some checks
	$this->_dochecks();
	// Initialization of properties
	$this->page = 0;
	$this->n = 2;
	$this->buffer = '';
	$this->pages = array();
	$this->PageSizes = array();
	$this->state = 0;
	$this->fonts = array();
	$this->FontFiles = array();
	$this->diffs = array();
	$this->images = array();
	$this->links = array();
	$this->InHeader = false;
	$this->InFooter = false;
	$this->lasth = 0;
	$this->FontFamily = '';
	$this->FontStyle = '';
	$this->FontSizePt = 12;
	$this->underline = false;
	$this->DrawColor = '0 G';
	$this->FillColor = '0 g';
	$this->TextColor = '0 g';
	$this->ColorFlag = false;
	$this->ws = 0;
	// Font path
	if(defined('FPDF_FONTPATH'))
	{
		$this->fontpath = FPDF_FONTPATH;
		if(substr($this->fontpath,-1)!='/' && substr($this->fontpath,-1)!='\\')
			$this->fontpath .= '/';
	}
	elseif(is_dir(dirname(__FILE__).'/font'))
		$this->fontpath = dirname(__FILE__).'/font/';
	else
		$this->fontpath = '';
	// Core fonts
	$this->CoreFonts = array('courier', 'helvetica', 'times', 'symbol', 'zapfdingbats');
	// Scale factor
	if($unit=='pt')
		$this->k = 1;
	elseif($unit=='mm')
		$this->k = 72/25.4;
	elseif($unit=='cm')
		$this->k = 72/2.54;
	elseif($unit=='in')
		$this->k = 72;
	else
		$this->Error('Incorrect unit: '.$unit);
	// Page sizes
	$this->StdPageSizes = array('a3'=>array(841.89,1190.55), 'a4'=>array(595.28,841.89), 'a5'=>array(420.94,595.28),
		'letter'=>array(612,792), 'legal'=>array(612,1008));
	$size = $this->_getpagesize($size);
	$this->DefPageSize = $size;
	$this->CurPageSize = $size;
	// Page orientation
	$orientation = strtolower($orientation);
	if($orientation=='p' || $orientation=='portrait')
	{
		$this->DefOrientation = 'P';
		$this->w = $size[0];
		$this->h = $size[1];
	}
	elseif($orientation=='l' || $orientation=='landscape')
	{
		$this->DefOrientation = 'L';
		$this->w = $size[1];
		$this->h = $size[0];
	}
	else
		$this->Error('Incorrect orientation: '.$orientation);
	$this->CurOrientation = $this->DefOrientation;
	$this->wPt = $this->w*$this->k;
	$this->hPt = $this->h*$this->k;
	// Page margins (1 cm)
	$margin = 28.35/$this->k;
	$this->SetMargins($margin,$margin);
	// Interior cell margin (1 mm)
	$this->cMargin = $margin/10;
	// Line width (0.2 mm)
	$this->LineWidth = .567/$this->k;
	// Automatic page break
	$this->SetAutoPageBreak(true,2*$margin);
	// Default display mode
	$this->SetDisplayMode('default');
	// Enable compression
	$this->SetCompression(true);
	// Set default PDF version number
	$this->PDFVersion = '1.3';
}

function SetMargins($left, $top, $right=null)
{
	// Set left, top and right margins
	$this->lMargin = $left;
	$this->tMargin = $top;
	if($right===null)
		$right = $left;
	$this->rMargin = $right;
}

function SetLeftMargin($margin)
{
	// Set left margin
	$this->lMargin = $margin;
	if($this->page>0 && $this->x<$margin)
		$this->x = $margin;
}

function SetTopMargin($margin)
{
	// Set top margin
	$this->tMargin = $margin;
}

function SetRightMargin($margin)
{
	// Set right margin
	$this->rMargin = $margin;
}

function SetAutoPageBreak($auto, $margin=0)
{
	// Set auto page break mode and triggering margin
	$this->AutoPageBreak = $auto;
	$this->bMargin = $margin;
	$this->PageBreakTrigger = $this->h-$margin;
}

function SetDisplayMode($zoom, $layout='default')
{
	// Set display mode in viewer
	if($zoom=='fullpage' || $zoom=='fullwidth' || $zoom=='real' || $zoom=='default' || !is_string($zoom))
		$this->ZoomMode = $zoom;
	else
		$this->Error('Incorrect zoom display mode: '.$zoom);
	if($layout=='single' || $layout=='continuous' || $layout=='two' || $layout=='default')
		$this->LayoutMode = $layout;
	else
		$this->Error('Incorrect layout display mode: '.$layout);
}

function SetCompression($compress)
{
	// Set page compression
	if(function_exists('gzcompress'))
		$this->compress = $compress;
	else
		$this->compress = false;
}

function SetTitle($title, $isUTF8=false)
{
	// Title of document
	if($isUTF8)
		$title = $this->_UTF8toUTF16($title);
	$this->title = $title;
}

function SetSubject($subject, $isUTF8=false)
{
	// Subject of document
	if($isUTF8)
		$subject = $this->_UTF8toUTF16($subject);
	$this->subject = $subject;
}

function SetAuthor($author, $isUTF8=false)
{
	// Author of document
	if($isUTF8)
		$author = $this->_UTF8toUTF16($author);
	$this->author = $author;
}

function SetKeywords($keywords, $isUTF8=false)
{
	// Keywords of document
	if($isUTF8)
		$keywords = $this->_UTF8toUTF16($keywords);
	$this->keywords = $keywords;
}

function SetCreator($creator, $isUTF8=false)
{
	// Creator of document
	if($isUTF8)
		$creator = $this->_UTF8toUTF16($creator);
	$this->creator = $creator;
}

function AliasNbPages($alias='{nb}')
{
	// Define an alias for total number of pages
	$this->AliasNbPages = $alias;
}

function Error($msg)
{
	// Fatal error
	die('<b>FPDF error:</b> '.$msg);
}

function Open()
{
	// Begin document
	$this->state = 1;
}

function Close()
{
	// Terminate document
	if($this->state==3)
		return;
	if($this->page==0)
		$this->AddPage();
	// Page footer
	$this->InFooter = true;
	$this->Footer();
	$this->InFooter = false;
	// Close page
	$this->_endpage();
	// Close document
	$this->_enddoc();
}

function AddPage($orientation='', $size='')
{
	// Start a new page
	if($this->state==0)
		$this->Open();
	$family = $this->FontFamily;
	$style = $this->FontStyle.($this->underline ? 'U' : '');
	$fontsize = $this->FontSizePt;
	$lw = $this->LineWidth;
	$dc = $this->DrawColor;
	$fc = $this->FillColor;
	$tc = $this->TextColor;
	$cf = $this->ColorFlag;
	if($this->page>0)
	{
		// Page footer
		$this->InFooter = true;
		$this->Footer();
		$this->InFooter = false;
		// Close page
		$this->_endpage();
	}
	// Start new page
	$this->_beginpage($orientation,$size);
	// Set line cap style to square
	$this->_out('2 J');
	// Set line width
	$this->LineWidth = $lw;
	$this->_out(sprintf('%.2F w',$lw*$this->k));
	// Set font
	if($family)
		$this->SetFont($family,$style,$fontsize);
	// Set colors
	$this->DrawColor = $dc;
	if($dc!='0 G')
		$this->_out($dc);
	$this->FillColor = $fc;
	if($fc!='0 g')
		$this->_out($fc);
	$this->TextColor = $tc;
	$this->ColorFlag = $cf;
	// Page header
	$this->InHeader = true;
	$this->Header();
	$this->InHeader = false;
	// Restore line width
	if($this->LineWidth!=$lw)
	{
		$this->LineWidth = $lw;
		$this->_out(sprintf('%.2F w',$lw*$this->k));
	}
	// Restore font
	if($family)
		$this->SetFont($family,$style,$fontsize);
	// Restore colors
	if($this->DrawColor!=$dc)
	{
		$this->DrawColor = $dc;
		$this->_out($dc);
	}
	if($this->FillColor!=$fc)
	{
		$this->FillColor = $fc;
		$this->_out($fc);
	}
	$this->TextColor = $tc;
	$this->ColorFlag = $cf;
}

function Header()
{
	// To be implemented in your own inherited class
}

function Footer()
{
	// To be implemented in your own inherited class
}

function PageNo()
{
	// Get current page number
	return $this->page;
}

function SetDrawColor($r, $g=null, $b=null)
{
	// Set color for all stroking operations
	if(($r==0 && $g==0 && $b==0) || $g===null)
		$this->DrawColor = sprintf('%.3F G',$r/255);
	else
		$this->DrawColor = sprintf('%.3F %.3F %.3F RG',$r/255,$g/255,$b/255);
	if($this->page>0)
		$this->_out($this->DrawColor);
}

function SetFillColor($r, $g=null, $b=null)
{
	// Set color for all filling operations
	if(($r==0 && $g==0 && $b==0) || $g===null)
		$this->FillColor = sprintf('%.3F g',$r/255);
	else
		$this->FillColor = sprintf('%.3F %.3F %.3F rg',$r/255,$g/255,$b/255);
	$this->ColorFlag = ($this->FillColor!=$this->TextColor);
	if($this->page>0)
		$this->_out($this->FillColor);
}

function SetTextColor($r, $g=null, $b=null)
{
	// Set color for text
	if(($r==0 && $g==0 && $b==0) || $g===null)
		$this->TextColor = sprintf('%.3F g',$r/255);
	else
		$this->TextColor = sprintf('%.3F %.3F %.3F rg',$r/255,$g/255,$b/255);
	$this->ColorFlag = ($this->FillColor!=$this->TextColor);
}

function GetStringWidth($s)
{
	// Get width of a string in the current font
	$s = (string)$s;
	$cw = &$this->CurrentFont['cw'];
	$w = 0;
	$l = strlen($s);
	for($i=0;$i<$l;$i++)
		$w += $cw[$s[$i]];
	return $w*$this->FontSize/1000;
}

function SetLineWidth($width)
{
	// Set line width
	$this->LineWidth = $width;
	if($this->page>0)
		$this->_out(sprintf('%.2F w',$width*$this->k));
}

function Line($x1, $y1, $x2, $y2)
{
	// Draw a line
	$this->_out(sprintf('%.2F %.2F m %.2F %.2F l S',$x1*$this->k,($this->h-$y1)*$this->k,$x2*$this->k,($this->h-$y2)*$this->k));
}

function Rect($x, $y, $w, $h, $style='')
{
	// Draw a rectangle
	if($style=='F')
		$op = 'f';
	elseif($style=='FD' || $style=='DF')
		$op = 'B';
	else
		$op = 'S';
	$this->_out(sprintf('%.2F %.2F %.2F %.2F re %s',$x*$this->k,($this->h-$y)*$this->k,$w*$this->k,-$h*$this->k,$op));
}

function AddFont($family, $style='', $file='')
{
	// Add a TrueType, OpenType or Type1 font
	$family = strtolower($family);
	if($file=='')
		$file = str_replace(' ','',$family).strtolower($style).'.php';
	$style = strtoupper($style);
	if($style=='IB')
		$style = 'BI';
	$fontkey = $family.$style;
	if(isset($this->fonts[$fontkey]))
		return;
	$info = $this->_loadfont($file);
	$info['i'] = count($this->fonts)+1;
	if(!empty($info['diff']))
	{
		// Search existing encodings
		$n = array_search($info['diff'],$this->diffs);
		if(!$n)
		{
			$n = count($this->diffs)+1;
			$this->diffs[$n] = $info['diff'];
		}
		$info['diffn'] = $n;
	}
	if(!empty($info['file']))
	{
		// Embedded font
		if($info['type']=='TrueType')
			$this->FontFiles[$info['file']] = array('length1'=>$info['originalsize']);
		else
			$this->FontFiles[$info['file']] = array('length1'=>$info['size1'], 'length2'=>$info['size2']);
	}
	$this->fonts[$fontkey] = $info;
}

function SetFont($family, $style='', $size=0)
{
	// Select a font; size given in points
	if($family=='')
		$family = $this->FontFamily;
	else
		$family = strtolower($family);
	$style = strtoupper($style);
	if(strpos($style,'U')!==false)
	{
		$this->underline = true;
		$style = str_replace('U','',$style);
	}
	else
		$this->underline = false;
	if($style=='IB')
		$style = 'BI';
	if($size==0)
		$size = $this->FontSizePt;
	// Test if font is already selected
	if($this->FontFamily==$family && $this->FontStyle==$style && $this->FontSizePt==$size)
		return;
	// Test if font is already loaded
	$fontkey = $family.$style;
	if(!isset($this->fonts[$fontkey]))
	{
		// Test if one of the core fonts
		if($family=='arial')
			$family = 'helvetica';
		if(in_array($family,$this->CoreFonts))
		{
			if($family=='symbol' || $family=='zapfdingbats')
				$style = '';
			$fontkey = $family.$style;
			if(!isset($this->fonts[$fontkey]))
				$this->AddFont($family,$style);
		}
		else
			$this->Error('Undefined font: '.$family.' '.$style);
	}
	// Select it
	$this->FontFamily = $family;
	$this->FontStyle = $style;
	$this->FontSizePt = $size;
	$this->FontSize = $size/$this->k;
	$this->CurrentFont = &$this->fonts[$fontkey];
	if($this->page>0)
		$this->_out(sprintf('BT /F%d %.2F Tf ET',$this->CurrentFont['i'],$this->FontSizePt));
}

function SetFontSize($size)
{
	// Set font size in points
	if($this->FontSizePt==$size)
		return;
	$this->FontSizePt = $size;
	$this->FontSize = $size/$this->k;
	if($this->page>0)
		$this->_out(sprintf('BT /F%d %.2F Tf ET',$this->CurrentFont['i'],$this->FontSizePt));
}

function AddLink()
{
	// Create a new internal link
	$n = count($this->links)+1;
	$this->links[$n] = array(0, 0);
	return $n;
}

function SetLink($link, $y=0, $page=-1)
{
	// Set destination of internal link
	if($y==-1)
		$y = $this->y;
	if($page==-1)
		$page = $this->page;
	$this->links[$link] = array($page, $y);
}

function Link($x, $y, $w, $h, $link)
{
	// Put a link on the page
	$this->PageLinks[$this->page][] = array($x*$this->k, $this->hPt-$y*$this->k, $w*$this->k, $h*$this->k, $link);
}

function Text($x, $y, $txt)
{
	// Output a string
	$s = sprintf('BT %.2F %.2F Td (%s) Tj ET',$x*$this->k,($this->h-$y)*$this->k,$this->_escape($txt));
	if($this->underline && $txt!='')
		$s .= ' '.$this->_dounderline($x,$y,$txt);
	if($this->ColorFlag)
		$s = 'q '.$this->TextColor.' '.$s.' Q';
	$this->_out($s);
}

function AcceptPageBreak()
{
	// Accept automatic page break or not
	return $this->AutoPageBreak;
}

function Cell($w, $h=0, $txt='', $border=0, $ln=0, $align='', $fill=false, $link='')
{
	// Output a cell
	$k = $this->k;
	if($this->y+$h>$this->PageBreakTrigger && !$this->InHeader && !$this->InFooter && $this->AcceptPageBreak())
	{
		// Automatic page break
		$x = $this->x;
		$ws = $this->ws;
		if($ws>0)
		{
			$this->ws = 0;
			$this->_out('0 Tw');
		}
		$this->AddPage($this->CurOrientation,$this->CurPageSize);
		$this->x = $x;
		if($ws>0)
		{
			$this->ws = $ws;
			$this->_out(sprintf('%.3F Tw',$ws*$k));
		}
	}
	if($w==0)
		$w = $this->w-$this->rMargin-$this->x;
	$s = '';
	if($fill || $border==1)
	{
		if($fill)
			$op = ($border==1) ? 'B' : 'f';
		else
			$op = 'S';
		$s = sprintf('%.2F %.2F %.2F %.2F re %s ',$this->x*$k,($this->h-$this->y)*$k,$w*$k,-$h*$k,$op);
	}
	if(is_string($border))
	{
		$x = $this->x;
		$y = $this->y;
		if(strpos($border,'L')!==false)
			$s .= sprintf('%.2F %.2F m %.2F %.2F l S ',$x*$k,($this->h-$y)*$k,$x*$k,($this->h-($y+$h))*$k);
		if(strpos($border,'T')!==false)
			$s .= sprintf('%.2F %.2F m %.2F %.2F l S ',$x*$k,($this->h-$y)*$k,($x+$w)*$k,($this->h-$y)*$k);
		if(strpos($border,'R')!==false)
			$s .= sprintf('%.2F %.2F m %.2F %.2F l S ',($x+$w)*$k,($this->h-$y)*$k,($x+$w)*$k,($this->h-($y+$h))*$k);
		if(strpos($border,'B')!==false)
			$s .= sprintf('%.2F %.2F m %.2F %.2F l S ',$x*$k,($this->h-($y+$h))*$k,($x+$w)*$k,($this->h-($y+$h))*$k);
	}
	if($txt!=='')
	{
		if($align=='R')
			$dx = $w-$this->cMargin-$this->GetStringWidth($txt);
		elseif($align=='C')
			$dx = ($w-$this->GetStringWidth($txt))/2;
		else
			$dx = $this->cMargin;
		if($this->ColorFlag)
			$s .= 'q '.$this->TextColor.' ';
		$txt2 = str_replace(')','\\)',str_replace('(','\\(',str_replace('\\','\\\\',$txt)));
		$s .= sprintf('BT %.2F %.2F Td (%s) Tj ET',($this->x+$dx)*$k,($this->h-($this->y+.5*$h+.3*$this->FontSize))*$k,$txt2);
		if($this->underline)
			$s .= ' '.$this->_dounderline($this->x+$dx,$this->y+.5*$h+.3*$this->FontSize,$txt);
		if($this->ColorFlag)
			$s .= ' Q';
		if($link)
			$this->Link($this->x+$dx,$this->y+.5*$h-.5*$this->FontSize,$this->GetStringWidth($txt),$this->FontSize,$link);
	}
	if($s)
		$this->_out($s);
	$this->lasth = $h;
	if($ln>0)
	{
		// Go to next line
		$this->y += $h;
		if($ln==1)
			$this->x = $this->lMargin;
	}
	else
		$this->x += $w;
}

function MultiCell($w, $h, $txt, $border=0, $align='J', $fill=false)
{
	// Output text with automatic or explicit line breaks
	$cw = &$this->CurrentFont['cw'];
	if($w==0)
		$w = $this->w-$this->rMargin-$this->x;
	$wmax = ($w-2*$this->cMargin)*1000/$this->FontSize;
	$s = str_replace("\r",'',$txt);
	$nb = strlen($s);
	if($nb>0 && $s[$nb-1]=="\n")
		$nb--;
	$b = 0;
	if($border)
	{
		if($border==1)
		{
			$border = 'LTRB';
			$b = 'LRT';
			$b2 = 'LR';
		}
		else
		{
			$b2 = '';
			if(strpos($border,'L')!==false)
				$b2 .= 'L';
			if(strpos($border,'R')!==false)
				$b2 .= 'R';
			$b = (strpos($border,'T')!==false) ? $b2.'T' : $b2;
		}
	}
	$sep = -1;
	$i = 0;
	$j = 0;
	$l = 0;
	$ns = 0;
	$nl = 1;
	while($i<$nb)
	{
		// Get next character
		$c = $s[$i];
		if($c=="\n")
		{
			// Explicit line break
			if($this->ws>0)
			{
				$this->ws = 0;
				$this->_out('0 Tw');
			}
			$this->Cell($w,$h,substr($s,$j,$i-$j),$b,2,$align,$fill);
			$i++;
			$sep = -1;
			$j = $i;
			$l = 0;
			$ns = 0;
			$nl++;
			if($border && $nl==2)
				$b = $b2;
			continue;
		}
		if($c==' ')
		{
			$sep = $i;
			$ls = $l;
			$ns++;
		}
		$l += $cw[$c];
		if($l>$wmax)
		{
			// Automatic line break
			if($sep==-1)
			{
				if($i==$j)
					$i++;
				if($this->ws>0)
				{
					$this->ws = 0;
					$this->_out('0 Tw');
				}
				$this->Cell($w,$h,substr($s,$j,$i-$j),$b,2,$align,$fill);
			}
			else
			{
				if($align=='J')
				{
					$this->ws = ($ns>1) ? ($wmax-$ls)/1000*$this->FontSize/($ns-1) : 0;
					$this->_out(sprintf('%.3F Tw',$this->ws*$this->k));
				}
				$this->Cell($w,$h,substr($s,$j,$sep-$j),$b,2,$align,$fill);
				$i = $sep+1;
			}
			$sep = -1;
			$j = $i;
			$l = 0;
			$ns = 0;
			$nl++;
			if($border && $nl==2)
				$b = $b2;
		}
		else
			$i++;
	}
	// Last chunk
	if($this->ws>0)
	{
		$this->ws = 0;
		$this->_out('0 Tw');
	}
	if($border && strpos($border,'B')!==false)
		$b .= 'B';
	$this->Cell($w,$h,substr($s,$j,$i-$j),$b,2,$align,$fill);
	$this->x = $this->lMargin;
}

function Write($h, $txt, $link='')
{
	// Output text in flowing mode
	$cw = &$this->CurrentFont['cw'];
	$w = $this->w-$this->rMargin-$this->x;
	$wmax = ($w-2*$this->cMargin)*1000/$this->FontSize;
	$s = str_replace("\r",'',$txt);
	$nb = strlen($s);
	$sep = -1;
	$i = 0;
	$j = 0;
	$l = 0;
	$nl = 1;
	while($i<$nb)
	{
		// Get next character
		$c = $s[$i];
		if($c=="\n")
		{
			// Explicit line break
			$this->Cell($w,$h,substr($s,$j,$i-$j),0,2,'',0,$link);
			$i++;
			$sep = -1;
			$j = $i;
			$l = 0;
			if($nl==1)
			{
				$this->x = $this->lMargin;
				$w = $this->w-$this->rMargin-$this->x;
				$wmax = ($w-2*$this->cMargin)*1000/$this->FontSize;
			}
			$nl++;
			continue;
		}
		if($c==' ')
			$sep = $i;
		$l += $cw[$c];
		if($l>$wmax)
		{
			// Automatic line break
			if($sep==-1)
			{
				if($this->x>$this->lMargin)
				{
					// Move to next line
					$this->x = $this->lMargin;
					$this->y += $h;
					$w = $this->w-$this->rMargin-$this->x;
					$wmax = ($w-2*$this->cMargin)*1000/$this->FontSize;
					$i++;
					$nl++;
					continue;
				}
				if($i==$j)
					$i++;
				$this->Cell($w,$h,substr($s,$j,$i-$j),0,2,'',0,$link);
			}
			else
			{
				$this->Cell($w,$h,substr($s,$j,$sep-$j),0,2,'',0,$link);
				$i = $sep+1;
			}
			$sep = -1;
			$j = $i;
			$l = 0;
			if($nl==1)
			{
				$this->x = $this->lMargin;
				$w = $this->w-$this->rMargin-$this->x;
				$wmax = ($w-2*$this->cMargin)*1000/$this->FontSize;
			}
			$nl++;
		}
		else
			$i++;
	}
	// Last chunk
	if($i!=$j)
		$this->Cell($l/1000*$this->FontSize,$h,substr($s,$j),0,0,'',0,$link);
}

function Ln($h=null)
{
	// Line feed; default value is last cell height
	$this->x = $this->lMargin;
	if($h===null)
		$this->y += $this->lasth;
	else
		$this->y += $h;
}

function Image($file, $x=null, $y=null, $w=0, $h=0, $type='', $link='')
{
	// Put an image on the page
	if(!isset($this->images[$file]))
	{
		// First use of this image, get info
		if($type=='')
		{
			$pos = strrpos($file,'.');
			if(!$pos)
				$this->Error('Image file has no extension and no type was specified: '.$file);
			$type = substr($file,$pos+1);
		}
		$type = strtolower($type);
		if($type=='jpeg')
			$type = 'jpg';
		$mtd = '_parse'.$type;
		if(!method_exists($this,$mtd))
			$this->Error('Unsupported image type: '.$type);
		$info = $this->$mtd($file);
		$info['i'] = count($this->images)+1;
		$this->images[$file] = $info;
	}
	else
		$info = $this->images[$file];

	// Automatic width and height calculation if needed
	if($w==0 && $h==0)
	{
		// Put image at 96 dpi
		$w = -96;
		$h = -96;
	}
	if($w<0)
		$w = -$info['w']*72/$w/$this->k;
	if($h<0)
		$h = -$info['h']*72/$h/$this->k;
	if($w==0)
		$w = $h*$info['w']/$info['h'];
	if($h==0)
		$h = $w*$info['h']/$info['w'];

	// Flowing mode
	if($y===null)
	{
		if($this->y+$h>$this->PageBreakTrigger && !$this->InHeader && !$this->InFooter && $this->AcceptPageBreak())
		{
			// Automatic page break
			$x2 = $this->x;
			$this->AddPage($this->CurOrientation,$this->CurPageSize);
			$this->x = $x2;
		}
		$y = $this->y;
		$this->y += $h;
	}

	if($x===null)
		$x = $this->x;
	$this->_out(sprintf('q %.2F 0 0 %.2F %.2F %.2F cm /I%d Do Q',$w*$this->k,$h*$this->k,$x*$this->k,($this->h-($y+$h))*$this->k,$info['i']));
	if($link)
		$this->Link($x,$y,$w,$h,$link);
}

function GetX()
{
	// Get x position
	return $this->x;
}

function SetX($x)
{
	// Set x position
	if($x>=0)
		$this->x = $x;
	else
		$this->x = $this->w+$x;
}

function GetY()
{
	// Get y position
	return $this->y;
}

function SetY($y)
{
	// Set y position and reset x
	$this->x = $this->lMargin;
	if($y>=0)
		$this->y = $y;
	else
		$this->y = $this->h+$y;
}

function SetXY($x, $y)
{
	// Set x and y positions
	$this->SetY($y);
	$this->SetX($x);
}

function Output($name='', $dest='')
{
	// Output PDF to some destination
	if($this->state<3)
		$this->Close();
	$dest = strtoupper($dest);
	if($dest=='')
	{
		if($name=='')
		{
			$name = 'doc.pdf';
			$dest = 'I';
		}
		else
			$dest = 'F';
	}
	switch($dest)
	{
		case 'I':
			// Send to standard output
			$this->_checkoutput();
			if(PHP_SAPI!='cli')
			{
				// We send to a browser
				header('Content-Type: application/pdf');
				header('Content-Disposition: inline; filename="'.$name.'"');
				header('Cache-Control: private, max-age=0, must-revalidate');
				header('Pragma: public');
			}
			echo $this->buffer;
			break;
		case 'D':
			// Download file
			$this->_checkoutput();
			header('Content-Type: application/x-download');
			header('Content-Disposition: attachment; filename="'.$name.'"');
			header('Cache-Control: private, max-age=0, must-revalidate');
			header('Pragma: public');
			echo $this->buffer;
			break;
		case 'F':
			// Save to local file
			$f = fopen($name,'wb');
			if(!$f)
				$this->Error('Unable to create output file: '.$name);
			fwrite($f,$this->buffer,strlen($this->buffer));
			fclose($f);
			break;
		case 'S':
			// Return as a string
			return $this->buffer;
		default:
			$this->Error('Incorrect output destination: '.$dest);
	}
	return '';
}

/*******************************************************************************
*                                                                              *
*                              Protected methods                               *
*                                                                              *
*******************************************************************************/
function _dochecks()
{
	// Check availability of %F
	if(sprintf('%.1F',1.0)!='1.0')
		$this->Error('This version of PHP is not supported');
	// Check mbstring overloading
	if(ini_get('mbstring.func_overload') & 2)
		$this->Error('mbstring overloading must be disabled');
	// Ensure runtime magic quotes are disabled
	if(get_magic_quotes_runtime())
		@set_magic_quotes_runtime(0);
}

function _checkoutput()
{
	if(PHP_SAPI!='cli')
	{
		if(headers_sent($file,$line))
			$this->Error("Some data has already been output, can't send PDF file (output started at $file:$line)");
	}
	if(ob_get_length())
	{
		// The output buffer is not empty
		if(preg_match('/^(\xEF\xBB\xBF)?\s*$/',ob_get_contents()))
		{
			// It contains only a UTF-8 BOM and/or whitespace, let's clean it
			ob_clean();
		}
		else
			$this->Error("Some data has already been output, can't send PDF file");
	}
}

function _getpagesize($size)
{
	if(is_string($size))
	{
		$size = strtolower($size);
		if(!isset($this->StdPageSizes[$size]))
			$this->Error('Unknown page size: '.$size);
		$a = $this->StdPageSizes[$size];
		return array($a[0]/$this->k, $a[1]/$this->k);
	}
	else
	{
		if($size[0]>$size[1])
			return array($size[1], $size[0]);
		else
			return $size;
	}
}

function _beginpage($orientation, $size)
{
	$this->page++;
	$this->pages[$this->page] = '';
	$this->state = 2;
	$this->x = $this->lMargin;
	$this->y = $this->tMargin;
	$this->FontFamily = '';
	// Check page size and orientation
	if($orientation=='')
		$orientation = $this->DefOrientation;
	else
		$orientation = strtoupper($orientation[0]);
	if($size=='')
		$size = $this->DefPageSize;
	else
		$size = $this->_getpagesize($size);
	if($orientation!=$this->CurOrientation || $size[0]!=$this->CurPageSize[0] || $size[1]!=$this->CurPageSize[1])
	{
		// New size or orientation
		if($orientation=='P')
		{
			$this->w = $size[0];
			$this->h = $size[1];
		}
		else
		{
			$this->w = $size[1];
			$this->h = $size[0];
		}
		$this->wPt = $this->w*$this->k;
		$this->hPt = $this->h*$this->k;
		$this->PageBreakTrigger = $this->h-$this->bMargin;
		$this->CurOrientation = $orientation;
		$this->CurPageSize = $size;
	}
	if($orientation!=$this->DefOrientation || $size[0]!=$this->DefPageSize[0] || $size[1]!=$this->DefPageSize[1])
		$this->PageSizes[$this->page] = array($this->wPt, $this->hPt);
}

function _endpage()
{
	$this->state = 1;
}

function _loadfont($font)
{
	// Load a font definition file from the font directory
	include($this->fontpath.$font);
	$a = get_defined_vars();
	if(!isset($a['name']))
		$this->Error('Could not include font definition file');
	return $a;
}

function _escape($s)
{
	// Escape special characters in strings
	$s = str_replace('\\','\\\\',$s);
	$s = str_replace('(','\\(',$s);
	$s = str_replace(')','\\)',$s);
	$s = str_replace("\r",'\\r',$s);
	return $s;
}

function _textstring($s)
{
	// Format a text string
	return '('.$this->_escape($s).')';
}

function _UTF8toUTF16($s)
{
	// Convert UTF-8 to UTF-16BE with BOM
	$res = "\xFE\xFF";
	$nb = strlen($s);
	$i = 0;
	while($i<$nb)
	{
		$c1 = ord($s[$i++]);
		if($c1>=224)
		{
			// 3-byte character
			$c2 = ord($s[$i++]);
			$c3 = ord($s[$i++]);
			$res .= chr((($c1 & 0x0F)<<4) + (($c2 & 0x3C)>>2));
			$res .= chr((($c2 & 0x03)<<6) + ($c3 & 0x3F));
		}
		elseif($c1>=192)
		{
			// 2-byte character
			$c2 = ord($s[$i++]);
			$res .= chr(($c1 & 0x1C)>>2);
			$res .= chr((($c1 & 0x03)<<6) + ($c2 & 0x3F));
		}
		else
		{
			// Single-byte character
			$res .= "\0".chr($c1);
		}
	}
	return $res;
}

function _dounderline($x, $y, $txt)
{
	// Underline text
	$up = $this->CurrentFont['up'];
	$ut = $this->CurrentFont['ut'];
	$w = $this->GetStringWidth($txt)+$this->ws*substr_count($txt,' ');
	return sprintf('%.2F %.2F %.2F %.2F re f',$x*$this->k,($this->h-($y-$up/1000*$this->FontSize))*$this->k,$w*$this->k,-$ut/1000*$this->FontSizePt);
}

function _parsejpg($file)
{
	// Extract info from a JPEG file
	$a = getimagesize($file);
	if(!$a)
		$this->Error('Missing or incorrect image file: '.$file);
	if($a[2]!=2)
		$this->Error('Not a JPEG file: '.$file);
	if(!isset($a['channels']) || $a['channels']==3)
		$colspace = 'DeviceRGB';
	elseif($a['channels']==4)
		$colspace = 'DeviceCMYK';
	else
		$colspace = 'DeviceGray';
	$bpc = isset($a['bits']) ? $a['bits'] : 8;
	$data = file_get_contents($file);
	return array('w'=>$a[0], 'h'=>$a[1], 'cs'=>$colspace, 'bpc'=>$bpc, 'f'=>'DCTDecode', 'data'=>$data);
}

function _parsepng($file)
{
	// Extract info from a PNG file
	$f = fopen($file,'rb');
	if(!$f)
		$this->Error('Can\'t open image file: '.$file);
	$info = $this->_parsepngstream($f,$file);
	fclose($f);
	return $info;
}

function _parsepngstream($f, $file)
{
	// Check signature
	if($this->_readstream($f,8)!=chr(137).'PNG'.chr(13).chr(10).chr(26).chr(10))
		$this->Error('Not a PNG file: '.$file);

	// Read header chunk
	$this->_readstream($f,4);
	if($this->_readstream($f,4)!='IHDR')
		$this->Error('Incorrect PNG file: '.$file);
	$w = $this->_readint($f);
	$h = $this->_readint($f);
	$bpc = ord($this->_readstream($f,1));
	if($bpc>8)
		$this->Error('16-bit depth not supported: '.$file);
	$ct = ord($this->_readstream($f,1));
	if($ct==0 || $ct==4)
		$colspace = 'DeviceGray';
	elseif($ct==2 || $ct==6)
		$colspace = 'DeviceRGB';
	elseif($ct==3)
		$colspace = 'Indexed';
	else
		$this->Error('Unknown color type: '.$file);
	if(ord($this->_readstream($f,1))!=0)
		$this->Error('Unknown compression method: '.$file);
	if(ord($this->_readstream($f,1))!=0)
		$this->Error('Unknown filter method: '.$file);
	if(ord($this->_readstream($f,1))!=0)
		$this->Error('Interlacing not supported: '.$file);
	$this->_readstream($f,4);
	$dp = '/Predictor 15 /Colors '.($colspace=='DeviceRGB' ? 3 : 1).' /BitsPerComponent '.$bpc.' /Columns '.$w;

	// Scan chunks looking for palette, transparency and image data
	$pal = '';
	$trns = '';
	$data = '';
	do
	{
		$n = $this->_readint($f);
		$type = $this->_readstream($f,4);
		if($type=='PLTE')
		{
			// Read palette
			$pal = $this->_readstream($f,$n);
			$this->_readstream($f,4);
		}
		elseif($type=='tRNS')
		{
			// Read transparency info
			$t = $this->_readstream($f,$n);
			if($ct==0)
				$trns = array(ord(substr($t,1,1)));
			elseif($ct==2)
				$trns = array(ord(substr($t,1,1)), ord(substr($t,3,1)), ord(substr($t,5,1)));
			else
			{
				$pos = strpos($t,chr(0));
				if($pos!==false)
					$trns = array($pos);
			}
			$this->_readstream($f,4);
		}
		elseif($type=='IDAT')
		{
			// Read image data block
			$data .= $this->_readstream($f,$n);
			$this->_readstream($f,4);
		}
		elseif($type=='IEND')
			break;
		else
			$this->_readstream($f,$n+4);
	}
	while($n);

	if($colspace=='Indexed' && empty($pal))
		$this->Error('Missing palette in '.$file);
	$info = array('w'=>$w, 'h'=>$h, 'cs'=>$colspace, 'bpc'=>$bpc, 'f'=>'FlateDecode', 'dp'=>$dp, 'pal'=>$pal, 'trns'=>$trns);
	if($ct>=4)
	{
		// Extract alpha channel
		if(!function_exists('gzuncompress'))
			$this->Error('Zlib not available, can\'t handle alpha channel: '.$file);
		$data = gzuncompress($data);
		$color = '';
		$alpha = '';
		if($ct==4)
		{
			// Gray image
			$len = 2*$w;
			for($i=0;$i<$h;$i++)
			{
				$pos = (1+$len)*$i;
				$color .= $data[$pos];
				$alpha .= $data[$pos];
				$line = substr($data,$pos+1,$len);
				$color .= preg_replace('/(.)./s','$1',$line);
				$alpha .= preg_replace('/.(.)/s','$1',$line);
			}
		}
		else
		{
			// RGB image
			$len = 4*$w;
			for($i=0;$i<$h;$i++)
			{
				$pos = (1+$len)*$i;
				$color .= $data[$pos];
				$alpha .= $data[$pos];
				$line = substr($data,$pos+1,$len);
				$color .= preg_replace('/(.{3})./s','$1',$line);
				$alpha .= preg_replace('/.{3}(.)/s','$1',$line);
			}
		}
		unset($data);
		$data = gzcompress($color);
		$info['smask'] = gzcompress($alpha);
		if($this->PDFVersion<'1.4')
			$this->PDFVersion = '1.4';
	}
	$info['data'] = $data;
	return $info;
}

function _readstream($f, $n)
{
	// Read n bytes from stream
	$res = '';
	while($n>0 && !feof($f))
	{
		$s = fread($f,$n);
		if($s===false)
			$this->Error('Error while reading stream');
		$n -= strlen($s);
		$res .= $s;
	}
	if($n>0)
		$this->Error('Unexpected end of stream');
	return $res;
}

function _readint($f)
{
	// Read a 4-byte integer from stream
	$a = unpack('Ni',$this->_readstream($f,4));
	return $a['i'];
}

function _parsegif($file)
{
	// Extract info from a GIF file (via PNG conversion)
	if(!function_exists('imagepng'))
		$this->Error('GD extension is required for GIF support');
	if(!function_exists('imagecreatefromgif'))
		$this->Error('GD has no GIF read support');
	$im = imagecreatefromgif($file);
	if(!$im)
		$this->Error('Missing or incorrect image file: '.$file);
	imageinterlace($im,0);
	$f = @fopen('php://temp','rb+');
	if($f)
	{
		// Perform conversion in memory
		ob_start();
		imagepng($im);
		$data = ob_get_clean();
		imagedestroy($im);
		fwrite($f,$data);
		rewind($f);
		$info = $this->_parsepngstream($f,$file);
		fclose($f);
	}
	else
	{
		// Use temporary file
		$tmp = tempnam('.','gif');
		if(!$tmp)
			$this->Error('Unable to create a temporary file');
		if(!imagepng($im,$tmp))
			$this->Error('Error while saving to temporary file');
		imagedestroy($im);
		$info = $this->_parsepng($tmp);
		unlink($tmp);
	}
	return $info;
}

function _newobj()
{
	// Begin a new object
	$this->n++;
	$this->offsets[$this->n] = strlen($this->buffer);
	$this->_out($this->n.' 0 obj');
}

function _putstream($s)
{
	$this->_out('stream');
	$this->_out($s);
	$this->_out('endstream');
}

function _out($s)
{
	// Add a line to the document
	if($this->state==2)
		$this->pages[$this->page] .= $s."\n";
	else
		$this->buffer .= $s."\n";
}

function _putpages()
{
	$nb = $this->page;
	if(!empty($this->AliasNbPages))
	{
		// Replace number of pages
		for($n=1;$n<=$nb;$n++)
			$this->pages[$n] = str_replace($this->AliasNbPages,$nb,$this->pages[$n]);
	}
	if($this->DefOrientation=='P')
	{
		$wPt = $this->DefPageSize[0]*$this->k;
		$hPt = $this->DefPageSize[1]*$this->k;
	}
	else
	{
		$wPt = $this->DefPageSize[1]*$this->k;
		$hPt = $this->DefPageSize[0]*$this->k;
	}
	$filter = ($this->compress) ? '/Filter /FlateDecode ' : '';
	for($n=1;$n<=$nb;$n++)
	{
		// Page
		$this->_newobj();
		$this->_out('<</Type /Page');
		$this->_out('/Parent 1 0 R');
		if(isset($this->PageSizes[$n]))
			$this->_out(sprintf('/MediaBox [0 0 %.2F %.2F]',$this->PageSizes[$n][0],$this->PageSizes[$n][1]));
		$this->_out('/Resources 2 0 R');
		if(isset($this->PageLinks[$n]))
		{
			// Links
			$annots = '/Annots [';
			foreach($this->PageLinks[$n] as $pl)
			{
				$rect = sprintf('%.2F %.2F %.2F %.2F',$pl[0],$pl[1],$pl[0]+$pl[2],$pl[1]-$pl[3]);
				$annots .= '<</Type /Annot /Subtype /Link /Rect ['.$rect.'] /Border [0 0 0] ';
				if(is_string($pl[4]))
					$annots .= '/A <</S /URI /URI '.$this->_textstring($pl[4]).'>>>>';
				else
				{
					$l = $this->links[$pl[4]];
					$h = isset($this->PageSizes[$l[0]]) ? $this->PageSizes[$l[0]][1] : $hPt;
					$annots .= sprintf('/Dest [%d 0 R /XYZ 0 %.2F null]>>',1+2*$l[0],$h-$l[1]*$this->k);
				}
			}
			$this->_out($annots.']');
		}
		if($this->PDFVersion>'1.3')
			$this->_out('/Group <</Type /Group /S /Transparency /CS /DeviceRGB>>');
		$this->_out('/Contents '.($this->n+1).' 0 R>>');
		$this->_out('endobj');
		// Page content
		$p = ($this->compress) ? gzcompress($this->pages[$n]) : $this->pages[$n];
		$this->_newobj();
		$this->_out('<<'.$filter.'/Length '.strlen($p).'>>');
		$this->_putstream($p);
		$this->_out('endobj');
	}
	// Pages root
	$this->offsets[1] = strlen($this->buffer);
	$this->_out('1 0 obj');
	$this->_out('<</Type /Pages');
	$kids = '/Kids [';
	for($i=0;$i<$nb;$i++)
		$kids .= (3+2*$i).' 0 R ';
	$this->_out($kids.']');
	$this->_out('/Count '.$nb);
	$this->_out(sprintf('/MediaBox [0 0 %.2F %.2F]',$wPt,$hPt));
	$this->_out('>>');
	$this->_out('endobj');
}

function _putfonts()
{
	$nf = $this->n;
	foreach($this->diffs as $diff)
	{
		// Encodings
		$this->_newobj();
		$this->_out('<</Type /Encoding /BaseEncoding /WinAnsiEncoding /Differences ['.$diff.']>>');
		$this->_out('endobj');
	}
	foreach($this->FontFiles as $file=>$info)
	{
		// Font file embedding
		$this->_newobj();
		$this->FontFiles[$file]['n'] = $this->n;
		$font = file_get_contents($this->fontpath.$file,true);
		if(!$font)
			$this->Error('Font file not found: '.$file);
		$compressed = (substr($file,-2)=='.z');
		if(!$compressed && isset($info['length2']))
			$font = substr($font,6,$info['length1']).substr($font,6+$info['length1']+6,$info['length2']);
		$this->_out('<</Length '.strlen($font));
		if($compressed)
			$this->_out('/Filter /FlateDecode');
		$this->_out('/Length1 '.$info['length1']);
		if(isset($info['length2']))
			$this->_out('/Length2 '.$info['length2'].' /Length3 0');
		$this->_out('>>');
		$this->_putstream($font);
		$this->_out('endobj');
	}
	foreach($this->fonts as $k=>$font)
	{
		// Font objects
		$this->fonts[$k]['n'] = $this->n+1;
		$type = $font['type'];
		$name = $font['name'];
		if($type=='Core')
		{
			// Core font
			$this->_newobj();
			$this->_out('<</Type /Font');
			$this->_out('/BaseFont /'.$name);
			$this->_out('/Subtype /Type1');
			if($name!='Symbol' && $name!='ZapfDingbats')
				$this->_out('/Encoding /WinAnsiEncoding');
			$this->_out('>>');
			$this->_out('endobj');
		}
		elseif($type=='Type1' || $type=='TrueType')
		{
			// Additional Type1 or TrueType/OpenType font
			$this->_newobj();
			$this->_out('<</Type /Font');
			$this->_out('/BaseFont /'.$name);
			$this->_out('/Subtype /'.$type);
			$this->_out('/FirstChar 32 /LastChar 255');
			$this->_out('/Widths '.($this->n+1).' 0 R');
			$this->_out('/FontDescriptor '.($this->n+2).' 0 R');
			if(isset($font['diffn']))
				$this->_out('/Encoding '.($nf+$font['diffn']).' 0 R');
			else
				$this->_out('/Encoding /WinAnsiEncoding');
			$this->_out('>>');
			$this->_out('endobj');
			// Widths
			$this->_newobj();
			$cw = &$font['cw'];
			$s = '[';
			for($i=32;$i<=255;$i++)
				$s .= $cw[chr($i)].' ';
			$this->_out($s.']');
			$this->_out('endobj');
			// Descriptor
			$this->_newobj();
			$s = '<</Type /FontDescriptor /FontName /'.$name;
			foreach($font['desc'] as $k=>$v)
				$s .= ' /'.$k.' '.$v;
			if(!empty($font['file']))
				$s .= ' /FontFile'.($type=='Type1' ? '' : '2').' '.$this->FontFiles[$font['file']]['n'].' 0 R';
			$this->_out($s.'>>');
			$this->_out('endobj');
		}
		else
		{
			// Allow for additional types
			$mtd = '_put'.strtolower($type);
			if(!method_exists($this,$mtd))
				$this->Error('Unsupported font type: '.$type);
			$this->$mtd($font);
		}
	}
}

function _putimages()
{
	foreach(array_keys($this->images) as $file)
	{
		$this->_putimage($this->images[$file]);
		unset($this->images[$file]['data']);
		unset($this->images[$file]['smask']);
	}
}

function _putimage(&$info)
{
	$this->_newobj();
	$info['n'] = $this->n;
	$this->_out('<</Type /XObject');
	$this->_out('/Subtype /Image');
	$this->_out('/Width '.$info['w']);
	$this->_out('/Height '.$info['h']);
	if($info['cs']=='Indexed')
		$this->_out('/ColorSpace [/Indexed /DeviceRGB '.(strlen($info['pal'])/3-1).' '.($this->n+1).' 0 R]');
	else
	{
		$this->_out('/ColorSpace /'.$info['cs']);
		if($info['cs']=='DeviceCMYK')
			$this->_out('/Decode [1 0 1 0 1 0 1 0]');
	}
	$this->_out('/BitsPerComponent '.$info['bpc']);
	if(isset($info['f']))
		$this->_out('/Filter /'.$info['f']);
	if(isset($info['dp']))
		$this->_out('/DecodeParms <<'.$info['dp'].'>>');
	if(isset($info['trns']) && is_array($info['trns']))
	{
		$trns = '';
		for($i=0;$i<count($info['trns']);$i++)
			$trns .= $info['trns'][$i].' '.$info['trns'][$i].' ';
		$this->_out('/Mask ['.$trns.']');
	}
	if(isset($info['smask']))
		$this->_out('/SMask '.($this->n+1).' 0 R');
	$this->_out('/Length '.strlen($info['data']).'>>');
	$this->_putstream($info['data']);
	$this->_out('endobj');
	// Soft mask
	if(isset($info['smask']))
	{
		$dp = '/Predictor 15 /Colors 1 /BitsPerComponent 8 /Columns '.$info['w'];
		$smask = array('w'=>$info['w'], 'h'=>$info['h'], 'cs'=>'DeviceGray', 'bpc'=>8, 'f'=>$info['f'], 'dp'=>$dp, 'data'=>$info['smask']);
		$this->_putimage($smask);
	}
	// Palette
	if($info['cs']=='Indexed')
	{
		$filter = ($this->compress) ? '/Filter /FlateDecode ' : '';
		$pal = ($this->compress) ? gzcompress($info['pal']) : $info['pal'];
		$this->_newobj();
		$this->_out('<<'.$filter.'/Length '.strlen($pal).'>>');
		$this->_putstream($pal);
		$this->_out('endobj');
	}
}

function _putxobjectdict()
{
	foreach($this->images as $image)
		$this->_out('/I'.$image['i'].' '.$image['n'].' 0 R');
}

function _putresourcedict()
{
	$this->_out('/ProcSet [/PDF /Text /ImageB /ImageC /ImageI]');
	$this->_out('/Font <<');
	foreach($this->fonts as $font)
		$this->_out('/F'.$font['i'].' '.$font['n'].' 0 R');
	$this->_out('>>');
	$this->_out('/XObject <<');
	$this->_putxobjectdict();
	$this->_out('>>');
}

function _putresources()
{
	$this->_putfonts();
	$this->_putimages();
	// Resource dictionary
	$this->offsets[2] = strlen($this->buffer);
	$this->_out('2 0 obj');
	$this->_out('<<');
	$this->_putresourcedict();
	$this->_out('>>');
	$this->_out('endobj');
}

function _putinfo()
{
	$this->_out('/Producer '.$this->_textstring('FPDF '.FPDF_VERSION));
	if(!empty($this->title))
		$this->_out('/Title '.$this->_textstring($this->title));
	if(!empty($this->subject))
		$this->_out('/Subject '.$this->_textstring($this->subject));
	if(!empty($this->author))
		$this->_out('/Author '.$this->_textstring($this->author));
	if(!empty($this->keywords))
		$this->_out('/Keywords '.$this->_textstring($this->keywords));
	if(!empty($this->creator))
		$this->_out('/Creator '.$this->_textstring($this->creator));
	$this->_out('/CreationDate '.$this->_textstring('D:'.@date('YmdHis')));
}

function _putcatalog()
{
	$this->_out('/Type /Catalog');
	$this->_out('/Pages 1 0 R');
	if($this->ZoomMode=='fullpage')
		$this->_out('/OpenAction [3 0 R /Fit]');
	elseif($this->ZoomMode=='fullwidth')
		$this->_out('/OpenAction [3 0 R /FitH null]');
	elseif($this->ZoomMode=='real')
		$this->_out('/OpenAction [3 0 R /XYZ null null 1]');
	elseif(!is_string($this->ZoomMode))
		$this->_out('/OpenAction [3 0 R /XYZ null null '.sprintf('%.2F',$this->ZoomMode/100).']');
	if($this->LayoutMode=='single')
		$this->_out('/PageLayout /SinglePage');
	elseif($this->LayoutMode=='continuous')
		$this->_out('/PageLayout /OneColumn');
	elseif($this->LayoutMode=='two')
		$this->_out('/PageLayout /TwoColumnLeft');
}

function _putheader()
{
	$this->_out('%PDF-'.$this->PDFVersion);
}

function _puttrailer()
{
	$this->_out('/Size '.($this->n+1));
	$this->_out('/Root '.$this->n.' 0 R');
	$this->_out('/Info '.($this->n-1).' 0 R');
}

function _enddoc()
{
	$this->_putheader();
	$this->_putpages();
	$this->_putresources();
	// Info
	$this->_newobj();
	$this->_out('<<');
	$this->_putinfo();
	$this->_out('>>');
	$this->_out('endobj');
	// Catalog
	$this->_newobj();
	$this->_out('<<');
	$this->_putcatalog();
	$this->_out('>>');
	$this->_out('endobj');
	// Cross-ref
	$o = strlen($this->buffer);
	$this->_out('xref');
	$this->_out('0 '.($this->n+1));
	$this->_out('0000000000 65535 f ');
	for($i=1;$i<=$this->n;$i++)
		$this->_out(sprintf('%010d 00000 n ',$this->offsets[$i]));
	// Trailer
	$this->_out('trailer');
	$this->_out('<<');
	$this->_puttrailer();
	$this->_out('>>');
	$this->_out('startxref');
	$this->_out($o);
	$this->_out('%%EOF');
	$this->state = 3;
}
// End of class
}

// Handle special IE contype request
if(isset($_SERVER['HTTP_USER_AGENT']) && $_SERVER['HTTP_USER_AGENT']=='contype')
{
	header('Content-Type: application/pdf');
	exit;
}

?>


File: /halaman\data_limitasi.php
<?php 
	$API->write("/ip/hotspot/user/profile/print");   
	$g = $API->read(); 
?>
<div class="span9">
            <h3 class="page-title">Daftar Group Limitasi Bandwidth Hotspot</h3>

<div class="well">
<?php if (count($g)>=1) {?>
    <table class="table">
      <thead>
        <tr>
          <th>No</th>
          <th>Nama Group</th>
          <th>Jml Pengguna (Shared User)</th>
          <th>Rate Limit (Rx/Tx)</th>
          <th style="width: 26px;">Aksi</th>
        </tr>
      </thead>
      <tbody>
		<?php 	
		$i=1;
		foreach($g as $tampil){ ?>	  
        <tr>
          <td><?php echo $i; ?></td>
          <td><?php echo $tampil['name']; ?></td>
          <td><?php echo $tampil['shared-users']; ?></td>
          <td><?php echo $tampil['rate-limit']; ?></td>
          <td>
              <a href="index.php?halaman=edit_group_limitasi&id=<?php echo $tampil['.id']; ?>"><i class="icon-pencil"></i></a>
              <a href="#" id="<?php echo $tampil['.id']; ?>" svn="<?php echo $tampil['name']; ?>" class="hapus" role="button" data-toggle="modal"><i class="icon-trash"></i></a>
          </td>
        </tr>
       	<?php 
			$i++;
			} 
		$API->disconnect();   
		?>
      </tbody>
    </table>
	<?php } else {echo "<b style='color:red'>Data Group Limitasi Bandwidth Hotspot Tidak ada <a href='index.php' title='Klik Untuk Kembali ke Halaman Utama'>Kembali</a></b>";} ?>
</div>

</div>

<script src="aksi/js/limitasi/hapus.js"></script>

<div class="modal small hide fade" id="myModal" tabindex="-1" role="dialog" aria-labelledby="myModalLabel" aria-hidden="true">
    <div class="modal-header">
        <button type="button" class="close" data-dismiss="modal" aria-hidden="true">×</button>
        <h3 id="myModalLabel">Konfirmasi</h3>
    </div>
    <div class="modal-body">
		<input type="hidden" id="idnya" name="idnya"/>
        <p class="error-text"></p>
    </div>
    <div class="modal-footer">
        <button class="btn" data-dismiss="modal" aria-hidden="true">Batal</button>
        <button class="btn btn-danger" id="hapus">Hapus!</button>
		<img src="images/loading.gif" id="lproses" class="load"/>
    </div>
</div>


File: /halaman\data_user_aktif.php
<?php 
	$API->write("/ip/hotspot/active/print");   
	$a = $API->read(); 
?>
<div class="span9">
            <h3 class="page-title">Daftar User Hotspot Sedang Aktif</h3>

<div class="well">
<?php if (count($a)>=1) {?>
    <table class="table">
      <thead>
        <tr>
          <th>No</th>
          <th>Nama User</th>
          <th>Address</th>
          <th>UpTime</th>
          <th>Mac-Address</th>
          <th>Login-Menggunakan</th>
        </tr>
      </thead>
      <tbody>
		<?php 	
		$i=1;
		foreach($a as $tampil){ ?>	  
        <tr>
          <td><?php echo $i; ?></td>
          <td><?php echo $tampil['user']; ?></td>
          <td><?php echo $tampil['address']; ?></td>
          <td><?php echo $tampil['uptime']; ?></td>
          <td><?php echo $tampil['mac-address']; ?></td>
          <td><?php echo $tampil['login-by']; ?></td>
        </tr>
		<?php 
			$i++;
			} 
		$API->disconnect();   
		?>
      </tbody>
    </table>
	<?php } else {echo "<b style='color:red'>Tidak ada user hotspot yang sedang aktif <a href='index.php' title='Klik Untuk Kembali ke Halaman Utama'>Kembali</a></b>";} ?>
</div>

</div>


File: /halaman\data_user_hotspot.php
<?php 

	function cariprofile($API,$namaprof){
		
		$API->write("/ip/hotspot/user/profile/print",false);   
		$API->write("?name=".$namaprof,true);   
		$p = $API->read(); 
	
		foreach($p as $tam){
		$nama = $tam['name'];
		$lm = $tam['rate-limit'];
		}
		
		$limitbw = $nama." (".$lm.")";	
		
		echo $limitbw;
	}
	
	$API->write("/ip/hotspot/user/print");   
	$uh = $API->read(); 
?>
<div class="span9">
            <h3 class="page-title">Daftar User Hotspot Mikrotik (<?php echo count($uh)." Buah"; ?>)</h3>
<?php if (count($uh)>=1) {?>
<div class="btn-toolbar">
    <button class="btn btn-primary export"> Export User (*.xls)</button>
    <button class="btn cetak">Cetak User (*.pdf)</button>
    <button class="btn btn-danger resetc">Clear Counter</button>
    <button class="btn btn-warning hapussuser">Hapus Semua User</button>
	<img src="images/loading.gif" id="lprosesc" class="load" style="padding-left:10px">
  <div class="btn-group">
  </div>
</div>

<script src="aksi/js/userhotspot/hapus.js"></script>

<div class="modal small hide fade" id="myModal" tabindex="-1" role="dialog" aria-labelledby="myModalLabel" aria-hidden="true">
    <div class="modal-header">
        <button type="button" class="close" data-dismiss="modal" aria-hidden="true">×</button>
        <h3 id="myModalLabel">Konfirmasi</h3>
    </div>
    <div class="modal-body">
		<input type="hidden" id="idnya" name="idnya"/>
		<input type="hidden" id="idc" name="idc"/>
        <p class="error-text"></p>
    </div>
    <div class="modal-footer">
        <button class="btn" data-dismiss="modal" aria-hidden="true">Batal</button>
        <button class="btn btn-danger" id="hapus">Hapus!</button>
        <button class="btn btn-danger" id="cc">Hapus Counter!</button>
        <button class="btn btn-danger" id="hapuss">Ya. Hapus Semua!</button>
        <button class="btn btn-danger" id="resetc">Ya. Reset Counter!</button>
		<img src="images/loading.gif" id="lprosesh" class="load"/>
    </div>
</div>
<?php } ?>

<div class="well">
<?php if (count($uh)>=1) {?>
    <table class="table">
      <thead>
        <tr>
          <th>No</th>
          <th>Nama User</th>
          <th>Password</th>
          <th>Limit Waktu</th>
          <th>Group Limit Bandwidth</th>
          <th>Keterangan</th>
          <th>Uptime</th>
          <th style="width: 26px;">Aksi</th>
        </tr>
      </thead>
      <tbody>
      <?php 
			$banyakData = count($uh);  
			
  		    $page = isset($_GET['data_ke']) ? $_GET['data_ke'] : 0;
			
			$no = 1;
			$limit = 10;  
			$stop = $page * $limit; 
			$lanjut = $stop + $limit;
			
			$API->write("/ip/hotspot/user/print");   
			$cetakuser = $API->read(); 
			
			foreach($cetakuser as $tampil){
				
				if ( $page == 0 ){ ?>
				<tr <?php if ($tampil['limit-uptime']==$tampil['uptime']){ echo "style='background-color:red'"; }?>> 
    				<td><?php echo $no; ?></td> 
					<td><?php echo $tampil['name']; ?></td>
					<td><?php echo $tampil['password']; ?></td>
					<td><?php echo @$tampil['limit-uptime']; ?></td>
					<td><?php echo cariprofile($API,$tampil['profile']); ?></td>
					<td><?php echo $tampil['comment']; ?></td>
					<td><?php echo $tampil['uptime']; ?></td>
					<td>
						<a href="index.php?halaman=edit_user_hotspot&id=<?php echo $tampil['.id']; ?>" title="Edit User"><i class="icon-pencil"></i></a>
						<a href="#" id="<?php echo $tampil['.id']; ?>" svn="<?php echo $tampil['name']; ?>" class="hapus" role="button" data-toggle="modal" title="Hapus User"><i class="icon-trash"></i></a>
						<a href="#" id="<?php echo $tampil['.id']; ?>" svn="<?php echo $tampil['name']; ?>" class="ccounter" role="button" data-toggle="modal" title="Clear Counter"><i class="icon-remove"></i></a>
					</td>
    			</tr> 	
					
				<?php 
					if ($no == 10){ break; }
				} else if ( empty ( $page ) ){ ?>
				<tr <?php if ($tampil['limit-uptime']==$tampil['uptime']){ echo "style='background-color:red'"; }?>> 
    				<td><?php echo $no; ?></td> 
					<td><?php echo $tampil['name']; ?></td>
					<td><?php echo $tampil['password']; ?></td>
					<td><?php echo @$tampil['limit-uptime']; ?></td>
					<td><?php echo cariprofile($API,$tampil['profile']); ?></td>
					<td><?php echo $tampil['comment']; ?></td>
					<td><?php echo $tampil['uptime']; ?></td>
					<td>
						<a href="index.php?halaman=edit_user_hotspot&id=<?php echo $tampil['.id']; ?>" title="Edit User"><i class="icon-pencil"></i></a>
						<a href="#" id="<?php echo $tampil['.id']; ?>" svn="<?php echo $tampil['name']; ?>" class="hapus" role="button" data-toggle="modal" title="Hapus User"><i class="icon-trash"></i></a>
						<a href="#" id="<?php echo $tampil['.id']; ?>" svn="<?php echo $tampil['name']; ?>" class="ccounter" role="button" data-toggle="modal" title="Clear Counter"><i class="icon-remove"></i></a>
					</td>
    			</tr> 
				<?php
				if ($no == $stop){ break; }
				} else { 
				if ($no > $stop){
				?>
				<tr <?php if ($tampil['limit-uptime']==$tampil['uptime']){ echo "style='background-color:red'"; }?>> 
    				<td><?php echo $no; ?></td> 
					<td><?php echo $tampil['name']; ?></td>
					<td><?php echo $tampil['password']; ?></td>
					<td><?php echo @$tampil['limit-uptime']; ?></td>
					<td><?php echo cariprofile($API,$tampil['profile']); ?></td>
					<td><?php echo $tampil['comment']; ?></td>
					<td><?php echo $tampil['uptime']; ?></td>
					<td>
					  <a href="index.php?halaman=edit_user_hotspot&id=<?php echo $tampil['.id']; ?>"><i class="icon-pencil" title="Edit User"></i></a>
					  <a href="#" id="<?php echo $tampil['.id']; ?>" svn="<?php echo $tampil['name']; ?>" class="hapus" role="button" data-toggle="modal" title="Hapus User"><i class="icon-trash"></i></a>
					  <a href="#" id="<?php echo $tampil['.id']; ?>" svn="<?php echo $tampil['name']; ?>" class="ccounter" role="button" data-toggle="modal" title="Clear Counter"><i class="icon-remove"></i></a>
					</td>					
    			</tr> 
				<?php
				if ($no == $lanjut){ break; }
				}
				}
				$no++;
			}
			$API->disconnect();
			?>
      </tbody>
    </table>
	
		<?php } else { echo "<b style='color:red'>Data User Hotspot Tidak ada <a href='index.php' title='Klik Untuk Kembali ke Halaman Utama'>Kembali</a></b>";} ?>
</div>
 
			<?php 
				if (count($uh)>10) {
				
				$banyakHalaman = ceil($banyakData / $limit);  
				$banyak = $banyakHalaman - 1;
				echo "<div class='pagination'><center>";  
					for($i = 0; $i <= $banyak; $i++){  

						if ($page != $i){  
						
							echo "<a class='page";
							if ($page == $i){ echo "active"; }
							echo "$aktif' href='index.php?halaman=daftar_user_hotspot&data_ke=".$i."'>".$i."</a>";
						
						} else {   
						
							echo "<a class='page";
							if ($page == $i){ echo " active"; }
							echo "$aktif' href='index.php?halaman=daftar_user_hotspot&data_ke=".$i."'>".$i."</a>";

						}  
				}	
				echo "</center></div>"; 
				}
			?>

</div>




File: /halaman\data_user_mikrotik.php
<?php 
	$API->write("/user/print");   
	$u = $API->read(); 
?>
<div class="span9">
            <h3 class="page-title">Daftar User Mikrotik</h3>
<div class="btn-toolbar">
    <button class="btn btn-success"><a href="index.php?halaman=tambah_user_mikrotik" style="color:white">Tambah User [+]</a></button>
  <div class="btn-group">
  </div>
</div>

<div class="well">
<?php if (count($u)>=1) {?>
    <table class="table">
      <thead>
        <tr>
          <th>No</th>
          <th>Nama</th>
          <th>Group</th>
          <th>Keterangan</th>
          <th style="width: 26px;">Aksi</th>
        </tr>
      </thead>
      <tbody>
		<?php 	
		$i=1;
		foreach($u as $tampil){ ?>	  
        <tr>
          <td><?php echo $i; ?></td>
          <td><?php echo $tampil['name']; ?></td>
          <td><?php echo $tampil['group']; ?></td>
          <td><?php echo $tampil['comment']; ?></td>
          <td>
              <a href="#" id="<?php echo $tampil['.id']; ?>" svn="<?php echo $tampil['name']; ?>" role="button" class="hapus" data-toggle="modal"><i class="icon-trash"></i></a>
          </td>
        </tr>
		<?php 
			$i++;
			} 
		$API->disconnect();   
		?>
	  </tbody>
    </table>
	<?php } else {echo "<b style='color:red'>Data User Mikrotik Tidak ada <a href='index.php' title='Klik Untuk Kembali ke Halaman Utama'>Kembali</a></b>";} ?>
</div>


</div>

<script src="aksi/js/usermikrotik/hapus.js"></script>

<div class="modal small hide fade" id="myModal" tabindex="-1" role="dialog" aria-labelledby="myModalLabel" aria-hidden="true">
    <div class="modal-header">
        <button type="button" class="close" data-dismiss="modal" aria-hidden="true">×</button>
        <h3 id="myModalLabel">Konfirmasi</h3>
    </div>
    <div class="modal-body">
		<input type="hidden" id="idnya" name="idnya"/>
        <p class="error-text"></p>
    </div>
    <div class="modal-footer">
        <button class="btn" data-dismiss="modal" aria-hidden="true">Batal</button>
        <button class="btn btn-danger" id="hapus">Hapus!</button>
		<img src="images/loading.gif" id="lproses" class="load"/>
    </div>
</div>


File: /halaman\edit_identity_mikrotik.php
	<?php   
	   $API->write("/system/identity/print");   
	   $id = $API->read(); 
	   foreach($id as $tampil){
		$iden = $tampil['name'];
	   }   
	?>
<div class="span9">
       <h3 class="page-title">Edit Identity Mikrotik</h3>
<div class="well">

    <form id="giden" action="" method="post">
	    <label>Identity</label>
        <input type="text" id="iden" value="<?php echo $iden; ?>" name="iden" class="input-xlarge required">
        <div>
		 <input class="btn btn-primary" type="submit" name="submit" value="Ganti">
			<img src="images/loading.gif" id="lproses" class="load"/>
			<button class="btn"><a href="index.php" style="color:black">Kembali</a></button>
        </div>
    </form>


</div>

<script src="aksi/js/editiden/editiden.js"></script>

</div>

<div class="modal small hide fade" id="myModal" tabindex="-1" role="dialog" aria-labelledby="myModalLabel" aria-hidden="true">
  <div class="modal-header">
    <button type="button" class="close tutup" data-dismiss="modal" aria-hidden="true">×</button>
    <h3 id="myModalLabel">Perhatian</h3>
  </div>
  <div class="modal-body">
    
    <p class="error-text"></p>
  </div>
  <div class="modal-footer">
    <button class="btn tutup" data-dismiss="modal" aria-hidden="true">Tutup</button>
  </div>
</div>
   

File: /halaman\edit_password_mikrotik.php
<div class="span9">
       <h3 class="page-title">Edit Password Mikrotik</h3>
<div class="well">

    <form id="gpass" action="" method="post">
	    <label>Password Lama</label>
        <input type="password" id="passl" name="passl" class="input-xlarge">
        <label>Password Baru</label>
        <input type="password" id="passb" name="passb" class="input-xlarge required">
        <div>
		 <input class="btn btn-primary" type="submit" name="submit" value="Ubah Password">
			<img src="images/loading.gif" id="lproses" class="load"/>
			<button class="btn"><a href="index.php" style="color:black">Kembali</a></button>
        </div>
    </form>


</div>

<script src="aksi/js/editpass/editpass.js"></script>

</div>

<div class="modal small hide fade" id="myModal" tabindex="-1" role="dialog" aria-labelledby="myModalLabel" aria-hidden="true">
  <div class="modal-header">
    <button type="button" class="close" data-dismiss="modal" aria-hidden="true">×</button>
    <h3 id="myModalLabel">Perhatian</h3>
  </div>
  <div class="modal-body">
    
    <p class="error-text"></p>
  </div>
  <div class="modal-footer">
    <button class="btn" data-dismiss="modal" aria-hidden="true">Tutup</button>
  </div>
</div>
   

File: /halaman\generate_user_hotspot.php
<?php 	$API->write("/ip/hotspot/user/profile/print");   
	    $glimit = $API->read(); 
?>
<div class="span9">
       <h3 class="page-title">Generate User Hotspot</h3>

<div class="well">

    <form id="guserhotspot" method="post" action="">
        
		<label>Panjang Nama User</label>
        <select name="puser" id="puser" class="input-large required warna">
			<option value="">-- Pilih --</option>
			<option value="3">3</option>
			<option value="4">4</option>
			<option value="5">5</option>
			<option value="6">6</option>
		</select>	
		<i style="color:green">*) panjang string username</i>
        <label>Panjang Password</label>
        <select name="ppass" id="ppass" class="input-large required warna">
			<option value="">-- Pilih --</option>
			<option value="3">3</option>
			<option value="4">4</option>
			<option value="5">5</option>
			<option value="6">6</option>
		</select>	
		<i style="color:green">*) panjang string password</i>
        <label>Group Limitasi Bandwidth</label>
        <select name="glimit" id="glimit" class="input-large required warna">
			<option value="">-- Pilih --</option>
			<?php 
				foreach($glimit as $g){
					?>
			<option value="<?php echo $g['name'];?>"><?php echo $g['name']." (".$g['rate-limit'].")"; ?></option>
			<?php } ?>
		</select>
        <label>Limit Waktu</label>
        <input type="text" id="lwaktu" name="lwaktu" class="input-large required">
		<select name="satuan" id="satuan" class="input-large required warna">
			<option value="">-- Pilih --</option>
			<option value="menit">Menit</option>
			<option value="jam">Jam</option>
			<option value="hari">Hari</option>
		</select>
		<label>Jumlah User</label>
        <select name="juser" id="juser" class="input-large required warna">
			<option value="">-- Pilih --</option>
			<option value="5">5 Buah</option>
			<option value="10">10 Buah</option>
			<option value="20">20 Buah</option>
			<option value="25">25 Buah</option>
			<option value="50">50 Buah</option>
			<option value="75">75 Buah</option>
			<option value="100">100 Buah</option>
			<option value="200">200 Buah</option>
			<option value="250">250 Buah</option>
			<option value="300">300 Buah</option>
			<option value="500">500 Buah</option>
			<option value="1000">1000 Buah</option>
		</select>	
		<i style="color:green">*) jumlah user yang akan digenerate</i>
		<label>Keterangan</label>
        <textarea id="ket" rows="2" class="required" name="ket"></textarea>
		
        <div style="padding-top:20px">
            <input class="btn btn-primary" id="simpan" type="submit" value="Generate User Hotspot">
			<img src="images/loading.gif" class="load" id="lproses"/>
			<button class="btn"><a href="index.php?halaman=daftar_user_hotspot" style="color:black">Kembali</a></button>
		</div>
	</form>
      </div>
  </div>

  <script src="aksi/js/userhotspot/generate.js"></script>
  
<div class="modal small hide fade" id="myModal" tabindex="-1" role="dialog" aria-labelledby="myModalLabel" aria-hidden="true">
  <div class="modal-header">
    <button type="button" class="close" data-dismiss="modal" aria-hidden="true">×</button>
    <h3 id="myModalLabel">Perhatian</h3>
  </div>
  <div class="modal-body">
    
    <p class="error-text"></p>
  </div>
  <div class="modal-footer">
    <button class="btn" data-dismiss="modal" aria-hidden="true">Tutup</button>
  </div>
</div>

   

File: /halaman\profile.php
	<?php   
	   $API->write("/user/group/print");   
	   $g = $API->read(); 
	   
	   $API->write("/user/print",false);   
	   $API->write("?name=".$_SESSION['user'],true);   
	   $p = $API->read(); 
	   foreach($p as $tam){
		$id = $tam['.id'];
		$nama = $tam['name'];
		$group = $tam['group'];
		$komen = $tam['comment'];
	   }
	?>
<div class="span9">
       <h3 class="page-title">Profile User Mikrotik</h3>

<div class="well">

    <form id="profile" action="" method="post">
        <label>Nama User</label>
        <input type="hidden" id="id" value="<?php echo $id; ?>">
        <input type="text" id="nama" value="<?php echo $nama; ?>" name="nama" class="input-xlarge required">
        <label>Group</label>
        <select name="group" id="group" class="input-large warna required">
		<option value="">-- Pilih --</option>
		<?php foreach($g as $tampil){ ?> 
			<option value="<?php echo $tampil['name'];?>" <?php if ($tampil['name']==$group){ echo "selected"; }?>><?php echo $tampil['name']; ?></option>
		<?php } ?>
		</select>
        <label>Keterangan</label>
        <textarea id="ket" name="ket" rows="3" class="required"><?php echo $komen; ?></textarea>
		
        <div style="padding-top:20px">
           <input class="btn btn-primary" id="simpan" type="submit" value="Update Profile">
            <img src="images/loading.gif" id="lproses" class="load"/>
			<button class="btn"><a href="index.php" style="color:black">Kembali</a></button>
        </div>
	</form>
      </div>
  </div>

<script src="aksi/js/profile/update.js"></script>
  
<div class="modal small hide fade" id="myModal" tabindex="-1" role="dialog" aria-labelledby="myModalLabel" aria-hidden="true">
  <div class="modal-header">
    <button type="button" class="close" data-dismiss="modal" aria-hidden="true">×</button>
    <h3 id="myModalLabel">Perhatian</h3>
  </div>
  <div class="modal-body">
    
    <p class="error-text"></p>
  </div>
  <div class="modal-footer">
    <button class="btn" data-dismiss="modal" aria-hidden="true">Tutup</button>
  </div>
</div>

   

File: /halaman\tambah_group_limitasi.php
<?php 
	if(!empty($_GET['id'])){
		$judul = "Edit";
		$id = $_GET['id'];
		$aksi = "update";
		$button = "Update";
	    $API->write("/ip/hotspot/user/profile/print",false);   
	    $API->write("?.id=".$id,true);   
	    $p = $API->read(); 
	    foreach($p as $tam){
			$nama = $tam['name'];
			$share = $tam['shared-users'];
			$limit = $tam['rate-limit'];
	    }
		$pecah = explode("/",$limit);
		if (count($pecah)>1){
			$limitnya = $pecah[0];
			$satuan = $pecah[1];
		} else {
			$limitnya = $pecah[0];
			$satuan = "";
		}
	} else {
		$id = "";
		$aksi = "save";
		$judul = "Tambah";
		$button = "Simpan";
		$limitnya = "";
		$satuan = "";
		$nama = "";
		$share = "";
	}
?>
<div class="span9">
       <h3 class="page-title"><?php echo $judul; ?> Group Limitasi Bandwidth Hotspot</h3>

<div class="well">

    <form id="glimitasi" method="post" action="">
        <label>Nama Group</label>
        <input type="hidden" id="idnya" name="idnya" value="<?php echo $id; ?>">
        <input type="hidden" id="aksi" name="aksi" value="<?php echo $aksi; ?>">
        <input type="text" id="nama" name="nama" value="<?php echo $nama; ?>" class="input-xlarge required">
        <label>Jml Pengguna (Shared User)</label>
        <input type="text" id="share" name="share" value="<?php echo $share; ?>" class="input-xlarge required">
        <label>Limit Bandwidth</label>
        <input type="text" id="limit" value="<?php echo $limitnya; ?>" name="limit" class="input-large required">
		<select name="satuan" id="satuan" class="input-large warna required">
			<option value="">-- Pilih --</option>
			<option value="k" <?php if ($satuan=="k"){ echo "selected"; }?>>Kilobyte</option>
			<option value="m" <?php if ($satuan=="m"){ echo "selected"; }?>>Megabyte</option>
		</select>
		
        <div style="padding-top:20px">
            <input class="btn btn-primary" id="simpan" type="submit" value="<?php echo $button; ?> Group">
            <img src="images/loading.gif" id="lproses" class="load"/>
			<button class="btn"><a href="index.php?halaman=daftar_group_limitasi" style="color:black">Kembali</a></button>
        </div>
	</form>
      </div>
  </div>

 <script src="aksi/js/limitasi/save.js"></script>
  
<div class="modal small hide fade" id="myModal" tabindex="-1" role="dialog" aria-labelledby="myModalLabel" aria-hidden="true">
  <div class="modal-header">
    <button type="button" class="close" data-dismiss="modal" aria-hidden="true">×</button>
    <h3 id="myModalLabel">Perhatian</h3>
  </div>
  <div class="modal-body">
    
    <p class="error-text"></p>
  </div>
  <div class="modal-footer">
    <button class="btn" data-dismiss="modal" aria-hidden="true">Tutup</button>
  </div>
</div>

   

File: /halaman\tambah_user_hotspot.php
<?php $API->write("/ip/hotspot/user/profile/print");   
	  $glimit = $API->read();
		
	if(!empty($_GET['id'])){
		$judul = "Edit";
		$id = $_GET['id'];
		$aksi = "update";
		$button = "Update";
	    $API->write("/ip/hotspot/user/print",false);   
	    $API->write("?.id=".$id,true);   
	    $p = $API->read(); 
	    foreach($p as $tam){
			$user = $tam['name'];
			//$limit = $tam['limit-uptime'];
			$pass = $tam['password'];
			$profile = $tam['profile'];
			$ket = $tam['comment'];
	    }
	//	$pecah = explode(":",$limit);
	//	if (count($pecah)>1){
	//		if ($pecah[0] != "00"){
	//		$limitnya = $pecah[0];
	//		$satuan = "jam";
	//		} else if ($pecah[1] != "00"){
	//		$limitnya = $pecah[1];
	//		$satuan = "menit";
	//		} else if ($pecah[2] != "00"){
	//		$limitnya = $pecah[2];
	//		$satuan = "detik";
	//		}
	//	} else {
	//		$limitnya = "";
	//		$satuan = "";
	//	}
	} else {
		$id = "";
		$aksi = "save";
		$judul = "Tambah";
		$button = "Simpan";
	//	$limitnya = "";
		$user = "";
		$pass = "";
		$ket = "";
		$profile = "";
	}
?>
<div class="span9">
       <h3 class="page-title"><?php echo $judul; ?> User Hotspot</h3>

<div class="well">

    <form id="tuserhotspot" method="post" action="">
        <label>Nama User</label>
        <input type="hidden" id="idnya" value="<?php echo $id; ?>">
        <input type="hidden" id="aksi" value="<?php echo $aksi; ?>">
        <input type="text" id="user" value="<?php echo $user; ?>" name="user" class="input-xlarge required">
        <label>Password</label>
        <input type="password" id="pass" name="pass" value="<?php echo $pass; ?>" class="input-xlarge required">
        <label>Group Limitasi Bandwidth</label>
        <select name="glimit" id="glimit" class="input-large required warna">
			<option value="">-- Pilih --</option>
			<?php 
				foreach($glimit as $g){
					?>
			<option value="<?php echo $g['name'];?>" <?php if ($g['name']==$profile){ echo "selected"; }?>><?php echo $g['name']." (".$g['rate-limit'].")"; ?></option>
			<?php } ?>
		</select>
        <!--<label>Limit Waktu</label>
		<input type="text" id="lwaktu" value="<?php echo $limitnya; ?>" name="lwaktu" class="input-large required">
		<select name="satuan" id="satuan" class="input-large required warna">
			<option value="">-- Pilih --</option>
			<option value="menit" <?php if ($satuan=="menit"){ echo "selected"; }?>>Menit</option>
			<option value="jam" <?php if ($satuan=="jam"){ echo "selected"; }?>>Jam</option>
			<option value="hari" <?php if ($satuan=="hari"){ echo "selected"; }?>>Hari</option>
		</select>-->
		
		<label>Keterangan</label>
        <textarea id="ket" name="ket" rows="2" class="required"><?php echo $ket; ?></textarea>
		
        <div style="padding-top:20px">
            <input class="btn btn-primary" id="simpan" type="submit" value="<?php echo $button; ?> User Hotspot">
			<img src="images/loading.gif" id="lproses" class="load"/>
			<button class="btn"><a href="index.php?halaman=daftar_user_hotspot" style="color:black">Kembali</a></button>
		</div>
	</form>
      </div>
  </div>
 
 <script src="aksi/js/userhotspot/save.js"></script>
 
<div class="modal small hide fade" id="myModal" tabindex="-1" role="dialog" aria-labelledby="myModalLabel" aria-hidden="true">
  <div class="modal-header">
    <button type="button" class="close" data-dismiss="modal" aria-hidden="true">×</button>
    <h3 id="myModalLabel">Perhatian</h3>
  </div>
  <div class="modal-body">
    <p class="error-text"></p>
  </div>
  <div class="modal-footer">
    <button class="btn" data-dismiss="modal" aria-hidden="true">Tutup</button>
  </div>
</div>

   

File: /halaman\tambah_user_mikrotik.php
	<?php   
	   $API->write("/user/group/print");   
	   $g = $API->read(); 
	?>
<div class="span9">
       <h3 class="page-title">Tambah User Mikrotik</h3>
<div class="well">

    <form id="user" method="post" action="">
        <label>Nama User</label>
        <input type="text" id="nama" name="nama" class="input-xlarge required">
        <label>Group</label>
        <select name="group" id="group" class="input-large warna required">
			<option value="">-- Pilih --</option>
		<?php foreach($g as $tampil){ ?> 
			<option value="<?php echo $tampil['name'];?>"><?php echo $tampil['name']; ?></option>
		<?php } ?>
		</select>
        <label>Password</label>
        <input type="password" id="pass" name="pass" class="input-large required">
        <label>Keterangan</label>
        <textarea id="ket" name="ket" rows="3" class="required"></textarea>
		
        <div style="padding-top:20px">
           <input class="btn btn-primary" id="simpan" type="submit" value="Simpan User">
            <img src="images/loading.gif" id="lproses" class="load"/>
			<button class="btn"><a href="index.php?halaman=daftar_user_mikrotik" style="color:black">Kembali</a></button>
        </div>
	</form>
      </div>
  </div>

<script src="aksi/js/usermikrotik/save.js"></script>
  
<div class="modal small hide fade" id="myModal" tabindex="-1" role="dialog" aria-labelledby="myModalLabel" aria-hidden="true">
  <div class="modal-header">
    <button type="button" class="close" data-dismiss="modal" aria-hidden="true">×</button>
    <h3 id="myModalLabel">Perhatian</h3>
  </div>
  <div class="modal-body">
    
    <p class="error-text"></p>
  </div>
  <div class="modal-footer">
    <button class="btn" data-dismiss="modal" aria-hidden="true">Tutup</button>
  </div>
</div>

   

File: /halaman\utama.php
<div class="span9">

	<div class="row-fluid">
		<div class="block">

			<div id="chart-container" class="block-body collapse in">
				<center><img src="images/mikrotik_router.png" title="Aplikasi Generate User Hotspot Mikrotik" width="70%" style="margin-top:16%;margin-bottom:22%"></center>

			</div>
		</div>
	</div>

</div>

File: /index.php
<?php 
	ini_set( "display_errors", 0); 
	session_start();
	// Cek Login
	if (isset($_SESSION['user'])){  
		require_once("penting/koneksi.php"); 
	?>	
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <title>Aplikasi Generate User Hotspot Mikrotik</title>
    <meta content="IE=edge,chrome=1" http-equiv="X-UA-Compatible">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" type="text/css" href="lib/bootstrap/css/bootstrap.css">
    <link rel="stylesheet" type="text/css" href="lib/bootstrap/css/bootstrap-responsive.css">
    <link rel="stylesheet" type="text/css" href="css/theme.css">
    <link rel="stylesheet" href="lib/font-awesome/css/font-awesome.css">
    <script src="lib/jquery-1.8.1.min.js" type="text/javascript"></script>
	<script type="text/javascript" src="lib/jquery.validate.min.js"></script>
    <link rel="shortcut icon" href="images/logo_mikrotik.png">
 </head>

  <body> 
	<script>var $jnoc = jQuery.noConflict();</script>
    
    <div class="navbar">
        <div class="navbar-inner">
            <div class="container-fluid">
                <ul class="nav pull-right">
                    
                    <li id="fat-menu" class="dropdown">
						<a href="#" id="drop3" role="button" class="dropdown-toggle" data-toggle="dropdown">
                            <i class="icon-user"></i> <?php echo $_SESSION['user']; ?>
                            <i class="icon-caret-down"></i>
                        </a>

                        <ul class="dropdown-menu">
                            <li><a tabindex="-1" href="index.php?halaman=profile">Profile User</a></li>
                            <li class="divider"></li>
                            <li><a tabindex="-1" href="logout.php">Logout</a></li>
                        </ul>
                    </li>
                    
                </ul>
                <a class="brand" href="index.php"><span class="first">Aplikasi Generate User Hotspot</span> <span class="second">Mikrotik</span></a>
            </div>
        </div>
    </div>
    

    <div class="container-fluid">
        
        <div class="row-fluid">
            <div class="span3">
                <div class="sidebar-nav">
                  <div class="nav-header" data-toggle="collapse" data-target="#dashboard-menu"><i class="icon-user"></i>Generate User Hotspot</div>
                    <ul id="dashboard-menu" class="nav nav-list collapse in">
                        <li><a href="index.php?halaman=daftar_user_hotspot">Daftar User Hotspot</a></li>
                        <li ><a href="index.php?halaman=daftar_user_aktif">Daftar User Sedang Aktif</a></li>
                        <li ><a href="index.php?halaman=generate_user_hotspot">Generate User Hotspot</a></li>
						<li ><a href="index.php?halaman=tambah_user_hotspot">Tambah User Hotspot</a></li>
                    </ul>

                <div class="nav-header" data-toggle="collapse" data-target="#settings-menu"><i class="icon-dashboard"></i>Group Limit Bandwidth Hotspot</div>
                <ul id="settings-menu" class="nav nav-list collapse in">
                  <li ><a href="index.php?halaman=tambah_group_limitasi">Tambah Group Limitasi Bandwidth</a></li>
                  <li ><a href="index.php?halaman=daftar_group_limitasi">Daftar Group Limitasi Bandwidth</a></li>
                </ul>
				
				<div class="nav-header" data-toggle="collapse" data-target="#accounts-menu"><i class="icon-wrench"></i>Extra Menu</div>
                <ul id="accounts-menu" class="nav nav-list collapse in">
                  <li ><a href="index.php?halaman=daftar_user_mikrotik">Daftar User Mikrotik</a></li>
                  <li ><a href="index.php?halaman=edit_password_mikrotik">Edit Password Mikrotik</a></li>
                  <li ><a href="index.php?halaman=edit_identity_mikrotik">Edit Identity Mikrotik</a></li>
                  <li ><a href="#ModalReboot" role="button" data-toggle="modal">Reboot Mikrotik</a></li>
                </ul>


            </div>
        </div>
      
	  <?php 

			@$hal=$_GET['halaman'];
			if(!$hal){ include "halaman/utama.php"; }
			else {
			switch($hal){
			case "daftar_user_hotspot" : include "halaman/data_user_hotspot.php"; break;
			case "daftar_user_mikrotik" : include "halaman/data_user_mikrotik.php"; break;
			case "daftar_group_limitasi" : include "halaman/data_limitasi.php"; break;
			case "daftar_user_aktif" : include "halaman/data_user_aktif.php"; break;
			case "tambah_user_hotspot" : include "halaman/tambah_user_hotspot.php"; break;
			case "edit_user_hotspot" : include "halaman/tambah_user_hotspot.php"; break;
			case "tambah_user_mikrotik" : include "halaman/tambah_user_mikrotik.php"; break;
			case "generate_user_hotspot" : include "halaman/generate_user_hotspot.php"; break;
			case "tambah_group_limitasi" : include "halaman/tambah_group_limitasi.php"; break;
			case "edit_group_limitasi" : include "halaman/tambah_group_limitasi.php"; break;
			case "edit_password_mikrotik" : include "halaman/edit_password_mikrotik.php"; break;
			case "edit_identity_mikrotik" : include "halaman/edit_identity_mikrotik.php"; break;
			case "reboot_mikrotik" : include "halaman/reboot_mikrotik.php"; break;
			case "profile" : include "halaman/profile.php"; break;
			default : include "halaman/utama.php"; break;
			}
			}
		?>

    </div>  
    
    <footer>
        <hr>
        <p class="pull-right">Aplikasi Generate User Hotspot Mikrotik</p>
        <p>Developed By <a href="#">Mahasiswa STMIK Bumigora Mataram</a></p>
    </footer>

    <script src="lib/bootstrap/js/bootstrap.js"></script>

 <div class="modal small hide fade" id="ModalReboot" tabindex="-1" role="dialog" aria-labelledby="myModalLabel" aria-hidden="true">
  <div class="modal-header">
    <button type="button" class="close" data-dismiss="modal" aria-hidden="true">×</button>
    <h3 id="myModalLabel">Reboot Mikrotik</h3>
  </div>
  <div class="modal-body">
    
    <p class="error-text"><i class="icon-warning-sign modal-icon"></i>Anda yakin akan Me-Reboot Mikrotik ?</p>
  </div>
  <div class="modal-footer">
    <button class="btn" data-dismiss="modal" aria-hidden="true">Batal</button>
    <button class="btn btn-danger" id="reboot" data-dismiss="modal">Ya!</button>
  </div>
</div>
  <script src="aksi/js/reboot/reboot.js"></script>
  </body>
</html>

<?php } else {
		header("location:login.php");
	}
	?>




File: /lib\bootstrap\css\bootstrap.css
/*!
 * Bootstrap v2.2.1
 *
 * Copyright 2012 Twitter, Inc
 * Licensed under the Apache License v2.0
 * http://www.apache.org/licenses/LICENSE-2.0
 *
 * Designed and built with all the love in the world @twitter by @mdo and @fat.
 */
.clearfix {
  *zoom: 1;
}
.clearfix:before,
.clearfix:after {
  display: table;
  content: "";
  line-height: 0;
}
.clearfix:after {
  clear: both;
}
.hide-text {
  font: 0/0 a;
  color: transparent;
  text-shadow: none;
  background-color: transparent;
  border: 0;
}
.input-block-level {
  display: block;
  width: 100%;
  min-height: 30px;
  -webkit-box-sizing: border-box;
  -moz-box-sizing: border-box;
  box-sizing: border-box;
}
article,
aside,
details,
figcaption,
figure,
footer,
header,
hgroup,
nav,
section {
  display: block;
}
audio,
canvas,
video {
  display: inline-block;
  *display: inline;
  *zoom: 1;
}
audio:not([controls]) {
  display: none;
}
html {
  font-size: 100%;
  -webkit-text-size-adjust: 100%;
  -ms-text-size-adjust: 100%;
}
a:focus {
  outline: thin dotted #333;
  outline: 5px auto -webkit-focus-ring-color;
  outline-offset: -2px;
}
a:hover,
a:active {
  outline: 0;
}
sub,
sup {
  position: relative;
  font-size: 75%;
  line-height: 0;
  vertical-align: baseline;
}
sup {
  top: -0.5em;
}
sub {
  bottom: -0.25em;
}
img {
  /* Responsive images (ensure images don't scale beyond their parents) */

  max-width: 100%;
  /* Part 1: Set a maxium relative to the parent */

  width: auto\9;
  /* IE7-8 need help adjusting responsive images */

  height: auto;
  /* Part 2: Scale the height according to the width, otherwise you get stretching */

  vertical-align: middle;
  border: 0;
  -ms-interpolation-mode: bicubic;
}
#map_canvas img,
.google-maps img {
  max-width: none;
}
button,
input,
select,
textarea {
  margin: 0;
  font-size: 100%;
  vertical-align: middle;
}
button,
input {
  *overflow: visible;
  line-height: normal;
}
button::-moz-focus-inner,
input::-moz-focus-inner {
  padding: 0;
  border: 0;
}
button,
html input[type="button"],
input[type="reset"],
input[type="submit"] {
  -webkit-appearance: button;
  cursor: pointer;
}
input[type="search"] {
  -webkit-box-sizing: content-box;
  -moz-box-sizing: content-box;
  box-sizing: content-box;
  -webkit-appearance: textfield;
}
input[type="search"]::-webkit-search-decoration,
input[type="search"]::-webkit-search-cancel-button {
  -webkit-appearance: none;
}
textarea {
  overflow: auto;
  vertical-align: top;
}
body {
  margin: 0;
  font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
  font-size: 14px;
  line-height: 20px;
  color: #333333;
  background-color: #ffffff;
}
a {
  color: #0088cc;
  text-decoration: none;
}
a:hover {
  color: #005580;
  text-decoration: underline;
}
.img-rounded {
  -webkit-border-radius: 6px;
  -moz-border-radius: 6px;
  border-radius: 6px;
}
.img-polaroid {
  padding: 4px;
  background-color: #fff;
  border: 1px solid #ccc;
  border: 1px solid rgba(0, 0, 0, 0.2);
  -webkit-box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
  -moz-box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
}
.img-circle {
  -webkit-border-radius: 500px;
  -moz-border-radius: 500px;
  border-radius: 500px;
}
.row {
  margin-left: -20px;
  *zoom: 1;
}
.row:before,
.row:after {
  display: table;
  content: "";
  line-height: 0;
}
.row:after {
  clear: both;
}
[class*="span"] {
  float: left;
  min-height: 1px;
  margin-left: 20px;
}
.container,
.navbar-static-top .container,
.navbar-fixed-top .container,
.navbar-fixed-bottom .container {
  width: 940px;
}
.span12 {
  width: 940px;
}
.span11 {
  width: 860px;
}
.span10 {
  width: 780px;
}
.span9 {
  width: 700px;
}
.span8 {
  width: 620px;
}
.span7 {
  width: 540px;
}
.span6 {
  width: 460px;
}
.span5 {
  width: 380px;
}
.span4 {
  width: 300px;
}
.span3 {
  width: 220px;
}
.span2 {
  width: 140px;
}
.span1 {
  width: 60px;
}
.offset12 {
  margin-left: 980px;
}
.offset11 {
  margin-left: 900px;
}
.offset10 {
  margin-left: 820px;
}
.offset9 {
  margin-left: 740px;
}
.offset8 {
  margin-left: 660px;
}
.offset7 {
  margin-left: 580px;
}
.offset6 {
  margin-left: 500px;
}
.offset5 {
  margin-left: 420px;
}
.offset4 {
  margin-left: 340px;
}
.offset3 {
  margin-left: 260px;
}
.offset2 {
  margin-left: 180px;
}
.offset1 {
  margin-left: 100px;
}
.row-fluid {
  width: 100%;
  *zoom: 1;
}
.row-fluid:before,
.row-fluid:after {
  display: table;
  content: "";
  line-height: 0;
}
.row-fluid:after {
  clear: both;
}
.row-fluid [class*="span"] {
  display: block;
  width: 100%;
  min-height: 30px;
  -webkit-box-sizing: border-box;
  -moz-box-sizing: border-box;
  box-sizing: border-box;
  float: left;
  margin-left: 2.127659574468085%;
  *margin-left: 2.074468085106383%;
}
.row-fluid [class*="span"]:first-child {
  margin-left: 0;
}
.row-fluid .controls-row [class*="span"] + [class*="span"] {
  margin-left: 2.127659574468085%;
}
.row-fluid .span12 {
  width: 100%;
  *width: 99.94680851063829%;
}
.row-fluid .span11 {
  width: 91.48936170212765%;
  *width: 91.43617021276594%;
}
.row-fluid .span10 {
  width: 82.97872340425532%;
  *width: 82.92553191489361%;
}
.row-fluid .span9 {
  width: 74.46808510638297%;
  *width: 74.41489361702126%;
}
.row-fluid .span8 {
  width: 65.95744680851064%;
  *width: 65.90425531914893%;
}
.row-fluid .span7 {
  width: 57.44680851063829%;
  *width: 57.39361702127659%;
}
.row-fluid .span6 {
  width: 48.93617021276595%;
  *width: 48.88297872340425%;
}
.row-fluid .span5 {
  width: 40.42553191489362%;
  *width: 40.37234042553192%;
}
.row-fluid .span4 {
  width: 31.914893617021278%;
  *width: 31.861702127659576%;
}
.row-fluid .span3 {
  width: 23.404255319148934%;
  *width: 23.351063829787233%;
}
.row-fluid .span2 {
  width: 14.893617021276595%;
  *width: 14.840425531914894%;
}
.row-fluid .span1 {
  width: 6.382978723404255%;
  *width: 6.329787234042553%;
}
.row-fluid .offset12 {
  margin-left: 104.25531914893617%;
  *margin-left: 104.14893617021275%;
}
.row-fluid .offset12:first-child {
  margin-left: 102.12765957446808%;
  *margin-left: 102.02127659574467%;
}
.row-fluid .offset11 {
  margin-left: 95.74468085106382%;
  *margin-left: 95.6382978723404%;
}
.row-fluid .offset11:first-child {
  margin-left: 93.61702127659574%;
  *margin-left: 93.51063829787232%;
}
.row-fluid .offset10 {
  margin-left: 87.23404255319149%;
  *margin-left: 87.12765957446807%;
}
.row-fluid .offset10:first-child {
  margin-left: 85.1063829787234%;
  *margin-left: 84.99999999999999%;
}
.row-fluid .offset9 {
  margin-left: 78.72340425531914%;
  *margin-left: 78.61702127659572%;
}
.row-fluid .offset9:first-child {
  margin-left: 76.59574468085106%;
  *margin-left: 76.48936170212764%;
}
.row-fluid .offset8 {
  margin-left: 70.2127659574468%;
  *margin-left: 70.10638297872339%;
}
.row-fluid .offset8:first-child {
  margin-left: 68.08510638297872%;
  *margin-left: 67.9787234042553%;
}
.row-fluid .offset7 {
  margin-left: 61.70212765957446%;
  *margin-left: 61.59574468085106%;
}
.row-fluid .offset7:first-child {
  margin-left: 59.574468085106375%;
  *margin-left: 59.46808510638297%;
}
.row-fluid .offset6 {
  margin-left: 53.191489361702125%;
  *margin-left: 53.085106382978715%;
}
.row-fluid .offset6:first-child {
  margin-left: 51.063829787234035%;
  *margin-left: 50.95744680851063%;
}
.row-fluid .offset5 {
  margin-left: 44.68085106382979%;
  *margin-left: 44.57446808510638%;
}
.row-fluid .offset5:first-child {
  margin-left: 42.5531914893617%;
  *margin-left: 42.4468085106383%;
}
.row-fluid .offset4 {
  margin-left: 36.170212765957444%;
  *margin-left: 36.06382978723405%;
}
.row-fluid .offset4:first-child {
  margin-left: 34.04255319148936%;
  *margin-left: 33.93617021276596%;
}
.row-fluid .offset3 {
  margin-left: 27.659574468085104%;
  *margin-left: 27.5531914893617%;
}
.row-fluid .offset3:first-child {
  margin-left: 25.53191489361702%;
  *margin-left: 25.425531914893618%;
}
.row-fluid .offset2 {
  margin-left: 19.148936170212764%;
  *margin-left: 19.04255319148936%;
}
.row-fluid .offset2:first-child {
  margin-left: 17.02127659574468%;
  *margin-left: 16.914893617021278%;
}
.row-fluid .offset1 {
  margin-left: 10.638297872340425%;
  *margin-left: 10.53191489361702%;
}
.row-fluid .offset1:first-child {
  margin-left: 8.51063829787234%;
  *margin-left: 8.404255319148938%;
}
[class*="span"].hide,
.row-fluid [class*="span"].hide {
  display: none;
}
[class*="span"].pull-right,
.row-fluid [class*="span"].pull-right {
  float: right;
}
.container {
  margin-right: auto;
  margin-left: auto;
  *zoom: 1;
}
.container:before,
.container:after {
  display: table;
  content: "";
  line-height: 0;
}
.container:after {
  clear: both;
}
.container-fluid {
  padding-right: 20px;
  padding-left: 20px;
  *zoom: 1;
}
.container-fluid:before,
.container-fluid:after {
  display: table;
  content: "";
  line-height: 0;
}
.container-fluid:after {
  clear: both;
}
p {
  margin: 0 0 10px;
}
.lead {
  margin-bottom: 20px;
  font-size: 21px;
  font-weight: 200;
  line-height: 30px;
}
small {
  font-size: 85%;
}
strong {
  font-weight: bold;
}
em {
  font-style: italic;
}
cite {
  font-style: normal;
}
.muted {
  color: #999999;
}
.text-warning {
  color: #c09853;
}
a.text-warning:hover {
  color: #a47e3c;
}
.text-error {
  color: #b94a48;
}
a.text-error:hover {
  color: #953b39;
}
.text-info {
  color: #3a87ad;
}
a.text-info:hover {
  color: #2d6987;
}
.text-success {
  color: #468847;
}
a.text-success:hover {
  color: #356635;
}
h1,
h2,
h3,
h4,
h5,
h6 {
  margin: 10px 0;
  font-family: inherit;
  font-weight: bold;
  line-height: 20px;
  color: inherit;
  text-rendering: optimizelegibility;
}
h1 small,
h2 small,
h3 small,
h4 small,
h5 small,
h6 small {
  font-weight: normal;
  line-height: 1;
  color: #999999;
}
h1,
h2,
h3 {
  line-height: 40px;
}
h1 {
  font-size: 38.5px;
}
h2 {
  font-size: 31.5px;
}
h3 {
  font-size: 24.5px;
}
h4 {
  font-size: 17.5px;
}
h5 {
  font-size: 14px;
}
h6 {
  font-size: 11.9px;
}
h1 small {
  font-size: 24.5px;
}
h2 small {
  font-size: 17.5px;
}
h3 small {
  font-size: 14px;
}
h4 small {
  font-size: 14px;
}
.page-header {
  padding-bottom: 9px;
  margin: 20px 0 30px;
  border-bottom: 1px solid #eeeeee;
}
ul,
ol {
  padding: 0;
  margin: 0 0 10px 25px;
}
ul ul,
ul ol,
ol ol,
ol ul {
  margin-bottom: 0;
}
li {
  line-height: 20px;
}
ul.unstyled,
ol.unstyled {
  margin-left: 0;
  list-style: none;
}
dl {
  margin-bottom: 20px;
}
dt,
dd {
  line-height: 20px;
}
dt {
  font-weight: bold;
}
dd {
  margin-left: 10px;
}
.dl-horizontal {
  *zoom: 1;
}
.dl-horizontal:before,
.dl-horizontal:after {
  display: table;
  content: "";
  line-height: 0;
}
.dl-horizontal:after {
  clear: both;
}
.dl-horizontal dt {
  float: left;
  width: 160px;
  clear: left;
  text-align: right;
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}
.dl-horizontal dd {
  margin-left: 180px;
}
hr {
  margin: 20px 0;
  border: 0;
  border-top: 1px solid #eeeeee;
  border-bottom: 1px solid #ffffff;
}
abbr[title],
abbr[data-original-title] {
  cursor: help;
  border-bottom: 1px dotted #999999;
}
abbr.initialism {
  font-size: 90%;
  text-transform: uppercase;
}
blockquote {
  padding: 0 0 0 15px;
  margin: 0 0 20px;
  border-left: 5px solid #eeeeee;
}
blockquote p {
  margin-bottom: 0;
  font-size: 16px;
  font-weight: 300;
  line-height: 25px;
}
blockquote small {
  display: block;
  line-height: 20px;
  color: #999999;
}
blockquote small:before {
  content: '\2014 \00A0';
}
blockquote.pull-right {
  float: right;
  padding-right: 15px;
  padding-left: 0;
  border-right: 5px solid #eeeeee;
  border-left: 0;
}
blockquote.pull-right p,
blockquote.pull-right small {
  text-align: right;
}
blockquote.pull-right small:before {
  content: '';
}
blockquote.pull-right small:after {
  content: '\00A0 \2014';
}
q:before,
q:after,
blockquote:before,
blockquote:after {
  content: "";
}
address {
  display: block;
  margin-bottom: 20px;
  font-style: normal;
  line-height: 20px;
}
code,
pre {
  padding: 0 3px 2px;
  font-family: Monaco, Menlo, Consolas, "Courier New", monospace;
  font-size: 12px;
  color: #333333;
  -webkit-border-radius: 3px;
  -moz-border-radius: 3px;
  border-radius: 3px;
}
code {
  padding: 2px 4px;
  color: #d14;
  background-color: #f7f7f9;
  border: 1px solid #e1e1e8;
}
pre {
  display: block;
  padding: 9.5px;
  margin: 0 0 10px;
  font-size: 13px;
  line-height: 20px;
  word-break: break-all;
  word-wrap: break-word;
  white-space: pre;
  white-space: pre-wrap;
  background-color: #f5f5f5;
  border: 1px solid #ccc;
  border: 1px solid rgba(0, 0, 0, 0.15);
  -webkit-border-radius: 4px;
  -moz-border-radius: 4px;
  border-radius: 4px;
}
pre.prettyprint {
  margin-bottom: 20px;
}
pre code {
  padding: 0;
  color: inherit;
  background-color: transparent;
  border: 0;
}
.pre-scrollable {
  max-height: 340px;
  overflow-y: scroll;
}
.label,
.badge {
  display: inline-block;
  padding: 2px 4px;
  font-size: 11.844px;
  font-weight: bold;
  line-height: 14px;
  color: #ffffff;
  vertical-align: baseline;
  white-space: nowrap;
  text-shadow: 0 -1px 0 rgba(0, 0, 0, 0.25);
  background-color: #999999;
}
.label {
  -webkit-border-radius: 3px;
  -moz-border-radius: 3px;
  border-radius: 3px;
}
.badge {
  padding-left: 9px;
  padding-right: 9px;
  -webkit-border-radius: 9px;
  -moz-border-radius: 9px;
  border-radius: 9px;
}
a.label:hover,
a.badge:hover {
  color: #ffffff;
  text-decoration: none;
  cursor: pointer;
}
.label-important,
.badge-important {
  background-color: #b94a48;
}
.label-important[href],
.badge-important[href] {
  background-color: #953b39;
}
.label-warning,
.badge-warning {
  background-color: #f89406;
}
.label-warning[href],
.badge-warning[href] {
  background-color: #c67605;
}
.label-success,
.badge-success {
  background-color: #468847;
}
.label-success[href],
.badge-success[href] {
  background-color: #356635;
}
.label-info,
.badge-info {
  background-color: #3a87ad;
}
.label-info[href],
.badge-info[href] {
  background-color: #2d6987;
}
.label-inverse,
.badge-inverse {
  background-color: #333333;
}
.label-inverse[href],
.badge-inverse[href] {
  background-color: #1a1a1a;
}
.btn .label,
.btn .badge {
  position: relative;
  top: -1px;
}
.btn-mini .label,
.btn-mini .badge {
  top: 0;
}
table {
  max-width: 100%;
  background-color: transparent;
  border-collapse: collapse;
  border-spacing: 0;
}
.table {
  width: 100%;
  margin-bottom: 20px;
}
.table th,
.table td {
  padding: 8px;
  line-height: 20px;
  text-align: left;
  vertical-align: top;
  border-top: 1px solid #dddddd;
}
.table th {
  font-weight: bold;
}
.table thead th {
  vertical-align: bottom;
}
.table caption + thead tr:first-child th,
.table caption + thead tr:first-child td,
.table colgroup + thead tr:first-child th,
.table colgroup + thead tr:first-child td,
.table thead:first-child tr:first-child th,
.table thead:first-child tr:first-child td {
  border-top: 0;
}
.table tbody + tbody {
  border-top: 2px solid #dddddd;
}
.table-condensed th,
.table-condensed td {
  padding: 4px 5px;
}
.table-bordered {
  border: 1px solid #dddddd;
  border-collapse: separate;
  *border-collapse: collapse;
  border-left: 0;
  -webkit-border-radius: 4px;
  -moz-border-radius: 4px;
  border-radius: 4px;
}
.table-bordered th,
.table-bordered td {
  border-left: 1px solid #dddddd;
}
.table-bordered caption + thead tr:first-child th,
.table-bordered caption + tbody tr:first-child th,
.table-bordered caption + tbody tr:first-child td,
.table-bordered colgroup + thead tr:first-child th,
.table-bordered colgroup + tbody tr:first-child th,
.table-bordered colgroup + tbody tr:first-child td,
.table-bordered thead:first-child tr:first-child th,
.table-bordered tbody:first-child tr:first-child th,
.table-bordered tbody:first-child tr:first-child td {
  border-top: 0;
}
.table-bordered thead:first-child tr:first-child th:first-child,
.table-bordered tbody:first-child tr:first-child td:first-child {
  -webkit-border-top-left-radius: 4px;
  border-top-left-radius: 4px;
  -moz-border-radius-topleft: 4px;
}
.table-bordered thead:first-child tr:first-child th:last-child,
.table-bordered tbody:first-child tr:first-child td:last-child {
  -webkit-border-top-right-radius: 4px;
  border-top-right-radius: 4px;
  -moz-border-radius-topright: 4px;
}
.table-bordered thead:last-child tr:last-child th:first-child,
.table-bordered tbody:last-child tr:last-child td:first-child,
.table-bordered tfoot:last-child tr:last-child td:first-child {
  -webkit-border-radius: 0 0 0 4px;
  -moz-border-radius: 0 0 0 4px;
  border-radius: 0 0 0 4px;
  -webkit-border-bottom-left-radius: 4px;
  border-bottom-left-radius: 4px;
  -moz-border-radius-bottomleft: 4px;
}
.table-bordered thead:last-child tr:last-child th:last-child,
.table-bordered tbody:last-child tr:last-child td:last-child,
.table-bordered tfoot:last-child tr:last-child td:last-child {
  -webkit-border-bottom-right-radius: 4px;
  border-bottom-right-radius: 4px;
  -moz-border-radius-bottomright: 4px;
}
.table-bordered caption + thead tr:first-child th:first-child,
.table-bordered caption + tbody tr:first-child td:first-child,
.table-bordered colgroup + thead tr:first-child th:first-child,
.table-bordered colgroup + tbody tr:first-child td:first-child {
  -webkit-border-top-left-radius: 4px;
  border-top-left-radius: 4px;
  -moz-border-radius-topleft: 4px;
}
.table-bordered caption + thead tr:first-child th:last-child,
.table-bordered caption + tbody tr:first-child td:last-child,
.table-bordered colgroup + thead tr:first-child th:last-child,
.table-bordered colgroup + tbody tr:first-child td:last-child {
  -webkit-border-top-right-radius: 4px;
  border-top-right-radius: 4px;
  -moz-border-radius-topright: 4px;
}
.table-striped tbody tr:nth-child(odd) td,
.table-striped tbody tr:nth-child(odd) th {
  background-color: #f9f9f9;
}
.table-hover tbody tr:hover td,
.table-hover tbody tr:hover th {
  background-color: #f5f5f5;
}
table td[class*="span"],
table th[class*="span"],
.row-fluid table td[class*="span"],
.row-fluid table th[class*="span"] {
  display: table-cell;
  float: none;
  margin-left: 0;
}
.table td.span1,
.table th.span1 {
  float: none;
  width: 44px;
  margin-left: 0;
}
.table td.span2,
.table th.span2 {
  float: none;
  width: 124px;
  margin-left: 0;
}
.table td.span3,
.table th.span3 {
  float: none;
  width: 204px;
  margin-left: 0;
}
.table td.span4,
.table th.span4 {
  float: none;
  width: 284px;
  margin-left: 0;
}
.table td.span5,
.table th.span5 {
  float: none;
  width: 364px;
  margin-left: 0;
}
.table td.span6,
.table th.span6 {
  float: none;
  width: 444px;
  margin-left: 0;
}
.table td.span7,
.table th.span7 {
  float: none;
  width: 524px;
  margin-left: 0;
}
.table td.span8,
.table th.span8 {
  float: none;
  width: 604px;
  margin-left: 0;
}
.table td.span9,
.table th.span9 {
  float: none;
  width: 684px;
  margin-left: 0;
}
.table td.span10,
.table th.span10 {
  float: none;
  width: 764px;
  margin-left: 0;
}
.table td.span11,
.table th.span11 {
  float: none;
  width: 844px;
  margin-left: 0;
}
.table td.span12,
.table th.span12 {
  float: none;
  width: 924px;
  margin-left: 0;
}
.table tbody tr.success td {
  background-color: #dff0d8;
}
.table tbody tr.error td {
  background-color: #f2dede;
}
.table tbody tr.warning td {
  background-color: #fcf8e3;
}
.table tbody tr.info td {
  background-color: #d9edf7;
}
.table-hover tbody tr.success:hover td {
  background-color: #d0e9c6;
}
.table-hover tbody tr.error:hover td {
  background-color: #ebcccc;
}
.table-hover tbody tr.warning:hover td {
  background-color: #faf2cc;
}
.table-hover tbody tr.info:hover td {
  background-color: #c4e3f3;
}
form {
  margin: 0 0 20px;
}
fieldset {
  padding: 0;
  margin: 0;
  border: 0;
}
legend {
  display: block;
  width: 100%;
  padding: 0;
  margin-bottom: 20px;
  font-size: 21px;
  line-height: 40px;
  color: #333333;
  border: 0;
  border-bottom: 1px solid #e5e5e5;
}
legend small {
  font-size: 15px;
  color: #999999;
}
label,
input,
button,
select,
textarea {
  font-size: 14px;
  font-weight: normal;
  line-height: 20px;
}
input,
button,
select,
textarea {
  font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
}
label {
  display: block;
  margin-bottom: 5px;
}
select,
textarea,
input[type="text"],
input[type="password"],
input[type="datetime"],
input[type="datetime-local"],
input[type="date"],
input[type="month"],
input[type="time"],
input[type="week"],
input[type="number"],
input[type="email"],
input[type="url"],
input[type="search"],
input[type="tel"],
input[type="color"],
.uneditable-input {
  display: inline-block;
  height: 20px;
  padding: 4px 6px;
  margin-bottom: 10px;
  font-size: 14px;
  line-height: 20px;
  color: #555555;
  -webkit-border-radius: 4px;
  -moz-border-radius: 4px;
  border-radius: 4px;
  vertical-align: middle;
}
input,
textarea,
.uneditable-input {
  width: 206px;
}
textarea {
  height: auto;
}
textarea,
input[type="text"],
input[type="password"],
input[type="datetime"],
input[type="datetime-local"],
input[type="date"],
input[type="month"],
input[type="time"],
input[type="week"],
input[type="number"],
input[type="email"],
input[type="url"],
input[type="search"],
input[type="tel"],
input[type="color"],
.uneditable-input {
  background-color: #ffffff;
  border: 1px solid #cccccc;
  -webkit-box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075);
  -moz-box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075);
  box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075);
  -webkit-transition: border linear .2s, box-shadow linear .2s;
  -moz-transition: border linear .2s, box-shadow linear .2s;
  -o-transition: border linear .2s, box-shadow linear .2s;
  transition: border linear .2s, box-shadow linear .2s;
}
textarea:focus,
input[type="text"]:focus,
input[type="password"]:focus,
input[type="datetime"]:focus,
input[type="datetime-local"]:focus,
input[type="date"]:focus,
input[type="month"]:focus,
input[type="time"]:focus,
input[type="week"]:focus,
input[type="number"]:focus,
input[type="email"]:focus,
input[type="url"]:focus,
input[type="search"]:focus,
input[type="tel"]:focus,
input[type="color"]:focus,
.uneditable-input:focus {
  border-color: rgba(82, 168, 236, 0.8);
  outline: 0;
  outline: thin dotted \9;
  /* IE6-9 */

  -webkit-box-shadow: inset 0 1px 1px rgba(0,0,0,.075), 0 0 8px rgba(82,168,236,.6);
  -moz-box-shadow: inset 0 1px 1px rgba(0,0,0,.075), 0 0 8px rgba(82,168,236,.6);
  box-shadow: inset 0 1px 1px rgba(0,0,0,.075), 0 0 8px rgba(82,168,236,.6);
}
input[type="radio"],
input[type="checkbox"] {
  margin: 4px 0 0;
  *margin-top: 0;
  /* IE7 */

  margin-top: 1px \9;
  /* IE8-9 */

  line-height: normal;
  cursor: pointer;
}
input[type="file"],
input[type="image"],
input[type="submit"],
input[type="reset"],
input[type="button"],
input[type="radio"],
input[type="checkbox"] {
  width: auto;
}
select,
input[type="file"] {
  height: 30px;
  /* In IE7, the height of the select element cannot be changed by height, only font-size */

  *margin-top: 4px;
  /* For IE7, add top margin to align select with labels */

  line-height: 30px;
}
select {
  width: 220px;
  border: 1px solid #cccccc;
  background-color: #ffffff;
}
select[multiple],
select[size] {
  height: auto;
}
select:focus,
input[type="file"]:focus,
input[type="radio"]:focus,
input[type="checkbox"]:focus {
  outline: thin dotted #333;
  outline: 5px auto -webkit-focus-ring-color;
  outline-offset: -2px;
}
.uneditable-input,
.uneditable-textarea {
  color: #999999;
  background-color: #fcfcfc;
  border-color: #cccccc;
  -webkit-box-shadow: inset 0 1px 2px rgba(0, 0, 0, 0.025);
  -moz-box-shadow: inset 0 1px 2px rgba(0, 0, 0, 0.025);
  box-shadow: inset 0 1px 2px rgba(0, 0, 0, 0.025);
  cursor: not-allowed;
}
.uneditable-input {
  overflow: hidden;
  white-space: nowrap;
}
.uneditable-textarea {
  width: auto;
  height: auto;
}
input:-moz-placeholder,
textarea:-moz-placeholder {
  color: #999999;
}
input:-ms-input-placeholder,
textarea:-ms-input-placeholder {
  color: #999999;
}
input::-webkit-input-placeholder,
textarea::-webkit-input-placeholder {
  color: #999999;
}
.radio,
.checkbox {
  min-height: 20px;
  padding-left: 20px;
}
.radio input[type="radio"],
.checkbox input[type="checkbox"] {
  float: left;
  margin-left: -20px;
}
.controls > .radio:first-child,
.controls > .checkbox:first-child {
  padding-top: 5px;
}
.radio.inline,
.checkbox.inline {
  display: inline-block;
  padding-top: 5px;
  margin-bottom: 0;
  vertical-align: middle;
}
.radio.inline + .radio.inline,
.checkbox.inline + .checkbox.inline {
  margin-left: 10px;
}
.input-mini {
  width: 60px;
}
.input-small {
  width: 90px;
}
.input-medium {
  width: 150px;
}
.input-large {
  width: 210px;
}
.input-xlarge {
  width: 270px;
}
.input-xxlarge {
  width: 530px;
}
input[class*="span"],
select[class*="span"],
textarea[class*="span"],
.uneditable-input[class*="span"],
.row-fluid input[class*="span"],
.row-fluid select[class*="span"],
.row-fluid textarea[class*="span"],
.row-fluid .uneditable-input[class*="span"] {
  float: none;
  margin-left: 0;
}
.input-append input[class*="span"],
.input-append .uneditable-input[class*="span"],
.input-prepend input[class*="span"],
.input-prepend .uneditable-input[class*="span"],
.row-fluid input[class*="span"],
.row-fluid select[class*="span"],
.row-fluid textarea[class*="span"],
.row-fluid .uneditable-input[class*="span"],
.row-fluid .input-prepend [class*="span"],
.row-fluid .input-append [class*="span"] {
  display: inline-block;
}
input,
textarea,
.uneditable-input {
  margin-left: 0;
}
.controls-row [class*="span"] + [class*="span"] {
  margin-left: 20px;
}
input.span12, textarea.span12, .uneditable-input.span12 {
  width: 926px;
}
input.span11, textarea.span11, .uneditable-input.span11 {
  width: 846px;
}
input.span10, textarea.span10, .uneditable-input.span10 {
  width: 766px;
}
input.span9, textarea.span9, .uneditable-input.span9 {
  width: 686px;
}
input.span8, textarea.span8, .uneditable-input.span8 {
  width: 606px;
}
input.span7, textarea.span7, .uneditable-input.span7 {
  width: 526px;
}
input.span6, textarea.span6, .uneditable-input.span6 {
  width: 446px;
}
input.span5, textarea.span5, .uneditable-input.span5 {
  width: 366px;
}
input.span4, textarea.span4, .uneditable-input.span4 {
  width: 286px;
}
input.span3, textarea.span3, .uneditable-input.span3 {
  width: 206px;
}
input.span2, textarea.span2, .uneditable-input.span2 {
  width: 126px;
}
input.span1, textarea.span1, .uneditable-input.span1 {
  width: 46px;
}
.controls-row {
  *zoom: 1;
}
.controls-row:before,
.controls-row:after {
  display: table;
  content: "";
  line-height: 0;
}
.controls-row:after {
  clear: both;
}
.controls-row [class*="span"],
.row-fluid .controls-row [class*="span"] {
  float: left;
}
.controls-row .checkbox[class*="span"],
.controls-row .radio[class*="span"] {
  padding-top: 5px;
}
input[disabled],
select[disabled],
textarea[disabled],
input[readonly],
select[readonly],
textarea[readonly] {
  cursor: not-allowed;
  background-color: #eeeeee;
}
input[type="radio"][disabled],
input[type="checkbox"][disabled],
input[type="radio"][readonly],
input[type="checkbox"][readonly] {
  background-color: transparent;
}
.control-group.warning > label,
.control-group.warning .help-block,
.control-group.warning .help-inline {
  color: #c09853;
}
.control-group.warning .checkbox,
.control-group.warning .radio,
.control-group.warning input,
.control-group.warning select,
.control-group.warning textarea {
  color: #c09853;
}
.control-group.warning input,
.control-group.warning select,
.control-group.warning textarea {
  border-color: #c09853;
  -webkit-box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075);
  -moz-box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075);
  box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075);
}
.control-group.warning input:focus,
.control-group.warning select:focus,
.control-group.warning textarea:focus {
  border-color: #a47e3c;
  -webkit-box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075), 0 0 6px #dbc59e;
  -moz-box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075), 0 0 6px #dbc59e;
  box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075), 0 0 6px #dbc59e;
}
.control-group.warning .input-prepend .add-on,
.control-group.warning .input-append .add-on {
  color: #c09853;
  background-color: #fcf8e3;
  border-color: #c09853;
}
.control-group.error > label,
.control-group.error .help-block,
.control-group.error .help-inline {
  color: #b94a48;
}
.control-group.error .checkbox,
.control-group.error .radio,
.control-group.error input,
.control-group.error select,
.control-group.error textarea {
  color: #b94a48;
}
.control-group.error input,
.control-group.error select,
.control-group.error textarea {
  border-color: #b94a48;
  -webkit-box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075);
  -moz-box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075);
  box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075);
}
.control-group.error input:focus,
.control-group.error select:focus,
.control-group.error textarea:focus {
  border-color: #953b39;
  -webkit-box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075), 0 0 6px #d59392;
  -moz-box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075), 0 0 6px #d59392;
  box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075), 0 0 6px #d59392;
}
.control-group.error .input-prepend .add-on,
.control-group.error .input-append .add-on {
  color: #b94a48;
  background-color: #f2dede;
  border-color: #b94a48;
}
.control-group.success > label,
.control-group.success .help-block,
.control-group.success .help-inline {
  color: #468847;
}
.control-group.success .checkbox,
.control-group.success .radio,
.control-group.success input,
.control-group.success select,
.control-group.success textarea {
  color: #468847;
}
.control-group.success input,
.control-group.success select,
.control-group.success textarea {
  border-color: #468847;
  -webkit-box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075);
  -moz-box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075);
  box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075);
}
.control-group.success input:focus,
.control-group.success select:focus,
.control-group.success textarea:focus {
  border-color: #356635;
  -webkit-box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075), 0 0 6px #7aba7b;
  -moz-box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075), 0 0 6px #7aba7b;
  box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075), 0 0 6px #7aba7b;
}
.control-group.success .input-prepend .add-on,
.control-group.success .input-append .add-on {
  color: #468847;
  background-color: #dff0d8;
  border-color: #468847;
}
.control-group.info > label,
.control-group.info .help-block,
.control-group.info .help-inline {
  color: #3a87ad;
}
.control-group.info .checkbox,
.control-group.info .radio,
.control-group.info input,
.control-group.info select,
.control-group.info textarea {
  color: #3a87ad;
}
.control-group.info input,
.control-group.info select,
.control-group.info textarea {
  border-color: #3a87ad;
  -webkit-box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075);
  -moz-box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075);
  box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075);
}
.control-group.info input:focus,
.control-group.info select:focus,
.control-group.info textarea:focus {
  border-color: #2d6987;
  -webkit-box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075), 0 0 6px #7ab5d3;
  -moz-box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075), 0 0 6px #7ab5d3;
  box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075), 0 0 6px #7ab5d3;
}
.control-group.info .input-prepend .add-on,
.control-group.info .input-append .add-on {
  color: #3a87ad;
  background-color: #d9edf7;
  border-color: #3a87ad;
}
input:focus:required:invalid,
textarea:focus:required:invalid,
select:focus:required:invalid {
  color: #b94a48;
  border-color: #ee5f5b;
}
input:focus:required:invalid:focus,
textarea:focus:required:invalid:focus,
select:focus:required:invalid:focus {
  border-color: #e9322d;
  -webkit-box-shadow: 0 0 6px #f8b9b7;
  -moz-box-shadow: 0 0 6px #f8b9b7;
  box-shadow: 0 0 6px #f8b9b7;
}
.form-actions {
  padding: 19px 20px 20px;
  margin-top: 20px;
  margin-bottom: 20px;
  background-color: #f5f5f5;
  border-top: 1px solid #e5e5e5;
  *zoom: 1;
}
.form-actions:before,
.form-actions:after {
  display: table;
  content: "";
  line-height: 0;
}
.form-actions:after {
  clear: both;
}
.help-block,
.help-inline {
  color: #595959;
}
.help-block {
  display: block;
  margin-bottom: 10px;
}
.help-inline {
  display: inline-block;
  *display: inline;
  /* IE7 inline-block hack */

  *zoom: 1;
  vertical-align: middle;
  padding-left: 5px;
}
.input-append,
.input-prepend {
  margin-bottom: 5px;
  font-size: 0;
  white-space: nowrap;
}
.input-append input,
.input-prepend input,
.input-append select,
.input-prepend select,
.input-append .uneditable-input,
.input-prepend .uneditable-input,
.input-append .dropdown-menu,
.input-prepend .dropdown-menu {
  font-size: 14px;
}
.input-append input,
.input-prepend input,
.input-append select,
.input-prepend select,
.input-append .uneditable-input,
.input-prepend .uneditable-input {
  position: relative;
  margin-bottom: 0;
  *margin-left: 0;
  vertical-align: top;
  -webkit-border-radius: 0 4px 4px 0;
  -moz-border-radius: 0 4px 4px 0;
  border-radius: 0 4px 4px 0;
}
.input-append input:focus,
.input-prepend input:focus,
.input-append select:focus,
.input-prepend select:focus,
.input-append .uneditable-input:focus,
.input-prepend .uneditable-input:focus {
  z-index: 2;
}
.input-append .add-on,
.input-prepend .add-on {
  display: inline-block;
  width: auto;
  height: 20px;
  min-width: 16px;
  padding: 4px 5px;
  font-size: 14px;
  font-weight: normal;
  line-height: 20px;
  text-align: center;
  text-shadow: 0 1px 0 #ffffff;
  background-color: #eeeeee;
  border: 1px solid #ccc;
}
.input-append .add-on,
.input-prepend .add-on,
.input-append .btn,
.input-prepend .btn {
  vertical-align: top;
  -webkit-border-radius: 0;
  -moz-border-radius: 0;
  border-radius: 0;
}
.input-append .active,
.input-prepend .active {
  background-color: #a9dba9;
  border-color: #46a546;
}
.input-prepend .add-on,
.input-prepend .btn {
  margin-right: -1px;
}
.input-prepend .add-on:first-child,
.input-prepend .btn:first-child {
  -webkit-border-radius: 4px 0 0 4px;
  -moz-border-radius: 4px 0 0 4px;
  border-radius: 4px 0 0 4px;
}
.input-append input,
.input-append select,
.input-append .uneditable-input {
  -webkit-border-radius: 4px 0 0 4px;
  -moz-border-radius: 4px 0 0 4px;
  border-radius: 4px 0 0 4px;
}
.input-append input + .btn-group .btn,
.input-append select + .btn-group .btn,
.input-append .uneditable-input + .btn-group .btn {
  -webkit-border-radius: 0 4px 4px 0;
  -moz-border-radius: 0 4px 4px 0;
  border-radius: 0 4px 4px 0;
}
.input-append .add-on,
.input-append .btn,
.input-append .btn-group {
  margin-left: -1px;
}
.input-append .add-on:last-child,
.input-append .btn:last-child {
  -webkit-border-radius: 0 4px 4px 0;
  -moz-border-radius: 0 4px 4px 0;
  border-radius: 0 4px 4px 0;
}
.input-prepend.input-append input,
.input-prepend.input-append select,
.input-prepend.input-append .uneditable-input {
  -webkit-border-radius: 0;
  -moz-border-radius: 0;
  border-radius: 0;
}
.input-prepend.input-append input + .btn-group .btn,
.input-prepend.input-append select + .btn-group .btn,
.input-prepend.input-append .uneditable-input + .btn-group .btn {
  -webkit-border-radius: 0 4px 4px 0;
  -moz-border-radius: 0 4px 4px 0;
  border-radius: 0 4px 4px 0;
}
.input-prepend.input-append .add-on:first-child,
.input-prepend.input-append .btn:first-child {
  margin-right: -1px;
  -webkit-border-radius: 4px 0 0 4px;
  -moz-border-radius: 4px 0 0 4px;
  border-radius: 4px 0 0 4px;
}
.input-prepend.input-append .add-on:last-child,
.input-prepend.input-append .btn:last-child {
  margin-left: -1px;
  -webkit-border-radius: 0 4px 4px 0;
  -moz-border-radius: 0 4px 4px 0;
  border-radius: 0 4px 4px 0;
}
.input-prepend.input-append .btn-group:first-child {
  margin-left: 0;
}
input.search-query {
  padding-right: 14px;
  padding-right: 4px \9;
  padding-left: 14px;
  padding-left: 4px \9;
  /* IE7-8 doesn't have border-radius, so don't indent the padding */

  margin-bottom: 0;
  -webkit-border-radius: 15px;
  -moz-border-radius: 15px;
  border-radius: 15px;
}
/* Allow for input prepend/append in search forms */
.form-search .input-append .search-query,
.form-search .input-prepend .search-query {
  -webkit-border-radius: 0;
  -moz-border-radius: 0;
  border-radius: 0;
}
.form-search .input-append .search-query {
  -webkit-border-radius: 14px 0 0 14px;
  -moz-border-radius: 14px 0 0 14px;
  border-radius: 14px 0 0 14px;
}
.form-search .input-append .btn {
  -webkit-border-radius: 0 14px 14px 0;
  -moz-border-radius: 0 14px 14px 0;
  border-radius: 0 14px 14px 0;
}
.form-search .input-prepend .search-query {
  -webkit-border-radius: 0 14px 14px 0;
  -moz-border-radius: 0 14px 14px 0;
  border-radius: 0 14px 14px 0;
}
.form-search .input-prepend .btn {
  -webkit-border-radius: 14px 0 0 14px;
  -moz-border-radius: 14px 0 0 14px;
  border-radius: 14px 0 0 14px;
}
.form-search input,
.form-inline input,
.form-horizontal input,
.form-search textarea,
.form-inline textarea,
.form-horizontal textarea,
.form-search select,
.form-inline select,
.form-horizontal select,
.form-search .help-inline,
.form-inline .help-inline,
.form-horizontal .help-inline,
.form-search .uneditable-input,
.form-inline .uneditable-input,
.form-horizontal .uneditable-input,
.form-search .input-prepend,
.form-inline .input-prepend,
.form-horizontal .input-prepend,
.form-search .input-append,
.form-inline .input-append,
.form-horizontal .input-append {
  display: inline-block;
  *display: inline;
  /* IE7 inline-block hack */

  *zoom: 1;
  margin-bottom: 0;
  vertical-align: middle;
}
.form-search .hide,
.form-inline .hide,
.form-horizontal .hide {
  display: none;
}
.form-search label,
.form-inline label,
.form-search .btn-group,
.form-inline .btn-group {
  display: inline-block;
}
.form-search .input-append,
.form-inline .input-append,
.form-search .input-prepend,
.form-inline .input-prepend {
  margin-bottom: 0;
}
.form-search .radio,
.form-search .checkbox,
.form-inline .radio,
.form-inline .checkbox {
  padding-left: 0;
  margin-bottom: 0;
  vertical-align: middle;
}
.form-search .radio input[type="radio"],
.form-search .checkbox input[type="checkbox"],
.form-inline .radio input[type="radio"],
.form-inline .checkbox input[type="checkbox"] {
  float: left;
  margin-right: 3px;
  margin-left: 0;
}
.control-group {
  margin-bottom: 10px;
}
legend + .control-group {
  margin-top: 20px;
  -webkit-margin-top-collapse: separate;
}
.form-horizontal .control-group {
  margin-bottom: 20px;
  *zoom: 1;
}
.form-horizontal .control-group:before,
.form-horizontal .control-group:after {
  display: table;
  content: "";
  line-height: 0;
}
.form-horizontal .control-group:after {
  clear: both;
}
.form-horizontal .control-label {
  float: left;
  width: 160px;
  padding-top: 5px;
  text-align: right;
}
.form-horizontal .controls {
  *display: inline-block;
  *padding-left: 20px;
  margin-left: 180px;
  *margin-left: 0;
}
.form-horizontal .controls:first-child {
  *padding-left: 180px;
}
.form-horizontal .help-block {
  margin-bottom: 0;
}
.form-horizontal input + .help-block,
.form-horizontal select + .help-block,
.form-horizontal textarea + .help-block {
  margin-top: 10px;
}
.form-horizontal .form-actions {
  padding-left: 180px;
}
.btn {
  display: inline-block;
  *display: inline;
  /* IE7 inline-block hack */

  *zoom: 1;
  padding: 4px 12px;
  margin-bottom: 0;
  font-size: 14px;
  line-height: 20px;
  *line-height: 20px;
  text-align: center;
  vertical-align: middle;
  cursor: pointer;
  color: #333333;
  text-shadow: 0 1px 1px rgba(255, 255, 255, 0.75);
  background-color: #f5f5f5;
  background-image: -moz-linear-gradient(top, #ffffff, #e6e6e6);
  background-image: -webkit-gradient(linear, 0 0, 0 100%, from(#ffffff), to(#e6e6e6));
  background-image: -webkit-linear-gradient(top, #ffffff, #e6e6e6);
  background-image: -o-linear-gradient(top, #ffffff, #e6e6e6);
  background-image: linear-gradient(to bottom, #ffffff, #e6e6e6);
  background-repeat: repeat-x;
  filter: progid:DXImageTransform.Microsoft.gradient(startColorstr='#ffffffff', endColorstr='#ffe6e6e6', GradientType=0);
  border-color: #e6e6e6 #e6e6e6 #bfbfbf;
  border-color: rgba(0, 0, 0, 0.1) rgba(0, 0, 0, 0.1) rgba(0, 0, 0, 0.25);
  *background-color: #e6e6e6;
  /* Darken IE7 buttons by default so they stand out more given they won't have borders */

  filter: progid:DXImageTransform.Microsoft.gradient(enabled = false);
  border: 1px solid #bbbbbb;
  *border: 0;
  border-bottom-color: #a2a2a2;
  -webkit-border-radius: 4px;
  -moz-border-radius: 4px;
  border-radius: 4px;
  *margin-left: .3em;
  -webkit-box-shadow: inset 0 1px 0 rgba(255,255,255,.2), 0 1px 2px rgba(0,0,0,.05);
  -moz-box-shadow: inset 0 1px 0 rgba(255,255,255,.2), 0 1px 2px rgba(0,0,0,.05);
  box-shadow: inset 0 1px 0 rgba(255,255,255,.2), 0 1px 2px rgba(0,0,0,.05);
}
.btn:hover,
.btn:active,
.btn.active,
.btn.disabled,
.btn[disabled] {
  color: #333333;
  background-color: #e6e6e6;
  *background-color: #d9d9d9;
}
.btn:active,
.btn.active {
  background-color: #cccccc \9;
}
.btn:first-child {
  *margin-left: 0;
}
.btn:hover {
  color: #333333;
  text-decoration: none;
  background-color: #e6e6e6;
  *background-color: #d9d9d9;
  /* Buttons in IE7 don't get borders, so darken on hover */

  background-position: 0 -15px;
  -webkit-transition: background-position 0.1s linear;
  -moz-transition: background-position 0.1s linear;
  -o-transition: background-position 0.1s linear;
  transition: background-position 0.1s linear;
}
.btn:focus {
  outline: thin dotted #333;
  outline: 5px auto -webkit-focus-ring-color;
  outline-offset: -2px;
}
.btn.active,
.btn:active {
  background-color: #e6e6e6;
  background-color: #d9d9d9 \9;
  background-image: none;
  outline: 0;
  -webkit-box-shadow: inset 0 2px 4px rgba(0,0,0,.15), 0 1px 2px rgba(0,0,0,.05);
  -moz-box-shadow: inset 0 2px 4px rgba(0,0,0,.15), 0 1px 2px rgba(0,0,0,.05);
  box-shadow: inset 0 2px 4px rgba(0,0,0,.15), 0 1px 2px rgba(0,0,0,.05);
}
.btn.disabled,
.btn[disabled] {
  cursor: default;
  background-color: #e6e6e6;
  background-image: none;
  opacity: 0.65;
  filter: alpha(opacity=65);
  -webkit-box-shadow: none;
  -moz-box-shadow: none;
  box-shadow: none;
}
.btn-large {
  padding: 11px 19px;
  font-size: 17.5px;
  -webkit-border-radius: 6px;
  -moz-border-radius: 6px;
  border-radius: 6px;
}
.btn-large [class^="icon-"],
.btn-large [class*=" icon-"] {
  margin-top: 2px;
}
.btn-small {
  padding: 2px 10px;
  font-size: 11.9px;
  -webkit-border-radius: 3px;
  -moz-border-radius: 3px;
  border-radius: 3px;
}
.btn-small [class^="icon-"],
.btn-small [class*=" icon-"] {
  margin-top: 0;
}
.btn-mini {
  padding: 1px 6px;
  font-size: 10.5px;
  -webkit-border-radius: 3px;
  -moz-border-radius: 3px;
  border-radius: 3px;
}
.btn-block {
  display: block;
  width: 100%;
  padding-left: 0;
  padding-right: 0;
  -webkit-box-sizing: border-box;
  -moz-box-sizing: border-box;
  box-sizing: border-box;
}
.btn-block + .btn-block {
  margin-top: 5px;
}
input[type="submit"].btn-block,
input[type="reset"].btn-block,
input[type="button"].btn-block {
  width: 100%;
}
.btn-primary.active,
.btn-warning.active,
.btn-danger.active,
.btn-success.active,
.btn-info.active,
.btn-inverse.active {
  color: rgba(255, 255, 255, 0.75);
}
.btn {
  border-color: #c5c5c5;
  border-color: rgba(0, 0, 0, 0.15) rgba(0, 0, 0, 0.15) rgba(0, 0, 0, 0.25);
}
.btn-primary {
  color: #ffffff;
  text-shadow: 0 -1px 0 rgba(0, 0, 0, 0.25);
  background-color: #006dcc;
  background-image: -moz-linear-gradient(top, #0088cc, #0044cc);
  background-image: -webkit-gradient(linear, 0 0, 0 100%, from(#0088cc), to(#0044cc));
  background-image: -webkit-linear-gradient(top, #0088cc, #0044cc);
  background-image: -o-linear-gradient(top, #0088cc, #0044cc);
  background-image: linear-gradient(to bottom, #0088cc, #0044cc);
  background-repeat: repeat-x;
  filter: progid:DXImageTransform.Microsoft.gradient(startColorstr='#ff0088cc', endColorstr='#ff0044cc', GradientType=0);
  border-color: #0044cc #0044cc #002a80;
  border-color: rgba(0, 0, 0, 0.1) rgba(0, 0, 0, 0.1) rgba(0, 0, 0, 0.25);
  *background-color: #0044cc;
  /* Darken IE7 buttons by default so they stand out more given they won't have borders */

  filter: progid:DXImageTransform.Microsoft.gradient(enabled = false);
}
.btn-primary:hover,
.btn-primary:active,
.btn-primary.active,
.btn-primary.disabled,
.btn-primary[disabled] {
  color: #ffffff;
  background-color: #0044cc;
  *background-color: #003bb3;
}
.btn-primary:active,
.btn-primary.active {
  background-color: #003399 \9;
}
.btn-warning {
  color: #ffffff;
  text-shadow: 0 -1px 0 rgba(0, 0, 0, 0.25);
  background-color: #faa732;
  background-image: -moz-linear-gradient(top, #fbb450, #f89406);
  background-image: -webkit-gradient(linear, 0 0, 0 100%, from(#fbb450), to(#f89406));
  background-image: -webkit-linear-gradient(top, #fbb450, #f89406);
  background-image: -o-linear-gradient(top, #fbb450, #f89406);
  background-image: linear-gradient(to bottom, #fbb450, #f89406);
  background-repeat: repeat-x;
  filter: progid:DXImageTransform.Microsoft.gradient(startColorstr='#fffbb450', endColorstr='#fff89406', GradientType=0);
  border-color: #f89406 #f89406 #ad6704;
  border-color: rgba(0, 0, 0, 0.1) rgba(0, 0, 0, 0.1) rgba(0, 0, 0, 0.25);
  *background-color: #f89406;
  /* Darken IE7 buttons by default so they stand out more given they won't have borders */

  filter: progid:DXImageTransform.Microsoft.gradient(enabled = false);
}
.btn-warning:hover,
.btn-warning:active,
.btn-warning.active,
.btn-warning.disabled,
.btn-warning[disabled] {
  color: #ffffff;
  background-color: #f89406;
  *background-color: #df8505;
}
.btn-warning:active,
.btn-warning.active {
  background-color: #c67605 \9;
}
.btn-danger {
  color: #ffffff;
  text-shadow: 0 -1px 0 rgba(0, 0, 0, 0.25);
  background-color: #da4f49;
  background-image: -moz-linear-gradient(top, #ee5f5b, #bd362f);
  background-image: -webkit-gradient(linear, 0 0, 0 100%, from(#ee5f5b), to(#bd362f));
  background-image: -webkit-linear-gradient(top, #ee5f5b, #bd362f);
  background-image: -o-linear-gradient(top, #ee5f5b, #bd362f);
  background-image: linear-gradient(to bottom, #ee5f5b, #bd362f);
  background-repeat: repeat-x;
  filter: progid:DXImageTransform.Microsoft.gradient(startColorstr='#ffee5f5b', endColorstr='#ffbd362f', GradientType=0);
  border-color: #bd362f #bd362f #802420;
  border-color: rgba(0, 0, 0, 0.1) rgba(0, 0, 0, 0.1) rgba(0, 0, 0, 0.25);
  *background-color: #bd362f;
  /* Darken IE7 buttons by default so they stand out more given they won't have borders */

  filter: progid:DXImageTransform.Microsoft.gradient(enabled = false);
}
.btn-danger:hover,
.btn-danger:active,
.btn-danger.active,
.btn-danger.disabled,
.btn-danger[disabled] {
  color: #ffffff;
  background-color: #bd362f;
  *background-color: #a9302a;
}
.btn-danger:active,
.btn-danger.active {
  background-color: #942a25 \9;
}
.btn-success {
  color: #ffffff;
  text-shadow: 0 -1px 0 rgba(0, 0, 0, 0.25);
  background-color: #5bb75b;
  background-image: -moz-linear-gradient(top, #62c462, #51a351);
  background-image: -webkit-gradient(linear, 0 0, 0 100%, from(#62c462), to(#51a351));
  background-image: -webkit-linear-gradient(top, #62c462, #51a351);
  background-image: -o-linear-gradient(top, #62c462, #51a351);
  background-image: linear-gradient(to bottom, #62c462, #51a351);
  background-repeat: repeat-x;
  filter: progid:DXImageTransform.Microsoft.gradient(startColorstr='#ff62c462', endColorstr='#ff51a351', GradientType=0);
  border-color: #51a351 #51a351 #387038;
  border-color: rgba(0, 0, 0, 0.1) rgba(0, 0, 0, 0.1) rgba(0, 0, 0, 0.25);
  *background-color: #51a351;
  /* Darken IE7 buttons by default so they stand out more given they won't have borders */

  filter: progid:DXImageTransform.Microsoft.gradient(enabled = false);
}
.btn-success:hover,
.btn-success:active,
.btn-success.active,
.btn-success.disabled,
.btn-success[disabled] {
  color: #ffffff;
  background-color: #51a351;
  *background-color: #499249;
}
.btn-success:active,
.btn-success.active {
  background-color: #408140 \9;
}
.btn-info {
  color: #ffffff;
  text-shadow: 0 -1px 0 rgba(0, 0, 0, 0.25);
  background-color: #49afcd;
  background-image: -moz-linear-gradient(top, #5bc0de, #2f96b4);
  background-image: -webkit-gradient(linear, 0 0, 0 100%, from(#5bc0de), to(#2f96b4));
  background-image: -webkit-linear-gradient(top, #5bc0de, #2f96b4);
  background-image: -o-linear-gradient(top, #5bc0de, #2f96b4);
  background-image: linear-gradient(to bottom, #5bc0de, #2f96b4);
  background-repeat: repeat-x;
  filter: progid:DXImageTransform.Microsoft.gradient(startColorstr='#ff5bc0de', endColorstr='#ff2f96b4', GradientType=0);
  border-color: #2f96b4 #2f96b4 #1f6377;
  border-color: rgba(0, 0, 0, 0.1) rgba(0, 0, 0, 0.1) rgba(0, 0, 0, 0.25);
  *background-color: #2f96b4;
  /* Darken IE7 buttons by default so they stand out more given they won't have borders */

  filter: progid:DXImageTransform.Microsoft.gradient(enabled = false);
}
.btn-info:hover,
.btn-info:active,
.btn-info.active,
.btn-info.disabled,
.btn-info[disabled] {
  color: #ffffff;
  background-color: #2f96b4;
  *background-color: #2a85a0;
}
.btn-info:active,
.btn-info.active {
  background-color: #24748c \9;
}
.btn-inverse {
  color: #ffffff;
  text-shadow: 0 -1px 0 rgba(0, 0, 0, 0.25);
  background-color: #363636;
  background-image: -moz-linear-gradient(top, #444444, #222222);
  background-image: -webkit-gradient(linear, 0 0, 0 100%, from(#444444), to(#222222));
  background-image: -webkit-linear-gradient(top, #444444, #222222);
  background-image: -o-linear-gradient(top, #444444, #222222);
  background-image: linear-gradient(to bottom, #444444, #222222);
  background-repeat: repeat-x;
  filter: progid:DXImageTransform.Microsoft.gradient(startColorstr='#ff444444', endColorstr='#ff222222', GradientType=0);
  border-color: #222222 #222222 #000000;
  border-color: rgba(0, 0, 0, 0.1) rgba(0, 0, 0, 0.1) rgba(0, 0, 0, 0.25);
  *background-color: #222222;
  /* Darken IE7 buttons by default so they stand out more given they won't have borders */

  filter: progid:DXImageTransform.Microsoft.gradient(enabled = false);
}
.btn-inverse:hover,
.btn-inverse:active,
.btn-inverse.active,
.btn-inverse.disabled,
.btn-inverse[disabled] {
  color: #ffffff;
  background-color: #222222;
  *background-color: #151515;
}
.btn-inverse:active,
.btn-inverse.active {
  background-color: #080808 \9;
}
button.btn,
input[type="submit"].btn {
  *padding-top: 3px;
  *padding-bottom: 3px;
}
button.btn::-moz-focus-inner,
input[type="submit"].btn::-moz-focus-inner {
  padding: 0;
  border: 0;
}
button.btn.btn-large,
input[type="submit"].btn.btn-large {
  *padding-top: 7px;
  *padding-bottom: 7px;
}
button.btn.btn-small,
input[type="submit"].btn.btn-small {
  *padding-top: 3px;
  *padding-bottom: 3px;
}
button.btn.btn-mini,
input[type="submit"].btn.btn-mini {
  *padding-top: 1px;
  *padding-bottom: 1px;
}
.btn-link,
.btn-link:active,
.btn-link[disabled] {
  background-color: transparent;
  background-image: none;
  -webkit-box-shadow: none;
  -moz-box-shadow: none;
  box-shadow: none;
}
.btn-link {
  border-color: transparent;
  cursor: pointer;
  color: #0088cc;
  -webkit-border-radius: 0;
  -moz-border-radius: 0;
  border-radius: 0;
}
.btn-link:hover {
  color: #005580;
  text-decoration: underline;
  background-color: transparent;
}
.btn-link[disabled]:hover {
  color: #333333;
  text-decoration: none;
}
.btn-group {
  position: relative;
  display: inline-block;
  *display: inline;
  /* IE7 inline-block hack */

  *zoom: 1;
  font-size: 0;
  vertical-align: middle;
  white-space: nowrap;
  *margin-left: .3em;
}
.btn-group:first-child {
  *margin-left: 0;
}
.btn-group + .btn-group {
  margin-left: 5px;
}
.btn-toolbar {
  font-size: 0;
  margin-top: 10px;
  margin-bottom: 10px;
}
.btn-toolbar .btn + .btn,
.btn-toolbar .btn-group + .btn,
.btn-toolbar .btn + .btn-group {
  margin-left: 5px;
}
.btn-group > .btn {
  position: relative;
  -webkit-border-radius: 0;
  -moz-border-radius: 0;
  border-radius: 0;
}
.btn-group > .btn + .btn {
  margin-left: -1px;
}
.btn-group > .btn,
.btn-group > .dropdown-menu {
  font-size: 14px;
}
.btn-group > .btn-mini {
  font-size: 11px;
}
.btn-group > .btn-small {
  font-size: 12px;
}
.btn-group > .btn-large {
  font-size: 16px;
}
.btn-group > .btn:first-child {
  margin-left: 0;
  -webkit-border-top-left-radius: 4px;
  -moz-border-radius-topleft: 4px;
  border-top-left-radius: 4px;
  -webkit-border-bottom-left-radius: 4px;
  -moz-border-radius-bottomleft: 4px;
  border-bottom-left-radius: 4px;
}
.btn-group > .btn:last-child,
.btn-group > .dropdown-toggle {
  -webkit-border-top-right-radius: 4px;
  -moz-border-radius-topright: 4px;
  border-top-right-radius: 4px;
  -webkit-border-bottom-right-radius: 4px;
  -moz-border-radius-bottomright: 4px;
  border-bottom-right-radius: 4px;
}
.btn-group > .btn.large:first-child {
  margin-left: 0;
  -webkit-border-top-left-radius: 6px;
  -moz-border-radius-topleft: 6px;
  border-top-left-radius: 6px;
  -webkit-border-bottom-left-radius: 6px;
  -moz-border-radius-bottomleft: 6px;
  border-bottom-left-radius: 6px;
}
.btn-group > .btn.large:last-child,
.btn-group > .large.dropdown-toggle {
  -webkit-border-top-right-radius: 6px;
  -moz-border-radius-topright: 6px;
  border-top-right-radius: 6px;
  -webkit-border-bottom-right-radius: 6px;
  -moz-border-radius-bottomright: 6px;
  border-bottom-right-radius: 6px;
}
.btn-group > .btn:hover,
.btn-group > .btn:focus,
.btn-group > .btn:active,
.btn-group > .btn.active {
  z-index: 2;
}
.btn-group .dropdown-toggle:active,
.btn-group.open .dropdown-toggle {
  outline: 0;
}
.btn-group > .btn + .dropdown-toggle {
  padding-left: 8px;
  padding-right: 8px;
  -webkit-box-shadow: inset 1px 0 0 rgba(255,255,255,.125), inset 0 1px 0 rgba(255,255,255,.2), 0 1px 2px rgba(0,0,0,.05);
  -moz-box-shadow: inset 1px 0 0 rgba(255,255,255,.125), inset 0 1px 0 rgba(255,255,255,.2), 0 1px 2px rgba(0,0,0,.05);
  box-shadow: inset 1px 0 0 rgba(255,255,255,.125), inset 0 1px 0 rgba(255,255,255,.2), 0 1px 2px rgba(0,0,0,.05);
  *padding-top: 5px;
  *padding-bottom: 5px;
}
.btn-group > .btn-mini + .dropdown-toggle {
  padding-left: 5px;
  padding-right: 5px;
  *padding-top: 2px;
  *padding-bottom: 2px;
}
.btn-group > .btn-small + .dropdown-toggle {
  *padding-top: 5px;
  *padding-bottom: 4px;
}
.btn-group > .btn-large + .dropdown-toggle {
  padding-left: 12px;
  padding-right: 12px;
  *padding-top: 7px;
  *padding-bottom: 7px;
}
.btn-group.open .dropdown-toggle {
  background-image: none;
  -webkit-box-shadow: inset 0 2px 4px rgba(0,0,0,.15), 0 1px 2px rgba(0,0,0,.05);
  -moz-box-shadow: inset 0 2px 4px rgba(0,0,0,.15), 0 1px 2px rgba(0,0,0,.05);
  box-shadow: inset 0 2px 4px rgba(0,0,0,.15), 0 1px 2px rgba(0,0,0,.05);
}
.btn-group.open .btn.dropdown-toggle {
  background-color: #e6e6e6;
}
.btn-group.open .btn-primary.dropdown-toggle {
  background-color: #0044cc;
}
.btn-group.open .btn-warning.dropdown-toggle {
  background-color: #f89406;
}
.btn-group.open .btn-danger.dropdown-toggle {
  background-color: #bd362f;
}
.btn-group.open .btn-success.dropdown-toggle {
  background-color: #51a351;
}
.btn-group.open .btn-info.dropdown-toggle {
  background-color: #2f96b4;
}
.btn-group.open .btn-inverse.dropdown-toggle {
  background-color: #222222;
}
.btn .caret {
  margin-top: 8px;
  margin-left: 0;
}
.btn-mini .caret,
.btn-small .caret,
.btn-large .caret {
  margin-top: 6px;
}
.btn-large .caret {
  border-left-width: 5px;
  border-right-width: 5px;
  border-top-width: 5px;
}
.dropup .btn-large .caret {
  border-bottom-width: 5px;
}
.btn-primary .caret,
.btn-warning .caret,
.btn-danger .caret,
.btn-info .caret,
.btn-success .caret,
.btn-inverse .caret {
  border-top-color: #ffffff;
  border-bottom-color: #ffffff;
}
.btn-group-vertical {
  display: inline-block;
  *display: inline;
  /* IE7 inline-block hack */

  *zoom: 1;
}
.btn-group-vertical .btn {
  display: block;
  float: none;
  width: 100%;
  -webkit-border-radius: 0;
  -moz-border-radius: 0;
  border-radius: 0;
}
.btn-group-vertical .btn + .btn {
  margin-left: 0;
  margin-top: -1px;
}
.btn-group-vertical .btn:first-child {
  -webkit-border-radius: 4px 4px 0 0;
  -moz-border-radius: 4px 4px 0 0;
  border-radius: 4px 4px 0 0;
}
.btn-group-vertical .btn:last-child {
  -webkit-border-radius: 0 0 4px 4px;
  -moz-border-radius: 0 0 4px 4px;
  border-radius: 0 0 4px 4px;
}
.btn-group-vertical .btn-large:first-child {
  -webkit-border-radius: 6px 6px 0 0;
  -moz-border-radius: 6px 6px 0 0;
  border-radius: 6px 6px 0 0;
}
.btn-group-vertical .btn-large:last-child {
  -webkit-border-radius: 0 0 6px 6px;
  -moz-border-radius: 0 0 6px 6px;
  border-radius: 0 0 6px 6px;
}
.nav {
  margin-left: 0;
  margin-bottom: 20px;
  list-style: none;
}
.nav > li > a {
  display: block;
}
.nav > li > a:hover {
  text-decoration: none;
  background-color: #eeeeee;
}
.nav > .pull-right {
  float: right;
}
.nav-header {
  display: block;
  padding: 3px 15px;
  font-size: 11px;
  font-weight: bold;
  line-height: 20px;
  color: #999999;
  text-shadow: 0 1px 0 rgba(255, 255, 255, 0.5);
  text-transform: uppercase;
}
.nav li + .nav-header {
  margin-top: 9px;
}
.nav-list {
  padding-left: 15px;
  padding-right: 15px;
  margin-bottom: 0;
}
.nav-list > li > a,
.nav-list .nav-header {
  margin-left: -15px;
  margin-right: -15px;
  text-shadow: 0 1px 0 rgba(255, 255, 255, 0.5);
}
.nav-list > li > a {
  padding: 3px 15px;
}
.nav-list > .active > a,
.nav-list > .active > a:hover {
  color: #ffffff;
  text-shadow: 0 -1px 0 rgba(0, 0, 0, 0.2);
  background-color: #0088cc;
}
.nav-list [class^="icon-"],
.nav-list [class*=" icon-"] {
  margin-right: 2px;
}
.nav-list .divider {
  *width: 100%;
  height: 1px;
  margin: 9px 1px;
  *margin: -5px 0 5px;
  overflow: hidden;
  background-color: #e5e5e5;
  border-bottom: 1px solid #ffffff;
}
.nav-tabs,
.nav-pills {
  *zoom: 1;
}
.nav-tabs:before,
.nav-pills:before,
.nav-tabs:after,
.nav-pills:after {
  display: table;
  content: "";
  line-height: 0;
}
.nav-tabs:after,
.nav-pills:after {
  clear: both;
}
.nav-tabs > li,
.nav-pills > li {
  float: left;
}
.nav-tabs > li > a,
.nav-pills > li > a {
  padding-right: 12px;
  padding-left: 12px;
  margin-right: 2px;
  line-height: 14px;
}
.nav-tabs {
  border-bottom: 1px solid #ddd;
}
.nav-tabs > li {
  margin-bottom: -1px;
}
.nav-tabs > li > a {
  padding-top: 8px;
  padding-bottom: 8px;
  line-height: 20px;
  border: 1px solid transparent;
  -webkit-border-radius: 4px 4px 0 0;
  -moz-border-radius: 4px 4px 0 0;
  border-radius: 4px 4px 0 0;
}
.nav-tabs > li > a:hover {
  border-color: #eeeeee #eeeeee #dddddd;
}
.nav-tabs > .active > a,
.nav-tabs > .active > a:hover {
  color: #555555;
  background-color: #ffffff;
  border: 1px solid #ddd;
  border-bottom-color: transparent;
  cursor: default;
}
.nav-pills > li > a {
  padding-top: 8px;
  padding-bottom: 8px;
  margin-top: 2px;
  margin-bottom: 2px;
  -webkit-border-radius: 5px;
  -moz-border-radius: 5px;
  border-radius: 5px;
}
.nav-pills > .active > a,
.nav-pills > .active > a:hover {
  color: #ffffff;
  background-color: #0088cc;
}
.nav-stacked > li {
  float: none;
}
.nav-stacked > li > a {
  margin-right: 0;
}
.nav-tabs.nav-stacked {
  border-bottom: 0;
}
.nav-tabs.nav-stacked > li > a {
  border: 1px solid #ddd;
  -webkit-border-radius: 0;
  -moz-border-radius: 0;
  border-radius: 0;
}
.nav-tabs.nav-stacked > li:first-child > a {
  -webkit-border-top-right-radius: 4px;
  -moz-border-radius-topright: 4px;
  border-top-right-radius: 4px;
  -webkit-border-top-left-radius: 4px;
  -moz-border-radius-topleft: 4px;
  border-top-left-radius: 4px;
}
.nav-tabs.nav-stacked > li:last-child > a {
  -webkit-border-bottom-right-radius: 4px;
  -moz-border-radius-bottomright: 4px;
  border-bottom-right-radius: 4px;
  -webkit-border-bottom-left-radius: 4px;
  -moz-border-radius-bottomleft: 4px;
  border-bottom-left-radius: 4px;
}
.nav-tabs.nav-stacked > li > a:hover {
  border-color: #ddd;
  z-index: 2;
}
.nav-pills.nav-stacked > li > a {
  margin-bottom: 3px;
}
.nav-pills.nav-stacked > li:last-child > a {
  margin-bottom: 1px;
}
.nav-tabs .dropdown-menu {
  -webkit-border-radius: 0 0 6px 6px;
  -moz-border-radius: 0 0 6px 6px;
  border-radius: 0 0 6px 6px;
}
.nav-pills .dropdown-menu {
  -webkit-border-radius: 6px;
  -moz-border-radius: 6px;
  border-radius: 6px;
}
.nav .dropdown-toggle .caret {
  border-top-color: #0088cc;
  border-bottom-color: #0088cc;
  margin-top: 6px;
}
.nav .dropdown-toggle:hover .caret {
  border-top-color: #005580;
  border-bottom-color: #005580;
}
/* move down carets for tabs */
.nav-tabs .dropdown-toggle .caret {
  margin-top: 8px;
}
.nav .active .dropdown-toggle .caret {
  border-top-color: #fff;
  border-bottom-color: #fff;
}
.nav-tabs .active .dropdown-toggle .caret {
  border-top-color: #555555;
  border-bottom-color: #555555;
}
.nav > .dropdown.active > a:hover {
  cursor: pointer;
}
.nav-tabs .open .dropdown-toggle,
.nav-pills .open .dropdown-toggle,
.nav > li.dropdown.open.active > a:hover {
  color: #ffffff;
  background-color: #999999;
  border-color: #999999;
}
.nav li.dropdown.open .caret,
.nav li.dropdown.open.active .caret,
.nav li.dropdown.open a:hover .caret {
  border-top-color: #ffffff;
  border-bottom-color: #ffffff;
  opacity: 1;
  filter: alpha(opacity=100);
}
.tabs-stacked .open > a:hover {
  border-color: #999999;
}
.tabbable {
  *zoom: 1;
}
.tabbable:before,
.tabbable:after {
  display: table;
  content: "";
  line-height: 0;
}
.tabbable:after {
  clear: both;
}
.tab-content {
  overflow: auto;
}
.tabs-below > .nav-tabs,
.tabs-right > .nav-tabs,
.tabs-left > .nav-tabs {
  border-bottom: 0;
}
.tab-content > .tab-pane,
.pill-content > .pill-pane {
  display: none;
}
.tab-content > .active,
.pill-content > .active {
  display: block;
}
.tabs-below > .nav-tabs {
  border-top: 1px solid #ddd;
}
.tabs-below > .nav-tabs > li {
  margin-top: -1px;
  margin-bottom: 0;
}
.tabs-below > .nav-tabs > li > a {
  -webkit-border-radius: 0 0 4px 4px;
  -moz-border-radius: 0 0 4px 4px;
  border-radius: 0 0 4px 4px;
}
.tabs-below > .nav-tabs > li > a:hover {
  border-bottom-color: transparent;
  border-top-color: #ddd;
}
.tabs-below > .nav-tabs > .active > a,
.tabs-below > .nav-tabs > .active > a:hover {
  border-color: transparent #ddd #ddd #ddd;
}
.tabs-left > .nav-tabs > li,
.tabs-right > .nav-tabs > li {
  float: none;
}
.tabs-left > .nav-tabs > li > a,
.tabs-right > .nav-tabs > li > a {
  min-width: 74px;
  margin-right: 0;
  margin-bottom: 3px;
}
.tabs-left > .nav-tabs {
  float: left;
  margin-right: 19px;
  border-right: 1px solid #ddd;
}
.tabs-left > .nav-tabs > li > a {
  margin-right: -1px;
  -webkit-border-radius: 4px 0 0 4px;
  -moz-border-radius: 4px 0 0 4px;
  border-radius: 4px 0 0 4px;
}
.tabs-left > .nav-tabs > li > a:hover {
  border-color: #eeeeee #dddddd #eeeeee #eeeeee;
}
.tabs-left > .nav-tabs .active > a,
.tabs-left > .nav-tabs .active > a:hover {
  border-color: #ddd transparent #ddd #ddd;
  *border-right-color: #ffffff;
}
.tabs-right > .nav-tabs {
  float: right;
  margin-left: 19px;
  border-left: 1px solid #ddd;
}
.tabs-right > .nav-tabs > li > a {
  margin-left: -1px;
  -webkit-border-radius: 0 4px 4px 0;
  -moz-border-radius: 0 4px 4px 0;
  border-radius: 0 4px 4px 0;
}
.tabs-right > .nav-tabs > li > a:hover {
  border-color: #eeeeee #eeeeee #eeeeee #dddddd;
}
.tabs-right > .nav-tabs .active > a,
.tabs-right > .nav-tabs .active > a:hover {
  border-color: #ddd #ddd #ddd transparent;
  *border-left-color: #ffffff;
}
.nav > .disabled > a {
  color: #999999;
}
.nav > .disabled > a:hover {
  text-decoration: none;
  background-color: transparent;
  cursor: default;
}
.navbar {
  overflow: visible;
  margin-bottom: 20px;
  color: #777777;
  *position: relative;
  *z-index: 2;
}
.navbar-inner {
  min-height: 40px;
  padding-left: 20px;
  padding-right: 20px;
  background-color: #fafafa;
  background-image: -moz-linear-gradient(top, #ffffff, #f2f2f2);
  background-image: -webkit-gradient(linear, 0 0, 0 100%, from(#ffffff), to(#f2f2f2));
  background-image: -webkit-linear-gradient(top, #ffffff, #f2f2f2);
  background-image: -o-linear-gradient(top, #ffffff, #f2f2f2);
  background-image: linear-gradient(to bottom, #ffffff, #f2f2f2);
  background-repeat: repeat-x;
  filter: progid:DXImageTransform.Microsoft.gradient(startColorstr='#ffffffff', endColorstr='#fff2f2f2', GradientType=0);
  border: 1px solid #d4d4d4;
  -webkit-border-radius: 4px;
  -moz-border-radius: 4px;
  border-radius: 4px;
  -webkit-box-shadow: 0 1px 4px rgba(0, 0, 0, 0.065);
  -moz-box-shadow: 0 1px 4px rgba(0, 0, 0, 0.065);
  box-shadow: 0 1px 4px rgba(0, 0, 0, 0.065);
  *zoom: 1;
}
.navbar-inner:before,
.navbar-inner:after {
  display: table;
  content: "";
  line-height: 0;
}
.navbar-inner:after {
  clear: both;
}
.navbar .container {
  width: auto;
}
.nav-collapse.collapse {
  height: auto;
  overflow: visible;
}
.navbar .brand {
  float: left;
  display: block;
  padding: 10px 20px 10px;
  margin-left: -20px;
  font-size: 20px;
  font-weight: 200;
  color: #777777;
  text-shadow: 0 1px 0 #ffffff;
}
.navbar .brand:hover {
  text-decoration: none;
}
.navbar-text {
  margin-bottom: 0;
  line-height: 40px;
}
.navbar-link {
  color: #777777;
}
.navbar-link:hover {
  color: #333333;
}
.navbar .divider-vertical {
  height: 40px;
  margin: 0 9px;
  border-left: 1px solid #f2f2f2;
  border-right: 1px solid #ffffff;
}
.navbar .btn,
.navbar .btn-group {
  margin-top: 5px;
}
.navbar .btn-group .btn,
.navbar .input-prepend .btn,
.navbar .input-append .btn {
  margin-top: 0;
}
.navbar-form {
  margin-bottom: 0;
  *zoom: 1;
}
.navbar-form:before,
.navbar-form:after {
  display: table;
  content: "";
  line-height: 0;
}
.navbar-form:after {
  clear: both;
}
.navbar-form input,
.navbar-form select,
.navbar-form .radio,
.navbar-form .checkbox {
  margin-top: 5px;
}
.navbar-form input,
.navbar-form select,
.navbar-form .btn {
  display: inline-block;
  margin-bottom: 0;
}
.navbar-form input[type="image"],
.navbar-form input[type="checkbox"],
.navbar-form input[type="radio"] {
  margin-top: 3px;
}
.navbar-form .input-append,
.navbar-form .input-prepend {
  margin-top: 6px;
  white-space: nowrap;
}
.navbar-form .input-append input,
.navbar-form .input-prepend input {
  margin-top: 0;
}
.navbar-search {
  position: relative;
  float: left;
  margin-top: 5px;
  margin-bottom: 0;
}
.navbar-search .search-query {
  margin-bottom: 0;
  padding: 4px 14px;
  font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
  font-size: 13px;
  font-weight: normal;
  line-height: 1;
  -webkit-border-radius: 15px;
  -moz-border-radius: 15px;
  border-radius: 15px;
}
.navbar-static-top {
  position: static;
  margin-bottom: 0;
}
.navbar-static-top .navbar-inner {
  -webkit-border-radius: 0;
  -moz-border-radius: 0;
  border-radius: 0;
}
.navbar-fixed-top,
.navbar-fixed-bottom {
  position: fixed;
  right: 0;
  left: 0;
  z-index: 1030;
  margin-bottom: 0;
}
.navbar-fixed-top .navbar-inner,
.navbar-static-top .navbar-inner {
  border-width: 0 0 1px;
}
.navbar-fixed-bottom .navbar-inner {
  border-width: 1px 0 0;
}
.navbar-fixed-top .navbar-inner,
.navbar-fixed-bottom .navbar-inner {
  padding-left: 0;
  padding-right: 0;
  -webkit-border-radius: 0;
  -moz-border-radius: 0;
  border-radius: 0;
}
.navbar-static-top .container,
.navbar-fixed-top .container,
.navbar-fixed-bottom .container {
  width: 940px;
}
.navbar-fixed-top {
  top: 0;
}
.navbar-fixed-top .navbar-inner,
.navbar-static-top .navbar-inner {
  -webkit-box-shadow: 0 1px 10px rgba(0,0,0,.1);
  -moz-box-shadow: 0 1px 10px rgba(0,0,0,.1);
  box-shadow: 0 1px 10px rgba(0,0,0,.1);
}
.navbar-fixed-bottom {
  bottom: 0;
}
.navbar-fixed-bottom .navbar-inner {
  -webkit-box-shadow: 0 -1px 10px rgba(0,0,0,.1);
  -moz-box-shadow: 0 -1px 10px rgba(0,0,0,.1);
  box-shadow: 0 -1px 10px rgba(0,0,0,.1);
}
.navbar .nav {
  position: relative;
  left: 0;
  display: block;
  float: left;
  margin: 0 10px 0 0;
}
.navbar .nav.pull-right {
  float: right;
  margin-right: 0;
}
.navbar .nav > li {
  float: left;
}
.navbar .nav > li > a {
  float: none;
  padding: 10px 15px 10px;
  color: #777777;
  text-decoration: none;
  text-shadow: 0 1px 0 #ffffff;
}
.navbar .nav .dropdown-toggle .caret {
  margin-top: 8px;
}
.navbar .nav > li > a:focus,
.navbar .nav > li > a:hover {
  background-color: transparent;
  color: #333333;
  text-decoration: none;
}
.navbar .nav > .active > a,
.navbar .nav > .active > a:hover,
.navbar .nav > .active > a:focus {
  color: #555555;
  text-decoration: none;
  background-color: #e5e5e5;
  -webkit-box-shadow: inset 0 3px 8px rgba(0, 0, 0, 0.125);
  -moz-box-shadow: inset 0 3px 8px rgba(0, 0, 0, 0.125);
  box-shadow: inset 0 3px 8px rgba(0, 0, 0, 0.125);
}
.navbar .btn-navbar {
  display: none;
  float: right;
  padding: 7px 10px;
  margin-left: 5px;
  margin-right: 5px;
  color: #ffffff;
  text-shadow: 0 -1px 0 rgba(0, 0, 0, 0.25);
  background-color: #ededed;
  background-image: -moz-linear-gradient(top, #f2f2f2, #e5e5e5);
  background-image: -webkit-gradient(linear, 0 0, 0 100%, from(#f2f2f2), to(#e5e5e5));
  background-image: -webkit-linear-gradient(top, #f2f2f2, #e5e5e5);
  background-image: -o-linear-gradient(top, #f2f2f2, #e5e5e5);
  background-image: linear-gradient(to bottom, #f2f2f2, #e5e5e5);
  background-repeat: repeat-x;
  filter: progid:DXImageTransform.Microsoft.gradient(startColorstr='#fff2f2f2', endColorstr='#ffe5e5e5', GradientType=0);
  border-color: #e5e5e5 #e5e5e5 #bfbfbf;
  border-color: rgba(0, 0, 0, 0.1) rgba(0, 0, 0, 0.1) rgba(0, 0, 0, 0.25);
  *background-color: #e5e5e5;
  /* Darken IE7 buttons by default so they stand out more given they won't have borders */

  filter: progid:DXImageTransform.Microsoft.gradient(enabled = false);
  -webkit-box-shadow: inset 0 1px 0 rgba(255,255,255,.1), 0 1px 0 rgba(255,255,255,.075);
  -moz-box-shadow: inset 0 1px 0 rgba(255,255,255,.1), 0 1px 0 rgba(255,255,255,.075);
  box-shadow: inset 0 1px 0 rgba(255,255,255,.1), 0 1px 0 rgba(255,255,255,.075);
}
.navbar .btn-navbar:hover,
.navbar .btn-navbar:active,
.navbar .btn-navbar.active,
.navbar .btn-navbar.disabled,
.navbar .btn-navbar[disabled] {
  color: #ffffff;
  background-color: #e5e5e5;
  *background-color: #d9d9d9;
}
.navbar .btn-navbar:active,
.navbar .btn-navbar.active {
  background-color: #cccccc \9;
}
.navbar .btn-navbar .icon-bar {
  display: block;
  width: 18px;
  height: 2px;
  background-color: #f5f5f5;
  -webkit-border-radius: 1px;
  -moz-border-radius: 1px;
  border-radius: 1px;
  -webkit-box-shadow: 0 1px 0 rgba(0, 0, 0, 0.25);
  -moz-box-shadow: 0 1px 0 rgba(0, 0, 0, 0.25);
  box-shadow: 0 1px 0 rgba(0, 0, 0, 0.25);
}
.btn-navbar .icon-bar + .icon-bar {
  margin-top: 3px;
}
.navbar .nav > li > .dropdown-menu:before {
  content: '';
  display: inline-block;
  border-left: 7px solid transparent;
  border-right: 7px solid transparent;
  border-bottom: 7px solid #ccc;
  border-bottom-color: rgba(0, 0, 0, 0.2);
  position: absolute;
  top: -7px;
  left: 9px;
}
.navbar .nav > li > .dropdown-menu:after {
  content: '';
  display: inline-block;
  border-left: 6px solid transparent;
  border-right: 6px solid transparent;
  border-bottom: 6px solid #ffffff;
  position: absolute;
  top: -6px;
  left: 10px;
}
.navbar-fixed-bottom .nav > li > .dropdown-menu:before {
  border-top: 7px solid #ccc;
  border-top-color: rgba(0, 0, 0, 0.2);
  border-bottom: 0;
  bottom: -7px;
  top: auto;
}
.navbar-fixed-bottom .nav > li > .dropdown-menu:after {
  border-top: 6px solid #ffffff;
  border-bottom: 0;
  bottom: -6px;
  top: auto;
}
.navbar .nav li.dropdown.open > .dropdown-toggle,
.navbar .nav li.dropdown.active > .dropdown-toggle,
.navbar .nav li.dropdown.open.active > .dropdown-toggle {
  background-color: #e5e5e5;
  color: #555555;
}
.navbar .nav li.dropdown > .dropdown-toggle .caret {
  border-top-color: #777777;
  border-bottom-color: #777777;
}
.navbar .nav li.dropdown.open > .dropdown-toggle .caret,
.navbar .nav li.dropdown.active > .dropdown-toggle .caret,
.navbar .nav li.dropdown.open.active > .dropdown-toggle .caret {
  border-top-color: #555555;
  border-bottom-color: #555555;
}
.navbar .pull-right > li > .dropdown-menu,
.navbar .nav > li > .dropdown-menu.pull-right {
  left: auto;
  right: 0;
}
.navbar .pull-right > li > .dropdown-menu:before,
.navbar .nav > li > .dropdown-menu.pull-right:before {
  left: auto;
  right: 12px;
}
.navbar .pull-right > li > .dropdown-menu:after,
.navbar .nav > li > .dropdown-menu.pull-right:after {
  left: auto;
  right: 13px;
}
.navbar .pull-right > li > .dropdown-menu .dropdown-menu,
.navbar .nav > li > .dropdown-menu.pull-right .dropdown-menu {
  left: auto;
  right: 100%;
  margin-left: 0;
  margin-right: -1px;
  -webkit-border-radius: 6px 0 6px 6px;
  -moz-border-radius: 6px 0 6px 6px;
  border-radius: 6px 0 6px 6px;
}
.navbar-inverse {
  color: #999999;
}
.navbar-inverse .navbar-inner {
  background-color: #1b1b1b;
  background-image: -moz-linear-gradient(top, #222222, #111111);
  background-image: -webkit-gradient(linear, 0 0, 0 100%, from(#222222), to(#111111));
  background-image: -webkit-linear-gradient(top, #222222, #111111);
  background-image: -o-linear-gradient(top, #222222, #111111);
  background-image: linear-gradient(to bottom, #222222, #111111);
  background-repeat: repeat-x;
  filter: progid:DXImageTransform.Microsoft.gradient(startColorstr='#ff222222', endColorstr='#ff111111', GradientType=0);
  border-color: #252525;
}
.navbar-inverse .brand,
.navbar-inverse .nav > li > a {
  color: #999999;
  text-shadow: 0 -1px 0 rgba(0, 0, 0, 0.25);
}
.navbar-inverse .brand:hover,
.navbar-inverse .nav > li > a:hover {
  color: #ffffff;
}
.navbar-inverse .nav > li > a:focus,
.navbar-inverse .nav > li > a:hover {
  background-color: transparent;
  color: #ffffff;
}
.navbar-inverse .nav .active > a,
.navbar-inverse .nav .active > a:hover,
.navbar-inverse .nav .active > a:focus {
  color: #ffffff;
  background-color: #111111;
}
.navbar-inverse .navbar-link {
  color: #999999;
}
.navbar-inverse .navbar-link:hover {
  color: #ffffff;
}
.navbar-inverse .divider-vertical {
  border-left-color: #111111;
  border-right-color: #222222;
}
.navbar-inverse .nav li.dropdown.open > .dropdown-toggle,
.navbar-inverse .nav li.dropdown.active > .dropdown-toggle,
.navbar-inverse .nav li.dropdown.open.active > .dropdown-toggle {
  background-color: #111111;
  color: #ffffff;
}
.navbar-inverse .nav li.dropdown > .dropdown-toggle .caret {
  border-top-color: #999999;
  border-bottom-color: #999999;
}
.navbar-inverse .nav li.dropdown.open > .dropdown-toggle .caret,
.navbar-inverse .nav li.dropdown.active > .dropdown-toggle .caret,
.navbar-inverse .nav li.dropdown.open.active > .dropdown-toggle .caret {
  border-top-color: #ffffff;
  border-bottom-color: #ffffff;
}
.navbar-inverse .navbar-search .search-query {
  color: #ffffff;
  background-color: #515151;
  border-color: #111111;
  -webkit-box-shadow: inset 0 1px 2px rgba(0,0,0,.1), 0 1px 0 rgba(255,255,255,.15);
  -moz-box-shadow: inset 0 1px 2px rgba(0,0,0,.1), 0 1px 0 rgba(255,255,255,.15);
  box-shadow: inset 0 1px 2px rgba(0,0,0,.1), 0 1px 0 rgba(255,255,255,.15);
  -webkit-transition: none;
  -moz-transition: none;
  -o-transition: none;
  transition: none;
}
.navbar-inverse .navbar-search .search-query:-moz-placeholder {
  color: #cccccc;
}
.navbar-inverse .navbar-search .search-query:-ms-input-placeholder {
  color: #cccccc;
}
.navbar-inverse .navbar-search .search-query::-webkit-input-placeholder {
  color: #cccccc;
}
.navbar-inverse .navbar-search .search-query:focus,
.navbar-inverse .navbar-search .search-query.focused {
  padding: 5px 15px;
  color: #333333;
  text-shadow: 0 1px 0 #ffffff;
  background-color: #ffffff;
  border: 0;
  -webkit-box-shadow: 0 0 3px rgba(0, 0, 0, 0.15);
  -moz-box-shadow: 0 0 3px rgba(0, 0, 0, 0.15);
  box-shadow: 0 0 3px rgba(0, 0, 0, 0.15);
  outline: 0;
}
.navbar-inverse .btn-navbar {
  color: #ffffff;
  text-shadow: 0 -1px 0 rgba(0, 0, 0, 0.25);
  background-color: #0e0e0e;
  background-image: -moz-linear-gradient(top, #151515, #040404);
  background-image: -webkit-gradient(linear, 0 0, 0 100%, from(#151515), to(#040404));
  background-image: -webkit-linear-gradient(top, #151515, #040404);
  background-image: -o-linear-gradient(top, #151515, #040404);
  background-image: linear-gradient(to bottom, #151515, #040404);
  background-repeat: repeat-x;
  filter: progid:DXImageTransform.Microsoft.gradient(startColorstr='#ff151515', endColorstr='#ff040404', GradientType=0);
  border-color: #040404 #040404 #000000;
  border-color: rgba(0, 0, 0, 0.1) rgba(0, 0, 0, 0.1) rgba(0, 0, 0, 0.25);
  *background-color: #040404;
  /* Darken IE7 buttons by default so they stand out more given they won't have borders */

  filter: progid:DXImageTransform.Microsoft.gradient(enabled = false);
}
.navbar-inverse .btn-navbar:hover,
.navbar-inverse .btn-navbar:active,
.navbar-inverse .btn-navbar.active,
.navbar-inverse .btn-navbar.disabled,
.navbar-inverse .btn-navbar[disabled] {
  color: #ffffff;
  background-color: #040404;
  *background-color: #000000;
}
.navbar-inverse .btn-navbar:active,
.navbar-inverse .btn-navbar.active {
  background-color: #000000 \9;
}
.breadcrumb {
  padding: 8px 15px;
  margin: 0 0 20px;
  list-style: none;
  background-color: #f5f5f5;
  -webkit-border-radius: 4px;
  -moz-border-radius: 4px;
  border-radius: 4px;
}
.breadcrumb li {
  display: inline-block;
  *display: inline;
  /* IE7 inline-block hack */

  *zoom: 1;
  text-shadow: 0 1px 0 #ffffff;
}
.breadcrumb .divider {
  padding: 0 5px;
  color: #ccc;
}
.breadcrumb .active {
  color: #999999;
}
.pagination {
  margin: 20px 0;
}
.pagination ul {
  display: inline-block;
  *display: inline;
  /* IE7 inline-block hack */

  *zoom: 1;
  margin-left: 0;
  margin-bottom: 0;
  -webkit-border-radius: 4px;
  -moz-border-radius: 4px;
  border-radius: 4px;
  -webkit-box-shadow: 0 1px 2px rgba(0, 0, 0, 0.05);
  -moz-box-shadow: 0 1px 2px rgba(0, 0, 0, 0.05);
  box-shadow: 0 1px 2px rgba(0, 0, 0, 0.05);
}
.pagination ul > li {
  display: inline;
}
.pagination ul > li > a,
.pagination ul > li > span {
  float: left;
  padding: 4px 12px;
  line-height: 20px;
  text-decoration: none;
  background-color: #ffffff;
  border: 1px solid #dddddd;
  border-left-width: 0;
}
.pagination ul > li > a:hover,
.pagination ul > .active > a,
.pagination ul > .active > span {
  background-color: #f5f5f5;
}
.pagination ul > .active > a,
.pagination ul > .active > span {
  color: #999999;
  cursor: default;
}
.pagination ul > .disabled > span,
.pagination ul > .disabled > a,
.pagination ul > .disabled > a:hover {
  color: #999999;
  background-color: transparent;
  cursor: default;
}
.pagination ul > li:first-child > a,
.pagination ul > li:first-child > span {
  border-left-width: 1px;
  -webkit-border-top-left-radius: 4px;
  -moz-border-radius-topleft: 4px;
  border-top-left-radius: 4px;
  -webkit-border-bottom-left-radius: 4px;
  -moz-border-radius-bottomleft: 4px;
  border-bottom-left-radius: 4px;
}
.pagination ul > li:last-child > a,
.pagination ul > li:last-child > span {
  -webkit-border-top-right-radius: 4px;
  -moz-border-radius-topright: 4px;
  border-top-right-radius: 4px;
  -webkit-border-bottom-right-radius: 4px;
  -moz-border-radius-bottomright: 4px;
  border-bottom-right-radius: 4px;
}
.pagination-centered {
  text-align: center;
}
.pagination-right {
  text-align: right;
}
.pagination-large ul > li > a,
.pagination-large ul > li > span {
  padding: 11px 19px;
  font-size: 17.5px;
}
.pagination-large ul > li:first-child > a,
.pagination-large ul > li:first-child > span {
  -webkit-border-top-left-radius: 6px;
  -moz-border-radius-topleft: 6px;
  border-top-left-radius: 6px;
  -webkit-border-bottom-left-radius: 6px;
  -moz-border-radius-bottomleft: 6px;
  border-bottom-left-radius: 6px;
}
.pagination-large ul > li:last-child > a,
.pagination-large ul > li:last-child > span {
  -webkit-border-top-right-radius: 6px;
  -moz-border-radius-topright: 6px;
  border-top-right-radius: 6px;
  -webkit-border-bottom-right-radius: 6px;
  -moz-border-radius-bottomright: 6px;
  border-bottom-right-radius: 6px;
}
.pagination-mini ul > li:first-child > a,
.pagination-small ul > li:first-child > a,
.pagination-mini ul > li:first-child > span,
.pagination-small ul > li:first-child > span {
  -webkit-border-top-left-radius: 3px;
  -moz-border-radius-topleft: 3px;
  border-top-left-radius: 3px;
  -webkit-border-bottom-left-radius: 3px;
  -moz-border-radius-bottomleft: 3px;
  border-bottom-left-radius: 3px;
}
.pagination-mini ul > li:last-child > a,
.pagination-small ul > li:last-child > a,
.pagination-mini ul > li:last-child > span,
.pagination-small ul > li:last-child > span {
  -webkit-border-top-right-radius: 3px;
  -moz-border-radius-topright: 3px;
  border-top-right-radius: 3px;
  -webkit-border-bottom-right-radius: 3px;
  -moz-border-radius-bottomright: 3px;
  border-bottom-right-radius: 3px;
}
.pagination-small ul > li > a,
.pagination-small ul > li > span {
  padding: 2px 10px;
  font-size: 11.9px;
}
.pagination-mini ul > li > a,
.pagination-mini ul > li > span {
  padding: 1px 6px;
  font-size: 10.5px;
}
.pager {
  margin: 20px 0;
  list-style: none;
  text-align: center;
  *zoom: 1;
}
.pager:before,
.pager:after {
  display: table;
  content: "";
  line-height: 0;
}
.pager:after {
  clear: both;
}
.pager li {
  display: inline;
}
.pager li > a,
.pager li > span {
  display: inline-block;
  padding: 5px 14px;
  background-color: #fff;
  border: 1px solid #ddd;
  -webkit-border-radius: 15px;
  -moz-border-radius: 15px;
  border-radius: 15px;
}
.pager li > a:hover {
  text-decoration: none;
  background-color: #f5f5f5;
}
.pager .next > a,
.pager .next > span {
  float: right;
}
.pager .previous > a,
.pager .previous > span {
  float: left;
}
.pager .disabled > a,
.pager .disabled > a:hover,
.pager .disabled > span {
  color: #999999;
  background-color: #fff;
  cursor: default;
}
.thumbnails {
  margin-left: -20px;
  list-style: none;
  *zoom: 1;
}
.thumbnails:before,
.thumbnails:after {
  display: table;
  content: "";
  line-height: 0;
}
.thumbnails:after {
  clear: both;
}
.row-fluid .thumbnails {
  margin-left: 0;
}
.thumbnails > li {
  float: left;
  margin-bottom: 20px;
  margin-left: 20px;
}
.thumbnail {
  display: block;
  padding: 4px;
  line-height: 20px;
  border: 1px solid #ddd;
  -webkit-border-radius: 4px;
  -moz-border-radius: 4px;
  border-radius: 4px;
  -webkit-box-shadow: 0 1px 3px rgba(0, 0, 0, 0.055);
  -moz-box-shadow: 0 1px 3px rgba(0, 0, 0, 0.055);
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.055);
  -webkit-transition: all 0.2s ease-in-out;
  -moz-transition: all 0.2s ease-in-out;
  -o-transition: all 0.2s ease-in-out;
  transition: all 0.2s ease-in-out;
}
a.thumbnail:hover {
  border-color: #0088cc;
  -webkit-box-shadow: 0 1px 4px rgba(0, 105, 214, 0.25);
  -moz-box-shadow: 0 1px 4px rgba(0, 105, 214, 0.25);
  box-shadow: 0 1px 4px rgba(0, 105, 214, 0.25);
}
.thumbnail > img {
  display: block;
  max-width: 100%;
  margin-left: auto;
  margin-right: auto;
}
.thumbnail .caption {
  padding: 9px;
  color: #555555;
}
.alert {
  padding: 8px 35px 8px 14px;
  margin-bottom: 20px;
  text-shadow: 0 1px 0 rgba(255, 255, 255, 0.5);
  background-color: #fcf8e3;
  border: 1px solid #fbeed5;
  -webkit-border-radius: 4px;
  -moz-border-radius: 4px;
  border-radius: 4px;
  color: #c09853;
}
.alert h4 {
  margin: 0;
}
.alert .close {
  position: relative;
  top: -2px;
  right: -21px;
  line-height: 20px;
}
.alert-success {
  background-color: #dff0d8;
  border-color: #d6e9c6;
  color: #468847;
}
.alert-danger,
.alert-error {
  background-color: #f2dede;
  border-color: #eed3d7;
  color: #b94a48;
}
.alert-info {
  background-color: #d9edf7;
  border-color: #bce8f1;
  color: #3a87ad;
}
.alert-block {
  padding-top: 14px;
  padding-bottom: 14px;
}
.alert-block > p,
.alert-block > ul {
  margin-bottom: 0;
}
.alert-block p + p {
  margin-top: 5px;
}
@-webkit-keyframes progress-bar-stripes {
  from {
    background-position: 40px 0;
  }
  to {
    background-position: 0 0;
  }
}
@-moz-keyframes progress-bar-stripes {
  from {
    background-position: 40px 0;
  }
  to {
    background-position: 0 0;
  }
}
@-ms-keyframes progress-bar-stripes {
  from {
    background-position: 40px 0;
  }
  to {
    background-position: 0 0;
  }
}
@-o-keyframes progress-bar-stripes {
  from {
    background-position: 0 0;
  }
  to {
    background-position: 40px 0;
  }
}
@keyframes progress-bar-stripes {
  from {
    background-position: 40px 0;
  }
  to {
    background-position: 0 0;
  }
}
.progress {
  overflow: hidden;
  height: 20px;
  margin-bottom: 20px;
  background-color: #f7f7f7;
  background-image: -moz-linear-gradient(top, #f5f5f5, #f9f9f9);
  background-image: -webkit-gradient(linear, 0 0, 0 100%, from(#f5f5f5), to(#f9f9f9));
  background-image: -webkit-linear-gradient(top, #f5f5f5, #f9f9f9);
  background-image: -o-linear-gradient(top, #f5f5f5, #f9f9f9);
  background-image: linear-gradient(to bottom, #f5f5f5, #f9f9f9);
  background-repeat: repeat-x;
  filter: progid:DXImageTransform.Microsoft.gradient(startColorstr='#fff5f5f5', endColorstr='#fff9f9f9', GradientType=0);
  -webkit-box-shadow: inset 0 1px 2px rgba(0, 0, 0, 0.1);
  -moz-box-shadow: inset 0 1px 2px rgba(0, 0, 0, 0.1);
  box-shadow: inset 0 1px 2px rgba(0, 0, 0, 0.1);
  -webkit-border-radius: 4px;
  -moz-border-radius: 4px;
  border-radius: 4px;
}
.progress .bar {
  width: 0%;
  height: 100%;
  color: #ffffff;
  float: left;
  font-size: 12px;
  text-align: center;
  text-shadow: 0 -1px 0 rgba(0, 0, 0, 0.25);
  background-color: #0e90d2;
  background-image: -moz-linear-gradient(top, #149bdf, #0480be);
  background-image: -webkit-gradient(linear, 0 0, 0 100%, from(#149bdf), to(#0480be));
  background-image: -webkit-linear-gradient(top, #149bdf, #0480be);
  background-image: -o-linear-gradient(top, #149bdf, #0480be);
  background-image: linear-gradient(to bottom, #149bdf, #0480be);
  background-repeat: repeat-x;
  filter: progid:DXImageTransform.Microsoft.gradient(startColorstr='#ff149bdf', endColorstr='#ff0480be', GradientType=0);
  -webkit-box-shadow: inset 0 -1px 0 rgba(0, 0, 0, 0.15);
  -moz-box-shadow: inset 0 -1px 0 rgba(0, 0, 0, 0.15);
  box-shadow: inset 0 -1px 0 rgba(0, 0, 0, 0.15);
  -webkit-box-sizing: border-box;
  -moz-box-sizing: border-box;
  box-sizing: border-box;
  -webkit-transition: width 0.6s ease;
  -moz-transition: width 0.6s ease;
  -o-transition: width 0.6s ease;
  transition: width 0.6s ease;
}
.progress .bar + .bar {
  -webkit-box-shadow: inset 1px 0 0 rgba(0,0,0,.15), inset 0 -1px 0 rgba(0,0,0,.15);
  -moz-box-shadow: inset 1px 0 0 rgba(0,0,0,.15), inset 0 -1px 0 rgba(0,0,0,.15);
  box-shadow: inset 1px 0 0 rgba(0,0,0,.15), inset 0 -1px 0 rgba(0,0,0,.15);
}
.progress-striped .bar {
  background-color: #149bdf;
  background-image: -webkit-gradient(linear, 0 100%, 100% 0, color-stop(0.25, rgba(255, 255, 255, 0.15)), color-stop(0.25, transparent), color-stop(0.5, transparent), color-stop(0.5, rgba(255, 255, 255, 0.15)), color-stop(0.75, rgba(255, 255, 255, 0.15)), color-stop(0.75, transparent), to(transparent));
  background-image: -webkit-linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
  background-image: -moz-linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
  background-image: -o-linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
  background-image: linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
  -webkit-background-size: 40px 40px;
  -moz-background-size: 40px 40px;
  -o-background-size: 40px 40px;
  background-size: 40px 40px;
}
.progress.active .bar {
  -webkit-animation: progress-bar-stripes 2s linear infinite;
  -moz-animation: progress-bar-stripes 2s linear infinite;
  -ms-animation: progress-bar-stripes 2s linear infinite;
  -o-animation: progress-bar-stripes 2s linear infinite;
  animation: progress-bar-stripes 2s linear infinite;
}
.progress-danger .bar,
.progress .bar-danger {
  background-color: #dd514c;
  background-image: -moz-linear-gradient(top, #ee5f5b, #c43c35);
  background-image: -webkit-gradient(linear, 0 0, 0 100%, from(#ee5f5b), to(#c43c35));
  background-image: -webkit-linear-gradient(top, #ee5f5b, #c43c35);
  background-image: -o-linear-gradient(top, #ee5f5b, #c43c35);
  background-image: linear-gradient(to bottom, #ee5f5b, #c43c35);
  background-repeat: repeat-x;
  filter: progid:DXImageTransform.Microsoft.gradient(startColorstr='#ffee5f5b', endColorstr='#ffc43c35', GradientType=0);
}
.progress-danger.progress-striped .bar,
.progress-striped .bar-danger {
  background-color: #ee5f5b;
  background-image: -webkit-gradient(linear, 0 100%, 100% 0, color-stop(0.25, rgba(255, 255, 255, 0.15)), color-stop(0.25, transparent), color-stop(0.5, transparent), color-stop(0.5, rgba(255, 255, 255, 0.15)), color-stop(0.75, rgba(255, 255, 255, 0.15)), color-stop(0.75, transparent), to(transparent));
  background-image: -webkit-linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
  background-image: -moz-linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
  background-image: -o-linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
  background-image: linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
}
.progress-success .bar,
.progress .bar-success {
  background-color: #5eb95e;
  background-image: -moz-linear-gradient(top, #62c462, #57a957);
  background-image: -webkit-gradient(linear, 0 0, 0 100%, from(#62c462), to(#57a957));
  background-image: -webkit-linear-gradient(top, #62c462, #57a957);
  background-image: -o-linear-gradient(top, #62c462, #57a957);
  background-image: linear-gradient(to bottom, #62c462, #57a957);
  background-repeat: repeat-x;
  filter: progid:DXImageTransform.Microsoft.gradient(startColorstr='#ff62c462', endColorstr='#ff57a957', GradientType=0);
}
.progress-success.progress-striped .bar,
.progress-striped .bar-success {
  background-color: #62c462;
  background-image: -webkit-gradient(linear, 0 100%, 100% 0, color-stop(0.25, rgba(255, 255, 255, 0.15)), color-stop(0.25, transparent), color-stop(0.5, transparent), color-stop(0.5, rgba(255, 255, 255, 0.15)), color-stop(0.75, rgba(255, 255, 255, 0.15)), color-stop(0.75, transparent), to(transparent));
  background-image: -webkit-linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
  background-image: -moz-linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
  background-image: -o-linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
  background-image: linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
}
.progress-info .bar,
.progress .bar-info {
  background-color: #4bb1cf;
  background-image: -moz-linear-gradient(top, #5bc0de, #339bb9);
  background-image: -webkit-gradient(linear, 0 0, 0 100%, from(#5bc0de), to(#339bb9));
  background-image: -webkit-linear-gradient(top, #5bc0de, #339bb9);
  background-image: -o-linear-gradient(top, #5bc0de, #339bb9);
  background-image: linear-gradient(to bottom, #5bc0de, #339bb9);
  background-repeat: repeat-x;
  filter: progid:DXImageTransform.Microsoft.gradient(startColorstr='#ff5bc0de', endColorstr='#ff339bb9', GradientType=0);
}
.progress-info.progress-striped .bar,
.progress-striped .bar-info {
  background-color: #5bc0de;
  background-image: -webkit-gradient(linear, 0 100%, 100% 0, color-stop(0.25, rgba(255, 255, 255, 0.15)), color-stop(0.25, transparent), color-stop(0.5, transparent), color-stop(0.5, rgba(255, 255, 255, 0.15)), color-stop(0.75, rgba(255, 255, 255, 0.15)), color-stop(0.75, transparent), to(transparent));
  background-image: -webkit-linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
  background-image: -moz-linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
  background-image: -o-linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
  background-image: linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
}
.progress-warning .bar,
.progress .bar-warning {
  background-color: #faa732;
  background-image: -moz-linear-gradient(top, #fbb450, #f89406);
  background-image: -webkit-gradient(linear, 0 0, 0 100%, from(#fbb450), to(#f89406));
  background-image: -webkit-linear-gradient(top, #fbb450, #f89406);
  background-image: -o-linear-gradient(top, #fbb450, #f89406);
  background-image: linear-gradient(to bottom, #fbb450, #f89406);
  background-repeat: repeat-x;
  filter: progid:DXImageTransform.Microsoft.gradient(startColorstr='#fffbb450', endColorstr='#fff89406', GradientType=0);
}
.progress-warning.progress-striped .bar,
.progress-striped .bar-warning {
  background-color: #fbb450;
  background-image: -webkit-gradient(linear, 0 100%, 100% 0, color-stop(0.25, rgba(255, 255, 255, 0.15)), color-stop(0.25, transparent), color-stop(0.5, transparent), color-stop(0.5, rgba(255, 255, 255, 0.15)), color-stop(0.75, rgba(255, 255, 255, 0.15)), color-stop(0.75, transparent), to(transparent));
  background-image: -webkit-linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
  background-image: -moz-linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
  background-image: -o-linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
  background-image: linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
}
.hero-unit {
  padding: 60px;
  margin-bottom: 30px;
  font-size: 18px;
  font-weight: 200;
  line-height: 30px;
  color: inherit;
  background-color: #eeeeee;
  -webkit-border-radius: 6px;
  -moz-border-radius: 6px;
  border-radius: 6px;
}
.hero-unit h1 {
  margin-bottom: 0;
  font-size: 60px;
  line-height: 1;
  color: inherit;
  letter-spacing: -1px;
}
.hero-unit li {
  line-height: 30px;
}
.media,
.media-body {
  overflow: hidden;
  *overflow: visible;
  zoom: 1;
}
.media,
.media .media {
  margin-top: 15px;
}
.media:first-child {
  margin-top: 0;
}
.media-object {
  display: block;
}
.media-heading {
  margin: 0 0 5px;
}
.media .pull-left {
  margin-right: 10px;
}
.media .pull-right {
  margin-left: 10px;
}
.media-list {
  margin-left: 0;
  list-style: none;
}
.tooltip {
  position: absolute;
  z-index: 1030;
  display: block;
  visibility: visible;
  padding: 5px;
  font-size: 11px;
  opacity: 0;
  filter: alpha(opacity=0);
}
.tooltip.in {
  opacity: 0.8;
  filter: alpha(opacity=80);
}
.tooltip.top {
  margin-top: -3px;
}
.tooltip.right {
  margin-left: 3px;
}
.tooltip.bottom {
  margin-top: 3px;
}
.tooltip.left {
  margin-left: -3px;
}
.tooltip-inner {
  max-width: 200px;
  padding: 3px 8px;
  color: #ffffff;
  text-align: center;
  text-decoration: none;
  background-color: #000000;
  -webkit-border-radius: 4px;
  -moz-border-radius: 4px;
  border-radius: 4px;
}
.tooltip-arrow {
  position: absolute;
  width: 0;
  height: 0;
  border-color: transparent;
  border-style: solid;
}
.tooltip.top .tooltip-arrow {
  bottom: 0;
  left: 50%;
  margin-left: -5px;
  border-width: 5px 5px 0;
  border-top-color: #000000;
}
.tooltip.right .tooltip-arrow {
  top: 50%;
  left: 0;
  margin-top: -5px;
  border-width: 5px 5px 5px 0;
  border-right-color: #000000;
}
.tooltip.left .tooltip-arrow {
  top: 50%;
  right: 0;
  margin-top: -5px;
  border-width: 5px 0 5px 5px;
  border-left-color: #000000;
}
.tooltip.bottom .tooltip-arrow {
  top: 0;
  left: 50%;
  margin-left: -5px;
  border-width: 0 5px 5px;
  border-bottom-color: #000000;
}
.popover {
  position: absolute;
  top: 0;
  left: 0;
  z-index: 1010;
  display: none;
  width: 236px;
  padding: 1px;
  background-color: #ffffff;
  -webkit-background-clip: padding-box;
  -moz-background-clip: padding;
  background-clip: padding-box;
  border: 1px solid #ccc;
  border: 1px solid rgba(0, 0, 0, 0.2);
  -webkit-border-radius: 6px;
  -moz-border-radius: 6px;
  border-radius: 6px;
  -webkit-box-shadow: 0 5px 10px rgba(0, 0, 0, 0.2);
  -moz-box-shadow: 0 5px 10px rgba(0, 0, 0, 0.2);
  box-shadow: 0 5px 10px rgba(0, 0, 0, 0.2);
}
.popover.top {
  margin-top: -10px;
}
.popover.right {
  margin-left: 10px;
}
.popover.bottom {
  margin-top: 10px;
}
.popover.left {
  margin-left: -10px;
}
.popover-title {
  margin: 0;
  padding: 8px 14px;
  font-size: 14px;
  font-weight: normal;
  line-height: 18px;
  background-color: #f7f7f7;
  border-bottom: 1px solid #ebebeb;
  -webkit-border-radius: 5px 5px 0 0;
  -moz-border-radius: 5px 5px 0 0;
  border-radius: 5px 5px 0 0;
}
.popover-content {
  padding: 9px 14px;
}
.popover-content p,
.popover-content ul,
.popover-content ol {
  margin-bottom: 0;
}
.popover .arrow,
.popover .arrow:after {
  position: absolute;
  display: inline-block;
  width: 0;
  height: 0;
  border-color: transparent;
  border-style: solid;
}
.popover .arrow:after {
  content: "";
  z-index: -1;
}
.popover.top .arrow {
  bottom: -10px;
  left: 50%;
  margin-left: -10px;
  border-width: 10px 10px 0;
  border-top-color: #ffffff;
}
.popover.top .arrow:after {
  border-width: 11px 11px 0;
  border-top-color: rgba(0, 0, 0, 0.25);
  bottom: -1px;
  left: -11px;
}
.popover.right .arrow {
  top: 50%;
  left: -10px;
  margin-top: -10px;
  border-width: 10px 10px 10px 0;
  border-right-color: #ffffff;
}
.popover.right .arrow:after {
  border-width: 11px 11px 11px 0;
  border-right-color: rgba(0, 0, 0, 0.25);
  bottom: -11px;
  left: -1px;
}
.popover.bottom .arrow {
  top: -10px;
  left: 50%;
  margin-left: -10px;
  border-width: 0 10px 10px;
  border-bottom-color: #ffffff;
}
.popover.bottom .arrow:after {
  border-width: 0 11px 11px;
  border-bottom-color: rgba(0, 0, 0, 0.25);
  top: -1px;
  left: -11px;
}
.popover.left .arrow {
  top: 50%;
  right: -10px;
  margin-top: -10px;
  border-width: 10px 0 10px 10px;
  border-left-color: #ffffff;
}
.popover.left .arrow:after {
  border-width: 11px 0 11px 11px;
  border-left-color: rgba(0, 0, 0, 0.25);
  bottom: -11px;
  right: -1px;
}
.modal-backdrop {
  position: fixed;
  top: 0;
  right: 0;
  bottom: 0;
  left: 0;
  z-index: 1040;
  background-color: #000000;
}
.modal-backdrop.fade {
  opacity: 0;
}
.modal-backdrop,
.modal-backdrop.fade.in {
  opacity: 0.8;
  filter: alpha(opacity=80);
}
.modal {
  position: fixed;
  top: 50%;
  left: 50%;
  z-index: 1050;
  width: 560px;
  margin: -250px 0 0 -280px;
  background-color: #ffffff;
  border: 1px solid #999;
  border: 1px solid rgba(0, 0, 0, 0.3);
  *border: 1px solid #999;
  /* IE6-7 */

  -webkit-border-radius: 6px;
  -moz-border-radius: 6px;
  border-radius: 6px;
  -webkit-box-shadow: 0 3px 7px rgba(0, 0, 0, 0.3);
  -moz-box-shadow: 0 3px 7px rgba(0, 0, 0, 0.3);
  box-shadow: 0 3px 7px rgba(0, 0, 0, 0.3);
  -webkit-background-clip: padding-box;
  -moz-background-clip: padding-box;
  background-clip: padding-box;
  outline: none;
}
.modal.fade {
  -webkit-transition: opacity .3s linear, top .3s ease-out;
  -moz-transition: opacity .3s linear, top .3s ease-out;
  -o-transition: opacity .3s linear, top .3s ease-out;
  transition: opacity .3s linear, top .3s ease-out;
  top: -25%;
}
.modal.fade.in {
  top: 50%;
}
.modal-header {
  padding: 9px 15px;
  border-bottom: 1px solid #eee;
}
.modal-header .close {
  margin-top: 2px;
}
.modal-header h3 {
  margin: 0;
  line-height: 30px;
}
.modal-body {
  overflow-y: auto;
  max-height: 400px;
  padding: 15px;
}
.modal-form {
  margin-bottom: 0;
}
.modal-footer {
  padding: 14px 15px 15px;
  margin-bottom: 0;
  text-align: right;
  background-color: #f5f5f5;
  border-top: 1px solid #ddd;
  -webkit-border-radius: 0 0 6px 6px;
  -moz-border-radius: 0 0 6px 6px;
  border-radius: 0 0 6px 6px;
  -webkit-box-shadow: inset 0 1px 0 #ffffff;
  -moz-box-shadow: inset 0 1px 0 #ffffff;
  box-shadow: inset 0 1px 0 #ffffff;
  *zoom: 1;
}
.modal-footer:before,
.modal-footer:after {
  display: table;
  content: "";
  line-height: 0;
}
.modal-footer:after {
  clear: both;
}
.modal-footer .btn + .btn {
  margin-left: 5px;
  margin-bottom: 0;
}
.modal-footer .btn-group .btn + .btn {
  margin-left: -1px;
}
.modal-footer .btn-block + .btn-block {
  margin-left: 0;
}
.dropup,
.dropdown {
  position: relative;
}
.dropdown-toggle {
  *margin-bottom: -3px;
}
.dropdown-toggle:active,
.open .dropdown-toggle {
  outline: 0;
}
.caret {
  display: inline-block;
  width: 0;
  height: 0;
  vertical-align: top;
  border-top: 4px solid #000000;
  border-right: 4px solid transparent;
  border-left: 4px solid transparent;
  content: "";
}
.dropdown .caret {
  margin-top: 8px;
  margin-left: 2px;
}
.dropdown-menu {
  position: absolute;
  top: 100%;
  left: 0;
  z-index: 1000;
  display: none;
  float: left;
  min-width: 160px;
  padding: 5px 0;
  margin: 2px 0 0;
  list-style: none;
  background-color: #ffffff;
  border: 1px solid #ccc;
  border: 1px solid rgba(0, 0, 0, 0.2);
  *border-right-width: 2px;
  *border-bottom-width: 2px;
  -webkit-border-radius: 6px;
  -moz-border-radius: 6px;
  border-radius: 6px;
  -webkit-box-shadow: 0 5px 10px rgba(0, 0, 0, 0.2);
  -moz-box-shadow: 0 5px 10px rgba(0, 0, 0, 0.2);
  box-shadow: 0 5px 10px rgba(0, 0, 0, 0.2);
  -webkit-background-clip: padding-box;
  -moz-background-clip: padding;
  background-clip: padding-box;
}
.dropdown-menu.pull-right {
  right: 0;
  left: auto;
}
.dropdown-menu .divider {
  *width: 100%;
  height: 1px;
  margin: 9px 1px;
  *margin: -5px 0 5px;
  overflow: hidden;
  background-color: #e5e5e5;
  border-bottom: 1px solid #ffffff;
}
.dropdown-menu li > a {
  display: block;
  padding: 3px 20px;
  clear: both;
  font-weight: normal;
  line-height: 20px;
  color: #333333;
  white-space: nowrap;
}
.dropdown-menu li > a:hover,
.dropdown-menu li > a:focus,
.dropdown-submenu:hover > a {
  text-decoration: none;
  color: #ffffff;
  background-color: #0081c2;
  background-image: -moz-linear-gradient(top, #0088cc, #0077b3);
  background-image: -webkit-gradient(linear, 0 0, 0 100%, from(#0088cc), to(#0077b3));
  background-image: -webkit-linear-gradient(top, #0088cc, #0077b3);
  background-image: -o-linear-gradient(top, #0088cc, #0077b3);
  background-image: linear-gradient(to bottom, #0088cc, #0077b3);
  background-repeat: repeat-x;
  filter: progid:DXImageTransform.Microsoft.gradient(startColorstr='#ff0088cc', endColorstr='#ff0077b3', GradientType=0);
}
.dropdown-menu .active > a,
.dropdown-menu .active > a:hover {
  color: #333333;
  text-decoration: none;
  outline: 0;
  background-color: #0081c2;
  background-image: -moz-linear-gradient(top, #0088cc, #0077b3);
  background-image: -webkit-gradient(linear, 0 0, 0 100%, from(#0088cc), to(#0077b3));
  background-image: -webkit-linear-gradient(top, #0088cc, #0077b3);
  background-image: -o-linear-gradient(top, #0088cc, #0077b3);
  background-image: linear-gradient(to bottom, #0088cc, #0077b3);
  background-repeat: repeat-x;
  filter: progid:DXImageTransform.Microsoft.gradient(startColorstr='#ff0088cc', endColorstr='#ff0077b3', GradientType=0);
}
.dropdown-menu .disabled > a,
.dropdown-menu .disabled > a:hover {
  color: #999999;
}
.dropdown-menu .disabled > a:hover {
  text-decoration: none;
  background-color: transparent;
  background-image: none;
  cursor: default;
}
.open {
  *z-index: 1000;
}
.open  > .dropdown-menu {
  display: block;
}
.pull-right > .dropdown-menu {
  right: 0;
  left: auto;
}
.dropup .caret,
.navbar-fixed-bottom .dropdown .caret {
  border-top: 0;
  border-bottom: 4px solid #000000;
  content: "";
}
.dropup .dropdown-menu,
.navbar-fixed-bottom .dropdown .dropdown-menu {
  top: auto;
  bottom: 100%;
  margin-bottom: 1px;
}
.dropdown-submenu {
  position: relative;
}
.dropdown-submenu > .dropdown-menu {
  top: 0;
  left: 100%;
  margin-top: -6px;
  margin-left: -1px;
  -webkit-border-radius: 0 6px 6px 6px;
  -moz-border-radius: 0 6px 6px 6px;
  border-radius: 0 6px 6px 6px;
}
.dropdown-submenu:hover > .dropdown-menu {
  display: block;
}
.dropup .dropdown-submenu > .dropdown-menu {
  top: auto;
  bottom: 0;
  margin-top: 0;
  margin-bottom: -2px;
  -webkit-border-radius: 5px 5px 5px 0;
  -moz-border-radius: 5px 5px 5px 0;
  border-radius: 5px 5px 5px 0;
}
.dropdown-submenu > a:after {
  display: block;
  content: " ";
  float: right;
  width: 0;
  height: 0;
  border-color: transparent;
  border-style: solid;
  border-width: 5px 0 5px 5px;
  border-left-color: #cccccc;
  margin-top: 5px;
  margin-right: -10px;
}
.dropdown-submenu:hover > a:after {
  border-left-color: #ffffff;
}
.dropdown-submenu.pull-left {
  float: none;
}
.dropdown-submenu.pull-left > .dropdown-menu {
  left: -100%;
  margin-left: 10px;
  -webkit-border-radius: 6px 0 6px 6px;
  -moz-border-radius: 6px 0 6px 6px;
  border-radius: 6px 0 6px 6px;
}
.dropdown .dropdown-menu .nav-header {
  padding-left: 20px;
  padding-right: 20px;
}
.typeahead {
  margin-top: 2px;
  -webkit-border-radius: 4px;
  -moz-border-radius: 4px;
  border-radius: 4px;
}
.accordion {
  margin-bottom: 20px;
}
.accordion-group {
  margin-bottom: 2px;
  border: 1px solid #e5e5e5;
  -webkit-border-radius: 4px;
  -moz-border-radius: 4px;
  border-radius: 4px;
}
.accordion-heading {
  border-bottom: 0;
}
.accordion-heading .accordion-toggle {
  display: block;
  padding: 8px 15px;
}
.accordion-toggle {
  cursor: pointer;
}
.accordion-inner {
  padding: 9px 15px;
  border-top: 1px solid #e5e5e5;
}
.carousel {
  position: relative;
  margin-bottom: 20px;
  line-height: 1;
}
.carousel-inner {
  overflow: hidden;
  width: 100%;
  position: relative;
}
.carousel .item {
  display: none;
  position: relative;
  -webkit-transition: 0.6s ease-in-out left;
  -moz-transition: 0.6s ease-in-out left;
  -o-transition: 0.6s ease-in-out left;
  transition: 0.6s ease-in-out left;
}
.carousel .item > img {
  display: block;
  line-height: 1;
}
.carousel .active,
.carousel .next,
.carousel .prev {
  display: block;
}
.carousel .active {
  left: 0;
}
.carousel .next,
.carousel .prev {
  position: absolute;
  top: 0;
  width: 100%;
}
.carousel .next {
  left: 100%;
}
.carousel .prev {
  left: -100%;
}
.carousel .next.left,
.carousel .prev.right {
  left: 0;
}
.carousel .active.left {
  left: -100%;
}
.carousel .active.right {
  left: 100%;
}
.carousel-control {
  position: absolute;
  top: 40%;
  left: 15px;
  width: 40px;
  height: 40px;
  margin-top: -20px;
  font-size: 60px;
  font-weight: 100;
  line-height: 30px;
  color: #ffffff;
  text-align: center;
  background: #222222;
  border: 3px solid #ffffff;
  -webkit-border-radius: 23px;
  -moz-border-radius: 23px;
  border-radius: 23px;
  opacity: 0.5;
  filter: alpha(opacity=50);
}
.carousel-control.right {
  left: auto;
  right: 15px;
}
.carousel-control:hover {
  color: #ffffff;
  text-decoration: none;
  opacity: 0.9;
  filter: alpha(opacity=90);
}
.carousel-caption {
  position: absolute;
  left: 0;
  right: 0;
  bottom: 0;
  padding: 15px;
  background: #333333;
  background: rgba(0, 0, 0, 0.75);
}
.carousel-caption h4,
.carousel-caption p {
  color: #ffffff;
  line-height: 20px;
}
.carousel-caption h4 {
  margin: 0 0 5px;
}
.carousel-caption p {
  margin-bottom: 0;
}
.media,
.media-body {
  overflow: hidden;
  *overflow: visible;
  zoom: 1;
}
.media,
.media .media {
  margin-top: 15px;
}
.media:first-child {
  margin-top: 0;
}
.media-object {
  display: block;
}
.media-heading {
  margin: 0 0 5px;
}
.media .pull-left {
  margin-right: 10px;
}
.media .pull-right {
  margin-left: 10px;
}
.media-list {
  margin-left: 0;
  list-style: none;
}
.well {
  min-height: 20px;
  padding: 19px;
  margin-bottom: 20px;
  background-color: #f5f5f5;
  border: 1px solid #e3e3e3;
  -webkit-border-radius: 4px;
  -moz-border-radius: 4px;
  border-radius: 4px;
  -webkit-box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.05);
  -moz-box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.05);
  box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.05);
}
.well blockquote {
  border-color: #ddd;
  border-color: rgba(0, 0, 0, 0.15);
}
.well-large {
  padding: 24px;
  -webkit-border-radius: 6px;
  -moz-border-radius: 6px;
  border-radius: 6px;
}
.well-small {
  padding: 9px;
  -webkit-border-radius: 3px;
  -moz-border-radius: 3px;
  border-radius: 3px;
}
.close {
  float: right;
  font-size: 20px;
  font-weight: bold;
  line-height: 20px;
  color: #000000;
  text-shadow: 0 1px 0 #ffffff;
  opacity: 0.2;
  filter: alpha(opacity=20);
}
.close:hover {
  color: #000000;
  text-decoration: none;
  cursor: pointer;
  opacity: 0.4;
  filter: alpha(opacity=40);
}
button.close {
  padding: 0;
  cursor: pointer;
  background: transparent;
  border: 0;
  -webkit-appearance: none;
}
.pull-right {
  float: right;
}
.pull-left {
  float: left;
}
.hide {
  display: none;
}
.show {
  display: block;
}
.invisible {
  visibility: hidden;
}
.affix {
  position: fixed;
}
.fade {
  opacity: 0;
  -webkit-transition: opacity 0.15s linear;
  -moz-transition: opacity 0.15s linear;
  -o-transition: opacity 0.15s linear;
  transition: opacity 0.15s linear;
}
.fade.in {
  opacity: 1;
}
.collapse {
  position: relative;
  height: 0;
  overflow: hidden;
  -webkit-transition: height 0.35s ease;
  -moz-transition: height 0.35s ease;
  -o-transition: height 0.35s ease;
  transition: height 0.35s ease;
}
.collapse.in {
  height: auto;
}
.hidden {
  display: none;
  visibility: hidden;
}
.visible-phone {
  display: none !important;
}
.visible-tablet {
  display: none !important;
}
.hidden-desktop {
  display: none !important;
}
.visible-desktop {
  display: inherit !important;
}
@media (min-width: 768px) and (max-width: 979px) {
  .hidden-desktop {
    display: inherit !important;
  }
  .visible-desktop {
    display: none !important ;
  }
  .visible-tablet {
    display: inherit !important;
  }
  .hidden-tablet {
    display: none !important;
  }
}
@media (max-width: 767px) {
  .hidden-desktop {
    display: inherit !important;
  }
  .visible-desktop {
    display: none !important;
  }
  .visible-phone {
    display: inherit !important;
  }
  .hidden-phone {
    display: none !important;
  }
}
@media (max-width: 767px) {
  body {
    padding-left: 20px;
    padding-right: 20px;
  }
  .navbar-fixed-top,
  .navbar-fixed-bottom,
  .navbar-static-top {
    margin-left: -20px;
    margin-right: -20px;
  }
  .container-fluid {
    padding: 0;
  }
  .dl-horizontal dt {
    float: none;
    clear: none;
    width: auto;
    text-align: left;
  }
  .dl-horizontal dd {
    margin-left: 0;
  }
  .container {
    width: auto;
  }
  .row-fluid {
    width: 100%;
  }
  .row,
  .thumbnails {
    margin-left: 0;
  }
  .thumbnails > li {
    float: none;
    margin-left: 0;
  }
  [class*="span"],
  .uneditable-input[class*="span"],
  .row-fluid [class*="span"] {
    float: none;
    display: block;
    width: 100%;
    margin-left: 0;
    -webkit-box-sizing: border-box;
    -moz-box-sizing: border-box;
    box-sizing: border-box;
  }
  .span12,
  .row-fluid .span12 {
    width: 100%;
    -webkit-box-sizing: border-box;
    -moz-box-sizing: border-box;
    box-sizing: border-box;
  }
  .row-fluid [class*="offset"]:first-child {
    margin-left: 0;
  }
  .input-large,
  .input-xlarge,
  .input-xxlarge,
  input[class*="span"],
  select[class*="span"],
  textarea[class*="span"],
  .uneditable-input {
    display: block;
    width: 100%;
    min-height: 30px;
    -webkit-box-sizing: border-box;
    -moz-box-sizing: border-box;
    box-sizing: border-box;
  }
  .input-prepend input,
  .input-append input,
  .input-prepend input[class*="span"],
  .input-append input[class*="span"] {
    display: inline-block;
    width: auto;
  }
  .controls-row [class*="span"] + [class*="span"] {
    margin-left: 0;
  }
  .modal {
    position: fixed;
    top: 20px;
    left: 20px;
    right: 20px;
    width: auto;
    margin: 0;
  }
  .modal.fade {
    top: -100px;
  }
  .modal.fade.in {
    top: 20px;
  }
}
@media (max-width: 480px) {
  .nav-collapse {
    -webkit-transform: translate3d(0, 0, 0);
  }
  .page-header h1 small {
    display: block;
    line-height: 20px;
  }
  input[type="checkbox"],
  input[type="radio"] {
    border: 1px solid #ccc;
  }
  .form-horizontal .control-label {
    float: none;
    width: auto;
    padding-top: 0;
    text-align: left;
  }
  .form-horizontal .controls {
    margin-left: 0;
  }
  .form-horizontal .control-list {
    padding-top: 0;
  }
  .form-horizontal .form-actions {
    padding-left: 10px;
    padding-right: 10px;
  }
  .media .pull-left,
  .media .pull-right {
    float: none;
    display: block;
    margin-bottom: 10px;
  }
  .media-object {
    margin-right: 0;
    margin-left: 0;
  }
  .modal {
    top: 10px;
    left: 10px;
    right: 10px;
  }
  .modal-header .close {
    padding: 10px;
    margin: -10px;
  }
  .carousel-caption {
    position: static;
  }
}
@media (min-width: 768px) and (max-width: 979px) {
  .row {
    margin-left: -20px;
    *zoom: 1;
  }
  .row:before,
  .row:after {
    display: table;
    content: "";
    line-height: 0;
  }
  .row:after {
    clear: both;
  }
  [class*="span"] {
    float: left;
    min-height: 1px;
    margin-left: 20px;
  }
  .container,
  .navbar-static-top .container,
  .navbar-fixed-top .container,
  .navbar-fixed-bottom .container {
    width: 724px;
  }
  .span12 {
    width: 724px;
  }
  .span11 {
    width: 662px;
  }
  .span10 {
    width: 600px;
  }
  .span9 {
    width: 538px;
  }
  .span8 {
    width: 476px;
  }
  .span7 {
    width: 414px;
  }
  .span6 {
    width: 352px;
  }
  .span5 {
    width: 290px;
  }
  .span4 {
    width: 228px;
  }
  .span3 {
    width: 166px;
  }
  .span2 {
    width: 104px;
  }
  .span1 {
    width: 42px;
  }
  .offset12 {
    margin-left: 764px;
  }
  .offset11 {
    margin-left: 702px;
  }
  .offset10 {
    margin-left: 640px;
  }
  .offset9 {
    margin-left: 578px;
  }
  .offset8 {
    margin-left: 516px;
  }
  .offset7 {
    margin-left: 454px;
  }
  .offset6 {
    margin-left: 392px;
  }
  .offset5 {
    margin-left: 330px;
  }
  .offset4 {
    margin-left: 268px;
  }
  .offset3 {
    margin-left: 206px;
  }
  .offset2 {
    margin-left: 144px;
  }
  .offset1 {
    margin-left: 82px;
  }
  .row-fluid {
    width: 100%;
    *zoom: 1;
  }
  .row-fluid:before,
  .row-fluid:after {
    display: table;
    content: "";
    line-height: 0;
  }
  .row-fluid:after {
    clear: both;
  }
  .row-fluid [class*="span"] {
    display: block;
    width: 100%;
    min-height: 30px;
    -webkit-box-sizing: border-box;
    -moz-box-sizing: border-box;
    box-sizing: border-box;
    float: left;
    margin-left: 2.7624309392265194%;
    *margin-left: 2.709239449864817%;
  }
  .row-fluid [class*="span"]:first-child {
    margin-left: 0;
  }
  .row-fluid .controls-row [class*="span"] + [class*="span"] {
    margin-left: 2.7624309392265194%;
  }
  .row-fluid .span12 {
    width: 100%;
    *width: 99.94680851063829%;
  }
  .row-fluid .span11 {
    width: 91.43646408839778%;
    *width: 91.38327259903608%;
  }
  .row-fluid .span10 {
    width: 82.87292817679558%;
    *width: 82.81973668743387%;
  }
  .row-fluid .span9 {
    width: 74.30939226519337%;
    *width: 74.25620077583166%;
  }
  .row-fluid .span8 {
    width: 65.74585635359117%;
    *width: 65.69266486422946%;
  }
  .row-fluid .span7 {
    width: 57.18232044198895%;
    *width: 57.12912895262725%;
  }
  .row-fluid .span6 {
    width: 48.61878453038674%;
    *width: 48.56559304102504%;
  }
  .row-fluid .span5 {
    width: 40.05524861878453%;
    *width: 40.00205712942283%;
  }
  .row-fluid .span4 {
    width: 31.491712707182323%;
    *width: 31.43852121782062%;
  }
  .row-fluid .span3 {
    width: 22.92817679558011%;
    *width: 22.87498530621841%;
  }
  .row-fluid .span2 {
    width: 14.3646408839779%;
    *width: 14.311449394616199%;
  }
  .row-fluid .span1 {
    width: 5.801104972375691%;
    *width: 5.747913483013988%;
  }
  .row-fluid .offset12 {
    margin-left: 105.52486187845304%;
    *margin-left: 105.41847889972962%;
  }
  .row-fluid .offset12:first-child {
    margin-left: 102.76243093922652%;
    *margin-left: 102.6560479605031%;
  }
  .row-fluid .offset11 {
    margin-left: 96.96132596685082%;
    *margin-left: 96.8549429881274%;
  }
  .row-fluid .offset11:first-child {
    margin-left: 94.1988950276243%;
    *margin-left: 94.09251204890089%;
  }
  .row-fluid .offset10 {
    margin-left: 88.39779005524862%;
    *margin-left: 88.2914070765252%;
  }
  .row-fluid .offset10:first-child {
    margin-left: 85.6353591160221%;
    *margin-left: 85.52897613729868%;
  }
  .row-fluid .offset9 {
    margin-left: 79.8342541436464%;
    *margin-left: 79.72787116492299%;
  }
  .row-fluid .offset9:first-child {
    margin-left: 77.07182320441989%;
    *margin-left: 76.96544022569647%;
  }
  .row-fluid .offset8 {
    margin-left: 71.2707182320442%;
    *margin-left: 71.16433525332079%;
  }
  .row-fluid .offset8:first-child {
    margin-left: 68.50828729281768%;
    *margin-left: 68.40190431409427%;
  }
  .row-fluid .offset7 {
    margin-left: 62.70718232044199%;
    *margin-left: 62.600799341718584%;
  }
  .row-fluid .offset7:first-child {
    margin-left: 59.94475138121547%;
    *margin-left: 59.838368402492065%;
  }
  .row-fluid .offset6 {
    margin-left: 54.14364640883978%;
    *margin-left: 54.037263430116376%;
  }
  .row-fluid .offset6:first-child {
    margin-left: 51.38121546961326%;
    *margin-left: 51.27483249088986%;
  }
  .row-fluid .offset5 {
    margin-left: 45.58011049723757%;
    *margin-left: 45.47372751851417%;
  }
  .row-fluid .offset5:first-child {
    margin-left: 42.81767955801105%;
    *margin-left: 42.71129657928765%;
  }
  .row-fluid .offset4 {
    margin-left: 37.01657458563536%;
    *margin-left: 36.91019160691196%;
  }
  .row-fluid .offset4:first-child {
    margin-left: 34.25414364640884%;
    *margin-left: 34.14776066768544%;
  }
  .row-fluid .offset3 {
    margin-left: 28.45303867403315%;
    *margin-left: 28.346655695309746%;
  }
  .row-fluid .offset3:first-child {
    margin-left: 25.69060773480663%;
    *margin-left: 25.584224756083227%;
  }
  .row-fluid .offset2 {
    margin-left: 19.88950276243094%;
    *margin-left: 19.783119783707537%;
  }
  .row-fluid .offset2:first-child {
    margin-left: 17.12707182320442%;
    *margin-left: 17.02068884448102%;
  }
  .row-fluid .offset1 {
    margin-left: 11.32596685082873%;
    *margin-left: 11.219583872105325%;
  }
  .row-fluid .offset1:first-child {
    margin-left: 8.56353591160221%;
    *margin-left: 8.457152932878806%;
  }
  input,
  textarea,
  .uneditable-input {
    margin-left: 0;
  }
  .controls-row [class*="span"] + [class*="span"] {
    margin-left: 20px;
  }
  input.span12, textarea.span12, .uneditable-input.span12 {
    width: 710px;
  }
  input.span11, textarea.span11, .uneditable-input.span11 {
    width: 648px;
  }
  input.span10, textarea.span10, .uneditable-input.span10 {
    width: 586px;
  }
  input.span9, textarea.span9, .uneditable-input.span9 {
    width: 524px;
  }
  input.span8, textarea.span8, .uneditable-input.span8 {
    width: 462px;
  }
  input.span7, textarea.span7, .uneditable-input.span7 {
    width: 400px;
  }
  input.span6, textarea.span6, .uneditable-input.span6 {
    width: 338px;
  }
  input.span5, textarea.span5, .uneditable-input.span5 {
    width: 276px;
  }
  input.span4, textarea.span4, .uneditable-input.span4 {
    width: 214px;
  }
  input.span3, textarea.span3, .uneditable-input.span3 {
    width: 152px;
  }
  input.span2, textarea.span2, .uneditable-input.span2 {
    width: 90px;
  }
  input.span1, textarea.span1, .uneditable-input.span1 {
    width: 28px;
  }
}
@media (min-width: 1200px) {
  .row {
    margin-left: -30px;
    *zoom: 1;
  }
  .row:before,
  .row:after {
    display: table;
    content: "";
    line-height: 0;
  }
  .row:after {
    clear: both;
  }
  [class*="span"] {
    float: left;
    min-height: 1px;
    margin-left: 30px;
  }
  .container,
  .navbar-static-top .container,
  .navbar-fixed-top .container,
  .navbar-fixed-bottom .container {
    width: 1170px;
  }
  .span12 {
    width: 1170px;
  }
  .span11 {
    width: 1070px;
  }
  .span10 {
    width: 970px;
  }
  .span9 {
    width: 870px;
  }
  .span8 {
    width: 770px;
  }
  .span7 {
    width: 670px;
  }
  .span6 {
    width: 570px;
  }
  .span5 {
    width: 470px;
  }
  .span4 {
    width: 370px;
  }
  .span3 {
    width: 270px;
  }
  .span2 {
    width: 170px;
  }
  .span1 {
    width: 70px;
  }
  .offset12 {
    margin-left: 1230px;
  }
  .offset11 {
    margin-left: 1130px;
  }
  .offset10 {
    margin-left: 1030px;
  }
  .offset9 {
    margin-left: 930px;
  }
  .offset8 {
    margin-left: 830px;
  }
  .offset7 {
    margin-left: 730px;
  }
  .offset6 {
    margin-left: 630px;
  }
  .offset5 {
    margin-left: 530px;
  }
  .offset4 {
    margin-left: 430px;
  }
  .offset3 {
    margin-left: 330px;
  }
  .offset2 {
    margin-left: 230px;
  }
  .offset1 {
    margin-left: 130px;
  }
  .row-fluid {
    width: 100%;
    *zoom: 1;
  }
  .row-fluid:before,
  .row-fluid:after {
    display: table;
    content: "";
    line-height: 0;
  }
  .row-fluid:after {
    clear: both;
  }
  .row-fluid [class*="span"] {
    display: block;
    width: 100%;
    min-height: 30px;
    -webkit-box-sizing: border-box;
    -moz-box-sizing: border-box;
    box-sizing: border-box;
    float: left;
    margin-left: 2.564102564102564%;
    *margin-left: 2.5109110747408616%;
  }
  .row-fluid [class*="span"]:first-child {
    margin-left: 0;
  }
  .row-fluid .controls-row [class*="span"] + [class*="span"] {
    margin-left: 2.564102564102564%;
  }
  .row-fluid .span12 {
    width: 100%;
    *width: 99.94680851063829%;
  }
  .row-fluid .span11 {
    width: 91.45299145299145%;
    *width: 91.39979996362975%;
  }
  .row-fluid .span10 {
    width: 82.90598290598291%;
    *width: 82.8527914166212%;
  }
  .row-fluid .span9 {
    width: 74.35897435897436%;
    *width: 74.30578286961266%;
  }
  .row-fluid .span8 {
    width: 65.81196581196582%;
    *width: 65.75877432260411%;
  }
  .row-fluid .span7 {
    width: 57.26495726495726%;
    *width: 57.21176577559556%;
  }
  .row-fluid .span6 {
    width: 48.717948717948715%;
    *width: 48.664757228587014%;
  }
  .row-fluid .span5 {
    width: 40.17094017094017%;
    *width: 40.11774868157847%;
  }
  .row-fluid .span4 {
    width: 31.623931623931625%;
    *width: 31.570740134569924%;
  }
  .row-fluid .span3 {
    width: 23.076923076923077%;
    *width: 23.023731587561375%;
  }
  .row-fluid .span2 {
    width: 14.52991452991453%;
    *width: 14.476723040552828%;
  }
  .row-fluid .span1 {
    width: 5.982905982905983%;
    *width: 5.929714493544281%;
  }
  .row-fluid .offset12 {
    margin-left: 105.12820512820512%;
    *margin-left: 105.02182214948171%;
  }
  .row-fluid .offset12:first-child {
    margin-left: 102.56410256410257%;
    *margin-left: 102.45771958537915%;
  }
  .row-fluid .offset11 {
    margin-left: 96.58119658119658%;
    *margin-left: 96.47481360247316%;
  }
  .row-fluid .offset11:first-child {
    margin-left: 94.01709401709402%;
    *margin-left: 93.91071103837061%;
  }
  .row-fluid .offset10 {
    margin-left: 88.03418803418803%;
    *margin-left: 87.92780505546462%;
  }
  .row-fluid .offset10:first-child {
    margin-left: 85.47008547008548%;
    *margin-left: 85.36370249136206%;
  }
  .row-fluid .offset9 {
    margin-left: 79.48717948717949%;
    *margin-left: 79.38079650845607%;
  }
  .row-fluid .offset9:first-child {
    margin-left: 76.92307692307693%;
    *margin-left: 76.81669394435352%;
  }
  .row-fluid .offset8 {
    margin-left: 70.94017094017094%;
    *margin-left: 70.83378796144753%;
  }
  .row-fluid .offset8:first-child {
    margin-left: 68.37606837606839%;
    *margin-left: 68.26968539734497%;
  }
  .row-fluid .offset7 {
    margin-left: 62.393162393162385%;
    *margin-left: 62.28677941443899%;
  }
  .row-fluid .offset7:first-child {
    margin-left: 59.82905982905982%;
    *margin-left: 59.72267685033642%;
  }
  .row-fluid .offset6 {
    margin-left: 53.84615384615384%;
    *margin-left: 53.739770867430444%;
  }
  .row-fluid .offset6:first-child {
    margin-left: 51.28205128205128%;
    *margin-left: 51.175668303327875%;
  }
  .row-fluid .offset5 {
    margin-left: 45.299145299145295%;
    *margin-left: 45.1927623204219%;
  }
  .row-fluid .offset5:first-child {
    margin-left: 42.73504273504273%;
    *margin-left: 42.62865975631933%;
  }
  .row-fluid .offset4 {
    margin-left: 36.75213675213675%;
    *margin-left: 36.645753773413354%;
  }
  .row-fluid .offset4:first-child {
    margin-left: 34.18803418803419%;
    *margin-left: 34.081651209310785%;
  }
  .row-fluid .offset3 {
    margin-left: 28.205128205128204%;
    *margin-left: 28.0987452264048%;
  }
  .row-fluid .offset3:first-child {
    margin-left: 25.641025641025642%;
    *margin-left: 25.53464266230224%;
  }
  .row-fluid .offset2 {
    margin-left: 19.65811965811966%;
    *margin-left: 19.551736679396257%;
  }
  .row-fluid .offset2:first-child {
    margin-left: 17.094017094017094%;
    *margin-left: 16.98763411529369%;
  }
  .row-fluid .offset1 {
    margin-left: 11.11111111111111%;
    *margin-left: 11.004728132387708%;
  }
  .row-fluid .offset1:first-child {
    margin-left: 8.547008547008547%;
    *margin-left: 8.440625568285142%;
  }
  input,
  textarea,
  .uneditable-input {
    margin-left: 0;
  }
  .controls-row [class*="span"] + [class*="span"] {
    margin-left: 30px;
  }
  input.span12, textarea.span12, .uneditable-input.span12 {
    width: 1156px;
  }
  input.span11, textarea.span11, .uneditable-input.span11 {
    width: 1056px;
  }
  input.span10, textarea.span10, .uneditable-input.span10 {
    width: 956px;
  }
  input.span9, textarea.span9, .uneditable-input.span9 {
    width: 856px;
  }
  input.span8, textarea.span8, .uneditable-input.span8 {
    width: 756px;
  }
  input.span7, textarea.span7, .uneditable-input.span7 {
    width: 656px;
  }
  input.span6, textarea.span6, .uneditable-input.span6 {
    width: 556px;
  }
  input.span5, textarea.span5, .uneditable-input.span5 {
    width: 456px;
  }
  input.span4, textarea.span4, .uneditable-input.span4 {
    width: 356px;
  }
  input.span3, textarea.span3, .uneditable-input.span3 {
    width: 256px;
  }
  input.span2, textarea.span2, .uneditable-input.span2 {
    width: 156px;
  }
  input.span1, textarea.span1, .uneditable-input.span1 {
    width: 56px;
  }
  .thumbnails {
    margin-left: -30px;
  }
  .thumbnails > li {
    margin-left: 30px;
  }
  .row-fluid .thumbnails {
    margin-left: 0;
  }
}
@media (max-width: 979px) {
  body {
    padding-top: 0;
  }
  .navbar-fixed-top,
  .navbar-fixed-bottom {
    position: static;
  }
  .navbar-fixed-top {
    margin-bottom: 20px;
  }
  .navbar-fixed-bottom {
    margin-top: 20px;
  }
  .navbar-fixed-top .navbar-inner,
  .navbar-fixed-bottom .navbar-inner {
    padding: 5px;
  }
  .navbar .container {
    width: auto;
    padding: 0;
  }
  .navbar .brand {
    padding-left: 10px;
    padding-right: 10px;
    margin: 0 0 0 -5px;
  }
  .nav-collapse {
    clear: both;
  }
  .nav-collapse .nav {
    float: none;
    margin: 0 0 10px;
  }
  .nav-collapse .nav > li {
    float: none;
  }
  .nav-collapse .nav > li > a {
    margin-bottom: 2px;
  }
  .nav-collapse .nav > .divider-vertical {
    display: none;
  }
  .nav-collapse .nav .nav-header {
    color: #777777;
    text-shadow: none;
  }
  .nav-collapse .nav > li > a,
  .nav-collapse .dropdown-menu a {
    padding: 9px 15px;
    font-weight: bold;
    color: #777777;
    -webkit-border-radius: 3px;
    -moz-border-radius: 3px;
    border-radius: 3px;
  }
  .nav-collapse .btn {
    padding: 4px 10px 4px;
    font-weight: normal;
    -webkit-border-radius: 4px;
    -moz-border-radius: 4px;
    border-radius: 4px;
  }
  .nav-collapse .dropdown-menu li + li a {
    margin-bottom: 2px;
  }
  .nav-collapse .nav > li > a:hover,
  .nav-collapse .dropdown-menu a:hover {
    background-color: #f2f2f2;
  }
  .navbar-inverse .nav-collapse .nav > li > a,
  .navbar-inverse .nav-collapse .dropdown-menu a {
    color: #999999;
  }
  .navbar-inverse .nav-collapse .nav > li > a:hover,
  .navbar-inverse .nav-collapse .dropdown-menu a:hover {
    background-color: #111111;
  }
  .nav-collapse.in .btn-group {
    margin-top: 5px;
    padding: 0;
  }
  .nav-collapse .dropdown-menu {
    position: static;
    top: auto;
    left: auto;
    float: none;
    display: none;
    max-width: none;
    margin: 0 15px;
    padding: 0;
    background-color: transparent;
    border: none;
    -webkit-border-radius: 0;
    -moz-border-radius: 0;
    border-radius: 0;
    -webkit-box-shadow: none;
    -moz-box-shadow: none;
    box-shadow: none;
  }
  .nav-collapse .open > .dropdown-menu {
    display: block;
  }
  .nav-collapse .dropdown-menu:before,
  .nav-collapse .dropdown-menu:after {
    display: none;
  }
  .nav-collapse .dropdown-menu .divider {
    display: none;
  }
  .nav-collapse .nav > li > .dropdown-menu:before,
  .nav-collapse .nav > li > .dropdown-menu:after {
    display: none;
  }
  .nav-collapse .navbar-form,
  .nav-collapse .navbar-search {
    float: none;
    padding: 10px 15px;
    margin: 10px 0;
    border-top: 1px solid #f2f2f2;
    border-bottom: 1px solid #f2f2f2;
    -webkit-box-shadow: inset 0 1px 0 rgba(255,255,255,.1), 0 1px 0 rgba(255,255,255,.1);
    -moz-box-shadow: inset 0 1px 0 rgba(255,255,255,.1), 0 1px 0 rgba(255,255,255,.1);
    box-shadow: inset 0 1px 0 rgba(255,255,255,.1), 0 1px 0 rgba(255,255,255,.1);
  }
  .navbar-inverse .nav-collapse .navbar-form,
  .navbar-inverse .nav-collapse .navbar-search {
    border-top-color: #111111;
    border-bottom-color: #111111;
  }
  .navbar .nav-collapse .nav.pull-right {
    float: none;
    margin-left: 0;
  }
  .nav-collapse,
  .nav-collapse.collapse {
    overflow: hidden;
    height: 0;
  }
  .navbar .btn-navbar {
    display: block;
  }
  .navbar-static .navbar-inner {
    padding-left: 10px;
    padding-right: 10px;
  }
}
@media (min-width: 980px) {
  .nav-collapse.collapse {
    height: auto !important;
    overflow: visible !important;
  }
}


File: /lib\bootstrap\js\bootstrap.js
/* ===================================================
 * bootstrap-transition.js v2.2.1
 * http://twitter.github.com/bootstrap/javascript.html#transitions
 * ===================================================
 * Copyright 2012 Twitter, Inc.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 * http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 * ========================================================== */


!function ($) {

  "use strict"; // jshint ;_;


  /* CSS TRANSITION SUPPORT (http://www.modernizr.com/)
   * ======================================================= */

  $(function () {

    $.support.transition = (function () {

      var transitionEnd = (function () {

        var el = document.createElement('bootstrap')
          , transEndEventNames = {
               'WebkitTransition' : 'webkitTransitionEnd'
            ,  'MozTransition'    : 'transitionend'
            ,  'OTransition'      : 'oTransitionEnd otransitionend'
            ,  'transition'       : 'transitionend'
            }
          , name

        for (name in transEndEventNames){
          if (el.style[name] !== undefined) {
            return transEndEventNames[name]
          }
        }

      }())

      return transitionEnd && {
        end: transitionEnd
      }

    })()

  })

}(window.jQuery);
/* =========================================================
 * bootstrap-modal.js v2.2.1
 * http://twitter.github.com/bootstrap/javascript.html#modals
 * =========================================================
 * Copyright 2012 Twitter, Inc.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 * http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 * ========================================================= */


!function ($) {

  "use strict"; // jshint ;_;


 /* MODAL CLASS DEFINITION
  * ====================== */

  var Modal = function (element, options) {
    this.options = options
    this.$element = $(element)
      .delegate('[data-dismiss="modal"]', 'click.dismiss.modal', $.proxy(this.hide, this))
    this.options.remote && this.$element.find('.modal-body').load(this.options.remote)
  }

  Modal.prototype = {

      constructor: Modal

    , toggle: function () {
        return this[!this.isShown ? 'show' : 'hide']()
      }

    , show: function () {
        var that = this
          , e = $.Event('show')

        this.$element.trigger(e)

        if (this.isShown || e.isDefaultPrevented()) return

        this.isShown = true

        this.escape()

        this.backdrop(function () {
          var transition = $.support.transition && that.$element.hasClass('fade')

          if (!that.$element.parent().length) {
            that.$element.appendTo(document.body) //don't move modals dom position
          }

          that.$element
            .show()

          if (transition) {
            that.$element[0].offsetWidth // force reflow
          }

          that.$element
            .addClass('in')
            .attr('aria-hidden', false)

          that.enforceFocus()

          transition ?
            that.$element.one($.support.transition.end, function () { that.$element.focus().trigger('shown') }) :
            that.$element.focus().trigger('shown')

        })
      }

    , hide: function (e) {
        e && e.preventDefault()

        var that = this

        e = $.Event('hide')

        this.$element.trigger(e)

        if (!this.isShown || e.isDefaultPrevented()) return

        this.isShown = false

        this.escape()

        $(document).off('focusin.modal')

        this.$element
          .removeClass('in')
          .attr('aria-hidden', true)

        $.support.transition && this.$element.hasClass('fade') ?
          this.hideWithTransition() :
          this.hideModal()
      }

    , enforceFocus: function () {
        var that = this
        $(document).on('focusin.modal', function (e) {
          if (that.$element[0] !== e.target && !that.$element.has(e.target).length) {
            that.$element.focus()
          }
        })
      }

    , escape: function () {
        var that = this
        if (this.isShown && this.options.keyboard) {
          this.$element.on('keyup.dismiss.modal', function ( e ) {
            e.which == 27 && that.hide()
          })
        } else if (!this.isShown) {
          this.$element.off('keyup.dismiss.modal')
        }
      }

    , hideWithTransition: function () {
        var that = this
          , timeout = setTimeout(function () {
              that.$element.off($.support.transition.end)
              that.hideModal()
            }, 500)

        this.$element.one($.support.transition.end, function () {
          clearTimeout(timeout)
          that.hideModal()
        })
      }

    , hideModal: function (that) {
        this.$element
          .hide()
          .trigger('hidden')

        this.backdrop()
      }

    , removeBackdrop: function () {
        this.$backdrop.remove()
        this.$backdrop = null
      }

    , backdrop: function (callback) {
        var that = this
          , animate = this.$element.hasClass('fade') ? 'fade' : ''

        if (this.isShown && this.options.backdrop) {
          var doAnimate = $.support.transition && animate

          this.$backdrop = $('<div class="modal-backdrop ' + animate + '" />')
            .appendTo(document.body)

          this.$backdrop.click(
            this.options.backdrop == 'static' ?
              $.proxy(this.$element[0].focus, this.$element[0])
            : $.proxy(this.hide, this)
          )

          if (doAnimate) this.$backdrop[0].offsetWidth // force reflow

          this.$backdrop.addClass('in')

          doAnimate ?
            this.$backdrop.one($.support.transition.end, callback) :
            callback()

        } else if (!this.isShown && this.$backdrop) {
          this.$backdrop.removeClass('in')

          $.support.transition && this.$element.hasClass('fade')?
            this.$backdrop.one($.support.transition.end, $.proxy(this.removeBackdrop, this)) :
            this.removeBackdrop()

        } else if (callback) {
          callback()
        }
      }
  }


 /* MODAL PLUGIN DEFINITION
  * ======================= */

  $.fn.modal = function (option) {
    return this.each(function () {
      var $this = $(this)
        , data = $this.data('modal')
        , options = $.extend({}, $.fn.modal.defaults, $this.data(), typeof option == 'object' && option)
      if (!data) $this.data('modal', (data = new Modal(this, options)))
      if (typeof option == 'string') data[option]()
      else if (options.show) data.show()
    })
  }

  $.fn.modal.defaults = {
      backdrop: true
    , keyboard: true
    , show: true
  }

  $.fn.modal.Constructor = Modal


 /* MODAL DATA-API
  * ============== */

  $(document).on('click.modal.data-api', '[data-toggle="modal"]', function (e) {
    var $this = $(this)
      , href = $this.attr('href')
      , $target = $($this.attr('data-target') || (href && href.replace(/.*(?=#[^\s]+$)/, ''))) //strip for ie7
      , option = $target.data('modal') ? 'toggle' : $.extend({ remote:!/#/.test(href) && href }, $target.data(), $this.data())

    e.preventDefault()

    $target
      .modal(option)
      .one('hide', function () {
        $this.focus()
      })
  })

}(window.jQuery);

/* ============================================================
 * bootstrap-dropdown.js v2.2.1
 * http://twitter.github.com/bootstrap/javascript.html#dropdowns
 * ============================================================
 * Copyright 2012 Twitter, Inc.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 * http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 * ============================================================ */


!function ($) {

  "use strict"; // jshint ;_;


 /* DROPDOWN CLASS DEFINITION
  * ========================= */

  var toggle = '[data-toggle=dropdown]'
    , Dropdown = function (element) {
        var $el = $(element).on('click.dropdown.data-api', this.toggle)
        $('html').on('click.dropdown.data-api', function () {
          $el.parent().removeClass('open')
        })
      }

  Dropdown.prototype = {

    constructor: Dropdown

  , toggle: function (e) {
      var $this = $(this)
        , $parent
        , isActive

      if ($this.is('.disabled, :disabled')) return

      $parent = getParent($this)

      isActive = $parent.hasClass('open')

      clearMenus()

      if (!isActive) {
        $parent.toggleClass('open')
        $this.focus()
      }

      return false
    }

  , keydown: function (e) {
      var $this
        , $items
        , $active
        , $parent
        , isActive
        , index

      if (!/(38|40|27)/.test(e.keyCode)) return

      $this = $(this)

      e.preventDefault()
      e.stopPropagation()

      if ($this.is('.disabled, :disabled')) return

      $parent = getParent($this)

      isActive = $parent.hasClass('open')

      if (!isActive || (isActive && e.keyCode == 27)) return $this.click()

      $items = $('[role=menu] li:not(.divider) a', $parent)

      if (!$items.length) return

      index = $items.index($items.filter(':focus'))

      if (e.keyCode == 38 && index > 0) index--                                        // up
      if (e.keyCode == 40 && index < $items.length - 1) index++                        // down
      if (!~index) index = 0

      $items
        .eq(index)
        .focus()
    }

  }

  function clearMenus() {
    $(toggle).each(function () {
      getParent($(this)).removeClass('open')
    })
  }

  function getParent($this) {
    var selector = $this.attr('data-target')
      , $parent

    if (!selector) {
      selector = $this.attr('href')
      selector = selector && /#/.test(selector) && selector.replace(/.*(?=#[^\s]*$)/, '') //strip for ie7
    }

    $parent = $(selector)
    $parent.length || ($parent = $this.parent())

    return $parent
  }


  /* DROPDOWN PLUGIN DEFINITION
   * ========================== */

  $.fn.dropdown = function (option) {
    return this.each(function () {
      var $this = $(this)
        , data = $this.data('dropdown')
      if (!data) $this.data('dropdown', (data = new Dropdown(this)))
      if (typeof option == 'string') data[option].call($this)
    })
  }

  $.fn.dropdown.Constructor = Dropdown


  /* APPLY TO STANDARD DROPDOWN ELEMENTS
   * =================================== */

  $(document)
    .on('click.dropdown.data-api touchstart.dropdown.data-api', clearMenus)
    .on('click.dropdown touchstart.dropdown.data-api', '.dropdown form', function (e) { e.stopPropagation() })
    .on('click.dropdown.data-api touchstart.dropdown.data-api'  , toggle, Dropdown.prototype.toggle)
    .on('keydown.dropdown.data-api touchstart.dropdown.data-api', toggle + ', [role=menu]' , Dropdown.prototype.keydown)

}(window.jQuery);
/* =============================================================
 * bootstrap-scrollspy.js v2.2.1
 * http://twitter.github.com/bootstrap/javascript.html#scrollspy
 * =============================================================
 * Copyright 2012 Twitter, Inc.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 * http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 * ============================================================== */


!function ($) {

  "use strict"; // jshint ;_;


 /* SCROLLSPY CLASS DEFINITION
  * ========================== */

  function ScrollSpy(element, options) {
    var process = $.proxy(this.process, this)
      , $element = $(element).is('body') ? $(window) : $(element)
      , href
    this.options = $.extend({}, $.fn.scrollspy.defaults, options)
    this.$scrollElement = $element.on('scroll.scroll-spy.data-api', process)
    this.selector = (this.options.target
      || ((href = $(element).attr('href')) && href.replace(/.*(?=#[^\s]+$)/, '')) //strip for ie7
      || '') + ' .nav li > a'
    this.$body = $('body')
    this.refresh()
    this.process()
  }

  ScrollSpy.prototype = {

      constructor: ScrollSpy

    , refresh: function () {
        var self = this
          , $targets

        this.offsets = $([])
        this.targets = $([])

        $targets = this.$body
          .find(this.selector)
          .map(function () {
            var $el = $(this)
              , href = $el.data('target') || $el.attr('href')
              , $href = /^#\w/.test(href) && $(href)
            return ( $href
              && $href.length
              && [[ $href.position().top, href ]] ) || null
          })
          .sort(function (a, b) { return a[0] - b[0] })
          .each(function () {
            self.offsets.push(this[0])
            self.targets.push(this[1])
          })
      }

    , process: function () {
        var scrollTop = this.$scrollElement.scrollTop() + this.options.offset
          , scrollHeight = this.$scrollElement[0].scrollHeight || this.$body[0].scrollHeight
          , maxScroll = scrollHeight - this.$scrollElement.height()
          , offsets = this.offsets
          , targets = this.targets
          , activeTarget = this.activeTarget
          , i

        if (scrollTop >= maxScroll) {
          return activeTarget != (i = targets.last()[0])
            && this.activate ( i )
        }

        for (i = offsets.length; i--;) {
          activeTarget != targets[i]
            && scrollTop >= offsets[i]
            && (!offsets[i + 1] || scrollTop <= offsets[i + 1])
            && this.activate( targets[i] )
        }
      }

    , activate: function (target) {
        var active
          , selector

        this.activeTarget = target

        $(this.selector)
          .parent('.active')
          .removeClass('active')

        selector = this.selector
          + '[data-target="' + target + '"],'
          + this.selector + '[href="' + target + '"]'

        active = $(selector)
          .parent('li')
          .addClass('active')

        if (active.parent('.dropdown-menu').length)  {
          active = active.closest('li.dropdown').addClass('active')
        }

        active.trigger('activate')
      }

  }


 /* SCROLLSPY PLUGIN DEFINITION
  * =========================== */

  $.fn.scrollspy = function (option) {
    return this.each(function () {
      var $this = $(this)
        , data = $this.data('scrollspy')
        , options = typeof option == 'object' && option
      if (!data) $this.data('scrollspy', (data = new ScrollSpy(this, options)))
      if (typeof option == 'string') data[option]()
    })
  }

  $.fn.scrollspy.Constructor = ScrollSpy

  $.fn.scrollspy.defaults = {
    offset: 10
  }


 /* SCROLLSPY DATA-API
  * ================== */

  $(window).on('load', function () {
    $('[data-spy="scroll"]').each(function () {
      var $spy = $(this)
      $spy.scrollspy($spy.data())
    })
  })

}(window.jQuery);
/* ========================================================
 * bootstrap-tab.js v2.2.1
 * http://twitter.github.com/bootstrap/javascript.html#tabs
 * ========================================================
 * Copyright 2012 Twitter, Inc.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 * http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 * ======================================================== */


!function ($) {

  "use strict"; // jshint ;_;


 /* TAB CLASS DEFINITION
  * ==================== */

  var Tab = function (element) {
    this.element = $(element)
  }

  Tab.prototype = {

    constructor: Tab

  , show: function () {
      var $this = this.element
        , $ul = $this.closest('ul:not(.dropdown-menu)')
        , selector = $this.attr('data-target')
        , previous
        , $target
        , e

      if (!selector) {
        selector = $this.attr('href')
        selector = selector && selector.replace(/.*(?=#[^\s]*$)/, '') //strip for ie7
      }

      if ( $this.parent('li').hasClass('active') ) return

      previous = $ul.find('.active:last a')[0]

      e = $.Event('show', {
        relatedTarget: previous
      })

      $this.trigger(e)

      if (e.isDefaultPrevented()) return

      $target = $(selector)

      this.activate($this.parent('li'), $ul)
      this.activate($target, $target.parent(), function () {
        $this.trigger({
          type: 'shown'
        , relatedTarget: previous
        })
      })
    }

  , activate: function ( element, container, callback) {
      var $active = container.find('> .active')
        , transition = callback
            && $.support.transition
            && $active.hasClass('fade')

      function next() {
        $active
          .removeClass('active')
          .find('> .dropdown-menu > .active')
          .removeClass('active')

        element.addClass('active')

        if (transition) {
          element[0].offsetWidth // reflow for transition
          element.addClass('in')
        } else {
          element.removeClass('fade')
        }

        if ( element.parent('.dropdown-menu') ) {
          element.closest('li.dropdown').addClass('active')
        }

        callback && callback()
      }

      transition ?
        $active.one($.support.transition.end, next) :
        next()

      $active.removeClass('in')
    }
  }


 /* TAB PLUGIN DEFINITION
  * ===================== */

  $.fn.tab = function ( option ) {
    return this.each(function () {
      var $this = $(this)
        , data = $this.data('tab')
      if (!data) $this.data('tab', (data = new Tab(this)))
      if (typeof option == 'string') data[option]()
    })
  }

  $.fn.tab.Constructor = Tab


 /* TAB DATA-API
  * ============ */

  $(document).on('click.tab.data-api', '[data-toggle="tab"], [data-toggle="pill"]', function (e) {
    e.preventDefault()
    $(this).tab('show')
  })

}(window.jQuery);
/* ===========================================================
 * bootstrap-tooltip.js v2.2.1
 * http://twitter.github.com/bootstrap/javascript.html#tooltips
 * Inspired by the original jQuery.tipsy by Jason Frame
 * ===========================================================
 * Copyright 2012 Twitter, Inc.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 * http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 * ========================================================== */


!function ($) {

  "use strict"; // jshint ;_;


 /* TOOLTIP PUBLIC CLASS DEFINITION
  * =============================== */

  var Tooltip = function (element, options) {
    this.init('tooltip', element, options)
  }

  Tooltip.prototype = {

    constructor: Tooltip

  , init: function (type, element, options) {
      var eventIn
        , eventOut

      this.type = type
      this.$element = $(element)
      this.options = this.getOptions(options)
      this.enabled = true

      if (this.options.trigger == 'click') {
        this.$element.on('click.' + this.type, this.options.selector, $.proxy(this.toggle, this))
      } else if (this.options.trigger != 'manual') {
        eventIn = this.options.trigger == 'hover' ? 'mouseenter' : 'focus'
        eventOut = this.options.trigger == 'hover' ? 'mouseleave' : 'blur'
        this.$element.on(eventIn + '.' + this.type, this.options.selector, $.proxy(this.enter, this))
        this.$element.on(eventOut + '.' + this.type, this.options.selector, $.proxy(this.leave, this))
      }

      this.options.selector ?
        (this._options = $.extend({}, this.options, { trigger: 'manual', selector: '' })) :
        this.fixTitle()
    }

  , getOptions: function (options) {
      options = $.extend({}, $.fn[this.type].defaults, options, this.$element.data())

      if (options.delay && typeof options.delay == 'number') {
        options.delay = {
          show: options.delay
        , hide: options.delay
        }
      }

      return options
    }

  , enter: function (e) {
      var self = $(e.currentTarget)[this.type](this._options).data(this.type)

      if (!self.options.delay || !self.options.delay.show) return self.show()

      clearTimeout(this.timeout)
      self.hoverState = 'in'
      this.timeout = setTimeout(function() {
        if (self.hoverState == 'in') self.show()
      }, self.options.delay.show)
    }

  , leave: function (e) {
      var self = $(e.currentTarget)[this.type](this._options).data(this.type)

      if (this.timeout) clearTimeout(this.timeout)
      if (!self.options.delay || !self.options.delay.hide) return self.hide()

      self.hoverState = 'out'
      this.timeout = setTimeout(function() {
        if (self.hoverState == 'out') self.hide()
      }, self.options.delay.hide)
    }

  , show: function () {
      var $tip
        , inside
        , pos
        , actualWidth
        , actualHeight
        , placement
        , tp

      if (this.hasContent() && this.enabled) {
        $tip = this.tip()
        this.setContent()

        if (this.options.animation) {
          $tip.addClass('fade')
        }

        placement = typeof this.options.placement == 'function' ?
          this.options.placement.call(this, $tip[0], this.$element[0]) :
          this.options.placement

        inside = /in/.test(placement)

        $tip
          .detach()
          .css({ top: 0, left: 0, display: 'block' })
          .insertAfter(this.$element)

        pos = this.getPosition(inside)

        actualWidth = $tip[0].offsetWidth
        actualHeight = $tip[0].offsetHeight

        switch (inside ? placement.split(' ')[1] : placement) {
          case 'bottom':
            tp = {top: pos.top + pos.height, left: pos.left + pos.width / 2 - actualWidth / 2}
            break
          case 'top':
            tp = {top: pos.top - actualHeight, left: pos.left + pos.width / 2 - actualWidth / 2}
            break
          case 'left':
            tp = {top: pos.top + pos.height / 2 - actualHeight / 2, left: pos.left - actualWidth}
            break
          case 'right':
            tp = {top: pos.top + pos.height / 2 - actualHeight / 2, left: pos.left + pos.width}
            break
        }

        $tip
          .offset(tp)
          .addClass(placement)
          .addClass('in')
      }
    }

  , setContent: function () {
      var $tip = this.tip()
        , title = this.getTitle()

      $tip.find('.tooltip-inner')[this.options.html ? 'html' : 'text'](title)
      $tip.removeClass('fade in top bottom left right')
    }

  , hide: function () {
      var that = this
        , $tip = this.tip()

      $tip.removeClass('in')

      function removeWithAnimation() {
        var timeout = setTimeout(function () {
          $tip.off($.support.transition.end).detach()
        }, 500)

        $tip.one($.support.transition.end, function () {
          clearTimeout(timeout)
          $tip.detach()
        })
      }

      $.support.transition && this.$tip.hasClass('fade') ?
        removeWithAnimation() :
        $tip.detach()

      return this
    }

  , fixTitle: function () {
      var $e = this.$element
      if ($e.attr('title') || typeof($e.attr('data-original-title')) != 'string') {
        $e.attr('data-original-title', $e.attr('title') || '').removeAttr('title')
      }
    }

  , hasContent: function () {
      return this.getTitle()
    }

  , getPosition: function (inside) {
      return $.extend({}, (inside ? {top: 0, left: 0} : this.$element.offset()), {
        width: this.$element[0].offsetWidth
      , height: this.$element[0].offsetHeight
      })
    }

  , getTitle: function () {
      var title
        , $e = this.$element
        , o = this.options

      title = $e.attr('data-original-title')
        || (typeof o.title == 'function' ? o.title.call($e[0]) :  o.title)

      return title
    }

  , tip: function () {
      return this.$tip = this.$tip || $(this.options.template)
    }

  , validate: function () {
      if (!this.$element[0].parentNode) {
        this.hide()
        this.$element = null
        this.options = null
      }
    }

  , enable: function () {
      this.enabled = true
    }

  , disable: function () {
      this.enabled = false
    }

  , toggleEnabled: function () {
      this.enabled = !this.enabled
    }

  , toggle: function (e) {
      var self = $(e.currentTarget)[this.type](this._options).data(this.type)
      self[self.tip().hasClass('in') ? 'hide' : 'show']()
    }

  , destroy: function () {
      this.hide().$element.off('.' + this.type).removeData(this.type)
    }

  }


 /* TOOLTIP PLUGIN DEFINITION
  * ========================= */

  $.fn.tooltip = function ( option ) {
    return this.each(function () {
      var $this = $(this)
        , data = $this.data('tooltip')
        , options = typeof option == 'object' && option
      if (!data) $this.data('tooltip', (data = new Tooltip(this, options)))
      if (typeof option == 'string') data[option]()
    })
  }

  $.fn.tooltip.Constructor = Tooltip

  $.fn.tooltip.defaults = {
    animation: true
  , placement: 'top'
  , selector: false
  , template: '<div class="tooltip"><div class="tooltip-arrow"></div><div class="tooltip-inner"></div></div>'
  , trigger: 'hover'
  , title: ''
  , delay: 0
  , html: false
  }

}(window.jQuery);
/* ===========================================================
 * bootstrap-popover.js v2.2.1
 * http://twitter.github.com/bootstrap/javascript.html#popovers
 * ===========================================================
 * Copyright 2012 Twitter, Inc.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 * http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 * =========================================================== */


!function ($) {

  "use strict"; // jshint ;_;


 /* POPOVER PUBLIC CLASS DEFINITION
  * =============================== */

  var Popover = function (element, options) {
    this.init('popover', element, options)
  }


  /* NOTE: POPOVER EXTENDS BOOTSTRAP-TOOLTIP.js
     ========================================== */

  Popover.prototype = $.extend({}, $.fn.tooltip.Constructor.prototype, {

    constructor: Popover

  , setContent: function () {
      var $tip = this.tip()
        , title = this.getTitle()
        , content = this.getContent()

      $tip.find('.popover-title')[this.options.html ? 'html' : 'text'](title)
      $tip.find('.popover-content > *')[this.options.html ? 'html' : 'text'](content)

      $tip.removeClass('fade top bottom left right in')
    }

  , hasContent: function () {
      return this.getTitle() || this.getContent()
    }

  , getContent: function () {
      var content
        , $e = this.$element
        , o = this.options

      content = $e.attr('data-content')
        || (typeof o.content == 'function' ? o.content.call($e[0]) :  o.content)

      return content
    }

  , tip: function () {
      if (!this.$tip) {
        this.$tip = $(this.options.template)
      }
      return this.$tip
    }

  , destroy: function () {
      this.hide().$element.off('.' + this.type).removeData(this.type)
    }

  })


 /* POPOVER PLUGIN DEFINITION
  * ======================= */

  $.fn.popover = function (option) {
    return this.each(function () {
      var $this = $(this)
        , data = $this.data('popover')
        , options = typeof option == 'object' && option
      if (!data) $this.data('popover', (data = new Popover(this, options)))
      if (typeof option == 'string') data[option]()
    })
  }

  $.fn.popover.Constructor = Popover

  $.fn.popover.defaults = $.extend({} , $.fn.tooltip.defaults, {
    placement: 'right'
  , trigger: 'click'
  , content: ''
  , template: '<div class="popover"><div class="arrow"></div><div class="popover-inner"><h3 class="popover-title"></h3><div class="popover-content"><p></p></div></div></div>'
  })

}(window.jQuery);
/* ==========================================================
 * bootstrap-affix.js v2.2.1
 * http://twitter.github.com/bootstrap/javascript.html#affix
 * ==========================================================
 * Copyright 2012 Twitter, Inc.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 * http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 * ========================================================== */


!function ($) {

  "use strict"; // jshint ;_;


 /* AFFIX CLASS DEFINITION
  * ====================== */

  var Affix = function (element, options) {
    this.options = $.extend({}, $.fn.affix.defaults, options)
    this.$window = $(window)
      .on('scroll.affix.data-api', $.proxy(this.checkPosition, this))
      .on('click.affix.data-api',  $.proxy(function () { setTimeout($.proxy(this.checkPosition, this), 1) }, this))
    this.$element = $(element)
    this.checkPosition()
  }

  Affix.prototype.checkPosition = function () {
    if (!this.$element.is(':visible')) return

    var scrollHeight = $(document).height()
      , scrollTop = this.$window.scrollTop()
      , position = this.$element.offset()
      , offset = this.options.offset
      , offsetBottom = offset.bottom
      , offsetTop = offset.top
      , reset = 'affix affix-top affix-bottom'
      , affix

    if (typeof offset != 'object') offsetBottom = offsetTop = offset
    if (typeof offsetTop == 'function') offsetTop = offset.top()
    if (typeof offsetBottom == 'function') offsetBottom = offset.bottom()

    affix = this.unpin != null && (scrollTop + this.unpin <= position.top) ?
      false    : offsetBottom != null && (position.top + this.$element.height() >= scrollHeight - offsetBottom) ?
      'bottom' : offsetTop != null && scrollTop <= offsetTop ?
      'top'    : false

    if (this.affixed === affix) return

    this.affixed = affix
    this.unpin = affix == 'bottom' ? position.top - scrollTop : null

    this.$element.removeClass(reset).addClass('affix' + (affix ? '-' + affix : ''))
  }


 /* AFFIX PLUGIN DEFINITION
  * ======================= */

  $.fn.affix = function (option) {
    return this.each(function () {
      var $this = $(this)
        , data = $this.data('affix')
        , options = typeof option == 'object' && option
      if (!data) $this.data('affix', (data = new Affix(this, options)))
      if (typeof option == 'string') data[option]()
    })
  }

  $.fn.affix.Constructor = Affix

  $.fn.affix.defaults = {
    offset: 0
  }


 /* AFFIX DATA-API
  * ============== */

  $(window).on('load', function () {
    $('[data-spy="affix"]').each(function () {
      var $spy = $(this)
        , data = $spy.data()

      data.offset = data.offset || {}

      data.offsetBottom && (data.offset.bottom = data.offsetBottom)
      data.offsetTop && (data.offset.top = data.offsetTop)

      $spy.affix(data)
    })
  })


}(window.jQuery);
/* ==========================================================
 * bootstrap-alert.js v2.2.1
 * http://twitter.github.com/bootstrap/javascript.html#alerts
 * ==========================================================
 * Copyright 2012 Twitter, Inc.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 * http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 * ========================================================== */


!function ($) {

  "use strict"; // jshint ;_;


 /* ALERT CLASS DEFINITION
  * ====================== */

  var dismiss = '[data-dismiss="alert"]'
    , Alert = function (el) {
        $(el).on('click', dismiss, this.close)
      }

  Alert.prototype.close = function (e) {
    var $this = $(this)
      , selector = $this.attr('data-target')
      , $parent

    if (!selector) {
      selector = $this.attr('href')
      selector = selector && selector.replace(/.*(?=#[^\s]*$)/, '') //strip for ie7
    }

    $parent = $(selector)

    e && e.preventDefault()

    $parent.length || ($parent = $this.hasClass('alert') ? $this : $this.parent())

    $parent.trigger(e = $.Event('close'))

    if (e.isDefaultPrevented()) return

    $parent.removeClass('in')

    function removeElement() {
      $parent
        .trigger('closed')
        .remove()
    }

    $.support.transition && $parent.hasClass('fade') ?
      $parent.on($.support.transition.end, removeElement) :
      removeElement()
  }


 /* ALERT PLUGIN DEFINITION
  * ======================= */

  $.fn.alert = function (option) {
    return this.each(function () {
      var $this = $(this)
        , data = $this.data('alert')
      if (!data) $this.data('alert', (data = new Alert(this)))
      if (typeof option == 'string') data[option].call($this)
    })
  }

  $.fn.alert.Constructor = Alert


 /* ALERT DATA-API
  * ============== */

  $(document).on('click.alert.data-api', dismiss, Alert.prototype.close)

}(window.jQuery);
/* ============================================================
 * bootstrap-button.js v2.2.1
 * http://twitter.github.com/bootstrap/javascript.html#buttons
 * ============================================================
 * Copyright 2012 Twitter, Inc.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 * http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 * ============================================================ */


!function ($) {

  "use strict"; // jshint ;_;


 /* BUTTON PUBLIC CLASS DEFINITION
  * ============================== */

  var Button = function (element, options) {
    this.$element = $(element)
    this.options = $.extend({}, $.fn.button.defaults, options)
  }

  Button.prototype.setState = function (state) {
    var d = 'disabled'
      , $el = this.$element
      , data = $el.data()
      , val = $el.is('input') ? 'val' : 'html'

    state = state + 'Text'
    data.resetText || $el.data('resetText', $el[val]())

    $el[val](data[state] || this.options[state])

    // push to event loop to allow forms to submit
    setTimeout(function () {
      state == 'loadingText' ?
        $el.addClass(d).attr(d, d) :
        $el.removeClass(d).removeAttr(d)
    }, 0)
  }

  Button.prototype.toggle = function () {
    var $parent = this.$element.closest('[data-toggle="buttons-radio"]')

    $parent && $parent
      .find('.active')
      .removeClass('active')

    this.$element.toggleClass('active')
  }


 /* BUTTON PLUGIN DEFINITION
  * ======================== */

  $.fn.button = function (option) {
    return this.each(function () {
      var $this = $(this)
        , data = $this.data('button')
        , options = typeof option == 'object' && option
      if (!data) $this.data('button', (data = new Button(this, options)))
      if (option == 'toggle') data.toggle()
      else if (option) data.setState(option)
    })
  }

  $.fn.button.defaults = {
    loadingText: 'loading...'
  }

  $.fn.button.Constructor = Button


 /* BUTTON DATA-API
  * =============== */

  $(document).on('click.button.data-api', '[data-toggle^=button]', function (e) {
    var $btn = $(e.target)
    if (!$btn.hasClass('btn')) $btn = $btn.closest('.btn')
    $btn.button('toggle')
  })

}(window.jQuery);
/* =============================================================
 * bootstrap-collapse.js v2.2.1
 * http://twitter.github.com/bootstrap/javascript.html#collapse
 * =============================================================
 * Copyright 2012 Twitter, Inc.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 * http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 * ============================================================ */


!function ($) {

  "use strict"; // jshint ;_;


 /* COLLAPSE PUBLIC CLASS DEFINITION
  * ================================ */

  var Collapse = function (element, options) {
    this.$element = $(element)
    this.options = $.extend({}, $.fn.collapse.defaults, options)

    if (this.options.parent) {
      this.$parent = $(this.options.parent)
    }

    this.options.toggle && this.toggle()
  }

  Collapse.prototype = {

    constructor: Collapse

  , dimension: function () {
      var hasWidth = this.$element.hasClass('width')
      return hasWidth ? 'width' : 'height'
    }

  , show: function () {
      var dimension
        , scroll
        , actives
        , hasData

      if (this.transitioning) return

      dimension = this.dimension()
      scroll = $.camelCase(['scroll', dimension].join('-'))
      actives = this.$parent && this.$parent.find('> .accordion-group > .in')

      if (actives && actives.length) {
        hasData = actives.data('collapse')
        if (hasData && hasData.transitioning) return
        actives.collapse('hide')
        hasData || actives.data('collapse', null)
      }

      this.$element[dimension](0)
      this.transition('addClass', $.Event('show'), 'shown')
      $.support.transition && this.$element[dimension](this.$element[0][scroll])
    }

  , hide: function () {
      var dimension
      if (this.transitioning) return
      dimension = this.dimension()
      this.reset(this.$element[dimension]())
      this.transition('removeClass', $.Event('hide'), 'hidden')
      this.$element[dimension](0)
    }

  , reset: function (size) {
      var dimension = this.dimension()

      this.$element
        .removeClass('collapse')
        [dimension](size || 'auto')
        [0].offsetWidth

      this.$element[size !== null ? 'addClass' : 'removeClass']('collapse')

      return this
    }

  , transition: function (method, startEvent, completeEvent) {
      var that = this
        , complete = function () {
            if (startEvent.type == 'show') that.reset()
            that.transitioning = 0
            that.$element.trigger(completeEvent)
          }

      this.$element.trigger(startEvent)

      if (startEvent.isDefaultPrevented()) return

      this.transitioning = 1

      this.$element[method]('in')

      $.support.transition && this.$element.hasClass('collapse') ?
        this.$element.one($.support.transition.end, complete) :
        complete()
    }

  , toggle: function () {
      this[this.$element.hasClass('in') ? 'hide' : 'show']()
    }

  }


 /* COLLAPSIBLE PLUGIN DEFINITION
  * ============================== */

  $.fn.collapse = function (option) {
    return this.each(function () {
      var $this = $(this)
        , data = $this.data('collapse')
        , options = typeof option == 'object' && option
      if (!data) $this.data('collapse', (data = new Collapse(this, options)))
      if (typeof option == 'string') data[option]()
    })
  }

  $.fn.collapse.defaults = {
    toggle: true
  }

  $.fn.collapse.Constructor = Collapse


 /* COLLAPSIBLE DATA-API
  * ==================== */

  $(document).on('click.collapse.data-api', '[data-toggle=collapse]', function (e) {
    var $this = $(this), href
      , target = $this.attr('data-target')
        || e.preventDefault()
        || (href = $this.attr('href')) && href.replace(/.*(?=#[^\s]+$)/, '') //strip for ie7
      , option = $(target).data('collapse') ? 'toggle' : $this.data()
    $this[$(target).hasClass('in') ? 'addClass' : 'removeClass']('collapsed')
    $(target).collapse(option)
  })

}(window.jQuery);
/* ==========================================================
 * bootstrap-carousel.js v2.2.1
 * http://twitter.github.com/bootstrap/javascript.html#carousel
 * ==========================================================
 * Copyright 2012 Twitter, Inc.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 * http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 * ========================================================== */


!function ($) {

  "use strict"; // jshint ;_;


 /* CAROUSEL CLASS DEFINITION
  * ========================= */

  var Carousel = function (element, options) {
    this.$element = $(element)
    this.options = options
    this.options.slide && this.slide(this.options.slide)
    this.options.pause == 'hover' && this.$element
      .on('mouseenter', $.proxy(this.pause, this))
      .on('mouseleave', $.proxy(this.cycle, this))
  }

  Carousel.prototype = {

    cycle: function (e) {
      if (!e) this.paused = false
      this.options.interval
        && !this.paused
        && (this.interval = setInterval($.proxy(this.next, this), this.options.interval))
      return this
    }

  , to: function (pos) {
      var $active = this.$element.find('.item.active')
        , children = $active.parent().children()
        , activePos = children.index($active)
        , that = this

      if (pos > (children.length - 1) || pos < 0) return

      if (this.sliding) {
        return this.$element.one('slid', function () {
          that.to(pos)
        })
      }

      if (activePos == pos) {
        return this.pause().cycle()
      }

      return this.slide(pos > activePos ? 'next' : 'prev', $(children[pos]))
    }

  , pause: function (e) {
      if (!e) this.paused = true
      if (this.$element.find('.next, .prev').length && $.support.transition.end) {
        this.$element.trigger($.support.transition.end)
        this.cycle()
      }
      clearInterval(this.interval)
      this.interval = null
      return this
    }

  , next: function () {
      if (this.sliding) return
      return this.slide('next')
    }

  , prev: function () {
      if (this.sliding) return
      return this.slide('prev')
    }

  , slide: function (type, next) {
      var $active = this.$element.find('.item.active')
        , $next = next || $active[type]()
        , isCycling = this.interval
        , direction = type == 'next' ? 'left' : 'right'
        , fallback  = type == 'next' ? 'first' : 'last'
        , that = this
        , e

      this.sliding = true

      isCycling && this.pause()

      $next = $next.length ? $next : this.$element.find('.item')[fallback]()

      e = $.Event('slide', {
        relatedTarget: $next[0]
      })

      if ($next.hasClass('active')) return

      if ($.support.transition && this.$element.hasClass('slide')) {
        this.$element.trigger(e)
        if (e.isDefaultPrevented()) return
        $next.addClass(type)
        $next[0].offsetWidth // force reflow
        $active.addClass(direction)
        $next.addClass(direction)
        this.$element.one($.support.transition.end, function () {
          $next.removeClass([type, direction].join(' ')).addClass('active')
          $active.removeClass(['active', direction].join(' '))
          that.sliding = false
          setTimeout(function () { that.$element.trigger('slid') }, 0)
        })
      } else {
        this.$element.trigger(e)
        if (e.isDefaultPrevented()) return
        $active.removeClass('active')
        $next.addClass('active')
        this.sliding = false
        this.$element.trigger('slid')
      }

      isCycling && this.cycle()

      return this
    }

  }


 /* CAROUSEL PLUGIN DEFINITION
  * ========================== */

  $.fn.carousel = function (option) {
    return this.each(function () {
      var $this = $(this)
        , data = $this.data('carousel')
        , options = $.extend({}, $.fn.carousel.defaults, typeof option == 'object' && option)
        , action = typeof option == 'string' ? option : options.slide
      if (!data) $this.data('carousel', (data = new Carousel(this, options)))
      if (typeof option == 'number') data.to(option)
      else if (action) data[action]()
      else if (options.interval) data.cycle()
    })
  }

  $.fn.carousel.defaults = {
    interval: 5000
  , pause: 'hover'
  }

  $.fn.carousel.Constructor = Carousel


 /* CAROUSEL DATA-API
  * ================= */

  $(document).on('click.carousel.data-api', '[data-slide]', function (e) {
    var $this = $(this), href
      , $target = $($this.attr('data-target') || (href = $this.attr('href')) && href.replace(/.*(?=#[^\s]+$)/, '')) //strip for ie7
      , options = $.extend({}, $target.data(), $this.data())
    $target.carousel(options)
    e.preventDefault()
  })

}(window.jQuery);
/* =============================================================
 * bootstrap-typeahead.js v2.2.1
 * http://twitter.github.com/bootstrap/javascript.html#typeahead
 * =============================================================
 * Copyright 2012 Twitter, Inc.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 * http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 * ============================================================ */


!function($){

  "use strict"; // jshint ;_;


 /* TYPEAHEAD PUBLIC CLASS DEFINITION
  * ================================= */

  var Typeahead = function (element, options) {
    this.$element = $(element)
    this.options = $.extend({}, $.fn.typeahead.defaults, options)
    this.matcher = this.options.matcher || this.matcher
    this.sorter = this.options.sorter || this.sorter
    this.highlighter = this.options.highlighter || this.highlighter
    this.updater = this.options.updater || this.updater
    this.$menu = $(this.options.menu).appendTo('body')
    this.source = this.options.source
    this.shown = false
    this.listen()
  }

  Typeahead.prototype = {

    constructor: Typeahead

  , select: function () {
      var val = this.$menu.find('.active').attr('data-value')
      this.$element
        .val(this.updater(val))
        .change()
      return this.hide()
    }

  , updater: function (item) {
      return item
    }

  , show: function () {
      var pos = $.extend({}, this.$element.offset(), {
        height: this.$element[0].offsetHeight
      })

      this.$menu.css({
        top: pos.top + pos.height
      , left: pos.left
      })

      this.$menu.show()
      this.shown = true
      return this
    }

  , hide: function () {
      this.$menu.hide()
      this.shown = false
      return this
    }

  , lookup: function (event) {
      var items

      this.query = this.$element.val()

      if (!this.query || this.query.length < this.options.minLength) {
        return this.shown ? this.hide() : this
      }

      items = $.isFunction(this.source) ? this.source(this.query, $.proxy(this.process, this)) : this.source

      return items ? this.process(items) : this
    }

  , process: function (items) {
      var that = this

      items = $.grep(items, function (item) {
        return that.matcher(item)
      })

      items = this.sorter(items)

      if (!items.length) {
        return this.shown ? this.hide() : this
      }

      return this.render(items.slice(0, this.options.items)).show()
    }

  , matcher: function (item) {
      return ~item.toLowerCase().indexOf(this.query.toLowerCase())
    }

  , sorter: function (items) {
      var beginswith = []
        , caseSensitive = []
        , caseInsensitive = []
        , item

      while (item = items.shift()) {
        if (!item.toLowerCase().indexOf(this.query.toLowerCase())) beginswith.push(item)
        else if (~item.indexOf(this.query)) caseSensitive.push(item)
        else caseInsensitive.push(item)
      }

      return beginswith.concat(caseSensitive, caseInsensitive)
    }

  , highlighter: function (item) {
      var query = this.query.replace(/[\-\[\]{}()*+?.,\\\^$|#\s]/g, '\\$&')
      return item.replace(new RegExp('(' + query + ')', 'ig'), function ($1, match) {
        return '<strong>' + match + '</strong>'
      })
    }

  , render: function (items) {
      var that = this

      items = $(items).map(function (i, item) {
        i = $(that.options.item).attr('data-value', item)
        i.find('a').html(that.highlighter(item))
        return i[0]
      })

      items.first().addClass('active')
      this.$menu.html(items)
      return this
    }

  , next: function (event) {
      var active = this.$menu.find('.active').removeClass('active')
        , next = active.next()

      if (!next.length) {
        next = $(this.$menu.find('li')[0])
      }

      next.addClass('active')
    }

  , prev: function (event) {
      var active = this.$menu.find('.active').removeClass('active')
        , prev = active.prev()

      if (!prev.length) {
        prev = this.$menu.find('li').last()
      }

      prev.addClass('active')
    }

  , listen: function () {
      this.$element
        .on('blur',     $.proxy(this.blur, this))
        .on('keypress', $.proxy(this.keypress, this))
        .on('keyup',    $.proxy(this.keyup, this))

      if (this.eventSupported('keydown')) {
        this.$element.on('keydown', $.proxy(this.keydown, this))
      }

      this.$menu
        .on('click', $.proxy(this.click, this))
        .on('mouseenter', 'li', $.proxy(this.mouseenter, this))
    }

  , eventSupported: function(eventName) {
      var isSupported = eventName in this.$element
      if (!isSupported) {
        this.$element.setAttribute(eventName, 'return;')
        isSupported = typeof this.$element[eventName] === 'function'
      }
      return isSupported
    }

  , move: function (e) {
      if (!this.shown) return

      switch(e.keyCode) {
        case 9: // tab
        case 13: // enter
        case 27: // escape
          e.preventDefault()
          break

        case 38: // up arrow
          e.preventDefault()
          this.prev()
          break

        case 40: // down arrow
          e.preventDefault()
          this.next()
          break
      }

      e.stopPropagation()
    }

  , keydown: function (e) {
      this.suppressKeyPressRepeat = !~$.inArray(e.keyCode, [40,38,9,13,27])
      this.move(e)
    }

  , keypress: function (e) {
      if (this.suppressKeyPressRepeat) return
      this.move(e)
    }

  , keyup: function (e) {
      switch(e.keyCode) {
        case 40: // down arrow
        case 38: // up arrow
        case 16: // shift
        case 17: // ctrl
        case 18: // alt
          break

        case 9: // tab
        case 13: // enter
          if (!this.shown) return
          this.select()
          break

        case 27: // escape
          if (!this.shown) return
          this.hide()
          break

        default:
          this.lookup()
      }

      e.stopPropagation()
      e.preventDefault()
  }

  , blur: function (e) {
      var that = this
      setTimeout(function () { that.hide() }, 150)
    }

  , click: function (e) {
      e.stopPropagation()
      e.preventDefault()
      this.select()
    }

  , mouseenter: function (e) {
      this.$menu.find('.active').removeClass('active')
      $(e.currentTarget).addClass('active')
    }

  }


  /* TYPEAHEAD PLUGIN DEFINITION
   * =========================== */

  $.fn.typeahead = function (option) {
    return this.each(function () {
      var $this = $(this)
        , data = $this.data('typeahead')
        , options = typeof option == 'object' && option
      if (!data) $this.data('typeahead', (data = new Typeahead(this, options)))
      if (typeof option == 'string') data[option]()
    })
  }

  $.fn.typeahead.defaults = {
    source: []
  , items: 8
  , menu: '<ul class="typeahead dropdown-menu"></ul>'
  , item: '<li><a href="#"></a></li>'
  , minLength: 1
  }

  $.fn.typeahead.Constructor = Typeahead


 /*   TYPEAHEAD DATA-API
  * ================== */

  $(document).on('focus.typeahead.data-api', '[data-provide="typeahead"]', function (e) {
    var $this = $(this)
    if ($this.data('typeahead')) return
    e.preventDefault()
    $this.typeahead($this.data())
  })

}(window.jQuery);


File: /lib\font-awesome\.gitignore
File: /lib\font-awesome\css\font-awesome-ie7.css
[class^="icon-"],
[class*=" icon-"] {
  font-family: FontAwesome;
  font-style: normal;
  font-weight: normal;
}
.btn.dropdown-toggle [class^="icon-"],
.btn.dropdown-toggle [class*=" icon-"] {
  /* keeps button heights with and without icons the same */

  line-height: 1.4em;
}
.icon-large {
  font-size: 1.3333em;
}
.icon-glass {
  *zoom: expression( this.runtimeStyle['zoom'] = '1', this.innerHTML = '&#xf000;&nbsp;');
}
.icon-music {
  *zoom: expression( this.runtimeStyle['zoom'] = '1', this.innerHTML = '&#xf001;&nbsp;');
}
.icon-search {
  *zoom: expression( this.runtimeStyle['zoom'] = '1', this.innerHTML = '&#xf002;&nbsp;');
}
.icon-envelope {
  *zoom: expression( this.runtimeStyle['zoom'] = '1', this.innerHTML = '&#xf003;&nbsp;');
}
.icon-heart {
  *zoom: expression( this.runtimeStyle['zoom'] = '1', this.innerHTML = '&#xf004;&nbsp;');
}
.icon-star {
  *zoom: expression( this.runtimeStyle['zoom'] = '1', this.innerHTML = '&#xf005;&nbsp;');
}
.icon-star-empty {
  *zoom: expression( this.runtimeStyle['zoom'] = '1', this.innerHTML = '&#xf006;&nbsp;');
}
.icon-user {
  *zoom: expression( this.runtimeStyle['zoom'] = '1', this.innerHTML = '&#xf007;&nbsp;');
}
.icon-film {
  *zoom: expression( this.runtimeStyle['zoom'] = '1', this.innerHTML = '&#xf008;&nbsp;');
}
.icon-th-large {
  *zoom: expression( this.runtimeStyle['zoom'] = '1', this.innerHTML = '&#xf009;&nbsp;');
}
.icon-th {
  *zoom: expression( this.runtimeStyle['zoom'] = '1', this.innerHTML = '&#xf00a;&nbsp;');
}
.icon-th-list {
  *zoom: expression( this.runtimeStyle['zoom'] = '1', this.innerHTML = '&#xf00b;&nbsp;');
}
.icon-ok {
  *zoom: expression( this.runtimeStyle['zoom'] = '1', this.innerHTML = '&#xf00c;&nbsp;');
}
.icon-remove {
  *zoom: expression( this.runtimeStyle['zoom'] = '1', this.innerHTML = '&#xf00d;&nbsp;');
}
.icon-zoom-in {
  *zoom: expression( this.runtimeStyle['zoom'] = '1', this.innerHTML = '&#xf00e;&nbsp;');
}
.icon-zoom-out {
  *zoom: expression( this.runtimeStyle['zoom'] = '1', this.innerHTML = '&#xf010;&nbsp;');
}
.icon-off {
  *zoom: expression( this.runtimeStyle['zoom'] = '1', this.innerHTML = '&#xf011;&nbsp;');
}
.icon-signal {
  *zoom: expression( this.runtimeStyle['zoom'] = '1', this.innerHTML = '&#xf012;&nbsp;');
}
.icon-cog {
  *zoom: expression( this.runtimeStyle['zoom'] = '1', this.innerHTML = '&#xf013;&nbsp;');
}
.icon-trash {
  *zoom: expression( this.runtimeStyle['zoom'] = '1', this.innerHTML = '&#xf014;&nbsp;');
}
.icon-home {
  *zoom: expression( this.runtimeStyle['zoom'] = '1', this.innerHTML = '&#xf015;&nbsp;');
}
.icon-file {
  *zoom: expression( this.runtimeStyle['zoom'] = '1', this.innerHTML = '&#xf016;&nbsp;');
}
.icon-time {
  *zoom: expression( this.runtimeStyle['zoom'] = '1', this.innerHTML = '&#xf017;&nbsp;');
}
.icon-road {
  *zoom: expression( this.runtimeStyle['zoom'] = '1', this.innerHTML = '&#xf018;&nbsp;');
}
.icon-download-alt {
  *zoom: expression( this.runtimeStyle['zoom'] = '1', this.innerHTML = '&#xf019;&nbsp;');
}
.icon-download {
  *zoom: expression( this.runtimeStyle['zoom'] = '1', this.innerHTML = '&#xf01a;&nbsp;');
}
.icon-upload {
  *zoom: expression( this.runtimeStyle['zoom'] = '1', this.innerHTML = '&#xf01b;&nbsp;');
}
.icon-inbox {
  *zoom: expression( this.runtimeStyle['zoom'] = '1', this.innerHTML = '&#xf01c;&nbsp;');
}
.icon-play-circle {
  *zoom: expression( this.runtimeStyle['zoom'] = '1', this.innerHTML = '&#xf01d;&nbsp;');
}
.icon-repeat {
  *zoom: expression( this.runtimeStyle['zoom'] = '1', this.innerHTML = '&#xf01e;&nbsp;');
}
.icon-refresh {
  *zoom: expression( this.runtimeStyle['zoom'] = '1', this.innerHTML = '&#xf021;&nbsp;');
}
.icon-list-alt {
  *zoom: expression( this.runtimeStyle['zoom'] = '1', this.innerHTML = '&#xf022;&nbsp;');
}
.icon-lock {
  *zoom: expression( this.runtimeStyle['zoom'] = '1', this.innerHTML = '&#xf023;&nbsp;');
}
.icon-flag {
  *zoom: expression( this.runtimeStyle['zoom'] = '1', this.innerHTML = '&#xf024;&nbsp;');
}
.icon-headphones {
  *zoom: expression( this.runtimeStyle['zoom'] = '1', this.innerHTML = '&#xf025;&nbsp;');
}
.icon-volume-off {
  *zoom: expression( this.runtimeStyle['zoom'] = '1', this.innerHTML = '&#xf026;&nbsp;');
}
.icon-volume-down {
  *zoom: expression( this.runtimeStyle['zoom'] = '1', this.innerHTML = '&#xf027;&nbsp;');
}
.icon-volume-up {
  *zoom: expression( this.runtimeStyle['zoom'] = '1', this.innerHTML = '&#xf028;&nbsp;');
}
.icon-qrcode {
  *zoom: expression( this.runtimeStyle['zoom'] = '1', this.innerHTML = '&#xf029;&nbsp;');
}
.icon-barcode {
  *zoom: expression( this.runtimeStyle['zoom'] = '1', this.innerHTML = '&#xf02a;&nbsp;');
}
.icon-tag {
  *zoom: expression( this.runtimeStyle['zoom'] = '1', this.innerHTML = '&#xf02b;&nbsp;');
}
.icon-tags {
  *zoom: expression( this.runtimeStyle['zoom'] = '1', this.innerHTML = '&#xf02c;&nbsp;');
}
.icon-book {
  *zoom: expression( this.runtimeStyle['zoom'] = '1', this.innerHTML = '&#xf02d;&nbsp;');
}
.icon-bookmark {
  *zoom: expression( this.runtimeStyle['zoom'] = '1', this.innerHTML = '&#xf02e;&nbsp;');
}
.icon-print {
  *zoom: expression( this.runtimeStyle['zoom'] = '1', this.innerHTML = '&#xf02f;&nbsp;');
}
.icon-camera {
  *zoom: expression( this.runtimeStyle['zoom'] = '1', this.innerHTML = '&#xf030;&nbsp;');
}
.icon-font {
  *zoom: expression( this.runtimeStyle['zoom'] = '1', this.innerHTML = '&#xf031;&nbsp;');
}
.icon-bold {
  *zoom: expression( this.runtimeStyle['zoom'] = '1', this.innerHTML = '&#xf032;&nbsp;');
}
.icon-italic {
  *zoom: expression( this.runtimeStyle['zoom'] = '1', this.innerHTML = '&#xf033;&nbsp;');
}
.icon-text-height {
  *zoom: expression( this.runtimeStyle['zoom'] = '1', this.innerHTML = '&#xf034;&nbsp;');
}
.icon-text-width {
  *zoom: expression( this.runtimeStyle['zoom'] = '1', this.innerHTML = '&#xf035;&nbsp;');
}
.icon-align-left {
  *zoom: expression( this.runtimeStyle['zoom'] = '1', this.innerHTML = '&#xf036;&nbsp;');
}
.icon-align-center {
  *zoom: expression( this.runtimeStyle['zoom'] = '1', this.innerHTML = '&#xf037;&nbsp;');
}
.icon-align-right {
  *zoom: expression( this.runtimeStyle['zoom'] = '1', this.innerHTML = '&#xf038;&nbsp;');
}
.icon-align-justify {
  *zoom: expression( this.runtimeStyle['zoom'] = '1', this.innerHTML = '&#xf039;&nbsp;');
}
.icon-list {
  *zoom: expression( this.runtimeStyle['zoom'] = '1', this.innerHTML = '&#xf03a;&nbsp;');
}
.icon-indent-left {
  *zoom: expression( this.runtimeStyle['zoom'] = '1', this.innerHTML = '&#xf03b;&nbsp;');
}
.icon-indent-right {
  *zoom: expression( this.runtimeStyle['zoom'] = '1', this.innerHTML = '&#xf03c;&nbsp;');
}
.icon-facetime-video {
  *zoom: expression( this.runtimeStyle['zoom'] = '1', this.innerHTML = '&#xf03d;&nbsp;');
}
.icon-picture {
  *zoom: expression( this.runtimeStyle['zoom'] = '1', this.innerHTML = '&#xf03e;&nbsp;');
}
.icon-pencil {
  *zoom: expression( this.runtimeStyle['zoom'] = '1', this.innerHTML = '&#xf040;&nbsp;');
}
.icon-map-marker {
  *zoom: expression( this.runtimeStyle['zoom'] = '1', this.innerHTML = '&#xf041;&nbsp;');
}
.icon-adjust {
  *zoom: expression( this.runtimeStyle['zoom'] = '1', this.innerHTML = '&#xf042;&nbsp;');
}
.icon-tint {
  *zoom: expression( this.runtimeStyle['zoom'] = '1', this.innerHTML = '&#xf043;&nbsp;');
}
.icon-edit {
  *zoom: expression( this.runtimeStyle['zoom'] = '1', this.innerHTML = '&#xf044;&nbsp;');
}
.icon-share {
  *zoom: expression( this.runtimeStyle['zoom'] = '1', this.innerHTML = '&#xf045;&nbsp;');
}
.icon-check {
  *zoom: expression( this.runtimeStyle['zoom'] = '1', this.innerHTML = '&#xf046;&nbsp;');
}
.icon-move {
  *zoom: expression( this.runtimeStyle['zoom'] = '1', this.innerHTML = '&#xf047;&nbsp;');
}
.icon-step-backward {
  *zoom: expression( this.runtimeStyle['zoom'] = '1', this.innerHTML = '&#xf048;&nbsp;');
}
.icon-fast-backward {
  *zoom: expression( this.runtimeStyle['zoom'] = '1', this.innerHTML = '&#xf049;&nbsp;');
}
.icon-backward {
  *zoom: expression( this.runtimeStyle['zoom'] = '1', this.innerHTML = '&#xf04a;&nbsp;');
}
.icon-play {
  *zoom: expression( this.runtimeStyle['zoom'] = '1', this.innerHTML = '&#xf04b;&nbsp;');
}
.icon-pause {
  *zoom: expression( this.runtimeStyle['zoom'] = '1', this.innerHTML = '&#xf04c;&nbsp;');
}
.icon-stop {
  *zoom: expression( this.runtimeStyle['zoom'] = '1', this.innerHTML = '&#xf04d;&nbsp;');
}
.icon-forward {
  *zoom: expression( this.runtimeStyle['zoom'] = '1', this.innerHTML = '&#xf04e;&nbsp;');
}
.icon-fast-forward {
  *zoom: expression( this.runtimeStyle['zoom'] = '1', this.innerHTML = '&#xf050;&nbsp;');
}
.icon-step-forward {
  *zoom: expression( this.runtimeStyle['zoom'] = '1', this.innerHTML = '&#xf051;&nbsp;');
}
.icon-eject {
  *zoom: expression( this.runtimeStyle['zoom'] = '1', this.innerHTML = '&#xf052;&nbsp;');
}
.icon-chevron-left {
  *zoom: expression( this.runtimeStyle['zoom'] = '1', this.innerHTML = '&#xf053;&nbsp;');
}
.icon-chevron-right {
  *zoom: expression( this.runtimeStyle['zoom'] = '1', this.innerHTML = '&#xf054;&nbsp;');
}
.icon-plus-sign {
  *zoom: expression( this.runtimeStyle['zoom'] = '1', this.innerHTML = '&#xf055;&nbsp;');
}
.icon-minus-sign {
  *zoom: expression( this.runtimeStyle['zoom'] = '1', this.innerHTML = '&#xf056;&nbsp;');
}
.icon-remove-sign {
  *zoom: expression( this.runtimeStyle['zoom'] = '1', this.innerHTML = '&#xf057;&nbsp;');
}
.icon-ok-sign {
  *zoom: expression( this.runtimeStyle['zoom'] = '1', this.innerHTML = '&#xf058;&nbsp;');
}
.icon-question-sign {
  *zoom: expression( this.runtimeStyle['zoom'] = '1', this.innerHTML = '&#xf059;&nbsp;');
}
.icon-info-sign {
  *zoom: expression( this.runtimeStyle['zoom'] = '1', this.innerHTML = '&#xf05a;&nbsp;');
}
.icon-screenshot {
  *zoom: expression( this.runtimeStyle['zoom'] = '1', this.innerHTML = '&#xf05b;&nbsp;');
}
.icon-remove-circle {
  *zoom: expression( this.runtimeStyle['zoom'] = '1', this.innerHTML = '&#xf05c;&nbsp;');
}
.icon-ok-circle {
  *zoom: expression( this.runtimeStyle['zoom'] = '1', this.innerHTML = '&#xf05d;&nbsp;');
}
.icon-ban-circle {
  *zoom: expression( this.runtimeStyle['zoom'] = '1', this.innerHTML = '&#xf05e;&nbsp;');
}
.icon-arrow-left {
  *zoom: expression( this.runtimeStyle['zoom'] = '1', this.innerHTML = '&#xf060;&nbsp;');
}
.icon-arrow-right {
  *zoom: expression( this.runtimeStyle['zoom'] = '1', this.innerHTML = '&#xf061;&nbsp;');
}
.icon-arrow-up {
  *zoom: expression( this.runtimeStyle['zoom'] = '1', this.innerHTML = '&#xf062;&nbsp;');
}
.icon-arrow-down {
  *zoom: expression( this.runtimeStyle['zoom'] = '1', this.innerHTML = '&#xf063;&nbsp;');
}
.icon-share-alt {
  *zoom: expression( this.runtimeStyle['zoom'] = '1', this.innerHTML = '&#xf064;&nbsp;');
}
.icon-resize-full {
  *zoom: expression( this.runtimeStyle['zoom'] = '1', this.innerHTML = '&#xf065;&nbsp;');
}
.icon-resize-small {
  *zoom: expression( this.runtimeStyle['zoom'] = '1', this.innerHTML = '&#xf066;&nbsp;');
}
.icon-plus {
  *zoom: expression( this.runtimeStyle['zoom'] = '1', this.innerHTML = '&#xf067;&nbsp;');
}
.icon-minus {
  *zoom: expression( this.runtimeStyle['zoom'] = '1', this.innerHTML = '&#xf068;&nbsp;');
}
.icon-asterisk {
  *zoom: expression( this.runtimeStyle['zoom'] = '1', this.innerHTML = '&#xf069;&nbsp;');
}
.icon-exclamation-sign {
  *zoom: expression( this.runtimeStyle['zoom'] = '1', this.innerHTML = '&#xf06a;&nbsp;');
}
.icon-gift {
  *zoom: expression( this.runtimeStyle['zoom'] = '1', this.innerHTML = '&#xf06b;&nbsp;');
}
.icon-leaf {
  *zoom: expression( this.runtimeStyle['zoom'] = '1', this.innerHTML = '&#xf06c;&nbsp;');
}
.icon-fire {
  *zoom: expression( this.runtimeStyle['zoom'] = '1', this.innerHTML = '&#xf06d;&nbsp;');
}
.icon-eye-open {
  *zoom: expression( this.runtimeStyle['zoom'] = '1', this.innerHTML = '&#xf06e;&nbsp;');
}
.icon-eye-close {
  *zoom: expression( this.runtimeStyle['zoom'] = '1', this.innerHTML = '&#xf070;&nbsp;');
}
.icon-warning-sign {
  *zoom: expression( this.runtimeStyle['zoom'] = '1', this.innerHTML = '&#xf071;&nbsp;');
}
.icon-plane {
  *zoom: expression( this.runtimeStyle['zoom'] = '1', this.innerHTML = '&#xf072;&nbsp;');
}
.icon-calendar {
  *zoom: expression( this.runtimeStyle['zoom'] = '1', this.innerHTML = '&#xf073;&nbsp;');
}
.icon-random {
  *zoom: expression( this.runtimeStyle['zoom'] = '1', this.innerHTML = '&#xf074;&nbsp;');
}
.icon-comment {
  *zoom: expression( this.runtimeStyle['zoom'] = '1', this.innerHTML = '&#xf075;&nbsp;');
}
.icon-magnet {
  *zoom: expression( this.runtimeStyle['zoom'] = '1', this.innerHTML = '&#xf076;&nbsp;');
}
.icon-chevron-up {
  *zoom: expression( this.runtimeStyle['zoom'] = '1', this.innerHTML = '&#xf077;&nbsp;');
}
.icon-chevron-down {
  *zoom: expression( this.runtimeStyle['zoom'] = '1', this.innerHTML = '&#xf078;&nbsp;');
}
.icon-retweet {
  *zoom: expression( this.runtimeStyle['zoom'] = '1', this.innerHTML = '&#xf079;&nbsp;');
}
.icon-shopping-cart {
  *zoom: expression( this.runtimeStyle['zoom'] = '1', this.innerHTML = '&#xf07a;&nbsp;');
}
.icon-folder-close {
  *zoom: expression( this.runtimeStyle['zoom'] = '1', this.innerHTML = '&#xf07b;&nbsp;');
}
.icon-folder-open {
  *zoom: expression( this.runtimeStyle['zoom'] = '1', this.innerHTML = '&#xf07c;&nbsp;');
}
.icon-resize-vertical {
  *zoom: expression( this.runtimeStyle['zoom'] = '1', this.innerHTML = '&#xf07d;&nbsp;');
}
.icon-resize-horizontal {
  *zoom: expression( this.runtimeStyle['zoom'] = '1', this.innerHTML = '&#xf07e;&nbsp;');
}
.icon-bar-chart {
  *zoom: expression( this.runtimeStyle['zoom'] = '1', this.innerHTML = '&#xf080;&nbsp;');
}
.icon-twitter-sign {
  *zoom: expression( this.runtimeStyle['zoom'] = '1', this.innerHTML = '&#xf081;&nbsp;');
}
.icon-facebook-sign {
  *zoom: expression( this.runtimeStyle['zoom'] = '1', this.innerHTML = '&#xf082;&nbsp;');
}
.icon-camera-retro {
  *zoom: expression( this.runtimeStyle['zoom'] = '1', this.innerHTML = '&#xf083;&nbsp;');
}
.icon-key {
  *zoom: expression( this.runtimeStyle['zoom'] = '1', this.innerHTML = '&#xf084;&nbsp;');
}
.icon-cogs {
  *zoom: expression( this.runtimeStyle['zoom'] = '1', this.innerHTML = '&#xf085;&nbsp;');
}
.icon-comments {
  *zoom: expression( this.runtimeStyle['zoom'] = '1', this.innerHTML = '&#xf086;&nbsp;');
}
.icon-thumbs-up {
  *zoom: expression( this.runtimeStyle['zoom'] = '1', this.innerHTML = '&#xf087;&nbsp;');
}
.icon-thumbs-down {
  *zoom: expression( this.runtimeStyle['zoom'] = '1', this.innerHTML = '&#xf088;&nbsp;');
}
.icon-star-half {
  *zoom: expression( this.runtimeStyle['zoom'] = '1', this.innerHTML = '&#xf089;&nbsp;');
}
.icon-heart-empty {
  *zoom: expression( this.runtimeStyle['zoom'] = '1', this.innerHTML = '&#xf08a;&nbsp;');
}
.icon-signout {
  *zoom: expression( this.runtimeStyle['zoom'] = '1', this.innerHTML = '&#xf08b;&nbsp;');
}
.icon-linkedin-sign {
  *zoom: expression( this.runtimeStyle['zoom'] = '1', this.innerHTML = '&#xf08c;&nbsp;');
}
.icon-pushpin {
  *zoom: expression( this.runtimeStyle['zoom'] = '1', this.innerHTML = '&#xf08d;&nbsp;');
}
.icon-external-link {
  *zoom: expression( this.runtimeStyle['zoom'] = '1', this.innerHTML = '&#xf08e;&nbsp;');
}
.icon-signin {
  *zoom: expression( this.runtimeStyle['zoom'] = '1', this.innerHTML = '&#xf090;&nbsp;');
}
.icon-trophy {
  *zoom: expression( this.runtimeStyle['zoom'] = '1', this.innerHTML = '&#xf091;&nbsp;');
}
.icon-github-sign {
  *zoom: expression( this.runtimeStyle['zoom'] = '1', this.innerHTML = '&#xf092;&nbsp;');
}
.icon-upload-alt {
  *zoom: expression( this.runtimeStyle['zoom'] = '1', this.innerHTML = '&#xf093;&nbsp;');
}
.icon-lemon {
  *zoom: expression( this.runtimeStyle['zoom'] = '1', this.innerHTML = '&#xf094;&nbsp;');
}
.icon-phone {
  *zoom: expression( this.runtimeStyle['zoom'] = '1', this.innerHTML = '&#xf095;&nbsp;');
}
.icon-check-empty {
  *zoom: expression( this.runtimeStyle['zoom'] = '1', this.innerHTML = '&#xf096;&nbsp;');
}
.icon-bookmark-empty {
  *zoom: expression( this.runtimeStyle['zoom'] = '1', this.innerHTML = '&#xf097;&nbsp;');
}
.icon-phone-sign {
  *zoom: expression( this.runtimeStyle['zoom'] = '1', this.innerHTML = '&#xf098;&nbsp;');
}
.icon-twitter {
  *zoom: expression( this.runtimeStyle['zoom'] = '1', this.innerHTML = '&#xf099;&nbsp;');
}
.icon-facebook {
  *zoom: expression( this.runtimeStyle['zoom'] = '1', this.innerHTML = '&#xf09a;&nbsp;');
}
.icon-github {
  *zoom: expression( this.runtimeStyle['zoom'] = '1', this.innerHTML = '&#xf09b;&nbsp;');
}
.icon-unlock {
  *zoom: expression( this.runtimeStyle['zoom'] = '1', this.innerHTML = '&#xf09c;&nbsp;');
}
.icon-credit-card {
  *zoom: expression( this.runtimeStyle['zoom'] = '1', this.innerHTML = '&#xf09d;&nbsp;');
}
.icon-rss {
  *zoom: expression( this.runtimeStyle['zoom'] = '1', this.innerHTML = '&#xf09e;&nbsp;');
}
.icon-hdd {
  *zoom: expression( this.runtimeStyle['zoom'] = '1', this.innerHTML = '&#xf0a0;&nbsp;');
}
.icon-bullhorn {
  *zoom: expression( this.runtimeStyle['zoom'] = '1', this.innerHTML = '&#xf0a1;&nbsp;');
}
.icon-bell {
  *zoom: expression( this.runtimeStyle['zoom'] = '1', this.innerHTML = '&#xf0a2;&nbsp;');
}
.icon-certificate {
  *zoom: expression( this.runtimeStyle['zoom'] = '1', this.innerHTML = '&#xf0a3;&nbsp;');
}
.icon-hand-right {
  *zoom: expression( this.runtimeStyle['zoom'] = '1', this.innerHTML = '&#xf0a4;&nbsp;');
}
.icon-hand-left {
  *zoom: expression( this.runtimeStyle['zoom'] = '1', this.innerHTML = '&#xf0a5;&nbsp;');
}
.icon-hand-up {
  *zoom: expression( this.runtimeStyle['zoom'] = '1', this.innerHTML = '&#xf0a6;&nbsp;');
}
.icon-hand-down {
  *zoom: expression( this.runtimeStyle['zoom'] = '1', this.innerHTML = '&#xf0a7;&nbsp;');
}
.icon-circle-arrow-left {
  *zoom: expression( this.runtimeStyle['zoom'] = '1', this.innerHTML = '&#xf0a8;&nbsp;');
}
.icon-circle-arrow-right {
  *zoom: expression( this.runtimeStyle['zoom'] = '1', this.innerHTML = '&#xf0a9;&nbsp;');
}
.icon-circle-arrow-up {
  *zoom: expression( this.runtimeStyle['zoom'] = '1', this.innerHTML = '&#xf0aa;&nbsp;');
}
.icon-circle-arrow-down {
  *zoom: expression( this.runtimeStyle['zoom'] = '1', this.innerHTML = '&#xf0ab;&nbsp;');
}
.icon-globe {
  *zoom: expression( this.runtimeStyle['zoom'] = '1', this.innerHTML = '&#xf0ac;&nbsp;');
}
.icon-wrench {
  *zoom: expression( this.runtimeStyle['zoom'] = '1', this.innerHTML = '&#xf0ad;&nbsp;');
}
.icon-tasks {
  *zoom: expression( this.runtimeStyle['zoom'] = '1', this.innerHTML = '&#xf0ae;&nbsp;');
}
.icon-filter {
  *zoom: expression( this.runtimeStyle['zoom'] = '1', this.innerHTML = '&#xf0b0;&nbsp;');
}
.icon-briefcase {
  *zoom: expression( this.runtimeStyle['zoom'] = '1', this.innerHTML = '&#xf0b1;&nbsp;');
}
.icon-fullscreen {
  *zoom: expression( this.runtimeStyle['zoom'] = '1', this.innerHTML = '&#xf0b2;&nbsp;');
}
.icon-group {
  *zoom: expression( this.runtimeStyle['zoom'] = '1', this.innerHTML = '&#xf0c0;&nbsp;');
}
.icon-link {
  *zoom: expression( this.runtimeStyle['zoom'] = '1', this.innerHTML = '&#xf0c1;&nbsp;');
}
.icon-cloud {
  *zoom: expression( this.runtimeStyle['zoom'] = '1', this.innerHTML = '&#xf0c2;&nbsp;');
}
.icon-beaker {
  *zoom: expression( this.runtimeStyle['zoom'] = '1', this.innerHTML = '&#xf0c3;&nbsp;');
}
.icon-cut {
  *zoom: expression( this.runtimeStyle['zoom'] = '1', this.innerHTML = '&#xf0c4;&nbsp;');
}
.icon-copy {
  *zoom: expression( this.runtimeStyle['zoom'] = '1', this.innerHTML = '&#xf0c5;&nbsp;');
}
.icon-paper-clip {
  *zoom: expression( this.runtimeStyle['zoom'] = '1', this.innerHTML = '&#xf0c6;&nbsp;');
}
.icon-save {
  *zoom: expression( this.runtimeStyle['zoom'] = '1', this.innerHTML = '&#xf0c7;&nbsp;');
}
.icon-sign-blank {
  *zoom: expression( this.runtimeStyle['zoom'] = '1', this.innerHTML = '&#xf0c8;&nbsp;');
}
.icon-reorder {
  *zoom: expression( this.runtimeStyle['zoom'] = '1', this.innerHTML = '&#xf0c9;&nbsp;');
}
.icon-list-ul {
  *zoom: expression( this.runtimeStyle['zoom'] = '1', this.innerHTML = '&#xf0ca;&nbsp;');
}
.icon-list-ol {
  *zoom: expression( this.runtimeStyle['zoom'] = '1', this.innerHTML = '&#xf0cb;&nbsp;');
}
.icon-strikethrough {
  *zoom: expression( this.runtimeStyle['zoom'] = '1', this.innerHTML = '&#xf0cc;&nbsp;');
}
.icon-underline {
  *zoom: expression( this.runtimeStyle['zoom'] = '1', this.innerHTML = '&#xf0cd;&nbsp;');
}
.icon-table {
  *zoom: expression( this.runtimeStyle['zoom'] = '1', this.innerHTML = '&#xf0ce;&nbsp;');
}
.icon-magic {
  *zoom: expression( this.runtimeStyle['zoom'] = '1', this.innerHTML = '&#xf0d0;&nbsp;');
}
.icon-truck {
  *zoom: expression( this.runtimeStyle['zoom'] = '1', this.innerHTML = '&#xf0d1;&nbsp;');
}
.icon-pinterest {
  *zoom: expression( this.runtimeStyle['zoom'] = '1', this.innerHTML = '&#xf0d2;&nbsp;');
}
.icon-pinterest-sign {
  *zoom: expression( this.runtimeStyle['zoom'] = '1', this.innerHTML = '&#xf0d3;&nbsp;');
}
.icon-google-plus-sign {
  *zoom: expression( this.runtimeStyle['zoom'] = '1', this.innerHTML = '&#xf0d4;&nbsp;');
}
.icon-google-plus {
  *zoom: expression( this.runtimeStyle['zoom'] = '1', this.innerHTML = '&#xf0d5;&nbsp;');
}
.icon-money {
  *zoom: expression( this.runtimeStyle['zoom'] = '1', this.innerHTML = '&#xf0d6;&nbsp;');
}
.icon-caret-down {
  *zoom: expression( this.runtimeStyle['zoom'] = '1', this.innerHTML = '&#xf0d7;&nbsp;');
}
.icon-caret-up {
  *zoom: expression( this.runtimeStyle['zoom'] = '1', this.innerHTML = '&#xf0d8;&nbsp;');
}
.icon-caret-left {
  *zoom: expression( this.runtimeStyle['zoom'] = '1', this.innerHTML = '&#xf0d9;&nbsp;');
}
.icon-caret-right {
  *zoom: expression( this.runtimeStyle['zoom'] = '1', this.innerHTML = '&#xf0da;&nbsp;');
}
.icon-columns {
  *zoom: expression( this.runtimeStyle['zoom'] = '1', this.innerHTML = '&#xf0db;&nbsp;');
}
.icon-sort {
  *zoom: expression( this.runtimeStyle['zoom'] = '1', this.innerHTML = '&#xf0dc;&nbsp;');
}
.icon-sort-down {
  *zoom: expression( this.runtimeStyle['zoom'] = '1', this.innerHTML = '&#xf0dd;&nbsp;');
}
.icon-sort-up {
  *zoom: expression( this.runtimeStyle['zoom'] = '1', this.innerHTML = '&#xf0de;&nbsp;');
}
.icon-envelope-alt {
  *zoom: expression( this.runtimeStyle['zoom'] = '1', this.innerHTML = '&#xf0e0;&nbsp;');
}
.icon-linkedin {
  *zoom: expression( this.runtimeStyle['zoom'] = '1', this.innerHTML = '&#xf0e1;&nbsp;');
}
.icon-undo {
  *zoom: expression( this.runtimeStyle['zoom'] = '1', this.innerHTML = '&#xf0e2;&nbsp;');
}
.icon-legal {
  *zoom: expression( this.runtimeStyle['zoom'] = '1', this.innerHTML = '&#xf0e3;&nbsp;');
}
.icon-dashboard {
  *zoom: expression( this.runtimeStyle['zoom'] = '1', this.innerHTML = '&#xf0e4;&nbsp;');
}
.icon-comment-alt {
  *zoom: expression( this.runtimeStyle['zoom'] = '1', this.innerHTML = '&#xf0e5;&nbsp;');
}
.icon-comments-alt {
  *zoom: expression( this.runtimeStyle['zoom'] = '1', this.innerHTML = '&#xf0e6;&nbsp;');
}
.icon-bolt {
  *zoom: expression( this.runtimeStyle['zoom'] = '1', this.innerHTML = '&#xf0e7;&nbsp;');
}
.icon-sitemap {
  *zoom: expression( this.runtimeStyle['zoom'] = '1', this.innerHTML = '&#xf0e8;&nbsp;');
}
.icon-umbrella {
  *zoom: expression( this.runtimeStyle['zoom'] = '1', this.innerHTML = '&#xf0e9;&nbsp;');
}
.icon-paste {
  *zoom: expression( this.runtimeStyle['zoom'] = '1', this.innerHTML = '&#xf0ea;&nbsp;');
}
.icon-user-md {
  *zoom: expression( this.runtimeStyle['zoom'] = '1', this.innerHTML = '&#xf200;&nbsp;');
}


File: /lib\font-awesome\css\font-awesome.css
/*  Font Awesome
    the iconic font designed for use with Twitter Bootstrap
    -------------------------------------------------------
    The full suite of pictographic icons, examples, and documentation
    can be found at: http://fortawesome.github.com/Font-Awesome/

    License
    -------------------------------------------------------
    The Font Awesome webfont, CSS, and LESS files are licensed under CC BY 3.0:
    http://creativecommons.org/licenses/by/3.0/ A mention of
    'Font Awesome - http://fortawesome.github.com/Font-Awesome' in human-readable
    source code is considered acceptable attribution (most common on the web).
    If human readable source code is not available to the end user, a mention in
    an 'About' or 'Credits' screen is considered acceptable (most common in desktop
    or mobile software).

    Contact
    -------------------------------------------------------
    Email: dave@davegandy.com
    Twitter: http://twitter.com/fortaweso_me
    Work: http://lemonwi.se co-founder

    */
@font-face {
  font-family: "FontAwesome";
  src: url('../font/fontawesome-webfont.eot');
  src: url('../font/fontawesome-webfont.eot?#iefix') format('eot'), url('../font/fontawesome-webfont.woff') format('woff'), url('../font/fontawesome-webfont.ttf') format('truetype'), url('../font/fontawesome-webfont.svg#FontAwesome') format('svg');
  font-weight: normal;
  font-style: normal;
}

/*  Font Awesome styles
    ------------------------------------------------------- */
[class^="icon-"]:before, [class*=" icon-"]:before {
  font-family: FontAwesome;
  font-weight: normal;
  font-style: normal;
  display: inline-block;
  text-decoration: inherit;
}
a [class^="icon-"], a [class*=" icon-"] {
  display: inline-block;
  text-decoration: inherit;
}
/* makes the font 33% larger relative to the icon container */
.icon-large:before {
  vertical-align: top;
  font-size: 1.3333333333333333em;
}
.btn [class^="icon-"], .btn [class*=" icon-"] {
  /* keeps button heights with and without icons the same */

  line-height: .9em;
}
li [class^="icon-"], li [class*=" icon-"] {
  display: inline-block;
  width: 1.25em;
  text-align: center;
}
li .icon-large[class^="icon-"], li .icon-large[class*=" icon-"] {
  /* 1.5 increased font size for icon-large * 1.25 width */

  width: 1.875em;
}
li[class^="icon-"], li[class*=" icon-"] {
  margin-left: 0;
  list-style-type: none;
}
li[class^="icon-"]:before, li[class*=" icon-"]:before {
  text-indent: -2em;
  text-align: center;
}
li[class^="icon-"].icon-large:before, li[class*=" icon-"].icon-large:before {
  text-indent: -1.3333333333333333em;
}
/*  Font Awesome uses the Unicode Private Use Area (PUA) to ensure screen
    readers do not read off random characters that represent icons */
.icon-glass:before                { content: "\f000"; }
.icon-music:before                { content: "\f001"; }
.icon-search:before               { content: "\f002"; }
.icon-envelope:before             { content: "\f003"; }
.icon-heart:before                { content: "\f004"; }
.icon-star:before                 { content: "\f005"; }
.icon-star-empty:before           { content: "\f006"; }
.icon-user:before                 { content: "\f007"; }
.icon-film:before                 { content: "\f008"; }
.icon-th-large:before             { content: "\f009"; }
.icon-th:before                   { content: "\f00a"; }
.icon-th-list:before              { content: "\f00b"; }
.icon-ok:before                   { content: "\f00c"; }
.icon-remove:before               { content: "\f00d"; }
.icon-zoom-in:before              { content: "\f00e"; }

.icon-zoom-out:before             { content: "\f010"; }
.icon-off:before                  { content: "\f011"; }
.icon-signal:before               { content: "\f012"; }
.icon-cog:before                  { content: "\f013"; }
.icon-trash:before                { content: "\f014"; }
.icon-home:before                 { content: "\f015"; }
.icon-file:before                 { content: "\f016"; }
.icon-time:before                 { content: "\f017"; }
.icon-road:before                 { content: "\f018"; }
.icon-download-alt:before         { content: "\f019"; }
.icon-download:before             { content: "\f01a"; }
.icon-upload:before               { content: "\f01b"; }
.icon-inbox:before                { content: "\f01c"; }
.icon-play-circle:before          { content: "\f01d"; }
.icon-repeat:before               { content: "\f01e"; }

/* \f020 doesn't work in Safari. all shifted one down */
.icon-refresh:before              { content: "\f021"; }
.icon-list-alt:before             { content: "\f022"; }
.icon-lock:before                 { content: "\f023"; }
.icon-flag:before                 { content: "\f024"; }
.icon-headphones:before           { content: "\f025"; }
.icon-volume-off:before           { content: "\f026"; }
.icon-volume-down:before          { content: "\f027"; }
.icon-volume-up:before            { content: "\f028"; }
.icon-qrcode:before               { content: "\f029"; }
.icon-barcode:before              { content: "\f02a"; }
.icon-tag:before                  { content: "\f02b"; }
.icon-tags:before                 { content: "\f02c"; }
.icon-book:before                 { content: "\f02d"; }
.icon-bookmark:before             { content: "\f02e"; }
.icon-print:before                { content: "\f02f"; }

.icon-camera:before               { content: "\f030"; }
.icon-font:before                 { content: "\f031"; }
.icon-bold:before                 { content: "\f032"; }
.icon-italic:before               { content: "\f033"; }
.icon-text-height:before          { content: "\f034"; }
.icon-text-width:before           { content: "\f035"; }
.icon-align-left:before           { content: "\f036"; }
.icon-align-center:before         { content: "\f037"; }
.icon-align-right:before          { content: "\f038"; }
.icon-align-justify:before        { content: "\f039"; }
.icon-list:before                 { content: "\f03a"; }
.icon-indent-left:before          { content: "\f03b"; }
.icon-indent-right:before         { content: "\f03c"; }
.icon-facetime-video:before       { content: "\f03d"; }
.icon-picture:before              { content: "\f03e"; }

.icon-pencil:before               { content: "\f040"; }
.icon-map-marker:before           { content: "\f041"; }
.icon-adjust:before               { content: "\f042"; }
.icon-tint:before                 { content: "\f043"; }
.icon-edit:before                 { content: "\f044"; }
.icon-share:before                { content: "\f045"; }
.icon-check:before                { content: "\f046"; }
.icon-move:before                 { content: "\f047"; }
.icon-step-backward:before        { content: "\f048"; }
.icon-fast-backward:before        { content: "\f049"; }
.icon-backward:before             { content: "\f04a"; }
.icon-play:before                 { content: "\f04b"; }
.icon-pause:before                { content: "\f04c"; }
.icon-stop:before                 { content: "\f04d"; }
.icon-forward:before              { content: "\f04e"; }

.icon-fast-forward:before         { content: "\f050"; }
.icon-step-forward:before         { content: "\f051"; }
.icon-eject:before                { content: "\f052"; }
.icon-chevron-left:before         { content: "\f053"; }
.icon-chevron-right:before        { content: "\f054"; }
.icon-plus-sign:before            { content: "\f055"; }
.icon-minus-sign:before           { content: "\f056"; }
.icon-remove-sign:before          { content: "\f057"; }
.icon-ok-sign:before              { content: "\f058"; }
.icon-question-sign:before        { content: "\f059"; }
.icon-info-sign:before            { content: "\f05a"; }
.icon-screenshot:before           { content: "\f05b"; }
.icon-remove-circle:before        { content: "\f05c"; }
.icon-ok-circle:before            { content: "\f05d"; }
.icon-ban-circle:before           { content: "\f05e"; }

.icon-arrow-left:before           { content: "\f060"; }
.icon-arrow-right:before          { content: "\f061"; }
.icon-arrow-up:before             { content: "\f062"; }
.icon-arrow-down:before           { content: "\f063"; }
.icon-share-alt:before            { content: "\f064"; }
.icon-resize-full:before          { content: "\f065"; }
.icon-resize-small:before         { content: "\f066"; }
.icon-plus:before                 { content: "\f067"; }
.icon-minus:before                { content: "\f068"; }
.icon-asterisk:before             { content: "\f069"; }
.icon-exclamation-sign:before     { content: "\f06a"; }
.icon-gift:before                 { content: "\f06b"; }
.icon-leaf:before                 { content: "\f06c"; }
.icon-fire:before                 { content: "\f06d"; }
.icon-eye-open:before             { content: "\f06e"; }

.icon-eye-close:before            { content: "\f070"; }
.icon-warning-sign:before         { content: "\f071"; }
.icon-plane:before                { content: "\f072"; }
.icon-calendar:before             { content: "\f073"; }
.icon-random:before               { content: "\f074"; }
.icon-comment:before              { content: "\f075"; }
.icon-magnet:before               { content: "\f076"; }
.icon-chevron-up:before           { content: "\f077"; }
.icon-chevron-down:before         { content: "\f078"; }
.icon-retweet:before              { content: "\f079"; }
.icon-shopping-cart:before        { content: "\f07a"; }
.icon-folder-close:before         { content: "\f07b"; }
.icon-folder-open:before          { content: "\f07c"; }
.icon-resize-vertical:before      { content: "\f07d"; }
.icon-resize-horizontal:before    { content: "\f07e"; }

.icon-bar-chart:before            { content: "\f080"; }
.icon-twitter-sign:before         { content: "\f081"; }
.icon-facebook-sign:before        { content: "\f082"; }
.icon-camera-retro:before         { content: "\f083"; }
.icon-key:before                  { content: "\f084"; }
.icon-cogs:before                 { content: "\f085"; }
.icon-comments:before             { content: "\f086"; }
.icon-thumbs-up:before            { content: "\f087"; }
.icon-thumbs-down:before          { content: "\f088"; }
.icon-star-half:before            { content: "\f089"; }
.icon-heart-empty:before          { content: "\f08a"; }
.icon-signout:before              { content: "\f08b"; }
.icon-linkedin-sign:before        { content: "\f08c"; }
.icon-pushpin:before              { content: "\f08d"; }
.icon-external-link:before        { content: "\f08e"; }

.icon-signin:before               { content: "\f090"; }
.icon-trophy:before               { content: "\f091"; }
.icon-github-sign:before          { content: "\f092"; }
.icon-upload-alt:before           { content: "\f093"; }
.icon-lemon:before                { content: "\f094"; }
.icon-phone:before                { content: "\f095"; }
.icon-check-empty:before          { content: "\f096"; }
.icon-bookmark-empty:before       { content: "\f097"; }
.icon-phone-sign:before           { content: "\f098"; }
.icon-twitter:before              { content: "\f099"; }
.icon-facebook:before             { content: "\f09a"; }
.icon-github:before               { content: "\f09b"; }
.icon-unlock:before               { content: "\f09c"; }
.icon-credit-card:before          { content: "\f09d"; }
.icon-rss:before                  { content: "\f09e"; }

.icon-hdd:before                  { content: "\f0a0"; }
.icon-bullhorn:before             { content: "\f0a1"; }
.icon-bell:before                 { content: "\f0a2"; }
.icon-certificate:before          { content: "\f0a3"; }
.icon-hand-right:before           { content: "\f0a4"; }
.icon-hand-left:before            { content: "\f0a5"; }
.icon-hand-up:before              { content: "\f0a6"; }
.icon-hand-down:before            { content: "\f0a7"; }
.icon-circle-arrow-left:before    { content: "\f0a8"; }
.icon-circle-arrow-right:before   { content: "\f0a9"; }
.icon-circle-arrow-up:before      { content: "\f0aa"; }
.icon-circle-arrow-down:before    { content: "\f0ab"; }
.icon-globe:before                { content: "\f0ac"; }
.icon-wrench:before               { content: "\f0ad"; }
.icon-tasks:before                { content: "\f0ae"; }

.icon-filter:before               { content: "\f0b0"; }
.icon-briefcase:before            { content: "\f0b1"; }
.icon-fullscreen:before           { content: "\f0b2"; }

.icon-group:before                { content: "\f0c0"; }
.icon-link:before                 { content: "\f0c1"; }
.icon-cloud:before                { content: "\f0c2"; }
.icon-beaker:before               { content: "\f0c3"; }
.icon-cut:before                  { content: "\f0c4"; }
.icon-copy:before                 { content: "\f0c5"; }
.icon-paper-clip:before           { content: "\f0c6"; }
.icon-save:before                 { content: "\f0c7"; }
.icon-sign-blank:before           { content: "\f0c8"; }
.icon-reorder:before              { content: "\f0c9"; }
.icon-list-ul:before              { content: "\f0ca"; }
.icon-list-ol:before              { content: "\f0cb"; }
.icon-strikethrough:before        { content: "\f0cc"; }
.icon-underline:before            { content: "\f0cd"; }
.icon-table:before                { content: "\f0ce"; }

.icon-magic:before                { content: "\f0d0"; }
.icon-truck:before                { content: "\f0d1"; }
.icon-pinterest:before            { content: "\f0d2"; }
.icon-pinterest-sign:before       { content: "\f0d3"; }
.icon-google-plus-sign:before     { content: "\f0d4"; }
.icon-google-plus:before          { content: "\f0d5"; }
.icon-money:before                { content: "\f0d6"; }
.icon-caret-down:before           { content: "\f0d7"; }
.icon-caret-up:before             { content: "\f0d8"; }
.icon-caret-left:before           { content: "\f0d9"; }
.icon-caret-right:before          { content: "\f0da"; }
.icon-columns:before              { content: "\f0db"; }
.icon-sort:before                 { content: "\f0dc"; }
.icon-sort-down:before            { content: "\f0dd"; }
.icon-sort-up:before              { content: "\f0de"; }

.icon-envelope-alt:before         { content: "\f0e0"; }
.icon-linkedin:before             { content: "\f0e1"; }
.icon-undo:before                 { content: "\f0e2"; }
.icon-legal:before                { content: "\f0e3"; }
.icon-dashboard:before            { content: "\f0e4"; }
.icon-comment-alt:before          { content: "\f0e5"; }
.icon-comments-alt:before         { content: "\f0e6"; }
.icon-bolt:before                 { content: "\f0e7"; }
.icon-sitemap:before              { content: "\f0e8"; }
.icon-umbrella:before             { content: "\f0e9"; }
.icon-paste:before                { content: "\f0ea"; }

.icon-user-md:before              { content: "\f200"; }


File: /lib\font-awesome\less\font-awesome-ie7.less
[class^="icon-"],
[class*=" icon-"] {
	font-family: FontAwesome;
	font-style: normal;
	font-weight: normal;
}

.btn.dropdown-toggle [class^="icon-"], .btn.dropdown-toggle [class*=" icon-"] {
/* keeps button heights with and without icons the same */
	line-height: 1.4em;
}

.icon-large {
	font-size: 1.3333em;
}

.ie7icon(@inner) {
	*zoom: ~"expression( this.runtimeStyle['zoom'] = '1', this.innerHTML = '@{inner}&nbsp;')";
}

.icon-glass                { .ie7icon('&#xf000;'); }
.icon-music                { .ie7icon('&#xf001;'); }
.icon-search               { .ie7icon('&#xf002;'); }
.icon-envelope             { .ie7icon('&#xf003;'); }
.icon-heart                { .ie7icon('&#xf004;'); }
.icon-star                 { .ie7icon('&#xf005;'); }
.icon-star-empty           { .ie7icon('&#xf006;'); }
.icon-user                 { .ie7icon('&#xf007;'); }
.icon-film                 { .ie7icon('&#xf008;'); }
.icon-th-large             { .ie7icon('&#xf009;'); }
.icon-th                   { .ie7icon('&#xf00a;'); }
.icon-th-list              { .ie7icon('&#xf00b;'); }
.icon-ok                   { .ie7icon('&#xf00c;'); }
.icon-remove               { .ie7icon('&#xf00d;'); }
.icon-zoom-in              { .ie7icon('&#xf00e;'); }

.icon-zoom-out             { .ie7icon('&#xf010;'); }
.icon-off                  { .ie7icon('&#xf011;'); }
.icon-signal               { .ie7icon('&#xf012;'); }
.icon-cog                  { .ie7icon('&#xf013;'); }
.icon-trash                { .ie7icon('&#xf014;'); }
.icon-home                 { .ie7icon('&#xf015;'); }
.icon-file                 { .ie7icon('&#xf016;'); }
.icon-time                 { .ie7icon('&#xf017;'); }
.icon-road                 { .ie7icon('&#xf018;'); }
.icon-download-alt         { .ie7icon('&#xf019;'); }
.icon-download             { .ie7icon('&#xf01a;'); }
.icon-upload               { .ie7icon('&#xf01b;'); }
.icon-inbox                { .ie7icon('&#xf01c;'); }
.icon-play-circle          { .ie7icon('&#xf01d;'); }
.icon-repeat               { .ie7icon('&#xf01e;'); }

.icon-refresh              { .ie7icon('&#xf021;'); }
.icon-list-alt             { .ie7icon('&#xf022;'); }
.icon-lock                 { .ie7icon('&#xf023;'); }
.icon-flag                 { .ie7icon('&#xf024;'); }
.icon-headphones           { .ie7icon('&#xf025;'); }
.icon-volume-off           { .ie7icon('&#xf026;'); }
.icon-volume-down          { .ie7icon('&#xf027;'); }
.icon-volume-up            { .ie7icon('&#xf028;'); }
.icon-qrcode               { .ie7icon('&#xf029;'); }
.icon-barcode              { .ie7icon('&#xf02a;'); }
.icon-tag                  { .ie7icon('&#xf02b;'); }
.icon-tags                 { .ie7icon('&#xf02c;'); }
.icon-book                 { .ie7icon('&#xf02d;'); }
.icon-bookmark             { .ie7icon('&#xf02e;'); }
.icon-print                { .ie7icon('&#xf02f;'); }

.icon-camera               { .ie7icon('&#xf030;'); }
.icon-font                 { .ie7icon('&#xf031;'); }
.icon-bold                 { .ie7icon('&#xf032;'); }
.icon-italic               { .ie7icon('&#xf033;'); }
.icon-text-height          { .ie7icon('&#xf034;'); }
.icon-text-width           { .ie7icon('&#xf035;'); }
.icon-align-left           { .ie7icon('&#xf036;'); }
.icon-align-center         { .ie7icon('&#xf037;'); }
.icon-align-right          { .ie7icon('&#xf038;'); }
.icon-align-justify        { .ie7icon('&#xf039;'); }
.icon-list                 { .ie7icon('&#xf03a;'); }
.icon-indent-left          { .ie7icon('&#xf03b;'); }
.icon-indent-right         { .ie7icon('&#xf03c;'); }
.icon-facetime-video       { .ie7icon('&#xf03d;'); }
.icon-picture              { .ie7icon('&#xf03e;'); }

.icon-pencil               { .ie7icon('&#xf040;'); }
.icon-map-marker           { .ie7icon('&#xf041;'); }
.icon-adjust               { .ie7icon('&#xf042;'); }
.icon-tint                 { .ie7icon('&#xf043;'); }
.icon-edit                 { .ie7icon('&#xf044;'); }
.icon-share                { .ie7icon('&#xf045;'); }
.icon-check                { .ie7icon('&#xf046;'); }
.icon-move                 { .ie7icon('&#xf047;'); }
.icon-step-backward        { .ie7icon('&#xf048;'); }
.icon-fast-backward        { .ie7icon('&#xf049;'); }
.icon-backward             { .ie7icon('&#xf04a;'); }
.icon-play                 { .ie7icon('&#xf04b;'); }
.icon-pause                { .ie7icon('&#xf04c;'); }
.icon-stop                 { .ie7icon('&#xf04d;'); }
.icon-forward              { .ie7icon('&#xf04e;'); }

.icon-fast-forward         { .ie7icon('&#xf050;'); }
.icon-step-forward         { .ie7icon('&#xf051;'); }
.icon-eject                { .ie7icon('&#xf052;'); }
.icon-chevron-left         { .ie7icon('&#xf053;'); }
.icon-chevron-right        { .ie7icon('&#xf054;'); }
.icon-plus-sign            { .ie7icon('&#xf055;'); }
.icon-minus-sign           { .ie7icon('&#xf056;'); }
.icon-remove-sign          { .ie7icon('&#xf057;'); }
.icon-ok-sign              { .ie7icon('&#xf058;'); }
.icon-question-sign        { .ie7icon('&#xf059;'); }
.icon-info-sign            { .ie7icon('&#xf05a;'); }
.icon-screenshot           { .ie7icon('&#xf05b;'); }
.icon-remove-circle        { .ie7icon('&#xf05c;'); }
.icon-ok-circle            { .ie7icon('&#xf05d;'); }
.icon-ban-circle           { .ie7icon('&#xf05e;'); }

.icon-arrow-left           { .ie7icon('&#xf060;'); }
.icon-arrow-right          { .ie7icon('&#xf061;'); }
.icon-arrow-up             { .ie7icon('&#xf062;'); }
.icon-arrow-down           { .ie7icon('&#xf063;'); }
.icon-share-alt            { .ie7icon('&#xf064;'); }
.icon-resize-full          { .ie7icon('&#xf065;'); }
.icon-resize-small         { .ie7icon('&#xf066;'); }
.icon-plus                 { .ie7icon('&#xf067;'); }
.icon-minus                { .ie7icon('&#xf068;'); }
.icon-asterisk             { .ie7icon('&#xf069;'); }
.icon-exclamation-sign     { .ie7icon('&#xf06a;'); }
.icon-gift                 { .ie7icon('&#xf06b;'); }
.icon-leaf                 { .ie7icon('&#xf06c;'); }
.icon-fire                 { .ie7icon('&#xf06d;'); }
.icon-eye-open             { .ie7icon('&#xf06e;'); }

.icon-eye-close            { .ie7icon('&#xf070;'); }
.icon-warning-sign         { .ie7icon('&#xf071;'); }
.icon-plane                { .ie7icon('&#xf072;'); }
.icon-calendar             { .ie7icon('&#xf073;'); }
.icon-random               { .ie7icon('&#xf074;'); }
.icon-comment              { .ie7icon('&#xf075;'); }
.icon-magnet               { .ie7icon('&#xf076;'); }
.icon-chevron-up           { .ie7icon('&#xf077;'); }
.icon-chevron-down         { .ie7icon('&#xf078;'); }
.icon-retweet              { .ie7icon('&#xf079;'); }
.icon-shopping-cart        { .ie7icon('&#xf07a;'); }
.icon-folder-close         { .ie7icon('&#xf07b;'); }
.icon-folder-open          { .ie7icon('&#xf07c;'); }
.icon-resize-vertical      { .ie7icon('&#xf07d;'); }
.icon-resize-horizontal    { .ie7icon('&#xf07e;'); }

.icon-bar-chart            { .ie7icon('&#xf080;'); }
.icon-twitter-sign         { .ie7icon('&#xf081;'); }
.icon-facebook-sign        { .ie7icon('&#xf082;'); }
.icon-camera-retro         { .ie7icon('&#xf083;'); }
.icon-key                  { .ie7icon('&#xf084;'); }
.icon-cogs                 { .ie7icon('&#xf085;'); }
.icon-comments             { .ie7icon('&#xf086;'); }
.icon-thumbs-up            { .ie7icon('&#xf087;'); }
.icon-thumbs-down          { .ie7icon('&#xf088;'); }
.icon-star-half            { .ie7icon('&#xf089;'); }
.icon-heart-empty          { .ie7icon('&#xf08a;'); }
.icon-signout              { .ie7icon('&#xf08b;'); }
.icon-linkedin-sign        { .ie7icon('&#xf08c;'); }
.icon-pushpin              { .ie7icon('&#xf08d;'); }
.icon-external-link        { .ie7icon('&#xf08e;'); }

.icon-signin               { .ie7icon('&#xf090;'); }
.icon-trophy               { .ie7icon('&#xf091;'); }
.icon-github-sign          { .ie7icon('&#xf092;'); }
.icon-upload-alt           { .ie7icon('&#xf093;'); }
.icon-lemon                { .ie7icon('&#xf094;'); }
.icon-phone                { .ie7icon('&#xf095;'); }
.icon-check-empty          { .ie7icon('&#xf096;'); }
.icon-bookmark-empty       { .ie7icon('&#xf097;'); }
.icon-phone-sign           { .ie7icon('&#xf098;'); }
.icon-twitter              { .ie7icon('&#xf099;'); }
.icon-facebook             { .ie7icon('&#xf09a;'); }
.icon-github               { .ie7icon('&#xf09b;'); }
.icon-unlock               { .ie7icon('&#xf09c;'); }
.icon-credit-card          { .ie7icon('&#xf09d;'); }
.icon-rss                  { .ie7icon('&#xf09e;'); }

.icon-hdd                  { .ie7icon('&#xf0a0;'); }
.icon-bullhorn             { .ie7icon('&#xf0a1;'); }
.icon-bell                 { .ie7icon('&#xf0a2;'); }
.icon-certificate          { .ie7icon('&#xf0a3;'); }
.icon-hand-right           { .ie7icon('&#xf0a4;'); }
.icon-hand-left            { .ie7icon('&#xf0a5;'); }
.icon-hand-up              { .ie7icon('&#xf0a6;'); }
.icon-hand-down            { .ie7icon('&#xf0a7;'); }
.icon-circle-arrow-left    { .ie7icon('&#xf0a8;'); }
.icon-circle-arrow-right   { .ie7icon('&#xf0a9;'); }
.icon-circle-arrow-up      { .ie7icon('&#xf0aa;'); }
.icon-circle-arrow-down    { .ie7icon('&#xf0ab;'); }
.icon-globe                { .ie7icon('&#xf0ac;'); }
.icon-wrench               { .ie7icon('&#xf0ad;'); }
.icon-tasks                { .ie7icon('&#xf0ae;'); }

.icon-filter               { .ie7icon('&#xf0b0;'); }
.icon-briefcase            { .ie7icon('&#xf0b1;'); }
.icon-fullscreen           { .ie7icon('&#xf0b2;'); }

.icon-group                { .ie7icon('&#xf0c0;'); }
.icon-link                 { .ie7icon('&#xf0c1;'); }
.icon-cloud                { .ie7icon('&#xf0c2;'); }
.icon-beaker               { .ie7icon('&#xf0c3;'); }
.icon-cut                  { .ie7icon('&#xf0c4;'); }
.icon-copy                 { .ie7icon('&#xf0c5;'); }
.icon-paper-clip           { .ie7icon('&#xf0c6;'); }
.icon-save                 { .ie7icon('&#xf0c7;'); }
.icon-sign-blank           { .ie7icon('&#xf0c8;'); }
.icon-reorder              { .ie7icon('&#xf0c9;'); }
.icon-list-ul              { .ie7icon('&#xf0ca;'); }
.icon-list-ol              { .ie7icon('&#xf0cb;'); }
.icon-strikethrough        { .ie7icon('&#xf0cc;'); }
.icon-underline            { .ie7icon('&#xf0cd;'); }
.icon-table                { .ie7icon('&#xf0ce;'); }

.icon-magic                { .ie7icon('&#xf0d0;'); }
.icon-truck                { .ie7icon('&#xf0d1;'); }
.icon-pinterest            { .ie7icon('&#xf0d2;'); }
.icon-pinterest-sign       { .ie7icon('&#xf0d3;'); }
.icon-google-plus-sign     { .ie7icon('&#xf0d4;'); }
.icon-google-plus          { .ie7icon('&#xf0d5;'); }
.icon-money                { .ie7icon('&#xf0d6;'); }
.icon-caret-down           { .ie7icon('&#xf0d7;'); }
.icon-caret-up             { .ie7icon('&#xf0d8;'); }
.icon-caret-left           { .ie7icon('&#xf0d9;'); }
.icon-caret-right          { .ie7icon('&#xf0da;'); }
.icon-columns              { .ie7icon('&#xf0db;'); }
.icon-sort                 { .ie7icon('&#xf0dc;'); }
.icon-sort-down            { .ie7icon('&#xf0dd;'); }
.icon-sort-up              { .ie7icon('&#xf0de;'); }

.icon-envelope-alt         { .ie7icon('&#xf0e0;'); }
.icon-linkedin             { .ie7icon('&#xf0e1;'); }
.icon-undo                 { .ie7icon('&#xf0e2;'); }
.icon-legal                { .ie7icon('&#xf0e3;'); }
.icon-dashboard            { .ie7icon('&#xf0e4;'); }
.icon-comment-alt          { .ie7icon('&#xf0e5;'); }
.icon-comments-alt         { .ie7icon('&#xf0e6;'); }
.icon-bolt                 { .ie7icon('&#xf0e7;'); }
.icon-sitemap              { .ie7icon('&#xf0e8;'); }
.icon-umbrella             { .ie7icon('&#xf0e9;'); }
.icon-paste                { .ie7icon('&#xf0ea;'); }

.icon-user-md              { .ie7icon('&#xf200;'); }


File: /lib\font-awesome\less\font-awesome.less
/*  Font Awesome
    the iconic font designed for use with Twitter Bootstrap
    -------------------------------------------------------
    The full suite of pictographic icons, examples, and documentation
    can be found at: http://fortawesome.github.com/Font-Awesome/

    License
    -------------------------------------------------------
    The Font Awesome webfont, CSS, and LESS files are licensed under CC BY 3.0:
    http://creativecommons.org/licenses/by/3.0/ A mention of
    'Font Awesome - http://fortawesome.github.com/Font-Awesome' in human-readable
    source code is considered acceptable attribution (most common on the web).
    If human readable source code is not available to the end user, a mention in
    an 'About' or 'Credits' screen is considered acceptable (most common in desktop
    or mobile software).

    Contact
    -------------------------------------------------------
    Email: dave@davegandy.com
    Twitter: http://twitter.com/fortaweso_me
    Work: Lead Product Designer @ http://kyruus.com

    */

@fontAwesomePath: '../font';

@font-face {
  font-family: 'FontAwesome';
  src: url('@{fontAwesomePath}/fontawesome-webfont.eot');
  src: url('@{fontAwesomePath}/fontawesome-webfont.eot?#iefix') format('embedded-opentype'),
    url('@{fontAwesomePath}/fontawesome-webfont.woff') format('woff'),
    url('@{fontAwesomePath}/fontawesome-webfont.ttf') format('truetype'),
    url('@{fontAwesomePath}/fontawesome-webfont.svg#FontAwesome') format('svg');
  font-weight: normal;
  font-style: normal;
}

/*  Font Awesome styles
    ------------------------------------------------------- */
[class^="icon-"]:before,
[class*=" icon-"]:before {
  font-family: FontAwesome;
  font-weight: normal;
  font-style: normal;
  display: inline-block;
  text-decoration: inherit;
}

a [class^="icon-"],
a [class*=" icon-"] {
  display: inline-block;
  text-decoration: inherit;
}

/* makes the font 33% larger relative to the icon container */
.icon-large:before {
  vertical-align: middle;
  font-size: 4/3em;
}

.btn, .nav-tabs {
  [class^="icon-"],
  [class*=" icon-"] {
  /* keeps button heights with and without icons the same */
    line-height: .9em;
  }
}

li {
  [class^="icon-"],
  [class*=" icon-"] {
    display: inline-block;
    width: 1.25em;
    text-align: center;
  }
  .icon-large:before,
  .icon-large:before {
    /* 1.5 increased font size for icon-large * 1.25 width */
    width: 1.5*1.25em;
  }
}

ul.icons {
  list-style-type: none;
  margin-left: 2em;
  text-indent: -.8em;

  li {
    [class^="icon-"],
    [class*=" icon-"] {
      width: .8em;
    }
    .icon-large:before,
    .icon-large:before {
      /* 1.5 increased font size for icon-large * 1.25 width */
      vertical-align: initial;
//      width: 1.5*1.25em;
    }
  }
}

/*  Font Awesome uses the Unicode Private Use Area (PUA) to ensure screen
    readers do not read off random characters that represent icons */
.icon-glass:before                { content: "\f000"; }
.icon-music:before                { content: "\f001"; }
.icon-search:before               { content: "\f002"; }
.icon-envelope:before             { content: "\f003"; }
.icon-heart:before                { content: "\f004"; }
.icon-star:before                 { content: "\f005"; }
.icon-star-empty:before           { content: "\f006"; }
.icon-user:before                 { content: "\f007"; }
.icon-film:before                 { content: "\f008"; }
.icon-th-large:before             { content: "\f009"; }
.icon-th:before                   { content: "\f00a"; }
.icon-th-list:before              { content: "\f00b"; }
.icon-ok:before                   { content: "\f00c"; }
.icon-remove:before               { content: "\f00d"; }
.icon-zoom-in:before              { content: "\f00e"; }

.icon-zoom-out:before             { content: "\f010"; }
.icon-off:before                  { content: "\f011"; }
.icon-signal:before               { content: "\f012"; }
.icon-cog:before                  { content: "\f013"; }
.icon-trash:before                { content: "\f014"; }
.icon-home:before                 { content: "\f015"; }
.icon-file:before                 { content: "\f016"; }
.icon-time:before                 { content: "\f017"; }
.icon-road:before                 { content: "\f018"; }
.icon-download-alt:before         { content: "\f019"; }
.icon-download:before             { content: "\f01a"; }
.icon-upload:before               { content: "\f01b"; }
.icon-inbox:before                { content: "\f01c"; }
.icon-play-circle:before          { content: "\f01d"; }
.icon-repeat:before               { content: "\f01e"; }

/* \f020 doesn't work in Safari. all shifted one down */
.icon-refresh:before              { content: "\f021"; }
.icon-list-alt:before             { content: "\f022"; }
.icon-lock:before                 { content: "\f023"; }
.icon-flag:before                 { content: "\f024"; }
.icon-headphones:before           { content: "\f025"; }
.icon-volume-off:before           { content: "\f026"; }
.icon-volume-down:before          { content: "\f027"; }
.icon-volume-up:before            { content: "\f028"; }
.icon-qrcode:before               { content: "\f029"; }
.icon-barcode:before              { content: "\f02a"; }
.icon-tag:before                  { content: "\f02b"; }
.icon-tags:before                 { content: "\f02c"; }
.icon-book:before                 { content: "\f02d"; }
.icon-bookmark:before             { content: "\f02e"; }
.icon-print:before                { content: "\f02f"; }

.icon-camera:before               { content: "\f030"; }
.icon-font:before                 { content: "\f031"; }
.icon-bold:before                 { content: "\f032"; }
.icon-italic:before               { content: "\f033"; }
.icon-text-height:before          { content: "\f034"; }
.icon-text-width:before           { content: "\f035"; }
.icon-align-left:before           { content: "\f036"; }
.icon-align-center:before         { content: "\f037"; }
.icon-align-right:before          { content: "\f038"; }
.icon-align-justify:before        { content: "\f039"; }
.icon-list:before                 { content: "\f03a"; }
.icon-indent-left:before          { content: "\f03b"; }
.icon-indent-right:before         { content: "\f03c"; }
.icon-facetime-video:before       { content: "\f03d"; }
.icon-picture:before              { content: "\f03e"; }

.icon-pencil:before               { content: "\f040"; }
.icon-map-marker:before           { content: "\f041"; }
.icon-adjust:before               { content: "\f042"; }
.icon-tint:before                 { content: "\f043"; }
.icon-edit:before                 { content: "\f044"; }
.icon-share:before                { content: "\f045"; }
.icon-check:before                { content: "\f046"; }
.icon-move:before                 { content: "\f047"; }
.icon-step-backward:before        { content: "\f048"; }
.icon-fast-backward:before        { content: "\f049"; }
.icon-backward:before             { content: "\f04a"; }
.icon-play:before                 { content: "\f04b"; }
.icon-pause:before                { content: "\f04c"; }
.icon-stop:before                 { content: "\f04d"; }
.icon-forward:before              { content: "\f04e"; }

.icon-fast-forward:before         { content: "\f050"; }
.icon-step-forward:before         { content: "\f051"; }
.icon-eject:before                { content: "\f052"; }
.icon-chevron-left:before         { content: "\f053"; }
.icon-chevron-right:before        { content: "\f054"; }
.icon-plus-sign:before            { content: "\f055"; }
.icon-minus-sign:before           { content: "\f056"; }
.icon-remove-sign:before          { content: "\f057"; }
.icon-ok-sign:before              { content: "\f058"; }
.icon-question-sign:before        { content: "\f059"; }
.icon-info-sign:before            { content: "\f05a"; }
.icon-screenshot:before           { content: "\f05b"; }
.icon-remove-circle:before        { content: "\f05c"; }
.icon-ok-circle:before            { content: "\f05d"; }
.icon-ban-circle:before           { content: "\f05e"; }

.icon-arrow-left:before           { content: "\f060"; }
.icon-arrow-right:before          { content: "\f061"; }
.icon-arrow-up:before             { content: "\f062"; }
.icon-arrow-down:before           { content: "\f063"; }
.icon-share-alt:before            { content: "\f064"; }
.icon-resize-full:before          { content: "\f065"; }
.icon-resize-small:before         { content: "\f066"; }
.icon-plus:before                 { content: "\f067"; }
.icon-minus:before                { content: "\f068"; }
.icon-asterisk:before             { content: "\f069"; }
.icon-exclamation-sign:before     { content: "\f06a"; }
.icon-gift:before                 { content: "\f06b"; }
.icon-leaf:before                 { content: "\f06c"; }
.icon-fire:before                 { content: "\f06d"; }
.icon-eye-open:before             { content: "\f06e"; }

.icon-eye-close:before            { content: "\f070"; }
.icon-warning-sign:before         { content: "\f071"; }
.icon-plane:before                { content: "\f072"; }
.icon-calendar:before             { content: "\f073"; }
.icon-random:before               { content: "\f074"; }
.icon-comment:before              { content: "\f075"; }
.icon-magnet:before               { content: "\f076"; }
.icon-chevron-up:before           { content: "\f077"; }
.icon-chevron-down:before         { content: "\f078"; }
.icon-retweet:before              { content: "\f079"; }
.icon-shopping-cart:before        { content: "\f07a"; }
.icon-folder-close:before         { content: "\f07b"; }
.icon-folder-open:before          { content: "\f07c"; }
.icon-resize-vertical:before      { content: "\f07d"; }
.icon-resize-horizontal:before    { content: "\f07e"; }

.icon-bar-chart:before            { content: "\f080"; }
.icon-twitter-sign:before         { content: "\f081"; }
.icon-facebook-sign:before        { content: "\f082"; }
.icon-camera-retro:before         { content: "\f083"; }
.icon-key:before                  { content: "\f084"; }
.icon-cogs:before                 { content: "\f085"; }
.icon-comments:before             { content: "\f086"; }
.icon-thumbs-up:before            { content: "\f087"; }
.icon-thumbs-down:before          { content: "\f088"; }
.icon-star-half:before            { content: "\f089"; }
.icon-heart-empty:before          { content: "\f08a"; }
.icon-signout:before              { content: "\f08b"; }
.icon-linkedin-sign:before        { content: "\f08c"; }
.icon-pushpin:before              { content: "\f08d"; }
.icon-external-link:before        { content: "\f08e"; }

.icon-signin:before               { content: "\f090"; }
.icon-trophy:before               { content: "\f091"; }
.icon-github-sign:before          { content: "\f092"; }
.icon-upload-alt:before           { content: "\f093"; }
.icon-lemon:before                { content: "\f094"; }
.icon-phone:before                { content: "\f095"; }
.icon-check-empty:before          { content: "\f096"; }
.icon-bookmark-empty:before       { content: "\f097"; }
.icon-phone-sign:before           { content: "\f098"; }
.icon-twitter:before              { content: "\f099"; }
.icon-facebook:before             { content: "\f09a"; }
.icon-github:before               { content: "\f09b"; }
.icon-unlock:before               { content: "\f09c"; }
.icon-credit-card:before          { content: "\f09d"; }
.icon-rss:before                  { content: "\f09e"; }

.icon-hdd:before                  { content: "\f0a0"; }
.icon-bullhorn:before             { content: "\f0a1"; }
.icon-bell:before                 { content: "\f0a2"; }
.icon-certificate:before          { content: "\f0a3"; }
.icon-hand-right:before           { content: "\f0a4"; }
.icon-hand-left:before            { content: "\f0a5"; }
.icon-hand-up:before              { content: "\f0a6"; }
.icon-hand-down:before            { content: "\f0a7"; }
.icon-circle-arrow-left:before    { content: "\f0a8"; }
.icon-circle-arrow-right:before   { content: "\f0a9"; }
.icon-circle-arrow-up:before      { content: "\f0aa"; }
.icon-circle-arrow-down:before    { content: "\f0ab"; }
.icon-globe:before                { content: "\f0ac"; }
.icon-wrench:before               { content: "\f0ad"; }
.icon-tasks:before                { content: "\f0ae"; }

.icon-filter:before               { content: "\f0b0"; }
.icon-briefcase:before            { content: "\f0b1"; }
.icon-fullscreen:before           { content: "\f0b2"; }

.icon-group:before                { content: "\f0c0"; }
.icon-link:before                 { content: "\f0c1"; }
.icon-cloud:before                { content: "\f0c2"; }
.icon-beaker:before               { content: "\f0c3"; }
.icon-cut:before                  { content: "\f0c4"; }
.icon-copy:before                 { content: "\f0c5"; }
.icon-paper-clip:before           { content: "\f0c6"; }
.icon-save:before                 { content: "\f0c7"; }
.icon-sign-blank:before           { content: "\f0c8"; }
.icon-reorder:before              { content: "\f0c9"; }
.icon-list-ul:before              { content: "\f0ca"; }
.icon-list-ol:before              { content: "\f0cb"; }
.icon-strikethrough:before        { content: "\f0cc"; }
.icon-underline:before            { content: "\f0cd"; }
.icon-table:before                { content: "\f0ce"; }

.icon-magic:before                { content: "\f0d0"; }
.icon-truck:before                { content: "\f0d1"; }
.icon-pinterest:before            { content: "\f0d2"; }
.icon-pinterest-sign:before       { content: "\f0d3"; }
.icon-google-plus-sign:before     { content: "\f0d4"; }
.icon-google-plus:before          { content: "\f0d5"; }
.icon-money:before                { content: "\f0d6"; }
.icon-caret-down:before           { content: "\f0d7"; }
.icon-caret-up:before             { content: "\f0d8"; }
.icon-caret-left:before           { content: "\f0d9"; }
.icon-caret-right:before          { content: "\f0da"; }
.icon-columns:before              { content: "\f0db"; }
.icon-sort:before                 { content: "\f0dc"; }
.icon-sort-down:before            { content: "\f0dd"; }
.icon-sort-up:before              { content: "\f0de"; }

.icon-envelope-alt:before         { content: "\f0e0"; }
.icon-linkedin:before             { content: "\f0e1"; }
.icon-undo:before                 { content: "\f0e2"; }
.icon-legal:before                { content: "\f0e3"; }
.icon-dashboard:before            { content: "\f0e4"; }
.icon-comment-alt:before          { content: "\f0e5"; }
.icon-comments-alt:before         { content: "\f0e6"; }
.icon-bolt:before                 { content: "\f0e7"; }
.icon-sitemap:before              { content: "\f0e8"; }
.icon-umbrella:before             { content: "\f0e9"; }
.icon-paste:before                { content: "\f0ea"; }

.icon-user-md:before              { content: "\f200"; }


File: /lib\font-awesome\README.md
#Font Awesome 2.0
##the iconic font designed for use with Twitter Bootstrap

The full suite of pictographic icons, examples, and documentation can be found at:
http://fortawesome.github.com/Font-Awesome/

##Contact
- Email: dave@davegandy.com
- Twitter: http://twitter.com/fortaweso_me
- Work: Lead Product Designer @ http://kyru.us

##License
Version 2.0 of the Font Awesome font, CSS, and LESS files are licensed under CC BY 3.0:
http://creativecommons.org/licenses/by/3.0/
A mention of 'Font Awesome - http://fortawesome.github.com/Font-Awesome'
in human-readable source code is considered acceptable attribution (most common on the
web). If human readable source code is not available to the end user, a mention in an 'About' 
or 'Credits' screen is considered acceptable (most common in desktop or mobile software).


File: /lib\font-awesome\sass\font-awesome.sass
/*  Font Awesome
 *    the iconic font designed for use with Twitter Bootstrap
 *    -------------------------------------------------------
 *    The full suite of pictographic icons, examples, and documentation
 *    can be found at: http://fortawesome.github.com/Font-Awesome/
 *
 *    License
 *    -------------------------------------------------------
 *    The Font Awesome webfont, CSS, and LESS files are licensed under CC BY 3.0:
 *    http://creativecommons.org/licenses/by/3.0/ A mention of
 *    'Font Awesome - http://fortawesome.github.com/Font-Awesome' in human-readable
 *    source code is considered acceptable attribution (most common on the web).
 *    If human readable source code is not available to the end user, a mention in
 *    an 'About' or 'Credits' screen is considered acceptable (most common in desktop
 *    or mobile software).
 *
 *    Contact
 *    -------------------------------------------------------
 *    Email: dave@davegandy.com
 *    Twitter: http://twitter.com/fortaweso_me
 *    Work: Lead Product Designer @ http://kyruus.com

@import compass/css3/font-face

$fontAwesomePath: "../font/fontawesome-webfont" !default

+font-face("FontAwesome", font-files("#{$fontAwesomePath}.woff", woff, "#{$fontAwesomePath}.ttf", truetype, "#{$fontAwesomePath}.svg#FontAwesomeRegular", svg), "#{$fontAwesomePath}.eot", normal, normal)

/*  Font Awesome styles
 *  -------------------------------------------------------

[class^="icon-"]:before,
[class*=" icon-"]:before
  font-family: FontAwesome
  font-weight: normal
  font-style: normal
  display: inline-block
  text-decoration: inherit

a [class^="icon-"],
a [class*=" icon-"]
  display: inline-block
  text-decoration: inherit

/* makes the font 33% larger relative to the icon container
.icon-large:before
  vertical-align: middle
  font-size: 4 / 3em

.btn, .nav-tabs
  [class^="icon-"],
  [class*=" icon-"]
    /* keeps button heights with and without icons the same
    line-height: .9em

li
  [class^="icon-"],
  [class*=" icon-"]
    display: inline-block
    width: 1.25em
    text-align: center
  .icon-large:before,
  .icon-large:before
    /* 1.5 increased font size for icon-large * 1.25 width
    width: 1.5 * 1.25em

ul.icons
  list-style-type: none
  margin-left: 2em
  text-indent: -0.8em
  li
    [class^="icon-"],
    [class*=" icon-"]
      width: .8em
    .icon-large:before,
    .icon-large:before
      /* 1.5 increased font size for icon-large * 1.25 width
      vertical-align: initial
      //      width: 1.5*1.25em;

/*  Font Awesome uses the Unicode Private Use Area (PUA) to ensure screen
 *  readers do not read off random characters that represent icons
.icon-glass:before
  content: "\f000"

.icon-music:before
  content: "\f001"

.icon-search:before
  content: "\f002"

.icon-envelope:before
  content: "\f003"

.icon-heart:before
  content: "\f004"

.icon-star:before
  content: "\f005"

.icon-star-empty:before
  content: "\f006"

.icon-user:before
  content: "\f007"

.icon-film:before
  content: "\f008"

.icon-th-large:before
  content: "\f009"

.icon-th:before
  content: "\f00a"

.icon-th-list:before
  content: "\f00b"

.icon-ok:before
  content: "\f00c"

.icon-remove:before
  content: "\f00d"

.icon-zoom-in:before
  content: "\f00e"

.icon-zoom-out:before
  content: "\f010"

.icon-off:before
  content: "\f011"

.icon-signal:before
  content: "\f012"

.icon-cog:before
  content: "\f013"

.icon-trash:before
  content: "\f014"

.icon-home:before
  content: "\f015"

.icon-file:before
  content: "\f016"

.icon-time:before
  content: "\f017"

.icon-road:before
  content: "\f018"

.icon-download-alt:before
  content: "\f019"

.icon-download:before
  content: "\f01a"

.icon-upload:before
  content: "\f01b"

.icon-inbox:before
  content: "\f01c"

.icon-play-circle:before
  content: "\f01d"

.icon-repeat:before
  content: "\f01e"

/* \f020 doesn't work in Safari. all shifted one down
.icon-refresh:before
  content: "\f021"

.icon-list-alt:before
  content: "\f022"

.icon-lock:before
  content: "\f023"

.icon-flag:before
  content: "\f024"

.icon-headphones:before
  content: "\f025"

.icon-volume-off:before
  content: "\f026"

.icon-volume-down:before
  content: "\f027"

.icon-volume-up:before
  content: "\f028"

.icon-qrcode:before
  content: "\f029"

.icon-barcode:before
  content: "\f02a"

.icon-tag:before
  content: "\f02b"

.icon-tags:before
  content: "\f02c"

.icon-book:before
  content: "\f02d"

.icon-bookmark:before
  content: "\f02e"

.icon-print:before
  content: "\f02f"

.icon-camera:before
  content: "\f030"

.icon-font:before
  content: "\f031"

.icon-bold:before
  content: "\f032"

.icon-italic:before
  content: "\f033"

.icon-text-height:before
  content: "\f034"

.icon-text-width:before
  content: "\f035"

.icon-align-left:before
  content: "\f036"

.icon-align-center:before
  content: "\f037"

.icon-align-right:before
  content: "\f038"

.icon-align-justify:before
  content: "\f039"

.icon-list:before
  content: "\f03a"

.icon-indent-left:before
  content: "\f03b"

.icon-indent-right:before
  content: "\f03c"

.icon-facetime-video:before
  content: "\f03d"

.icon-picture:before
  content: "\f03e"

.icon-pencil:before
  content: "\f040"

.icon-map-marker:before
  content: "\f041"

.icon-adjust:before
  content: "\f042"

.icon-tint:before
  content: "\f043"

.icon-edit:before
  content: "\f044"

.icon-share:before
  content: "\f045"

.icon-check:before
  content: "\f046"

.icon-move:before
  content: "\f047"

.icon-step-backward:before
  content: "\f048"

.icon-fast-backward:before
  content: "\f049"

.icon-backward:before
  content: "\f04a"

.icon-play:before
  content: "\f04b"

.icon-pause:before
  content: "\f04c"

.icon-stop:before
  content: "\f04d"

.icon-forward:before
  content: "\f04e"

.icon-fast-forward:before
  content: "\f050"

.icon-step-forward:before
  content: "\f051"

.icon-eject:before
  content: "\f052"

.icon-chevron-left:before
  content: "\f053"

.icon-chevron-right:before
  content: "\f054"

.icon-plus-sign:before
  content: "\f055"

.icon-minus-sign:before
  content: "\f056"

.icon-remove-sign:before
  content: "\f057"

.icon-ok-sign:before
  content: "\f058"

.icon-question-sign:before
  content: "\f059"

.icon-info-sign:before
  content: "\f05a"

.icon-screenshot:before
  content: "\f05b"

.icon-remove-circle:before
  content: "\f05c"

.icon-ok-circle:before
  content: "\f05d"

.icon-ban-circle:before
  content: "\f05e"

.icon-arrow-left:before
  content: "\f060"

.icon-arrow-right:before
  content: "\f061"

.icon-arrow-up:before
  content: "\f062"

.icon-arrow-down:before
  content: "\f063"

.icon-share-alt:before
  content: "\f064"

.icon-resize-full:before
  content: "\f065"

.icon-resize-small:before
  content: "\f066"

.icon-plus:before
  content: "\f067"

.icon-minus:before
  content: "\f068"

.icon-asterisk:before
  content: "\f069"

.icon-exclamation-sign:before
  content: "\f06a"

.icon-gift:before
  content: "\f06b"

.icon-leaf:before
  content: "\f06c"

.icon-fire:before
  content: "\f06d"

.icon-eye-open:before
  content: "\f06e"

.icon-eye-close:before
  content: "\f070"

.icon-warning-sign:before
  content: "\f071"

.icon-plane:before
  content: "\f072"

.icon-calendar:before
  content: "\f073"

.icon-random:before
  content: "\f074"

.icon-comment:before
  content: "\f075"

.icon-magnet:before
  content: "\f076"

.icon-chevron-up:before
  content: "\f077"

.icon-chevron-down:before
  content: "\f078"

.icon-retweet:before
  content: "\f079"

.icon-shopping-cart:before
  content: "\f07a"

.icon-folder-close:before
  content: "\f07b"

.icon-folder-open:before
  content: "\f07c"

.icon-resize-vertical:before
  content: "\f07d"

.icon-resize-horizontal:before
  content: "\f07e"

.icon-bar-chart:before
  content: "\f080"

.icon-twitter-sign:before
  content: "\f081"

.icon-facebook-sign:before
  content: "\f082"

.icon-camera-retro:before
  content: "\f083"

.icon-key:before
  content: "\f084"

.icon-cogs:before
  content: "\f085"

.icon-comments:before
  content: "\f086"

.icon-thumbs-up:before
  content: "\f087"

.icon-thumbs-down:before
  content: "\f088"

.icon-star-half:before
  content: "\f089"

.icon-heart-empty:before
  content: "\f08a"

.icon-signout:before
  content: "\f08b"

.icon-linkedin-sign:before
  content: "\f08c"

.icon-pushpin:before
  content: "\f08d"

.icon-external-link:before
  content: "\f08e"

.icon-signin:before
  content: "\f090"

.icon-trophy:before
  content: "\f091"

.icon-github-sign:before
  content: "\f092"

.icon-upload-alt:before
  content: "\f093"

.icon-lemon:before
  content: "\f094"

.icon-phone:before
  content: "\f095"

.icon-check-empty:before
  content: "\f096"

.icon-bookmark-empty:before
  content: "\f097"

.icon-phone-sign:before
  content: "\f098"

.icon-twitter:before
  content: "\f099"

.icon-facebook:before
  content: "\f09a"

.icon-github:before
  content: "\f09b"

.icon-unlock:before
  content: "\f09c"

.icon-credit-card:before
  content: "\f09d"

.icon-rss:before
  content: "\f09e"

.icon-hdd:before
  content: "\f0a0"

.icon-bullhorn:before
  content: "\f0a1"

.icon-bell:before
  content: "\f0a2"

.icon-certificate:before
  content: "\f0a3"

.icon-hand-right:before
  content: "\f0a4"

.icon-hand-left:before
  content: "\f0a5"

.icon-hand-up:before
  content: "\f0a6"

.icon-hand-down:before
  content: "\f0a7"

.icon-circle-arrow-left:before
  content: "\f0a8"

.icon-circle-arrow-right:before
  content: "\f0a9"

.icon-circle-arrow-up:before
  content: "\f0aa"

.icon-circle-arrow-down:before
  content: "\f0ab"

.icon-globe:before
  content: "\f0ac"

.icon-wrench:before
  content: "\f0ad"

.icon-tasks:before
  content: "\f0ae"

.icon-filter:before
  content: "\f0b0"

.icon-briefcase:before
  content: "\f0b1"

.icon-fullscreen:before
  content: "\f0b2"

.icon-group:before
  content: "\f0c0"

.icon-link:before
  content: "\f0c1"

.icon-cloud:before
  content: "\f0c2"

.icon-beaker:before
  content: "\f0c3"

.icon-cut:before
  content: "\f0c4"

.icon-copy:before
  content: "\f0c5"

.icon-paper-clip:before
  content: "\f0c6"

.icon-save:before
  content: "\f0c7"

.icon-sign-blank:before
  content: "\f0c8"

.icon-reorder:before
  content: "\f0c9"

.icon-list-ul:before
  content: "\f0ca"

.icon-list-ol:before
  content: "\f0cb"

.icon-strikethrough:before
  content: "\f0cc"

.icon-underline:before
  content: "\f0cd"

.icon-table:before
  content: "\f0ce"

.icon-magic:before
  content: "\f0d0"

.icon-truck:before
  content: "\f0d1"

.icon-pinterest:before
  content: "\f0d2"

.icon-pinterest-sign:before
  content: "\f0d3"

.icon-google-plus-sign:before
  content: "\f0d4"

.icon-google-plus:before
  content: "\f0d5"

.icon-money:before
  content: "\f0d6"

.icon-caret-down:before
  content: "\f0d7"

.icon-caret-up:before
  content: "\f0d8"

.icon-caret-left:before
  content: "\f0d9"

.icon-caret-right:before
  content: "\f0da"

.icon-columns:before
  content: "\f0db"

.icon-sort:before
  content: "\f0dc"

.icon-sort-down:before
  content: "\f0dd"

.icon-sort-up:before
  content: "\f0de"

.icon-envelope-alt:before
  content: "\f0e0"

.icon-linkedin:before
  content: "\f0e1"

.icon-undo:before
  content: "\f0e2"

.icon-legal:before
  content: "\f0e3"

.icon-dashboard:before
  content: "\f0e4"

.icon-comment-alt:before
  content: "\f0e5"

.icon-comments-alt:before
  content: "\f0e6"

.icon-bolt:before
  content: "\f0e7"

.icon-sitemap:before
  content: "\f0e8"

.icon-umbrella:before
  content: "\f0e9"

.icon-paste:before
  content: "\f0ea"

.icon-user-md:before
  content: "\f200"


File: /lib\font-awesome\sass\font-awesome.scss
/*  Font Awesome
    the iconic font designed for use with Twitter Bootstrap
    -------------------------------------------------------
    The full suite of pictographic icons, examples, and documentation
    can be found at: http://fortawesome.github.com/Font-Awesome/

    License
    -------------------------------------------------------
    The Font Awesome webfont, CSS, and LESS files are licensed under CC BY 3.0:
    http://creativecommons.org/licenses/by/3.0/ A mention of
    'Font Awesome - http://fortawesome.github.com/Font-Awesome' in human-readable
    source code is considered acceptable attribution (most common on the web).
    If human readable source code is not available to the end user, a mention in
    an 'About' or 'Credits' screen is considered acceptable (most common in desktop
    or mobile software).

    Contact
    -------------------------------------------------------
    Email: dave@davegandy.com
    Twitter: http://twitter.com/fortaweso_me
    Work: Lead Product Designer @ http://kyruus.com

    */

@import "compass/css3/font-face";
$fontAwesomePath: "../font/fontawesome-webfont" !default;

@include font-face(
    'FontAwesome',
    font-files(
        "#{$fontAwesomePath}.woff", woff,
        "#{$fontAwesomePath}.ttf", truetype,
        "#{$fontAwesomePath}.svg#FontAwesomeRegular", svg),
    '#{$fontAwesomePath}.eot',
    normal,
    normal);

/*  Font Awesome styles
    ------------------------------------------------------- */
[class^="icon-"]:before,
[class*=" icon-"]:before {
  font-family: FontAwesome;
  font-weight: normal;
  font-style: normal;
  display: inline-block;
  text-decoration: inherit;
}

a [class^="icon-"],
a [class*=" icon-"] {
  display: inline-block;
  text-decoration: inherit;
}

/* makes the font 33% larger relative to the icon container */
.icon-large:before {
  vertical-align: middle;
  font-size: 4/3em;
}

.btn, .nav-tabs {
  [class^="icon-"],
  [class*=" icon-"] {
  /* keeps button heights with and without icons the same */
    line-height: .9em;
  }
}

li {
  [class^="icon-"],
  [class*=" icon-"] {
    display: inline-block;
    width: 1.25em;
    text-align: center;
  }
  .icon-large:before,
  .icon-large:before {
    /* 1.5 increased font size for icon-large * 1.25 width */
    width: 1.5*1.25em;
  }
}

ul.icons {
  list-style-type: none;
  margin-left: 2em;
  text-indent: -.8em;

  li {
    [class^="icon-"],
    [class*=" icon-"] {
      width: .8em;
    }
    .icon-large:before,
    .icon-large:before {
      /* 1.5 increased font size for icon-large * 1.25 width */
      vertical-align: initial;
//      width: 1.5*1.25em;
    }
  }
}

/*  Font Awesome uses the Unicode Private Use Area (PUA) to ensure screen
    readers do not read off random characters that represent icons */
.icon-glass:before                { content: "\f000"; }
.icon-music:before                { content: "\f001"; }
.icon-search:before               { content: "\f002"; }
.icon-envelope:before             { content: "\f003"; }
.icon-heart:before                { content: "\f004"; }
.icon-star:before                 { content: "\f005"; }
.icon-star-empty:before           { content: "\f006"; }
.icon-user:before                 { content: "\f007"; }
.icon-film:before                 { content: "\f008"; }
.icon-th-large:before             { content: "\f009"; }
.icon-th:before                   { content: "\f00a"; }
.icon-th-list:before              { content: "\f00b"; }
.icon-ok:before                   { content: "\f00c"; }
.icon-remove:before               { content: "\f00d"; }
.icon-zoom-in:before              { content: "\f00e"; }

.icon-zoom-out:before             { content: "\f010"; }
.icon-off:before                  { content: "\f011"; }
.icon-signal:before               { content: "\f012"; }
.icon-cog:before                  { content: "\f013"; }
.icon-trash:before                { content: "\f014"; }
.icon-home:before                 { content: "\f015"; }
.icon-file:before                 { content: "\f016"; }
.icon-time:before                 { content: "\f017"; }
.icon-road:before                 { content: "\f018"; }
.icon-download-alt:before         { content: "\f019"; }
.icon-download:before             { content: "\f01a"; }
.icon-upload:before               { content: "\f01b"; }
.icon-inbox:before                { content: "\f01c"; }
.icon-play-circle:before          { content: "\f01d"; }
.icon-repeat:before               { content: "\f01e"; }

/* \f020 doesn't work in Safari. all shifted one down */
.icon-refresh:before              { content: "\f021"; }
.icon-list-alt:before             { content: "\f022"; }
.icon-lock:before                 { content: "\f023"; }
.icon-flag:before                 { content: "\f024"; }
.icon-headphones:before           { content: "\f025"; }
.icon-volume-off:before           { content: "\f026"; }
.icon-volume-down:before          { content: "\f027"; }
.icon-volume-up:before            { content: "\f028"; }
.icon-qrcode:before               { content: "\f029"; }
.icon-barcode:before              { content: "\f02a"; }
.icon-tag:before                  { content: "\f02b"; }
.icon-tags:before                 { content: "\f02c"; }
.icon-book:before                 { content: "\f02d"; }
.icon-bookmark:before             { content: "\f02e"; }
.icon-print:before                { content: "\f02f"; }

.icon-camera:before               { content: "\f030"; }
.icon-font:before                 { content: "\f031"; }
.icon-bold:before                 { content: "\f032"; }
.icon-italic:before               { content: "\f033"; }
.icon-text-height:before          { content: "\f034"; }
.icon-text-width:before           { content: "\f035"; }
.icon-align-left:before           { content: "\f036"; }
.icon-align-center:before         { content: "\f037"; }
.icon-align-right:before          { content: "\f038"; }
.icon-align-justify:before        { content: "\f039"; }
.icon-list:before                 { content: "\f03a"; }
.icon-indent-left:before          { content: "\f03b"; }
.icon-indent-right:before         { content: "\f03c"; }
.icon-facetime-video:before       { content: "\f03d"; }
.icon-picture:before              { content: "\f03e"; }

.icon-pencil:before               { content: "\f040"; }
.icon-map-marker:before           { content: "\f041"; }
.icon-adjust:before               { content: "\f042"; }
.icon-tint:before                 { content: "\f043"; }
.icon-edit:before                 { content: "\f044"; }
.icon-share:before                { content: "\f045"; }
.icon-check:before                { content: "\f046"; }
.icon-move:before                 { content: "\f047"; }
.icon-step-backward:before        { content: "\f048"; }
.icon-fast-backward:before        { content: "\f049"; }
.icon-backward:before             { content: "\f04a"; }
.icon-play:before                 { content: "\f04b"; }
.icon-pause:before                { content: "\f04c"; }
.icon-stop:before                 { content: "\f04d"; }
.icon-forward:before              { content: "\f04e"; }

.icon-fast-forward:before         { content: "\f050"; }
.icon-step-forward:before         { content: "\f051"; }
.icon-eject:before                { content: "\f052"; }
.icon-chevron-left:before         { content: "\f053"; }
.icon-chevron-right:before        { content: "\f054"; }
.icon-plus-sign:before            { content: "\f055"; }
.icon-minus-sign:before           { content: "\f056"; }
.icon-remove-sign:before          { content: "\f057"; }
.icon-ok-sign:before              { content: "\f058"; }
.icon-question-sign:before        { content: "\f059"; }
.icon-info-sign:before            { content: "\f05a"; }
.icon-screenshot:before           { content: "\f05b"; }
.icon-remove-circle:before        { content: "\f05c"; }
.icon-ok-circle:before            { content: "\f05d"; }
.icon-ban-circle:before           { content: "\f05e"; }

.icon-arrow-left:before           { content: "\f060"; }
.icon-arrow-right:before          { content: "\f061"; }
.icon-arrow-up:before             { content: "\f062"; }
.icon-arrow-down:before           { content: "\f063"; }
.icon-share-alt:before            { content: "\f064"; }
.icon-resize-full:before          { content: "\f065"; }
.icon-resize-small:before         { content: "\f066"; }
.icon-plus:before                 { content: "\f067"; }
.icon-minus:before                { content: "\f068"; }
.icon-asterisk:before             { content: "\f069"; }
.icon-exclamation-sign:before     { content: "\f06a"; }
.icon-gift:before                 { content: "\f06b"; }
.icon-leaf:before                 { content: "\f06c"; }
.icon-fire:before                 { content: "\f06d"; }
.icon-eye-open:before             { content: "\f06e"; }

.icon-eye-close:before            { content: "\f070"; }
.icon-warning-sign:before         { content: "\f071"; }
.icon-plane:before                { content: "\f072"; }
.icon-calendar:before             { content: "\f073"; }
.icon-random:before               { content: "\f074"; }
.icon-comment:before              { content: "\f075"; }
.icon-magnet:before               { content: "\f076"; }
.icon-chevron-up:before           { content: "\f077"; }
.icon-chevron-down:before         { content: "\f078"; }
.icon-retweet:before              { content: "\f079"; }
.icon-shopping-cart:before        { content: "\f07a"; }
.icon-folder-close:before         { content: "\f07b"; }
.icon-folder-open:before          { content: "\f07c"; }
.icon-resize-vertical:before      { content: "\f07d"; }
.icon-resize-horizontal:before    { content: "\f07e"; }

.icon-bar-chart:before            { content: "\f080"; }
.icon-twitter-sign:before         { content: "\f081"; }
.icon-facebook-sign:before        { content: "\f082"; }
.icon-camera-retro:before         { content: "\f083"; }
.icon-key:before                  { content: "\f084"; }
.icon-cogs:before                 { content: "\f085"; }
.icon-comments:before             { content: "\f086"; }
.icon-thumbs-up:before            { content: "\f087"; }
.icon-thumbs-down:before          { content: "\f088"; }
.icon-star-half:before            { content: "\f089"; }
.icon-heart-empty:before          { content: "\f08a"; }
.icon-signout:before              { content: "\f08b"; }
.icon-linkedin-sign:before        { content: "\f08c"; }
.icon-pushpin:before              { content: "\f08d"; }
.icon-external-link:before        { content: "\f08e"; }

.icon-signin:before               { content: "\f090"; }
.icon-trophy:before               { content: "\f091"; }
.icon-github-sign:before          { content: "\f092"; }
.icon-upload-alt:before           { content: "\f093"; }
.icon-lemon:before                { content: "\f094"; }
.icon-phone:before                { content: "\f095"; }
.icon-check-empty:before          { content: "\f096"; }
.icon-bookmark-empty:before       { content: "\f097"; }
.icon-phone-sign:before           { content: "\f098"; }
.icon-twitter:before              { content: "\f099"; }
.icon-facebook:before             { content: "\f09a"; }
.icon-github:before               { content: "\f09b"; }
.icon-unlock:before               { content: "\f09c"; }
.icon-credit-card:before          { content: "\f09d"; }
.icon-rss:before                  { content: "\f09e"; }

.icon-hdd:before                  { content: "\f0a0"; }
.icon-bullhorn:before             { content: "\f0a1"; }
.icon-bell:before                 { content: "\f0a2"; }
.icon-certificate:before          { content: "\f0a3"; }
.icon-hand-right:before           { content: "\f0a4"; }
.icon-hand-left:before            { content: "\f0a5"; }
.icon-hand-up:before              { content: "\f0a6"; }
.icon-hand-down:before            { content: "\f0a7"; }
.icon-circle-arrow-left:before    { content: "\f0a8"; }
.icon-circle-arrow-right:before   { content: "\f0a9"; }
.icon-circle-arrow-up:before      { content: "\f0aa"; }
.icon-circle-arrow-down:before    { content: "\f0ab"; }
.icon-globe:before                { content: "\f0ac"; }
.icon-wrench:before               { content: "\f0ad"; }
.icon-tasks:before                { content: "\f0ae"; }

.icon-filter:before               { content: "\f0b0"; }
.icon-briefcase:before            { content: "\f0b1"; }
.icon-fullscreen:before           { content: "\f0b2"; }

.icon-group:before                { content: "\f0c0"; }
.icon-link:before                 { content: "\f0c1"; }
.icon-cloud:before                { content: "\f0c2"; }
.icon-beaker:before               { content: "\f0c3"; }
.icon-cut:before                  { content: "\f0c4"; }
.icon-copy:before                 { content: "\f0c5"; }
.icon-paper-clip:before           { content: "\f0c6"; }
.icon-save:before                 { content: "\f0c7"; }
.icon-sign-blank:before           { content: "\f0c8"; }
.icon-reorder:before              { content: "\f0c9"; }
.icon-list-ul:before              { content: "\f0ca"; }
.icon-list-ol:before              { content: "\f0cb"; }
.icon-strikethrough:before        { content: "\f0cc"; }
.icon-underline:before            { content: "\f0cd"; }
.icon-table:before                { content: "\f0ce"; }

.icon-magic:before                { content: "\f0d0"; }
.icon-truck:before                { content: "\f0d1"; }
.icon-pinterest:before            { content: "\f0d2"; }
.icon-pinterest-sign:before       { content: "\f0d3"; }
.icon-google-plus-sign:before     { content: "\f0d4"; }
.icon-google-plus:before          { content: "\f0d5"; }
.icon-money:before                { content: "\f0d6"; }
.icon-caret-down:before           { content: "\f0d7"; }
.icon-caret-up:before             { content: "\f0d8"; }
.icon-caret-left:before           { content: "\f0d9"; }
.icon-caret-right:before          { content: "\f0da"; }
.icon-columns:before              { content: "\f0db"; }
.icon-sort:before                 { content: "\f0dc"; }
.icon-sort-down:before            { content: "\f0dd"; }
.icon-sort-up:before              { content: "\f0de"; }

.icon-envelope-alt:before         { content: "\f0e0"; }
.icon-linkedin:before             { content: "\f0e1"; }
.icon-undo:before                 { content: "\f0e2"; }
.icon-legal:before                { content: "\f0e3"; }
.icon-dashboard:before            { content: "\f0e4"; }
.icon-comment-alt:before          { content: "\f0e5"; }
.icon-comments-alt:before         { content: "\f0e6"; }
.icon-bolt:before                 { content: "\f0e7"; }
.icon-sitemap:before              { content: "\f0e8"; }
.icon-umbrella:before             { content: "\f0e9"; }
.icon-paste:before                { content: "\f0ea"; }

.icon-user-md:before              { content: "\f200"; }


File: /login.php
<?php 
	ini_set( "display_errors", 0); 
	session_start();
	// Cek Login
	if (isset($_SESSION['user'])){
		header("location:index.php");
	} else {	
?>
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <title>Halaman Login | Aplikasi Generate User Hotspot Mikrotik</title>
    <meta content="IE=edge,chrome=1" http-equiv="X-UA-Compatible">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" type="text/css" href="lib/bootstrap/css/bootstrap.css">
    <link rel="stylesheet" type="text/css" href="lib/bootstrap/css/bootstrap-responsive.css">
    <link rel="stylesheet" type="text/css" href="css/theme.css">
    <link rel="stylesheet" href="lib/font-awesome/css/font-awesome.css">
    <script src="lib/jquery-1.8.1.min.js" type="text/javascript"></script>
	<script type="text/javascript" src="lib/jquery.validate.min.js"></script>
    <link rel="shortcut icon" href="images/logo_mikrotik.png">
 </head>

  <body> 
	<script>var $jnoc = jQuery.noConflict();</script>
    
    <div class="navbar">
        <div class="navbar-inner">
            <div class="container-fluid">
                <ul class="nav pull-right">
                    
                </ul>
                <a class="brand" href="#"><span class="first">Aplikasi Generate User Hotspot</span> <span class="second">Mikrotik</span></a>
            </div>
        </div>
    </div>
    

    <div class="container-fluid">
        
        <div class="row-fluid">
    <div class="dialog span4">
        <div class="block">
            <div class="block-heading">Silahkan Login</div>
            <div class="block-body">
			
                <form method="post" action="" id="loginform">
				
					<label>Ip Address</label>
                    <input type="text" id="ip" name="ip" class="required span12">
                    <label>Username</label>
                    <input type="text" id="user" name="user" class="required span12">
                    <label>Password</label>
                    <input type="password" id="pass" name="pass" class="span12">
					
					<img src="images/loading.gif" id="lproses" class="load pull-right" style="padding-top:5px">
					<input type="submit" name="submit" value="Login" id="masuk" class="btn btn-primary pull-right"/>
					
                    <a href="#myModal" role="button" data-toggle="modal" id="login" class="btn load btn-primary pull-right">Login</a>      
					<div class="clearfix"></div>
                </form>
				
            </div>
        </div>

    </div>
</div>

    <script src="lib/bootstrap/js/bootstrap.js"></script>
    <script src="aksi/js/login/aksi_login.js"></script>
    
	<div class="modal small hide fade" id="myModal" tabindex="-1" role="dialog" aria-labelledby="myModalLabel" aria-hidden="true">
    <div class="modal-header">
        <button type="button" class="close" data-dismiss="modal" aria-hidden="true">×</button>
        <h3 id="myModalLabel">Perhatian</h3>
    </div>
    <div class="modal-body">
        <p class="error-text"></p>
    </div>
    <div class="modal-footer">
        <button class="btn btn-danger" data-dismiss="modal" aria-hidden="true">Tutup</button>
    </div>
</div>

  </body>
</html>

<?php } ?>



File: /logout.php
<?php 
/* Proses Logout :
   Hapus Session User Lalu Arahkan ke Halaman Login
*/
session_start();
unset($_SESSION['user']);
header("location:login.php");
?>

File: /penting\excel_export.php
<?php

  require_once("koneksi.php");
  
  function cariprofile($API,$namaprof){
		
		$API->write("/ip/hotspot/user/profile/print",false);   
		$API->write("?name=".$namaprof,true);   
		$p = $API->read(); 
	
		foreach($p as $tam){
		$nama = $tam['name'];
		$lm = $tam['rate-limit'];
		}
		
		$limitbw = $nama." (".$lm.")";	
		
		return $limitbw;
	}
	
  $API->write("/ip/hotspot/user/print");    
  $uh = $API->read();

  function cleanData(&$str){
    $str = preg_replace("/\t/", "\\t", $str);
    $str = preg_replace("/\r?\n/", "\\n", $str);
    if(strstr($str, '"')) $str = '"' . str_replace('"', '""', $str) . '"';
  }

  $filename = "data_user_hotspot.xls";

  header("Content-Disposition: attachment; filename=\"$filename\"");
  header("Content-Type: application/vnd.ms-excel");

  $flag = false;
  $no=1;
  
  foreach($uh as $row) {
	
    if(!$flag) {
      echo "No"."\t"."Nama User"."\t"."Password"."\t"."Limit Waktu"."\t"."Limit Bandwidth"."\n";
      $flag = true;
    }
	
	$limitbw = cariprofile($API,$row['profile']);
	
	echo "\t".$no."\t".$row['name']."\t".$row['password']."\t".$row['limit-uptime']."\t".$limitbw."\n";
	
	$no++;
  }

  exit;
?>


File: /penting\koneksi.php

	<?php 
		 include("routeros_api.php");
		 $API = new routeros_api();
		 if (!$API->connect("192.168.10.1","admin","a")){
			 unset($_SESSION["user"]);
			 header("location:login.php");
		 }
	?>

File: /penting\pdf_export.php
<?php
ini_set( "display_errors", 0);
require_once('../fpdf/fpdf.php');
require_once('koneksi.php');


class PDF extends FPDF{

	function cariprofile($API,$namaprof){
		
		$API->write("/ip/hotspot/user/profile/print",false);   
		$API->write("?name=".$namaprof,true);   
		$p = $API->read(); 
	
		foreach($p as $tam){
		$nama = $tam['name'];
		$lm = $tam['rate-limit'];
		}
		
		$limitbw = $nama." (".$lm.")";	
		
		return $limitbw;
	}
	
 function LoadData($gue){
  $data = array();
  if (is_array($gue)) {
  foreach($gue as $coba)
   $data[] = explode('|',$coba);
  }
  return $data;
 }
 
function Kepala(){
	

    $this->Image('../images/miklogo.png',12,13,16);
	$this->Ln(2);

    $this->SetFont('Arial','B',15);
    $this->Cell(45);

	$this->Cell(100,0,'Aplikasi Generate User Hotspot',0,0,'C');
	$this->Ln(8);
	$this->Cell(45);
	$this->Cell(100,0,'Sekolah Tinggi Teologia Arastamar Mataram (STTAM)',0,0,'C');
	$this->Ln(8);
	$this->SetFont('Arial','B',12);
	$this->Cell(45);
	$this->Cell(100,0,'Developed By. Mahasiswa STMIK Bumigora Mataram',0,0,'C');
	$this->Ln(6);
    $this->SetFont('Arial','B',8);
	$this->Cell(45);
	$this->Line(10, 33, 210-10, 33);
	$this->Line(10, 34, 210-10, 34);
	$this->Ln(5);
    $this->SetFont('Arial','B',15);
    $this->Cell(45);
	$this->Cell(100,0,'DATA USER HOTSPOT',0,0,'C');
	$this->Ln(5);
	$this->SetFont('Arial','',12);
} 

 function FancyTable($header, $data){
  $this->SetFillColor(50,50,50);
  $this->SetTextColor(255);
  $this->SetDrawColor(0,0,0);
  $this->SetFont('Arial','',12);
  $w = array(10, 45, 45, 40, 50);
  for($i=0;$i<count($header);$i++)
  $this->Cell($w[$i],7,$header[$i],1,0,'C',true);
  $this->Ln();
  $this->SetFillColor(200,200,200);
  $this->SetTextColor(0);
  $this->SetFont('Arial','',12);

  $fill = false;
  foreach($data as $row){

   $this->Cell($w[0],6,$row[0],'LR',0,'C',$fill); 
   $this->Cell($w[1],6,$row[1],'LR',0,'C',$fill);
   $this->Cell($w[2],6,$row[2],'LR',0,'C',$fill);
   $this->Cell($w[3],6,$row[3],'LR',0,'C',$fill);
   $this->Cell($w[4],6,$row[4],'LR',0,'C',$fill);
   $this->Ln();
   $fill = !$fill;
  }
   $this->Cell(array_sum($w),0,'','T');
 }
 }

 $pdf = new PDF();
 $header = array('No', 'Nama User', 'Password', 'Limit Waktu', 'Limit Bandwidth');
 $no=1;
 $API->write("/ip/hotspot/user/print");   
 $uh = $API->read();
 foreach($uh as $tampil){
	 
  $limitbw = $pdf->cariprofile($API,$tampil['profile']);
	
 @$gue[] .= $no."|".$tampil['name']."|".$tampil['password']."|".$tampil['limit-uptime']."|".$limitbw;
 $no++;
 }

 $data = $pdf->LoadData($gue);
 $pdf->SetFont('Arial','',12);
 $pdf->AddPage();
 $pdf->Kepala();
 $pdf->FancyTable($header,$data);
 $pdf->Output("data_user_hotspot.pdf","D");

?>

File: /penting\routeros_api.php
<?php
/*****************************
 *
 * RouterOS PHP API class v1.6
 * Author: Denis Basta
 * Contributors:
 *    Nick Barnes
 *    Ben Menking (ben [at] infotechsc [dot] com)
 *    Jeremy Jefferson (http://jeremyj.com)
 *    Cristian Deluxe (djcristiandeluxe [at] gmail [dot] com)
 *    Mikhail Moskalev (mmv.rus [at] gmail [dot] com)
 *
 * http://www.mikrotik.com
 * http://wiki.mikrotik.com/wiki/API_PHP_class
 *
 ******************************/

class RouterosAPI
{
    var $debug     = false; //  Show debug information
    var $connected = false; //  Connection state
    var $port      = 8728;  //  Port to connect to (default 8729 for ssl)
    var $ssl       = false; //  Connect using SSL (must enable api-ssl in IP/Services)
    var $timeout   = 3;     //  Connection attempt timeout and data read timeout
    var $attempts  = 5;     //  Connection attempt count
    var $delay     = 3;     //  Delay between connection attempts in seconds

    var $socket;            //  Variable for storing socket resource
    var $error_no;          //  Variable for storing connection error number, if any
    var $error_str;         //  Variable for storing connection error text, if any

    /* Check, can be var used in foreach  */
    public function isIterable($var)
    {
        return $var !== null
                && (is_array($var)
                || $var instanceof Traversable
                || $var instanceof Iterator
                || $var instanceof IteratorAggregate
                );
    }

    /**
     * Print text for debug purposes
     *
     * @param string      $text       Text to print
     *
     * @return void
     */
    public function debug($text)
    {
        if ($this->debug) {
            echo $text . "\n";
        }
    }


    /**
     *
     *
     * @param string        $length
     *
     * @return void
     */
    public function encodeLength($length)
    {
        if ($length < 0x80) {
            $length = chr($length);
        } elseif ($length < 0x4000) {
            $length |= 0x8000;
            $length = chr(($length >> 8) & 0xFF) . chr($length & 0xFF);
        } elseif ($length < 0x200000) {
            $length |= 0xC00000;
            $length = chr(($length >> 16) & 0xFF) . chr(($length >> 8) & 0xFF) . chr($length & 0xFF);
        } elseif ($length < 0x10000000) {
            $length |= 0xE0000000;
            $length = chr(($length >> 24) & 0xFF) . chr(($length >> 16) & 0xFF) . chr(($length >> 8) & 0xFF) . chr($length & 0xFF);
        } elseif ($length >= 0x10000000) {
            $length = chr(0xF0) . chr(($length >> 24) & 0xFF) . chr(($length >> 16) & 0xFF) . chr(($length >> 8) & 0xFF) . chr($length & 0xFF);
        }

        return $length;
    }


    /**
     * Login to RouterOS
     *
     * @param string      $ip         Hostname (IP or domain) of the RouterOS server
     * @param string      $login      The RouterOS username
     * @param string      $password   The RouterOS password
     *
     * @return boolean                If we are connected or not
     */
    public function connect($ip, $login, $password)
    {
        for ($ATTEMPT = 1; $ATTEMPT <= $this->attempts; $ATTEMPT++) {
            $this->connected = false;
            $PROTOCOL = ($this->ssl ? 'ssl://' : '' );
            $context = stream_context_create(array('ssl' => array('ciphers' => 'ADH:ALL', 'verify_peer' => false, 'verify_peer_name' => false)));
            $this->debug('Connection attempt #' . $ATTEMPT . ' to ' . $PROTOCOL . $ip . ':' . $this->port . '...');
            $this->socket = @stream_socket_client($PROTOCOL . $ip.':'. $this->port, $this->error_no, $this->error_str, $this->timeout, STREAM_CLIENT_CONNECT,$context);
            if ($this->socket) {
                socket_set_timeout($this->socket, $this->timeout);
                $this->write('/login', false);
                $this->write('=name=' . $login, false);
                $this->write('=password=' . $password);
                $RESPONSE = $this->read(false);
                if (isset($RESPONSE[0])) {
                    if ($RESPONSE[0] == '!done') {
                        if (!isset($RESPONSE[1])) {
                            // Login method post-v6.43
                            $this->connected = true;
                            break;
                        } else {
                            // Login method pre-v6.43
                            $MATCHES = array();
                            if (preg_match_all('/[^=]+/i', $RESPONSE[1], $MATCHES)) {
                                if ($MATCHES[0][0] == 'ret' && strlen($MATCHES[0][1]) == 32) {
                                    $this->write('/login', false);
                                    $this->write('=name=' . $login, false);
                                    $this->write('=response=00' . md5(chr(0) . $password . pack('H*', $MATCHES[0][1])));
                                    $RESPONSE = $this->read(false);
                                    if (isset($RESPONSE[0]) && $RESPONSE[0] == '!done') {
                                        $this->connected = true;
                                        break;
                                    }
                                }
                            }
                        }
                    }
                }
                fclose($this->socket);
            }
            sleep($this->delay);
        }

        if ($this->connected) {
            $this->debug('Connected...');
        } else {
            $this->debug('Error...');
        }
        return $this->connected;
    }


    /**
     * Disconnect from RouterOS
     *
     * @return void
     */
    public function disconnect()
    {
        // let's make sure this socket is still valid.  it may have been closed by something else
        if( is_resource($this->socket) ) {
            fclose($this->socket);
        }
        $this->connected = false;
        $this->debug('Disconnected...');
    }


    /**
     * Parse response from Router OS
     *
     * @param array       $response   Response data
     *
     * @return array                  Array with parsed data
     */
    public function parseResponse($response)
    {
        if (is_array($response)) {
            $PARSED      = array();
            $CURRENT     = null;
            $singlevalue = null;
            foreach ($response as $x) {
                if (in_array($x, array('!fatal','!re','!trap'))) {
                    if ($x == '!re') {
                        $CURRENT =& $PARSED[];
                    } else {
                        $CURRENT =& $PARSED[$x][];
                    }
                } elseif ($x != '!done') {
                    $MATCHES = array();
                    if (preg_match_all('/[^=]+/i', $x, $MATCHES)) {
                        if ($MATCHES[0][0] == 'ret') {
                            $singlevalue = $MATCHES[0][1];
                        }
                        $CURRENT[$MATCHES[0][0]] = (isset($MATCHES[0][1]) ? $MATCHES[0][1] : '');
                    }
                }
            }

            if (empty($PARSED) && !is_null($singlevalue)) {
                $PARSED = $singlevalue;
            }

            return $PARSED;
        } else {
            return array();
        }
    }


    /**
     * Parse response from Router OS
     *
     * @param array       $response   Response data
     *
     * @return array                  Array with parsed data
     */
    public function parseResponse4Smarty($response)
    {
        if (is_array($response)) {
            $PARSED      = array();
            $CURRENT     = null;
            $singlevalue = null;
            foreach ($response as $x) {
                if (in_array($x, array('!fatal','!re','!trap'))) {
                    if ($x == '!re') {
                        $CURRENT =& $PARSED[];
                    } else {
                        $CURRENT =& $PARSED[$x][];
                    }
                } elseif ($x != '!done') {
                    $MATCHES = array();
                    if (preg_match_all('/[^=]+/i', $x, $MATCHES)) {
                        if ($MATCHES[0][0] == 'ret') {
                            $singlevalue = $MATCHES[0][1];
                        }
                        $CURRENT[$MATCHES[0][0]] = (isset($MATCHES[0][1]) ? $MATCHES[0][1] : '');
                    }
                }
            }
            foreach ($PARSED as $key => $value) {
                $PARSED[$key] = $this->arrayChangeKeyName($value);
            }
            return $PARSED;
            if (empty($PARSED) && !is_null($singlevalue)) {
                $PARSED = $singlevalue;
            }
        } else {
            return array();
        }
    }


    /**
     * Change "-" and "/" from array key to "_"
     *
     * @param array       $array      Input array
     *
     * @return array                  Array with changed key names
     */
    public function arrayChangeKeyName(&$array)
    {
        if (is_array($array)) {
            foreach ($array as $k => $v) {
                $tmp = str_replace("-", "_", $k);
                $tmp = str_replace("/", "_", $tmp);
                if ($tmp) {
                    $array_new[$tmp] = $v;
                } else {
                    $array_new[$k] = $v;
                }
            }
            return $array_new;
        } else {
            return $array;
        }
    }


    /**
     * Read data from Router OS
     *
     * @param boolean     $parse      Parse the data? default: true
     *
     * @return array                  Array with parsed or unparsed data
     */
    public function read($parse = true)
    {
        $RESPONSE     = array();
        $receiveddone = false;
        while (true) {
            // Read the first byte of input which gives us some or all of the length
            // of the remaining reply.
            $BYTE   = ord(fread($this->socket, 1));
            $LENGTH = 0;
            // If the first bit is set then we need to remove the first four bits, shift left 8
            // and then read another byte in.
            // We repeat this for the second and third bits.
            // If the fourth bit is set, we need to remove anything left in the first byte
            // and then read in yet another byte.
            if ($BYTE & 128) {
                if (($BYTE & 192) == 128) {
                    $LENGTH = (($BYTE & 63) << 8) + ord(fread($this->socket, 1));
                } else {
                    if (($BYTE & 224) == 192) {
                        $LENGTH = (($BYTE & 31) << 8) + ord(fread($this->socket, 1));
                        $LENGTH = ($LENGTH << 8) + ord(fread($this->socket, 1));
                    } else {
                        if (($BYTE & 240) == 224) {
                            $LENGTH = (($BYTE & 15) << 8) + ord(fread($this->socket, 1));
                            $LENGTH = ($LENGTH << 8) + ord(fread($this->socket, 1));
                            $LENGTH = ($LENGTH << 8) + ord(fread($this->socket, 1));
                        } else {
                            $LENGTH = ord(fread($this->socket, 1));
                            $LENGTH = ($LENGTH << 8) + ord(fread($this->socket, 1));
                            $LENGTH = ($LENGTH << 8) + ord(fread($this->socket, 1));
                            $LENGTH = ($LENGTH << 8) + ord(fread($this->socket, 1));
                        }
                    }
                }
            } else {
                $LENGTH = $BYTE;
            }

            $_ = "";

            // If we have got more characters to read, read them in.
            if ($LENGTH > 0) {
                $_      = "";
                $retlen = 0;
                while ($retlen < $LENGTH) {
                    $toread = $LENGTH - $retlen;
                    $_ .= fread($this->socket, $toread);
                    $retlen = strlen($_);
                }
                $RESPONSE[] = $_;
                $this->debug('>>> [' . $retlen . '/' . $LENGTH . '] bytes read.');
            }

            // If we get a !done, make a note of it.
            if ($_ == "!done") {
                $receiveddone = true;
            }

            $STATUS = socket_get_status($this->socket);
            if ($LENGTH > 0) {
                $this->debug('>>> [' . $LENGTH . ', ' . $STATUS['unread_bytes'] . ']' . $_);
            }

            if ((!$this->connected && !$STATUS['unread_bytes']) || ($this->connected && !$STATUS['unread_bytes'] && $receiveddone)) {
                break;
            }
        }

        if ($parse) {
            $RESPONSE = $this->parseResponse($RESPONSE);
        }

        return $RESPONSE;
    }


    /**
     * Write (send) data to Router OS
     *
     * @param string      $command    A string with the command to send
     * @param mixed       $param2     If we set an integer, the command will send this data as a "tag"
     *                                If we set it to boolean true, the funcion will send the comand and finish
     *                                If we set it to boolean false, the funcion will send the comand and wait for next command
     *                                Default: true
     *
     * @return boolean                Return false if no command especified
     */
    public function write($command, $param2 = true)
    {
        if ($command) {
            $data = explode("\n", $command);
            foreach ($data as $com) {
                $com = trim($com);
                fwrite($this->socket, $this->encodeLength(strlen($com)) . $com);
                $this->debug('<<< [' . strlen($com) . '] ' . $com);
            }

            if (gettype($param2) == 'integer') {
                fwrite($this->socket, $this->encodeLength(strlen('.tag=' . $param2)) . '.tag=' . $param2 . chr(0));
                $this->debug('<<< [' . strlen('.tag=' . $param2) . '] .tag=' . $param2);
            } elseif (gettype($param2) == 'boolean') {
                fwrite($this->socket, ($param2 ? chr(0) : ''));
            }

            return true;
        } else {
            return false;
        }
    }


    /**
     * Write (send) data to Router OS
     *
     * @param string      $com        A string with the command to send
     * @param array       $arr        An array with arguments or queries
     *
     * @return array                  Array with parsed
     */
    public function comm($com, $arr = array())
    {
        $count = count($arr);
        $this->write($com, !$arr);
        $i = 0;
        if ($this->isIterable($arr)) {
            foreach ($arr as $k => $v) {
                switch ($k[0]) {
                    case "?":
                        $el = "$k=$v";
                        break;
                    case "~":
                        $el = "$k~$v";
                        break;
                    default:
                        $el = "=$k=$v";
                        break;
                }

                $last = ($i++ == $count - 1);
                $this->write($el, $last);
            }
        }

        return $this->read();
    }

    /**
     * Standard destructor
     *
     * @return void
     */
    public function __destruct()
    {
        $this->disconnect();
    }
}


File: /README.md
# mikrotik-php-api-hotspot-user-generator
Hotspot User Generator Mikrotik PHP API

Aplikasi manajemen user hotspot menggunakan Mikrotik PHP API. Memiliki kemampuan sbb:

1. Dapat membuat sebuah dan melakukan generate user hotspot melalui interface aplikasi
2. Dapat memanagement bandwdith user melalui interface aplikasi
3. Dapat mengatur waktu akses ke jaringan hotspot melalui antarmuka aplikasi
4. Mencetak user yang telah digenerate menjadi file *.pdf
5. mengeksport user yang telah di generate menjadi file excel (*.xls)


