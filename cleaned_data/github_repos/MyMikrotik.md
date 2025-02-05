# Repository Information
Name: MyMikrotik

# Directory Structure
Directory structure:
└── github_repos/MyMikrotik/
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
    │   │       ├── pack-dfe2e3ad87cd30a2ba3af513193b40dc93273126.idx
    │   │       └── pack-dfe2e3ad87cd30a2ba3af513193b40dc93273126.pack
    │   ├── packed-refs
    │   └── refs/
    │       ├── heads/
    │       │   └── main
    │       ├── remotes/
    │       │   └── origin/
    │       │       └── HEAD
    │       └── tags/
    └── Mikrotik Firewall example (not complet)


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
	url = https://github.com/b-fluid/MyMikrotik.git
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
0000000000000000000000000000000000000000 e47726127607f663e78e2670936181e2e205e169 vivek-dodia <vivek.dodia@icloud.com> 1738606405 -0500	clone: from https://github.com/b-fluid/MyMikrotik.git


File: /.git\logs\refs\heads\main
0000000000000000000000000000000000000000 e47726127607f663e78e2670936181e2e205e169 vivek-dodia <vivek.dodia@icloud.com> 1738606405 -0500	clone: from https://github.com/b-fluid/MyMikrotik.git


File: /.git\logs\refs\remotes\origin\HEAD
0000000000000000000000000000000000000000 e47726127607f663e78e2670936181e2e205e169 vivek-dodia <vivek.dodia@icloud.com> 1738606405 -0500	clone: from https://github.com/b-fluid/MyMikrotik.git


File: /.git\packed-refs
# pack-refs with: peeled fully-peeled sorted 
e47726127607f663e78e2670936181e2e205e169 refs/remotes/origin/main


File: /.git\refs\heads\main
e47726127607f663e78e2670936181e2e205e169


File: /.git\refs\remotes\origin\HEAD
ref: refs/remotes/origin/main


File: /Mikrotik Firewall example (not complet)
 Voici une ancienne version de mon script de pare-feu que je rends public.
#
# Ceci est compilé à partir d'une expérience wiki / forum / personnelle.
#
# Il bloque le trafic entrant frauduleux, inclut certaines règles de portknock, le blocage du courrier indésirable SMTP, certaines limitations de débit ICMP,
# bloque certaines analyses de ports et les attaques DOS.
#
# Dans le script ci-dessous, remplacez X.X.X.X, Y.Y.Y.Y et Z.Z.Z.Z par vos propres valeurs. Le port frappé à la ligne 34 commence à la ligne 42.
# Si vous souhaitez la désactiver, ce sont vos lignes à ajuster. Vous voudrez probablement ajuster le port et les protocoles sur le port si vous choisissez de l'utiliser
#
#
# De plus ci-dessous, nous avons la liste des Bogons.
# Mais tout d’abord Kezako que le Bogons ??? 
# Un Bogon est une adresse IP bidon à partir de l’espace Bogon, qui est un ensemble d’adresses IP qui n’est pas encore officiellement attribuée à une entité par l’Internet
# Assigned numéro Authority (IANA) ou un Institut régional d’enregistrement Internet.
# Les adresses IP de Bogon sont des adresses légitimes. Vous pouvez voir une adresse IP Bogon à la suite d’une mauvaise configuration (intentionnelle ou involontaire) qui
# imbéciles un destinataire sur l’adresse IP légitime d’un expéditeur. Les adresses IP de Bogon sont populaires dans le piratage ou les activités malveillantes et sont
# utilisées par les spammeurs et ceux qui lancent des attaques par déni de service distribué. En tant que tel, de nombreux fournisseurs de services Internet et pare-feu bloquent bogons.
# Un Bogon est également connu comme un espace Bogon ou une adresse IP Bogon.
# Les adresses IP constituent le composant central de toute l'infrastructure Internet et intranet à travers le monde. Ils permettent d'identifier de manière unique un site Web,
# un serveur ou tout autre appareil ou appareil connecté. Ces adresses sont utilisées pour établir la communication entre les clients et les applications.
# L'IANA attribue des adresses IP uniques à chaque instance et nœud résidant sur ce réseau hétérogène. La plage d'adresses IP allouées ou enregistrées à une entité quelconque
# fait partie de l'espace réservé aux adresses IP. D'autre part, toute autre adresse qui fait partie de l'espace d'adressage mais n'est pas encore enregistrée provient de cet espace.
# Toute adresse dans l'espace bogon est appelée bogon ou adresse IP bogon.
# Les adresses IP des espaces Bogon ne sont normalement pas visibles sur Internet ou sur un réseau informatique, mais elles sont toujours exploitées, principalement pour des activités
# illégales ou frauduleuses. Les pirates informatiques manipulent l'adresse IP source sur une adresse IP erronée, donnant ainsi au destinataire l'impression que le paquet provient d'une source fiable.
# Donc interdire clairement toutes les plages d’adresses dont on ne se sert pas. Et n’autoriser les IP LAN, WAN et VLAN dont notre réseau a besoin. Ne pas oublier le Vlan car on peut galérer un moment.
# Donc:
#
/ip firewall address-list
#rfc 1918, loopback, and multicast
add address=10.0.0.0/8 comment=" ### Private[RFC 1918] - CLASS A - loopback, and multicast # Vérifiez si vous avez besoin de ce sous-réseau avant de l’activer ou le desactiver ### " disabled=no list=bogons
add address=127.0.0.1 comment=" ### Loopback [RFC 3330] ### " disabled=no list=bogons
add address=169.254.0.0/16 comment=" ### Link Local [RFC 3330] ### " disabled=no list=bogons
add address=192.168.0.0/16 comment=" ### Private[RFC 1918] - CLASS C # Vérifiez si vous avez besoin de ce sous-réseau avant de l’activer ou le desactiver ###" disabled=no list=bogons
add address=172.16.0.0/20 comment="" disabled=no list=bogons
add address=10.0.0.0/8 comment="" disabled=no list=bogons
add address=172.16.0.0/12 comment=" ### Private[RFC 1918] - CLASS B # Vérifiez si vous avez besoin de ce sous-réseau avant de l’activer ou le desactiver ### " disabled=no list=bogons
add address=192.0.2.0/24 comment=" ### Reserved - IANA - TestNet1 ### " disabled=no  list=bogons
add address=192.88.99.0/24 comment=" ### 6to4 Relay Anycast [RFC 3068] ### " disabled=no  list=bogons
add address=198.18.0.0/15 comment=" ### NIDB Testing ### " disabled=no  list=bogons
add address=198.51.100.0/24 comment=" ### Reserved - IANA - TestNet2 ### " disabled=no  list=bogons
add address=203.0.113.0/24 comment=" ### Reserved - IANA - TestNet3 ### " disabled=no  list=bogons
add address=224.0.0.0/4 comment=" ### MC, Class D, IANA # Vérifiez si vous avez besoin de ce sous-réseau avant de l’activer ou le désactiver ### " disabled=yes  list=bogons
add address=240.0.0.0/4 comment="" disabled=no list=bogons
 
