# Repository Information
Name: mikrotik-example

# Directory Structure
Directory structure:
└── github_repos/mikrotik-example/
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
    │   │       ├── pack-253900c65f49d98cc614ec4be85ed61bfa4b647f.idx
    │   │       └── pack-253900c65f49d98cc614ec4be85ed61bfa4b647f.pack
    │   ├── packed-refs
    │   └── refs/
    │       ├── heads/
    │       │   └── master
    │       ├── remotes/
    │       │   └── origin/
    │       │       └── HEAD
    │       └── tags/
    ├── .gitignore
    ├── build.gradle
    ├── gradle/
    │   └── wrapper/
    │       ├── gradle-wrapper.jar
    │       └── gradle-wrapper.properties
    ├── gradlew
    ├── gradlew.bat
    ├── README.md
    ├── settings.gradle
    └── src/
        ├── main/
        │   ├── java/
        │   │   └── mikrotik/
        │   │       └── example/
        │   │           ├── command/
        │   │           │   └── MikrotikCommands.java
        │   │           ├── MikrotikExampleApplication.java
        │   │           └── runner/
        │   │               ├── AbstractMikrotikRunner.java
        │   │               ├── DpRelatedMikrotikCommandRunner.java
        │   │               ├── MikrotikAnnonTlsLoginRunner.java
        │   │               ├── MikrotikDhcpServerCommandRunner.java
        │   │               ├── MikrotikInterfaceCommandRunner.java
        │   │               ├── MikrotikIpPoolCommandRunner.java
        │   │               ├── MikrotikLoginRunner.java
        │   │               └── MikrotikPppoeServerCommandRunner.java
        │   └── resources/
        │       └── application.properties
        ├── site/
        │   └── images/
        └── test/
            └── java/
                └── mikrotik/
                    └── example/
                        └── MikrotikExampleApplicationTests.java


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
	url = https://github.com/amitmisra16/mikrotik-example.git
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
0000000000000000000000000000000000000000 8a74e1fb54fcc8e8789148a47b3a6b09a3757e06 vivek-dodia <vivek.dodia@icloud.com> 1738606312 -0500	clone: from https://github.com/amitmisra16/mikrotik-example.git


File: /.git\logs\refs\heads\master
0000000000000000000000000000000000000000 8a74e1fb54fcc8e8789148a47b3a6b09a3757e06 vivek-dodia <vivek.dodia@icloud.com> 1738606312 -0500	clone: from https://github.com/amitmisra16/mikrotik-example.git


File: /.git\logs\refs\remotes\origin\HEAD
0000000000000000000000000000000000000000 8a74e1fb54fcc8e8789148a47b3a6b09a3757e06 vivek-dodia <vivek.dodia@icloud.com> 1738606312 -0500	clone: from https://github.com/amitmisra16/mikrotik-example.git


File: /.git\packed-refs
# pack-refs with: peeled fully-peeled sorted 
8a74e1fb54fcc8e8789148a47b3a6b09a3757e06 refs/remotes/origin/master


File: /.git\refs\heads\master
8a74e1fb54fcc8e8789148a47b3a6b09a3757e06


File: /.git\refs\remotes\origin\HEAD
ref: refs/remotes/origin/master


File: /.gitignore
.gradle
/build/
!gradle/wrapper/gradle-wrapper.jar

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
/out/

### NetBeans ###
/nbproject/private/
/build/
/nbbuild/
/dist/
/nbdist/
/.nb-gradle/

File: /build.gradle
buildscript {
	ext {
		springBootVersion = '2.0.2.RELEASE'
	}
	repositories {
		mavenCentral()
	}
	dependencies {
		classpath("org.springframework.boot:spring-boot-gradle-plugin:${springBootVersion}")
	}
}

apply plugin: 'java'
apply plugin: 'eclipse'
apply plugin: 'org.springframework.boot'
apply plugin: 'io.spring.dependency-management'

group = 'mikrotik.example'
version = '0.0.1-SNAPSHOT'
sourceCompatibility = 1.8

repositories {
	mavenCentral()
}


