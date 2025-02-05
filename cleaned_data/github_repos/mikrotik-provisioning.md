# Repository Information
Name: mikrotik-provisioning

# Directory Structure
Directory structure:
└── github_repos/mikrotik-provisioning/
    ├── .dockerignore
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
    │   │       ├── pack-68fe686bd718116f1febca5abfc388c2b40314a5.idx
    │   │       └── pack-68fe686bd718116f1febca5abfc388c2b40314a5.pack
    │   ├── packed-refs
    │   └── refs/
    │       ├── heads/
    │       │   └── master
    │       ├── remotes/
    │       │   └── origin/
    │       │       └── HEAD
    │       └── tags/
    ├── .gitignore
    ├── .golangci.yml
    ├── cmd/
    │   └── mikrotik_provisioning/
    │       └── main.go
    ├── go.mod
    ├── go.sum
    ├── internal/
    │   ├── app/
    │   │   └── mikrotik_provisioning.go
    │   ├── config/
    │   │   └── config.go
    │   └── pkg/
    │       ├── address_list/
    │       │   └── address_list.go
    │       ├── errors/
    │       │   └── errors.go
    │       ├── http/
    │       │   ├── address_list.go
    │       │   ├── errors.go
    │       │   ├── handler.go
    │       │   ├── middleware/
    │       │   │   └── middleware.go
    │       │   ├── response.go
    │       │   └── types.go
    │       └── repository/
    │           └── mongo/
    │               ├── address_list.go
    │               ├── indexes.go
    │               └── mongo.go
    ├── pkg/
    │   └── validator/
    │       └── validator.go
    ├── scripts/
    │   ├── docker-compose.yml
    │   └── Dockerfile
    └── templates/
        ├── GetAddressList
        └── GetAddressLists


# Content
File: /.dockerignore
/.idea
/.mongo
/scripts
config.yml

File: /.git\config
[core]
	repositoryformatversion = 0
	filemode = false
	bare = false
	logallrefupdates = true
	symlinks = false
	ignorecase = true
[remote "origin"]
	url = https://github.com/oGi4i/mikrotik-provisioning.git
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
0000000000000000000000000000000000000000 7d67cde2a17cbdca21226607a9888005a3044ed4 vivek-dodia <vivek.dodia@icloud.com> 1738606402 -0500	clone: from https://github.com/oGi4i/mikrotik-provisioning.git


File: /.git\logs\refs\heads\master
0000000000000000000000000000000000000000 7d67cde2a17cbdca21226607a9888005a3044ed4 vivek-dodia <vivek.dodia@icloud.com> 1738606402 -0500	clone: from https://github.com/oGi4i/mikrotik-provisioning.git


File: /.git\logs\refs\remotes\origin\HEAD
0000000000000000000000000000000000000000 7d67cde2a17cbdca21226607a9888005a3044ed4 vivek-dodia <vivek.dodia@icloud.com> 1738606402 -0500	clone: from https://github.com/oGi4i/mikrotik-provisioning.git


File: /.git\packed-refs
# pack-refs with: peeled fully-peeled sorted 
7d67cde2a17cbdca21226607a9888005a3044ed4 refs/remotes/origin/master


File: /.git\refs\heads\master
7d67cde2a17cbdca21226607a9888005a3044ed4


File: /.git\refs\remotes\origin\HEAD
ref: refs/remotes/origin/master


File: /.gitignore
/.idea
/.mongo
config.yml

File: /.golangci.yml
# More info on config here: https://github.com/golangci/golangci-lint#config-file
run:
  deadline: 5m
  issues-exit-code: 1
  tests: true
  skip-dirs:
    - bin
    - vendor
    - var
    - tmp
  skip-files:
    - \.pb\.go$
    - \.pb\.goclay\.go$

output:
  format: colored-line-number
  print-issued-lines: true
  print-linter-name: true

linters-settings:
  govet:
    check-shadowing: true
  golint:
    min-confidence: 0
  goconst:
    min-len:         2
    min-occurrences: 2
  goimports:
    local-prefixes: mikrotik_provisioning
  errchek:
    check-type-assertions: false
  nakedret:
    max-func-lines: 30
  gocritic:
    enabled-checks:
      - appendAssign
      - caseOrder
      - dupArg
      - dupBranchBody
      - dupCase
      - dupSubExpr
      - flagDeref
      - assignOp
      - captLocal
      - defaultCaseOrder
      - elseif
      - ifElseChain
      - regexpMust
      - singleCaseSwitch
      - sloppyLen
      - switchTrue
      - typeSwitchVar
      - underef
      - unslice
      - commentedOutCode
      - commentedOutImport

linters:
  disable-all: true
  enable:
    - gocritic
    - golint
    - govet
    - errcheck
    - deadcode
    - dupl
    - structcheck
    - varcheck
    - ineffassign
    - typecheck
    - goconst
    - goimports
    - megacheck # (staticcheck + gosimple + unused in one linter)
    - gosec
    - unparam
    - bodyclose
    - unconvert

issues:
  exclude-use-default: false
  exclude:
    # _ instead of err checks
    - G104
    - G101
    # for "public interface + private struct implementation" cases only!
    - exported func * returns unexported type *, which can be annoying to use
    # can be removed in the development phase
    # - (comment on exported (method|function|type|const)|should have( a package)? comment|comment should be of the form)
    # not for the active development - can be removed in the stable phase
    - should have a package comment, unless it's in another file for this package
    - don't use an underscore in package name
    # errcheck: Almost all programs ignore errors on these functions and in most cases it's ok
    - Error return value of .((os\.)?std(out|err)\..*|.*Close|.*Flush|os\.Remove(All)?|.*printf?|os\.(Un)?Setenv|.*Rollback). is not checked
    - should check returned error before deferring
    # golint: Allow "userId", and not "userID"
    # - (var|const|struct|method|func) (.+) should be (.+)
    - should have comment
    - is a pure function but its return value is ignored
    # golint: allow any comments
    - comment on exported type (.+) should be of the form (.+)
    # golint: allow capitalized errors
    # - error strings should not be capitalized or end with punctuation or a newline


File: /cmd\mikrotik_provisioning\main.go
package main

import (
	"context"
	"log"
	"net/http"
	"path/filepath"
	"text/template"

	"github.com/go-chi/chi"
	"github.com/go-chi/chi/middleware"
	"github.com/go-chi/render"

	"mikrotik_provisioning/internal/app"
	"mikrotik_provisioning/internal/config"
	mux "mikrotik_provisioning/internal/pkg/http"
	mw "mikrotik_provisioning/internal/pkg/http/middleware"
	"mikrotik_provisioning/internal/pkg/repository/mongo"
)

func main() {
	config, err := config.ParseConfig()
	if err != nil {
		log.Fatalf("failed to parse config file with error: %q\n", err)
	}

	templateFiles, err := filepath.Glob("templates/*")
	if err != nil {
		log.Fatalf("failed to get template filenames with glob with error: %q\n", err)
	}

	templates := new(template.Template)
	templates, err = templates.Delims("#(", ")#").ParseFiles(templateFiles...)
	if err != nil {
		log.Fatalf("failed to parse template files with error: %q\n", err)
	}

	ctx := context.Background()
	mongoStore, err := mongo.NewMongoStorage(ctx, config.DB)
	if err != nil {
		log.Fatalf("failed to initialize MongoStore with error: %q\n", err)
	}

	service := app.NewMikrotikProvisioningService(mongoStore)
	mw := mw.NewMiddleware(service, config.Access)
	handler := mux.NewAddressListHandler(service, templates)

	r := chi.NewRouter()
	r.Use(middleware.Logger)
	r.Use(middleware.Recoverer)
	r.Use(middleware.AllowContentType("application/json"))
	r.Use(mw.CheckAcceptHeader("*/*", "application/json", "text/plain"))
	r.Use(render.SetContentType(render.ContentTypeJSON))

	r.Route("/address-list", func(r chi.Router) {
		r.Get("/", handler.GetAddressLists)                                                            // GET /address-list
		r.With(mw.EnsureAuth).With(mw.EnsureAddressListNotExists).Post("/", handler.CreateAddressList) // POST /address-list

		r.Route("/{addressListName:[A-Za-z0-9-]+}", func(r chi.Router) {
			r.With(mw.EnsureAddressListExists).Get("/", handler.GetAddressList)                           // GET /address-list/whats-up
			r.With(mw.EnsureAuth).With(mw.EnsureAddressListExists).Put("/", handler.UpdateAddressList)    // PUT /address-list/whats-up
			r.With(mw.EnsureAuth).With(mw.EnsureAddressListExists).Patch("/", handler.PatchAddressList)   // PATCH /address-list/whats-up
			r.With(mw.EnsureAuth).With(mw.EnsureAddressListExists).Delete("/", handler.DeleteAddressList) // DELETE /address-list/whats-up
		})
	})

	err = http.ListenAndServe(":3333", r)
	if err != nil {
		log.Fatalf("failed to initialize http server with error: %q\n", err)
	}
}


