# Repository Information
Name: mikrotik-java

# Directory Structure
Directory structure:
└── github_repos/mikrotik-java/
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
    │   │       ├── pack-fa1db1ed4382664b63c32a7744475da5ab8d037d.idx
    │   │       └── pack-fa1db1ed4382664b63c32a7744475da5ab8d037d.pack
    │   ├── packed-refs
    │   └── refs/
    │       ├── heads/
    │       │   └── master
    │       ├── remotes/
    │       │   └── origin/
    │       │       └── HEAD
    │       └── tags/
    ├── .github/
    │   └── workflows/
    │       └── maven.yml
    ├── .gitignore
    ├── .travis.yml
    ├── CONTRIBUTING.md
    ├── LICENCE.md
    ├── pom.xml
    ├── README.md
    └── src/
        └── main/
            └── java/
                ├── examples/
                │   ├── AddAndModify.java
                │   ├── AnonymousSocketFactory.java
                │   ├── AsyncCommand.java
                │   ├── AsyncWithErrorHandling.java
                │   ├── CharacterSets.java
                │   ├── CommandWithWhere.java
                │   ├── Config.java
                │   ├── ConnectTLSAnonymous.java
                │   ├── ConnectTLSCertificate.java
                │   ├── DownloadConfig.java
                │   ├── Example.java
                │   ├── NestedExpressions.java
                │   ├── ScriptCommand.java
                │   ├── SimpleCommand.java
                │   ├── SimpleCommandWithResults.java
                │   └── TryWithResources.java
                └── me/
                    └── legrange/
                        └── mikrotik/
                            ├── ApiConnection.java
                            ├── ApiConnectionException.java
                            ├── grammar.txt
                            ├── impl/
                            │   ├── ApiCommandException.java
                            │   ├── ApiConnectionImpl.java
                            │   ├── ApiDataException.java
                            │   ├── Command.java
                            │   ├── Done.java
                            │   ├── Error.java
                            │   ├── Parameter.java
                            │   ├── ParseException.java
                            │   ├── Parser.java
                            │   ├── Response.java
                            │   ├── Result.java
                            │   ├── ScanException.java
                            │   ├── Scanner.java
                            │   └── Util.java
                            ├── MikrotikApiException.java
                            └── ResultListener.java


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
	url = https://github.com/GideonLeGrange/mikrotik-java.git
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
0000000000000000000000000000000000000000 ec5f6650816e5e63a00fbb0ae3aa511493df3a65 vivek-dodia <vivek.dodia@icloud.com> 1738605789 -0500	clone: from https://github.com/GideonLeGrange/mikrotik-java.git


File: /.git\logs\refs\heads\master
0000000000000000000000000000000000000000 ec5f6650816e5e63a00fbb0ae3aa511493df3a65 vivek-dodia <vivek.dodia@icloud.com> 1738605789 -0500	clone: from https://github.com/GideonLeGrange/mikrotik-java.git


File: /.git\logs\refs\remotes\origin\HEAD
0000000000000000000000000000000000000000 ec5f6650816e5e63a00fbb0ae3aa511493df3a65 vivek-dodia <vivek.dodia@icloud.com> 1738605789 -0500	clone: from https://github.com/GideonLeGrange/mikrotik-java.git


File: /.git\packed-refs
# pack-refs with: peeled fully-peeled sorted 
4c2f69a60998185340617726a776d61188440c6d refs/remotes/origin/issue-55
ec5f6650816e5e63a00fbb0ae3aa511493df3a65 refs/remotes/origin/master
74c77bf4d840bff4b986d9c8c44a7c4fe85f3c37 refs/tags/1.1.1
2e074e5c535f4fe3e71ac0edaf9c96e35cbc3fff refs/tags/1.1.2
a115355d2273c7faf63129373b8c8d35cbf2272d refs/tags/1.1.3
160b7f51526d66ab122242561a0f162ac83e0303 refs/tags/1.1.4
267cb151f7a112bef18227ce0bff96516b10c2c9 refs/tags/1.1.5
70db71c8cc1801a3208a480c74bbe4c5e7ef6c72 refs/tags/2.0.0
4af6339ae13afef46b9d634414b2853ce27ab35b refs/tags/2.0.1
adaca0413e00f6e8bbdf7e16a9034262507e54cd refs/tags/2.0.2
0408db9b614dc21221cf9e74a72834752bdf9de9 refs/tags/2.0.3
5c2d3a9e50d80893235bfcd20ed6ecfe6341d254 refs/tags/mikrotik-1.1.6
^b89a91084a272f2546f6aff6e3ca968b0f4597a8
aefec5ea61908c089d0a35c03cc45e18410252ee refs/tags/mikrotik-java-1.0
^e4f651b5b5e936f46c0c602f857b2c493897036d
2148dea982fb908fc2bfa7ba6256b6cfec6e476d refs/tags/v1.1
69633f3390145af04b6a218e38f57ec23f4e05a6 refs/tags/v2.1
56d10d6937b6b9902b787489972077c4b04516b2 refs/tags/v2.2
c0e97f81380f9d08734eff87b63e7f059d10b7cd refs/tags/v3.0
30906dc2a9607164e6c7c88ea08e39cce7e68ac0 refs/tags/v3.0.1
a2437f1afe56c0958732ea23b151015a71404e86 refs/tags/v3.0.2
56bd38672e450341c949cd368c71bce98e5c5802 refs/tags/v3.0.3
6d9141a6d2b601415bcd635877f62fda02240d72 refs/tags/v3.0.4
af9fc52336c14707950905d03b73eca241fdebc6 refs/tags/v3.0.5
7aac1b95e28130ed572ee225b9ce46dcb016f1ea refs/tags/v3.0.6
283b3f68ef5395d62fc72062cfe90541280c0212 refs/tags/v3.0.7


File: /.git\refs\heads\master
ec5f6650816e5e63a00fbb0ae3aa511493df3a65


File: /.git\refs\remotes\origin\HEAD
ref: refs/remotes/origin/master


File: /.github\workflows\maven.yml
# This workflow will build a Java project with Maven
# For more information see: https://help.github.com/actions/language-and-framework-guides/building-and-testing-java-with-maven

name: Java CI with Maven

on:
  push:
    branches: [ master ]
  pull_request:
    branches: [ master ]

jobs:
  build:

    runs-on: ubuntu-latest

    steps:
    - uses: actions/checkout@v2
    - name: Set up JDK 1.8
      uses: actions/setup-java@v1
      with:
        java-version: 1.8
    - name: Build with Maven
      run: mvn -B package --file pom.xml


File: /.gitignore

# Maven 
target/

# Netbeans
build/
dist/
#nbproject/
nb-configuration.xml
nbactions.xml

# IntelliJ
File: /.travis.yml
language: java


File: /CONTRIBUTING.md
Thank you for considering contributing to this project. This library is one tiny way I am giving back to the open source community, and I am
always amazed and humbled when users contribute back. 

There are several ways of contributing to this small open source library:

* You can ask for help
* You can log a bug
* You can contribute code

# Ask for help
If you experience a problem using the mikrotik-java library, the best way to get in touch with me is to either send me an
email or open an issue on GitHub. While you can seek help on StackOverflow or the Mikrotik Forums (both of which I've seen 
people do), I do not read those sites often. If you wish to log your question there (it makes sense for it to be searchable or 
in a place where other interested people can find it) and want me to take a look at it, please send me an email pointing to 
the question. 

I find that it is very easy to help users of this library if they include the following things which are usually quite relevant:

* A snipped of sample code showing what they're doing 
* The stack trace (if there is one) when it goes wrong
* Version of the library they're using

# Log a bug 
If you are pretty sure you have found a bug in the library, please log a bug by opening an issue on GithHub. When things get buggy, 
the following information (mostly the same as for asking help) becomes important:

* A snipped of sample code showing what they're doing 
* The stack trace (if there is one) when it goes wrong
* Version of the library they're using
* The version of RouterOS they're connecting to

I take bug reports very seriously, and will usually bring out immediate minor versions to fix show stoppers. 

# Contribute code 
If you want to contribute code to this library, you're welcome. Please read this section before submitting pull requests.

## If you're fixing a bug
If you've fixed a bug, please submit the pull request on GitHub. If there is an already existing issue being fixed, please 
reference that issue so I can look at what you're fixing, and if not, please explain the issue you're fixing in the pull request. 

## If you want new functionality or API changes
Please contact me via email before you create a pull request for feature additions or API changes. The mikrotik-java library is stable and,
for it's current purpose, feature complete. The situations in which I will add features to the library or change it's interface are:
* If Mikrotik adds new RouterOS functionality that requires an API change to remain feature complete
* If some very bad design flaw in the interface is discovered
* If somebody has a truly compelling reason for adding to the library. To be compelling means the added functionality must be useful 
for more users than just the submitter
* If some new pattern or convention arises in the Java standard libraries that is useful 

I *really* hate declining people's PRs, but I will do so if I don't think they add value as explained above, or if I can't figure out why
they want the change. For this reason, if you are at all unsure if your PR will be accepted, please contact me and discuss what you want 
before submitting a PR. 

Gideon 


File: /LICENCE.md
Apache License
Version 2.0, January 2004
http://www.apache.org/licenses/

TERMS AND CONDITIONS FOR USE, REPRODUCTION, AND DISTRIBUTION

1. Definitions.

"License" shall mean the terms and conditions for use, reproduction, and
distribution as defined by Sections 1 through 9 of this document.

"Licensor" shall mean the copyright owner or entity authorized by the copyright
owner that is granting the License.

"Legal Entity" shall mean the union of the acting entity and all other entities
that control, are controlled by, or are under common control with that entity.
For the purposes of this definition, "control" means (i) the power, direct or
indirect, to cause the direction or management of such entity, whether by
contract or otherwise, or (ii) ownership of fifty percent (50%) or more of the
outstanding shares, or (iii) beneficial ownership of such entity.

"You" (or "Your") shall mean an individual or Legal Entity exercising
permissions granted by this License.

"Source" form shall mean the preferred form for making modifications, including
but not limited to software source code, documentation source, and configuration
files.

"Object" form shall mean any form resulting from mechanical transformation or
translation of a Source form, including but not limited to compiled object code,
generated documentation, and conversions to other media types.

"Work" shall mean the work of authorship, whether in Source or Object form, made
available under the License, as indicated by a copyright notice that is included
in or attached to the work (an example is provided in the Appendix below).

"Derivative Works" shall mean any work, whether in Source or Object form, that
is based on (or derived from) the Work and for which the editorial revisions,
annotations, elaborations, or other modifications represent, as a whole, an
original work of authorship. For the purposes of this License, Derivative Works
shall not include works that remain separable from, or merely link (or bind by
name) to the interfaces of, the Work and Derivative Works thereof.