dependencies {
	compile('org.springframework.boot:spring-boot-starter-actuator')
	runtime('org.springframework.boot:spring-boot-devtools')
	compileOnly('org.projectlombok:lombok')
	testCompile('org.springframework.boot:spring-boot-starter-test')
	compile('me.legrange:mikrotik:3.0.4')
}


File: /gradle\wrapper\gradle-wrapper.properties
#Thu Jun 07 15:56:09 EDT 2018
distributionBase=GRADLE_USER_HOME
distributionPath=wrapper/dists
zipStoreBase=GRADLE_USER_HOME
zipStorePath=wrapper/dists
distributionUrl=https\://services.gradle.org/distributions/gradle-4.5.1-all.zip


File: /gradlew
#!/usr/bin/env sh

##############################################################################
##
##  Gradle start up script for UN*X
##
##############################################################################

# Attempt to set APP_HOME
# Resolve links: $0 may be a link
PRG="$0"
# Need this for relative symlinks.
while [ -h "$PRG" ] ; do
    ls=`ls -ld "$PRG"`
    link=`expr "$ls" : '.*-> \(.*\)$'`
    if expr "$link" : '/.*' > /dev/null; then
        PRG="$link"
    else
        PRG=`dirname "$PRG"`"/$link"
    fi
done
SAVED="`pwd`"
cd "`dirname \"$PRG\"`/" >/dev/null
APP_HOME="`pwd -P`"
cd "$SAVED" >/dev/null

APP_NAME="Gradle"
APP_BASE_NAME=`basename "$0"`

# Add default JVM options here. You can also use JAVA_OPTS and GRADLE_OPTS to pass JVM options to this script.
DEFAULT_JVM_OPTS=""

# Use the maximum available, or set MAX_FD != -1 to use that value.
MAX_FD="maximum"

warn ( ) {
    echo "$*"
}

die ( ) {
    echo
    echo "$*"
    echo
    exit 1
}

# OS specific support (must be 'true' or 'false').
cygwin=false
msys=false
darwin=false
nonstop=false
case "`uname`" in
  CYGWIN* )
    cygwin=true
    ;;
  Darwin* )
    darwin=true
    ;;
  MINGW* )
    msys=true
    ;;
  NONSTOP* )
    nonstop=true
    ;;
esac

CLASSPATH=$APP_HOME/gradle/wrapper/gradle-wrapper.jar

# Determine the Java command to use to start the JVM.
if [ -n "$JAVA_HOME" ] ; then
    if [ -x "$JAVA_HOME/jre/sh/java" ] ; then
        # IBM's JDK on AIX uses strange locations for the executables
        JAVACMD="$JAVA_HOME/jre/sh/java"
    else
        JAVACMD="$JAVA_HOME/bin/java"
    fi
    if [ ! -x "$JAVACMD" ] ; then
        die "ERROR: JAVA_HOME is set to an invalid directory: $JAVA_HOME

Please set the JAVA_HOME variable in your environment to match the
location of your Java installation."
    fi
else
    JAVACMD="java"
    which java >/dev/null 2>&1 || die "ERROR: JAVA_HOME is not set and no 'java' command could be found in your PATH.

Please set the JAVA_HOME variable in your environment to match the
location of your Java installation."
fi

# Increase the maximum file descriptors if we can.
if [ "$cygwin" = "false" -a "$darwin" = "false" -a "$nonstop" = "false" ] ; then
    MAX_FD_LIMIT=`ulimit -H -n`
    if [ $? -eq 0 ] ; then
        if [ "$MAX_FD" = "maximum" -o "$MAX_FD" = "max" ] ; then
            MAX_FD="$MAX_FD_LIMIT"
        fi
        ulimit -n $MAX_FD
        if [ $? -ne 0 ] ; then
            warn "Could not set maximum file descriptor limit: $MAX_FD"
        fi
    else
        warn "Could not query maximum file descriptor limit: $MAX_FD_LIMIT"
    fi
fi

# For Darwin, add options to specify how the application appears in the dock
if $darwin; then
    GRADLE_OPTS="$GRADLE_OPTS \"-Xdock:name=$APP_NAME\" \"-Xdock:icon=$APP_HOME/media/gradle.icns\""