File: /go.mod
module mikrotik_provisioning

go 1.15

require (
	github.com/go-chi/chi v4.1.2+incompatible
	github.com/go-chi/render v1.0.1
	github.com/go-playground/universal-translator v0.17.0 // indirect
	github.com/leodido/go-urn v1.2.0 // indirect
	go.mongodb.org/mongo-driver v1.4.0
	gopkg.in/go-playground/assert.v1 v1.2.1 // indirect
	gopkg.in/go-playground/validator.v9 v9.31.0
	gopkg.in/yaml.v2 v2.3.0
)


File: /go.sum
github.com/BurntSushi/toml v0.3.1/go.mod h1:xHWCNGjB5oqiDr8zfno3MHue2Ht5sIBksp03qcyfWMU=
github.com/aws/aws-sdk-go v1.29.15 h1:0ms/213murpsujhsnxnNKNeVouW60aJqSd992Ks3mxs=
github.com/aws/aws-sdk-go v1.29.15/go.mod h1:1KvfttTE3SPKMpo8g2c6jL3ZKfXtFvKscTgahTma5Xg=
github.com/davecgh/go-spew v1.1.0 h1:ZDRjVQ15GmhC3fiQ8ni8+OwkZQO4DARzQgrnXU1Liz8=
github.com/davecgh/go-spew v1.1.0/go.mod h1:J7Y8YcW2NihsgmVo/mv3lAwl/skON4iLHjSsI+c5H38=
github.com/davecgh/go-spew v1.1.1 h1:vj9j/u1bqnvCEfJOwUhtlOARqs3+rkHYY13jYWTU97c=
github.com/davecgh/go-spew v1.1.1/go.mod h1:J7Y8YcW2NihsgmVo/mv3lAwl/skON4iLHjSsI+c5H38=
github.com/go-chi/chi v4.1.2+incompatible h1:fGFk2Gmi/YKXk0OmGfBh0WgmN3XB8lVnEyNz34tQRec=
github.com/go-chi/chi v4.1.2+incompatible/go.mod h1:eB3wogJHnLi3x/kFX2A+IbTBlXxmMeXJVKy9tTv1XzQ=
github.com/go-chi/render v1.0.1 h1:4/5tis2cKaNdnv9zFLfXzcquC9HbeZgCnxGnKrltBS8=
github.com/go-chi/render v1.0.1/go.mod h1:pq4Rr7HbnsdaeHagklXub+p6Wd16Af5l9koip1OvJns=
github.com/go-playground/locales v0.13.0 h1:HyWk6mgj5qFqCT5fjGBuRArbVDfE4hi8+e8ceBS/t7Q=
github.com/go-playground/locales v0.13.0/go.mod h1:taPMhCMXrRLJO55olJkUXHZBHCxTMfnGwq/HNwmWNS8=
github.com/go-playground/universal-translator v0.17.0 h1:icxd5fm+REJzpZx7ZfpaD876Lmtgy7VtROAbHHXk8no=
github.com/go-playground/universal-translator v0.17.0/go.mod h1:UkSxE5sNxxRwHyU+Scu5vgOQjsIJAF8j9muTVoKLVtA=
github.com/go-sql-driver/mysql v1.5.0/go.mod h1:DCzpHaOWr8IXmIStZouvnhqoel9Qv2LBy8hT2VhHyBg=
github.com/go-stack/stack v1.8.0 h1:5SgMzNM5HxrEjV0ww2lTmX6E2Izsfxas4+YHWRs3Lsk=
github.com/go-stack/stack v1.8.0/go.mod h1:v0f6uXyyMGvRgIKkXu+yp6POWl0qKG85gN/melR3HDY=
github.com/gobuffalo/attrs v0.0.0-20190224210810-a9411de4debd/go.mod h1:4duuawTqi2wkkpB4ePgWMaai6/Kc6WEz83bhFwpHzj0=
github.com/gobuffalo/depgen v0.0.0-20190329151759-d478694a28d3/go.mod h1:3STtPUQYuzV0gBVOY3vy6CfMm/ljR4pABfrTeHNLHUY=
github.com/gobuffalo/depgen v0.1.0/go.mod h1:+ifsuy7fhi15RWncXQQKjWS9JPkdah5sZvtHc2RXGlg=
github.com/gobuffalo/envy v1.6.15/go.mod h1:n7DRkBerg/aorDM8kbduw5dN3oXGswK5liaSCx4T5NI=
github.com/gobuffalo/envy v1.7.0/go.mod h1:n7DRkBerg/aorDM8kbduw5dN3oXGswK5liaSCx4T5NI=
github.com/gobuffalo/flect v0.1.0/go.mod h1:d2ehjJqGOH/Kjqcoz+F7jHTBbmDb38yXA598Hb50EGs=
github.com/gobuffalo/flect v0.1.1/go.mod h1:8JCgGVbRjJhVgD6399mQr4fx5rRfGKVzFjbj6RE/9UI=
github.com/gobuffalo/flect v0.1.3/go.mod h1:8JCgGVbRjJhVgD6399mQr4fx5rRfGKVzFjbj6RE/9UI=
github.com/gobuffalo/genny v0.0.0-20190329151137-27723ad26ef9/go.mod h1:rWs4Z12d1Zbf19rlsn0nurr75KqhYp52EAGGxTbBhNk=
github.com/gobuffalo/genny v0.0.0-20190403191548-3ca520ef0d9e/go.mod h1:80lIj3kVJWwOrXWWMRzzdhW3DsrdjILVil/SFKBzF28=
github.com/gobuffalo/genny v0.1.0/go.mod h1:XidbUqzak3lHdS//TPu2OgiFB+51Ur5f7CSnXZ/JDvo=
github.com/gobuffalo/genny v0.1.1/go.mod h1:5TExbEyY48pfunL4QSXxlDOmdsD44RRq4mVZ0Ex28Xk=
github.com/gobuffalo/gitgen v0.0.0-20190315122116-cc086187d211/go.mod h1:vEHJk/E9DmhejeLeNt7UVvlSGv3ziL+djtTr3yyzcOw=
github.com/gobuffalo/gogen v0.0.0-20190315121717-8f38393713f5/go.mod h1:V9QVDIxsgKNZs6L2IYiGR8datgMhB577vzTDqypH360=
github.com/gobuffalo/gogen v0.1.0/go.mod h1:8NTelM5qd8RZ15VjQTFkAW6qOMx5wBbW4dSCS3BY8gg=
github.com/gobuffalo/gogen v0.1.1/go.mod h1:y8iBtmHmGc4qa3urIyo1shvOD8JftTtfcKi+71xfDNE=
github.com/gobuffalo/logger v0.0.0-20190315122211-86e12af44bc2/go.mod h1:QdxcLw541hSGtBnhUc4gaNIXRjiDppFGaDqzbrBd3v8=
github.com/gobuffalo/mapi v1.0.1/go.mod h1:4VAGh89y6rVOvm5A8fKFxYG+wIW6LO1FMTG9hnKStFc=
github.com/gobuffalo/mapi v1.0.2/go.mod h1:4VAGh89y6rVOvm5A8fKFxYG+wIW6LO1FMTG9hnKStFc=
github.com/gobuffalo/packd v0.0.0-20190315124812-a385830c7fc0/go.mod h1:M2Juc+hhDXf/PnmBANFCqx4DM3wRbgDvnVWeG2RIxq4=
github.com/gobuffalo/packd v0.1.0/go.mod h1:M2Juc+hhDXf/PnmBANFCqx4DM3wRbgDvnVWeG2RIxq4=
github.com/gobuffalo/packr/v2 v2.0.9/go.mod h1:emmyGweYTm6Kdper+iywB6YK5YzuKchGtJQZ0Odn4pQ=
github.com/gobuffalo/packr/v2 v2.2.0/go.mod h1:CaAwI0GPIAv+5wKLtv8Afwl+Cm78K/I/VCm/3ptBN+0=
github.com/gobuffalo/syncx v0.0.0-20190224160051-33c29581e754/go.mod h1:HhnNqWY95UYwwW3uSASeV7vtgYkT2t16hJgV3AEPUpw=
github.com/golang/snappy v0.0.1 h1:Qgr9rKW7uDUkrbSmQeiDsGa8SjGyCOGtuasMWwvp2P4=
github.com/golang/snappy v0.0.1/go.mod h1:/XxbfmMg8lxefKM7IXC3fBNl/7bRcc72aCRzEWrmP2Q=
github.com/google/go-cmp v0.2.0 h1:+dTQ8DZQJz0Mb/HjFlkptS1FeQ4cWSnN941F8aEG4SQ=
github.com/google/go-cmp v0.2.0/go.mod h1:oXzfMopK8JAjlY9xF4vHSVASa0yLyX7SntLO5aqRK0M=
github.com/inconshreveable/mousetrap v1.0.0/go.mod h1:PxqpIevigyE2G7u3NXJIT2ANytuPF1OarO4DADm73n8=
github.com/jmespath/go-jmespath v0.0.0-20180206201540-c2b33e8439af h1:pmfjZENx5imkbgOkpRUYLnmbU7UEFbjtDA2hxJ1ichM=
github.com/jmespath/go-jmespath v0.0.0-20180206201540-c2b33e8439af/go.mod h1:Nht3zPeWKUH0NzdCt2Blrr5ys8VGpn0CEB0cQHVjt7k=
github.com/joho/godotenv v1.3.0/go.mod h1:7hK45KPybAkOC6peb+G5yklZfMxEjkZhHbwpqxOKXbg=
github.com/karrick/godirwalk v1.8.0/go.mod h1:H5KPZjojv4lE+QYImBI8xVtrBRgYrIVsaRPx4tDPEn4=
github.com/karrick/godirwalk v1.10.3/go.mod h1:RoGL9dQei4vP9ilrpETWE8CLOZ1kiN0LhBygSwrAsHA=
github.com/klauspost/compress v1.9.5 h1:U+CaK85mrNNb4k8BNOfgJtJ/gr6kswUCFj6miSzVC6M=
github.com/klauspost/compress v1.9.5/go.mod h1:RyIbtBH6LamlWaDj8nUwkbUhJ87Yi3uG0guNDohfE1A=
github.com/konsorten/go-windows-terminal-sequences v1.0.1/go.mod h1:T0+1ngSBFLxvqU3pZ+m/2kptfBszLMUkC4ZK/EgS/cQ=
github.com/konsorten/go-windows-terminal-sequences v1.0.2/go.mod h1:T0+1ngSBFLxvqU3pZ+m/2kptfBszLMUkC4ZK/EgS/cQ=
github.com/kr/pretty v0.1.0 h1:L/CwN0zerZDmRFUapSPitk6f+Q3+0za1rQkzVuMiMFI=
github.com/kr/pretty v0.1.0/go.mod h1:dAy3ld7l9f0ibDNOQOHHMYYIIbhfbHSm3C4ZsoJORNo=
github.com/kr/pty v1.1.1/go.mod h1:pFQYn66WHrOpPYNljwOMqo10TkYh1fy3cYio2l3bCsQ=
github.com/kr/text v0.1.0 h1:45sCR5RtlFHMR4UwH9sdQ5TC8v0qDQCHnXt+kaKSTVE=
github.com/kr/text v0.1.0/go.mod h1:4Jbv+DJW3UT/LiOwJeYQe1efqtUx/iVham/4vfdArNI=
github.com/leodido/go-urn v1.2.0 h1:hpXL4XnriNwQ/ABnpepYM/1vCLWNDfUNts8dX3xTG6Y=
github.com/leodido/go-urn v1.2.0/go.mod h1:+8+nEpDfqqsY+g338gtMEUOtuK+4dEMhiQEgxpxOKII=
github.com/markbates/oncer v0.0.0-20181203154359-bf2de49a0be2/go.mod h1:Ld9puTsIW75CHf65OeIOkyKbteujpZVXDpWK6YGZbxE=
github.com/markbates/safe v1.0.1/go.mod h1:nAqgmRi7cY2nqMc92/bSEeQA+R4OheNU2T1kNSCBdG0=
github.com/montanaflynn/stats v0.0.0-20171201202039-1bf9dbcd8cbe/go.mod h1:wL8QJuTMNUDYhXwkmfOly8iTdp5TEcJFWZD2D7SIkUc=
github.com/pelletier/go-toml v1.4.0/go.mod h1:PN7xzY2wHTK0K9p34ErDQMlFxa51Fk0OUruD3k1mMwo=
github.com/pkg/errors v0.8.0/go.mod h1:bwawxfHBFNV+L2hUp1rHADufV3IMtnDRdf1r5NINEl0=
github.com/pkg/errors v0.8.1/go.mod h1:bwawxfHBFNV+L2hUp1rHADufV3IMtnDRdf1r5NINEl0=
github.com/pkg/errors v0.9.1 h1:FEBLx1zS214owpjy7qsBeixbURkuhQAwrK5UwLGTwt4=
github.com/pkg/errors v0.9.1/go.mod h1:bwawxfHBFNV+L2hUp1rHADufV3IMtnDRdf1r5NINEl0=
github.com/pmezard/go-difflib v1.0.0 h1:4DBwDE0NGyQoBHbLQYPwSUPoCMWR5BEzIk/f1lZbAQM=
github.com/pmezard/go-difflib v1.0.0/go.mod h1:iKH77koFhYxTK1pcRnkKkqfTogsbg7gZNVY4sRDYZ/4=
github.com/rogpeppe/go-internal v1.1.0/go.mod h1:M8bDsm7K2OlrFYOpmOWEs/qY81heoFRclV5y23lUDJ4=
github.com/rogpeppe/go-internal v1.2.2/go.mod h1:M8bDsm7K2OlrFYOpmOWEs/qY81heoFRclV5y23lUDJ4=
github.com/rogpeppe/go-internal v1.3.0/go.mod h1:M8bDsm7K2OlrFYOpmOWEs/qY81heoFRclV5y23lUDJ4=
github.com/sirupsen/logrus v1.4.0/go.mod h1:LxeOpSwHxABJmUn/MG1IvRgCAasNZTLOkJPxbbu5VWo=
github.com/sirupsen/logrus v1.4.1/go.mod h1:ni0Sbl8bgC9z8RoU9G6nDWqqs/fq4eDPysMBDgk/93Q=
github.com/sirupsen/logrus v1.4.2/go.mod h1:tLMulIdttU9McNUspp0xgXVQah82FyeX6MwdIuYE2rE=
github.com/spf13/cobra v0.0.3/go.mod h1:1l0Ry5zgKvJasoi3XT1TypsSe7PqH0Sj9dhYf7v3XqQ=
github.com/spf13/pflag v1.0.3/go.mod h1:DYY7MBk1bdzusC3SYhjObp+wFpr4gzcvqqNjLnInEg4=
github.com/stretchr/objx v0.1.0/go.mod h1:HFkY916IF+rwdDfMAkV7OtwuqBVzrE8GR6GFx+wExME=
github.com/stretchr/objx v0.1.1/go.mod h1:HFkY916IF+rwdDfMAkV7OtwuqBVzrE8GR6GFx+wExME=
github.com/stretchr/testify v1.2.2/go.mod h1:a8OnRcib4nhh0OaRAV+Yts87kKdq0PP7pXfy6kDkUVs=
github.com/stretchr/testify v1.3.0 h1:TivCn/peBQ7UY8ooIcPgZFpTNSz0Q2U6UrFlUfqbe0Q=
github.com/stretchr/testify v1.3.0/go.mod h1:M5WIy9Dh21IEIfnGCwXGc5bZfKNJtfHm1UVUgZn+9EI=
github.com/stretchr/testify v1.4.0 h1:2E4SXV/wtOkTonXsotYi4li6zVWxYlZuYNCXe9XRJyk=
github.com/stretchr/testify v1.4.0/go.mod h1:j7eGeouHqKxXV5pUuKE4zz7dFj8WfuZ+81PSLYec5m4=
github.com/tidwall/pretty v1.0.0 h1:HsD+QiTn7sK6flMKIvNmpqz1qrpP3Ps6jOKIKMooyg4=
github.com/tidwall/pretty v1.0.0/go.mod h1:XNkn88O1ChpSDQmQeStsy+sBenx6DDtFZJxhVysOjyk=
github.com/xdg/scram v0.0.0-20180814205039-7eeb5667e42c h1:u40Z8hqBAAQyv+vATcGgV0YCnDjqSL7/q/JyPhhJSPk=
github.com/xdg/scram v0.0.0-20180814205039-7eeb5667e42c/go.mod h1:lB8K/P019DLNhemzwFU4jHLhdvlE6uDZjXFejJXr49I=
github.com/xdg/stringprep v0.0.0-20180714160509-73f8eece6fdc h1:n+nNi93yXLkJvKwXNP9d55HC7lGK4H/SRcwB5IaUZLo=
github.com/xdg/stringprep v0.0.0-20180714160509-73f8eece6fdc/go.mod h1:Jhud4/sHMO4oL310DaZAKk9ZaJ08SJfe+sJh0HrGL1Y=
go.mongodb.org/mongo-driver v1.4.0 h1:C8rFn1VF4GVEM/rG+dSoMmlm2pyQ9cs2/oRtUATejRU=
go.mongodb.org/mongo-driver v1.4.0/go.mod h1:llVBH2pkj9HywK0Dtdt6lDikOjFLbceHVu/Rc0iMKLs=
golang.org/x/crypto v0.0.0-20180904163835-0709b304e793/go.mod h1:6SG95UA2DQfeDnfUPMdvaQW0Q7yPrPDi9nlGo2tz2b4=
golang.org/x/crypto v0.0.0-20190308221718-c2843e01d9a2 h1:VklqNMn3ovrHsnt90PveolxSbWFaJdECFbxSq0Mqo2M=
golang.org/x/crypto v0.0.0-20190308221718-c2843e01d9a2/go.mod h1:djNgcEr1/C05ACkg1iLfiJU5Ep61QUkGW8qpdssI0+w=
golang.org/x/crypto v0.0.0-20190422162423-af44ce270edf/go.mod h1:WFFai1msRO1wXaEeE5yQxYXgSfI8pQAWXbQop6sCtWE=
golang.org/x/crypto v0.0.0-20190530122614-20be4c3c3ed5 h1:8dUaAV7K4uHsF56JQWkprecIQKdPHtR9jCHF5nB8uzc=
golang.org/x/crypto v0.0.0-20190530122614-20be4c3c3ed5/go.mod h1:yigFU9vqHzYiE8UmvKecakEJjdnWj3jj499lnFckfCI=
golang.org/x/net v0.0.0-20190311183353-d8887717615a/go.mod h1:t9HGtf8HONx5eT2rtn7q6eTqICYqUVnKs3thJo3Qplg=
golang.org/x/net v0.0.0-20190404232315-eb5bcb51f2a3/go.mod h1:t9HGtf8HONx5eT2rtn7q6eTqICYqUVnKs3thJo3Qplg=
golang.org/x/net v0.0.0-20200202094626-16171245cfb2 h1:CCH4IOTTfewWjGOlSp+zGcjutRKlBEZQ6wTn8ozI/nI=
golang.org/x/net v0.0.0-20200202094626-16171245cfb2/go.mod h1:z5CRVTTTmAJ677TzLLGU+0bjPO0LkuOLi4/5GtJWs/s=
golang.org/x/sync v0.0.0-20190227155943-e225da77a7e6/go.mod h1:RxMgew5VJxzue5/jJTE5uejpjVlOe/izrB70Jof72aM=
golang.org/x/sync v0.0.0-20190412183630-56d357773e84/go.mod h1:RxMgew5VJxzue5/jJTE5uejpjVlOe/izrB70Jof72aM=
golang.org/x/sync v0.0.0-20190423024810-112230192c58 h1:8gQV6CLnAEikrhgkHFbMAEhagSSnXWGV915qUMm9mrU=
golang.org/x/sync v0.0.0-20190423024810-112230192c58/go.mod h1:RxMgew5VJxzue5/jJTE5uejpjVlOe/izrB70Jof72aM=
golang.org/x/sync v0.0.0-20190911185100-cd5d95a43a6e h1:vcxGaoTs7kV8m5Np9uUNQin4BrLOthgV7252N8V+FwY=
golang.org/x/sync v0.0.0-20190911185100-cd5d95a43a6e/go.mod h1:RxMgew5VJxzue5/jJTE5uejpjVlOe/izrB70Jof72aM=
golang.org/x/sys v0.0.0-20180905080454-ebe1bf3edb33/go.mod h1:STP8DvDyc/dI5b8T5hshtkjS+E42TnysNCUPdjciGhY=
golang.org/x/sys v0.0.0-20190215142949-d0b11bdaac8a/go.mod h1:STP8DvDyc/dI5b8T5hshtkjS+E42TnysNCUPdjciGhY=
golang.org/x/sys v0.0.0-20190403152447-81d4e9dc473e/go.mod h1:h1NjWce9XRLGQEsW7wpKNCjG9DtNlClVuFLEZdDNbEs=
golang.org/x/sys v0.0.0-20190412213103-97732733099d/go.mod h1:h1NjWce9XRLGQEsW7wpKNCjG9DtNlClVuFLEZdDNbEs=
golang.org/x/sys v0.0.0-20190419153524-e8e3143a4f4a/go.mod h1:h1NjWce9XRLGQEsW7wpKNCjG9DtNlClVuFLEZdDNbEs=
golang.org/x/sys v0.0.0-20190422165155-953cdadca894/go.mod h1:h1NjWce9XRLGQEsW7wpKNCjG9DtNlClVuFLEZdDNbEs=
golang.org/x/sys v0.0.0-20190531175056-4c3a928424d2/go.mod h1:h1NjWce9XRLGQEsW7wpKNCjG9DtNlClVuFLEZdDNbEs=
golang.org/x/text v0.3.0 h1:g61tztE5qeGQ89tm6NTjjM9VPIm088od1l6aSorWRWg=
golang.org/x/text v0.3.0/go.mod h1:NqM8EUOU14njkJ3fqMW+pc6Ldnwhi/IjpwHt7yyuwOQ=
golang.org/x/text v0.3.2/go.mod h1:bEr9sfX3Q8Zfm5fL9x+3itogRgK3+ptLWKqgva+5dAk=
golang.org/x/text v0.3.3 h1:cokOdA+Jmi5PJGXLlLllQSgYigAEfHXJAERHVMaCc2k=
golang.org/x/text v0.3.3/go.mod h1:5Zoc/QRtKVWzQhOtBMvqHzDpF6irO9z98xDceosuGiQ=
golang.org/x/tools v0.0.0-20180917221912-90fa682c2a6e/go.mod h1:n7NCudcB/nEzxVGmLbDWY5pfWTLqBcC2KZ6jyYvM4mQ=
golang.org/x/tools v0.0.0-20190329151228-23e29df326fe/go.mod h1:LCzVGOaR6xXOjkQ3onu1FJEFr0SW1gC7cKk1uF8kGRs=
golang.org/x/tools v0.0.0-20190416151739-9c9e1878f421/go.mod h1:LCzVGOaR6xXOjkQ3onu1FJEFr0SW1gC7cKk1uF8kGRs=
golang.org/x/tools v0.0.0-20190420181800-aa740d480789/go.mod h1:LCzVGOaR6xXOjkQ3onu1FJEFr0SW1gC7cKk1uF8kGRs=
golang.org/x/tools v0.0.0-20190531172133-b3315ee88b7d/go.mod h1:/rFqwRUd4F7ZHNgwSSTFct+R/Kf4OFW1sUzUTQQTgfc=
gopkg.in/check.v1 v0.0.0-20161208181325-20d25e280405 h1:yhCVgyC4o1eVCa2tZl7eS0r+SDo693bJlVdllGtEeKM=
gopkg.in/check.v1 v0.0.0-20161208181325-20d25e280405/go.mod h1:Co6ibVJAznAaIkqp8huTwlJQCZ016jof/cbN4VW5Yz0=
gopkg.in/check.v1 v1.0.0-20180628173108-788fd7840127 h1:qIbj1fsPNlZgppZ+VLlY7N33q108Sa+fhmuc+sWQYwY=
gopkg.in/check.v1 v1.0.0-20180628173108-788fd7840127/go.mod h1:Co6ibVJAznAaIkqp8huTwlJQCZ016jof/cbN4VW5Yz0=
gopkg.in/errgo.v2 v2.1.0/go.mod h1:hNsd1EY+bozCKY1Ytp96fpM3vjJbqLJn88ws8XvfDNI=
gopkg.in/go-playground/assert.v1 v1.2.1 h1:xoYuJVE7KT85PYWrN730RguIQO0ePzVRfFMXadIrXTM=
gopkg.in/go-playground/assert.v1 v1.2.1/go.mod h1:9RXL0bg/zibRAgZUYszZSwO/z8Y/a8bDuhia5mkpMnE=
gopkg.in/go-playground/validator.v9 v9.31.0 h1:bmXmP2RSNtFES+bn4uYuHT7iJFJv7Vj+an+ZQdDaD1M=
gopkg.in/go-playground/validator.v9 v9.31.0/go.mod h1:+c9/zcJMFNgbLvly1L1V+PpxWdVbfP1avr/N00E2vyQ=
gopkg.in/yaml.v2 v2.2.2 h1:ZCJp+EgiOT7lHqUV2J862kp8Qj64Jo6az82+3Td9dZw=
gopkg.in/yaml.v2 v2.2.2/go.mod h1:hI93XBmqTisBFMUTm0b8Fm+jr3Dg1NNxqwp+5A1VGuI=
gopkg.in/yaml.v2 v2.3.0 h1:clyUAQHOM3G0M3f5vQj7LuJrETvjVot3Z5el9nffUtU=
gopkg.in/yaml.v2 v2.3.0/go.mod h1:hI93XBmqTisBFMUTm0b8Fm+jr3Dg1NNxqwp+5A1VGuI=


