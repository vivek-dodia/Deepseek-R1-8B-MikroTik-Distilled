# Repository Information
Name: MikrotikJSON4DatadogAPI

# Directory Structure
Directory structure:
└── github_repos/MikrotikJSON4DatadogAPI/
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
    │   │       ├── pack-61d0288f6be9bc4a3fbb68bf101ef3607938e721.idx
    │   │       └── pack-61d0288f6be9bc4a3fbb68bf101ef3607938e721.pack
    │   ├── packed-refs
    │   └── refs/
    │       ├── heads/
    │       │   └── master
    │       ├── remotes/
    │       │   └── origin/
    │       │       └── HEAD
    │       └── tags/
    ├── datadog-dashboard-examples/
    │   └── dual-wan-example.json
    ├── DatadogMonitoring.rsc
    ├── LICENSE
    ├── LoadGlobalFunctions.rsc
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
	url = https://github.com/mtrimarchi/MikrotikJSON4DatadogAPI.git
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
0000000000000000000000000000000000000000 6851761a4ac045be26bfef93a3eed29cdeca6cdb vivek-dodia <vivek.dodia@icloud.com> 1738605958 -0500	clone: from https://github.com/mtrimarchi/MikrotikJSON4DatadogAPI.git


File: /.git\logs\refs\heads\master
0000000000000000000000000000000000000000 6851761a4ac045be26bfef93a3eed29cdeca6cdb vivek-dodia <vivek.dodia@icloud.com> 1738605958 -0500	clone: from https://github.com/mtrimarchi/MikrotikJSON4DatadogAPI.git


File: /.git\logs\refs\remotes\origin\HEAD
0000000000000000000000000000000000000000 6851761a4ac045be26bfef93a3eed29cdeca6cdb vivek-dodia <vivek.dodia@icloud.com> 1738605958 -0500	clone: from https://github.com/mtrimarchi/MikrotikJSON4DatadogAPI.git


File: /.git\packed-refs
# pack-refs with: peeled fully-peeled sorted 
6851761a4ac045be26bfef93a3eed29cdeca6cdb refs/remotes/origin/master


File: /.git\refs\heads\master
6851761a4ac045be26bfef93a3eed29cdeca6cdb


File: /.git\refs\remotes\origin\HEAD
ref: refs/remotes/origin/master


