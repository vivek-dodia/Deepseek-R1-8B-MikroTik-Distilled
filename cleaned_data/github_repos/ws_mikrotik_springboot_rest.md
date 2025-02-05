# Repository Information
Name: ws_mikrotik_springboot_rest

# Directory Structure
Directory structure:
└── github_repos/ws_mikrotik_springboot_rest/
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
    │   │       ├── pack-11afc1c57a8eca448a62c1313474d6d767ab2e94.idx
    │   │       └── pack-11afc1c57a8eca448a62c1313474d6d767ab2e94.pack
    │   ├── packed-refs
    │   └── refs/
    │       ├── heads/
    │       │   └── master
    │       ├── remotes/
    │       │   └── origin/
    │       │       └── HEAD
    │       └── tags/
    ├── .gitignore
    ├── .mvn/
    │   └── wrapper/
    │       ├── maven-wrapper.jar
    │       ├── maven-wrapper.properties
    │       └── MavenWrapperDownloader.java
    ├── mvnw
    ├── mvnw.cmd
    ├── pom.xml
    ├── Procfile
    ├── src/
    │   ├── main/
    │   │   ├── java/
    │   │   │   └── br/
    │   │   │       └── com/
    │   │   │           └── trixsolucao/
    │   │   │               └── mkws/
    │   │   │                   ├── controller/
    │   │   │                   │   ├── HotSpotController.java
    │   │   │                   │   ├── OpenConnection.java
    │   │   │                   │   ├── PPPoeController.java
    │   │   │                   │   ├── ResourcesController.java
    │   │   │                   │   └── response/
    │   │   │                   │       ├── DefaultResponseEnum.java
    │   │   │                   │       ├── GenericResponse.java
    │   │   │                   │       └── ModelResponse.java
    │   │   │                   ├── exception/
    │   │   │                   │   └── HeaderException.java
    │   │   │                   ├── filter/
    │   │   │                   │   └── RequestFilter.java
    │   │   │                   ├── mkapi/
    │   │   │                   │   ├── ConnectionBean.java
    │   │   │                   │   └── Mikrotik.java
    │   │   │                   ├── MkwsApplication.java
    │   │   │                   ├── model/
    │   │   │                   │   ├── FirewallNat.java
    │   │   │                   │   ├── HotspotActiveUser.java
    │   │   │                   │   ├── HotspotHost.java
    │   │   │                   │   ├── HotspotUser.java
    │   │   │                   │   ├── mapping/
    │   │   │                   │   │   ├── MapToObject.java
    │   │   │                   │   │   └── MkMapping.java
    │   │   │                   │   ├── MkCommand.java
    │   │   │                   │   ├── NetworkInterface.java
    │   │   │                   │   ├── PPPActiveUser.java
    │   │   │                   │   ├── PPPProfiles.java
    │   │   │                   │   ├── PPPUsers.java
    │   │   │                   │   ├── RadiusProfile.java
    │   │   │                   │   ├── RadiusUser.java
    │   │   │                   │   ├── Resources.java
    │   │   │                   │   └── TypesList.java
    │   │   │                   └── util/
    │   │   │                       └── JasyptTools.java
    │   │   └── resources/
    │   │       ├── application-dev.yml
    │   │       └── application.properties
    │   └── test/
    │       └── java/
    │           └── br/
    │               └── com/
    │                   └── trixsolucao/
    │                       └── mkws/
    │                           └── MkwsApplicationTests.java
    └── system.properties


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
	url = https://github.com/renanccortes/ws_mikrotik_springboot_rest.git
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
0000000000000000000000000000000000000000 56379c870accf28ed6f6f934a997d78714983f3d vivek-dodia <vivek.dodia@icloud.com> 1738606453 -0500	clone: from https://github.com/renanccortes/ws_mikrotik_springboot_rest.git


File: /.git\logs\refs\heads\master
0000000000000000000000000000000000000000 56379c870accf28ed6f6f934a997d78714983f3d vivek-dodia <vivek.dodia@icloud.com> 1738606453 -0500	clone: from https://github.com/renanccortes/ws_mikrotik_springboot_rest.git


File: /.git\logs\refs\remotes\origin\HEAD
0000000000000000000000000000000000000000 56379c870accf28ed6f6f934a997d78714983f3d vivek-dodia <vivek.dodia@icloud.com> 1738606453 -0500	clone: from https://github.com/renanccortes/ws_mikrotik_springboot_rest.git


File: /.git\packed-refs
# pack-refs with: peeled fully-peeled sorted 
56379c870accf28ed6f6f934a997d78714983f3d refs/remotes/origin/master


File: /.git\refs\heads\master
56379c870accf28ed6f6f934a997d78714983f3d


File: /.git\refs\remotes\origin\HEAD
ref: refs/remotes/origin/master


File: /.gitignore
HELP.md
target/
!.mvn/wrapper/maven-wrapper.jar
!**/src/main/**
!**/src/test/**

### STS ###
.apt_generated
.classpath
.factorypath
.project
.settings
.springBeans
.sts4-cache

### IntelliJ IDEA ###
.idea
*.iws
*.iml
*.ipr

### NetBeans ###
/nbproject/private/
/nbbuild/
/dist/
/nbdist/
/.nb-gradle/
build/

### VS Code ###
File: /.mvn\wrapper\maven-wrapper.properties
distributionUrl=https://repo.maven.apache.org/maven2/org/apache/maven/apache-maven/3.6.3/apache-maven-3.6.3-bin.zip
wrapperUrl=https://repo.maven.apache.org/maven2/io/takari/maven-wrapper/0.5.6/maven-wrapper-0.5.6.jar


File: /.mvn\wrapper\MavenWrapperDownloader.java
/*
 * Copyright 2007-present the original author or authors.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *      https://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */
import java.net.*;
import java.io.*;
import java.nio.channels.*;
import java.util.Properties;

public class MavenWrapperDownloader {

    private static final String WRAPPER_VERSION = "0.5.6";
    /**
     * Default URL to download the maven-wrapper.jar from, if no 'downloadUrl' is provided.
     */
    private static final String DEFAULT_DOWNLOAD_URL = "https://repo.maven.apache.org/maven2/io/takari/maven-wrapper/"
        + WRAPPER_VERSION + "/maven-wrapper-" + WRAPPER_VERSION + ".jar";

    /**
     * Path to the maven-wrapper.properties file, which might contain a downloadUrl property to
     * use instead of the default one.
     */
    private static final String MAVEN_WRAPPER_PROPERTIES_PATH =
            ".mvn/wrapper/maven-wrapper.properties";

    /**
     * Path where the maven-wrapper.jar will be saved to.
     */
    private static final String MAVEN_WRAPPER_JAR_PATH =
            ".mvn/wrapper/maven-wrapper.jar";

    /**
     * Name of the property which should be used to override the default download url for the wrapper.
     */
    private static final String PROPERTY_NAME_WRAPPER_URL = "wrapperUrl";

    public static void main(String args[]) {
        System.out.println("- Downloader started");
        File baseDirectory = new File(args[0]);
        System.out.println("- Using base directory: " + baseDirectory.getAbsolutePath());

        // If the maven-wrapper.properties exists, read it and check if it contains a custom
        // wrapperUrl parameter.
        File mavenWrapperPropertyFile = new File(baseDirectory, MAVEN_WRAPPER_PROPERTIES_PATH);
        String url = DEFAULT_DOWNLOAD_URL;
        if(mavenWrapperPropertyFile.exists()) {
            FileInputStream mavenWrapperPropertyFileInputStream = null;
            try {
                mavenWrapperPropertyFileInputStream = new FileInputStream(mavenWrapperPropertyFile);
                Properties mavenWrapperProperties = new Properties();
                mavenWrapperProperties.load(mavenWrapperPropertyFileInputStream);
                url = mavenWrapperProperties.getProperty(PROPERTY_NAME_WRAPPER_URL, url);
            } catch (IOException e) {
                System.out.println("- ERROR loading '" + MAVEN_WRAPPER_PROPERTIES_PATH + "'");
            } finally {
                try {
                    if(mavenWrapperPropertyFileInputStream != null) {
                        mavenWrapperPropertyFileInputStream.close();
                    }
                } catch (IOException e) {
                    // Ignore ...
                }
            }
        }
        System.out.println("- Downloading from: " + url);

        File outputFile = new File(baseDirectory.getAbsolutePath(), MAVEN_WRAPPER_JAR_PATH);
        if(!outputFile.getParentFile().exists()) {
            if(!outputFile.getParentFile().mkdirs()) {
                System.out.println(
                        "- ERROR creating output directory '" + outputFile.getParentFile().getAbsolutePath() + "'");
            }
        }
        System.out.println("- Downloading to: " + outputFile.getAbsolutePath());
        try {
            downloadFileFromURL(url, outputFile);
            System.out.println("Done");
            System.exit(0);
        } catch (Throwable e) {
            System.out.println("- Error downloading");
            e.printStackTrace();
            System.exit(1);
        }
    }

    private static void downloadFileFromURL(String urlString, File destination) throws Exception {
        if (System.getenv("MVNW_USERNAME") != null && System.getenv("MVNW_PASSWORD") != null) {
            String username = System.getenv("MVNW_USERNAME");
            char[] password = System.getenv("MVNW_PASSWORD").toCharArray();
            Authenticator.setDefault(new Authenticator() {
                @Override
                protected PasswordAuthentication getPasswordAuthentication() {
                    return new PasswordAuthentication(username, password);
                }
            });
        }
        URL website = new URL(urlString);
        ReadableByteChannel rbc;
        rbc = Channels.newChannel(website.openStream());
        FileOutputStream fos = new FileOutputStream(destination);
        fos.getChannel().transferFrom(rbc, 0, Long.MAX_VALUE);
        fos.close();
        rbc.close();
    }

}


File: /mvnw
#!/bin/sh
# ----------------------------------------------------------------------------
# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#    https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.
# ----------------------------------------------------------------------------

# ----------------------------------------------------------------------------
# Maven Start Up Batch script
#
# Required ENV vars:
# ------------------
#   JAVA_HOME - location of a JDK home dir
#
# Optional ENV vars
# -----------------
#   M2_HOME - location of maven2's installed home dir
#   MAVEN_OPTS - parameters passed to the Java VM when running Maven
#     e.g. to debug Maven itself, use
#       set MAVEN_OPTS=-Xdebug -Xrunjdwp:transport=dt_socket,server=y,suspend=y,address=8000
#   MAVEN_SKIP_RC - flag to disable loading of mavenrc files
# ----------------------------------------------------------------------------

if [ -z "$MAVEN_SKIP_RC" ] ; then

  if [ -f /etc/mavenrc ] ; then
    . /etc/mavenrc
  fi

  if [ -f "$HOME/.mavenrc" ] ; then
    . "$HOME/.mavenrc"
  fi

fi

# OS specific support.  $var _must_ be set to either true or false.
cygwin=false;
darwin=false;
mingw=false
case "`uname`" in
  CYGWIN*) cygwin=true ;;
  MINGW*) mingw=true;;
  Darwin*) darwin=true
    # Use /usr/libexec/java_home if available, otherwise fall back to /Library/Java/Home
    # See https://developer.apple.com/library/mac/qa/qa1170/_index.html
    if [ -z "$JAVA_HOME" ]; then
      if [ -x "/usr/libexec/java_home" ]; then
        export JAVA_HOME="`/usr/libexec/java_home`"
      else
        export JAVA_HOME="/Library/Java/Home"
      fi
    fi
    ;;
esac

if [ -z "$JAVA_HOME" ] ; then
  if [ -r /etc/gentoo-release ] ; then
    JAVA_HOME=`java-config --jre-home`
  fi
fi

if [ -z "$M2_HOME" ] ; then
  ## resolve links - $0 may be a link to maven's home
  PRG="$0"

  # need this for relative symlinks
  while [ -h "$PRG" ] ; do
    ls=`ls -ld "$PRG"`
    link=`expr "$ls" : '.*-> \(.*\)$'`
    if expr "$link" : '/.*' > /dev/null; then
      PRG="$link"
    else
      PRG="`dirname "$PRG"`/$link"
    fi
  done

  saveddir=`pwd`

  M2_HOME=`dirname "$PRG"`/..

  # make it fully qualified
  M2_HOME=`cd "$M2_HOME" && pwd`

  cd "$saveddir"
  # echo Using m2 at $M2_HOME
fi

# For Cygwin, ensure paths are in UNIX format before anything is touched
if $cygwin ; then
  [ -n "$M2_HOME" ] &&
    M2_HOME=`cygpath --unix "$M2_HOME"`
  [ -n "$JAVA_HOME" ] &&
    JAVA_HOME=`cygpath --unix "$JAVA_HOME"`
  [ -n "$CLASSPATH" ] &&
    CLASSPATH=`cygpath --path --unix "$CLASSPATH"`
fi

# For Mingw, ensure paths are in UNIX format before anything is touched
if $mingw ; then
  [ -n "$M2_HOME" ] &&
    M2_HOME="`(cd "$M2_HOME"; pwd)`"
  [ -n "$JAVA_HOME" ] &&
    JAVA_HOME="`(cd "$JAVA_HOME"; pwd)`"
fi

if [ -z "$JAVA_HOME" ]; then
  javaExecutable="`which javac`"
  if [ -n "$javaExecutable" ] && ! [ "`expr \"$javaExecutable\" : '\([^ ]*\)'`" = "no" ]; then
    # readlink(1) is not available as standard on Solaris 10.
    readLink=`which readlink`
    if [ ! `expr "$readLink" : '\([^ ]*\)'` = "no" ]; then
      if $darwin ; then
        javaHome="`dirname \"$javaExecutable\"`"
        javaExecutable="`cd \"$javaHome\" && pwd -P`/javac"
      else
        javaExecutable="`readlink -f \"$javaExecutable\"`"
      fi
      javaHome="`dirname \"$javaExecutable\"`"
      javaHome=`expr "$javaHome" : '\(.*\)/bin'`
      JAVA_HOME="$javaHome"
      export JAVA_HOME
    fi
  fi
