# Repository Information
Name: mikrotik_router_manager

# Directory Structure
Directory structure:
└── github_repos/mikrotik_router_manager/
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
    │   │       ├── pack-88bae3f3c200da077894716de16597dd47d3c7e1.idx
    │   │       └── pack-88bae3f3c200da077894716de16597dd47d3c7e1.pack
    │   ├── packed-refs
    │   └── refs/
    │       ├── heads/
    │       │   └── master
    │       ├── remotes/
    │       │   └── origin/
    │       │       └── HEAD
    │       └── tags/
    ├── .gitignore
    ├── Database/
    │   ├── router_manager_2017-08-25.sql
    │   ├── router_manager_2017-08-26.sql
    │   └── router_manager_2017-09-22.sql
    ├── generate-xcodeproj.sh
    ├── LICENSE
    ├── mikrotik_router_manager.xcodeproj/
    │   ├── CHTTPParser_Info.plist
    │   ├── Configuration_Info.plist
    │   ├── CORE_Info.plist
    │   ├── CredentialsHTTP_Info.plist
    │   ├── Credentials_Info.plist
    │   ├── Cryptor_Info.plist
    │   ├── CryptoSwift_Info.plist
    │   ├── GeneratedModuleMap/
    │   │   └── CHTTPParser/
    │   │       └── module.modulemap
    │   ├── HeliumLogger_Info.plist
    │   ├── KituraNet_Info.plist
    │   ├── KituraSession_Info.plist
    │   ├── KituraTemplateEngine_Info.plist
    │   ├── Kitura_Info.plist
    │   ├── LoggerAPI_Info.plist
    │   ├── project.pbxproj
    │   ├── project.xcworkspace/
    │   │   └── contents.xcworkspacedata
    │   ├── Socket_Info.plist
    │   ├── SSLService_Info.plist
    │   ├── SwiftKueryMySQL_Info.plist
    │   ├── SwiftKuery_Info.plist
    │   ├── SwiftyJSON_Info.plist
    │   └── xcshareddata/
    │       └── xcschemes/
    │           └── xcschememanagement.plist
    ├── Package.pins
    ├── Package.swift
    ├── README.md
    ├── server_start.sh
    └── Sources/
        ├── CORE/
        │   ├── BaseComponent.swift
        │   ├── Bitter.swift
        │   ├── Engine.swift
        │   ├── EngineConfig.swift
        │   ├── HttpCustomerLogin.swift
        │   ├── HttpServerComponent.swift
        │   ├── HttpUserAPI.swift
        │   ├── HtttpRouterAPI.swift
        │   ├── LogComponent.swift
        │   ├── MikrotikConnection.swift
        │   ├── MysqlConnection.swift
        │   ├── profile_config.plist
        │   └── SessionManager.swift
        └── SERVER/
            └── main.swift


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
	url = https://github.com/DungntVccorp/mikrotik_router_manager.git
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
0000000000000000000000000000000000000000 7b2a7c4db73cb3f09fe03c687dc40cefb8d95843 vivek-dodia <vivek.dodia@icloud.com> 1738606301 -0500	clone: from https://github.com/DungntVccorp/mikrotik_router_manager.git


File: /.git\logs\refs\heads\master
0000000000000000000000000000000000000000 7b2a7c4db73cb3f09fe03c687dc40cefb8d95843 vivek-dodia <vivek.dodia@icloud.com> 1738606301 -0500	clone: from https://github.com/DungntVccorp/mikrotik_router_manager.git


File: /.git\logs\refs\remotes\origin\HEAD
0000000000000000000000000000000000000000 7b2a7c4db73cb3f09fe03c687dc40cefb8d95843 vivek-dodia <vivek.dodia@icloud.com> 1738606301 -0500	clone: from https://github.com/DungntVccorp/mikrotik_router_manager.git


File: /.git\packed-refs
# pack-refs with: peeled fully-peeled sorted 
7b2a7c4db73cb3f09fe03c687dc40cefb8d95843 refs/remotes/origin/master


File: /.git\refs\heads\master
7b2a7c4db73cb3f09fe03c687dc40cefb8d95843


File: /.git\refs\remotes\origin\HEAD
ref: refs/remotes/origin/master


File: /.gitignore
# Xcode
#
# gitignore contributors: remember to update Global/Xcode.gitignore, Objective-C.gitignore & Swift.gitignore

## Build generated
build/
DerivedData/

## Various settings
*.pbxuser
!default.pbxuser
*.mode1v3
!default.mode1v3
*.mode2v3
!default.mode2v3
*.perspectivev3
!default.perspectivev3
xcuserdata/

## Other
*.moved-aside
*.xccheckout
*.xcscmblueprint

## Obj-C/Swift specific
*.hmap
*.ipa
*.dSYM.zip
*.dSYM

## Playgrounds
timeline.xctimeline
playground.xcworkspace

# Swift Package Manager
#
# Add this line if you want to avoid checking in source code from Swift Package Manager dependencies.
# Packages/
# Package.pins
.build/

# CocoaPods
#
# We recommend against adding the Pods directory to your .gitignore. However
# you should judge for yourself, the pros and cons are mentioned at:
# https://guides.cocoapods.org/using/using-cocoapods.html#should-i-check-the-pods-directory-into-source-control
#
# Pods/

# Carthage
#
# Add this line if you want to avoid checking in source code from Carthage dependencies.
# Carthage/Checkouts

Carthage/Build

# fastlane
#
# It is recommended to not store the screenshots in the git repo. Instead, use fastlane to re-generate the
# screenshots whenever they are needed.
# For more information about the recommended setup visit:
# https://docs.fastlane.tools/best-practices/source-control/#source-control

fastlane/report.xml
fastlane/Preview.html
fastlane/screenshots
fastlane/test_output


File: /Database\router_manager_2017-08-25.sql
# ************************************************************
# Sequel Pro SQL dump
# Version 4541
#
# http://www.sequelpro.com/
# https://github.com/sequelpro/sequelpro
#
# Host: 127.0.0.1 (MySQL 5.7.19)
# Database: router_manager
# Generation Time: 2017-08-25 00:28:16 +0000
# ************************************************************


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;


# Dump of table tbl_router
# ------------------------------------------------------------

DROP TABLE IF EXISTS `tbl_router`;

CREATE TABLE `tbl_router` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(200) DEFAULT '',
  `username` varchar(200) NOT NULL DEFAULT '',
  `password` varchar(200) NOT NULL DEFAULT '',
  `ip_address` varchar(200) NOT NULL DEFAULT '',
  `description` varchar(500) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

LOCK TABLES `tbl_router` WRITE;
/*!40000 ALTER TABLE `tbl_router` DISABLE KEYS */;

INSERT INTO `tbl_router` (`id`, `name`, `username`, `password`, `ip_address`, `description`)
VALUES
	(1,'a','admin','123456','10.0.0.1',NULL),
	(4,'d','admin','123456','10.10.10.2','test'),
	(5,'c','asd','aasd','asd',NULL);

/*!40000 ALTER TABLE `tbl_router` ENABLE KEYS */;
UNLOCK TABLES;



/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;


File: /Database\router_manager_2017-08-26.sql
# ************************************************************
# Sequel Pro SQL dump
# Version 4541
#
# http://www.sequelpro.com/
# https://github.com/sequelpro/sequelpro
#
# Host: 127.0.0.1 (MySQL 5.7.19)
# Database: router_manager
# Generation Time: 2017-08-26 02:46:03 +0000
# ************************************************************


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;


# Dump of table tbl_router
# ------------------------------------------------------------

DROP TABLE IF EXISTS `tbl_router`;

CREATE TABLE `tbl_router` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(200) DEFAULT '',
  `username` varchar(200) NOT NULL DEFAULT '',
  `password` varchar(200) NOT NULL DEFAULT '',
  `ip_address` varchar(200) NOT NULL DEFAULT '',
  `description` varchar(500) DEFAULT NULL,
  `port` int(11) NOT NULL DEFAULT '8728',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

LOCK TABLES `tbl_router` WRITE;
/*!40000 ALTER TABLE `tbl_router` DISABLE KEYS */;

INSERT INTO `tbl_router` (`id`, `name`, `username`, `password`, `ip_address`, `description`, `port`)
VALUES
	(1,'dungnt','admin','123456','10.3.2.113','test update',8728);

/*!40000 ALTER TABLE `tbl_router` ENABLE KEYS */;
UNLOCK TABLES;



/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;


File: /Database\router_manager_2017-09-22.sql
# ************************************************************
# Sequel Pro SQL dump
# Version 4541
#
# http://www.sequelpro.com/
# https://github.com/sequelpro/sequelpro
#
# Host: 127.0.0.1 (MySQL 5.7.19)
# Database: router_manager
# Generation Time: 2017-09-21 17:13:52 +0000
# ************************************************************


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;


# Dump of table tbl_router
# ------------------------------------------------------------

DROP TABLE IF EXISTS `tbl_router`;

CREATE TABLE `tbl_router` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(200) DEFAULT '',
  `username` varchar(200) NOT NULL DEFAULT '',
  `password` varchar(200) NOT NULL DEFAULT '',
  `ip_address` varchar(200) NOT NULL DEFAULT '',
  `description` varchar(500) DEFAULT NULL,
  `port` int(11) NOT NULL DEFAULT '8728',
  `type` int(11) NOT NULL,
  `use_userman` int(11) DEFAULT '0',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

LOCK TABLES `tbl_router` WRITE;
/*!40000 ALTER TABLE `tbl_router` DISABLE KEYS */;

INSERT INTO `tbl_router` (`id`, `name`, `username`, `password`, `ip_address`, `description`, `port`, `type`, `use_userman`)
VALUES
	(63,'abcb','admin','123456','10.3.3.176','akjshda ',8728,0,0);

/*!40000 ALTER TABLE `tbl_router` ENABLE KEYS */;
UNLOCK TABLES;


# Dump of table tbl_user
# ------------------------------------------------------------

DROP TABLE IF EXISTS `tbl_user`;

CREATE TABLE `tbl_user` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `routerId` int(11) unsigned NOT NULL,
  `username` varchar(50) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL DEFAULT '',
  `password` varchar(50) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL DEFAULT '',
  `created_at` date NOT NULL,
  `profile_id` varchar(50) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL DEFAULT '',
  `use_userman` int(11) NOT NULL DEFAULT '0',
  PRIMARY KEY (`id`),
  KEY `of_router` (`routerId`),
  CONSTRAINT `of_router` FOREIGN KEY (`routerId`) REFERENCES `tbl_router` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;




/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;


File: /generate-xcodeproj.sh
swift package -Xlinker -L/usr/local/lib generate-xcodeproj


File: /LICENSE
                                 Apache License
                           Version 2.0, January 2004
                        http://www.apache.org/licenses/

   TERMS AND CONDITIONS FOR USE, REPRODUCTION, AND DISTRIBUTION

   1. Definitions.

      "License" shall mean the terms and conditions for use, reproduction,
      and distribution as defined by Sections 1 through 9 of this document.

      "Licensor" shall mean the copyright owner or entity authorized by
      the copyright owner that is granting the License.

      "Legal Entity" shall mean the union of the acting entity and all
      other entities that control, are controlled by, or are under common
      control with that entity. For the purposes of this definition,
      "control" means (i) the power, direct or indirect, to cause the
      direction or management of such entity, whether by contract or
      otherwise, or (ii) ownership of fifty percent (50%) or more of the
      outstanding shares, or (iii) beneficial ownership of such entity.

      "You" (or "Your") shall mean an individual or Legal Entity
      exercising permissions granted by this License.

      "Source" form shall mean the preferred form for making modifications,
      including but not limited to software source code, documentation
      source, and configuration files.

      "Object" form shall mean any form resulting from mechanical
      transformation or translation of a Source form, including but
      not limited to compiled object code, generated documentation,
      and conversions to other media types.

      "Work" shall mean the work of authorship, whether in Source or
      Object form, made available under the License, as indicated by a
      copyright notice that is included in or attached to the work
      (an example is provided in the Appendix below).

      "Derivative Works" shall mean any work, whether in Source or Object
      form, that is based on (or derived from) the Work and for which the
      editorial revisions, annotations, elaborations, or other modifications
      represent, as a whole, an original work of authorship. For the purposes
      of this License, Derivative Works shall not include works that remain
      separable from, or merely link (or bind by name) to the interfaces of,
      the Work and Derivative Works thereof.

      "Contribution" shall mean any work of authorship, including
      the original version of the Work and any modifications or additions
      to that Work or Derivative Works thereof, that is intentionally
      submitted to Licensor for inclusion in the Work by the copyright owner
      or by an individual or Legal Entity authorized to submit on behalf of
      the copyright owner. For the purposes of this definition, "submitted"
      means any form of electronic, verbal, or written communication sent
      to the Licensor or its representatives, including but not limited to
      communication on electronic mailing lists, source code control systems,
      and issue tracking systems that are managed by, or on behalf of, the
      Licensor for the purpose of discussing and improving the Work, but
      excluding communication that is conspicuously marked or otherwise
      designated in writing by the copyright owner as "Not a Contribution."

      "Contributor" shall mean Licensor and any individual or Legal Entity
      on behalf of whom a Contribution has been received by Licensor and
      subsequently incorporated within the Work.

   2. Grant of Copyright License. Subject to the terms and conditions of
      this License, each Contributor hereby grants to You a perpetual,
      worldwide, non-exclusive, no-charge, royalty-free, irrevocable
      copyright license to reproduce, prepare Derivative Works of,
      publicly display, publicly perform, sublicense, and distribute the
      Work and such Derivative Works in Source or Object form.

   3. Grant of Patent License. Subject to the terms and conditions of
      this License, each Contributor hereby grants to You a perpetual,
      worldwide, non-exclusive, no-charge, royalty-free, irrevocable
      (except as stated in this section) patent license to make, have made,
      use, offer to sell, sell, import, and otherwise transfer the Work,
      where such license applies only to those patent claims licensable
      by such Contributor that are necessarily infringed by their
      Contribution(s) alone or by combination of their Contribution(s)
      with the Work to which such Contribution(s) was submitted. If You
      institute patent litigation against any entity (including a
      cross-claim or counterclaim in a lawsuit) alleging that the Work
      or a Contribution incorporated within the Work constitutes direct
      or contributory patent infringement, then any patent licenses
      granted to You under this License for that Work shall terminate
      as of the date such litigation is filed.

   4. Redistribution. You may reproduce and distribute copies of the
      Work or Derivative Works thereof in any medium, with or without
      modifications, and in Source or Object form, provided that You
      meet the following conditions:

      (a) You must give any other recipients of the Work or
          Derivative Works a copy of this License; and

      (b) You must cause any modified files to carry prominent notices
          stating that You changed the files; and

      (c) You must retain, in the Source form of any Derivative Works
          that You distribute, all copyright, patent, trademark, and
          attribution notices from the Source form of the Work,
          excluding those notices that do not pertain to any part of
          the Derivative Works; and

      (d) If the Work includes a "NOTICE" text file as part of its
          distribution, then any Derivative Works that You distribute must
          include a readable copy of the attribution notices contained
          within such NOTICE file, excluding those notices that do not
          pertain to any part of the Derivative Works, in at least one
          of the following places: within a NOTICE text file distributed
          as part of the Derivative Works; within the Source form or
          documentation, if provided along with the Derivative Works; or,
          within a display generated by the Derivative Works, if and
          wherever such third-party notices normally appear. The contents
          of the NOTICE file are for informational purposes only and
          do not modify the License. You may add Your own attribution
          notices within Derivative Works that You distribute, alongside
          or as an addendum to the NOTICE text from the Work, provided
          that such additional attribution notices cannot be construed
          as modifying the License.

      You may add Your own copyright statement to Your modifications and
      may provide additional or different license terms and conditions
      for use, reproduction, or distribution of Your modifications, or
      for any such Derivative Works as a whole, provided Your use,
      reproduction, and distribution of the Work otherwise complies with
      the conditions stated in this License.

   5. Submission of Contributions. Unless You explicitly state otherwise,
      any Contribution intentionally submitted for inclusion in the Work
      by You to the Licensor shall be under the terms and conditions of
      this License, without any additional terms or conditions.
      Notwithstanding the above, nothing herein shall supersede or modify
      the terms of any separate license agreement you may have executed
      with Licensor regarding such Contributions.

   6. Trademarks. This License does not grant permission to use the trade
      names, trademarks, service marks, or product names of the Licensor,
      except as required for reasonable and customary use in describing the
      origin of the Work and reproducing the content of the NOTICE file.

   7. Disclaimer of Warranty. Unless required by applicable law or
      agreed to in writing, Licensor provides the Work (and each
      Contributor provides its Contributions) on an "AS IS" BASIS,
      WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
      implied, including, without limitation, any warranties or conditions
      of TITLE, NON-INFRINGEMENT, MERCHANTABILITY, or FITNESS FOR A
      PARTICULAR PURPOSE. You are solely responsible for determining the
      appropriateness of using or redistributing the Work and assume any
      risks associated with Your exercise of permissions under this License.

   8. Limitation of Liability. In no event and under no legal theory,
      whether in tort (including negligence), contract, or otherwise,
      unless required by applicable law (such as deliberate and grossly
      negligent acts) or agreed to in writing, shall any Contributor be
      liable to You for damages, including any direct, indirect, special,
      incidental, or consequential damages of any character arising as a
      result of this License or out of the use or inability to use the
      Work (including but not limited to damages for loss of goodwill,
      work stoppage, computer failure or malfunction, or any and all
      other commercial damages or losses), even if such Contributor
      has been advised of the possibility of such damages.

   9. Accepting Warranty or Additional Liability. While redistributing
      the Work or Derivative Works thereof, You may choose to offer,
      and charge a fee for, acceptance of support, warranty, indemnity,
      or other liability obligations and/or rights consistent with this
      License. However, in accepting such obligations, You may act only
      on Your own behalf and on Your sole responsibility, not on behalf
      of any other Contributor, and only if You agree to indemnify,
      defend, and hold each Contributor harmless for any liability
      incurred by, or claims asserted against, such Contributor by reason
      of your accepting any such warranty or additional liability.

   END OF TERMS AND CONDITIONS

   APPENDIX: How to apply the Apache License to your work.

      To apply the Apache License to your work, attach the following
      boilerplate notice, with the fields enclosed by brackets "{}"
      replaced with your own identifying information. (Don't include
      the brackets!)  The text should be enclosed in the appropriate
      comment syntax for the file format. We also recommend that a
      file or class name and description of purpose be included on the
      same "printed page" as the copyright notice for easier
      identification within third-party archives.

   Copyright {yyyy} {name of copyright owner}

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.


File: /mikrotik_router_manager.xcodeproj\CHTTPParser_Info.plist
<?xml version="1.0" encoding="UTF-8"?>
<plist version="1.0">
<dict>
  <key>CFBundleDevelopmentRegion</key>
  <string>en</string>
  <key>CFBundleExecutable</key>
  <string>$(EXECUTABLE_NAME)</string>
  <key>CFBundleIdentifier</key>
  <string>$(PRODUCT_BUNDLE_IDENTIFIER)</string>
  <key>CFBundleInfoDictionaryVersion</key>
  <string>6.0</string>
  <key>CFBundleName</key>
  <string>$(PRODUCT_NAME)</string>
  <key>CFBundlePackageType</key>
  <string>FMWK</string>
  <key>CFBundleShortVersionString</key>
  <string>1.0</string>
  <key>CFBundleSignature</key>
  <string>????</string>
  <key>CFBundleVersion</key>
  <string>$(CURRENT_PROJECT_VERSION)</string>
  <key>NSPrincipalClass</key>
  <string></string>
</dict>
</plist>


File: /mikrotik_router_manager.xcodeproj\Configuration_Info.plist
<?xml version="1.0" encoding="UTF-8"?>
<plist version="1.0">
<dict>
  <key>CFBundleDevelopmentRegion</key>
  <string>en</string>
  <key>CFBundleExecutable</key>
  <string>$(EXECUTABLE_NAME)</string>
  <key>CFBundleIdentifier</key>
  <string>$(PRODUCT_BUNDLE_IDENTIFIER)</string>
  <key>CFBundleInfoDictionaryVersion</key>
  <string>6.0</string>
  <key>CFBundleName</key>
  <string>$(PRODUCT_NAME)</string>
  <key>CFBundlePackageType</key>
  <string>FMWK</string>
  <key>CFBundleShortVersionString</key>
  <string>1.0</string>
  <key>CFBundleSignature</key>
  <string>????</string>
  <key>CFBundleVersion</key>
  <string>$(CURRENT_PROJECT_VERSION)</string>
  <key>NSPrincipalClass</key>
  <string></string>
</dict>
</plist>


File: /mikrotik_router_manager.xcodeproj\CORE_Info.plist
<?xml version="1.0" encoding="UTF-8"?>
<plist version="1.0">
<dict>
  <key>CFBundleDevelopmentRegion</key>
  <string>en</string>
  <key>CFBundleExecutable</key>
  <string>$(EXECUTABLE_NAME)</string>
  <key>CFBundleIdentifier</key>
  <string>$(PRODUCT_BUNDLE_IDENTIFIER)</string>
  <key>CFBundleInfoDictionaryVersion</key>
  <string>6.0</string>
  <key>CFBundleName</key>
  <string>$(PRODUCT_NAME)</string>
  <key>CFBundlePackageType</key>
  <string>FMWK</string>
  <key>CFBundleShortVersionString</key>
  <string>1.0</string>
  <key>CFBundleSignature</key>
  <string>????</string>
  <key>CFBundleVersion</key>
  <string>$(CURRENT_PROJECT_VERSION)</string>
  <key>NSPrincipalClass</key>
  <string></string>
</dict>
</plist>


File: /mikrotik_router_manager.xcodeproj\CredentialsHTTP_Info.plist
<?xml version="1.0" encoding="UTF-8"?>
<plist version="1.0">
<dict>
  <key>CFBundleDevelopmentRegion</key>
  <string>en</string>
  <key>CFBundleExecutable</key>
  <string>$(EXECUTABLE_NAME)</string>
  <key>CFBundleIdentifier</key>
  <string>$(PRODUCT_BUNDLE_IDENTIFIER)</string>
  <key>CFBundleInfoDictionaryVersion</key>
  <string>6.0</string>
  <key>CFBundleName</key>
  <string>$(PRODUCT_NAME)</string>
  <key>CFBundlePackageType</key>
  <string>FMWK</string>
  <key>CFBundleShortVersionString</key>
  <string>1.0</string>
  <key>CFBundleSignature</key>
  <string>????</string>
  <key>CFBundleVersion</key>
  <string>$(CURRENT_PROJECT_VERSION)</string>
  <key>NSPrincipalClass</key>
  <string></string>
</dict>
</plist>


File: /mikrotik_router_manager.xcodeproj\Credentials_Info.plist
<?xml version="1.0" encoding="UTF-8"?>
<plist version="1.0">
<dict>
  <key>CFBundleDevelopmentRegion</key>
  <string>en</string>
  <key>CFBundleExecutable</key>
  <string>$(EXECUTABLE_NAME)</string>
  <key>CFBundleIdentifier</key>
  <string>$(PRODUCT_BUNDLE_IDENTIFIER)</string>
  <key>CFBundleInfoDictionaryVersion</key>
  <string>6.0</string>
  <key>CFBundleName</key>
  <string>$(PRODUCT_NAME)</string>
  <key>CFBundlePackageType</key>
  <string>FMWK</string>
  <key>CFBundleShortVersionString</key>
  <string>1.0</string>
  <key>CFBundleSignature</key>
  <string>????</string>
  <key>CFBundleVersion</key>
  <string>$(CURRENT_PROJECT_VERSION)</string>
  <key>NSPrincipalClass</key>
  <string></string>
</dict>
</plist>


File: /mikrotik_router_manager.xcodeproj\Cryptor_Info.plist
<?xml version="1.0" encoding="UTF-8"?>
<plist version="1.0">
<dict>
  <key>CFBundleDevelopmentRegion</key>
  <string>en</string>
  <key>CFBundleExecutable</key>
  <string>$(EXECUTABLE_NAME)</string>
  <key>CFBundleIdentifier</key>
  <string>$(PRODUCT_BUNDLE_IDENTIFIER)</string>
  <key>CFBundleInfoDictionaryVersion</key>
  <string>6.0</string>
  <key>CFBundleName</key>
  <string>$(PRODUCT_NAME)</string>
  <key>CFBundlePackageType</key>
  <string>FMWK</string>
  <key>CFBundleShortVersionString</key>
  <string>1.0</string>
  <key>CFBundleSignature</key>
  <string>????</string>
  <key>CFBundleVersion</key>
  <string>$(CURRENT_PROJECT_VERSION)</string>
  <key>NSPrincipalClass</key>
  <string></string>
</dict>
</plist>


File: /mikrotik_router_manager.xcodeproj\CryptoSwift_Info.plist
<?xml version="1.0" encoding="UTF-8"?>
<plist version="1.0">
<dict>
  <key>CFBundleDevelopmentRegion</key>
  <string>en</string>
  <key>CFBundleExecutable</key>
  <string>$(EXECUTABLE_NAME)</string>
  <key>CFBundleIdentifier</key>
  <string>$(PRODUCT_BUNDLE_IDENTIFIER)</string>
  <key>CFBundleInfoDictionaryVersion</key>
  <string>6.0</string>
  <key>CFBundleName</key>
  <string>$(PRODUCT_NAME)</string>
  <key>CFBundlePackageType</key>
  <string>FMWK</string>
  <key>CFBundleShortVersionString</key>
  <string>1.0</string>
  <key>CFBundleSignature</key>
  <string>????</string>
  <key>CFBundleVersion</key>
  <string>$(CURRENT_PROJECT_VERSION)</string>
  <key>NSPrincipalClass</key>
  <string></string>
</dict>
</plist>


File: /mikrotik_router_manager.xcodeproj\GeneratedModuleMap\CHTTPParser\module.modulemap
module CHTTPParser {
    umbrella header "/Volumes/DATA1/mikrotik_router_manager/.build/checkouts/Kitura-net.git--7410958935072501107/Sources/CHTTPParser/include/CHTTPParser.h"
    export *
}


File: /mikrotik_router_manager.xcodeproj\HeliumLogger_Info.plist
<?xml version="1.0" encoding="UTF-8"?>
<plist version="1.0">
<dict>
  <key>CFBundleDevelopmentRegion</key>
  <string>en</string>
  <key>CFBundleExecutable</key>
  <string>$(EXECUTABLE_NAME)</string>
  <key>CFBundleIdentifier</key>
  <string>$(PRODUCT_BUNDLE_IDENTIFIER)</string>
  <key>CFBundleInfoDictionaryVersion</key>
  <string>6.0</string>
  <key>CFBundleName</key>
  <string>$(PRODUCT_NAME)</string>
  <key>CFBundlePackageType</key>
  <string>FMWK</string>
  <key>CFBundleShortVersionString</key>
  <string>1.0</string>
  <key>CFBundleSignature</key>
  <string>????</string>
  <key>CFBundleVersion</key>
  <string>$(CURRENT_PROJECT_VERSION)</string>
  <key>NSPrincipalClass</key>
  <string></string>
</dict>
</plist>


File: /mikrotik_router_manager.xcodeproj\KituraNet_Info.plist
<?xml version="1.0" encoding="UTF-8"?>
<plist version="1.0">
<dict>
  <key>CFBundleDevelopmentRegion</key>
  <string>en</string>
  <key>CFBundleExecutable</key>
  <string>$(EXECUTABLE_NAME)</string>
  <key>CFBundleIdentifier</key>
  <string>$(PRODUCT_BUNDLE_IDENTIFIER)</string>
  <key>CFBundleInfoDictionaryVersion</key>
  <string>6.0</string>
  <key>CFBundleName</key>
  <string>$(PRODUCT_NAME)</string>
  <key>CFBundlePackageType</key>
  <string>FMWK</string>
  <key>CFBundleShortVersionString</key>
  <string>1.0</string>
  <key>CFBundleSignature</key>
  <string>????</string>
  <key>CFBundleVersion</key>
  <string>$(CURRENT_PROJECT_VERSION)</string>
  <key>NSPrincipalClass</key>
  <string></string>
</dict>
</plist>


File: /mikrotik_router_manager.xcodeproj\KituraSession_Info.plist
<?xml version="1.0" encoding="UTF-8"?>
<plist version="1.0">
<dict>
  <key>CFBundleDevelopmentRegion</key>
  <string>en</string>
  <key>CFBundleExecutable</key>
  <string>$(EXECUTABLE_NAME)</string>
  <key>CFBundleIdentifier</key>
  <string>$(PRODUCT_BUNDLE_IDENTIFIER)</string>
  <key>CFBundleInfoDictionaryVersion</key>
  <string>6.0</string>
  <key>CFBundleName</key>
  <string>$(PRODUCT_NAME)</string>
  <key>CFBundlePackageType</key>
  <string>FMWK</string>
  <key>CFBundleShortVersionString</key>
  <string>1.0</string>
  <key>CFBundleSignature</key>
  <string>????</string>
  <key>CFBundleVersion</key>
  <string>$(CURRENT_PROJECT_VERSION)</string>
  <key>NSPrincipalClass</key>
  <string></string>
</dict>
</plist>


File: /mikrotik_router_manager.xcodeproj\KituraTemplateEngine_Info.plist
<?xml version="1.0" encoding="UTF-8"?>
<plist version="1.0">
<dict>
  <key>CFBundleDevelopmentRegion</key>
  <string>en</string>
  <key>CFBundleExecutable</key>
  <string>$(EXECUTABLE_NAME)</string>
  <key>CFBundleIdentifier</key>
  <string>$(PRODUCT_BUNDLE_IDENTIFIER)</string>
  <key>CFBundleInfoDictionaryVersion</key>
  <string>6.0</string>
  <key>CFBundleName</key>
  <string>$(PRODUCT_NAME)</string>
  <key>CFBundlePackageType</key>
  <string>FMWK</string>
  <key>CFBundleShortVersionString</key>
  <string>1.0</string>
  <key>CFBundleSignature</key>
  <string>????</string>
  <key>CFBundleVersion</key>
  <string>$(CURRENT_PROJECT_VERSION)</string>
  <key>NSPrincipalClass</key>
  <string></string>
</dict>
</plist>


File: /mikrotik_router_manager.xcodeproj\Kitura_Info.plist
<?xml version="1.0" encoding="UTF-8"?>
<plist version="1.0">
<dict>
  <key>CFBundleDevelopmentRegion</key>
  <string>en</string>
  <key>CFBundleExecutable</key>
  <string>$(EXECUTABLE_NAME)</string>
  <key>CFBundleIdentifier</key>
  <string>$(PRODUCT_BUNDLE_IDENTIFIER)</string>
  <key>CFBundleInfoDictionaryVersion</key>
  <string>6.0</string>
  <key>CFBundleName</key>
  <string>$(PRODUCT_NAME)</string>
  <key>CFBundlePackageType</key>
  <string>FMWK</string>
  <key>CFBundleShortVersionString</key>
  <string>1.0</string>
  <key>CFBundleSignature</key>
  <string>????</string>
  <key>CFBundleVersion</key>
  <string>$(CURRENT_PROJECT_VERSION)</string>
  <key>NSPrincipalClass</key>
  <string></string>
</dict>
</plist>


File: /mikrotik_router_manager.xcodeproj\LoggerAPI_Info.plist
<?xml version="1.0" encoding="UTF-8"?>
<plist version="1.0">
<dict>
  <key>CFBundleDevelopmentRegion</key>
  <string>en</string>
  <key>CFBundleExecutable</key>
  <string>$(EXECUTABLE_NAME)</string>
  <key>CFBundleIdentifier</key>
  <string>$(PRODUCT_BUNDLE_IDENTIFIER)</string>
  <key>CFBundleInfoDictionaryVersion</key>
  <string>6.0</string>
  <key>CFBundleName</key>
  <string>$(PRODUCT_NAME)</string>
  <key>CFBundlePackageType</key>
  <string>FMWK</string>
  <key>CFBundleShortVersionString</key>
  <string>1.0</string>
  <key>CFBundleSignature</key>
  <string>????</string>
  <key>CFBundleVersion</key>
  <string>$(CURRENT_PROJECT_VERSION)</string>
  <key>NSPrincipalClass</key>
  <string></string>
</dict>
</plist>


File: /mikrotik_router_manager.xcodeproj\project.pbxproj
// !$*UTF8*$!
{
	archiveVersion = 1;
	classes = {
	};
	objectVersion = 46;
	objects = {

/* Begin PBXAggregateTarget section */
		"CCurl::CCurl::ProductTarget" /* CCurl */ = {
			isa = PBXAggregateTarget;
			buildConfigurationList = OBJ_1057 /* Build configuration list for PBXAggregateTarget "CCurl" */;
			buildPhases = (
			);
			dependencies = (
			);
			name = CCurl;
			productName = CCurl;
		};
		"CMySQL::CMySQL::ProductTarget" /* CMySQL */ = {
			isa = PBXAggregateTarget;
			buildConfigurationList = OBJ_1061 /* Build configuration list for PBXAggregateTarget "CMySQL" */;
			buildPhases = (
			);
			dependencies = (
			);
			name = CMySQL;
			productName = CMySQL;
		};
		"CommonCrypto::CommonCrypto::ProductTarget" /* CommonCrypto */ = {
			isa = PBXAggregateTarget;
			buildConfigurationList = OBJ_1053 /* Build configuration list for PBXAggregateTarget "CommonCrypto" */;
			buildPhases = (
			);
			dependencies = (
			);
			name = CommonCrypto;
			productName = CommonCrypto;
		};
		"Kitura-Credentials::Kitura-Credentials::ProductTarget" /* Kitura-Credentials */ = {
			isa = PBXAggregateTarget;
			buildConfigurationList = OBJ_1043 /* Build configuration list for PBXAggregateTarget "Kitura-Credentials" */;
			buildPhases = (
			);
			dependencies = (
				OBJ_1046 /* PBXTargetDependency */,
			);
			name = "Kitura-Credentials";
			productName = "Kitura-Credentials";
		};
		"Kitura-CredentialsHTTP::Kitura-CredentialsHTTP::ProductTarget" /* Kitura-CredentialsHTTP */ = {
			isa = PBXAggregateTarget;
			buildConfigurationList = OBJ_1038 /* Build configuration list for PBXAggregateTarget "Kitura-CredentialsHTTP" */;
			buildPhases = (
			);
			dependencies = (
				OBJ_1041 /* PBXTargetDependency */,
			);
			name = "Kitura-CredentialsHTTP";
			productName = "Kitura-CredentialsHTTP";
		};
		"Kitura-Session::Kitura-Session::ProductTarget" /* Kitura-Session */ = {
			isa = PBXAggregateTarget;
			buildConfigurationList = OBJ_1048 /* Build configuration list for PBXAggregateTarget "Kitura-Session" */;
			buildPhases = (
			);
			dependencies = (
				OBJ_1051 /* PBXTargetDependency */,
			);
			name = "Kitura-Session";
			productName = "Kitura-Session";
		};
/* End PBXAggregateTarget section */

/* Begin PBXBuildFile section */
		OBJ_1004 /* Socket.swift in Sources */ = {isa = PBXBuildFile; fileRef = OBJ_319 /* Socket.swift */; };
		OBJ_1005 /* SocketProtocols.swift in Sources */ = {isa = PBXBuildFile; fileRef = OBJ_320 /* SocketProtocols.swift */; };
		OBJ_1006 /* SocketUtils.swift in Sources */ = {isa = PBXBuildFile; fileRef = OBJ_321 /* SocketUtils.swift */; };
		OBJ_1012 /* main.swift in Sources */ = {isa = PBXBuildFile; fileRef = OBJ_332 /* main.swift */; };
		OBJ_1014 /* Configuration.framework in Frameworks */ = {isa = PBXBuildFile; fileRef = "Configuration::Configuration::Product" /* Configuration.framework */; };
		OBJ_1015 /* LoggerAPI.framework in Frameworks */ = {isa = PBXBuildFile; fileRef = "LoggerAPI::LoggerAPI::Product" /* LoggerAPI.framework */; };
		OBJ_1022 /* ConfigurationManager.swift in Sources */ = {isa = PBXBuildFile; fileRef = OBJ_324 /* ConfigurationManager.swift */; };
		OBJ_1023 /* ConfigurationNode.swift in Sources */ = {isa = PBXBuildFile; fileRef = OBJ_325 /* ConfigurationNode.swift */; };
		OBJ_1024 /* Deserializer.swift in Sources */ = {isa = PBXBuildFile; fileRef = OBJ_326 /* Deserializer.swift */; };
		OBJ_1025 /* JSONDeserializer.swift in Sources */ = {isa = PBXBuildFile; fileRef = OBJ_328 /* JSONDeserializer.swift */; };
		OBJ_1026 /* PLISTDeserializer.swift in Sources */ = {isa = PBXBuildFile; fileRef = OBJ_329 /* PLISTDeserializer.swift */; };
		OBJ_1027 /* PathUtilities.swift in Sources */ = {isa = PBXBuildFile; fileRef = OBJ_330 /* PathUtilities.swift */; };
		OBJ_1029 /* LoggerAPI.framework in Frameworks */ = {isa = PBXBuildFile; fileRef = "LoggerAPI::LoggerAPI::Product" /* LoggerAPI.framework */; };
		OBJ_1035 /* Logger.swift in Sources */ = {isa = PBXBuildFile; fileRef = OBJ_336 /* Logger.swift */; };
		OBJ_365 /* Package.swift in Sources */ = {isa = PBXBuildFile; fileRef = OBJ_6 /* Package.swift */; };
		OBJ_371 /* Package.swift in Sources */ = {isa = PBXBuildFile; fileRef = OBJ_31 /* Package.swift */; };
		OBJ_377 /* Package.swift in Sources */ = {isa = PBXBuildFile; fileRef = OBJ_36 /* Package.swift */; };
		OBJ_383 /* Package.swift in Sources */ = {isa = PBXBuildFile; fileRef = OBJ_43 /* Package.swift */; };
		OBJ_389 /* Package.swift in Sources */ = {isa = PBXBuildFile; fileRef = OBJ_52 /* Package.swift */; };
		OBJ_395 /* Package.swift in Sources */ = {isa = PBXBuildFile; fileRef = OBJ_63 /* Package.swift */; };
		OBJ_401 /* Package.swift in Sources */ = {isa = PBXBuildFile; fileRef = OBJ_76 /* Package.swift */; };
		OBJ_407 /* Package.swift in Sources */ = {isa = PBXBuildFile; fileRef = OBJ_126 /* Package.swift */; };
		OBJ_413 /* Package.swift in Sources */ = {isa = PBXBuildFile; fileRef = OBJ_130 /* Package.swift */; };
		OBJ_419 /* Package.swift in Sources */ = {isa = PBXBuildFile; fileRef = OBJ_135 /* Package.swift */; };
		OBJ_425 /* Package.swift in Sources */ = {isa = PBXBuildFile; fileRef = OBJ_186 /* Package.swift */; };
		OBJ_431 /* Package.swift in Sources */ = {isa = PBXBuildFile; fileRef = OBJ_190 /* Package.swift */; };
		OBJ_437 /* Package.swift in Sources */ = {isa = PBXBuildFile; fileRef = OBJ_197 /* Package.swift */; };
		OBJ_443 /* Package.swift in Sources */ = {isa = PBXBuildFile; fileRef = OBJ_248 /* Package.swift */; };
		OBJ_449 /* Package.swift in Sources */ = {isa = PBXBuildFile; fileRef = OBJ_316 /* Package.swift */; };
		OBJ_455 /* Package.swift in Sources */ = {isa = PBXBuildFile; fileRef = OBJ_318 /* Package.swift */; };
		OBJ_461 /* Package.swift in Sources */ = {isa = PBXBuildFile; fileRef = OBJ_333 /* Package.swift */; };
		OBJ_467 /* Package.swift in Sources */ = {isa = PBXBuildFile; fileRef = OBJ_337 /* Package.swift */; };
		OBJ_473 /* main.swift in Sources */ = {isa = PBXBuildFile; fileRef = OBJ_22 /* main.swift */; };
		OBJ_475 /* CORE.framework in Frameworks */ = {isa = PBXBuildFile; fileRef = "mikrotik_router_manager::CORE::Product" /* CORE.framework */; };
		OBJ_476 /* KituraCORS.framework in Frameworks */ = {isa = PBXBuildFile; fileRef = "KituraCORS::KituraCORS::Product" /* KituraCORS.framework */; };
		OBJ_477 /* HeliumLogger.framework in Frameworks */ = {isa = PBXBuildFile; fileRef = "HeliumLogger::HeliumLogger::Product" /* HeliumLogger.framework */; };
		OBJ_478 /* CredentialsHTTP.framework in Frameworks */ = {isa = PBXBuildFile; fileRef = "Kitura-CredentialsHTTP::CredentialsHTTP::Product" /* CredentialsHTTP.framework */; };
		OBJ_479 /* Credentials.framework in Frameworks */ = {isa = PBXBuildFile; fileRef = "Kitura-Credentials::Credentials::Product" /* Credentials.framework */; };
		OBJ_480 /* KituraSession.framework in Frameworks */ = {isa = PBXBuildFile; fileRef = "Kitura-Session::KituraSession::Product" /* KituraSession.framework */; };
		OBJ_481 /* Cryptor.framework in Frameworks */ = {isa = PBXBuildFile; fileRef = "Cryptor::Cryptor::Product" /* Cryptor.framework */; };
		OBJ_482 /* Kitura.framework in Frameworks */ = {isa = PBXBuildFile; fileRef = "Kitura::Kitura::Product" /* Kitura.framework */; };
		OBJ_483 /* KituraTemplateEngine.framework in Frameworks */ = {isa = PBXBuildFile; fileRef = "Kitura-TemplateEngine::KituraTemplateEngine::Product" /* KituraTemplateEngine.framework */; };
		OBJ_484 /* SwiftyJSON.framework in Frameworks */ = {isa = PBXBuildFile; fileRef = "SwiftyJSON::SwiftyJSON::Product" /* SwiftyJSON.framework */; };
		OBJ_485 /* KituraNet.framework in Frameworks */ = {isa = PBXBuildFile; fileRef = "Kitura-net::KituraNet::Product" /* KituraNet.framework */; };
		OBJ_486 /* SSLService.framework in Frameworks */ = {isa = PBXBuildFile; fileRef = "SSLService::SSLService::Product" /* SSLService.framework */; };
		OBJ_487 /* CHTTPParser.framework in Frameworks */ = {isa = PBXBuildFile; fileRef = "Kitura-net::CHTTPParser::Product" /* CHTTPParser.framework */; };
		OBJ_488 /* SwiftKueryMySQL.framework in Frameworks */ = {isa = PBXBuildFile; fileRef = "SwiftKueryMySQL::SwiftKueryMySQL::Product" /* SwiftKueryMySQL.framework */; };
		OBJ_489 /* SwiftKuery.framework in Frameworks */ = {isa = PBXBuildFile; fileRef = "SwiftKuery::SwiftKuery::Product" /* SwiftKuery.framework */; };
		OBJ_490 /* CryptoSwift.framework in Frameworks */ = {isa = PBXBuildFile; fileRef = "CryptoSwift::CryptoSwift::Product" /* CryptoSwift.framework */; };
		OBJ_491 /* Socket.framework in Frameworks */ = {isa = PBXBuildFile; fileRef = "Socket::Socket::Product" /* Socket.framework */; };
		OBJ_492 /* Configuration.framework in Frameworks */ = {isa = PBXBuildFile; fileRef = "Configuration::Configuration::Product" /* Configuration.framework */; };
		OBJ_493 /* LoggerAPI.framework in Frameworks */ = {isa = PBXBuildFile; fileRef = "LoggerAPI::LoggerAPI::Product" /* LoggerAPI.framework */; };
		OBJ_538 /* BaseComponent.swift in Sources */ = {isa = PBXBuildFile; fileRef = OBJ_9 /* BaseComponent.swift */; };
		OBJ_539 /* Bitter.swift in Sources */ = {isa = PBXBuildFile; fileRef = OBJ_10 /* Bitter.swift */; };
		OBJ_540 /* Engine.swift in Sources */ = {isa = PBXBuildFile; fileRef = OBJ_11 /* Engine.swift */; };
		OBJ_541 /* EngineConfig.swift in Sources */ = {isa = PBXBuildFile; fileRef = OBJ_12 /* EngineConfig.swift */; };
		OBJ_542 /* HttpCustomerLogin.swift in Sources */ = {isa = PBXBuildFile; fileRef = OBJ_13 /* HttpCustomerLogin.swift */; };
		OBJ_543 /* HttpServerComponent.swift in Sources */ = {isa = PBXBuildFile; fileRef = OBJ_14 /* HttpServerComponent.swift */; };
		OBJ_544 /* HttpUserAPI.swift in Sources */ = {isa = PBXBuildFile; fileRef = OBJ_15 /* HttpUserAPI.swift */; };
		OBJ_545 /* HtttpRouterAPI.swift in Sources */ = {isa = PBXBuildFile; fileRef = OBJ_16 /* HtttpRouterAPI.swift */; };
		OBJ_546 /* LogComponent.swift in Sources */ = {isa = PBXBuildFile; fileRef = OBJ_17 /* LogComponent.swift */; };
		OBJ_547 /* MikrotikConnection.swift in Sources */ = {isa = PBXBuildFile; fileRef = OBJ_18 /* MikrotikConnection.swift */; };
		OBJ_548 /* MysqlConnection.swift in Sources */ = {isa = PBXBuildFile; fileRef = OBJ_19 /* MysqlConnection.swift */; };
		OBJ_549 /* SessionManager.swift in Sources */ = {isa = PBXBuildFile; fileRef = OBJ_20 /* SessionManager.swift */; };
		OBJ_551 /* KituraCORS.framework in Frameworks */ = {isa = PBXBuildFile; fileRef = "KituraCORS::KituraCORS::Product" /* KituraCORS.framework */; };
		OBJ_552 /* HeliumLogger.framework in Frameworks */ = {isa = PBXBuildFile; fileRef = "HeliumLogger::HeliumLogger::Product" /* HeliumLogger.framework */; };
		OBJ_553 /* CredentialsHTTP.framework in Frameworks */ = {isa = PBXBuildFile; fileRef = "Kitura-CredentialsHTTP::CredentialsHTTP::Product" /* CredentialsHTTP.framework */; };
		OBJ_554 /* Credentials.framework in Frameworks */ = {isa = PBXBuildFile; fileRef = "Kitura-Credentials::Credentials::Product" /* Credentials.framework */; };
		OBJ_555 /* KituraSession.framework in Frameworks */ = {isa = PBXBuildFile; fileRef = "Kitura-Session::KituraSession::Product" /* KituraSession.framework */; };
		OBJ_556 /* Cryptor.framework in Frameworks */ = {isa = PBXBuildFile; fileRef = "Cryptor::Cryptor::Product" /* Cryptor.framework */; };
		OBJ_557 /* Kitura.framework in Frameworks */ = {isa = PBXBuildFile; fileRef = "Kitura::Kitura::Product" /* Kitura.framework */; };
		OBJ_558 /* KituraTemplateEngine.framework in Frameworks */ = {isa = PBXBuildFile; fileRef = "Kitura-TemplateEngine::KituraTemplateEngine::Product" /* KituraTemplateEngine.framework */; };
		OBJ_559 /* SwiftyJSON.framework in Frameworks */ = {isa = PBXBuildFile; fileRef = "SwiftyJSON::SwiftyJSON::Product" /* SwiftyJSON.framework */; };
		OBJ_560 /* KituraNet.framework in Frameworks */ = {isa = PBXBuildFile; fileRef = "Kitura-net::KituraNet::Product" /* KituraNet.framework */; };
		OBJ_561 /* SSLService.framework in Frameworks */ = {isa = PBXBuildFile; fileRef = "SSLService::SSLService::Product" /* SSLService.framework */; };
		OBJ_562 /* CHTTPParser.framework in Frameworks */ = {isa = PBXBuildFile; fileRef = "Kitura-net::CHTTPParser::Product" /* CHTTPParser.framework */; };
		OBJ_563 /* SwiftKueryMySQL.framework in Frameworks */ = {isa = PBXBuildFile; fileRef = "SwiftKueryMySQL::SwiftKueryMySQL::Product" /* SwiftKueryMySQL.framework */; };
		OBJ_564 /* SwiftKuery.framework in Frameworks */ = {isa = PBXBuildFile; fileRef = "SwiftKuery::SwiftKuery::Product" /* SwiftKuery.framework */; };
		OBJ_565 /* CryptoSwift.framework in Frameworks */ = {isa = PBXBuildFile; fileRef = "CryptoSwift::CryptoSwift::Product" /* CryptoSwift.framework */; };
		OBJ_566 /* Socket.framework in Frameworks */ = {isa = PBXBuildFile; fileRef = "Socket::Socket::Product" /* Socket.framework */; };
		OBJ_567 /* Configuration.framework in Frameworks */ = {isa = PBXBuildFile; fileRef = "Configuration::Configuration::Product" /* Configuration.framework */; };
		OBJ_568 /* LoggerAPI.framework in Frameworks */ = {isa = PBXBuildFile; fileRef = "LoggerAPI::LoggerAPI::Product" /* LoggerAPI.framework */; };
		OBJ_592 /* AllowedOrigins.swift in Sources */ = {isa = PBXBuildFile; fileRef = OBJ_28 /* AllowedOrigins.swift */; };
		OBJ_593 /* CORS.swift in Sources */ = {isa = PBXBuildFile; fileRef = OBJ_29 /* CORS.swift */; };
		OBJ_594 /* Options.swift in Sources */ = {isa = PBXBuildFile; fileRef = OBJ_30 /* Options.swift */; };
		OBJ_596 /* Kitura.framework in Frameworks */ = {isa = PBXBuildFile; fileRef = "Kitura::Kitura::Product" /* Kitura.framework */; };
		OBJ_597 /* KituraTemplateEngine.framework in Frameworks */ = {isa = PBXBuildFile; fileRef = "Kitura-TemplateEngine::KituraTemplateEngine::Product" /* KituraTemplateEngine.framework */; };
		OBJ_598 /* SwiftyJSON.framework in Frameworks */ = {isa = PBXBuildFile; fileRef = "SwiftyJSON::SwiftyJSON::Product" /* SwiftyJSON.framework */; };
		OBJ_599 /* KituraNet.framework in Frameworks */ = {isa = PBXBuildFile; fileRef = "Kitura-net::KituraNet::Product" /* KituraNet.framework */; };
		OBJ_600 /* SSLService.framework in Frameworks */ = {isa = PBXBuildFile; fileRef = "SSLService::SSLService::Product" /* SSLService.framework */; };
		OBJ_601 /* Socket.framework in Frameworks */ = {isa = PBXBuildFile; fileRef = "Socket::Socket::Product" /* Socket.framework */; };
		OBJ_602 /* LoggerAPI.framework in Frameworks */ = {isa = PBXBuildFile; fileRef = "LoggerAPI::LoggerAPI::Product" /* LoggerAPI.framework */; };
		OBJ_603 /* CHTTPParser.framework in Frameworks */ = {isa = PBXBuildFile; fileRef = "Kitura-net::CHTTPParser::Product" /* CHTTPParser.framework */; };
		OBJ_616 /* HeliumLogger.swift in Sources */ = {isa = PBXBuildFile; fileRef = OBJ_34 /* HeliumLogger.swift */; };
		OBJ_617 /* HeliumStreamLogger.swift in Sources */ = {isa = PBXBuildFile; fileRef = OBJ_35 /* HeliumStreamLogger.swift */; };
		OBJ_619 /* LoggerAPI.framework in Frameworks */ = {isa = PBXBuildFile; fileRef = "LoggerAPI::LoggerAPI::Product" /* LoggerAPI.framework */; };
		OBJ_625 /* CredentialsHTTPBasic.swift in Sources */ = {isa = PBXBuildFile; fileRef = OBJ_39 /* CredentialsHTTPBasic.swift */; };
		OBJ_626 /* CredentialsHTTPDigest.swift in Sources */ = {isa = PBXBuildFile; fileRef = OBJ_40 /* CredentialsHTTPDigest.swift */; };
		OBJ_627 /* UserProfileLoader.swift in Sources */ = {isa = PBXBuildFile; fileRef = OBJ_41 /* UserProfileLoader.swift */; };
		OBJ_628 /* VerifyPassword.swift in Sources */ = {isa = PBXBuildFile; fileRef = OBJ_42 /* VerifyPassword.swift */; };
		OBJ_630 /* Credentials.framework in Frameworks */ = {isa = PBXBuildFile; fileRef = "Kitura-Credentials::Credentials::Product" /* Credentials.framework */; };
		OBJ_631 /* KituraSession.framework in Frameworks */ = {isa = PBXBuildFile; fileRef = "Kitura-Session::KituraSession::Product" /* KituraSession.framework */; };
		OBJ_632 /* Cryptor.framework in Frameworks */ = {isa = PBXBuildFile; fileRef = "Cryptor::Cryptor::Product" /* Cryptor.framework */; };
		OBJ_633 /* Kitura.framework in Frameworks */ = {isa = PBXBuildFile; fileRef = "Kitura::Kitura::Product" /* Kitura.framework */; };
		OBJ_634 /* KituraTemplateEngine.framework in Frameworks */ = {isa = PBXBuildFile; fileRef = "Kitura-TemplateEngine::KituraTemplateEngine::Product" /* KituraTemplateEngine.framework */; };
		OBJ_635 /* SwiftyJSON.framework in Frameworks */ = {isa = PBXBuildFile; fileRef = "SwiftyJSON::SwiftyJSON::Product" /* SwiftyJSON.framework */; };
		OBJ_636 /* KituraNet.framework in Frameworks */ = {isa = PBXBuildFile; fileRef = "Kitura-net::KituraNet::Product" /* KituraNet.framework */; };
		OBJ_637 /* SSLService.framework in Frameworks */ = {isa = PBXBuildFile; fileRef = "SSLService::SSLService::Product" /* SSLService.framework */; };
		OBJ_638 /* Socket.framework in Frameworks */ = {isa = PBXBuildFile; fileRef = "Socket::Socket::Product" /* Socket.framework */; };
		OBJ_639 /* LoggerAPI.framework in Frameworks */ = {isa = PBXBuildFile; fileRef = "LoggerAPI::LoggerAPI::Product" /* LoggerAPI.framework */; };
		OBJ_640 /* CHTTPParser.framework in Frameworks */ = {isa = PBXBuildFile; fileRef = "Kitura-net::CHTTPParser::Product" /* CHTTPParser.framework */; };
		OBJ_656 /* BaseCacheElement.swift in Sources */ = {isa = PBXBuildFile; fileRef = OBJ_46 /* BaseCacheElement.swift */; };
		OBJ_657 /* Credentials.swift in Sources */ = {isa = PBXBuildFile; fileRef = OBJ_47 /* Credentials.swift */; };
		OBJ_658 /* CredentialsPluginProtocol.swift in Sources */ = {isa = PBXBuildFile; fileRef = OBJ_48 /* CredentialsPluginProtocol.swift */; };
		OBJ_659 /* RouterRequest+UserProfile.swift in Sources */ = {isa = PBXBuildFile; fileRef = OBJ_49 /* RouterRequest+UserProfile.swift */; };
		OBJ_660 /* UserProfile.swift in Sources */ = {isa = PBXBuildFile; fileRef = OBJ_50 /* UserProfile.swift */; };
		OBJ_661 /* UserProfileDelegate.swift in Sources */ = {isa = PBXBuildFile; fileRef = OBJ_51 /* UserProfileDelegate.swift */; };
		OBJ_663 /* KituraSession.framework in Frameworks */ = {isa = PBXBuildFile; fileRef = "Kitura-Session::KituraSession::Product" /* KituraSession.framework */; };
		OBJ_664 /* Cryptor.framework in Frameworks */ = {isa = PBXBuildFile; fileRef = "Cryptor::Cryptor::Product" /* Cryptor.framework */; };
		OBJ_665 /* Kitura.framework in Frameworks */ = {isa = PBXBuildFile; fileRef = "Kitura::Kitura::Product" /* Kitura.framework */; };
		OBJ_666 /* KituraTemplateEngine.framework in Frameworks */ = {isa = PBXBuildFile; fileRef = "Kitura-TemplateEngine::KituraTemplateEngine::Product" /* KituraTemplateEngine.framework */; };
		OBJ_667 /* SwiftyJSON.framework in Frameworks */ = {isa = PBXBuildFile; fileRef = "SwiftyJSON::SwiftyJSON::Product" /* SwiftyJSON.framework */; };
		OBJ_668 /* KituraNet.framework in Frameworks */ = {isa = PBXBuildFile; fileRef = "Kitura-net::KituraNet::Product" /* KituraNet.framework */; };
		OBJ_669 /* SSLService.framework in Frameworks */ = {isa = PBXBuildFile; fileRef = "SSLService::SSLService::Product" /* SSLService.framework */; };
		OBJ_670 /* Socket.framework in Frameworks */ = {isa = PBXBuildFile; fileRef = "Socket::Socket::Product" /* Socket.framework */; };
		OBJ_671 /* LoggerAPI.framework in Frameworks */ = {isa = PBXBuildFile; fileRef = "LoggerAPI::LoggerAPI::Product" /* LoggerAPI.framework */; };
		OBJ_672 /* CHTTPParser.framework in Frameworks */ = {isa = PBXBuildFile; fileRef = "Kitura-net::CHTTPParser::Product" /* CHTTPParser.framework */; };
		OBJ_687 /* CookieCryptography.swift in Sources */ = {isa = PBXBuildFile; fileRef = OBJ_55 /* CookieCryptography.swift */; };
		OBJ_688 /* CookieManagement.swift in Sources */ = {isa = PBXBuildFile; fileRef = OBJ_56 /* CookieManagement.swift */; };
		OBJ_689 /* CookieParameter.swift in Sources */ = {isa = PBXBuildFile; fileRef = OBJ_57 /* CookieParameter.swift */; };
		OBJ_690 /* InMemoryStore.swift in Sources */ = {isa = PBXBuildFile; fileRef = OBJ_58 /* InMemoryStore.swift */; };
		OBJ_691 /* RouterRequest+Session.swift in Sources */ = {isa = PBXBuildFile; fileRef = OBJ_59 /* RouterRequest+Session.swift */; };
		OBJ_692 /* Session.swift in Sources */ = {isa = PBXBuildFile; fileRef = OBJ_60 /* Session.swift */; };
		OBJ_693 /* SessionState.swift in Sources */ = {isa = PBXBuildFile; fileRef = OBJ_61 /* SessionState.swift */; };
		OBJ_694 /* Store.swift in Sources */ = {isa = PBXBuildFile; fileRef = OBJ_62 /* Store.swift */; };
		OBJ_696 /* Cryptor.framework in Frameworks */ = {isa = PBXBuildFile; fileRef = "Cryptor::Cryptor::Product" /* Cryptor.framework */; };
		OBJ_697 /* Kitura.framework in Frameworks */ = {isa = PBXBuildFile; fileRef = "Kitura::Kitura::Product" /* Kitura.framework */; };
		OBJ_698 /* KituraTemplateEngine.framework in Frameworks */ = {isa = PBXBuildFile; fileRef = "Kitura-TemplateEngine::KituraTemplateEngine::Product" /* KituraTemplateEngine.framework */; };
		OBJ_699 /* SwiftyJSON.framework in Frameworks */ = {isa = PBXBuildFile; fileRef = "SwiftyJSON::SwiftyJSON::Product" /* SwiftyJSON.framework */; };
		OBJ_700 /* KituraNet.framework in Frameworks */ = {isa = PBXBuildFile; fileRef = "Kitura-net::KituraNet::Product" /* KituraNet.framework */; };
		OBJ_701 /* SSLService.framework in Frameworks */ = {isa = PBXBuildFile; fileRef = "SSLService::SSLService::Product" /* SSLService.framework */; };
		OBJ_702 /* Socket.framework in Frameworks */ = {isa = PBXBuildFile; fileRef = "Socket::Socket::Product" /* Socket.framework */; };
		OBJ_703 /* LoggerAPI.framework in Frameworks */ = {isa = PBXBuildFile; fileRef = "LoggerAPI::LoggerAPI::Product" /* LoggerAPI.framework */; };
		OBJ_704 /* CHTTPParser.framework in Frameworks */ = {isa = PBXBuildFile; fileRef = "Kitura-net::CHTTPParser::Product" /* CHTTPParser.framework */; };
		OBJ_718 /* Crypto.swift in Sources */ = {isa = PBXBuildFile; fileRef = OBJ_66 /* Crypto.swift */; };
		OBJ_719 /* Cryptor.swift in Sources */ = {isa = PBXBuildFile; fileRef = OBJ_67 /* Cryptor.swift */; };
		OBJ_720 /* Digest.swift in Sources */ = {isa = PBXBuildFile; fileRef = OBJ_68 /* Digest.swift */; };
		OBJ_721 /* HMAC.swift in Sources */ = {isa = PBXBuildFile; fileRef = OBJ_69 /* HMAC.swift */; };
		OBJ_722 /* KeyDerivation.swift in Sources */ = {isa = PBXBuildFile; fileRef = OBJ_70 /* KeyDerivation.swift */; };
		OBJ_723 /* Random.swift in Sources */ = {isa = PBXBuildFile; fileRef = OBJ_71 /* Random.swift */; };
		OBJ_724 /* Status.swift in Sources */ = {isa = PBXBuildFile; fileRef = OBJ_72 /* Status.swift */; };
		OBJ_725 /* StreamCryptor.swift in Sources */ = {isa = PBXBuildFile; fileRef = OBJ_73 /* StreamCryptor.swift */; };
		OBJ_726 /* Updatable.swift in Sources */ = {isa = PBXBuildFile; fileRef = OBJ_74 /* Updatable.swift */; };
		OBJ_727 /* Utilities.swift in Sources */ = {isa = PBXBuildFile; fileRef = OBJ_75 /* Utilities.swift */; };
		OBJ_733 /* Error.swift in Sources */ = {isa = PBXBuildFile; fileRef = OBJ_79 /* Error.swift */; };
		OBJ_734 /* FileResourceServer.swift in Sources */ = {isa = PBXBuildFile; fileRef = OBJ_80 /* FileResourceServer.swift */; };
		OBJ_735 /* HTTPVersion.swift in Sources */ = {isa = PBXBuildFile; fileRef = OBJ_81 /* HTTPVersion.swift */; };
		OBJ_736 /* Headers.swift in Sources */ = {isa = PBXBuildFile; fileRef = OBJ_82 /* Headers.swift */; };
		OBJ_737 /* InternalError.swift in Sources */ = {isa = PBXBuildFile; fileRef = OBJ_83 /* InternalError.swift */; };
		OBJ_738 /* JSONPError.swift in Sources */ = {isa = PBXBuildFile; fileRef = OBJ_84 /* JSONPError.swift */; };
		OBJ_739 /* Kitura.swift in Sources */ = {isa = PBXBuildFile; fileRef = OBJ_85 /* Kitura.swift */; };
		OBJ_740 /* LinkParameter.swift in Sources */ = {isa = PBXBuildFile; fileRef = OBJ_86 /* LinkParameter.swift */; };
		OBJ_741 /* MimeTypeAcceptor.swift in Sources */ = {isa = PBXBuildFile; fileRef = OBJ_87 /* MimeTypeAcceptor.swift */; };
		OBJ_742 /* RouteRegex.swift in Sources */ = {isa = PBXBuildFile; fileRef = OBJ_88 /* RouteRegex.swift */; };
		OBJ_743 /* Router.swift in Sources */ = {isa = PBXBuildFile; fileRef = OBJ_89 /* Router.swift */; };
		OBJ_744 /* RouterElement.swift in Sources */ = {isa = PBXBuildFile; fileRef = OBJ_90 /* RouterElement.swift */; };
		OBJ_745 /* RouterElementWalker.swift in Sources */ = {isa = PBXBuildFile; fileRef = OBJ_91 /* RouterElementWalker.swift */; };
		OBJ_746 /* RouterHTTPVerbs+Error.swift in Sources */ = {isa = PBXBuildFile; fileRef = OBJ_92 /* RouterHTTPVerbs+Error.swift */; };
		OBJ_747 /* RouterHTTPVerbs_generated.swift in Sources */ = {isa = PBXBuildFile; fileRef = OBJ_93 /* RouterHTTPVerbs_generated.swift */; };
		OBJ_748 /* RouterHandler.swift in Sources */ = {isa = PBXBuildFile; fileRef = OBJ_94 /* RouterHandler.swift */; };
		OBJ_749 /* RouterMethod.swift in Sources */ = {isa = PBXBuildFile; fileRef = OBJ_95 /* RouterMethod.swift */; };
		OBJ_750 /* RouterMiddleware.swift in Sources */ = {isa = PBXBuildFile; fileRef = OBJ_96 /* RouterMiddleware.swift */; };
		OBJ_751 /* RouterMiddlewareGenerator.swift in Sources */ = {isa = PBXBuildFile; fileRef = OBJ_97 /* RouterMiddlewareGenerator.swift */; };
		OBJ_752 /* RouterMiddlewareWalker.swift in Sources */ = {isa = PBXBuildFile; fileRef = OBJ_98 /* RouterMiddlewareWalker.swift */; };
		OBJ_753 /* RouterParameterWalker.swift in Sources */ = {isa = PBXBuildFile; fileRef = OBJ_99 /* RouterParameterWalker.swift */; };
		OBJ_754 /* RouterRequest.swift in Sources */ = {isa = PBXBuildFile; fileRef = OBJ_100 /* RouterRequest.swift */; };
		OBJ_755 /* RouterResponse.swift in Sources */ = {isa = PBXBuildFile; fileRef = OBJ_101 /* RouterResponse.swift */; };
		OBJ_756 /* SSLConfig.swift in Sources */ = {isa = PBXBuildFile; fileRef = OBJ_102 /* SSLConfig.swift */; };
		OBJ_757 /* Stack.swift in Sources */ = {isa = PBXBuildFile; fileRef = OBJ_103 /* Stack.swift */; };
		OBJ_758 /* String+Extensions.swift in Sources */ = {isa = PBXBuildFile; fileRef = OBJ_104 /* String+Extensions.swift */; };
		OBJ_759 /* TemplatingError.swift in Sources */ = {isa = PBXBuildFile; fileRef = OBJ_105 /* TemplatingError.swift */; };
		OBJ_760 /* BodyParser.swift in Sources */ = {isa = PBXBuildFile; fileRef = OBJ_107 /* BodyParser.swift */; };
		OBJ_761 /* BodyParserProtocol.swift in Sources */ = {isa = PBXBuildFile; fileRef = OBJ_108 /* BodyParserProtocol.swift */; };
		OBJ_762 /* JSONBodyParser.swift in Sources */ = {isa = PBXBuildFile; fileRef = OBJ_109 /* JSONBodyParser.swift */; };
		OBJ_763 /* MultiPartBodyParser.swift in Sources */ = {isa = PBXBuildFile; fileRef = OBJ_110 /* MultiPartBodyParser.swift */; };
		OBJ_764 /* ParsedBody.swift in Sources */ = {isa = PBXBuildFile; fileRef = OBJ_111 /* ParsedBody.swift */; };
		OBJ_765 /* Part.swift in Sources */ = {isa = PBXBuildFile; fileRef = OBJ_112 /* Part.swift */; };
		OBJ_766 /* RawBodyParser.swift in Sources */ = {isa = PBXBuildFile; fileRef = OBJ_113 /* RawBodyParser.swift */; };
		OBJ_767 /* TextBodyParser.swift in Sources */ = {isa = PBXBuildFile; fileRef = OBJ_114 /* TextBodyParser.swift */; };
		OBJ_768 /* URLEncodedBodyParser.swift in Sources */ = {isa = PBXBuildFile; fileRef = OBJ_115 /* URLEncodedBodyParser.swift */; };
		OBJ_769 /* ContentType.swift in Sources */ = {isa = PBXBuildFile; fileRef = OBJ_117 /* ContentType.swift */; };
		OBJ_770 /* types.swift in Sources */ = {isa = PBXBuildFile; fileRef = OBJ_118 /* types.swift */; };
		OBJ_771 /* CacheRelatedHeadersSetter.swift in Sources */ = {isa = PBXBuildFile; fileRef = OBJ_120 /* CacheRelatedHeadersSetter.swift */; };
		OBJ_772 /* CompositeHeadersSetter.swift in Sources */ = {isa = PBXBuildFile; fileRef = OBJ_121 /* CompositeHeadersSetter.swift */; };
		OBJ_773 /* FileServer.swift in Sources */ = {isa = PBXBuildFile; fileRef = OBJ_122 /* FileServer.swift */; };
		OBJ_774 /* ResourcePathHandler.swift in Sources */ = {isa = PBXBuildFile; fileRef = OBJ_123 /* ResourcePathHandler.swift */; };
		OBJ_775 /* ResponseHeadersSetter.swift in Sources */ = {isa = PBXBuildFile; fileRef = OBJ_124 /* ResponseHeadersSetter.swift */; };
		OBJ_776 /* StaticFileServer.swift in Sources */ = {isa = PBXBuildFile; fileRef = OBJ_125 /* StaticFileServer.swift */; };
		OBJ_778 /* KituraTemplateEngine.framework in Frameworks */ = {isa = PBXBuildFile; fileRef = "Kitura-TemplateEngine::KituraTemplateEngine::Product" /* KituraTemplateEngine.framework */; };
		OBJ_779 /* SwiftyJSON.framework in Frameworks */ = {isa = PBXBuildFile; fileRef = "SwiftyJSON::SwiftyJSON::Product" /* SwiftyJSON.framework */; };
		OBJ_780 /* KituraNet.framework in Frameworks */ = {isa = PBXBuildFile; fileRef = "Kitura-net::KituraNet::Product" /* KituraNet.framework */; };
		OBJ_781 /* SSLService.framework in Frameworks */ = {isa = PBXBuildFile; fileRef = "SSLService::SSLService::Product" /* SSLService.framework */; };
		OBJ_782 /* Socket.framework in Frameworks */ = {isa = PBXBuildFile; fileRef = "Socket::Socket::Product" /* Socket.framework */; };
		OBJ_783 /* LoggerAPI.framework in Frameworks */ = {isa = PBXBuildFile; fileRef = "LoggerAPI::LoggerAPI::Product" /* LoggerAPI.framework */; };
		OBJ_784 /* CHTTPParser.framework in Frameworks */ = {isa = PBXBuildFile; fileRef = "Kitura-net::CHTTPParser::Product" /* CHTTPParser.framework */; };
		OBJ_796 /* TemplateEngine.swift in Sources */ = {isa = PBXBuildFile; fileRef = OBJ_129 /* TemplateEngine.swift */; };
		OBJ_802 /* LclJSONSerialization.swift in Sources */ = {isa = PBXBuildFile; fileRef = OBJ_133 /* LclJSONSerialization.swift */; };
		OBJ_803 /* SwiftyJSON.swift in Sources */ = {isa = PBXBuildFile; fileRef = OBJ_134 /* SwiftyJSON.swift */; };
		OBJ_809 /* BufferList.swift in Sources */ = {isa = PBXBuildFile; fileRef = OBJ_146 /* BufferList.swift */; };
		OBJ_810 /* ClientRequest.swift in Sources */ = {isa = PBXBuildFile; fileRef = OBJ_147 /* ClientRequest.swift */; };
		OBJ_811 /* ClientResponse.swift in Sources */ = {isa = PBXBuildFile; fileRef = OBJ_148 /* ClientResponse.swift */; };
		OBJ_812 /* ConnectionUpgradeFactory.swift in Sources */ = {isa = PBXBuildFile; fileRef = OBJ_149 /* ConnectionUpgradeFactory.swift */; };
		OBJ_813 /* ConnectionUpgrader.swift in Sources */ = {isa = PBXBuildFile; fileRef = OBJ_150 /* ConnectionUpgrader.swift */; };
		OBJ_814 /* Error.swift in Sources */ = {isa = PBXBuildFile; fileRef = OBJ_151 /* Error.swift */; };
		OBJ_815 /* FastCGI.swift in Sources */ = {isa = PBXBuildFile; fileRef = OBJ_153 /* FastCGI.swift */; };
		OBJ_816 /* FastCGIRecordCreate.swift in Sources */ = {isa = PBXBuildFile; fileRef = OBJ_154 /* FastCGIRecordCreate.swift */; };
		OBJ_817 /* FastCGIRecordParser.swift in Sources */ = {isa = PBXBuildFile; fileRef = OBJ_155 /* FastCGIRecordParser.swift */; };
		OBJ_818 /* FastCGIServer.swift in Sources */ = {isa = PBXBuildFile; fileRef = OBJ_156 /* FastCGIServer.swift */; };
		OBJ_819 /* FastCGIServerRequest.swift in Sources */ = {isa = PBXBuildFile; fileRef = OBJ_157 /* FastCGIServerRequest.swift */; };
		OBJ_820 /* FastCGIServerResponse.swift in Sources */ = {isa = PBXBuildFile; fileRef = OBJ_158 /* FastCGIServerResponse.swift */; };
		OBJ_821 /* HTTP.swift in Sources */ = {isa = PBXBuildFile; fileRef = OBJ_160 /* HTTP.swift */; };
		OBJ_822 /* HTTPServer.swift in Sources */ = {isa = PBXBuildFile; fileRef = OBJ_161 /* HTTPServer.swift */; };
		OBJ_823 /* HTTPServerRequest.swift in Sources */ = {isa = PBXBuildFile; fileRef = OBJ_162 /* HTTPServerRequest.swift */; };
		OBJ_824 /* HTTPServerResponse.swift in Sources */ = {isa = PBXBuildFile; fileRef = OBJ_163 /* HTTPServerResponse.swift */; };
		OBJ_825 /* IncomingHTTPSocketProcessor.swift in Sources */ = {isa = PBXBuildFile; fileRef = OBJ_164 /* IncomingHTTPSocketProcessor.swift */; };
		OBJ_826 /* KeepAliveState.swift in Sources */ = {isa = PBXBuildFile; fileRef = OBJ_165 /* KeepAliveState.swift */; };
		OBJ_827 /* HTTPParser.swift in Sources */ = {isa = PBXBuildFile; fileRef = OBJ_167 /* HTTPParser.swift */; };
		OBJ_828 /* HTTPParserStatus.swift in Sources */ = {isa = PBXBuildFile; fileRef = OBJ_168 /* HTTPParserStatus.swift */; };
		OBJ_829 /* ParseResults.swift in Sources */ = {isa = PBXBuildFile; fileRef = OBJ_169 /* ParseResults.swift */; };
		OBJ_830 /* URLParser.swift in Sources */ = {isa = PBXBuildFile; fileRef = OBJ_170 /* URLParser.swift */; };
		OBJ_831 /* HeadersContainer.swift in Sources */ = {isa = PBXBuildFile; fileRef = OBJ_171 /* HeadersContainer.swift */; };
		OBJ_832 /* IncomingSocketHandler.swift in Sources */ = {isa = PBXBuildFile; fileRef = OBJ_172 /* IncomingSocketHandler.swift */; };
		OBJ_833 /* IncomingSocketManager.swift in Sources */ = {isa = PBXBuildFile; fileRef = OBJ_173 /* IncomingSocketManager.swift */; };
		OBJ_834 /* IncomingSocketProcessor.swift in Sources */ = {isa = PBXBuildFile; fileRef = OBJ_174 /* IncomingSocketProcessor.swift */; };
		OBJ_835 /* IncomingSocketProcessorCreator.swift in Sources */ = {isa = PBXBuildFile; fileRef = OBJ_175 /* IncomingSocketProcessorCreator.swift */; };
		OBJ_836 /* ListenerGroup.swift in Sources */ = {isa = PBXBuildFile; fileRef = OBJ_176 /* ListenerGroup.swift */; };
		OBJ_837 /* SPIUtils.swift in Sources */ = {isa = PBXBuildFile; fileRef = OBJ_177 /* SPIUtils.swift */; };
		OBJ_838 /* Server.swift in Sources */ = {isa = PBXBuildFile; fileRef = OBJ_179 /* Server.swift */; };
		OBJ_839 /* ServerDelegate.swift in Sources */ = {isa = PBXBuildFile; fileRef = OBJ_180 /* ServerDelegate.swift */; };
		OBJ_840 /* ServerLifecycleListener.swift in Sources */ = {isa = PBXBuildFile; fileRef = OBJ_181 /* ServerLifecycleListener.swift */; };
		OBJ_841 /* ServerMonitor.swift in Sources */ = {isa = PBXBuildFile; fileRef = OBJ_182 /* ServerMonitor.swift */; };
		OBJ_842 /* ServerState.swift in Sources */ = {isa = PBXBuildFile; fileRef = OBJ_183 /* ServerState.swift */; };
		OBJ_843 /* ServerRequest.swift in Sources */ = {isa = PBXBuildFile; fileRef = OBJ_184 /* ServerRequest.swift */; };
		OBJ_844 /* ServerResponse.swift in Sources */ = {isa = PBXBuildFile; fileRef = OBJ_185 /* ServerResponse.swift */; };
		OBJ_846 /* SSLService.framework in Frameworks */ = {isa = PBXBuildFile; fileRef = "SSLService::SSLService::Product" /* SSLService.framework */; };
		OBJ_847 /* Socket.framework in Frameworks */ = {isa = PBXBuildFile; fileRef = "Socket::Socket::Product" /* Socket.framework */; };
		OBJ_848 /* LoggerAPI.framework in Frameworks */ = {isa = PBXBuildFile; fileRef = "LoggerAPI::LoggerAPI::Product" /* LoggerAPI.framework */; };
		OBJ_849 /* CHTTPParser.framework in Frameworks */ = {isa = PBXBuildFile; fileRef = "Kitura-net::CHTTPParser::Product" /* CHTTPParser.framework */; };
		OBJ_858 /* SSLService.swift in Sources */ = {isa = PBXBuildFile; fileRef = OBJ_189 /* SSLService.swift */; };
		OBJ_860 /* Socket.framework in Frameworks */ = {isa = PBXBuildFile; fileRef = "Socket::Socket::Product" /* Socket.framework */; };
		OBJ_866 /* http_parser.c in Sources */ = {isa = PBXBuildFile; fileRef = OBJ_138 /* http_parser.c */; };
		OBJ_867 /* utils.c in Sources */ = {isa = PBXBuildFile; fileRef = OBJ_139 /* utils.c */; };
		OBJ_873 /* MySQLConnection.swift in Sources */ = {isa = PBXBuildFile; fileRef = OBJ_193 /* MySQLConnection.swift */; };
		OBJ_874 /* MySQLPreparedStatement.swift in Sources */ = {isa = PBXBuildFile; fileRef = OBJ_194 /* MySQLPreparedStatement.swift */; };
		OBJ_875 /* MySQLResultFetcher.swift in Sources */ = {isa = PBXBuildFile; fileRef = OBJ_195 /* MySQLResultFetcher.swift */; };
		OBJ_876 /* MySQLThreadSafeConnection.swift in Sources */ = {isa = PBXBuildFile; fileRef = OBJ_196 /* MySQLThreadSafeConnection.swift */; };
		OBJ_878 /* SwiftKuery.framework in Frameworks */ = {isa = PBXBuildFile; fileRef = "SwiftKuery::SwiftKuery::Product" /* SwiftKuery.framework */; };
		OBJ_884 /* AggregateColumnExpression.swift in Sources */ = {isa = PBXBuildFile; fileRef = OBJ_200 /* AggregateColumnExpression.swift */; };
		OBJ_885 /* AuxiliaryTable.swift in Sources */ = {isa = PBXBuildFile; fileRef = OBJ_201 /* AuxiliaryTable.swift */; };
		OBJ_886 /* Buildable.swift in Sources */ = {isa = PBXBuildFile; fileRef = OBJ_202 /* Buildable.swift */; };
		OBJ_887 /* Column.swift in Sources */ = {isa = PBXBuildFile; fileRef = OBJ_203 /* Column.swift */; };
		OBJ_888 /* ColumnAndExpressions_Extensions.swift in Sources */ = {isa = PBXBuildFile; fileRef = OBJ_204 /* ColumnAndExpressions_Extensions.swift */; };
		OBJ_889 /* Condition.swift in Sources */ = {isa = PBXBuildFile; fileRef = OBJ_205 /* Condition.swift */; };
		OBJ_890 /* ConditionalClause.swift in Sources */ = {isa = PBXBuildFile; fileRef = OBJ_206 /* ConditionalClause.swift */; };
		OBJ_891 /* Connection.swift in Sources */ = {isa = PBXBuildFile; fileRef = OBJ_207 /* Connection.swift */; };
		OBJ_892 /* ConnectionPool.swift in Sources */ = {isa = PBXBuildFile; fileRef = OBJ_208 /* ConnectionPool.swift */; };
		OBJ_893 /* ConnectionPoolConnection.swift in Sources */ = {isa = PBXBuildFile; fileRef = OBJ_209 /* ConnectionPoolConnection.swift */; };
		OBJ_894 /* ConnectionPoolOptions.swift in Sources */ = {isa = PBXBuildFile; fileRef = OBJ_210 /* ConnectionPoolOptions.swift */; };
		OBJ_895 /* Delete.swift in Sources */ = {isa = PBXBuildFile; fileRef = OBJ_211 /* Delete.swift */; };
		OBJ_896 /* Field.swift in Sources */ = {isa = PBXBuildFile; fileRef = OBJ_212 /* Field.swift */; };
		OBJ_897 /* Filter.swift in Sources */ = {isa = PBXBuildFile; fileRef = OBJ_213 /* Filter.swift */; };
		OBJ_898 /* FilterAndHaving_Extensions.swift in Sources */ = {isa = PBXBuildFile; fileRef = OBJ_214 /* FilterAndHaving_Extensions.swift */; };
		OBJ_899 /* FilterAndHaving_GlobalFunctions.swift in Sources */ = {isa = PBXBuildFile; fileRef = OBJ_215 /* FilterAndHaving_GlobalFunctions.swift */; };
		OBJ_900 /* Having.swift in Sources */ = {isa = PBXBuildFile; fileRef = OBJ_216 /* Having.swift */; };
		OBJ_901 /* Index.swift in Sources */ = {isa = PBXBuildFile; fileRef = OBJ_217 /* Index.swift */; };
		OBJ_902 /* IndexColumn.swift in Sources */ = {isa = PBXBuildFile; fileRef = OBJ_218 /* IndexColumn.swift */; };
		OBJ_903 /* IndexColumnOrdered.swift in Sources */ = {isa = PBXBuildFile; fileRef = OBJ_219 /* IndexColumnOrdered.swift */; };
		OBJ_904 /* Insert.swift in Sources */ = {isa = PBXBuildFile; fileRef = OBJ_220 /* Insert.swift */; };
		OBJ_905 /* Join.swift in Sources */ = {isa = PBXBuildFile; fileRef = OBJ_221 /* Join.swift */; };
		OBJ_906 /* Migration.swift in Sources */ = {isa = PBXBuildFile; fileRef = OBJ_222 /* Migration.swift */; };
		OBJ_907 /* OrderBy.swift in Sources */ = {isa = PBXBuildFile; fileRef = OBJ_223 /* OrderBy.swift */; };
		OBJ_908 /* Parameter.swift in Sources */ = {isa = PBXBuildFile; fileRef = OBJ_224 /* Parameter.swift */; };
		OBJ_909 /* Predicate.swift in Sources */ = {isa = PBXBuildFile; fileRef = OBJ_225 /* Predicate.swift */; };
		OBJ_910 /* PreparedStatement.swift in Sources */ = {isa = PBXBuildFile; fileRef = OBJ_226 /* PreparedStatement.swift */; };
		OBJ_911 /* Query.swift in Sources */ = {isa = PBXBuildFile; fileRef = OBJ_227 /* Query.swift */; };
		OBJ_912 /* QueryBuilder.swift in Sources */ = {isa = PBXBuildFile; fileRef = OBJ_228 /* QueryBuilder.swift */; };
		OBJ_913 /* QueryError.swift in Sources */ = {isa = PBXBuildFile; fileRef = OBJ_229 /* QueryError.swift */; };
		OBJ_914 /* QueryResult.swift in Sources */ = {isa = PBXBuildFile; fileRef = OBJ_230 /* QueryResult.swift */; };
		OBJ_915 /* QuerySuffixProtocol.swift in Sources */ = {isa = PBXBuildFile; fileRef = OBJ_231 /* QuerySuffixProtocol.swift */; };
		OBJ_916 /* Raw.swift in Sources */ = {isa = PBXBuildFile; fileRef = OBJ_232 /* Raw.swift */; };
		OBJ_917 /* RawField.swift in Sources */ = {isa = PBXBuildFile; fileRef = OBJ_233 /* RawField.swift */; };
		OBJ_918 /* ResultFetcher.swift in Sources */ = {isa = PBXBuildFile; fileRef = OBJ_234 /* ResultFetcher.swift */; };
		OBJ_919 /* ResultSet.swift in Sources */ = {isa = PBXBuildFile; fileRef = OBJ_235 /* ResultSet.swift */; };
		OBJ_920 /* RowSequence.swift in Sources */ = {isa = PBXBuildFile; fileRef = OBJ_236 /* RowSequence.swift */; };
		OBJ_921 /* SQLDataType.swift in Sources */ = {isa = PBXBuildFile; fileRef = OBJ_237 /* SQLDataType.swift */; };
		OBJ_922 /* ScalarColumnExpression.swift in Sources */ = {isa = PBXBuildFile; fileRef = OBJ_238 /* ScalarColumnExpression.swift */; };
		OBJ_923 /* Select.swift in Sources */ = {isa = PBXBuildFile; fileRef = OBJ_239 /* Select.swift */; };
		OBJ_924 /* SpecialOperators_Extensions.swift in Sources */ = {isa = PBXBuildFile; fileRef = OBJ_240 /* SpecialOperators_Extensions.swift */; };
		OBJ_925 /* String+Buildable.swift in Sources */ = {isa = PBXBuildFile; fileRef = OBJ_241 /* String+Buildable.swift */; };
		OBJ_926 /* Subqueries_GlobalFunctionsAndExtensions.swift in Sources */ = {isa = PBXBuildFile; fileRef = OBJ_242 /* Subqueries_GlobalFunctionsAndExtensions.swift */; };
		OBJ_927 /* Table.swift in Sources */ = {isa = PBXBuildFile; fileRef = OBJ_243 /* Table.swift */; };
		OBJ_928 /* Union.swift in Sources */ = {isa = PBXBuildFile; fileRef = OBJ_244 /* Union.swift */; };
		OBJ_929 /* Update.swift in Sources */ = {isa = PBXBuildFile; fileRef = OBJ_245 /* Update.swift */; };
		OBJ_930 /* Utils.swift in Sources */ = {isa = PBXBuildFile; fileRef = OBJ_246 /* Utils.swift */; };
		OBJ_931 /* With.swift in Sources */ = {isa = PBXBuildFile; fileRef = OBJ_247 /* With.swift */; };
		OBJ_937 /* AES.swift in Sources */ = {isa = PBXBuildFile; fileRef = OBJ_251 /* AES.swift */; };
		OBJ_938 /* Array+Extension.swift in Sources */ = {isa = PBXBuildFile; fileRef = OBJ_252 /* Array+Extension.swift */; };
		OBJ_939 /* Authenticator.swift in Sources */ = {isa = PBXBuildFile; fileRef = OBJ_253 /* Authenticator.swift */; };
		OBJ_940 /* BatchedCollection.swift in Sources */ = {isa = PBXBuildFile; fileRef = OBJ_254 /* BatchedCollection.swift */; };
		OBJ_941 /* Bit.swift in Sources */ = {isa = PBXBuildFile; fileRef = OBJ_255 /* Bit.swift */; };
		OBJ_942 /* BlockCipher.swift in Sources */ = {isa = PBXBuildFile; fileRef = OBJ_256 /* BlockCipher.swift */; };
		OBJ_943 /* BlockMode.swift in Sources */ = {isa = PBXBuildFile; fileRef = OBJ_258 /* BlockMode.swift */; };
		OBJ_944 /* BlockModeOptions.swift in Sources */ = {isa = PBXBuildFile; fileRef = OBJ_259 /* BlockModeOptions.swift */; };
		OBJ_945 /* BlockModeWorker.swift in Sources */ = {isa = PBXBuildFile; fileRef = OBJ_260 /* BlockModeWorker.swift */; };
		OBJ_946 /* CBC.swift in Sources */ = {isa = PBXBuildFile; fileRef = OBJ_261 /* CBC.swift */; };
		OBJ_947 /* CFB.swift in Sources */ = {isa = PBXBuildFile; fileRef = OBJ_262 /* CFB.swift */; };
		OBJ_948 /* CTR.swift in Sources */ = {isa = PBXBuildFile; fileRef = OBJ_263 /* CTR.swift */; };
		OBJ_949 /* ECB.swift in Sources */ = {isa = PBXBuildFile; fileRef = OBJ_264 /* ECB.swift */; };
		OBJ_950 /* OFB.swift in Sources */ = {isa = PBXBuildFile; fileRef = OBJ_265 /* OFB.swift */; };
		OBJ_951 /* PCBC.swift in Sources */ = {isa = PBXBuildFile; fileRef = OBJ_266 /* PCBC.swift */; };
		OBJ_952 /* RandomAccessBlockModeWorker.swift in Sources */ = {isa = PBXBuildFile; fileRef = OBJ_267 /* RandomAccessBlockModeWorker.swift */; };
		OBJ_953 /* Blowfish.swift in Sources */ = {isa = PBXBuildFile; fileRef = OBJ_268 /* Blowfish.swift */; };
		OBJ_954 /* CSArrayType+Extensions.swift in Sources */ = {isa = PBXBuildFile; fileRef = OBJ_269 /* CSArrayType+Extensions.swift */; };
		OBJ_955 /* ChaCha20.swift in Sources */ = {isa = PBXBuildFile; fileRef = OBJ_270 /* ChaCha20.swift */; };
		OBJ_956 /* Checksum.swift in Sources */ = {isa = PBXBuildFile; fileRef = OBJ_271 /* Checksum.swift */; };
		OBJ_957 /* Cipher.swift in Sources */ = {isa = PBXBuildFile; fileRef = OBJ_272 /* Cipher.swift */; };
		OBJ_958 /* Collection+Extension.swift in Sources */ = {isa = PBXBuildFile; fileRef = OBJ_273 /* Collection+Extension.swift */; };
		OBJ_959 /* Cryptors.swift in Sources */ = {isa = PBXBuildFile; fileRef = OBJ_274 /* Cryptors.swift */; };
		OBJ_960 /* Digest.swift in Sources */ = {isa = PBXBuildFile; fileRef = OBJ_275 /* Digest.swift */; };
		OBJ_961 /* DigestType.swift in Sources */ = {isa = PBXBuildFile; fileRef = OBJ_276 /* DigestType.swift */; };
		OBJ_962 /* AES+Foundation.swift in Sources */ = {isa = PBXBuildFile; fileRef = OBJ_278 /* AES+Foundation.swift */; };
		OBJ_963 /* Blowfish+Foundation.swift in Sources */ = {isa = PBXBuildFile; fileRef = OBJ_279 /* Blowfish+Foundation.swift */; };
		OBJ_964 /* CSArrayType+Foundation.swift in Sources */ = {isa = PBXBuildFile; fileRef = OBJ_280 /* CSArrayType+Foundation.swift */; };
		OBJ_965 /* ChaCha20+Foundation.swift in Sources */ = {isa = PBXBuildFile; fileRef = OBJ_281 /* ChaCha20+Foundation.swift */; };
		OBJ_966 /* Data+Extension.swift in Sources */ = {isa = PBXBuildFile; fileRef = OBJ_282 /* Data+Extension.swift */; };
		OBJ_967 /* HMAC+Foundation.swift in Sources */ = {isa = PBXBuildFile; fileRef = OBJ_283 /* HMAC+Foundation.swift */; };
		OBJ_968 /* Rabbit+Foundation.swift in Sources */ = {isa = PBXBuildFile; fileRef = OBJ_284 /* Rabbit+Foundation.swift */; };
		OBJ_969 /* String+FoundationExtension.swift in Sources */ = {isa = PBXBuildFile; fileRef = OBJ_285 /* String+FoundationExtension.swift */; };
		OBJ_970 /* Utils+Foundation.swift in Sources */ = {isa = PBXBuildFile; fileRef = OBJ_286 /* Utils+Foundation.swift */; };
		OBJ_971 /* Generics.swift in Sources */ = {isa = PBXBuildFile; fileRef = OBJ_287 /* Generics.swift */; };
		OBJ_972 /* HMAC.swift in Sources */ = {isa = PBXBuildFile; fileRef = OBJ_288 /* HMAC.swift */; };
		OBJ_973 /* Int+Extension.swift in Sources */ = {isa = PBXBuildFile; fileRef = OBJ_289 /* Int+Extension.swift */; };
		OBJ_974 /* MD5.swift in Sources */ = {isa = PBXBuildFile; fileRef = OBJ_290 /* MD5.swift */; };
		OBJ_975 /* NoPadding.swift in Sources */ = {isa = PBXBuildFile; fileRef = OBJ_291 /* NoPadding.swift */; };
		OBJ_976 /* Operators.swift in Sources */ = {isa = PBXBuildFile; fileRef = OBJ_292 /* Operators.swift */; };
		OBJ_977 /* PBKDF1.swift in Sources */ = {isa = PBXBuildFile; fileRef = OBJ_294 /* PBKDF1.swift */; };
		OBJ_978 /* PBKDF2.swift in Sources */ = {isa = PBXBuildFile; fileRef = OBJ_295 /* PBKDF2.swift */; };
		OBJ_979 /* PKCS5.swift in Sources */ = {isa = PBXBuildFile; fileRef = OBJ_296 /* PKCS5.swift */; };
		OBJ_980 /* PKCS7.swift in Sources */ = {isa = PBXBuildFile; fileRef = OBJ_297 /* PKCS7.swift */; };
		OBJ_981 /* PKCS7Padding.swift in Sources */ = {isa = PBXBuildFile; fileRef = OBJ_298 /* PKCS7Padding.swift */; };
		OBJ_982 /* Padding.swift in Sources */ = {isa = PBXBuildFile; fileRef = OBJ_299 /* Padding.swift */; };
		OBJ_983 /* Poly1305.swift in Sources */ = {isa = PBXBuildFile; fileRef = OBJ_300 /* Poly1305.swift */; };
		OBJ_984 /* Rabbit.swift in Sources */ = {isa = PBXBuildFile; fileRef = OBJ_301 /* Rabbit.swift */; };
		OBJ_985 /* RandomAccessCryptor.swift in Sources */ = {isa = PBXBuildFile; fileRef = OBJ_302 /* RandomAccessCryptor.swift */; };
		OBJ_986 /* RandomBytesSequence.swift in Sources */ = {isa = PBXBuildFile; fileRef = OBJ_303 /* RandomBytesSequence.swift */; };
		OBJ_987 /* SHA1.swift in Sources */ = {isa = PBXBuildFile; fileRef = OBJ_304 /* SHA1.swift */; };
		OBJ_988 /* SHA2.swift in Sources */ = {isa = PBXBuildFile; fileRef = OBJ_305 /* SHA2.swift */; };
		OBJ_989 /* SHA3.swift in Sources */ = {isa = PBXBuildFile; fileRef = OBJ_306 /* SHA3.swift */; };
		OBJ_990 /* SecureBytes.swift in Sources */ = {isa = PBXBuildFile; fileRef = OBJ_307 /* SecureBytes.swift */; };
		OBJ_991 /* String+Extension.swift in Sources */ = {isa = PBXBuildFile; fileRef = OBJ_308 /* String+Extension.swift */; };
		OBJ_992 /* UInt16+Extension.swift in Sources */ = {isa = PBXBuildFile; fileRef = OBJ_309 /* UInt16+Extension.swift */; };
		OBJ_993 /* UInt32+Extension.swift in Sources */ = {isa = PBXBuildFile; fileRef = OBJ_310 /* UInt32+Extension.swift */; };
		OBJ_994 /* UInt64+Extension.swift in Sources */ = {isa = PBXBuildFile; fileRef = OBJ_311 /* UInt64+Extension.swift */; };
		OBJ_995 /* UInt8+Extension.swift in Sources */ = {isa = PBXBuildFile; fileRef = OBJ_312 /* UInt8+Extension.swift */; };
		OBJ_996 /* Updatable.swift in Sources */ = {isa = PBXBuildFile; fileRef = OBJ_313 /* Updatable.swift */; };
		OBJ_997 /* Utils.swift in Sources */ = {isa = PBXBuildFile; fileRef = OBJ_314 /* Utils.swift */; };
		OBJ_998 /* ZeroPadding.swift in Sources */ = {isa = PBXBuildFile; fileRef = OBJ_315 /* ZeroPadding.swift */; };
/* End PBXBuildFile section */

/* Begin PBXContainerItemProxy section */
		99A5E50B1F7943EB006A38C6 /* PBXContainerItemProxy */ = {
			isa = PBXContainerItemProxy;
			containerPortal = OBJ_1 /* Project object */;
			proxyType = 1;
			remoteGlobalIDString = "mikrotik_router_manager::CORE";
			remoteInfo = CORE;
		};
		99A5E50C1F7943EB006A38C6 /* PBXContainerItemProxy */ = {
			isa = PBXContainerItemProxy;
			containerPortal = OBJ_1 /* Project object */;
			proxyType = 1;
			remoteGlobalIDString = "KituraCORS::KituraCORS";
			remoteInfo = KituraCORS;
		};
		99A5E50D1F7943EB006A38C6 /* PBXContainerItemProxy */ = {
			isa = PBXContainerItemProxy;
			containerPortal = OBJ_1 /* Project object */;
			proxyType = 1;
			remoteGlobalIDString = "Kitura::Kitura";
			remoteInfo = Kitura;
		};
		99A5E50E1F7943EB006A38C6 /* PBXContainerItemProxy */ = {
			isa = PBXContainerItemProxy;
			containerPortal = OBJ_1 /* Project object */;
			proxyType = 1;
			remoteGlobalIDString = "Kitura-TemplateEngine::KituraTemplateEngine";
			remoteInfo = KituraTemplateEngine;
		};
		99A5E50F1F7943EB006A38C6 /* PBXContainerItemProxy */ = {
			isa = PBXContainerItemProxy;
			containerPortal = OBJ_1 /* Project object */;
			proxyType = 1;
			remoteGlobalIDString = "SwiftyJSON::SwiftyJSON";
			remoteInfo = SwiftyJSON;
		};
		99A5E5101F7943EB006A38C6 /* PBXContainerItemProxy */ = {
			isa = PBXContainerItemProxy;
			containerPortal = OBJ_1 /* Project object */;
			proxyType = 1;
			remoteGlobalIDString = "Kitura-net::KituraNet";
			remoteInfo = KituraNet;
		};
		99A5E5111F7943EB006A38C6 /* PBXContainerItemProxy */ = {
			isa = PBXContainerItemProxy;
			containerPortal = OBJ_1 /* Project object */;
			proxyType = 1;
			remoteGlobalIDString = "SSLService::SSLService";
			remoteInfo = SSLService;
		};
		99A5E5121F7943EB006A38C6 /* PBXContainerItemProxy */ = {
			isa = PBXContainerItemProxy;
			containerPortal = OBJ_1 /* Project object */;
			proxyType = 1;
			remoteGlobalIDString = "Socket::Socket";
			remoteInfo = Socket;
		};
		99A5E5131F7943EB006A38C6 /* PBXContainerItemProxy */ = {
			isa = PBXContainerItemProxy;
			containerPortal = OBJ_1 /* Project object */;
			proxyType = 1;
			remoteGlobalIDString = "Socket::Socket";
			remoteInfo = Socket;
		};
		99A5E5141F7943EB006A38C6 /* PBXContainerItemProxy */ = {
			isa = PBXContainerItemProxy;
			containerPortal = OBJ_1 /* Project object */;
			proxyType = 1;
			remoteGlobalIDString = "LoggerAPI::LoggerAPI";
			remoteInfo = LoggerAPI;
		};
		99A5E5151F7943EB006A38C6 /* PBXContainerItemProxy */ = {
			isa = PBXContainerItemProxy;
			containerPortal = OBJ_1 /* Project object */;
			proxyType = 1;
			remoteGlobalIDString = "Kitura-net::CHTTPParser";
			remoteInfo = CHTTPParser;
		};
		99A5E5161F7943EB006A38C6 /* PBXContainerItemProxy */ = {
			isa = PBXContainerItemProxy;
			containerPortal = OBJ_1 /* Project object */;
			proxyType = 1;
			remoteGlobalIDString = "SSLService::SSLService";
			remoteInfo = SSLService;
		};
		99A5E5171F7943EB006A38C6 /* PBXContainerItemProxy */ = {
			isa = PBXContainerItemProxy;
			containerPortal = OBJ_1 /* Project object */;
			proxyType = 1;
			remoteGlobalIDString = "Socket::Socket";
			remoteInfo = Socket;
		};
		99A5E5181F7943EB006A38C6 /* PBXContainerItemProxy */ = {
			isa = PBXContainerItemProxy;
			containerPortal = OBJ_1 /* Project object */;
			proxyType = 1;
			remoteGlobalIDString = "LoggerAPI::LoggerAPI";
			remoteInfo = LoggerAPI;
		};
		99A5E5191F7943EB006A38C6 /* PBXContainerItemProxy */ = {
			isa = PBXContainerItemProxy;
			containerPortal = OBJ_1 /* Project object */;
			proxyType = 1;
			remoteGlobalIDString = "Kitura-net::CHTTPParser";
			remoteInfo = CHTTPParser;
		};
		99A5E51A1F7943EB006A38C6 /* PBXContainerItemProxy */ = {
			isa = PBXContainerItemProxy;
			containerPortal = OBJ_1 /* Project object */;
			proxyType = 1;
			remoteGlobalIDString = "Kitura-TemplateEngine::KituraTemplateEngine";
			remoteInfo = KituraTemplateEngine;
		};
		99A5E51B1F7943EB006A38C6 /* PBXContainerItemProxy */ = {
			isa = PBXContainerItemProxy;
			containerPortal = OBJ_1 /* Project object */;
			proxyType = 1;
			remoteGlobalIDString = "SwiftyJSON::SwiftyJSON";
			remoteInfo = SwiftyJSON;
		};
		99A5E51C1F7943EB006A38C6 /* PBXContainerItemProxy */ = {
			isa = PBXContainerItemProxy;
			containerPortal = OBJ_1 /* Project object */;
			proxyType = 1;
			remoteGlobalIDString = "Kitura-net::KituraNet";
			remoteInfo = KituraNet;
		};
		99A5E51D1F7943EB006A38C6 /* PBXContainerItemProxy */ = {
			isa = PBXContainerItemProxy;
			containerPortal = OBJ_1 /* Project object */;
			proxyType = 1;
			remoteGlobalIDString = "SSLService::SSLService";
			remoteInfo = SSLService;
		};
		99A5E51E1F7943EB006A38C6 /* PBXContainerItemProxy */ = {
			isa = PBXContainerItemProxy;
			containerPortal = OBJ_1 /* Project object */;
			proxyType = 1;
			remoteGlobalIDString = "Socket::Socket";
			remoteInfo = Socket;
		};
		99A5E51F1F7943EB006A38C6 /* PBXContainerItemProxy */ = {
			isa = PBXContainerItemProxy;
			containerPortal = OBJ_1 /* Project object */;
			proxyType = 1;
			remoteGlobalIDString = "LoggerAPI::LoggerAPI";
			remoteInfo = LoggerAPI;
		};
		99A5E5201F7943EB006A38C6 /* PBXContainerItemProxy */ = {
			isa = PBXContainerItemProxy;
			containerPortal = OBJ_1 /* Project object */;
			proxyType = 1;
			remoteGlobalIDString = "Kitura-net::CHTTPParser";
			remoteInfo = CHTTPParser;
		};
		99A5E5211F7943EB006A38C6 /* PBXContainerItemProxy */ = {
			isa = PBXContainerItemProxy;
			containerPortal = OBJ_1 /* Project object */;
			proxyType = 1;
			remoteGlobalIDString = "HeliumLogger::HeliumLogger";
			remoteInfo = HeliumLogger;
		};
		99A5E5221F7943EB006A38C6 /* PBXContainerItemProxy */ = {
			isa = PBXContainerItemProxy;
			containerPortal = OBJ_1 /* Project object */;
			proxyType = 1;
			remoteGlobalIDString = "LoggerAPI::LoggerAPI";
			remoteInfo = LoggerAPI;
		};
		99A5E5231F7943EB006A38C6 /* PBXContainerItemProxy */ = {
			isa = PBXContainerItemProxy;
			containerPortal = OBJ_1 /* Project object */;
			proxyType = 1;
			remoteGlobalIDString = "Kitura-CredentialsHTTP::CredentialsHTTP";
			remoteInfo = CredentialsHTTP;
		};
		99A5E5241F7943EB006A38C6 /* PBXContainerItemProxy */ = {
			isa = PBXContainerItemProxy;
			containerPortal = OBJ_1 /* Project object */;
			proxyType = 1;
			remoteGlobalIDString = "Kitura-Credentials::Credentials";
			remoteInfo = Credentials;
		};
		99A5E5251F7943EB006A38C6 /* PBXContainerItemProxy */ = {
			isa = PBXContainerItemProxy;
			containerPortal = OBJ_1 /* Project object */;
			proxyType = 1;
			remoteGlobalIDString = "Kitura-Session::KituraSession";
			remoteInfo = KituraSession;
		};
		99A5E5261F7943EB006A38C6 /* PBXContainerItemProxy */ = {
			isa = PBXContainerItemProxy;
			containerPortal = OBJ_1 /* Project object */;
			proxyType = 1;
			remoteGlobalIDString = "Cryptor::Cryptor";
			remoteInfo = Cryptor;
		};
		99A5E5271F7943EB006A38C6 /* PBXContainerItemProxy */ = {
			isa = PBXContainerItemProxy;
			containerPortal = OBJ_1 /* Project object */;
			proxyType = 1;
			remoteGlobalIDString = "Kitura::Kitura";
			remoteInfo = Kitura;
		};
		99A5E5281F7943EB006A38C6 /* PBXContainerItemProxy */ = {
			isa = PBXContainerItemProxy;
			containerPortal = OBJ_1 /* Project object */;
			proxyType = 1;
			remoteGlobalIDString = "Kitura-TemplateEngine::KituraTemplateEngine";
			remoteInfo = KituraTemplateEngine;
		};
		99A5E5291F7943EB006A38C6 /* PBXContainerItemProxy */ = {
			isa = PBXContainerItemProxy;
			containerPortal = OBJ_1 /* Project object */;
			proxyType = 1;
			remoteGlobalIDString = "SwiftyJSON::SwiftyJSON";
			remoteInfo = SwiftyJSON;
		};
		99A5E52A1F7943EB006A38C6 /* PBXContainerItemProxy */ = {
			isa = PBXContainerItemProxy;
			containerPortal = OBJ_1 /* Project object */;
			proxyType = 1;
			remoteGlobalIDString = "Kitura-net::KituraNet";
			remoteInfo = KituraNet;
		};
		99A5E52B1F7943EB006A38C6 /* PBXContainerItemProxy */ = {
			isa = PBXContainerItemProxy;
			containerPortal = OBJ_1 /* Project object */;
			proxyType = 1;
			remoteGlobalIDString = "SSLService::SSLService";
			remoteInfo = SSLService;
		};
		99A5E52C1F7943EB006A38C6 /* PBXContainerItemProxy */ = {
			isa = PBXContainerItemProxy;
			containerPortal = OBJ_1 /* Project object */;
			proxyType = 1;
			remoteGlobalIDString = "Socket::Socket";
			remoteInfo = Socket;
		};
		99A5E52D1F7943EB006A38C6 /* PBXContainerItemProxy */ = {
			isa = PBXContainerItemProxy;
			containerPortal = OBJ_1 /* Project object */;
			proxyType = 1;
			remoteGlobalIDString = "LoggerAPI::LoggerAPI";
			remoteInfo = LoggerAPI;
		};
		99A5E52E1F7943EB006A38C6 /* PBXContainerItemProxy */ = {
			isa = PBXContainerItemProxy;
			containerPortal = OBJ_1 /* Project object */;
			proxyType = 1;
			remoteGlobalIDString = "Kitura-net::CHTTPParser";
			remoteInfo = CHTTPParser;
		};
		99A5E52F1F7943EB006A38C6 /* PBXContainerItemProxy */ = {
			isa = PBXContainerItemProxy;
			containerPortal = OBJ_1 /* Project object */;
			proxyType = 1;
			remoteGlobalIDString = "Cryptor::Cryptor";
			remoteInfo = Cryptor;
		};
		99A5E5301F7943EB006A38C6 /* PBXContainerItemProxy */ = {
			isa = PBXContainerItemProxy;
			containerPortal = OBJ_1 /* Project object */;
			proxyType = 1;
			remoteGlobalIDString = "Kitura::Kitura";
			remoteInfo = Kitura;
		};
		99A5E5311F7943EB006A38C6 /* PBXContainerItemProxy */ = {
			isa = PBXContainerItemProxy;
			containerPortal = OBJ_1 /* Project object */;
			proxyType = 1;
			remoteGlobalIDString = "Kitura-TemplateEngine::KituraTemplateEngine";
			remoteInfo = KituraTemplateEngine;
		};
		99A5E5321F7943EB006A38C6 /* PBXContainerItemProxy */ = {
			isa = PBXContainerItemProxy;
			containerPortal = OBJ_1 /* Project object */;
			proxyType = 1;
			remoteGlobalIDString = "SwiftyJSON::SwiftyJSON";
			remoteInfo = SwiftyJSON;
		};
		99A5E5331F7943EB006A38C6 /* PBXContainerItemProxy */ = {
			isa = PBXContainerItemProxy;
			containerPortal = OBJ_1 /* Project object */;
			proxyType = 1;
			remoteGlobalIDString = "Kitura-net::KituraNet";
			remoteInfo = KituraNet;
		};
		99A5E5341F7943EB006A38C6 /* PBXContainerItemProxy */ = {
			isa = PBXContainerItemProxy;
			containerPortal = OBJ_1 /* Project object */;
			proxyType = 1;
			remoteGlobalIDString = "SSLService::SSLService";
			remoteInfo = SSLService;
		};
		99A5E5351F7943EB006A38C6 /* PBXContainerItemProxy */ = {
			isa = PBXContainerItemProxy;
			containerPortal = OBJ_1 /* Project object */;
			proxyType = 1;
			remoteGlobalIDString = "Socket::Socket";
			remoteInfo = Socket;
		};
		99A5E5361F7943EB006A38C6 /* PBXContainerItemProxy */ = {
			isa = PBXContainerItemProxy;
			containerPortal = OBJ_1 /* Project object */;
			proxyType = 1;
			remoteGlobalIDString = "LoggerAPI::LoggerAPI";
			remoteInfo = LoggerAPI;
		};
		99A5E5371F7943EB006A38C6 /* PBXContainerItemProxy */ = {
			isa = PBXContainerItemProxy;
			containerPortal = OBJ_1 /* Project object */;
			proxyType = 1;
			remoteGlobalIDString = "Kitura-net::CHTTPParser";
			remoteInfo = CHTTPParser;
		};
		99A5E5381F7943EB006A38C6 /* PBXContainerItemProxy */ = {
			isa = PBXContainerItemProxy;
			containerPortal = OBJ_1 /* Project object */;
			proxyType = 1;
			remoteGlobalIDString = "Kitura-Session::KituraSession";
			remoteInfo = KituraSession;
		};
		99A5E5391F7943EB006A38C6 /* PBXContainerItemProxy */ = {
			isa = PBXContainerItemProxy;
			containerPortal = OBJ_1 /* Project object */;
			proxyType = 1;
			remoteGlobalIDString = "Cryptor::Cryptor";
			remoteInfo = Cryptor;
		};
		99A5E53A1F7943EB006A38C6 /* PBXContainerItemProxy */ = {
			isa = PBXContainerItemProxy;
			containerPortal = OBJ_1 /* Project object */;
			proxyType = 1;
			remoteGlobalIDString = "Kitura::Kitura";
			remoteInfo = Kitura;
		};
		99A5E53B1F7943EB006A38C6 /* PBXContainerItemProxy */ = {
			isa = PBXContainerItemProxy;
			containerPortal = OBJ_1 /* Project object */;
			proxyType = 1;
			remoteGlobalIDString = "Kitura-TemplateEngine::KituraTemplateEngine";
			remoteInfo = KituraTemplateEngine;
		};
		99A5E53C1F7943EB006A38C6 /* PBXContainerItemProxy */ = {
			isa = PBXContainerItemProxy;
			containerPortal = OBJ_1 /* Project object */;
			proxyType = 1;
			remoteGlobalIDString = "SwiftyJSON::SwiftyJSON";
			remoteInfo = SwiftyJSON;
		};
		99A5E53D1F7943EB006A38C6 /* PBXContainerItemProxy */ = {
			isa = PBXContainerItemProxy;
			containerPortal = OBJ_1 /* Project object */;
			proxyType = 1;
			remoteGlobalIDString = "Kitura-net::KituraNet";
			remoteInfo = KituraNet;
		};
		99A5E53E1F7943EB006A38C6 /* PBXContainerItemProxy */ = {
			isa = PBXContainerItemProxy;
			containerPortal = OBJ_1 /* Project object */;
			proxyType = 1;
			remoteGlobalIDString = "SSLService::SSLService";
			remoteInfo = SSLService;
		};
		99A5E53F1F7943EB006A38C6 /* PBXContainerItemProxy */ = {
			isa = PBXContainerItemProxy;
			containerPortal = OBJ_1 /* Project object */;
			proxyType = 1;
			remoteGlobalIDString = "Socket::Socket";
			remoteInfo = Socket;
		};
		99A5E5401F7943EB006A38C6 /* PBXContainerItemProxy */ = {
			isa = PBXContainerItemProxy;
			containerPortal = OBJ_1 /* Project object */;
			proxyType = 1;
			remoteGlobalIDString = "LoggerAPI::LoggerAPI";
			remoteInfo = LoggerAPI;
		};
		99A5E5411F7943EB006A38C6 /* PBXContainerItemProxy */ = {
			isa = PBXContainerItemProxy;
			containerPortal = OBJ_1 /* Project object */;
			proxyType = 1;
			remoteGlobalIDString = "Kitura-net::CHTTPParser";
			remoteInfo = CHTTPParser;
		};
		99A5E5421F7943EB006A38C6 /* PBXContainerItemProxy */ = {
			isa = PBXContainerItemProxy;
			containerPortal = OBJ_1 /* Project object */;
			proxyType = 1;
			remoteGlobalIDString = "Kitura-Credentials::Credentials";
			remoteInfo = Credentials;
		};
		99A5E5431F7943EB006A38C6 /* PBXContainerItemProxy */ = {
			isa = PBXContainerItemProxy;
			containerPortal = OBJ_1 /* Project object */;
			proxyType = 1;
			remoteGlobalIDString = "Kitura-Session::KituraSession";
			remoteInfo = KituraSession;
		};
		99A5E5441F7943EB006A38C6 /* PBXContainerItemProxy */ = {
			isa = PBXContainerItemProxy;
			containerPortal = OBJ_1 /* Project object */;
			proxyType = 1;
			remoteGlobalIDString = "Cryptor::Cryptor";
			remoteInfo = Cryptor;
		};
		99A5E5451F7943EB006A38C6 /* PBXContainerItemProxy */ = {
			isa = PBXContainerItemProxy;
			containerPortal = OBJ_1 /* Project object */;
			proxyType = 1;
			remoteGlobalIDString = "Kitura::Kitura";
			remoteInfo = Kitura;
		};
		99A5E5461F7943EB006A38C6 /* PBXContainerItemProxy */ = {
			isa = PBXContainerItemProxy;
			containerPortal = OBJ_1 /* Project object */;
			proxyType = 1;
			remoteGlobalIDString = "Kitura-TemplateEngine::KituraTemplateEngine";
			remoteInfo = KituraTemplateEngine;
		};
		99A5E5471F7943EB006A38C6 /* PBXContainerItemProxy */ = {
			isa = PBXContainerItemProxy;
			containerPortal = OBJ_1 /* Project object */;
			proxyType = 1;
			remoteGlobalIDString = "SwiftyJSON::SwiftyJSON";
			remoteInfo = SwiftyJSON;
		};
		99A5E5481F7943EB006A38C6 /* PBXContainerItemProxy */ = {
			isa = PBXContainerItemProxy;
			containerPortal = OBJ_1 /* Project object */;
			proxyType = 1;
			remoteGlobalIDString = "Kitura-net::KituraNet";
			remoteInfo = KituraNet;
		};
		99A5E5491F7943EB006A38C6 /* PBXContainerItemProxy */ = {
			isa = PBXContainerItemProxy;
			containerPortal = OBJ_1 /* Project object */;
			proxyType = 1;
			remoteGlobalIDString = "SSLService::SSLService";
			remoteInfo = SSLService;
		};
		99A5E54A1F7943EB006A38C6 /* PBXContainerItemProxy */ = {
			isa = PBXContainerItemProxy;
			containerPortal = OBJ_1 /* Project object */;
			proxyType = 1;
			remoteGlobalIDString = "Kitura-net::CHTTPParser";
			remoteInfo = CHTTPParser;
		};
		99A5E54B1F7943EB006A38C6 /* PBXContainerItemProxy */ = {
			isa = PBXContainerItemProxy;
			containerPortal = OBJ_1 /* Project object */;
			proxyType = 1;
			remoteGlobalIDString = "SwiftKueryMySQL::SwiftKueryMySQL";
			remoteInfo = SwiftKueryMySQL;
		};
		99A5E54C1F7943EB006A38C6 /* PBXContainerItemProxy */ = {
			isa = PBXContainerItemProxy;
			containerPortal = OBJ_1 /* Project object */;
			proxyType = 1;
			remoteGlobalIDString = "SwiftKuery::SwiftKuery";
			remoteInfo = SwiftKuery;
		};
		99A5E54D1F7943EB006A38C6 /* PBXContainerItemProxy */ = {
			isa = PBXContainerItemProxy;
			containerPortal = OBJ_1 /* Project object */;
			proxyType = 1;
			remoteGlobalIDString = "SwiftKuery::SwiftKuery";
			remoteInfo = SwiftKuery;
		};
		99A5E54E1F7943EB006A38C6 /* PBXContainerItemProxy */ = {
			isa = PBXContainerItemProxy;
			containerPortal = OBJ_1 /* Project object */;
			proxyType = 1;
			remoteGlobalIDString = "CryptoSwift::CryptoSwift";
			remoteInfo = CryptoSwift;
		};
		99A5E54F1F7943EB006A38C6 /* PBXContainerItemProxy */ = {
			isa = PBXContainerItemProxy;
			containerPortal = OBJ_1 /* Project object */;
			proxyType = 1;
			remoteGlobalIDString = "Socket::Socket";
			remoteInfo = Socket;
		};
		99A5E5501F7943EB006A38C6 /* PBXContainerItemProxy */ = {
			isa = PBXContainerItemProxy;
			containerPortal = OBJ_1 /* Project object */;
			proxyType = 1;
			remoteGlobalIDString = "Configuration::ConfigurationTestExecutable";
			remoteInfo = ConfigurationTestExecutable;
		};
		99A5E5511F7943EB006A38C6 /* PBXContainerItemProxy */ = {
			isa = PBXContainerItemProxy;
			containerPortal = OBJ_1 /* Project object */;
			proxyType = 1;
			remoteGlobalIDString = "Configuration::Configuration";
			remoteInfo = Configuration;
		};
		99A5E5521F7943EB006A38C6 /* PBXContainerItemProxy */ = {
			isa = PBXContainerItemProxy;
			containerPortal = OBJ_1 /* Project object */;
			proxyType = 1;
			remoteGlobalIDString = "LoggerAPI::LoggerAPI";
			remoteInfo = LoggerAPI;
		};
		99A5E5531F7943EB006A38C6 /* PBXContainerItemProxy */ = {
			isa = PBXContainerItemProxy;
			containerPortal = OBJ_1 /* Project object */;
			proxyType = 1;
			remoteGlobalIDString = "LoggerAPI::LoggerAPI";
			remoteInfo = LoggerAPI;
		};
		99A5E5541F7943EB006A38C6 /* PBXContainerItemProxy */ = {
			isa = PBXContainerItemProxy;
			containerPortal = OBJ_1 /* Project object */;
			proxyType = 1;
			remoteGlobalIDString = "Configuration::Configuration";
			remoteInfo = Configuration;
		};
		99A5E5551F7943EB006A38C6 /* PBXContainerItemProxy */ = {
			isa = PBXContainerItemProxy;
			containerPortal = OBJ_1 /* Project object */;
			proxyType = 1;
			remoteGlobalIDString = "LoggerAPI::LoggerAPI";
			remoteInfo = LoggerAPI;
		};
		99A5E5561F7943EB006A38C6 /* PBXContainerItemProxy */ = {
			isa = PBXContainerItemProxy;
			containerPortal = OBJ_1 /* Project object */;
			proxyType = 1;
			remoteGlobalIDString = "KituraCORS::KituraCORS";
			remoteInfo = KituraCORS;
		};
		99A5E5571F7943EB006A38C6 /* PBXContainerItemProxy */ = {
			isa = PBXContainerItemProxy;
			containerPortal = OBJ_1 /* Project object */;
			proxyType = 1;
			remoteGlobalIDString = "HeliumLogger::HeliumLogger";
			remoteInfo = HeliumLogger;
		};
		99A5E5581F7943EB006A38C6 /* PBXContainerItemProxy */ = {
			isa = PBXContainerItemProxy;
			containerPortal = OBJ_1 /* Project object */;
			proxyType = 1;
			remoteGlobalIDString = "Kitura-CredentialsHTTP::CredentialsHTTP";
			remoteInfo = CredentialsHTTP;
		};
		99A5E5591F7943EB006A38C6 /* PBXContainerItemProxy */ = {
			isa = PBXContainerItemProxy;
			containerPortal = OBJ_1 /* Project object */;
			proxyType = 1;
			remoteGlobalIDString = "Kitura-Credentials::Credentials";
			remoteInfo = Credentials;
		};
		99A5E55A1F7943EB006A38C6 /* PBXContainerItemProxy */ = {
			isa = PBXContainerItemProxy;
			containerPortal = OBJ_1 /* Project object */;
			proxyType = 1;
			remoteGlobalIDString = "Kitura-Session::KituraSession";
			remoteInfo = KituraSession;
		};
		99A5E55B1F7943EB006A38C6 /* PBXContainerItemProxy */ = {
			isa = PBXContainerItemProxy;
			containerPortal = OBJ_1 /* Project object */;
			proxyType = 1;
			remoteGlobalIDString = "Cryptor::Cryptor";
			remoteInfo = Cryptor;
		};
		99A5E55C1F7943EB006A38C6 /* PBXContainerItemProxy */ = {
			isa = PBXContainerItemProxy;
			containerPortal = OBJ_1 /* Project object */;
			proxyType = 1;
			remoteGlobalIDString = "Kitura::Kitura";
			remoteInfo = Kitura;
		};
		99A5E55D1F7943EB006A38C6 /* PBXContainerItemProxy */ = {
			isa = PBXContainerItemProxy;
			containerPortal = OBJ_1 /* Project object */;
			proxyType = 1;
			remoteGlobalIDString = "Kitura-TemplateEngine::KituraTemplateEngine";
			remoteInfo = KituraTemplateEngine;
		};
		99A5E55E1F7943EB006A38C6 /* PBXContainerItemProxy */ = {
			isa = PBXContainerItemProxy;
			containerPortal = OBJ_1 /* Project object */;
			proxyType = 1;
			remoteGlobalIDString = "SwiftyJSON::SwiftyJSON";
			remoteInfo = SwiftyJSON;
		};
		99A5E55F1F7943EB006A38C6 /* PBXContainerItemProxy */ = {
			isa = PBXContainerItemProxy;
			containerPortal = OBJ_1 /* Project object */;
			proxyType = 1;
			remoteGlobalIDString = "Kitura-net::KituraNet";
			remoteInfo = KituraNet;
		};
		99A5E5601F7943EB006A38C6 /* PBXContainerItemProxy */ = {
			isa = PBXContainerItemProxy;
			containerPortal = OBJ_1 /* Project object */;
			proxyType = 1;
			remoteGlobalIDString = "SSLService::SSLService";
			remoteInfo = SSLService;
		};
		99A5E5611F7943EB006A38C6 /* PBXContainerItemProxy */ = {
			isa = PBXContainerItemProxy;
			containerPortal = OBJ_1 /* Project object */;
			proxyType = 1;
			remoteGlobalIDString = "Kitura-net::CHTTPParser";
			remoteInfo = CHTTPParser;
		};
		99A5E5621F7943EB006A38C6 /* PBXContainerItemProxy */ = {
			isa = PBXContainerItemProxy;
			containerPortal = OBJ_1 /* Project object */;
			proxyType = 1;
			remoteGlobalIDString = "SwiftKueryMySQL::SwiftKueryMySQL";
			remoteInfo = SwiftKueryMySQL;
		};
		99A5E5631F7943EB006A38C6 /* PBXContainerItemProxy */ = {
			isa = PBXContainerItemProxy;
			containerPortal = OBJ_1 /* Project object */;
			proxyType = 1;
			remoteGlobalIDString = "SwiftKuery::SwiftKuery";
			remoteInfo = SwiftKuery;
		};
		99A5E5641F7943EB006A38C6 /* PBXContainerItemProxy */ = {
			isa = PBXContainerItemProxy;
			containerPortal = OBJ_1 /* Project object */;
			proxyType = 1;
			remoteGlobalIDString = "CryptoSwift::CryptoSwift";
			remoteInfo = CryptoSwift;
		};
		99A5E5651F7943EB006A38C6 /* PBXContainerItemProxy */ = {
			isa = PBXContainerItemProxy;
			containerPortal = OBJ_1 /* Project object */;
			proxyType = 1;
			remoteGlobalIDString = "Socket::Socket";
			remoteInfo = Socket;
		};
		99A5E5661F7943EB006A38C6 /* PBXContainerItemProxy */ = {
			isa = PBXContainerItemProxy;
			containerPortal = OBJ_1 /* Project object */;
			proxyType = 1;
			remoteGlobalIDString = "Configuration::ConfigurationTestExecutable";
			remoteInfo = ConfigurationTestExecutable;
		};
		99A5E5671F7943EB006A38C6 /* PBXContainerItemProxy */ = {
			isa = PBXContainerItemProxy;
			containerPortal = OBJ_1 /* Project object */;
			proxyType = 1;
			remoteGlobalIDString = "Configuration::Configuration";
			remoteInfo = Configuration;
		};
		99A5E5681F7943EB006A38C6 /* PBXContainerItemProxy */ = {
			isa = PBXContainerItemProxy;
			containerPortal = OBJ_1 /* Project object */;
			proxyType = 1;
			remoteGlobalIDString = "LoggerAPI::LoggerAPI";
			remoteInfo = LoggerAPI;
		};
		99A5E5691F7943EE006A38C6 /* PBXContainerItemProxy */ = {
			isa = PBXContainerItemProxy;
			containerPortal = OBJ_1 /* Project object */;
			proxyType = 1;
			remoteGlobalIDString = "Kitura-CredentialsHTTP::CredentialsHTTP";
			remoteInfo = CredentialsHTTP;
		};
		99A5E56A1F7943EE006A38C6 /* PBXContainerItemProxy */ = {
			isa = PBXContainerItemProxy;
			containerPortal = OBJ_1 /* Project object */;
			proxyType = 1;
			remoteGlobalIDString = "Kitura-Credentials::Credentials";
			remoteInfo = Credentials;
		};
		99A5E56B1F7943EE006A38C6 /* PBXContainerItemProxy */ = {
			isa = PBXContainerItemProxy;
			containerPortal = OBJ_1 /* Project object */;
			proxyType = 1;
			remoteGlobalIDString = "Kitura-Session::KituraSession";
			remoteInfo = KituraSession;
		};
/* End PBXContainerItemProxy section */

/* Begin PBXFileReference section */
		"Configuration::Configuration::Product" /* Configuration.framework */ = {isa = PBXFileReference; explicitFileType = wrapper.framework; path = Configuration.framework; sourceTree = BUILT_PRODUCTS_DIR; };
		"Configuration::ConfigurationTestExecutable::Product" /* ConfigurationTestExecutable */ = {isa = PBXFileReference; lastKnownFileType = text; path = ConfigurationTestExecutable; sourceTree = BUILT_PRODUCTS_DIR; };
		"CryptoSwift::CryptoSwift::Product" /* CryptoSwift.framework */ = {isa = PBXFileReference; explicitFileType = wrapper.framework; path = CryptoSwift.framework; sourceTree = BUILT_PRODUCTS_DIR; };
		"Cryptor::Cryptor::Product" /* Cryptor.framework */ = {isa = PBXFileReference; explicitFileType = wrapper.framework; path = Cryptor.framework; sourceTree = BUILT_PRODUCTS_DIR; };
		"HeliumLogger::HeliumLogger::Product" /* HeliumLogger.framework */ = {isa = PBXFileReference; explicitFileType = wrapper.framework; path = HeliumLogger.framework; sourceTree = BUILT_PRODUCTS_DIR; };
		"Kitura-Credentials::Credentials::Product" /* Credentials.framework */ = {isa = PBXFileReference; explicitFileType = wrapper.framework; path = Credentials.framework; sourceTree = BUILT_PRODUCTS_DIR; };
		"Kitura-CredentialsHTTP::CredentialsHTTP::Product" /* CredentialsHTTP.framework */ = {isa = PBXFileReference; explicitFileType = wrapper.framework; path = CredentialsHTTP.framework; sourceTree = BUILT_PRODUCTS_DIR; };
		"Kitura-Session::KituraSession::Product" /* KituraSession.framework */ = {isa = PBXFileReference; explicitFileType = wrapper.framework; path = KituraSession.framework; sourceTree = BUILT_PRODUCTS_DIR; };
		"Kitura-TemplateEngine::KituraTemplateEngine::Product" /* KituraTemplateEngine.framework */ = {isa = PBXFileReference; explicitFileType = wrapper.framework; path = KituraTemplateEngine.framework; sourceTree = BUILT_PRODUCTS_DIR; };
		"Kitura-net::CHTTPParser::Product" /* CHTTPParser.framework */ = {isa = PBXFileReference; explicitFileType = wrapper.framework; path = CHTTPParser.framework; sourceTree = BUILT_PRODUCTS_DIR; };
		"Kitura-net::KituraNet::Product" /* KituraNet.framework */ = {isa = PBXFileReference; explicitFileType = wrapper.framework; path = KituraNet.framework; sourceTree = BUILT_PRODUCTS_DIR; };
		"Kitura::Kitura::Product" /* Kitura.framework */ = {isa = PBXFileReference; explicitFileType = wrapper.framework; path = Kitura.framework; sourceTree = BUILT_PRODUCTS_DIR; };
		"KituraCORS::KituraCORS::Product" /* KituraCORS.framework */ = {isa = PBXFileReference; explicitFileType = wrapper.framework; path = KituraCORS.framework; sourceTree = BUILT_PRODUCTS_DIR; };
		"LoggerAPI::LoggerAPI::Product" /* LoggerAPI.framework */ = {isa = PBXFileReference; explicitFileType = wrapper.framework; path = LoggerAPI.framework; sourceTree = BUILT_PRODUCTS_DIR; };
		OBJ_10 /* Bitter.swift */ = {isa = PBXFileReference; lastKnownFileType = sourcecode.swift; path = Bitter.swift; sourceTree = "<group>"; };
		OBJ_100 /* RouterRequest.swift */ = {isa = PBXFileReference; lastKnownFileType = sourcecode.swift; path = RouterRequest.swift; sourceTree = "<group>"; };
		OBJ_101 /* RouterResponse.swift */ = {isa = PBXFileReference; lastKnownFileType = sourcecode.swift; path = RouterResponse.swift; sourceTree = "<group>"; };
		OBJ_102 /* SSLConfig.swift */ = {isa = PBXFileReference; lastKnownFileType = sourcecode.swift; path = SSLConfig.swift; sourceTree = "<group>"; };
		OBJ_103 /* Stack.swift */ = {isa = PBXFileReference; lastKnownFileType = sourcecode.swift; path = Stack.swift; sourceTree = "<group>"; };
		OBJ_104 /* String+Extensions.swift */ = {isa = PBXFileReference; lastKnownFileType = sourcecode.swift; path = "String+Extensions.swift"; sourceTree = "<group>"; };
		OBJ_105 /* TemplatingError.swift */ = {isa = PBXFileReference; lastKnownFileType = sourcecode.swift; path = TemplatingError.swift; sourceTree = "<group>"; };
		OBJ_107 /* BodyParser.swift */ = {isa = PBXFileReference; lastKnownFileType = sourcecode.swift; path = BodyParser.swift; sourceTree = "<group>"; };
		OBJ_108 /* BodyParserProtocol.swift */ = {isa = PBXFileReference; lastKnownFileType = sourcecode.swift; path = BodyParserProtocol.swift; sourceTree = "<group>"; };
		OBJ_109 /* JSONBodyParser.swift */ = {isa = PBXFileReference; lastKnownFileType = sourcecode.swift; path = JSONBodyParser.swift; sourceTree = "<group>"; };
		OBJ_11 /* Engine.swift */ = {isa = PBXFileReference; lastKnownFileType = sourcecode.swift; path = Engine.swift; sourceTree = "<group>"; };
		OBJ_110 /* MultiPartBodyParser.swift */ = {isa = PBXFileReference; lastKnownFileType = sourcecode.swift; path = MultiPartBodyParser.swift; sourceTree = "<group>"; };
		OBJ_111 /* ParsedBody.swift */ = {isa = PBXFileReference; lastKnownFileType = sourcecode.swift; path = ParsedBody.swift; sourceTree = "<group>"; };
		OBJ_112 /* Part.swift */ = {isa = PBXFileReference; lastKnownFileType = sourcecode.swift; path = Part.swift; sourceTree = "<group>"; };
		OBJ_113 /* RawBodyParser.swift */ = {isa = PBXFileReference; lastKnownFileType = sourcecode.swift; path = RawBodyParser.swift; sourceTree = "<group>"; };
		OBJ_114 /* TextBodyParser.swift */ = {isa = PBXFileReference; lastKnownFileType = sourcecode.swift; path = TextBodyParser.swift; sourceTree = "<group>"; };
		OBJ_115 /* URLEncodedBodyParser.swift */ = {isa = PBXFileReference; lastKnownFileType = sourcecode.swift; path = URLEncodedBodyParser.swift; sourceTree = "<group>"; };
		OBJ_117 /* ContentType.swift */ = {isa = PBXFileReference; lastKnownFileType = sourcecode.swift; path = ContentType.swift; sourceTree = "<group>"; };
		OBJ_118 /* types.swift */ = {isa = PBXFileReference; lastKnownFileType = sourcecode.swift; path = types.swift; sourceTree = "<group>"; };
		OBJ_12 /* EngineConfig.swift */ = {isa = PBXFileReference; lastKnownFileType = sourcecode.swift; path = EngineConfig.swift; sourceTree = "<group>"; };
		OBJ_120 /* CacheRelatedHeadersSetter.swift */ = {isa = PBXFileReference; lastKnownFileType = sourcecode.swift; path = CacheRelatedHeadersSetter.swift; sourceTree = "<group>"; };
		OBJ_121 /* CompositeHeadersSetter.swift */ = {isa = PBXFileReference; lastKnownFileType = sourcecode.swift; path = CompositeHeadersSetter.swift; sourceTree = "<group>"; };
		OBJ_122 /* FileServer.swift */ = {isa = PBXFileReference; lastKnownFileType = sourcecode.swift; path = FileServer.swift; sourceTree = "<group>"; };
		OBJ_123 /* ResourcePathHandler.swift */ = {isa = PBXFileReference; lastKnownFileType = sourcecode.swift; path = ResourcePathHandler.swift; sourceTree = "<group>"; };
		OBJ_124 /* ResponseHeadersSetter.swift */ = {isa = PBXFileReference; lastKnownFileType = sourcecode.swift; path = ResponseHeadersSetter.swift; sourceTree = "<group>"; };
		OBJ_125 /* StaticFileServer.swift */ = {isa = PBXFileReference; lastKnownFileType = sourcecode.swift; path = StaticFileServer.swift; sourceTree = "<group>"; };
		OBJ_126 /* Package.swift */ = {isa = PBXFileReference; explicitFileType = sourcecode.swift; name = Package.swift; path = "/Volumes/DATA1/mikrotik_router_manager/.build/checkouts/Kitura.git-6522211175291160341/Package.swift"; sourceTree = "<group>"; };
		OBJ_129 /* TemplateEngine.swift */ = {isa = PBXFileReference; lastKnownFileType = sourcecode.swift; path = TemplateEngine.swift; sourceTree = "<group>"; };
		OBJ_13 /* HttpCustomerLogin.swift */ = {isa = PBXFileReference; lastKnownFileType = sourcecode.swift; path = HttpCustomerLogin.swift; sourceTree = "<group>"; };
		OBJ_130 /* Package.swift */ = {isa = PBXFileReference; explicitFileType = sourcecode.swift; name = Package.swift; path = "/Volumes/DATA1/mikrotik_router_manager/.build/checkouts/Kitura-TemplateEngine.git--5059963620657797085/Package.swift"; sourceTree = "<group>"; };
		OBJ_133 /* LclJSONSerialization.swift */ = {isa = PBXFileReference; lastKnownFileType = sourcecode.swift; path = LclJSONSerialization.swift; sourceTree = "<group>"; };
		OBJ_134 /* SwiftyJSON.swift */ = {isa = PBXFileReference; lastKnownFileType = sourcecode.swift; path = SwiftyJSON.swift; sourceTree = "<group>"; };
		OBJ_135 /* Package.swift */ = {isa = PBXFileReference; explicitFileType = sourcecode.swift; name = Package.swift; path = "/Volumes/DATA1/mikrotik_router_manager/.build/checkouts/SwiftyJSON.git--6955445084174387031/Package.swift"; sourceTree = "<group>"; };
		OBJ_138 /* http_parser.c */ = {isa = PBXFileReference; lastKnownFileType = sourcecode.c.c; path = http_parser.c; sourceTree = "<group>"; };
		OBJ_139 /* utils.c */ = {isa = PBXFileReference; lastKnownFileType = sourcecode.c.c; path = utils.c; sourceTree = "<group>"; };
		OBJ_14 /* HttpServerComponent.swift */ = {isa = PBXFileReference; lastKnownFileType = sourcecode.swift; path = HttpServerComponent.swift; sourceTree = "<group>"; };
		OBJ_141 /* CHTTPParser.h */ = {isa = PBXFileReference; lastKnownFileType = sourcecode.c.h; path = CHTTPParser.h; sourceTree = "<group>"; };
		OBJ_142 /* http_parser.h */ = {isa = PBXFileReference; lastKnownFileType = sourcecode.c.h; path = http_parser.h; sourceTree = "<group>"; };
		OBJ_143 /* utils.h */ = {isa = PBXFileReference; lastKnownFileType = sourcecode.c.h; path = utils.h; sourceTree = "<group>"; };
		OBJ_144 /* module.modulemap */ = {isa = PBXFileReference; lastKnownFileType = "sourcecode.module-map"; name = module.modulemap; path = /Volumes/DATA1/mikrotik_router_manager/mikrotik_router_manager.xcodeproj/GeneratedModuleMap/CHTTPParser/module.modulemap; sourceTree = "<group>"; };
		OBJ_146 /* BufferList.swift */ = {isa = PBXFileReference; lastKnownFileType = sourcecode.swift; path = BufferList.swift; sourceTree = "<group>"; };
		OBJ_147 /* ClientRequest.swift */ = {isa = PBXFileReference; lastKnownFileType = sourcecode.swift; path = ClientRequest.swift; sourceTree = "<group>"; };
		OBJ_148 /* ClientResponse.swift */ = {isa = PBXFileReference; lastKnownFileType = sourcecode.swift; path = ClientResponse.swift; sourceTree = "<group>"; };
		OBJ_149 /* ConnectionUpgradeFactory.swift */ = {isa = PBXFileReference; lastKnownFileType = sourcecode.swift; path = ConnectionUpgradeFactory.swift; sourceTree = "<group>"; };
		OBJ_15 /* HttpUserAPI.swift */ = {isa = PBXFileReference; lastKnownFileType = sourcecode.swift; path = HttpUserAPI.swift; sourceTree = "<group>"; };
		OBJ_150 /* ConnectionUpgrader.swift */ = {isa = PBXFileReference; lastKnownFileType = sourcecode.swift; path = ConnectionUpgrader.swift; sourceTree = "<group>"; };
		OBJ_151 /* Error.swift */ = {isa = PBXFileReference; lastKnownFileType = sourcecode.swift; path = Error.swift; sourceTree = "<group>"; };
		OBJ_153 /* FastCGI.swift */ = {isa = PBXFileReference; lastKnownFileType = sourcecode.swift; path = FastCGI.swift; sourceTree = "<group>"; };
		OBJ_154 /* FastCGIRecordCreate.swift */ = {isa = PBXFileReference; lastKnownFileType = sourcecode.swift; path = FastCGIRecordCreate.swift; sourceTree = "<group>"; };
		OBJ_155 /* FastCGIRecordParser.swift */ = {isa = PBXFileReference; lastKnownFileType = sourcecode.swift; path = FastCGIRecordParser.swift; sourceTree = "<group>"; };
		OBJ_156 /* FastCGIServer.swift */ = {isa = PBXFileReference; lastKnownFileType = sourcecode.swift; path = FastCGIServer.swift; sourceTree = "<group>"; };
		OBJ_157 /* FastCGIServerRequest.swift */ = {isa = PBXFileReference; lastKnownFileType = sourcecode.swift; path = FastCGIServerRequest.swift; sourceTree = "<group>"; };
		OBJ_158 /* FastCGIServerResponse.swift */ = {isa = PBXFileReference; lastKnownFileType = sourcecode.swift; path = FastCGIServerResponse.swift; sourceTree = "<group>"; };
		OBJ_16 /* HtttpRouterAPI.swift */ = {isa = PBXFileReference; lastKnownFileType = sourcecode.swift; path = HtttpRouterAPI.swift; sourceTree = "<group>"; };
		OBJ_160 /* HTTP.swift */ = {isa = PBXFileReference; lastKnownFileType = sourcecode.swift; path = HTTP.swift; sourceTree = "<group>"; };
		OBJ_161 /* HTTPServer.swift */ = {isa = PBXFileReference; lastKnownFileType = sourcecode.swift; path = HTTPServer.swift; sourceTree = "<group>"; };
		OBJ_162 /* HTTPServerRequest.swift */ = {isa = PBXFileReference; lastKnownFileType = sourcecode.swift; path = HTTPServerRequest.swift; sourceTree = "<group>"; };
		OBJ_163 /* HTTPServerResponse.swift */ = {isa = PBXFileReference; lastKnownFileType = sourcecode.swift; path = HTTPServerResponse.swift; sourceTree = "<group>"; };
		OBJ_164 /* IncomingHTTPSocketProcessor.swift */ = {isa = PBXFileReference; lastKnownFileType = sourcecode.swift; path = IncomingHTTPSocketProcessor.swift; sourceTree = "<group>"; };
		OBJ_165 /* KeepAliveState.swift */ = {isa = PBXFileReference; lastKnownFileType = sourcecode.swift; path = KeepAliveState.swift; sourceTree = "<group>"; };
		OBJ_167 /* HTTPParser.swift */ = {isa = PBXFileReference; lastKnownFileType = sourcecode.swift; path = HTTPParser.swift; sourceTree = "<group>"; };
		OBJ_168 /* HTTPParserStatus.swift */ = {isa = PBXFileReference; lastKnownFileType = sourcecode.swift; path = HTTPParserStatus.swift; sourceTree = "<group>"; };
		OBJ_169 /* ParseResults.swift */ = {isa = PBXFileReference; lastKnownFileType = sourcecode.swift; path = ParseResults.swift; sourceTree = "<group>"; };
		OBJ_17 /* LogComponent.swift */ = {isa = PBXFileReference; lastKnownFileType = sourcecode.swift; path = LogComponent.swift; sourceTree = "<group>"; };
		OBJ_170 /* URLParser.swift */ = {isa = PBXFileReference; lastKnownFileType = sourcecode.swift; path = URLParser.swift; sourceTree = "<group>"; };
		OBJ_171 /* HeadersContainer.swift */ = {isa = PBXFileReference; lastKnownFileType = sourcecode.swift; path = HeadersContainer.swift; sourceTree = "<group>"; };
		OBJ_172 /* IncomingSocketHandler.swift */ = {isa = PBXFileReference; lastKnownFileType = sourcecode.swift; path = IncomingSocketHandler.swift; sourceTree = "<group>"; };
		OBJ_173 /* IncomingSocketManager.swift */ = {isa = PBXFileReference; lastKnownFileType = sourcecode.swift; path = IncomingSocketManager.swift; sourceTree = "<group>"; };
		OBJ_174 /* IncomingSocketProcessor.swift */ = {isa = PBXFileReference; lastKnownFileType = sourcecode.swift; path = IncomingSocketProcessor.swift; sourceTree = "<group>"; };
		OBJ_175 /* IncomingSocketProcessorCreator.swift */ = {isa = PBXFileReference; lastKnownFileType = sourcecode.swift; path = IncomingSocketProcessorCreator.swift; sourceTree = "<group>"; };
		OBJ_176 /* ListenerGroup.swift */ = {isa = PBXFileReference; lastKnownFileType = sourcecode.swift; path = ListenerGroup.swift; sourceTree = "<group>"; };
		OBJ_177 /* SPIUtils.swift */ = {isa = PBXFileReference; lastKnownFileType = sourcecode.swift; path = SPIUtils.swift; sourceTree = "<group>"; };
		OBJ_179 /* Server.swift */ = {isa = PBXFileReference; lastKnownFileType = sourcecode.swift; path = Server.swift; sourceTree = "<group>"; };
		OBJ_18 /* MikrotikConnection.swift */ = {isa = PBXFileReference; lastKnownFileType = sourcecode.swift; path = MikrotikConnection.swift; sourceTree = "<group>"; };
		OBJ_180 /* ServerDelegate.swift */ = {isa = PBXFileReference; lastKnownFileType = sourcecode.swift; path = ServerDelegate.swift; sourceTree = "<group>"; };
		OBJ_181 /* ServerLifecycleListener.swift */ = {isa = PBXFileReference; lastKnownFileType = sourcecode.swift; path = ServerLifecycleListener.swift; sourceTree = "<group>"; };
		OBJ_182 /* ServerMonitor.swift */ = {isa = PBXFileReference; lastKnownFileType = sourcecode.swift; path = ServerMonitor.swift; sourceTree = "<group>"; };
		OBJ_183 /* ServerState.swift */ = {isa = PBXFileReference; lastKnownFileType = sourcecode.swift; path = ServerState.swift; sourceTree = "<group>"; };
		OBJ_184 /* ServerRequest.swift */ = {isa = PBXFileReference; lastKnownFileType = sourcecode.swift; path = ServerRequest.swift; sourceTree = "<group>"; };
		OBJ_185 /* ServerResponse.swift */ = {isa = PBXFileReference; lastKnownFileType = sourcecode.swift; path = ServerResponse.swift; sourceTree = "<group>"; };
		OBJ_186 /* Package.swift */ = {isa = PBXFileReference; explicitFileType = sourcecode.swift; name = Package.swift; path = "/Volumes/DATA1/mikrotik_router_manager/.build/checkouts/Kitura-net.git--7410958935072501107/Package.swift"; sourceTree = "<group>"; };
		OBJ_189 /* SSLService.swift */ = {isa = PBXFileReference; lastKnownFileType = sourcecode.swift; path = SSLService.swift; sourceTree = "<group>"; };
		OBJ_19 /* MysqlConnection.swift */ = {isa = PBXFileReference; lastKnownFileType = sourcecode.swift; path = MysqlConnection.swift; sourceTree = "<group>"; };
		OBJ_190 /* Package.swift */ = {isa = PBXFileReference; explicitFileType = sourcecode.swift; name = Package.swift; path = "/Volumes/DATA1/mikrotik_router_manager/.build/checkouts/BlueSSLService.git--6577639804771281610/Package.swift"; sourceTree = "<group>"; };
		OBJ_193 /* MySQLConnection.swift */ = {isa = PBXFileReference; lastKnownFileType = sourcecode.swift; path = MySQLConnection.swift; sourceTree = "<group>"; };
		OBJ_194 /* MySQLPreparedStatement.swift */ = {isa = PBXFileReference; lastKnownFileType = sourcecode.swift; path = MySQLPreparedStatement.swift; sourceTree = "<group>"; };
		OBJ_195 /* MySQLResultFetcher.swift */ = {isa = PBXFileReference; lastKnownFileType = sourcecode.swift; path = MySQLResultFetcher.swift; sourceTree = "<group>"; };
		OBJ_196 /* MySQLThreadSafeConnection.swift */ = {isa = PBXFileReference; lastKnownFileType = sourcecode.swift; path = MySQLThreadSafeConnection.swift; sourceTree = "<group>"; };
		OBJ_197 /* Package.swift */ = {isa = PBXFileReference; explicitFileType = sourcecode.swift; name = Package.swift; path = "/Volumes/DATA1/mikrotik_router_manager/.build/checkouts/SwiftKueryMySQL.git-7601298671331203969/Package.swift"; sourceTree = "<group>"; };
		OBJ_20 /* SessionManager.swift */ = {isa = PBXFileReference; lastKnownFileType = sourcecode.swift; path = SessionManager.swift; sourceTree = "<group>"; };
		OBJ_200 /* AggregateColumnExpression.swift */ = {isa = PBXFileReference; lastKnownFileType = sourcecode.swift; path = AggregateColumnExpression.swift; sourceTree = "<group>"; };
		OBJ_201 /* AuxiliaryTable.swift */ = {isa = PBXFileReference; lastKnownFileType = sourcecode.swift; path = AuxiliaryTable.swift; sourceTree = "<group>"; };
		OBJ_202 /* Buildable.swift */ = {isa = PBXFileReference; lastKnownFileType = sourcecode.swift; path = Buildable.swift; sourceTree = "<group>"; };
		OBJ_203 /* Column.swift */ = {isa = PBXFileReference; lastKnownFileType = sourcecode.swift; path = Column.swift; sourceTree = "<group>"; };
		OBJ_204 /* ColumnAndExpressions_Extensions.swift */ = {isa = PBXFileReference; lastKnownFileType = sourcecode.swift; path = ColumnAndExpressions_Extensions.swift; sourceTree = "<group>"; };
		OBJ_205 /* Condition.swift */ = {isa = PBXFileReference; lastKnownFileType = sourcecode.swift; path = Condition.swift; sourceTree = "<group>"; };
		OBJ_206 /* ConditionalClause.swift */ = {isa = PBXFileReference; lastKnownFileType = sourcecode.swift; path = ConditionalClause.swift; sourceTree = "<group>"; };
		OBJ_207 /* Connection.swift */ = {isa = PBXFileReference; lastKnownFileType = sourcecode.swift; path = Connection.swift; sourceTree = "<group>"; };
		OBJ_208 /* ConnectionPool.swift */ = {isa = PBXFileReference; lastKnownFileType = sourcecode.swift; path = ConnectionPool.swift; sourceTree = "<group>"; };
		OBJ_209 /* ConnectionPoolConnection.swift */ = {isa = PBXFileReference; lastKnownFileType = sourcecode.swift; path = ConnectionPoolConnection.swift; sourceTree = "<group>"; };
		OBJ_210 /* ConnectionPoolOptions.swift */ = {isa = PBXFileReference; lastKnownFileType = sourcecode.swift; path = ConnectionPoolOptions.swift; sourceTree = "<group>"; };
		OBJ_211 /* Delete.swift */ = {isa = PBXFileReference; lastKnownFileType = sourcecode.swift; path = Delete.swift; sourceTree = "<group>"; };
		OBJ_212 /* Field.swift */ = {isa = PBXFileReference; lastKnownFileType = sourcecode.swift; path = Field.swift; sourceTree = "<group>"; };
		OBJ_213 /* Filter.swift */ = {isa = PBXFileReference; lastKnownFileType = sourcecode.swift; path = Filter.swift; sourceTree = "<group>"; };
		OBJ_214 /* FilterAndHaving_Extensions.swift */ = {isa = PBXFileReference; lastKnownFileType = sourcecode.swift; path = FilterAndHaving_Extensions.swift; sourceTree = "<group>"; };
		OBJ_215 /* FilterAndHaving_GlobalFunctions.swift */ = {isa = PBXFileReference; lastKnownFileType = sourcecode.swift; path = FilterAndHaving_GlobalFunctions.swift; sourceTree = "<group>"; };
		OBJ_216 /* Having.swift */ = {isa = PBXFileReference; lastKnownFileType = sourcecode.swift; path = Having.swift; sourceTree = "<group>"; };
		OBJ_217 /* Index.swift */ = {isa = PBXFileReference; lastKnownFileType = sourcecode.swift; path = Index.swift; sourceTree = "<group>"; };
		OBJ_218 /* IndexColumn.swift */ = {isa = PBXFileReference; lastKnownFileType = sourcecode.swift; path = IndexColumn.swift; sourceTree = "<group>"; };
		OBJ_219 /* IndexColumnOrdered.swift */ = {isa = PBXFileReference; lastKnownFileType = sourcecode.swift; path = IndexColumnOrdered.swift; sourceTree = "<group>"; };
		OBJ_22 /* main.swift */ = {isa = PBXFileReference; lastKnownFileType = sourcecode.swift; path = main.swift; sourceTree = "<group>"; };
		OBJ_220 /* Insert.swift */ = {isa = PBXFileReference; lastKnownFileType = sourcecode.swift; path = Insert.swift; sourceTree = "<group>"; };
		OBJ_221 /* Join.swift */ = {isa = PBXFileReference; lastKnownFileType = sourcecode.swift; path = Join.swift; sourceTree = "<group>"; };
		OBJ_222 /* Migration.swift */ = {isa = PBXFileReference; lastKnownFileType = sourcecode.swift; path = Migration.swift; sourceTree = "<group>"; };
		OBJ_223 /* OrderBy.swift */ = {isa = PBXFileReference; lastKnownFileType = sourcecode.swift; path = OrderBy.swift; sourceTree = "<group>"; };
		OBJ_224 /* Parameter.swift */ = {isa = PBXFileReference; lastKnownFileType = sourcecode.swift; path = Parameter.swift; sourceTree = "<group>"; };
		OBJ_225 /* Predicate.swift */ = {isa = PBXFileReference; lastKnownFileType = sourcecode.swift; path = Predicate.swift; sourceTree = "<group>"; };
		OBJ_226 /* PreparedStatement.swift */ = {isa = PBXFileReference; lastKnownFileType = sourcecode.swift; path = PreparedStatement.swift; sourceTree = "<group>"; };
		OBJ_227 /* Query.swift */ = {isa = PBXFileReference; lastKnownFileType = sourcecode.swift; path = Query.swift; sourceTree = "<group>"; };
		OBJ_228 /* QueryBuilder.swift */ = {isa = PBXFileReference; lastKnownFileType = sourcecode.swift; path = QueryBuilder.swift; sourceTree = "<group>"; };
		OBJ_229 /* QueryError.swift */ = {isa = PBXFileReference; lastKnownFileType = sourcecode.swift; path = QueryError.swift; sourceTree = "<group>"; };
		OBJ_230 /* QueryResult.swift */ = {isa = PBXFileReference; lastKnownFileType = sourcecode.swift; path = QueryResult.swift; sourceTree = "<group>"; };
		OBJ_231 /* QuerySuffixProtocol.swift */ = {isa = PBXFileReference; lastKnownFileType = sourcecode.swift; path = QuerySuffixProtocol.swift; sourceTree = "<group>"; };
		OBJ_232 /* Raw.swift */ = {isa = PBXFileReference; lastKnownFileType = sourcecode.swift; path = Raw.swift; sourceTree = "<group>"; };
		OBJ_233 /* RawField.swift */ = {isa = PBXFileReference; lastKnownFileType = sourcecode.swift; path = RawField.swift; sourceTree = "<group>"; };
		OBJ_234 /* ResultFetcher.swift */ = {isa = PBXFileReference; lastKnownFileType = sourcecode.swift; path = ResultFetcher.swift; sourceTree = "<group>"; };
		OBJ_235 /* ResultSet.swift */ = {isa = PBXFileReference; lastKnownFileType = sourcecode.swift; path = ResultSet.swift; sourceTree = "<group>"; };
		OBJ_236 /* RowSequence.swift */ = {isa = PBXFileReference; lastKnownFileType = sourcecode.swift; path = RowSequence.swift; sourceTree = "<group>"; };
		OBJ_237 /* SQLDataType.swift */ = {isa = PBXFileReference; lastKnownFileType = sourcecode.swift; path = SQLDataType.swift; sourceTree = "<group>"; };
		OBJ_238 /* ScalarColumnExpression.swift */ = {isa = PBXFileReference; lastKnownFileType = sourcecode.swift; path = ScalarColumnExpression.swift; sourceTree = "<group>"; };
		OBJ_239 /* Select.swift */ = {isa = PBXFileReference; lastKnownFileType = sourcecode.swift; path = Select.swift; sourceTree = "<group>"; };
		OBJ_24 /* Database */ = {isa = PBXFileReference; lastKnownFileType = folder; path = Database; sourceTree = SOURCE_ROOT; };
		OBJ_240 /* SpecialOperators_Extensions.swift */ = {isa = PBXFileReference; lastKnownFileType = sourcecode.swift; path = SpecialOperators_Extensions.swift; sourceTree = "<group>"; };
		OBJ_241 /* String+Buildable.swift */ = {isa = PBXFileReference; lastKnownFileType = sourcecode.swift; path = "String+Buildable.swift"; sourceTree = "<group>"; };
		OBJ_242 /* Subqueries_GlobalFunctionsAndExtensions.swift */ = {isa = PBXFileReference; lastKnownFileType = sourcecode.swift; path = Subqueries_GlobalFunctionsAndExtensions.swift; sourceTree = "<group>"; };
		OBJ_243 /* Table.swift */ = {isa = PBXFileReference; lastKnownFileType = sourcecode.swift; path = Table.swift; sourceTree = "<group>"; };
		OBJ_244 /* Union.swift */ = {isa = PBXFileReference; lastKnownFileType = sourcecode.swift; path = Union.swift; sourceTree = "<group>"; };
		OBJ_245 /* Update.swift */ = {isa = PBXFileReference; lastKnownFileType = sourcecode.swift; path = Update.swift; sourceTree = "<group>"; };
		OBJ_246 /* Utils.swift */ = {isa = PBXFileReference; lastKnownFileType = sourcecode.swift; path = Utils.swift; sourceTree = "<group>"; };
		OBJ_247 /* With.swift */ = {isa = PBXFileReference; lastKnownFileType = sourcecode.swift; path = With.swift; sourceTree = "<group>"; };
		OBJ_248 /* Package.swift */ = {isa = PBXFileReference; explicitFileType = sourcecode.swift; name = Package.swift; path = "/Volumes/DATA1/mikrotik_router_manager/.build/checkouts/Swift-Kuery.git-1645988340584907058/Package.swift"; sourceTree = "<group>"; };
		OBJ_251 /* AES.swift */ = {isa = PBXFileReference; lastKnownFileType = sourcecode.swift; path = AES.swift; sourceTree = "<group>"; };
		OBJ_252 /* Array+Extension.swift */ = {isa = PBXFileReference; lastKnownFileType = sourcecode.swift; path = "Array+Extension.swift"; sourceTree = "<group>"; };
		OBJ_253 /* Authenticator.swift */ = {isa = PBXFileReference; lastKnownFileType = sourcecode.swift; path = Authenticator.swift; sourceTree = "<group>"; };
		OBJ_254 /* BatchedCollection.swift */ = {isa = PBXFileReference; lastKnownFileType = sourcecode.swift; path = BatchedCollection.swift; sourceTree = "<group>"; };
		OBJ_255 /* Bit.swift */ = {isa = PBXFileReference; lastKnownFileType = sourcecode.swift; path = Bit.swift; sourceTree = "<group>"; };
		OBJ_256 /* BlockCipher.swift */ = {isa = PBXFileReference; lastKnownFileType = sourcecode.swift; path = BlockCipher.swift; sourceTree = "<group>"; };
		OBJ_258 /* BlockMode.swift */ = {isa = PBXFileReference; lastKnownFileType = sourcecode.swift; path = BlockMode.swift; sourceTree = "<group>"; };
		OBJ_259 /* BlockModeOptions.swift */ = {isa = PBXFileReference; lastKnownFileType = sourcecode.swift; path = BlockModeOptions.swift; sourceTree = "<group>"; };
		OBJ_260 /* BlockModeWorker.swift */ = {isa = PBXFileReference; lastKnownFileType = sourcecode.swift; path = BlockModeWorker.swift; sourceTree = "<group>"; };
		OBJ_261 /* CBC.swift */ = {isa = PBXFileReference; lastKnownFileType = sourcecode.swift; path = CBC.swift; sourceTree = "<group>"; };
		OBJ_262 /* CFB.swift */ = {isa = PBXFileReference; lastKnownFileType = sourcecode.swift; path = CFB.swift; sourceTree = "<group>"; };
		OBJ_263 /* CTR.swift */ = {isa = PBXFileReference; lastKnownFileType = sourcecode.swift; path = CTR.swift; sourceTree = "<group>"; };
		OBJ_264 /* ECB.swift */ = {isa = PBXFileReference; lastKnownFileType = sourcecode.swift; path = ECB.swift; sourceTree = "<group>"; };
		OBJ_265 /* OFB.swift */ = {isa = PBXFileReference; lastKnownFileType = sourcecode.swift; path = OFB.swift; sourceTree = "<group>"; };
		OBJ_266 /* PCBC.swift */ = {isa = PBXFileReference; lastKnownFileType = sourcecode.swift; path = PCBC.swift; sourceTree = "<group>"; };
		OBJ_267 /* RandomAccessBlockModeWorker.swift */ = {isa = PBXFileReference; lastKnownFileType = sourcecode.swift; path = RandomAccessBlockModeWorker.swift; sourceTree = "<group>"; };
		OBJ_268 /* Blowfish.swift */ = {isa = PBXFileReference; lastKnownFileType = sourcecode.swift; path = Blowfish.swift; sourceTree = "<group>"; };
		OBJ_269 /* CSArrayType+Extensions.swift */ = {isa = PBXFileReference; lastKnownFileType = sourcecode.swift; path = "CSArrayType+Extensions.swift"; sourceTree = "<group>"; };
		OBJ_270 /* ChaCha20.swift */ = {isa = PBXFileReference; lastKnownFileType = sourcecode.swift; path = ChaCha20.swift; sourceTree = "<group>"; };
		OBJ_271 /* Checksum.swift */ = {isa = PBXFileReference; lastKnownFileType = sourcecode.swift; path = Checksum.swift; sourceTree = "<group>"; };
		OBJ_272 /* Cipher.swift */ = {isa = PBXFileReference; lastKnownFileType = sourcecode.swift; path = Cipher.swift; sourceTree = "<group>"; };
		OBJ_273 /* Collection+Extension.swift */ = {isa = PBXFileReference; lastKnownFileType = sourcecode.swift; path = "Collection+Extension.swift"; sourceTree = "<group>"; };
		OBJ_274 /* Cryptors.swift */ = {isa = PBXFileReference; lastKnownFileType = sourcecode.swift; path = Cryptors.swift; sourceTree = "<group>"; };
		OBJ_275 /* Digest.swift */ = {isa = PBXFileReference; lastKnownFileType = sourcecode.swift; path = Digest.swift; sourceTree = "<group>"; };
		OBJ_276 /* DigestType.swift */ = {isa = PBXFileReference; lastKnownFileType = sourcecode.swift; path = DigestType.swift; sourceTree = "<group>"; };
		OBJ_278 /* AES+Foundation.swift */ = {isa = PBXFileReference; lastKnownFileType = sourcecode.swift; path = "AES+Foundation.swift"; sourceTree = "<group>"; };
		OBJ_279 /* Blowfish+Foundation.swift */ = {isa = PBXFileReference; lastKnownFileType = sourcecode.swift; path = "Blowfish+Foundation.swift"; sourceTree = "<group>"; };
		OBJ_28 /* AllowedOrigins.swift */ = {isa = PBXFileReference; lastKnownFileType = sourcecode.swift; path = AllowedOrigins.swift; sourceTree = "<group>"; };
		OBJ_280 /* CSArrayType+Foundation.swift */ = {isa = PBXFileReference; lastKnownFileType = sourcecode.swift; path = "CSArrayType+Foundation.swift"; sourceTree = "<group>"; };
		OBJ_281 /* ChaCha20+Foundation.swift */ = {isa = PBXFileReference; lastKnownFileType = sourcecode.swift; path = "ChaCha20+Foundation.swift"; sourceTree = "<group>"; };
		OBJ_282 /* Data+Extension.swift */ = {isa = PBXFileReference; lastKnownFileType = sourcecode.swift; path = "Data+Extension.swift"; sourceTree = "<group>"; };
		OBJ_283 /* HMAC+Foundation.swift */ = {isa = PBXFileReference; lastKnownFileType = sourcecode.swift; path = "HMAC+Foundation.swift"; sourceTree = "<group>"; };
		OBJ_284 /* Rabbit+Foundation.swift */ = {isa = PBXFileReference; lastKnownFileType = sourcecode.swift; path = "Rabbit+Foundation.swift"; sourceTree = "<group>"; };
		OBJ_285 /* String+FoundationExtension.swift */ = {isa = PBXFileReference; lastKnownFileType = sourcecode.swift; path = "String+FoundationExtension.swift"; sourceTree = "<group>"; };
		OBJ_286 /* Utils+Foundation.swift */ = {isa = PBXFileReference; lastKnownFileType = sourcecode.swift; path = "Utils+Foundation.swift"; sourceTree = "<group>"; };
		OBJ_287 /* Generics.swift */ = {isa = PBXFileReference; lastKnownFileType = sourcecode.swift; path = Generics.swift; sourceTree = "<group>"; };
		OBJ_288 /* HMAC.swift */ = {isa = PBXFileReference; lastKnownFileType = sourcecode.swift; path = HMAC.swift; sourceTree = "<group>"; };
		OBJ_289 /* Int+Extension.swift */ = {isa = PBXFileReference; lastKnownFileType = sourcecode.swift; path = "Int+Extension.swift"; sourceTree = "<group>"; };
		OBJ_29 /* CORS.swift */ = {isa = PBXFileReference; lastKnownFileType = sourcecode.swift; path = CORS.swift; sourceTree = "<group>"; };
		OBJ_290 /* MD5.swift */ = {isa = PBXFileReference; lastKnownFileType = sourcecode.swift; path = MD5.swift; sourceTree = "<group>"; };
		OBJ_291 /* NoPadding.swift */ = {isa = PBXFileReference; lastKnownFileType = sourcecode.swift; path = NoPadding.swift; sourceTree = "<group>"; };
		OBJ_292 /* Operators.swift */ = {isa = PBXFileReference; lastKnownFileType = sourcecode.swift; path = Operators.swift; sourceTree = "<group>"; };
		OBJ_294 /* PBKDF1.swift */ = {isa = PBXFileReference; lastKnownFileType = sourcecode.swift; path = PBKDF1.swift; sourceTree = "<group>"; };
		OBJ_295 /* PBKDF2.swift */ = {isa = PBXFileReference; lastKnownFileType = sourcecode.swift; path = PBKDF2.swift; sourceTree = "<group>"; };
		OBJ_296 /* PKCS5.swift */ = {isa = PBXFileReference; lastKnownFileType = sourcecode.swift; path = PKCS5.swift; sourceTree = "<group>"; };
		OBJ_297 /* PKCS7.swift */ = {isa = PBXFileReference; lastKnownFileType = sourcecode.swift; path = PKCS7.swift; sourceTree = "<group>"; };
		OBJ_298 /* PKCS7Padding.swift */ = {isa = PBXFileReference; lastKnownFileType = sourcecode.swift; path = PKCS7Padding.swift; sourceTree = "<group>"; };
		OBJ_299 /* Padding.swift */ = {isa = PBXFileReference; lastKnownFileType = sourcecode.swift; path = Padding.swift; sourceTree = "<group>"; };
		OBJ_30 /* Options.swift */ = {isa = PBXFileReference; lastKnownFileType = sourcecode.swift; path = Options.swift; sourceTree = "<group>"; };
		OBJ_300 /* Poly1305.swift */ = {isa = PBXFileReference; lastKnownFileType = sourcecode.swift; path = Poly1305.swift; sourceTree = "<group>"; };
		OBJ_301 /* Rabbit.swift */ = {isa = PBXFileReference; lastKnownFileType = sourcecode.swift; path = Rabbit.swift; sourceTree = "<group>"; };
		OBJ_302 /* RandomAccessCryptor.swift */ = {isa = PBXFileReference; lastKnownFileType = sourcecode.swift; path = RandomAccessCryptor.swift; sourceTree = "<group>"; };
		OBJ_303 /* RandomBytesSequence.swift */ = {isa = PBXFileReference; lastKnownFileType = sourcecode.swift; path = RandomBytesSequence.swift; sourceTree = "<group>"; };
		OBJ_304 /* SHA1.swift */ = {isa = PBXFileReference; lastKnownFileType = sourcecode.swift; path = SHA1.swift; sourceTree = "<group>"; };
		OBJ_305 /* SHA2.swift */ = {isa = PBXFileReference; lastKnownFileType = sourcecode.swift; path = SHA2.swift; sourceTree = "<group>"; };
		OBJ_306 /* SHA3.swift */ = {isa = PBXFileReference; lastKnownFileType = sourcecode.swift; path = SHA3.swift; sourceTree = "<group>"; };
		OBJ_307 /* SecureBytes.swift */ = {isa = PBXFileReference; lastKnownFileType = sourcecode.swift; path = SecureBytes.swift; sourceTree = "<group>"; };
		OBJ_308 /* String+Extension.swift */ = {isa = PBXFileReference; lastKnownFileType = sourcecode.swift; path = "String+Extension.swift"; sourceTree = "<group>"; };
		OBJ_309 /* UInt16+Extension.swift */ = {isa = PBXFileReference; lastKnownFileType = sourcecode.swift; path = "UInt16+Extension.swift"; sourceTree = "<group>"; };
		OBJ_31 /* Package.swift */ = {isa = PBXFileReference; explicitFileType = sourcecode.swift; name = Package.swift; path = "/Volumes/DATA1/mikrotik_router_manager/.build/checkouts/Kitura-CORS.git-6045985022829947324/Package.swift"; sourceTree = "<group>"; };
		OBJ_310 /* UInt32+Extension.swift */ = {isa = PBXFileReference; lastKnownFileType = sourcecode.swift; path = "UInt32+Extension.swift"; sourceTree = "<group>"; };
		OBJ_311 /* UInt64+Extension.swift */ = {isa = PBXFileReference; lastKnownFileType = sourcecode.swift; path = "UInt64+Extension.swift"; sourceTree = "<group>"; };
		OBJ_312 /* UInt8+Extension.swift */ = {isa = PBXFileReference; lastKnownFileType = sourcecode.swift; path = "UInt8+Extension.swift"; sourceTree = "<group>"; };
		OBJ_313 /* Updatable.swift */ = {isa = PBXFileReference; lastKnownFileType = sourcecode.swift; path = Updatable.swift; sourceTree = "<group>"; };
		OBJ_314 /* Utils.swift */ = {isa = PBXFileReference; lastKnownFileType = sourcecode.swift; path = Utils.swift; sourceTree = "<group>"; };
		OBJ_315 /* ZeroPadding.swift */ = {isa = PBXFileReference; lastKnownFileType = sourcecode.swift; path = ZeroPadding.swift; sourceTree = "<group>"; };
		OBJ_316 /* Package.swift */ = {isa = PBXFileReference; explicitFileType = sourcecode.swift; name = Package.swift; path = "/Volumes/DATA1/mikrotik_router_manager/.build/checkouts/CryptoSwift.git--6440749087414195235/Package.swift"; sourceTree = "<group>"; };
		OBJ_318 /* Package.swift */ = {isa = PBXFileReference; explicitFileType = sourcecode.swift; name = Package.swift; path = "/Volumes/DATA1/mikrotik_router_manager/.build/checkouts/BlueSocket.git-3162807777605905816/Package.swift"; sourceTree = "<group>"; };
		OBJ_319 /* Socket.swift */ = {isa = PBXFileReference; lastKnownFileType = sourcecode.swift; path = Socket.swift; sourceTree = "<group>"; };
		OBJ_320 /* SocketProtocols.swift */ = {isa = PBXFileReference; lastKnownFileType = sourcecode.swift; path = SocketProtocols.swift; sourceTree = "<group>"; };
		OBJ_321 /* SocketUtils.swift */ = {isa = PBXFileReference; lastKnownFileType = sourcecode.swift; path = SocketUtils.swift; sourceTree = "<group>"; };
		OBJ_324 /* ConfigurationManager.swift */ = {isa = PBXFileReference; lastKnownFileType = sourcecode.swift; path = ConfigurationManager.swift; sourceTree = "<group>"; };
		OBJ_325 /* ConfigurationNode.swift */ = {isa = PBXFileReference; lastKnownFileType = sourcecode.swift; path = ConfigurationNode.swift; sourceTree = "<group>"; };
		OBJ_326 /* Deserializer.swift */ = {isa = PBXFileReference; lastKnownFileType = sourcecode.swift; path = Deserializer.swift; sourceTree = "<group>"; };
		OBJ_328 /* JSONDeserializer.swift */ = {isa = PBXFileReference; lastKnownFileType = sourcecode.swift; path = JSONDeserializer.swift; sourceTree = "<group>"; };
		OBJ_329 /* PLISTDeserializer.swift */ = {isa = PBXFileReference; lastKnownFileType = sourcecode.swift; path = PLISTDeserializer.swift; sourceTree = "<group>"; };
		OBJ_330 /* PathUtilities.swift */ = {isa = PBXFileReference; lastKnownFileType = sourcecode.swift; path = PathUtilities.swift; sourceTree = "<group>"; };
		OBJ_332 /* main.swift */ = {isa = PBXFileReference; lastKnownFileType = sourcecode.swift; path = main.swift; sourceTree = "<group>"; };
		OBJ_333 /* Package.swift */ = {isa = PBXFileReference; explicitFileType = sourcecode.swift; name = Package.swift; path = "/Volumes/DATA1/mikrotik_router_manager/.build/checkouts/Configuration.git--2683441109504822782/Package.swift"; sourceTree = "<group>"; };
		OBJ_336 /* Logger.swift */ = {isa = PBXFileReference; lastKnownFileType = sourcecode.swift; path = Logger.swift; sourceTree = "<group>"; };
		OBJ_337 /* Package.swift */ = {isa = PBXFileReference; explicitFileType = sourcecode.swift; name = Package.swift; path = "/Volumes/DATA1/mikrotik_router_manager/.build/checkouts/LoggerAPI.git--6449715459278086880/Package.swift"; sourceTree = "<group>"; };
		OBJ_34 /* HeliumLogger.swift */ = {isa = PBXFileReference; lastKnownFileType = sourcecode.swift; path = HeliumLogger.swift; sourceTree = "<group>"; };
		OBJ_35 /* HeliumStreamLogger.swift */ = {isa = PBXFileReference; lastKnownFileType = sourcecode.swift; path = HeliumStreamLogger.swift; sourceTree = "<group>"; };
		OBJ_36 /* Package.swift */ = {isa = PBXFileReference; explicitFileType = sourcecode.swift; name = Package.swift; path = "/Volumes/DATA1/mikrotik_router_manager/.build/checkouts/HeliumLogger.git-2106793442615829935/Package.swift"; sourceTree = "<group>"; };
		OBJ_39 /* CredentialsHTTPBasic.swift */ = {isa = PBXFileReference; lastKnownFileType = sourcecode.swift; path = CredentialsHTTPBasic.swift; sourceTree = "<group>"; };
		OBJ_40 /* CredentialsHTTPDigest.swift */ = {isa = PBXFileReference; lastKnownFileType = sourcecode.swift; path = CredentialsHTTPDigest.swift; sourceTree = "<group>"; };
		OBJ_41 /* UserProfileLoader.swift */ = {isa = PBXFileReference; lastKnownFileType = sourcecode.swift; path = UserProfileLoader.swift; sourceTree = "<group>"; };
		OBJ_42 /* VerifyPassword.swift */ = {isa = PBXFileReference; lastKnownFileType = sourcecode.swift; path = VerifyPassword.swift; sourceTree = "<group>"; };
		OBJ_43 /* Package.swift */ = {isa = PBXFileReference; explicitFileType = sourcecode.swift; name = Package.swift; path = "/Volumes/DATA1/mikrotik_router_manager/.build/checkouts/Kitura-CredentialsHTTP.git--2255905302832386242/Package.swift"; sourceTree = "<group>"; };
		OBJ_46 /* BaseCacheElement.swift */ = {isa = PBXFileReference; lastKnownFileType = sourcecode.swift; path = BaseCacheElement.swift; sourceTree = "<group>"; };
		OBJ_47 /* Credentials.swift */ = {isa = PBXFileReference; lastKnownFileType = sourcecode.swift; path = Credentials.swift; sourceTree = "<group>"; };
		OBJ_48 /* CredentialsPluginProtocol.swift */ = {isa = PBXFileReference; lastKnownFileType = sourcecode.swift; path = CredentialsPluginProtocol.swift; sourceTree = "<group>"; };
		OBJ_49 /* RouterRequest+UserProfile.swift */ = {isa = PBXFileReference; lastKnownFileType = sourcecode.swift; path = "RouterRequest+UserProfile.swift"; sourceTree = "<group>"; };
		OBJ_50 /* UserProfile.swift */ = {isa = PBXFileReference; lastKnownFileType = sourcecode.swift; path = UserProfile.swift; sourceTree = "<group>"; };
		OBJ_51 /* UserProfileDelegate.swift */ = {isa = PBXFileReference; lastKnownFileType = sourcecode.swift; path = UserProfileDelegate.swift; sourceTree = "<group>"; };
		OBJ_52 /* Package.swift */ = {isa = PBXFileReference; explicitFileType = sourcecode.swift; name = Package.swift; path = "/Volumes/DATA1/mikrotik_router_manager/.build/checkouts/Kitura-Credentials.git-1137106172743287290/Package.swift"; sourceTree = "<group>"; };
		OBJ_55 /* CookieCryptography.swift */ = {isa = PBXFileReference; lastKnownFileType = sourcecode.swift; path = CookieCryptography.swift; sourceTree = "<group>"; };
		OBJ_56 /* CookieManagement.swift */ = {isa = PBXFileReference; lastKnownFileType = sourcecode.swift; path = CookieManagement.swift; sourceTree = "<group>"; };
		OBJ_57 /* CookieParameter.swift */ = {isa = PBXFileReference; lastKnownFileType = sourcecode.swift; path = CookieParameter.swift; sourceTree = "<group>"; };
		OBJ_58 /* InMemoryStore.swift */ = {isa = PBXFileReference; lastKnownFileType = sourcecode.swift; path = InMemoryStore.swift; sourceTree = "<group>"; };
		OBJ_59 /* RouterRequest+Session.swift */ = {isa = PBXFileReference; lastKnownFileType = sourcecode.swift; path = "RouterRequest+Session.swift"; sourceTree = "<group>"; };
		OBJ_6 /* Package.swift */ = {isa = PBXFileReference; explicitFileType = sourcecode.swift; path = Package.swift; sourceTree = "<group>"; };
		OBJ_60 /* Session.swift */ = {isa = PBXFileReference; lastKnownFileType = sourcecode.swift; path = Session.swift; sourceTree = "<group>"; };
		OBJ_61 /* SessionState.swift */ = {isa = PBXFileReference; lastKnownFileType = sourcecode.swift; path = SessionState.swift; sourceTree = "<group>"; };
		OBJ_62 /* Store.swift */ = {isa = PBXFileReference; lastKnownFileType = sourcecode.swift; path = Store.swift; sourceTree = "<group>"; };
		OBJ_63 /* Package.swift */ = {isa = PBXFileReference; explicitFileType = sourcecode.swift; name = Package.swift; path = "/Volumes/DATA1/mikrotik_router_manager/.build/checkouts/Kitura-Session.git-4044573149666132076/Package.swift"; sourceTree = "<group>"; };
		OBJ_66 /* Crypto.swift */ = {isa = PBXFileReference; lastKnownFileType = sourcecode.swift; path = Crypto.swift; sourceTree = "<group>"; };
		OBJ_67 /* Cryptor.swift */ = {isa = PBXFileReference; lastKnownFileType = sourcecode.swift; path = Cryptor.swift; sourceTree = "<group>"; };
		OBJ_68 /* Digest.swift */ = {isa = PBXFileReference; lastKnownFileType = sourcecode.swift; path = Digest.swift; sourceTree = "<group>"; };
		OBJ_69 /* HMAC.swift */ = {isa = PBXFileReference; lastKnownFileType = sourcecode.swift; path = HMAC.swift; sourceTree = "<group>"; };
		OBJ_70 /* KeyDerivation.swift */ = {isa = PBXFileReference; lastKnownFileType = sourcecode.swift; path = KeyDerivation.swift; sourceTree = "<group>"; };
		OBJ_71 /* Random.swift */ = {isa = PBXFileReference; lastKnownFileType = sourcecode.swift; path = Random.swift; sourceTree = "<group>"; };
		OBJ_72 /* Status.swift */ = {isa = PBXFileReference; lastKnownFileType = sourcecode.swift; path = Status.swift; sourceTree = "<group>"; };
		OBJ_73 /* StreamCryptor.swift */ = {isa = PBXFileReference; lastKnownFileType = sourcecode.swift; path = StreamCryptor.swift; sourceTree = "<group>"; };
		OBJ_74 /* Updatable.swift */ = {isa = PBXFileReference; lastKnownFileType = sourcecode.swift; path = Updatable.swift; sourceTree = "<group>"; };
		OBJ_75 /* Utilities.swift */ = {isa = PBXFileReference; lastKnownFileType = sourcecode.swift; path = Utilities.swift; sourceTree = "<group>"; };
		OBJ_76 /* Package.swift */ = {isa = PBXFileReference; explicitFileType = sourcecode.swift; name = Package.swift; path = "/Volumes/DATA1/mikrotik_router_manager/.build/checkouts/BlueCryptor.git-2709167748876642405/Package.swift"; sourceTree = "<group>"; };
		OBJ_79 /* Error.swift */ = {isa = PBXFileReference; lastKnownFileType = sourcecode.swift; path = Error.swift; sourceTree = "<group>"; };
		OBJ_80 /* FileResourceServer.swift */ = {isa = PBXFileReference; lastKnownFileType = sourcecode.swift; path = FileResourceServer.swift; sourceTree = "<group>"; };
		OBJ_81 /* HTTPVersion.swift */ = {isa = PBXFileReference; lastKnownFileType = sourcecode.swift; path = HTTPVersion.swift; sourceTree = "<group>"; };
		OBJ_82 /* Headers.swift */ = {isa = PBXFileReference; lastKnownFileType = sourcecode.swift; path = Headers.swift; sourceTree = "<group>"; };
		OBJ_83 /* InternalError.swift */ = {isa = PBXFileReference; lastKnownFileType = sourcecode.swift; path = InternalError.swift; sourceTree = "<group>"; };
		OBJ_84 /* JSONPError.swift */ = {isa = PBXFileReference; lastKnownFileType = sourcecode.swift; path = JSONPError.swift; sourceTree = "<group>"; };
		OBJ_85 /* Kitura.swift */ = {isa = PBXFileReference; lastKnownFileType = sourcecode.swift; path = Kitura.swift; sourceTree = "<group>"; };
		OBJ_86 /* LinkParameter.swift */ = {isa = PBXFileReference; lastKnownFileType = sourcecode.swift; path = LinkParameter.swift; sourceTree = "<group>"; };
		OBJ_87 /* MimeTypeAcceptor.swift */ = {isa = PBXFileReference; lastKnownFileType = sourcecode.swift; path = MimeTypeAcceptor.swift; sourceTree = "<group>"; };
		OBJ_88 /* RouteRegex.swift */ = {isa = PBXFileReference; lastKnownFileType = sourcecode.swift; path = RouteRegex.swift; sourceTree = "<group>"; };
		OBJ_89 /* Router.swift */ = {isa = PBXFileReference; lastKnownFileType = sourcecode.swift; path = Router.swift; sourceTree = "<group>"; };
		OBJ_9 /* BaseComponent.swift */ = {isa = PBXFileReference; lastKnownFileType = sourcecode.swift; path = BaseComponent.swift; sourceTree = "<group>"; };
		OBJ_90 /* RouterElement.swift */ = {isa = PBXFileReference; lastKnownFileType = sourcecode.swift; path = RouterElement.swift; sourceTree = "<group>"; };
		OBJ_91 /* RouterElementWalker.swift */ = {isa = PBXFileReference; lastKnownFileType = sourcecode.swift; path = RouterElementWalker.swift; sourceTree = "<group>"; };
		OBJ_92 /* RouterHTTPVerbs+Error.swift */ = {isa = PBXFileReference; lastKnownFileType = sourcecode.swift; path = "RouterHTTPVerbs+Error.swift"; sourceTree = "<group>"; };
		OBJ_93 /* RouterHTTPVerbs_generated.swift */ = {isa = PBXFileReference; lastKnownFileType = sourcecode.swift; path = RouterHTTPVerbs_generated.swift; sourceTree = "<group>"; };
		OBJ_94 /* RouterHandler.swift */ = {isa = PBXFileReference; lastKnownFileType = sourcecode.swift; path = RouterHandler.swift; sourceTree = "<group>"; };
		OBJ_95 /* RouterMethod.swift */ = {isa = PBXFileReference; lastKnownFileType = sourcecode.swift; path = RouterMethod.swift; sourceTree = "<group>"; };
		OBJ_96 /* RouterMiddleware.swift */ = {isa = PBXFileReference; lastKnownFileType = sourcecode.swift; path = RouterMiddleware.swift; sourceTree = "<group>"; };
		OBJ_97 /* RouterMiddlewareGenerator.swift */ = {isa = PBXFileReference; lastKnownFileType = sourcecode.swift; path = RouterMiddlewareGenerator.swift; sourceTree = "<group>"; };
		OBJ_98 /* RouterMiddlewareWalker.swift */ = {isa = PBXFileReference; lastKnownFileType = sourcecode.swift; path = RouterMiddlewareWalker.swift; sourceTree = "<group>"; };
		OBJ_99 /* RouterParameterWalker.swift */ = {isa = PBXFileReference; lastKnownFileType = sourcecode.swift; path = RouterParameterWalker.swift; sourceTree = "<group>"; };
		"SSLService::SSLService::Product" /* SSLService.framework */ = {isa = PBXFileReference; explicitFileType = wrapper.framework; path = SSLService.framework; sourceTree = BUILT_PRODUCTS_DIR; };
		"Socket::Socket::Product" /* Socket.framework */ = {isa = PBXFileReference; explicitFileType = wrapper.framework; path = Socket.framework; sourceTree = BUILT_PRODUCTS_DIR; };
		"SwiftKuery::SwiftKuery::Product" /* SwiftKuery.framework */ = {isa = PBXFileReference; explicitFileType = wrapper.framework; path = SwiftKuery.framework; sourceTree = BUILT_PRODUCTS_DIR; };
		"SwiftKueryMySQL::SwiftKueryMySQL::Product" /* SwiftKueryMySQL.framework */ = {isa = PBXFileReference; explicitFileType = wrapper.framework; path = SwiftKueryMySQL.framework; sourceTree = BUILT_PRODUCTS_DIR; };
		"SwiftyJSON::SwiftyJSON::Product" /* SwiftyJSON.framework */ = {isa = PBXFileReference; explicitFileType = wrapper.framework; path = SwiftyJSON.framework; sourceTree = BUILT_PRODUCTS_DIR; };
		"mikrotik_router_manager::CORE::Product" /* CORE.framework */ = {isa = PBXFileReference; explicitFileType = wrapper.framework; path = CORE.framework; sourceTree = BUILT_PRODUCTS_DIR; };
		"mikrotik_router_manager::SERVER::Product" /* SERVER */ = {isa = PBXFileReference; lastKnownFileType = text; path = SERVER; sourceTree = BUILT_PRODUCTS_DIR; };
/* End PBXFileReference section */

/* Begin PBXFrameworksBuildPhase section */
		OBJ_1007 /* Frameworks */ = {
			isa = PBXFrameworksBuildPhase;
			buildActionMask = 0;
			files = (
			);
			runOnlyForDeploymentPostprocessing = 0;
		};
		OBJ_1013 /* Frameworks */ = {
			isa = PBXFrameworksBuildPhase;
			buildActionMask = 0;
			files = (
				OBJ_1014 /* Configuration.framework in Frameworks */,
				OBJ_1015 /* LoggerAPI.framework in Frameworks */,
			);
			runOnlyForDeploymentPostprocessing = 0;
		};
		OBJ_1028 /* Frameworks */ = {
			isa = PBXFrameworksBuildPhase;
			buildActionMask = 0;
			files = (
				OBJ_1029 /* LoggerAPI.framework in Frameworks */,
			);
			runOnlyForDeploymentPostprocessing = 0;
		};
		OBJ_1036 /* Frameworks */ = {
			isa = PBXFrameworksBuildPhase;
			buildActionMask = 0;
			files = (
			);
			runOnlyForDeploymentPostprocessing = 0;
		};
		OBJ_474 /* Frameworks */ = {
			isa = PBXFrameworksBuildPhase;
			buildActionMask = 0;
			files = (
				OBJ_475 /* CORE.framework in Frameworks */,
				OBJ_476 /* KituraCORS.framework in Frameworks */,
				OBJ_477 /* HeliumLogger.framework in Frameworks */,
				OBJ_478 /* CredentialsHTTP.framework in Frameworks */,
				OBJ_479 /* Credentials.framework in Frameworks */,
				OBJ_480 /* KituraSession.framework in Frameworks */,
				OBJ_481 /* Cryptor.framework in Frameworks */,
				OBJ_482 /* Kitura.framework in Frameworks */,
				OBJ_483 /* KituraTemplateEngine.framework in Frameworks */,
				OBJ_484 /* SwiftyJSON.framework in Frameworks */,
				OBJ_485 /* KituraNet.framework in Frameworks */,
				OBJ_486 /* SSLService.framework in Frameworks */,
				OBJ_487 /* CHTTPParser.framework in Frameworks */,
				OBJ_488 /* SwiftKueryMySQL.framework in Frameworks */,
				OBJ_489 /* SwiftKuery.framework in Frameworks */,
				OBJ_490 /* CryptoSwift.framework in Frameworks */,
				OBJ_491 /* Socket.framework in Frameworks */,
				OBJ_492 /* Configuration.framework in Frameworks */,
				OBJ_493 /* LoggerAPI.framework in Frameworks */,
			);
			runOnlyForDeploymentPostprocessing = 0;
		};
		OBJ_550 /* Frameworks */ = {
			isa = PBXFrameworksBuildPhase;
			buildActionMask = 0;
			files = (
				OBJ_551 /* KituraCORS.framework in Frameworks */,
				OBJ_552 /* HeliumLogger.framework in Frameworks */,
				OBJ_553 /* CredentialsHTTP.framework in Frameworks */,
				OBJ_554 /* Credentials.framework in Frameworks */,
				OBJ_555 /* KituraSession.framework in Frameworks */,
				OBJ_556 /* Cryptor.framework in Frameworks */,
				OBJ_557 /* Kitura.framework in Frameworks */,
				OBJ_558 /* KituraTemplateEngine.framework in Frameworks */,
				OBJ_559 /* SwiftyJSON.framework in Frameworks */,
				OBJ_560 /* KituraNet.framework in Frameworks */,
				OBJ_561 /* SSLService.framework in Frameworks */,
				OBJ_562 /* CHTTPParser.framework in Frameworks */,
				OBJ_563 /* SwiftKueryMySQL.framework in Frameworks */,
				OBJ_564 /* SwiftKuery.framework in Frameworks */,
				OBJ_565 /* CryptoSwift.framework in Frameworks */,
				OBJ_566 /* Socket.framework in Frameworks */,
				OBJ_567 /* Configuration.framework in Frameworks */,
				OBJ_568 /* LoggerAPI.framework in Frameworks */,
			);
			runOnlyForDeploymentPostprocessing = 0;
		};
		OBJ_595 /* Frameworks */ = {
			isa = PBXFrameworksBuildPhase;
			buildActionMask = 0;
			files = (
				OBJ_596 /* Kitura.framework in Frameworks */,
				OBJ_597 /* KituraTemplateEngine.framework in Frameworks */,
				OBJ_598 /* SwiftyJSON.framework in Frameworks */,
				OBJ_599 /* KituraNet.framework in Frameworks */,
				OBJ_600 /* SSLService.framework in Frameworks */,
				OBJ_601 /* Socket.framework in Frameworks */,
				OBJ_602 /* LoggerAPI.framework in Frameworks */,
				OBJ_603 /* CHTTPParser.framework in Frameworks */,
			);
			runOnlyForDeploymentPostprocessing = 0;
		};
		OBJ_618 /* Frameworks */ = {
			isa = PBXFrameworksBuildPhase;
			buildActionMask = 0;
			files = (
				OBJ_619 /* LoggerAPI.framework in Frameworks */,
			);
			runOnlyForDeploymentPostprocessing = 0;
		};
		OBJ_629 /* Frameworks */ = {
			isa = PBXFrameworksBuildPhase;
			buildActionMask = 0;
			files = (
				OBJ_630 /* Credentials.framework in Frameworks */,
				OBJ_631 /* KituraSession.framework in Frameworks */,
				OBJ_632 /* Cryptor.framework in Frameworks */,
				OBJ_633 /* Kitura.framework in Frameworks */,
				OBJ_634 /* KituraTemplateEngine.framework in Frameworks */,
				OBJ_635 /* SwiftyJSON.framework in Frameworks */,
				OBJ_636 /* KituraNet.framework in Frameworks */,
				OBJ_637 /* SSLService.framework in Frameworks */,
				OBJ_638 /* Socket.framework in Frameworks */,
				OBJ_639 /* LoggerAPI.framework in Frameworks */,
				OBJ_640 /* CHTTPParser.framework in Frameworks */,
			);
			runOnlyForDeploymentPostprocessing = 0;
		};
		OBJ_662 /* Frameworks */ = {
			isa = PBXFrameworksBuildPhase;
			buildActionMask = 0;
			files = (
				OBJ_663 /* KituraSession.framework in Frameworks */,
				OBJ_664 /* Cryptor.framework in Frameworks */,
				OBJ_665 /* Kitura.framework in Frameworks */,
				OBJ_666 /* KituraTemplateEngine.framework in Frameworks */,
				OBJ_667 /* SwiftyJSON.framework in Frameworks */,
				OBJ_668 /* KituraNet.framework in Frameworks */,
				OBJ_669 /* SSLService.framework in Frameworks */,
				OBJ_670 /* Socket.framework in Frameworks */,
				OBJ_671 /* LoggerAPI.framework in Frameworks */,
				OBJ_672 /* CHTTPParser.framework in Frameworks */,
			);
			runOnlyForDeploymentPostprocessing = 0;
		};
		OBJ_695 /* Frameworks */ = {
			isa = PBXFrameworksBuildPhase;
			buildActionMask = 0;
			files = (
				OBJ_696 /* Cryptor.framework in Frameworks */,
				OBJ_697 /* Kitura.framework in Frameworks */,
				OBJ_698 /* KituraTemplateEngine.framework in Frameworks */,
				OBJ_699 /* SwiftyJSON.framework in Frameworks */,
				OBJ_700 /* KituraNet.framework in Frameworks */,
				OBJ_701 /* SSLService.framework in Frameworks */,
				OBJ_702 /* Socket.framework in Frameworks */,
				OBJ_703 /* LoggerAPI.framework in Frameworks */,
				OBJ_704 /* CHTTPParser.framework in Frameworks */,
			);
			runOnlyForDeploymentPostprocessing = 0;
		};
		OBJ_728 /* Frameworks */ = {
			isa = PBXFrameworksBuildPhase;
			buildActionMask = 0;
			files = (
			);
			runOnlyForDeploymentPostprocessing = 0;
		};
		OBJ_777 /* Frameworks */ = {
			isa = PBXFrameworksBuildPhase;
			buildActionMask = 0;
			files = (
				OBJ_778 /* KituraTemplateEngine.framework in Frameworks */,
				OBJ_779 /* SwiftyJSON.framework in Frameworks */,
				OBJ_780 /* KituraNet.framework in Frameworks */,
				OBJ_781 /* SSLService.framework in Frameworks */,
				OBJ_782 /* Socket.framework in Frameworks */,
				OBJ_783 /* LoggerAPI.framework in Frameworks */,
				OBJ_784 /* CHTTPParser.framework in Frameworks */,
			);
			runOnlyForDeploymentPostprocessing = 0;
		};
		OBJ_797 /* Frameworks */ = {
			isa = PBXFrameworksBuildPhase;
			buildActionMask = 0;
			files = (
			);
			runOnlyForDeploymentPostprocessing = 0;
		};
		OBJ_804 /* Frameworks */ = {
			isa = PBXFrameworksBuildPhase;
			buildActionMask = 0;
			files = (
			);
			runOnlyForDeploymentPostprocessing = 0;
		};
		OBJ_845 /* Frameworks */ = {
			isa = PBXFrameworksBuildPhase;
			buildActionMask = 0;
			files = (
				OBJ_846 /* SSLService.framework in Frameworks */,
				OBJ_847 /* Socket.framework in Frameworks */,
				OBJ_848 /* LoggerAPI.framework in Frameworks */,
				OBJ_849 /* CHTTPParser.framework in Frameworks */,
			);
			runOnlyForDeploymentPostprocessing = 0;
		};
		OBJ_859 /* Frameworks */ = {
			isa = PBXFrameworksBuildPhase;
			buildActionMask = 0;
			files = (
				OBJ_860 /* Socket.framework in Frameworks */,
			);
			runOnlyForDeploymentPostprocessing = 0;
		};
		OBJ_868 /* Frameworks */ = {
			isa = PBXFrameworksBuildPhase;
			buildActionMask = 0;
			files = (
			);
			runOnlyForDeploymentPostprocessing = 0;
		};
		OBJ_877 /* Frameworks */ = {
			isa = PBXFrameworksBuildPhase;
			buildActionMask = 0;
			files = (
				OBJ_878 /* SwiftKuery.framework in Frameworks */,
			);
			runOnlyForDeploymentPostprocessing = 0;
		};
		OBJ_932 /* Frameworks */ = {
			isa = PBXFrameworksBuildPhase;
			buildActionMask = 0;
			files = (
			);
			runOnlyForDeploymentPostprocessing = 0;
		};
		OBJ_999 /* Frameworks */ = {
			isa = PBXFrameworksBuildPhase;
			buildActionMask = 0;
			files = (
			);
			runOnlyForDeploymentPostprocessing = 0;
		};
/* End PBXFrameworksBuildPhase section */

/* Begin PBXGroup section */
		OBJ_106 /* bodyParser */ = {
			isa = PBXGroup;
			children = (
				OBJ_107 /* BodyParser.swift */,
				OBJ_108 /* BodyParserProtocol.swift */,
				OBJ_109 /* JSONBodyParser.swift */,
				OBJ_110 /* MultiPartBodyParser.swift */,
				OBJ_111 /* ParsedBody.swift */,
				OBJ_112 /* Part.swift */,
				OBJ_113 /* RawBodyParser.swift */,
				OBJ_114 /* TextBodyParser.swift */,
				OBJ_115 /* URLEncodedBodyParser.swift */,
			);
			path = bodyParser;
			sourceTree = "<group>";
		};
		OBJ_116 /* contentType */ = {
			isa = PBXGroup;
			children = (
				OBJ_117 /* ContentType.swift */,
				OBJ_118 /* types.swift */,
			);
			path = contentType;
			sourceTree = "<group>";
		};
		OBJ_119 /* staticFileServer */ = {
			isa = PBXGroup;
			children = (
				OBJ_120 /* CacheRelatedHeadersSetter.swift */,
				OBJ_121 /* CompositeHeadersSetter.swift */,
				OBJ_122 /* FileServer.swift */,
				OBJ_123 /* ResourcePathHandler.swift */,
				OBJ_124 /* ResponseHeadersSetter.swift */,
				OBJ_125 /* StaticFileServer.swift */,
			);
			path = staticFileServer;
			sourceTree = "<group>";
		};
		OBJ_127 /* Kitura-TemplateEngine 1.7.2 */ = {
			isa = PBXGroup;
			children = (
				OBJ_128 /* KituraTemplateEngine */,
				OBJ_130 /* Package.swift */,
			);
			name = "Kitura-TemplateEngine 1.7.2";
			sourceTree = SOURCE_ROOT;
		};
		OBJ_128 /* KituraTemplateEngine */ = {
			isa = PBXGroup;
			children = (
				OBJ_129 /* TemplateEngine.swift */,
			);
			name = KituraTemplateEngine;
			path = ".build/checkouts/Kitura-TemplateEngine.git--5059963620657797085/Sources/KituraTemplateEngine";
			sourceTree = SOURCE_ROOT;
		};
		OBJ_131 /* SwiftyJSON 17.0.0 */ = {
			isa = PBXGroup;
			children = (
				OBJ_132 /* SwiftyJSON */,
				OBJ_135 /* Package.swift */,
			);
			name = "SwiftyJSON 17.0.0";
			sourceTree = SOURCE_ROOT;
		};
		OBJ_132 /* SwiftyJSON */ = {
			isa = PBXGroup;
			children = (
				OBJ_133 /* LclJSONSerialization.swift */,
				OBJ_134 /* SwiftyJSON.swift */,
			);
			name = SwiftyJSON;
			path = ".build/checkouts/SwiftyJSON.git--6955445084174387031/Sources/SwiftyJSON";
			sourceTree = SOURCE_ROOT;
		};
		OBJ_136 /* Kitura-net 1.7.16 */ = {
			isa = PBXGroup;
			children = (
				OBJ_137 /* CHTTPParser */,
				OBJ_145 /* KituraNet */,
				OBJ_186 /* Package.swift */,
			);
			name = "Kitura-net 1.7.16";
			sourceTree = SOURCE_ROOT;
		};
		OBJ_137 /* CHTTPParser */ = {
			isa = PBXGroup;
			children = (
				OBJ_138 /* http_parser.c */,
				OBJ_139 /* utils.c */,
				OBJ_140 /* include */,
			);
			name = CHTTPParser;
			path = ".build/checkouts/Kitura-net.git--7410958935072501107/Sources/CHTTPParser";
			sourceTree = SOURCE_ROOT;
		};
		OBJ_140 /* include */ = {
			isa = PBXGroup;
			children = (
				OBJ_141 /* CHTTPParser.h */,
				OBJ_142 /* http_parser.h */,
				OBJ_143 /* utils.h */,
				OBJ_144 /* module.modulemap */,
			);
			path = include;
			sourceTree = "<group>";
		};
		OBJ_145 /* KituraNet */ = {
			isa = PBXGroup;
			children = (
				OBJ_146 /* BufferList.swift */,
				OBJ_147 /* ClientRequest.swift */,
				OBJ_148 /* ClientResponse.swift */,
				OBJ_149 /* ConnectionUpgradeFactory.swift */,
				OBJ_150 /* ConnectionUpgrader.swift */,
				OBJ_151 /* Error.swift */,
				OBJ_152 /* FastCGI */,
				OBJ_159 /* HTTP */,
				OBJ_166 /* HTTPParser */,
				OBJ_171 /* HeadersContainer.swift */,
				OBJ_172 /* IncomingSocketHandler.swift */,
				OBJ_173 /* IncomingSocketManager.swift */,
				OBJ_174 /* IncomingSocketProcessor.swift */,
				OBJ_175 /* IncomingSocketProcessorCreator.swift */,
				OBJ_176 /* ListenerGroup.swift */,
				OBJ_177 /* SPIUtils.swift */,
				OBJ_178 /* Server */,
				OBJ_184 /* ServerRequest.swift */,
				OBJ_185 /* ServerResponse.swift */,
			);
			name = KituraNet;
			path = ".build/checkouts/Kitura-net.git--7410958935072501107/Sources/KituraNet";
			sourceTree = SOURCE_ROOT;
		};
		OBJ_152 /* FastCGI */ = {
			isa = PBXGroup;
			children = (
				OBJ_153 /* FastCGI.swift */,
				OBJ_154 /* FastCGIRecordCreate.swift */,
				OBJ_155 /* FastCGIRecordParser.swift */,
				OBJ_156 /* FastCGIServer.swift */,
				OBJ_157 /* FastCGIServerRequest.swift */,
				OBJ_158 /* FastCGIServerResponse.swift */,
			);
			path = FastCGI;
			sourceTree = "<group>";
		};
		OBJ_159 /* HTTP */ = {
			isa = PBXGroup;
			children = (
				OBJ_160 /* HTTP.swift */,
				OBJ_161 /* HTTPServer.swift */,
				OBJ_162 /* HTTPServerRequest.swift */,
				OBJ_163 /* HTTPServerResponse.swift */,
				OBJ_164 /* IncomingHTTPSocketProcessor.swift */,
				OBJ_165 /* KeepAliveState.swift */,
			);
			path = HTTP;
			sourceTree = "<group>";
		};
		OBJ_166 /* HTTPParser */ = {
			isa = PBXGroup;
			children = (
				OBJ_167 /* HTTPParser.swift */,
				OBJ_168 /* HTTPParserStatus.swift */,
				OBJ_169 /* ParseResults.swift */,
				OBJ_170 /* URLParser.swift */,
			);
			path = HTTPParser;
			sourceTree = "<group>";
		};
		OBJ_178 /* Server */ = {
			isa = PBXGroup;
			children = (
				OBJ_179 /* Server.swift */,
				OBJ_180 /* ServerDelegate.swift */,
				OBJ_181 /* ServerLifecycleListener.swift */,
				OBJ_182 /* ServerMonitor.swift */,
				OBJ_183 /* ServerState.swift */,
			);
			path = Server;
			sourceTree = "<group>";
		};
		OBJ_187 /* SSLService 0.12.55 */ = {
			isa = PBXGroup;
			children = (
				OBJ_188 /* SSLService */,
				OBJ_190 /* Package.swift */,
			);
			name = "SSLService 0.12.55";
			sourceTree = SOURCE_ROOT;
		};
		OBJ_188 /* SSLService */ = {
			isa = PBXGroup;
			children = (
				OBJ_189 /* SSLService.swift */,
			);
			name = SSLService;
			path = ".build/checkouts/BlueSSLService.git--6577639804771281610/Sources/SSLService";
			sourceTree = SOURCE_ROOT;
		};
		OBJ_191 /* SwiftKueryMySQL 0.13.1 */ = {
			isa = PBXGroup;
			children = (
				OBJ_192 /* SwiftKueryMySQL */,
				OBJ_197 /* Package.swift */,
			);
			name = "SwiftKueryMySQL 0.13.1";
			sourceTree = SOURCE_ROOT;
		};
		OBJ_192 /* SwiftKueryMySQL */ = {
			isa = PBXGroup;
			children = (
				OBJ_193 /* MySQLConnection.swift */,
				OBJ_194 /* MySQLPreparedStatement.swift */,
				OBJ_195 /* MySQLResultFetcher.swift */,
				OBJ_196 /* MySQLThreadSafeConnection.swift */,
			);
			name = SwiftKueryMySQL;
			path = ".build/checkouts/SwiftKueryMySQL.git-7601298671331203969/Sources/SwiftKueryMySQL";
			sourceTree = SOURCE_ROOT;
		};
		OBJ_198 /* SwiftKuery 0.13.3 */ = {
			isa = PBXGroup;
			children = (
				OBJ_199 /* SwiftKuery */,
				OBJ_248 /* Package.swift */,
			);
			name = "SwiftKuery 0.13.3";
			sourceTree = SOURCE_ROOT;
		};
		OBJ_199 /* SwiftKuery */ = {
			isa = PBXGroup;
			children = (
				OBJ_200 /* AggregateColumnExpression.swift */,
				OBJ_201 /* AuxiliaryTable.swift */,
				OBJ_202 /* Buildable.swift */,
				OBJ_203 /* Column.swift */,
				OBJ_204 /* ColumnAndExpressions_Extensions.swift */,
				OBJ_205 /* Condition.swift */,
				OBJ_206 /* ConditionalClause.swift */,
				OBJ_207 /* Connection.swift */,
				OBJ_208 /* ConnectionPool.swift */,
				OBJ_209 /* ConnectionPoolConnection.swift */,
				OBJ_210 /* ConnectionPoolOptions.swift */,
				OBJ_211 /* Delete.swift */,
				OBJ_212 /* Field.swift */,
				OBJ_213 /* Filter.swift */,
				OBJ_214 /* FilterAndHaving_Extensions.swift */,
				OBJ_215 /* FilterAndHaving_GlobalFunctions.swift */,
				OBJ_216 /* Having.swift */,
				OBJ_217 /* Index.swift */,
				OBJ_218 /* IndexColumn.swift */,
				OBJ_219 /* IndexColumnOrdered.swift */,
				OBJ_220 /* Insert.swift */,
				OBJ_221 /* Join.swift */,
				OBJ_222 /* Migration.swift */,
				OBJ_223 /* OrderBy.swift */,
				OBJ_224 /* Parameter.swift */,
				OBJ_225 /* Predicate.swift */,
				OBJ_226 /* PreparedStatement.swift */,
				OBJ_227 /* Query.swift */,
				OBJ_228 /* QueryBuilder.swift */,
				OBJ_229 /* QueryError.swift */,
				OBJ_230 /* QueryResult.swift */,
				OBJ_231 /* QuerySuffixProtocol.swift */,
				OBJ_232 /* Raw.swift */,
				OBJ_233 /* RawField.swift */,
				OBJ_234 /* ResultFetcher.swift */,
				OBJ_235 /* ResultSet.swift */,
				OBJ_236 /* RowSequence.swift */,
				OBJ_237 /* SQLDataType.swift */,
				OBJ_238 /* ScalarColumnExpression.swift */,
				OBJ_239 /* Select.swift */,
				OBJ_240 /* SpecialOperators_Extensions.swift */,
				OBJ_241 /* String+Buildable.swift */,
				OBJ_242 /* Subqueries_GlobalFunctionsAndExtensions.swift */,
				OBJ_243 /* Table.swift */,
				OBJ_244 /* Union.swift */,
				OBJ_245 /* Update.swift */,
				OBJ_246 /* Utils.swift */,
				OBJ_247 /* With.swift */,
			);
			name = SwiftKuery;
			path = ".build/checkouts/Swift-Kuery.git-1645988340584907058/Sources/SwiftKuery";
			sourceTree = SOURCE_ROOT;
		};
		OBJ_21 /* SERVER */ = {
			isa = PBXGroup;
			children = (
				OBJ_22 /* main.swift */,
			);
			name = SERVER;
			path = Sources/SERVER;
			sourceTree = SOURCE_ROOT;
		};
		OBJ_23 /* Tests */ = {
			isa = PBXGroup;
			children = (
			);
			name = Tests;
			sourceTree = SOURCE_ROOT;
		};
		OBJ_249 /* CryptoSwift 0.7.2 */ = {
			isa = PBXGroup;
			children = (
				OBJ_250 /* CryptoSwift */,
				OBJ_316 /* Package.swift */,
			);
			name = "CryptoSwift 0.7.2";
			sourceTree = SOURCE_ROOT;
		};
		OBJ_25 /* Dependencies */ = {
			isa = PBXGroup;
			children = (
				OBJ_26 /* KituraCORS 1.7.0 */,
				OBJ_32 /* HeliumLogger 1.7.0 */,
				OBJ_37 /* Kitura-CredentialsHTTP 1.8.0 */,
				OBJ_44 /* Kitura-Credentials 1.7.2 */,
				OBJ_53 /* Kitura-Session 1.7.0 */,
				OBJ_64 /* Cryptor 0.8.17 */,
				OBJ_77 /* Kitura 1.7.9 */,
				OBJ_127 /* Kitura-TemplateEngine 1.7.2 */,
				OBJ_131 /* SwiftyJSON 17.0.0 */,
				OBJ_136 /* Kitura-net 1.7.16 */,
				OBJ_187 /* SSLService 0.12.55 */,
				OBJ_191 /* SwiftKueryMySQL 0.13.1 */,
				OBJ_198 /* SwiftKuery 0.13.3 */,
				OBJ_249 /* CryptoSwift 0.7.2 */,
				OBJ_317 /* Socket 0.12.61 */,
				OBJ_322 /* Configuration 1.0.1 */,
				OBJ_334 /* LoggerAPI 1.7.1 */,
			);
			name = Dependencies;
			sourceTree = "<group>";
		};
		OBJ_250 /* CryptoSwift */ = {
			isa = PBXGroup;
			children = (
				OBJ_251 /* AES.swift */,
				OBJ_252 /* Array+Extension.swift */,
				OBJ_253 /* Authenticator.swift */,
				OBJ_254 /* BatchedCollection.swift */,
				OBJ_255 /* Bit.swift */,
				OBJ_256 /* BlockCipher.swift */,
				OBJ_257 /* BlockMode */,
				OBJ_268 /* Blowfish.swift */,
				OBJ_269 /* CSArrayType+Extensions.swift */,
				OBJ_270 /* ChaCha20.swift */,
				OBJ_271 /* Checksum.swift */,
				OBJ_272 /* Cipher.swift */,
				OBJ_273 /* Collection+Extension.swift */,
				OBJ_274 /* Cryptors.swift */,
				OBJ_275 /* Digest.swift */,
				OBJ_276 /* DigestType.swift */,
				OBJ_277 /* Foundation */,
				OBJ_287 /* Generics.swift */,
				OBJ_288 /* HMAC.swift */,
				OBJ_289 /* Int+Extension.swift */,
				OBJ_290 /* MD5.swift */,
				OBJ_291 /* NoPadding.swift */,
				OBJ_292 /* Operators.swift */,
				OBJ_293 /* PKCS */,
				OBJ_299 /* Padding.swift */,
				OBJ_300 /* Poly1305.swift */,
				OBJ_301 /* Rabbit.swift */,
				OBJ_302 /* RandomAccessCryptor.swift */,
				OBJ_303 /* RandomBytesSequence.swift */,
				OBJ_304 /* SHA1.swift */,
				OBJ_305 /* SHA2.swift */,
				OBJ_306 /* SHA3.swift */,
				OBJ_307 /* SecureBytes.swift */,
				OBJ_308 /* String+Extension.swift */,
				OBJ_309 /* UInt16+Extension.swift */,
				OBJ_310 /* UInt32+Extension.swift */,
				OBJ_311 /* UInt64+Extension.swift */,
				OBJ_312 /* UInt8+Extension.swift */,
				OBJ_313 /* Updatable.swift */,
				OBJ_314 /* Utils.swift */,
				OBJ_315 /* ZeroPadding.swift */,
			);
			name = CryptoSwift;
			path = ".build/checkouts/CryptoSwift.git--6440749087414195235/Sources/CryptoSwift";
			sourceTree = SOURCE_ROOT;
		};
		OBJ_257 /* BlockMode */ = {
			isa = PBXGroup;
			children = (
				OBJ_258 /* BlockMode.swift */,
				OBJ_259 /* BlockModeOptions.swift */,
				OBJ_260 /* BlockModeWorker.swift */,
				OBJ_261 /* CBC.swift */,
				OBJ_262 /* CFB.swift */,
				OBJ_263 /* CTR.swift */,
				OBJ_264 /* ECB.swift */,
				OBJ_265 /* OFB.swift */,
				OBJ_266 /* PCBC.swift */,
				OBJ_267 /* RandomAccessBlockModeWorker.swift */,
			);
			path = BlockMode;
			sourceTree = "<group>";
		};
		OBJ_26 /* KituraCORS 1.7.0 */ = {
			isa = PBXGroup;
			children = (
				OBJ_27 /* KituraCORS */,
				OBJ_31 /* Package.swift */,
			);
			name = "KituraCORS 1.7.0";
			sourceTree = SOURCE_ROOT;
		};
		OBJ_27 /* KituraCORS */ = {
			isa = PBXGroup;
			children = (
				OBJ_28 /* AllowedOrigins.swift */,
				OBJ_29 /* CORS.swift */,
				OBJ_30 /* Options.swift */,
			);
			name = KituraCORS;
			path = ".build/checkouts/Kitura-CORS.git-6045985022829947324/Sources/KituraCORS";
			sourceTree = SOURCE_ROOT;
		};
		OBJ_277 /* Foundation */ = {
			isa = PBXGroup;
			children = (
				OBJ_278 /* AES+Foundation.swift */,
				OBJ_279 /* Blowfish+Foundation.swift */,
				OBJ_280 /* CSArrayType+Foundation.swift */,
				OBJ_281 /* ChaCha20+Foundation.swift */,
				OBJ_282 /* Data+Extension.swift */,
				OBJ_283 /* HMAC+Foundation.swift */,
				OBJ_284 /* Rabbit+Foundation.swift */,
				OBJ_285 /* String+FoundationExtension.swift */,
				OBJ_286 /* Utils+Foundation.swift */,
			);
			path = Foundation;
			sourceTree = "<group>";
		};
		OBJ_293 /* PKCS */ = {
			isa = PBXGroup;
			children = (
				OBJ_294 /* PBKDF1.swift */,
				OBJ_295 /* PBKDF2.swift */,
				OBJ_296 /* PKCS5.swift */,
				OBJ_297 /* PKCS7.swift */,
				OBJ_298 /* PKCS7Padding.swift */,
			);
			path = PKCS;
			sourceTree = "<group>";
		};
		OBJ_317 /* Socket 0.12.61 */ = {
			isa = PBXGroup;
			children = (
				OBJ_318 /* Package.swift */,
				OBJ_319 /* Socket.swift */,
				OBJ_320 /* SocketProtocols.swift */,
				OBJ_321 /* SocketUtils.swift */,
			);
			name = "Socket 0.12.61";
			path = ".build/checkouts/BlueSocket.git-3162807777605905816/Sources";
			sourceTree = SOURCE_ROOT;
		};
		OBJ_32 /* HeliumLogger 1.7.0 */ = {
			isa = PBXGroup;
			children = (
				OBJ_33 /* HeliumLogger */,
				OBJ_36 /* Package.swift */,
			);
			name = "HeliumLogger 1.7.0";
			sourceTree = SOURCE_ROOT;
		};
		OBJ_322 /* Configuration 1.0.1 */ = {
			isa = PBXGroup;
			children = (
				OBJ_323 /* Configuration */,
				OBJ_331 /* ConfigurationTestExecutable */,
				OBJ_333 /* Package.swift */,
			);
			name = "Configuration 1.0.1";
			sourceTree = SOURCE_ROOT;
		};
		OBJ_323 /* Configuration */ = {
			isa = PBXGroup;
			children = (
				OBJ_324 /* ConfigurationManager.swift */,
				OBJ_325 /* ConfigurationNode.swift */,
				OBJ_326 /* Deserializer.swift */,
				OBJ_327 /* Deserializers */,
				OBJ_330 /* PathUtilities.swift */,
			);
			name = Configuration;
			path = ".build/checkouts/Configuration.git--2683441109504822782/Sources/Configuration";
			sourceTree = SOURCE_ROOT;
		};
		OBJ_327 /* Deserializers */ = {
			isa = PBXGroup;
			children = (
				OBJ_328 /* JSONDeserializer.swift */,
				OBJ_329 /* PLISTDeserializer.swift */,
			);
			path = Deserializers;
			sourceTree = "<group>";
		};
		OBJ_33 /* HeliumLogger */ = {
			isa = PBXGroup;
			children = (
				OBJ_34 /* HeliumLogger.swift */,
				OBJ_35 /* HeliumStreamLogger.swift */,
			);
			name = HeliumLogger;
			path = ".build/checkouts/HeliumLogger.git-2106793442615829935/Sources/HeliumLogger";
			sourceTree = SOURCE_ROOT;
		};
		OBJ_331 /* ConfigurationTestExecutable */ = {
			isa = PBXGroup;
			children = (
				OBJ_332 /* main.swift */,
			);
			name = ConfigurationTestExecutable;
			path = ".build/checkouts/Configuration.git--2683441109504822782/Sources/ConfigurationTestExecutable";
			sourceTree = SOURCE_ROOT;
		};
		OBJ_334 /* LoggerAPI 1.7.1 */ = {
			isa = PBXGroup;
			children = (
				OBJ_335 /* LoggerAPI */,
				OBJ_337 /* Package.swift */,
			);
			name = "LoggerAPI 1.7.1";
			sourceTree = SOURCE_ROOT;
		};
		OBJ_335 /* LoggerAPI */ = {
			isa = PBXGroup;
			children = (
				OBJ_336 /* Logger.swift */,
			);
			name = LoggerAPI;
			path = ".build/checkouts/LoggerAPI.git--6449715459278086880/Sources/LoggerAPI";
			sourceTree = SOURCE_ROOT;
		};
		OBJ_338 /* Products */ = {
			isa = PBXGroup;
			children = (
				"mikrotik_router_manager::SERVER::Product" /* SERVER */,
				"mikrotik_router_manager::CORE::Product" /* CORE.framework */,
				"KituraCORS::KituraCORS::Product" /* KituraCORS.framework */,
				"HeliumLogger::HeliumLogger::Product" /* HeliumLogger.framework */,
				"Kitura-CredentialsHTTP::CredentialsHTTP::Product" /* CredentialsHTTP.framework */,
				"Kitura-Credentials::Credentials::Product" /* Credentials.framework */,
				"Kitura-Session::KituraSession::Product" /* KituraSession.framework */,
				"Cryptor::Cryptor::Product" /* Cryptor.framework */,
				"Kitura::Kitura::Product" /* Kitura.framework */,
				"Kitura-TemplateEngine::KituraTemplateEngine::Product" /* KituraTemplateEngine.framework */,
				"SwiftyJSON::SwiftyJSON::Product" /* SwiftyJSON.framework */,
				"Kitura-net::KituraNet::Product" /* KituraNet.framework */,
				"SSLService::SSLService::Product" /* SSLService.framework */,
				"Kitura-net::CHTTPParser::Product" /* CHTTPParser.framework */,
				"SwiftKueryMySQL::SwiftKueryMySQL::Product" /* SwiftKueryMySQL.framework */,
				"SwiftKuery::SwiftKuery::Product" /* SwiftKuery.framework */,
				"CryptoSwift::CryptoSwift::Product" /* CryptoSwift.framework */,
				"Socket::Socket::Product" /* Socket.framework */,
				"Configuration::ConfigurationTestExecutable::Product" /* ConfigurationTestExecutable */,
				"Configuration::Configuration::Product" /* Configuration.framework */,
				"LoggerAPI::LoggerAPI::Product" /* LoggerAPI.framework */,
			);
			name = Products;
			sourceTree = BUILT_PRODUCTS_DIR;
		};
		OBJ_37 /* Kitura-CredentialsHTTP 1.8.0 */ = {
			isa = PBXGroup;
			children = (
				OBJ_38 /* CredentialsHTTP */,
				OBJ_43 /* Package.swift */,
			);
			name = "Kitura-CredentialsHTTP 1.8.0";
			sourceTree = SOURCE_ROOT;
		};
		OBJ_38 /* CredentialsHTTP */ = {
			isa = PBXGroup;
			children = (
				OBJ_39 /* CredentialsHTTPBasic.swift */,
				OBJ_40 /* CredentialsHTTPDigest.swift */,
				OBJ_41 /* UserProfileLoader.swift */,
				OBJ_42 /* VerifyPassword.swift */,
			);
			name = CredentialsHTTP;
			path = ".build/checkouts/Kitura-CredentialsHTTP.git--2255905302832386242/Sources/CredentialsHTTP";
			sourceTree = SOURCE_ROOT;
		};
		OBJ_44 /* Kitura-Credentials 1.7.2 */ = {
			isa = PBXGroup;
			children = (
				OBJ_45 /* Credentials */,
				OBJ_52 /* Package.swift */,
			);
			name = "Kitura-Credentials 1.7.2";
			sourceTree = SOURCE_ROOT;
		};
		OBJ_45 /* Credentials */ = {
			isa = PBXGroup;
			children = (
				OBJ_46 /* BaseCacheElement.swift */,
				OBJ_47 /* Credentials.swift */,
				OBJ_48 /* CredentialsPluginProtocol.swift */,
				OBJ_49 /* RouterRequest+UserProfile.swift */,
				OBJ_50 /* UserProfile.swift */,
				OBJ_51 /* UserProfileDelegate.swift */,
			);
			name = Credentials;
			path = ".build/checkouts/Kitura-Credentials.git-1137106172743287290/Sources/Credentials";
			sourceTree = SOURCE_ROOT;
		};
		OBJ_5 /*  */ = {
			isa = PBXGroup;
			children = (
				OBJ_6 /* Package.swift */,
				OBJ_7 /* Sources */,
				OBJ_23 /* Tests */,
				OBJ_24 /* Database */,
				OBJ_25 /* Dependencies */,
				OBJ_338 /* Products */,
			);
			name = "";
			sourceTree = "<group>";
		};
		OBJ_53 /* Kitura-Session 1.7.0 */ = {
			isa = PBXGroup;
			children = (
				OBJ_54 /* KituraSession */,
				OBJ_63 /* Package.swift */,
			);
			name = "Kitura-Session 1.7.0";
			sourceTree = SOURCE_ROOT;
		};
		OBJ_54 /* KituraSession */ = {
			isa = PBXGroup;
			children = (
				OBJ_55 /* CookieCryptography.swift */,
				OBJ_56 /* CookieManagement.swift */,
				OBJ_57 /* CookieParameter.swift */,
				OBJ_58 /* InMemoryStore.swift */,
				OBJ_59 /* RouterRequest+Session.swift */,
				OBJ_60 /* Session.swift */,
				OBJ_61 /* SessionState.swift */,
				OBJ_62 /* Store.swift */,
			);
			name = KituraSession;
			path = ".build/checkouts/Kitura-Session.git-4044573149666132076/Sources/KituraSession";
			sourceTree = SOURCE_ROOT;
		};
		OBJ_64 /* Cryptor 0.8.17 */ = {
			isa = PBXGroup;
			children = (
				OBJ_65 /* Cryptor */,
				OBJ_76 /* Package.swift */,
			);
			name = "Cryptor 0.8.17";
			sourceTree = SOURCE_ROOT;
		};
		OBJ_65 /* Cryptor */ = {
			isa = PBXGroup;
			children = (
				OBJ_66 /* Crypto.swift */,
				OBJ_67 /* Cryptor.swift */,
				OBJ_68 /* Digest.swift */,
				OBJ_69 /* HMAC.swift */,
				OBJ_70 /* KeyDerivation.swift */,
				OBJ_71 /* Random.swift */,
				OBJ_72 /* Status.swift */,
				OBJ_73 /* StreamCryptor.swift */,
				OBJ_74 /* Updatable.swift */,
				OBJ_75 /* Utilities.swift */,
			);
			name = Cryptor;
			path = ".build/checkouts/BlueCryptor.git-2709167748876642405/Sources/Cryptor";
			sourceTree = SOURCE_ROOT;
		};
		OBJ_7 /* Sources */ = {
			isa = PBXGroup;
			children = (
				OBJ_8 /* CORE */,
				OBJ_21 /* SERVER */,
			);
			name = Sources;
			sourceTree = SOURCE_ROOT;
		};
		OBJ_77 /* Kitura 1.7.9 */ = {
			isa = PBXGroup;
			children = (
				OBJ_78 /* Kitura */,
				OBJ_126 /* Package.swift */,
			);
			name = "Kitura 1.7.9";
			sourceTree = SOURCE_ROOT;
		};
		OBJ_78 /* Kitura */ = {
			isa = PBXGroup;
			children = (
				OBJ_79 /* Error.swift */,
				OBJ_80 /* FileResourceServer.swift */,
				OBJ_81 /* HTTPVersion.swift */,
				OBJ_82 /* Headers.swift */,
				OBJ_83 /* InternalError.swift */,
				OBJ_84 /* JSONPError.swift */,
				OBJ_85 /* Kitura.swift */,
				OBJ_86 /* LinkParameter.swift */,
				OBJ_87 /* MimeTypeAcceptor.swift */,
				OBJ_88 /* RouteRegex.swift */,
				OBJ_89 /* Router.swift */,
				OBJ_90 /* RouterElement.swift */,
				OBJ_91 /* RouterElementWalker.swift */,
				OBJ_92 /* RouterHTTPVerbs+Error.swift */,
				OBJ_93 /* RouterHTTPVerbs_generated.swift */,
				OBJ_94 /* RouterHandler.swift */,
				OBJ_95 /* RouterMethod.swift */,
				OBJ_96 /* RouterMiddleware.swift */,
				OBJ_97 /* RouterMiddlewareGenerator.swift */,
				OBJ_98 /* RouterMiddlewareWalker.swift */,
				OBJ_99 /* RouterParameterWalker.swift */,
				OBJ_100 /* RouterRequest.swift */,
				OBJ_101 /* RouterResponse.swift */,
				OBJ_102 /* SSLConfig.swift */,
				OBJ_103 /* Stack.swift */,
				OBJ_104 /* String+Extensions.swift */,
				OBJ_105 /* TemplatingError.swift */,
				OBJ_106 /* bodyParser */,
				OBJ_116 /* contentType */,
				OBJ_119 /* staticFileServer */,
			);
			name = Kitura;
			path = ".build/checkouts/Kitura.git-6522211175291160341/Sources/Kitura";
			sourceTree = SOURCE_ROOT;
		};
		OBJ_8 /* CORE */ = {
			isa = PBXGroup;
			children = (
				OBJ_9 /* BaseComponent.swift */,
				OBJ_10 /* Bitter.swift */,
				OBJ_11 /* Engine.swift */,
				OBJ_12 /* EngineConfig.swift */,
				OBJ_13 /* HttpCustomerLogin.swift */,
				OBJ_14 /* HttpServerComponent.swift */,
				OBJ_15 /* HttpUserAPI.swift */,
				OBJ_16 /* HtttpRouterAPI.swift */,
				OBJ_17 /* LogComponent.swift */,
				OBJ_18 /* MikrotikConnection.swift */,
				OBJ_19 /* MysqlConnection.swift */,
				OBJ_20 /* SessionManager.swift */,
			);
			name = CORE;
			path = Sources/CORE;
			sourceTree = SOURCE_ROOT;
		};
/* End PBXGroup section */

/* Begin PBXNativeTarget section */
		"Configuration::Configuration" /* Configuration */ = {
			isa = PBXNativeTarget;
			buildConfigurationList = OBJ_1018 /* Build configuration list for PBXNativeTarget "Configuration" */;
			buildPhases = (
				OBJ_1021 /* Sources */,
				OBJ_1028 /* Frameworks */,
			);
			buildRules = (
			);
			dependencies = (
				OBJ_1030 /* PBXTargetDependency */,
			);
			name = Configuration;
			productName = Configuration;
			productReference = "Configuration::Configuration::Product" /* Configuration.framework */;
			productType = "com.apple.product-type.framework";
		};
		"Configuration::ConfigurationTestExecutable" /* ConfigurationTestExecutable */ = {
			isa = PBXNativeTarget;
			buildConfigurationList = OBJ_1008 /* Build configuration list for PBXNativeTarget "ConfigurationTestExecutable" */;
			buildPhases = (
				OBJ_1011 /* Sources */,
				OBJ_1013 /* Frameworks */,
			);
			buildRules = (
			);
			dependencies = (
				OBJ_1016 /* PBXTargetDependency */,
				OBJ_1017 /* PBXTargetDependency */,
			);
			name = ConfigurationTestExecutable;
			productName = ConfigurationTestExecutable;
			productReference = "Configuration::ConfigurationTestExecutable::Product" /* ConfigurationTestExecutable */;
			productType = "com.apple.product-type.tool";
		};
		"Configuration::SwiftPMPackageDescription" /* ConfigurationPackageDescription */ = {
			isa = PBXNativeTarget;
			buildConfigurationList = OBJ_457 /* Build configuration list for PBXNativeTarget "ConfigurationPackageDescription" */;
			buildPhases = (
				OBJ_460 /* Sources */,
			);
			buildRules = (
			);
			dependencies = (
			);
			name = ConfigurationPackageDescription;
			productName = ConfigurationPackageDescription;
			productType = "com.apple.product-type.framework";
		};
		"CryptoSwift::CryptoSwift" /* CryptoSwift */ = {
			isa = PBXNativeTarget;
			buildConfigurationList = OBJ_933 /* Build configuration list for PBXNativeTarget "CryptoSwift" */;
			buildPhases = (
				OBJ_936 /* Sources */,
				OBJ_999 /* Frameworks */,
			);
			buildRules = (
			);
			dependencies = (
			);
			name = CryptoSwift;
			productName = CryptoSwift;
			productReference = "CryptoSwift::CryptoSwift::Product" /* CryptoSwift.framework */;
			productType = "com.apple.product-type.framework";
		};
		"CryptoSwift::SwiftPMPackageDescription" /* CryptoSwiftPackageDescription */ = {
			isa = PBXNativeTarget;
			buildConfigurationList = OBJ_445 /* Build configuration list for PBXNativeTarget "CryptoSwiftPackageDescription" */;
			buildPhases = (
				OBJ_448 /* Sources */,
			);
			buildRules = (
			);
			dependencies = (
			);
			name = CryptoSwiftPackageDescription;
			productName = CryptoSwiftPackageDescription;
			productType = "com.apple.product-type.framework";
		};
		"Cryptor::Cryptor" /* Cryptor */ = {
			isa = PBXNativeTarget;
			buildConfigurationList = OBJ_714 /* Build configuration list for PBXNativeTarget "Cryptor" */;
			buildPhases = (
				OBJ_717 /* Sources */,
				OBJ_728 /* Frameworks */,
			);
			buildRules = (
			);
			dependencies = (
			);
			name = Cryptor;
			productName = Cryptor;
			productReference = "Cryptor::Cryptor::Product" /* Cryptor.framework */;
			productType = "com.apple.product-type.framework";
		};
		"Cryptor::SwiftPMPackageDescription" /* CryptorPackageDescription */ = {
			isa = PBXNativeTarget;
			buildConfigurationList = OBJ_397 /* Build configuration list for PBXNativeTarget "CryptorPackageDescription" */;
			buildPhases = (
				OBJ_400 /* Sources */,
			);
			buildRules = (
			);
			dependencies = (
			);
			name = CryptorPackageDescription;
			productName = CryptorPackageDescription;
			productType = "com.apple.product-type.framework";
		};
		"HeliumLogger::HeliumLogger" /* HeliumLogger */ = {
			isa = PBXNativeTarget;
			buildConfigurationList = OBJ_612 /* Build configuration list for PBXNativeTarget "HeliumLogger" */;
			buildPhases = (
				OBJ_615 /* Sources */,
				OBJ_618 /* Frameworks */,
			);
			buildRules = (
			);
			dependencies = (
				OBJ_620 /* PBXTargetDependency */,
			);
			name = HeliumLogger;
			productName = HeliumLogger;
			productReference = "HeliumLogger::HeliumLogger::Product" /* HeliumLogger.framework */;
			productType = "com.apple.product-type.framework";
		};
		"HeliumLogger::SwiftPMPackageDescription" /* HeliumLoggerPackageDescription */ = {
			isa = PBXNativeTarget;
			buildConfigurationList = OBJ_373 /* Build configuration list for PBXNativeTarget "HeliumLoggerPackageDescription" */;
			buildPhases = (
				OBJ_376 /* Sources */,
			);
			buildRules = (
			);
			dependencies = (
			);
			name = HeliumLoggerPackageDescription;
			productName = HeliumLoggerPackageDescription;
			productType = "com.apple.product-type.framework";
		};
		"Kitura-Credentials::Credentials" /* Credentials */ = {
			isa = PBXNativeTarget;
			buildConfigurationList = OBJ_652 /* Build configuration list for PBXNativeTarget "Credentials" */;
			buildPhases = (
				OBJ_655 /* Sources */,
				OBJ_662 /* Frameworks */,
			);
			buildRules = (
			);
			dependencies = (
				OBJ_673 /* PBXTargetDependency */,
				OBJ_674 /* PBXTargetDependency */,
				OBJ_675 /* PBXTargetDependency */,
				OBJ_676 /* PBXTargetDependency */,
				OBJ_677 /* PBXTargetDependency */,
				OBJ_678 /* PBXTargetDependency */,
				OBJ_679 /* PBXTargetDependency */,
				OBJ_680 /* PBXTargetDependency */,
				OBJ_681 /* PBXTargetDependency */,
				OBJ_682 /* PBXTargetDependency */,
			);
			name = Credentials;
			productName = Credentials;
			productReference = "Kitura-Credentials::Credentials::Product" /* Credentials.framework */;
			productType = "com.apple.product-type.framework";
		};
		"Kitura-Credentials::SwiftPMPackageDescription" /* Kitura-CredentialsPackageDescription */ = {
			isa = PBXNativeTarget;
			buildConfigurationList = OBJ_385 /* Build configuration list for PBXNativeTarget "Kitura-CredentialsPackageDescription" */;
			buildPhases = (
				OBJ_388 /* Sources */,
			);
			buildRules = (
			);
			dependencies = (
			);
			name = "Kitura-CredentialsPackageDescription";
			productName = "Kitura-CredentialsPackageDescription";
			productType = "com.apple.product-type.framework";
		};
		"Kitura-CredentialsHTTP::CredentialsHTTP" /* CredentialsHTTP */ = {
			isa = PBXNativeTarget;
			buildConfigurationList = OBJ_621 /* Build configuration list for PBXNativeTarget "CredentialsHTTP" */;
			buildPhases = (
				OBJ_624 /* Sources */,
				OBJ_629 /* Frameworks */,
			);
			buildRules = (
			);
			dependencies = (
				OBJ_641 /* PBXTargetDependency */,
				OBJ_642 /* PBXTargetDependency */,
				OBJ_643 /* PBXTargetDependency */,
				OBJ_644 /* PBXTargetDependency */,
				OBJ_645 /* PBXTargetDependency */,
				OBJ_646 /* PBXTargetDependency */,
				OBJ_647 /* PBXTargetDependency */,
				OBJ_648 /* PBXTargetDependency */,
				OBJ_649 /* PBXTargetDependency */,
				OBJ_650 /* PBXTargetDependency */,
				OBJ_651 /* PBXTargetDependency */,
			);
			name = CredentialsHTTP;
			productName = CredentialsHTTP;
			productReference = "Kitura-CredentialsHTTP::CredentialsHTTP::Product" /* CredentialsHTTP.framework */;
			productType = "com.apple.product-type.framework";
		};
		"Kitura-CredentialsHTTP::SwiftPMPackageDescription" /* Kitura-CredentialsHTTPPackageDescription */ = {
			isa = PBXNativeTarget;
			buildConfigurationList = OBJ_379 /* Build configuration list for PBXNativeTarget "Kitura-CredentialsHTTPPackageDescription" */;
			buildPhases = (
				OBJ_382 /* Sources */,
			);
			buildRules = (
			);
			dependencies = (
			);
			name = "Kitura-CredentialsHTTPPackageDescription";
			productName = "Kitura-CredentialsHTTPPackageDescription";
			productType = "com.apple.product-type.framework";
		};
		"Kitura-Session::KituraSession" /* KituraSession */ = {
			isa = PBXNativeTarget;
			buildConfigurationList = OBJ_683 /* Build configuration list for PBXNativeTarget "KituraSession" */;
			buildPhases = (
				OBJ_686 /* Sources */,
				OBJ_695 /* Frameworks */,
			);
			buildRules = (
			);
			dependencies = (
				OBJ_705 /* PBXTargetDependency */,
				OBJ_706 /* PBXTargetDependency */,
				OBJ_707 /* PBXTargetDependency */,
				OBJ_708 /* PBXTargetDependency */,
				OBJ_709 /* PBXTargetDependency */,
				OBJ_710 /* PBXTargetDependency */,
				OBJ_711 /* PBXTargetDependency */,
				OBJ_712 /* PBXTargetDependency */,
				OBJ_713 /* PBXTargetDependency */,
			);
			name = KituraSession;
			productName = KituraSession;
			productReference = "Kitura-Session::KituraSession::Product" /* KituraSession.framework */;
			productType = "com.apple.product-type.framework";
		};
		"Kitura-Session::SwiftPMPackageDescription" /* Kitura-SessionPackageDescription */ = {
			isa = PBXNativeTarget;
			buildConfigurationList = OBJ_391 /* Build configuration list for PBXNativeTarget "Kitura-SessionPackageDescription" */;
			buildPhases = (
				OBJ_394 /* Sources */,
			);
			buildRules = (
			);
			dependencies = (
			);
			name = "Kitura-SessionPackageDescription";
			productName = "Kitura-SessionPackageDescription";
			productType = "com.apple.product-type.framework";
		};
		"Kitura-TemplateEngine::KituraTemplateEngine" /* KituraTemplateEngine */ = {
			isa = PBXNativeTarget;
			buildConfigurationList = OBJ_792 /* Build configuration list for PBXNativeTarget "KituraTemplateEngine" */;
			buildPhases = (
				OBJ_795 /* Sources */,
				OBJ_797 /* Frameworks */,
			);
			buildRules = (
			);
			dependencies = (
			);
			name = KituraTemplateEngine;
			productName = KituraTemplateEngine;
			productReference = "Kitura-TemplateEngine::KituraTemplateEngine::Product" /* KituraTemplateEngine.framework */;
			productType = "com.apple.product-type.framework";
		};
		"Kitura-TemplateEngine::SwiftPMPackageDescription" /* Kitura-TemplateEnginePackageDescription */ = {
			isa = PBXNativeTarget;
			buildConfigurationList = OBJ_409 /* Build configuration list for PBXNativeTarget "Kitura-TemplateEnginePackageDescription" */;
			buildPhases = (
				OBJ_412 /* Sources */,
			);
			buildRules = (
			);
			dependencies = (
			);
			name = "Kitura-TemplateEnginePackageDescription";
			productName = "Kitura-TemplateEnginePackageDescription";
			productType = "com.apple.product-type.framework";
		};
		"Kitura-net::CHTTPParser" /* CHTTPParser */ = {
			isa = PBXNativeTarget;
			buildConfigurationList = OBJ_862 /* Build configuration list for PBXNativeTarget "CHTTPParser" */;
			buildPhases = (
				OBJ_865 /* Sources */,
				OBJ_868 /* Frameworks */,
			);
			buildRules = (
			);
			dependencies = (
			);
			name = CHTTPParser;
			productName = CHTTPParser;
			productReference = "Kitura-net::CHTTPParser::Product" /* CHTTPParser.framework */;
			productType = "com.apple.product-type.framework";
		};
		"Kitura-net::KituraNet" /* KituraNet */ = {
			isa = PBXNativeTarget;
			buildConfigurationList = OBJ_805 /* Build configuration list for PBXNativeTarget "KituraNet" */;
			buildPhases = (
				OBJ_808 /* Sources */,
				OBJ_845 /* Frameworks */,
			);
			buildRules = (
			);
			dependencies = (
				OBJ_850 /* PBXTargetDependency */,
				OBJ_851 /* PBXTargetDependency */,
				OBJ_852 /* PBXTargetDependency */,
				OBJ_853 /* PBXTargetDependency */,
			);
			name = KituraNet;
			productName = KituraNet;
			productReference = "Kitura-net::KituraNet::Product" /* KituraNet.framework */;
			productType = "com.apple.product-type.framework";
		};
		"Kitura-net::SwiftPMPackageDescription" /* Kitura-netPackageDescription */ = {
			isa = PBXNativeTarget;
			buildConfigurationList = OBJ_421 /* Build configuration list for PBXNativeTarget "Kitura-netPackageDescription" */;
			buildPhases = (
				OBJ_424 /* Sources */,
			);
			buildRules = (
			);
			dependencies = (
			);
			name = "Kitura-netPackageDescription";
			productName = "Kitura-netPackageDescription";
			productType = "com.apple.product-type.framework";
		};
		"Kitura::Kitura" /* Kitura */ = {
			isa = PBXNativeTarget;
			buildConfigurationList = OBJ_729 /* Build configuration list for PBXNativeTarget "Kitura" */;
			buildPhases = (
				OBJ_732 /* Sources */,
				OBJ_777 /* Frameworks */,
			);
			buildRules = (
			);
			dependencies = (
				OBJ_785 /* PBXTargetDependency */,
				OBJ_786 /* PBXTargetDependency */,
				OBJ_787 /* PBXTargetDependency */,
				OBJ_788 /* PBXTargetDependency */,
				OBJ_789 /* PBXTargetDependency */,
				OBJ_790 /* PBXTargetDependency */,
				OBJ_791 /* PBXTargetDependency */,
			);
			name = Kitura;
			productName = Kitura;
			productReference = "Kitura::Kitura::Product" /* Kitura.framework */;
			productType = "com.apple.product-type.framework";
		};
		"Kitura::SwiftPMPackageDescription" /* KituraPackageDescription */ = {
			isa = PBXNativeTarget;
			buildConfigurationList = OBJ_403 /* Build configuration list for PBXNativeTarget "KituraPackageDescription" */;
			buildPhases = (
				OBJ_406 /* Sources */,
			);
			buildRules = (
			);
			dependencies = (
			);
			name = KituraPackageDescription;
			productName = KituraPackageDescription;
			productType = "com.apple.product-type.framework";
		};
		"KituraCORS::KituraCORS" /* KituraCORS */ = {
			isa = PBXNativeTarget;
			buildConfigurationList = OBJ_588 /* Build configuration list for PBXNativeTarget "KituraCORS" */;
			buildPhases = (
				OBJ_591 /* Sources */,
				OBJ_595 /* Frameworks */,
			);
			buildRules = (
			);
			dependencies = (
				OBJ_604 /* PBXTargetDependency */,
				OBJ_605 /* PBXTargetDependency */,
				OBJ_606 /* PBXTargetDependency */,
				OBJ_607 /* PBXTargetDependency */,
				OBJ_608 /* PBXTargetDependency */,
				OBJ_609 /* PBXTargetDependency */,
				OBJ_610 /* PBXTargetDependency */,
				OBJ_611 /* PBXTargetDependency */,
			);
			name = KituraCORS;
			productName = KituraCORS;
			productReference = "KituraCORS::KituraCORS::Product" /* KituraCORS.framework */;
			productType = "com.apple.product-type.framework";
		};
		"KituraCORS::SwiftPMPackageDescription" /* KituraCORSPackageDescription */ = {
			isa = PBXNativeTarget;
			buildConfigurationList = OBJ_367 /* Build configuration list for PBXNativeTarget "KituraCORSPackageDescription" */;
			buildPhases = (
				OBJ_370 /* Sources */,
			);
			buildRules = (
			);
			dependencies = (
			);
			name = KituraCORSPackageDescription;
			productName = KituraCORSPackageDescription;
			productType = "com.apple.product-type.framework";
		};
		"LoggerAPI::LoggerAPI" /* LoggerAPI */ = {
			isa = PBXNativeTarget;
			buildConfigurationList = OBJ_1031 /* Build configuration list for PBXNativeTarget "LoggerAPI" */;
			buildPhases = (
				OBJ_1034 /* Sources */,
				OBJ_1036 /* Frameworks */,
			);
			buildRules = (
			);
			dependencies = (
			);
			name = LoggerAPI;
			productName = LoggerAPI;
			productReference = "LoggerAPI::LoggerAPI::Product" /* LoggerAPI.framework */;
			productType = "com.apple.product-type.framework";
		};
		"LoggerAPI::SwiftPMPackageDescription" /* LoggerAPIPackageDescription */ = {
			isa = PBXNativeTarget;
			buildConfigurationList = OBJ_463 /* Build configuration list for PBXNativeTarget "LoggerAPIPackageDescription" */;
			buildPhases = (
				OBJ_466 /* Sources */,
			);
			buildRules = (
			);
			dependencies = (
			);
			name = LoggerAPIPackageDescription;
			productName = LoggerAPIPackageDescription;
			productType = "com.apple.product-type.framework";
		};
		"SSLService::SSLService" /* SSLService */ = {
			isa = PBXNativeTarget;
			buildConfigurationList = OBJ_854 /* Build configuration list for PBXNativeTarget "SSLService" */;
			buildPhases = (
				OBJ_857 /* Sources */,
				OBJ_859 /* Frameworks */,
			);
			buildRules = (
			);
			dependencies = (
				OBJ_861 /* PBXTargetDependency */,
			);
			name = SSLService;
			productName = SSLService;
			productReference = "SSLService::SSLService::Product" /* SSLService.framework */;
			productType = "com.apple.product-type.framework";
		};
		"SSLService::SwiftPMPackageDescription" /* SSLServicePackageDescription */ = {
			isa = PBXNativeTarget;
			buildConfigurationList = OBJ_427 /* Build configuration list for PBXNativeTarget "SSLServicePackageDescription" */;
			buildPhases = (
				OBJ_430 /* Sources */,
			);
			buildRules = (
			);
			dependencies = (
			);
			name = SSLServicePackageDescription;
			productName = SSLServicePackageDescription;
			productType = "com.apple.product-type.framework";
		};
		"Socket::Socket" /* Socket */ = {
			isa = PBXNativeTarget;
			buildConfigurationList = OBJ_1000 /* Build configuration list for PBXNativeTarget "Socket" */;
			buildPhases = (
				OBJ_1003 /* Sources */,
				OBJ_1007 /* Frameworks */,
			);
			buildRules = (
			);
			dependencies = (
			);
			name = Socket;
			productName = Socket;
			productReference = "Socket::Socket::Product" /* Socket.framework */;
			productType = "com.apple.product-type.framework";
		};
		"Socket::SwiftPMPackageDescription" /* SocketPackageDescription */ = {
			isa = PBXNativeTarget;
			buildConfigurationList = OBJ_451 /* Build configuration list for PBXNativeTarget "SocketPackageDescription" */;
			buildPhases = (
				OBJ_454 /* Sources */,
			);
			buildRules = (
			);
			dependencies = (
			);
			name = SocketPackageDescription;
			productName = SocketPackageDescription;
			productType = "com.apple.product-type.framework";
		};
		"SwiftKuery::SwiftKuery" /* SwiftKuery */ = {
			isa = PBXNativeTarget;
			buildConfigurationList = OBJ_880 /* Build configuration list for PBXNativeTarget "SwiftKuery" */;
			buildPhases = (
				OBJ_883 /* Sources */,
				OBJ_932 /* Frameworks */,
			);
			buildRules = (
			);
			dependencies = (
			);
			name = SwiftKuery;
			productName = SwiftKuery;
			productReference = "SwiftKuery::SwiftKuery::Product" /* SwiftKuery.framework */;
			productType = "com.apple.product-type.framework";
		};
		"SwiftKuery::SwiftPMPackageDescription" /* SwiftKueryPackageDescription */ = {
			isa = PBXNativeTarget;
			buildConfigurationList = OBJ_439 /* Build configuration list for PBXNativeTarget "SwiftKueryPackageDescription" */;
			buildPhases = (
				OBJ_442 /* Sources */,
			);
			buildRules = (
			);
			dependencies = (
			);
			name = SwiftKueryPackageDescription;
			productName = SwiftKueryPackageDescription;
			productType = "com.apple.product-type.framework";
		};
		"SwiftKueryMySQL::SwiftKueryMySQL" /* SwiftKueryMySQL */ = {
			isa = PBXNativeTarget;
			buildConfigurationList = OBJ_869 /* Build configuration list for PBXNativeTarget "SwiftKueryMySQL" */;
			buildPhases = (
				OBJ_872 /* Sources */,
				OBJ_877 /* Frameworks */,
			);
			buildRules = (
			);
			dependencies = (
				OBJ_879 /* PBXTargetDependency */,
			);
			name = SwiftKueryMySQL;
			productName = SwiftKueryMySQL;
			productReference = "SwiftKueryMySQL::SwiftKueryMySQL::Product" /* SwiftKueryMySQL.framework */;
			productType = "com.apple.product-type.framework";
		};
		"SwiftKueryMySQL::SwiftPMPackageDescription" /* SwiftKueryMySQLPackageDescription */ = {
			isa = PBXNativeTarget;
			buildConfigurationList = OBJ_433 /* Build configuration list for PBXNativeTarget "SwiftKueryMySQLPackageDescription" */;
			buildPhases = (
				OBJ_436 /* Sources */,
			);
			buildRules = (
			);
			dependencies = (
			);
			name = SwiftKueryMySQLPackageDescription;
			productName = SwiftKueryMySQLPackageDescription;
			productType = "com.apple.product-type.framework";
		};
		"SwiftyJSON::SwiftPMPackageDescription" /* SwiftyJSONPackageDescription */ = {
			isa = PBXNativeTarget;
			buildConfigurationList = OBJ_415 /* Build configuration list for PBXNativeTarget "SwiftyJSONPackageDescription" */;
			buildPhases = (
				OBJ_418 /* Sources */,
			);
			buildRules = (
			);
			dependencies = (
			);
			name = SwiftyJSONPackageDescription;
			productName = SwiftyJSONPackageDescription;
			productType = "com.apple.product-type.framework";
		};
		"SwiftyJSON::SwiftyJSON" /* SwiftyJSON */ = {
			isa = PBXNativeTarget;
			buildConfigurationList = OBJ_798 /* Build configuration list for PBXNativeTarget "SwiftyJSON" */;
			buildPhases = (
				OBJ_801 /* Sources */,
				OBJ_804 /* Frameworks */,
			);
			buildRules = (
			);
			dependencies = (
			);
			name = SwiftyJSON;
			productName = SwiftyJSON;
			productReference = "SwiftyJSON::SwiftyJSON::Product" /* SwiftyJSON.framework */;
			productType = "com.apple.product-type.framework";
		};
		"mikrotik_router_manager::CORE" /* CORE */ = {
			isa = PBXNativeTarget;
			buildConfigurationList = OBJ_534 /* Build configuration list for PBXNativeTarget "CORE" */;
			buildPhases = (
				OBJ_537 /* Sources */,
				OBJ_550 /* Frameworks */,
			);
			buildRules = (
			);
			dependencies = (
				OBJ_569 /* PBXTargetDependency */,
				OBJ_570 /* PBXTargetDependency */,
				OBJ_571 /* PBXTargetDependency */,
				OBJ_572 /* PBXTargetDependency */,
				OBJ_573 /* PBXTargetDependency */,
				OBJ_574 /* PBXTargetDependency */,
				OBJ_575 /* PBXTargetDependency */,
				OBJ_576 /* PBXTargetDependency */,
				OBJ_577 /* PBXTargetDependency */,
				OBJ_578 /* PBXTargetDependency */,
				OBJ_579 /* PBXTargetDependency */,
				OBJ_580 /* PBXTargetDependency */,
				OBJ_581 /* PBXTargetDependency */,
				OBJ_582 /* PBXTargetDependency */,
				OBJ_583 /* PBXTargetDependency */,
				OBJ_584 /* PBXTargetDependency */,
				OBJ_585 /* PBXTargetDependency */,
				OBJ_586 /* PBXTargetDependency */,
				OBJ_587 /* PBXTargetDependency */,
			);
			name = CORE;
			productName = CORE;
			productReference = "mikrotik_router_manager::CORE::Product" /* CORE.framework */;
			productType = "com.apple.product-type.framework";
		};
		"mikrotik_router_manager::SERVER" /* SERVER */ = {
			isa = PBXNativeTarget;
			buildConfigurationList = OBJ_469 /* Build configuration list for PBXNativeTarget "SERVER" */;
			buildPhases = (
				OBJ_472 /* Sources */,
				OBJ_474 /* Frameworks */,
			);
			buildRules = (
			);
			dependencies = (
				OBJ_494 /* PBXTargetDependency */,
				OBJ_496 /* PBXTargetDependency */,
				OBJ_498 /* PBXTargetDependency */,
				OBJ_500 /* PBXTargetDependency */,
				OBJ_502 /* PBXTargetDependency */,
				OBJ_504 /* PBXTargetDependency */,
				OBJ_506 /* PBXTargetDependency */,
				OBJ_508 /* PBXTargetDependency */,
				OBJ_510 /* PBXTargetDependency */,
				OBJ_512 /* PBXTargetDependency */,
				OBJ_514 /* PBXTargetDependency */,
				OBJ_516 /* PBXTargetDependency */,
				OBJ_518 /* PBXTargetDependency */,
				OBJ_520 /* PBXTargetDependency */,
				OBJ_522 /* PBXTargetDependency */,
				OBJ_524 /* PBXTargetDependency */,
				OBJ_526 /* PBXTargetDependency */,
				OBJ_528 /* PBXTargetDependency */,
				OBJ_530 /* PBXTargetDependency */,
				OBJ_532 /* PBXTargetDependency */,
			);
			name = SERVER;
			productName = SERVER;
			productReference = "mikrotik_router_manager::SERVER::Product" /* SERVER */;
			productType = "com.apple.product-type.tool";
		};
		"mikrotik_router_manager::SwiftPMPackageDescription" /* mikrotik_router_managerPackageDescription */ = {
			isa = PBXNativeTarget;
			buildConfigurationList = OBJ_361 /* Build configuration list for PBXNativeTarget "mikrotik_router_managerPackageDescription" */;
			buildPhases = (
				OBJ_364 /* Sources */,
			);
			buildRules = (
			);
			dependencies = (
			);
			name = mikrotik_router_managerPackageDescription;
			productName = mikrotik_router_managerPackageDescription;
			productType = "com.apple.product-type.framework";
		};
/* End PBXNativeTarget section */

/* Begin PBXProject section */
		OBJ_1 /* Project object */ = {
			isa = PBXProject;
			attributes = {
				LastUpgradeCheck = 9999;
			};
			buildConfigurationList = OBJ_2 /* Build configuration list for PBXProject "mikrotik_router_manager" */;
			compatibilityVersion = "Xcode 3.2";
			developmentRegion = English;
			hasScannedForEncodings = 0;
			knownRegions = (
				en,
			);
			mainGroup = OBJ_5 /*  */;
			productRefGroup = OBJ_338 /* Products */;
			projectDirPath = "";
			projectRoot = "";
			targets = (
				"mikrotik_router_manager::SwiftPMPackageDescription" /* mikrotik_router_managerPackageDescription */,
				"KituraCORS::SwiftPMPackageDescription" /* KituraCORSPackageDescription */,
				"HeliumLogger::SwiftPMPackageDescription" /* HeliumLoggerPackageDescription */,
				"Kitura-CredentialsHTTP::SwiftPMPackageDescription" /* Kitura-CredentialsHTTPPackageDescription */,
				"Kitura-Credentials::SwiftPMPackageDescription" /* Kitura-CredentialsPackageDescription */,
				"Kitura-Session::SwiftPMPackageDescription" /* Kitura-SessionPackageDescription */,
				"Cryptor::SwiftPMPackageDescription" /* CryptorPackageDescription */,
				"Kitura::SwiftPMPackageDescription" /* KituraPackageDescription */,
				"Kitura-TemplateEngine::SwiftPMPackageDescription" /* Kitura-TemplateEnginePackageDescription */,
				"SwiftyJSON::SwiftPMPackageDescription" /* SwiftyJSONPackageDescription */,
				"Kitura-net::SwiftPMPackageDescription" /* Kitura-netPackageDescription */,
				"SSLService::SwiftPMPackageDescription" /* SSLServicePackageDescription */,
				"SwiftKueryMySQL::SwiftPMPackageDescription" /* SwiftKueryMySQLPackageDescription */,
				"SwiftKuery::SwiftPMPackageDescription" /* SwiftKueryPackageDescription */,
				"CryptoSwift::SwiftPMPackageDescription" /* CryptoSwiftPackageDescription */,
				"Socket::SwiftPMPackageDescription" /* SocketPackageDescription */,
				"Configuration::SwiftPMPackageDescription" /* ConfigurationPackageDescription */,
				"LoggerAPI::SwiftPMPackageDescription" /* LoggerAPIPackageDescription */,
				"mikrotik_router_manager::SERVER" /* SERVER */,
				"mikrotik_router_manager::CORE" /* CORE */,
				"KituraCORS::KituraCORS" /* KituraCORS */,
				"HeliumLogger::HeliumLogger" /* HeliumLogger */,
				"Kitura-CredentialsHTTP::CredentialsHTTP" /* CredentialsHTTP */,
				"Kitura-Credentials::Credentials" /* Credentials */,
				"Kitura-Session::KituraSession" /* KituraSession */,
				"Cryptor::Cryptor" /* Cryptor */,
				"Kitura::Kitura" /* Kitura */,
				"Kitura-TemplateEngine::KituraTemplateEngine" /* KituraTemplateEngine */,
				"SwiftyJSON::SwiftyJSON" /* SwiftyJSON */,
				"Kitura-net::KituraNet" /* KituraNet */,
				"SSLService::SSLService" /* SSLService */,
				"Kitura-net::CHTTPParser" /* CHTTPParser */,
				"SwiftKueryMySQL::SwiftKueryMySQL" /* SwiftKueryMySQL */,
				"SwiftKuery::SwiftKuery" /* SwiftKuery */,
				"CryptoSwift::CryptoSwift" /* CryptoSwift */,
				"Socket::Socket" /* Socket */,
				"Configuration::ConfigurationTestExecutable" /* ConfigurationTestExecutable */,
				"Configuration::Configuration" /* Configuration */,
				"LoggerAPI::LoggerAPI" /* LoggerAPI */,
				"Kitura-CredentialsHTTP::Kitura-CredentialsHTTP::ProductTarget" /* Kitura-CredentialsHTTP */,
				"Kitura-Credentials::Kitura-Credentials::ProductTarget" /* Kitura-Credentials */,
				"Kitura-Session::Kitura-Session::ProductTarget" /* Kitura-Session */,
				"CommonCrypto::CommonCrypto::ProductTarget" /* CommonCrypto */,
				"CCurl::CCurl::ProductTarget" /* CCurl */,
				"CMySQL::CMySQL::ProductTarget" /* CMySQL */,
			);
		};
/* End PBXProject section */

/* Begin PBXSourcesBuildPhase section */
		OBJ_1003 /* Sources */ = {
			isa = PBXSourcesBuildPhase;
			buildActionMask = 0;
			files = (
				OBJ_1004 /* Socket.swift in Sources */,
				OBJ_1005 /* SocketProtocols.swift in Sources */,
				OBJ_1006 /* SocketUtils.swift in Sources */,
			);
			runOnlyForDeploymentPostprocessing = 0;
		};
		OBJ_1011 /* Sources */ = {
			isa = PBXSourcesBuildPhase;
			buildActionMask = 0;
			files = (
				OBJ_1012 /* main.swift in Sources */,
			);
			runOnlyForDeploymentPostprocessing = 0;
		};
		OBJ_1021 /* Sources */ = {
			isa = PBXSourcesBuildPhase;
			buildActionMask = 0;
			files = (
				OBJ_1022 /* ConfigurationManager.swift in Sources */,
				OBJ_1023 /* ConfigurationNode.swift in Sources */,
				OBJ_1024 /* Deserializer.swift in Sources */,
				OBJ_1025 /* JSONDeserializer.swift in Sources */,
				OBJ_1026 /* PLISTDeserializer.swift in Sources */,
				OBJ_1027 /* PathUtilities.swift in Sources */,
			);
			runOnlyForDeploymentPostprocessing = 0;
		};
		OBJ_1034 /* Sources */ = {
			isa = PBXSourcesBuildPhase;
			buildActionMask = 0;
			files = (
				OBJ_1035 /* Logger.swift in Sources */,
			);
			runOnlyForDeploymentPostprocessing = 0;
		};
		OBJ_364 /* Sources */ = {
			isa = PBXSourcesBuildPhase;
			buildActionMask = 0;
			files = (
				OBJ_365 /* Package.swift in Sources */,
			);
			runOnlyForDeploymentPostprocessing = 0;
		};
		OBJ_370 /* Sources */ = {
			isa = PBXSourcesBuildPhase;
			buildActionMask = 0;
			files = (
				OBJ_371 /* Package.swift in Sources */,
			);
			runOnlyForDeploymentPostprocessing = 0;
		};
		OBJ_376 /* Sources */ = {
			isa = PBXSourcesBuildPhase;
			buildActionMask = 0;
			files = (
				OBJ_377 /* Package.swift in Sources */,
			);
			runOnlyForDeploymentPostprocessing = 0;
		};
		OBJ_382 /* Sources */ = {
			isa = PBXSourcesBuildPhase;
			buildActionMask = 0;
			files = (
				OBJ_383 /* Package.swift in Sources */,
			);
			runOnlyForDeploymentPostprocessing = 0;
		};
		OBJ_388 /* Sources */ = {
			isa = PBXSourcesBuildPhase;
			buildActionMask = 0;
			files = (
				OBJ_389 /* Package.swift in Sources */,
			);
			runOnlyForDeploymentPostprocessing = 0;
		};
		OBJ_394 /* Sources */ = {
			isa = PBXSourcesBuildPhase;
			buildActionMask = 0;
			files = (
				OBJ_395 /* Package.swift in Sources */,
			);
			runOnlyForDeploymentPostprocessing = 0;
		};
		OBJ_400 /* Sources */ = {
			isa = PBXSourcesBuildPhase;
			buildActionMask = 0;
			files = (
				OBJ_401 /* Package.swift in Sources */,
			);
			runOnlyForDeploymentPostprocessing = 0;
		};
		OBJ_406 /* Sources */ = {
			isa = PBXSourcesBuildPhase;
			buildActionMask = 0;
			files = (
				OBJ_407 /* Package.swift in Sources */,
			);
			runOnlyForDeploymentPostprocessing = 0;
		};
		OBJ_412 /* Sources */ = {
			isa = PBXSourcesBuildPhase;
			buildActionMask = 0;
			files = (
				OBJ_413 /* Package.swift in Sources */,
			);
			runOnlyForDeploymentPostprocessing = 0;
		};
		OBJ_418 /* Sources */ = {
			isa = PBXSourcesBuildPhase;
			buildActionMask = 0;
			files = (
				OBJ_419 /* Package.swift in Sources */,
			);
			runOnlyForDeploymentPostprocessing = 0;
		};
		OBJ_424 /* Sources */ = {
			isa = PBXSourcesBuildPhase;
			buildActionMask = 0;
			files = (
				OBJ_425 /* Package.swift in Sources */,
			);
			runOnlyForDeploymentPostprocessing = 0;
		};
		OBJ_430 /* Sources */ = {
			isa = PBXSourcesBuildPhase;
			buildActionMask = 0;
			files = (
				OBJ_431 /* Package.swift in Sources */,
			);
			runOnlyForDeploymentPostprocessing = 0;
		};
		OBJ_436 /* Sources */ = {
			isa = PBXSourcesBuildPhase;
			buildActionMask = 0;
			files = (
				OBJ_437 /* Package.swift in Sources */,
			);
			runOnlyForDeploymentPostprocessing = 0;
		};
		OBJ_442 /* Sources */ = {
			isa = PBXSourcesBuildPhase;
			buildActionMask = 0;
			files = (
				OBJ_443 /* Package.swift in Sources */,
			);
			runOnlyForDeploymentPostprocessing = 0;
		};
		OBJ_448 /* Sources */ = {
			isa = PBXSourcesBuildPhase;
			buildActionMask = 0;
			files = (
				OBJ_449 /* Package.swift in Sources */,
			);
			runOnlyForDeploymentPostprocessing = 0;
		};
		OBJ_454 /* Sources */ = {
			isa = PBXSourcesBuildPhase;
			buildActionMask = 0;
			files = (
				OBJ_455 /* Package.swift in Sources */,
			);
			runOnlyForDeploymentPostprocessing = 0;
		};
		OBJ_460 /* Sources */ = {
			isa = PBXSourcesBuildPhase;
			buildActionMask = 0;
			files = (
				OBJ_461 /* Package.swift in Sources */,
			);
			runOnlyForDeploymentPostprocessing = 0;
		};
		OBJ_466 /* Sources */ = {
			isa = PBXSourcesBuildPhase;
			buildActionMask = 0;
			files = (
				OBJ_467 /* Package.swift in Sources */,
			);
			runOnlyForDeploymentPostprocessing = 0;
		};
		OBJ_472 /* Sources */ = {
			isa = PBXSourcesBuildPhase;
			buildActionMask = 0;
			files = (
				OBJ_473 /* main.swift in Sources */,
			);
			runOnlyForDeploymentPostprocessing = 0;
		};
		OBJ_537 /* Sources */ = {
			isa = PBXSourcesBuildPhase;
			buildActionMask = 0;
			files = (
				OBJ_538 /* BaseComponent.swift in Sources */,
				OBJ_539 /* Bitter.swift in Sources */,
				OBJ_540 /* Engine.swift in Sources */,
				OBJ_541 /* EngineConfig.swift in Sources */,
				OBJ_542 /* HttpCustomerLogin.swift in Sources */,
				OBJ_543 /* HttpServerComponent.swift in Sources */,
				OBJ_544 /* HttpUserAPI.swift in Sources */,
				OBJ_545 /* HtttpRouterAPI.swift in Sources */,
				OBJ_546 /* LogComponent.swift in Sources */,
				OBJ_547 /* MikrotikConnection.swift in Sources */,
				OBJ_548 /* MysqlConnection.swift in Sources */,
				OBJ_549 /* SessionManager.swift in Sources */,
			);
			runOnlyForDeploymentPostprocessing = 0;
		};
		OBJ_591 /* Sources */ = {
			isa = PBXSourcesBuildPhase;
			buildActionMask = 0;
			files = (
				OBJ_592 /* AllowedOrigins.swift in Sources */,
				OBJ_593 /* CORS.swift in Sources */,
				OBJ_594 /* Options.swift in Sources */,
			);
			runOnlyForDeploymentPostprocessing = 0;
		};
		OBJ_615 /* Sources */ = {
			isa = PBXSourcesBuildPhase;
			buildActionMask = 0;
			files = (
				OBJ_616 /* HeliumLogger.swift in Sources */,
				OBJ_617 /* HeliumStreamLogger.swift in Sources */,
			);
			runOnlyForDeploymentPostprocessing = 0;
		};
		OBJ_624 /* Sources */ = {
			isa = PBXSourcesBuildPhase;
			buildActionMask = 0;
			files = (
				OBJ_625 /* CredentialsHTTPBasic.swift in Sources */,
				OBJ_626 /* CredentialsHTTPDigest.swift in Sources */,
				OBJ_627 /* UserProfileLoader.swift in Sources */,
				OBJ_628 /* VerifyPassword.swift in Sources */,
			);
			runOnlyForDeploymentPostprocessing = 0;
		};
		OBJ_655 /* Sources */ = {
			isa = PBXSourcesBuildPhase;
			buildActionMask = 0;
			files = (
				OBJ_656 /* BaseCacheElement.swift in Sources */,
				OBJ_657 /* Credentials.swift in Sources */,
				OBJ_658 /* CredentialsPluginProtocol.swift in Sources */,
				OBJ_659 /* RouterRequest+UserProfile.swift in Sources */,
				OBJ_660 /* UserProfile.swift in Sources */,
				OBJ_661 /* UserProfileDelegate.swift in Sources */,
			);
			runOnlyForDeploymentPostprocessing = 0;
		};
		OBJ_686 /* Sources */ = {
			isa = PBXSourcesBuildPhase;
			buildActionMask = 0;
			files = (
				OBJ_687 /* CookieCryptography.swift in Sources */,
				OBJ_688 /* CookieManagement.swift in Sources */,
				OBJ_689 /* CookieParameter.swift in Sources */,
				OBJ_690 /* InMemoryStore.swift in Sources */,
				OBJ_691 /* RouterRequest+Session.swift in Sources */,
				OBJ_692 /* Session.swift in Sources */,
				OBJ_693 /* SessionState.swift in Sources */,
				OBJ_694 /* Store.swift in Sources */,
			);
			runOnlyForDeploymentPostprocessing = 0;
		};
		OBJ_717 /* Sources */ = {
			isa = PBXSourcesBuildPhase;
			buildActionMask = 0;
			files = (
				OBJ_718 /* Crypto.swift in Sources */,
				OBJ_719 /* Cryptor.swift in Sources */,
				OBJ_720 /* Digest.swift in Sources */,
				OBJ_721 /* HMAC.swift in Sources */,
				OBJ_722 /* KeyDerivation.swift in Sources */,
				OBJ_723 /* Random.swift in Sources */,
				OBJ_724 /* Status.swift in Sources */,
				OBJ_725 /* StreamCryptor.swift in Sources */,
				OBJ_726 /* Updatable.swift in Sources */,
				OBJ_727 /* Utilities.swift in Sources */,
			);
			runOnlyForDeploymentPostprocessing = 0;
		};
		OBJ_732 /* Sources */ = {
			isa = PBXSourcesBuildPhase;
			buildActionMask = 0;
			files = (
				OBJ_733 /* Error.swift in Sources */,
				OBJ_734 /* FileResourceServer.swift in Sources */,
				OBJ_735 /* HTTPVersion.swift in Sources */,
				OBJ_736 /* Headers.swift in Sources */,
				OBJ_737 /* InternalError.swift in Sources */,
				OBJ_738 /* JSONPError.swift in Sources */,
				OBJ_739 /* Kitura.swift in Sources */,
				OBJ_740 /* LinkParameter.swift in Sources */,
				OBJ_741 /* MimeTypeAcceptor.swift in Sources */,
				OBJ_742 /* RouteRegex.swift in Sources */,
				OBJ_743 /* Router.swift in Sources */,
				OBJ_744 /* RouterElement.swift in Sources */,
				OBJ_745 /* RouterElementWalker.swift in Sources */,
				OBJ_746 /* RouterHTTPVerbs+Error.swift in Sources */,
				OBJ_747 /* RouterHTTPVerbs_generated.swift in Sources */,
				OBJ_748 /* RouterHandler.swift in Sources */,
				OBJ_749 /* RouterMethod.swift in Sources */,
				OBJ_750 /* RouterMiddleware.swift in Sources */,
				OBJ_751 /* RouterMiddlewareGenerator.swift in Sources */,
				OBJ_752 /* RouterMiddlewareWalker.swift in Sources */,
				OBJ_753 /* RouterParameterWalker.swift in Sources */,
				OBJ_754 /* RouterRequest.swift in Sources */,
				OBJ_755 /* RouterResponse.swift in Sources */,
				OBJ_756 /* SSLConfig.swift in Sources */,
				OBJ_757 /* Stack.swift in Sources */,
				OBJ_758 /* String+Extensions.swift in Sources */,
				OBJ_759 /* TemplatingError.swift in Sources */,
				OBJ_760 /* BodyParser.swift in Sources */,
				OBJ_761 /* BodyParserProtocol.swift in Sources */,
				OBJ_762 /* JSONBodyParser.swift in Sources */,
				OBJ_763 /* MultiPartBodyParser.swift in Sources */,
				OBJ_764 /* ParsedBody.swift in Sources */,
				OBJ_765 /* Part.swift in Sources */,
				OBJ_766 /* RawBodyParser.swift in Sources */,
				OBJ_767 /* TextBodyParser.swift in Sources */,
				OBJ_768 /* URLEncodedBodyParser.swift in Sources */,
				OBJ_769 /* ContentType.swift in Sources */,
				OBJ_770 /* types.swift in Sources */,
				OBJ_771 /* CacheRelatedHeadersSetter.swift in Sources */,
				OBJ_772 /* CompositeHeadersSetter.swift in Sources */,
				OBJ_773 /* FileServer.swift in Sources */,
				OBJ_774 /* ResourcePathHandler.swift in Sources */,
				OBJ_775 /* ResponseHeadersSetter.swift in Sources */,
				OBJ_776 /* StaticFileServer.swift in Sources */,
			);
			runOnlyForDeploymentPostprocessing = 0;
		};
		OBJ_795 /* Sources */ = {
			isa = PBXSourcesBuildPhase;
			buildActionMask = 0;
			files = (
				OBJ_796 /* TemplateEngine.swift in Sources */,
			);
			runOnlyForDeploymentPostprocessing = 0;
		};
		OBJ_801 /* Sources */ = {
			isa = PBXSourcesBuildPhase;
			buildActionMask = 0;
			files = (
				OBJ_802 /* LclJSONSerialization.swift in Sources */,
				OBJ_803 /* SwiftyJSON.swift in Sources */,
			);
			runOnlyForDeploymentPostprocessing = 0;
		};
		OBJ_808 /* Sources */ = {
			isa = PBXSourcesBuildPhase;
			buildActionMask = 0;
			files = (
				OBJ_809 /* BufferList.swift in Sources */,
				OBJ_810 /* ClientRequest.swift in Sources */,
				OBJ_811 /* ClientResponse.swift in Sources */,
				OBJ_812 /* ConnectionUpgradeFactory.swift in Sources */,
				OBJ_813 /* ConnectionUpgrader.swift in Sources */,
				OBJ_814 /* Error.swift in Sources */,
				OBJ_815 /* FastCGI.swift in Sources */,
				OBJ_816 /* FastCGIRecordCreate.swift in Sources */,
				OBJ_817 /* FastCGIRecordParser.swift in Sources */,
				OBJ_818 /* FastCGIServer.swift in Sources */,
				OBJ_819 /* FastCGIServerRequest.swift in Sources */,
				OBJ_820 /* FastCGIServerResponse.swift in Sources */,
				OBJ_821 /* HTTP.swift in Sources */,
				OBJ_822 /* HTTPServer.swift in Sources */,
				OBJ_823 /* HTTPServerRequest.swift in Sources */,
				OBJ_824 /* HTTPServerResponse.swift in Sources */,
				OBJ_825 /* IncomingHTTPSocketProcessor.swift in Sources */,
				OBJ_826 /* KeepAliveState.swift in Sources */,
				OBJ_827 /* HTTPParser.swift in Sources */,
				OBJ_828 /* HTTPParserStatus.swift in Sources */,
				OBJ_829 /* ParseResults.swift in Sources */,
				OBJ_830 /* URLParser.swift in Sources */,
				OBJ_831 /* HeadersContainer.swift in Sources */,
				OBJ_832 /* IncomingSocketHandler.swift in Sources */,
				OBJ_833 /* IncomingSocketManager.swift in Sources */,
				OBJ_834 /* IncomingSocketProcessor.swift in Sources */,
				OBJ_835 /* IncomingSocketProcessorCreator.swift in Sources */,
				OBJ_836 /* ListenerGroup.swift in Sources */,
				OBJ_837 /* SPIUtils.swift in Sources */,
				OBJ_838 /* Server.swift in Sources */,
				OBJ_839 /* ServerDelegate.swift in Sources */,
				OBJ_840 /* ServerLifecycleListener.swift in Sources */,
				OBJ_841 /* ServerMonitor.swift in Sources */,
				OBJ_842 /* ServerState.swift in Sources */,
				OBJ_843 /* ServerRequest.swift in Sources */,
				OBJ_844 /* ServerResponse.swift in Sources */,
			);
			runOnlyForDeploymentPostprocessing = 0;
		};
		OBJ_857 /* Sources */ = {
			isa = PBXSourcesBuildPhase;
			buildActionMask = 0;
			files = (
				OBJ_858 /* SSLService.swift in Sources */,
			);
			runOnlyForDeploymentPostprocessing = 0;
		};
		OBJ_865 /* Sources */ = {
			isa = PBXSourcesBuildPhase;
			buildActionMask = 0;
			files = (
				OBJ_866 /* http_parser.c in Sources */,
				OBJ_867 /* utils.c in Sources */,
			);
			runOnlyForDeploymentPostprocessing = 0;
		};
		OBJ_872 /* Sources */ = {
			isa = PBXSourcesBuildPhase;
			buildActionMask = 0;
			files = (
				OBJ_873 /* MySQLConnection.swift in Sources */,
				OBJ_874 /* MySQLPreparedStatement.swift in Sources */,
				OBJ_875 /* MySQLResultFetcher.swift in Sources */,
				OBJ_876 /* MySQLThreadSafeConnection.swift in Sources */,
			);
			runOnlyForDeploymentPostprocessing = 0;
		};
		OBJ_883 /* Sources */ = {
			isa = PBXSourcesBuildPhase;
			buildActionMask = 0;
			files = (
				OBJ_884 /* AggregateColumnExpression.swift in Sources */,
				OBJ_885 /* AuxiliaryTable.swift in Sources */,
				OBJ_886 /* Buildable.swift in Sources */,
				OBJ_887 /* Column.swift in Sources */,
				OBJ_888 /* ColumnAndExpressions_Extensions.swift in Sources */,
				OBJ_889 /* Condition.swift in Sources */,
				OBJ_890 /* ConditionalClause.swift in Sources */,
				OBJ_891 /* Connection.swift in Sources */,
				OBJ_892 /* ConnectionPool.swift in Sources */,
				OBJ_893 /* ConnectionPoolConnection.swift in Sources */,
				OBJ_894 /* ConnectionPoolOptions.swift in Sources */,
				OBJ_895 /* Delete.swift in Sources */,
				OBJ_896 /* Field.swift in Sources */,
				OBJ_897 /* Filter.swift in Sources */,
				OBJ_898 /* FilterAndHaving_Extensions.swift in Sources */,
				OBJ_899 /* FilterAndHaving_GlobalFunctions.swift in Sources */,
				OBJ_900 /* Having.swift in Sources */,
				OBJ_901 /* Index.swift in Sources */,
				OBJ_902 /* IndexColumn.swift in Sources */,
				OBJ_903 /* IndexColumnOrdered.swift in Sources */,
				OBJ_904 /* Insert.swift in Sources */,
				OBJ_905 /* Join.swift in Sources */,
				OBJ_906 /* Migration.swift in Sources */,
				OBJ_907 /* OrderBy.swift in Sources */,
				OBJ_908 /* Parameter.swift in Sources */,
				OBJ_909 /* Predicate.swift in Sources */,
				OBJ_910 /* PreparedStatement.swift in Sources */,
				OBJ_911 /* Query.swift in Sources */,
				OBJ_912 /* QueryBuilder.swift in Sources */,
				OBJ_913 /* QueryError.swift in Sources */,
				OBJ_914 /* QueryResult.swift in Sources */,
				OBJ_915 /* QuerySuffixProtocol.swift in Sources */,
				OBJ_916 /* Raw.swift in Sources */,
				OBJ_917 /* RawField.swift in Sources */,
				OBJ_918 /* ResultFetcher.swift in Sources */,
				OBJ_919 /* ResultSet.swift in Sources */,
				OBJ_920 /* RowSequence.swift in Sources */,
				OBJ_921 /* SQLDataType.swift in Sources */,
				OBJ_922 /* ScalarColumnExpression.swift in Sources */,
				OBJ_923 /* Select.swift in Sources */,
				OBJ_924 /* SpecialOperators_Extensions.swift in Sources */,
				OBJ_925 /* String+Buildable.swift in Sources */,
				OBJ_926 /* Subqueries_GlobalFunctionsAndExtensions.swift in Sources */,
				OBJ_927 /* Table.swift in Sources */,
				OBJ_928 /* Union.swift in Sources */,
				OBJ_929 /* Update.swift in Sources */,
				OBJ_930 /* Utils.swift in Sources */,
				OBJ_931 /* With.swift in Sources */,
			);
			runOnlyForDeploymentPostprocessing = 0;
		};
		OBJ_936 /* Sources */ = {
			isa = PBXSourcesBuildPhase;
			buildActionMask = 0;
			files = (
				OBJ_937 /* AES.swift in Sources */,
				OBJ_938 /* Array+Extension.swift in Sources */,
				OBJ_939 /* Authenticator.swift in Sources */,
				OBJ_940 /* BatchedCollection.swift in Sources */,
				OBJ_941 /* Bit.swift in Sources */,
				OBJ_942 /* BlockCipher.swift in Sources */,
				OBJ_943 /* BlockMode.swift in Sources */,
				OBJ_944 /* BlockModeOptions.swift in Sources */,
				OBJ_945 /* BlockModeWorker.swift in Sources */,
				OBJ_946 /* CBC.swift in Sources */,
				OBJ_947 /* CFB.swift in Sources */,
				OBJ_948 /* CTR.swift in Sources */,
				OBJ_949 /* ECB.swift in Sources */,
				OBJ_950 /* OFB.swift in Sources */,
				OBJ_951 /* PCBC.swift in Sources */,
				OBJ_952 /* RandomAccessBlockModeWorker.swift in Sources */,
				OBJ_953 /* Blowfish.swift in Sources */,
				OBJ_954 /* CSArrayType+Extensions.swift in Sources */,
				OBJ_955 /* ChaCha20.swift in Sources */,
				OBJ_956 /* Checksum.swift in Sources */,
				OBJ_957 /* Cipher.swift in Sources */,
				OBJ_958 /* Collection+Extension.swift in Sources */,
				OBJ_959 /* Cryptors.swift in Sources */,
				OBJ_960 /* Digest.swift in Sources */,
				OBJ_961 /* DigestType.swift in Sources */,
				OBJ_962 /* AES+Foundation.swift in Sources */,
				OBJ_963 /* Blowfish+Foundation.swift in Sources */,
				OBJ_964 /* CSArrayType+Foundation.swift in Sources */,
				OBJ_965 /* ChaCha20+Foundation.swift in Sources */,
				OBJ_966 /* Data+Extension.swift in Sources */,
				OBJ_967 /* HMAC+Foundation.swift in Sources */,
				OBJ_968 /* Rabbit+Foundation.swift in Sources */,
				OBJ_969 /* String+FoundationExtension.swift in Sources */,
				OBJ_970 /* Utils+Foundation.swift in Sources */,
				OBJ_971 /* Generics.swift in Sources */,
				OBJ_972 /* HMAC.swift in Sources */,
				OBJ_973 /* Int+Extension.swift in Sources */,
				OBJ_974 /* MD5.swift in Sources */,
				OBJ_975 /* NoPadding.swift in Sources */,
				OBJ_976 /* Operators.swift in Sources */,
				OBJ_977 /* PBKDF1.swift in Sources */,
				OBJ_978 /* PBKDF2.swift in Sources */,
				OBJ_979 /* PKCS5.swift in Sources */,
				OBJ_980 /* PKCS7.swift in Sources */,
				OBJ_981 /* PKCS7Padding.swift in Sources */,
				OBJ_982 /* Padding.swift in Sources */,
				OBJ_983 /* Poly1305.swift in Sources */,
				OBJ_984 /* Rabbit.swift in Sources */,
				OBJ_985 /* RandomAccessCryptor.swift in Sources */,
				OBJ_986 /* RandomBytesSequence.swift in Sources */,
				OBJ_987 /* SHA1.swift in Sources */,
				OBJ_988 /* SHA2.swift in Sources */,
				OBJ_989 /* SHA3.swift in Sources */,
				OBJ_990 /* SecureBytes.swift in Sources */,
				OBJ_991 /* String+Extension.swift in Sources */,
				OBJ_992 /* UInt16+Extension.swift in Sources */,
				OBJ_993 /* UInt32+Extension.swift in Sources */,
				OBJ_994 /* UInt64+Extension.swift in Sources */,
				OBJ_995 /* UInt8+Extension.swift in Sources */,
				OBJ_996 /* Updatable.swift in Sources */,
				OBJ_997 /* Utils.swift in Sources */,
				OBJ_998 /* ZeroPadding.swift in Sources */,
			);
			runOnlyForDeploymentPostprocessing = 0;
		};
/* End PBXSourcesBuildPhase section */

/* Begin PBXTargetDependency section */
		OBJ_1016 /* PBXTargetDependency */ = {
			isa = PBXTargetDependency;
			target = "Configuration::Configuration" /* Configuration */;
			targetProxy = 99A5E5511F7943EB006A38C6 /* PBXContainerItemProxy */;
		};
		OBJ_1017 /* PBXTargetDependency */ = {
			isa = PBXTargetDependency;
			target = "LoggerAPI::LoggerAPI" /* LoggerAPI */;
			targetProxy = 99A5E5531F7943EB006A38C6 /* PBXContainerItemProxy */;
		};
		OBJ_1030 /* PBXTargetDependency */ = {
			isa = PBXTargetDependency;
			target = "LoggerAPI::LoggerAPI" /* LoggerAPI */;
			targetProxy = 99A5E5521F7943EB006A38C6 /* PBXContainerItemProxy */;
		};
		OBJ_1041 /* PBXTargetDependency */ = {
			isa = PBXTargetDependency;
			target = "Kitura-CredentialsHTTP::CredentialsHTTP" /* CredentialsHTTP */;
			targetProxy = 99A5E5691F7943EE006A38C6 /* PBXContainerItemProxy */;
		};
		OBJ_1046 /* PBXTargetDependency */ = {
			isa = PBXTargetDependency;
			target = "Kitura-Credentials::Credentials" /* Credentials */;
			targetProxy = 99A5E56A1F7943EE006A38C6 /* PBXContainerItemProxy */;
		};
		OBJ_1051 /* PBXTargetDependency */ = {
			isa = PBXTargetDependency;
			target = "Kitura-Session::KituraSession" /* KituraSession */;
			targetProxy = 99A5E56B1F7943EE006A38C6 /* PBXContainerItemProxy */;
		};
		OBJ_494 /* PBXTargetDependency */ = {
			isa = PBXTargetDependency;
			target = "mikrotik_router_manager::CORE" /* CORE */;
			targetProxy = 99A5E50B1F7943EB006A38C6 /* PBXContainerItemProxy */;
		};
		OBJ_496 /* PBXTargetDependency */ = {
			isa = PBXTargetDependency;
			target = "KituraCORS::KituraCORS" /* KituraCORS */;
			targetProxy = 99A5E5561F7943EB006A38C6 /* PBXContainerItemProxy */;
		};
		OBJ_498 /* PBXTargetDependency */ = {
			isa = PBXTargetDependency;
			target = "HeliumLogger::HeliumLogger" /* HeliumLogger */;
			targetProxy = 99A5E5571F7943EB006A38C6 /* PBXContainerItemProxy */;
		};
		OBJ_500 /* PBXTargetDependency */ = {
			isa = PBXTargetDependency;
			target = "Kitura-CredentialsHTTP::CredentialsHTTP" /* CredentialsHTTP */;
			targetProxy = 99A5E5581F7943EB006A38C6 /* PBXContainerItemProxy */;
		};
		OBJ_502 /* PBXTargetDependency */ = {
			isa = PBXTargetDependency;
			target = "Kitura-Credentials::Credentials" /* Credentials */;
			targetProxy = 99A5E5591F7943EB006A38C6 /* PBXContainerItemProxy */;
		};
		OBJ_504 /* PBXTargetDependency */ = {
			isa = PBXTargetDependency;
			target = "Kitura-Session::KituraSession" /* KituraSession */;
			targetProxy = 99A5E55A1F7943EB006A38C6 /* PBXContainerItemProxy */;
		};
		OBJ_506 /* PBXTargetDependency */ = {
			isa = PBXTargetDependency;
			target = "Cryptor::Cryptor" /* Cryptor */;
			targetProxy = 99A5E55B1F7943EB006A38C6 /* PBXContainerItemProxy */;
		};
		OBJ_508 /* PBXTargetDependency */ = {
			isa = PBXTargetDependency;
			target = "Kitura::Kitura" /* Kitura */;
			targetProxy = 99A5E55C1F7943EB006A38C6 /* PBXContainerItemProxy */;
		};
		OBJ_510 /* PBXTargetDependency */ = {
			isa = PBXTargetDependency;
			target = "Kitura-TemplateEngine::KituraTemplateEngine" /* KituraTemplateEngine */;
			targetProxy = 99A5E55D1F7943EB006A38C6 /* PBXContainerItemProxy */;
		};
		OBJ_512 /* PBXTargetDependency */ = {
			isa = PBXTargetDependency;
			target = "SwiftyJSON::SwiftyJSON" /* SwiftyJSON */;
			targetProxy = 99A5E55E1F7943EB006A38C6 /* PBXContainerItemProxy */;
		};
		OBJ_514 /* PBXTargetDependency */ = {
			isa = PBXTargetDependency;
			target = "Kitura-net::KituraNet" /* KituraNet */;
			targetProxy = 99A5E55F1F7943EB006A38C6 /* PBXContainerItemProxy */;
		};
		OBJ_516 /* PBXTargetDependency */ = {
			isa = PBXTargetDependency;
			target = "SSLService::SSLService" /* SSLService */;
			targetProxy = 99A5E5601F7943EB006A38C6 /* PBXContainerItemProxy */;
		};
		OBJ_518 /* PBXTargetDependency */ = {
			isa = PBXTargetDependency;
			target = "Kitura-net::CHTTPParser" /* CHTTPParser */;
			targetProxy = 99A5E5611F7943EB006A38C6 /* PBXContainerItemProxy */;
		};
		OBJ_520 /* PBXTargetDependency */ = {
			isa = PBXTargetDependency;
			target = "SwiftKueryMySQL::SwiftKueryMySQL" /* SwiftKueryMySQL */;
			targetProxy = 99A5E5621F7943EB006A38C6 /* PBXContainerItemProxy */;
		};
		OBJ_522 /* PBXTargetDependency */ = {
			isa = PBXTargetDependency;
			target = "SwiftKuery::SwiftKuery" /* SwiftKuery */;
			targetProxy = 99A5E5631F7943EB006A38C6 /* PBXContainerItemProxy */;
		};
		OBJ_524 /* PBXTargetDependency */ = {
			isa = PBXTargetDependency;
			target = "CryptoSwift::CryptoSwift" /* CryptoSwift */;
			targetProxy = 99A5E5641F7943EB006A38C6 /* PBXContainerItemProxy */;
		};
		OBJ_526 /* PBXTargetDependency */ = {
			isa = PBXTargetDependency;
			target = "Socket::Socket" /* Socket */;
			targetProxy = 99A5E5651F7943EB006A38C6 /* PBXContainerItemProxy */;
		};
		OBJ_528 /* PBXTargetDependency */ = {
			isa = PBXTargetDependency;
			target = "Configuration::ConfigurationTestExecutable" /* ConfigurationTestExecutable */;
			targetProxy = 99A5E5661F7943EB006A38C6 /* PBXContainerItemProxy */;
		};
		OBJ_530 /* PBXTargetDependency */ = {
			isa = PBXTargetDependency;
			target = "Configuration::Configuration" /* Configuration */;
			targetProxy = 99A5E5671F7943EB006A38C6 /* PBXContainerItemProxy */;
		};
		OBJ_532 /* PBXTargetDependency */ = {
			isa = PBXTargetDependency;
			target = "LoggerAPI::LoggerAPI" /* LoggerAPI */;
			targetProxy = 99A5E5681F7943EB006A38C6 /* PBXContainerItemProxy */;
		};
		OBJ_569 /* PBXTargetDependency */ = {
			isa = PBXTargetDependency;
			target = "KituraCORS::KituraCORS" /* KituraCORS */;
			targetProxy = 99A5E50C1F7943EB006A38C6 /* PBXContainerItemProxy */;
		};
		OBJ_570 /* PBXTargetDependency */ = {
			isa = PBXTargetDependency;
			target = "HeliumLogger::HeliumLogger" /* HeliumLogger */;
			targetProxy = 99A5E5211F7943EB006A38C6 /* PBXContainerItemProxy */;
		};
		OBJ_571 /* PBXTargetDependency */ = {
			isa = PBXTargetDependency;
			target = "Kitura-CredentialsHTTP::CredentialsHTTP" /* CredentialsHTTP */;
			targetProxy = 99A5E5231F7943EB006A38C6 /* PBXContainerItemProxy */;
		};
		OBJ_572 /* PBXTargetDependency */ = {
			isa = PBXTargetDependency;
			target = "Kitura-Credentials::Credentials" /* Credentials */;
			targetProxy = 99A5E5421F7943EB006A38C6 /* PBXContainerItemProxy */;
		};
		OBJ_573 /* PBXTargetDependency */ = {
			isa = PBXTargetDependency;
			target = "Kitura-Session::KituraSession" /* KituraSession */;
			targetProxy = 99A5E5431F7943EB006A38C6 /* PBXContainerItemProxy */;
		};
		OBJ_574 /* PBXTargetDependency */ = {
			isa = PBXTargetDependency;
			target = "Cryptor::Cryptor" /* Cryptor */;
			targetProxy = 99A5E5441F7943EB006A38C6 /* PBXContainerItemProxy */;
		};
		OBJ_575 /* PBXTargetDependency */ = {
			isa = PBXTargetDependency;
			target = "Kitura::Kitura" /* Kitura */;
			targetProxy = 99A5E5451F7943EB006A38C6 /* PBXContainerItemProxy */;
		};
		OBJ_576 /* PBXTargetDependency */ = {
			isa = PBXTargetDependency;
			target = "Kitura-TemplateEngine::KituraTemplateEngine" /* KituraTemplateEngine */;
			targetProxy = 99A5E5461F7943EB006A38C6 /* PBXContainerItemProxy */;
		};
		OBJ_577 /* PBXTargetDependency */ = {
			isa = PBXTargetDependency;
			target = "SwiftyJSON::SwiftyJSON" /* SwiftyJSON */;
			targetProxy = 99A5E5471F7943EB006A38C6 /* PBXContainerItemProxy */;
		};
		OBJ_578 /* PBXTargetDependency */ = {
			isa = PBXTargetDependency;
			target = "Kitura-net::KituraNet" /* KituraNet */;
			targetProxy = 99A5E5481F7943EB006A38C6 /* PBXContainerItemProxy */;
		};
		OBJ_579 /* PBXTargetDependency */ = {
			isa = PBXTargetDependency;
			target = "SSLService::SSLService" /* SSLService */;
			targetProxy = 99A5E5491F7943EB006A38C6 /* PBXContainerItemProxy */;
		};
		OBJ_580 /* PBXTargetDependency */ = {
			isa = PBXTargetDependency;
			target = "Kitura-net::CHTTPParser" /* CHTTPParser */;
			targetProxy = 99A5E54A1F7943EB006A38C6 /* PBXContainerItemProxy */;
		};
		OBJ_581 /* PBXTargetDependency */ = {
			isa = PBXTargetDependency;
			target = "SwiftKueryMySQL::SwiftKueryMySQL" /* SwiftKueryMySQL */;
			targetProxy = 99A5E54B1F7943EB006A38C6 /* PBXContainerItemProxy */;
		};
		OBJ_582 /* PBXTargetDependency */ = {
			isa = PBXTargetDependency;
			target = "SwiftKuery::SwiftKuery" /* SwiftKuery */;
			targetProxy = 99A5E54D1F7943EB006A38C6 /* PBXContainerItemProxy */;
		};
		OBJ_583 /* PBXTargetDependency */ = {
			isa = PBXTargetDependency;
			target = "CryptoSwift::CryptoSwift" /* CryptoSwift */;
			targetProxy = 99A5E54E1F7943EB006A38C6 /* PBXContainerItemProxy */;
		};
		OBJ_584 /* PBXTargetDependency */ = {
			isa = PBXTargetDependency;
			target = "Socket::Socket" /* Socket */;
			targetProxy = 99A5E54F1F7943EB006A38C6 /* PBXContainerItemProxy */;
		};
		OBJ_585 /* PBXTargetDependency */ = {
			isa = PBXTargetDependency;
			target = "Configuration::ConfigurationTestExecutable" /* ConfigurationTestExecutable */;
			targetProxy = 99A5E5501F7943EB006A38C6 /* PBXContainerItemProxy */;
		};
		OBJ_586 /* PBXTargetDependency */ = {
			isa = PBXTargetDependency;
			target = "Configuration::Configuration" /* Configuration */;
			targetProxy = 99A5E5541F7943EB006A38C6 /* PBXContainerItemProxy */;
		};
		OBJ_587 /* PBXTargetDependency */ = {
			isa = PBXTargetDependency;
			target = "LoggerAPI::LoggerAPI" /* LoggerAPI */;
			targetProxy = 99A5E5551F7943EB006A38C6 /* PBXContainerItemProxy */;
		};
		OBJ_604 /* PBXTargetDependency */ = {
			isa = PBXTargetDependency;
			target = "Kitura::Kitura" /* Kitura */;
			targetProxy = 99A5E50D1F7943EB006A38C6 /* PBXContainerItemProxy */;
		};
		OBJ_605 /* PBXTargetDependency */ = {
			isa = PBXTargetDependency;
			target = "Kitura-TemplateEngine::KituraTemplateEngine" /* KituraTemplateEngine */;
			targetProxy = 99A5E51A1F7943EB006A38C6 /* PBXContainerItemProxy */;
		};
		OBJ_606 /* PBXTargetDependency */ = {
			isa = PBXTargetDependency;
			target = "SwiftyJSON::SwiftyJSON" /* SwiftyJSON */;
			targetProxy = 99A5E51B1F7943EB006A38C6 /* PBXContainerItemProxy */;
		};
		OBJ_607 /* PBXTargetDependency */ = {
			isa = PBXTargetDependency;
			target = "Kitura-net::KituraNet" /* KituraNet */;
			targetProxy = 99A5E51C1F7943EB006A38C6 /* PBXContainerItemProxy */;
		};
		OBJ_608 /* PBXTargetDependency */ = {
			isa = PBXTargetDependency;
			target = "SSLService::SSLService" /* SSLService */;
			targetProxy = 99A5E51D1F7943EB006A38C6 /* PBXContainerItemProxy */;
		};
		OBJ_609 /* PBXTargetDependency */ = {
			isa = PBXTargetDependency;
			target = "Socket::Socket" /* Socket */;
			targetProxy = 99A5E51E1F7943EB006A38C6 /* PBXContainerItemProxy */;
		};
		OBJ_610 /* PBXTargetDependency */ = {
			isa = PBXTargetDependency;
			target = "LoggerAPI::LoggerAPI" /* LoggerAPI */;
			targetProxy = 99A5E51F1F7943EB006A38C6 /* PBXContainerItemProxy */;
		};
		OBJ_611 /* PBXTargetDependency */ = {
			isa = PBXTargetDependency;
			target = "Kitura-net::CHTTPParser" /* CHTTPParser */;
			targetProxy = 99A5E5201F7943EB006A38C6 /* PBXContainerItemProxy */;
		};
		OBJ_620 /* PBXTargetDependency */ = {
			isa = PBXTargetDependency;
			target = "LoggerAPI::LoggerAPI" /* LoggerAPI */;
			targetProxy = 99A5E5221F7943EB006A38C6 /* PBXContainerItemProxy */;
		};
		OBJ_641 /* PBXTargetDependency */ = {
			isa = PBXTargetDependency;
			target = "Kitura-Credentials::Credentials" /* Credentials */;
			targetProxy = 99A5E5241F7943EB006A38C6 /* PBXContainerItemProxy */;
		};
		OBJ_642 /* PBXTargetDependency */ = {
			isa = PBXTargetDependency;
			target = "Kitura-Session::KituraSession" /* KituraSession */;
			targetProxy = 99A5E5381F7943EB006A38C6 /* PBXContainerItemProxy */;
		};
		OBJ_643 /* PBXTargetDependency */ = {
			isa = PBXTargetDependency;
			target = "Cryptor::Cryptor" /* Cryptor */;
			targetProxy = 99A5E5391F7943EB006A38C6 /* PBXContainerItemProxy */;
		};
		OBJ_644 /* PBXTargetDependency */ = {
			isa = PBXTargetDependency;
			target = "Kitura::Kitura" /* Kitura */;
			targetProxy = 99A5E53A1F7943EB006A38C6 /* PBXContainerItemProxy */;
		};
		OBJ_645 /* PBXTargetDependency */ = {
			isa = PBXTargetDependency;
			target = "Kitura-TemplateEngine::KituraTemplateEngine" /* KituraTemplateEngine */;
			targetProxy = 99A5E53B1F7943EB006A38C6 /* PBXContainerItemProxy */;
		};
		OBJ_646 /* PBXTargetDependency */ = {
			isa = PBXTargetDependency;
			target = "SwiftyJSON::SwiftyJSON" /* SwiftyJSON */;
			targetProxy = 99A5E53C1F7943EB006A38C6 /* PBXContainerItemProxy */;
		};
		OBJ_647 /* PBXTargetDependency */ = {
			isa = PBXTargetDependency;
			target = "Kitura-net::KituraNet" /* KituraNet */;
			targetProxy = 99A5E53D1F7943EB006A38C6 /* PBXContainerItemProxy */;
		};
		OBJ_648 /* PBXTargetDependency */ = {
			isa = PBXTargetDependency;
			target = "SSLService::SSLService" /* SSLService */;
			targetProxy = 99A5E53E1F7943EB006A38C6 /* PBXContainerItemProxy */;
		};
		OBJ_649 /* PBXTargetDependency */ = {
			isa = PBXTargetDependency;
			target = "Socket::Socket" /* Socket */;
			targetProxy = 99A5E53F1F7943EB006A38C6 /* PBXContainerItemProxy */;
		};
		OBJ_650 /* PBXTargetDependency */ = {
			isa = PBXTargetDependency;
			target = "LoggerAPI::LoggerAPI" /* LoggerAPI */;
			targetProxy = 99A5E5401F7943EB006A38C6 /* PBXContainerItemProxy */;
		};
		OBJ_651 /* PBXTargetDependency */ = {
			isa = PBXTargetDependency;
			target = "Kitura-net::CHTTPParser" /* CHTTPParser */;
			targetProxy = 99A5E5411F7943EB006A38C6 /* PBXContainerItemProxy */;
		};
		OBJ_673 /* PBXTargetDependency */ = {
			isa = PBXTargetDependency;
			target = "Kitura-Session::KituraSession" /* KituraSession */;
			targetProxy = 99A5E5251F7943EB006A38C6 /* PBXContainerItemProxy */;
		};
		OBJ_674 /* PBXTargetDependency */ = {
			isa = PBXTargetDependency;
			target = "Cryptor::Cryptor" /* Cryptor */;
			targetProxy = 99A5E52F1F7943EB006A38C6 /* PBXContainerItemProxy */;
		};
		OBJ_675 /* PBXTargetDependency */ = {
			isa = PBXTargetDependency;
			target = "Kitura::Kitura" /* Kitura */;
			targetProxy = 99A5E5301F7943EB006A38C6 /* PBXContainerItemProxy */;
		};
		OBJ_676 /* PBXTargetDependency */ = {
			isa = PBXTargetDependency;
			target = "Kitura-TemplateEngine::KituraTemplateEngine" /* KituraTemplateEngine */;
			targetProxy = 99A5E5311F7943EB006A38C6 /* PBXContainerItemProxy */;
		};
		OBJ_677 /* PBXTargetDependency */ = {
			isa = PBXTargetDependency;
			target = "SwiftyJSON::SwiftyJSON" /* SwiftyJSON */;
			targetProxy = 99A5E5321F7943EB006A38C6 /* PBXContainerItemProxy */;
		};
		OBJ_678 /* PBXTargetDependency */ = {
			isa = PBXTargetDependency;
			target = "Kitura-net::KituraNet" /* KituraNet */;
			targetProxy = 99A5E5331F7943EB006A38C6 /* PBXContainerItemProxy */;
		};
		OBJ_679 /* PBXTargetDependency */ = {
			isa = PBXTargetDependency;
			target = "SSLService::SSLService" /* SSLService */;
			targetProxy = 99A5E5341F7943EB006A38C6 /* PBXContainerItemProxy */;
		};
		OBJ_680 /* PBXTargetDependency */ = {
			isa = PBXTargetDependency;
			target = "Socket::Socket" /* Socket */;
			targetProxy = 99A5E5351F7943EB006A38C6 /* PBXContainerItemProxy */;
		};
		OBJ_681 /* PBXTargetDependency */ = {
			isa = PBXTargetDependency;
			target = "LoggerAPI::LoggerAPI" /* LoggerAPI */;
			targetProxy = 99A5E5361F7943EB006A38C6 /* PBXContainerItemProxy */;
		};
		OBJ_682 /* PBXTargetDependency */ = {
			isa = PBXTargetDependency;
			target = "Kitura-net::CHTTPParser" /* CHTTPParser */;
			targetProxy = 99A5E5371F7943EB006A38C6 /* PBXContainerItemProxy */;
		};
		OBJ_705 /* PBXTargetDependency */ = {
			isa = PBXTargetDependency;
			target = "Cryptor::Cryptor" /* Cryptor */;
			targetProxy = 99A5E5261F7943EB006A38C6 /* PBXContainerItemProxy */;
		};
		OBJ_706 /* PBXTargetDependency */ = {
			isa = PBXTargetDependency;
			target = "Kitura::Kitura" /* Kitura */;
			targetProxy = 99A5E5271F7943EB006A38C6 /* PBXContainerItemProxy */;
		};
		OBJ_707 /* PBXTargetDependency */ = {
			isa = PBXTargetDependency;
			target = "Kitura-TemplateEngine::KituraTemplateEngine" /* KituraTemplateEngine */;
			targetProxy = 99A5E5281F7943EB006A38C6 /* PBXContainerItemProxy */;
		};
		OBJ_708 /* PBXTargetDependency */ = {
			isa = PBXTargetDependency;
			target = "SwiftyJSON::SwiftyJSON" /* SwiftyJSON */;
			targetProxy = 99A5E5291F7943EB006A38C6 /* PBXContainerItemProxy */;
		};
		OBJ_709 /* PBXTargetDependency */ = {
			isa = PBXTargetDependency;
			target = "Kitura-net::KituraNet" /* KituraNet */;
			targetProxy = 99A5E52A1F7943EB006A38C6 /* PBXContainerItemProxy */;
		};
		OBJ_710 /* PBXTargetDependency */ = {
			isa = PBXTargetDependency;
			target = "SSLService::SSLService" /* SSLService */;
			targetProxy = 99A5E52B1F7943EB006A38C6 /* PBXContainerItemProxy */;
		};
		OBJ_711 /* PBXTargetDependency */ = {
			isa = PBXTargetDependency;
			target = "Socket::Socket" /* Socket */;
			targetProxy = 99A5E52C1F7943EB006A38C6 /* PBXContainerItemProxy */;
		};
		OBJ_712 /* PBXTargetDependency */ = {
			isa = PBXTargetDependency;
			target = "LoggerAPI::LoggerAPI" /* LoggerAPI */;
			targetProxy = 99A5E52D1F7943EB006A38C6 /* PBXContainerItemProxy */;
		};
		OBJ_713 /* PBXTargetDependency */ = {
			isa = PBXTargetDependency;
			target = "Kitura-net::CHTTPParser" /* CHTTPParser */;
			targetProxy = 99A5E52E1F7943EB006A38C6 /* PBXContainerItemProxy */;
		};
		OBJ_785 /* PBXTargetDependency */ = {
			isa = PBXTargetDependency;
			target = "Kitura-TemplateEngine::KituraTemplateEngine" /* KituraTemplateEngine */;
			targetProxy = 99A5E50E1F7943EB006A38C6 /* PBXContainerItemProxy */;
		};
		OBJ_786 /* PBXTargetDependency */ = {
			isa = PBXTargetDependency;
			target = "SwiftyJSON::SwiftyJSON" /* SwiftyJSON */;
			targetProxy = 99A5E50F1F7943EB006A38C6 /* PBXContainerItemProxy */;
		};
		OBJ_787 /* PBXTargetDependency */ = {
			isa = PBXTargetDependency;
			target = "Kitura-net::KituraNet" /* KituraNet */;
			targetProxy = 99A5E5101F7943EB006A38C6 /* PBXContainerItemProxy */;
		};
		OBJ_788 /* PBXTargetDependency */ = {
			isa = PBXTargetDependency;
			target = "SSLService::SSLService" /* SSLService */;
			targetProxy = 99A5E5161F7943EB006A38C6 /* PBXContainerItemProxy */;
		};
		OBJ_789 /* PBXTargetDependency */ = {
			isa = PBXTargetDependency;
			target = "Socket::Socket" /* Socket */;
			targetProxy = 99A5E5171F7943EB006A38C6 /* PBXContainerItemProxy */;
		};
		OBJ_790 /* PBXTargetDependency */ = {
			isa = PBXTargetDependency;
			target = "LoggerAPI::LoggerAPI" /* LoggerAPI */;
			targetProxy = 99A5E5181F7943EB006A38C6 /* PBXContainerItemProxy */;
		};
		OBJ_791 /* PBXTargetDependency */ = {
			isa = PBXTargetDependency;
			target = "Kitura-net::CHTTPParser" /* CHTTPParser */;
			targetProxy = 99A5E5191F7943EB006A38C6 /* PBXContainerItemProxy */;
		};
		OBJ_850 /* PBXTargetDependency */ = {
			isa = PBXTargetDependency;
			target = "SSLService::SSLService" /* SSLService */;
			targetProxy = 99A5E5111F7943EB006A38C6 /* PBXContainerItemProxy */;
		};
		OBJ_851 /* PBXTargetDependency */ = {
			isa = PBXTargetDependency;
			target = "Socket::Socket" /* Socket */;
			targetProxy = 99A5E5131F7943EB006A38C6 /* PBXContainerItemProxy */;
		};
		OBJ_852 /* PBXTargetDependency */ = {
			isa = PBXTargetDependency;
			target = "LoggerAPI::LoggerAPI" /* LoggerAPI */;
			targetProxy = 99A5E5141F7943EB006A38C6 /* PBXContainerItemProxy */;
		};
		OBJ_853 /* PBXTargetDependency */ = {
			isa = PBXTargetDependency;
			target = "Kitura-net::CHTTPParser" /* CHTTPParser */;
			targetProxy = 99A5E5151F7943EB006A38C6 /* PBXContainerItemProxy */;
		};
		OBJ_861 /* PBXTargetDependency */ = {
			isa = PBXTargetDependency;
			target = "Socket::Socket" /* Socket */;
			targetProxy = 99A5E5121F7943EB006A38C6 /* PBXContainerItemProxy */;
		};
		OBJ_879 /* PBXTargetDependency */ = {
			isa = PBXTargetDependency;
			target = "SwiftKuery::SwiftKuery" /* SwiftKuery */;
			targetProxy = 99A5E54C1F7943EB006A38C6 /* PBXContainerItemProxy */;
		};
/* End PBXTargetDependency section */

/* Begin XCBuildConfiguration section */
		OBJ_1001 /* Debug */ = {
			isa = XCBuildConfiguration;
			buildSettings = {
				ENABLE_TESTABILITY = YES;
				FRAMEWORK_SEARCH_PATHS = (
					"$(inherited)",
					"$(PLATFORM_DIR)/Developer/Library/Frameworks",
				);
				HEADER_SEARCH_PATHS = "$(inherited)";
				INFOPLIST_FILE = mikrotik_router_manager.xcodeproj/Socket_Info.plist;
				LD_RUNPATH_SEARCH_PATHS = "$(TOOLCHAIN_DIR)/usr/lib/swift/macosx";
				OTHER_LDFLAGS = "$(inherited)";
				OTHER_SWIFT_FLAGS = "$(inherited)";
				PRODUCT_BUNDLE_IDENTIFIER = Socket;
				PRODUCT_MODULE_NAME = "$(TARGET_NAME:c99extidentifier)";
				PRODUCT_NAME = "$(TARGET_NAME:c99extidentifier)";
				SKIP_INSTALL = YES;
				SWIFT_VERSION = 3.0;
				TARGET_NAME = Socket;
			};
			name = Debug;
		};
		OBJ_1002 /* Release */ = {
			isa = XCBuildConfiguration;
			buildSettings = {
				ENABLE_TESTABILITY = YES;
				FRAMEWORK_SEARCH_PATHS = (
					"$(inherited)",
					"$(PLATFORM_DIR)/Developer/Library/Frameworks",
				);
				HEADER_SEARCH_PATHS = "$(inherited)";
				INFOPLIST_FILE = mikrotik_router_manager.xcodeproj/Socket_Info.plist;
				LD_RUNPATH_SEARCH_PATHS = "$(TOOLCHAIN_DIR)/usr/lib/swift/macosx";
				OTHER_LDFLAGS = "$(inherited)";
				OTHER_SWIFT_FLAGS = "$(inherited)";
				PRODUCT_BUNDLE_IDENTIFIER = Socket;
				PRODUCT_MODULE_NAME = "$(TARGET_NAME:c99extidentifier)";
				PRODUCT_NAME = "$(TARGET_NAME:c99extidentifier)";
				SKIP_INSTALL = YES;
				SWIFT_VERSION = 3.0;
				TARGET_NAME = Socket;
			};
			name = Release;
		};
		OBJ_1009 /* Debug */ = {
			isa = XCBuildConfiguration;
			buildSettings = {
				FRAMEWORK_SEARCH_PATHS = (
					"$(inherited)",
					"$(PLATFORM_DIR)/Developer/Library/Frameworks",
				);
				HEADER_SEARCH_PATHS = "$(inherited)";
				INFOPLIST_FILE = mikrotik_router_manager.xcodeproj/ConfigurationTestExecutable_Info.plist;
				LD_RUNPATH_SEARCH_PATHS = "$(TOOLCHAIN_DIR)/usr/lib/swift/macosx @executable_path";
				OTHER_LDFLAGS = "$(inherited)";
				OTHER_SWIFT_FLAGS = "$(inherited)";
				SWIFT_FORCE_DYNAMIC_LINK_STDLIB = YES;
				SWIFT_FORCE_STATIC_LINK_STDLIB = NO;
				SWIFT_VERSION = 3.0;
				TARGET_NAME = ConfigurationTestExecutable;
			};
			name = Debug;
		};
		OBJ_1010 /* Release */ = {
			isa = XCBuildConfiguration;
			buildSettings = {
				FRAMEWORK_SEARCH_PATHS = (
					"$(inherited)",
					"$(PLATFORM_DIR)/Developer/Library/Frameworks",
				);
				HEADER_SEARCH_PATHS = "$(inherited)";
				INFOPLIST_FILE = mikrotik_router_manager.xcodeproj/ConfigurationTestExecutable_Info.plist;
				LD_RUNPATH_SEARCH_PATHS = "$(TOOLCHAIN_DIR)/usr/lib/swift/macosx @executable_path";
				OTHER_LDFLAGS = "$(inherited)";
				OTHER_SWIFT_FLAGS = "$(inherited)";
				SWIFT_FORCE_DYNAMIC_LINK_STDLIB = YES;
				SWIFT_FORCE_STATIC_LINK_STDLIB = NO;
				SWIFT_VERSION = 3.0;
				TARGET_NAME = ConfigurationTestExecutable;
			};
			name = Release;
		};
		OBJ_1019 /* Debug */ = {
			isa = XCBuildConfiguration;
			buildSettings = {
				ENABLE_TESTABILITY = YES;
				FRAMEWORK_SEARCH_PATHS = (
					"$(inherited)",
					"$(PLATFORM_DIR)/Developer/Library/Frameworks",
				);
				HEADER_SEARCH_PATHS = "$(inherited)";
				INFOPLIST_FILE = mikrotik_router_manager.xcodeproj/Configuration_Info.plist;
				LD_RUNPATH_SEARCH_PATHS = "$(TOOLCHAIN_DIR)/usr/lib/swift/macosx";
				OTHER_LDFLAGS = "$(inherited)";
				OTHER_SWIFT_FLAGS = "$(inherited)";
				PRODUCT_BUNDLE_IDENTIFIER = Configuration;
				PRODUCT_MODULE_NAME = "$(TARGET_NAME:c99extidentifier)";
				PRODUCT_NAME = "$(TARGET_NAME:c99extidentifier)";
				SKIP_INSTALL = YES;
				SWIFT_VERSION = 3.0;
				TARGET_NAME = Configuration;
			};
			name = Debug;
		};
		OBJ_1020 /* Release */ = {
			isa = XCBuildConfiguration;
			buildSettings = {
				ENABLE_TESTABILITY = YES;
				FRAMEWORK_SEARCH_PATHS = (
					"$(inherited)",
					"$(PLATFORM_DIR)/Developer/Library/Frameworks",
				);
				HEADER_SEARCH_PATHS = "$(inherited)";
				INFOPLIST_FILE = mikrotik_router_manager.xcodeproj/Configuration_Info.plist;
				LD_RUNPATH_SEARCH_PATHS = "$(TOOLCHAIN_DIR)/usr/lib/swift/macosx";
				OTHER_LDFLAGS = "$(inherited)";
				OTHER_SWIFT_FLAGS = "$(inherited)";
				PRODUCT_BUNDLE_IDENTIFIER = Configuration;
				PRODUCT_MODULE_NAME = "$(TARGET_NAME:c99extidentifier)";
				PRODUCT_NAME = "$(TARGET_NAME:c99extidentifier)";
				SKIP_INSTALL = YES;
				SWIFT_VERSION = 3.0;
				TARGET_NAME = Configuration;
			};
			name = Release;
		};
		OBJ_1032 /* Debug */ = {
			isa = XCBuildConfiguration;
			buildSettings = {
				ENABLE_TESTABILITY = YES;
				FRAMEWORK_SEARCH_PATHS = (
					"$(inherited)",
					"$(PLATFORM_DIR)/Developer/Library/Frameworks",
				);
				HEADER_SEARCH_PATHS = "$(inherited)";
				INFOPLIST_FILE = mikrotik_router_manager.xcodeproj/LoggerAPI_Info.plist;
				LD_RUNPATH_SEARCH_PATHS = "$(TOOLCHAIN_DIR)/usr/lib/swift/macosx";
				OTHER_LDFLAGS = "$(inherited)";
				OTHER_SWIFT_FLAGS = "$(inherited)";
				PRODUCT_BUNDLE_IDENTIFIER = LoggerAPI;
				PRODUCT_MODULE_NAME = "$(TARGET_NAME:c99extidentifier)";
				PRODUCT_NAME = "$(TARGET_NAME:c99extidentifier)";
				SKIP_INSTALL = YES;
				SWIFT_VERSION = 4.0;
				TARGET_NAME = LoggerAPI;
			};
			name = Debug;
		};
		OBJ_1033 /* Release */ = {
			isa = XCBuildConfiguration;
			buildSettings = {
				ENABLE_TESTABILITY = YES;
				FRAMEWORK_SEARCH_PATHS = (
					"$(inherited)",
					"$(PLATFORM_DIR)/Developer/Library/Frameworks",
				);
				HEADER_SEARCH_PATHS = "$(inherited)";
				INFOPLIST_FILE = mikrotik_router_manager.xcodeproj/LoggerAPI_Info.plist;
				LD_RUNPATH_SEARCH_PATHS = "$(TOOLCHAIN_DIR)/usr/lib/swift/macosx";
				OTHER_LDFLAGS = "$(inherited)";
				OTHER_SWIFT_FLAGS = "$(inherited)";
				PRODUCT_BUNDLE_IDENTIFIER = LoggerAPI;
				PRODUCT_MODULE_NAME = "$(TARGET_NAME:c99extidentifier)";
				PRODUCT_NAME = "$(TARGET_NAME:c99extidentifier)";
				SKIP_INSTALL = YES;
				SWIFT_VERSION = 4.0;
				TARGET_NAME = LoggerAPI;
			};
			name = Release;
		};
		OBJ_1039 /* Debug */ = {
			isa = XCBuildConfiguration;
			buildSettings = {
			};
			name = Debug;
		};
		OBJ_1040 /* Release */ = {
			isa = XCBuildConfiguration;
			buildSettings = {
			};
			name = Release;
		};
		OBJ_1044 /* Debug */ = {
			isa = XCBuildConfiguration;
			buildSettings = {
			};
			name = Debug;
		};
		OBJ_1045 /* Release */ = {
			isa = XCBuildConfiguration;
			buildSettings = {
			};
			name = Release;
		};
		OBJ_1049 /* Debug */ = {
			isa = XCBuildConfiguration;
			buildSettings = {
			};
			name = Debug;
		};
		OBJ_1050 /* Release */ = {
			isa = XCBuildConfiguration;
			buildSettings = {
			};
			name = Release;
		};
		OBJ_1054 /* Debug */ = {
			isa = XCBuildConfiguration;
			buildSettings = {
			};
			name = Debug;
		};
		OBJ_1055 /* Release */ = {
			isa = XCBuildConfiguration;
			buildSettings = {
			};
			name = Release;
		};
		OBJ_1058 /* Debug */ = {
			isa = XCBuildConfiguration;
			buildSettings = {
			};
			name = Debug;
		};
		OBJ_1059 /* Release */ = {
			isa = XCBuildConfiguration;
			buildSettings = {
			};
			name = Release;
		};
		OBJ_1062 /* Debug */ = {
			isa = XCBuildConfiguration;
			buildSettings = {
			};
			name = Debug;
		};
		OBJ_1063 /* Release */ = {
			isa = XCBuildConfiguration;
			buildSettings = {
			};
			name = Release;
		};
		OBJ_3 /* Debug */ = {
			isa = XCBuildConfiguration;
			buildSettings = {
				CLANG_ENABLE_OBJC_ARC = YES;
				COMBINE_HIDPI_IMAGES = YES;
				COPY_PHASE_STRIP = NO;
				DEBUG_INFORMATION_FORMAT = dwarf;
				DYLIB_INSTALL_NAME_BASE = "@rpath";
				ENABLE_NS_ASSERTIONS = YES;
				GCC_OPTIMIZATION_LEVEL = 0;
				MACOSX_DEPLOYMENT_TARGET = 10.10;
				ONLY_ACTIVE_ARCH = YES;
				OTHER_LDFLAGS = "-L/usr/local/lib";
				OTHER_SWIFT_FLAGS = "-DXcode";
				PRODUCT_NAME = "$(TARGET_NAME)";
				SDKROOT = macosx;
				SUPPORTED_PLATFORMS = "macosx iphoneos iphonesimulator appletvos appletvsimulator watchos watchsimulator";
				SWIFT_ACTIVE_COMPILATION_CONDITIONS = SWIFT_PACKAGE;
				SWIFT_OPTIMIZATION_LEVEL = "-Onone";
				USE_HEADERMAP = NO;
			};
			name = Debug;
		};
		OBJ_362 /* Debug */ = {
			isa = XCBuildConfiguration;
			buildSettings = {
				LD = /usr/bin/true;
				OTHER_SWIFT_FLAGS = "-swift-version 3 -I /Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/lib/swift/pm/3 -target x86_64-apple-macosx10.10 -sdk /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX10.13.sdk";
				SWIFT_VERSION = 3.0;
			};
			name = Debug;
		};
		OBJ_363 /* Release */ = {
			isa = XCBuildConfiguration;
			buildSettings = {
				LD = /usr/bin/true;
				OTHER_SWIFT_FLAGS = "-swift-version 3 -I /Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/lib/swift/pm/3 -target x86_64-apple-macosx10.10 -sdk /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX10.13.sdk";
				SWIFT_VERSION = 3.0;
			};
			name = Release;
		};
		OBJ_368 /* Debug */ = {
			isa = XCBuildConfiguration;
			buildSettings = {
				LD = /usr/bin/true;
				OTHER_SWIFT_FLAGS = "-swift-version 3 -I /Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/lib/swift/pm/3 -target x86_64-apple-macosx10.10 -sdk /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX10.13.sdk";
				SWIFT_VERSION = 3.0;
			};
			name = Debug;
		};
		OBJ_369 /* Release */ = {
			isa = XCBuildConfiguration;
			buildSettings = {
				LD = /usr/bin/true;
				OTHER_SWIFT_FLAGS = "-swift-version 3 -I /Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/lib/swift/pm/3 -target x86_64-apple-macosx10.10 -sdk /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX10.13.sdk";
				SWIFT_VERSION = 3.0;
			};
			name = Release;
		};
		OBJ_374 /* Debug */ = {
			isa = XCBuildConfiguration;
			buildSettings = {
				LD = /usr/bin/true;
				OTHER_SWIFT_FLAGS = "-swift-version 3 -I /Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/lib/swift/pm/3 -target x86_64-apple-macosx10.10 -sdk /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX10.13.sdk";
				SWIFT_VERSION = 3.0;
			};
			name = Debug;
		};
		OBJ_375 /* Release */ = {
			isa = XCBuildConfiguration;
			buildSettings = {
				LD = /usr/bin/true;
				OTHER_SWIFT_FLAGS = "-swift-version 3 -I /Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/lib/swift/pm/3 -target x86_64-apple-macosx10.10 -sdk /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX10.13.sdk";
				SWIFT_VERSION = 3.0;
			};
			name = Release;
		};
		OBJ_380 /* Debug */ = {
			isa = XCBuildConfiguration;
			buildSettings = {
				LD = /usr/bin/true;
				OTHER_SWIFT_FLAGS = "-swift-version 3 -I /Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/lib/swift/pm/3 -target x86_64-apple-macosx10.10 -sdk /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX10.13.sdk";
				SWIFT_VERSION = 3.0;
			};
			name = Debug;
		};
		OBJ_381 /* Release */ = {
			isa = XCBuildConfiguration;
			buildSettings = {
				LD = /usr/bin/true;
				OTHER_SWIFT_FLAGS = "-swift-version 3 -I /Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/lib/swift/pm/3 -target x86_64-apple-macosx10.10 -sdk /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX10.13.sdk";
				SWIFT_VERSION = 3.0;
			};
			name = Release;
		};
		OBJ_386 /* Debug */ = {
			isa = XCBuildConfiguration;
			buildSettings = {
				LD = /usr/bin/true;
				OTHER_SWIFT_FLAGS = "-swift-version 3 -I /Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/lib/swift/pm/3 -target x86_64-apple-macosx10.10 -sdk /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX10.13.sdk";
				SWIFT_VERSION = 3.0;
			};
			name = Debug;
		};
		OBJ_387 /* Release */ = {
			isa = XCBuildConfiguration;
			buildSettings = {
				LD = /usr/bin/true;
				OTHER_SWIFT_FLAGS = "-swift-version 3 -I /Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/lib/swift/pm/3 -target x86_64-apple-macosx10.10 -sdk /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX10.13.sdk";
				SWIFT_VERSION = 3.0;
			};
			name = Release;
		};
		OBJ_392 /* Debug */ = {
			isa = XCBuildConfiguration;
			buildSettings = {
				LD = /usr/bin/true;
				OTHER_SWIFT_FLAGS = "-swift-version 3 -I /Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/lib/swift/pm/3 -target x86_64-apple-macosx10.10 -sdk /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX10.13.sdk";
				SWIFT_VERSION = 3.0;
			};
			name = Debug;
		};
		OBJ_393 /* Release */ = {
			isa = XCBuildConfiguration;
			buildSettings = {
				LD = /usr/bin/true;
				OTHER_SWIFT_FLAGS = "-swift-version 3 -I /Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/lib/swift/pm/3 -target x86_64-apple-macosx10.10 -sdk /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX10.13.sdk";
				SWIFT_VERSION = 3.0;
			};
			name = Release;
		};
		OBJ_398 /* Debug */ = {
			isa = XCBuildConfiguration;
			buildSettings = {
				LD = /usr/bin/true;
				OTHER_SWIFT_FLAGS = "-swift-version 4 -I /Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/lib/swift/pm/4 -target x86_64-apple-macosx10.10 -sdk /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX10.13.sdk";
				SWIFT_VERSION = 4.0;
			};
			name = Debug;
		};
		OBJ_399 /* Release */ = {
			isa = XCBuildConfiguration;
			buildSettings = {
				LD = /usr/bin/true;
				OTHER_SWIFT_FLAGS = "-swift-version 4 -I /Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/lib/swift/pm/4 -target x86_64-apple-macosx10.10 -sdk /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX10.13.sdk";
				SWIFT_VERSION = 4.0;
			};
			name = Release;
		};
		OBJ_4 /* Release */ = {
			isa = XCBuildConfiguration;
			buildSettings = {
				CLANG_ENABLE_OBJC_ARC = YES;
				COMBINE_HIDPI_IMAGES = YES;
				COPY_PHASE_STRIP = YES;
				DEBUG_INFORMATION_FORMAT = "dwarf-with-dsym";
				DYLIB_INSTALL_NAME_BASE = "@rpath";
				GCC_OPTIMIZATION_LEVEL = s;
				MACOSX_DEPLOYMENT_TARGET = 10.10;
				OTHER_LDFLAGS = "-L/usr/local/lib";
				OTHER_SWIFT_FLAGS = "-DXcode";
				PRODUCT_NAME = "$(TARGET_NAME)";
				SDKROOT = macosx;
				SUPPORTED_PLATFORMS = "macosx iphoneos iphonesimulator appletvos appletvsimulator watchos watchsimulator";
				SWIFT_ACTIVE_COMPILATION_CONDITIONS = SWIFT_PACKAGE;
				SWIFT_OPTIMIZATION_LEVEL = "-Owholemodule";
				USE_HEADERMAP = NO;
			};
			name = Release;
		};
		OBJ_404 /* Debug */ = {
			isa = XCBuildConfiguration;
			buildSettings = {
				LD = /usr/bin/true;
				OTHER_SWIFT_FLAGS = "-swift-version 4 -I /Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/lib/swift/pm/4 -target x86_64-apple-macosx10.10 -sdk /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX10.13.sdk";
				SWIFT_VERSION = 4.0;
			};
			name = Debug;
		};
		OBJ_405 /* Release */ = {
			isa = XCBuildConfiguration;
			buildSettings = {
				LD = /usr/bin/true;
				OTHER_SWIFT_FLAGS = "-swift-version 4 -I /Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/lib/swift/pm/4 -target x86_64-apple-macosx10.10 -sdk /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX10.13.sdk";
				SWIFT_VERSION = 4.0;
			};
			name = Release;
		};
		OBJ_410 /* Debug */ = {
			isa = XCBuildConfiguration;
			buildSettings = {
				LD = /usr/bin/true;
				OTHER_SWIFT_FLAGS = "-swift-version 4 -I /Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/lib/swift/pm/4 -target x86_64-apple-macosx10.10 -sdk /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX10.13.sdk";
				SWIFT_VERSION = 4.0;
			};
			name = Debug;
		};
		OBJ_411 /* Release */ = {
			isa = XCBuildConfiguration;
			buildSettings = {
				LD = /usr/bin/true;
				OTHER_SWIFT_FLAGS = "-swift-version 4 -I /Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/lib/swift/pm/4 -target x86_64-apple-macosx10.10 -sdk /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX10.13.sdk";
				SWIFT_VERSION = 4.0;
			};
			name = Release;
		};
		OBJ_416 /* Debug */ = {
			isa = XCBuildConfiguration;
			buildSettings = {
				LD = /usr/bin/true;
				OTHER_SWIFT_FLAGS = "-swift-version 4 -I /Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/lib/swift/pm/4 -target x86_64-apple-macosx10.10 -sdk /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX10.13.sdk";
				SWIFT_VERSION = 4.0;
			};
			name = Debug;
		};
		OBJ_417 /* Release */ = {
			isa = XCBuildConfiguration;
			buildSettings = {
				LD = /usr/bin/true;
				OTHER_SWIFT_FLAGS = "-swift-version 4 -I /Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/lib/swift/pm/4 -target x86_64-apple-macosx10.10 -sdk /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX10.13.sdk";
				SWIFT_VERSION = 4.0;
			};
			name = Release;
		};
		OBJ_422 /* Debug */ = {
			isa = XCBuildConfiguration;
			buildSettings = {
				LD = /usr/bin/true;
				OTHER_SWIFT_FLAGS = "-swift-version 4 -I /Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/lib/swift/pm/4 -target x86_64-apple-macosx10.10 -sdk /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX10.13.sdk";
				SWIFT_VERSION = 4.0;
			};
			name = Debug;
		};
		OBJ_423 /* Release */ = {
			isa = XCBuildConfiguration;
			buildSettings = {
				LD = /usr/bin/true;
				OTHER_SWIFT_FLAGS = "-swift-version 4 -I /Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/lib/swift/pm/4 -target x86_64-apple-macosx10.10 -sdk /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX10.13.sdk";
				SWIFT_VERSION = 4.0;
			};
			name = Release;
		};
		OBJ_428 /* Debug */ = {
			isa = XCBuildConfiguration;
			buildSettings = {
				LD = /usr/bin/true;
				OTHER_SWIFT_FLAGS = "-swift-version 4 -I /Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/lib/swift/pm/4 -target x86_64-apple-macosx10.10 -sdk /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX10.13.sdk";
				SWIFT_VERSION = 4.0;
			};
			name = Debug;
		};
		OBJ_429 /* Release */ = {
			isa = XCBuildConfiguration;
			buildSettings = {
				LD = /usr/bin/true;
				OTHER_SWIFT_FLAGS = "-swift-version 4 -I /Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/lib/swift/pm/4 -target x86_64-apple-macosx10.10 -sdk /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX10.13.sdk";
				SWIFT_VERSION = 4.0;
			};
			name = Release;
		};
		OBJ_434 /* Debug */ = {
			isa = XCBuildConfiguration;
			buildSettings = {
				LD = /usr/bin/true;
				OTHER_SWIFT_FLAGS = "-swift-version 3 -I /Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/lib/swift/pm/3 -target x86_64-apple-macosx10.10 -sdk /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX10.13.sdk";
				SWIFT_VERSION = 3.0;
			};
			name = Debug;
		};
		OBJ_435 /* Release */ = {
			isa = XCBuildConfiguration;
			buildSettings = {
				LD = /usr/bin/true;
				OTHER_SWIFT_FLAGS = "-swift-version 3 -I /Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/lib/swift/pm/3 -target x86_64-apple-macosx10.10 -sdk /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX10.13.sdk";
				SWIFT_VERSION = 3.0;
			};
			name = Release;
		};
		OBJ_440 /* Debug */ = {
			isa = XCBuildConfiguration;
			buildSettings = {
				LD = /usr/bin/true;
				OTHER_SWIFT_FLAGS = "-swift-version 4 -I /Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/lib/swift/pm/4 -target x86_64-apple-macosx10.10 -sdk /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX10.13.sdk";
				SWIFT_VERSION = 4.0;
			};
			name = Debug;
		};
		OBJ_441 /* Release */ = {
			isa = XCBuildConfiguration;
			buildSettings = {
				LD = /usr/bin/true;
				OTHER_SWIFT_FLAGS = "-swift-version 4 -I /Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/lib/swift/pm/4 -target x86_64-apple-macosx10.10 -sdk /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX10.13.sdk";
				SWIFT_VERSION = 4.0;
			};
			name = Release;
		};
		OBJ_446 /* Debug */ = {
			isa = XCBuildConfiguration;
			buildSettings = {
				LD = /usr/bin/true;
				OTHER_SWIFT_FLAGS = "-swift-version 4 -I /Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/lib/swift/pm/4 -target x86_64-apple-macosx10.10 -sdk /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX10.13.sdk";
				SWIFT_VERSION = 4.0;
			};
			name = Debug;
		};
		OBJ_447 /* Release */ = {
			isa = XCBuildConfiguration;
			buildSettings = {
				LD = /usr/bin/true;
				OTHER_SWIFT_FLAGS = "-swift-version 4 -I /Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/lib/swift/pm/4 -target x86_64-apple-macosx10.10 -sdk /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX10.13.sdk";
				SWIFT_VERSION = 4.0;
			};
			name = Release;
		};
		OBJ_452 /* Debug */ = {
			isa = XCBuildConfiguration;
			buildSettings = {
				LD = /usr/bin/true;
				OTHER_SWIFT_FLAGS = "-swift-version 3 -I /Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/lib/swift/pm/3 -target x86_64-apple-macosx10.10 -sdk /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX10.13.sdk";
				SWIFT_VERSION = 3.0;
			};
			name = Debug;
		};
		OBJ_453 /* Release */ = {
			isa = XCBuildConfiguration;
			buildSettings = {
				LD = /usr/bin/true;
				OTHER_SWIFT_FLAGS = "-swift-version 3 -I /Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/lib/swift/pm/3 -target x86_64-apple-macosx10.10 -sdk /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX10.13.sdk";
				SWIFT_VERSION = 3.0;
			};
			name = Release;
		};
		OBJ_458 /* Debug */ = {
			isa = XCBuildConfiguration;
			buildSettings = {
				LD = /usr/bin/true;
				OTHER_SWIFT_FLAGS = "-swift-version 3 -I /Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/lib/swift/pm/3 -target x86_64-apple-macosx10.10 -sdk /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX10.13.sdk";
				SWIFT_VERSION = 3.0;
			};
			name = Debug;
		};
		OBJ_459 /* Release */ = {
			isa = XCBuildConfiguration;
			buildSettings = {
				LD = /usr/bin/true;
				OTHER_SWIFT_FLAGS = "-swift-version 3 -I /Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/lib/swift/pm/3 -target x86_64-apple-macosx10.10 -sdk /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX10.13.sdk";
				SWIFT_VERSION = 3.0;
			};
			name = Release;
		};
		OBJ_464 /* Debug */ = {
			isa = XCBuildConfiguration;
			buildSettings = {
				LD = /usr/bin/true;
				OTHER_SWIFT_FLAGS = "-swift-version 4 -I /Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/lib/swift/pm/4 -target x86_64-apple-macosx10.10 -sdk /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX10.13.sdk";
				SWIFT_VERSION = 4.0;
			};
			name = Debug;
		};
		OBJ_465 /* Release */ = {
			isa = XCBuildConfiguration;
			buildSettings = {
				LD = /usr/bin/true;
				OTHER_SWIFT_FLAGS = "-swift-version 4 -I /Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/lib/swift/pm/4 -target x86_64-apple-macosx10.10 -sdk /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX10.13.sdk";
				SWIFT_VERSION = 4.0;
			};
			name = Release;
		};
		OBJ_470 /* Debug */ = {
			isa = XCBuildConfiguration;
			buildSettings = {
				FRAMEWORK_SEARCH_PATHS = (
					"$(inherited)",
					"$(PLATFORM_DIR)/Developer/Library/Frameworks",
				);
				HEADER_SEARCH_PATHS = (
					"$(inherited)",
					"$(SRCROOT)/.build/checkouts/CommonCrypto.git-1219305460334093717",
					"$(SRCROOT)/.build/checkouts/Kitura-net.git--7410958935072501107/Sources/CHTTPParser/include",
					"$(SRCROOT)/.build/checkouts/CCurl.git-8026296523752779197",
					"$(SRCROOT)/.build/checkouts/CMySQL.git-3001417495195486492",
					"$(SRCROOT)/mikrotik_router_manager.xcodeproj/GeneratedModuleMap/CHTTPParser",
				);
				INFOPLIST_FILE = mikrotik_router_manager.xcodeproj/SERVER_Info.plist;
				LD_RUNPATH_SEARCH_PATHS = "$(TOOLCHAIN_DIR)/usr/lib/swift/macosx @executable_path";
				OTHER_LDFLAGS = "$(inherited)";
				OTHER_SWIFT_FLAGS = "$(inherited) -Xcc -fmodule-map-file=$(SRCROOT)/mikrotik_router_manager.xcodeproj/GeneratedModuleMap/CHTTPParser/module.modulemap";
				SWIFT_FORCE_DYNAMIC_LINK_STDLIB = YES;
				SWIFT_FORCE_STATIC_LINK_STDLIB = NO;
				SWIFT_VERSION = 3.0;
				TARGET_NAME = SERVER;
			};
			name = Debug;
		};
		OBJ_471 /* Release */ = {
			isa = XCBuildConfiguration;
			buildSettings = {
				FRAMEWORK_SEARCH_PATHS = (
					"$(inherited)",
					"$(PLATFORM_DIR)/Developer/Library/Frameworks",
				);
				HEADER_SEARCH_PATHS = (
					"$(inherited)",
					"$(SRCROOT)/.build/checkouts/CommonCrypto.git-1219305460334093717",
					"$(SRCROOT)/.build/checkouts/Kitura-net.git--7410958935072501107/Sources/CHTTPParser/include",
					"$(SRCROOT)/.build/checkouts/CCurl.git-8026296523752779197",
					"$(SRCROOT)/.build/checkouts/CMySQL.git-3001417495195486492",
					"$(SRCROOT)/mikrotik_router_manager.xcodeproj/GeneratedModuleMap/CHTTPParser",
				);
				INFOPLIST_FILE = mikrotik_router_manager.xcodeproj/SERVER_Info.plist;
				LD_RUNPATH_SEARCH_PATHS = "$(TOOLCHAIN_DIR)/usr/lib/swift/macosx @executable_path";
				OTHER_LDFLAGS = "$(inherited)";
				OTHER_SWIFT_FLAGS = "$(inherited) -Xcc -fmodule-map-file=$(SRCROOT)/mikrotik_router_manager.xcodeproj/GeneratedModuleMap/CHTTPParser/module.modulemap";
				SWIFT_FORCE_DYNAMIC_LINK_STDLIB = YES;
				SWIFT_FORCE_STATIC_LINK_STDLIB = NO;
				SWIFT_VERSION = 3.0;
				TARGET_NAME = SERVER;
			};
			name = Release;
		};
		OBJ_535 /* Debug */ = {
			isa = XCBuildConfiguration;
			buildSettings = {
				ENABLE_TESTABILITY = YES;
				FRAMEWORK_SEARCH_PATHS = (
					"$(inherited)",
					"$(PLATFORM_DIR)/Developer/Library/Frameworks",
				);
				HEADER_SEARCH_PATHS = (
					"$(inherited)",
					"$(SRCROOT)/.build/checkouts/CommonCrypto.git-1219305460334093717",
					"$(SRCROOT)/.build/checkouts/Kitura-net.git--7410958935072501107/Sources/CHTTPParser/include",
					"$(SRCROOT)/.build/checkouts/CCurl.git-8026296523752779197",
					"$(SRCROOT)/.build/checkouts/CMySQL.git-3001417495195486492",
					"$(SRCROOT)/mikrotik_router_manager.xcodeproj/GeneratedModuleMap/CHTTPParser",
				);
				INFOPLIST_FILE = mikrotik_router_manager.xcodeproj/CORE_Info.plist;
				LD_RUNPATH_SEARCH_PATHS = "$(TOOLCHAIN_DIR)/usr/lib/swift/macosx";
				OTHER_LDFLAGS = "$(inherited)";
				OTHER_SWIFT_FLAGS = "$(inherited) -Xcc -fmodule-map-file=$(SRCROOT)/mikrotik_router_manager.xcodeproj/GeneratedModuleMap/CHTTPParser/module.modulemap";
				PRODUCT_BUNDLE_IDENTIFIER = CORE;
				PRODUCT_MODULE_NAME = "$(TARGET_NAME:c99extidentifier)";
				PRODUCT_NAME = "$(TARGET_NAME:c99extidentifier)";
				SKIP_INSTALL = YES;
				SWIFT_VERSION = 3.0;
				TARGET_NAME = CORE;
			};
			name = Debug;
		};
		OBJ_536 /* Release */ = {
			isa = XCBuildConfiguration;
			buildSettings = {
				ENABLE_TESTABILITY = YES;
				FRAMEWORK_SEARCH_PATHS = (
					"$(inherited)",
					"$(PLATFORM_DIR)/Developer/Library/Frameworks",
				);
				HEADER_SEARCH_PATHS = (
					"$(inherited)",
					"$(SRCROOT)/.build/checkouts/CommonCrypto.git-1219305460334093717",
					"$(SRCROOT)/.build/checkouts/Kitura-net.git--7410958935072501107/Sources/CHTTPParser/include",
					"$(SRCROOT)/.build/checkouts/CCurl.git-8026296523752779197",
					"$(SRCROOT)/.build/checkouts/CMySQL.git-3001417495195486492",
					"$(SRCROOT)/mikrotik_router_manager.xcodeproj/GeneratedModuleMap/CHTTPParser",
				);
				INFOPLIST_FILE = mikrotik_router_manager.xcodeproj/CORE_Info.plist;
				LD_RUNPATH_SEARCH_PATHS = "$(TOOLCHAIN_DIR)/usr/lib/swift/macosx";
				OTHER_LDFLAGS = "$(inherited)";
				OTHER_SWIFT_FLAGS = "$(inherited) -Xcc -fmodule-map-file=$(SRCROOT)/mikrotik_router_manager.xcodeproj/GeneratedModuleMap/CHTTPParser/module.modulemap";
				PRODUCT_BUNDLE_IDENTIFIER = CORE;
				PRODUCT_MODULE_NAME = "$(TARGET_NAME:c99extidentifier)";
				PRODUCT_NAME = "$(TARGET_NAME:c99extidentifier)";
				SKIP_INSTALL = YES;
				SWIFT_VERSION = 3.0;
				TARGET_NAME = CORE;
			};
			name = Release;
		};
		OBJ_589 /* Debug */ = {
			isa = XCBuildConfiguration;
			buildSettings = {
				ENABLE_TESTABILITY = YES;
				FRAMEWORK_SEARCH_PATHS = (
					"$(inherited)",
					"$(PLATFORM_DIR)/Developer/Library/Frameworks",
				);
				HEADER_SEARCH_PATHS = (
					"$(inherited)",
					"$(SRCROOT)/.build/checkouts/Kitura-net.git--7410958935072501107/Sources/CHTTPParser/include",
					"$(SRCROOT)/.build/checkouts/CCurl.git-8026296523752779197",
					"$(SRCROOT)/mikrotik_router_manager.xcodeproj/GeneratedModuleMap/CHTTPParser",
				);
				INFOPLIST_FILE = mikrotik_router_manager.xcodeproj/KituraCORS_Info.plist;
				LD_RUNPATH_SEARCH_PATHS = "$(TOOLCHAIN_DIR)/usr/lib/swift/macosx";
				OTHER_LDFLAGS = "$(inherited)";
				OTHER_SWIFT_FLAGS = "$(inherited) -Xcc -fmodule-map-file=$(SRCROOT)/mikrotik_router_manager.xcodeproj/GeneratedModuleMap/CHTTPParser/module.modulemap";
				PRODUCT_BUNDLE_IDENTIFIER = KituraCORS;
				PRODUCT_MODULE_NAME = "$(TARGET_NAME:c99extidentifier)";
				PRODUCT_NAME = "$(TARGET_NAME:c99extidentifier)";
				SKIP_INSTALL = YES;
				SWIFT_VERSION = 3.0;
				TARGET_NAME = KituraCORS;
			};
			name = Debug;
		};
		OBJ_590 /* Release */ = {
			isa = XCBuildConfiguration;
			buildSettings = {
				ENABLE_TESTABILITY = YES;
				FRAMEWORK_SEARCH_PATHS = (
					"$(inherited)",
					"$(PLATFORM_DIR)/Developer/Library/Frameworks",
				);
				HEADER_SEARCH_PATHS = (
					"$(inherited)",
					"$(SRCROOT)/.build/checkouts/Kitura-net.git--7410958935072501107/Sources/CHTTPParser/include",
					"$(SRCROOT)/.build/checkouts/CCurl.git-8026296523752779197",
					"$(SRCROOT)/mikrotik_router_manager.xcodeproj/GeneratedModuleMap/CHTTPParser",
				);
				INFOPLIST_FILE = mikrotik_router_manager.xcodeproj/KituraCORS_Info.plist;
				LD_RUNPATH_SEARCH_PATHS = "$(TOOLCHAIN_DIR)/usr/lib/swift/macosx";
				OTHER_LDFLAGS = "$(inherited)";
				OTHER_SWIFT_FLAGS = "$(inherited) -Xcc -fmodule-map-file=$(SRCROOT)/mikrotik_router_manager.xcodeproj/GeneratedModuleMap/CHTTPParser/module.modulemap";
				PRODUCT_BUNDLE_IDENTIFIER = KituraCORS;
				PRODUCT_MODULE_NAME = "$(TARGET_NAME:c99extidentifier)";
				PRODUCT_NAME = "$(TARGET_NAME:c99extidentifier)";
				SKIP_INSTALL = YES;
				SWIFT_VERSION = 3.0;
				TARGET_NAME = KituraCORS;
			};
			name = Release;
		};
		OBJ_613 /* Debug */ = {
			isa = XCBuildConfiguration;
			buildSettings = {
				ENABLE_TESTABILITY = YES;
				FRAMEWORK_SEARCH_PATHS = (
					"$(inherited)",
					"$(PLATFORM_DIR)/Developer/Library/Frameworks",
				);
				HEADER_SEARCH_PATHS = "$(inherited)";
				INFOPLIST_FILE = mikrotik_router_manager.xcodeproj/HeliumLogger_Info.plist;
				LD_RUNPATH_SEARCH_PATHS = "$(TOOLCHAIN_DIR)/usr/lib/swift/macosx";
				OTHER_LDFLAGS = "$(inherited)";
				OTHER_SWIFT_FLAGS = "$(inherited)";
				PRODUCT_BUNDLE_IDENTIFIER = HeliumLogger;
				PRODUCT_MODULE_NAME = "$(TARGET_NAME:c99extidentifier)";
				PRODUCT_NAME = "$(TARGET_NAME:c99extidentifier)";
				SKIP_INSTALL = YES;
				SWIFT_VERSION = 3.0;
				TARGET_NAME = HeliumLogger;
			};
			name = Debug;
		};
		OBJ_614 /* Release */ = {
			isa = XCBuildConfiguration;
			buildSettings = {
				ENABLE_TESTABILITY = YES;
				FRAMEWORK_SEARCH_PATHS = (
					"$(inherited)",
					"$(PLATFORM_DIR)/Developer/Library/Frameworks",
				);
				HEADER_SEARCH_PATHS = "$(inherited)";
				INFOPLIST_FILE = mikrotik_router_manager.xcodeproj/HeliumLogger_Info.plist;
				LD_RUNPATH_SEARCH_PATHS = "$(TOOLCHAIN_DIR)/usr/lib/swift/macosx";
				OTHER_LDFLAGS = "$(inherited)";
				OTHER_SWIFT_FLAGS = "$(inherited)";
				PRODUCT_BUNDLE_IDENTIFIER = HeliumLogger;
				PRODUCT_MODULE_NAME = "$(TARGET_NAME:c99extidentifier)";
				PRODUCT_NAME = "$(TARGET_NAME:c99extidentifier)";
				SKIP_INSTALL = YES;
				SWIFT_VERSION = 3.0;
				TARGET_NAME = HeliumLogger;
			};
			name = Release;
		};
		OBJ_622 /* Debug */ = {
			isa = XCBuildConfiguration;
			buildSettings = {
				ENABLE_TESTABILITY = YES;
				FRAMEWORK_SEARCH_PATHS = (
					"$(inherited)",
					"$(PLATFORM_DIR)/Developer/Library/Frameworks",
				);
				HEADER_SEARCH_PATHS = (
					"$(inherited)",
					"$(SRCROOT)/.build/checkouts/CommonCrypto.git-1219305460334093717",
					"$(SRCROOT)/.build/checkouts/Kitura-net.git--7410958935072501107/Sources/CHTTPParser/include",
					"$(SRCROOT)/.build/checkouts/CCurl.git-8026296523752779197",
					"$(SRCROOT)/mikrotik_router_manager.xcodeproj/GeneratedModuleMap/CHTTPParser",
				);
				INFOPLIST_FILE = mikrotik_router_manager.xcodeproj/CredentialsHTTP_Info.plist;
				LD_RUNPATH_SEARCH_PATHS = "$(TOOLCHAIN_DIR)/usr/lib/swift/macosx";
				OTHER_LDFLAGS = "$(inherited)";
				OTHER_SWIFT_FLAGS = "$(inherited) -Xcc -fmodule-map-file=$(SRCROOT)/mikrotik_router_manager.xcodeproj/GeneratedModuleMap/CHTTPParser/module.modulemap";
				PRODUCT_BUNDLE_IDENTIFIER = CredentialsHTTP;
				PRODUCT_MODULE_NAME = "$(TARGET_NAME:c99extidentifier)";
				PRODUCT_NAME = "$(TARGET_NAME:c99extidentifier)";
				SKIP_INSTALL = YES;
				SWIFT_VERSION = 3.0;
				TARGET_NAME = CredentialsHTTP;
			};
			name = Debug;
		};
		OBJ_623 /* Release */ = {
			isa = XCBuildConfiguration;
			buildSettings = {
				ENABLE_TESTABILITY = YES;
				FRAMEWORK_SEARCH_PATHS = (
					"$(inherited)",
					"$(PLATFORM_DIR)/Developer/Library/Frameworks",
				);
				HEADER_SEARCH_PATHS = (
					"$(inherited)",
					"$(SRCROOT)/.build/checkouts/CommonCrypto.git-1219305460334093717",
					"$(SRCROOT)/.build/checkouts/Kitura-net.git--7410958935072501107/Sources/CHTTPParser/include",
					"$(SRCROOT)/.build/checkouts/CCurl.git-8026296523752779197",
					"$(SRCROOT)/mikrotik_router_manager.xcodeproj/GeneratedModuleMap/CHTTPParser",
				);
				INFOPLIST_FILE = mikrotik_router_manager.xcodeproj/CredentialsHTTP_Info.plist;
				LD_RUNPATH_SEARCH_PATHS = "$(TOOLCHAIN_DIR)/usr/lib/swift/macosx";
				OTHER_LDFLAGS = "$(inherited)";
				OTHER_SWIFT_FLAGS = "$(inherited) -Xcc -fmodule-map-file=$(SRCROOT)/mikrotik_router_manager.xcodeproj/GeneratedModuleMap/CHTTPParser/module.modulemap";
				PRODUCT_BUNDLE_IDENTIFIER = CredentialsHTTP;
				PRODUCT_MODULE_NAME = "$(TARGET_NAME:c99extidentifier)";
				PRODUCT_NAME = "$(TARGET_NAME:c99extidentifier)";
				SKIP_INSTALL = YES;
				SWIFT_VERSION = 3.0;
				TARGET_NAME = CredentialsHTTP;
			};
			name = Release;
		};
		OBJ_653 /* Debug */ = {
			isa = XCBuildConfiguration;
			buildSettings = {
				ENABLE_TESTABILITY = YES;
				FRAMEWORK_SEARCH_PATHS = (
					"$(inherited)",
					"$(PLATFORM_DIR)/Developer/Library/Frameworks",
				);
				HEADER_SEARCH_PATHS = (
					"$(inherited)",
					"$(SRCROOT)/.build/checkouts/CommonCrypto.git-1219305460334093717",
					"$(SRCROOT)/.build/checkouts/Kitura-net.git--7410958935072501107/Sources/CHTTPParser/include",
					"$(SRCROOT)/.build/checkouts/CCurl.git-8026296523752779197",
					"$(SRCROOT)/mikrotik_router_manager.xcodeproj/GeneratedModuleMap/CHTTPParser",
				);
				INFOPLIST_FILE = mikrotik_router_manager.xcodeproj/Credentials_Info.plist;
				LD_RUNPATH_SEARCH_PATHS = "$(TOOLCHAIN_DIR)/usr/lib/swift/macosx";
				OTHER_LDFLAGS = "$(inherited)";
				OTHER_SWIFT_FLAGS = "$(inherited) -Xcc -fmodule-map-file=$(SRCROOT)/mikrotik_router_manager.xcodeproj/GeneratedModuleMap/CHTTPParser/module.modulemap";
				PRODUCT_BUNDLE_IDENTIFIER = Credentials;
				PRODUCT_MODULE_NAME = "$(TARGET_NAME:c99extidentifier)";
				PRODUCT_NAME = "$(TARGET_NAME:c99extidentifier)";
				SKIP_INSTALL = YES;
				SWIFT_VERSION = 3.0;
				TARGET_NAME = Credentials;
			};
			name = Debug;
		};
		OBJ_654 /* Release */ = {
			isa = XCBuildConfiguration;
			buildSettings = {
				ENABLE_TESTABILITY = YES;
				FRAMEWORK_SEARCH_PATHS = (
					"$(inherited)",
					"$(PLATFORM_DIR)/Developer/Library/Frameworks",
				);
				HEADER_SEARCH_PATHS = (
					"$(inherited)",
					"$(SRCROOT)/.build/checkouts/CommonCrypto.git-1219305460334093717",
					"$(SRCROOT)/.build/checkouts/Kitura-net.git--7410958935072501107/Sources/CHTTPParser/include",
					"$(SRCROOT)/.build/checkouts/CCurl.git-8026296523752779197",
					"$(SRCROOT)/mikrotik_router_manager.xcodeproj/GeneratedModuleMap/CHTTPParser",
				);
				INFOPLIST_FILE = mikrotik_router_manager.xcodeproj/Credentials_Info.plist;
				LD_RUNPATH_SEARCH_PATHS = "$(TOOLCHAIN_DIR)/usr/lib/swift/macosx";
				OTHER_LDFLAGS = "$(inherited)";
				OTHER_SWIFT_FLAGS = "$(inherited) -Xcc -fmodule-map-file=$(SRCROOT)/mikrotik_router_manager.xcodeproj/GeneratedModuleMap/CHTTPParser/module.modulemap";
				PRODUCT_BUNDLE_IDENTIFIER = Credentials;
				PRODUCT_MODULE_NAME = "$(TARGET_NAME:c99extidentifier)";
				PRODUCT_NAME = "$(TARGET_NAME:c99extidentifier)";
				SKIP_INSTALL = YES;
				SWIFT_VERSION = 3.0;
				TARGET_NAME = Credentials;
			};
			name = Release;
		};
		OBJ_684 /* Debug */ = {
			isa = XCBuildConfiguration;
			buildSettings = {
				ENABLE_TESTABILITY = YES;
				FRAMEWORK_SEARCH_PATHS = (
					"$(inherited)",
					"$(PLATFORM_DIR)/Developer/Library/Frameworks",
				);
				HEADER_SEARCH_PATHS = (
					"$(inherited)",
					"$(SRCROOT)/.build/checkouts/CommonCrypto.git-1219305460334093717",
					"$(SRCROOT)/.build/checkouts/Kitura-net.git--7410958935072501107/Sources/CHTTPParser/include",
					"$(SRCROOT)/.build/checkouts/CCurl.git-8026296523752779197",
					"$(SRCROOT)/mikrotik_router_manager.xcodeproj/GeneratedModuleMap/CHTTPParser",
				);
				INFOPLIST_FILE = mikrotik_router_manager.xcodeproj/KituraSession_Info.plist;
				LD_RUNPATH_SEARCH_PATHS = "$(TOOLCHAIN_DIR)/usr/lib/swift/macosx";
				OTHER_LDFLAGS = "$(inherited)";
				OTHER_SWIFT_FLAGS = "$(inherited) -Xcc -fmodule-map-file=$(SRCROOT)/mikrotik_router_manager.xcodeproj/GeneratedModuleMap/CHTTPParser/module.modulemap";
				PRODUCT_BUNDLE_IDENTIFIER = KituraSession;
				PRODUCT_MODULE_NAME = "$(TARGET_NAME:c99extidentifier)";
				PRODUCT_NAME = "$(TARGET_NAME:c99extidentifier)";
				SKIP_INSTALL = YES;
				SWIFT_VERSION = 3.0;
				TARGET_NAME = KituraSession;
			};
			name = Debug;
		};
		OBJ_685 /* Release */ = {
			isa = XCBuildConfiguration;
			buildSettings = {
				ENABLE_TESTABILITY = YES;
				FRAMEWORK_SEARCH_PATHS = (
					"$(inherited)",
					"$(PLATFORM_DIR)/Developer/Library/Frameworks",
				);
				HEADER_SEARCH_PATHS = (
					"$(inherited)",
					"$(SRCROOT)/.build/checkouts/CommonCrypto.git-1219305460334093717",
					"$(SRCROOT)/.build/checkouts/Kitura-net.git--7410958935072501107/Sources/CHTTPParser/include",
					"$(SRCROOT)/.build/checkouts/CCurl.git-8026296523752779197",
					"$(SRCROOT)/mikrotik_router_manager.xcodeproj/GeneratedModuleMap/CHTTPParser",
				);
				INFOPLIST_FILE = mikrotik_router_manager.xcodeproj/KituraSession_Info.plist;
				LD_RUNPATH_SEARCH_PATHS = "$(TOOLCHAIN_DIR)/usr/lib/swift/macosx";
				OTHER_LDFLAGS = "$(inherited)";
				OTHER_SWIFT_FLAGS = "$(inherited) -Xcc -fmodule-map-file=$(SRCROOT)/mikrotik_router_manager.xcodeproj/GeneratedModuleMap/CHTTPParser/module.modulemap";
				PRODUCT_BUNDLE_IDENTIFIER = KituraSession;
				PRODUCT_MODULE_NAME = "$(TARGET_NAME:c99extidentifier)";
				PRODUCT_NAME = "$(TARGET_NAME:c99extidentifier)";
				SKIP_INSTALL = YES;
				SWIFT_VERSION = 3.0;
				TARGET_NAME = KituraSession;
			};
			name = Release;
		};
		OBJ_715 /* Debug */ = {
			isa = XCBuildConfiguration;
			buildSettings = {
				ENABLE_TESTABILITY = YES;
				FRAMEWORK_SEARCH_PATHS = (
					"$(inherited)",
					"$(PLATFORM_DIR)/Developer/Library/Frameworks",
				);
				HEADER_SEARCH_PATHS = (
					"$(inherited)",
					"$(SRCROOT)/.build/checkouts/CommonCrypto.git-1219305460334093717",
				);
				INFOPLIST_FILE = mikrotik_router_manager.xcodeproj/Cryptor_Info.plist;
				LD_RUNPATH_SEARCH_PATHS = "$(TOOLCHAIN_DIR)/usr/lib/swift/macosx";
				OTHER_LDFLAGS = "$(inherited)";
				OTHER_SWIFT_FLAGS = "$(inherited)";
				PRODUCT_BUNDLE_IDENTIFIER = Cryptor;
				PRODUCT_MODULE_NAME = "$(TARGET_NAME:c99extidentifier)";
				PRODUCT_NAME = "$(TARGET_NAME:c99extidentifier)";
				SKIP_INSTALL = YES;
				SWIFT_VERSION = 4.0;
				TARGET_NAME = Cryptor;
			};
			name = Debug;
		};
		OBJ_716 /* Release */ = {
			isa = XCBuildConfiguration;
			buildSettings = {
				ENABLE_TESTABILITY = YES;
				FRAMEWORK_SEARCH_PATHS = (
					"$(inherited)",
					"$(PLATFORM_DIR)/Developer/Library/Frameworks",
				);
				HEADER_SEARCH_PATHS = (
					"$(inherited)",
					"$(SRCROOT)/.build/checkouts/CommonCrypto.git-1219305460334093717",
				);
				INFOPLIST_FILE = mikrotik_router_manager.xcodeproj/Cryptor_Info.plist;
				LD_RUNPATH_SEARCH_PATHS = "$(TOOLCHAIN_DIR)/usr/lib/swift/macosx";
				OTHER_LDFLAGS = "$(inherited)";
				OTHER_SWIFT_FLAGS = "$(inherited)";
				PRODUCT_BUNDLE_IDENTIFIER = Cryptor;
				PRODUCT_MODULE_NAME = "$(TARGET_NAME:c99extidentifier)";
				PRODUCT_NAME = "$(TARGET_NAME:c99extidentifier)";
				SKIP_INSTALL = YES;
				SWIFT_VERSION = 4.0;
				TARGET_NAME = Cryptor;
			};
			name = Release;
		};
		OBJ_730 /* Debug */ = {
			isa = XCBuildConfiguration;
			buildSettings = {
				ENABLE_TESTABILITY = YES;
				FRAMEWORK_SEARCH_PATHS = (
					"$(inherited)",
					"$(PLATFORM_DIR)/Developer/Library/Frameworks",
				);
				HEADER_SEARCH_PATHS = (
					"$(inherited)",
					"$(SRCROOT)/.build/checkouts/Kitura-net.git--7410958935072501107/Sources/CHTTPParser/include",
					"$(SRCROOT)/.build/checkouts/CCurl.git-8026296523752779197",
					"$(SRCROOT)/mikrotik_router_manager.xcodeproj/GeneratedModuleMap/CHTTPParser",
				);
				INFOPLIST_FILE = mikrotik_router_manager.xcodeproj/Kitura_Info.plist;
				LD_RUNPATH_SEARCH_PATHS = "$(TOOLCHAIN_DIR)/usr/lib/swift/macosx";
				OTHER_LDFLAGS = "$(inherited)";
				OTHER_SWIFT_FLAGS = "$(inherited) -Xcc -fmodule-map-file=$(SRCROOT)/mikrotik_router_manager.xcodeproj/GeneratedModuleMap/CHTTPParser/module.modulemap";
				PRODUCT_BUNDLE_IDENTIFIER = Kitura;
				PRODUCT_MODULE_NAME = "$(TARGET_NAME:c99extidentifier)";
				PRODUCT_NAME = "$(TARGET_NAME:c99extidentifier)";
				SKIP_INSTALL = YES;
				SWIFT_VERSION = 4.0;
				TARGET_NAME = Kitura;
			};
			name = Debug;
		};
		OBJ_731 /* Release */ = {
			isa = XCBuildConfiguration;
			buildSettings = {
				ENABLE_TESTABILITY = YES;
				FRAMEWORK_SEARCH_PATHS = (
					"$(inherited)",
					"$(PLATFORM_DIR)/Developer/Library/Frameworks",
				);
				HEADER_SEARCH_PATHS = (
					"$(inherited)",
					"$(SRCROOT)/.build/checkouts/Kitura-net.git--7410958935072501107/Sources/CHTTPParser/include",
					"$(SRCROOT)/.build/checkouts/CCurl.git-8026296523752779197",
					"$(SRCROOT)/mikrotik_router_manager.xcodeproj/GeneratedModuleMap/CHTTPParser",
				);
				INFOPLIST_FILE = mikrotik_router_manager.xcodeproj/Kitura_Info.plist;
				LD_RUNPATH_SEARCH_PATHS = "$(TOOLCHAIN_DIR)/usr/lib/swift/macosx";
				OTHER_LDFLAGS = "$(inherited)";
				OTHER_SWIFT_FLAGS = "$(inherited) -Xcc -fmodule-map-file=$(SRCROOT)/mikrotik_router_manager.xcodeproj/GeneratedModuleMap/CHTTPParser/module.modulemap";
				PRODUCT_BUNDLE_IDENTIFIER = Kitura;
				PRODUCT_MODULE_NAME = "$(TARGET_NAME:c99extidentifier)";
				PRODUCT_NAME = "$(TARGET_NAME:c99extidentifier)";
				SKIP_INSTALL = YES;
				SWIFT_VERSION = 4.0;
				TARGET_NAME = Kitura;
			};
			name = Release;
		};
		OBJ_793 /* Debug */ = {
			isa = XCBuildConfiguration;
			buildSettings = {
				ENABLE_TESTABILITY = YES;
				FRAMEWORK_SEARCH_PATHS = (
					"$(inherited)",
					"$(PLATFORM_DIR)/Developer/Library/Frameworks",
				);
				HEADER_SEARCH_PATHS = "$(inherited)";
				INFOPLIST_FILE = mikrotik_router_manager.xcodeproj/KituraTemplateEngine_Info.plist;
				LD_RUNPATH_SEARCH_PATHS = "$(TOOLCHAIN_DIR)/usr/lib/swift/macosx";
				OTHER_LDFLAGS = "$(inherited)";
				OTHER_SWIFT_FLAGS = "$(inherited)";
				PRODUCT_BUNDLE_IDENTIFIER = KituraTemplateEngine;
				PRODUCT_MODULE_NAME = "$(TARGET_NAME:c99extidentifier)";
				PRODUCT_NAME = "$(TARGET_NAME:c99extidentifier)";
				SKIP_INSTALL = YES;
				SWIFT_VERSION = 4.0;
				TARGET_NAME = KituraTemplateEngine;
			};
			name = Debug;
		};
		OBJ_794 /* Release */ = {
			isa = XCBuildConfiguration;
			buildSettings = {
				ENABLE_TESTABILITY = YES;
				FRAMEWORK_SEARCH_PATHS = (
					"$(inherited)",
					"$(PLATFORM_DIR)/Developer/Library/Frameworks",
				);
				HEADER_SEARCH_PATHS = "$(inherited)";
				INFOPLIST_FILE = mikrotik_router_manager.xcodeproj/KituraTemplateEngine_Info.plist;
				LD_RUNPATH_SEARCH_PATHS = "$(TOOLCHAIN_DIR)/usr/lib/swift/macosx";
				OTHER_LDFLAGS = "$(inherited)";
				OTHER_SWIFT_FLAGS = "$(inherited)";
				PRODUCT_BUNDLE_IDENTIFIER = KituraTemplateEngine;
				PRODUCT_MODULE_NAME = "$(TARGET_NAME:c99extidentifier)";
				PRODUCT_NAME = "$(TARGET_NAME:c99extidentifier)";
				SKIP_INSTALL = YES;
				SWIFT_VERSION = 4.0;
				TARGET_NAME = KituraTemplateEngine;
			};
			name = Release;
		};
		OBJ_799 /* Debug */ = {
			isa = XCBuildConfiguration;
			buildSettings = {
				ENABLE_TESTABILITY = YES;
				FRAMEWORK_SEARCH_PATHS = (
					"$(inherited)",
					"$(PLATFORM_DIR)/Developer/Library/Frameworks",
				);
				HEADER_SEARCH_PATHS = "$(inherited)";
				INFOPLIST_FILE = mikrotik_router_manager.xcodeproj/SwiftyJSON_Info.plist;
				LD_RUNPATH_SEARCH_PATHS = "$(TOOLCHAIN_DIR)/usr/lib/swift/macosx";
				OTHER_LDFLAGS = "$(inherited)";
				OTHER_SWIFT_FLAGS = "$(inherited)";
				PRODUCT_BUNDLE_IDENTIFIER = SwiftyJSON;
				PRODUCT_MODULE_NAME = "$(TARGET_NAME:c99extidentifier)";
				PRODUCT_NAME = "$(TARGET_NAME:c99extidentifier)";
				SKIP_INSTALL = YES;
				SWIFT_VERSION = 4.0;
				TARGET_NAME = SwiftyJSON;
			};
			name = Debug;
		};
		OBJ_800 /* Release */ = {
			isa = XCBuildConfiguration;
			buildSettings = {
				ENABLE_TESTABILITY = YES;
				FRAMEWORK_SEARCH_PATHS = (
					"$(inherited)",
					"$(PLATFORM_DIR)/Developer/Library/Frameworks",
				);
				HEADER_SEARCH_PATHS = "$(inherited)";
				INFOPLIST_FILE = mikrotik_router_manager.xcodeproj/SwiftyJSON_Info.plist;
				LD_RUNPATH_SEARCH_PATHS = "$(TOOLCHAIN_DIR)/usr/lib/swift/macosx";
				OTHER_LDFLAGS = "$(inherited)";
				OTHER_SWIFT_FLAGS = "$(inherited)";
				PRODUCT_BUNDLE_IDENTIFIER = SwiftyJSON;
				PRODUCT_MODULE_NAME = "$(TARGET_NAME:c99extidentifier)";
				PRODUCT_NAME = "$(TARGET_NAME:c99extidentifier)";
				SKIP_INSTALL = YES;
				SWIFT_VERSION = 4.0;
				TARGET_NAME = SwiftyJSON;
			};
			name = Release;
		};
		OBJ_806 /* Debug */ = {
			isa = XCBuildConfiguration;
			buildSettings = {
				ENABLE_TESTABILITY = YES;
				FRAMEWORK_SEARCH_PATHS = (
					"$(inherited)",
					"$(PLATFORM_DIR)/Developer/Library/Frameworks",
				);
				HEADER_SEARCH_PATHS = (
					"$(inherited)",
					"$(SRCROOT)/.build/checkouts/Kitura-net.git--7410958935072501107/Sources/CHTTPParser/include",
					"$(SRCROOT)/.build/checkouts/CCurl.git-8026296523752779197",
					"$(SRCROOT)/mikrotik_router_manager.xcodeproj/GeneratedModuleMap/CHTTPParser",
				);
				INFOPLIST_FILE = mikrotik_router_manager.xcodeproj/KituraNet_Info.plist;
				LD_RUNPATH_SEARCH_PATHS = "$(TOOLCHAIN_DIR)/usr/lib/swift/macosx";
				OTHER_LDFLAGS = "$(inherited)";
				OTHER_SWIFT_FLAGS = "$(inherited) -Xcc -fmodule-map-file=$(SRCROOT)/mikrotik_router_manager.xcodeproj/GeneratedModuleMap/CHTTPParser/module.modulemap";
				PRODUCT_BUNDLE_IDENTIFIER = KituraNet;
				PRODUCT_MODULE_NAME = "$(TARGET_NAME:c99extidentifier)";
				PRODUCT_NAME = "$(TARGET_NAME:c99extidentifier)";
				SKIP_INSTALL = YES;
				SWIFT_VERSION = 4.0;
				TARGET_NAME = KituraNet;
			};
			name = Debug;
		};
		OBJ_807 /* Release */ = {
			isa = XCBuildConfiguration;
			buildSettings = {
				ENABLE_TESTABILITY = YES;
				FRAMEWORK_SEARCH_PATHS = (
					"$(inherited)",
					"$(PLATFORM_DIR)/Developer/Library/Frameworks",
				);
				HEADER_SEARCH_PATHS = (
					"$(inherited)",
					"$(SRCROOT)/.build/checkouts/Kitura-net.git--7410958935072501107/Sources/CHTTPParser/include",
					"$(SRCROOT)/.build/checkouts/CCurl.git-8026296523752779197",
					"$(SRCROOT)/mikrotik_router_manager.xcodeproj/GeneratedModuleMap/CHTTPParser",
				);
				INFOPLIST_FILE = mikrotik_router_manager.xcodeproj/KituraNet_Info.plist;
				LD_RUNPATH_SEARCH_PATHS = "$(TOOLCHAIN_DIR)/usr/lib/swift/macosx";
				OTHER_LDFLAGS = "$(inherited)";
				OTHER_SWIFT_FLAGS = "$(inherited) -Xcc -fmodule-map-file=$(SRCROOT)/mikrotik_router_manager.xcodeproj/GeneratedModuleMap/CHTTPParser/module.modulemap";
				PRODUCT_BUNDLE_IDENTIFIER = KituraNet;
				PRODUCT_MODULE_NAME = "$(TARGET_NAME:c99extidentifier)";
				PRODUCT_NAME = "$(TARGET_NAME:c99extidentifier)";
				SKIP_INSTALL = YES;
				SWIFT_VERSION = 4.0;
				TARGET_NAME = KituraNet;
			};
			name = Release;
		};
		OBJ_855 /* Debug */ = {
			isa = XCBuildConfiguration;
			buildSettings = {
				ENABLE_TESTABILITY = YES;
				FRAMEWORK_SEARCH_PATHS = (
					"$(inherited)",
					"$(PLATFORM_DIR)/Developer/Library/Frameworks",
				);
				HEADER_SEARCH_PATHS = "$(inherited)";
				INFOPLIST_FILE = mikrotik_router_manager.xcodeproj/SSLService_Info.plist;
				LD_RUNPATH_SEARCH_PATHS = "$(TOOLCHAIN_DIR)/usr/lib/swift/macosx";
				OTHER_LDFLAGS = "$(inherited)";
				OTHER_SWIFT_FLAGS = "$(inherited)";
				PRODUCT_BUNDLE_IDENTIFIER = SSLService;
				PRODUCT_MODULE_NAME = "$(TARGET_NAME:c99extidentifier)";
				PRODUCT_NAME = "$(TARGET_NAME:c99extidentifier)";
				SKIP_INSTALL = YES;
				SWIFT_VERSION = 4.0;
				TARGET_NAME = SSLService;
			};
			name = Debug;
		};
		OBJ_856 /* Release */ = {
			isa = XCBuildConfiguration;
			buildSettings = {
				ENABLE_TESTABILITY = YES;
				FRAMEWORK_SEARCH_PATHS = (
					"$(inherited)",
					"$(PLATFORM_DIR)/Developer/Library/Frameworks",
				);
				HEADER_SEARCH_PATHS = "$(inherited)";
				INFOPLIST_FILE = mikrotik_router_manager.xcodeproj/SSLService_Info.plist;
				LD_RUNPATH_SEARCH_PATHS = "$(TOOLCHAIN_DIR)/usr/lib/swift/macosx";
				OTHER_LDFLAGS = "$(inherited)";
				OTHER_SWIFT_FLAGS = "$(inherited)";
				PRODUCT_BUNDLE_IDENTIFIER = SSLService;
				PRODUCT_MODULE_NAME = "$(TARGET_NAME:c99extidentifier)";
				PRODUCT_NAME = "$(TARGET_NAME:c99extidentifier)";
				SKIP_INSTALL = YES;
				SWIFT_VERSION = 4.0;
				TARGET_NAME = SSLService;
			};
			name = Release;
		};
		OBJ_863 /* Debug */ = {
			isa = XCBuildConfiguration;
			buildSettings = {
				DEFINES_MODULE = NO;
				ENABLE_TESTABILITY = YES;
				FRAMEWORK_SEARCH_PATHS = (
					"$(inherited)",
					"$(PLATFORM_DIR)/Developer/Library/Frameworks",
				);
				HEADER_SEARCH_PATHS = (
					"$(inherited)",
					"$(SRCROOT)/.build/checkouts/Kitura-net.git--7410958935072501107/Sources/CHTTPParser/include",
					"$(SRCROOT)/.build/checkouts/CCurl.git-8026296523752779197",
				);
				INFOPLIST_FILE = mikrotik_router_manager.xcodeproj/CHTTPParser_Info.plist;
				LD_RUNPATH_SEARCH_PATHS = "$(TOOLCHAIN_DIR)/usr/lib/swift/macosx";
				OTHER_LDFLAGS = "$(inherited)";
				OTHER_SWIFT_FLAGS = "$(inherited)";
				PRODUCT_BUNDLE_IDENTIFIER = CHTTPParser;
				PRODUCT_MODULE_NAME = "$(TARGET_NAME:c99extidentifier)";
				PRODUCT_NAME = "$(TARGET_NAME:c99extidentifier)";
				SKIP_INSTALL = YES;
				TARGET_NAME = CHTTPParser;
			};
			name = Debug;
		};
		OBJ_864 /* Release */ = {
			isa = XCBuildConfiguration;
			buildSettings = {
				DEFINES_MODULE = NO;
				ENABLE_TESTABILITY = YES;
				FRAMEWORK_SEARCH_PATHS = (
					"$(inherited)",
					"$(PLATFORM_DIR)/Developer/Library/Frameworks",
				);
				HEADER_SEARCH_PATHS = (
					"$(inherited)",
					"$(SRCROOT)/.build/checkouts/Kitura-net.git--7410958935072501107/Sources/CHTTPParser/include",
					"$(SRCROOT)/.build/checkouts/CCurl.git-8026296523752779197",
				);
				INFOPLIST_FILE = mikrotik_router_manager.xcodeproj/CHTTPParser_Info.plist;
				LD_RUNPATH_SEARCH_PATHS = "$(TOOLCHAIN_DIR)/usr/lib/swift/macosx";
				OTHER_LDFLAGS = "$(inherited)";
				OTHER_SWIFT_FLAGS = "$(inherited)";
				PRODUCT_BUNDLE_IDENTIFIER = CHTTPParser;
				PRODUCT_MODULE_NAME = "$(TARGET_NAME:c99extidentifier)";
				PRODUCT_NAME = "$(TARGET_NAME:c99extidentifier)";
				SKIP_INSTALL = YES;
				TARGET_NAME = CHTTPParser;
			};
			name = Release;
		};
		OBJ_870 /* Debug */ = {
			isa = XCBuildConfiguration;
			buildSettings = {
				ENABLE_TESTABILITY = YES;
				FRAMEWORK_SEARCH_PATHS = (
					"$(inherited)",
					"$(PLATFORM_DIR)/Developer/Library/Frameworks",
				);
				HEADER_SEARCH_PATHS = (
					"$(inherited)",
					"$(SRCROOT)/.build/checkouts/CMySQL.git-3001417495195486492",
				);
				INFOPLIST_FILE = mikrotik_router_manager.xcodeproj/SwiftKueryMySQL_Info.plist;
				LD_RUNPATH_SEARCH_PATHS = "$(TOOLCHAIN_DIR)/usr/lib/swift/macosx";
				OTHER_LDFLAGS = "$(inherited)";
				OTHER_SWIFT_FLAGS = "$(inherited)";
				PRODUCT_BUNDLE_IDENTIFIER = SwiftKueryMySQL;
				PRODUCT_MODULE_NAME = "$(TARGET_NAME:c99extidentifier)";
				PRODUCT_NAME = "$(TARGET_NAME:c99extidentifier)";
				SKIP_INSTALL = YES;
				SWIFT_VERSION = 3.0;
				TARGET_NAME = SwiftKueryMySQL;
			};
			name = Debug;
		};
		OBJ_871 /* Release */ = {
			isa = XCBuildConfiguration;
			buildSettings = {
				ENABLE_TESTABILITY = YES;
				FRAMEWORK_SEARCH_PATHS = (
					"$(inherited)",
					"$(PLATFORM_DIR)/Developer/Library/Frameworks",
				);
				HEADER_SEARCH_PATHS = (
					"$(inherited)",
					"$(SRCROOT)/.build/checkouts/CMySQL.git-3001417495195486492",
				);
				INFOPLIST_FILE = mikrotik_router_manager.xcodeproj/SwiftKueryMySQL_Info.plist;
				LD_RUNPATH_SEARCH_PATHS = "$(TOOLCHAIN_DIR)/usr/lib/swift/macosx";
				OTHER_LDFLAGS = "$(inherited)";
				OTHER_SWIFT_FLAGS = "$(inherited)";
				PRODUCT_BUNDLE_IDENTIFIER = SwiftKueryMySQL;
				PRODUCT_MODULE_NAME = "$(TARGET_NAME:c99extidentifier)";
				PRODUCT_NAME = "$(TARGET_NAME:c99extidentifier)";
				SKIP_INSTALL = YES;
				SWIFT_VERSION = 3.0;
				TARGET_NAME = SwiftKueryMySQL;
			};
			name = Release;
		};
		OBJ_881 /* Debug */ = {
			isa = XCBuildConfiguration;
			buildSettings = {
				ENABLE_TESTABILITY = YES;
				FRAMEWORK_SEARCH_PATHS = (
					"$(inherited)",
					"$(PLATFORM_DIR)/Developer/Library/Frameworks",
				);
				HEADER_SEARCH_PATHS = "$(inherited)";
				INFOPLIST_FILE = mikrotik_router_manager.xcodeproj/SwiftKuery_Info.plist;
				LD_RUNPATH_SEARCH_PATHS = "$(TOOLCHAIN_DIR)/usr/lib/swift/macosx";
				OTHER_LDFLAGS = "$(inherited)";
				OTHER_SWIFT_FLAGS = "$(inherited)";
				PRODUCT_BUNDLE_IDENTIFIER = SwiftKuery;
				PRODUCT_MODULE_NAME = "$(TARGET_NAME:c99extidentifier)";
				PRODUCT_NAME = "$(TARGET_NAME:c99extidentifier)";
				SKIP_INSTALL = YES;
				SWIFT_VERSION = 4.0;
				TARGET_NAME = SwiftKuery;
			};
			name = Debug;
		};
		OBJ_882 /* Release */ = {
			isa = XCBuildConfiguration;
			buildSettings = {
				ENABLE_TESTABILITY = YES;
				FRAMEWORK_SEARCH_PATHS = (
					"$(inherited)",
					"$(PLATFORM_DIR)/Developer/Library/Frameworks",
				);
				HEADER_SEARCH_PATHS = "$(inherited)";
				INFOPLIST_FILE = mikrotik_router_manager.xcodeproj/SwiftKuery_Info.plist;
				LD_RUNPATH_SEARCH_PATHS = "$(TOOLCHAIN_DIR)/usr/lib/swift/macosx";
				OTHER_LDFLAGS = "$(inherited)";
				OTHER_SWIFT_FLAGS = "$(inherited)";
				PRODUCT_BUNDLE_IDENTIFIER = SwiftKuery;
				PRODUCT_MODULE_NAME = "$(TARGET_NAME:c99extidentifier)";
				PRODUCT_NAME = "$(TARGET_NAME:c99extidentifier)";
				SKIP_INSTALL = YES;
				SWIFT_VERSION = 4.0;
				TARGET_NAME = SwiftKuery;
			};
			name = Release;
		};
		OBJ_934 /* Debug */ = {
			isa = XCBuildConfiguration;
			buildSettings = {
				ENABLE_TESTABILITY = YES;
				FRAMEWORK_SEARCH_PATHS = (
					"$(inherited)",
					"$(PLATFORM_DIR)/Developer/Library/Frameworks",
				);
				HEADER_SEARCH_PATHS = "$(inherited)";
				INFOPLIST_FILE = mikrotik_router_manager.xcodeproj/CryptoSwift_Info.plist;
				LD_RUNPATH_SEARCH_PATHS = "$(TOOLCHAIN_DIR)/usr/lib/swift/macosx";
				OTHER_LDFLAGS = "$(inherited)";
				OTHER_SWIFT_FLAGS = "$(inherited)";
				PRODUCT_BUNDLE_IDENTIFIER = CryptoSwift;
				PRODUCT_MODULE_NAME = "$(TARGET_NAME:c99extidentifier)";
				PRODUCT_NAME = "$(TARGET_NAME:c99extidentifier)";
				SKIP_INSTALL = YES;
				SWIFT_VERSION = 4.0;
				TARGET_NAME = CryptoSwift;
			};
			name = Debug;
		};
		OBJ_935 /* Release */ = {
			isa = XCBuildConfiguration;
			buildSettings = {
				ENABLE_TESTABILITY = YES;
				FRAMEWORK_SEARCH_PATHS = (
					"$(inherited)",
					"$(PLATFORM_DIR)/Developer/Library/Frameworks",
				);
				HEADER_SEARCH_PATHS = "$(inherited)";
				INFOPLIST_FILE = mikrotik_router_manager.xcodeproj/CryptoSwift_Info.plist;
				LD_RUNPATH_SEARCH_PATHS = "$(TOOLCHAIN_DIR)/usr/lib/swift/macosx";
				OTHER_LDFLAGS = "$(inherited)";
				OTHER_SWIFT_FLAGS = "$(inherited)";
				PRODUCT_BUNDLE_IDENTIFIER = CryptoSwift;
				PRODUCT_MODULE_NAME = "$(TARGET_NAME:c99extidentifier)";
				PRODUCT_NAME = "$(TARGET_NAME:c99extidentifier)";
				SKIP_INSTALL = YES;
				SWIFT_VERSION = 4.0;
				TARGET_NAME = CryptoSwift;
			};
			name = Release;
		};
/* End XCBuildConfiguration section */

/* Begin XCConfigurationList section */
		OBJ_1000 /* Build configuration list for PBXNativeTarget "Socket" */ = {
			isa = XCConfigurationList;
			buildConfigurations = (
				OBJ_1001 /* Debug */,
				OBJ_1002 /* Release */,
			);
			defaultConfigurationIsVisible = 0;
			defaultConfigurationName = Debug;
		};
		OBJ_1008 /* Build configuration list for PBXNativeTarget "ConfigurationTestExecutable" */ = {
			isa = XCConfigurationList;
			buildConfigurations = (
				OBJ_1009 /* Debug */,
				OBJ_1010 /* Release */,
			);
			defaultConfigurationIsVisible = 0;
			defaultConfigurationName = Debug;
		};
		OBJ_1018 /* Build configuration list for PBXNativeTarget "Configuration" */ = {
			isa = XCConfigurationList;
			buildConfigurations = (
				OBJ_1019 /* Debug */,
				OBJ_1020 /* Release */,
			);
			defaultConfigurationIsVisible = 0;
			defaultConfigurationName = Debug;
		};
		OBJ_1031 /* Build configuration list for PBXNativeTarget "LoggerAPI" */ = {
			isa = XCConfigurationList;
			buildConfigurations = (
				OBJ_1032 /* Debug */,
				OBJ_1033 /* Release */,
			);
			defaultConfigurationIsVisible = 0;
			defaultConfigurationName = Debug;
		};
		OBJ_1038 /* Build configuration list for PBXAggregateTarget "Kitura-CredentialsHTTP" */ = {
			isa = XCConfigurationList;
			buildConfigurations = (
				OBJ_1039 /* Debug */,
				OBJ_1040 /* Release */,
			);
			defaultConfigurationIsVisible = 0;
			defaultConfigurationName = Debug;
		};
		OBJ_1043 /* Build configuration list for PBXAggregateTarget "Kitura-Credentials" */ = {
			isa = XCConfigurationList;
			buildConfigurations = (
				OBJ_1044 /* Debug */,
				OBJ_1045 /* Release */,
			);
			defaultConfigurationIsVisible = 0;
			defaultConfigurationName = Debug;
		};
		OBJ_1048 /* Build configuration list for PBXAggregateTarget "Kitura-Session" */ = {
			isa = XCConfigurationList;
			buildConfigurations = (
				OBJ_1049 /* Debug */,
				OBJ_1050 /* Release */,
			);
			defaultConfigurationIsVisible = 0;
			defaultConfigurationName = Debug;
		};
		OBJ_1053 /* Build configuration list for PBXAggregateTarget "CommonCrypto" */ = {
			isa = XCConfigurationList;
			buildConfigurations = (
				OBJ_1054 /* Debug */,
				OBJ_1055 /* Release */,
			);
			defaultConfigurationIsVisible = 0;
			defaultConfigurationName = Debug;
		};
		OBJ_1057 /* Build configuration list for PBXAggregateTarget "CCurl" */ = {
			isa = XCConfigurationList;
			buildConfigurations = (
				OBJ_1058 /* Debug */,
				OBJ_1059 /* Release */,
			);
			defaultConfigurationIsVisible = 0;
			defaultConfigurationName = Debug;
		};
		OBJ_1061 /* Build configuration list for PBXAggregateTarget "CMySQL" */ = {
			isa = XCConfigurationList;
			buildConfigurations = (
				OBJ_1062 /* Debug */,
				OBJ_1063 /* Release */,
			);
			defaultConfigurationIsVisible = 0;
			defaultConfigurationName = Debug;
		};
		OBJ_2 /* Build configuration list for PBXProject "mikrotik_router_manager" */ = {
			isa = XCConfigurationList;
			buildConfigurations = (
				OBJ_3 /* Debug */,
				OBJ_4 /* Release */,
			);
			defaultConfigurationIsVisible = 0;
			defaultConfigurationName = Debug;
		};
		OBJ_361 /* Build configuration list for PBXNativeTarget "mikrotik_router_managerPackageDescription" */ = {
			isa = XCConfigurationList;
			buildConfigurations = (
				OBJ_362 /* Debug */,
				OBJ_363 /* Release */,
			);
			defaultConfigurationIsVisible = 0;
			defaultConfigurationName = Debug;
		};
		OBJ_367 /* Build configuration list for PBXNativeTarget "KituraCORSPackageDescription" */ = {
			isa = XCConfigurationList;
			buildConfigurations = (
				OBJ_368 /* Debug */,
				OBJ_369 /* Release */,
			);
			defaultConfigurationIsVisible = 0;
			defaultConfigurationName = Debug;
		};
		OBJ_373 /* Build configuration list for PBXNativeTarget "HeliumLoggerPackageDescription" */ = {
			isa = XCConfigurationList;
			buildConfigurations = (
				OBJ_374 /* Debug */,
				OBJ_375 /* Release */,
			);
			defaultConfigurationIsVisible = 0;
			defaultConfigurationName = Debug;
		};
		OBJ_379 /* Build configuration list for PBXNativeTarget "Kitura-CredentialsHTTPPackageDescription" */ = {
			isa = XCConfigurationList;
			buildConfigurations = (
				OBJ_380 /* Debug */,
				OBJ_381 /* Release */,
			);
			defaultConfigurationIsVisible = 0;
			defaultConfigurationName = Debug;
		};
		OBJ_385 /* Build configuration list for PBXNativeTarget "Kitura-CredentialsPackageDescription" */ = {
			isa = XCConfigurationList;
			buildConfigurations = (
				OBJ_386 /* Debug */,
				OBJ_387 /* Release */,
			);
			defaultConfigurationIsVisible = 0;
			defaultConfigurationName = Debug;
		};
		OBJ_391 /* Build configuration list for PBXNativeTarget "Kitura-SessionPackageDescription" */ = {
			isa = XCConfigurationList;
			buildConfigurations = (
				OBJ_392 /* Debug */,
				OBJ_393 /* Release */,
			);
			defaultConfigurationIsVisible = 0;
			defaultConfigurationName = Debug;
		};
		OBJ_397 /* Build configuration list for PBXNativeTarget "CryptorPackageDescription" */ = {
			isa = XCConfigurationList;
			buildConfigurations = (
				OBJ_398 /* Debug */,
				OBJ_399 /* Release */,
			);
			defaultConfigurationIsVisible = 0;
			defaultConfigurationName = Debug;
		};
		OBJ_403 /* Build configuration list for PBXNativeTarget "KituraPackageDescription" */ = {
			isa = XCConfigurationList;
			buildConfigurations = (
				OBJ_404 /* Debug */,
				OBJ_405 /* Release */,
			);
			defaultConfigurationIsVisible = 0;
			defaultConfigurationName = Debug;
		};
		OBJ_409 /* Build configuration list for PBXNativeTarget "Kitura-TemplateEnginePackageDescription" */ = {
			isa = XCConfigurationList;
			buildConfigurations = (
				OBJ_410 /* Debug */,
				OBJ_411 /* Release */,
			);
			defaultConfigurationIsVisible = 0;
			defaultConfigurationName = Debug;
		};
		OBJ_415 /* Build configuration list for PBXNativeTarget "SwiftyJSONPackageDescription" */ = {
			isa = XCConfigurationList;
			buildConfigurations = (
				OBJ_416 /* Debug */,
				OBJ_417 /* Release */,
			);
			defaultConfigurationIsVisible = 0;
			defaultConfigurationName = Debug;
		};
		OBJ_421 /* Build configuration list for PBXNativeTarget "Kitura-netPackageDescription" */ = {
			isa = XCConfigurationList;
			buildConfigurations = (
				OBJ_422 /* Debug */,
				OBJ_423 /* Release */,
			);
			defaultConfigurationIsVisible = 0;
			defaultConfigurationName = Debug;
		};
		OBJ_427 /* Build configuration list for PBXNativeTarget "SSLServicePackageDescription" */ = {
			isa = XCConfigurationList;
			buildConfigurations = (
				OBJ_428 /* Debug */,
				OBJ_429 /* Release */,
			);
			defaultConfigurationIsVisible = 0;
			defaultConfigurationName = Debug;
		};
		OBJ_433 /* Build configuration list for PBXNativeTarget "SwiftKueryMySQLPackageDescription" */ = {
			isa = XCConfigurationList;
			buildConfigurations = (
				OBJ_434 /* Debug */,
				OBJ_435 /* Release */,
			);
			defaultConfigurationIsVisible = 0;
			defaultConfigurationName = Debug;
		};
		OBJ_439 /* Build configuration list for PBXNativeTarget "SwiftKueryPackageDescription" */ = {
			isa = XCConfigurationList;
			buildConfigurations = (
				OBJ_440 /* Debug */,
				OBJ_441 /* Release */,
			);
			defaultConfigurationIsVisible = 0;
			defaultConfigurationName = Debug;
		};
		OBJ_445 /* Build configuration list for PBXNativeTarget "CryptoSwiftPackageDescription" */ = {
			isa = XCConfigurationList;
			buildConfigurations = (
				OBJ_446 /* Debug */,
				OBJ_447 /* Release */,
			);
			defaultConfigurationIsVisible = 0;
			defaultConfigurationName = Debug;
		};
		OBJ_451 /* Build configuration list for PBXNativeTarget "SocketPackageDescription" */ = {
			isa = XCConfigurationList;
			buildConfigurations = (
				OBJ_452 /* Debug */,
				OBJ_453 /* Release */,
			);
			defaultConfigurationIsVisible = 0;
			defaultConfigurationName = Debug;
		};
		OBJ_457 /* Build configuration list for PBXNativeTarget "ConfigurationPackageDescription" */ = {
			isa = XCConfigurationList;
			buildConfigurations = (
				OBJ_458 /* Debug */,
				OBJ_459 /* Release */,
			);
			defaultConfigurationIsVisible = 0;
			defaultConfigurationName = Debug;
		};
		OBJ_463 /* Build configuration list for PBXNativeTarget "LoggerAPIPackageDescription" */ = {
			isa = XCConfigurationList;
			buildConfigurations = (
				OBJ_464 /* Debug */,
				OBJ_465 /* Release */,
			);
			defaultConfigurationIsVisible = 0;
			defaultConfigurationName = Debug;
		};
		OBJ_469 /* Build configuration list for PBXNativeTarget "SERVER" */ = {
			isa = XCConfigurationList;
			buildConfigurations = (
				OBJ_470 /* Debug */,
				OBJ_471 /* Release */,
			);
			defaultConfigurationIsVisible = 0;
			defaultConfigurationName = Debug;
		};
		OBJ_534 /* Build configuration list for PBXNativeTarget "CORE" */ = {
			isa = XCConfigurationList;
			buildConfigurations = (
				OBJ_535 /* Debug */,
				OBJ_536 /* Release */,
			);
			defaultConfigurationIsVisible = 0;
			defaultConfigurationName = Debug;
		};
		OBJ_588 /* Build configuration list for PBXNativeTarget "KituraCORS" */ = {
			isa = XCConfigurationList;
			buildConfigurations = (
				OBJ_589 /* Debug */,
				OBJ_590 /* Release */,
			);
			defaultConfigurationIsVisible = 0;
			defaultConfigurationName = Debug;
		};
		OBJ_612 /* Build configuration list for PBXNativeTarget "HeliumLogger" */ = {
			isa = XCConfigurationList;
			buildConfigurations = (
				OBJ_613 /* Debug */,
				OBJ_614 /* Release */,
			);
			defaultConfigurationIsVisible = 0;
			defaultConfigurationName = Debug;
		};
		OBJ_621 /* Build configuration list for PBXNativeTarget "CredentialsHTTP" */ = {
			isa = XCConfigurationList;
			buildConfigurations = (
				OBJ_622 /* Debug */,
				OBJ_623 /* Release */,
			);
			defaultConfigurationIsVisible = 0;
			defaultConfigurationName = Debug;
		};
		OBJ_652 /* Build configuration list for PBXNativeTarget "Credentials" */ = {
			isa = XCConfigurationList;
			buildConfigurations = (
				OBJ_653 /* Debug */,
				OBJ_654 /* Release */,
			);
			defaultConfigurationIsVisible = 0;
			defaultConfigurationName = Debug;
		};
		OBJ_683 /* Build configuration list for PBXNativeTarget "KituraSession" */ = {
			isa = XCConfigurationList;
			buildConfigurations = (
				OBJ_684 /* Debug */,
				OBJ_685 /* Release */,
			);
			defaultConfigurationIsVisible = 0;
			defaultConfigurationName = Debug;
		};
		OBJ_714 /* Build configuration list for PBXNativeTarget "Cryptor" */ = {
			isa = XCConfigurationList;
			buildConfigurations = (
				OBJ_715 /* Debug */,
				OBJ_716 /* Release */,
			);
			defaultConfigurationIsVisible = 0;
			defaultConfigurationName = Debug;
		};
		OBJ_729 /* Build configuration list for PBXNativeTarget "Kitura" */ = {
			isa = XCConfigurationList;
			buildConfigurations = (
				OBJ_730 /* Debug */,
				OBJ_731 /* Release */,
			);
			defaultConfigurationIsVisible = 0;
			defaultConfigurationName = Debug;
		};
		OBJ_792 /* Build configuration list for PBXNativeTarget "KituraTemplateEngine" */ = {
			isa = XCConfigurationList;
			buildConfigurations = (
				OBJ_793 /* Debug */,
				OBJ_794 /* Release */,
			);
			defaultConfigurationIsVisible = 0;
			defaultConfigurationName = Debug;
		};
		OBJ_798 /* Build configuration list for PBXNativeTarget "SwiftyJSON" */ = {
			isa = XCConfigurationList;
			buildConfigurations = (
				OBJ_799 /* Debug */,
				OBJ_800 /* Release */,
			);
			defaultConfigurationIsVisible = 0;
			defaultConfigurationName = Debug;
		};
		OBJ_805 /* Build configuration list for PBXNativeTarget "KituraNet" */ = {
			isa = XCConfigurationList;
			buildConfigurations = (
				OBJ_806 /* Debug */,
				OBJ_807 /* Release */,
			);
			defaultConfigurationIsVisible = 0;
			defaultConfigurationName = Debug;
		};
		OBJ_854 /* Build configuration list for PBXNativeTarget "SSLService" */ = {
			isa = XCConfigurationList;
			buildConfigurations = (
				OBJ_855 /* Debug */,
				OBJ_856 /* Release */,
			);
			defaultConfigurationIsVisible = 0;
			defaultConfigurationName = Debug;
		};
		OBJ_862 /* Build configuration list for PBXNativeTarget "CHTTPParser" */ = {
			isa = XCConfigurationList;
			buildConfigurations = (
				OBJ_863 /* Debug */,
				OBJ_864 /* Release */,
			);
			defaultConfigurationIsVisible = 0;
			defaultConfigurationName = Debug;
		};
		OBJ_869 /* Build configuration list for PBXNativeTarget "SwiftKueryMySQL" */ = {
			isa = XCConfigurationList;
			buildConfigurations = (
				OBJ_870 /* Debug */,
				OBJ_871 /* Release */,
			);
			defaultConfigurationIsVisible = 0;
			defaultConfigurationName = Debug;
		};
		OBJ_880 /* Build configuration list for PBXNativeTarget "SwiftKuery" */ = {
			isa = XCConfigurationList;
			buildConfigurations = (
				OBJ_881 /* Debug */,
				OBJ_882 /* Release */,
			);
			defaultConfigurationIsVisible = 0;
			defaultConfigurationName = Debug;
		};
		OBJ_933 /* Build configuration list for PBXNativeTarget "CryptoSwift" */ = {
			isa = XCConfigurationList;
			buildConfigurations = (
				OBJ_934 /* Debug */,
				OBJ_935 /* Release */,
			);
			defaultConfigurationIsVisible = 0;
			defaultConfigurationName = Debug;
		};
/* End XCConfigurationList section */
	};
	rootObject = OBJ_1 /* Project object */;
}


File: /mikrotik_router_manager.xcodeproj\project.xcworkspace\contents.xcworkspacedata
<?xml version="1.0" encoding="UTF-8"?>
<Workspace
   version = "1.0">
   <FileRef
      location = "self:">
   </FileRef>
</Workspace>


File: /mikrotik_router_manager.xcodeproj\Socket_Info.plist
<?xml version="1.0" encoding="UTF-8"?>
<plist version="1.0">
<dict>
  <key>CFBundleDevelopmentRegion</key>
  <string>en</string>
  <key>CFBundleExecutable</key>
  <string>$(EXECUTABLE_NAME)</string>
  <key>CFBundleIdentifier</key>
  <string>$(PRODUCT_BUNDLE_IDENTIFIER)</string>
  <key>CFBundleInfoDictionaryVersion</key>
  <string>6.0</string>
  <key>CFBundleName</key>
  <string>$(PRODUCT_NAME)</string>
  <key>CFBundlePackageType</key>
  <string>FMWK</string>
  <key>CFBundleShortVersionString</key>
  <string>1.0</string>
  <key>CFBundleSignature</key>
  <string>????</string>
  <key>CFBundleVersion</key>
  <string>$(CURRENT_PROJECT_VERSION)</string>
  <key>NSPrincipalClass</key>
  <string></string>
</dict>
</plist>


File: /mikrotik_router_manager.xcodeproj\SSLService_Info.plist
<?xml version="1.0" encoding="UTF-8"?>
<plist version="1.0">
<dict>
  <key>CFBundleDevelopmentRegion</key>
  <string>en</string>
  <key>CFBundleExecutable</key>
  <string>$(EXECUTABLE_NAME)</string>
  <key>CFBundleIdentifier</key>
  <string>$(PRODUCT_BUNDLE_IDENTIFIER)</string>
  <key>CFBundleInfoDictionaryVersion</key>
  <string>6.0</string>
  <key>CFBundleName</key>
  <string>$(PRODUCT_NAME)</string>
  <key>CFBundlePackageType</key>
  <string>FMWK</string>
  <key>CFBundleShortVersionString</key>
  <string>1.0</string>
  <key>CFBundleSignature</key>
  <string>????</string>
  <key>CFBundleVersion</key>
  <string>$(CURRENT_PROJECT_VERSION)</string>
  <key>NSPrincipalClass</key>
  <string></string>
</dict>
</plist>


File: /mikrotik_router_manager.xcodeproj\SwiftKueryMySQL_Info.plist
<?xml version="1.0" encoding="UTF-8"?>
<plist version="1.0">
<dict>
  <key>CFBundleDevelopmentRegion</key>
  <string>en</string>
  <key>CFBundleExecutable</key>
  <string>$(EXECUTABLE_NAME)</string>
  <key>CFBundleIdentifier</key>
  <string>$(PRODUCT_BUNDLE_IDENTIFIER)</string>
  <key>CFBundleInfoDictionaryVersion</key>
  <string>6.0</string>
  <key>CFBundleName</key>
  <string>$(PRODUCT_NAME)</string>
  <key>CFBundlePackageType</key>
  <string>FMWK</string>
  <key>CFBundleShortVersionString</key>
  <string>1.0</string>
  <key>CFBundleSignature</key>
  <string>????</string>
  <key>CFBundleVersion</key>
  <string>$(CURRENT_PROJECT_VERSION)</string>
  <key>NSPrincipalClass</key>
  <string></string>
</dict>
</plist>


File: /mikrotik_router_manager.xcodeproj\SwiftKuery_Info.plist
<?xml version="1.0" encoding="UTF-8"?>
<plist version="1.0">
<dict>
  <key>CFBundleDevelopmentRegion</key>
  <string>en</string>
  <key>CFBundleExecutable</key>
  <string>$(EXECUTABLE_NAME)</string>
  <key>CFBundleIdentifier</key>
  <string>$(PRODUCT_BUNDLE_IDENTIFIER)</string>
  <key>CFBundleInfoDictionaryVersion</key>
  <string>6.0</string>
  <key>CFBundleName</key>
  <string>$(PRODUCT_NAME)</string>
  <key>CFBundlePackageType</key>
  <string>FMWK</string>
  <key>CFBundleShortVersionString</key>
  <string>1.0</string>
  <key>CFBundleSignature</key>
  <string>????</string>
  <key>CFBundleVersion</key>
  <string>$(CURRENT_PROJECT_VERSION)</string>
  <key>NSPrincipalClass</key>
  <string></string>
</dict>
</plist>


File: /mikrotik_router_manager.xcodeproj\SwiftyJSON_Info.plist
<?xml version="1.0" encoding="UTF-8"?>
<plist version="1.0">
<dict>
  <key>CFBundleDevelopmentRegion</key>
  <string>en</string>
  <key>CFBundleExecutable</key>
  <string>$(EXECUTABLE_NAME)</string>
  <key>CFBundleIdentifier</key>
  <string>$(PRODUCT_BUNDLE_IDENTIFIER)</string>
  <key>CFBundleInfoDictionaryVersion</key>
  <string>6.0</string>
  <key>CFBundleName</key>
  <string>$(PRODUCT_NAME)</string>
  <key>CFBundlePackageType</key>
  <string>FMWK</string>
  <key>CFBundleShortVersionString</key>
  <string>1.0</string>
  <key>CFBundleSignature</key>
  <string>????</string>
  <key>CFBundleVersion</key>
  <string>$(CURRENT_PROJECT_VERSION)</string>
  <key>NSPrincipalClass</key>
  <string></string>
</dict>
</plist>


File: /mikrotik_router_manager.xcodeproj\xcshareddata\xcschemes\xcschememanagement.plist
<?xml version="1.0" encoding="UTF-8"?>
<plist version="1.0">
<dict>
  <key>SchemeUserState</key>
  <dict>
    <key>mikrotik_router_manager-Package.xcscheme</key>
    <dict></dict>
  </dict>
  <key>SuppressBuildableAutocreation</key>
  <dict></dict>
</dict>
</plist>


File: /Package.pins
{
  "autoPin": true,
  "pins": [
    {
      "package": "CCurl",
      "reason": null,
      "repositoryURL": "https://github.com/IBM-Swift/CCurl.git",
      "version": "0.4.0"
    },
    {
      "package": "CMySQL",
      "reason": null,
      "repositoryURL": "https://github.com/IBM-Swift/CMySQL.git",
      "version": "0.1.1"
    },
    {
      "package": "CommonCrypto",
      "reason": null,
      "repositoryURL": "https://github.com/IBM-Swift/CommonCrypto.git",
      "version": "0.1.4"
    },
    {
      "package": "Configuration",
      "reason": null,
      "repositoryURL": "https://github.com/IBM-Swift/Configuration.git",
      "version": "1.0.1"
    },
    {
      "package": "CryptoSwift",
      "reason": null,
      "repositoryURL": "https://github.com/krzyzanowskim/CryptoSwift.git",
      "version": "0.6.9"
    },
    {
      "package": "Cryptor",
      "reason": null,
      "repositoryURL": "https://github.com/IBM-Swift/BlueCryptor.git",
      "version": "0.8.16"
    },
    {
      "package": "HeliumLogger",
      "reason": null,
      "repositoryURL": "https://github.com/IBM-Swift/HeliumLogger.git",
      "version": "1.7.0"
    },
    {
      "package": "Kitura",
      "reason": null,
      "repositoryURL": "https://github.com/IBM-Swift/Kitura.git",
      "version": "1.7.6"
    },
    {
      "package": "Kitura-Credentials",
      "reason": null,
      "repositoryURL": "https://github.com/IBM-Swift/Kitura-Credentials.git",
      "version": "1.7.2"
    },
    {
      "package": "Kitura-CredentialsHTTP",
      "reason": null,
      "repositoryURL": "https://github.com/IBM-Swift/Kitura-CredentialsHTTP.git",
      "version": "1.8.0"
    },
    {
      "package": "Kitura-Session",
      "reason": null,
      "repositoryURL": "https://github.com/IBM-Swift/Kitura-Session.git",
      "version": "1.7.0"
    },
    {
      "package": "Kitura-TemplateEngine",
      "reason": null,
      "repositoryURL": "https://github.com/IBM-Swift/Kitura-TemplateEngine.git",
      "version": "1.7.1"
    },
    {
      "package": "Kitura-net",
      "reason": null,
      "repositoryURL": "https://github.com/IBM-Swift/Kitura-net.git",
      "version": "1.7.15"
    },
    {
      "package": "KituraCORS",
      "reason": null,
      "repositoryURL": "https://github.com/IBM-Swift/Kitura-CORS.git",
      "version": "1.7.0"
    },
    {
      "package": "LoggerAPI",
      "reason": null,
      "repositoryURL": "https://github.com/IBM-Swift/LoggerAPI.git",
      "version": "1.7.0"
    },
    {
      "package": "SSLService",
      "reason": null,
      "repositoryURL": "https://github.com/IBM-Swift/BlueSSLService.git",
      "version": "0.12.48"
    },
    {
      "package": "Socket",
      "reason": null,
      "repositoryURL": "https://github.com/IBM-Swift/BlueSocket.git",
      "version": "0.12.61"
    },
    {
      "package": "SwiftKuery",
      "reason": null,
      "repositoryURL": "https://github.com/IBM-Swift/Swift-Kuery.git",
      "version": "0.13.2"
    },
    {
      "package": "SwiftKueryMySQL",
      "reason": null,
      "repositoryURL": "https://github.com/IBM-Swift/SwiftKueryMySQL.git",
      "version": "0.13.1"
    },
    {
      "package": "SwiftyJSON",
      "reason": null,
      "repositoryURL": "https://github.com/IBM-Swift/SwiftyJSON.git",
      "version": "16.0.1"
    }
  ],
  "version": 1
}

File: /Package.swift
// swift-tools-version:3.1

import PackageDescription
//swift package -Xlinker -L/usr/local/lib generate-xcodeproj
let package = Package(
    name: "mikrotik_router_manager",
    targets: [Target(name: "SERVER", dependencies:["CORE"]),
              ],
    dependencies: [
        .Package(url: "https://github.com/IBM-Swift/Configuration.git",Version(1,0,1)),
        .Package(url: "https://github.com/IBM-Swift/BlueSocket.git", Version(0,12,61)),
        .Package(url: "https://github.com/krzyzanowskim/CryptoSwift.git",Version(0,7,2)),
        .Package(url: "https://github.com/IBM-Swift/SwiftKueryMySQL.git",Version(0,13,1)),
        .Package(url: "https://github.com/IBM-Swift/Kitura-CredentialsHTTP.git",Version(1,8,0)),
        .Package(url: "https://github.com/IBM-Swift/HeliumLogger.git",Version(1,7,0)),
        .Package(url: "https://github.com/IBM-Swift/Kitura-CORS.git", Version(1,7,0)),
        ]
)


File: /README.md
# mikrotik_router_manager

Mikrotik API for swift running on ubuntu 16.10 or mac osx

https://wiki.mikrotik.com/wiki/Manual:API




BUILD ON MAC OSX

run sh generate-xcodeproj.sh

BUILD ON UBUNTU

thư viện yêu cầu 
  clang , libmysqlclient-dev , openssl


run swift build


File: /server_start.sh
swift build -Xlinker -L/usr/local/lib
.build/x86_64-apple-macosx10.10/debug/SERVER

File: /Sources\CORE\BaseComponent.swift
//
//  BaseComponent.swift
//  mikrotik_router_manager
//
//  Created by dung.nt on 8/21/17.
//
//

import Foundation

public enum ComponentType {
    case None
    case MikrotikAPI
    case DataBase
    case HttpServer
    case Operation
    case Logging
    case Session
    case DataStoreFile
}
public class BaseComponent {
    
    public func componentType() -> ComponentType{
        return .None
    }
   
    public func loadConfig(){
        
    }
    public func start(){
        
    }
}


File: /Sources\CORE\Bitter.swift
//
//  Bitter.swift
//  Bitter
//
//  Created by Umberto Raimondi on 01/02/16.
//  Copyright © 2016 Umberto Raimondi. All rights reserved.
//
// MARK: Int types extensions
/**
 Extension that adds a few additional functionalities to Int:
 - toIntN/toUIntN truncating bit pattern conversions
 - allOnes
 - size
 - Byte indexed subscript
 */
extension Int{
    /// Perform a bit pattern truncating conversion to UInt8
    public var toU8: UInt8{return UInt8(truncatingBitPattern:self)}
    /// Perform a bit pattern truncating conversion to Int8
    public var to8: Int8{return Int8(truncatingBitPattern:self)}
    /// Perform a bit pattern truncating conversion to UInt16
    public var toU16: UInt16{return UInt16(truncatingBitPattern:self)}
    /// Perform a bit pattern truncating conversion to Int16
    public var to16: Int16{return Int16(truncatingBitPattern:self)}
    /// Perform a bit pattern truncating conversion to UInt32
    public var toU32: UInt32{return UInt32(truncatingBitPattern:self)}
    /// Perform a bit pattern truncating conversion to Int32
    public var to32: Int32{return Int32(truncatingBitPattern:self)}
    /// Perform a bit pattern truncating conversion to UInt64
    public var toU64: UInt64{
        return UInt64(self) //No difference if the platform is 32 or 64
    }
    /// Perform a bit pattern truncating conversion to Int64
    public var to64: Int64{
        return Int64(self) //No difference if the platform is 32 or 64
    }
    /// Perform a bit pattern truncating conversion to Int
    public var toInt:Int{return self}
    /// Perform a bit pattern truncating conversion to UInt
    public var toUInt:UInt{return UInt(bitPattern:self)}
    
    /// Returns a Int with all ones
    public static var allOnes:Int{return Int(bitPattern: UInt.max)}
    
    /// Returns the size of this type (number of bytes)
    public static var size:Int{return MemoryLayout<Int>.stride}
    
    
    /// Get bit 0 value
    public var b0:Int{
        if(Int.size == 8){
            return Int(bitPattern: UInt( (self.toU64 & (0x1 << 0)) >> 0 ))
        } else {
            return Int(bitPattern: UInt( (self.toU32 & (0x1 << 0)) >> 0 ))
        }
    }
    /// Set bit 0 and return a new Int
    public func setb0(_ bit:Int)->Int{
        let nv = bit != 0 ? 1 : 0
        if(Int.size == 8){
            return Int(bitPattern: UInt( (self.toU64 & ~(0x1 << 0)) | (nv.toU64 << 0) ))
        } else {
            return Int(bitPattern: UInt( (self.toU32 & ~(0x1 << 0)) | (nv.toU32 << 0) ))
        }
    }
    /// Get bit 1 value
    public var b1:Int{
        if(Int.size == 8){
            return Int(bitPattern: UInt( (self.toU64 & (0x1 << 1)) >> 1 ))
        } else {
            return Int(bitPattern: UInt( (self.toU32 & (0x1 << 1)) >> 1 ))
        }
    }
    /// Set bit 1 and return a new Int
    public func setb1(_ bit:Int)->Int{
        let nv = bit != 0 ? 1 : 0
        if(Int.size == 8){
            return Int(bitPattern: UInt( (self.toU64 & ~(0x1 << 1)) | (nv.toU64 << 1) ))
        } else {
            return Int(bitPattern: UInt( (self.toU32 & ~(0x1 << 1)) | (nv.toU32 << 1) ))
        }
    }
    /// Get bit 2 value
    public var b2:Int{
        if(Int.size == 8){
            return Int(bitPattern: UInt( (self.toU64 & (0x1 << 2)) >> 2 ))
        } else {
            return Int(bitPattern: UInt( (self.toU32 & (0x1 << 2)) >> 2 ))
        }
    }
    /// Set bit 2 and return a new Int
    public func setb2(_ bit:Int)->Int{
        let nv = bit != 0 ? 1 : 0
        if(Int.size == 8){
            return Int(bitPattern: UInt( (self.toU64 & ~(0x1 << 2)) | (nv.toU64 << 2) ))
        } else {
            return Int(bitPattern: UInt( (self.toU32 & ~(0x1 << 2)) | (nv.toU32 << 2) ))
        }
    }
    /// Get bit 3 value
    public var b3:Int{
        if(Int.size == 8){
            return Int(bitPattern: UInt( (self.toU64 & (0x1 << 3)) >> 3 ))
        } else {
            return Int(bitPattern: UInt( (self.toU32 & (0x1 << 3)) >> 3 ))
        }
    }
    /// Set bit 3 and return a new Int
    public func setb3(_ bit:Int)->Int{
        let nv = bit != 0 ? 1 : 0
        if(Int.size == 8){
            return Int(bitPattern: UInt( (self.toU64 & ~(0x1 << 3)) | (nv.toU64 << 3) ))
        } else {
            return Int(bitPattern: UInt( (self.toU32 & ~(0x1 << 3)) | (nv.toU32 << 3) ))
        }
    }
    /// Get bit 4 value
    public var b4:Int{
        if(Int.size == 8){
            return Int(bitPattern: UInt( (self.toU64 & (0x1 << 4)) >> 4 ))
        } else {
            return Int(bitPattern: UInt( (self.toU32 & (0x1 << 4)) >> 4 ))
        }
    }
    /// Set bit 4 and return a new Int
    public func setb4(_ bit:Int)->Int{
        let nv = bit != 0 ? 1 : 0
        if(Int.size == 8){
            return Int(bitPattern: UInt( (self.toU64 & ~(0x1 << 4)) | (nv.toU64 << 4) ))
        } else {
            return Int(bitPattern: UInt( (self.toU32 & ~(0x1 << 4)) | (nv.toU32 << 4) ))
        }
    }
    /// Get bit 5 value
    public var b5:Int{
        if(Int.size == 8){
            return Int(bitPattern: UInt( (self.toU64 & (0x1 << 5)) >> 5 ))
        } else {
            return Int(bitPattern: UInt( (self.toU32 & (0x1 << 5)) >> 5 ))
        }
    }
    /// Set bit 5 and return a new Int
    public func setb5(_ bit:Int)->Int{
        let nv = bit != 0 ? 1 : 0
        if(Int.size == 8){
            return Int(bitPattern: UInt( (self.toU64 & ~(0x1 << 5)) | (nv.toU64 << 5) ))
        } else {
            return Int(bitPattern: UInt( (self.toU32 & ~(0x1 << 5)) | (nv.toU32 << 5) ))
        }
    }
    /// Get bit 6 value
    public var b6:Int{
        if(Int.size == 8){
            return Int(bitPattern: UInt( (self.toU64 & (0x1 << 6)) >> 6 ))
        } else {
            return Int(bitPattern: UInt( (self.toU32 & (0x1 << 6)) >> 6 ))
        }
    }
    /// Set bit 6 and return a new Int
    public func setb6(_ bit:Int)->Int{
        let nv = bit != 0 ? 1 : 0
        if(Int.size == 8){
            return Int(bitPattern: UInt( (self.toU64 & ~(0x1 << 6)) | (nv.toU64 << 6) ))
        } else {
            return Int(bitPattern: UInt( (self.toU32 & ~(0x1 << 6)) | (nv.toU32 << 6) ))
        }
    }
    /// Get bit 7 value
    public var b7:Int{
        if(Int.size == 8){
            return Int(bitPattern: UInt( (self.toU64 & (0x1 << 7)) >> 7 ))
        } else {
            return Int(bitPattern: UInt( (self.toU32 & (0x1 << 7)) >> 7 ))
        }
    }
    /// Set bit 7 and return a new Int
    public func setb7(_ bit:Int)->Int{
        let nv = bit != 0 ? 1 : 0
        if(Int.size == 8){
            return Int(bitPattern: UInt( (self.toU64 & ~(0x1 << 7)) | (nv.toU64 << 7) ))
        } else {
            return Int(bitPattern: UInt( (self.toU32 & ~(0x1 << 7)) | (nv.toU32 << 7) ))
        }
    }
    
    
    /// Subscript that returns or set one of the bytes of a Int
    /// at the given index.
    /// Trying to access an out of index byte will result in an error.
    public subscript(index: Int) -> Int {
        get {
            precondition(index<Int.size,"Byte set index out of range")
            if(Int.size == 8){
                return Int(bitPattern: UInt((self.toU64 & (0xFF << (index.toU64*8))) >> (index.toU64*8)) )
            }else{
                return Int(bitPattern: UInt((self.toU32 & (0xFF << (index.toU32*8))) >> (index.toU32*8)) )
            }
        }
        set(newValue) {
            precondition(index<Int.size,"Byte set index out of range")
            if(Int.size == 8){
                self = Int(bitPattern: UInt((self.toU64 & ~(0xFF << (index.toU64*8))) | (newValue.toU64 << (index.toU64*8))) )
            }else{
                self = Int(bitPattern: UInt((self.toU32 & ~(0xFF << (index.toU32*8))) | (newValue.toU32 << (index.toU32*8))) )
            }
        }
    }
}
/**
 Extension that adds a few additional functionalities to UInt:
 - toIntN/toUIntN truncating bit pattern conversions
 - allOnes
 - size
 - Byte indexed subscript
 */
extension UInt{
    /// Perform a bit pattern truncating conversion to UInt8
    public var toU8: UInt8{return UInt8(truncatingBitPattern:self)}
    /// Perform a bit pattern truncating conversion to Int8
    public var to8: Int8{return Int8(truncatingBitPattern:self)}
    /// Perform a bit pattern truncating conversion to UInt16
    public var toU16: UInt16{return UInt16(truncatingBitPattern:self)}
    /// Perform a bit pattern truncating conversion to Int16
    public var to16: Int16{return Int16(truncatingBitPattern:self)}
    /// Perform a bit pattern truncating conversion to UInt32
    public var toU32: UInt32{return UInt32(truncatingBitPattern:self)}
    /// Perform a bit pattern truncating conversion to Int32
    public var to32: Int32{return Int32(truncatingBitPattern:self)}
    /// Perform a bit pattern truncating conversion to UInt64
    public var toU64: UInt64{
        return UInt64(self) //No difference if the platform is 32 or 64
    }
    /// Perform a bit pattern truncating conversion to Int64
    public var to64: Int64{
        return Int64(self) //No difference if the platform is 32 or 64
    }
    /// Perform a bit pattern truncating conversion to Int
    public var toInt:Int{return Int(bitPattern:self)}
    /// Perform a bit pattern truncating conversion to UInt
    public var toUInt:UInt{return self}
    
    /// Returns a UInt with all ones
    public static var allOnes:UInt{return UInt.max}
    
    /// Returns the size of this type (number of bytes)
    public static var size:Int{return MemoryLayout<UInt>.stride}
    
    
    /// Get bit 0 value
    public var b0:UInt{
        if(Int.size == 8){
            return UInt( (self.toU64 & (0x1 << 0)) >> 0 )
        } else {
            return UInt( (self.toU32 & (0x1 << 0)) >> 0 )
        }
    }
    /// Set bit 0 and return a new UInt
    public func setb0(_ bit:Int)->UInt{
        let nv = bit != 0 ? 1 : 0
        if(Int.size == 8){
            return UInt( (self.toU64 & ~(0x1 << 0)) | (nv.toU64 << 0) )
        } else {
            return UInt( (self.toU32 & ~(0x1 << 0)) | (nv.toU32 << 0) )
        }
    }
    /// Get bit 1 value
    public var b1:UInt{
        if(Int.size == 8){
            return UInt( (self.toU64 & (0x1 << 1)) >> 1 )
        } else {
            return UInt( (self.toU32 & (0x1 << 1)) >> 1 )
        }
    }
    /// Set bit 1 and return a new UInt
    public func setb1(_ bit:Int)->UInt{
        let nv = bit != 0 ? 1 : 0
        if(Int.size == 8){
            return UInt( (self.toU64 & ~(0x1 << 1)) | (nv.toU64 << 1) )
        } else {
            return UInt( (self.toU32 & ~(0x1 << 1)) | (nv.toU32 << 1) )
        }
    }
    /// Get bit 2 value
    public var b2:UInt{
        if(Int.size == 8){
            return UInt( (self.toU64 & (0x1 << 2)) >> 2 )
        } else {
            return UInt( (self.toU32 & (0x1 << 2)) >> 2 )
        }
    }
    /// Set bit 2 and return a new UInt
    public func setb2(_ bit:Int)->UInt{
        let nv = bit != 0 ? 1 : 0
        if(Int.size == 8){
            return UInt( (self.toU64 & ~(0x1 << 2)) | (nv.toU64 << 2) )
        } else {
            return UInt( (self.toU32 & ~(0x1 << 2)) | (nv.toU32 << 2) )
        }
    }
    /// Get bit 3 value
    public var b3:UInt{
        if(Int.size == 8){
            return UInt( (self.toU64 & (0x1 << 3)) >> 3 )
        } else {
            return UInt( (self.toU32 & (0x1 << 3)) >> 3 )
        }
    }
    /// Set bit 3 and return a new UInt
    public func setb3(_ bit:Int)->UInt{
        let nv = bit != 0 ? 1 : 0
        if(Int.size == 8){
            return UInt( (self.toU64 & ~(0x1 << 3)) | (nv.toU64 << 3) )
        } else {
            return UInt( (self.toU32 & ~(0x1 << 3)) | (nv.toU32 << 3) )
        }
    }
    /// Get bit 4 value
    public var b4:UInt{
        if(Int.size == 8){
            return UInt( (self.toU64 & (0x1 << 4)) >> 4 )
        } else {
            return UInt( (self.toU32 & (0x1 << 4)) >> 4 )
        }
    }
    /// Set bit 4 and return a new UInt
    public func setb4(_ bit:Int)->UInt{
        let nv = bit != 0 ? 1 : 0
        if(Int.size == 8){
            return UInt( (self.toU64 & ~(0x1 << 4)) | (nv.toU64 << 4) )
        } else {
            return UInt( (self.toU32 & ~(0x1 << 4)) | (nv.toU32 << 4) )
        }
    }
    /// Get bit 5 value
    public var b5:UInt{
        if(Int.size == 8){
            return UInt( (self.toU64 & (0x1 << 5)) >> 5 )
        } else {
            return UInt( (self.toU32 & (0x1 << 5)) >> 5 )
        }
    }
    /// Set bit 5 and return a new UInt
    public func setb5(_ bit:Int)->UInt{
        let nv = bit != 0 ? 1 : 0
        if(Int.size == 8){
            return UInt( (self.toU64 & ~(0x1 << 5)) | (nv.toU64 << 5) )
        } else {
            return UInt( (self.toU32 & ~(0x1 << 5)) | (nv.toU32 << 5) )
        }
    }
    /// Get bit 6 value
    public var b6:UInt{
        if(Int.size == 8){
            return UInt( (self.toU64 & (0x1 << 6)) >> 6 )
        } else {
            return UInt( (self.toU32 & (0x1 << 6)) >> 6 )
        }
    }
    /// Set bit 6 and return a new UInt
    public func setb6(_ bit:Int)->UInt{
        let nv = bit != 0 ? 1 : 0
        if(Int.size == 8){
            return UInt( (self.toU64 & ~(0x1 << 6)) | (nv.toU64 << 6) )
        } else {
            return UInt( (self.toU32 & ~(0x1 << 6)) | (nv.toU32 << 6) )
        }
    }
    /// Get bit 7 value
    public var b7:UInt{
        if(Int.size == 8){
            return UInt( (self.toU64 & (0x1 << 7)) >> 7 )
        } else {
            return UInt( (self.toU32 & (0x1 << 7)) >> 7 )
        }
    }
    /// Set bit 7 and return a new UInt
    public func setb7(_ bit:Int)->UInt{
        let nv = bit != 0 ? 1 : 0
        if(Int.size == 8){
            return UInt( (self.toU64 & ~(0x1 << 7)) | (nv.toU64 << 7) )
        } else {
            return UInt( (self.toU32 & ~(0x1 << 7)) | (nv.toU32 << 7) )
        }
    }
    
    
    /// Subscript that returns or set one of the bytes of a UInt
    /// at the given index.
    /// Trying to access an out of index byte will result in an error.
    public subscript(index: Int) -> UInt {
        get {
            precondition(index<Int.size,"Byte set index out of range")
            if(UInt.size == 8){
                return UInt(self.toU64 & (0xFF << (index.toU64*8))) >> (index*8).toUInt
            }else{
                return UInt(self.toU32 & (0xFF << (index.toU32*8))) >> (index*8).toUInt
            }
        }
        set(newValue) {
            precondition(index<Int.size,"Byte set index out of range")
            if(UInt.size == 8){
                self = UInt((self.toU64 & ~(0xFF << (index.toU64*8))) | (newValue.toU64 << (index.toU64*8)))
            }else{
                self = UInt((self.toU32 & ~(0xFF << (index.toU32*8))) | (newValue.toU32 << (index.toU32*8)))
            }
        }
    }
}

/**
 Extension that adds a few additional functionalities to Int8:
 - toIntN/toUIntN truncating bit pattern conversions
 - allOnes
 - size
 - Byte indexed subscript
 */
extension Int8 {
    /// Perform a bit pattern truncating conversion to UInt8
    public var toU8: UInt8{return UInt8(bitPattern:self)}
    /// Perform a bit pattern truncating conversion to Int8
    public var to8: Int8{return self}
    /// Perform a bit pattern truncating conversion to UInt16
    public var toU16: UInt16{return UInt16(self)}
    /// Perform a bit pattern truncating conversion to Int16
    public var to16: Int16{return Int16(self)}
    /// Perform a bit pattern truncating conversion to UInt32
    public var toU32: UInt32{return UInt32(self)}
    /// Perform a bit pattern truncating conversion to Int32
    public var to32: Int32{return Int32(self)}
    /// Perform a bit pattern truncating conversion to UInt64
    public var toU64: UInt64{return UInt64(self)}
    /// Perform a bit pattern truncating conversion to Int64
    public var to64: Int64{return Int64(self)}
    /// Perform a bit pattern truncating conversion to Int
    public var toInt:Int{return Int(bitPattern:UInt(self))}
    /// Perform a bit pattern truncating conversion to UInt
    public var toUInt:UInt{return UInt(self)}
    /// Returns a Int8 with all ones
    public static var allOnes:Int8{return Int8(bitPattern: UInt8.max)}
    
    /// Returns the size of this type (number of bytes)
    public static var size:Int{return MemoryLayout<Int8>.stride}
    
    /// Get bit 0 value
    public var b0:Int8{
        return ( (self.toU8 & (0x1 << 0)) >> 0 ).to8
    }
    /// Set bit 0 and return a new Int
    public func setb0(_ bit:Int)->Int8{
        let nv = bit != 0 ? 1 : 0
        return ( (self.toU8 & ~(0x1 << 0)) | (nv.toU8 << 0) ).to8
    }
    /// Get bit 1 value
    public var b1:Int8{
        return ( (self.toU8 & (0x1 << 1)) >> 1 ).to8
    }
    /// Set bit 1 and return a new Int
    public func setb1(_ bit:Int)->Int8{
        let nv = bit != 0 ? 1 : 0
        return ( (self.toU8 & ~(0x1 << 1)) | (nv.toU8 << 1) ).to8
    }
    /// Get bit 2 value
    public var b2:Int8{
        return ( (self.toU8 & (0x1 << 2)) >> 2 ).to8
    }
    /// Set bit 2 and return a new Int
    public func setb2(_ bit:Int)->Int8{
        let nv = bit != 0 ? 1 : 0
        return ( (self.toU8 & ~(0x1 << 2)) | (nv.toU8 << 2) ).to8
    }
    /// Get bit 3 value
    public var b3:Int8{
        return ( (self.toU8 & (0x1 << 3)) >> 3 ).to8
    }
    /// Set bit 3 and return a new Int
    public func setb3(_ bit:Int)->Int8{
        let nv = bit != 0 ? 1 : 0
        return ( (self.toU8 & ~(0x1 << 3)) | (nv.toU8 << 3) ).to8
    }
    /// Get bit 4 value
    public var b4:Int8{
        return ( (self.toU8 & (0x1 << 4)) >> 4 ).to8
    }
    /// Set bit 4 and return a new Int
    public func setb4(_ bit:Int)->Int8{
        let nv = bit != 0 ? 1 : 0
        return ( (self.toU8 & ~(0x1 << 4)) | (nv.toU8 << 4) ).to8
    }
    /// Get bit 5 value
    public var b5:Int8{
        return ( (self.toU8 & (0x1 << 5)) >> 5 ).to8
    }
    /// Set bit 5 and return a new Int
    public func setb5(_ bit:Int)->Int8{
        let nv = bit != 0 ? 1 : 0
        return ( (self.toU8 & ~(0x1 << 5)) | (nv.toU8 << 5) ).to8
    }
    /// Get bit 6 value
    public var b6:Int8{
        return ( (self.toU8 & (0x1 << 6)) >> 6 ).to8
    }
    /// Set bit 6 and return a new Int
    public func setb6(_ bit:Int)->Int8{
        let nv = bit != 0 ? 1 : 0
        return ( (self.toU8 & ~(0x1 << 6)) | (nv.toU8 << 6) ).to8
    }
    /// Get bit 7 value
    public var b7:Int8{
        return ( (self.toU8 & (0x1 << 7)) >> 7 ).to8
    }
    /// Set bit 7 and return a new Int
    public func setb7(_ bit:Int)->Int8{
        let nv = bit != 0 ? 1 : 0
        return ( (self.toU8 & ~(0x1 << 7)) | (nv.toU8 << 7) ).to8
    }
    
    
    
    /// Subscript that returns or set one of the bytes of this integer
    /// at the given index.
    /// Trying to access an out of index byte will result in an error.
    public subscript(index: Int) -> Int8 {
        get {
            precondition(index<Int8.size,"Byte set index out of range")
            return self
        }
        set(newValue) {
            precondition(index<Int8.size,"Byte set index out of range")
            self = newValue
        }
    }
}

/**
 Extension that adds a few additional functionalities to UInt8:
 - toIntN/toUIntN truncating bit pattern conversions
 - allOnes
 - size
 - Byte indexed subscript
 */
extension UInt8 {
    /// Perform a bit pattern truncating conversion to UInt8
    public var toU8: UInt8{return self}
    /// Perform a bit pattern truncating conversion to Int8
    public var to8: Int8{return Int8(bitPattern:self)}
    /// Perform a bit pattern truncating conversion to UInt16
    public var toU16: UInt16{return UInt16(self)}
    /// Perform a bit pattern truncating conversion to Int16
    public var to16: Int16{return Int16(self)}
    /// Perform a bit pattern truncating conversion to UInt32
    public var toU32: UInt32{return UInt32(self)}
    /// Perform a bit pattern truncating conversion to Int32
    public var to32: Int32{return Int32(self)}
    /// Perform a bit pattern truncating conversion to UInt64
    public var toU64: UInt64{return UInt64(self)}
    /// Perform a bit pattern truncating conversion to Int64
    public var to64: Int64{return Int64(self)}
    /// Perform a bit pattern truncating conversion to Int
    public var toInt:Int{return Int(bitPattern:UInt(self))}
    /// Perform a bit pattern truncating conversion to UInt
    public var toUInt:UInt{return UInt(self)}
    /// Returns a UInt8 with all ones
    public static var allOnes:UInt8{return UInt8.max}
    
    /// Returns the size of this type (number of bytes)
    public static var size:Int{return MemoryLayout<UInt8>.stride}
    
    /// Get bit 0 value
    public var b0:UInt8{
        return (self & (0x1 << 0)) >> 0
    }
    /// Set bit 0 and return a new UInt
    public func setb0(_ bit:Int)->UInt8{
        let nv = bit != 0 ? 1 : 0
        return (self & ~(0x1 << 0)) | (nv.toU8 << 0)
    }
    /// Get bit 1 value
    public var b1:UInt8{
        return (self & (0x1 << 1)) >> 1
    }
    /// Set bit 1 and return a new UInt
    public func setb1(_ bit:Int)->UInt8{
        let nv = bit != 0 ? 1 : 0
        return (self & ~(0x1 << 1)) | (nv.toU8 << 1)
    }
    /// Get bit 2 value
    public var b2:UInt8{
        return (self & (0x1 << 2)) >> 2
    }
    /// Set bit 2 and return a new UInt
    public func setb2(_ bit:Int)->UInt8{
        let nv = bit != 0 ? 1 : 0
        return (self & ~(0x1 << 2)) | (nv.toU8 << 2)
    }
    /// Get bit 3 value
    public var b3:UInt8{
        return (self & (0x1 << 3)) >> 3
    }
    /// Set bit 3 and return a new UInt
    public func setb3(_ bit:Int)->UInt8{
        let nv = bit != 0 ? 1 : 0
        return (self & ~(0x1 << 3)) | (nv.toU8 << 3)
    }
    /// Get bit 4 value
    public var b4:UInt8{
        return (self & (0x1 << 4)) >> 4
    }
    /// Set bit 4 and return a new UInt
    public func setb4(_ bit:Int)->UInt8{
        let nv = bit != 0 ? 1 : 0
        return (self & ~(0x1 << 4)) | (nv.toU8 << 4)
    }
    /// Get bit 5 value
    public var b5:UInt8{
        return (self & (0x1 << 5)) >> 5
    }
    /// Set bit 5 and return a new UInt
    public func setb5(_ bit:Int)->UInt8{
        let nv = bit != 0 ? 1 : 0
        return (self & ~(0x1 << 5)) | (nv.toU8 << 5)
    }
    /// Get bit 6 value
    public var b6:UInt8{
        return (self & (0x1 << 6)) >> 6
    }
    /// Set bit 6 and return a new UInt
    public func setb6(_ bit:Int)->UInt8{
        let nv = bit != 0 ? 1 : 0
        return (self & ~(0x1 << 6)) | (nv.toU8 << 6)
    }
    /// Get bit 7 value
    public var b7:UInt8{
        return (self & (0x1 << 7)) >> 7
    }
    /// Set bit 7 and return a new UInt
    public func setb7(_ bit:Int)->UInt8{
        let nv = bit != 0 ? 1 : 0
        return (self & ~(0x1 << 7)) | (nv.toU8 << 7)
    }
    
    
    
    /// Subscript that returns or set one of the bytes of this integer
    /// at the given index.
    /// Trying to access an out of index byte will result in an error.
    public subscript(index: Int) -> UInt8 {
        get {
            precondition(index<Int8.size,"Byte set index out of range")
            return self
        }
        set(newValue) {
            precondition(index<Int8.size,"Byte set index out of range")
            self = newValue
        }
    }
}

/**
 Extension that adds a few additional functionalities to Int16:
 - toIntN/toUIntN truncating bit pattern conversions
 - allOnes
 - size
 - Byte indexed subscript
 */
extension Int16 {
    /// Perform a bit pattern truncating conversion to UInt8
    public var toU8: UInt8{return UInt8(truncatingBitPattern:self)}
    /// Perform a bit pattern truncating conversion to Int8
    public var to8: Int8{return Int8(truncatingBitPattern:self)}
    /// Perform a bit pattern truncating conversion to UInt16
    public var toU16: UInt16{return UInt16(bitPattern:self)}
    /// Perform a bit pattern truncating conversion to Int16
    public var to16: Int16{return self}
    /// Perform a bit pattern truncating conversion to UInt32
    public var toU32: UInt32{return UInt32(self)}
    /// Perform a bit pattern truncating conversion to Int32
    public var to32: Int32{return Int32(self)}
    /// Perform a bit pattern truncating conversion to UInt64
    public var toU64: UInt64{return UInt64(self)}
    /// Perform a bit pattern truncating conversion to Int64
    public var to64: Int64{return Int64(self)}
    /// Perform a bit pattern truncating conversion to Int
    public var toInt:Int{return Int(bitPattern:UInt(self))}
    /// Perform a bit pattern truncating conversion to UInt
    public var toUInt:UInt{return UInt(self)}
    /// Returns a Int16 with all ones
    public static var allOnes:Int16{return Int16(bitPattern: UInt16.max)}
    
    /// Returns the size of this type (number of bytes)
    public static var size:Int{return MemoryLayout<Int16>.stride}
    
    /// Get bit 0 value
    public var b0:Int16{
        return ( (self.toU16 & (0x1 << 0)) >> 0 ).to16
    }
    /// Set bit 0 and return a new Int
    public func setb0(_ bit:Int)->Int16{
        let nv = bit != 0 ? 1 : 0
        return ( (self.toU16 & ~(0x1 << 0)) | (nv.toU16 << 0) ).to16
    }
    /// Get bit 1 value
    public var b1:Int16{
        return ( (self.toU16 & (0x1 << 1)) >> 1 ).to16
    }
    /// Set bit 1 and return a new Int
    public func setb1(_ bit:Int)->Int16{
        let nv = bit != 0 ? 1 : 0
        return ( (self.toU16 & ~(0x1 << 1)) | (nv.toU16 << 1) ).to16
    }
    /// Get bit 2 value
    public var b2:Int16{
        return ( (self.toU16 & (0x1 << 2)) >> 2 ).to16
    }
    /// Set bit 2 and return a new Int
    public func setb2(_ bit:Int)->Int16{
        let nv = bit != 0 ? 1 : 0
        return ( (self.toU16 & ~(0x1 << 2)) | (nv.toU16 << 2) ).to16
    }
    /// Get bit 3 value
    public var b3:Int16{
        return ( (self.toU16 & (0x1 << 3)) >> 3 ).to16
    }
    /// Set bit 3 and return a new Int
    public func setb3(_ bit:Int)->Int16{
        let nv = bit != 0 ? 1 : 0
        return ( (self.toU16 & ~(0x1 << 3)) | (nv.toU16 << 3) ).to16
    }
    /// Get bit 4 value
    public var b4:Int16{
        return ( (self.toU16 & (0x1 << 4)) >> 4 ).to16
    }
    /// Set bit 4 and return a new Int
    public func setb4(_ bit:Int)->Int16{
        let nv = bit != 0 ? 1 : 0
        return ( (self.toU16 & ~(0x1 << 4)) | (nv.toU16 << 4) ).to16
    }
    /// Get bit 5 value
    public var b5:Int16{
        return ( (self.toU16 & (0x1 << 5)) >> 5 ).to16
    }
    /// Set bit 5 and return a new Int
    public func setb5(_ bit:Int)->Int16{
        let nv = bit != 0 ? 1 : 0
        return ( (self.toU16 & ~(0x1 << 5)) | (nv.toU16 << 5) ).to16
    }
    /// Get bit 6 value
    public var b6:Int16{
        return ( (self.toU16 & (0x1 << 6)) >> 6 ).to16
    }
    /// Set bit 6 and return a new Int
    public func setb6(_ bit:Int)->Int16{
        let nv = bit != 0 ? 1 : 0
        return ( (self.toU16 & ~(0x1 << 6)) | (nv.toU16 << 6) ).to16
    }
    /// Get bit 7 value
    public var b7:Int16{
        return ( (self.toU16 & (0x1 << 7)) >> 7 ).to16
    }
    /// Set bit 7 and return a new Int
    public func setb7(_ bit:Int)->Int16{
        let nv = bit != 0 ? 1 : 0
        return ( (self.toU16 & ~(0x1 << 7)) | (nv.toU16 << 7) ).to16
    }
    
    
    
    /// Subscript that returns or set one of the bytes of a Int16
    /// at the given index.
    /// Trying to access an out of index byte will result in an error.
    public subscript(index: Int) -> Int16 {
        get {
            precondition(index<Int16.size,"Byte set index out of range")
            return ((self.toU16 & (0xFF << (index.toU16*8))) >> (index.toU16*8)).to16
        }
        set(newValue) {
            precondition(index<Int16.size,"Byte set index out of range")
            self = ( (self.toU16 & ~(0xFF << (index.toU16*8))) | (newValue.toU16 << (index.toU16*8)) ).to16
        }
    }
}

/**
 Extension that adds a few additional functionalities to UInt16:
 - toIntN/toUIntN truncating bit pattern conversions
 - allOnes
 - size
 - Byte indexed subscript
 */
extension UInt16 {
    /// Perform a bit pattern truncating conversion to UInt8
    public var toU8: UInt8{return UInt8(truncatingBitPattern:self)}
    /// Perform a bit pattern truncating conversion to Int8
    public var to8: Int8{return Int8(truncatingBitPattern:self)}
    /// Perform a bit pattern truncating conversion to UInt16
    public var toU16: UInt16{return self}
    /// Perform a bit pattern truncating conversion to Int16
    public var to16: Int16{return Int16(bitPattern:self)}
    /// Perform a bit pattern truncating conversion to UInt32
    public var toU32: UInt32{return UInt32(self)}
    /// Perform a bit pattern truncating conversion to Int32
    public var to32: Int32{return Int32(self)}
    /// Perform a bit pattern truncating conversion to UInt64
    public var toU64: UInt64{return UInt64(self)}
    /// Perform a bit pattern truncating conversion to Int64
    public var to64: Int64{return Int64(self)}
    /// Perform a bit pattern truncating conversion to Int
    public var toInt:Int{return Int(bitPattern:UInt(self))}
    /// Perform a bit pattern truncating conversion to UInt
    public var toUInt:UInt{return UInt(self)}
    /// Returns a UInt16 with all ones
    public static var allOnes:UInt16{return UInt16.max}
    
    /// Returns the size of this type (number of bytes)
    public static var size:Int{return MemoryLayout<UInt16>.stride}
    
    /// Get bit 0 value
    public var b0:UInt16{
        return (self & (0x1 << 0)) >> 0
    }
    /// Set bit 0 and return a new UInt
    public func setb0(_ bit:Int)->UInt16{
        let nv = bit != 0 ? 1 : 0
        return (self & ~(0x1 << 0)) | (nv.toU16 << 0)
    }
    /// Get bit 1 value
    public var b1:UInt16{
        return (self & (0x1 << 1)) >> 1
    }
    /// Set bit 1 and return a new UInt
    public func setb1(_ bit:Int)->UInt16{
        let nv = bit != 0 ? 1 : 0
        return (self & ~(0x1 << 1)) | (nv.toU16 << 1)
    }
    /// Get bit 2 value
    public var b2:UInt16{
        return (self & (0x1 << 2)) >> 2
    }
    /// Set bit 2 and return a new UInt
    public func setb2(_ bit:Int)->UInt16{
        let nv = bit != 0 ? 1 : 0
        return (self & ~(0x1 << 2)) | (nv.toU16 << 2)
    }
    /// Get bit 3 value
    public var b3:UInt16{
        return (self & (0x1 << 3)) >> 3
    }
    /// Set bit 3 and return a new UInt
    public func setb3(_ bit:Int)->UInt16{
        let nv = bit != 0 ? 1 : 0
        return (self & ~(0x1 << 3)) | (nv.toU16 << 3)
    }
    /// Get bit 4 value
    public var b4:UInt16{
        return (self & (0x1 << 4)) >> 4
    }
    /// Set bit 4 and return a new UInt
    public func setb4(_ bit:Int)->UInt16{
        let nv = bit != 0 ? 1 : 0
        return (self & ~(0x1 << 4)) | (nv.toU16 << 4)
    }
    /// Get bit 5 value
    public var b5:UInt16{
        return (self & (0x1 << 5)) >> 5
    }
    /// Set bit 5 and return a new UInt
    public func setb5(_ bit:Int)->UInt16{
        let nv = bit != 0 ? 1 : 0
        return (self & ~(0x1 << 5)) | (nv.toU16 << 5)
    }
    /// Get bit 6 value
    public var b6:UInt16{
        return (self & (0x1 << 6)) >> 6
    }
    /// Set bit 6 and return a new UInt
    public func setb6(_ bit:Int)->UInt16{
        let nv = bit != 0 ? 1 : 0
        return (self & ~(0x1 << 6)) | (nv.toU16 << 6)
    }
    /// Get bit 7 value
    public var b7:UInt16{
        return (self & (0x1 << 7)) >> 7
    }
    /// Set bit 7 and return a new UInt
    public func setb7(_ bit:Int)->UInt16{
        let nv = bit != 0 ? 1 : 0
        return (self & ~(0x1 << 7)) | (nv.toU16 << 7)
    }
    
    
    
    /// Subscript that returns or set one of the bytes of a UInt16
    /// at the given index.
    /// Trying to access an out of index byte will result in an error.
    public subscript(index: Int) -> UInt16 {
        get {
            precondition(index<Int16.size,"Byte set index out of range")
            return (self & (0xFF << (index.toU16*8))) >> (index.toU16*8)
        }
        set(newValue) {
            precondition(index<Int16.size,"Byte set index out of range")
            self = (self & ~(0xFF << (index.toU16*8))) | (newValue.toU16 << (index.toU16*8))
        }
    }
}

/**
 Extension that adds a few additional functionalities to Int32:
 - toIntN/toUIntN truncating bit pattern conversions
 - allOnes
 - size
 - Byte indexed subscript
 */
extension Int32 {
    /// Perform a bit pattern truncating conversion to UInt8
    public var toU8: UInt8{return UInt8(truncatingBitPattern:self)}
    /// Perform a bit pattern truncating conversion to Int8
    public var to8: Int8{return Int8(truncatingBitPattern:self)}
    /// Perform a bit pattern truncating conversion to UInt16
    public var toU16: UInt16{return UInt16(truncatingBitPattern:self)}
    /// Perform a bit pattern truncating conversion to Int16
    public var to16: Int16{return Int16(truncatingBitPattern:self)}
    /// Perform a bit pattern truncating conversion to UInt32
    public var toU32: UInt32{return UInt32(bitPattern:self)}
    /// Perform a bit pattern truncating conversion to Int32
    public var to32: Int32{return self}
    /// Perform a bit pattern truncating conversion to UInt64
    public var toU64: UInt64{return UInt64(self)}
    /// Perform a bit pattern truncating conversion to Int64
    public var to64: Int64{return Int64(self)}
    /// Perform a bit pattern truncating conversion to Int
    public var toInt:Int{return Int(bitPattern:UInt(self))}
    /// Perform a bit pattern truncating conversion to UInt
    public var toUInt:UInt{return UInt(self)}
    /// Returns a Int32 with all ones
    public static var allOnes:Int32{return Int32(bitPattern: UInt32.max)}
    
    /// Returns the size of this type (number of bytes)
    public static var size:Int{return MemoryLayout<Int32>.stride}
    
    /// Get bit 0 value
    public var b0:Int32{
        return ( (self.toU32 & (0x1 << 0)) >> 0 ).to32
    }
    /// Set bit 0 and return a new Int
    public func setb0(_ bit:Int)->Int32{
        let nv = bit != 0 ? 1 : 0
        return ( (self.toU32 & ~(0x1 << 0)) | (nv.toU32 << 0) ).to32
    }
    /// Get bit 1 value
    public var b1:Int32{
        return ( (self.toU32 & (0x1 << 1)) >> 1 ).to32
    }
    /// Set bit 1 and return a new Int
    public func setb1(_ bit:Int)->Int32{
        let nv = bit != 0 ? 1 : 0
        return ( (self.toU32 & ~(0x1 << 1)) | (nv.toU32 << 1) ).to32
    }
    /// Get bit 2 value
    public var b2:Int32{
        return ( (self.toU32 & (0x1 << 2)) >> 2 ).to32
    }
    /// Set bit 2 and return a new Int
    public func setb2(_ bit:Int)->Int32{
        let nv = bit != 0 ? 1 : 0
        return ( (self.toU32 & ~(0x1 << 2)) | (nv.toU32 << 2) ).to32
    }
    /// Get bit 3 value
    public var b3:Int32{
        return ( (self.toU32 & (0x1 << 3)) >> 3 ).to32
    }
    /// Set bit 3 and return a new Int
    public func setb3(_ bit:Int)->Int32{
        let nv = bit != 0 ? 1 : 0
        return ( (self.toU32 & ~(0x1 << 3)) | (nv.toU32 << 3) ).to32
    }
    /// Get bit 4 value
    public var b4:Int32{
        return ( (self.toU32 & (0x1 << 4)) >> 4 ).to32
    }
    /// Set bit 4 and return a new Int
    public func setb4(_ bit:Int)->Int32{
        let nv = bit != 0 ? 1 : 0
        return ( (self.toU32 & ~(0x1 << 4)) | (nv.toU32 << 4) ).to32
    }
    /// Get bit 5 value
    public var b5:Int32{
        return ( (self.toU32 & (0x1 << 5)) >> 5 ).to32
    }
    /// Set bit 5 and return a new Int
    public func setb5(_ bit:Int)->Int32{
        let nv = bit != 0 ? 1 : 0
        return ( (self.toU32 & ~(0x1 << 5)) | (nv.toU32 << 5) ).to32
    }
    /// Get bit 6 value
    public var b6:Int32{
        return ( (self.toU32 & (0x1 << 6)) >> 6 ).to32
    }
    /// Set bit 6 and return a new Int
    public func setb6(_ bit:Int)->Int32{
        let nv = bit != 0 ? 1 : 0
        return ( (self.toU32 & ~(0x1 << 6)) | (nv.toU32 << 6) ).to32
    }
    /// Get bit 7 value
    public var b7:Int32{
        return ( (self.toU32 & (0x1 << 7)) >> 7 ).to32
    }
    /// Set bit 7 and return a new Int
    public func setb7(_ bit:Int)->Int32{
        let nv = bit != 0 ? 1 : 0
        return ( (self.toU32 & ~(0x1 << 7)) | (nv.toU32 << 7) ).to32
    }
    
    
    
    /// Subscript that returns or set one of the bytes of a Int32
    /// at the given index.
    /// Trying to access an out of index byte will result in an error.
    public subscript(index: Int) -> Int32 {
        get {
            precondition(index<Int32.size,"Byte set index out of range")
            return ((self.toU32 & (0xFF << (index.toU32*8))) >> (index.toU32*8)).to32
        }
        set(newValue) {
            precondition(index<Int32.size,"Byte set index out of range")
            self = ( (self.toU32 & ~(0xFF << (index.toU32*8))) | (newValue.toU32 << (index.toU32*8)) ).to32
        }
    }
}

/**
 Extension that adds a few additional functionalities to UInt32:
 - toIntN/toUIntN truncating bit pattern conversions
 - allOnes
 - size
 - Byte indexed subscript
 */
extension UInt32 {
    /// Perform a bit pattern truncating conversion to UInt8
    public var toU8: UInt8{return UInt8(truncatingBitPattern:self)}
    /// Perform a bit pattern truncating conversion to Int8
    public var to8: Int8{return Int8(truncatingBitPattern:self)}
    /// Perform a bit pattern truncating conversion to UInt16
    public var toU16: UInt16{return UInt16(truncatingBitPattern:self)}
    /// Perform a bit pattern truncating conversion to Int16
    public var to16: Int16{return Int16(truncatingBitPattern:self)}
    /// Perform a bit pattern truncating conversion to UInt32
    public var toU32: UInt32{return self}
    /// Perform a bit pattern truncating conversion to Int32
    public var to32: Int32{return Int32(bitPattern:self)}
    /// Perform a bit pattern truncating conversion to UInt64
    public var toU64: UInt64{return UInt64(self)}
    /// Perform a bit pattern truncating conversion to Int64
    public var to64: Int64{return Int64(self)}
    /// Perform a bit pattern truncating conversion to Int
    public var toInt:Int{return Int(bitPattern:UInt(self))}
    /// Perform a bit pattern truncating conversion to UInt
    public var toUInt:UInt{return UInt(self)}
    /// Returns a UInt32 with all ones
    public static var allOnes:UInt32{return UInt32.max}
    
    /// Returns the size of this type (number of bytes)
    public static var size:Int{return MemoryLayout<UInt32>.stride}
    
    /// Get bit 0 value
    public var b0:UInt32{
        return (self & (0x1 << 0)) >> 0
    }
    /// Set bit 0 and return a new UInt
    public func setb0(_ bit:Int)->UInt32{
        let nv = bit != 0 ? 1 : 0
        return (self & ~(0x1 << 0)) | (nv.toU32 << 0)
    }
    /// Get bit 1 value
    public var b1:UInt32{
        return (self & (0x1 << 1)) >> 1
    }
    /// Set bit 1 and return a new UInt
    public func setb1(_ bit:Int)->UInt32{
        let nv = bit != 0 ? 1 : 0
        return (self & ~(0x1 << 1)) | (nv.toU32 << 1)
    }
    /// Get bit 2 value
    public var b2:UInt32{
        return (self & (0x1 << 2)) >> 2
    }
    /// Set bit 2 and return a new UInt
    public func setb2(_ bit:Int)->UInt32{
        let nv = bit != 0 ? 1 : 0
        return (self & ~(0x1 << 2)) | (nv.toU32 << 2)
    }
    /// Get bit 3 value
    public var b3:UInt32{
        return (self & (0x1 << 3)) >> 3
    }
    /// Set bit 3 and return a new UInt
    public func setb3(_ bit:Int)->UInt32{
        let nv = bit != 0 ? 1 : 0
        return (self & ~(0x1 << 3)) | (nv.toU32 << 3)
    }
    /// Get bit 4 value
    public var b4:UInt32{
        return (self & (0x1 << 4)) >> 4
    }
    /// Set bit 4 and return a new UInt
    public func setb4(_ bit:Int)->UInt32{
        let nv = bit != 0 ? 1 : 0
        return (self & ~(0x1 << 4)) | (nv.toU32 << 4)
    }
    /// Get bit 5 value
    public var b5:UInt32{
        return (self & (0x1 << 5)) >> 5
    }
    /// Set bit 5 and return a new UInt
    public func setb5(_ bit:Int)->UInt32{
        let nv = bit != 0 ? 1 : 0
        return (self & ~(0x1 << 5)) | (nv.toU32 << 5)
    }
    /// Get bit 6 value
    public var b6:UInt32{
        return (self & (0x1 << 6)) >> 6
    }
    /// Set bit 6 and return a new UInt
    public func setb6(_ bit:Int)->UInt32{
        let nv = bit != 0 ? 1 : 0
        return (self & ~(0x1 << 6)) | (nv.toU32 << 6)
    }
    /// Get bit 7 value
    public var b7:UInt32{
        return (self & (0x1 << 7)) >> 7
    }
    /// Set bit 7 and return a new UInt
    public func setb7(_ bit:Int)->UInt32{
        let nv = bit != 0 ? 1 : 0
        return (self & ~(0x1 << 7)) | (nv.toU32 << 7)
    }
    
    
    
    /// Subscript that returns or set one of the bytes of a UInt32
    /// at the given index.
    /// Trying to access an out of index byte will result in an error.
    public subscript(index: Int) -> UInt32 {
        get {
            precondition(index<Int32.size,"Byte set index out of range")
            return (self & (0xFF << (index.toU32*8))) >> (index.toU32*8)
        }
        set(newValue) {
            precondition(index<Int32.size,"Byte set index out of range")
            self = (self & ~(0xFF << (index.toU32*8))) | (newValue.toU32 << (index.toU32*8))
        }
    }
}

/**
 Extension that adds a few additional functionalities to Int64:
 - toIntN/toUIntN truncating bit pattern conversions
 - allOnes
 - size
 - Byte indexed subscript
 */
extension Int64 {
    /// Perform a bit pattern truncating conversion to UInt8
    public var toU8: UInt8{return UInt8(truncatingBitPattern:self)}
    /// Perform a bit pattern truncating conversion to Int8
    public var to8: Int8{return Int8(truncatingBitPattern:self)}
    /// Perform a bit pattern truncating conversion to UInt16
    public var toU16: UInt16{return UInt16(truncatingBitPattern:self)}
    /// Perform a bit pattern truncating conversion to Int16
    public var to16: Int16{return Int16(truncatingBitPattern:self)}
    /// Perform a bit pattern truncating conversion to UInt32
    public var toU32: UInt32{return UInt32(truncatingBitPattern:self)}
    /// Perform a bit pattern truncating conversion to Int32
    public var to32: Int32{return Int32(truncatingBitPattern:self)}
    /// Perform a bit pattern truncating conversion to UInt64
    public var toU64: UInt64{return UInt64(bitPattern:self)}
    /// Perform a bit pattern truncating conversion to Int64
    public var to64: Int64{return self}
    /// Perform a bit pattern truncating conversion to Int
    public var toInt:Int{return Int(truncatingBitPattern:self)}
    /// Perform a bit pattern truncating conversion to UInt
    public var toUInt:UInt{return UInt(truncatingBitPattern:self)}
    /// Returns a Int64 with all ones
    public static var allOnes:Int64{return Int64(bitPattern: UInt64.max)}
    
    /// Returns the size of this type (number of bytes)
    public static var size:Int{return MemoryLayout<Int64>.stride}
    
    /// Get bit 0 value
    public var b0:Int64{
        return ( (self.toU64 & (0x1 << 0)) >> 0 ).to64
    }
    /// Set bit 0 and return a new Int
    public func setb0(_ bit:Int)->Int64{
        let nv = bit != 0 ? 1 : 0
        return ( (self.toU64 & ~(0x1 << 0)) | (nv.toU64 << 0) ).to64
    }
    /// Get bit 1 value
    public var b1:Int64{
        return ( (self.toU64 & (0x1 << 1)) >> 1 ).to64
    }
    /// Set bit 1 and return a new Int
    public func setb1(_ bit:Int)->Int64{
        let nv = bit != 0 ? 1 : 0
        return ( (self.toU64 & ~(0x1 << 1)) | (nv.toU64 << 1) ).to64
    }
    /// Get bit 2 value
    public var b2:Int64{
        return ( (self.toU64 & (0x1 << 2)) >> 2 ).to64
    }
    /// Set bit 2 and return a new Int
    public func setb2(_ bit:Int)->Int64{
        let nv = bit != 0 ? 1 : 0
        return ( (self.toU64 & ~(0x1 << 2)) | (nv.toU64 << 2) ).to64
    }
    /// Get bit 3 value
    public var b3:Int64{
        return ( (self.toU64 & (0x1 << 3)) >> 3 ).to64
    }
    /// Set bit 3 and return a new Int
    public func setb3(_ bit:Int)->Int64{
        let nv = bit != 0 ? 1 : 0
        return ( (self.toU64 & ~(0x1 << 3)) | (nv.toU64 << 3) ).to64
    }
    /// Get bit 4 value
    public var b4:Int64{
        return ( (self.toU64 & (0x1 << 4)) >> 4 ).to64
    }
    /// Set bit 4 and return a new Int
    public func setb4(_ bit:Int)->Int64{
        let nv = bit != 0 ? 1 : 0
        return ( (self.toU64 & ~(0x1 << 4)) | (nv.toU64 << 4) ).to64
    }
    /// Get bit 5 value
    public var b5:Int64{
        return ( (self.toU64 & (0x1 << 5)) >> 5 ).to64
    }
    /// Set bit 5 and return a new Int
    public func setb5(_ bit:Int)->Int64{
        let nv = bit != 0 ? 1 : 0
        return ( (self.toU64 & ~(0x1 << 5)) | (nv.toU64 << 5) ).to64
    }
    /// Get bit 6 value
    public var b6:Int64{
        return ( (self.toU64 & (0x1 << 6)) >> 6 ).to64
    }
    /// Set bit 6 and return a new Int
    public func setb6(_ bit:Int)->Int64{
        let nv = bit != 0 ? 1 : 0
        return ( (self.toU64 & ~(0x1 << 6)) | (nv.toU64 << 6) ).to64
    }
    /// Get bit 7 value
    public var b7:Int64{
        return ( (self.toU64 & (0x1 << 7)) >> 7 ).to64
    }
    /// Set bit 7 and return a new Int
    public func setb7(_ bit:Int)->Int64{
        let nv = bit != 0 ? 1 : 0
        return ( (self.toU64 & ~(0x1 << 7)) | (nv.toU64 << 7) ).to64
    }
    
    
    
    /// Subscript that returns or set one of the bytes of a Int64
    /// at the given index.
    /// Trying to access an out of index byte will result in an error.
    public subscript(index: Int) -> Int64 {
        get {
            precondition(index<Int64.size,"Byte set index out of range")
            return ((self.toU64 & (0xFF << (index.toU64*8))) >> (index.toU64*8)).to64
        }
        set(newValue) {
            precondition(index<Int64.size,"Byte set index out of range")
            self = ( (self.toU64 & ~(0xFF << (index.toU64*8))) | (newValue.toU64 << (index.toU64*8)) ).to64
        }
    }
}

/**
 Extension that adds a few additional functionalities to UInt64:
 - toIntN/toUIntN truncating bit pattern conversions
 - allOnes
 - size
 - Byte indexed subscript
 */
extension UInt64 {
    /// Perform a bit pattern truncating conversion to UInt8
    public var toU8: UInt8{return UInt8(truncatingBitPattern:self)}
    /// Perform a bit pattern truncating conversion to Int8
    public var to8: Int8{return Int8(truncatingBitPattern:self)}
    /// Perform a bit pattern truncating conversion to UInt16
    public var toU16: UInt16{return UInt16(truncatingBitPattern:self)}
    /// Perform a bit pattern truncating conversion to Int16
    public var to16: Int16{return Int16(truncatingBitPattern:self)}
    /// Perform a bit pattern truncating conversion to UInt32
    public var toU32: UInt32{return UInt32(truncatingBitPattern:self)}
    /// Perform a bit pattern truncating conversion to Int32
    public var to32: Int32{return Int32(truncatingBitPattern:self)}
    /// Perform a bit pattern truncating conversion to UInt64
    public var toU64: UInt64{return self}
    /// Perform a bit pattern truncating conversion to Int64
    public var to64: Int64{return Int64(bitPattern:self)}
    /// Perform a bit pattern truncating conversion to Int
    public var toInt:Int{return Int(truncatingBitPattern:self)}
    /// Perform a bit pattern truncating conversion to UInt
    public var toUInt:UInt{return UInt(truncatingBitPattern:self)}
    /// Returns a UInt64 with all ones
    public static var allOnes:UInt64{return UInt64.max}
    
    /// Returns the size of this type (number of bytes)
    public static var size:Int{return MemoryLayout<UInt64>.stride}
    
    /// Get bit 0 value
    public var b0:UInt64{
        return (self & (0x1 << 0)) >> 0
    }
    /// Set bit 0 and return a new UInt
    public func setb0(_ bit:Int)->UInt64{
        let nv = bit != 0 ? 1 : 0
        return (self & ~(0x1 << 0)) | (nv.toU64 << 0)
    }
    /// Get bit 1 value
    public var b1:UInt64{
        return (self & (0x1 << 1)) >> 1
    }
    /// Set bit 1 and return a new UInt
    public func setb1(_ bit:Int)->UInt64{
        let nv = bit != 0 ? 1 : 0
        return (self & ~(0x1 << 1)) | (nv.toU64 << 1)
    }
    /// Get bit 2 value
    public var b2:UInt64{
        return (self & (0x1 << 2)) >> 2
    }
    /// Set bit 2 and return a new UInt
    public func setb2(_ bit:Int)->UInt64{
        let nv = bit != 0 ? 1 : 0
        return (self & ~(0x1 << 2)) | (nv.toU64 << 2)
    }
    /// Get bit 3 value
    public var b3:UInt64{
        return (self & (0x1 << 3)) >> 3
    }
    /// Set bit 3 and return a new UInt
    public func setb3(_ bit:Int)->UInt64{
        let nv = bit != 0 ? 1 : 0
        return (self & ~(0x1 << 3)) | (nv.toU64 << 3)
    }
    /// Get bit 4 value
    public var b4:UInt64{
        return (self & (0x1 << 4)) >> 4
    }
    /// Set bit 4 and return a new UInt
    public func setb4(_ bit:Int)->UInt64{
        let nv = bit != 0 ? 1 : 0
        return (self & ~(0x1 << 4)) | (nv.toU64 << 4)
    }
    /// Get bit 5 value
    public var b5:UInt64{
        return (self & (0x1 << 5)) >> 5
    }
    /// Set bit 5 and return a new UInt
    public func setb5(_ bit:Int)->UInt64{
        let nv = bit != 0 ? 1 : 0
        return (self & ~(0x1 << 5)) | (nv.toU64 << 5)
    }
    /// Get bit 6 value
    public var b6:UInt64{
        return (self & (0x1 << 6)) >> 6
    }
    /// Set bit 6 and return a new UInt
    public func setb6(_ bit:Int)->UInt64{
        let nv = bit != 0 ? 1 : 0
        return (self & ~(0x1 << 6)) | (nv.toU64 << 6)
    }
    /// Get bit 7 value
    public var b7:UInt64{
        return (self & (0x1 << 7)) >> 7
    }
    /// Set bit 7 and return a new UInt
    public func setb7(_ bit:Int)->UInt64{
        let nv = bit != 0 ? 1 : 0
        return (self & ~(0x1 << 7)) | (nv.toU64 << 7)
    }
    
    
    
    /// Subscript that returns or set one of the bytes of a UInt64
    /// at the given index.
    /// Trying to access an out of index byte will result in an error.
    public subscript(index: Int) -> UInt64 {
        get {
            precondition(index<Int64.size,"Byte set index out of range")
            return (self & (0xFF << (index.toU64*8))) >> (index.toU64*8)
        }
        set(newValue) {
            precondition(index<Int64.size,"Byte set index out of range")
            self = (self & ~(0xFF << (index.toU64*8))) | (newValue.toU64 << (index.toU64*8))
        }
    }
}



// MARK: Operators
/// Double negation operator
prefix operator ~~

/// Double negation operator for Int8
/// Returns 1 if value is not equal to 0, 0 otherwise
prefix func ~~(value: Int8)->Int8{
    return (value>0) ? 1 : 0
}
/// Double negation operator for UInt8
/// Returns 1 if value is not equal to 0, 0 otherwise
prefix func ~~(value: UInt8)->UInt8{
    return (value>0) ? 1 : 0
}
/// Double negation operator for Int16
/// Returns 1 if value is not equal to 0, 0 otherwise
prefix func ~~(value: Int16)->Int16{
    return (value>0) ? 1 : 0
}
/// Double negation operator for UInt16
/// Returns 1 if value is not equal to 0, 0 otherwise
prefix func ~~(value: UInt16)->UInt16{
    return (value>0) ? 1 : 0
}
/// Double negation operator for Int32
/// Returns 1 if value is not equal to 0, 0 otherwise
prefix func ~~(value: Int32)->Int32{
    return (value>0) ? 1 : 0
}
/// Double negation operator for UInt32
/// Returns 1 if value is not equal to 0, 0 otherwise
prefix func ~~(value: UInt32)->UInt32{
    return (value>0) ? 1 : 0
}
/// Double negation operator for Int64
/// Returns 1 if value is not equal to 0, 0 otherwise
prefix func ~~(value: Int64)->Int64{
    return (value>0) ? 1 : 0
}
/// Double negation operator for UInt64
/// Returns 1 if value is not equal to 0, 0 otherwise
prefix func ~~(value: UInt64)->UInt64{
    return (value>0) ? 1 : 0
}


File: /Sources\CORE\Engine.swift
//
//  Engine.swift
//  mikrotik_router_manager
//
//  Created by dung.nt on 8/21/17.
//
//

import Foundation
public class Engine {
    
    public static let sharedInstance = Engine()
    
    private init() {
        loadConfig()
        
    }
    
    var ListComponent = Dictionary<ComponentType,BaseComponent>()
    
    func registerComponent(component :  BaseComponent){
        ListComponent[component.componentType()] = component
    }
    func getComponent(type : ComponentType) -> BaseComponent?{
        return ListComponent[type]
    }
    
    func loadComponentConfig(){
        
        for c in ListComponent {
            c.value.loadConfig()
        }
    }
    func startComponent(){
        for c in ListComponent {
            c.value.start()
        }
    }
    
    public func start(){
        loadComponentConfig()
        startComponent()
    }
}


File: /Sources\CORE\EngineConfig.swift
//
//  EngineConfig.swift
//  mikrotik_router_manager
//
//  Created by dung.nt on 8/21/17.
//
//

import Foundation

extension Engine{ /// extension register
    func loadConfig(){
        registerComponent(component: SessionManager())
        registerComponent(component: LogComponent())
        registerComponent(component: HttpServerComponent())
        registerComponent(component: MysqlConnection())
        
    }
    
}
public extension Engine{ /// extension get component
    public func mySQLConnection() -> MysqlConnection?{
        if let op = self.getComponent(type: ComponentType.DataBase) as? MysqlConnection{
            return op
        }
        return nil
    }
    public func getSession() -> SessionManager?{
        if let op = self.getComponent(type: ComponentType.Session) as? SessionManager{
            return op
        }
        return nil
    }
}


File: /Sources\CORE\HttpCustomerLogin.swift
//
//  HttpCustomerLogin.swift
//  CORE
//
//  Created by dung.nt on 9/25/17.
//

import Foundation
extension HttpServerComponent{
    func apiForCustommer(){
        let api = "/api/customer"
        router.get("\(api)/login") { (request, response, next) in
            response.send(json: ["status":200,"message":"ok"])
            next()
        }
    }
}


File: /Sources\CORE\HttpServerComponent.swift
//
//  HttpServerComponent.swift
//  mikrotik_router_manager
//
//  Created by dung.nt on 8/23/17.
//
//

import Foundation
import Kitura
import Credentials
import CredentialsHTTP
import KituraCORS
public class HttpServerComponent : BaseComponent{
    
    let router = Router()
    let credentials = Credentials()
    
    
    public override func componentType() -> ComponentType {
        return .HttpServer
    }
    public override func loadConfig() {
        
        Kitura.addHTTPServer(onPort: Engine.sharedInstance.getSession()?.http_port ?? 8080, with: router)
        
        let users = ["dungnt" : "12345","khanhnd":"12345"]
        let basicCredentials = CredentialsHTTPBasic(verifyPassword: { userId, password, callback in
            if let storedPassword = users[userId], storedPassword == password {
                callback(UserProfile(id: userId, displayName: userId, provider: "HTTPBasic"))
            } else {
                callback(nil)
            }
        })
        
        credentials.register(plugin: basicCredentials)
        
        router.all("/api", middleware: credentials)
        router.all(middleware: BodyParser())
        self.apiForCustommer()
        self.routerAPI()
        self.userAPI()
//        srouter.all("/ping", middleware: credentials)
        router.all("/ping") { (routerRequest, routerResponse, next) in
            routerResponse.headers["Access-Control-Allow-Origin"] = "*"
            try? Engine.sharedInstance.mySQLConnection()?.execute("SELECT * from tbl_router where ip_address='\(routerRequest.remoteAddress)'", onCompletion: { (results) in
                var arr = results.asRows
                if(results.success && arr?.count == 1){
                    
                    if let data = arr?[0]{
                        if let server_ip = data["ip_address"] as? String, let username = data["username"] as? String , let pwd : String = data["password"] as? String,let port : Int32 = data["port"] as? Int32 {
                            let mk = MikrotikConnection(host: server_ip, port: Int(port), userName: username, password: pwd)
                            let rs_ip = Request(api: "/ip/address/print", type: ApiType.GET, p: nil, q: ["comment":"hotspotip"], u: nil)
                            let r =  mk.sendAPI2(r: rs_ip)
                            if(r.0 == true && r.2?.SentenceData.count == 1){
                                if let address = r.2?.SentenceData[0]["address"]{
                                    if let ip = address.components(separatedBy: "/").first{
                                        routerResponse.send(json: ["status":200,"message":"ok","data":["ip":"http://\(ip)"]])
                                    }else{
                                        routerResponse.send(json: ["status":400,"message":"ok","data":["ip":""]])
                                    }
                                }else{
                                    routerResponse.send(json: ["status":400,"message":"không tồn tại remove trên database"])
                                }
                                
                            }else{
                               routerResponse.send(json: ["status":400,"message":"không tồn tại remove trên database"])
                            }
                        }else{
                            routerResponse.send(json: ["status":400,"message":"không tồn tại remove trên database"])
                        }
                    }else{
                        routerResponse.send(json: ["status":400,"message":"không tồn tại remove trên database"])
                    }
                }else{
                    routerResponse.send(json: ["status":400,"message":"không tồn tại remove trên database"])
                }
                
                
                next()
            })
            
            
            
        }
        
    }
    public override func start() {
        Kitura.run()
    }
 
}


File: /Sources\CORE\HttpUserAPI.swift
//
//  HttpUserAPI.swift
//  mikrotik_router_manager
//
//  Created by dung.nt on 9/14/17.
//
//

import Foundation

extension HttpServerComponent{
    func userAPI(){
        let api = "/user"

        router.post  (api) { (routerRequest, routerResponse, next) in
            routerResponse.headers["Access-Control-Allow-Origin"] = "*"
            routerResponse.headers["Content-type"] = "application/json"

            var profile_id : String?
            var router_id : String?
            var mac_address : String?
            var profileName : String!
            var connect_time : Int = 0
            for p in (routerRequest.body?.asURLEncoded ?? [:]){
                if(p.key == "profile_id"){
                    profile_id = p.value
                }else if(p.key == "router_id"){
                    router_id = p.value
                }else if(p.key == "mac_address"){
                    mac_address = p.value
                }
                
            }
            if(profile_id == nil || profile_id?.isEmpty == true || router_id == nil || router_id?.isEmpty == true || mac_address == nil || mac_address?.isEmpty == true){
                routerResponse.send(json: ["status":400,"message":"thiếu params"])
                next()
                return
            }
            if let p_name = Engine.sharedInstance.getSession()?.profiles[profile_id ?? ""]?["name"] as? String{
                profileName = p_name
            }
            if let _time = Engine.sharedInstance.getSession()?.profiles[profile_id ?? ""]?["time"] as? Int{
                connect_time = Int(_time)
            }
            if(profileName == nil || connect_time == 0){
                routerResponse.send(json: ["status":400,"message":"Không tìm thấy thông tin profile"])
                next()
                return
            }
            do{
                try Engine.sharedInstance.mySQLConnection()!.execute("SELECT * FROM `tbl_router` WHERE id = \(router_id!)", onCompletion: { (results) in
                    var arr = results.asRows
                    if(results.success && arr?.count == 1){
                        
                        if let data = arr?[0]{
                            if let server_ip = data["ip_address"] as? String, let username = data["username"] as? String , let pwd : String = data["password"] as? String,let port : Int32 = data["port"] as? Int32,let use_userman = data["use_userman"] as? Int32 {
                                let mk = MikrotikConnection(host: server_ip, port: Int(port), userName: username, password: pwd)
                                
                                let random_username = UUID().uuidString
                                let random_password = UUID().uuidString
                                if(use_userman == 1){
                                    /// USERMAN USER
                                    let req_create_user = Request(api: "/tool/user-manager/user/add", type: ApiType.ADD, p: ["username":random_username,"password":random_password,"customer":"admin","disabled":"no","shared-users":"1","caller-id":mac_address!], q: nil, u: nil)
                                    let add_profile_to_user = Request.init(api: "/tool/user-manager/user/create-and-activate-profile", type: ApiType.ADD, p: ["profile":profileName,"customer":"admin","numbers":random_username], q: nil, u: nil)
                                    
                                    _ = mk.sendAPIs(requests: [req_create_user,add_profile_to_user])
                                    
                                    routerResponse.send(json: ["status":200,"message":"ok","data":["username":random_username,"password":random_password]])
                                }else{
                                    /// HOTSPOT USER
                                    //ip hotspot user add name=abc password=abc profile=free_15p_2md_512 limit-uptime=15m
                                    let rq_add = Request(api: "/ip/hotspot/user/add", type: ApiType.ADD, p: ["name":random_username,"password":random_password,"profile":profileName,"limit-uptime":"\(connect_time)m"], q: nil, u: nil)
                                    let r = mk.sendAPIs(requests: [rq_add])
                                    
                                    routerResponse.send(json: ["status":200,"message":"ok","data":["username":random_username,"password":random_password]])
                                }
                                
                                
                            }else{
                                routerResponse.send(json: ["status":400,"message":"\(results.asError?.localizedDescription ?? "Lỗi lấy thông tin router")"])
                            }
                        }else{
                            routerResponse.send(json: ["status":400,"message":"\(results.asError?.localizedDescription ?? "Lỗi truy vấn SQL")"])
                        }
                        
                        //routerResponse.send(json: ["status":200,"message":"ok","data":results.asRows])
                    }else{
                        routerResponse.send(json: ["status":400,"message":"\(results.asError?.localizedDescription ?? "Lỗi truy vấn SQL")"])
                    }
                    next()
                })
                
                
            }catch{
                routerResponse.send(json: ["status":500,"message":"\(error.localizedDescription)"])
                next()
            }
            
            
            
            
        }
    }
}


File: /Sources\CORE\HtttpRouterAPI.swift
//
//  HtttpRouterAPI.swift
//  mikrotik_router_manager
//
//  Created by dung.nt on 8/25/17.
//
//

import Foundation
extension String {
    func toBool() -> Bool? {
        switch self {
        case "True", "true", "yes", "1":
            return true
        case "False", "false", "no", "0":
            return false
        default:
            return nil
        }
    }
}

extension HttpServerComponent{
    //// ----------------------------------------- API ROUTER -------------------------------------------------///
    /// GET LIST ROUTER
    func routerAPI(){
        let api = "/api/router"
        router.get(api) { (routerRequest, routerResponse, next) in
            do{
                try Engine.sharedInstance.mySQLConnection()?.execute("select * from tbl_router where customerName = '\(routerRequest.userProfile?.id ?? "")' ORDER BY id desc", onCompletion: { (results) in
                    if(results.success){
                        routerResponse.send(json: ["status":200,"data":results.asRows!])
                    }else{
                        routerResponse.send(json: ["status":400,"message":"\(results.asError?.localizedDescription ?? "Execute Error")"])
                    }
                })
            }catch{
                routerResponse.send(json: ["status":500,"message":"\(error.localizedDescription)"])
            }
            
            next()
        }
        
        /// DELETE
        router.delete(api) { (routerRequest, routerResponse, next) in
            
            var id_router : String?
            for p in (routerRequest.body?.asMultiPart ?? []){
                if(p.name == "id"){
                    id_router = p.body.asText
                }
            }
            guard id_router != nil else{
                routerResponse.send(json: ["status":400,"message":"missing id_router"])
                next()
                return
            }
            
            
            do{
                try Engine.sharedInstance.mySQLConnection()?.execute("DELETE FROM `tbl_router` WHERE id = \(id_router ?? "")", onCompletion: { (result) in
                    if(result.success){
                        routerResponse.send(json: ["status":200,"message":"\(result.asValue ?? "")"])
                        
                    }else{
                        routerResponse.send(json: ["status":400,"message":"\(result.asError?.localizedDescription ?? "Execute Query Error")"])
                        
                    }
                })
            }catch{
                routerResponse.send(json: ["status":500,"message":"\(error.localizedDescription)"])
            }
            next()
        }
        /// CREATE
        router.post(api) { (routerRequest, routerResponse, next) in
            var user_name : String?
            var password : String?
            var ip_adddress : String?
            var name : String?
            var des : String?
            var port : Int = 8728
            var type : Int = 0
            var use_userman : Bool = false
            for p in (routerRequest.body?.asMultiPart ?? []){
                if(p.name == "name"){
                    name = p.body.asText
                }else if p.name == "ip_address" {
                    ip_adddress = p.body.asText
                }else if p.name == "username"{
                    user_name = p.body.asText
                }else if p.name == "password" {
                    password = p.body.asText
                }else if p.name == "description" {
                    des = p.body.asText
                }else if p.name == "port" {
                    port = Int(p.body.asText ?? "8278")!
                }else if p.name == "type" {
                    type = Int(p.body.asText ?? "0")!
                }else if p.name == "use_userman" {
                    use_userman = (p.body.asText ?? "0").toBool()!
                }
            }
            
            let password_for_radius_login = UUID().uuidString
            
            /// 10.3.3.200 là ip cua router host
            
            /// TODO CHECK ROUTER DA DUOC ADD HAY CHUA
            
            if (user_name != nil && ip_adddress != nil && name != nil && password != nil){
                //// TRƯỜNG HỢP ROUTER LÀM LUÔN HOST RADIUS
                try? Engine.sharedInstance.mySQLConnection()?.execute("select * from `tbl_router` where ip_address = '\(ip_adddress ?? "")'", onCompletion: { (QueryResult) in
                    if(QueryResult.success == true && QueryResult.asRows?.count == 0){
                        let mk =  MikrotikConnection(host: ip_adddress!, port: port, userName: user_name!, password: password!)
                        
                        /// RADIUS SERVER
                        /// 1.0 lấy danh sách radius cũ
                        if (type == 0){
                            let requset = Request(api: "/radius/getall")
                            let result =  mk.sendAPIs(requests: [requset])
                            if result.0 == false {
                                routerResponse.send(json: ["status":400,"message":"\(result.1?.localizedDescription ?? "") " + "có thể do lỗi ko lấy được danh sách radius"])
                                next()
                                return
                            }
                            
                            /// 1.1 Xoá hết danh sách radius cũ
                            for r in result.2 ?? []{
                                for s in r.SentenceData{
                                    if let uid = s[".id"]{
                                        let requset_remove = Request(api: "/radius/remove")
                                        requset_remove.uid = uid
                                        requset_remove.apiType = .DEL
                                        _ = mk.sendAPI2(r: requset_remove)
                                        
                                    }
                                }
                            }
                            
                            /// 1.2 thêm máy chủ radius mới
                            let create_radius_params = ["address":"127.0.0.1","comment":"LOCAL_RADIUS","secret":password_for_radius_login,"service":"hotspot"]
                            let request_create_radius = Request(api: "/radius/add", type: ApiType.ADD, p: create_radius_params, q: nil, u: nil)
                            let rs_create_radius = mk.sendAPI2(r: request_create_radius)
                            if (rs_create_radius.0 == false){
                                routerResponse.send(json: ["status":400,"message":"không tạo được radius"])
                                next()
                                return
                            }
                            
                            let set_enable_incoming = Request(api: "/radius/incoming/set", type: ApiType.SET, p: ["accept":"yes","port":"1700"], q: nil, u: nil)
                            _ = mk.sendAPI2(r: set_enable_incoming)
                            
                            
                            /// b2 add profile and limit cho new router
                            /// b2.1 set path save DB
                            let s = Calendar.current.component(Calendar.Component.second, from: Date())
                            if(use_userman){
                                /// GET LIST OLD PROFILE
                                let list_old_profiles = mk.sendAPI2(r: Request(api: "/ip/hotspot/user/profile/print", type: ApiType.GET, p: nil, q: nil, u: nil))
                                if(list_old_profiles.0){
                                    /// XOA ALL PROFILE OLD
                                    var listRequestRemove = Array<Request>()
                                    for old in (list_old_profiles.2?.SentenceData ?? []).reversed(){
                                        if let name = old["name"]{
                                            if name != "default" {
                                                listRequestRemove.append(Request(api: "/ip/hotspot/user/profile/remove", type: ApiType.ADD, p: ["numbers":name], q: nil, u: nil))
                                            }
                                            
                                        }
                                    }
                                    if listRequestRemove.count != 0 {
                                        _ = mk.sendAPIs(requests: listRequestRemove)
                                    }
                                }
                                
                                
                                
                            }else{
                                let userman_set_db_path = Request(api: "/tool/user-manager/database/set", type: ApiType.SET, p: ["db-path":"mk/\(UUID().uuidString)/db"], q: nil, u: nil)
                                let rs_userman_set_db_path = mk.sendAPI2(r: userman_set_db_path)
                                
                                if (rs_userman_set_db_path.0 == false){
                                    routerResponse.send(json: ["status":400,"message":"userman không khởi tạo được đường dẫn db \(rs_userman_set_db_path.1?.localizedDescription ?? "")"])
                                    next()
                                    return
                                }
                                /// b2.2 add limit and profile
                                
                                for p in Engine.sharedInstance.getSession()!.profiles{
                                    if let name : String = p.value["name"] as? String,let md = p.value["md"] as? Int,let mu = p.value["mu"] as? Int,let time = p.value["time"] as? Int{
                                        //rq profile , profile limitation , profile profile-limitation
                                        let rq_add = Request(api: "/tool/user-manager/profile/add", type: ApiType.ADD, p: ["name":name,"owner":"admin","starts-at":"logon","validity":"\(time * 60)"], q: nil, u: nil)
                                        let rq_add_profile_limitation = Request(api: "/tool/user-manager/profile/limitation/add", type: ApiType.ADD, p: ["name":name,"owner":"admin","uptime-limit":"\(time * 60)","rate-limit-rx":"\(mu * 1024)","rate-limit-tx":"\(md * 1024)","rate-limit-min-rx":"\((mu * 1024) / 2)","rate-limit-min-tx":"\((md * 1024) / 2)"], q: nil, u: nil)
                                        let rq_add_profile_profile_limitation = Request(api: "/tool/user-manager/profile/profile-limitation/add", type: ApiType.ADD, p: ["limitation":name,"profile":name], q: nil, u: nil)
                                        _ = mk.sendAPIs(requests: [rq_add,rq_add_profile_limitation,rq_add_profile_profile_limitation])
                                    }
                                }
                            }
                            
                            
                            
                            /// LOCAL USERMAN ADD ROUTER
                            /// 3.1 kiểm tra danh sách đã được add xem đã add ip này hay chưa
                            let rq_get_router_in_userman = Request(api: "/tool/user-manager/router/print")
                            let rs_get_router_in_userman = mk.sendAPI2(r: rq_get_router_in_userman)
                            if rs_get_router_in_userman.0 == false {
                                routerResponse.send(json: ["status":400,"message":"lỗi không lấy được thông tin id của rourer được đăng ký trên userman \(rs_get_router_in_userman.1?.localizedDescription ?? "")"])
                                next()
                                return
                            }
                            /// 3.2 xoá nếu tồn tại
                            for s in rs_get_router_in_userman.2?.SentenceData ?? []{
                                if let _ip = s["ip-address"],let uid = s[".id"] {
                                    if ("127.0.0.1" == _ip){
                                        let requset_remove = Request(api: "/tool/user-manager/router/remove")
                                        requset_remove.uid = uid
                                        requset_remove.apiType = .DEL
                                        _ = mk.sendAPI2(r: requset_remove)
                                    }
                                }
                            }
                            
                            
                            
                            /// 3.3 thêm mới router
                            let usernam_add_router_params = ["coa-port":"1700","customer":"admin","disabled":"no","log":"auth-fail","use-coa":"yes","ip-address":"127.0.0.1","shared-secret":password_for_radius_login,"name":"Localhost"]
                            let userman_create_router = Request(api: "/tool/user-manager/router/add", type: ApiType.ADD, p: usernam_add_router_params, q: nil, u: nil)
                            let rs_userman_create_router = mk.sendAPI2(r: userman_create_router)
                            if (rs_userman_create_router.0 == false){
                                routerResponse.send(json: ["status":400,"message":"userman không tạo được router \(rs_userman_create_router.1?.localizedDescription ?? "")"])
                                next()
                                return
                            }
                            
                            /// 4 CONFIG HOTSPOT // DEFAULT ether2 // không sử dụng userman
                            if(use_userman){
                                let calc = (s & 254).setb7(0)
                                
                                let hotspot_pool_name = "hotspot-pool_\(s)"
                                let dhcp_for_hotspot_name = "dhcp-for-hotspot-\(s)"
                                let hotspot_profile_name = "hotspot-profile_\(s)"
                                let rq_add_dns = Request(api: "/ip/dns/set", type: ApiType.SET, p: ["servers":"8.8.8.8","allow-remote-requests":"yes"], q: nil, u: nil)
                                
                                let rq_cr_ip_add = Request(api: "/ip/address/add", type: ApiType.ADD, p: ["address":"10.3.\(s).1/23","interface":"ether2","comment":"hotspotip"], q: nil, u: nil)
                                
                                
                                var rq_cr_pool : Request = Request(api: "")
                                if(calc < s){
                                    rq_cr_pool = Request(api: "/ip/pool/add", type: ApiType.ADD, p: ["name":hotspot_pool_name,"ranges":"10.3.\(calc).2-10.3.\(s).254"], q: nil, u: nil)
                                }else{
                                    rq_cr_pool = Request(api: "/ip/pool/add", type: ApiType.ADD, p: ["name":hotspot_pool_name,"ranges":"10.3.\(s).2-10.3.\(s+1).254"], q: nil, u: nil)
                                }
                                
                                
                                
                                let rq_cr_dhcp_server_network = Request(api: "/ip/dhcp-server/network/add", type: ApiType.ADD, p: ["address":"10.3.\(calc).0/23","gateway":"10.3.\(s).1","dns-server":"8.8.8.8"], q: nil, u: nil)
                                
                                let rq_cr_dhcp_server = Request(api: "/ip/dhcp-server/add", type: ApiType.ADD, p: ["name":dhcp_for_hotspot_name,"interface":"ether2","lease-time":"10m","address-pool":hotspot_pool_name,"bootp-support":"static","authoritative":"yes","disabled":"no"], q: nil, u: nil)
                                
                                let rq_cr_add_nad_ip = Request(api: "/ip/firewall/nat/add", type: ApiType.ADD, p: ["chain":"srcnat","action":"masquerade","src-address":"10.3.\(calc).0/23"], q: nil, u: nil)
                                
                                let rq_cr_add_hotspot_profile = Request(api: "/ip/hotspot/profile/add", type: ApiType.ADD, p: ["name":hotspot_profile_name,"hotspot-address":"10.3.\(s).1","use-radius":"no"], q: nil, u: nil)
                                
                                let rq_cr_add_hotspot = Request(api: "/ip/hotspot/add", type: ApiType.ADD, p: ["address-pool":hotspot_pool_name,"interface":"ether2","profile":hotspot_profile_name,"disabled":"no","name":"HOTSPOT_\(s)"], q: nil, u: nil)
                                
                                let walled_garden = Request(api: "/ip/hotspot/walled-garden/ip/add", type: ApiType.ADD, p: ["action":"accept","disabled":"no","dst-address":Engine.sharedInstance.getSession()!.hotspot_server_ip_address], q: nil, u: nil)
                                
                                /// ADD NEW PROFILE
                                var arr_profiles = Array<Request>()
                                arr_profiles = arr_profiles + [rq_add_dns,rq_cr_ip_add,rq_cr_pool,rq_cr_dhcp_server_network,rq_cr_dhcp_server,rq_cr_add_nad_ip,rq_cr_add_hotspot_profile,rq_cr_add_hotspot,walled_garden]
                                for p in Engine.sharedInstance.getSession()!.profiles{
                                    if let name : String = p.value["name"] as? String,let md = p.value["md"] as? Int,let mu = p.value["mu"] as? Int{
                                        //ip hotspot user profile add shared-users=1 name=profile_name address-pool=hotspot-pool_51 rate-limit=1048576/1048576
                                        let rq = Request(api: "/ip/hotspot/user/profile/add", type: ApiType.ADD, p: ["shared-users":"1","name":name,"address-pool":"hotspot-pool_\(s)","rate-limit":"\(mu)k/\(md)k"], q: nil, u: nil)
                                        
                                        arr_profiles.append(rq)
                                    }
                                }
                                if(arr_profiles.count != 0){
                                    _ = mk.sendAPIs(requests: arr_profiles)
                                }
                                
                                _ = mk.sendAPIs(requests: arr_profiles)
                            }
                            
                            try? Engine.sharedInstance.mySQLConnection()?.execute("INSERT INTO `tbl_router` (`name`, `username`, `password`, `ip_address`, `description`,`port`,`type`,`use_userman`,`customerName`) VALUES ('\(name ?? "")', '\(user_name ?? "")', '\(password ?? "")', '\(ip_adddress ?? "")', '\(des ?? "")', \(port), \(type),\(use_userman ? 1 : 0),\(routerRequest.userProfile?.id ?? "")", onCompletion: { (results) in
                                if(results.success){
                                    try? Engine.sharedInstance.mySQLConnection()?.execute("select * from `tbl_router` where ip_address = '\(ip_adddress ?? "")'", onCompletion: { (QueryResult) in
                                        
                                        let resultRow = QueryResult.asRows ?? []
                                        if(resultRow.count == 1){
                                            if let _newID = resultRow[0]["id"] as? Int32{
                                                let rq_edit_id = Request(api: "/system/identity/set", type: ApiType.ADD, p: ["name":"\(_newID)"], q: nil, u: nil)
                                                let r = mk.sendAPI2(r: rq_edit_id)
                                                print(r.0)
                                            }
                                        }
                                        
                                        
                                        routerResponse.send(json: ["status":200,"message":"ok","data":resultRow])
                                        next()
                                    })
                                    
                                }else{
                                    routerResponse.send(json: ["status":400,"message":"\(results.asError?.localizedDescription ?? "Unknow error")"])
                                    next()
                                }
                            })
                        }
                        else{
                            /// host radius server public
                            
                            let mk_public = MikrotikConnection(host: Engine.sharedInstance.getSession()!.public_server_radius_ip, port: Engine.sharedInstance.getSession()!.public_server_radius_port, userName: Engine.sharedInstance.getSession()!.public_server_radius_username, password: Engine.sharedInstance.getSession()!.public_server_radius_password)
                            
                            let requset = Request(api: "/radius/getall")
                            let result =  mk.sendAPIs(requests: [requset])
                            if result.0 == false {
                                routerResponse.send(json: ["status":400,"message":"\(result.1?.localizedDescription ?? "có thể do lỗi ko lấy được danh sách radius")"])
                                next()
                                return
                            }
                            
                            /// 1.1 Xoá hết danh sách radius cũ
                            for r in result.2 ?? []{
                                for s in r.SentenceData{
                                    if let uid = s[".id"]{
                                        let requset_remove = Request(api: "/radius/remove")
                                        requset_remove.uid = uid
                                        requset_remove.apiType = .DEL
                                        _ = mk.sendAPI2(r: requset_remove)
                                        
                                    }
                                }
                            }
                            
                            /// 1.2 thêm máy chủ radius mới
                            let create_radius_params = ["address":Engine.sharedInstance.getSession()!.public_server_radius_ip,"comment":"PUBLIC_RADIUS","secret":password_for_radius_login,"service":"hotspot,ppp"]
                            let request_create_radius = Request(api: "/radius/add", type: ApiType.ADD, p: create_radius_params, q: nil, u: nil)
                            let rs_create_radius = mk.sendAPI2(r: request_create_radius)
                            if (rs_create_radius.0 == false){
                                routerResponse.send(json: ["status":400,"message":"không tạo được radius"])
                                next()
                                return
                            }
                            
                            let set_enable_incoming = Request(api: "/radius/incoming/set", type: ApiType.SET, p: ["accept":"yes","port":"1700"], q: nil, u: nil)
                            _ = mk.sendAPI2(r: set_enable_incoming)
                            
                            
                            /// 4 CONFIG HOTSPOT // DEFAULT ether2
                            
                            /// 4.1 dns --> ip dns set servers=8.8.8.8 allow-remote-requests=yes
                            //let rq_add_dns = Request(api: "/ip/dns/set", type: ApiType.SET, p: ["servers":"8.8.8.8","allow-remote-requests":"yes"], q: nil, u: nil)
                            /// 4.2 create IP address -> ip address add address=192.168.50.1/24 interface=ether2
                            //let rq_cr_ip_add = Request(api: "/ip/address/add", type: ApiType.ADD, p: ["address":"192.168.50.1/24","interface":"ether2"], q: nil, u: nil)
                            /// 4.3 create add pool -> ip pool add name=hotspot-pool ranges=192.168.50.2-192.168.50.254
                            //Request(api: "", type: ApiType.ADD, p: ["":""], q: nil, u: nil)
                            //let rq_cr_pool = Request(api: "/ip/pool/add", type: ApiType.ADD, p: ["name":"hotspot-pool","ranges":"192.168.50.2-192.168.50.254"], q: nil, u: nil)
                            /// 4.4 create dhcp-server network -> ip dhcp-server network add address=192.168.50.0/24 gateway=192.168.50.1 dns-server=8.8.8.8
                            //let rq_cr_dhcp_server_network = Request(api: "/ip/dhcp-server/network/add", type: ApiType.ADD, p: ["address":"192.168.50.0/24","gateway":"192.168.50.1","dns-server":"8.8.8.8"], q: nil, u: nil)
                            /// 4.5 create dhcp-server -> ip dhcp-server add name=dhcp-for-hotspot interface=ether2 lease-time=10m address-pool=hotspot-pool bootp-support=static authoritative=yes  disabled=no
                            //let rq_cr_dhcp_server = Request(api: "/ip/dhcp-server/add", type: ApiType.ADD, p: ["name":"dhcp-for-hotspot","interface":"ether2","lease-time":"10m","address-pool":"hotspot-pool","bootp-support":"static","authoritative":"yes","disabled":"no"], q: nil, u: nil)
                            /// 4.6 add nas cho day ip -> ip firewall nat add chain=srcnat action=masquerade src-address=192.168.50.0/24
                            //let rq_cr_add_nad_ip = Request(api: "/ip/firewall/nat/add", type: ApiType.ADD, p: ["chain":"srcnat","action":"masquerade","src-address":"192.168.50.0/24"], q: nil, u: nil)
                            /// 4.7 create hotspot profile server -> ip hotspot profile add name=hotspot-profile hotspot-address=192.168.50.1 use-radius=no
                            //let rq_cr_add_hotspot_profile = Request(api: "/ip/hotspot/profile/add", type: ApiType.ADD, p: ["name":"hotspot-profile","hotspot-address":"192.168.50.1","use-radius":"yes"], q: nil, u: nil)
                            /// 4.8 create hotspot -> ip hotspot add address-pool=hotspot-pool interface=ether2 profile=hotspot-profile disabled=no name=HOTSPOT
                            //let rq_cr_add_hotspot = Request(api: "/ip/hotspot/add", type: ApiType.ADD, p: ["address-pool":"hotspot-pool","interface":"ether2","profile":"hotspot-profile","disabled":"no","name":"HOTSPOT"], q: nil, u: nil)
                            /// 4.9 mở ip (if use PUBLIC ROUTER ) -> ip hotspot walled-garden ip add action=accept disabled=no dst-address=192.168.70.253 server=!HOTSPOT
                            //_ = mk.sendAPIs(requests: [rq_add_dns,rq_cr_ip_add,rq_cr_pool,rq_cr_dhcp_server_network,rq_cr_dhcp_server,rq_cr_add_nad_ip,rq_cr_add_hotspot_profile,rq_cr_add_hotspot])
                            
                            
                            /// ADD ROUTER TO PUBLIC RADIUS
                            let usernam_add_router_params = ["coa-port":"1700","customer":"admin","disabled":"no","log":"auth-fail","use-coa":"yes","ip-address":ip_adddress!,"shared-secret":password_for_radius_login,"name":"\(name ?? "")__\(ip_adddress ?? "")"]
                            let userman_create_router = Request(api: "/tool/user-manager/router/add", type: ApiType.ADD, p: usernam_add_router_params, q: nil, u: nil)
                            let rs_userman_create_router = mk_public.sendAPI2(r: userman_create_router)
                            if (rs_userman_create_router.0 == false){
                                routerResponse.send(json: ["status":400,"message":"userman không tạo được router \(rs_userman_create_router.1?.localizedDescription ?? "")"])
                                next()
                                return
                            }
                            
                            try? Engine.sharedInstance.mySQLConnection()?.execute("INSERT INTO `tbl_router` (`name`, `username`, `password`, `ip_address`, `description`,`port`,`type`,`use_userman`) VALUES ('\(name ?? "")', '\(user_name ?? "")', '\(password ?? "")', '\(ip_adddress ?? "")', '\(des ?? "")', \(port), \(type),\(use_userman ? 1 : 0))", onCompletion: { (results) in
                                if(results.success){
                                    try? Engine.sharedInstance.mySQLConnection()?.execute("select * from `tbl_router` where ip_address = '\(ip_adddress ?? "")'", onCompletion: { (QueryResult) in
                                        routerResponse.send(json: ["status":200,"message":"ok","data":QueryResult.asRows ?? []])
                                        next()
                                    })
                                    
                                }else{
                                    routerResponse.send(json: ["status":400,"message":"\(results.asError?.localizedDescription ?? "Unknow error")"])
                                    next()
                                }
                            })
                        }
                    }else{
                        routerResponse.send(json: ["status":400,"message":"Đã tồn tại server"])
                        next()
                    }
                })
                
                /// b1 connect to router lấy về danh sách radius
            }else{
                routerResponse.send(json: ["status":400,"message":"missing param"])
                next()
            }
            
        }
        router.put(api) { (routerRequest, routerResponse, next) in
            var user_name : String?
            var password : String?
            var ip_adddress : String?
            var name : String?
            var des : String?
            var id_router : String?
            var strUpdate = ""
            for p in (routerRequest.body?.asMultiPart ?? []){
                if(p.name == "name"){
                    name = p.body.asText
                    if(name?.isEmpty == false){
                        if(strUpdate.isEmpty == false){
                            strUpdate = strUpdate + ","
                        }
                        strUpdate += "`name`='\(name!)'"
                    }
                }else if p.name == "ip_address" {
                    ip_adddress = p.body.asText
                    if(ip_adddress?.isEmpty == false){
                        if(strUpdate.isEmpty == false){
                            strUpdate = strUpdate + ","
                        }
                        strUpdate += "`ip_address`='\(ip_adddress!)'"
                    }
                }else if p.name == "username"{
                    user_name = p.body.asText
                    if(user_name?.isEmpty == false){
                        if(user_name?.isEmpty == false){
                            strUpdate = strUpdate + ","
                        }
                        strUpdate += "`username`='\(user_name!)'"
                    }
                }else if p.name == "password" {
                    password = p.body.asText
                    if(password?.isEmpty == false){
                        if(password?.isEmpty == false){
                            strUpdate = strUpdate + ","
                        }
                        strUpdate += "`password`='\(password!)'"
                    }
                    
                }else if p.name == "description" {
                    des = p.body.asText
                    if(des?.isEmpty == false){
                        if(des?.isEmpty == false){
                            strUpdate = strUpdate + ","
                        }
                        strUpdate += "`description`='\(des!)'"
                    }
                }else if p.name == "id"{
                    id_router = p.body.asText
                }
            }
            
            guard id_router != nil else{
                routerResponse.send(json: ["status":400,"message":"missing id_router"])
                next()
                return
            }
            
            guard user_name != nil || ip_adddress != nil || name != nil || password != nil else{
                routerResponse.send(json: ["status":400,"message":"no update"])
                next()
                return
            }
            
            
            
            do{
                try Engine.sharedInstance.mySQLConnection()?.execute("update `tbl_router` set \(strUpdate) WHERE `id` = \(id_router ?? "")", onCompletion: { (result) in
                    if(result.success){
                        routerResponse.send(json: ["status":200])
                    }else{
                        routerResponse.send(json: ["status":400,"message":"\(result.asError?.localizedDescription ?? "Unknow Error")"])
                    }
                })
            }catch{
                routerResponse.send(json: ["status":500,"message":"\(error.localizedDescription)"])
            }
            
            
            next()
        }
    }
}


File: /Sources\CORE\LogComponent.swift
//
//  LogComponent.swift
//  mikrotik_router_manager
//
//  Created by dung.nt on 8/21/17.
//
//

import Foundation
import HeliumLogger
import LoggerAPI
class LogComponent : BaseComponent{
    
    override func componentType() -> ComponentType {
        return .Logging
    }
    override func loadConfig() {
        HeliumLogger.use()
    }
    override func start() {
        Log.info("")
    }
}


File: /Sources\CORE\MikrotikConnection.swift
//
//  MikrotikConnection.swift
//  mikrotik_router_manager
//
//  Created by dung.nt on 8/21/17.
//
//

import Foundation
import Socket
import CryptoSwift

public enum ReturnType {
    case NONE
    case DONE
    case TRAP
    case HALT
    case RE
}
public enum SentenceError : Error{
    case NoData
    case DataFailure
    case DataInvalidFormat
}
public enum MikrotikConnectionError : Error{
    case LOGIN
    case API
    case MISSING_PARAM
    case UNKNOW
}

public enum ApiType {
    case SET
    case GET
    case ADD
    case DEL
}

public class Request{
    var api : String!
    var params : Dictionary<String,String>?
    var apiType : ApiType? = .GET
    var querys : Dictionary<String,String>?

    var uid : String?
    init(api : String,type : ApiType? = .GET,p : Dictionary<String,String>? = nil,q : Dictionary<String,String>? = nil,u : String? = nil ) {
        self.api = api
        self.apiType = type
        self.params = p
        self.querys = q
        self.uid = u
    }
}

public class Sentence{
    
    
    
    var returnType : ReturnType = .NONE /// 0 = NONE
    var SentenceData = Array<Dictionary<String,String>>()
    var isDone : Bool = false
    private var oldData : Data!
    func ReadLength(data : Data) -> (Int,Int){ /// LEN - SIZE
        if data.count < 1 {
            return (-1,0)
        }
        let firstChar = data[0]
        if (firstChar & 0xE0) == 0xE0 {
            
        }else if (firstChar & 0xC0) == 0xC0 {
            
        }else if (firstChar & 0x80) == 0x80 { // 2-byte encoded length
            var c = Int(firstChar)
             c = c & ~0xC0;
             c = (c << 8) | Int(data[1])
            return (c,2)
        }else { // assume 1-byte encoded length...same on both LE and BE systems
            return (Int(firstChar),1)
        }
        return (-1,0)
    }
    
    init(data : Data) throws {
        
        guard data.count > 3 else {
            throw SentenceError.NoData
        }
        let len = self.ReadLength(data: data)
        guard len.0 > 0 else {
            throw SentenceError.DataInvalidFormat
        }
        let typeData = data.subdata(in: len.1..<len.0+len.1)
        let strType = String(data: typeData, encoding: String.Encoding.utf8)
        guard strType != nil else {
            throw SentenceError.DataInvalidFormat
        }
        if strType! == "!done" {
            self.returnType = .DONE
            isDone = true
            self.unPackDone(data: data.subdata(in: len.0+len.1..<data.count))
        }else if strType == "!trap"{
            self.returnType = .TRAP
            isDone = true
            self.unPackTrap(data: data.subdata(in: len.0+len.1..<data.count))
        }else if strType == "!re"{
            self.returnType = .RE
            SentenceData.append([:])
            self.unPackRe(data: data.subdata(in: len.0+len.1..<data.count))
        }
        
    }
    func updateData(data : Data){
        if oldData != nil {
            oldData.append(data)
            self.unPackRe(data: oldData)
            oldData = nil
        }else{
            self.unPackRe(data: data)
        }
    }
    
    func unPackDone(data : Data){
        let len = self.ReadLength(data: data)
        if len.0 > 0 {
            let contentData = data.subdata(in: len.1..<len.0+len.1)
            if let strContent = String(data: contentData, encoding: String.Encoding.utf8){
                let arr = strContent.components(separatedBy: "=")
                if arr.count == 3 {
                    var dic = Dictionary<String,String>()
                    dic[arr[1]] = arr[2]
                    SentenceData.append(dic)
                }
            }
            self.unPackDone(data: data.subdata(in: len.0+len.1..<data.count))
        }
    }
    
    func unPackTrap(data : Data){
        let len = self.ReadLength(data: data)
        if len.0 > 0 {
            let contentData = data.subdata(in: len.1..<len.0+len.1)
            if let strContent = String(data: contentData, encoding: String.Encoding.ascii){
                let arr = strContent.components(separatedBy: "=")
                if arr.count == 3 {
                    var dic = Dictionary<String,String>()
                    dic[arr[1]] = arr[2]
                    SentenceData.append(dic)
                }
            }
            self.unPackTrap(data: data.subdata(in: len.0+len.1..<data.count))
        }
    }
    
    func unPackRe(data : Data){
        let len = self.ReadLength(data: data)
        if len.0 < 0 {
            return
        }
        if data.count < len.1 || data.count < len.0 + len.1 {
            oldData = data
            return // dư data
        }
        let contentData = data.subdata(in: len.1..<len.0+len.1)
        if let strContent = String(data: contentData, encoding: String.Encoding.utf8){
            if strContent.isEmpty == false {
                if strContent == "!re" {
                    SentenceData.append([:])
                }else{
                    if strContent != "!done" {
                        let arr = strContent.components(separatedBy: "=")
                        if arr.count == 3 {
                            SentenceData[SentenceData.count - 1][arr[1]] = arr[2]
                        }
                        
                    }
                }
                //SentenceData.append(strContent)
            }
            if strContent != "!done" {
                self.unPackRe(data: data.subdata(in: len.0+len.1..<data.count))
            }else{
                isDone = true
            }
            
        }
        
    }
    
}


class MikrotikConnection{
    var userName : String!
    var password : String!
    var hostName : String!
    var hostPort : Int = 0
    var tcpSocket : Socket!
    
    init(host : String,port : Int,userName : String,password : String) {
        self.userName = userName
        self.password = password
        self.hostName = host
        self.hostPort = port
    }
    
    func send(word : String,endsentence : Bool) -> Bool{
        if word.isEmpty {
            if endsentence {
                do{
                    try self.tcpSocket.write(from: Data(bytes: [0x0]))
                }catch{
                    return false
                }
            }
            return true
        }else{
            if let data = word.data(using: String.Encoding.utf8){
                var len = data.count
                do{
                    
                    if len < 0x80 {
                        var data = Data()
                        data.append([UInt8(len)], count: 1)
                        try self.tcpSocket.write(from: data)
                    }else if len < 0x4000 {
                        len = len | 0x8000;
                        try self.tcpSocket.write(from: Data(bytes: [UInt8(len >> 8)]))
                        try self.tcpSocket.write(from: Data(bytes: [UInt8(len)]))
                    }else if len < 0x20000 {
                        len = len | 0xC00000;
                        try self.tcpSocket.write(from: Data(bytes: [UInt8(len >> 16)]))
                        try self.tcpSocket.write(from: Data(bytes: [UInt8(len >> 8)]))
                        try self.tcpSocket.write(from: Data(bytes: [UInt8(len)]))
                    }
                    else if len < 0x10000000 {
                        len = len | 0xE0000000;
                        try self.tcpSocket.write(from: Data(bytes: [UInt8(len >> 24)]))
                        try self.tcpSocket.write(from: Data(bytes: [UInt8(len >> 16)]))
                        try self.tcpSocket.write(from: Data(bytes: [UInt8(len >> 8)]))
                        try self.tcpSocket.write(from: Data(bytes: [UInt8(len)]))
                    }else{
                        try self.tcpSocket.write(from: Data(bytes: [0xF0]))
                        try self.tcpSocket.write(from: Data(bytes: [UInt8(len >> 24)]))
                        try self.tcpSocket.write(from: Data(bytes: [UInt8(len >> 16)]))
                        try self.tcpSocket.write(from: Data(bytes: [UInt8(len >> 8)]))
                        try self.tcpSocket.write(from: Data(bytes: [UInt8(len)]))
                    }
                    try self.tcpSocket.write(from: data)
                    if endsentence {
                        try self.tcpSocket.write(from: Data(bytes: [0x0]))
                    }
                    return true
                }catch{
                    return false
                }
                
            }
        }
        return false
    }
    func sendAPIs(requests : Array<Request>) -> (Bool,Error?,Array<Sentence>?){
        do{
            tcpSocket = try Socket.create()
            tcpSocket.readBufferSize = 4096
            try tcpSocket.connect(to: self.hostName, port: Int32(self.hostPort), timeout: 2000)
            /// SEND GET TOKEN
            var success : Bool = false
            success =  self.send(word: "/login", endsentence: true)
            guard success == true else {
                tcpSocket.close()
                return (false,MikrotikConnectionError.LOGIN,nil)
            }
            /// READ TOKEN
            var data : Data = Data()
            var lenRead =  try tcpSocket.read(into: &data)
            guard lenRead > 0 else {
                tcpSocket.close()
                return (false,MikrotikConnectionError.LOGIN,nil)
            }
            /// read type
            let sentence = try Sentence(data: data)
            guard sentence.returnType == .DONE else {
                tcpSocket.close()
                return (false,MikrotikConnectionError.LOGIN,nil)
            }
            /// SEND LOGIN
            success =  self.send(word: "/login", endsentence: false)
            guard success == true && self.userName != nil else {
                tcpSocket.close()
                return (false,MikrotikConnectionError.LOGIN,nil)
            }
            success = self.send(word: "=name=\(self.userName!)",endsentence: false)
            guard success == true && sentence.SentenceData.count == 1 else {
                tcpSocket.close()
                return (false,MikrotikConnectionError.LOGIN,nil)
            }
            
            
            
            var chal = self.hexStringToBytes("00")!
            chal = chal + password.data(using: String.Encoding.ascii)!.bytes
            chal = chal + self.hexStringToBytes(sentence.SentenceData[0]["ret"]!)!
            chal = chal.md5()
            success = self.send(word: "=response=00\(chal.toHexString())",endsentence: true)
            guard success == true && sentence.SentenceData.count == 1 else {
                tcpSocket.close()
                return (false,MikrotikConnectionError.LOGIN,nil)
            }
            data.removeAll()
            lenRead = 0
            lenRead =  try tcpSocket.read(into: &data)
            guard lenRead > 0 else {
                tcpSocket.close()
                return (false,MikrotikConnectionError.LOGIN,nil)
            }
            let sentenceLoginS2 = try Sentence(data: data)
            guard sentenceLoginS2.returnType == .DONE else {
                tcpSocket.close()
                return (false,MikrotikConnectionError.LOGIN,nil)
            }
            /// LOGIN SUCCESS
            var result = Array<Sentence>()
            for r in requests{
                if r.apiType == .GET {
                    success = self.send(word: r.api, endsentence:false)
                    guard success == true else {
                        tcpSocket.close()
                        return (false,MikrotikConnectionError.API,nil)
                    }
                    success = self.send(word: "=detail=", endsentence:false)
                    guard success == true else {
                        tcpSocket.close()
                        return (false,MikrotikConnectionError.API,nil)
                    }
                    if r.querys != nil {
                        var i = 0
                        for p in r.querys! {
                            i = i + 1
                            success = self.send(word: "?\(p.key)=\(p.value)", endsentence: false)
                            guard success == true else {
                                tcpSocket.close()
                                return (false,MikrotikConnectionError.API,nil)
                                
                            }
                        }
                    }
                    success = self.send(word: "", endsentence: true)
                    
                    guard success == true else {
                        tcpSocket.close()
                        return (false,MikrotikConnectionError.API,nil)
                    }
                    
                    var sentenceData : Sentence!
                    repeat{
                        data.removeAll()
                        lenRead = 0
                        lenRead =  try tcpSocket.read(into: &data)
                        if sentenceData == nil {
                            sentenceData = try Sentence(data: data)
                        }
                        else{
                            sentenceData.updateData(data: data)
                        }
                    }while !sentenceData.isDone
                    
                    
                    result.append(sentenceData)
                    
                }
                else if r.apiType == .SET{
                    if r.params == nil{
                        return (false,MikrotikConnectionError.MISSING_PARAM,nil)
                    }
                    success = self.send(word: r.api, endsentence:false)
                    guard success == true else {
                        tcpSocket.close()
                        return (false,MikrotikConnectionError.API,nil)
                    }
                    if r.uid != nil {
                        success = self.send(word: "=.id=\(r.uid!)", endsentence:false)
                        guard success == true else {
                            tcpSocket.close()
                            return (false,MikrotikConnectionError.API,nil)
                        }
                    }
                    
                    
                    
                    if r.params != nil {
                        var i = 0
                        for p in r.params! {
                            i = i + 1
                            success = self.send(word: "=\(p.key)=\(p.value)", endsentence: false)
                            guard success == true else {
                                tcpSocket.close()
                                return (false,MikrotikConnectionError.API,nil)
                                
                            }
                        }
                    }
                    success = self.send(word: "", endsentence: true)
                    
                    guard success == true else {
                        tcpSocket.close()
                        return (false,MikrotikConnectionError.API,nil)
                    }
                    
                    var sentenceData : Sentence!
                    repeat{
                        data.removeAll()
                        lenRead = 0
                        lenRead =  try tcpSocket.read(into: &data)
                        if sentenceData == nil {
                            sentenceData = try Sentence(data: data)
                        }
                        else{
                            sentenceData.updateData(data: data)
                        }
                    }while !sentenceData.isDone
                    
                    
                    result.append(sentenceData)
                    
                    
                }
                else if r.apiType == .ADD{
                    if r.params == nil {
                        return (false,MikrotikConnectionError.MISSING_PARAM,nil)
                    }
                    success = self.send(word: r.api, endsentence:false)
                    guard success == true else {
                        tcpSocket.close()
                        return (false,MikrotikConnectionError.API,nil)
                    }
                    if r.params != nil {
                        var i = 0
                        for p in r.params! {
                            i = i + 1
                            success = self.send(word: "=\(p.key)=\(p.value)", endsentence: false)
                            guard success == true else {
                                tcpSocket.close()
                                return (false,MikrotikConnectionError.API,nil)
                                
                            }
                        }
                    }
                    success = self.send(word: "", endsentence: true)
                    
                    guard success == true else {
                        tcpSocket.close()
                        return (false,MikrotikConnectionError.API,nil)
                    }
                    
                    var sentenceData : Sentence!
                    repeat{
                        data.removeAll()
                        lenRead = 0
                        lenRead =  try tcpSocket.read(into: &data)
                        if sentenceData == nil {
                            sentenceData = try Sentence(data: data)
                        }
                        else{
                            sentenceData.updateData(data: data)
                        }
                    }while !sentenceData.isDone
                    
                    
                    result.append(sentenceData)
                    
                }
                else{ // DELETE
                    if r.uid == nil {
                        return (false,MikrotikConnectionError.MISSING_PARAM,nil)
                    }
                    success = self.send(word: r.api, endsentence:false)
                    guard success == true else {
                        tcpSocket.close()
                        return (false,MikrotikConnectionError.API,nil)
                    }
                    success = self.send(word: "=.id=\(r.uid!)", endsentence:true)
                    guard success == true else {
                        tcpSocket.close()
                        return (false,MikrotikConnectionError.API,nil)
                    }
                    var sentenceData : Sentence!
                    repeat{
                        data.removeAll()
                        lenRead = 0
                        lenRead =  try tcpSocket.read(into: &data)
                        if sentenceData == nil {
                            sentenceData = try Sentence(data: data)
                        }
                        else{
                            sentenceData.updateData(data: data)
                        }
                    }while !sentenceData.isDone
                    
                    
                    result.append(sentenceData)
                }
            }
            tcpSocket.close()
            return (true,nil,result)
        }catch{
            return (false,error,nil)
        }
    }
    
    func sendAPI2(r : Request) -> (Bool,Error?,Sentence?){ // ISSUCCESS - ERROR - Sentence
        do {
            tcpSocket = try Socket.create()
            tcpSocket.readBufferSize = 4096
            try tcpSocket.connect(to: self.hostName, port: Int32(self.hostPort), timeout: 2000)
            /// SEND GET TOKEN
            var success : Bool = false
            success =  self.send(word: "/login", endsentence: true)
            guard success == true else {
                tcpSocket.close()
                return (false,MikrotikConnectionError.LOGIN,nil)
            }
            /// READ TOKEN
            var data : Data = Data()
            var lenRead =  try tcpSocket.read(into: &data)
            guard lenRead > 0 else {
                tcpSocket.close()
                return (false,MikrotikConnectionError.LOGIN,nil)
            }
            /// read type
            let sentence = try Sentence(data: data)
            guard sentence.returnType == .DONE else {
                tcpSocket.close()
                return (false,MikrotikConnectionError.LOGIN,nil)
            }
            /// SEND LOGIN
            success =  self.send(word: "/login", endsentence: false)
            guard success == true && self.userName != nil else {
                tcpSocket.close()
                return (false,MikrotikConnectionError.LOGIN,nil)
            }
            success = self.send(word: "=name=\(self.userName!)",endsentence: false)
            guard success == true && sentence.SentenceData.count == 1 else {
                tcpSocket.close()
                return (false,MikrotikConnectionError.LOGIN,nil)
            }
            
            
            
            var chal = self.hexStringToBytes("00")!
            chal = chal + password.data(using: String.Encoding.ascii)!.bytes
            chal = chal + self.hexStringToBytes(sentence.SentenceData[0]["ret"]!)!
            chal = chal.md5()
            success = self.send(word: "=response=00\(chal.toHexString())",endsentence: true)
            guard success == true && sentence.SentenceData.count == 1 else {
                tcpSocket.close()
                return (false,MikrotikConnectionError.LOGIN,nil)
            }
            data.removeAll()
            lenRead = 0
            lenRead =  try tcpSocket.read(into: &data)
            guard lenRead > 0 else {
                tcpSocket.close()
                return (false,MikrotikConnectionError.LOGIN,nil)
            }
            let sentenceLoginS2 = try Sentence(data: data)
            guard sentenceLoginS2.returnType == .DONE else {
                tcpSocket.close()
                return (false,MikrotikConnectionError.LOGIN,nil)
            }
            /// send abc
            
            if r.apiType == .GET {
                success = self.send(word: r.api, endsentence:false)
                guard success == true else {
                    tcpSocket.close()
                    return (false,MikrotikConnectionError.API,nil)
                }
                success = self.send(word: "=detail=", endsentence:false)
                guard success == true else {
                    tcpSocket.close()
                    return (false,MikrotikConnectionError.API,nil)
                }
                if r.querys != nil {
                    var i = 0
                    for p in r.querys! {
                        i = i + 1
                        success = self.send(word: "?\(p.key)=\(p.value)", endsentence: false)
                        guard success == true else {
                            tcpSocket.close()
                            return (false,MikrotikConnectionError.API,nil)
                            
                        }
                    }
                }
                success = self.send(word: "", endsentence: true)
                
                guard success == true else {
                    tcpSocket.close()
                    return (false,MikrotikConnectionError.API,nil)
                }
                
                var sentenceData : Sentence!
                repeat{
                    data.removeAll()
                    lenRead = 0
                    lenRead =  try tcpSocket.read(into: &data)
                    if sentenceData == nil {
                        sentenceData = try Sentence(data: data)
                    }
                    else{
                        sentenceData.updateData(data: data)
                    }
                }while !sentenceData.isDone
                
                
                tcpSocket.close()
                return (true,nil,sentenceData)
            }
            else if r.apiType == .SET{
                if r.params == nil{
                    return (false,MikrotikConnectionError.MISSING_PARAM,nil)
                }
                success = self.send(word: r.api, endsentence:false)
                guard success == true else {
                    tcpSocket.close()
                    return (false,MikrotikConnectionError.API,nil)
                }
                if r.uid != nil {
                    success = self.send(word: "=.id=\(r.uid!)", endsentence:false)
                    guard success == true else {
                        tcpSocket.close()
                        return (false,MikrotikConnectionError.API,nil)
                    }
                }
                
                
                
                if r.params != nil {
                    var i = 0
                    for p in r.params! {
                        i = i + 1
                        success = self.send(word: "=\(p.key)=\(p.value)", endsentence: false)
                        guard success == true else {
                            tcpSocket.close()
                            return (false,MikrotikConnectionError.API,nil)
                            
                        }
                    }
                }
                success = self.send(word: "", endsentence: true)
                
                guard success == true else {
                    tcpSocket.close()
                    return (false,MikrotikConnectionError.API,nil)
                }
                
                var sentenceData : Sentence!
                repeat{
                    data.removeAll()
                    lenRead = 0
                    lenRead =  try tcpSocket.read(into: &data)
                    if sentenceData == nil {
                        sentenceData = try Sentence(data: data)
                    }
                    else{
                        sentenceData.updateData(data: data)
                    }
                }while !sentenceData.isDone
                
                
                tcpSocket.close()
                return (true,nil,sentenceData)
                
                
            }
            else if r.apiType == .ADD{
                if r.params == nil {
                    return (false,MikrotikConnectionError.MISSING_PARAM,nil)
                }
                success = self.send(word: r.api, endsentence:false)
                guard success == true else {
                    tcpSocket.close()
                    return (false,MikrotikConnectionError.API,nil)
                }
                if r.params != nil {
                    var i = 0
                    for p in r.params! {
                        i = i + 1
                        success = self.send(word: "=\(p.key)=\(p.value)", endsentence: false)
                        guard success == true else {
                            tcpSocket.close()
                            return (false,MikrotikConnectionError.API,nil)
                            
                        }
                    }
                }
                success = self.send(word: "", endsentence: true)
                
                guard success == true else {
                    tcpSocket.close()
                    return (false,MikrotikConnectionError.API,nil)
                }
                
                var sentenceData : Sentence!
                repeat{
                    data.removeAll()
                    lenRead = 0
                    lenRead =  try tcpSocket.read(into: &data)
                    if sentenceData == nil {
                        sentenceData = try Sentence(data: data)
                    }
                    else{
                        sentenceData.updateData(data: data)
                    }
                }while !sentenceData.isDone
                
                
                tcpSocket.close()
                return (true,nil,sentenceData)
                
            }
            else{ // DELETE
                if r.uid == nil {
                    return (false,MikrotikConnectionError.MISSING_PARAM,nil)
                }
                success = self.send(word: r.api, endsentence:false)
                guard success == true else {
                    tcpSocket.close()
                    return (false,MikrotikConnectionError.API,nil)
                }
                success = self.send(word: "=.id=\(r.uid!)", endsentence:true)
                guard success == true else {
                    tcpSocket.close()
                    return (false,MikrotikConnectionError.API,nil)
                }
                var sentenceData : Sentence!
                repeat{
                    data.removeAll()
                    lenRead = 0
                    lenRead =  try tcpSocket.read(into: &data)
                    if sentenceData == nil {
                        sentenceData = try Sentence(data: data)
                    }
                    else{
                        sentenceData.updateData(data: data)
                    }
                }while !sentenceData.isDone
                
                
                tcpSocket.close()
                return (true,nil,sentenceData)
            }
            
        } catch  {
            return (false,error,nil)
        }
    }
    
    func sendAPI(api : String , params : Dictionary<String,String>? = nil,apiType : ApiType = .GET,querys : Dictionary<String,String>? = nil,uid : String? = nil) -> (Bool,Error?,Sentence?){ // ISSUCCESS - ERROR - Sentence
        do {
            tcpSocket = try Socket.create()
            tcpSocket.readBufferSize = 4096
            try tcpSocket.connect(to: self.hostName, port: Int32(self.hostPort), timeout: 2000)
            /// SEND GET TOKEN
            var success : Bool = false
            success =  self.send(word: "/login", endsentence: true)
            guard success == true else {
                tcpSocket.close()
                return (false,MikrotikConnectionError.LOGIN,nil)
            }
            /// READ TOKEN
            var data : Data = Data()
            var lenRead =  try tcpSocket.read(into: &data)
            guard lenRead > 0 else {
                tcpSocket.close()
                return (false,MikrotikConnectionError.LOGIN,nil)
            }
            /// read type
            let sentence = try Sentence(data: data)
            guard sentence.returnType == .DONE else {
                tcpSocket.close()
                return (false,MikrotikConnectionError.LOGIN,nil)
            }
            /// SEND LOGIN
            success =  self.send(word: "/login", endsentence: false)
            guard success == true && self.userName != nil else {
                tcpSocket.close()
                return (false,MikrotikConnectionError.LOGIN,nil)
            }
            success = self.send(word: "=name=\(self.userName!)",endsentence: false)
            guard success == true && sentence.SentenceData.count == 1 else {
                tcpSocket.close()
                return (false,MikrotikConnectionError.LOGIN,nil)
            }
            
            
            
            var chal = self.hexStringToBytes("00")!
            chal = chal + password.data(using: String.Encoding.ascii)!.bytes
            chal = chal + self.hexStringToBytes(sentence.SentenceData[0]["ret"]!)!
            chal = chal.md5()
            success = self.send(word: "=response=00\(chal.toHexString())",endsentence: true)
            guard success == true && sentence.SentenceData.count == 1 else {
                tcpSocket.close()
                return (false,MikrotikConnectionError.LOGIN,nil)
            }
            data.removeAll()
            lenRead = 0
            lenRead =  try tcpSocket.read(into: &data)
            guard lenRead > 0 else {
                tcpSocket.close()
                return (false,MikrotikConnectionError.LOGIN,nil)
            }
            let sentenceLoginS2 = try Sentence(data: data)
            guard sentenceLoginS2.returnType == .DONE else {
                tcpSocket.close()
                return (false,MikrotikConnectionError.LOGIN,nil)
            }
            /// send abc
            
            if apiType == .GET {
                success = self.send(word: api, endsentence:false)
                guard success == true else {
                    tcpSocket.close()
                    return (false,MikrotikConnectionError.API,nil)
                }
                success = self.send(word: "=detail=", endsentence:false)
                guard success == true else {
                    tcpSocket.close()
                    return (false,MikrotikConnectionError.API,nil)
                }
                if querys != nil {
                    var i = 0
                    for p in querys! {
                        i = i + 1
                        success = self.send(word: "?\(p.key)=\(p.value)", endsentence: false)
                        guard success == true else {
                            tcpSocket.close()
                            return (false,MikrotikConnectionError.API,nil)
                            
                        }
                    }
                }
                success = self.send(word: "", endsentence: true)
                
                guard success == true else {
                    tcpSocket.close()
                    return (false,MikrotikConnectionError.API,nil)
                }
                
                var sentenceData : Sentence!
                repeat{
                    data.removeAll()
                    lenRead = 0
                    lenRead =  try tcpSocket.read(into: &data)
                    if sentenceData == nil {
                        sentenceData = try Sentence(data: data)
                    }
                    else{
                        sentenceData.updateData(data: data)
                    }
                }while !sentenceData.isDone
                
                
                tcpSocket.close()
                return (true,nil,sentenceData)
            }
            else if apiType == .SET{
                if params == nil || uid == nil {
                    return (false,MikrotikConnectionError.MISSING_PARAM,nil)
                }
                success = self.send(word: api, endsentence:false)
                guard success == true else {
                    tcpSocket.close()
                    return (false,MikrotikConnectionError.API,nil)
                }
                success = self.send(word: "=.id=\(uid!)", endsentence:false)
                guard success == true else {
                    tcpSocket.close()
                    return (false,MikrotikConnectionError.API,nil)
                }
                
                
                if params != nil {
                    var i = 0
                    for p in params! {
                        i = i + 1
                        success = self.send(word: "=\(p.key)=\(p.value)", endsentence: false)
                        guard success == true else {
                            tcpSocket.close()
                            return (false,MikrotikConnectionError.API,nil)
                            
                        }
                    }
                }
                success = self.send(word: "", endsentence: true)
                
                guard success == true else {
                    tcpSocket.close()
                    return (false,MikrotikConnectionError.API,nil)
                }
                
                var sentenceData : Sentence!
                repeat{
                    data.removeAll()
                    lenRead = 0
                    lenRead =  try tcpSocket.read(into: &data)
                    if sentenceData == nil {
                        sentenceData = try Sentence(data: data)
                    }
                    else{
                        sentenceData.updateData(data: data)
                    }
                }while !sentenceData.isDone
                
                
                tcpSocket.close()
                return (true,nil,sentenceData)
                
                
            }
            else if apiType == .ADD{
                if params == nil {
                    return (false,MikrotikConnectionError.MISSING_PARAM,nil)
                }
                success = self.send(word: api, endsentence:false)
                guard success == true else {
                    tcpSocket.close()
                    return (false,MikrotikConnectionError.API,nil)
                }
                if params != nil {
                    var i = 0
                    for p in params! {
                        i = i + 1
                        success = self.send(word: "=\(p.key)=\(p.value)", endsentence: false)
                        guard success == true else {
                            tcpSocket.close()
                            return (false,MikrotikConnectionError.API,nil)
                            
                        }
                    }
                }
                success = self.send(word: "", endsentence: true)
                
                guard success == true else {
                    tcpSocket.close()
                    return (false,MikrotikConnectionError.API,nil)
                }
                
                var sentenceData : Sentence!
                repeat{
                    data.removeAll()
                    lenRead = 0
                    lenRead =  try tcpSocket.read(into: &data)
                    if sentenceData == nil {
                        sentenceData = try Sentence(data: data)
                    }
                    else{
                        sentenceData.updateData(data: data)
                    }
                }while !sentenceData.isDone
                
                
                tcpSocket.close()
                return (true,nil,sentenceData)
                
            }
            else{ // DELETE
                if uid == nil {
                    return (false,MikrotikConnectionError.MISSING_PARAM,nil)
                }
                success = self.send(word: api, endsentence:false)
                guard success == true else {
                    tcpSocket.close()
                    return (false,MikrotikConnectionError.API,nil)
                }
                success = self.send(word: "=.id=\(uid!)", endsentence:true)
                guard success == true else {
                    tcpSocket.close()
                    return (false,MikrotikConnectionError.API,nil)
                }
                var sentenceData : Sentence!
                repeat{
                    data.removeAll()
                    lenRead = 0
                    lenRead =  try tcpSocket.read(into: &data)
                    if sentenceData == nil {
                        sentenceData = try Sentence(data: data)
                    }
                    else{
                        sentenceData.updateData(data: data)
                    }
                }while !sentenceData.isDone
                
                
                tcpSocket.close()
                return (true,nil,sentenceData)
            }
            
        } catch  {
            return (false,error,nil)
        }
    }
    
    func hexStringToBytes(_ string: String) -> [UInt8]? {
        let length = string.characters.count
        if length & 1 != 0 {
            return nil
        }
        var bytes = [UInt8]()
        bytes.reserveCapacity(length/2)
        var index = string.startIndex
        for _ in 0..<length/2 {
            let nextIndex = string.index(index, offsetBy: 2)
            if let b = UInt8(string[index..<nextIndex], radix: 16) {
                bytes.append(b)
            } else {
                return nil
            }
            index = nextIndex
        }
        return bytes
    }
}


File: /Sources\CORE\MysqlConnection.swift
import SwiftKueryMySQL
import SwiftKuery
import LoggerAPI

public enum executeError : Error {
    case NoConnected
}
/// CONNECTION

public class MysqlConnection : BaseComponent{
    
    var mysqlConnection : MySQLConnection!
    
    public override func componentType() -> ComponentType{
      return ComponentType.DataBase
    }
    public override func start(){
        mysqlConnection = MySQLConnection(host: Engine.sharedInstance.getSession()?.mysqlHostName ?? "", user: Engine.sharedInstance.getSession()?.mysqlUserName ?? "", password: Engine.sharedInstance.getSession()?.mysqlPassword ?? "", database: Engine.sharedInstance.getSession()?.mysqlDBName ?? "", port: 3306, unixSocket: nil, clientFlag: 0, characterSet: nil, reconnect: true)
        mysqlConnection.connect { error in
            Log.info("MYSQL CONNECTED")
            if error != nil {
                Log.info("MYSQL CONFIG FAILURE" + (error?.localizedDescription ?? ""))
                fatalError()
            }
        }
    }
    public override func loadConfig(){
        
    }
    
    
    public func execute(_ raw: String, onCompletion: @escaping ((QueryResult) -> ())) throws{
        if mysqlConnection.isConnected {
            mysqlConnection.execute(raw, onCompletion: onCompletion)
        }else{
            throw executeError.NoConnected
        }
    }
    
}


File: /Sources\CORE\profile_config.plist
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<array>
	<dict>
		<key>id</key>
		<integer>0</integer>
		<key>name</key>
		<string>free_30p_2md_1mu</string>
		<key>up</key>
		<integer>1</integer>
		<key>down</key>
		<integer>2</integer>
		<key>time</key>
		<integer>30</integer>
	</dict>
	<dict>
		<key>id</key>
		<integer>1</integer>
		<key>name</key>
		<string>free_30p_2md_2mu</string>
		<key>up</key>
		<integer>2</integer>
		<key>down</key>
		<integer>2</integer>
		<key>time</key>
		<integer>30</integer>
	</dict>
	<dict>
		<key>id</key>
		<integer>2</integer>
		<key>name</key>
		<string>free_30p_3md_1mu</string>
		<key>up</key>
		<integer>1</integer>
		<key>down</key>
		<integer>3</integer>
		<key>time</key>
		<integer>30</integer>
	</dict>
	<dict>
		<key>id</key>
		<integer>3</integer>
		<key>name</key>
		<string>free_30p_3md_2mu</string>
		<key>up</key>
		<integer>2</integer>
		<key>down</key>
		<integer>3</integer>
		<key>time</key>
		<integer>30</integer>
	</dict>
	<dict>
		<key>id</key>
		<integer>4</integer>
		<key>name</key>
		<string>free_30p_5md_2mu</string>
		<key>up</key>
		<integer>2</integer>
		<key>down</key>
		<integer>5</integer>
		<key>time</key>
		<integer>30</integer>
	</dict>
	<dict>
		<key>id</key>
		<integer>5</integer>
		<key>name</key>
		<string>free_30p_5md_3mu</string>
		<key>up</key>
		<integer>3</integer>
		<key>down</key>
		<integer>5</integer>
		<key>time</key>
		<integer>30</integer>
	</dict>
	<dict>
		<key>id</key>
		<integer>6</integer>
		<key>name</key>
		<string>free_45p_2md_1mu</string>
		<key>up</key>
		<integer>1</integer>
		<key>down</key>
		<integer>2</integer>
		<key>time</key>
		<integer>45</integer>
	</dict>
	<dict>
		<key>id</key>
		<integer>7</integer>
		<key>name</key>
		<string>free_45p_2md_2mu</string>
		<key>up</key>
		<integer>2</integer>
		<key>down</key>
		<integer>2</integer>
		<key>time</key>
		<integer>45</integer>
	</dict>
	<dict>
		<key>id</key>
		<integer>8</integer>
		<key>name</key>
		<string>free_45p_3md_1mu</string>
		<key>up</key>
		<integer>1</integer>
		<key>down</key>
		<integer>3</integer>
		<key>time</key>
		<integer>45</integer>
	</dict>
	<dict>
		<key>id</key>
		<integer>9</integer>
		<key>name</key>
		<string>free_45p_3md_2mu</string>
		<key>up</key>
		<integer>2</integer>
		<key>down</key>
		<integer>3</integer>
		<key>time</key>
		<integer>45</integer>
	</dict>
	<dict>
		<key>id</key>
		<integer>10</integer>
		<key>name</key>
		<string>free_45p_5md_2mu</string>
		<key>up</key>
		<integer>2</integer>
		<key>down</key>
		<integer>5</integer>
		<key>time</key>
		<integer>45</integer>
	</dict>
	<dict>
		<key>id</key>
		<integer>11</integer>
		<key>name</key>
		<string>free_45p_5md_3mu</string>
		<key>up</key>
		<integer>3</integer>
		<key>down</key>
		<integer>5</integer>
		<key>time</key>
		<integer>45</integer>
	</dict>
    
    
    
    <dict>
        <key>id</key>
        <integer>12</integer>
        <key>name</key>
        <string>free_60p_2md_1mu</string>
        <key>up</key>
        <integer>1</integer>
        <key>down</key>
        <integer>2</integer>
        <key>time</key>
        <integer>60</integer>
    </dict>
    <dict>
        <key>id</key>
        <integer>13</integer>
        <key>name</key>
        <string>free_60p_2md_2mu</string>
        <key>up</key>
        <integer>2</integer>
        <key>down</key>
        <integer>2</integer>
        <key>time</key>
        <integer>60</integer>
    </dict>
    <dict>
        <key>id</key>
        <integer>14</integer>
        <key>name</key>
        <string>free_60p_3md_1mu</string>
        <key>up</key>
        <integer>1</integer>
        <key>down</key>
        <integer>3</integer>
        <key>time</key>
        <integer>60</integer>
    </dict>
    <dict>
        <key>id</key>
        <integer>15</integer>
        <key>name</key>
        <string>free_60p_3md_2mu</string>
        <key>up</key>
        <integer>2</integer>
        <key>down</key>
        <integer>3</integer>
        <key>time</key>
        <integer>60</integer>
    </dict>
    <dict>
        <key>id</key>
        <integer>16</integer>
        <key>name</key>
        <string>free_60p_5md_2mu</string>
        <key>up</key>
        <integer>2</integer>
        <key>down</key>
        <integer>5</integer>
        <key>time</key>
        <integer>60</integer>
    </dict>
    <dict>
        <key>id</key>
        <integer>17</integer>
        <key>name</key>
        <string>free_60p_5md_3mu</string>
        <key>up</key>
        <integer>3</integer>
        <key>down</key>
        <integer>5</integer>
        <key>time</key>
        <integer>60</integer>
    </dict>
    
    
    <dict>
        <key>id</key>
        <integer>18</integer>
        <key>name</key>
        <string>free_15p_2md_1mu</string>
        <key>up</key>
        <integer>1</integer>
        <key>down</key>
        <integer>2</integer>
        <key>time</key>
        <integer>15</integer>
    </dict>
    <dict>
        <key>id</key>
        <integer>19</integer>
        <key>name</key>
        <string>free_15p_2md_2mu</string>
        <key>up</key>
        <integer>2</integer>
        <key>down</key>
        <integer>2</integer>
        <key>time</key>
        <integer>15</integer>
    </dict>
    <dict>
        <key>id</key>
        <integer>20</integer>
        <key>name</key>
        <string>free_15p_3md_1mu</string>
        <key>up</key>
        <integer>1</integer>
        <key>down</key>
        <integer>3</integer>
        <key>time</key>
        <integer>15</integer>
    </dict>
    <dict>
        <key>id</key>
        <integer>21</integer>
        <key>name</key>
        <string>free_15p_3md_2mu</string>
        <key>up</key>
        <integer>2</integer>
        <key>down</key>
        <integer>3</integer>
        <key>time</key>
        <integer>15</integer>
    </dict>
    <dict>
        <key>id</key>
        <integer>22</integer>
        <key>name</key>
        <string>free_15p_5md_2mu</string>
        <key>up</key>
        <integer>2</integer>
        <key>down</key>
        <integer>5</integer>
        <key>time</key>
        <integer>15</integer>
    </dict>
    <dict>
        <key>id</key>
        <integer>23</integer>
        <key>name</key>
        <string>free_15p_5md_3mu</string>
        <key>up</key>
        <integer>3</integer>
        <key>down</key>
        <integer>5</integer>
        <key>time</key>
        <integer>15</integer>
    </dict>
    
	
</array>
</plist>


File: /Sources\CORE\SessionManager.swift
//
//  SessionManager.swift
//  mikrotik_router_manager
//
//  Created by dung.nt on 8/25/17.
//
//

import Foundation
import Configuration

public class SessionManager : BaseComponent{
    
    

    
    var mysqlHostName : String = "wificonnect.ddns.net"
    var mysqlUserName : String = "root"
    var mysqlPassword : String = "Anhdung!@321"
    var mysqlDBName : String = "router_manager"
    var dataStorePath : String = "db.plist"
    var public_server_radius_ip : String = "10.3.3.202"
    var public_server_radius_username : String = "admin"
    var public_server_radius_password : String = "123456"
    var public_server_radius_port : Int = 8728
    var hotspot_server_ip_address :String =  "10.3.3.30"
    
    
    var http_port : Int = 8080
    
    var profiles : Dictionary<String,Dictionary<String,Any>> = [
        "0":["id":0,"name":"free_test_1p_2md_2mu","md":2048,"mu":2048,"time":1],
        
        "1":["id":1,"name":"free_15p_2md_512kmu","md":2048,"mu":512,"time":15],
        "3":["id":3,"name":"free_15p_3md_640kmu","md":3072,"mu":640,"time":15],
        "5":["id":5,"name":"free_15p_5md_1mu","md":5 * 1024,"mu":1024,"time":15],
        
        "7":["id":7,"name":"free_30p_2md_512kmu","md":2048,"mu":512,"time":30],
        "9":["id":9,"name":"free_30p_3md_640kmu","md":3072,"mu":640,"time":30],
        "11":["id":11,"name":"free_30p_5md_1mu","md":5 * 1024,"mu":1024,"time":30],
        
        "13":["id":13,"name":"free_45p_2md_512kmu","md":2048,"mu":512,"time":45],
        "15":["id":15,"name":"free_45p_3md_640kmu","md":3072,"mu":640,"time":45],
        "17":["id":17,"name":"free_45p_5md_1mu","md":5 * 1024,"mu":1024,"time":45],
        
        "19":["id":19,"name":"free_60p_2md_512kmu","md":2048,"mu":512,"time":60],  // 1h
        "21":["id":21,"name":"free_60p_3md_640kmu","md":3072,"mu":640,"time":60],
        "23":["id":23,"name":"free_60p_5md_1mu","md":5 * 1024,"mu":1024,"time":60],
        
        "24":["id":24,"name":"package_1d_5md_1mu","md":3 * 1024,"mu":512,"time":1440],// 1 day
        "25":["id":25,"name":"package_1d_5md_1mu","md":5 * 1024,"mu":1024,"time":1440],
        "27":["id":27,"name":"package_1d_9md_1.3mu","md":9 * 1024,"mu":2048,"time":1440],
        "29":["id":29,"name":"package_1d_15md_2.2mu","md":15 * 1024,"mu":4096,"time":1440],
        "30":["id":30,"name":"package_1d_20md_2.8mu","md":20 * 1024,"mu":10240,"time":1440],
        
        "31":["id":31,"name":"package_1w_5md_1mu","md":3 * 1024,"mu":512,"time":1440 * 7],// 7 day
        "32":["id":32,"name":"package_1w_5md_1mu","md":5 * 1024,"mu":1024,"time":1440 * 7],
        "33":["id":33,"name":"package_1w_9md_1.3mu","md":9 * 1024,"mu":2048,"time":1440 * 7],
        "34":["id":34,"name":"package_1w_15md_2.2mu","md":15 * 1024,"mu":4096,"time":1440 * 7],
        "35":["id":35,"name":"package_1w_20md_2.8mu","md":20 * 1024,"mu":10240,"time":1440 * 7],
        
        "36":["id":36,"name":"package_1m_5md_1mu","md":3 * 1024,"mu":512,"time":1440 * 30],// 30 day
        "37":["id":37,"name":"package_1m_5md_1mu","md":5 * 1024,"mu":1024,"time":1440 * 30],
        "38":["id":38,"name":"package_1m_9md_1.3mu","md":9 * 1024,"mu":2048,"time":1440 * 30],
        "39":["id":39,"name":"package_1m_15md_2.2mu","md":15 * 1024,"mu":4096,"time":1440 * 30],
        "40":["id":40,"name":"package_1m_20md_2.8mu","md":20 * 1024,"mu":10240,"time":1440 * 30]
    ]
    
    public let manager = ConfigurationManager()
    
    public override func componentType() -> ComponentType {
        return .Session
    }
    override init() {
        manager.load(.commandLineArguments)
    }
    public override func loadConfig() {
        
    }
    public override func start() {
        
    }
}


File: /Sources\SERVER\main.swift


import Foundation
import CORE

//let task = Process()
//
//task.launchPath = "/sbin/ping"
//task.arguments = ["10.3.2.172","-t","1"]
//let pipe = Pipe()
//task.standardOutput = pipe
//task.launch()
//
//let data = pipe.fileHandleForReading.readDataToEndOfFile()
//let output: String = String(data: data, encoding: .utf8)!
//
//print(output)

Engine.sharedInstance.start()