File: /internal\app\mikrotik_provisioning.go
package app

import (
	"context"

	"mikrotik_provisioning/internal/pkg/address_list"
)

type UseCases interface {
	Storage
}

type Storage interface {
	GetAddressLists(ctx context.Context) ([]*address_list.AddressList, error)
	CreateAddressList(ctx context.Context, addressList *address_list.AddressList) (*address_list.AddressList, error)
	GetAddressList(ctx context.Context, name string) (*address_list.AddressList, error)
	UpdateAddressList(ctx context.Context, id string, addressList *address_list.AddressList) (*address_list.AddressList, error)
	DeleteAddressList(ctx context.Context, id string) error
	UpdateEntriesInAddressList(ctx context.Context, action address_list.Action, id string, addresses []*address_list.Address) (*address_list.AddressList, error)
}

type Service struct {
	storage Storage
}

func NewMikrotikProvisioningService(storage Storage) *Service {
	return &Service{storage: storage}
}

func (s *Service) GetAddressLists(ctx context.Context) ([]*address_list.AddressList, error) {
	return s.storage.GetAddressLists(ctx)
}

func (s *Service) CreateAddressList(ctx context.Context, addressList *address_list.AddressList) (*address_list.AddressList, error) {
	return s.storage.CreateAddressList(ctx, addressList)
}

