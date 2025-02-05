# Repository Information
Name: ips-mikrotik-suricata

# Directory Structure
Directory structure:
└── github_repos/ips-mikrotik-suricata/
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
    │   │       ├── pack-4b2510d2829be9ace4fa3d756b6c2f5c03a34277.idx
    │   │       └── pack-4b2510d2829be9ace4fa3d756b6c2f5c03a34277.pack
    │   ├── packed-refs
    │   └── refs/
    │       ├── heads/
    │       │   └── master
    │       ├── remotes/
    │       │   └── origin/
    │       │       └── HEAD
    │       └── tags/
    ├── config.php
    ├── functions.php
    ├── images/
    ├── ips_start.sh
    ├── LICENSE
    ├── mikrotik-ips-clean.php
    ├── mikrotik-ips-cron.php
    ├── mikrotik-ips-install.php
    ├── README
    ├── README.EN
    ├── README.ES
    ├── schema.sql
    └── share/
        └── routeros_api.php


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
	url = https://github.com/elmaxid/ips-mikrotik-suricata.git
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
0000000000000000000000000000000000000000 5a9379089fb5b9c121c1025341b2ad3aac17dfcb vivek-dodia <vivek.dodia@icloud.com> 1738605811 -0500	clone: from https://github.com/elmaxid/ips-mikrotik-suricata.git


File: /.git\logs\refs\heads\master
0000000000000000000000000000000000000000 5a9379089fb5b9c121c1025341b2ad3aac17dfcb vivek-dodia <vivek.dodia@icloud.com> 1738605811 -0500	clone: from https://github.com/elmaxid/ips-mikrotik-suricata.git


File: /.git\logs\refs\remotes\origin\HEAD
0000000000000000000000000000000000000000 5a9379089fb5b9c121c1025341b2ad3aac17dfcb vivek-dodia <vivek.dodia@icloud.com> 1738605811 -0500	clone: from https://github.com/elmaxid/ips-mikrotik-suricata.git


File: /.git\packed-refs
# pack-refs with: peeled fully-peeled sorted 
5a9379089fb5b9c121c1025341b2ad3aac17dfcb refs/remotes/origin/master


File: /.git\refs\heads\master
5a9379089fb5b9c121c1025341b2ad3aac17dfcb


File: /.git\refs\remotes\origin\HEAD
ref: refs/remotes/origin/master


File: /config.php
<?php
// header( 'Content-Type: text/plain' );
/* Database username */
$user_name    = "xxxxxxx";
/* Database password */
$password     = "xxxxxxxxxx";
$database     = "snorby";
$server       = "localhost";
$PID_app_file = '/tmp/ips_mikrotik.pid';
$PID_reload_file = '/tmp/ips_mikrotik_reload.pid'; //para recargar las reglas



// TELEGRAM API
$url_api_telegram="https://api.telegram.org/botXXXXXXXX:XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/sendMessage?chat_id=XXXXXXXXXXX&text=";
$active_api_telegram=false; //true para funcionar

//mail report
$active_mail_report=false;

$cfg[ 'whitelist' ] = array('10.10.','192.168.','172.16','1.1.1.'); //whiteliist ,'82.165.177.154'

$router['ip']="10.200.200.1"; //IP Router
$router['user']="xxxx"; // user login
$router['pass']="xxxxxx";  //pass
?>

File: /functions.php
<?php


/**
 * [get_signature obtiene las firmas que se utilizaran para IPS]
 * @return [type] [description]
 */
function get_signature( ) {
    global $db;
    $SQL = "SELECT  sig_name,src_or_dst,timeout  FROM sigs_to_block LIMIT 100;"; //limit to 100 
    if ( !$result = $db->query( $SQL ) ) {
        die( 'There was an error running the query [' . $db->error . ']' );
    } //!$result = $db->query( $SQL )
    $i = 0;
    while ( $row = $result->fetch_assoc() ) {
        // echo var_dump($row);
        $ret[ $i ][ 'sig_name' ]   = $row[ 'sig_name' ];
        $ret[ $i ][ 'src_or_dst' ] = $row[ 'src_or_dst' ];
        $ret[ $i ][ 'timeout' ]    = $row[ 'timeout' ];
        $i++;
    } //$row = $result->fetch_assoc()
    mysqli_free_result( $result );
    return $ret;
}
/**
 * [save_to_db_block guarda en la DB el bloqueo si no existe el IP en la lista. El mantenimiento de la misma la realiza otro agente]
 * @param  [array] $array_to_db [array con los datos a guardar en DB]
 * @return [type]              [description]
 */
function save_to_db_block( $array_to_db = NULL ) {
    global $db;
    if ( !$array_to_db )
        return false;
    $sql = "INSERT INTO block_queue (que_ip_adr, que_sig_name, que_sig_sid,que_timeout,que_event_timestamp)
              SELECT * FROM (SELECT '$array_to_db[que_ip_adr]', '$array_to_db[que_sig_name]', '$array_to_db[que_sig_sid]','$array_to_db[que_timeout]','$array_to_db[que_event_timestamp]') AS tmp
        WHERE NOT EXISTS ( SELECT que_ip_adr FROM block_queue WHERE que_ip_adr = '$array_to_db[que_ip_adr]'  ) LIMIT 1;";
    // $sql="INSERT INTO block_queue (que_ip_adr, que_sig_name, que_sig_sid,que_timeout)
    //             SELECT * FROM (SELECT '$array_to_db[que_ip_adr]', '$array_to_db[que_sig_name]', '$array_to_db[que_sig_sid]','$array_to_db[que_timeout]') AS tmp 
    //      WHERE   (SELECT que_processed FROM block_queue WHERE que_ip_adr = '$array_to_db[que_ip_adr]' ) != 0";
    //  echo $sql;
    if ( !$result = $db->query( $sql ) ) {
        die( 'There was an error running the query [' . $db->error . ']' );
    } //!$result = $db->query( $sql )
    //    while($row = $result->fetch_assoc())  echo $row;
    //  mysqli_free_result($result);
}
/**
 * [get_text_to_report hace el formato de la linea de texto a agregar como comentario en el address list]
 * @param  [type] $row                [description]
 * @param  [type] $ARRAY_sig_to_block [description]
 * @return [type]                     [description]
 */