# my public addressing
add address=217.70.184.38 comment="Domain directional-driller.com heberge chez Gandi.net" disabled=no list=public-add
add address=217.70.184.38 comment="Domain francoisthirion.com heberge chez Gandi.net" disabled=no list=public-add
add address=217.70.184.38 comment="Domain quad9.fr heberge chez Gandi.net" disabled=no list=public-add
add address=217.70.184.38 comment="Domain directional-driller.com heberge chez Gandi.net" disabled=no list=public-add
 
#my private addressing
#  add address=S.S.S.S/SS comment="" disabled=no list=internal-nets
add address=10.0.0.0/8 disabled=no list=internal-nets
add address=192.168.0.0/16 disabled=no list=internal-nets
add address=172.25.25.0/24 disabled=no list=internal-nets

#any port knock exclusions
add address=Y.Y.Y.Y comment="" disabled=no list=port-knock-3
 
#any SMTP exclusions
add address=Z.Z.Z.Z comment="" disabled=no list=smtp-bypass
#
/ip firewall nat
add action=masquerade chain=srcnat out-interface=ether1
# 
/ip firewall filter
# Match more than 5 pings in 5 seconds.  Then drop the traffic inbound and forward.
#
add action=accept chain=input comment="start of greg rules up to 5 pings in 5 seconds" disabled=no limit=5,5 protocol=icmp
add action=add-src-to-address-list address-list=icmp-attack address-list-timeout=12h chain=input comment="add all other icmp input into icmp-attack address list." disabled=no protocol=icmp
add action=drop chain=input comment=" ### drop excessive icmp traffic for 12 hours / Refuser tout traffic excessif en ICMP pour 12 hrs. ### " disabled=no src-address-list=icmp-attack protocol=icmp
add action=drop chain=forward comment=" ### drop excessive icmp traffic for 12 hours / Refuser tout traffic excessif en ICMP pour 12 hrs. ### " disabled=yes src-address-list=icmp-attack protocol=icmp
#
#drop 1918 inbound (bogons)
#
add action=drop chain=forward comment="block rfc 1918 and multicast inbound" disabled=no in-interface=ether1 src-address-list=bogons
add action=drop chain=forward comment="block our addressing inbound - spoofed" disabled=no in-interface=ether1 src-address-list=public-add
add action=drop chain=input comment="block rfc 1918 and multicast inbound" disabled=no in-interface=ether1 src-address-list=bogons
add action=drop chain=input comment="block our addressing inbound - spoofed" disabled=no in-interface=ether1 src-address-list=public-add
#
# Basic configuration
#
add action=drop chain=input comment=" ### Drop DNS requests from public / Refuse les requetes DNS provenant du reseau public protocole TCP ### " connection-state=new dst-port=53 in-interface=ether1 protocol=tcp
add action=drop chain=input comment=" ### Drop DNS requests from public / Refuse les requetes DNS provenant du reseau public protocole UDP ### " connection-state=new dst-port=53 in-interface=ether1 protocol=udp

add action=drop chain=input comment=" ### Drop DNS requests from public / Refuse les requetes DNS provenant du reseau public protocole TCP ### " connection-state=new dst-port=53 in-interface=wlan1 protocol=tcp
add action=drop chain=input comment=" ### Drop DNS requests from public / Refuse les requetes DNS provenant du reseau public protocole UDP ### " connection-state=new dst-port=53 in-interface=wlan1 protocol=udp

add action=drop chain=input comment=" ### Disallow weird packets / Interdire les paquets bizarres ### " connection-state=invalid
add action=accept chain=input comment=" ### Allow LAN access to router and Internet / Autoriser l’accès à la LAN au routeur et à Internet ### " connection-state=new in-interface=bridge1-LAN
add action=fasttrack-connection chain=forward comment="FastTrack Established and Related" connection-state=established,related
add action=accept chain=input comment="Allow connections that originated from LAN" connection-state=established
add action=accept chain=input comment="Allow connections that originated from LAN" connection-state=related
add action=accept chain=input comment="Allow ping ICMP from anywhere" protocol=icmp
add action=accept chain=input comment=" ### Allow WAN access to router / permettre les acces WAN vers le router ### " dst-port=8291 protocol=tcp
add action=drop chain=input comment="Disallow anything from anywhere on any interface"
add action=drop chain=forward comment="Disallow weird packets" connection-state=invalid
#
#
#start port knocking
#
# Le port « knock » lui-même est similaire à une poignée de main secrète et peut considt de n’importe quel nombre de TCP, UDP, ou ICMP ou d’autres paquets de protocole à des ports numérotés
# sur la machine de destination.
# Le KNock peut également consister en des chaînes de texte envoyées à l’appareil en cours de frappe pour ajouter une complexité et une sécurité supplémentaires.
# Exemple de frappe de port :
# L'hote  envoie une connexion à l’un des ports du routeur, le routeur stocke l’ADRESSE IP du demandeur pendant un certain temps.
# Si l’hôte envoie à nouveau une connexion dans les autres ports, le routeur vérifie si l’IP est la même IP à partir de la première connexion.
# Si l’IP est la même et que le temps entre le premier attemp et le second est dans un délai spécifié, l’IP du demandeur sera autorisé à accéder au routeur.
# et ca s ecrit ainsi