File: /datadog-dashboard-examples\dual-wan-example.json
{
    "title":"Mikrotik Router with Dual WAN",
    "description":"Dashboard for a router with ether1 and ether2 used as uplink WAN connectivity",
    "widgets":[
       {
          "id":123456789001,
          "definition":{
             "type":"timeseries",
             "requests":[
                {
                   "q":"avg:system.cpu.load{$host}",
                   "display_type":"line",
                   "style":{
                      "palette":"dog_classic",
                      "line_type":"solid",
                      "line_width":"normal"
                   }
                }
             ],
             "custom_links":[
                
             ],
             "yaxis":{
                "min":"0",
                "max":"100"
             },
             "markers":[
                {
                   "value":"y = 30",
                   "display_type":"warning dashed"
                },
                {
                   "value":"40 < y < 100",
                   "display_type":"error dashed",
                   "label":"Error threshold"
                }
             ],
             "title":"System CPU Load",
             "title_size":"13",
             "title_align":"center",
             "show_legend":true,
             "legend_size":"0"
          },
          "layout":{
             "x":1,
             "y":20,
             "width":47,
             "height":15
          }
       },
       {
          "id":123456789002,
          "definition":{
             "type":"timeseries",
             "requests":[
                {
                   "q":"sum:system.memory.free{$host}, sum:system.memory.total{$host}-sum:system.memory.free{$host}",
                   "metadata":[
                      {
                         "expression":"sum:system.memory.free{$host}",
                         "alias_name":"Free Memory"
                      },
                      {
                         "expression":"sum:system.memory.total{$host}-sum:system.memory.free{$host}",
                         "alias_name":"Used Memory"
                      }
                   ],
                   "display_type":"area",
                   "style":{
                      "palette":"orange",
                      "line_type":"solid",
                      "line_width":"normal"
                   }
                }
             ],
             "custom_links":[
                
             ],
             "yaxis":{
                "min":"0"
             },
             "title":"System RAM",
             "title_size":"13",
             "title_align":"center",
             "show_legend":true,
             "legend_size":"0"
          },
          "layout":{
             "x":49,
             "y":20,
             "width":47,
             "height":15
          }
       },
       {
          "id":123456789003,
          "definition":{
             "type":"timeseries",
             "requests":[
                {
                   "q":"avg:system.firewall.connections{$host}",
                   "display_type":"bars",
                   "style":{
                      "palette":"orange",
                      "line_type":"solid",
                      "line_width":"normal"
                   }
                }
             ],
             "custom_links":[
                
             ],
             "title":"Connection Tracking Active Sessions",
             "title_size":"13",
             "title_align":"center",
             "show_legend":true,
             "legend_size":"0"
          },
          "layout":{
             "x":1,
             "y":36,
             "width":47,
             "height":15
          }
       },
       {
          "id":12345678900,
          "definition":{
             "type":"timeseries",
             "requests":[
                {
                   "q":"(avg:system.interfaces.ether1.rx_bits_per_second{$host}+avg:system.interfaces.ether2.rx_bits_per_second{$host})*1000",
                   "metadata":[
                      {
                         "expression":"(avg:system.interfaces.ether1.rx_bits_per_second{$host}+avg:system.interfaces.ether2.rx_bits_per_second{$host})*1000",
                         "alias_name":"WAN Download"
                      }
                   ],
                   "display_type":"area",
                   "style":{
                      "palette":"orange",
                      "line_type":"solid",
                      "line_width":"normal"
                   }
                },
                {
                   "q":"(avg:system.interfaces.ether1.tx_bits_per_second{$host}+avg:system.interfaces.ether2.tx_bits_per_second{$host})*1000",
                   "metadata":[
                      {
                         "expression":"(avg:system.interfaces.ether1.tx_bits_per_second{$host}+avg:system.interfaces.ether2.tx_bits_per_second{$host})*1000",
                         "alias_name":"WAN Upload"
                      }
                   ],
                   "display_type":"area",
                   "style":{
                      "palette":"purple",
                      "line_type":"solid",
                      "line_width":"normal"
                   }
                }
             ],
             "yaxis":{
                "label":"",
                "scale":"linear",
                "min":"auto",
                "max":"auto",
                "include_zero":true
             },
             "title":"WAN I/O Rate",
             "title_size":"13",
             "title_align":"center",
             "time":{
                
             },
             "show_legend":true,
             "legend_size":"0"
          },
          "layout":{
             "x":49,
             "y":36,
             "width":47,
             "height":15
          }
       },
       {
          "id":123456789005,
          "definition":{
             "type":"timeseries",
             "requests":[
                {
                   "q":"max:system.disk.writesect.total{$host}",
                   "display_type":"area",
                   "style":{
                      "palette":"grey",
                      "line_type":"solid",
                      "line_width":"normal"
                   }
                }
             ],
             "custom_links":[
                
             ],
             "title":"System disk total write sectors",
             "title_size":"13",
             "title_align":"center",
             "show_legend":true,
             "legend_size":"0"
          },
          "layout":{
             "x":1,
             "y":100,
             "width":47,
             "height":15
          }
       },
       {
          "id":123456789006,
          "definition":{
             "type":"timeseries",
             "requests":[
                {
                   "q":"avg:system.disk.badblocks{$host}",
                   "display_type":"line",
                   "style":{
                      "palette":"warm",
                      "line_type":"solid",
                      "line_width":"thick"
                   }
                }
             ],
             "custom_links":[
                
             ],
             "yaxis":{
                "min":"0"
             },
             "markers":[
                {
                   "value":"y > 1",
                   "display_type":"error dashed",
                   "label":"Bad blocks"
                }
             ],
             "title":"System HDD Bad Blocks",
             "title_size":"13",
             "title_align":"center",
             "show_legend":true,
             "legend_size":"0"
          },
          "layout":{
             "x":49,
             "y":100,
             "width":47,
             "height":15
          }
       },
       {
          "id":123456789007,
          "layout":{
             "x":1,
             "y":2,
             "width":15,
             "height":8
          },
          "definition":{
             "title":"CPU Load",
             "title_size":"13",
             "title_align":"center",
             "type":"alert_value",
             "alert_id":"12345678904",
             "unit":"%",
             "text_align":"center",
             "precision":0
          }
       },
       {
          "id":123456789008,
          "layout":{
             "x":17,
             "y":2,
             "width":15,
             "height":8
          },
          "definition":{
             "title":"RAM Usage",
             "title_size":"13",
             "title_align":"center",
             "type":"alert_value",
             "alert_id":"12345678903",
             "unit":"%",
             "text_align":"center",
             "precision":0
          }
       },
       {
          "id":123456789009,
          "definition":{
             "type":"query_value",
             "requests":[
                {
                   "q":"avg:system.uptime{$host}",
                   "aggregator":"last"
                }
             ],
             "custom_links":[
                
             ],
             "title":"System Uptime",
             "title_size":"13",
             "title_align":"center",
             "time":{
                "live_span":"1m"
             },
             "autoscale":true,
             "precision":2
          },
          "layout":{
             "x":17,
             "y":11,
             "width":15,
             "height":8
          }
       },
       {
          "id":123456789010,
          "layout":{
             "x":65,
             "y":1,
             "width":31,
             "height":18
          },
          "definition":{
             "title":"Monitoring CPU",
             "title_size":"13",
             "title_align":"center",
             "time":{
                "live_span":"alert"
             },
             "type":"alert_graph",
             "alert_id":"12345678901",
             "viz_type":"timeseries"
          }
       },
       {
          "id":123456789011,
          "layout":{
             "x":33,
             "y":1,
             "width":31,
             "height":18
          },
          "definition":{
             "title":"Monitoring RAM",
             "title_size":"13",
             "title_align":"center",
             "time":{
                "live_span":"alert"
             },
             "type":"alert_graph",
             "alert_id":"12345678902",
             "viz_type":"timeseries"
          }
       },
       {
          "id":123456789012,
          "definition":{
             "type":"timeseries",
             "requests":[
                {
                   "q":"avg:system.health.consumption{$host}/10",
                   "metadata":[
                      {
                         "expression":"avg:system.health.consumption{$host}/10",
                         "alias_name":"W"
                      }
                   ],
                   "display_type":"line",
                   "style":{
                      "palette":"warm",
                      "line_type":"solid",
                      "line_width":"thick"
                   }
                },
                {
                   "q":"avg:system.health.current{$host}/1000",
                   "metadata":[
                      {
                         "expression":"avg:system.health.current{$host}/1000",
                         "alias_name":"A"
                      }
                   ],
                   "display_type":"line",
                   "style":{
                      "palette":"cool",
                      "line_type":"solid",
                      "line_width":"thin"
                   }
                },
                {
                   "q":"avg:system.health.voltage{$host}/10",
                   "metadata":[
                      {
                         "expression":"avg:system.health.voltage{$host}/10",
                         "alias_name":"V"
                      }
                   ],
                   "display_type":"line",
                   "style":{
                      "palette":"cool",
                      "line_type":"solid",
                      "line_width":"thin"
                   }
                }
             ],
             "yaxis":{
                "label":"",
                "scale":"linear",
                "min":"auto",
                "max":"auto",
                "include_zero":true
             },
             "title":"System Health",
             "title_size":"13",
             "title_align":"center",
             "time":{
                
             },
             "show_legend":true,
             "legend_size":"0"
          },
          "layout":{
             "x":1,
             "y":52,
             "width":47,
             "height":23
          }
       },
       {
          "id":123456789013,
          "definition":{
             "type":"timeseries",
             "requests":[
                {
                   "q":"avg:system.health.fanspeed.1{$host}",
                   "metadata":[
                      {
                         "expression":"avg:system.health.fanspeed.1{$host}",
                         "alias_name":"RPM"
                      }
                   ],
                   "display_type":"line",
                   "style":{
                      "palette":"dog_classic",
                      "line_type":"solid",
                      "line_width":"normal"
                   }
                },
                {
                   "q":"avg:system.health.fanspeed.2{$host}",
                   "metadata":[
                      {
                         "expression":"avg:system.health.fanspeed.2{$host}",
                         "alias_name":"RPM"
                      }
                   ],
                   "display_type":"line",
                   "style":{
                      "palette":"dog_classic",
                      "line_type":"solid",
                      "line_width":"normal"
                   }
                }
             ],
             "yaxis":{
                "label":"",
                "scale":"linear",
                "min":"auto",
                "max":"auto",
                "include_zero":true
             },
             "title":"FAN Speed",
             "title_size":"13",
             "title_align":"center",
             "time":{
                
             },
             "show_legend":true,
             "legend_size":"0"
          },
          "layout":{
             "x":49,
             "y":76,
             "width":47,
             "height":23
          }
       },
       {
          "id":123456789014,
          "definition":{
             "type":"timeseries",
             "requests":[
                {
                   "q":"avg:system.health.temperature{$host}",
                   "metadata":[
                      {
                         "expression":"avg:system.health.temperature{$host}",
                         "alias_name":"°C"
                      }
                   ],
                   "display_type":"line",
                   "style":{
                      "palette":"dog_classic",
                      "line_type":"solid",
                      "line_width":"normal"
                   }
                },
                {
                   "q":"avg:system.health.temperature.cpu{$host}",
                   "metadata":[
                      {
                         "expression":"avg:system.health.temperature.cpu{$host}",
                         "alias_name":"°C"
                      }
                   ],
                   "display_type":"line",
                   "style":{
                      "palette":"dog_classic",
                      "line_type":"solid",
                      "line_width":"normal"
                   }
                }
             ],
             "yaxis":{
                "label":"",
                "scale":"linear",
                "min":"auto",
                "max":"auto",
                "include_zero":true
             },
             "title":"Temperature",
             "title_size":"13",
             "title_align":"center",
             "time":{
                
             },
             "show_legend":true,
             "legend_size":"0"
          },
          "layout":{
             "x":1,
             "y":76,
             "width":47,
             "height":23
          }
       },
       {
          "id":123456789015,
          "definition":{
             "type":"timeseries",
             "requests":[
                {
                   "q":"avg:system.uptime{$host}",
                   "display_type":"line",
                   "style":{
                      "palette":"dog_classic",
                      "line_type":"solid",
                      "line_width":"normal"
                   }
                }
             ],
             "yaxis":{
                "label":"",
                "scale":"linear",
                "min":"auto",
                "max":"auto",
                "include_zero":true
             },
             "title":"System Uptime",
             "title_size":"13",
             "title_align":"center",
             "time":{
                
             },
             "show_legend":true,
             "legend_size":"0"
          },
          "layout":{
             "x":49,
             "y":52,
             "width":47,
             "height":23
          }
       },
       {
          "id":123456789016,
          "layout":{
             "x":1,
             "y":11,
             "width":15,
             "height":8
          },
          "definition":{
             "title":"Temperature",
             "title_size":"13",
             "title_align":"center",
             "type":"alert_value",
             "alert_id":"11563128",
             "unit":"°C",
             "text_align":"center",
             "precision":2
          }
       }
    ],
    "template_variables":[
       {
          "name":"host",
          "default":"*",
          "prefix":"host"
       }
    ],
    "layout_type":"free",
    "is_read_only":false,
    "notify_list":[
       
    ],
    "id":"xxx-xxx-xxx"
 }