"Contribution" shall mean any work of authorship, including the original version
of the Work and any modifications or additions to that Work or Derivative Works
thereof, that is intentionally submitted to Licensor for inclusion in the Work
by the copyright owner or by an individual or Legal Entity authorized to submit
on behalf of the copyright owner. For the purposes of this definition,
"submitted" means any form of electronic, verbal, or written communication sent
to the Licensor or its representatives, including but not limited to
communication on electronic mailing lists, source code control systems, and
issue tracking systems that are managed by, or on behalf of, the Licensor for
the purpose of discussing and improving the Work, but excluding communication
that is conspicuously marked or otherwise designated in writing by the copyright
owner as "Not a Contribution."

"Contributor" shall mean Licensor and any individual or Legal Entity on behalf
of whom a Contribution has been received by Licensor and subsequently
incorporated within the Work.

2. Grant of Copyright License.

Subject to the terms and conditions of this License, each Contributor hereby
grants to You a perpetual, worldwide, non-exclusive, no-charge, royalty-free,
irrevocable copyright license to reproduce, prepare Derivative Works of,
publicly display, publicly perform, sublicense, and distribute the Work and such
Derivative Works in Source or Object form.

3. Grant of Patent License.

Subject to the terms and conditions of this License, each Contributor hereby
grants to You a perpetual, worldwide, non-exclusive, no-charge, royalty-free,
irrevocable (except as stated in this section) patent license to make, have
made, use, offer to sell, sell, import, and otherwise transfer the Work, where
such license applies only to those patent claims licensable by such Contributor
that are necessarily infringed by their Contribution(s) alone or by combination
of their Contribution(s) with the Work to which such Contribution(s) was
submitted. If You institute patent litigation against any entity (including a
cross-claim or counterclaim in a lawsuit) alleging that the Work or a
Contribution incorporated within the Work constitutes direct or contributory
patent infringement, then any patent licenses granted to You under this License
for that Work shall terminate as of the date such litigation is filed.

4. Redistribution.

You may reproduce and distribute copies of the Work or Derivative Works thereof
in any medium, with or without modifications, and in Source or Object form,
provided that You meet the following conditions:

You must give any other recipients of the Work or Derivative Works a copy of
this License; and
You must cause any modified files to carry prominent notices stating that You
changed the files; and
You must retain, in the Source form of any Derivative Works that You distribute,
all copyright, patent, trademark, and attribution notices from the Source form
of the Work, excluding those notices that do not pertain to any part of the
Derivative Works; and
If the Work includes a "NOTICE" text file as part of its distribution, then any
Derivative Works that You distribute must include a readable copy of the
attribution notices contained within such NOTICE file, excluding those notices
that do not pertain to any part of the Derivative Works, in at least one of the
following places: within a NOTICE text file distributed as part of the
Derivative Works; within the Source form or documentation, if provided along
with the Derivative Works; or, within a display generated by the Derivative
Works, if and wherever such third-party notices normally appear. The contents of
the NOTICE file are for informational purposes only and do not modify the
License. You may add Your own attribution notices within Derivative Works that
You distribute, alongside or as an addendum to the NOTICE text from the Work,
provided that such additional attribution notices cannot be construed as
modifying the License.
You may add Your own copyright statement to Your modifications and may provide
additional or different license terms and conditions for use, reproduction, or
distribution of Your modifications, or for any such Derivative Works as a whole,
provided Your use, reproduction, and distribution of the Work otherwise complies
with the conditions stated in this License.

5. Submission of Contributions.

Unless You explicitly state otherwise, any Contribution intentionally submitted
for inclusion in the Work by You to the Licensor shall be under the terms and
conditions of this License, without any additional terms or conditions.
Notwithstanding the above, nothing herein shall supersede or modify the terms of
any separate license agreement you may have executed with Licensor regarding
such Contributions.

6. Trademarks.

This License does not grant permission to use the trade names, trademarks,
service marks, or product names of the Licensor, except as required for
reasonable and customary use in describing the origin of the Work and
reproducing the content of the NOTICE file.

7. Disclaimer of Warranty.

Unless required by applicable law or agreed to in writing, Licensor provides the
Work (and each Contributor provides its Contributions) on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied,
including, without limitation, any warranties or conditions of TITLE,
NON-INFRINGEMENT, MERCHANTABILITY, or FITNESS FOR A PARTICULAR PURPOSE. You are
solely responsible for determining the appropriateness of using or
redistributing the Work and assume any risks associated with Your exercise of
permissions under this License.

8. Limitation of Liability.

In no event and under no legal theory, whether in tort (including negligence),
contract, or otherwise, unless required by applicable law (such as deliberate
and grossly negligent acts) or agreed to in writing, shall any Contributor be
liable to You for damages, including any direct, indirect, special, incidental,
or consequential damages of any character arising as a result of this License or
out of the use or inability to use the Work (including but not limited to
damages for loss of goodwill, work stoppage, computer failure or malfunction, or
any and all other commercial damages or losses), even if such Contributor has
been advised of the possibility of such damages.

9. Accepting Warranty or Additional Liability.

While redistributing the Work or Derivative Works thereof, You may choose to
offer, and charge a fee for, acceptance of support, warranty, indemnity, or
other liability obligations and/or rights consistent with this License. However,
in accepting such obligations, You may act only on Your own behalf and on Your
sole responsibility, not on behalf of any other Contributor, and only if You
agree to indemnify, defend, and hold each Contributor harmless for any liability
incurred by, or claims asserted against, such Contributor by reason of your
accepting any such warranty or additional liability.

END OF TERMS AND CONDITIONS




File: /pom.xml
<?xml version="1.0" encoding="UTF-8"?>

