# Repository Information
Name: MikrotikDotNet

# Directory Structure
Directory structure:
└── github_repos/MikrotikDotNet/
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
    │   │       ├── pack-634730190aa7a42e6bebc321ab720378d94185d8.idx
    │   │       └── pack-634730190aa7a42e6bebc321ab720378d94185d8.pack
    │   ├── packed-refs
    │   └── refs/
    │       ├── heads/
    │       │   └── master
    │       ├── remotes/
    │       │   └── origin/
    │       │       └── HEAD
    │       └── tags/
    ├── .gitattributes
    ├── .gitignore
    ├── azure-pipelines.yml
    ├── Mikrotik.Net/
    │   ├── Exceptions/
    │   │   ├── CommandFalureTypes.cs
    │   │   ├── MKCommandException.cs
    │   │   ├── MKConnectionException.cs
    │   │   ├── MKException.cs
    │   │   └── MKResponseParseException.cs
    │   ├── IMKCommand.cs
    │   ├── IMKConnection.cs
    │   ├── Mikrotik.Net.csproj
    │   ├── MKCommand.cs
    │   ├── MKCommandParameter.cs
    │   ├── MKCommandParameterCollection.cs
    │   ├── MKConnection.cs
    │   ├── MKQueryLogicOperators.cs
    │   └── ReponseParser/
    │       ├── MemberNameHelper.cs
    │       ├── MKResponseParser.cs
    │       └── RowParser.cs
    ├── Mikrotik.Net.UnitTest/
    │   ├── Mikrotik.Net.UnitTest.csproj
    │   ├── MkResponseParserTests/
    │   │   ├── Given_Response_Parser.cs
    │   │   ├── When_Parsing_Dynamic_Object.cs
    │   │   └── When_Parsing_Typed_Object.cs
    │   └── StringTools.cs
    ├── MikrotikDotNet.sln
    ├── NewAuthenticationMode
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
	url = https://github.com/janmohammadi/MikrotikDotNet.git
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
0000000000000000000000000000000000000000 c91c82eee8d46d582f9606173db74aa42de07cda vivek-dodia <vivek.dodia@icloud.com> 1738605952 -0500	clone: from https://github.com/janmohammadi/MikrotikDotNet.git


File: /.git\logs\refs\heads\master
0000000000000000000000000000000000000000 c91c82eee8d46d582f9606173db74aa42de07cda vivek-dodia <vivek.dodia@icloud.com> 1738605952 -0500	clone: from https://github.com/janmohammadi/MikrotikDotNet.git


File: /.git\logs\refs\remotes\origin\HEAD
0000000000000000000000000000000000000000 c91c82eee8d46d582f9606173db74aa42de07cda vivek-dodia <vivek.dodia@icloud.com> 1738605952 -0500	clone: from https://github.com/janmohammadi/MikrotikDotNet.git


File: /.git\packed-refs
# pack-refs with: peeled fully-peeled sorted 
c91c82eee8d46d582f9606173db74aa42de07cda refs/remotes/origin/master


File: /.git\refs\heads\master
c91c82eee8d46d582f9606173db74aa42de07cda


File: /.git\refs\remotes\origin\HEAD
ref: refs/remotes/origin/master


File: /.gitattributes
# Auto detect text files and perform LF normalization
* text=auto

# Custom for Visual Studio
*.cs     diff=csharp

# Standard to msysgit
*.doc	 diff=astextplain
*.DOC	 diff=astextplain
*.docx diff=astextplain
*.DOCX diff=astextplain
*.dot  diff=astextplain
*.DOT  diff=astextplain
*.pdf  diff=astextplain
*.PDF	 diff=astextplain
*.rtf	 diff=astextplain
*.RTF	 diff=astextplain


File: /.gitignore
## Ignore Visual Studio temporary files, build results, and
## files generated by popular Visual Studio add-ons.

# User-specific files
*.suo
*.user
*.userosscache
*.sln.docstates

# User-specific files (MonoDevelop/Xamarin Studio)
*.userprefs

# Build results
[Dd]ebug/
[Dd]ebugPublic/
[Rr]elease/
[Rr]eleases/
x64/
x86/
build/
bld/
[Bb]in/
[Oo]bj/

# Visual Studio 2015 cache/options directory
.vs/
# Uncomment if you have tasks that create the project's static files in wwwroot
#wwwroot/

# MSTest test Results
[Tt]est[Rr]esult*/
[Bb]uild[Ll]og.*

# NUNIT
*.VisualState.xml
TestResult.xml

# Build Results of an ATL Project
[Dd]ebugPS/
[Rr]eleasePS/
dlldata.c

# DNX
project.lock.json
artifacts/

*_i.c
*_p.c
*_i.h
*.ilk
*.meta
*.obj
*.pch
*.pdb
*.pgc
*.pgd
*.rsp
*.sbr
*.tlb
*.tli
*.tlh
*.tmp
*.tmp_proj
File: /azure-pipelines.yml
# .NET Desktop
# Build and run tests for .NET Desktop or Windows classic desktop solutions.
# Add steps that publish symbols, save build artifacts, and more:
# https://docs.microsoft.com/azure/devops/pipelines/apps/windows/dot-net

trigger:
- master

variables:
  BUILD_BUILDNUMBER: '1.3.0'

steps:
  - task: DotNetCoreCLI@2
    inputs:
      command: 'pack'
      packagesToPack: '**/Mikrotik.Net.csproj'
      versioningScheme: byBuildNumber
  - task: PublishBuildArtifacts@1
    inputs:
      PathtoPublish: '$(Build.ArtifactStagingDirectory)'
      ArtifactName: 'drop'
      publishLocation: 'Container'

