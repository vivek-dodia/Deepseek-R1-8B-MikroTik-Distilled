# Repository Information
Name: Ruby_MikroTik_Backup

# Directory Structure
Directory structure:
└── github_repos/Ruby_MikroTik_Backup/
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
    │   │       ├── pack-58e1592ad07c8561464bc510672a27ba36281b03.idx
    │   │       └── pack-58e1592ad07c8561464bc510672a27ba36281b03.pack
    │   ├── packed-refs
    │   └── refs/
    │       ├── heads/
    │       │   └── master
    │       ├── remotes/
    │       │   └── origin/
    │       │       └── HEAD
    │       └── tags/
    ├── .gitignore
    ├── example/
    │   └── backup.rb
    ├── Gemfile
    ├── lib/
    │   ├── mikrotik-backup/
    │   │   └── version.rb
    │   └── mikrotik-backup.rb
    ├── LICENSE.txt
    ├── mikrotik-backup.gemspec
    ├── Rakefile
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
	url = https://github.com/YouSysAdmin/Ruby_MikroTik_Backup.git
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
0000000000000000000000000000000000000000 19ce4f0c47f42f0f8f80228d979bf8d845cdc5c5 vivek-dodia <vivek.dodia@icloud.com> 1738606076 -0500	clone: from https://github.com/YouSysAdmin/Ruby_MikroTik_Backup.git


File: /.git\logs\refs\heads\master
0000000000000000000000000000000000000000 19ce4f0c47f42f0f8f80228d979bf8d845cdc5c5 vivek-dodia <vivek.dodia@icloud.com> 1738606076 -0500	clone: from https://github.com/YouSysAdmin/Ruby_MikroTik_Backup.git


File: /.git\logs\refs\remotes\origin\HEAD
0000000000000000000000000000000000000000 19ce4f0c47f42f0f8f80228d979bf8d845cdc5c5 vivek-dodia <vivek.dodia@icloud.com> 1738606076 -0500	clone: from https://github.com/YouSysAdmin/Ruby_MikroTik_Backup.git


File: /.git\packed-refs
# pack-refs with: peeled fully-peeled sorted 
b734a3a0f6eccc8119613d6853c634f1f4a3541e refs/remotes/origin/0.0.5
19ce4f0c47f42f0f8f80228d979bf8d845cdc5c5 refs/remotes/origin/master
0fcabce301702a7a2a6fdf2e05289babf695fe98 refs/tags/0.0.1
845b0d82bee3c916f0c4c7f4c27605dce0eb8886 refs/tags/0.0.3
^7dffab0bcf64630433b18001a88059f127f44905
3a9bfd497d8959ed9beeb96826a95f6eac730f63 refs/tags/0.0.4


File: /.git\refs\heads\master
19ce4f0c47f42f0f8f80228d979bf8d845cdc5c5


File: /.git\refs\remotes\origin\HEAD
ref: refs/remotes/origin/master


File: /.gitignore
/.bundle/
/.yardoc
/Gemfile.lock
/_yardoc/
/coverage/
/doc/
/pkg/
/spec/reports/
/tmp/
*.bundle
*.so
*.o
*.a
File: /example\backup.rb
require 'mikrotik-backup'

# Time format
time = Time.now.strftime("%d-%m-%Y")

#Config
# name - associate host name (and name backup file)
# host - host address
# user - user name
# password - user password
# path - local folder for save backup file. "/var/backup/"
# format - backup format binary or script
config = [
    {name:"Router1-#{time}", host: '10.10.10.1' , user:'admin' , password:'admin', path:'./', format:'binary'},
    {name:"Router2-#{time}", host: '10.10.10.2' , user:'admin' , password:'admin', path:'./', format:'script'},
    {name:"Router3-#{time}", host: '10.10.10.3' , user:'admin' , password:'admin', path:'./', format:'binary'},
    {name:"Router4-#{time}", host: '10.10.10.4' , user:'admin' , password:'admin', path:'./', format:'script'},
]


mtik_backup = MTik_backup.new(config)

# Logging
mtik_backup.logger(Logger::DEBUG) # remove this line if not used log, default output only Error
# Log out to file
#mtik_backup.logger(Logger::DEBUG,'backup.log')

# Start backup and download file to local machine
mtik_backup.backup_and_download

# Create backup and save to router memory, do not download file to local machine (return true)
#    mtik_backup.backup 
# Only download created file. (return true)
#    mtik_backup.download

File: /Gemfile
source 'https://rubygems.org'