function get_text_to_report( $row, $ARRAY_sig_to_block ) {
    $msg_TXT = "From Suricata:  $row[sig_name] -> $row[sid]:$row[signature] -> event Timestamp: $row[timestamp] ->IP " . $ARRAY_sig_to_block[ 'src_or_dst' ] . " ntoa : " . $row[ 'ip_' . $ARRAY_sig_to_block[ 'src_or_dst' ] ] . " " . $row[ $ARRAY_sig_to_block[ 'src_or_dst' ] ] . " -> Timeout: " . $ARRAY_sig_to_block[ 'timeout' ];
    return $msg_TXT;
}
/**
 * [array_search_partial busca un string en un valor de un array y devuelve el key]
 * @param  [type] $arr     [description]
 * @param  [type] $keyword [description]
 * @return [type]          [description]
 */
function array_search_partial( $arr, $keyword ) {      
    foreach ( $arr as $index => $string ) {      
        if ( strpos( $keyword , $string) !== FALSE )   return $index;
    } //$arr as $index => $string
}
/**
 * [get_last_event ontiene el ultimo valor del evento para empezar a buscar por nuevas incidencias]
 * @return [type] [description]
 */
function get_last_event( ) {
    global $db;
    $SQL = "SELECT  id  FROM events_with_join order by id desc LIMIT 1;"; // get the last event
    if ( !$result = $db->query( $SQL ) ) {
        die( 'There was an error running the query [' . $db->error . ']' );
    } //!$result = $db->query( $SQL )
    $i   = 0;
    $row = $result->fetch_assoc();
    mysqli_free_result( $result );
    return $row[ id ];
}


/**
 * [send_to_telegram Envia el Alerta por Telegram]
 * @param  [type] $text [description]
 * @return [type]       [description]
 */
function send_to_telegram($text) {
        global   $url_api_telegram;  
    $fetch=file_get_contents($url_api_telegram.$text);
    // echo $fetch;
   $ret_fetch=json_decode($fetch,true);
    // echo var_dump($ret_fetch);
   if ($ret_fetch[ok]) {
        // echo "Enviado con exito";
        return true;
   }
  
}

?>

File: /ips_start.sh
File: /LICENSE
                    GNU GENERAL PUBLIC LICENSE
                       Version 2, June 1991

 Copyright (C) 1989, 1991 Free Software Foundation, Inc., <http://fsf.org/>
 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA
 Everyone is permitted to copy and distribute verbatim copies
 of this license document, but changing it is not allowed.

                            Preamble

  The licenses for most software are designed to take away your
freedom to share and change it.  By contrast, the GNU General Public
License is intended to guarantee your freedom to share and change free
software--to make sure the software is free for all its users.  This
General Public License applies to most of the Free Software
Foundation's software and to any other program whose authors commit to
using it.  (Some other Free Software Foundation software is covered by
the GNU Lesser General Public License instead.)  You can apply it to
your programs, too.

  When we speak of free software, we are referring to freedom, not
price.  Our General Public Licenses are designed to make sure that you
have the freedom to distribute copies of free software (and charge for
this service if you wish), that you receive source code or can get it
if you want it, that you can change the software or use pieces of it
in new free programs; and that you know you can do these things.

  To protect your rights, we need to make restrictions that forbid
anyone to deny you these rights or to ask you to surrender the rights.
These restrictions translate to certain responsibilities for you if you
distribute copies of the software, or if you modify it.

  For example, if you distribute copies of such a program, whether
gratis or for a fee, you must give the recipients all the rights that
you have.  You must make sure that they, too, receive or can get the
source code.  And you must show them these terms so they know their
rights.

  We protect your rights with two steps: (1) copyright the software, and
(2) offer you this license which gives you legal permission to copy,
distribute and/or modify the software.

  Also, for each author's protection and ours, we want to make certain
that everyone understands that there is no warranty for this free
software.  If the software is modified by someone else and passed on, we
want its recipients to know that what they have is not the original, so
that any problems introduced by others will not reflect on the original
authors' reputations.

  Finally, any free program is threatened constantly by software
patents.  We wish to avoid the danger that redistributors of a free
program will individually obtain patent licenses, in effect making the
program proprietary.  To prevent this, we have made it clear that any
patent must be licensed for everyone's free use or not licensed at all.

  The precise terms and conditions for copying, distribution and
modification follow.

                    GNU GENERAL PUBLIC LICENSE
   TERMS AND CONDITIONS FOR COPYING, DISTRIBUTION AND MODIFICATION

  0. This License applies to any program or other work which contains
a notice placed by the copyright holder saying it may be distributed
under the terms of this General Public License.  The "Program", below,
refers to any such program or work, and a "work based on the Program"
means either the Program or any derivative work under copyright law:
that is to say, a work containing the Program or a portion of it,
either verbatim or with modifications and/or translated into another
language.  (Hereinafter, translation is included without limitation in
the term "modification".)  Each licensee is addressed as "you".

Activities other than copying, distribution and modification are not
covered by this License; they are outside its scope.  The act of
running the Program is not restricted, and the output from the Program
is covered only if its contents constitute a work based on the
Program (independent of having been made by running the Program).
Whether that is true depends on what the Program does.

  1. You may copy and distribute verbatim copies of the Program's
source code as you receive it, in any medium, provided that you
conspicuously and appropriately publish on each copy an appropriate
copyright notice and disclaimer of warranty; keep intact all the
notices that refer to this License and to the absence of any warranty;
and give any other recipients of the Program a copy of this License
along with the Program.

You may charge a fee for the physical act of transferring a copy, and
you may at your option offer warranty protection in exchange for a fee.

  2. You may modify your copy or copies of the Program or any portion
of it, thus forming a work based on the Program, and copy and
distribute such modifications or work under the terms of Section 1
above, provided that you also meet all of these conditions:

    a) You must cause the modified files to carry prominent notices
    stating that you changed the files and the date of any change.

    b) You must cause any work that you distribute or publish, that in
    whole or in part contains or is derived from the Program or any
    part thereof, to be licensed as a whole at no charge to all third
    parties under the terms of this License.

    c) If the modified program normally reads commands interactively
    when run, you must cause it, when started running for such
    interactive use in the most ordinary way, to print or display an
    announcement including an appropriate copyright notice and a
    notice that there is no warranty (or else, saying that you provide
    a warranty) and that users may redistribute the program under
    these conditions, and telling the user how to view a copy of this
    License.  (Exception: if the Program itself is interactive but
    does not normally print such an announcement, your work based on
    the Program is not required to print an announcement.)

These requirements apply to the modified work as a whole.  If
identifiable sections of that work are not derived from the Program,
and can be reasonably considered independent and separate works in
themselves, then this License, and its terms, do not apply to those
sections when you distribute them as separate works.  But when you
distribute the same sections as part of a whole which is a work based
on the Program, the distribution of the whole must be on the terms of
this License, whose permissions for other licensees extend to the
entire whole, and thus to each and every part regardless of who wrote it.