File: /Mikrotik.Net\Exceptions\CommandFalureTypes.cs
﻿using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace MikrotikDotNet.Exceptions
{
    /// <summary>
    /// The values for "Category" field in Api Exceptions.
    /// </summary>
    /// <seealso href="http://wiki.mikrotik.com/wiki/Manual:API#category" target="_blank" />
    public enum CommandFailureTypes
    {
        /// <summary>
        ///  missing item or command
        /// </summary>
        MissingItemOrCommand = 0,
        /// <summary>
        /// argument value failure
        /// </summary>
        ArgumentValueFailure = 1,
        /// <summary>
        /// The execution of command interrupted
        /// </summary>
        ExecutionOfCommandInterrupted = 2,
        /// <summary>
        /// The scripting related failure
        /// </summary>
        ScriptingRelatedFailure = 3,
        /// <summary>
        /// The general failure
        /// </summary>
        GeneralFailure = 4,
        /// <summary>
        /// The API related failure
        /// </summary>
        APIRelatedFailure = 5,
        /// <summary>
        /// The tty related failure
        /// </summary>
        TTYRelatedFailure = 6,
        /// <summary>
        /// The value generated with return command
        /// </summary>
        ValueGeneratedWithReturnCommand = 7
    }
}


File: /Mikrotik.Net\Exceptions\MKCommandException.cs
﻿using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace MikrotikDotNet.Exceptions
{
    /// <summary>
    /// Class MKCommandException.
    /// </summary>
    /// <seealso cref="MikrotikDotNet.Exceptions.MKException" />
    public class MKCommandException : MKException
    {
        public MKCommandException()
        {
          
        }

        public MKCommandException(string message)
            : base(message)
        {
        }

        public MKCommandException(string message, CommandFailureTypes errorCategory) : this(message)
        {
            this.ErrorCategory = errorCategory;
        }

        public CommandFailureTypes ErrorCategory { get; set; }
    }
}


File: /Mikrotik.Net\Exceptions\MKConnectionException.cs
﻿using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace MikrotikDotNet.Exceptions
{
    public class MKConnectionException : MKException
    {
        public MKConnectionException()
        {
        }

        public MKConnectionException(string message)
            : base(message)
        {
        }
    }
}


File: /Mikrotik.Net\Exceptions\MKException.cs
﻿using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace MikrotikDotNet.Exceptions
{
    public class MKException : Exception
    {
        public MKException()
        {
        }

        public MKException(string msg)
            : base(msg)
        {
        }
    }
}


File: /Mikrotik.Net\Exceptions\MKResponseParseException.cs
﻿using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace MikrotikDotNet.Exceptions
{
    public class MKResponseParseException : MKException
    {
        public MKResponseParseException()
        {
        }

        public MKResponseParseException(string message)
            : base(message)
        {
        }
    }
}


File: /Mikrotik.Net\IMKCommand.cs
﻿using System.Collections.Generic;

namespace MikrotikDotNet
{
    public interface IMKCommand
    {
        string CommandText { get; set; }
        IMKConnection Connection { get; set; }
        MKCommandParameterCollection Parameters { get; set; }

        void ExecuteBackground();
        void ExecuteNonQuery();
        IEnumerable<string> ExecuteReader(string propList = null, MKCommandParameterCollection queryConditions = null, MKQueryLogicOperators logic = MKQueryLogicOperators.And);
        IEnumerable<TType> ExecuteReader<TType>(MKCommandParameterCollection queryConditions, MKQueryLogicOperators logic );
        IEnumerable<TType> ExecuteReader<TType>();
        IEnumerable<dynamic> ExecuteReaderDynamic(MKCommandParameterCollection queryConditions , MKQueryLogicOperators logic);

        IEnumerable<dynamic> ExecuteReaderDynamic();
    }
}

File: /Mikrotik.Net\IMKConnection.cs
﻿using System;
using System.Collections.Generic;

namespace MikrotikDotNet
{
    public interface IMKConnection
    {
        Guid GUID { get; }
        string Host { get; set; }
        bool IsOpen { get; }
        string Password { get; set; }
        int Port { get; set; }
        string UserName { get; set; }

        void Close();
        IMKCommand CreateCommand();
        IMKCommand CreateCommand(string commandText);
        void Dispose();
        string EncodePassword(string password, string hash);
        bool Equals(MKConnection other);
        void Open();
        void Open(string host, string username, string password, int port);
        void Push();
        List<string> Read();
        void Send(string co);
    }
}

File: /Mikrotik.Net\Mikrotik.Net.csproj
<Project Sdk="Microsoft.NET.Sdk">

  <PropertyGroup>
    <TargetFramework>netstandard2.0</TargetFramework>
    <RootNamespace>MikrotikDotNet</RootNamespace>
  </PropertyGroup>

</Project>


File: /Mikrotik.Net\MKCommand.cs
﻿using System;
using System.Collections.Generic;
using MikrotikDotNet.Exceptions;
using MikrotikDotNet.ReponseParser;

namespace MikrotikDotNet
{
    /// <summary>
    ///     Represents a Api Command in Mikrotik.
    /// </summary>
    public class MKCommand : IMKCommand
    {
        /// <summary>
        ///     The command text
        /// </summary>
        private string commandText;

        /// <summary>
        ///     Initializes a new instance of the <see cref="MKCommand" /> class.
        /// </summary>
        public MKCommand()
        {
            Parameters = new MKCommandParameterCollection();
        }

        /// <summary>
        ///     Initializes a new instance of the <see cref="MKCommand" /> class.
        /// </summary>
        /// <param name="connection">The connection.</param>
        public MKCommand(MKConnection connection)
            : this()
        {
            Connection = connection;
        }