fi

# For Cygwin, switch paths to Windows format before running java
if $cygwin ; then
    APP_HOME=`cygpath --path --mixed "$APP_HOME"`
    CLASSPATH=`cygpath --path --mixed "$CLASSPATH"`
    JAVACMD=`cygpath --unix "$JAVACMD"`

    # We build the pattern for arguments to be converted via cygpath
    ROOTDIRSRAW=`find -L / -maxdepth 1 -mindepth 1 -type d 2>/dev/null`
    SEP=""
    for dir in $ROOTDIRSRAW ; do
        ROOTDIRS="$ROOTDIRS$SEP$dir"
        SEP="|"
    done
    OURCYGPATTERN="(^($ROOTDIRS))"
    # Add a user-defined pattern to the cygpath arguments
    if [ "$GRADLE_CYGPATTERN" != "" ] ; then
        OURCYGPATTERN="$OURCYGPATTERN|($GRADLE_CYGPATTERN)"
    fi
    # Now convert the arguments - kludge to limit ourselves to /bin/sh
    i=0
    for arg in "$@" ; do
        CHECK=`echo "$arg"|egrep -c "$OURCYGPATTERN" -`
        CHECK2=`echo "$arg"|egrep -c "^-"`                                 ### Determine if an option

        if [ $CHECK -ne 0 ] && [ $CHECK2 -eq 0 ] ; then                    ### Added a condition
            eval `echo args$i`=`cygpath --path --ignore --mixed "$arg"`
        else
            eval `echo args$i`="\"$arg\""
        fi
        i=$((i+1))
    done
    case $i in
        (0) set -- ;;
        (1) set -- "$args0" ;;
        (2) set -- "$args0" "$args1" ;;
        (3) set -- "$args0" "$args1" "$args2" ;;
        (4) set -- "$args0" "$args1" "$args2" "$args3" ;;
        (5) set -- "$args0" "$args1" "$args2" "$args3" "$args4" ;;
        (6) set -- "$args0" "$args1" "$args2" "$args3" "$args4" "$args5" ;;
        (7) set -- "$args0" "$args1" "$args2" "$args3" "$args4" "$args5" "$args6" ;;
        (8) set -- "$args0" "$args1" "$args2" "$args3" "$args4" "$args5" "$args6" "$args7" ;;
        (9) set -- "$args0" "$args1" "$args2" "$args3" "$args4" "$args5" "$args6" "$args7" "$args8" ;;
    esac
fi

# Escape application args
save ( ) {
    for i do printf %s\\n "$i" | sed "s/'/'\\\\''/g;1s/^/'/;\$s/\$/' \\\\/" ; done
    echo " "
}
APP_ARGS=$(save "$@")

# Collect all arguments for the java command, following the shell quoting and substitution rules
eval set -- $DEFAULT_JVM_OPTS $JAVA_OPTS $GRADLE_OPTS "\"-Dorg.gradle.appname=$APP_BASE_NAME\"" -classpath "\"$CLASSPATH\"" org.gradle.wrapper.GradleWrapperMain "$APP_ARGS"

# by default we should be in the correct project dir, but when run from Finder on Mac, the cwd is wrong
if [ "$(uname)" = "Darwin" ] && [ "$HOME" = "$PWD" ]; then
  cd "$(dirname "$0")"
fi

exec "$JAVACMD" "$@"


File: /gradlew.bat
@if "%DEBUG%" == "" @echo off
@rem ##########################################################################
@rem
@rem  Gradle startup script for Windows
@rem
@rem ##########################################################################

@rem Set local scope for the variables with windows NT shell
if "%OS%"=="Windows_NT" setlocal

set DIRNAME=%~dp0
if "%DIRNAME%" == "" set DIRNAME=.
set APP_BASE_NAME=%~n0
set APP_HOME=%DIRNAME%

@rem Add default JVM options here. You can also use JAVA_OPTS and GRADLE_OPTS to pass JVM options to this script.
set DEFAULT_JVM_OPTS=

@rem Find java.exe
if defined JAVA_HOME goto findJavaFromJavaHome

