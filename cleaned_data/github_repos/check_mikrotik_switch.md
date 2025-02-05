# Repository Information
Name: check_mikrotik_switch

# Directory Structure
Directory structure:
└── github_repos/check_mikrotik_switch/
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
    │   │       ├── pack-13b184718d50d1ce36e72c7ff9a1d9fa71f28020.idx
    │   │       └── pack-13b184718d50d1ce36e72c7ff9a1d9fa71f28020.pack
    │   ├── packed-refs
    │   └── refs/
    │       ├── heads/
    │       │   └── master
    │       ├── remotes/
    │       │   └── origin/
    │       │       └── HEAD
    │       └── tags/
    ├── .gitignore
    ├── check_mikrotik_switch.pl
    ├── icingaexchange.yml
    ├── LICENSE
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
	url = https://github.com/bemworld/check_mikrotik_switch.git
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
0000000000000000000000000000000000000000 0248db7218bdc77e31f2bae7ea3b9ea9e9d9493c vivek-dodia <vivek.dodia@icloud.com> 1738606044 -0500	clone: from https://github.com/bemworld/check_mikrotik_switch.git


File: /.git\logs\refs\heads\master
0000000000000000000000000000000000000000 0248db7218bdc77e31f2bae7ea3b9ea9e9d9493c vivek-dodia <vivek.dodia@icloud.com> 1738606044 -0500	clone: from https://github.com/bemworld/check_mikrotik_switch.git


File: /.git\logs\refs\remotes\origin\HEAD
0000000000000000000000000000000000000000 0248db7218bdc77e31f2bae7ea3b9ea9e9d9493c vivek-dodia <vivek.dodia@icloud.com> 1738606044 -0500	clone: from https://github.com/bemworld/check_mikrotik_switch.git


File: /.git\packed-refs
# pack-refs with: peeled fully-peeled sorted 
0248db7218bdc77e31f2bae7ea3b9ea9e9d9493c refs/remotes/origin/master


File: /.git\refs\heads\master
0248db7218bdc77e31f2bae7ea3b9ea9e9d9493c


File: /.git\refs\remotes\origin\HEAD
ref: refs/remotes/origin/master


File: /.gitignore
/nbproject/

File: /check_mikrotik_switch.pl
#!/usr/bin/perl -w

use strict;
use Net::SNMP;
use Set::IntSpan;
use Getopt::Long qw(:config no_ignore_case);

my $snmpSession;
my $host = '127.0.0.1';
my $community = 'public';
my $warn;
my $crit;
my $stat = 0;
my $msg = '';
my $perf = '';
my $type;
my @ports;

my %checkTypeNeedsPorts = map {$_ => 1} qw(portName portOperState portAdminState portMtu portMacAddress portRxDiscards portTxDiscards portTxErrors portRxErrors portRxPackets portTxPackets portTxBytes portRxBytes );

# port statistics are returned as sum, except for those defined in %doNotSumValues.
# checks with value != undef can only handle one port.
my %doNotSumValues = (
    'portName'        => undef,
    'portOperState'  => '',
    'portAdminState' => '',
    'portMtu'         => '',
    'portMacAddress' => undef
);

my %oids = (
    'cpu'                  => ".1.3.6.1.2.1.25.3.3.1.2.1",
    'activeFan'            => '.1.3.6.1.4.1.14988.1.1.3.9.0',
    'voltage'              => '.1.3.6.1.4.1.14988.1.1.3.8.0',
    'temperature'          => '.1.3.6.1.4.1.14988.1.1.3.10.0',
    'processorTemperature' => '.1.3.6.1.4.1.14988.1.1.3.11.0',
    'current'              => '.1.3.6.1.4.1.14988.1.1.3.13.0',
    'powerConsumption'     => '.1.3.6.1.4.1.14988.1.1.3.12.0',
    'psu1State'            => '.1.3.6.1.4.1.14988.1.1.3.15.0',
    'psu2State'            => '.1.3.6.1.4.1.14988.1.1.3.16.0',
    'diskTotal'            => ".1.3.6.1.2.1.25.2.3.1.5.1",
    'diskUsed'             => ".1.3.6.1.2.1.25.2.3.1.6.1",
    'memTotal'             => ".1.3.6.1.2.1.25.2.3.1.5.2",
    'memUsed'              => ".1.3.6.1.2.1.25.2.3.1.6.2",
    'portName'             => '.1.3.6.1.2.1.2.2.1.2',
    'portOperState'        => '.1.3.6.1.2.1.2.2.1.8',
    'portAdminState'       => '.1.3.6.1.2.1.2.2.1.7',
    'portMtu'              => '.1.3.6.1.2.1.2.2.1.4',
    'portMacAddress'       => '.1.3.6.1.2.1.2.2.1.6',
    'portRxDiscards'       => '.1.3.6.1.2.1.2.2.1.13',
    'portTxDiscards'       => '.1.3.6.1.2.1.2.2.1.19',
    'portTxErrors'         => '.1.3.6.1.2.1.2.2.1.20',
    'portRxErrors'         => '.1.3.6.1.2.1.2.2.1.14',
    'portRxPackets'        => '.1.3.6.1.2.1.31.1.1.1.7',
    'portTxPackets'        => '.1.3.6.1.2.1.31.1.1.1.11',
    'portTxBytes'          => '.1.3.6.1.2.1.31.1.1.1.10',
    'portRxBytes'          => '.1.3.6.1.2.1.31.1.1.1.6'
);