<project xmlns="http://maven.apache.org/POM/4.0.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">  
  <parent> 
    <groupId>org.sonatype.oss</groupId>  
    <artifactId>oss-parent</artifactId>  
    <version>9</version> 
  </parent>  
  <modelVersion>4.0.0</modelVersion>  
  <groupId>me.legrange</groupId>  
  <artifactId>mikrotik</artifactId>  
  <version>3.0.8</version>  
  <packaging>jar</packaging>  
  <name>Mikrotik API Java Client Library</name>  
  <url>https://github.com/GideonLeGrange/mikrotik-java</url>  
  <licenses> 
    <license> 
      <name>The Apache Software License, Version 2.0</name>  
      <url>http://www.apache.org/licenses/LICENSE-2.0.txt</url>  
      <distribution>repo</distribution> 
    </license> 
  </licenses>  
  <scm> 
    <url>git@github.com:GideonLeGrange/mikrotik-java.git</url>  
    <connection>scm:git:git@github.com:GideonLeGrange/mikrotik-java.git</connection>  
    <developerConnection>scm:git:git@github.com:GideonLeGrange/mikrotik-java.git</developerConnection> 
  </scm>  
  <build> 
    <plugins> 
      <plugin> 
        <groupId>org.apache.maven.plugins</groupId>  
        <artifactId>maven-compiler-plugin</artifactId>  
        <version>2.3.2</version>  
        <configuration> 
          <showDeprecation>true</showDeprecation>  
          <source>1.7</source>  
          <target>1.7</target> 
        </configuration> 
      </plugin>  
      <plugin> 
        <groupId>org.apache.maven.plugins</groupId>  
        <artifactId>maven-jar-plugin</artifactId>  
        <version>2.3.2</version>  
        <executions> 
          <execution> 
            <id>default-jar</id>  
            <phase>package</phase>  
            <goals> 
              <goal>jar</goal> 
            </goals>  
            <configuration> 
              <excludes> 
                <exclude>**/examples</exclude>  
                <exclude>**/examples/*</exclude> 
              </excludes> 
            </configuration> 
          </execution> 
        </executions> 
      </plugin>  
      <plugin> 
        <groupId>org.apache.maven.plugins</groupId>  
        <artifactId>maven-source-plugin</artifactId>  
        <version>2.2.1</version>  
        <executions> 
          <execution> 
            <id>attach-sources</id>  
            <goals> 
              <goal>jar</goal> 
            </goals> 
          </execution> 
        </executions> 
      </plugin>  
      <plugin> 
        <groupId>org.apache.maven.plugins</groupId>  
        <artifactId>maven-javadoc-plugin</artifactId>  
        <version>2.9.1</version>  
        <configuration> 
          <excludePackageNames>example;*.impl</excludePackageNames> 
        </configuration>  
        <executions> 
          <execution> 
            <id>attach-javadocs</id>  
            <goals> 
              <goal>jar</goal> 
            </goals> 
          </execution> 
        </executions> 
      </plugin>  
   </plugins> 
  </build>  
  <profiles> 
    <profile> 
      <id>release</id>  
      <build> 
        <plugins> 
          <plugin> 
            <groupId>org.apache.maven.plugins</groupId>  
            <artifactId>maven-source-plugin</artifactId>  
            <version>2.4</version>  
            <executions> 
              <execution> 
                <id>attach-sources</id>  
                <goals> 
                  <goal>jar</goal> 
                </goals> 
              </execution> 
            </executions> 
          </plugin>  
          <plugin> 
            <groupId>org.apache.maven.plugins</groupId>  
            <artifactId>maven-javadoc-plugin</artifactId>  
            <version>2.10.1</version>  
            <executions> 
              <execution> 
                <id>attach-javadocs</id>  
                <goals> 
                  <goal>jar</goal> 
                </goals> 
              </execution> 
            </executions> 
          </plugin>  
          <plugin> 
            <groupId>org.apache.maven.plugins</groupId>  
            <artifactId>maven-gpg-plugin</artifactId>  
            <version>1.6</version>  
            <executions> 
              <execution> 
                <id>sign-artifacts</id>  
                <phase>verify</phase>  
                <goals> 
                  <goal>sign</goal> 
                </goals> 
              </execution> 
            </executions> 
          </plugin>  
          <plugin> 
            <groupId>org.sonatype.plugins</groupId>  
            <artifactId>nexus-staging-maven-plugin</artifactId>  
            <version>1.6.5</version>  
            <extensions>true</extensions>  
            <configuration> 
              <serverId>ossrh</serverId>  
              <nexusUrl>https://oss.sonatype.org/</nexusUrl>  
              <autoReleaseAfterClose>true</autoReleaseAfterClose> 
            </configuration> 
          </plugin> 
        </plugins> 
      </build>  
      <distributionManagement> 
        <snapshotRepository> 
          <id>ossrh</id>  
          <url>https://oss.sonatype.org/content/repositories/snapshots</url> 
        </snapshotRepository> 
      </distributionManagement> 
    </profile> 
  </profiles>  
  <properties> 
    <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding> 
  </properties>  
  <dependencies> 
    <dependency> 
      <groupId>junit</groupId>  
      <artifactId>junit</artifactId>  
      <version>4.13.1</version>  
      <scope>test</scope> 
    </dependency>  
  </dependencies> 
</project>


File: /README.md
# mikrotik-java 

A Java client library implementation for the Mikrotik RouterOS API. 

This project provides a Java client to manipulate Mikrotik routers using the remote API. Simple things must be easy to do, and complex things must be possible.

## Versions

![Java CI with Maven](https://github.com/GideonLeGrange/mikrotik-java/workflows/Java%20CI%20with%20Maven/badge.svg)

**The current stable version is 3.0.8**

Version 3.0.8 fixes a null pointer error 

### Changes in version 3.0:

Version 3.0 addresses the problems the API had around TLS encryption. The way secure connections are implemented is changed so that the user has complete control over the creation of TLS sockets. To this end:
* A new method, `connect(SocketFactory fact, String host, int port, int timeout)`, was added to allow for better user control over sockets and especially encryption.
* The `connectTLS()` API methods were removed. 
* Most of the overloaded `connect()` methods were removed. 
* Added a pre-built `jar` file to the downloads.

Further changes include:
* The previously deprecated `disconnect()` method is removed. 

#### Versions 1.x and 2.x

Versions 1 and 2 are considered *obsolete* and will no longer be supported or patched. 

## Getting the API

Maven users can use the artifact from Maven Central with this dependency:

```xml
<dependency>
  <groupId>me.legrange</groupId>
  <artifactId>mikrotik</artifactId>
  <version>3.0.8</version>
</dependency>
```

You can also download the pre-built jar file, or a zip or tar.gz file with the source for the latest release [here](https://github.com/GideonLeGrange/mikrotik-java/releases/latest)

## Asking for help or contributing

I welcome contributions, be it bug fixes or other improvements. 

Please read [CONTRIBUTING.md](CONTRIBUTING.md) for information on how to contribute to this project.

# Using the API

How to use the API is best illustrated by examples. 

These examples should illustrate how to use this library. Please note that I assume that the user is proficient in Java and understands the Mikrotik command line syntax. The command line syntax gives you an indication of what commands you can pass, but the RouterOS API used by this library does not support everyting. 

Some things to consider when debugging your API calls are:
* The RouterOS API does not support auto-completion. You need to write out command and parameter names. For example, you can't say `/ip/hotspot/user/add name=john add=10.0.0.1`, you need to write out `address`.
* You need to quote values with spaces in. You can't say `name=Joe Blogs`, you need to use `name="Joe Blogs"`
* Exceptions with a root cause of `ApiCommandException` are errors received from the remote RouterOS device and contain the error message received. 

## Opening a connection
Here is a simple example: Connect to a router and reboot it. 

```java
ApiConnection con = ApiConnection.connect("10.0.1.1"); // connect to router
con.login("admin","password"); // log in to router
con.execute("/system/reboot"); // execute a command
con.close(); // disconnect from router
```
The above example shows a easy way of creating an unencrypted connection using the default API port and timeout, which is useful for development and testing.

### TLS encryption

For production environments, encrypting API traffic is recommended. To do this you need to open a TLS connection to the router by passing an instance of the `SocketFactory` you wish to use to construct the TLS socket to the API:

```java
ApiConnection con = ApiConnection.connect(SSLSocketFactory.getDefault(), "10.0.1.1", ApiConnection.DEFAULT_TLS_PORT, ApiConnection.DEFAULT_CONNECTION_TIMEOUT);
```

Above an instance of the default SSL socket factory is passed to the API. This will work as long as the router's certificate has been added to the local key store.  Besides allowing the user to specify the socket factory, the above method also gives full control over the TCP Port and connection timeout. 

RouterOS also supports anonymous TLS. An example showing how to create a socket factory for anonymous TLS is `AnonymousSocketFactory` in the examples directory.

### Connection timeouts

By default, the API will generate an exception if it cannot connect to the specified router. This can take place immediately (typically if the OS returns a 'Connection refused' error), but can also take up to 60 seconds if the router host is firewalled or if there are other network problems. This 60 seconds is the 'default connection timeout' an can be overridded by passing the preferred timeout to the APi as last parameter in a ```connect()``` call. For example:

```java
   ApiConnection con = ApiConnection.connect(SSLSocketFactory.getDefault(), "10.0.1.1", ApiConnection.DEFAULT_TLS_PORT, 2000); // connect to router on the default API port and fail in 2 seconds
```	

### Constants
Some constants are provided in `ApiConnection` to make it easier for users to construct connections with default ports and timeouts:

Constant | Use for | Value 
---------|---------|------
DEFAULT_PORT | Default TCP `port` value for unencrypyted connections | 8728
DEFAULT_TLS_PORT | Default TCP `port` value for encrypyted connections | 8729
DEFAULT_CONNECTION_TIMEOUT | Default connection `timeout` value (ms) | 60000

### Try with resources 

The API can also be used in a "try with resources" statement which will ensure that the connection is closed:

```java
        try (ApiConnection con = ApiConnection.connect(SocketFactory.getDefault(), Config.HOST, ApiConnection.DEFAULT_PORT, 2000)) {
            con.login(Config.USERNAME, Config.PASSWORD);
            con.execute("/user/add name=eric");
        }
```

In following examples the connection, login and disconnection code will not be repeated. In all cases it is assumed that an `ApiConnection` has been established, `login()` has been called, and that the connection is called `con`.

## Reading data 

A simple example that returns a result - Print all interfaces:


```java
List<Map<String, String>> rs = con.execute("/interface/print");
for (Map<String,String> r : rs) {
  System.out.println(r);
}
```

Results are returned as a list of maps of String key/value pairs. The reason for this is that a command can return multiple results, which have multpile variables. For example, to print the names of all the interfaces returned in the command above, do:

```java
for (Map<String, String> map : rs) { 
  System.out.println(map.get("name"));
}
```

### Filtering results

The same query, but with the results filtered: Print all interfaces of type 'vlan'.

```java
List<Map<String, String>> rs = con.execute("/interface/print where type=vlan");
```

### Selecting returned fields

The same query, but we only want certain result fields names: Print all interfaces of type 'vlan' and return just their name:

```java
List<Map<String, String>> rs = con.execute("/interface/print where type=vlan return name");
```

## Writing data 

Creating, modifying and deleting configuration objects is of course possible.

### Creating an object 

This example shows how to create a new GRE interface: 

```java
con.execute("/interface/gre/add remote-address=192.168.1.1 name=gre1 keepalive=10");
```

### Modify an existing object

Change the IP address in the object created by the above example:

```java
con.execute("/interface/gre/set .id=gre1 remote-address=10.0.1.1"); 
```

### Remove an existing object

And now remove the object:

```java
con.execute("/interface/gre/remove .id=gre1"); 
```

### Un-setting a variable on an object 

Un-setting a variable is a bit different, and you need to use a parameter called `value-name`. This isn't well documented. Let's say you have a firewall rule that was set up like this:

```java
con.execute("/ip/firewall/filter/add action=accept chain=forward time=00:00:01-01,mon")
```
Assuming the rule can be accessed as `.id=*1`, you un-set it by using `value-name` as seen below:

```java 
con.execute("/ip/firewall/filter/unset .id=*1 value-name=time");
```

## Asynchronous commands

We can run some commands asynchronously in order to continue receiving updates:

This example shows how to run '/interface wireless monitor' and have the result sent to a listener object, which prints it:

```java
String tag = con.execute("/interface/wireless/monitor .id=wlan1 return signal-to-noise", 
      new ResultListener() {

            public void receive(Map<String, String> result) {
                System.out.println(result);
            }

           public void error(MikrotikApiException e) {
               System.out.println("An error occurred: " + e.getMessage());
           }

           public void completed() {
                System.out.println("Asynchronous command has finished"); 
           }
            
        }
  );
```

The `ResultListener` interface has three methods the user needs to implement:
* `receive()` is called to receive results produced by the router from the API. 
* `error()` is called when an exception is raised based on a 'trap' received from the router or another (typically connection) problem.
* `completed()` is called when the router has indicated that the command has completed or has been cancelled. 

The above command will run and send results asynchronously as they become available, until it is canceled. The command (identified by the unique String returned) is canceled like this:

```java
con.cancel(tag);
```

## Command timeouts

Command timeouts can be used to make sure that synchronous commands either return or fail within a specific time. Command timeouts are separate from the connection timeout used in ```connect()```, and can be set using ```setTimeout()```. Here is an example:

```java
ApiConnection con = ApiConnection.connect("10.0.1.1"); // connect to router
con.setTimeout(5000); // set command timeout to 5 seconds
con.login("admin","password"); // log in to router
con.execute("/system/reboot"); // execute a command
``` 
 	
It is important to note that command timeouts can be set before ```login()``` is called, and can therefore influence the behaviour of login. 

The default command timeout, if none is set by the user, is 60 seconds. 

# References

The RouterOS API is documented here: http://wiki.mikrotik.com/wiki/Manual:API

# Licence

This library is released under the Apache 2.0 licence. See the [LICENCE.md](LICENCE.md) file



File: /src\main\java\examples\AddAndModify.java
package examples;

import me.legrange.mikrotik.MikrotikApiException;

/**
 * Example 6: Create and modify object
 *
 * @author gideon
 */
public class AddAndModify extends Example {

    public static void main(String... args) throws Exception {
        AddAndModify ex = new AddAndModify();
        ex.connect();
        ex.test();
        ex.disconnect();
    }

    private void test() throws MikrotikApiException, InterruptedException {
        System.out.println("Creating interface gre1");
        con.execute("/interface/gre/add remote-address=1.2.3.4 name=gre1 keepalive=10 comment='test comment'");
        System.out.println("Adding firewall rule for interface gre1");
        con.execute("/ip/firewall/filter/add action=drop chain=forward in-interface=gre1 protocol=udp dst-port=78,80");//,80,32");
        System.out.println("Waiting 10 seconds");
        Thread.sleep(10000); // 10 seconds for the user to look on the router to see the interface with /interface gre print
        System.out.println("Changing IP for interface gre1");
        con.execute("/interface/gre/set remote-address=172.16.1.1 .id=gre1");
        // now look again and the IP has changed
    }
}


File: /src\main\java\examples\AnonymousSocketFactory.java
/*
 * Copyright 2016 gideon.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *      http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */
package examples;

import java.io.IOException;
import java.net.InetAddress;
import java.net.Socket;
import java.net.UnknownHostException;
import java.util.LinkedList;
import java.util.List;
import javax.net.SocketFactory;
import javax.net.ssl.SSLSocket;
import javax.net.ssl.SSLSocketFactory;

/**
 *
 * @since 3.0
 * @author Gideon le Grange https://github.com/GideonLeGrange
 */
public class AnonymousSocketFactory extends SocketFactory {

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


File: /src\main\java\examples\AsyncCommand.java
package examples;

import java.util.Map;
import me.legrange.mikrotik.MikrotikApiException;
import me.legrange.mikrotik.ResultListener;

/**
 * Example 4: Asynchronous results. Run a command and receive results for it asynchronously with a ResultListener
 *
 * @author gideon
 */
public class AsyncCommand extends Example {

    public static void main(String... args) throws Exception {
        AsyncCommand ex = new AsyncCommand();
        ex.connect();
        ex.test();
        ex.disconnect();
    }