File: /DatadogMonitoring.rsc
{

# Datadog API Settings
:local apikey "a1b2c3...DATADOG APIKEY";
:local applicationkey "a1b2c3...DATADOG APPLICATION KEY";
:local ddendpoint "https://app.datadoghq.com/api/v1";
:local type "gauge";
:local tags "source:mikrotik";

# Misc variables for stuff and things.
:local metrics;
:local metric "";
:local value "";
:local httpdata "";
:local datetime [$timestamp];
:local identity [/system identity get name];

# Exceptional metrics pre-declared due to some additional checks

# system resource bad-blocks
:local badblocks [/system resource get bad-blocks];
:if ([:len $badblocks] = 0) do={
    :set badblocks 0;
}

# system resource write-sect-total
:local writesecttotal [/system resource get write-sect-total];
:if ([:len $writesecttotal] = 0) do={
    :set writesecttotal 0;
}

# system resource write-sect-since-reboot
:local writesectsincereboot [/system resource get write-sect-since-reboot];
:if ([:len $writesectsincereboot] = 0) do={
    :set writesectsincereboot 0;
}

# system health voltage
:local healthvoltage [/system health get voltage];
:if ([:len $healthvoltage] = 0) do={
    :set healthvoltage 0;
}

# system health current
:local healthcurrent [/system health get current];
:if ([:len $healthcurrent] = 0) do={
    :set healthcurrent 0;
}

# system health temperature
:local healthtemperature [/system health get temperature];
:if ([:len $healthtemperature] = 0) do={
    :set healthtemperature 0;
}

# system health cpu-temperature
:local healthcputemperature [/system health get cpu-temperature];
:if ([:len $healthcputemperature] = 0) do={
    :set healthcputemperature 0;
}

# system health power-consumption
:local healthpowerconsumption [/system health get power-consumption];
:if ([:len $healthpowerconsumption] = 0) do={
    :set healthpowerconsumption 0;
}

# system health fan1-speed
:local healthfan1speed [/system health get fan1-speed];
:if ([:len $healthfan1speed] = 0) do={
    :set healthfan1speed 0;
}

# system health fan2-speed
:local healthfan2speed [/system health get fan2-speed];
:if ([:len $healthfan2speed] = 0) do={
    :set healthfan2speed 0;
}

# Create metrics array
:set metrics {
    "system.cpu.load"=[/system resource get cpu-load];
    "system.memory.total"=[/system resource get total-memory];
    "system.memory.free"=[/system resource get free-memory];
    "system.disk.hddspace.total"=[/system resource get total-hdd-space];
    "system.disk.hddspace.free"=[/system resource get free-hdd-space];
    "system.disk.writesect.total"=$writesecttotal;
    "system.disk.writesect.sincereboot"=$writesectsincereboot;
    "system.disk.badblocks"=$badblocks;
    "system.firewall.connections"=[/ip firewall connection print count-only];
    "system.ppp.all"=[/ppp active print count-only];
    "system.ppp.sstp"=[/ppp active print count-only where service=sstp];
    "system.ppp.pptp"=[/ppp active print count-only where service=pptp];
    "system.ppp.ovpn"=[/ppp active print count-only where service=ovpn];
    "system.ppp.pppoe"=[/ppp active print count-only where service=pppoe];
    "system.ppp.l2tp"=[/ppp active print count-only where service=l2tp];
    "system.health.voltage"=$healthvoltage;
    "system.health.current"=$healthcurrent;
    "system.health.temperature"=$healthtemperature;
    "system.health.temperature.cpu"=$healthcputemperature;
    "system.health.consumption"=$healthpowerconsumption;
    "system.health.fanspeed.1"=$healthfan1speed;
    "system.health.fanspeed.2"=$healthfan2speed;
}

# Additional values that we can add to main metrics array

# monitor-traffic tx/rx bps on all ethernet interfaces
:foreach interface in=[/interface ethernet find] do={
    :local intfName [/interface get $interface name];
    /interface monitor-traffic $intfName once do={
        :set ($metrics->("system.interfaces.".$intfName.".tx-bits-per-second")) (tx-bits-per-second / 1024);
        :set ($metrics->("system.interfaces.".$intfName.".rx-bits-per-second")) (rx-bits-per-second / 1024);
    }
}

# monitor-traffic tx/rx bps on all vlan interfaces
:foreach interface in=[/interface vlan find] do={
    :local intfName [/interface get $interface name];
    /interface monitor-traffic $intfName once do={
        :set ($metrics->("system.interfaces.".$intfName.".tx-bits-per-second")) (tx-bits-per-second / 1024);
        :set ($metrics->("system.interfaces.".$intfName.".rx-bits-per-second")) (rx-bits-per-second / 1024);
    }
}

# monitor-traffic tx/rx bps on all bridge interfaces
:foreach interface in=[/interface bridge find] do={
    :local intfName [/interface get $interface name];
    /interface monitor-traffic $intfName once do={
        :set ($metrics->("system.interfaces.".$intfName.".tx-bits-per-second")) (tx-bits-per-second / 1024);
        :set ($metrics->("system.interfaces.".$intfName.".rx-bits-per-second")) (rx-bits-per-second / 1024);
    }
}

# monitor-traffic tx/rx bps on all bonding interfaces
:foreach interface in=[/interface bonding find] do={
    :local intfName [/interface get $interface name];
    /interface monitor-traffic $intfName once do={
        :set ($metrics->("system.interfaces.".$intfName.".tx-bits-per-second")) (tx-bits-per-second / 1024);
        :set ($metrics->("system.interfaces.".$intfName.".rx-bits-per-second")) (rx-bits-per-second / 1024);
    }
}

# monitor-traffic tx/rx bps on all pppoe-client interfaces
:foreach interface in=[/interface pppoe-client find] do={
    :local intfName [/interface get $interface name];
    /interface monitor-traffic $intfName once do={
        :set ($metrics->("system.interfaces.".$intfName.".tx-bits-per-second")) (tx-bits-per-second / 1024);
        :set ($metrics->("system.interfaces.".$intfName.".rx-bits-per-second")) (rx-bits-per-second / 1024);
    }
}

# Datadog JSON data to parse with Datadog API post-timeseries-points

# Open Series
:set httpdata ($httpdata."{\"series\":[");

:foreach metric,value in=($metrics) do={
    :set httpdata ($httpdata."{\"metric\":\"".$metric."\",\"points\":[[".$datetime.",".$value."]],\"type\":\"".$type."\",\"tags\":\"".$tags."\",\"host\":\"".$identity."\"},");
}

# Remove "," on latest "}" when append last info or you will get a 400 Bad Request
# Payload is not in the expected format: invalid character ']' looking for beginning of value

# set system.uptime metric as closing series
:set $metric "system.uptime";
:set $value [$uptimeseconds];
:set httpdata ($httpdata."{\"metric\":\"".$metric."\",\"points\":[[".$datetime.",".$value."]],\"type\":\"".$type."\",\"tags\":\"".$tags."\",\"host\":\"".$identity."\"}");

# Close Series
:set httpdata ($httpdata."]}");

# Call API via POST
:set ddendpoint ($ddendpoint."/series\?api_key=".$apikey."&application_key=".$applicationkey);
/tool fetch keep-result=no mode=https http-method=post http-header-field="Content-Type:application/json" http-data=$httpdata url=$ddendpoint;

}


