# Repository Information
Name: lua-mikrotik

# Directory Structure
Directory structure:
└── github_repos/lua-mikrotik/
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
    │   │       ├── pack-6a2301ab1f3906cec87da239f113ef11c8a891c0.idx
    │   │       └── pack-6a2301ab1f3906cec87da239f113ef11c8a891c0.pack
    │   ├── packed-refs
    │   └── refs/
    │       ├── heads/
    │       │   └── master
    │       ├── remotes/
    │       │   └── origin/
    │       │       └── HEAD
    │       └── tags/
    ├── doc/
    │   └── api.md
    ├── LICENSE
    ├── Mikrotik.lua
    ├── README.md
    └── rockspecs/
        └── lua-mikrotik-1.1-0.rockspec


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
	url = https://github.com/karolba/lua-mikrotik.git
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
0000000000000000000000000000000000000000 d98e072aa5b4039eb68e0de51d9bef41e0c1cde9 vivek-dodia <vivek.dodia@icloud.com> 1738606299 -0500	clone: from https://github.com/karolba/lua-mikrotik.git


File: /.git\logs\refs\heads\master
0000000000000000000000000000000000000000 d98e072aa5b4039eb68e0de51d9bef41e0c1cde9 vivek-dodia <vivek.dodia@icloud.com> 1738606299 -0500	clone: from https://github.com/karolba/lua-mikrotik.git


File: /.git\logs\refs\remotes\origin\HEAD
0000000000000000000000000000000000000000 d98e072aa5b4039eb68e0de51d9bef41e0c1cde9 vivek-dodia <vivek.dodia@icloud.com> 1738606299 -0500	clone: from https://github.com/karolba/lua-mikrotik.git


File: /.git\packed-refs
# pack-refs with: peeled fully-peeled sorted 
d98e072aa5b4039eb68e0de51d9bef41e0c1cde9 refs/remotes/origin/master
d98e072aa5b4039eb68e0de51d9bef41e0c1cde9 refs/tags/v1.1-0


File: /.git\refs\heads\master
d98e072aa5b4039eb68e0de51d9bef41e0c1cde9


File: /.git\refs\remotes\origin\HEAD
ref: refs/remotes/origin/master


File: /doc\api.md
### `Mikrotik:create(<ip>, [port], [timeout])`

Connects to the given `ip` address and `port`. The optional `timeout` parameter tells
`luasocket` how long to wait on reads in seconds.  Creates a `mt` object, returns `nil` on connection failures.

If `port` is unspecified, the default value of `8728` is used.

### `mt:login(<username>, <password>)`

Authenticates with the endpoint. This has to be the first method called on the `mt` object. Returns
`true` on a successfull login and `nil` on failure.

### `mt:sendSentence(<sentence>, [callback])`