# Specify your gem's dependencies in mikrotik_backup.gemspec
gemspec
# Add Net::SSH GEM
gem 'net-ssh'
# Add Net::SFTP GEM
gem 'net-sftp'

File: /lib\mikrotik-backup\version.rb
module MikrotikBackup
  VERSION = "0.0.5"
end


File: /lib\mikrotik-backup.rb
require "mikrotik-backup/version"
require 'net/ssh'
require 'net/sftp'
# MikroTik backup class
# noinspection RubyArgCount
class MTik_backup
  # Initialize
  def initialize(config)
    @config = config
    @config.each do |c|
      unless c[:port].is_a? Integer
        c[:port] = 22
      end
    end
    logger
  end
  # Setting for Ruby Logger
  def logger(log_level = Logger::ERROR,log_file = nil)
    if log_file.nil?
      @log = Logger.new(STDOUT)
    else
      @log = Logger.new(log_file)
    end
    @log.level = log_level
    @log.formatter = proc { |severity, datetime, progname, msg|
      "[#{datetime.strftime("%Y-%m-%d %H:%M:%S")}] #{severity}: #{msg}\n"
    }
  end
  # Backup MTik config
  def backup
    @config.each do |config|
      connect_to_host(config[:host],config[:port],config[:user],config[:password])
      backup_config(config[:name],config[:format])
    end
    return true
  end
  # Only download MTik config
  def download
    @config.each do |config|
      download_backup(config[:host],config[:port],config[:user],config[:password],config[:name],config[:path],config[:format])
    end
    return true
  end
  # Backup and download MTik config
  def backup_and_download
    @config.each do |config|
      connect_to_host(config[:host],config[:port],config[:user],config[:password])
      backup_config(config[:name],config[:format])
      download_backup(config[:host],config[:port],config[:user],config[:password],config[:name],config[:path],config[:format])
    end
    return true
  end

# Private section
  private
  # Function connect to SSH/SFTP host
  def connect_to_host(host,port,user,password,sftp=false)
    begin
      if sftp
        @log.info("SFTP connect to host #{host}:#{port}")
        @ssh_connect = Net::SFTP.start(host,user,:password=>password,:port=>port)
      else
        @log.info("SSH connect to host #{host}:#{port}")
        @ssh_connect = Net::SSH.start(host,user,:password=>password,:port=>port)
      end
    rescue Exception => error
      @log.error("#{error}")
      exit
    end
  end
  # Backup function, send SSH command
  def backup_config(name,format='binary')
    @log.info("Backup MikroTik configuration")
    if format == 'binary'
      send_command("/system backup save name=#{name}")
    elsif format == 'script'
      send_command("/export file=#{name}")
    end
    @ssh_connect.close
  end
  # Download backup file from host
  def download_backup(host,port,user,password,name,path,format)
    connect_to_host(host,port,user,password,true)
    if format == 'binary'
      local_file = path+name+".backup"
      remote_file = name+".backup"
    elsif format== 'script'
      local_file = path+name+".rsc"
      remote_file = name+".rsc"
    end
    download_file(remote_file,local_file)
    @ssh_connect.close(@ssh_connect)
  end
  # Send command to host (SSH)
  def send_command(command)
    begin
      @ssh_connect.exec!(command)
    rescue Exception => error
      @log.error("#{error}")
    end
  end
  # Download file from host
  def download_file(remote_file, local_file)
    begin
      @log.info("Download file #{remote_file} to #{local_file}")
      @ssh_connect.download!(remote_file,local_file)
    rescue Exception => error
      @log.error("#{error}")
      exit
    end
  end
end



File: /LICENSE.txt
Copyright (c) 2015 POS_troi

MIT License

Permission is hereby granted, free of charge, to any person obtaining
a copy of this software and associated documentation files (the
"Software"), to deal in the Software without restriction, including
without limitation the rights to use, copy, modify, merge, publish,
distribute, sublicense, and/or sell copies of the Software, and to
permit persons to whom the Software is furnished to do so, subject to
the following conditions:

The above copyright notice and this permission notice shall be
included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.


File: /mikrotik-backup.gemspec
# coding: utf-8
lib = File.expand_path('../lib', __FILE__)
$LOAD_PATH.unshift(lib) unless $LOAD_PATH.include?(lib)
require 'mikrotik-backup/version'