File: /LICENSE
MIT License

Copyright (c) 2019 Manuele Trimarchi

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


File: /LoadGlobalFunctions.rsc
{

# Julian Calendar function
:global functionJulianDate do={

:local months [:toarray "jan,feb,mar,apr,may,jun,jul,aug,sep,oct,nov,dec"];
:local jd
:local M [:pick $1 0 3];
:local D [:pick $1 4 6];
:local Y [:pick $1 7 11];

:for x from=0 to=([:len $months] - 1) do={
    :if ([:tostr [:pick $months $x]] = $M) do={:set M ($x + 1) } 
}
:if ( $M = 1 || $M = 2) do={
    :set Y ($Y-1);
    :set M ($M+12);
}

:local A ($Y/100)
:local B ($A/4)
:local C (2-$A+$B)
:local E ((($Y+4716) * 36525)/100)
:local F ((306001*($M+1))/10000)
return ($C+$D+$E+$F-1525)
};

# Timestamp function to get UNIX POSIX timestamp in UTC timezone
:global timestamp do={

:global functionJulianDate $functionJulianDate
:local currenttime [/system clock get time];
:local jdnow [$functionJulianDate [/system clock get date]]
:local days ($jdnow - 2440587)
:local hours [:pick $currenttime 0 2]
:local minutes [:pick $currenttime 3 5]
:local seconds [:pick $currenttime 6 8]

return (($days * 86400) + ($hours * 3600) + ($minutes * 60) + $seconds - [/system clock get gmt-offset]);
}

# Get uptime in seconds
:global uptimeseconds do={

:local UptimeSeconds 0;
:local uptime [/system resource get uptime];
:local weekend 0;
:local dayend 0;
:local weeks 0;
:local days 0;

:if ([:find $uptime "w" -1] > 0) do={
    :set weekend [:find $uptime "w" -1];
    :set weeks [:pick $uptime 0 $weekend];
    :set weekend ($weekend+1);
};

:if ([:find $uptime "d" -1] > 0) do={
    :set dayend [:find $uptime "d" -1];
    :set days [:pick $uptime $weekend $dayend];
};

:local time [:pick $uptime ([:len $uptime]-8) [:len $uptime]]; 

:local hours [:pick $time 0 2];
:local minutes [:pick $time 3 5];
:local seconds [:pick $time 6 8]; 

return ($weeks*86400*7+$days*86400+$hours*3600+$minutes*60+$seconds);
}

}