        /// <summary>
        ///     Initializes a new instance of the <see cref="MKCommand" /> class.
        /// </summary>
        /// <param name="connection">The connection.</param>
        /// <param name="commandText">The command text.</param>
        public MKCommand(MKConnection connection, string commandText)
            : this(connection)
        {
            CommandText = commandText;
        }

        /// <summary>
        ///     Gets or sets the command text.
        /// </summary>
        /// <remarks>
        ///     Command text can be in the API format (slash separated) or terminal format (space separated).
        ///     note that all parameters must add in the <see cref="Parameters" /> collection.
        /// </remarks>
        /// <value>The command text.</value>
        /// <example>
        ///     var command="interface pppoe-client add";
        ///     //or
        ///     var command=@"/interface/pppoe-client/add";
        /// </example>
        public string CommandText
        {
            get { return commandText; }
            set
            {
                commandText = value.Replace(" ", @"/");
                if (!commandText.StartsWith("/"))
                    commandText = @"/" + commandText;
            }
        }

        /// <summary>
        ///     Gets or sets the <see cref="MKConnection" />.
        /// </summary>
        /// <value>The connection.</value>
        public IMKConnection Connection { get; set; }

        /// <summary>
        ///     Gets or sets the parameters that will pass with the command.
        /// </summary>
        /// <value>The parameters.</value>
        /// <example>
        ///     var cmd = conn.CreateCommand("interface pppoe-client remove");
        ///     cmd.Parameters.Add(".id", "NormalUser");
        ///     cmd.Parameters.Add("disabled", "yes");
        /// </example>
        public MKCommandParameterCollection Parameters { get; set; }


        /// <summary>
        ///     Sends the Command, but does not read the the response.you should execute a read command whenever you want.
        /// </summary>
        /// <remarks>
        ///     this method is suitable for commands that will execute in background for a while, like ping, bandwidth-test etc.
        /// </remarks>
        /// <example>
        /// </example>
        public void ExecuteBackground()
        {
            verifyConnection();
            sendCommand();
        }

        /// <summary>
        ///     Executes the command against the connection.
        /// </summary>
        public void ExecuteNonQuery()
        {
            verifyConnection();
            sendCommand();
            var res = Connection.Read();
            checkResponse(res);
        }

        /// <summary>
        ///     Checks the response.
        /// </summary>
        /// <param name="res">The resource.</param>
        /// <exception cref="MKCommandException"></exception>
        /// <exception cref="MikrotikDotNet.Exceptions.MKCommandException"></exception>
        private void checkResponse(List<string> res)
        {
            var firstRow = res[0];
            if (firstRow.StartsWith("!trap") || firstRow.StartsWith("!fatal"))
            {
                var rowData = RowParser.Parse(firstRow);
                var exMessage = "";
                //if (MKResponseParser.HasField("category", firstRow))
                CommandFailureTypes errorCategory= CommandFailureTypes.GeneralFailure;
                if (rowData.ContainsKey("category"))
                {
                    var cat = int.Parse(rowData["category"]);
                    exMessage = "Category: " + (CommandFailureTypes)cat;
                    errorCategory = (CommandFailureTypes) cat;
                }
                exMessage += "\n" + rowData["message"];
                throw new MKCommandException(exMessage,errorCategory);
            }
            res.Remove("!done");
        }

        /// <summary>
        ///     Sends the command.
        /// </summary>
        private void sendCommand()
        {
            Connection.Send(CommandText);
            foreach (var parameter in Parameters)
            {
                Connection.Send(parameter.Serialize());
            }
            Connection.Push();
        }

        /// <summary>
        ///     Verifies the connection.
        /// </summary>
        /// <exception cref="ArgumentException">Connection object can not be null to excute command</exception>
        /// <exception cref="MikrotikDotNet.Exceptions.MKCommandException">Connection is not open</exception>
        private void verifyConnection()
        {
            if (Connection == null)
                throw new ArgumentException("Connection object can not be null to excute command");

            if (!Connection.IsOpen)
                throw new MKCommandException("Connection is not open");
        }




        /// <summary>
        ///     Gets the command text queries.
        /// </summary>
        /// <param name="commandText">The command text.</param>
        /// <returns>MKCommandParameterCollection.</returns>
        private MKCommandParameterCollection getCommandTextQueries(string commandText)
        {
            var query = new MKCommandParameterCollection();
            var idx = commandText.IndexOf(@"/where/");
            var parameters = commandText.Substring(idx, commandText.Length - idx)
                .Replace(@"/where/", "")
                .Split('=', ',');
            CommandText = commandText.Substring(0, idx);
            for (var i = 0; i < parameters.Length; i += 2)
            {
                query.Add(parameters[i], parameters[i + 1]);
            }

            return query;
        }


        /// <summary>
        ///     Excutes CommandText for read
        /// </summary>
        /// <param name="propList">
        ///     Optional:CSV of properies. limits number of Fileds that will be returned in result. it can
        ///     increase performance.
        /// </param>
        /// <param name="queryConditions">
        ///     Optional: Limits rows by condition on fields. Default logic is AND. You can change it in
        ///     Logic argument of this method
        /// </param>
        /// <param name="logic">The logic.</param>
        /// <returns>A collection of string in raw format of API result.</returns>
        public IEnumerable<string> ExecuteReader(string propList = null,
            MKCommandParameterCollection queryConditions = null, MKQueryLogicOperators logic = MKQueryLogicOperators.And)
        {
            verifyConnection();

            if (!string.IsNullOrEmpty(propList))
            {
                Parameters.Add(".proplist", propList);
            }
            //*******************************************

            if (CommandText.Contains(@"/where/"))
            {
                if (queryConditions == null)
                    queryConditions = new MKCommandParameterCollection();
                queryConditions.AddRange(getCommandTextQueries(CommandText));
            }

            if (queryConditions != null)
            {
                foreach (var q in queryConditions)
                {
                    q.Name = "?" + q.Name;
                    Parameters.Add(q);
                }
                if (queryConditions.Count > 1)
                {
                    switch (logic)
                    {
                        case MKQueryLogicOperators.And:
                            Parameters.Add("?#", "&");
                            break;

                        case MKQueryLogicOperators.Or:
                            Parameters.Add("?#", "|");

                            break;
                    }
                }
            }

            sendCommand();
            var res = Connection.Read();
            checkResponse(res);
            return res;
        }