add action=add-src-to-address-list address-list=ICMP address-list-timeout=1m chain=input disabled=no protocol=icmp
add action=add-src-to-address-list address-list="ICMP + Http" address-list-timeout=1m chain=input disabled=no dst-port=80 protocol=tcp src-address-list=ICMP
add  action=drop chain=input disabled=no dst-port=22,23,8291 protocol=tcp src-address-list="!ICMP + Http"
#
add action=add-src-to-address-list address-list=port-knock-1 address-list-timeout=15s chain=input comment="port knock step 1 - udp 444" disabled=no dst-port=444 protocol=udp
add action=add-src-to-address-list address-list=port-knock-2 address-list-timeout=15s chain=input comment="port knock step 2 - udp 117" disabled=no dst-port=117 protocol=udp src-address-list=port-knock-1
add action=add-src-to-address-list address-list=port-knock-3 address-list-timeout=5h chain=input comment="port knock step 3 - tcp 600 - final" disabled=no dst-port=600 protocol=tcp src-address-list=port-knock-2
add action=accept chain=input comment="allow winbox in via port knock" disabled=no dst-port=8291 protocol=tcp src-address-list=port-knock-3
add action=drop chain=input comment="allow winbox in via port knock" disabled=no dst-port=8291 protocol=tcp
#
# port scans and DOS
#
add action=add-src-to-address-list address-list=port-scan address-list-timeout=2w chain=input comment="add port scannes to port-scan list" disabled=no in-interface=ether1 protocol=tcp psd=21,3s,3,1 src-address-list=!internal-nets
add action=add-src-to-address-list address-list=port-scan address-list-timeout=2w chain=input comment="NMAP FIN Stealth scan" disabled=no protocol=tcp tcp-flags=fin,!syn,!rst,!psh,!ack,!urg
add action=add-src-to-address-list address-list=port-scan address-list-timeout=2w chain=input comment="SYN/FIN scan" disabled=no protocol=tcp tcp-flags=fin,syn
add action=add-src-to-address-list address-list=port-scan address-list-timeout=2w chain=input comment="SYN/RST scan" disabled=no protocol=tcp tcp-flags=syn,rst
add action=add-src-to-address-list address-list=port-scan address-list-timeout=2w chain=input comment="FIN/PSH/URG scan" disabled=no protocol=tcp tcp-flags=fin,psh,urg,!syn,!rst,!ack
add action=add-src-to-address-list address-list=port-scan address-list-timeout=2w chain=input comment="ALL/ALL scan" disabled=no protocol=tcp tcp-flags=fin,syn,rst,psh,ack,urg
add action=add-src-to-address-list address-list=port-scan address-list-timeout=2w chain=input comment="NMAP NULL scan" disabled=no protocol=tcp tcp-flags=!fin,!syn,!rst,!psh,!ack,!urg
add action=tarpit chain=input comment="tarpit port-scan address list to router" disabled=no protocol=tcp src-address-list=port-scan
add action=drop chain=input comment="drop port-scan address list to our router" disabled=no src-address-list=port-scan
add action=drop chain=forward comment="drop port-scan address list to our infrastructure" disabled=no src-address-list=port-scan
add action=drop chain=forward comment="drop windows ports" disabled=no port=135-139 protocol=tcp
add action=accept chain=forward comment="allow smtp-bypass list to create multiple sessions" disabled=no dst-port=25 protocol=tcp src-address-list=smtp-bypass
add action=drop chain=forward comment="drop smtp traffic marked as spam" disabled=no dst-port=25 protocol=tcp src-address-list=spam-block
add action=add-src-to-address-list address-list=spam-block address-list-timeout=2h chain=forward comment="more than 5 smtp connections out as spam. add to address list" connection-limit=30,32 disabled=no dst-port=25 limit=50,5 protocol=tcp src-address-list=bogons
add action=accept chain=input comment=" ### Accepter les ports 80 et 8080 provenant de portknock / allow 80 and 8080 from portknock ### " disabled=no dst-port=80,8080 protocol=tcp src-address-list=port-knock-3
add action=drop chain=input comment="block 80 and 8080 from everyone else" disabled=no dst-port=80,8080 protocol=tcp
#
# Règle l7 dans la chaîne de sortie qui voit les paquets sortants et entrant.
#
add action=accept chain=input comment="" disabled=no layer7-protocol=telnet protocol=tcp
add action=passthrough chain=output comment="" disabled=no layer7-protocol=telnet protocol=tcp
#
# Firewall regles mangle
#
/ip firewall mangle
add action=mark-packet chain=prerouting comment=" ### internal-traffic packet mark / marquage de paquets du traffic internet ### " dst-address-list=internal-nets new-packet-mark=internal-traffic passthrough=no src-address-list=internal-nets
add action=mark-packet chain=prerouting comment=" ### admin-in packet mark DNS / admin-in des paquest marque DNS sur port 53 UDP ### " in-interface=ether1 new-packet-mark=admin-in passthrough=no protocol=udp src-port=53
add action=mark-packet chain=prerouting comment=" ### admin-in packet mark snmp / admin-in des paquets marques smnp sur port 161 UDP ### " dst-port=161 in-interface=ether1 new-packet-mark=admin-in passthrough=no protocol=udp
add action=mark-connection chain=prerouting comment=" ### Remote Protocols admin connection mark / Protocole de remote access admin marquage deconnection en TCP ### " new-connection-mark=admin port=20,21,22,23,3389,8291 protocol=tcp
add action=mark-connection chain=prerouting comment=" ### icmp connection mark as admin / Preroute les connections marques ICMP comme admin ### " new-connection-mark=admin protocol=icmp src-address-list=internal-nets
add action=mark-packet chain=prerouting comment=" ### admin-in packet mark / Preroute les paquests marques admin-in ### " connection-mark=admin in-interface=ether1 new-packet-mark=admin-in passthrough=no
add action=mark-packet chain=prerouting comment=" ### admin-out packet mark ### " connection-mark=admin new-packet-mark=admin-out passthrough=no
add action=mark-connection chain=prerouting comment=" ### streaming video connection mark ### " dst-port=80 layer7-protocol=video new-connection-mark=streaming-video protocol=tcp src-address-list=internal-nets
add action=mark-packet chain=prerouting comment=" ### streaming video in packet mark ### " connection-mark=streaming-video in-interface=ether1 new-packet-mark=streaming-video-in passthrough=no
add action=mark-packet chain=prerouting comment=" ### streaming video out packet mark ### " connection-mark=streaming-video new-packet-mark=streaming-video-out passthrough=no
add action=mark-connection chain=prerouting comment=" ### http traffic connection mark ### " dst-port=80,443 new-connection-mark=http protocol=tcp src-address-list=internal-nets
add action=mark-connection chain=prerouting comment=" ### http traffic connection mark ### " connection-bytes=5000000-4294967295 dst-port=80,443 new-connection-mark=http-download protocol=tcp src-address-list=internal-nets
add action=mark-packet chain=prerouting comment=" ### http in packet mark ### " connection-mark=http in-interface=ether1 new-packet-mark=http-in passthrough=no
add action=mark-packet chain=prerouting comment=" ### http out packet mark### " connection-mark=http new-packet-mark=http-out passthrough=no
#
# Regles Mangle Cocernat les jeux
#
add action=mark-connection chain=prerouting comment=" ### wow connetion mark as gaming ###" dst-port=1119,3724,6112-6114,4000,6881-6999 new-connection-mark=games protocol=tcp src-address-list=internal-nets
add action=mark-connection chain=prerouting comment=" ### eve online connetion mark as gaming ### " dst-address=87.237.38.200 new-connection-mark=games src-address-list=internal-nets
add action=mark-connection chain=prerouting comment=" ### starcraft 2 connetion mark as gaming ### " dst-port=1119 new-connection-mark=games protocol=tcp src-address-list=internal-nets
add action=mark-connection chain=prerouting comment=" ### heros of newerth connetion mark as gaming ### " dst-port=11031,11235-11335 new-connection-mark=games protocol=tcp src-address-list=internal-nets
add action=mark-connection chain=prerouting comment=" ### steam connetion mark as gaming ### " dst-port=27014-27050 new-connection-mark=games protocol=tcp src-address-list=internal-nets
add action=mark-connection chain=prerouting comment=" ###xbox live connetion mark as gaming ### " dst-port=3074 new-connection-mark=games protocol=tcp src-address-list=internal-nets
add action=mark-connection chain=prerouting comment=" ###ps3 online connetion mark as gaming ###" dst-port=5223 new-connection-mark=games protocol=tcp src-address-list=internal-nets
add action=mark-connection chain=prerouting comment=" ### wii online connetion mark as gaming ### " dst-port=28910,29900,29901,29920 new-connection-mark=games protocol=tcp src-address-list=internal-nets
add action=mark-packet chain=prerouting comment="games packet mark forever-saken-game" dst-address-list=external-nets new-packet-mark=games-in passthrough=no src-address-list=forever-saken-game
add action=mark-packet chain=prerouting comment="games packet mark wow" dst-address-list=external-nets new-packet-mark=games-in passthrough=no protocol=udp src-port=53,3724
add action=mark-packet chain=prerouting comment="games packet mark starcraft2" dst-address-list=external-nets new-packet-mark=games-in passthrough=no protocol=udp src-port=1119,6113
add action=mark-packet chain=prerouting comment="games packet mark HoN" dst-address-list=external-nets new-packet-mark=games-in passthrough=no protocol=udp src-port=11031,11235-11335
add action=mark-packet chain=prerouting comment="games packet mark steam in" dst-address-list=external-nets new-packet-mark=games-in passthrough=no port=4380,28960,27000-27030 protocol=udp
add action=mark-packet chain=prerouting comment="games packet mark steam out" dst-port=53,1500,3005,3101,3478,4379-4380,4380,28960,27000-27030,28960 new-packet-mark=games-out passthrough=no protocol=udp src-address-list=internal-nets
add action=mark-packet chain=prerouting comment="games packet mark xbox live" dst-address-list=external-nets new-packet-mark=games-in passthrough=no protocol=udp src-port=88,3074,3544,4500
add action=mark-packet chain=prerouting comment="games packet mark ps3 online" dst-address-list=external-nets new-packet-mark=games-in passthrough=no protocol=udp src-port=3478,3479,3658
add action=mark-packet chain=prerouting comment="games packet mark in" connection-mark=games dst-address-list=external-nets new-packet-mark=games-in passthrough=no
add action=mark-packet chain=prerouting comment="games packet mark out" connection-mark=games new-packet-mark=games-out passthrough=no
#
# Regles Mangle Concernant les Voice IP
#
add action=mark-packet chain=prerouting comment="voip-in packet mark teamspeak" dst-address-list= external-nets new-packet-mark=voip-in passthrough=no protocol=udp src-port=9987
add action=mark-packet chain=prerouting comment="voip-out packet mark teamspeak" dst-port=9987 new-packet-mark=voip-out passthrough=no protocol=udp src-address-list=internal-nets
add action=mark-packet chain=prerouting comment="voip-out packet mark teamspeak" dst-address-list=external-nets new-packet-mark=voip-in passthrough=no protocol=udp src-port=9987
add action=mark-packet chain=prerouting comment="voip-in packet mark ventrilo" dst-address-list=external-nets new-packet-mark=voip-in passthrough=no protocol=udp src-port=3784
add action=mark-packet chain=prerouting comment="voip-out packet mark ventrilo" dst-port=3784 new-packet-mark=voip-out passthrough=no protocol=udp src-address-list=internal-nets
add action=mark-packet chain=prerouting comment="voip-in packet mark ventrilo" dst-address-list=external-nets new-packet-mark=voip-in passthrough=no protocol=tcp src-port=3784
add action=mark-packet chain=prerouting comment="voip-out packet mark ventrilo" dst-port=3784 new-packet-mark=voip-out passthrough=no protocol=tcp src-address-list=internal-nets
add action=mark-packet chain=prerouting comment="voip-in packet mark SIP" dst-address-list=internal-nets new-packet-mark=voip-in passthrough=no port=5060 protocol=tcp
add action=mark-packet chain=prerouting comment="voip-out packet mark SIP" new-packet-mark=voip-out passthrough=no port=5060 protocol=tcp src-address-list=internal-nets
add action=mark-packet chain=prerouting comment="voip-in packet mark udp SIP" dst-address-list=internal-nets new-packet-mark=voip-in passthrough=no port=5004,5060 protocol=udp
add action=mark-packet chain=prerouting comment="voip-out packet mark udp SIP" new-packet-mark=voip-out passthrough=no port=5004,5060 protocol=udp src-address-list=internal-nets
add action=mark-packet chain=prerouting comment="voip-in packet mark RTP" dst-address-list=internal-nets new-packet-mark=voip-in packet-size=100-400 passthrough=no port=16348-32768 protocol=udp
add action=mark-packet chain=prerouting comment="voip-out packet mark RTP" new-packet-mark=voip-in packet-size=100-400 passthrough=no port=16348-32768 protocol=udp src-address-list=internal-nets
#
# Regles Mangles concernant les VPN
#