set JAVA_EXE=java.exe
%JAVA_EXE% -version >NUL 2>&1
if "%ERRORLEVEL%" == "0" goto init

echo.
echo ERROR: JAVA_HOME is not set and no 'java' command could be found in your PATH.
echo.
echo Please set the JAVA_HOME variable in your environment to match the
echo location of your Java installation.

goto fail

:findJavaFromJavaHome
set JAVA_HOME=%JAVA_HOME:"=%
set JAVA_EXE=%JAVA_HOME%/bin/java.exe

if exist "%JAVA_EXE%" goto init

echo.
echo ERROR: JAVA_HOME is set to an invalid directory: %JAVA_HOME%
echo.
echo Please set the JAVA_HOME variable in your environment to match the
echo location of your Java installation.

goto fail

:init
@rem Get command-line arguments, handling Windows variants

if not "%OS%" == "Windows_NT" goto win9xME_args

:win9xME_args
@rem Slurp the command line arguments.
set CMD_LINE_ARGS=
set _SKIP=2

:win9xME_args_slurp
if "x%~1" == "x" goto execute

set CMD_LINE_ARGS=%*

:execute
@rem Setup the command line

set CLASSPATH=%APP_HOME%\gradle\wrapper\gradle-wrapper.jar

@rem Execute Gradle
"%JAVA_EXE%" %DEFAULT_JVM_OPTS% %JAVA_OPTS% %GRADLE_OPTS% "-Dorg.gradle.appname=%APP_BASE_NAME%" -classpath "%CLASSPATH%" org.gradle.wrapper.GradleWrapperMain %CMD_LINE_ARGS%

:end
@rem End local scope for the variables with windows NT shell
if "%ERRORLEVEL%"=="0" goto mainEnd

:fail
rem Set variable GRADLE_EXIT_CONSOLE if you need the _script_ return code instead of
rem the _cmd.exe /c_ return code!
if  not "" == "%GRADLE_EXIT_CONSOLE%" exit 1
exit /b 1

:mainEnd
if "%OS%"=="Windows_NT" endlocal

:omega


File: /README.md
# Mikrotik Example