func (s *Service) GetAddressList(ctx context.Context, name string) (*address_list.AddressList, error) {
	return s.storage.GetAddressList(ctx, name)
}

func (s *Service) UpdateAddressList(ctx context.Context, id string, addressList *address_list.AddressList) (*address_list.AddressList, error) {
	return s.storage.UpdateAddressList(ctx, id, addressList)
}

func (s *Service) DeleteAddressList(ctx context.Context, id string) error {
	return s.storage.DeleteAddressList(ctx, id)
}

func (s *Service) UpdateEntriesInAddressList(ctx context.Context, action address_list.Action, id string, addresses []*address_list.Address) (*address_list.AddressList, error) {
	return s.storage.UpdateEntriesInAddressList(ctx, action, id, addresses)
}


File: /internal\config\config.go
package config

import (
	"io/ioutil"
	"time"

	"gopkg.in/go-playground/validator.v9"
	"gopkg.in/yaml.v2"

	valid "mikrotik_provisioning/pkg/validator"
)

const (
	configFile = "config.yml"
)

type (
	Config struct {
		Access      *Access      `yaml:"access" validator:"required"`
		DB          *Database    `yaml:"database" validator:"required"`
		Application *Application `yaml:"application" validator:"required"`
	}

	Access struct {
		Users []*User `yaml:"users" validator:"required"`
	}

	User struct {
		AccessKey string `yaml:"access_key" bson:"access_key" validator:"required,access_key"`
		SecretKey string `yaml:"secret_key" bson:"secret_key" validator:"required,secret_key"`
	}

	Database struct {
		DSN         string        `yaml:"dsn" validator:"required,mongo_dsn"`
		Name        string        `yaml:"name" validator:"required,alphanum"`
		Collections []*Collection `yaml:"collections" validator:"required"`
		Timeout     time.Duration `yaml:"timeout" validator:"required,min=1"`
	}

	Collection struct {
		Resource string               `yaml:"resource" validator:"required,alphanum"`
		Name     string               `yaml:"name" validator:"required,alphanum"`
		Indexes  []*CollectionIndexes `yaml:"indexes" validator:"required"`
	}

	CollectionIndexes struct {
		Name   string `yaml:"name" validator:"required,alphanum"`
		Unique bool   `yaml:"unique" validator:"required"`
		Field  string `yaml:"field" validator:"required,alphanum"`
	}

	Application struct{}

	Template struct {
		Name string `yaml:"name" validator:"required,alphanum"`
		Path string `yaml:"path" validator:"required,file"`
	}
)