fi

if [ -z "$JAVACMD" ] ; then
  if [ -n "$JAVA_HOME"  ] ; then
    if [ -x "$JAVA_HOME/jre/sh/java" ] ; then
      # IBM's JDK on AIX uses strange locations for the executables
      JAVACMD="$JAVA_HOME/jre/sh/java"
    else
      JAVACMD="$JAVA_HOME/bin/java"
    fi
  else
    JAVACMD="`which java`"
  fi
fi

if [ ! -x "$JAVACMD" ] ; then
  echo "Error: JAVA_HOME is not defined correctly." >&2
  echo "  We cannot execute $JAVACMD" >&2
  exit 1
fi

if [ -z "$JAVA_HOME" ] ; then
  echo "Warning: JAVA_HOME environment variable is not set."
fi

CLASSWORLDS_LAUNCHER=org.codehaus.plexus.classworlds.launcher.Launcher

# traverses directory structure from process work directory to filesystem root
# first directory with .mvn subdirectory is considered project base directory
find_maven_basedir() {

  if [ -z "$1" ]
  then
    echo "Path not specified to find_maven_basedir"
    return 1
  fi

  basedir="$1"
  wdir="$1"
  while [ "$wdir" != '/' ] ; do
    if [ -d "$wdir"/.mvn ] ; then
      basedir=$wdir
      break
    fi
    # workaround for JBEAP-8937 (on Solaris 10/Sparc)
    if [ -d "${wdir}" ]; then
      wdir=`cd "$wdir/.."; pwd`
    fi
    # end of workaround
  done
  echo "${basedir}"
}

# concatenates all lines of a file
concat_lines() {
  if [ -f "$1" ]; then
    echo "$(tr -s '\n' ' ' < "$1")"
  fi
}

BASE_DIR=`find_maven_basedir "$(pwd)"`
if [ -z "$BASE_DIR" ]; then
  exit 1;
fi

##########################################################################################
# Extension to allow automatically downloading the maven-wrapper.jar from Maven-central
# This allows using the maven wrapper in projects that prohibit checking in binary data.
##########################################################################################
if [ -r "$BASE_DIR/.mvn/wrapper/maven-wrapper.jar" ]; then
    if [ "$MVNW_VERBOSE" = true ]; then
      echo "Found .mvn/wrapper/maven-wrapper.jar"
    fi
else
    if [ "$MVNW_VERBOSE" = true ]; then
      echo "Couldn't find .mvn/wrapper/maven-wrapper.jar, downloading it ..."
    fi
    if [ -n "$MVNW_REPOURL" ]; then
      jarUrl="$MVNW_REPOURL/io/takari/maven-wrapper/0.5.6/maven-wrapper-0.5.6.jar"
    else
      jarUrl="https://repo.maven.apache.org/maven2/io/takari/maven-wrapper/0.5.6/maven-wrapper-0.5.6.jar"
    fi
    while IFS="=" read key value; do
      case "$key" in (wrapperUrl) jarUrl="$value"; break ;;
      esac
    done < "$BASE_DIR/.mvn/wrapper/maven-wrapper.properties"
    if [ "$MVNW_VERBOSE" = true ]; then
      echo "Downloading from: $jarUrl"
    fi
    wrapperJarPath="$BASE_DIR/.mvn/wrapper/maven-wrapper.jar"
    if $cygwin; then
      wrapperJarPath=`cygpath --path --windows "$wrapperJarPath"`
    fi

    if command -v wget > /dev/null; then
        if [ "$MVNW_VERBOSE" = true ]; then
          echo "Found wget ... using wget"
        fi
        if [ -z "$MVNW_USERNAME" ] || [ -z "$MVNW_PASSWORD" ]; then
            wget "$jarUrl" -O "$wrapperJarPath"
        else
            wget --http-user=$MVNW_USERNAME --http-password=$MVNW_PASSWORD "$jarUrl" -O "$wrapperJarPath"
        fi
    elif command -v curl > /dev/null; then
        if [ "$MVNW_VERBOSE" = true ]; then
          echo "Found curl ... using curl"
        fi
        if [ -z "$MVNW_USERNAME" ] || [ -z "$MVNW_PASSWORD" ]; then
            curl -o "$wrapperJarPath" "$jarUrl" -f
        else
            curl --user $MVNW_USERNAME:$MVNW_PASSWORD -o "$wrapperJarPath" "$jarUrl" -f
        fi

    else
        if [ "$MVNW_VERBOSE" = true ]; then
          echo "Falling back to using Java to download"
        fi
        javaClass="$BASE_DIR/.mvn/wrapper/MavenWrapperDownloader.java"
        # For Cygwin, switch paths to Windows format before running javac
        if $cygwin; then
          javaClass=`cygpath --path --windows "$javaClass"`
        fi
        if [ -e "$javaClass" ]; then
            if [ ! -e "$BASE_DIR/.mvn/wrapper/MavenWrapperDownloader.class" ]; then
                if [ "$MVNW_VERBOSE" = true ]; then
                  echo " - Compiling MavenWrapperDownloader.java ..."
                fi
                # Compiling the Java class
                ("$JAVA_HOME/bin/javac" "$javaClass")
            fi
            if [ -e "$BASE_DIR/.mvn/wrapper/MavenWrapperDownloader.class" ]; then
                # Running the downloader
                if [ "$MVNW_VERBOSE" = true ]; then
                  echo " - Running MavenWrapperDownloader.java ..."
                fi
                ("$JAVA_HOME/bin/java" -cp .mvn/wrapper MavenWrapperDownloader "$MAVEN_PROJECTBASEDIR")
            fi
        fi
    fi
fi
##########################################################################################
# End of extension
##########################################################################################

export MAVEN_PROJECTBASEDIR=${MAVEN_BASEDIR:-"$BASE_DIR"}
if [ "$MVNW_VERBOSE" = true ]; then
  echo $MAVEN_PROJECTBASEDIR
fi
MAVEN_OPTS="$(concat_lines "$MAVEN_PROJECTBASEDIR/.mvn/jvm.config") $MAVEN_OPTS"

# For Cygwin, switch paths to Windows format before running java
if $cygwin; then
  [ -n "$M2_HOME" ] &&
    M2_HOME=`cygpath --path --windows "$M2_HOME"`
  [ -n "$JAVA_HOME" ] &&
    JAVA_HOME=`cygpath --path --windows "$JAVA_HOME"`
  [ -n "$CLASSPATH" ] &&
    CLASSPATH=`cygpath --path --windows "$CLASSPATH"`
  [ -n "$MAVEN_PROJECTBASEDIR" ] &&
    MAVEN_PROJECTBASEDIR=`cygpath --path --windows "$MAVEN_PROJECTBASEDIR"`
fi

# Provide a "standardized" way to retrieve the CLI args that will
# work with both Windows and non-Windows executions.
MAVEN_CMD_LINE_ARGS="$MAVEN_CONFIG $@"
export MAVEN_CMD_LINE_ARGS

WRAPPER_LAUNCHER=org.apache.maven.wrapper.MavenWrapperMain

exec "$JAVACMD" \
  $MAVEN_OPTS \
  -classpath "$MAVEN_PROJECTBASEDIR/.mvn/wrapper/maven-wrapper.jar" \
  "-Dmaven.home=${M2_HOME}" "-Dmaven.multiModuleProjectDirectory=${MAVEN_PROJECTBASEDIR}" \
  ${WRAPPER_LAUNCHER} $MAVEN_CONFIG "$@"


File: /mvnw.cmd
@REM ----------------------------------------------------------------------------
@REM Licensed to the Apache Software Foundation (ASF) under one
@REM or more contributor license agreements.  See the NOTICE file
@REM distributed with this work for additional information
@REM regarding copyright ownership.  The ASF licenses this file
@REM to you under the Apache License, Version 2.0 (the
@REM "License"); you may not use this file except in compliance
@REM with the License.  You may obtain a copy of the License at
@REM
@REM    https://www.apache.org/licenses/LICENSE-2.0
@REM
@REM Unless required by applicable law or agreed to in writing,
@REM software distributed under the License is distributed on an
@REM "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
@REM KIND, either express or implied.  See the License for the
@REM specific language governing permissions and limitations
@REM under the License.
@REM ----------------------------------------------------------------------------

@REM ----------------------------------------------------------------------------
@REM Maven Start Up Batch script
@REM
@REM Required ENV vars:
@REM JAVA_HOME - location of a JDK home dir
@REM
@REM Optional ENV vars
@REM M2_HOME - location of maven2's installed home dir
@REM MAVEN_BATCH_ECHO - set to 'on' to enable the echoing of the batch commands
@REM MAVEN_BATCH_PAUSE - set to 'on' to wait for a keystroke before ending
@REM MAVEN_OPTS - parameters passed to the Java VM when running Maven
@REM     e.g. to debug Maven itself, use
@REM set MAVEN_OPTS=-Xdebug -Xrunjdwp:transport=dt_socket,server=y,suspend=y,address=8000
@REM MAVEN_SKIP_RC - flag to disable loading of mavenrc files
@REM ----------------------------------------------------------------------------

@REM Begin all REM lines with '@' in case MAVEN_BATCH_ECHO is 'on'
@echo off
@REM set title of command window
title %0
@REM enable echoing by setting MAVEN_BATCH_ECHO to 'on'
@if "%MAVEN_BATCH_ECHO%" == "on"  echo %MAVEN_BATCH_ECHO%

@REM set %HOME% to equivalent of $HOME
if "%HOME%" == "" (set "HOME=%HOMEDRIVE%%HOMEPATH%")

@REM Execute a user defined script before this one
if not "%MAVEN_SKIP_RC%" == "" goto skipRcPre
@REM check for pre script, once with legacy .bat ending and once with .cmd ending
if exist "%HOME%\mavenrc_pre.bat" call "%HOME%\mavenrc_pre.bat"
if exist "%HOME%\mavenrc_pre.cmd" call "%HOME%\mavenrc_pre.cmd"
:skipRcPre

@setlocal

set ERROR_CODE=0

@REM To isolate internal variables from possible post scripts, we use another setlocal
@setlocal

@REM ==== START VALIDATION ====
if not "%JAVA_HOME%" == "" goto OkJHome

echo.
echo Error: JAVA_HOME not found in your environment. >&2
echo Please set the JAVA_HOME variable in your environment to match the >&2
echo location of your Java installation. >&2
echo.
goto error

:OkJHome
if exist "%JAVA_HOME%\bin\java.exe" goto init

echo.
echo Error: JAVA_HOME is set to an invalid directory. >&2
echo JAVA_HOME = "%JAVA_HOME%" >&2
echo Please set the JAVA_HOME variable in your environment to match the >&2
echo location of your Java installation. >&2
echo.
goto error

@REM ==== END VALIDATION ====

:init

@REM Find the project base dir, i.e. the directory that contains the folder ".mvn".
@REM Fallback to current working directory if not found.

set MAVEN_PROJECTBASEDIR=%MAVEN_BASEDIR%
IF NOT "%MAVEN_PROJECTBASEDIR%"=="" goto endDetectBaseDir

set EXEC_DIR=%CD%
set WDIR=%EXEC_DIR%
:findBaseDir
IF EXIST "%WDIR%"\.mvn goto baseDirFound
cd ..
IF "%WDIR%"=="%CD%" goto baseDirNotFound
set WDIR=%CD%
goto findBaseDir

:baseDirFound
set MAVEN_PROJECTBASEDIR=%WDIR%
cd "%EXEC_DIR%"
goto endDetectBaseDir

:baseDirNotFound
set MAVEN_PROJECTBASEDIR=%EXEC_DIR%
cd "%EXEC_DIR%"

:endDetectBaseDir

IF NOT EXIST "%MAVEN_PROJECTBASEDIR%\.mvn\jvm.config" goto endReadAdditionalConfig

@setlocal EnableExtensions EnableDelayedExpansion
for /F "usebackq delims=" %%a in ("%MAVEN_PROJECTBASEDIR%\.mvn\jvm.config") do set JVM_CONFIG_MAVEN_PROPS=!JVM_CONFIG_MAVEN_PROPS! %%a
@endlocal & set JVM_CONFIG_MAVEN_PROPS=%JVM_CONFIG_MAVEN_PROPS%

:endReadAdditionalConfig

SET MAVEN_JAVA_EXE="%JAVA_HOME%\bin\java.exe"
set WRAPPER_JAR="%MAVEN_PROJECTBASEDIR%\.mvn\wrapper\maven-wrapper.jar"
set WRAPPER_LAUNCHER=org.apache.maven.wrapper.MavenWrapperMain

set DOWNLOAD_URL="https://repo.maven.apache.org/maven2/io/takari/maven-wrapper/0.5.6/maven-wrapper-0.5.6.jar"

FOR /F "tokens=1,2 delims==" %%A IN ("%MAVEN_PROJECTBASEDIR%\.mvn\wrapper\maven-wrapper.properties") DO (
    IF "%%A"=="wrapperUrl" SET DOWNLOAD_URL=%%B
)