This project uses java api provided by [Mikrotik-java](https://github.com/GideonLeGrange/mikrotik-java) to connect to a mikrotik routerOS and execute some 
commands. 

## Initial setup

Follow the [blog](http://myhomelab.blogspot.com/2013/05/installing-mikrotik-routeros-under-VirtualBox.html) to setup Mikrotik routerOS virtualbox locally.

## Port forwarding on virtual box

![Virtualbox port forwarding setting](./src/site/images/VBPortFwdSetting.png)

## Running the project

Each command is part of a separate spring boot command line runner. To execute all the commands simply run the following command - 

```$bash
./gradlew build
```




File: /settings.gradle
rootProject.name = 'mikrotik-example'


File: /src\main\java\mikrotik\example\command\MikrotikCommands.java
package mikrotik.example.command;

public enum MikrotikCommands {

    INTERFACE_PRINT("/interface/print"),
    INTERFACE_ETHERNET_PRINT("/interface/ethernet/print"),
    INTERFACE_PPPOE_SERVER_PRINT_COMMAND("/interface/pppoe-server/print"),
    INTERFACE_PPPOE_SERVER_SERVER_PRINT_COMMAND("/interface/pppoe-server/server/print"),
    INTERFACE_PPPOE_CLIENT_PRINT_COMMAND("/interface/pppoe-client/print"),
    PPP_PROFILE_PRINT("/ppp/profile/print"),
    PPP_SECRET_PRINT("/ppp/secret/print"),
    IP_ADDRESS_PRINT("/ip/address/print"),
    IP_POOL_PRINT_COMMAND("/ip/pool/print"),
    IP_POOL_USER_PRINT_COMMAND("/ip/pool/used/print"),
    DHCP_SERVER_PRINT_COMMAND("/ip/dhcp-server/print"),
    DHCP_SERVER_LEASE_PRINT("/ip/dhcp-server/lease/print"),
    DHCP_CLIENT_PRINT_COMMAND("/ip/dhcp-client/print"),
    CALEA_ADD_ACTION_SRC_IP("/ip/firewall/calea/add action=sniff-pc chain=forward sniff-id=%s "+
             "sniff-target=%s sniff-target-port=%s src-address=%s"),
    CALEA_ADD_ACTION_DEST_IP("/ip/firewall/calea/add action=sniff-pc chain=forward sniff-id=%s "+
            "sniff-target=%s sniff-target-port=%s dst-address=%s"),

    CALEA_FIND_ACTION_SNIFF_ID("/ip/firewall/calea/find sniff-id=%s"),
    CALEA_FIND_ACTION_SRC_IP("/ip/firewall/calea/find action src-address=%s"),
    CALEA_FIND_ACTION_DST_IP("/ip/firewall/calea/find action dst-address=%s"),
    CALEA_FIND_ALL("/ip/firewall/calea/print"),
    CALEA_REMOVE_SNIFF_ID("/ip/firewall/calea/remove numbers=%s")
;
    private String command;

    MikrotikCommands(String commandName) {
        this.command = commandName;
    }

    public String command() {
        return command;
    }

    public String command(String... args) {
        return String.format(command, args);
    }
}


File: /src\main\java\mikrotik\example\MikrotikExampleApplication.java
package mikrotik.example;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

@SpringBootApplication
public class MikrotikExampleApplication {

	public static void main(String[] args) {
		SpringApplication.run(MikrotikExampleApplication.class, args);
	}
}


File: /src\main\java\mikrotik\example\runner\AbstractMikrotikRunner.java
package mikrotik.example.runner;

import java.io.IOException;
import java.net.InetAddress;
import java.net.Socket;
import java.net.UnknownHostException;
import java.util.LinkedList;
import java.util.List;
import java.util.Map;

import javax.net.SocketFactory;
import javax.net.ssl.SSLSocket;
import javax.net.ssl.SSLSocketFactory;

import org.springframework.beans.factory.annotation.Value;
import org.springframework.boot.CommandLineRunner;
import org.springframework.stereotype.Component;

import lombok.extern.slf4j.Slf4j;
import me.legrange.mikrotik.ApiConnection;
import me.legrange.mikrotik.MikrotikApiException;

@Component
@Slf4j
public abstract class AbstractMikrotikRunner implements CommandLineRunner {

    @Value("${mikrotik.management.ipaddress}")
    private String mikrotikIpAddress;

    @Value("${mikrotik.management.port:8728}")
    private int mikrotikPort;

    @Value("${mikrotik.management.tls.port:8729}")
    private int mikrotikTlsPort;

    @Value("${mikrotik.username}")
    private String mikrotikUsername;

    @Value("${mikrotik.password}")
    private String mikrotikPassword;

    protected ApiConnection connect() throws MikrotikApiException {
        ApiConnection apiConnection = ApiConnection.connect(mikrotikIpAddress);
        apiConnection.login(mikrotikUsername, mikrotikPassword);
        log.info("Connected using username: {}", mikrotikUsername);
        return apiConnection;
    }

    protected ApiConnection connectUsingAnnonTls() throws MikrotikApiException {
        ApiConnection apiConnection = ApiConnection.connect(AnonymousSocketFactory.getDefault(), mikrotikIpAddress, ApiConnection.DEFAULT_TLS_PORT, ApiConnection.DEFAULT_CONNECTION_TIMEOUT);
        apiConnection.login(mikrotikUsername, mikrotikPassword);
        log.info("=========================================================\nConnected over TLS using username: {}", mikrotikUsername);
        return apiConnection;
    }

    protected void printResultSet(List<Map<String, String>> rs) {
        for (Map<String, String> r : rs) {
            log.info("{}", r);
        }
    }

    static class AnonymousSocketFactory extends SocketFactory {

        @Override
        public Socket createSocket() throws IOException {
            return fixSocket((SSLSocket) SSLSocketFactory.getDefault().createSocket());
        }

        @Override
        public Socket createSocket(String host, int port) throws IOException, UnknownHostException {
            return fixSocket((SSLSocket) SSLSocketFactory.getDefault().createSocket(host, port));
        }

        @Override
        public Socket createSocket(String host, int port, InetAddress localHost, int localPort) throws IOException, UnknownHostException {
            return fixSocket((SSLSocket) SSLSocketFactory.getDefault().createSocket(host, port, localHost, localPort));
        }

        @Override
        public Socket createSocket(InetAddress address, int port) throws IOException {
            return fixSocket((SSLSocket) SSLSocketFactory.getDefault().createSocket(address, port));
        }

        @Override
        public Socket createSocket(InetAddress address, int port, InetAddress localAddress, int localPort) throws IOException {
            return fixSocket((SSLSocket) SSLSocketFactory.getDefault().createSocket(address, port, localAddress, localPort));
        }

        private Socket fixSocket(SSLSocket ssl) {
            List<String> cs = new LinkedList<>();
            // not happy with this code. Without it, SSL throws a "Remote host closed connection during handshake" error
            // caused by a "SSL peer shut down incorrectly" error
            for (String s : ssl.getSupportedCipherSuites()) {
                if (s.startsWith("TLS_DH_anon")) {
                    cs.add(s);
                }
            }
            ssl.setEnabledCipherSuites(cs.toArray(new String[]{}));
            return ssl;
        }

        public static SocketFactory getDefault() {
            if (fact == null) {
                fact = new AnonymousSocketFactory();
            }
            return fact;
        }

        private AnonymousSocketFactory() {

        }

        private static AnonymousSocketFactory fact;

    }

}


File: /src\main\java\mikrotik\example\runner\DpRelatedMikrotikCommandRunner.java
package mikrotik.example.runner;

import java.util.List;
import java.util.Map;

import org.springframework.core.annotation.Order;
import org.springframework.stereotype.Component;

import lombok.extern.slf4j.Slf4j;
import me.legrange.mikrotik.ApiConnection;
import me.legrange.mikrotik.MikrotikApiException;
import mikrotik.example.command.MikrotikCommands;

@Component
@Order(7)
@Slf4j
public class DpRelatedMikrotikCommandRunner extends AbstractMikrotikRunner {

    @Override
    public void run(String... args) throws Exception {
        try (ApiConnection apiConnection = connectUsingAnnonTls()) {
            log.info("Print the current DHCP lease table");
            List<Map<String,String>> rs = apiConnection.execute(MikrotikCommands.DHCP_SERVER_LEASE_PRINT.command());
            printResultSet(rs);

            log.info("Create a new sniff target for a source IP address");
            String command = MikrotikCommands.CALEA_ADD_ACTION_SRC_IP.command("1", "172.16.35.131", "22200", "10.10.10.10");
            log.info("Command: {}", command);
            printResultSet(apiConnection.execute(MikrotikCommands.CALEA_ADD_ACTION_SRC_IP.command("1", "172.16.35.131", "22200", "10.10.10.10")));

            log.info("Create a new sniff target for a destination IP address");
            printResultSet(apiConnection.execute(MikrotikCommands.CALEA_ADD_ACTION_DEST_IP.command("2", "172.16.35.131", "22200", "20.20.20.20")));

            log.info("Find all calea record with sniff id");
            List<Map<String, String>> resultSet = apiConnection.execute(MikrotikCommands.CALEA_FIND_ALL.command());
            int caleaRecords = resultSet.size();
            log.info("Number of calea records {}", caleaRecords);
            printResultSet(resultSet);

            log.info("Remove all calea records");
            String cmd = MikrotikCommands.CALEA_REMOVE_SNIFF_ID.command(generateSequence(resultSet.size()));
            log.info("Remove all command: {}", cmd);
            apiConnection.execute(cmd);

            log.info("Find all calea record with sniff id");
            resultSet = apiConnection.execute(MikrotikCommands.CALEA_FIND_ALL.command());
            caleaRecords = resultSet.size();
            log.info("Number of calea records {}", caleaRecords);
            printResultSet(resultSet);
        } finally {
            log.info("Finished executing DpRelatedMikrotikCommandRunner\n=========================================================\n");
        }

    }

    private String generateSequence(int maxNumber) {
        StringBuilder seqBuilder = new StringBuilder();
        for(int i = 0 ; i < maxNumber; i++) {
            seqBuilder.append(i);
            if (i < maxNumber -1)
                seqBuilder.append(",");
        }
        return seqBuilder.toString();
    }
}


File: /src\main\java\mikrotik\example\runner\MikrotikAnnonTlsLoginRunner.java
package mikrotik.example.runner;

import org.springframework.core.annotation.Order;
import org.springframework.stereotype.Component;

import lombok.extern.slf4j.Slf4j;
import me.legrange.mikrotik.ApiConnection;

@Component
@Order(6)
@Slf4j
public class MikrotikAnnonTlsLoginRunner extends AbstractMikrotikRunner {

    @Override
    public void run(String... args) throws Exception {

        try (ApiConnection apiConnection = connectUsingAnnonTls()) {
            log.info("Connected using anonymous tls connection");
        } finally {
            log.info("Finished executing MikrotikAnnonTlsLoginRunner\n=========================================================\n");
        }
    }
}


File: /src\main\java\mikrotik\example\runner\MikrotikDhcpServerCommandRunner.java
package mikrotik.example.runner;

import java.util.List;
import java.util.Map;

import org.springframework.core.annotation.Order;
import org.springframework.stereotype.Component;

import lombok.extern.slf4j.Slf4j;
import me.legrange.mikrotik.ApiConnection;
import mikrotik.example.command.MikrotikCommands;

@Component
@Order(4)
@Slf4j
public class MikrotikDhcpServerCommandRunner extends AbstractMikrotikRunner {
    @Override
    public void run(String... args) throws Exception {
        try (ApiConnection apiConnection = connectUsingAnnonTls()) {
            log.info("Get Mikrokit dhcp-server info");
            List<Map<String, String>> rs = apiConnection.execute(MikrotikCommands.DHCP_SERVER_PRINT_COMMAND.command());
            printResultSet(rs);

            log.info("Get Mikrotik dhcp-server lease info");
            printResultSet(apiConnection.execute(MikrotikCommands.DHCP_SERVER_LEASE_PRINT.command()));

            log.info("Get Mikrotik dhcp-client print");
            printResultSet(apiConnection.execute(MikrotikCommands.DHCP_CLIENT_PRINT_COMMAND.command()));
        } finally {
            log.info("Finished executing MikrotikDhcpServerCommandRunner\n=========================================================\n");
        }
    }
}


File: /src\main\java\mikrotik\example\runner\MikrotikInterfaceCommandRunner.java
package mikrotik.example.runner;

import java.util.List;
import java.util.Map;

import org.springframework.core.annotation.Order;
import org.springframework.stereotype.Component;

import lombok.extern.slf4j.Slf4j;
import me.legrange.mikrotik.ApiConnection;
import mikrotik.example.command.MikrotikCommands;

@Component
@Order(2)
@Slf4j
public class MikrotikInterfaceCommandRunner extends AbstractMikrotikRunner {

    @Override
    public void run(String... args) throws Exception {
        try (ApiConnection apiConnection = connectUsingAnnonTls()) {


            log.info("Get Mikrokit interface info");
            List<Map<String, String>> rs = apiConnection.execute(MikrotikCommands.INTERFACE_PRINT.command());
            printResultSet(rs);

            log.info("Get Mikrotik ethernet info");
            rs = apiConnection.execute(MikrotikCommands.INTERFACE_ETHERNET_PRINT.command());
            printResultSet(rs);

            log.info("Get Mikrokit ip address");
            rs = apiConnection.execute(MikrotikCommands.IP_ADDRESS_PRINT.command());
            printResultSet(rs);

            log.info("Get Mikrotik pppoe-server print");
            rs = apiConnection.execute(MikrotikCommands.INTERFACE_PPPOE_SERVER_PRINT_COMMAND.command());
            printResultSet(rs);

            log.info("Get Mikrotik pppoe-server server print");
            printResultSet(apiConnection.execute(MikrotikCommands.INTERFACE_PPPOE_SERVER_SERVER_PRINT_COMMAND.command()));

            log.info("Get Mikrotik pppoe-client print");
            printResultSet(apiConnection.execute(MikrotikCommands.INTERFACE_PPPOE_CLIENT_PRINT_COMMAND.command()));

            log.info("Get PPP profile print");
            printResultSet(apiConnection.execute(MikrotikCommands.PPP_PROFILE_PRINT.command()));

            log.info("Get PPP secret print");
            printResultSet(apiConnection.execute(MikrotikCommands.PPP_SECRET_PRINT.command()));
        } finally {
            log.info("Finished executing MikrotikInterfaceCommandRunner\n=========================================================\n");
        }
    }
}


File: /src\main\java\mikrotik\example\runner\MikrotikIpPoolCommandRunner.java
package mikrotik.example.runner;

import java.util.List;
import java.util.Map;

import org.springframework.core.annotation.Order;
import org.springframework.stereotype.Component;

import lombok.extern.slf4j.Slf4j;
import me.legrange.mikrotik.ApiConnection;
import mikrotik.example.command.MikrotikCommands;

@Component
@Order(3)
@Slf4j
public class MikrotikIpPoolCommandRunner extends AbstractMikrotikRunner {

    @Override
    public void run(String... args) throws Exception {
        try (ApiConnection apiConnection = connectUsingAnnonTls()) {
            log.info("Get Mikrokit ip pool info");
            List<Map<String, String>> rs = apiConnection.execute(MikrotikCommands.IP_POOL_PRINT_COMMAND.command());
            printResultSet(rs);

            log.info("Get Mikrokit used ip pool info");
            rs = apiConnection.execute(MikrotikCommands.IP_POOL_USER_PRINT_COMMAND.command());
            printResultSet(rs);
        } finally {
            log.info("Finished executing MikrotikIpPoolCommandRunner\n=========================================================\n");
        }
    }
}


File: /src\main\java\mikrotik\example\runner\MikrotikLoginRunner.java
package mikrotik.example.runner;

import org.springframework.core.annotation.Order;
import org.springframework.stereotype.Component;

import lombok.extern.slf4j.Slf4j;
import me.legrange.mikrotik.ApiConnection;

@Component
@Order(1)
@Slf4j
public class MikrotikLoginRunner extends AbstractMikrotikRunner {

    @Override
    public void run(String... args) throws Exception {
        try (ApiConnection apiConnection = connect()) {
            log.info("Connected to mikrotik over non-tls\n=========================================================\n");
        }
    }
}


File: /src\main\java\mikrotik\example\runner\MikrotikPppoeServerCommandRunner.java
package mikrotik.example.runner;

import java.util.List;
import java.util.Map;

import org.springframework.core.annotation.Order;
import org.springframework.stereotype.Component;

import lombok.extern.slf4j.Slf4j;
import me.legrange.mikrotik.ApiConnection;
import mikrotik.example.command.MikrotikCommands;

@Component
@Slf4j
@Order(5)
public class MikrotikPppoeServerCommandRunner extends AbstractMikrotikRunner {
    @Override
    public void run(String... args) throws Exception {
        try (ApiConnection apiConnection = connectUsingAnnonTls()) {
            log.info("Get Mikrokit pppoe-server info");
            List<Map<String, String>> rs = apiConnection.execute(MikrotikCommands.INTERFACE_PPPOE_SERVER_PRINT_COMMAND.command());
            printResultSet(rs);
        } finally {
            log.info("Finished executing MikrotikPppoeServerCommandRunner\n=========================================================\n");
        }
    }
}


File: /src\main\resources\application.properties
mikrotik.management.ipaddress=127.0.0.1
mikrotik.management.port=8728
mikrotik.management.tls.port=8729
#mikrotik.username=top_mgr_usr
mikrotik.username=dp_top_mgr_usr
mikrotik.password=password
logging.level.root=INFO, CONSOLE
logging.level.mikrokit.example=INFO
File: /src\test\java\mikrotik\example\MikrotikExampleApplicationTests.java
package mikrotik.example;

import org.junit.Test;
import org.junit.runner.RunWith;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.test.context.junit4.SpringRunner;

@RunWith(SpringRunner.class)
@SpringBootTest
public class MikrotikExampleApplicationTests {

	@Test
	public void contextLoads() {
	}

}


