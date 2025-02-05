# Repository Information
Name: ansible-ovpn-mikrotik

# Directory Structure
Directory structure:
└── github_repos/ansible-ovpn-mikrotik/
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
    │   │       ├── pack-1377c32a7bcf69974d66a8b3e5caaff51fb7193f.idx
    │   │       └── pack-1377c32a7bcf69974d66a8b3e5caaff51fb7193f.pack
    │   ├── packed-refs
    │   └── refs/
    │       ├── heads/
    │       │   └── master
    │       ├── remotes/
    │       │   └── origin/
    │       │       └── HEAD
    │       └── tags/
    ├── .gitignore
    ├── .travis.yml
    ├── ansible.cfg
    ├── inventories/
    │   └── sample/
    │       ├── group_vars/
    │       │   └── all.yml
    │       └── hosts.ini
    ├── LICENSE
    ├── playbooks/
    │   ├── add_clients.yml
    │   ├── install.yml
    │   ├── revoke_clients.yml
    │   ├── roles/
    │   │   ├── add_clients/
    │   │   │   ├── tasks/
    │   │   │   │   ├── add_gen_key.yml
    │   │   │   │   └── main.yml
    │   │   │   └── templates/
    │   │   │       ├── client_ccd.j2
    │   │   │       ├── client_common.ovpn.j2
    │   │   │       ├── client_pkcs12.ovpn.j2
    │   │   │       ├── client_pki_embedded.ovpn.j2
    │   │   │       └── client_pki_files.ovpn.j2
    │   │   ├── openvpn/
    │   │   │   ├── defaults/
    │   │   │   │   └── main.yml
    │   │   │   ├── handlers/
    │   │   │   │   └── main.yml
    │   │   │   ├── tasks/
    │   │   │   │   ├── firewall.yml
    │   │   │   │   ├── main.yml
    │   │   │   │   ├── openvpn.yml
    │   │   │   │   ├── packages.yml
    │   │   │   │   └── pki.yml
    │   │   │   ├── templates/
    │   │   │   │   ├── etc_iptables_rules.v4.j2
    │   │   │   │   ├── etc_openvpn_easyrsa_easyrsa3_vars.j2
    │   │   │   │   ├── etc_openvpn_server.conf.j2
    │   │   │   │   └── group_vars_all.yml.j2
    │   │   │   └── vars/
    │   │   │       ├── Debian.yml
    │   │   │       └── RedHat.yml
    │   │   ├── revoke_clients/
    │   │   │   └── tasks/
    │   │   │       └── main.yml
    │   │   └── sync_clients/
    │   │       └── tasks/
    │   │           └── main.yml
    │   └── sync_clients.yml
    ├── README.md
    ├── test/
    │   ├── ansible-vars/
    │   │   ├── 01_install_centos.yml
    │   │   ├── 01_install_debian.yml
    │   │   ├── 01_install_ubuntu.yml
    │   │   ├── 02_add_clients.yml
    │   │   ├── 03_revoke_clients.yml
    │   │   └── 04_sync_clients.yml
    │   ├── docker-inventory
    │   ├── docker-setup.sh
    │   ├── Dockerfile.centos-7
    │   ├── Dockerfile.debian-8.7
    │   └── Dockerfile.ubuntu-16.04
    └── TODO.md


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
	url = https://github.com/dteslya/ansible-ovpn-mikrotik.git
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
0000000000000000000000000000000000000000 8f8d9d9d8ae43a677131b9fa3318ed8474c1c1f7 vivek-dodia <vivek.dodia@icloud.com> 1738605988 -0500	clone: from https://github.com/dteslya/ansible-ovpn-mikrotik.git


File: /.git\logs\refs\heads\master
0000000000000000000000000000000000000000 8f8d9d9d8ae43a677131b9fa3318ed8474c1c1f7 vivek-dodia <vivek.dodia@icloud.com> 1738605988 -0500	clone: from https://github.com/dteslya/ansible-ovpn-mikrotik.git


File: /.git\logs\refs\remotes\origin\HEAD
0000000000000000000000000000000000000000 8f8d9d9d8ae43a677131b9fa3318ed8474c1c1f7 vivek-dodia <vivek.dodia@icloud.com> 1738605988 -0500	clone: from https://github.com/dteslya/ansible-ovpn-mikrotik.git


File: /.git\packed-refs
# pack-refs with: peeled fully-peeled sorted 
8f8d9d9d8ae43a677131b9fa3318ed8474c1c1f7 refs/remotes/origin/master


File: /.git\refs\heads\master
8f8d9d9d8ae43a677131b9fa3318ed8474c1c1f7


File: /.git\refs\remotes\origin\HEAD
ref: refs/remotes/origin/master


File: /.gitignore
fetched_creds
*.retry
/inventories
test/host_vars
test/group_vars
test/docker-inventory
File: /.travis.yml
---
language: python

cache: pip

sudo: required

env:
  global:
    - ANSIBLE_HOST_KEY_CHECKING=false
  matrix:
#    - distribution: centos
#      version: 7
#      init: /usr/lib/systemd/systemd
#      run_opts: "'--detach --privileged --volume=/sys/fs/cgroup:/sys/fs/cgroup'"
#      ssh: sshd
#      docker_concurrent_containers: 1
    - distribution: ubuntu
      version: 16.04
      init: /sbin/init
      run_opts: "'--detach --privileged --volume=/sys/fs/cgroup:/sys/fs/cgroup'"
      ssh: ssh
      docker_concurrent_containers: 1
#    - distribution: debian
#      version: 8.7
#      init: /bin/systemd
#      run_opts: "'--detach --privileged --volume=/sys/fs/cgroup:/sys/fs/cgroup'"
#      ssh: ssh
#      docker_concurrent_containers: 1
#    - distribution: ubuntu
#      version: 16.04
#      init: /sbin/init
#      run_opts: "'--detach --privileged --volume=/sys/fs/cgroup:/sys/fs/cgroup'"
#      ssh: ssh
#      docker_concurrent_containers: 2

services:
  - docker

before_install:
  # Pull container
  - sudo docker pull ${distribution}:${version}
  - ssh-keygen -t rsa -f /home/travis/.ssh/id_rsa -q -N ""
  - cp /home/travis/.ssh/id_rsa.pub test/id_rsa.pub
  # Build container
  - sudo docker build --rm=true --file=test/Dockerfile.${distribution}-${version} --tag=${distribution}-${version}:ansible .

install:
  - sudo -H pip install ansible ansible-lint
  - sudo apt-get -y install openssl