add action=mark-packet chain=prerouting comment="vpn-in packet mark GRE" in-interface=ether1 new-packet-mark=vpn-in passthrough=no protocol=gre
add action=mark-packet chain=prerouting comment="vpn-out packet mark GRE" new-packet-mark=vpn-out passthrough=no protocol=gre
add action=mark-packet chain=prerouting comment="vpn-in packet mark ESP" in-interface=ether1 new-packet-mark=vpn-in passthrough=no protocol=ipsec-esp
add action=mark-packet chain=prerouting comment="vpn-out packet mark ESP" new-packet-mark=vpn-out passthrough=no protocol=ipsec-esp
add action=mark-packet chain=prerouting comment="vpn-in packet mark VPN UDP ports" in-interface=ether1 new-packet-mark=vpn-in passthrough=no protocol=udp src-port=500,1701,4500
add action=mark-packet chain=prerouting comment="vpn-out packet mark VPN UDP ports"  new-packet-mark=vpn-out passthrough=no protocol=udp src-port=500,1701,4500
add action=mark-packet chain=prerouting comment="vpn-in packet mark PPTP" in-interface=ether1 new-packet-mark=vpn-in passthrough=no protocol=tcp src-port=1723
add action=mark-packet chain=prerouting comment="vpn-out packet mark PPTP" new-packet-mark=vpn-out passthrough=no protocol=tcp src-port=1723
add action=mark-packet chain=prerouting comment="all in" in-interface=ether1 new-packet-mark=in passthrough=no
add action=mark-packet chain=prerouting comment="all out" new-packet-mark=out passthrough=no
#
# Mangle identifie nos différentes portions de traffic
#
add action=mark-packet chain=prerouting comment="Famille-servers-out packet mark" new-packet-mark=Famille-servers-out passthrough=no src-address-list=Famille-servers
add action=mark-packet chain=prerouting comment="Famille-servers-in packet mark" dst-address-list=Famille-servers new-packet-mark=Famille-servers-in passthrough=no
#
# Ennonce des Queue type
#
/queue type
add kind=pfifo name=streaming-video-in pfifo-limit=500
add kind=pcq name=games-in-pcq pcq-burst-rate=0 pcq-burst-threshold=0 pcq-burst-time=10s pcq-classifier=dst-address pcq-dst-address-mask=32 pcq-dst-address6-mask=64 pcq-limit=50 pcq-rate=100k pcq-src-address-mask=32 pcq-src-address6-mask=64 pcq-total-limit=750000 queue tree
#
#
/queue tree
add burst-limit=0 burst-threshold=0 burst-time=0s disabled=no limit-at=0 max-limit=100M name=in parent=global priority=8
add burst-limit=0 burst-threshold=0 burst-time=0s disabled=no limit-at=0 max-limit=100M name=out parent=global priority=8 queue tree
add max-limit=100M name=in parent=global queue=default
add max-limit=100M name=out parent=global queue=default
add limit-at=3M max-limit=100M name=http-in packet-mark=http-in parent=in priority=4 queue=default
add limit-at=4M max-limit=100M name=streaming-video-in packet-mark=streaming-video-in parent=in priority=3 queue=streaming-video-in
add limit-at=500k max-limit=100M name=gaming-in packet-mark=games-in parent=in priority=2 queue=games-in-pcq
add max-limit=100M name=download-in packet-mark=in parent=in queue=default
add max-limit=100M name=upload-out packet-mark=out parent=out queue=default
add limit-at=500k max-limit=100M name=gaming-out packet-mark=games-out parent=out priority=2 queue=default
add limit-at=3M max-limit=100M name=http-out packet-mark=http-out parent=out priority=4 queue=default
add limit-at=4M max-limit=100M name=streaming-video-out packet-mark=streaming-video-out parent=out priority=3 queue=default
add limit-at=1M max-limit=100M name=Famille-servers-in packet-mark=Famille-servers-in parent=in priority=1 queue=default
add limit-at=1M max-limit=100M name=Famille-servers-out packet-mark=Famille-servers-out parent=out priority=1 queue=default
add limit-at=500k max-limit=100M name=voip-in packet-mark=voip-in parent=in priority=1 queue=default
add limit-at=500k max-limit=100M name=vpn-in packet-mark=vpn-in parent=in priority=2 queue=default
add limit-at=500k max-limit=100M name=voip-out packet-mark=voip-out parent=out priority=1 queue=default
add limit-at=500k max-limit=100M name=vpn-out packet-mark=vpn-out parent=out priority=2 queue=default
add limit-at=500k max-limit=100M name=admin-in packet-mark=admin-in parent=in priority=1 queue=default
add limit-at=500k max-limit=100M name=admin-out packet-mark=admin-out parent=out priority=1 queue=default
#
# L7 Matcher collecte les 10 premiers paquets d'une connexion ou les 2 premiers Ko d'une connexion et recherche le motif dans les données collectées. 
# Si le motif n'est pas trouvé dans les données collectées, le correcteur arrête alors son inspection.
# La mémoire allouée est libérée et le protocole est considéré comme inconnu. Vous devez tenir compte du fait qu'un grand nombre de connexions augmentera
# considérablement l'utilisation de la mémoire et du processeur. Pour éviter cela, ajoutez des filtres de pare-feu réguliers afin de réduire la quantité
# de données transmise aux filtres de couche 7 à plusieurs reprises.
# La condition supplémentaire est que le contrôleur de couche 7 doit voir les deux sens du trafic (entrant et sortant).
# Pour satisfaire à cette exigence,les regles l7 doivent être définies dans une  chaîne en aval. 
# Si la règle est définie dans la chaîne d'entrée / sortie, elle doit également l'être dans la chaîne de sortie / sortie, sinon les données collectées
# risquent de ne pas être complètes, ce qui entraînerait un modèle mal assorti.
# 
# Exemple d'utilisation simple du L7
# Tout d’abord, ajoutez les chaînes Regexp au menu des protocoles pour définir les chaînes que vous recherchez.
#
# Dans cet exemple, nous allons utiliser un modèle pour faire correspondre les paquets rdp.
# 
/ip firewall layer7-protocol
add name=rdp regexp="rdpdr.*cliprdr.*rdpsnd"
add comment="" name=telnet regexp="^\\xff[\\xfb-\\xfe].\\xff[\\xfb-\\xfe].\\xff[\\xfb-\\xfe]"
# Notez que nous avons besoin des deux directions, c’est pourquoi nous avons également besoin de la règle l7 dans la chaîne de sortie qui voit les paquets sortants.
#
# Youtube Matcher 
add name=youtube regexp="(GET \\/videoplayback\\\?|GET \\/crossdomain\\.xml)"
# Remarque: lorsque l'utilisateur est connecté, YouTube utilise HTTPS, ce qui signifie que L7 ne pourra pas correspondre à ce trafic.
# Seul le HTTP non crypté peut être mis en correspondance.
# Add Layer 7 torrent blocking protocols.
# 
# Blocker 100% torrent est impossible car de nos jours de nouvelles applications torrents utilisant la méthode chiffrée les rend presque impossible à inspecter au
# niveau du trafic SSL. J’ai utilisé Forefront TMG 2010 qui est capable d’inspecter le trafic SSL jusqu a un certain point.
# Cependant, nous pouvons bloquer l’accès aux torrents de base en utilisant les éléments suivants.
# (Les motifs ont été récupérés à partir de sources publiques et peu de Mikrotik et quelques tests  personnels .
# Modifié en fonction de vos besoins puis copier et coller, comme nous aimons tous copier coller n’esr ce pas? :p)
add name=commontorrentsites regexp="^.*(get|GET).+(torrent|piratebay|thepiratebay|isohunt|entertane|demonoid|btjunkie|mininova|flixflux|torrentz|vertor|h33t|btscene|bitunity|bittoxic|thunderbytes|entertane|zoozle|vcdq|bitnova|bitsoup|meganova|fulldls|btbot|flixflux|seedpeer|fenopy|gpirate|commonbits).*\$"
#
# ou sous une autre forme. Voici nos déclarations regex l7:
# 
add comment="" name=speedtest-servers regexp="^.*(get|GET).+speedtest.*\$"
add comment="" name=torrent-wwws regexp="^.*(get|GET).+(torrent|thepiratebay|isohunt|entertane|demonoid|btjunkie|mininova|flixflux|vertor|h33t|zoozle|bitnova|bitsoup|meganova|fulldls|btbot|fenopy|gpirate|commonbits).*\$"
add comment="" name=torrent-dns regexp="^.+(torrent|thepiratebay|isohunt|entertane|demonoid|btjunkie|mininova|flixflux|vertor|h33t|zoozle|bitnova|bitsoup|meganova|fulldls|btbot|fenopy|gpirate|commonbits).*\$"
add comment="" name=netflix regexp="^.*(get|GET).+(netflix).*\$"
add comment="" name=mp4 regexp="^.*(get|GET).+\\.mp4.*\$"
add comment="" name=swf regexp="^.*(get|GET).+\\.swf.*\$"
add comment="" name=flv regexp="^.*(get|GET).+\\.flv.*\$"
add name=video regexp="^.*(get|GET).+(\\.flv|\\.mp4|netflix|\\.swf).*\$"