        /// <summary>
        ///     Executes the command against the connection. reads and Creates Typed objects from the result.
        /// 
        /// </summary>
        /// <typeparam name="TType">The type of the t type.</typeparam>
        /// <param name="queryConditions">The query conditions.</param>
        /// <param name="logic">The logic.</param>
        /// <returns>IEnumerable&lt;TType&gt;.</returns>
        public IEnumerable<TType> ExecuteReader<TType>(MKCommandParameterCollection queryConditions,MKQueryLogicOperators logic)
        {
            var propList = string.Join(",", MKResponseParser.GetMkPropList<TType>());
            var rows = ExecuteReader(propList, queryConditions, logic);

            var result = MKResponseParser.GetList<TType>(rows);
            return result;
        }

        public IEnumerable<TType> ExecuteReader<TType>()
        {
            return ExecuteReader<TType>(null, MKQueryLogicOperators.And);
        }

        /// <summary>
        ///   Executes the command against the connection. reads and Creates dynamic objects from the result.
        /// </summary>
        /// <param name="queryConditions">The query conditions.</param>
        /// <param name="logic">The logic.</param>
        /// <returns>IEnumerable&lt;dynamic&gt;.</returns>
        public IEnumerable<dynamic> ExecuteReaderDynamic(MKCommandParameterCollection queryConditions ,
           MKQueryLogicOperators logic)
        {
            //var propList = string.Join(",", MKResponseParser.GetMkPropList<TType>());
            var rows = ExecuteReader(null, queryConditions, logic);

            var result = MKResponseParser.GetDynamicList(rows);
            return result;
        }

        public virtual IEnumerable<dynamic> ExecuteReaderDynamic()
        {
            return ExecuteReaderDynamic(null, MKQueryLogicOperators.And);
        }
    }
}

File: /Mikrotik.Net\MKCommandParameter.cs
﻿using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using MikrotikDotNet.ReponseParser;

namespace MikrotikDotNet
{
    public class MKCommandParameter
    {
        public string Name { get; set; }

        public string Value { get; set; }

        public string Serialize()
        {
            var prefix = "";
            if (!(Name.StartsWith("?") || Name.StartsWith("=")))
                prefix = "=";

            var opt = "=";
            if (Name.StartsWith("?#"))
                opt = "";

            return $"{prefix}{MemberNameHelper.PascalToTrain(Name)}{opt}{Value}";
        }

        public MKCommandParameter(string name, string value)
        {
            this.Name = name;
            this.Value = value;
        }
    }
}


File: /Mikrotik.Net\MKCommandParameterCollection.cs
﻿using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace MikrotikDotNet
{
    public class MKCommandParameterCollection : List<MKCommandParameter>
    {
        public void Add(string name, string value)
        {
            this.Add(new MKCommandParameter(name, value));
        }
    }
}


File: /Mikrotik.Net\MKConnection.cs
﻿using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Net.Sockets;
using System.Text;
using System.Threading.Tasks;
using MikrotikDotNet.Exceptions;

namespace MikrotikDotNet
{


    /// <summary>
    /// Represents an open connection to Mikrotik server. This class can not be inherited.
    /// </summary>
    public sealed class MKConnection : IDisposable, IEquatable<MKConnection>, IMKConnection
    {
        public Guid GUID { get; private set; }

        private TcpClient con;
        private Stream connection;

        public MKConnection(string host, string username, string password)
        {
            init(host, username, password, 8728);
        }


        public MKConnection(string host, string username, string password, int port)
        {
            init(host, username, password, port);
        }

        private void init(string host, string username, string password, int port)
        {
            GUID = Guid.NewGuid();
            con = new TcpClient();
            Host = host;
            UserName = username;
            Password = password;
            Port = port;
        }


        public string Host { get; set; }

        public bool IsOpen { get; private set; }

        public string Password { get; set; }

        public string UserName { get; set; }

        public int Port { get; set; }

        public void Close()
        {
            connection.Close();
            con.Close();
        }

        public void Dispose()
        {
            connection.Close();
            con.Close();
            connection.Dispose();
        }

        public string EncodePassword(string Password, string hash)
        {
            byte[] hash_byte = new byte[hash.Length / 2];
            for (int i = 0; i <= hash.Length - 2; i += 2)
            {
                hash_byte[i / 2] = Byte.Parse(hash.Substring(i, 2), System.Globalization.NumberStyles.HexNumber);
            }
            byte[] heslo = new byte[1 + Password.Length + hash_byte.Length];
            heslo[0] = 0;
            Encoding.ASCII.GetBytes(Password.ToCharArray()).CopyTo(heslo, 1);
            hash_byte.CopyTo(heslo, 1 + Password.Length);

            Byte[] hotovo;
            System.Security.Cryptography.MD5 md5;

            md5 = new System.Security.Cryptography.MD5CryptoServiceProvider();

            hotovo = md5.ComputeHash(heslo);

            //Convert encoded bytes back to a 'readable' string
            string navrat = "";
            foreach (byte h in hotovo)
            {
                navrat += h.ToString("x2");
            }
            return navrat;
        }