Gem::Specification.new do |spec|
  spec.name          = "mikrotik-backup"
  spec.version       = MikrotikBackup::VERSION
  spec.authors       = ["POS_troi"]
  spec.email         = ["root@sysalex.com"]
  spec.summary       = %q{Backup MikroTik configuration using SSH and SFTP.}
  spec.description   = %q{Backup MikroTik configuration using SSH and SFTP.}
  spec.homepage      = "https://sysalex.com"
  spec.license       = "MIT"

  spec.files         = `git ls-files -z`.split("\x0")
  spec.executables   = spec.files.grep(%r{^bin/}) { |f| File.basename(f) }
  spec.test_files    = spec.files.grep(%r{^(test|spec|features)/})
  spec.require_paths = ["lib"]

  spec.add_development_dependency "bundler", "~> 1.7"
  spec.add_development_dependency "rake", "~> 10.0"
  spec.add_dependency "net-ssh", "~> 2.9"
  spec.add_dependency "net-sftp", "~> 2.1"
end

File: /Rakefile
require "bundler/gem_tasks"



File: /README.md
[![Gem Version](https://badge.fury.io/rb/mikrotik-backup.svg)](http://badge.fury.io/rb/mikrotik-backup)

# Mikrotik Backup

Backup MikroTik configuration using SSH and SFTP.

## Installation

Add this line to your application's Gemfile:

```ruby
gem 'mikrotik-backup'
```

And then execute:

    $ bundle

Or install it yourself as:

    $ gem install mikrotik-backup

## Usage

### Backup only
```ruby

require 'mikrotik-backup'

#Time format
time = Time.now.strftime("%d-%m-%Y")

#Config
# name - associate host name (and name backup file)
# host - host address
# port - port to connect to. If not specified defaults to 22
# user - user name
# password - user password
# path - local folder for save backup file. "/var/backup/"
# format - backup file format, 'binary' or 'script'
config = [
    {name:"Router1-#{time}", host: '10.10.10.1', user:'admin', password:'admin', path:'./', format:'binary'},
    {name:"Router2-#{time}", host: '10.10.10.2', port:'2222', user:'admin', password:'admin', path:'./', format:'script'}
]


backup = MTik_backup.new(config)
# Start backup
backup.backup
```

### Only Download backup (previously created)
```ruby
backup.download
```

### Create backup and download
```ruby
backup.backup_and_download
```

### Logging
```ruby
# Logging only Error, out to console
backup.logger(Logger::ERROR) #<- Default

# Full log out to console
backup.logger(Logger::DEBUG)

# Full log out to file
backup.logger(Logger::DEBUG,'backup.log')
```
### Work log (Logger::DEBUG)
```
[2015-02-11 13:01:32] INFO: SSH connect to host 192.168.1.1
[2015-02-11 13:01:36] INFO: Backup MikroTik configuration
[2015-02-11 13:01:37] INFO: SFTP connect to host 192.168.1.1
[2015-02-11 13:01:38] INFO: Download file Router1-11-02-2015.backup to ./Router1-11-02-2015.backup
[2015-02-11 13:01:38] INFO: SSH connect to host 176.xxx.xxx.28
[2015-02-11 13:01:38] INFO: Backup MikroTik configuration
[2015-02-11 13:01:39] INFO: SFTP connect to host 176.xxx.xxx.28
[2015-02-11 13:01:39] INFO: Download file Router2-11-02-2015.backup to ./Router2-11-02-2015.backup
[2015-02-11 13:01:39] INFO: SSH connect to host 188.xxx.xxx.56
[2015-02-11 13:01:40] INFO: Backup MikroTik configuration
[2015-02-11 13:01:41] INFO: SFTP connect to host 188.xxx.xxx.56
[2015-02-11 13:01:41] INFO: Download file Router3-11-02-2015.backup to ./Router3-11-02-2015.backup
[2015-02-11 13:01:41] INFO: SSH connect to host 188.xxx.xxx.74
[2015-02-11 13:01:42] INFO: Backup MikroTik configuration
[2015-02-11 13:01:42] INFO: SFTP connect to host 188.xxx.xxx.74
[2015-02-11 13:01:43] INFO: Download file Router4-11-02-2015.backup to ./Router4-11-02-2015.backup
```

## Problem

```
ERROR: Creation of file mapping failed with error: 998
```
**Close Pageant PuTTY**

## Contributing

1. Fork it ( https://github.com/POStroi/ruby_mikrotik_backup/fork )
2. Create your feature branch (`git checkout -b my-new-feature`)
3. Commit your changes (`git commit -am 'Add some feature'`)
4. Push to the branch (`git push origin my-new-feature`)
5. Create a new Pull Request


