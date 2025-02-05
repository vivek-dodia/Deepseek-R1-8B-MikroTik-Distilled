# Repository Information
Name: Mikrotik-Proxylizer

# Directory Structure
Directory structure:
└── github_repos/Mikrotik-Proxylizer/
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
    │   │       ├── pack-18c84d7970d4fbc326bddba021421dd8724da9c9.idx
    │   │       └── pack-18c84d7970d4fbc326bddba021421dd8724da9c9.pack
    │   ├── packed-refs
    │   └── refs/
    │       ├── heads/
    │       │   └── main
    │       ├── remotes/
    │       │   └── origin/
    │       │       └── HEAD
    │       └── tags/
    ├── install.sh
    ├── proxylizer_0.1.1b.tar.gz
    ├── proxylyzer.sql
    ├── radius.sql
    ├── README.md
    ├── syslog-ng.sh
    └── webproxylogtomysql.php


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
	url = https://github.com/jsilvestree/Mikrotik-Proxylizer.git
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
0000000000000000000000000000000000000000 5bc89622964ad36398e24dc7ce344c02bbe86ea4 vivek-dodia <vivek.dodia@icloud.com> 1738606403 -0500	clone: from https://github.com/jsilvestree/Mikrotik-Proxylizer.git


File: /.git\logs\refs\heads\main
0000000000000000000000000000000000000000 5bc89622964ad36398e24dc7ce344c02bbe86ea4 vivek-dodia <vivek.dodia@icloud.com> 1738606403 -0500	clone: from https://github.com/jsilvestree/Mikrotik-Proxylizer.git


File: /.git\logs\refs\remotes\origin\HEAD
0000000000000000000000000000000000000000 5bc89622964ad36398e24dc7ce344c02bbe86ea4 vivek-dodia <vivek.dodia@icloud.com> 1738606403 -0500	clone: from https://github.com/jsilvestree/Mikrotik-Proxylizer.git


File: /.git\packed-refs
# pack-refs with: peeled fully-peeled sorted 
5bc89622964ad36398e24dc7ce344c02bbe86ea4 refs/remotes/origin/main


File: /.git\refs\heads\main
5bc89622964ad36398e24dc7ce344c02bbe86ea4


File: /.git\refs\remotes\origin\HEAD
ref: refs/remotes/origin/main


File: /install.sh
#!/bin/bash
# Se quiser configurar a rede manualmente para acesso rapido,edite o ip e descomente, retire o (#)do começo da linhas 3,4,5,6,7,8
#ifconfig eth1 192.168.0.52/24 up
#route del default gw 192.168.0.4
#route add default gw 192.168.0.1 eth1
#echo "" >> /etc/resolv.conf
#echo "nameserver 192.168.0.13" >> /etc/resolv.conf
#/etc/init.d/networking restart

sudo apt-get update
sudo apt-get install syslog-ng libapache2-mod-php5 php5-cli php-pear php-db php-mail php-mail-mime php-net-smtp php5-mysql mysql-server mysql-client -y

echo "ServerName mikrotik" >> /etc/apache2/httpd.conf

sudo tar -xvzf  ./proxylizer_0.1.1b.tar.gz -C /var/www/
cp -rf ./webproxylogtomysql.php  /var/www/proxylizer/
chown mikrotik:www-data /var/www/proxylizer -R 
sudo chown mikrotik:www-data /var/www/proxylizer -R 
sudo chmod g+w /var/www/proxylizer -R
sudo chmod ug+x /var/www/proxylizer/checkwebproxy.sh /var/www/proxylizer/mail_send.php /var/www/proxylizer/webproxylogtomysql.php

#scp -rp mikrotik@192.168.0.53:/etc/syslog-ng/syslog-ng.conf /etc/syslog-ng/
chmod +x ./syslog-ng.sh
mv /etc/syslog-ng/syslog-ng.conf /etc/syslog-ng/syslog-ng.conf-ori
echo "" >> /etc/syslog-ng/syslog-ng.conf
./syslog-ng.sh
#sudo gedit /etc/syslog-ng/syslog-ng.conf 

mkfifo /home/mikrotik/mysql.pipe
sudo chown mikrotik:mikrotik /home/mikrotik/mysql.pipe
sudo chmod g+w /home/mikrotik/mysql.pipe
#scp -rp mikrotik@192.168.0.53:/var/www/proxylizer/webproxylogtomysql.php /var/www/proxylizer/

#gedit /var/www/proxylizer/webproxylogtomysql.php

sudo /etc/init.d/syslog-ng restart


sudo mkdir /var/log/proxylizer
sudo chown mikrotik:mikrotik /var/log/proxylizer
sudo chmod u+w /var/log/proxylizer



touch /home/mikrotik/proxylizercrontab
cat <<ATEOFIM >> /home/mikrotik/proxylizercrontab 
SHELL=/bin/sh
PATH=/usr/local/sbin:/usr/local/bin:/sbin:/bin:/usr/sbin:/usr/bin
File: /proxylyzer.sql

GRANT ALL PRIVILEGES ON proxylizerdb.* TO proxylizer@localhost IDENTIFIED BY "password" WITH GRANT OPTION;
FLUSH PRIVILEGES;