script:
  # Ansible syntax check.
  - ansible-lint -x 306 playbooks/install.yml
  - ansible-lint -x 306 playbooks/sync_clients.yml
  - ansible-lint -x 306 playbooks/add_clients.yml
  - ansible-lint -x 306 playbooks/revoke_clients.yml

  - sudo test/docker-setup.sh

  # Create ansible vars directories
  - mkdir test/host_vars test/group_vars

  # Copy default all.yml in group_vars
  - cp inventories/sample/group_vars/all.yml test/group_vars/all.yml

  # Test role
  - ansible-playbook -i test/docker-inventory -e "@test/ansible-vars/01_install_${distribution}.yml" --diff playbooks/install.yml

  # Test role idempotence
  - >
    ansible-playbook -i test/docker-inventory -e "@test/ansible-vars/01_install_${distribution}.yml" playbooks/install.yml
    | grep -q 'changed=0.*failed=0'
    && (echo 'Idempotence test: pass' && exit 0)
    || (echo 'Idempotence test: fail' && exit 1)

  # Check if ca_password(s) got written to host_vars
  - if [ $(ls -l test/host_vars/*.yml | wc -l) -ne $docker_concurrent_containers ];then echo "Not all ca passwords written to host_vars" && exit 1;fi

  # Test adding clients
  - ansible-playbook -i test/docker-inventory -e "@test/ansible-vars/02_add_clients.yml" playbooks/add_clients.yml

  # Test revoking a client
  - ansible-playbook -i test/docker-inventory -e "@test/ansible-vars/03_revoke_clients.yml" playbooks/revoke_clients.yml

  # Test syncing clients
  - ansible-playbook -i test/docker-inventory -e "@test/ansible-vars/04_sync_clients.yml" playbooks/sync_clients.yml

  # Test adding a client using a CSR
  #- openssl genrsa -out ~/test.key 2048
  #- openssl req -new -sha256 -key ~/test.key -out ~/test.csr -batch -subj "/CN=test@domain.com"
  #- ansible-playbook -i test/docker-inventory -e "csr_path=~/test.csr cn=test@domain.com" playbooks/add_clients.yml


File: /ansible.cfg
[defaults]
# Workaround for https://github.com/ansible/ansible/issues/13401
scp_if_ssh=True

[ssh_connection]
pipelining = True


File: /inventories\sample\group_vars\all.yml
# By default the DN is randomly generated and organizational mode is used.
openvpn_key_country:  "US"
openvpn_key_province: "California"
openvpn_key_city: "Beverly Hills"
openvpn_key_org: "ACME CORPORATION"
openvpn_key_ou: "Anvil Department"
openvpn_key_email: "user@example.com"

# Set this to true to use cn_only DN mode instead.
# Consider uncommenting and setting openvpn_server_common_name_manual as well then.
easyrsa_dn_mode_cn_only: false
# openvpn_server_common_name_manual: "Company FooBar Ltd."

# `proto` and `port` where OpenVPN will listen at.
# `mask` and `cidr` refer to the subnets used for tunneling.
# `server_extra_options` defines config options added to the OpenVPN server config,
#  e.g. `push ...` or `client-to-client`.
# `client_extra_options` defines config options added to the OpenVPN client config.
openvpn_instances:
  - {
      proto: udp,
      port: 1194,
      mask: "192.168.69.0 255.255.255.0",
      cidr: "192.168.69.0/24",
      server_extra_options: ['push "route 172.16.0.0 255.240.0.0"'],
      client_extra_options: [],
  }
  # Uncomment below to listen on TCP 443. This will look like normal SSL/TLS traffic
  # and will be more likely to get through restrictive firewalls.
  - {
      proto: tcp,
      port: 443,
      mask: "192.168.70.0 255.255.255.0",
      cidr: "192.168.70.0/24",
      server_extra_options: ['route 172.16.0.0 255.240.0.0', 'push "route 172.16.0.0 255.240.0.0"'],
      client_extra_options: [],
 }

# Whether sync_clients.yml playbook wil show a prompt displaying which clients to add 
# and revoke before actually doing it and will only continue execution after confirmation input
# Set this to false to disable this prompt.
prompt_before_syncing_clients: true

# maintain a list of your valid_clients here, used by the `sync_clients.yml` playbook
valid_clients:
  - name: mikrotik
    ccd: ['iroute 172.16.0.0 255.240.0.0']
  - name: user1

# Whether the install.yml playbook will load iptables rules.
# If set to false you have to apply them yourself. See README section "Firewall".
load_iptables_rules: true
iptables_path: "/sbin/iptables"
openvpn_path_iptables_rules: "{{ openvpn_path }}/openvpn_iptables_rules.sh"

# path where fetched credentials are stored
local_creds_folder: "{{ playbook_dir }}/../fetched_creds/{{ openvpn_server_remote_host }}"

# This variable will be used as the `remote` directive in the OpenVPN configuration.
# So make sure this is resolvable by the clients.
# If this is not the case with `inventory_hostname`, one could use `ansible_default_ipv4.address`.
openvpn_server_remote_host: "{{ inventory_hostname }}"

openvpn_path: "/etc/openvpn"
openvpn_path_ccd: "{{ openvpn_path }}/ccd"
openvpn_path_pki: "{{ openvpn_path }}/pki"
openvpn_path_keys: "{{ openvpn_path_pki }}/private"
openvpn_path_certs: "{{ openvpn_path_pki }}/issued"
openvpn_path_reqs: "{{ openvpn_path_pki }}/reqs"
openvpn_hmac_firewall: "{{ openvpn_path_pki }}/ta.key"
openvpn_ca_cert: "{{ openvpn_path_pki }}/ca.crt"
openvpn_path_easyrsa: "{{ openvpn_path }}/easyrsa/easyrsa3"
dhparams_size: "{{ openvpn_key_size }}"
dhparams_location: "{{ openvpn_path_pki }}/dh.pem"
openvpn_crl: "{{ openvpn_path_pki }}/crl.pem"
openvpn_server_common_name_file: "{{ openvpn_path }}/openvpn_server_common_name"

openvpn_key_size: "2048"
# Changed for mikrotik compatibility
openvpn_cipher: "AES-128-CBC"
openvpn_auth_digest: "SHA1"
#openvpn_cipher: "AES-256-CBC"
#openvpn_auth_digest: "SHA256"
# For all available ciphers use: openvpn --show-tls
# For all available PFS ciphers (without eliptic curve cryptography) use: openvpn --show-tls | grep -e "-DHE-"
# Configuration here just uses PFS ciphers leveraging AES256 and at least SHA256
openvpn_tls_cipher: "TLS-DHE-DSS-WITH-AES-256-GCM-SHA384:TLS-DHE-RSA-WITH-AES-256-GCM-SHA384:TLS-DHE-RSA-WITH-AES-256-CBC-SHA256:TLS-DHE-DSS-WITH-AES-256-CBC-SHA256"

openvpn_easyrsa_version: v3.0.6

File: /inventories\sample\hosts.ini
[localhost]
127.0.0.1 ansible_python_interpreter=python

[openvpn]
# Enter your hosts here.
# Typical Digital Ocean config w/ root user and pub/priv key authentication
#255.255.255.255 ansible_user=root
# Typical azure config w/ ssh authentication
#255.255.255.255 ansible_user=vpnuser ansible_become=yes
# Config for a machine with pub/priv key and password
#255.255.255.255 ansible_user=vpnuser ansible_become=yes ansible_become_pass=password


File: /LICENSE
                    GNU GENERAL PUBLIC LICENSE
                       Version 3, 29 June 2007

 Copyright (C) 2007 Free Software Foundation, Inc. <http://fsf.org/>
 Everyone is permitted to copy and distribute verbatim copies
 of this license document, but changing it is not allowed.

                            Preamble

  The GNU General Public License is a free, copyleft license for
software and other kinds of works.

  The licenses for most software and other practical works are designed
to take away your freedom to share and change the works.  By contrast,
the GNU General Public License is intended to guarantee your freedom to
share and change all versions of a program--to make sure it remains free
software for all its users.  We, the Free Software Foundation, use the
GNU General Public License for most of our software; it applies also to
any other work released this way by its authors.  You can apply it to
your programs, too.

  When we speak of free software, we are referring to freedom, not
price.  Our General Public Licenses are designed to make sure that you
have the freedom to distribute copies of free software (and charge for
them if you wish), that you receive source code or can get it if you
want it, that you can change the software or use pieces of it in new
free programs, and that you know you can do these things.

  To protect your rights, we need to prevent others from denying you
these rights or asking you to surrender the rights.  Therefore, you have
certain responsibilities if you distribute copies of the software, or if
you modify it: responsibilities to respect the freedom of others.

  For example, if you distribute copies of such a program, whether
gratis or for a fee, you must pass on to the recipients the same
freedoms that you received.  You must make sure that they, too, receive
or can get the source code.  And you must show them these terms so they
know their rights.

  Developers that use the GNU GPL protect your rights with two steps:
(1) assert copyright on the software, and (2) offer you this License
giving you legal permission to copy, distribute and/or modify it.

  For the developers' and authors' protection, the GPL clearly explains
that there is no warranty for this free software.  For both users' and
authors' sake, the GPL requires that modified versions be marked as
changed, so that their problems will not be attributed erroneously to
authors of previous versions.

  Some devices are designed to deny users access to install or run
modified versions of the software inside them, although the manufacturer
can do so.  This is fundamentally incompatible with the aim of
protecting users' freedom to change the software.  The systematic
pattern of such abuse occurs in the area of products for individuals to
use, which is precisely where it is most unacceptable.  Therefore, we
have designed this version of the GPL to prohibit the practice for those
products.  If such problems arise substantially in other domains, we
stand ready to extend this provision to those domains in future versions
of the GPL, as needed to protect the freedom of users.

  Finally, every program is threatened constantly by software patents.
States should not allow patents to restrict development and use of
software on general-purpose computers, but in those that do, we wish to
avoid the special danger that patents applied to a free program could
make it effectively proprietary.  To prevent this, the GPL assures that
patents cannot be used to render the program non-free.

  The precise terms and conditions for copying, distribution and
modification follow.

                       TERMS AND CONDITIONS

  0. Definitions.

  "This License" refers to version 3 of the GNU General Public License.

  "Copyright" also means copyright-like laws that apply to other kinds of
works, such as semiconductor masks.

  "The Program" refers to any copyrightable work licensed under this
License.  Each licensee is addressed as "you".  "Licensees" and
"recipients" may be individuals or organizations.

  To "modify" a work means to copy from or adapt all or part of the work
in a fashion requiring copyright permission, other than the making of an
exact copy.  The resulting work is called a "modified version" of the
earlier work or a work "based on" the earlier work.

  A "covered work" means either the unmodified Program or a work based
on the Program.

  To "propagate" a work means to do anything with it that, without
permission, would make you directly or secondarily liable for
infringement under applicable copyright law, except executing it on a
computer or modifying a private copy.  Propagation includes copying,
distribution (with or without modification), making available to the
public, and in some countries other activities as well.

  To "convey" a work means any kind of propagation that enables other
parties to make or receive copies.  Mere interaction with a user through
a computer network, with no transfer of a copy, is not conveying.

  An interactive user interface displays "Appropriate Legal Notices"
to the extent that it includes a convenient and prominently visible
feature that (1) displays an appropriate copyright notice, and (2)
tells the user that there is no warranty for the work (except to the
extent that warranties are provided), that licensees may convey the
work under this License, and how to view a copy of this License.  If
the interface presents a list of user commands or options, such as a
menu, a prominent item in the list meets this criterion.

  1. Source Code.

  The "source code" for a work means the preferred form of the work
for making modifications to it.  "Object code" means any non-source
form of a work.

  A "Standard Interface" means an interface that either is an official
standard defined by a recognized standards body, or, in the case of
interfaces specified for a particular programming language, one that
is widely used among developers working in that language.

  The "System Libraries" of an executable work include anything, other
than the work as a whole, that (a) is included in the normal form of
packaging a Major Component, but which is not part of that Major
Component, and (b) serves only to enable use of the work with that
Major Component, or to implement a Standard Interface for which an
implementation is available to the public in source code form.  A
"Major Component", in this context, means a major essential component
(kernel, window system, and so on) of the specific operating system
(if any) on which the executable work runs, or a compiler used to
produce the work, or an object code interpreter used to run it.

  The "Corresponding Source" for a work in object code form means all
the source code needed to generate, install, and (for an executable
work) run the object code and to modify the work, including scripts to
control those activities.  However, it does not include the work's
System Libraries, or general-purpose tools or generally available free
programs which are used unmodified in performing those activities but
which are not part of the work.  For example, Corresponding Source
includes interface definition files associated with source files for
the work, and the source code for shared libraries and dynamically
linked subprograms that the work is specifically designed to require,
such as by intimate data communication or control flow between those
subprograms and other parts of the work.

  The Corresponding Source need not include anything that users
can regenerate automatically from other parts of the Corresponding
Source.

  The Corresponding Source for a work in source code form is that
same work.

  2. Basic Permissions.

  All rights granted under this License are granted for the term of
copyright on the Program, and are irrevocable provided the stated
conditions are met.  This License explicitly affirms your unlimited
permission to run the unmodified Program.  The output from running a
covered work is covered by this License only if the output, given its
content, constitutes a covered work.  This License acknowledges your
rights of fair use or other equivalent, as provided by copyright law.

  You may make, run and propagate covered works that you do not
convey, without conditions so long as your license otherwise remains
in force.  You may convey covered works to others for the sole purpose
of having them make modifications exclusively for you, or provide you
with facilities for running those works, provided that you comply with
the terms of this License in conveying all material for which you do
not control copyright.  Those thus making or running the covered works
for you must do so exclusively on your behalf, under your direction
and control, on terms that prohibit them from making any copies of
your copyrighted material outside their relationship with you.

  Conveying under any other circumstances is permitted solely under
the conditions stated below.  Sublicensing is not allowed; section 10
makes it unnecessary.

  3. Protecting Users' Legal Rights From Anti-Circumvention Law.

  No covered work shall be deemed part of an effective technological
measure under any applicable law fulfilling obligations under article
11 of the WIPO copyright treaty adopted on 20 December 1996, or
similar laws prohibiting or restricting circumvention of such
measures.

  When you convey a covered work, you waive any legal power to forbid
circumvention of technological measures to the extent such circumvention
is effected by exercising rights under this License with respect to
the covered work, and you disclaim any intention to limit operation or
modification of the work as a means of enforcing, against the work's
users, your or third parties' legal rights to forbid circumvention of
technological measures.

  4. Conveying Verbatim Copies.

  You may convey verbatim copies of the Program's source code as you
receive it, in any medium, provided that you conspicuously and
appropriately publish on each copy an appropriate copyright notice;
keep intact all notices stating that this License and any
non-permissive terms added in accord with section 7 apply to the code;
keep intact all notices of the absence of any warranty; and give all
recipients a copy of this License along with the Program.

  You may charge any price or no price for each copy that you convey,
and you may offer support or warranty protection for a fee.

  5. Conveying Modified Source Versions.

  You may convey a work based on the Program, or the modifications to
produce it from the Program, in the form of source code under the
terms of section 4, provided that you also meet all of these conditions:

    a) The work must carry prominent notices stating that you modified
    it, and giving a relevant date.

    b) The work must carry prominent notices stating that it is
    released under this License and any conditions added under section
    7.  This requirement modifies the requirement in section 4 to
    "keep intact all notices".

    c) You must license the entire work, as a whole, under this
    License to anyone who comes into possession of a copy.  This
    License will therefore apply, along with any applicable section 7
    additional terms, to the whole of the work, and all its parts,
    regardless of how they are packaged.  This License gives no
    permission to license the work in any other way, but it does not
    invalidate such permission if you have separately received it.

    d) If the work has interactive user interfaces, each must display
    Appropriate Legal Notices; however, if the Program has interactive
    interfaces that do not display Appropriate Legal Notices, your
    work need not make them do so.

  A compilation of a covered work with other separate and independent
works, which are not by their nature extensions of the covered work,
and which are not combined with it such as to form a larger program,
in or on a volume of a storage or distribution medium, is called an
"aggregate" if the compilation and its resulting copyright are not
used to limit the access or legal rights of the compilation's users
beyond what the individual works permit.  Inclusion of a covered work
in an aggregate does not cause this License to apply to the other
parts of the aggregate.

  6. Conveying Non-Source Forms.

  You may convey a covered work in object code form under the terms
of sections 4 and 5, provided that you also convey the
machine-readable Corresponding Source under the terms of this License,
in one of these ways:

    a) Convey the object code in, or embodied in, a physical product
    (including a physical distribution medium), accompanied by the
    Corresponding Source fixed on a durable physical medium
    customarily used for software interchange.

    b) Convey the object code in, or embodied in, a physical product
    (including a physical distribution medium), accompanied by a
    written offer, valid for at least three years and valid for as
    long as you offer spare parts or customer support for that product
    model, to give anyone who possesses the object code either (1) a
    copy of the Corresponding Source for all the software in the
    product that is covered by this License, on a durable physical
    medium customarily used for software interchange, for a price no
    more than your reasonable cost of physically performing this
    conveying of source, or (2) access to copy the
    Corresponding Source from a network server at no charge.

    c) Convey individual copies of the object code with a copy of the
    written offer to provide the Corresponding Source.  This
    alternative is allowed only occasionally and noncommercially, and
    only if you received the object code with such an offer, in accord
    with subsection 6b.

    d) Convey the object code by offering access from a designated
    place (gratis or for a charge), and offer equivalent access to the
    Corresponding Source in the same way through the same place at no
    further charge.  You need not require recipients to copy the
    Corresponding Source along with the object code.  If the place to
    copy the object code is a network server, the Corresponding Source
    may be on a different server (operated by you or a third party)
    that supports equivalent copying facilities, provided you maintain
    clear directions next to the object code saying where to find the
    Corresponding Source.  Regardless of what server hosts the
    Corresponding Source, you remain obligated to ensure that it is
    available for as long as needed to satisfy these requirements.

    e) Convey the object code using peer-to-peer transmission, provided
    you inform other peers where the object code and Corresponding
    Source of the work are being offered to the general public at no
    charge under subsection 6d.

  A separable portion of the object code, whose source code is excluded
from the Corresponding Source as a System Library, need not be
included in conveying the object code work.

  A "User Product" is either (1) a "consumer product", which means any
tangible personal property which is normally used for personal, family,
or household purposes, or (2) anything designed or sold for incorporation
into a dwelling.  In determining whether a product is a consumer product,
doubtful cases shall be resolved in favor of coverage.  For a particular
product received by a particular user, "normally used" refers to a
typical or common use of that class of product, regardless of the status
of the particular user or of the way in which the particular user
actually uses, or expects or is expected to use, the product.  A product
is a consumer product regardless of whether the product has substantial
commercial, industrial or non-consumer uses, unless such uses represent
the only significant mode of use of the product.

  "Installation Information" for a User Product means any methods,
procedures, authorization keys, or other information required to install
and execute modified versions of a covered work in that User Product from
a modified version of its Corresponding Source.  The information must
suffice to ensure that the continued functioning of the modified object
code is in no case prevented or interfered with solely because
modification has been made.

  If you convey an object code work under this section in, or with, or
specifically for use in, a User Product, and the conveying occurs as
part of a transaction in which the right of possession and use of the
User Product is transferred to the recipient in perpetuity or for a
fixed term (regardless of how the transaction is characterized), the
Corresponding Source conveyed under this section must be accompanied
by the Installation Information.  But this requirement does not apply
if neither you nor any third party retains the ability to install
modified object code on the User Product (for example, the work has
been installed in ROM).

  The requirement to provide Installation Information does not include a
requirement to continue to provide support service, warranty, or updates
for a work that has been modified or installed by the recipient, or for
the User Product in which it has been modified or installed.  Access to a
network may be denied when the modification itself materially and
adversely affects the operation of the network or violates the rules and
protocols for communication across the network.

  Corresponding Source conveyed, and Installation Information provided,
in accord with this section must be in a format that is publicly
documented (and with an implementation available to the public in
source code form), and must require no special password or key for
unpacking, reading or copying.

  7. Additional Terms.

  "Additional permissions" are terms that supplement the terms of this
License by making exceptions from one or more of its conditions.
Additional permissions that are applicable to the entire Program shall
be treated as though they were included in this License, to the extent
that they are valid under applicable law.  If additional permissions
apply only to part of the Program, that part may be used separately
under those permissions, but the entire Program remains governed by
this License without regard to the additional permissions.

  When you convey a copy of a covered work, you may at your option
remove any additional permissions from that copy, or from any part of
it.  (Additional permissions may be written to require their own
removal in certain cases when you modify the work.)  You may place
additional permissions on material, added by you to a covered work,
for which you have or can give appropriate copyright permission.

  Notwithstanding any other provision of this License, for material you
add to a covered work, you may (if authorized by the copyright holders of
that material) supplement the terms of this License with terms:

    a) Disclaiming warranty or limiting liability differently from the
    terms of sections 15 and 16 of this License; or

    b) Requiring preservation of specified reasonable legal notices or
    author attributions in that material or in the Appropriate Legal
    Notices displayed by works containing it; or

    c) Prohibiting misrepresentation of the origin of that material, or
    requiring that modified versions of such material be marked in
    reasonable ways as different from the original version; or

    d) Limiting the use for publicity purposes of names of licensors or
    authors of the material; or

    e) Declining to grant rights under trademark law for use of some
    trade names, trademarks, or service marks; or

    f) Requiring indemnification of licensors and authors of that
    material by anyone who conveys the material (or modified versions of
    it) with contractual assumptions of liability to the recipient, for
    any liability that these contractual assumptions directly impose on
    those licensors and authors.

  All other non-permissive additional terms are considered "further
restrictions" within the meaning of section 10.  If the Program as you
received it, or any part of it, contains a notice stating that it is
governed by this License along with a term that is a further
restriction, you may remove that term.  If a license document contains
a further restriction but permits relicensing or conveying under this
License, you may add to a covered work material governed by the terms
of that license document, provided that the further restriction does
not survive such relicensing or conveying.

  If you add terms to a covered work in accord with this section, you
must place, in the relevant source files, a statement of the
additional terms that apply to those files, or a notice indicating
where to find the applicable terms.

  Additional terms, permissive or non-permissive, may be stated in the
form of a separately written license, or stated as exceptions;
the above requirements apply either way.

  8. Termination.

  You may not propagate or modify a covered work except as expressly
provided under this License.  Any attempt otherwise to propagate or
modify it is void, and will automatically terminate your rights under
this License (including any patent licenses granted under the third
paragraph of section 11).

  However, if you cease all violation of this License, then your
license from a particular copyright holder is reinstated (a)
provisionally, unless and until the copyright holder explicitly and
finally terminates your license, and (b) permanently, if the copyright
holder fails to notify you of the violation by some reasonable means
prior to 60 days after the cessation.

  Moreover, your license from a particular copyright holder is
reinstated permanently if the copyright holder notifies you of the
violation by some reasonable means, this is the first time you have
received notice of violation of this License (for any work) from that
copyright holder, and you cure the violation prior to 30 days after
your receipt of the notice.

  Termination of your rights under this section does not terminate the
licenses of parties who have received copies or rights from you under
this License.  If your rights have been terminated and not permanently
reinstated, you do not qualify to receive new licenses for the same
material under section 10.

  9. Acceptance Not Required for Having Copies.

  You are not required to accept this License in order to receive or
run a copy of the Program.  Ancillary propagation of a covered work
occurring solely as a consequence of using peer-to-peer transmission
to receive a copy likewise does not require acceptance.  However,
nothing other than this License grants you permission to propagate or
modify any covered work.  These actions infringe copyright if you do
not accept this License.  Therefore, by modifying or propagating a
covered work, you indicate your acceptance of this License to do so.

  10. Automatic Licensing of Downstream Recipients.

  Each time you convey a covered work, the recipient automatically
receives a license from the original licensors, to run, modify and
propagate that work, subject to this License.  You are not responsible
for enforcing compliance by third parties with this License.

  An "entity transaction" is a transaction transferring control of an
organization, or substantially all assets of one, or subdividing an
organization, or merging organizations.  If propagation of a covered
work results from an entity transaction, each party to that
transaction who receives a copy of the work also receives whatever
licenses to the work the party's predecessor in interest had or could
give under the previous paragraph, plus a right to possession of the
Corresponding Source of the work from the predecessor in interest, if
the predecessor has it or can get it with reasonable efforts.

  You may not impose any further restrictions on the exercise of the
rights granted or affirmed under this License.  For example, you may
not impose a license fee, royalty, or other charge for exercise of
rights granted under this License, and you may not initiate litigation
(including a cross-claim or counterclaim in a lawsuit) alleging that
any patent claim is infringed by making, using, selling, offering for
sale, or importing the Program or any portion of it.

  11. Patents.

  A "contributor" is a copyright holder who authorizes use under this
License of the Program or a work on which the Program is based.  The
work thus licensed is called the contributor's "contributor version".

  A contributor's "essential patent claims" are all patent claims
owned or controlled by the contributor, whether already acquired or
hereafter acquired, that would be infringed by some manner, permitted
by this License, of making, using, or selling its contributor version,
but do not include claims that would be infringed only as a
consequence of further modification of the contributor version.  For
purposes of this definition, "control" includes the right to grant
patent sublicenses in a manner consistent with the requirements of
this License.

  Each contributor grants you a non-exclusive, worldwide, royalty-free
patent license under the contributor's essential patent claims, to
make, use, sell, offer for sale, import and otherwise run, modify and
propagate the contents of its contributor version.

  In the following three paragraphs, a "patent license" is any express
agreement or commitment, however denominated, not to enforce a patent
(such as an express permission to practice a patent or covenant not to
sue for patent infringement).  To "grant" such a patent license to a
party means to make such an agreement or commitment not to enforce a
patent against the party.

  If you convey a covered work, knowingly relying on a patent license,
and the Corresponding Source of the work is not available for anyone
to copy, free of charge and under the terms of this License, through a
publicly available network server or other readily accessible means,
then you must either (1) cause the Corresponding Source to be so
available, or (2) arrange to deprive yourself of the benefit of the
patent license for this particular work, or (3) arrange, in a manner
consistent with the requirements of this License, to extend the patent
license to downstream recipients.  "Knowingly relying" means you have
actual knowledge that, but for the patent license, your conveying the
covered work in a country, or your recipient's use of the covered work
in a country, would infringe one or more identifiable patents in that
country that you have reason to believe are valid.

  If, pursuant to or in connection with a single transaction or
arrangement, you convey, or propagate by procuring conveyance of, a
covered work, and grant a patent license to some of the parties
receiving the covered work authorizing them to use, propagate, modify
or convey a specific copy of the covered work, then the patent license
you grant is automatically extended to all recipients of the covered
work and works based on it.

  A patent license is "discriminatory" if it does not include within
the scope of its coverage, prohibits the exercise of, or is
conditioned on the non-exercise of one or more of the rights that are
specifically granted under this License.  You may not convey a covered
work if you are a party to an arrangement with a third party that is
in the business of distributing software, under which you make payment
to the third party based on the extent of your activity of conveying
the work, and under which the third party grants, to any of the
parties who would receive the covered work from you, a discriminatory
patent license (a) in connection with copies of the covered work
conveyed by you (or copies made from those copies), or (b) primarily
for and in connection with specific products or compilations that
contain the covered work, unless you entered into that arrangement,
or that patent license was granted, prior to 28 March 2007.

  Nothing in this License shall be construed as excluding or limiting
any implied license or other defenses to infringement that may
otherwise be available to you under applicable patent law.

  12. No Surrender of Others' Freedom.

  If conditions are imposed on you (whether by court order, agreement or
otherwise) that contradict the conditions of this License, they do not
excuse you from the conditions of this License.  If you cannot convey a
covered work so as to satisfy simultaneously your obligations under this
License and any other pertinent obligations, then as a consequence you may
not convey it at all.  For example, if you agree to terms that obligate you
to collect a royalty for further conveying from those to whom you convey
the Program, the only way you could satisfy both those terms and this
License would be to refrain entirely from conveying the Program.

  13. Use with the GNU Affero General Public License.

  Notwithstanding any other provision of this License, you have
permission to link or combine any covered work with a work licensed
under version 3 of the GNU Affero General Public License into a single
combined work, and to convey the resulting work.  The terms of this
License will continue to apply to the part which is the covered work,
but the special requirements of the GNU Affero General Public License,
section 13, concerning interaction through a network will apply to the
combination as such.

  14. Revised Versions of this License.

  The Free Software Foundation may publish revised and/or new versions of
the GNU General Public License from time to time.  Such new versions will
be similar in spirit to the present version, but may differ in detail to
address new problems or concerns.

  Each version is given a distinguishing version number.  If the
Program specifies that a certain numbered version of the GNU General
Public License "or any later version" applies to it, you have the
option of following the terms and conditions either of that numbered
version or of any later version published by the Free Software
Foundation.  If the Program does not specify a version number of the
GNU General Public License, you may choose any version ever published
by the Free Software Foundation.

  If the Program specifies that a proxy can decide which future
versions of the GNU General Public License can be used, that proxy's
public statement of acceptance of a version permanently authorizes you
to choose that version for the Program.

  Later license versions may give you additional or different
permissions.  However, no additional obligations are imposed on any
author or copyright holder as a result of your choosing to follow a
later version.

  15. Disclaimer of Warranty.

  THERE IS NO WARRANTY FOR THE PROGRAM, TO THE EXTENT PERMITTED BY
APPLICABLE LAW.  EXCEPT WHEN OTHERWISE STATED IN WRITING THE COPYRIGHT
HOLDERS AND/OR OTHER PARTIES PROVIDE THE PROGRAM "AS IS" WITHOUT WARRANTY
OF ANY KIND, EITHER EXPRESSED OR IMPLIED, INCLUDING, BUT NOT LIMITED TO,
THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR
PURPOSE.  THE ENTIRE RISK AS TO THE QUALITY AND PERFORMANCE OF THE PROGRAM
IS WITH YOU.  SHOULD THE PROGRAM PROVE DEFECTIVE, YOU ASSUME THE COST OF
ALL NECESSARY SERVICING, REPAIR OR CORRECTION.

  16. Limitation of Liability.

  IN NO EVENT UNLESS REQUIRED BY APPLICABLE LAW OR AGREED TO IN WRITING
WILL ANY COPYRIGHT HOLDER, OR ANY OTHER PARTY WHO MODIFIES AND/OR CONVEYS
THE PROGRAM AS PERMITTED ABOVE, BE LIABLE TO YOU FOR DAMAGES, INCLUDING ANY
GENERAL, SPECIAL, INCIDENTAL OR CONSEQUENTIAL DAMAGES ARISING OUT OF THE
USE OR INABILITY TO USE THE PROGRAM (INCLUDING BUT NOT LIMITED TO LOSS OF
DATA OR DATA BEING RENDERED INACCURATE OR LOSSES SUSTAINED BY YOU OR THIRD
PARTIES OR A FAILURE OF THE PROGRAM TO OPERATE WITH ANY OTHER PROGRAMS),
EVEN IF SUCH HOLDER OR OTHER PARTY HAS BEEN ADVISED OF THE POSSIBILITY OF
SUCH DAMAGES.

  17. Interpretation of Sections 15 and 16.

  If the disclaimer of warranty and limitation of liability provided
above cannot be given local legal effect according to their terms,
reviewing courts shall apply local law that most closely approximates
an absolute waiver of all civil liability in connection with the
Program, unless a warranty or assumption of liability accompanies a
copy of the Program in return for a fee.

                     END OF TERMS AND CONDITIONS

            How to Apply These Terms to Your New Programs

  If you develop a new program, and you want it to be of the greatest
possible use to the public, the best way to achieve this is to make it
free software which everyone can redistribute and change under these terms.

  To do so, attach the following notices to the program.  It is safest
to attach them to the start of each source file to most effectively
state the exclusion of warranty; and each file should have at least
the "copyright" line and a pointer to where the full notice is found.

    {one line to give the program's name and a brief idea of what it does.}
    Copyright (C) {year}  {name of author}

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.

Also add information on how to contact you by electronic and paper mail.

  If the program does terminal interaction, make it output a short
notice like this when it starts in an interactive mode:

    {project}  Copyright (C) {year}  {fullname}
    This program comes with ABSOLUTELY NO WARRANTY; for details type `show w'.
    This is free software, and you are welcome to redistribute it
    under certain conditions; type `show c' for details.

The hypothetical commands `show w' and `show c' should show the appropriate
parts of the General Public License.  Of course, your program's commands
might be different; for a GUI interface, you would use an "about box".

  You should also get your employer (if you work as a programmer) or school,
if any, to sign a "copyright disclaimer" for the program, if necessary.
For more information on this, and how to apply and follow the GNU GPL, see
<http://www.gnu.org/licenses/>.

  The GNU General Public License does not permit incorporating your program
into proprietary programs.  If your program is a subroutine library, you
may consider it more useful to permit linking proprietary applications with
the library.  If this is what you want to do, use the GNU Lesser General
Public License instead of this License.  But first, please read
<http://www.gnu.org/philosophy/why-not-lgpl.html>.


File: /playbooks\add_clients.yml
- name: Add clients to OpenVPN's PKI
# ========================================================
  # Allows caller to override hosts using '-e cmd_hosts='
  hosts: "{{ cmd_hosts | default('openvpn') }}"

  roles:
    - add_clients


File: /playbooks\install.yml
- name: Install required software, configure and harden
# ========================================================
  hosts: "{{ cmd_hosts | default('openvpn') }}"

# You need a python 2 interpreter first, so skip gathering facts, then use
# 'setup:' to get them after the python 2 interpreter has been installed.
# See 'pre_tasks' below
  gather_facts: False
  pre_tasks:
    # If python doesn't exist on path (type returns non-zero), install python
    - name: OpenVPN | install | Install python2 if necessary
      raw: 'type python >/dev/null 2>&1 || (apt -y update && apt install -y python-minimal)'
      changed_when: false

    - name: OpenVPN | install | Gather facts after python2 is available
      setup:

  roles:
    - openvpn

File: /playbooks\revoke_clients.yml
- name: Revoke client access
# ========================================================
  # Allows caller to override hosts using '-e cmd_hosts='
  hosts: "{{ cmd_hosts | default('openvpn') }}"

  roles:
    - revoke_clients


File: /playbooks\roles\add_clients\tasks\add_gen_key.yml
---
- name: OpenVPN | Add Clients | Check for existing private key passwords
  delegate_to: localhost
  stat:
    path: "{{ local_creds_folder }}/{{ item }}/{{ openvpn_server_common_name }}_pk_pass.txt"
  become: False
  register: client_pk_passwords_local
  with_items:
    - "{{ clients_to_add }}"

- name: OpenVPN | Add Clients | Generate private key passwords
  shell: echo "$(head /dev/urandom | tr -dc A-Za-z0-9 | head -c15)"
  no_log: true
  register: client_pk_passwords
  with_items: "{{ clients_to_add }}"
  when: not client_pk_passwords_local.results[0].stat.exists

- name: OpenVPN | Add Clients | Make local destination
  delegate_to: localhost
  file:
    path: "{{ local_creds_folder }}/{{ item }}/"
    state: directory
  become: False
  with_items:
    - "{{ clients_to_add }}"

- name: OpenVPN | Add Clients | Write private key pass phrases
  delegate_to: localhost
  copy:
    content: "{{ item[1].stdout }}"
    dest: "{{ local_creds_folder }}/{{ item[0] }}/{{ openvpn_server_common_name }}_pk_pass.txt"
  no_log: true
  become: False
  with_together:
    - "{{ clients_to_add }}"
    - "{{ client_pk_passwords.results }}"
  when: not client_pk_passwords_local.results[0].stat.exists

- name: OpenVPN | Add Clients | Read private key pass phrases
  delegate_to: localhost
  command: cat "{{ local_creds_folder }}/{{ item }}/{{ openvpn_server_common_name }}_pk_pass.txt"
  no_log: true
  become: False
  register: client_pk_passwords
  with_items: "{{ clients_to_add }}"
  changed_when: false

- name: OpenVPN | Add Clients | Build Clients
  expect:
    command: ./easyrsa build-client-full "{{ item[0] }}" --req-cn "{{ item[0] }}"
    responses:
      'Enter PEM pass phrase:$': "{{ item[1].stdout }}"
      'Verifying - Enter PEM pass phrase:$': "{{ item[1].stdout }}"
      'Enter pass phrase for .*?:$': "{{ ca_password }}"
    chdir: "{{ openvpn_path_easyrsa }}"
    creates: "{{ openvpn_path_keys }}/{{ item[0] }}.key"
  no_log: true
  with_together:
    - "{{ clients_to_add }}"
    - "{{ client_pk_passwords.results }}"

- name: OpenVPN | Add Clients | Make client configuration directory
  file:
    path: "{{ openvpn_path_pki }}/ovpn"
    mode: 0700
    state: directory

- name: OpenVPN | Add Clients | Register CA certificate contents
  command: cat {{ openvpn_ca_cert }}
  no_log: true
  register: openvpn_ca_contents
  changed_when: false

- name: OpenVPN | Add Clients | Register HMAC firewall key contents
  command: cat {{ openvpn_hmac_firewall }}
  no_log: true
  register: openvpn_hmac_firewall_contents
  changed_when: false

- name: OpenVPN | Add Clients | Register client key contents
  command: cat "{{ openvpn_path_keys }}/{{ item }}.key"
  with_items: "{{ clients_to_add }}"
  no_log: true
  register: openvpn_client_keys
  changed_when: false

- name: OpenVPN | Add Clients | Register client certificate contents
  command: cat "{{ openvpn_path_certs }}/{{ item }}.crt"
  with_items: "{{ clients_to_add }}"
  no_log: true
  register: openvpn_client_certs
  changed_when: false

- name: OpenVPN | Add Clients | Build client configs (.ovpn files; pki embedded)
  template:
    src: client_pki_embedded.ovpn.j2
    dest: "{{ openvpn_path_pki }}/ovpn/{{ item[0] }}-pki-embedded.ovpn"
    mode: 0400
  no_log: true
  with_together:
    - "{{ clients_to_add }}"
    - "{{ openvpn_client_certs.results }}"
    - "{{ openvpn_client_keys.results }}"

- name: OpenVPN | Add Clients | Build client configs (.ovpn files; pki external files)
  template:
    src: client_pki_files.ovpn.j2
    dest: "{{ openvpn_path_pki }}/ovpn/{{ item }}-pki-files.ovpn"
    mode: 0400
  no_log: true
  with_items:
    - "{{ clients_to_add }}"

- name: OpenVPN | Add Clients | Get list of clients with ccd defined
  set_fact:
    valid_clients_with_ccd: "{{ valid_clients | selectattr('ccd', 'defined') | selectattr('name', 'defined') | list }}"

- name: OpenVPN | Add Clients | Build ccd configs
  template:
    src: client_ccd.j2
    dest: "{{ openvpn_path_ccd }}/{{ item.name }}"
    mode: 0644
  with_items: "{{ valid_clients_with_ccd }}"

- name: OpenVPN | Add Clients | Build client configs (.ovpn files; external pkcs12)
  template:
    src: client_pkcs12.ovpn.j2
    dest: "{{ openvpn_path_pki }}/ovpn/{{ item }}-pkcs12.ovpn"
    mode: 0400
  no_log: true
  with_items:
    - "{{ clients_to_add }}"

- name: OpenVPN | Add Clients | Generate PKCS#12
  shell: >
    openssl pkcs12 -export
    -in "{{ openvpn_path_certs }}/{{ item[0] }}.crt"
    -inkey "{{ openvpn_path_keys }}/{{ item[0] }}.key"
    -certfile {{ openvpn_ca_cert }}
    -name "{{ item[0] }}"
    -out "{{ openvpn_path_pki }}/ovpn/{{ item[0] }}.p12"
    -passin pass:{{ item[1].stdout }}
    -passout pass:{{ item[1].stdout }}
  args:
    creates: "{{ openvpn_path_pki }}/ovpn/{{ item[0] }}.p12"
  no_log: true
  with_together:
    - "{{ clients_to_add }}"
    - "{{ client_pk_passwords.results }}"
  tags:
    - skip_ansible_lint

- name: OpenVPN | Add Clients | Get .ovpn files (*-pki-embedded.ovpn)
  fetch:
    src: "{{ openvpn_path_pki }}/ovpn/{{ item }}-pki-embedded.ovpn"
    dest: "{{ local_creds_folder }}/{{ item }}/"
    flat: yes
  with_items:
    - "{{ clients_to_add }}"

- name: OpenVPN | Add Clients | Get .ovpn files (*-pki-files.ovpn)
  fetch:
    src: "{{ openvpn_path_pki }}/ovpn/{{ item }}-pki-files.ovpn"
    dest: "{{ local_creds_folder }}/{{ item }}/"
    flat: yes
  with_items:
    - "{{ clients_to_add }}"

- name: OpenVPN | Add Clients | Get .ovpn files (*-pkcs12.ovpn)
  fetch:
    src: "{{ openvpn_path_pki }}/ovpn/{{ item }}-pkcs12.ovpn"
    dest: "{{ local_creds_folder }}/{{ item }}/"
    flat: yes
  with_items:
    - "{{ clients_to_add }}"

- name: OpenVPN | Add Clients | Get client PKCS#12 files
  fetch:
    src: "{{ openvpn_path_pki }}/ovpn/{{ item }}.p12"
    dest: "{{ local_creds_folder }}/{{ item }}/"
    flat: yes
  with_items:
    - "{{ clients_to_add }}"

- name: OpenVPN | Add Clients | Get client CA cert
  fetch:
    src: "{{ openvpn_ca_cert }}"
    dest: "{{ local_creds_folder }}/{{ item }}/"
    flat: yes
  with_items:
    - "{{ clients_to_add }}"

- name: OpenVPN | Add Clients | Get client certs
  fetch:
    src: "{{ openvpn_path_certs }}/{{ item }}.crt"
    dest: "{{ local_creds_folder }}/{{ item }}/"
    flat: yes
  with_items:
    - "{{ clients_to_add }}"

- name: OpenVPN | Add Clients | Get client keys
  fetch:
    src: "{{ openvpn_path_keys }}/{{ item }}.key"
    dest: "{{ local_creds_folder }}/{{ item }}/"
    flat: yes
  with_items:
    - "{{ clients_to_add }}"

- name: OpenVPN | Add Clients | Clear bash history
  shell: cat /dev/null > ~/.bash_history && history -c
  args:
    executable: /bin/bash
  ignore_errors: true
  changed_when: false


File: /playbooks\roles\add_clients\tasks\main.yml
---
- name: OpenVPN | Add Clients | Set variables
  include_vars: ../../openvpn/defaults/main.yml

- name: OpenVPN | Add Clients | Register the OpenVPN server common name
  command: cat {{ openvpn_server_common_name_file }}
  no_log: true
  register: openvpn_server_common_name_result
  changed_when: false

- name: OpenVPN | Add Clients | Set server common name variable
  set_fact:
    openvpn_server_common_name: "{{ openvpn_server_common_name_result.stdout }}"

- name: OpenVPN | Add Clients | Add clients and generate keys
  include: add_gen_key.yml
  when: clients_to_add is defined



File: /playbooks\roles\add_clients\templates\client_ccd.j2
{% for entry in item.ccd %}
{{ entry }}
{% endfor %}

File: /playbooks\roles\add_clients\templates\client_common.ovpn.j2
client

{% for instance in openvpn_instances %}
remote {{ openvpn_server_remote_host }} {{ instance.port }} {{ instance.proto }}

{% for item in instance.client_extra_options %}
{{ item }}
{% endfor %}

{% endfor %}

dev tun
cipher {{ openvpn_cipher }}
auth {{ openvpn_auth_digest }}
resolv-retry infinite
nobind
persist-key
persist-tun
remote-cert-tls server
verify-x509-name "server@{{ openvpn_server_common_name }}" name
tls-version-min 1.2
#comp-lzo
key-direction 1
verb 3
{#
<tls-auth>
{{ openvpn_hmac_firewall_contents.stdout }}
</tls-auth>
#}

File: /playbooks\roles\add_clients\templates\client_pkcs12.ovpn.j2
{% include "client_common.ovpn.j2" %}

pkcs12 {{ item }}.p12


File: /playbooks\roles\add_clients\templates\client_pki_embedded.ovpn.j2
{% include "client_common.ovpn.j2" %}

<ca>
{{ openvpn_ca_contents.stdout }}
</ca>

<cert>
{{ item[1].stdout }}
</cert>

<key>
{{ item[2].stdout }}
</key>


File: /playbooks\roles\add_clients\templates\client_pki_files.ovpn.j2
{% include "client_common.ovpn.j2" %}

ca ca.crt
cert {{ item }}.crt
key {{ item }}.key


File: /playbooks\roles\openvpn\defaults\main.yml
---
required_packages:
  - sudo
  - python-pip
  - python-virtualenv
  - git
  # Used for the sync_clients matching
  - gawk
  # Used to verify GPG signatures for mirrored packages
  - gnupg
  - iptables
  # Used to keep iptables rules after reboot
  - iptables-persistent
  - netfilter-persistent
  # Word List dictionary used by several roles to generate random data
  - "{{ package_name_words }}"
  - openssl
  - openvpn


File: /playbooks\roles\openvpn\handlers\main.yml
---
- name: clear history
  shell: cat /dev/null > ~/.bash_history && history -c
  args:
    executable: /bin/bash
  changed_when: false

- name: start openvpn
  service:
    name: "openvpn@{{ item.proto }}-{{ item.port }}.service"
    state: started
  with_items: "{{ openvpn_instances }}"


File: /playbooks\roles\openvpn\tasks\firewall.yml
---
- name: OpenVPN | Firewall | Reread ansible_default_ipv4
  setup:
    filter: ansible_default_ipv4*

- name: OpenVPN | Firewall | Flush existing firewall rules
  iptables:
    table: nat
    flush: true
  when: load_iptables_rules
  changed_when: false

- name: OpenVPN | Firewall | Write iptables rules file
  template:
    src: etc_iptables_rules.v4.j2
    dest: "{{ openvpn_path_iptables_rules }}"
    owner: root
    group: root
    mode: 0744

- name: OpenVPN | Firewall | Load iptables rules
  command: "{{ openvpn_path_iptables_rules }}"
  when: load_iptables_rules
  changed_when: false


File: /playbooks\roles\openvpn\tasks\main.yml
---
- name: OpenVPN | Install | Set Distro/Version specific variables
  include_vars: "{{ item }}"
  with_first_found:
    #- "../vars/{{ ansible_distribution }}-{{ ansible_distribution_major_version | int}}.yml"
    #- "../vars/{{ ansible_distribution }}.yml"
    - "../vars/{{ ansible_os_family }}.yml"
    #- "../vars/default.yml"
  notify:
    - clear history

- include: packages.yml
- include: pki.yml
- include: openvpn.yml
- include: firewall.yml

File: /playbooks\roles\openvpn\tasks\openvpn.yml
---
- name: OpenVPN | sysctl | Enable IPv4 traffic forwarding
  sysctl:
    name: net.ipv4.ip_forward
    value: 1

- name: OpenVPN | Configuration | Create client configuration directory
  file:
    path: "{{ openvpn_path_ccd }}"
    state: directory
    mode: 0755

- name: OpenVPN | Configuration | Copy OpenVPN server configuration files into place
  template:
    src: etc_openvpn_server.conf.j2
    dest: "{{ openvpn_path }}/{{ item.proto }}-{{ item.port }}.conf"
  with_items: "{{ openvpn_instances }}"
  notify:
    - start openvpn

- name: OpenVPN | systemd | Enable services
  service:
    name: "openvpn@{{ item.proto }}-{{ item.port }}.service"
    enabled: true
  with_items: "{{ openvpn_instances }}"
  notify:
    - start openvpn


File: /playbooks\roles\openvpn\tasks\packages.yml
---
- name: OpenVPN | package | Ensure the APT cache is up to date
  apt:
    update_cache: yes
  changed_when: False
  when: ansible_os_family == "Debian"

- name: OpenVPN | package | Install {{ ansible_os_family }} specific packages
  package:
    name: "{{ item }}"
  with_items: "{{ os_family_specific_pre }}"
  register: install_specific_result
  until: install_specific_result is success
  retries: 5
  delay: 5

#- name: OpenVPN | package | Get official OpenVPN APT key
#  # Work around for ansible issue https://github.com/ansible/ansible/issues/22647
#  get_url:
#    url: https://swupdate.openvpn.net/repos/repo-public.gpg
#    dest: ~/openvpn.gpg
#  when: ansible_os_family == "Debian"
#
#- name: OpenVPN | package | Add the official OpenVPN APT key
#  # Work around for ansible issue https://github.com/ansible/ansible/issues/22647
#  apt_key:
#    file: ~/openvpn.gpg
#    state: present
#  when: ansible_os_family == "Debian"
#
#- name: OpenVPN | package | Reread ansible_lsb facts
#  setup: filter=ansible_lsb*
#
#- name: OpenVPN | package | Add the official OpenVPN repository
#  apt_repository:
#    repo: 'deb https://build.openvpn.net/debian/openvpn/stable {{ ansible_lsb.codename }} main'
#    state: present
#    update_cache: yes
#  when: ansible_os_family == "Debian"

- name: OpenVPN | package | Add debian backports
  apt_repository:
    repo: 'deb http://ftp.debian.org/debian {{ ansible_lsb.codename }}-backports main'
    state: present
    update_cache: yes
  when: ansible_distribution in ['Debian']

- name: OpenVPN | package | Upgrade systemd on debian
  apt:
    name: systemd
    state: latest
    default_release: "{{ ansible_lsb.codename }}-backports"
  when: ansible_distribution in ['Debian']
  tags:
    # Need latest, systemd v215 is really old and a pain to support alongside newer versions
    - skip_ansible_lint

- name: OpenVPN | package | Install required packages
  package:
    name: "{{ item }}"
  with_items: "{{ required_packages }}"
  register: install_required_result
  until: install_required_result is success
  retries: 5
  delay: 5
  tags:
    - skip_ansible_lint

- name: OpenVPN | package | Install pexpect via pip
  pip:
    name: "pexpect"
    version: "3.3"


File: /playbooks\roles\openvpn\tasks\pki.yml
---
- name: OpenVPN | PKI | EasyRSA Checkout
  git:
    repo: https://github.com/OpenVPN/easy-rsa.git
    accept_hostkey: True
    remote: github
    version: "{{ openvpn_easyrsa_version }}"
    dest: "{{ openvpn_path }}/easyrsa"

- name: OpenVPN | PKI | Make local destination folder
  delegate_to: localhost
  file: path={{ local_creds_folder }}/ state=directory
  become: False

- name: OpenVPN | PKI | Generate a random server common name
  shell: grep -v -P "[\x80-\xFF]" {{ path_dict }} | sed -e "s/'//" | shuf -n 2 | xargs | sed -e 's/ /./g' | cut -c 1-64 > {{ openvpn_server_common_name_file }}
  args:
    creates: "{{ openvpn_server_common_name_file }}"
  when: openvpn_server_common_name_manual is not defined

- name: OpenVPN | PKI | Set server common name
  shell: echo "{{ openvpn_server_common_name_manual }}" > {{ openvpn_server_common_name_file }}
  args:
    creates: "{{ openvpn_server_common_name_file }}"
  when: openvpn_server_common_name_manual is defined

- name: OpenVPN | PKI | Register the OpenVPN server common name
  command: cat {{ openvpn_server_common_name_file }}
  register: openvpn_server_common_name_result
  changed_when: false

- name: OpenVPN | PKI | Generate CA password
  shell: echo "$(head /dev/urandom | tr -dc A-Za-z0-9 | head -c15)"
  no_log: true
  register: ca_password_result
  when: ca_password is not defined

- name: OpenVPN | PKI | Store CA password
  delegate_to: localhost
  lineinfile:
    line: "ca_password: {{ ca_password_result.stdout }}"
    path: "{{ inventory_dir }}/host_vars/{{ inventory_hostname }}.yml"
    create: true
  become: False
  when: ca_password is not defined

- name: OpenVPN | PKI | Set CA password variable
  set_fact:
    ca_password: "{{ ca_password_result.stdout }}"
  when: ca_password is not defined

- name: OpenVPN | PKI | Set common name variable
  set_fact:
    openvpn_server_common_name: "{{ openvpn_server_common_name_result.stdout }}"

- name: OpenVPN | PKI | Set server key and cert path variables
  set_fact:
    path_server_key: "{{ openvpn_path_keys }}/server@{{ openvpn_server_common_name }}.key"
    path_server_cert: "{{ openvpn_path_certs }}/server@{{ openvpn_server_common_name }}.crt"

- name: OpenVPN | PKI | EasyRSA Link project
  file:
    src: ./easyrsa/easyrsa3/pki
    dest: "{{ openvpn_path_pki }}"
    owner: root
    group: root
    force: yes
    state: link

- name: OpenVPN | PKI | Deploy vars configuration
  template:
    src: etc_openvpn_easyrsa_easyrsa3_vars.j2
    dest: "{{ openvpn_path_easyrsa }}/vars"
    owner: root
    group: root
    mode: 0600

- name: OpenVPN | PKI | Intialize PKI
  shell: echo 'yes' | ./easyrsa init-pki
  args:
    chdir: "{{ openvpn_path_easyrsa }}"
    creates: "{{ openvpn_path_keys }}"

- name: OpenVPN | PKI | Build CA
  expect:
    command: ./easyrsa build-ca --req-cn "ca@{{ openvpn_server_common_name }}"
    responses:
      'Enter New CA Key Passphrase: $': "{{ ca_password }}"
      'Re-Enter New CA Key Passphrase: $': "{{ ca_password }}"
    chdir: "{{ openvpn_path_easyrsa }}"
    creates: "{{ openvpn_path_easyrsa }}/pki/private/ca.key"

- name: OpenVPN | PKI | Build CRL
  expect:
    command: ./easyrsa gen-crl
    responses:
      'Enter pass phrase for .*?:$': "{{ ca_password }}"
    chdir: "{{ openvpn_path_easyrsa }}"
    creates: "{{ openvpn_crl }}"

- name: OpenVPN | PKI | Add server
  expect:
    command: ./easyrsa build-server-full "server@{{ openvpn_server_common_name }}" nopass --req-cn "server@{{ openvpn_server_common_name }}"
    responses:
      'Enter pass phrase for .*?:$' : "{{ ca_password }}"
    chdir: "{{ openvpn_path_easyrsa }}"
    creates: "{{ path_server_key }}"

- name: OpenVPN | PKI | Build ta.key
  shell: openvpn --genkey --secret ta.key
  args:
    chdir: "{{ openvpn_path_easyrsa }}/pki"
    creates: "{{ openvpn_hmac_firewall }}"
  tags:
    - skip_ansible_lint

- name: OpenVPN | PKI | Build dh.pem
  shell: ./easyrsa gen-dh
  args:
    chdir: "{{ openvpn_path_easyrsa }}"
    creates: "{{ dhparams_location }}"
  tags:
    - skip_ansible_lint

- name: OpenVPN | Add Clients | Get CA cert
  fetch:
    src: "{{ openvpn_ca_cert }}"
    dest: "{{ local_creds_folder }}/ca@{{ openvpn_server_common_name }}.crt"
    flat: yes


File: /playbooks\roles\openvpn\templates\etc_iptables_rules.v4.j2
#!/usr/bin/env bash
# Generated by ansible
# This script is used to configure iptables to work with OpenVPN on this host

# Allow connections to the VPN
{#
{% for instance in openvpn_instances %}
{{ iptables_path }} -A INPUT -p {{ instance.proto }} --dport {{ instance.port }} -j ACCEPT
{% endfor %}
#}
# This rule is necessary for OpenVPN to work and forward IP packets
{% for instance in openvpn_instances %}
{{ iptables_path }} -t nat -A POSTROUTING -s {{ instance.cidr }} -o {{ ansible_default_ipv4.interface }} -j MASQUERADE
{% endfor %}

{#
{% for instance in openvpn_instances %}
{{ iptables_path }} -A FORWARD -s {{ instance.cidr }} -j ACCEPT
{% endfor %}
#}

{#
# Allow SSH connections on the VPN
{% for instance in openvpn_instances %}
{{ iptables_path }} -A INPUT -p tcp -d {{ instance.cidr }} --dport {{ ansible_port | default('22') }} -j ACCEPT
{% endfor %}
#}

# Consider removing SSH access from the main IPv4 address after you established a VPN connection, e.g. with:
{#
{{ iptables_path }} -A INPUT -p tcp -i {{ ansible_default_ipv4.interface }} --dport {{ ansible_port | default('22') }} -j DROP
#}
# Save rules
/usr/sbin/netfilter-persistent save


File: /playbooks\roles\openvpn\templates\etc_openvpn_easyrsa_easyrsa3_vars.j2
# Easy-RSA 3 parameter settings

# NOTE: If you installed Easy-RSA from your distro's package manager, don't edit
# this file in place -- instead, you should copy the entire easy-rsa directory
# to another location so future upgrades don't wipe out your changes.

# HOW TO USE THIS FILE
#
# vars.example contains built-in examples to Easy-RSA settings. You MUST name
# this file 'vars' if you want it to be used as a configuration file. If you do
# not, it WILL NOT be automatically read when you call easyrsa commands.
#
# It is not necessary to use this config file unless you wish to change
# operational defaults. These defaults should be fine for many uses without the
# need to copy and edit the 'vars' file.
#
# All of the editable settings are shown commented and start with the command
# 'set_var' -- this means any set_var command that is uncommented has been
# modified by the user. If you're happy with a default, there is no need to
# define the value to its default.

# NOTES FOR WINDOWS USERS
#
# Paths for Windows  *MUST* use forward slashes, or optionally double-esscaped
# backslashes (single forward slashes are recommended.) This means your path to
# the openssl binary might look like this:
# "C:/Program Files/OpenSSL-Win32/bin/openssl.exe"

# A little housekeeping: DON'T EDIT THIS SECTION
#
# Easy-RSA 3.x doesn't source into the environment directly.
# Complain if a user tries to do this:
if [ -z "$EASYRSA_CALLER" ]; then
  echo "You appear to be sourcing an Easy-RSA 'vars' file." >&2
  echo "This is no longer necessary and is disallowed. See the section called" >&2
  echo "'How to use this file' near the top comments for more details." >&2
  return 1
fi

# DO YOUR EDITS BELOW THIS POINT

# This variable should point to the top level of the easy-rsa tree. By default,
# this is taken to be the directory you are currently in.

#set_var EASYRSA  "$PWD"

# If your OpenSSL command is not in the system PATH, you will need to define the
# path to it here. Normally this means a full path to the executable, otherwise
# you could have left it undefined here and the shown default would be used.
#
# Windows users, remember to use paths with forward-slashes (or escaped
# back-slashes.) Windows users should declare the full path to the openssl
# binary here if it is not in their system PATH.

#set_var EASYRSA_OPENSSL  "openssl"
#
# This sample is in Windows syntax -- edit it for your path if not using PATH:
#set_var EASYRSA_OPENSSL  "C:/Program Files/OpenSSL-Win32/bin/openssl.exe"

# Edit this variable to point to your soon-to-be-created key directory.
#
# WARNING: init-pki will do a rm -rf on this directory so make sure you define
# it correctly! (Interactive mode will prompt before acting.)

#set_var EASYRSA_PKI    "$EASYRSA/pki"

# Define X509 DN mode.
# This is used to adjust what elements are included in the Subject field as the DN
# (this is the "Distinguished Name.")
# Note that in cn_only mode the Organizational fields further below aren't used.
#
# Choices are:
#   cn_only  - use just a CN value
#   org      - use the "traditional" Country/Province/City/Org/OU/email/CN format
{% if easyrsa_dn_mode_cn_only %}
set_var EASYRSA_DN "cn_only"
{% else %}
set_var EASYRSA_DN "org"
{% endif %}

# Organizational fields (used with 'org' mode and ignored in 'cn_only' mode.)
# These are the default values for fields which will be placed in the
# certificate.  Don't leave any of these fields blank, although interactively
# you may omit any specific field by typing the "." symbol (not valid for
# email.)

set_var EASYRSA_REQ_COUNTRY  "{{ openvpn_key_country }}"
set_var EASYRSA_REQ_PROVINCE "{{ openvpn_key_province }}"
set_var EASYRSA_REQ_CITY "{{ openvpn_key_city }}"
set_var EASYRSA_REQ_ORG  "{{ openvpn_key_org }}"
set_var EASYRSA_REQ_EMAIL  "{{ openvpn_key_email }}"
set_var EASYRSA_REQ_OU   "{{ openvpn_key_ou }}"

# Choose a size in bits for your keypairs. The recommended value is 2048.  Using
# 2048-bit keys is considered more than sufficient for many years into the
# future. Larger keysizes will slow down TLS negotiation and make key/DH param
# generation take much longer. Values up to 4096 should be accepted by most
# software. Only used when the crypto alg is rsa (see below.)

set_var EASYRSA_KEY_SIZE {{ dhparams_size }}

# The default crypto mode is rsa; ec can enable elliptic curve support.
# Note that not all software supports ECC, so use care when enabling it.
# Choices for crypto alg are: (each in lower-case)
#  * rsa
#  * ec

#set_var EASYRSA_ALGO   rsa

# Define the named curve, used in ec mode only:

#set_var EASYRSA_CURVE    secp384r1

# In how many days should the root CA key expire?

#set_var EASYRSA_CA_EXPIRE  3650

# In how many days should certificates expire?

#set_var EASYRSA_CERT_EXPIRE  3650

# How many days until the next CRL publish date?  Note that the CRL can still be
# parsed after this timeframe passes. It is only used for an expected next
# publication date.

#set_var EASYRSA_CRL_DAYS 180

# Support deprecated "Netscape" extensions? (choices "yes" or "no".) The default
# is "no" to discourage use of deprecated extensions. If you require this
# feature to use with --ns-cert-type, set this to "yes" here. This support
# should be replaced with the more modern --remote-cert-tls feature.  If you do
# not use --ns-cert-type in your configs, it is safe (and recommended) to leave
# this defined to "no".  When set to "yes", server-signed certs get the
# nsCertType=server attribute, and also get any NS_COMMENT defined below in the
# nsComment field.

#set_var EASYRSA_NS_SUPPORT "no"

# When NS_SUPPORT is set to "yes", this field is added as the nsComment field.
# Set this blank to omit it. With NS_SUPPORT set to "no" this field is ignored.

#set_var EASYRSA_NS_COMMENT "Easy-RSA Generated Certificate"

# A temp file used to stage cert extensions during signing. The default should
# be fine for most users; however, some users might want an alternative under a
# RAM-based FS, such as /dev/shm or /tmp on some systems.

#set_var EASYRSA_TEMP_FILE  "$EASYRSA_PKI/extensions.temp"

# !!
# NOTE: ADVANCED OPTIONS BELOW THIS POINT
# PLAY WITH THEM AT YOUR OWN RISK
# !!

# Broken shell command aliases: If you have a largely broken shell that is
# missing any of these POSIX-required commands used by Easy-RSA, you will need
# to define an alias to the proper path for the command.  The symptom will be
# some form of a 'command not found' error from your shell. This means your
# shell is BROKEN, but you can hack around it here if you really need. These
# shown values are not defaults: it is up to you to know what you're doing if
# you touch these.
#
#alias awk="/alt/bin/awk"
#alias cat="/alt/bin/cat"

# X509 extensions directory:
# If you want to customize the X509 extensions used, set the directory to look
# for extensions here. Each cert type you sign must have a matching filename,
# and an optional file named 'COMMON' is included first when present. Note that
# when undefined here, default behaviour is to look in $EASYRSA_PKI first, then
# fallback to $EASYRSA for the 'x509-types' dir.  You may override this
# detection with an explicit dir here.
#
#set_var EASYRSA_EXT_DIR  "$EASYRSA/x509-types"

# OpenSSL config file:
# If you need to use a specific openssl config file, you can reference it here.
# Normally this file is auto-detected from a file named openssl-1.0.cnf from the
# EASYRSA_PKI or EASYRSA dir (in that order.) NOTE that this file is Easy-RSA
# specific and you cannot just use a standard config file, so this is an
# advanced feature.

#set_var EASYRSA_SSL_CONF "$EASYRSA/openssl-1.0.cnf"

# Default CN:
# This is best left alone. Interactively you will set this manually, and BATCH
# callers are expected to set this themselves.

set_var EASYRSA_REQ_CN   "ca@{{ openvpn_server_common_name }}"

# Cryptographic digest to use.
# Do not change this default unless you understand the security implications.
# Valid choices include: md5, sha1, sha256, sha224, sha384, sha512

#set_var EASYRSA_DIGEST   "sha256"

# Batch mode. Leave this disabled unless you intend to call Easy-RSA explicitly
# in batch mode without any user input, confirmation on dangerous operations,
# or most output. Setting this to any non-blank string enables batch mode.

set_var EASYRSA_BATCH    "yes"


File: /playbooks\roles\openvpn\templates\etc_openvpn_server.conf.j2
dev tun-{{ item.proto }}-{{ item.port }}
server {{ item.mask }}
proto {{ item.proto }}
port {{ item.port }}

ca {{ openvpn_ca_cert }}
cert "{{ path_server_cert }}"
key "{{ path_server_key }}"
dh {{ dhparams_location }}
crl-verify {{ openvpn_crl }}

{% for item in item.server_extra_options %}
{{ item }}
{% endfor %}

# Fix for the Windows 10 DNS leak described here:
# https://community.openvpn.net/openvpn/ticket/605
#push block-outside-dns

remote-cert-tls client
keepalive 10 120
#tls-auth {{ openvpn_hmac_firewall }} 0
cipher {{ openvpn_cipher }}
tls-cipher {{ openvpn_tls_cipher }}
auth {{ openvpn_auth_digest }}
tls-version-min 1.2
#comp-lzo
persist-key
persist-tun

client-to-client
keepalive 10 120
tun-mtu 1500
mssfix 1450
File: /playbooks\roles\openvpn\templates\group_vars_all.yml.j2
---
# Generated by pki.yml task
ca_password: {{ ca_password_result.stdout }}


File: /playbooks\roles\openvpn\vars\Debian.yml
---

package_name_words: wamerican-huge

path_dict: /usr/share/dict/american-english-huge

os_family_specific_pre:
  # Make sure https repos can be added (needed for OpenVPN repo)
  #- apt-transport-https
  #- ca-certificates
  # Required for the apt_repository module
  #- python-software-properties
  #- software-properties-common


File: /playbooks\roles\openvpn\vars\RedHat.yml
---
package_name_words: words

path_dict: /usr/share/dict/words

os_family_specific_pre:
  - epel-release
  - yum-cron
  - yum-utils

File: /playbooks\roles\revoke_clients\tasks\main.yml
---
- name: OpenVPN | Revoke Client | Set variables
  include_vars: ../../openvpn/defaults/main.yml

- name: OpenVPN | Revoke Client | Register the OpenVPN server common name
  command: cat {{ openvpn_server_common_name_file }}
  no_log: true
  register: openvpn_server_common_name_result
  changed_when: false

- name: OpenVPN | Revoke Client | Set the server common name
  set_fact:
    openvpn_server_common_name: "{{ openvpn_server_common_name_result.stdout }}"

- name: OpenVPN | Revoke Client | Revoke access
  expect:
    command: ./easyrsa revoke "{{ item }}"
    responses:
      'Enter pass phrase for .*?:$': "{{ ca_password }}"
    chdir: "{{ openvpn_path_easyrsa }}"
  no_log: false
  with_items: "{{ clients_to_revoke }}"

- name: OpenVPN | Revoke Client | Rebuild CRL
  expect:
    command: ./easyrsa gen-crl
    responses:
      'Enter pass phrase for .*?:$': "{{ ca_password }}"
    chdir: "{{ openvpn_path_easyrsa }}"


File: /playbooks\roles\sync_clients\tasks\main.yml
---
- name: OpenVPN | Sync Clients | Register the OpenVPN server common name
  command: cat {{ openvpn_server_common_name_file }}
  no_log: true
  register: openvpn_server_common_name_result
  changed_when: false

- name: OpenVPN | Sync Clients | Set server common name variable
  set_fact:
    openvpn_server_common_name: "{{ openvpn_server_common_name_result.stdout }}"

- name: OpenVPN | Sync Clients | Get clients that are currently valid
  shell: awk '/^V\s/' {{ openvpn_path_pki }}/index.txt | awk -F 'CN=' '{print $NF}' | awk -F '/' '{print $1}'
  register: currently_valid_clients_out
  changed_when: false

- name: OpenVPN | Sync Clients | Get list of desired valid clients
  set_fact:
    valid_clients_names: "{{ valid_clients | map(attribute='name') | list }}"

- name: OpenVPN | Sync Clients | Set facts
  set_fact:
    currently_valid_clients: "{{ currently_valid_clients_out.stdout.splitlines() }}"
    desired_valid_clients: "{{ valid_clients_names }} + [ 'server@' + openvpn_server_common_name ]"
    clients_to_revoke: []
    clients_to_add: []

- name: OpenVPN | Sync Clients | Sync clients that will be revoked
  set_fact:
    clients_to_revoke: "{{ currently_valid_clients | difference(desired_valid_clients) }}"

- name: OpenVPN | Sync Clients | Sync clients that will be added
  set_fact:
    clients_to_add: "{{ desired_valid_clients | difference(currently_valid_clients) }}"

- name: OpenVPN | Sync Clients | Ask user if we should proceed
  pause:
    prompt: "We will add {{ clients_to_add }} and we will revoke {{ clients_to_revoke }}. Press 'Y' or 'y' to proceed"
  when: prompt_before_syncing_clients
  register: sync_prompt

- name: OpenVPN | Sync Clients | Abort if user does not want to proceed
  fail:
    msg: "Aborted due to user input!"
  when: prompt_before_syncing_clients and sync_prompt.user_input not in ["Y", "y"]

- name: OpenVPN | Sync Clients | Add clients
  include_role:
    name: add_clients
  when: clients_to_add | length

- name: OpenVPN | Sync Clients | Revoke clients
  include_role:
    name: revoke_clients
  when: clients_to_revoke | length


File: /playbooks\sync_clients.yml
- name: Sync desired valid clients with OpenVPN's current PKI
# ========================================================
  # Allows caller to override hosts using '-e cmd_hosts='
  hosts: "{{ cmd_hosts | default('openvpn') }}"

  roles:
    - sync_clients


File: /README.md
# ansible-openvpn-mikrotik [![Build Status](https://travis-ci.org/dteslya/ansible-ovpn-mikrotik.svg?branch=master)](https://travis-ci.org/dteslya/ansible-ovpn-mikrotik)

Ansible role and playbooks for installing openvpn and managing clients.

This is a fork of [ansible-openvpn](https://github.com/BastiPaeltz/ansible-openvpn) which in turn is a fork of [ansible-openvpn-hardened](https://github.com/bau-sec/ansible-openvpn-hardened).

Notable changes:
- Support for Mikrotik routers as clients
- Ability to define `client-config-dir` for clients in `group_vars/all.yml`
- Adding clients using a CSR functionality is stripped
- Distro repository is used to install OpenVPN package instead of official OpenVPN repository
- EasyRSA v3.0.6 is used
- Firewall rules are saved using `netfilter-persistent`

Hence Mikrotik RouterOS only supports TCP connection type I define a separate OpenVPN instance with `proto: tcp` and `port: 443`. This instance can also be used by other clients in case of restrictive firewalls on the network.

To further guarantee RouterOS support the following settings are now default:
- `comp-lzo` is disabled
- `cipher AES-128-CBC`
- `auth SHA1`

## Supported Targets

The following Linux distros are tested:

- Ubuntu 18.04
- Ubuntu 16.04

Other distros and versions may work too.

# Quick start

Copy the sample Ansible inventory and variables to edit for your setup. (I will use `my_project` as an example for the rest of this documentation)

    cp -r inventories/sample inventories/my_project

Edit the inventory hosts (`hosts.ini`) to target your desired host. You can also change the [configuration variables](#configuration-variables) in (`group_vars/all.yml`), the defaults are however sufficient for this quickstart example.
It is also possible to [target multiple hosts each using different variables](#targeting-multiple-hosts).

OpenVPN requires some firewall rules to forward packets. By default **NO** firewall rules will be written/altered.  
However you can set `load_iptables_rules` to `true` and a [generated script](./playbooks/roles/openvpn/templates/etc_iptables_rules.v4.j2), that you can find at `/etc/openvpn/openvpn_iptables_rules.sh` on the host (after installation finished) will load the minimum required rules into ip(v4)tables. If you opt to not do this you can set the firewall rules by hand. OpenVPN will need at least the `MASQUERADE` rule from that script to work.

Run the install playbook

    ansible-playbook -i inventories/my_project/hosts.ini playbooks/install.yml

The OpenVPN server is now up and running. Time to add some clients.

## Client state syncing

When you run the `sync_clients.yml` playboook it will sync the desired state (which clients are in the `valid_clients` list, by default "phone" and "laptop") with the current state (which clients are currently valid on the OpenVPN host).  
Clients that are not desired but currently valid will be revoked.  
Clients that are desired but currently not present on the OpenVPN host will be created/added.  
**NOTE**: Once you revoke a client, it is NOT possible to make it valid again, so I suggest using somewhat unique names as `valid_clients`.  

By default once you run the `sync_clients.yml` playbook it will first tell you which clients it will add and revoke before doing it, you will have to manually confirm before it proceeds. You can disable this prompt by setting `prompt_before_syncing_clients` to `false`.

    ansible-playbook playbooks/sync_clients.yml -i inventories/my_project/hosts.ini

After the playbook finished, the credentials will be in the `fetched_creds/` directory after the playbook finished succesfully.  
You'll be prompted for the private key passphrase, this is stored in a file ending in `.txt` in the client directory you just entered in the step above.  
Try connecting to the OpenVPN server:

    cd fetched_creds/[inventory_hostname]/[client name]/
    openvpn [client name]-pki-embedded.ovpn

With the `sync_clients.yml` playbook you can maintain state of your clients, even on different hosts, see [Targeting multiple hosts](#targeting-multiple-hosts) and [State Management](#How-to-manage-state).

## Adding clients manually

To add clients, you can also run the `add_clients.yml` playbook. It needs a list named `clients_to_add`, see [the file used for the tests](./test/ansible-vars/02_add_clients.yml) on how this looks like.

    ansible-playbook playbooks/add_clients.yml -i inventories/my_project/hosts.ini -e "@test/ansible-vars/02_add_clients.yml"

The credentials will be in the `fetched_creds/` directory after the playbook finished succesfully. Try connecting to the OpenVPN server:

    cd fetched_creds/[inventory_hostname]/[client name]/
    openvpn [client name]-pki-embedded.ovpn

You'll be prompted for the private key passphrase, this is stored in a file ending in `.txt` in the client directory you just entered in the step above.

### Distributing key files

Three different OpenVPN configuration files are provided because OpenVPN clients on different platforms have different requirements for how the PKI information is referenced by the .ovpn file. This is just for convenience. All the configuration information and PKI info is the same, it's just formatted differently to support different OpenVPN clients.

- **PKI embedded** - the easiest if your client supports it. Only one file required and all the PKI information is embedded.
  - `XYZ-pki-embedded.ovpn`
- **PKCS#12** - all the PKI information is stored in the PKCS#12 file and referenced by the config. This can be more secure on Android where the OS can store the information in the PKCS#12 file in hardware backed encrypted storage.
  - `XYZ-pkcs.ovpn`
  - `XYZ.p12`
- **PKI files** - if the above two fail, all clients should support this. All of the PKI information is stored in separate files and referenced by the config.
  - `XYZ-pki-files.ovpn` - OpenVPN configuration
  - `ca.pem` - CA certificate
  - `XYZ.key` - client private key
  - `XYZ.pem` - client certificate

All private keys (embedded in config, pkcs, and .key) are encrypted with a passphrase to facilitate secure distribution to client devices.

For maximum security when copying the PKI files and configs to client devices don't copy the .txt file containing the randomly generated passphrase. Enter the passphrase manually onto the device after the key has been transferred.

### Private key passphrases

Entering a pass phrase every time the client is started can be annoying. There are a few options to make this less burdensome after the keys have been securely distributed to the client devices.

1. When starting the client, use `openvpn --config [config] --askpass [pass.txt]` if you don't want to enter the password for the private key

  From the OpenVPN man page:

  > If file is specified, read the password from the first line of file. Keep in mind that storing your password in a file to a certain extent invalidates the extra security provided by using an encrypted key.

### Adding clients using a CSR

Clients can also be added using a certificate signing request, CSR. This is useful if you intend to use keys generated and stored in a TPM. Generating the CSR will depend on your hardware, OS, TPM software, etc. If you're interested in this feature, you can probably figure this out (though [`.travis.yml`](.travis.yml) has an example of generating a CSR with *openssl*). This [blog post](https://qistoph.blogspot.nl/2015/12/tpm-authentication-in-openvpn-and-putty.html) shows how to create private key stored in a TPM and generate a CSR on Windows.

The variable `csr_path` specifies the local path to the CSR. `cn` specifies the common name specified when the CSR was created.

    ansible-playbook -e "csr_path=~/test.csr cn=test@domain.com" playbooks/add_clients.yml

This will generate the client's signed certificate and put it in `fetched_creds/[server ip]/[cn]/` as well as a nearly complete `.ovpn` client configuration file. You'll need to add references to or embed your private key and signed certificate. This will vary based on how your private key is stored. If your following the guide in the blog post mentioned above you'd do this using the OpenVPN option `cryptoapicert`.

## Targeting multiple hosts
It is possible to not only target multiple hosts but also use different groups and apply certain configuration variables to that group only. An example:

Consider this `hosts.ini` inventory:
```
[production]
bastion-prod-us-east-1
bastion-prod-us-east-2

[qa]
bastion-qa

[openvpn:children]
production
qa
```

You can now create a file `production.yml` in `group_vars/`:
```
openvpn_key_country:  "US"
openvpn_key_province: "Ohio"
openvpn_key_city: "Cleveland"
openvpn_key_org: "FOOBAR CORPORATION"
openvpn_key_ou: "Operations"
openvpn_key_email: "foobar@example.com"
```

This configuration will now be applied to hosts in the `production` group only and will override variables from the `all.yml`.  
You can even do this on a per-host level, which will override group-level variables.  
E.g. create a file `host_vars/bastion-prod-us-east-1.yml`:
```
openvpn_key_ou: "Operations Unit B"
```

Further reading: [Ansible variable documentation, especially section: "Precedence"](http://docs.ansible.com/ansible/latest/user_guide/playbooks_variables.html).

This also comes in handy when managing clients with the `sync_clients.yml` playbook because you can then configure which clients are valid on a per-host or per-group basis.

## How to manage state

You can use this to manage state by committing and continously updating configuration, especially for client syncing.
There are different approaches you can take, here are two suggestions:  
- Manage all configuration files (all `inventories/` files) on a separate location, e.g. inside of [Jenkins](https://wiki.jenkins.io/display/JENKINS/Config+File+Provider+Plugin) and once these change, trigger a run of the playbook(s), especially `sync_clients.yml`. Disadvantage: You can not easily run this from anywhere else since the configuration files are missing.
- Encrypt all configuration files (e.g. using `ansible-vault`), commit them to source control and trigger a run of the playbook(s) after a new commit is pushed.

## Revoke client access manually

To revoke clients access, you can run the `revoke_clients.yml` playbook. It needs a list named `clients_to_revoke`, see [the file used for the tests](./test/ansible-vars/03_revoke_clients.yml) on how this looks like.

    ansible-playbook playbooks/revoke_clients.yml -e "@test/ansible-vars/03_revoke_clients.yml"

# Managing the OpenVPN server

## Configuration variables

There is documentation on the most important variables in [all.yml](./inventories/sample/group_vars/all.yml).

### OpenVPN server configuration
For the full server configuration, see [`etc_openvpn_server.conf.j2`](playbooks/roles/openvpn/templates/etc_openvpn_server.conf.j2)
- `tls-auth` aids in mitigating risk of denial-of-service attacks. Additionally, when combined with usage of UDP at the transport layer (the default configuration used by *ansible-openvpn-hardened*), it complicates attempts to port scan the OpenVPN server because any unsigned packets can be immediately dropped without sending anything back to the scanner.
  - From the [OpenVPN hardening guide](https://community.openvpn.net/openvpn/wiki/Hardening):

    > The tls-auth option uses a static pre-shared key (PSK) that must be generated in advance and shared among all peers. This features adds "extra protection" to the TLS channel by requiring that incoming packets have a valid signature generated using the PSK key... The primary benefit is that an unauthenticated client cannot cause the same CPU/crypto load against a server as the junk traffic can be dropped much sooner. This can aid in mitigating denial-of-service attempts.

- `push block-outside-dns` used by OpenVPN server to fix a potential dns leak on Windows 10
  - See https://community.openvpn.net/openvpn/ticket/605
- `tls-cipher` limits allowable TLS ciphers to a subset that supports [**perfect forward secrecy**](https://en.wikipedia.org/wiki/Forward_secrecy)
  - From wikipedia:

	> Forward secrecy protects past sessions against future compromises of secret keys or passwords. If forward secrecy is used, encrypted communications and sessions recorded in the past cannot be retrieved and decrypted should long-term secret keys or passwords be compromised in the future, even if the adversary actively interfered.

- `cipher` set to `AES-256-CBC` by default
- `2048` bit RSA key size by default.
  - This can be increased to `4096` by changing `openvpn_key_size` in [`defaults/main.yml`](playbooks/roles/openvpn/defaults/main.yml) if you don't mind extra processing time. Consensus seems to be that 2048 is sufficient for all but the most sensitive data.

### OpenVPN client configuration
For the full client configuration, see [`client_common.ovpn.j2`](playbooks/roles/add_clients/templates/client_common.ovpn.j2)
- `verify-x509-name` prevents MitM attacks by verifying the server name in the supplied certificate matches the clients configuration.
- `persist-tun` prevents the traffic from leaking out over the default interface during interruptions and reconnection attempts by keeping the tun device up until connectivity is restored.

### PKI
- [easy-rsa](https://github.com/OpenVPN/easy-rsa) is used to manage the public key infrastructure.
- OpenVPN is configured to read the CRL generated by *easy-rsa* so that a single client's access can be revoked without having to reissue credentials to all of the clients.
- The private keys generated for the clients and CA are all protected with a randomly generated passphrase to facilitate secure distribution to client devices.

### Firewall

OpenVPN requires some firewall rules to forward packets.  
By default **NO** firewall rules will be written/altered.  
However you can set `load_iptables_rules` to `true` and a [generated script](./playbooks/roles/openvpn/templates/etc_iptables_rules.v4.j2), that you can find at `/etc/openvpn/openvpn_iptables_rules.sh` on the host (after installation finished) will load the minimum required rules into ip(v4)tables. If you opt to not do this you can set the firewall rules by hand. OpenVPN will need at least the `MASQUERADE` rule from that script.

### Credentials (CA password)

Credentials are generated during the install process and are saved as yml formatted files in the Ansible file hierarchy so they can be used without requiring the playbook caller to take any action. The locations are below.

- CA Private key passphrase - saved in `inventories/my_project/host_vars/[inventory_hostname].yml`


File: /test\ansible-vars\01_install_centos.yml
load_iptables_rules: True

openvpn_instances:
  - {
      proto: udp,
      port: 1194,
      mask: "10.9.0.0 255.255.255.0",
      cidr: "10.9.0.0/24",
      server_extra_options: ['push "route 10.10.0.0 255.255.255.0"'],
      client_extra_options: [],
  }
  - {
      proto: tcp,
      port: 443,
      mask: "10.8.0.0 255.255.255.0",
      cidr: "10.8.0.0/24",
      server_extra_options: ['push "redirect-gateway def1"'],
      client_extra_options: [],
  }


File: /test\ansible-vars\01_install_debian.yml
easyrsa_dn_mode_cn_only: True
openvpn_server_common_name_manual: "Company Foo Ltd.test"

openvpn_instances:
  - {
      proto: udp,
      port: 1194,
      mask: "10.9.0.0 255.255.255.0",
      cidr: "10.9.0.0/24",
      server_extra_options: ['push "route 10.10.0.0 255.255.255.0"'],
      client_extra_options: [],
  }

File: /test\ansible-vars\01_install_ubuntu.yml
---
load_iptables_rules: False

File: /test\ansible-vars\02_add_clients.yml
clients_to_add:
- "testuser1@{{openvpn_server_common_name}}"
- testuser2_will_be_revoked
- testuser3_will_be_revoked
- testuser4_will_be_revoked_by_sync
- "testuser5 with spaces"

File: /test\ansible-vars\03_revoke_clients.yml
clients_to_revoke:
- testuser2_will_be_revoked
- testuser3_will_be_revoked

File: /test\ansible-vars\04_sync_clients.yml
valid_clients:
- name: "testuser1@{{openvpn_server_common_name}}"
- name: testuser1
- name: testuser5

prompt_before_syncing_clients: False

File: /test\docker-inventory
[localhost]
127.0.0.1 ansible_python_interpreter=python

[openvpn]


File: /test\docker-setup.sh
#!/bin/bash

set -eo pipefail

if  [ ! -z ${docker_build_image} ]
then
  docker build --rm=true --file=test/Dockerfile.${distribution}-${version} --tag=${distribution}-${version}:ansible .
fi

for ((i=1; i<=${docker_concurrent_containers}; i++))
do
    # Run the container
    container_id=$(docker run ${run_opts} ${distribution}-${version}:ansible "${init}")
    container_ip=$(docker inspect --format '{{ .NetworkSettings.IPAddress }}' ${container_id})
    docker ps

    # Get the IP of the container and add it to the inventory
    echo "$(echo ${container_id} | cut -c1-13) ansible_host=${container_ip} ansible_user=docker ansible_become=yes ansible_become_pass=password" >> test/docker-inventory
done

File: /test\Dockerfile.centos-7
FROM centos:centos7
ENV container docker

RUN yum -y update; yum clean all

RUN yum -y swap -- remove systemd-container systemd-container-libs -- install systemd systemd-libs

RUN systemctl mask dev-mqueue.mount dev-hugepages.mount \
    systemd-remount-fs.service sys-kernel-config.mount \
    sys-kernel-debug.mount sys-fs-fuse-connections.mount \
    display-manager.service graphical.target systemd-logind.service

RUN yum -y install openssh-server sudo openssh-clients
RUN ssh-keygen -q -f /etc/ssh/ssh_host_rsa_key -N '' -t rsa && \
    ssh-keygen -q -f /etc/ssh/ssh_host_ecdsa_key -N '' -t ecdsa && \
    ssh-keygen -q -f /etc/ssh/ssh_host_ed25519_key -N '' -t ed25519

RUN useradd -m -G wheel -s /bin/bash docker
RUN echo 'docker:password' | chpasswd

RUN mkdir /home/docker/.ssh
ADD test/id_rsa.pub /home/docker/.ssh/authorized_keys
RUN chown -R docker:docker /home/docker/.ssh/
RUN chmod 701 /home/docker
RUN chmod 700 /home/docker/.ssh
RUN chmod 600 /home/docker/.ssh/authorized_keys

RUN bash -c 'echo "Defaults:docker !requiretty" | (EDITOR="tee -a" visudo)'
RUN cat /etc/sudoers

RUN systemctl enable sshd.service

VOLUME [ "/sys/fs/cgroup" ]
VOLUME ["/run"]

EXPOSE 22

CMD ["/usr/sbin/init"]


File: /test\Dockerfile.debian-8.7
FROM debian:8.7
ENV container docker

RUN apt-get update; apt-get -y upgrade

RUN DEBIAN_FRONTEND=noninteractive apt-get -q -y install systemd openssh-server sudo openssh-client

RUN systemctl mask dev-mqueue.mount dev-hugepages.mount \
    sys-kernel-debug.mount sys-fs-fuse-connections.mount \
    display-manager.service graphical.target systemd-logind.service

RUN useradd -m -G sudo -s /bin/bash docker
RUN echo 'docker:password' | chpasswd

RUN mkdir /home/docker/.ssh
ADD test/id_rsa.pub /home/docker/.ssh/authorized_keys
RUN chown -R docker:docker /home/docker/.ssh/
RUN chmod 701 /home/docker
RUN chmod 700 /home/docker/.ssh
RUN chmod 600 /home/docker/.ssh/authorized_keys

VOLUME [ "/sys/fs/cgroup" ]
VOLUME ["/run"]

EXPOSE 22

CMD ["/bin/systemd"]


File: /test\Dockerfile.ubuntu-16.04
FROM ubuntu:16.04
ENV container docker

RUN apt-get update; apt-get -y upgrade

RUN DEBIAN_FRONTEND=noninteractive apt-get -q -y install systemd dbus openssh-server sudo openssh-client locales

# Uncomment to speed up local tests by pre-installing most required packages
#RUN DEBIAN_FRONTEND=noninteractive apt-get -q -y install aptitude iptables-persistent apt-transport-https ca-certificates python-software-properties unattended-upgrades debsums debsecan apt-listchanges libpam-pwquality aide-common
#RUN DEBIAN_FRONTEND=noninteractive apt-get -q -y install sudo python-pip python-virtualenv git gnupg iptables aide openssl dnsmasq auditd

RUN systemctl mask dev-mqueue.mount dev-hugepages.mount \
    sys-kernel-debug.mount sys-fs-fuse-connections.mount \
    display-manager.service graphical.target systemd-logind.service

RUN useradd -m -G sudo -s /bin/bash docker
RUN echo 'docker:password' | chpasswd

RUN mkdir /home/docker/.ssh
ADD test/id_rsa.pub /home/docker/.ssh/authorized_keys
RUN chown -R docker:docker /home/docker/.ssh/
RUN chmod 701 /home/docker
RUN chmod 700 /home/docker/.ssh
RUN chmod 600 /home/docker/.ssh/authorized_keys

RUN systemctl enable ssh.service

VOLUME [ "/sys/fs/cgroup" ]
VOLUME ["/run"]

EXPOSE 22

RUN locale-gen en_US.UTF-8
ENV LANG en_US.UTF-8
ENV LANGUAGE en_US:en
ENV LC_ALL en_US.UTF-8

CMD ["/bin/systemd"]


File: /TODO.md
- add Mikrotik setup instructions