Thus, it is not the intent of this section to claim rights or contest
your rights to work written entirely by you; rather, the intent is to
exercise the right to control the distribution of derivative or
collective works based on the Program.

In addition, mere aggregation of another work not based on the Program
with the Program (or with a work based on the Program) on a volume of
a storage or distribution medium does not bring the other work under
the scope of this License.

  3. You may copy and distribute the Program (or a work based on it,
under Section 2) in object code or executable form under the terms of
Sections 1 and 2 above provided that you also do one of the following:

    a) Accompany it with the complete corresponding machine-readable
    source code, which must be distributed under the terms of Sections
    1 and 2 above on a medium customarily used for software interchange; or,

    b) Accompany it with a written offer, valid for at least three
    years, to give any third party, for a charge no more than your
    cost of physically performing source distribution, a complete
    machine-readable copy of the corresponding source code, to be
    distributed under the terms of Sections 1 and 2 above on a medium
    customarily used for software interchange; or,

    c) Accompany it with the information you received as to the offer
    to distribute corresponding source code.  (This alternative is
    allowed only for noncommercial distribution and only if you
    received the program in object code or executable form with such
    an offer, in accord with Subsection b above.)

The source code for a work means the preferred form of the work for
making modifications to it.  For an executable work, complete source
code means all the source code for all modules it contains, plus any
associated interface definition files, plus the scripts used to
control compilation and installation of the executable.  However, as a
special exception, the source code distributed need not include
anything that is normally distributed (in either source or binary
form) with the major components (compiler, kernel, and so on) of the
operating system on which the executable runs, unless that component
itself accompanies the executable.

If distribution of executable or object code is made by offering
access to copy from a designated place, then offering equivalent
access to copy the source code from the same place counts as
distribution of the source code, even though third parties are not
compelled to copy the source along with the object code.

  4. You may not copy, modify, sublicense, or distribute the Program
except as expressly provided under this License.  Any attempt
otherwise to copy, modify, sublicense or distribute the Program is
void, and will automatically terminate your rights under this License.
However, parties who have received copies, or rights, from you under
this License will not have their licenses terminated so long as such
parties remain in full compliance.

  5. You are not required to accept this License, since you have not
signed it.  However, nothing else grants you permission to modify or
distribute the Program or its derivative works.  These actions are
prohibited by law if you do not accept this License.  Therefore, by
modifying or distributing the Program (or any work based on the
Program), you indicate your acceptance of this License to do so, and
all its terms and conditions for copying, distributing or modifying
the Program or works based on it.

  6. Each time you redistribute the Program (or any work based on the
Program), the recipient automatically receives a license from the
original licensor to copy, distribute or modify the Program subject to
these terms and conditions.  You may not impose any further
restrictions on the recipients' exercise of the rights granted herein.
You are not responsible for enforcing compliance by third parties to
this License.

  7. If, as a consequence of a court judgment or allegation of patent
infringement or for any other reason (not limited to patent issues),
conditions are imposed on you (whether by court order, agreement or
otherwise) that contradict the conditions of this License, they do not
excuse you from the conditions of this License.  If you cannot
distribute so as to satisfy simultaneously your obligations under this
License and any other pertinent obligations, then as a consequence you
may not distribute the Program at all.  For example, if a patent
license would not permit royalty-free redistribution of the Program by
all those who receive copies directly or indirectly through you, then
the only way you could satisfy both it and this License would be to
refrain entirely from distribution of the Program.

If any portion of this section is held invalid or unenforceable under
any particular circumstance, the balance of the section is intended to
apply and the section as a whole is intended to apply in other
circumstances.

It is not the purpose of this section to induce you to infringe any
patents or other property right claims or to contest validity of any
such claims; this section has the sole purpose of protecting the
integrity of the free software distribution system, which is
implemented by public license practices.  Many people have made
generous contributions to the wide range of software distributed
through that system in reliance on consistent application of that
system; it is up to the author/donor to decide if he or she is willing
to distribute software through any other system and a licensee cannot
impose that choice.

This section is intended to make thoroughly clear what is believed to
be a consequence of the rest of this License.

  8. If the distribution and/or use of the Program is restricted in
certain countries either by patents or by copyrighted interfaces, the
original copyright holder who places the Program under this License
may add an explicit geographical distribution limitation excluding
those countries, so that distribution is permitted only in or among
countries not thus excluded.  In such case, this License incorporates
the limitation as if written in the body of this License.

  9. The Free Software Foundation may publish revised and/or new versions
of the General Public License from time to time.  Such new versions will
be similar in spirit to the present version, but may differ in detail to
address new problems or concerns.

Each version is given a distinguishing version number.  If the Program
specifies a version number of this License which applies to it and "any
later version", you have the option of following the terms and conditions
either of that version or of any later version published by the Free
Software Foundation.  If the Program does not specify a version number of
this License, you may choose any version ever published by the Free Software
Foundation.

  10. If you wish to incorporate parts of the Program into other free
programs whose distribution conditions are different, write to the author
to ask for permission.  For software which is copyrighted by the Free
Software Foundation, write to the Free Software Foundation; we sometimes
make exceptions for this.  Our decision will be guided by the two goals
of preserving the free status of all derivatives of our free software and
of promoting the sharing and reuse of software generally.

                            NO WARRANTY

  11. BECAUSE THE PROGRAM IS LICENSED FREE OF CHARGE, THERE IS NO WARRANTY
FOR THE PROGRAM, TO THE EXTENT PERMITTED BY APPLICABLE LAW.  EXCEPT WHEN
OTHERWISE STATED IN WRITING THE COPYRIGHT HOLDERS AND/OR OTHER PARTIES
PROVIDE THE PROGRAM "AS IS" WITHOUT WARRANTY OF ANY KIND, EITHER EXPRESSED
OR IMPLIED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF
MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE.  THE ENTIRE RISK AS
TO THE QUALITY AND PERFORMANCE OF THE PROGRAM IS WITH YOU.  SHOULD THE
PROGRAM PROVE DEFECTIVE, YOU ASSUME THE COST OF ALL NECESSARY SERVICING,
REPAIR OR CORRECTION.

  12. IN NO EVENT UNLESS REQUIRED BY APPLICABLE LAW OR AGREED TO IN WRITING