    private void test() throws MikrotikApiException, InterruptedException {
       String id = con.execute("/interface/wireless/monitor .id=wlan1 .proplist=signal-strength", new ResultListener() {
           private int prev = 0;

           public void receive(Map<String, String> result) {
               System.out.println(result);
/*               int val = Integer.parseInt(result.get("signal-strength"));
               String sym = (val == prev) ? " " : ((val < prev) ? "-" : "+");
               System.out.printf("%d %s\n", val, sym);
               prev = val;
  */          }

           @Override
           public void error(MikrotikApiException ex) {
               throw new RuntimeException(ex.getMessage(), ex);
           }

           @Override
           public void completed() {
           }


        });
       // let it run for 60 seconds 
       Thread.sleep(60000);
       con.cancel(id);
    }
}


File: /src\main\java\examples\AsyncWithErrorHandling.java
package examples;

import java.util.Map;
import me.legrange.mikrotik.MikrotikApiException;
import me.legrange.mikrotik.ResultListener;

/**
 * Example 5: Asynchronous results, with error and completion. Run a command and receive results, errors and completion notification for it asynchronously with a ResponseListener
 *
 * @author gideon
 */
public class AsyncWithErrorHandling extends Example {

    public static void main(String... args) throws Exception {
        AsyncWithErrorHandling ex = new AsyncWithErrorHandling();
        ex.connect();
        ex.test();
        ex.disconnect();
    }

    private void test() throws MikrotikApiException, InterruptedException {
        boolean completed = false;
       String id = con.execute("/interface/wireless/monitor .id=wlan1", new ResultListener() {
           private int prev = 0;

           @Override
           public void receive(Map<String, String> result) {
               int val = Integer.parseInt(result.get("signal-strength"));
               String sym = (val == prev) ? " " : ((val < prev) ? "-" : "+");
               System.out.printf("%d %s\n", val, sym);
               prev = val;
           }

           @Override
           public void error(MikrotikApiException ex) {
               System.out.printf("An error ocurred: %s\n", ex.getMessage());
               ex.printStackTrace();
           }

           @Override
           public void completed() {
               System.out.printf("The request has been completed\n");
           }


        });
       // let it run for 60 seconds 
       Thread.sleep(10000);
       con.cancel(id);
       Thread.sleep(2000);
    }
}


File: /src\main\java\examples\CharacterSets.java
package examples;

import java.util.List;
import java.util.Map;
import me.legrange.mikrotik.MikrotikApiException;

/**
 * Example to show that different character sets may work some times. 
 *
 * @author gideon
 */
public class CharacterSets extends Example {
    
    private static final String JAPANESE = "事報ハヤ久送とゅ歳用ト候新放すルドう二5春園ユヲロ然納レ部悲と被状クヘ芸一ーあぽだ野健い産隊ず";
    private static final String CRYLLIC = "Лорем ипсум долор сит амет, легере елояуентиам хис ид. Елигенди нолуиссе вих ут. Нихил";
    private static final String ARABIC = "تجهيز والمانيا تم قام. وحتّى المتاخمة ما وقد. أسر أمدها تكبّد عل. فقد بسبب ترتيب استدعى أم, مما مع غرّة، لأداء. الشتاء، عسكرياً";

    public static void main(String... args) throws Exception {
        CharacterSets ex = new CharacterSets();
        ex.connect();
        ex.test();
        ex.disconnect();
    }

    private void test() throws MikrotikApiException {
        con.execute("/ip/hotspot/user/add name=userJ comment='" + JAPANESE + "'");
        con.execute("/ip/hotspot/user/add name=userC comment='" + CRYLLIC + "'");
        con.execute("/ip/hotspot/user/add name=userA comment='" + ARABIC + "'");

        for (Map<String, String> res : con.execute("/ip/hotspot/user/print return name,comment")) {
            System.out.printf("%s : %s\n", res.get("name"), res.get("comment"));
        }
    }
}


File: /src\main\java\examples\CommandWithWhere.java
package examples;

import java.util.List;
import java.util.Map;
import me.legrange.mikrotik.MikrotikApiException;

/**
 * Example 3: Queries. Print all interfaces of a certain type. 
 *
 * @author gideon
 */
public class CommandWithWhere extends Example {

    public static void main(String... args) throws Exception {
        CommandWithWhere ex = new CommandWithWhere();
        ex.connect();
        ex.test();
        ex.disconnect();
    }

    private void test() throws MikrotikApiException {
        List<Map<String, String>> results =  con.execute("/interface/print where type=ether");
        for (Map<String, String> result : results) {
            System.out.println(result);
        }
    }
}


File: /src\main\java\examples\Config.java
package examples;

/**
 * Config class for examples
 *
 * @author gideon
 */
public class Config {

    public static final String HOST = "ce2.ter.cpt.adept.za.net";
    public static final String USERNAME = "adept";
    public static final String PASSWORD = "34ffp9";

}


File: /src\main\java\examples\ConnectTLSAnonymous.java
/*
 * Copyright 2015 gideon.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *      http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */
package examples;

import java.util.List;
import java.util.Map;
import me.legrange.mikrotik.ApiConnection;
import me.legrange.mikrotik.MikrotikApiException;

/**
 * Example: Open an Anonymous TLS connection
 *
 * @author gideon
 */
public class ConnectTLSAnonymous {

    public static void main(String... args) throws Exception {
        ConnectTLSAnonymous ex = new ConnectTLSAnonymous();
        ex.connect();
        ex.test();
        ex.disconnect();
    }

    private void test() throws MikrotikApiException {
        List<Map<String, String>> results = con.execute("/interface/print");
        for (Map<String, String> result : results) {
            System.out.println(result);
        }
    }

    protected void connect() throws Exception {
        con = ApiConnection.connect(AnonymousSocketFactory.getDefault(), Config.HOST, ApiConnection.DEFAULT_TLS_PORT, ApiConnection.DEFAULT_CONNECTION_TIMEOUT);
        con.login(Config.USERNAME, Config.PASSWORD);
    }

    protected void disconnect() throws Exception {
        con.close();
    }

    private ApiConnection con;
}


File: /src\main\java\examples\ConnectTLSCertificate.java
/*
 * Copyright 2015 gideon.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *      http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */
package examples;

import java.util.List;
import java.util.Map;
import javax.net.ssl.SSLSocketFactory;
import me.legrange.mikrotik.ApiConnection;
import me.legrange.mikrotik.MikrotikApiException;

/**
 * Example: Open a TLS connection
 *
 * @author gideon
 */
public class ConnectTLSCertificate {

    public static void main(String... args) throws Exception {
        ConnectTLSCertificate ex = new ConnectTLSCertificate();
        ex.connect();
        ex.test();
        ex.disconnect();
    }

    private void test() throws MikrotikApiException {
        List<Map<String, String>> results = con.execute("/interface/print");
        for (Map<String, String> result : results) {
            System.out.println(result);
        }
    }

    protected void connect() throws Exception {
        con = ApiConnection.connect(SSLSocketFactory.getDefault(), Config.HOST, ApiConnection.DEFAULT_TLS_PORT, ApiConnection.DEFAULT_CONNECTION_TIMEOUT);
        con.login(Config.USERNAME, Config.PASSWORD);
    }

    protected void disconnect() throws Exception {
        con.close();
    }

    private ApiConnection con;
}


File: /src\main\java\examples\DownloadConfig.java
package examples;

import java.util.List;
import java.util.Map;
import me.legrange.mikrotik.MikrotikApiException;

/**
 * Example 7: Dump your complete config
 *
 * @author gideon
 */
public class DownloadConfig extends Example {

    public static void main(String... args) throws Exception {
        DownloadConfig ex = new DownloadConfig();
        ex.connect();
        ex.test();
        ex.disconnect();
    }

    private void test() throws MikrotikApiException, InterruptedException {
        con.execute("/export file=conf");
        List<Map<String, String>> res = con.execute("/file/print detail where name=conf.rsc");
        con.execute("/file/remove .id=conf.rsc");   
        String text = res.get(0).get("contents");
            for (String line : text.split("\r")) {
            System.out.println(line);
        }
    }
}


File: /src\main\java\examples\Example.java
package examples;

import javax.net.SocketFactory;
import me.legrange.mikrotik.ApiConnection;

/**
 *
 * @author gideon
 */
 abstract class Example {
     
    protected void connect() throws Exception {
        con = ApiConnection.connect(SocketFactory.getDefault(), Config.HOST, ApiConnection.DEFAULT_PORT, 2000);
        con.login(Config.USERNAME, Config.PASSWORD);
    }

    protected void disconnect() throws Exception {
        con.close();
    }
    
    protected ApiConnection con;
    
}


File: /src\main\java\examples\NestedExpressions.java
package examples;

import me.legrange.mikrotik.MikrotikApiException;

import java.util.List;
import java.util.Map;

/**
 * Example 2: A command that returns results. Print all interfaces
 *
 * @author gideon
 */
public class NestedExpressions extends Example {

    public static void main(String... args) throws Exception {
        NestedExpressions ex = new NestedExpressions();
        ex.connect();
        ex.test("/ip/firewall/nat/print where (src-address=\"192.168.15.52\" or src-address=\"192.168.15.53\")");
        ex.test("/ip/firewall/nat/print where chain=api_test and (src-address=192.168.15.52) and action=log ");
        ex.test("/ip/firewall/nat/print where chain=api_test and (src-address=192.168.15.53 or src-address=192.168.15.52) and action=log ");
        ex.test("/ip/firewall/nat/print where chain=api_test and (src-address=\"192.168.15.53\" or src-address=\"192.168.15.52\") and action=log ");
        ex.disconnect();
    }

    private void test(String cmd) throws MikrotikApiException {
        System.out.println("Command: " + cmd);
        List<Map<String, String>> results = con.execute(cmd);
        for (Map<String, String> result : results) {
            System.out.println(result);
        }
        System.out.println();
    }
}


File: /src\main\java\examples\ScriptCommand.java
package examples;

import me.legrange.mikrotik.MikrotikApiException;

/**
 * Example 1: A very simple command: Reboot the remote router
 * @author gideon
 */
public class ScriptCommand extends Example {
    
        public static void main(String...args) throws Exception {
            ScriptCommand ex = new ScriptCommand();
            ex.connect();
            ex.test();
            ex.disconnect();
        }
        
        private void test() throws MikrotikApiException {
            con.execute("/ip/hotspot/user/profile/add name=\"cahyo-cek-2\" idle-timeout=none keepalive-timeout=2m status-autorefresh=1m shared-users=1 add-mac-cookie=true mac-cookie-timeout=3d parent-queue=none rate-limit=512k/512k on-login=:put(\",re,3000,12d,3000,,Enable,\")");
        }

        ///
    /*
    /ip/hotspot/user/profile/add name="cahyo-cek-2" idle-timeout=none keepalive-timeout=2m status-autorefresh=1m shared-users=1 add-mac-cookie=true mac-cookie-timeout=3d parent-queue=none rate-limit=512k/512k on-login=:put (",re,3000,12d,3000,,Enable,");
    /system scheduler add name="usercahyo-cek-2-$user" interval=12:00:00 on-even="/ip hotspot active remove [find user=\"$user\"] ; /ip hotspot user set \"$user\" disable=yes ; /system scheduler remove [find name=usercahyo-cek-2-$user]"
*/
   
}


File: /src\main\java\examples\SimpleCommand.java
package examples;

import me.legrange.mikrotik.MikrotikApiException;

/**
 * Example 1: A very simple command: Reboot the remote router
 * @author gideon
 */
public class SimpleCommand extends Example {
    
