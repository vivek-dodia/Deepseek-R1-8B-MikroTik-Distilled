# Repository Information
Name: Mikrotik-Script-Framework

# Directory Structure
Directory structure:
└── github_repos/Mikrotik-Script-Framework/
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
    │   │       ├── pack-f552af2a359fc68d9253ceda274f6aee4338ae8e.idx
    │   │       └── pack-f552af2a359fc68d9253ceda274f6aee4338ae8e.pack
    │   ├── packed-refs
    │   └── refs/
    │       ├── heads/
    │       │   └── main
    │       ├── remotes/
    │       │   └── origin/
    │       │       └── HEAD
    │       └── tags/
    ├── .gitattributes
    ├── DEVELOPMENT
    ├── LICENSE
    ├── README.md
    ├── releases/
    │   ├── release 1.0 stable.zip
    │   └── release 2.0 stable.zip
    └── sources/
        ├── config/
        │   ├── config-hardening.rsc
        │   ├── default.rsc
        │   ├── dns-over-https.rsc
        │   ├── firewall nat ntp.rsc
        │   ├── firewall rules.rsc
        │   ├── opendns firewall rules to resolvePublicIP.rsc
        │   ├── ovpn/
        │   │   └── certificateca.rsc
        │   ├── router pcc dinamico.rsc
        │   └── router-wan-lan.rsc
        ├── config-init.rsc
        ├── config-module-dyndns.rsc
        ├── config-module-pcc-init.rsc
        ├── default.rsc
        ├── dns-dos.rsc
        ├── geoip.rsc
        ├── init.rsc
        ├── lure-firewall/
        │   ├── lure-firewall-filter.rsc
        │   ├── lure-geoip.rsc
        │   ├── lure-services.rsc
        │   ├── lureinputfilter - copia - copia.rsc
        │   └── lureinputfilter - copia.rsc
        ├── module-arrays.rsc
        ├── module-base32.rsc
        ├── module-bin.rsc
        ├── module-dyndns.rsc
        ├── module-functions.rsc
        ├── module-geoip.rsc
        ├── module-hex.rsc
        ├── module-hmac.rsc
        ├── module-json.rsc
        ├── module-pcc-init.rsc
        ├── module-services - copia.rsc
        ├── module-sha1.rsc
        ├── module-time.rsc
        ├── module-totp.rsc
        ├── msf-install.rsc
        ├── script-dyndns.rsc
        ├── script-ovpn-dalejos.rsc
        ├── script-pcc-qos-wan.rsc
        ├── spamhaus.rsc
        ├── templates/
        │   ├── template-config.rsc
        │   ├── template-module.rsc
        │   ├── template-script.rsc
        │   └── template-tool.rsc
        ├── tool/
        │   ├── api-rest/
        │   │   └── api-rest.rsc
        │   ├── dhcp/
        │   │   ├── client/
        │   │   │   ├── dhcp-client-route.rsc
        │   │   │   └── dhcp-client.rsc
        │   │   └── server/
        │   │       ├── config-dhcp-lease.rsc
        │   │       ├── dhcp-lease-script.rsc
        │   │       ├── dhcp-lease-server.rsc
        │   │       ├── module-functions.rsc
        │   │       ├── readme.txt
        │   │       └── server.zip
        │   ├── icmp/
        │   │   └── flood-ping-latency.rsc
        │   ├── json/
        │   │   ├── json.rsc
        │   │   ├── mod-json.rsc
        │   │   └── module-json.rsc
        │   ├── monitor/
        │   │   ├── config-monitor-traffic.rsc
        │   │   ├── monitor-traffic-dev.rsc
        │   │   ├── monitor-traffic.rsc
        │   │   └── readme-monitor.txt
        │   ├── monitor 2.zip
        │   ├── monitor.zip
        │   ├── others/
        │   │   ├── config-module.rsc
        │   │   ├── create-address-list.rsc
        │   │   ├── dhcp-client.rsc
        │   │   ├── dhcp-server.rsc
        │   │   ├── hex.rsc
        │   │   └── read.rsc
        │   ├── romon/
        │   │   ├── config-romon.rsc
        │   │   ├── module-romon.rsc
        │   │   ├── module-var.rsc
        │   │   └── vtp/
        │   │       ├── config-romon.rsc
        │   │       ├── config-vtp.rsc
        │   │       ├── module-vtp-client.rsc
        │   │       └── module-vtp.rsc
        │   ├── switch/
        │   │   └── mac-search.rsc
        │   ├── telegram/
        │   │   ├── config-module-telegram.rsc
        │   │   ├── config-script-telegram-active-users.rsc
        │   │   ├── config-script-telegram-log.rsc
        │   │   ├── config-script-telegram-routes.rsc
        │   │   ├── module-telegram.rsc
        │   │   ├── script-telegram-active-users.rsc
        │   │   ├── script-telegram-log.rsc
        │   │   ├── script-telegram-response.rsc
        │   │   └── script-telegram-routes.rsc
        │   └── voltage/
        │       └── script-voltage.rsc
        ├── tool-module-status.rsc
        └── tool-script-status.rsc


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
	url = https://github.com/dalejos/Mikrotik-Script-Framework.git
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
0000000000000000000000000000000000000000 a8aee94f9f3ff2cce6a8f8734336a21b2087ee3e vivek-dodia <vivek.dodia@icloud.com> 1738606092 -0500	clone: from https://github.com/dalejos/Mikrotik-Script-Framework.git


File: /.git\logs\refs\heads\main
0000000000000000000000000000000000000000 a8aee94f9f3ff2cce6a8f8734336a21b2087ee3e vivek-dodia <vivek.dodia@icloud.com> 1738606092 -0500	clone: from https://github.com/dalejos/Mikrotik-Script-Framework.git


File: /.git\logs\refs\remotes\origin\HEAD
0000000000000000000000000000000000000000 a8aee94f9f3ff2cce6a8f8734336a21b2087ee3e vivek-dodia <vivek.dodia@icloud.com> 1738606092 -0500	clone: from https://github.com/dalejos/Mikrotik-Script-Framework.git


File: /.git\packed-refs
# pack-refs with: peeled fully-peeled sorted 
ffc75bf1b60fa579787914e57d0cc73d9b857e44 refs/remotes/origin/development-v7
a8aee94f9f3ff2cce6a8f8734336a21b2087ee3e refs/remotes/origin/main


File: /.git\refs\heads\main
a8aee94f9f3ff2cce6a8f8734336a21b2087ee3e


File: /.git\refs\remotes\origin\HEAD
ref: refs/remotes/origin/main


File: /.gitattributes
# Auto detect text files and perform LF normalization
* text=auto

File: /LICENSE
                                 Apache License
                           Version 2.0, January 2004
                        http://www.apache.org/licenses/

   TERMS AND CONDITIONS FOR USE, REPRODUCTION, AND DISTRIBUTION

   1. Definitions.

      "License" shall mean the terms and conditions for use, reproduction,
      and distribution as defined by Sections 1 through 9 of this document.

      "Licensor" shall mean the copyright owner or entity authorized by
      the copyright owner that is granting the License.

      "Legal Entity" shall mean the union of the acting entity and all
      other entities that control, are controlled by, or are under common
      control with that entity. For the purposes of this definition,
      "control" means (i) the power, direct or indirect, to cause the
      direction or management of such entity, whether by contract or
      otherwise, or (ii) ownership of fifty percent (50%) or more of the
      outstanding shares, or (iii) beneficial ownership of such entity.

      "You" (or "Your") shall mean an individual or Legal Entity
      exercising permissions granted by this License.

      "Source" form shall mean the preferred form for making modifications,
      including but not limited to software source code, documentation
      source, and configuration files.

      "Object" form shall mean any form resulting from mechanical
      transformation or translation of a Source form, including but
      not limited to compiled object code, generated documentation,
      and conversions to other media types.

      "Work" shall mean the work of authorship, whether in Source or
      Object form, made available under the License, as indicated by a
      copyright notice that is included in or attached to the work
      (an example is provided in the Appendix below).

      "Derivative Works" shall mean any work, whether in Source or Object
      form, that is based on (or derived from) the Work and for which the
      editorial revisions, annotations, elaborations, or other modifications
      represent, as a whole, an original work of authorship. For the purposes
      of this License, Derivative Works shall not include works that remain
      separable from, or merely link (or bind by name) to the interfaces of,
      the Work and Derivative Works thereof.

      "Contribution" shall mean any work of authorship, including
      the original version of the Work and any modifications or additions
      to that Work or Derivative Works thereof, that is intentionally
      submitted to Licensor for inclusion in the Work by the copyright owner
      or by an individual or Legal Entity authorized to submit on behalf of
      the copyright owner. For the purposes of this definition, "submitted"
      means any form of electronic, verbal, or written communication sent
      to the Licensor or its representatives, including but not limited to
      communication on electronic mailing lists, source code control systems,
      and issue tracking systems that are managed by, or on behalf of, the
      Licensor for the purpose of discussing and improving the Work, but
      excluding communication that is conspicuously marked or otherwise
      designated in writing by the copyright owner as "Not a Contribution."

      "Contributor" shall mean Licensor and any individual or Legal Entity
      on behalf of whom a Contribution has been received by Licensor and
      subsequently incorporated within the Work.

   2. Grant of Copyright License. Subject to the terms and conditions of
      this License, each Contributor hereby grants to You a perpetual,
      worldwide, non-exclusive, no-charge, royalty-free, irrevocable
      copyright license to reproduce, prepare Derivative Works of,
      publicly display, publicly perform, sublicense, and distribute the
      Work and such Derivative Works in Source or Object form.

   3. Grant of Patent License. Subject to the terms and conditions of
      this License, each Contributor hereby grants to You a perpetual,
      worldwide, non-exclusive, no-charge, royalty-free, irrevocable
      (except as stated in this section) patent license to make, have made,
      use, offer to sell, sell, import, and otherwise transfer the Work,
      where such license applies only to those patent claims licensable
      by such Contributor that are necessarily infringed by their
      Contribution(s) alone or by combination of their Contribution(s)
      with the Work to which such Contribution(s) was submitted. If You
      institute patent litigation against any entity (including a
      cross-claim or counterclaim in a lawsuit) alleging that the Work
      or a Contribution incorporated within the Work constitutes direct
      or contributory patent infringement, then any patent licenses
      granted to You under this License for that Work shall terminate
      as of the date such litigation is filed.

   4. Redistribution. You may reproduce and distribute copies of the
      Work or Derivative Works thereof in any medium, with or without
      modifications, and in Source or Object form, provided that You
      meet the following conditions:

      (a) You must give any other recipients of the Work or
          Derivative Works a copy of this License; and

      (b) You must cause any modified files to carry prominent notices
          stating that You changed the files; and

      (c) You must retain, in the Source form of any Derivative Works
          that You distribute, all copyright, patent, trademark, and
          attribution notices from the Source form of the Work,
          excluding those notices that do not pertain to any part of
          the Derivative Works; and

      (d) If the Work includes a "NOTICE" text file as part of its
          distribution, then any Derivative Works that You distribute must
          include a readable copy of the attribution notices contained
          within such NOTICE file, excluding those notices that do not
          pertain to any part of the Derivative Works, in at least one
          of the following places: within a NOTICE text file distributed
          as part of the Derivative Works; within the Source form or
          documentation, if provided along with the Derivative Works; or,
          within a display generated by the Derivative Works, if and
          wherever such third-party notices normally appear. The contents
          of the NOTICE file are for informational purposes only and
          do not modify the License. You may add Your own attribution
          notices within Derivative Works that You distribute, alongside
          or as an addendum to the NOTICE text from the Work, provided
          that such additional attribution notices cannot be construed
          as modifying the License.

      You may add Your own copyright statement to Your modifications and
      may provide additional or different license terms and conditions
      for use, reproduction, or distribution of Your modifications, or
      for any such Derivative Works as a whole, provided Your use,
      reproduction, and distribution of the Work otherwise complies with
      the conditions stated in this License.

   5. Submission of Contributions. Unless You explicitly state otherwise,
      any Contribution intentionally submitted for inclusion in the Work
      by You to the Licensor shall be under the terms and conditions of
      this License, without any additional terms or conditions.
      Notwithstanding the above, nothing herein shall supersede or modify
      the terms of any separate license agreement you may have executed
      with Licensor regarding such Contributions.

   6. Trademarks. This License does not grant permission to use the trade
      names, trademarks, service marks, or product names of the Licensor,
      except as required for reasonable and customary use in describing the
      origin of the Work and reproducing the content of the NOTICE file.

   7. Disclaimer of Warranty. Unless required by applicable law or
      agreed to in writing, Licensor provides the Work (and each
      Contributor provides its Contributions) on an "AS IS" BASIS,
      WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
      implied, including, without limitation, any warranties or conditions
      of TITLE, NON-INFRINGEMENT, MERCHANTABILITY, or FITNESS FOR A
      PARTICULAR PURPOSE. You are solely responsible for determining the
      appropriateness of using or redistributing the Work and assume any
      risks associated with Your exercise of permissions under this License.

   8. Limitation of Liability. In no event and under no legal theory,
      whether in tort (including negligence), contract, or otherwise,
      unless required by applicable law (such as deliberate and grossly
      negligent acts) or agreed to in writing, shall any Contributor be
      liable to You for damages, including any direct, indirect, special,
      incidental, or consequential damages of any character arising as a
      result of this License or out of the use or inability to use the
      Work (including but not limited to damages for loss of goodwill,
      work stoppage, computer failure or malfunction, or any and all
      other commercial damages or losses), even if such Contributor
      has been advised of the possibility of such damages.

   9. Accepting Warranty or Additional Liability. While redistributing
      the Work or Derivative Works thereof, You may choose to offer,
      and charge a fee for, acceptance of support, warranty, indemnity,
      or other liability obligations and/or rights consistent with this
      License. However, in accepting such obligations, You may act only
      on Your own behalf and on Your sole responsibility, not on behalf
      of any other Contributor, and only if You agree to indemnify,
      defend, and hold each Contributor harmless for any liability
      incurred by, or claims asserted against, such Contributor by reason
      of your accepting any such warranty or additional liability.

   END OF TERMS AND CONDITIONS

   APPENDIX: How to apply the Apache License to your work.

      To apply the Apache License to your work, attach the following
      boilerplate notice, with the fields enclosed by brackets "[]"
      replaced with your own identifying information. (Don't include
      the brackets!)  The text should be enclosed in the appropriate
      comment syntax for the file format. We also recommend that a
      file or class name and description of purpose be included on the
      same "printed page" as the copyright notice for easier
      identification within third-party archives.

   Copyright [yyyy] [name of copyright owner]

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.


File: /README.md
# Mikrotik Script Framework
Development version 3.0 alpha

## Support on Beerpay
Hey dude! Help me out for a couple of :beers:!