Sends the `sentence` to the remote endpoint. Sentence should always be a table, as per the 
[RouterOS API](https://wiki.mikrotik.com/wiki/Manual:API). Returns number of bytes written,
or `nil` on failure.

If the optional `callback` parameter is provided, the sentence will be assigned a unique tag,
and every received response with the same tag will be passed to the callback, instead of being
returned from `mt:readSentence()`. Note that for this to work `mt:readSentence()` or `mt:wait()`
has to be called, as this library is not asynchronous.

Example usage:

```lua
local packages = 0

mt:sendSentence({ '/system/package/print' }, function(res)
    if res.type == '!re' then
        print("RouterOS package: " .. res['=name'] .. " version " .. res['=version'])
        packages = packages + 1
    elseif res.type == '!done' then
        print("Number of packages: " .. packages)
    end
end)

mt:wait()
```

### `mt:readSentence()`

Reads the next sentence from the remote endpoint, synchronously. Depending on the value of `timeout`
given in the constructor, either blocks indefinitely or `timeout` seconds. Returns `nil` on failure,
throws an `error` on timeout. Does not return sentences with registered callback.

The returned `sentence` table is mapped from the response. The first line of the received sentence,
(typically one of `!re`, `!data`, `!trap`, or `!fatal`) becomes the `sentence.type` field.

For example, this raw sentence received from RouterOS

    {
        '!re',
        '=disabled=no',
        '=name=routeros-x86',
        ''
    }

would be translated to and returned from `readSentence()` as

    {
        type = '!re',
        '=disabled' = 'no',
        '=name' = 'routeros-x86'
    }

### `mt:wait()`

Waits for all tagged sentences with callbacks to complete. Returns `true` when a non-handled sentence is
ready to be read by `mt:readSentence()` and `nil` on failure.

### `mt.debug = <true/false>`

Whether to display all communication with the endpoint on stdout


File: /LICENSE
MIT License

Copyright (c) 2018 Karol Baraniecki

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.


File: /Mikrotik.lua
-- Compatibility with Lua 5.1 with no built-in bitwise operations. 
if not pcall(require, 'bit32') then
    -- The BitOp library required.
    require('bit')
    bit32 = bit
end
local bnot, band, bor = bit32.bnot, bit32.band, bit32.bor
local lrotate, rrotate = bit32.lrotate or bit32.lshift, bit32.rrotate or bit32.rshift

-- openresty?
local has_ngx, ngx = pcall(require, 'ngx')

local socket = (has_ngx and ngx.socket) or require('socket') 
local md5 = (has_ngx and ngx.md5) or require('md5')


local DEFAULT_PORT = 8728

local function table_empty(t)
    return next(t) == nil
end

local function byte(int, byteIdx)
    local shifted = rrotate(int, 8 * byteIdx)
    return band(shifted, 0xff)
end

local function hextostring(str)
    return (str:gsub('..', function(encodedByte)
        return string.char(tonumber(encodedByte, 16))
    end))
end

local function md5sumhex(str)
    if type(md5) == 'function' then
        -- Openresty md5
        return md5(str)
    elseif md5.sumhexa then
        -- MD5
        return md5.sumhexa(str)
    elseif md5.new and md5.tohex then
        -- md5.lua
        local sum = md5.new()
        sum:update(str)
        return md5.tohex(sum:finish())
    else
        error('Unknown md5 library detected')
    end
end

local function parseWord(word)
    local _, equalsPos = string.find(word, '.=')
    if not equalsPos then
        return "type", word
    end

    local tag = word:sub(1, equalsPos - 1)
    local value = word:sub(equalsPos + 1)
    return tag, value
end

local function encodeLength(l)
    local char = string.char

    if l < 0x80 then
        return char(l)
    elseif l < 0x4000 then
        local l = bor(l, 0x8000)
        return
            char(byte(l, 1)) ..
            char(byte(l, 0))
    elseif l < 0x200000 then
        local l = bor(l, 0xC00000)
        return
            char(byte(l, 2)) ..
            char(byte(l, 1)) ..
            char(byte(l, 0))
    elseif l < 0x10000000 then
        local l = bor(l, 0xE0000000)
        return
            char(byte(l, 3)) ..
            char(byte(l, 2)) ..
            char(byte(l, 1)) ..
            char(byte(l, 0))
    else
        return
            '\xF0' .. 
            char(byte(l, 3)) ..
            char(byte(l, 2)) ..
            char(byte(l, 1)) ..
            char(byte(l, 0))
    end
end

local function encodeWord(word)
    return encodeLength(string.len(word)) .. word
end

-- class Mikrotik

local Mikrotik = {}
Mikrotik.__index = Mikrotik

function Mikrotik:create(address, port, timeout)
    local mtk = {}
    setmetatable(mtk, Mikrotik)
    
    local client = socket.tcp()
    if timeout then
        client:settimeout(timeout)
    end
    if not client:connect(address, port or DEFAULT_PORT) then
        return nil
    end

    mtk.client = client
    mtk.nextSentenceTagId = 0
    mtk.tagToCallbackTable = {}
    mtk.debug = false

    return mtk
end

function Mikrotik:readByte()
    return self.client:receive(1):byte(1)
end

function Mikrotik:readLen()
    local l = self:readByte()
    if band(l, 0x80) == 0x00 then
        return l
    elseif band(l, 0xc0) == 0x80 then
        l = band(l, bnot(0xc0))

        return
            lrotate(l, 8) +
            self:readByte()
    elseif band(l, 0xe0) == 0xc0 then
        l = band(l, bnot(0xc0))

        return 
            lrotate(l, 16) +
            lrotate(self:readByte(), 8) +
            self:readByte() 
    elseif band(l, 0xf0) == 0xe0 then
        l = band(l, bnot(0xf0))

        return 
            lrotate(l, 24) + 
            lrotate(self:readByte(), 16) +
            lrotate(self:readByte(), 8) +
            self:readByte()
    elseif band(l, 0xf8) == 0xf0 then
        return
            lrotate(self:readByte(), 24) +
            lrotate(self:readByte(), 16) +
            lrotate(self:readByte(), 8) +
            self:readByte()
    end
end

-- Gets a tag from a message going to be sent
local function getTag(sentence)
    local function starts_with(str, start)
        return str:sub(1, #start) == start
    end

    local TAG_PREFIX = '.tag='

    for i, word in ipairs(sentence) do
        if starts_with(word, TAG_PREFIX) then
            return word:sub(#TAG_PREFIX + 1)
        end
    end

    return nil
end

function Mikrotik:sendSentence(sentence, callback) 
    if self.debug then
        for k, v in ipairs(sentence) do
            print(">>>>>>", v)
        end
    end
    local message = ""
    for i, word in ipairs(sentence) do
        message = message .. encodeWord(word)
    end

    if callback then
        local tag = getTag(sentence)
        if not tag then
            tag = self:nextTag()
            message = message .. encodeWord('.tag=' .. tag)
            if self.debug then
                print(">>>>>> (added by sendSentence) ", '.tag=' .. tag)
            end
        end

        self.tagToCallbackTable[tag] = callback
    end

    if self.debug then
        print(">>>>>>")
    end
    -- The closing empty word - essentialy a null byte
    message = message .. '\0'
    return self:send(message)
end

function Mikrotik:readWord()
    local len = self:readLen()
    if not len or len == 0 then
        return nil
    end
    return self.client:receive(len)
end

function Mikrotik:readSentenceBypassingCallbacks()
    local sentence = {}
    while true do
        local word = self:readWord()
        if not word then
            if self.debug then
                for k, v in pairs(sentence) do
                    print("<<<<<<", k, v)
                end
                print("<<<<<<")
            end
            return sentence
        end

        local tag, value = parseWord(word)
        sentence[tag] = value
    end
end

function Mikrotik:handleCallback(sentence)
    local tag = sentence['.tag']
    if not tag then
        return false
    end

    local callback = self.tagToCallbackTable[tag]
    if not callback then
        return false
    end

    callback(sentence)

    local type = sentence.type
    if type == '!done' or type == '!trap' then
        self.tagToCallbackTable[tag] = nil
    end

    return true
end

function Mikrotik:readSentence()
    if self.queuedSentence then
        self.queuedSentence = nil
        return self.queuedSentence
    end
    local sentence
    repeat 
        sentence = self:readSentenceBypassingCallbacks()
    until not self:handleCallback(sentence) or table_empty(self.tagToCallbackTable)
    return sentence
end

function Mikrotik:send(message)
    return self.client:send(message)
end

function Mikrotik:wait()
    local sentence = self:readSentence()
    self.queuedSentence = sentence
    return sentence
end

function Mikrotik:nextTag()
    self.nextSentenceTagId = self.nextSentenceTagId + 1
    return "lua-mtk-" .. self.nextSentenceTagId
end

function Mikrotik:login(user, pass)
    self:sendSentence({ "/login" })

    local loginResponse = self:readSentence()
    if not loginResponse or loginResponse.type ~= '!done' then
        return nil
    end

    local challange = hextostring(loginResponse['=ret'])

    local sum = md5sumhex('\0' .. pass .. challange)

    self:sendSentence({ "/login", "=name=" .. user, "=response=00" .. sum })
 
    local challangeResponse = self:readSentence()
    if not challangeResponse or challangeResponse.type ~= '!done' then
        -- Bad credentials?
        return nil
    end

    return true
end

return Mikrotik


File: /README.md
# lua-mikrotik

A lightweight lua library for talking to the [Mikrotik RouterOS API](https://wiki.mikrotik.com/wiki/Manual:API).

## Requirements: 

* Either:
	* [luasocket](https://github.com/diegonehab/luasocket)
	* Either the [kikito's md5 library](https://github.com/kikito/md5.lua) or the [keplerproject's md5 library](https://github.com/keplerproject/md5)
	* On older Lua versions with no `bit32` (`<= 5.1`), either [BitOp](http://luaforge.net/projects/bit/), or [BitLib](https://github.com/LuaDist/bitlib)
* or [OpenResty](https://openresty.org/en/), which contains all these dependencies.

## Documentation:

For documentation see [doc/api.md](https://github.com/karolba/lua-mikrotik/blob/master/doc/api.md).

## Examples:

Starting a RouterOS script from `/system/script` by name synchronously:

```lua
local Mikrotik = require 'Mikrotik'

local function runScript(mt, scriptname)
    assert(mt:sendSentence({ '/system/script/print', '?name=' .. scriptname, '=.proplist=.id' }))

    local message = assert(mt:readSentence())
    assert(message.type == '!re')
    assert(mt:readSentence().type == '!done')

    assert(mt:sendSentence({ '/system/script/run', '=number=' .. message['=.id']}))
    assert(mt:readSentence().type == '!done')

    print('OK!')
end

local mt = assert(Mikrotik:create('192.168.88.1'))
assert(mt:login('login', 'password'), 'Failed login')

runScript(mt, 'example-routeros-script-name')
```

The same result can be accomplished by using "tagged sentences" and callbacks:

```lua
local Mikrotik = require 'Mikrotik'

local function runScript(mt, scriptname)
    assert(mt:sendSentence({ '/system/script/print', '?name=' .. scriptname, '=.proplist=.id' }, function(res)
        if res.type == '!re' then
            assert(mt:sendSentence({ '/system/script/run', '=number=' .. res['=.id'] }, function(res)
                if res.type == '!done' then
                    print('OK!')
                end
            end))
        end
    end))
end

local mt = assert(Mikrotik:create('192.168.88.1'))
assert(mt:login('login', 'password'), 'Failed login')

runScript(mt, 'example-routeros-script-name')

assert(mt:wait())
```


File: /rockspecs\lua-mikrotik-1.1-0.rockspec
package = "lua-mikrotik"
version = "1.1-0"
source = {
   url = "git://github.com/karolba/lua-mikrotik",
   tag = "v1.1-0"
}
description = {
   summary = "A lightweight library for communicating with the Mikrotik RouterOS API",
   homepage = "https://github.com/karolba/lua-mikrotik",
   license = "MIT/X11"
}
dependencies = {
   "lua >= 5.1, < 5.4",
   "luasocket > 2.0, < 4.0",
   "md5 >= 1.0, < 1.3"
}
build = {
   type = "builtin",
   modules = {
      Mikrotik = "Mikrotik.lua"
   }
}