@REM Extension to allow automatically downloading the maven-wrapper.jar from Maven-central
@REM This allows using the maven wrapper in projects that prohibit checking in binary data.
if exist %WRAPPER_JAR% (
    if "%MVNW_VERBOSE%" == "true" (
        echo Found %WRAPPER_JAR%
    )
) else (
    if not "%MVNW_REPOURL%" == "" (
        SET DOWNLOAD_URL="%MVNW_REPOURL%/io/takari/maven-wrapper/0.5.6/maven-wrapper-0.5.6.jar"
    )
    if "%MVNW_VERBOSE%" == "true" (
        echo Couldn't find %WRAPPER_JAR%, downloading it ...
        echo Downloading from: %DOWNLOAD_URL%
    )

    powershell -Command "&{"^
		"$webclient = new-object System.Net.WebClient;"^
		"if (-not ([string]::IsNullOrEmpty('%MVNW_USERNAME%') -and [string]::IsNullOrEmpty('%MVNW_PASSWORD%'))) {"^
		"$webclient.Credentials = new-object System.Net.NetworkCredential('%MVNW_USERNAME%', '%MVNW_PASSWORD%');"^
		"}"^
		"[Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12; $webclient.DownloadFile('%DOWNLOAD_URL%', '%WRAPPER_JAR%')"^
		"}"
    if "%MVNW_VERBOSE%" == "true" (
        echo Finished downloading %WRAPPER_JAR%
    )
)
@REM End of extension

@REM Provide a "standardized" way to retrieve the CLI args that will
@REM work with both Windows and non-Windows executions.
set MAVEN_CMD_LINE_ARGS=%*

%MAVEN_JAVA_EXE% %JVM_CONFIG_MAVEN_PROPS% %MAVEN_OPTS% %MAVEN_DEBUG_OPTS% -classpath %WRAPPER_JAR% "-Dmaven.multiModuleProjectDirectory=%MAVEN_PROJECTBASEDIR%" %WRAPPER_LAUNCHER% %MAVEN_CONFIG% %*
if ERRORLEVEL 1 goto error
goto end

:error
set ERROR_CODE=1

:end
@endlocal & set ERROR_CODE=%ERROR_CODE%

if not "%MAVEN_SKIP_RC%" == "" goto skipRcPost
@REM check for post script, once with legacy .bat ending and once with .cmd ending
if exist "%HOME%\mavenrc_post.bat" call "%HOME%\mavenrc_post.bat"
if exist "%HOME%\mavenrc_post.cmd" call "%HOME%\mavenrc_post.cmd"
:skipRcPost

@REM pause the script if MAVEN_BATCH_PAUSE is set to 'on'
if "%MAVEN_BATCH_PAUSE%" == "on" pause

if "%MAVEN_TERMINATE_CMD%" == "on" exit %ERROR_CODE%

exit /B %ERROR_CODE%


File: /pom.xml
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
	xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 https://maven.apache.org/xsd/maven-4.0.0.xsd">
	<modelVersion>4.0.0</modelVersion>
	<parent>
		<groupId>org.springframework.boot</groupId>
		<artifactId>spring-boot-starter-parent</artifactId>
		<version>2.3.1.RELEASE</version>
		<relativePath/> <!-- lookup parent from repository -->
	</parent>
	<groupId>br.com.trixsolucao</groupId>
	<artifactId>mkws</artifactId>
	<version>0.0.1-SNAPSHOT</version>
	<name>mkws</name>
	<description>WebService Consumes Mikrotik</description>

	<properties>
		<java.version>13</java.version>
	</properties>

	<dependencies>

		<dependency>
			<groupId>com.github.ulisesbocchio</groupId>
			<artifactId>jasypt-spring-boot-starter</artifactId>
			<version>2.0.0</version>
		</dependency>

		<!-- https://mvnrepository.com/artifact/me.legrange/mikrotik -->
		<dependency>
			<groupId>me.legrange</groupId>
			<artifactId>mikrotik</artifactId>
			<version>3.0.7</version>
		</dependency>


		<dependency>
			<groupId>org.projectlombok</groupId>
			<artifactId>lombok</artifactId>
			<version>1.18.12</version>
			<scope>provided</scope>
		</dependency>


		<dependency>
			<groupId>org.springframework.boot</groupId>
			<artifactId>spring-boot-starter-web</artifactId>
		</dependency>

		<dependency>
			<groupId>org.springframework.boot</groupId>
			<artifactId>spring-boot-starter-test</artifactId>
			<scope>test</scope>
			<exclusions>
				<exclusion>
					<groupId>org.junit.vintage</groupId>
					<artifactId>junit-vintage-engine</artifactId>
				</exclusion>
			</exclusions>
		</dependency>
	</dependencies>

	<build>
		<plugins>
			<plugin>
				<groupId>org.springframework.boot</groupId>
				<artifactId>spring-boot-maven-plugin</artifactId>

			</plugin>
		</plugins>
	</build>

</project>


File: /Procfile
web: java -Dserver.port=$PORT $JAVA_OPTS -jar target/mkws-0.0.1-SNAPSHOT.jar

File: /src\main\java\br\com\trixsolucao\mkws\controller\HotSpotController.java
package br.com.trixsolucao.mkws.controller;

import br.com.trixsolucao.mkws.mkapi.Mikrotik;
import br.com.trixsolucao.mkws.model.*;
import br.com.trixsolucao.mkws.model.mapping.MapToObject;
import com.fasterxml.jackson.core.JsonProcessingException;
import com.fasterxml.jackson.databind.ObjectMapper;
import me.legrange.mikrotik.MikrotikApiException;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.Comparator;
import java.util.List;
import java.util.Map;
import java.util.Optional;
import java.util.stream.Collectors;

@RestController
@RequestMapping({"/hotspot"})
public class HotSpotController {


    /* Sessão de métodos de usuários */

    @GetMapping("/users")
    public ResponseEntity listar(@RequestHeader Map<String, String> connectionHeader) {
        try {

            Mikrotik.getInstance().onConectar(connectionHeader.get("hostmk"), connectionHeader.get("portmk"), connectionHeader.get("usuariomk"), connectionHeader.get("senhamk"));

            List<Map<String, String>> hotSpotUsersMap = Mikrotik.getInstance().onEnviarComando("/ip/hotspot/user/print");
            var hotSpotUsers = MapToObject.mapToObject(hotSpotUsersMap, HotspotUser.class);

            List<Map<String, String>> hotspotActivesMap = Mikrotik.getInstance().onEnviarComando("/ip/hotspot/active/print");
            var hotspotActiveUsers = MapToObject.mapToObject(hotspotActivesMap, HotspotActiveUser.class);

            //Definindo online/offline conforme a lista de ativos buscada anteriormente
            // incluido sorted ordenando por nome de usuário
            List<HotspotUser> hotSpotSorted = hotSpotUsers.stream().peek(u ->
                    u.setOnline(hotspotActiveUsers.contains(new HotspotActiveUser(u.getName())))
            ).sorted(Comparator.comparing(HotspotUser::getName)).collect(Collectors.toList());


            return ResponseEntity.ok().body(hotSpotSorted);

        } catch (MikrotikApiException e) {
            return ResponseEntity.status(HttpStatus.BAD_REQUEST).body(e.getMessage());
        } catch (Exception ex) {
            return ResponseEntity.status(HttpStatus.INTERNAL_SERVER_ERROR).body(ex.getMessage());
        }

    }

    @PutMapping(value = "/users/{id}")
    public ResponseEntity editar(@PathVariable("id") String id, @RequestHeader Map<String, String> connectionHeader, @RequestBody HotspotUser hotSpotUser) {
        try {

            Mikrotik.getInstance().onConectar(connectionHeader.get("hostmk"), connectionHeader.get("portmk"), connectionHeader.get("usuariomk"), connectionHeader.get("senhamk"));
            hotSpotUser.setId(null);
            String valores = MapToObject.getStringFromObject(hotSpotUser);
            Optional<Object> optionalID = Optional.ofNullable(id);

            if (optionalID.isPresent()) {
                Mikrotik.getInstance().onEnviarComando("/ip/hotspot/user/set numbers=" + optionalID.get() + valores);
                return ResponseEntity.ok().body("HotSpot editado com sucesso");
            } else {
                return ResponseEntity.badRequest().body("Id não encontrado!");
            }

        } catch (MikrotikApiException e) {
            return ResponseEntity.status(HttpStatus.BAD_REQUEST).body(e.getMessage());
        } catch (Exception ex) {
            return ResponseEntity.status(HttpStatus.INTERNAL_SERVER_ERROR).body(ex.getMessage());
        }
    }

    @PostMapping("/users")
    public ResponseEntity adicionar(@RequestBody HotspotUser hotspotUser, @RequestHeader Map<String, String> connectionHeader) {
        try {

            Mikrotik.getInstance().onConectar(connectionHeader.get("hostmk"), connectionHeader.get("portmk"), connectionHeader.get("usuariomk"), connectionHeader.get("senhamk"));

            String valores = MapToObject.getStringFromObject(hotspotUser);


            Mikrotik.getInstance().onEnviarComando("/ip/hotspot/user/add " + valores);
            return ResponseEntity.ok().body("HotSpot cadastrado com sucesso");

        } catch (MikrotikApiException e) {
            return ResponseEntity.status(HttpStatus.BAD_REQUEST).body(e.getMessage());
        } catch (Exception ex) {
            return ResponseEntity.status(HttpStatus.INTERNAL_SERVER_ERROR).body(ex.getMessage());

        }
    }

    @DeleteMapping("/users/{name}")
    public ResponseEntity remover(@PathVariable("name") String name, @RequestHeader Map<String, String> connectionHeader) {
        try {

            Mikrotik.getInstance().onConectar(connectionHeader.get("hostmk"), connectionHeader.get("portmk"), connectionHeader.get("usuariomk"), connectionHeader.get("senhamk"));

            Optional<Object> optionalName = Optional.ofNullable(name);
            if (optionalName.isPresent()) {
                List<Map<String, String>> user = Mikrotik.getInstance().onEnviarComando("/ip/hotspot/user/print where name=" + optionalName.get());
                if (!user.isEmpty()) {
                    Mikrotik.getInstance().onEnviarComando("/ip/hotspot/user/remove .id=" + user.get(0).get(".id"));
                    return ResponseEntity.ok().body("Hotspot removido com sucesso");
                } else {
                    return ResponseEntity.badRequest().body("Nome não encontrado no Mikrotik");
                }

            }

            return ResponseEntity.badRequest().body("Requisição inválida, nome não encontrado");

        } catch (MikrotikApiException e) {
            return ResponseEntity.status(HttpStatus.BAD_REQUEST).body(e.getMessage());
        } catch (Exception ex) {
            return ResponseEntity.status(HttpStatus.INTERNAL_SERVER_ERROR).body(ex.getMessage());
        }
    }



    /* Sessão de métodos de planos de usuário */
//
//    @GetMapping("/plans")
//    public ResponseEntity listarPlanos(@RequestHeader Map<String, String> connectionHeader) {
//        try {
//
//
//            Mikrotik.getInstance().onConectar(connectionHeader.get("hostmk"), connectionHeader.get("portmk"), connectionHeader.get("usuariomk"), connectionHeader.get("senhamk"));
//
//            List<Map<String, String>> pppUsersMap = Mikrotik.getInstance().onEnviarComando("/ip/hotspot/profile/print");
//            return ResponseEntity.ok().body(MapToObject.mapToObject(pppUsersMap, PPPProfiles.class));
//
//        } catch (MikrotikApiException e) {
//            return ResponseEntity.status(HttpStatus.BAD_REQUEST).body(e.getMessage());
//        } catch (Exception ex) {
//            return ResponseEntity.status(HttpStatus.INTERNAL_SERVER_ERROR).body(ex.getMessage());
//        }
//
//    }
//
//    @PutMapping(value = "/plans/{id}")
//    public ResponseEntity editarPlanos(@PathVariable("id") String id, @RequestHeader Map<String, String> connectionHeader, @RequestBody PPPUsers pppoeUser) {
//        try {
//
//            Mikrotik.getInstance().onConectar(connectionHeader.get("hostmk"), connectionHeader.get("portmk"), connectionHeader.get("usuariomk"), connectionHeader.get("senhamk"));
//            String valores = MapToObject.getStringFromObject(pppoeUser);
//            Optional<Object> optionalID = Optional.ofNullable(id);
//
//            if (optionalID.isPresent()) {
//                Mikrotik.getInstance().onEnviarComando("/ppp/profile/set " + valores);
//                return ResponseEntity.ok().body("Plano editado com sucesso");
//            } else {
//                return ResponseEntity.badRequest().body("Id não encontrado!");
//            }
//
//        } catch (MikrotikApiException e) {
//            return ResponseEntity.status(HttpStatus.BAD_REQUEST).body(e.getMessage());
//        } catch (Exception ex) {
//            return ResponseEntity.status(HttpStatus.INTERNAL_SERVER_ERROR).body(ex.getMessage());
//        }
//    }
//
//    @PostMapping("/plans")
//    public ResponseEntity adicionarPlano(@RequestBody PPPUsers pppoeUser, @RequestHeader Map<String, String> connectionHeader) {
//        try {
//
//
//            Mikrotik.getInstance().onConectar(connectionHeader.get("hostmk"), connectionHeader.get("portmk"), connectionHeader.get("usuariomk"), connectionHeader.get("senhamk"));
//
//            String valores = MapToObject.getStringFromObject(pppoeUser);
//
//            Mikrotik.getInstance().onEnviarComando("/ppp/profile/add " + valores);
//
//
//            return ResponseEntity.ok().body("Plano cadastrado com sucesso");
//
//        } catch (MikrotikApiException e) {
//            return ResponseEntity.status(HttpStatus.BAD_REQUEST).body(e.getMessage());
//        } catch (Exception ex) {
//            return ResponseEntity.status(HttpStatus.INTERNAL_SERVER_ERROR).body(ex.getMessage());
//
//        }
//    }
//
//
//    @DeleteMapping(path = {"/plans/{id}"})
//    public ResponseEntity removerPlano(@PathVariable("id") String id, @RequestHeader Map<String, String> connectionHeader) {
//        try {
//
//
//            Mikrotik.getInstance().onConectar(connectionHeader.get("hostmk"), connectionHeader.get("portmk"), connectionHeader.get("usuariomk"), connectionHeader.get("senhamk"));
//
//            Optional<Object> optionalId = Optional.ofNullable(id);
//            if (optionalId.isPresent()) {
//
//                Mikrotik.getInstance().onEnviarComando("/ppp/profile/remove .id=" + optionalId.get());
//                return ResponseEntity.ok().body("Plano removido com sucesso");
//
//
//            }
//
//            return ResponseEntity.badRequest().body("Requisição inválida, plano não encontrado");
//
//        } catch (MikrotikApiException e) {
//            return ResponseEntity.status(HttpStatus.BAD_REQUEST).body(e.getMessage());
//        } catch (Exception ex) {
//            return ResponseEntity.status(HttpStatus.INTERNAL_SERVER_ERROR).body(ex.getMessage());
//        }
//    }


}