        public static void main(String...args) throws Exception {
            SimpleCommand ex = new SimpleCommand();
            ex.connect();
            ex.test();
            ex.disconnect();
        }
        
        private void test() throws MikrotikApiException {
            con.execute("/system/reboot");
        }

   
}


File: /src\main\java\examples\SimpleCommandWithResults.java
package examples;

import java.util.List;
import java.util.Map;
import me.legrange.mikrotik.MikrotikApiException;

/**
 * Example 2: A command that returns results. Print all interfaces
 *
 * @author gideon
 */
public class SimpleCommandWithResults extends Example {

    public static void main(String... args) throws Exception {
        SimpleCommandWithResults ex = new SimpleCommandWithResults();
        ex.connect();
        ex.test();
        ex.disconnect();
    }

    private void test() throws MikrotikApiException {
        List<Map<String, String>> results =  con.execute("/interface/print");
        for (Map<String, String> result : results) {
            System.out.println(result);
        }
    }
}


File: /src\main\java\examples\TryWithResources.java
package examples;

import javax.net.SocketFactory;
import me.legrange.mikrotik.ApiConnection;
import me.legrange.mikrotik.MikrotikApiException;

/**
 * Example 9: Try with resources
 *
 * @author gideon
 */
public class TryWithResources  {

    public static void main(String... args) throws Exception {
        TryWithResources ex = new TryWithResources();
        ex.test();
    }

    private void test() throws MikrotikApiException, InterruptedException {
        try (ApiConnection con = ApiConnection.connect(SocketFactory.getDefault(), Config.HOST, ApiConnection.DEFAULT_PORT, 2000)) {
            con.login(Config.USERNAME, Config.PASSWORD);
            con.execute("/user/add name=eric");
        }
    }
}


File: /src\main\java\me\legrange\mikrotik\ApiConnection.java
package me.legrange.mikrotik;

import java.util.List;
import java.util.Map;
import javax.net.SocketFactory;
import me.legrange.mikrotik.impl.ApiConnectionImpl;

/**
 * The Mikrotik API connection. This is the class used to connect to a remote
 * Mikrotik and send commands to it.
 *
 * @author GideonLeGrange
 */
public abstract class ApiConnection implements AutoCloseable {

    /**
     * default TCP port used by Mikrotik API
     */
    public static final int DEFAULT_PORT = 8728;
    /**
     * default TCP TLS port used by Mikrotik API
     */
    public static final int DEFAULT_TLS_PORT = 8729;
    /**
     * default connection timeout to use when opening the connection
     */
    public static final int DEFAULT_CONNECTION_TIMEOUT = 60000;
    /**
     * default command timeout used for synchronous commands
     */
    public static final int DEFAULT_COMMAND_TIMEOUT = 60000;

    
    /**
     * Create a new API connection to the give device on the supplied port using 
     * the supplied socket factory to create the socket. 
     *
     * @param fact SocketFactory to use for TCP socket creation.
     * @param host The host to which to connect.
     * @param port The TCP port to use.
     * @param timeout The connection timeout to use when opening the connection.
     * @return The ApiConnection
     * @throws me.legrange.mikrotik.MikrotikApiException Thrown if there is a
     * problem connecting
     * @since 3.0
     */
    public static ApiConnection connect(SocketFactory fact, String host, int port, int timeout) throws MikrotikApiException {
        return ApiConnectionImpl.connect(fact, host, port, timeout);
    }

    /**
     * Create a new API connection to the give device on the default API port.
     *
     * @param host The host to which to connect.
     * @return The ApiConnection
     * @throws me.legrange.mikrotik.MikrotikApiException Thrown if there is a
     * problem connecting
     */
    public static ApiConnection connect(String host) throws MikrotikApiException {
        return connect(SocketFactory.getDefault(), host, DEFAULT_PORT, DEFAULT_COMMAND_TIMEOUT);
    }

    /**
     * Check the state of connection.
     *
     * @return if connection is established to router it returns true.
     */
    public abstract boolean isConnected();

    /**
     * Log in to the remote router.
     *
     * @param username - username of the user on the router
     * @param password - password for the user
     * @throws me.legrange.mikrotik.MikrotikApiException Thrown if the API encounters an error on login.
     */
    public abstract void login(String username, String password) throws MikrotikApiException;

    /**
     * execute a command and return a list of results.
     *
     * @param cmd Command to execute
     * @return The list of results
     * @throws me.legrange.mikrotik.MikrotikApiException Thrown if the API encounters an error executing a command.
     */
    public abstract List<Map<String, String>> execute(String cmd) throws MikrotikApiException;

    /**
     * execute a command and attach a result listener to receive it's results.
     *
     * @param cmd Command to execute
     * @param lis ResultListener that will receive the results
     * @return A command object that can be used to cancel the command.
     * @throws me.legrange.mikrotik.MikrotikApiException Thrown if the API encounters an error executing a command.
     */
    public abstract String execute(String cmd, ResultListener lis) throws MikrotikApiException;

    /**
     * cancel a command
     *
     * @param tag The tag of the command to cancel
     * @throws me.legrange.mikrotik.MikrotikApiException Thrown if there is a
     * problem cancelling the command
     */
    public abstract void cancel(String tag) throws MikrotikApiException;

    /**
     * set the command timeout. The command timeout is used to time out API
     * commands after a specific time.
     *
     * Note: This is not the same as the timeout value passed in the connect()
     * methods. This timeout is specific to synchronous
     * commands, that timeout is applied to opening the API socket.
     *
     * @param timeout The time out in milliseconds.
     * @throws MikrotikApiException Thrown if the timeout specified is invalid.
     * @since 2.1
     */
    public abstract void setTimeout(int timeout) throws MikrotikApiException;

    /**
     * Disconnect from the remote API
     *
     * @throws me.legrange.mikrotik.ApiConnectionException Thrown if there is a
     * problem closing the connection.
     * @since 2.2
     */
    @Override
    public abstract void close() throws ApiConnectionException;

}


File: /src\main\java\me\legrange\mikrotik\ApiConnectionException.java
package me.legrange.mikrotik;

/**
 * Exception thrown if the Api experiences a connection problem
 * @author GideonLeGrange
 */
public class ApiConnectionException extends MikrotikApiException {

    /** 
     * Create a new exception. 
     * 
     * @param msg The message
     */
    public ApiConnectionException(String msg) {
        super(msg);
    }

    /** 
     * Create a new exception 
     * @param msg The message
     * @param err The underlying cause 
     */
    public ApiConnectionException(String msg, Throwable err) {
        super(msg, err);
    }
    
    
    
}


File: /src\main\java\me\legrange\mikrotik\grammar.txt
command  = action [ query ] [ return ]
action   = ("/" word)+
query    = "where" expr
expr     = expr "and" expr | expr "or" expr | "not" expr | hasExpr | eqExpr | lessExpr | moreExpr | notExpr | nestedExpr
hasExpr  = name
eqExpr   = name "=" value
lessExpr = name "<" value
moreExpr = name ">" value
notExpr  = name "!=" value
nestedExpr = "(" expr ")" 
return   = "return" (name)+


 


File: /src\main\java\me\legrange\mikrotik\impl\ApiCommandException.java
package me.legrange.mikrotik.impl;

import me.legrange.mikrotik.MikrotikApiException;

/**
 * Thrown when the Mikrotik returns an error when receiving our command.
 *
 * @author GideonLeGrange
 */
public class ApiCommandException extends MikrotikApiException {

    private String tag = null;
    private int category = 0;

    /**
     * return the tag associated with this exception, if there is one
     *
     * @return the tag associated with this exception. Null if there is no tag
     */
    public String getTag() {
        return tag;
    }

    ApiCommandException(String msg) {
        super(msg);
    }

    ApiCommandException(String msg, Throwable err) {
        super(msg, err);
    }

    public int getCategory() {
        return category;
    }

    ApiCommandException(Error err) {
        super(err.getMessage());
        tag = err.getTag();
        category = err.getCategory();
    }


}


File: /src\main\java\me\legrange\mikrotik\impl\ApiConnectionImpl.java
package me.legrange.mikrotik.impl;

import java.io.DataInputStream;
import java.io.DataOutputStream;
import java.io.IOException;
import java.io.UnsupportedEncodingException;
import java.net.InetAddress;
import java.net.InetSocketAddress;
import java.net.Socket;
import java.net.UnknownHostException;
import java.util.Arrays;
import java.util.LinkedList;
import java.util.List;
import java.util.Map;
import java.util.concurrent.ConcurrentHashMap;
import java.util.concurrent.LinkedBlockingQueue;
import java.util.concurrent.atomic.AtomicInteger;
import javax.net.SocketFactory;
import me.legrange.mikrotik.ApiConnection;
import me.legrange.mikrotik.ApiConnectionException;
import me.legrange.mikrotik.MikrotikApiException;
import me.legrange.mikrotik.ResultListener;

/**
 * The Mikrotik API connection implementation. This is the class used to connect
 * to a remote Mikrotik and send commands to it.
 *
 * @author GideonLeGrange
 */
public final class ApiConnectionImpl extends ApiConnection {

    /**
     * Create a new API connection to the give device on the supplied port
     *
     * @param fact The socket factory used to construct the connection socket.
     * @param host The host to which to connect.
     * @param port The TCP port to use.
     * @param timeOut The connection timeout
     * @return The ApiConnection
     * @throws me.legrange.mikrotik.ApiConnectionException Thrown if there is a
     * problem connecting
     */
    public static ApiConnection connect(SocketFactory fact, String host, int port, int timeOut) throws ApiConnectionException {
        ApiConnectionImpl con = new ApiConnectionImpl();
        con.open(host, port, fact, timeOut);
        return con;
    }

    @Override
    public boolean isConnected() {
        return connected;
    }

    @Override
    public void login(String username, String password) throws MikrotikApiException {
        if (username.trim().isEmpty()) {
            throw new ApiConnectionException("API username cannot be empty");
        }
        Command cmd = new Command("/login");
        cmd.addParameter("name", username);
        cmd.addParameter("password", password);
        List<Map<String, String>> list = execute(cmd, timeout);
        if (!list.isEmpty()) {
            Map<String, String> res = list.get(0);
            if (res.containsKey("ret")) {
                String hash = res.get("ret");
                String chal = Util.hexStrToStr("00") + new String(password.toCharArray()) + Util.hexStrToStr(hash);
                chal = Util.hashMD5(chal);
                execute("/login name=" + username + " response=00" + chal);
            }
        }
    }

    @Override
    public List<Map<String, String>> execute(String cmd) throws MikrotikApiException {
        return execute(Parser.parse(cmd), timeout);
    }

    @Override
    public String execute(String cmd, ResultListener lis) throws MikrotikApiException {
        return execute(Parser.parse(cmd), lis);
    }

    @Override
    public void cancel(String tag) throws MikrotikApiException {
        execute(String.format("/cancel tag=%s", tag));
    }

    @Override
    public void setTimeout(int timeout) throws MikrotikApiException {
        if (timeout > 0) {
            this.timeout = timeout;
        } else {
            throw new MikrotikApiException(String.format("Invalid timeout value '%d'; must be postive", timeout));
        }
    }