File: /README.md
# MikrotikJSON4DatadogAPI

This is a simple example to generate and push metrics in JSON format to Datadog API using RouterOS scripting language.

I'm using [Timeseries Points](https://docs.datadoghq.com/api/?lang=bash#post-timeseries-points) `POST` Datadog API call.


With this example you can generate a dashboard like that:

![datadog-public-dashboard-example](https://github.com/mtrimarchi/MikrotikJSON4DatadogAPI/raw/master/datadog-public-dashboard-example.png "Datadog public dashboard example")

So, let's go!

# First step, LoadGlobalFunctions.rsc

At first, we need to add some basic global functions and load them on startup.

You have to go on `System \ Scheduler` and add a new Schedule.

Configure the schedule this way:
- **Schedule name** → `LoadAllFunctions`
- **Start Date** → `Nov/27/2018`
- **Start Time** → `startup`
- **Interval** → `00:00:00`
- **On Event** → _just copy/paste [LoadGlobalFunctions.rsc](https://github.com/mtrimarchi/MikrotikJSON4DatadogAPI/raw/master/LoadGlobalFunctions.rsc) content_

Ok, now if we reboot our router we will get loaded three functions. We can find them on `System \ Scripts \ Environment`.

These loaded scripts are named:
- **functionJulianDate** _Julian Calendar function wich convert RouterOS date call in JD format seconds_
- **timestamp** _Timestamp function to get UNIX POSIX timestamp in UTC timezone_
- **uptimeseconds** _Get uptime in seconds_

# Second step, DatadogMonitoring.rsc

First of all we need to generate an `API Key` and a new `Application Key`. We can do it [here](https://app.datadoghq.com/account/settings#api).

Once created both keys, as already done before, we have to add a new Schedule. This one generate the JSON data and push it to Datadog API using `fetch` command. We need to adapt vars on the script because when we call Datadog API we need to identify ourself with the generated `API key` and `Application key`.

When you copy [DatadogMonitoring.rsc](https://github.com/mtrimarchi/MikrotikJSON4DatadogAPI/raw/master/DatadogMonitoring.rsc) pay attention to the first part of the script identified as "Datadog API Settings".

Adapt all the values:
- **apikey** → _Your API keys are unique to your organization. An API key is required by the Datadog Agent to submit metrics and events to Datadog._
- **applicationkey** → _Application keys, in conjunction with your org's API key, give you full access to Datadog's programmatic API. Application keys are associated with the user account that created them and can be named. The application key is used to log all requests made to the API._
- **ddendpoint** → `"https://app.datadoghq.com/api/v1"` _URL Datadog API endpoint._
- **type** → `"gauge"` _[optional, default=gauge]: Type of your metric either: gauge, rate, or count._
- **tags** → `"source:mikrotik"` _[optional, default=None]: A list of tags associated with the metric._

Now you have to go once again on `System \ Scheduler` and add a new Schedule.

Configure the schedule this way:
- **Schedule name** → `DatadogMonitoring`
- **Start Date** → `Nov/27/2018`
- **Start Time** → `00:00:00`
- **Interval** → `00:00:05`
- **On Event** → _copy/paste the modified content of DatadogMonitoring.rsc_

You can adjust `Interval` seconds value in order to change the frequency timeframe for generation and push of the JSON to Datadog.

# Let's test!

You can see `system.cpu.load` metric using `Metrics Explorer` on Datadog website.

Click here for an example: [https://app.datadoghq.com/metric/explorer?live=true&exp_metric=system.cpu.load](https://app.datadoghq.com/metric/explorer?live=true&exp_metric=system.cpu.load)