File: /src\main\java\br\com\trixsolucao\mkws\controller\OpenConnection.java
package br.com.trixsolucao.mkws.controller;


import br.com.trixsolucao.mkws.exception.HeaderException;
import br.com.trixsolucao.mkws.mkapi.Mikrotik;
import br.com.trixsolucao.mkws.model.FirewallNat;
import br.com.trixsolucao.mkws.model.mapping.MapToObject;
import com.fasterxml.jackson.databind.ObjectMapper;
import me.legrange.mikrotik.MikrotikApiException;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.RequestHeader;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import java.util.List;
import java.util.Map;
import java.util.function.Function;


@RestController
@RequestMapping({"/open"})
public class OpenConnection {


    public ResponseEntity testarConexao(@RequestHeader Map<String, String> connectionHeader) {
        try {
            Mikrotik.getInstance().onConectar(connectionHeader.get("hostmk"), connectionHeader.get("portmk"), connectionHeader.get("usuariomk"), connectionHeader.get("senhamk"));
            return ResponseEntity.ok().build();

        }  catch (MikrotikApiException ex) {
            return ResponseEntity.status(HttpStatus.GATEWAY_TIMEOUT).build();
        } catch (Exception ex) {
            return ResponseEntity.status(HttpStatus.INTERNAL_SERVER_ERROR).build();
        }

    }

    public static void main(String[] args) {

    }
    /*
    *  Método criado para uso pontual
    *  Criado para atualizar todas regras setando o in-interface
    * */
    public static void changeFirewallNatRules(String host, String port, String user, String password, String pppoeIn) {
        try {
            Mikrotik.getInstance().onConectar(host, port, user, password);
            List<Map<String, String>> maps = Mikrotik.getInstance().onEnviarComando("/ip/firewall/nat/print");

            Function<FirewallNat, FirewallNat> functionFirewallNat = item -> {
                item.setInInterface(pppoeIn);
                item.setIdAux(item.getId());
                item.setId(null);
                return item;
            };

            MapToObject.mapToObject(maps, FirewallNat.class).stream().filter(item -> item.getAction().equals("dst-nat"))
                    .map(functionFirewallNat).forEach(
                    item ->
                    {
                        String itemString = MapToObject.getStringFromObject(item);
                        try {
                            Mikrotik.getInstance().onEnviarComando("/ip/firewall/nat/set numbers=" + item.getIdAux() + itemString);
                        } catch (MikrotikApiException e) {
                            e.printStackTrace();
                        }
                    }
            );
        } catch (MikrotikApiException e) {
            e.printStackTrace();
        }
    }
}


File: /src\main\java\br\com\trixsolucao\mkws\controller\PPPoeController.java
package br.com.trixsolucao.mkws.controller;

import br.com.trixsolucao.mkws.mkapi.Mikrotik;
import br.com.trixsolucao.mkws.model.PPPActiveUser;
import br.com.trixsolucao.mkws.model.PPPProfiles;
import br.com.trixsolucao.mkws.model.PPPUsers;
import br.com.trixsolucao.mkws.model.mapping.MapToObject;
import me.legrange.mikrotik.MikrotikApiException;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.Comparator;
import java.util.List;
import java.util.Map;
import java.util.Optional;
import java.util.stream.Collectors;


@RestController
@RequestMapping({"/pppoe"})
public class PPPoeController {



    /* Sessão de métodos de usuários */

    @GetMapping("/users")
    public ResponseEntity listar(@RequestHeader Map<String, String> connectionHeader) {
        try {
            Mikrotik.getInstance().onConectar(connectionHeader.get("hostmk"), connectionHeader.get("portmk"), connectionHeader.get("usuariomk"), connectionHeader.get("senhamk"));

            List<Map<String, String>> pppUsersMap = Mikrotik.getInstance().onEnviarComando("/ppp/secret/print");
            var pppUsers = MapToObject.mapToObject(pppUsersMap, PPPUsers.class);

            List<Map<String, String>> pppActivesMap = Mikrotik.getInstance().onEnviarComando("/ppp/active/print");
            var pppActiveUsers = MapToObject.mapToObject(pppActivesMap, PPPActiveUser.class);

            //Definindo online/offline conforme a lista de ativos buscada anteriormente
            // incluido sorted ordenando por nome de usuário
            List<PPPUsers> pppSorted = pppUsers.stream().peek(u ->
                    u.setOnline(pppActiveUsers.contains(new PPPActiveUser(u.getUser())))
            ).sorted(Comparator.comparing(PPPUsers::getUser)).collect(Collectors.toList());


            return ResponseEntity.ok().body(pppSorted);

        } catch (MikrotikApiException e) {
            return ResponseEntity.status(HttpStatus.BAD_REQUEST).body(e.getMessage());
        } catch (Exception ex) {
            return ResponseEntity.status(HttpStatus.INTERNAL_SERVER_ERROR).body(ex.getMessage());
        }

    }

    @PutMapping(value = "/users/{id}")
    public ResponseEntity editar(@PathVariable("id") String id, @RequestHeader Map<String, String> connectionHeader, @RequestBody PPPUsers pppoeUser) {
        try {

            Mikrotik.getInstance().onConectar(connectionHeader.get("hostmk"), connectionHeader.get("portmk"), connectionHeader.get("usuariomk"), connectionHeader.get("senhamk"));
            pppoeUser.setId(null);
            String valores = MapToObject.getStringFromObject(pppoeUser);
            Optional<Object> optionalID = Optional.ofNullable(id);

            if (optionalID.isPresent()) {
                Mikrotik.getInstance().onEnviarComando("/ppp/secret/set numbers=" + optionalID.get() + valores);
                return ResponseEntity.ok().body("PPPoe editado com sucesso");
            } else {
                return ResponseEntity.badRequest().body("Id não encontrado!");
            }

        } catch (MikrotikApiException e) {
            return ResponseEntity.status(HttpStatus.BAD_REQUEST).body(e.getMessage());
        } catch (Exception ex) {
            return ResponseEntity.status(HttpStatus.INTERNAL_SERVER_ERROR).body(ex.getMessage());
        }
    }

    @PostMapping("/users")
    public ResponseEntity adicionar(@RequestBody PPPUsers pppoeUser, @RequestHeader Map<String, String> connectionHeader) {
        try {

            Mikrotik.getInstance().onConectar(connectionHeader.get("hostmk"), connectionHeader.get("portmk"), connectionHeader.get("usuariomk"), connectionHeader.get("senhamk"));

            String valores = MapToObject.getStringFromObject(pppoeUser);

            System.out.println("ADD >>>> " + valores);

            Mikrotik.getInstance().onEnviarComando("/ppp/secret/add " + valores);

            return ResponseEntity.ok().body("PPPoe cadastrado com sucesso");

        } catch (MikrotikApiException e) {
            return ResponseEntity.status(HttpStatus.BAD_REQUEST).body(e.getMessage());
        } catch (Exception ex) {
            return ResponseEntity.status(HttpStatus.INTERNAL_SERVER_ERROR).body(ex.getMessage());

        }
    }

    @DeleteMapping("/users/{name}")
    public ResponseEntity remover(@PathVariable("name") String name, @RequestHeader Map<String, String> connectionHeader) {
        try {

            Mikrotik.getInstance().onConectar(connectionHeader.get("hostmk"), connectionHeader.get("portmk"), connectionHeader.get("usuariomk"), connectionHeader.get("senhamk"));

            Optional<Object> optionalName = Optional.ofNullable(name);
            if (optionalName.isPresent()) {
                List<Map<String, String>> user = Mikrotik.getInstance().onEnviarComando("/ppp/secret/print where name=" + optionalName.get());
                if (!user.isEmpty()) {
                    Mikrotik.getInstance().onEnviarComando("/ppp/secret/remove .id=" + user.get(0).get(".id"));
                    return ResponseEntity.ok().body("PPPoe removido com sucesso");
                } else {
                    return ResponseEntity.badRequest().body("Nome não encontrado no Mikrotik");
                }

            }

            return ResponseEntity.badRequest().body("Requisição inválida, nome não encontrado");

        } catch (MikrotikApiException e) {
            return ResponseEntity.status(HttpStatus.BAD_REQUEST).body(e.getMessage());
        } catch (Exception ex) {
            return ResponseEntity.status(HttpStatus.INTERNAL_SERVER_ERROR).body(ex.getMessage());
        }
    }


    /* Sessão de métodos de usuários ativos */

    @GetMapping("/actives")
    public ResponseEntity listarAtivos(@RequestHeader Map<String, String> connectionHeader) {
        try {

            System.out.println("Request -->>> " + connectionHeader);
            Mikrotik.getInstance().onConectar(connectionHeader.get("hostmk"), connectionHeader.get("portmk"), connectionHeader.get("usuariomk"), connectionHeader.get("senhamk"));

            List<Map<String, String>> pppActivesMap = Mikrotik.getInstance().onEnviarComando("/ppp/active/print");
            return ResponseEntity.ok().body(MapToObject.mapToObject(pppActivesMap, PPPActiveUser.class));

        } catch (MikrotikApiException e) {
            return ResponseEntity.status(HttpStatus.BAD_REQUEST).body(e.getMessage());
        } catch (Exception ex) {
            return ResponseEntity.status(HttpStatus.INTERNAL_SERVER_ERROR).body(ex.getMessage());
        }

    }


    @DeleteMapping(path = {"/actives/{name}"})
    public ResponseEntity removerActive(@PathVariable("name") String name, @RequestHeader Map<String, String> connectionHeader) {

        try {

            Mikrotik.getInstance().onConectar(connectionHeader.get("hostmk"), connectionHeader.get("portmk"), connectionHeader.get("usuariomk"), connectionHeader.get("senhamk"));

            Optional<Object> optionalName = Optional.ofNullable(name);
            if (optionalName.isPresent()) {
                List<Map<String, String>> user = Mikrotik.getInstance().onEnviarComando("/ppp/active/print where name=" + optionalName.get());
                if (!user.isEmpty()) {
                    Mikrotik.getInstance().onEnviarComando("/ppp/active/remove .id=" + user.get(0).get(".id"));
                    return ResponseEntity.ok().body("Usuário desconectado com sucesso");
                } else {
                    return ResponseEntity.badRequest().body("Usuário não logado");
                }

            }

            return ResponseEntity.badRequest().body("Requisição inválida, nome não encontrado");

        } catch (MikrotikApiException e) {
            return ResponseEntity.status(HttpStatus.BAD_REQUEST).body(e.getMessage());
        } catch (Exception ex) {
            return ResponseEntity.status(HttpStatus.INTERNAL_SERVER_ERROR).body(ex.getMessage());
        }
    }



    /* Sessão de métodos de planos de usuário */

    @GetMapping("/plans")
    public ResponseEntity listarPlanos(@RequestHeader Map<String, String> connectionHeader) {
        try {

            Mikrotik.getInstance().onConectar(connectionHeader.get("hostmk"), connectionHeader.get("portmk"), connectionHeader.get("usuariomk"), connectionHeader.get("senhamk"));

            List<Map<String, String>> pppUsersMap = Mikrotik.getInstance().onEnviarComando("/ppp/profile/print");
            return ResponseEntity.ok().body(MapToObject.mapToObject(pppUsersMap, PPPProfiles.class));

        } catch (MikrotikApiException e) {
            return ResponseEntity.status(HttpStatus.BAD_REQUEST).body(e.getMessage());
        } catch (Exception ex) {
            return ResponseEntity.status(HttpStatus.INTERNAL_SERVER_ERROR).body(ex.getMessage());
        }

    }

    @PutMapping(value = "/plans/{id}")
    public ResponseEntity editarPlanos(@PathVariable("id") String id, @RequestHeader Map<String, String> connectionHeader, @RequestBody PPPProfiles pppoeProfile) {
        try {

            Mikrotik.getInstance().onConectar(connectionHeader.get("hostmk"), connectionHeader.get("portmk"), connectionHeader.get("usuariomk"), connectionHeader.get("senhamk"));
            pppoeProfile.setId(null);
            String valores = MapToObject.getStringFromObject(pppoeProfile);
            Optional<Object> optionalID = Optional.ofNullable(id);

            if (optionalID.isPresent()) {
                Mikrotik.getInstance().onEnviarComando("/ppp/profile/set numbers=" + optionalID.get() + valores);
                return ResponseEntity.ok().body("Plano editado com sucesso");
            } else {
                return ResponseEntity.badRequest().body("Id não encontrado!");
            }

        } catch (MikrotikApiException e) {
            return ResponseEntity.status(HttpStatus.BAD_REQUEST).body(e.getMessage());
        } catch (Exception ex) {
            return ResponseEntity.status(HttpStatus.INTERNAL_SERVER_ERROR).body(ex.getMessage());
        }
    }