File: /radius.sql
-- phpMyAdmin SQL Dump
-- version 2.11.11.3
-- http://www.phpmyadmin.net
--
-- Servidor: localhost
-- Tempo de Geração: Abr 12, 2011 as 10:35 PM
-- Versão do Servidor: 5.0.75
-- Versão do PHP: 5.2.6-3ubuntu4.6

SET SQL_MODE="NO_AUTO_VALUE_ON_ZERO";

--
-- Banco de Dados: `radius`
--

-- --------------------------------------------------------

--
-- Estrutura da tabela `acl`
--

CREATE TABLE IF NOT EXISTS `acl` (
  `id` int(5) NOT NULL auto_increment,
  `username` varchar(16) NOT NULL default '',
  `password` varchar(16) NOT NULL default '',
  `staffname` varchar(32) NOT NULL default '',
  `string` varchar(100) default NULL,
  PRIMARY KEY  (`id`)
) ENGINE=MyISAM  DEFAULT CHARSET=latin1 AUTO_INCREMENT=4 ;

--
-- Extraindo dados da tabela `acl`
--

INSERT INTO `acl` (`id`, `username`, `password`, `staffname`, `string`) VALUES
(3, 'julio', 'thR8cQNXHkY4E', '', NULL);

-- --------------------------------------------------------

--
-- Estrutura da tabela `aut_noticias`
--

CREATE TABLE IF NOT EXISTS `aut_noticias` (
  `id` int(11) NOT NULL auto_increment,
  `titulo` varchar(255) NOT NULL default '',
  `conteudo` text NOT NULL,
  `autor_id` int(11) NOT NULL default '0',
  `data` int(11) NOT NULL default '0',
  PRIMARY KEY  (`id`)
) ENGINE=MyISAM  DEFAULT CHARSET=latin1 AUTO_INCREMENT=4 ;

--
-- Extraindo dados da tabela `aut_noticias`
--

INSERT INTO `aut_noticias` (`id`, `titulo`, `conteudo`, `autor_id`, `data`) VALUES
(1, 'Sistema de Usuários', 'bla bla bla\r\n\r\nbla bla bla', 1, 1079449401),
(2, 'Atentado em Madri', 'onono onono onono onono', 1, 1079449430),
(3, 'Kernel 2.6', 'oioioi oioioi oioioi oioioi', 2, 1079449456);

-- --------------------------------------------------------

--
-- Estrutura da tabela `aut_usuarios`
--

CREATE TABLE IF NOT EXISTS `aut_usuarios` (
  `id` int(11) NOT NULL auto_increment,
  `nome` varchar(60) NOT NULL default '',
  `login` varchar(40) NOT NULL default '',
  `senha` varchar(40) NOT NULL default '',
  `postar` enum('S','N') NOT NULL default 'S',
  PRIMARY KEY  (`id`)
) ENGINE=MyISAM  DEFAULT CHARSET=latin1 AUTO_INCREMENT=3 ;

--
-- Extraindo dados da tabela `aut_usuarios`
--

INSERT INTO `aut_usuarios` (`id`, `nome`, `login`, `senha`, `postar`) VALUES
(1, 'Albert Einstein', 'einstein', 'e7d80ffeefa212b7c5c55700e4f7193e', 'S'),
(2, 'Usuário Teste', 'admin', '698dc19d489c4e4db73e28a713eab07b', 'N');

-- --------------------------------------------------------

--
-- Estrutura da tabela `login`
--

CREATE TABLE IF NOT EXISTS `login` (
  `id` int(5) NOT NULL auto_increment,
  `usuario` text NOT NULL,
  `senha` text NOT NULL,
  `email` text NOT NULL,
  `nome` text NOT NULL,
  `titulo` text NOT NULL,
  `url` text NOT NULL,
  `time` int(15) NOT NULL,
  `ip` varchar(15) NOT NULL,
  PRIMARY KEY  (`id`),
  UNIQUE KEY `id` (`id`)
) ENGINE=MyISAM  DEFAULT CHARSET=latin1 AUTO_INCREMENT=2 ;

--
-- Extraindo dados da tabela `login`
--

INSERT INTO `login` (`id`, `usuario`, `senha`, `email`, `nome`, `titulo`, `url`, `time`, `ip`) VALUES
(1, 'user', '1234', 'email@email.com', 'user', 'sr', 'www.google.com.br', 1262697392, '127.0.0.1');

-- --------------------------------------------------------

--
-- Estrutura da tabela `nas`
--

CREATE TABLE IF NOT EXISTS `nas` (
  `id` int(10) NOT NULL auto_increment,
  `nasname` varchar(128) NOT NULL,
  `shortname` varchar(32) default NULL,
  `type` varchar(30) default 'other',
  `ports` int(5) default NULL,
  `secret` varchar(60) NOT NULL default 'secret',
  `community` varchar(50) default NULL,
  `description` varchar(200) default 'RADIUS Client',
  PRIMARY KEY  (`id`),
  KEY `nasname` (`nasname`)
) ENGINE=MyISAM  DEFAULT CHARSET=latin1 AUTO_INCREMENT=3 ;

--
-- Extraindo dados da tabela `nas`
--