        public void Open()
        {

            if (string.IsNullOrEmpty(Host) || string.IsNullOrEmpty(UserName) || Port == 0)
            {
                throw new ArgumentNullException(
                    "Host, Username and Port must have a value. Please initiate them first.");
            }

            try
            {
                con.Connect(Host, Port);
                connection = (Stream)con.GetStream();
            }
            catch (SocketException)
            {
                throw new MKConnectionException(string.Format("Can not connect to {0}.", Host));
            }

            Send("/login");
            Push();
            string hash = Read()[0].Split(new string[] { "ret=" }, StringSplitOptions.None)[1];
            string errorMsg = "";
            Send("/login");
            Send("=name=" + UserName);
            try
            {
                Send("=password=" + Password);
            }
            catch (Exception)
            {
                throw new MKConnectionException(string.Format("Invalid UserName or Password failed for {0} With User:{1} and Pass:{2}.", Host, UserName, Password));
            }
            try
            {
                Send("=response=00" + EncodePassword(Password, hash));
            }
            catch (Exception)
            {
                throw new MKConnectionException(string.Format("Invalid UserName or Password failed for {0} With User:{1} and Pass:{2}.", Host, UserName, Password));
            }

            Push();

            if (Read()[0] != "!done")
            {
                throw new MKConnectionException(string.Format("Invalid UserName or Password failed for {0} With User:{1} and Pass:{2}.", Host, UserName, Password));
            }
            IsOpen = true;
        }

        public void Open(string host, string username, string password, int port)
        {
            init(host,username,password,port);
            Open();
        }

        public void Push()
        {
            connection.WriteByte(0);
        }

        public List<string> Read()
        {
            List<string> output = new List<string>();
            string o = "";
            byte[] tmp = new byte[4];
            long count;
            while (true)
            {
                tmp[3] = (byte)connection.ReadByte();
                //if(tmp[3] == 220) tmp[3] = (byte)connection.ReadByte(); it sometimes happend to me that
                //mikrotik send 220 as some kind of "bonus" between words, this fixed things, not sure about it though
                if (tmp[3] == 0)
                {
                    output.Add(o);
                    if (o.Substring(0, 5) == "!done")
                    {
                        break;
                    }
                    else
                    {
                        o = "";
                        continue;
                    }
                }
                else
                {
                    if (tmp[3] < 0x80)
                    {
                        count = tmp[3];
                    }
                    else
                    {
                        if (tmp[3] < 0xC0)
                        {
                            int tmpi = BitConverter.ToInt32(new byte[] { (byte)connection.ReadByte(), tmp[3], 0, 0 }, 0);
                            count = tmpi ^ 0x8000;
                        }
                        else
                        {
                            if (tmp[3] < 0xE0)
                            {
                                tmp[2] = (byte)connection.ReadByte();
                                int tmpi = BitConverter.ToInt32(new byte[] { (byte)connection.ReadByte(), tmp[2], tmp[3], 0 }, 0);
                                count = tmpi ^ 0xC00000;
                            }
                            else
                            {
                                if (tmp[3] < 0xF0)
                                {
                                    tmp[2] = (byte)connection.ReadByte();
                                    tmp[1] = (byte)connection.ReadByte();
                                    int tmpi = BitConverter.ToInt32(new byte[] { (byte)connection.ReadByte(), tmp[1], tmp[2], tmp[3] }, 0);
                                    count = tmpi ^ 0xE0000000;
                                }
                                else
                                {
                                    if (tmp[3] == 0xF0)
                                    {
                                        tmp[3] = (byte)connection.ReadByte();
                                        tmp[2] = (byte)connection.ReadByte();
                                        tmp[1] = (byte)connection.ReadByte();
                                        tmp[0] = (byte)connection.ReadByte();
                                        count = BitConverter.ToInt32(tmp, 0);
                                    }
                                    else
                                    {
                                        //Error in packet reception, unknown length
                                        break;
                                    }
                                }
                            }
                        }
                    }
                }

                for (int i = 0; i < count; i++)
                {
                    o += (Char)connection.ReadByte();
                }
            }
            return output;
        }

        public void Send(string co)
        {
            byte[] bajty = Encoding.ASCII.GetBytes(co.ToCharArray());
            byte[] velikost = EncodeLength(bajty.Length);

            connection.Write(velikost, 0, velikost.Length);
            connection.Write(bajty, 0, bajty.Length);
        }

        private byte[] EncodeLength(int delka)
        {
            if (delka < 0x80)
            {
                byte[] tmp = BitConverter.GetBytes(delka);
                return new byte[1] { tmp[0] };
            }
            if (delka < 0x4000)
            {
                byte[] tmp = BitConverter.GetBytes(delka | 0x8000);
                return new byte[2] { tmp[1], tmp[0] };
            }
            if (delka < 0x200000)
            {
                byte[] tmp = BitConverter.GetBytes(delka | 0xC00000);
                return new byte[3] { tmp[2], tmp[1], tmp[0] };
            }
            if (delka < 0x10000000)
            {
                byte[] tmp = BitConverter.GetBytes(delka | 0xE0000000);
                return new byte[4] { tmp[3], tmp[2], tmp[1], tmp[0] };
            }
            else
            {
                byte[] tmp = BitConverter.GetBytes(delka);
                return new byte[5] { 0xF0, tmp[3], tmp[2], tmp[1], tmp[0] };
            }
        }

        public IMKCommand CreateCommand()
        {
            return new MKCommand(this);
        }

        public IMKCommand CreateCommand(string commandText)
        {
            return new MKCommand(this, commandText);
        }

        public bool Equals(MKConnection other)
        {
            return this.GUID == other.GUID;
        }
    }
}