func ParseConfig() (*Config, error) {
	file, err := ioutil.ReadFile(configFile)
	if err != nil {
		return nil, err
	}

	config := new(Config)
	if err := yaml.Unmarshal(file, &config); err != nil {
		return nil, err
	}

	validator := validator.New()
	if err := valid.RegisterValidators(validator); err != nil {
		return nil, err
	}
	if err := validator.Struct(config); err != nil {
		return nil, err
	}

	return config, nil
}


File: /internal\pkg\address_list\address_list.go
package address_list

import (
	"net/http"

	"gopkg.in/go-playground/validator.v9"
)

type (
	Address struct {
		Address  string `json:"address" bson:"address" validator:"required,ipv4|fqdn"`
		Disabled bool   `json:"disabled,omitempty" bson:"disabled,omitempty" validator:"omitempty"`
		Comment  string `json:"comment,omitempty" bson:"comment,omitempty" validator:"omitempty,comment"`
	}

	AddressList struct {
		ID        string     `json:"-" validator:"omitempty"`
		Name      string     `json:"name" validator:"required,address_list_name"`
		Addresses []*Address `json:"addresses" validator:"required"`
	}

	AddressListRequest struct {
		*AddressList
	}

	AddressListResponse struct {
		*AddressList
	}

	AddressListPatchRequest struct {
		Action    Action     `json:"action" validator:"required,oneof=add remove"`
		Addresses []*Address `json:"addresses" validator:"required"`
	}

	Action string
)

const (
	AddAction    Action = "add"
	RemoveAction Action = "remove"
)

func (a *AddressListRequest) Bind(r *http.Request) error {
	validator := validator.New()
	if err := validator.Struct(a); err != nil {
		return err
	}

	return nil
}

func (a *AddressListPatchRequest) Bind(r *http.Request) error {
	validator := validator.New()
	if err := validator.Struct(a); err != nil {
		return err
	}

	return nil
}

func (rd *AddressListResponse) Render(w http.ResponseWriter, r *http.Request) error {
	return nil
}


File: /internal\pkg\errors\errors.go
package errors

type Error string

func (e Error) Error() string {
	return string(e)
}


File: /internal\pkg\http\address_list.go
package http

import (
	"net/http"

	"github.com/go-chi/render"

	"mikrotik_provisioning/internal/pkg/address_list"
)

func (h *AddressListHandler) GetAddressLists(w http.ResponseWriter, r *http.Request) {
	results, err := h.service.GetAddressLists(r.Context())
	if err != nil {
		_ = render.Render(w, r, ErrInternalServerError(err))
	}

	var out []byte
	switch r.Context().Value(FormatKey) {
	case RSCFormat:
		if len(results) != 0 {
			out, err = h.getAddressListsTextResponse(results)
			if err != nil {
				_ = render.Render(w, r, ErrRender(err))
			}
			_, _ = w.Write(out)
		} else {
			render.Status(r, http.StatusOK)
		}
	default:
		if err != nil {
			_ = render.Render(w, r, ErrInternalServerError(err))
		}

		if err := render.RenderList(w, r, getAddressListsJSONResponse(results)); err != nil {
			_ = render.Render(w, r, ErrRender(err))
		}
	}
}

func (h *AddressListHandler) CreateAddressList(w http.ResponseWriter, r *http.Request) {
	data := &address_list.AddressListRequest{}
	if err := render.Bind(r, data); err != nil {
		_ = render.Render(w, r, ErrInvalidRequest(err))
		return
	}

	addressList, err := h.service.CreateAddressList(r.Context(), data.AddressList)
	if err != nil {
		_ = render.Render(w, r, ErrInternalServerError(err))
		return
	}

	render.Status(r, http.StatusCreated)
	_ = render.Render(w, r, newAddressListResponse(addressList))
}

func (h *AddressListHandler) GetAddressList(w http.ResponseWriter, r *http.Request) {
	addressList := r.Context().Value(AddressListKey).(*address_list.AddressList)

	switch r.Context().Value(FormatKey) {
	case RSCFormat:
		if out, err := h.getAddressListTextResponse(addressList); err != nil {
			_ = render.Render(w, r, ErrRender(err))
		} else {
			_, _ = w.Write(out)
		}
	default:
		if err := render.Render(w, r, newAddressListResponse(addressList)); err != nil {
			_ = render.Render(w, r, ErrRender(err))
		}
	}
}

func (h *AddressListHandler) UpdateAddressList(w http.ResponseWriter, r *http.Request) {
	addressList := r.Context().Value(AddressListKey).(*address_list.AddressList)

	data := &address_list.AddressListRequest{AddressList: addressList}
	if err := render.Bind(r, data); err != nil {
		_ = render.Render(w, r, ErrInvalidRequest(err))
		return
	}

	addressList, err := h.service.UpdateAddressList(r.Context(), data.AddressList.ID, data.AddressList)
	if err != nil {
		_ = render.Render(w, r, ErrInternalServerError(err))
		return
	}

	_ = render.Render(w, r, newAddressListResponse(addressList))
}

func (h *AddressListHandler) DeleteAddressList(w http.ResponseWriter, r *http.Request) {
	addressList := r.Context().Value(AddressListKey).(*address_list.AddressList)

	err := h.service.DeleteAddressList(r.Context(), addressList.ID)
	if err != nil {
		_ = render.Render(w, r, ErrInvalidRequest(err))
		return
	}

	render.Status(r, http.StatusNoContent)
}

func (h *AddressListHandler) PatchAddressList(w http.ResponseWriter, r *http.Request) {
	addressList := r.Context().Value(AddressListKey).(*address_list.AddressList)

	data := &address_list.AddressListPatchRequest{}
	err := render.Bind(r, data)
	if err != nil {
		_ = render.Render(w, r, ErrInvalidRequest(err))
		return
	}

	addressList, err = h.service.UpdateEntriesInAddressList(r.Context(), data.Action, addressList.ID, data.Addresses)
	if err != nil {
		_ = render.Render(w, r, ErrInternalServerError(err))
		return
	}

	_ = render.Render(w, r, newAddressListResponse(addressList))
}