[![Beerpay](https://beerpay.io/dalejos/Mikrotik-Script-Framework/badge.svg?style=beer-square)](https://beerpay.io/dalejos/Mikrotik-Script-Framework)  [![Beerpay](https://beerpay.io/dalejos/Mikrotik-Script-Framework/make-wish.svg?style=flat-square)](https://beerpay.io/dalejos/Mikrotik-Script-Framework?focus=wish)

File: /sources\config\config-hardening.rsc
#IP Services

:local services {\
    "api"={\
        "disabled"=true;\
        "port"=8728;\
        "address"="";\
        "certificate"="none"};\
    "api-ssl"={\
        "disabled"=true;\
        "port"=8729;\
        "address"="";\
        "certificate"="none"};\
    "ftp"={\
        "disabled"=true;\
        "port"=21;\
        "address"="";\
        "certificate"="none"};\
    "ssh"={\
        "disabled"=true;\
        "port"=22;\
        "address"="";\
        "certificate"="none"};\
    "telnet"={\
        "disabled"=true;\
        "port"=23;\
        "address"="";\
        "certificate"="none"};\
    "winbox"={\
        "disabled"=false;\
        "port"=8291;\
        "address"="";\
        "certificate"="none"};\
    "www"={\
        "disabled"=true;\
        "port"=80;\
        "address"="";\
        "certificate"="none"};\
    "www-ssl"={\
        "disabled"=true;\
        "port"=443;\
        "address"="";\
        "certificate"="none"}\
};

:foreach service,properties in=$services do={
    :put "name: $service";
    :put "disabled: $($properties->"disabled")";
    :put "port: $($properties->"port")";
    :put "address: $($properties->"address")";
    :put "certificate: $($properties->"certificate")";
    :put "";
    /ip service set $service disabled=($properties->"disabled") port=($properties->"port") address=($properties->"address") certificate=($properties->"certificate");
}

#IP Neighbor
:local neighborInterfaceList "none";
/ip neighbor discovery-settings set discover-interface-list=$neighborInterfaceList;

#IP Proxy
:local proxyEnabled false;
/ip proxy set enabled=$proxyEnabled;

#IP Socks
:local socksEnabled false;
/ip socks set enabled=$socksEnabled;

#IP Upnp
:local upnpEnabled false;
/ip upnp set enabled=$upnpEnabled;

#IP Cloud
:local ddnsEnabled false;
:local updateTime false;
/ip cloud set ddns-enabled=$ddnsEnabled update-time=$updateTime;

#IP SMB
:local smbEnabled false;
/ip smb set enabled=$smbEnabled;

#IP SSH
:if (!($services->"ssh"->"disabled")) do={
    :local strongCrypto true;
    /ip ssh set strong-crypto=$strongCrypto;
}


#Tool Romon
:local enabledRomon false;
/tool romon set enabled=$enabledRomon;

#Mac Server
:local macServerInterfaceList "none";
:local macWinboxInterfaceList "none";
:local macPingEnabled false;
/tool mac-server set allowed-interface-list=$macServerInterfaceList;
/tool mac-server mac-winbox set allowed-interface-list=$macWinboxInterfaceList;
/tool mac-server ping set enabled=$macPingEnabled;

#Bandwidth Server
:local bandwidthServerEnabled false;
/tool bandwidth-server set enabled=$bandwidthServerEnabled;

#DNS Server
:local allowRemoteRequests true;
/ip dns set allow-remote-requests=$allowRemoteRequests;



File: /sources\config\default.rsc
#| RouterMode:
#|  * WAN port is protected by firewall and enabled DHCP client
#|  * Ethernet interfaces (except WAN port ether1) are part of LAN bridge
#| LAN Configuration:
#|     IP address 192.168.88.1/24 is set on bridge (LAN port)
#|     DHCP Server: enabled;
#| WAN (gateway) Configuration:
#|     gateway:  ether1 ;
#|     ip4 firewall:  enabled;
#|     NAT:   enabled;
#|     DHCP Client: enabled;
#|     DNS: enabled;

:log info Starting_defconf_script_;
#-------------------------------------------------------------------------------
# Apply configuration.
# these commands are executed after installation or configuration reset
#-------------------------------------------------------------------------------
:if ($action = "apply") do={
# wait for interfaces
:local count 0; 
:while ([/interface ethernet find] = "") do={ 
:if ($count = 30) do={
:log warning "DefConf: Unable to find ethernet interfaces";
/quit;
}
:delay 1s; :set count ($count +1); 
};

 /interface list add name=WAN comment="defconf"
 /interface list add name=LAN comment="defconf"
 /interface bridge
   add name=bridge disabled=no auto-mac=yes protocol-mode=rstp comment=defconf;
 :local bMACIsSet 0;
 :foreach k in=[/interface find where !(slave=yes  || name~"ether1" || name~"bridge")] do={
   :local tmpPortName [/interface get $k name];
   :log info "port: $tmpPortName"
   :if ($bMACIsSet = 0) do={
     :if ([/interface get $k type] = "ether") do={
       /interface bridge set "bridge" auto-mac=no admin-mac=[/interface ethernet get $tmpPortName mac-address];
       :set bMACIsSet 1;
     }
   }
   /interface bridge port
     add bridge=bridge interface=$tmpPortName comment=defconf;
 }
   /ip pool add name="default-dhcp" ranges=192.168.88.10-192.168.88.254;
   /ip dhcp-server
     add name=defconf address-pool="default-dhcp" interface=bridge lease-time=10m disabled=no;
   /ip dhcp-server network
     add address=192.168.88.0/24 gateway=192.168.88.1 comment="defconf";
  /ip address add address=192.168.88.1/24 interface=bridge comment="defconf";
   /ip dhcp-client add interface=ether1 disabled=no comment="defconf";
 /interface list member add list=LAN interface=bridge comment="defconf"
 /interface list member add list=WAN interface=ether1 comment="defconf"
 /ip firewall nat add chain=srcnat out-interface-list=WAN ipsec-policy=out,none action=masquerade comment="defconf: masquerade"
 /ip firewall {
   filter add chain=input action=accept connection-state=established,related,untracked comment="defconf: accept established,related,untracked"
   filter add chain=input action=drop connection-state=invalid comment="defconf: drop invalid"
   filter add chain=input action=accept protocol=icmp comment="defconf: accept ICMP"
   filter add chain=input action=drop in-interface-list=!LAN comment="defconf: drop all not coming from LAN"
   filter add chain=forward action=accept ipsec-policy=in,ipsec comment="defconf: accept in ipsec policy"
   filter add chain=forward action=accept ipsec-policy=out,ipsec comment="defconf: accept out ipsec policy"
   filter add chain=forward action=fasttrack-connection connection-state=established,related comment="defconf: fasttrack"
   filter add chain=forward action=accept connection-state=established,related,untracked comment="defconf: accept established,related, untracked"
   filter add chain=forward action=drop connection-state=invalid comment="defconf: drop invalid"
   filter add chain=forward action=drop connection-state=new connection-nat-state=!dstnat in-interface-list=WAN comment="defconf:  drop all from WAN not DSTNATed"
 }
   /ip neighbor discovery-settings set discover-interface-list=LAN
   /tool mac-server set allowed-interface-list=LAN
   /tool mac-server mac-winbox set allowed-interface-list=LAN
 /ip dns {
     set allow-remote-requests=yes
     static add name=router.lan address=192.168.88.1
 }

}
#-------------------------------------------------------------------------------
# Revert configuration.
# these commands are executed if user requests to remove default configuration
#-------------------------------------------------------------------------------
:if ($action = "revert") do={
/user set admin password=""
 /system routerboard mode-button set enabled=no
 /system routerboard mode-button set on-event=""
 /system script remove [find comment~"defconf"]
 /ip firewall filter remove [find comment~"defconf"]
 /ip firewall nat remove [find comment~"defconf"]
 /interface list member remove [find comment~"defconf"]
 /interface detect-internet set detect-interface-list=none
 /interface detect-internet set lan-interface-list=none
 /interface detect-internet set wan-interface-list=none
 /interface detect-internet set internet-interface-list=none
 /interface list remove [find comment~"defconf"]
 /tool mac-server set allowed-interface-list=all
 /tool mac-server mac-winbox set allowed-interface-list=all
 /ip neighbor discovery-settings set discover-interface-list=!dynamic
   :local o [/ip dhcp-server network find comment="defconf"]
   :if ([:len $o] != 0) do={ /ip dhcp-server network remove $o }
   :local o [/ip dhcp-server find name="defconf" !disabled]
   :if ([:len $o] != 0) do={ /ip dhcp-server remove $o }
   /ip pool {
     :local o [find name="default-dhcp" ranges=192.168.88.10-192.168.88.254]
     :if ([:len $o] != 0) do={ remove $o }
   }
   :local o [/ip dhcp-client find comment="defconf"]
   :if ([:len $o] != 0) do={ /ip dhcp-client remove $o }
 /ip dns {
   set allow-remote-requests=no
   :local o [static find name=router.lan address=192.168.88.1]
   :if ([:len $o] != 0) do={ static remove $o }
 }
 /ip address {
   :local o [find comment="defconf"]
   :if ([:len $o] != 0) do={ remove $o }
 }
 :foreach iface in=[/interface ethernet find] do={
   /interface ethernet set $iface name=[get $iface default-name]
 }
 /interface bridge port remove [find comment="defconf"]
 /interface bridge remove [find comment="defconf"]
}
:log info Defconf_script_finished;



File: /sources\config\dns-over-https.rsc

{
    :local body "";
    :foreach int in=[/log find] do={
        :local logItem [/log get $int];
        :set body ("$body\r\n" . ($logItem->"message"));
        :set body ("$body\r\n" . ($logItem->"time"));
    }

    :put $body;
}


{
    :local message "";
    :foreach id in=[/log find] do={
        :local logItem [/log get $id];
        :foreach k,v in=$logItem do={
            :if ($k!=".id") do={
                :set message "$message $v";
            }
        }
        :set message "$message\r\n";
    }
    :put $message;
}

{
    :local body "";
    :foreach id in=[/log find] do={
        :local logItem [/log get $id];
        :foreach k,v in=$logItem do={
            :set body "$body $v";
        }
        :set body "$body\r\n";
    }
    :put $body;
}

        :foreach k,v in=[/log get $id] do={
            :set body ($body . $v);
        }
        :set body "$body\r\n";








# jul/17/2020 19:38:00 by RouterOS 6.48beta12
# software id = 3615-9B9N
#
# model = RouterBOARD SXTsq G-5acD
# serial number = 819307718685
/ip dns
set use-doh-server=
    
/ip dns static
add address= name= type=A
add address= name= type=A
add address= name= type=AAAA
add address= name= type=AAAA

#Alibaba Public DNS
#DoH/DoT/DNS Json API, Best DoH server in China

/ip dns
set use-doh-server=https://dns.alidns.com/dns-query

/ip dns static
add address=223.6.6.6 name=dns.alidns.com type=A
add address=223.5.5.5 name=dns.alidns.com type=A
add address=2400:3200::1 name=dns.alidns.com type=AAAA
add address=2400:3200:baba::1 name=dns.alidns.com type=AAAA
          
#AdGuard
#Default provides ad-blocking at DNS level, while Family protection adds adult site blocking
/ip dns
set use-doh-server=https://dns.adguard.com/dns-query
    
/ip dns static
add address=176.103.130.130 name=dns.adguard.com type=A
add address=176.103.130.131 name=dns.adguard.com type=A
add address=2a00:5a60::ad2:ff name=dns.adguard.com type=AAAA
add address=2a00:5a60::ad1:ff name=dns.adguard.com type=AAAA

#AdGuard Family
/ip dns
set use-doh-server=https://dns-family.adguard.com/dns-query
    
/ip dns static
add address= name=dns-family.adguard.com type=A
add address= name=dns-family.adguard.com type=A
add address=2a00:5a60::bad2:ff name=dns-family.adguard.com type=AAAA
add address=2a00:5a60::bad1:ff name=dns-family.adguard.com type=AAAA

#Google
#Full RFC 8484 support
/ip dns
set use-doh-server=https://dns.google/dns-query

/ip dns static
add address=8.8.8.8 name=dns.google type=A
add address=8.8.4.4 name=dns.google type=A

#Google DNS64
/ip dns
set use-doh-server=https://dns64.dns.google/dns-query

/ip dns static
add address=2001:4860:4860::64 name=dns64.dns.google type=AAAA
add address=2001:4860:4860::6464 name=dns64.dns.google type=AAAA

#Cloudflare
#Supports both -04 and -13 content-types
/ip dns
set use-doh-server=https://cloudflare-dns.com/dns-query
    
/ip dns static
add address=104.16.248.249 name=cloudflare-dns.com type=A
add address=104.16.249.249 name=cloudflare-dns.com type=A
add address=2606:4700::6810:f8f9 name=cloudflare-dns.com type=AAAA
add address=2606:4700::6810:f9f9 name=cloudflare-dns.com type=AAAA

#Cloudflare Mozilla
/ip dns
set use-doh-server=https://mozilla.cloudflare-dns.com/dns-query
    
/ip dns static
add address=104.16.249.249 name=mozilla.cloudflare-dns.com type=A
add address=104.16.248.249 name=mozilla.cloudflare-dns.com type=A
add address=2606:4700::6810:f9f9 name=mozilla.cloudflare-dns.com type=AAAA
add address=2606:4700::6810:f8f9 name=mozilla.cloudflare-dns.com type=AAAA

#Cloudflare Block Malware
/ip dns
set use-doh-server=https://security.cloudflare-dns.com/dns-query
    
/ip dns static
add address=104.18.212.220 name=security.cloudflare-dns.com type=A
add address=104.18.213.220 name=security.cloudflare-dns.com type=A
add address=2606:4700::6812:d5dc name=security.cloudflare-dns.com type=AAAA
add address=2606:4700::6812:d4dc name=security.cloudflare-dns.com type=AAAA

#Cloudflare Block Malware and Adult Content
/ip dns
set use-doh-server=https://family.cloudflare-dns.com/dns-query
    
/ip dns static
add address=104.18.209.237 name=family.cloudflare-dns.com type=A
add address=104.18.210.237 name=family.cloudflare-dns.com type=A
add address=2606:4700::6812:d1ed name=family.cloudflare-dns.com type=AAAA
add address=2606:4700::6812:d2ed name=family.cloudflare-dns.com type=AAAA

#Cloudflare DNS64
/ip dns
set use-doh-server=
    
/ip dns static
add address= name= type=A
add address= name= type=A
add address= name= type=AAAA
add address= name= type=AAAA

https://dns64.cloudflare-dns.com/dns-query
Addresses:  2606:4700:4700::64
          2606:4700:4700::6400
          



#Cloudflare
add address=104.16.249.249 name=cloudflare-dns.com type=A
add address=104.16.248.249 name=cloudflare-dns.com type=A

#Cloudflare Family
add address=104.18.209.237 name=family.cloudflare-dns.com type=A
add address=104.18.210.237 name=family.cloudflare-dns.com type=A

add address=8.8.8.8 name=dns.google type=A
add address=8.8.4.4 name=dns.google type=A


File: /sources\config\firewall nat ntp.rsc
/ip firewall nat
add action=masquerade chain=srcnat comment="NTP NAT" protocol=udp src-port=123 to-ports=10000-20000

File: /sources\config\firewall rules.rsc
#Version: 3.0 alpha
#Fecha: 16-01-2018
#RouterOS 6.4x

#/ip firewall filter {
#    add chain=input action=accept protocol=icmp comment="Aceptar ICMP en todas las interfaces"
#    add chain=input action=accept connection-state=established,related comment="Aceptar conexiones con estado stablished, related"
#    
#    add chain=input action=accept in-interface=WAN01 dst-port=8291 protocol=tcp comment="Aceptar conexion al Mikrotik por la WAN01"
#    add chain=input action=drop in-interface=WAN01 comment="Rechazar los paquetes de la WAN01"
#    add chain=input action=drop in-interface=WAN02 comment="Rechazar los paquetes de la WAN02"
#    add chain=input action=drop in-interface=WAN03 comment="Rechazar los paquetes de la WAN03"
#    add chain=input action=drop in-interface=WAN04 comment="Rechazar los paquetes de la WAN04"
#    
#    add chain=forward action=accept connection-state=established,related comment="Aceptar conexiones con estado stablished, related"
#    add chain=forward action=drop connection-state=invalid comment="Rechazar paquetes invalidados."
#    add chain=forward action=drop connection-state=new connection-nat-state=!dstnat in-interface=WAN01 comment="Rechazar los paquetes de la WAN01 que no estan NATeados"
#}

/ip firewall filter {
    #input
    add action=accept chain=input comment="Aceptar conexiones con estado stablished, related" connection-state=established,related
    add action=accept chain=input comment="Aceptar conexion al Mikrotik por la WAN" dst-port=8291 in-interface-list=WAN protocol=tcp
    add action=accept chain=input comment="Aceptar ICMP en todas las interfaces" protocol=icmp
    add action=drop chain=input comment="Rechazar los paquetes de la WAN" in-interface-list=WAN
    
    #forward
    add action=accept chain=forward comment="Aceptar conexiones con estado stablished, related" connection-state=established,related
    add action=drop chain=forward comment="Rechazar paquetes invalidados." connection-state=invalid
    add action=drop chain=forward comment="Rechazar los paquetes de la WAN que no estan NATeados" connection-nat-state=!dstnat connection-state=new in-interface-list=WAN
}

/ip firewall nat {
    add action=dst-nat chain=dstnat in-interface=WAN01 protocol=tcp dst-port=3389 to-addresses=192.168.10.10 to-ports=3389
}

:put "OK...";

File: /sources\config\opendns firewall rules to resolvePublicIP.rsc
#Haciendo una consulta DNS al dominio myip.opendns.com usando los DNS de opendns obtendremos
#la ip publica de la interface de salida.

#OpenDNS ofrece las siguientes direcciones de servidor de nombres de dominio (IPv4) para uso público:10​

#208.67.222.222 (OpenDNS Home Free/VIP)
#208.67.220.220 (OpenDNS Home Free/VIP)
#208.67.222.123 (OpenDNS FamilyShield) port 53, 443, 5353
#208.67.220.123 (OpenDNS FamilyShield) port 53, 443, 5353


/ip firewall address-list
add address=208.67.222.222 comment=RESOLVER1.OPENDNS.COM list=\
    RESOLVERS-OPENDNS
add address=208.67.220.220 comment=RESOLVER2.OPENDNS.COM list=\
    RESOLVERS-OPENDNS

/ip firewall mangle
add action=mark-routing chain=output comment=ID:RESOLVERS-OPENDNS \
    dst-address-list=RESOLVERS-OPENDNS dst-port=53 new-routing-mark=main \
    passthrough=no protocol=udp
    

File: /sources\config\ovpn\certificateca.rsc

:global commonCert {\
    "country"="VE";\
    "state"="LARA";\
    "locality"="Barquisimeto";\
    "organization"="MSF";\
    "unit"="TI";\
    "keySize"=2048;\
    "daysValid"=365
}

:global generateCert do={
    :local properties $1;
    /certificate
    {
        add name=($properties->"name") country=($properties->"country") state=($properties->"state") locality=($properties->"locality") \
            organization=($properties->"organization") unit=($properties->"unit") common-name=($properties->"commonName") key-size=($properties->"keySize") \
            days-valid=($properties->"daysValid") key-usage=($properties->"keyUsage");
    }
    
}

:global generateCA do={
    :global commonCert;
    :global generateCert;
    
    :local CA {\
        "name"="CA";\
        "country"=($commonCert->"country");\
        "state"=($commonCert->"state");\
        "locality"=($commonCert->"locality");\
        "organization"=($commonCert->"organization");\
        "unit"=($commonCert->"unit");\
        "commonName"=[/system identity get name];\
        "keySize"=($commonCert->"keySize");\
        "daysValid"=(($commonCert->"daysValid") * 5);\
        "keyUsage"="key-cert-sign,crl-sign"
    }
    
    $generateCert $CA;
}

#   $1: Certificado
:global sign do={
    :local certificate $1;
    :local caCrlHost $2;
    :local ca $3;
    /certificate
    {
        :if ([:len $ca] > 0) do={
            sign $certificate ca-crl-host=$caCrlHost ca=$ca;
        } else={
            sign $certificate ca-crl-host=$caCrlHost;
        }        
    }
}

:global generateServer do={
    :global commonCert;
    :global generateCert;
    
    :local name "opvn-server";
    
    :local server {\
        "name"=$name;\
        "country"=($commonCert->"country");\
        "state"=($commonCert->"state");\
        "locality"=($commonCert->"locality");\
        "organization"=($commonCert->"organization");\
        "unit"=($commonCert->"unit");\
        "commonName"="$name@$([/system identity get name])";\
        "keySize"=($commonCert->"keySize");\
        "daysValid"=(($commonCert->"daysValid") * 5);\
        "keyUsage"="digital-signature,key-encipherment,tls-server"
    }
    
    $generateCert $server;
}

:global generateClient do={
    :global commonCert;
    :global generateCert;
    
    :local name $1;
    
    :local server {\
        "name"=$name;\
        "country"=($commonCert->"country");\
        "state"=($commonCert->"state");\
        "locality"=($commonCert->"locality");\
        "organization"=($commonCert->"organization");\
        "unit"=($commonCert->"unit");\
        "commonName"="$name@$([/system identity get name])";\
        "keySize"=($commonCert->"keySize");\
        "daysValid"=(($commonCert->"daysValid") * 1);\
        "keyUsage"="digital-signature,tls-client"
    }
    
    $generateCert $server;
}


File: /sources\config\router pcc dinamico.rsc
#Version: 3.0 alpha
#Fecha: 16-01-2018
#RouterOS 6.4x

:local lCIRDLen "24";
:local lAddress "192.168.10.1";
:local lNetwork "192.168.10.0";
:local lCIRDAddress "$lAddress/$lCIRDLen";
:local lCIRDNetwork "$lNetwork/$lCIRDLen";
:local lDHCPServerRange "192.168.10.101-192.168.10.199";
:local lDHCPServerGateway "$lAddress";
:local lDHCPServerDNS "$lAddress";
:local lDNSServer "8.8.8.8,8.8.4.4";

/interface ethernet {
    set [ find default-name=ether1 ] comment="WAN 01" name=WAN01;
    set [ find default-name=ether2 ] comment="WAN 02" name=WAN02;
    set [ find default-name=ether3 ] comment="WAN 03" name=WAN03;
    set [ find default-name=ether4 ] comment="WAN 04" name=WAN04;
    set [ find default-name=ether5 ] comment="LAN 01" name=LAN01;
}

/interface list {
    add name=WAN
}

/interface list member {
    add interface=WAN01 list=WAN
    add interface=WAN02 list=WAN
    add interface=WAN03 list=WAN
    add interface=WAN04 list=WAN
}

/ip dhcp-client {
    add dhcp-options=hostname,clientid disabled=no add-default-route=no interface=WAN01 comment="Cliente DHCP interface WAN01";
    add dhcp-options=hostname,clientid disabled=no add-default-route=no interface=WAN02 comment="Cliente DHCP interface WAN02";
    add dhcp-options=hostname,clientid disabled=no add-default-route=no interface=WAN03 comment="Cliente DHCP interface WAN03";
    add dhcp-options=hostname,clientid disabled=no add-default-route=no interface=WAN04 comment="Cliente DHCP interface WAN04";
}

/ip address {
    add address=$lCIRDAddress interface=LAN01 comment="IP interface LAN01";
}

/ip pool {
    add name=DHCP_POOL_LAN01 ranges=$lDHCPServerRange;
}

/ip dhcp-server {
    add address-pool=DHCP_POOL_LAN01 disabled=no interface=LAN01 name=DHCP_LAN01;
}

/ip dhcp-server network {
    add address=$lCIRDNetwork dns-server=$lDHCPServerDNS gateway=$lDHCPServerGateway comment="Parametros servidor DHCP interface LAN01";
}

/ip firewall nat {
    add chain=srcnat src-address=$lCIRDAddress out-interface=WAN01 action=masquerade comment="Masquerade red local a WAN01";
    add chain=srcnat src-address=$lCIRDAddress out-interface=WAN02 action=masquerade comment="Masquerade red local a WAN02";
    add chain=srcnat src-address=$lCIRDAddress out-interface=WAN03 action=masquerade comment="Masquerade red local a WAN03";
    add chain=srcnat src-address=$lCIRDAddress out-interface=WAN04 action=masquerade comment="Masquerade red local a WAN04";
}

/ip dns {
    set allow-remote-requests=yes cache-max-ttl=1w cache-size=2048KiB max-udp-packet-size=512 servers=$lDNSServer;
}

/ip firewall mangle {
    #Gestionar Dinamicamente    
    add action=accept chain=prerouting comment=ID:WAN01 dst-address=127.0.0.0/24 in-interface=LAN01
    add action=accept chain=prerouting comment=ID:WAN02 dst-address=127.0.0.0/24 in-interface=LAN01
    add action=accept chain=prerouting comment=ID:WAN03 dst-address=127.0.0.0/24 in-interface=LAN01
    add action=accept chain=prerouting comment=ID:WAN04 dst-address=127.0.0.0/24 in-interface=LAN01

    add action=mark-connection chain=input comment="Marcar input wan1_conn" \
        in-interface=WAN01 new-connection-mark=wan1_conn passthrough=yes
    add action=mark-connection chain=input comment="Marcar input wan2_conn" \
        in-interface=WAN02 new-connection-mark=wan2_conn passthrough=yes
    add action=mark-connection chain=input comment="Marcar input wan3_conn" \
        in-interface=WAN03 new-connection-mark=wan3_conn passthrough=yes
    add action=mark-connection chain=input comment="Marcar input wan4_conn" \
        in-interface=WAN04 new-connection-mark=wan4_conn passthrough=yes
        
    add action=mark-routing chain=output comment="Marcar output to_wan1" \
        connection-mark=wan1_conn new-routing-mark=to_wan1
    add action=mark-routing chain=output comment="Marcar output to_wan2" \
        connection-mark=wan2_conn new-routing-mark=to_wan2
    add action=mark-routing chain=output comment="Marcar output to_wan3" \
        connection-mark=wan3_conn new-routing-mark=to_wan3
    add action=mark-routing chain=output comment="Marcar output to_wan4" \
        connection-mark=wan4_conn new-routing-mark=to_wan4
        
    add action=mark-connection chain=prerouting comment="PCC wan1_conn" \
        connection-mark=no-mark dst-address-type=!local in-interface=LAN01 \
        new-connection-mark=wan1_conn passthrough=yes per-connection-classifier=\
        both-addresses:4/0
    add action=mark-connection chain=prerouting comment="PCC wan2_conn" \
        connection-mark=no-mark dst-address-type=!local in-interface=LAN01 \
        new-connection-mark=wan2_conn passthrough=yes per-connection-classifier=\
        both-addresses:4/1
    add action=mark-connection chain=prerouting comment="PCC wan3_conn" \
        connection-mark=no-mark dst-address-type=!local in-interface=LAN01 \
        new-connection-mark=wan3_conn passthrough=yes per-connection-classifier=\
        both-addresses:4/2    
    add action=mark-connection chain=prerouting comment="PCC wan4_conn" \
        connection-mark=no-mark dst-address-type=!local in-interface=LAN01 \
        new-connection-mark=wan4_conn passthrough=yes per-connection-classifier=\
        both-addresses:4/3
        
    add action=mark-routing chain=prerouting comment="Marcar prerouting to_wan1" \
        connection-mark=wan1_conn in-interface=LAN01 new-routing-mark=to_wan1
    add action=mark-routing chain=prerouting comment="Marcar prerouting to_wan2" \
        connection-mark=wan2_conn in-interface=LAN01 new-routing-mark=to_wan2
    add action=mark-routing chain=prerouting comment="Marcar prerouting to_wan3" \
        connection-mark=wan3_conn in-interface=LAN01 new-routing-mark=to_wan3
    add action=mark-routing chain=prerouting comment="Marcar prerouting to_wan4" \
        connection-mark=wan4_conn in-interface=LAN01 new-routing-mark=to_wan4
        
    add action=mark-connection chain=prerouting comment=\
        "Marcar coneccion RDP wan1_nat" dst-port=3389 in-interface=\
        WAN01 new-connection-mark=wan1_nat passthrough=yes protocol=tcp
    add action=mark-routing chain=output comment=\
        "Rutear coneccion NATeada to_wan1" connection-mark=wan1_nat \
        new-routing-mark=to_wan1 passthrough=yes
}

#Gestionar Dinamicamente

/ip route {
    add gateway=WAN01 distance=1 comment="ID:WAN01";
    add gateway=WAN02 distance=2 comment="ID:WAN02";
    add gateway=WAN03 distance=3 comment="ID:WAN03";
    add gateway=WAN04 distance=4 comment="ID:WAN04";
    
    add dst-address=0.0.0.0/0 gateway=WAN01 routing-mark=to_wan1 check-gateway=ping comment="ID:WAN01";
    add dst-address=0.0.0.0/0 gateway=WAN02 routing-mark=to_wan2 check-gateway=ping comment="ID:WAN02";
    add dst-address=0.0.0.0/0 gateway=WAN03 routing-mark=to_wan3 check-gateway=ping comment="ID:WAN03";
    add dst-address=0.0.0.0/0 gateway=WAN04 routing-mark=to_wan4 check-gateway=ping comment="ID:WAN04";
}

:put "OK...";

File: /sources\config\router-wan-lan.rsc
:local routerName "router.lan";


/interface list {
    add name=WAN comment="MSF WAN list";
    add name=LAN comment="MSF LAN list";
}


File: /sources\config-init.rsc
#Version: 3.0 alpha
#Fecha: 22-08-2017
#RouterOS 6.40 y superior.
#Comentario: Configuracion inicial de MSF.

:global setLastError;
:local lScriptName "config-init";

#TODO-BEGIN

:global gModules;
:set gModules \
{\
    "01"=\
    {\
        "name"="module-functions";\
        "enable"=true;\
        "loaded"=false;\
        "config"=false;\
        "description"="Funciones Generales."\
    };\
    "02"=\
    {\
        "name"="module-dyndns";\
        "enable"=false;\
        "loaded"=false;\
        "config"=true;\
        "description"="DynDNS Update."\
    };\
    "03"=\
    {\
        "name"="module-pcc-init";\
        "enable"=false;\
        "loaded"=false;\
        "config"=true;\
        "description"="Inicializacion de modulo de balanceo por PCC."\
    };\
    "04"=\
    {\
        "name"="module-geoip";\
        "enable"=true;\
        "loaded"=false;\
        "config"=false;\
        "description"="Herramienta para localizar IP geograficamente."\
    };\
    "05"=\
    {\
        "name"="module-arrays";\
        "enable"=true;\
        "loaded"=false;\
        "config"=false;\
        "description"="Funciones para manejo de arreglos."\
    };\
    "06"=\
    {\
        "name"="module-hex";\
        "enable"=true;\
        "loaded"=false;\
        "config"=false;\
        "description"="Funciones manejo de hexadecimal."\
    };\
    "07"=\
    {\
        "name"="module-base32";\
        "enable"=true;\
        "loaded"=false;\
        "config"=false;\
        "description"="Funciones Base32."\
    };\    
    "08"=\
    {\
        "name"="module-sha1";\
        "enable"=true;\
        "loaded"=false;\
        "config"=false;\
        "description"="Funciones sha1 digest."\
    };\
    "09"=\
    {\
        "name"="module-hmac";\
        "enable"=true;\
        "loaded"=false;\
        "config"=false;\
        "description"="Funciones hmac."\
    };\
    "10"=\
    {\
        "name"="module-time";\
        "enable"=true;\
        "loaded"=false;\
        "config"=false;\
        "description"="Funciones timestamp."\
    };\
    "11"=\
    {\
        "name"="module-totp";\
        "enable"=true;\
        "loaded"=false;\
        "config"=false;\
        "description"="Funciones TOTP."\
    }\
}

:global gScripts;
:set gScripts \
{\
    "init"=\
    {\
        "startRun"=0;\
        "endRun"=0;\
        "enable"=true;\
        "startDate"="";\
        "startTime"="startup";\
        "interval"=0m;\
        "description"="Inicializacion del MSF."\
    };\
    "script-pcc-qos-wan"=\
    {\
        "startRun"=0;\
        "endRun"=0;\
        "enable"=true;\
        "startDate"="";\
        "startTime"="startup";\
        "interval"=10m;\
        "description"="PCC QoS para interfaces WAN."\
    };\
    "script-dyndns"=\
    {\
        "startRun"=0;\
        "endRun"=0;\
        "enable"=true;\
        "startDate"="";\
        "startTime"="startup";\
        "interval"=5m;\
        "description"="Dyndns Update."\
    }\
}

#TODO-END

$setLastError 0 ("$lScriptName cargado.");

File: /sources\config-module-dyndns.rsc
#Version: 3.0 alpha
#Fecha: 22-08-2017
#RouterOS 6.40 y superior.
#Comentario:

:global setLastError;
:local lScriptName "config-module-dyndns";

#TODO-BEGIN

:global gDynDNS;
:global gDynDNS \
{ \
    "user"=""; \
    "password"=""; \
    "host"=""; \
    "interface"="WAN01"
};

#TODO-END

$setLastError 0 ("$lScriptName cargado.");

File: /sources\config-module-pcc-init.rsc
#Version: 3.0 alpha
#Fecha: 22-08-2017
#RouterOS 6.40 y superior.
#Comentario:

:global setLastError;
:local lScriptName "config-module-pcc-init";

#TODO-BEGIN

:global gWanInterfaces;
:set gWanInterfaces \
{\
    "WAN01"=\
    {\
        "dhcp"=true;\
        "ip"="";\
        "gateway"="";\
        "enableRouting"=false;\
        "routingMark"="to_wan1";\
        "distance"=1;\
        "pingTime"="";\
        "lastInterfaceCheck"="";\
        "lastRoutingCheck"="";\
        "status"=""\
    };\
    "WAN02"=\
    {\
        "dhcp"=true;\
        "ip"="";\
        "gateway"="";\
        "enableRouting"=false;\
        "routingMark"="to_wan2";\
        "distance"=1;\
        "pingTime"="";\
        "lastInterfaceCheck"="";\
        "lastRoutingCheck"="";\
        "status"=""\
    };\
    "WAN03"=\
    {\
        "dhcp"=true;\
        "ip"="";\
        "gateway"="";\
        "enableRouting"=false;\
        "routingMark"="to_wan3";\
        "distance"=1;\
        "pingTime"="";\
        "lastInterfaceCheck"="";\
        "lastRoutingCheck"="";\
        "status"=""\
    };\
    "WAN04"=\
    {\
        "dhcp"=true;\
        "ip"="";\
        "gateway"="";\
        "enableRouting"=false;\
        "routingMark"="to_wan4";\
        "distance"=1;\
        "pingTime"="";\
        "lastInterfaceCheck"="";\
        "lastRoutingCheck"="";\
        "status"=""\
    }\
}

:global gPingHost;
:set gPingHost \
{\
    "8.8.8.8";\
    "8.8.4.4"
}

:global gPingQoS;
:set gPingQoS \
{\
    "pingCount"=10;\
    "umbralCount"=7;\
    "size"=64;\
    "timeout"="500ms"
}

#TODO-END

$setLastError 0 ("$lScriptName cargado.");

File: /sources\default.rsc
#| Switch mode:
#|  * all interfaces switched;
#| LAN Configuration:

:global defconfMode;
:log info "Starting defconf script";
#-------------------------------------------------------------------------------
# Apply configuration.
# these commands are executed after installation or configuration reset
#-------------------------------------------------------------------------------
:if ($action = "apply") do={
  # wait for interfaces
  :local count 0;
  :while ([/interface ethernet find] = "") do={
    :if ($count = 30) do={
      :log warning "DefConf: Unable to find ethernet interfaces";
      /quit;
    }
    :delay 1s; :set count ($count +1); 
  };
 /interface bridge
   add name=bridge disabled=no auto-mac=yes protocol-mode=rstp comment=defconf;
 :local bMACIsSet 0;
 :foreach k in=[/interface find where !(slave=yes  || name~"bridge")] do={
   :local tmpPortName [/interface get $k name];
   :if ($bMACIsSet = 0) do={
     :if ([/interface get $k type] = "ether") do={
       /interface bridge set "bridge" auto-mac=no admin-mac=[/interface ethernet get $tmpPortName mac-address];
       :set bMACIsSet 1;
     }
   }
   /interface bridge port
     add bridge=bridge interface=$tmpPortName comment=defconf;
 }
  /ip address add address=192.168.88.1/24 interface=bridge comment="defconf";
}
#-------------------------------------------------------------------------------
# Revert configuration.
# these commands are executed if user requests to remove default configuration
#-------------------------------------------------------------------------------
:if ($action = "revert") do={
/user set admin password=""
 /system routerboard mode-button set enabled=no
 /system routerboard mode-button set on-event=""
 /system script remove [find comment~"defconf"]
 /ip firewall filter remove [find comment~"defconf"]
 /ip firewall nat remove [find comment~"defconf"]
 /interface list member remove [find comment~"defconf"]
 /interface detect-internet set detect-interface-list=none
 /interface detect-internet set lan-interface-list=none
 /interface detect-internet set wan-interface-list=none
 /interface detect-internet set internet-interface-list=none
 /interface list remove [find comment~"defconf"]
 /tool mac-server set allowed-interface-list=all
 /tool mac-server mac-winbox set allowed-interface-list=all
 /ip neighbor discovery-settings set discover-interface-list=!dynamic
   :local o [/ip dhcp-server network find comment="defconf"]
   :if ([:len $o] != 0) do={ /ip dhcp-server network remove $o }
   :local o [/ip dhcp-server find name="defconf" !disabled]
   :if ([:len $o] != 0) do={ /ip dhcp-server remove $o }
   /ip pool {
     :local o [find name="default-dhcp" ranges=192.168.88.10-192.168.88.254]
     :if ([:len $o] != 0) do={ remove $o }
   }
   :local o [/ip dhcp-client find comment="defconf"]
   :if ([:len $o] != 0) do={ /ip dhcp-client remove $o }
 /ip dns {
   set allow-remote-requests=no
   :local o [static find comment="defconf"]
   :if ([:len $o] != 0) do={ static remove $o }
 }
 /ip address {
   :local o [find comment="defconf"]
   :if ([:len $o] != 0) do={ remove $o }
 }
 :foreach iface in=[/interface ethernet find] do={
   /interface ethernet set $iface name=[get $iface default-name]
 }
 /interface bridge port remove [find comment="defconf"]
 /interface bridge remove [find comment="defconf"]
 /interface wireless cap set enabled=no interfaces="" caps-man-addresses=""
  /caps-man manager set enabled=no
  /caps-man manager interface remove [find comment="defconf"]
  /caps-man manager interface set [ find default=yes ] forbid=no
  /caps-man provisioning remove [find comment="defconf"]
  /caps-man configuration remove [find comment="defconf"]
}
:log info Defconf_script_finished;
:set defconfMode;




-------------------------------------------------------------------------------
#| Switch mode:

#|  * all interfaces switched;

#| LAN Configuration:



:global defconfMode;

:log info "Starting defconf script";

#-------------------------------------------------------------------------------

# Apply configuration.

# these commands are executed after installation or configuration reset

#-------------------------------------------------------------------------------

:if ($action = "apply") do={

  # wait for interfaces
                              
  :local count 0;

  :while ([/interface ethernet find] = "") do={

    :if ($count = 30) do={

      :log warning "DefConf: Unable to find ethernet interfaces";

      /quit;

    }

    :delay 1s; :set count ($count +1); 

  };

 /interface bridge

   add name=bridge disabled=no auto-mac=yes protocol-mode=rstp comment=defconf;

 :local bMACIsSet 0;

 :foreach k in=[/interface find where !(slave=yes  || name~"bridge")] do={

   :local tmpPortName [/interface get $k name];

   :if ($bMACIsSet = 0) do={

     :if ([/interface get $k type] = "ether") do={

       /interface bridge set "bridge" auto-mac=no admin-mac=[/interface ethernet g
et $tmpPortName mac-address];

       :set bMACIsSet 1;

     }

   }

   /interface bridge port

     add bridge=bridge interface=$tmpPortName comment=defconf;

 }

  /ip address add address=192.168.88.1/24 interface=bridge comment="defconf";
                              
}

#-------------------------------------------------------------------------------

# Revert configuration.

# these commands are executed if user requests to remove default configuration

#-------------------------------------------------------------------------------

:if ($action = "revert") do={

/user set admin password=""

 /system routerboard mode-button set enabled=no

 /system routerboard mode-button set on-event=""

 /system script remove [find comment~"defconf"]

 /ip firewall filter remove [find comment~"defconf"]

 /ip firewall nat remove [find comment~"defconf"]
 /interface list member remove [find comment~"defconf"]

 /interface detect-internet set detect-interface-list=none

 /interface detect-internet set lan-interface-list=none

 /interface detect-internet set wan-interface-list=none

 /interface detect-internet set internet-interface-list=none

 /interface list remove [find comment~"defconf"]

 /tool mac-server set allowed-interface-list=all

 /tool mac-server mac-winbox set allowed-interface-list=all

 /ip neighbor discovery-settings set discover-interface-list=!dynamic

   :local o [/ip dhcp-server network find comment="defconf"]

   :if ([:len $o] != 0) do={ /ip dhcp-server network remove $o }

   :local o [/ip dhcp-server find name="defconf" !disabled]

   :if ([:len $o] != 0) do={ /ip dhcp-server remove $o }

   /ip pool {

     :local o [find name="default-dhcp" ranges=192.168.88.10-192.168.88.254]

     :if ([:len $o] != 0) do={ remove $o }

   }

   :local o [/ip dhcp-client find comment="defconf"]

   :if ([:len $o] != 0) do={ /ip dhcp-client remove $o }

 /ip dns {

   set allow-remote-requests=no
   :local o [static find comment="defconf"]

   :if ([:len $o] != 0) do={ static remove $o }

 }                            

 /ip address {

   :local o [find comment="defconf"]

   :if ([:len $o] != 0) do={ remove $o }

 }

 :foreach iface in=[/interface ethernet find] do={

   /interface ethernet set $iface name=[get $iface default-name]

 }

 /interface bridge port remove [find comment="defconf"]

 /interface bridge remove [find comment="defconf"]

 /interface wireless cap set enabled=no interfaces="" caps-man-addresses=""

  /caps-man manager set enabled=no
                              
  /caps-man manager interface remove [find comment="defconf"]

  /caps-man manager interface set [ find default=yes ] forbid=no

  /caps-man provisioning remove [find comment="defconf"]

  /caps-man configuration remove [find comment="defconf"]

}

:log info Defconf_script_finished;

:set defconfMode;



File: /sources\dns-dos.rsc
#Version: 3.0 alpha.
#Fecha: 22-12-2019.
#RouterOS 6.43 y superior.
#Comentario: Se introduce el calculo del delay para el API, 45 consultas por minuto.

#TODO-BEGIN

:local server 192.168.88.1;
:local serverPort 53;


:for index from=1 to=5 do={
    :local domainName "mikroterosyubiquiteros.ns$index.com";
#    /resolve server=$server server-port=$serverPort domain-name=$domainName;
    :do {
        /resolve domain-name=$domainName;
     } on-error={
     }
    :put $domainName;
}
#TODO-END

File: /sources\geoip.rsc
#Version: 3.0 alpha.
#Fecha: 22-12-2019.
#RouterOS 6.43 y superior.
#Comentario: Se introduce el calculo del delay para el API, 45 consultas por minuto.

#TODO-BEGIN

:local getCurrentTimestamp;
:local getCurrentTimestamp do={
    :local date [/system clock get date];
    :local months ({"jan"=1;"feb"=2;"mar"=3;"apr"=4;"may"=5;"jun"=6;"jul"=7;"aug"=8;"sep"=9;"oct"=10;"nov"=11;"dec"=12});
    :local daysForMonths ({31;28;31;30;31;30;31;31;30;31;30;31});
    
    :local day [:tonum [:pick $date 4 6]];
    :local month ($months->[:pick $date 0 3]);
    :local year [:tonum [:pick $date 7 11]];
    
    :local leapDays (($year - 1968) / 4);
    
    :if ((($leapDays * 4) + 1968) = $year) do={
        :set leapDays ($leapDays - 1);
        :set ($daysForMonths->1) 29;
    }
    
    :local days ($day - 1);
    
    :if (($month - 1) > 0) do={
        :for index from=0 to=($month - 2) do={
            :set days ($days + ($daysForMonths->($index)));
        }
    }
        
    :local daysForYear 365;
    :local secondsForDay 86400;
    :local gmtOffset [/system clock get gmt-offset];
    
    :local now [/system clock get time];
    :local hour [:tonum [:pick $now 0 2]];
    :local minutes [:tonum [:pick $now 3 5]];
    :local seconds [:tonum [:pick $now 6 8]];

    :local timestamp ((((($year - 1970) * $daysForYear) + $leapDays + $days) * $secondsForDay) + ($hour * 3600) + ($minutes * 60) + seconds);
    
    :if ($gmtOffset <= $secondsForDay) do={
        :set timestamp ($timestamp - $gmtOffset);
    } else={
        :set timestamp ($timestamp + (-$gmtOffset&0x00000000FFFFFFFF));
    }
    
    :return $timestamp;    
}


:local format;
:local format do={
    :local src $1;
    :local length $2;
    :local lengthSrc [:len $src];
    
    :if ($lengthSrc < ($length)) do={
        :for index from=$lengthSrc to=($length - 1) do={
            :set src ($src . " ");
        }
    } else={
        :set src ([:pick $src 0 ($length - 1)] . " ");
    }
    :return $src;
}

:local dstAddressQueryList ([]);
:local dstAddressQueryResult ([]);
:local idx 0;
:local request 0;
:local timeStamp [$getCurrentTimestamp];
:local firewallConnections [/ip firewall connection find];

:put "";
:put ("Nro. de conexiones: " . [:len $firewallConnections]);
:put "";
:put ([$format "#" 5] . [$format "SRC. ADDRESS" 22] . [$format "DST. ADDRESS" 22] . [$format "PROTO" 7] \
. [$format "COUNTRY" 9] . [$format "COUNTRY NAME" 25] . [$format "AS" 10] . [$format "AS NAME" 30]);

:foreach id in=$firewallConnections do={
    :local connection [/ip firewall connection get $id];
    :local dstAddress ($connection->"dst-address");
    :local srcAddress ($connection->"src-address");
    :local protocol ($connection->"protocol");
    
    :if (([:len $dstAddress] > 0) and ([:len $srcAddress] > 0)) do={
        :local data;
        :local dnsCache ([]);
        :local dnsData;
        
        :local dstIp $dstAddress;
        :local doubleDot [:find $dstIp ":"];
        :if ( $doubleDot > 0) do={ 
            :set dstIp [:pick $dstIp 0 $doubleDot];
        }
        
        :local indexFind [:find $dstAddressQueryList $dstIp];
        :if (!($indexFind >=0)) do={
        
            
            :foreach idDns in=[/ip dns cache all find data=$dstIp] do={
                :set dnsData [/ip dns cache all get $idDns];
                :set dnsCache ($dnsCache, {$dnsData});
                
                :foreach oIdDns in=[/ip dns cache all find data=($dnsData->"name")] do={
                    :set dnsData [/ip dns cache all get $oIdDns];
                    :set dnsCache ($dnsCache, {$dnsData});
                }
            }
        
        
            :local lUrl "http://ip-api.com/csv/$dstIp?fields=status,message,country,countryCode,as,asname,query";
            :local result;
            
            
            do {
                :local isPrivate  ((10.0.0.0 = ($dstIp&255.0.0.0)) or (172.16.0.0 = ($dstIp&255.240.0.0)) or  (192.168.0.0 = ($dstIp&255.255.0.0)));
                :local isReserved ((0.0.0.0 = ($dstIp&255.0.0.0)) or (127.0.0.0 = ($dstIp&255.0.0.0)) or (169.254.0.0 = ($dstIp&255.255.0.0)) \
                or (224.0.0.0 = ($dstIp&240.0.0.0)) or (240.0.0.0 = ($dstIp&240.0.0.0)));
                :if ($isPrivate or $isReserved) do={
                    :if ($isPrivate) do={
                        :set data {"country"=""; "countryCode"="PRIVATE"; "as"=""; "asname"=""; "dnsCache"=($dnsCache)};
                    } else={
                        :set data {"country"=""; "countryCode"="RESERVED"; "as"=""; "asname"=""; "dnsCache"=($dnsCache)};
                    }
                } else={
                    :set result [/tool fetch url=$lUrl mode=http as-value output=user];
                    :set request ($request + 1);
                    :if ($request >= 45) do={
                        :set request 0;
                        :local timeToDelay ([$getCurrentTimestamp] - $timeStamp);
                        :if ($timeToDelay < 65) do={
                            :delay (65 - $timeToDelay);
                        }
                        :set timeStamp [$getCurrentTimestamp];
                    }
                    
                    :local arrayResult [:toarray ($result->"data")];
                    
                    :if ([:typeof $arrayResult] = "array") do={
                        :if ([:pick $arrayResult 0] = "success") do={
                            :local as (($arrayResult->3) . " ");
                            :set as [:pick $as 0 [:find $as " "]];
                            :set data {"country"=($arrayResult->1); "countryCode"=($arrayResult->2); "as"=$as; "asname"=($arrayResult->4); "dnsCache"=($dnsCache)};
                        }
                    }
                }
                :set dstAddressQueryList ($dstAddressQueryList, $dstIp);
                :set dstAddressQueryResult ($dstAddressQueryResult, {$data});
            } on-error={
                :put ([$format $dstIp 16] . " - ERROR");
            }
        } else={
            :set data ($dstAddressQueryResult->$indexFind);
            :set dnsCache ($data->"dnsCache");
        }

        :set idx ($idx + 1);
        :put ([$format $idx 5] . [$format $srcAddress 22] . [$format $dstAddress 22] . [$format $protocol 7] \
        . [$format ($data->"countryCode") 9] . [$format ($data->"country") 25] . [$format ($data->"as") 10] . [$format ($data->"asname") 30]);
        :if ([:len $dnsCache] > 0) do={
            :foreach dnsData in=$dnsCache do={
                :put ([$format ("     type: " . ($dnsData->"type")) 27] . [$format ("name: " . ($dnsData->"name")) 50]);
            }
            :put "";
        }
    }
}

#TODO-END

File: /sources\init.rsc
#Version: 3.0 alpha
#Fecha: 22-08-2017
#RouterOS 6.40 y superior.
#Comentario: Inicializacion de MSF.

#Constante EMPTYARRAY
#   Descripcion: Representa un array vacio en MSF.
:global EMPTYARRAY [:toarray ""];

#Function isEmptyArray
#   Descripcion: Retorna si un array esta vacio o no.
#   Param:
#       $1: Un array.
#   Return: boolean.
#
:global isEmptyArray do={
    :global EMPTYARRAY;
    :return ($1 = $EMPTYARRAY);
}

#Constante NOTHING
#   Descripcion: Representa el valor de una variable vacia en MSF.
:global NOTHING [:nothing];

#Function isNothing
#   Descripcion: Retorna si una variable esta vacia o no.
#   Param:
#       $1: Una variable.
#   Return: boolean.
#   

:global isNothing do={
    :global NOTHING;
    :return ($1 = $NOTHING);
}

#Constante MSFVERSION
#   Descripcion: Version del MSF.
:global MSFVERSION "3.0 alpha";

#Constante ROSVERSION
#   Descripcion: Version minima de RouterOS para ejecutar MSF.
:global ROSVERSION "6.40";

#Array lastError
#   Descripcion: Estructura para el paso de errores entre ejecucion de scripts en MSF.
#   Keys:
#       code: Codigo de error.
#       msg: Mensaje de error.
:global lastError;
:set lastError {"code"=0; "msg"=""};

#Function setLastError
#   Descripcion: Establece los valores para el array lastError.
#   Param:
#       $1: Codigo de error.
#       $2: Mensaje de error.
#   Return:
:global setLastError do={
    :global lastError;
    :set ($lastError->"code") $1;
    :set ($lastError->"msg") "$2 (codigo $1).";
}

:global logInfo do={
    :log info message="$1 - $2";
}

:global logWarning do={
    :log warning message="$1 - $2";
}

:global logError do={
    :log error message="$1 - $2";
}

:global logDebug do={
    :log debug message="$1 - $2";
}

#Function loadScript
#   Descripcion: Carga un script de configuracion.
#   Param:
#      $1: nombre del script.
#
:global loadScript do={
    :global isEmptyArray;
    :global setLastError;
    :global lastError;
    :local lScriptId [/system script find name=$1];
    
    $setLastError 1 ("Cargando $1...");
    :if (!([$isEmptyArray $lScriptId])) do={
        do {
            [/system script run $lScriptId];
            :if (($lastError->"code") != 0) do={
                $setLastError 2 ("No se pudo cargar $1");
            }
        } on-error={
            $setLastError 3 ("Ejecutando $1");
        }
    } else={
        $setLastError 4 ("No se ha instalado $1");
    }
    :return ($lastError->"code");
}

#Function setModuleLoaded
#   Param:
#   $1: Id del modulo
#
:global setModuleLoaded do={
    :global gModules;    
    :set ($gModules->"$1"->"loaded") true;
}

#Cargar modulos

:local loadModules do={
    :global gModules;    
    :global logInfo;
    :global logError;
    :global lastError;
    :global loadScript;
    :local lScriptName "init.loadModules";
    :local lErrorCode;
    
    :foreach kModuleId,fModule in=$gModules do={
    
        :if ($fModule->"enable") do={
            :set lErrorCode 0;
            
            :if ($fModule->"config") do={
                :set lErrorCode [$loadScript ("config-" . ($fModule->"name"))];

                :if ($lErrorCode != 0) do={
                    $logError $lScriptName (($fModule->"name") . " - " .($lastError->"msg"));
                } else={
                    $logInfo $lScriptName ($lastError->"msg");
                }
            }
            
            :if ($lErrorCode = 0) do={
                :set lErrorCode [$loadScript ($fModule->"name")];

                :if ($lErrorCode != 0) do={
                    $logError $lScriptName ($lastError->"msg");
                } else={
                    :set ($gModules->"$kModuleId"->"loaded") true;
                    $logInfo $lScriptName ($lastError->"msg");
                }            
            }            
        }
    }
}

#Function scheduleScripts

:local scheduleScripts do={
    :global isEmptyArray;
    :global gScripts;
    :global logInfo;
    :global logError;
    :local lScriptName "init.scheduleScripts";
    
    :foreach kScript,fScript in=$gScripts do={
    
        :if ($fScript->"enable") do={
            :local lScriptId [/system script find name=$kScript];
            
            :if (!([$isEmptyArray $lScriptId])) do={
                :local lSchedulerId ([/system scheduler find name=$kScript]);
                
                :if (([$isEmptyArray $lSchedulerId])) do={
                    $logInfo $lScriptName ("Registrando script $kScript...");
                    [/system scheduler add comment=($fScript->"description") \
                                           name=$kScript \
                                           on-event=$kScript \
                                           start-date=($fScript->"startDate") \
                                           start-time=($fScript->"startTime") \
                                           interval=($fScript->"interval")];
                           
                    :set lScriptId [/system scheduler find name=$kScript];
                    
                    :if (!([$isEmptyArray $lScriptId])) do={
                        $logInfo $lScriptName ("Script $kScript registrado.");
                    } else={
                        $logError $lScriptName ("Registrando script $kScript.");
                    }                        
                } else={
                    $logInfo $lScriptName ("Script $kScript registrado.");
                    :local lScheduler ([/system scheduler get $lSchedulerId]);
                    
                    :if ($lScheduler->"interval" != $fScript->"interval") do={
                        [/system scheduler set $lSchedulerId interva=($fScript->"interval")];
                    }
                    :if ($lScheduler->"start-date" != $fScript->"startDate") do={
                        [/system scheduler set $lSchedulerId start-date=($fScript->"startDate")];
                    }
                    :if ($lScheduler->"start-time" != $fScript->"startTime") do={
                        [/system scheduler set $lSchedulerId start-time=($fScript->"startTime")];
                    }
                    :if ($lScheduler->"comment" != $fScript->"description") do={
                        [/system scheduler set $lSchedulerId comment=($fScript->"description")];
                    }
                }
            } else={
                $logError $lScriptName ("Script $kScript no instalado.");
            }
        } else={
            :local lSchedulerId ([/system scheduler find name=$kScript]);
            :if (!([$isEmptyArray $lSchedulerId])) do={
                [/system scheduler remove $lSchedulerId];
                $logInfo $lScriptName ("Script $kScript removido.");
            } else={
                $logInfo $lScriptName ("Script $kScript deshabilitado.");
            }
        }
    }
}

#Function scheduleScripts

:global setScriptStartRun do={
    :global gScripts;
    :local lCount [:tonum ($gScripts->"$1"->"startRun")];
    :set lCount ($lCount + 1);
    :set ($gScripts->"$1"->"startRun") $lCount;
}

#Function scheduleScripts

:global setScriptEndRun do={
    :global gScripts;
    :local lCount [:tonum ($gScripts->"$1"->"endRun")];
    :set lCount ($lCount + 1);
    :set ($gScripts->"$1"->"endRun") $lCount;
}


do {
#TODO-BEGIN

:local lScriptName "init";
:local lConfigName "config-init";

:local lErrorCode [$loadScript $lConfigName];

:if ($lErrorCode != 0) do={
    $logError $lScriptName ($lastError->"msg");
    :return $lErrorCode;
} else={
    $logInfo $lScriptName ($lastError->"msg");
}

$loadModules;
$scheduleScripts;

#TODO-END

    $logInfo $lScriptName "MSF cargado.";
} on-error={
    $logError $lScriptName "ERROR Cargando MSF.";
}

File: /sources\lure-firewall\lure-firewall-filter.rsc
#Esta regla debe ir luego de las reglas INPUT que se aceptan
#Procesa los INPUT desde las lita de interface WAN y que no este en la lista
#secure_list
#Agrega a la lista secure_list tu red local.

:global services;
:if ([:len $services] <= 0) do={
    /system script run lure-services
}

:local chainName "lure_input";

/ip firewall filter

:local jumpId [find jump-target=$chainName];

:if ([:len $jumpId] <= 0) do={
    add action=jump chain=input comment="lure input" connection-state=new \
        in-interface-list=WAN jump-target=$chainName src-address-list=\
        !secure_list
}

remove numbers=[find chain=$chainName];

add action=tarpit chain=$chainName comment="lure input BLACKLIST TCP TARPIT" \
    protocol=tcp src-address-list=lure_input_blacklist;
    
add action=drop chain=$chainName comment="lure input BLACKLIST DROP" \
    src-address-list=lure_input_blacklist;

add action=add-src-to-address-list address-list=lure_input_blacklist \
    address-list-timeout=none-static chain=$chainName comment=\
    "lure input BLACKLIST" log=yes log-prefix="LURE DROP -> ";
    
:foreach service in=$services do={
    add action=add-src-to-address-list address-list=($service->"list") \
        address-list-timeout=none-static chain=$chainName comment=\
        ($service->"comment") dst-port=($service->"port") protocol=($service->"protocol");
}

add action=add-src-to-address-list address-list=lure_input_tcp \
    address-list-timeout=none-static chain=$chainName comment=\
    "lure input TCP" protocol=tcp;
add action=add-src-to-address-list address-list=lure_input_udp \
    address-list-timeout=none-static chain=$chainName comment=\
    "lure input UDP" protocol=udp;


File: /sources\lure-firewall\lure-geoip.rsc
#Version: 3.0 alpha.
#Fecha: 22-12-2019.
#RouterOS 6.43 y superior.
#Comentario: Se introduce el calculo del delay para el API, 45 consultas por minuto.

#TODO-BEGIN

:local getCurrentTimestamp;
:local getCurrentTimestamp do={
    :local date [/system clock get date];
    :local months ({"jan"=1;"feb"=2;"mar"=3;"apr"=4;"may"=5;"jun"=6;"jul"=7;"aug"=8;"sep"=9;"oct"=10;"nov"=11;"dec"=12});
    :local daysForMonths ({31;28;31;30;31;30;31;31;30;31;30;31});
    
    :local day [:tonum [:pick $date 4 6]];
    :local month ($months->[:pick $date 0 3]);
    :local year [:tonum [:pick $date 7 11]];
    
    :local leapDays (($year - 1968) / 4);
    
    :if ((($leapDays * 4) + 1968) = $year) do={
        :set leapDays ($leapDays - 1);
        :set ($daysForMonths->1) 29;
    }
    
    :local days ($day - 1);
    
    :if (($month - 1) > 0) do={
        :for index from=0 to=($month - 2) do={
            :set days ($days + ($daysForMonths->($index)));
        }
    }
        
    :local daysForYear 365;
    :local secondsForDay 86400;
    :local gmtOffset [/system clock get gmt-offset];
    
    :local now [/system clock get time];
    :local hour [:tonum [:pick $now 0 2]];
    :local minutes [:tonum [:pick $now 3 5]];
    :local seconds [:tonum [:pick $now 6 8]];

    :local timestamp ((((($year - 1970) * $daysForYear) + $leapDays + $days) * $secondsForDay) + ($hour * 3600) + ($minutes * 60) + seconds);
    
    :if ($gmtOffset <= $secondsForDay) do={
        :set timestamp ($timestamp - $gmtOffset);
    } else={
        :set timestamp ($timestamp + (-$gmtOffset&0x00000000FFFFFFFF));
    }
    
    :return $timestamp;    
}


:local format;
:local format do={
    :local src $1;
    :local length $2;
    :local lengthSrc [:len $src];
    
    :if ($lengthSrc < ($length)) do={
        :for index from=$lengthSrc to=($length - 1) do={
            :set src ($src . " ");
        }
    } else={
        :set src ([:pick $src 0 ($length - 1)] . " ");
    }
    :return $src;
}


:local globalBlackList "lure_input_blacklist";
:local tcpBlackList "lure_input_tcp";
:local udpBlackList "lure_input_udp";

:local dstAddressQueryList ([]);
:local dstAddressQueryResult ([]);
:local idx 0;
:local request 0;
:local timeStamp [$getCurrentTimestamp];
:local blackList [/ip firewall address-list find list="$globalBlackList"];

:put "";
:put ("Cantidad de IPs en la black list: " . [:len $blackList]);
:put "";
:put ([$format "#" 5] . [$format "SRC. ADDRESS" 22] . [$format "PROTO" 20] \
. [$format "COUNTRY" 9] . [$format "COUNTRY NAME" 25] . [$format "AS" 10] . [$format "AS NAME" 30]);

:foreach id in=$blackList do={
    :local connection [/ip firewall address-list get $id];
    :local dstAddress ($connection->"address");
    :local srcAddress ($connection->"address");
    :local protocol "";
    
    :if ([:len [/ip firewall address-list find list="$tcpBlackList" address="$srcAddress"]] > 0) do={
        :set protocol "TCP,";
    }
    
    :if ([:len [/ip firewall address-list find list="$udpBlackList" address="$srcAddress"]] > 0) do={
        :set protocol "$($protocol)UDP,";
    }
    
    :if ([:len $protocol] > 0) do={
        :set protocol [:pick $protocol 0 ([:len $protocol]-1)];
    }
    
    :if (([:len $dstAddress] > 0) and ([:len $srcAddress] > 0)) do={
        :local data;
        :local dnsCache ([]);
        :local dnsData;
        
        :local dstIp $dstAddress;
        :local doubleDot [:find $dstIp ":"];
        :if ( $doubleDot > 0) do={ 
            :set dstIp [:pick $dstIp 0 $doubleDot];
        }
        
        :local indexFind [:find $dstAddressQueryList $dstIp];
        :if (!($indexFind >=0)) do={
        
            
            :foreach idDns in=[/ip dns cache all find data=$dstIp] do={
                :set dnsData [/ip dns cache all get $idDns];
                :set dnsCache ($dnsCache, {$dnsData});
                
                :foreach oIdDns in=[/ip dns cache all find data=($dnsData->"name")] do={
                    :set dnsData [/ip dns cache all get $oIdDns];
                    :set dnsCache ($dnsCache, {$dnsData});
                }
            }
        
        
            :local lUrl "http://ip-api.com/csv/$dstIp?fields=status,message,country,countryCode,as,asname,query";
            :local result;
            
            
            do {
                :local isPrivate  ((10.0.0.0 = ($dstIp&255.0.0.0)) or (172.16.0.0 = ($dstIp&255.240.0.0)) or  (192.168.0.0 = ($dstIp&255.255.0.0)));
                :local isReserved ((0.0.0.0 = ($dstIp&255.0.0.0)) or (127.0.0.0 = ($dstIp&255.0.0.0)) or (169.254.0.0 = ($dstIp&255.255.0.0)) \
                or (224.0.0.0 = ($dstIp&240.0.0.0)) or (240.0.0.0 = ($dstIp&240.0.0.0)));
                :if ($isPrivate or $isReserved) do={
                    :if ($isPrivate) do={
                        :set data {"country"=""; "countryCode"="PRIVATE"; "as"=""; "asname"=""; "dnsCache"=($dnsCache)};
                    } else={
                        :set data {"country"=""; "countryCode"="RESERVED"; "as"=""; "asname"=""; "dnsCache"=($dnsCache)};
                    }
                } else={
                    :set result [/tool fetch url=$lUrl mode=http as-value output=user];
                    :set request ($request + 1);
                    :if ($request >= 45) do={
                        :set request 0;
                        :local timeToDelay ([$getCurrentTimestamp] - $timeStamp);
                        :if ($timeToDelay < 65) do={
                            :delay (65 - $timeToDelay);
                        }
                        :set timeStamp [$getCurrentTimestamp];
                    }
                    
                    :local arrayResult [:toarray ($result->"data")];
                    
                    :if ([:typeof $arrayResult] = "array") do={
                        :if ([:pick $arrayResult 0] = "success") do={
                            :local as (($arrayResult->3) . " ");
                            :set as [:pick $as 0 [:find $as " "]];
                            :set data {"country"=($arrayResult->1); "countryCode"=($arrayResult->2); "as"=$as; "asname"=($arrayResult->4); "dnsCache"=($dnsCache)};
                        }
                    }
                }
                :set dstAddressQueryList ($dstAddressQueryList, $dstIp);
                :set dstAddressQueryResult ($dstAddressQueryResult, {$data});
            } on-error={
                :put ([$format $dstIp 16] . " - ERROR");
            }
        } else={
            :set data ($dstAddressQueryResult->$indexFind);
            :set dnsCache ($data->"dnsCache");
        }

        :set idx ($idx + 1);
        :put ([$format $idx 5] . [$format $srcAddress 22] . [$format $protocol 20] \
        . [$format ($data->"countryCode") 9] . [$format ($data->"country") 25] . [$format ($data->"as") 10] . [$format ($data->"asname") 30]);
        :if ([:len $dnsCache] > 0) do={
            :foreach dnsData in=$dnsCache do={
                :put ([$format ("     type: " . ($dnsData->"type")) 27] . [$format ("name: " . ($dnsData->"name")) 50]);
            }
            :put "";
        }
    }
}

#TODO-END

File: /sources\lure-firewall\lure-services.rsc
:global services;
:set services \
{\
    {\
        "port"="21";\
        "protocol"="tcp";\
        "list"="lure_ftp";\
        "comment"="Ftp"\
    };\
    {\
        "port"="22";\
        "protocol"="tcp";\
        "list"="lure_ssh";\
        "comment"="Secure Shell"\
    };\
    {\
        "port"="23";\
        "protocol"="tcp";\
        "list"="lure_telnet";\
        "comment"="Telnet"\
    };\
    {\
        "port"="53";\
        "protocol"="tcp";\
        "list"="lure_dns";\
        "comment"="Dns"\
    };\
    {\
        "port"="3389";\
        "protocol"="tcp";\
        "list"="lure_microsoft_rdp";\
        "comment"="Microsoft RDP"\
    };\
    {\
        "port"="8291";\
        "protocol"="tcp";\
        "list"="lure_mikrotik_winbox";\
        "comment"="Mikrotik Winbox"\
    };\
    {\
        "port"="8728, 8729";\
        "protocol"="tcp";\
        "list"="lure_mikrotik_api";\
        "comment"="Mikrotik Api"\
    };\
    {\
        "port"="53";\
        "protocol"="udp";\
        "list"="lure_dns";\
        "comment"="Dns"\
    };\
    {\
        "port"="2000";\
        "protocol"="udp";\
        "list"="lure_mikrotik_bandwith";\
        "comment"="Mikrotik Bandwith"\
    }\
};

File: /sources\lure-firewall\lureinputfilter - copia - copia.rsc
#Esta regla debe ir luego de las reglas INPUT que si aceptas
#Procesa los INPUT desde las lita de interface WAN y que no este en la lista
#secure_list
#Agrega a la lista secure_list tu red local.

:global services;
:set services [:toarray ""];

#Function registerService
#   Param:
#   $1: port
#   $2: protocol
#   $3: list
#   $4: comment

:global registerService;
:set registerService do={
    :global services;
    :local length [:len $services];
    :set ($services->$length) {"port"=$1;"protocol"=$2;"list"=$3;"comment"=$4};
}

$registerService 21 "tcp" "lure_ftp" "Ftp";
$registerService 22 "tcp" "lure_ssh" "Secure Shell";
$registerService 23 "tcp" "lure_telnet" "Telnet";

:put "";
:global services;
:for i from=1 to=100 do={
    /system/script/run test-array02;
    :local length [:len $services];
    :put "Pasada ($i), longitud del arreglo: $length";
}

:put "";
:put "Datos en el arreglo...";
:put "";
:foreach service in=$services do={
    :put $service;
}

:put "";
:local length [:len $services];
:put "Longitud esperada del arreglo: 3, longitud final del arreglo: $length";
:put "";






:local chainName "lure_input";

/ip firewall filter

remove numbers=[find jump-target=$chainName];

add action=jump chain=input comment="lure input" connection-state=new \
    in-interface-list=WAN jump-target=$chainName src-address-list=\
    !secure_list


:local services;
:set services \
{\
    {\
        "port"="21";\
        "protocol"="tcp";\
        "list"="lure_ftp";\
        "comment"="Ftp"\
    };\
    {\
        "port"="22";\
        "protocol"="tcp";\
        "list"="lure_ssh";\
        "comment"="Secure Shell"\
    };\
    {\
        "port"="23";\
        "protocol"="tcp";\
        "list"="lure_telnet";\
        "comment"="Telnet"\
    };\
    {\
        "port"="53";\
        "protocol"="tcp";\
        "list"="lure_dns";\
        "comment"="Dns"\
    };\
    {\
        "port"="3389";\
        "protocol"="tcp";\
        "list"="lure_microsoft_rdp";\
        "comment"="Microsoft RDP"\
    };\
    {\
        "port"="8291";\
        "protocol"="tcp";\
        "list"="lure_mikrotik_winbox";\
        "comment"="Mikrotik Winbox"\
    };\
    {\
        "port"="8728, 8729";\
        "protocol"="tcp";\
        "list"="lure_mikrotik_api";\
        "comment"="Mikrotik Api"\
    };\
    {\
        "port"="53";\
        "protocol"="udp";\
        "list"="lure_dns";\
        "comment"="Dns"\
    };\
    {\
        "port"="2000";\
        "protocol"="udp";\
        "list"="lure_mikrotik_bandwith";\
        "comment"="Mikrotik Bandwith"\
    }\
};

remove numbers=[find chain=$chainName];

add action=tarpit chain=$chainName comment="lure input BLACKLIST TCP TARPIT" \
    protocol=tcp src-address-list=lure_input_blacklist;
    
add action=drop chain=$chainName comment="lure input BLACKLIST DROP" \
    src-address-list=lure_input_blacklist;

add action=add-src-to-address-list address-list=lure_input_blacklist \
    address-list-timeout=none-static chain=$chainName comment=\
    "lure input BLACKLIST" log=yes log-prefix="LURE DROP -> ";
    
:foreach service in=$services do={
    add action=add-src-to-address-list address-list=($service->"list") \
        address-list-timeout=none-static chain=$chainName comment=\
        ($service->"comment") dst-port=($service->"port") protocol=($service->"protocol");
}

add action=add-src-to-address-list address-list=lure_input_tcp \
    address-list-timeout=none-static chain=$chainName comment=\
    "lure input TCP" protocol=tcp;
add action=add-src-to-address-list address-list=lure_input_udp \
    address-list-timeout=none-static chain=$chainName comment=\
    "lure input UDP" protocol=udp;


File: /sources\lure-firewall\lureinputfilter - copia.rsc
#Esta regla debe ir luego de las reglas INPUT que si aceptas
#Procesa los INPUT desde las lita de interface WAN y que no este en la lista
#secure_list
#Agrega a la lista secure_list tu red local.


:global bu ({});
:global i 0;
:global j 0;
:do {
    :set ($bu->$i) 1024;
    :set i ($i + 1);
    :set j ($j + 1);
    :if ($j >= 1024) do={
        :put "INDEX: $i";
        :set j 0;
    }
} while=(true);


:global services;
:set services ({});

#Function registerService
#   Param:
#   $1: port
#   $2: protocol
#   $3: list
#   $4: comment

:global registerService;
:set registerService do={
    :global services;
    :local length [:len $services];
    :set ($services->$length) {"port"=$1;"protocol"=$2;"list"=$3;"comment"=$4};
}

$registerService 21 "tcp" "lure_ftp" "Ftp";
$registerService 22 "tcp" "lure_ssh" "Secure Shell";
$registerService 23 "tcp" "lure_telnet" "Telnet";

:foreach service in=$services do={
    :put $service;
}






:local chainName "lure_input";

/ip firewall filter

remove numbers=[find jump-target=$chainName];

add action=jump chain=input comment="lure input" connection-state=new \
    in-interface-list=WAN jump-target=$chainName src-address-list=\
    !secure_list


:local services;
:set services \
{\
    {\
        "port"="21";\
        "protocol"="tcp";\
        "list"="lure_ftp";\
        "comment"="Ftp"\
    };\
    {\
        "port"="22";\
        "protocol"="tcp";\
        "list"="lure_ssh";\
        "comment"="Secure Shell"\
    };\
    {\
        "port"="23";\
        "protocol"="tcp";\
        "list"="lure_telnet";\
        "comment"="Telnet"\
    };\
    {\
        "port"="53";\
        "protocol"="tcp";\
        "list"="lure_dns";\
        "comment"="Dns"\
    };\
    {\
        "port"="3389";\
        "protocol"="tcp";\
        "list"="lure_microsoft_rdp";\
        "comment"="Microsoft RDP"\
    };\
    {\
        "port"="8291";\
        "protocol"="tcp";\
        "list"="lure_mikrotik_winbox";\
        "comment"="Mikrotik Winbox"\
    };\
    {\
        "port"="8728, 8729";\
        "protocol"="tcp";\
        "list"="lure_mikrotik_api";\
        "comment"="Mikrotik Api"\
    };\
    {\
        "port"="53";\
        "protocol"="udp";\
        "list"="lure_dns";\
        "comment"="Dns"\
    };\
    {\
        "port"="2000";\
        "protocol"="udp";\
        "list"="lure_mikrotik_bandwith";\
        "comment"="Mikrotik Bandwith"\
    }\
};

remove numbers=[find chain=$chainName];

add action=tarpit chain=$chainName comment="lure input BLACKLIST TCP TARPIT" \
    protocol=tcp src-address-list=lure_input_blacklist;
    
add action=drop chain=$chainName comment="lure input BLACKLIST DROP" \
    src-address-list=lure_input_blacklist;

add action=add-src-to-address-list address-list=lure_input_blacklist \
    address-list-timeout=none-static chain=$chainName comment=\
    "lure input BLACKLIST" log=yes log-prefix="LURE DROP -> ";
    
:foreach service in=$services do={
    add action=add-src-to-address-list address-list=($service->"list") \
        address-list-timeout=none-static chain=$chainName comment=\
        ($service->"comment") dst-port=($service->"port") protocol=($service->"protocol");
}

add action=add-src-to-address-list address-list=lure_input_tcp \
    address-list-timeout=none-static chain=$chainName comment=\
    "lure input TCP" protocol=tcp;
add action=add-src-to-address-list address-list=lure_input_udp \
    address-list-timeout=none-static chain=$chainName comment=\
    "lure input UDP" protocol=udp;


File: /sources\module-arrays.rsc
#Version: 3.0 alpha
#Fecha: 22-08-2017
#RouterOS 6.40 y superior.
#Comentario: 

:global setLastError;
:local lScriptName "module-arrays";

#TODO-BEGIN

:global getInitializedArray;
:global getInitializedArray do={
    :local size $1;
    :local value [:tonum $2];
    :local result ({});
    :for index from=0 to=($size - 1) do={
        :set result ($result , $value);
    }
    :return $result;
}

:global arrayCopy;
:global arrayCopy do={
    :local src $1;
    :local srcPos [:tonum $2];
    :local dest $3;
    :local destPos [:tonum $4];
    :local length [:tonum $5];
    
    :for index from=$srcPos to=($srcPos + $length - 1) do={
        :set ($dest->$destPos) ($src->$index);
        :set destPos ($destPos + 1);
    }
    :return $dest;
}

:global arrayClone;
:global arrayClone do={
    :local src $1;
    :local dest ({});
    :local length [:len $src];
    
    :for index from=0 to=($length - 1) do={
        :set dest ($dest , $src->$index);
    }
    :return $dest;
}

#TODO-END

$setLastError 0 ("$lScriptName cargado.");

File: /sources\module-base32.rsc
#Version: 3.0 alpha
#Fecha: 22-08-2017
#RouterOS 6.40 y superior.
#Comentario: 
#Requiere: module-hex

:global setLastError;
:local lScriptName "module-base32";

#TODO-BEGIN

:global decodeBase32;
:global decodeBase32 do={
    :global CHARTOBYTE;
    
    :local str $1;
    :local strLength [:len $str];
    :local numBytes ((($strLength * 5) + 7) / 8);
    :local result ({});
    :local resultIndex 0;
    :local which 0;
    :local working 0;
    
    :local index 0;
    :local break false;
    :while (($index < $strLength) && (!$break)) do={
        :local val ($CHARTOBYTE->[:pick $str $index]);
        #:put "index: $index";
        #:put "val: $val";
        :if ($val >= 97 && $val <= 122) do={
            :set val ($val - 97);
        } else={
            :if ($val >= 65 && $val <= 90) do={
                :set val ($val - 65);
            } else={
                :if ($val >= 50 && $val <= 55) do={
                    :set val (26 + ($val - 50));
                } else={
                    :if ($val = 61) do={
                        #special case
                        :set which 0;
                        :set break true;
                        #:put "break $break";
                    } else={
                        #Error
                    }                
                }
            }
        }
        
        :if (!$break) do={
            :if ($which = 0) do={
                :set working (($val & 0x1F) << 3);
                :set which 1;        
            } else={
                :if ($which = 1) do={
                    :set working ($working | (($val & 0x1C) >> 2));
                    :set ($result->$resultIndex) $working;
                    :set resultIndex ($resultIndex + 1);
                    :set working (($val & 0x03) << 6);
                    :set which 2;            
                } else={
                    :if ($which = 2) do={
                        :set working ($working | (($val & 0x1F) << 1));
                        :set which 3;                
                    } else={
                        :if ($which = 3) do={
                            :set working ($working | (($val & 0x10) >> 4));
                            :set ($result->$resultIndex) $working;
                            :set resultIndex ($resultIndex + 1);
                            :set working (($val & 0x0F) << 4);
                            :set which 4;                    
                        } else={
                            :if ($which = 4) do={
                                :set working ($working | (($val & 0x1E) >> 1));
                                :set ($result->$resultIndex) $working;
                                :set resultIndex ($resultIndex + 1);
                                :set working (($val & 0x01) << 7);
                                :set which 5;
                            } else={
                                :if ($which = 5) do={
                                    :set working ($working | (($val & 0x1F) << 2));
                                    :set which 6;
                                } else={
                                    :if ($which = 6) do={
                                        :set working ($working | (($val & 0x18) >> 3));
                                        :set ($result->$resultIndex) $working;
                                        :set resultIndex ($resultIndex + 1);
                                        :set working (($val & 0x07) << 5);
                                        :set which 7;                                
                                    } else={
                                        :if ($which = 7) do={
                                            :set working ($working | ($val & 0x1F));
                                            :set ($result->$resultIndex) $working;
                                            :set resultIndex ($resultIndex + 1);
                                            :set which 0;
                                        }                                
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
        :set index ($index + 1);
    }    

    :if ($which != 0) do={
        :set ($result->$resultIndex) $working;
    }
    
    #:put "result";
    #:put $result;
    :return $result;
}

#$decodeBase32 "GEZDGNBVGY======";

#2 50
#7 55
#A 65
#Z 90
#a 97
#z 122
#= 61

#TODO-END

$setLastError 0 ("$lScriptName cargado.");

File: /sources\module-bin.rsc
#Version: 3.0 alpha
#Fecha: 22-08-2017
#RouterOS 6.40 y superior.
#Comentario: 

:global setLastError;
:local lScriptName "module-bin";

#TODO-BEGIN

:global numToBin;
:global numToBin do={
    :local num [:tonum $1];
    :local bin "";
    
    :if ([:typeof $num] = "num") do={
        :if ($num > 0) do={
            :while ($num > 0) do={
                :local bit ($num & 0x0000000000000001);
                :set bin ("$bit$bin");
                :set num ($num >> 1);
            }
        } else={
            :set bin "0";
        }
    }
    :return $bin;
}

#TODO-END

$setLastError 0 ("$lScriptName cargado.");

File: /sources\module-dyndns.rsc
#Version: 3.0 alpha
#Fecha: 22-08-2017
#RouterOS 6.40 y superior.
#Comentario: 

:global setLastError;
:local lScriptName "module-dyndns";

#TODO-BEGIN

:global getFileContents;

#http://checkip.dyndns.com/

#Function resolveHost
#   Param:
#   $1: domain-name
#   $2: server
#   $3: server-port
#
:global resolveHost;
:global resolveHost do={
    :local domainName "domain-name=.";
    :local dnsServer "";
    :local serverPort "";
    
    :if ([:len $1] > 0) do={
        :set domainName "domain-name=$1";
        :if ([:len $2] > 0) do={
            :set dnsServer " server=$2";
            :if ([:len $3] > 0) do={
                :set serverPort " server-port=$3";
            }
        }
    }
    
    :local command [:parse "[:resolve $domainName$dnsServer$serverPort]"];
    :local ip;
    
    do {
        :set ip [$command];
    } on-error={
        :return "0";
    }
    :return [:toip $ip];
};

#Function getInterfaceIP
#   Param:
#   $1: Interface
#   $2: Notation CIRD
#
:global getInterfaceIP;
:global getInterfaceIP do={
    :local lIp;
    :local lCIRD;
    
    :if ([:len $2] > 0) do={
        :set lCIRD $2;
    }
    do {
        :set lIp [/ip address get [find interface=$1] address];
    } on-error={
        :return "0";
    }
    :if (!$lCIRD) do={
        :set $lIp [:pick $lIp 0 [:find $lIp "/"]];
    }
    :return $lIp;
};

#Function getIPFromExternalServer
#   Param:
#   $1: Interface
#
:global getIPFromExternalServer;
:global getIPFromExternalServer do={
	:local onError true;
	:local result;

	:while ($onError) do={
		do {
			:set result [/tool fetch url=http://checkip.dyndns.org/ as-value output=user];
			:set onError false;
		} on-error={
		}
	}
	:local data ($result->"data");
	:return [:pick $data ([:find $data "Current IP Address: " -1] + 20) [:find $data "</body>" -1]];
}

#Function resolvePublicIP
#   Param:
#   $1: Interface
#
#   Resolver ip publica consultando OpenDNS
:global resolvePublicIP;
:global resolvePublicIP do={
    :global resolveHost;
    
    :local listName "RESOLVERS-OPENDNS";
    :local servers [/ip firewall address-list find list=$listName];
    :local ip "0";
     
    :foreach server in=$servers do={
        :local ipServer [:toip [/ip firewall address-list get $server address]];
        :set ip [$resolveHost "myip.opendns.com" $ipServer];
        :if ($ip != "0") do={
            :return [:toip $ip];
        }
    }
    #:return [:toip [:resolve myip.opendns.com server=208.67.222.222]]
}

#TODO-END

$setLastError 0 ("$lScriptName cargado.");

File: /sources\module-functions.rsc
#Version: 3.0 alpha
#Fecha: 22-08-2017
#RouterOS 6.40 y superior.
#Comentario: Funciones de uso general en MSF.

:global setLastError;
:local lScriptName "module-functions";

#TODO-BEGIN

:global NOTHING;

#Function getFileContents
#   Param:
#   $1: File name.
#
:global getFileContents;
:global getFileContents do={
    :local lContents;
    
    do {
        :set lContents [/file get [find name=$1] contents];
    } on-error={
        :return $NOTHING;
    }
    :return $lContents;
}

#Function getNetAddress
#   Param:
#   $1: CIRD address.
#
:global getNetAddress;
:global getNetAddress do={

    :local vAddress $1;
    :local vShift 0;
    :local vAddressLen ([:len $vAddress]);
    :local vIP 0.0.0.0;
    :local vNetAddress 0.0.0.0;
    :local lLocateSlash [:find $vAddress "/"];
    
    :put "lLocateSlash: $lLocateSlash";
    
    :set vIP [:pick $vAddress 0 $lLocateSlash];
    :put "vIP: $vIP";
    
    :set vShift [:pick $vAddress ($lLocateSlash + 1) $vAddressLen];
    :put "vShift: $vShift";

    :for i from=( $vAddressLen - 1) to=0 do={ 
        :if ( [:pick $vAddress $i] = "/") do={ 
            :set vIP [:pick $vAddress 0 $i];
            :set vShift ( [:tonum [:pick $vAddress ($i + 1) ($vAddressLen)]] );
        }
    }
    :set vNetAddress ($vIP & (255.255.255.255 ^ (255.255.255.255 >> $vShift)));
    :return "$vNetAddress/$vShift";
}

#Function isScriptRuning
#   Param:
#   $1: Nombre del script.
#
:global isScriptRuning;
:global isScriptRuning do={
    :local lIsRuning ([:len [/system script job find script=$1]] > 1);
    :return $lIsRuning;
}

#Function createFirewallAddressList
#   Param:
#   $1: Nombre de la lista.
#   $1: Lista de urls.
#
:global createFirewallAddressList;
:global createFirewallAddressList do={
    
    :local vListName $1;
    
    :local vDomainList $2;

    :local vDnsCache [/ip dns cache find];

    :foreach fDns in=$vDnsCache do={
        :local vDnsName [/ip dns cache get $fDns name];
        
        :foreach fDomain in=$vDomainList do={
            :if (([:len $fDomain] > 0)) do={
                :if (([:find $vDnsName $fDomain] >= 0)) do={
                    :local vDnsAddress [/ip dns cache get $fDns address];
                    :local vDnsType [/ip dns cache all get $fDns type];
                    
                    :if ($vDnsType = "A") do={            
                        :if (([:len [/ip firewall address-list find list=$vListName address=$vDnsAddress]] = 0)) do={
                            /ip firewall address-list add address=$vDnsAddress list=$vListName comment=$vDnsName;
                            :log info "Add address: $vDnsName, IP: $vDnsAddress, list: $vListName";
                        }
                    }
                }
            }
        }
    }
}

#TODO-END

$setLastError 0 ("$lScriptName cargado.");

File: /sources\module-geoip.rsc
#Version: 3.0 alpha
#Fecha: 22-08-2017
#RouterOS 6.40 y superior.
#Comentario: 

:global setLastError;
:local lScriptName "module-geoip";

#TODO-BEGIN

:global getGeoIP;
:global getGeoIP do={

    :global getFileContents;
    :global logInfo;
    :global logError;
    :global logWarning;

    :local lIP [:toip $1];
    :local result;
    
    :set result {"ip"="$lIP";\
                 "success"=false;\
                 "countryCode"="";\
                 "country"="";\
                 "msg"=""};
                 
    :local lFetch false;
    :local lUrl "http://ip-api.com/csv/$lIP?fields=status,country,countryCode,message,query";
    :local lFileName "geoip.csv";
    
    do {
        [/tool fetch url=$lUrl mode=http dst-path="/$lFileName"];
        :set lFetch true;
    } on-error={
        $logError $lScritpName ("Error realizando consulta Geo IP");
    }
    
    :if ($lFetch) do={
        :local lContents [$getFileContents $lFileName];
        :if ($lContents = [:nothing]) do={
            :set lContents "Geo IP ERROR: No se pudo obtener el contenido del archivo.";
        } else={
            :set lContents [:toarray $lContents];
            
            :if ([:typeof $lContents] = "array") do={
                :if ([:pick $lContents 0] = "success") do={
                    :set ($result->"success") true;                
                    :set ($result->"country") [:pick $lContents 1];
                    :set ($result->"countryCode") [:pick $lContents 2];
                    :set ($result->"ip") [:pick $lContents 3];
                } else={
                    :set ($result->"success") false;
                    :set ($result->"msg") [:pick $lContents 1];
                    :set ($result->"ip") [:pick $lContents 2];
                }
            } else={
            
            }
        }
    }    
        
    :return $result;    
}

#TODO-END

$setLastError 0 ("$lScriptName cargado.");

File: /sources\module-hex.rsc
#Version: 3.0 alpha
#Fecha: 22-08-2017
#RouterOS 6.40 y superior.
#Comentario: 

:global setLastError;
:local lScriptName "module-hex";

#TODO-BEGIN

:global getHexFromByte;
:global getHexFromByte do={
    :local HEXDIGITS "0123456789ABCDEF";
    :local byte [:tonum $1];
    :local hex "";
    :local index 0;
    
    if ([:typeof $byte] = "num") do={
        :set index (($byte>>4)&0xF);
        :set hex [:pick $HEXDIGITS $index];
        :set index (($byte>>0)&0xF);
        :set hex ($hex . [:pick $HEXDIGITS $index]);
    }
    :return $hex;
}

{
:local hex "";
:local cr "\r\n";
:local function ("{:local CHARBYTE [:toarray \"\"];");
:for i from=0x00 to=0xFF do={
    :set hex [$getHexFromByte $i];
    :set function ($function . $cr . (":set (\$CHARBYTE->\"\\$hex\") 0x$hex;"));
}
:set function ($function . $cr . ":return \$CHARBYTE;}");
:set function [:parse $function];

:global CHARTOBYTE;
:set CHARTOBYTE [$function];
}
global stringToByteArray;
global stringToByteArray do={
    :global CHARTOBYTE;
    :local char "";
    :local result ({});
    :for index from=0 to=([:len $1]-1) do={
        :set char [:pick $1 $index]
        :set result ($result , ($CHARTOBYTE->"$char"));
        #:put ("$char: " . ($CHARTOBYTE->"$char"));
    }
    :return $result;
}

:global printByteArrayToHex;
:global printByteArrayToHex do={
    :global getHexFromByte;
    :local array $1;
    :local str "";
    :local hex "";
    #:put $array;
    :for index from=0 to=([:len $array] - 1) do={
        :set hex [$getHexFromByte ($array->$index)];
        #:put $hex;
        :set str "$str$hex";
    }
    :put $str;
}


#TODO-END

$setLastError 0 ("$lScriptName cargado.");

File: /sources\module-hmac.rsc
#Version: 3.0 alpha
#Fecha: 22-08-2017
#RouterOS 6.40 y superior.
#Comentario: 
#Requiere: module-arrays, module-sha1

:global setLastError;
:local lScriptName "module-hmac";

#TODO-BEGIN

:global hmacSha1;
:global hmacSha1 do={
    :global sha1;
    :global arrayClone;
    :global getInitializedArray;
    #:global printByteArrayToHex;
    
    :local key $1;
    :local data $2;
    :local keyLength [:len $key];
    
    :local blockSize 0x40; #64
    :local opad 0x5C; #92
    :local ipad 0x36; #54
    
    :if ($keyLength > $blockSize) do={
        :set key [$sha1 [$arrayClone $key]];
    }
    
    :if (keyLength < $blockSize) do={
        :for index from=$keyLength to=($blockSize - 1) do={
            :set ($key->$index) 0x0;
        }
    }
    
    :local oKeyPad [$getInitializedArray $blockSize 0];
    :local iKeyPad [$getInitializedArray $blockSize 0];
    
    :for index from=0 to=($blockSize - 1) do={
        :set ($oKeyPad->$index) ($opad ^ ($key->$index));
        :set ($iKeyPad->$index) ($ipad ^ ($key->$index));
    }

    :local iSha ($iKeyPad , $data);
    :local hmacSha [$sha1 $iSha];
    
    :local oSha ($oKeyPad , $hmacSha);
    :set hmacSha [$sha1 $oSha];
    
    #:put "hmacSha";
    #[$printByteArrayToHex $hmacSha];
    
    
    :return $hmacSha;
}

#:global stringToByteArray;

#$hmacSha1 [$stringToByteArray "123456"] [$stringToByteArray "Hola"];

#TODO-END

$setLastError 0 ("$lScriptName cargado.");

File: /sources\module-json.rsc
# -------------------------------- JParseFunctions ---------------------------------------------------
# ------------------------------- fJParsePrint ----------------------------------------------------------------
:global fJParsePrint
:if (!any $fJParsePrint) do={ :global fJParsePrint do={
  :global JParseOut
  :local TempPath
  :global fJParsePrint

  :if ([:len $1] = 0) do={
    :set $1 "\$JParseOut"
    :set $2 $JParseOut
   }
   
  :foreach k,v in=$2 do={
    :if ([:typeof $k] = "str") do={
      :set k "\"$k\""
    }
    :set TempPath ($1. "->" . $k)
    :if ([:typeof $v] = "array") do={
      :if ([:len $v] > 0) do={
        $fJParsePrint $TempPath $v
      } else={
        :put "$TempPath = [] ($[:typeof $v])"
      }
    } else={
        :put "$TempPath = $v ($[:typeof $v])"
    }
  }
}}
# ------------------------------- fJParsePrintVar ----------------------------------------------------------------
:global fJParsePrintVar
:if (!any $fJParsePrintVar) do={ :global fJParsePrintVar do={
  :global JParseOut
  :local TempPath
  :global fJParsePrintVar
  :local fJParsePrintRet ""

  :if ([:len $1] = 0) do={
    :set $1 "\$JParseOut"
    :set $2 $JParseOut
   }
   
  :foreach k,v in=$2 do={
    :if ([:typeof $k] = "str") do={
      :set k "\"$k\""
    }
    :set TempPath ($1. "->" . $k)
    :if ($fJParsePrintRet != "") do={
      :set fJParsePrintRet ($fJParsePrintRet . "\r\n")
    }    
    :if ([:typeof $v] = "array") do={
      :if ([:len $v] > 0) do={
        :set fJParsePrintRet ($fJParsePrintRet . [$fJParsePrintVar $TempPath $v])
      } else={
        :set fJParsePrintRet ($fJParsePrintRet . "$TempPath = [] ($[:typeof $v])")
      }
    } else={
        :set fJParsePrintRet ($fJParsePrintRet . "$TempPath = $v ($[:typeof $v])")
    }
  }
  :return $fJParsePrintRet
}}
# ------------------------------- fJSkipWhitespace ----------------------------------------------------------------
:global fJSkipWhitespace
:if (!any $fJSkipWhitespace) do={ :global fJSkipWhitespace do={
  :global Jpos
  :global JSONIn
  :global Jdebug
  :while ($Jpos < [:len $JSONIn] and ([:pick $JSONIn $Jpos] ~ "[ \r\n\t]")) do={
    :set Jpos ($Jpos + 1)
  }
  :if ($Jdebug) do={:put "fJSkipWhitespace: Jpos=$Jpos Char=$[:pick $JSONIn $Jpos]"}
}}
# -------------------------------- fJParse ---------------------------------------------------------------
:global fJParse
:if (!any $fJParse) do={ :global fJParse do={
  :global Jpos
  :global JSONIn
  :global Jdebug
  :global fJSkipWhitespace
  :local Char

  :if (!$1) do={
    :set Jpos 0
   }
  
  $fJSkipWhitespace
  :set Char [:pick $JSONIn $Jpos]
  :if ($Jdebug) do={:put "fJParse: Jpos=$Jpos Char=$Char"}
  :if ($Char="{") do={
    :set Jpos ($Jpos + 1)
    :global fJParseObject
    :return [$fJParseObject]
  } else={
    :if ($Char="[") do={
      :set Jpos ($Jpos + 1)
      :global fJParseArray
      :return [$fJParseArray]
    } else={
      :if ($Char="\"") do={
        :set Jpos ($Jpos + 1)
        :global fJParseString
        :return [$fJParseString]
      } else={
#        :if ([:pick $JSONIn $Jpos ($Jpos+2)]~"^-\?[0-9]") do={
        :if ($Char~"[eE0-9.+-]") do={
          :global fJParseNumber
          :return [$fJParseNumber]
        } else={

          :if ($Char="n" and [:pick $JSONIn $Jpos ($Jpos+4)]="null") do={
            :set Jpos ($Jpos + 4)
            :return []
          } else={
            :if ($Char="t" and [:pick $JSONIn $Jpos ($Jpos+4)]="true") do={
              :set Jpos ($Jpos + 4)
              :return true
            } else={
              :if ($Char="f" and [:pick $JSONIn $Jpos ($Jpos+5)]="false") do={
                :set Jpos ($Jpos + 5)
                :return false
              } else={
                :put "Err.Raise 8732. No JSON object could be fJParseed"
                :set Jpos ($Jpos + 1)
                :return []
              }
            }
          }
        }
      }
    }
  }
}}

#-------------------------------- fJParseString ---------------------------------------------------------------
:global fJParseString
:if (!any $fJParseString) do={ :global fJParseString do={
  :global Jpos
  :global JSONIn
  :global Jdebug
  :global fUnicodeToUTF8
  :local Char
  :local StartIdx
  :local Char2
  :local TempString ""
  :local UTFCode
  :local Unicode

  :set StartIdx $Jpos
  :set Char [:pick $JSONIn $Jpos]
  :if ($Jdebug) do={:put "fJParseString: Jpos=$Jpos Char=$Char"}
  :while ($Jpos < [:len $JSONIn] and $Char != "\"") do={
    :if ($Char="\\") do={
      :set Char2 [:pick $JSONIn ($Jpos + 1)]
      :if ($Char2 = "u") do={
        :set UTFCode [:tonum "0x$[:pick $JSONIn ($Jpos+2) ($Jpos+6)]"]
        :if ($UTFCode>=0xD800 and $UTFCode<=0xDFFF) do={
# Surrogate pair
          :set Unicode  (($UTFCode & 0x3FF) << 10)
          :set UTFCode [:tonum "0x$[:pick $JSONIn ($Jpos+8) ($Jpos+12)]"]
          :set Unicode ($Unicode | ($UTFCode & 0x3FF) | 0x10000)
          :set TempString ($TempString . [:pick $JSONIn $StartIdx $Jpos] . [$fUnicodeToUTF8 $Unicode])         
          :set Jpos ($Jpos + 12)
        } else= {
# Basic Multilingual Plane (BMP)
          :set Unicode $UTFCode
          :set TempString ($TempString . [:pick $JSONIn $StartIdx $Jpos] . [$fUnicodeToUTF8 $Unicode])
          :set Jpos ($Jpos + 6)
        }
        :set StartIdx $Jpos
        :if ($Jdebug) do={:put "fJParseString Unicode: $Unicode"}
      } else={
        :if ($Char2 ~ "[\\bfnrt\"]") do={
          :if ($Jdebug) do={:put "fJParseString escape: Char+Char2 $Char$Char2"}
          :set TempString ($TempString . [:pick $JSONIn $StartIdx $Jpos] . [[:parse "(\"\\$Char2\")"]])
          :set Jpos ($Jpos + 2)
          :set StartIdx $Jpos
        } else={
          :if ($Char2 = "/") do={
            :if ($Jdebug) do={:put "fJParseString /: Char+Char2 $Char$Char2"}
            :set TempString ($TempString . [:pick $JSONIn $StartIdx $Jpos] . "/")
            :set Jpos ($Jpos + 2)
            :set StartIdx $Jpos
          } else={
            :put "Err.Raise 8732. Invalid escape"
            :set Jpos ($Jpos + 2)
          }
        }
      }
    } else={
      :set Jpos ($Jpos + 1)
    }
    :set Char [:pick $JSONIn $Jpos]
  }
  :set TempString ($TempString . [:pick $JSONIn $StartIdx $Jpos])
  :set Jpos ($Jpos + 1)
  :if ($Jdebug) do={:put "fJParseString: $TempString"}
  :return $TempString
}}

#-------------------------------- fJParseNumber ---------------------------------------------------------------
:global fJParseNumber
:if (!any $fJParseNumber) do={ :global fJParseNumber do={
  :global Jpos
  :local StartIdx
  :global JSONIn
  :global Jdebug
  :local NumberString
  :local Number

  :set StartIdx $Jpos   
  :set Jpos ($Jpos + 1)
  :while ($Jpos < [:len $JSONIn] and [:pick $JSONIn $Jpos]~"[eE0-9.+-]") do={
    :set Jpos ($Jpos + 1)
  }
  :set NumberString [:pick $JSONIn $StartIdx $Jpos]
  :set Number [:tonum $NumberString] 
  :if ([:typeof $Number] = "num") do={
    :if ($Jdebug) do={:put "fJParseNumber: StartIdx=$StartIdx Jpos=$Jpos $Number ($[:typeof $Number])"}
    :return $Number
  } else={
    :if ($Jdebug) do={:put "fJParseNumber: StartIdx=$StartIdx Jpos=$Jpos $NumberString ($[:typeof $NumberString])"}
    :return $NumberString
  }
}}

#-------------------------------- fJParseArray ---------------------------------------------------------------
:global fJParseArray
:if (!any $fJParseArray) do={ :global fJParseArray do={
  :global Jpos
  :global JSONIn
  :global Jdebug
  :global fJParse
  :global fJSkipWhitespace
  :local Value
  :local ParseArrayRet [:toarray ""]
  
  $fJSkipWhitespace    
  :while ($Jpos < [:len $JSONIn] and [:pick $JSONIn $Jpos]!= "]") do={
    :set Value [$fJParse true]
    :set ($ParseArrayRet->([:len $ParseArrayRet])) $Value
    :if ($Jdebug) do={:put "fJParseArray: Value="; :put $Value}
    $fJSkipWhitespace
    :if ([:pick $JSONIn $Jpos] = ",") do={
      :set Jpos ($Jpos + 1)
      $fJSkipWhitespace
    }
  }
  :set Jpos ($Jpos + 1)
#  :if ($Jdebug) do={:put "ParseArrayRet: "; :put $ParseArrayRet}
  :return $ParseArrayRet
}}

# -------------------------------- fJParseObject ---------------------------------------------------------------
:global fJParseObject
:if (!any $fJParseObject) do={ :global fJParseObject do={
  :global Jpos
  :global JSONIn
  :global Jdebug
  :global fJSkipWhitespace
  :global fJParseString
  :global fJParse
# Syntax :local ParseObjectRet ({}) don't work in recursive call, use [:toarray ""] for empty array!!!
  :local ParseObjectRet [:toarray ""]
  :local Key
  :local Value
  :local ExitDo false
  
  $fJSkipWhitespace
  :while ($Jpos < [:len $JSONIn] and [:pick $JSONIn $Jpos]!="}" and !$ExitDo) do={
    :if ([:pick $JSONIn $Jpos]!="\"") do={
      :put "Err.Raise 8732. Expecting property name"
      :set ExitDo true
    } else={
      :set Jpos ($Jpos + 1)
      :set Key [$fJParseString]
      $fJSkipWhitespace
      :if ([:pick $JSONIn $Jpos] != ":") do={
        :put "Err.Raise 8732. Expecting : delimiter"
        :set ExitDo true
      } else={
        :set Jpos ($Jpos + 1)
        :set Value [$fJParse true]
        :set ($ParseObjectRet->$Key) $Value
        :if ($Jdebug) do={:put "fJParseObject: Key=$Key Value="; :put $Value}
        $fJSkipWhitespace
        :if ([:pick $JSONIn $Jpos]=",") do={
          :set Jpos ($Jpos + 1)
          $fJSkipWhitespace
        }
      }
    }
  }
  :set Jpos ($Jpos + 1)
#  :if ($Jdebug) do={:put "ParseObjectRet: "; :put $ParseObjectRet}
  :return $ParseObjectRet
}}

# ------------------- fByteToEscapeChar ----------------------
:global fByteToEscapeChar
:if (!any $fByteToEscapeChar) do={ :global fByteToEscapeChar do={
#  :set $1 [:tonum $1]
  :return [[:parse "(\"\\$[:pick "0123456789ABCDEF" (($1 >> 4) & 0xF)]$[:pick "0123456789ABCDEF" ($1 & 0xF)]\")"]]
}}

# ------------------- fUnicodeToUTF8----------------------
:global fUnicodeToUTF8
:if (!any $fUnicodeToUTF8) do={ :global fUnicodeToUTF8 do={
  :global fByteToEscapeChar
#  :local Ubytes [:tonum $1]
  :local Nbyte
  :local EscapeStr ""

  :if ($1 < 0x80) do={
    :set EscapeStr [$fByteToEscapeChar $1]
  } else={
    :if ($1 < 0x800) do={
      :set Nbyte 2
    } else={  
      :if ($1 < 0x10000) do={
        :set Nbyte 3
      } else={
        :if ($1 < 0x20000) do={
          :set Nbyte 4
        } else={
          :if ($1 < 0x4000000) do={
            :set Nbyte 5
          } else={
            :if ($1 < 0x80000000) do={
              :set Nbyte 6
            }
          }
        }
      }
    }
    :for i from=2 to=$Nbyte do={
      :set EscapeStr ([$fByteToEscapeChar ($1 & 0x3F | 0x80)] . $EscapeStr)
      :set $1 ($1 >> 6)
    }
    :set EscapeStr ([$fByteToEscapeChar (((0xFF00 >> $Nbyte) & 0xFF) | $1)] . $EscapeStr)
  }
  :return $EscapeStr
}}

# ------------------- Load JSON from arg --------------------------------
global JSONLoads
if (!any $JSONLoads) do={ global JSONLoads do={
    global JSONIn $1
    global fJParse
    local ret [$fJParse]
    set JSONIn
    global Jpos; set Jpos
    global Jdebug; if (!$Jdebug) do={set Jdebug}
    return $ret
}}

# ------------------- Load JSON from file --------------------------------
global JSONLoad
if (!any $JSONLoad) do={ global JSONLoad do={
    if ([len [/file find name=$1]] > 0) do={
        global JSONLoads
        return [$JSONLoads [/file get $1 contents]]
    }
}}

# ------------------- Unload JSON parser library ----------------------
global JSONUnload
if (!any $JSONUnload) do={ global JSONUnload do={
    global JSONIn; set JSONIn
    global Jpos; set Jpos
    global Jdebug; set Jdebug
    global fByteToEscapeChar; set fByteToEscapeChar
    global fJParse; set fJParse
    global fJParseArray; set fJParseArray
    global fJParseNumber; set fJParseNumber
    global fJParseObject; set fJParseObject
    global fJParsePrint; set fJParsePrint
    global fJParsePrintVar; set fJParsePrintVar
    global fJParseString; set fJParseString
    global fJSkipWhitespace; set fJSkipWhitespace
    global fUnicodeToUTF8; set fUnicodeToUTF8
    global JSONLoads; set JSONLoads
    global JSONLoad; set JSONLoad
    global JSONUnload; set JSONUnload
}}
# ------------------- End JParseFunctions----------------------


File: /sources\module-pcc-init.rsc
#Version: 3.0 alpha
#Fecha: 22-08-2017
#RouterOS 6.40 y superior.
#Comentario: 

:global setLastError;
:local lScriptName "module-pcc-init";

#TODO-BEGIN
:global gWanInterfaces;

#Function pingQoS
#   Param:
#   $1: Host
#   $2: Interface
#   $3: Routing Table
#
:global pingQoS;
:global pingQoS do={
    :global gPingQoS;
    :local lCount 0;
    
    :for i from=1 to=($gPingQoS->"pingCount") do={
        :set lCount ([/ping $1 interface $2 routing-table $3 count 1 interval ($gPingQoS->"timeout") size ($gPingQoS->"size")] + $lCount);
    }
    :return ($lCount >= $gPingQoS->"umbralCount");
}

:foreach kWan,fInterface in=$gWanInterfaces do={
    [/ip route set [find comment="ID:$kWan"] disabled=yes];
}

#TODO-END

$setLastError 0 ("$lScriptName cargado.");

File: /sources\module-services - copia.rsc
:global services;
:set services ({});

#Function registerService
#   Param:
#   $1: port
#   $2: protocol
#   $3: list
#   $4: comment

:local registerService do={
    :global services;
    
    :local id "$1$2";
    :local service {"port"="$1";"protocol"="$2";"list"="$3";"comment"="$4"};
    :set ($services->($id)) $service;
}

# TCP
$registerService "21"               "tcp"   "lure_ftp"                   "Ftp";
$registerService "22"               "tcp"   "lure_ssh"                   "Secure Shell";
$registerService "23"               "tcp"   "lure_telnet"                "Telnet";
$registerService "53"               "tcp"   "lure_dns"                   "Dns";
$registerService "3389"             "tcp"   "lure_microsoft_rdp"         "Microsoft RDP";
$registerService "8291"             "tcp"   "lure_mikrotik_winbox"       "Mikrotik Winbox";
$registerService "8728,8729"        "tcp"   "lure_mikrotik_api"          "Mikrotik Api";

# UDP
$registerService "53"               "udp"   "lure_dns" "Dns";
$registerService "2000"             "udp"   "lure_mikrotik_bandwith"     "Mikrotik Bandwith";

:set ($services->"load") true;

:foreach service in=$services do={
    :put $service;
}



File: /sources\module-sha1.rsc
#Version: 3.0 alpha
#Fecha: 22-08-2017
#RouterOS 6.40 y superior.
#Comentario: 
#Requiere: module-arrays, 

:global setLastError;
:local lScriptName "module-sha1";

#TODO-BEGIN

:global mod;
:global mod do={
    :local dividendo $1;
    :local divisor $2;
    :local resto ($dividendo / $divisor);
    :set resto ($divisor * $resto);
    :set resto ($dividendo - $resto);
    :return $resto;
}

#Function padTheMessage
#   Param:
#   $1: data (array de byte).
#
:global padTheMessage;
:global padTheMessage do={
    :global mod;
    :global getInitializedArray;

    :local data $1;
    :local origLength [:len $data];
    :local tailLength [$mod $origLength 64];
    :local padLength 0;
    
    :if ((64 - tailLength) >= 9) do={
        :set padLength (64 - $tailLength);
    } else={
        :setb padLength (128 - $tailLength);
    }
    
    :local thePad [$getInitializedArray $padLength 0];
    :set ($thePad->0) 0x80;
    
    :local lengthInBits ($origLength * 8);
    
    :local index 0;
    
    :for cnt from=0 to=7 do={
        :set index ($padLength - 1 - $cnt);
        :set ($thePad->$index) (($lengthInBits >> (8 * cnt)) & 0x000000000000FF);
    }
    
    :return ($data , $thePad);
}

:global rotateLeft;
:global rotateLeft do={
    :local value [:tonum $1];
    :local bits [:tonum $2];
    :return ((($value << $bits) | ($value >> (32 - $bits))) & 0x00000000FFFFFFFF);
}

:global bitInvertion;
:global bitInvertion do={
    :local value [:tonum $1];
    :return (-$value-1&0x00000000FFFFFFFF);
}

:global processTheBlock;
:global processTheBlock do={
    :global getInitializedArray;
    :global rotateLeft;
    :global bitInvertion;

    :local work $1;
    :local H $2;
    :local K $3;
    
    :local temp 0;
    :local A 0;
    :local B 0;
    :local C 0;
    :local D 0;
    :local E 0;
    :local F 0;
    
    :local W [$getInitializedArray 80 0];

    :for outer from=0 to=15 do={
        :set temp 0;
        :for inner from=0 to=3 do={
            :set temp ((($work->($outer * 4 + $inner)) & 0x00000000000000FF) << (24 - $inner * 8));
            :set ($W->$outer) (($W->$outer) | $temp);
        }
    }
    
    :for j from=16 to=79 do={
        :set ($W->$j) [$rotateLeft (($W->($j - 3)) ^ ($W->($j - 8)) ^ ($W->($j - 14)) ^ ($W->($j - 16))) 1];
    }

    :set A ($H->0);
    :set B ($H->1);
    :set C ($H->2);
    :set D ($H->3);
    :set E ($H->4);
    
    :for j from= 0 to=19 do={
        :set F (($B & $C) | ([$bitInvertion $B] & $D));
        :set temp (([$rotateLeft $A 5] + $F + $E + ($K->0) + ($W->$j)) & 0x00000000FFFFFFFF );

        :set E $D;
        :set D $C;
        :set C [$rotateLeft $B 30];
        :set B $A;
        :set A $temp;
    }
    
    :for j from=20 to=39 do={
        :set F ($B ^ $C ^ $D);
        :set temp (([$rotateLeft $A 5] + $F + $E + ($K->1) + ($W->$j)) & 0x00000000FFFFFFFF );

        :set E $D;
        :set D $C;
        :set C [$rotateLeft $B 30];
        :set B $A;
        :set A $temp;
    }
    
    :for j from=40 to=59 do={
        :set F (($B & $C) | ($B & $D) | ($C & $D));
        :set temp (([$rotateLeft $A 5] + $F + $E + ($K->2) + ($W->$j)) & 0x00000000FFFFFFFF );

        :set E $D;
        :set D $C;
        :set C [$rotateLeft $B 30];
        :set B $A;
        :set A $temp;
    }

    :for j from=60 to=79 do={
        :set F ($B ^ $C ^ $D);
        :set temp (([$rotateLeft $A 5] + $F + $E + ($K->3) + ($W->$j)) & 0x00000000FFFFFFFF );

        :set E $D;
        :set D $C;
        :set C [$rotateLeft $B 30];
        :set B $A;
        :set A $temp;
    }

    :set ($H->0) ((($H->0) + $A) & 0x00000000FFFFFFFF);
    :set ($H->1) ((($H->1) + $B) & 0x00000000FFFFFFFF);
    :set ($H->2) ((($H->2) + $C) & 0x00000000FFFFFFFF);
    :set ($H->3) ((($H->3) + $D) & 0x00000000FFFFFFFF);
    :set ($H->4) ((($H->4) + $E) & 0x00000000FFFFFFFF);
        
    :return $H;
}

:global fill;
:global fill do={
    :local value [:tonum $1];
    :local array $2;
    :local off [:tonum $3];
    
    :set ($array->($off + 0)) (($value >> 24) & 0xFF);
    :set ($array->($off + 1)) (($value >> 16) & 0xFF);
    :set ($array->($off + 2)) (($value >> 8) & 0xFF);
    :set ($array->($off + 3)) (($value >> 0) & 0xFF);
    
    :return $array;
}

:global sha1;
:global sha1 do={
    :global mod;
    :global getInitializedArray;
    :global padTheMessage;
    :global arrayCopy;
    :global arrayClone;
    :global processTheBlock;
    :global fill;
    
    :local data $1;
    :local paddedData [$padTheMessage $data];
    :local paddedLength [:len $paddedData];

    :local H {0x67452301; 0xEFCDAB89; 0x98BADCFE; 0x10325476; 0xC3D2E1F0};
    :local K {0x5A827999; 0x6ED9EBA1; 0x8F1BBCDC; 0xCA62C1D6};

    :local paddedMod [$mod $paddedLength 64];
    :if ($paddedMod != 0) do={
        #Error
        :return ({});
    }
    
    :local passesReq ($paddedLength / 64);
    :local work [$getInitializedArray 64 0];
    
    :for passCntr from=0 to=($passesReq - 1) do={
        :set work [$arrayCopy $paddedData (64 * $passCntr) $work 0 64];
        :set H [$processTheBlock $work [$arrayClone $H] $K];
    }
    
    :local digest [$getInitializedArray 20 0];    

    :set digest [$fill ($H->0) $digest 0];
    :set digest [$fill ($H->1) $digest 4];
    :set digest [$fill ($H->2) $digest 8];
    :set digest [$fill ($H->3) $digest 12];
    :set digest [$fill ($H->4) $digest 16];
    
    :return $digest;
}

#TODO-END

$setLastError 0 ("$lScriptName cargado.");

File: /sources\module-time.rsc
#Version: 3.0 alpha
#Fecha: 22-08-2017
#RouterOS 6.40 y superior.
#Comentario: 

:global setLastError;
:local lScriptName "module-time";

#TODO-BEGIN

#Function getTimestamp
#   Param:
#   $1: Date.
#   $2: Time.
#   $3: Gmt.
#
:global getTimestamp;
:global getTimestamp do={
    :local date $1;
    :local months ({"jan"=1;"feb"=2;"mar"=3;"apr"=4;"may"=5;"jun"=6;"jul"=7;"aug"=8;"sep"=9;"oct"=10;"nov"=11;"dec"=12});
    :local daysForMonths ({31;28;31;30;31;30;31;31;30;31;30;31});
    
    :local day [:tonum [:pick $date 4 6]];
    :local month ($months->[:pick $date 0 3]);
    :local year [:tonum [:pick $date 7 11]];
    
    :local leapDays (($year - 1968) / 4);
    
    :if ((($leapDays * 4) + 1968) = $year) do={
        :set leapDays ($leapDays - 1);
        :set ($daysForMonths->1) 29;
    }
    
    :local days ($day - 1);
    
    :if (($month - 1) > 0) do={
        :for index from=0 to=($month - 2) do={
            :set days ($days + ($daysForMonths->($index)));
        }
    }
        
    :local now $2;
    :local hour [:tonum [:pick $now 0 2]];
    :local minutes [:tonum [:pick $now 3 5]];
    :local seconds [:tonum [:pick $now 6 8]];
    
    :local daysForYear 365;
    :local secondsForDay 86400;
    :local gmtOffset $3;

    :local timestamp ((((($year - 1970) * $daysForYear) + $leapDays + $days) * $secondsForDay) + ($hour * 3600) + ($minutes * 60) + seconds);
    
    :if ($gmtOffset <= $secondsForDay) do={
        #+
        :set timestamp ($timestamp - $gmtOffset);
    } else={
        #-
        :set timestamp ($timestamp + (-$gmtOffset&0x00000000FFFFFFFF));
    }
    
    :return $timestamp;    
}

:global getCurrentTimestamp;
:global getCurrentTimestamp do={
    :global getTimestamp;
    :return [$getTimestamp [/system clock get date] [/system clock get time] [/system clock get gmt-offset]];
}

:global getDateTimeFromTimestamp;
:global getDateTimeFromTimestamp do={
    
}


{
    :local timestamp 1602476374;
    :local hour (1602476374 / 3600);
    :local sec (1602476374 % 3600);
    :local min ($sec / 60);
    :set sec ($sec % 60);
    
    :local day ($hour / 24);
    :set hour ($hour % 24);
    
    :local year (($day / 365) + 1970);
    :set day ($day % 365);
    
    :local dayMonth {31;28;31;30;31;30;31;31;30;31;30;31};
    :local month 1;
    :foreach m in=$dayMonth do={
        :if (($day - $m) > 0) do={
            :set day ($day - $m);
            :set month ($month + 1);
        }
    }

    :local leapDays (($year - 1968) / 4);
    
    :set ($day - )
    

    :put "timestamp: $timestamp";
    :put "Time: $leapDays $day/$month/$year $hour:$min:$sec";
}

#TODO-END

$setLastError 0 ("$lScriptName cargado.");

File: /sources\module-totp.rsc
#Version: 3.0 alpha
#Fecha: 23-03-2018
#RouterOS 6.41 y superior.
#Comentario: Para el funcionamiento adecuado se debe sincronizar la hora mediante el cliente ntp.
#            Instalar el paquete NTP y activar el cliente.
#            Verificar si no se tiene bloquedo el puerto UDP 123, de ser necesario para el funcionamiento del NTP client agregar la regla NAT:
#            add action=masquerade chain=srcnat comment="NTP NAT" protocol=udp src-port=123 to-ports=10000-20000
#            esta regla debeb tener prioridad sobre las demas src NAT.
#Requiere: module-arrays, module-base32, module-hmac

:global setLastError;
:local lScriptName "module-totp";

#TODO-BEGIN

:global generateTOTP;
:global generateTOTP do={
    :global decodeBase32;
    :global getInitializedArray;
    :global hmacSha1;
    :global mod;
    :global arrayClone;
    
    :local base32Secret $1;
    :local timeSeconds [:tonum $2];
    :local timeStepSeconds [:tonum $3];
    
    :local key [$decodeBase32 $base32Secret];
    :local data [$getInitializedArray 8 0];
    :local value ($timeSeconds / $timeStepSeconds);

    :local index 7;
    
    :while (($index >= 0) && ($value > 0)) do={
        :set ($data->$index) ($value & 0xFF);
        :set index ($index - 1);
        :set value ($value >> 8);
    }    
    
    :local hash [$hmacSha1 [$arrayClone $key] [$arrayClone $data]];
    
    :local offset (($hash->([:len $hash] - 1)) & 0xF);

    :local truncatedHash 0;
    
    :for index from=$offset to=($offset + 3) do={
        :set truncatedHash ($truncatedHash << 8);
        :set truncatedHash ($truncatedHash | (($hash->$index) & 0xFF));
    }

    :set truncatedHash ($truncatedHash & 0x7FFFFFFF);
    :set truncatedHash [$mod $truncatedHash 1000000];
    
    :local code [:tostr $truncatedHash];
    
    :while ([:len $code] < 6) do={
        :set code "0$code";
    }
    
    :return $code;
}

#:global getCurrentTimestamp;

#:put [$generateTOTP "JKNHS6PZ37WYDBR2NWDLN36L4H7QGLAA" [$getCurrentTimestamp] 30];

#TODO-END

$setLastError 0 ("$lScriptName cargado.");

File: /sources\msf-install.rsc
#Version: 3.0 alpha
#Fecha: 25-03-2018
#RouterOS 6.40 y superior.
#Comentario: Instalacion de MSF.

#Array lastError
#   Descripcion: Estructura para el paso de errores entre ejecucion de scripts en MSF.
#   Keys:
#       code: Codigo de error.
#       msg: Mensaje de error.
:global lastError;
:set lastError {"code"=0; "msg"=""};

#Function setLastError
#   Descripcion: Establece los valores para el array lastError.
#   Param:
#       $1: Codigo de error.
#       $2: Mensaje de error.
#   Return:
:global setLastError do={
    :global lastError;
    :set ($lastError->"code") $1;
    :set ($lastError->"msg") "$2 (codigo $1).";
}

#Function loadScript
#   Descripcion: Carga un script de configuracion.
#   Param:
#      $1: nombre del script.
#
:global loadScript do={
    :global isEmptyArray;
    :global setLastError;
    :global lastError;
    :local lScriptId [/system script find name=$1];
    
    $setLastError 1 ("Cargando $1...");
    :if (!([$isEmptyArray $lScriptId])) do={
        do {
            [/system script run $lScriptId];
            :if (($lastError->"code") != 0) do={
                $setLastError 2 ("No se pudo cargar $1");
            }
        } on-error={
            $setLastError 3 ("Ejecutando $1");
        }
    } else={
        $setLastError 4 ("No se ha instalado $1");
    }
    :return ($lastError->"code");
}

do {
#TODO-BEGIN

:local files [/file find where name~"msf/"];

:foreach id in=$files do={
    :local f [/file get $id];
    :local name ($f->"name");
    :set name [:pick $name ([:find $name "/"] + 1) [:len $name]];
    :set name [:pick $name 0 [:find $name "."]];
    :put "Instalando $name...";
    /system script add name=$name source=($f->"contents");
}

#:local lScriptName "init";
#:local lConfigName "config-init";

#:local lErrorCode [$loadScript $lConfigName];

#:if ($lErrorCode != 0) do={
#    $logError $lScriptName ($lastError->"msg");
#    :return $lErrorCode;
#} else={
#    $logInfo $lScriptName ($lastError->"msg");
#}

#TODO-END

    :put "$lScriptName MSF instalado.";
} on-error={
    :put "$lScriptName ERROR instalando MSF.";
}

File: /sources\script-dyndns.rsc
#Version: 3.0 alpha
#Fecha: 22-08-2017
#RouterOS 6.40 y superior.
#Comentario:

:global isScriptRuning;
:global setScriptStartRun;
:global setScriptEndRun;
:global logInfo;
:global logError;
:global logWarning;
:local lScritpName "script-dyndns";

:if ([$isScriptRuning $lScritpName]) do={
    $logWarning $lScritpName "Script corriendo.";
    return 255;
}

$setScriptStartRun $lScritpName;

#TODO-BEGIN

:global getFileContents;
:global gDynDNS;
:global getInterfaceIP;
:global resolveHost;

:local lLocalIp [$getInterfaceIP ($gDynDNS->"interface")];

:if ($lLocalIp != "0") do={
    :local lRemoteIP [$resolveHost ($gDynDNS->"host")];
    
    :if ($lRemoteIP != "0") do={
        :if ($lLocalIp != $lRemoteIP) do={
            $logInfo $lScritpName ("IP remota $lRemoteIP");
            $logInfo $lScritpName ("IP local: $lLocalIp");
            $logInfo $lScritpName ("Se necesita actualizar la IP, enviando actualizacion...!");
            
            :local lFetch false;
            :local lPath ("/nic/update?hostname=" . ($gDynDNS->"host") . "&myip=$lLocalIp&wildcard=NOCHG&mx=NOCHG&backmx=NOCHG");
            :local lFileName ("DynDNS." . ($gDynDNS->"host"));
            
            
            do {
                [/tool fetch address=members.dyndns.org src-path=$lPath mode=http user=($gDynDNS->"user") password=($gDynDNS->"password") dst-path="/$lFileName"];
                :set lFetch true;
            } on-error={
                $logError $lScritpName ("No se pudo enviar la actualizacion.");
            }
            :if ($lFetch) do={
                :local lContents [$getFileContents $lFileName];
                :if ($lContents = [:nothing]) do={
                    :set lContents "DynDNS ERROR: No se pudo obtener el contenido del archivo.";
                }
                :if ($lContents~"good") do={
                    $logInfo $lScritpName ("Resultado de la actualizacion $lContents");
                } else={
                    $logError $lScritpName ("Resultado de la actualizacion $lContents");
                }                
            }
        } else={
            $logInfo $lScritpName ("No se necesita realizar ningun cambio, IP: $lLocalIp");
        }
    } else={
        $logError $lScritpName ("No se pudo resolver el nombre de dominio " . ($gDynDNS->"host") . ".");
    }

} else={
    $logError $lScritpName ("No existe IP en interface " . ($gDynDNS->"interface") . ".");
}

#:delay 1
#:global str [/file find name="DynDNS.$ddnshost"];
#/file remove $str
#:global ipddns $ipfresh

#TODO-END

$setScriptEndRun $lScritpName;


File: /sources\script-ovpn-dalejos.rsc
#Version: 3.0 alpha
#Fecha: 22-08-2017
#RouterOS 6.40 y superior.
#Comentario:

:global isScriptRuning;
:global setScriptStartRun;
:global setScriptEndRun;
:global logInfo;
:global logError;
:global logWarning;
:local lScritpName "script-ovpn-dalejos";

:if ([$isScriptRuning $lScritpName]) do={
    $logWarning $lScritpName "Script corriendo.";
    return 255;
}

$setScriptStartRun $lScritpName;

#TODO-BEGIN
:global generateTOTP;
:global getCurrentTimestamp;

:local pass [$generateTOTP "JKNHS6PZ37WYDBR2NWDLN36L4H7QGLAA" [$getCurrentTimestamp] 120];

/ppp secret set dalejos password=$pass;

#TODO-END

$setScriptEndRun $lScritpName;


File: /sources\script-pcc-qos-wan.rsc
#Version: 3.0 alpha
#Fecha: 22-08-2017
#RouterOS 6.40 y superior.
#Comentario:

:global isScriptRuning;
:global setScriptStartRun;
:global setScriptEndRun;
:global logInfo;
:global logError;
:global logWarning;
:local lScritpName "script-pcc-qos-wan";

:if ([$isScriptRuning $lScritpName]) do={
    $logWarning $lScritpName "Script corriendo.";
    return 255;
}

$setScriptStartRun $lScritpName;

#TODO-BEGIN

:global gWanInterfaces;
:global getNetAddress;
:global gPingHost;
:global pingQoS;

:foreach kWan,fInterface in=$gWanInterfaces do={
    
    :local lGateway ($fInterface->"gateway");
    :local lAddress;
    
    $logInfo $lScritpName ("Chequeando interface $kWan");
    
    :if ($fInterface->"dhcp") do={
        :local lDhcpId [/ip dhcp-client find interface=$kWan];
        :if ([:len $lDhcpId] > 0) do={
            :set lGateway [/ip dhcp-client get $lDhcpId gateway];
            :set lAddress [/ip dhcp-client get $lDhcpId address];
        }
    } else={
        :set lAddress [/ip address get [find interface=$kWan] address];
    }
    
    :set lGateway [:toip $lGateway];
    
    :if ([:len $lGateway] > 0) do={
        :local lQoS false;
        $logInfo $lScritpName ("$kWan gateway: $lGateway");
        [/ip route set [find comment="ID:$kWan"] gateway="$lGateway%$kWan"];
        
        :local lNetAddress [$getNetAddress $lAddress]
        [/ip firewall mangle set [find comment="ID:$kWan"] dst-address=$lNetAddress];
        
        :if ( !($fInterface->"enableRouting")) do={
            $logInfo $lScritpName ("Iniciando ping al gateway $lGateway...");
            :set lQoS ([$pingQoS $lGateway $kWan "main"]);
            $logInfo $lScritpName ("QoS: $lQoS");
            :if ($lQoS) do={
                [/ip route set [find comment="ID:$kWan"] disabled=no];
                :delay 3s;
                #Revisar para actializar
                #:foreach fHost in=$gPingHost do={
                #    :set lQoS ([$pingQoS $fHost $kWan ($fInterface->"RoutingMark")]);
                #}
                $logInfo $lScritpName ("Iniciando ping a 8.8.8.8...");
                :set lQoS ([$pingQoS "8.8.8.8" $kWan ($fInterface->"routingMark")]);
                $logInfo $lScritpName ("QoS: $lQoS");
                :if ($lQoS) do={
                    :set ($fInterface->"enableRouting") true;
                } else={
                    [/ip route set [find comment="ID:$kWan"] disabled=yes];
                }
            }
        } else={
            $logInfo $lScritpName ("Iniciando ping a 8.8.8.8...");
            :set lQoS ([$pingQoS "8.8.8.8" $kWan ($fInterface->"routingMark")]);
            $logInfo $lScritpName ("QoS: $lQoS");
            :if ( !($lQoS)) do={
                [/ip route set [find comment="ID:$kWan"] disabled=yes];
                :set ($fInterface->"enableRouting") false;
            }
        }
    } else={
        [/ip route set [find comment="ID:$kWan"] disabled=yes];
        $logWarning $lScritpName ("Gateway no encontrado, deshabilitando ruta ID:$kWan");
    }
}

#TODO-END

$setScriptEndRun $lScritpName;


File: /sources\spamhaus.rsc
#Version: 3.0 alpha.
#Fecha: 22-12-2019.
#RouterOS 6.43 y superior.
#Comentario:

#TODO-BEGIN

:local spamhausList;
:local spamhausList do={
    :local asList ({"error"=false; data=[]});
    :local url $1;
    
    do {
        :local result [/tool fetch url=$url mode=https as-value output=user];
        :local found -1;
        :local start 0;
        :local line "";
        
        :do {
            :set found [find ($result->"data") "\n" $found];
            :if ($found >= 0) do={
                :set line [pick ($result->"data") $start $found];
                :set start ($found + 1);
                :if ([pick $line 0] != ";") do={
                    :local asn [pick $line 0 [find $line " ;"]];
                    :set ($asList->"data") (($asList->"data"), asn);
                }
            }
        } while=($found >= 0);
    } on-error={
        :set ($asList->"error") true;
    }
    :return $asList;
}

:put [$spamhausList "https://www.spamhaus.org/drop/asndrop.txt"];
:put [$spamhausList "https://www.spamhaus.org/drop/drop.txt"];

#TODO-END
#(192.168.10.10&(255.255.255.255<<32-24))

File: /sources\templates\template-config.rsc
#Version: 3.0 alpha
#Fecha: 22-08-2017
#RouterOS 6.40 y superior.
#Comentario:

:global setLastError;
:local lScriptName "config-";

#TODO-BEGIN

#TODO-END

$setLastError 0 ("$lScriptName cargado.");

File: /sources\templates\template-module.rsc
#Version: 3.0 alpha
#Fecha: 22-08-2017
#RouterOS 6.40 y superior.
#Comentario: 

:global setLastError;
:local lScriptName "module-";

#TODO-BEGIN

#TODO-END

$setLastError 0 ("$lScriptName cargado.");

File: /sources\templates\template-script.rsc
#Version: 3.0 alpha
#Fecha: 22-08-2017
#RouterOS 6.40 y superior.
#Comentario:

:global isScriptRuning;
:global setScriptStartRun;
:global setScriptEndRun;
:global logInfo;
:global logError;
:global logWarning;
:local lScritpName "script-";

:if ([$isScriptRuning $lScritpName]) do={
    $logWarning $lScritpName "Script corriendo.";
    return 255;
}

$setScriptStartRun $lScritpName;

#TODO-BEGIN

#TODO-END

$setScriptEndRun $lScritpName;


File: /sources\templates\template-tool.rsc
#Version: 3.0 alpha
#Fecha: 22-08-2017
#RouterOS 6.40 y superior.
#Comentario:

#TODO-BEGIN



#TODO-END


File: /sources\tool\api-rest\api-rest.rsc
/tool fetch url="https://127.0.0.1/rest/system/identity/set" user=admin password="*" \
output=user http-method=post http-data="{\"name\":\"API REST\"}" http-header-field="content-type: application/json"


File: /sources\tool\dhcp\client\dhcp-client-route.rsc
/ip route
add comment=WAN1 distance=1 dst-address=208.67.220.220/32 gateway=192.168.0.1 scope=10
add comment=WAN2 distance=1 dst-address=208.67.222.222/32 gateway=192.168.0.2 scope=10


File: /sources\tool\dhcp\client\dhcp-client.rsc
:local dhcpBound $bound;
:local dhcpGatewayAddress $"gateway-address";
:local findComment "WAN1";

:if ($dhcpBound = 1) do={
	/ip route set [find comment~"$findComment" gateway!="$dhcpGatewayAddress"] gateway="$dhcpGatewayAddress";
}

File: /sources\tool\dhcp\server\config-dhcp-lease.rsc
:global dhcpLeaseConfig;
:set dhcpLeaseConfig [:toarray ""];

#Segmento de red del DHCP server, tipo ip-prefix.
:set ($dhcpLeaseConfig->"net") 192.168.88.0/24;

#Filtro MAC para no procesar dispositivos cuyas MAC esten en esta lista, tipo array de str.
:set ($dhcpLeaseConfig->"filterMAC") {"70:71:BC:AD:4D:DC"; "CE:E0:E0:5D:EB:A0"};

#Nombre del DHCP server, tipo str.
:set ($dhcpLeaseConfig->"dhcpServer") "defconf";

#Tiempo por defecto del lease-time del servidor DHCP expresado en minutos, se recomienda un valor entre 5m y 10m, tipo time.
:set ($dhcpLeaseConfig->"dhcpLeaseTime") 10m;

#Tiempo de desbloqueo por defecto, expresa el tiempo en segundos; 60 * 60 (una hora), tipo num.
:set ($dhcpLeaseConfig->"unlockedTime") (60 * 60);

#Tiempo de bloqueo por defecto, expresa el tiempo en segundos; 60 * 60 (una hora), tipo num.
:set ($dhcpLeaseConfig->"lockedTime") (60 * 60);

File: /sources\tool\dhcp\server\dhcp-lease-script.rsc
:global dhcpLeases;
if ([:typeof $dhcpLeases] != "array") do={
    :set $dhcpLeases [:toarray ""];
}
:global getCurrentTimestamp;
:global format;
:global dhcpLeaseConfig;

:local dhcpServer "";
:local dhcpLeaseTime 10m;
:local unlockedTime (60 * 60);
:local lockedTime (60 * 30);

:if ($dhcpLeaseConfig~"dhcpServer") do={
    :set dhcpServer ($dhcpLeaseConfig->"dhcpServer");
}

:if ($dhcpLeaseConfig~"dhcpLeaseTime") do={
    :set dhcpLeaseTime ($dhcpLeaseConfig->"dhcpLeaseTime");
}

:if ($dhcpLeaseConfig~"unlockedTime") do={
    :set unlockedTime ($dhcpLeaseConfig->"unlockedTime");
}

:if ($dhcpLeaseConfig~"lockedTime") do={
    :set lockedTime ($dhcpLeaseConfig->"lockedTime");
}

:local dhcpServerId [/ip dhcp-server find where name=$dhcpServer];
:if ([:len $dhcpServerId] > 0) do={
    :local defaultLeaseTime [/ip dhcp-server get $dhcpServerId lease-time];
    :if ($defaultLeaseTime < dhcpLeaseTime) do={
        :set dhcpLeaseTime $defaultLeaseTime;
    }
}
:local dhcpLastSeen (($dhcpLeaseTime / 2) + 15s);
:local timestamp [$getCurrentTimestamp];

:put "";
:put "";
:put "dhcpServer: $dhcpServer";
:put "dhcpLeaseTime: $dhcpLeaseTime";
:put "dhcpLastSeen: $dhcpLastSeen";
:put "timestamp: $timestamp";
:put "unlockedTime: $unlockedTime";
:put "lockedTime: $lockedTime";

:put "";
:put ([$format " MAC-ADDRESS" 20] . [$format "IP" 16] . [$format "HOST NAME" 21] . [$format "BOUND" 7] . [$format "LAST-SEEN" 11] \
 . [$format "BOUND TIME" 16] . [$format "CHECK TIME" 16] . [$format "UPTIME" 16]);

:foreach mac,lease in=$dhcpLeases do={

    :local leaseId [/ip dhcp-server lease find where active-mac-address=$mac];
    :local leaseInfo [:toarray ""];
    if ([:len $leaseId] > 0) do={
        :set leaseInfo [/ip dhcp-server lease get $leaseId];
    }
    if (($lease->"bound") = true) do={
        if ([:len $leaseInfo] > 0) do={
            
            :if (($leaseInfo->"last-seen") < $dhcpLastSeen) do={
                :set ($lease->"uptime") (($timestamp - ($lease->"checkTime")) + ($lease->"uptime"));
            } else={
                if ([/ping ($leaseInfo->"active-address") count=3] > 0) do={
                    :set ($lease->"uptime") (($timestamp - ($lease->"checkTime")) + ($lease->"uptime"));
                    :set ($dhcpLeases->$mac) $lease;
                }
            }
            
            :if (($lease->"uptime") >= $unlockedTime) do={
                /ip firewall raw add chain="prerouting" src-mac-address=$mac action="drop" comment=("$mac-" . ($timestamp + $lockedTime));
                :set ($dhcpLeases->$mac);
                /ip dhcp-server lease remove $leaseId;
            }                        
        }
    }
    
    :set ($lease->"checkTime") $timestamp;
    :put ([$format (" $mac") 20] . [$format ($leaseInfo->"active-address") 16] . [$format ($lease->"hostname") 21] . [$format ($lease->"bound") 7] . [$format ($leaseInfo->"last-seen") 11] \
    . [$format ($lease->"boundTime") 16] . [$format ($lease->"checkTime") 16] . [$format [:totime (($lease->"uptime") . "s")] 16]);    
}

:put "";
:put ([$format " MAC-ADDRESS" 20] . [$format "LOCKED TIME" 16] . [$format "TIME TO UNLOCK" 16]);
 
:local rawLockeds [/ip firewall raw find where comment~"^[0-9A-F][0-9A-F]:"];
:foreach rawId in=$rawLockeds do={
    :local itemRaw [/ip firewall raw get $rawId];
    :local mac ($itemRaw->"src-mac-address");
    :local downtime [:tonum [:pick ($itemRaw->"comment") 18 [:len ($itemRaw->"comment")]]];
    :put ([$format (" $mac") 20] . [$format $downtime 16] . [$format [:totime (($downtime - $timestamp) . "s")] 16]);
    :if ($timestamp > $downtime) do={
        /ip firewall raw remove $rawId;
    }
}

File: /sources\tool\dhcp\server\dhcp-lease-server.rsc
:global dhcpLeases;
if ([:typeof $dhcpLeases] != "array") do={
    :set $dhcpLeases [:toarray ""];
}
:global getCurrentTimestamp;
:global dhcpLeaseConfig;

:local net 0.0.0.0/0;
:local filterMAC [:toarray ""];

:if ($dhcpLeaseConfig~"net") do={
    :set net ($dhcpLeaseConfig->"net");
}

:if ($dhcpLeaseConfig~"filterMAC") do={
    :set filterMAC ($dhcpLeaseConfig->"filterMAC");
}

:if (($leaseActIP in $net) && (!($filterMAC~$leaseActMAC))) do={
    :local lease;
    :if ($leaseBound = 1) do={
        :local leaseId [/ip dhcp-server lease find where active-mac-address=$leaseActMAC];
        :local leaseInfo [/ip dhcp-server lease get $leaseId];
        :if ($leaseInfo->"dynamic") do={
            :local rawLocked [/ip firewall raw find where comment~"^$leaseActMAC"];
            :if ([:len $rawLocked] = 0) do={
                :if ([:len ($dhcpLeases->$leaseActMAC)] = 0) do={
                    :local timestamp [$getCurrentTimestamp];
                    :set lease {"hostname"=($"lease-hostname"); "bound"=true; "boundTime"=$timestamp; "checkTime"=$timestamp; "uptime"=0};
                } else={
                    :set lease ($dhcpLeases->$leaseActMAC);
                    :set ($lease->"bound") true;
                }
                :set ($dhcpLeases->$leaseActMAC) $lease;
            } else={
                /ip dhcp-server lease remove $leaseId;
            }
        }
    } else={
        :if ([:len ($dhcpLeases->$leaseActMAC)] > 0) do={
            :set lease ($dhcpLeases->$leaseActMAC);
            :set ($lease->"bound") false;
            :set ($dhcpLeases->$leaseActMAC) $lease;
        }
    }
}

File: /sources\tool\dhcp\server\module-functions.rsc
:global format;
:set format do={
    :local src $1;
    :local length $2;
    :local lengthSrc [:len $src];
    
    :if ($lengthSrc < ($length)) do={
        :for index from=$lengthSrc to=($length - 1) do={
            :set src ($src . " ");
        }
    } else={
        :set src ([:pick $src 0 ($length - 1)] . " ");
    }
    :return $src;
}

:global getCurrentTimestamp;
:set getCurrentTimestamp do={
    :local date [/system clock get date];
    :local months ({"jan"=1;"feb"=2;"mar"=3;"apr"=4;"may"=5;"jun"=6;"jul"=7;"aug"=8;"sep"=9;"oct"=10;"nov"=11;"dec"=12});
    :local daysForMonths ({31;28;31;30;31;30;31;31;30;31;30;31});
    
    :local day [:tonum [:pick $date 4 6]];
    :local month ($months->[:pick $date 0 3]);
    :local year [:tonum [:pick $date 7 11]];
    
    :local leapDays (($year - 1968) / 4);
    
    :if ((($leapDays * 4) + 1968) = $year) do={
        :set leapDays ($leapDays - 1);
        :set ($daysForMonths->1) 29;
    }
    
    :local days ($day - 1);
    
    :if (($month - 1) > 0) do={
        :for index from=0 to=($month - 2) do={
            :set days ($days + ($daysForMonths->($index)));
        }
    }
        
    :local daysForYear 365;
    :local secondsForDay 86400;
    :local gmtOffset [/system clock get gmt-offset];
    
    :local now [/system clock get time];
    :local hour [:tonum [:pick $now 0 2]];
    :local minutes [:tonum [:pick $now 3 5]];
    :local seconds [:tonum [:pick $now 6 8]];

    :local timestamp ((((($year - 1970) * $daysForYear) + $leapDays + $days) * $secondsForDay) + ($hour * 3600) + ($minutes * 60) + seconds);
    
    :if ($gmtOffset <= $secondsForDay) do={
        :set timestamp ($timestamp - $gmtOffset);
    } else={
        :set timestamp ($timestamp + (-$gmtOffset&0x00000000FFFFFFFF));
    }
    
    :return $timestamp;    
}

File: /sources\tool\dhcp\server\readme.txt
PASOS PARA INSTALACION

1 - Configurar los parametros en el archivo config-dhcp-lease.

2 - Agregar al repositorio de scritps los siguientes scripts:
    - config-dhcp-lease
    - module-functions
    - dhcp-lease-script
    
3 - Instalar el dhcp-lease-server en la seccion script del DHCP server.

4 - Crear un scheduler para correr al inicio del router los scripts:
    - config-dhcp-lease
    - module-functions

5 - Crear un scheduler para correr periodicamente entre 1 y 5 minutos el siguiente script:
    - config-dhcp-lease
    - module-functions
    - dhcp-lease-script

6 - Reiniciar el router.

7 - Limpiar los leases concedidos del servidor DHCP.

File: /sources\tool\icmp\flood-ping-latency.rsc
:global pingLatency;
:set pingLatency do={
    
}



:global dhcpLeases;
if ([:typeof $dhcpLeases] != "array") do={
    :set $dhcpLeases [:toarray ""];
}
:global getCurrentTimestamp;
:global dhcpLeaseConfig;

:local net 0.0.0.0/0;
:local filterMAC [:toarray ""];

:if ($dhcpLeaseConfig~"net") do={
    :set net ($dhcpLeaseConfig->"net");
}

:if ($dhcpLeaseConfig~"filterMAC") do={
    :set filterMAC ($dhcpLeaseConfig->"filterMAC");
}

:if (($leaseActIP in $net) && (!($filterMAC~$leaseActMAC))) do={
    :local lease;
    :if ($leaseBound = 1) do={
        :local leaseId [/ip dhcp-server lease find where active-mac-address=$leaseActMAC];
        :local leaseInfo [/ip dhcp-server lease get $leaseId];
        :if ($leaseInfo->"dynamic") do={
            :local rawLocked [/ip firewall raw find where comment~"^$leaseActMAC"];
            :if ([:len $rawLocked] = 0) do={
                :if ([:len ($dhcpLeases->$leaseActMAC)] = 0) do={
                    :local timestamp [$getCurrentTimestamp];
                    :set lease {"hostname"=($"lease-hostname"); "bound"=true; "boundTime"=$timestamp; "checkTime"=$timestamp; "uptime"=0};
                } else={
                    :set lease ($dhcpLeases->$leaseActMAC);
                    :set ($lease->"bound") true;
                }
                :set ($dhcpLeases->$leaseActMAC) $lease;
            } else={
                /ip dhcp-server lease remove $leaseId;
            }
        }
    } else={
        :if ([:len ($dhcpLeases->$leaseActMAC)] > 0) do={
            :set lease ($dhcpLeases->$leaseActMAC);
            :set ($lease->"bound") false;
            :set ($dhcpLeases->$leaseActMAC) $lease;
        }
    }
}

File: /sources\tool\json\json.rsc
{

:global jsonTokenizer;

:global initialize do={
    :global jsonTokenizer;
    :if ([:typeof $1] = "str") do={
        :set jsonTokenizer {"index"=0;"length"=0;"char"="";"string"="$1"};
        :set ($jsonTokenizer->"length") [:len ($jsonTokenizer->"string")];
        :return true;
    }
    :return false;
}

:global nextChar do={
    :global jsonTokenizer;
    :if ((($jsonTokenizer->"index") >= 0) and (($jsonTokenizer->"index") < ($jsonTokenizer->"length"))) do={
        :set ($jsonTokenizer->"char") [:pick ($jsonTokenizer->"string") ($jsonTokenizer->"index")];
        :set ($jsonTokenizer->"index") (($jsonTokenizer->"index") + 1);
        :return true;
    }
    :return false;
}

:global a "\n"

:global isWhiteSpace do={
    :return (($1 = " ") or ($1 = "\10") or ($1 = "\09") or ($1 = "\0C"));
}


### TEST ###

:local test "{\"ok\":true}";

:put [$initialize $test];
}

:while ([$nextChar]) do={
    :put ($jsonTokenizer->"char");
}


File: /sources\tool\json\mod-json.rsc
:global getAll do={
    :local path "$1";
    :local where "";
    :if ([:len $2] > 0) do={
        :set where "where $2";
    }
    :local result [:toarray ""];
    :local ids [[:parse "$path find $where"]];
    :foreach id in=$ids do={
        :local item [[:parse "$path get $id"]];
        :set result ($result , {$item});
    }
    :return $result;
}

:global toJson do={
    :global toJson;
    :local result "";
    :if ([:typeof $1] = "array") do={
        :if ([:len $1] > 0) do={
            :if (!any ($1->0)) do={
#               object
                :set result "{";
                :local comma "";
                :foreach k,v in=$1 do={
                    :set result ($result . "$comma\"$k\":" . [$toJson $v]);
                    :if ($comma="") do={
                        :set comma ",";
                    }
                }
                :return ($result . "}");
            } else={
#               array
                :set result "[";
                :local comma "";
                :foreach v in=$1 do={
                    :set result ($result . "$comma" . [$toJson $v]);
                    :if ($comma="") do={
                        :set comma ",";
                    }
                }
                :return ($result . "]");
            }
        } else={
            :return [:toarray ""];
        }
    } else={
        :if ([:typeof $1] = "str" || [:typeof $1] = "id" || [:typeof $1] = "ip" \
             || [:typeof $1] = "ip-prefix" || [:typeof $1] = "ip6" || [:typeof $1] = "ip6-prefix") do={
            :return "\"$1\"";
        } else={
            :if ([:typeof $1] = "num" || [:typeof $1] = "bool") do={
                :return "$1";
            } else={
                :if ([:typeof $1] = "nothing" || [:typeof $1] = "nil" || $1 = null) do={
                    :return "null";
                } else={
                    :return ("\"" . [:typeof $1] . ": $1\"");
                }
            }
        }
    
#        :put "Err.Raise. Expecting param array.";
#        :return [:toarray ""];
    }
}


:global fromJson do={

    :local skipWhiteSpaces do={
        :local json $1;
        :while (($json->"pos") < ($json->"len") and ([:pick ($json->"in") ($json->"pos")] ~ "[ \r\n\t]")) do={
            :set ($json->"pos") (($json->"pos") + 1);
        }
        :return $json;
    }
    

}


:global json [:toarray ""];

:set ($json->"len") 0;
:set ($json->"in") "";
:set ($json->"pos") 0;
:set ($json->"debug") false;

:set ($json->"skipWhiteSpaces") do={
    :local json $1;
    :while (($json->"pos") < ($json->"len") and ([:pick ($json->"in") ($json->"pos")] ~ "[ \r\n\t]")) do={
        :set ($json->"pos") (($json->"pos") + 1);
    }
    :return $json;
}

:set ($json->"parse") do={
    :local json $1;
    :local Char;

    :set json [($json->"skipWhiteSpaces")];
    :set Char [:pick ($json->"in") ($json->"pos")];
      
    :if ($Char="{") do={
        :set ($json->"pos") (($json->"pos") + 1);
        :return [($json->"parseObject")];
    } else={
        :if ($Char="[") do={
            :set ($json->"pos") (($json->"pos") + 1);
            :return [($json->"parseArray")];
        } else={
            :if ($Char="\"") do={
                :set ($json->"pos") (($json->"pos") + 1);
                :return [($json->"parseString")];
            } else={
                :if ($Char~"[eE0-9.+-]") do={
                    :return [($json->"parseNumber")];
                } else={
                    :if ($Char="n" and [:pick ($json->"in") ($json->"pos") (($json->"pos") + 4)]="null") do={
                        :set ($json->"pos") (($json->"pos") + 4);
                        :return [];
                    } else={
                        :if ($Char="t" and [:pick ($json->"in") ($json->"pos") (($json->"pos") + 4)]="true") do={
                            :set ($json->"pos") (($json->"pos") + 4);
                            :return true;
                        } else={
                            :if ($Char="f" and [:pick ($json->"in") ($json->"pos") (($json->"pos") + 5)]="false") do={
                                :set ($json->"pos") (($json->"pos") + 5);
                                :return false;
                            } else={
                                :put "Err.Raise 8732. No JSON object";
                                :set ($json->"pos") (($json->"pos") + 1);
                                :return [];
                            }
                        }
                    }
                }
            }
        }
    }
}

:set ($json->"parseString") do={
    :global json;
    :local unicodeToUTF8 ($json->"unicodeToUTF8");
    
    :local Char;
    :local StartIdx;
    :local Char2;
    :local TempString "";
    :local UTFCode;
    :local Unicode;

    :set StartIdx ($json->"pos");
    :set Char [:pick ($json->"in") ($json->"pos")];
  
    :while (($json->"pos") < ($json->"len") and $Char != "\"") do={
        :if ($Char="\\") do={
            :set Char2 [:pick ($json->"in") (($json->"pos") + 1)];
            :if ($Char2 = "u") do={
                :set UTFCode [:tonum ("0x" . [:pick ($json->"in") (($json->"pos") + 2) (($json->"pos") + 6)])];
                :if ($UTFCode>=0xD800 and $UTFCode<=0xDFFF) do={
# Surrogate pair
                    :set Unicode  (($UTFCode & 0x3FF) << 10);
                    :set UTFCode [:tonum ("0x" . [:pick ($json->"in") (($json->"pos") + 8) (($json->"pos") + 12)])];
                    :set Unicode ($Unicode | ($UTFCode & 0x3FF) | 0x10000);
                    :set TempString ($TempString . [:pick ($json->"in") $StartIdx ($json->"pos")] . [$unicodeToUTF8 $Unicode]);
                    :set ($json->"pos") (($json->"pos") + 12);
                } else={
# Basic Multilingual Plane (BMP)
                    :set Unicode $UTFCode;
                    :set TempString ($TempString . [:pick ($json->"in") $StartIdx ($json->"pos")] . [$unicodeToUTF8 $Unicode]);
                    :set ($json->"pos") (($json->"pos") + 6);
                }
                :set StartIdx ($json->"pos");
            } else={
                :if ($Char2 ~ "[\\bfnrt\"]") do={
                    :set TempString ($TempString . [:pick ($json->"in") $StartIdx ($json->"pos")] . [[:parse "(\"\\$Char2\")"]]);
                    :set ($json->"pos") (($json->"pos") + 2);
                    :set StartIdx ($json->"pos");
                } else={
                    :if ($Char2 = "/") do={
                        :set TempString ($TempString . [:pick ($json->"in") $StartIdx ($json->"pos")] . "/");
                        :set ($json->"pos") (($json->"pos") + 2);
                        :set StartIdx ($json->"pos");
                    } else={
                        :put "Err.Raise 8732. Invalid escape";
                        :set ($json->"pos") (($json->"pos") + 2);
                    }
                }
            }
        } else={
            :set ($json->"pos") (($json->"pos") + 1);
        }
        :set Char [:pick ($json->"in") ($json->"pos")];
    }
    :set TempString ($TempString . [:pick ($json->"in") $StartIdx ($json->"pos")]);
    :set ($json->"pos") (($json->"pos") + 1);
    :return $TempString;
}

:set ($json->"parseNumber") do={
    :global json;    
    :local StartIdx
    :local NumberString
    :local Number

    :set StartIdx ($json->"pos");
    :set ($json->"pos") (($json->"pos") + 1);
    :while (($json->"pos") < ($json->"len") and [:pick ($json->"in") ($json->"pos")]~"[eE0-9.+-]") do={
        :set ($json->"pos") (($json->"pos") + 1);
    }
    :set NumberString [:pick ($json->"in") $StartIdx ($json->"pos")];
    :set Number [:tonum $NumberString];
    :if ([:typeof $Number] = "num") do={
        :return $Number;
    } else={
        :return $NumberString;
    }
}

:set ($json->"parseArray") do={
    :global json;    
    :local Value;
    :local ParseArrayRet [:toarray ""];
    
    [($json->"skipWhiteSpaces")];
    :while (($json->"pos") < ($json->"len") and [:pick ($json->"in") ($json->"pos")]!= "]") do={
        :set Value [($json->"parse")];
        :set ($ParseArrayRet->([:len $ParseArrayRet])) $Value;
        [($json->"skipWhiteSpaces")];
        :if ([:pick ($json->"in") ($json->"pos")] = ",") do={
            :set ($json->"pos") (($json->"pos") + 1);
            [($json->"skipWhiteSpaces")];
        }
    }
    :set ($json->"pos") (($json->"pos") + 1);
    :return $ParseArrayRet;
}

:set ($json->"parseObject") do={
    :global json;
# Syntax :local ParseObjectRet ({}) don't work in recursive call, use [:toarray ""] for empty array!!!
    :local ParseObjectRet [:toarray ""];
    :local Key;
    :local Value;
    :local ExitDo false;
 
    [($json->"skipWhiteSpaces")];
    
    :while (($json->"pos") < ($json->"len") and [:pick ($json->"in") ($json->"pos")]!="}" and !$ExitDo) do={
        :if ([:pick ($json->"in") ($json->"pos")]!="\"") do={
            :put "Err.Raise 8732. Expecting property name";
            :set ExitDo true;
        } else={
            :set ($json->"pos") (($json->"pos") + 1);
            :set Key [($json->"parseString")];
            [($json->"skipWhiteSpaces")];
            :if ([:pick ($json->"in") ($json->"pos")] != ":") do={
                :put "Err.Raise 8732. Expecting : delimiter";
                :set ExitDo true;
            } else={
                :set ($json->"pos") (($json->"pos") + 1);
                :set Value [($json->"parse")];
                :set ($ParseObjectRet->$Key) $Value;
                [($json->"skipWhiteSpaces")];
                :if ([:pick ($json->"in") ($json->"pos")]=",") do={
                    :set ($json->"pos") (($json->"pos") + 1);
                    [($json->"skipWhiteSpaces")];
                }
            }
        }
    }
    :set ($json->"pos") (($json->"pos") + 1);
    :return $ParseObjectRet;
}

:set ($json->"byteToEscapeChar") do={
    :return [[:parse "(\"\\$[:pick "0123456789ABCDEF" (($1 >> 4) & 0xF)]$[:pick "0123456789ABCDEF" ($1 & 0xF)]\")"]];
}

:set ($json->"unicodeToUTF8") do={
    :global json;
    :local byteToEscapeChar ($json->"byteToEscapeChar");
    
    :local Nbyte;
    :local EscapeStr "";
    
    :if ($1 < 0x80) do={
        :set EscapeStr [$byteToEscapeChar $1];
    } else={
        :if ($1 < 0x800) do={
            :set Nbyte 2;
        } else={
            :if ($1 < 0x10000) do={
                :set Nbyte 3;
            } else={
                :if ($1 < 0x20000) do={
                    :set Nbyte 4;
                } else={
                    :if ($1 < 0x4000000) do={
                        :set Nbyte 5;
                    } else={
                        :if ($1 < 0x80000000) do={
                            :set Nbyte 6;
                        }
                    }
                }
            }
        }
        :for i from=2 to=$Nbyte do={
            :set EscapeStr ([$byteToEscapeChar ($1 & 0x3F | 0x80)] . $EscapeStr);
            :set $1 ($1 >> 6);
        }
        :set EscapeStr ([$byteToEscapeChar (((0xFF00 >> $Nbyte) & 0xFF) | $1)] . $EscapeStr);
    }
    :return $EscapeStr;
}

global jsonParse do={
    :global json;
    :set ($json->"in") $1;
    :set ($json->"pos") 0;
    :set ($json->"len") [:len $1];    
    :set ($json->"debug") false;
    
    :return [($json->"parse")];
}










# -------------------------------- JParseFunctions ---------------------------------------------------
# ------------------------------- fJParsePrint ----------------------------------------------------------------
:global fJParsePrint
:if (!any $fJParsePrint) do={ :global fJParsePrint do={
  :global JParseOut
  :local TempPath
  :global fJParsePrint

  :if ([:len $1] = 0) do={
    :set $1 "\$JParseOut"
    :set $2 $JParseOut
   }
   
  :foreach k,v in=$2 do={
    :if ([:typeof $k] = "str") do={
      :set k "\"$k\""
    }
    :set TempPath ($1. "->" . $k)
    :if ([:typeof $v] = "array") do={
      :if ([:len $v] > 0) do={
        $fJParsePrint $TempPath $v
      } else={
        :put "$TempPath = [] ($[:typeof $v])"
      }
    } else={
        :put "$TempPath = $v ($[:typeof $v])"
    }
  }
}}
# ------------------------------- fJParsePrintVar ----------------------------------------------------------------
:global fJParsePrintVar
:if (!any $fJParsePrintVar) do={ :global fJParsePrintVar do={
  :global JParseOut
  :local TempPath
  :global fJParsePrintVar
  :local fJParsePrintRet ""

  :if ([:len $1] = 0) do={
    :set $1 "\$JParseOut"
    :set $2 $JParseOut
   }
   
  :foreach k,v in=$2 do={
    :if ([:typeof $k] = "str") do={
      :set k "\"$k\""
    }
    :set TempPath ($1. "->" . $k)
    :if ($fJParsePrintRet != "") do={
      :set fJParsePrintRet ($fJParsePrintRet . "\r\n")
    }    
    :if ([:typeof $v] = "array") do={
      :if ([:len $v] > 0) do={
        :set fJParsePrintRet ($fJParsePrintRet . [$fJParsePrintVar $TempPath $v])
      } else={
        :set fJParsePrintRet ($fJParsePrintRet . "$TempPath = [] ($[:typeof $v])")
      }
    } else={
        :set fJParsePrintRet ($fJParsePrintRet . "$TempPath = $v ($[:typeof $v])")
    }
  }
  :return $fJParsePrintRet
}}


# ------------------- Load JSON from arg --------------------------------
global JSONLoads
if (!any $JSONLoads) do={ global JSONLoads do={
    global JSONIn $1
    global fJParse
    local ret [$fJParse]
    set JSONIn
    global Jpos; set Jpos
    global Jdebug; if (!$Jdebug) do={set Jdebug}
    return $ret
}}

# ------------------- Load JSON from file --------------------------------
global JSONLoad
if (!any $JSONLoad) do={ global JSONLoad do={
    if ([len [/file find name=$1]] > 0) do={
        global JSONLoads
        return [$JSONLoads [/file get $1 contents]]
    }
}}

# ------------------- Unload JSON parser library ----------------------
global JSONUnload
if (!any $JSONUnload) do={ global JSONUnload do={
    global JSONIn; set JSONIn
    global Jpos; set Jpos
    global Jdebug; set Jdebug
    global fByteToEscapeChar; set fByteToEscapeChar
    global fJParse; set fJParse
    global fJParseArray; set fJParseArray
    global fJParseNumber; set fJParseNumber
    global fJParseObject; set fJParseObject
    global fJParsePrint; set fJParsePrint
    global fJParsePrintVar; set fJParsePrintVar
    global fJParseString; set fJParseString
    global fJSkipWhitespace; set fJSkipWhitespace
    global fUnicodeToUTF8; set fUnicodeToUTF8
    global JSONLoads; set JSONLoads
    global JSONLoad; set JSONLoad
    global JSONUnload; set JSONUnload
}}
# ------------------- End JParseFunctions----------------------


File: /sources\tool\json\module-json.rsc
:global getAll do={
    :local path "$1";
    :local where "";
    :if ([:len $2] > 0) do={
        :set where "where $2";
    }
    :local result [:toarray ""];
    :local ids [[:parse "$path find $where"]];
    :foreach id in=$ids do={
        :local item [[:parse "$path get $id"]];
        :set result ($result , {$item});
    }
    :return $result;
}

:global toJson do={
    :global toJson;
    :local result "";
    :if ([:typeof $1] = "array") do={
        :if ([:len $1] > 0) do={
            :if (!any ($1->0)) do={
#               object
                :set result "{";
                :local comma "";
                :foreach k,v in=$1 do={
                    :set result ($result . "$comma\"$k\":" . [$toJson $v]);
                    :if ($comma="") do={
                        :set comma ",";
                    }
                }
                :return ($result . "}");
            } else={
#               array
                :set result "[";
                :local comma "";
                :foreach v in=$1 do={
                    :set result ($result . "$comma" . [$toJson $v]);
                    :if ($comma="") do={
                        :set comma ",";
                    }
                }
                :return ($result . "]");
            }
        } else={
            :return [:toarray ""];
        }
    } else={
        :if ([:typeof $1] = "str" || [:typeof $1] = "id" || [:typeof $1] = "ip" \
             || [:typeof $1] = "ip-prefix" || [:typeof $1] = "ip6" || [:typeof $1] = "ip6-prefix") do={
            :return "\"$1\"";
        } else={
            :if ([:typeof $1] = "num" || [:typeof $1] = "bool") do={
                :return "$1";
            } else={
                :if ([:typeof $1] = "nothing" || [:typeof $1] = "nil" || $1 = null) do={
                    :return "null";
                } else={
                    :return ("\"" . [:typeof $1] . ": $1\"");
                }
            }
        }
    
#        :put "Err.Raise. Expecting param array.";
#        :return [:toarray ""];
    }
}


:global json [:toarray ""];

:set ($json->"len") 0;
:set ($json->"in") "";
:set ($json->"pos") 0;
:set ($json->"debug") false;

:set ($json->"skipWhiteSpaces") do={
    :global json;    
    :while (($json->"pos") < ($json->"len") and ([:pick ($json->"in") ($json->"pos")] ~ "[ \r\n\t]")) do={
        :set ($json->"pos") (($json->"pos") + 1);
    }
}

:set ($json->"parse") do={
    :global json;
    :local Char;

#    :if (!$1) do={
#        :set ($json->"pos") 0;
#    }

    [($json->"skipWhiteSpaces")];
    :set Char [:pick ($json->"in") ($json->"pos")];
      
    :if ($Char="{") do={
        :set ($json->"pos") (($json->"pos") + 1);
        :return [($json->"parseObject")];
    } else={
        :if ($Char="[") do={
            :set ($json->"pos") (($json->"pos") + 1);
            :return [($json->"parseArray")];
        } else={
            :if ($Char="\"") do={
                :set ($json->"pos") (($json->"pos") + 1);
                :return [($json->"parseString")];
            } else={
                :if ($Char~"[eE0-9.+-]") do={
                    :return [($json->"parseNumber")];
                } else={
                    :if ($Char="n" and [:pick ($json->"in") ($json->"pos") (($json->"pos") + 4)]="null") do={
                        :set ($json->"pos") (($json->"pos") + 4);
                        :return [];
                    } else={
                        :if ($Char="t" and [:pick ($json->"in") ($json->"pos") (($json->"pos") + 4)]="true") do={
                            :set ($json->"pos") (($json->"pos") + 4);
                            :return true;
                        } else={
                            :if ($Char="f" and [:pick ($json->"in") ($json->"pos") (($json->"pos") + 5)]="false") do={
                                :set ($json->"pos") (($json->"pos") + 5);
                                :return false;
                            } else={
                                :put "Err.Raise 8732. No JSON object";
                                :set ($json->"pos") (($json->"pos") + 1);
                                :return [];
                            }
                        }
                    }
                }
            }
        }
    }
}

:set ($json->"parseString") do={
    :global json;
    :local unicodeToUTF8 ($json->"unicodeToUTF8");
    
    :local Char;
    :local StartIdx;
    :local Char2;
    :local TempString "";
    :local UTFCode;
    :local Unicode;

    :set StartIdx ($json->"pos");
    :set Char [:pick ($json->"in") ($json->"pos")];
  
    :while (($json->"pos") < ($json->"len") and $Char != "\"") do={
        :if ($Char="\\") do={
            :set Char2 [:pick ($json->"in") (($json->"pos") + 1)];
            :if ($Char2 = "u") do={
                :set UTFCode [:tonum ("0x" . [:pick ($json->"in") (($json->"pos") + 2) (($json->"pos") + 6)])];
                :if ($UTFCode>=0xD800 and $UTFCode<=0xDFFF) do={
# Surrogate pair
                    :set Unicode  (($UTFCode & 0x3FF) << 10);
                    :set UTFCode [:tonum ("0x" . [:pick ($json->"in") (($json->"pos") + 8) (($json->"pos") + 12)])];
                    :set Unicode ($Unicode | ($UTFCode & 0x3FF) | 0x10000);
                    :set TempString ($TempString . [:pick ($json->"in") $StartIdx ($json->"pos")] . [$unicodeToUTF8 $Unicode]);
                    :set ($json->"pos") (($json->"pos") + 12);
                } else={
# Basic Multilingual Plane (BMP)
                    :set Unicode $UTFCode;
                    :set TempString ($TempString . [:pick ($json->"in") $StartIdx ($json->"pos")] . [$unicodeToUTF8 $Unicode]);
                    :set ($json->"pos") (($json->"pos") + 6);
                }
                :set StartIdx ($json->"pos");
            } else={
                :if ($Char2 ~ "[\\bfnrt\"]") do={
                    :set TempString ($TempString . [:pick ($json->"in") $StartIdx ($json->"pos")] . [[:parse "(\"\\$Char2\")"]]);
                    :set ($json->"pos") (($json->"pos") + 2);
                    :set StartIdx ($json->"pos");
                } else={
                    :if ($Char2 = "/") do={
                        :set TempString ($TempString . [:pick ($json->"in") $StartIdx ($json->"pos")] . "/");
                        :set ($json->"pos") (($json->"pos") + 2);
                        :set StartIdx ($json->"pos");
                    } else={
                        :put "Err.Raise 8732. Invalid escape";
                        :set ($json->"pos") (($json->"pos") + 2);
                    }
                }
            }
        } else={
            :set ($json->"pos") (($json->"pos") + 1);
        }
        :set Char [:pick ($json->"in") ($json->"pos")];
    }
    :set TempString ($TempString . [:pick ($json->"in") $StartIdx ($json->"pos")]);
    :set ($json->"pos") (($json->"pos") + 1);
    :return $TempString;
}

:set ($json->"parseNumber") do={
    :global json;    
    :local StartIdx
    :local NumberString
    :local Number

    :set StartIdx ($json->"pos");
    :set ($json->"pos") (($json->"pos") + 1);
    :while (($json->"pos") < ($json->"len") and [:pick ($json->"in") ($json->"pos")]~"[eE0-9.+-]") do={
        :set ($json->"pos") (($json->"pos") + 1);
    }
    :set NumberString [:pick ($json->"in") $StartIdx ($json->"pos")];
    :set Number [:tonum $NumberString];
    :if ([:typeof $Number] = "num") do={
        :return $Number;
    } else={
        :return $NumberString;
    }
}

:set ($json->"parseArray") do={
    :global json;    
    :local Value;
    :local ParseArrayRet [:toarray ""];
    
    [($json->"skipWhiteSpaces")];
    :while (($json->"pos") < ($json->"len") and [:pick ($json->"in") ($json->"pos")]!= "]") do={
        :set Value [($json->"parse")];
        :set ($ParseArrayRet->([:len $ParseArrayRet])) $Value;
        [($json->"skipWhiteSpaces")];
        :if ([:pick ($json->"in") ($json->"pos")] = ",") do={
            :set ($json->"pos") (($json->"pos") + 1);
            [($json->"skipWhiteSpaces")];
        }
    }
    :set ($json->"pos") (($json->"pos") + 1);
    :return $ParseArrayRet;
}

:set ($json->"parseObject") do={
    :global json;
# Syntax :local ParseObjectRet ({}) don't work in recursive call, use [:toarray ""] for empty array!!!
    :local ParseObjectRet [:toarray ""];
    :local Key;
    :local Value;
    :local ExitDo false;
 
    [($json->"skipWhiteSpaces")];
    
    :while (($json->"pos") < ($json->"len") and [:pick ($json->"in") ($json->"pos")]!="}" and !$ExitDo) do={
        :if ([:pick ($json->"in") ($json->"pos")]!="\"") do={
            :put "Err.Raise 8732. Expecting property name";
            :set ExitDo true;
        } else={
            :set ($json->"pos") (($json->"pos") + 1);
            :set Key [($json->"parseString")];
            [($json->"skipWhiteSpaces")];
            :if ([:pick ($json->"in") ($json->"pos")] != ":") do={
                :put "Err.Raise 8732. Expecting : delimiter";
                :set ExitDo true;
            } else={
                :set ($json->"pos") (($json->"pos") + 1);
                :set Value [($json->"parse")];
                :set ($ParseObjectRet->$Key) $Value;
                [($json->"skipWhiteSpaces")];
                :if ([:pick ($json->"in") ($json->"pos")]=",") do={
                    :set ($json->"pos") (($json->"pos") + 1);
                    [($json->"skipWhiteSpaces")];
                }
            }
        }
    }
    :set ($json->"pos") (($json->"pos") + 1);
    :return $ParseObjectRet;
}

:set ($json->"byteToEscapeChar") do={
    :return [[:parse "(\"\\$[:pick "0123456789ABCDEF" (($1 >> 4) & 0xF)]$[:pick "0123456789ABCDEF" ($1 & 0xF)]\")"]];
}

:set ($json->"unicodeToUTF8") do={
    :global json;
    :local byteToEscapeChar ($json->"byteToEscapeChar");
    
    :local Nbyte;
    :local EscapeStr "";
    
    :if ($1 < 0x80) do={
        :set EscapeStr [$byteToEscapeChar $1];
    } else={
        :if ($1 < 0x800) do={
            :set Nbyte 2;
        } else={
            :if ($1 < 0x10000) do={
                :set Nbyte 3;
            } else={
                :if ($1 < 0x20000) do={
                    :set Nbyte 4;
                } else={
                    :if ($1 < 0x4000000) do={
                        :set Nbyte 5;
                    } else={
                        :if ($1 < 0x80000000) do={
                            :set Nbyte 6;
                        }
                    }
                }
            }
        }
        :for i from=2 to=$Nbyte do={
            :set EscapeStr ([$byteToEscapeChar ($1 & 0x3F | 0x80)] . $EscapeStr);
            :set $1 ($1 >> 6);
        }
        :set EscapeStr ([$byteToEscapeChar (((0xFF00 >> $Nbyte) & 0xFF) | $1)] . $EscapeStr);
    }
    :return $EscapeStr;
}

global jsonParse do={
    :global json;
    :set ($json->"in") $1;
    :set ($json->"pos") 0;
    :set ($json->"len") [:len $1];    
    :set ($json->"debug") false;
    
    :return [($json->"parse")];
}










# -------------------------------- JParseFunctions ---------------------------------------------------
# ------------------------------- fJParsePrint ----------------------------------------------------------------
:global fJParsePrint
:if (!any $fJParsePrint) do={ :global fJParsePrint do={
  :global JParseOut
  :local TempPath
  :global fJParsePrint

  :if ([:len $1] = 0) do={
    :set $1 "\$JParseOut"
    :set $2 $JParseOut
   }
   
  :foreach k,v in=$2 do={
    :if ([:typeof $k] = "str") do={
      :set k "\"$k\""
    }
    :set TempPath ($1. "->" . $k)
    :if ([:typeof $v] = "array") do={
      :if ([:len $v] > 0) do={
        $fJParsePrint $TempPath $v
      } else={
        :put "$TempPath = [] ($[:typeof $v])"
      }
    } else={
        :put "$TempPath = $v ($[:typeof $v])"
    }
  }
}}
# ------------------------------- fJParsePrintVar ----------------------------------------------------------------
:global fJParsePrintVar
:if (!any $fJParsePrintVar) do={ :global fJParsePrintVar do={
  :global JParseOut
  :local TempPath
  :global fJParsePrintVar
  :local fJParsePrintRet ""

  :if ([:len $1] = 0) do={
    :set $1 "\$JParseOut"
    :set $2 $JParseOut
   }
   
  :foreach k,v in=$2 do={
    :if ([:typeof $k] = "str") do={
      :set k "\"$k\""
    }
    :set TempPath ($1. "->" . $k)
    :if ($fJParsePrintRet != "") do={
      :set fJParsePrintRet ($fJParsePrintRet . "\r\n")
    }    
    :if ([:typeof $v] = "array") do={
      :if ([:len $v] > 0) do={
        :set fJParsePrintRet ($fJParsePrintRet . [$fJParsePrintVar $TempPath $v])
      } else={
        :set fJParsePrintRet ($fJParsePrintRet . "$TempPath = [] ($[:typeof $v])")
      }
    } else={
        :set fJParsePrintRet ($fJParsePrintRet . "$TempPath = $v ($[:typeof $v])")
    }
  }
  :return $fJParsePrintRet
}}


# ------------------- Load JSON from arg --------------------------------
global JSONLoads
if (!any $JSONLoads) do={ global JSONLoads do={
    global JSONIn $1
    global fJParse
    local ret [$fJParse]
    set JSONIn
    global Jpos; set Jpos
    global Jdebug; if (!$Jdebug) do={set Jdebug}
    return $ret
}}

# ------------------- Load JSON from file --------------------------------
global JSONLoad
if (!any $JSONLoad) do={ global JSONLoad do={
    if ([len [/file find name=$1]] > 0) do={
        global JSONLoads
        return [$JSONLoads [/file get $1 contents]]
    }
}}

# ------------------- Unload JSON parser library ----------------------
global JSONUnload
if (!any $JSONUnload) do={ global JSONUnload do={
    global JSONIn; set JSONIn
    global Jpos; set Jpos
    global Jdebug; set Jdebug
    global fByteToEscapeChar; set fByteToEscapeChar
    global fJParse; set fJParse
    global fJParseArray; set fJParseArray
    global fJParseNumber; set fJParseNumber
    global fJParseObject; set fJParseObject
    global fJParsePrint; set fJParsePrint
    global fJParsePrintVar; set fJParsePrintVar
    global fJParseString; set fJParseString
    global fJSkipWhitespace; set fJSkipWhitespace
    global fUnicodeToUTF8; set fUnicodeToUTF8
    global JSONLoads; set JSONLoads
    global JSONLoad; set JSONLoad
    global JSONUnload; set JSONUnload
}}
# ------------------- End JParseFunctions----------------------


File: /sources\tool\monitor\config-monitor-traffic.rsc
:global monitorTrafficConfig;
:set monitorTrafficConfig [:toarray ""];

:global monitorTrafficData;
:set monitorTrafficData [:toarray ""];

#Intervalo de tiempo para el monitoreo.
:set ($monitorTrafficConfig->"interval") 1s;

#Duracion del monitoreo.
:set ($monitorTrafficConfig->"duration") 1m;

#Tiempo de espera antes de monitorear luego de hacer un UP.
:set ($monitorTrafficConfig->"delayForUp") 30s;

#Lista de interfaces a monitorear.
:set ($monitorTrafficConfig->"interfaces") [:toarray ""];

:set ($monitorTrafficConfig->"interfaces"->"ether1-wan") {"rx-average"=1024; "up"="ether1-wan-up"; "down"="ether1-wan-down"};
:set ($monitorTrafficConfig->"interfaces"->"ether2") {"rx-average"=2048; "up"=""; "down"=""};

File: /sources\tool\monitor\monitor-traffic-dev.rsc
/execute {
    :global monitorTrafficData;
    :global monitorTrafficConfig;
    :if ([:len ($monitorTrafficData->"ether1-wan")] = 0) do={
        :set ($monitorTrafficData->"ether1-wan") {"enable"=true; "data"={"count"=0;"sum"=0;"average"=0}};
    };
    :local enable ($monitorTrafficData->"ether1-wan"->"enable");
    :if (!$enable) do={
        :set ($monitorTrafficData->"ether1-wan"->"enable") true;
        :local up ($monitorTrafficConfig->"interfaces"->"ether1-wan"->"up");
        :if ([:len [/system script find where name="$up"]] > 0) do={
            /system script run "$up";
        };
        :delay ($monitorTrafficConfig->"delayForUp");
    };
    :set ($monitorTrafficData->"ether1-wan") {"enable"=true; "data"={"count"=0;"sum"=0;"average"=0}};
    /interface monitor-traffic ether1-wan interval=($monitorTrafficConfig->"interval") duration=($monitorTrafficConfig->"duration") do={
        :global monitorTrafficData;
        :local data ($monitorTrafficData->"ether1-wan"->"data");
        :local count (($data->"count") + 1);
        :local sum (($data->"sum") + ($"rx-bits-per-second"));
        :set ($monitorTrafficData->"ether1-wan"->"data") {"count"=$count;"sum"=$sum;"average"=($sum / $count)};
    };
    :local rxAverage ($monitorTrafficConfig->"interfaces"->"ether1-wan"->"rx-average");
    :local interfaceAverage ($monitorTrafficData->"ether1-wan"->"data"->"average");
    :if ($interfaceAverage < $rxAverage) do={
        :set ($monitorTrafficData->"ether1-wan"->"enable") false;
        :local down ($monitorTrafficConfig->"interfaces"->"ether1-wan"->"down");
        :if ([:len [/system script find where name="$down"]] > 0) do={
            /system script run "$down";
        };
    };
};

File: /sources\tool\monitor\monitor-traffic.rsc
:global monitorTrafficConfig;
:foreach interface,data in=($monitorTrafficConfig->"interfaces") do={
    /execute "{ \
        :global monitorTrafficData; \
        :global monitorTrafficConfig; \
        :if ([:len (\$monitorTrafficData->\"$interface\")] = 0) do={ \
            :set (\$monitorTrafficData->\"$interface\") {\"enable\"=true; \"data\"={\"count\"=0;\"sum\"=0;\"average\"=0}}; \
        }; \
        :local enable (\$monitorTrafficData->\"$interface\"->\"enable\"); \
        :if (!\$enable) do={ \
            :set (\$monitorTrafficData->\"$interface\"->\"enable\") true; \
            :local up (\$monitorTrafficConfig->\"interfaces\"->\"$interface\"->\"up\"); \
            :if ([:len [/system script find where name=\"\$up\"]] > 0) do={ \
                /system script run \"\$up\"; \
            }; \
            :delay (\$monitorTrafficConfig->\"delayForUp\"); \
        }; \
        :set (\$monitorTrafficData->\"$interface\") {\"enable\"=true; \"data\"={\"count\"=0;\"sum\"=0;\"average\"=0}}; \
        /interface monitor-traffic $interface interval=(\$monitorTrafficConfig->\"interval\") duration=(\$monitorTrafficConfig->\"duration\") do={ \
            :global monitorTrafficData; \
            :local data (\$monitorTrafficData->\"$interface\"->\"data\"); \
            :local count ((\$data->\"count\") + 1); \
            :local sum ((\$data->\"sum\") + (\$\"rx-bits-per-second\")); \
            :set (\$monitorTrafficData->\"$interface\"->\"data\") {\"count\"=\$count;\"sum\"=\$sum;\"average\"=(\$sum / \$count)}; \
        }; \
        :local rxAverage (\$monitorTrafficConfig->\"interfaces\"->\"$interface\"->\"rx-average\"); \
        :local interfaceAverage (\$monitorTrafficData->\"$interface\"->\"data\"->\"average\"); \
        :if (\$interfaceAverage < \$rxAverage) do={ \
            :set (\$monitorTrafficData->\"$interface\"->\"enable\") false; \
            :local down (\$monitorTrafficConfig->\"interfaces\"->\"$interface\"->\"down\"); \
            :if ([:len [/system script find where name=\"\$down\"]] > 0) do={ \
                /system script run \"\$down\"; \
            }; \
        }; \
    };";
}

File: /sources\tool\monitor\readme-monitor.txt
PASOS PARA INSTALACION

1 - Configurar los parametros en el archivo config-monitor-traffic.

2 - Agregar al repositorio de scritps los siguientes scripts:
    - config-monitor-traffic
    - monitor-traffic
    
3 - Crear un scheduler para correr al inicio del router los scripts:
    - config-monitor-traffic

4 - Crear un scheduler para correr periodicamente entre 5 y 60 minutos el siguiente script:
    - monitor-traffic

5 - Reiniciar el router.

File: /sources\tool\others\config-module.rsc
:global config;
:set config { \
    "telegram"={ \
        "botToken"="XXXXXXXXXX:XXXX_XXXXXXXXXXXXXXXX_XXXXX-XXXXXXX"; \
        "chatID"="XXXXXXXXX" \
    }; \
    "dyndns"={ \
        "user"="dyndnsUser"; \
        "password"="dyndnsPassword"; \
        "host"="dyndnsHost"; \
        "interface"="publicInterface" \
    } \
};

:global telegramBotToken "XXXXXXXXXX:XXXX_XXXXXXXXXXXXXXXX_XXXXX-XXXXXXX";
:global telegramChatID "XXXXXXXXX";

File: /sources\tool\others\create-address-list.rsc
{
:local listPar "VLAN55-PAR";
:local listImpar "VLAN55-IMPAR";
:local ipPrefix "192.168.55.";

:for index from=1 to=254 do={
    if (($index % 2) = 0) do={
        /ip firewall address-list add list="$listPar" address="$ipPrefix$index";
    } else={
        /ip firewall address-list add list="$listImpar" address="$ipPrefix$index";
    }
}
}

File: /sources\tool\others\dhcp-client.rsc
:local dhcpBound $bound;
:local dhcpServerAddress $"server-address";
:local dhcpLeaseAddress $"lease-address";
:local dhcpInterface $interface;
:local dhcpGatewayAddress $"gateway-address";
:local dhcpVendorSpecific $"vendor-specific";
:local dhcpLeaseOptions $"lease-options";
:local strDhcpLeaseOptions [:tostr $dhcpLeaseOptions];

/log info "bound: $dhcpBound";
/log info "server-address: $dhcpServerAddress";
/log info "lease-address: $dhcpLeaseAddress";
/log info "interface: $dhcpInterface";
/log info "gateway-address: $dhcpGatewayAddress";
/log info "vendor-specific: $dhcpVendorSpecific";
/log info "lease-options: $strDhcpLeaseOptions";

# DHCP CLIENT SCRIPT (VALID)
:local interfacename "ether1";
:local wan1newgw [ip dhcp-client get [find interface=$interfacename] gateway];
:local wan1routegw [/ip route get [find comment="WAN1"] gateway ];
:if ($wan1newgw != $wan1routegw) do={
     /ip route set [find comment="WAN1"] gateway="$wan1newgw%$interfacename";	 
	 /ip route set [find comment="WAN1MARK"] gateway="$wan1newgw%$interfacename";
}

# DHCP CLIENT SCRIPT (BEST)
:local dhcpGatewayAddress $"gateway-address";
:if ($bound = 1) do={
    /ip route set [find comment~"WAN1" gateway!="$dhcpGatewayAddress%$interface"] gateway="$dhcpGatewayAddress%$interface";
}





File: /sources\tool\others\dhcp-server.rsc
/log info "leaseBound : $leaseBound";
/log info "leaseServerName : $leaseServerName";
/log info "leaseActMAC : $leaseActMAC";
/log info "leaseActIP : $leaseActIP";
/log info ("lease-hostname : " . $"lease-hostname");
/log info ("lease-options : " . [:tostr $"lease-options"]);

File: /sources\tool\others\hex.rsc
:global byteToHex;
:set byteToHex do={
    :local byte [:tonum $1];
    do {
        :return "$[:pick "0123456789ABCDEF" (($byte >> 4) & 0xF)]$[:pick "0123456789ABCDEF" ($byte & 0xF)]";
    } on-error={
        :return "";
    }
}

:global byteToChar;
:set byteToChar do={
    :global byteToHex;
    :local hex [$byteToHex $1];
    :local result [:parse "{:return \"\\$hex\";}"];
    return [$result];
}

:for i from=0x00 to=0xFF do={
    :put [$byteToChar $i];
}



:global charToByte;
:set charToByte do={
    :local hexDigits "0123456789ABCDEF";
    :for i from=0 to=255 do={
        :put "$[:pick $hexDigits (($i >> 4) & 0xF)]$[:pick $hexDigits ($i & 0xF)]";
    }
}


File: /sources\tool\others\read.rsc
:global readKey do={
    :return [/terminal inkey];
}

:global readLn do={
    :local msg "$1";
    :local line "";
    :local key;
    do {
        :put "$msg$line  ";
        :set key [/terminal inkey];
        :if ($key != 8) do={
            :set line "$line$key";        
        } else={
            :set line [:pick $line 0 ([:len $line]-1)];
        }
        /terminal cuu;
    } while=($key!=13);
    :return $line;
}

File: /sources\tool\romon\config-romon.rsc
:global romons;

:set romons \
{\
    "CC:54:00:00:00:02"=\
    {\
        "interface"=\
        {\
            "bridges"=\
            {\
                "bridge"=\
                {\
                    "pvid"="100";\
                    "port"=\
                    {\
                        {\
                            "ports"="ether1,ether2,ether3,ether4,ether5,ether6,ether7,ether8,ether9,ether10,ether11,ether12\
                                    ether13,ether14,ether15,ether16,ether17,ether18,ether19,ether20,ether21,ether22,ether23,ether24\
                                    ether25,ether26,ether27,ether28,ether29,ether30,ether31,ether32,ether33,ether34,ether35,ether36\
                                    ether37,ether38,ether39,ether40,ether41,ether42,ether43,ether44,ether45,ether46,\
                                    ether49,ether50,ether51,ether52,ether53,ether54,bonding-lan";\
                            "pvid"="10"\
                        }\
                    };\
                    "vlan"=\
                    {\
                        "10,20,30,40,50,100"=\
                        {\
                            "tagged"="ether49,ether50,ether51,ether52"\
                        }\
                    }\
                }\
            }\
        }\
    }\
};

:put $romons;

:set romons {"CC:54:00:00:00:02"={"interface"={"bridges"={"bridge"={"pvid"="100";"ports"={"pvids"={"10"="ether1"}};"vlans"={"10,20,30,40,50,100"={"tagged"="ether49,ether50,ether51,ether52"}}}}}}};
:put $romons;

:foreach id,value in=$romons do={
    :put $id;
    :local bridges ($value->"interface"->"bridges");
    :foreach bridgeName,bridgeValue in=$bridges do={
        :put "bridgeName: $bridgeName";
        :put ("pvid: " . ($bridgeValue->"pvid"));
        :put ($bridgeValue->"ports"->"pvids");
    };
};

                        "ether1,ether2,ether3,ether4,ether5,ether6,ether7,ether8,ether9,ether10,ether11,ether12\
                        ether13,ether14,ether15,ether16,ether17,ether18,ether19,ether20,ether21,ether22,ether23,ether24\
                        ether25,ether26,ether27,ether28,ether29,ether30,ether31,ether32,ether33,ether34,ether35,ether36\
                        ether37,ether38,ether39,ether40,ether41,ether42,ether43,ether44,ether45,ether46,\
                        ether49,ether50,ether51,ether52,ether53,ether54,bonding-lan"=\


                            "10"="ether1,ether2,ether3,ether4,ether5,ether6,ether7,ether8,ether9,ether10,ether11,ether12\
                                  ether13,ether14,ether15,ether16,ether17,ether18,ether19,ether20,ether21,ether22,ether23,ether24\
                                  ether25,ether26,ether27,ether28,ether29,ether30,ether31,ether32,ether33,ether34,ether35,ether36\
                                  ether37,ether38,ether39,ether40,ether41,ether42,ether43,ether44,ether45,ether46,\
                                  ether49,ether50,ether51,ether52,ether53,ether54,bonding-lan";\

:set gModules \
{\
    "01"=\
    {\
        "name"="module-functions";\
        "enable"=true;\
        "loaded"=false;\
        "config"=false;\
        "description"="Funciones Generales."\
    };\
    "02"=\
    {\
        "name"="module-dyndns";\
        "enable"=false;\
        "loaded"=false;\
        "config"=true;\
        "description"="DynDNS Update."\
    };\
    "03"=\
    {\
        "name"="module-pcc-init";\
        "enable"=false;\
        "loaded"=false;\
        "config"=true;\
        "description"="Inicializacion de modulo de balanceo por PCC."\
    };\
    "04"=\
    {\
        "name"="module-geoip";\
        "enable"=true;\
        "loaded"=false;\
        "config"=false;\
        "description"="Herramienta para localizar IP geograficamente."\
    };\
    "05"=\
    {\
        "name"="module-arrays";\
        "enable"=true;\
        "loaded"=false;\
        "config"=false;\
        "description"="Funciones para manejo de arreglos."\
    };\
    "06"=\
    {\
        "name"="module-hex";\
        "enable"=true;\
        "loaded"=false;\
        "config"=false;\
        "description"="Funciones manejo de hexadecimal."\
    };\
    "07"=\
    {\
        "name"="module-base32";\
        "enable"=true;\
        "loaded"=false;\
        "config"=false;\
        "description"="Funciones Base32."\
    };\    
    "08"=\
    {\
        "name"="module-sha1";\
        "enable"=true;\
        "loaded"=false;\
        "config"=false;\
        "description"="Funciones sha1 digest."\
    };\
    "09"=\
    {\
        "name"="module-hmac";\
        "enable"=true;\
        "loaded"=false;\
        "config"=false;\
        "description"="Funciones hmac."\
    };\
    "10"=\
    {\
        "name"="module-time";\
        "enable"=true;\
        "loaded"=false;\
        "config"=false;\
        "description"="Funciones timestamp."\
    };\
    "11"=\
    {\
        "name"="module-totp";\
        "enable"=true;\
        "loaded"=false;\
        "config"=false;\
        "description"="Funciones TOTP."\
    }\
}

:global gScripts;
:set gScripts \
{\
    "init"=\
    {\
        "startRun"=0;\
        "endRun"=0;\
        "enable"=true;\
        "startDate"="";\
        "startTime"="startup";\
        "interval"=0m;\
        "description"="Inicializacion del MSF."\
    };\
    "script-pcc-qos-wan"=\
    {\
        "startRun"=0;\
        "endRun"=0;\
        "enable"=true;\
        "startDate"="";\
        "startTime"="startup";\
        "interval"=10m;\
        "description"="PCC QoS para interfaces WAN."\
    };\
    "script-dyndns"=\
    {\
        "startRun"=0;\
        "endRun"=0;\
        "enable"=true;\
        "startDate"="";\
        "startTime"="startup";\
        "interval"=5m;\
        "description"="Dyndns Update."\
    }\
}

#TODO-END

$setLastError 0 ("$lScriptName cargado.");

File: /sources\tool\romon\module-romon.rsc
#Version: 3.0 alpha
#Fecha: 22-03-2020
#RouterOS 6.46.4 y superior.
#Comentario: 

:global romonId;
:global romonUser;

:global setRomonTarget;
:global setRomonTarget do={
    :global romonId;
    :global romonUser;
    :if (([:len $1] > 0) or ([:len $id] > 0)) do={
        :set romonId "$1$id";
    }
    
    :if (([:len $user] > 0)) do={
        :set romonUser "$user";
    }
}

:global executeRomonCommand;

:global executeRomonCommand do={
    :global romonId;
    :global romonUser;
    /tool romon ssh address=$romonId user=$romonUser command=$romonCommand;
}

:global setRomonIdentity;

:global setRomonIdentity do={
    :global executeRomonCommand;
    :local command "/system identity set name=\"$1\"";
    :put "$command";
    $executeRomonCommand romonCommand=$command;
}

:global setInterfacePVID;

:global setInterfacePVID do={
    :global executeRomonCommand;
    :local command "/interface bridge port set [find bridge=$1 interface=$2] pvid=$3";
    $executeRomonCommand romonCommand=$command;
}

:global setInterfaceTaggetVLAN;

:global setInterfaceTaggetVLAN do={
    :global executeRomonCommand;
    :local command "{\
    :local bridgeName \"$1\";\
    :local vlanIds [:toarray \"$2\"];\
    :local interfaceNames [:toarray \"$3\"];\
    :foreach vlanId in=\$vlanIds do={\
        :put \"VLAN: \$vlanId\";\
        :local id [/interface bridge vlan find where vlan-ids~\"\$vlanId\"];\
        :if (([:len \$id] = 0)) do={\
            :local interfaceName \"\";\
            :foreach iName in=\$interfaceNames do={\
                :set interfaceName \"\$interfaceName,\$iName\";\
            };\
             /interface bridge vlan add bridge=\$bridgeName vlan-ids=\$vlanId tagged=\"\$interfaceName\";\
        } else={\
            :foreach iName in=\$interfaceNames do={\
                :local tagged [/interface bridge vlan get \$id tagged];\
                :local interfaceName \"\";\
                :foreach iTagged in=\$tagged do={\
                    :if ([:len \$interfaceName] = 0) do={\
                        :set interfaceName \"\$iTagged\";\
                    } else={\
                        :set interfaceName \"\$interfaceName,\$iTagged\";\
                    }\
                };\
                :put \"Interface: \$iName - Current: \$interfaceName\";\
                :if (!(\$interfaceName~\$iName)) do={\
                    :set interfaceName \"\$interfaceName,\$iName\";\
                    /interface bridge vlan set \$id tagged=\"\$interfaceName\";\
                }\
            };\
        }\
    };\
:put \"EXECUTE\"}";
    $executeRomonCommand romonCommand=$command;
}

{
    :local bridgeName "$1";
    :local vlanIds [:toarray "$2"];
    :local interfaceNames [:toarray "$3"];
    :foreach vlanId in=$vlanIds do={
        :local id [/interface bridge vlan find where vlan-ids~"$vlanId"];
        :if (([:len $id] = 0)) do={
            :local interfaceName "";
            :foreach iName in=$interfaceNames do={
                :set interfaceName "$interfaceName,$iName";
            };
             /interface bridge vlan add bridge=$bridgeName vlan-ids=$vlanId tagged="$interfaceName";
        } else={
            :foreach iName in=$interfaceNames do={
                :local tagged [/interface bridge vlan get $id tagged];
                :local interfaceName "";
                :foreach iTagged in=$tagged do={
                    :if ([:len $interfaceName] = 0) do={
                        :set interfaceName "$iTagged";
                    } else={
                        :set interfaceName "$interfaceName,$iTagged";
                    }
                };
                :if (!($interfaceName~$iName)) do={
                    :set interfaceName "$interfaceName,$iName";
                    /interface bridge vlan set $id tagged="$interfaceName";
                }
            };
        }
    }
}

{
    :local ethers [/interface ethernet find];
~
    :foreach ether in=$ethers do={
        :local name [/interface ethernet get $ether name];
        do {
            /interface bridge port add bridge="bridge" interface=$name pvid=10;
        } on-error={
            :put "Error al agregar interface $name";
        }
    }
}

#DHCP Script
/log info message=("Lease $leaseBound - $leaseActIP - " . $"lease-hostname");
:if ($leaseBound = 1) do={
    /ip dns static add address=$leaseActIP name=($"lease-hostname" . ".ccvc.local");
}

/interface bridge
add name=bridge pvid=100 vlan-filtering=yes
/interface bridge port
add bridge=bridge interface=ether1 pvid=10
add bridge=bridge interface=ether2 pvid=10
add bridge=bridge interface=ether3 pvid=10
add bridge=bridge interface=ether4 pvid=10
add bridge=bridge interface=ether5 pvid=10
add bridge=bridge interface=ether6 pvid=10
add bridge=bridge interface=ether7 pvid=10
add bridge=bridge interface=ether8 pvid=10
add bridge=bridge interface=ether9 pvid=10
add bridge=bridge interface=ether10 pvid=10
add bridge=bridge interface=ether11 pvid=10
add bridge=bridge interface=ether12 pvid=10
add bridge=bridge interface=ether13 pvid=10
add bridge=bridge interface=ether14 pvid=10
add bridge=bridge interface=ether15 pvid=10
add bridge=bridge interface=ether16 pvid=10
add bridge=bridge interface=ether17 pvid=10
add bridge=bridge interface=ether18 pvid=10
add bridge=bridge interface=ether19 pvid=10
add bridge=bridge interface=ether20 pvid=10
add bridge=bridge interface=ether21 pvid=10
add bridge=bridge interface=ether22 pvid=10
add bridge=bridge interface=ether23 pvid=10
add bridge=bridge interface=ether24 pvid=10
add bridge=bridge interface=ether25 pvid=10
add bridge=bridge interface=ether26 pvid=10
/interface bridge vlan
add bridge=bridge tagged=ether25,ether26 vlan-ids=100
add bridge=bridge tagged=ether25,ether26 vlan-ids=10
/ip dhcp-client
remove 0
add disabled=no interface=bridge






















File: /sources\tool\romon\module-var.rsc
#Version: 3.0 alpha
#Fecha: 22-03-2020
#RouterOS 6.46.4 y superior.
#Comentario: 

:global toStringValue;
:set toStringValue do={
    :global toStringValue;
    :local inputVar $1;
    :local stringValue "";
        
    :if ([:typeof $inputVar] = "str") do={
        :set stringValue "\"$inputVar\"";
    } else={
        :if ([:typeof $inputVar] = "array") do={
            :if ([:len $inputVar] > 0) do={
                :foreach k,v in=$inputVar do={
                    :if ([:typeof $k] = "str") do={
                        :set stringValue ($stringValue . "\"" . $k ."\"=" . [$toStringValue $v] . ";");
                    } else={
                        :set stringValue ($stringValue . [$toStringValue $v] . ";");
                    }
                }
                :set stringValue ("{" . [:pick $stringValue 0 ([:len $stringValue] - 1)]. "}");
            } else={
                :set stringValue "[:toarray \"\"]";
            }
        } else={
            :set stringValue $inputVar;
        }
    }
    :return $stringValue;
}

File: /sources\tool\romon\vtp\config-romon.rsc
{

:global config;
:if ([:typeof $config] != "array") do={
    :set $config [:toarray ""];
}

:global vtp [:toarray ""];

:set ($vtp->"SwitchCore") \
{\
    "romonId"="CC:00:00:00:00:02";\
    "romonUser"="admin";\
    "identity"="Switch Core";\
    "bridges"=\
    {\
        "bridge"=\
        {\
            "pvid"="1";\
            "ports"=\
            {\
                "ether1"={"pvid"="1"};\
                "ether2"={"pvid"="1"};\
                "ether3"={"pvid"="1"};\
                "ether4"={"pvid"="1"};\
                "ether5"={"pvid"="1"};\
                "ether6"={"pvid"="1"};\
                "ether7"={"pvid"="1"};\
                "ether8"={"pvid"="1"};\
                "ether9"={"pvid"="1"};\
                "ether10"={"pvid"="1"};\
                "ether11"={"pvid"="1"};\
                "ether12"={"pvid"="1"};\
                "ether13"={"pvid"="1"};\
                "ether14"={"pvid"="1"};\
                "ether15"={"pvid"="1"};\
                "ether16"={"pvid"="1"};\
                "ether17"={"pvid"="1"};\
                "ether18"={"pvid"="1"};\
                "ether19"={"pvid"="1"};\
                "ether20"={"pvid"="1"};\
                "ether21"={"pvid"="1"};\
                "ether22"={"pvid"="1"};\
                "ether23"={"pvid"="1"};\
                "ether24"={"pvid"="1"}\
            };\
            "vlans"=\
            {\
                "10,20,30,100"=\
                {\
                    "tagged"="ether21,ether22,ether23,ether24";\
                    "untagged"=""\
                };\
                "10"=\
                {\
                    "tagged"="ether1";\
                    "untagged"=""\
                }\
            }\
        }\
    }\
};

:set ($config->"vtp") $vtp;

:foreach id,vtpItem in=$vtp do={
    :put "";
    :put "Id       : $id";
    :put "romonId  : $($vtpItem->"romonId")";
    :put "romonUser: $($vtpItem->"romonUser")";
    :put "identity : $($vtpItem->"identity")";
    
    :foreach bridgeName,bridgeItem in=($vtpItem->"bridges") do={
        :put "";
        :put "    bridge  : $bridgeName";
        :put "    PVID    : $($bridgeItem->"pvid")";

        :foreach etherName,etherItem in=($bridgeItem->"ports") do={
            :put "        ether: $etherName, PVID: $($etherItem->"pvid")";
        }
        :foreach vlans,vlanItem in=($bridgeItem->"vlans") do={
            :put "        vlans: $vlans, tagged: $($vlanItem->"tagged")";
        }
    }    
}

}

File: /sources\tool\romon\vtp\config-vtp.rsc
:global romons;

:set romons \
{\
    "CC:54:00:00:00:02"=\
    {\
        "interface"=\
        {\
            "bridges"=\
            {\
                "bridge"=\
                {\
                    "pvid"="100";\
                    "port"=\
                    {\
                        {\
                            "ports"="ether1,ether2,ether3,ether4,ether5,ether6,ether7,ether8,ether9,ether10,ether11,ether12\
                                    ether13,ether14,ether15,ether16,ether17,ether18,ether19,ether20,ether21,ether22,ether23,ether24\
                                    ether25,ether26,ether27,ether28,ether29,ether30,ether31,ether32,ether33,ether34,ether35,ether36\
                                    ether37,ether38,ether39,ether40,ether41,ether42,ether43,ether44,ether45,ether46,\
                                    ether49,ether50,ether51,ether52,ether53,ether54,bonding-lan";\
                            "pvid"="10"\
                        }\
                    };\
                    "vlan"=\
                    {\
                        "10,20,30,40,50,100"=\
                        {\
                            "tagged"="ether49,ether50,ether51,ether52"\
                        }\
                    }\
                }\
            }\
        }\
    }\
};

:put $romons;

:set romons {"CC:54:00:00:00:02"={"interface"={"bridges"={"bridge"={"pvid"="100";"ports"={"pvids"={"10"="ether1"}};"vlans"={"10,20,30,40,50,100"={"tagged"="ether49,ether50,ether51,ether52"}}}}}}};
:put $romons;

:foreach id,value in=$romons do={
    :put $id;
    :local bridges ($value->"interface"->"bridges");
    :foreach bridgeName,bridgeValue in=$bridges do={
        :put "bridgeName: $bridgeName";
        :put ("pvid: " . ($bridgeValue->"pvid"));
        :put ($bridgeValue->"ports"->"pvids");
    };
};

                        "ether1,ether2,ether3,ether4,ether5,ether6,ether7,ether8,ether9,ether10,ether11,ether12\
                        ether13,ether14,ether15,ether16,ether17,ether18,ether19,ether20,ether21,ether22,ether23,ether24\
                        ether25,ether26,ether27,ether28,ether29,ether30,ether31,ether32,ether33,ether34,ether35,ether36\
                        ether37,ether38,ether39,ether40,ether41,ether42,ether43,ether44,ether45,ether46,\
                        ether49,ether50,ether51,ether52,ether53,ether54,bonding-lan"=\


                            "10"="ether1,ether2,ether3,ether4,ether5,ether6,ether7,ether8,ether9,ether10,ether11,ether12\
                                  ether13,ether14,ether15,ether16,ether17,ether18,ether19,ether20,ether21,ether22,ether23,ether24\
                                  ether25,ether26,ether27,ether28,ether29,ether30,ether31,ether32,ether33,ether34,ether35,ether36\
                                  ether37,ether38,ether39,ether40,ether41,ether42,ether43,ether44,ether45,ether46,\
                                  ether49,ether50,ether51,ether52,ether53,ether54,bonding-lan";\

/tool fetch url="https://api.telegram.org/bot1200682853:AAGs_3qqqaFZhz43Kk69X_DSesk-pvVARDs/sendMessage\?chat_id=617220857&text=Mikrotik test message" keep-result=no

:set gModules \
{\
    "01"=\
    {\
        "name"="module-functions";\
        "enable"=true;\
        "loaded"=false;\
        "config"=false;\
        "description"="Funciones Generales."\
    };\
    "02"=\
    {\
        "name"="module-dyndns";\
        "enable"=false;\
        "loaded"=false;\
        "config"=true;\
        "description"="DynDNS Update."\
    };\
    "03"=\
    {\
        "name"="module-pcc-init";\
        "enable"=false;\
        "loaded"=false;\
        "config"=true;\
        "description"="Inicializacion de modulo de balanceo por PCC."\
    };\
    "04"=\
    {\
        "name"="module-geoip";\
        "enable"=true;\
        "loaded"=false;\
        "config"=false;\
        "description"="Herramienta para localizar IP geograficamente."\
    };\
    "05"=\
    {\
        "name"="module-arrays";\
        "enable"=true;\
        "loaded"=false;\
        "config"=false;\
        "description"="Funciones para manejo de arreglos."\
    };\
    "06"=\
    {\
        "name"="module-hex";\
        "enable"=true;\
        "loaded"=false;\
        "config"=false;\
        "description"="Funciones manejo de hexadecimal."\
    };\
    "07"=\
    {\
        "name"="module-base32";\
        "enable"=true;\
        "loaded"=false;\
        "config"=false;\
        "description"="Funciones Base32."\
    };\    
    "08"=\
    {\
        "name"="module-sha1";\
        "enable"=true;\
        "loaded"=false;\
        "config"=false;\
        "description"="Funciones sha1 digest."\
    };\
    "09"=\
    {\
        "name"="module-hmac";\
        "enable"=true;\
        "loaded"=false;\
        "config"=false;\
        "description"="Funciones hmac."\
    };\
    "10"=\
    {\
        "name"="module-time";\
        "enable"=true;\
        "loaded"=false;\
        "config"=false;\
        "description"="Funciones timestamp."\
    };\
    "11"=\
    {\
        "name"="module-totp";\
        "enable"=true;\
        "loaded"=false;\
        "config"=false;\
        "description"="Funciones TOTP."\
    }\
}

:global gScripts;
:set gScripts \
{\
    "init"=\
    {\
        "startRun"=0;\
        "endRun"=0;\
        "enable"=true;\
        "startDate"="";\
        "startTime"="startup";\
        "interval"=0m;\
        "description"="Inicializacion del MSF."\
    };\
    "script-pcc-qos-wan"=\
    {\
        "startRun"=0;\
        "endRun"=0;\
        "enable"=true;\
        "startDate"="";\
        "startTime"="startup";\
        "interval"=10m;\
        "description"="PCC QoS para interfaces WAN."\
    };\
    "script-dyndns"=\
    {\
        "startRun"=0;\
        "endRun"=0;\
        "enable"=true;\
        "startDate"="";\
        "startTime"="startup";\
        "interval"=5m;\
        "description"="Dyndns Update."\
    }\
}

#TODO-END

$setLastError 0 ("$lScriptName cargado.");

File: /sources\tool\romon\vtp\module-vtp-client.rsc
do {
    :put "Cargando setInterfaceTaggetVLAN...";
    :global setInterfaceTaggetVLAN;
    :set setInterfaceTaggetVLAN do={
        :local bridgeName "$1";
        :local vlanIds [:toarray "$2"];
        :local interfaceNames [:toarray "$3"];
        :put "vlanIds: $[:tostr $vlanIds]";
        :put "interfaceNames: $[:tostr $interfaceNames]";
        :foreach vlanId in=$vlanIds do={
            :local id [/interface bridge vlan find where vlan-ids="$vlanId" dynamic=no];
            :if (([:len $id] = 0)) do={
                :local interfaceName "";
                :foreach iName in=$interfaceNames do={
                    :set interfaceName "$interfaceName,$iName";
                };
                do {
                    :put "Creando VLAN en: $bridgeName / $vlanId / $interfaceName";
                    /interface bridge vlan add bridge=$bridgeName vlan-ids=$vlanId tagged="$interfaceName";
                } on-error={
                    :put "ERROR creando VLAN en: $bridgeName / $vlanId / $interfaceName";
                }
            } else={
                :foreach iName in=$interfaceNames do={
                    :local tagged [/interface bridge vlan get $id tagged];
                    :local interfaceName "";
                    :foreach iTagged in=$tagged do={
                        :if ([:len $interfaceName] = 0) do={
                            :set interfaceName "$iTagged";
                        } else={
                            :set interfaceName "$interfaceName,$iTagged";
                        }
                    };
                    :if (!($interfaceName~$iName)) do={
                        :set interfaceName "$interfaceName,$iName";
                        /interface bridge vlan set $id tagged="$interfaceName";
                    }
                };
            }
        }
    }
} on-error={
    :put "ERROR cargando modulo.";
}

File: /sources\tool\romon\vtp\module-vtp.rsc
#Version: 3.0 alpha
#Fecha: 22-03-2020
#RouterOS 6.46.4 y superior.
#Comentario: 


:global toSafeRomonCommand do={
    :local command $1;
    :local safeCommand "";
    :local lastLetter "";
    :local currentLetter "";
    :local hexChar "";
    :for i from=0 to=[:len $command] do={
        :set currentLetter [:pick $command $i];
        :if (!(($currentLetter = "\r") or ($currentLetter = "\n"))) do={
            :set safeCommand "$safeCommand$currentLetter";
        }
        :set lastLetter $currentLetter;
    }
    :return $safeCommand;
}

:put [$toSafeRomonCommand $script]

#Function executeRomonCommand
#   Parametros:
#   $1: romon address
#   $2: romon user
#   $3: command
#   Comentario:
#   Retorna:

:global executeRomonCommand;
:set executeRomonCommand do={
    /tool romon ssh address=$1 user=$2 command=$3;
}

#Function setRomonIdentity
#   Parametros:
#   $1: romon address
#   $2: romon user
#   $3: identity
#   Comentario:
#   Retorna:

:global setRomonIdentity;
:global setRomonIdentity do={
    :global executeRomonCommand;
    :local command "/system identity set name=\"$3\"";
    $executeRomonCommand $1 $2 $command;
}

#Function setInterfacePVID
#   Parametros:
#   $1: romon address
#   $2: romon user
#   $3: brigge
#   $4: interface
#   $5: pvid
#   Comentario:
#   Retorna:

:global setInterfacePVID;
:global setInterfacePVID do={
    :global executeRomonCommand;
    :local command "/interface bridge port set [find bridge=$3 interface=$4] pvid=$5";
    $executeRomonCommand $1 $2 $command;
}

#Function setInterfaceTaggetVLAN
#   Parametros:
#   $1: romon address
#   $2: romon user
#   $3: brigge
#   $4: interfaces
#   $5: vlans
#   Comentario:
#   Retorna:

:global setInterfaceTaggetVLAN;
:global setInterfaceTaggetVLAN do={
    :global executeRomonCommand;
    :local command "{\
    :local bridgeName \"$3\";\
    :local vlanIds [:toarray \"$5\"];\
    :local interfaceNames [:toarray \"$4\"];\
    :foreach vlanId in=\$vlanIds do={\
        :put \"VLAN: \$vlanId\";\
        :local id [/interface bridge vlan find where vlan-ids~\"\$vlanId\" dynamic=no];\
        :if (([:len \$id] = 0)) do={\
            :local interfaceName \"\";\
            :foreach iName in=\$interfaceNames do={\
                :set interfaceName \"\$interfaceName,\$iName\";\
            };\
             /interface bridge vlan add bridge=\$bridgeName vlan-ids=\$vlanId tagged=\"\$interfaceName\";\
        } else={\
            :foreach iName in=\$interfaceNames do={\
                :local tagged [/interface bridge vlan get \$id tagged];\
                :local interfaceName \"\";\
                :foreach iTagged in=\$tagged do={\
                    :if ([:len \$interfaceName] = 0) do={\
                        :set interfaceName \"\$iTagged\";\
                    } else={\
                        :set interfaceName \"\$interfaceName,\$iTagged\";\
                    }\
                };\
                :put \"Interface: \$iName - Current: \$interfaceName\";\
                :if (!(\$interfaceName~\$iName)) do={\
                    :set interfaceName \"\$interfaceName,\$iName\";\
                    /interface bridge vlan set \$id tagged=\"\$interfaceName\";\
                }\
            };\
        }\
    };\
    :put \"EXECUTE\"}";
    $executeRomonCommand $1 $2 $command;
}



#############################################################

/system reset-configuration no-defaults=yes skip-backup=yes;
/tool romon set enabled=yes id="CC:00:00:00:00:01";

:global setInterfaceTaggetVLAN do={
    :local bridgeName "$1";
    :local vlanIds [:toarray "$2"];
    :local interfaceNames [:toarray "$3"];
    :put "vlanIds: $[:tostr $vlanIds]";
    :put "interfaceNames: $[:tostr $interfaceNames]";
    :foreach vlanId in=$vlanIds do={
        :local id [/interface bridge vlan find where vlan-ids="$vlanId" dynamic=no];
        :if (([:len $id] = 0)) do={
            :local interfaceName "";
            :foreach iName in=$interfaceNames do={
                :set interfaceName "$interfaceName,$iName";
            };
            do {
                :put "Creando VLAN en: $bridgeName / $vlanId / $interfaceName";
                /interface bridge vlan add bridge=$bridgeName vlan-ids=$vlanId tagged="$interfaceName";
            } on-error={
                :put "ERROR creando VLAN en: $bridgeName / $vlanId / $interfaceName";
            }
        } else={
            :foreach iName in=$interfaceNames do={
                :local tagged [/interface bridge vlan get $id tagged];
                :local interfaceName "";
                :foreach iTagged in=$tagged do={
                    :if ([:len $interfaceName] = 0) do={
                        :set interfaceName "$iTagged";
                    } else={
                        :set interfaceName "$interfaceName,$iTagged";
                    }
                };
                :if (!($interfaceName~$iName)) do={
                    :set interfaceName "$interfaceName,$iName";
                    /interface bridge vlan set $id tagged="$interfaceName";
                }
            };
        }
    }
}

{
    :local ethers [/interface ethernet find];
    
    :foreach ether in=$ethers do={
        :local name [/interface ethernet get $ether name];
        do {
            /interface bridge port add bridge="bridge" interface=$name;
        } on-error={
            :put "Error al agregar interface $name";
        }
    }
}

#DHCP Script
/log info message=("Lease $leaseBound - $leaseActIP - " . $"lease-hostname");
:if ($leaseBound = 1) do={
    /ip dns static add address=$leaseActIP name=($"lease-hostname" . ".ccvc.local");
}

/interface bridge
add name=bridge pvid=100 vlan-filtering=yes
/interface bridge port
add bridge=bridge interface=ether1 pvid=10
add bridge=bridge interface=ether2 pvid=10
add bridge=bridge interface=ether3 pvid=10
add bridge=bridge interface=ether4 pvid=10
add bridge=bridge interface=ether5 pvid=10
add bridge=bridge interface=ether6 pvid=10
add bridge=bridge interface=ether7 pvid=10
add bridge=bridge interface=ether8 pvid=10
add bridge=bridge interface=ether9 pvid=10
add bridge=bridge interface=ether10 pvid=10
add bridge=bridge interface=ether11 pvid=10
add bridge=bridge interface=ether12 pvid=10
add bridge=bridge interface=ether13 pvid=10
add bridge=bridge interface=ether14 pvid=10
add bridge=bridge interface=ether15 pvid=10
add bridge=bridge interface=ether16 pvid=10
add bridge=bridge interface=ether17 pvid=10
add bridge=bridge interface=ether18 pvid=10
add bridge=bridge interface=ether19 pvid=10
add bridge=bridge interface=ether20 pvid=10
add bridge=bridge interface=ether21 pvid=10
add bridge=bridge interface=ether22 pvid=10
add bridge=bridge interface=ether23 pvid=10
add bridge=bridge interface=ether24 pvid=10
add bridge=bridge interface=ether25 pvid=10
add bridge=bridge interface=ether26 pvid=10
/interface bridge vlan
add bridge=bridge tagged=ether25,ether26 vlan-ids=100
add bridge=bridge tagged=ether25,ether26 vlan-ids=10
/ip dhcp-client
remove 0
add disabled=no interface=bridge





:global setInterfaceTaggetVLAN do={    :local bridgeName "$1";    :local vlanIds [:toarray "$2"];    :local interfaceNames [:toarray "$3"];    :put "vlanIds: $vlanIds";    :put "interfaceNames: $interfaceNames"    :foreach vlanId in=$vlanIds do={        :local id [/interface bridge vlan find where vlan-ids="$vlanId" dynamic=no];        :if (([:len $id] = 0)) do={            :local interfaceName "";            :foreach iName in=$interfaceNames do={                :set interfaceName "$interfaceName,$iName";            };             /interface bridge vlan add bridge=$bridgeName vlan-ids=$vlanId tagged="$interfaceName";        } else={            :foreach iName in=$interfaceNames do={                :local tagged [/interface bridge vlan get $id tagged];                :local interfaceName "";                :foreach iTagged in=$tagged do={                    :if ([:len $interfaceName] = 0) do={                        :set interfaceName "$iTagged";                    } else={                        :set interfaceName "$interfaceName,$iTagged";                    }                };                :if (!($interfaceName~$iName)) do={                    :set interfaceName "$interfaceName,$iName";                    /interface bridge vlan set $id tagged="$interfaceName";                }            };        }    }}
















File: /sources\tool\switch\mac-search.rsc
{
    :local interfaceInfo [:toarray ""];
    
    :local bridges [/interface bridge find];
    
    :foreach id in=$bridges do={
        :local bridgeName [/interface bridge get $id name];
        :put "Bridge: $bridgeName";
        :local vlans [/interface bridge vlan find where bridge=$bridgeName];
        :foreach vid in=$vlans do={
            :local vlanId [/interface bridge vlan get $vid vlan-ids];
            :put "VLAN  : $vlanId";
            :put "";
            :local hosts [/interface bridge host find where local=yes bridge=$bridgeName vid=$vlanId];
            :foreach h in=$hosts do={
                :local i [/interface bridge host get $h];
                :put (($i->"interface") . ": " . ($i->"mac-address"));
            }
        }
    }
}

:global F [:toarray ""];

:set ($F->"f1") do={:put "$1";};

:global f1 ($F->"f1");

File: /sources\tool\telegram\config-module-telegram.rsc
:global config;
:if ([:typeof $config] != "array") do={
    :set $config [:toarray ""];
}

:local telegram {"botToken"=""; "chatID"=""; "updateId"=0};

:set ($config->"telegram") $telegram;

File: /sources\tool\telegram\config-script-telegram-active-users.rsc
:global config;
:if ([:typeof $config] != "array") do={
    :set $config [:toarray ""];
}

:if ([:typeof ($config->"telegram")] = "array" ) do={
    :local activeUsers {"lastUser"=0; "messages"=[:toarray ""]};
    :set ($config->"telegram"->"activeUsers") $activeUsers;
}

File: /sources\tool\telegram\config-script-telegram-log.rsc
:global lastLogId 0;
:global messagesLog ({});

File: /sources\tool\telegram\config-script-telegram-routes.rsc
:global config;
:if ([:typeof $config] != "array") do={
    :set $config [:toarray ""];
}

:if ([:typeof ($config->"telegram")] = "array" ) do={
    :set ($config->"telegram"->"routes") {"list"=[:toarray ""]; "messages"=[:toarray ""]};
}

File: /sources\tool\telegram\module-telegram.rsc
:global encodeUrl;
:set encodeUrl do={
    :local url $1;
    :local safe "";
    :local safeChar {" "="%20"; \
                     "!"="%21"; \
                     "#"="%23"; \
                     "%"="%25"; \
                     "&"="%26"; \
                     "'"="%27"; \
                     "("="%28"; \
                     ")"="%29"; \
                     "*"="%2A"; \
                     "+"="%2B"; \
                     ","="%2C"; \
                     "-"="%2D"; \
                     "."="%2E"; \
                     "/"="%2F"; \
                     ":"="%3A"; \
                     ";"="%3B"; \
                     "<"="%3C"; \
                     ">"="%3E"; \
                     "="="%3D"; \
                     "@"="%40"; \
                     "["="%5B"; \
                     "]"="%5D"; \
                     "^"="%5E"; \
                     "_"="%5F"; \
                     "`"="%60"; \
                     "{"="%7B"; \
                     "|"="%7C"; \
                     "}"="%7D"; \
                     "~"="%7E"};
    
    :set ($safeChar->"\n") "%0A";
    :set ($safeChar->"\"") "%22";
    :set ($safeChar->"\$") "%24";
    :set ($safeChar->"\?") "%3F";
    :set ($safeChar->"\\") "%5C";
    
    :for i from=0 to=([:len $url]-1) do={
        :local char [:pick $url $i];
        :if (($safeChar->$char)!=nil) do={
            :set char ($safeChar->$char);
        }
        :set safe "$safe$char";
    }    
    :return $safe;
}

:global telegramSendMessage;
:set telegramSendMessage do={
    :global encodeUrl;
    :local botToken $1;
    :local isSend false;
    :local params [:toarray ""];
    :local urlParams "";
    
    :if ($2 != nil) do={:set ($params->0) "chat_id=$[$encodeUrl $2]";};
    :if ($3 != nil) do={:set ($params->1) "text=$[$encodeUrl $3]";};
    :if ($4 != nil) do={:set ($params->2) "parse_mode=$[$encodeUrl $4]";};
    :if ($5 != nil) do={:set ($params->3) "reply_to_message_id=$[$encodeUrl $5]";};
    
    :if ([:len $params] > 0) do={
        :set urlParams "\?";
        :foreach p in=$params do={
            :set urlParams "$urlParams$p&";
        }
        :set urlParams [:pick $urlParams 0 ([:len $urlParams]-1)];
    }    
    
    do {
        :local result [/tool fetch url="https://api.telegram.org/bot$botToken/sendMessage$urlParams" output=user as-value];
        :if (($result->"status") = "finished") do={
            :set isSend (($result->"data")~"\"ok\":true");
        }
    } on-error={
        :return $isSend;
    }
    :return $isSend;
}

:global telegramGetUpdates;
:set telegramGetUpdates do={
    :global encodeUrl;
    :local botToken $1;
    :local params [:toarray ""];
    :local urlParams "";
    
    :if ($2 != nil) do={:set ($params->0) "offset=$[$encodeUrl $2]";};
    :if ($3 != nil) do={:set ($params->1) "limit=$[$encodeUrl $3]";};
    
    :if ([:len $params] > 0) do={
        :set urlParams "\?";
        :foreach p in=$params do={
            :set urlParams "$urlParams$p&";
        }
        :set urlParams [:pick $urlParams 0 ([:len $urlParams]-1)];
    }
    
    do {
        :local result [/tool fetch url="https://api.telegram.org/bot$botToken/getUpdates$urlParams" output=user as-value];
        :if (($result->"status") = "finished") do={
            :return ($result->"data");
        }
    } on-error={
        :return "";
    }
    :return "";
}

File: /sources\tool\telegram\script-telegram-active-users.rsc
:if ([:len [/system script job find script="script-telegram-active-users"]] > 1) do={
    :return 255;
}

:global config;
:global telegramSendMessage;

:local botToken ($config->"telegram"->"botToken");
:local chatID ($config->"telegram"->"chatID");

:local addressType;
:set addressType do={
    :local ipAddress [:toip $1];
    :if ([:len $ipAddress] = 0) do={
        :return "UNKNOW";
    }
    :local isPrivate  ((10.0.0.0 = ($ipAddress&255.0.0.0)) \
                        or (172.16.0.0 = ($ipAddress&255.240.0.0)) \
                        or  (192.168.0.0 = ($ipAddress&255.255.0.0)));
    :if ($isPrivate) do={
        :return "PRIVATE";
    }
    :local isReserved ((0.0.0.0 = ($ipAddress&255.0.0.0)) \
                        or (127.0.0.0 = ($ipAddress&255.0.0.0)) \
                        or (169.254.0.0 = ($ipAddress&255.255.0.0)) \
                        or (224.0.0.0 = ($ipAddress&240.0.0.0)) \
                        or (240.0.0.0 = ($ipAddress&240.0.0.0)));
    :if ($isReserved) do={
        :return "RESERVED";
    }
    :return "PUBLIC";
}

:local identity [/system identity get name];

:foreach id in=[/user active find] do={
    :local lastIndex [:tonum ("0x" . [:pick $id 1 [:len $id]])];
    :if (($config->"telegram"->"activeUsers"->"lastUser") < $lastIndex) do={
        :set ($config->"telegram"->"activeUsers"->"lastUser") $lastIndex;
        :local userData [/user active get $id];
        :local name ($userData->"name");
        :local when ($userData->"when");
        :local address ($userData->"address");
        :local via ($userData->"via");
        :local ipType [$addressType $address];
        :if ($ipType="PUBLIC") do={
            :local lUrl "http://ip-api.com/csv/$address?fields=status,message,country,countryCode,as,asname,query";
            :local result [/tool fetch url=$lUrl mode=http as-value output=user];
            :local arrayResult [:toarray ($result->"data")];
            :if ([:typeof $arrayResult] = "array") do={
                :if ([:pick $arrayResult 0] = "success") do={
                    :set ipType "country: *$($arrayResult->2) - $($arrayResult->1)*\n\
                                 as: *$($arrayResult->3)*";
                }
            }
        }
        :set ($config->"telegram"->"activeUsers"->"messages"->"id-$lastIndex") "*Login on: $identity*\n\n\
                                           at: *$when*\n\
                                           user: *$name*\n\
                                           from: *$address*\n\
                                           via: *$via*\n\
                                           $ipType";
    }
}

:foreach id,message in=($config->"telegram"->"activeUsers"->"messages") do={
    :local send [$telegramSendMessage $botToken $chatID $message "Markdown"];    
    :if ($send) do={
        :set ($config->"telegram"->"activeUsers"->"messages"->"$id");
    }
}

File: /sources\tool\telegram\script-telegram-log.rsc
:if ([:len [/system script job find script="script-telegram-log"]] > 1) do={
    :return 255;
}

:global lastLogId;
:global messagesLog;

:global telegramSendMessage;
:global telegramBotToken;
:global telegramChatID;

:local identity [/system identity get name];
:local filterTopics "^(system;error;critical|system;info;account)\$";

:foreach id in=[/log find topics~"$filterTopics"] do={
    :local lastIndex [:tonum ("0x" . [:pick $id 1 [:len $id]])];
    :if ($lastLogId < $lastIndex) do={
        :set lastLogId $lastIndex;
        :local logData [/log get $id];
        :set ($messagesLog->"id-$lastIndex") ($logData->"message");
    }
}

:foreach id,message in=$messagesLog do={
    :local send [$telegramSendMessage $telegramBotToken $telegramChatID $message];
    
    :if ($send) do={
        :set ($messagesLog->"$id");
    }
}

File: /sources\tool\telegram\script-telegram-response.rsc
:if ([:len [/system script job find script="script-telegram-active-users"]] > 1) do={
    :return 255;
}

:global config;
:global telegramSendMessage;
:global telegramGetUpdates;
:global JSONLoads;

:local botToken ($config->"telegram"->"botToken");
:local chatID ($config->"telegram"->"chatID");

:global jsonResponse [$JSONLoads [$telegramGetUpdates $botToken (($config->"telegram"->"updateId") + 1) 1]];

:if (($jsonResponse->"ok") = true) do={
    :if ([:len ($jsonResponse->"result")] = 1) do={
        :local update (($jsonResponse->"result"->0));
        :local message (($jsonResponse->"result"->0->"message"));
        :set ($config->"telegram"->"updateId") ($update->"update_id");
        
        :if (($message->"text") = "/getrbinfo") do={
            :local identity [/system identity get name];
            :local response "*Identity*\n\
                            name: *$identity*\n\n\
                            *Routerboard*\n";
            :foreach k,v in=[/system routerboard get] do={
                :set response "$response$k: *$v*\n";
            }
            :local send [$telegramSendMessage $botToken $chatID $response "Markdown" ($message->"message_id")];    
        }
        
        :if (($message->"text") = "/getwirelessinfo") do={
            :local response "";
            :foreach id in=[/interface wireless find] do={
                :local wl [/interface wireless get $id];
                :set response "*Interface*\n\
                                name: *$($wl->"name")*\n\n\
                                *Monitor*\n";
                :local wlMonitor [/interface wireless monitor $id once as-value];
                :foreach k,v in=$wlMonitor do={
                    :if ($k!=".id") do={
                        :set response "$response$k: *$v*\n";
                    }
                }
            }
            :local send [$telegramSendMessage $botToken $chatID $response "Markdown" ($message->"message_id")];    
        }
    }
}

File: /sources\tool\telegram\script-telegram-routes.rsc
:if ([:len [/system script job find script="script-telegram-routes"]] > 1) do={
    :return 255;
}

:global config;
:global telegramSendMessage;

:local botToken ($config->"telegram"->"botToken");
:local chatID ($config->"telegram"->"chatID");

:local identity [/system identity get name];

:local list ($config->"telegram"->"routes"->"list");
:local messages ($config->"telegram"->"routes"->"messages");

:foreach id in=[/ip route find where comment~"MAIN"] do={
	:local route [/ip route get $id];
	:local icon "\F0\9F\98\81";
	:set icon "\E2\9C\85";
	:if (!($route->"active")) do={
		:set icon "\F0\9F\98\A1";
		:set icon "\E2\9D\8C";
	}
	:local index [:tonum ("0x" . [:pick $id 1 [:len $id]])];
    

    
	:if ([:len ($list->"id-$index")] = 0) do={
		:local identity [/system identity get name];
		:local message "*Identity*\n\
					   name: *$identity*\n\n\
					   *Informacion de ruta* $icon\n";			
		:foreach k,v in=$route do={
			:if ($k!=".id") do={
				:set message "$message$k: *$v*\n";
			}
		}			
        :set ($list->"id-$index") ($route->"active");
        :local length ([:len $messages] + 1);
        :set ($messages->"id-$length") $message;
        
	} else={
		:if (($list->"id-$index") != ($route->"active")) do={
            :local identity [/system identity get name];
            :local message "*Identity*\n\
                           name: *$identity*\n\n\
                           *Informacion de ruta* $icon\n";			
			:foreach k,v in=$route do={
				:if ($k!=".id") do={
					:set message "$message$k: *$v*\n";
				}
			}
            :set ($list->"id-$index") ($route->"active");
            :local length ([:len $messages] + 1);
            :set ($messages->"id-$length") $message;
		}
	}
}
:set ($config->"telegram"->"routes"->"list") $list;
:set ($config->"telegram"->"routes"->"messages") $messages;

:foreach id,message in=($config->"telegram"->"routes"->"messages") do={
    :local send [$telegramSendMessage $botToken $chatID $message "Markdown"];    
    :if ($send) do={
        :set ($config->"telegram"->"routes"->"messages"->"$id");
    }
}


File: /sources\tool\voltage\script-voltage.rsc
:local scriptName "script-voltage";
:if ([:len [/system script job find script=$scriptName]] > 1) do={
    :return 255;
}

:local strVoltage "";
:local strAverage "";
:local currentVoltage [/system health get voltage];
:local currentAverage 0;
:global voltage {"current"=$currentVoltage; "average"=$currentVoltage; count=1};

:while (true) do={
    :set currentVoltage [/system health get voltage];
    :set ($voltage->"current") $currentVoltage;
    :set ($voltage->"average") ($currentVoltage + ($voltage->"average"));
    :set ($voltage->"count") (($voltage->"count") + 1);
    :set currentAverage (($voltage->"average") / ($voltage->"count"));
    
    :set strVoltage "$($currentVoltage / 10).$($currentVoltage % 10)V";
    :set strAverage "$($currentAverage / 10).$($currentAverage % 10)V";
    :put "$strVoltage / $strAverage";
    :delay 1s;
}

{
    :local count 0;
    :while ($count < 3) do={
        :beep frequency=784 length=300ms;
        :delay 300ms;
        :beep frequency=880 length=300ms;
        :delay 200ms;
        :beep frequency=988 length=300ms;
        :delay 200ms;
        :beep frequency=988 length=300ms;
        :delay 200ms;
        :beep frequency=988 length=300ms;
        :delay 200ms;
        :beep frequency=988 length=300ms;
        :delay 200ms;
        :beep frequency=988 length=300ms;
        :delay 200ms;
        :beep frequency=988 length=300ms;
        :delay 400ms;
        :set count ($count + 1);
    }
}






:global messagesLog;

:global telegramSendMessage;
:global telegramBotToken;
:global telegramChatID;

:local identity [/system identity get name];
:local filterTopics "^(system;error;critical|system;info;account)\$";

:foreach id in=[/log find topics~"$filterTopics"] do={
    :local lastIndex [:tonum ("0x" . [:pick $id 1 [:len $id]])];
    :if ($lastLogId < $lastIndex) do={
        :set lastLogId $lastIndex;
        :local logData [/log get $id];
        :set ($messagesLog->"id-$lastIndex") ($logData->"message");
    }
}

:foreach id,message in=$messagesLog do={
    :local send [$telegramSendMessage $telegramBotToken $telegramChatID $message];
    
    :if ($send) do={
        :set ($messagesLog->"$id");
    }
}

File: /sources\tool-module-status.rsc
#Version: 3.0 alpha
#Fecha: 22-08-2017
#RouterOS 6.40 y superior.
#Comentario:

#TODO-BEGIN

:global gModules;

:put "";
:put "########## Module Status ##########";
:put "";

:foreach kModule,fModule in=$gModules do={
	:put ("Modulo: $kModule - " . ($fModule->"name"));
	:put ("Descripcion: " . ($fModule->"description"));
	:put ("Habilitado: " . ($fModule->"enable"));
	:put ("Cargado: " . ($fModule->"loaded"));
	:put ("Config: " . ($fModule->"config"));
	:put "";
}

#TODO-END


File: /sources\tool-script-status.rsc
#Version: 3.0 alpha
#Fecha: 22-08-2017
#RouterOS 6.40 y superior.
#Comentario:

#TODO-BEGIN

:global gScripts;
:put "";
:put "########## Script Status ##########";
:put "";
:foreach kScript,fScript in=$gScripts do={
    :put "Script: $kScript";
    :put ("Descripcion: " . ($fScript->"description"));
    :if ($fScript->"enable") do={
        :put ("Nro. veces ejecutado: " . ($fScript->"startRun"));
        :put ("Nro. veces ejecucion terminada: " . ($fScript->"endRun"));
        :put ("Intervalo de ejecucion: " . ($fScript->"interval"));
    } else={
        :put "Script deshabilitado.";
    }
    :put "";
}

#TODO-END


