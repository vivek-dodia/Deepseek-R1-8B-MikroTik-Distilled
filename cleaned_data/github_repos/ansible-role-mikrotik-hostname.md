# Repository Information
Name: ansible-role-mikrotik-hostname

# Directory Structure
Directory structure:
└── github_repos/ansible-role-mikrotik-hostname/
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
    │   │       ├── pack-3018eb7ba8fc528558d2c411cb4c4d60cc3096df.idx
    │   │       └── pack-3018eb7ba8fc528558d2c411cb4c4d60cc3096df.pack
    │   ├── packed-refs
    │   └── refs/
    │       ├── heads/
    │       │   └── master
    │       ├── remotes/
    │       │   └── origin/
    │       │       └── HEAD
    │       └── tags/
    ├── .gitignore
    ├── ansible.cfg
    ├── defaults/
    │   └── main.yml
    ├── Pipfile
    ├── Pipfile.lock
    ├── playbook.yml
    ├── README.md
    ├── tasks/
    │   └── main.yml
    └── Vagrantfile


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
	url = https://github.com/jugatsu/ansible-role-mikrotik-hostname.git
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
0000000000000000000000000000000000000000 48f979f0e742378147520801549cf7f5749744dd vivek-dodia <vivek.dodia@icloud.com> 1738606367 -0500	clone: from https://github.com/jugatsu/ansible-role-mikrotik-hostname.git


File: /.git\logs\refs\heads\master
0000000000000000000000000000000000000000 48f979f0e742378147520801549cf7f5749744dd vivek-dodia <vivek.dodia@icloud.com> 1738606367 -0500	clone: from https://github.com/jugatsu/ansible-role-mikrotik-hostname.git


File: /.git\logs\refs\remotes\origin\HEAD
0000000000000000000000000000000000000000 48f979f0e742378147520801549cf7f5749744dd vivek-dodia <vivek.dodia@icloud.com> 1738606367 -0500	clone: from https://github.com/jugatsu/ansible-role-mikrotik-hostname.git


File: /.git\packed-refs
# pack-refs with: peeled fully-peeled sorted 
e078db942970ac441ec8b294d6e359214c4d9942 refs/remotes/origin/dependabot/pip/ansible-2.9.20
0d8a9cfa92f5e2dcd36bbfd590cdffd545b7e5d4 refs/remotes/origin/dependabot/pip/cryptography-3.2
b9c1f77920aedd156022e84365973d190dc28ce3 refs/remotes/origin/dependabot/pip/py-1.10.0
b70c987a1888d65bcd7b0416486faa7e421debf7 refs/remotes/origin/dependabot/pip/urllib3-1.26.5
48f979f0e742378147520801549cf7f5749744dd refs/remotes/origin/master


File: /.git\refs\heads\master
48f979f0e742378147520801549cf7f5749744dd


File: /.git\refs\remotes\origin\HEAD
ref: refs/remotes/origin/master


File: /.gitignore
# Vagrant
.vagrant

