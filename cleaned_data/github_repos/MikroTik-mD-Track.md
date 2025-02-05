# Repository Information
Name: MikroTik-mD-Track

# Directory Structure
Directory structure:
└── github_repos/MikroTik-mD-Track/
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
    │   │       │   └── main
    │   │       └── remotes/
    │   │           └── origin/
    │   │               └── HEAD
    │   ├── objects/
    │   │   ├── info/
    │   │   └── pack/
    │   │       ├── pack-9899b123af014fcf1014352f52b61a45f74456d1.idx
    │   │       └── pack-9899b123af014fcf1014352f52b61a45f74456d1.pack
    │   ├── packed-refs
    │   └── refs/
    │       ├── heads/
    │       │   └── main
    │       ├── remotes/
    │       │   └── origin/
    │       │       └── HEAD
    │       └── tags/
    ├── antennas_mikrotik.mat
    ├── Example.m
    ├── Example_data/
    │   ├── csi_measurements.txt
    │   ├── ftm_measurements.txt
    │   └── oscillator.mat
    ├── Generate_calibration.m
    ├── How to calibrate.md
    ├── LICENSE.txt
    ├── mD-Track/
    │   ├── Grid_AoA.m
    │   ├── Individual_Azimuth_Elevation_Estimator.m
    │   ├── Jointly_Azimuth_Elevation_Estimator.m
    │   ├── Jointly_Azimuth_Elevation_Estimator_Faster.m
    │   └── mD_track_2D.m
    ├── Parse_csi.m
    ├── Parse_ftm.m
    ├── README.md
    └── Sanitize.m


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
	url = https://github.com/IMDEANetworksWNG/MikroTik-mD-Track.git
	fetch = +refs/heads/*:refs/remotes/origin/*
[branch "main"]
	remote = origin
	merge = refs/heads/main


File: /.git\description
Unnamed repository; edit this file 'description' to name the repository.


File: /.git\HEAD
ref: refs/heads/main


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
0000000000000000000000000000000000000000 6f064b9a670fab8ff7d8dc0e17d2ef28e95050ba vivek-dodia <vivek.dodia@icloud.com> 1738606062 -0500	clone: from https://github.com/IMDEANetworksWNG/MikroTik-mD-Track.git


File: /.git\logs\refs\heads\main
0000000000000000000000000000000000000000 6f064b9a670fab8ff7d8dc0e17d2ef28e95050ba vivek-dodia <vivek.dodia@icloud.com> 1738606062 -0500	clone: from https://github.com/IMDEANetworksWNG/MikroTik-mD-Track.git


File: /.git\logs\refs\remotes\origin\HEAD
0000000000000000000000000000000000000000 6f064b9a670fab8ff7d8dc0e17d2ef28e95050ba vivek-dodia <vivek.dodia@icloud.com> 1738606062 -0500	clone: from https://github.com/IMDEANetworksWNG/MikroTik-mD-Track.git


File: /.git\packed-refs
# pack-refs with: peeled fully-peeled sorted 
6f064b9a670fab8ff7d8dc0e17d2ef28e95050ba refs/remotes/origin/main


File: /.git\refs\heads\main
6f064b9a670fab8ff7d8dc0e17d2ef28e95050ba


File: /.git\refs\remotes\origin\HEAD
ref: refs/remotes/origin/main


File: /Example.m
%%
close all
clear all

% Load the position of the MikroTik antennas
load('antennas_mikrotik.mat')

addpath("mD-Track/")

% Calibration
att = 1e-1;

% Number of samples gathered for CSI
num_samples = 250;

% number of antennas
N = 6;

% frequency
freq = 60.48e9;

% speed of light
c = 3e8;

% the wavelength
lambda = c/freq;

% distance between antennas
d = lambda*0.58;

% step for the angle
step_angle = 1;

% take the codebook
[cb_az, theta_az] = Grid_AoA(step_angle, N,d,lambda);
[cb_el, theta_el] = Grid_AoA(step_angle, N,d,lambda);

% Load the oscillator
load('Example_data/oscillator.mat')


% Set up the folders
currentFolder = pwd;
csi_filename = [pwd '/Example_data/csi_measurements.txt'];
ftm_filename = [pwd '/Example_data/ftm_measurements.txt'];
%% CSI
[magnitudes, phases, ~] = Parse_csi(csi_filename);

% Clean the data
pre_channel = zeros(6, 6, num_samples);

% We go up to 30 instead of 32
% so that 31 and 32 are disabled
% since they return random data
for jj=1:30

    a = phases(:, jj);
    a = a*2*pi/1024;
    
    % Move to complex domain
    a = exp(1i*a);

    
    converging_limit = 50;
    converging_retries = 0;
    converged = 0;
    
    % Sometimes it does not converge at first since the seed is random
    while converged == 0

        try
            [a, phase_offset_0, converged] = Sanitize(a);
        catch
            disp(['Converging error on file ' csi_filename])
        end

        if converging_retries == converging_limit

            break
        end

        converging_retries = converging_retries + 1;
    end

    if converging_retries == converging_limit
        disp(['Converging threshold reached, ignoring ' csi_filename])
        continue
    end

    % Remove oscilator
    a = a/exp(1i*antenna_oscilator_phases(antenna_positions == jj));

    [row,col] = find(antenna_positions == jj);
    pre_channel(row, col, :) = a(1:num_samples, :);
end

csi_data = pre_channel;

% Average over the number of samples
csi_data = sum(csi_data,3)/num_samples;

% Apply mD-Track
[Az_estimated, El_estimated, att] = mD_track_2D(csi_data.', cb_az, cb_el);

% move argument to angles
Az_estimated = rad2deg(theta_az(Az_estimated));
El_estimated = rad2deg(theta_el(El_estimated));


% re-estimate azimuth. More info at this paper: Uniform Rectangular Antenna Array Design and Calibration Issues for 2-D ESPRIT Application
Az_estimated_2 = asind(sind(Az_estimated) ./ cosd(El_estimated));

% Power
power = abs(att).^2;

%% FTM
ftm_times = Parse_ftm(ftm_filename);

% Create a histogram
distances = zeros(size(ftm_times, 1), 1);

for i=1:size(ftm_times, 1)

    % Calculate the distance in meters
    T1 = ftm_times(i, 1);
    T2 = ftm_times(i, 2);
    T3 = ftm_times(i, 3);
    T4 = ftm_times(i, 4);

    dist = 3e8 * (((T4-T1)-(T3-T2))*1e-12)/2;

    distances(i, 1) = dist;
end

distance = median(distances) - antenna_ftm_offset;


%% Nice display

clc
disp(['Main path has an azimut of ' num2str(Az_estimated(1)) ' degrees, an elevation of ' num2str(El_estimated(1)) ' degrees and a power of ' num2str(power(1))])
disp(['The other router is at ' num2str(distance) ' meters'])


File: /Example_data\csi_measurements.txt

[ 659.770366] [AOA] Measurement: 0,1626941839.561276,04:ce:14:0b:84:6c,2,1,1,0,128,93,99,62,373,953,786,381,583,660,497,15,1019,221,724,329,128,284,171,975,136,181,905,985,1020,305,887,544,607,721,920,1012,207,38,82,98,30,16,65,41,76,53,16,59,75,20,25,20,16,68,107,89,13,21,35,62,22,25,63,40,78,60,75,97,99
[ 659.800106] [AOA] Measurement: 0,1626941839.591017,04:ce:14:0b:84:6c,2,1,1,0,128,124,110,508,480,1009,836,946,749,636,471,28,49,154,777,362,899,782,987,339,658,375,224,600,15,734,32,539,538,592,863,175,460,34,69,88,31,15,63,40,79,47,25,44,67,20,20,19,17,49,96,79,17,12,5,53,29,24,53,29,70,62,79,82,86
[ 659.829486] [AOA] Measurement: 0,1626941839.620396,04:ce:14:0b:84:6c,2,1,1,0,128,641,1009,659,588,482,910,412,619,606,485,28,25,211,772,319,955,815,34,782,972,801,73,585,128,730,25,596,636,599,834,115,391,38,82,88,22,15,58,30,61,54,6,72,76,19,28,11,26,87,99,91,30,37,67,69,20,29,66,52,82,54,70,94,106
[ 659.853134] [AOA] Measurement: 0,1626941839.644049,04:ce:14:0b:84:6c,2,1,1,0,128,207,225,635,563,494,12,1015,790,626,456,113,68,223,754,339,62,336,227,938,116,28,763,542,258,800,13,988,355,117,675,192,450,37,82,88,21,15,59,30,60,52,7,72,76,19,28,12,26,88,100,90,29,37,67,69,20,30,64,53,84,56,71,94,106
[ 659.893310] [AOA] Measurement: 0,1626941839.684227,04:ce:14:0b:84:6c,2,1,1,0,128,582,950,73,363,583,39,865,763,586,452,1005,39,208,775,368,891,265,114,271,658,376,224,571,1019,697,31,573,557,572,863,848,61,44,103,126,42,23,84,50,98,61,26,71,91,25,30,17,26,83,133,111,13,22,28,76,33,32,78,47,96,79,101,112,120
[ 659.923172] [AOA] Measurement: 0,1626941839.714082,04:ce:14:0b:84:6c,2,1,1,0,128,56,83,507,528,520,983,890,744,999,181,506,890,734,625,878,702,323,148,821,842,394,257,521,857,653,1012,1011,300,1006,607,388,713,38,81,85,19,16,56,25,55,52,7,71,73,17,28,11,27,87,96,88,33,39,72,67,20,29,65,54,83,53,68,89,103
[ 659.949929] [AOA] Measurement: 0,1626941839.740843,04:ce:14:0b:84:6c,2,1,1,0,128,240,248,586,552,477,1009,11,809,568,398,27,27,644,531,334,32,755,1010,1018,195,151,813,512,220,849,53,934,368,650,841,504,742,24,46,68,27,21,56,43,66,29,28,18,49,20,10,14,16,25,65,56,34,9,26,38,43,14,42,15,45,48,62,56,59
[ 659.977331] [AOA] Measurement: 0,1626941839.768242,04:ce:14:0b:84:6c,2,1,1,0,128,203,210,656,564,484,984,1015,751,81,264,41,40,190,707,367,51,342,248,861,83,639,598,27,41,792,20,499,570,684,897,850,991,37,85,97,30,16,65,38,74,52,16,64,76,20,27,13,23,77,108,91,16,25,43,67,20,25,64,46,84,62,79,94,103
[ 660.000553] [AOA] Measurement: 0,1626941839.791468,04:ce:14:0b:84:6c,2,1,1,0,128,678,38,115,323,451,985,1000,806,20,198,56,28,145,591,858,925,764,2,413,968,555,598,9,67,843,53,492,650,714,905,652,819,39,87,92,26,16,61,32,66,54,9,70,78,19,29,12,25,84,102,90,25,32,60,66,18,28,64,51,84,57,74,93,107
[ 660.032979] [AOA] Measurement: 0,1626941839.823888,04:ce:14:0b:84:6c,2,1,1,0,128,622,950,44,364,466,965,362,535,1011,216,522,891,666,572,798,753,782,988,327,705,337,220,1013,870,179,845,59,421,54,619,349,785,35,73,102,37,23,76,56,94,44,34,37,71,23,17,18,17,44,103,86,33,12,20,59,48,22,66,25,69,66,83,86,92
[ 660.062855] [AOA] Measurement: 0,1626941839.853764,04:ce:14:0b:84:6c,2,1,1,0,128,729,51,597,512,449,994,38,845,638,489,68,13,156,747,810,864,804,39,360,929,615,612,7,30,858,50,463,537,132,683,225,461,39,84,97,30,17,66,39,73,51,13,65,79,18,27,14,22,78,107,92,19,27,48,66,21,25,67,45,82,59,75,95,105
[ 660.086117] [AOA] Measurement: 0,1626941839.877034,04:ce:14:0b:84:6c,2,1,1,0,128,239,286,651,584,418,980,36,826,573,407,50,76,76,705,383,56,351,237,934,134,96,770,522,199,890,30,464,585,697,885,138,350,27,36,58,22,19,52,49,59,22,26,13,42,13,7,12,10,18,57,50,37,7,28,37,44,11,42,11,35,35,49,56,54
[ 660.116104] [AOA] Measurement: 0,1626941839.907021,04:ce:14:0b:84:6c,2,1,1,0,128,637,966,26,366,998,801,378,567,7,234,500,883,729,619,860,700,800,22,277,694,816,37,27,926,164,820,36,365,77,639,584,911,39,84,97,29,17,62,37,68,53,11,68,79,18,29,13,25,81,104,91,24,31,56,68,19,28,66,49,84,56,73,93,105
[ 660.143068] [AOA] Measurement: 0,1626941839.933979,04:ce:14:0b:84:6c,2,1,1,0,128,230,209,604,544,426,992,493,640,60,230,491,848,626,557,859,880,782,1,381,940,610,595,18,83,846,64,476,571,634,816,158,516,37,80,95,31,16,66,42,77,49,20,57,76,17,24,14,20,66,104,88,11,18,25,61,26,23,64,40,76,61,73,88,99
[ 660.172635] [AOA] Measurement: 0,1626941839.963546,04:ce:14:0b:84:6c,2,1,1,0,128,130,93,575,520,513,976,926,781,569,390,25,26,147,720,394,898,287,146,777,809,436,233,611,927,573,32,578,569,1016,615,427,734,34,56,87,30,21,71,58,86,33,35,22,57,18,11,14,16,29,86,71,42,10,30,51,53,15,58,17,55,53,69,75,74
[ 660.202480] [AOA] Measurement: 0,1626941839.993390,04:ce:14:0b:84:6c,2,1,1,0,128,235,209,573,507,922,776,421,608,31,274,530,911,638,522,829,777,757,994,363,966,739,487,579,165,805,43,507,592,146,724,179,462,33,67,86,31,17,65,47,78,42,24,36,63,15,18,15,13,47,93,76,19,11,0,52,34,21,59,27,62,56,71,77,83
[ 660.232513] [AOA] Measurement: 0,1626941840.023430,04:ce:14:0b:84:6c,2,1,1,0,128,154,159,577,569,499,942,351,559,1015,232,471,874,623,545,863,687,862,991,807,804,811,52,591,17,631,1000,607,568,990,613,798,46,39,86,97,29,16,64,37,73,54,13,66,79,18,28,14,22,77,108,90,18,26,44,67,20,25,66,45,82,59,76,93,102
[ 660.256639] [AOA] Measurement: 0,1626941840.047555,04:ce:14:0b:84:6c,2,1,1,0,128,174,147,542,483,990,789,369,556,26,249,456,856,692,596,881,744,766,992,264,684,820,60,575,113,753,34,1013,346,86,638,444,845,40,85,92,26,16,60,33,64,53,9,72,78,18,29,13,26,83,104,92,28,32,60,68,20,26,66,49,84,56,72,95,105
[ 660.286065] [AOA] Measurement: 0,1626941840.076976,04:ce:14:0b:84:6c,2,1,1,0,128,588,955,998,335,1002,811,369,570,41,243,511,905,156,755,938,721,287,108,820,834,369,252,569,983,688,1006,573,537,1006,611,469,833,37,85,97,29,17,64,38,72,53,12,68,78,16,28,13,23,80,106,92,22,28,52,66,21,27,67,48,83,59,74,96,105
[ 660.316165] [AOA] Measurement: 0,1626941840.107082,04:ce:14:0b:84:6c,2,1,1,0,128,194,198,637,549,930,835,460,601,65,222,78,79,90,725,429,115,372,252,897,89,160,785,491,209,341,887,986,376,142,711,677,962,38,83,94,25,17,60,33,63,52,6,71,78,17,30,12,27,86,102,91,30,35,68,68,20,28,67,53,85,54,70,94,106
[ 660.341611] [AOA] Measurement: 0,1626941840.132521,04:ce:14:0b:84:6c,2,1,1,0,128,740,60,142,430,465,1005,13,826,540,377,467,889,588,553,893,927,822,1018,377,967,605,597,971,49,338,878,475,579,738,972,510,725,46,95,114,36,19,74,52,87,61,18,72,93,19,32,18,24,87,127,106,17,27,47,75,27,29,77,51,93,68,87,109,119
[ 660.373250] [AOA] Measurement: 0,1626941840.164161,04:ce:14:0b:84:6c,2,1,1,0,128,174,113,617,526,505,978,334,577,630,503,38,74,160,724,420,917,294,153,804,830,393,229,600,980,658,37,552,570,584,821,640,871,36,75,91,30,16,65,48,80,46,19,50,73,12,24,18,14,55,100,80,10,16,14,58,29,21,62,31,67,56,69,84,90
[ 660.408900] [AOA] Measurement: 0,1626941840.199789,04:ce:14:0b:84:6c,2,1,1,0,128,189,147,602,547,493,949,946,788,619,485,34,34,190,772,407,971,312,195,892,1000,367,281,567,129,695,1022,549,610,60,660,406,667,37,75,94,32,17,63,47,79,46,19,54,75,13,25,17,16,60,104,84,11,18,25,62,25,23,66,37,73,58,71,92,99
[ 660.436967] [AOA] Measurement: 0,1626941840.227882,04:ce:14:0b:84:6c,2,1,1,0,128,705,1012,602,557,526,998,398,624,19,289,57,41,212,779,405,942,803,1015,808,804,383,247,557,57,691,12,603,621,569,826,157,471,45,85,107,38,19,74,58,95,52,25,56,87,14,27,24,17,60,114,92,17,18,11,64,35,25,71,35,74,63,81,101,105
[ 660.465494] [AOA] Measurement: 0,1626941840.256411,04:ce:14:0b:84:6c,2,1,1,0,128,159,179,565,549,514,1011,928,756,597,372,1004,19,703,588,857,723,804,970,758,799,296,175,83,725,640,1013,584,567,521,820,85,351,33,49,65,25,16,52,49,69,28,24,24,55,6,15,20,11,26,73,55,35,12,16,39,42,15,46,15,36,41,54,63,63
[ 660.493518] [AOA] Measurement: 0,1626941840.284428,04:ce:14:0b:84:6c,2,1,1,0,128,593,990,984,300,952,768,383,569,72,335,1007,34,215,771,858,693,776,968,789,812,870,99,602,15,700,986,945,309,75,686,834,113,33,54,72,28,17,56,50,73,33,25,30,62,9,17,21,12,34,85,64,26,14,5,51,36,20,53,23,52,50,64,80,79
[ 660.523285] [AOA] Measurement: 0,1626941840.314197,04:ce:14:0b:84:6c,2,1,1,0,128,185,231,702,629,486,1019,984,823,564,448,28,25,285,695,367,37,353,215,1000,159,151,839,538,234,830,16,558,659,721,915,128,283,38,80,85,20,15,56,28,57,51,5,71,69,17,29,12,26,87,99,88,32,38,73,65,21,30,63,54,83,53,67,93,104
[ 660.553625] [AOA] Measurement: 0,1626941840.344535,04:ce:14:0b:84:6c,2,1,1,0,128,67,92,1020,294,459,977,947,821,641,515,34,38,177,755,365,905,805,1003,844,817,338,179,623,33,701,26,575,591,680,903,112,387,38,82,90,24,16,58,32,64,52,7,69,74,17,29,12,27,87,101,89,31,36,69,67,22,28,65,50,83,53,69,96,104
[ 660.578121] [AOA] Measurement: 0,1626941840.369036,04:ce:14:0b:84:6c,2,1,1,0,128,184,177,552,560,523,1020,903,721,84,305,1022,47,177,736,877,700,750,937,821,822,828,76,40,867,702,1022,1003,354,579,860,945,196,39,84,92,27,17,62,34,66,51,10,70,74,17,29,14,25,84,104,91,25,33,61,67,21,27,64,49,84,54,70,98,104
[ 660.610794] [AOA] Measurement: 0,1626941840.401708,04:ce:14:0b:84:6c,2,1,1,0,128,197,202,679,555,439,980,914,755,619,494,1003,12,672,472,833,848,303,209,860,83,192,852,529,156,814,50,493,594,704,895,270,463,27,50,63,25,19,53,46,65,23,26,18,52,8,13,22,10,23,62,52,39,14,23,39,39,16,38,17,41,44,60,61,63
[ 660.637677] [AOA] Measurement: 0,1626941840.428587,04:ce:14:0b:84:6c,2,1,1,0,128,145,158,548,495,944,856,968,800,41,248,470,830,675,507,354,1005,285,186,852,70,697,731,497,159,250,854,502,572,97,678,887,136,47,109,119,34,21,79,45,89,64,18,80,93,21,34,18,28,98,131,114,23,31,59,82,26,33,81,55,103,73,92,126,129
[ 660.668873] [AOA] Measurement: 0,1626941840.459790,04:ce:14:0b:84:6c,2,1,1,0,128,637,966,45,359,489,970,954,800,618,487,64,64,213,769,374,944,303,142,770,804,358,177,587,958,615,6,515,522,50,671,724,1023,28,59,74,29,21,59,44,70,31,27,26,59,10,16,19,12,37,79,63,32,13,13,48,34,21,46,22,53,52,67,71,75
[ 660.693522] [AOA] Measurement: 0,1626941840.484432,04:ce:14:0b:84:6c,2,1,1,0,128,662,956,997,288,1008,808,355,566,49,312,514,858,631,566,815,691,771,979,812,780,813,56,638,29,644,1004,1015,355,41,626,693,10,39,86,95,29,18,62,36,70,53,11,66,75,18,28,14,23,80,106,90,23,30,55,66,21,26,66,49,85,56,72,98,105
[ 660.726136] [AOA] Measurement: 0,1626941840.517046,04:ce:14:0b:84:6c,2,1,1,0,128,132,111,1010,316,921,746,355,629,612,476,20,78,168,743,817,675,792,955,240,606,836,992,26,706,123,857,577,581,578,866,112,363,46,105,112,27,20,75,38,75,65,7,88,92,21,36,14,33,111,126,112,41,48,87,84,26,37,79,66,103,64,83,118,130
[ 660.751213] [AOA] Measurement: 0,1626941840.542131,04:ce:14:0b:84:6c,2,1,1,0,128,89,126,53,390,904,773,458,572,76,282,34,86,189,723,834,752,285,196,865,108,179,18,540,172,754,43,526,646,576,842,499,789,42,101,115,36,20,74,43,84,59,18,74,88,18,31,16,26,87,128,108,17,27,46,75,24,29,73,51,94,67,89,115,124
[ 660.777360] [AOA] Measurement: 0,1626941840.568277,04:ce:14:0b:84:6c,2,1,1,0,128,128,99,969,293,942,757,390,567,4,146,510,891,189,744,408,934,248,116,817,751,371,197,562,929,69,841,593,523,501,788,1012,248,28,55,72,27,24,65,51,71,24,32,20,58,5,11,20,13,28,71,63,46,16,30,47,46,19,46,19,49,53,71,69,74
[ 660.808171] [AOA] Measurement: 0,1626941840.599082,04:ce:14:0b:84:6c,2,1,1,0,128,117,105,595,604,485,999,924,752,545,419,430,867,665,561,906,698,249,104,770,801,834,51,640,980,594,974,541,509,579,860,962,200,37,89,109,41,24,83,54,92,46,33,48,81,15,23,21,20,60,120,95,24,18,4,69,36,28,69,38,83,71,91,106,111
[ 660.832960] [AOA] Measurement: 0,1626941840.623873,04:ce:14:0b:84:6c,2,1,1,0,128,676,1023,122,388,888,811,982,800,611,428,479,839,697,518,832,779,344,190,937,129,200,868,589,209,852,30,470,570,696,899,928,113,43,101,112,32,20,72,41,81,59,14,78,87,18,32,15,27,94,126,107,24,33,62,79,23,32,76,55,98,66,85,115,124
[ 660.866694] [AOA] Measurement: 0,1626941840.657604,04:ce:14:0b:84:6c,2,1,1,0,128,188,196,614,562,810,767,479,651,46,240,460,824,744,468,870,799,785,17,896,75,138,843,528,222,811,42,503,603,673,894,743,996,31,58,77,27,21,69,54,75,30,34,22,61,8,14,20,10,38,91,76,38,15,23,52,44,18,53,24,58,58,75,71,76
[ 660.892345] [AOA] Measurement: 0,1626941840.683260,04:ce:14:0b:84:6c,2,1,1,0,128,699,44,84,331,879,828,521,615,613,396,947,1019,896,367,779,864,873,88,997,138,1022,824,971,86,881,35,442,627,700,888,572,820,31,62,85,30,22,69,53,77,30,34,21,60,10,11,20,9,32,85,68,41,15,25,50,44,18,54,23,55,57,75,73,77
[ 660.923801] [AOA] Measurement: 0,1626941840.714713,04:ce:14:0b:84:6c,2,1,1,0,128,198,230,629,506,386,967,4,790,625,476,981,7,240,635,859,863,366,222,327,891,85,851,512,245,849,37,449,593,669,874,718,0,32,66,85,31,22,72,54,80,37,32,28,65,9,16,18,13,45,98,78,35,15,18,55,40,22,59,27,65,63,80,84,90
[ 660.954507] [AOA] Measurement: 0,1626941840.745417,04:ce:14:0b:84:6c,2,1,1,0,128,691,19,581,522,894,767,511,641,642,464,1022,38,218,711,397,939,780,2,334,909,159,868,564,205,793,19,518,582,715,907,619,847,38,86,98,31,17,65,39,74,51,14,62,74,16,26,12,21,75,109,90,16,23,42,63,19,25,64,44,79,58,75,96,103
[ 660.983918] [AOA] Measurement: 0,1626941840.774834,04:ce:14:0b:84:6c,2,1,1,0,128,163,116,518,520,997,839,417,581,26,247,504,880,662,616,876,713,766,948,274,630,359,206,559,976,21,810,617,561,559,838,534,795,29,58,79,28,18,64,47,70,35,27,29,59,10,16,17,9,40,84,68,25,11,12,49,34,18,52,26,59,55,69,72,78
[ 661.011104] [AOA] Measurement: 0,1626941840.802015,04:ce:14:0b:84:6c,2,1,1,0,128,253,237,602,512,357,999,1011,815,624,441,52,28,261,610,383,9,316,198,881,48,624,643,997,38,859,63,529,599,689,906,880,1015,42,99,114,35,18,77,46,86,60,16,72,87,18,30,13,26,88,128,106,20,29,53,74,22,30,77,53,97,67,86,113,124
[ 661.042160] [AOA] Measurement: 0,1626941840.833074,04:ce:14:0b:84:6c,2,1,1,0,128,691,992,1002,300,957,797,389,578,60,251,462,859,704,594,453,929,337,158,862,850,306,204,617,87,745,68,550,535,596,832,142,388,38,87,95,29,15,62,37,70,53,12,65,75,16,27,12,23,79,107,91,20,28,52,65,18,26,67,47,82,57,76,96,103
[ 661.067082] [AOA] Measurement: 0,1626941840.857999,04:ce:14:0b:84:6c,2,1,1,0,128,701,53,650,521,821,792,495,639,87,248,487,887,813,497,414,160,332,232,952,84,516,610,961,41,294,826,930,390,183,732,899,157,33,49,76,21,18,67,61,77,29,35,14,59,10,9,22,2,29,83,68,48,14,37,48,53,13,51,21,53,54,70,68,71
[ 661.095912] [AOA] Measurement: 0,1626941840.886822,04:ce:14:0b:84:6c,2,1,1,0,128,236,248,686,518,319,981,1023,855,649,434,31,39,347,666,413,341,346,245,986,142,71,784,504,264,904,82,430,556,760,920,577,781,37,85,97,28,15,63,39,70,52,13,66,76,16,28,14,23,81,106,89,22,29,55,66,19,27,65,48,82,58,73,96,105
[ 661.121951] [AOA] Measurement: 0,1626941840.912867,04:ce:14:0b:84:6c,2,1,1,0,128,622,978,29,369,473,928,382,560,55,269,56,87,279,798,455,868,248,105,841,844,871,80,1015,809,143,852,598,599,572,869,570,888,32,48,69,21,13,61,50,70,32,28,24,55,15,13,21,4,33,80,66,28,10,16,45,37,15,54,22,55,52,65,71,73
[ 661.151800] [AOA] Measurement: 0,1626941840.942717,04:ce:14:0b:84:6c,2,1,1,0,128,193,144,523,531,560,1010,864,747,634,464,14,40,663,559,430,890,305,168,810,821,375,210,598,950,704,47,593,583,600,860,596,731,38,82,95,25,15,61,34,65,53,7,69,77,17,28,13,24,84,101,88,27,31,59,67,20,27,66,49,83,57,72,96,108
[ 661.176380] [AOA] Measurement: 0,1626941840.967297,04:ce:14:0b:84:6c,2,1,1,0,128,659,964,1020,306,952,802,388,604,1018,233,516,875,214,761,314,875,341,179,773,788,893,73,619,40,657,15,565,601,575,806,944,200,38,86,95,26,14,62,38,69,52,9,68,78,18,27,15,21,81,105,90,22,29,53,66,20,25,67,47,81,58,72,93,104
[ 661.203537] [AOA] Measurement: 0,1626941840.994451,04:ce:14:0b:84:6c,2,1,1,0,128,256,257,638,610,509,996,930,757,611,463,1008,46,239,744,399,155,361,190,937,124,151,809,596,214,933,60,523,591,692,906,316,546,38,85,90,23,15,59,34,62,51,6,71,76,18,29,12,24,86,100,88,31,35,70,67,20,29,65,52,83,53,68,92,105
[ 661.243422] [AOA] Measurement: 0,1626941841.034338,04:ce:14:0b:84:6c,2,1,1,0,128,624,967,524,526,542,980,984,785,640,434,20,40,204,753,477,927,707,945,214,556,847,68,54,746,117,867,565,497,522,821,682,1002,45,99,111,31,20,72,43,80,61,10,82,91,21,33,17,27,99,122,108,31,39,71,80,24,32,78,58,99,65,85,113,123
[ 661.273826] [AOA] Measurement: 0,1626941841.064741,04:ce:14:0b:84:6c,2,1,1,0,128,637,1022,63,364,942,766,447,612,609,486,25,37,212,704,838,888,329,186,854,87,640,620,51,5,851,9,958,393,134,702,896,137,37,81,89,22,15,60,32,61,52,5,72,75,18,29,12,25,88,96,88,33,38,73,67,21,30,64,53,83,53,68,92,104
[ 661.300465] [AOA] Measurement: 0,1626941841.091376,04:ce:14:0b:84:6c,2,1,1,0,128,611,947,1018,309,997,827,395,609,59,251,548,906,189,767,835,722,290,185,838,867,309,203,588,50,108,823,595,572,91,669,459,716,27,49,67,29,19,53,41,66,29,30,22,50,14,15,15,20,27,68,54,33,9,17,39,41,17,44,16,43,45,59,60,63
[ 661.332108] [AOA] Measurement: 0,1626941841.123023,04:ce:14:0b:84:6c,2,1,1,0,128,200,214,62,353,422,974,502,639,567,404,3,37,119,678,361,0,785,30,918,112,53,718,1012,69,771,34,516,596,707,894,586,816,39,85,93,27,17,61,34,67,53,10,67,76,17,28,12,25,82,105,91,24,31,58,66,19,27,65,49,84,57,73,95,106
[ 661.356505] [AOA] Measurement: 0,1626941841.147419,04:ce:14:0b:84:6c,2,1,1,0,128,642,956,25,327,465,959,387,546,622,482,458,859,626,557,901,727,803,976,236,709,783,43,20,873,279,892,532,521,57,663,431,789,44,103,124,41,21,81,51,96,60,20,73,95,20,32,18,27,89,135,113,16,26,39,80,29,31,79,51,98,75,95,118,129
[ 661.386824] [AOA] Measurement: 0,1626941841.177735,04:ce:14:0b:84:6c,2,1,1,0,128,125,128,536,551,506,946,940,751,591,458,12,54,163,742,875,692,287,102,203,621,807,19,594,960,95,819,39,329,1022,643,44,303,38,83,94,27,17,62,34,66,53,9,68,76,18,29,11,25,84,104,90,26,33,62,68,19,30,65,52,85,55,71,93,105
[ 661.417235] [AOA] Measurement: 0,1626941841.208152,04:ce:14:0b:84:6c,2,1,1,0,128,255,255,574,554,475,12,971,768,653,453,2,22,220,709,390,989,815,1017,884,93,167,797,560,158,834,26,533,611,649,883,656,830,37,85,94,28,18,62,36,69,50,11,67,75,16,29,12,23,80,106,89,23,29,52,67,20,26,64,47,82,57,73,93,105
[ 661.444545] [AOA] Measurement: 0,1626941841.235455,04:ce:14:0b:84:6c,2,1,1,0,128,681,16,97,325,428,992,471,608,1001,170,451,810,597,377,862,984,814,38,959,90,1019,762,950,6,340,810,856,363,187,705,679,1000,42,100,110,31,20,71,41,79,61,11,80,90,18,32,13,29,98,126,106,29,37,65,77,23,31,75,57,99,66,86,112,126
[ 661.476677] [AOA] Measurement: 0,1626941841.267594,04:ce:14:0b:84:6c,2,1,1,0,128,709,48,122,329,398,1016,463,649,25,193,419,811,454,338,843,950,852,46,400,917,520,636,962,67,418,832,403,594,754,909,201,390,29,52,75,27,23,68,54,70,28,33,16,55,5,13,14,8,30,82,68,39,15,24,50,45,17,53,19,55,51,70,76,76
[ 661.502574] [AOA] Measurement: 0,1626941841.293484,04:ce:14:0b:84:6c,2,1,1,0,128,124,111,527,508,936,766,395,570,1023,210,487,853,219,773,455,922,294,115,778,790,893,37,573,921,654,1019,550,544,523,789,373,672,44,100,111,31,19,71,44,79,61,10,79,90,17,32,15,26,98,123,106,28,34,67,77,22,30,76,56,97,64,84,114,123
[ 661.531560] [AOA] Measurement: 0,1626941841.322474,04:ce:14:0b:84:6c,2,1,1,0,128,747,56,91,351,898,816,461,666,79,223,534,893,421,633,422,258,850,70,1005,126,527,605,896,1,444,908,447,610,734,946,277,519,39,84,95,27,15,60,37,68,52,9,67,77,16,26,15,22,81,106,91,24,32,58,66,19,25,66,48,83,56,71,95,103
[ 661.562599] [AOA] Measurement: 0,1626941841.353512,04:ce:14:0b:84:6c,2,1,1,0,128,572,929,0,355,1018,822,348,560,34,241,37,65,195,797,441,900,347,189,807,807,344,194,584,918,615,1021,571,541,549,838,495,814,48,99,113,33,18,76,47,87,65,14,77,91,21,32,20,23,91,129,107,23,31,60,76,22,30,77,54,97,68,88,113,125
[ 661.595003] [AOA] Measurement: 0,1626941841.385916,04:ce:14:0b:84:6c,2,1,1,0,128,147,148,502,525,509,991,933,752,42,260,507,900,190,767,420,951,344,181,817,888,420,301,548,75,107,835,560,597,570,840,841,118,38,85,95,27,17,61,36,68,50,10,68,78,17,29,14,23,80,107,89,22,27,51,65,20,24,65,47,82,56,73,95,106
[ 661.620303] [AOA] Measurement: 0,1626941841.411218,04:ce:14:0b:84:6c,2,1,1,0,128,122,134,545,546,516,996,930,764,653,503,1008,6,694,548,921,780,787,966,827,860,822,67,585,40,148,799,1021,349,616,851,950,266,39,83,96,29,16,64,38,70,53,11,66,76,16,29,14,22,82,105,91,24,30,56,65,20,26,65,46,84,55,70,96,105
[ 661.647131] [AOA] Measurement: 0,1626941841.438046,04:ce:14:0b:84:6c,2,1,1,0,128,619,1005,26,355,930,762,452,612,56,281,497,893,259,794,373,1005,301,120,927,25,268,251,560,124,243,859,998,338,68,671,646,959,38,83,93,25,16,61,35,65,53,10,69,75,18,27,15,22,82,105,89,24,31,55,67,18,25,65,46,81,55,71,95,104
[ 661.678902] [AOA] Measurement: 0,1626941841.469817,04:ce:14:0b:84:6c,2,1,1,0,128,211,167,577,543,560,977,838,737,38,178,539,906,216,765,868,718,767,994,762,799,383,183,597,930,591,1019,573,533,995,617,315,564,43,85,89,17,17,64,29,57,57,6,84,81,20,33,13,32,103,106,97,43,47,90,77,26,37,75,65,92,57,74,105,114
[ 661.704170] [AOA] Measurement: 0,1626941841.495086,04:ce:14:0b:84:6c,2,1,1,0,128,189,164,634,584,421,978,455,594,612,440,1023,44,64,680,337,1004,300,193,876,127,220,828,545,149,792,13,604,628,661,858,207,443,30,71,92,38,25,73,46,81,35,37,35,66,17,23,12,23,47,94,78,34,14,18,59,44,23,63,28,64,58,75,81,90
[ 661.736381] [AOA] Measurement: 0,1626941841.527292,04:ce:14:0b:84:6c,2,1,1,0,128,186,183,574,505,891,805,39,794,553,363,966,4,92,693,751,815,338,187,883,85,153,777,502,155,791,39,539,585,634,868,109,236,29,71,96,40,25,72,49,82,34,35,35,68,14,23,11,22,52,99,76,32,16,12,60,43,21,63,30,67,57,74,81,90
[ 661.766283] [AOA] Measurement: 0,1626941841.557197,04:ce:14:0b:84:6c,2,1,1,0,128,211,220,590,561,388,988,1012,792,537,367,19,2,99,735,226,997,325,179,901,107,173,780,515,169,815,34,564,606,694,906,622,694,42,101,112,34,18,74,40,83,58,15,76,91,19,33,14,29,93,127,107,20,32,54,78,26,30,76,54,95,67,87,115,125
[ 661.795375] [AOA] Measurement: 0,1626941841.586288,04:ce:14:0b:84:6c,2,1,1,0,128,214,210,587,525,357,955,456,579,10,187,16,32,30,664,325,931,842,13,887,83,128,754,510,161,862,69,501,590,578,857,96,267,44,100,108,28,19,71,37,73,60,10,80,88,20,33,13,30,98,121,106,31,37,71,77,24,32,77,60,98,63,84,110,124
[ 661.821544] [AOA] Measurement: 0,1626941841.612455,04:ce:14:0b:84:6c,2,1,1,0,128,611,946,575,568,486,967,923,782,12,253,2,13,141,734,881,705,778,968,250,618,340,222,545,938,115,831,47,377,551,843,652,891,43,99,114,35,20,74,46,87,58,17,71,91,17,29,16,25,89,127,105,20,30,56,74,22,28,77,52,94,65,85,113,125
[ 661.852416] [AOA] Measurement: 0,1626941841.643331,04:ce:14:0b:84:6c,2,1,1,0,128,105,103,2,331,1021,849,921,744,66,274,41,45,199,759,391,944,287,171,249,700,817,78,57,935,252,856,535,518,655,896,500,777,37,85,97,28,15,63,39,72,54,11,68,77,17,27,15,23,80,104,92,22,30,56,68,18,26,64,46,84,56,73,99,105
[ 661.879017] [AOA] Measurement: 0,1626941841.669932,04:ce:14:0b:84:6c,2,1,1,0,128,618,969,999,330,970,835,376,563,31,240,73,90,128,739,869,716,310,149,801,810,388,225,601,960,635,1018,554,515,574,846,697,20,39,59,86,26,17,74,69,85,33,28,22,70,10,13,27,0,32,96,78,38,12,22,53,48,20,65,23,55,59,76,91,92
[ 661.910774] [AOA] Measurement: 0,1626941841.701691,04:ce:14:0b:84:6c,2,1,1,0,128,644,972,1018,296,991,788,383,604,590,446,40,7,187,741,877,713,313,168,843,837,857,37,55,783,642,40,550,567,600,864,805,0,37,80,87,21,17,55,29,57,51,5,74,73,17,28,12,27,87,96,88,35,39,74,67,20,30,65,54,81,51,67,92,104
[ 661.941158] [AOA] Measurement: 0,1626941841.732069,04:ce:14:0b:84:6c,2,1,1,0,128,131,108,553,559,523,1020,969,790,575,411,29,22,183,750,468,955,318,121,766,773,383,209,614,950,646,29,541,509,545,807,672,22,38,83,93,26,16,60,33,65,52,8,70,76,18,28,13,24,85,104,91,26,33,61,68,20,28,65,50,84,55,70,98,104
[ 661.972018] [AOA] Measurement: 0,1626941841.762936,04:ce:14:0b:84:6c,2,1,1,0,128,629,925,1018,284,995,813,356,569,43,244,521,847,650,553,419,969,794,1013,256,649,801,26,550,68,714,15,559,586,629,873,285,559,31,48,68,25,15,54,43,68,28,30,21,54,10,11,20,12,28,70,57,32,10,20,43,40,14,44,18,45,42,57,61,61
[ 661.997352] [AOA] Measurement: 0,1626941841.788268,04:ce:14:0b:84:6c,2,1,1,0,128,138,111,1012,330,974,788,386,564,606,406,24,40,242,800,407,890,284,105,804,810,359,180,629,922,584,1000,586,559,472,825,1009,234,33,67,86,30,16,63,47,78,42,24,39,66,13,18,18,14,44,93,74,18,11,1,52,32,20,58,28,63,54,70,82,84
[ 662.024287] [AOA] Measurement: 0,1626941841.815204,04:ce:14:0b:84:6c,2,1,1,0,128,152,163,557,546,502,970,980,778,31,264,512,902,679,573,423,965,271,124,879,991,285,265,605,145,216,822,984,361,44,672,730,1022,37,80,85,19,15,57,28,56,51,5,72,74,17,28,12,26,87,95,88,36,38,74,66,21,30,63,55,82,50,65,92,102
[ 662.055809] [AOA] Measurement: 0,1626941841.846726,04:ce:14:0b:84:6c,2,1,1,0,128,621,974,21,356,511,971,940,787,513,412,24,77,177,728,449,948,387,189,809,811,400,231,600,979,657,999,1015,352,593,874,362,595,37,84,90,24,16,59,30,61,52,6,71,73,18,28,12,25,88,99,90,32,38,68,66,21,30,64,54,83,53,70,93,102
[ 662.086243] [AOA] Measurement: 0,1626941841.877153,04:ce:14:0b:84:6c,2,1,1,0,128,159,216,648,586,892,791,494,614,61,188,500,882,173,636,898,968,289,184,970,158,104,827,478,238,937,30,415,563,692,924,832,48,38,84,94,30,16,65,39,73,51,14,60,76,17,27,15,21,73,104,88,14,21,36,63,21,25,65,40,78,58,74,94,99
[ 662.116633] [AOA] Measurement: 0,1626941841.907551,04:ce:14:0b:84:6c,2,1,1,0,128,199,174,658,600,470,994,977,801,614,444,41,47,659,507,918,922,800,1013,841,79,157,843,528,216,796,1002,542,619,683,867,68,259,29,49,69,23,16,58,48,67,29,27,23,53,10,13,19,10,29,74,59,31,11,16,45,38,16,48,20,50,49,63,70,69
[ 662.146379] [AOA] Measurement: 0,1626941841.937290,04:ce:14:0b:84:6c,2,1,1,0,128,171,159,605,531,467,997,917,786,590,459,20,21,195,757,445,992,359,182,891,1010,284,247,548,164,804,68,562,616,613,842,29,290,30,50,68,25,16,57,47,68,29,28,22,53,11,13,17,10,27,71,56,33,12,21,41,41,16,45,19,44,45,61,61,63
[ 662.179305] [AOA] Measurement: 0,1626941841.970215,04:ce:14:0b:84:6c,2,1,1,0,128,118,102,544,522,1011,816,385,572,13,226,502,869,676,573,415,896,774,954,292,662,849,69,552,1012,164,850,956,294,78,671,4,379,49,108,119,33,20,75,45,86,65,12,87,96,22,33,17,29,103,135,117,31,38,69,84,25,34,82,59,104,70,90,123,130
[ 662.212623] [AOA] Measurement: 0,1626941842.003534,04:ce:14:0b:84:6c,2,1,1,0,128,158,158,532,546,579,1022,882,718,573,441,13,76,656,595,856,692,323,158,833,848,372,238,535,952,652,1017,635,581,539,855,529,669,27,42,59,20,17,51,46,60,23,27,12,45,10,12,18,10,19,63,50,37,10,25,38,42,13,40,13,37,40,56,55,56
[ 662.245426] [AOA] Measurement: 0,1626941842.036337,04:ce:14:0b:84:6c,2,1,1,0,128,131,149,6,334,979,797,379,555,59,300,506,887,682,592,867,718,732,960,284,728,787,56,67,942,732,25,585,586,603,865,5,280,38,83,93,27,16,60,36,70,53,10,68,77,17,28,15,24,82,107,91,24,31,58,65,20,28,66,48,83,55,72,95,104
[ 662.277655] [AOA] Measurement: 0,1626941842.068565,04:ce:14:0b:84:6c,2,1,1,0,128,548,914,1006,320,528,1008,902,773,548,400,455,844,672,611,863,676,728,920,190,542,852,24,92,784,112,837,589,561,596,835,678,956,37,84,94,27,17,61,37,69,52,10,70,78,18,28,14,23,83,104,90,24,29,56,66,20,27,64,50,84,57,70,95,101
[ 662.308084] [AOA] Measurement: 0,1626941842.098998,04:ce:14:0b:84:6c,2,1,1,0,128,183,161,523,490,1012,790,912,741,57,277,4,1,146,723,808,691,786,979,857,830,841,9,35,718,16,817,35,385,541,806,706,988,39,85,87,24,16,59,31,63,52,6,71,73,17,28,12,25,87,99,87,29,37,69,66,20,29,64,53,82,53,70,94,104
[ 662.337264] [AOA] Measurement: 0,1626941842.128174,04:ce:14:0b:84:6c,2,1,1,0,128,181,144,544,523,516,984,382,593,622,470,1022,1,688,566,430,907,281,156,839,832,399,234,576,926,639,31,530,580,582,822,316,587,40,86,94,27,17,63,36,71,52,11,68,77,17,29,13,23,82,105,90,24,30,56,66,19,27,66,50,85,56,72,97,106
[ 662.370707] [AOA] Measurement: 0,1626941842.161618,04:ce:14:0b:84:6c,2,1,1,0,128,120,122,572,598,477,966,940,753,540,468,484,878,254,815,889,692,802,966,272,656,852,48,616,952,632,7,609,602,534,827,542,778,33,70,90,32,16,65,47,77,42,22,44,70,14,21,17,13,52,97,78,13,14,10,55,28,21,60,31,66,55,72,84,89
[ 662.403295] [AOA] Measurement: 0,1626941842.194205,04:ce:14:0b:84:6c,2,1,1,0,128,136,121,566,523,491,971,861,701,39,270,109,98,158,718,420,873,261,146,792,797,871,47,564,927,629,23,579,593,567,806,792,75,39,85,94,27,16,61,34,67,53,10,71,77,18,28,14,22,82,106,89,23,31,57,66,20,26,65,48,84,57,74,96,104
[ 662.435958] [AOA] Measurement: 0,1626941842.226868,04:ce:14:0b:84:6c,2,1,1,0,128,610,965,1023,293,963,763,414,602,84,327,56,27,217,784,464,963,300,154,780,801,381,232,478,981,129,869,33,421,18,602,224,486,47,103,122,39,21,83,54,97,60,24,68,95,19,30,21,21,81,134,108,13,23,32,75,31,28,79,47,91,73,94,118,122
[ 662.469095] [AOA] Measurement: 0,1626941842.260011,04:ce:14:0b:84:6c,2,1,1,0,128,115,106,611,553,513,1012,938,779,559,438,72,65,210,792,406,896,771,972,808,819,348,245,603,1017,679,1014,530,517,608,829,85,356,31,54,72,27,16,59,45,69,33,26,30,57,13,16,19,9,38,86,67,25,11,9,48,35,17,51,24,55,50,65,73,76
[ 662.494791] [AOA] Measurement: 0,1626941842.285708,04:ce:14:0b:84:6c,2,1,1,0,128,127,126,539,507,486,996,368,579,39,260,514,886,157,716,919,708,749,966,304,636,370,258,44,835,720,11,539,508,30,626,206,423,38,85,93,26,16,63,36,69,51,9,65,75,17,27,14,22,82,106,90,21,29,53,65,20,27,65,48,83,56,71,96,103
[ 662.525217] [AOA] Measurement: 0,1626941842.316128,04:ce:14:0b:84:6c,2,1,1,0,128,160,128,521,537,530,1008,956,782,605,428,1023,8,170,763,879,734,293,104,190,568,841,41,19,757,89,844,588,547,489,796,574,925,48,107,120,34,19,78,47,88,65,14,84,97,19,35,16,28,100,135,112,27,37,65,84,25,34,83,58,105,72,92,123,131
[ 662.557400] [AOA] Measurement: 0,1626941842.348317,04:ce:14:0b:84:6c,2,1,1,0,128,598,955,607,558,505,958,908,756,612,494,0,44,189,738,456,917,269,148,807,844,374,242,614,1008,682,1002,577,573,57,668,286,558,47,103,114,29,18,75,41,79,66,9,88,96,20,36,16,30,106,130,114,36,42,81,84,26,35,81,65,104,69,88,120,135
[ 662.587349] [AOA] Measurement: 0,1626941842.378260,04:ce:14:0b:84:6c,2,1,1,0,128,637,965,38,354,490,935,861,753,607,429,988,1011,251,773,873,716,266,135,166,582,850,3,37,710,55,812,17,360,28,638,709,15,39,85,95,28,16,62,36,69,52,12,67,78,17,28,13,22,82,103,87,23,30,56,67,20,27,66,49,84,57,72,95,106
[ 662.613465] [AOA] Measurement: 0,1626941842.404375,04:ce:14:0b:84:6c,2,1,1,0,128,607,953,2,342,497,984,385,612,8,209,53,31,185,759,374,902,754,959,213,562,853,27,34,781,135,864,564,530,553,801,989,235,46,97,104,22,18,68,35,67,62,7,89,90,19,34,13,33,113,118,109,44,49,97,83,26,38,80,68,102,61,79,112,131
[ 662.646570] [AOA] Measurement: 0,1626941842.437479,04:ce:14:0b:84:6c,2,1,1,0,128,58,75,554,529,515,984,378,558,75,249,85,72,192,801,367,857,786,964,789,776,360,221,587,950,652,27,575,537,523,816,716,1000,29,49,69,23,17,56,46,66,29,28,20,54,11,12,20,12,26,73,59,33,11,17,43,39,16,47,21,49,46,61,65,66
[ 662.679422] [AOA] Measurement: 0,1626941842.470333,04:ce:14:0b:84:6c,2,1,1,0,128,151,131,517,505,529,990,367,554,4,107,1012,6,682,607,854,685,809,973,222,571,850,31,604,931,626,1003,608,562,452,770,410,787,38,85,94,27,15,64,36,71,53,14,67,76,17,28,14,23,76,108,91,19,26,48,66,20,25,65,46,83,59,73,95,105
[ 662.712369] [AOA] Measurement: 0,1626941842.503279,04:ce:14:0b:84:6c,2,1,1,0,128,574,911,532,545,478,993,933,768,608,426,1007,26,264,822,422,914,319,125,781,815,393,252,597,948,653,1010,596,544,530,798,66,356,45,100,108,29,20,70,40,75,61,10,83,90,21,33,16,29,100,121,107,33,38,73,79,23,33,77,58,98,65,84,112,124
[ 662.744377] [AOA] Measurement: 0,1626941842.535292,04:ce:14:0b:84:6c,2,1,1,0,128,615,959,585,524,497,979,874,745,69,210,29,21,235,718,866,676,793,980,297,675,384,169,588,829,68,851,581,586,518,803,842,106,34,56,76,28,22,66,56,79,30,34,18,62,12,14,22,13,27,82,67,45,14,32,47,52,18,52,19,48,53,72,74,73
[ 662.774005] [AOA] Measurement: 0,1626941842.564916,04:ce:14:0b:84:6c,2,1,1,0,128,127,118,562,548,954,781,366,564,6,247,69,47,634,544,942,732,761,955,787,780,808,2,83,811,112,818,606,589,536,822,998,223,43,95,116,38,20,79,56,95,56,27,58,87,18,26,22,17,66,126,101,18,17,12,70,37,26,75,38,83,71,89,108,113
[ 662.806701] [AOA] Measurement: 0,1626941842.597617,04:ce:14:0b:84:6c,2,1,1,0,128,170,196,637,576,447,994,950,769,664,458,38,37,227,710,321,1,329,238,939,138,153,817,548,221,773,1002,29,456,144,704,137,370,37,84,96,29,16,63,39,73,53,14,63,77,16,26,14,21,75,105,90,17,27,45,65,20,25,65,44,81,57,74,96,104
[ 662.836274] [AOA] Measurement: 0,1626941842.627183,04:ce:14:0b:84:6c,2,1,1,0,128,169,240,697,626,412,983,25,827,590,444,17,60,219,690,355,103,288,202,907,154,111,804,962,1006,899,22,518,607,671,913,43,245,38,82,87,23,16,57,30,59,53,6,71,75,16,29,12,25,86,99,87,32,36,70,67,20,29,65,53,84,54,69,91,105
[ 662.869971] [AOA] Measurement: 0,1626941842.660880,04:ce:14:0b:84:6c,2,1,1,0,128,631,954,1015,307,974,790,409,607,14,201,488,837,670,559,909,732,779,931,247,609,364,212,50,806,125,830,63,349,3,640,516,838,47,106,122,35,18,77,48,88,64,18,80,96,20,33,18,26,97,137,114,23,30,56,80,26,31,81,57,103,71,94,122,132
[ 662.903659] [AOA] Measurement: 0,1626941842.694569,04:ce:14:0b:84:6c,2,1,1,0,128,552,913,546,522,492,967,924,764,559,414,70,63,239,790,445,929,393,221,764,787,381,202,564,952,619,1007,564,560,569,850,583,780,39,82,86,21,16,57,29,58,52,5,71,74,17,28,12,25,87,99,86,32,39,70,67,21,31,64,52,84,52,68,96,105
[ 662.932483] [AOA] Measurement: 0,1626941842.723369,04:ce:14:0b:84:6c,2,1,1,0,128,685,82,118,380,897,792,508,637,53,238,478,881,226,649,356,112,371,214,962,110,38,789,444,222,325,846,473,597,732,948,640,781,27,46,66,23,17,55,45,64,24,27,16,48,10,12,18,11,24,66,53,36,11,23,38,41,14,41,15,39,42,55,57,58
[ 662.972676] [AOA] Measurement: 0,1626941842.763587,04:ce:14:0b:84:6c,2,1,1,0,128,138,136,556,528,539,12,931,755,554,411,972,1019,743,610,843,650,828,1017,819,810,325,191,587,951,643,29,578,571,563,816,68,288,27,47,66,24,18,57,45,68,28,28,21,53,11,14,18,11,29,73,60,31,10,16,45,37,16,47,20,48,49,64,70,73
[ 663.005926] [AOA] Measurement: 0,1626941842.796836,04:ce:14:0b:84:6c,2,1,1,0,128,620,950,1015,336,1009,769,416,567,640,441,64,49,224,807,362,872,333,155,763,791,836,30,627,977,31,796,41,354,959,565,525,916,38,83,90,24,16,59,32,62,52,7,70,77,17,28,13,25,86,100,89,31,36,71,66,20,30,65,53,83,51,69,92,103
[ 663.039778] [AOA] Measurement: 0,1626941842.830689,04:ce:14:0b:84:6c,2,1,1,0,128,145,117,541,544,994,819,369,555,15,198,523,916,704,570,876,696,794,968,747,789,827,1019,1021,671,121,829,541,499,500,744,917,213,33,54,79,27,20,65,55,79,30,34,19,60,13,14,22,14,28,82,68,46,13,29,47,50,18,51,18,48,53,70,73,74
[ 663.073682] [AOA] Measurement: 0,1626941842.864593,04:ce:14:0b:84:6c,2,1,1,0,128,158,123,562,522,540,12,927,821,585,388,49,29,213,761,454,931,351,195,860,855,328,198,535,869,573,975,559,526,533,796,19,298,37,72,94,34,20,75,58,89,41,34,35,73,15,18,23,14,42,102,83,34,14,16,58,45,21,62,27,66,63,79,86,90
[ 663.107125] [AOA] Measurement: 0,1626941842.898035,04:ce:14:0b:84:6c,2,1,1,0,128,255,245,663,573,855,788,481,620,46,210,7,42,241,725,357,93,327,190,398,971,146,827,1001,1012,922,43,442,552,685,912,776,957,34,72,90,30,16,65,45,78,44,24,45,69,15,20,19,13,53,97,77,16,13,7,53,30,22,59,31,65,55,72,84,89
[ 663.140596] [AOA] Measurement: 0,1626941842.931513,04:ce:14:0b:84:6c,2,1,1,0,128,97,116,516,529,512,1022,866,749,577,317,24,66,201,793,431,913,275,109,759,791,374,208,560,864,600,996,567,514,536,830,548,752,37,79,84,18,15,56,27,55,51,6,71,73,16,28,10,25,88,97,86,33,40,74,65,19,32,63,52,81,50,63,88,101
[ 663.166705] [AOA] Measurement: 0,1626941842.957621,04:ce:14:0b:84:6c,2,1,1,0,128,644,964,552,556,557,1020,933,770,538,428,494,859,701,603,878,691,267,94,805,837,304,202,539,946,75,798,33,340,553,804,913,254,38,84,90,23,15,60,32,63,53,7,69,76,18,28,13,24,85,105,91,29,34,63,67,20,28,63,51,84,54,70,95,102
[ 663.196831] [AOA] Measurement: 0,1626941842.987740,04:ce:14:0b:84:6c,2,1,1,0,128,670,1023,68,317,893,770,466,622,593,407,1015,2,229,674,807,953,333,202,914,65,570,567,986,38,860,23,937,384,196,751,271,591,34,58,83,30,20,67,53,81,35,34,26,63,13,15,23,12,35,83,70,36,13,24,50,46,19,52,21,53,53,70,74,74
[ 663.230743] [AOA] Measurement: 0,1626941843.021652,04:ce:14:0b:84:6c,2,1,1,0,128,186,149,573,531,931,760,395,585,31,255,46,70,189,746,882,739,731,987,872,927,342,280,582,45,172,849,992,343,23,644,908,249,38,83,96,29,16,67,41,74,52,14,63,76,16,25,15,21,75,106,90,19,26,45,65,19,24,66,46,82,59,72,97,105
[ 663.264833] [AOA] Measurement: 0,1626941843.055741,04:ce:14:0b:84:6c,2,1,1,0,128,641,985,133,419,496,988,409,611,122,315,1022,12,655,525,891,836,854,45,836,64,198,935,551,180,808,22,556,579,69,663,723,114,45,98,108,23,18,69,36,70,63,7,86,92,20,34,14,31,105,127,112,34,42,81,82,25,34,80,61,106,69,88,121,129
[ 663.293401] [AOA] Measurement: 0,1626941843.084311,04:ce:14:0b:84:6c,2,1,1,0,128,203,228,643,573,478,10,949,751,38,224,452,874,656,527,827,888,830,20,353,938,125,799,473,167,909,34,531,643,694,925,987,156,38,80,85,21,16,56,28,58,52,5,72,75,17,29,13,25,88,98,86,33,37,72,66,21,29,64,51,82,52,67,94,105
[ 663.327009] [AOA] Measurement: 0,1626941843.117920,04:ce:14:0b:84:6c,2,1,1,0,128,184,178,514,554,521,972,361,569,1020,221,452,857,691,598,901,701,326,165,771,807,333,213,650,8,677,3,588,575,531,825,300,629,38,84,94,28,17,62,36,68,51,10,68,76,16,28,13,24,82,106,90,23,31,57,66,20,26,65,48,82,54,71,96,106
[ 663.380642] [AOA] Measurement: 0,1626941843.171551,04:ce:14:0b:84:6c,2,1,1,0,128,176,192,596,551,512,1005,925,739,46,264,21,34,203,762,382,950,299,164,823,980,321,267,573,125,169,801,27,369,70,684,181,560,38,84,95,30,16,63,36,70,52,11,67,77,18,27,13,23,79,104,91,23,28,55,66,20,26,66,49,85,57,71,97,104
[ 663.414612] [AOA] Measurement: 0,1626941843.205529,04:ce:14:0b:84:6c,2,1,1,0,128,106,112,983,319,972,795,352,557,35,262,1011,7,639,574,914,685,324,138,794,793,337,184,609,1020,634,4,567,543,976,589,751,30,38,81,89,22,16,59,31,60,53,6,71,75,16,29,11,24,86,99,88,30,36,69,66,20,29,64,52,81,52,68,93,105
[ 663.442680] [AOA] Measurement: 0,1626941843.233589,04:ce:14:0b:84:6c,2,1,1,0,128,100,79,545,506,481,981,322,570,39,243,522,848,684,573,875,704,779,988,278,647,383,207,604,945,58,824,63,379,565,821,532,728,37,84,92,26,17,61,35,67,52,10,68,76,17,28,14,23,82,105,91,24,32,59,65,19,26,65,47,82,55,71,96,104
[ 663.477747] [AOA] Measurement: 0,1626941843.268655,04:ce:14:0b:84:6c,2,1,1,0,128,140,113,509,526,544,6,950,746,591,410,14,45,219,797,434,874,775,953,216,588,878,45,597,901,585,955,578,527,997,627,707,4,47,104,108,26,20,72,37,73,64,8,88,94,21,34,14,31,109,127,113,39,45,88,82,27,35,82,64,104,65,85,119,134
[ 663.506456] [AOA] Measurement: 0,1626941843.297366,04:ce:14:0b:84:6c,2,1,1,0,128,171,144,566,538,531,994,963,778,571,429,29,47,210,779,472,947,303,150,789,820,842,34,592,964,123,821,47,400,556,860,397,604,38,84,94,29,16,63,39,70,51,12,67,78,17,28,15,22,78,105,89,18,27,45,64,20,25,64,45,79,58,74,93,104
[ 663.540380] [AOA] Measurement: 0,1626941843.331298,04:ce:14:0b:84:6c,2,1,1,0,128,195,200,556,521,508,994,385,588,559,432,42,80,224,767,340,904,803,990,865,985,291,251,559,61,845,30,518,566,640,864,626,852,37,82,88,21,16,59,30,58,51,5,72,75,17,29,12,26,88,99,89,33,39,72,66,21,29,64,53,82,50,67,90,102
[ 663.566837] [AOA] Measurement: 0,1626941843.357755,04:ce:14:0b:84:6c,2,1,1,0,128,207,217,154,407,404,983,31,806,2,183,523,905,185,651,415,124,294,193,934,85,95,826,508,266,850,4,479,571,718,897,400,638,39,75,104,35,21,78,58,95,45,33,41,79,15,22,22,14,53,109,89,28,14,7,60,42,23,69,30,73,66,86,94,99
[ 663.597304] [AOA] Measurement: 0,1626941843.388214,04:ce:14:0b:84:6c,2,1,1,0,128,184,238,616,540,455,6,976,799,606,430,16,52,200,678,410,171,344,196,900,99,1015,739,1009,42,911,26,511,628,752,921,541,669,34,62,88,31,20,73,57,87,37,34,34,71,15,17,22,14,42,104,84,35,14,17,58,46,22,65,25,63,63,81,89,95
[ 663.631585] [AOA] Measurement: 0,1626941843.422495,04:ce:14:0b:84:6c,2,1,1,0,128,175,127,498,490,543,6,852,746,661,523,6,38,176,727,361,897,737,1012,796,785,381,228,613,975,625,28,586,615,637,859,374,535,38,84,90,25,17,59,33,64,53,9,69,76,18,28,12,24,83,99,89,27,32,62,65,21,27,65,49,84,54,71,96,106
[ 663.665951] [AOA] Measurement: 0,1626941843.456867,04:ce:14:0b:84:6c,2,1,1,0,128,81,91,577,550,987,811,939,766,17,194,454,837,711,577,908,790,320,128,806,827,354,181,585,888,713,73,566,549,575,841,626,821,39,84,91,25,16,59,31,64,51,8,69,77,17,27,13,24,81,102,89,25,32,61,66,19,26,64,48,80,55,71,96,104
[ 663.694393] [AOA] Measurement: 0,1626941843.485303,04:ce:14:0b:84:6c,2,1,1,0,128,241,264,668,610,478,10,968,739,643,488,940,999,687,471,824,913,768,970,418,979,118,813,502,216,883,18,543,633,669,907,192,293,37,82,93,25,16,61,33,66,53,8,69,77,16,29,13,25,85,102,91,29,34,63,67,20,27,65,50,84,55,70,93,105
[ 663.740748] [AOA] Measurement: 0,1626941843.531658,04:ce:14:0b:84:6c,2,1,1,0,128,667,35,68,366,873,752,472,585,51,245,969,11,716,473,796,947,789,1018,962,144,19,812,928,1008,373,825,877,402,166,744,836,92,38,83,93,26,17,62,35,67,53,11,68,77,17,28,13,24,80,107,90,24,28,54,66,19,27,65,47,83,56,70,93,103
[ 663.773501] [AOA] Measurement: 0,1626941843.564418,04:ce:14:0b:84:6c,2,1,1,0,128,254,248,602,515,463,2,969,822,609,452,1015,9,218,726,375,52,349,224,895,88,160,797,492,197,835,26,521,587,124,672,599,816,36,82,96,28,17,64,41,73,51,13,64,76,16,26,15,21,74,105,88,18,25,43,65,21,24,66,45,80,57,73,94,102
[ 663.803506] [AOA] Measurement: 0,1626941843.594417,04:ce:14:0b:84:6c,2,1,1,0,128,184,234,628,583,434,1007,998,764,67,235,994,27,237,738,311,40,366,208,927,136,124,820,538,257,864,1023,485,552,124,696,836,105,37,82,97,29,16,63,38,71,51,13,65,77,17,27,14,20,76,106,85,19,26,44,64,20,26,65,45,81,58,73,95,104
[ 663.831655] [AOA] Measurement: 0,1626941843.622565,04:ce:14:0b:84:6c,2,1,1,0,128,187,234,640,578,447,1000,1000,804,19,265,478,881,712,535,838,901,773,997,425,982,612,636,543,243,926,63,464,604,677,938,845,1013,38,84,95,26,17,60,35,68,53,11,69,77,18,28,13,22,78,104,90,23,30,56,67,19,25,65,48,82,56,73,93,101
[ 663.863976] [AOA] Measurement: 0,1626941843.654891,04:ce:14:0b:84:6c,2,1,1,0,128,133,151,546,559,572,1015,926,733,989,207,1000,32,644,564,873,687,741,936,811,824,788,5,615,944,602,1010,603,557,528,834,884,142,39,83,87,23,15,58,32,61,52,6,71,75,17,27,13,25,87,102,89,30,34,69,66,21,28,64,51,82,54,66,93,103
[ 663.898126] [AOA] Measurement: 0,1626941843.689042,04:ce:14:0b:84:6c,2,1,1,0,128,627,953,1014,354,976,798,408,607,44,263,489,854,690,553,859,692,292,126,833,847,327,203,633,15,666,1008,542,570,556,803,163,449,43,98,114,37,18,75,48,89,61,18,73,90,19,30,19,24,86,125,106,19,28,45,76,24,29,76,49,92,68,88,113,116
[ 663.932136] [AOA] Measurement: 0,1626941843.723047,04:ce:14:0b:84:6c,2,1,1,0,128,592,947,964,291,1005,790,434,588,623,464,5,62,217,783,417,879,277,123,814,828,358,216,590,941,613,979,567,558,582,870,438,641,38,85,94,28,15,63,38,69,51,11,69,78,17,27,13,24,80,108,90,23,30,57,67,19,27,65,49,83,57,72,95,105
[ 663.967303] [AOA] Measurement: 0,1626941843.758214,04:ce:14:0b:84:6c,2,1,1,0,128,593,942,532,499,524,1002,930,801,44,325,8,24,185,762,409,909,257,139,801,796,331,212,579,957,647,19,589,594,601,834,645,940,39,82,91,24,16,62,34,68,54,10,67,77,17,29,14,23,83,102,91,23,31,57,65,19,27,66,49,83,56,72,94,105
[ 664.004397] [AOA] Measurement: 0,1626941843.795308,04:ce:14:0b:84:6c,2,1,1,0,128,179,211,600,538,962,840,969,771,52,183,501,857,709,539,372,67,761,995,374,950,595,644,485,197,860,5,522,598,751,944,478,714,46,103,121,36,20,79,47,89,63,18,79,95,22,33,16,27,91,127,112,19,29,51,81,26,31,82,54,101,74,93,121,131
[ 664.036579] [AOA] Measurement: 0,1626941843.827494,04:ce:14:0b:84:6c,2,1,1,0,128,184,193,1023,319,478,968,977,785,582,446,20,9,673,557,859,813,319,158,854,57,192,895,519,173,273,885,592,616,729,921,280,603,48,107,118,33,19,75,43,84,63,14,84,94,22,33,17,27,100,127,112,26,32,61,81,26,31,81,56,102,71,92,123,132
[ 664.066234] [AOA] Measurement: 0,1626941843.857150,04:ce:14:0b:84:6c,2,1,1,0,128,137,75,606,577,526,15,926,766,588,473,65,56,235,789,394,909,328,148,271,620,829,48,603,1015,723,69,557,536,623,874,598,848,37,81,95,31,17,64,39,76,50,14,60,74,17,26,16,19,68,105,87,12,21,34,60,23,24,63,37,75,58,74,93,97
[ 664.099097] [AOA] Measurement: 0,1626941843.890010,04:ce:14:0b:84:6c,2,1,1,0,128,643,1008,81,376,499,1006,476,639,600,411,31,47,177,724,386,11,749,2,322,894,631,562,5,1018,303,886,531,609,671,882,824,19,39,82,105,38,20,76,54,92,51,27,50,79,16,23,21,16,59,113,90,17,16,5,63,36,25,68,34,76,65,84,97,101
[ 664.129625] [AOA] Measurement: 0,1626941843.920538,04:ce:14:0b:84:6c,2,1,1,0,128,137,118,10,313,1008,844,381,555,48,289,83,63,202,767,384,887,303,156,845,866,357,209,607,31,693,19,1017,360,1021,615,219,598,37,82,88,22,14,60,32,63,51,6,70,77,18,28,13,25,84,103,89,29,34,61,66,20,27,65,50,82,55,71,95,104
[ 664.161757] [AOA] Measurement: 0,1626941843.952671,04:ce:14:0b:84:6c,2,1,1,0,128,112,111,626,573,502,1010,386,592,634,472,16,18,203,764,411,920,273,124,849,812,346,186,632,3,617,991,627,601,536,806,661,935,47,101,108,24,19,69,33,70,64,6,87,90,21,35,14,32,110,123,109,42,49,93,82,25,38,77,67,101,64,80,114,129
[ 664.195970] [AOA] Measurement: 0,1626941843.986885,04:ce:14:0b:84:6c,2,1,1,0,128,722,36,57,330,959,839,452,613,7,177,531,899,158,655,377,101,805,29,387,952,524,563,981,64,868,15,950,421,704,906,611,921,38,83,89,23,16,60,32,64,51,8,70,74,17,28,12,24,84,101,88,28,33,62,66,20,28,65,49,83,53,70,94,105
[ 664.224474] [AOA] Measurement: 0,1626941844.015390,04:ce:14:0b:84:6c,2,1,1,0,128,123,114,525,514,964,794,353,570,62,289,449,831,666,557,864,696,799,978,812,814,326,215,558,993,131,857,526,554,986,598,20,349,39,84,97,26,15,63,37,69,50,11,67,76,17,28,13,22,82,105,89,22,29,56,67,20,25,65,46,81,56,71,97,105
[ 664.254452] [AOA] Measurement: 0,1626941844.045361,04:ce:14:0b:84:6c,2,1,1,0,128,186,237,116,376,405,986,434,611,89,270,998,995,703,451,339,111,365,266,965,144,58,749,461,195,872,1,928,406,136,701,711,905,44,95,102,24,18,64,33,63,60,6,84,86,20,33,13,31,105,112,98,43,47,89,77,26,37,74,64,95,57,75,104,121
[ 664.292494] [AOA] Measurement: 0,1626941844.083404,04:ce:14:0b:84:6c,2,1,1,0,128,571,944,998,355,961,779,385,585,611,427,977,24,169,733,894,741,270,102,205,606,804,7,50,746,654,1023,632,603,540,785,195,488,36,84,96,28,16,64,39,74,49,15,62,76,17,26,14,19,71,108,86,12,22,39,63,22,24,66,41,79,56,73,93,100
[ 664.329674] [AOA] Measurement: 0,1626941844.120585,04:ce:14:0b:84:6c,2,1,1,0,128,99,69,549,537,1014,777,403,575,45,233,468,867,237,782,424,881,712,952,843,861,365,189,561,896,633,1009,598,574,512,822,108,353,33,57,82,30,21,69,58,83,32,36,25,65,13,15,23,12,35,93,73,41,14,25,52,49,19,55,22,55,60,77,82,79
[ 664.363391] [AOA] Measurement: 0,1626941844.154307,04:ce:14:0b:84:6c,2,1,1,0,128,119,130,589,557,592,1005,923,769,610,466,6,35,242,791,370,880,318,156,807,815,375,209,590,928,704,61,575,569,616,913,502,673,40,84,93,24,15,61,34,65,51,9,67,75,18,29,13,23,83,103,91,25,30,61,66,18,28,64,49,82,55,70,94,104
[ 664.398800] [AOA] Measurement: 0,1626941844.189715,04:ce:14:0b:84:6c,2,1,1,0,128,170,151,565,534,486,992,973,803,586,470,26,57,197,774,450,942,231,126,799,831,849,53,61,842,707,27,558,552,581,895,862,1005,30,51,67,26,17,56,44,68,30,27,21,52,11,13,18,10,28,72,57,34,10,17,41,39,14,45,17,41,45,59,61,60
[ 664.432556] [AOA] Measurement: 0,1626941844.223469,04:ce:14:0b:84:6c,2,1,1,0,128,647,943,51,359,985,810,916,737,70,273,507,846,683,559,855,713,789,982,772,832,806,33,10,882,233,865,9,350,612,835,580,946,38,82,88,22,16,58,29,61,51,6,72,74,19,28,11,25,88,100,90,31,36,71,67,20,29,65,51,81,52,69,93,103
[ 664.465379] [AOA] Measurement: 0,1626941844.256294,04:ce:14:0b:84:6c,2,1,1,0,128,103,91,587,633,503,971,359,572,17,238,994,10,248,811,444,914,348,130,832,839,347,218,44,778,139,850,523,518,550,838,870,119,38,82,90,24,16,60,33,66,53,9,69,76,16,28,12,26,86,102,90,28,35,65,68,20,28,65,50,82,54,70,94,103
[ 664.494043] [AOA] Measurement: 0,1626941844.284958,04:ce:14:0b:84:6c,2,1,1,0,128,220,235,596,537,918,810,473,617,613,405,50,78,234,743,317,24,824,12,914,122,170,830,510,194,883,22,461,580,729,924,967,72,39,84,97,28,17,62,38,72,52,13,65,77,17,28,15,21,75,105,91,16,25,45,64,20,25,65,46,82,58,73,97,104
[ 664.531942] [AOA] Measurement: 0,1626941844.322853,04:ce:14:0b:84:6c,2,1,1,0,128,180,148,534,506,520,993,898,771,614,471,60,67,167,768,424,927,373,179,825,810,364,219,565,984,640,1005,606,584,612,866,717,954,39,81,87,21,14,57,30,57,50,6,69,74,16,28,11,25,86,95,87,34,36,72,67,21,31,62,53,83,50,68,92,104
[ 664.567316] [AOA] Measurement: 0,1626941844.358231,04:ce:14:0b:84:6c,2,1,1,0,128,683,1007,529,517,493,980,390,573,53,250,478,882,146,727,844,752,786,989,299,803,346,250,546,95,726,8,23,415,102,675,282,683,46,104,121,37,20,79,50,94,63,18,76,95,19,31,19,24,92,127,113,19,28,52,79,25,31,81,53,100,73,92,121,131
[ 664.603562] [AOA] Measurement: 0,1626941844.394473,04:ce:14:0b:84:6c,2,1,1,0,128,145,145,552,557,443,962,319,496,36,248,490,865,649,530,874,719,811,977,844,855,317,223,590,8,705,8,487,523,12,651,567,921,38,85,94,28,16,63,37,70,53,11,65,77,17,28,14,22,80,105,90,21,29,55,66,19,27,65,49,83,56,72,95,101
[ 664.641240] [AOA] Measurement: 0,1626941844.432158,04:ce:14:0b:84:6c,2,1,1,0,128,156,169,657,579,464,992,959,785,625,433,11,4,243,704,323,48,813,24,918,90,109,779,520,223,854,1023,528,619,711,896,770,976,35,63,85,30,21,71,57,85,34,34,25,65,14,15,21,14,34,86,72,43,14,25,52,50,18,59,22,59,58,76,84,87
[ 664.668471] [AOA] Measurement: 0,1626941844.459386,04:ce:14:0b:84:6c,2,1,1,0,128,138,142,610,610,478,966,965,752,589,376,1022,24,268,822,485,946,262,112,749,754,342,178,615,876,617,1022,615,574,529,814,673,951,36,85,93,26,16,62,36,67,53,9,69,77,17,28,13,23,81,104,89,26,30,59,66,19,27,65,48,83,57,71,96,105
[ 664.700381] [AOA] Measurement: 0,1626941844.491291,04:ce:14:0b:84:6c,2,1,1,0,128,136,110,557,524,926,749,329,499,48,255,465,880,254,772,931,748,304,164,778,812,410,285,625,8,666,1,504,539,988,597,883,184,47,106,119,33,20,78,46,87,64,14,82,96,21,35,17,27,100,128,116,24,35,64,84,26,33,82,58,104,72,93,121,132
[ 664.728700] [AOA] Measurement: 0,1626941844.519616,04:ce:14:0b:84:6c,2,1,1,0,128,168,127,515,542,983,784,358,536,614,478,20,53,275,825,405,906,308,178,769,842,379,229,614,985,664,19,602,583,578,836,669,930,26,45,62,23,18,54,46,66,26,26,18,50,10,12,17,11,24,67,54,34,10,22,40,39,16,44,15,42,44,57,61,61
[ 664.758979] [AOA] Measurement: 0,1626941844.549890,04:ce:14:0b:84:6c,2,1,1,0,128,611,948,1016,329,958,814,372,557,57,253,458,813,744,629,376,904,792,1010,803,766,836,41,522,946,657,7,89,405,593,824,586,902,38,78,85,20,16,56,28,56,51,5,70,73,17,28,11,26,88,94,87,33,37,72,67,20,30,62,54,81,51,66,90,103
[ 664.794698] [AOA] Measurement: 0,1626941844.585608,04:ce:14:0b:84:6c,2,1,1,0,128,117,160,552,561,508,998,906,751,550,406,1008,20,630,576,463,899,734,912,829,830,316,171,66,744,70,798,91,459,520,773,792,1002,28,52,68,25,15,58,45,70,28,27,21,54,10,14,17,12,28,74,59,31,11,18,41,38,17,49,19,48,47,62,66,68
[ 664.830238] [AOA] Measurement: 0,1626941844.621154,04:ce:14:0b:84:6c,2,1,1,0,128,607,949,72,363,1014,775,365,595,539,402,482,865,723,571,847,686,772,4,247,622,869,5,39,690,24,805,1010,338,1012,648,896,161,38,75,99,35,21,76,57,93,44,32,40,75,16,20,23,15,47,108,85,33,14,14,60,45,22,64,29,68,63,82,90,90
[ 664.859548] [AOA] Measurement: 0,1626941844.650459,04:ce:14:0b:84:6c,2,1,1,0,128,149,146,634,584,396,968,440,618,79,275,487,834,656,505,848,857,738,999,946,109,159,824,538,191,846,28,480,566,670,912,698,924,37,81,89,22,16,57,30,60,52,6,72,73,17,28,11,24,86,102,90,29,35,63,68,20,28,64,51,83,56,71,95,104
[ 664.895291] [AOA] Measurement: 0,1626941844.686208,04:ce:14:0b:84:6c,2,1,1,0,128,183,134,1014,257,1012,815,411,600,17,252,530,904,759,620,446,946,791,997,854,874,321,228,559,44,200,869,18,429,639,826,930,162,47,100,107,24,18,68,36,72,64,6,89,95,21,35,14,32,112,124,111,41,46,90,83,27,37,78,66,104,66,86,117,131
[ 664.923542] [AOA] Measurement: 0,1626941844.714460,04:ce:14:0b:84:6c,2,1,1,0,128,605,971,62,350,986,804,376,555,31,260,510,888,692,574,451,925,289,147,815,848,368,246,620,983,634,981,595,579,588,829,637,938,30,57,77,28,16,62,46,72,34,26,31,61,13,16,19,11,38,86,67,27,11,9,49,35,17,53,22,54,50,66,72,76
[ 664.951138] [AOA] Measurement: 0,1626941844.742054,04:ce:14:0b:84:6c,2,1,1,0,128,661,968,511,500,986,808,396,626,18,205,36,35,227,780,392,903,788,994,211,578,842,21,8,765,1020,805,21,309,28,632,356,693,37,84,96,28,17,62,38,73,52,15,60,75,17,27,15,20,73,106,87,15,25,38,64,21,24,64,41,81,58,74,92,101
[ 664.984474] [AOA] Measurement: 0,1626941844.775390,04:ce:14:0b:84:6c,2,1,1,0,128,623,19,80,367,988,852,984,774,616,451,975,15,202,648,358,43,362,236,912,95,534,631,517,222,284,812,460,554,173,740,452,732,25,43,59,22,16,51,44,59,21,27,10,43,10,9,16,12,19,53,45,40,9,28,35,41,11,36,14,34,39,53,55,55
[ 665.016835] [AOA] Measurement: 0,1626941844.807747,04:ce:14:0b:84:6c,2,1,1,0,128,118,88,12,294,984,787,346,559,92,301,505,894,197,745,401,919,794,990,791,797,364,204,529,924,75,832,36,382,970,552,642,960,39,84,91,26,15,59,32,66,49,9,67,75,16,27,13,23,82,101,88,27,30,57,67,20,27,63,48,82,54,71,93,105
[ 665.052579] [AOA] Measurement: 0,1626941844.843492,04:ce:14:0b:84:6c,2,1,1,0,128,107,121,549,484,997,811,934,769,566,455,52,59,226,800,486,974,277,160,811,836,359,208,588,17,123,822,592,555,601,861,541,834,48,107,120,33,20,80,45,86,64,13,85,93,20,34,17,28,102,134,115,29,38,73,84,25,34,81,61,104,70,90,122,135
[ 665.089030] [AOA] Measurement: 0,1626941844.879943,04:ce:14:0b:84:6c,2,1,1,0,128,627,956,60,353,501,1,341,527,45,276,30,31,220,797,369,890,738,964,267,609,775,995,0,805,117,844,84,381,66,625,333,594,38,83,89,23,16,59,31,63,52,8,68,75,17,27,14,23,84,103,88,26,32,60,66,19,27,65,49,82,55,72,95,103
[ 665.122993] [AOA] Measurement: 0,1626941844.913908,04:ce:14:0b:84:6c,2,1,1,0,128,173,208,649,559,432,1000,479,593,626,427,7,26,252,687,345,72,350,213,990,167,75,791,985,61,891,1018,929,361,139,704,1010,254,30,55,75,28,17,60,47,71,35,28,29,60,13,16,18,11,38,81,67,26,10,8,49,34,18,52,23,57,52,68,75,79
[ 665.153619] [AOA] Measurement: 0,1626941844.944534,04:ce:14:0b:84:6c,2,1,1,0,128,599,921,978,296,905,763,361,599,59,282,49,63,223,763,437,911,305,172,816,822,341,195,561,962,44,835,30,396,16,652,928,232,38,82,90,24,15,60,34,65,53,7,70,77,17,28,13,24,82,102,91,25,32,60,67,19,27,66,48,83,55,71,95,102
[ 665.181779] [AOA] Measurement: 0,1626941844.972694,04:ce:14:0b:84:6c,2,1,1,0,128,618,935,1012,299,973,795,339,551,77,273,14,6,184,780,431,903,777,940,789,790,858,6,617,989,604,4,529,522,584,820,245,451,39,82,91,23,16,60,32,62,51,8,70,77,16,28,13,24,84,103,88,30,33,64,67,21,29,66,50,84,53,71,95,105
[ 665.209238] [AOA] Measurement: 0,1626941845.000153,04:ce:14:0b:84:6c,2,1,1,0,128,148,124,574,515,493,1001,878,771,561,457,1008,56,196,786,393,886,307,164,793,806,319,216,620,999,682,3,563,546,511,814,333,572,38,85,93,26,16,60,35,65,52,10,69,76,17,29,12,24,80,105,89,24,29,55,66,20,26,64,47,83,55,73,96,105
[ 665.241314] [AOA] Measurement: 0,1626941845.032228,04:ce:14:0b:84:6c,2,1,1,0,128,95,124,569,532,558,1006,958,804,551,433,26,32,666,596,428,950,250,98,251,643,359,231,588,50,680,1020,16,376,598,825,80,274,37,84,96,29,17,62,38,69,50,15,63,76,17,27,15,20,75,107,87,16,26,44,64,20,25,64,45,81,58,74,94,103
[ 665.274829] [AOA] Measurement: 0,1626941845.065744,04:ce:14:0b:84:6c,2,1,1,0,128,131,128,530,516,1001,820,915,765,598,459,5,1,254,834,427,929,338,169,785,805,338,181,563,969,648,989,570,541,564,801,942,156,39,85,89,24,15,61,33,65,52,7,69,76,17,28,14,23,83,103,89,28,32,62,65,20,27,65,49,83,55,70,96,103
[ 665.302651] [AOA] Measurement: 0,1626941845.093566,04:ce:14:0b:84:6c,2,1,1,0,128,249,274,671,570,918,814,40,864,599,435,979,7,225,695,816,928,795,1010,402,959,529,587,972,22,926,62,497,575,759,949,714,928,39,85,95,28,17,65,39,72,53,13,66,78,17,27,15,22,78,105,90,21,28,51,66,19,25,65,47,83,58,72,95,104
[ 665.330616] [AOA] Measurement: 0,1626941845.121531,04:ce:14:0b:84:6c,2,1,1,0,128,109,112,1011,295,920,737,303,503,1,222,544,884,223,799,381,885,304,136,808,830,392,229,595,902,621,3,571,575,52,684,488,784,35,56,80,28,21,66,54,80,29,34,19,57,12,13,23,15,26,79,65,47,13,33,45,51,17,48,17,45,48,66,70,69
[ 665.361780] [AOA] Measurement: 0,1626941845.152691,04:ce:14:0b:84:6c,2,1,1,0,128,621,953,1002,298,1012,781,356,547,47,297,507,906,163,735,937,761,261,105,280,645,792,36,1021,812,148,829,42,398,46,667,32,366,39,84,91,25,15,59,34,65,52,6,70,76,17,28,12,24,83,102,89,28,32,62,67,20,28,64,50,84,56,71,96,106
[ 665.395843] [AOA] Measurement: 0,1626941845.186758,04:ce:14:0b:84:6c,2,1,1,0,128,180,131,479,503,540,988,327,519,54,218,7,4,705,595,863,691,776,939,260,635,872,58,19,738,86,821,1018,291,21,596,170,495,37,82,97,31,16,65,41,74,49,13,63,76,17,26,15,22,78,106,88,21,27,51,65,20,26,64,45,82,58,74,95,104
[ 665.428208] [AOA] Measurement: 0,1626941845.219119,04:ce:14:0b:84:6c,2,1,1,0,128,624,980,14,326,997,837,879,750,34,281,29,49,687,601,428,938,297,112,799,791,415,248,624,1011,688,0,552,525,580,840,483,760,39,83,88,23,15,58,32,62,52,7,70,76,16,28,12,25,86,101,87,33,37,72,66,20,30,63,51,82,52,68,89,103
[ 665.460807] [AOA] Measurement: 0,1626941845.251722,04:ce:14:0b:84:6c,2,1,1,0,128,150,132,585,515,988,788,312,531,19,230,502,866,232,757,356,855,766,1012,828,855,363,198,585,911,40,816,573,588,563,825,55,284,39,84,91,27,15,62,36,68,52,12,67,77,17,28,13,23,80,106,90,21,29,51,65,21,26,65,44,82,57,72,96,103
[ 665.494501] [AOA] Measurement: 0,1626941845.285416,04:ce:14:0b:84:6c,2,1,1,0,128,95,84,960,272,1005,806,370,593,47,206,452,837,726,628,375,915,787,970,217,589,921,64,1010,706,66,835,571,563,568,815,20,383,44,100,113,34,18,74,46,84,61,15,79,92,21,33,16,25,90,125,105,23,32,56,77,24,30,78,53,94,68,88,112,121
[ 665.526866] [AOA] Measurement: 0,1626941845.317778,04:ce:14:0b:84:6c,2,1,1,0,128,135,87,530,528,563,1018,924,786,581,336,35,39,195,840,415,902,302,156,765,786,336,186,595,889,84,838,556,519,520,808,139,392,33,70,89,30,17,64,44,77,43,23,43,69,13,21,17,15,49,94,76,15,13,5,53,29,21,59,29,65,55,70,82,85
[ 665.555190] [AOA] Measurement: 0,1626941845.346105,04:ce:14:0b:84:6c,2,1,1,0,128,185,140,575,553,517,1012,892,743,569,462,488,885,168,756,876,712,815,990,818,839,352,254,666,19,623,989,540,571,1021,641,756,66,39,86,105,37,20,76,54,92,52,29,53,82,18,25,22,17,67,120,96,13,18,20,69,30,27,74,41,87,67,86,108,112
[ 665.587739] [AOA] Measurement: 0,1626941845.378649,04:ce:14:0b:84:6c,2,1,1,0,128,140,136,551,586,520,999,955,797,559,441,67,77,260,845,385,943,271,132,792,831,343,209,16,785,140,829,562,534,544,829,394,679,45,100,111,33,19,73,41,82,62,13,81,91,20,34,17,27,96,123,106,28,35,67,76,24,31,77,56,99,66,85,110,126
[ 665.616549] [AOA] Measurement: 0,1626941845.407463,04:ce:14:0b:84:6c,2,1,1,0,128,635,962,3,345,988,815,355,558,24,240,1010,6,746,593,929,736,289,96,766,789,379,257,8,746,109,815,3,347,1003,644,325,680,38,83,94,24,16,62,35,68,53,9,68,76,17,28,14,23,82,104,90,27,31,57,65,20,27,66,48,82,55,69,97,105
[ 665.647689] [AOA] Measurement: 0,1626941845.438600,04:ce:14:0b:84:6c,2,1,1,0,128,648,19,146,397,891,809,1003,825,604,420,1003,21,226,703,354,94,321,219,948,101,99,814,527,251,867,17,966,413,692,875,917,178,37,83,95,30,15,65,40,74,51,16,60,74,17,26,16,19,71,106,88,14,22,38,63,20,25,64,42,81,58,72,91,102
[ 665.676523] [AOA] Measurement: 0,1626941845.467438,04:ce:14:0b:84:6c,2,1,1,0,128,104,110,534,534,524,998,1012,840,589,471,25,45,176,795,375,913,338,140,795,809,393,266,616,984,661,10,586,540,610,850,941,125,38,85,92,25,17,63,36,66,53,9,67,76,16,27,14,23,79,105,89,22,28,52,67,19,25,65,47,83,57,74,93,104
[ 665.708803] [AOA] Measurement: 0,1626941845.499717,04:ce:14:0b:84:6c,2,1,1,0,128,634,941,581,571,488,1008,856,774,627,469,456,830,735,618,382,896,721,955,888,839,366,215,615,1,78,827,75,406,11,625,11,293,30,57,74,27,18,59,45,69,33,28,26,56,12,15,18,11,31,78,62,30,11,13,44,38,17,47,18,46,48,63,65,68
[ 665.742645] [AOA] Measurement: 0,1626941845.533561,04:ce:14:0b:84:6c,2,1,1,0,128,120,122,542,458,989,804,324,560,11,259,479,839,714,539,414,866,750,989,260,667,852,1015,87,803,666,37,569,590,593,813,182,385,37,79,95,31,17,65,43,76,49,18,56,74,16,24,17,18,64,102,84,11,17,24,59,24,23,64,36,73,58,73,90,93
[ 665.770988] [AOA] Measurement: 0,1626941845.561903,04:ce:14:0b:84:6c,2,1,1,0,128,610,947,68,368,969,802,910,775,568,450,44,55,256,757,436,930,291,155,787,785,389,246,588,936,636,1007,1021,342,34,630,690,5,38,79,83,19,14,55,28,53,50,5,71,73,17,27,10,26,88,92,84,35,39,74,65,20,30,62,53,80,49,66,88,101
[ 665.804999] [AOA] Measurement: 0,1626941845.595914,04:ce:14:0b:84:6c,2,1,1,0,128,692,25,559,547,937,787,423,594,28,204,517,873,670,534,860,864,717,976,324,958,645,652,8,32,876,49,442,541,671,886,962,231,29,52,71,26,17,58,44,68,32,27,24,56,11,14,18,10,33,80,62,29,11,14,45,35,18,50,21,50,51,64,68,72
[ 665.832924] [AOA] Measurement: 0,1626941845.623839,04:ce:14:0b:84:6c,2,1,1,0,128,95,104,583,552,524,974,353,560,24,223,51,54,170,756,424,911,295,140,788,804,377,210,605,963,593,987,610,588,566,837,109,411,46,105,123,37,19,79,49,92,63,17,79,95,20,33,17,27,91,133,111,19,29,48,79,26,30,81,52,97,71,93,119,128
[ 665.862628] [AOA] Measurement: 0,1626941845.653537,04:ce:14:0b:84:6c,2,1,1,0,128,606,950,535,500,6,841,322,531,35,295,511,927,205,784,435,957,243,118,217,585,820,65,595,996,681,1001,13,347,555,832,894,221,35,79,95,32,18,65,43,77,48,19,56,75,17,24,16,18,67,107,88,13,22,34,63,22,24,65,41,78,59,73,95,104
[ 665.899649] [AOA] Measurement: 0,1626941845.690566,04:ce:14:0b:84:6c,2,1,1,0,128,155,130,567,571,537,1016,916,757,638,481,15,53,231,830,381,875,278,147,772,787,378,248,627,953,701,31,571,575,567,844,192,457,45,100,109,31,19,71,40,77,62,9,83,88,20,34,15,30,102,119,105,36,41,76,79,23,34,76,62,99,63,82,110,123
[ 665.929095] [AOA] Measurement: 0,1626941845.720010,04:ce:14:0b:84:6c,2,1,1,0,128,134,124,514,526,549,1014,919,740,599,439,27,58,142,723,423,900,800,988,837,818,354,196,1018,774,183,857,541,559,10,629,394,668,37,76,94,31,17,65,43,77,47,20,52,73,15,23,17,17,64,104,83,11,18,26,60,24,23,62,37,75,59,72,89,98
[ 665.963128] [AOA] Measurement: 0,1626941845.754045,04:ce:14:0b:84:6c,2,1,1,0,128,172,231,94,378,453,990,473,611,599,436,971,2,733,513,376,133,810,15,420,963,553,606,946,982,342,827,905,422,201,749,70,277,47,105,115,29,18,75,40,78,64,10,88,94,21,33,14,30,109,130,114,34,41,81,82,25,33,79,62,103,67,88,121,135
[ 665.995986] [AOA] Measurement: 0,1626941845.786898,04:ce:14:0b:84:6c,2,1,1,0,128,644,964,561,547,493,992,936,784,574,458,29,35,646,545,879,736,743,940,811,823,862,8,536,40,711,11,604,593,589,823,870,202,39,86,95,29,16,62,37,69,52,13,65,75,17,28,14,22,77,105,91,22,26,50,66,19,25,65,46,81,57,72,94,105
[ 666.033013] [AOA] Measurement: 0,1626941845.823923,04:ce:14:0b:84:6c,2,1,1,0,128,238,147,611,552,515,991,881,758,632,471,2,11,227,755,403,928,323,170,831,806,380,222,603,1019,639,39,562,546,553,814,984,174,38,84,91,24,14,58,32,64,51,8,70,76,18,28,12,25,85,103,89,28,34,64,66,19,28,63,51,82,53,69,94,102
[ 666.068374] [AOA] Measurement: 0,1626941845.859288,04:ce:14:0b:84:6c,2,1,1,0,128,88,86,532,537,537,1022,877,721,50,296,1014,36,180,762,401,878,798,973,826,814,360,220,627,1021,672,44,575,547,582,879,537,789,33,63,87,32,20,70,53,83,37,32,30,67,14,18,21,13,39,95,74,33,13,15,55,43,20,60,25,63,60,75,83,84
[ 666.100853] [AOA] Measurement: 0,1626941845.891763,04:ce:14:0b:84:6c,2,1,1,0,128,624,950,486,501,474,995,928,804,572,409,422,791,668,580,884,708,746,953,282,599,872,1,614,938,589,19,643,615,591,837,936,135,38,83,90,23,15,60,32,62,51,8,70,77,18,28,13,24,85,102,89,27,34,63,66,21,28,65,51,84,53,71,95,104
[ 666.129997] [AOA] Measurement: 0,1626941845.920912,04:ce:14:0b:84:6c,2,1,1,0,128,612,989,653,603,423,994,1010,801,583,425,1011,38,192,697,361,26,358,216,917,139,176,801,520,206,253,837,515,594,672,876,86,301,47,106,114,30,19,72,38,76,65,8,88,94,22,35,16,31,107,126,113,38,42,84,83,26,35,81,63,104,67,86,121,131
[ 666.163229] [AOA] Measurement: 0,1626941845.954139,04:ce:14:0b:84:6c,2,1,1,0,128,584,938,589,562,949,755,417,587,35,278,28,46,169,745,350,873,781,993,293,667,874,79,566,36,670,987,1015,290,31,628,543,869,37,83,92,24,16,59,33,66,51,8,70,76,18,28,13,23,84,102,90,27,33,60,66,20,28,64,51,84,54,70,95,106
[ 666.200684] [AOA] Measurement: 0,1626941845.991595,04:ce:14:0b:84:6c,2,1,1,0,128,202,203,590,543,444,1013,982,808,606,443,10,11,167,730,431,27,390,230,890,89,239,856,498,153,851,46,512,614,714,913,1011,153,38,85,92,27,17,61,34,64,52,9,68,75,16,27,14,24,83,104,90,26,33,59,66,20,26,65,49,82,55,71,96,105
[ 666.244529] [AOA] Measurement: 0,1626941846.035445,04:ce:14:0b:84:6c,2,1,1,0,128,582,943,1017,344,528,1001,957,787,591,431,42,69,178,802,385,861,297,148,808,818,320,219,576,938,665,9,593,580,555,820,1017,269,37,81,89,22,16,58,31,61,51,6,72,76,18,28,12,26,87,97,86,31,36,71,67,20,30,63,52,82,51,66,92,103
[ 666.278460] [AOA] Measurement: 0,1626941846.069376,04:ce:14:0b:84:6c,2,1,1,0,128,620,951,598,557,495,987,966,769,543,410,437,846,619,532,896,692,749,940,212,601,805,33,1016,745,76,808,16,338,34,649,198,584,45,100,111,32,18,73,44,81,62,11,79,89,22,32,16,27,96,125,107,30,34,67,78,24,32,76,56,97,66,87,112,123
[ 666.312868] [AOA] Measurement: 0,1626941846.103785,04:ce:14:0b:84:6c,2,1,1,0,128,215,273,678,616,462,1017,15,828,549,393,15,41,242,754,353,58,343,227,909,128,123,821,569,245,907,51,488,598,719,935,464,637,32,63,83,29,16,62,44,75,40,26,35,63,14,18,19,11,44,89,72,20,13,2,52,32,21,57,28,62,55,69,79,84
[ 666.341130] [AOA] Measurement: 0,1626941846.132047,04:ce:14:0b:84:6c,2,1,1,0,128,645,973,1007,317,1008,798,362,574,66,291,47,46,195,745,418,915,755,981,265,628,833,27,584,12,674,14,996,320,24,622,398,682,39,85,93,26,15,62,34,65,51,10,69,76,18,27,13,24,82,106,92,25,29,55,67,20,26,64,48,83,57,73,94,101
[ 666.369950] [AOA] Measurement: 0,1626941846.160867,04:ce:14:0b:84:6c,2,1,1,0,128,626,954,32,367,577,2,891,756,636,482,49,47,187,758,416,935,747,971,815,829,351,239,551,1020,664,7,597,563,513,789,779,132,26,45,63,23,16,55,45,65,24,28,18,51,11,11,19,11,26,72,58,34,10,20,41,40,15,47,18,43,45,60,62,64
[ 666.404763] [AOA] Measurement: 0,1626941846.195677,04:ce:14:0b:84:6c,2,1,1,0,128,147,210,662,528,428,972,7,850,593,403,993,1014,213,637,387,142,285,207,366,930,608,612,1001,41,883,14,449,558,189,741,94,372,38,85,97,29,17,63,37,70,51,13,65,76,17,27,14,20,77,107,91,18,26,47,66,20,26,65,44,80,57,73,95,100
[ 666.433524] [AOA] Measurement: 0,1626941846.224441,04:ce:14:0b:84:6c,2,1,1,0,128,653,997,505,557,444,943,996,795,60,287,21,47,194,790,432,906,272,106,841,855,320,242,8,803,158,861,27,405,551,802,311,553,38,84,94,26,17,61,35,65,53,9,69,76,17,28,14,24,83,102,90,26,33,62,67,18,27,64,49,83,52,70,95,105
[ 666.470885] [AOA] Measurement: 0,1626941846.261796,04:ce:14:0b:84:6c,2,1,1,0,128,95,91,572,541,998,830,869,703,610,463,15,37,169,770,368,904,366,184,823,831,345,187,607,936,591,11,563,540,575,834,566,809,30,63,84,29,17,61,46,75,38,26,36,62,13,18,18,12,40,89,71,19,12,2,51,31,20,55,26,61,53,70,80,81
[ 666.514774] [AOA] Measurement: 0,1626941846.305691,04:ce:14:0b:84:6c,2,1,1,0,128,116,119,1006,288,980,811,310,561,1023,230,476,867,673,541,907,737,333,126,788,811,777,25,1006,864,208,882,553,560,629,879,235,514,47,103,114,29,19,73,38,80,65,10,88,95,21,34,16,30,105,130,114,37,41,80,82,25,33,80,62,103,68,89,123,135
[ 666.550208] [AOA] Measurement: 0,1626941846.341125,04:ce:14:0b:84:6c,2,1,1,0,128,181,244,604,557,913,797,1004,799,592,435,19,47,162,681,382,55,739,1001,930,145,123,857,521,198,863,22,465,567,712,944,690,976,44,98,112,34,19,75,46,86,60,18,76,91,19,32,17,26,91,124,107,22,31,58,77,24,30,78,53,95,67,85,113,123
[ 666.579551] [AOA] Measurement: 0,1626941846.370468,04:ce:14:0b:84:6c,2,1,1,0,128,598,939,3,313,955,773,364,575,67,227,450,840,646,545,889,721,301,150,791,786,395,228,597,932,701,18,541,545,1008,619,121,392,38,82,93,26,16,62,35,65,53,10,67,76,17,28,13,23,81,105,89,23,31,57,66,21,26,65,47,82,55,72,94,103
[ 666.610193] [AOA] Measurement: 0,1626941846.401104,04:ce:14:0b:84:6c,2,1,1,0,128,603,942,562,526,991,813,353,540,7,219,523,891,676,565,939,713,761,962,248,612,360,230,582,1012,106,803,26,388,570,865,668,918,39,84,97,29,16,63,35,70,53,11,69,78,17,28,13,24,83,104,90,24,31,57,67,21,25,65,50,84,55,72,95,103
[ 666.643180] [AOA] Measurement: 0,1626941846.434095,04:ce:14:0b:84:6c,2,1,1,0,128,131,113,564,541,493,983,889,726,586,426,1018,19,233,839,391,879,374,177,801,814,372,218,613,897,586,996,580,510,498,841,264,544,39,84,89,22,15,57,31,61,51,7,69,75,17,29,13,24,84,101,88,28,34,63,66,19,27,64,49,82,55,71,95,106
[ 666.681533] [AOA] Measurement: 0,1626941846.472443,04:ce:14:0b:84:6c,2,1,1,0,128,569,910,1006,366,523,977,340,520,41,255,1014,39,179,777,902,739,747,936,255,605,411,231,42,779,579,986,9,316,20,684,848,99,27,43,63,23,18,52,45,64,25,29,17,50,10,11,17,11,24,66,55,37,10,22,40,41,13,41,16,42,44,59,58,61
[ 666.716499] [AOA] Measurement: 0,1626941846.507416,04:ce:14:0b:84:6c,2,1,1,0,128,89,92,591,591,522,1003,897,733,570,373,29,59,245,819,434,913,278,119,820,794,431,239,650,948,637,22,600,592,545,864,402,602,37,74,102,36,22,75,57,93,44,33,39,74,16,20,22,15,48,109,89,30,13,9,60,43,23,68,30,71,67,85,99,100
[ 666.750643] [AOA] Measurement: 0,1626941846.541559,04:ce:14:0b:84:6c,2,1,1,0,128,138,118,22,356,996,811,909,724,575,434,37,38,648,588,928,741,781,969,251,635,410,260,603,945,139,823,627,583,539,823,61,368,37,80,95,31,15,66,43,75,49,18,56,74,16,25,16,17,63,104,83,11,20,27,60,24,24,63,39,73,58,73,88,98
[ 666.779913] [AOA] Measurement: 0,1626941846.570829,04:ce:14:0b:84:6c,2,1,1,0,128,184,238,615,569,397,980,29,841,590,420,1004,15,678,477,862,923,826,16,1016,165,117,854,478,227,874,1009,378,554,180,761,864,101,37,77,105,36,21,77,58,95,47,32,41,79,18,22,23,15,52,116,89,30,14,7,61,42,25,67,31,71,64,84,95,98
[ 666.814872] [AOA] Measurement: 0,1626941846.605790,04:ce:14:0b:84:6c,2,1,1,0,128,638,957,28,340,964,803,368,624,595,474,1009,12,185,730,381,868,766,981,150,521,864,58,1013,763,706,28,571,530,34,631,727,71,47,99,106,24,19,70,34,66,62,7,89,90,21,34,13,32,111,118,108,42,47,93,83,26,37,78,67,101,61,81,114,130
[ 666.848352] [AOA] Measurement: 0,1626941846.639262,04:ce:14:0b:84:6c,2,1,1,0,128,132,118,509,508,523,973,897,776,571,387,0,40,229,792,852,697,744,937,192,564,847,26,663,949,87,832,73,388,557,813,889,147,37,84,94,27,16,63,36,68,51,11,65,76,18,26,13,22,81,105,89,22,29,51,67,20,25,65,46,82,57,75,96,103
[ 666.883088] [AOA] Measurement: 0,1626941846.674003,04:ce:14:0b:84:6c,2,1,1,0,128,137,118,538,533,989,807,962,770,552,430,1021,45,189,781,927,721,315,149,188,568,853,54,47,782,594,980,594,575,545,834,852,4,38,85,94,26,15,62,37,70,52,11,67,77,16,28,13,23,80,105,89,22,29,56,66,20,26,65,47,83,56,71,93,106
[ 666.917744] [AOA] Measurement: 0,1626941846.708662,04:ce:14:0b:84:6c,2,1,1,0,128,115,118,544,540,997,788,444,592,20,234,474,855,671,599,907,728,334,132,809,803,811,86,622,35,701,1017,593,614,529,801,243,551,38,84,91,25,17,60,35,66,52,10,68,76,17,27,12,24,81,103,88,23,30,56,67,19,27,63,46,82,56,74,96,102
[ 666.950434] [AOA] Measurement: 0,1626941846.741344,04:ce:14:0b:84:6c,2,1,1,0,128,200,149,565,525,486,984,373,551,42,252,41,41,637,564,870,705,794,983,794,806,332,211,583,5,680,0,58,354,631,864,8,172,37,83,93,25,16,61,34,69,53,9,67,77,17,28,14,24,82,105,91,25,31,55,64,20,27,64,48,83,55,72,95,104
[ 666.985558] [AOA] Measurement: 0,1626941846.776476,04:ce:14:0b:84:6c,2,1,1,0,128,181,183,617,560,483,995,997,783,648,493,997,1,667,536,358,969,271,145,852,100,214,881,573,180,774,1022,962,348,112,697,1014,267,37,82,87,21,16,57,31,59,52,6,71,75,17,30,12,26,86,100,89,32,36,68,67,20,30,62,52,82,52,66,94,101
[ 667.020281] [AOA] Measurement: 0,1626941846.811198,04:ce:14:0b:84:6c,2,1,1,0,128,95,106,519,523,533,998,907,717,16,221,498,870,205,765,891,691,755,941,858,864,399,274,625,965,649,1009,572,549,586,854,610,810,36,78,80,18,15,53,28,55,50,5,71,73,17,28,11,26,86,99,86,33,36,70,65,19,30,63,52,81,51,67,92,105
[ 667.049977] [AOA] Measurement: 0,1626941846.840893,04:ce:14:0b:84:6c,2,1,1,0,128,685,1012,106,399,400,982,467,635,620,454,62,18,216,703,360,72,364,253,923,119,147,808,546,271,853,20,995,440,718,896,844,1022,38,83,89,24,16,61,34,64,50,9,67,75,17,28,14,25,80,103,89,25,30,56,65,20,26,64,49,80,56,72,95,102
[ 667.084658] [AOA] Measurement: 0,1626941846.875576,04:ce:14:0b:84:6c,2,1,1,0,128,196,204,612,539,459,1006,419,577,114,255,503,872,699,565,375,24,367,198,913,118,137,806,542,216,295,821,969,401,90,694,623,954,39,84,94,28,15,63,35,68,52,11,67,76,17,29,14,23,79,105,90,24,31,56,67,19,26,66,47,83,56,73,96,105
[ 667.118725] [AOA] Measurement: 0,1626941846.909635,04:ce:14:0b:84:6c,2,1,1,0,128,133,94,0,340,991,829,896,762,582,460,50,46,174,778,410,951,283,109,799,797,336,201,549,955,671,23,998,331,35,648,842,155,46,103,109,24,19,71,38,73,64,8,89,96,21,34,14,30,108,127,114,38,45,84,84,25,35,82,63,104,64,86,119,130
[ 667.154651] [AOA] Measurement: 0,1626941846.945566,04:ce:14:0b:84:6c,2,1,1,0,128,719,49,130,409,917,808,490,619,25,205,35,70,213,685,308,25,755,1000,399,954,550,594,1002,64,307,857,977,390,204,762,690,911,35,74,92,31,17,66,44,77,45,22,49,70,15,21,17,15,59,99,79,12,16,16,57,25,22,60,34,70,57,73,90,92
[ 667.184249] [AOA] Measurement: 0,1626941846.975165,04:ce:14:0b:84:6c,2,1,1,0,128,112,106,524,547,517,993,930,778,591,495,20,74,212,827,469,951,278,89,818,829,357,216,609,960,104,840,994,328,542,827,89,411,37,80,82,17,15,55,27,54,51,6,70,72,18,28,12,26,88,96,89,34,36,71,65,20,30,64,54,81,51,66,89,99
[ 667.214685] [AOA] Measurement: 0,1626941847.005597,04:ce:14:0b:84:6c,2,1,1,0,128,215,224,667,598,406,985,1023,804,84,212,1003,22,127,622,374,82,363,210,902,90,47,808,566,270,864,18,482,584,694,886,502,693,47,105,114,30,20,73,39,79,64,10,86,96,22,34,16,30,106,132,115,34,40,80,81,25,33,80,62,103,68,89,121,132
[ 667.254075] [AOA] Measurement: 0,1626941847.044987,04:ce:14:0b:84:6c,2,1,1,0,128,215,239,64,360,899,831,968,792,23,200,471,832,240,682,378,83,345,305,914,89,159,803,525,252,835,1004,473,629,718,916,225,417,38,83,90,24,16,60,31,67,52,9,69,76,17,28,12,25,82,105,90,27,31,60,66,20,27,65,49,83,55,72,93,105
[ 667.292626] [AOA] Measurement: 0,1626941847.083538,04:ce:14:0b:84:6c,2,1,1,0,128,102,103,581,583,493,975,1004,806,536,421,1016,21,215,790,905,711,819,988,813,830,351,238,1023,730,103,827,604,582,586,864,236,460,39,81,86,22,15,58,30,58,51,6,72,75,17,28,12,26,87,98,86,31,36,69,67,20,28,65,52,82,53,68,93,104
[ 667.331486] [AOA] Measurement: 0,1626941847.122398,04:ce:14:0b:84:6c,2,1,1,0,128,189,134,569,550,606,22,874,713,600,473,44,101,250,827,416,871,315,182,816,814,374,247,632,1010,673,27,598,597,617,863,376,574,37,70,93,35,20,73,58,88,39,33,29,70,14,18,21,14,39,101,82,36,15,16,57,47,22,62,26,63,62,80,92,96
[ 667.364662] [AOA] Measurement: 0,1626941847.155577,04:ce:14:0b:84:6c,2,1,1,0,128,98,121,600,574,554,1003,897,755,644,504,7,18,205,818,429,929,310,159,749,770,375,234,561,981,669,1019,1014,356,573,829,937,218,28,49,70,26,17,58,47,67,29,26,22,54,11,13,18,10,29,73,58,33,10,18,43,39,16,48,19,44,47,62,65,68
[ 667.394413] [AOA] Measurement: 0,1626941847.185329,04:ce:14:0b:84:6c,2,1,1,0,128,96,127,541,545,486,977,936,766,584,414,457,855,662,568,901,695,795,969,764,774,372,222,634,981,625,1018,585,539,585,837,356,631,28,50,68,26,18,57,46,66,28,28,19,52,10,11,18,10,26,70,56,34,11,19,40,39,16,45,16,43,45,59,61,65
[ 667.429492] [AOA] Measurement: 0,1626941847.220403,04:ce:14:0b:84:6c,2,1,1,0,128,174,153,579,583,522,973,926,765,597,400,1013,52,285,822,387,892,339,146,763,791,382,201,592,900,565,977,605,553,519,815,74,424,38,81,86,21,14,57,29,61,51,6,70,72,18,28,12,25,85,99,90,30,34,66,67,19,29,64,50,83,53,69,94,105
[ 667.463866] [AOA] Measurement: 0,1626941847.254781,04:ce:14:0b:84:6c,2,1,1,0,128,117,128,537,522,530,971,877,801,595,385,22,55,200,773,426,930,281,136,728,752,912,16,614,923,662,36,536,539,535,801,393,626,40,83,90,25,16,59,32,64,52,8,70,75,18,28,12,25,86,103,89,28,35,65,65,20,28,64,49,82,54,69,94,102
[ 667.500827] [AOA] Measurement: 0,1626941847.291739,04:ce:14:0b:84:6c,2,1,1,0,128,109,81,532,551,531,986,894,730,35,194,503,886,196,751,865,731,312,121,771,767,804,1,107,770,602,1000,546,517,518,813,545,921,38,82,87,22,14,59,31,61,52,7,71,76,18,28,12,26,87,103,87,29,35,66,66,20,28,65,51,83,54,69,95,102
[ 667.539534] [AOA] Measurement: 0,1626941847.330446,04:ce:14:0b:84:6c,2,1,1,0,128,152,122,601,573,489,982,905,770,544,446,489,834,256,806,434,959,344,194,809,819,340,190,554,985,674,56,616,637,559,837,581,795,37,84,90,25,16,58,33,63,51,7,67,76,17,27,14,23,85,103,89,27,33,62,66,19,29,65,51,82,53,68,94,105
[ 667.573720] [AOA] Measurement: 0,1626941847.364635,04:ce:14:0b:84:6c,2,1,1,0,128,123,105,555,516,464,954,400,589,52,313,530,879,227,779,831,725,282,126,871,847,872,29,558,3,707,23,510,556,621,866,434,621,37,77,95,31,17,64,43,76,49,18,53,73,17,24,15,17,62,103,83,11,17,23,59,23,24,62,36,74,57,73,91,97
[ 667.603465] [AOA] Measurement: 0,1626941847.394382,04:ce:14:0b:84:6c,2,1,1,0,128,230,222,605,568,460,945,1002,824,605,419,466,871,687,535,897,806,745,988,342,955,172,836,21,1012,289,872,546,609,678,940,204,328,37,77,85,20,15,55,30,57,51,6,70,76,17,27,12,26,87,92,86,34,39,75,65,21,31,62,53,80,48,62,87,101
[ 667.637899] [AOA] Measurement: 0,1626941847.428810,04:ce:14:0b:84:6c,2,1,1,0,128,113,102,6,334,529,959,880,750,615,487,48,37,263,773,390,891,284,155,782,781,820,23,10,735,106,859,604,610,623,824,807,25,38,76,84,20,15,55,28,53,49,7,71,72,17,28,11,26,88,91,83,37,41,78,64,21,32,61,51,78,47,63,87,99
[ 667.675514] [AOA] Measurement: 0,1626941847.466428,04:ce:14:0b:84:6c,2,1,1,0,128,174,144,604,553,512,1019,896,752,595,434,16,41,222,779,363,909,295,137,834,805,363,262,576,30,633,1017,34,404,569,848,669,939,27,41,57,22,17,52,46,60,21,27,13,45,9,9,17,11,21,61,53,37,11,24,39,41,13,42,15,40,42,57,57,58
[ 667.712634] [AOA] Measurement: 0,1626941847.503544,04:ce:14:0b:84:6c,2,1,1,0,128,116,109,520,477,1016,791,336,553,14,215,483,863,701,631,866,699,769,987,270,626,778,1017,16,758,142,814,1018,354,52,652,128,383,47,107,123,35,20,77,45,86,64,13,80,96,20,35,17,29,101,136,116,27,35,68,84,23,33,83,61,105,69,92,125,131
[ 667.752406] [AOA] Measurement: 0,1626941847.543316,04:ce:14:0b:84:6c,2,1,1,0,128,196,250,635,565,422,994,985,795,588,423,18,53,188,690,834,895,333,211,328,962,181,823,996,21,283,837,561,644,650,879,288,488,29,50,66,25,18,58,45,66,28,27,20,52,10,12,18,10,25,70,60,32,11,20,41,40,16,45,15,43,46,59,63,64
[ 667.785395] [AOA] Measurement: 0,1626941847.576312,04:ce:14:0b:84:6c,2,1,1,0,128,167,160,492,506,550,971,909,774,567,336,9,49,677,580,929,704,743,925,265,656,420,229,547,882,27,789,595,601,548,825,435,733,40,85,92,25,17,61,34,66,53,9,68,77,18,28,13,22,83,102,88,27,32,61,65,19,27,64,50,83,55,73,96,103
[ 667.820915] [AOA] Measurement: 0,1626941847.611832,04:ce:14:0b:84:6c,2,1,1,0,128,645,957,21,381,1,838,929,746,104,300,1007,1020,684,595,374,891,784,961,801,831,357,279,596,43,696,47,550,560,580,848,1007,269,31,50,71,25,21,63,54,71,27,32,17,55,10,12,20,13,26,76,60,43,12,28,45,50,16,47,16,46,49,64,67,68
[ 667.856768] [AOA] Measurement: 0,1626941847.647685,04:ce:14:0b:84:6c,2,1,1,0,128,137,142,550,532,476,1018,909,775,62,309,68,66,201,747,411,918,316,194,774,768,791,1006,71,777,662,40,594,623,583,817,814,984,37,78,87,21,15,56,28,57,52,6,70,73,18,28,11,25,86,96,86,31,36,70,66,20,28,63,52,81,52,67,91,104
[ 667.891686] [AOA] Measurement: 0,1626941847.682596,04:ce:14:0b:84:6c,2,1,1,0,128,156,105,506,487,986,788,363,560,1018,111,400,813,674,569,834,667,766,925,274,600,401,214,585,932,49,855,564,574,542,821,154,395,38,81,85,20,14,57,29,55,50,6,72,74,18,28,11,25,87,95,87,34,39,73,66,20,29,64,52,81,50,65,90,103
[ 667.926614] [AOA] Measurement: 0,1626941847.717528,04:ce:14:0b:84:6c,2,1,1,0,128,153,141,1001,320,988,785,359,550,99,311,19,19,242,798,395,879,274,137,761,828,355,206,36,761,6,760,38,354,1002,630,510,854,26,42,60,21,18,53,45,61,22,28,13,45,10,11,17,11,20,60,52,36,11,23,37,42,13,39,14,37,42,56,54,52
[ 667.962301] [AOA] Measurement: 0,1626941847.753216,04:ce:14:0b:84:6c,2,1,1,0,128,720,48,628,595,462,946,423,583,85,290,530,910,226,752,352,982,749,991,874,106,196,152,586,167,752,987,595,664,686,912,159,340,37,84,94,26,16,60,34,66,52,11,69,76,16,27,12,24,83,101,90,25,32,61,67,20,28,64,50,83,53,70,93,106
[ 667.998179] [AOA] Measurement: 0,1626941847.789094,04:ce:14:0b:84:6c,2,1,1,0,128,126,105,473,467,1010,765,369,580,622,462,504,897,230,754,475,935,301,143,829,849,349,222,587,963,663,6,556,607,636,849,59,335,39,82,88,22,15,59,29,59,51,6,72,75,18,28,12,25,86,100,90,29,35,67,66,20,29,65,52,83,52,70,95,105
[ 668.031409] [AOA] Measurement: 0,1626941847.822319,04:ce:14:0b:84:6c,2,1,1,0,128,103,122,544,556,530,994,902,723,585,385,1023,22,250,789,395,886,296,119,745,753,403,242,613,968,685,5,591,550,542,857,858,84,37,80,83,19,14,56,26,53,49,6,71,73,17,28,12,25,87,92,86,33,38,72,67,19,30,63,53,83,52,69,91,103
[ 668.070971] [AOA] Measurement: 0,1626941847.861881,04:ce:14:0b:84:6c,2,1,1,0,128,82,108,571,559,518,993,938,771,608,415,17,21,195,789,381,867,820,1015,771,793,380,231,631,961,618,1021,594,592,545,836,283,465,32,56,78,28,21,67,58,77,27,34,20,57,11,13,20,12,26,81,67,46,14,31,45,51,17,50,17,45,51,70,68,68
[ 668.107641] [AOA] Measurement: 0,1626941847.898556,04:ce:14:0b:84:6c,2,1,1,0,128,181,151,570,584,559,1014,894,757,564,433,973,52,238,815,396,849,294,86,785,794,808,27,22,725,64,794,609,550,533,824,922,146,38,82,88,22,14,57,31,60,51,6,71,75,17,28,13,25,86,98,89,28,34,65,67,20,27,63,51,82,54,70,95,105
[ 668.143948] [AOA] Measurement: 0,1626941847.934859,04:ce:14:0b:84:6c,2,1,1,0,128,175,142,572,519,509,992,916,743,600,488,505,867,162,756,867,743,778,1009,762,752,891,30,40,802,176,891,563,569,585,836,856,76,39,83,87,22,15,58,32,61,51,5,72,74,18,29,11,26,87,98,88,32,35,71,68,21,30,65,52,83,50,67,93,102
[ 668.183278] [AOA] Measurement: 0,1626941847.974189,04:ce:14:0b:84:6c,2,1,1,0,128,164,147,523,530,476,976,945,747,613,464,27,32,692,599,404,918,298,148,826,820,366,288,580,22,671,1020,554,572,600,887,735,961,39,84,93,25,17,60,34,68,52,9,70,76,18,28,13,24,84,100,89,27,34,63,66,19,26,64,51,81,53,70,94,106
[ 668.228116] [AOA] Measurement: 0,1626941848.019032,04:ce:14:0b:84:6c,2,1,1,0,128,591,937,35,348,934,758,368,541,1009,220,451,858,688,561,898,738,706,931,351,771,813,73,557,48,227,858,489,500,41,653,456,784,25,42,59,21,18,53,45,62,21,29,12,45,9,10,16,11,18,59,50,38,10,25,37,41,14,38,13,34,40,53,52,53
[ 668.262966] [AOA] Measurement: 0,1626941848.053879,04:ce:14:0b:84:6c,2,1,1,0,128,144,108,499,527,968,786,402,661,583,455,0,25,181,770,350,869,746,989,213,599,876,87,535,978,107,808,9,307,65,643,190,534,40,84,103,39,20,76,54,91,51,29,51,81,18,23,21,16,60,110,89,20,16,6,62,36,25,68,33,77,65,84,97,101
[ 668.293076] [AOA] Measurement: 0,1626941848.083994,04:ce:14:0b:84:6c,2,1,1,0,128,129,131,624,582,465,1012,923,776,619,468,0,1017,702,570,368,1020,396,224,845,57,220,61,560,166,239,877,528,571,641,875,442,676,38,83,96,29,16,64,39,74,50,15,62,77,16,26,15,19,72,107,86,13,21,37,62,21,23,64,38,78,59,73,94,97
[ 668.323857] [AOA] Measurement: 0,1626941848.114771,04:ce:14:0b:84:6c,2,1,1,0,128,593,920,15,353,513,1006,914,751,594,411,8,31,197,739,386,885,271,129,815,806,811,1020,531,913,103,848,47,368,27,654,232,559,36,82,89,22,16,57,30,62,50,7,69,74,17,28,12,26,85,97,88,32,36,68,66,21,28,63,53,82,52,68,95,104
[ 668.363143] [AOA] Measurement: 0,1626941848.154051,04:ce:14:0b:84:6c,2,1,1,0,128,700,47,77,346,863,768,489,624,593,432,479,861,178,647,316,96,301,205,959,162,98,832,482,197,316,828,934,362,178,700,1002,254,46,104,114,30,19,73,37,79,65,8,87,94,21,36,15,31,108,130,115,35,42,82,83,26,34,81,64,104,67,89,122,135
[ 668.397525] [AOA] Measurement: 0,1626941848.188440,04:ce:14:0b:84:6c,2,1,1,0,128,184,198,608,541,428,999,961,777,132,267,9,6,214,702,391,73,354,234,333,929,177,868,526,260,901,35,497,586,691,863,438,731,38,84,93,27,16,63,34,67,51,10,68,79,18,28,12,24,81,104,91,26,31,57,66,21,27,65,48,82,56,71,95,105
[ 668.433516] [AOA] Measurement: 0,1626941848.224428,04:ce:14:0b:84:6c,2,1,1,0,128,173,174,629,584,449,977,945,764,603,460,1017,32,295,821,423,984,340,220,824,14,305,266,567,148,766,3,547,586,662,862,386,600,35,74,93,31,17,65,44,78,47,21,52,72,16,23,16,15,59,100,80,11,17,20,58,25,22,62,35,71,57,72,88,96
[ 668.473072] [AOA] Measurement: 0,1626941848.263985,04:ce:14:0b:84:6c,2,1,1,0,128,114,122,549,565,471,978,842,695,592,432,5,35,672,603,864,698,779,963,783,790,365,242,27,758,142,879,610,604,532,818,1002,259,26,47,64,24,17,54,44,63,25,28,18,49,10,12,18,11,25,65,55,34,12,21,38,40,15,44,15,44,44,59,61,62
[ 668.505100] [AOA] Measurement: 0,1626941848.296013,04:ce:14:0b:84:6c,2,1,1,0,128,638,980,569,563,486,949,925,740,609,458,465,868,717,599,848,664,747,944,221,617,835,16,88,782,167,877,39,364,565,837,416,684,38,83,92,24,16,61,34,65,52,11,68,77,17,28,14,23,82,103,90,24,31,59,66,19,27,64,49,82,54,71,95,105
[ 668.537953] [AOA] Measurement: 0,1626941848.328867,04:ce:14:0b:84:6c,2,1,1,0,128,659,979,7,333,1003,819,411,588,623,495,11,26,686,562,863,746,757,957,272,781,787,69,601,116,711,1010,603,614,649,897,547,800,46,98,113,33,19,74,44,85,60,14,74,89,19,31,17,24,89,124,105,22,30,51,74,24,29,75,52,95,70,86,110,118
[ 668.574437] [AOA] Measurement: 0,1626941848.365352,04:ce:14:0b:84:6c,2,1,1,0,128,127,94,577,520,471,977,979,794,609,480,3,20,218,782,422,898,272,113,234,568,866,1,593,951,609,21,631,600,585,831,191,423,37,84,91,27,17,60,34,68,52,11,67,76,17,28,14,23,81,106,88,24,28,54,65,20,26,65,47,84,58,72,95,104
[ 668.604408] [AOA] Measurement: 0,1626941848.395324,04:ce:14:0b:84:6c,2,1,1,0,128,88,98,570,580,542,1009,851,719,585,430,523,908,227,762,432,925,789,935,797,789,398,213,67,823,667,31,610,588,567,828,51,351,39,83,91,26,17,60,34,64,52,8,70,74,17,28,12,25,85,99,87,31,36,70,67,21,28,65,51,82,52,68,91,102
[ 668.640814] [AOA] Measurement: 0,1626941848.431729,04:ce:14:0b:84:6c,2,1,1,0,128,174,120,32,330,947,777,409,641,39,270,491,864,233,750,398,910,773,1023,798,773,891,83,537,1,104,845,7,335,41,619,567,8,25,43,62,22,17,52,46,61,24,27,16,47,10,11,17,12,22,64,55,37,10,24,38,40,14,41,16,40,42,55,59,58
[ 668.676579] [AOA] Measurement: 0,1626941848.467494,04:ce:14:0b:84:6c,2,1,1,0,128,117,73,529,526,494,960,418,599,33,236,67,56,200,788,351,868,335,155,803,788,400,246,584,996,677,1021,580,569,571,840,104,456,37,84,93,24,17,61,33,67,53,10,68,76,17,29,12,23,84,102,91,30,33,63,66,21,28,64,49,84,54,69,95,104
[ 668.710893] [AOA] Measurement: 0,1626941848.501805,04:ce:14:0b:84:6c,2,1,1,0,128,188,146,556,550,541,997,994,805,546,429,20,62,210,810,426,932,298,128,779,805,393,247,620,993,640,2,584,570,580,813,1016,313,37,84,89,23,15,59,32,62,52,7,71,76,17,28,12,26,86,102,89,29,35,66,67,19,28,65,52,83,54,69,93,104
[ 668.742298] [AOA] Measurement: 0,1626941848.533215,04:ce:14:0b:84:6c,2,1,1,0,128,185,178,605,573,402,969,976,802,670,440,80,84,208,719,438,102,337,192,880,110,214,822,599,250,810,47,581,652,697,909,1011,172,38,83,90,24,16,60,33,64,53,7,71,75,16,28,12,24,84,102,89,27,35,64,67,20,27,64,51,84,54,70,96,103
[ 668.773547] [AOA] Measurement: 0,1626941848.564463,04:ce:14:0b:84:6c,2,1,1,0,128,191,136,3,324,991,813,385,578,10,218,476,848,673,572,388,885,353,197,804,810,398,245,593,17,656,21,5,368,568,817,602,922,30,57,75,27,16,61,47,71,34,27,30,59,11,15,19,9,34,81,63,28,11,11,47,36,18,51,21,53,49,64,69,70
[ 668.812862] [AOA] Measurement: 0,1626941848.603773,04:ce:14:0b:84:6c,2,1,1,0,128,152,134,518,519,569,1021,838,708,590,467,12,48,235,836,375,862,808,1014,202,595,892,55,47,814,642,995,557,535,584,879,589,878,37,84,92,24,14,60,34,64,51,8,68,75,18,28,14,24,84,103,89,26,32,59,66,20,27,65,49,82,55,71,94,103
[ 668.852708] [AOA] Measurement: 0,1626941848.643618,04:ce:14:0b:84:6c,2,1,1,0,128,659,998,80,374,495,1004,380,574,74,280,1014,24,672,559,419,970,779,993,818,990,302,261,603,136,241,867,7,416,72,671,743,59,37,84,94,27,16,63,37,70,52,11,66,76,16,28,13,22,78,103,89,20,29,50,65,20,25,65,45,81,58,72,94,103
[ 668.892621] [AOA] Measurement: 0,1626941848.683531,04:ce:14:0b:84:6c,2,1,1,0,128,130,100,534,538,492,1011,949,822,501,386,67,47,181,752,848,704,354,165,765,782,415,228,577,980,667,9,559,562,571,865,955,232,27,48,69,26,17,57,46,66,29,28,21,54,11,13,17,11,31,77,60,32,11,16,43,39,16,47,17,47,46,62,63,68
[ 668.932610] [AOA] Measurement: 0,1626941848.723521,04:ce:14:0b:84:6c,2,1,1,0,128,167,143,562,516,969,799,980,817,99,277,2,55,226,788,436,972,307,155,892,1022,339,294,574,89,679,998,993,314,103,678,377,728,38,83,88,23,16,59,30,63,52,8,71,74,17,28,12,25,85,103,88,29,34,66,66,20,28,66,50,83,54,71,93,104
[ 668.972606] [AOA] Measurement: 0,1626941848.763517,04:ce:14:0b:84:6c,2,1,1,0,128,166,115,486,495,1017,801,383,526,1020,195,489,867,664,555,897,726,730,922,314,663,839,14,578,915,70,808,38,357,992,610,633,925,39,82,88,21,15,57,29,60,52,6,70,76,17,29,11,26,85,100,89,28,34,66,66,20,30,64,51,83,53,70,94,107
[ 669.012014] [AOA] Measurement: 0,1626941848.802931,04:ce:14:0b:84:6c,2,1,1,0,128,556,932,16,367,1017,832,912,718,579,397,48,64,180,780,436,898,763,977,804,826,356,199,588,887,607,1002,604,571,502,835,525,716,33,72,91,31,17,65,46,76,43,22,46,69,15,21,18,15,53,99,79,12,14,10,55,28,22,61,31,68,55,71,86,91
[ 669.042814] [AOA] Measurement: 0,1626941848.833725,04:ce:14:0b:84:6c,2,1,1,0,128,154,165,608,568,448,1010,948,768,96,271,10,3,698,567,371,998,312,204,893,88,235,838,579,201,803,21,535,569,670,851,247,506,37,78,81,20,16,55,28,56,51,5,71,72,17,29,12,25,87,98,86,33,36,70,67,21,29,62,53,81,51,67,93,103
[ 669.082186] [AOA] Measurement: 0,1626941848.873096,04:ce:14:0b:84:6c,2,1,1,0,128,693,7,109,360,934,811,985,808,50,219,515,872,207,701,784,865,384,223,960,123,191,824,549,228,840,59,446,595,175,703,1005,253,38,73,93,34,20,72,53,89,44,31,39,74,15,20,21,12,48,103,83,25,13,6,58,41,23,67,32,71,64,81,94,94
[ 669.122539] [AOA] Measurement: 0,1626941848.913450,04:ce:14:0b:84:6c,2,1,1,0,128,187,103,622,562,532,977,906,782,597,481,25,10,735,570,409,919,321,161,830,834,371,239,550,983,668,19,572,546,592,817,749,20,37,83,94,30,16,64,40,73,50,13,63,77,16,26,14,21,73,105,90,15,23,40,63,21,24,64,41,77,56,74,95,100
[ 669.162632] [AOA] Measurement: 0,1626941848.953542,04:ce:14:0b:84:6c,2,1,1,0,128,629,964,984,323,1004,808,438,586,17,243,1001,34,183,787,390,878,727,945,279,624,814,10,52,709,80,823,588,541,526,786,528,850,46,105,116,29,20,75,42,79,65,11,86,96,20,34,16,30,105,131,114,32,41,77,83,23,33,81,62,105,69,91,122,130
[ 669.212092] [AOA] Measurement: 0,1626941849.003009,04:ce:14:0b:84:6c,2,1,1,0,128,609,937,558,556,528,1002,956,750,618,496,1023,23,206,798,398,907,310,145,795,816,774,37,23,822,661,974,643,604,586,837,1014,277,46,98,103,27,19,67,36,71,63,9,84,89,20,34,15,29,103,115,102,37,43,81,79,24,34,75,62,98,62,82,110,123
[ 669.252663] [AOA] Measurement: 0,1626941849.043574,04:ce:14:0b:84:6c,2,1,1,0,128,160,196,48,360,450,990,16,832,562,365,23,49,263,729,391,79,288,193,921,110,119,837,519,210,863,42,448,593,716,921,931,133,43,94,117,39,20,81,55,96,57,26,59,89,19,25,20,17,67,126,99,19,17,10,69,35,26,72,36,82,69,90,106,111
[ 669.293821] [AOA] Measurement: 0,1626941849.084730,04:ce:14:0b:84:6c,2,1,1,0,128,728,83,125,408,927,818,11,792,578,382,979,997,720,487,870,972,776,10,419,954,553,614,985,40,339,836,944,367,149,699,242,535,43,96,113,37,20,76,50,91,59,22,69,87,19,29,19,21,78,123,101,13,23,34,73,26,29,76,47,89,69,86,107,116
[ 669.331426] [AOA] Measurement: 0,1626941849.122341,04:ce:14:0b:84:6c,2,1,1,0,128,152,107,520,515,498,966,383,583,48,298,536,864,672,580,900,731,789,994,266,616,832,17,68,827,120,867,621,587,569,799,359,599,26,42,59,21,17,52,47,60,22,26,12,45,9,9,18,10,19,61,51,37,11,24,37,41,12,39,13,37,41,55,59,55
[ 669.362038] [AOA] Measurement: 0,1626941849.152953,04:ce:14:0b:84:6c,2,1,1,0,128,737,63,619,571,888,807,8,828,606,408,22,1,171,664,408,184,302,174,960,136,104,835,456,208,304,847,941,360,107,670,272,594,31,62,82,30,17,62,47,74,39,25,36,63,13,18,17,13,46,89,72,19,12,2,53,33,21,56,29,63,55,69,80,81
[ 669.393111] [AOA] Measurement: 0,1626941849.184028,04:ce:14:0b:84:6c,2,1,1,0,128,148,147,543,531,499,991,917,782,586,484,997,1018,648,540,819,712,792,1013,837,803,369,199,13,763,52,813,23,385,581,839,303,635,34,62,82,30,20,69,57,81,33,31,25,63,12,14,22,11,36,90,70,38,12,18,51,47,20,55,21,56,57,73,79,77
[ 669.429710] [AOA] Measurement: 0,1626941849.220621,04:ce:14:0b:84:6c,2,1,1,0,128,646,976,547,509,547,3,343,555,105,328,986,1005,645,540,851,700,777,939,259,637,850,34,54,916,767,3,568,564,577,801,1,316,27,44,64,23,17,55,47,64,26,27,15,48,9,10,18,9,24,64,54,34,10,25,38,42,13,40,14,39,42,55,56,52
[ 669.464581] [AOA] Measurement: 0,1626941849.255496,04:ce:14:0b:84:6c,2,1,1,0,128,178,157,580,572,567,7,955,799,571,429,71,95,215,791,463,949,333,136,834,883,305,206,599,1005,654,7,578,568,561,828,333,546,35,79,84,19,16,56,28,54,49,5,70,73,17,28,11,27,88,92,85,33,39,74,66,22,30,63,53,78,50,66,90,101


File: /Example_data\ftm_measurements.txt

[  676.477559] wil6210 0000:01:00.0 wlan0: wil_ftm_evt_per_dest_res: [FTM] Measurement: 259446684, 85354308, 94500864, 270442728
[  676.485887] wil6210 0000:01:00.0 wlan0: wil_ftm_evt_per_dest_res: [FTM] Measurement: 279586716, 105494256, 114155520, 290097336
[  676.497264] wil6210 0000:01:00.0 wlan0: wil_ftm_evt_per_dest_res: [FTM] Measurement: 299222940, 125130564, 133785600, 309727524
[  678.131355] wil6210 0000:01:00.0 wlan0: wil_ftm_evt_per_dest_res: [FTM] Measurement: 344786844, 120894000, 130037760, 355780224
[  678.139513] wil6210 0000:01:00.0 wlan0: wil_ftm_evt_per_dest_res: [FTM] Measurement: 364902300, 141009468, 149673984, 375416412
[  678.150884] wil6210 0000:01:00.0 wlan0: wil_ftm_evt_per_dest_res: [FTM] Measurement: 384538524, 160645716, 169291776, 395034168
[  679.758553] wil6210 0000:01:00.0 wlan0: wil_ftm_evt_per_dest_res: [FTM] Measurement: 430077852, 85349796, 94476288, 441053640
[  679.765942] wil6210 0000:01:00.0 wlan0: wil_ftm_evt_per_dest_res: [FTM] Measurement: 450193308, 105465312, 114124800, 460702116
[  679.777496] wil6210 0000:01:00.0 wlan0: wil_ftm_evt_per_dest_res: [FTM] Measurement: 469829532, 125101488, 133742592, 480319908
[  681.397400] wil6210 0000:01:00.0 wlan0: wil_ftm_evt_per_dest_res: [FTM] Measurement: 515362716, 85359444, 94507008, 526359516
[  681.405739] wil6210 0000:01:00.0 wlan0: wil_ftm_evt_per_dest_res: [FTM] Measurement: 535502748, 105499644, 114161664, 546014172
[  681.417154] wil6210 0000:01:00.0 wlan0: wil_ftm_evt_per_dest_res: [FTM] Measurement: 555138972, 125135940, 133779456, 565631928
[  683.051528] wil6210 0000:01:00.0 wlan0: wil_ftm_evt_per_dest_res: [FTM] Measurement: 600672156, 120887496, 130037760, 611671212
[  683.059642] wil6210 0000:01:00.0 wlan0: wil_ftm_evt_per_dest_res: [FTM] Measurement: 620812188, 141027624, 149692416, 631325832


File: /Generate_calibration.m
close all
clear all
%% ONLY MODIFY THESE PARAMETERS
% Set up the folders
currentFolder = pwd;

% These are the measurements from the router
csi_filename = [pwd '/Example_data/csi_measurements.txt'];
ftm_filename = [pwd '/Example_data/ftm_measurements.txt'];

% Output filename, the calibration file
out_filename = 'oscillator.mat';

% True distance of the routers in meters
routers_true_distance = 2;

%% Do the calibration
% Load the position of the MikroTik antennas
load('antennas_mikrotik.mat')

% Number of samples gathered for CSI
num_samples = 250;

%% CSI
[magnitudes, phases, ~] = Parse_csi(csi_filename);

% Clean the data
pre_channel = zeros(6, 6, num_samples);

% We go up to 30 instead of 32
% so that 31 and 32 are disabled
% since they return random data
for jj=1:30

    a = phases(:, jj);
    a = a*2*pi/1024;
    
    % Move to complex domain
    a = exp(1i*a);

    
    converging_limit = 50;
    converging_retries = 0;
    converged = 0;
    
    % Sometimes it does not converge at first since the seed is random
    while converged == 0

        try
            [a, phase_offset_0, converged] = Sanitize(a);
        catch
            disp(['Converging error on file ' filename])
        end

        if converging_retries == converging_limit

            break
        end

        converging_retries = converging_retries + 1;
    end

    if converging_retries == converging_limit
        disp(['Converging threshold reached, ignoring ' filename])
        continue
    end
    
    [row,col] = find(antenna_positions == jj);
    pre_channel(row, col, :) = a(1:num_samples, :);
end

antenna_oscilator_phases = pre_channel;

% Average over the number of samples
antenna_oscilator_phases = sum(antenna_oscilator_phases,3)/num_samples;

%% FTM
ftm_times = Parse_ftm(ftm_filename);

% Create a histogram
distances = zeros(size(ftm_times, 1), 1);

for i=1:size(ftm_times, 1)

    % Calculate the distance in meters
    T1 = ftm_times(i, 1);
    T2 = ftm_times(i, 2);
    T3 = ftm_times(i, 3);
    T4 = ftm_times(i, 4);

    dist = 3e8 * (((T4-T1)-(T3-T2))*1e-12)/2;

    distances(i, 1) = dist;
end

distance = median(distances);

antenna_ftm_offset = abs(distance - routers_true_distance);

%% Save the calibration
save(out_filename, 'antenna_ftm_offset', 'antenna_oscilator_phases');


File: /How to calibrate.md
# Steps to calibrate the routers

**NOTE:** Must be done once per device

1. Setup 2 routers at a known distance, preferably on a tripod.
2. Make sure the antennas are aligned, both in azimut and elevation
3. Cover the routers with 60GHz absorving material (You could also do this outdoors without the material, in a place where there are no walls and therefore no reflections)
4. Use the scripts listed [here](https://github.com/IMDEANetworksWNG/Mikrotik-researcher-tools) to get 300 CSI measurements and 10 FTM measurements
5. Copy the files ftm_measurements.txt and csi_measurements.txt to a know location in your PC
5. Follow the instructions on the Generate_calibration.m script



File: /LICENSE.txt
MIT License

Copyright (c) 2021 Alejandro Blanco Pizarro and Pablo Jiménez Mateo

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



File: /mD-Track\Grid_AoA.m
function [cb_aoa, theta] = Grid_AoA(step_angle, N,d,lambda)
%UNTITLED9 Summary of this function goes here
%   Detailed explanation goes here

    
    %%%%%% AoA %%%%%%
    theta = -90:step_angle:(90-step_angle);
    % pass to radian
    theta = deg2rad(theta);

    % Calculate the steering matrix
    cb_aoa = ones(N,length(theta));

    for i = 1:N
        cb_aoa(i,:) = exp(-1i*(i-1)*d*2*pi*sin(theta)/lambda);
    end
end



File: /mD-Track\Individual_Azimuth_Elevation_Estimator.m
function [index_az_max,index_el_max,attenuation] = Individual_Azimuth_Elevation_Estimator(channel,S_az,S_el,index_el)
%UNTITLED7 Summary of this function goes here
%   Detailed explanation goes here
        
    % estimate azimuth knowing elevation
    channel_el = sum(channel .* S_el(:,index_el)',2);
    spectrum_az = (S_az' * channel_el);
    [~,index_az_max] = max(abs(spectrum_az));

    % estimate elevation knowing azimuth
    channel_az = sum(channel .* conj(S_az(:,index_az_max)),1);
    spectrum_el = (S_el' * channel_az.');
    [~,index_el_max] = max(abs(spectrum_el));
    attenuation = spectrum_el(index_el_max);

    
end



File: /mD-Track\Jointly_Azimuth_Elevation_Estimator.m
function [matrix_az_el] = Jointly_Azimuth_Elevation_Estimator(S_az, S_el, channel_aux)
%UNTITLED2 Summary of this function goes here
%   Detailed explanation goes here

    [~,len_az] = size(S_az);
    [~,len_el] = size(S_el);
    matrix_az_el = zeros(len_az, len_el);
    
    
    for index_az = 1:len_el
        
        channel_az = S_az(:,index_az)'.*channel_aux.';
        channel_aoa = sum(channel_az,2);

%             channel_freq = fft(channel_aoa);
        channel_az_el = (S_el')*channel_aoa;
        alpha = sum((channel_az_el),2);

        matrix_az_el(index_az, :) = alpha;
    end
end



File: /mD-Track\Jointly_Azimuth_Elevation_Estimator_Faster.m
function [channel_az_el] = Jointly_Azimuth_Elevation_Estimator_Faster(S_az, S_el, channel_aux)
%UNTITLED2 Summary of this function goes here
%   Detailed explanation goes here

%     [~,len_az] = size(S_az);
%     [~,len_el] = size(S_el);
%     matrix_az_el = zeros(len_az, len_el);
    
    channel_az = S_az'*channel_aux.';
    channel_az_el = S_el'*channel_az.';
%     matrix_aoa_toa = channel_steering/(K*N);
    
%     matrix_aoa_toa = matrix_aoa_toa.';
    
%     for index_az = 1:len_el
%         
%         channel_az = S_az(:,index_az)'.*channel_aux.';
%         channel_aoa = sum(channel_az,2);
% 
% %             channel_freq = fft(channel_aoa);
%         channel_az_el = (S_el')*channel_aoa;
%         alpha = sum((channel_az_el),2);
% 
%         matrix_az_el(index_az, :) = alpha;
%     end
end



File: /mD-Track\mD_track_2D.m
function [Az_estimated, El_estimated, att] = mD_track_2D(channel, S_az, S_el)
%UNTITLED Summary of this function goes here
%   Detailed explanation goes here
    
    % number of antennas and active subcarriers
    [N, M] = size(channel);
    
    
    index_zeros = channel == 0;

    %% In mD-track paper is 3.2.1 Initial estimation

    % take auxiliar variables to remove them in the loop
    channel_aux = channel;

    % variables for the arguments of angles and times of arrivas
    arg_max_el = zeros(1,0);
    arg_max_az = zeros(1,0);

    % variable for the power of the attenuation
    power = zeros(1,0);
    att = zeros(1,0);

      
    % variable for reconstract the estimate parameters
    channel_recontract = zeros(0,N,M);

    out = false;
    l = 0;
    while (out == 0)
        % iterate over the number of paths
        l = l + 1;
%         z functions
%         [matrix_az_el] = Jointly_Azimuth_Elevation_Estimator(S_az, S_el, channel_aux);
        [matrix_az_el] = Jointly_Azimuth_Elevation_Estimator_Faster(S_az, S_el, channel_aux);
        % take the power
        matrix_az_el_power = abs(matrix_az_el).^2;
        max_value = max(matrix_az_el_power(:));

        % take the position of the maximum
        [index_az_max, index_el_max] = find(matrix_az_el_power == max_value);

        if length(index_az_max) > 1
            index_az_max = index_az_max(1);
            index_el_max = index_el_max(1);
        end
        
        attenuation = matrix_az_el(index_az_max, index_el_max);
        attenuation = attenuation/((N*M)-sum(index_zeros(:)));
        att(l) = attenuation;

        % take the power of the maximum
        power(l) = abs(attenuation).^2;
        
        
        % check the power
        if (power(1) * 10^(-25/10) > power(l)) % Originally (-25/10)
            out = true;
            power(l) = [];
            att(l) = [];
            l = l -1;
            break;
        end
        
        % take the argument of the path to be saved
        arg_max_el(l) = index_el_max;
        arg_max_az(l) = index_az_max;

        % take the pattern of the component
        pattern_el = (S_el(:,arg_max_el(l)));
        pattern_az = S_az(:,arg_max_az(l));
       
        % create the component
        channel_remove_el = repmat(pattern_el,1,N).';
%         channel_remove_toa = channel_remove_toa * attenuation;
        channel_remove_el_az = (channel_remove_el .* pattern_az)*attenuation;

        channel_remove_el_az(index_zeros) = 0;
        % remove it from the channel
        channel_aux = channel_aux - channel_remove_el_az;

        % recontract the signal
        channel_recontract(l,:,:) = channel_remove_el_az;
    end
    
   
    % number of estimated paths
    L_estimated = l;
    
    %% In mD-track paper is 3.2.2  Iterative path parameter refinement.

    % take the output of the previous part as a residual
    channel_residual = channel_aux;

    % fix to ten iterations
    for iteration = 1:10
    %     iteration
        for l = 1:(L_estimated)

            % add noise
            channel_component = squeeze(channel_recontract(l,:,:)) + channel_residual;

            [index_az_max,index_el_max,attenuation] = Individual_Azimuth_Elevation_Estimator(channel_component,S_az,S_el,arg_max_el(l));
            attenuation = attenuation/((N*M)-sum(index_zeros(:)));
            att(l) = attenuation;

            % take the power
            power(l) = abs(attenuation).^2;
            
            arg_max_el(l) = index_el_max;
            arg_max_az(l) = index_az_max;

            % take the pattern of the component
            pattern_el = (S_el(:,arg_max_el(l)));
            pattern_az = S_az(:,arg_max_az(l));
                       
            % reconstract the signal
            channel_remove_el = repmat(pattern_el,1,N).';
%             channel_remove_toa = channel_remove_toa .* (cos(shift_phase_component(l)) + 1i*sin(shift_phase_component(l)));
%             channel_remove_toa = channel_remove_toa * attenuation;

            channel_remove_el_az = channel_remove_el .* pattern_az;
            channel_remove_el_az(index_zeros) = 0;
            channel_recontract(l,:,:) = channel_remove_el_az * attenuation;

%             channel_recontract(l,:,:) = channel_remove_toa_aoa * sqrt(power(l));

            
            % remove everything from the channel
            channel_sum = sum(channel_recontract,1);
            channel_sum = squeeze(channel_sum);
            channel_residual = channel - channel_sum;

        end
        
    end
    
    
    % take toa and aoa
%     ToA_estimated = times_toa(arg_max_toas);
%     AoA_estimated = rad2deg(angles(arg_max_aoas));
    El_estimated = arg_max_el;
    Az_estimated = arg_max_az;
end



File: /Parse_csi.m
% Parses the AoA results and returns a matrix
function [magnitudes, phases, times] = Parse_csi(filename)

    fid = fopen(filename);
    tline = fgetl(fid);
    
    correct   = 0;
    incorrect = 0;
    
    % This structure will hold the times of each measurement, this
    % way we can check if there are duplicates
    times = zeros(0, 1);
    
    % Magnitude
    magnitudes = zeros(1, 32);
    phases     = zeros(1, 32);
    
    % Read the file line by line
    while ischar(tline)
        
        % A valid line contains the string 'wil6210-aoa$' and has 71 ','
        if contains(tline, "[AOA]") == 1 && count(tline, ",") == 71
             
           % Split the data
           splitted = split(tline, ",");
           
           time = splitted{2};
           
           % Check if the time already exists
           if ~ismember(time, times)
               
               times(end+1, 1) = str2double(time);
           else
               
               disp("duplicated")
               continue
           end
           
          correct = correct + 1;

          % Now we can get the data
          % There are 32 elements
                   
          % Phase
          for i=9:(9+31)
              
              phases(correct, i-8) = str2num(splitted{i});
          end
          
          % Amplitude
          for i=(9+32):(9+32+31)
              
              magnitudes(correct, i-(9+31)) = str2num(splitted{i});
          end
          
        else
            
           incorrect = incorrect +1;
        end
        
        
        % Get next line
        tline = fgetl(fid);
    end
    
    %disp(['In the file ' filename ' there were ' num2str(correct) ' valid entries and ' num2str(incorrect) ' invalid entries, with a ratio of ' num2str(correct/(correct+incorrect))]);
    
    fclose(fid);
end



File: /Parse_ftm.m
% Parses the FTM results and returns a matrix
function [ftm_times] = Parse_ftm(filename)

    fid = fopen(filename);
    tline = fgetl(fid);

    % Save the data
    ftm_times = zeros(0, 4);
    
    % Counter
    curr_measurement = 1;
    
    % Read the file line by line
    while ischar(tline)
        
        % A valid line contains the string '[FTM] Measurement:' and has 3 ','
        if contains(tline, "[FTM] Measurement:") == 1 && count(tline, ",") == 3
             
            % Split the data
            splitted = split(tline, ":");
            
            splitted = split(splitted{6}, " ");

            % Times
            aux = split(splitted{2}, ",");
            t1 = str2num(aux{1});
            
            aux = split(splitted{3}, ",");
            t2 = str2num(aux{1});
            
            aux = split(splitted{4}, ",");
            t3 = str2num(aux{1});
            
            t4 = str2num(splitted{5});
            
            ftm_times(curr_measurement, 1) = t1;
            ftm_times(curr_measurement, 2) = t2;
            ftm_times(curr_measurement, 3) = t3;
            ftm_times(curr_measurement, 4) = t4;

            curr_measurement = curr_measurement + 1;
        end
        
        % Get next line
        tline = fgetl(fid);
    end    
    
    fclose(fid);
end



File: /README.md
# MikroTik antenna calibration + CSI cleaning + mD-Track


This repository includes:

- antennas_mikrotik.mat: A MATLAB binary file with the logical antenna indexing from the MikroTik antennas
- Parse_csi.m: A MATLAB script that reads a CSI capture from the router and transforms it to MATLAB structures
- Parse_ftm.m: A MATLAB script that reads an FTM capture from the router and transforms it to MATLAB structures
- Sanitize.m: A MATLAB script that corrects the CSI captures from the MikroTik devices
- mD-Track: A custom implementation of the mD-Track algorithm to estimate azimut and elevation using CSI data
- Example_data: Some real measurements for the Example.m script
- Example.m: A MATLAB script that shows step by step how to convert CSI and FTM measurements to azimut, elevation and distance
- How to calibrate.md: A tutorial that explains how to calibrate the routers
- Generate_calibration.m: A MATLAB script that aids the creation of the calibration file

### MIT License

Copyright (c) 2021 Alejandro Blanco Pizarro and Pablo Jiménez Mateo

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


File: /Sanitize.m
function [csi_data,offset,converged] = Sanitize(csi_data)
%UNTITLED5 Summary of this function goes here
%   Detailed explanation goes here
% take the data for antenna 2
%     csi_data = csi_data(:,17);

    % create a grid for the possible values
    grid = linspace(-pi,pi,1024);

    % move to complex number
    S_phase = exp(1i*grid);

    % create the spectrum. To do that, we multiply by the conjugate. The phase
    % that maximizes the real part is the correct value
    spectrum_phase = csi_data * conj(S_phase);

    % take the max
    [~, index_max] = max(sum(real(spectrum_phase),1));

    % we center based on the angle that maximizes the real part
    offset_phase = grid(index_max);

    csi_data = csi_data .* conj(S_phase(index_max));

    csi_data = csi_data .* exp(1i*pi/2);


    % apply guaxian mixture model
    GM = fitgmdist(angle(csi_data),2);

    % show the mean of the gaussian distribution
    GM.mu;
    GM.ComponentProportion;
    converged = GM.Converged;
    % order the phase in term of the proportion
    [~, index_sort] = sort(GM.ComponentProportion, "descend");

    mu_sorted = GM.mu(index_sort);
    % take the phase in the middle
    phase_middle = mean(mu_sorted);

    % sum to the outliers pi/2
    if (mu_sorted(2) < mu_sorted(1))
        index_out = angle(csi_data) < phase_middle;
    else
        index_out = angle(csi_data) > phase_middle;
    end

    % check whether is pi/2, pi and 3pi/2
    grid_pi = [pi/2, pi, -pi/2];

    diff_mu = diff(mu_sorted);

    % look for the minimum of the substraction
    sub_diff_mu = diff_mu + grid_pi;
    [~, index_min_mu] = min(abs(sub_diff_mu));


    % analizy when the jump is pi/2, pi or 3*pi/2
    csi_data(index_out) = csi_data(index_out) .* exp(1i*grid_pi(index_min_mu));

    % csi_data = csi_data .* exp(-1i*offset_mu);


    % remove the pi/2 offset
    csi_data = csi_data .* exp(-1i*pi/2);

    % it should be center at 0 or closer to 0
    mean_offset = median(angle(csi_data));

    csi_data = csi_data .* exp(-1i*mean_offset);

    offset = mean_offset + offset_phase;

    csi_data = csi_data*exp(1i*offset);
end