INSERT INTO `nas` (`id`, `nasname`, `shortname`, `type`, `ports`, `secret`, `community`, `description`) VALUES
(1, '0.0.0.0/0', 'TesteMikrotik', 'other', NULL, 'nassecret', NULL, 'RADIUS Client Teste');

-- --------------------------------------------------------

--
-- Estrutura da tabela `radacct`
--

CREATE TABLE IF NOT EXISTS `radacct` (
  `RadAcctId` bigint(21) NOT NULL auto_increment,
  `AcctSessionId` varchar(32) NOT NULL default '',
  `AcctUniqueId` varchar(32) NOT NULL default '',
  `UserName` varchar(64) NOT NULL default '',
  `Realm` varchar(64) default '',
  `NASIPAddress` varchar(15) NOT NULL default '',
  `NASPortId` varchar(15) default NULL,
  `NASPortType` varchar(32) default NULL,
  `AcctStartTime` datetime NOT NULL default '0000-00-00 00:00:00',
  `AcctStopTime` datetime NOT NULL default '0000-00-00 00:00:00',
  `AcctSessionTime` int(12) default NULL,
  `AcctAuthentic` varchar(32) default NULL,
  `ConnectInfo_start` varchar(50) default NULL,
  `ConnectInfo_stop` varchar(50) default NULL,
  `AcctInputOctets` bigint(12) default NULL,
  `AcctOutputOctets` bigint(12) default NULL,
  `CalledStationId` varchar(50) NOT NULL default '',
  `CallingStationId` varchar(50) NOT NULL default '',
  `AcctTerminateCause` varchar(32) NOT NULL default '',
  `ServiceType` varchar(32) default NULL,
  `FramedProtocol` varchar(32) default NULL,
  `FramedIPAddress` varchar(15) NOT NULL default '',
  `AcctStartDelay` int(12) default NULL,
  `AcctStopDelay` int(12) default NULL,
  PRIMARY KEY  (`RadAcctId`),
  KEY `UserName` (`UserName`),
  KEY `FramedIPAddress` (`FramedIPAddress`),
  KEY `AcctSessionId` (`AcctSessionId`),
  KEY `AcctUniqueId` (`AcctUniqueId`),
  KEY `AcctStartTime` (`AcctStartTime`),
  KEY `AcctStopTime` (`AcctStopTime`),
  KEY `NASIPAddress` (`NASIPAddress`)
) ENGINE=MyISAM  DEFAULT CHARSET=latin1 AUTO_INCREMENT=3366 ;

--
-- Extraindo dados da tabela `radacct`
--



-- --------------------------------------------------------

--
-- Estrutura da tabela `radcheck`
--

CREATE TABLE IF NOT EXISTS `radcheck` (
  `id` int(11) unsigned NOT NULL auto_increment,
  `UserName` varchar(64) NOT NULL default '',
  `Attribute` varchar(32) NOT NULL default '',
  `op` char(2) NOT NULL default '==',
  `Value` varchar(253) NOT NULL default '',
  `NOME_USUARIO` varchar(255) NOT NULL,
  `RG` varchar(20) NOT NULL,
  `CPF` varchar(20) NOT NULL,
  `DDD` varchar(3) default NULL,
  `TELEFONE` varchar(9) default NULL,
  `ENDERECO` varchar(255) default NULL,
  `COMPLEMENTO` varchar(45) default NULL,
  `BAIRRO` varchar(45) default NULL,
  `CIDADE` varchar(45) default NULL,
  `ESTADO` varchar(2) default NULL,
  `DATA_CRIACAO` datetime default NULL,
  `DATA_ATUALIZACAO` datetime default NULL,
  `REMOTE_ADDR` varchar(15) default NULL,
  PRIMARY KEY  (`id`),
  KEY `UserName` (`UserName`(32))
) ENGINE=MyISAM  DEFAULT CHARSET=latin1 AUTO_INCREMENT=3293 ;

--
-- Extraindo dados da tabela `radcheck`
--

INSERT INTO `radcheck` (`id`, `UserName`, `Attribute`, `op`, `Value`, `NOME_USUARIO`, `RG`, `CPF`, `DDD`, `TELEFONE`, `ENDERECO`, `COMPLEMENTO`, `BAIRRO`, `CIDADE`, `ESTADO`, `DATA_CRIACAO`, `DATA_ATUALIZACAO`, `REMOTE_ADDR`) VALUES
(1, 'user', 'Password', ':=', '1234', '', '', '', NULL, NULL, NULL, '', NULL, NULL, NULL, NULL, NULL, NULL),
(3287, '', 'Password', ':=', '', '', '', '', NULL, NULL, NULL, '', NULL, NULL, NULL, NULL, NULL, NULL);

-- --------------------------------------------------------

--
-- Estrutura da tabela `radgroupcheck`
--

CREATE TABLE IF NOT EXISTS `radgroupcheck` (
  `id` int(11) unsigned NOT NULL auto_increment,
  `GroupName` varchar(64) NOT NULL default '',
  `Attribute` varchar(32) NOT NULL default '',
  `op` char(2) NOT NULL default '==',
  `Value` varchar(253) NOT NULL default '',
  PRIMARY KEY  (`id`),
  KEY `GroupName` (`GroupName`(32))
) ENGINE=MyISAM  DEFAULT CHARSET=latin1 AUTO_INCREMENT=11 ;