File: /internal\pkg\http\errors.go
package http

import (
	"net/http"

	"github.com/go-chi/render"
)

type ErrResponse struct {
	Err            error `json:"-"` // low-level runtime error
	HTTPStatusCode int   `json:"-"` // http response status code

	StatusText string `json:"status"`          // user-level status message
	AppCode    int64  `json:"code,omitempty"`  // application-specific error code
	ErrorText  string `json:"error,omitempty"` // application-level error message, for debugging
}

func (e *ErrResponse) Render(w http.ResponseWriter, r *http.Request) error {
	render.Status(r, e.HTTPStatusCode)
	return nil
}

func ErrInvalidRequest(err error) render.Renderer {
	return &ErrResponse{
		Err:            err,
		HTTPStatusCode: http.StatusBadRequest,
		StatusText:     "invalid request",
		ErrorText:      err.Error(),
	}
}

func ErrInternalServerError(err error) render.Renderer {
	return &ErrResponse{
		Err:            err,
		HTTPStatusCode: http.StatusInternalServerError,
		StatusText:     "internal server error",
		ErrorText:      err.Error(),
	}
}

func ErrRender(err error) render.Renderer {
	return &ErrResponse{
		Err:            err,
		HTTPStatusCode: http.StatusUnprocessableEntity,
		StatusText:     "error rendering response",
		ErrorText:      err.Error(),
	}
}

var ErrNotFound = &ErrResponse{HTTPStatusCode: 404, StatusText: "resource not found"}


File: /internal\pkg\http\handler.go
package http

import (
	"net/http"
	"text/template"

	"mikrotik_provisioning/internal/app"
)

type Middleware interface {
	EnsureAddressListExists(next http.Handler) http.Handler
	EnsureAddressListNotExists(next http.Handler) http.Handler
	EnsureAuth(next http.Handler) http.Handler
	CheckAcceptHeader(contentTypes ...string) func(next http.Handler) http.Handler
}

type Handler interface {
	GetAddressLists(w http.ResponseWriter, r *http.Request)
	CreateAddressList(w http.ResponseWriter, r *http.Request)
	GetAddressList(w http.ResponseWriter, r *http.Request)
	UpdateAddressList(w http.ResponseWriter, r *http.Request)
	PatchAddressList(w http.ResponseWriter, r *http.Request)
	DeleteAddressList(w http.ResponseWriter, r *http.Request)
}

type AddressListHandler struct {
	service   app.UseCases
	templates *template.Template
}

func NewAddressListHandler(service app.UseCases, templates *template.Template) *AddressListHandler {
	return &AddressListHandler{service: service, templates: templates}
}


File: /internal\pkg\http\middleware\middleware.go
package middleware

import (
	"bytes"
	"context"
	"encoding/json"
	"fmt"
	"io/ioutil"
	"net/http"
	"strings"

	"github.com/go-chi/chi"
	"github.com/go-chi/render"

	"gopkg.in/go-playground/validator.v9"

	"mikrotik_provisioning/internal/app"
	"mikrotik_provisioning/internal/config"
	"mikrotik_provisioning/internal/pkg/address_list"
	mux "mikrotik_provisioning/internal/pkg/http"
)

type Middleware struct {
	validator *validator.Validate
	service   app.UseCases
	config    *config.Access
}

func NewMiddleware(service app.UseCases, config *config.Access) *Middleware {
	return &Middleware{validator: validator.New(), service: service, config: config}
}

func (m *Middleware) isValidAddressListRequest(request *address_list.AddressListRequest) error {
	if err := m.validator.Struct(request); err != nil {
		return err
	}

	return nil
}

func (m *Middleware) checkAccessKeys(accessKey string, secretKey string) bool {
	for _, v := range m.config.Users {
		if v.AccessKey == accessKey && v.SecretKey == secretKey {
			return true
		}
	}

	return false
}

func (m *Middleware) EnsureAddressListExists(next http.Handler) http.Handler {
	return http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
		if addressListName := chi.URLParam(r, "addressListName"); addressListName != "" {
			addressList, err := m.service.GetAddressList(r.Context(), addressListName)
			if err != nil {
				_ = render.Render(w, r, mux.ErrInternalServerError(err))
				return
			}

			if addressList == nil {
				_ = render.Render(w, r, mux.ErrNotFound)
				return
			}

			ctx := context.WithValue(r.Context(), mux.AddressListKey, addressList)
			next.ServeHTTP(w, r.WithContext(ctx))
		} else {
			_ = render.Render(w, r, mux.ErrNotFound)
			return
		}
	})
}

func (m *Middleware) EnsureAddressListNotExists(next http.Handler) http.Handler {
	return http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
		data := new(address_list.AddressListRequest)

		bodyBytes, _ := ioutil.ReadAll(r.Body)
		r.Body.Close()
		r.Body = ioutil.NopCloser(bytes.NewBuffer(bodyBytes))

		if err := json.Unmarshal(bodyBytes, data); err != nil {
			_ = render.Render(w, r, mux.ErrInvalidRequest(err))
			return
		}

		if err := m.isValidAddressListRequest(data); err != nil {
			_ = render.Render(w, r, mux.ErrInvalidRequest(err))
			return
		}

		result, err := m.service.GetAddressList(r.Context(), data.Name)
		if err != nil {
			_ = render.Render(w, r, mux.ErrInternalServerError(err))
			return
		}

		if result != nil {
			_ = render.Render(w, r, mux.ErrInvalidRequest(fmt.Errorf("address list already exists: %s", result.Name)))
			return
		}

		next.ServeHTTP(w, r)
	})
}

func (m *Middleware) EnsureAuth(next http.Handler) http.Handler {
	return http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
		if auth := r.Header.Get("Authorization"); auth != "" {
			authValues := strings.Split(auth, ":")
			if len(authValues) == 2 {
				accessKey := authValues[0]
				secretKey := authValues[1]
				if m.checkAccessKeys(accessKey, secretKey) {
					next.ServeHTTP(w, r)
				}
			} else {
				http.Error(w, http.StatusText(http.StatusForbidden), http.StatusForbidden)
				return
			}
		} else {
			http.Error(w, http.StatusText(http.StatusUnauthorized), http.StatusUnauthorized)
			return
		}
	})
}

func (m *Middleware) CheckAcceptHeader(contentTypes ...string) func(next http.Handler) http.Handler {
	cT := make([]string, 0)
	for _, t := range contentTypes {
		cT = append(cT, strings.ToLower(t))
	}

	return func(next http.Handler) http.Handler {
		fn := func(w http.ResponseWriter, r *http.Request) {
			s := strings.ToLower(strings.TrimSpace(r.Header.Get(string(mux.AcceptKey))))
			if i := strings.Index(s, ";"); i > -1 {
				s = s[0:i]
			}

			if format := r.URL.Query().Get(string(mux.FormatKey)); format == string(mux.RSCFormat) {
				ctx := context.WithValue(r.Context(), mux.FormatKey, mux.RSCFormat)
				next.ServeHTTP(w, r.WithContext(ctx))
				return
			} else if format != "" {
				_ = render.Render(w, r, mux.ErrInvalidRequest(fmt.Errorf("invalid format parameter value: %s", format)))
				return
			}

			ctx := context.WithValue(r.Context(), mux.AcceptKey, s)
			for _, t := range cT {
				if t == s {
					next.ServeHTTP(w, r.WithContext(ctx))
					return
				}
			}

			w.WriteHeader(http.StatusNotAcceptable)
		}
		return http.HandlerFunc(fn)
	}
}


File: /internal\pkg\http\response.go
package http

import (
	"bytes"

	"github.com/go-chi/render"

	"mikrotik_provisioning/internal/pkg/address_list"
)

func newAddressListResponse(addressList *address_list.AddressList) *address_list.AddressListResponse {
	return &address_list.AddressListResponse{AddressList: addressList}
}

func getAddressListsJSONResponse(addressLists []*address_list.AddressList) []render.Renderer {
	list := make([]render.Renderer, len(addressLists))

	for i, addressList := range addressLists {
		list[i] = newAddressListResponse(addressList)
	}
	return list
}

func (h *AddressListHandler) getAddressListsTextResponse(addressLists []*address_list.AddressList) ([]byte, error) {
	output := bytes.Buffer{}
	err := h.templates.ExecuteTemplate(&output, "GetAddressLists", addressLists)
	if err != nil {
		return nil, err
	}

	return output.Bytes(), nil
}

func (h *AddressListHandler) getAddressListTextResponse(addressList *address_list.AddressList) ([]byte, error) {
	output := bytes.Buffer{}
	err := h.templates.ExecuteTemplate(&output, "GetAddressList", addressList)
	if err != nil {
		return nil, err
	}

	return output.Bytes(), nil
}


