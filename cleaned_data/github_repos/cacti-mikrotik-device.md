# Repository Information
Name: cacti-mikrotik-device

# Directory Structure
Directory structure:
└── github_repos/cacti-mikrotik-device/
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
    │   │       ├── pack-ed05799cf7ba72bdcd394ddca7d8167ae3f20f6a.idx
    │   │       └── pack-ed05799cf7ba72bdcd394ddca7d8167ae3f20f6a.pack
    │   ├── packed-refs
    │   └── refs/
    │       ├── heads/
    │       │   └── master
    │       ├── remotes/
    │       │   └── origin/
    │       │       └── HEAD
    │       └── tags/
    ├── cacti_host_template_mikrotik_device.xml
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
	url = https://github.com/danpalamo/cacti-mikrotik-device.git
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
0000000000000000000000000000000000000000 91f7fa3a0432a0f6153dbda72564957f8470b0c0 vivek-dodia <vivek.dodia@icloud.com> 1738606444 -0500	clone: from https://github.com/danpalamo/cacti-mikrotik-device.git


File: /.git\logs\refs\heads\master
0000000000000000000000000000000000000000 91f7fa3a0432a0f6153dbda72564957f8470b0c0 vivek-dodia <vivek.dodia@icloud.com> 1738606444 -0500	clone: from https://github.com/danpalamo/cacti-mikrotik-device.git


File: /.git\logs\refs\remotes\origin\HEAD
0000000000000000000000000000000000000000 91f7fa3a0432a0f6153dbda72564957f8470b0c0 vivek-dodia <vivek.dodia@icloud.com> 1738606444 -0500	clone: from https://github.com/danpalamo/cacti-mikrotik-device.git


File: /.git\packed-refs
# pack-refs with: peeled fully-peeled sorted 
91f7fa3a0432a0f6153dbda72564957f8470b0c0 refs/remotes/origin/master
91f7fa3a0432a0f6153dbda72564957f8470b0c0 refs/tags/1.0


File: /.git\refs\heads\master
91f7fa3a0432a0f6153dbda72564957f8470b0c0


File: /.git\refs\remotes\origin\HEAD
ref: refs/remotes/origin/master