File: /Mikrotik.Net\MKQueryLogicOperators.cs
﻿using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace MikrotikDotNet
{
    public enum MKQueryLogicOperators
    {
        And,
        Or
    }
}


File: /Mikrotik.Net\ReponseParser\MemberNameHelper.cs
﻿using System.Globalization;
using System.Text.RegularExpressions;

namespace MikrotikDotNet.ReponseParser
{
    public class MemberNameHelper
    {
        public static string TrainToPascal(string name)
        {
            TextInfo textInfo = new CultureInfo("en-US", false).TextInfo;
            return textInfo.ToTitleCase(name.Replace("-", " ")).Replace(" ",string.Empty).Replace(".",string.Empty);
        }

        public static string PascalToTrain(string name)
        {
            if (name.ToLower() == "mkid")
                return ".id";

            return Regex.Replace(name, "(\\B[A-Z])", "-$1").ToLower();
        }
    }
}

File: /Mikrotik.Net\ReponseParser\MKResponseParser.cs
﻿using System;
using System.Collections.Generic;
using System.Dynamic;
using System.Text.RegularExpressions;
using MikrotikDotNet.Exceptions;

namespace MikrotikDotNet.ReponseParser
{
    public static class MKResponseParser
    {


        public static TType GetObject<TType>(string row)
        {


            var rowData = RowParser.Parse(row);



            var resObj = Activator.CreateInstance<TType>();

            foreach (var prop in typeof(TType).GetProperties())
            {



                var mkField = MemberNameHelper.PascalToTrain(prop.Name);
                if (!rowData.ContainsKey(mkField))
                    continue;

                var fieldVal = rowData[mkField];

                var propType = prop.PropertyType;

                var propVal = Convert.ChangeType(fieldVal, propType);
                prop.SetValue(resObj, propVal);
            }
            return resObj;
        }


        public static dynamic GetDynamicObject(string row)
        {
            var rowData = RowParser.Parse(row);
            return createDynamicObject(rowData);
        }
        private static dynamic createDynamicObject(Dictionary<string, string> rowData)
        {
            var res = new ExpandoObject() as IDictionary<string, Object>;


            foreach (var field in rowData.Keys)
                res.Add(MemberNameHelper.TrainToPascal(field), rowData[field]);

            return res;
        }






        public static IEnumerable<TType> GetList<TType>(IEnumerable<string> rows)
        {
            var lst = new List<TType>();
            foreach (var row in rows)
            {
                if (!row.StartsWith("!trap"))
                    lst.Add(GetObject<TType>(row));
            }
            return lst;
        }

        public static IEnumerable<string> GetMkPropList<TType>()
        {
            var lst = new List<string>();
            foreach (var prop in typeof(TType).GetProperties())
            {
                lst.Add(MemberNameHelper.PascalToTrain(prop.Name));
            };
            return lst;
        }

        public static IEnumerable<dynamic> GetDynamicList(IEnumerable<string> rows)
        {

            foreach (var row in rows)
            {
                var rowData = RowParser.Parse(row);
                yield return createDynamicObject(rowData);

            }

        }
    }
}


File: /Mikrotik.Net\ReponseParser\RowParser.cs
﻿using System.Collections.Generic;

namespace MikrotikDotNet.ReponseParser
{
    public class RowParser
    {
        public static Dictionary<string, string> Parse(string row)
        {
            var res = new Dictionary<string, string>();
            //var fields = new List<string>();
            //var values = new List<string>();

            int start = 0, end;
            do
            {
                start = row.IndexOf("=", start + 1);
                end = row.IndexOf("=", start + 1);
                var field = row.Substring(start + 1, end - start - 1);

                start = end;

                //------------------- value
                var value = "";
                var valueLen = row.IndexOf("=", end + 1) - end - 1;
                if (valueLen >= 0)
                    value = row.Substring(end + 1, valueLen);
                else
                    value = row.Substring(end + 1, row.Length - end-1);

                res.Add(field, value);
            } while (end < row.LastIndexOf("="));
            return res;
        }
    }
}

File: /Mikrotik.Net.UnitTest\Mikrotik.Net.UnitTest.csproj
<Project Sdk="Microsoft.NET.Sdk">

  <PropertyGroup>
    <TargetFramework>netstandard2.0</TargetFramework>
  </PropertyGroup>

  <ItemGroup>
    <PackageReference Include="Microsoft.CSharp" Version="4.7.0" />
    <PackageReference Include="xunit" Version="2.4.1" />
  </ItemGroup>

  <ItemGroup>
    <ProjectReference Include="..\Mikrotik.Net\Mikrotik.Net.csproj" />
  </ItemGroup>

</Project>


File: /Mikrotik.Net.UnitTest\MkResponseParserTests\Given_Response_Parser.cs
﻿namespace Mikrotik.Net.UnitTest.MkResponseParserTests
{
    public class Given_Response_Parser
    {
   

    }
}

File: /Mikrotik.Net.UnitTest\MkResponseParserTests\When_Parsing_Dynamic_Object.cs
﻿using MikrotikDotNet.ReponseParser;
using Xunit;

namespace Mikrotik.Net.UnitTest.MkResponseParserTests
{
    public class When_Parsing_Dynamic_Object : Given_Response_Parser
    {
     
       

        [Fact]
        public void Then_Can_Return_Correct_Response()
        {
            var row =
                "!re=.id=*1FE=name=NormalUser=max-mtu=1480=max-mru=1480=mrru=disabled=interface=ether1=user==password=123=profile=default=keepalive-timeout=60=service-name==ac-name==add-default-route=false=dial-on-demand=false=use-peer-dns=false=allow=pap,chap,mschap1,mschap2=running=false=disabled=true";

            dynamic response = MKResponseParser.GetDynamicObject(row);

            Assert.Equal(response.Id, "*1FE");
            Assert.Equal(response.Name, "NormalUser");
            Assert.Equal(response.Disabled, "true");
            Assert.Equal(response.Running, "false");
            Assert.Equal(response.KeepaliveTimeout, "60");
        }
    }
}