sub usage {
    my $message = $_[0];
    
    if (defined $message && length $message) {
      $message .= "\n" unless $message =~ /\n$/;
   }
   print $message;
   my $command = $0;
   $command =~ s#^.*/##;
   
   print STDERR qq{
$message

Usage:
    ${0} 
         -H <ip-address>
         [-C <community>]
         -t <test type>
         [-i <switch ports>]
         -w <warn range>
         -c <crit range>
         
    Parameters:
        -H <ip-address>     The IP address or the host name of the switch
        [-C <community>]    The SNMP community string (default: public) [optional]
        -t <test type>      The test type to execute. See below.
        -w <warn range>     Range for result WARNING, see https://nagios-plugins.org/doc/guidelines.html#THRESHOLDFORMAT
        -c <crit range>     Range for result CRITICAL, see https://nagios-plugins.org/doc/guidelines.html#THRESHOLDFORMAT
            
    Additional parameter, depending on test (testname starts with "port"):
        -i <switch ports>   single, multiple and ranges possible, for example: 1,5-10,22-24
    
    The following test types are available (-t):
            cpu                  
            activeFan            
            voltage              
            temperature          
            processorTemperature 
            current              
            powerConsumption     
            psu1State            
            psu2State            
            diskTotal            
            diskUsed             
            memTotal             
            memUsed              
            portName             
            portOperState        
            portAdminState       
            portMtu              
            portMacAddress       
            portRxDiscards       
            portTxDiscards       
            portTxErrors         
            portRxErrors         
            portRxPackets        
            portTxPackets        
            portTxBytes          
            portRxBytes    
    
    All port results are added up, except for 'portName', 'portOperState', 'portAdminState', 'portMtu', 'portMacAddress'
    
    }
    
}


sub expandPorts {
    my ($optName, $optValue) = @_;
    my $span = Set::IntSpan->new($optValue);
    @ports = $span->elements();
}

sub expandAndValidateRanges {
    my ($optName, $optValue) = @_;
    
    my $range = {
        from    => 0, 
        negInf  => 0, 
        to      => 0, 
        posInf  => 1, 
        alertIf => 'outside'
    };
    
    if($optValue =~ qr/^(\@)?((?:~?)|(?:-?\d+)(?:\.\d+)?)(:)?(-?\d+(?:\.\d+)?)?$/){
        if ($1){
            $range->{alertIf} = 'inside'
        }
        
        if($2){
            if($2 eq '~'){
                $range->{negInf} = 1;
            }else{
                $range->{from} = $2;
            }
        }
        
        if($4){
            $range->{to} = $4;
            $range->{posInf} = 0;
        }
        
        if ($range->{posInf} == 0 && $range->{negInf} == 0 && $range->{from} >= $range->{to}) {
            print "Invalid range definition for -$optName option\n";
            exit 3;
        }
        
        if($optName eq 'w'){
            $warn = $range;
        }else{
            $crit = $range;
        }
       
    }else{
        print "Invalid -$optName value, must be in nagios range format [@][start:]end\n";
        exit 3;
    }
}

sub alertByRange{
    my ($range, $value) = @_;
    my $ok = 0;
    my $alert = 1;
    if ($range->{alertIf} eq 'inside') {
        $ok = 1;
        $alert = 0;
    }
    if ($range->{posInf} == 0 && $range->{negInf} == 0) {
        if ($range->{from} <= $value && $value <= $range->{to}) {
            return $ok;
        } else {
            return $alert;
        }
    } elsif ($range->{negInf} == 0 && $range->{posInf} == 1) {
        if ( $value >= $range->{from} ) {
            return $ok;
        } else {
            return $alert;
        }
    } elsif ($range->{negInf} == 1 && $range->{posInf} == 0) {
        if ($value <= $range->{to}) {
            return $ok;
        } else {
            return $alert;
        }
    } else {
        return $ok;
    }
}