--
-- Extraindo dados da tabela `radgroupcheck`
--


-- --------------------------------------------------------

--
-- Estrutura da tabela `radgroupreply`
--

CREATE TABLE IF NOT EXISTS `radgroupreply` (
  `id` int(11) unsigned NOT NULL auto_increment,
  `GroupName` varchar(64) NOT NULL default '',
  `Attribute` varchar(32) NOT NULL default '',
  `op` char(2) NOT NULL default '=',
  `Value` varchar(253) NOT NULL default '',
  PRIMARY KEY  (`id`),
  KEY `GroupName` (`GroupName`(32))
) ENGINE=MyISAM  DEFAULT CHARSET=latin1 AUTO_INCREMENT=43 ;

--
-- Extraindo dados da tabela `radgroupreply`
--

INSERT INTO `radgroupreply` (`id`, `GroupName`, `Attribute`, `op`, `Value`) VALUES
(1, 'teste', 'Mikrotik-Rate-Limit', ':=', '964000/548000');

-- --------------------------------------------------------

--
-- Estrutura da tabela `radpostauth`
--

CREATE TABLE IF NOT EXISTS `radpostauth` (
  `id` int(11) NOT NULL auto_increment,
  `user` varchar(64) NOT NULL default '',
  `pass` varchar(64) NOT NULL default '',
  `reply` varchar(32) NOT NULL default '',
  `date` timestamp NOT NULL default CURRENT_TIMESTAMP on update CURRENT_TIMESTAMP,
  PRIMARY KEY  (`id`)
) ENGINE=MyISAM  DEFAULT CHARSET=latin1 AUTO_INCREMENT=4164 ;

--
-- Extraindo dados da tabela `radpostauth`
--


-- --------------------------------------------------------

--
-- Estrutura da tabela `radreply`
--

CREATE TABLE IF NOT EXISTS `radreply` (
  `id` int(11) unsigned NOT NULL auto_increment,
  `UserName` varchar(64) NOT NULL default '',
  `Attribute` varchar(32) NOT NULL default '',
  `op` char(2) NOT NULL default '=',
  `Value` varchar(253) NOT NULL default '',
  PRIMARY KEY  (`id`),
  KEY `UserName` (`UserName`(32))
) ENGINE=MyISAM  DEFAULT CHARSET=latin1 AUTO_INCREMENT=254 ;

--
-- Extraindo dados da tabela `radreply`
--

INSERT INTO `radreply` (`id`, `UserName`, `Attribute`, `op`, `Value`) VALUES
(1, 'user', 'Auth-Type', '=', 'PAP');

-- --------------------------------------------------------

--
-- Estrutura da tabela `radusergroup`
--