    @Override
    public void close() throws ApiConnectionException {
        if (!connected) {
            throw new ApiConnectionException(("Not/no longer connected to remote Mikrotik"));
        }
        connected = false;
        processor.interrupt();
        reader.interrupt();
        try {
            in.close();
            out.close();
            sock.close();
        } catch (IOException ex) {
            throw new ApiConnectionException(String.format("Error closing socket: %s", ex.getMessage()), ex);
        }
    }

    private List<Map<String, String>> execute(Command cmd, int timeout) throws MikrotikApiException {
        SyncListener l = new SyncListener();
        execute(cmd, l);
        return l.getResults(timeout);
    }

    private String execute(Command cmd, ResultListener lis) throws MikrotikApiException {
        String tag = nextTag();
        cmd.setTag(tag);
        listeners.put(tag, lis);
        try {
            Util.write(cmd, out);
        } catch (UnsupportedEncodingException ex) {
            throw new ApiDataException(ex.getMessage(), ex);
        } catch (IOException ex) {
            throw new ApiConnectionException(ex.getMessage(), ex);
        }
        return tag;
    }

    private ApiConnectionImpl() {
        this.listeners = new ConcurrentHashMap<>();
    }

    /**
     * Start the API. Connects to the Mikrotik
     */
    private void open(String host, int port, SocketFactory fact, int conTimeout) throws ApiConnectionException {
        try {
            InetAddress ia = InetAddress.getByName(host.trim());
            sock = fact.createSocket();
            sock.connect(new InetSocketAddress(ia, port), conTimeout);
            in = new DataInputStream(sock.getInputStream());
            out = new DataOutputStream(sock.getOutputStream());
            connected = true;
            reader = new Reader();
            reader.setDaemon(true);
            reader.start();
            processor = new Processor();
            processor.setDaemon(true);
            processor.start();
        } catch (UnknownHostException ex) {
            connected = false;
            throw new ApiConnectionException(String.format("Unknown host '%s'", host), ex);
        } catch (IOException ex) {
            connected = false;
            throw new ApiConnectionException(String.format("Error connecting to %s:%d : %s", host, port, ex.getMessage()), ex);
        }
    }

    private synchronized String nextTag() {
        return Integer.toHexString(_tag.incrementAndGet());
    }

    private Socket sock = null;
    private DataOutputStream out = null;
    private DataInputStream in = null;
    private boolean connected = false;
    private Reader reader;
    private Processor processor;
    private final Map<String, ResultListener> listeners;
    private final AtomicInteger _tag = new AtomicInteger(0);
    private int timeout = ApiConnection.DEFAULT_COMMAND_TIMEOUT;

    /**
     * thread to read data from the socket and process it into Strings
     */
    private class Reader extends Thread {

        private Reader() {
            super("Mikrotik API Reader");
        }

        private String take() throws ApiConnectionException, ApiDataException {
            Object val;
            try {
                val = queue.take();
            } catch (InterruptedException ex) {
                throw new ApiConnectionException("Interrupted while reading data from queue.", ex);
            }
            if (val instanceof ApiConnectionException) {
                throw (ApiConnectionException) val;
            } else if (val instanceof ApiDataException) {
                throw (ApiDataException) val;
            }
            return (String) val;
        }

        private boolean isEmpty() {
            return queue.isEmpty();
        }

        @Override
        public void run() {
            while (connected) {
                try {
                    String s = Util.decode(in);
                    put(s);
                } catch (ApiDataException ex) {
                    put(ex);
                } catch (ApiConnectionException ex) {
                    if (connected || !sock.isClosed()) {
                        put(ex);
                    }
                }
            }
        }

        private void put(Object data) {
            try {
                queue.put(data);
            } catch (InterruptedException ignored) {
            }
        }

        private final LinkedBlockingQueue queue = new LinkedBlockingQueue(40);
    }

    /**
     * Thread to take the received strings and process it into Result objects
     */
    private class Processor extends Thread {

        private Processor() {
            super("Mikrotik API Result Processor");
        }

        @Override
        public void run() {
            while (connected) {
                Response res;
                try {
                    res = unpack();
                } catch (ApiCommandException ex) {
                    String tag = ex.getTag();
                    if (tag != null) {
                        res = new Error(tag, ex.getMessage(), ex.getCategory());
                    } else {
                        continue;
                    }
                } catch (MikrotikApiException ex) {
                    continue;
                }
                if (res.getTag() != null) {
                    ResultListener l = listeners.get(res.getTag());
                    if (l != null) {
                        if (res instanceof Result) {
                            l.receive((Result) res);
                        } else if (res instanceof Done) {
                            if (l instanceof SyncListener) {
                                ((SyncListener) l).completed((Done) res);
                            } else {
                                l.completed();
                            }
                            listeners.remove(res.getTag());
                        } else if (res instanceof Error) {
                            l.error(new ApiCommandException((Error) res));
                        }
                    }
                } else {
                    nextTag();
                }
            }
        }

        private void nextLine() throws ApiConnectionException, ApiDataException {
            if (lines.isEmpty()) {
                String block = reader.take();
                String[] parts = block.split("\n");
                lines.addAll(Arrays.asList(parts));
            }
            line = lines.remove(0);
        }

        private boolean hasNextLine() {
            return !lines.isEmpty() || !reader.isEmpty();
        }

        private String peekLine() throws ApiConnectionException, ApiDataException {
            if (lines.isEmpty()) {
                String block = reader.take();
                String[] parts = block.split("\n");
                lines.addAll(Arrays.asList(parts));
            }
            return lines.get(0);
        }

        private Response unpack() throws MikrotikApiException {
            if (line == null) {
                nextLine();
            }
            switch (line) {
                case "!re":
                    return unpackRe();
                case "!done":
                    return unpackDone();
                case "!trap":
                case "!halt":
                    return unpackError();
                case "":
                default:
                    throw new ApiDataException(String.format("Unexpected line '%s'", line));
            }
        }

        private Result unpackRe() throws ApiDataException, ApiConnectionException {
            nextLine();
            Result res = new Result();
            while (!line.startsWith(("!"))) {
                if (line.startsWith(("="))) {
                    String[] parts = line.split("=", 3);
                    if (parts.length == 3) {
                        if (!parts[2].endsWith("\r")) {
                            res.put(parts[1], unpackResult(parts[2]));
                        } else {
                            final StringBuilder sb = new StringBuilder();
                            sb.append(parts[2]);
                            while (!lines.isEmpty()) {
                                nextLine();
                                sb.append(line);
                            }
                            res.put(parts[1], sb.toString());
                        }
                    } else {
                        throw new ApiDataException(String.format("Malformed line '%s'", line));
                    }
                } else if (line.startsWith(".tag=")) {
                    String[] parts = line.split("=", 2);
                    if (parts.length == 2) {
                        res.setTag(parts[1]);
                    }
                } else {
                    throw new ApiDataException(String.format("Unexpected line '%s'", line));
                }
                if (hasNextLine()) {
                    nextLine();
                } else {
                    line = null;
                    break;
                }
            }
            return res;
        }

        private String unpackResult(String first) throws ApiConnectionException, ApiDataException {
            StringBuilder buf = new StringBuilder(first);
            line = null;

            while (hasNextLine()) {
                String peek = peekLine();
                if (!(peek.startsWith("!") || peek.startsWith("=") || peek.startsWith(".tag="))) {
                    nextLine();
                    buf.append("\n");
                    buf.append(line);
                } else {
                    break;
                }
            }
            return buf.toString();
        }

        private Done unpackDone() throws MikrotikApiException {
            Done done = new Done(null);
            if (hasNextLine()) {
                nextLine();

                while (!line.startsWith("!")) {
                    if (line.startsWith(".tag=")) {
                        String[] parts = line.split("=", 2);
                        if (parts.length == 2) {
                            done.setTag(parts[1]);
                        }
                    } else if (line.startsWith(("=ret"))) {
                        String[] parts = line.split("=", 3);
                        if (parts.length == 3) {
                            done.setHash(parts[2]);
                        } else {
                            throw new ApiDataException(String.format("Malformed line '%s'", line));
                        }
                    }
                    if (hasNextLine()) {
                        nextLine();
                    } else {
                        line = null;
                        break;
                    }
                }
            }
            return done;
        }

        private Error unpackError() throws MikrotikApiException {
            nextLine();
            Error err = new Error();
            if (hasNextLine()) {
                while (!line.startsWith("!")) {
                    if (line.startsWith(".tag=")) {
                        String[] parts = line.split("=", 2);
                        if (parts.length == 2) {
                            err.setTag(parts[1]);
                        }
                    } else if (line.startsWith("=message=")) {
                        err.setMessage(line.split("=", 3)[2]);
                    }
                    else if (line.startsWith("=category=")) {
                        err.setCategory(Integer.parseInt(line.split("=", 3)[2]));
                    }
                    if (hasNextLine()) {
                        nextLine();
                    } else {
                        line = null;
                        break;
                    }
                }
            }
            return err;
        }

        private final List<String> lines = new LinkedList<>();
        private String line;
    }

    private static class SyncListener implements ResultListener {

        @Override
        public synchronized void error(MikrotikApiException ex) {
            this.err = ex;
            notifyAll();
        }

        @Override
        public synchronized void completed() {
            complete = true;
            notifyAll();
        }

        synchronized void completed(Done done) {
            if (done.getHash() != null) {
                Result res = new Result();
                res.put("ret", done.getHash());
                results.add(res);
            }
            complete = true;
            notifyAll();
        }

        @Override
        public void receive(Map<String, String> result) {
            results.add(result);
        }

        private List<Map<String, String>> getResults(int timeout) throws MikrotikApiException {
            try {
                synchronized (this) { // don't wait if we already have a result.
                    int waitTime = timeout;
                    while (!complete && (waitTime > 0)) {
                        long start = System.currentTimeMillis();
                        wait(waitTime);
                        waitTime = waitTime - (int) (System.currentTimeMillis() - start);
                        if ((waitTime <= 0) && !complete) {
                            err = new ApiConnectionException(String.format("Command timed out after %d ms", timeout));
                        }
                    }
                }
            } catch (InterruptedException ex) {
                throw new ApiConnectionException(ex.getMessage(), ex);
            }
            if (err != null) {
                throw new MikrotikApiException(err.getMessage(), err);
            }
            return results;
        }

        private final List<Map<String, String>> results = new LinkedList<>();
        private MikrotikApiException err;
        private boolean complete = false;
    }
}


File: /src\main\java\me\legrange\mikrotik\impl\ApiDataException.java
package me.legrange.mikrotik.impl;

import me.legrange.mikrotik.MikrotikApiException;

/**
 * Thrown if there is a problem unpacking data from the Api. 
 * @author GideonLeGrange
 */
public class ApiDataException extends MikrotikApiException {

    ApiDataException(String msg) {
        super(msg);
    }