WILL ANY COPYRIGHT HOLDER, OR ANY OTHER PARTY WHO MAY MODIFY AND/OR
REDISTRIBUTE THE PROGRAM AS PERMITTED ABOVE, BE LIABLE TO YOU FOR DAMAGES,
INCLUDING ANY GENERAL, SPECIAL, INCIDENTAL OR CONSEQUENTIAL DAMAGES ARISING
OUT OF THE USE OR INABILITY TO USE THE PROGRAM (INCLUDING BUT NOT LIMITED
TO LOSS OF DATA OR DATA BEING RENDERED INACCURATE OR LOSSES SUSTAINED BY
YOU OR THIRD PARTIES OR A FAILURE OF THE PROGRAM TO OPERATE WITH ANY OTHER
PROGRAMS), EVEN IF SUCH HOLDER OR OTHER PARTY HAS BEEN ADVISED OF THE
POSSIBILITY OF SUCH DAMAGES.

                     END OF TERMS AND CONDITIONS

            How to Apply These Terms to Your New Programs

  If you develop a new program, and you want it to be of the greatest
possible use to the public, the best way to achieve this is to make it
free software which everyone can redistribute and change under these terms.

  To do so, attach the following notices to the program.  It is safest
to attach them to the start of each source file to most effectively
convey the exclusion of warranty; and each file should have at least
the "copyright" line and a pointer to where the full notice is found.

    {description}
    Copyright (C) {year}  {fullname}

    This program is free software; you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation; either version 2 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License along
    with this program; if not, write to the Free Software Foundation, Inc.,
    51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.

Also add information on how to contact you by electronic and paper mail.

If the program is interactive, make it output a short notice like this
when it starts in an interactive mode:

    Gnomovision version 69, Copyright (C) year name of author
    Gnomovision comes with ABSOLUTELY NO WARRANTY; for details type `show w'.
    This is free software, and you are welcome to redistribute it
    under certain conditions; type `show c' for details.

The hypothetical commands `show w' and `show c' should show the appropriate
parts of the General Public License.  Of course, the commands you use may
be called something other than `show w' and `show c'; they could even be
mouse-clicks or menu items--whatever suits your program.