    @PostMapping("/plans")
    public ResponseEntity adicionarPlano(@RequestBody PPPUsers pppoeUser, @RequestHeader Map<String, String> connectionHeader) {
        try {

            Mikrotik.getInstance().onConectar(connectionHeader.get("hostmk"), connectionHeader.get("portmk"), connectionHeader.get("usuariomk"), connectionHeader.get("senhamk"));

            String valores = MapToObject.getStringFromObject(pppoeUser);

            Mikrotik.getInstance().onEnviarComando("/ppp/profile/add " + valores);


            return ResponseEntity.ok().body("Plano cadastrado com sucesso");

        } catch (MikrotikApiException e) {
            return ResponseEntity.status(HttpStatus.BAD_REQUEST).body(e.getMessage());
        } catch (Exception ex) {
            return ResponseEntity.status(HttpStatus.INTERNAL_SERVER_ERROR).body(ex.getMessage());

        }
    }


    @DeleteMapping(path = {"/plans/{id}"})
    public ResponseEntity removerPlano(@PathVariable("id") String id, @RequestHeader Map<String, String> connectionHeader) {
        try {

            Mikrotik.getInstance().onConectar(connectionHeader.get("hostmk"), connectionHeader.get("portmk"), connectionHeader.get("usuariomk"), connectionHeader.get("senhamk"));

            Optional<Object> optionalId = Optional.ofNullable(id);
            if (optionalId.isPresent()) {

                Mikrotik.getInstance().onEnviarComando("/ppp/profile/remove .id=" + optionalId.get());
                return ResponseEntity.ok().body("Plano removido com sucesso");
            }

            return ResponseEntity.badRequest().body("Requisição inválida, plano não encontrado");

        } catch (MikrotikApiException e) {
            return ResponseEntity.status(HttpStatus.BAD_REQUEST).body(e.getMessage());
        } catch (Exception ex) {
            return ResponseEntity.status(HttpStatus.INTERNAL_SERVER_ERROR).body(ex.getMessage());
        }
    }


}


File: /src\main\java\br\com\trixsolucao\mkws\controller\ResourcesController.java
package br.com.trixsolucao.mkws.controller;

import br.com.trixsolucao.mkws.mkapi.Mikrotik;
import br.com.trixsolucao.mkws.model.Resources;
import br.com.trixsolucao.mkws.model.mapping.MapToObject;
import me.legrange.mikrotik.MikrotikApiException;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestHeader;
import org.springframework.web.bind.annotation.RestController;

import java.util.List;
import java.util.Map;

@RestController
public class ResourcesController {

    @GetMapping("/resources")
    public ResponseEntity listar(@RequestHeader Map<String, String> connectionHeader) {
        try {

            Mikrotik.getInstance().onConectar(connectionHeader.get("hostmk"), connectionHeader.get("portmk"), connectionHeader.get("usuariomk"), connectionHeader.get("senhamk"));

            List<Map<String, String>> resourcesMap = Mikrotik.getInstance().onEnviarComando("/system/resource/print");
            return ResponseEntity.ok().body(MapToObject.mapToObject(resourcesMap, Resources.class));

        } catch (MikrotikApiException e) {
            return ResponseEntity.status(HttpStatus.BAD_REQUEST).body(e.getMessage());
        } catch (Exception ex) {
            return ResponseEntity.status(HttpStatus.INTERNAL_SERVER_ERROR).body(ex.getMessage());
        }

    }


}


File: /src\main\java\br\com\trixsolucao\mkws\controller\response\DefaultResponseEnum.java
package br.com.trixsolucao.mkws.controller.response;

public enum DefaultResponseEnum {
    OK(00, "Requisição ok."),
    ERROR(99, "Ocorreu um erro inesperado.");

    public int returnCode;
    public String returnMessage;

    DefaultResponseEnum(int returnCode, String returnMessage) {
        this.returnCode = returnCode;
        this.returnMessage = returnMessage;
    }

    public int getReturnCode() {
        return this.returnCode;
    }

    public String getReturnMessage() {
        return this.returnMessage;
    }
}


File: /src\main\java\br\com\trixsolucao\mkws\controller\response\GenericResponse.java
/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package br.com.trixsolucao.mkws.controller.response;

import com.fasterxml.jackson.annotation.JsonTypeInfo;

public class GenericResponse<T> extends ModelResponse {

    @JsonTypeInfo(use = JsonTypeInfo.Id.NONE, include = JsonTypeInfo.As.WRAPPER_OBJECT, property = "@class")
    private T responseData;

    public GenericResponse() {
        super(0, "");
    }

    public GenericResponse(int returnCode, String returnMessage, T responseData) {
        super(returnCode, returnMessage);
        this.responseData = responseData;
    }

    public T getResponseData() {
        return responseData;
    }

    public void setResponseData(T responseData) {
        this.responseData = responseData;
    }

}



File: /src\main\java\br\com\trixsolucao\mkws\controller\response\ModelResponse.java
package br.com.trixsolucao.mkws.controller.response;

public class ModelResponse {

    protected int returnCode;
    protected String returnMessage;

    protected ModelResponse(int returnCode, String returnMessage) {
        this.returnCode = returnCode;
        this.returnMessage = returnMessage;
    }

    public int getReturnCode() {
        return this.returnCode;
    }

    public void setReturnCode(int returnCode) {
        this.returnCode = returnCode;
    }

    public String getReturnMessage() {
        return this.returnMessage;
    }

    public void setReturnMessage(String returnMessage) {
        this.returnMessage = returnMessage;
    }
}




File: /src\main\java\br\com\trixsolucao\mkws\exception\HeaderException.java
package br.com.trixsolucao.mkws.exception;

public class HeaderException extends Exception {

    public HeaderException(String message) {
        super(message);
    }
}


File: /src\main\java\br\com\trixsolucao\mkws\filter\RequestFilter.java
package br.com.trixsolucao.mkws.filter;

import com.fasterxml.jackson.databind.ObjectMapper;
import org.springframework.http.HttpStatus;
import org.springframework.stereotype.Component;

import javax.servlet.*;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.io.IOException;
import java.util.HashMap;
import java.util.Map;
import java.util.Optional;

@Component
public class RequestFilter implements Filter {
    @Override
    public void doFilter(ServletRequest request, ServletResponse response, FilterChain chain) throws IOException, ServletException {
        HttpServletRequest  httpRequest = (HttpServletRequest)request;
        Map<String,String> erros = new HashMap<>();

        Optional.ofNullable(httpRequest.getHeader("hostmk")).ifPresentOrElse((value) ->{}, () -> {erros.put("hostmk", "NULL not allowed");});
        Optional.ofNullable(httpRequest.getHeader("portmk")).ifPresentOrElse((value) ->{}, () -> {erros.put("portmk", "NULL not allowed");});
        Optional.ofNullable(httpRequest.getHeader("usuariomk")).ifPresentOrElse((value) ->{}, () -> {erros.put("usuariomk", "NULL not allowed");});
        Optional.ofNullable(httpRequest.getHeader("senhamk")).ifPresentOrElse((value) ->{}, () -> {erros.put("senhamk", "NULL not allowed");});

        if(!erros.isEmpty()){
            HttpServletResponse  myResponse= (HttpServletResponse) response;
            myResponse.setStatus(HttpStatus.BAD_REQUEST.value());
            myResponse.getOutputStream().flush();
            String errosJson = new ObjectMapper().writeValueAsString(erros);
            myResponse.getOutputStream().println(errosJson);
        } else {
            chain.doFilter(request, response);
        }

    }

    /*
    *
    *   List<String> mensagemDeErro = new ArrayList<>();
        Optional.ofNullable(connectionHeader.get("hostmk")).ifPresentOrElse((value) ->{}, () -> {
            mensagemDeErro.add("attribute hostmk not accept null");
        });
        Optional.ofNullable(connectionHeader.get("portmk")).ifPresentOrElse((value) ->{}, () -> {mensagemDeErro.add("attribute portmk not accept null");});
        Optional.ofNullable(connectionHeader.get("usuariomk")).ifPresentOrElse((value) ->{}, () -> {mensagemDeErro.add("attribute usuariomk not accept null");});
        Optional.ofNullable(connectionHeader.get("senhamk")).ifPresentOrElse((value) ->{}, () -> {mensagemDeErro.add("attribute senhamk not accept null");});

        if(!mensagemDeErro.isEmpty()){
            throw new HeaderException(mensagemDeErro.toString());
        }
    * */
}


File: /src\main\java\br\com\trixsolucao\mkws\mkapi\ConnectionBean.java
/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package br.com.trixsolucao.mkws.mkapi;

import me.legrange.mikrotik.ApiConnection;

/**
 *
 * @author Renan
 */
public class ConnectionBean {

    private String usuario;
    private String senha;
    private String porta;
    private String host;

    private Object objetoAcao;

    public ConnectionBean() {
        porta = ApiConnection.DEFAULT_PORT + "";
    }

    public String getUsuario() {
        return usuario;
    }

    public void setUsuario(String usuario) {
        this.usuario = usuario;
    }

    public String getSenha() {
        return senha;
    }

    public void setSenha(String senha) {
        this.senha = senha;
    }

    public String getPorta() {
        return porta;
    }

    public void setPorta(String porta) {
        this.porta = porta;
    }

    public String getHost() {
        return host;
    }

    public void setHost(String host) {
        this.host = host;
    }

    public Object getObjetoAcao() {
        return objetoAcao;
    }

    public void setObjetoAcao(Object objetoAcao) {
        this.objetoAcao = objetoAcao;
    }

}


File: /src\main\java\br\com\trixsolucao\mkws\mkapi\Mikrotik.java
/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package br.com.trixsolucao.mkws.mkapi;


import me.legrange.mikrotik.ApiConnection;
import me.legrange.mikrotik.MikrotikApiException;
import me.legrange.mikrotik.ResultListener;

import java.util.List;
import java.util.Map;
import javax.net.SocketFactory;

/**
 *
 * @author Renan
 */
public class Mikrotik {

    private static Mikrotik instance;

    private ApiConnection conexao;

    private Mikrotik() {

    }

    public static Mikrotik getInstance() {
        if (instance == null) {
            instance = new Mikrotik();
        }

        return instance;
    }

    public void onConectar(String host, String port, String usuario, String senha) throws MikrotikApiException {
        try {
            conexao = ApiConnection.connect(SocketFactory.getDefault(), host, Integer.parseInt(port), 2000);
            conexao.login(usuario, senha);
        } catch (MikrotikApiException ex) {
            throw ex;
        }
    }

    public void onConectar(ConnectionBean connectionBean) throws MikrotikApiException {
        try {
            conexao = ApiConnection.connect(SocketFactory.getDefault(), connectionBean.getHost(), Integer.parseInt(connectionBean.getPorta()), 2000);
            conexao.login(connectionBean.getUsuario(), connectionBean.getSenha());
        } catch (MikrotikApiException ex) {
            throw ex;
        }
    }
    
    
    @SuppressWarnings("empty-statement")
    public List<Map<String, String>> onEnviarComando(String comando) throws MikrotikApiException {
        if (conexao == null || !conexao.isConnected()) {
            throw new MikrotikApiException("Nâo conectado");
        }
        List<Map<String, String>> execute = conexao.execute(comando);
        return execute;
    }

 

    public String onEnviarComandoAssincrono(String comando, ResultListener listener) throws MikrotikApiException {
        String tag = conexao.execute("/interface/monitor-traffic where name=eth1_Internet  return rx-bits-per-second",
                listener
        );

        System.out.println(tag);

        return tag;
    }

}


File: /src\main\java\br\com\trixsolucao\mkws\MkwsApplication.java
package br.com.trixsolucao.mkws;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

@SpringBootApplication
public class MkwsApplication {

	public static void main(String[] args) {
		SpringApplication.run(MkwsApplication.class, args);
	}

}


File: /src\main\java\br\com\trixsolucao\mkws\model\FirewallNat.java
package br.com.trixsolucao.mkws.model;

import br.com.trixsolucao.mkws.model.mapping.MkMapping;
import com.fasterxml.jackson.annotation.JsonIgnore;

public class FirewallNat {

    @MkMapping(from ="chain")
    private String chain;

    @MkMapping(from =".id")
    private String id;

    @JsonIgnore
    private String idAux;

    @MkMapping(from ="action")
    private String action;

    @MkMapping(from ="to-ports")
    private String toPorts;

    @MkMapping(from ="dst-port")
    private String dstPort;

    @MkMapping(from ="protocol")
    private String protocol;

    @MkMapping(from ="disabled")
    private String disabled;
    @MkMapping(from = "in-interface")
    private String inInterface;

    public String getIdAux() {
        return idAux;
    }

    public void setIdAux(String idAux) {
        this.idAux = idAux;
    }

    public String getChain() {
        return chain;
    }

    public void setChain(String chain) {
        this.chain = chain;
    }

    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public String getAction() {
        return action;
    }

    public void setAction(String action) {
        this.action = action;
    }


    public String getToPorts() {
        return toPorts;
    }

    public void setToPorts(String toPorts) {
        this.toPorts = toPorts;
    }

    public String getDstPort() {
        return dstPort;
    }

    public void setDstPort(String dstPort) {
        this.dstPort = dstPort;
    }

    public String getProtocol() {
        return protocol;
    }

    public void setProtocol(String protocol) {
        this.protocol = protocol;
    }

    public String getDisabled() {
        return disabled;
    }

    public void setDisabled(String disabled) {
        this.disabled = disabled;
    }

    public String getInInterface() {
        return inInterface;
    }

    public void setInInterface(String inInterface) {
        this.inInterface = inInterface;
    }