    ApiDataException(String msg, Throwable err) {
        super(msg, err);
    }

    
    
}


File: /src\main\java\me\legrange\mikrotik\impl\Command.java
package me.legrange.mikrotik.impl;

import java.util.Arrays;
import java.util.LinkedList;
import java.util.List;

/**
 * A command sent to a Mikrotik. This internal class is used to build complex commands
 * with parameters, queries and property lists.
 *
 * @author GideonLeGrange
 */
class Command {

    @Override
    public String toString() {
        return String.format("cmd[%s] = %s, params = %s, queries = %s, props=%s ", tag, cmd, params, queries, properties);
    }

    Command(String cmd) {
        if (!cmd.startsWith("/")) {
            cmd = "/" + cmd;
        }
        this.cmd = cmd;
    }

    String getCommand() {
        return cmd;
    }

    /**
     * Add a parameter to a command.
     */
    void addParameter(String name, String value) {
        params.add(new Parameter(name, value));
    }

    /**
     * Add a valueless parameter to the command
     */
    void addParameter(Parameter param) {
        params.add(param);
    }

    /**
     * Add a property to include in a result
     */
    void addProperty(String... names) {
        properties.addAll(Arrays.asList(names));
    }

    void addQuery(String... queries) {
        this.queries.addAll(Arrays.asList(queries));
    }

    void setTag(String tag) {
        this.tag = tag;
    }

    List<String> getQueries() {
        return queries;

    }

    String getTag() {
        return tag;
    }

    List<String> getProperties() {
        return properties;
    }

    List<Parameter> getParameters() {
        return params;
    }
    private final String cmd;
    private final List<Parameter> params = new LinkedList<>();
    private final List<String> queries = new LinkedList<>();
    private final List<String> properties = new LinkedList<>();
    private String tag;
}


File: /src\main\java\me\legrange\mikrotik\impl\Done.java
package me.legrange.mikrotik.impl;

/**
 * Internal representation of !done
 * @author GideonLeGrange
 */
class Done extends Response {

    Done(String tag) {
        super(tag);
    }

    void setHash(String hash) {
        this.hash = hash;
    }
    
    String getHash() {
        return hash;
    }
    
    private String hash;
    
}


File: /src\main\java\me\legrange\mikrotik\impl\Error.java
package me.legrange.mikrotik.impl;

/**
 * Used to encapsulate API error information. We need to pass both the message and the tag (if one was used).
 *
 * @author GideonLeGrange
 */
class Error extends Response {

    private String message;
    private int category;

    Error(String tag, String message, int category) {
        super(tag);
        this.message = message;
    }

    Error() {
        super(null);
    }

    String getMessage() {
        return message;
    }

    void setMessage(String message) {
        this.message = message;
    }

    int getCategory() {
        return category;
    }

    void setCategory(int category) {
        this.category = category;
    }
}


File: /src\main\java\me\legrange\mikrotik\impl\Parameter.java
package me.legrange.mikrotik.impl;

/**
 * A command parameter
 *
 * @author GideonLeGrange
 */
class Parameter {

    @Override
    public String toString() {
        if (hasValue()) {
            return String.format("%s=%s", name, value);
        } else {
            return name;
        }
    }

    Parameter(String name, String value) {
        this.name = name;
        this.value = value;
    }

    Parameter(String name) {
        this(name, null);
    }

    boolean hasValue() {
        return value != null;
    }

    String getName() {
        return name;
    }

    String getValue() {
        return value;
    }
    private String name;
    private String value;
}


File: /src\main\java\me\legrange\mikrotik\impl\ParseException.java
package me.legrange.mikrotik.impl;

import me.legrange.mikrotik.MikrotikApiException;

/**
 * Exception thrown if the parser encounters an error while parsing a command line.
 * @author GideonLeGrange
 */
public class ParseException extends MikrotikApiException {

    ParseException(String msg) {
        super(msg);
    }

    ParseException(String msg, Throwable err) {
        super(msg, err);
    }
    
    
    
}


File: /src\main\java\me\legrange\mikrotik\impl\Parser.java
package me.legrange.mikrotik.impl;

import java.util.Arrays;
import java.util.LinkedList;
import java.util.List;

import me.legrange.mikrotik.impl.Scanner.Token;

/**
 * Parse the pseudo-command line into command objects.
 *
 * @author GideonLeGrange
 */
class Parser {

    /**
     * parse the given bit of text into a Command object
     */
    static Command parse(String text) throws ParseException {
        Parser parser = new Parser(text);
        return parser.parse();
    }

    /**
     * run parse on the internal data and return the command object
     */
    private Command parse() throws ParseException {
        command();
        while (!is(Token.WHERE, Token.RETURN, Token.EOL)) {
            param();
        }
        if (token == Token.WHERE) {
            where();
        }
        if (token == Token.RETURN) {
            returns();
        }
        expect(Token.EOL);
        return cmd;
    }

    private void command() throws ParseException {
        StringBuilder path = new StringBuilder();
        do {
            expect(Token.SLASH);
            path.append("/");
            next();
            expect(Token.TEXT);
            path.append(text);
            next();
        } while (token == Token.SLASH);
        cmd = new Command(path.toString());
    }

    private void param() throws ParseException {
        String name = text;
        next();
        if (token == Token.EQUALS) {
            next();
            StringBuilder val = new StringBuilder();
            if (token == Token.PIPE) { // handle cases like  hotspot=!auth 
                val.append(token);
                next();
            }
            expect(Token.TEXT);
            val.append(text);
            next();
            while (is(Token.COMMA, Token.SLASH)) {
                val.append(token);
                next();
                expect(Token.TEXT);
                val.append(text);
                next();
            }
            cmd.addParameter(new Parameter(name, val.toString()));
        } else {
            cmd.addParameter(new Parameter(name));
        }
    }

    private void where() throws ParseException {
        next(); // swallow the word "where"
        expr();
    }

    private void expr() throws ParseException {
        expect(Token.NOT, Token.TEXT, Token.LEFT_BRACKET);
        switch (token) {
            case NOT:
                notExpr();
                break;
            case TEXT: {
                String name = text;
                next();
                expect(Token.EQUALS, Token.LESS, Token.MORE, Token.NOT_EQUALS);
                switch (token) {
                    case EQUALS:
                        eqExpr(name);
                        break;
                    case NOT_EQUALS:
                        notExpr(name);
                        break;
                    case LESS:
                        lessExpr(name);
                        break;
                    case MORE:
                        moreExpr(name);
                        break;
                    default:
                        hasExpr(name);
                }
            }
            break;
            case LEFT_BRACKET:
                nestedExpr();
                break;
        }
        // if you get here, you had a expression, see if you want more. 
        switch (token) {
            case AND:
                andExpr();
                break;
            case OR:
                orExpr();
                break;
        }
    }

    private void nestedExpr() throws ParseException {
        expect(Token.LEFT_BRACKET);
        next();
        expr();
        expect(Token.RIGHT_BRACKET);
        next();
    }

    private void andExpr() throws ParseException {
        next(); // eat and
        expr();
        cmd.addQuery("?#&");
    }

    private void orExpr() throws ParseException {
        next(); // eat or
        expr();
        cmd.addQuery("?#|");
    }


    private void notExpr() throws ParseException {
        next(); // eat not
        expr();
        cmd.addQuery("?#!");
    }

    private void eqExpr(String name) throws ParseException {
        next(); // eat = 
        expect(Token.TEXT);
        cmd.addQuery(String.format("?%s=%s", name, text));
        next();
    }

    private void lessExpr(String name) throws ScanException {
        next(); // eat < 
        cmd.addQuery(String.format("?<%s=%s", name, text));
        next();
    }

    private void notExpr(String name) throws ScanException {
        next(); // eat !=
        cmd.addQuery(String.format("?%s=%s", name, text));
        cmd.addQuery("?#!");
        next();
    }

    private void moreExpr(String name) throws ScanException {
        next(); // eat >
        cmd.addQuery(String.format("?>%s=%s", name, text));
        next();
    }

    private void hasExpr(String name) {
        cmd.addQuery(String.format("?%s", name));
    }

    private void returns() throws ParseException {
        next();
        expect(Token.TEXT);
        List<String> props = new LinkedList<>();
        while (!(token == Token.EOL)) {
            if (token != Token.COMMA) {
                props.add(text);
            }
            next();
        }
        cmd.addProperty(props.toArray(new String[props.size()]));
    }

    private void expect(Token... tokens) throws ParseException {
        if (!is(tokens))
            throw new ParseException(String.format("Expected %s but found %s at position %d", Arrays.asList(tokens), this.token, scanner.pos()));
    }

    private boolean is(Token... tokens) {
        for (Token want : tokens) {
            if (this.token == want) return true;
        }
        return false;
    }

    /**
     * move to the next token returned by the scanner
     */
    private void next() throws ScanException {
        token = scanner.next();
        while (token == Token.WS) {
            token = scanner.next();
        }
        text = scanner.text();
    }

    private Parser(String line) throws ScanException {
        line = line.trim();
        scanner = new Scanner(line);
        next();
    }

    private final Scanner scanner;
    private Token token;
    private String text;
    private Command cmd;

}


File: /src\main\java\me\legrange\mikrotik\impl\Response.java
package me.legrange.mikrotik.impl;

/**
 * Super type of possible API responses
 *
 * @author GideonLeGrange
 */
abstract class Response {

    public String getTag() {
        return tag;
    }
    
    @Override
    public String toString() {
        return String.format("%s: tag=%s", getClass().getSimpleName(), tag);
    }
    
    void setTag(String tag) { 
        this.tag = tag;
    }
    
    protected Response(String tag) {
        this.tag = tag;
    }
    
    private  String tag;
}


File: /src\main\java\me\legrange\mikrotik\impl\Result.java
    package me.legrange.mikrotik.impl;

import java.util.Collection;
import java.util.HashMap;
import java.util.Map;
import java.util.Set;

/**
 * A result from an API command. 
 * @author GideonLeGrange
 */
class Result extends Response implements Map<String, String> {

    public String get(String key) {
        return map.get(key);
    }
    
    @Override
    public boolean isEmpty() {
        return map.isEmpty();
    }
    
    @Override
    public String toString() {
        return String.format("tag=%s, data=%s", getTag(), map);
    }

    @Override
    public int size() {
        return map.size();
    }

    @Override
    public boolean containsKey(Object o) {
        return map.containsKey(o);
    }

    @Override
    public boolean containsValue(Object o) {
        return map.containsValue(o);
    }

    @Override
    public String get(Object o) {
        return map.get(o);
    }

    @Override
    public String put(String k, String v) {
        return map.put(k, v);
    }

    @Override
    public String remove(Object o) {
        return map.remove(o);
    }

    @Override
    public void putAll(Map<? extends String, ? extends String> map) {
        this.map.putAll(map);
    }

    @Override
    public void clear() {
        map.clear();
    }

    @Override
    public Set<String> keySet() {
        return map.keySet();
    }

    @Override
    public Collection<String> values() {
        return map.values();
    }

    @Override
    public Set<Entry<String, String>> entrySet() {
        return map.entrySet();
    }

    Result() {
        super(null);
        this.map = new HashMap<>();
    }
   