sub createSession {
    my ($switch, $comm) = @_;
    my $snmpVersion = '2c';
    my ($session, $error) = Net::SNMP->session(
        -hostname       => $host,
        -community      => $community,
        -version        => $snmpVersion
    );
    if ($error || !defined($session)) {
        printf('Failed to establish SNMP session (%s)', $error);
        exit 3;
    }
    return $session;
}

sub exitUnknown {
    my ($message, $error) = @_;
    print "$message: $error\n";
    $snmpSession->close;
    exit 3;
}

GetOptions(
    'H=s'   => \$host,
    'C=s'   => \$community,
    'w=s'   => \&expandAndValidateRanges,
    'c=s'   => \&expandAndValidateRanges,
    't=s'   => \$type,
    'i=s'   => \&expandPorts
) or usage("Invalid commmand line options.");
 
if (!(defined $oids{$type} || $type eq 'mem' || $type eq 'disk')){
    usage("Check type $type not supported");
    exit 3;
}

if ($checkTypeNeedsPorts {$type} && !@ports) {
    usage("For check type $type, port list must not be empty");
    exit 3;
}

if (defined $doNotSumValues{$type} && @ports != 1) {
    usage("For check type $type, only one port is allowed");
    exit 3;
}

$snmpSession = createSession($host,$community);

if ($checkTypeNeedsPorts {$type}) {
    my $ret;
    foreach my $port (@ports) {
    
        my $oid = "$oids{$type}.$port";
        my $hashResponse = $snmpSession->get_request(-varbindlist => [$oid]);
        my $response = "$hashResponse->{$oid}";
        
        if (exists $doNotSumValues{$type} && !defined $doNotSumValues {$type}) {
            $ret .= " $response";
        } else {
            $ret += $response;
        }
    }
    
    if (exists $doNotSumValues{$type} && !defined $doNotSumValues{$type}) {
        $msg = "$type: OK - $ret";
    } else {
        if (alertByRange($crit, $ret) == 1) {
            $stat = 2;
            $msg = "$type: Crit - $ret";
        } elsif (alertByRange($warn, $ret) == 1) {
            $stat = 1;
            $msg = "$type: WARN - $ret";
        } else {
            $stat = 0;
            $msg = "$type: OK - $ret";
        }
    }
    
} elsif ($type eq "mem" || $type eq "disk") {

    my $oid = $oids{"$type"."Used"};
    my $hashResponse = $snmpSession->get_request(-varbindlist => [$oid]);
    my $used = "$hashResponse->{$oid}";
    
    if ($used eq '' || $used eq 'n/a' || $used eq 'noSuchInstance'){
        exitUnknown("$type not supported, response", $used);
    }
    
    $oid = $oids{"$type"."Total"};
    $hashResponse = $snmpSession->get_request(-varbindlist => [$oid]);
    my $total = "$hashResponse->{$oid}";
    
    my $free = $total - $used;

    $used = int($used / 1024 / 1024);
    $free = int($free / 1024 / 1024);
    $total = int($total / 1024 / 1024);

    my $freePercent = int($free / $total * 100);
    
    if (alertByRange($crit, $freePercent) == 1) {
        $stat = 2;
        $msg = "$type: CRIT - ";
    } elsif (alertByRange($warn, $freePercent) == 1) {
        $stat = 1;
        $msg = "$type: WARN - ";
    } else {
        $stat = 0;
        $msg = "$type: OK - ";
    }
    
    $msg .= "$type free: $freePercent%";
    $perf = "total=$total"."MB"."used=$used"."MB";
    
} else {

    my $oid = "$oids{$type}";
    my $hashResponse = $snmpSession->get_request(-varbindlist => [$oid]);
    my $response = "$hashResponse->{$oid}";

    if ($response eq '' || $response eq 'n/a' || $response eq 'noSuchInstance'){
        exitUnknown("$type not supported, response", $response);
    } else {
    
        if ($type eq "voltage" || index($type, 'emperature') != -1 || index($type, 'current') != -1 ) {
            $response /= 10;
        }
        
        if (alertByRange($crit, $response) == 1) {
            $stat = 2;
            $msg = "$type: CRIT - ";
        } elsif (alertByRange($warn, $response) == 1) {
            $stat = 1;
            $msg = "$type: WARN - ";
        } else {
            $stat = 0;
            $msg = "$type: OK - ";
        }
        
        $perf = "$type=$response";
    }

    if (index($type, 'emperature') != -1) {
        $response .= "°C";
    } elsif ($type eq 'cpu') {
        $response .= "%";
    } elsif ($type eq 'voltage') {
        $response .= "V";
    }
    $msg .= $response;
    $perf = "$type=$response";
}

$snmpSession->close;

print "$msg | $perf\n";

exit $stat;