    @Override
    public String toString() {
        return "FirewallNat{" +
                "chain='" + chain + '\'' +
                ", id='" + id + '\'' +
                ", action='" + action + '\'' +
                ", toPorts='" + toPorts + '\'' +
                ", dstPort='" + dstPort + '\'' +
                ", protocol='" + protocol + '\'' +
                ", disabled='" + disabled + '\'' +
                ", inInterface='" + inInterface + '\'' +
                '}';
    }
}


File: /src\main\java\br\com\trixsolucao\mkws\model\HotspotActiveUser.java
/*
 * Mikrotik4J, Intregrate Java and Mikrotik RouterOS
 *
 * Copyright (c) 2012, Eits It Solutions and Arthur  
 * or third-party contributors as indicated by the @author tags or express 
 * copyright attribution statements applied by the authors.  All third-party 
 * contributions are distributed under license by Eits It Solutions.
 *
 * This copyrighted material is made available to anyone wishing to use, modify,
 * copy, or redistribute it subject to the terms and conditions of the GNU
 * Lesser General Public License, as published by the Free Software Foundation.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY
 * or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU Lesser General Public License
 * for more details.
 *
 * You should have received a copy of the GNU Lesser General Public License
 * along with this distribution; if not, write to:
 * Free Software Foundation, Inc.
 * 51 Franklin Street, Fifth Floor
 * Boston, MA  02110-1301  USA
 */
package br.com.trixsolucao.mkws.model;


import br.com.trixsolucao.mkws.model.mapping.MkMapping;

/**
 * @author Renan
 */
public class HotspotActiveUser {

    @MkMapping(from = "id")
    private String id;
    @MkMapping(from = "server")
    private String server;
    @MkMapping(from = "user")
    private String user;
    @MkMapping(from = "address")
    private String ipAddress;
    @MkMapping(from = "mac-address")
    private String macAddress;
    @MkMapping(from = "login-by")
    private String loginBy;
    @MkMapping(from = "uptime")
    private String uptime;
    @MkMapping(from = "session-time-left")
    private String sessionTimeLeft;
    @MkMapping(from = "radius")
    private boolean radius;

    /**
     * Default constructor, do nothing...
     */
    public HotspotActiveUser() {
        // do nothing
    }

    public HotspotActiveUser(String user) {
        this.user = user;
    }

    /**
     * @return the id
     */
    public String getId() {
        return id;
    }

    /**
     * @param id the id to set
     */
    public void setId(String id) {
        this.id = id;
    }

    /**
     * @return the server
     */
    public String getServer() {
        return server;
    }

    /**
     * @param server the server to set
     */
    public void setServer(String server) {
        this.server = server;
    }

    /**
     * @return the user
     */
    public String getUser() {
        return user;
    }

    /**
     * @param user the user to set
     */
    public void setUser(String user) {
        this.user = user;
    }

    /**
     * @return the ipAddress
     */
    public String getIpAddress() {
        return ipAddress;
    }

    /**
     * @param ipAddress the ipAddress to set
     */
    public void setIpAddress(String ipAddress) {
        this.ipAddress = ipAddress;
    }

    /**
     * @return the macAddres
     */
    public String getMacAddress() {
        return macAddress;
    }

    /**
     * @param macAddress the macAddres to set
     */
    public void setMacAddress(String macAddress) {
        this.macAddress = macAddress;
    }

    /**
     * @return the loginBy
     */
    public String getLoginBy() {
        return loginBy;
    }

    /**
     * @param loginBy the loginBy to set
     */
    public void setLoginBy(String loginBy) {
        this.loginBy = loginBy;
    }

    /**
     * @return the uptime
     */
    public String getUptime() {
        return uptime;
    }

    /**
     * @param uptime the uptime to set
     */
    public void setUptime(String uptime) {
        this.uptime = uptime;
    }

    /**
     * @return the sessionTimeLeft
     */
    public String getSessionTimeLeft() {
        return sessionTimeLeft;
    }

    /**
     * @param sessionTimeLeft the sessionTimeLeft to set
     */
    public void setSessionTimeLeft(String sessionTimeLeft) {
        this.sessionTimeLeft = sessionTimeLeft;
    }

    /**
     * @return the radius
     */
    public boolean isRadius() {
        return radius;
    }

    /**
     * @param radius the radius to set
     */
    public void setRadius(boolean radius) {
        this.radius = radius;
    }
}


File: /src\main\java\br\com\trixsolucao\mkws\model\HotspotHost.java
/*
 * Mikrotik4J, Intregrate Java and Mikrotik RouterOS
 *
 * Copyright (c) 2012, Eits It Solutions and Arthur 
 * or third-party contributors as indicated by the @author tags or express 
 * copyright attribution statements applied by the authors.  All third-party 
 * contributions are distributed under license by Eits It Solutions.
 *
 * This copyrighted material is made available to anyone wishing to use, modify,
 * copy, or redistribute it subject to the terms and conditions of the GNU
 * Lesser General Public License, as published by the Free Software Foundation.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY
 * or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU Lesser General Public License
 * for more details.
 *
 * You should have received a copy of the GNU Lesser General Public License
 * along with this distribution; if not, write to:
 * Free Software Foundation, Inc.
 * 51 Franklin Street, Fifth Floor
 * Boston, MA  02110-1301  USA
 */
package br.com.trixsolucao.mkws.model;


import br.com.trixsolucao.mkws.model.mapping.MkMapping;

/**
 * @author Renan
 */
public class HotspotHost {

    @MkMapping(from = "mac-address")
    private String macAddress;
    @MkMapping(from = "address")
    private String ipAddress;
    @MkMapping(from = "to-address")
    private String toAddress;
    @MkMapping(from = "server")
    private String server;
    @MkMapping(from = "uptime")
    private String uptime;
    @MkMapping(from = "found-by")
    private String foundBy;
    @MkMapping(from = "authorized")
    private boolean autorized;
    @MkMapping(from = "bypassed")
    private boolean bypassed;

    /**
     * Default constructor, do nothing...
     */
    public HotspotHost() {
        // do nothing
    }

    /**
     * @return the macAddress
     */
    public String getMacAddress() {
        return macAddress;
    }

    /**
     * @param macAddress the macAddress to set
     */
    public void setMacAddress(String macAddress) {
        this.macAddress = macAddress;
    }

    /**
     * @return the ipAddress
     */
    public String getIpAddress() {
        return ipAddress;
    }

    /**
     * @param ipAddress the ipAddress to set
     */
    public void setIpAddress(String ipAddress) {
        this.ipAddress = ipAddress;
    }

    /**
     * @return the toAddress
     */
    public String getToAddress() {
        return toAddress;
    }

    /**
     * @param toAddress the toAddress to set
     */
    public void setToAddress(String toAddress) {
        this.toAddress = toAddress;
    }

    /**
     * @return the server
     */
    public String getServer() {
        return server;
    }

    /**
     * @param server the server to set
     */
    public void setServer(String server) {
        this.server = server;
    }

    /**
     * @return the uptime
     */
    public String getUptime() {
        return uptime;
    }

    /**
     * @param uptime the uptime to set
     */
    public void setUptime(String uptime) {
        this.uptime = uptime;
    }

    /**
     * @return the foundBy
     */
    public String getFoundBy() {
        return foundBy;
    }

    /**
     * @param foundBy the foundBy to set
     */
    public void setFoundBy(String foundBy) {
        this.foundBy = foundBy;
    }

    /**
     * @return the autorized
     */
    public boolean isAutorized() {
        return autorized;
    }

    /**
     * @param autorized the autorized to set
     */
    public void setAutorized(boolean autorized) {
        this.autorized = autorized;
    }

    /**
     * @return the bypassed
     */
    public boolean isBypassed() {
        return bypassed;
    }

    /**
     * @param bypassed the bypassed to set
     */
    public void setBypassed(boolean bypassed) {
        this.bypassed = bypassed;
    }
}


File: /src\main\java\br\com\trixsolucao\mkws\model\HotspotUser.java
package br.com.trixsolucao.mkws.model;

import br.com.trixsolucao.mkws.model.mapping.MkMapping;
import com.fasterxml.jackson.annotation.JsonIgnore;

/**
 *
 * @author Renan
 */

public class HotspotUser {


    @MkMapping(from = ".id")
    private String id;

    @MkMapping(from = "comment")
    private String comment;

    @MkMapping(from = "name")
    private String name;
    @MkMapping(from = "password")
    private String password;
    @MkMapping(from = "profile")
    private String profile;


    private boolean online;

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public String getPassword() {
        return password;
    }

    public void setPassword(String password) {
        this.password = password;
    }

    public String getProfile() {
        return profile;
    }

    public void setProfile(String profile) {
        this.profile = profile;
    }

    public boolean isOnline() {
        return online;
    }

    public void setOnline(boolean online) {
        this.online = online;
    }

    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public String getComment() {
        return comment;
    }

    public void setComment(String comment) {
        this.comment = comment;
    }
}


File: /src\main\java\br\com\trixsolucao\mkws\model\mapping\MapToObject.java
/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package br.com.trixsolucao.mkws.model.mapping;

import java.lang.annotation.Annotation;
import java.lang.reflect.Field;
import java.util.ArrayList;
import java.util.List;
import java.util.Map;
import java.util.logging.Level;
import java.util.logging.Logger;
import com.fasterxml.jackson.databind.ObjectMapper;
import java.util.HashMap;

/**
 *
 * @author Renan
 */
public class MapToObject {





    public static <T> List<T> mapToObject(List<Map<String, String>> listMap, Class<T> clazz) {

        List<T> retorno = new ArrayList<>();

        List<Element<Field, MkMapping>> elements = getAnnotatedFields(MkMapping.class, clazz);

        for (Map<String, String> map : listMap) {
            retorno.add(getObjectFromMap(map, elements, clazz));
        }

        return retorno;

    }

    public static String getStringFromObject(Object object) {
       return  getStringFromMap(getMapFromObject(object));
    }


    public static Map<String, Object> getMapFromObject(Object object) {
        List<Element<Field, MkMapping>> elements = getAnnotatedFields(MkMapping.class, object.getClass());
        Map<String, Object> map = new HashMap<>();
        try {
            for (Element<Field, MkMapping> e : elements) {
                Field f = e.getField();

                f.setAccessible(true);

                //ignora nulos
                if (f.get(object) == null) {
                    continue;
                }
                String chave = "";
                if (e.getAnnotation().from().trim().equals("id")) {
                    chave = "." + e.getAnnotation().from().trim();
                } else {
                    chave = e.getAnnotation().from().trim();
                }
                // if is primitive, cast as primitive
                if (f.getType().isPrimitive()) {

                    map.put("." + e.getAnnotation().from(), f.get(object));

                } else {
                    //Se for String coloco aspas simples por conta dos espaços
                    if (f.getType().isAssignableFrom(String.class)) {
                        map.put(chave, "'" + f.get(object) + "'");
                    } else {
                        map.put(chave, f.get(object));
                    }

                }
            }

        } catch (IllegalAccessException ex) {
            Logger.getLogger(MapToObject.class.getName()).log(Level.SEVERE, null, ex);
        }

        return map;
    }

    public static String getStringFromMap(Map<String, Object> map) {
        StringBuilder stringBuilder = new StringBuilder();
        for (String key : map.keySet()) {

            Object value = map.get(key);

            if (key != null && value != null) {
                stringBuilder.append(" ");
                stringBuilder.append(key);
                stringBuilder.append("=");
                stringBuilder.append(value.toString());

            }

        }

        return stringBuilder.toString();
    }

    private static <T> T getObjectFromMap(Map<String, String> map, List<Element<Field, MkMapping>> elementos, Class<T> clazz) {
        try {
            Object object = clazz.newInstance();

            for (Element<Field, MkMapping> e : elementos) {

                Field f = e.getField();

                f.setAccessible(true);

                // if is primitive, cast as primitive
                if (f.getType().isPrimitive()) {

                    if (f.getType().isAssignableFrom(boolean.class
                    )) {
                        f.set(object, Boolean.valueOf((String) map.get(
                                e.getAnnotation().from())));

                    } else if (f.getType().isAssignableFrom(int.class
                    )) {
                        int intValue = Integer.parseInt(map.get(
                                e.getAnnotation().from()).toString());
                        f.set(object, intValue);

                    } else if (f.getType().isAssignableFrom(double.class
                    )) {
                        double doubleValue = Double.parseDouble(map.get(
                                e.getAnnotation().from()).toString());
                        f.set(object, doubleValue);

                    } else if (f.getType().isAssignableFrom(long.class
                    )) {
                        long longValue = Long.parseLong(map.get(
                                e.getAnnotation().from()).toString());
                        f.set(object, longValue);
                    }
                } else {
                    if (f.getType().isAssignableFrom(Boolean.class
                    )) {
                        f.set(object, Boolean.valueOf((String) map.get(
                                e.getAnnotation().from())));

                    } else {
                        // if object, cast normal to the complex object (String, Integer..)
                        f.set(object, f.getType().cast(map.get(e.getAnnotation().from())));
                    }
                }
            }

            return (T) object;

        } catch (InstantiationException ex) {
            Logger.getLogger(MapToObject.class
                    .getName()).log(Level.SEVERE, null, ex);

        } catch (IllegalAccessException ex) {
            Logger.getLogger(MapToObject.class
                    .getName()).log(Level.SEVERE, null, ex);
        }

        return null;

    }

    public static <A extends Annotation> List<Element<Field, A>>
            getAnnotatedFields(Class<A> annotation, Class<?> clazz) {

        List<Element<Field, A>> elementos = new ArrayList<>();

        Field[] fields = clazz.getDeclaredFields();

        for (Field f : fields) {

            if (f.isAnnotationPresent(annotation)) {
                elementos.add(new Element<>(f, f.getAnnotation(annotation)));
            }
        }

        return elementos;

    }