    private final Map<String, String> map;

}


File: /src\main\java\me\legrange\mikrotik\impl\ScanException.java
package me.legrange.mikrotik.impl;

/**
 * Exception thrown if the scanner encounters an error while scanning a command line.
 * @author GideonLeGrange
 */
public class ScanException extends ParseException {

    ScanException(String msg) {
        super(msg);
    }

    ScanException(String msg, Throwable err) {
        super(msg, err);
    }
    
}


File: /src\main\java\me\legrange\mikrotik\impl\Scanner.java
/*
 * Copyright 2014 GideonLeGrange.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *      http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */
package me.legrange.mikrotik.impl;

import java.util.Locale;
import static me.legrange.mikrotik.impl.Scanner.Token.*;
/**
 * A simple scanner.
 *
 * @author gideon
 */
class Scanner {

    enum Token {

        SLASH("/"), COMMA(","), EOL(), WS, TEXT,
        LESS("<"), MORE(">"), EQUALS("="), NOT_EQUALS("!="), PIPE("!"),
        LEFT_BRACKET("("), RIGHT_BRACKET(")"),
        WHERE, NOT, AND, OR, RETURN;

        @Override
        public String toString() {
            return (symb == null) ? name() : symb;
        }

        private Token(String symb) {
            this.symb = symb;
        }

        private Token() {
            symb = null;
        }

        private final String symb;
    }

    /**
     * create a scanner for the given line of text
     */
    Scanner(String line) {
        this.line = line;
        nextChar();
    }

    /**
     * return the next token from the text
     */
    Token next() throws ScanException {
        text = null;
        switch (c) {
            case '\n':
                return EOL;
            case ' ':
            case '\t':
                return whiteSpace();
            case ',':
                nextChar();
                return COMMA;
            case '/':
                nextChar();
                return SLASH;
            case '<':
                nextChar();
                return LESS;
            case '>':
                nextChar();
                return MORE;
            case '=':
                nextChar();
                return EQUALS;
            case '(' :
                nextChar();
                return LEFT_BRACKET;
            case ')' :
                nextChar();
                return RIGHT_BRACKET;
            case '!':
                return pipe();
            case '"':
                return quotedText('"');
            case '\'':
                return quotedText('\'');
            default:
                return name();
        }

    }

    /**
     * return the text associated with the last token returned
     */
    String text() {
        if (text != null) {
            return text.toString();
        }
        return "";
    }

    /**
     * return the position of the scanner
     */
    int pos() {
        return pos;
    }

    /**
     * process 'name' tokens which could be key words or text
     */
    private Token name() throws ScanException {
        text = new StringBuilder();
        while (!in(c, "[ \t\r\n=<>!)]")) {
            text.append(c);
            nextChar();
        }
        String val = text.toString().toLowerCase(Locale.getDefault());
        switch (val) {
            case "where":
                return WHERE;
            case "not":
                return NOT;
            case "and":
                return AND;
            case "or":
                return OR;
            case "return":
                return RETURN;
        }
        return TEXT;
    }

    /**
     * process quoted text
     */
    private Token quotedText(char quote) throws ScanException {
        nextChar(); // eat the '"'
        text = new StringBuilder();
        while (c != quote) {
            if (c == '\n') {
                throw new ScanException("Unclosed quoted text, reached end of line.");
            }
            text.append(c);
            nextChar();
        }
        nextChar(); // eat the '"'
        return TEXT;
    }

    /**
     * process notEquals !
     */
    private Token pipe() {
        nextChar(); // eat !
        if (c == '=') {
            nextChar(); // eat =
            return NOT_EQUALS;
        }
        return PIPE;
    }

    /**
     * process white space
     */
    private Token whiteSpace() {
        while ((c == ' ') || (c == '\t')) {
            nextChar();
        }
        return WS;
    }

    /**
     * return the next character from the line of text
     */
    private void nextChar() {
        if (pos < line.length()) {
            c = line.charAt(pos);
            pos++;
        } else {
            c = '\n';
        }
    }

    /**
     * check if the character matches the give expression
     */
    private boolean in(char c, String cs) {
        return ("" + c).matches(cs);
    }

    private final String line;
    private int pos = 0;
    private char c;
    private StringBuilder text;
}


File: /src\main\java\me\legrange\mikrotik\impl\Util.java
package me.legrange.mikrotik.impl;

import java.io.IOException;
import java.io.InputStream;
import java.io.OutputStream;
import java.io.UnsupportedEncodingException;
import java.nio.charset.Charset;
import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;
import java.util.List;
import me.legrange.mikrotik.ApiConnectionException;

/**
 * Utility library that handles the low level encoding required by the Mikrotik
 * API.
 *
 * @author GideonLeGrange. Possibly some code by janisk left.
 */
final class Util {

    /**
     * write a command to the output stream
     */
    static void write(Command cmd, OutputStream out) throws UnsupportedEncodingException, IOException {
        encode(cmd.getCommand(), out);
        for (Parameter param : cmd.getParameters()) {
            encode(String.format("=%s=%s", param.getName(), param.hasValue() ? param.getValue() : ""), out);
        }
        String tag = cmd.getTag();
        if ((tag != null) && !tag.equals("")) {
            encode(String.format(".tag=%s", tag), out);
        }
        List<String> props = cmd.getProperties();
        if (!props.isEmpty()) {
            StringBuilder buf = new StringBuilder("=.proplist=");
            for (int i = 0; i < props.size(); ++i) {
                if (i > 0) {
                    buf.append(",");
                }
                buf.append(props.get(i));
            }
            encode(buf.toString(), out);
        }
        for (String query : cmd.getQueries()) {
            encode(query, out);
        }
        out.write(0);
    }

    /**
     * decode bytes from an input stream of Mikrotik protocol sentences into
     * text
     */
    static String decode(InputStream in) throws ApiDataException, ApiConnectionException {
        StringBuilder res = new StringBuilder();
        decode(in, res);
        return res.toString();
    }

    /**
     * decode bytes from an input stream into Mikrotik protocol sentences
     */
    private static void decode(InputStream in, StringBuilder result) throws ApiDataException, ApiConnectionException {
        try {
            int len = readLen(in);
            if (len > 0) {
                byte buf[] = new byte[len];
                for (int i = 0; i < len; ++i) {
                    int c = in.read();
                    if (c < 0) {
                        throw new ApiDataException("Truncated data. Expected to read more bytes");
                    }
                    buf[i] = (byte) (c & 0xFF);
                }
                String res = new String(buf, Charset.forName("UTF-8"));
                if (result.length() > 0) {
                    result.append("\n");
                }
                result.append(res);
                decode(in, result);
            }
        } catch (IOException ex) {
            throw new ApiConnectionException(ex.getMessage(), ex);
        }
    }

    /**
     * makes MD5 hash of string for use with RouterOS API
     *
     * @param s - variable to make hash from
     * @return - the md5 hash
     */
    static String hashMD5(String s) throws ApiDataException {
        MessageDigest algorithm = null;
        try {
            algorithm = MessageDigest.getInstance("MD5");
        } catch (NoSuchAlgorithmException nsae) {
            throw new ApiDataException("Cannot find MD5 digest algorithm");
        }
        byte[] defaultBytes = new byte[s.length()];
        for (int i = 0; i < s.length(); i++) {
            defaultBytes[i] = (byte) (0xFF & s.charAt(i));
        }
        algorithm.reset();
        algorithm.update(defaultBytes);
        byte messageDigest[] = algorithm.digest();
        StringBuilder hexString = new StringBuilder();
        for (int i = 0; i < messageDigest.length; i++) {
            String hex = Integer.toHexString(0xFF & messageDigest[i]);
            if (hex.length() == 1) {
                hexString.append('0');
            }
            hexString.append(hex);
        }
        return hexString.toString();
    }

    /**
     * converts hex value string to normal strint for use with RouterOS API
     *
     * @param s - hex string to convert to
     * @return - converted string.
     */
    static String hexStrToStr(String s) {
        StringBuilder ret = new StringBuilder();
        for (int i = 0; i < s.length(); i += 2) {
            ret.append((char) Integer.parseInt(s.substring(i, i + 2), 16));
        }
        return ret.toString();
    }

    /**
     * encode text using Mikrotik's encoding scheme and write it to an output
     * stream.
     */
    private static void encode(String word, OutputStream out) throws UnsupportedEncodingException, IOException {
        byte bytes[] = word.getBytes("UTF-8");
        int len = bytes.length;
        if (len < 0x80) {
            out.write(len);
        } else if (len < 0x4000) {
            len = len | 0x8000;
            out.write(len >> 8);
            out.write(len);
        } else if (len < 0x20000) {
            len = len | 0xC00000;
            out.write(len >> 16);
            out.write(len >> 8);
            out.write(len);
        } else if (len < 0x10000000) {
            len = len | 0xE0000000;
            out.write(len >> 24);
            out.write(len >> 16);
            out.write(len >> 8);
            out.write(len);
        } else {
            out.write(0xF0);
            out.write(len >> 24);
            out.write(len >> 16);
            out.write(len >> 8);
            out.write(len);
        }
        out.write(bytes);
    }

    /**
     * read length bytes from stream and return length of coming word
     */
    private static int readLen(InputStream in) throws IOException {
        int c = in.read();
        if (c > 0) {
            if ((c & 0x80) == 0) {
            } else if ((c & 0xC0) == 0x80) {
                c = c & ~0xC0;
                c = (c << 8) | in.read();
            } else if ((c & 0xE0) == 0xC0) {
                c = c & ~0xE0;
                c = (c << 8) | in.read();
                c = (c << 8) | in.read();
            } else if ((c & 0xF0) == 0xE0) {
                c = c & ~0xF0;
                c = (c << 8) | in.read();
                c = (c << 8) | in.read();
                c = (c << 8) | in.read();
            } else if ((c & 0xF8) == 0xF0) {
                c = in.read();
                c = (c << 8) | in.read();
                c = (c << 8) | in.read();
                c = (c << 8) | in.read();
                c = (c << 8) | in.read();
            }
        }
        return c;
    }
}

File: /src\main\java\me\legrange\mikrotik\MikrotikApiException.java
package me.legrange.mikrotik;

/**
 * Thrown by the Mikrotik API to indicate errors
 *
 * @author GideonLeGrange
 */
public class MikrotikApiException extends Exception {


    /** 
     * Create a new exception 
     * @param msg The message
     */
    public MikrotikApiException(String msg) {
        super(msg);
    }

 
    /** 
     * Create a new exception 
     * @param msg The message
     * @param err The underlying cause 
     */
    public MikrotikApiException(String msg, Throwable err) {
        super(msg, err);
    }
}


File: /src\main\java\me\legrange\mikrotik\ResultListener.java
package me.legrange.mikrotik;

import java.util.Map;

/**
 * Implement this interface to receive command results from the Mikrotik Api.
 * @author GideonLeGrange
 */
public interface ResultListener {
    
    /** receive data from router
     * @param result The data received */
    void receive(Map<String, String> result);

    /** called if the command associated with this listener experiences an error
     * @param ex Exception encountered */
    void error(MikrotikApiException ex);
    
    /** called when the command associated with this listener is done */
    void completed();
   
}