You should also get your employer (if you work as a programmer) or your
school, if any, to sign a "copyright disclaimer" for the program, if
necessary.  Here is a sample; alter the names:

  Yoyodyne, Inc., hereby disclaims all copyright interest in the program
  `Gnomovision' (which makes passes at compilers) written by James Hacker.

  {signature of Ty Coon}, 1 April 1989
  Ty Coon, President of Vice

This General Public License does not permit incorporating your program into
proprietary programs.  If your program is a subroutine library, you may
consider it more useful to permit linking proprietary applications with the
library.  If this is what you want to do, use the GNU Lesser General
Public License instead of this License.


File: /mikrotik-ips-clean.php
<?php

/*****************************
 *
 * IPS MikroTik Suricata
 *
 * This script is the daemon to clean DB
 * 
 * Author: Maximiliano Dobladez info@mkesolutions.net
 *
 * http://maxid.com.ar | http://www.mkesolutions.net  
 *
 * for API MIKROTIK:
 * http://www.mikrotik.com
 * http://wiki.mikrotik.com/wiki/API_PHP_class
 *
 * Inspired on: http://forum.mikrotik.com/viewtopic.php?t=111727
 *
 * LICENSE: GPLv2 GNU GENERAL PUBLIC LICENSE
 *
 * v1.2 - 3 March 17 - This script mikrotik-ips-daemon_db.php is depreceated because now we use trigger on DB
 * v1.1 - 10 Feb 17 - add support telegram, multiple whitelist,
 * v1.0 - 2 Feb 17 - initial version
 ******************************/


$DEBUG = false;
// $DEBUG=true;
if ( !$DEBUG )
    error_reporting( 0 );
require 'functions.php';
require 'config.php';
/* Wait for a connection to the database */
$i = 0;
while ( $i < 100 ) {
    $db_ = new mysqli( $server, $user_name, $password, $database );
    if ( $db_->connect_errno > 0 ) {
        print( 'Unable to connect to database [' . $db_->connect_error . ']' );
        sleep( 10 );
        $i = $i + 10;
    } //$db_->connect_errno > 0
    else {
        $i = 100;
        touch( $PID_app_file );
    }
} //$i < 100
while ( file_exists( $PID_app_file ) ) {
    // Borra los bloqueos procesados que tenga como fecha la hora de agregado mas el timeout para eliminarlo y que se vuelva a agregar luego 
    $SQL = "DELETE FROM block_queue WHERE  que_processed=1 AND (que_added + INTERVAL que_timeout HOUR_SECOND) <= NOW()  ;";
    if ( !$result = $db_->query( $SQL ) ) {
        die( 'There was an error running the query [' . $db_->error . ']' );
    } //!$result = $db_->query( $SQL )
    mysqli_free_result( $result );
    sleep( 10 );
    /* Sleep 10 seconds then do again */
    mysqli_ping( $db_ );
} //file_exists( $PID_app_file )
echo "Shutdown services Clean DB\n";
unlink( $PID_app_file );
$db_->close();
?>

File: /mikrotik-ips-cron.php
<?php

/*****************************
 *
 * IPS MikroTik Suricata
 *
 * This script is the daemon to clean DB
 * 
 * Author: Maximiliano Dobladez info@mkesolutions.net
 *
 * http://maxid.com.ar | http://www.mkesolutions.net  
 *
 * for API MIKROTIK:
 * http://www.mikrotik.com
 * http://wiki.mikrotik.com/wiki/API_PHP_class
 *
 * Inspired on: http://forum.mikrotik.com/viewtopic.php?t=111727
 *
 * LICENSE: GPLv2 GNU GENERAL PUBLIC LICENSE
 *
 * v1.2 - 3 March 17 - This script mikrotik-ips-daemon_db.php is depreceated because now we use trigger on DB
 * v1.1 - 10 Feb 17 - add support telegram, multiple whitelist,
 * v1.0 - 2 Feb 17 - initial version
 ******************************/


$DEBUG = false;
// $DEBUG=true;
if ( !$DEBUG )
    error_reporting( 0 );
require( 'share/routeros_api.php' );
$API = new RouterosAPI();
require 'functions.php';
require 'config.php';

/* Wait for a connection to the database */
$i                  = 0;
while ( $i < 100 ) {
    $db_ = new mysqli( $server, $user_name, $password, $database );
    if ( $db_->connect_errno > 0 ) {
        print( 'Unable to connect to database [' . $db_->connect_error . ']' );
        sleep( 10 );
        $i = $i + 10;
    } //$db_->connect_errno > 0
    else {
        $i = 100;
        touch( $PID_app_file );
    }
} //$i < 100
while ( file_exists( $PID_app_file ) ) {
    $SQL = "SELECT *,inet_ntoa(que_ip_adr) as ip FROM block_queue WHERE que_processed = 0 LIMIT 10;";
    if ( !$result = $db_->query( $SQL ) ) {
        die( 'There was an error running the query [' . $db_->error . ']' );
    } //!$result = $db_->query( $SQL )
    while ( $row = $result->fetch_assoc() ) {
        // if ( strpos( $row[ 'que_ip_adr' ], $cfg[ 'whitelist' ] ) !== true ) {
        if (!   array_search_partial($cfg[ 'whitelist' ],$row[ 'ip' ])) {
            /* Does not match local address... */
            try {
                $API->connect( $router['ip'], $router['user'], $router['pass'] );
            }
            catch ( Exception $e ) {
                die( 'Unable to connect to RouterOS. Error:' . $e );
            }
            /* Now add the address into the Blocked address-list group */
            $comment_tmp="From suricata, " . $row[ 'que_sig_name' ] . " => " . $row[ 'que_sig_gid' ] . ":" . $row[ 'que_sig_sid' ] . " => event timestamp: " . $row[ 'que_event_timestamp' ] ;
            $API->comm( "/ip/firewall/address-list/add", array(
                 "list" => "Blocked",
                "address" => $row[ 'ip' ],
                "timeout" => $row[ 'que_timeout' ],
                "comment" => $comment_tmp
            ) );
            $API->disconnect();
            //si esta activo el api de telegram, avisar
            if ($active_api_telegram) {
                $comment_tmp.=" => IP: ".$row['ip'] . " => Timeout: ".$row[ 'que_timeout' ];
                send_to_telegram($comment_tmp);
            }
            //si esta activo el mail envio por correo el alerta
            if ($active_mail_report) {
                    /* Send email indicating bad block attempt*/
                    $to      = 'noreply@gmail.com';
                    $subject = 'Suricata on snort-host: attempted block on local address';
                    $message = 'A record in the block_queue indicated a block on a local IP Address (' . $row[ 'ip' ] . ")\r\n";
                    $message = $message . "\r\n";
                    $message = $message . "The signature ID is " . $row[ 'que_sig_id' ] . " named: " . $row[ 'que_sig_name' ] . "\r\n";
                    $message = $message . "    with a que_id of " . $row[ 'que_id' ] . "\r\n\r\n";
                    $message = $message . "Check the src_or_dst field in events_to_block for the signature to make sure it is correct (src/dst).\r\n\r\n";
                    $message = $message . "The record was not processed but marked as completed.\r\n";
                    $headers = 'From: noreply@gmail.com' . "\r\n" . 'Reply-To: noreply@gmail.com' . "\r\n" . 'X-Mailer: PHP/' . phpversion();
                    // mail($to, $subject, $message, $headers);                
            }
        }  
        else {
          // echo "Exception";
        }
        $SQL2 = "UPDATE block_queue set que_processed = 1 WHERE que_id = " . $row[ 'que_id' ] . ";";
        if ( !$result2 = $db_->query( $SQL2 ) ) {
            die( 'There was an error running the query [' . $db_->error . ']' );
        } //!$result2 = $db_->query( $SQL2 )
        mysqli_free_result( $result2 );
    } //eof while
    mysqli_free_result( $result );
    sleep( 2 );
    /* Sleep 2 seconds then do again */
    mysqli_ping( $db_ );
} //file_exists( $PID_app_file )
echo "Shutdown services cron\n";
unlink( $PID_app_file );
$db_->close();

?>

File: /mikrotik-ips-install.php
<?php

/*****************************
 *
 * IPS MikroTik Suricata
 *
 * This script is the daemon to clean DB
 * 
 * Author: Maximiliano Dobladez info@mkesolutions.net
 *
 * http://maxid.com.ar | http://www.mkesolutions.net  
 *
 * for API MIKROTIK:
 * http://www.mikrotik.com
 * http://wiki.mikrotik.com/wiki/API_PHP_class
 *
 * Inspired on: http://forum.mikrotik.com/viewtopic.php?t=111727
 *
 * LICENSE: GPLv2 GNU GENERAL PUBLIC LICENSE
 *
 * v1.2 - 3 March 17 - This script mikrotik-ips-daemon_db.php is depreceated because now we use trigger on DB
 * v1.1 - 10 Feb 17 - add support telegram, multiple whitelist,
 * v1.0 - 2 Feb 17 - initial version
 ******************************/


$DEBUG = false;
// $DEBUG=true;
if ( !$DEBUG )
    error_reporting( 0 );
require( 'share/routeros_api.php' );
$API = new RouterosAPI();
require 'config.php';
/* Wait for a connection to the database */
$db_ = new mysqli( $server, $user_name, $password, $database );
if ( $db_->connect_errno > 0 )
    die( 'Unable to connect to database [' . $db_->connect_error . ']' );
echo "Connect OK - DB MySQL\n";
if ( isset( $router[ 'ip' ] ) ) {
    try {
        $API->connect( $router[ 'ip' ], $router[ 'user' ], $router[ 'pass' ] );
    }
    catch ( Exception $e ) {
        die( 'Unable to connect to RouterOS. Error:' . $e );
    }
    echo "Connect OK - API MikroTik RouterOS\n";
} //isset( $router[ 'ip' ] )

/*
$SQL_DB = "              DROP TABLE IF EXISTS `block_queue`;";
if ( !$result = $db_->query( $SQL_DB ) ) {
    die( 'There was an error running the query [' . $db_->error . ']' );
} //!$result = $db_->query( $SQL_DB )
$SQL_DB = " 
                    CREATE TABLE `block_queue` (
                      `que_id` int(11) NOT NULL AUTO_INCREMENT,
                      `que_added` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT 'When the block was added',
                      `que_ip_adr` varchar(64) COLLATE utf8_unicode_ci NOT NULL COMMENT 'The IP address to block',
                      `que_timeout` varchar(12) COLLATE utf8_unicode_ci NOT NULL COMMENT 'How long to block for',
                      `que_sig_name` varchar(256) COLLATE utf8_unicode_ci NOT NULL COMMENT 'The name of the signature that caused the block',
                      `que_sig_gid` int(10) NOT NULL COMMENT 'The signature group ID',
                      `que_sig_sid` int(10) NOT NULL COMMENT 'The signature ID',
                      `que_event_timestamp` timestamp NOT NULL DEFAULT '0000-00-00 00:00:00' COMMENT 'When the event was triggered',
                      `que_processed` int(11) NOT NULL DEFAULT '0' COMMENT 'If this item has been processed (0=no, <>0=yes)',
                      PRIMARY KEY (`que_id`),
                      KEY `que_added` (`que_added`)
                    ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci COMMENT='Queue of ip addresses to block on firewall';";
if ( !$result = $db_->query( $SQL_DB ) ) {
    die( 'There was an error running the query [' . $db_->error . ']' );
} //!$result = $db_->query( $SQL_DB )
$SQL_DB = "                     DROP TABLE IF EXISTS `sigs_to_block`;";
if ( !$result = $db_->query( $SQL_DB ) ) {
    die( 'There was an error running the query [' . $db_->error . ']' );
} //!$result = $db_->query( $SQL_DB )
$SQL_DB = " 
                    CREATE TABLE `sigs_to_block` (
                      `sig_name` text COLLATE utf8_unicode_ci NOT NULL,
                      `src_or_dst` char(3) COLLATE utf8_unicode_ci NOT NULL DEFAULT 'src',
                      `timeout` varchar(12) COLLATE utf8_unicode_ci NOT NULL DEFAULT '01:00:00',
                      UNIQUE KEY `sig_name_unique_index` (`sig_name`(64))
                    ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;";
if ( !$result = $db_->query( $SQL_DB ) ) {
    die( 'There was an error running the query [' . $db_->error . ']' );
} //!$result = $db_->query( $SQL_DB )
$SQL_DB = " 
                    INSERT INTO `sigs_to_block` (`sig_name`, `src_or_dst`, `timeout`) VALUES
                    ('ET COMPROMISED Known Compromised or Hostile Host Traffic',    'src',  '01:00:00'),
                    ('ET POLICY Suspicious inbound to', 'src',  '01:00:00'),
                    ('ET DROP Dshield Block Listed Source', 'src',  '01:00:00'),
                    ('ET SCAN Sipvicious Scan', 'src',  '01:00:00'),
                    ('ET SCAN Sipvicious User-Agent Detected (friendly-scanner)',   'src',  '01:00:00'),
                    ('ET DROP Spamhaus DROP Listed Traffic Inbound',    'src',  '01:00:00'),
                    ('ET POLICY Outgoing Basic Auth Base64 HTTP Password detected unencrypted', 'dst',  '23:59:59'),
                    ('ET CINS Active Threat Intelligence Poor Reputation IP',   'src',  '01:00:00'),
                    ('GPL SNMP public access udp',  'src',  '01:00:00'),
                    ('ET TOR Known Tor Relay/Router (Not Exit) Node Traffic',   'src',  '01:00:00'),
                    ('GPL DNS named version attempt',   'src',  '01:00:00'),
                    ('ET VOIP Modified Sipvicious Asterisk PBX User-Agent', 'src',  '01:00:00'),
                    ('GPL RPC xdmcp info query',    'src',  '01:00:00'),
                    ('GPL RPC portmap listing UDP 111', 'src',  '01:00:00'),
                    ('GPL ATTACK_RESPONSE id check returned root',  'src',  '00:01:10'),
                    ('ET VOIP Multiple Unauthorized SIP Responses UDP', 'dst',  '00:59:59'),
                    ('ET POLICY Suspicious inbound to mySQL port 3306', 'src',  '00:10:00'),
                    ('ET SCAN Behavioral Unusually fast Terminal Server Traffic, Potential Scan or Infection (Inbound)',    'src',  '00:10:00'),
                    ('ET DOS Possible NTP DDoS Inbound Frequent',   'src',  '00:10:00'),
                    ('ET SCAN SipCLI VOIP Scan',    'src',  '01:00:00'); ";



if ( !$result = $db_->query( $SQL_DB ) ) {
    die( 'There was an error running the query [' . $db_->error . ']' );
} //!$result = $db_->query( $SQL_DB )
echo "Create Schema MySQL OK \n";



   $SQL_DB = ' 
                    DROP TRIGGER `after_iphdr_insert`;
                      DELIMITER ;;
                      CREATE TRIGGER `after_iphdr_insert` AFTER INSERT ON `iphdr` FOR EACH ROW
                      BEGIN
                        DECLARE this_event INT(11) default 0;
                        DECLARE this_event_signature INT(10) default 0;
                        DECLARE this_event_timestamp TIMESTAMP;
                        DECLARE this_sig INT(10) default 0;
                        DECLARE this_sig_name VARCHAR(256) default "";
                        DECLARE this_sig_gid INT(10) default 0;
                        DECLARE timeout VARCHAR(12) default "";
                        DECLARE interested INT default 0;
                        DECLARE direction VARCHAR(3) default "";
                        DECLARE ip_src VARCHAR(64) default "";
                        DECLARE ip_dst VARCHAR(64) default "";
                        SELECT event.id, event.signature, event.timestamp
                        INTO this_event, this_event_signature, this_event_timestamp
                        FROM event
                        WHERE event.sid = NEW.sid and event.cid = NEW.cid;  
                        SELECT signature.sig_sid, signature.sig_gid, signature.sig_name 
                        INTO this_sig, this_sig_gid, this_sig_name
                        FROM signature
                        WHERE signature.sig_id = this_event_signature;
                        SELECT count(*), sigs_to_block.src_or_dst, sigs_to_block.timeout
                        INTO interested, direction, timeout
                        FROM sigs_to_block
                        WHERE this_sig_name LIKE CONCAT(sigs_to_block.sig_name, '%');
                        IF (interested > 0) THEN
                         IF (direction = "src") THEN
                            INSERT INTO block_queue
                         SET que_ip_adr =NEW.ip_src,
                                que_timeout = timeout,
                                que_sig_name = this_sig_name,
                                que_sig_gid = this_sig_gid,
                                que_sig_sid = this_sig,
                                que_event_timestamp = this_event_timestamp;
                          ELSE
                            INSERT INTO block_queue
                         SET que_ip_adr =NEW.ip_dst,
                                que_timeout = timeout,
                                que_sig_name = this_sig_name,
                                que_sig_gid = this_sig_gid,
                                que_sig_sid = this_sig,
                                que_event_timestamp = this_event_timestamp;
                          END IF;
                        END IF;
                      END;;
                      DELIMITER ;';
                 

if ( !$result = $db_->query( $SQL_DB ) ) {
    die( 'There was an error running the query [' . $db_->error . ']' );
} //!$result = $db_->query( $SQL_DB )
echo "Create Trigget Schema MySQL OK \n";
*/

$db_->close();
$API->disconnect();
?>

File: /README
README.EN

File: /README.EN
IPS-MikroTik-Suricata is module which connect to Suricata's DB (MySql) using Barnyard2. This module search for custom alerts and when found it, take an IPS action and connect to MikroTik RouterOS via API to add the  Attack's Source IP address and block it (add IP to address list).

Inspired on post from Tom Fisk: http://forum.mikrotik.com/viewtopic.php?t=111727

# New Version
Suricata2MikroTik eve.json version: https://github.com/elmaxid/Suricata2MikroTik


Changelog:

3 March 17: v1.3

* The new schema.sql now support trigger to add the alert. So now is depreceated the daemon mikrotik-ips-daemon_db.php
* Update the instalation file.

Requeriment:

* Suricata,Baynyard2 running
* IP and login for router MikroTik RouterOS
* GIT

** Features

* Detect an Alert from Suricata and connect to RouterOS to block de Attack source IP Address
* Notification:
		* Email
		* Telegram (API Bot)


Instalation

Once we have Suricata working and running on our network, the next step is the instalation of IPS-MikroTik-Suricata:

We have 5 main files

config.php:

File with the config of DB and Router's Login

mikrotik-ips-daemon_db.php: 

Daemon which connect to MySql DB and detect the pattern of alerts and save to DB for block it (DEPRECEATED)

mikrotik-ips-cron.php:

Daemon which take the alert and connect with MikroTik via API and add the IP address to a list (ip firewall address-list) to block IP

mikrotik-ips-clean.php: 

Daemon to maintance and clean the DB.


mikrotik-ips-install.php

File for install and configuration. Create the table with the correct schema and Check the connection via API with MikroTik.


--
To install, Clone the repository and copy to /opt/ips-mikrotik-suricata

cd /opt

git clone https://github.com/elmaxid/ips-mikrotik-suricata.git

cd ips-mikrotik-suricata

-- to Config

* Edit the file config.php  with DB and API Logins

* Create the DB schema 

mysql -u username -p snorby < schema.sql

* To check the DB Connection and API Login:

php -f mikrotik-ips-install.php

* To run, just set the permision 

chmod 777 /opt/ips-mikrotik-suricata/ips_start.sh 

* Edit the file ip_start.sh with the correct path and run it

/opt/ips-mikrotik-suricata/./ips_start.sh 


----

How work it

For run Suricata, you need to redirect the traffic from MikroTik RouterOS to Suricata server, to do it just use Packet Sniffer or  Mangle Send To TZSP Action.



File: /README.ES
IPS-MikroTik-Suricata es una implementación de un módulo que se conecta a la base de datos MySQL del Suricata (utilizando Unified2 y Barnyard2) y busca por alertas predefinidas, en caso de encontrarla toma acción IPS conectándose al MikroTik RouterOS via API para bloquear el IP atacante.

Inspirado en un post de Tom Fisk del foro de MikroTik: http://forum.mikrotik.com/viewtopic.php?t=111727

Mirar la wiki para ver documentación: https://github.com/elmaxid/ips-mikrotik-suricata/wiki/Instalaci%C3%B3n-y-Uso

Lista de Cambios:

3 Marzo 17: v1.3

* Se hizo el schema de la DB con trigger, ahora no es necesario el Demonio mikrotik-ips-daemon_db.php
* Se actualizo la instalación

Requerimientos:

* Suricata funcionando
* Baynyard2 para guardar las alertas en MySql
* IP y datos de acceso de un MikroTik RouterOS
* GIT

** Funcionalidades

* Detecta alertas de Suricata y se conecta al RouterOS para bloquear el ataque
* Notificación de acción:
		* Correo electrónico
		* Telegram (API Bot)


Instalación:

Una vez que se tiene el Suricata instalado y funcionando en nuestra red, podemos proceder a la instalación de IPS-MikroTik-Suricata:

Disponemos de 5 archivos:

config.php:

Archivo de configuración con los datos de acceso a la DB y accesos a MikroTik

mikrotik-ips-daemon_db.php: 

Demonio que se conecta a la DB MySQL y detecta por patrones de Alertas y guarda en DB los datos para bloquear esa alerta.

mikrotik-ips-cron.php:

Demonio que toma las alertas de bloqueos y se conecta al MikroTik via API para agregar a una lista (firewall address-list) la dirección IP para luego bloquearla.

mikrotik-ips-clean.php: 

Demonio de limpieza y mantenimiento de la DB.

mikrotik-ips-install.php

Archivo de instalación y configuración. Crea las tablas con la estructura correspondiente. Chequea conexión API con MikroTik.


--
Para instalar hay que descargar el archivo y copiarlo al directorio /opt/ips-mikrotik-suricata

cd /opt

git clone https://github.com/elmaxid/ips-mikrotik-suricata.git

cd ips-mikrotik-suricata

-- para instalar y configurar

* Configurar archivo config.php  con los datos de la MySQL DB y MikroTik RouterOS API Access

Luego instalar schema DB Mysql

mysql -u username -p snorby < schema.sql

* Para chequear la configuración o Conexión con API ejecutar:

php -f mikrotik-ips-install.php

* Para ejecutar, setear  los permisos y ejecutar

chmod 777 /opt/ips-mikrotik-suricata/ips_start.sh 

* Modificar ip_start.sh con los  datos correctos (path)  y ejecutarlo para iniciar el trabajo

/opt/ips-mikrotik-suricata/./ips_start.sh 


----

Funcionamiento:

Para que el Suricata reciba el tráfico del MikroTik RouterOS hay que redirecionar el mismo, esto se puede realizar con Packet Sniffer o con Mangle Send To TZSP Action.


File: /schema.sql




USE snorby;

SET foreign_key_checks = 0;
-- DROP TABLE `block_queue`, `sigs_to_block`;
#  DROP TRIGGER `after_iphdr_insert`;
#  
 CREATE TABLE `block_queue` (
                      `que_id` int(11) NOT NULL AUTO_INCREMENT,
                      `que_added` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT 'When the block was added',
                      `que_ip_adr` varchar(64) COLLATE utf8_unicode_ci NOT NULL COMMENT 'The IP address to block',
                      `que_timeout` varchar(12) COLLATE utf8_unicode_ci NOT NULL COMMENT 'How long to block for',
                      `que_sig_name` varchar(256) COLLATE utf8_unicode_ci NOT NULL COMMENT 'The name of the signature that caused the block',
                      `que_sig_gid` int(10) NOT NULL COMMENT 'The signature group ID',
                      `que_sig_sid` int(10) NOT NULL COMMENT 'The signature ID',
                      `que_event_timestamp` timestamp NOT NULL DEFAULT '0000-00-00 00:00:00' COMMENT 'When the event was triggered',
                      `que_processed` int(11) NOT NULL DEFAULT '0' COMMENT 'If this item has been processed (0=no, <>0=yes)',
                      PRIMARY KEY (`que_id`),
                      KEY `que_added` (`que_added`)
                    ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci COMMENT='Queue of ip addresses to block on firewall';



   CREATE TABLE `sigs_to_block` (
                      `sig_name` text COLLATE utf8_unicode_ci NOT NULL,
                      `src_or_dst` char(3) COLLATE utf8_unicode_ci NOT NULL DEFAULT 'src',
                      `timeout` varchar(12) COLLATE utf8_unicode_ci NOT NULL DEFAULT '01:00:00',
                      UNIQUE KEY `sig_name_unique_index` (`sig_name`(64))
                    ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;


    INSERT INTO `sigs_to_block` (`sig_name`, `src_or_dst`, `timeout`) VALUES
                    ('ET COMPROMISED Known Compromised or Hostile Host Traffic',    'src',  '01:00:00'),
                    ('ET POLICY Suspicious inbound to', 'src',  '01:00:00'),
                    ('ET DROP Dshield Block Listed Source', 'src',  '01:00:00'),
                    ('ET SCAN Sipvicious Scan', 'src',  '01:00:00'),
                    ('ET SCAN Sipvicious User-Agent Detected (friendly-scanner)',   'src',  '01:00:00'),
                    ('ET DROP Spamhaus DROP Listed Traffic Inbound',    'src',  '01:00:00'),
                    ('ET POLICY Outgoing Basic Auth Base64 HTTP Password detected unencrypted', 'dst',  '23:59:59'),
                    ('ET CINS Active Threat Intelligence Poor Reputation IP',   'src',  '01:00:00'),
                    ('GPL SNMP public access udp',  'src',  '01:00:00'),
                    ('ET TOR Known Tor Relay/Router (Not Exit) Node Traffic',   'src',  '01:00:00'),
                    ('GPL DNS named version attempt',   'src',  '01:00:00'),
                    ('ET VOIP Modified Sipvicious Asterisk PBX User-Agent', 'src',  '01:00:00'),
                    ('GPL RPC xdmcp info query',    'src',  '01:00:00'),
                    ('GPL RPC portmap listing UDP 111', 'src',  '01:00:00'),
                    ('GPL ATTACK_RESPONSE id check returned root',  'src',  '00:01:10'),
                    ('ET VOIP Multiple Unauthorized SIP Responses UDP', 'dst',  '00:59:59'),
                    ('ET POLICY Suspicious inbound to mySQL port 3306', 'src',  '00:10:00'),
                    ('ET SCAN Behavioral Unusually fast Terminal Server Traffic, Potential Scan or Infection (Inbound)',    'src',  '00:10:00'),
                    ('ET DOS Possible NTP DDoS Inbound Frequent',   'src',  '00:10:00'),
                    ('ET SCAN SipCLI VOIP Scan',    'src',  '01:00:00');


                      DELIMITER ;;
                      CREATE TRIGGER `after_iphdr_insert` AFTER INSERT ON `iphdr` FOR EACH ROW
                      BEGIN
                        DECLARE this_event INT(11) default 0;
                        DECLARE this_event_signature INT(10) default 0;
                        DECLARE this_event_timestamp TIMESTAMP;
                        DECLARE this_sig INT(10) default 0;
                        DECLARE this_sig_name VARCHAR(256) default "";
                        DECLARE this_sig_gid INT(10) default 0;
                        DECLARE timeout VARCHAR(12) default "";
                        DECLARE interested INT default 0;
                        DECLARE direction VARCHAR(3) default "";
                        DECLARE ip_src VARCHAR(64) default "";
                        DECLARE ip_dst VARCHAR(64) default "";
                        SELECT event.id, event.signature, event.timestamp
                        INTO this_event, this_event_signature, this_event_timestamp
                        FROM event
                        WHERE event.sid = NEW.sid and event.cid = NEW.cid;  
                        SELECT signature.sig_sid, signature.sig_gid, signature.sig_name 
                        INTO this_sig, this_sig_gid, this_sig_name
                        FROM signature
                        WHERE signature.sig_id = this_event_signature;
                        SELECT count(*), sigs_to_block.src_or_dst, sigs_to_block.timeout
                        INTO interested, direction, timeout
                        FROM sigs_to_block
                        WHERE this_sig_name LIKE CONCAT(sigs_to_block.sig_name, '%');
                        IF (interested > 0) THEN
                         IF (direction = "src") THEN
                            INSERT INTO block_queue
                         SET que_ip_adr =NEW.ip_src,
                                que_timeout = timeout,
                                que_sig_name = this_sig_name,
                                que_sig_gid = this_sig_gid,
                                que_sig_sid = this_sig,
                                que_event_timestamp = this_event_timestamp;
                          ELSE
                            INSERT INTO block_queue
                         SET que_ip_adr =NEW.ip_dst,
                                que_timeout = timeout,
                                que_sig_name = this_sig_name,
                                que_sig_gid = this_sig_gid,
                                que_sig_sid = this_sig,
                                que_event_timestamp = this_event_timestamp;
                          END IF;
                        END IF;
                      END;;
                      DELIMITER ;



File: /share\routeros_api.php
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
    var $timeout   = 2;     //  Connection attempt timeout and data read timeout
    var $attempts  = 2;     //  Connection attempt count
    var $delay     = 2;     //  Delay between connection attempts in seconds
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
            $this->debug('Connection attempt #' . $ATTEMPT . ' to ' . $PROTOCOL . $ip . ':' . $this->port . '...');
            $this->socket = @fsockopen($PROTOCOL . $ip, $this->port, $this->error_no, $this->error_str, $this->timeout);
            if ($this->socket) {
                socket_set_timeout($this->socket, $this->timeout);
                $this->write('/login');
                $RESPONSE = $this->read(false);
                if (isset($RESPONSE[0]) && $RESPONSE[0] == '!done') {
                    $MATCHES = array();
                    if (preg_match_all('/[^=]+/i', $RESPONSE[1], $MATCHES)) {
                        if ($MATCHES[0][0] == 'ret' && strlen($MATCHES[0][1]) == 32) {
                            $this->write('/login', false);
                            $this->write('=name=' . $login, false);
                            $this->write('=response=00' . md5(chr(0) . $password . pack('H*', $MATCHES[0][1])));
                            $RESPONSE = $this->read(false);
                            if ($RESPONSE[0] == '!done') {
                                $this->connected = true;
                                break;
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