File: /cacti_host_template_mikrotik_device.xml
<cacti>	
	<hash_0201011a162958ae5818bf54e27aadbdfc9ec3>
		<name>Mikrotik Device</name>
		<graph_templates>hash_0001010d8e82c9620f50637182ebfd27589084|hash_0001018458139b0b9d802f74010e59ef4828b3</graph_templates>
		<data_queries>hash_040101d75e406fdeca4fcef45b8be3a9a63cbc</data_queries>
	</hash_0201011a162958ae5818bf54e27aadbdfc9ec3>
	<hash_0001010d8e82c9620f50637182ebfd27589084>
		<name>Mikrotik - CPU Usage</name>
		<graph>
			<t_title></t_title>
			<title>|host_description| - MTK CPU Usage</title>
			<t_vertical_label></t_vertical_label>
			<vertical_label>percent</vertical_label>
			<t_image_format_id></t_image_format_id>
			<image_format_id>1</image_format_id>
			<t_height></t_height>
			<height>200</height>
			<t_width></t_width>
			<width>700</width>
			<t_base_value></t_base_value>
			<base_value>1000</base_value>
			<t_slope_mode></t_slope_mode>
			<slope_mode>on</slope_mode>
			<t_auto_scale></t_auto_scale>
			<auto_scale>on</auto_scale>
			<t_auto_scale_opts></t_auto_scale_opts>
			<auto_scale_opts>2</auto_scale_opts>
			<t_auto_scale_log></t_auto_scale_log>
			<auto_scale_log></auto_scale_log>
			<t_scale_log_units></t_scale_log_units>
			<scale_log_units></scale_log_units>
			<t_auto_scale_rigid></t_auto_scale_rigid>
			<auto_scale_rigid>on</auto_scale_rigid>
			<t_upper_limit></t_upper_limit>
			<upper_limit>100</upper_limit>
			<t_lower_limit></t_lower_limit>
			<lower_limit>0</lower_limit>
			<t_unit_value></t_unit_value>
			<unit_value></unit_value>
			<t_unit_exponent_value></t_unit_exponent_value>
			<unit_exponent_value></unit_exponent_value>
			<t_unit_length></t_unit_length>
			<unit_length></unit_length>
			<t_no_gridfit></t_no_gridfit>
			<no_gridfit></no_gridfit>
			<t_alt_y_grid></t_alt_y_grid>
			<alt_y_grid></alt_y_grid>
			<t_right_axis></t_right_axis>
			<right_axis></right_axis>
			<t_right_axis_label></t_right_axis_label>
			<right_axis_label></right_axis_label>
			<t_right_axis_format></t_right_axis_format>
			<right_axis_format>0</right_axis_format>
			<t_right_axis_formatter></t_right_axis_formatter>
			<right_axis_formatter>0</right_axis_formatter>
			<t_left_axis_formatter></t_left_axis_formatter>
			<left_axis_formatter>0</left_axis_formatter>
			<t_auto_padding></t_auto_padding>
			<auto_padding>on</auto_padding>
			<t_dynamic_labels></t_dynamic_labels>
			<dynamic_labels></dynamic_labels>
			<t_force_rules_legend></t_force_rules_legend>
			<force_rules_legend></force_rules_legend>
			<t_tab_width></t_tab_width>
			<tab_width>40</tab_width>
			<t_legend_position></t_legend_position>
			<legend_position>0</legend_position>
			<t_legend_direction></t_legend_direction>
			<legend_direction>0</legend_direction>
		</graph>
		<items>
			<hash_100101fa9c36c7ca3b1ef320aeb2a0b4677b0e>
				<graph_type_id>7</graph_type_id>
				<task_item_id>hash_080101a459834b76dcc310b0d96515948427c7</task_item_id>
				<color_id>FF0000</color_id>
				<alpha>FF</alpha>
				<consolidation_function_id>1</consolidation_function_id>
				<cdef_id>0</cdef_id>
				<vdef_id>0</vdef_id>
				<shift></shift>
				<value></value>
				<gprint_id>hash_060101e9c43831e54eca8069317a2ce8c6f751</gprint_id>
				<textalign></textalign>
				<text_format>CPU Usage</text_format>
				<hard_return></hard_return>
				<line_width>0.00</line_width>
				<dashes></dashes>
				<dash_offset>0</dash_offset>
				<sequence>1</sequence>
			</hash_100101fa9c36c7ca3b1ef320aeb2a0b4677b0e>
			<hash_1001013c78a1f994b5d18a1196941f4c0a19c2>
				<graph_type_id>9</graph_type_id>
				<task_item_id>hash_080101a459834b76dcc310b0d96515948427c7</task_item_id>
				<color_id>0</color_id>
				<alpha>FF</alpha>
				<consolidation_function_id>4</consolidation_function_id>
				<cdef_id>0</cdef_id>
				<vdef_id>0</vdef_id>
				<shift></shift>
				<value></value>
				<gprint_id>hash_06010119414480d6897c8731c7dc6c5310653e</gprint_id>
				<textalign></textalign>
				<text_format>Current:</text_format>
				<hard_return></hard_return>
				<line_width>0.00</line_width>
				<dashes></dashes>
				<dash_offset>0</dash_offset>
				<sequence>2</sequence>
			</hash_1001013c78a1f994b5d18a1196941f4c0a19c2>
			<hash_1001019061fa8d753230985161c77663e190c4>
				<graph_type_id>9</graph_type_id>
				<task_item_id>hash_080101a459834b76dcc310b0d96515948427c7</task_item_id>
				<color_id>0</color_id>
				<alpha>FF</alpha>
				<consolidation_function_id>1</consolidation_function_id>
				<cdef_id>0</cdef_id>
				<vdef_id>0</vdef_id>
				<shift></shift>
				<value></value>
				<gprint_id>hash_06010119414480d6897c8731c7dc6c5310653e</gprint_id>
				<textalign></textalign>
				<text_format>Average:</text_format>
				<hard_return></hard_return>
				<line_width>0.00</line_width>
				<dashes></dashes>
				<dash_offset>0</dash_offset>
				<sequence>3</sequence>
			</hash_1001019061fa8d753230985161c77663e190c4>
			<hash_100101725e027340ff19210e454f463d78cf0a>
				<graph_type_id>9</graph_type_id>
				<task_item_id>hash_080101a459834b76dcc310b0d96515948427c7</task_item_id>
				<color_id>0</color_id>
				<alpha>FF</alpha>
				<consolidation_function_id>3</consolidation_function_id>
				<cdef_id>0</cdef_id>
				<vdef_id>0</vdef_id>
				<shift></shift>
				<value></value>
				<gprint_id>hash_06010119414480d6897c8731c7dc6c5310653e</gprint_id>
				<textalign></textalign>
				<text_format>Maximum:</text_format>
				<hard_return>on</hard_return>
				<line_width>0.00</line_width>
				<dashes></dashes>
				<dash_offset>0</dash_offset>
				<sequence>4</sequence>
			</hash_100101725e027340ff19210e454f463d78cf0a>
		</items>
		<inputs>
			<hash_090101dd025237d52f0ed4149a9188f19515ec>
				<name>Data Source [CPULOAD]</name>
				<description></description>
				<column_name>task_item_id</column_name>
				<items>hash_000101fa9c36c7ca3b1ef320aeb2a0b4677b0e|hash_0001013c78a1f994b5d18a1196941f4c0a19c2|hash_0001019061fa8d753230985161c77663e190c4|hash_000101725e027340ff19210e454f463d78cf0a</items>
			</hash_090101dd025237d52f0ed4149a9188f19515ec>
		</inputs>
	</hash_0001010d8e82c9620f50637182ebfd27589084>
	<hash_0001018458139b0b9d802f74010e59ef4828b3>
		<name>Host MIB - Uptime</name>
		<graph>
			<t_title></t_title>
			<title>|host_description| - Uptime</title>
			<t_vertical_label></t_vertical_label>
			<vertical_label>days</vertical_label>
			<t_image_format_id></t_image_format_id>
			<image_format_id>1</image_format_id>
			<t_height></t_height>
			<height>200</height>
			<t_width></t_width>
			<width>700</width>
			<t_base_value></t_base_value>
			<base_value>1000</base_value>
			<t_slope_mode></t_slope_mode>
			<slope_mode>on</slope_mode>
			<t_auto_scale></t_auto_scale>
			<auto_scale>on</auto_scale>
			<t_auto_scale_opts></t_auto_scale_opts>
			<auto_scale_opts>2</auto_scale_opts>
			<t_auto_scale_log></t_auto_scale_log>
			<auto_scale_log></auto_scale_log>
			<t_scale_log_units></t_scale_log_units>
			<scale_log_units></scale_log_units>
			<t_auto_scale_rigid></t_auto_scale_rigid>
			<auto_scale_rigid></auto_scale_rigid>
			<t_upper_limit></t_upper_limit>
			<upper_limit>100</upper_limit>
			<t_lower_limit></t_lower_limit>
			<lower_limit>0</lower_limit>
			<t_unit_value></t_unit_value>
			<unit_value></unit_value>
			<t_unit_exponent_value></t_unit_exponent_value>
			<unit_exponent_value></unit_exponent_value>
			<t_unit_length></t_unit_length>
			<unit_length></unit_length>
			<t_no_gridfit></t_no_gridfit>
			<no_gridfit></no_gridfit>
			<t_alt_y_grid></t_alt_y_grid>
			<alt_y_grid></alt_y_grid>
			<t_right_axis></t_right_axis>
			<right_axis></right_axis>
			<t_right_axis_label></t_right_axis_label>
			<right_axis_label></right_axis_label>
			<t_right_axis_format></t_right_axis_format>
			<right_axis_format>0</right_axis_format>
			<t_right_axis_formatter></t_right_axis_formatter>
			<right_axis_formatter>0</right_axis_formatter>
			<t_left_axis_formatter></t_left_axis_formatter>
			<left_axis_formatter>0</left_axis_formatter>
			<t_auto_padding></t_auto_padding>
			<auto_padding>on</auto_padding>
			<t_dynamic_labels></t_dynamic_labels>
			<dynamic_labels></dynamic_labels>
			<t_force_rules_legend></t_force_rules_legend>
			<force_rules_legend></force_rules_legend>
			<t_tab_width></t_tab_width>
			<tab_width>40</tab_width>
			<t_legend_position></t_legend_position>
			<legend_position>0</legend_position>
			<t_legend_direction></t_legend_direction>
			<legend_direction>0</legend_direction>
		</graph>
		<items>
			<hash_1001012fd612aad151a3f5300730cfef25a317>
				<graph_type_id>7</graph_type_id>
				<task_item_id>hash_080101889a43e0b6feddaa482f0e3198529f4d</task_item_id>
				<color_id>F51D30</color_id>
				<alpha>7F</alpha>
				<consolidation_function_id>1</consolidation_function_id>
				<cdef_id>hash_050101b83f4207a85eb6490bc55411c60672f1</cdef_id>
				<vdef_id>0</vdef_id>
				<shift></shift>
				<value></value>
				<gprint_id>hash_060101e9c43831e54eca8069317a2ce8c6f751</gprint_id>
				<textalign></textalign>
				<text_format>Uptime</text_format>
				<hard_return></hard_return>
				<line_width>0.00</line_width>
				<dashes></dashes>
				<dash_offset>0</dash_offset>
				<sequence>1</sequence>
			</hash_1001012fd612aad151a3f5300730cfef25a317>
			<hash_100101b0d1cfffe8c7aad3fe8258425b5807a2>
				<graph_type_id>9</graph_type_id>
				<task_item_id>hash_080101889a43e0b6feddaa482f0e3198529f4d</task_item_id>
				<color_id>0</color_id>
				<alpha>FF</alpha>
				<consolidation_function_id>4</consolidation_function_id>
				<cdef_id>hash_050101b83f4207a85eb6490bc55411c60672f1</cdef_id>
				<vdef_id>0</vdef_id>
				<shift></shift>
				<value></value>
				<gprint_id>hash_06010119414480d6897c8731c7dc6c5310653e</gprint_id>
				<textalign></textalign>
				<text_format>Current:</text_format>
				<hard_return></hard_return>
				<line_width>0.00</line_width>
				<dashes></dashes>
				<dash_offset>0</dash_offset>
				<sequence>2</sequence>
			</hash_100101b0d1cfffe8c7aad3fe8258425b5807a2>
			<hash_1001011c623b64a0f5a3c6080f05b295e50149>
				<graph_type_id>9</graph_type_id>
				<task_item_id>hash_080101889a43e0b6feddaa482f0e3198529f4d</task_item_id>
				<color_id>0</color_id>
				<alpha>FF</alpha>
				<consolidation_function_id>1</consolidation_function_id>
				<cdef_id>hash_050101b83f4207a85eb6490bc55411c60672f1</cdef_id>
				<vdef_id>0</vdef_id>
				<shift></shift>
				<value></value>
				<gprint_id>hash_06010119414480d6897c8731c7dc6c5310653e</gprint_id>
				<textalign></textalign>
				<text_format>Average:</text_format>
				<hard_return></hard_return>
				<line_width>0.00</line_width>
				<dashes></dashes>
				<dash_offset>0</dash_offset>
				<sequence>3</sequence>
			</hash_1001011c623b64a0f5a3c6080f05b295e50149>
			<hash_10010171c52f3352ac23c770052e7b443e3b70>
				<graph_type_id>9</graph_type_id>
				<task_item_id>hash_080101889a43e0b6feddaa482f0e3198529f4d</task_item_id>
				<color_id>0</color_id>
				<alpha>FF</alpha>
				<consolidation_function_id>3</consolidation_function_id>
				<cdef_id>hash_050101b83f4207a85eb6490bc55411c60672f1</cdef_id>
				<vdef_id>0</vdef_id>
				<shift></shift>
				<value></value>
				<gprint_id>hash_06010119414480d6897c8731c7dc6c5310653e</gprint_id>
				<textalign></textalign>
				<text_format>Maximum:</text_format>
				<hard_return></hard_return>
				<line_width>0.00</line_width>
				<dashes></dashes>
				<dash_offset>0</dash_offset>
				<sequence>4</sequence>
			</hash_10010171c52f3352ac23c770052e7b443e3b70>
			<hash_100101c80ab96e38583769cb24279a610cbe1a>
				<graph_type_id>4</graph_type_id>
				<task_item_id>hash_080101889a43e0b6feddaa482f0e3198529f4d</task_item_id>
				<color_id>F51D30</color_id>
				<alpha>FF</alpha>
				<consolidation_function_id>3</consolidation_function_id>
				<cdef_id>hash_050101b83f4207a85eb6490bc55411c60672f1</cdef_id>
				<vdef_id>0</vdef_id>
				<shift></shift>
				<value></value>
				<gprint_id>hash_060101e9c43831e54eca8069317a2ce8c6f751</gprint_id>
				<textalign></textalign>
				<text_format></text_format>
				<hard_return></hard_return>
				<line_width>1.00</line_width>
				<dashes></dashes>
				<dash_offset>0</dash_offset>
				<sequence>5</sequence>
			</hash_100101c80ab96e38583769cb24279a610cbe1a>
		</items>
		<inputs>
			<hash_090101f01f67f386990379901e0294e1928165>
				<name>Data Source [uptime]</name>
				<description></description>
				<column_name>task_item_id</column_name>
				<items>hash_0001012fd612aad151a3f5300730cfef25a317|hash_000101b0d1cfffe8c7aad3fe8258425b5807a2|hash_0001011c623b64a0f5a3c6080f05b295e50149|hash_00010171c52f3352ac23c770052e7b443e3b70|hash_000101c80ab96e38583769cb24279a610cbe1a</items>
			</hash_090101f01f67f386990379901e0294e1928165>
		</inputs>
	</hash_0001018458139b0b9d802f74010e59ef4828b3>
	<hash_0001015deb0d66c81262843dce5f3861be9966>
		<name>Interface - Traffic (bits/sec)</name>
		<graph>
			<t_title>on</t_title>
			<title>|host_description| - Traffic</title>
			<t_vertical_label></t_vertical_label>
			<vertical_label>bits per second</vertical_label>
			<t_image_format_id></t_image_format_id>
			<image_format_id>1</image_format_id>
			<t_height></t_height>
			<height>200</height>
			<t_width></t_width>
			<width>700</width>
			<t_base_value></t_base_value>
			<base_value>1000</base_value>
			<t_slope_mode></t_slope_mode>
			<slope_mode>on</slope_mode>
			<t_auto_scale></t_auto_scale>
			<auto_scale>on</auto_scale>
			<t_auto_scale_opts></t_auto_scale_opts>
			<auto_scale_opts>2</auto_scale_opts>
			<t_auto_scale_log></t_auto_scale_log>
			<auto_scale_log></auto_scale_log>
			<t_scale_log_units></t_scale_log_units>
			<scale_log_units></scale_log_units>
			<t_auto_scale_rigid></t_auto_scale_rigid>
			<auto_scale_rigid>on</auto_scale_rigid>
			<t_upper_limit></t_upper_limit>
			<upper_limit>100</upper_limit>
			<t_lower_limit></t_lower_limit>
			<lower_limit>0</lower_limit>
			<t_unit_value></t_unit_value>
			<unit_value></unit_value>
			<t_unit_exponent_value></t_unit_exponent_value>
			<unit_exponent_value></unit_exponent_value>
			<t_unit_length></t_unit_length>
			<unit_length></unit_length>
			<t_no_gridfit></t_no_gridfit>
			<no_gridfit></no_gridfit>
			<t_alt_y_grid></t_alt_y_grid>
			<alt_y_grid></alt_y_grid>
			<t_right_axis></t_right_axis>
			<right_axis></right_axis>
			<t_right_axis_label></t_right_axis_label>
			<right_axis_label></right_axis_label>
			<t_right_axis_format></t_right_axis_format>
			<right_axis_format>0</right_axis_format>
			<t_right_axis_formatter></t_right_axis_formatter>
			<right_axis_formatter>0</right_axis_formatter>
			<t_left_axis_formatter></t_left_axis_formatter>
			<left_axis_formatter>0</left_axis_formatter>
			<t_auto_padding></t_auto_padding>
			<auto_padding>on</auto_padding>
			<t_dynamic_labels></t_dynamic_labels>
			<dynamic_labels></dynamic_labels>
			<t_force_rules_legend></t_force_rules_legend>
			<force_rules_legend></force_rules_legend>
			<t_tab_width></t_tab_width>
			<tab_width></tab_width>
			<t_legend_position></t_legend_position>
			<legend_position>0</legend_position>
			<t_legend_direction></t_legend_direction>
			<legend_direction>0</legend_direction>
		</graph>
		<items>
			<hash_10010167b03eadc8e1d948a23326b7c6e225aa>
				<graph_type_id>4</graph_type_id>
				<task_item_id>hash_0801012df25c57022b0c7e7d0be4c035ada1a0</task_item_id>
				<color_id>00CF00</color_id>
				<alpha>FF</alpha>
				<consolidation_function_id>3</consolidation_function_id>
				<cdef_id>hash_05010173f95f8b77b5508157d64047342c421e</cdef_id>
				<vdef_id>0</vdef_id>
				<shift></shift>
				<value></value>
				<gprint_id>hash_060101e9c43831e54eca8069317a2ce8c6f751</gprint_id>
				<textalign></textalign>
				<text_format></text_format>
				<hard_return></hard_return>
				<line_width>0.00</line_width>
				<dashes></dashes>
				<dash_offset>0</dash_offset>
				<sequence>1</sequence>
			</hash_10010167b03eadc8e1d948a23326b7c6e225aa>
			<hash_1001010470b2427dbfadb6b8346e10a71268fa>
				<graph_type_id>7</graph_type_id>
				<task_item_id>hash_0801012df25c57022b0c7e7d0be4c035ada1a0</task_item_id>
				<color_id>00CF00</color_id>
				<alpha>7F</alpha>
				<consolidation_function_id>1</consolidation_function_id>
				<cdef_id>hash_05010173f95f8b77b5508157d64047342c421e</cdef_id>
				<vdef_id>0</vdef_id>
				<shift></shift>
				<value></value>
				<gprint_id>hash_060101e9c43831e54eca8069317a2ce8c6f751</gprint_id>
				<textalign></textalign>
				<text_format>Inbound</text_format>
				<hard_return></hard_return>
				<line_width>0.00</line_width>
				<dashes></dashes>
				<dash_offset>0</dash_offset>
				<sequence>2</sequence>
			</hash_1001010470b2427dbfadb6b8346e10a71268fa>
			<hash_10010184a5fe0db518550266309823f994ce9c>
				<graph_type_id>9</graph_type_id>
				<task_item_id>hash_0801012df25c57022b0c7e7d0be4c035ada1a0</task_item_id>
				<color_id>0</color_id>
				<alpha>FF</alpha>
				<consolidation_function_id>4</consolidation_function_id>
				<cdef_id>hash_05010173f95f8b77b5508157d64047342c421e</cdef_id>
				<vdef_id>0</vdef_id>
				<shift></shift>
				<value></value>
				<gprint_id>hash_060101e9c43831e54eca8069317a2ce8c6f751</gprint_id>
				<textalign></textalign>
				<text_format>Current:</text_format>
				<hard_return></hard_return>
				<line_width>0.00</line_width>
				<dashes></dashes>
				<dash_offset>0</dash_offset>
				<sequence>3</sequence>
			</hash_10010184a5fe0db518550266309823f994ce9c>
			<hash_1001012f222f28084085cd06a1f46e4449c793>
				<graph_type_id>9</graph_type_id>
				<task_item_id>hash_0801012df25c57022b0c7e7d0be4c035ada1a0</task_item_id>
				<color_id>0</color_id>
				<alpha>FF</alpha>
				<consolidation_function_id>1</consolidation_function_id>
				<cdef_id>hash_05010173f95f8b77b5508157d64047342c421e</cdef_id>
				<vdef_id>0</vdef_id>
				<shift></shift>
				<value></value>
				<gprint_id>hash_060101e9c43831e54eca8069317a2ce8c6f751</gprint_id>
				<textalign></textalign>
				<text_format>Average:</text_format>
				<hard_return></hard_return>
				<line_width>0.00</line_width>
				<dashes></dashes>
				<dash_offset>0</dash_offset>
				<sequence>4</sequence>
			</hash_1001012f222f28084085cd06a1f46e4449c793>
			<hash_10010155acbcc33f46ee6d754e8e81d1b54808>
				<graph_type_id>9</graph_type_id>
				<task_item_id>hash_0801012df25c57022b0c7e7d0be4c035ada1a0</task_item_id>
				<color_id>0</color_id>
				<alpha>FF</alpha>
				<consolidation_function_id>3</consolidation_function_id>
				<cdef_id>hash_05010173f95f8b77b5508157d64047342c421e</cdef_id>
				<vdef_id>0</vdef_id>
				<shift></shift>
				<value></value>
				<gprint_id>hash_060101e9c43831e54eca8069317a2ce8c6f751</gprint_id>
				<textalign></textalign>
				<text_format>Maximum:</text_format>
				<hard_return>on</hard_return>
				<line_width>0.00</line_width>
				<dashes></dashes>
				<dash_offset>0</dash_offset>
				<sequence>5</sequence>
			</hash_10010155acbcc33f46ee6d754e8e81d1b54808>
			<hash_100101d71b8ba294f057e0f135cc4c644e6b0d>
				<graph_type_id>4</graph_type_id>
				<task_item_id>hash_080101721c0794526d1ac1c359f27dc56faa49</task_item_id>
				<color_id>002A97</color_id>
				<alpha>FF</alpha>
				<consolidation_function_id>3</consolidation_function_id>
				<cdef_id>hash_05010173f95f8b77b5508157d64047342c421e</cdef_id>
				<vdef_id>0</vdef_id>
				<shift></shift>
				<value></value>
				<gprint_id>hash_060101e9c43831e54eca8069317a2ce8c6f751</gprint_id>
				<textalign></textalign>
				<text_format></text_format>
				<hard_return></hard_return>
				<line_width>0.00</line_width>
				<dashes></dashes>
				<dash_offset>0</dash_offset>
				<sequence>6</sequence>
			</hash_100101d71b8ba294f057e0f135cc4c644e6b0d>
			<hash_100101fdaf2321fc890e355711c2bffc07d036>
				<graph_type_id>7</graph_type_id>
				<task_item_id>hash_080101721c0794526d1ac1c359f27dc56faa49</task_item_id>
				<color_id>002A97</color_id>
				<alpha>7F</alpha>
				<consolidation_function_id>1</consolidation_function_id>
				<cdef_id>hash_05010173f95f8b77b5508157d64047342c421e</cdef_id>
				<vdef_id>0</vdef_id>
				<shift></shift>
				<value></value>
				<gprint_id>hash_060101e9c43831e54eca8069317a2ce8c6f751</gprint_id>
				<textalign></textalign>
				<text_format>Outbound</text_format>
				<hard_return></hard_return>
				<line_width>0.00</line_width>
				<dashes></dashes>
				<dash_offset>0</dash_offset>
				<sequence>7</sequence>
			</hash_100101fdaf2321fc890e355711c2bffc07d036>
			<hash_100101768318f42819217ed81196d2179d3e1b>
				<graph_type_id>9</graph_type_id>
				<task_item_id>hash_080101721c0794526d1ac1c359f27dc56faa49</task_item_id>
				<color_id>0</color_id>
				<alpha>FF</alpha>
				<consolidation_function_id>4</consolidation_function_id>
				<cdef_id>hash_05010173f95f8b77b5508157d64047342c421e</cdef_id>
				<vdef_id>0</vdef_id>
				<shift></shift>
				<value></value>
				<gprint_id>hash_060101e9c43831e54eca8069317a2ce8c6f751</gprint_id>
				<textalign></textalign>
				<text_format>Current:</text_format>
				<hard_return></hard_return>
				<line_width>0.00</line_width>
				<dashes></dashes>
				<dash_offset>0</dash_offset>
				<sequence>8</sequence>
			</hash_100101768318f42819217ed81196d2179d3e1b>
			<hash_100101cb3aa6256dcb3acd50d4517b77a1a5c3>
				<graph_type_id>9</graph_type_id>
				<task_item_id>hash_080101721c0794526d1ac1c359f27dc56faa49</task_item_id>
				<color_id>0</color_id>
				<alpha>FF</alpha>
				<consolidation_function_id>1</consolidation_function_id>
				<cdef_id>hash_05010173f95f8b77b5508157d64047342c421e</cdef_id>
				<vdef_id>0</vdef_id>
				<shift></shift>
				<value></value>
				<gprint_id>hash_060101e9c43831e54eca8069317a2ce8c6f751</gprint_id>
				<textalign></textalign>
				<text_format>Average:</text_format>
				<hard_return></hard_return>
				<line_width>0.00</line_width>
				<dashes></dashes>
				<dash_offset>0</dash_offset>
				<sequence>9</sequence>
			</hash_100101cb3aa6256dcb3acd50d4517b77a1a5c3>
			<hash_100101671e989be7cbf12c623b4e79d91c7bed>
				<graph_type_id>9</graph_type_id>
				<task_item_id>hash_080101721c0794526d1ac1c359f27dc56faa49</task_item_id>
				<color_id>0</color_id>
				<alpha>FF</alpha>
				<consolidation_function_id>3</consolidation_function_id>
				<cdef_id>hash_05010173f95f8b77b5508157d64047342c421e</cdef_id>
				<vdef_id>0</vdef_id>
				<shift></shift>
				<value></value>
				<gprint_id>hash_060101e9c43831e54eca8069317a2ce8c6f751</gprint_id>
				<textalign></textalign>
				<text_format>Maximum:</text_format>
				<hard_return>on</hard_return>
				<line_width>0.00</line_width>
				<dashes></dashes>
				<dash_offset>0</dash_offset>
				<sequence>10</sequence>
			</hash_100101671e989be7cbf12c623b4e79d91c7bed>
		</items>
		<inputs>
			<hash_090101e9d4191277fdfd7d54171f153da57fb0>
				<name>Inbound Data Source</name>
				<description></description>
				<column_name>task_item_id</column_name>
				<items>hash_00010167b03eadc8e1d948a23326b7c6e225aa|hash_0001010470b2427dbfadb6b8346e10a71268fa|hash_00010184a5fe0db518550266309823f994ce9c|hash_0001012f222f28084085cd06a1f46e4449c793|hash_00010155acbcc33f46ee6d754e8e81d1b54808</items>
			</hash_090101e9d4191277fdfd7d54171f153da57fb0>
			<hash_0901017b361722a11a03238ee8ab7ce44a1037>
				<name>Outbound Data Source</name>
				<description></description>
				<column_name>task_item_id</column_name>
				<items>hash_000101d71b8ba294f057e0f135cc4c644e6b0d|hash_000101fdaf2321fc890e355711c2bffc07d036|hash_000101768318f42819217ed81196d2179d3e1b|hash_000101cb3aa6256dcb3acd50d4517b77a1a5c3|hash_000101671e989be7cbf12c623b4e79d91c7bed</items>
			</hash_0901017b361722a11a03238ee8ab7ce44a1037>
		</inputs>
	</hash_0001015deb0d66c81262843dce5f3861be9966>
	<hash_00010106621cd4a9289417cadcb8f9b5cfba80>
		<name>Interface - Errors/Discards</name>
		<graph>
			<t_title>on</t_title>
			<title>|host_description| - Errors/Discards</title>
			<t_vertical_label></t_vertical_label>
			<vertical_label>errors/sec</vertical_label>
			<t_image_format_id></t_image_format_id>
			<image_format_id>1</image_format_id>
			<t_height></t_height>
			<height>200</height>
			<t_width></t_width>
			<width>700</width>
			<t_base_value></t_base_value>
			<base_value>1000</base_value>
			<t_slope_mode></t_slope_mode>
			<slope_mode>on</slope_mode>
			<t_auto_scale></t_auto_scale>
			<auto_scale>on</auto_scale>
			<t_auto_scale_opts></t_auto_scale_opts>
			<auto_scale_opts>2</auto_scale_opts>
			<t_auto_scale_log></t_auto_scale_log>
			<auto_scale_log></auto_scale_log>
			<t_scale_log_units></t_scale_log_units>
			<scale_log_units></scale_log_units>
			<t_auto_scale_rigid></t_auto_scale_rigid>
			<auto_scale_rigid>on</auto_scale_rigid>
			<t_upper_limit></t_upper_limit>
			<upper_limit>100</upper_limit>
			<t_lower_limit></t_lower_limit>
			<lower_limit>0</lower_limit>
			<t_unit_value></t_unit_value>
			<unit_value></unit_value>
			<t_unit_exponent_value></t_unit_exponent_value>
			<unit_exponent_value></unit_exponent_value>
			<t_unit_length></t_unit_length>
			<unit_length></unit_length>
			<t_no_gridfit></t_no_gridfit>
			<no_gridfit></no_gridfit>
			<t_alt_y_grid></t_alt_y_grid>
			<alt_y_grid></alt_y_grid>
			<t_right_axis></t_right_axis>
			<right_axis></right_axis>
			<t_right_axis_label></t_right_axis_label>
			<right_axis_label></right_axis_label>
			<t_right_axis_format></t_right_axis_format>
			<right_axis_format>0</right_axis_format>
			<t_right_axis_formatter></t_right_axis_formatter>
			<right_axis_formatter></right_axis_formatter>
			<t_left_axis_formatter></t_left_axis_formatter>
			<left_axis_formatter></left_axis_formatter>
			<t_auto_padding></t_auto_padding>
			<auto_padding>on</auto_padding>
			<t_dynamic_labels></t_dynamic_labels>
			<dynamic_labels></dynamic_labels>
			<t_force_rules_legend></t_force_rules_legend>
			<force_rules_legend></force_rules_legend>
			<t_tab_width></t_tab_width>
			<tab_width></tab_width>
			<t_legend_position></t_legend_position>
			<legend_position></legend_position>
			<t_legend_direction></t_legend_direction>
			<legend_direction></legend_direction>
		</graph>
		<items>
			<hash_1001017e04a041721df1f8828381a9ea2f2154>
				<graph_type_id>4</graph_type_id>
				<task_item_id>hash_0801014e2a72240955380dc8ffacfcc8c09874</task_item_id>
				<color_id>FFAB00</color_id>
				<alpha>FF</alpha>
				<consolidation_function_id>1</consolidation_function_id>
				<cdef_id>0</cdef_id>
				<vdef_id>0</vdef_id>
				<shift></shift>
				<value></value>
				<gprint_id>hash_060101e9c43831e54eca8069317a2ce8c6f751</gprint_id>
				<textalign></textalign>
				<text_format>Discards In</text_format>
				<hard_return></hard_return>
				<line_width>0.00</line_width>
				<dashes></dashes>
				<dash_offset>0</dash_offset>
				<sequence>1</sequence>
			</hash_1001017e04a041721df1f8828381a9ea2f2154>
			<hash_100101afc8bca6b1b3030a6d71818272336c6c>
				<graph_type_id>9</graph_type_id>
				<task_item_id>hash_0801014e2a72240955380dc8ffacfcc8c09874</task_item_id>
				<color_id>0</color_id>
				<alpha>FF</alpha>
				<consolidation_function_id>4</consolidation_function_id>
				<cdef_id>0</cdef_id>
				<vdef_id>0</vdef_id>
				<shift></shift>
				<value></value>
				<gprint_id>hash_060101e9c43831e54eca8069317a2ce8c6f751</gprint_id>
				<textalign></textalign>
				<text_format>Current:</text_format>
				<hard_return></hard_return>
				<line_width>0.00</line_width>
				<dashes></dashes>
				<dash_offset>0</dash_offset>
				<sequence>2</sequence>
			</hash_100101afc8bca6b1b3030a6d71818272336c6c>
			<hash_1001016ac169785f5aeaf1cc5cdfd38dfcfb6c>
				<graph_type_id>9</graph_type_id>
				<task_item_id>hash_0801014e2a72240955380dc8ffacfcc8c09874</task_item_id>
				<color_id>0</color_id>
				<alpha>FF</alpha>
				<consolidation_function_id>1</consolidation_function_id>
				<cdef_id>0</cdef_id>
				<vdef_id>0</vdef_id>
				<shift></shift>
				<value></value>
				<gprint_id>hash_060101e9c43831e54eca8069317a2ce8c6f751</gprint_id>
				<textalign></textalign>
				<text_format>Average:</text_format>
				<hard_return></hard_return>
				<line_width>0.00</line_width>
				<dashes></dashes>
				<dash_offset>0</dash_offset>
				<sequence>3</sequence>
			</hash_1001016ac169785f5aeaf1cc5cdfd38dfcfb6c>
			<hash_100101178c0a0ce001d36a663ff6f213c07505>
				<graph_type_id>9</graph_type_id>
				<task_item_id>hash_0801014e2a72240955380dc8ffacfcc8c09874</task_item_id>
				<color_id>0</color_id>
				<alpha>FF</alpha>
				<consolidation_function_id>3</consolidation_function_id>
				<cdef_id>0</cdef_id>
				<vdef_id>0</vdef_id>
				<shift></shift>
				<value></value>
				<gprint_id>hash_060101e9c43831e54eca8069317a2ce8c6f751</gprint_id>
				<textalign></textalign>
				<text_format>Maximum:</text_format>
				<hard_return>on</hard_return>
				<line_width>0.00</line_width>
				<dashes></dashes>
				<dash_offset>0</dash_offset>
				<sequence>4</sequence>
			</hash_100101178c0a0ce001d36a663ff6f213c07505>
			<hash_1001018e3268c0abde7550616bff719f10ee2f>
				<graph_type_id>4</graph_type_id>
				<task_item_id>hash_080101c802e2fd77f5b0a4c4298951bf65957c</task_item_id>
				<color_id>F51D30</color_id>
				<alpha>FF</alpha>
				<consolidation_function_id>1</consolidation_function_id>
				<cdef_id>0</cdef_id>
				<vdef_id>0</vdef_id>
				<shift></shift>
				<value></value>
				<gprint_id>hash_060101e9c43831e54eca8069317a2ce8c6f751</gprint_id>
				<textalign></textalign>
				<text_format>Errors In</text_format>
				<hard_return></hard_return>
				<line_width>0.00</line_width>
				<dashes></dashes>
				<dash_offset>0</dash_offset>
				<sequence>5</sequence>
			</hash_1001018e3268c0abde7550616bff719f10ee2f>
			<hash_10010118891392b149de63b62c4258a68d75f8>
				<graph_type_id>9</graph_type_id>
				<task_item_id>hash_080101c802e2fd77f5b0a4c4298951bf65957c</task_item_id>
				<color_id>0</color_id>
				<alpha>FF</alpha>
				<consolidation_function_id>4</consolidation_function_id>
				<cdef_id>0</cdef_id>
				<vdef_id>0</vdef_id>
				<shift></shift>
				<value></value>
				<gprint_id>hash_060101e9c43831e54eca8069317a2ce8c6f751</gprint_id>
				<textalign></textalign>
				<text_format>Current:</text_format>
				<hard_return></hard_return>
				<line_width>0.00</line_width>
				<dashes></dashes>
				<dash_offset>0</dash_offset>
				<sequence>6</sequence>
			</hash_10010118891392b149de63b62c4258a68d75f8>
			<hash_100101dfc9d23de0182c9967ae3dabdfa55a16>
				<graph_type_id>9</graph_type_id>
				<task_item_id>hash_080101c802e2fd77f5b0a4c4298951bf65957c</task_item_id>
				<color_id>0</color_id>
				<alpha>FF</alpha>
				<consolidation_function_id>1</consolidation_function_id>
				<cdef_id>0</cdef_id>
				<vdef_id>0</vdef_id>
				<shift></shift>
				<value></value>
				<gprint_id>hash_060101e9c43831e54eca8069317a2ce8c6f751</gprint_id>
				<textalign></textalign>
				<text_format>Average:</text_format>
				<hard_return></hard_return>
				<line_width>0.00</line_width>
				<dashes></dashes>
				<dash_offset>0</dash_offset>
				<sequence>7</sequence>
			</hash_100101dfc9d23de0182c9967ae3dabdfa55a16>
			<hash_100101c47ba64e2e5ea8bf84aceec644513176>
				<graph_type_id>9</graph_type_id>
				<task_item_id>hash_080101c802e2fd77f5b0a4c4298951bf65957c</task_item_id>
				<color_id>0</color_id>
				<alpha>FF</alpha>
				<consolidation_function_id>3</consolidation_function_id>
				<cdef_id>0</cdef_id>
				<vdef_id>0</vdef_id>
				<shift></shift>
				<value></value>
				<gprint_id>hash_060101e9c43831e54eca8069317a2ce8c6f751</gprint_id>
				<textalign></textalign>
				<text_format>Maximum:</text_format>
				<hard_return>on</hard_return>
				<line_width>0.00</line_width>
				<dashes></dashes>
				<dash_offset>0</dash_offset>
				<sequence>8</sequence>
			</hash_100101c47ba64e2e5ea8bf84aceec644513176>
			<hash_100101617d10dff9bbc3edd9d733d9c254da76>
				<graph_type_id>4</graph_type_id>
				<task_item_id>hash_08010113ebb33f9cbccfcba828db1075a8167c</task_item_id>
				<color_id>C4FD3D</color_id>
				<alpha>FF</alpha>
				<consolidation_function_id>1</consolidation_function_id>
				<cdef_id>0</cdef_id>
				<vdef_id>0</vdef_id>
				<shift></shift>
				<value></value>
				<gprint_id>hash_060101e9c43831e54eca8069317a2ce8c6f751</gprint_id>
				<textalign></textalign>
				<text_format>Discards Out</text_format>
				<hard_return></hard_return>
				<line_width>0.00</line_width>
				<dashes></dashes>
				<dash_offset>0</dash_offset>
				<sequence>9</sequence>
			</hash_100101617d10dff9bbc3edd9d733d9c254da76>
			<hash_1001019269a66502c34d00ac3c8b1fcc329ac6>
				<graph_type_id>9</graph_type_id>
				<task_item_id>hash_08010113ebb33f9cbccfcba828db1075a8167c</task_item_id>
				<color_id>0</color_id>
				<alpha>FF</alpha>
				<consolidation_function_id>4</consolidation_function_id>
				<cdef_id>0</cdef_id>
				<vdef_id>0</vdef_id>
				<shift></shift>
				<value></value>
				<gprint_id>hash_060101e9c43831e54eca8069317a2ce8c6f751</gprint_id>
				<textalign></textalign>
				<text_format>Current:</text_format>
				<hard_return></hard_return>
				<line_width>0.00</line_width>
				<dashes></dashes>
				<dash_offset>0</dash_offset>
				<sequence>10</sequence>
			</hash_1001019269a66502c34d00ac3c8b1fcc329ac6>
			<hash_100101d45deed7e1ad8350f3b46b537ae0a933>
				<graph_type_id>9</graph_type_id>
				<task_item_id>hash_08010113ebb33f9cbccfcba828db1075a8167c</task_item_id>
				<color_id>0</color_id>
				<alpha>FF</alpha>
				<consolidation_function_id>1</consolidation_function_id>
				<cdef_id>0</cdef_id>
				<vdef_id>0</vdef_id>
				<shift></shift>
				<value></value>
				<gprint_id>hash_060101e9c43831e54eca8069317a2ce8c6f751</gprint_id>
				<textalign></textalign>
				<text_format>Average:</text_format>
				<hard_return></hard_return>
				<line_width>0.00</line_width>
				<dashes></dashes>
				<dash_offset>0</dash_offset>
				<sequence>11</sequence>
			</hash_100101d45deed7e1ad8350f3b46b537ae0a933>
			<hash_1001012f64cf47dc156e8c800ae03c3b893e3c>
				<graph_type_id>9</graph_type_id>
				<task_item_id>hash_08010113ebb33f9cbccfcba828db1075a8167c</task_item_id>
				<color_id>0</color_id>
				<alpha>FF</alpha>
				<consolidation_function_id>3</consolidation_function_id>
				<cdef_id>0</cdef_id>
				<vdef_id>0</vdef_id>
				<shift></shift>
				<value></value>
				<gprint_id>hash_060101e9c43831e54eca8069317a2ce8c6f751</gprint_id>
				<textalign></textalign>
				<text_format>Maximum:</text_format>
				<hard_return>on</hard_return>
				<line_width>0.00</line_width>
				<dashes></dashes>
				<dash_offset>0</dash_offset>
				<sequence>12</sequence>
			</hash_1001012f64cf47dc156e8c800ae03c3b893e3c>
			<hash_10010157434bef8cb21283c1a73f055b0ada19>
				<graph_type_id>4</graph_type_id>
				<task_item_id>hash_08010131399c3725bee7e09ec04049e3d5cd17</task_item_id>
				<color_id>00694A</color_id>
				<alpha>FF</alpha>
				<consolidation_function_id>1</consolidation_function_id>
				<cdef_id>0</cdef_id>
				<vdef_id>0</vdef_id>
				<shift></shift>
				<value></value>
				<gprint_id>hash_060101e9c43831e54eca8069317a2ce8c6f751</gprint_id>
				<textalign></textalign>
				<text_format>Errors Out</text_format>
				<hard_return></hard_return>
				<line_width>0.00</line_width>
				<dashes></dashes>
				<dash_offset>0</dash_offset>
				<sequence>13</sequence>
			</hash_10010157434bef8cb21283c1a73f055b0ada19>
			<hash_100101660a1b9365ccbba356fd142faaec9f04>
				<graph_type_id>9</graph_type_id>
				<task_item_id>hash_08010131399c3725bee7e09ec04049e3d5cd17</task_item_id>
				<color_id>0</color_id>
				<alpha>FF</alpha>
				<consolidation_function_id>4</consolidation_function_id>
				<cdef_id>0</cdef_id>
				<vdef_id>0</vdef_id>
				<shift></shift>
				<value></value>
				<gprint_id>hash_060101e9c43831e54eca8069317a2ce8c6f751</gprint_id>
				<textalign></textalign>
				<text_format>Current:</text_format>
				<hard_return></hard_return>
				<line_width>0.00</line_width>
				<dashes></dashes>
				<dash_offset>0</dash_offset>
				<sequence>14</sequence>
			</hash_100101660a1b9365ccbba356fd142faaec9f04>
			<hash_10010128c5297bdaedcca29acf245ef4bbed9e>
				<graph_type_id>9</graph_type_id>
				<task_item_id>hash_08010131399c3725bee7e09ec04049e3d5cd17</task_item_id>
				<color_id>0</color_id>
				<alpha>FF</alpha>
				<consolidation_function_id>1</consolidation_function_id>
				<cdef_id>0</cdef_id>
				<vdef_id>0</vdef_id>
				<shift></shift>
				<value></value>
				<gprint_id>hash_060101e9c43831e54eca8069317a2ce8c6f751</gprint_id>
				<textalign></textalign>
				<text_format>Average:</text_format>
				<hard_return></hard_return>
				<line_width>0.00</line_width>
				<dashes></dashes>
				<dash_offset>0</dash_offset>
				<sequence>15</sequence>
			</hash_10010128c5297bdaedcca29acf245ef4bbed9e>
			<hash_10010199098604fd0c78fd7dabac8f40f1fb29>
				<graph_type_id>9</graph_type_id>
				<task_item_id>hash_08010131399c3725bee7e09ec04049e3d5cd17</task_item_id>
				<color_id>0</color_id>
				<alpha>FF</alpha>
				<consolidation_function_id>3</consolidation_function_id>
				<cdef_id>0</cdef_id>
				<vdef_id>0</vdef_id>
				<shift></shift>
				<value></value>
				<gprint_id>hash_060101e9c43831e54eca8069317a2ce8c6f751</gprint_id>
				<textalign></textalign>
				<text_format>Maximum:</text_format>
				<hard_return>on</hard_return>
				<line_width>0.00</line_width>
				<dashes></dashes>
				<dash_offset>0</dash_offset>
				<sequence>16</sequence>
			</hash_10010199098604fd0c78fd7dabac8f40f1fb29>
		</items>
		<inputs>
			<hash_090101fa83cd3a3b4271b644cb6459ea8c35dc>
				<name>Discards In Data Source</name>
				<description></description>
				<column_name>task_item_id</column_name>
				<items>hash_0001017e04a041721df1f8828381a9ea2f2154|hash_000101afc8bca6b1b3030a6d71818272336c6c|hash_0001016ac169785f5aeaf1cc5cdfd38dfcfb6c|hash_000101178c0a0ce001d36a663ff6f213c07505</items>
			</hash_090101fa83cd3a3b4271b644cb6459ea8c35dc>
			<hash_0901017946e8ee1e38a65462b85e31a15e35e5>
				<name>Errors In Data Source</name>
				<description></description>
				<column_name>task_item_id</column_name>
				<items>hash_0001018e3268c0abde7550616bff719f10ee2f|hash_00010118891392b149de63b62c4258a68d75f8|hash_000101dfc9d23de0182c9967ae3dabdfa55a16|hash_000101c47ba64e2e5ea8bf84aceec644513176</items>
			</hash_0901017946e8ee1e38a65462b85e31a15e35e5>
			<hash_090101e5acdd5368137c408d56ecf55b0e077c>
				<name>Discards Out Data Source</name>
				<description></description>
				<column_name>task_item_id</column_name>
				<items>hash_000101617d10dff9bbc3edd9d733d9c254da76|hash_0001019269a66502c34d00ac3c8b1fcc329ac6|hash_000101d45deed7e1ad8350f3b46b537ae0a933|hash_0001012f64cf47dc156e8c800ae03c3b893e3c</items>
			</hash_090101e5acdd5368137c408d56ecf55b0e077c>
			<hash_090101a028e586e5fae667127c655fe0ac67f0>
				<name>Errors Out Data Source</name>
				<description></description>
				<column_name>task_item_id</column_name>
				<items>hash_00010157434bef8cb21283c1a73f055b0ada19|hash_000101660a1b9365ccbba356fd142faaec9f04|hash_00010128c5297bdaedcca29acf245ef4bbed9e|hash_00010199098604fd0c78fd7dabac8f40f1fb29</items>
			</hash_090101a028e586e5fae667127c655fe0ac67f0>
		</inputs>
	</hash_00010106621cd4a9289417cadcb8f9b5cfba80>
	<hash_000101e0d1625a1f4776a5294583659d5cee15>
		<name>Interface - Unicast Packets</name>
		<graph>
			<t_title>on</t_title>
			<title>|host_description| - Unicast Packets</title>
			<t_vertical_label></t_vertical_label>
			<vertical_label>packets/sec</vertical_label>
			<t_image_format_id></t_image_format_id>
			<image_format_id>1</image_format_id>
			<t_height></t_height>
			<height>200</height>
			<t_width></t_width>
			<width>700</width>
			<t_base_value></t_base_value>
			<base_value>1000</base_value>
			<t_slope_mode></t_slope_mode>
			<slope_mode>on</slope_mode>
			<t_auto_scale></t_auto_scale>
			<auto_scale>on</auto_scale>
			<t_auto_scale_opts></t_auto_scale_opts>
			<auto_scale_opts>2</auto_scale_opts>
			<t_auto_scale_log></t_auto_scale_log>
			<auto_scale_log></auto_scale_log>
			<t_scale_log_units></t_scale_log_units>
			<scale_log_units></scale_log_units>
			<t_auto_scale_rigid></t_auto_scale_rigid>
			<auto_scale_rigid>on</auto_scale_rigid>
			<t_upper_limit></t_upper_limit>
			<upper_limit>100</upper_limit>
			<t_lower_limit></t_lower_limit>
			<lower_limit>0</lower_limit>
			<t_unit_value></t_unit_value>
			<unit_value></unit_value>
			<t_unit_exponent_value></t_unit_exponent_value>
			<unit_exponent_value></unit_exponent_value>
			<t_unit_length></t_unit_length>
			<unit_length></unit_length>
			<t_no_gridfit></t_no_gridfit>
			<no_gridfit></no_gridfit>
			<t_alt_y_grid></t_alt_y_grid>
			<alt_y_grid></alt_y_grid>
			<t_right_axis></t_right_axis>
			<right_axis></right_axis>
			<t_right_axis_label></t_right_axis_label>
			<right_axis_label></right_axis_label>
			<t_right_axis_format></t_right_axis_format>
			<right_axis_format>0</right_axis_format>
			<t_right_axis_formatter></t_right_axis_formatter>
			<right_axis_formatter></right_axis_formatter>
			<t_left_axis_formatter></t_left_axis_formatter>
			<left_axis_formatter></left_axis_formatter>
			<t_auto_padding></t_auto_padding>
			<auto_padding>on</auto_padding>
			<t_dynamic_labels></t_dynamic_labels>
			<dynamic_labels></dynamic_labels>
			<t_force_rules_legend></t_force_rules_legend>
			<force_rules_legend></force_rules_legend>
			<t_tab_width></t_tab_width>
			<tab_width></tab_width>
			<t_legend_position></t_legend_position>
			<legend_position></legend_position>
			<t_legend_direction></t_legend_direction>
			<legend_direction></legend_direction>
		</graph>
		<items>
			<hash_100101d4e5f253f01c3ea77182c5a46418fc44>
				<graph_type_id>7</graph_type_id>
				<task_item_id>hash_080101636672962b5bb2f31d86985e2ab4bdfe</task_item_id>
				<color_id>FFF200</color_id>
				<alpha>7F</alpha>
				<consolidation_function_id>1</consolidation_function_id>
				<cdef_id>0</cdef_id>
				<vdef_id>0</vdef_id>
				<shift></shift>
				<value></value>
				<gprint_id>hash_060101e9c43831e54eca8069317a2ce8c6f751</gprint_id>
				<textalign></textalign>
				<text_format>Unicast Packets In</text_format>
				<hard_return></hard_return>
				<line_width>0.00</line_width>
				<dashes></dashes>
				<dash_offset>0</dash_offset>
				<sequence>1</sequence>
			</hash_100101d4e5f253f01c3ea77182c5a46418fc44>
			<hash_100101526a96add143da021c5f00d8764a6c12>
				<graph_type_id>9</graph_type_id>
				<task_item_id>hash_080101636672962b5bb2f31d86985e2ab4bdfe</task_item_id>
				<color_id>0</color_id>
				<alpha>FF</alpha>
				<consolidation_function_id>4</consolidation_function_id>
				<cdef_id>0</cdef_id>
				<vdef_id>0</vdef_id>
				<shift></shift>
				<value></value>
				<gprint_id>hash_060101e9c43831e54eca8069317a2ce8c6f751</gprint_id>
				<textalign></textalign>
				<text_format>Current:</text_format>
				<hard_return></hard_return>
				<line_width>0.00</line_width>
				<dashes></dashes>
				<dash_offset>0</dash_offset>
				<sequence>2</sequence>
			</hash_100101526a96add143da021c5f00d8764a6c12>
			<hash_10010181eeb46f451212f00fd7caee42a81c0b>
				<graph_type_id>9</graph_type_id>
				<task_item_id>hash_080101636672962b5bb2f31d86985e2ab4bdfe</task_item_id>
				<color_id>0</color_id>
				<alpha>FF</alpha>
				<consolidation_function_id>1</consolidation_function_id>
				<cdef_id>0</cdef_id>
				<vdef_id>0</vdef_id>
				<shift></shift>
				<value></value>
				<gprint_id>hash_060101e9c43831e54eca8069317a2ce8c6f751</gprint_id>
				<textalign></textalign>
				<text_format>Average:</text_format>
				<hard_return></hard_return>
				<line_width>0.00</line_width>
				<dashes></dashes>
				<dash_offset>0</dash_offset>
				<sequence>3</sequence>
			</hash_10010181eeb46f451212f00fd7caee42a81c0b>
			<hash_100101089e4d1c3faeb00fd5dcc9622b06d656>
				<graph_type_id>9</graph_type_id>
				<task_item_id>hash_080101636672962b5bb2f31d86985e2ab4bdfe</task_item_id>
				<color_id>0</color_id>
				<alpha>FF</alpha>
				<consolidation_function_id>3</consolidation_function_id>
				<cdef_id>0</cdef_id>
				<vdef_id>0</vdef_id>
				<shift></shift>
				<value></value>
				<gprint_id>hash_060101e9c43831e54eca8069317a2ce8c6f751</gprint_id>
				<textalign></textalign>
				<text_format>Maximum:</text_format>
				<hard_return>on</hard_return>
				<line_width>0.00</line_width>
				<dashes></dashes>
				<dash_offset>0</dash_offset>
				<sequence>4</sequence>
			</hash_100101089e4d1c3faeb00fd5dcc9622b06d656>
			<hash_1001019d052e7d632c479737fbfaced0821f79>
				<graph_type_id>7</graph_type_id>
				<task_item_id>hash_08010118ce92c125a236a190ee9dd948f56268</task_item_id>
				<color_id>00234B</color_id>
				<alpha>7F</alpha>
				<consolidation_function_id>1</consolidation_function_id>
				<cdef_id>0</cdef_id>
				<vdef_id>0</vdef_id>
				<shift></shift>
				<value></value>
				<gprint_id>hash_060101e9c43831e54eca8069317a2ce8c6f751</gprint_id>
				<textalign></textalign>
				<text_format>Unicast Packets Out</text_format>
				<hard_return></hard_return>
				<line_width>0.00</line_width>
				<dashes></dashes>
				<dash_offset>0</dash_offset>
				<sequence>5</sequence>
			</hash_1001019d052e7d632c479737fbfaced0821f79>
			<hash_1001019b9fa6268571b6a04fa4411d8e08c730>
				<graph_type_id>9</graph_type_id>
				<task_item_id>hash_08010118ce92c125a236a190ee9dd948f56268</task_item_id>
				<color_id>0</color_id>
				<alpha>FF</alpha>
				<consolidation_function_id>4</consolidation_function_id>
				<cdef_id>0</cdef_id>
				<vdef_id>0</vdef_id>
				<shift></shift>
				<value></value>
				<gprint_id>hash_060101e9c43831e54eca8069317a2ce8c6f751</gprint_id>
				<textalign></textalign>
				<text_format>Current:</text_format>
				<hard_return></hard_return>
				<line_width>0.00</line_width>
				<dashes></dashes>
				<dash_offset>0</dash_offset>
				<sequence>6</sequence>
			</hash_1001019b9fa6268571b6a04fa4411d8e08c730>
			<hash_1001018e8f2fbeb624029cbda1d2a6ddd991ba>
				<graph_type_id>9</graph_type_id>
				<task_item_id>hash_08010118ce92c125a236a190ee9dd948f56268</task_item_id>
				<color_id>0</color_id>
				<alpha>FF</alpha>
				<consolidation_function_id>1</consolidation_function_id>
				<cdef_id>0</cdef_id>
				<vdef_id>0</vdef_id>
				<shift></shift>
				<value></value>
				<gprint_id>hash_060101e9c43831e54eca8069317a2ce8c6f751</gprint_id>
				<textalign></textalign>
				<text_format>Average:</text_format>
				<hard_return></hard_return>
				<line_width>0.00</line_width>
				<dashes></dashes>
				<dash_offset>0</dash_offset>
				<sequence>7</sequence>
			</hash_1001018e8f2fbeb624029cbda1d2a6ddd991ba>
			<hash_100101c76495beb1ed01f0799838eb8a893124>
				<graph_type_id>9</graph_type_id>
				<task_item_id>hash_08010118ce92c125a236a190ee9dd948f56268</task_item_id>
				<color_id>0</color_id>
				<alpha>FF</alpha>
				<consolidation_function_id>3</consolidation_function_id>
				<cdef_id>0</cdef_id>
				<vdef_id>0</vdef_id>
				<shift></shift>
				<value></value>
				<gprint_id>hash_060101e9c43831e54eca8069317a2ce8c6f751</gprint_id>
				<textalign></textalign>
				<text_format>Maximum:</text_format>
				<hard_return>on</hard_return>
				<line_width>0.00</line_width>
				<dashes></dashes>
				<dash_offset>0</dash_offset>
				<sequence>8</sequence>
			</hash_100101c76495beb1ed01f0799838eb8a893124>
			<hash_100101042d90f1a390c15509ae208bd97aa885>
				<graph_type_id>4</graph_type_id>
				<task_item_id>hash_080101636672962b5bb2f31d86985e2ab4bdfe</task_item_id>
				<color_id>FFF200</color_id>
				<alpha>FF</alpha>
				<consolidation_function_id>3</consolidation_function_id>
				<cdef_id>0</cdef_id>
				<vdef_id>0</vdef_id>
				<shift></shift>
				<value></value>
				<gprint_id>hash_060101e9c43831e54eca8069317a2ce8c6f751</gprint_id>
				<textalign></textalign>
				<text_format></text_format>
				<hard_return></hard_return>
				<line_width>1.00</line_width>
				<dashes></dashes>
				<dash_offset>0</dash_offset>
				<sequence>9</sequence>
			</hash_100101042d90f1a390c15509ae208bd97aa885>
			<hash_1001013641f6b8e83ea26e73d41ceccf38b131>
				<graph_type_id>4</graph_type_id>
				<task_item_id>hash_08010118ce92c125a236a190ee9dd948f56268</task_item_id>
				<color_id>00234B</color_id>
				<alpha>FF</alpha>
				<consolidation_function_id>3</consolidation_function_id>
				<cdef_id>0</cdef_id>
				<vdef_id>0</vdef_id>
				<shift></shift>
				<value></value>
				<gprint_id>hash_060101e9c43831e54eca8069317a2ce8c6f751</gprint_id>
				<textalign></textalign>
				<text_format></text_format>
				<hard_return></hard_return>
				<line_width>1.00</line_width>
				<dashes></dashes>
				<dash_offset>0</dash_offset>
				<sequence>10</sequence>
			</hash_1001013641f6b8e83ea26e73d41ceccf38b131>
		</items>
		<inputs>
			<hash_09010100ae916640272f5aca54d73ae34c326b>
				<name>Unicast Packets Out Data Source</name>
				<description></description>
				<column_name>task_item_id</column_name>
				<items>hash_0001019d052e7d632c479737fbfaced0821f79|hash_0001019b9fa6268571b6a04fa4411d8e08c730|hash_0001018e8f2fbeb624029cbda1d2a6ddd991ba|hash_000101c76495beb1ed01f0799838eb8a893124|hash_0001013641f6b8e83ea26e73d41ceccf38b131</items>
			</hash_09010100ae916640272f5aca54d73ae34c326b>
			<hash_0901011bc1652f82488ebfb7242c65d2ffa9c7>
				<name>Unicast Packets In Data Source</name>
				<description></description>
				<column_name>task_item_id</column_name>
				<items>hash_000101d4e5f253f01c3ea77182c5a46418fc44|hash_000101526a96add143da021c5f00d8764a6c12|hash_00010181eeb46f451212f00fd7caee42a81c0b|hash_000101089e4d1c3faeb00fd5dcc9622b06d656|hash_000101042d90f1a390c15509ae208bd97aa885</items>
			</hash_0901011bc1652f82488ebfb7242c65d2ffa9c7>
		</inputs>
	</hash_000101e0d1625a1f4776a5294583659d5cee15>
	<hash_00010110ca5530554da7b73dc69d291bf55d38>
		<name>Interface - Non-Unicast Packets</name>
		<graph>
			<t_title>on</t_title>
			<title>|host_description| - Non-Unicast Packets</title>
			<t_vertical_label></t_vertical_label>
			<vertical_label>packets/sec</vertical_label>
			<t_image_format_id></t_image_format_id>
			<image_format_id>1</image_format_id>
			<t_height></t_height>
			<height>200</height>
			<t_width></t_width>
			<width>700</width>
			<t_base_value></t_base_value>
			<base_value>1000</base_value>
			<t_slope_mode></t_slope_mode>
			<slope_mode>on</slope_mode>
			<t_auto_scale></t_auto_scale>
			<auto_scale>on</auto_scale>
			<t_auto_scale_opts></t_auto_scale_opts>
			<auto_scale_opts>2</auto_scale_opts>
			<t_auto_scale_log></t_auto_scale_log>
			<auto_scale_log></auto_scale_log>
			<t_scale_log_units></t_scale_log_units>
			<scale_log_units></scale_log_units>
			<t_auto_scale_rigid></t_auto_scale_rigid>
			<auto_scale_rigid>on</auto_scale_rigid>
			<t_upper_limit></t_upper_limit>
			<upper_limit>100</upper_limit>
			<t_lower_limit></t_lower_limit>
			<lower_limit>0</lower_limit>
			<t_unit_value></t_unit_value>
			<unit_value></unit_value>
			<t_unit_exponent_value></t_unit_exponent_value>
			<unit_exponent_value></unit_exponent_value>
			<t_unit_length></t_unit_length>
			<unit_length></unit_length>
			<t_no_gridfit></t_no_gridfit>
			<no_gridfit></no_gridfit>
			<t_alt_y_grid></t_alt_y_grid>
			<alt_y_grid></alt_y_grid>
			<t_right_axis></t_right_axis>
			<right_axis></right_axis>
			<t_right_axis_label></t_right_axis_label>
			<right_axis_label></right_axis_label>
			<t_right_axis_format></t_right_axis_format>
			<right_axis_format>0</right_axis_format>
			<t_right_axis_formatter></t_right_axis_formatter>
			<right_axis_formatter></right_axis_formatter>
			<t_left_axis_formatter></t_left_axis_formatter>
			<left_axis_formatter></left_axis_formatter>
			<t_auto_padding></t_auto_padding>
			<auto_padding>on</auto_padding>
			<t_dynamic_labels></t_dynamic_labels>
			<dynamic_labels></dynamic_labels>
			<t_force_rules_legend></t_force_rules_legend>
			<force_rules_legend></force_rules_legend>
			<t_tab_width></t_tab_width>
			<tab_width></tab_width>
			<t_legend_position></t_legend_position>
			<legend_position></legend_position>
			<t_legend_direction></t_legend_direction>
			<legend_direction></legend_direction>
		</graph>
		<items>
			<hash_100101fe66cb973966d22250de073405664200>
				<graph_type_id>7</graph_type_id>
				<task_item_id>hash_08010193e2b6f59b10b13f2ddf2da3ae98b89a</task_item_id>
				<color_id>FFF200</color_id>
				<alpha>7F</alpha>
				<consolidation_function_id>1</consolidation_function_id>
				<cdef_id>0</cdef_id>
				<vdef_id>0</vdef_id>
				<shift></shift>
				<value></value>
				<gprint_id>hash_060101e9c43831e54eca8069317a2ce8c6f751</gprint_id>
				<textalign></textalign>
				<text_format>Non-Unicast Packets In</text_format>
				<hard_return></hard_return>
				<line_width>0.00</line_width>
				<dashes></dashes>
				<dash_offset>0</dash_offset>
				<sequence>1</sequence>
			</hash_100101fe66cb973966d22250de073405664200>
			<hash_1001011ba3fc3466ad32fdd2669cac6cad6faa>
				<graph_type_id>9</graph_type_id>
				<task_item_id>hash_08010193e2b6f59b10b13f2ddf2da3ae98b89a</task_item_id>
				<color_id>0</color_id>
				<alpha>FF</alpha>
				<consolidation_function_id>4</consolidation_function_id>
				<cdef_id>0</cdef_id>
				<vdef_id>0</vdef_id>
				<shift></shift>
				<value></value>
				<gprint_id>hash_060101e9c43831e54eca8069317a2ce8c6f751</gprint_id>
				<textalign></textalign>
				<text_format>Current:</text_format>
				<hard_return></hard_return>
				<line_width>0.00</line_width>
				<dashes></dashes>
				<dash_offset>0</dash_offset>
				<sequence>2</sequence>
			</hash_1001011ba3fc3466ad32fdd2669cac6cad6faa>
			<hash_100101f810154d3a934c723c21659e66199cdf>
				<graph_type_id>9</graph_type_id>
				<task_item_id>hash_08010193e2b6f59b10b13f2ddf2da3ae98b89a</task_item_id>
				<color_id>0</color_id>
				<alpha>FF</alpha>
				<consolidation_function_id>1</consolidation_function_id>
				<cdef_id>0</cdef_id>
				<vdef_id>0</vdef_id>
				<shift></shift>
				<value></value>
				<gprint_id>hash_060101e9c43831e54eca8069317a2ce8c6f751</gprint_id>
				<textalign></textalign>
				<text_format>Average:</text_format>
				<hard_return></hard_return>
				<line_width>0.00</line_width>
				<dashes></dashes>
				<dash_offset>0</dash_offset>
				<sequence>3</sequence>
			</hash_100101f810154d3a934c723c21659e66199cdf>
			<hash_10010198a161df359b01304346657ff1a9d787>
				<graph_type_id>9</graph_type_id>
				<task_item_id>hash_08010193e2b6f59b10b13f2ddf2da3ae98b89a</task_item_id>
				<color_id>0</color_id>
				<alpha>FF</alpha>
				<consolidation_function_id>3</consolidation_function_id>
				<cdef_id>0</cdef_id>
				<vdef_id>0</vdef_id>
				<shift></shift>
				<value></value>
				<gprint_id>hash_060101e9c43831e54eca8069317a2ce8c6f751</gprint_id>
				<textalign></textalign>
				<text_format>Maximum:</text_format>
				<hard_return>on</hard_return>
				<line_width>0.00</line_width>
				<dashes></dashes>
				<dash_offset>0</dash_offset>
				<sequence>4</sequence>
			</hash_10010198a161df359b01304346657ff1a9d787>
			<hash_100101d5e55eaf617ad1f0516f6343b3f07c5e>
				<graph_type_id>7</graph_type_id>
				<task_item_id>hash_0801017be68cbc4ee0b2973eb9785f8c7a35c7</task_item_id>
				<color_id>00234B</color_id>
				<alpha>7F</alpha>
				<consolidation_function_id>1</consolidation_function_id>
				<cdef_id>0</cdef_id>
				<vdef_id>0</vdef_id>
				<shift></shift>
				<value></value>
				<gprint_id>hash_060101e9c43831e54eca8069317a2ce8c6f751</gprint_id>
				<textalign></textalign>
				<text_format>Non-Unicast Packets Out</text_format>
				<hard_return></hard_return>
				<line_width>0.00</line_width>
				<dashes></dashes>
				<dash_offset>0</dash_offset>
				<sequence>5</sequence>
			</hash_100101d5e55eaf617ad1f0516f6343b3f07c5e>
			<hash_1001019fde6b8c84089b9f9044e681162e7567>
				<graph_type_id>9</graph_type_id>
				<task_item_id>hash_0801017be68cbc4ee0b2973eb9785f8c7a35c7</task_item_id>
				<color_id>0</color_id>
				<alpha>FF</alpha>
				<consolidation_function_id>4</consolidation_function_id>
				<cdef_id>0</cdef_id>
				<vdef_id>0</vdef_id>
				<shift></shift>
				<value></value>
				<gprint_id>hash_060101e9c43831e54eca8069317a2ce8c6f751</gprint_id>
				<textalign></textalign>
				<text_format>Current:</text_format>
				<hard_return></hard_return>
				<line_width>0.00</line_width>
				<dashes></dashes>
				<dash_offset>0</dash_offset>
				<sequence>6</sequence>
			</hash_1001019fde6b8c84089b9f9044e681162e7567>
			<hash_1001019a3510727c3d9fa7e2e7a015783a99b3>
				<graph_type_id>9</graph_type_id>
				<task_item_id>hash_0801017be68cbc4ee0b2973eb9785f8c7a35c7</task_item_id>
				<color_id>0</color_id>
				<alpha>FF</alpha>
				<consolidation_function_id>1</consolidation_function_id>
				<cdef_id>0</cdef_id>
				<vdef_id>0</vdef_id>
				<shift></shift>
				<value></value>
				<gprint_id>hash_060101e9c43831e54eca8069317a2ce8c6f751</gprint_id>
				<textalign></textalign>
				<text_format>Average:</text_format>
				<hard_return></hard_return>
				<line_width>0.00</line_width>
				<dashes></dashes>
				<dash_offset>0</dash_offset>
				<sequence>7</sequence>
			</hash_1001019a3510727c3d9fa7e2e7a015783a99b3>
			<hash_100101451afd23f2cb59ab9b975fd6e2735815>
				<graph_type_id>9</graph_type_id>
				<task_item_id>hash_0801017be68cbc4ee0b2973eb9785f8c7a35c7</task_item_id>
				<color_id>0</color_id>
				<alpha>FF</alpha>
				<consolidation_function_id>3</consolidation_function_id>
				<cdef_id>0</cdef_id>
				<vdef_id>0</vdef_id>
				<shift></shift>
				<value></value>
				<gprint_id>hash_060101e9c43831e54eca8069317a2ce8c6f751</gprint_id>
				<textalign></textalign>
				<text_format>Maximum:</text_format>
				<hard_return>on</hard_return>
				<line_width>0.00</line_width>
				<dashes></dashes>
				<dash_offset>0</dash_offset>
				<sequence>8</sequence>
			</hash_100101451afd23f2cb59ab9b975fd6e2735815>
			<hash_100101c72c76b0c6d9066a4feea17ca032b3cd>
				<graph_type_id>4</graph_type_id>
				<task_item_id>hash_08010193e2b6f59b10b13f2ddf2da3ae98b89a</task_item_id>
				<color_id>FFF200</color_id>
				<alpha>FF</alpha>
				<consolidation_function_id>3</consolidation_function_id>
				<cdef_id>0</cdef_id>
				<vdef_id>0</vdef_id>
				<shift></shift>
				<value></value>
				<gprint_id>hash_060101e9c43831e54eca8069317a2ce8c6f751</gprint_id>
				<textalign></textalign>
				<text_format></text_format>
				<hard_return></hard_return>
				<line_width>1.00</line_width>
				<dashes></dashes>
				<dash_offset>0</dash_offset>
				<sequence>9</sequence>
			</hash_100101c72c76b0c6d9066a4feea17ca032b3cd>
			<hash_1001018b281ba233f7a382f8d9094f2019ec94>
				<graph_type_id>4</graph_type_id>
				<task_item_id>hash_0801017be68cbc4ee0b2973eb9785f8c7a35c7</task_item_id>
				<color_id>00234B</color_id>
				<alpha>FF</alpha>
				<consolidation_function_id>3</consolidation_function_id>
				<cdef_id>0</cdef_id>
				<vdef_id>0</vdef_id>
				<shift></shift>
				<value></value>
				<gprint_id>hash_060101e9c43831e54eca8069317a2ce8c6f751</gprint_id>
				<textalign></textalign>
				<text_format></text_format>
				<hard_return></hard_return>
				<line_width>1.00</line_width>
				<dashes></dashes>
				<dash_offset>0</dash_offset>
				<sequence>10</sequence>
			</hash_1001018b281ba233f7a382f8d9094f2019ec94>
		</items>
		<inputs>
			<hash_090101e3177d0e56278de320db203f32fb803d>
				<name>Non-Unicast Packets In Data Source</name>
				<description></description>
				<column_name>task_item_id</column_name>
				<items>hash_000101fe66cb973966d22250de073405664200|hash_0001011ba3fc3466ad32fdd2669cac6cad6faa|hash_000101f810154d3a934c723c21659e66199cdf|hash_00010198a161df359b01304346657ff1a9d787|hash_000101c72c76b0c6d9066a4feea17ca032b3cd</items>
			</hash_090101e3177d0e56278de320db203f32fb803d>
			<hash_0901014f20fba2839764707f1c3373648c5fef>
				<name>Non-Unicast Packets Out Data Source</name>
				<description></description>
				<column_name>task_item_id</column_name>
				<items>hash_000101d5e55eaf617ad1f0516f6343b3f07c5e|hash_0001019fde6b8c84089b9f9044e681162e7567|hash_0001019a3510727c3d9fa7e2e7a015783a99b3|hash_000101451afd23f2cb59ab9b975fd6e2735815|hash_0001018b281ba233f7a382f8d9094f2019ec94</items>
			</hash_0901014f20fba2839764707f1c3373648c5fef>
		</inputs>
	</hash_00010110ca5530554da7b73dc69d291bf55d38>
	<hash_000101df244b337547b434b486662c3c5c7472>
		<name>Interface - Traffic (bytes/sec)</name>
		<graph>
			<t_title>on</t_title>
			<title>|host_description| - Traffic</title>
			<t_vertical_label></t_vertical_label>
			<vertical_label>bytes per second</vertical_label>
			<t_image_format_id></t_image_format_id>
			<image_format_id>1</image_format_id>
			<t_height></t_height>
			<height>200</height>
			<t_width></t_width>
			<width>700</width>
			<t_base_value></t_base_value>
			<base_value>1000</base_value>
			<t_slope_mode></t_slope_mode>
			<slope_mode>on</slope_mode>
			<t_auto_scale></t_auto_scale>
			<auto_scale>on</auto_scale>
			<t_auto_scale_opts></t_auto_scale_opts>
			<auto_scale_opts>2</auto_scale_opts>
			<t_auto_scale_log></t_auto_scale_log>
			<auto_scale_log></auto_scale_log>
			<t_scale_log_units></t_scale_log_units>
			<scale_log_units></scale_log_units>
			<t_auto_scale_rigid></t_auto_scale_rigid>
			<auto_scale_rigid>on</auto_scale_rigid>
			<t_upper_limit></t_upper_limit>
			<upper_limit>100</upper_limit>
			<t_lower_limit></t_lower_limit>
			<lower_limit>0</lower_limit>
			<t_unit_value></t_unit_value>
			<unit_value></unit_value>
			<t_unit_exponent_value></t_unit_exponent_value>
			<unit_exponent_value></unit_exponent_value>
			<t_unit_length></t_unit_length>
			<unit_length></unit_length>
			<t_no_gridfit></t_no_gridfit>
			<no_gridfit></no_gridfit>
			<t_alt_y_grid></t_alt_y_grid>
			<alt_y_grid></alt_y_grid>
			<t_right_axis></t_right_axis>
			<right_axis></right_axis>
			<t_right_axis_label></t_right_axis_label>
			<right_axis_label></right_axis_label>
			<t_right_axis_format></t_right_axis_format>
			<right_axis_format>0</right_axis_format>
			<t_right_axis_formatter></t_right_axis_formatter>
			<right_axis_formatter></right_axis_formatter>
			<t_left_axis_formatter></t_left_axis_formatter>
			<left_axis_formatter></left_axis_formatter>
			<t_auto_padding></t_auto_padding>
			<auto_padding>on</auto_padding>
			<t_dynamic_labels></t_dynamic_labels>
			<dynamic_labels></dynamic_labels>
			<t_force_rules_legend></t_force_rules_legend>
			<force_rules_legend></force_rules_legend>
			<t_tab_width></t_tab_width>
			<tab_width></tab_width>
			<t_legend_position></t_legend_position>
			<legend_position></legend_position>
			<t_legend_direction></t_legend_direction>
			<legend_direction></legend_direction>
		</graph>
		<items>
			<hash_100101b276e28b10447b11ee289f78e0c1ed82>
				<graph_type_id>4</graph_type_id>
				<task_item_id>hash_0801012df25c57022b0c7e7d0be4c035ada1a0</task_item_id>
				<color_id>00CF00</color_id>
				<alpha>FF</alpha>
				<consolidation_function_id>3</consolidation_function_id>
				<cdef_id>0</cdef_id>
				<vdef_id>0</vdef_id>
				<shift></shift>
				<value></value>
				<gprint_id>hash_060101e9c43831e54eca8069317a2ce8c6f751</gprint_id>
				<textalign></textalign>
				<text_format></text_format>
				<hard_return></hard_return>
				<line_width>0.00</line_width>
				<dashes></dashes>
				<dash_offset>0</dash_offset>
				<sequence>1</sequence>
			</hash_100101b276e28b10447b11ee289f78e0c1ed82>
			<hash_100101de3eefd6d6c58afabdabcaf6c0168378>
				<graph_type_id>7</graph_type_id>
				<task_item_id>hash_0801012df25c57022b0c7e7d0be4c035ada1a0</task_item_id>
				<color_id>00CF00</color_id>
				<alpha>7F</alpha>
				<consolidation_function_id>1</consolidation_function_id>
				<cdef_id>0</cdef_id>
				<vdef_id>0</vdef_id>
				<shift></shift>
				<value></value>
				<gprint_id>hash_060101e9c43831e54eca8069317a2ce8c6f751</gprint_id>
				<textalign></textalign>
				<text_format>Inbound</text_format>
				<hard_return></hard_return>
				<line_width>0.00</line_width>
				<dashes></dashes>
				<dash_offset>0</dash_offset>
				<sequence>2</sequence>
			</hash_100101de3eefd6d6c58afabdabcaf6c0168378>
			<hash_1001011a80fa108f5c46eecb03090c65bc9a12>
				<graph_type_id>9</graph_type_id>
				<task_item_id>hash_0801012df25c57022b0c7e7d0be4c035ada1a0</task_item_id>
				<color_id>0</color_id>
				<alpha>FF</alpha>
				<consolidation_function_id>4</consolidation_function_id>
				<cdef_id>0</cdef_id>
				<vdef_id>0</vdef_id>
				<shift></shift>
				<value></value>
				<gprint_id>hash_060101e9c43831e54eca8069317a2ce8c6f751</gprint_id>
				<textalign></textalign>
				<text_format>Current:</text_format>
				<hard_return></hard_return>
				<line_width>0.00</line_width>
				<dashes></dashes>
				<dash_offset>0</dash_offset>
				<sequence>3</sequence>
			</hash_1001011a80fa108f5c46eecb03090c65bc9a12>
			<hash_100101fe458892e7faa9d232e343d911e845f3>
				<graph_type_id>9</graph_type_id>
				<task_item_id>hash_0801012df25c57022b0c7e7d0be4c035ada1a0</task_item_id>
				<color_id>0</color_id>
				<alpha>FF</alpha>
				<consolidation_function_id>1</consolidation_function_id>
				<cdef_id>0</cdef_id>
				<vdef_id>0</vdef_id>
				<shift></shift>
				<value></value>
				<gprint_id>hash_060101e9c43831e54eca8069317a2ce8c6f751</gprint_id>
				<textalign></textalign>
				<text_format>Average:</text_format>
				<hard_return></hard_return>
				<line_width>0.00</line_width>
				<dashes></dashes>
				<dash_offset>0</dash_offset>
				<sequence>4</sequence>
			</hash_100101fe458892e7faa9d232e343d911e845f3>
			<hash_100101175c0a68689bebc38aad2fbc271047b3>
				<graph_type_id>9</graph_type_id>
				<task_item_id>hash_0801012df25c57022b0c7e7d0be4c035ada1a0</task_item_id>
				<color_id>0</color_id>
				<alpha>FF</alpha>
				<consolidation_function_id>3</consolidation_function_id>
				<cdef_id>0</cdef_id>
				<vdef_id>0</vdef_id>
				<shift></shift>
				<value></value>
				<gprint_id>hash_060101e9c43831e54eca8069317a2ce8c6f751</gprint_id>
				<textalign></textalign>
				<text_format>Maximum:</text_format>
				<hard_return>on</hard_return>
				<line_width>0.00</line_width>
				<dashes></dashes>
				<dash_offset>0</dash_offset>
				<sequence>5</sequence>
			</hash_100101175c0a68689bebc38aad2fbc271047b3>
			<hash_100101f9da7d4c2da9636f2f3e37f4781954db>
				<graph_type_id>4</graph_type_id>
				<task_item_id>hash_080101721c0794526d1ac1c359f27dc56faa49</task_item_id>
				<color_id>002A97</color_id>
				<alpha>FF</alpha>
				<consolidation_function_id>3</consolidation_function_id>
				<cdef_id>0</cdef_id>
				<vdef_id>0</vdef_id>
				<shift></shift>
				<value></value>
				<gprint_id>hash_060101e9c43831e54eca8069317a2ce8c6f751</gprint_id>
				<textalign></textalign>
				<text_format></text_format>
				<hard_return></hard_return>
				<line_width>0.00</line_width>
				<dashes></dashes>
				<dash_offset>0</dash_offset>
				<sequence>6</sequence>
			</hash_100101f9da7d4c2da9636f2f3e37f4781954db>
			<hash_1001011bf2283106510491ddf3b9c1376c0b31>
				<graph_type_id>4</graph_type_id>
				<task_item_id>hash_080101721c0794526d1ac1c359f27dc56faa49</task_item_id>
				<color_id>002A97</color_id>
				<alpha>7F</alpha>
				<consolidation_function_id>1</consolidation_function_id>
				<cdef_id>0</cdef_id>
				<vdef_id>0</vdef_id>
				<shift></shift>
				<value></value>
				<gprint_id>hash_060101e9c43831e54eca8069317a2ce8c6f751</gprint_id>
				<textalign></textalign>
				<text_format>Outbound</text_format>
				<hard_return></hard_return>
				<line_width>0.00</line_width>
				<dashes></dashes>
				<dash_offset>0</dash_offset>
				<sequence>7</sequence>
			</hash_1001011bf2283106510491ddf3b9c1376c0b31>
			<hash_100101c5202f1690ffe45600c0d31a4a804f67>
				<graph_type_id>9</graph_type_id>
				<task_item_id>hash_080101721c0794526d1ac1c359f27dc56faa49</task_item_id>
				<color_id>0</color_id>
				<alpha>FF</alpha>
				<consolidation_function_id>4</consolidation_function_id>
				<cdef_id>0</cdef_id>
				<vdef_id>0</vdef_id>
				<shift></shift>
				<value></value>
				<gprint_id>hash_060101e9c43831e54eca8069317a2ce8c6f751</gprint_id>
				<textalign></textalign>
				<text_format>Current:</text_format>
				<hard_return></hard_return>
				<line_width>0.00</line_width>
				<dashes></dashes>
				<dash_offset>0</dash_offset>
				<sequence>8</sequence>
			</hash_100101c5202f1690ffe45600c0d31a4a804f67>
			<hash_100101eb9794e3fdafc2b74f0819269569ed40>
				<graph_type_id>9</graph_type_id>
				<task_item_id>hash_080101721c0794526d1ac1c359f27dc56faa49</task_item_id>
				<color_id>0</color_id>
				<alpha>FF</alpha>
				<consolidation_function_id>1</consolidation_function_id>
				<cdef_id>0</cdef_id>
				<vdef_id>0</vdef_id>
				<shift></shift>
				<value></value>
				<gprint_id>hash_060101e9c43831e54eca8069317a2ce8c6f751</gprint_id>
				<textalign></textalign>
				<text_format>Average:</text_format>
				<hard_return></hard_return>
				<line_width>0.00</line_width>
				<dashes></dashes>
				<dash_offset>0</dash_offset>
				<sequence>9</sequence>
			</hash_100101eb9794e3fdafc2b74f0819269569ed40>
			<hash_1001016bcedd61e3ccf7518ca431940c93c439>
				<graph_type_id>9</graph_type_id>
				<task_item_id>hash_080101721c0794526d1ac1c359f27dc56faa49</task_item_id>
				<color_id>0</color_id>
				<alpha>FF</alpha>
				<consolidation_function_id>3</consolidation_function_id>
				<cdef_id>0</cdef_id>
				<vdef_id>0</vdef_id>
				<shift></shift>
				<value></value>
				<gprint_id>hash_060101e9c43831e54eca8069317a2ce8c6f751</gprint_id>
				<textalign></textalign>
				<text_format>Maximum:</text_format>
				<hard_return>on</hard_return>
				<line_width>0.00</line_width>
				<dashes></dashes>
				<dash_offset>0</dash_offset>
				<sequence>10</sequence>
			</hash_1001016bcedd61e3ccf7518ca431940c93c439>
		</items>
		<inputs>
			<hash_0901012764a4f142ba9fd95872106a1b43541e>
				<name>Inbound Data Source</name>
				<description></description>
				<column_name>task_item_id</column_name>
				<items>hash_000101b276e28b10447b11ee289f78e0c1ed82|hash_000101de3eefd6d6c58afabdabcaf6c0168378|hash_0001011a80fa108f5c46eecb03090c65bc9a12|hash_000101fe458892e7faa9d232e343d911e845f3|hash_000101175c0a68689bebc38aad2fbc271047b3</items>
			</hash_0901012764a4f142ba9fd95872106a1b43541e>
			<hash_090101f73f7ddc1f4349356908122093dbfca2>
				<name>Outbound Data Source</name>
				<description></description>
				<column_name>task_item_id</column_name>
				<items>hash_000101f9da7d4c2da9636f2f3e37f4781954db|hash_0001011bf2283106510491ddf3b9c1376c0b31|hash_000101c5202f1690ffe45600c0d31a4a804f67|hash_000101eb9794e3fdafc2b74f0819269569ed40|hash_0001016bcedd61e3ccf7518ca431940c93c439</items>
			</hash_090101f73f7ddc1f4349356908122093dbfca2>
		</inputs>
	</hash_000101df244b337547b434b486662c3c5c7472>
	<hash_0001011742b2066384637022d178cc5072905a>
		<name>Interface - Traffic (bits/sec, 95th Percentile)</name>
		<graph>
			<t_title>on</t_title>
			<title>|host_description| - Traffic</title>
			<t_vertical_label></t_vertical_label>
			<vertical_label>bits per second</vertical_label>
			<t_image_format_id></t_image_format_id>
			<image_format_id>1</image_format_id>
			<t_height></t_height>
			<height>200</height>
			<t_width></t_width>
			<width>700</width>
			<t_base_value></t_base_value>
			<base_value>1000</base_value>
			<t_slope_mode></t_slope_mode>
			<slope_mode>on</slope_mode>
			<t_auto_scale></t_auto_scale>
			<auto_scale>on</auto_scale>
			<t_auto_scale_opts></t_auto_scale_opts>
			<auto_scale_opts>2</auto_scale_opts>
			<t_auto_scale_log></t_auto_scale_log>
			<auto_scale_log></auto_scale_log>
			<t_scale_log_units></t_scale_log_units>
			<scale_log_units></scale_log_units>
			<t_auto_scale_rigid></t_auto_scale_rigid>
			<auto_scale_rigid>on</auto_scale_rigid>
			<t_upper_limit></t_upper_limit>
			<upper_limit>100</upper_limit>
			<t_lower_limit></t_lower_limit>
			<lower_limit>0</lower_limit>
			<t_unit_value></t_unit_value>
			<unit_value></unit_value>
			<t_unit_exponent_value></t_unit_exponent_value>
			<unit_exponent_value></unit_exponent_value>
			<t_unit_length></t_unit_length>
			<unit_length></unit_length>
			<t_no_gridfit></t_no_gridfit>
			<no_gridfit></no_gridfit>
			<t_alt_y_grid></t_alt_y_grid>
			<alt_y_grid></alt_y_grid>
			<t_right_axis></t_right_axis>
			<right_axis></right_axis>
			<t_right_axis_label></t_right_axis_label>
			<right_axis_label></right_axis_label>
			<t_right_axis_format></t_right_axis_format>
			<right_axis_format>0</right_axis_format>
			<t_right_axis_formatter></t_right_axis_formatter>
			<right_axis_formatter></right_axis_formatter>
			<t_left_axis_formatter></t_left_axis_formatter>
			<left_axis_formatter></left_axis_formatter>
			<t_auto_padding></t_auto_padding>
			<auto_padding>on</auto_padding>
			<t_dynamic_labels></t_dynamic_labels>
			<dynamic_labels></dynamic_labels>
			<t_force_rules_legend></t_force_rules_legend>
			<force_rules_legend></force_rules_legend>
			<t_tab_width></t_tab_width>
			<tab_width></tab_width>
			<t_legend_position></t_legend_position>
			<legend_position></legend_position>
			<t_legend_direction></t_legend_direction>
			<legend_direction></legend_direction>
		</graph>
		<items>
			<hash_10010111d87688979b97cf026809f75cef30be>
				<graph_type_id>4</graph_type_id>
				<task_item_id>hash_0801012df25c57022b0c7e7d0be4c035ada1a0</task_item_id>
				<color_id>00CF00</color_id>
				<alpha>FF</alpha>
				<consolidation_function_id>3</consolidation_function_id>
				<cdef_id>hash_05010173f95f8b77b5508157d64047342c421e</cdef_id>
				<vdef_id>0</vdef_id>
				<shift></shift>
				<value></value>
				<gprint_id>hash_060101e9c43831e54eca8069317a2ce8c6f751</gprint_id>
				<textalign></textalign>
				<text_format></text_format>
				<hard_return></hard_return>
				<line_width>1.00</line_width>
				<dashes></dashes>
				<dash_offset>0</dash_offset>
				<sequence>1</sequence>
			</hash_10010111d87688979b97cf026809f75cef30be>
			<hash_100101918e6e7d41bb4bae0ea2937b461742a4>
				<graph_type_id>7</graph_type_id>
				<task_item_id>hash_0801012df25c57022b0c7e7d0be4c035ada1a0</task_item_id>
				<color_id>00CF00</color_id>
				<alpha>7F</alpha>
				<consolidation_function_id>1</consolidation_function_id>
				<cdef_id>hash_05010173f95f8b77b5508157d64047342c421e</cdef_id>
				<vdef_id>0</vdef_id>
				<shift></shift>
				<value></value>
				<gprint_id>hash_060101e9c43831e54eca8069317a2ce8c6f751</gprint_id>
				<textalign></textalign>
				<text_format>Inbound</text_format>
				<hard_return></hard_return>
				<line_width>0.00</line_width>
				<dashes></dashes>
				<dash_offset>0</dash_offset>
				<sequence>2</sequence>
			</hash_100101918e6e7d41bb4bae0ea2937b461742a4>
			<hash_100101f19fbd06c989ea85acd6b4f926e4a456>
				<graph_type_id>9</graph_type_id>
				<task_item_id>hash_0801012df25c57022b0c7e7d0be4c035ada1a0</task_item_id>
				<color_id>0</color_id>
				<alpha>FF</alpha>
				<consolidation_function_id>4</consolidation_function_id>
				<cdef_id>hash_05010173f95f8b77b5508157d64047342c421e</cdef_id>
				<vdef_id>0</vdef_id>
				<shift></shift>
				<value></value>
				<gprint_id>hash_060101e9c43831e54eca8069317a2ce8c6f751</gprint_id>
				<textalign></textalign>
				<text_format>Current:</text_format>
				<hard_return></hard_return>
				<line_width>0.00</line_width>
				<dashes></dashes>
				<dash_offset>0</dash_offset>
				<sequence>3</sequence>
			</hash_100101f19fbd06c989ea85acd6b4f926e4a456>
			<hash_100101fc150a15e20c57e11e8d05feca557ef9>
				<graph_type_id>9</graph_type_id>
				<task_item_id>hash_0801012df25c57022b0c7e7d0be4c035ada1a0</task_item_id>
				<color_id>0</color_id>
				<alpha>FF</alpha>
				<consolidation_function_id>1</consolidation_function_id>
				<cdef_id>hash_05010173f95f8b77b5508157d64047342c421e</cdef_id>
				<vdef_id>0</vdef_id>
				<shift></shift>
				<value></value>
				<gprint_id>hash_060101e9c43831e54eca8069317a2ce8c6f751</gprint_id>
				<textalign></textalign>
				<text_format>Average:</text_format>
				<hard_return></hard_return>
				<line_width>0.00</line_width>
				<dashes></dashes>
				<dash_offset>0</dash_offset>
				<sequence>4</sequence>
			</hash_100101fc150a15e20c57e11e8d05feca557ef9>
			<hash_100101ccbd86e03ccf07483b4d29e63612fb18>
				<graph_type_id>9</graph_type_id>
				<task_item_id>hash_0801012df25c57022b0c7e7d0be4c035ada1a0</task_item_id>
				<color_id>0</color_id>
				<alpha>FF</alpha>
				<consolidation_function_id>3</consolidation_function_id>
				<cdef_id>hash_05010173f95f8b77b5508157d64047342c421e</cdef_id>
				<vdef_id>0</vdef_id>
				<shift></shift>
				<value></value>
				<gprint_id>hash_060101e9c43831e54eca8069317a2ce8c6f751</gprint_id>
				<textalign></textalign>
				<text_format>Maximum:</text_format>
				<hard_return>on</hard_return>
				<line_width>0.00</line_width>
				<dashes></dashes>
				<dash_offset>0</dash_offset>
				<sequence>5</sequence>
			</hash_100101ccbd86e03ccf07483b4d29e63612fb18>
			<hash_10010175796e3f885739c2d7229fd25babf30d>
				<graph_type_id>4</graph_type_id>
				<task_item_id>hash_080101721c0794526d1ac1c359f27dc56faa49</task_item_id>
				<color_id>002A97</color_id>
				<alpha>FF</alpha>
				<consolidation_function_id>3</consolidation_function_id>
				<cdef_id>0</cdef_id>
				<vdef_id>0</vdef_id>
				<shift></shift>
				<value></value>
				<gprint_id>hash_060101e9c43831e54eca8069317a2ce8c6f751</gprint_id>
				<textalign></textalign>
				<text_format></text_format>
				<hard_return></hard_return>
				<line_width>1.00</line_width>
				<dashes></dashes>
				<dash_offset>0</dash_offset>
				<sequence>6</sequence>
			</hash_10010175796e3f885739c2d7229fd25babf30d>
			<hash_100101964c5c30cd05eaf5a49c0377d173de86>
				<graph_type_id>7</graph_type_id>
				<task_item_id>hash_080101721c0794526d1ac1c359f27dc56faa49</task_item_id>
				<color_id>002A97</color_id>
				<alpha>7F</alpha>
				<consolidation_function_id>1</consolidation_function_id>
				<cdef_id>hash_05010173f95f8b77b5508157d64047342c421e</cdef_id>
				<vdef_id>0</vdef_id>
				<shift></shift>
				<value></value>
				<gprint_id>hash_060101e9c43831e54eca8069317a2ce8c6f751</gprint_id>
				<textalign></textalign>
				<text_format>Outbound</text_format>
				<hard_return></hard_return>
				<line_width>0.00</line_width>
				<dashes></dashes>
				<dash_offset>0</dash_offset>
				<sequence>7</sequence>
			</hash_100101964c5c30cd05eaf5a49c0377d173de86>
			<hash_100101b1a6fb775cf62e79e1c4bc4933c7e4ce>
				<graph_type_id>9</graph_type_id>
				<task_item_id>hash_080101721c0794526d1ac1c359f27dc56faa49</task_item_id>
				<color_id>0</color_id>
				<alpha>FF</alpha>
				<consolidation_function_id>4</consolidation_function_id>
				<cdef_id>hash_05010173f95f8b77b5508157d64047342c421e</cdef_id>
				<vdef_id>0</vdef_id>
				<shift></shift>
				<value></value>
				<gprint_id>hash_060101e9c43831e54eca8069317a2ce8c6f751</gprint_id>
				<textalign></textalign>
				<text_format>Current:</text_format>
				<hard_return></hard_return>
				<line_width>0.00</line_width>
				<dashes></dashes>
				<dash_offset>0</dash_offset>
				<sequence>8</sequence>
			</hash_100101b1a6fb775cf62e79e1c4bc4933c7e4ce>
			<hash_100101721038182a872ab266b5cf1bf7f7755c>
				<graph_type_id>9</graph_type_id>
				<task_item_id>hash_080101721c0794526d1ac1c359f27dc56faa49</task_item_id>
				<color_id>0</color_id>
				<alpha>FF</alpha>
				<consolidation_function_id>1</consolidation_function_id>
				<cdef_id>hash_05010173f95f8b77b5508157d64047342c421e</cdef_id>
				<vdef_id>0</vdef_id>
				<shift></shift>
				<value></value>
				<gprint_id>hash_060101e9c43831e54eca8069317a2ce8c6f751</gprint_id>
				<textalign></textalign>
				<text_format>Average:</text_format>
				<hard_return></hard_return>
				<line_width>0.00</line_width>
				<dashes></dashes>
				<dash_offset>0</dash_offset>
				<sequence>9</sequence>
			</hash_100101721038182a872ab266b5cf1bf7f7755c>
			<hash_1001012302f80c2c70b897d12182a1fc11ecd6>
				<graph_type_id>9</graph_type_id>
				<task_item_id>hash_080101721c0794526d1ac1c359f27dc56faa49</task_item_id>
				<color_id>0</color_id>
				<alpha>FF</alpha>
				<consolidation_function_id>3</consolidation_function_id>
				<cdef_id>hash_05010173f95f8b77b5508157d64047342c421e</cdef_id>
				<vdef_id>0</vdef_id>
				<shift></shift>
				<value></value>
				<gprint_id>hash_060101e9c43831e54eca8069317a2ce8c6f751</gprint_id>
				<textalign></textalign>
				<text_format>Maximum:</text_format>
				<hard_return>on</hard_return>
				<line_width>0.00</line_width>
				<dashes></dashes>
				<dash_offset>0</dash_offset>
				<sequence>10</sequence>
			</hash_1001012302f80c2c70b897d12182a1fc11ecd6>
			<hash_1001014ffc7af8533d103748316752b70f8e3c>
				<graph_type_id>1</graph_type_id>
				<task_item_id>0</task_item_id>
				<color_id>0</color_id>
				<alpha>FF</alpha>
				<consolidation_function_id>1</consolidation_function_id>
				<cdef_id>0</cdef_id>
				<vdef_id>0</vdef_id>
				<shift></shift>
				<value></value>
				<gprint_id>hash_060101e9c43831e54eca8069317a2ce8c6f751</gprint_id>
				<textalign></textalign>
				<text_format></text_format>
				<hard_return>on</hard_return>
				<line_width>0.00</line_width>
				<dashes></dashes>
				<dash_offset>0</dash_offset>
				<sequence>11</sequence>
			</hash_1001014ffc7af8533d103748316752b70f8e3c>
			<hash_10010164527c4b6eeeaf627acc5117ff2180fd>
				<graph_type_id>2</graph_type_id>
				<task_item_id>hash_080101721c0794526d1ac1c359f27dc56faa49</task_item_id>
				<color_id>FF0000</color_id>
				<alpha>FF</alpha>
				<consolidation_function_id>1</consolidation_function_id>
				<cdef_id>0</cdef_id>
				<vdef_id>0</vdef_id>
				<shift></shift>
				<value>|95:bits:0:max:2|</value>
				<gprint_id>hash_060101e9c43831e54eca8069317a2ce8c6f751</gprint_id>
				<textalign></textalign>
				<text_format>95th Percentile</text_format>
				<hard_return></hard_return>
				<line_width>0.00</line_width>
				<dashes></dashes>
				<dash_offset>0</dash_offset>
				<sequence>12</sequence>
			</hash_10010164527c4b6eeeaf627acc5117ff2180fd>
			<hash_100101d5bbcbdbf83ae858862611ac6de8fc62>
				<graph_type_id>1</graph_type_id>
				<task_item_id>hash_080101721c0794526d1ac1c359f27dc56faa49</task_item_id>
				<color_id>0</color_id>
				<alpha>FF</alpha>
				<consolidation_function_id>1</consolidation_function_id>
				<cdef_id>0</cdef_id>
				<vdef_id>0</vdef_id>
				<shift></shift>
				<value></value>
				<gprint_id>hash_060101e9c43831e54eca8069317a2ce8c6f751</gprint_id>
				<textalign></textalign>
				<text_format>(|95:bits:6:max:2| mbit in+out)</text_format>
				<hard_return></hard_return>
				<line_width>0.00</line_width>
				<dashes></dashes>
				<dash_offset>0</dash_offset>
				<sequence>13</sequence>
			</hash_100101d5bbcbdbf83ae858862611ac6de8fc62>
		</items>
		<inputs>
			<hash_090101562726cccdb67d5c6941e9e826ef4ef5>
				<name>Inbound Data Source</name>
				<description></description>
				<column_name>task_item_id</column_name>
				<items>hash_00010111d87688979b97cf026809f75cef30be|hash_000101918e6e7d41bb4bae0ea2937b461742a4|hash_000101f19fbd06c989ea85acd6b4f926e4a456|hash_000101fc150a15e20c57e11e8d05feca557ef9|hash_000101ccbd86e03ccf07483b4d29e63612fb18</items>
			</hash_090101562726cccdb67d5c6941e9e826ef4ef5>
			<hash_09010182426afec226f8189c8928e7f083f80f>
				<name>Outbound Data Source</name>
				<description></description>
				<column_name>task_item_id</column_name>
				<items>hash_00010175796e3f885739c2d7229fd25babf30d|hash_000101964c5c30cd05eaf5a49c0377d173de86|hash_000101b1a6fb775cf62e79e1c4bc4933c7e4ce|hash_000101721038182a872ab266b5cf1bf7f7755c|hash_0001012302f80c2c70b897d12182a1fc11ecd6|hash_00010164527c4b6eeeaf627acc5117ff2180fd|hash_000101d5bbcbdbf83ae858862611ac6de8fc62</items>
			</hash_09010182426afec226f8189c8928e7f083f80f>
		</inputs>
	</hash_0001011742b2066384637022d178cc5072905a>
	<hash_00010113b47e10b2d5db45707d61851f69c52b>
		<name>Interface - Traffic (bits/sec, Total Bandwidth)</name>
		<graph>
			<t_title>on</t_title>
			<title>|host_description| - Traffic</title>
			<t_vertical_label></t_vertical_label>
			<vertical_label>bits per second</vertical_label>
			<t_image_format_id></t_image_format_id>
			<image_format_id>1</image_format_id>
			<t_height></t_height>
			<height>200</height>
			<t_width></t_width>
			<width>700</width>
			<t_base_value></t_base_value>
			<base_value>1000</base_value>
			<t_slope_mode></t_slope_mode>
			<slope_mode>on</slope_mode>
			<t_auto_scale></t_auto_scale>
			<auto_scale>on</auto_scale>
			<t_auto_scale_opts></t_auto_scale_opts>
			<auto_scale_opts>2</auto_scale_opts>
			<t_auto_scale_log></t_auto_scale_log>
			<auto_scale_log></auto_scale_log>
			<t_scale_log_units></t_scale_log_units>
			<scale_log_units></scale_log_units>
			<t_auto_scale_rigid></t_auto_scale_rigid>
			<auto_scale_rigid>on</auto_scale_rigid>
			<t_upper_limit></t_upper_limit>
			<upper_limit>100</upper_limit>
			<t_lower_limit></t_lower_limit>
			<lower_limit>0</lower_limit>
			<t_unit_value></t_unit_value>
			<unit_value></unit_value>
			<t_unit_exponent_value></t_unit_exponent_value>
			<unit_exponent_value></unit_exponent_value>
			<t_unit_length></t_unit_length>
			<unit_length></unit_length>
			<t_no_gridfit></t_no_gridfit>
			<no_gridfit></no_gridfit>
			<t_alt_y_grid></t_alt_y_grid>
			<alt_y_grid></alt_y_grid>
			<t_right_axis></t_right_axis>
			<right_axis></right_axis>
			<t_right_axis_label></t_right_axis_label>
			<right_axis_label></right_axis_label>
			<t_right_axis_format></t_right_axis_format>
			<right_axis_format>0</right_axis_format>
			<t_right_axis_formatter></t_right_axis_formatter>
			<right_axis_formatter>0</right_axis_formatter>
			<t_left_axis_formatter></t_left_axis_formatter>
			<left_axis_formatter>0</left_axis_formatter>
			<t_auto_padding></t_auto_padding>
			<auto_padding>on</auto_padding>
			<t_dynamic_labels></t_dynamic_labels>
			<dynamic_labels></dynamic_labels>
			<t_force_rules_legend></t_force_rules_legend>
			<force_rules_legend></force_rules_legend>
			<t_tab_width></t_tab_width>
			<tab_width></tab_width>
			<t_legend_position></t_legend_position>
			<legend_position>0</legend_position>
			<t_legend_direction></t_legend_direction>
			<legend_direction>0</legend_direction>
		</graph>
		<items>
			<hash_1001019ee6db2f910144bc95760876d0a16a62>
				<graph_type_id>4</graph_type_id>
				<task_item_id>hash_0801012df25c57022b0c7e7d0be4c035ada1a0</task_item_id>
				<color_id>00CF00</color_id>
				<alpha>FF</alpha>
				<consolidation_function_id>3</consolidation_function_id>
				<cdef_id>hash_05010173f95f8b77b5508157d64047342c421e</cdef_id>
				<vdef_id>0</vdef_id>
				<shift></shift>
				<value></value>
				<gprint_id>hash_060101e9c43831e54eca8069317a2ce8c6f751</gprint_id>
				<textalign></textalign>
				<text_format></text_format>
				<hard_return></hard_return>
				<line_width>1.00</line_width>
				<dashes></dashes>
				<dash_offset>0</dash_offset>
				<sequence>1</sequence>
			</hash_1001019ee6db2f910144bc95760876d0a16a62>
			<hash_1001011995d8c23e7d8e1efa2b2c55daf3c5a7>
				<graph_type_id>7</graph_type_id>
				<task_item_id>hash_0801012df25c57022b0c7e7d0be4c035ada1a0</task_item_id>
				<color_id>00CF00</color_id>
				<alpha>7F</alpha>
				<consolidation_function_id>1</consolidation_function_id>
				<cdef_id>hash_05010173f95f8b77b5508157d64047342c421e</cdef_id>
				<vdef_id>0</vdef_id>
				<shift></shift>
				<value></value>
				<gprint_id>hash_060101e9c43831e54eca8069317a2ce8c6f751</gprint_id>
				<textalign></textalign>
				<text_format>Inbound</text_format>
				<hard_return></hard_return>
				<line_width>0.00</line_width>
				<dashes></dashes>
				<dash_offset>0</dash_offset>
				<sequence>2</sequence>
			</hash_1001011995d8c23e7d8e1efa2b2c55daf3c5a7>
			<hash_10010155083351cd728b82cc4dde68eb935700>
				<graph_type_id>9</graph_type_id>
				<task_item_id>hash_0801012df25c57022b0c7e7d0be4c035ada1a0</task_item_id>
				<color_id>0</color_id>
				<alpha>FF</alpha>
				<consolidation_function_id>4</consolidation_function_id>
				<cdef_id>hash_05010173f95f8b77b5508157d64047342c421e</cdef_id>
				<vdef_id>0</vdef_id>
				<shift></shift>
				<value></value>
				<gprint_id>hash_060101e9c43831e54eca8069317a2ce8c6f751</gprint_id>
				<textalign></textalign>
				<text_format>Current:</text_format>
				<hard_return></hard_return>
				<line_width>0.00</line_width>
				<dashes></dashes>
				<dash_offset>0</dash_offset>
				<sequence>3</sequence>
			</hash_10010155083351cd728b82cc4dde68eb935700>
			<hash_10010154782f71929e7d1734ed5ad4b8dda50d>
				<graph_type_id>9</graph_type_id>
				<task_item_id>hash_0801012df25c57022b0c7e7d0be4c035ada1a0</task_item_id>
				<color_id>0</color_id>
				<alpha>FF</alpha>
				<consolidation_function_id>1</consolidation_function_id>
				<cdef_id>hash_05010173f95f8b77b5508157d64047342c421e</cdef_id>
				<vdef_id>0</vdef_id>
				<shift></shift>
				<value></value>
				<gprint_id>hash_060101e9c43831e54eca8069317a2ce8c6f751</gprint_id>
				<textalign></textalign>
				<text_format>Average:</text_format>
				<hard_return></hard_return>
				<line_width>0.00</line_width>
				<dashes></dashes>
				<dash_offset>0</dash_offset>
				<sequence>4</sequence>
			</hash_10010154782f71929e7d1734ed5ad4b8dda50d>
			<hash_10010188d3094d5dc2164cbf2f974aeb92f051>
				<graph_type_id>9</graph_type_id>
				<task_item_id>hash_0801012df25c57022b0c7e7d0be4c035ada1a0</task_item_id>
				<color_id>0</color_id>
				<alpha>FF</alpha>
				<consolidation_function_id>3</consolidation_function_id>
				<cdef_id>hash_05010173f95f8b77b5508157d64047342c421e</cdef_id>
				<vdef_id>0</vdef_id>
				<shift></shift>
				<value></value>
				<gprint_id>hash_060101e9c43831e54eca8069317a2ce8c6f751</gprint_id>
				<textalign></textalign>
				<text_format>Maximum:</text_format>
				<hard_return></hard_return>
				<line_width>0.00</line_width>
				<dashes></dashes>
				<dash_offset>0</dash_offset>
				<sequence>5</sequence>
			</hash_10010188d3094d5dc2164cbf2f974aeb92f051>
			<hash_1001015b43e4102600ad75379c5afd235099c4>
				<graph_type_id>1</graph_type_id>
				<task_item_id>hash_0801012df25c57022b0c7e7d0be4c035ada1a0</task_item_id>
				<color_id>0</color_id>
				<alpha>FF</alpha>
				<consolidation_function_id>1</consolidation_function_id>
				<cdef_id>0</cdef_id>
				<vdef_id>0</vdef_id>
				<shift></shift>
				<value></value>
				<gprint_id>hash_060101e9c43831e54eca8069317a2ce8c6f751</gprint_id>
				<textalign></textalign>
				<text_format>Total In:  |sum:auto:current:2:auto|</text_format>
				<hard_return>on</hard_return>
				<line_width>0.00</line_width>
				<dashes></dashes>
				<dash_offset>0</dash_offset>
				<sequence>6</sequence>
			</hash_1001015b43e4102600ad75379c5afd235099c4>
			<hash_100101c4886a8552ee60c6559de8ab16c2dcf2>
				<graph_type_id>4</graph_type_id>
				<task_item_id>hash_080101721c0794526d1ac1c359f27dc56faa49</task_item_id>
				<color_id>002A97</color_id>
				<alpha>FF</alpha>
				<consolidation_function_id>3</consolidation_function_id>
				<cdef_id>hash_05010173f95f8b77b5508157d64047342c421e</cdef_id>
				<vdef_id>0</vdef_id>
				<shift></shift>
				<value></value>
				<gprint_id>hash_060101e9c43831e54eca8069317a2ce8c6f751</gprint_id>
				<textalign></textalign>
				<text_format></text_format>
				<hard_return></hard_return>
				<line_width>1.00</line_width>
				<dashes></dashes>
				<dash_offset>0</dash_offset>
				<sequence>7</sequence>
			</hash_100101c4886a8552ee60c6559de8ab16c2dcf2>
			<hash_1001014a381a8e87d4db1ac99cf8d9078266d3>
				<graph_type_id>7</graph_type_id>
				<task_item_id>hash_080101721c0794526d1ac1c359f27dc56faa49</task_item_id>
				<color_id>002A97</color_id>
				<alpha>7F</alpha>
				<consolidation_function_id>1</consolidation_function_id>
				<cdef_id>hash_05010173f95f8b77b5508157d64047342c421e</cdef_id>
				<vdef_id>0</vdef_id>
				<shift></shift>
				<value></value>
				<gprint_id>hash_060101e9c43831e54eca8069317a2ce8c6f751</gprint_id>
				<textalign></textalign>
				<text_format>Outbound</text_format>
				<hard_return></hard_return>
				<line_width>0.00</line_width>
				<dashes></dashes>
				<dash_offset>0</dash_offset>
				<sequence>8</sequence>
			</hash_1001014a381a8e87d4db1ac99cf8d9078266d3>
			<hash_1001015bff63207c7bf076d76ff3036b5dad54>
				<graph_type_id>9</graph_type_id>
				<task_item_id>hash_080101721c0794526d1ac1c359f27dc56faa49</task_item_id>
				<color_id>0</color_id>
				<alpha>FF</alpha>
				<consolidation_function_id>4</consolidation_function_id>
				<cdef_id>hash_05010173f95f8b77b5508157d64047342c421e</cdef_id>
				<vdef_id>0</vdef_id>
				<shift></shift>
				<value></value>
				<gprint_id>hash_060101e9c43831e54eca8069317a2ce8c6f751</gprint_id>
				<textalign></textalign>
				<text_format>Current:</text_format>
				<hard_return></hard_return>
				<line_width>0.00</line_width>
				<dashes></dashes>
				<dash_offset>0</dash_offset>
				<sequence>9</sequence>
			</hash_1001015bff63207c7bf076d76ff3036b5dad54>
			<hash_100101979fff9d691ca35e3f4b3383d9cae43f>
				<graph_type_id>9</graph_type_id>
				<task_item_id>hash_080101721c0794526d1ac1c359f27dc56faa49</task_item_id>
				<color_id>0</color_id>
				<alpha>FF</alpha>
				<consolidation_function_id>1</consolidation_function_id>
				<cdef_id>hash_05010173f95f8b77b5508157d64047342c421e</cdef_id>
				<vdef_id>0</vdef_id>
				<shift></shift>
				<value></value>
				<gprint_id>hash_060101e9c43831e54eca8069317a2ce8c6f751</gprint_id>
				<textalign></textalign>
				<text_format>Average:</text_format>
				<hard_return></hard_return>
				<line_width>0.00</line_width>
				<dashes></dashes>
				<dash_offset>0</dash_offset>
				<sequence>10</sequence>
			</hash_100101979fff9d691ca35e3f4b3383d9cae43f>
			<hash_1001010e715933830112c23c15f7e3463f77b6>
				<graph_type_id>9</graph_type_id>
				<task_item_id>hash_080101721c0794526d1ac1c359f27dc56faa49</task_item_id>
				<color_id>0</color_id>
				<alpha>FF</alpha>
				<consolidation_function_id>3</consolidation_function_id>
				<cdef_id>hash_05010173f95f8b77b5508157d64047342c421e</cdef_id>
				<vdef_id>0</vdef_id>
				<shift></shift>
				<value></value>
				<gprint_id>hash_060101e9c43831e54eca8069317a2ce8c6f751</gprint_id>
				<textalign></textalign>
				<text_format>Maximum:</text_format>
				<hard_return></hard_return>
				<line_width>0.00</line_width>
				<dashes></dashes>
				<dash_offset>0</dash_offset>
				<sequence>11</sequence>
			</hash_1001010e715933830112c23c15f7e3463f77b6>
			<hash_100101db7c15d253ca666601b3296f2574edc9>
				<graph_type_id>1</graph_type_id>
				<task_item_id>hash_080101721c0794526d1ac1c359f27dc56faa49</task_item_id>
				<color_id>0</color_id>
				<alpha>FF</alpha>
				<consolidation_function_id>1</consolidation_function_id>
				<cdef_id>0</cdef_id>
				<vdef_id>0</vdef_id>
				<shift></shift>
				<value></value>
				<gprint_id>hash_060101e9c43831e54eca8069317a2ce8c6f751</gprint_id>
				<textalign></textalign>
				<text_format>Total Out: |sum:auto:current:2:auto|</text_format>
				<hard_return>on</hard_return>
				<line_width>0.00</line_width>
				<dashes></dashes>
				<dash_offset>0</dash_offset>
				<sequence>12</sequence>
			</hash_100101db7c15d253ca666601b3296f2574edc9>
		</items>
		<inputs>
			<hash_09010169a23877302e7d142f254b208c58b596>
				<name>Inbound Data Source</name>
				<description></description>
				<column_name>task_item_id</column_name>
				<items>hash_0001019ee6db2f910144bc95760876d0a16a62|hash_0001011995d8c23e7d8e1efa2b2c55daf3c5a7|hash_00010155083351cd728b82cc4dde68eb935700|hash_00010154782f71929e7d1734ed5ad4b8dda50d|hash_00010188d3094d5dc2164cbf2f974aeb92f051|hash_0001015b43e4102600ad75379c5afd235099c4</items>
			</hash_09010169a23877302e7d142f254b208c58b596>
			<hash_090101f28013abf8e5813870df0f4111a5e695>
				<name>Outbound Data Source</name>
				<description></description>
				<column_name>task_item_id</column_name>
				<items>hash_000101c4886a8552ee60c6559de8ab16c2dcf2|hash_0001014a381a8e87d4db1ac99cf8d9078266d3|hash_0001015bff63207c7bf076d76ff3036b5dad54|hash_000101979fff9d691ca35e3f4b3383d9cae43f|hash_0001010e715933830112c23c15f7e3463f77b6|hash_000101db7c15d253ca666601b3296f2574edc9</items>
			</hash_090101f28013abf8e5813870df0f4111a5e695>
		</inputs>
	</hash_00010113b47e10b2d5db45707d61851f69c52b>
	<hash_0001018ad6790c22b693680e041f21d62537ac>
		<name>Interface - Traffic (bytes/sec, Total Bandwidth)</name>
		<graph>
			<t_title>on</t_title>
			<title>|host_description| - Traffic</title>
			<t_vertical_label></t_vertical_label>
			<vertical_label>bytes per second</vertical_label>
			<t_image_format_id></t_image_format_id>
			<image_format_id>1</image_format_id>
			<t_height></t_height>
			<height>200</height>
			<t_width></t_width>
			<width>700</width>
			<t_base_value></t_base_value>
			<base_value>1000</base_value>
			<t_slope_mode></t_slope_mode>
			<slope_mode>on</slope_mode>
			<t_auto_scale></t_auto_scale>
			<auto_scale>on</auto_scale>
			<t_auto_scale_opts></t_auto_scale_opts>
			<auto_scale_opts>2</auto_scale_opts>
			<t_auto_scale_log></t_auto_scale_log>
			<auto_scale_log></auto_scale_log>
			<t_scale_log_units></t_scale_log_units>
			<scale_log_units></scale_log_units>
			<t_auto_scale_rigid></t_auto_scale_rigid>
			<auto_scale_rigid>on</auto_scale_rigid>
			<t_upper_limit></t_upper_limit>
			<upper_limit>100</upper_limit>
			<t_lower_limit></t_lower_limit>
			<lower_limit>0</lower_limit>
			<t_unit_value></t_unit_value>
			<unit_value></unit_value>
			<t_unit_exponent_value></t_unit_exponent_value>
			<unit_exponent_value></unit_exponent_value>
			<t_unit_length></t_unit_length>
			<unit_length></unit_length>
			<t_no_gridfit></t_no_gridfit>
			<no_gridfit></no_gridfit>
			<t_alt_y_grid></t_alt_y_grid>
			<alt_y_grid></alt_y_grid>
			<t_right_axis></t_right_axis>
			<right_axis></right_axis>
			<t_right_axis_label></t_right_axis_label>
			<right_axis_label></right_axis_label>
			<t_right_axis_format></t_right_axis_format>
			<right_axis_format>0</right_axis_format>
			<t_right_axis_formatter></t_right_axis_formatter>
			<right_axis_formatter></right_axis_formatter>
			<t_left_axis_formatter></t_left_axis_formatter>
			<left_axis_formatter></left_axis_formatter>
			<t_auto_padding></t_auto_padding>
			<auto_padding>on</auto_padding>
			<t_dynamic_labels></t_dynamic_labels>
			<dynamic_labels></dynamic_labels>
			<t_force_rules_legend></t_force_rules_legend>
			<force_rules_legend></force_rules_legend>
			<t_tab_width></t_tab_width>
			<tab_width></tab_width>
			<t_legend_position></t_legend_position>
			<legend_position></legend_position>
			<t_legend_direction></t_legend_direction>
			<legend_direction></legend_direction>
		</graph>
		<items>
			<hash_1001013baa47b136f8c36ccea69196b0285a6c>
				<graph_type_id>4</graph_type_id>
				<task_item_id>hash_0801012df25c57022b0c7e7d0be4c035ada1a0</task_item_id>
				<color_id>00CF00</color_id>
				<alpha>FF</alpha>
				<consolidation_function_id>3</consolidation_function_id>
				<cdef_id>0</cdef_id>
				<vdef_id>0</vdef_id>
				<shift></shift>
				<value></value>
				<gprint_id>hash_060101e9c43831e54eca8069317a2ce8c6f751</gprint_id>
				<textalign></textalign>
				<text_format></text_format>
				<hard_return></hard_return>
				<line_width>1.00</line_width>
				<dashes></dashes>
				<dash_offset>0</dash_offset>
				<sequence>1</sequence>
			</hash_1001013baa47b136f8c36ccea69196b0285a6c>
			<hash_1001013ff8dba1ca6279692b3fcabed0bc2631>
				<graph_type_id>7</graph_type_id>
				<task_item_id>hash_0801012df25c57022b0c7e7d0be4c035ada1a0</task_item_id>
				<color_id>00CF00</color_id>
				<alpha>7F</alpha>
				<consolidation_function_id>1</consolidation_function_id>
				<cdef_id>0</cdef_id>
				<vdef_id>0</vdef_id>
				<shift></shift>
				<value></value>
				<gprint_id>hash_060101e9c43831e54eca8069317a2ce8c6f751</gprint_id>
				<textalign></textalign>
				<text_format>Inbound</text_format>
				<hard_return></hard_return>
				<line_width>0.00</line_width>
				<dashes></dashes>
				<dash_offset>0</dash_offset>
				<sequence>2</sequence>
			</hash_1001013ff8dba1ca6279692b3fcabed0bc2631>
			<hash_10010166bfdb701c8eeadffe55e926d6e77e71>
				<graph_type_id>9</graph_type_id>
				<task_item_id>hash_0801012df25c57022b0c7e7d0be4c035ada1a0</task_item_id>
				<color_id>0</color_id>
				<alpha>FF</alpha>
				<consolidation_function_id>4</consolidation_function_id>
				<cdef_id>0</cdef_id>
				<vdef_id>0</vdef_id>
				<shift></shift>
				<value></value>
				<gprint_id>hash_060101e9c43831e54eca8069317a2ce8c6f751</gprint_id>
				<textalign></textalign>
				<text_format>Current:</text_format>
				<hard_return></hard_return>
				<line_width>0.00</line_width>
				<dashes></dashes>
				<dash_offset>0</dash_offset>
				<sequence>3</sequence>
			</hash_10010166bfdb701c8eeadffe55e926d6e77e71>
			<hash_100101777aa88fb0a79b60d081e0e3759f1cf7>
				<graph_type_id>9</graph_type_id>
				<task_item_id>hash_0801012df25c57022b0c7e7d0be4c035ada1a0</task_item_id>
				<color_id>0</color_id>
				<alpha>FF</alpha>
				<consolidation_function_id>1</consolidation_function_id>
				<cdef_id>0</cdef_id>
				<vdef_id>0</vdef_id>
				<shift></shift>
				<value></value>
				<gprint_id>hash_060101e9c43831e54eca8069317a2ce8c6f751</gprint_id>
				<textalign></textalign>
				<text_format>Average:</text_format>
				<hard_return></hard_return>
				<line_width>0.00</line_width>
				<dashes></dashes>
				<dash_offset>0</dash_offset>
				<sequence>4</sequence>
			</hash_100101777aa88fb0a79b60d081e0e3759f1cf7>
			<hash_100101de265acbbfa99eb4b3e9f7e90c7feeda>
				<graph_type_id>9</graph_type_id>
				<task_item_id>hash_0801012df25c57022b0c7e7d0be4c035ada1a0</task_item_id>
				<color_id>0</color_id>
				<alpha>FF</alpha>
				<consolidation_function_id>3</consolidation_function_id>
				<cdef_id>0</cdef_id>
				<vdef_id>0</vdef_id>
				<shift></shift>
				<value></value>
				<gprint_id>hash_060101e9c43831e54eca8069317a2ce8c6f751</gprint_id>
				<textalign></textalign>
				<text_format>Maximum:</text_format>
				<hard_return></hard_return>
				<line_width>0.00</line_width>
				<dashes></dashes>
				<dash_offset>0</dash_offset>
				<sequence>5</sequence>
			</hash_100101de265acbbfa99eb4b3e9f7e90c7feeda>
			<hash_10010176ae747365553a02313a2d8a0dd55c8a>
				<graph_type_id>1</graph_type_id>
				<task_item_id>hash_0801012df25c57022b0c7e7d0be4c035ada1a0</task_item_id>
				<color_id>0</color_id>
				<alpha>FF</alpha>
				<consolidation_function_id>1</consolidation_function_id>
				<cdef_id>0</cdef_id>
				<vdef_id>0</vdef_id>
				<shift></shift>
				<value></value>
				<gprint_id>hash_060101e9c43831e54eca8069317a2ce8c6f751</gprint_id>
				<textalign></textalign>
				<text_format>Total In:  |sum:auto:current:2:auto|</text_format>
				<hard_return>on</hard_return>
				<line_width>0.00</line_width>
				<dashes></dashes>
				<dash_offset>0</dash_offset>
				<sequence>6</sequence>
			</hash_10010176ae747365553a02313a2d8a0dd55c8a>
			<hash_10010143a2cef12147952c703fc0fc473dec7a>
				<graph_type_id>4</graph_type_id>
				<task_item_id>hash_080101721c0794526d1ac1c359f27dc56faa49</task_item_id>
				<color_id>002A97</color_id>
				<alpha>FF</alpha>
				<consolidation_function_id>3</consolidation_function_id>
				<cdef_id>0</cdef_id>
				<vdef_id>0</vdef_id>
				<shift></shift>
				<value></value>
				<gprint_id>hash_060101e9c43831e54eca8069317a2ce8c6f751</gprint_id>
				<textalign></textalign>
				<text_format></text_format>
				<hard_return></hard_return>
				<line_width>1.00</line_width>
				<dashes></dashes>
				<dash_offset>0</dash_offset>
				<sequence>7</sequence>
			</hash_10010143a2cef12147952c703fc0fc473dec7a>
			<hash_100101cf8c9f69878f0f595d583eac109a9be1>
				<graph_type_id>7</graph_type_id>
				<task_item_id>hash_080101721c0794526d1ac1c359f27dc56faa49</task_item_id>
				<color_id>002A97</color_id>
				<alpha>7F</alpha>
				<consolidation_function_id>1</consolidation_function_id>
				<cdef_id>0</cdef_id>
				<vdef_id>0</vdef_id>
				<shift></shift>
				<value></value>
				<gprint_id>hash_060101e9c43831e54eca8069317a2ce8c6f751</gprint_id>
				<textalign></textalign>
				<text_format>Outbound</text_format>
				<hard_return></hard_return>
				<line_width>0.00</line_width>
				<dashes></dashes>
				<dash_offset>0</dash_offset>
				<sequence>8</sequence>
			</hash_100101cf8c9f69878f0f595d583eac109a9be1>
			<hash_10010154e3971b3dd751dd2509f62721c12b41>
				<graph_type_id>9</graph_type_id>
				<task_item_id>hash_080101721c0794526d1ac1c359f27dc56faa49</task_item_id>
				<color_id>0</color_id>
				<alpha>FF</alpha>
				<consolidation_function_id>4</consolidation_function_id>
				<cdef_id>0</cdef_id>
				<vdef_id>0</vdef_id>
				<shift></shift>
				<value></value>
				<gprint_id>hash_060101e9c43831e54eca8069317a2ce8c6f751</gprint_id>
				<textalign></textalign>
				<text_format>Current:</text_format>
				<hard_return></hard_return>
				<line_width>0.00</line_width>
				<dashes></dashes>
				<dash_offset>0</dash_offset>
				<sequence>9</sequence>
			</hash_10010154e3971b3dd751dd2509f62721c12b41>
			<hash_1001016824d29c3f13fe1e849f1dbb8377d3f1>
				<graph_type_id>9</graph_type_id>
				<task_item_id>hash_080101721c0794526d1ac1c359f27dc56faa49</task_item_id>
				<color_id>0</color_id>
				<alpha>FF</alpha>
				<consolidation_function_id>1</consolidation_function_id>
				<cdef_id>0</cdef_id>
				<vdef_id>0</vdef_id>
				<shift></shift>
				<value></value>
				<gprint_id>hash_060101e9c43831e54eca8069317a2ce8c6f751</gprint_id>
				<textalign></textalign>
				<text_format>Average:</text_format>
				<hard_return></hard_return>
				<line_width>0.00</line_width>
				<dashes></dashes>
				<dash_offset>0</dash_offset>
				<sequence>10</sequence>
			</hash_1001016824d29c3f13fe1e849f1dbb8377d3f1>
			<hash_100101fdaec5b9227522c758ad55882c483a83>
				<graph_type_id>9</graph_type_id>
				<task_item_id>hash_080101721c0794526d1ac1c359f27dc56faa49</task_item_id>
				<color_id>0</color_id>
				<alpha>FF</alpha>
				<consolidation_function_id>3</consolidation_function_id>
				<cdef_id>0</cdef_id>
				<vdef_id>0</vdef_id>
				<shift></shift>
				<value></value>
				<gprint_id>hash_060101e9c43831e54eca8069317a2ce8c6f751</gprint_id>
				<textalign></textalign>
				<text_format>Maximum:</text_format>
				<hard_return></hard_return>
				<line_width>0.00</line_width>
				<dashes></dashes>
				<dash_offset>0</dash_offset>
				<sequence>11</sequence>
			</hash_100101fdaec5b9227522c758ad55882c483a83>
			<hash_100101d6041d14f9c8fb9b7ddcf3556f763c03>
				<graph_type_id>1</graph_type_id>
				<task_item_id>hash_080101721c0794526d1ac1c359f27dc56faa49</task_item_id>
				<color_id>0</color_id>
				<alpha>FF</alpha>
				<consolidation_function_id>1</consolidation_function_id>
				<cdef_id>0</cdef_id>
				<vdef_id>0</vdef_id>
				<shift></shift>
				<value></value>
				<gprint_id>hash_060101e9c43831e54eca8069317a2ce8c6f751</gprint_id>
				<textalign></textalign>
				<text_format>Total Out: |sum:auto:current:2:auto|</text_format>
				<hard_return>on</hard_return>
				<line_width>0.00</line_width>
				<dashes></dashes>
				<dash_offset>0</dash_offset>
				<sequence>12</sequence>
			</hash_100101d6041d14f9c8fb9b7ddcf3556f763c03>
		</items>
		<inputs>
			<hash_0901018644b933b6a09dde6c32ff24655eeb9a>
				<name>Outbound Data Source</name>
				<description></description>
				<column_name>task_item_id</column_name>
				<items>hash_00010143a2cef12147952c703fc0fc473dec7a|hash_000101cf8c9f69878f0f595d583eac109a9be1|hash_00010154e3971b3dd751dd2509f62721c12b41|hash_0001016824d29c3f13fe1e849f1dbb8377d3f1|hash_000101fdaec5b9227522c758ad55882c483a83|hash_000101d6041d14f9c8fb9b7ddcf3556f763c03</items>
			</hash_0901018644b933b6a09dde6c32ff24655eeb9a>
			<hash_09010149c4b4800f3e638a6f6bb681919aea80>
				<name>Inbound Data Source</name>
				<description></description>
				<column_name>task_item_id</column_name>
				<items>hash_0001013baa47b136f8c36ccea69196b0285a6c|hash_0001013ff8dba1ca6279692b3fcabed0bc2631|hash_00010166bfdb701c8eeadffe55e926d6e77e71|hash_000101777aa88fb0a79b60d081e0e3759f1cf7|hash_000101de265acbbfa99eb4b3e9f7e90c7feeda|hash_00010176ae747365553a02313a2d8a0dd55c8a</items>
			</hash_09010149c4b4800f3e638a6f6bb681919aea80>
		</inputs>
	</hash_0001018ad6790c22b693680e041f21d62537ac>
	<hash_000101d4dff05337bbf42c70cb6f73647d0d2a>
		<name>Interface - Multicast Packets (Legacy)</name>
		<graph>
			<t_title>on</t_title>
			<title>|host_description| - Multicast Packets</title>
			<t_vertical_label></t_vertical_label>
			<vertical_label>packets/sec</vertical_label>
			<t_image_format_id></t_image_format_id>
			<image_format_id>1</image_format_id>
			<t_height></t_height>
			<height>200</height>
			<t_width></t_width>
			<width>700</width>
			<t_base_value></t_base_value>
			<base_value>1000</base_value>
			<t_slope_mode></t_slope_mode>
			<slope_mode>on</slope_mode>
			<t_auto_scale></t_auto_scale>
			<auto_scale>on</auto_scale>
			<t_auto_scale_opts></t_auto_scale_opts>
			<auto_scale_opts>2</auto_scale_opts>
			<t_auto_scale_log></t_auto_scale_log>
			<auto_scale_log></auto_scale_log>
			<t_scale_log_units></t_scale_log_units>
			<scale_log_units></scale_log_units>
			<t_auto_scale_rigid></t_auto_scale_rigid>
			<auto_scale_rigid>on</auto_scale_rigid>
			<t_upper_limit></t_upper_limit>
			<upper_limit>100</upper_limit>
			<t_lower_limit></t_lower_limit>
			<lower_limit>0</lower_limit>
			<t_unit_value></t_unit_value>
			<unit_value></unit_value>
			<t_unit_exponent_value></t_unit_exponent_value>
			<unit_exponent_value></unit_exponent_value>
			<t_unit_length></t_unit_length>
			<unit_length></unit_length>
			<t_no_gridfit></t_no_gridfit>
			<no_gridfit></no_gridfit>
			<t_alt_y_grid></t_alt_y_grid>
			<alt_y_grid></alt_y_grid>
			<t_right_axis></t_right_axis>
			<right_axis></right_axis>
			<t_right_axis_label></t_right_axis_label>
			<right_axis_label></right_axis_label>
			<t_right_axis_format></t_right_axis_format>
			<right_axis_format>0</right_axis_format>
			<t_right_axis_formatter></t_right_axis_formatter>
			<right_axis_formatter>0</right_axis_formatter>
			<t_left_axis_formatter></t_left_axis_formatter>
			<left_axis_formatter>0</left_axis_formatter>
			<t_auto_padding></t_auto_padding>
			<auto_padding>on</auto_padding>
			<t_dynamic_labels></t_dynamic_labels>
			<dynamic_labels></dynamic_labels>
			<t_force_rules_legend></t_force_rules_legend>
			<force_rules_legend></force_rules_legend>
			<t_tab_width></t_tab_width>
			<tab_width></tab_width>
			<t_legend_position></t_legend_position>
			<legend_position>0</legend_position>
			<t_legend_direction></t_legend_direction>
			<legend_direction>0</legend_direction>
		</graph>
		<items>
			<hash_10010134a594c6b419427329b10f73f40e85f7>
				<graph_type_id>7</graph_type_id>
				<task_item_id>hash_080101636672962b5bb2f31d86985e2ab4bdfe</task_item_id>
				<color_id>FFF200</color_id>
				<alpha>7F</alpha>
				<consolidation_function_id>1</consolidation_function_id>
				<cdef_id>0</cdef_id>
				<vdef_id>0</vdef_id>
				<shift></shift>
				<value></value>
				<gprint_id>hash_060101e9c43831e54eca8069317a2ce8c6f751</gprint_id>
				<textalign></textalign>
				<text_format>Multicast Packets In</text_format>
				<hard_return></hard_return>
				<line_width>0.00</line_width>
				<dashes></dashes>
				<dash_offset>0</dash_offset>
				<sequence>1</sequence>
			</hash_10010134a594c6b419427329b10f73f40e85f7>
			<hash_1001011540d561f6ab4b55ac810661fb0c93ee>
				<graph_type_id>9</graph_type_id>
				<task_item_id>hash_080101636672962b5bb2f31d86985e2ab4bdfe</task_item_id>
				<color_id>0</color_id>
				<alpha>FF</alpha>
				<consolidation_function_id>4</consolidation_function_id>
				<cdef_id>0</cdef_id>
				<vdef_id>0</vdef_id>
				<shift></shift>
				<value></value>
				<gprint_id>hash_060101e9c43831e54eca8069317a2ce8c6f751</gprint_id>
				<textalign></textalign>
				<text_format>Current:</text_format>
				<hard_return></hard_return>
				<line_width>0.00</line_width>
				<dashes></dashes>
				<dash_offset>0</dash_offset>
				<sequence>2</sequence>
			</hash_1001011540d561f6ab4b55ac810661fb0c93ee>
			<hash_100101e9e41de3845454688f838662e4c34aa7>
				<graph_type_id>9</graph_type_id>
				<task_item_id>hash_080101636672962b5bb2f31d86985e2ab4bdfe</task_item_id>
				<color_id>0</color_id>
				<alpha>FF</alpha>
				<consolidation_function_id>1</consolidation_function_id>
				<cdef_id>0</cdef_id>
				<vdef_id>0</vdef_id>
				<shift></shift>
				<value></value>
				<gprint_id>hash_060101e9c43831e54eca8069317a2ce8c6f751</gprint_id>
				<textalign></textalign>
				<text_format>Average:</text_format>
				<hard_return></hard_return>
				<line_width>0.00</line_width>
				<dashes></dashes>
				<dash_offset>0</dash_offset>
				<sequence>3</sequence>
			</hash_100101e9e41de3845454688f838662e4c34aa7>
			<hash_100101350ebb1cd31fb46d9997bc21a00d36b1>
				<graph_type_id>9</graph_type_id>
				<task_item_id>hash_080101636672962b5bb2f31d86985e2ab4bdfe</task_item_id>
				<color_id>0</color_id>
				<alpha>FF</alpha>
				<consolidation_function_id>3</consolidation_function_id>
				<cdef_id>0</cdef_id>
				<vdef_id>0</vdef_id>
				<shift></shift>
				<value></value>
				<gprint_id>hash_060101e9c43831e54eca8069317a2ce8c6f751</gprint_id>
				<textalign></textalign>
				<text_format>Maximum:</text_format>
				<hard_return>on</hard_return>
				<line_width>0.00</line_width>
				<dashes></dashes>
				<dash_offset>0</dash_offset>
				<sequence>4</sequence>
			</hash_100101350ebb1cd31fb46d9997bc21a00d36b1>
			<hash_10010116f958e2b047113d38c7550c76ef04c8>
				<graph_type_id>7</graph_type_id>
				<task_item_id>hash_08010118ce92c125a236a190ee9dd948f56268</task_item_id>
				<color_id>00234B</color_id>
				<alpha>7F</alpha>
				<consolidation_function_id>1</consolidation_function_id>
				<cdef_id>0</cdef_id>
				<vdef_id>0</vdef_id>
				<shift></shift>
				<value></value>
				<gprint_id>hash_060101e9c43831e54eca8069317a2ce8c6f751</gprint_id>
				<textalign></textalign>
				<text_format>Multicast Packets Out</text_format>
				<hard_return></hard_return>
				<line_width>0.00</line_width>
				<dashes></dashes>
				<dash_offset>0</dash_offset>
				<sequence>5</sequence>
			</hash_10010116f958e2b047113d38c7550c76ef04c8>
			<hash_100101a393430c1db0d9da48dca3098022cf50>
				<graph_type_id>9</graph_type_id>
				<task_item_id>hash_08010118ce92c125a236a190ee9dd948f56268</task_item_id>
				<color_id>0</color_id>
				<alpha>FF</alpha>
				<consolidation_function_id>4</consolidation_function_id>
				<cdef_id>0</cdef_id>
				<vdef_id>0</vdef_id>
				<shift></shift>
				<value></value>
				<gprint_id>hash_060101e9c43831e54eca8069317a2ce8c6f751</gprint_id>
				<textalign></textalign>
				<text_format>Current:</text_format>
				<hard_return></hard_return>
				<line_width>0.00</line_width>
				<dashes></dashes>
				<dash_offset>0</dash_offset>
				<sequence>6</sequence>
			</hash_100101a393430c1db0d9da48dca3098022cf50>
			<hash_1001013f73834149d86814a4dbbfa4052fdb14>
				<graph_type_id>9</graph_type_id>
				<task_item_id>hash_08010118ce92c125a236a190ee9dd948f56268</task_item_id>
				<color_id>0</color_id>
				<alpha>FF</alpha>
				<consolidation_function_id>1</consolidation_function_id>
				<cdef_id>0</cdef_id>
				<vdef_id>0</vdef_id>
				<shift></shift>
				<value></value>
				<gprint_id>hash_060101e9c43831e54eca8069317a2ce8c6f751</gprint_id>
				<textalign></textalign>
				<text_format>Average:</text_format>
				<hard_return></hard_return>
				<line_width>0.00</line_width>
				<dashes></dashes>
				<dash_offset>0</dash_offset>
				<sequence>7</sequence>
			</hash_1001013f73834149d86814a4dbbfa4052fdb14>
			<hash_10010107164e2d5ebe685b622a97250dab9cc2>
				<graph_type_id>9</graph_type_id>
				<task_item_id>hash_08010118ce92c125a236a190ee9dd948f56268</task_item_id>
				<color_id>0</color_id>
				<alpha>FF</alpha>
				<consolidation_function_id>3</consolidation_function_id>
				<cdef_id>0</cdef_id>
				<vdef_id>0</vdef_id>
				<shift></shift>
				<value></value>
				<gprint_id>hash_060101e9c43831e54eca8069317a2ce8c6f751</gprint_id>
				<textalign></textalign>
				<text_format>Maximum:</text_format>
				<hard_return>on</hard_return>
				<line_width>0.00</line_width>
				<dashes></dashes>
				<dash_offset>0</dash_offset>
				<sequence>8</sequence>
			</hash_10010107164e2d5ebe685b622a97250dab9cc2>
			<hash_1001012a19f1c71b1ff8edea69af3f1825cec0>
				<graph_type_id>4</graph_type_id>
				<task_item_id>hash_080101636672962b5bb2f31d86985e2ab4bdfe</task_item_id>
				<color_id>FFF200</color_id>
				<alpha>FF</alpha>
				<consolidation_function_id>3</consolidation_function_id>
				<cdef_id>0</cdef_id>
				<vdef_id>0</vdef_id>
				<shift></shift>
				<value></value>
				<gprint_id>hash_060101e9c43831e54eca8069317a2ce8c6f751</gprint_id>
				<textalign></textalign>
				<text_format></text_format>
				<hard_return></hard_return>
				<line_width>1.00</line_width>
				<dashes></dashes>
				<dash_offset>0</dash_offset>
				<sequence>9</sequence>
			</hash_1001012a19f1c71b1ff8edea69af3f1825cec0>
			<hash_100101e9625f33db3635e39e206334da9f99ef>
				<graph_type_id>4</graph_type_id>
				<task_item_id>hash_08010118ce92c125a236a190ee9dd948f56268</task_item_id>
				<color_id>00234B</color_id>
				<alpha>FF</alpha>
				<consolidation_function_id>3</consolidation_function_id>
				<cdef_id>0</cdef_id>
				<vdef_id>0</vdef_id>
				<shift></shift>
				<value></value>
				<gprint_id>hash_060101e9c43831e54eca8069317a2ce8c6f751</gprint_id>
				<textalign></textalign>
				<text_format></text_format>
				<hard_return></hard_return>
				<line_width>1.00</line_width>
				<dashes></dashes>
				<dash_offset>0</dash_offset>
				<sequence>10</sequence>
			</hash_100101e9625f33db3635e39e206334da9f99ef>
		</items>
		<inputs>
			<hash_090101a29d473b1bbc98a1c032237622ea0837>
				<name>Multicast Packets Out Data Source</name>
				<description></description>
				<column_name>task_item_id</column_name>
				<items>hash_00010116f958e2b047113d38c7550c76ef04c8|hash_000101a393430c1db0d9da48dca3098022cf50|hash_0001013f73834149d86814a4dbbfa4052fdb14|hash_00010107164e2d5ebe685b622a97250dab9cc2|hash_000101e9625f33db3635e39e206334da9f99ef</items>
			</hash_090101a29d473b1bbc98a1c032237622ea0837>
			<hash_090101cc896ba8b616aa6a66a1ba1ce802e68e>
				<name>Multicast Packets In Data Source</name>
				<description></description>
				<column_name>task_item_id</column_name>
				<items>hash_00010134a594c6b419427329b10f73f40e85f7|hash_0001011540d561f6ab4b55ac810661fb0c93ee|hash_000101e9e41de3845454688f838662e4c34aa7|hash_000101350ebb1cd31fb46d9997bc21a00d36b1|hash_0001012a19f1c71b1ff8edea69af3f1825cec0</items>
			</hash_090101cc896ba8b616aa6a66a1ba1ce802e68e>
		</inputs>
	</hash_000101d4dff05337bbf42c70cb6f73647d0d2a>
	<hash_000101ed3f434a9ebd2f23ab9bc173d608b3d7>
		<name>Interface - Broadcast Packets (Legacy)</name>
		<graph>
			<t_title>on</t_title>
			<title>|host_description| - Broadcast Packets</title>
			<t_vertical_label></t_vertical_label>
			<vertical_label>packets/sec</vertical_label>
			<t_image_format_id></t_image_format_id>
			<image_format_id>1</image_format_id>
			<t_height></t_height>
			<height>200</height>
			<t_width></t_width>
			<width>700</width>
			<t_base_value></t_base_value>
			<base_value>1000</base_value>
			<t_slope_mode></t_slope_mode>
			<slope_mode>on</slope_mode>
			<t_auto_scale></t_auto_scale>
			<auto_scale>on</auto_scale>
			<t_auto_scale_opts></t_auto_scale_opts>
			<auto_scale_opts>2</auto_scale_opts>
			<t_auto_scale_log></t_auto_scale_log>
			<auto_scale_log></auto_scale_log>
			<t_scale_log_units></t_scale_log_units>
			<scale_log_units></scale_log_units>
			<t_auto_scale_rigid></t_auto_scale_rigid>
			<auto_scale_rigid>on</auto_scale_rigid>
			<t_upper_limit></t_upper_limit>
			<upper_limit>100</upper_limit>
			<t_lower_limit></t_lower_limit>
			<lower_limit>0</lower_limit>
			<t_unit_value></t_unit_value>
			<unit_value></unit_value>
			<t_unit_exponent_value></t_unit_exponent_value>
			<unit_exponent_value></unit_exponent_value>
			<t_unit_length></t_unit_length>
			<unit_length></unit_length>
			<t_no_gridfit></t_no_gridfit>
			<no_gridfit></no_gridfit>
			<t_alt_y_grid></t_alt_y_grid>
			<alt_y_grid></alt_y_grid>
			<t_right_axis></t_right_axis>
			<right_axis></right_axis>
			<t_right_axis_label></t_right_axis_label>
			<right_axis_label></right_axis_label>
			<t_right_axis_format></t_right_axis_format>
			<right_axis_format>0</right_axis_format>
			<t_right_axis_formatter></t_right_axis_formatter>
			<right_axis_formatter>0</right_axis_formatter>
			<t_left_axis_formatter></t_left_axis_formatter>
			<left_axis_formatter>0</left_axis_formatter>
			<t_auto_padding></t_auto_padding>
			<auto_padding>on</auto_padding>
			<t_dynamic_labels></t_dynamic_labels>
			<dynamic_labels></dynamic_labels>
			<t_force_rules_legend></t_force_rules_legend>
			<force_rules_legend></force_rules_legend>
			<t_tab_width></t_tab_width>
			<tab_width></tab_width>
			<t_legend_position></t_legend_position>
			<legend_position>0</legend_position>
			<t_legend_direction></t_legend_direction>
			<legend_direction>0</legend_direction>
		</graph>
		<items>
			<hash_100101ea54bfaa4bad2b6862165840418f5fd4>
				<graph_type_id>7</graph_type_id>
				<task_item_id>hash_08010193e2b6f59b10b13f2ddf2da3ae98b89a</task_item_id>
				<color_id>FFF200</color_id>
				<alpha>7F</alpha>
				<consolidation_function_id>1</consolidation_function_id>
				<cdef_id>0</cdef_id>
				<vdef_id>0</vdef_id>
				<shift></shift>
				<value></value>
				<gprint_id>hash_060101e9c43831e54eca8069317a2ce8c6f751</gprint_id>
				<textalign></textalign>
				<text_format>Broadcast Packets In</text_format>
				<hard_return></hard_return>
				<line_width>0.00</line_width>
				<dashes></dashes>
				<dash_offset>0</dash_offset>
				<sequence>1</sequence>
			</hash_100101ea54bfaa4bad2b6862165840418f5fd4>
			<hash_100101a2508ab1f57dff7b143433ab81ff7a3e>
				<graph_type_id>9</graph_type_id>
				<task_item_id>hash_08010193e2b6f59b10b13f2ddf2da3ae98b89a</task_item_id>
				<color_id>0</color_id>
				<alpha>FF</alpha>
				<consolidation_function_id>4</consolidation_function_id>
				<cdef_id>0</cdef_id>
				<vdef_id>0</vdef_id>
				<shift></shift>
				<value></value>
				<gprint_id>hash_060101e9c43831e54eca8069317a2ce8c6f751</gprint_id>
				<textalign></textalign>
				<text_format>Current:</text_format>
				<hard_return></hard_return>
				<line_width>0.00</line_width>
				<dashes></dashes>
				<dash_offset>0</dash_offset>
				<sequence>2</sequence>
			</hash_100101a2508ab1f57dff7b143433ab81ff7a3e>
			<hash_100101cab434df67b94a93728ab794b1d0f6fb>
				<graph_type_id>9</graph_type_id>
				<task_item_id>hash_08010193e2b6f59b10b13f2ddf2da3ae98b89a</task_item_id>
				<color_id>0</color_id>
				<alpha>FF</alpha>
				<consolidation_function_id>1</consolidation_function_id>
				<cdef_id>0</cdef_id>
				<vdef_id>0</vdef_id>
				<shift></shift>
				<value></value>
				<gprint_id>hash_060101e9c43831e54eca8069317a2ce8c6f751</gprint_id>
				<textalign></textalign>
				<text_format>Average:</text_format>
				<hard_return></hard_return>
				<line_width>0.00</line_width>
				<dashes></dashes>
				<dash_offset>0</dash_offset>
				<sequence>3</sequence>
			</hash_100101cab434df67b94a93728ab794b1d0f6fb>
			<hash_10010129d51e734ad14bcdb3a9b7a640f2c4a3>
				<graph_type_id>9</graph_type_id>
				<task_item_id>hash_08010193e2b6f59b10b13f2ddf2da3ae98b89a</task_item_id>
				<color_id>0</color_id>
				<alpha>FF</alpha>
				<consolidation_function_id>3</consolidation_function_id>
				<cdef_id>0</cdef_id>
				<vdef_id>0</vdef_id>
				<shift></shift>
				<value></value>
				<gprint_id>hash_060101e9c43831e54eca8069317a2ce8c6f751</gprint_id>
				<textalign></textalign>
				<text_format>Maximum:</text_format>
				<hard_return>on</hard_return>
				<line_width>0.00</line_width>
				<dashes></dashes>
				<dash_offset>0</dash_offset>
				<sequence>4</sequence>
			</hash_10010129d51e734ad14bcdb3a9b7a640f2c4a3>
			<hash_100101725d97e3666c2417241ca7bb67a8c902>
				<graph_type_id>7</graph_type_id>
				<task_item_id>hash_0801017be68cbc4ee0b2973eb9785f8c7a35c7</task_item_id>
				<color_id>00234B</color_id>
				<alpha>7F</alpha>
				<consolidation_function_id>1</consolidation_function_id>
				<cdef_id>0</cdef_id>
				<vdef_id>0</vdef_id>
				<shift></shift>
				<value></value>
				<gprint_id>hash_060101e9c43831e54eca8069317a2ce8c6f751</gprint_id>
				<textalign></textalign>
				<text_format>Broadcast Packets Out</text_format>
				<hard_return></hard_return>
				<line_width>0.00</line_width>
				<dashes></dashes>
				<dash_offset>0</dash_offset>
				<sequence>5</sequence>
			</hash_100101725d97e3666c2417241ca7bb67a8c902>
			<hash_100101b01f45a155e10f49d640d13b50aa61a5>
				<graph_type_id>9</graph_type_id>
				<task_item_id>hash_0801017be68cbc4ee0b2973eb9785f8c7a35c7</task_item_id>
				<color_id>0</color_id>
				<alpha>FF</alpha>
				<consolidation_function_id>4</consolidation_function_id>
				<cdef_id>0</cdef_id>
				<vdef_id>0</vdef_id>
				<shift></shift>
				<value></value>
				<gprint_id>hash_060101e9c43831e54eca8069317a2ce8c6f751</gprint_id>
				<textalign></textalign>
				<text_format>Current:</text_format>
				<hard_return></hard_return>
				<line_width>0.00</line_width>
				<dashes></dashes>
				<dash_offset>0</dash_offset>
				<sequence>6</sequence>
			</hash_100101b01f45a155e10f49d640d13b50aa61a5>
			<hash_100101eb37825efbb281484cdb1e896764b73a>
				<graph_type_id>9</graph_type_id>
				<task_item_id>hash_0801017be68cbc4ee0b2973eb9785f8c7a35c7</task_item_id>
				<color_id>0</color_id>
				<alpha>FF</alpha>
				<consolidation_function_id>1</consolidation_function_id>
				<cdef_id>0</cdef_id>
				<vdef_id>0</vdef_id>
				<shift></shift>
				<value></value>
				<gprint_id>hash_060101e9c43831e54eca8069317a2ce8c6f751</gprint_id>
				<textalign></textalign>
				<text_format>Average:</text_format>
				<hard_return></hard_return>
				<line_width>0.00</line_width>
				<dashes></dashes>
				<dash_offset>0</dash_offset>
				<sequence>7</sequence>
			</hash_100101eb37825efbb281484cdb1e896764b73a>
			<hash_100101b18b67ef2779d5ff43843cac220d9bb9>
				<graph_type_id>9</graph_type_id>
				<task_item_id>hash_0801017be68cbc4ee0b2973eb9785f8c7a35c7</task_item_id>
				<color_id>0</color_id>
				<alpha>FF</alpha>
				<consolidation_function_id>3</consolidation_function_id>
				<cdef_id>0</cdef_id>
				<vdef_id>0</vdef_id>
				<shift></shift>
				<value></value>
				<gprint_id>hash_060101e9c43831e54eca8069317a2ce8c6f751</gprint_id>
				<textalign></textalign>
				<text_format>Maximum:</text_format>
				<hard_return>on</hard_return>
				<line_width>0.00</line_width>
				<dashes></dashes>
				<dash_offset>0</dash_offset>
				<sequence>8</sequence>
			</hash_100101b18b67ef2779d5ff43843cac220d9bb9>
			<hash_10010156ea543140aa516299ba202b313fc822>
				<graph_type_id>4</graph_type_id>
				<task_item_id>hash_08010193e2b6f59b10b13f2ddf2da3ae98b89a</task_item_id>
				<color_id>FFF200</color_id>
				<alpha>FF</alpha>
				<consolidation_function_id>3</consolidation_function_id>
				<cdef_id>0</cdef_id>
				<vdef_id>0</vdef_id>
				<shift></shift>
				<value></value>
				<gprint_id>hash_060101e9c43831e54eca8069317a2ce8c6f751</gprint_id>
				<textalign></textalign>
				<text_format></text_format>
				<hard_return></hard_return>
				<line_width>1.00</line_width>
				<dashes></dashes>
				<dash_offset>0</dash_offset>
				<sequence>9</sequence>
			</hash_10010156ea543140aa516299ba202b313fc822>
			<hash_100101ce17bd1ed1efaa2f7eb2b1fef7354d8d>
				<graph_type_id>4</graph_type_id>
				<task_item_id>hash_0801017be68cbc4ee0b2973eb9785f8c7a35c7</task_item_id>
				<color_id>00234B</color_id>
				<alpha>FF</alpha>
				<consolidation_function_id>3</consolidation_function_id>
				<cdef_id>0</cdef_id>
				<vdef_id>0</vdef_id>
				<shift></shift>
				<value></value>
				<gprint_id>hash_060101e9c43831e54eca8069317a2ce8c6f751</gprint_id>
				<textalign></textalign>
				<text_format></text_format>
				<hard_return></hard_return>
				<line_width>1.00</line_width>
				<dashes></dashes>
				<dash_offset>0</dash_offset>
				<sequence>10</sequence>
			</hash_100101ce17bd1ed1efaa2f7eb2b1fef7354d8d>
		</items>
		<inputs>
			<hash_090101a5c3743e175afaa77f6fa1f452f72c32>
				<name>Non-Unicast Packets In Data Source</name>
				<description></description>
				<column_name>task_item_id</column_name>
				<items>hash_000101ea54bfaa4bad2b6862165840418f5fd4|hash_000101a2508ab1f57dff7b143433ab81ff7a3e|hash_000101cab434df67b94a93728ab794b1d0f6fb|hash_00010129d51e734ad14bcdb3a9b7a640f2c4a3|hash_00010156ea543140aa516299ba202b313fc822</items>
			</hash_090101a5c3743e175afaa77f6fa1f452f72c32>
			<hash_09010130e4a03de4ed9d772a0bbe93830b8b73>
				<name>Non-Unicast Packets Out Data Source</name>
				<description></description>
				<column_name>task_item_id</column_name>
				<items>hash_000101725d97e3666c2417241ca7bb67a8c902|hash_000101b01f45a155e10f49d640d13b50aa61a5|hash_000101eb37825efbb281484cdb1e896764b73a|hash_000101b18b67ef2779d5ff43843cac220d9bb9|hash_000101ce17bd1ed1efaa2f7eb2b1fef7354d8d</items>
			</hash_09010130e4a03de4ed9d772a0bbe93830b8b73>
		</inputs>
	</hash_000101ed3f434a9ebd2f23ab9bc173d608b3d7>
	<hash_010101e2e9bce1fc21d108dacce70a57a282ac>
		<name>Mikorotik SNMP Total CPU Load</name>
		<ds>
			<t_name></t_name>
			<name>|host_description| - MTK_CPU_LOAD</name>
			<data_source_path></data_source_path>
			<data_input_id>hash_0301013eb92bb845b9660a7445cf9740726522</data_input_id>
			<t_data_source_profile_id></t_data_source_profile_id>
			<data_source_profile_id>hash_200101d62c52891f4f9688729a5bc9fad91b18</data_source_profile_id>
			<t_rrd_step></t_rrd_step>
			<rrd_step>300</rrd_step>
			<t_active></t_active>
			<active>on</active>
		</ds>
		<items>
			<hash_080101a459834b76dcc310b0d96515948427c7>
				<t_data_source_name></t_data_source_name>
				<data_source_name>CPULOAD</data_source_name>
				<t_rrd_minimum></t_rrd_minimum>
				<rrd_minimum>0</rrd_minimum>
				<t_rrd_maximum></t_rrd_maximum>
				<rrd_maximum>100</rrd_maximum>
				<t_data_source_type_id></t_data_source_type_id>
				<data_source_type_id>1</data_source_type_id>
				<rrd_heartbeat>600</rrd_heartbeat>
				<t_data_input_field_id></t_data_input_field_id>
				<data_input_field_id>0</data_input_field_id>
			</hash_080101a459834b76dcc310b0d96515948427c7>
		</items>
		<data>
			<item_000>
				<data_input_field_id>hash_07010192f5906c8dc0f964b41f4253df582c38</data_input_field_id>
				<t_value></t_value>
				<value></value>
			</item_000>
			<item_001>
				<data_input_field_id>hash_07010132285d5bf16e56c478f5e83f32cda9ef</data_input_field_id>
				<t_value></t_value>
				<value></value>
			</item_001>
			<item_002>
				<data_input_field_id>hash_070101ad14ac90641aed388139f6ba86a2e48b</data_input_field_id>
				<t_value></t_value>
				<value></value>
			</item_002>
			<item_003>
				<data_input_field_id>hash_0701019c55a74bd571b4f00a96fd4b793278c6</data_input_field_id>
				<t_value></t_value>
				<value></value>
			</item_003>
			<item_004>
				<data_input_field_id>hash_070101012ccb1d3687d3edb29c002ea66e72da</data_input_field_id>
				<t_value></t_value>
				<value></value>
			</item_004>
			<item_005>
				<data_input_field_id>hash_0701014276a5ec6e3fe33995129041b1909762</data_input_field_id>
				<t_value></t_value>
				<value>1.3.6.1.4.1.2021.11.10.0</value>
			</item_005>
			<item_006>
				<data_input_field_id>hash_070101fc64b99742ec417cc424dbf8c7692d36</data_input_field_id>
				<t_value></t_value>
				<value></value>
			</item_006>
			<item_007>
				<data_input_field_id>hash_07010120832ce12f099c8e54140793a091af90</data_input_field_id>
				<t_value></t_value>
				<value></value>
			</item_007>
			<item_008>
				<data_input_field_id>hash_070101c60c9aac1e1b3555ea0620b8bbfd82cb</data_input_field_id>
				<t_value></t_value>
				<value></value>
			</item_008>
			<item_009>
				<data_input_field_id>hash_070101feda162701240101bc74148415ef415a</data_input_field_id>
				<t_value></t_value>
				<value></value>
			</item_009>
		</data>
	</hash_010101e2e9bce1fc21d108dacce70a57a282ac>
	<hash_0101011550426df5d1a523ea43447439f278a8>
		<name>Host MIB - Uptime</name>
		<ds>
			<t_name></t_name>
			<name>|host_description| - Uptime</name>
			<data_source_path></data_source_path>
			<data_input_id>hash_0301013eb92bb845b9660a7445cf9740726522</data_input_id>
			<t_data_source_profile_id></t_data_source_profile_id>
			<data_source_profile_id>hash_200101d62c52891f4f9688729a5bc9fad91b18</data_source_profile_id>
			<t_rrd_step></t_rrd_step>
			<rrd_step>300</rrd_step>
			<t_active></t_active>
			<active>on</active>
		</ds>
		<items>
			<hash_080101889a43e0b6feddaa482f0e3198529f4d>
				<t_data_source_name></t_data_source_name>
				<data_source_name>uptime</data_source_name>
				<t_rrd_minimum></t_rrd_minimum>
				<rrd_minimum>0</rrd_minimum>
				<t_rrd_maximum></t_rrd_maximum>
				<rrd_maximum>0</rrd_maximum>
				<t_data_source_type_id></t_data_source_type_id>
				<data_source_type_id>1</data_source_type_id>
				<t_rrd_heartbeat></t_rrd_heartbeat>
				<rrd_heartbeat>600</rrd_heartbeat>
				<t_data_input_field_id></t_data_input_field_id>
				<data_input_field_id>0</data_input_field_id>
			</hash_080101889a43e0b6feddaa482f0e3198529f4d>
		</items>
		<data>
			<item_000>
				<data_input_field_id>hash_07010192f5906c8dc0f964b41f4253df582c38</data_input_field_id>
				<t_value></t_value>
				<value></value>
			</item_000>
			<item_001>
				<data_input_field_id>hash_07010132285d5bf16e56c478f5e83f32cda9ef</data_input_field_id>
				<t_value></t_value>
				<value></value>
			</item_001>
			<item_002>
				<data_input_field_id>hash_070101ad14ac90641aed388139f6ba86a2e48b</data_input_field_id>
				<t_value></t_value>
				<value></value>
			</item_002>
			<item_003>
				<data_input_field_id>hash_0701019c55a74bd571b4f00a96fd4b793278c6</data_input_field_id>
				<t_value></t_value>
				<value></value>
			</item_003>
			<item_004>
				<data_input_field_id>hash_070101012ccb1d3687d3edb29c002ea66e72da</data_input_field_id>
				<t_value></t_value>
				<value></value>
			</item_004>
			<item_005>
				<data_input_field_id>hash_0701014276a5ec6e3fe33995129041b1909762</data_input_field_id>
				<t_value></t_value>
				<value>.1.3.6.1.2.1.1.3.0</value>
			</item_005>
			<item_006>
				<data_input_field_id>hash_070101fc64b99742ec417cc424dbf8c7692d36</data_input_field_id>
				<t_value></t_value>
				<value></value>
			</item_006>
			<item_007>
				<data_input_field_id>hash_07010120832ce12f099c8e54140793a091af90</data_input_field_id>
				<t_value></t_value>
				<value></value>
			</item_007>
			<item_008>
				<data_input_field_id>hash_070101c60c9aac1e1b3555ea0620b8bbfd82cb</data_input_field_id>
				<t_value></t_value>
				<value></value>
			</item_008>
			<item_009>
				<data_input_field_id>hash_070101feda162701240101bc74148415ef415a</data_input_field_id>
				<t_value></t_value>
				<value></value>
			</item_009>
		</data>
	</hash_0101011550426df5d1a523ea43447439f278a8>
	<hash_0101016632e1e0b58a565c135d7ff90440c335>
		<name>Interface - Traffic</name>
		<ds>
			<t_name>on</t_name>
			<name>|host_description| - Traffic</name>
			<data_source_path></data_source_path>
			<data_input_id>hash_030101bf566c869ac6443b0c75d1c32b5a350e</data_input_id>
			<t_data_source_profile_id></t_data_source_profile_id>
			<data_source_profile_id>hash_200101d62c52891f4f9688729a5bc9fad91b18</data_source_profile_id>
			<t_rrd_step></t_rrd_step>
			<rrd_step>300</rrd_step>
			<t_active></t_active>
			<active>on</active>
		</ds>
		<items>
			<hash_0801012df25c57022b0c7e7d0be4c035ada1a0>
				<t_data_source_name></t_data_source_name>
				<data_source_name>traffic_in</data_source_name>
				<t_rrd_minimum></t_rrd_minimum>
				<rrd_minimum>0</rrd_minimum>
				<t_rrd_maximum>on</t_rrd_maximum>
				<rrd_maximum>100000000</rrd_maximum>
				<t_data_source_type_id></t_data_source_type_id>
				<data_source_type_id>2</data_source_type_id>
				<t_rrd_heartbeat></t_rrd_heartbeat>
				<rrd_heartbeat>600</rrd_heartbeat>
				<t_data_input_field_id></t_data_input_field_id>
				<data_input_field_id>0</data_input_field_id>
			</hash_0801012df25c57022b0c7e7d0be4c035ada1a0>
			<hash_080101721c0794526d1ac1c359f27dc56faa49>
				<t_data_source_name></t_data_source_name>
				<data_source_name>traffic_out</data_source_name>
				<t_rrd_minimum></t_rrd_minimum>
				<rrd_minimum>0</rrd_minimum>
				<t_rrd_maximum>on</t_rrd_maximum>
				<rrd_maximum>100000000</rrd_maximum>
				<t_data_source_type_id></t_data_source_type_id>
				<data_source_type_id>2</data_source_type_id>
				<t_rrd_heartbeat></t_rrd_heartbeat>
				<rrd_heartbeat>600</rrd_heartbeat>
				<t_data_input_field_id></t_data_input_field_id>
				<data_input_field_id>0</data_input_field_id>
			</hash_080101721c0794526d1ac1c359f27dc56faa49>
		</items>
		<data>
			<item_000>
				<data_input_field_id>hash_070101617cdc8a230615e59f06f361ef6e7728</data_input_field_id>
				<t_value></t_value>
				<value></value>
			</item_000>
			<item_001>
				<data_input_field_id>hash_070101acb449d1451e8a2a655c2c99d31142c7</data_input_field_id>
				<t_value></t_value>
				<value></value>
			</item_001>
			<item_002>
				<data_input_field_id>hash_070101f4facc5e2ca7ebee621f09bc6d9fc792</data_input_field_id>
				<t_value></t_value>
				<value></value>
			</item_002>
			<item_003>
				<data_input_field_id>hash_0701011cc1493a6781af2c478fa4de971531cf</data_input_field_id>
				<t_value></t_value>
				<value></value>
			</item_003>
			<item_004>
				<data_input_field_id>hash_070101b5c23f246559df38662c255f4aa21d6b</data_input_field_id>
				<t_value></t_value>
				<value></value>
			</item_004>
			<item_005>
				<data_input_field_id>hash_0701016027a919c7c7731fbe095b6f53ab127b</data_input_field_id>
				<t_value>on</t_value>
				<value></value>
			</item_005>
			<item_006>
				<data_input_field_id>hash_070101cbbe5c1ddfb264a6e5d509ce1c78c95f</data_input_field_id>
				<t_value>on</t_value>
				<value></value>
			</item_006>
			<item_007>
				<data_input_field_id>hash_070101e6deda7be0f391399c5130e7c4a48b28</data_input_field_id>
				<t_value>on</t_value>
				<value></value>
			</item_007>
			<item_008>
				<data_input_field_id>hash_070101c1f36ee60c3dc98945556d57f26e475b</data_input_field_id>
				<t_value></t_value>
				<value></value>
			</item_008>
			<item_009>
				<data_input_field_id>hash_0701012cf7129ad3ff819a7a7ac189bee48ce8</data_input_field_id>
				<t_value></t_value>
				<value></value>
			</item_009>
			<item_010>
				<data_input_field_id>hash_0701016b13ac0a0194e171d241d4b06f913158</data_input_field_id>
				<t_value></t_value>
				<value></value>
			</item_010>
			<item_011>
				<data_input_field_id>hash_0701013a33d4fc65b8329ab2ac46a36da26b72</data_input_field_id>
				<t_value></t_value>
				<value></value>
			</item_011>
		</data>
	</hash_0101016632e1e0b58a565c135d7ff90440c335>
	<hash_01010136335cd98633963a575b70639cd2fdad>
		<name>Interface - Errors/Discards</name>
		<ds>
			<t_name>on</t_name>
			<name>|host_description| - Errors/Discards</name>
			<data_source_path></data_source_path>
			<data_input_id>hash_030101bf566c869ac6443b0c75d1c32b5a350e</data_input_id>
			<t_data_source_profile_id></t_data_source_profile_id>
			<data_source_profile_id>hash_200101d62c52891f4f9688729a5bc9fad91b18</data_source_profile_id>
			<t_rrd_step></t_rrd_step>
			<rrd_step>300</rrd_step>
			<t_active></t_active>
			<active>on</active>
		</ds>
		<items>
			<hash_080101c802e2fd77f5b0a4c4298951bf65957c>
				<t_data_source_name></t_data_source_name>
				<data_source_name>errors_in</data_source_name>
				<t_rrd_minimum></t_rrd_minimum>
				<rrd_minimum>0</rrd_minimum>
				<t_rrd_maximum></t_rrd_maximum>
				<rrd_maximum>10000000</rrd_maximum>
				<t_data_source_type_id></t_data_source_type_id>
				<data_source_type_id>2</data_source_type_id>
				<t_rrd_heartbeat></t_rrd_heartbeat>
				<rrd_heartbeat>600</rrd_heartbeat>
				<t_data_input_field_id></t_data_input_field_id>
				<data_input_field_id>0</data_input_field_id>
			</hash_080101c802e2fd77f5b0a4c4298951bf65957c>
			<hash_0801014e2a72240955380dc8ffacfcc8c09874>
				<t_data_source_name></t_data_source_name>
				<data_source_name>discards_in</data_source_name>
				<t_rrd_minimum></t_rrd_minimum>
				<rrd_minimum>0</rrd_minimum>
				<t_rrd_maximum></t_rrd_maximum>
				<rrd_maximum>10000000</rrd_maximum>
				<t_data_source_type_id></t_data_source_type_id>
				<data_source_type_id>2</data_source_type_id>
				<t_rrd_heartbeat></t_rrd_heartbeat>
				<rrd_heartbeat>600</rrd_heartbeat>
				<t_data_input_field_id></t_data_input_field_id>
				<data_input_field_id>0</data_input_field_id>
			</hash_0801014e2a72240955380dc8ffacfcc8c09874>
			<hash_08010113ebb33f9cbccfcba828db1075a8167c>
				<t_data_source_name></t_data_source_name>
				<data_source_name>discards_out</data_source_name>
				<t_rrd_minimum></t_rrd_minimum>
				<rrd_minimum>0</rrd_minimum>
				<t_rrd_maximum></t_rrd_maximum>
				<rrd_maximum>10000000</rrd_maximum>
				<t_data_source_type_id></t_data_source_type_id>
				<data_source_type_id>2</data_source_type_id>
				<t_rrd_heartbeat></t_rrd_heartbeat>
				<rrd_heartbeat>600</rrd_heartbeat>
				<t_data_input_field_id></t_data_input_field_id>
				<data_input_field_id>0</data_input_field_id>
			</hash_08010113ebb33f9cbccfcba828db1075a8167c>
			<hash_08010131399c3725bee7e09ec04049e3d5cd17>
				<t_data_source_name></t_data_source_name>
				<data_source_name>errors_out</data_source_name>
				<t_rrd_minimum></t_rrd_minimum>
				<rrd_minimum>0</rrd_minimum>
				<t_rrd_maximum></t_rrd_maximum>
				<rrd_maximum>10000000</rrd_maximum>
				<t_data_source_type_id></t_data_source_type_id>
				<data_source_type_id>2</data_source_type_id>
				<t_rrd_heartbeat></t_rrd_heartbeat>
				<rrd_heartbeat>600</rrd_heartbeat>
				<t_data_input_field_id></t_data_input_field_id>
				<data_input_field_id>0</data_input_field_id>
			</hash_08010131399c3725bee7e09ec04049e3d5cd17>
		</items>
		<data>
			<item_000>
				<data_input_field_id>hash_070101617cdc8a230615e59f06f361ef6e7728</data_input_field_id>
				<t_value></t_value>
				<value></value>
			</item_000>
			<item_001>
				<data_input_field_id>hash_070101acb449d1451e8a2a655c2c99d31142c7</data_input_field_id>
				<t_value></t_value>
				<value></value>
			</item_001>
			<item_002>
				<data_input_field_id>hash_070101f4facc5e2ca7ebee621f09bc6d9fc792</data_input_field_id>
				<t_value></t_value>
				<value></value>
			</item_002>
			<item_003>
				<data_input_field_id>hash_0701011cc1493a6781af2c478fa4de971531cf</data_input_field_id>
				<t_value></t_value>
				<value></value>
			</item_003>
			<item_004>
				<data_input_field_id>hash_070101b5c23f246559df38662c255f4aa21d6b</data_input_field_id>
				<t_value></t_value>
				<value></value>
			</item_004>
			<item_005>
				<data_input_field_id>hash_0701016027a919c7c7731fbe095b6f53ab127b</data_input_field_id>
				<t_value>on</t_value>
				<value></value>
			</item_005>
			<item_006>
				<data_input_field_id>hash_070101cbbe5c1ddfb264a6e5d509ce1c78c95f</data_input_field_id>
				<t_value>on</t_value>
				<value></value>
			</item_006>
			<item_007>
				<data_input_field_id>hash_070101e6deda7be0f391399c5130e7c4a48b28</data_input_field_id>
				<t_value>on</t_value>
				<value></value>
			</item_007>
			<item_008>
				<data_input_field_id>hash_070101c1f36ee60c3dc98945556d57f26e475b</data_input_field_id>
				<t_value></t_value>
				<value></value>
			</item_008>
		</data>
	</hash_01010136335cd98633963a575b70639cd2fdad>
	<hash_0101012f654f7d69ac71a5d56b1db8543ccad3>
		<name>Interface - Unicast Packets</name>
		<ds>
			<t_name>on</t_name>
			<name>|host_description| - Unicast Packets</name>
			<data_source_path></data_source_path>
			<data_input_id>hash_030101bf566c869ac6443b0c75d1c32b5a350e</data_input_id>
			<t_data_source_profile_id></t_data_source_profile_id>
			<data_source_profile_id>hash_200101d62c52891f4f9688729a5bc9fad91b18</data_source_profile_id>
			<t_rrd_step></t_rrd_step>
			<rrd_step>300</rrd_step>
			<t_active></t_active>
			<active>on</active>
		</ds>
		<items>
			<hash_080101636672962b5bb2f31d86985e2ab4bdfe>
				<t_data_source_name></t_data_source_name>
				<data_source_name>unicast_in</data_source_name>
				<t_rrd_minimum></t_rrd_minimum>
				<rrd_minimum>0</rrd_minimum>
				<t_rrd_maximum></t_rrd_maximum>
				<rrd_maximum>1000000000</rrd_maximum>
				<t_data_source_type_id></t_data_source_type_id>
				<data_source_type_id>2</data_source_type_id>
				<t_rrd_heartbeat></t_rrd_heartbeat>
				<rrd_heartbeat>600</rrd_heartbeat>
				<t_data_input_field_id></t_data_input_field_id>
				<data_input_field_id>0</data_input_field_id>
			</hash_080101636672962b5bb2f31d86985e2ab4bdfe>
			<hash_08010118ce92c125a236a190ee9dd948f56268>
				<t_data_source_name></t_data_source_name>
				<data_source_name>unicast_out</data_source_name>
				<t_rrd_minimum></t_rrd_minimum>
				<rrd_minimum>0</rrd_minimum>
				<t_rrd_maximum></t_rrd_maximum>
				<rrd_maximum>1000000000</rrd_maximum>
				<t_data_source_type_id></t_data_source_type_id>
				<data_source_type_id>2</data_source_type_id>
				<t_rrd_heartbeat></t_rrd_heartbeat>
				<rrd_heartbeat>600</rrd_heartbeat>
				<t_data_input_field_id></t_data_input_field_id>
				<data_input_field_id>0</data_input_field_id>
			</hash_08010118ce92c125a236a190ee9dd948f56268>
		</items>
		<data>
			<item_000>
				<data_input_field_id>hash_070101617cdc8a230615e59f06f361ef6e7728</data_input_field_id>
				<t_value></t_value>
				<value></value>
			</item_000>
			<item_001>
				<data_input_field_id>hash_070101acb449d1451e8a2a655c2c99d31142c7</data_input_field_id>
				<t_value></t_value>
				<value></value>
			</item_001>
			<item_002>
				<data_input_field_id>hash_070101f4facc5e2ca7ebee621f09bc6d9fc792</data_input_field_id>
				<t_value></t_value>
				<value></value>
			</item_002>
			<item_003>
				<data_input_field_id>hash_0701011cc1493a6781af2c478fa4de971531cf</data_input_field_id>
				<t_value></t_value>
				<value></value>
			</item_003>
			<item_004>
				<data_input_field_id>hash_070101b5c23f246559df38662c255f4aa21d6b</data_input_field_id>
				<t_value></t_value>
				<value></value>
			</item_004>
			<item_005>
				<data_input_field_id>hash_0701016027a919c7c7731fbe095b6f53ab127b</data_input_field_id>
				<t_value>on</t_value>
				<value></value>
			</item_005>
			<item_006>
				<data_input_field_id>hash_070101cbbe5c1ddfb264a6e5d509ce1c78c95f</data_input_field_id>
				<t_value>on</t_value>
				<value></value>
			</item_006>
			<item_007>
				<data_input_field_id>hash_070101e6deda7be0f391399c5130e7c4a48b28</data_input_field_id>
				<t_value>on</t_value>
				<value></value>
			</item_007>
			<item_008>
				<data_input_field_id>hash_070101c1f36ee60c3dc98945556d57f26e475b</data_input_field_id>
				<t_value></t_value>
				<value></value>
			</item_008>
		</data>
	</hash_0101012f654f7d69ac71a5d56b1db8543ccad3>
	<hash_010101c84e511401a747409053c90ba910d0fe>
		<name>Interface - Non-Unicast Packets</name>
		<ds>
			<t_name>on</t_name>
			<name>|host_description| - Non-Unicast Packets</name>
			<data_source_path></data_source_path>
			<data_input_id>hash_030101bf566c869ac6443b0c75d1c32b5a350e</data_input_id>
			<t_data_source_profile_id></t_data_source_profile_id>
			<data_source_profile_id>hash_200101d62c52891f4f9688729a5bc9fad91b18</data_source_profile_id>
			<t_rrd_step></t_rrd_step>
			<rrd_step>300</rrd_step>
			<t_active></t_active>
			<active>on</active>
		</ds>
		<items>
			<hash_0801017be68cbc4ee0b2973eb9785f8c7a35c7>
				<t_data_source_name></t_data_source_name>
				<data_source_name>nonunicast_out</data_source_name>
				<t_rrd_minimum></t_rrd_minimum>
				<rrd_minimum>0</rrd_minimum>
				<t_rrd_maximum></t_rrd_maximum>
				<rrd_maximum>1000000000</rrd_maximum>
				<t_data_source_type_id></t_data_source_type_id>
				<data_source_type_id>2</data_source_type_id>
				<t_rrd_heartbeat></t_rrd_heartbeat>
				<rrd_heartbeat>600</rrd_heartbeat>
				<t_data_input_field_id></t_data_input_field_id>
				<data_input_field_id>0</data_input_field_id>
			</hash_0801017be68cbc4ee0b2973eb9785f8c7a35c7>
			<hash_08010193e2b6f59b10b13f2ddf2da3ae98b89a>
				<t_data_source_name></t_data_source_name>
				<data_source_name>nonunicast_in</data_source_name>
				<t_rrd_minimum></t_rrd_minimum>
				<rrd_minimum>0</rrd_minimum>
				<t_rrd_maximum></t_rrd_maximum>
				<rrd_maximum>1000000000</rrd_maximum>
				<t_data_source_type_id></t_data_source_type_id>
				<data_source_type_id>2</data_source_type_id>
				<t_rrd_heartbeat></t_rrd_heartbeat>
				<rrd_heartbeat>600</rrd_heartbeat>
				<t_data_input_field_id></t_data_input_field_id>
				<data_input_field_id>0</data_input_field_id>
			</hash_08010193e2b6f59b10b13f2ddf2da3ae98b89a>
		</items>
		<data>
			<item_000>
				<data_input_field_id>hash_070101617cdc8a230615e59f06f361ef6e7728</data_input_field_id>
				<t_value></t_value>
				<value></value>
			</item_000>
			<item_001>
				<data_input_field_id>hash_070101acb449d1451e8a2a655c2c99d31142c7</data_input_field_id>
				<t_value></t_value>
				<value></value>
			</item_001>
			<item_002>
				<data_input_field_id>hash_070101f4facc5e2ca7ebee621f09bc6d9fc792</data_input_field_id>
				<t_value></t_value>
				<value></value>
			</item_002>
			<item_003>
				<data_input_field_id>hash_0701011cc1493a6781af2c478fa4de971531cf</data_input_field_id>
				<t_value></t_value>
				<value></value>
			</item_003>
			<item_004>
				<data_input_field_id>hash_070101b5c23f246559df38662c255f4aa21d6b</data_input_field_id>
				<t_value></t_value>
				<value></value>
			</item_004>
			<item_005>
				<data_input_field_id>hash_0701016027a919c7c7731fbe095b6f53ab127b</data_input_field_id>
				<t_value>on</t_value>
				<value></value>
			</item_005>
			<item_006>
				<data_input_field_id>hash_070101cbbe5c1ddfb264a6e5d509ce1c78c95f</data_input_field_id>
				<t_value>on</t_value>
				<value></value>
			</item_006>
			<item_007>
				<data_input_field_id>hash_070101e6deda7be0f391399c5130e7c4a48b28</data_input_field_id>
				<t_value>on</t_value>
				<value></value>
			</item_007>
			<item_008>
				<data_input_field_id>hash_070101c1f36ee60c3dc98945556d57f26e475b</data_input_field_id>
				<t_value></t_value>
				<value></value>
			</item_008>
		</data>
	</hash_010101c84e511401a747409053c90ba910d0fe>
	<hash_0301013eb92bb845b9660a7445cf9740726522>
		<name>Get SNMP Data</name>
		<type_id>2</type_id>
		<input_string></input_string>
		<fields>
			<hash_07010192f5906c8dc0f964b41f4253df582c38>
				<name>SNMP IP Address</name>
				<update_rra></update_rra>
				<regexp_match></regexp_match>
				<allow_nulls></allow_nulls>
				<type_code>hostname</type_code>
				<input_output>in</input_output>
				<data_name>management_ip</data_name>
			</hash_07010192f5906c8dc0f964b41f4253df582c38>
			<hash_07010132285d5bf16e56c478f5e83f32cda9ef>
				<name>SNMP Community</name>
				<update_rra></update_rra>
				<regexp_match></regexp_match>
				<allow_nulls></allow_nulls>
				<type_code>snmp_community</type_code>
				<input_output>in</input_output>
				<data_name>snmp_community</data_name>
			</hash_07010132285d5bf16e56c478f5e83f32cda9ef>
			<hash_070101ad14ac90641aed388139f6ba86a2e48b>
				<name>SNMP Username</name>
				<update_rra></update_rra>
				<regexp_match></regexp_match>
				<allow_nulls>on</allow_nulls>
				<type_code>snmp_username</type_code>
				<input_output>in</input_output>
				<data_name>snmp_username</data_name>
			</hash_070101ad14ac90641aed388139f6ba86a2e48b>
			<hash_0701019c55a74bd571b4f00a96fd4b793278c6>
				<name>SNMP Password</name>
				<update_rra></update_rra>
				<regexp_match></regexp_match>
				<allow_nulls>on</allow_nulls>
				<type_code>snmp_password</type_code>
				<input_output>in</input_output>
				<data_name>snmp_password</data_name>
			</hash_0701019c55a74bd571b4f00a96fd4b793278c6>
			<hash_070101012ccb1d3687d3edb29c002ea66e72da>
				<name>SNMP Version (1, 2, or 3)</name>
				<update_rra></update_rra>
				<regexp_match></regexp_match>
				<allow_nulls>on</allow_nulls>
				<type_code>snmp_version</type_code>
				<input_output>in</input_output>
				<data_name>snmp_version</data_name>
			</hash_070101012ccb1d3687d3edb29c002ea66e72da>
			<hash_0701014276a5ec6e3fe33995129041b1909762>
				<name>OID</name>
				<update_rra></update_rra>
				<regexp_match></regexp_match>
				<allow_nulls></allow_nulls>
				<type_code>snmp_oid</type_code>
				<input_output>in</input_output>
				<data_name>oid</data_name>
			</hash_0701014276a5ec6e3fe33995129041b1909762>
			<hash_070101fc64b99742ec417cc424dbf8c7692d36>
				<name>SNMP Port</name>
				<update_rra></update_rra>
				<regexp_match></regexp_match>
				<allow_nulls></allow_nulls>
				<type_code>snmp_port</type_code>
				<input_output>in</input_output>
				<data_name>snmp_port</data_name>
			</hash_070101fc64b99742ec417cc424dbf8c7692d36>
			<hash_07010120832ce12f099c8e54140793a091af90>
				<name>SNMP Authenticaion Protocol (v3)</name>
				<update_rra></update_rra>
				<regexp_match></regexp_match>
				<allow_nulls></allow_nulls>
				<type_code>snmp_auth_protocol</type_code>
				<input_output>in</input_output>
				<data_name>snmp_auth_protocol</data_name>
			</hash_07010120832ce12f099c8e54140793a091af90>
			<hash_070101c60c9aac1e1b3555ea0620b8bbfd82cb>
				<name>SNMP Privacy Passphrase (v3)</name>
				<update_rra></update_rra>
				<regexp_match></regexp_match>
				<allow_nulls></allow_nulls>
				<type_code>snmp_priv_passphrase</type_code>
				<input_output>in</input_output>
				<data_name>snmp_priv_passphrase</data_name>
			</hash_070101c60c9aac1e1b3555ea0620b8bbfd82cb>
			<hash_070101feda162701240101bc74148415ef415a>
				<name>SNMP Privacy Protocol (v3)</name>
				<update_rra></update_rra>
				<regexp_match></regexp_match>
				<allow_nulls></allow_nulls>
				<type_code>snmp_priv_protocol</type_code>
				<input_output>in</input_output>
				<data_name>snmp_priv_protocol</data_name>
			</hash_070101feda162701240101bc74148415ef415a>
		</fields>
	</hash_0301013eb92bb845b9660a7445cf9740726522>
	<hash_030101bf566c869ac6443b0c75d1c32b5a350e>
		<name>Get SNMP Data (Indexed)</name>
		<type_id>3</type_id>
		<input_string></input_string>
		<fields>
			<hash_070101617cdc8a230615e59f06f361ef6e7728>
				<name>SNMP IP Address</name>
				<update_rra></update_rra>
				<regexp_match></regexp_match>
				<allow_nulls></allow_nulls>
				<type_code>hostname</type_code>
				<input_output>in</input_output>
				<data_name>management_ip</data_name>
			</hash_070101617cdc8a230615e59f06f361ef6e7728>
			<hash_070101acb449d1451e8a2a655c2c99d31142c7>
				<name>SNMP Community</name>
				<update_rra></update_rra>
				<regexp_match></regexp_match>
				<allow_nulls></allow_nulls>
				<type_code>snmp_community</type_code>
				<input_output>in</input_output>
				<data_name>snmp_community</data_name>
			</hash_070101acb449d1451e8a2a655c2c99d31142c7>
			<hash_070101f4facc5e2ca7ebee621f09bc6d9fc792>
				<name>SNMP Username (v3)</name>
				<update_rra></update_rra>
				<regexp_match></regexp_match>
				<allow_nulls>on</allow_nulls>
				<type_code>snmp_username</type_code>
				<input_output>in</input_output>
				<data_name>snmp_username</data_name>
			</hash_070101f4facc5e2ca7ebee621f09bc6d9fc792>
			<hash_0701011cc1493a6781af2c478fa4de971531cf>
				<name>SNMP Password (v3)</name>
				<update_rra></update_rra>
				<regexp_match></regexp_match>
				<allow_nulls>on</allow_nulls>
				<type_code>snmp_password</type_code>
				<input_output>in</input_output>
				<data_name>snmp_password</data_name>
			</hash_0701011cc1493a6781af2c478fa4de971531cf>
			<hash_070101b5c23f246559df38662c255f4aa21d6b>
				<name>SNMP Version (1, 2, or 3)</name>
				<update_rra></update_rra>
				<regexp_match></regexp_match>
				<allow_nulls></allow_nulls>
				<type_code>snmp_version</type_code>
				<input_output>in</input_output>
				<data_name>snmp_version</data_name>
			</hash_070101b5c23f246559df38662c255f4aa21d6b>
			<hash_0701016027a919c7c7731fbe095b6f53ab127b>
				<name>Index Type</name>
				<update_rra></update_rra>
				<regexp_match></regexp_match>
				<allow_nulls></allow_nulls>
				<type_code>index_type</type_code>
				<input_output>in</input_output>
				<data_name>index_type</data_name>
			</hash_0701016027a919c7c7731fbe095b6f53ab127b>
			<hash_070101cbbe5c1ddfb264a6e5d509ce1c78c95f>
				<name>Index Value</name>
				<update_rra></update_rra>
				<regexp_match></regexp_match>
				<allow_nulls></allow_nulls>
				<type_code>index_value</type_code>
				<input_output>in</input_output>
				<data_name>index_value</data_name>
			</hash_070101cbbe5c1ddfb264a6e5d509ce1c78c95f>
			<hash_070101e6deda7be0f391399c5130e7c4a48b28>
				<name>Output Type ID</name>
				<update_rra></update_rra>
				<regexp_match></regexp_match>
				<allow_nulls></allow_nulls>
				<type_code>output_type</type_code>
				<input_output>in</input_output>
				<data_name>output_type</data_name>
			</hash_070101e6deda7be0f391399c5130e7c4a48b28>
			<hash_070101c1f36ee60c3dc98945556d57f26e475b>
				<name>SNMP Port</name>
				<update_rra></update_rra>
				<regexp_match></regexp_match>
				<allow_nulls></allow_nulls>
				<type_code>snmp_port</type_code>
				<input_output>in</input_output>
				<data_name>snmp_port</data_name>
			</hash_070101c1f36ee60c3dc98945556d57f26e475b>
			<hash_0701012cf7129ad3ff819a7a7ac189bee48ce8>
				<name>SNMP Authenticaion Protocol (v3)</name>
				<update_rra></update_rra>
				<regexp_match></regexp_match>
				<allow_nulls></allow_nulls>
				<type_code>snmp_auth_protocol</type_code>
				<input_output>in</input_output>
				<data_name>snmp_auth_protocol</data_name>
			</hash_0701012cf7129ad3ff819a7a7ac189bee48ce8>
			<hash_0701016b13ac0a0194e171d241d4b06f913158>
				<name>SNMP Privacy Passphrase (v3)</name>
				<update_rra></update_rra>
				<regexp_match></regexp_match>
				<allow_nulls></allow_nulls>
				<type_code>snmp_priv_passphrase</type_code>
				<input_output>in</input_output>
				<data_name>snmp_priv_passphrase</data_name>
			</hash_0701016b13ac0a0194e171d241d4b06f913158>
			<hash_0701013a33d4fc65b8329ab2ac46a36da26b72>
				<name>SNMP Privacy Protocol (v3)</name>
				<update_rra></update_rra>
				<regexp_match></regexp_match>
				<allow_nulls></allow_nulls>
				<type_code>snmp_priv_protocol</type_code>
				<input_output>in</input_output>
				<data_name>snmp_priv_protocol</data_name>
			</hash_0701013a33d4fc65b8329ab2ac46a36da26b72>
		</fields>
	</hash_030101bf566c869ac6443b0c75d1c32b5a350e>
	<hash_200101d62c52891f4f9688729a5bc9fad91b18>
		<name>System Default</name>
		<step>300</step>
		<heartbeat>600</heartbeat>
		<x_files_factor>0.5</x_files_factor>
		<default>on</default>
		<cf_items>1|2|3|4</cf_items>
		<items>
			<item_000>
				<name>Daily (5 Minute Average)</name>
				<steps>1</steps>
				<rows>600</rows>
				<timespan>86400</timespan>
			</item_000>
			<item_001>
				<name>Weekly (30 Minute Average)</name>
				<steps>6</steps>
				<rows>700</rows>
				<timespan>604800</timespan>
			</item_001>
			<item_002>
				<name>Monthly (2 Hour Average)</name>
				<steps>24</steps>
				<rows>775</rows>
				<timespan>2618784</timespan>
			</item_002>
			<item_003>
				<name>Yearly (1 Day Average)</name>
				<steps>288</steps>
				<rows>797</rows>
				<timespan>31536000</timespan>
			</item_003>
		</items>
	</hash_200101d62c52891f4f9688729a5bc9fad91b18>
	<hash_060101e9c43831e54eca8069317a2ce8c6f751>
		<name>Normal</name>
		<gprint_text>%8.2lf %s</gprint_text>
	</hash_060101e9c43831e54eca8069317a2ce8c6f751>
	<hash_06010119414480d6897c8731c7dc6c5310653e>
		<name>Exact Numbers</name>
		<gprint_text>%8.0lf</gprint_text>
	</hash_06010119414480d6897c8731c7dc6c5310653e>
	<hash_050101b83f4207a85eb6490bc55411c60672f1>
		<name>Convert Timeticks to Days</name>
		<items>
			<hash_14010122f30001791ccbe84893f46d9badf084>
				<sequence>1</sequence>
				<type>4</type>
				<value>CURRENT_DATA_SOURCE</value>
			</hash_14010122f30001791ccbe84893f46d9badf084>
			<hash_140101c0490dd4fc2d4b8113a97544fcda692e>
				<sequence>2</sequence>
				<type>6</type>
				<value>8640000</value>
			</hash_140101c0490dd4fc2d4b8113a97544fcda692e>
			<hash_14010170d5ff8f23a96469a769d20b084a835a>
				<sequence>3</sequence>
				<type>2</type>
				<value>4</value>
			</hash_14010170d5ff8f23a96469a769d20b084a835a>
		</items>
	</hash_050101b83f4207a85eb6490bc55411c60672f1>
	<hash_05010173f95f8b77b5508157d64047342c421e>
		<name>Turn Bytes into Bits</name>
		<items>
			<hash_1401019bbf6b792507bb9bb17d2af0970f9be9>
				<sequence>1</sequence>
				<type>4</type>
				<value>CURRENT_DATA_SOURCE</value>
			</hash_1401019bbf6b792507bb9bb17d2af0970f9be9>
			<hash_140101a4b8eb2c3bf4920a3ef571a7a004be53>
				<sequence>2</sequence>
				<type>6</type>
				<value>8</value>
			</hash_140101a4b8eb2c3bf4920a3ef571a7a004be53>
			<hash_140101caa4e023ac2d7b1c4b4c8c4adfd55dfe>
				<sequence>3</sequence>
				<type>2</type>
				<value>3</value>
			</hash_140101caa4e023ac2d7b1c4b4c8c4adfd55dfe>
		</items>
	</hash_05010173f95f8b77b5508157d64047342c421e>
	<hash_040101d75e406fdeca4fcef45b8be3a9a63cbc>
		<name>SNMP - Interface Statistics</name>
		<description>Queries a host for a list of monitorable interfaces</description>
		<xml_path>&lt;path_cacti&gt;/resource/snmp_queries/interface.xml</xml_path>
		<data_input_id>hash_030101bf566c869ac6443b0c75d1c32b5a350e</data_input_id>
		<graphs>
			<hash_110101a4b829746fb45e35e10474c36c69c0cf>
				<graph_template_id>hash_00010106621cd4a9289417cadcb8f9b5cfba80</graph_template_id>
				<name>In/Out Errors/Discarded Packets</name>
				<rrd>
					<item_000>
						<snmp_field_name>ifInErrors</snmp_field_name>
						<data_template_id>hash_01010136335cd98633963a575b70639cd2fdad</data_template_id>
						<data_template_rrd_id>hash_080101c802e2fd77f5b0a4c4298951bf65957c</data_template_rrd_id>
					</item_000>
					<item_001>
						<snmp_field_name>ifInDiscards</snmp_field_name>
						<data_template_id>hash_01010136335cd98633963a575b70639cd2fdad</data_template_id>
						<data_template_rrd_id>hash_0801014e2a72240955380dc8ffacfcc8c09874</data_template_rrd_id>
					</item_001>
					<item_002>
						<snmp_field_name>ifOutDiscards</snmp_field_name>
						<data_template_id>hash_01010136335cd98633963a575b70639cd2fdad</data_template_id>
						<data_template_rrd_id>hash_08010113ebb33f9cbccfcba828db1075a8167c</data_template_rrd_id>
					</item_002>
					<item_003>
						<snmp_field_name>ifOutErrors</snmp_field_name>
						<data_template_id>hash_01010136335cd98633963a575b70639cd2fdad</data_template_id>
						<data_template_rrd_id>hash_08010131399c3725bee7e09ec04049e3d5cd17</data_template_rrd_id>
					</item_003>
				</rrd>
				<sv_graph>
					<hash_1201010180de36c2fc1b1c3d929705cdaadfc6>
						<field_name>title</field_name>
						<sequence>1</sequence>
						<text>|host_description| - Errors - |query_ifAlias|</text>
					</hash_1201010180de36c2fc1b1c3d929705cdaadfc6>
					<hash_120101299d3434851fc0d5c0e105429069709d>
						<field_name>title</field_name>
						<sequence>2</sequence>
						<text>|host_description| - Errors - |query_ifName|</text>
					</hash_120101299d3434851fc0d5c0e105429069709d>
					<hash_1201018c8860b17fd67a9a500b4cb8b5e19d4b>
						<field_name>title</field_name>
						<sequence>3</sequence>
						<text>|host_description| - Errors - |query_ifIP| (|query_ifDescr|)</text>
					</hash_1201018c8860b17fd67a9a500b4cb8b5e19d4b>
					<hash_120101d96360ae5094e5732e7e7496ceceb636>
						<field_name>title</field_name>
						<sequence>4</sequence>
						<text>|host_description| - Errors - |query_ifDescr|/|query_ifIndex|</text>
					</hash_120101d96360ae5094e5732e7e7496ceceb636>
				</sv_graph>
				<sv_data_source>
					<hash_1301016537b3209e0697fbec278e94e7317b52>
						<field_name>name</field_name>
						<data_template_id>hash_01010136335cd98633963a575b70639cd2fdad</data_template_id>
						<sequence>1</sequence>
						<text>|host_description| - Errors - |query_ifIP| - |query_ifName|</text>
					</hash_1301016537b3209e0697fbec278e94e7317b52>
					<hash_1301016d3f612051016f48c951af8901720a1c>
						<field_name>name</field_name>
						<data_template_id>hash_01010136335cd98633963a575b70639cd2fdad</data_template_id>
						<sequence>2</sequence>
						<text>|host_description| - Errors - |query_ifName|</text>
					</hash_1301016d3f612051016f48c951af8901720a1c>
					<hash_13010162bc981690576d0b2bd0041ec2e4aa6f>
						<field_name>name</field_name>
						<data_template_id>hash_01010136335cd98633963a575b70639cd2fdad</data_template_id>
						<sequence>3</sequence>
						<text>|host_description| - Errors - |query_ifIP|/|query_ifDescr|</text>
					</hash_13010162bc981690576d0b2bd0041ec2e4aa6f>
					<hash_130101adb270d55ba521d205eac6a21478804a>
						<field_name>name</field_name>
						<data_template_id>hash_01010136335cd98633963a575b70639cd2fdad</data_template_id>
						<sequence>4</sequence>
						<text>|host_description| - Errors - |query_ifDescr|</text>
					</hash_130101adb270d55ba521d205eac6a21478804a>
				</sv_data_source>
			</hash_110101a4b829746fb45e35e10474c36c69c0cf>
			<hash_11010101e33224f8b15997d3d09d6b1bf83e18>
				<graph_template_id>hash_00010110ca5530554da7b73dc69d291bf55d38</graph_template_id>
				<name>In/Out Non-Unicast Packets</name>
				<rrd>
					<item_000>
						<snmp_field_name>ifOutNUcastPkts</snmp_field_name>
						<data_template_id>hash_010101c84e511401a747409053c90ba910d0fe</data_template_id>
						<data_template_rrd_id>hash_0801017be68cbc4ee0b2973eb9785f8c7a35c7</data_template_rrd_id>
					</item_000>
					<item_001>
						<snmp_field_name>ifInNUcastPkts</snmp_field_name>
						<data_template_id>hash_010101c84e511401a747409053c90ba910d0fe</data_template_id>
						<data_template_rrd_id>hash_08010193e2b6f59b10b13f2ddf2da3ae98b89a</data_template_rrd_id>
					</item_001>
				</rrd>
				<sv_graph>
					<hash_1201016a1d5e477fd0b8a4d743993be0fa2c8c>
						<field_name>title</field_name>
						<sequence>1</sequence>
						<text>|host_description| - Non-Unicast Packets - |query_ifAlias|</text>
					</hash_1201016a1d5e477fd0b8a4d743993be0fa2c8c>
					<hash_120101750a290cadc3dc60bb682a5c5f47df16>
						<field_name>title</field_name>
						<sequence>2</sequence>
						<text>|host_description| - Non-Unicast Packets - |query_ifName|</text>
					</hash_120101750a290cadc3dc60bb682a5c5f47df16>
					<hash_120101bde195eecc256c42ca9725f1f22c1dc0>
						<field_name>title</field_name>
						<sequence>3</sequence>
						<text>|host_description| - Non-Unicast Packets - |query_ifIP| (|query_ifDescr|)</text>
					</hash_120101bde195eecc256c42ca9725f1f22c1dc0>
					<hash_120101d9e97d22689e4ffddaca23b46f2aa306>
						<field_name>title</field_name>
						<sequence>4</sequence>
						<text>|host_description| - Non-Unicast Packets - |query_ifDescr|/|query_ifIndex|</text>
					</hash_120101d9e97d22689e4ffddaca23b46f2aa306>
				</sv_graph>
				<sv_data_source>
					<hash_13010177065435f3bbb2ff99bc3b43b81de8fe>
						<field_name>name</field_name>
						<data_template_id>hash_010101c84e511401a747409053c90ba910d0fe</data_template_id>
						<sequence>1</sequence>
						<text>|host_description| - Non-Unicast Packets - |query_ifIP| - |query_ifName|</text>
					</hash_13010177065435f3bbb2ff99bc3b43b81de8fe>
					<hash_130101240d8893092619c97a54265e8d0b86a1>
						<field_name>name</field_name>
						<data_template_id>hash_010101c84e511401a747409053c90ba910d0fe</data_template_id>
						<sequence>2</sequence>
						<text>|host_description| - Non-Unicast Packets - |query_ifName|</text>
					</hash_130101240d8893092619c97a54265e8d0b86a1>
					<hash_1301014b200ecf445bdeb4c84975b74991df34>
						<field_name>name</field_name>
						<data_template_id>hash_010101c84e511401a747409053c90ba910d0fe</data_template_id>
						<sequence>3</sequence>
						<text>|host_description| - Non-Unicast Packets - |query_ifIP|/|query_ifDescr|</text>
					</hash_1301014b200ecf445bdeb4c84975b74991df34>
					<hash_130101d6da3887646078e4d01fe60a123c2179>
						<field_name>name</field_name>
						<data_template_id>hash_010101c84e511401a747409053c90ba910d0fe</data_template_id>
						<sequence>4</sequence>
						<text>|host_description| - Non-Unicast Packets - |query_ifDescr|</text>
					</hash_130101d6da3887646078e4d01fe60a123c2179>
				</sv_data_source>
			</hash_11010101e33224f8b15997d3d09d6b1bf83e18>
			<hash_1101011e6edee3115c42d644dbd014f0577066>
				<graph_template_id>hash_000101e0d1625a1f4776a5294583659d5cee15</graph_template_id>
				<name>In/Out Unicast Packets</name>
				<rrd>
					<item_000>
						<snmp_field_name>ifInUcastPkts</snmp_field_name>
						<data_template_id>hash_0101012f654f7d69ac71a5d56b1db8543ccad3</data_template_id>
						<data_template_rrd_id>hash_080101636672962b5bb2f31d86985e2ab4bdfe</data_template_rrd_id>
					</item_000>
					<item_001>
						<snmp_field_name>ifOutUcastPkts</snmp_field_name>
						<data_template_id>hash_0101012f654f7d69ac71a5d56b1db8543ccad3</data_template_id>
						<data_template_rrd_id>hash_08010118ce92c125a236a190ee9dd948f56268</data_template_rrd_id>
					</item_001>
				</rrd>
				<sv_graph>
					<hash_12010154f5a5508fc525a15bc2be83a880e0c9>
						<field_name>title</field_name>
						<sequence>1</sequence>
						<text>|host_description| - Unicast Packets - |query_ifAlias|</text>
					</hash_12010154f5a5508fc525a15bc2be83a880e0c9>
					<hash_12010148ceaba62e0c2671a810a7f1adc5f751>
						<field_name>title</field_name>
						<sequence>2</sequence>
						<text>|host_description| - Unicast Packets - |query_ifName|</text>
					</hash_12010148ceaba62e0c2671a810a7f1adc5f751>
					<hash_120101d6258884bed44abe46d264198adc7c5d>
						<field_name>title</field_name>
						<sequence>3</sequence>
						<text>|host_description| - Unicast Packets - |query_ifIP| (|query_ifDescr|)</text>
					</hash_120101d6258884bed44abe46d264198adc7c5d>
					<hash_1201016eb58d9835b2b86222306d6ced9961d9>
						<field_name>title</field_name>
						<sequence>4</sequence>
						<text>|host_description| - Unicast Packets - |query_ifDescr|/|query_ifIndex|</text>
					</hash_1201016eb58d9835b2b86222306d6ced9961d9>
				</sv_graph>
				<sv_data_source>
					<hash_130101ce7769b97d80ca31d21f83dc18ba93c2>
						<field_name>name</field_name>
						<data_template_id>hash_0101012f654f7d69ac71a5d56b1db8543ccad3</data_template_id>
						<sequence>1</sequence>
						<text>|host_description| - Unicast Packets - |query_ifIP| - |query_ifName|</text>
					</hash_130101ce7769b97d80ca31d21f83dc18ba93c2>
					<hash_1301011ee1f9717f3f4771f7f823ca5a8b83dd>
						<field_name>name</field_name>
						<data_template_id>hash_0101012f654f7d69ac71a5d56b1db8543ccad3</data_template_id>
						<sequence>2</sequence>
						<text>|host_description| - Unicast Packets - |query_ifName|</text>
					</hash_1301011ee1f9717f3f4771f7f823ca5a8b83dd>
					<hash_130101a7dbd54604533b592d4fae6e67587e32>
						<field_name>name</field_name>
						<data_template_id>hash_0101012f654f7d69ac71a5d56b1db8543ccad3</data_template_id>
						<sequence>3</sequence>
						<text>|host_description| - Unicast Packets - |query_ifIP|/|query_ifDescr|</text>
					</hash_130101a7dbd54604533b592d4fae6e67587e32>
					<hash_130101b148fa7199edcf06cd71c89e5c5d7b63>
						<field_name>name</field_name>
						<data_template_id>hash_0101012f654f7d69ac71a5d56b1db8543ccad3</data_template_id>
						<sequence>4</sequence>
						<text>|host_description| - Unicast Packets - |query_ifDescr|</text>
					</hash_130101b148fa7199edcf06cd71c89e5c5d7b63>
				</sv_data_source>
			</hash_1101011e6edee3115c42d644dbd014f0577066>
			<hash_110101ab93b588c29731ab15db601ca0bc9dec>
				<graph_template_id>hash_000101df244b337547b434b486662c3c5c7472</graph_template_id>
				<name>In/Out Bytes (64-bit Counters)</name>
				<rrd>
					<item_000>
						<snmp_field_name>ifHCInOctets</snmp_field_name>
						<data_template_id>hash_0101016632e1e0b58a565c135d7ff90440c335</data_template_id>
						<data_template_rrd_id>hash_0801012df25c57022b0c7e7d0be4c035ada1a0</data_template_rrd_id>
					</item_000>
					<item_001>
						<snmp_field_name>ifHCOutOctets</snmp_field_name>
						<data_template_id>hash_0101016632e1e0b58a565c135d7ff90440c335</data_template_id>
						<data_template_rrd_id>hash_080101721c0794526d1ac1c359f27dc56faa49</data_template_rrd_id>
					</item_001>
				</rrd>
				<sv_graph>
					<hash_12010174c33dd7c052d14a8224148ab3fe23ae>
						<field_name>title</field_name>
						<sequence>1</sequence>
						<text>|host_description| - Traffic - |query_ifAlias|</text>
					</hash_12010174c33dd7c052d14a8224148ab3fe23ae>
					<hash_1201010a5eb36e98c04ad6be8e1ef66caeed3c>
						<field_name>title</field_name>
						<sequence>2</sequence>
						<text>|host_description| - Traffic - |query_ifName|</text>
					</hash_1201010a5eb36e98c04ad6be8e1ef66caeed3c>
					<hash_1201014c4386a96e6057b7bd0b78095209ddfa>
						<field_name>title</field_name>
						<sequence>3</sequence>
						<text>|host_description| - Traffic - |query_ifIP| (|query_ifDescr|)</text>
					</hash_1201014c4386a96e6057b7bd0b78095209ddfa>
					<hash_120101fd3a384768b0388fa64119fe2f0cc113>
						<field_name>title</field_name>
						<sequence>4</sequence>
						<text>|host_description| - Traffic - |query_ifDescr|/|query_ifIndex|</text>
					</hash_120101fd3a384768b0388fa64119fe2f0cc113>
				</sv_graph>
				<sv_data_source>
					<hash_130101c582d3b37f19e4a703d9bf4908dc6548>
						<field_name>name</field_name>
						<data_template_id>hash_0101016632e1e0b58a565c135d7ff90440c335</data_template_id>
						<sequence>1</sequence>
						<text>|host_description| - Traffic - |query_ifIP| - |query_ifName|</text>
					</hash_130101c582d3b37f19e4a703d9bf4908dc6548>
					<hash_130101ce0b9c92a15759d3ddbd7161d26a98b7>
						<field_name>rrd_maximum</field_name>
						<data_template_id>hash_0101016632e1e0b58a565c135d7ff90440c335</data_template_id>
						<sequence>1</sequence>
						<text>|query_ifSpeed|</text>
					</hash_130101ce0b9c92a15759d3ddbd7161d26a98b7>
					<hash_130101e1be83d708ed3c0b8715ccb6517a0365>
						<field_name>name</field_name>
						<data_template_id>hash_0101016632e1e0b58a565c135d7ff90440c335</data_template_id>
						<sequence>2</sequence>
						<text>|host_description| - Traffic - |query_ifName|</text>
					</hash_130101e1be83d708ed3c0b8715ccb6517a0365>
					<hash_13010157a9ae1f197498ca8dcde90194f61cbc>
						<field_name>name</field_name>
						<data_template_id>hash_0101016632e1e0b58a565c135d7ff90440c335</data_template_id>
						<sequence>3</sequence>
						<text>|host_description| - Traffic - |query_ifIP|/|query_ifDescr|</text>
					</hash_13010157a9ae1f197498ca8dcde90194f61cbc>
					<hash_1301010110e120981c7ff15304e4a85cb42cbe>
						<field_name>name</field_name>
						<data_template_id>hash_0101016632e1e0b58a565c135d7ff90440c335</data_template_id>
						<sequence>4</sequence>
						<text>|host_description| - Traffic - |query_ifDescr|</text>
					</hash_1301010110e120981c7ff15304e4a85cb42cbe>
				</sv_data_source>
			</hash_110101ab93b588c29731ab15db601ca0bc9dec>
			<hash_110101ae34f5f385bed8c81a158bf3030f1089>
				<graph_template_id>hash_0001015deb0d66c81262843dce5f3861be9966</graph_template_id>
				<name>In/Out Bits</name>
				<rrd>
					<item_000>
						<snmp_field_name>ifInOctets</snmp_field_name>
						<data_template_id>hash_0101016632e1e0b58a565c135d7ff90440c335</data_template_id>
						<data_template_rrd_id>hash_0801012df25c57022b0c7e7d0be4c035ada1a0</data_template_rrd_id>
					</item_000>
					<item_001>
						<snmp_field_name>ifOutOctets</snmp_field_name>
						<data_template_id>hash_0101016632e1e0b58a565c135d7ff90440c335</data_template_id>
						<data_template_rrd_id>hash_080101721c0794526d1ac1c359f27dc56faa49</data_template_rrd_id>
					</item_001>
				</rrd>
				<sv_graph>
					<hash_120101aafaab75d93c10a760d600c4ab4a742c>
						<field_name>title</field_name>
						<sequence>2</sequence>
						<text>|host_description| - Traffic - |query_ifAlias|</text>
					</hash_120101aafaab75d93c10a760d600c4ab4a742c>
					<hash_120101bda15298139ad22bdc8a3b0952d4e3ab>
						<field_name>title</field_name>
						<sequence>3</sequence>
						<text>|host_description| - Traffic - |query_ifIP| (|query_ifDescr|)</text>
					</hash_120101bda15298139ad22bdc8a3b0952d4e3ab>
					<hash_12010129e48483d0471fcd996bfb702a5960aa>
						<field_name>title</field_name>
						<sequence>4</sequence>
						<text>|host_description| - Traffic - |query_ifDescr|/|query_ifIndex|</text>
					</hash_12010129e48483d0471fcd996bfb702a5960aa>
					<hash_12010149dca5592ac26ff149a4fbd18d690644>
						<field_name>title</field_name>
						<sequence>5</sequence>
						<text>|host_description| - Traffic - |query_ifName|</text>
					</hash_12010149dca5592ac26ff149a4fbd18d690644>
				</sv_graph>
				<sv_data_source>
					<hash_13010187a659326af8c75158e5142874fd74b0>
						<field_name>name</field_name>
						<data_template_id>hash_0101016632e1e0b58a565c135d7ff90440c335</data_template_id>
						<sequence>1</sequence>
						<text>|host_description| - Traffic - |query_ifIP| - |query_ifName|</text>
					</hash_13010187a659326af8c75158e5142874fd74b0>
					<hash_1301017e093c535fa3d810fa76fc3d8c80c94b>
						<field_name>rrd_maximum</field_name>
						<data_template_id>hash_0101016632e1e0b58a565c135d7ff90440c335</data_template_id>
						<sequence>1</sequence>
						<text>|query_ifSpeed|</text>
					</hash_1301017e093c535fa3d810fa76fc3d8c80c94b>
					<hash_13010114aa2dead86bbad0f992f1514722c95e>
						<field_name>name</field_name>
						<data_template_id>hash_0101016632e1e0b58a565c135d7ff90440c335</data_template_id>
						<sequence>2</sequence>
						<text>|host_description| - Traffic - |query_ifName|</text>
					</hash_13010114aa2dead86bbad0f992f1514722c95e>
					<hash_13010170390712158c3c5052a7d830fb456489>
						<field_name>name</field_name>
						<data_template_id>hash_0101016632e1e0b58a565c135d7ff90440c335</data_template_id>
						<sequence>3</sequence>
						<text>|host_description| - Traffic - |query_ifIP|/|query_ifDescr|</text>
					</hash_13010170390712158c3c5052a7d830fb456489>
					<hash_130101084efd82bbddb69fb2ac9bd0b0f16ac6>
						<field_name>name</field_name>
						<data_template_id>hash_0101016632e1e0b58a565c135d7ff90440c335</data_template_id>
						<sequence>4</sequence>
						<text>|host_description| - Traffic - |query_ifDescr|</text>
					</hash_130101084efd82bbddb69fb2ac9bd0b0f16ac6>
				</sv_data_source>
			</hash_110101ae34f5f385bed8c81a158bf3030f1089>
			<hash_1101011e16a505ddefb40356221d7a50619d91>
				<graph_template_id>hash_0001015deb0d66c81262843dce5f3861be9966</graph_template_id>
				<name>In/Out Bits (64-bit Counters)</name>
				<rrd>
					<item_000>
						<snmp_field_name>ifHCInOctets</snmp_field_name>
						<data_template_id>hash_0101016632e1e0b58a565c135d7ff90440c335</data_template_id>
						<data_template_rrd_id>hash_0801012df25c57022b0c7e7d0be4c035ada1a0</data_template_rrd_id>
					</item_000>
					<item_001>
						<snmp_field_name>ifHCOutOctets</snmp_field_name>
						<data_template_id>hash_0101016632e1e0b58a565c135d7ff90440c335</data_template_id>
						<data_template_rrd_id>hash_080101721c0794526d1ac1c359f27dc56faa49</data_template_rrd_id>
					</item_001>
				</rrd>
				<sv_graph>
					<hash_1201013f42d358965cb94ce4f708b59e04f82b>
						<field_name>title</field_name>
						<sequence>1</sequence>
						<text>|host_description| - Traffic - |query_ifName|</text>
					</hash_1201013f42d358965cb94ce4f708b59e04f82b>
					<hash_12010169c14fbcc23aecb9920b3cdad7f89901>
						<field_name>title</field_name>
						<sequence>2</sequence>
						<text>|host_description| - Traffic - |query_ifDescr|/|query_ifIndex|</text>
					</hash_12010169c14fbcc23aecb9920b3cdad7f89901>
					<hash_120101a1d061ff7fb9875b29c54de4fadddcdc>
						<field_name>title</field_name>
						<sequence>3</sequence>
						<text>|host_description| - Traffic - |query_ifAlias|</text>
					</hash_120101a1d061ff7fb9875b29c54de4fadddcdc>
					<hash_12010145f44b2f811ea8a8ace1cbed8ef906f1>
						<field_name>title</field_name>
						<sequence>4</sequence>
						<text>|host_description| - Traffic - |query_ifIP| (|query_ifDescr|)</text>
					</hash_12010145f44b2f811ea8a8ace1cbed8ef906f1>
				</sv_graph>
				<sv_data_source>
					<hash_1301012e8b27c63d98249096ad5bc320787f43>
						<field_name>name</field_name>
						<data_template_id>hash_0101016632e1e0b58a565c135d7ff90440c335</data_template_id>
						<sequence>1</sequence>
						<text>|host_description| - Traffic - |query_ifIP| - |query_ifName|</text>
					</hash_1301012e8b27c63d98249096ad5bc320787f43>
					<hash_130101e85ddc56efa677b70448f9e931360b77>
						<field_name>rrd_maximum</field_name>
						<data_template_id>hash_0101016632e1e0b58a565c135d7ff90440c335</data_template_id>
						<sequence>1</sequence>
						<text>|query_ifSpeed|</text>
					</hash_130101e85ddc56efa677b70448f9e931360b77>
					<hash_1301018d820d091ec1a9683cfa74a462f239ee>
						<field_name>name</field_name>
						<data_template_id>hash_0101016632e1e0b58a565c135d7ff90440c335</data_template_id>
						<sequence>2</sequence>
						<text>|host_description| - Traffic - |query_ifName|</text>
					</hash_1301018d820d091ec1a9683cfa74a462f239ee>
					<hash_13010162a47c18be10f273a5f5a13a76b76f54>
						<field_name>name</field_name>
						<data_template_id>hash_0101016632e1e0b58a565c135d7ff90440c335</data_template_id>
						<sequence>3</sequence>
						<text>|host_description| - Traffic - |query_ifIP|/|query_ifDescr|</text>
					</hash_13010162a47c18be10f273a5f5a13a76b76f54>
					<hash_13010137bb8c5b38bb7e89ec88ea7ccacf44d4>
						<field_name>name</field_name>
						<data_template_id>hash_0101016632e1e0b58a565c135d7ff90440c335</data_template_id>
						<sequence>4</sequence>
						<text>|host_description| - Traffic - |query_ifDescr|</text>
					</hash_13010137bb8c5b38bb7e89ec88ea7ccacf44d4>
					<hash_130101db6547fe6d8a04e7d007eb8aab9d4ec5>
						<field_name>name</field_name>
						<data_template_id>hash_0101016632e1e0b58a565c135d7ff90440c335</data_template_id>
						<sequence>5</sequence>
						<text>|host_description| - Traffic - |query_ifAlias|</text>
					</hash_130101db6547fe6d8a04e7d007eb8aab9d4ec5>
				</sv_data_source>
			</hash_1101011e16a505ddefb40356221d7a50619d91>
			<hash_110101d1e0d9b8efd4af98d28ce2aad81a87e7>
				<graph_template_id>hash_000101df244b337547b434b486662c3c5c7472</graph_template_id>
				<name>In/Out Bytes</name>
				<rrd>
					<item_000>
						<snmp_field_name>ifInOctets</snmp_field_name>
						<data_template_id>hash_0101016632e1e0b58a565c135d7ff90440c335</data_template_id>
						<data_template_rrd_id>hash_0801012df25c57022b0c7e7d0be4c035ada1a0</data_template_rrd_id>
					</item_000>
					<item_001>
						<snmp_field_name>ifOutOctets</snmp_field_name>
						<data_template_id>hash_0101016632e1e0b58a565c135d7ff90440c335</data_template_id>
						<data_template_rrd_id>hash_080101721c0794526d1ac1c359f27dc56faa49</data_template_rrd_id>
					</item_001>
				</rrd>
				<sv_graph>
					<hash_120101a5899a68c68e50959a099d7ac591873a>
						<field_name>title</field_name>
						<sequence>1</sequence>
						<text>|host_description| - Traffic - |query_ifAlias|</text>
					</hash_120101a5899a68c68e50959a099d7ac591873a>
					<hash_1201017fb4a267065f960df81c15f9022cd3a4>
						<field_name>title</field_name>
						<sequence>2</sequence>
						<text>|host_description| - Traffic - |query_ifName|</text>
					</hash_1201017fb4a267065f960df81c15f9022cd3a4>
					<hash_120101e403f5a733bf5c8401a110609683deb3>
						<field_name>title</field_name>
						<sequence>3</sequence>
						<text>|host_description| - Traffic - |query_ifIP| (|query_ifDescr|)</text>
					</hash_120101e403f5a733bf5c8401a110609683deb3>
					<hash_120101809c2e80552d56b65ca496c1c2fff398>
						<field_name>title</field_name>
						<sequence>4</sequence>
						<text>|host_description| - Traffic - |query_ifDescr|/|query_ifIndex|</text>
					</hash_120101809c2e80552d56b65ca496c1c2fff398>
				</sv_graph>
				<sv_data_source>
					<hash_130101c7ee2110bf81639086d2da03d9d88286>
						<field_name>name</field_name>
						<data_template_id>hash_0101016632e1e0b58a565c135d7ff90440c335</data_template_id>
						<sequence>1</sequence>
						<text>|host_description| - Traffic - |query_ifIP| - |query_ifName|</text>
					</hash_130101c7ee2110bf81639086d2da03d9d88286>
					<hash_13010127eb220995925e1a5e0e41b2582a2af6>
						<field_name>rrd_maximum</field_name>
						<data_template_id>hash_0101016632e1e0b58a565c135d7ff90440c335</data_template_id>
						<sequence>1</sequence>
						<text>|query_ifSpeed|</text>
					</hash_13010127eb220995925e1a5e0e41b2582a2af6>
					<hash_1301018ef8ae2ef548892ab95bb6c9f0b3170e>
						<field_name>name</field_name>
						<data_template_id>hash_0101016632e1e0b58a565c135d7ff90440c335</data_template_id>
						<sequence>2</sequence>
						<text>|host_description| - Traffic - |query_ifName|</text>
					</hash_1301018ef8ae2ef548892ab95bb6c9f0b3170e>
					<hash_1301013a0f707d1c8fd0e061b70241541c7e2e>
						<field_name>name</field_name>
						<data_template_id>hash_0101016632e1e0b58a565c135d7ff90440c335</data_template_id>
						<sequence>3</sequence>
						<text>|host_description| - Traffic - |query_ifIP|/|query_ifDescr|</text>
					</hash_1301013a0f707d1c8fd0e061b70241541c7e2e>
					<hash_1301012347e9f53564a54d43f3c00d4b60040d>
						<field_name>name</field_name>
						<data_template_id>hash_0101016632e1e0b58a565c135d7ff90440c335</data_template_id>
						<sequence>4</sequence>
						<text>|host_description| - Traffic - |query_ifDescr|</text>
					</hash_1301012347e9f53564a54d43f3c00d4b60040d>
				</sv_data_source>
			</hash_110101d1e0d9b8efd4af98d28ce2aad81a87e7>
			<hash_110101ed7f68175d7bb83db8ead332fc945720>
				<graph_template_id>hash_0001011742b2066384637022d178cc5072905a</graph_template_id>
				<name>In/Out Bits with 95th Percentile</name>
				<rrd>
					<item_000>
						<snmp_field_name>ifInOctets</snmp_field_name>
						<data_template_id>hash_0101016632e1e0b58a565c135d7ff90440c335</data_template_id>
						<data_template_rrd_id>hash_0801012df25c57022b0c7e7d0be4c035ada1a0</data_template_rrd_id>
					</item_000>
					<item_001>
						<snmp_field_name>ifOutOctets</snmp_field_name>
						<data_template_id>hash_0101016632e1e0b58a565c135d7ff90440c335</data_template_id>
						<data_template_rrd_id>hash_080101721c0794526d1ac1c359f27dc56faa49</data_template_rrd_id>
					</item_001>
				</rrd>
				<sv_graph>
					<hash_1201011acc9985eb91a7234ff97608cb85b0f5>
						<field_name>title</field_name>
						<sequence>1</sequence>
						<text>|host_description| - Traffic - |query_ifAlias|</text>
					</hash_1201011acc9985eb91a7234ff97608cb85b0f5>
					<hash_120101f434ec853c479d424276f367e9806a75>
						<field_name>title</field_name>
						<sequence>2</sequence>
						<text>|host_description| - Traffic - |query_ifName|</text>
					</hash_120101f434ec853c479d424276f367e9806a75>
					<hash_1201019b085245847444c5fb90ebbf4448e265>
						<field_name>title</field_name>
						<sequence>3</sequence>
						<text>|host_description| - Traffic - |query_ifIP| (|query_ifDescr|)</text>
					</hash_1201019b085245847444c5fb90ebbf4448e265>
					<hash_1201015977863f28629bd8eb93a2a9cbc3e306>
						<field_name>title</field_name>
						<sequence>4</sequence>
						<text>|host_description| - Traffic - |query_ifDescr|/|query_ifIndex|</text>
					</hash_1201015977863f28629bd8eb93a2a9cbc3e306>
				</sv_graph>
				<sv_data_source>
					<hash_1301017e87efd0075caba9908e2e6e569b25b0>
						<field_name>name</field_name>
						<data_template_id>hash_0101016632e1e0b58a565c135d7ff90440c335</data_template_id>
						<sequence>1</sequence>
						<text>|host_description| - Traffic - |query_ifIP| - |query_ifName|</text>
					</hash_1301017e87efd0075caba9908e2e6e569b25b0>
					<hash_1301013b018f789ff72cc5693ef79e3a794370>
						<field_name>rrd_maximum</field_name>
						<data_template_id>hash_0101016632e1e0b58a565c135d7ff90440c335</data_template_id>
						<sequence>1</sequence>
						<text>|query_ifSpeed|</text>
					</hash_1301013b018f789ff72cc5693ef79e3a794370>
					<hash_130101dd28d96a253ab86846aedb25d1cca712>
						<field_name>name</field_name>
						<data_template_id>hash_0101016632e1e0b58a565c135d7ff90440c335</data_template_id>
						<sequence>2</sequence>
						<text>|host_description| - Traffic - |query_ifName|</text>
					</hash_130101dd28d96a253ab86846aedb25d1cca712>
					<hash_130101ce425fed4eb3174e4f1cde9713eeafa0>
						<field_name>name</field_name>
						<data_template_id>hash_0101016632e1e0b58a565c135d7ff90440c335</data_template_id>
						<sequence>3</sequence>
						<text>|host_description| - Traffic - |query_ifIP|/|query_ifDescr|</text>
					</hash_130101ce425fed4eb3174e4f1cde9713eeafa0>
					<hash_130101d0d05156ddb2c65181588db4b64d3907>
						<field_name>name</field_name>
						<data_template_id>hash_0101016632e1e0b58a565c135d7ff90440c335</data_template_id>
						<sequence>4</sequence>
						<text>|host_description| - Traffic - |query_ifDescr|</text>
					</hash_130101d0d05156ddb2c65181588db4b64d3907>
				</sv_data_source>
			</hash_110101ed7f68175d7bb83db8ead332fc945720>
			<hash_110101f85386cd2fc94634ef167c7f1e5fbcd0>
				<graph_template_id>hash_00010113b47e10b2d5db45707d61851f69c52b</graph_template_id>
				<name>In/Out Bits with Total Bandwidth</name>
				<rrd>
					<item_000>
						<snmp_field_name>ifInOctets</snmp_field_name>
						<data_template_id>hash_0101016632e1e0b58a565c135d7ff90440c335</data_template_id>
						<data_template_rrd_id>hash_0801012df25c57022b0c7e7d0be4c035ada1a0</data_template_rrd_id>
					</item_000>
					<item_001>
						<snmp_field_name>ifOutOctets</snmp_field_name>
						<data_template_id>hash_0101016632e1e0b58a565c135d7ff90440c335</data_template_id>
						<data_template_rrd_id>hash_080101721c0794526d1ac1c359f27dc56faa49</data_template_rrd_id>
					</item_001>
				</rrd>
				<sv_graph>
					<hash_120101820eb01dd91c9026fbdf667a7f25302f>
						<field_name>title</field_name>
						<sequence>1</sequence>
						<text>|host_description| - Traffic - |query_ifAlias|</text>
					</hash_120101820eb01dd91c9026fbdf667a7f25302f>
					<hash_12010137b6711af3930c56309cf8956d8bbf14>
						<field_name>title</field_name>
						<sequence>2</sequence>
						<text>|host_description| - Traffic - |query_ifName|</text>
					</hash_12010137b6711af3930c56309cf8956d8bbf14>
					<hash_120101cc435c5884a75421329a9b08207c1c90>
						<field_name>title</field_name>
						<sequence>3</sequence>
						<text>|host_description| - Traffic - |query_ifIP| (|query_ifDescr|)</text>
					</hash_120101cc435c5884a75421329a9b08207c1c90>
					<hash_12010182edeea1ec249c9818773e3145836492>
						<field_name>title</field_name>
						<sequence>4</sequence>
						<text>|host_description| - Traffic - |query_ifDescr|/|query_ifIndex|</text>
					</hash_12010182edeea1ec249c9818773e3145836492>
				</sv_graph>
				<sv_data_source>
					<hash_130101b225229dbbb48c1766cf90298674ceed>
						<field_name>name</field_name>
						<data_template_id>hash_0101016632e1e0b58a565c135d7ff90440c335</data_template_id>
						<sequence>1</sequence>
						<text>|host_description| - Traffic - |query_ifIP| - |query_ifName|</text>
					</hash_130101b225229dbbb48c1766cf90298674ceed>
					<hash_130101e9ab404a294e406c20fdd30df766161f>
						<field_name>rrd_maximum</field_name>
						<data_template_id>hash_0101016632e1e0b58a565c135d7ff90440c335</data_template_id>
						<sequence>1</sequence>
						<text>|query_ifSpeed|</text>
					</hash_130101e9ab404a294e406c20fdd30df766161f>
					<hash_130101c79248ddbbd195907260887b021a055d>
						<field_name>name</field_name>
						<data_template_id>hash_0101016632e1e0b58a565c135d7ff90440c335</data_template_id>
						<sequence>2</sequence>
						<text>|host_description| - Traffic - |query_ifName|</text>
					</hash_130101c79248ddbbd195907260887b021a055d>
					<hash_13010112a6750d973b7f14783f205d86220082>
						<field_name>name</field_name>
						<data_template_id>hash_0101016632e1e0b58a565c135d7ff90440c335</data_template_id>
						<sequence>3</sequence>
						<text>|host_description| - Traffic - |query_ifIP|/|query_ifDescr|</text>
					</hash_13010112a6750d973b7f14783f205d86220082>
					<hash_13010125b151fcfe093812cb5c208e36dd697e>
						<field_name>name</field_name>
						<data_template_id>hash_0101016632e1e0b58a565c135d7ff90440c335</data_template_id>
						<sequence>4</sequence>
						<text>|host_description| - Traffic - |query_ifDescr|</text>
					</hash_13010125b151fcfe093812cb5c208e36dd697e>
				</sv_data_source>
			</hash_110101f85386cd2fc94634ef167c7f1e5fbcd0>
			<hash_1101017d309bf200b6e3cdb59a33493c2e58e0>
				<graph_template_id>hash_0001018ad6790c22b693680e041f21d62537ac</graph_template_id>
				<name>In/Out Bytes with Total Bandwidth</name>
				<rrd>
					<item_000>
						<snmp_field_name>ifInOctets</snmp_field_name>
						<data_template_id>hash_0101016632e1e0b58a565c135d7ff90440c335</data_template_id>
						<data_template_rrd_id>hash_0801012df25c57022b0c7e7d0be4c035ada1a0</data_template_rrd_id>
					</item_000>
					<item_001>
						<snmp_field_name>ifOutOctets</snmp_field_name>
						<data_template_id>hash_0101016632e1e0b58a565c135d7ff90440c335</data_template_id>
						<data_template_rrd_id>hash_080101721c0794526d1ac1c359f27dc56faa49</data_template_rrd_id>
					</item_001>
				</rrd>
				<sv_graph>
					<hash_120101c0422682831631bf539023fc04615025>
						<field_name>title</field_name>
						<sequence>1</sequence>
						<text>|host_description| - Traffic - |query_ifAlias|</text>
					</hash_120101c0422682831631bf539023fc04615025>
					<hash_12010187522150ee8a601b4d6a1f6b9e919c47>
						<field_name>title</field_name>
						<sequence>2</sequence>
						<text>|host_description| - Traffic - |query_ifName|</text>
					</hash_12010187522150ee8a601b4d6a1f6b9e919c47>
					<hash_120101993a87c04f550f1209d689d584aa8b45>
						<field_name>title</field_name>
						<sequence>3</sequence>
						<text>|host_description| - Traffic - |query_ifIP| (|query_ifDescr|)</text>
					</hash_120101993a87c04f550f1209d689d584aa8b45>
					<hash_120101183bb486c92a566fddcb0585ede37865>
						<field_name>title</field_name>
						<sequence>4</sequence>
						<text>|host_description| - Traffic - |query_ifDescr|/|query_ifIndex|</text>
					</hash_120101183bb486c92a566fddcb0585ede37865>
				</sv_graph>
				<sv_data_source>
					<hash_130101119578a4f01ab47e820b0e894e5e5bb3>
						<field_name>name</field_name>
						<data_template_id>hash_0101016632e1e0b58a565c135d7ff90440c335</data_template_id>
						<sequence>1</sequence>
						<text>|host_description| - Traffic - |query_ifIP| - |query_ifName|</text>
					</hash_130101119578a4f01ab47e820b0e894e5e5bb3>
					<hash_130101fdc4cb976c4b9053bfa2af791a21c5b5>
						<field_name>rrd_maximum</field_name>
						<data_template_id>hash_0101016632e1e0b58a565c135d7ff90440c335</data_template_id>
						<sequence>1</sequence>
						<text>|query_ifSpeed|</text>
					</hash_130101fdc4cb976c4b9053bfa2af791a21c5b5>
					<hash_130101940e57d24b2623849c77b59ed05931b9>
						<field_name>name</field_name>
						<data_template_id>hash_0101016632e1e0b58a565c135d7ff90440c335</data_template_id>
						<sequence>2</sequence>
						<text>|host_description| - Traffic - |query_ifName|</text>
					</hash_130101940e57d24b2623849c77b59ed05931b9>
					<hash_1301010f045eab01bbc4437b30da568ed5cb03>
						<field_name>name</field_name>
						<data_template_id>hash_0101016632e1e0b58a565c135d7ff90440c335</data_template_id>
						<sequence>3</sequence>
						<text>|host_description| - Traffic - |query_ifIP|/|query_ifDescr|</text>
					</hash_1301010f045eab01bbc4437b30da568ed5cb03>
					<hash_130101bd70bf71108d32f0bf91b24c85b87ff0>
						<field_name>name</field_name>
						<data_template_id>hash_0101016632e1e0b58a565c135d7ff90440c335</data_template_id>
						<sequence>4</sequence>
						<text>|host_description| - Traffic - |query_ifDescr|</text>
					</hash_130101bd70bf71108d32f0bf91b24c85b87ff0>
				</sv_data_source>
			</hash_1101017d309bf200b6e3cdb59a33493c2e58e0>
			<hash_110101a06c23783baa5022299706f5ff2a56e7>
				<graph_template_id>hash_0001011742b2066384637022d178cc5072905a</graph_template_id>
				<name>In/Out Bits (64-bit Counters) with 95th Percentile</name>
				<rrd>
					<item_000>
						<snmp_field_name>ifHCInOctets</snmp_field_name>
						<data_template_id>hash_0101016632e1e0b58a565c135d7ff90440c335</data_template_id>
						<data_template_rrd_id>hash_0801012df25c57022b0c7e7d0be4c035ada1a0</data_template_rrd_id>
					</item_000>
					<item_001>
						<snmp_field_name>ifHCOutOctets</snmp_field_name>
						<data_template_id>hash_0101016632e1e0b58a565c135d7ff90440c335</data_template_id>
						<data_template_rrd_id>hash_080101721c0794526d1ac1c359f27dc56faa49</data_template_rrd_id>
					</item_001>
				</rrd>
				<sv_graph>
					<hash_120101a877a37f5d0e6f49a5d9d99ac7e347f3>
						<field_name>title</field_name>
						<sequence>1</sequence>
						<text>|host_description| - Traffic - |query_ifAlias| </text>
					</hash_120101a877a37f5d0e6f49a5d9d99ac7e347f3>
					<hash_1201019e42f7e5310653f35f977285e48ecfa5>
						<field_name>title</field_name>
						<sequence>2</sequence>
						<text>|host_description| - Traffic - |query_ifName| </text>
					</hash_1201019e42f7e5310653f35f977285e48ecfa5>
					<hash_120101cab54d19353de5548e0151180cb7c5dd>
						<field_name>title</field_name>
						<sequence>3</sequence>
						<text>|host_description| - Traffic - |query_ifIP| (|query_ifDescr|) </text>
					</hash_120101cab54d19353de5548e0151180cb7c5dd>
					<hash_120101f9de6e508d7fa64d91d163d864b9f31a>
						<field_name>title</field_name>
						<sequence>4</sequence>
						<text>|host_description| - Traffic - |query_ifDescr|/|query_ifIndex| </text>
					</hash_120101f9de6e508d7fa64d91d163d864b9f31a>
				</sv_graph>
				<sv_data_source>
					<hash_130101af8c10bb98e3d96d7aeed76069f5d8f6>
						<field_name>name</field_name>
						<data_template_id>hash_0101016632e1e0b58a565c135d7ff90440c335</data_template_id>
						<sequence>1</sequence>
						<text>|host_description| - Traffic - |query_ifIP| - |query_ifName| </text>
					</hash_130101af8c10bb98e3d96d7aeed76069f5d8f6>
					<hash_130101d5fe4ab8a8049c76715b11367544a77b>
						<field_name>rrd_maximum</field_name>
						<data_template_id>hash_0101016632e1e0b58a565c135d7ff90440c335</data_template_id>
						<sequence>1</sequence>
						<text>|query_ifSpeed|</text>
					</hash_130101d5fe4ab8a8049c76715b11367544a77b>
					<hash_130101eb9aa71f654327ecea55af11c6ff06ac>
						<field_name>name</field_name>
						<data_template_id>hash_0101016632e1e0b58a565c135d7ff90440c335</data_template_id>
						<sequence>2</sequence>
						<text>|host_description| - Traffic - |query_ifName|</text>
					</hash_130101eb9aa71f654327ecea55af11c6ff06ac>
					<hash_130101afe143588235f0465993fd642dbc2ad9>
						<field_name>name</field_name>
						<data_template_id>hash_0101016632e1e0b58a565c135d7ff90440c335</data_template_id>
						<sequence>3</sequence>
						<text>|host_description| - Traffic - |query_ifIP|/|query_ifDescr|</text>
					</hash_130101afe143588235f0465993fd642dbc2ad9>
					<hash_130101424ebeaaef4a5cbffdc4611beeb7c19c>
						<field_name>name</field_name>
						<data_template_id>hash_0101016632e1e0b58a565c135d7ff90440c335</data_template_id>
						<sequence>4</sequence>
						<text>|host_description| - Traffic - |query_ifDescr|</text>
					</hash_130101424ebeaaef4a5cbffdc4611beeb7c19c>
				</sv_data_source>
			</hash_110101a06c23783baa5022299706f5ff2a56e7>
			<hash_1101011e24c56421c50a2114c15afd159a538c>
				<graph_template_id>hash_00010113b47e10b2d5db45707d61851f69c52b</graph_template_id>
				<name>In/Out Bits (64-bit Counters) with Total Bandwidth</name>
				<rrd>
					<item_000>
						<snmp_field_name>ifHCInOctets</snmp_field_name>
						<data_template_id>hash_0101016632e1e0b58a565c135d7ff90440c335</data_template_id>
						<data_template_rrd_id>hash_0801012df25c57022b0c7e7d0be4c035ada1a0</data_template_rrd_id>
					</item_000>
					<item_001>
						<snmp_field_name>ifHCOutOctets</snmp_field_name>
						<data_template_id>hash_0101016632e1e0b58a565c135d7ff90440c335</data_template_id>
						<data_template_rrd_id>hash_080101721c0794526d1ac1c359f27dc56faa49</data_template_rrd_id>
					</item_001>
				</rrd>
				<sv_graph>
					<hash_120101419c8f569d1695b86c1943f7204abf3d>
						<field_name>title</field_name>
						<sequence>1</sequence>
						<text>|host_description| - Traffic - |query_ifAlias|</text>
					</hash_120101419c8f569d1695b86c1943f7204abf3d>
					<hash_1201011819f9ccdb512f19acfdc4edcda425b5>
						<field_name>title</field_name>
						<sequence>2</sequence>
						<text>|host_description| - Traffic - |query_ifName|</text>
					</hash_1201011819f9ccdb512f19acfdc4edcda425b5>
					<hash_12010108310b48a18f195d941fcd2c4ed40e7b>
						<field_name>title</field_name>
						<sequence>3</sequence>
						<text>|host_description| - Traffic - |query_ifIP| (|query_ifDescr|)</text>
					</hash_12010108310b48a18f195d941fcd2c4ed40e7b>
					<hash_120101dffe8e880677480a795b1232fc1207e5>
						<field_name>title</field_name>
						<sequence>4</sequence>
						<text>|host_description| - Traffic - |query_ifDescr|/|query_ifIndex|</text>
					</hash_120101dffe8e880677480a795b1232fc1207e5>
				</sv_graph>
				<sv_data_source>
					<hash_130101694c4ef8e495357d8303d1c127d0c55e>
						<field_name>name</field_name>
						<data_template_id>hash_0101016632e1e0b58a565c135d7ff90440c335</data_template_id>
						<sequence>1</sequence>
						<text>|host_description| - Traffic - |query_ifIP| - |query_ifName|</text>
					</hash_130101694c4ef8e495357d8303d1c127d0c55e>
					<hash_1301010a772cfb504e15d7e784dd0e73ced97a>
						<field_name>rrd_maximum</field_name>
						<data_template_id>hash_0101016632e1e0b58a565c135d7ff90440c335</data_template_id>
						<sequence>1</sequence>
						<text>|query_ifSpeed|</text>
					</hash_1301010a772cfb504e15d7e784dd0e73ced97a>
					<hash_130101114c55114ede9f492d84b1c79d3bbae6>
						<field_name>name</field_name>
						<data_template_id>hash_0101016632e1e0b58a565c135d7ff90440c335</data_template_id>
						<sequence>2</sequence>
						<text>|host_description| - Traffic - |query_ifName| </text>
					</hash_130101114c55114ede9f492d84b1c79d3bbae6>
					<hash_1301018aa4f743291cd2afdea20a4180e6eb42>
						<field_name>name</field_name>
						<data_template_id>hash_0101016632e1e0b58a565c135d7ff90440c335</data_template_id>
						<sequence>3</sequence>
						<text>|host_description| - Traffic - |query_ifIP|/|query_ifDescr|</text>
					</hash_1301018aa4f743291cd2afdea20a4180e6eb42>
					<hash_1301013d4ba44d5e6a7bbcd5a448b9ef113c59>
						<field_name>name</field_name>
						<data_template_id>hash_0101016632e1e0b58a565c135d7ff90440c335</data_template_id>
						<sequence>4</sequence>
						<text>|host_description| - Traffic - |query_ifDescr|</text>
					</hash_1301013d4ba44d5e6a7bbcd5a448b9ef113c59>
				</sv_data_source>
			</hash_1101011e24c56421c50a2114c15afd159a538c>
			<hash_110101fefe4ae1ec313b6875d6502319f08cde>
				<graph_template_id>hash_0001018ad6790c22b693680e041f21d62537ac</graph_template_id>
				<name>In/Out Bytes (64-bit Counters) with Total Bandwidth</name>
				<rrd>
					<item_000>
						<snmp_field_name>ifHCInOctets</snmp_field_name>
						<data_template_id>hash_0101016632e1e0b58a565c135d7ff90440c335</data_template_id>
						<data_template_rrd_id>hash_0801012df25c57022b0c7e7d0be4c035ada1a0</data_template_rrd_id>
					</item_000>
					<item_001>
						<snmp_field_name>ifHCOutOctets</snmp_field_name>
						<data_template_id>hash_0101016632e1e0b58a565c135d7ff90440c335</data_template_id>
						<data_template_rrd_id>hash_080101721c0794526d1ac1c359f27dc56faa49</data_template_rrd_id>
					</item_001>
				</rrd>
				<sv_graph>
					<hash_1201019be678415c48e9ee7a16e5208e523c6d>
						<field_name>title</field_name>
						<sequence>1</sequence>
						<text>|host_description| - Traffic - |query_ifAlias|</text>
					</hash_1201019be678415c48e9ee7a16e5208e523c6d>
					<hash_120101702b89f7db8eae17a358e246d6264d05>
						<field_name>title</field_name>
						<sequence>2</sequence>
						<text>|host_description| - Traffic - |query_ifName|</text>
					</hash_120101702b89f7db8eae17a358e246d6264d05>
					<hash_1201011fc5aabb79ad301bee69e6bb0094df2c>
						<field_name>title</field_name>
						<sequence>3</sequence>
						<text>|host_description| - Traffic - |query_ifIP| (|query_ifDescr|)</text>
					</hash_1201011fc5aabb79ad301bee69e6bb0094df2c>
					<hash_120101bb5bd62bcfbfc5ff765afe625b830d31>
						<field_name>title</field_name>
						<sequence>4</sequence>
						<text>|host_description| - Traffic - |query_ifDescr|/|query_ifIndex|</text>
					</hash_120101bb5bd62bcfbfc5ff765afe625b830d31>
				</sv_graph>
				<sv_data_source>
					<hash_130101e29d0a2547c6a48e73ce2c800e308515>
						<field_name>name</field_name>
						<data_template_id>hash_0101016632e1e0b58a565c135d7ff90440c335</data_template_id>
						<sequence>1</sequence>
						<text>|host_description| - Traffic - |query_ifIP| - |query_ifName|</text>
					</hash_130101e29d0a2547c6a48e73ce2c800e308515>
					<hash_130101cf780d419b924d0cbbb173b9a4918208>
						<field_name>rrd_maximum</field_name>
						<data_template_id>hash_0101016632e1e0b58a565c135d7ff90440c335</data_template_id>
						<sequence>1</sequence>
						<text>|query_ifSpeed|</text>
					</hash_130101cf780d419b924d0cbbb173b9a4918208>
					<hash_1301013aeeb54a14baa08beaa59a1cd6af12c8>
						<field_name>name</field_name>
						<data_template_id>hash_0101016632e1e0b58a565c135d7ff90440c335</data_template_id>
						<sequence>2</sequence>
						<text>|host_description| - Traffic - |query_ifName|</text>
					</hash_1301013aeeb54a14baa08beaa59a1cd6af12c8>
					<hash_13010130aaee4b45f97ac74641442e17e4527e>
						<field_name>name</field_name>
						<data_template_id>hash_0101016632e1e0b58a565c135d7ff90440c335</data_template_id>
						<sequence>3</sequence>
						<text>|host_description| - Traffic - |query_ifIP|/|query_ifDescr|</text>
					</hash_13010130aaee4b45f97ac74641442e17e4527e>
					<hash_130101da2842ddfe7ea7d7b06266cc107169aa>
						<field_name>name</field_name>
						<data_template_id>hash_0101016632e1e0b58a565c135d7ff90440c335</data_template_id>
						<sequence>4</sequence>
						<text>|host_description| - Traffic - |query_ifDescr|</text>
					</hash_130101da2842ddfe7ea7d7b06266cc107169aa>
				</sv_data_source>
			</hash_110101fefe4ae1ec313b6875d6502319f08cde>
			<hash_110101c5792b18bf1263b5bf3826f9196376d9>
				<graph_template_id>hash_000101ed3f434a9ebd2f23ab9bc173d608b3d7</graph_template_id>
				<name>Interface - Broadcast Packets (Legacy)</name>
				<rrd>
					<item_000>
						<snmp_field_name>ifOutBroadcastPkts</snmp_field_name>
						<data_template_id>hash_010101c84e511401a747409053c90ba910d0fe</data_template_id>
						<data_template_rrd_id>hash_0801017be68cbc4ee0b2973eb9785f8c7a35c7</data_template_rrd_id>
					</item_000>
					<item_001>
						<snmp_field_name>ifInBroadcastPkts</snmp_field_name>
						<data_template_id>hash_010101c84e511401a747409053c90ba910d0fe</data_template_id>
						<data_template_rrd_id>hash_08010193e2b6f59b10b13f2ddf2da3ae98b89a</data_template_rrd_id>
					</item_001>
				</rrd>
				<sv_graph>
					<hash_1201016b166ed8f603998fdc51719da3478e55>
						<field_name>title</field_name>
						<sequence>1</sequence>
						<text>|host_description| - Broadcast Packets - |query_ifAlias|</text>
					</hash_1201016b166ed8f603998fdc51719da3478e55>
					<hash_120101dd545c92388329c666f7e88f99618e87>
						<field_name>title</field_name>
						<sequence>2</sequence>
						<text>|host_description| - Broadcast Packets - |query_ifName|</text>
					</hash_120101dd545c92388329c666f7e88f99618e87>
					<hash_12010171574f16039ab62c26d626c113ebdab0>
						<field_name>title</field_name>
						<sequence>3</sequence>
						<text>|host_description| - Broadcast Packets - |query_ifIP| (|query_ifDescr|)</text>
					</hash_12010171574f16039ab62c26d626c113ebdab0>
					<hash_120101555ae21f832f02689c7a6e2f690ec7d3>
						<field_name>title</field_name>
						<sequence>4</sequence>
						<text>|host_description| - Broadcast Packets - |query_ifDescr|/|query_ifIndex|</text>
					</hash_120101555ae21f832f02689c7a6e2f690ec7d3>
				</sv_graph>
				<sv_data_source>
					<hash_130101fc4e456b3fe4b712c943700ef1b3be80>
						<field_name>name</field_name>
						<data_template_id>hash_010101c84e511401a747409053c90ba910d0fe</data_template_id>
						<sequence>1</sequence>
						<text>|host_description| - Broadcast Packets - |query_ifAlias| </text>
					</hash_130101fc4e456b3fe4b712c943700ef1b3be80>
					<hash_130101aea995fae5b2500b69819a09d20e9760>
						<field_name>name</field_name>
						<data_template_id>hash_010101c84e511401a747409053c90ba910d0fe</data_template_id>
						<sequence>2</sequence>
						<text>|host_description| - Broadcast Packets - |query_ifName|</text>
					</hash_130101aea995fae5b2500b69819a09d20e9760>
					<hash_1301018e07b64fa0767a318ec6d0320c3f9e2c>
						<field_name>name</field_name>
						<data_template_id>hash_010101c84e511401a747409053c90ba910d0fe</data_template_id>
						<sequence>3</sequence>
						<text>|host_description| - Broadcast Packets - |query_ifIP| (|query_ifDescr|)</text>
					</hash_1301018e07b64fa0767a318ec6d0320c3f9e2c>
					<hash_1301019e7c0ec6d0025a509af6a510804c2488>
						<field_name>name</field_name>
						<data_template_id>hash_010101c84e511401a747409053c90ba910d0fe</data_template_id>
						<sequence>4</sequence>
						<text>|host_description| - Broadcast Packets - |query_ifDescr|/|query_ifIndex|</text>
					</hash_1301019e7c0ec6d0025a509af6a510804c2488>
				</sv_data_source>
			</hash_110101c5792b18bf1263b5bf3826f9196376d9>
			<hash_110101524e65b03f12b772f5c5bdad3f9dd783>
				<graph_template_id>hash_000101d4dff05337bbf42c70cb6f73647d0d2a</graph_template_id>
				<name>Interface - Multicast Packets (Legacy)</name>
				<rrd>
					<item_000>
						<snmp_field_name>ifInMulticastPkts</snmp_field_name>
						<data_template_id>hash_0101012f654f7d69ac71a5d56b1db8543ccad3</data_template_id>
						<data_template_rrd_id>hash_080101636672962b5bb2f31d86985e2ab4bdfe</data_template_rrd_id>
					</item_000>
					<item_001>
						<snmp_field_name>ifOutMulticastPkts</snmp_field_name>
						<data_template_id>hash_0101012f654f7d69ac71a5d56b1db8543ccad3</data_template_id>
						<data_template_rrd_id>hash_08010118ce92c125a236a190ee9dd948f56268</data_template_rrd_id>
					</item_001>
				</rrd>
				<sv_graph>
					<hash_120101c5e2bd31d661ba33d5169e505bf920b6>
						<field_name>title</field_name>
						<sequence>1</sequence>
						<text>|host_description| - Multicast Packets - |query_ifAlias|</text>
					</hash_120101c5e2bd31d661ba33d5169e505bf920b6>
					<hash_120101be5c494fd82964bd9bd267399c4f7a3b>
						<field_name>title</field_name>
						<sequence>2</sequence>
						<text>|host_description| - Multicast Packets - |query_ifName|</text>
					</hash_120101be5c494fd82964bd9bd267399c4f7a3b>
					<hash_120101ca3d99f3c6f8ee1e3849e28274be14ba>
						<field_name>title</field_name>
						<sequence>3</sequence>
						<text>|host_description| - Multicast Packets - |query_ifIP| (|query_ifDescr|)</text>
					</hash_120101ca3d99f3c6f8ee1e3849e28274be14ba>
					<hash_1201016f48f284918085de78181d9698fb35ad>
						<field_name>title</field_name>
						<sequence>4</sequence>
						<text>|host_description| - Multicast Packets - |query_ifDescr|/|query_ifIndex|</text>
					</hash_1201016f48f284918085de78181d9698fb35ad>
				</sv_graph>
				<sv_data_source>
					<hash_13010187418ca7ce94c355ba7bbc8625f53f92>
						<field_name>name</field_name>
						<data_template_id>hash_0101012f654f7d69ac71a5d56b1db8543ccad3</data_template_id>
						<sequence>1</sequence>
						<text>|host_description| - Multicast Packets - |query_ifAlias|</text>
					</hash_13010187418ca7ce94c355ba7bbc8625f53f92>
					<hash_130101ab0e5022e10f6529ac66772815be583f>
						<field_name>name</field_name>
						<data_template_id>hash_0101012f654f7d69ac71a5d56b1db8543ccad3</data_template_id>
						<sequence>2</sequence>
						<text>|host_description| - Multicast Packets - |query_ifName|</text>
					</hash_130101ab0e5022e10f6529ac66772815be583f>
					<hash_13010127da5a787ff471f3da8bde88f6ecd4c9>
						<field_name>name</field_name>
						<data_template_id>hash_0101012f654f7d69ac71a5d56b1db8543ccad3</data_template_id>
						<sequence>3</sequence>
						<text>|host_description| - Multicast Packets - |query_ifIP| (|query_ifDescr|)</text>
					</hash_13010127da5a787ff471f3da8bde88f6ecd4c9>
					<hash_1301013ac3c16381774c78791b5b568d06bc4f>
						<field_name>name</field_name>
						<data_template_id>hash_0101012f654f7d69ac71a5d56b1db8543ccad3</data_template_id>
						<sequence>4</sequence>
						<text>|host_description| - Multicast Packets - |query_ifDescr|/|query_ifIndex|</text>
					</hash_1301013ac3c16381774c78791b5b568d06bc4f>
				</sv_data_source>
			</hash_110101524e65b03f12b772f5c5bdad3f9dd783>
		</graphs>
	</hash_040101d75e406fdeca4fcef45b8be3a9a63cbc>
</cacti>

File: /README.md
# cacti-mikrotik-device
Simple Mikrotik device template based off of Cisco device template

compatible with cacti version 1.1.38, likely many others

monitors mikrotik total CPU load via SNMP OID .1.3.6.1.4.1.2021.11.10.0

monitors uptime via SNMP OID .1.3.6.1.2.1.1.3.0

monitors interface traffic via standard IFMIB OID