File: /icingaexchange.yml
name: check_mikrotik_switch
description: "file:///README.md"
url: "https://github.com/bemworld/check_mikrotik_switch"
tags: MikroTik, Switch, Routerboard, Voltage, Port statistics, Port errors
vendor: ~
target: Network, Hardware, Sensor, Temperature
type: Plugin
license: Simplified BSD License
releases: 
  - 
    name: 0.1
    description: "0.1 Release"
    files: 
      - 
        name: check_mikrotik_switch.pl
        url: "file:///check_mikrotik_switch.pl"
        description: "First release"
        checksum: 999ba90af6d003867984090312197866

File: /LICENSE
Copyright (c) 2015, Bernd Klier <bem@bemworld.de>
All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:

1. Redistributions of source code must retain the above copyright notice, this
   list of conditions and the following disclaimer.
2. Redistributions in binary form must reproduce the above copyright notice,
   this list of conditions and the following disclaimer in the documentation
   and/or other materials provided with the distribution.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR
ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
(INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
(INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

File: /README.md
# check_mikrotik_switch.pl

## Overview

This is a simple check script for Nagios/Icinga to monitor switches from MikroTik.

It is tested with CRS125-24G-1S and CRS226-24G-2S switches. 

Due to the lack of other hardware i couldn't test some features, e.g. memory and disk.

## Author
 Bernd Klier bem -(at)- bemworld.de
 
## Installation

In your Nagios plugins directory run

<pre><code>git clone git@github.com:bemworld/check_mikrotik_switch.git</code></pre>

## Usage


         
	Parameters:
        -H <ip-address>     The IP address or the host name of the switch
        [-C <community>]    The SNMP community string (default: public) [optional]
        -t <test type>      The test type to execute. See below.
        -i <switch ports>   single, multiple and ranges possible, for example: 1,5-10,22-24
        -w <warn range>     Range for result WARNING, standard nagios threshhold format
        -c <crit range>     Range for result CRITICAL, standard nagios threshhold format
        
        
The following test types are available (-t):

            cpu                  
            activeFan            
            voltage              
            temperature          
            processorTemperature 
            current              
            powerConsumption     
            psu1State            
            psu2State
            disk
            diskTotal            
            diskUsed
            mem
            memTotal             
            memUsed              
            portName             
            portOperState        
            portAdminState       
            portMtu              
            portMacAddress       
            portRxDiscards       
            portTxDiscards       
            portTxErrors         
            portRxErrors         
            portRxPackets        
            portTxPackets        
            portTxBytes          
            portRxBytes    
    
   All port results are added up, except for 'portName', 'portOperState', 'portAdminState', 'portMtu', 'portMacAddress'

### Install in Nagios

Create commands, e.g.

<pre><code>
define command {
        command_name                    check_mt_voltage
        command_line                    $USER1$/check_mikrotik_switch.pl -H $HOSTADDRESS$ -C public -t voltage -w $ARG1$ -c $ARG2$
}

define command {
        command_name                    check_mt_cpu
        command_line                    $USER1$/check_mikrotik_switch.pl -H $HOSTADDRESS$ -C public -t cpu -w $ARG1$ -c $ARG2$
}

define command {
        command_name                    check_mt_temp
        command_line                    $USER1$/check_mikrotik_switch.pl -H $HOSTADDRESS$ -C public -t temperature -w $ARG1$ -c $ARG2$
}

define command {
        command_name                    check_mt_port_sum
        command_line                    $USER1$/check_mikrotik_switch.pl -H $HOSTADDRESS$ -C public -t $ARG1$ -i $ARG2$ -w $ARG3$ -c $ARG4$
}

define command {
        command_name                    check_mt_port_info
        command_line                    $USER1$/check_mikrotik_switch.pl -H $HOSTADDRESS$ -C public -t $ARG1$ -i $ARG2$
}

</code></pre>


### Service samples

#### Check Voltage

This will check each host that is listed in the MikroTik Switches group. It will issue a warning if the voltage is below 23V or above 26V and a critical error if it is below 22V or above 27V

<pre><code>
define service {
        use                     generic-service
        hostgroup_name          MikroTik Switches
        service_description     MikroTik Voltage
        check_command           check_mt_voltage!23:26!22:27
}
</code></pre>

#### Check TX Errors

This test adds up all tx-errors on ports 1-25 (all ports on a CRS125-24G-1S). 

<pre><code>
define service {
        use                     generic-service
        hostgroup_name          MikroTik Switches
        service_description     MikroTik TX Errors
        check_command           check_mt_port_sum!portTxErrors!1-25!10!50
}
</code></pre>

#### Port Names

This test returns the port names of ports 1, 3, 4, 5 and 25
<pre><code>
define service {
        use                     generic-service
        hostgroup_name          MikroTik Switches
        service_description     MikroTik Port Names
        check_command           check_mt_port_info!portName!1,3-5,25
}
</code></pre>