File: /internal\pkg\http\types.go
package http

type ContextKey string

type Format string

type Action string

const (
	FormatKey      ContextKey = "format"
	AcceptKey      ContextKey = "Accept"
	AddressListKey ContextKey = "addressList"

	RSCFormat Format = "rsc"
)


File: /internal\pkg\repository\mongo\address_list.go
package mongo

import (
	"context"
	"errors"

	"go.mongodb.org/mongo-driver/bson"
	"go.mongodb.org/mongo-driver/bson/primitive"
	"go.mongodb.org/mongo-driver/mongo/options"

	"mikrotik_provisioning/internal/pkg/address_list"
)

type AddressList struct {
	ID        primitive.ObjectID      `bson:"_id,omitempty"`
	Name      string                  `bson:"name"`
	Addresses []*address_list.Address `bson:"addresses"`
}

func (a *AddressList) ToAddressList() *address_list.AddressList {
	return &address_list.AddressList{
		ID:        a.ID.Hex(),
		Name:      a.Name,
		Addresses: a.Addresses,
	}
}

func (s *Storage) CreateAddressList(ctx context.Context, addressList *address_list.AddressList) (*address_list.AddressList, error) {
	res, err := s.collections["address-list"].InsertOne(ctx, &AddressList{
		Name:      addressList.Name,
		Addresses: addressList.Addresses,
	})
	if err != nil {
		return nil, err
	}

	addressList.ID = res.InsertedID.(primitive.ObjectID).Hex()

	return addressList, nil
}

func (s *Storage) GetAddressLists(ctx context.Context) ([]*address_list.AddressList, error) {
	cur, err := s.collections["address-list"].Find(ctx, bson.M{})
	defer cur.Close(ctx)
	if err != nil {
		return nil, err
	}

	result := make([]*address_list.AddressList, 0)
	for cur.Next(ctx) {
		data := new(AddressList)
		err := cur.Decode(data)
		if err != nil {
			return nil, err
		}

		result = append(result, data.ToAddressList())
	}

	return result, nil
}

func (s *Storage) GetAddressList(ctx context.Context, name string) (*address_list.AddressList, error) {
	res := s.collections["address-list"].FindOne(ctx, bson.M{"name": name})
	if res.Err() != nil {
		if res.Err().Error() == NoDocumentsError {
			return nil, nil
		}
		return nil, res.Err()
	}

	if b, err := res.DecodeBytes(); err != nil {
		if b.String() == "" && err.Error() == NoDocumentsError {
			return nil, nil
		}
		return nil, err
	}

	data := new(AddressList)
	err := res.Decode(data)
	if err != nil {
		return nil, err
	}

	return data.ToAddressList(), nil
}

func (s *Storage) UpdateAddressList(ctx context.Context, id string, addressList *address_list.AddressList) (*address_list.AddressList, error) {
	objectID, err := primitive.ObjectIDFromHex(id)
	if err != nil {
		return nil, err
	}

	res := s.collections["address-list"].FindOneAndReplace(ctx, bson.M{"_id": objectID}, &AddressList{
		ID:        objectID,
		Name:      addressList.Name,
		Addresses: addressList.Addresses,
	}, options.FindOneAndReplace().SetReturnDocument(options.After))
	if res.Err() != nil {
		return nil, res.Err()
	}

	data := new(AddressList)
	err = res.Decode(data)
	if err != nil {
		return nil, err
	}

	return data.ToAddressList(), nil
}

func (s *Storage) UpdateEntriesInAddressList(ctx context.Context, action address_list.Action, id string, addresses []*address_list.Address) (*address_list.AddressList, error) {
	currentData, err := s.getAddressListByID(ctx, id)
	if err != nil {
		return nil, err
	}

	objectID, err := primitive.ObjectIDFromHex(id)
	if err != nil {
		return nil, err
	}

	bsonAddresses := addressesToBsonList(currentData, addresses)

	var update bson.M
	switch action {
	case address_list.AddAction:
		update = bson.M{"$push": bson.M{"addresses": bson.M{"$each": bsonAddresses}}}
	case address_list.RemoveAction:
		update = bson.M{"$pull": bson.M{"addresses": bson.M{"$in": bsonAddresses}}}
	}
	res := s.collections["address-list"].FindOneAndUpdate(ctx, bson.M{"_id": objectID}, update)
	if res.Err() != nil {
		return nil, res.Err()
	}

	data := new(AddressList)
	err = res.Decode(data)
	if err != nil {
		return nil, err
	}

	newData, err := s.getAddressListByID(ctx, id)
	if err != nil {
		return nil, err
	}

	return newData.ToAddressList(), nil
}

func (s *Storage) DeleteAddressList(ctx context.Context, id string) error {
	objectID, err := primitive.ObjectIDFromHex(id)
	if err != nil {
		return err
	}

	res, err := s.collections["address-list"].DeleteOne(ctx, bson.M{"_id": objectID})
	if err != nil {
		return err
	}

	if res.DeletedCount == 0 {
		return errors.New("failed deleting mongodb object")
	}

	return nil
}

func (s *Storage) getAddressListByID(ctx context.Context, id string) (*AddressList, error) {
	objectID, err := primitive.ObjectIDFromHex(id)
	if err != nil {
		return nil, err
	}

	res := s.collections["address-list"].FindOne(ctx, bson.M{"_id": objectID})
	if res.Err() != nil {
		if res.Err().Error() == NoDocumentsError {
			return nil, nil
		}
		return nil, res.Err()
	}

	b, err := res.DecodeBytes()
	if err != nil {
		if b.String() == "" && err.Error() == NoDocumentsError {
			return nil, nil
		}
		return nil, err
	}

	data := new(AddressList)
	err = res.Decode(data)
	if err != nil {
		return nil, err
	}

	return data, nil
}

func addressesToBsonList(addressList *AddressList, addresses []*address_list.Address) primitive.A {
	bsonA := primitive.A{}
	ok := true
	for _, a := range addresses {
		for _, b := range addressList.Addresses {
			if b == a {
				ok = false
				break
			}
		}
		if ok {
			bsonA = append(bsonA, a)
		}
	}

	return bsonA
}


File: /internal\pkg\repository\mongo\indexes.go
package mongo

import (
	"context"
	"fmt"

	"go.mongodb.org/mongo-driver/bson"
	"go.mongodb.org/mongo-driver/mongo"
	"go.mongodb.org/mongo-driver/mongo/options"

	"mikrotik_provisioning/internal/config"
)

type Index struct {
	Version    int32            `bson:"v"`
	Key        map[string]int32 `bson:"key"`
	Name       string           `bson:"name"`
	Namespace  string           `bson:"ns"`
	Unique     bool             `bson:"unique"`
	Background bool             `bson:"background"`
}

func createIndexes(ctx context.Context, collection *mongo.Collection, indexList []*config.CollectionIndexes) error {
	cur, err := collection.Indexes().List(ctx)
	defer cur.Close(ctx)
	if err != nil {
		return fmt.Errorf("failed to get list of indexes for collection: %s from mongodb with error: %q", collection.Name(), err)
	}

	indexes := make([]string, 0)
	for cur.Next(ctx) {
		index := new(Index)
		err := cur.Decode(&index)

		if err != nil {
			return fmt.Errorf("failed to decode index model for collection: %s from mongodb with error: %q", collection.Name(), err)
		}

		indexes = append(indexes, index.Name)
	}

	for _, index := range indexList {
		var exists bool
		for _, i := range indexes {
			if index.Name == i {
				exists = true
				break
			}
		}

		if exists {
			continue
		}

		res, err := collection.Indexes().CreateOne(ctx, mongo.IndexModel{
			Keys:    bson.D{{Key: index.Field, Value: 1}},
			Options: options.Index().SetBackground(true).SetName(index.Name).SetUnique(index.Unique),
		})

		if err != nil || res != index.Name {
			return fmt.Errorf("failed to create index for collection: %s in mongodb with error: %q", index.Name, err)
		}
	}

	return nil
}


File: /internal\pkg\repository\mongo\mongo.go
package mongo

import (
	"context"
	"fmt"
	"time"

	"go.mongodb.org/mongo-driver/mongo"
	"go.mongodb.org/mongo-driver/mongo/options"
	"go.mongodb.org/mongo-driver/mongo/readpref"

	"mikrotik_provisioning/internal/config"
)

const (
	NoDocumentsError = "mongo: no documents in result"
)

type Storage struct {
	collections map[string]*mongo.Collection
}