# Ensuite, utilisez les protocoles définis dans le pare-feu.
/ip firewall filter
# ajouter quelques protocoles connus pour réduire l'utilisation de la mémoire 
# 
add action=accept chain=forward comment="" disabled=no port=80 protocol=tcp
add action=accept chain=forward comment="" disabled=no port=8080 protocol=tcp
add action=accept chain=forward comment="" disabled=no port=443 protocol=tcp
add action=accept chain=forward comment="" disabled=no layer7-protocol=rdp protocol=tcp
# Comme vous pouvez le constater avant la règle l7, nous avons ajouté plusieurs règles régulières qui correspondent au trafic connu, réduisant ainsi l’utilisation de la mémoire.
# Dans cet exemple, nous allons essayer de faire correspondre le protocole telnet se connectant à notre routeur. Test Ok ! bon pour Production.
#
# Add System Scheduler for Spamhaus, DShield, and malc0de.
/system scheduler
add comment="Download spamnaus list" interval=3d name=DownloadSpamhausList on-event=DownloadSpamhaus policy=ftp,reboot,read,write,policy,test,password,sniff,sensitive,romon start-date=may/21/2019 start-time=23:41:00
add comment="Apply spamnaus List" interval=3d name=InstallSpamhausList on-event=ReplaceSpamhaus policy=ftp,reboot,read,write,policy,test,password,sniff,sensitive,romon start-date=may/21/2019 start-time=23:46:00
add comment="Download dshield list" interval=3d name=DownloadDShieldList on-event=Download_dshield policy=ftp,reboot,read,write,policy,test,password,sniff,sensitive,romon start-date=may/21/2019 start-time=23:51:00
add comment="Apply dshield List" interval=3d name=InstallDShieldList on-event=Replace_dshield policy=ftp,reboot,read,write,policy,test,password,sniff,sensitive,romon start-date=may/21/2019 start-time=23:56:00
add comment="Download malc0de list" interval=3d name=Downloadmalc0deList on-event=Download_malc0de policy=ftp,reboot,read,write,policy,test,password,sniff,sensitive,romon start-date=may/21/2019 start-time=23:51:00
add comment="Apply malc0de List" interval=3d name=Installmalc0deList on-event=Replace_malc0de policy=ftp,reboot,read,write,policy,test,password,sniff,sensitive,romon start-date=may/21/2019 start-time=23:56:00
#
#
# Ceci est une liste de tous les ports communs trouvés sur http://en.wikipedia.org/wiki/List_of_TCP_and_UDP port_numbers et autres sources.
# Par défaut, ils sont activés pour éviter les problèmes immédiats lors de l'application du script.
# Examinez attentivement la liste des ports et supprimez ou désactivez les entrées inutiles.
#
/ip firewall filter
add action=jump chain=forward comment="Jump to \"Manage Common Ports\" Chain" jump-target="Manage Common Ports"
add chain="Manage Common Ports" comment="\"All hosts on this subnet\" Broadcast" src-address=224.0.0.1
add chain="Manage Common Ports" comment="\"All routers on this subnet\" Broadcast" src-address=224.0.0.2
add chain="Manage Common Ports" comment="DVMRP (Distance Vector Multicast Routing Protocol)" src-address=224.0.0.4
add chain="Manage Common Ports" comment="OSPF - All OSPF Routers Broadcast" src-address=224.0.0.5
add chain="Manage Common Ports" comment="OSPF - OSPF DR Routers Broadcast" src-address=224.0.0.6
add chain="Manage Common Ports" comment="RIP Broadcast" src-address=224.0.0.9
add chain="Manage Common Ports" comment="EIGRP Broadcast" src-address=224.0.0.10
add chain="Manage Common Ports" comment="PIM Broadcast" src-address=224.0.0.13
add chain="Manage Common Ports" comment="VRRP Broadcast" src-address=224.0.0.18
add chain="Manage Common Ports" comment="IS-IS Broadcast" src-address=224.0.0.19
add chain="Manage Common Ports" comment="IS-IS Broadcast" src-address=224.0.0.20
add chain="Manage Common Ports" comment="IS-IS Broadcast" src-address=224.0.0.21
add chain="Manage Common Ports" comment="IGMP Broadcast" src-address=224.0.0.22
add chain="Manage Common Ports" comment="GRE Protocol (Local Management)" protocol=gre
add chain="Manage Common Ports" comment="FTPdata transfer" port=20 protocol=tcp
add chain="Manage Common Ports" comment="FTPdata transfer  " port=20 protocol=udp
add chain="Manage Common Ports" comment="FTPcontrol (command)" port=21 protocol=tcp
add chain="Manage Common Ports" comment="Secure Shell(SSH)" port=22 protocol=tcp
add chain="Manage Common Ports" comment="Secure Shell(SSH)   " port=22 protocol=udp
add chain="Manage Common Ports" comment=Telnet port=23 protocol=tcp
add chain="Manage Common Ports" comment=Telnet port=23 protocol=udp
add chain="Manage Common Ports" comment="Priv-mail: any privatemailsystem." port=24 protocol=tcp
add chain="Manage Common Ports" comment="Priv-mail: any privatemailsystem.  " port=24 protocol=udp
add chain="Manage Common Ports" comment="Simple Mail Transfer Protocol(SMTP)" port=25 protocol=tcp
add chain="Manage Common Ports" comment="Simple Mail Transfer Protocol(SMTP)  " port=25 protocol=udp
add chain="Manage Common Ports" comment="TIME protocol" port=37 protocol=tcp
add chain="Manage Common Ports" comment="TIME protocol  " port=37 protocol=udp
add chain="Manage Common Ports" comment="ARPA Host Name Server Protocol & WINS" port=42 protocol=tcp
add chain="Manage Common Ports" comment="ARPA Host Name Server Protocol  & WINS  " port=42 protocol=udp
add chain="Manage Common Ports" comment="WHOIS protocol" port=43 protocol=tcp
add chain="Manage Common Ports" comment="WHOIS protocol" port=43 protocol=udp
add chain="Manage Common Ports" comment="Domain Name System (DNS)" port=53 protocol=tcp
add chain="Manage Common Ports" comment="Domain Name System (DNS)" port=53 protocol=udp
add chain="Manage Common Ports" comment="Mail Transfer Protocol(RFC 780)" port=57 protocol=tcp
add chain="Manage Common Ports" comment="(BOOTP) Server & (DHCP)  " port=67 protocol=udp
add chain="Manage Common Ports" comment="(BOOTP) Client & (DHCP)  " port=68 protocol=udp
add chain="Manage Common Ports" comment="Trivial File Transfer Protocol (TFTP)  " port=69 protocol=udp
add chain="Manage Common Ports" comment="Gopher protocol" port=70 protocol=tcp
add chain="Manage Common Ports" comment="Finger protocol" port=79 protocol=tcp
add chain="Manage Common Ports" comment="Hypertext Transfer Protocol (HTTP)" port=80 protocol=tcp
add chain="Manage Common Ports" comment="RemoteTELNETService protocol" port=107 protocol=tcp
add chain="Manage Common Ports" comment="Post Office Protocolv2 (POP2)" port=109 protocol=tcp
add chain="Manage Common Ports" comment="Post Office Protocolv3 (POP3)" port=110 protocol=tcp
add chain="Manage Common Ports" comment="IdentAuthentication Service/Identification Protocol" port=113 protocol=tcp
add chain="Manage Common Ports" comment="Authentication Service (auth)  " port=113 protocol=udp
add chain="Manage Common Ports" comment="Simple File Transfer Protocol (SFTP)" port=115 protocol=tcp
add chain="Manage Common Ports" comment="Network Time Protocol(NTP)" port=123 protocol=udp
add chain="Manage Common Ports" comment="NetBIOSNetBIOS Name Service" port=137 protocol=tcp
add chain="Manage Common Ports" comment="NetBIOSNetBIOS Name Service  " port=137 protocol=udp
add chain="Manage Common Ports" comment="NetBIOSNetBIOS Datagram Service" port=138 protocol=tcp
add chain="Manage Common Ports" comment="NetBIOSNetBIOS Datagram Service  " port=138 protocol=udp
add chain="Manage Common Ports" comment="NetBIOSNetBIOS Session Service" port=139 protocol=tcp
add chain="Manage Common Ports" comment="NetBIOSNetBIOS Session Service  " port=139 protocol=udp
add chain="Manage Common Ports" comment="Internet Message Access Protocol (IMAP)" port=143 protocol=tcp
add chain="Manage Common Ports" comment="Background File Transfer Program (BFTP)" port=152 protocol=tcp
add chain="Manage Common Ports" comment="Background File Transfer Program (BFTP)  " port=152 protocol=udp
add chain="Manage Common Ports" comment="SGMP,Simple Gateway Monitoring Protocol" port=153 protocol=tcp
add chain="Manage Common Ports" comment="SGMP,Simple Gateway Monitoring Protocol  " port=153 protocol=udp
add chain="Manage Common Ports" comment="DMSP, Distributed Mail Service Protocol" port=158 protocol=tcp
add chain="Manage Common Ports" comment="DMSP, Distributed Mail Service Protocol  " port=158 protocol=udp
add chain="Manage Common Ports" comment="Simple Network Management Protocol(SNMP)  " port=161 protocol=udp
add chain="Manage Common Ports" comment="Simple Network Management ProtocolTrap (SNMPTRAP)" port=162 protocol=tcp
add chain="Manage Common Ports" comment="Simple Network Management ProtocolTrap (SNMPTRAP)  " port=162 protocol=udp
add chain="Manage Common Ports" comment="BGP (Border Gateway Protocol)" port=179 protocol=tcp
add chain="Manage Common Ports" comment="Internet Message Access Protocol (IMAP), version 3" port=220 protocol=tcp
add chain="Manage Common Ports" comment="Internet Message Access Protocol (IMAP), version 3" port=220 protocol=udp
add chain="Manage Common Ports" comment="BGMP, Border Gateway Multicast Protocol" port=264 protocol=tcp
add chain="Manage Common Ports" comment="BGMP, Border Gateway Multicast Protocol  " port=264 protocol=udp
add chain="Manage Common Ports" comment="Lightweight Directory Access Protocol (LDAP)" port=389 protocol=tcp
add chain="Manage Common Ports" comment="Lightweight Directory Access Protocol (LDAP)" port=389 protocol=udp
add chain="Manage Common Ports" comment="SSTP TCP Port 443 (Local Management) & HTTPS" port=443 protocol=tcp
add chain="Manage Common Ports" comment="Microsoft-DSActive Directory, Windows shares" port=445 protocol=tcp
add chain="Manage Common Ports" comment="L2TP/ IPSEC UDP Port 500 (Local Management)" port=500 protocol=udp
add chain="Manage Common Ports" comment="Modbus, Protocol" port=502 protocol=tcp
add chain="Manage Common Ports" comment="Modbus, Protocol  " port=502 protocol=udp
add chain="Manage Common Ports" comment="Shell (Remote Shell, rsh, remsh)" port=514 protocol=tcp
add chain="Manage Common Ports" comment="Syslog - used for system logging  " port=514 protocol=udp
add chain="Manage Common Ports" comment="Routing Information Protocol (RIP)  " port=520 protocol=udp
add chain="Manage Common Ports" comment="e-mail message submission (SMTP)" port=587 protocol=tcp
add chain="Manage Common Ports" comment="LDP,Label Distribution Protocol" port=646 protocol=tcp
add chain="Manage Common Ports" comment="LDP,Label Distribution Protocol" port=646 protocol=udp
add chain="Manage Common Ports" comment="FTPS Protocol (data):FTP over TLS/SSL" port=989 protocol=tcp
add chain="Manage Common Ports" comment="FTPS Protocol (data):FTP over TLS/SSL" port=989 protocol=udp
add chain="Manage Common Ports" comment="FTPS Protocol (control):FTP over TLS/SSL" port=990 protocol=tcp
add chain="Manage Common Ports" comment="FTPS Protocol (control):FTP over TLS/SSL" port=990 protocol=udp
add chain="Manage Common Ports" comment="TELNET protocol overTLS/SSL" port=992 protocol=tcp
add chain="Manage Common Ports" comment="TELNET protocol overTLS/SSL" port=992 protocol=udp
add chain="Manage Common Ports" comment="Internet Message Access Protocol over TLS/SSL (IMAPS)" port=993 protocol=tcp
add chain="Manage Common Ports" comment="Post Office Protocol3 over TLS/SSL (POP3S)" port=995 protocol=tcp
add chain="Manage Common Ports" comment="OVPN TCP Port 1194 (Local Management)" port=1194 protocol=tcp
add chain="Manage Common Ports" comment="PPTP Port 1723 (Local Management)" port=1723 protocol=tcp
add chain="Manage Common Ports" comment="L2TP UDP Port 1701 (Local Management)" port=1701 protocol=udp
add chain="Manage Common Ports" comment="L2TP UDP Port 4500 (Local Management)" port=4500 protocol=udp
#
/ip firewall filter
add chain=input comment="Accept Related or Established Connections" connection-state=established,related disabled=yes
add chain=forward comment="Accept New Connections" connection-state=new disabled=yes
add chain=forward comment="Accept Related or Established Connections" connection-state=established,related disabled=yes