    public static class Element<F, A extends Annotation> {

        private F field;
        private A annotation;

        /**
         *
         * @param field
         * @param annotation
         */
        public Element(F field, A annotation) {
            this.field = field;
            this.annotation = annotation;
        }

        /**
         * @return the field
         */
        public F getField() {
            return field;
        }

        /**
         * @return the annotation
         */
        public A getAnnotation() {
            return annotation;
        }
    }

}


File: /src\main\java\br\com\trixsolucao\mkws\model\mapping\MkMapping.java
/*
 * Mikrotik4J, Intregrate Java and Mikrotik RouterOS
 *
 * Copyright (c) 2012, Eits It Solutions and Arthur  
 * or third-party contributors as indicated by the @author tags or express 
 * copyright attribution statements applied by the authors.  All third-party 
 * contributions are distributed under license by Eits It Solutions.
 *
 * This copyrighted material is made available to anyone wishing to use, modify,
 * copy, or redistribute it subject to the terms and conditions of the GNU
 * Lesser General Public License, as published by the Free Software Foundation.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY
 * or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU Lesser General Public License
 * for more details.
 *
 * You should have received a copy of the GNU Lesser General Public License
 * along with this distribution; if not, write to:
 * Free Software Foundation, Inc.
 * 51 Franklin Street, Fifth Floor
 * Boston, MA  02110-1301  USA
 */
package br.com.trixsolucao.mkws.model.mapping;

import java.lang.annotation.ElementType;
import java.lang.annotation.Retention;
import java.lang.annotation.RetentionPolicy;
import java.lang.annotation.Target;

/**
 *  @author Renan
 */
@Target(ElementType.FIELD)
@Retention(RetentionPolicy.RUNTIME)
public @interface MkMapping {

    /**
     * The name attribute of the result to be mapped to the attribute of the
     * bean
     *
     * @return the result attribute name to help mapping
     */
    public String from() default "";
}


File: /src\main\java\br\com\trixsolucao\mkws\model\MkCommand.java
/*
 * Mikrotik4J, Intregrate Java and Mikrotik RouterOS
 *
 * Copyright (c) 2012, Eits It Solutions and Arthur  
 * or third-party contributors as indicated by the @author tags or express 
 * copyright attribution statements applied by the authors.  All third-party 
 * contributions are distributed under license by Eits It Solutions.
 *
 * This copyrighted material is made available to anyone wishing to use, modify,
 * copy, or redistribute it subject to the terms and conditions of the GNU
 * Lesser General Public License, as published by the Free Software Foundation.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY
 * or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU Lesser General Public License
 * for more details.
 *
 * You should have received a copy of the GNU Lesser General Public License
 * along with this distribution; if not, write to:
 * Free Software Foundation, Inc.
 * 51 Franklin Street, Fifth Floor
 * Boston, MA  02110-1301  USA
 */
package br.com.trixsolucao.mkws.model;

import java.util.ArrayList;
import java.util.List;

/**
 * Class that encapsulates a command to be sent to the router, it<br/> is
 * possible to send a command with parameters more easily by using <br/> the
 * aiding methods
 *
 * @author Arthur Gregorio
 *
 * @since 1.0
 * @version 1.0, 23/07/2012
 */
public class MkCommand {

    private String baseCommand;
    private List<Parameter> parameters;

    /**
     * The base command to send for the router
     *
     * For example:
     *
     * To retrieve the ip address list send:
     *
     * <code>/ip/address/print</code> as base command
     *
     * if you want to put any parameter in this command, use the
     * {@link MkCommand#appendParameter(String, String)} method
     *
     * @param baseCommand the base command to concatenates with the parameters
     */
    public MkCommand(String baseCommand) {
        this.baseCommand = baseCommand;
        this.parameters = new ArrayList<>();
    }

    /**
     * Append a new parameter in the command string
     *
     * @param parameter the parameter
     * @param value the parameter value
     */
    public void appendParameter(String parameter, String value) {
        parameters.add(new Parameter(parameter, value, ParameterType.COMMON));
    }

    /**
     * Add a where condition to the command string
     * 
     * @param parameter the parameter key
     * @param value the value for the given key
     */
    public void appendWhere(String parameter, String value) {
        parameters.add(new Parameter(parameter, value, ParameterType.WHERE));
    }
    
    
     public void appendEdit(String parameter, String value) {
        parameters.add(new Parameter(parameter, value, ParameterType.EDIT));
    }
    
    /**
     * Concatenates the parameters of a command string to be sent to the router
     *
     * @return the command string
     */
    public String asCommandString() {

        StringBuilder command = new StringBuilder(baseCommand);

        for (int i = 0; i < parameters.size(); i++) {

            Parameter p = parameters.get(i);

            if (p.getType() == ParameterType.COMMON) {
                command.append("\n=");
                command.append(p.getParameter());
                command.append("=");
                command.append(p.getValue());
            } else if(p.getType() == ParameterType.WHERE) {
                command.append("\n?");
                command.append(p.getParameter());
                command.append("=");
                command.append(p.getValue());
            }  else { 
                command.append("\n=");
                command.append(p.getParameter());
                command.append("=");
                command.append(p.getValue());
            }          
        }

        return command.toString();
    }

    /**
     * The encapsulation for parameters in the command
     *
     * @author Arthur Gregorio
     *
     * @since 1.0
     * @version 1.0, 23/07/2012
     */
    private class Parameter {

        private String parameter;
        private String value;
        private ParameterType type;        

        /**
         * Constructor thats recei one parameter and one value for<br/> this
         * parameter (key=value)
         *
         * @param parameter the parameter (key)
         * @param value the value for the parametert (value)
         */
        public Parameter(String parameter, String value, ParameterType type) {
            this.parameter = parameter;
            this.value = value;
            this.type = type;
        }

        /**
         * @return the value of value
         */
        public String getValue() {
            return value;
        }

        /**
         * @return the parameter
         */
        public String getParameter() {
            return parameter;
        }

        /**
         * @return the parameter type
         */
        public ParameterType getType() {
            return type;
        }
    }
    
    /**
     * Mark if the command is where or common command
     */
    private enum ParameterType {
        WHERE, COMMON, EDIT;
    }
}


File: /src\main\java\br\com\trixsolucao\mkws\model\NetworkInterface.java
/*
 * Mikrotik4J, Intregrate Java and Mikrotik RouterOS
 *
 * Copyright (c) 2012, Eits It Solutions and Arthur 
 * or third-party contributors as indicated by the @author tags or express 
 * copyright attribution statements applied by the authors.  All third-party 
 * contributions are distributed under license by Eits It Solutions.
 *
 * This copyrighted material is made available to anyone wishing to use, modify,
 * copy, or redistribute it subject to the terms and conditions of the GNU
 * Lesser General Public License, as published by the Free Software Foundation.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY
 * or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU Lesser General Public License
 * for more details.
 *
 * You should have received a copy of the GNU Lesser General Public License
 * along with this distribution; if not, write to:
 * Free Software Foundation, Inc.
 * 51 Franklin Street, Fifth Floor
 * Boston, MA  02110-1301  USA
 */
package br.com.trixsolucao.mkws.model;


import br.com.trixsolucao.mkws.model.mapping.MkMapping;

/**
 * @author Renan
 */
public class NetworkInterface {

    @MkMapping(from = "id")
    private String id;
    @MkMapping(from = "address")
    private String address;
    @MkMapping(from = "network")
    private String network;
    @MkMapping(from = "interface")
    private String interfaceName;
    @MkMapping(from = "actual-interface")
    private String actualInterface;
    @MkMapping(from = "invalid")
    private boolean invalid;
    @MkMapping(from = "dynamic")
    private boolean dynamic;
    @MkMapping(from = "disabled")
    private boolean disabled;
    @MkMapping(from = "comment")
    private String comment;

    @MkMapping(from = "name")
    private String name;

    /**
     * Default constructor, do nothing...
     */
    public NetworkInterface() {
        // do nothing
    }

    /**
     * @return the id
     */
    public String getId() {
        return id;
    }

    /**
     * @param id the id to set
     */
    public void setId(String id) {
        this.id = id;
    }

    /**
     * @return the address
     */
    public String getAddress() {
        return address;
    }

    /**
     * @param address the address to set
     */
    public void setAddress(String address) {
        this.address = address;
    }

    /**
     * @return the network
     */
    public String getNetwork() {
        return network;
    }

    /**
     * @param network the network to set
     */
    public void setNetwork(String network) {
        this.network = network;
    }

    /**
     * @return the interfaceName
     */
    public String getInterfaceName() {
        return interfaceName;
    }

    /**
     * @param interfaceName the interfaceName to set
     */
    public void setInterfaceName(String interfaceName) {
        this.interfaceName = interfaceName;
    }

    /**
     * @return the actualInterface
     */
    public String getActualInterface() {
        return actualInterface;
    }

    /**
     * @param actualInterface the actualInterface to set
     */
    public void setActualInterface(String actualInterface) {
        this.actualInterface = actualInterface;
    }

    /**
     * @return the invalid
     */
    public boolean isInvalid() {
        return invalid;
    }

    /**
     * @param invalid the invalid to set
     */
    public void setInvalid(boolean invalid) {
        this.invalid = invalid;
    }

    /**
     * @return the dynamic
     */
    public boolean isDynamic() {
        return dynamic;
    }

    /**
     * @param dynamic the dynamic to set
     */
    public void setDynamic(boolean dynamic) {
        this.dynamic = dynamic;
    }

    /**
     * @return the disabled
     */
    public boolean isDisabled() {
        return disabled;
    }

    /**
     * @param disabled the disabled to set
     */
    public void setDisabled(boolean disabled) {
        this.disabled = disabled;
    }

    /**
     * @return the comment
     */
    public String getComment() {
        return comment;
    }

    /**
     * @param comment the comment to set
     */
    public void setComment(String comment) {
        this.comment = comment;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

}


File: /src\main\java\br\com\trixsolucao\mkws\model\PPPActiveUser.java
/*
 * Mikrotik4J, Intregrate Java and Mikrotik RouterOS
 *
 * Copyright (c) 2012, Eits It Solutions and Arthur 
 * or third-party contributors as indicated by the @author tags or express 
 * copyright attribution statements applied by the authors.  All third-party 
 * contributions are distributed under license by Eits It Solutions.
 *
 * This copyrighted material is made available to anyone wishing to use, modify,
 * copy, or redistribute it subject to the terms and conditions of the GNU
 * Lesser General Public License, as published by the Free Software Foundation.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY
 * or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU Lesser General Public License
 * for more details.
 *
 * You should have received a copy of the GNU Lesser General Public License
 * along with this distribution; if not, write to:
 * Free Software Foundation, Inc.
 * 51 Franklin Street, Fifth Floor
 * Boston, MA  02110-1301  USA
 */
package br.com.trixsolucao.mkws.model;


import br.com.trixsolucao.mkws.model.mapping.MkMapping;

import java.util.Objects;

/**
 * @author Renan
 */
public class PPPActiveUser {

    @MkMapping(from = "id")
    private String id;
    @MkMapping(from = "server")
    private String server;
    @MkMapping(from = "name")
    private String user;
    @MkMapping(from = "address")
    private String ipAddress;
    @MkMapping(from = "caller-id")
    private String macAddress;
    @MkMapping(from = "login-by")
    private String loginBy;
    @MkMapping(from = "uptime")
    private String uptime;
    @MkMapping(from = "session-time-left")
    private String sessionTimeLeft;
    @MkMapping(from = "radius")
    private boolean radius;

    /**
     * Default constructor, do nothing...
     */
    public PPPActiveUser() {
        // do nothing
    }

    public PPPActiveUser(String user) {
        this.user = user;
    }

    /**
     * @return the id
     */
    public String getId() {
        return id;
    }

    /**
     * @param id the id to set
     */
    public void setId(String id) {
        this.id = id;
    }

    /**
     * @return the server
     */
    public String getServer() {
        return server;
    }

    /**
     * @param server the server to set
     */
    public void setServer(String server) {
        this.server = server;
    }

    /**
     * @return the user
     */
    public String getUser() {
        return user;
    }

    /**
     * @param user the user to set
     */
    public void setUser(String user) {
        this.user = user;
    }

    /**
     * @return the ipAddress
     */
    public String getIpAddress() {
        return ipAddress;
    }

    /**
     * @param ipAddress the ipAddress to set
     */
    public void setIpAddress(String ipAddress) {
        this.ipAddress = ipAddress;
    }

    /**
     * @return the macAddres
     */
    public String getMacAddress() {
        return macAddress;
    }

    /**
     * @param macAddress the macAddres to set
     */
    public void setMacAddress(String macAddress) {
        this.macAddress = macAddress;
    }

    /**
     * @return the loginBy
     */
    public String getLoginBy() {
        return loginBy;
    }

    /**
     * @param loginBy the loginBy to set
     */
    public void setLoginBy(String loginBy) {
        this.loginBy = loginBy;
    }

    /**
     * @return the uptime
     */
    public String getUptime() {
        return uptime;
    }

    /**
     * @param uptime the uptime to set
     */
    public void setUptime(String uptime) {
        this.uptime = uptime;
    }

    /**
     * @return the sessionTimeLeft
     */
    public String getSessionTimeLeft() {
        return sessionTimeLeft;
    }

    /**
     * @param sessionTimeLeft the sessionTimeLeft to set
     */
    public void setSessionTimeLeft(String sessionTimeLeft) {
        this.sessionTimeLeft = sessionTimeLeft;
    }