CREATE TABLE IF NOT EXISTS `radusergroup` (
  `UserName` varchar(64) NOT NULL default '',
  `GroupName` varchar(64) NOT NULL default '',
  `priority` int(11) NOT NULL default '1',
  KEY `UserName` (`UserName`(32))
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

--
-- Extraindo dados da tabela `radusergroup`
--

INSERT INTO `radusergroup` (`UserName`, `GroupName`, `priority`) VALUES
('user', 'teste', 1);



File: /README.md
# Mikrotik Proxylizer
### :blue_book: Documentação

### A documentação é encontrada em [Mikrotik-Proxylizer](https://github.com/jsilvestree/Mikrotik-Proxylizer/blob/6f9573052cc7a95628598dbff7940aa5f71dc43e/instalar-proxylizer.pdf) and [Mais Infomações](https://github.com/jsilvestree/Mikrotik-Proxylizer).
###### Este link leva para uma páguina antiga que pode ou não estar funcionando!
        https://wiki.mikrotik.com/wiki/Proxylizer

                                                                           
*    MikroTik Proxylizer, Web-proxy log analyzer                           
*    Copyright (C) 2009  MikroTik                                          
*                                                                          
*    This program is free software: you can redistribute it and/or modify  
*    it under the terms of the GNU General Public License as published by  
*    the Free Software Foundation, either version 3 of the License, or     
*    (at your option) any later version.                                    
*                                                                           
*    This program is distributed in the hope that it will be useful,        
*    but WITHOUT ANY WARRANTY; without even the implied warranty of         
*    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the          
*    GNU General Public License for more details.                           
*                                                                           
*    You should have received a copy of the GNU General Public License      
*    along with this program.  If not, see <http://www.gnu.org/licenses/>.  
### :penguin: Compatibility

Mikrotik-Proxylizer will run on popular distros as long as the minimum requirements are met.

* Ubuntu
* Debian
* CentOS é preciso modificar varios comandos                                                                            

#### Este projeto foi descontinuado pela Mikrotik e os arquivos originais não estão mais disponiveis,  coloquei no github para interessados estudarem os codigos 
Não existe garantias, use por sua conta e risco.

###### Note: MikroTik has discontinued the Proxylizer project, it will no longer receive updates, and technical support will not be available



O script install.sh são alguns passos do guia de instalação, você pode usar o script ou executar comando por comando.
se executar o install.sh ele instalará no Ubuntu varios pacotes e suas dependencias.

O script espera um usuario do linux chamado mikrotik, se o nome do seu usuario é outro edite o script antes de executalo.

Alguns pacotes Que irá instalar
syslog-ng 
libapache2-mod-php5
php5-cli 
php-pear
php-db 
php-mail 
php-mail-mime 
php-net-smtp
php5-mysql 
mysql-server
mysql-client

Esta instalação foi usado o Ubuntu com nome de usuário mikrotik.

###### Para mais informações leia o documento instalar-proxylizer.pdf no repositório Mikrotik-Proxylizer.
* :computer: Console

``` sudo apt-get update```

``` sudo apt-get install syslog-ng libapache2-mod-php5 php5-cli php-pear php-db php-mail php-mail-mime php-net-smtp php5-mysql mysql-server mysql-client -y ```

``` echo "ServerName mikrotik" >> /etc/apache2/httpd.conf ```

``` sudo tar -xvzf  ./proxylizer_0.1.1b.tar.gz -C /var/www/```

```cp -rf ./webproxylogtomysql.php  /var/www/proxylizer/```

```chown mikrotik:www-data /var/www/proxylizer -R ```

```sudo chown mikrotik:www-data /var/www/proxylizer -R ```

```sudo chmod g+w /var/www/proxylizer -R```

```sudo chmod ug+x /var/www/proxylizer/checkwebproxy.sh /var/www/proxylizer/mail_send.php /var/www/proxylizer/webproxylogtomysql.php```

```#scp -rp mikrotik@192.168.0.53:/etc/syslog-ng/syslog-ng.conf /etc/syslog-ng/```

```chmod +x ./syslog-ng.sh```

```mv /etc/syslog-ng/syslog-ng.conf /etc/syslog-ng/syslog-ng.conf-ori```

```echo "" >> /etc/syslog-ng/syslog-ng.conf```

```./syslog-ng.sh```

```#sudo gedit /etc/syslog-ng/syslog-ng.conf ```

```mkfifo /home/mikrotik/mysql.pipe```

```sudo chown mikrotik:mikrotik /home/mikrotik/mysql.pipe```

```sudo chmod g+w /home/mikrotik/mysql.pipe```

```#scp -rp mikrotik@192.168.0.53:/var/www/proxylizer/webproxylogtomysql.php /var/www/proxylizer/```


```#gedit /var/www/proxylizer/webproxylogtomysql.php```

```sudo /etc/init.d/syslog-ng restart```


```sudo mkdir /var/log/proxylizer```

```sudo chown mikrotik:mikrotik /var/log/proxylizer```

```bash 
sudo chmod u+w /var/log/proxylizer
```




```bash
touch /home/mikrotik/proxylizercrontab

cat <<ATEOFIM >> /home/mikrotik/proxylizercrontab 

SHELL=/bin/sh

PATH=/usr/local/sbin:/usr/local/bin:/sbin:/bin:/usr/sbin:/usr/bin

File: /syslog-ng.sh
#!/bin/bash
cat <<ATEOFIM >> /etc/syslog-ng/syslog-ng.conf
#
# Configuration file for syslog-ng under Debian
#
# attempts at reproducing default syslog behavior

# the standard syslog levels are (in descending order of priority):
# emerg alert crit err warning notice info debug
# the aliases "error", "panic", and "warn" are deprecated
# the "none" priority found in the original syslogd configuration is
# only used in internal messages created by syslogd


######
# options

options {
        # disable the chained hostname format in logs
        # (default is enabled)
        chain_hostnames(0);

        # the time to wait before a died connection is re-established
        # (default is 60)
        time_reopen(10);

        # the time to wait before an idle destination file is closed
        # (default is 60)
        time_reap(360);

        # the number of lines buffered before written to file
        # you might want to increase this if your disk isn't catching with
        # all the log messages you get or if you want less disk activity
        # (say on a laptop)
        # (default is 0)
        #sync(0);

        # the number of lines fitting in the output queue
        log_fifo_size(2048);

        # enable or disable directory creation for destination files
        create_dirs(yes);

        # default owner, group, and permissions for log files
        # (defaults are 0, 0, 0600)
        #owner(root);
        group(adm);
        perm(0640);

        # default owner, group, and permissions for created directories
        # (defaults are 0, 0, 0700)
        #dir_owner(root);
        #dir_group(root);
        dir_perm(0755);

        # enable or disable DNS usage
        # syslog-ng blocks on DNS queries, so enabling DNS may lead to
        # a Denial of Service attack
        # (default is yes)
        use_dns(no);

        # maximum length of message in bytes
        # this is only limited by the program listening on the /dev/log Unix
        # socket, glibc can handle arbitrary length log messages, but -- for
        # example -- syslogd accepts only 1024 bytes
        # (default is 2048)
        #log_msg_size(2048);

	#Disable statistic log messages.
	stats_freq(0);

	# Some program send log messages through a private implementation.
	# and sometimes that implementation is bad. If this happen syslog-ng
	# may recognise the program name as hostname. Whit this option
	# we tell the syslog-ng that if a hostname match this regexp than that
	# is not a real hostname.
	bad_hostname("^gconfd$");
};


######
# sources

# all known message sources
source s_all {
        # message generated by Syslog-NG
        internal();
        # standard Linux log source (this is the default place for the syslog()
        # function to send logs to)
        unix-stream("/dev/log");
        # messages from the kernel
        file("/proc/kmsg" log_prefix("kernel: "));
        # use the following line if you want to receive remote UDP logging messages
        # (this is equivalent to the "-r" syslogd flag)
        # udp();
};


######
# destinations

# some standard log files
destination df_auth { file("/var/log/auth.log"); };
destination df_syslog { file("/var/log/syslog"); };
destination df_cron { file("/var/log/cron.log"); };
destination df_daemon { file("/var/log/daemon.log"); };
destination df_kern { file("/var/log/kern.log"); };
destination df_lpr { file("/var/log/lpr.log"); };
destination df_mail { file("/var/log/mail.log"); };
destination df_user { file("/var/log/user.log"); };
destination df_uucp { file("/var/log/uucp.log"); };
destination d_mysql {
pipe("/home/mikrotik/mysql.pipe"
template("$HOST $YEAR-$MONTH-$DAY $HOUR:$MIN:$SEC $MSG\n") template-escape(yes));
};
log { source(net); destination(d_mysql); };


# these files are meant for the mail system log files
# and provide re-usable destinations for {mail,cron,...}.info,
# {mail,cron,...}.notice, etc.
destination df_facility_dot_info { file("/var/log/$FACILITY.info"); };
destination df_facility_dot_notice { file("/var/log/$FACILITY.notice"); };
destination df_facility_dot_warn { file("/var/log/$FACILITY.warn"); };
destination df_facility_dot_err { file("/var/log/$FACILITY.err"); };
destination df_facility_dot_crit { file("/var/log/$FACILITY.crit"); };

# these files are meant for the news system, and are kept separated
# because they should be owned by "news" instead of "root"
destination df_news_dot_notice { file("/var/log/news/news.notice" owner("news")); };
destination df_news_dot_err { file("/var/log/news/news.err" owner("news")); };
destination df_news_dot_crit { file("/var/log/news/news.crit" owner("news")); };

# some more classical and useful files found in standard syslog configurations
destination df_debug { file("/var/log/debug"); };
destination df_messages { file("/var/log/messages"); };

# pipes
# a console to view log messages under X
destination dp_xconsole { pipe("/dev/xconsole"); };

# consoles
# this will send messages to everyone logged in
destination du_all { usertty("*"); };


######
# filters

# all messages from the auth and authpriv facilities
filter f_auth { facility(auth, authpriv); };

# all messages except from the auth and authpriv facilities
filter f_syslog { not facility(auth, authpriv); };

# respectively: messages from the cron, daemon, kern, lpr, mail, news, user,
# and uucp facilities
filter f_cron { facility(cron); };
filter f_daemon { facility(daemon); };
filter f_kern { facility(kern); };
filter f_lpr { facility(lpr); };
filter f_mail { facility(mail); };
filter f_news { facility(news); };
filter f_user { facility(user); };
filter f_uucp { facility(uucp); };

# some filters to select messages of priority greater or equal to info, warn,
# and err
# (equivalents of syslogd's *.info, *.warn, and *.err)
filter f_at_least_info { level(info..emerg); };
filter f_at_least_notice { level(notice..emerg); };
filter f_at_least_warn { level(warn..emerg); };
filter f_at_least_err { level(err..emerg); };
filter f_at_least_crit { level(crit..emerg); };

# all messages of priority debug not coming from the auth, authpriv, news, and
# mail facilities
filter f_debug { level(debug) and not facility(auth, authpriv, news, mail); };

# all messages of info, notice, or warn priority not coming form the auth,
# authpriv, cron, daemon, mail, and news facilities
filter f_messages {
        level(info,notice,warn)
            and not facility(auth,authpriv,cron,daemon,mail,news);
};

# messages with priority emerg
filter f_emerg { level(emerg); };

# complex filter for messages usually sent to the xconsole
filter f_xconsole {
    facility(daemon,mail)
        or level(debug,info,notice,warn)
        or (facility(news)
                and level(crit,err,notice));
};


######
# logs
# order matters if you use "flags(final);" to mark the end of processing in a
# "log" statement

# these rules provide the same behavior as the commented original syslogd rules

File: /webproxylogtomysql.php
#!/usr/bin/php
<?php
/****************************************************************************
*                                                                           *
*    MikroTik Proxylizer, Web-proxy log analyzer                            *
*    Copyright (C) 2009  MikroTik                                           *
*                                                                           *
*    This program is free software: you can redistribute it and/or modify   *
*    it under the terms of the GNU General Public License as published by   *
*    the Free Software Foundation, either version 3 of the License, or      *
*    (at your option) any later version.                                    *
*                                                                           *
*    This program is distributed in the hope that it will be useful,        *
*    but WITHOUT ANY WARRANTY; without even the implied warranty of         *
*    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the          *
*    GNU General Public License for more details.                           *
*                                                                           *
*    You should have received a copy of the GNU General Public License      *
*    along with this program.  If not, see <http://www.gnu.org/licenses/>.  *
*                                                                           *
****************************************************************************/
if (isset($_SERVER['REQUEST_URI'])) return;
define("STARTED_FROM_INDEX", 2);
chdir(dirname($argv[0]));
if(!include("config_constants.php")) {
    echo date("Y-m-d H:i | ") . "No configuration written!\n";
} else {
    include('DB.php');
    while( true ) {
            $pid = pcntl_fork();
            if ($pid == -1) {
            die('could not fork');
        } else if ($pid) {
            pcntl_waitpid($pid, $status); //Protect against Zombie children
            sleep(1);
            continue;
        } else {
            set_time_limit(0);
            ob_implicit_flush();
            define("DEBUG", 0);
            define("IP_DIGIT", "(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)");
            define("IP_REGEXP", "^" . IP_DIGIT . "\\." . IP_DIGIT . "\\." . IP_DIGIT . "\\." . IP_DIGIT . "$");
            $MYSQL_PIPE = "/home/mikrotik/mysql.pipe";
            // tell PEAR to write no backtrace
            $skiptrace = &PEAR::getStaticProperty('PEAR_Error', 'skiptrace');
            $skiptrace = true;
            
            /////////////////////////////////////
            
            //print_r($_SERVER);
            while (true) {
                $file = @fopen($MYSQL_PIPE, "r");
                if ($file == false) {
                echo date("Y-m-d H:i | ") . "Error : Can't open file {$MYSQL_PIPE}\n";
                sleep(1);
                continue;
                }
                if ($db = connectDB()) {
                    while ($line = fgets($file)) {
    		    $line = str_replace("\n", "", $line);
                        //echo "{$line}\n";
                        $rawlog = explode(" ", $line);
                        //interesting for me;
                        // $rawlog['0'] = Host;
                        //$rawlog['1'] = Date;
                        //$rawlog['2'] = Time;
                        //$rawlog['4'] = IP;
                        //$rawlog['6'] = URL;
                        //$rawlog['7'] = action;
                        //$rawlog['8'] = cache;
                        $date = $rawlog['1'];
                        $time = $rawlog['2'];
                        //$datetime = $date . " " . $time;
                        $date = strtotime($date);
                        $date = date("Y-m-d",$date);
                        $time = strtotime($time);
                        $time = date("H:i",$time);
                        if ($rawlog['3'] == 'web-proxy,account') {
                            $host = ip2long($rawlog['0']);
                            list(, $host) = unpack('l', pack('l', $host));
                            if ($host === false) echo date("Y-m-d H:i | ") .  "Invalid Host IP address";
                            $IP = eregIP($rawlog['4']);
                            if ($IP !== false) {
                                $IP = ip2long($rawlog['4']);
                                if ($IP !== false) {
                                    list(, $IP) = unpack('l', pack('l', $IP));
                                    parseURL($rawlog['6']);
                                    parseDomain($fulldomain);
                                    parseAction($rawlog['7']);
                                    parseCache($line);
                                    //echo "Action = {$action}\n";
                                    //echo "Cache = {$cache}\n";
                                    if(insertLine($db));
                                } else {
                                    echo date("Y-m-d H:i | ") . "Invalid IP address!!!\n";
                                }
                            } else {
                                echo date("Y-m-d H:i | ") . "Invalid IP address!!!\n";
                            }
                        } else {
                            echo date("Y-m-d H:i | ") . "Not valid web proxy log!!!\n";
                        }
                    }
                $db->disconnect();
                }
                fclose($file);
            }
        }
    }
}
function eregIP ($ip) {
    if (ereg(IP_REGEXP, $ip)) {
        return $ip;
    } else {
        return false;
    }
}

function connectDB() {
global $config_const;
    $DBpaswrd = $config_const['DB_PASSWORD'];
    if ($DBpaswrd != "") $DBpaswrd = ":" . $DBpaswrd;
    $dsn = "{$config_const['DB_TYPE']}://{$config_const['DB_USERNAME']}{$DBpaswrd}@{$config_const['DB_HOST']}/{$config_const['DB_NAME']}"; 
    $options = array(
    'debug'       => 2,
    'portability' => DB_PORTABILITY_ALL,
    );
    do {
        $db = & DB::connect($dsn, $options);
        if (PEAR::isError($db)) {
            echo "/1/ ";
            echo date("Y-m-d H:i | ") . "Code " . $errcode=$db->getcode() . " ";
            echo $db->getMessage() . "\n";
            if ($errcode == DB_ERROR_ACCESS_VIOLATION || $errcode == DB_ERROR_NOSUCHDB) {
                return false;
            }
            return false;
        } else {
            return $db;
        }
    } while (true);
}


function insertLine (& $db) {
global $subdomain, $domain, $topdomain, $domainid , $cofig_const ;
    $query = "INSERT INTO domain(subdomain, domain, topdomain)
                    VALUES ('{$subdomain}', '{$domain}', '{$topdomain}')";
        do {
            $insertdata = & $db->query($query);
            $iserror = false;
            if (PEAR::isError($insertdata)) {
                $msg = $insertdata->getMessage() . "\n";
                $errcode = $insertdata->getCode();
                if ($errcode = DB_ERROR_CONSTRAINT || $errcode = DB_ERROR_ALREADY_EXISTS) {
                    $testquery = "SELECT ID from domain WHERE subdomain = '{$subdomain}'
                                and domain = '{$domain}' and topdomain = '{$topdomain}'";
                    // domain exists
                    $res =& $db->query($testquery);
                    if (PEAR::isError($res)) {
                        $errorcode = $res->getCode();
                        if ($errorcode == DB_ERROR_ACCESS_VIOLATION || $errcode == DB_ERROR_NOSUCHDB || 
                            $errcode == DB_ERROR_NODBSELECTED || $errcode == DB_ERROR || 
                            $errcode == DB_ERROR_NODBSELECTED) {
                            // domain exists but connection lost
                            echo "/2/ ";
                            echo date("Y-m-d H:i | ") . "CODE: " . $res->getCode() . " ";
                            echo $res->getMessage() . " \n";
                            $iserror = true;
                            $db->disconnect();
                            $db = connectDB();
                        } else {
                            $iserror = false;
                        }
                    } else {
                        // domain exists, id selected
                        $row =& $res->fetchRow();
                        $domainid = $row['0'];
                        insertWebproxyTable($db);
                        $iserror = false;
                    }
                } elseif ($errcode == DB_ERROR_ACCESS_VIOLATION || $errcode == DB_ERROR_NOSUCHDB || 
                            $errcode == DB_ERROR_NODBSELECTED || $errcode == DB_ERROR ||
                            $errcode == DB_ERROR_NODBSELECTED) {
                    // no connection, etc
                    echo "/3/ ";
                    echo date("Y-m-d H:i | ") . "CODE: " . $res->getCode() . " ";
                    echo $res->getMessage() . " \n";
                    $iserror = false;
                    $db->disconnect();
                    $db = connectDB();
                } else {
                    echo "/4/ ";
                    echo date("Y-m-d H:i | ") . $insertdata->getMessage() . "\n";
                }
            } else {
                // domain inserted
                $querymaxid = "SELECT max(ID) FROM domain";
                $res =& $db->query($querymaxid);
                if (PEAR::isError($res)) {
                    echo "/5/ ";
                    echo date("Y-m-d H:i | ") . "CODE: " . $res->getCode() . " ";
                    echo $res->getMessage() . "\n";
                } else {
                    $row =& $res->fetchRow();
                    $domainid = $row['0'];
                    insertWebproxyTable($db);
                    $iserror = false;
                }
            }
        } while ($iserror ==true);
    }

function insertWebproxyTable (& $db) {
global $domainid, $host, $date, $time, $IP, $domainid, $path, $action, $cache, $iserror, $line;
    $query = "INSERT INTO webproxylog (host, event_date, event_time, IP, domain_id, path, action, cache)"
    . " VALUES ('{$host}', '{$date}', '{$time}', "
    . "'{$IP}', '{$domainid}', '{$path}', '{$action}', '{$cache}')";
    $insertdata = & $db->query($query);
    if (PEAR::isError($insertdata)) {
        echo "/6/ ";
        echo date("Y-m-d H:i | ") . $insertdata->getMessage() . "\n";
        $iserror = false;
    } else if (DEBUG) {
        $query = "SELECT MAX(id) FROM webproxylog";
        $res = & $db->query($query);
        if (!PEAR::isError($res)) {
            $row = $res->fetchRow();
            if ($row) {
                $logID = $row[0];
                $msg = str_replace("'", "''", $line);
                $query = "INSERT INTO msg (logid, msg) VALUES ({$logID}, '{$msg}')";
                $res = & $db->query($query);
            }
        }
    }
}

function parseDomain($d) {
global $subdomain, $domain, $topdomain;
    $is_ipv4 = ip2long($d);
    if ($is_ipv4 !== false) {
        $subdomain = "";
        $domain = $d;
        $topdomain = "";
    } else {
        $posoflastdot = strrpos($d, '.');
        if ($posoflastdot === false) {
            $subdomain = "";
            $domain = $d;
            $topdomain = "";
        } else {
            $topdomain = substr($d, $posoflastdot + 1);
            $rawdomain = substr($d, 0, $posoflastdot);
            $posofprelastdot = strrpos($rawdomain, '.');
            if ($posofprelastdot !== false) {
                $domain = substr($rawdomain, $posofprelastdot + 1);
                $subdomain = substr($rawdomain, 0, $posofprelastdot);
            } else {
                $domain = $rawdomain;
                $subdomain = "";
            }
        }
    }
}

function parseURL($u) {
global $fulldomain, $path;
    $posofquestion = strpos($u, '?');
    if ($posofquestion != false) {
        $u = substr($u, 0, $posofquestion);
    }
    $posofcolonslash = strpos($u, '://');
    $address = substr($u, $posofcolonslash + 3);
    $posofslash = strpos($address, '/');
    if ($posofslash != false) {
        $fulldomain = substr($address, 0, $posofslash);
        $path = substr($address, $posofslash + 1);
    } else {
        $fulldomain = $address;
        $path = "";
    }
}

function parseAction($a) {
global $action;
    $action = $a == 'action=allow' ? 1 : 0;
}

function parseCache($l) {
global $cache;
    $c = substr($l, -9);
    $cache = $c == 'cache=HIT' ? 1 : 0;
}?>