File: /Mikrotik.Net.UnitTest\MkResponseParserTests\When_Parsing_Typed_Object.cs
﻿using MikrotikDotNet.ReponseParser;
using Xunit;

namespace Mikrotik.Net.UnitTest.MkResponseParserTests
{
    public class When_Parsing_Typed_Object : Given_Response_Parser
    {

        class TestModel
        {
            public string A { get; set; }
            public string B { get; set; }
            public string C { get; set; }

        }


        [Fact]
        public void Then_Ignores_Fields_That_Are_Not_Avaliable_In_Object_Type()
        {
            var responseText = "!re=a=a=b=b=x=x";
            var res = MKResponseParser.GetObject<TestModel>(responseText);

            Assert.Equal("a", res.A);
            Assert.Equal("b", res.B);
            Assert.Equal(null, res.C);
        }

        [Fact]
        public void Then_Ignores_Properties_That_Are_Not_Avaliable_In_Input_String()
        {
            var responseText = "!re=a=a=b=b";
            var res = MKResponseParser.GetObject<TestModel>(responseText);

            Assert.Equal("a", res.A);
            Assert.Equal("b", res.B);
            Assert.Equal(null, res.C);
        }


        [Fact]
        public void Then_Maps_Properites_That_Are_Avaliable()
        {
            var responseText = "!re=a=a=b=b=c=c";
            var res = MKResponseParser.GetObject<TestModel>(responseText);

            Assert.Equal("a",res.A);
            Assert.Equal("b",res.B);
            Assert.Equal("c",res.C);

        }

    }
}

File: /Mikrotik.Net.UnitTest\StringTools.cs
﻿namespace Mikrotik.Net.UnitTest
{
    public static class StringTools
    {
        public static string ExtractBetween(this string str, string startTag, string endTag, bool inclusive)
        {
            string rtn = null;

            int s = str.IndexOf(startTag);
            if (s >= 0)
            {
                if (!inclusive)
                    s += startTag.Length;

                int e = str.IndexOf(endTag, s);
                if (e > s)
                {
                    if (inclusive)
                        e += startTag.Length;

                    rtn = str.Substring(s, e - s);
                }
            }

            return rtn;
        }
    }
}

File: /MikrotikDotNet.sln
﻿
Microsoft Visual Studio Solution File, Format Version 12.00
# Visual Studio Version 17
VisualStudioVersion = 17.0.31919.166
MinimumVisualStudioVersion = 10.0.40219.1
Project("{FAE04EC0-301F-11D3-BF4B-00C04F79EFBC}") = "Mikrotik.Net", "Mikrotik.Net\Mikrotik.Net.csproj", "{039CB199-8D64-4733-BE09-BCEEDB6051CB}"
EndProject
Project("{FAE04EC0-301F-11D3-BF4B-00C04F79EFBC}") = "Mikrotik.Net.UnitTest", "Mikrotik.Net.UnitTest\Mikrotik.Net.UnitTest.csproj", "{DB61A740-FA5E-4979-99E7-6F3DE4F91EA1}"
EndProject
Global
	GlobalSection(SolutionConfigurationPlatforms) = preSolution
		Debug|Any CPU = Debug|Any CPU
		Release|Any CPU = Release|Any CPU
	EndGlobalSection
	GlobalSection(ProjectConfigurationPlatforms) = postSolution
		{039CB199-8D64-4733-BE09-BCEEDB6051CB}.Debug|Any CPU.ActiveCfg = Debug|Any CPU
		{039CB199-8D64-4733-BE09-BCEEDB6051CB}.Debug|Any CPU.Build.0 = Debug|Any CPU
		{039CB199-8D64-4733-BE09-BCEEDB6051CB}.Release|Any CPU.ActiveCfg = Release|Any CPU
		{039CB199-8D64-4733-BE09-BCEEDB6051CB}.Release|Any CPU.Build.0 = Release|Any CPU
		{DB61A740-FA5E-4979-99E7-6F3DE4F91EA1}.Debug|Any CPU.ActiveCfg = Debug|Any CPU
		{DB61A740-FA5E-4979-99E7-6F3DE4F91EA1}.Debug|Any CPU.Build.0 = Debug|Any CPU
		{DB61A740-FA5E-4979-99E7-6F3DE4F91EA1}.Release|Any CPU.ActiveCfg = Release|Any CPU
		{DB61A740-FA5E-4979-99E7-6F3DE4F91EA1}.Release|Any CPU.Build.0 = Release|Any CPU
	EndGlobalSection
	GlobalSection(SolutionProperties) = preSolution
		HideSolutionNode = FALSE
	EndGlobalSection
	GlobalSection(ExtensibilityGlobals) = postSolution
		SolutionGuid = {14657D93-A0D8-44A3-B992-557F5F075132}
	EndGlobalSection
	GlobalSection(CodealikeProperties) = postSolution
		SolutionGuid = 16b0ed00-5ac8-44de-b2f2-86b4a53f0be2
	EndGlobalSection
EndGlobal


File: /NewAuthenticationMode
                            ****************Pay Attention****************
Login method post-v6.43:

For Using MikrotikDotNet  you Must  Update the firmware to 6.43 or higher


File: /README.md
# MikrotikDotNet
MikrotikDotNet is a lightweight and easy to use ADO.NET like library for Mikrotik Api with extensibility and performance in mind.