    /**
     * @return the radius
     */
    public boolean isRadius() {
        return radius;
    }

    /**
     * @param radius the radius to set
     */
    public void setRadius(boolean radius) {
        this.radius = radius;
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;
        PPPActiveUser that = (PPPActiveUser) o;
        return Objects.equals(user, that.user);
    }

    @Override
    public int hashCode() {
        return Objects.hash(user);
    }
}


File: /src\main\java\br\com\trixsolucao\mkws\model\PPPProfiles.java
/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package br.com.trixsolucao.mkws.model;


import br.com.trixsolucao.mkws.model.mapping.MkMapping;

/**
 *
 * @author Renan
 */
public class PPPProfiles {

    @MkMapping(from = "id")
    private String id;
    @MkMapping(from = "name")
    private String name;
    @MkMapping(from = "local-address")
    private String localAddress;
    @MkMapping(from = "remote-address")
    private String remoteAddress;
    @MkMapping(from = "use-mpls")
    private String useMpls;
    @MkMapping(from = "use-compression")
    private String useCompression;
    @MkMapping(from = "use-encryption")
    private String useEncryption;
    @MkMapping(from = "only-one")
    private String onlyOne;
    @MkMapping(from = "change-tcp-mss")
    private String changeTcpMss;
    @MkMapping(from = "use-upnp")
    private String useUpnp;
    @MkMapping(from = "address-list")
    private String addressList;
    @MkMapping(from = "dns-server")
    private String dnsServcer;
    @MkMapping(from = "on-up")
    private String onUp;
    @MkMapping(from = "on-down")
    private String onDown;
    @MkMapping(from = "rate-limit")
    private String rateLimit;

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public String getLocalAddress() {
        return localAddress;
    }

    public void setLocalAddress(String localAddress) {
        this.localAddress = localAddress;
    }

    public String getRemoteAddress() {
        return remoteAddress;
    }

    public void setRemoteAddress(String remoteAddress) {
        this.remoteAddress = remoteAddress;
    }

    public String getUseMpls() {
        return useMpls;
    }

    public void setUseMpls(String useMpls) {
        this.useMpls = useMpls;
    }

    public String getUseCompression() {
        return useCompression;
    }

    public void setUseCompression(String useCompression) {
        this.useCompression = useCompression;
    }

    public String getUseEncryption() {
        return useEncryption;
    }

    public void setUseEncryption(String useEncryption) {
        this.useEncryption = useEncryption;
    }

    public String getOnlyOne() {
        return onlyOne;
    }

    public void setOnlyOne(String onlyOne) {
        this.onlyOne = onlyOne;
    }

    public String getChangeTcpMss() {
        return changeTcpMss;
    }

    public void setChangeTcpMss(String changeTcpMss) {
        this.changeTcpMss = changeTcpMss;
    }

    public String getUseUpnp() {
        return useUpnp;
    }

    public void setUseUpnp(String useUpnp) {
        this.useUpnp = useUpnp;
    }

    public String getAddressList() {
        return addressList;
    }

    public void setAddressList(String addressList) {
        this.addressList = addressList;
    }

    public String getDnsServcer() {
        return dnsServcer;
    }

    public void setDnsServcer(String dnsServcer) {
        this.dnsServcer = dnsServcer;
    }

    public String getOnUp() {
        return onUp;
    }

    public void setOnUp(String onUp) {
        this.onUp = onUp;
    }

    public String getOnDown() {
        return onDown;
    }

    public void setOnDown(String onDown) {
        this.onDown = onDown;
    }

    public String getRateLimit() {
        return rateLimit;
    }

    public void setRateLimit(String rateLimit) {
        this.rateLimit = rateLimit;
    }

    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

}


File: /src\main\java\br\com\trixsolucao\mkws\model\PPPUsers.java
/*
 * Mikrotik4J, Intregrate Java and Mikrotik RouterOS
 *
 * Copyright (c) 2012, Eits It Solutions and Arthur   
 * or third-party contributors as indicated by the @author tags or express 
 * copyright attribution statements applied by the authors.  All third-party 
 * contributions are distributed under license by Eits It Solutions.
 *
 * This copyrighted material is made available to anyone wishing to use, modify,
 * copy, or redistribute it subject to the terms and conditions of the GNU
 * Lesser General Public License, as published by the Free Software Foundation.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY
 * or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU Lesser General Public License
 * for more details.
 *
 * You should have received a copy of the GNU Lesser General Public License
 * along with this distribution; if not, write to:
 * Free Software Foundation, Inc.
 * 51 Franklin Street, Fifth Floor
 * Boston, MA  02110-1301  USA
 */
package br.com.trixsolucao.mkws.model;


import br.com.trixsolucao.mkws.mkapi.ConnectionBean;
import br.com.trixsolucao.mkws.model.mapping.MkMapping;

/**
 * @author Renan
 */
public class PPPUsers   {

    @MkMapping(from = ".id")
    private String id;
    @MkMapping(from = "service")
    private String service;
    @MkMapping(from = "name")
    private String user;
    @MkMapping(from = "password")
    private String password;
    @MkMapping(from = "address")
    private String ipAddress;
    @MkMapping(from = "caller-id")
    private String macAddress;
    @MkMapping(from = "profile")
    private String profile;

    @MkMapping(from = "routes")
    private String routes;

    @MkMapping(from = "limit-bytes-in")
    private String limitIn;

    @MkMapping(from = "limit-bytes-out")
    private String limitOut;

    @MkMapping(from = "last-logged-out")
    private Boolean lastLogout;

    private String newUser;

    @MkMapping(from = "comment")
    private String comment;

    private boolean online;

    private ConnectionBean connectionBean;


    /**
     * Default constructor, do nothing...
     */
    public PPPUsers() {
        // do nothing
    }

    public ConnectionBean getConnectionBean() {
        return connectionBean;
    }

    public void setConnectionBean(ConnectionBean connectionBean) {
        this.connectionBean = connectionBean;
    }

    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public String getService() {
        return service;
    }

    public void setService(String service) {
        this.service = service;
    }

    public String getUser() {
        return user;
    }

    public void setUser(String user) {
        this.user = user;
    }

    public String getPassword() {
        return password;
    }

    public void setPassword(String password) {
        this.password = password;
    }

    public String getIpAddress() {
        return ipAddress;
    }

    public void setIpAddress(String ipAddress) {
        this.ipAddress = ipAddress;
    }

    public String getMacAddress() {
        return macAddress;
    }

    public void setMacAddress(String macAddress) {
        this.macAddress = macAddress;
    }

    public String getProfile() {
        return profile;
    }

    public void setProfile(String profile) {
        this.profile = profile;
    }

    public String getRoutes() {
        return routes;
    }

    public void setRoutes(String routes) {
        this.routes = routes;
    }

    public String getLimitIn() {
        return limitIn;
    }

    public void setLimitIn(String limitIn) {
        this.limitIn = limitIn;
    }

    public String getLimitOut() {
        return limitOut;
    }

    public void setLimitOut(String limitOut) {
        this.limitOut = limitOut;
    }

    public Boolean isLastLogout() {
        return lastLogout;
    }

    public void setLastLogout(Boolean lastLogout) {
        this.lastLogout = lastLogout;
    }

    public boolean isOnline() {
        return online;
    }

    public void setOnline(boolean online) {
        this.online = online;
    }

    public String getNewUser() {
        if (newUser == null || newUser.equals("")) {
            newUser = user;
        }

        return newUser;
    }

    public void setNewUser(String newUser) {
        this.newUser = newUser;
    }

    public String getComment() {
        return comment;
    }

    public void setComment(String comment) {
        this.comment = comment;
    }

}


File: /src\main\java\br\com\trixsolucao\mkws\model\RadiusProfile.java
/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package br.com.trixsolucao.mkws.model;


import br.com.trixsolucao.mkws.model.mapping.MkMapping;

/**
 *
 * @author Renan
 */
public class RadiusProfile {
    
    @MkMapping(from= "name")
    private String name;

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    
    
    
}


File: /src\main\java\br\com\trixsolucao\mkws\model\RadiusUser.java
/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package br.com.trixsolucao.mkws.model;


import br.com.trixsolucao.mkws.model.mapping.MkMapping;

/**
 *
 * @author Renan
 */
public class RadiusUser {
     
  
    @MkMapping(from = "username")
    private String user;
    @MkMapping(from = "password")
    private String password;
    @MkMapping(from = "shared-users")
    private String sharedUsers;
    @MkMapping(from = "actual-profile")
    private String profile;   
    
    @MkMapping(from = "customer")
    private String customer;
    
    @MkMapping(from = "first-name")
    private String nome;
    
    @MkMapping(from = "disabled")
    private String disabled;
    
    private String newUser;

    
    public String getUserPropert() {
        return "username";
    }

    public String getUser() {
        return user;
    }

    public void setUser(String user) {
        this.user = user;
    }
    
    public String getPasswordPropert() {
        return "password";
    }

    public String getPassword() {
        return password;
    }

    public void setPassword(String password) {
        this.password = password;
    }
    
    public String getProfilePropert() {
        return "actual-profile";
    }

    public String getSharedUsers() {
        return sharedUsers;
    }

    public void setSharedUsers(String sharedUsers) {
        this.sharedUsers = sharedUsers;
    }
    
    public String getSharedUsersPropert() {
        return "shared-users";
    }

    public String getProfile() {
        return profile;
    }

    public void setProfile(String profile) {
        this.profile = profile;
    }

    public String getNewUser() {
        return newUser;
    }

    public void setNewUser(String newUser) {
        this.newUser = newUser;
    }
    
    public String getCustomerPropert() {
        return "customer";
    }

    public String getCustomer() {
        if(customer == null || customer.equals("")) customer = "admin";
        return customer;
    }

    public void setCustomer(String customer) {
        this.customer = customer;
    }

    public String getNomePropert() {
        return "first-name";
    }
    
    public String getNome() {
        return nome;
    }

    public void setNome(String nome) {
        this.nome = nome;
    }

    public String getDisabledPropert() {
        return "disabled";
    }
    
    public String getDisabled() {
        return disabled;
    }
    
    public String getDisabledString() {
        if(disabled == null) return "";
        if(disabled.equals("false")) return "ATIVO";
        else return "BLOQUEADO";
      
    }
    
    public boolean isAtivo() {
        if(disabled.equals("false")) return true;
        else return false;
    }

    public void setDisabled(String disabled) {
        this.disabled = disabled;
    }
    
    
    
    
    
}


File: /src\main\java\br\com\trixsolucao\mkws\model\Resources.java
package br.com.trixsolucao.mkws.model;

import br.com.trixsolucao.mkws.model.mapping.MkMapping;
import lombok.Getter;
import lombok.Setter;

@Getter
@Setter
public class Resources {

    @MkMapping(from = "uptime")
    private String uptime;

    @MkMapping(from = "version")
    private String version;

    @MkMapping(from = "build-time")
    private String buildTime;

    @MkMapping(from = "factory-software")
    private String factorySoftware;

    @MkMapping(from = "free-memory")
    private String freeMemory;

    @MkMapping(from = "total-memory")
    private String totalMemory;

    @MkMapping(from = "cpu")
    private String cpu;

    @MkMapping(from = "cpu-count")
    private String cpuCount;

    @MkMapping(from = "cpu-frequency")
    private String cpuFrequency;

    @MkMapping(from = "cpu-load")
    private String cpuLoad;

    @MkMapping(from = "free-hdd-space")
    private String freeHdSpace;

    @MkMapping(from = "write-sect-since-reboot")
    private String writeSectSinceReboot;

    @MkMapping(from = "write-sect-total")
    private String writeSectTotal;

    @MkMapping(from = "bad-blocks")
    private String badBlocks;

    @MkMapping(from = "architecture-name")
    private String architectureName;

    @MkMapping(from = "board-name")
    private String boardName;

    @MkMapping(from = "platform")
    private String platform;


}


File: /src\main\java\br\com\trixsolucao\mkws\model\TypesList.java
package br.com.trixsolucao.mkws.model;

public enum TypesList {

    PPPOE_LIST("pppoe_list"),
    PPPOE_ACTIVES("pppoe_actives"),
    PPPOE_PLANS("pppoe_plans");

    private String type;


    TypesList(String type) {
        this.type = type;
    }

    public String getType() {
        return type;
    }
}


File: /src\main\java\br\com\trixsolucao\mkws\util\JasyptTools.java
package br.com.trixsolucao.mkws.util;

import org.jasypt.util.text.BasicTextEncryptor;
/*
*  Classe ainda não usada
* */


public class JasyptTools {

    private static BasicTextEncryptor bte;
    private static final String CODIFICACAO = "ESSA SENHA É UM SEGREDO, SABEMOS QUE NÃO DEVERIA ESTAR NO CÓDIGO";


    public static String decode(String pass) {
        bte = new BasicTextEncryptor();
        bte.setPassword(CODIFICACAO);
        return bte.decrypt(pass);

    }

    public static String encode(String pass) {
        bte = new BasicTextEncryptor();
        bte.setPassword(CODIFICACAO);
        return bte.encrypt(pass);
    }
}


File: /src\main\resources\application-dev.yml
app:
  message: Propriedades carregadas para o ambiente de desenvolvimento



File: /src\main\resources\application.properties
spring.profiles.active=dev

spring.application.name=WebService Rest API Mikrotik RouterOS
java.runtime.version=9


File: /src\test\java\br\com\trixsolucao\mkws\MkwsApplicationTests.java
package br.com.trixsolucao.mkws;

import org.junit.jupiter.api.Test;
import org.springframework.boot.test.context.SpringBootTest;

@SpringBootTest
class MkwsApplicationTests {

	@Test
	void contextLoads() {
	}

}


File: /system.properties
java.runtime.version=11