#
/ipv6 firewall filter
add chain=input action=drop connection-state=invalid comment="Drop (invalid)"
add chain=input action=accept connection-state=established,related comment="Accept (established, related)"
add chain=input action=accept in-interface=ether1protocol=udp src-port=547 limit=10,20:packet comment="Accept DHCP (10/sec)"
add chain=input action=drop in-interface=ether1 protocol=udp src-port=547 comment="Drop DHCP (>10/sec)"
add chain=input action=accept in-interface=ether1 protocol=icmpv6 limit=10,20:packet comment="Accept external ICMP (10/sec)"
add chain=input action=drop in-interface=ether1 protocol=icmpv6 comment="Drop external ICMP (>10/sec)"
add chain=input action=accept in-interface=!ether1 protocol=icmpv6 comment="Accept internal ICMP"
add chain=input action=drop in-interface=ether1 comment="Drop external"
add chain=input action=reject comment="Reject everything else"
add chain=output action=accept comment="Accept all"
add chain=forward action=drop connection-state=invalid comment="Drop (invalid)"
add chain=forward action=accept connection-state=established,related comment="Accept (established, related)"
add chain=forward action=accept in-interface=ether1 protocol=icmpv6 limit=20,50:packet comment="Accept external ICMP (20/sec)"
add chain=forward action=drop in-interface=ether1 protocol=icmpv6 comment="Drop external ICMP (>20/sec)"
add chain=forward action=accept in-interface=!ether1 comment="Accept internal"
add chain=forward action=accept out-interface=ether1-WAN comment="Accept outgoing"
add chain=forward action=drop in-interface=ether1 comment="Drop external"
add chain=forward action=reject comment="Reject everything else"