[NuGet package:](https://www.nuget.org/packages/Mikrotik.Net)
```
Install-Package Mikrotik.Net
```

## How to use:
Simple command with parameters (ExecuteNonQuery):
```cs
using (var conn = new MKConnection(IPADDRESS, USERNAME, PASSWORD))
{
    conn.Open();
    var cmd = conn.CreateCommand("interface pppoe-client add");
    cmd.Parameters.Add("interface", "ether1");
    cmd.Parameters.Add("Name", "Test"); // You can use PascalCase or kebab-case in parameter name.
    cmd.Parameters.Add("user","Test");
    cmd.Parameters.Add("password", "Test");
    cmd.ExecuteNonQuery();
}
```

Read response: (ExecuteReader):
```cs
using (var conn = new MKConnection(IPADDRESS, USERNAME, PASSWORD))
{
  conn.Open();
  var cmd = conn.CreateCommand("ip address print");
  var result = cmd.ExecuteReader();
  foreach (var line in result)
    Console.WriteLine(line);
  
}
```
Result (Raw api response):
```
!re=.id=*4=address=10.20.1.19/16=network=10.20.0.0=interface=bridge1=actual-interface=bridge1=invalid=false=dynamic=false=disabled=false
!re=.id=*5=address=172.16.0.1/30=network=172.16.0.0=interface=bridge1=actual-interface=bridge1=invalid=false=dynamic=false=disabled=false
!re=.id=*6=address=172.19.1.19/19=network=172.19.0.0=interface=bridge1=actual-interface=bridge1=invalid=false=dynamic=false=disabled=false
```

To query data at API level:

Filtering at API level decreases network payload and improves the performance.

```cs
using (var conn = new MKConnection(IPADDRESS, USERNAME, PASSWORD))
{
     conn.Open();
     var cmd = conn.CreateCommand("ip address print where address=172.16.0.1/30");
     var result = cmd.ExecuteReader();
     foreach (var line in result)
          Console.WriteLine(line);

}
```

Result:

```
!re=.id=*5=address=172.16.0.1/30=network=172.16.0.0=interface=bridge1=actual-nterface=bridge1=invalid=false=dynamic=false=disabled=false
```

Or:

```cs
using (var conn = new MKConnection(IPADDRESS, USERNAME, PASSWORD))
{
conn.Open();
var cmd = conn.CreateCommand("ip address print");
var condition = new MKCommandParameterCollection()
{
     new MKCommandParameter("address","172.16.0.1/3"),
     new MKCommandParameter("address","172.19.1.19/19")
};

var result = cmd.ExecuteReader(queryConditions: condition, logic: MKQueryLogicOperators.Or);
foreach (var line in result)
     Console.WriteLine(line);

}


```

Result:
```
!re=.id=*5=address=172.16.0.1/30=network=172.16.0.0=interface=bridge1=actual-nterface=bridge1=invalid=false=dynamic=false=disabled=false
!re=.id=*6=address=172.19.1.19/19=network=172.19.0.0=interface=bridge1=actual-interface=bridge1=invalid=false=dynamic=false=disabled=false
```

To deserialize response: (ExecuteReader<T>)
```cs
class MyIpAddress
{
    public string MKID { get; set; }  //MKID always referce to .id field in response.
    public string Address { get; set; } // Use PascalCase naming style for properties. it will convert from/to kebab-case naming.
    public string Interface { get; set; }
}
//------------------------------------------------
using (var conn = new MKConnection(IPADDRESS, USERNAME, PASSWORD))
{
    conn.Open();
    var cmd = conn.CreateCommand("ip address print");
    var result = cmd.ExecuteReader<MyIpAddress>();

    foreach (var ip in result)
        Console.WriteLine($"{ip.MKID} - {ip.Address} - {ip.Interface}");

}

```
Result:
```
*4 - 10.20.1.19/16 - bridge1
*5 - 172.16.0.1/30 - bridge1
*6 - 172.19.1.19/19 - bridge1
```
>Note: Using method ExecuteReader<T> only reads the fields that are present is the given type, using the .proplist field in query.


To get dynamic object response: (ExecuteReaderDynamic)
you can get response object without defining any model class.

```cs

using (var conn = new MKConnection(IPADDRESS, USERNAME, PASSWORD))
{
    conn.Open();
    var cmd = conn.CreateCommand("ip address print");
    var result = cmd.ExecuteReaderDynamic();

    foreach (var ip in result)
        Console.WriteLine($"{ip.Id} - {ip.Address} - {ip.Interface}"); //MKID switched to Id
}

```
Result:
```
*4 - 10.20.1.19/16 - bridge1
*5 - 172.16.0.1/30 - bridge1
*6 - 172.19.1.19/19 - bridge1
```
>Note: Using method ExecuteReaderDynamic reads all fields from the router it will increase response payload.

Read data from background commands: (ExecuteBackground)
Some commands works in background ( like ping,bandwith test, discovert,...)

```cs
using (var conn = new MKConnection(IPADDRESS, USERNAME, PASSWORD))
{
    conn.Open();
    var cmd = conn.CreateCommand("ping");
    cmd.Parameters.Add("address", "10.20.0.4");
    cmd.Parameters.Add("count", "3");
    cmd.Parameters.Add("interval", "1");
    cmd.ExecuteBackground();

    Thread.Sleep(5000); 
    
    var result = cmd.ExecuteReaderDynamic();
    foreach (var ip in result)
        Console.WriteLine($"{ip.Host} - {ip.Time} - {ip.Ttl}");

}
```


Result:
```
10.20.0.4 - 13ms - 128
10.20.0.4 - 6ms - 128
10.20.0.4 - 4ms - 128
```