func NewMongoStorage(ctx context.Context, dbConfig *config.Database) (*Storage, error) {
	client, err := mongo.Connect(
		ctx,
		options.Client().ApplyURI(dbConfig.DSN),
		options.Client().SetConnectTimeout(dbConfig.Timeout*time.Second),
		options.Client().SetDirect(true),
	)
	if err != nil {
		return nil, fmt.Errorf("failed to connect to mongodb: %q", err)
	}

	err = client.Ping(ctx, readpref.Nearest())
	if err != nil {
		return nil, fmt.Errorf("failed to ping mongodb: %q", err)
	}

	collections := make(map[string]*mongo.Collection)
	for _, coll := range dbConfig.Collections {
		collections[coll.Resource] = client.Database(dbConfig.Name).Collection(coll.Name)

		if err := createIndexes(ctx, collections[coll.Resource], coll.Indexes); err != nil {
			return nil, err
		}
	}

	return &Storage{collections: collections}, nil
}


File: /pkg\validator\validator.go
package validator

import (
	"regexp"

	"gopkg.in/go-playground/validator.v9"
)

func addressListNameValidator(fl validator.FieldLevel) bool {
	if ok, _ := regexp.MatchString(`^[A-Za-z0-9-]+$`, fl.Field().String()); !ok {
		return false
	}

	return true
}

func commentValidator(fl validator.FieldLevel) bool {
	if ok, _ := regexp.MatchString(`^[A-Za-zА-Яа-я0-9\s,.:-]+$`, fl.Field().String()); !ok {
		return false
	}

	return true
}

func accessKeyValidator(fl validator.FieldLevel) bool {
	if ok, _ := regexp.MatchString(`^[A-Z0-9]{24}$`, fl.Field().String()); !ok {
		return false
	}

	return true
}

func secretKeyValidator(fl validator.FieldLevel) bool {
	if ok, _ := regexp.MatchString(`^[a-f0-9]{64}$`, fl.Field().String()); !ok {
		return false
	}

	return true
}

func mongoDSNValidator(fl validator.FieldLevel) bool {
	if ok, _ := regexp.MatchString(`^mongodb://([a-zA-Z0-9][a-zA-Z0-9.-]+[a-zA-Z0-9]|(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])):([0-9]{1,4}|[1-5][0-9]{4}|6[0-4][0-9]{3}|65[0-4][0-9]{2}|655[0-2][0-9]|6553[0-5])$`, fl.Field().String()); !ok {
		return false
	}

	return true
}

func RegisterValidators(v *validator.Validate) error {
	if err := v.RegisterValidation("address_list_name", addressListNameValidator); err != nil {
		return err
	}

	if err := v.RegisterValidation("comment", commentValidator); err != nil {
		return err
	}

	if err := v.RegisterValidation("access_key", accessKeyValidator); err != nil {
		return err
	}

	if err := v.RegisterValidation("secret_key", secretKeyValidator); err != nil {
		return err
	}

	if err := v.RegisterValidation("mongo_dsn", mongoDSNValidator); err != nil {
		return err
	}

	return nil
}


File: /scripts\docker-compose.yml
version: '3.7'
services:
  mikrotik_provisioning:
    image: ogi4i/mikrotik-provisioning:latest
    container_name: mikrotik_provisioning
    hostname: mikrotik_provisioning
    network_mode: bridge
    depends_on:
      - mongo_provisioning
    ports:
      - 3333:3333
    volumes:
      - ./config.yml:/app/config.yml
  mongo_provisioning:
    image: mongo:4.2
    container_name: mongo_provisioning
    hostname: mongo_provisioning
    network_mode: bridge
    volumes:
      - ../.mongo:/data/db
    ports:
      - 27018:27017

File: /scripts\Dockerfile
###############################################################################
# BUILD STAGE

FROM golang:1.15-alpine as builder
RUN mkdir /build
ADD . /build/
WORKDIR /build
RUN apk --no-cache add git
RUN CGO_ENABLED=0 GOOS=linux go build -a -installsuffix cgo -ldflags '-extldflags "-static"' -o app ./cmd/mikrotik_provisioning

###############################################################################
# PACKAGE STAGE

FROM scratch
COPY --from=builder /build/app /app/
COPY --from=builder /build/templates /app/templates
WORKDIR /app
CMD ["./app"]


File: /templates\GetAddressList
do {
    :local newACL {"#(.Name)#"={#(range $index, $addr := .Addresses)##(if $index)#;#(end)#"#($addr.Address)#"={"disabled"=#($addr.Disabled)#; "comment"="#($addr.Comment)#"; "exists"=false}#(end)#}}
    :local listOfACLs ({})

    :foreach l,addrs in=$newACL do={
        :set listOfACLs [:toarray ($listOfACLs . "," . $l)]
        :foreach k,v in=$addrs do={
            :foreach addr in=[/ip firewall address-list find list=$l dynamic=no] do={
                :if ([/ip firewall address-list get $addr address] = $k) do={
                    :local c [/ip firewall address-list get $addr comment]
                    :set ($v->"exists") true
                    :if ([/ip firewall address-list get $addr disabled] != ($v->"disabled")) do={
                        :if (($v->"disabled") = false) do={
                            /ip firewall address-list enable $addr
                            :log info ("Enabled address: " . $k . " for address-list: " . $l)
                        } else={
                            /ip firewall address-list disable $addr
                            :log info ("Disabled address: " . $k . " for address-list: " . $l)
                        }
                    }
                    :if ($c != ($v->"comment")) do={
                        /ip firewall address-list set $addr comment=($v->"comment")
                        :log info ("Changed comment for address: \"" . $k . "\" from: \"" . $c . "\" to: \"" . ($v->"comment") . "\" for address-list: " . $l)
                    }
                }
            }
        }
    }
    :foreach l,addrs in=$newACL do={
        :foreach k,v in=$addrs do={
            :if (($v->"exists") = false) do={
                :local c ($v->"comment")
                :local d
                :if (($v->"disabled") = false) do={
                    :set $d "no"
                } else={
                    :set $d "yes"
                }
                /ip firewall address-list add list=$l address=$k disabled=$d comment=$c
                :log info ("Added new address: \"" . $k . "\", enabled: " . !($v->"disabled") . ", comment: \"" . $c . "\" for address-list: " . $l)
            }
        }
    }
    :foreach l in=$listOfACLs do={
        :foreach id in=[/ip firewall address-list find list=$l dynamic=no] do={
            :local address [/ip firewall address-list get $id address]
            :if ([:typeof ($newACL->$l->$address)] != [:typeof ({})]) do={
                /ip firewall address-list remove $addr
                :log info ("Removed old address: " . $address . " from address-list: " . $l)
            }
        }
    }
} on-error={
    :log error "Error while executing UpdateACL script"
}

File: /templates\GetAddressLists
do {
    :local newACL {#(range $index, $acl := .)##(if $index)#;#(end)#"#($acl.Name)#"={#(range $i, $addr := $acl.Addresses)##(if $i)#;#(end)#"#($addr.Address)#"={"disabled"=#($addr.Disabled)#; "comment"="#($addr.Comment)#"; "exists"=false}#(end)#}#(end)#}
    :local listOfACLs ({})

    :foreach l,addrs in=$newACL do={
        :set listOfACLs [:toarray ($listOfACLs . "," . $l)]
        :foreach k,v in=$addrs do={
            :foreach addr in=[/ip firewall address-list find list=$l dynamic=no] do={
                :if ([/ip firewall address-list get $addr address] = $k) do={
                    :local c [/ip firewall address-list get $addr comment]
                    :set ($v->"exists") true
                    :if ([/ip firewall address-list get $addr disabled] != ($v->"disabled")) do={
                        :if (($v->"disabled") = false) do={
                            /ip firewall address-list enable $addr
                            :log info ("Enabled address: " . $k . " for address-list: " . $l)
                        } else={
                            /ip firewall address-list disable $addr
                            :log info ("Disabled address: " . $k . " for address-list: " . $l)
                        }
                    }
                    :if ($c != ($v->"comment")) do={
                        /ip firewall address-list set $addr comment=($v->"comment")
                        :log info ("Changed comment for address: \"" . $k . "\" from: \"" . $c . "\" to: \"" . ($v->"comment") . "\" for address-list: " . $l)
                    }
                }
            }
        }
    }
    :foreach l,addrs in=$newACL do={
        :foreach k,v in=$addrs do={
            :if (($v->"exists") = false) do={
                :local c ($v->"comment")
                :local d
                :if (($v->"disabled") = false) do={
                    :set $d "no"
                } else={
                    :set $d "yes"
                }
                /ip firewall address-list add list=$l address=$k disabled=$d comment=$c
                :log info ("Added new address: \"" . $k . "\", enabled: " . !($v->"disabled") . ", comment: \"" . $c . "\" for address-list: " . $l)
            }
        }
    }
    :foreach l in=$listOfACLs do={
        :foreach id in=[/ip firewall address-list find list=$l dynamic=no] do={
            :local address [/ip firewall address-list get $id address]
            :if ([:typeof ($newACL->$l->$address)] != [:typeof ({})]) do={
                /ip firewall address-list remove $addr
                :log info ("Removed old address: " . $address . " from address-list: " . $l)
            }
        }
    }
} on-error={
    :log error "Error while executing UpdateACL script"
}