# Packer
packer_cache
output/virtualbox*
box/*.box

# Test-kitchen
.kitchen


File: /ansible.cfg
[defaults]
roles_path = ../
host_key_checking = False
retry_files_enabled = False
nocows = True


File: /defaults\main.yml
---
# defaults file for ansible-role-mikrotic-hostname

mikrotik_hostname: MikroTik


File: /Pipfile
[[source]]
url = "https://pypi.python.org/simple"
verify_ssl = true
name = "pypi"

[packages]
ansible = "*"
molecule = "*"
docker-py = "*"
pywinrm = ">=0.3.0"
python-vagrant = ""

[dev-packages]

[requires]
python_version = "2.7"


File: /Pipfile.lock
{
    "_meta": {
        "hash": {
            "sha256": "7ab91b858172efbd620c06050555d5af47cb5bc2f409ecd9919aa331c9d7bbd0"
        },
        "pipfile-spec": 6,
        "requires": {
            "python_version": "2.7"
        },
        "sources": [
            {
                "name": "pypi",
                "url": "https://pypi.python.org/simple",
                "verify_ssl": true
            }
        ]
    },
    "default": {
        "ansible": {
            "hashes": [
                "sha256:a1ab8e0f13e79a20661ad6546f45a142afeaeb664deb2c290e32362d8ae5b618"
            ],
            "index": "pypi",
            "version": "==2.7.0"
        },
        "ansible-lint": {
            "hashes": [
                "sha256:7686dad54aab9281562a5788415af1488b9af8a5acc99c042ecb9959b6ab7a57"
            ],
            "version": "==3.4.23"
        },
        "anyconfig": {
            "hashes": [
                "sha256:4d6016ae6eecc5e502bc7e99ae0639c5710c5c67bde5f21b06b9eaafd9ce0e7e"
            ],
            "version": "==0.9.7"
        },
        "arrow": {
            "hashes": [
                "sha256:a558d3b7b6ce7ffc74206a86c147052de23d3d4ef0e17c210dd478c53575c4cd"
            ],
            "version": "==0.12.1"
        },
        "asn1crypto": {
            "hashes": [
                "sha256:2f1adbb7546ed199e3c90ef23ec95c5cf3585bac7d11fb7eb562a3fe89c64e87",
                "sha256:9d5c20441baf0cb60a4ac34cc447c6c189024b6b4c6cd7877034f4965c464e49"
            ],
            "version": "==0.24.0"
        },
        "atomicwrites": {
            "hashes": [
                "sha256:0312ad34fcad8fac3704d441f7b317e50af620823353ec657a53e981f92920c0",
                "sha256:ec9ae8adaae229e4f8446952d204a3e4b5fdd2d099f9be3aaf556120135fb3ee"
            ],
            "version": "==1.2.1"
        },
        "attrs": {
            "hashes": [
                "sha256:10cbf6e27dbce8c30807caf056c8eb50917e0eaafe86347671b57254006c3e69",
                "sha256:ca4be454458f9dec299268d472aaa5a11f67a4ff70093396e1ceae9c76cf4bbb"
            ],
            "version": "==18.2.0"
        },
        "backports.functools-lru-cache": {
            "hashes": [
                "sha256:9d98697f088eb1b0fa451391f91afb5e3ebde16bbdb272819fd091151fda4f1a",
                "sha256:f0b0e4eba956de51238e17573b7087e852dfe9854afd2e9c873f73fc0ca0a6dd"
            ],
            "version": "==1.5"
        },
        "backports.ssl-match-hostname": {
            "hashes": [
                "sha256:502ad98707319f4a51fa2ca1c677bd659008d27ded9f6380c79e8932e38dcdf2"
            ],
            "markers": "python_version < '3.5'",
            "version": "==3.5.0.1"
        },
        "bcrypt": {
            "hashes": [
                "sha256:01477981abf74e306e8ee31629a940a5e9138de000c6b0898f7f850461c4a0a5",
                "sha256:054d6e0acaea429e6da3613fcd12d05ee29a531794d96f6ab959f29a39f33391",
                "sha256:0872eeecdf9a429c1420158500eedb323a132bc5bf3339475151c52414729e70",
                "sha256:09a3b8c258b815eadb611bad04ca15ec77d86aa9ce56070e1af0d5932f17642a",
                "sha256:0f317e4ffbdd15c3c0f8ab5fbd86aa9aabc7bea18b5cc5951b456fe39e9f738c",
                "sha256:2788c32673a2ad0062bea850ab73cffc0dba874db10d7a3682b6f2f280553f20",
                "sha256:321d4d48be25b8d77594d8324c0585c80ae91ac214f62db9098734e5e7fb280f",
                "sha256:346d6f84ff0b493dbc90c6b77136df83e81f903f0b95525ee80e5e6d5e4eef84",
                "sha256:34dd60b90b0f6de94a89e71fcd19913a30e83091c8468d0923a93a0cccbfbbff",
                "sha256:3b4c23300c4eded8895442c003ae9b14328ae69309ac5867e7530de8bdd7875d",
                "sha256:43d1960e7db14042319c46925892d5fa99b08ff21d57482e6f5328a1aca03588",
                "sha256:49e96267cd9be55a349fd74f9852eb9ae2c427cd7f6455d0f1765d7332292832",
                "sha256:63e06ffdaf4054a89757a3a1ab07f1b922daf911743114a54f7c561b9e1baa58",
                "sha256:67ed1a374c9155ec0840214ce804616de49c3df9c5bc66740687c1c9b1cd9e8d",
                "sha256:6b662a5669186439f4f583636c8d6ea77cf92f7cfe6aae8d22edf16c36840574",
                "sha256:6efd9ca20aefbaf2e7e6817a2c6ed4a50ff6900fafdea1bcb1d0e9471743b144",
                "sha256:8569844a5d8e1fdde4d7712a05ab2e6061343ac34af6e7e3d7935b2bd1907bfd",
                "sha256:8629ea6a8a59f865add1d6a87464c3c676e60101b8d16ef404d0a031424a8491",
                "sha256:988cac675e25133d01a78f2286189c1f01974470817a33eaf4cfee573cfb72a5",
                "sha256:9a6fedda73aba1568962f7543a1f586051c54febbc74e87769bad6a4b8587c39",
                "sha256:9eced8962ce3b7124fe20fd358cf8c7470706437fa064b9874f849ad4c5866fc",
                "sha256:a005ed6163490988711ff732386b08effcbf8df62ae93dd1e5bda0714fad8afb",
                "sha256:ae35dbcb6b011af6c840893b32399252d81ff57d52c13e12422e16b5fea1d0fb",
                "sha256:b1e8491c6740f21b37cca77bc64677696a3fb9f32360794d57fa8477b7329eda",
                "sha256:c906bdb482162e9ef48eea9f8c0d967acceb5c84f2d25574c7d2a58d04861df1",
                "sha256:cb18ffdc861dbb244f14be32c47ab69604d0aca415bee53485fcea4f8e93d5ef",
                "sha256:cc2f24dc1c6c88c56248e93f28d439ee4018338567b0bbb490ea26a381a29b1e",
                "sha256:d860c7fff18d49e20339fc6dffc2d485635e36d4b2cccf58f45db815b64100b4",
                "sha256:d86da365dda59010ba0d1ac45aa78390f56bf7f992e65f70b3b081d5e5257b09",
                "sha256:e22f0997622e1ceec834fd25947dc2ee2962c2133ea693d61805bc867abaf7ea",
                "sha256:f2fe545d27a619a552396533cddf70d83cecd880a611cdfdbb87ca6aec52f66b",
                "sha256:f425e925485b3be48051f913dbe17e08e8c48588fdf44a26b8b14067041c0da6",
                "sha256:f7fd3ed3745fe6e81e28dc3b3d76cce31525a91f32a387e1febd6b982caf8cdb",
                "sha256:f9210820ee4818d84658ed7df16a7f30c9fba7d8b139959950acef91745cc0f7"
            ],
            "version": "==3.1.4"
        },
        "binaryornot": {
            "hashes": [
                "sha256:359501dfc9d40632edc9fac890e19542db1a287bbcfa58175b66658392018061",
                "sha256:b8b71173c917bddcd2c16070412e369c3ed7f0528926f70cac18a6c97fd563e4"
            ],
            "version": "==0.4.4"
        },
        "cerberus": {
            "hashes": [
                "sha256:f5c2e048fb15ecb3c088d192164316093fcfa602a74b3386eefb2983aa7e800a"
            ],
            "version": "==1.2"
        },
        "certifi": {
            "hashes": [
                "sha256:376690d6f16d32f9d1fe8932551d80b23e9d393a8578c5633a2ed39a64861638",
                "sha256:456048c7e371c089d0a77a5212fb37a2c2dce1e24146e3b7e0261736aaeaa22a"
            ],
            "version": "==2018.8.24"
        },
        "cffi": {
            "hashes": [
                "sha256:151b7eefd035c56b2b2e1eb9963c90c6302dc15fbd8c1c0a83a163ff2c7d7743",
                "sha256:1553d1e99f035ace1c0544050622b7bc963374a00c467edafac50ad7bd276aef",
                "sha256:1b0493c091a1898f1136e3f4f991a784437fac3673780ff9de3bcf46c80b6b50",
                "sha256:2ba8a45822b7aee805ab49abfe7eec16b90587f7f26df20c71dd89e45a97076f",
                "sha256:3bb6bd7266598f318063e584378b8e27c67de998a43362e8fce664c54ee52d30",
                "sha256:3c85641778460581c42924384f5e68076d724ceac0f267d66c757f7535069c93",
                "sha256:3eb6434197633b7748cea30bf0ba9f66727cdce45117a712b29a443943733257",
                "sha256:495c5c2d43bf6cebe0178eb3e88f9c4aa48d8934aa6e3cddb865c058da76756b",
                "sha256:4c91af6e967c2015729d3e69c2e51d92f9898c330d6a851bf8f121236f3defd3",
                "sha256:57b2533356cb2d8fac1555815929f7f5f14d68ac77b085d2326b571310f34f6e",
                "sha256:770f3782b31f50b68627e22f91cb182c48c47c02eb405fd689472aa7b7aa16dc",
                "sha256:79f9b6f7c46ae1f8ded75f68cf8ad50e5729ed4d590c74840471fc2823457d04",
                "sha256:7a33145e04d44ce95bcd71e522b478d282ad0eafaf34fe1ec5bbd73e662f22b6",
                "sha256:857959354ae3a6fa3da6651b966d13b0a8bed6bbc87a0de7b38a549db1d2a359",
                "sha256:87f37fe5130574ff76c17cab61e7d2538a16f843bb7bca8ebbc4b12de3078596",
                "sha256:95d5251e4b5ca00061f9d9f3d6fe537247e145a8524ae9fd30a2f8fbce993b5b",
                "sha256:9d1d3e63a4afdc29bd76ce6aa9d58c771cd1599fbba8cf5057e7860b203710dd",
                "sha256:a36c5c154f9d42ec176e6e620cb0dd275744aa1d804786a71ac37dc3661a5e95",
                "sha256:a6a5cb8809091ec9ac03edde9304b3ad82ad4466333432b16d78ef40e0cce0d5",
                "sha256:ae5e35a2c189d397b91034642cb0eab0e346f776ec2eb44a49a459e6615d6e2e",
                "sha256:b0f7d4a3df8f06cf49f9f121bead236e328074de6449866515cea4907bbc63d6",
                "sha256:b75110fb114fa366b29a027d0c9be3709579602ae111ff61674d28c93606acca",
                "sha256:ba5e697569f84b13640c9e193170e89c13c6244c24400fc57e88724ef610cd31",
                "sha256:be2a9b390f77fd7676d80bc3cdc4f8edb940d8c198ed2d8c0be1319018c778e1",
                "sha256:ca1bd81f40adc59011f58159e4aa6445fc585a32bb8ac9badf7a2c1aa23822f2",
                "sha256:d5d8555d9bfc3f02385c1c37e9f998e2011f0db4f90e250e5bc0c0a85a813085",
                "sha256:e55e22ac0a30023426564b1059b035973ec82186ddddbac867078435801c7801",
                "sha256:e90f17980e6ab0f3c2f3730e56d1fe9bcba1891eeea58966e89d352492cc74f4",
                "sha256:ecbb7b01409e9b782df5ded849c178a0aa7c906cf8c5a67368047daab282b184",
                "sha256:ed01918d545a38998bfa5902c7c00e0fee90e957ce036a4000a88e3fe2264917",
                "sha256:edabd457cd23a02965166026fd9bfd196f4324fe6032e866d0f3bd0301cd486f",
                "sha256:fdf1c1dc5bafc32bc5d08b054f94d659422b05aba244d6be4ddc1c72d9aa70fb"
            ],
            "version": "==1.11.5"
        },
        "chardet": {
            "hashes": [
                "sha256:84ab92ed1c4d4f16916e05906b6b75a6c0fb5db821cc65e70cbd64a3e2a5eaae",
                "sha256:fc323ffcaeaed0e0a02bf4d117757b98aed530d9ed4531e3e15460124c106691"
            ],
            "version": "==3.0.4"
        },
        "click": {
            "hashes": [
                "sha256:29f99fc6125fbc931b758dc053b3114e55c77a6e4c6c3a2674a2dc986016381d",
                "sha256:f15516df478d5a56180fbf80e68f206010e6d160fc39fa508b65e035fd75130b"
            ],
            "version": "==6.7"
        },
        "click-completion": {
            "hashes": [
                "sha256:7ca12978493a7450486cef155845af4fae48744c3f97b7250a254de65c9e5e5a"
            ],
            "version": "==0.3.1"
        },
        "colorama": {
            "hashes": [
                "sha256:463f8483208e921368c9f306094eb6f725c6ca42b0f97e313cb5d5512459feda",
                "sha256:48eb22f4f8461b1df5734a074b57042430fb06e1d61bd1e11b078c0fe6d7a1f1"
            ],
            "version": "==0.3.9"
        },
        "configparser": {
            "hashes": [
                "sha256:5308b47021bc2340965c371f0f058cc6971a04502638d4244225c49d80db273a"
            ],
            "markers": "python_version < '3.2'",
            "version": "==3.5.0"
        },
        "cookiecutter": {
            "hashes": [
                "sha256:1316a52e1c1f08db0c9efbf7d876dbc01463a74b155a0d83e722be88beda9a3e",
                "sha256:ed8f54a8fc79b6864020d773ce11539b5f08e4617f353de1f22d23226f6a0d36"
            ],
            "version": "==1.6.0"
        },
        "cryptography": {
            "hashes": [
                "sha256:02602e1672b62e803e08617ec286041cc453e8d43f093a5f4162095506bc0beb",
                "sha256:10b48e848e1edb93c1d3b797c83c72b4c387ab0eb4330aaa26da8049a6cbede0",
                "sha256:17db09db9d7c5de130023657be42689d1a5f60502a14f6f745f6f65a6b8195c0",
                "sha256:227da3a896df1106b1a69b1e319dce218fa04395e8cc78be7e31ca94c21254bc",
                "sha256:2cbaa03ac677db6c821dac3f4cdfd1461a32d0615847eedbb0df54bb7802e1f7",
                "sha256:31db8febfc768e4b4bd826750a70c79c99ea423f4697d1dab764eb9f9f849519",
                "sha256:4a510d268e55e2e067715d728e4ca6cd26a8e9f1f3d174faf88e6f2cb6b6c395",
                "sha256:6a88d9004310a198c474d8a822ee96a6dd6c01efe66facdf17cb692512ae5bc0",
                "sha256:76936ec70a9b72eb8c58314c38c55a0336a2b36de0c7ee8fb874a4547cadbd39",
                "sha256:7e3b4aecc4040928efa8a7cdaf074e868af32c58ffc9bb77e7bf2c1a16783286",
                "sha256:8168bcb08403ef144ff1fb880d416f49e2728101d02aaadfe9645883222c0aa5",
                "sha256:8229ceb79a1792823d87779959184a1bf95768e9248c93ae9f97c7a2f60376a1",
                "sha256:8a19e9f2fe69f6a44a5c156968d9fc8df56d09798d0c6a34ccc373bb186cee86",
                "sha256:8d10113ca826a4c29d5b85b2c4e045ffa8bad74fb525ee0eceb1d38d4c70dfd6",
                "sha256:be495b8ec5a939a7605274b6e59fbc35e76f5ad814ae010eb679529671c9e119",
                "sha256:dc2d3f3b1548f4d11786616cf0f4415e25b0fbecb8a1d2cd8c07568f13fdde38",
                "sha256:e4aecdd9d5a3d06c337894c9a6e2961898d3f64fe54ca920a72234a3de0f9cb3",
                "sha256:e79ab4485b99eacb2166f3212218dd858258f374855e1568f728462b0e6ee0d9",
                "sha256:f995d3667301e1754c57b04e0bae6f0fa9d710697a9f8d6712e8cca02550910f"
            ],
            "version": "==2.3.1"
        },
        "docker-py": {
            "hashes": [
                "sha256:35b506e95861914fa5ad57a6707e3217b4082843b883be246190f57013948aba",
                "sha256:4c2a75875764d38d67f87bc7d03f7443a3895704efc57962bdf6500b8d4bc415"
            ],
            "index": "pypi",
            "version": "==1.10.6"
        },
        "docker-pycreds": {
            "hashes": [
                "sha256:0a941b290764ea7286bd77f54c0ace43b86a8acd6eb9ead3de9840af52384079",
                "sha256:8b0e956c8d206f832b06aa93a710ba2c3bcbacb5a314449c040b0b814355bbff"
            ],
            "version": "==0.3.0"
        },
        "enum34": {
            "hashes": [
                "sha256:2d81cbbe0e73112bdfe6ef8576f2238f2ba27dd0d55752a776c41d38b7da2850",
                "sha256:644837f692e5f550741432dd3f223bbb9852018674981b1664e5dc339387588a",
                "sha256:6bd0f6ad48ec2aa117d3d141940d484deccda84d4fcd884f5c3d93c23ecd8c79",
                "sha256:8ad8c4783bf61ded74527bffb48ed9b54166685e4230386a9ed9b1279e2df5b1"
            ],
            "markers": "python_version < '3.4'",
            "version": "==1.1.6"
        },
        "fasteners": {
            "hashes": [
                "sha256:427c76773fe036ddfa41e57d89086ea03111bbac57c55fc55f3006d027107e18",
                "sha256:564a115ff9698767df401efca29620cbb1a1c2146b7095ebd304b79cc5807a7c"
            ],
            "version": "==0.14.1"
        },
        "flake8": {
            "hashes": [
                "sha256:7253265f7abd8b313e3892944044a365e3f4ac3fcdcfb4298f55ee9ddf188ba0",
                "sha256:c7841163e2b576d435799169b78703ad6ac1bbb0f199994fc05f700b2a90ea37"
            ],
            "version": "==3.5.0"
        },
        "funcsigs": {
            "hashes": [
                "sha256:330cc27ccbf7f1e992e69fef78261dc7c6569012cf397db8d3de0234e6c937ca",
                "sha256:a7bb0f2cf3a3fd1ab2732cb49eba4252c2af4240442415b4abce3b87022a8f50"
            ],
            "markers": "python_version < '3.0'",
            "version": "==1.0.2"
        },
        "future": {
            "hashes": [
                "sha256:e39ced1ab767b5936646cedba8bcce582398233d6a627067d4c6a454c90cfedb"
            ],
            "version": "==0.16.0"
        },
        "git-url-parse": {
            "hashes": [
                "sha256:7929b594725394b34008fae557991eed727afab9521937fd59f565105361ec81",
                "sha256:a7d1dba7fc253dff8afb7b683af35834864c9796eb130b44ec63b2584bbc6522",
                "sha256:d647f3d7b10b6aec4a14495c45b2bd500dcfa73d2711578ef2149879bbcdf06d"
            ],
            "version": "==1.1.0"
        },
        "idna": {
            "hashes": [
                "sha256:156a6814fb5ac1fc6850fb002e0852d56c0c8d2531923a51032d1b70760e186e",
                "sha256:684a38a6f903c1d71d6d5fac066b58d7768af4de2b832e426ec79c30daa94a16"
            ],
            "version": "==2.7"
        },
        "ipaddress": {
            "hashes": [
                "sha256:64b28eec5e78e7510698f6d4da08800a5c575caa4a286c93d651c5d3ff7b6794",
                "sha256:b146c751ea45cad6188dd6cf2d9b757f6f4f8d6ffb96a023e6f2e26eea02a72c"
            ],
            "markers": "python_version < '3.3'",
            "version": "==1.0.22"
        },
        "jinja2": {
            "hashes": [
                "sha256:74c935a1b8bb9a3947c50a54766a969d4846290e1e788ea44c1392163723c3bd",
                "sha256:f84be1bb0040caca4cea721fcbbbbd61f9be9464ca236387158b0feea01914a4"
            ],
            "version": "==2.10"
        },
        "jinja2-time": {
            "hashes": [
                "sha256:d14eaa4d315e7688daa4969f616f226614350c48730bfa1692d2caebd8c90d40",
                "sha256:d3eab6605e3ec8b7a0863df09cc1d23714908fa61aa6986a845c20ba488b4efa"
            ],
            "version": "==0.2.0"
        },
        "markupsafe": {
            "hashes": [
                "sha256:a6be69091dac236ea9c6bc7d012beab42010fa914c459791d627dad4910eb665"
            ],
            "version": "==1.0"
        },
        "mccabe": {
            "hashes": [
                "sha256:ab8a6258860da4b6677da4bd2fe5dc2c659cff31b3ee4f7f5d64e79735b80d42",
                "sha256:dd8d182285a0fe56bace7f45b5e7d1a6ebcbf524e8f3bd87eb0f125271b8831f"
            ],
            "version": "==0.6.1"
        },
        "molecule": {
            "hashes": [
                "sha256:438440c851898ef7a6ba659cc8c691ff6422d05cc5233ff862698ff82732181f",
                "sha256:5892fb121e535cb4f530779f63f27b508ddc14d8c8fddb719eb17b54e5c4d438",
                "sha256:b97885056a0acb1a811afa79911730855b7d11f5c74cf06465f5c5ef8629d974"
            ],
            "index": "pypi",
            "version": "==2.18.1"
        },
        "monotonic": {
            "hashes": [
                "sha256:23953d55076df038541e648a53676fb24980f7a1be290cdda21300b3bc21dfb0",
                "sha256:552a91f381532e33cbd07c6a2655a21908088962bb8fa7239ecbcc6ad1140cc7"
            ],
            "version": "==1.5"
        },
        "more-itertools": {
            "hashes": [
                "sha256:c187a73da93e7a8acc0001572aebc7e3c69daf7bf6881a2cea10650bd4420092",
                "sha256:c476b5d3a34e12d40130bc2f935028b5f636df8f372dc2c1c01dc19681b2039e",
                "sha256:fcbfeaea0be121980e15bc97b3817b5202ca73d0eae185b4550cbfce2a3ebb3d"
            ],
            "version": "==4.3.0"
        },
        "ntlm-auth": {
            "hashes": [
                "sha256:7bc02a3fbdfee7275d3dc20fce8028ed8eb6d32364637f28be9e9ae9160c6d5c",
                "sha256:9b13eaf88f16a831637d75236a93d60c0049536715aafbf8190ba58a590b023e"
            ],
            "version": "==1.2.0"
        },
        "paramiko": {
            "hashes": [
                "sha256:3c16b2bfb4c0d810b24c40155dbfd113c0521e7e6ee593d704e84b4c658a1f3b",
                "sha256:a8975a7df3560c9f1e2b43dc54ebd40fd00a7017392ca5445ce7df409f900fcb"
            ],
            "version": "==2.4.2"
        },
        "pathlib2": {
            "hashes": [
                "sha256:8eb170f8d0d61825e09a95b38be068299ddeda82f35e96c3301a8a5e7604cb83",
                "sha256:d1aa2a11ba7b8f7b21ab852b1fb5afb277e1bb99d5dfc663380b5015c0d80c5a"
            ],
            "markers": "python_version < '3.6'",
            "version": "==2.3.2"
        },
        "pathspec": {
            "hashes": [
                "sha256:54a5eab895d89f342b52ba2bffe70930ef9f8d96e398cccf530d21fa0516a873"
            ],
            "version": "==0.5.9"
        },
        "pbr": {
            "hashes": [
                "sha256:4f2b11d95917af76e936811be8361b2b19616e5ef3b55956a429ec7864378e0c",
                "sha256:e0f23b61ec42473723b2fec2f33fb12558ff221ee551962f01dd4de9053c2055"
            ],
            "version": "==4.1.0"
        },
        "pexpect": {
            "hashes": [
                "sha256:2a8e88259839571d1251d278476f3eec5db26deb73a70be5ed5dc5435e418aba",
                "sha256:3fbd41d4caf27fa4a377bfd16fef87271099463e6fa73e92a52f92dfee5d425b"
            ],
            "version": "==4.6.0"
        },
        "pluggy": {
            "hashes": [
                "sha256:6e3836e39f4d36ae72840833db137f7b7d35105079aee6ec4a62d9f80d594dd1",
                "sha256:95eb8364a4708392bae89035f45341871286a333f749c3141c20573d2b3876e1"
            ],
            "version": "==0.7.1"
        },
        "poyo": {
            "hashes": [
                "sha256:c34a5413191210ed564640510e9c4a4ba3b698746d6b454d46eb5bfb30edcd1d",
                "sha256:d1c317054145a6b1ca0608b5e676b943ddc3bfd671f886a2fe09288b98221edb"
            ],
            "version": "==0.4.2"
        },
        "psutil": {
            "hashes": [
                "sha256:0ff2b16e9045d01edb1dd10d7fbcc184012e37f6cd38029e959f2be9c6223f50",
                "sha256:254adb6a27c888f141d2a6032ae231d8ed4fc5f7583b4c825e5f7d7c78d26d2e",
                "sha256:319e12f6bae4d4d988fbff3bed792953fa3b44c791f085b0a1a230f755671ef7",
                "sha256:529ae235896efb99a6f77653a7138273ab701ec9f0343a1f5030945108dee3c4",
                "sha256:686e5a35fe4c0acc25f3466c32e716f2d498aaae7b7edc03e2305b682226bcf6",
                "sha256:6d981b4d863b20c8ceed98b8ac3d1ca7f96d28707a80845d360fa69c8fc2c44b",
                "sha256:7789885a72aa3075d28d028236eb3f2b84d908f81d38ad41769a6ddc2fd81b7c",
                "sha256:7f4616bcb44a6afda930cfc40215e5e9fa7c6896e683b287c771c937712fbe2f",
                "sha256:7fdb3d02bfd68f508e6745021311a4a4dbfec53fca03721474e985f310e249ba",
                "sha256:a9b85b335b40a528a8e2a6b549592138de8429c6296e7361892958956e6a73cf",
                "sha256:dc85fad15ef98103ecc047a0d81b55bbf5fe1b03313b96e883acc2e2fa87ed5c"
            ],
            "markers": "sys_platform != 'win32' and sys_platform != 'cygwin'",
            "version": "==5.4.6"
        },
        "ptyprocess": {
            "hashes": [
                "sha256:923f299cc5ad920c68f2bc0bc98b75b9f838b93b599941a6b63ddbc2476394c0",
                "sha256:d7cc528d76e76342423ca640335bd3633420dc1366f258cb31d05e865ef5ca1f"
            ],
            "version": "==0.6.0"
        },
        "py": {
            "hashes": [
                "sha256:bf92637198836372b520efcba9e020c330123be8ce527e535d185ed4b6f45694",
                "sha256:e76826342cefe3c3d5f7e8ee4316b80d1dd8a300781612ddbc765c17ba25a6c6"
            ],
            "version": "==1.7.0"
        },
        "pyasn1": {
            "hashes": [
                "sha256:0ad0fe0593dde1e599cac0bf65bb1a4ec663032f0bc68ee44850db4251e8c501",
                "sha256:13794d835643ee970b2c059dbfe4eb5d751e16c693c8baee61c526abd209e5c7",
                "sha256:49a8ed515f26913049113820b462f698e6ed26df62c389dafb6fa3685ddca8de",
                "sha256:74ac8521a0480f228549be20bea555ae35678f0e754c2fbc6f1576b0959bec43",
                "sha256:89399ca8ecd4524f974e926d4ef9e7a787903e01f0a9cdff3131ad1361792fe5",
                "sha256:8f291e0338d519a1a0d07f0b9d03c9265f6be26eb32fdd21af6d3259d14ea49c",
                "sha256:b9d3abc5031e61927c82d4d96c1cec1e55676c1a991623cfed28faea73cdd7ca",
                "sha256:d3bbd726c1a760d4ca596a4d450c380b81737612fe0182f5bb3caebc17461fd9",
                "sha256:dea873d6c907c1cf1341fd88742a61efce33227d7743cb37564ab7d7e77dd9fd",
                "sha256:ded5eea5cb88bc1ce9aa074b5a3092f95ce4741887e317e9b49c7ece75d7ea0e",
                "sha256:e8b69ea2200d42201cbedd486eedb8980f320d4534f83ce2fb468e96aa5545d0",
                "sha256:edad117649643230493aeb4955456ce19ab4b12e94489dde6f7094cdb5a3c87e",
                "sha256:f58f2a3d12fd754aa123e9fa74fb7345333000a035f3921dbdaa08597aa53137"
            ],
            "version": "==0.4.4"
        },
        "pycodestyle": {
            "hashes": [
                "sha256:682256a5b318149ca0d2a9185d365d8864a768a28db66a84a2ea946bcc426766",
                "sha256:6c4245ade1edfad79c3446fadfc96b0de2759662dc29d07d80a6f27ad1ca6ba9"
            ],
            "version": "==2.3.1"
        },
        "pycparser": {
            "hashes": [
                "sha256:a988718abfad80b6b157acce7bf130a30876d27603738ac39f140993246b25b3"
            ],
            "version": "==2.19"
        },
        "pyflakes": {
            "hashes": [
                "sha256:08bd6a50edf8cffa9fa09a463063c425ecaaf10d1eb0335a7e8b1401aef89e6f",
                "sha256:8d616a382f243dbf19b54743f280b80198be0bca3a5396f1d2e1fca6223e8805"
            ],
            "version": "==1.6.0"
        },
        "pynacl": {
            "hashes": [
                "sha256:05c26f93964373fc0abe332676cb6735f0ecad27711035b9472751faa8521255",
                "sha256:0c6100edd16fefd1557da078c7a31e7b7d7a52ce39fdca2bec29d4f7b6e7600c",
                "sha256:0d0a8171a68edf51add1e73d2159c4bc19fc0718e79dec51166e940856c2f28e",
                "sha256:1c780712b206317a746ace34c209b8c29dbfd841dfbc02aa27f2084dd3db77ae",
                "sha256:2424c8b9f41aa65bbdbd7a64e73a7450ebb4aa9ddedc6a081e7afcc4c97f7621",
                "sha256:2d23c04e8d709444220557ae48ed01f3f1086439f12dbf11976e849a4926db56",
                "sha256:30f36a9c70450c7878053fa1344aca0145fd47d845270b43a7ee9192a051bf39",
                "sha256:37aa336a317209f1bb099ad177fef0da45be36a2aa664507c5d72015f956c310",
                "sha256:4943decfc5b905748f0756fdd99d4f9498d7064815c4cf3643820c9028b711d1",
                "sha256:57ef38a65056e7800859e5ba9e6091053cd06e1038983016effaffe0efcd594a",
                "sha256:5bd61e9b44c543016ce1f6aef48606280e45f892a928ca7068fba30021e9b786",
                "sha256:6482d3017a0c0327a49dddc8bd1074cc730d45db2ccb09c3bac1f8f32d1eb61b",
                "sha256:7d3ce02c0784b7cbcc771a2da6ea51f87e8716004512493a2b69016326301c3b",
                "sha256:a14e499c0f5955dcc3991f785f3f8e2130ed504fa3a7f44009ff458ad6bdd17f",
                "sha256:a39f54ccbcd2757d1d63b0ec00a00980c0b382c62865b61a505163943624ab20",
                "sha256:aabb0c5232910a20eec8563503c153a8e78bbf5459490c49ab31f6adf3f3a415",
                "sha256:bd4ecb473a96ad0f90c20acba4f0bf0df91a4e03a1f4dd6a4bdc9ca75aa3a715",
                "sha256:e2da3c13307eac601f3de04887624939aca8ee3c9488a0bb0eca4fb9401fc6b1",
                "sha256:f67814c38162f4deb31f68d590771a29d5ae3b1bd64b75cf232308e5c74777e0"
            ],
            "version": "==1.3.0"
        },
        "pytest": {
            "hashes": [
                "sha256:7e258ee50338f4e46957f9e09a0f10fb1c2d05493fa901d113a8dafd0790de4e",
                "sha256:9332147e9af2dcf46cd7ceb14d5acadb6564744ddff1fe8c17f0ce60ece7d9a2"
            ],
            "version": "==3.8.2"
        },
        "python-dateutil": {
            "hashes": [
                "sha256:1adb80e7a782c12e52ef9a8182bebeb73f1d7e24e374397af06fb4956c8dc5c0",
                "sha256:e27001de32f627c22380a688bcc43ce83504a7bc5da472209b4c70f02829f0b8"
            ],
            "version": "==2.7.3"
        },
        "python-gilt": {
            "hashes": [
                "sha256:4fd58c128635d1f4a8c93305e648f23379ce56e23624e4c5479427fcd2d5656e",
                "sha256:c7321ef1a8efddbdef657b4fd21c3eaf1b4cb24a9656d97b73a444b1feb2067a",
                "sha256:e23a45a6905e6bb7aec3ff7652b48309933a6991fad4546d9e793ac7e0513f8a"
            ],
            "version": "==1.2.1"
        },
        "python-vagrant": {
            "hashes": [
                "sha256:af9a8a9802d382d45dbea96aa3cfbe77c6e6ad65b3fe7b7c799d41ab988179c6"
            ],
            "index": "pypi",
            "version": "==0.5.15"
        },
        "pywinrm": {
            "hashes": [
                "sha256:799fc3e33fec8684443adf5778860388289102ea4fa1458f1bf307d167855573",
                "sha256:ade21b22c72eb3e2e4656798c232ee5f7ce07d157184561eec50691502bc7464"
            ],
            "index": "pypi",
            "version": "==0.3.0"
        },
        "pyyaml": {
            "hashes": [
                "sha256:3d7da3009c0f3e783b2c873687652d83b1bbfd5c88e9813fb7e5b03c0dd3108b",
                "sha256:3ef3092145e9b70e3ddd2c7ad59bdd0252a94dfe3949721633e41344de00a6bf",
                "sha256:40c71b8e076d0550b2e6380bada1f1cd1017b882f7e16f09a65be98e017f211a",
                "sha256:558dd60b890ba8fd982e05941927a3911dc409a63dcb8b634feaa0cda69330d3",
                "sha256:a7c28b45d9f99102fa092bb213aa12e0aaf9a6a1f5e395d36166639c1f96c3a1",
                "sha256:aa7dd4a6a427aed7df6fb7f08a580d68d9b118d90310374716ae90b710280af1",
                "sha256:bc558586e6045763782014934bfaf39d48b8ae85a2713117d16c39864085c613",
                "sha256:d46d7982b62e0729ad0175a9bc7e10a566fc07b224d2c79fafb5e032727eaa04",
                "sha256:d5eef459e30b09f5a098b9cea68bebfeb268697f78d647bd255a085371ac7f3f",
                "sha256:e01d3203230e1786cd91ccfdc8f8454c8069c91bee3962ad93b87a4b2860f537",
                "sha256:e170a9e6fcfd19021dd29845af83bb79236068bf5fd4df3327c1be18182b2531"
            ],
            "version": "==3.13"
        },
        "requests": {
            "hashes": [
                "sha256:63b52e3c866428a224f97cab011de738c36aec0185aa91cfacd418b5d58911d1",
                "sha256:ec22d826a36ed72a7358ff3fe56cbd4ba69dd7a6718ffd450ff0e9df7a47ce6a"
            ],
            "version": "==2.19.1"
        },
        "requests-ntlm": {
            "hashes": [
                "sha256:1eb43d1026b64d431a8e0f1e8a8c8119ac698e72e9b95102018214411a8463ea",
                "sha256:9189c92e8c61ae91402a64b972c4802b2457ce6a799d658256ebf084d5c7eb71"
            ],
            "version": "==1.1.0"
        },
        "scandir": {
            "hashes": [
                "sha256:04b8adb105f2ed313a7c2ef0f1cf7aff4871aa7a1883fa4d8c44b5551ab052d6",
                "sha256:1444134990356c81d12f30e4b311379acfbbcd03e0bab591de2696a3b126d58e",
                "sha256:1b5c314e39f596875e5a95dd81af03730b338c277c54a454226978d5ba95dbb6",
                "sha256:346619f72eb0ddc4cf355ceffd225fa52506c92a2ff05318cfabd02a144e7c4e",
                "sha256:44975e209c4827fc18a3486f257154d34ec6eaec0f90fef0cca1caa482db7064",
                "sha256:61859fd7e40b8c71e609c202db5b0c1dbec0d5c7f1449dec2245575bdc866792",
                "sha256:a5e232a0bf188362fa00123cc0bb842d363a292de7126126df5527b6a369586a",
                "sha256:c14701409f311e7a9b7ec8e337f0815baf7ac95776cc78b419a1e6d49889a383",
                "sha256:c7708f29d843fc2764310732e41f0ce27feadde453261859ec0fca7865dfc41b",
                "sha256:c9009c527929f6e25604aec39b0a43c3f831d2947d89d6caaab22f057b7055c8",
                "sha256:f5c71e29b4e2af7ccdc03a020c626ede51da471173b4a6ad1e904f2b2e04b4bd"
            ],
            "markers": "python_version < '3.5'",
            "version": "==1.9.0"
        },
        "sh": {
            "hashes": [
                "sha256:ae3258c5249493cebe73cb4e18253a41ed69262484bad36fdb3efcb8ad8870bb",
                "sha256:b52bf5833ed01c7b5c5fb73a7f71b3d98d48e9b9b8764236237bdc7ecae850fc"
            ],
            "version": "==1.12.14"
        },
        "six": {
            "hashes": [
                "sha256:70e8a77beed4562e7f14fe23a786b54f6296e34344c23bc42f07b15018ff98e9",
                "sha256:832dc0e10feb1aa2c68dcc57dbb658f1c7e65b9b61af69048abc87a2db00a0eb"
            ],
            "version": "==1.11.0"
        },
        "tabulate": {
            "hashes": [
                "sha256:e4ca13f26d0a6be2a2915428dc21e732f1e44dad7f76d7030b2ef1ec251cf7f2"
            ],
            "version": "==0.8.2"
        },
        "testinfra": {
            "hashes": [
                "sha256:2d0de80ac8de6b527a8192e0eec6ba7aea1d71d8bc26480947063397d78f5364",
                "sha256:9871d55f0e95de79b281575ce1e39ef09d811742d626055cb8a1bfa114296606"
            ],
            "version": "==1.14.1"
        },
        "tree-format": {
            "hashes": [
                "sha256:a538523aa78ae7a4b10003b04f3e1b37708e0e089d99c9d3b9e1c71384c9a7f9",
                "sha256:b5056228dbedde1fb81b79f71fb0c23c98e9d365230df9b29af76e8d8003de11"
            ],
            "version": "==0.1.2"
        },
        "urllib3": {
            "hashes": [
                "sha256:a68ac5e15e76e7e5dd2b8f94007233e01effe3e50e8daddf69acfd81cb686baf",
                "sha256:b5725a0bd4ba422ab0e66e89e030c806576753ea3ee08554382c14e685d117b5"
            ],
            "version": "==1.23"
        },
        "websocket-client": {
            "hashes": [
                "sha256:c42b71b68f9ef151433d6dcc6a7cb98ac72d2ad1e3a74981ca22bc5d9134f166",
                "sha256:f5889b1d0a994258cfcbc8f2dc3e457f6fc7b32a8d74873033d12e4eab4bdf63"
            ],
            "version": "==0.53.0"
        },
        "whichcraft": {
            "hashes": [
                "sha256:7533870f751901a0ce43c93cc9850186e9eba7fe58c924dfb435968ba9c9fa4e",
                "sha256:fecddd531f237ffc5db8b215409afb18fa30300699064cca4817521b4fc81815"
            ],
            "version": "==0.5.2"
        },
        "xmltodict": {
            "hashes": [
                "sha256:8f8d7d40aa28d83f4109a7e8aa86e67a4df202d9538be40c0cb1d70da527b0df",
                "sha256:add07d92089ff611badec526912747cf87afd4f9447af6661aca074eeaf32615"
            ],
            "version": "==0.11.0"
        },
        "yamllint": {
            "hashes": [
                "sha256:93e255e4bd96c7c0850bf182b09f6b35625130f15b37a0e03d8bf378d747081c",
                "sha256:e9b7dec24921ef13180902e5dbcaae9157c773e3e3e2780ef77d3a4dd67d799f"
            ],
            "version": "==1.11.1"
        }
    },
    "develop": {}
}


File: /playbook.yml
---

- hosts: all
  gather_facts: no
  connection: network_cli
  vars:
    ansible_user: admin+cet
    ansible_ssh_pass: ''
    ansible_network_os: routeros
  roles:
    - ansible-role-mikrotik-hostname


File: /README.md
ansible-role-mikrotik-hostname
=========

An Ansible Role that configures hostname on MikroTik routers (https://mikrotik.com).

:point_up: You can use https://github.com/jugatsu/packer-mikrotik to build Vagrant box for testing this role.

Requirements
------------

This role only supports ansible 2.7.

Role Variables
--------------

Hostname of router:

`mikrotik_hostname: "MikroTik"`


Example Playbook
----------------
```yaml
- hosts: routers
  roles:
    - { role: ansible-role-mikrotik-hostname }
```

How to test role
----------------

Install pipenv (https://github.com/pypa/pipenv) and use this commands:

```bash
pipenv install
pipenv shell
vagrant up --provision
```

License
-------

BSD


File: /tasks\main.yml
---
# tasks file for ansible-role-mikrotik-hostname

- name: Get hostname.
  routeros_command:
    commands: :put [/system identity get value-name=name]
  register: hostname_result

- name: Ensure hostname is configured.
  routeros_command:
    commands:
      - /system identity set name={{ mikrotik_hostname }}
    wait_for:
      - result[0] contains ''
  when: mikrotik_hostname not in hostname_result.stdout_lines[0]
  changed_when: True


File: /Vagrantfile
Vagrant.configure("2") do |config|
  config.vm.box = "mikrotik-routeros-6.38.5"
  config.vm.provision "ansible" do |ansible|
    ansible.compatibility_mode = '2.0'
    ansible.playbook = "playbook.yml"
    ansible.extra_vars = {
      mikrotik_hostname: "router",
    }
  end
end


