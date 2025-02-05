# Repository Information
Name: MVC-Php-Mikrotik

# Directory Structure
Directory structure:
└── github_repos/MVC-Php-Mikrotik/
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
    │   │       ├── pack-a9325d952688c5224ada299ab83a518ebfd7ee0f.idx
    │   │       └── pack-a9325d952688c5224ada299ab83a518ebfd7ee0f.pack
    │   ├── packed-refs
    │   └── refs/
    │       ├── heads/
    │       │   └── master
    │       ├── remotes/
    │       │   └── origin/
    │       │       └── HEAD
    │       └── tags/
    ├── .htaccess
    ├── app/
    │   ├── .htaccess
    │   ├── bootstrap.php
    │   ├── config/
    │   │   ├── conexionRouter.php
    │   │   ├── config.php
    │   │   └── datosTicket.php
    │   ├── controllers/
    │   │   ├── Dashboard.php
    │   │   ├── GrupoLimiteAnchoBanda.php
    │   │   ├── Paginas.php
    │   │   ├── UsuariosHotspot.php
    │   │   └── UsuariosMikrotik.php
    │   ├── helpers/
    │   │   ├── helper.php
    │   │   └── sesionHelper.php
    │   ├── libraries/
    │   │   ├── controller.php
    │   │   ├── core.php
    │   │   ├── database.php
    │   │   └── RouterosAPI.php
    │   └── views/
    │       ├── dashboard/
    │       │   └── index.php
    │       ├── grupoLimiteAnchoBanda/
    │       │   ├── generador.php
    │       │   ├── index.php
    │       │   └── partials/
    │       │       └── modalShowProfile.php
    │       ├── paginas/
    │       │   └── login.php
    │       ├── shared/
    │       │   ├── footer.php
    │       │   ├── head.php
    │       │   ├── navbar.php
    │       │   ├── noData.php
    │       │   ├── scriptjs.php
    │       │   └── sidebar.php
    │       ├── usuariosHotspot/
    │       │   ├── activos.php
    │       │   ├── agregar.php
    │       │   ├── generador.php
    │       │   ├── index.php
    │       │   ├── partials/
    │       │   │   └── modalShowUser.php
    │       │   ├── verVouchers.php
    │       │   └── vouchers.php
    │       └── usuariosMikrotik/
    │           ├── agregar.php
    │           ├── datosTicket.php
    │           ├── editarIdentidad.php
    │           ├── editarPassword.php
    │           ├── editarPerfilMikrotik.php
    │           ├── index.php
    │           └── reiniciarMikrotik.php
    ├── public/
    │   ├── .htaccess
    │   ├── css/
    │   │   ├── material-dashboard.minf066.css
    │   │   └── style.css
    │   ├── fontawesome/
    │   │   ├── css/
    │   │   │   └── all.css
    │   │   └── webfonts/
    │   │       ├── fa-brands-400.eot
    │   │       ├── fa-brands-400.ttf
    │   │       ├── fa-brands-400.woff
    │   │       ├── fa-brands-400.woff2
    │   │       ├── fa-regular-400.eot
    │   │       ├── fa-regular-400.ttf
    │   │       ├── fa-regular-400.woff
    │   │       ├── fa-regular-400.woff2
    │   │       ├── fa-solid-900.eot
    │   │       ├── fa-solid-900.ttf
    │   │       ├── fa-solid-900.woff
    │   │       └── fa-solid-900.woff2
    │   ├── img/
    │   ├── index.php
    │   └── js/
    │       ├── grupoLimiteAnchoBanda/
    │       │   └── index.js
    │       ├── material-dashboard.minf066.js
    │       ├── plugins/
    │       │   ├── bootstrap-notify.js
    │       │   └── sweetalert2.js
    │       ├── usuariosHotspot/
    │       │   ├── activos.js
    │       │   ├── agregar.js
    │       │   ├── generador.js
    │       │   ├── index.js
    │       │   └── verVouchers.js
    │       └── usuariosMikrotik/
    │           ├── index.js
    │           └── reiniciarMikrotik.js
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
	url = https://github.com/engelcituk/MVC-Php-Mikrotik.git
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
0000000000000000000000000000000000000000 93d0bd8b685e335733b2627ebc7a52879596ba60 vivek-dodia <vivek.dodia@icloud.com> 1738606093 -0500	clone: from https://github.com/engelcituk/MVC-Php-Mikrotik.git


File: /.git\logs\refs\heads\master
0000000000000000000000000000000000000000 93d0bd8b685e335733b2627ebc7a52879596ba60 vivek-dodia <vivek.dodia@icloud.com> 1738606093 -0500	clone: from https://github.com/engelcituk/MVC-Php-Mikrotik.git


File: /.git\logs\refs\remotes\origin\HEAD
0000000000000000000000000000000000000000 93d0bd8b685e335733b2627ebc7a52879596ba60 vivek-dodia <vivek.dodia@icloud.com> 1738606093 -0500	clone: from https://github.com/engelcituk/MVC-Php-Mikrotik.git


File: /.git\packed-refs
# pack-refs with: peeled fully-peeled sorted 
93d0bd8b685e335733b2627ebc7a52879596ba60 refs/remotes/origin/master


File: /.git\refs\heads\master
93d0bd8b685e335733b2627ebc7a52879596ba60


File: /.git\refs\remotes\origin\HEAD
ref: refs/remotes/origin/master


File: /.htaccess
<IfModule mod_rewrite.c>
    RewriteEngine On
    RewriteRule ^$ public/ [L]
    RewriteRule (.*) public/$1 [L]    
</IfModule>

File: /app\.htaccess
Options -Indexes


File: /app\bootstrap.php

<?php
// carga de archivo de configuracion 
require_once 'config/config.php';
require_once 'config/conexionRouter.php';
require_once 'config/datosTicket.php';

// carga de archivos helpers
require_once 'helpers/helper.php';
require_once 'helpers/sesionHelper.php';


// carga automática de nuestros archivos de la carpeta libraries-> bibliotecas base
spl_autoload_register( function($className){
    require_once 'libraries/'. $className .'.php';
});



File: /app\config\conexionRouter.php
<?php 
            //datos de conexion router
            define("ROUTER_IP", "192.168.1.102");
            define("ROUTER_USER", "admin");
            define("ROUTER_PASS", "proyecto2020");
        

File: /app\config\config.php
<?php 

// Raíz de la aplicación
define('APPROOT', dirname(dirname (__FILE__)));
// Url raíz
define('URLROOT', 'http://localhost:8888/base');
//nombre del sitio
define('SITENAME', 'MikrotikPHP');
define('ROOTFOLDER','/base/');

File: /app\config\datosTicket.php
<?php 
                    //datos para el ticket
                    define("ENCABEZADO", "ENCABEZADO DEL TICKET XD");
                    define("PIE", "pie de pagina del ticket");
                

File: /app\controllers\Dashboard.php
<?php

class Dashboard extends Controller {
    

    public function __construct(){   
        
        if (!estaLogueado()) {
            redirect('paginas/login');
        }
         
    }
    public function index(){
        
        $this->view('dashboard/index');
    }

}


File: /app\controllers\GrupoLimiteAnchoBanda.php
<?php

class GrupoLimiteAnchoBanda extends Controller {
   
    public $API;
    public $connected;

    public function __construct(){

        $this->API = $this->routerosAPI(); //instancia de routeros

        $this->connected = connected($this->API); // llamo al helper connected y le paso la instancia de RouterOS
        
        if (!estaLogueado()) {
            redirect('paginas/login');
        }

    }
    public function index(){
        //obtengo los usersProfile
        $usersProfile = $this->getHotspotsUsersProfile();

	    $data = array('usersProfile' =>$usersProfile); // construyo un array con los datos obtenidos
        
        $this->view('grupoLimiteAnchoBanda/index', $data);
    }

    public function generador(){

        if($_SERVER['REQUEST_METHOD'] == 'POST'){
            //saneamos los datos que vienen por POST
            $_POST = filter_input_array(INPUT_POST, FILTER_SANITIZE_STRING);
            //array de campos del formulario
            $fields = [
                'nameGroup'=> trim($_POST['nameGroup']) ,
                'numberSharedUsers' => trim($_POST['numberSharedUsers']),
                'limit' => trim($_POST['limit']),
                'unidadLimit' => trim($_POST['unidadLimit']),
                'nameGroup_err' => '',
                'numberSharedUsers_err' => '',
                'limit_err'=>'',
                'unidadLimit_err'=>'',
                'messageApi' => ''

            ];

             //Sí nameGroup es vacía regresamos mensaje de validacíon
            if(empty($fields['nameGroup'])){
                $fields['nameGroup_err'] = 'Indique un nombre';
            }
            //Sí numberSharedUsers es vacía regresamos mensaje de validacíon
            if(empty($fields['numberSharedUsers'])){ 
                $fields['numberSharedUsers_err'] = 'Indique un número de usuarios compartidos';
            }
             //Sí limit es vacía regresamos mensaje de validacíon
            if(empty($fields['limit'])){ 
                $fields['limit_err'] = 'Defina un valor númerico';
            }
             //Sí unidadLimit es vacía regresamos mensaje de validacíon
             if(empty($fields['unidadLimit'])){ 
                $fields['unidadLimit_err'] = 'Por favor elija una unidad';
            }
            
            $this->saveBandwidthLimitGroup($fields); //guardo

        } else {

             //Iniciar array de campos
             $fields = [
                'nameGroup'=> '',
                'numberSharedUsers' => '',
                'limit' => '',
                'unidadLimit'=>'',
                'nameGroup_err' => '',
                'numberSharedUsers_err' => '',
                'limit_err'=>'',
                'unidadLimit_err'=>'',
                'messageApi' => ''
            ];

            $data = array('fields' => $fields ); // construyo un array con los datos

            $this->view('grupoLimiteAnchoBanda/generador', $data);
        }
    }

    public function saveBandwidthLimitGroup($fields){
        if( empty($fields['nameGroup_err']) && empty($fields['numberSharedUsers_err']) && 
            empty($fields['limit_err']) && empty($fields['unidadLimit_err'])   ){
            
            if($this->connected){

                $name = $fields['nameGroup'];
                $sharedUsers = $fields['numberSharedUsers'];
                $limit = $fields['limit'];
                $unidadLimite = $fields['unidadLimit'];
                $rateLimit = $limit.''.$unidadLimite.'/'.$limit.''.$unidadLimite;

                $this->API->write("/ip/hotspot/user/profile/add",false);	
                $this->API->write("=name=".$name,false);	
                $this->API->write("=shared-users=".$sharedUsers,false);	
                $this->API->write("=rate-limit=".$rateLimit,true);	
                $this->API->read();
                
                $fields['messageApi'] = 'Datos guardados correctamente.';
          
                flashMensaje('messageApi', $fields['messageApi'], 'alert alert-success'); 

                $data = array('fields' => $fields ); // construyo un array con los datos obtenidos

                redirect('grupolimiteanchobanda/generador'); 

            } else {

                $fields['messageApi'] = 'Falló el guardado de la información';

                flashMensaje('messageApi', $fields['messageApi'], 'alert alert-danger'); 

                $data = array('fields' => $fields ); // construyo un array con los datos obtenidos

                $this->view('usuariosHotspot/agregar', $data);

            }

        } else {

            $data = array('fields' => $fields ); // construyo un array con los datos obtenidos
   
            $this->view('grupoLimiteAnchoBanda/generador', $data);

        }
    }

    public function getHotspotsUsersProfile(){
        //Sí estoy connectado, otengo los users hotspot, se guardan en un array
        if($this->connected){

	        $this->API->write('/ip/hotspot/user/profile/print');   
            $usersProfile = $this->API->read();

        } else {

            $usersProfile = [];

        } 

        return $usersProfile;
    }
    
    public function getInfoHotspotUserProfile(){
        //si idProfile está definida y se está recibiendo por post
        if (isset($_POST['idProfile']) && $_POST['idProfile'] && isset($_POST['tokenCsrf']) && $_POST['tokenCsrf']) {

            $idProfile= $_POST['idProfile'];

            if($this->connected){

                $this->API->write("/ip/hotspot/user/profile/print",false); 

                $this->API->write("?.id=".$idProfile,true);   

                $userProfile = $this->API->read();

                $respuesta = array ('ok' => true, 'mensaje' => 'Se ha obtenido los datos' ,'userProfile'=>$userProfile);

            } else {

                $respuesta = array ('ok' => false, 'mensaje' => 'No se ha obtenido datos' ,'userProfile'=>[]);
            }

            echo json_encode($respuesta);
        }
    }

    public function updateHotspotUserProfile(){

        if (isset($_POST['user']) && $_POST['user'] && isset($_POST['tokenCsrf']) && $_POST['tokenCsrf']) {

            $usuario = $_POST['user']; //el usuario array

            $id = $usuario['id'];
            $name= $usuario['name'];
            $sharedUsers= $usuario['sharedUsers'];
            $limite= $usuario['limite'];
            $tipoUnidad= $usuario['tipoUnidad'];
            $rateLimit = $limite.''.$tipoUnidad.'/'.$limite.''.$tipoUnidad;

            if($this->connected){

                $this->API->write("/ip/hotspot/user/profile/set",false);	
                $this->API->write("=name=".$name,false);	
                $this->API->write("=shared-users=".$sharedUsers,false);	
                $this->API->write("=rate-limit=".$rateLimit,false);		
                $this->API->write("=.id=".$id,true);
                $this->API->read();

                $respuesta = array ('ok' => true, 'mensaje' => 'Se ha actualizado los datos del usuario','user' => $usuario);

            }else{
                $respuesta = array ('ok' => false, 'mensaje' => 'No se ha podido actualizar los datos del usuario','user'=>[]);
            }            
            echo json_encode($respuesta);
        }
    }

    public function deleteHotspotsUserProfile(){
        
        if (isset($_POST['id']) && $_POST['id'] && isset($_POST['tokenCsrf']) && $_POST['tokenCsrf']) {
            
            $id= $_POST['id'];

            if($this->connected){
               
                $this->API->write('/ip/hotspot/user/profile/remove',false);

                $this->API->write('=.id='.$id,true);

                $this->API->read();

                $respuesta = array ('ok' => true, 'mensaje' => 'Se ha borrado exitosamente la información');

            }else {

                $respuesta = array ('ok' => false, 'mensaje' => 'No se ha podido borrar la información');

            }

            echo json_encode($respuesta);
        }        
    }

}


File: /app\controllers\Paginas.php
<?php

class Paginas extends Controller {

    public $API;

    public function __construct(){
        $this->API = $this->routerosAPI(); 

    }

    public function index(){
       
        if (estaLogueado()) {
            redirect('dashboard');
        }

        $data = [
            'ip'=> '',
            'username' => '',
            'password' => '',
            'ip_err' => '',
            'username_err' => '',
            'messageApi'=>''
        ];
        // Cargar vista
        $this->view('paginas/login', $data);
    }

    public function login(){

        if($_SERVER['REQUEST_METHOD'] == 'POST'){
            //saneamos los datos que vienen por POST
            $_POST = filter_input_array(INPUT_POST, FILTER_SANITIZE_STRING);

            $data = [
                'ip'=> trim($_POST['ip']) ,
                'username' => trim($_POST['username']),
                'password' => trim($_POST['password']),
                'ip_err' => '',
                'username_err' => '',
                'messageApi'=>''
            ];

             //Validamos ip
            if(empty($data['ip'])){
                $data['ip_err'] = 'Por favor ingrese la ip';
            }
            //Validamos username
            if(empty($data['username'])){ 
                $data['username_err'] = 'Por favor ingrese el nombre de usuario';
            }
            // se asegura que no haya errores de validación
            if( empty($data['ip_err']) && empty($data['username_err']) ){
                $conectado = $this->conectar($data); //verifico si conecta con los datos al mikrotik
                if($conectado){ //si se conecta, se crea las variables de sesion y redirijo al dashboard
                    $this->createUserSession($data);
                    $this->writeInfoConexionRouter($data);//se escribe en el archivo de configuración los datos de acceso al router
                    redirect('dashboard');                
                }else{
                    $data['messageApi'] = '¡La conexión al Mikrotik FALLÓ! Verifique la conexión con el enrutador o el nombre de usuario/contraseña ¡Quizás no sean correctos!';
                    flashMensaje('messageApi', $data['messageApi'], 'alert alert-danger');
                    $this->view('paginas/login', $data);
                }
            }else{
                // carga la vista login con el arreglo de errores y se imprimirían en el formulario
                $this->view('paginas/login', $data);
            }

        } else {
            //Iniciar data
            $data = [
                'ip'=> '',
                'username' => '',
                'password' => '',
                'ip_err' => '',
                'username_err' => '',
                'messageApi'=>''
            ];
            // Cargar vista
            $this->view('paginas/login', $data);
        }      
    }

    public function conectar($data){
        return  $this->API->connect($data['ip'],$data['username'],$data['password']); //verifico si se conecta, me regresa un booleano
        
    }
    public function createUserSession($data){
        $_SESSION['ip'] = $data['ip'];
        $_SESSION['usuario'] = $data['username'];
        $_SESSION['tokencsrf'] = csrf_token(); //token generado gracias al helper       
    }
    public function logout(){
        //elimino las variables de sesion 
        unset($_SESSION['ip']);
        unset($_SESSION['usuario']);
        unset($_SESSION['tokencsrf']);
        unset($_SESSION['dataUsers']);


        session_destroy();// destruyo la sesion 

        redirect('paginas/login'); //redirijo la raiz
    }

    public function writeInfoConexionRouter($data){
        
        $archivo = 'conexionRouter.php';

        $ip = $data["ip"];
        $username = $data["username"]; 
        $password = $data["password"];
     
        $manejador = fopen('../app/config/'.$archivo, 'w') or die('No puede abrir el archivo '.$archivo);
        $codigo = 
        '<?php 
            //datos de conexion router
            define("ROUTER_IP", "'.$ip.'");
            define("ROUTER_USER", "'.$username.'");
            define("ROUTER_PASS", "'.$password.'");
        ';
        fwrite($manejador, $codigo);
        fclose($manejador);
    }
    
}

File: /app\controllers\UsuariosHotspot.php
<?php

class UsuariosHotspot extends Controller {
   
    public $API;
    public $connected;

    public function __construct(){

        if (!estaLogueado()) {
            redirect('paginas/login');
        }

        $this->API = $this->routerosAPI(); //instancia de routeros

        $this->connected = connected($this->API); // llamo al helper connected y le paso la instancia de RouterOS
    }

    public function index(){
        //obtengo el listado de usuarios
        $users = $this->getUsersHotspot();
        //obtengo el listado de grupos limite de anchos de banda (o perfil)
        $anchosBanda = $this->getBandwidthLimitGroup();
        // users se muestran en el datatables, anchosabanda en el modal de edit userhotspot
	    $data = array('users' =>$users, 'anchosBanda' => $anchosBanda); // construyo un array con los datos obtenidos

        $this->view('usuariosHotspot/index', $data);
    }

    public function activos(){
        //obtengo los usuarios activos
        $usersActive = $this->getUsersHotspotActive();

	    $data = array('users' =>$usersActive); // construyo un array con los datos obtenidos

        $this->view('usuariosHotspot/activos', $data);
    }

    public function generador(){
        //obtengo el listado de grupos limite de anchos de banda (o perfil)
        $anchosBanda = $this->getBandwidthLimitGroup();

        if($_SERVER['REQUEST_METHOD'] == 'POST'){
            //saneamos los datos que vienen por POST
            $_POST = filter_input_array(INPUT_POST, FILTER_SANITIZE_STRING);
            //array de campos del formulario
            $fields = [
                'longitudUser'=> trim($_POST['longitudUser']) ,
                'longitudPassword' => trim($_POST['longitudPassword']),
                'grupoLimiteAnchosBanda' => trim($_POST['grupoLimiteAnchosBanda']),
                'tipoTiempos' => trim($_POST['tipoTiempos']),
                'limiteTiempo' => trim($_POST['limiteTiempo']),
                'cantidadUsers' => trim($_POST['cantidadUsers']),
                'precio' => trim($_POST['precio']),
                'longitudUser_err' => '',
                'longitudPassword_err' => '',
                'grupoLimiteAnchosBanda_err'=>'',
                'tipoTiempos_err'=>'',
                'limiteTiempo_err'=>'',
                'cantidadUsers_err'=>'',
                'precio_err'=>'',
                'messageApi' => ''

            ];

             //Sí longitudUser es vacía regresamos mensaje de validacíon
             if(empty($fields['longitudUser'])){
                $fields['longitudUser_err'] = 'Elija la longitud de caracteres para los usuarios';
            }
            //Sí longitudPassword es vacía regresamos mensaje de validacíon
            if(empty($fields['longitudPassword'])){ 
                $fields['longitudPassword_err'] = 'Elija la longitud de caracteres para las contraseñas';
            }
             //Sí grupoLimiteAnchosBanda es vacía regresamos mensaje de validacíon
            if(empty($fields['grupoLimiteAnchosBanda'])){ 
                $fields['grupoLimiteAnchosBanda_err'] = 'Por favor elija un elemento de la lista';
            }
             //Sí tipoTiempos es vacía regresamos mensaje de validacíon
             if(empty($fields['tipoTiempos'])){ 
                $fields['tipoTiempos_err'] = 'Por favor elija un tiempo';
            }
            //Sí limiteTiempo es vacía regresamos mensaje de validacíon
            if(empty($fields['limiteTiempo'])){ 
                $fields['limiteTiempo_err'] = 'Por favor ingrese el limite de tiempo';
            }
             //Sí cantidadUsers es vacía regresamos mensaje de validacíon
            if(empty($fields['cantidadUsers'])){ 
                $fields['cantidadUsers_err'] = 'Elija la cantidad de usuarios';
            }
             //Sí precio es vacía regresamos mensaje de validacíon
             if(empty($fields['precio'])){ 
                $fields['precio_err'] = 'Por favor ingrese el precio para los vouchers';
            }
            
            $this->saveUsersHotspot($fields, $anchosBanda);

        }else{

             //Iniciar array de campos
             $fields = [
                'longitudUser'=> '',
                'longitudPassword' => '',
                'grupoLimiteAnchosBanda' => '',
                'tipoTiempos'=>'',
                'limiteTiempo'=>'',
                'cantidadUsers'=>'',
                'precio'=>'',
                'longitudUser_err' => '',
                'longitudPassword_err' => '',
                'grupoLimiteAnchosBanda_err'=>'',
                'tipoTiempos_err'=>'',
                'limiteTiempo_err'=>'',
                'cantidadUsers_err'=>'',
                'precio_err'=>'',
                'messageApi' => ''
            ];

            $data = array('anchosBanda' => $anchosBanda, 'fields' => $fields ); // construyo un array con los datos

            $this->view('usuariosHotspot/generador', $data);

        }       
    }

    public function agregar(){
        //obtengo el listado de grupos limite de anchos de banda (o perfil)
        $anchosBanda = $this->getBandwidthLimitGroup();

        if($_SERVER['REQUEST_METHOD'] == 'POST'){
            //saneamos los datos que vienen por POST
            $_POST = filter_input_array(INPUT_POST, FILTER_SANITIZE_STRING);

            //array de campos del formulario
            $fields = [
                'username'=> trim($_POST['username']) ,
                'password' => trim($_POST['password']),
                'limiteTiempo'=>trim($_POST['limiteTiempo']),
                'tipoTiempos'=>trim($_POST['tipoTiempos']),
                'grupoLimiteAnchosBanda' => trim($_POST['grupoLimiteAnchosBanda']),
                'informacion' => trim($_POST['informacion']),
                'username_err' => '',
                'password_err' => '',
                'limiteTiempo_err' => '',
                'tipoTiempos_err' => '',
                'grupoLimiteAnchosBanda_err'=>'',
                'informacion_err'=>'',
                'messageApi'=>''

            ];

            //Sí username es vacía regresamos mensaje de validacíon
            if(empty($fields['username'])){
                $fields['username_err'] = 'Por favor ingrese el nombre de usuario';
            }
            //Sí password es vacía regresamos mensaje de validacíon
            if(empty($fields['password'])){ 
                $fields['password_err'] = 'Por favor ingrese la contraseña para el usuario';
            }
            //Sí limiteTiempo es vacía regresamos mensaje de validacíon
            if(empty($fields['limiteTiempo'])){ 
                $fields['limiteTiempo_err'] = 'Por favor indique un límite de tiempos';
            }
            //Sí tipoTiempos es vacía regresamos mensaje de validacíon
            if(empty($fields['tipoTiempos'])){ 
                $fields['tipoTiempos_err'] = 'Por favor seleccione el tipo de tiempo';
            }
             //Sí grupoLimiteAnchosBanda es vacía regresamos mensaje de validacíon
            if(empty($fields['grupoLimiteAnchosBanda'])){ 
                $fields['grupoLimiteAnchosBanda_err'] = 'Por favor elija un elemento de la lista';
            }
             //Sí informacion es vacía regresamos mensaje de validacíon
             if(empty($fields['informacion'])){ 
                $fields['informacion_err'] = 'Por favor ingrese el precio';
            }
            //guardo los datos de user hotspot
            $this->saveUserHotspot($fields, $anchosBanda);

        } else {

            //Iniciar array de campos
            $fields = [
                'username'=> '',
                'password' => '',
                'limiteTiempo'=>'',
                'tipoTiempos'=>'',
                'grupoLimiteAnchosBanda' => '',
                'informacion'=>'',  
                'username_err' => '',
                'password_err' => '',
                'limiteTiempo_err' => '',
                'tipoTiempos_err' => '',
                'grupoLimiteAnchosBanda_err'=>'',
                'informacion_err'=>'',
                'messageApi' => ''
            ];

            $data = array('anchosBanda' => $anchosBanda, 'fields' => $fields ); // construyo un array con los datos

            $this->view('usuariosHotspot/agregar', $data);
        }
    }

    public function saveUsersHotspot($fields, $anchosBanda){
        //sino hay ningún campo vacío guardamos los datos
        if( empty($fields['longitudUser_err']) && empty($fields['longitudPassword_err']) && 
            empty($fields['grupoLimiteAnchosBanda_err']) && empty($fields['tipoTiempos_err']) &&
            empty($fields['limiteTiempo_err']) && empty($fields['cantidadUsers_err']) &&
            empty($fields['precio_err'])  ){

            if( $this->connected){

                $dataUsers = array();
                
                $profile = $fields['grupoLimiteAnchosBanda'];
                $tiempo = tranformarTiempo($fields['limiteTiempo'], $fields['tipoTiempos']); //helper
                $precio = $fields['precio'];//información

                for ( $i=0; $i < $fields['cantidadUsers']; $i++) { 

                    $username = generateUserString($fields['longitudUser']); //helper
                    $password = generateUserPasswordString($fields['longitudPassword']); //helper
                    
                    $this->API->write("/ip/hotspot/user/add",false);	
                    $this->API->write("=name=".$username,false);	
                    $this->API->write("=password=".$password,false);	
                    $this->API->write("=profile=".$profile,false);	
                    $this->API->write("=limit-uptime=".$tiempo,false);		
                    $this->API->write("=comment=".$precio,true);	
                    $this->API->read();

	                $dataUsers[] = ['name'=>$username,'password'=>$password, 'profile'=>$profile,'limitUptime'=>$tiempo, 'comment'=>$precio];

                }
                
                $fields['messageApi'] = 'Generación de usuarios Hotspot realizados exitosamente.';
          
                flashMensaje('messageApiSuccess', $fields['messageApi'], 'alert alert-success'); 
   
                $data = array('anchosBanda' => $anchosBanda, 'fields' => $fields ); // construyo un array con los datos obtenidos
                
                $_SESSION['dataUsers'] = json_encode($dataUsers);

                redirect('usuarioshotspot/vouchers'); // redirijo a la pagina con los datos para ver los vouchers de users

            } else {
                //si hubo falla al conectarse al mikrotik
                $fields['messageApi'] = 'Falló la generación de usuarios Hotspot';

                flashMensaje('messageApi', $fields['messageApi'], 'alert alert-danger'); 

                $data = array('anchosBanda' => $anchosBanda, 'fields' => $fields ); // construyo un array con los datos obtenidos

                $this->view('usuariosHotspot/generador', $data);
                
            }

        } else { //si hay campos vacíos se regresa el array de errores y se conserva los campos rellenados, y los datos de anchos de banda

            $data = array('anchosBanda' => $anchosBanda, 'fields' => $fields ); // construyo un array con los datos obtenidos
   
            $this->view('usuariosHotspot/generador', $data);
   
        }
    }
    
    //funcion que se encarga de procesar la logica de guardado, validar si campos están vacíos
    public function saveUserHotspot($fields, $anchosBanda){
        //sino hay ningún campo vacío guardamos los datos
        if( empty($fields['username_err']) && empty($fields['password_err']) && 
            empty($fields['limiteTiempo_err']) && empty($fields['tipoTiempos_err']) &&
            empty($fields['grupoLimiteAnchosBanda_err']) && empty($fields['informacion_err']) ){

         if($this->connected){
             
             $username = $fields['username'];
             $password = $fields['password'];
             $grupoLimiteAnchosBanda = $fields['grupoLimiteAnchosBanda']; //perfil
             $tiempo = tranformarTiempo($fields['limiteTiempo'], $fields['tipoTiempos']); //helper
             $precio = $fields['informacion'];

             $this->API->write("/ip/hotspot/user/add",false);	
             $this->API->write("=name=".$username,false);	
             $this->API->write("=password=".$password,false);	
             $this->API->write("=profile=".$grupoLimiteAnchosBanda,false);
             $this->API->write("=limit-uptime=".$tiempo,false);		
             $this->API->write("=comment=".$precio,true);	
             $this->API->read();

             $fields['messageApi'] = 'Datos de usuario Hotspot guardados correctamente.';
          
             flashMensaje('messageApi', $fields['messageApi'], 'alert alert-success'); 

             redirect('usuarioshotspot/agregar'); // redirijo a la pagina sin los datos, porque se han guardado, pero se muestra el mensaje flash               
                          
         } else {

             $fields['messageApi'] = 'Falló el guardado del Usuario Hotspot';

             flashMensaje('messageApi', $fields['messageApi'], 'alert alert-danger'); 

             $data = array('anchosBanda' => $anchosBanda, 'fields' => $fields ); // construyo un array con los datos obtenidos

             $this->view('usuariosHotspot/agregar', $data);
         }

     } else { //si hay campos vacíos se regresa el array de errores y se conserva los campos rellenados, y los datos de anchos de banda

         $data = array('anchosBanda' => $anchosBanda, 'fields' => $fields ); // construyo un array con los datos obtenidos

         $this->view('usuariosHotspot/agregar', $data);
     }
     
    }
    
    //obtengo los datos del usuario, desde una llamada ajax, ocupo el token csrf
    public function getInfoUserHotspot(){
        //si idUser está definida y se está recibiendo por post
        if (isset($_POST['idUser']) && $_POST['idUser'] && isset($_POST['tokenCsrf']) && $_POST['tokenCsrf']) {
            $idUser= $_POST['idUser'];
            if($this->connected){

                $this->API->write("/ip/hotspot/user/print",false); 

                $this->API->write("?.id=".$idUser,true);   

                $user = $this->API->read();

                $respuesta = array ('ok' => true, 'mensaje' => 'Se ha obtenido los datos del usuario','user'=>$user);
            }else{
                $respuesta = array ('ok' => false, 'mensaje' => 'No se ha obtenido datos del usuario','user'=>[]);
            }

            echo json_encode($respuesta);
        }
    }
    public function updateUserHotspot(){

        if (isset($_POST['user']) && $_POST['user'] && isset($_POST['tokenCsrf']) && $_POST['tokenCsrf']) {

            $usuario = $_POST['user']; //el usuario array

            $name= $usuario['username'];
            $password= $usuario['password'];
            $profile= $usuario['profile'];
            $comment= $usuario['comment'];
            $id = $usuario['id'];

            if($this->connected){

                $this->API->write("/ip/hotspot/user/set",false); 
                $this->API->write("=name=".$name,false);	
                $this->API->write("=password=".$password,false);	
                $this->API->write("=profile=".$profile,false);		
                $this->API->write("=comment=".$comment,false);		
                $this->API->write("=.id=".$id,true);
                $this->API->read();

                $respuesta = array ('ok' => true, 'mensaje' => 'Se ha actualizado los datos del usuario','user' => $usuario);

            }else{
                $respuesta = array ('ok' => false, 'mensaje' => 'No se ha podido actualizar los datos del usuario','user'=>[]);
            }            
            echo json_encode($respuesta);
        }
    }

    public function deleteUserHotspot(){
        
        if (isset($_POST['id']) && $_POST['id'] && isset($_POST['tokenCsrf']) && $_POST['tokenCsrf']) {
            
            $id= $_POST['id'];

            if($this->connected){
                
                $this->API->write('/ip/hotspot/user/remove',false);
                $this->API->write('=.id='.$id,true);
                $this->API->read();

                $respuesta = array ('ok' => true, 'mensaje' => 'Se ha borrado exitosamente al usuario');

            }else {
                $respuesta = array ('ok' => false, 'mensaje' => 'No se ha podido borrar los datos del usuario');

            }
            echo json_encode($respuesta);
        }        
    }

    public function resetCounterUserHotspot(){

        if (isset($_POST['id']) && $_POST['id'] && isset($_POST['tokenCsrf']) && $_POST['tokenCsrf']) {

            $id= $_POST['id'];

            if($this->connected){

                $this->API->write('/ip/hotspot/user/reset-counters',false);	
                $this->API->write('=.id='.$id,true);
                $this->API->read();

                $respuesta = array ('ok' => true, 'mensaje' => 'Se ha reseteado el contador del usuario');

            } else {
                $respuesta = array ('ok' => false, 'mensaje' => 'No se ha podido resetear el contador del usuario');

            }
            echo json_encode($respuesta);
        }        
    }

    public function getUsersHotspot(){
        //Sí estoy connectado, otengo los users hotspot, se guardan en un array
        if($this->connected){
            $this->API->write('/ip/hotspot/user/print'); 
            $users = $this->API->read(); 
        } else {
            $users = [];
        } 
        return $users;
    }

    public function getUsersHotspotActive(){
        //Sí estoy connectado, otengo los users hotspot, se guardan en un array
        if($this->connected){
	        $this->API->write("/ip/hotspot/active/print");   

            $usersActive = $this->API->read(); 
        } else {
            $usersActive = [];
        } 

        return $usersActive;
    }

    public function getBandwidthLimitGroup(){
        //Sí estoy connectado, obtengo los grupos limite de ancho de banda y los guardo en un array
        if($this->connected){
            $this->API->write("/ip/hotspot/user/profile/print");
            $anchosBanda = $this->API->read();;
        }else {
            $anchosBanda = [];
        }
        return $anchosBanda;
    }

    public function vouchers(){

        if (isset($_SESSION['dataUsers']) && $_SESSION['dataUsers']){

            $data = json_decode($_SESSION['dataUsers']);
            $this->view('usuariosHotspot/vouchers', $data);

        } else {
            $this->view('shared/noData');   
        }
    }

    public function verVouchers(){
       
        $this->view('usuariosHotspot/verVouchers');

    }

}



File: /app\controllers\UsuariosMikrotik.php
<?php

class UsuariosMikrotik extends Controller {
   
    public $API;
    public $connected;

    public function __construct()
    {     
        $this->API = $this->routerosAPI(); //instancia de routeros

        $this->connected = connected($this->API); // llamo al helper connected y le paso la instancia de RouterOS
          
        if (!estaLogueado()) {
            redirect('paginas/login');
        }
    }

    public function index(){

        //obtengo el listado de usuarios
        $usersMikrotik = $this->getUsersMikrotik();
        
	    $data = array('users' =>$usersMikrotik); // construyo un array con los datos obtenidos

        $this->view('usuariosMikrotik/index', $data);
    }

    public function agregar(){

        //obtengo el listado de usuarios
        $groupUsers = $this->getUserGroups();

        if($_SERVER['REQUEST_METHOD'] == 'POST'){

            //saneamos los datos que vienen por POST
            $_POST = filter_input_array(INPUT_POST, FILTER_SANITIZE_STRING);

            //array de campos del formulario
            $fields = [
                'name' => trim($_POST['name']),
                'groupUser'=>trim($_POST['groupUser']),
                'password' => trim($_POST['password']),
                'informacion'=>trim($_POST['informacion']),
                'name_err' => '',
                'groupUser_err' => '',
                'password_err' => '',
                'informacion_err' => '',
                'messageApi'=>''

            ];

            //Sí name es vacía regresamos mensaje de validación
            if(empty($fields['name'])){
                $fields['name_err'] = 'Por favor ingrese el nombre de usuario';
            }
            //Sí groupUser es vacía regresamos mensaje de validación
            if(empty($fields['groupUser'])){ 
                $fields['groupUser_err'] = 'Por favor seleccione un elemento de la lista';
            }

            //Sí password es vacía regresamos mensaje de validación
            if(empty($fields['password'])){ 
                $fields['password_err'] = 'Por favor ingrese la contraseña para el usuario';
            }

            //Sí informacion es vacía regresamos mensaje de validación
            if(empty($fields['informacion'])){ 
                $fields['informacion_err'] = 'Por favor ingrese la información';
            }
            //guardo los datos de user mikrotik
            $this->saveUserMikrotik($groupUsers , $fields);


        } else {
             //array de campos del formulario
             $fields = [
                'name'=> '' ,
                'groupUser'=>'',
                'password' => '',
                'informacion'=>'',
                'name_err' => '',
                'groupUser_err' => '',
                'password_err' => '',
                'informacion_err' => '',
                'messageApi'=>''

            ];

            $data = array('groupUsers' => $groupUsers, 'fields' => $fields); // construyo un array con los datos obtenidos

            $this->view('usuariosMikrotik/agregar', $data);
        }
	    
    }

    public function saveUserMikrotik($groupUsers , $fields){
       //sino hay ningún campo vacío guardamos los datos
       if(empty($fields['name_err']) && empty($fields['groupUser_err']) && 
          empty($fields['password_err']) && empty($fields['informacion_err']) ){
           
            if( $this->connected ){

                $name = $fields['name'];
                $groupUser = $fields['groupUser']; 
                $password = $fields['password'];
                $informacion = $fields['informacion'];

                $this->API->write('/user/add',false);	
                $this->API->write('=name='.$name,false);	
                $this->API->write('=group='.$groupUser,false);	
                $this->API->write('=password='.$password,true);
                $this->API->write('=comment='.$informacion,false);	
                $this->API->read();

                $fields['messageApi'] = 'Datos de usuario Mikrotik guardados correctamente.';
          
                flashMensaje('messageApi', $fields['messageApi'], 'alert alert-success'); 

                redirect('usuariosmikrotik/agregar'); // redirijo a la pagina sin los datos, porque se han guardado, pero se muestra el mensaje flash 

            } else {

                $fields['messageApi'] = 'Falló el guardado del Usuario Mikrotik';

                flashMensaje('messageApi', $fields['messageApi'], 'alert alert-danger'); 

                $data = array('groupUsers' => $groupUsers, 'fields' => $fields ); // construyo un array con los datos obtenidos

                $this->view('usuariosMikrotik/agregar', $data);

            }

       } else {

            $data = array('groupUsers' => $groupUsers, 'fields' => $fields ); // construyo un array con los datos obtenidos
    
            $this->view('usuariosMikrotik/agregar', $data);

       }

    }

    public function editarPassword(){

        if($_SERVER['REQUEST_METHOD'] == 'POST'){
            //saneamos los datos que vienen por POST
            $_POST = filter_input_array(INPUT_POST, FILTER_SANITIZE_STRING);

            //array de campos del formulario
            $fields = [
                'oldPassword' => trim($_POST['oldPassword']),
                'newPassword'=>trim($_POST['newPassword']),
                'oldPassword_err' => '',
                'newPassword_err' => '',
                'messageApi'=>''
            ];
            //Sí oldPassword es vacía regresamos mensaje de validación
            if(empty($fields['oldPassword'])){
                $fields['oldPassword_err'] = 'Por favor ingrese la contraseña anterior';
            }
            //Sí newPassword es vacía regresamos mensaje de validación
            if(empty($fields['newPassword'])){ 
                $fields['newPassword_err'] = 'Por favor indique la nueva contraseña';
            }

            $this->updatePasswordMikrotik($fields);
            
        } else {

            //array de campos del formulario
            $fields = [
                'oldPassword'=> '' ,
                'newPassword'=>'',
                'oldPassword_err' => '',
                'newPassword_err' => '',
                'messageApi'=>''

            ];

            $data = array('fields' => $fields); // construyo un array con los datos obtenidos

            $this->view('usuariosMikrotik/editarPassword', $data);

        }        
    }

    public function updatePasswordMikrotik($fields){

        if(empty($fields['oldPassword_err']) && empty($fields['newPassword_err']) ){

            $oldPassword = $fields['oldPassword'];
            $newPassword = $fields['newPassword'];

            if( $this->connected ) {

                $this->API->write("/password",false);	
                $this->API->write("=old-password=".$oldPassword,false);	
                $this->API->write("=new-password=".$newPassword,false);	
                $this->API->write("=confirm-new-password=".$newPassword,true);
                $this->API->read();
                //actualizo en el archivo conexionRouter.php la nueva contraseña
                $this->updateDatosConexionRouter($_SESSION['ip'], $_SESSION['usuario'], $newPassword); 

                $fields['messageApi'] = 'Contraseña del Mikrotik actualizado exitosamente.';
          
                flashMensaje('messageApi', $fields['messageApi'], 'alert alert-success'); 

                redirect('usuariosmikrotik/editarpassword'); 
    
            } else {

                $fields['messageApi'] = 'Falló la actualización de la contraseña del Mikrotik';

                flashMensaje('messageApi', $fields['messageApi'], 'alert alert-danger'); 

                $data = array('fields' => $fields ); // construyo un array con los datos obtenidos

                $this->view('usuariosMikrotik/agregar', $data);

            }

        } else {

            $data = array('fields' => $fields ); // construyo un array con los datos obtenidos
    
            $this->view('usuariosMikrotik/editarPassword', $data);

        }
    }

    public function updateDatosConexionRouter($ip, $username, $newPassword){
        
        $archivo = 'conexionRouter.php';
     
        $manejador = fopen('../app/config/'.$archivo, 'w') or die('No puede abrir el archivo '.$archivo);
        $codigo = 
        '<?php 
            //datos de conexion router
            define("ROUTER_IP", "'.$ip.'");
            define("ROUTER_USER", "'.$username.'");
            define("ROUTER_PASS", "'.$newPassword.'");
        ';
        fwrite($manejador, $codigo);
        fclose($manejador);
    }

    public function editarIdentidad(){

        if($_SERVER['REQUEST_METHOD'] == 'POST'){
            //saneamos los datos que vienen por POST
            $_POST = filter_input_array(INPUT_POST, FILTER_SANITIZE_STRING);

            //array de campos del formulario
            $fields = [
                'identidad' => trim($_POST['identidad']),
                'identidad_err' => '',
                'messageApi'=>''
            ];
            //Sí identidad es vacía regresamos mensaje de validación
            if(empty($fields['identidad'])){
                $fields['identidad_err'] = 'Por favor ingrese un nombre';
            }

            if( empty($fields['identidad_err']) ){

                $identidad = $fields['identidad'];

                if( $this->connected ) {

                    $this->API->write('/system/identity/set',false);	
                    $this->API->write('=name='.$identidad,true);
                    $this->API->read();

                    $fields['messageApi'] = 'Nombre del Mikrotik actualizado exitosamente.';
          
                    flashMensaje('messageApi', $fields['messageApi'], 'alert alert-success'); 

                    redirect('usuariosmikrotik/editaridentidad'); 

                } else {

                    $fields['messageApi'] = 'Falló la actualización del nombre para el Mikrotik';

                    flashMensaje('messageApi', $fields['messageApi'], 'alert alert-danger'); 

                    $data = array('fields' => $fields );

                    $this->view('usuariosMikrotik/editarIdentidad', $data);
                }
            } else {

                $data = array('fields' => $fields ); // construyo un array con los datos obtenidos
    
                $this->view('usuariosMikrotik/editarIdentidad', $data);
            }
            
        } else {

            $identidad = $this->getIdentityMikrotik(); // regresa un array, se debe acceder al indice 1 y su valor name

            $fields = [
                'identidad'=> $identidad[0]['name'],
                'identidad_err' => '',
                'messageApi'=>''
            ];

            $data = array('fields' => $fields );

            $this->view('usuariosMikrotik/editarIdentidad', $data);

        }
    }

    public function reiniciarMikrotik(){

        if($_SERVER['REQUEST_METHOD'] == 'POST'){

            if (isset($_POST['tokenCsrf']) && $_POST['tokenCsrf']) {
            
                if($this->connected){
                    
                    $this->API->write('/system/reboot',true);	
                    $this->API->read();

                    $respuesta = array ('ok' => true, 'mensaje' => 'Reinicio del equipo '.$_SESSION['usuario'].' en proceso...');
    
                    unset($_SESSION['ip']);
                    unset($_SESSION['usuario']);
                    unset($_SESSION['tokencsrf']);
                    unset($_SESSION['dataUsers']);
                    session_destroy();// destruyo la sesion
    
                } else {
    
                    $respuesta = array ('ok' => false, 'mensaje' => 'No se ha podido reiniciar el equipo');
    
                }
                echo json_encode($respuesta);
    
            }

        } else {
            
            $this->view('usuariosMikrotik/reiniciarMikrotik');             
        }
        
    }

    public function editarPerfilMikrotik(){
        //obtengo el listado de grupos
        $groupUsers = $this->getUserGroups();

        if($_SERVER['REQUEST_METHOD'] == 'POST'){
            //saneamos los datos que vienen por POST
            $_POST = filter_input_array(INPUT_POST, FILTER_SANITIZE_STRING);

            //array de campos del formulario
            $fields = [
                'id' => trim($_POST['id']),
                'name' => trim($_POST['name']),
                'groupUser'=>trim($_POST['groupUser']),
                'informacion'=>trim($_POST['informacion']),
                'name_err' => '',
                'groupUser_err' => '',
                'informacion_err' => '',
                'messageApi'=>''
            ];
            //Sí name es vacía regresamos mensaje de validación
            if(empty($fields['name'])){
                $fields['name_err'] = 'Por favor ingrese el nombre de usuario';
            }
            //Sí groupUser es vacía regresamos mensaje de validación
            if(empty($fields['groupUser'])){ 
                $fields['groupUser_err'] = 'Por favor seleccione un elemento de la lista';
            }
            //Sí informacion es vacía regresamos mensaje de validación
            if(empty($fields['informacion'])){ 
                $fields['informacion_err'] = 'Por favor ingrese la información';
            }
            //guardo los datos de user mikrotik
            $this->updateUserMikrotik($groupUsers , $fields);


        } else {

            $user = $this->getInfoUserMikrotikByName();
            $userMikrotik = $user[0]; //tomo el primer elemento de la fila
            
            $fields = [
                'id' =>$userMikrotik['.id'],
                'name'=> $userMikrotik['name'],
                'groupUser'=>$userMikrotik['group'],
                'informacion'=>$userMikrotik['comment'],
                'name_err' => '',
                'groupUser_err' => '',
                'informacion_err' => '',
                'messageApi'=>''

            ];

            $data = array('groupUsers' => $groupUsers, 'fields' => $fields); // construyo un array con los datos obtenidos

            $this->view('usuariosMikrotik/editarPerfilMikrotik', $data);
        } 
    }

    public function updateUserMikrotik($groupUsers , $fields){
        //sino hay ningún campo vacío guardamos los datos
       if(empty($fields['name_err']) && empty($fields['groupUser_err']) && empty($fields['informacion_err']) ){
           
            if( $this->connected){
                $this->API->write("/user/set",false);	
                $this->API->write("=name=".$fields['name'],false);	
                $this->API->write("=group=".$fields['groupUser'],false);	
                $this->API->write("=comment=".$fields['informacion'],false);	
                $this->API->write("=.id=".$fields['id'],true);
                $this->API->read();

                $fields['messageApi'] = 'Se actualizaron los datos del usuario Mikrotik.';
          
                flashMensaje('messageApi', $fields['messageApi'], 'alert alert-success'); 

                redirect('usuariosmikrotik/editarperfilmikrotik'); // redirijo a la pagina sin los datos, porque se han guardado, pero se muestra el mensaje flash 

           } else {

            $fields['messageApi'] = 'Falló la actualización de los datos del Usuario Mikrotik';

            flashMensaje('messageApi', $fields['messageApi'], 'alert alert-danger'); 

            $data = array('groupUsers' => $groupUsers, 'fields' => $fields ); // construyo un array con los datos obtenidos

            $this->view('usuariosMikrotik/editarPerfilMikrotik', $data);

           }

       } else {

        $data = array('groupUsers' => $groupUsers, 'fields' => $fields ); // construyo un array con los datos obtenidos
   
        $this->view('usuariosMikrotik/editarPerfilMikrotik', $data);

       }
    }

    public function getUsersMikrotik(){
        //Sí estoy connectado, otengo los users del mikrotik, se guardan en un array
        if($this->connected){
            $this->API->write('/user/print'); 
            $usersMikrotik = $this->API->read(); 
        } else {
            $usersMikrotik = [];
        } 

        return $usersMikrotik;
    }

    public function getInfoUserMikrotikByName(){
        //Sí estoy connectado, otengo los groupUsers del mikrotik, se guardan en un array
        if($this->connected){
            $this->API->write('/user/print',false);   
	        $this->API->write('?name='.$_SESSION['usuario'],true); // el name del router guardado en sesion   
            $userMikrotik = $this->API->read(); 
       
        } else {
            $userMikrotik = [];
        } 

        return $userMikrotik;
    }

    public function getUserGroups(){
        //Sí estoy connectado, otengo los groupUsers del mikrotik, se guardan en un array
        if($this->connected){
            $this->API->write('/user/group/print'); 
            $groupUsers = $this->API->read(); 
        } else {
            $groupUsers = [];
        } 

        return $groupUsers;
    }

    public function getIdentityMikrotik() {
        //Sí estoy connectado, otengo  indetidad del mikrotik, se guardan en un array
        if($this->connected){
            $this->API->write('/system/identity/print'); 
            $indetidad = $this->API->read(); 
        } else {
            $indetidad = [];
        } 

        return $indetidad;
    }


    public function deleteUserMikrotik(){
        
        if (isset($_POST['id']) && $_POST['id'] && isset($_POST['tokenCsrf']) && $_POST['tokenCsrf']) {
            
            $id= $_POST['id'];

            if($this->connected){
                
                $this->API->write('/user/remove',false);
                $this->API->write('=.id='.$id,true);
                $this->API->read();

                $respuesta = array ('ok' => true, 'mensaje' => 'Se ha borrado exitosamente al usuario');

            } else {

                $respuesta = array ('ok' => false, 'mensaje' => 'No se ha podido borrar los datos del usuario');

            }
            echo json_encode($respuesta);
        }        
    }

    public function datosTicket(){

        if($_SERVER['REQUEST_METHOD'] == 'POST'){
             //saneamos los datos que vienen por POST
             $_POST = filter_input_array(INPUT_POST, FILTER_SANITIZE_STRING);

             //array de campos del formulario
             $fields = [
                 'encabezado' => trim($_POST['encabezado']),
                 'pie'=>trim($_POST['pie']),
                 'encabezado_err' => '',
                 'pie_err' => ''
             ];
 
             //Sí encabezado es vacía regresamos mensaje de validación
             if(empty($fields['encabezado'])){
                 $fields['encabezado_err'] = 'Por favor indique un encabezado';
             }
             //Sí pie es vacía regresamos mensaje de validación
             if(empty($fields['pie'])){ 
                 $fields['pie_err'] = 'Por favor indique el pie de página';
             }

            if(empty($fields['encabezado_err']) && empty($fields['pie_err']) ){

                $archivo = 'datosTicket.php';
     
                $manejador = fopen('../app/config/'.$archivo, 'w') or die('No puede abrir el archivo '.$archivo);
                $codigo = 
                '<?php 
                    //datos para el ticket
                    define("ENCABEZADO", "'.strtoupper($fields["encabezado"]).'");
                    define("PIE", "'.$fields["pie"].'");
                ';
                fwrite($manejador, $codigo);
                fclose($manejador);

                $mensaje= 'Los datos se han cambiado exitosamente.';
          
                flashMensaje('datosTicket', $mensaje, 'alert alert-success'); 

                redirect('usuariosmikrotik/datosticket'); 

            } else {

                $mensaje= 'Error al cambiar el encabezado y pie para los tickets.';

                flashMensaje('datosTicket', $mensaje, 'alert alert-danger'); 

                $data = array('fields' => $fields ); // construyo un array con los datos obtenidos

                $this->view('usuariosMikrotik/datosTicket', $data);
            }

        } else {
            //array de campos del formulario
            $fields = [
                'encabezado'=> ENCABEZADO ,
                'pie'=> PIE,
                'encabezado_err' => '',
                'pie_err' => ''
            ];

            $data = array('fields' => $fields); 

            $this->view('usuariosMikrotik/datosTicket', $data);
        }

       

    }
}


File: /app\helpers\helper.php
<?php
// sencilla redirecion a una pagina
function redirect($pagina){

    header('location: '.URLROOT.'/'.$pagina);

}

function activeMenu($url){
    //obtener la url
    $directoryURI = $_SERVER['REQUEST_URI'];
    $path = parse_url($directoryURI, PHP_URL_PATH);
    
    return $active = ($url == $path) ? 'active' : ''; 
}

function activeMenuArray($urlArray){ //recibo un array
    $directoryURI = $_SERVER['REQUEST_URI'];
    $path = array (parse_url($directoryURI, PHP_URL_PATH));
    $existe = false;
    
    foreach ($urlArray as $value) {// recorro el array de urls
        if (in_array($value, $path)) { //path el valor permitido
            $existe = true;
            break;
        } 
    }
    return $active = $existe  ? 'active' : '';
}

function setCollapseShowArray($urlArray){ //recibo un array
    $directoryURI = $_SERVER['REQUEST_URI'];
    $path = array (parse_url($directoryURI, PHP_URL_PATH));
    $existe = false;
    
    foreach ($urlArray as $value) { // recorro el array de urls
        if (in_array($value, $path)) { //path el valor permitido
            $existe = true;
            break;
        } 
    }
    return $show = $existe  ? 'show' : '';
}

function csrf_token(){
    return md5(uniqid(mt_rand(), true));
}

function connected($API){
    return $API->connect(ROUTER_IP, ROUTER_USER, ROUTER_PASS); //constantes tomadas del archivo config/conexionRouter.php
}

 
function generateUserString( $strength = 6) {
    $permitted_chars = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ';

    $input_length = strlen($permitted_chars );
    $randomUserString = '';
    for($i = 0; $i < $strength; $i++) {
        $random_character = $permitted_chars [mt_rand(0, $input_length - 1)];
        $randomUserString .= $random_character;
    }
 
    return $randomUserString;
}

function generateUserPasswordString($strength = 6) {
    $permitted_chars = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ';

    $input_length = strlen($permitted_chars );
    $randomPasswordstring = '';
    for($i = 0; $i < $strength; $i++) {
        $random_character = $permitted_chars [mt_rand(0, $input_length - 1)];
        $randomPasswordstring .= $random_character;
    }
 
    return $randomPasswordstring;
}

function tranformarTiempo($cantidad, $tiempo){
    
    switch ($tiempo) {
        case 'minuto':
            return '00:'.$cantidad.':00';
            break;
        case 'hora':
            return $cantidad.':00:00';
            break;
        case 'dia':
            $total = $cantidad * 24;
            return $total.':00:00';           
            break;
    }
}


File: /app\helpers\sesionHelper.php
<?php

session_start();

function estaLogueado(){
    if( isset( $_SESSION['usuario']) && isset( $_SESSION['tokencsrf'])){
        return true;
    }else {
        return false;
    }
}

// helper mensaje de sesion flash
function flashMensaje($name='', $message='', $class='alert alert-success'){
    if( !empty($name) ){
        if( !empty($message) && empty($_SESSION[$name]) ){
            if( !empty($_SESSION[$name]) ){
                unset($_SESSION[$name]);
            }

            if( !empty($_SESSION[$name.'_class']) ){
                unset($_SESSION[$name.'_class']);
            }
            $_SESSION[$name] = $message;
            $_SESSION[$name.'_class'] = $class;
        }elseif( empty($message) && !empty($_SESSION[$name])){
            $class= !empty($_SESSION[$name.'_class']) ? $_SESSION[$name.'_class'] : '';
            echo '<div class="'.$class.' alert-dismissible fade show " role="alert">'.$_SESSION[$name].'
                    <button type="button" class="close" data-dismiss="alert" aria-label="Close">
                        <span aria-hidden="true">&times;</span>
                    </button>
                </div>';
            unset($_SESSION[$name]);
            unset($_SESSION[$name.'_class']);
            
        }
    }
}


File: /app\libraries\controller.php
<?php
/**
 * Controlador base
 * Carga de modelos y vistas
 */
 class Controller { 
     //cargar modelo
     public function model($model){
         // requerir el archivo del modelo
         require_once '../app/models/'.$model.'.php';
         // se instancia el modelo
         return new $model();   
     }
     //metodo para cargar la vista
     public function view($view, $data=[]){
        // verificamos que el archivo de la vista exista dentro de la carpeta vistas
        if(file_exists('../app/views/'. $view. '.php')){
            //requerimos la vista
            require_once '../app/views/'. $view. '.php';
        }else{
            // si la vista no existe
            die('La vista no existe');
        }
    }
    // requiero la clase routeros_api y genero una instancia de esta, para usar en los constructores de los controladores
    public function routerosAPI()
    {
        require_once 'RouterosAPI.php'; //ubicado dentro de la carpeta libraries

        return new RouterosAPI(); //genero la instancia
        
    }


 }

File: /app\libraries\core.php
<?php
error_reporting(E_ALL);
ini_set('display_errors', '1');
/**
 * clase principal de la aplicación
 * Crea URL y cargar del controllador nucleo
 * Formateo de la URL /controllador/metodo/parametros
 */

class Core {
     protected $controladorActual = 'Paginas';
     protected $metodoActual = 'index';
     protected $parametros = [];

     public function __construct(){
         $url = $this->getUrl();         
         // busca en los controladores el primer valor de nuestro array url
         if($url && file_exists('../app/controllers/'. ucwords($url[0]).'.php')){
             // sí existe, establezco ese controlador en la propiedad $controladorActual
             $this->controladorActual = ucwords($url[0]);
             unset($url[0]); // elimino la variable con el indice 1
         }
         // Requiero el controllador llamado de manera dinamica
         require_once '../app/controllers/'.$this->controladorActual.'.php';
         // instancio la clase controlador
         $this->controladorActual = new $this->controladorActual;

         //Revisar la segunda parte del url 
         if(isset($url[1])){
             //Revisar si el nmetodo existe en el controlador
            if (method_exists($this->controladorActual, $url[1])) {
                $this->metodoActual = $url[1];
                unset($url[1]); // elimino la variable con el indice 2
            }
         }
         // echo $this->metodoActual; 
         // obtener parametros restantes
        $this->parametros = $url ? array_values($url) : []; // operador ternario
         // llamar un callback con el array de parametros
        call_user_func_array([$this->controladorActual, $this->metodoActual], $this->parametros);
         
     }

     public function getUrl(){         
         if(isset($_GET['url'])){
             $url = rtrim($_GET['url'],'/'); // elimino los diagonales al final
             $url = filter_var($url, FILTER_SANITIZE_URL);// saneo la url
             $url = explode('/', $url); // divide la cadena en partes (creando un array)
             return $url; // regreso url en un array
         } else  {
             $url[0]='Paginas';
            return $url;
         }
     }
 }

File: /app\libraries\database.php
<?php

/**
 * Clase base de datos PDO
 * Conectar a la base de datos
 * Crear sentencias preparadas
 * Bind values (valores enlazados)
 * Retorno de resultados
 */

 class Database {

     private $host = DB_HOST;
     private $user = DB_USER;
     private $pass = DB_PASS;
     private $dbname = DB_NAME;

     private $dbh; // database handler
     private $stmt; // sentencia
     private $error;

     public function __construct()
     {
         // seteamos Nombre del Origen de Datos (DSN)
         $dsn = 'mysql:host=' . $this->host . ';dbname=' . $this->dbname;
         $options = array(
             PDO::ATTR_PERSISTENT => true,
             PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION
         );

         // creamos una instancia de pdo
         try {
             $this->dbh = new PDO($dsn, $this->user, $this->pass, $options);
         } catch(PDOException $e) {
             $this->error = $e->getMessage();
             echo $this->error;
         }
     }

     // para usar en sentencias sql
     public function query($sql){
         $this->stmt = $this->dbh->prepare($sql);
     }
     // función para enlazar valores
     public function bind($param, $value, $type = null){
         if(is_null($type)){
             switch(true){
                 case is_int($value):
                    $type = PDO::PARAM_INT;
                    break;
                case is_bool($value):
                    $type = PDO::PARAM_BOOL;
                    break;
                case is_null($value):
                    $type = PDO::PARAM_NULL;
                    break;
                default:
                    $type = PDO::PARAM_STR;

             }
         }
         $this->stmt->bindValue($param,$value, $type);
     }

     // para ejecutar la sentencia preparada (ejecutar consultas)
     public function execute(){
         return $this->stmt->execute();
     }

     //obtener el conjunto de resultados como una matriz de objetos
     public function resultSet(){
        $this->execute();
        return $this->stmt->fetchAll(PDO::FETCH_OBJ);
    }

    // para obtener un solo registro como objeto
    public function single(){
        $this->execute();
        return $this->stmt->fetch(PDO::FETCH_OBJ);
    }
    
    //obtener un recuento de filas
    public function rowCount(){
        return $this->stmt->rowCount();
    } 
 }

File: /app\libraries\RouterosAPI.php
<?php
/*****************************
 *
 * RouterOS PHP API class v1.6
 * Author: Denis Basta
 * Contributors:
 *    Nick Barnes
 *    Ben Menking (ben [at] infotechsc [dot] com)
 *    Jeremy Jefferson (http://jeremyj.com)
 *    Cristian Deluxe (djcristiandeluxe [at] gmail [dot] com)
 *
 * http://www.mikrotik.com
 * http://wiki.mikrotik.com/wiki/API_PHP_class
 *
 ******************************/

class RouterosAPI
{
    var $debug = false;      // Show debug information
    var $error_no;           // Variable for storing connection error number, if any
    var $error_str;          // Variable for storing connection error text, if any
    var $attempts = 5;  //5     // Connection attempt count
    var $connected = false;  // Connection state
    var $delay = 5;  //3        // Delay between connection attempts in seconds
    var $port = 8728;        // Port to connect to
    var $timeout = 5; //3       // Connection attempt timeout and data read timeout
    var $socket;             // Variable for storing socket resource

    /* Check, can be var used in foreach  */
    function is_iterable($var)
    {
        return $var !== null
                && (is_array($var)
                || $var instanceof Traversable
                || $var instanceof Iterator
                || $var instanceof IteratorAggregate
                );
    }
    
    /**
     * Print text for debug purposes
     *
     * @param string      $text       Text to print
     *
     * @return void
     */
    function debug($text)
    {
        if ($this->debug)
            echo $text . "\n";
    }
	
	
    /**
     * 
     *
     * @param string        $length
     *
     * @return void
     */
    function encode_length($length)
    {
        if ($length < 0x80) {
            $length = chr($length);
        } else if ($length < 0x4000) {
            $length |= 0x8000;
            $length = chr(($length >> 8) & 0xFF) . chr($length & 0xFF);
        } else if ($length < 0x200000) {
            $length |= 0xC00000;
            $length = chr(($length >> 16) & 0xFF) . chr(($length >> 8) & 0xFF) . chr($length & 0xFF);
        } else if ($length < 0x10000000) {
            $length |= 0xE0000000;
            $length = chr(($length >> 24) & 0xFF) . chr(($length >> 16) & 0xFF) . chr(($length >> 8) & 0xFF) . chr($length & 0xFF);
        } else if ($length >= 0x10000000)
            $length = chr(0xF0) . chr(($length >> 24) & 0xFF) . chr(($length >> 16) & 0xFF) . chr(($length >> 8) & 0xFF) . chr($length & 0xFF);
        return $length;
    }
	
	
    /**
     * Login to RouterOS
     *
     * @param string      $ip         Hostname (IP or domain) of the RouterOS server
     * @param string      $login      The RouterOS username
     * @param string      $password   The RouterOS password
     *
     * @return boolean                If we are connected or not
     */
    function connect($ip, $login, $password)
    {
        for ($ATTEMPT = 1; $ATTEMPT <= $this->attempts; $ATTEMPT++) {
            $this->connected = false;
            $this->debug('Connection attempt #' . $ATTEMPT . ' to ' . $ip . ':' . $this->port . '...');
            $this->socket = @fsockopen($ip, $this->port, $this->error_no, $this->error_str, $this->timeout);
            if ($this->socket) {
                socket_set_timeout($this->socket, $this->timeout);
                $this->write('/login');
                $RESPONSE = $this->read(false);
                if ($RESPONSE[0] == '!done') {
                    $MATCHES = array();
                    if (preg_match_all('/[^=]+/i', $RESPONSE[1], $MATCHES)) {
                        if ($MATCHES[0][0] == 'ret' && strlen($MATCHES[0][1]) == 32) {
                            $this->write('/login', false);
                            $this->write('=name=' . $login, false);
                            $this->write('=response=00' . md5(chr(0) . $password . pack('H*', $MATCHES[0][1])));
                            $RESPONSE = $this->read(false);
                            if ($RESPONSE[0] == '!done') {
                                $this->connected = true;
                                break;
                            }
                        }
                    }
                }
                fclose($this->socket);
            }
            sleep($this->delay);
        }
        if ($this->connected)
            $this->debug('Connected...');
        else
            $this->debug('Error...');
        return $this->connected;
    }
	
	
    /**
     * Disconnect from RouterOS
     *
     * @return void
     */
    function disconnect()
    {
        fclose($this->socket);
        $this->connected = false;
        $this->debug('Disconnected...');
    }
	
	
    /**
     * Parse response from Router OS
     *
     * @param array       $response   Response data
     *
     * @return array                  Array with parsed data
     */
    function parse_response($response)
    {
        if (is_array($response)) {
            $PARSED      = array();
            $CURRENT     = null;
            $singlevalue = null;
            foreach ($response as $x) {
                if (in_array($x, array(
                    '!fatal',
                    '!re',
                    '!trap'
                ))) {
                    if ($x == '!re') {
                        $CURRENT =& $PARSED[];
                    } else
                        $CURRENT =& $PARSED[$x][];
                } else if ($x != '!done') {
                    $MATCHES = array();
                    if (preg_match_all('/[^=]+/i', $x, $MATCHES)) {
                        if ($MATCHES[0][0] == 'ret') {
                            $singlevalue = $MATCHES[0][1];
                        }
						$CURRENT[$MATCHES[0][0]] = (isset($MATCHES[0][1]) ? $MATCHES[0][1] : '');
					}
                }
            }
            if (empty($PARSED) && !is_null($singlevalue)) {
                $PARSED = $singlevalue;
            }
            return $PARSED;
        } else
            return array();
    }
	
	
    /**
     * Parse response from Router OS
     *
     * @param array       $response   Response data
     *
     * @return array                  Array with parsed data
     */
    function parse_response4smarty($response)
    {
        if (is_array($response)) {
            $PARSED  = array();
            $CURRENT = null;
            $singlevalue = null;
            foreach ($response as $x) {
                if (in_array($x, array(
                    '!fatal',
                    '!re',
                    '!trap'
                ))) {
                    if ($x == '!re')
                        $CURRENT =& $PARSED[];
                    else
                        $CURRENT =& $PARSED[$x][];
                } else if ($x != '!done') {
                    $MATCHES = array();
                    if (preg_match_all('/[^=]+/i', $x, $MATCHES)) {
                        if ($MATCHES[0][0] == 'ret') {
                            $singlevalue = $MATCHES[0][1];
                        }
                        $CURRENT[$MATCHES[0][0]] = (isset($MATCHES[0][1]) ? $MATCHES[0][1] : '');
					}
                }
            }
            foreach ($PARSED as $key => $value) {
                $PARSED[$key] = $this->array_change_key_name($value);
            }
            return $PARSED;
            if (empty($PARSED) && !is_null($singlevalue)) {
                $PARSED = $singlevalue;
            }
        } else {
            return array();
        }
    }
	
	
    /**
     * Change "-" and "/" from array key to "_"
     *
     * @param array       $array      Input array
     *
     * @return array                  Array with changed key names
     */
    function array_change_key_name(&$array)
    {
        if (is_array($array)) {
            foreach ($array as $k => $v) {
                $tmp = str_replace("-", "_", $k);
                $tmp = str_replace("/", "_", $tmp);
                if ($tmp) {
                    $array_new[$tmp] = $v;
                } else {
                    $array_new[$k] = $v;
                }
            }
            return $array_new;
        } else {
            return $array;
        }
    }
	
	
    /**
     * Read data from Router OS
     *
     * @param boolean     $parse      Parse the data? default: true
     *
     * @return array                  Array with parsed or unparsed data
     */
    function read($parse = true)
    {
        $RESPONSE = array();
        $receiveddone = false;
        while (true) {
            // Read the first byte of input which gives us some or all of the length
            // of the remaining reply.
            $BYTE   = ord(fread($this->socket, 1));
            $LENGTH = 0;
            // If the first bit is set then we need to remove the first four bits, shift left 8
            // and then read another byte in.
            // We repeat this for the second and third bits.
            // If the fourth bit is set, we need to remove anything left in the first byte
            // and then read in yet another byte.
            if ($BYTE & 128) {
                if (($BYTE & 192) == 128) {
                    $LENGTH = (($BYTE & 63) << 8) + ord(fread($this->socket, 1));
                } else {
                    if (($BYTE & 224) == 192) {
                        $LENGTH = (($BYTE & 31) << 8) + ord(fread($this->socket, 1));
                        $LENGTH = ($LENGTH << 8) + ord(fread($this->socket, 1));
                    } else {
                        if (($BYTE & 240) == 224) {
                            $LENGTH = (($BYTE & 15) << 8) + ord(fread($this->socket, 1));
                            $LENGTH = ($LENGTH << 8) + ord(fread($this->socket, 1));
                            $LENGTH = ($LENGTH << 8) + ord(fread($this->socket, 1));
                        } else {
                            $LENGTH = ord(fread($this->socket, 1));
                            $LENGTH = ($LENGTH << 8) + ord(fread($this->socket, 1));
                            $LENGTH = ($LENGTH << 8) + ord(fread($this->socket, 1));
                            $LENGTH = ($LENGTH << 8) + ord(fread($this->socket, 1));
                        }
                    }
                }
            } else {
                $LENGTH = $BYTE;
            }
            // If we have got more characters to read, read them in.
            if ($LENGTH > 0) {
                $_      = "";
                $retlen = 0;
                while ($retlen < $LENGTH) {
                    $toread = $LENGTH - $retlen;
                    $_ .= fread($this->socket, $toread);
                    $retlen = strlen($_);
                }
                $RESPONSE[] = $_;
                $this->debug('>>> [' . $retlen . '/' . $LENGTH . '] bytes read.');
            }
            // If we get a !done, make a note of it.
            if ($_ == "!done")
                $receiveddone = true;
            $STATUS = socket_get_status($this->socket);
            if ($LENGTH > 0)
                $this->debug('>>> [' . $LENGTH . ', ' . $STATUS['unread_bytes'] . ']' . $_);
            if ((!$this->connected && !$STATUS['unread_bytes']) || ($this->connected && !$STATUS['unread_bytes'] && $receiveddone))
                break;
        }
        if ($parse)
            $RESPONSE = $this->parse_response($RESPONSE);
        return $RESPONSE;
    }
	
	
    /**
     * Write (send) data to Router OS
     *
     * @param string      $command    A string with the command to send
     * @param mixed       $param2     If we set an integer, the command will send this data as a "tag"
     *                                If we set it to boolean true, the funcion will send the comand and finish
     *                                If we set it to boolean false, the funcion will send the comand and wait for next command
     *                                Default: true
     *
     * @return boolean                Return false if no command especified
     */
    function write($command, $param2 = true)
    {
        if ($command) {
            $data = explode("\n", $command);
            foreach ($data as $com) {
                $com = trim($com);
                fwrite($this->socket, $this->encode_length(strlen($com)) . $com);
                $this->debug('<<< [' . strlen($com) . '] ' . $com);
            }
            if (gettype($param2) == 'integer') {
                fwrite($this->socket, $this->encode_length(strlen('.tag=' . $param2)) . '.tag=' . $param2 . chr(0));
                $this->debug('<<< [' . strlen('.tag=' . $param2) . '] .tag=' . $param2);
            } else if (gettype($param2) == 'boolean')
                fwrite($this->socket, ($param2 ? chr(0) : ''));
            return true;
        } else
            return false;
    }
	
	
    /**
     * Write (send) data to Router OS
     *
     * @param string      $com        A string with the command to send
     * @param array       $arr        An array with arguments or queries
     *
     * @return array                  Array with parsed
     */
    function comm($com, $arr = array())
    {
        $count = count($arr);
        $this->write($com, !$arr);
        $i = 0;
        if ($this->is_iterable($arr)) {
            foreach ($arr as $k => $v) {
                switch ($k[0]) {
                    case "?":
                        $el = "$k=$v";
                        break;
                    case "~":
                        $el = "$k~$v";
                        break;
                    default:
                        $el = "=$k=$v";
                        break;
                }

                $last = ($i++ == $count - 1);
                $this->write($el, $last);
            }
        }
        return $this->read();
    }
}
?>


File: /app\views\dashboard\index.php
<?php require APPROOT . '/views/shared/head.php'; ?>
    <body class="">
        <div class="wrapper "> 
            <!-- sidebar -->
            <?php require APPROOT . '/views/shared/sidebar.php'; ?> 
            <!-- sidebar -->
            <div class="main-panel">
            <!-- Navbar -->
                <?php require APPROOT . '/views/shared/navbar.php'; ?> 
            <!-- End Navbar -->
            <div class="content">
                <div class="content">
                    <div class="container-fluid">
                        <div class="row">
                        <div class="col-md-9">
                            <div class="card ">
                            <div class="card-header card-header-success card-header-icon">
                                <h4 class="card-title">Pagina de inicio <?php //echo $data['info']; ?> </h4>
                                <img class="img-fluid" src="<?php echo URLROOT; ?>/img/mikrotik-logo.jpg" height="300px" alt="logo mikrotik"/>
                            </div>
                            <div class="card-body ">
                                <div class="row">
                                </div>
                            </div>
                            </div>
                        </div>
                        </div>
                    </div>
                </div>
            </div>
            <!-- footer -->
            <?php require APPROOT . '/views/shared/footer.php'; ?> 
            <!-- footer -->
            </div>
        </div>
        <?php require APPROOT . '/views/shared/scriptjs.php'; ?> 
    </body>
</html>

File: /app\views\grupoLimiteAnchoBanda\generador.php
<?php require APPROOT . '/views/shared/head.php'; ?>
    <body class="">
        <div class="wrapper ">
            <!-- sidebar -->
            <?php require APPROOT . '/views/shared/sidebar.php'; ?> 
            <!-- sidebar -->
            <div class="main-panel">
            <!-- Navbar -->
                <?php require APPROOT . '/views/shared/navbar.php'; ?> 
            <!-- End Navbar -->
            <div class="content">
                <div class="content">
                    <div class="container-fluid">
                        <div class="row">
                        <div class="col-md-12">
                            <a href="<?php echo URLROOT; ?>/grupolimiteanchobanda" class="btn btn-warning mr-auto" > <i class="fas fa-arrow-left"></i> Volver</a>
                            
                            <?php flashMensaje('messageApi'); ?>

                            <div class="card ">
                                <div class="card-header card-header-success card-header-icon">
                                    <div class="card-icon">
                                        <i class="fas fa-user"></i>
                                    </div>
                                    <h4 class="card-title">Agregar grupo límite de ancho de banda Hotspot</h4>
                                </div>
                                <div class="card-body ">
                                    <div class="row">
                                        <div class="col-md-6">
                                            <form action="<?php echo URLROOT.'/grupolimiteanchobanda/generador'; ?>" method="post">
                                                <div class="form-group d-none">
                                                    <input type="text" class="form-control" name="tokenCSRF" value="<?php echo $_SESSION["tokencsrf"]; ?>">
                                                </div>
                                                <div class="form-group">
                                                    <label for="nameGroup" class="form-label"> Nombre del grupo </label> 
                                                    <input type="text" class="form-control" name="nameGroup"  aria-required="true" value="<?php echo $data['fields']['nameGroup'];?>">
                                                    <span class="error" for="nameGroup"><?php echo $data['fields']['nameGroup_err'];?></span>
                                                </div>
    
                                                <div class="form-group">
                                                    <label for="numberSharedUsers" class="form-label"> Número de usuarios (Usuarios compartidos) </label> 
                                                    <input type="number" min="1" class="form-control" name="numberSharedUsers" aria-required="true" value="<?php echo $data['fields']['numberSharedUsers'];?>" placeholder="Mínimo 1">
                                                    <span class="error"><?php echo $data['fields']['numberSharedUsers_err'];?></span>
                                                </div>

                                                <div class="form-group">
                                                    <label for="limit" class="form-label"> Límite de ancho de banda </label> 
                                                    <input type="number" min="128" class="form-control" name="limit" aria-required="true" value="<?php echo $data['fields']['limit'];?>" placeholder="por ejemplo: 128/256/512/1024">
                                                    <span class="error"><?php echo $data['fields']['limit_err'];?></span>
                                                </div>
    
                                                <div class="form-group">
                                                    <label for="unidadLimit" class="form-label"> En unidades de </label>
                                                    <select class="custom-select custom-select-sm" name="unidadLimit">
                                                        <option value='' <?php echo ($data['fields']['unidadLimit'] == '') ? 'selected': ''; ?> >Elija unidad</option>
                                                        <option value='k' <?php echo ($data['fields']['unidadLimit'] == 'k') ? 'selected': '';  ?> >Kilobyte</option>
                                                        <option value='m' <?php echo ($data['fields']['unidadLimit'] == 'm') ? 'selected': '';  ?> >Megabyte</option>
                                                       
                                                    </select> 
                                                    <span class="error"><?php echo $data['fields']['unidadLimit_err'];?></span>
                                                </div>
    
                                                <button class="btn btn-primary"> <i class="fas fa-save"></i> Guardar</button>
                                            </form>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                        </div>
                    </div>
                </div>
            </div>
            <!-- footer -->
            <?php require APPROOT . '/views/shared/footer.php'; ?> 
            <!-- footer -->
            </div>
        </div>
        <?php require APPROOT . '/views/shared/scriptjs.php'; ?> 
    </body>
</html>

File: /app\views\grupoLimiteAnchoBanda\index.php
<?php require APPROOT . '/views/shared/head.php'; ?>
    <body class="">
        <div class="wrapper ">
            <!-- sidebar -->
            <?php require APPROOT . '/views/shared/sidebar.php'; ?>  
            <!-- sidebar -->
            <div class="main-panel">
            <!-- Navbar -->
                <?php require APPROOT . '/views/shared/navbar.php'; ?> 
            <!-- End Navbar -->
            <div class="content">
                <div class="content">
                    <div class="container-fluid">
                        <div class="row">
                            <div class="col-md-12">
                               
                                <a href="<?php echo URLROOT; ?>/grupolimiteanchobanda/generador" class="btn btn-info mr-auto" ><i class="fas fa-wifi"></i> Agregar perfil</a> 
                                    
                                <div class="card ">
                                    <div class="card-header card-header-success card-header-icon">
                                        <div class="card-icon">
                                            <i class="fas fa-wifi"></i>
                                        </div>
                                        <h4 class="card-title">Usuarios Perfil hotspot</h4>    
                                    </div>
                                   
                                    <div class="card-body ">
                                        <div class="material-datatables">
                                            <table id="tablaUsersProfile" class="table table-striped table-no-bordered table-hover" cellspacing="0" width="100%" style="width:100%">
                                                <thead>
                                                    <tr>
                                                        <th>No.</th>
                                                        <th>Nombre</th>
                                                        <th>Núm. usuarios (usuarios compartidos)</th>
                                                        <th>Límite velocidad (Rx/Tx)</th>   
                                                        <th class="disabled-sorting text-right">Acciones</th>
                                                    </tr>
                                                </thead>
                                                <tbody>
                                                    <?php 
                                                        if(count( $data['usersProfile'] ) >0){ //si los datos son mayores a cero
                                                            $contador = 1;
                                                            foreach ($data['usersProfile'] as  $item) {
                                                                $id = "'".$item[".id"]."'";// pongo el id entre comillas
                                                                $name = "'".$item["name"]."'";
                                                                echo '<tr>';
                                                                echo '<td>'.$contador .'</td>';
                                                                echo '<td>'.$item["name"] .'</td>';
                                                                echo '<td>'.$item["shared-users"].'</td>';
                                                                echo '<td>'.$rateLimit = !empty($item['rate-limit']) ? $item["rate-limit"] : "".'</td>';
                                                                
                                                                echo '
                                                                    <td class="text-right">
                                                                        <button class="btn btn-sm btn-info" onclick="showHotspotsUserProfile('.$id.')"><i class="fas fa-edit"></i></button>
                                                                        
                                                                        <button class="btn btn-sm btn-danger" onclick="deleteHotspotsUserProfile('.$id.','.$name.')"><i class="fas fa-trash"></i></button>
                                                                    </td>
                                                                ';
                                                                echo '</tr>';
                                                                $contador++;
                                                            }
                                                        }
                                                    ?>
                                                </tbody>
                                            </table>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            <!-- modal modalShowUser-->
            <?php require APPROOT .'/views/grupoLimiteAnchoBanda/partials/modalShowProfile.php'; ?> 
            <!-- modal modalShowUser-->
            <!-- footer -->
            <?php require APPROOT . '/views/shared/footer.php'; ?> 
            <!-- footer -->
            </div>
        </div>
        <?php require APPROOT . '/views/shared/scriptjs.php'; ?> 
        <script src="<?php echo URLROOT; ?>/js/grupoLimiteAnchoBanda/index.js"></script> <!-- Contiene el script para aplicar datatables y más-->
    </body>
</html> 

File: /app\views\grupoLimiteAnchoBanda\partials\modalShowProfile.php

<div class="modal fade" id="hotspotUserProfile" tabindex="-1" role="dialog" aria-labelledby="hotspotUserProfileLabel" aria-hidden="true">
  <div class="modal-dialog" role="document">
    <div class="modal-content">
      <div class="modal-header">
        <h5 class="modal-title" id="hotspotUserProfileLabel">Actualizar información del perfil hotspot</h5>
        <button type="button" class="close" data-dismiss="modal" aria-label="Close">
          <span aria-hidden="true">&times;</span>
        </button>
      </div>
      <div class="modal-body">
      <form>
        <div class="card-body ">
            <div class="form-group d-none">
              <input type="text" class="form-control " id="tokenCSRF" value="<?php echo $_SESSION["tokencsrf"]; ?>">
              <input type="text" class="form-control " id="idHotspotUserProfile">
            </div>
            
            <div class="form-group">
              <label for="name" class="form-label"> Nombre del perfil *</label> 
              <input type="text" class="form-control " id="name" required="true" aria-required="true" aria-invalid="false" onkeyup="activeButton()">
              <label id="name-error" class="error" for="name"></label>
            </div>

            <div class="form-group">
               <label for="sharedUsers" class="form-label"> Número de usuarios (Usuario compartido)*</label> 
              <input type="number" min="1" class="form-control validarEntero " id="sharedUsers" required="true" aria-required="true" aria-invalid="false" onkeyup="activeButton()">
              <label id="sharedUsers-error" class="error" for="sharedUsers"></label>
            </div>
            
            <div class="form-group">
               <label for="limite" class="form-label"> Limite de ancho de banda (valores númericos)</label> 
              <input type="number" min="1" class="form-control validarEntero " id="limite" required="true" aria-required="true" aria-invalid="false" onkeyup="activeButton()">
              <label id="limite-error" class="error" for="limite"></label>
            </div> 

            

            <div class="form-group">
              <label for="unidadLimit" class="form-label"> En unidades de </label>
              <select class="custom-select custom-select-sm" name="unidadLimit" id="tipoUnidad" onchange="activeButton()">
                  <option value='' >Elija unidad</option>
                  <option value='k' >Kilobyte</option>
                  <option value='m' >Megabyte</option>
                  
              </select> 
              <label id="unidadLimit-error" class="error" for="unidadLimit"></label>
          </div>
            
                        
          </div>          
      </form>
      </div>
      <div class="modal-footer">
        <button type="button" class="btn btn-warning mr-auto" data-dismiss="modal"> <i class="fas fa-window-close"></i> Cerrar</button>
        <button type="button" class="btn btn-primary" id="btnSavehotspotUserProfile" onclick="updateHotspotUserProfile()" disabled> <i class="fas fa-save"></i> Guardar cambios</button>
      </div>
    </div>
  </div>
</div>

File: /app\views\paginas\login.php
<?php require APPROOT.'/views/shared/head.php'; ?>
<body class="off-canvas-sidebar">

  <!-- Navbar -->
  <nav class="navbar navbar-expand-lg navbar-transparent navbar-absolute fixed-top text-white">
    <div class="container">
      <div class="navbar-wrapper">
        <a class="navbar-brand" href="#pablo">Página de inicio de sesión</a>
      </div>
      <button class="navbar-toggler" type="button" data-toggle="collapse" aria-controls="navigation-index" aria-expanded="false" aria-label="Toggle navigation">
        <span class="sr-only">Toggle navigation</span>
        <span class="navbar-toggler-icon icon-bar"></span>
        <span class="navbar-toggler-icon icon-bar"></span>
        <span class="navbar-toggler-icon icon-bar"></span>
      </button>
    </div>
  </nav>
  <!-- End Navbar -->
  <div class="wrapper wrapper-full-page">
    <div class="page-header login-page header-filter" filter-color="black" style="background-image: url('<?php echo URLROOT; ?>/img/mikrotik-logo.jpg'); background-size: cover; background-position: top center;">
      <!--   you can change the color of the filter page using: data-color="blue | purple | green | orange | red | rose " -->
      <div class="container">
        <div class="row">
          <div class="col-lg-4 col-md-6 col-sm-8 ml-auto mr-auto">
            <form class="form"  action="<?php echo URLROOT . '/paginas/login'; ?>" method="post">
              <div class="card card-login card-hidden">
                <div class="card-header card-header-rose text-center">
                  <h4 class="card-title">Iniciar sesión</h4>
                  
                </div>
                <div class="card-body ">
                  <p class="card-description text-center">Ingrese los datos solicitados</p>
                  <span class="bmd-form-group ">
                    <div class="input-group">
                      <div class="input-group-prepend">
                        <span class="input-group-text">
                        <i class="fas fa-map-pin"></i>
                        </span>
                      </div>
                      
                      <input type="text" class="form-control <?php echo (!empty($data['ip_err'])) ? 'is-invalid':''; ?>" name="ip" placeholder="Dirección ip" value="<?php echo $data['ip'];?>" >
                      <span class="invalid-feedback"><?php echo $data['ip_err'];?></span>

                    </div>
                  </span>
                  <span class="bmd-form-group">
                    <div class="input-group">
                      <div class="input-group-prepend">
                        <span class="input-group-text">
                        <i class="fas fa-user"></i>
                        </span> 
                      </div>
                      <input type="text" class="form-control <?php echo (!empty($data['username_err'])) ? 'is-invalid':''; ?>" name="username" placeholder="nombre de usuario" value="<?php echo $data['username'];?>">
                      <span class="invalid-feedback"><?php echo $data['username_err'];?></span>

                    </div>
                  </span>
                  <span class="bmd-form-group">
                    <div class="input-group">
                      <div class="input-group-prepend">
                        <span class="input-group-text">
                        <i class="fas fa-lock"></i>
                        </span>
                      </div>
                      <input type="password" class="form-control"  name="password" placeholder="Contraseña...">
                      
                    </div>
                  </span>
                  
                  <br>
                  <?php flashMensaje('messageApi'); ?>
                </div>
                <div class="card-footer justify-content-center">
                  <button class="btn btn-primary"> <i class="fas fa-sign-in-alt"></i> Iniciar sesión</button>
                </div>
              </div>
            </form>
          </div>
        </div>
      </div>
    <!-- End Navbar -->
    <?php require APPROOT.'/views/shared/footer.php'; ?>
    <!-- End Navbar --> 
    </div>
  </div>
    <?php require APPROOT.'/views/shared/scriptjs.php'; ?>
    <script>
        $(document).ready(function() {
          md.checkFullPageBackgroundImage();
          setTimeout(function() {
            // after 1000 ms we add the class animated to the login/register card
            $('.card').removeClass('card-hidden');
          }, 700);
        });
        localStorage.removeItem('listaTicketsMK');
      </script>
    </body>
</html>



File: /app\views\shared\footer.php
<footer class="footer">
    <div class="container">
        <div class="copyright float-right">
        &copy;
        <script>
            document.write(new Date().getFullYear())
        </script>, Hecho con <i class="fas fa-heart fa-2x"></i> por
            <a href="https://github.com/engelcituk" target="_blank">eCituk</a> para administrar su mikrotik         
        </div>
    </div>
</footer>

File: /app\views\shared\head.php
<!DOCTYPE html>
<html lang="es">

<head>
    <meta charset="UTF-8">
    <!-- <meta name="csrf-token" content="<?php //echo estaLogueado() ? $_SESSION['tokencsrf'] : ''; ?>"> -->
    <link rel="apple-touch-icon" sizes="76x76" href="<?php echo URLROOT; ?>/img/apple-icon.png">
    <link rel="icon" type="image/png" href="<?php echo URLROOT; ?>/img/favicon.png">
    <title><?php echo SITENAME; ?></title>
    <link rel="stylesheet" href="<?php echo URLROOT; ?>/css/style.css">
    <!--     Fonts and icons     -->
    <link rel="stylesheet" type="text/css" href="<?php echo URLROOT; ?>/fontawesome/css/all.css" />
    <!-- CSS Files -->
    <link href="<?php echo URLROOT; ?>/css/material-dashboard.minf066.css" rel="stylesheet" />
</head>




File: /app\views\shared\navbar.php
<nav class="navbar navbar-expand-lg navbar-transparent navbar-absolute fixed-top ">
    <div class="container-fluid">
        <div class="navbar-wrapper">
        <div class="navbar-minimize">
            <button id="minimizeSidebar" class="btn btn-just-icon btn-white btn-fab btn-round">
            <i class=" text_align-center visible-on-sidebar-regular fas fa-ellipsis-v"></i>
            <i class=" visible-on-sidebar-mini fas fa-bars"></i>

            </button>
        </div>
        
        </div>
        <button class="navbar-toggler" type="button" data-toggle="collapse" aria-controls="navigation-index" aria-expanded="false" aria-label="Toggle navigation">
        <span class="sr-only">Toggle navigation</span>
        <span class="navbar-toggler-icon icon-bar"></span>
        <span class="navbar-toggler-icon icon-bar"></span>
        <span class="navbar-toggler-icon icon-bar"></span>
        </button>
        <div class="collapse navbar-collapse justify-content-end">
        
        <ul class="navbar-nav">
            <li class="nav-item dropdown">
            <a class="nav-link" href="#" id="navbarDropdownProfile" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
                <i class="fas fa-user"></i>
                <p class="d-lg-none d-md-block">
                Account
                </p>
            </a>
            <div class="dropdown-menu dropdown-menu-right" aria-labelledby="navbarDropdownProfile">
                <a class="dropdown-item" href="<?php echo URLROOT; ?>/usuariosmikrotik/editarperfilmikrotik">Perfil</a>
                <div class="dropdown-divider"></div>
                <a class="dropdown-item" href="<?php echo URLROOT; ?>/paginas/logout">Salir</a>
            </div>
            </li>
        </ul>
        </div>
    </div>
    </nav>

File: /app\views\shared\noData.php
<?php require APPROOT . '/views/shared/head.php'; ?>
    <body class="">
        <div class="wrapper ">
            <!-- sidebar -->
            <?php require APPROOT.'/views/shared/sidebar.php'; ?> 
            <!-- sidebar -->
            <div class="main-panel">
            <!-- Navbar -->
                <?php require APPROOT.'/views/shared/navbar.php'; ?> 
            <!-- End Navbar -->
            <div class="content">
                <div class="content">
                    <div class="container-fluid">
                        <div class="row">
                            <div class="col-md-12">
                             <a href="<?php echo URLROOT; ?>/usuarioshotspot" class="btn btn-warning mr-auto" > <i class="fas fa-arrow-left"></i> Volver</a> 
                                
                                <?php flashMensaje('messageApi'); ?>

                                <div class="card ">
                                    <div class="card-header card-header-danger card-header-icon">
                                        <div class="card-icon">
                                            <i class="fas fa-folder-open"></i>
                                        </div>
                                        <h4 class="card-title">No se recibe informacion a mostrar</h4>

                                        
                                    </div>
                                    <div class="card-body ">
                                       
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            <!-- footer -->
            <?php require APPROOT.'/views/shared/footer.php'; ?> 
            <!-- footer -->
            </div>
        </div>
        <?php require APPROOT.'/views/shared/scriptjs.php'; ?> 
        <script src="<?php echo URLROOT; ?>/js/usuariosHotspot/generador.js"></script> <!-- Contiene el script para aplicar validaciones -->
    </body>
</html>

File: /app\views\shared\scriptjs.php
  <!--   Core JS Files   -->
  <script src="<?php echo URLROOT; ?>/js/jquery.min.js"></script>
  <script src="<?php echo URLROOT; ?>/js/popper.min.js"></script>
  <script src="<?php echo URLROOT; ?>/js/bootstrap-material-design.min.js"></script>
  <script src="<?php echo URLROOT; ?>/js/perfect-scrollbar.jquery.min.js"></script>
  <!-- Control Center for Material Dashboard: parallax effects, scripts for the example pages etc -->
  <script src="<?php echo URLROOT; ?>/js/material-dashboard.minf066.js" type="text/javascript"></script>
  <!--  Plugin for Sweet Alert -->
  <script src="<?php echo URLROOT; ?>/js/plugins/sweetalert2.js"></script>
  <!--  DataTables.net Plugin, full documentation here: https://datatables.net/  -->
  <script src="<?php echo URLROOT; ?>/js/plugins/jquery.dataTables.min.js"></script>
  <!--  Notifications Plugin    -->
  <script src="<?php echo URLROOT; ?>/js/plugins/bootstrap-notify.js"></script>

    
  

File: /app\views\shared\sidebar.php
<div class="sidebar" data-color="rose" data-background-color="black" data-image="<?php echo URLROOT; ?>/img/sidebar-1.png">
      <div class="logo">
        <a href="#" class="simple-text logo-mini">
          MK
        </a>
        <a href="#" class="simple-text logo-normal">
          Mikrotik php
        </a>
      </div>
      <div class="sidebar-wrapper">
        <div class="user">
          <div class="photo">
            <img src="<?php echo URLROOT; ?>/img/avatar.png" />
          </div>
          <div class="user-info">
            <a data-toggle="collapse" href="#collapseExample" class="username">
              <span>
                 <?php echo $_SESSION['usuario'];?>
                <b class="caret"></b>
              </span>
            </a>
            <div class="collapse" id="collapseExample">
              <ul class="nav">
                <li class="nav-item">
                  <a class="nav-link" href="<?php echo URLROOT; ?>/usuariosmikrotik/editarperfilmikrotik">
                    <span class="sidebar-mini"> P </span>
                    <span class="sidebar-normal"> Perfil </span>
                  </a>
                </li>
              </ul>
            </div>
          </div>
        </div>
        <ul class="nav">
          <li class="nav-item <?php echo activeMenu(ROOTFOLDER.'dashboard'); ?>">
            <a class="nav-link" href="<?php echo URLROOT; ?>/dashboard">
            <i class="fas fa-tachometer-alt"></i>
              <p> Dashboard </p>
            </a>
          </li>
          <li class="nav-item <?php echo activeMenuArray([ROOTFOLDER.'usuarioshotspot']); ?>">
            <a class="nav-link" data-toggle="collapse" href="#pagesExamples">
            <i class="fas fa-users"></i>
              <p> Hotspot
                <b class="caret"></b>
              </p>
            </a>
            <div class="collapse <?php echo setCollapseShowArray([ROOTFOLDER.'usuarioshotspot',ROOTFOLDER.'usuarioshotspot/activos',ROOTFOLDER.'usuarioshotspot/generador',ROOTFOLDER.'usuarioshotspot/agregar']); ?>" id="pagesExamples">
              <ul class="nav">
                <li class="nav-item <?php echo activeMenu(ROOTFOLDER.'usuarioshotspot'); ?>">
                  <a class="nav-link" href="<?php echo URLROOT; ?>/usuarioshotspot">
                    <span class="sidebar-mini"> <i class="fas fa-users"></i> </span>
                    <span class="sidebar-normal">Usuarios hotspot </span>
                  </a>
                </li>
                <li class="nav-item <?php echo activeMenu(ROOTFOLDER.'usuarioshotspot/activos'); ?>">
                  <a class="nav-link" href="<?php echo URLROOT; ?>/usuarioshotspot/activos">
                    <span class="sidebar-mini"> <i class="fas fa-hourglass-start"></i> </span>
                    <span class="sidebar-normal"> Usuarios activos </span>
                  </a>
                </li>
                <li class="nav-item <?php echo activeMenu(ROOTFOLDER.'usuarioshotspot/generador'); ?>">
                  <a class="nav-link" href="<?php echo URLROOT; ?>/usuarioshotspot/generador">
                    <span class="sidebar-mini"> <i class="fas fa-plus-square"></i>  </span>
                    <span class="sidebar-normal"> Generador </span>
                  </a>
                </li>
                <li class="nav-item <?php echo activeMenu(ROOTFOLDER.'usuarioshotspot/agregar'); ?>">
                  <a class="nav-link" href="<?php echo URLROOT; ?>/usuarioshotspot/agregar">
                    <span class="sidebar-mini"> <i class="fas fa-user"></i>  </span>
                    <span class="sidebar-normal"> Agregar usuario </span>
                  </a>
                </li>
                
              </ul>
            </div>
          </li>
          <li class="nav-item <?php echo activeMenuArray([ROOTFOLDER.'grupolimiteanchobanda',ROOTFOLDER.'grupolimiteanchobanda/generador']); ?>">
            <a class="nav-link" data-toggle="collapse" href="#componentsExamples">
            <i class="fas fa-wifi"></i>
              <p> Perfiles
                <b class="caret"></b>
              </p>
            </a>
            <div class="collapse <?php echo setCollapseShowArray([ROOTFOLDER.'grupolimiteanchobanda',ROOTFOLDER.'grupolimiteanchobanda/generador']); ?> " id="componentsExamples">
              <ul class="nav">
                <li class="nav-item <?php echo activeMenu(ROOTFOLDER.'grupolimiteanchobanda'); ?>">
                  <a class="nav-link" href="<?php echo URLROOT; ?>/grupolimiteanchobanda">
                    <span class="sidebar-mini"> <i class="fas fa-list"></i> </span>
                    <span class="sidebar-normal"> Lista de grupo límite </span>
                  </a>
                </li>
                <li class="nav-item <?php echo activeMenu(ROOTFOLDER.'grupolimiteanchobanda/generador'); ?>">
                  <a class="nav-link" href="<?php echo URLROOT; ?>/grupolimiteanchobanda/generador">
                    <span class="sidebar-mini"> <i class="fas fa-layer-group"></i> </span>
                    <span class="sidebar-normal"> Agregar grupo limite </span>
                  </a>
                </li>
                
                
              </ul>
            </div>
          </li>
          <li class="nav-item <?php echo activeMenuArray([ROOTFOLDER.'usuariosmikrotik/editarperfilmikrotik',ROOTFOLDER.'usuariosmikrotik',ROOTFOLDER.'usuariosmikrotik/editarpassword',ROOTFOLDER.'usuariosmikrotik/editaridentidad',ROOTFOLDER.'usuariosmikrotik/reiniciarmikrotik',ROOTFOLDER.'usuariosmikrotik/datosticket']); ?>">
            <a class="nav-link" data-toggle="collapse" href="#formsExamples">
            <i class="fas fa-bars"></i>
              <p> Extras mikrotik
                <b class="caret"></b>
              </p>
            </a>
            <div class="collapse <?php echo setCollapseShowArray([ROOTFOLDER.'usuariosmikrotik/editarperfilmikrotik',ROOTFOLDER.'usuariosmikrotik',ROOTFOLDER.'usuariosmikrotik/editarpassword',ROOTFOLDER.'usuariosmikrotik/agregar',ROOTFOLDER.'usuariosmikrotik/editaridentidad',ROOTFOLDER.'usuariosmikrotik/reiniciarmikrotik',ROOTFOLDER.'usuariosmikrotik/datosticket']); ?>" id="formsExamples">
              <ul class="nav">
                <li class="nav-item <?php echo activeMenu(ROOTFOLDER.'usuariosmikrotik'); ?>">
                  <a class="nav-link" href="<?php echo URLROOT; ?>/usuariosmikrotik">
                    <span class="sidebar-mini"> <i class="fas fa-users"></i> </span>
                    <span class="sidebar-normal"> Usuarios admin </span>
                  </a>
                </li>
                <li class="nav-item <?php echo activeMenu(ROOTFOLDER.'usuariosmikrotik/agregar'); ?>">
                  <a class="nav-link" href="<?php echo URLROOT; ?>/usuariosmikrotik/agregar">
                    <span class="sidebar-mini"> <i class="fas fa-plus-square"></i> </span>
                    <span class="sidebar-normal"> Agregar </span>
                  </a>
                </li>
                <li class="nav-item <?php echo activeMenu(ROOTFOLDER.'usuariosmikrotik/editarperfilmikrotik'); ?>">
                  <a class="nav-link" href="<?php echo URLROOT; ?>/usuariosmikrotik/editarperfilmikrotik ">
                    <span class="sidebar-mini"> <i class="fas fa-user-circle"></i> </span>
                    <span class="sidebar-normal"> Perfil </span>
                  </a>
                </li>
                <li class="nav-item <?php echo activeMenu(ROOTFOLDER.'usuariosmikrotik/editarpassword'); ?>">
                  <a class="nav-link" href="<?php echo URLROOT; ?>/usuariosmikrotik/editarpassword">
                    <span class="sidebar-mini"> <i class="fas fa-lock"></i> </span>
                    <span class="sidebar-normal"> Editar contraseña MKT </span>
                  </a>
                </li>
                <li class="nav-item <?php echo activeMenu(ROOTFOLDER.'usuariosmikrotik/editaridentidad'); ?>">
                  <a class="nav-link" href="<?php echo URLROOT; ?>/usuariosmikrotik/editaridentidad">
                    <span class="sidebar-mini"> <i class="fas fa-file-signature"></i> </span>
                    <span class="sidebar-normal"> Editar identidad MKT </span>
                  </a>
                </li>
                
                <li class="nav-item <?php echo activeMenu(ROOTFOLDER.'usuariosmikrotik/datosticket'); ?>">
                <a class="nav-link" href="<?php echo URLROOT; ?>/usuariosmikrotik/datosticket">
                    <span class="sidebar-mini"> <i class="fas fa-ticket-alt"></i></span>
                    <span class="sidebar-normal"> Datos Ticket </span>
                  </a>
                </li>

                <li class="nav-item <?php echo activeMenu(ROOTFOLDER.'usuariosmikrotik/reiniciarmikrotik'); ?>">
                  <a class="nav-link" href="<?php echo URLROOT; ?>/usuariosmikrotik/reiniciarmikrotik">
                    <span class="sidebar-mini"> <i class="fas fa-power-off"></i> </span>
                    <span class="sidebar-normal"> Reiniciar Mikrotik </span>
                  </a>
                </li>

              </ul>
            </div>
          </li>

        </ul>
      </div>
    </div>

File: /app\views\usuariosHotspot\activos.php
<?php require APPROOT . '/views/shared/head.php'; ?>
    <body class="">
        <div class="wrapper ">
            <!-- sidebar -->
            <?php require APPROOT . '/views/shared/sidebar.php'; ?>  
            <!-- sidebar -->
            <div class="main-panel">
            <!-- Navbar -->
                <?php require APPROOT . '/views/shared/navbar.php'; ?> 
            <!-- End Navbar -->
            <div class="content">
                <div class="content">
                    <div class="container-fluid">
                        <div class="row">
                            <div class="col-md-12">
                                
                            <a href="<?php echo URLROOT; ?>/usuarioshotspot" class="btn btn-warning mr-auto" > <i class="fas fa-arrow-left"></i> Volver</a> 
                                
                                <div class="card ">
                                    <div class="card-header card-header-success card-header-icon">
                                        <div class="card-icon">
                                            <i class="fa fa-users"></i>
                                        </div>
                                        <h4 class="card-title">Usuarios hotspot en activo</h4>
                                    </div>
                                   
                                    <div class="card-body ">
                                        <div class="material-datatables">
                                            <table id="tablaUsersActive" class="table table-striped table-no-bordered table-hover" cellspacing="0" width="100%" style="width:100%">
                                                <thead>
                                                    <tr>
                                                        <th>No.</th>
                                                        <th>Usuario</th>
                                                        <th>Dirección</th>
                                                        <th>Tiempo Límite</th>
                                                        <th>Dirección Mac</th>
                                                        <th>T en uso</th>
                                                    </tr>
                                                </thead>
                                                <tbody>
                                                    <?php 
                                                        if(count($data['users'])>0){ //si los datos son mayores a cero
                                                            $contador = 1;
                                                            foreach ($data['users'] as  $item) {
                                                                
                                                                echo '<tr>';
                                                                    echo '<td>'.$contador .'</td>';
                                                                    echo '<td>'.$item["user"].'</td>';
                                                                    echo '<td>'.$item["address"].'</td>';
                                                                    echo '<td>'.$item["uptime"].'</td>';
                                                                    echo '<td>'.$item["mac-address"].'</td>';
                                                                    echo '<td>'.$item["login-by"].'</td>';

                                                                echo '</tr>';
                                                                $contador++;
                                                            }
                                                        }
                                                    ?>
                                                    
                                                </tbody>
                                            </table>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            <!-- footer -->
            <?php require APPROOT . '/views/shared/footer.php'; ?> 
            <!-- footer -->
            </div>
        </div>
        <?php require APPROOT . '/views/shared/scriptjs.php'; ?> 
        <script src="<?php echo URLROOT; ?>/js/usuariosHotspot/activos.js"></script> <!-- Contiene el script para aplicar datatables -->
    </body>
</html> 

File: /app\views\usuariosHotspot\agregar.php
<?php require APPROOT . '/views/shared/head.php'; ?>
    <body class="">
        <div class="wrapper ">
            <!-- sidebar -->
            <?php require APPROOT . '/views/shared/sidebar.php'; ?> 
            <!-- sidebar -->
            <div class="main-panel">
            <!-- Navbar -->
                <?php require APPROOT . '/views/shared/navbar.php'; ?> 
            <!-- End Navbar -->
            <div class="content">
                <div class="content">
                    <div class="container-fluid">
                        <div class="row">
                        <div class="col-md-12">
                            <a href="<?php echo URLROOT; ?>/usuarioshotspot" class="btn btn-warning mr-auto" > <i class="fas fa-arrow-left"></i> Volver</a>
                            
                            <?php flashMensaje('messageApi'); ?>

                            <div class="card ">
                                <div class="card-header card-header-success card-header-icon">
                                    <div class="card-icon">
                                        <i class="fas fa-user"></i>
                                    </div>
                                    <h4 class="card-title">Agregar un solo usuario hotspot</h4>
                                </div>
                                <div class="card-body ">
                                    <div class="row">
                                        <div class="col-md-6">
                                            <form action="<?php echo URLROOT.'/usuarioshotspot/agregar'; ?>" method="post">
                                                <div class="form-group d-none">
                                                    <input type="text" class="form-control" name="tokenCSRF" value="<?php echo $_SESSION["tokencsrf"]; ?>">
                                                </div>
                                                <div class="form-group">
                                                    <label for="username" class="form-label"> Nombre de usuario *</label> 
                                                    <input type="text" class="form-control" name="username"  aria-required="true" value="<?php echo $data['fields']['username'];?>">
                                                    <span class="error" for="username"><?php echo $data['fields']['username_err'];?></span>
                                                </div>
    
                                                <div class="form-group">
                                                    <label for="password" class="form-label"> Contraseña *</label> 
                                                    <input type="password" class="form-control" name="password" aria-required="true" value="<?php echo $data['fields']['password'];?>">
                                                    <span class="error"><?php echo $data['fields']['password_err'];?></span>
                                                </div>

                                                <div class="form-group">
                                                    <label for="limiteTiempo" class="form-label"> Límite de tiempo *</label> 
                                                    <input type="number" min="1" class="form-control validarEntero" name="limiteTiempo" aria-required="true" value="<?php echo $data['fields']['limiteTiempo'];?>" placeholder="ingrese un numero para minutos, horas o días">
                                                    <span class="error"><?php echo $data['fields']['limiteTiempo_err'];?></span>
                                                </div>

                                                <div class="form-group">
                                                    <label for="tt" class="form-label"> Tipo de tiempos*</label>
                                                    <select class="custom-select custom-select-sm" name="tipoTiempos">
                                                        <option value="" <?php echo ($data['fields']['tipoTiempos'] == '' ) ? 'selected': ''; ?> >Elija un tiempo</option>
                                                        <option value="minuto" <?php echo ($data['fields']['tipoTiempos'] == 'minuto' ) ? 'selected': ''; ?> >Minuto</option>
                                                        <option value="hora" <?php echo ($data['fields']['tipoTiempos'] == 'hora' ) ? 'selected': ''; ?> >Hora</option>
                                                        <option value="dia" <?php echo ($data['fields']['tipoTiempos'] == 'dia' ) ? 'selected': ''; ?> >Día </option>
                                                        
                                                    </select> 
                                                    <span class="error"><?php echo $data['fields']['tipoTiempos_err'];?></span>
                                                </div>
 

                                                <div class="form-group">
                                                    <label for="GLAB" class="form-label"> Perfiles *</label>
                                                    <select class="custom-select custom-select-sm" name="grupoLimiteAnchosBanda">
                                                        <?php $selected = ($data['fields']['grupoLimiteAnchosBanda'] == '') ? 'selected': '';?>
                                                        <option value='' <?php echo $selected; ?> >Elija</option>
                                                        <?php 

                                                            foreach ($data["anchosBanda"] as $item) {
                                                                $selected = ($data['fields']['grupoLimiteAnchosBanda'] == $item["name"]) ? 'selected': '';
                                                                $dash = !empty($item['rate-limit']) ? '--' : ''; //dash es un guion
                                                                echo '<option value="'.$item["name"].'" '.$selected.'>'.$item["name"].$dash.$item["rate-limit"].'</option>';
                                                        }
                                                        ?>
                                                    </select> 
                                                    <span class="error"><?php echo $data['fields']['grupoLimiteAnchosBanda_err'];?></span>
                                                </div>
    
                                                <div class="form-group">
                                                    <label for="información" class="form-label"> Precio *</label>
                                                    <textarea class="form-control" name="informacion" rows="2" aria-required="true"> <?php echo $data['fields']['informacion'];?></textarea>
                                                    <span class="error"><?php echo $data['fields']['informacion_err'];?></span>
                                                </div> 
                                                <button class="btn btn-primary"> <i class="fas fa-save"></i> Guardar usuario</button>
                                            </form>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                        </div>
                    </div>
                </div>
            </div>
            <!-- footer -->
            <?php require APPROOT . '/views/shared/footer.php'; ?> 
            <!-- footer -->
            </div>
        </div>
        <?php require APPROOT . '/views/shared/scriptjs.php'; ?> 
        <script src="<?php echo URLROOT; ?>/js/usuariosHotspot/agregar.js"></script> <!-- Contiene el script para aplicar validaciones -->

    </body>
</html>

File: /app\views\usuariosHotspot\generador.php
<?php require APPROOT . '/views/shared/head.php'; ?>
    <body class="">
        <div class="wrapper ">
            <!-- sidebar -->
            <?php require APPROOT . '/views/shared/sidebar.php'; ?> 
            <!-- sidebar -->
            <div class="main-panel">
            <!-- Navbar -->
                <?php require APPROOT . '/views/shared/navbar.php'; ?> 
            <!-- End Navbar -->
            <div class="content">
                <div class="content">
                    <div class="container-fluid">
                        <div class="row">
                            <div class="col-md-12">
                            <a href="<?php echo URLROOT; ?>/usuarioshotspot" class="btn btn-warning mr-auto" > <i class="fas fa-arrow-left"></i> Volver</a> 
                                
                                <?php flashMensaje('messageApi'); ?>

                                <div class="card ">
                                    <div class="card-header card-header-success card-header-icon">
                                        <div class="card-icon">
                                            <i class="fas fa-users"></i>
                                        </div>
                                        <h4 class="card-title">Generador de usuarios hotspot</h4>

                                        
                                    </div>
                                    <div class="card-body ">
                                        <form action="<?php echo URLROOT.'/usuarioshotspot/generador'; ?>" method="post">
                                            <div class="row">
                                                <div class="col-md-6">
                                                    <div class="form-group d-none">
                                                        <input type="text" class="form-control" name="tokenCSRF" value="<?php echo $_SESSION["tokencsrf"]; ?>">
                                                    </div>
                                                    
                                                    <div class="form-group">
                                                        <label for="GLAB" class="form-label"> Longitud del nombre de usuario*</label>
                                                        <select class="custom-select custom-select-sm" name="longitudUser">
                                                            <option value="" <?php echo ($data['fields']['longitudUser'] == '' ) ? 'selected': ''; ?> >Elija longitud</option>
                                                            <option value="3" <?php echo ($data['fields']['longitudUser'] == 3 ) ? 'selected': ''; ?> >3</option>
                                                            <option value="4" <?php echo ($data['fields']['longitudUser'] == 4 ) ? 'selected': ''; ?> >4</option>
                                                            <option value="5" <?php echo ($data['fields']['longitudUser'] == 5 ) ? 'selected': ''; ?> >5</option>
                                                            <option value="6" <?php echo ($data['fields']['longitudUser'] == 6 ) ? 'selected': ''; ?> >6</option>
                                                        </select> 
                                                        <span class="error"><?php echo $data['fields']['longitudUser_err'];?></span>
                                                    </div>

                                                    <div class="form-group">
                                                        <label for="GLAB" class="form-label"> Perfil *</label>
                                                        <select class="custom-select custom-select-sm" name="grupoLimiteAnchosBanda">
                                                            <?php $selected = ($data['fields']['grupoLimiteAnchosBanda'] == '') ? 'selected': '';?>
                                                            <option value='' <?php echo $selected; ?> >Elija</option>
                                                            <?php 
                                                                foreach ($data['anchosBanda'] as $item) {
                                                                    $selected = ($data['fields']['grupoLimiteAnchosBanda'] == $item["name"]) ? 'selected': '';
                                                                    $dash = !empty($item['rate-limit']) ? '--' : ''; //dash es un guion
                                                                    echo '<option value="'.$item["name"].'" '.$selected.'>'.$item["name"].$dash.$item["rate-limit"].'</option>';
                                                            }
                                                            ?>
                                                        </select> 
                                                        <span class="error"><?php echo $data['fields']['grupoLimiteAnchosBanda_err'];?></span>
                                                    </div>


                                                    <div class="form-group">
                                                        <label for="limiteTiempo" class="form-label"> Límite de tiempo *</label> 
                                                        <input type="number" min="1" class="form-control validarEntero" name="limiteTiempo" aria-required="true" value="<?php echo $data['fields']['limiteTiempo'];?>" placeholder="ingrese un numero para minutos, horas o días">
                                                        <span class="error"><?php echo $data['fields']['limiteTiempo_err'];?></span>
                                                    </div>

                                                    <div class="form-group">
                                                        <label for="información" class="form-label"> Precio </label>
                                                        <textarea class="form-control" name="precio" rows="2" aria-required="true" > <?php echo $data['fields']['precio'];?></textarea>
                                                        <span class="error"><?php echo $data['fields']['precio_err'];?></span>
                                                    </div> 
                                                </div>
                                                <div class="col-md-6">

                                                    <div class="form-group">
                                                        <label for="GLAB" class="form-label"> Longitud de la contraseña*</label>
                                                        <select class="custom-select custom-select-sm" name="longitudPassword">
                                                            <option value="" <?php echo ($data['fields']['longitudPassword'] == '' ) ? 'selected': ''; ?> >Elija longitud</option>
                                                            <option value="3" <?php echo ($data['fields']['longitudPassword'] == 3 ) ? 'selected': ''; ?> >3</option>
                                                            <option value="4" <?php echo ($data['fields']['longitudPassword'] == 4 ) ? 'selected': ''; ?> >4</option>
                                                            <option value="5" <?php echo ($data['fields']['longitudPassword'] == 5 ) ? 'selected': ''; ?> >5</option>
                                                            <option value="6" <?php echo ($data['fields']['longitudPassword'] == 6 ) ? 'selected': ''; ?> >6</option>
                                                        </select> 
                                                        <span class="error"><?php echo $data['fields']['longitudPassword_err'];?></span>
                                                    </div>

                                                    <div class="form-group">
                                                        <label for="GLAB" class="form-label"> Tipo de tiempos*</label>
                                                        <select class="custom-select custom-select-sm" name="tipoTiempos">
                                                            <option value="" <?php echo ($data['fields']['tipoTiempos'] == '' ) ? 'selected': ''; ?> >Elija un tiempo</option>
                                                            <option value="minuto" <?php echo ($data['fields']['tipoTiempos'] == 'minuto' ) ? 'selected': ''; ?> >Minuto</option>
                                                            <option value="hora" <?php echo ($data['fields']['tipoTiempos'] == 'hora' ) ? 'selected': ''; ?> >Hora</option>
                                                            <option value="dia" <?php echo ($data['fields']['tipoTiempos'] == 'dia' ) ? 'selected': ''; ?> >Día </option>
                                                            
                                                        </select> 
                                                        <span class="error"><?php echo $data['fields']['tipoTiempos_err'];?></span>
                                                    </div>

                                                    <div class="form-group">
                                                        <label for="GLAB" class="form-label"> Cantidad de usuarios a generar*</label>
                                                        <select class="custom-select custom-select-sm" name="cantidadUsers">
                                                            <option value="" <?php echo ($data['fields']['cantidadUsers'] == '' ) ? 'selected': ''; ?> >Elija cantidad</option>
                                                            <option value="5" <?php echo ($data['fields']['cantidadUsers'] == 5 ) ? 'selected': ''; ?> >5 Usuarios</option>
                                                            <option value="10" <?php echo ($data['fields']['cantidadUsers'] == 10 ) ? 'selected': ''; ?> >10 Usuarios</option>
                                                            <option value="15" <?php echo ($data['fields']['cantidadUsers'] == 15 ) ? 'selected': ''; ?> >15 Usuarios</option>
                                                            <option value="20" <?php echo ($data['fields']['cantidadUsers'] == 20 ) ? 'selected': ''; ?> >20 Usuarios</option>
                                                            <option value="25" <?php echo ($data['fields']['cantidadUsers'] == 25 ) ? 'selected': ''; ?> >25 Usuarios</option>
                                                            <option value="50" <?php echo ($data['fields']['cantidadUsers'] == 50 ) ? 'selected': ''; ?> >50 Usuarios</option>
                                                            <option value="100" <?php echo ($data['fields']['cantidadUsers'] == 100 ) ? 'selected': ''; ?> >100 Usuarios</option>
                                                            <option value="150" <?php echo ($data['fields']['cantidadUsers'] == 150 ) ? 'selected': ''; ?> >150 Usuarios</option>
                                                            <option value="200" <?php echo ($data['fields']['cantidadUsers'] == 200 ) ? 'selected': ''; ?> >200 Usuarios</option>
                                                            <option value="250" <?php echo ($data['fields']['cantidadUsers'] == 250 ) ? 'selected': ''; ?> >250 Usuarios</option>
                                                            <option value="300" <?php echo ($data['fields']['cantidadUsers'] == 300 ) ? 'selected': ''; ?> >300 Usuarios</option>
                                                            <option value="500" <?php echo ($data['fields']['cantidadUsers'] == 500 ) ? 'selected': ''; ?> >500 Usuarios</option>
                                                        </select> 
                                                        <span class="error"><?php echo $data['fields']['cantidadUsers_err'];?></span>
                                                    </div>

                                                </div>
                                                
                                            </div>
                                            <button class="btn btn-primary mr-auto"> <i class="fas fa-save"></i> Generar usuarios</button>    
                                        </form>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            <!-- footer -->
            <?php require APPROOT . '/views/shared/footer.php'; ?> 
            <!-- footer -->
            </div>
        </div>
        <?php require APPROOT . '/views/shared/scriptjs.php'; ?> 
        <script src="<?php echo URLROOT; ?>/js/usuariosHotspot/generador.js"></script> <!-- Contiene el script para aplicar validaciones -->
    </body>
</html>

File: /app\views\usuariosHotspot\index.php
<?php require APPROOT . '/views/shared/head.php'; ?>
    <body class="">
        <div class="wrapper ">
            <!-- sidebar -->
            <?php require APPROOT . '/views/shared/sidebar.php'; ?>  
            <!-- sidebar -->
            <div class="main-panel">
            <!-- Navbar -->
                <?php require APPROOT . '/views/shared/navbar.php'; ?> 
            <!-- End Navbar -->
            <div class="content">
                <div class="content">
                    <div class="container-fluid">
                        <div class="row">
                            <div class="col-md-12">
                                <div class="dosBotones">
                                    <a href="<?php echo URLROOT; ?>/usuarioshotspot/agregar" class="btn btn-info mr-auto" > <i class="fa fa-user"></i> Agregar usuario</a> 
                                    <a href="<?php echo URLROOT; ?>/usuarioshotspot/generador" class="btn btn-info" > <i class="fa fa-users"></i> Agregar usuarios</a> 
                                </div>
                                
                                <div class="card ">
                                    <div class="card-header card-header-success card-header-icon">
                                        <div class="card-icon">
                                            <i class="fa fa-users"></i>
                                        </div>
                                        <h4 class="card-title">Usuarios hotspot</h4>
                                        <hr>
                                        <div class="row">
                                            <div class="col-md-2">
                                                <button class="btn btn-primary" id="btnTickets" onclick="verTickets()"> <i class="fa fa-ticket-alt"></i> Ver tickets</button>
                                            </div>
                                            <div class="col-md-2">
                                                <div class="form-check">
                                                    <label class="form-check-label">
                                                        <input class="form-check-input selectAll" type="checkbox" value=""> Seleccionar todo
                                                        <span class="form-check-sign">
                                                        <span class="check"></span>
                                                        </span>
                                                    </label>
                                                </div>
                                            </div>
                                        </div>
                                        

                                    </div>
                                   
                                    <div class="card-body ">
                                        <div class="material-datatables">
                                            <table id="tablaUsers" class="table table-striped table-no-bordered table-hover" cellspacing="0" width="100%" style="width:100%">
                                                <thead>
                                                    <tr>
                                                    <th>No.</th>
                                                    <th>ID</th>
                                                    <th>Usuario</th>
                                                    <th>Contraseña</th>
                                                    <th>Tiempo</th>
                                                    <th>AnchoBandaLG</th>
                                                    <th>Información</th>
                                                    <th>TActividad</th>
                                                    <th class="disabled-sorting text-right">Acciones</th>
                                                    </tr>
                                                </thead>
                                                <tbody>
                                                    <?php 
                                                        if(count($data['users'])>0){ //si los datos son mayores a cero
                                                            $contador = 1;
                                                            foreach ($data['users'] as  $item) {
                                                                $id = "'".$item[".id"]."'";// pongo el id entre comillas
                                                                $username = "'".$item["name"]."'";
                                                                echo '<tr>';
                                                                echo '<td>'.$contador .'</td>';
                                                                echo '<td>'.$item[".id"] .'</td>';
                                                                echo '<td>'.$item["name"].'</td>';
                                                                echo '<td>'.$password = !empty($item['password']) ? $item["password"] : "".'</td>';
                                                                echo '<td>'.$limitUptime = !empty($item['limit-uptime']) ? $item["limit-uptime"] : "".'</td>';
                                                                echo '<td>'.$profile = !empty($item['profile']) ? $item["profile"] : "".'</td>';
                                                                echo '<td>'.$comment = !empty($item['comment']) ? $item["comment"] : "".'</td>';
                                                                echo '<td>'.$item["uptime"].'</td>';
                                                                echo '
                                                                    <td class="text-right">
                                                                        <button class="btn btn-sm btn-info" onclick="showUserHotspot('.$id.')"><i class="fas fa-edit"></i></button>
                                                                        <button class="btn btn-sm btn-warning" onclick="resetCounterUserHotspot('.$id.','.$username.')"><i class="fas fa-hourglass-start"></i></button>
                                                                        <button class="btn btn-sm btn-danger" onclick="deleteUserHotspot('.$id.','.$username.')"><i class="fas fa-trash"></i></button>
                                                                    </td>
                                                                ';
                                                                echo '</tr>';
                                                                $contador++;
                                                            }
                                                        }
                                                    ?>
                                                    
                                                </tbody>
                                            </table>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            <!-- modal modalShowUser-->
            <?php require APPROOT .'/views/usuariosHotspot/partials/modalShowUser.php'; ?> 
            <!-- modal modalShowUser-->
            <!-- footer -->
            <?php require APPROOT . '/views/shared/footer.php'; ?> 
            <!-- footer -->
            </div>
        </div>
        <?php require APPROOT . '/views/shared/scriptjs.php'; ?> 
        <script src="<?php echo URLROOT; ?>/js/usuariosHotspot/index.js"></script> <!-- Contiene el script para aplicar datatables -->
    </body>
</html> 

File: /app\views\usuariosHotspot\partials\modalShowUser.php

<div class="modal fade" id="showUserHotspot" tabindex="-1" role="dialog" aria-labelledby="showUserHotspotLabel" aria-hidden="true">
  <div class="modal-dialog" role="document">
    <div class="modal-content">
      <div class="modal-header">
        <h5 class="modal-title" id="showUserHotspotLabel">Actualizar información del usuario hotspot</h5>
        <button type="button" class="close" data-dismiss="modal" aria-label="Close">
          <span aria-hidden="true">&times;</span>
        </button>
      </div>
      <div class="modal-body">
      <form>
        <div class="card-body ">
            <div class="form-group d-none">
              <input type="text" class="form-control " id="tokenCSRF" value="<?php echo $_SESSION["tokencsrf"]; ?>">
              <input type="text" class="form-control " id="idUserHotspot">
            </div>
            
            <div class="form-group">
              <label for="username" class="form-label"> Nombre de usuario *</label> 
              <input type="text" class="form-control " id="username" required="true" aria-required="true" aria-invalid="false" onkeyup="activeButton()">
              <label id="username-error" class="error" for="username"></label>
            </div>
            <div class="form-group">
               <label for="password" class="form-label"> Contraseña *</label> 
              <input type="Contraseña" class="form-control " id="password" required="true" aria-required="true" aria-invalid="false" onkeyup="activeButton()">
              <label id="password-error" class="error" for="password"></label>
            </div> 

            <div class="form-group">
              <label for="GLAB" class="form-label"> Perfiles*</label>
              <select class="custom-select custom-select-sm" id="grupoLimiteAnchosBanda" onchange="activeButton()">
                <option value=''>Elija</option>
                <?php 
                  foreach ($data["anchosBanda"] as $item) {
                    $dash = !empty($item['rate-limit']) ? '--' : ''; //dash es un guion
                    echo '<option value="'.$item["name"].'">'.$item["name"].$dash.$item["rate-limit"].'</option>';
                  }
                ?>
              </select> 
            </div> 

            <div class="form-group">
              <label for="información" class="form-label"> Información *</label>
              <textarea class="form-control" id="informacion" rows="2" onkeyup="activeButton()" required="true" aria-required="true" aria-invalid="false" ></textarea>
            </div> 
                        
          </div>          
      </form>
      </div>
      <div class="modal-footer">
        <button type="button" class="btn btn-warning mr-auto" data-dismiss="modal"> <i class="fas fa-window-close"></i> Cerrar</button>
        <button type="button" class="btn btn-primary" id="btnSaveUserHotspot" onclick="updateUserHotspot()" disabled> <i class="fas fa-save"></i> Guardar cambios</button>
      </div>
    </div>
  </div>
</div>

File: /app\views\usuariosHotspot\verVouchers.php
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN"      "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
 <html xmlns="http://www.w3.org/1999/xhtml"> 

 <head> <meta charset="utf-8"> 
     <title>Vouchers</title> 
    <link rel="icon" type="image/png" href="<?php echo URLROOT; ?>/img/favicon.png">
     
 	<style> @media print {   .noprint { 
 	                                      display: none;  
 	                                    }  
 	                         .pagebreak {  page-break-after: always;  
 	                                   }
 	                      }
    </style> 
</head> 
    <body> 
        <input type="hidden" id="encabezado" value="<?php echo ENCABEZADO;?>">
        <input type="hidden" id="pie" value="<?php  echo PIE;?>">
        
        <div id="vouchers">

        </div>
        <script src="<?php echo URLROOT; ?>/js/jquery.min.js"></script>
        <script src="<?php echo URLROOT; ?>/js/usuariosHotspot/verVouchers.js"></script> <!-- Contiene el script para pintar los tickets -->    
    </body>
</html>
<p class="noprint" style="font-size: 10px">
    <a href="<?php echo URLROOT; ?>/usuarioshotspot" class="btn btn-warning mr-auto" > <i class="fas fa-arrow-left"></i> Volver</a>
</p>
<p class="pagebreak">&nbsp;</p>

File: /app\views\usuariosHotspot\vouchers.php
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN"      "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
 <html xmlns="http://www.w3.org/1999/xhtml"> 

 <head> <meta charset="utf-8"> 
     <title>Vouchers</title> 
    <link rel="icon" type="image/png" href="<?php echo URLROOT; ?>/img/favicon.png">
     
 	<style> @media print {   .noprint { 
 	                                      display: none;  
 	                                    }  
 	                         .pagebreak {  page-break-after: always;  
 	                                   }
 	                      }
    </style> 
</head> 
    <body> 
<?php
    $contador = 1;
    
    foreach ($data as $item) {
        echo '
                <table style="display: inline-block; width: 250px; border: 1px solid #121DAE; line-height: 110%; font-family: arial; font-size: 12px; margin: 1px;">     
                <tbody>         
                    <tr>             
                        <td style="text-align: center; color: #2F38F4; font-size: 13px; border-bottom: 1px #ccc solid;"><b>'.ENCABEZADO.'</b></td>        
                    </tr>          
                    <tr>              
                        <td>                   
                            <table style=" text-align: center; width: 240px; background-color: #fff; line-height: 110%; font-size: 11px;">              
                                <tbody>                
                                    <tr style="background-color: #eee;">                               
                                        <td style="background-color: #fff; width: 33%"><b>Número</b></td>                               
                                        <td style="width: 33%"><b>Paquete</b></td>                                 
                                        <td style="width: 33%">Datos</td>                            
                                    </tr>                           
                                    <tr>                              
                                        <td ><b>'.$contador.'</b></td>                              
                                        <td><b> '.$item->profile.'</b></td>                              
                                        <td>Ilimitados</td>                   
                                    </tr>                       
                                </tbody>                  
                            </table>           
                        </td>             
                    </tr>             
                    <tr>       
                        <td>                  
                                <table style=" text-align: center; width: 240px; background-color: #fff; line-height: 110%; font-size: 11px;">               
                                    <tbody>                         
                                        <tr style="background-color: #eee;">                             
                                            <td style="width: 33%">Tiempo</td>                             
                                            <td style="width: 33%"></td>                             
                                            <td style="width: 33%">Precio</td>                         
                                        </tr>                         
                                        <tr>                        
                                            <td> '.$item->limitUptime.'</td>                             
                                            <td></td>                             
                                            <td>$'.$item->comment.'</td>            </tr>                     
                                </tbody>                   
                            </table>                
                        </td>              
                    </tr>              
                    <tr>                 
                        <td>                      
                            <table style=" text-align: center; width: 240px; background-color: #fff; line-height: 110%; font-size: 12px; border-top: 1px solid #ccc;">    
                                <tbody>                             
                                    <tr style="color: #1A16B8; font-size: 11px;">                       
                                        <td style="width: 50%">Usuario</td>                          
                                        <td>Contraseña</td>                   
                                    </tr>                         
                                    <tr style="background-color: #fff;">                                
                                        <td style="color: #000000; border: 1px #ccc solid;">'.$item->name.'</td>                               
                                        <td style="color: #000000; border: 1px #ccc solid;">'.$item->password.'</td>                                
                                    </tr>                          
                                </tbody>                      
                            </table>                 
                        </td>              
                    </tr>              
                    <tr>                   
                        <td style="text-align: center; font-size:11px;">'.PIE.'</td>             
                        </tr>      
                    </tbody>     
            </table>
             ';

             $contador++;
    }  
?>
    </body>
</html>
<p class="noprint" style="font-size: 10px">
    <a href="<?php echo URLROOT; ?>/usuarioshotspot" class="btn btn-warning mr-auto" > <i class="fas fa-arrow-left"></i> Volver</a>
</p>
<p class="pagebreak">&nbsp;</p>

File: /app\views\usuariosMikrotik\agregar.php
<?php require APPROOT . '/views/shared/head.php'; ?>
    <body class="">
        <div class="wrapper ">
            <!-- sidebar -->
            <?php require APPROOT . '/views/shared/sidebar.php'; ?> 
            <!-- sidebar -->
            <div class="main-panel">
            <!-- Navbar -->
                <?php require APPROOT . '/views/shared/navbar.php'; ?> 
            <!-- End Navbar -->
            <div class="content">
                <div class="content">
                    <div class="container-fluid">
                        <div class="row">
                        <div class="col-md-12">
                            <a href="<?php echo URLROOT; ?>/usuariosmikrotik" class="btn btn-warning mr-auto" > <i class="fas fa-arrow-left"></i> Volver</a>
                            
                            <?php flashMensaje('messageApi'); ?>

                            <div class="card ">
                            <div class="card-header card-header-success card-header-icon">
                                <div class="card-icon">
                                <i class="fa fa-user"></i>
                                </div>
                                <h4 class="card-title">Agregar usuario mikrotik</h4>
                            </div>
                            <div class="card-body ">
                                <div class="row">
                                    <div class="col-md-6">
                                        <form action="<?php echo URLROOT.'/usuariosmikrotik/agregar'; ?>" method="post">
                                        
                                            <div class="form-group d-none">
                                                <input type="text" class="form-control" value="<?php echo $_SESSION["tokencsrf"]; ?>">
                                            </div>
                                            
                                            <div class="form-group">
                                                <label for="name" class="form-label"> Nombre de usuario *</label> 
                                                <input type="text" class="form-control"  aria-required="true" aria-invalid="false" name="name" value="<?php echo $data['fields']['name'];?>">
                                                <span class="error" for="name"><?php echo $data['fields']['name_err'];?></span>
                                            </div>

                                            <div class="form-group">
                                                <label for="groupUser" class="form-label"> Grupo </label>
                                                <select class="custom-select custom-select-sm" name="groupUser">
                                                <?php $selected = ($data['fields']['groupUser'] == '') ? 'selected': '';?>
                                                    <option value='' <?php echo $selected; ?> >Elija grupo</option>
                                                    <?php 
                                                        foreach ($data["groupUsers"] as $item) {
                                                            $selected = ($data['fields']['groupUser'] == $item["name"]) ? 'selected': '';
                                                            echo '<option value="'.$item["name"].'" '.$selected.'>'.$item["name"].'</option>';
                                                        }
                                                    ?>
                                                </select> 
                                                <span class="error" for="groupUser"><?php echo $data['fields']['groupUser_err'];?></span>
                                            </div>


                                            <div class="form-group">
                                                <label for="password" class="form-label"> Contraseña</label> 
                                                <input type="password" class="form-control" aria-required="true" name="password" aria-invalid="false" value="<?php echo $data['fields']['password'];?>">
                                                <span class="error" for="password"><?php echo $data['fields']['password_err'];?></span>
                                            </div>
                                            
                                            <div class="form-group">
                                                <label for="informacion" class="form-label"> Información *</label>
                                                <textarea class="form-control" name="informacion" rows="2" aria-required="true" aria-invalid="false" > <?php echo $data['fields']['informacion'];?></textarea>
                                                <span class="error"><?php echo $data['fields']['informacion_err'];?></span>

                                            </div>
                                            <button class="btn btn-primary"> <i class="fas fa-save"></i> Guardar </button>

                                            
                                        </form>
                                    </div>
                                </div>
                            </div>
                            </div>
                        </div>
                        </div>
                    </div>
                </div>
            </div>
            <!-- footer -->
            <?php require APPROOT . '/views/shared/footer.php'; ?> 
            <!-- footer -->
            </div>
        </div>
        <?php require APPROOT . '/views/shared/scriptjs.php'; ?> 
    </body>
</html>

File: /app\views\usuariosMikrotik\datosTicket.php
<?php require APPROOT . '/views/shared/head.php'; ?>
    <body class="">
        <div class="wrapper ">
            <!-- sidebar -->
            <?php require APPROOT . '/views/shared/sidebar.php'; ?> 
            <!-- sidebar -->
            <div class="main-panel">
            <!-- Navbar -->
                <?php require APPROOT . '/views/shared/navbar.php'; ?> 
            <!-- End Navbar -->
            <div class="content">
                <div class="content">
                    <div class="container-fluid">
                        <div class="row">
                        <div class="col-md-12">
                            <a href="<?php echo URLROOT; ?>/usuariosmikrotik" class="btn btn-warning mr-auto" > <i class="fas fa-arrow-left"></i> Volver</a>
                            
                            <?php flashMensaje('datosTicket'); ?>

                            <div class="card ">
                            <div class="card-header card-header-success card-header-icon">
                                <div class="card-icon">
                                <i class="fa fa-lock"></i>
                                </div>
                                <h4 class="card-title">Algunos datos a mostrar cuando se generan los tickets</h4>
                                
                            </div>
                            <div class="card-body ">
                                <div class="row">
                                    <div class="col-md-6">
                                
                                        <form action="<?php echo URLROOT.'/usuariosmikrotik/datosticket'; ?>" method="post">
                                        
                                            <div class="form-group d-none">
                                                <input type="text" class="form-control" value="<?php echo $_SESSION["tokencsrf"]; ?>">
                                            </div>
                                            
                                            <div class="form-group">
                                                <label for="encabezado" class="form-label"> Encabezado para los tickets (max 25)</label> 
                                                <input type="text" minlength="5" maxlength="25" class="form-control"  aria-required="true" aria-invalid="false" name="encabezado" value="<?php echo $data['fields']['encabezado'];?>">
                                                <span class="error" for="encabezado"><?php echo $data['fields']['encabezado_err'];?></span>
                                            </div>

                                            <div class="form-group">
                                                <label for="pie" class="form-label"> Pie de página para el ticket (max 40)</label> 
                                                <input type="text"  minlength="5" maxlength="40" class="form-control"  aria-required="true" aria-invalid="false" name="pie" value="<?php echo $data['fields']['pie'];?>">
                                                <span class="error" for="pie"><?php echo $data['fields']['pie_err'];?></span>
                                            </div>
                                            
                                            <button class="btn btn-primary"> <i class="fas fa-save"></i> Guardar </button>

                                        </form>
                                    </div>
                                </div>
                            </div>
                            </div>
                        </div>
                        </div>
                    </div>
                </div>
            </div>
            <!-- footer -->
            <?php require APPROOT . '/views/shared/footer.php'; ?> 
            <!-- footer -->
            </div>
        </div>
        <?php require APPROOT . '/views/shared/scriptjs.php'; ?> 
    </body>
</html>



File: /app\views\usuariosMikrotik\editarIdentidad.php
<?php require APPROOT . '/views/shared/head.php'; ?>
    <body class="">
        <div class="wrapper ">
            <!-- sidebar -->
            <?php require APPROOT . '/views/shared/sidebar.php'; ?> 
            <!-- sidebar -->
            <div class="main-panel">
            <!-- Navbar -->
                <?php require APPROOT . '/views/shared/navbar.php'; ?> 
            <!-- End Navbar -->
            <div class="content">
                <div class="content">
                    <div class="container-fluid">
                        <div class="row">
                            <div class="col-md-12">
                                <a href="<?php echo URLROOT; ?>/usuariosmikrotik" class="btn btn-warning mr-auto" > <i class="fas fa-arrow-left"></i> Volver</a>
                                
                                <?php flashMensaje('messageApi'); ?>


                                <div class="card ">
                                    <div class="card-header card-header-success card-header-icon">
                                        <div class="card-icon">
                                        <i class="fa fa-info"></i>
                                        </div>
                                        <h4 class="card-title">Actualizar identidad del Mikrotik</h4>
                                        
                                    </div>
                                    <div class="card-body ">
                                   

                                        <div class="row">
                                            <div class="col-md-6">
                                                <form action="<?php echo URLROOT.'/usuariosmikrotik/editarIdentidad'; ?>" method="post">
                                                    <div class="form-group d-none">
                                                        <input type="text" class="form-control" value="<?php echo $_SESSION["tokencsrf"]; ?>">
                                                    </div>
                                                    
                                                    <div class="form-group">
                                                        <label for="identidad" class="form-label"> Identidad </label> 
                                                        <input type="text" class="form-control"  aria-required="true" aria-invalid="false" name="identidad" value="<?php echo $data['fields']['identidad'];?>">
                                                        <span class="error" for="identidad"><?php echo $data['fields']['identidad_err'];?></span>
                                                    </div>
                                                    <button class="btn btn-primary"> <i class="fas fa-save"></i> Guardar </button>
                                                </form>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            <!-- footer -->
            <?php require APPROOT . '/views/shared/footer.php'; ?> 
            <!-- footer -->
            </div>
        </div>
        <?php require APPROOT . '/views/shared/scriptjs.php'; ?> 
    </body>
</html>

File: /app\views\usuariosMikrotik\editarPassword.php
<?php require APPROOT . '/views/shared/head.php'; ?>
    <body class="">
        <div class="wrapper ">
            <!-- sidebar -->
            <?php require APPROOT . '/views/shared/sidebar.php'; ?> 
            <!-- sidebar -->
            <div class="main-panel">
            <!-- Navbar -->
                <?php require APPROOT . '/views/shared/navbar.php'; ?> 
            <!-- End Navbar -->
            <div class="content">
                <div class="content">
                    <div class="container-fluid">
                        <div class="row">
                        <div class="col-md-12">
                            <a href="<?php echo URLROOT; ?>/usuariosmikrotik" class="btn btn-warning mr-auto" > <i class="fas fa-arrow-left"></i> Volver</a>
                            
                            <?php flashMensaje('messageApi'); ?>

                            <div class="card ">
                            <div class="card-header card-header-success card-header-icon">
                                <div class="card-icon">
                                <i class="fa fa-lock"></i>
                                </div>
                                <h4 class="card-title">Actualizar contraseña del Mikrotik</h4>
                                
                            </div>
                            <div class="card-body ">
                                <div class="row">
                                    <div class="col-md-6">
                                
                                        <form action="<?php echo URLROOT.'/usuariosmikrotik/editarpassword'; ?>" method="post">
                                        
                                            <div class="form-group d-none">
                                                <input type="text" class="form-control" value="<?php echo $_SESSION["tokencsrf"]; ?>">
                                            </div>
                                            
                                            <div class="form-group">
                                                <label for="oldPassword" class="form-label"> Contraseña anterior</label> 
                                                <input type="password" class="form-control"  aria-required="true" aria-invalid="false" name="oldPassword" value="<?php echo $data['fields']['oldPassword'];?>">
                                                <span class="error" for="oldPassword"><?php echo $data['fields']['oldPassword_err'];?></span>
                                            </div>

                                            <div class="form-group">
                                                <label for="newPassword" class="form-label"> Nueva contraseña  *</label> 
                                                <input type="password" class="form-control"  aria-required="true" aria-invalid="false" name="newPassword" value="<?php echo $data['fields']['newPassword'];?>">
                                                <span class="error" for="newPassword"><?php echo $data['fields']['newPassword_err'];?></span>
                                            </div>
                                            
                                            <button class="btn btn-primary"> <i class="fas fa-save"></i> Guardar </button>

                                        </form>
                                    </div>
                                </div>
                            </div>
                            </div>
                        </div>
                        </div>
                    </div>
                </div>
            </div>
            <!-- footer -->
            <?php require APPROOT . '/views/shared/footer.php'; ?> 
            <!-- footer -->
            </div>
        </div>
        <?php require APPROOT . '/views/shared/scriptjs.php'; ?> 
    </body>
</html>

File: /app\views\usuariosMikrotik\editarPerfilMikrotik.php
<?php require APPROOT . '/views/shared/head.php'; ?>
    <body class="">
        <div class="wrapper ">
            <!-- sidebar -->
            <?php require APPROOT . '/views/shared/sidebar.php'; ?> 
            <!-- sidebar -->
            <div class="main-panel">
            <!-- Navbar -->
                <?php require APPROOT . '/views/shared/navbar.php'; ?> 
            <!-- End Navbar -->
            <div class="content">
                <div class="content">
                    <div class="container-fluid">
                        <div class="row">
                        <div class="col-md-12">
                            <a href="<?php echo URLROOT; ?>/usuariosmikrotik" class="btn btn-warning mr-auto" > <i class="fas fa-arrow-left"></i> Volver</a>
                            
                            <?php flashMensaje('messageApi'); ?>

                            <div class="card ">
                            <div class="card-header card-header-success card-header-icon">
                                <div class="card-icon">
                                <i class="fa fa-user"></i>
                                </div>
                                <h4 class="card-title">Perfil del Mikrotik</h4>
                                
                            </div>
                            <div class="card-body ">
                                <div class="row">
                                    <div class="col-md-6">
                                
                                        <form action="<?php echo URLROOT.'/usuariosmikrotik/editarperfilmikrotik'; ?>" method="post">
                                        
                                            <div class="form-group d-none">
                                                <input type="text" class="form-control" value="<?php echo $_SESSION["tokencsrf"]; ?>">
                                                <input type="text" class="form-control" name="id" value="<?php echo $data['fields']['id'];?>">

                                            </div>
                                            
                                            <div class="form-group">
                                                <label for="name" class="form-label"> Nombre de usuario *</label> 
                                                <input type="text" class="form-control"  aria-required="true" aria-invalid="false" name="name" value="<?php echo $data['fields']['name'];?>">
                                                <span class="error" for="name"><?php echo $data['fields']['name_err'];?></span>
                                            </div>

                                            <div class="form-group">
                                                <label for="groupUser" class="form-label"> Grupo </label>
                                                <select class="custom-select custom-select-sm" name="groupUser">
                                                <?php $selected = ($data['fields']['groupUser'] == '') ? 'selected': '';?>
                                                    <option value='' <?php echo $selected; ?> >Elija grupo</option>
                                                    <?php 
                                                        foreach ($data["groupUsers"] as $item) {
                                                            $selected = ($data['fields']['groupUser'] == $item["name"]) ? 'selected': '';
                                                            echo '<option value="'.$item["name"].'" '.$selected.'>'.$item["name"].'</option>';
                                                        }
                                                    ?>
                                                </select> 
                                                <span class="error" for="groupUser"><?php echo $data['fields']['groupUser_err'];?></span>
                                            </div>

                                            
                                            <div class="form-group">
                                                <label for="informacion" class="form-label"> Información *</label>
                                                <textarea class="form-control" name="informacion" rows="2" aria-required="true" aria-invalid="false" > <?php echo $data['fields']['informacion'];?></textarea>
                                                <span class="error"><?php echo $data['fields']['informacion_err'];?></span>

                                            </div>
                                            <button class="btn btn-primary"> <i class="fas fa-save"></i> Guardar </button>

                                            
                                        </form>
                                    </div>
                                </div>
                            </div>
                            </div>
                        </div>
                        </div>
                    </div>
                </div>
            </div>
            <!-- footer -->
            <?php require APPROOT . '/views/shared/footer.php'; ?> 
            <!-- footer -->
            </div>
        </div>
        <?php require APPROOT . '/views/shared/scriptjs.php'; ?> 
    </body>
</html>

File: /app\views\usuariosMikrotik\index.php
<?php require APPROOT . '/views/shared/head.php'; ?>
    <body class="">
        <div class="wrapper ">
            <!-- sidebar -->
            <?php require APPROOT . '/views/shared/sidebar.php'; ?>  
            <!-- sidebar -->
            <div class="main-panel">
            <!-- Navbar -->
                <?php require APPROOT . '/views/shared/navbar.php'; ?> 
            <!-- End Navbar -->
            <div class="content">
                <div class="content">
                    <div class="container-fluid">
                        <div class="row">
                            <div class="col-md-12">
                                
                                <a href="<?php echo URLROOT; ?>/usuariosmikrotik/agregar" class="btn btn-info mr-auto" > <i class="fa fa-user"></i> Agregar usuario MK</a> 
                                    
                                <input type="hidden" class="form-control " id="tokenCSRF" value="<?php echo $_SESSION["tokencsrf"]; ?>">
                                
                                <div class="card ">
                                    <div class="card-header card-header-success card-header-icon">
                                        <div class="card-icon">
                                            <i class="fa fa-users"></i>
                                        </div>
                                        <h4 class="card-title">Usuarios del mikrotik</h4>
                                    </div>
                                   
                                    <div class="card-body ">
                                        <div class="material-datatables">
                                            <table id="usersMikrotik" class="table table-striped table-no-bordered table-hover" cellspacing="0" width="100%" style="width:100%">
                                                <thead>
                                                    <tr>
                                                    <th>No.</th>
                                                    <th>Nombre</th>
                                                    <th>Grupo</th>
                                                    <th>Información</th>
                                                    <th class="disabled-sorting text-right">Acciones</th>
                                                    </tr>
                                                </thead>
                                                <tbody>
                                                    <?php 
                                                        if(count($data['users'] )>0){ //si los datos son mayores a cero
                                                            $contador = 1;
                                                            foreach ( $data['users'] as  $item) {
                                                                $id = "'".$item[".id"]."'";// pongo el id entre comillas
                                                                $name = "'".$item["name"]."'";
                                                                echo '<tr>';
                                                                echo '<td>'.$contador .'</td>';
                                                                echo '<td>'.$item["name"].'</td>';
                                                                echo '<td>'.$item["group"] .'</td>';
                                                                echo '<td>'.$password = !empty($item['comment']) ? $item["comment"] : "".'</td>';
                                                                echo '
                                                                    <td class="text-right">
                                                                        <button class="btn btn-sm btn-danger" onclick="deleteUserMikrotik('.$id.','.$name.')"><i class="fas fa-trash"></i></button>
                                                                    </td>
                                                                ';
                                                                echo '</tr>';
                                                                $contador++;
                                                            }
                                                        }
                                                    ?>
                                                    
                                                </tbody>
                                            </table>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            
            <!-- footer -->
            <?php require APPROOT . '/views/shared/footer.php'; ?> 
            <!-- footer -->
            </div>
        </div>
        <?php require APPROOT . '/views/shared/scriptjs.php'; ?> 
        <script src="<?php echo URLROOT; ?>/js/usuariosMikrotik/index.js"></script> <!-- Contiene el script para aplicar datatables -->
    </body>
</html> 

File: /app\views\usuariosMikrotik\reiniciarMikrotik.php
<?php require APPROOT . '/views/shared/head.php'; ?>
    <body class="">
        <div class="wrapper ">
            <!-- sidebar -->
            <?php require APPROOT . '/views/shared/sidebar.php'; ?> 
            <!-- sidebar -->
            <div class="main-panel">
            <!-- Navbar -->
                <?php require APPROOT . '/views/shared/navbar.php'; ?> 
            <!-- End Navbar -->
            <div class="content">
                <div class="content">
                    <div class="container-fluid">
                        <div class="row">
                        <div class="col-md-12">
                            <div class="card ">
                            <div class="card-header card-header-danger card-header-icon">
                                <div class="card-icon">
                                    <i class="fas fa-power-off"></i>
                                </div>
                                <h4 class="card-title">Reiniciar el equipo</h4>
                            </div>
                            <div class="card-body ">
                                <div class="row">
                                    <input type="hidden" class="form-control " id="tokenCSRF" value="<?php echo $_SESSION["tokencsrf"]; ?>">
                                    <input type="hidden" class="form-control " id="mikrotik" value="<?php echo $_SESSION['usuario']; ?>">
                                    <input type="hidden" class="form-control " id="urlRoot" value="<?php echo URLROOT; ?>">
                                    <button class="btn btn-danger mt-5 btn-block" onclick="reboot()"> <i class="fas fa-power-off"></i> Reiniciar</button>
                                </div>
                            </div>
                            </div>
                        </div>
                        </div>
                    </div>
                </div>
            </div>
            <!-- footer -->
            <?php require APPROOT . '/views/shared/footer.php'; ?> 
            <!-- footer -->
            </div>
        </div>
        <?php require APPROOT . '/views/shared/scriptjs.php'; ?> 
        <script src="<?php echo URLROOT; ?>/js/usuariosMikrotik/reiniciarMikrotik.js"></script> <!-- Contiene el script para aplicar datatables -->

    </body>
</html>

File: /public\.htaccess
<IfModule mod_rewrite.c>
    Options -Multiviews
    RewriteEngine On
    RewriteBase /base/public/
    RewriteCond %{REQUEST_FILENAME} !-d
    RewriteCond %{REQUEST_FILENAME} !-f
    RewriteRule ^(.+)$ index.php?url=$1 [QSA,L]
</IfModule>

File: /public\css\material-dashboard.minf066.css
/*!

 * Material Dashboard PRO - v2.1.0

 * Product Page: https://www.creative-tim.com/product/material-dashboard-pro
 * Copyright 2019 Creative Tim (https://www.creative-tim.com)

 * Coded by Creative Tim


 * The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

 */


 .card{font-size:.875rem}@media print{*,:after,:before{text-shadow:none!important;box-shadow:none!important}a:not(.btn){text-decoration:underline}abbr[title]:after{content:" (" attr(title) ")"}pre{white-space:pre-wrap!important}blockquote,pre{border:1px solid #999;page-break-inside:avoid}thead{display:table-header-group}img,tr{page-break-inside:avoid}h2,h3,p{orphans:3;widows:3}h2,h3{page-break-after:avoid}@page{size:a3}.container,body{min-width:992px!important}.navbar{display:none}.badge{border:1px solid #000}.table{border-collapse:collapse!important}.table td,.table th{background-color:#fff!important}.table-bordered td,.table-bordered th{border:1px solid #ddd!important}}*,:after,:before{box-sizing:border-box}html{font-family:sans-serif;line-height:1.15;-webkit-text-size-adjust:100%;-ms-text-size-adjust:100%;-ms-overflow-style:scrollbar;-webkit-tap-highlight-color:rgba(0,0,0,0)}@-ms-viewport{width:device-width}article,aside,dialog,figcaption,figure,footer,header,hgroup,main,nav,section{display:block}body{margin:0;font-family:Roboto,Helvetica,Arial,sans-serif;font-size:1rem;font-weight:400;line-height:1.5;color:#212529;text-align:left;background-color:#fafafa}[tabindex="-1"]:focus{outline:0!important}hr{box-sizing:content-box;height:0;overflow:visible}h1,h2,h3,h4,h5,h6{margin-top:0;margin-bottom:.5rem}p{margin-top:0;margin-bottom:1rem}abbr[data-original-title],abbr[title]{text-decoration:underline;text-decoration:underline dotted;cursor:help;border-bottom:0}address{font-style:normal;line-height:inherit}address,dl,ol,ul{margin-bottom:1rem}dl,ol,ul{margin-top:0}ol ol,ol ul,ul ol,ul ul{margin-bottom:0}dt{font-weight:500}dd{margin-bottom:.5rem;margin-left:0}blockquote{margin:0 0 1rem}dfn{font-style:italic}b,strong{font-weight:bolder}small{font-size:80%}sub,sup{position:relative;font-size:75%;line-height:0;vertical-align:baseline}sub{bottom:-.25em}sup{top:-.5em}a{text-decoration:none;background-color:transparent;-webkit-text-decoration-skip:objects}a:hover{color:#0a6ebd;text-decoration:underline}a:not([href]):not([tabindex]),a:not([href]):not([tabindex]):focus,a:not([href]):not([tabindex]):hover{color:inherit;text-decoration:none}a:not([href]):not([tabindex]):focus{outline:0}code,kbd,pre,samp{font-family:monospace,monospace;font-size:1em}pre{margin-top:0;margin-bottom:1rem;overflow:auto;-ms-overflow-style:scrollbar}figure{margin:0 0 1rem}img{vertical-align:middle;border-style:none}svg:not(:root){overflow:hidden}table{border-collapse:collapse}caption{padding-top:.75rem;padding-bottom:.75rem;color:#6c757d;text-align:left;caption-side:bottom}th{text-align:inherit}label{display:inline-block;margin-bottom:.5rem}button{border-radius:0}button:focus{outline:1px dotted;outline:5px auto -webkit-focus-ring-color}button,input,optgroup,select,textarea{margin:0;font-family:inherit;font-size:inherit;line-height:inherit}button,input{overflow:visible}button,select{text-transform:none}[type=reset],[type=submit],button,html [type=button]{-webkit-appearance:button}[type=button]::-moz-focus-inner,[type=reset]::-moz-focus-inner,[type=submit]::-moz-focus-inner,button::-moz-focus-inner{padding:0;border-style:none}input[type=checkbox],input[type=radio]{box-sizing:border-box;padding:0}input[type=date],input[type=datetime-local],input[type=month],input[type=time]{-webkit-appearance:listbox}textarea{overflow:auto;resize:vertical}fieldset{min-width:0;padding:0;margin:0;border:0}legend{display:block;width:100%;max-width:100%;padding:0;margin-bottom:.5rem;font-size:1.5rem;line-height:inherit;color:inherit;white-space:normal}progress{vertical-align:baseline}[type=number]::-webkit-inner-spin-button,[type=number]::-webkit-outer-spin-button{height:auto}[type=search]{outline-offset:-2px;-webkit-appearance:none}[type=search]::-webkit-search-cancel-button,[type=search]::-webkit-search-decoration{-webkit-appearance:none}::-webkit-file-upload-button{font:inherit;-webkit-appearance:button}output{display:inline-block}summary{display:list-item;cursor:pointer}template{display:none}[hidden]{display:none!important}.h1,.h2,.h3,.h4,.h5,.h6,h1,h2,h3,h4,h5,h6{margin-bottom:.5rem;font-family:inherit;font-weight:400;line-height:1.2;color:inherit}.h1,h1{font-size:2.5rem}.h2,h2{font-size:2rem}.h3,h3{font-size:1.75rem}.h4,h4{font-size:1.5rem}.h5,h5{font-size:1.25rem}.h6,h6{font-size:1rem}.lead{font-size:1.25rem;font-weight:300}.display-1{font-size:7rem}.display-1,.display-2{font-weight:300;line-height:1.2}.display-2{font-size:3.5rem}.display-3{font-size:2.8125rem}.display-3,.display-4{font-weight:300;line-height:1.2}.display-4{font-size:2.125rem}hr{margin-top:1rem;margin-bottom:1rem;border:0;border-top:1px solid rgba(0,0,0,.1)}.small,small{font-size:80%;font-weight:400}.mark,mark{padding:.2em;background-color:#fcf8e3}.list-inline,.list-unstyled{padding-left:0;list-style:none}.list-inline-item{display:inline-block}.list-inline-item:not(:last-child){margin-right:.5rem}.initialism{font-size:90%;text-transform:uppercase}.blockquote{margin-bottom:1rem;font-size:1.25rem}.blockquote-footer{display:block;font-size:80%;color:#6c757d}.blockquote-footer:before{content:"\2014 \00A0"}.img-fluid,.img-thumbnail{max-width:100%;height:auto}.img-thumbnail{padding:.25rem;background-color:#fafafa;border:1px solid #dee2e6;border-radius:.25rem;box-shadow:0 1px 2px rgba(0,0,0,.075)}.figure{display:inline-block}.figure-img{margin-bottom:.5rem;line-height:1}.figure-caption{font-size:90%;color:#6c757d}code,kbd,pre,samp{font-family:SFMono-Regular,Menlo,Monaco,Consolas,Liberation Mono,Courier New,monospace}code{font-size:87.5%;color:#e91e63;word-break:break-word}a>code{color:inherit}kbd{padding:.2rem .4rem;font-size:87.5%;color:#fff;background-color:#212529;border-radius:.2rem;box-shadow:inset 0 -.1rem 0 rgba(0,0,0,.25)}kbd kbd{padding:0;font-size:100%;font-weight:500;box-shadow:none}pre{display:block;font-size:87.5%;color:#212529}pre code{font-size:inherit;color:inherit;word-break:normal}.pre-scrollable{max-height:340px;overflow-y:scroll}.container{width:100%;padding-right:15px;padding-left:15px;margin-right:auto;margin-left:auto}@media (min-width:576px){.container{max-width:540px}}@media (min-width:768px){.container{max-width:720px}}@media (min-width:992px){.container{max-width:960px}}@media (min-width:1200px){.container{max-width:1140px}}.container-fluid{width:100%;padding-right:15px;padding-left:15px;margin-right:auto;margin-left:auto}.row{display:flex;flex-wrap:wrap;margin-right:-15px;margin-left:-15px}.no-gutters{margin-right:0;margin-left:0}.no-gutters>.col,.no-gutters>[class*=col-]{padding-right:0;padding-left:0}.col,.col-1,.col-2,.col-3,.col-4,.col-5,.col-6,.col-7,.col-8,.col-9,.col-10,.col-11,.col-12,.col-auto,.col-lg,.col-lg-1,.col-lg-2,.col-lg-3,.col-lg-4,.col-lg-5,.col-lg-6,.col-lg-7,.col-lg-8,.col-lg-9,.col-lg-10,.col-lg-11,.col-lg-12,.col-lg-auto,.col-md,.col-md-1,.col-md-2,.col-md-3,.col-md-4,.col-md-5,.col-md-6,.col-md-7,.col-md-8,.col-md-9,.col-md-10,.col-md-11,.col-md-12,.col-md-auto,.col-sm,.col-sm-1,.col-sm-2,.col-sm-3,.col-sm-4,.col-sm-5,.col-sm-6,.col-sm-7,.col-sm-8,.col-sm-9,.col-sm-10,.col-sm-11,.col-sm-12,.col-sm-auto,.col-xl,.col-xl-1,.col-xl-2,.col-xl-3,.col-xl-4,.col-xl-5,.col-xl-6,.col-xl-7,.col-xl-8,.col-xl-9,.col-xl-10,.col-xl-11,.col-xl-12,.col-xl-auto{position:relative;width:100%;min-height:1px;padding-right:15px;padding-left:15px}.col{flex-basis:0;flex-grow:1;max-width:100%}.col-auto{flex:0 0 auto;width:auto;max-width:none}.col-1{flex:0 0 8.333333%;max-width:8.333333%}.col-2{flex:0 0 16.666667%;max-width:16.666667%}.col-3{flex:0 0 25%;max-width:25%}.col-4{flex:0 0 33.333333%;max-width:33.333333%}.col-5{flex:0 0 41.666667%;max-width:41.666667%}.col-6{flex:0 0 50%;max-width:50%}.col-7{flex:0 0 58.333333%;max-width:58.333333%}.col-8{flex:0 0 66.666667%;max-width:66.666667%}.col-9{flex:0 0 75%;max-width:75%}.col-10{flex:0 0 83.333333%;max-width:83.333333%}.col-11{flex:0 0 91.666667%;max-width:91.666667%}.col-12{flex:0 0 100%;max-width:100%}.order-first{order:-1}.order-last{order:13}.order-0{order:0}.order-1{order:1}.order-2{order:2}.order-3{order:3}.order-4{order:4}.order-5{order:5}.order-6{order:6}.order-7{order:7}.order-8{order:8}.order-9{order:9}.order-10{order:10}.order-11{order:11}.order-12{order:12}.offset-1{margin-left:8.333333%}.offset-2{margin-left:16.666667%}.offset-3{margin-left:25%}.offset-4{margin-left:33.333333%}.offset-5{margin-left:41.666667%}.offset-6{margin-left:50%}.offset-7{margin-left:58.333333%}.offset-8{margin-left:66.666667%}.offset-9{margin-left:75%}.offset-10{margin-left:83.333333%}.offset-11{margin-left:91.666667%}@media (min-width:576px){.col-sm{flex-basis:0;flex-grow:1;max-width:100%}.col-sm-auto{flex:0 0 auto;width:auto;max-width:none}.col-sm-1{flex:0 0 8.333333%;max-width:8.333333%}.col-sm-2{flex:0 0 16.666667%;max-width:16.666667%}.col-sm-3{flex:0 0 25%;max-width:25%}.col-sm-4{flex:0 0 33.333333%;max-width:33.333333%}.col-sm-5{flex:0 0 41.666667%;max-width:41.666667%}.col-sm-6{flex:0 0 50%;max-width:50%}.col-sm-7{flex:0 0 58.333333%;max-width:58.333333%}.col-sm-8{flex:0 0 66.666667%;max-width:66.666667%}.col-sm-9{flex:0 0 75%;max-width:75%}.col-sm-10{flex:0 0 83.333333%;max-width:83.333333%}.col-sm-11{flex:0 0 91.666667%;max-width:91.666667%}.col-sm-12{flex:0 0 100%;max-width:100%}.order-sm-first{order:-1}.order-sm-last{order:13}.order-sm-0{order:0}.order-sm-1{order:1}.order-sm-2{order:2}.order-sm-3{order:3}.order-sm-4{order:4}.order-sm-5{order:5}.order-sm-6{order:6}.order-sm-7{order:7}.order-sm-8{order:8}.order-sm-9{order:9}.order-sm-10{order:10}.order-sm-11{order:11}.order-sm-12{order:12}.offset-sm-0{margin-left:0}.offset-sm-1{margin-left:8.333333%}.offset-sm-2{margin-left:16.666667%}.offset-sm-3{margin-left:25%}.offset-sm-4{margin-left:33.333333%}.offset-sm-5{margin-left:41.666667%}.offset-sm-6{margin-left:50%}.offset-sm-7{margin-left:58.333333%}.offset-sm-8{margin-left:66.666667%}.offset-sm-9{margin-left:75%}.offset-sm-10{margin-left:83.333333%}.offset-sm-11{margin-left:91.666667%}}@media (min-width:768px){.col-md{flex-basis:0;flex-grow:1;max-width:100%}.col-md-auto{flex:0 0 auto;width:auto;max-width:none}.col-md-1{flex:0 0 8.333333%;max-width:8.333333%}.col-md-2{flex:0 0 16.666667%;max-width:16.666667%}.col-md-3{flex:0 0 25%;max-width:25%}.col-md-4{flex:0 0 33.333333%;max-width:33.333333%}.col-md-5{flex:0 0 41.666667%;max-width:41.666667%}.col-md-6{flex:0 0 50%;max-width:50%}.col-md-7{flex:0 0 58.333333%;max-width:58.333333%}.col-md-8{flex:0 0 66.666667%;max-width:66.666667%}.col-md-9{flex:0 0 75%;max-width:75%}.col-md-10{flex:0 0 83.333333%;max-width:83.333333%}.col-md-11{flex:0 0 91.666667%;max-width:91.666667%}.col-md-12{flex:0 0 100%;max-width:100%}.order-md-first{order:-1}.order-md-last{order:13}.order-md-0{order:0}.order-md-1{order:1}.order-md-2{order:2}.order-md-3{order:3}.order-md-4{order:4}.order-md-5{order:5}.order-md-6{order:6}.order-md-7{order:7}.order-md-8{order:8}.order-md-9{order:9}.order-md-10{order:10}.order-md-11{order:11}.order-md-12{order:12}.offset-md-0{margin-left:0}.offset-md-1{margin-left:8.333333%}.offset-md-2{margin-left:16.666667%}.offset-md-3{margin-left:25%}.offset-md-4{margin-left:33.333333%}.offset-md-5{margin-left:41.666667%}.offset-md-6{margin-left:50%}.offset-md-7{margin-left:58.333333%}.offset-md-8{margin-left:66.666667%}.offset-md-9{margin-left:75%}.offset-md-10{margin-left:83.333333%}.offset-md-11{margin-left:91.666667%}}@media (min-width:992px){.col-lg{flex-basis:0;flex-grow:1;max-width:100%}.col-lg-auto{flex:0 0 auto;width:auto;max-width:none}.col-lg-1{flex:0 0 8.333333%;max-width:8.333333%}.col-lg-2{flex:0 0 16.666667%;max-width:16.666667%}.col-lg-3{flex:0 0 25%;max-width:25%}.col-lg-4{flex:0 0 33.333333%;max-width:33.333333%}.col-lg-5{flex:0 0 41.666667%;max-width:41.666667%}.col-lg-6{flex:0 0 50%;max-width:50%}.col-lg-7{flex:0 0 58.333333%;max-width:58.333333%}.col-lg-8{flex:0 0 66.666667%;max-width:66.666667%}.col-lg-9{flex:0 0 75%;max-width:75%}.col-lg-10{flex:0 0 83.333333%;max-width:83.333333%}.col-lg-11{flex:0 0 91.666667%;max-width:91.666667%}.col-lg-12{flex:0 0 100%;max-width:100%}.order-lg-first{order:-1}.order-lg-last{order:13}.order-lg-0{order:0}.order-lg-1{order:1}.order-lg-2{order:2}.order-lg-3{order:3}.order-lg-4{order:4}.order-lg-5{order:5}.order-lg-6{order:6}.order-lg-7{order:7}.order-lg-8{order:8}.order-lg-9{order:9}.order-lg-10{order:10}.order-lg-11{order:11}.order-lg-12{order:12}.offset-lg-0{margin-left:0}.offset-lg-1{margin-left:8.333333%}.offset-lg-2{margin-left:16.666667%}.offset-lg-3{margin-left:25%}.offset-lg-4{margin-left:33.333333%}.offset-lg-5{margin-left:41.666667%}.offset-lg-6{margin-left:50%}.offset-lg-7{margin-left:58.333333%}.offset-lg-8{margin-left:66.666667%}.offset-lg-9{margin-left:75%}.offset-lg-10{margin-left:83.333333%}.offset-lg-11{margin-left:91.666667%}}@media (min-width:1200px){.col-xl{flex-basis:0;flex-grow:1;max-width:100%}.col-xl-auto{flex:0 0 auto;width:auto;max-width:none}.col-xl-1{flex:0 0 8.333333%;max-width:8.333333%}.col-xl-2{flex:0 0 16.666667%;max-width:16.666667%}.col-xl-3{flex:0 0 25%;max-width:25%}.col-xl-4{flex:0 0 33.333333%;max-width:33.333333%}.col-xl-5{flex:0 0 41.666667%;max-width:41.666667%}.col-xl-6{flex:0 0 50%;max-width:50%}.col-xl-7{flex:0 0 58.333333%;max-width:58.333333%}.col-xl-8{flex:0 0 66.666667%;max-width:66.666667%}.col-xl-9{flex:0 0 75%;max-width:75%}.col-xl-10{flex:0 0 83.333333%;max-width:83.333333%}.col-xl-11{flex:0 0 91.666667%;max-width:91.666667%}.col-xl-12{flex:0 0 100%;max-width:100%}.order-xl-first{order:-1}.order-xl-last{order:13}.order-xl-0{order:0}.order-xl-1{order:1}.order-xl-2{order:2}.order-xl-3{order:3}.order-xl-4{order:4}.order-xl-5{order:5}.order-xl-6{order:6}.order-xl-7{order:7}.order-xl-8{order:8}.order-xl-9{order:9}.order-xl-10{order:10}.order-xl-11{order:11}.order-xl-12{order:12}.offset-xl-0{margin-left:0}.offset-xl-1{margin-left:8.333333%}.offset-xl-2{margin-left:16.666667%}.offset-xl-3{margin-left:25%}.offset-xl-4{margin-left:33.333333%}.offset-xl-5{margin-left:41.666667%}.offset-xl-6{margin-left:50%}.offset-xl-7{margin-left:58.333333%}.offset-xl-8{margin-left:66.666667%}.offset-xl-9{margin-left:75%}.offset-xl-10{margin-left:83.333333%}.offset-xl-11{margin-left:91.666667%}}.table{width:100%;max-width:100%;margin-bottom:1rem;background-color:transparent}.table td,.table th{padding:.75rem;vertical-align:top;border-top:1px solid rgba(0,0,0,.06)}.table thead th{vertical-align:bottom;border-bottom:2px solid rgba(0,0,0,.06)}.table tbody+tbody{border-top:2px solid rgba(0,0,0,.06)}.table .table{background-color:#fafafa}.table-sm td,.table-sm th{padding:.3rem}.table-bordered,.table-bordered td,.table-bordered th{border:1px solid rgba(0,0,0,.06)}.table-bordered thead td,.table-bordered thead th{border-bottom-width:2px}.table-striped tbody tr:nth-of-type(odd){background-color:rgba(0,0,0,.05)}.table-hover tbody tr:hover{background-color:rgba(0,0,0,.075)}.table-primary,.table-primary>td,.table-primary>th{background-color:#c1e2fc}.table-hover .table-primary:hover,.table-hover .table-primary:hover>td,.table-hover .table-primary:hover>th{background-color:#a9d7fb}.table-secondary,.table-secondary>td,.table-secondary>th{background-color:#d6d8db}.table-hover .table-secondary:hover,.table-hover .table-secondary:hover>td,.table-hover .table-secondary:hover>th{background-color:#c8cbcf}.table-success,.table-success>td,.table-success>th{background-color:#cde9ce}.table-hover .table-success:hover,.table-hover .table-success:hover>td,.table-hover .table-success:hover>th{background-color:#bbe1bd}.table-info,.table-info>td,.table-info>th{background-color:#b8ecf3}.table-hover .table-info:hover,.table-hover .table-info:hover>td,.table-hover .table-info:hover>th{background-color:#a2e6ef}.table-warning,.table-warning>td,.table-warning>th{background-color:#fff9c8}.table-hover .table-warning:hover,.table-hover .table-warning:hover>td,.table-hover .table-warning:hover>th{background-color:#fff6af}.table-danger,.table-danger>td,.table-danger>th{background-color:#fccac7}.table-hover .table-danger:hover,.table-hover .table-danger:hover>td,.table-hover .table-danger:hover>th{background-color:#fbb3af}.table-light,.table-light>td,.table-light>th{background-color:#fdfdfe}.table-hover .table-light:hover,.table-hover .table-light:hover>td,.table-hover .table-light:hover>th{background-color:#ececf6}.table-dark,.table-dark>td,.table-dark>th{background-color:#c6c8ca}.table-hover .table-dark:hover,.table-hover .table-dark:hover>td,.table-hover .table-dark:hover>th{background-color:#b9bbbe}.table-active,.table-active>td,.table-active>th,.table-hover .table-active:hover,.table-hover .table-active:hover>td,.table-hover .table-active:hover>th{background-color:rgba(0,0,0,.075)}.table .thead-dark th{color:#fafafa;background-color:#212529;border-color:#32383e}.table .thead-light th{color:#495057;background-color:#e9ecef;border-color:rgba(0,0,0,.06)}.table-dark{color:#fafafa;background-color:#212529}.table-dark td,.table-dark th,.table-dark thead th{border-color:#32383e}.table-dark.table-bordered{border:0}.table-dark.table-striped tbody tr:nth-of-type(odd){background-color:hsla(0,0%,100%,.05)}.table-dark.table-hover tbody tr:hover{background-color:hsla(0,0%,100%,.075)}@media (max-width:575.98px){.table-responsive-sm{display:block;width:100%;overflow-x:auto;-webkit-overflow-scrolling:touch;-ms-overflow-style:-ms-autohiding-scrollbar}.table-responsive-sm>.table-bordered{border:0}}@media (max-width:767.98px){.table-responsive-md{display:block;width:100%;overflow-x:auto;-webkit-overflow-scrolling:touch;-ms-overflow-style:-ms-autohiding-scrollbar}.table-responsive-md>.table-bordered{border:0}}@media (max-width:991.98px){.table-responsive-lg{display:block;width:100%;overflow-x:auto;-webkit-overflow-scrolling:touch;-ms-overflow-style:-ms-autohiding-scrollbar}.table-responsive-lg>.table-bordered{border:0}}@media (max-width:1199.98px){.table-responsive-xl{display:block;width:100%;overflow-x:auto;-webkit-overflow-scrolling:touch;-ms-overflow-style:-ms-autohiding-scrollbar}.table-responsive-xl>.table-bordered{border:0}}.table-responsive{display:block;width:100%;overflow-x:auto;-webkit-overflow-scrolling:touch;-ms-overflow-style:-ms-autohiding-scrollbar}.table-responsive>.table-bordered{border:0}.form-control{display:block;width:100%;padding:.4375rem 0;font-size:1rem;line-height:1.5;color:#495057;background-color:transparent;background-clip:padding-box;border:1px solid #d2d2d2;box-shadow:none;transition:border-color .15s ease-in-out,box-shadow .15s ease-in-out}.form-control::-ms-expand{background-color:transparent;border:0}.form-control:focus{color:#495057;background-color:transparent;border-color:#9acffa;outline:0;box-shadow:none,0 0 0 .2rem rgba(33,150,243,.25)}.form-control::placeholder{color:#6c757d;opacity:1}.form-control:disabled,.form-control[readonly]{background-color:#e9ecef;opacity:1}select.form-control:not([size]):not([multiple]){height:calc(2.4375rem + 2px)}select.form-control:focus::-ms-value{color:#495057;background-color:transparent}.form-control-file,.form-control-range{display:block;width:100%}.col-form-label{padding-top:calc(.4375rem + 1px);padding-bottom:calc(.4375rem + 1px);margin-bottom:0;font-size:inherit;line-height:1.5}.col-form-label-lg{padding-top:calc(.5625rem + 1px);padding-bottom:calc(.5625rem + 1px);font-size:1.25rem;line-height:1.5}.col-form-label-sm{padding-top:calc(.25rem + 1px);padding-bottom:calc(.25rem + 1px);font-size:.875rem;line-height:1.5}.form-control-plaintext{display:block;width:100%;padding-top:.4375rem;padding-bottom:.4375rem;margin-bottom:0;line-height:1.5;background-color:transparent;border:solid transparent;border-width:1px 0}.form-control-plaintext.form-control-lg,.form-control-plaintext.form-control-sm,.input-group-lg>.form-control-plaintext.form-control,.input-group-lg>.input-group-append>.form-control-plaintext.btn,.input-group-lg>.input-group-append>.form-control-plaintext.input-group-text,.input-group-lg>.input-group-prepend>.form-control-plaintext.btn,.input-group-lg>.input-group-prepend>.form-control-plaintext.input-group-text,.input-group-sm>.form-control-plaintext.form-control,.input-group-sm>.input-group-append>.form-control-plaintext.btn,.input-group-sm>.input-group-append>.form-control-plaintext.input-group-text,.input-group-sm>.input-group-prepend>.form-control-plaintext.btn,.input-group-sm>.input-group-prepend>.form-control-plaintext.input-group-text{padding-right:0;padding-left:0}.form-control-sm,.input-group-sm>.form-control,.input-group-sm>.input-group-append>.btn,.input-group-sm>.input-group-append>.input-group-text,.input-group-sm>.input-group-prepend>.btn,.input-group-sm>.input-group-prepend>.input-group-text{padding:.25rem 0;font-size:.875rem;line-height:1.5;border-radius:.2rem}.input-group-sm>.input-group-append>select.btn:not([size]):not([multiple]),.input-group-sm>.input-group-append>select.input-group-text:not([size]):not([multiple]),.input-group-sm>.input-group-prepend>select.btn:not([size]):not([multiple]),.input-group-sm>.input-group-prepend>select.input-group-text:not([size]):not([multiple]),.input-group-sm>select.form-control:not([size]):not([multiple]),select.form-control-sm:not([size]):not([multiple]){height:calc(2.125rem + 2px)}.form-control-lg,.input-group-lg>.form-control,.input-group-lg>.input-group-append>.btn,.input-group-lg>.input-group-append>.input-group-text,.input-group-lg>.input-group-prepend>.btn,.input-group-lg>.input-group-prepend>.input-group-text{padding:.5625rem 0;font-size:1.25rem;line-height:1.5;border-radius:.3rem}.input-group-lg>.input-group-append>select.btn:not([size]):not([multiple]),.input-group-lg>.input-group-append>select.input-group-text:not([size]):not([multiple]),.input-group-lg>.input-group-prepend>select.btn:not([size]):not([multiple]),.input-group-lg>.input-group-prepend>select.input-group-text:not([size]):not([multiple]),.input-group-lg>select.form-control:not([size]):not([multiple]),select.form-control-lg:not([size]):not([multiple]){height:calc(4.125rem + 2px)}.form-group{margin-bottom:1rem}.form-text{display:block;margin-top:.25rem}.form-row{display:flex;flex-wrap:wrap;margin-right:-5px;margin-left:-5px}.form-row>.col,.form-row>[class*=col-]{padding-right:5px;padding-left:5px}.form-check{position:relative;display:block;padding-left:1.25rem}.form-check-input{position:absolute;margin-top:.3rem;margin-left:-1.25rem}.form-check-input:disabled~.form-check-label{color:#6c757d}.form-check-label{margin-bottom:0}.form-check-inline{display:inline-flex;align-items:center;padding-left:0;margin-right:.75rem}.form-check-inline .form-check-input{position:static;margin-top:0;margin-right:.3125rem;margin-left:0}.valid-feedback{display:none;width:100%;margin-top:.25rem;font-size:80%;color:#4caf50}.valid-tooltip{position:absolute;top:100%;z-index:5;display:none;max-width:100%;padding:.5rem;margin-top:.1rem;font-size:.875rem;line-height:1;color:#fff;background-color:rgba(76,175,80,.8);border-radius:.2rem}.custom-select.is-valid,.form-control.is-valid,.was-validated .custom-select:valid,.was-validated .form-control:valid{border-color:#4caf50}.custom-select.is-valid:focus,.form-control.is-valid:focus,.was-validated .custom-select:valid:focus,.was-validated .form-control:valid:focus{border-color:#4caf50;box-shadow:0 0 0 .2rem rgba(76,175,80,.25)}.custom-select.is-valid~.valid-feedback,.custom-select.is-valid~.valid-tooltip,.form-control.is-valid~.valid-feedback,.form-control.is-valid~.valid-tooltip,.was-validated .custom-select:valid~.valid-feedback,.was-validated .custom-select:valid~.valid-tooltip,.was-validated .form-control:valid~.valid-feedback,.was-validated .form-control:valid~.valid-tooltip{display:block}.form-check-input.is-valid~.form-check-label,.was-validated .form-check-input:valid~.form-check-label{color:#4caf50}.form-check-input.is-valid~.valid-feedback,.form-check-input.is-valid~.valid-tooltip,.was-validated .form-check-input:valid~.valid-feedback,.was-validated .form-check-input:valid~.valid-tooltip{display:block}.custom-control-input.is-valid~.custom-control-label,.was-validated .custom-control-input:valid~.custom-control-label{color:#4caf50}.custom-control-input.is-valid~.custom-control-label:before,.was-validated .custom-control-input:valid~.custom-control-label:before{background-color:#a3d7a5}.custom-control-input.is-valid~.valid-feedback,.custom-control-input.is-valid~.valid-tooltip,.was-validated .custom-control-input:valid~.valid-feedback,.was-validated .custom-control-input:valid~.valid-tooltip{display:block}.custom-control-input.is-valid:checked~.custom-control-label:before,.was-validated .custom-control-input:valid:checked~.custom-control-label:before{background-color:#6ec071}.custom-control-input.is-valid:focus~.custom-control-label:before,.was-validated .custom-control-input:valid:focus~.custom-control-label:before{box-shadow:0 0 0 1px #fafafa,0 0 0 .2rem rgba(76,175,80,.25)}.custom-file-input.is-valid~.custom-file-label,.was-validated .custom-file-input:valid~.custom-file-label{border-color:#4caf50}.custom-file-input.is-valid~.custom-file-label:before,.was-validated .custom-file-input:valid~.custom-file-label:before{border-color:inherit}.custom-file-input.is-valid~.valid-feedback,.custom-file-input.is-valid~.valid-tooltip,.was-validated .custom-file-input:valid~.valid-feedback,.was-validated .custom-file-input:valid~.valid-tooltip{display:block}.custom-file-input.is-valid:focus~.custom-file-label,.was-validated .custom-file-input:valid:focus~.custom-file-label{box-shadow:0 0 0 .2rem rgba(76,175,80,.25)}.invalid-feedback{display:none;width:100%;margin-top:.25rem;font-size:80%;color:#f44336}.invalid-tooltip{position:absolute;top:100%;z-index:5;display:none;max-width:100%;padding:.5rem;margin-top:.1rem;font-size:.875rem;line-height:1;color:#fff;background-color:rgba(244,67,54,.8);border-radius:.2rem}.custom-select.is-invalid,.form-control.is-invalid,.was-validated .custom-select:invalid,.was-validated .form-control:invalid{border-color:#f44336}.custom-select.is-invalid:focus,.form-control.is-invalid:focus,.was-validated .custom-select:invalid:focus,.was-validated .form-control:invalid:focus{border-color:#f44336;box-shadow:0 0 0 .2rem rgba(244,67,54,.25)}.custom-select.is-invalid~.invalid-feedback,.custom-select.is-invalid~.invalid-tooltip,.form-control.is-invalid~.invalid-feedback,.form-control.is-invalid~.invalid-tooltip,.was-validated .custom-select:invalid~.invalid-feedback,.was-validated .custom-select:invalid~.invalid-tooltip,.was-validated .form-control:invalid~.invalid-feedback,.was-validated .form-control:invalid~.invalid-tooltip{display:block}.form-check-input.is-invalid~.form-check-label,.was-validated .form-check-input:invalid~.form-check-label{color:#f44336}.form-check-input.is-invalid~.invalid-feedback,.form-check-input.is-invalid~.invalid-tooltip,.was-validated .form-check-input:invalid~.invalid-feedback,.was-validated .form-check-input:invalid~.invalid-tooltip{display:block}.custom-control-input.is-invalid~.custom-control-label,.was-validated .custom-control-input:invalid~.custom-control-label{color:#f44336}.custom-control-input.is-invalid~.custom-control-label:before,.was-validated .custom-control-input:invalid~.custom-control-label:before{background-color:#fbb4af}.custom-control-input.is-invalid~.invalid-feedback,.custom-control-input.is-invalid~.invalid-tooltip,.was-validated .custom-control-input:invalid~.invalid-feedback,.was-validated .custom-control-input:invalid~.invalid-tooltip{display:block}.custom-control-input.is-invalid:checked~.custom-control-label:before,.was-validated .custom-control-input:invalid:checked~.custom-control-label:before{background-color:#f77066}.custom-control-input.is-invalid:focus~.custom-control-label:before,.was-validated .custom-control-input:invalid:focus~.custom-control-label:before{box-shadow:0 0 0 1px #fafafa,0 0 0 .2rem rgba(244,67,54,.25)}.custom-file-input.is-invalid~.custom-file-label,.was-validated .custom-file-input:invalid~.custom-file-label{border-color:#f44336}.custom-file-input.is-invalid~.custom-file-label:before,.was-validated .custom-file-input:invalid~.custom-file-label:before{border-color:inherit}.custom-file-input.is-invalid~.invalid-feedback,.custom-file-input.is-invalid~.invalid-tooltip,.was-validated .custom-file-input:invalid~.invalid-feedback,.was-validated .custom-file-input:invalid~.invalid-tooltip{display:block}.custom-file-input.is-invalid:focus~.custom-file-label,.was-validated .custom-file-input:invalid:focus~.custom-file-label{box-shadow:0 0 0 .2rem rgba(244,67,54,.25)}.form-inline{display:flex;flex-flow:row wrap;align-items:center}.form-inline .form-check{width:100%}@media (min-width:576px){.form-inline label{justify-content:center}.form-inline .form-group,.form-inline label{display:flex;align-items:center;margin-bottom:0}.form-inline .form-group{flex:0 0 auto;flex-flow:row wrap}.form-inline .form-control{display:inline-block;width:auto;vertical-align:middle}.form-inline .form-control-plaintext{display:inline-block}.form-inline .input-group{width:auto}.form-inline .form-check{display:flex;align-items:center;justify-content:center;width:auto;padding-left:0}.form-inline .form-check-input{position:relative;margin-top:0;margin-right:.25rem;margin-left:0}.form-inline .custom-control{align-items:center;justify-content:center}.form-inline .custom-control-label{margin-bottom:0}}.btn{display:inline-block;text-align:center;white-space:nowrap;vertical-align:middle;user-select:none;border:1px solid transparent;padding:.46875rem 1rem;font-size:1rem;line-height:1.5;border-radius:.25rem;transition:color .15s ease-in-out,background-color .15s ease-in-out,border-color .15s ease-in-out,box-shadow .15s ease-in-out}.btn:focus,.btn:hover{text-decoration:none}.btn.focus,.btn:focus{outline:0;box-shadow:0 0 0 .2rem rgba(33,150,243,.25)}.btn.disabled,.btn:disabled{opacity:.65;box-shadow:none}.btn:not(:disabled):not(.disabled){cursor:pointer}.btn:not(:disabled):not(.disabled).active,.btn:not(:disabled):not(.disabled):active{background-image:none;box-shadow:none}.btn:not(:disabled):not(.disabled).active:focus,.btn:not(:disabled):not(.disabled):active:focus{box-shadow:0 0 0 .2rem rgba(33,150,243,.25),none}a.btn.disabled,fieldset:disabled a.btn{pointer-events:none}.btn-primary{color:#fff;background-color:#2196f3;border-color:#2196f3;box-shadow:none}.btn-primary:hover{color:#fff;background-color:#0c83e2;border-color:#0c7cd5}.btn-primary.focus,.btn-primary:focus{box-shadow:none,0 0 0 .2rem rgba(33,150,243,.5)}.btn-primary.disabled,.btn-primary:disabled{color:#fff;background-color:#2196f3;border-color:#2196f3}.btn-primary:not(:disabled):not(.disabled).active,.btn-primary:not(:disabled):not(.disabled):active,.show>.btn-primary.dropdown-toggle{color:#fff;background-color:#0c7cd5;border-color:#0b75c9}.btn-primary:not(:disabled):not(.disabled).active:focus,.btn-primary:not(:disabled):not(.disabled):active:focus,.show>.btn-primary.dropdown-toggle:focus{box-shadow:none,0 0 0 .2rem rgba(33,150,243,.5)}.btn-secondary{color:#fff;background-color:#6c757d;border-color:#6c757d;box-shadow:none}.btn-secondary:hover{color:#fff;background-color:#5a6268;border-color:#545b62}.btn-secondary.focus,.btn-secondary:focus{box-shadow:none,0 0 0 .2rem hsla(208,7%,46%,.5)}.btn-secondary.disabled,.btn-secondary:disabled{color:#fff;background-color:#6c757d;border-color:#6c757d}.btn-secondary:not(:disabled):not(.disabled).active,.btn-secondary:not(:disabled):not(.disabled):active,.show>.btn-secondary.dropdown-toggle{color:#fff;background-color:#545b62;border-color:#4e555b}.btn-secondary:not(:disabled):not(.disabled).active:focus,.btn-secondary:not(:disabled):not(.disabled):active:focus,.show>.btn-secondary.dropdown-toggle:focus{box-shadow:none,0 0 0 .2rem hsla(208,7%,46%,.5)}.btn-success{color:#fff;background-color:#4caf50;border-color:#4caf50;box-shadow:none}.btn-success:hover{color:#fff;background-color:#409444;border-color:#3d8b40}.btn-success.focus,.btn-success:focus{box-shadow:none,0 0 0 .2rem rgba(76,175,80,.5)}.btn-success.disabled,.btn-success:disabled{color:#fff;background-color:#4caf50;border-color:#4caf50}.btn-success:not(:disabled):not(.disabled).active,.btn-success:not(:disabled):not(.disabled):active,.show>.btn-success.dropdown-toggle{color:#fff;background-color:#3d8b40;border-color:#39833c}.btn-success:not(:disabled):not(.disabled).active:focus,.btn-success:not(:disabled):not(.disabled):active:focus,.show>.btn-success.dropdown-toggle:focus{box-shadow:none,0 0 0 .2rem rgba(76,175,80,.5)}.btn-info{color:#fff;background-color:#00bcd4;border-color:#00bcd4;box-shadow:none}.btn-info:hover{color:#fff;background-color:#009aae;border-color:#008fa1}.btn-info.focus,.btn-info:focus{box-shadow:none,0 0 0 .2rem rgba(0,188,212,.5)}.btn-info.disabled,.btn-info:disabled{color:#fff;background-color:#00bcd4;border-color:#00bcd4}.btn-info:not(:disabled):not(.disabled).active,.btn-info:not(:disabled):not(.disabled):active,.show>.btn-info.dropdown-toggle{color:#fff;background-color:#008fa1;border-color:#008394}.btn-info:not(:disabled):not(.disabled).active:focus,.btn-info:not(:disabled):not(.disabled):active:focus,.show>.btn-info.dropdown-toggle:focus{box-shadow:none,0 0 0 .2rem rgba(0,188,212,.5)}.btn-warning{color:#212529;background-color:#ffeb3b;border-color:#ffeb3b;box-shadow:none}.btn-warning:hover{color:#212529;background-color:#ffe715;border-color:#ffe608}.btn-warning.focus,.btn-warning:focus{box-shadow:none,0 0 0 .2rem rgba(255,235,59,.5)}.btn-warning.disabled,.btn-warning:disabled{color:#212529;background-color:#ffeb3b;border-color:#ffeb3b}.btn-warning:not(:disabled):not(.disabled).active,.btn-warning:not(:disabled):not(.disabled):active,.show>.btn-warning.dropdown-toggle{color:#212529;background-color:#ffe608;border-color:#fae100}.btn-warning:not(:disabled):not(.disabled).active:focus,.btn-warning:not(:disabled):not(.disabled):active:focus,.show>.btn-warning.dropdown-toggle:focus{box-shadow:none,0 0 0 .2rem rgba(255,235,59,.5)}.btn-danger{color:#fff;background-color:#f44336;border-color:#f44336;box-shadow:none}.btn-danger:hover{color:#fff;background-color:#f22112;border-color:#ea1c0d}.btn-danger.focus,.btn-danger:focus{box-shadow:none,0 0 0 .2rem rgba(244,67,54,.5)}.btn-danger.disabled,.btn-danger:disabled{color:#fff;background-color:#f44336;border-color:#f44336}.btn-danger:not(:disabled):not(.disabled).active,.btn-danger:not(:disabled):not(.disabled):active,.show>.btn-danger.dropdown-toggle{color:#fff;background-color:#ea1c0d;border-color:#de1b0c}.btn-danger:not(:disabled):not(.disabled).active:focus,.btn-danger:not(:disabled):not(.disabled):active:focus,.show>.btn-danger.dropdown-toggle:focus{box-shadow:none,0 0 0 .2rem rgba(244,67,54,.5)}.btn-light{color:#212529;background-color:#f8f9fa;border-color:#f8f9fa;box-shadow:none}.btn-light:hover{color:#212529;background-color:#e2e6ea;border-color:#dae0e5}.btn-light.focus,.btn-light:focus{box-shadow:none,0 0 0 .2rem rgba(248,249,250,.5)}.btn-light.disabled,.btn-light:disabled{color:#212529;background-color:#f8f9fa;border-color:#f8f9fa}.btn-light:not(:disabled):not(.disabled).active,.btn-light:not(:disabled):not(.disabled):active,.show>.btn-light.dropdown-toggle{color:#212529;background-color:#dae0e5;border-color:#d3d9df}.btn-light:not(:disabled):not(.disabled).active:focus,.btn-light:not(:disabled):not(.disabled):active:focus,.show>.btn-light.dropdown-toggle:focus{box-shadow:none,0 0 0 .2rem rgba(248,249,250,.5)}.btn-dark{color:#fff;background-color:#343a40;border-color:#343a40;box-shadow:none}.btn-dark:hover{color:#fff;background-color:#23272b;border-color:#1d2124}.btn-dark.focus,.btn-dark:focus{box-shadow:none,0 0 0 .2rem rgba(52,58,64,.5)}.btn-dark.disabled,.btn-dark:disabled{color:#fff;background-color:#343a40;border-color:#343a40}.btn-dark:not(:disabled):not(.disabled).active,.btn-dark:not(:disabled):not(.disabled):active,.show>.btn-dark.dropdown-toggle{color:#fff;background-color:#1d2124;border-color:#171a1d}.btn-dark:not(:disabled):not(.disabled).active:focus,.btn-dark:not(:disabled):not(.disabled):active:focus,.show>.btn-dark.dropdown-toggle:focus{box-shadow:none,0 0 0 .2rem rgba(52,58,64,.5)}.btn-outline-primary{color:#2196f3;background-color:transparent;background-image:none;border-color:#2196f3}.btn-outline-primary:hover{color:#fff;background-color:#2196f3;border-color:#2196f3}.btn-outline-primary.focus,.btn-outline-primary:focus{box-shadow:0 0 0 .2rem rgba(33,150,243,.5)}.btn-outline-primary.disabled,.btn-outline-primary:disabled{color:#2196f3;background-color:transparent}.btn-outline-primary:not(:disabled):not(.disabled).active,.btn-outline-primary:not(:disabled):not(.disabled):active,.show>.btn-outline-primary.dropdown-toggle{color:#fff;background-color:#2196f3;border-color:#2196f3}.btn-outline-primary:not(:disabled):not(.disabled).active:focus,.btn-outline-primary:not(:disabled):not(.disabled):active:focus,.show>.btn-outline-primary.dropdown-toggle:focus{box-shadow:0 0 0 .2rem rgba(33,150,243,.5)}.btn-outline-secondary{color:#6c757d;background-color:transparent;background-image:none;border-color:#6c757d}.btn-outline-secondary:hover{color:#fff;background-color:#6c757d;border-color:#6c757d}.btn-outline-secondary.focus,.btn-outline-secondary:focus{box-shadow:0 0 0 .2rem hsla(208,7%,46%,.5)}.btn-outline-secondary.disabled,.btn-outline-secondary:disabled{color:#6c757d;background-color:transparent}.btn-outline-secondary:not(:disabled):not(.disabled).active,.btn-outline-secondary:not(:disabled):not(.disabled):active,.show>.btn-outline-secondary.dropdown-toggle{color:#fff;background-color:#6c757d;border-color:#6c757d}.btn-outline-secondary:not(:disabled):not(.disabled).active:focus,.btn-outline-secondary:not(:disabled):not(.disabled):active:focus,.show>.btn-outline-secondary.dropdown-toggle:focus{box-shadow:0 0 0 .2rem hsla(208,7%,46%,.5)}.btn-outline-success{color:#4caf50;background-color:transparent;background-image:none;border-color:#4caf50}.btn-outline-success:hover{color:#fff;background-color:#4caf50;border-color:#4caf50}.btn-outline-success.focus,.btn-outline-success:focus{box-shadow:0 0 0 .2rem rgba(76,175,80,.5)}.btn-outline-success.disabled,.btn-outline-success:disabled{color:#4caf50;background-color:transparent}.btn-outline-success:not(:disabled):not(.disabled).active,.btn-outline-success:not(:disabled):not(.disabled):active,.show>.btn-outline-success.dropdown-toggle{color:#fff;background-color:#4caf50;border-color:#4caf50}.btn-outline-success:not(:disabled):not(.disabled).active:focus,.btn-outline-success:not(:disabled):not(.disabled):active:focus,.show>.btn-outline-success.dropdown-toggle:focus{box-shadow:0 0 0 .2rem rgba(76,175,80,.5)}.btn-outline-info{color:#00bcd4;background-color:transparent;background-image:none;border-color:#00bcd4}.btn-outline-info:hover{color:#fff;background-color:#00bcd4;border-color:#00bcd4}.btn-outline-info.focus,.btn-outline-info:focus{box-shadow:0 0 0 .2rem rgba(0,188,212,.5)}.btn-outline-info.disabled,.btn-outline-info:disabled{color:#00bcd4;background-color:transparent}.btn-outline-info:not(:disabled):not(.disabled).active,.btn-outline-info:not(:disabled):not(.disabled):active,.show>.btn-outline-info.dropdown-toggle{color:#fff;background-color:#00bcd4;border-color:#00bcd4}.btn-outline-info:not(:disabled):not(.disabled).active:focus,.btn-outline-info:not(:disabled):not(.disabled):active:focus,.show>.btn-outline-info.dropdown-toggle:focus{box-shadow:0 0 0 .2rem rgba(0,188,212,.5)}.btn-outline-warning{color:#ffeb3b;background-color:transparent;background-image:none;border-color:#ffeb3b}.btn-outline-warning:hover{color:#212529;background-color:#ffeb3b;border-color:#ffeb3b}.btn-outline-warning.focus,.btn-outline-warning:focus{box-shadow:0 0 0 .2rem rgba(255,235,59,.5)}.btn-outline-warning.disabled,.btn-outline-warning:disabled{color:#ffeb3b;background-color:transparent}.btn-outline-warning:not(:disabled):not(.disabled).active,.btn-outline-warning:not(:disabled):not(.disabled):active,.show>.btn-outline-warning.dropdown-toggle{color:#212529;background-color:#ffeb3b;border-color:#ffeb3b}.btn-outline-warning:not(:disabled):not(.disabled).active:focus,.btn-outline-warning:not(:disabled):not(.disabled):active:focus,.show>.btn-outline-warning.dropdown-toggle:focus{box-shadow:0 0 0 .2rem rgba(255,235,59,.5)}.btn-outline-danger{color:#f44336;background-color:transparent;background-image:none;border-color:#f44336}.btn-outline-danger:hover{color:#fff;background-color:#f44336;border-color:#f44336}.btn-outline-danger.focus,.btn-outline-danger:focus{box-shadow:0 0 0 .2rem rgba(244,67,54,.5)}.btn-outline-danger.disabled,.btn-outline-danger:disabled{color:#f44336;background-color:transparent}.btn-outline-danger:not(:disabled):not(.disabled).active,.btn-outline-danger:not(:disabled):not(.disabled):active,.show>.btn-outline-danger.dropdown-toggle{color:#fff;background-color:#f44336;border-color:#f44336}.btn-outline-danger:not(:disabled):not(.disabled).active:focus,.btn-outline-danger:not(:disabled):not(.disabled):active:focus,.show>.btn-outline-danger.dropdown-toggle:focus{box-shadow:0 0 0 .2rem rgba(244,67,54,.5)}.btn-outline-light{color:#f8f9fa;background-color:transparent;background-image:none;border-color:#f8f9fa}.btn-outline-light:hover{color:#212529;background-color:#f8f9fa;border-color:#f8f9fa}.btn-outline-light.focus,.btn-outline-light:focus{box-shadow:0 0 0 .2rem rgba(248,249,250,.5)}.btn-outline-light.disabled,.btn-outline-light:disabled{color:#f8f9fa;background-color:transparent}.btn-outline-light:not(:disabled):not(.disabled).active,.btn-outline-light:not(:disabled):not(.disabled):active,.show>.btn-outline-light.dropdown-toggle{color:#212529;background-color:#f8f9fa;border-color:#f8f9fa}.btn-outline-light:not(:disabled):not(.disabled).active:focus,.btn-outline-light:not(:disabled):not(.disabled):active:focus,.show>.btn-outline-light.dropdown-toggle:focus{box-shadow:0 0 0 .2rem rgba(248,249,250,.5)}.btn-outline-dark{color:#343a40;background-color:transparent;background-image:none;border-color:#343a40}.btn-outline-dark:hover{color:#fff;background-color:#343a40;border-color:#343a40}.btn-outline-dark.focus,.btn-outline-dark:focus{box-shadow:0 0 0 .2rem rgba(52,58,64,.5)}.btn-outline-dark.disabled,.btn-outline-dark:disabled{color:#343a40;background-color:transparent}.btn-outline-dark:not(:disabled):not(.disabled).active,.btn-outline-dark:not(:disabled):not(.disabled):active,.show>.btn-outline-dark.dropdown-toggle{color:#fff;background-color:#343a40;border-color:#343a40}.btn-outline-dark:not(:disabled):not(.disabled).active:focus,.btn-outline-dark:not(:disabled):not(.disabled):active:focus,.show>.btn-outline-dark.dropdown-toggle:focus{box-shadow:0 0 0 .2rem rgba(52,58,64,.5)}.btn-link{font-weight:400;color:#9c27b0;background-color:transparent}.btn-link:hover{color:#0a6ebd;background-color:transparent}.btn-link.focus,.btn-link:focus,.btn-link:hover{text-decoration:underline;border-color:transparent}.btn-link.focus,.btn-link:focus{box-shadow:none}.btn-link.disabled,.btn-link:disabled{color:#999}.btn-group-lg>.btn,.btn-lg{padding:1.125rem 2.25rem;font-size:1.25rem;line-height:1.5;border-radius:.3rem}.btn-group-sm>.btn,.btn-sm{padding:.40625rem 1.25rem;font-size:.875rem;line-height:1.5;border-radius:.1875rem}.btn-block{display:block;width:100%}.btn-block+.btn-block{margin-top:.5rem}input[type=button].btn-block,input[type=reset].btn-block,input[type=submit].btn-block{width:100%}.fade{opacity:0;transition:opacity .15s linear}.fade.show{opacity:1}.collapse{display:none}.collapse.show{display:block}tr.collapse.show{display:table-row}tbody.collapse.show{display:table-row-group}.collapsing{height:0;overflow:hidden;transition:height .35s ease}.collapsing,.dropdown,.dropup{position:relative}.dropdown-toggle:after{display:inline-block;width:0;height:0;margin-left:.255em;vertical-align:.255em;content:"";border-top:.3em solid;border-right:.3em solid transparent;border-bottom:0;border-left:.3em solid transparent}.dropdown-toggle:empty:after{margin-left:0}.dropdown-menu{position:absolute;top:100%;left:0;z-index:1000;float:left;min-width:10rem;padding:.5rem 0;margin:.125rem 0 0;font-size:1rem;color:#212529;text-align:left;list-style:none;background-color:#fff;background-clip:padding-box;border:1px solid rgba(0,0,0,.15);border-radius:.25rem;box-shadow:0 2px 2px 0 rgba(0,0,0,.14),0 3px 1px -2px rgba(0,0,0,.2),0 1px 5px 0 rgba(0,0,0,.12)}.dropup .dropdown-menu{margin-top:0;margin-bottom:.125rem}.dropup .dropdown-toggle:after{display:inline-block;width:0;height:0;margin-left:.255em;vertical-align:.255em;content:"";border-top:0;border-right:.3em solid transparent;border-bottom:.3em solid;border-left:.3em solid transparent}.dropup .dropdown-toggle:empty:after{margin-left:0}.dropright .dropdown-menu{margin-top:0;margin-left:.125rem}.dropright .dropdown-toggle:after{display:inline-block;width:0;height:0;margin-left:.255em;vertical-align:.255em;content:"";border-top:.3em solid transparent;border-bottom:.3em solid transparent;border-left:.3em solid}.dropright .dropdown-toggle:empty:after{margin-left:0}.dropright .dropdown-toggle:after{vertical-align:0}.dropleft .dropdown-menu{margin-top:0;margin-right:.125rem}.dropleft .dropdown-toggle:after{display:inline-block;width:0;height:0;margin-left:.255em;vertical-align:.255em;content:"";display:none}.dropleft .dropdown-toggle:before{display:inline-block;width:0;height:0;margin-right:.255em;vertical-align:.255em;content:"";border-top:.3em solid transparent;border-right:.3em solid;border-bottom:.3em solid transparent}.dropleft .dropdown-toggle:empty:after{margin-left:0}.dropleft .dropdown-toggle:before{vertical-align:0}.dropdown-divider{height:0;margin:.5rem 0;overflow:hidden;border-top:1px solid #e9ecef}.dropdown-item{display:block;width:100%;padding:.625rem 1.25rem;clear:both;font-weight:400;color:#212529;text-align:inherit;white-space:nowrap;background-color:transparent;border:0}.dropdown-item:focus,.dropdown-item:hover{color:#16181b;text-decoration:none;background-color:#f8f9fa}.dropdown-item.active,.dropdown-item:active{color:#fff;text-decoration:none;background-color:#2196f3}.dropdown-item.disabled,.dropdown-item:disabled{color:#6c757d;background-color:transparent}.dropdown-menu.show{display:block}.dropdown-header{display:block;padding:.5rem 1.25rem;margin-bottom:0;font-size:.875rem;color:#6c757d;white-space:nowrap}.btn-group,.btn-group-vertical{display:inline-flex;vertical-align:middle}.btn-group-vertical>.btn,.btn-group>.btn{position:relative;flex:0 1 auto}.btn-group-vertical>.btn.active,.btn-group-vertical>.btn:active,.btn-group-vertical>.btn:focus,.btn-group-vertical>.btn:hover,.btn-group>.btn.active,.btn-group>.btn:active,.btn-group>.btn:focus,.btn-group>.btn:hover{z-index:1}.btn-group-vertical .btn+.btn,.btn-group-vertical .btn+.btn-group,.btn-group-vertical .btn-group+.btn,.btn-group-vertical .btn-group+.btn-group,.btn-group .btn+.btn,.btn-group .btn+.btn-group,.btn-group .btn-group+.btn,.btn-group .btn-group+.btn-group{margin-left:-1px}.btn-toolbar{display:flex;flex-wrap:wrap;justify-content:flex-start}.btn-toolbar .input-group{width:auto}.btn-group>.btn:first-child{margin-left:0}.btn-group>.btn-group:not(:last-child)>.btn,.btn-group>.btn:not(:last-child):not(.dropdown-toggle){border-top-right-radius:0;border-bottom-right-radius:0}.btn-group>.btn-group:not(:first-child)>.btn,.btn-group>.btn:not(:first-child){border-top-left-radius:0;border-bottom-left-radius:0}.dropdown-toggle-split{padding-right:.75rem;padding-left:.75rem}.dropdown-toggle-split:after{margin-left:0}.btn-group-sm>.btn+.dropdown-toggle-split,.btn-sm+.dropdown-toggle-split{padding-right:.9375rem;padding-left:.9375rem}.btn-group-lg>.btn+.dropdown-toggle-split,.btn-lg+.dropdown-toggle-split{padding-right:1.6875rem;padding-left:1.6875rem}.btn-group.show .dropdown-toggle,.btn-group.show .dropdown-toggle.btn-link{box-shadow:none}.btn-group-vertical{flex-direction:column;align-items:flex-start;justify-content:center}.btn-group-vertical .btn,.btn-group-vertical .btn-group{width:100%}.btn-group-vertical>.btn+.btn,.btn-group-vertical>.btn+.btn-group,.btn-group-vertical>.btn-group+.btn,.btn-group-vertical>.btn-group+.btn-group{margin-top:-1px;margin-left:0}.btn-group-vertical>.btn-group:not(:last-child)>.btn,.btn-group-vertical>.btn:not(:last-child):not(.dropdown-toggle){border-bottom-right-radius:0;border-bottom-left-radius:0}.btn-group-vertical>.btn-group:not(:first-child)>.btn,.btn-group-vertical>.btn:not(:first-child){border-top-left-radius:0;border-top-right-radius:0}.btn-group-toggle>.btn,.btn-group-toggle>.btn-group>.btn{margin-bottom:0}.btn-group-toggle>.btn-group>.btn input[type=checkbox],.btn-group-toggle>.btn-group>.btn input[type=radio],.btn-group-toggle>.btn input[type=checkbox],.btn-group-toggle>.btn input[type=radio]{position:absolute;clip:rect(0,0,0,0);pointer-events:none}.input-group{position:relative;display:flex;flex-wrap:wrap;align-items:stretch;width:100%}.input-group>.custom-file,.input-group>.custom-select,.input-group>.form-control{position:relative;flex:1 1 auto;width:1%;margin-bottom:0}.input-group>.custom-file:focus,.input-group>.custom-select:focus,.input-group>.form-control:focus{z-index:3}.input-group>.custom-file+.custom-file,.input-group>.custom-file+.custom-select,.input-group>.custom-file+.form-control,.input-group>.custom-select+.custom-file,.input-group>.custom-select+.custom-select,.input-group>.custom-select+.form-control,.input-group>.form-control+.custom-file,.input-group>.form-control+.custom-select,.input-group>.form-control+.form-control{margin-left:-1px}.input-group>.custom-select:not(:last-child),.input-group>.form-control:not(:last-child){border-top-right-radius:0;border-bottom-right-radius:0}.input-group>.custom-select:not(:first-child),.input-group>.form-control:not(:first-child){border-top-left-radius:0;border-bottom-left-radius:0}.input-group>.custom-file{display:flex;align-items:center}.input-group>.custom-file:not(:last-child) .custom-file-label,.input-group>.custom-file:not(:last-child) .custom-file-label:before{border-top-right-radius:0;border-bottom-right-radius:0}.input-group>.custom-file:not(:first-child) .custom-file-label,.input-group>.custom-file:not(:first-child) .custom-file-label:before{border-top-left-radius:0;border-bottom-left-radius:0}.input-group-append,.input-group-prepend{display:flex}.input-group-append .btn,.input-group-prepend .btn{position:relative;z-index:2}.input-group-append .btn+.btn,.input-group-append .btn+.input-group-text,.input-group-append .input-group-text+.btn,.input-group-append .input-group-text+.input-group-text,.input-group-prepend .btn+.btn,.input-group-prepend .btn+.input-group-text,.input-group-prepend .input-group-text+.btn,.input-group-prepend .input-group-text+.input-group-text{margin-left:-1px}.input-group-prepend{margin-right:-1px}.input-group-append{margin-left:-1px}.input-group-text{display:flex;align-items:center;padding:.4375rem 0;margin-bottom:0;font-size:1rem;font-weight:400;line-height:1.5;color:#495057;text-align:center;white-space:nowrap;background-color:transparent;border:1px solid transparent;border-radius:0}.input-group-text input[type=checkbox],.input-group-text input[type=radio]{margin-top:0}.input-group>.input-group-append:last-child>.btn:not(:last-child):not(.dropdown-toggle),.input-group>.input-group-append:last-child>.input-group-text:not(:last-child),.input-group>.input-group-append:not(:last-child)>.btn,.input-group>.input-group-append:not(:last-child)>.input-group-text,.input-group>.input-group-prepend>.btn,.input-group>.input-group-prepend>.input-group-text{border-top-right-radius:0;border-bottom-right-radius:0}.input-group>.input-group-append>.btn,.input-group>.input-group-append>.input-group-text,.input-group>.input-group-prepend:first-child>.btn:not(:first-child),.input-group>.input-group-prepend:first-child>.input-group-text:not(:first-child),.input-group>.input-group-prepend:not(:first-child)>.btn,.input-group>.input-group-prepend:not(:first-child)>.input-group-text{border-top-left-radius:0;border-bottom-left-radius:0}.custom-control{position:relative;display:block;min-height:1.5rem;padding-left:1.5rem}.custom-control-inline{display:inline-flex;margin-right:1rem}.custom-control-input{position:absolute;z-index:-1;opacity:0}.custom-control-input:checked~.custom-control-label:before{color:#fff;background-color:#2196f3;box-shadow:none}.custom-control-input:focus~.custom-control-label:before{box-shadow:0 0 0 1px #fafafa,0 0 0 .2rem rgba(33,150,243,.25)}.custom-control-input:active~.custom-control-label:before{color:#fff;background-color:#cae6fc;box-shadow:none}.custom-control-input:disabled~.custom-control-label{color:#6c757d}.custom-control-input:disabled~.custom-control-label:before{background-color:#e9ecef}.custom-control-label{margin-bottom:0}.custom-control-label:before{pointer-events:none;user-select:none;background-color:#dee2e6;box-shadow:inset 0 .25rem .25rem rgba(0,0,0,.1)}.custom-control-label:after,.custom-control-label:before{position:absolute;top:.25rem;left:0;display:block;width:1rem;height:1rem;content:""}.custom-control-label:after{background-repeat:no-repeat;background-position:50%;background-size:50% 50%}.custom-checkbox .custom-control-label:before{border-radius:.25rem}.custom-checkbox .custom-control-input:checked~.custom-control-label:before{background-color:#2196f3}.custom-checkbox .custom-control-input:checked~.custom-control-label:after{background-image:url("data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 8 8'%3E%3Cpath fill='%23ffffff' d='M6.564.75l-3.59 3.612-1.538-1.55L0 4.26 2.974 7.25 8 2.193z'/%3E%3C/svg%3E")}.custom-checkbox .custom-control-input:indeterminate~.custom-control-label:before{background-color:#2196f3;box-shadow:none}.custom-checkbox .custom-control-input:indeterminate~.custom-control-label:after{background-image:url("data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 4 4'%3E%3Cpath stroke='%23ffffff' d='M0 2h4'/%3E%3C/svg%3E")}.custom-checkbox .custom-control-input:disabled:checked~.custom-control-label:before{background-color:rgba(33,150,243,.5)}.custom-checkbox .custom-control-input:disabled:indeterminate~.custom-control-label:before{background-color:rgba(33,150,243,.5)}.custom-radio .custom-control-label:before{border-radius:50%}.custom-radio .custom-control-input:checked~.custom-control-label:before{background-color:#2196f3}.custom-radio .custom-control-input:checked~.custom-control-label:after{background-image:url("data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='-4 -4 8 8'%3E%3Ccircle r='3' fill='%23ffffff'/%3E%3C/svg%3E")}.custom-radio .custom-control-input:disabled:checked~.custom-control-label:before{background-color:rgba(33,150,243,.5)}.custom-select{display:inline-block;width:100%;height:calc(2.4375rem + 2px);padding:.375rem 1.75rem .375rem .75rem;line-height:1.5;color:#495057;vertical-align:middle;background:#fff url("data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 4 5'%3E%3Cpath fill='%23343a40' d='M2 0L0 2h4zm0 5L0 3h4z'/%3E%3C/svg%3E") no-repeat right .75rem center;background-size:8px 10px;border:1px solid #d2d2d2;border-radius:.25rem;appearance:none}.custom-select:focus{border-color:#9acffa;outline:0;box-shadow:inset 0 1px 2px rgba(0,0,0,.075),0 0 5px rgba(154,207,250,.5)}.custom-select:focus::-ms-value{color:#495057;background-color:transparent}.custom-select[multiple],.custom-select[size]:not([size="1"]){height:auto;padding-right:.75rem;background-image:none}.custom-select:disabled{color:#6c757d;background-color:#e9ecef}.custom-select::-ms-expand{opacity:0}.custom-select-sm{height:calc(2.125rem + 2px);font-size:75%}.custom-select-lg,.custom-select-sm{padding-top:.375rem;padding-bottom:.375rem}.custom-select-lg{height:calc(4.125rem + 2px);font-size:125%}.custom-file{display:inline-block;margin-bottom:0}.custom-file,.custom-file-input{position:relative;width:100%;height:calc(2.4375rem + 2px)}.custom-file-input{z-index:2;margin:0;opacity:0}.custom-file-input:focus~.custom-file-control{border-color:#9acffa;box-shadow:0 0 0 .2rem rgba(33,150,243,.25)}.custom-file-input:focus~.custom-file-control:before{border-color:#9acffa}.custom-file-input:lang(en)~.custom-file-label:after{content:"Browse"}.custom-file-label{left:0;z-index:1;height:calc(2.4375rem + 2px);border:0 solid #d2d2d2;border-radius:0;box-shadow:none}.custom-file-label,.custom-file-label:after{position:absolute;top:0;right:0;padding:.46875rem 1rem;line-height:1.3;color:#495057;background-color:transparent}.custom-file-label:after{bottom:0;z-index:3;display:block;height:calc((2.4375rem + 2px) - 0 * 2);content:"Browse";border-left:0 solid #d2d2d2;border-radius:0 0 0 0}.nav{display:flex;flex-wrap:wrap;padding-left:0;margin-bottom:0;list-style:none}.nav-link{display:block;padding:.5rem 1rem}.nav-link:focus,.nav-link:hover{text-decoration:none}.nav-link.disabled{color:#6c757d}.nav-tabs{border-bottom:1px solid #dee2e6}.nav-tabs .nav-item{margin-bottom:-1px}.nav-tabs .nav-link{border:1px solid transparent;border-top-left-radius:.25rem;border-top-right-radius:.25rem}.nav-tabs .nav-link:focus,.nav-tabs .nav-link:hover{border-color:#e9ecef #e9ecef #dee2e6}.nav-tabs .nav-link.disabled{color:#6c757d;background-color:transparent;border-color:transparent}.nav-tabs .nav-item.show .nav-link,.nav-tabs .nav-link.active{color:#495057;background-color:#fafafa;border-color:#dee2e6 #dee2e6 #fafafa}.nav-tabs .dropdown-menu{margin-top:-1px;border-top-left-radius:0;border-top-right-radius:0}.nav-pills .nav-link{border-radius:.25rem}.nav-pills .nav-link.active,.nav-pills .show>.nav-link{color:#fff;background-color:#2196f3}.nav-fill .nav-item{flex:1 1 auto;text-align:center}.nav-justified .nav-item{flex-basis:0;flex-grow:1;text-align:center}.tab-content>.tab-pane{display:none}.tab-content>.active{display:block}.navbar{position:relative;padding:.5rem 1rem}.navbar,.navbar>.container,.navbar>.container-fluid{display:flex;flex-wrap:wrap;align-items:center;justify-content:space-between}.navbar-brand{display:inline-block;padding-top:.3125rem;padding-bottom:.3125rem;margin-right:1rem;font-size:1.25rem;line-height:inherit;white-space:nowrap}.navbar-brand:focus,.navbar-brand:hover{text-decoration:none}.navbar-nav{display:flex;flex-direction:column;padding-left:0;margin-bottom:0;list-style:none}.navbar-nav .nav-link{padding-right:0;padding-left:0}.navbar-nav .dropdown-menu{position:static;float:none}.navbar-text{display:inline-block;padding-top:.5rem;padding-bottom:.5rem}.navbar-collapse{flex-basis:100%;flex-grow:1;align-items:center}.navbar-toggler{padding:.25rem .75rem;font-size:1.25rem;line-height:1;background-color:transparent;border:1px solid transparent;border-radius:.25rem}.navbar-toggler:focus,.navbar-toggler:hover{text-decoration:none}.navbar-toggler:not(:disabled):not(.disabled){cursor:pointer}.navbar-toggler-icon{display:inline-block;width:1.5em;height:1.5em;vertical-align:middle;content:"";background:no-repeat 50%;background-size:100% 100%}@media (max-width:575.98px){.navbar-expand-sm>.container,.navbar-expand-sm>.container-fluid{padding-right:0;padding-left:0}}@media (min-width:576px){.navbar-expand-sm{flex-flow:row nowrap;justify-content:flex-start}.navbar-expand-sm .navbar-nav{flex-direction:row}.navbar-expand-sm .navbar-nav .dropdown-menu{position:absolute}.navbar-expand-sm .navbar-nav .dropdown-menu-right{right:0;left:auto}.navbar-expand-sm .navbar-nav .nav-link{padding-right:.5rem;padding-left:.5rem}.navbar-expand-sm>.container,.navbar-expand-sm>.container-fluid{flex-wrap:nowrap}.navbar-expand-sm .navbar-collapse{display:flex!important;flex-basis:auto}.navbar-expand-sm .navbar-toggler{display:none}.navbar-expand-sm .dropup .dropdown-menu{top:auto;bottom:100%}}@media (max-width:767.98px){.navbar-expand-md>.container,.navbar-expand-md>.container-fluid{padding-right:0;padding-left:0}}@media (min-width:768px){.navbar-expand-md{flex-flow:row nowrap;justify-content:flex-start}.navbar-expand-md .navbar-nav{flex-direction:row}.navbar-expand-md .navbar-nav .dropdown-menu{position:absolute}.navbar-expand-md .navbar-nav .dropdown-menu-right{right:0;left:auto}.navbar-expand-md .navbar-nav .nav-link{padding-right:.5rem;padding-left:.5rem}.navbar-expand-md>.container,.navbar-expand-md>.container-fluid{flex-wrap:nowrap}.navbar-expand-md .navbar-collapse{display:flex!important;flex-basis:auto}.navbar-expand-md .navbar-toggler{display:none}.navbar-expand-md .dropup .dropdown-menu{top:auto;bottom:100%}}@media (max-width:991.98px){.navbar-expand-lg>.container,.navbar-expand-lg>.container-fluid{padding-right:0;padding-left:0}}@media (min-width:992px){.navbar-expand-lg{flex-flow:row nowrap;justify-content:flex-start}.navbar-expand-lg .navbar-nav{flex-direction:row}.navbar-expand-lg .navbar-nav .dropdown-menu{position:absolute}.navbar-expand-lg .navbar-nav .dropdown-menu-right{right:0;left:auto}.navbar-expand-lg .navbar-nav .nav-link{padding-right:.5rem;padding-left:.5rem}.navbar-expand-lg>.container,.navbar-expand-lg>.container-fluid{flex-wrap:nowrap}.navbar-expand-lg .navbar-collapse{display:flex!important;flex-basis:auto}.navbar-expand-lg .navbar-toggler{display:none}.navbar-expand-lg .dropup .dropdown-menu{top:auto;bottom:100%}}@media (max-width:1199.98px){.navbar-expand-xl>.container,.navbar-expand-xl>.container-fluid{padding-right:0;padding-left:0}}@media (min-width:1200px){.navbar-expand-xl{flex-flow:row nowrap;justify-content:flex-start}.navbar-expand-xl .navbar-nav{flex-direction:row}.navbar-expand-xl .navbar-nav .dropdown-menu{position:absolute}.navbar-expand-xl .navbar-nav .dropdown-menu-right{right:0;left:auto}.navbar-expand-xl .navbar-nav .nav-link{padding-right:.5rem;padding-left:.5rem}.navbar-expand-xl>.container,.navbar-expand-xl>.container-fluid{flex-wrap:nowrap}.navbar-expand-xl .navbar-collapse{display:flex!important;flex-basis:auto}.navbar-expand-xl .navbar-toggler{display:none}.navbar-expand-xl .dropup .dropdown-menu{top:auto;bottom:100%}}.navbar-expand{flex-flow:row nowrap;justify-content:flex-start}.navbar-expand>.container,.navbar-expand>.container-fluid{padding-right:0;padding-left:0}.navbar-expand .navbar-nav{flex-direction:row}.navbar-expand .navbar-nav .dropdown-menu{position:absolute}.navbar-expand .navbar-nav .dropdown-menu-right{right:0;left:auto}.navbar-expand .navbar-nav .nav-link{padding-right:.5rem;padding-left:.5rem}.navbar-expand>.container,.navbar-expand>.container-fluid{flex-wrap:nowrap}.navbar-expand .navbar-collapse{display:flex!important;flex-basis:auto}.navbar-expand .navbar-toggler{display:none}.navbar-expand .dropup .dropdown-menu{top:auto;bottom:100%}.navbar-light .navbar-brand,.navbar-light .navbar-brand:focus,.navbar-light .navbar-brand:hover{color:rgba(0,0,0,.9)}.navbar-light .navbar-nav .nav-link{color:rgba(0,0,0,.5)}.navbar-light .navbar-nav .nav-link:focus,.navbar-light .navbar-nav .nav-link:hover{color:rgba(0,0,0,.7)}.navbar-light .navbar-nav .nav-link.disabled{color:rgba(0,0,0,.3)}.navbar-light .navbar-nav .active>.nav-link,.navbar-light .navbar-nav .nav-link.active,.navbar-light .navbar-nav .nav-link.show,.navbar-light .navbar-nav .show>.nav-link{color:rgba(0,0,0,.9)}.navbar-light .navbar-toggler{color:rgba(0,0,0,.5);border-color:rgba(0,0,0,.1)}.navbar-light .navbar-toggler-icon{background-image:url("data:image/svg+xml;charset=utf8,%3Csvg viewBox='0 0 30 30' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath stroke='rgba(0, 0, 0, 0.5)' stroke-width='2' stroke-linecap='round' stroke-miterlimit='10' d='M4 7h22M4 15h22M4 23h22'/%3E%3C/svg%3E")}.navbar-light .navbar-text{color:rgba(0,0,0,.5)}.navbar-light .navbar-text a,.navbar-light .navbar-text a:focus,.navbar-light .navbar-text a:hover{color:rgba(0,0,0,.9)}.navbar-dark .navbar-brand,.navbar-dark .navbar-brand:focus,.navbar-dark .navbar-brand:hover{color:#fff}.navbar-dark .navbar-nav .nav-link{color:hsla(0,0%,100%,.5)}.navbar-dark .navbar-nav .nav-link:focus,.navbar-dark .navbar-nav .nav-link:hover{color:hsla(0,0%,100%,.75)}.navbar-dark .navbar-nav .nav-link.disabled{color:hsla(0,0%,100%,.25)}.navbar-dark .navbar-nav .active>.nav-link,.navbar-dark .navbar-nav .nav-link.active,.navbar-dark .navbar-nav .nav-link.show,.navbar-dark .navbar-nav .show>.nav-link{color:#fff}.navbar-dark .navbar-toggler{color:hsla(0,0%,100%,.5);border-color:hsla(0,0%,100%,.1)}.navbar-dark .navbar-toggler-icon{background-image:url("data:image/svg+xml;charset=utf8,%3Csvg viewBox='0 0 30 30' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath stroke='rgba(255, 255, 255, 0.5)' stroke-width='2' stroke-linecap='round' stroke-miterlimit='10' d='M4 7h22M4 15h22M4 23h22'/%3E%3C/svg%3E")}.navbar-dark .navbar-text{color:hsla(0,0%,100%,.5)}.navbar-dark .navbar-text a,.navbar-dark .navbar-text a:focus,.navbar-dark .navbar-text a:hover{color:#fff}.card{position:relative;display:flex;flex-direction:column;min-width:0;word-wrap:break-word;background-color:#fff;background-clip:border-box;border:1px solid #eee;border-radius:.25rem}.card>hr{margin-right:0;margin-left:0}.card>.list-group:first-child .list-group-item:first-child{border-top-left-radius:.25rem;border-top-right-radius:.25rem}.card>.list-group:last-child .list-group-item:last-child{border-bottom-right-radius:.25rem;border-bottom-left-radius:.25rem}.card-body{flex:1 1 auto;padding:1.25rem}.card-title{margin-bottom:.75rem}.card-subtitle{margin-top:-.375rem}.card-subtitle,.card-text:last-child{margin-bottom:0}.card-link:hover{text-decoration:none}.card-link+.card-link{margin-left:1.25rem}.card-header{padding:.75rem 1.25rem;margin-bottom:0;background-color:#fff;border-bottom:1px solid #eee}.card-header:first-child{border-radius:calc(.25rem - 1px) calc(.25rem - 1px) 0 0}.card-header+.list-group .list-group-item:first-child{border-top:0}.card-footer{padding:.75rem 1.25rem;background-color:#fff;border-top:1px solid #eee}.card-footer:last-child{border-radius:0 0 calc(.25rem - 1px) calc(.25rem - 1px)}.card-header-tabs{margin-bottom:-.75rem;border-bottom:0}.card-header-pills,.card-header-tabs{margin-right:-.625rem;margin-left:-.625rem}.card-img-overlay{position:absolute;top:0;right:0;bottom:0;left:0;padding:1.25rem}.card-img{width:100%;border-radius:calc(.25rem - 1px)}.card-img-top{width:100%;border-top-left-radius:calc(.25rem - 1px);border-top-right-radius:calc(.25rem - 1px)}.card-img-bottom{width:100%;border-bottom-right-radius:calc(.25rem - 1px);border-bottom-left-radius:calc(.25rem - 1px)}.card-deck{display:flex;flex-direction:column}.card-deck .card{margin-bottom:15px}@media (min-width:576px){.card-deck{flex-flow:row wrap;margin-right:-15px;margin-left:-15px}.card-deck .card{display:flex;flex:1 0 0%;flex-direction:column;margin-right:15px;margin-bottom:0;margin-left:15px}}.card-group{display:flex;flex-direction:column}.card-group>.card{margin-bottom:15px}@media (min-width:576px){.card-group{flex-flow:row wrap}.card-group>.card{flex:1 0 0%;margin-bottom:0}.card-group>.card+.card{margin-left:0;border-left:0}.card-group>.card:first-child{border-top-right-radius:0;border-bottom-right-radius:0}.card-group>.card:first-child .card-header,.card-group>.card:first-child .card-img-top{border-top-right-radius:0}.card-group>.card:first-child .card-footer,.card-group>.card:first-child .card-img-bottom{border-bottom-right-radius:0}.card-group>.card:last-child{border-top-left-radius:0;border-bottom-left-radius:0}.card-group>.card:last-child .card-header,.card-group>.card:last-child .card-img-top{border-top-left-radius:0}.card-group>.card:last-child .card-footer,.card-group>.card:last-child .card-img-bottom{border-bottom-left-radius:0}.card-group>.card:only-child{border-radius:.25rem}.card-group>.card:only-child .card-header,.card-group>.card:only-child .card-img-top{border-top-left-radius:.25rem;border-top-right-radius:.25rem}.card-group>.card:only-child .card-footer,.card-group>.card:only-child .card-img-bottom{border-bottom-right-radius:.25rem;border-bottom-left-radius:.25rem}.card-group>.card:not(:first-child):not(:last-child):not(:only-child),.card-group>.card:not(:first-child):not(:last-child):not(:only-child) .card-footer,.card-group>.card:not(:first-child):not(:last-child):not(:only-child) .card-header,.card-group>.card:not(:first-child):not(:last-child):not(:only-child) .card-img-bottom,.card-group>.card:not(:first-child):not(:last-child):not(:only-child) .card-img-top{border-radius:0}}.card-columns .card{margin-bottom:.75rem}@media (min-width:576px){.card-columns{column-count:3;column-gap:1.25rem}.card-columns .card{display:inline-block;width:100%}}.breadcrumb{display:flex;flex-wrap:wrap;padding:.75rem 1rem;margin-bottom:1rem;list-style:none;background-color:#e9ecef;border-radius:.25rem}.breadcrumb-item+.breadcrumb-item:before{display:inline-block;padding-right:.5rem;padding-left:.5rem;color:#6c757d;content:"/"}.breadcrumb-item+.breadcrumb-item:hover:before{text-decoration:underline;text-decoration:none}.breadcrumb-item.active{color:#6c757d}.pagination{display:flex;padding-left:0;list-style:none;border-radius:.25rem}.page-link{position:relative;display:block;padding:.5rem .75rem;margin-left:0;line-height:1.25;color:#2196f3;background-color:transparent;border:0 solid #dee2e6}.page-link:hover{color:#0a6ebd;text-decoration:none;background-color:#e9ecef;border-color:#dee2e6}.page-link:focus{z-index:2;outline:0;box-shadow:0 0 0 .2rem rgba(33,150,243,.25)}.page-link:not(:disabled):not(.disabled){cursor:pointer}.page-item:first-child .page-link{margin-left:0;border-top-left-radius:.25rem;border-bottom-left-radius:.25rem}.page-item:last-child .page-link{border-top-right-radius:.25rem;border-bottom-right-radius:.25rem}.page-item.active .page-link{z-index:1;color:#fff;background-color:#2196f3;border-color:#2196f3}.page-item.disabled .page-link{color:#6c757d;pointer-events:none;cursor:auto;background-color:transparent;border-color:#dee2e6}.pagination-lg .page-link{padding:.75rem 0;font-size:1.25rem;line-height:1.5}.pagination-lg .page-item:first-child .page-link{border-top-left-radius:.3rem;border-bottom-left-radius:.3rem}.pagination-lg .page-item:last-child .page-link{border-top-right-radius:.3rem;border-bottom-right-radius:.3rem}.pagination-sm .page-link{padding:.25rem 0;font-size:.875rem;line-height:1.5}.pagination-sm .page-item:first-child .page-link{border-top-left-radius:.2rem;border-bottom-left-radius:.2rem}.pagination-sm .page-item:last-child .page-link{border-top-right-radius:.2rem;border-bottom-right-radius:.2rem}.jumbotron{padding:2rem 1rem;margin-bottom:2rem;background-color:#e9ecef;border-radius:.3rem}@media (min-width:576px){.jumbotron{padding:4rem 2rem}}.jumbotron-fluid{padding-right:0;padding-left:0;border-radius:0}.alert{padding:.75rem 1.25rem;margin-bottom:1rem;border:1px solid transparent;border-radius:.25rem}.alert-heading{color:inherit}.alert-link{font-weight:500}.alert-dismissible{padding-right:4rem}.alert-dismissible .close{position:absolute;top:0;right:0;padding:.75rem 1.25rem;color:inherit}.alert-primary{color:#114e7e;background-color:#d3eafd;border-color:#c1e2fc}.alert-primary hr{border-top-color:#a9d7fb}.alert-primary .alert-link{color:#0b3251}.alert-secondary{color:#383d41;background-color:#e2e3e5;border-color:#d6d8db}.alert-secondary hr{border-top-color:#c8cbcf}.alert-secondary .alert-link{color:#202326}.alert-success{color:#285b2a;background-color:#dbefdc;border-color:#cde9ce}.alert-success hr{border-top-color:#bbe1bd}.alert-success .alert-link{color:#18381a}.alert-info{color:#00626e;background-color:#ccf2f6;border-color:#b8ecf3}.alert-info hr{border-top-color:#a2e6ef}.alert-info .alert-link{color:#00353b}.alert-warning{color:#857a1f;background-color:#fffbd8;border-color:#fff9c8}.alert-warning hr{border-top-color:#fff6af}.alert-warning .alert-link{color:#5c5415}.alert-danger{color:#7f231c;background-color:#fdd9d7;border-color:#fccac7}.alert-danger hr{border-top-color:#fbb3af}.alert-danger .alert-link{color:#551713}.alert-light{color:#818182;background-color:#fefefe;border-color:#fdfdfe}.alert-light hr{border-top-color:#ececf6}.alert-light .alert-link{color:#686868}.alert-dark{color:#1b1e21;background-color:#d6d8d9;border-color:#c6c8ca}.alert-dark hr{border-top-color:#b9bbbe}.alert-dark .alert-link{color:#040505}@keyframes a{0%{background-position:1rem 0}to{background-position:0 0}}.progress{display:flex;height:1rem;overflow:hidden;font-size:.75rem;background-color:#e9ecef;border-radius:.25rem;box-shadow:inset 0 .1rem .1rem rgba(0,0,0,.1)}.progress-bar{display:flex;flex-direction:column;justify-content:center;color:#fff;text-align:center;background-color:#2196f3;transition:width .6s ease}.progress-bar-striped{background-image:linear-gradient(45deg,hsla(0,0%,100%,.15) 25%,transparent 0,transparent 50%,hsla(0,0%,100%,.15) 0,hsla(0,0%,100%,.15) 75%,transparent 0,transparent);background-size:1rem 1rem}.progress-bar-animated{animation:a 1s linear infinite}.media{display:flex;align-items:flex-start}.media-body{flex:1}.list-group{display:flex;flex-direction:column;padding-left:0;margin-bottom:0}.list-group-item-action{width:100%;color:#495057;text-align:inherit}.list-group-item-action:focus,.list-group-item-action:hover{color:#495057;text-decoration:none;background-color:#f8f9fa}.list-group-item-action:active{color:#212529;background-color:#e9ecef}.list-group-item{position:relative;display:block;padding:.75rem 1.25rem;margin-bottom:0;background-color:inherit;border:0 solid rgba(0,0,0,.125)}.list-group-item:first-child{border-top-left-radius:0;border-top-right-radius:0}.list-group-item:last-child{margin-bottom:0;border-bottom-right-radius:0;border-bottom-left-radius:0}.list-group-item:focus,.list-group-item:hover{z-index:1;text-decoration:none}.list-group-item.disabled,.list-group-item:disabled{color:#6c757d;background-color:inherit}.list-group-item.active{z-index:2;color:#fff;background-color:#2196f3;border-color:#2196f3}.list-group-flush .list-group-item{border-right:0;border-left:0;border-radius:0}.list-group-flush:first-child .list-group-item:first-child{border-top:0}.list-group-flush:last-child .list-group-item:last-child{border-bottom:0}.list-group-item-primary{color:#114e7e;background-color:#c1e2fc}.list-group-item-primary.list-group-item-action:focus,.list-group-item-primary.list-group-item-action:hover{color:#114e7e;background-color:#a9d7fb}.list-group-item-primary.list-group-item-action.active{color:#fff;background-color:#114e7e;border-color:#114e7e}.list-group-item-secondary{color:#383d41;background-color:#d6d8db}.list-group-item-secondary.list-group-item-action:focus,.list-group-item-secondary.list-group-item-action:hover{color:#383d41;background-color:#c8cbcf}.list-group-item-secondary.list-group-item-action.active{color:#fff;background-color:#383d41;border-color:#383d41}.list-group-item-success{color:#285b2a;background-color:#cde9ce}.list-group-item-success.list-group-item-action:focus,.list-group-item-success.list-group-item-action:hover{color:#285b2a;background-color:#bbe1bd}.list-group-item-success.list-group-item-action.active{color:#fff;background-color:#285b2a;border-color:#285b2a}.list-group-item-info{color:#00626e;background-color:#b8ecf3}.list-group-item-info.list-group-item-action:focus,.list-group-item-info.list-group-item-action:hover{color:#00626e;background-color:#a2e6ef}.list-group-item-info.list-group-item-action.active{color:#fff;background-color:#00626e;border-color:#00626e}.list-group-item-warning{color:#857a1f;background-color:#fff9c8}.list-group-item-warning.list-group-item-action:focus,.list-group-item-warning.list-group-item-action:hover{color:#857a1f;background-color:#fff6af}.list-group-item-warning.list-group-item-action.active{color:#fff;background-color:#857a1f;border-color:#857a1f}.list-group-item-danger{color:#7f231c;background-color:#fccac7}.list-group-item-danger.list-group-item-action:focus,.list-group-item-danger.list-group-item-action:hover{color:#7f231c;background-color:#fbb3af}.list-group-item-danger.list-group-item-action.active{color:#fff;background-color:#7f231c;border-color:#7f231c}.list-group-item-light{color:#818182;background-color:#fdfdfe}.list-group-item-light.list-group-item-action:focus,.list-group-item-light.list-group-item-action:hover{color:#818182;background-color:#ececf6}.list-group-item-light.list-group-item-action.active{color:#fff;background-color:#818182;border-color:#818182}.list-group-item-dark{color:#1b1e21;background-color:#c6c8ca}.list-group-item-dark.list-group-item-action:focus,.list-group-item-dark.list-group-item-action:hover{color:#1b1e21;background-color:#b9bbbe}.list-group-item-dark.list-group-item-action.active{color:#fff;background-color:#1b1e21;border-color:#1b1e21}.close{float:right;font-size:1.5rem;font-weight:500;line-height:1;color:#000;text-shadow:0 1px 0 #fff;opacity:.5}.close:focus,.close:hover{color:#000;text-decoration:none;opacity:.75}.close:not(:disabled):not(.disabled){cursor:pointer}button.close{padding:0;background-color:transparent;border:0;-webkit-appearance:none}.badge{padding:.25em .4em;font-size:75%;font-weight:500;line-height:1;text-align:center;white-space:nowrap;vertical-align:baseline;border-radius:.25rem}.badge:empty{display:none}.btn .badge{position:relative;top:-1px}.badge-pill{padding-right:.6em;padding-left:.6em;border-radius:10rem}.badge-primary{color:#fff;background-color:#2196f3}.badge-primary[href]:focus,.badge-primary[href]:hover{color:#fff;text-decoration:none;background-color:#0c7cd5}.badge-secondary{color:#fff;background-color:#6c757d}.badge-secondary[href]:focus,.badge-secondary[href]:hover{color:#fff;text-decoration:none;background-color:#545b62}.badge-success{color:#fff;background-color:#4caf50}.badge-success[href]:focus,.badge-success[href]:hover{color:#fff;text-decoration:none;background-color:#3d8b40}.badge-info{color:#fff;background-color:#00bcd4}.badge-info[href]:focus,.badge-info[href]:hover{color:#fff;text-decoration:none;background-color:#008fa1}.badge-warning{color:#212529;background-color:#ffeb3b}.badge-warning[href]:focus,.badge-warning[href]:hover{color:#212529;text-decoration:none;background-color:#ffe608}.badge-danger{color:#fff;background-color:#f44336}.badge-danger[href]:focus,.badge-danger[href]:hover{color:#fff;text-decoration:none;background-color:#ea1c0d}.badge-light{color:#212529;background-color:#f8f9fa}.badge-light[href]:focus,.badge-light[href]:hover{color:#212529;text-decoration:none;background-color:#dae0e5}.badge-dark{color:#fff;background-color:#343a40}.badge-dark[href]:focus,.badge-dark[href]:hover{color:#fff;text-decoration:none;background-color:#1d2124}.modal,.modal-open{overflow:hidden}.modal{position:fixed;top:0;right:0;bottom:0;left:0;z-index:1050;display:none;outline:0}.modal-open .modal{overflow-x:hidden;overflow-y:auto}.modal-dialog{position:relative;width:auto;margin:.5rem;pointer-events:none}.modal.fade .modal-dialog{transition:transform .3s ease-out;transform:translateY(-25%)}.modal.show .modal-dialog{transform:translate(0)}.modal-dialog-centered{display:flex;align-items:center;min-height:calc(100% - 1rem)}.modal-content{position:relative;display:flex;flex-direction:column;width:100%;pointer-events:auto;background-color:#fff;background-clip:padding-box;border:1px solid rgba(0,0,0,.2);border-radius:.3rem;box-shadow:0 .25rem .5rem rgba(0,0,0,.5);outline:0}.modal-backdrop{position:fixed;top:0;right:0;bottom:0;left:0;z-index:1040;background-color:#000}.modal-backdrop.fade{opacity:0}.modal-backdrop.show{opacity:.26}.modal-header{display:flex;align-items:flex-start;justify-content:space-between;padding:1rem;border-bottom:1px solid #e9ecef;border-top-left-radius:.3rem;border-top-right-radius:.3rem}.modal-header .close{padding:1rem;margin:-1rem -1rem -1rem auto}.modal-title{margin-bottom:0;line-height:1.5}.modal-body{position:relative;flex:1 1 auto;padding:1rem}.modal-footer{display:flex;align-items:center;justify-content:flex-end;padding:1rem;border-top:1px solid #e9ecef}.modal-footer>:not(:first-child){margin-left:.25rem}.modal-footer>:not(:last-child){margin-right:.25rem}.modal-scrollbar-measure{position:absolute;top:-9999px;width:50px;height:50px;overflow:scroll}@media (min-width:576px){.modal-dialog{max-width:500px;margin:1.75rem auto}.modal-dialog-centered{min-height:calc(100% - 3.5rem)}.modal-content{box-shadow:0 .5rem 1rem rgba(0,0,0,.5)}.modal-sm{max-width:300px}}@media (min-width:992px){.modal-lg{max-width:800px}}.tooltip{position:absolute;z-index:1070;display:block;margin:0;font-family:Roboto,Helvetica,Arial,sans-serif;font-style:normal;font-weight:400;line-height:1.5;text-align:left;text-align:start;text-decoration:none;text-shadow:none;text-transform:none;letter-spacing:normal;word-break:normal;word-spacing:normal;white-space:normal;line-break:auto;word-wrap:break-word}.tooltip.show{opacity:.9}.tooltip .arrow{position:absolute;display:block;width:.8rem;height:.4rem}.tooltip .arrow:before{position:absolute;content:"";border-color:transparent;border-style:solid}.bs-tooltip-auto[x-placement^=top],.bs-tooltip-top{padding:.4rem 0}.bs-tooltip-auto[x-placement^=top] .arrow,.bs-tooltip-top .arrow{bottom:0}.bs-tooltip-auto[x-placement^=top] .arrow:before,.bs-tooltip-top .arrow:before{top:0;border-width:.4rem .4rem 0;border-top-color:rgba(97,97,97,.9)}.bs-tooltip-auto[x-placement^=right],.bs-tooltip-right{padding:0 .4rem}.bs-tooltip-auto[x-placement^=right] .arrow,.bs-tooltip-right .arrow{left:0;width:.4rem;height:.8rem}.bs-tooltip-auto[x-placement^=right] .arrow:before,.bs-tooltip-right .arrow:before{right:0;border-width:.4rem .4rem .4rem 0;border-right-color:rgba(97,97,97,.9)}.bs-tooltip-auto[x-placement^=bottom],.bs-tooltip-bottom{padding:.4rem 0}.bs-tooltip-auto[x-placement^=bottom] .arrow,.bs-tooltip-bottom .arrow{top:0}.bs-tooltip-auto[x-placement^=bottom] .arrow:before,.bs-tooltip-bottom .arrow:before{bottom:0;border-width:0 .4rem .4rem;border-bottom-color:rgba(97,97,97,.9)}.bs-tooltip-auto[x-placement^=left],.bs-tooltip-left{padding:0 .4rem}.bs-tooltip-auto[x-placement^=left] .arrow,.bs-tooltip-left .arrow{right:0;width:.4rem;height:.8rem}.bs-tooltip-auto[x-placement^=left] .arrow:before,.bs-tooltip-left .arrow:before{left:0;border-width:.4rem 0 .4rem .4rem;border-left-color:rgba(97,97,97,.9)}.tooltip-inner{max-width:200px;padding:.25rem .5rem;color:#fff;text-align:center;background-color:rgba(97,97,97,.9);border-radius:.25rem}.popover{top:0;left:0;z-index:1060;max-width:276px;font-family:Roboto,Helvetica,Arial,sans-serif;font-style:normal;font-weight:400;line-height:1.5;text-align:left;text-align:start;text-decoration:none;text-shadow:none;text-transform:none;letter-spacing:normal;word-break:normal;word-spacing:normal;white-space:normal;line-break:auto;font-size:.875rem;word-wrap:break-word;background-color:#fff;background-clip:padding-box;border:1px solid rgba(0,0,0,.2);border-radius:.3rem;box-shadow:0 .25rem .5rem rgba(0,0,0,.2)}.popover,.popover .arrow{position:absolute;display:block}.popover .arrow{width:1rem;height:.5rem;margin:0 .3rem}.popover .arrow:after,.popover .arrow:before{position:absolute;display:block;content:"";border-color:transparent;border-style:solid}.bs-popover-auto[x-placement^=top],.bs-popover-top{margin-bottom:.5rem}.bs-popover-auto[x-placement^=top] .arrow,.bs-popover-top .arrow{bottom:calc((.5rem + 1px) * -1)}.bs-popover-auto[x-placement^=top] .arrow:after,.bs-popover-auto[x-placement^=top] .arrow:before,.bs-popover-top .arrow:after,.bs-popover-top .arrow:before{border-width:.5rem .5rem 0}.bs-popover-auto[x-placement^=top] .arrow:before,.bs-popover-top .arrow:before{bottom:0;border-top-color:rgba(0,0,0,.25)}.bs-popover-auto[x-placement^=top] .arrow:after,.bs-popover-top .arrow:after{bottom:1px;border-top-color:#fff}.bs-popover-auto[x-placement^=right],.bs-popover-right{margin-left:.5rem}.bs-popover-auto[x-placement^=right] .arrow,.bs-popover-right .arrow{left:calc((.5rem + 1px) * -1);width:.5rem;height:1rem;margin:.3rem 0}.bs-popover-auto[x-placement^=right] .arrow:after,.bs-popover-auto[x-placement^=right] .arrow:before,.bs-popover-right .arrow:after,.bs-popover-right .arrow:before{border-width:.5rem .5rem .5rem 0}.bs-popover-auto[x-placement^=right] .arrow:before,.bs-popover-right .arrow:before{left:0;border-right-color:rgba(0,0,0,.25)}.bs-popover-auto[x-placement^=right] .arrow:after,.bs-popover-right .arrow:after{left:1px;border-right-color:#fff}.bs-popover-auto[x-placement^=bottom],.bs-popover-bottom{margin-top:.5rem}.bs-popover-auto[x-placement^=bottom] .arrow,.bs-popover-bottom .arrow{top:calc((.5rem + 1px) * -1)}.bs-popover-auto[x-placement^=bottom] .arrow:after,.bs-popover-auto[x-placement^=bottom] .arrow:before,.bs-popover-bottom .arrow:after,.bs-popover-bottom .arrow:before{border-width:0 .5rem .5rem}.bs-popover-auto[x-placement^=bottom] .arrow:before,.bs-popover-bottom .arrow:before{top:0;border-bottom-color:rgba(0,0,0,.25)}.bs-popover-auto[x-placement^=bottom] .arrow:after,.bs-popover-bottom .arrow:after{top:1px;border-bottom-color:#fff}.bs-popover-auto[x-placement^=bottom] .popover-header:before,.bs-popover-bottom .popover-header:before{position:absolute;top:0;left:50%;display:block;width:1rem;margin-left:-.5rem;content:"";border-bottom:1px solid #f7f7f7}.bs-popover-auto[x-placement^=left],.bs-popover-left{margin-right:.5rem}.bs-popover-auto[x-placement^=left] .arrow,.bs-popover-left .arrow{right:calc((.5rem + 1px) * -1);width:.5rem;height:1rem;margin:.3rem 0}.bs-popover-auto[x-placement^=left] .arrow:after,.bs-popover-auto[x-placement^=left] .arrow:before,.bs-popover-left .arrow:after,.bs-popover-left .arrow:before{border-width:.5rem 0 .5rem .5rem}.bs-popover-auto[x-placement^=left] .arrow:before,.bs-popover-left .arrow:before{right:0;border-left-color:rgba(0,0,0,.25)}.bs-popover-auto[x-placement^=left] .arrow:after,.bs-popover-left .arrow:after{right:1px;border-left-color:#fff}.popover-header{padding:.5rem .75rem;margin-bottom:0;font-size:1rem;color:inherit;background-color:#f7f7f7;border-bottom:1px solid #ebebeb;border-top-left-radius:calc(.3rem - 1px);border-top-right-radius:calc(.3rem - 1px)}.popover-header:empty{display:none}.popover-body{padding:.5rem .75rem;color:#212529}.carousel{position:relative}.carousel-inner{position:relative;width:100%;overflow:hidden}.carousel-item{position:relative;display:none;align-items:center;width:100%;transition:transform .6s ease;backface-visibility:hidden;perspective:1000px}.carousel-item-next,.carousel-item-prev,.carousel-item.active{display:block}.carousel-item-next,.carousel-item-prev{position:absolute;top:0}.carousel-item-next.carousel-item-left,.carousel-item-prev.carousel-item-right{transform:translateX(0)}@supports (transform-style:preserve-3d){.carousel-item-next.carousel-item-left,.carousel-item-prev.carousel-item-right{transform:translateZ(0)}}.active.carousel-item-right,.carousel-item-next{transform:translateX(100%)}@supports (transform-style:preserve-3d){.active.carousel-item-right,.carousel-item-next{transform:translate3d(100%,0,0)}}.active.carousel-item-left,.carousel-item-prev{transform:translateX(-100%)}@supports (transform-style:preserve-3d){.active.carousel-item-left,.carousel-item-prev{transform:translate3d(-100%,0,0)}}.carousel-control-next,.carousel-control-prev{position:absolute;top:0;bottom:0;display:flex;align-items:center;justify-content:center;width:15%;color:#fff;text-align:center;opacity:.5}.carousel-control-next:focus,.carousel-control-next:hover,.carousel-control-prev:focus,.carousel-control-prev:hover{color:#fff;text-decoration:none;outline:0;opacity:.9}.carousel-control-prev{left:0}.carousel-control-next{right:0}.carousel-control-next-icon,.carousel-control-prev-icon{display:inline-block;width:20px;height:20px;background:transparent no-repeat 50%;background-size:100% 100%}.carousel-control-prev-icon{background-image:url("data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' fill='%23ffffff' viewBox='0 0 8 8'%3E%3Cpath d='M5.25 0l-4 4 4 4 1.5-1.5-2.5-2.5 2.5-2.5-1.5-1.5z'/%3E%3C/svg%3E")}.carousel-control-next-icon{background-image:url("data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' fill='%23ffffff' viewBox='0 0 8 8'%3E%3Cpath d='M2.75 0l-1.5 1.5 2.5 2.5-2.5 2.5 1.5 1.5 4-4-4-4z'/%3E%3C/svg%3E")}.carousel-indicators{position:absolute;right:0;bottom:10px;left:0;z-index:15;display:flex;justify-content:center;padding-left:0;margin-right:15%;margin-left:15%;list-style:none}.carousel-indicators li{position:relative;flex:0 1 auto;width:30px;height:3px;margin-right:3px;margin-left:3px;text-indent:-999px;background-color:hsla(0,0%,100%,.5)}.carousel-indicators li:before{top:-10px}.carousel-indicators li:after,.carousel-indicators li:before{position:absolute;left:0;display:inline-block;width:100%;height:10px;content:""}.carousel-indicators li:after{bottom:-10px}.carousel-indicators .active{background-color:#fff}.carousel-caption{position:absolute;right:15%;bottom:20px;left:15%;z-index:10;padding-top:20px;padding-bottom:20px;color:#fff;text-align:center}.align-baseline{vertical-align:baseline!important}.align-top{vertical-align:top!important}.align-middle{vertical-align:middle!important}.align-bottom{vertical-align:bottom!important}.align-text-bottom{vertical-align:text-bottom!important}.align-text-top{vertical-align:text-top!important}.bg-primary{background-color:#2196f3!important}a.bg-primary:focus,a.bg-primary:hover,button.bg-primary:focus,button.bg-primary:hover{background-color:#0c7cd5!important}.bg-secondary{background-color:#6c757d!important}a.bg-secondary:focus,a.bg-secondary:hover,button.bg-secondary:focus,button.bg-secondary:hover{background-color:#545b62!important}.bg-success{background-color:#4caf50!important}a.bg-success:focus,a.bg-success:hover,button.bg-success:focus,button.bg-success:hover{background-color:#3d8b40!important}.bg-info{background-color:#00bcd4!important}a.bg-info:focus,a.bg-info:hover,button.bg-info:focus,button.bg-info:hover{background-color:#008fa1!important}.bg-warning{background-color:#ffeb3b!important}a.bg-warning:focus,a.bg-warning:hover,button.bg-warning:focus,button.bg-warning:hover{background-color:#ffe608!important}.bg-danger{background-color:#f44336!important}a.bg-danger:focus,a.bg-danger:hover,button.bg-danger:focus,button.bg-danger:hover{background-color:#ea1c0d!important}.bg-light{background-color:#f8f9fa!important}a.bg-light:focus,a.bg-light:hover,button.bg-light:focus,button.bg-light:hover{background-color:#dae0e5!important}.bg-dark{background-color:#343a40!important}a.bg-dark:focus,a.bg-dark:hover,button.bg-dark:focus,button.bg-dark:hover{background-color:#1d2124!important}.bg-white{background-color:#fff!important}.bg-transparent{background-color:transparent!important}.border{border:1px solid #dee2e6!important}.border-top{border-top:1px solid #dee2e6!important}.border-right{border-right:1px solid #dee2e6!important}.border-bottom{border-bottom:1px solid #dee2e6!important}.border-left{border-left:1px solid #dee2e6!important}.border-0{border:0!important}.border-top-0{border-top:0!important}.border-right-0{border-right:0!important}.border-bottom-0{border-bottom:0!important}.border-left-0{border-left:0!important}.border-primary{border-color:#2196f3!important}.border-secondary{border-color:#6c757d!important}.border-success{border-color:#4caf50!important}.border-info{border-color:#00bcd4!important}.border-warning{border-color:#ffeb3b!important}.border-danger{border-color:#f44336!important}.border-light{border-color:#f8f9fa!important}.border-dark{border-color:#343a40!important}.border-white{border-color:#fff!important}.rounded{border-radius:.25rem!important}.rounded-top{border-top-left-radius:.25rem!important}.rounded-right,.rounded-top{border-top-right-radius:.25rem!important}.rounded-bottom,.rounded-right{border-bottom-right-radius:.25rem!important}.rounded-bottom,.rounded-left{border-bottom-left-radius:.25rem!important}.rounded-left{border-top-left-radius:.25rem!important}.rounded-circle{border-radius:50%!important}.rounded-0{border-radius:0!important}.clearfix:after{display:block;clear:both;content:""}.d-none{display:none!important}.d-inline{display:inline!important}.d-inline-block{display:inline-block!important}.d-block{display:block!important}.d-table{display:table!important}.d-table-row{display:table-row!important}.d-table-cell{display:table-cell!important}.d-flex{display:flex!important}.d-inline-flex{display:inline-flex!important}@media (min-width:576px){.d-sm-none{display:none!important}.d-sm-inline{display:inline!important}.d-sm-inline-block{display:inline-block!important}.d-sm-block{display:block!important}.d-sm-table{display:table!important}.d-sm-table-row{display:table-row!important}.d-sm-table-cell{display:table-cell!important}.d-sm-flex{display:flex!important}.d-sm-inline-flex{display:inline-flex!important}}@media (min-width:768px){.d-md-none{display:none!important}.d-md-inline{display:inline!important}.d-md-inline-block{display:inline-block!important}.d-md-block{display:block!important}.d-md-table{display:table!important}.d-md-table-row{display:table-row!important}.d-md-table-cell{display:table-cell!important}.d-md-flex{display:flex!important}.d-md-inline-flex{display:inline-flex!important}}@media (min-width:992px){.d-lg-none{display:none!important}.d-lg-inline{display:inline!important}.d-lg-inline-block{display:inline-block!important}.d-lg-block{display:block!important}.d-lg-table{display:table!important}.d-lg-table-row{display:table-row!important}.d-lg-table-cell{display:table-cell!important}.d-lg-flex{display:flex!important}.d-lg-inline-flex{display:inline-flex!important}}@media (min-width:1200px){.d-xl-none{display:none!important}.d-xl-inline{display:inline!important}.d-xl-inline-block{display:inline-block!important}.d-xl-block{display:block!important}.d-xl-table{display:table!important}.d-xl-table-row{display:table-row!important}.d-xl-table-cell{display:table-cell!important}.d-xl-flex{display:flex!important}.d-xl-inline-flex{display:inline-flex!important}}@media print{.d-print-none{display:none!important}.d-print-inline{display:inline!important}.d-print-inline-block{display:inline-block!important}.d-print-block{display:block!important}.d-print-table{display:table!important}.d-print-table-row{display:table-row!important}.d-print-table-cell{display:table-cell!important}.d-print-flex{display:flex!important}.d-print-inline-flex{display:inline-flex!important}}.embed-responsive{position:relative;display:block;width:100%;padding:0;overflow:hidden}.embed-responsive:before{display:block;content:""}.embed-responsive .embed-responsive-item,.embed-responsive embed,.embed-responsive iframe,.embed-responsive object,.embed-responsive video{position:absolute;top:0;bottom:0;left:0;width:100%;height:100%;border:0}.embed-responsive-21by9:before{padding-top:42.857143%}.embed-responsive-16by9:before{padding-top:56.25%}.embed-responsive-4by3:before{padding-top:75%}.embed-responsive-1by1:before{padding-top:100%}.flex-row{flex-direction:row!important}.flex-column{flex-direction:column!important}.flex-row-reverse{flex-direction:row-reverse!important}.flex-column-reverse{flex-direction:column-reverse!important}.flex-wrap{flex-wrap:wrap!important}.flex-nowrap{flex-wrap:nowrap!important}.flex-wrap-reverse{flex-wrap:wrap-reverse!important}.justify-content-start{justify-content:flex-start!important}.justify-content-end{justify-content:flex-end!important}.justify-content-center{justify-content:center!important}.justify-content-between{justify-content:space-between!important}.justify-content-around{justify-content:space-around!important}.align-items-start{align-items:flex-start!important}.align-items-end{align-items:flex-end!important}.align-items-center{align-items:center!important}.align-items-baseline{align-items:baseline!important}.align-items-stretch{align-items:stretch!important}.align-content-start{align-content:flex-start!important}.align-content-end{align-content:flex-end!important}.align-content-center{align-content:center!important}.align-content-between{align-content:space-between!important}.align-content-around{align-content:space-around!important}.align-content-stretch{align-content:stretch!important}.align-self-auto{align-self:auto!important}.align-self-start{align-self:flex-start!important}.align-self-end{align-self:flex-end!important}.align-self-center{align-self:center!important}.align-self-baseline{align-self:baseline!important}.align-self-stretch{align-self:stretch!important}@media (min-width:576px){.flex-sm-row{flex-direction:row!important}.flex-sm-column{flex-direction:column!important}.flex-sm-row-reverse{flex-direction:row-reverse!important}.flex-sm-column-reverse{flex-direction:column-reverse!important}.flex-sm-wrap{flex-wrap:wrap!important}.flex-sm-nowrap{flex-wrap:nowrap!important}.flex-sm-wrap-reverse{flex-wrap:wrap-reverse!important}.justify-content-sm-start{justify-content:flex-start!important}.justify-content-sm-end{justify-content:flex-end!important}.justify-content-sm-center{justify-content:center!important}.justify-content-sm-between{justify-content:space-between!important}.justify-content-sm-around{justify-content:space-around!important}.align-items-sm-start{align-items:flex-start!important}.align-items-sm-end{align-items:flex-end!important}.align-items-sm-center{align-items:center!important}.align-items-sm-baseline{align-items:baseline!important}.align-items-sm-stretch{align-items:stretch!important}.align-content-sm-start{align-content:flex-start!important}.align-content-sm-end{align-content:flex-end!important}.align-content-sm-center{align-content:center!important}.align-content-sm-between{align-content:space-between!important}.align-content-sm-around{align-content:space-around!important}.align-content-sm-stretch{align-content:stretch!important}.align-self-sm-auto{align-self:auto!important}.align-self-sm-start{align-self:flex-start!important}.align-self-sm-end{align-self:flex-end!important}.align-self-sm-center{align-self:center!important}.align-self-sm-baseline{align-self:baseline!important}.align-self-sm-stretch{align-self:stretch!important}}@media (min-width:768px){.flex-md-row{flex-direction:row!important}.flex-md-column{flex-direction:column!important}.flex-md-row-reverse{flex-direction:row-reverse!important}.flex-md-column-reverse{flex-direction:column-reverse!important}.flex-md-wrap{flex-wrap:wrap!important}.flex-md-nowrap{flex-wrap:nowrap!important}.flex-md-wrap-reverse{flex-wrap:wrap-reverse!important}.justify-content-md-start{justify-content:flex-start!important}.justify-content-md-end{justify-content:flex-end!important}.justify-content-md-center{justify-content:center!important}.justify-content-md-between{justify-content:space-between!important}.justify-content-md-around{justify-content:space-around!important}.align-items-md-start{align-items:flex-start!important}.align-items-md-end{align-items:flex-end!important}.align-items-md-center{align-items:center!important}.align-items-md-baseline{align-items:baseline!important}.align-items-md-stretch{align-items:stretch!important}.align-content-md-start{align-content:flex-start!important}.align-content-md-end{align-content:flex-end!important}.align-content-md-center{align-content:center!important}.align-content-md-between{align-content:space-between!important}.align-content-md-around{align-content:space-around!important}.align-content-md-stretch{align-content:stretch!important}.align-self-md-auto{align-self:auto!important}.align-self-md-start{align-self:flex-start!important}.align-self-md-end{align-self:flex-end!important}.align-self-md-center{align-self:center!important}.align-self-md-baseline{align-self:baseline!important}.align-self-md-stretch{align-self:stretch!important}}@media (min-width:992px){.flex-lg-row{flex-direction:row!important}.flex-lg-column{flex-direction:column!important}.flex-lg-row-reverse{flex-direction:row-reverse!important}.flex-lg-column-reverse{flex-direction:column-reverse!important}.flex-lg-wrap{flex-wrap:wrap!important}.flex-lg-nowrap{flex-wrap:nowrap!important}.flex-lg-wrap-reverse{flex-wrap:wrap-reverse!important}.justify-content-lg-start{justify-content:flex-start!important}.justify-content-lg-end{justify-content:flex-end!important}.justify-content-lg-center{justify-content:center!important}.justify-content-lg-between{justify-content:space-between!important}.justify-content-lg-around{justify-content:space-around!important}.align-items-lg-start{align-items:flex-start!important}.align-items-lg-end{align-items:flex-end!important}.align-items-lg-center{align-items:center!important}.align-items-lg-baseline{align-items:baseline!important}.align-items-lg-stretch{align-items:stretch!important}.align-content-lg-start{align-content:flex-start!important}.align-content-lg-end{align-content:flex-end!important}.align-content-lg-center{align-content:center!important}.align-content-lg-between{align-content:space-between!important}.align-content-lg-around{align-content:space-around!important}.align-content-lg-stretch{align-content:stretch!important}.align-self-lg-auto{align-self:auto!important}.align-self-lg-start{align-self:flex-start!important}.align-self-lg-end{align-self:flex-end!important}.align-self-lg-center{align-self:center!important}.align-self-lg-baseline{align-self:baseline!important}.align-self-lg-stretch{align-self:stretch!important}}@media (min-width:1200px){.flex-xl-row{flex-direction:row!important}.flex-xl-column{flex-direction:column!important}.flex-xl-row-reverse{flex-direction:row-reverse!important}.flex-xl-column-reverse{flex-direction:column-reverse!important}.flex-xl-wrap{flex-wrap:wrap!important}.flex-xl-nowrap{flex-wrap:nowrap!important}.flex-xl-wrap-reverse{flex-wrap:wrap-reverse!important}.justify-content-xl-start{justify-content:flex-start!important}.justify-content-xl-end{justify-content:flex-end!important}.justify-content-xl-center{justify-content:center!important}.justify-content-xl-between{justify-content:space-between!important}.justify-content-xl-around{justify-content:space-around!important}.align-items-xl-start{align-items:flex-start!important}.align-items-xl-end{align-items:flex-end!important}.align-items-xl-center{align-items:center!important}.align-items-xl-baseline{align-items:baseline!important}.align-items-xl-stretch{align-items:stretch!important}.align-content-xl-start{align-content:flex-start!important}.align-content-xl-end{align-content:flex-end!important}.align-content-xl-center{align-content:center!important}.align-content-xl-between{align-content:space-between!important}.align-content-xl-around{align-content:space-around!important}.align-content-xl-stretch{align-content:stretch!important}.align-self-xl-auto{align-self:auto!important}.align-self-xl-start{align-self:flex-start!important}.align-self-xl-end{align-self:flex-end!important}.align-self-xl-center{align-self:center!important}.align-self-xl-baseline{align-self:baseline!important}.align-self-xl-stretch{align-self:stretch!important}}.float-left{float:left!important}.float-right{float:right!important}.float-none{float:none!important}@media (min-width:576px){.float-sm-left{float:left!important}.float-sm-right{float:right!important}.float-sm-none{float:none!important}}@media (min-width:768px){.float-md-left{float:left!important}.float-md-right{float:right!important}.float-md-none{float:none!important}}@media (min-width:992px){.float-lg-left{float:left!important}.float-lg-right{float:right!important}.float-lg-none{float:none!important}}@media (min-width:1200px){.float-xl-left{float:left!important}.float-xl-right{float:right!important}.float-xl-none{float:none!important}}.position-static{position:static!important}.position-relative{position:relative!important}.position-absolute{position:absolute!important}.position-fixed{position:fixed!important}.position-sticky{position:sticky!important}.fixed-top{top:0}.fixed-bottom,.fixed-top{position:fixed;right:0;left:0;z-index:1030}.fixed-bottom{bottom:0}@supports (position:sticky){.sticky-top{position:sticky;top:0;z-index:1020}}.bootstrap-datetimepicker-widget .btn[data-action=clear]:after,.bootstrap-datetimepicker-widget .btn[data-action=decrementHours]:after,.bootstrap-datetimepicker-widget .btn[data-action=decrementMinutes]:after,.bootstrap-datetimepicker-widget .btn[data-action=incrementHours]:after,.bootstrap-datetimepicker-widget .btn[data-action=incrementMinutes]:after,.bootstrap-datetimepicker-widget .btn[data-action=showHours]:after,.bootstrap-datetimepicker-widget .btn[data-action=showMinutes]:after,.bootstrap-datetimepicker-widget .btn[data-action=today]:after,.bootstrap-datetimepicker-widget .btn[data-action=togglePeriod]:after,.bootstrap-datetimepicker-widget .picker-switch:after,.bootstrap-datetimepicker-widget table th.next:after,.bootstrap-datetimepicker-widget table th.prev:after,.sr-only{white-space:nowrap;clip-path:inset(50%)}.sr-only-focusable:active,.sr-only-focusable:focus{position:static;width:auto;height:auto;overflow:visible;clip:auto;white-space:normal;clip-path:none}.w-25{width:25%!important}.w-50{width:50%!important}.w-75{width:75%!important}.w-100{width:100%!important}.h-25{height:25%!important}.h-50{height:50%!important}.h-75{height:75%!important}.h-100{height:100%!important}.mw-100{max-width:100%!important}.mh-100{max-height:100%!important}.m-0{margin:0!important}.mt-0,.my-0{margin-top:0!important}.mr-0,.mx-0{margin-right:0!important}.mb-0,.my-0{margin-bottom:0!important}.ml-0,.mx-0{margin-left:0!important}.m-1{margin:.25rem!important}.mt-1,.my-1{margin-top:.25rem!important}.mr-1,.mx-1{margin-right:.25rem!important}.mb-1,.my-1{margin-bottom:.25rem!important}.ml-1,.mx-1{margin-left:.25rem!important}.m-2{margin:.5rem!important}.mt-2,.my-2{margin-top:.5rem!important}.mr-2,.mx-2{margin-right:.5rem!important}.mb-2,.my-2{margin-bottom:.5rem!important}.ml-2,.mx-2{margin-left:.5rem!important}.m-3{margin:1rem!important}.mt-3,.my-3{margin-top:1rem!important}.mr-3,.mx-3{margin-right:1rem!important}.mb-3,.my-3{margin-bottom:1rem!important}.ml-3,.mx-3{margin-left:1rem!important}.m-4{margin:1.5rem!important}.mt-4,.my-4{margin-top:1.5rem!important}.mr-4,.mx-4{margin-right:1.5rem!important}.mb-4,.my-4{margin-bottom:1.5rem!important}.ml-4,.mx-4{margin-left:1.5rem!important}.m-5{margin:3rem!important}.mt-5,.my-5{margin-top:3rem!important}.mr-5,.mx-5{margin-right:3rem!important}.mb-5,.my-5{margin-bottom:3rem!important}.ml-5,.mx-5{margin-left:3rem!important}.p-0{padding:0!important}.pt-0,.py-0{padding-top:0!important}.pr-0,.px-0{padding-right:0!important}.pb-0,.py-0{padding-bottom:0!important}.pl-0,.px-0{padding-left:0!important}.p-1{padding:.25rem!important}.pt-1,.py-1{padding-top:.25rem!important}.pr-1,.px-1{padding-right:.25rem!important}.pb-1,.py-1{padding-bottom:.25rem!important}.pl-1,.px-1{padding-left:.25rem!important}.p-2{padding:.5rem!important}.pt-2,.py-2{padding-top:.5rem!important}.pr-2,.px-2{padding-right:.5rem!important}.pb-2,.py-2{padding-bottom:.5rem!important}.pl-2,.px-2{padding-left:.5rem!important}.p-3{padding:1rem!important}.pt-3,.py-3{padding-top:1rem!important}.pr-3,.px-3{padding-right:1rem!important}.pb-3,.py-3{padding-bottom:1rem!important}.pl-3,.px-3{padding-left:1rem!important}.p-4{padding:1.5rem!important}.pt-4,.py-4{padding-top:1.5rem!important}.pr-4,.px-4{padding-right:1.5rem!important}.pb-4,.py-4{padding-bottom:1.5rem!important}.pl-4,.px-4{padding-left:1.5rem!important}.p-5{padding:3rem!important}.pt-5,.py-5{padding-top:3rem!important}.pr-5,.px-5{padding-right:3rem!important}.pb-5,.py-5{padding-bottom:3rem!important}.pl-5,.px-5{padding-left:3rem!important}.m-auto{margin:auto!important}.mt-auto,.my-auto{margin-top:auto!important}.mr-auto,.mx-auto{margin-right:auto!important}.mb-auto,.my-auto{margin-bottom:auto!important}.ml-auto,.mx-auto{margin-left:auto!important}@media (min-width:576px){.m-sm-0{margin:0!important}.mt-sm-0,.my-sm-0{margin-top:0!important}.mr-sm-0,.mx-sm-0{margin-right:0!important}.mb-sm-0,.my-sm-0{margin-bottom:0!important}.ml-sm-0,.mx-sm-0{margin-left:0!important}.m-sm-1{margin:.25rem!important}.mt-sm-1,.my-sm-1{margin-top:.25rem!important}.mr-sm-1,.mx-sm-1{margin-right:.25rem!important}.mb-sm-1,.my-sm-1{margin-bottom:.25rem!important}.ml-sm-1,.mx-sm-1{margin-left:.25rem!important}.m-sm-2{margin:.5rem!important}.mt-sm-2,.my-sm-2{margin-top:.5rem!important}.mr-sm-2,.mx-sm-2{margin-right:.5rem!important}.mb-sm-2,.my-sm-2{margin-bottom:.5rem!important}.ml-sm-2,.mx-sm-2{margin-left:.5rem!important}.m-sm-3{margin:1rem!important}.mt-sm-3,.my-sm-3{margin-top:1rem!important}.mr-sm-3,.mx-sm-3{margin-right:1rem!important}.mb-sm-3,.my-sm-3{margin-bottom:1rem!important}.ml-sm-3,.mx-sm-3{margin-left:1rem!important}.m-sm-4{margin:1.5rem!important}.mt-sm-4,.my-sm-4{margin-top:1.5rem!important}.mr-sm-4,.mx-sm-4{margin-right:1.5rem!important}.mb-sm-4,.my-sm-4{margin-bottom:1.5rem!important}.ml-sm-4,.mx-sm-4{margin-left:1.5rem!important}.m-sm-5{margin:3rem!important}.mt-sm-5,.my-sm-5{margin-top:3rem!important}.mr-sm-5,.mx-sm-5{margin-right:3rem!important}.mb-sm-5,.my-sm-5{margin-bottom:3rem!important}.ml-sm-5,.mx-sm-5{margin-left:3rem!important}.p-sm-0{padding:0!important}.pt-sm-0,.py-sm-0{padding-top:0!important}.pr-sm-0,.px-sm-0{padding-right:0!important}.pb-sm-0,.py-sm-0{padding-bottom:0!important}.pl-sm-0,.px-sm-0{padding-left:0!important}.p-sm-1{padding:.25rem!important}.pt-sm-1,.py-sm-1{padding-top:.25rem!important}.pr-sm-1,.px-sm-1{padding-right:.25rem!important}.pb-sm-1,.py-sm-1{padding-bottom:.25rem!important}.pl-sm-1,.px-sm-1{padding-left:.25rem!important}.p-sm-2{padding:.5rem!important}.pt-sm-2,.py-sm-2{padding-top:.5rem!important}.pr-sm-2,.px-sm-2{padding-right:.5rem!important}.pb-sm-2,.py-sm-2{padding-bottom:.5rem!important}.pl-sm-2,.px-sm-2{padding-left:.5rem!important}.p-sm-3{padding:1rem!important}.pt-sm-3,.py-sm-3{padding-top:1rem!important}.pr-sm-3,.px-sm-3{padding-right:1rem!important}.pb-sm-3,.py-sm-3{padding-bottom:1rem!important}.pl-sm-3,.px-sm-3{padding-left:1rem!important}.p-sm-4{padding:1.5rem!important}.pt-sm-4,.py-sm-4{padding-top:1.5rem!important}.pr-sm-4,.px-sm-4{padding-right:1.5rem!important}.pb-sm-4,.py-sm-4{padding-bottom:1.5rem!important}.pl-sm-4,.px-sm-4{padding-left:1.5rem!important}.p-sm-5{padding:3rem!important}.pt-sm-5,.py-sm-5{padding-top:3rem!important}.pr-sm-5,.px-sm-5{padding-right:3rem!important}.pb-sm-5,.py-sm-5{padding-bottom:3rem!important}.pl-sm-5,.px-sm-5{padding-left:3rem!important}.m-sm-auto{margin:auto!important}.mt-sm-auto,.my-sm-auto{margin-top:auto!important}.mr-sm-auto,.mx-sm-auto{margin-right:auto!important}.mb-sm-auto,.my-sm-auto{margin-bottom:auto!important}.ml-sm-auto,.mx-sm-auto{margin-left:auto!important}}@media (min-width:768px){.m-md-0{margin:0!important}.mt-md-0,.my-md-0{margin-top:0!important}.mr-md-0,.mx-md-0{margin-right:0!important}.mb-md-0,.my-md-0{margin-bottom:0!important}.ml-md-0,.mx-md-0{margin-left:0!important}.m-md-1{margin:.25rem!important}.mt-md-1,.my-md-1{margin-top:.25rem!important}.mr-md-1,.mx-md-1{margin-right:.25rem!important}.mb-md-1,.my-md-1{margin-bottom:.25rem!important}.ml-md-1,.mx-md-1{margin-left:.25rem!important}.m-md-2{margin:.5rem!important}.mt-md-2,.my-md-2{margin-top:.5rem!important}.mr-md-2,.mx-md-2{margin-right:.5rem!important}.mb-md-2,.my-md-2{margin-bottom:.5rem!important}.ml-md-2,.mx-md-2{margin-left:.5rem!important}.m-md-3{margin:1rem!important}.mt-md-3,.my-md-3{margin-top:1rem!important}.mr-md-3,.mx-md-3{margin-right:1rem!important}.mb-md-3,.my-md-3{margin-bottom:1rem!important}.ml-md-3,.mx-md-3{margin-left:1rem!important}.m-md-4{margin:1.5rem!important}.mt-md-4,.my-md-4{margin-top:1.5rem!important}.mr-md-4,.mx-md-4{margin-right:1.5rem!important}.mb-md-4,.my-md-4{margin-bottom:1.5rem!important}.ml-md-4,.mx-md-4{margin-left:1.5rem!important}.m-md-5{margin:3rem!important}.mt-md-5,.my-md-5{margin-top:3rem!important}.mr-md-5,.mx-md-5{margin-right:3rem!important}.mb-md-5,.my-md-5{margin-bottom:3rem!important}.ml-md-5,.mx-md-5{margin-left:3rem!important}.p-md-0{padding:0!important}.pt-md-0,.py-md-0{padding-top:0!important}.pr-md-0,.px-md-0{padding-right:0!important}.pb-md-0,.py-md-0{padding-bottom:0!important}.pl-md-0,.px-md-0{padding-left:0!important}.p-md-1{padding:.25rem!important}.pt-md-1,.py-md-1{padding-top:.25rem!important}.pr-md-1,.px-md-1{padding-right:.25rem!important}.pb-md-1,.py-md-1{padding-bottom:.25rem!important}.pl-md-1,.px-md-1{padding-left:.25rem!important}.p-md-2{padding:.5rem!important}.pt-md-2,.py-md-2{padding-top:.5rem!important}.pr-md-2,.px-md-2{padding-right:.5rem!important}.pb-md-2,.py-md-2{padding-bottom:.5rem!important}.pl-md-2,.px-md-2{padding-left:.5rem!important}.p-md-3{padding:1rem!important}.pt-md-3,.py-md-3{padding-top:1rem!important}.pr-md-3,.px-md-3{padding-right:1rem!important}.pb-md-3,.py-md-3{padding-bottom:1rem!important}.pl-md-3,.px-md-3{padding-left:1rem!important}.p-md-4{padding:1.5rem!important}.pt-md-4,.py-md-4{padding-top:1.5rem!important}.pr-md-4,.px-md-4{padding-right:1.5rem!important}.pb-md-4,.py-md-4{padding-bottom:1.5rem!important}.pl-md-4,.px-md-4{padding-left:1.5rem!important}.p-md-5{padding:3rem!important}.pt-md-5,.py-md-5{padding-top:3rem!important}.pr-md-5,.px-md-5{padding-right:3rem!important}.pb-md-5,.py-md-5{padding-bottom:3rem!important}.pl-md-5,.px-md-5{padding-left:3rem!important}.m-md-auto{margin:auto!important}.mt-md-auto,.my-md-auto{margin-top:auto!important}.mr-md-auto,.mx-md-auto{margin-right:auto!important}.mb-md-auto,.my-md-auto{margin-bottom:auto!important}.ml-md-auto,.mx-md-auto{margin-left:auto!important}}@media (min-width:992px){.m-lg-0{margin:0!important}.mt-lg-0,.my-lg-0{margin-top:0!important}.mr-lg-0,.mx-lg-0{margin-right:0!important}.mb-lg-0,.my-lg-0{margin-bottom:0!important}.ml-lg-0,.mx-lg-0{margin-left:0!important}.m-lg-1{margin:.25rem!important}.mt-lg-1,.my-lg-1{margin-top:.25rem!important}.mr-lg-1,.mx-lg-1{margin-right:.25rem!important}.mb-lg-1,.my-lg-1{margin-bottom:.25rem!important}.ml-lg-1,.mx-lg-1{margin-left:.25rem!important}.m-lg-2{margin:.5rem!important}.mt-lg-2,.my-lg-2{margin-top:.5rem!important}.mr-lg-2,.mx-lg-2{margin-right:.5rem!important}.mb-lg-2,.my-lg-2{margin-bottom:.5rem!important}.ml-lg-2,.mx-lg-2{margin-left:.5rem!important}.m-lg-3{margin:1rem!important}.mt-lg-3,.my-lg-3{margin-top:1rem!important}.mr-lg-3,.mx-lg-3{margin-right:1rem!important}.mb-lg-3,.my-lg-3{margin-bottom:1rem!important}.ml-lg-3,.mx-lg-3{margin-left:1rem!important}.m-lg-4{margin:1.5rem!important}.mt-lg-4,.my-lg-4{margin-top:1.5rem!important}.mr-lg-4,.mx-lg-4{margin-right:1.5rem!important}.mb-lg-4,.my-lg-4{margin-bottom:1.5rem!important}.ml-lg-4,.mx-lg-4{margin-left:1.5rem!important}.m-lg-5{margin:3rem!important}.mt-lg-5,.my-lg-5{margin-top:3rem!important}.mr-lg-5,.mx-lg-5{margin-right:3rem!important}.mb-lg-5,.my-lg-5{margin-bottom:3rem!important}.ml-lg-5,.mx-lg-5{margin-left:3rem!important}.p-lg-0{padding:0!important}.pt-lg-0,.py-lg-0{padding-top:0!important}.pr-lg-0,.px-lg-0{padding-right:0!important}.pb-lg-0,.py-lg-0{padding-bottom:0!important}.pl-lg-0,.px-lg-0{padding-left:0!important}.p-lg-1{padding:.25rem!important}.pt-lg-1,.py-lg-1{padding-top:.25rem!important}.pr-lg-1,.px-lg-1{padding-right:.25rem!important}.pb-lg-1,.py-lg-1{padding-bottom:.25rem!important}.pl-lg-1,.px-lg-1{padding-left:.25rem!important}.p-lg-2{padding:.5rem!important}.pt-lg-2,.py-lg-2{padding-top:.5rem!important}.pr-lg-2,.px-lg-2{padding-right:.5rem!important}.pb-lg-2,.py-lg-2{padding-bottom:.5rem!important}.pl-lg-2,.px-lg-2{padding-left:.5rem!important}.p-lg-3{padding:1rem!important}.pt-lg-3,.py-lg-3{padding-top:1rem!important}.pr-lg-3,.px-lg-3{padding-right:1rem!important}.pb-lg-3,.py-lg-3{padding-bottom:1rem!important}.pl-lg-3,.px-lg-3{padding-left:1rem!important}.p-lg-4{padding:1.5rem!important}.pt-lg-4,.py-lg-4{padding-top:1.5rem!important}.pr-lg-4,.px-lg-4{padding-right:1.5rem!important}.pb-lg-4,.py-lg-4{padding-bottom:1.5rem!important}.pl-lg-4,.px-lg-4{padding-left:1.5rem!important}.p-lg-5{padding:3rem!important}.pt-lg-5,.py-lg-5{padding-top:3rem!important}.pr-lg-5,.px-lg-5{padding-right:3rem!important}.pb-lg-5,.py-lg-5{padding-bottom:3rem!important}.pl-lg-5,.px-lg-5{padding-left:3rem!important}.m-lg-auto{margin:auto!important}.mt-lg-auto,.my-lg-auto{margin-top:auto!important}.mr-lg-auto,.mx-lg-auto{margin-right:auto!important}.mb-lg-auto,.my-lg-auto{margin-bottom:auto!important}.ml-lg-auto,.mx-lg-auto{margin-left:auto!important}}@media (min-width:1200px){.m-xl-0{margin:0!important}.mt-xl-0,.my-xl-0{margin-top:0!important}.mr-xl-0,.mx-xl-0{margin-right:0!important}.mb-xl-0,.my-xl-0{margin-bottom:0!important}.ml-xl-0,.mx-xl-0{margin-left:0!important}.m-xl-1{margin:.25rem!important}.mt-xl-1,.my-xl-1{margin-top:.25rem!important}.mr-xl-1,.mx-xl-1{margin-right:.25rem!important}.mb-xl-1,.my-xl-1{margin-bottom:.25rem!important}.ml-xl-1,.mx-xl-1{margin-left:.25rem!important}.m-xl-2{margin:.5rem!important}.mt-xl-2,.my-xl-2{margin-top:.5rem!important}.mr-xl-2,.mx-xl-2{margin-right:.5rem!important}.mb-xl-2,.my-xl-2{margin-bottom:.5rem!important}.ml-xl-2,.mx-xl-2{margin-left:.5rem!important}.m-xl-3{margin:1rem!important}.mt-xl-3,.my-xl-3{margin-top:1rem!important}.mr-xl-3,.mx-xl-3{margin-right:1rem!important}.mb-xl-3,.my-xl-3{margin-bottom:1rem!important}.ml-xl-3,.mx-xl-3{margin-left:1rem!important}.m-xl-4{margin:1.5rem!important}.mt-xl-4,.my-xl-4{margin-top:1.5rem!important}.mr-xl-4,.mx-xl-4{margin-right:1.5rem!important}.mb-xl-4,.my-xl-4{margin-bottom:1.5rem!important}.ml-xl-4,.mx-xl-4{margin-left:1.5rem!important}.m-xl-5{margin:3rem!important}.mt-xl-5,.my-xl-5{margin-top:3rem!important}.mr-xl-5,.mx-xl-5{margin-right:3rem!important}.mb-xl-5,.my-xl-5{margin-bottom:3rem!important}.ml-xl-5,.mx-xl-5{margin-left:3rem!important}.p-xl-0{padding:0!important}.pt-xl-0,.py-xl-0{padding-top:0!important}.pr-xl-0,.px-xl-0{padding-right:0!important}.pb-xl-0,.py-xl-0{padding-bottom:0!important}.pl-xl-0,.px-xl-0{padding-left:0!important}.p-xl-1{padding:.25rem!important}.pt-xl-1,.py-xl-1{padding-top:.25rem!important}.pr-xl-1,.px-xl-1{padding-right:.25rem!important}.pb-xl-1,.py-xl-1{padding-bottom:.25rem!important}.pl-xl-1,.px-xl-1{padding-left:.25rem!important}.p-xl-2{padding:.5rem!important}.pt-xl-2,.py-xl-2{padding-top:.5rem!important}.pr-xl-2,.px-xl-2{padding-right:.5rem!important}.pb-xl-2,.py-xl-2{padding-bottom:.5rem!important}.pl-xl-2,.px-xl-2{padding-left:.5rem!important}.p-xl-3{padding:1rem!important}.pt-xl-3,.py-xl-3{padding-top:1rem!important}.pr-xl-3,.px-xl-3{padding-right:1rem!important}.pb-xl-3,.py-xl-3{padding-bottom:1rem!important}.pl-xl-3,.px-xl-3{padding-left:1rem!important}.p-xl-4{padding:1.5rem!important}.pt-xl-4,.py-xl-4{padding-top:1.5rem!important}.pr-xl-4,.px-xl-4{padding-right:1.5rem!important}.pb-xl-4,.py-xl-4{padding-bottom:1.5rem!important}.pl-xl-4,.px-xl-4{padding-left:1.5rem!important}.p-xl-5{padding:3rem!important}.pt-xl-5,.py-xl-5{padding-top:3rem!important}.pr-xl-5,.px-xl-5{padding-right:3rem!important}.pb-xl-5,.py-xl-5{padding-bottom:3rem!important}.pl-xl-5,.px-xl-5{padding-left:3rem!important}.m-xl-auto{margin:auto!important}.mt-xl-auto,.my-xl-auto{margin-top:auto!important}.mr-xl-auto,.mx-xl-auto{margin-right:auto!important}.mb-xl-auto,.my-xl-auto{margin-bottom:auto!important}.ml-xl-auto,.mx-xl-auto{margin-left:auto!important}}.text-justify{text-align:justify!important}.text-nowrap{white-space:nowrap!important}.text-truncate{overflow:hidden;text-overflow:ellipsis;white-space:nowrap}.text-left{text-align:left!important}.text-right{text-align:right!important}.text-center{text-align:center!important}@media (min-width:576px){.text-sm-left{text-align:left!important}.text-sm-right{text-align:right!important}.text-sm-center{text-align:center!important}}@media (min-width:768px){.text-md-left{text-align:left!important}.text-md-right{text-align:right!important}.text-md-center{text-align:center!important}}@media (min-width:992px){.text-lg-left{text-align:left!important}.text-lg-right{text-align:right!important}.text-lg-center{text-align:center!important}}@media (min-width:1200px){.text-xl-left{text-align:left!important}.text-xl-right{text-align:right!important}.text-xl-center{text-align:center!important}}.text-lowercase{text-transform:lowercase!important}.text-uppercase{text-transform:uppercase!important}.text-capitalize{text-transform:capitalize!important}.font-weight-light{font-weight:300!important}.font-weight-normal{font-weight:400!important}.font-weight-bold{font-weight:500!important}.font-italic{font-style:italic!important}.text-white{color:#fff!important}.text-primary{color:#2196f3!important}a.text-primary:focus,a.text-primary:hover{color:#0c7cd5!important}.text-secondary{color:#6c757d!important}a.text-secondary:focus,a.text-secondary:hover{color:#545b62!important}a.text-success:focus,a.text-success:hover{color:#3d8b40!important}a.text-info:focus,a.text-info:hover{color:#008fa1!important}.text-warning{color:#ffeb3b!important}a.text-warning:focus,a.text-warning:hover{color:#ffe608!important}a.text-danger:focus,a.text-danger:hover{color:#ea1c0d!important}.text-light{color:#f8f9fa!important}a.text-light:focus,a.text-light:hover{color:#dae0e5!important}.text-dark{color:#343a40!important}a.text-dark:focus,a.text-dark:hover{color:#1d2124!important}.bmd-help,.text-muted{color:#6c757d!important}.text-hide{font:0/0 a;color:transparent;text-shadow:none;background-color:transparent;border:0}.visible{visibility:visible!important}.invisible{visibility:hidden!important}.btn{position:relative;padding:12px 30px;margin:.3125rem 1px;font-size:.75rem;font-weight:400;line-height:1.428571;text-decoration:none;text-transform:uppercase;letter-spacing:0;cursor:pointer;background-color:transparent;border:0;border-radius:.2rem;transition:box-shadow .2s cubic-bezier(.4,0,1,1),background-color .2s cubic-bezier(.4,0,.2,1);will-change:box-shadow,transform}.btn,.btn.active.focus,.btn.active:focus,.btn.focus,.btn:active.focus,.btn:active:focus,.btn:focus{outline:0}.btn.btn-primary{color:#fff;background-color:#9c27b0;border-color:#9c27b0;box-shadow:0 2px 2px 0 rgba(156,39,176,.14),0 3px 1px -2px rgba(156,39,176,.2),0 1px 5px 0 rgba(156,39,176,.12)}.btn.btn-primary.focus,.btn.btn-primary:focus,.btn.btn-primary:hover{color:#fff;background-color:#9124a3;border-color:#701c7e}.btn.btn-primary.active,.btn.btn-primary:active,.open>.btn.btn-primary.dropdown-toggle,.show>.btn.btn-primary.dropdown-toggle{color:#fff;background-color:#9124a3;border-color:#701c7e;box-shadow:0 2px 2px 0 rgba(156,39,176,.14),0 3px 1px -2px rgba(156,39,176,.2),0 1px 5px 0 rgba(156,39,176,.12)}.btn.btn-primary.active.focus,.btn.btn-primary.active:focus,.btn.btn-primary.active:hover,.btn.btn-primary:active.focus,.btn.btn-primary:active:focus,.btn.btn-primary:active:hover,.open>.btn.btn-primary.dropdown-toggle.focus,.open>.btn.btn-primary.dropdown-toggle:focus,.open>.btn.btn-primary.dropdown-toggle:hover,.show>.btn.btn-primary.dropdown-toggle.focus,.show>.btn.btn-primary.dropdown-toggle:focus,.show>.btn.btn-primary.dropdown-toggle:hover{color:#fff;background-color:#9124a3;border-color:#3f1048}.open>.btn.btn-primary.dropdown-toggle.bmd-btn-icon{color:inherit;background-color:#9c27b0}.open>.btn.btn-primary.dropdown-toggle.bmd-btn-icon:hover{background-color:#9124a3}.btn.btn-primary.disabled.focus,.btn.btn-primary.disabled:focus,.btn.btn-primary.disabled:hover,.btn.btn-primary:disabled.focus,.btn.btn-primary:disabled:focus,.btn.btn-primary:disabled:hover{background-color:#9c27b0;border-color:#9c27b0}.btn.btn-primary:active,.btn.btn-primary:focus,.btn.btn-primary:hover{box-shadow:0 14px 26px -12px rgba(156,39,176,.42),0 4px 23px 0 rgba(0,0,0,.12),0 8px 10px -5px rgba(156,39,176,.2)}.btn.btn-primary.btn-link{box-shadow:none}.btn.btn-primary.btn-link,.btn.btn-primary.btn-link:active,.btn.btn-primary.btn-link:focus,.btn.btn-primary.btn-link:hover{background-color:transparent;color:#9c27b0}.btn.btn-secondary{color:#333;background-color:#fafafa;border-color:#ccc;box-shadow:0 2px 2px 0 hsla(0,0%,98%,.14),0 3px 1px -2px hsla(0,0%,98%,.2),0 1px 5px 0 hsla(0,0%,98%,.12)}.btn.btn-secondary.focus,.btn.btn-secondary:focus,.btn.btn-secondary:hover{color:#333;background-color:#f2f2f2;border-color:#adadad}.btn.btn-secondary.active,.btn.btn-secondary:active,.open>.btn.btn-secondary.dropdown-toggle,.show>.btn.btn-secondary.dropdown-toggle{color:#333;background-color:#f2f2f2;border-color:#adadad;box-shadow:0 2px 2px 0 hsla(0,0%,98%,.14),0 3px 1px -2px hsla(0,0%,98%,.2),0 1px 5px 0 hsla(0,0%,98%,.12)}.btn.btn-secondary.active.focus,.btn.btn-secondary.active:focus,.btn.btn-secondary.active:hover,.btn.btn-secondary:active.focus,.btn.btn-secondary:active:focus,.btn.btn-secondary:active:hover,.open>.btn.btn-secondary.dropdown-toggle.focus,.open>.btn.btn-secondary.dropdown-toggle:focus,.open>.btn.btn-secondary.dropdown-toggle:hover,.show>.btn.btn-secondary.dropdown-toggle.focus,.show>.btn.btn-secondary.dropdown-toggle:focus,.show>.btn.btn-secondary.dropdown-toggle:hover{color:#333;background-color:#f2f2f2;border-color:#8c8c8c}.open>.btn.btn-secondary.dropdown-toggle.bmd-btn-icon{color:inherit;background-color:#fafafa}.open>.btn.btn-secondary.dropdown-toggle.bmd-btn-icon:hover{background-color:#f2f2f2}.btn.btn-secondary.disabled.focus,.btn.btn-secondary.disabled:focus,.btn.btn-secondary.disabled:hover,.btn.btn-secondary:disabled.focus,.btn.btn-secondary:disabled:focus,.btn.btn-secondary:disabled:hover{background-color:#fafafa;border-color:#ccc}.btn.btn-secondary:active,.btn.btn-secondary:focus,.btn.btn-secondary:hover{box-shadow:0 14px 26px -12px hsla(0,0%,98%,.42),0 4px 23px 0 rgba(0,0,0,.12),0 8px 10px -5px hsla(0,0%,98%,.2)}.btn.btn-secondary.btn-link{box-shadow:none}.btn.btn-secondary.btn-link,.btn.btn-secondary.btn-link:active,.btn.btn-secondary.btn-link:focus,.btn.btn-secondary.btn-link:hover{background-color:transparent;color:#fafafa}.btn.btn-info{color:#fff;background-color:#00bcd4;border-color:#00bcd4;box-shadow:0 2px 2px 0 rgba(0,188,212,.14),0 3px 1px -2px rgba(0,188,212,.2),0 1px 5px 0 rgba(0,188,212,.12)}.btn.btn-info.focus,.btn.btn-info:focus,.btn.btn-info:hover{color:#fff;background-color:#00aec5;border-color:#008697}.btn.btn-info.active,.btn.btn-info:active,.open>.btn.btn-info.dropdown-toggle,.show>.btn.btn-info.dropdown-toggle{color:#fff;background-color:#00aec5;border-color:#008697;box-shadow:0 2px 2px 0 rgba(0,188,212,.14),0 3px 1px -2px rgba(0,188,212,.2),0 1px 5px 0 rgba(0,188,212,.12)}.btn.btn-info.active.focus,.btn.btn-info.active:focus,.btn.btn-info.active:hover,.btn.btn-info:active.focus,.btn.btn-info:active:focus,.btn.btn-info:active:hover,.open>.btn.btn-info.dropdown-toggle.focus,.open>.btn.btn-info.dropdown-toggle:focus,.open>.btn.btn-info.dropdown-toggle:hover,.show>.btn.btn-info.dropdown-toggle.focus,.show>.btn.btn-info.dropdown-toggle:focus,.show>.btn.btn-info.dropdown-toggle:hover{color:#fff;background-color:#00aec5;border-color:#004b55}.open>.btn.btn-info.dropdown-toggle.bmd-btn-icon{color:inherit;background-color:#00bcd4}.open>.btn.btn-info.dropdown-toggle.bmd-btn-icon:hover{background-color:#00aec5}.btn.btn-info.disabled.focus,.btn.btn-info.disabled:focus,.btn.btn-info.disabled:hover,.btn.btn-info:disabled.focus,.btn.btn-info:disabled:focus,.btn.btn-info:disabled:hover{background-color:#00bcd4;border-color:#00bcd4}.btn.btn-info:active,.btn.btn-info:focus,.btn.btn-info:hover{box-shadow:0 14px 26px -12px rgba(0,188,212,.42),0 4px 23px 0 rgba(0,0,0,.12),0 8px 10px -5px rgba(0,188,212,.2)}.btn.btn-info.btn-link{box-shadow:none}.btn.btn-info.btn-link,.btn.btn-info.btn-link:active,.btn.btn-info.btn-link:focus,.btn.btn-info.btn-link:hover{background-color:transparent;color:#00bcd4}.btn.btn-success{color:#fff;background-color:#4caf50;border-color:#4caf50;box-shadow:0 2px 2px 0 rgba(76,175,80,.14),0 3px 1px -2px rgba(76,175,80,.2),0 1px 5px 0 rgba(76,175,80,.12)}.btn.btn-success.focus,.btn.btn-success:focus,.btn.btn-success:hover{color:#fff;background-color:#47a44b;border-color:#39843c}.btn.btn-success.active,.btn.btn-success:active,.open>.btn.btn-success.dropdown-toggle,.show>.btn.btn-success.dropdown-toggle{color:#fff;background-color:#47a44b;border-color:#39843c;box-shadow:0 2px 2px 0 rgba(76,175,80,.14),0 3px 1px -2px rgba(76,175,80,.2),0 1px 5px 0 rgba(76,175,80,.12)}.btn.btn-success.active.focus,.btn.btn-success.active:focus,.btn.btn-success.active:hover,.btn.btn-success:active.focus,.btn.btn-success:active:focus,.btn.btn-success:active:hover,.open>.btn.btn-success.dropdown-toggle.focus,.open>.btn.btn-success.dropdown-toggle:focus,.open>.btn.btn-success.dropdown-toggle:hover,.show>.btn.btn-success.dropdown-toggle.focus,.show>.btn.btn-success.dropdown-toggle:focus,.show>.btn.btn-success.dropdown-toggle:hover{color:#fff;background-color:#47a44b;border-color:#255627}.open>.btn.btn-success.dropdown-toggle.bmd-btn-icon{color:inherit;background-color:#4caf50}.open>.btn.btn-success.dropdown-toggle.bmd-btn-icon:hover{background-color:#47a44b}.btn.btn-success.disabled.focus,.btn.btn-success.disabled:focus,.btn.btn-success.disabled:hover,.btn.btn-success:disabled.focus,.btn.btn-success:disabled:focus,.btn.btn-success:disabled:hover{background-color:#4caf50;border-color:#4caf50}.btn.btn-success:active,.btn.btn-success:focus,.btn.btn-success:hover{box-shadow:0 14px 26px -12px rgba(76,175,80,.42),0 4px 23px 0 rgba(0,0,0,.12),0 8px 10px -5px rgba(76,175,80,.2)}.btn.btn-success.btn-link{box-shadow:none}.btn.btn-success.btn-link,.btn.btn-success.btn-link:active,.btn.btn-success.btn-link:focus,.btn.btn-success.btn-link:hover{background-color:transparent;color:#4caf50}.btn.btn-warning{color:#fff;background-color:#ff9800;border-color:#ff9800;box-shadow:0 2px 2px 0 rgba(255,152,0,.14),0 3px 1px -2px rgba(255,152,0,.2),0 1px 5px 0 rgba(255,152,0,.12)}.btn.btn-warning.focus,.btn.btn-warning:focus,.btn.btn-warning:hover{color:#fff;background-color:#f08f00;border-color:#c27400}.btn.btn-warning.active,.btn.btn-warning:active,.open>.btn.btn-warning.dropdown-toggle,.show>.btn.btn-warning.dropdown-toggle{color:#fff;background-color:#f08f00;border-color:#c27400;box-shadow:0 2px 2px 0 rgba(255,152,0,.14),0 3px 1px -2px rgba(255,152,0,.2),0 1px 5px 0 rgba(255,152,0,.12)}.btn.btn-warning.active.focus,.btn.btn-warning.active:focus,.btn.btn-warning.active:hover,.btn.btn-warning:active.focus,.btn.btn-warning:active:focus,.btn.btn-warning:active:hover,.open>.btn.btn-warning.dropdown-toggle.focus,.open>.btn.btn-warning.dropdown-toggle:focus,.open>.btn.btn-warning.dropdown-toggle:hover,.show>.btn.btn-warning.dropdown-toggle.focus,.show>.btn.btn-warning.dropdown-toggle:focus,.show>.btn.btn-warning.dropdown-toggle:hover{color:#fff;background-color:#f08f00;border-color:#804c00}.open>.btn.btn-warning.dropdown-toggle.bmd-btn-icon{color:inherit;background-color:#ff9800}.open>.btn.btn-warning.dropdown-toggle.bmd-btn-icon:hover{background-color:#f08f00}.btn.btn-warning.disabled.focus,.btn.btn-warning.disabled:focus,.btn.btn-warning.disabled:hover,.btn.btn-warning:disabled.focus,.btn.btn-warning:disabled:focus,.btn.btn-warning:disabled:hover{background-color:#ff9800;border-color:#ff9800}.btn.btn-warning:active,.btn.btn-warning:focus,.btn.btn-warning:hover{box-shadow:0 14px 26px -12px rgba(255,152,0,.42),0 4px 23px 0 rgba(0,0,0,.12),0 8px 10px -5px rgba(255,152,0,.2)}.btn.btn-warning.btn-link{box-shadow:none}.btn.btn-warning.btn-link,.btn.btn-warning.btn-link:active,.btn.btn-warning.btn-link:focus,.btn.btn-warning.btn-link:hover{background-color:transparent;color:#ff9800}.btn.btn-danger{color:#fff;background-color:#f44336;border-color:#f44336;box-shadow:0 2px 2px 0 rgba(244,67,54,.14),0 3px 1px -2px rgba(244,67,54,.2),0 1px 5px 0 rgba(244,67,54,.12)}.btn.btn-danger.focus,.btn.btn-danger:focus,.btn.btn-danger:hover{color:#fff;background-color:#f33527;border-color:#e11b0c}.btn.btn-danger.active,.btn.btn-danger:active,.open>.btn.btn-danger.dropdown-toggle,.show>.btn.btn-danger.dropdown-toggle{color:#fff;background-color:#f33527;border-color:#e11b0c;box-shadow:0 2px 2px 0 rgba(244,67,54,.14),0 3px 1px -2px rgba(244,67,54,.2),0 1px 5px 0 rgba(244,67,54,.12)}.btn.btn-danger.active.focus,.btn.btn-danger.active:focus,.btn.btn-danger.active:hover,.btn.btn-danger:active.focus,.btn.btn-danger:active:focus,.btn.btn-danger:active:hover,.open>.btn.btn-danger.dropdown-toggle.focus,.open>.btn.btn-danger.dropdown-toggle:focus,.open>.btn.btn-danger.dropdown-toggle:hover,.show>.btn.btn-danger.dropdown-toggle.focus,.show>.btn.btn-danger.dropdown-toggle:focus,.show>.btn.btn-danger.dropdown-toggle:hover{color:#fff;background-color:#f33527;border-color:#a21309}.open>.btn.btn-danger.dropdown-toggle.bmd-btn-icon{color:inherit;background-color:#f44336}.open>.btn.btn-danger.dropdown-toggle.bmd-btn-icon:hover{background-color:#f33527}.btn.btn-danger.disabled.focus,.btn.btn-danger.disabled:focus,.btn.btn-danger.disabled:hover,.btn.btn-danger:disabled.focus,.btn.btn-danger:disabled:focus,.btn.btn-danger:disabled:hover{background-color:#f44336;border-color:#f44336}.btn.btn-danger:active,.btn.btn-danger:focus,.btn.btn-danger:hover{box-shadow:0 14px 26px -12px rgba(244,67,54,.42),0 4px 23px 0 rgba(0,0,0,.12),0 8px 10px -5px rgba(244,67,54,.2)}.btn.btn-danger.btn-link{box-shadow:none}.btn.btn-danger.btn-link,.btn.btn-danger.btn-link:active,.btn.btn-danger.btn-link:focus,.btn.btn-danger.btn-link:hover{background-color:transparent;color:#f44336}.btn.btn-rose{color:#fff;background-color:#e91e63;border-color:#e91e63;box-shadow:0 2px 2px 0 rgba(233,30,99,.14),0 3px 1px -2px rgba(233,30,99,.2),0 1px 5px 0 rgba(233,30,99,.12)}.btn.btn-rose.focus,.btn.btn-rose:focus,.btn.btn-rose:hover{color:#fff;background-color:#ea2c6d;border-color:#b8124a}.btn.btn-rose.active,.btn.btn-rose:active,.open>.btn.btn-rose.dropdown-toggle,.show>.btn.btn-rose.dropdown-toggle{color:#fff;background-color:#ea2c6d;border-color:#b8124a;box-shadow:0 2px 2px 0 rgba(233,30,99,.14),0 3px 1px -2px rgba(233,30,99,.2),0 1px 5px 0 rgba(233,30,99,.12)}.btn.btn-rose.active.focus,.btn.btn-rose.active:focus,.btn.btn-rose.active:hover,.btn.btn-rose:active.focus,.btn.btn-rose:active:focus,.btn.btn-rose:active:hover,.open>.btn.btn-rose.dropdown-toggle.focus,.open>.btn.btn-rose.dropdown-toggle:focus,.open>.btn.btn-rose.dropdown-toggle:hover,.show>.btn.btn-rose.dropdown-toggle.focus,.show>.btn.btn-rose.dropdown-toggle:focus,.show>.btn.btn-rose.dropdown-toggle:hover{color:#fff;background-color:#ea2c6d;border-color:#7b0c32}.open>.btn.btn-rose.dropdown-toggle.bmd-btn-icon{color:inherit;background-color:#e91e63}.open>.btn.btn-rose.dropdown-toggle.bmd-btn-icon:hover{background-color:#ea2c6d}.btn.btn-rose.disabled.focus,.btn.btn-rose.disabled:focus,.btn.btn-rose.disabled:hover,.btn.btn-rose:disabled.focus,.btn.btn-rose:disabled:focus,.btn.btn-rose:disabled:hover{background-color:#e91e63;border-color:#e91e63}.btn.btn-rose:active,.btn.btn-rose:focus,.btn.btn-rose:hover{box-shadow:0 14px 26px -12px rgba(233,30,99,.42),0 4px 23px 0 rgba(0,0,0,.12),0 8px 10px -5px rgba(233,30,99,.2)}.btn.btn-rose.btn-link{box-shadow:none}.btn.btn-rose.btn-link,.btn.btn-rose.btn-link:active,.btn.btn-rose.btn-link:focus,.btn.btn-rose.btn-link:hover{background-color:transparent;color:#e91e63}.btn,.btn.btn-default{color:#fff;background-color:#999;border-color:#999;box-shadow:0 2px 2px 0 hsla(0,0%,60%,.14),0 3px 1px -2px hsla(0,0%,60%,.2),0 1px 5px 0 hsla(0,0%,60%,.12)}.btn.btn-default.focus,.btn.btn-default:focus,.btn.btn-default:hover,.btn.focus,.btn:focus,.btn:hover{color:#fff;background-color:#919191;border-color:#7a7a7a}.btn.active,.btn.btn-default.active,.btn.btn-default:active,.btn:active,.open>.btn.btn-default.dropdown-toggle,.open>.btn.dropdown-toggle,.show>.btn.btn-default.dropdown-toggle,.show>.btn.dropdown-toggle{color:#fff;background-color:#919191;border-color:#7a7a7a;box-shadow:0 2px 2px 0 hsla(0,0%,60%,.14),0 3px 1px -2px hsla(0,0%,60%,.2),0 1px 5px 0 hsla(0,0%,60%,.12)}.btn.active.focus,.btn.active:focus,.btn.active:hover,.btn.btn-default.active.focus,.btn.btn-default.active:focus,.btn.btn-default.active:hover,.btn.btn-default:active.focus,.btn.btn-default:active:focus,.btn.btn-default:active:hover,.btn:active.focus,.btn:active:focus,.btn:active:hover,.open>.btn.btn-default.dropdown-toggle.focus,.open>.btn.btn-default.dropdown-toggle:focus,.open>.btn.btn-default.dropdown-toggle:hover,.open>.btn.dropdown-toggle.focus,.open>.btn.dropdown-toggle:focus,.open>.btn.dropdown-toggle:hover,.show>.btn.btn-default.dropdown-toggle.focus,.show>.btn.btn-default.dropdown-toggle:focus,.show>.btn.btn-default.dropdown-toggle:hover,.show>.btn.dropdown-toggle.focus,.show>.btn.dropdown-toggle:focus,.show>.btn.dropdown-toggle:hover{color:#fff;background-color:#919191;border-color:#595959}.open>.btn.btn-default.dropdown-toggle.bmd-btn-icon,.open>.btn.dropdown-toggle.bmd-btn-icon{color:inherit;background-color:#999}.open>.btn.btn-default.dropdown-toggle.bmd-btn-icon:hover,.open>.btn.dropdown-toggle.bmd-btn-icon:hover{background-color:#919191}.btn.btn-default.disabled.focus,.btn.btn-default.disabled:focus,.btn.btn-default.disabled:hover,.btn.btn-default:disabled.focus,.btn.btn-default:disabled:focus,.btn.btn-default:disabled:hover,.btn.disabled.focus,.btn.disabled:focus,.btn.disabled:hover,.btn:disabled.focus,.btn:disabled:focus,.btn:disabled:hover{background-color:#999;border-color:#999}.btn.btn-default:active,.btn.btn-default:focus,.btn.btn-default:hover,.btn:active,.btn:focus,.btn:hover{box-shadow:0 14px 26px -12px hsla(0,0%,60%,.42),0 4px 23px 0 rgba(0,0,0,.12),0 8px 10px -5px hsla(0,0%,60%,.2)}.btn.btn-default.btn-link,.btn.btn-link{background-color:transparent;color:#999;box-shadow:none}.btn.btn-default.btn-link:active,.btn.btn-default.btn-link:focus,.btn.btn-default.btn-link:hover,.btn.btn-link:active,.btn.btn-link:focus,.btn.btn-link:hover{background-color:transparent;color:#999}.btn.btn-white,.btn.btn-white:focus,.btn.btn-white:hover{background-color:#fff;color:#999}.btn.btn-white.btn-link{color:#fff;background:transparent;box-shadow:none}.btn.btn-link:active,.btn.btn-link:focus,.btn.btn-link:hover{text-decoration:none!important}.btn-group-raised .btn.btn-link,.btn-group-raised .btn.btn-link.active,.btn-group-raised .btn.btn-link:active,.btn-group-raised .btn.btn-link:focus,.btn-group-raised .btn.btn-link:hover,.btn-group-raised .btn.disabled,.btn-group-raised .btn:disabled,.btn-group-raised .btn[disabled],.btn.btn-raised.btn-link,.btn.btn-raised.btn-link.active,.btn.btn-raised.btn-link:active,.btn.btn-raised.btn-link:focus,.btn.btn-raised.btn-link:hover,.btn.btn-raised.disabled,.btn.btn-raised:disabled,.btn.btn-raised[disabled],fieldset[disabled][disabled] .btn-group-raised .btn,fieldset[disabled][disabled] .btn.btn-raised{box-shadow:none}.btn.btn-outline,.btn.btn-outline-danger,.btn.btn-outline-info,.btn.btn-outline-primary,.btn.btn-outline-secondary,.btn.btn-outline-success,.btn.btn-outline-warning{border:1px solid currentColor}.btn.btn-outline{color:#333;background-color:transparent;border-color:#333}.btn.btn-outline.focus,.btn.btn-outline:focus,.btn.btn-outline:hover{color:#333;background-color:hsla(0,0%,60%,.2);border-color:#333}.btn.btn-outline.active,.btn.btn-outline:active,.open>.btn.btn-outline.dropdown-toggle,.show>.btn.btn-outline.dropdown-toggle{color:#333;background-color:hsla(0,0%,60%,.2);border-color:#333;box-shadow:0 2px 2px 0 rgba(0,0,0,.14),0 3px 1px -2px rgba(0,0,0,.2),0 1px 5px 0 rgba(0,0,0,.12)}.btn.btn-outline.active.focus,.btn.btn-outline.active:focus,.btn.btn-outline.active:hover,.btn.btn-outline:active.focus,.btn.btn-outline:active:focus,.btn.btn-outline:active:hover,.open>.btn.btn-outline.dropdown-toggle.focus,.open>.btn.btn-outline.dropdown-toggle:focus,.open>.btn.btn-outline.dropdown-toggle:hover,.show>.btn.btn-outline.dropdown-toggle.focus,.show>.btn.btn-outline.dropdown-toggle:focus,.show>.btn.btn-outline.dropdown-toggle:hover{color:#333;background-color:hsla(0,0%,60%,.4);border-color:#333}.open>.btn.btn-outline.dropdown-toggle.bmd-btn-icon{color:inherit;background-color:transparent}.open>.btn.btn-outline.dropdown-toggle.bmd-btn-icon:hover{background-color:hsla(0,0%,60%,.2)}.bg-inverse .btn.btn-outline,.btn.btn-outline.disabled.focus,.btn.btn-outline.disabled:focus,.btn.btn-outline.disabled:hover,.btn.btn-outline:disabled.focus,.btn.btn-outline:disabled:focus,.btn.btn-outline:disabled:hover{background-color:transparent;border-color:#333}.bg-inverse .btn.btn-outline{color:#333}.bg-inverse .btn.btn-outline.focus,.bg-inverse .btn.btn-outline:focus,.bg-inverse .btn.btn-outline:hover{color:#333;background-color:hsla(0,0%,80%,.15);border-color:hsla(0,0%,80%,.15)}.bg-inverse .btn.btn-outline.active,.bg-inverse .btn.btn-outline:active,.open>.bg-inverse .btn.btn-outline.dropdown-toggle,.show>.bg-inverse .btn.btn-outline.dropdown-toggle{color:#333;background-color:hsla(0,0%,80%,.15);border-color:hsla(0,0%,80%,.15);box-shadow:0 2px 2px 0 rgba(0,0,0,.14),0 3px 1px -2px rgba(0,0,0,.2),0 1px 5px 0 rgba(0,0,0,.12)}.bg-inverse .btn.btn-outline.active.focus,.bg-inverse .btn.btn-outline.active:focus,.bg-inverse .btn.btn-outline.active:hover,.bg-inverse .btn.btn-outline:active.focus,.bg-inverse .btn.btn-outline:active:focus,.bg-inverse .btn.btn-outline:active:hover,.open>.bg-inverse .btn.btn-outline.dropdown-toggle.focus,.open>.bg-inverse .btn.btn-outline.dropdown-toggle:focus,.open>.bg-inverse .btn.btn-outline.dropdown-toggle:hover,.show>.bg-inverse .btn.btn-outline.dropdown-toggle.focus,.show>.bg-inverse .btn.btn-outline.dropdown-toggle:focus,.show>.bg-inverse .btn.btn-outline.dropdown-toggle:hover{color:#333;background-color:hsla(0,0%,80%,.25);border-color:hsla(0,0%,80%,.25)}.open>.bg-inverse .btn.btn-outline.dropdown-toggle.bmd-btn-icon{color:inherit;background-color:transparent}.open>.bg-inverse .btn.btn-outline.dropdown-toggle.bmd-btn-icon:hover{background-color:hsla(0,0%,80%,.15)}.bg-inverse .btn.btn-outline.disabled.focus,.bg-inverse .btn.btn-outline.disabled:focus,.bg-inverse .btn.btn-outline.disabled:hover,.bg-inverse .btn.btn-outline:disabled.focus,.bg-inverse .btn.btn-outline:disabled:focus,.bg-inverse .btn.btn-outline:disabled:hover{background-color:transparent;border-color:#333}.btn.btn-outline.btn-link{background-color:transparent}.btn.btn-outline-primary{color:#9c27b0;background-color:transparent;border-color:#9c27b0}.btn.btn-outline-primary.focus,.btn.btn-outline-primary:focus,.btn.btn-outline-primary:hover{color:#9c27b0;background-color:hsla(0,0%,60%,.2);border-color:#9c27b0}.btn.btn-outline-primary.active,.btn.btn-outline-primary:active,.open>.btn.btn-outline-primary.dropdown-toggle,.show>.btn.btn-outline-primary.dropdown-toggle{color:#9c27b0;background-color:hsla(0,0%,60%,.2);border-color:#9c27b0;box-shadow:0 2px 2px 0 rgba(0,0,0,.14),0 3px 1px -2px rgba(0,0,0,.2),0 1px 5px 0 rgba(0,0,0,.12)}.btn.btn-outline-primary.active.focus,.btn.btn-outline-primary.active:focus,.btn.btn-outline-primary.active:hover,.btn.btn-outline-primary:active.focus,.btn.btn-outline-primary:active:focus,.btn.btn-outline-primary:active:hover,.open>.btn.btn-outline-primary.dropdown-toggle.focus,.open>.btn.btn-outline-primary.dropdown-toggle:focus,.open>.btn.btn-outline-primary.dropdown-toggle:hover,.show>.btn.btn-outline-primary.dropdown-toggle.focus,.show>.btn.btn-outline-primary.dropdown-toggle:focus,.show>.btn.btn-outline-primary.dropdown-toggle:hover{color:#9c27b0;background-color:hsla(0,0%,60%,.4);border-color:#9c27b0}.open>.btn.btn-outline-primary.dropdown-toggle.bmd-btn-icon{color:inherit;background-color:transparent}.open>.btn.btn-outline-primary.dropdown-toggle.bmd-btn-icon:hover{background-color:hsla(0,0%,60%,.2)}.bg-inverse .btn.btn-outline-primary,.btn.btn-outline-primary.disabled.focus,.btn.btn-outline-primary.disabled:focus,.btn.btn-outline-primary.disabled:hover,.btn.btn-outline-primary:disabled.focus,.btn.btn-outline-primary:disabled:focus,.btn.btn-outline-primary:disabled:hover{background-color:transparent;border-color:#9c27b0}.bg-inverse .btn.btn-outline-primary{color:#9c27b0}.bg-inverse .btn.btn-outline-primary.focus,.bg-inverse .btn.btn-outline-primary:focus,.bg-inverse .btn.btn-outline-primary:hover{color:#9c27b0;background-color:hsla(0,0%,80%,.15);border-color:hsla(0,0%,80%,.15)}.bg-inverse .btn.btn-outline-primary.active,.bg-inverse .btn.btn-outline-primary:active,.open>.bg-inverse .btn.btn-outline-primary.dropdown-toggle,.show>.bg-inverse .btn.btn-outline-primary.dropdown-toggle{color:#9c27b0;background-color:hsla(0,0%,80%,.15);border-color:hsla(0,0%,80%,.15);box-shadow:0 2px 2px 0 rgba(0,0,0,.14),0 3px 1px -2px rgba(0,0,0,.2),0 1px 5px 0 rgba(0,0,0,.12)}.bg-inverse .btn.btn-outline-primary.active.focus,.bg-inverse .btn.btn-outline-primary.active:focus,.bg-inverse .btn.btn-outline-primary.active:hover,.bg-inverse .btn.btn-outline-primary:active.focus,.bg-inverse .btn.btn-outline-primary:active:focus,.bg-inverse .btn.btn-outline-primary:active:hover,.open>.bg-inverse .btn.btn-outline-primary.dropdown-toggle.focus,.open>.bg-inverse .btn.btn-outline-primary.dropdown-toggle:focus,.open>.bg-inverse .btn.btn-outline-primary.dropdown-toggle:hover,.show>.bg-inverse .btn.btn-outline-primary.dropdown-toggle.focus,.show>.bg-inverse .btn.btn-outline-primary.dropdown-toggle:focus,.show>.bg-inverse .btn.btn-outline-primary.dropdown-toggle:hover{color:#9c27b0;background-color:hsla(0,0%,80%,.25);border-color:hsla(0,0%,80%,.25)}.open>.bg-inverse .btn.btn-outline-primary.dropdown-toggle.bmd-btn-icon{color:inherit;background-color:transparent}.open>.bg-inverse .btn.btn-outline-primary.dropdown-toggle.bmd-btn-icon:hover{background-color:hsla(0,0%,80%,.15)}.bg-inverse .btn.btn-outline-primary.disabled.focus,.bg-inverse .btn.btn-outline-primary.disabled:focus,.bg-inverse .btn.btn-outline-primary.disabled:hover,.bg-inverse .btn.btn-outline-primary:disabled.focus,.bg-inverse .btn.btn-outline-primary:disabled:focus,.bg-inverse .btn.btn-outline-primary:disabled:hover{background-color:transparent;border-color:#9c27b0}.btn.btn-outline-primary.btn-link{background-color:transparent}.btn.btn-outline-secondary{color:#333;background-color:transparent;border-color:#333}.btn.btn-outline-secondary.focus,.btn.btn-outline-secondary:focus,.btn.btn-outline-secondary:hover{color:#333;background-color:hsla(0,0%,60%,.2);border-color:#333}.btn.btn-outline-secondary.active,.btn.btn-outline-secondary:active,.open>.btn.btn-outline-secondary.dropdown-toggle,.show>.btn.btn-outline-secondary.dropdown-toggle{color:#333;background-color:hsla(0,0%,60%,.2);border-color:#333;box-shadow:0 2px 2px 0 rgba(0,0,0,.14),0 3px 1px -2px rgba(0,0,0,.2),0 1px 5px 0 rgba(0,0,0,.12)}.btn.btn-outline-secondary.active.focus,.btn.btn-outline-secondary.active:focus,.btn.btn-outline-secondary.active:hover,.btn.btn-outline-secondary:active.focus,.btn.btn-outline-secondary:active:focus,.btn.btn-outline-secondary:active:hover,.open>.btn.btn-outline-secondary.dropdown-toggle.focus,.open>.btn.btn-outline-secondary.dropdown-toggle:focus,.open>.btn.btn-outline-secondary.dropdown-toggle:hover,.show>.btn.btn-outline-secondary.dropdown-toggle.focus,.show>.btn.btn-outline-secondary.dropdown-toggle:focus,.show>.btn.btn-outline-secondary.dropdown-toggle:hover{color:#333;background-color:hsla(0,0%,60%,.4);border-color:#333}.open>.btn.btn-outline-secondary.dropdown-toggle.bmd-btn-icon{color:inherit;background-color:transparent}.open>.btn.btn-outline-secondary.dropdown-toggle.bmd-btn-icon:hover{background-color:hsla(0,0%,60%,.2)}.bg-inverse .btn.btn-outline-secondary,.btn.btn-outline-secondary.disabled.focus,.btn.btn-outline-secondary.disabled:focus,.btn.btn-outline-secondary.disabled:hover,.btn.btn-outline-secondary:disabled.focus,.btn.btn-outline-secondary:disabled:focus,.btn.btn-outline-secondary:disabled:hover{background-color:transparent;border-color:#333}.bg-inverse .btn.btn-outline-secondary{color:#333}.bg-inverse .btn.btn-outline-secondary.focus,.bg-inverse .btn.btn-outline-secondary:focus,.bg-inverse .btn.btn-outline-secondary:hover{color:#333;background-color:hsla(0,0%,80%,.15);border-color:hsla(0,0%,80%,.15)}.bg-inverse .btn.btn-outline-secondary.active,.bg-inverse .btn.btn-outline-secondary:active,.open>.bg-inverse .btn.btn-outline-secondary.dropdown-toggle,.show>.bg-inverse .btn.btn-outline-secondary.dropdown-toggle{color:#333;background-color:hsla(0,0%,80%,.15);border-color:hsla(0,0%,80%,.15);box-shadow:0 2px 2px 0 rgba(0,0,0,.14),0 3px 1px -2px rgba(0,0,0,.2),0 1px 5px 0 rgba(0,0,0,.12)}.bg-inverse .btn.btn-outline-secondary.active.focus,.bg-inverse .btn.btn-outline-secondary.active:focus,.bg-inverse .btn.btn-outline-secondary.active:hover,.bg-inverse .btn.btn-outline-secondary:active.focus,.bg-inverse .btn.btn-outline-secondary:active:focus,.bg-inverse .btn.btn-outline-secondary:active:hover,.open>.bg-inverse .btn.btn-outline-secondary.dropdown-toggle.focus,.open>.bg-inverse .btn.btn-outline-secondary.dropdown-toggle:focus,.open>.bg-inverse .btn.btn-outline-secondary.dropdown-toggle:hover,.show>.bg-inverse .btn.btn-outline-secondary.dropdown-toggle.focus,.show>.bg-inverse .btn.btn-outline-secondary.dropdown-toggle:focus,.show>.bg-inverse .btn.btn-outline-secondary.dropdown-toggle:hover{color:#333;background-color:hsla(0,0%,80%,.25);border-color:hsla(0,0%,80%,.25)}.open>.bg-inverse .btn.btn-outline-secondary.dropdown-toggle.bmd-btn-icon{color:inherit;background-color:transparent}.open>.bg-inverse .btn.btn-outline-secondary.dropdown-toggle.bmd-btn-icon:hover{background-color:hsla(0,0%,80%,.15)}.bg-inverse .btn.btn-outline-secondary.disabled.focus,.bg-inverse .btn.btn-outline-secondary.disabled:focus,.bg-inverse .btn.btn-outline-secondary.disabled:hover,.bg-inverse .btn.btn-outline-secondary:disabled.focus,.bg-inverse .btn.btn-outline-secondary:disabled:focus,.bg-inverse .btn.btn-outline-secondary:disabled:hover{background-color:transparent;border-color:#333}.btn.btn-outline-secondary.btn-link{background-color:transparent}.btn.btn-outline-info{color:#00bcd4;background-color:transparent;border-color:#00bcd4}.btn.btn-outline-info.focus,.btn.btn-outline-info:focus,.btn.btn-outline-info:hover{color:#00bcd4;background-color:hsla(0,0%,60%,.2);border-color:#00bcd4}.btn.btn-outline-info.active,.btn.btn-outline-info:active,.open>.btn.btn-outline-info.dropdown-toggle,.show>.btn.btn-outline-info.dropdown-toggle{color:#00bcd4;background-color:hsla(0,0%,60%,.2);border-color:#00bcd4;box-shadow:0 2px 2px 0 rgba(0,0,0,.14),0 3px 1px -2px rgba(0,0,0,.2),0 1px 5px 0 rgba(0,0,0,.12)}.btn.btn-outline-info.active.focus,.btn.btn-outline-info.active:focus,.btn.btn-outline-info.active:hover,.btn.btn-outline-info:active.focus,.btn.btn-outline-info:active:focus,.btn.btn-outline-info:active:hover,.open>.btn.btn-outline-info.dropdown-toggle.focus,.open>.btn.btn-outline-info.dropdown-toggle:focus,.open>.btn.btn-outline-info.dropdown-toggle:hover,.show>.btn.btn-outline-info.dropdown-toggle.focus,.show>.btn.btn-outline-info.dropdown-toggle:focus,.show>.btn.btn-outline-info.dropdown-toggle:hover{color:#00bcd4;background-color:hsla(0,0%,60%,.4);border-color:#00bcd4}.open>.btn.btn-outline-info.dropdown-toggle.bmd-btn-icon{color:inherit;background-color:transparent}.open>.btn.btn-outline-info.dropdown-toggle.bmd-btn-icon:hover{background-color:hsla(0,0%,60%,.2)}.bg-inverse .btn.btn-outline-info,.btn.btn-outline-info.disabled.focus,.btn.btn-outline-info.disabled:focus,.btn.btn-outline-info.disabled:hover,.btn.btn-outline-info:disabled.focus,.btn.btn-outline-info:disabled:focus,.btn.btn-outline-info:disabled:hover{background-color:transparent;border-color:#00bcd4}.bg-inverse .btn.btn-outline-info{color:#00bcd4}.bg-inverse .btn.btn-outline-info.focus,.bg-inverse .btn.btn-outline-info:focus,.bg-inverse .btn.btn-outline-info:hover{color:#00bcd4;background-color:hsla(0,0%,80%,.15);border-color:hsla(0,0%,80%,.15)}.bg-inverse .btn.btn-outline-info.active,.bg-inverse .btn.btn-outline-info:active,.open>.bg-inverse .btn.btn-outline-info.dropdown-toggle,.show>.bg-inverse .btn.btn-outline-info.dropdown-toggle{color:#00bcd4;background-color:hsla(0,0%,80%,.15);border-color:hsla(0,0%,80%,.15);box-shadow:0 2px 2px 0 rgba(0,0,0,.14),0 3px 1px -2px rgba(0,0,0,.2),0 1px 5px 0 rgba(0,0,0,.12)}.bg-inverse .btn.btn-outline-info.active.focus,.bg-inverse .btn.btn-outline-info.active:focus,.bg-inverse .btn.btn-outline-info.active:hover,.bg-inverse .btn.btn-outline-info:active.focus,.bg-inverse .btn.btn-outline-info:active:focus,.bg-inverse .btn.btn-outline-info:active:hover,.open>.bg-inverse .btn.btn-outline-info.dropdown-toggle.focus,.open>.bg-inverse .btn.btn-outline-info.dropdown-toggle:focus,.open>.bg-inverse .btn.btn-outline-info.dropdown-toggle:hover,.show>.bg-inverse .btn.btn-outline-info.dropdown-toggle.focus,.show>.bg-inverse .btn.btn-outline-info.dropdown-toggle:focus,.show>.bg-inverse .btn.btn-outline-info.dropdown-toggle:hover{color:#00bcd4;background-color:hsla(0,0%,80%,.25);border-color:hsla(0,0%,80%,.25)}.open>.bg-inverse .btn.btn-outline-info.dropdown-toggle.bmd-btn-icon{color:inherit;background-color:transparent}.open>.bg-inverse .btn.btn-outline-info.dropdown-toggle.bmd-btn-icon:hover{background-color:hsla(0,0%,80%,.15)}.bg-inverse .btn.btn-outline-info.disabled.focus,.bg-inverse .btn.btn-outline-info.disabled:focus,.bg-inverse .btn.btn-outline-info.disabled:hover,.bg-inverse .btn.btn-outline-info:disabled.focus,.bg-inverse .btn.btn-outline-info:disabled:focus,.bg-inverse .btn.btn-outline-info:disabled:hover{background-color:transparent;border-color:#00bcd4}.btn.btn-outline-info.btn-link{background-color:transparent}.btn.btn-outline-success{color:#4caf50;background-color:transparent;border-color:#4caf50}.btn.btn-outline-success.focus,.btn.btn-outline-success:focus,.btn.btn-outline-success:hover{color:#4caf50;background-color:hsla(0,0%,60%,.2);border-color:#4caf50}.btn.btn-outline-success.active,.btn.btn-outline-success:active,.open>.btn.btn-outline-success.dropdown-toggle,.show>.btn.btn-outline-success.dropdown-toggle{color:#4caf50;background-color:hsla(0,0%,60%,.2);border-color:#4caf50;box-shadow:0 2px 2px 0 rgba(0,0,0,.14),0 3px 1px -2px rgba(0,0,0,.2),0 1px 5px 0 rgba(0,0,0,.12)}.btn.btn-outline-success.active.focus,.btn.btn-outline-success.active:focus,.btn.btn-outline-success.active:hover,.btn.btn-outline-success:active.focus,.btn.btn-outline-success:active:focus,.btn.btn-outline-success:active:hover,.open>.btn.btn-outline-success.dropdown-toggle.focus,.open>.btn.btn-outline-success.dropdown-toggle:focus,.open>.btn.btn-outline-success.dropdown-toggle:hover,.show>.btn.btn-outline-success.dropdown-toggle.focus,.show>.btn.btn-outline-success.dropdown-toggle:focus,.show>.btn.btn-outline-success.dropdown-toggle:hover{color:#4caf50;background-color:hsla(0,0%,60%,.4);border-color:#4caf50}.open>.btn.btn-outline-success.dropdown-toggle.bmd-btn-icon{color:inherit;background-color:transparent}.open>.btn.btn-outline-success.dropdown-toggle.bmd-btn-icon:hover{background-color:hsla(0,0%,60%,.2)}.bg-inverse .btn.btn-outline-success,.btn.btn-outline-success.disabled.focus,.btn.btn-outline-success.disabled:focus,.btn.btn-outline-success.disabled:hover,.btn.btn-outline-success:disabled.focus,.btn.btn-outline-success:disabled:focus,.btn.btn-outline-success:disabled:hover{background-color:transparent;border-color:#4caf50}.bg-inverse .btn.btn-outline-success{color:#4caf50}.bg-inverse .btn.btn-outline-success.focus,.bg-inverse .btn.btn-outline-success:focus,.bg-inverse .btn.btn-outline-success:hover{color:#4caf50;background-color:hsla(0,0%,80%,.15);border-color:hsla(0,0%,80%,.15)}.bg-inverse .btn.btn-outline-success.active,.bg-inverse .btn.btn-outline-success:active,.open>.bg-inverse .btn.btn-outline-success.dropdown-toggle,.show>.bg-inverse .btn.btn-outline-success.dropdown-toggle{color:#4caf50;background-color:hsla(0,0%,80%,.15);border-color:hsla(0,0%,80%,.15);box-shadow:0 2px 2px 0 rgba(0,0,0,.14),0 3px 1px -2px rgba(0,0,0,.2),0 1px 5px 0 rgba(0,0,0,.12)}.bg-inverse .btn.btn-outline-success.active.focus,.bg-inverse .btn.btn-outline-success.active:focus,.bg-inverse .btn.btn-outline-success.active:hover,.bg-inverse .btn.btn-outline-success:active.focus,.bg-inverse .btn.btn-outline-success:active:focus,.bg-inverse .btn.btn-outline-success:active:hover,.open>.bg-inverse .btn.btn-outline-success.dropdown-toggle.focus,.open>.bg-inverse .btn.btn-outline-success.dropdown-toggle:focus,.open>.bg-inverse .btn.btn-outline-success.dropdown-toggle:hover,.show>.bg-inverse .btn.btn-outline-success.dropdown-toggle.focus,.show>.bg-inverse .btn.btn-outline-success.dropdown-toggle:focus,.show>.bg-inverse .btn.btn-outline-success.dropdown-toggle:hover{color:#4caf50;background-color:hsla(0,0%,80%,.25);border-color:hsla(0,0%,80%,.25)}.open>.bg-inverse .btn.btn-outline-success.dropdown-toggle.bmd-btn-icon{color:inherit;background-color:transparent}.open>.bg-inverse .btn.btn-outline-success.dropdown-toggle.bmd-btn-icon:hover{background-color:hsla(0,0%,80%,.15)}.bg-inverse .btn.btn-outline-success.disabled.focus,.bg-inverse .btn.btn-outline-success.disabled:focus,.bg-inverse .btn.btn-outline-success.disabled:hover,.bg-inverse .btn.btn-outline-success:disabled.focus,.bg-inverse .btn.btn-outline-success:disabled:focus,.bg-inverse .btn.btn-outline-success:disabled:hover{background-color:transparent;border-color:#4caf50}.btn.btn-outline-success.btn-link{background-color:transparent}.btn.btn-outline-warning{color:#ff9800;background-color:transparent;border-color:#ff9800}.btn.btn-outline-warning.focus,.btn.btn-outline-warning:focus,.btn.btn-outline-warning:hover{color:#ff9800;background-color:hsla(0,0%,60%,.2);border-color:#ff9800}.btn.btn-outline-warning.active,.btn.btn-outline-warning:active,.open>.btn.btn-outline-warning.dropdown-toggle,.show>.btn.btn-outline-warning.dropdown-toggle{color:#ff9800;background-color:hsla(0,0%,60%,.2);border-color:#ff9800;box-shadow:0 2px 2px 0 rgba(0,0,0,.14),0 3px 1px -2px rgba(0,0,0,.2),0 1px 5px 0 rgba(0,0,0,.12)}.btn.btn-outline-warning.active.focus,.btn.btn-outline-warning.active:focus,.btn.btn-outline-warning.active:hover,.btn.btn-outline-warning:active.focus,.btn.btn-outline-warning:active:focus,.btn.btn-outline-warning:active:hover,.open>.btn.btn-outline-warning.dropdown-toggle.focus,.open>.btn.btn-outline-warning.dropdown-toggle:focus,.open>.btn.btn-outline-warning.dropdown-toggle:hover,.show>.btn.btn-outline-warning.dropdown-toggle.focus,.show>.btn.btn-outline-warning.dropdown-toggle:focus,.show>.btn.btn-outline-warning.dropdown-toggle:hover{color:#ff9800;background-color:hsla(0,0%,60%,.4);border-color:#ff9800}.open>.btn.btn-outline-warning.dropdown-toggle.bmd-btn-icon{color:inherit;background-color:transparent}.open>.btn.btn-outline-warning.dropdown-toggle.bmd-btn-icon:hover{background-color:hsla(0,0%,60%,.2)}.bg-inverse .btn.btn-outline-warning,.btn.btn-outline-warning.disabled.focus,.btn.btn-outline-warning.disabled:focus,.btn.btn-outline-warning.disabled:hover,.btn.btn-outline-warning:disabled.focus,.btn.btn-outline-warning:disabled:focus,.btn.btn-outline-warning:disabled:hover{background-color:transparent;border-color:#ff9800}.bg-inverse .btn.btn-outline-warning{color:#ff9800}.bg-inverse .btn.btn-outline-warning.focus,.bg-inverse .btn.btn-outline-warning:focus,.bg-inverse .btn.btn-outline-warning:hover{color:#ff9800;background-color:hsla(0,0%,80%,.15);border-color:hsla(0,0%,80%,.15)}.bg-inverse .btn.btn-outline-warning.active,.bg-inverse .btn.btn-outline-warning:active,.open>.bg-inverse .btn.btn-outline-warning.dropdown-toggle,.show>.bg-inverse .btn.btn-outline-warning.dropdown-toggle{color:#ff9800;background-color:hsla(0,0%,80%,.15);border-color:hsla(0,0%,80%,.15);box-shadow:0 2px 2px 0 rgba(0,0,0,.14),0 3px 1px -2px rgba(0,0,0,.2),0 1px 5px 0 rgba(0,0,0,.12)}.bg-inverse .btn.btn-outline-warning.active.focus,.bg-inverse .btn.btn-outline-warning.active:focus,.bg-inverse .btn.btn-outline-warning.active:hover,.bg-inverse .btn.btn-outline-warning:active.focus,.bg-inverse .btn.btn-outline-warning:active:focus,.bg-inverse .btn.btn-outline-warning:active:hover,.open>.bg-inverse .btn.btn-outline-warning.dropdown-toggle.focus,.open>.bg-inverse .btn.btn-outline-warning.dropdown-toggle:focus,.open>.bg-inverse .btn.btn-outline-warning.dropdown-toggle:hover,.show>.bg-inverse .btn.btn-outline-warning.dropdown-toggle.focus,.show>.bg-inverse .btn.btn-outline-warning.dropdown-toggle:focus,.show>.bg-inverse .btn.btn-outline-warning.dropdown-toggle:hover{color:#ff9800;background-color:hsla(0,0%,80%,.25);border-color:hsla(0,0%,80%,.25)}.open>.bg-inverse .btn.btn-outline-warning.dropdown-toggle.bmd-btn-icon{color:inherit;background-color:transparent}.open>.bg-inverse .btn.btn-outline-warning.dropdown-toggle.bmd-btn-icon:hover{background-color:hsla(0,0%,80%,.15)}.bg-inverse .btn.btn-outline-warning.disabled.focus,.bg-inverse .btn.btn-outline-warning.disabled:focus,.bg-inverse .btn.btn-outline-warning.disabled:hover,.bg-inverse .btn.btn-outline-warning:disabled.focus,.bg-inverse .btn.btn-outline-warning:disabled:focus,.bg-inverse .btn.btn-outline-warning:disabled:hover{background-color:transparent;border-color:#ff9800}.btn.btn-outline-warning.btn-link{background-color:transparent}.btn.btn-outline-danger{color:#f44336;background-color:transparent;border-color:#f44336}.btn.btn-outline-danger.focus,.btn.btn-outline-danger:focus,.btn.btn-outline-danger:hover{color:#f44336;background-color:hsla(0,0%,60%,.2);border-color:#f44336}.btn.btn-outline-danger.active,.btn.btn-outline-danger:active,.open>.btn.btn-outline-danger.dropdown-toggle,.show>.btn.btn-outline-danger.dropdown-toggle{color:#f44336;background-color:hsla(0,0%,60%,.2);border-color:#f44336;box-shadow:0 2px 2px 0 rgba(0,0,0,.14),0 3px 1px -2px rgba(0,0,0,.2),0 1px 5px 0 rgba(0,0,0,.12)}.btn.btn-outline-danger.active.focus,.btn.btn-outline-danger.active:focus,.btn.btn-outline-danger.active:hover,.btn.btn-outline-danger:active.focus,.btn.btn-outline-danger:active:focus,.btn.btn-outline-danger:active:hover,.open>.btn.btn-outline-danger.dropdown-toggle.focus,.open>.btn.btn-outline-danger.dropdown-toggle:focus,.open>.btn.btn-outline-danger.dropdown-toggle:hover,.show>.btn.btn-outline-danger.dropdown-toggle.focus,.show>.btn.btn-outline-danger.dropdown-toggle:focus,.show>.btn.btn-outline-danger.dropdown-toggle:hover{color:#f44336;background-color:hsla(0,0%,60%,.4);border-color:#f44336}.open>.btn.btn-outline-danger.dropdown-toggle.bmd-btn-icon{color:inherit;background-color:transparent}.open>.btn.btn-outline-danger.dropdown-toggle.bmd-btn-icon:hover{background-color:hsla(0,0%,60%,.2)}.bg-inverse .btn.btn-outline-danger,.btn.btn-outline-danger.disabled.focus,.btn.btn-outline-danger.disabled:focus,.btn.btn-outline-danger.disabled:hover,.btn.btn-outline-danger:disabled.focus,.btn.btn-outline-danger:disabled:focus,.btn.btn-outline-danger:disabled:hover{background-color:transparent;border-color:#f44336}.bg-inverse .btn.btn-outline-danger{color:#f44336}.bg-inverse .btn.btn-outline-danger.focus,.bg-inverse .btn.btn-outline-danger:focus,.bg-inverse .btn.btn-outline-danger:hover{color:#f44336;background-color:hsla(0,0%,80%,.15);border-color:hsla(0,0%,80%,.15)}.bg-inverse .btn.btn-outline-danger.active,.bg-inverse .btn.btn-outline-danger:active,.open>.bg-inverse .btn.btn-outline-danger.dropdown-toggle,.show>.bg-inverse .btn.btn-outline-danger.dropdown-toggle{color:#f44336;background-color:hsla(0,0%,80%,.15);border-color:hsla(0,0%,80%,.15);box-shadow:0 2px 2px 0 rgba(0,0,0,.14),0 3px 1px -2px rgba(0,0,0,.2),0 1px 5px 0 rgba(0,0,0,.12)}.bg-inverse .btn.btn-outline-danger.active.focus,.bg-inverse .btn.btn-outline-danger.active:focus,.bg-inverse .btn.btn-outline-danger.active:hover,.bg-inverse .btn.btn-outline-danger:active.focus,.bg-inverse .btn.btn-outline-danger:active:focus,.bg-inverse .btn.btn-outline-danger:active:hover,.open>.bg-inverse .btn.btn-outline-danger.dropdown-toggle.focus,.open>.bg-inverse .btn.btn-outline-danger.dropdown-toggle:focus,.open>.bg-inverse .btn.btn-outline-danger.dropdown-toggle:hover,.show>.bg-inverse .btn.btn-outline-danger.dropdown-toggle.focus,.show>.bg-inverse .btn.btn-outline-danger.dropdown-toggle:focus,.show>.bg-inverse .btn.btn-outline-danger.dropdown-toggle:hover{color:#f44336;background-color:hsla(0,0%,80%,.25);border-color:hsla(0,0%,80%,.25)}.open>.bg-inverse .btn.btn-outline-danger.dropdown-toggle.bmd-btn-icon{color:inherit;background-color:transparent}.open>.bg-inverse .btn.btn-outline-danger.dropdown-toggle.bmd-btn-icon:hover{background-color:hsla(0,0%,80%,.15)}.bg-inverse .btn.btn-outline-danger.disabled.focus,.bg-inverse .btn.btn-outline-danger.disabled:focus,.bg-inverse .btn.btn-outline-danger.disabled:hover,.bg-inverse .btn.btn-outline-danger:disabled.focus,.bg-inverse .btn.btn-outline-danger:disabled:focus,.bg-inverse .btn.btn-outline-danger:disabled:hover{background-color:transparent;border-color:#f44336}.btn.btn-outline-danger.btn-link{background-color:transparent}.btn-group-lg .btn,.btn-group-lg>.btn,.btn.btn-lg{padding:1.125rem 2.25rem;font-size:.875rem;line-height:1.333333;border-radius:.2rem}.btn-group-sm .btn,.btn-group-sm>.btn,.btn.btn-sm{padding:.40625rem 1.25rem;font-size:.6875rem;line-height:1.5;border-radius:.2rem}.btn.btn-round{border-radius:30px}.btn.btn-fab,.btn.btn-just-icon{font-size:24px;height:41px;min-width:41px;width:41px;padding:0;overflow:hidden;position:relative;line-height:41px}.btn.btn-fab.btn-round,.btn.btn-just-icon.btn-round{border-radius:50%}.btn-group-sm .btn.btn-fab,.btn-group-sm .btn.btn-just-icon,.btn-group-sm>.btn.btn-fab,.btn-group-sm>.btn.btn-just-icon,.btn.btn-fab.btn-fab-mini,.btn.btn-fab.btn-sm,.btn.btn-just-icon.btn-fab-mini,.btn.btn-just-icon.btn-sm{height:30px;min-width:30px;width:30px}.btn-group-sm .btn.btn-fab .fa,.btn-group-sm .btn.btn-fab .material-icons,.btn-group-sm .btn.btn-just-icon .fa,.btn-group-sm .btn.btn-just-icon .material-icons,.btn-group-sm>.btn.btn-fab .fa,.btn-group-sm>.btn.btn-fab .material-icons,.btn-group-sm>.btn.btn-just-icon .fa,.btn-group-sm>.btn.btn-just-icon .material-icons,.btn.btn-fab.btn-fab-mini .fa,.btn.btn-fab.btn-fab-mini .material-icons,.btn.btn-fab.btn-sm .fa,.btn.btn-fab.btn-sm .material-icons,.btn.btn-just-icon.btn-fab-mini .fa,.btn.btn-just-icon.btn-fab-mini .material-icons,.btn.btn-just-icon.btn-sm .fa,.btn.btn-just-icon.btn-sm .material-icons{font-size:17px;line-height:29px}.btn-group-lg .btn.btn-fab,.btn-group-lg .btn.btn-just-icon,.btn-group-lg>.btn.btn-fab,.btn-group-lg>.btn.btn-just-icon,.btn.btn-fab.btn-lg,.btn.btn-just-icon.btn-lg{height:57px;min-width:57px;width:57px;line-height:56px}.btn-group-lg .btn.btn-fab .fa,.btn-group-lg .btn.btn-fab .material-icons,.btn-group-lg .btn.btn-just-icon .fa,.btn-group-lg .btn.btn-just-icon .material-icons,.btn-group-lg>.btn.btn-fab .fa,.btn-group-lg>.btn.btn-fab .material-icons,.btn-group-lg>.btn.btn-just-icon .fa,.btn-group-lg>.btn.btn-just-icon .material-icons,.btn.btn-fab.btn-lg .fa,.btn.btn-fab.btn-lg .material-icons,.btn.btn-just-icon.btn-lg .fa,.btn.btn-just-icon.btn-lg .material-icons{font-size:32px;line-height:56px}.btn.btn-fab .fa,.btn.btn-fab .material-icons,.btn.btn-just-icon .fa,.btn.btn-just-icon .material-icons{margin-top:0;position:absolute;width:100%;transform:none;left:0;top:0;height:100%;line-height:41px;font-size:20px}.btn-group-lg>.btn-just-icon.btn,.btn-just-icon.btn-lg{font-size:24px;height:41px;min-width:41px;width:41px}.input-group-btn>.btn{border:0}.btn .material-icons,.btn:not(.btn-just-icon):not(.btn-fab) .fa{position:relative;display:inline-block;top:0;margin-top:-1em;margin-bottom:-1em;font-size:1.1rem;vertical-align:middle}.bg-inverse .btn-group-vertical.disabled,.bg-inverse .btn-group-vertical:disabled,.bg-inverse .btn-group-vertical[disabled],.bg-inverse .btn-group.disabled,.bg-inverse .btn-group:disabled,.bg-inverse .btn-group[disabled],.bg-inverse .btn.disabled,.bg-inverse .btn:disabled,.bg-inverse .btn[disabled],.bg-inverse .input-group-btn .btn.disabled,.bg-inverse .input-group-btn .btn:disabled,.bg-inverse .input-group-btn .btn[disabled],.bg-inverse fieldset[disabled][disabled] .btn,.bg-inverse fieldset[disabled][disabled] .btn-group,.bg-inverse fieldset[disabled][disabled] .btn-group-vertical,.bg-inverse fieldset[disabled][disabled] .input-group-btn .btn{color:hsla(0,0%,100%,.3)}.btn-group,.btn-group-vertical{position:relative;margin:10px 1px}.btn-group-vertical .dropdown-menu,.btn-group .dropdown-menu{border-radius:0 0 .25rem .25rem}.btn-group-vertical.btn-group-raised,.btn-group.btn-group-raised{box-shadow:0 2px 2px 0 rgba(0,0,0,.14),0 3px 1px -2px rgba(0,0,0,.2),0 1px 5px 0 rgba(0,0,0,.12)}.btn-group-vertical .btn,.btn-group-vertical .btn+.btn,.btn-group-vertical .btn-group,.btn-group-vertical .btn:active,.btn-group-vertical>.btn-group,.btn-group .btn,.btn-group .btn+.btn,.btn-group .btn-group,.btn-group .btn:active,.btn-group>.btn-group{margin:0}.form-check{margin-bottom:.5rem}.form-check,.form-check .form-check-label{padding-left:0}.form-check .form-check-input{position:absolute;margin:0;z-index:-1;left:0;pointer-events:none}.form-check .form-check-sign:before{display:block;position:absolute;left:0;content:"";background-color:rgba(0,0,0,.84);height:20px;width:20px;border-radius:100%;z-index:1;opacity:0;margin:0;top:0;transform:scale3d(2.3,2.3,1)}.form-check .form-check-sign .check{position:relative;display:inline-block;width:20px;height:20px;border:1px solid rgba(0,0,0,.54);overflow:hidden;z-index:1;border-radius:3px}.form-check .form-check-sign .check:before{position:absolute;content:"";transform:rotate(45deg);display:block;margin-top:-3px;margin-left:7px;width:0;color:#fff;height:0;box-shadow:0 0 0 0,0 0 0 0,0 0 0 0,0 0 0 0,0 0 0 0,0 0 0 0,inset 0 0 0 0;animation:checkboxOff .3s forwards}.form-check .form-check-input:focus+.form-check-sign .check:after{opacity:.2}.form-check .form-check-input:checked+.form-check-sign .check{background:#9c27b0}.form-check .form-check-input:checked+.form-check-sign .check:before{color:#fff;box-shadow:0 0 0 10px,10px -10px 0 10px,32px 0 0 20px,0 32px 0 20px,-5px 5px 0 10px,20px -12px 0 11px;animation:b .3s forwards}.form-check .form-check-input:checked+.form-check-sign:before{animation:c .5s}.form-check .form-check-input:checked+.form-check-sign .check:after{animation:c .5s forwards}.form-check .form-check-input:not(:checked)+.form-check-sign .check:after,.form-check .form-check-input:not(:checked)+.form-check-sign:before{animation:c .5s}.form-check .rtl .form-check .form-check-sign .check:before{margin-right:10px}.form-check .form-check-input[disabled]+.circle,.form-check .form-check-input[disabled]~.form-check-sign .check,fieldset[disabled] .form-check,fieldset[disabled] .form-check .form-check-input{opacity:.5}.form-check .form-check-input[disabled]~.form-check-sign .check{border-color:#000;opacity:.26}.form-check .form-check-input[disabled]+.form-check-sign .check:after{background-color:rgba(0,0,0,.87);transform:rotate(-45deg)}.form-check .form-check-input[disabled][checked]+.form-check-sign .check{background-color:#000}.form-check .form-check-label{cursor:pointer;padding-left:25px;position:relative}.form-group.is-focused .form-check .form-check-label{color:rgba(0,0,0,.26)}.form-group.is-focused .form-check .form-check-label:focus,.form-group.is-focused .form-check .form-check-label:hover{color:rgba(0,0,0,.54)}fieldset[disabled] .form-group.is-focused .form-check .form-check-label{color:rgba(0,0,0,.26)}.form-check .form-check-label span{display:block;position:absolute;left:-1px;top:-1px;transition-duration:.2s}.form-check .form-check-label .circle{border:1px solid rgba(0,0,0,.54);height:15px;width:15px;border-radius:100%;top:1px}.form-check .form-check-label .circle .check{height:15px;width:15px;border-radius:100%;background-color:#9c27b0;transform:scale3d(0,0,0)}.form-check .form-check-input{opacity:0;height:0;width:0;overflow:hidden}.form-check .form-check-input:checked~.check,.form-check .form-check-input:checked~.circle{opacity:1}.form-check .form-check-input:checked~.check{background-color:#9c27b0}.form-check .form-check-input:checked~.circle{border-color:#9c27b0}.form-check .form-check-input:checked .check:before{animation:b .5s forwards}.form-check .form-check-input:checked~.circle .check{transform:scale3d(.65,.65,1)}.form-check .form-check-input[disabled]~.check,.form-check .form-check-input[disabled]~.circle{opacity:.26}.form-check .form-check-input[disabled]~.check{background-color:#000}.form-check .form-check-input[disabled]~.circle{border-color:#000}.form-check .form-check-input[disabled]+.circle .check{background-color:#000}.form-check .form-check-sign{vertical-align:middle;position:relative;top:-2px;float:left;padding-right:10px;display:inline-block}.form-check .form-check-label .circle:before{display:block;position:absolute;left:-1px;content:"";background-color:rgba(0,0,0,.84);height:15px;width:15px;border-radius:100%;z-index:1;opacity:0;margin:0;top:-1px;transform:scale3d(2.3,2.3,1)}.form-check .form-check-label .form-check-input:checked+.circle:before{animation:c .5s}.form-check .form-check-label .form-check-input:checked+.circle .check:before{color:#fff;box-shadow:0 0 0 10px,10px -10px 0 10px,32px 0 0 20px,0 32px 0 20px,-5px 5px 0 10px,20px -12px 0 11px;animation:b .3s forwards}.form-check+.form-check{margin-top:0}@keyframes b{0%{box-shadow:0 0 0 10px,10px -10px 0 10px,32px 0 0 20px,0 32px 0 20px,-5px 5px 0 10px,15px 2px 0 11px}50%{box-shadow:0 0 0 10px,10px -10px 0 10px,32px 0 0 20px,0 32px 0 20px,-5px 5px 0 10px,20px 2px 0 11px}to{box-shadow:0 0 0 10px,10px -10px 0 10px,32px 0 0 20px,0 32px 0 20px,-5px 5px 0 10px,20px -12px 0 11px}}@keyframes c{0%{opacity:0}50%{opacity:.2}to{opacity:0}}.badge{padding:5px 12px;text-transform:uppercase;font-size:10px;color:#fff;display:inline-block;white-space:normal}.badge.badge-primary{background-color:#9c27b0}.badge.badge-info{background-color:#00bcd4}.badge.badge-success{background-color:#4caf50}.badge.badge-warning{background-color:#ff9800}.badge.badge-danger{background-color:#f44336}.badge.badge-rose{background-color:#e91e63}.badge.badge-default{background-color:#999}.badge-default[href]:focus,.badge-default[href]:hover{background-color:#8c8c8c}.badge-primary[href]:focus,.badge-primary[href]:hover{background-color:#89229b}.badge-info[href]:focus,.badge-info[href]:hover{background-color:#00a5bb}.badge-success[href]:focus,.badge-success[href]:hover{background-color:#449d48}.badge-warning[href]:focus,.badge-warning[href]:hover{background-color:#e68900;color:#fff}.badge-danger[href]:focus,.badge-danger[href]:hover{background-color:#f32c1e}.badge-rose[href]:focus,.badge-rose[href]:hover{background-color:#d81558}form{margin-bottom:1.125rem}.card form{margin:0}.navbar form{margin-bottom:0}.navbar form .bmd-form-group{display:inline-block;padding-top:0}.navbar form .btn{margin-bottom:0}.form-control{background:no-repeat bottom,50% calc(100% - 1px);background-size:0 100%,100% 100%;border:0;height:36px;transition:background 0s ease-out;padding-left:0;padding-right:0;border-radius:0;font-size:14px}.bmd-form-group.is-focused .form-control,.form-control:focus{background-size:100% 100%,100% 100%;transition-duration:.3s;box-shadow:none}.form-control::-moz-placeholder{color:#aaa;font-weight:400;font-size:14px}.form-control:-ms-input-placeholder{color:#aaa;font-weight:400;font-size:14px}.form-control::-webkit-input-placeholder{color:#aaa;font-weight:400;font-size:14px}.has-white .form-control::-moz-placeholder{color:#fff}.has-white .form-control:-ms-input-placeholder{color:#fff}.has-white .form-control::-webkit-input-placeholder{color:#fff}.bmd-help{position:absolute;display:none;font-size:.8rem;font-weight:400}.bmd-form-group.is-focused .bmd-help{display:block}.bmd-help:nth-of-type(2){padding-top:1rem}.bmd-help+.bmd-help{position:relative;margin-bottom:0}.checkbox-inline,.checkbox label,.is-focused .checkbox-inline,.is-focused .checkbox label,.is-focused .radio-inline,.is-focused .radio label,.is-focused .switch label,.radio-inline,.radio label,.switch label{color:#999}.checkbox-inline label:has(input[type=checkbox][disabled]),.checkbox-inline label:has(input[type=checkbox][disabled]):focus,.checkbox-inline label:has(input[type=checkbox][disabled]):hover,.checkbox-inline label:has(input[type=radio][disabled]),.checkbox-inline label:has(input[type=radio][disabled]):focus,.checkbox-inline label:has(input[type=radio][disabled]):hover,.checkbox label label:has(input[type=checkbox][disabled]),.checkbox label label:has(input[type=checkbox][disabled]):focus,.checkbox label label:has(input[type=checkbox][disabled]):hover,.checkbox label label:has(input[type=radio][disabled]),.checkbox label label:has(input[type=radio][disabled]):focus,.checkbox label label:has(input[type=radio][disabled]):hover,.is-focused .checkbox-inline label:has(input[type=checkbox][disabled]),.is-focused .checkbox-inline label:has(input[type=checkbox][disabled]):focus,.is-focused .checkbox-inline label:has(input[type=checkbox][disabled]):hover,.is-focused .checkbox-inline label:has(input[type=radio][disabled]),.is-focused .checkbox-inline label:has(input[type=radio][disabled]):focus,.is-focused .checkbox-inline label:has(input[type=radio][disabled]):hover,.is-focused .checkbox label label:has(input[type=checkbox][disabled]),.is-focused .checkbox label label:has(input[type=checkbox][disabled]):focus,.is-focused .checkbox label label:has(input[type=checkbox][disabled]):hover,.is-focused .checkbox label label:has(input[type=radio][disabled]),.is-focused .checkbox label label:has(input[type=radio][disabled]):focus,.is-focused .checkbox label label:has(input[type=radio][disabled]):hover,.is-focused .radio-inline label:has(input[type=checkbox][disabled]),.is-focused .radio-inline label:has(input[type=checkbox][disabled]):focus,.is-focused .radio-inline label:has(input[type=checkbox][disabled]):hover,.is-focused .radio-inline label:has(input[type=radio][disabled]),.is-focused .radio-inline label:has(input[type=radio][disabled]):focus,.is-focused .radio-inline label:has(input[type=radio][disabled]):hover,.is-focused .radio label label:has(input[type=checkbox][disabled]),.is-focused .radio label label:has(input[type=checkbox][disabled]):focus,.is-focused .radio label label:has(input[type=checkbox][disabled]):hover,.is-focused .radio label label:has(input[type=radio][disabled]),.is-focused .radio label label:has(input[type=radio][disabled]):focus,.is-focused .radio label label:has(input[type=radio][disabled]):hover,.is-focused .switch label label:has(input[type=checkbox][disabled]),.is-focused .switch label label:has(input[type=checkbox][disabled]):focus,.is-focused .switch label label:has(input[type=checkbox][disabled]):hover,.is-focused .switch label label:has(input[type=radio][disabled]),.is-focused .switch label label:has(input[type=radio][disabled]):focus,.is-focused .switch label label:has(input[type=radio][disabled]):hover,.radio-inline label:has(input[type=checkbox][disabled]),.radio-inline label:has(input[type=checkbox][disabled]):focus,.radio-inline label:has(input[type=checkbox][disabled]):hover,.radio-inline label:has(input[type=radio][disabled]),.radio-inline label:has(input[type=radio][disabled]):focus,.radio-inline label:has(input[type=radio][disabled]):hover,.radio label label:has(input[type=checkbox][disabled]),.radio label label:has(input[type=checkbox][disabled]):focus,.radio label label:has(input[type=checkbox][disabled]):hover,.radio label label:has(input[type=radio][disabled]),.radio label label:has(input[type=radio][disabled]):focus,.radio label label:has(input[type=radio][disabled]):hover,.switch label label:has(input[type=checkbox][disabled]),.switch label label:has(input[type=checkbox][disabled]):focus,.switch label label:has(input[type=checkbox][disabled]):hover,.switch label label:has(input[type=radio][disabled]),.switch label label:has(input[type=radio][disabled]):focus,.switch label label:has(input[type=radio][disabled]):hover,fieldset[disabled] .checkbox-inline,fieldset[disabled] .checkbox-inline:focus,fieldset[disabled] .checkbox-inline:hover,fieldset[disabled] .checkbox label,fieldset[disabled] .checkbox label:focus,fieldset[disabled] .checkbox label:hover,fieldset[disabled] .is-focused .checkbox-inline,fieldset[disabled] .is-focused .checkbox-inline:focus,fieldset[disabled] .is-focused .checkbox-inline:hover,fieldset[disabled] .is-focused .checkbox label,fieldset[disabled] .is-focused .checkbox label:focus,fieldset[disabled] .is-focused .checkbox label:hover,fieldset[disabled] .is-focused .radio-inline,fieldset[disabled] .is-focused .radio-inline:focus,fieldset[disabled] .is-focused .radio-inline:hover,fieldset[disabled] .is-focused .radio label,fieldset[disabled] .is-focused .radio label:focus,fieldset[disabled] .is-focused .radio label:hover,fieldset[disabled] .is-focused .switch label,fieldset[disabled] .is-focused .switch label:focus,fieldset[disabled] .is-focused .switch label:hover,fieldset[disabled] .radio-inline,fieldset[disabled] .radio-inline:focus,fieldset[disabled] .radio-inline:hover,fieldset[disabled] .radio label,fieldset[disabled] .radio label:focus,fieldset[disabled] .radio label:hover,fieldset[disabled] .switch label,fieldset[disabled] .switch label:focus,fieldset[disabled] .switch label:hover{color:#999}[class*=" bmd-label"],[class^=bmd-label]{color:#999}.form-control,.is-focused .form-control{background-image:linear-gradient(0deg,#9c27b0 2px,rgba(156,39,176,0) 0),linear-gradient(0deg,#d2d2d2 1px,hsla(0,0%,82%,0) 0)}.form-control:invalid{background-image:linear-gradient(0deg,#f44336 2px,rgba(244,67,54,0) 0),linear-gradient(0deg,#d2d2d2 1px,hsla(0,0%,82%,0) 0)}.form-control:read-only{background-image:linear-gradient(0deg,#d2d2d2 1px,hsla(0,0%,82%,0) 0),linear-gradient(0deg,#d2d2d2 1px,hsla(0,0%,82%,0) 0)}.form-control.disabled,.form-control:disabled,.form-control[disabled],fieldset[disabled][disabled] .form-control{background-image:linear-gradient(90deg,#d2d2d2 0,#d2d2d2 30%,transparent 0,transparent);background-repeat:repeat-x;background-size:3px 1px}.form-control.form-control-success,.is-focused .form-control.form-control-success{background-image:linear-gradient(0deg,#9c27b0 2px,rgba(156,39,176,0) 0),linear-gradient(0deg,#d2d2d2 1px,hsla(0,0%,82%,0) 0),"data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCA2MTIgNzkyIj48cGF0aCBmaWxsPSIjNWNiODVjIiBkPSJNMjMzLjggNjEwYy0xMy4zIDAtMjYtNi0zNC0xNi44TDkwLjUgNDQ4LjhDNzYuMyA0MzAgODAgNDAzLjMgOTguOCAzODljMTguOC0xNC4yIDQ1LjUtMTAuNCA1OS44IDguNGw3MiA5NUw0NTEuMyAyNDJjMTIuNS0yMCAzOC44LTI2LjIgNTguOC0xMy43IDIwIDEyLjQgMjYgMzguNyAxMy43IDU4LjhMMjcwIDU5MGMtNy40IDEyLTIwLjIgMTkuNC0zNC4zIDIwaC0yeiIvPjwvc3ZnPg=="}.form-control.form-control-warning,.is-focused .form-control.form-control-warning{background-image:linear-gradient(0deg,#9c27b0 2px,rgba(156,39,176,0) 0),linear-gradient(0deg,#d2d2d2 1px,hsla(0,0%,82%,0) 0),"data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCA2MTIgNzkyIj48cGF0aCBmaWxsPSIjZjBhZDRlIiBkPSJNNjAzIDY0MC4ybC0yNzguNS01MDljLTMuOC02LjYtMTAuOC0xMC42LTE4LjUtMTAuNnMtMTQuNyA0LTE4LjUgMTAuNkw5IDY0MC4yYy0zLjcgNi41LTMuNiAxNC40LjIgMjAuOCAzLjggNi41IDEwLjggMTAuNCAxOC4zIDEwLjRoNTU3YzcuNiAwIDE0LjYtNCAxOC40LTEwLjQgMy41LTYuNCAzLjYtMTQuNCAwLTIwLjh6bS0yNjYuNC0zMGgtNjEuMlY1NDloNjEuMnY2MS4yem0wLTEwN2gtNjEuMlYzMDRoNjEuMnYxOTl6Ii8+PC9zdmc+"}.form-control.form-control-danger,.is-focused .form-control.form-control-danger{background-image:linear-gradient(0deg,#9c27b0 2px,rgba(156,39,176,0) 0),linear-gradient(0deg,#d2d2d2 1px,hsla(0,0%,82%,0) 0),"data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCA2MTIgNzkyIj48cGF0aCBmaWxsPSIjZDk1MzRmIiBkPSJNNDQ3IDU0NC40Yy0xNC40IDE0LjQtMzcuNiAxNC40LTUyIDBsLTg5LTkyLjctODkgOTIuN2MtMTQuNSAxNC40LTM3LjcgMTQuNC01MiAwLTE0LjQtMTQuNC0xNC40LTM3LjYgMC01Mmw5Mi40LTk2LjMtOTIuNC05Ni4zYy0xNC40LTE0LjQtMTQuNC0zNy42IDAtNTJzMzcuNi0xNC4zIDUyIDBsODkgOTIuOCA4OS4yLTkyLjdjMTQuNC0xNC40IDM3LjYtMTQuNCA1MiAwIDE0LjMgMTQuNCAxNC4zIDM3LjYgMCA1MkwzNTQuNiAzOTZsOTIuNCA5Ni40YzE0LjQgMTQuNCAxNC40IDM3LjYgMCA1MnoiLz48L3N2Zz4="}.is-focused .valid-feedback{display:none;width:100%;margin-top:.25rem;font-size:80%;color:#999}.is-focused .valid-tooltip{position:absolute;top:100%;z-index:5;display:none;max-width:100%;padding:.5rem;margin-top:.1rem;font-size:.875rem;line-height:1;color:#fff;background-color:hsla(0,0%,60%,.8);border-radius:.2rem}.is-focused .custom-select.is-valid,.is-focused .form-control.is-valid,.was-validated .is-focused .custom-select:valid,.was-validated .is-focused .form-control:valid{border-color:#999}.is-focused .custom-select.is-valid:focus,.is-focused .form-control.is-valid:focus,.was-validated .is-focused .custom-select:valid:focus,.was-validated .is-focused .form-control:valid:focus{border-color:#999;box-shadow:0 0 0 .2rem hsla(0,0%,60%,.25)}.is-focused .custom-select.is-valid~.valid-feedback,.is-focused .custom-select.is-valid~.valid-tooltip,.is-focused .form-control.is-valid~.valid-feedback,.is-focused .form-control.is-valid~.valid-tooltip,.was-validated .is-focused .custom-select:valid~.valid-feedback,.was-validated .is-focused .custom-select:valid~.valid-tooltip,.was-validated .is-focused .form-control:valid~.valid-feedback,.was-validated .is-focused .form-control:valid~.valid-tooltip{display:block}.is-focused .form-check-input.is-valid~.form-check-label,.was-validated .is-focused .form-check-input:valid~.form-check-label{color:#999}.is-focused .form-check-input.is-valid~.valid-feedback,.is-focused .form-check-input.is-valid~.valid-tooltip,.was-validated .is-focused .form-check-input:valid~.valid-feedback,.was-validated .is-focused .form-check-input:valid~.valid-tooltip{display:block}.is-focused .custom-control-input.is-valid~.custom-control-label,.was-validated .is-focused .custom-control-input:valid~.custom-control-label{color:#999}.is-focused .custom-control-input.is-valid~.custom-control-label:before,.was-validated .is-focused .custom-control-input:valid~.custom-control-label:before{background-color:#d9d9d9}.is-focused .custom-control-input.is-valid~.valid-feedback,.is-focused .custom-control-input.is-valid~.valid-tooltip,.was-validated .is-focused .custom-control-input:valid~.valid-feedback,.was-validated .is-focused .custom-control-input:valid~.valid-tooltip{display:block}.is-focused .custom-control-input.is-valid:checked~.custom-control-label:before,.was-validated .is-focused .custom-control-input:valid:checked~.custom-control-label:before{background-color:#b3b3b3}.is-focused .custom-control-input.is-valid:focus~.custom-control-label:before,.was-validated .is-focused .custom-control-input:valid:focus~.custom-control-label:before{box-shadow:0 0 0 1px #fafafa,0 0 0 .2rem hsla(0,0%,60%,.25)}.is-focused .custom-file-input.is-valid~.custom-file-label,.was-validated .is-focused .custom-file-input:valid~.custom-file-label{border-color:#999}.is-focused .custom-file-input.is-valid~.custom-file-label:before,.was-validated .is-focused .custom-file-input:valid~.custom-file-label:before{border-color:inherit}.is-focused .custom-file-input.is-valid~.valid-feedback,.is-focused .custom-file-input.is-valid~.valid-tooltip,.was-validated .is-focused .custom-file-input:valid~.valid-feedback,.was-validated .is-focused .custom-file-input:valid~.valid-tooltip{display:block}.is-focused .custom-file-input.is-valid:focus~.custom-file-label,.was-validated .is-focused .custom-file-input:valid:focus~.custom-file-label{box-shadow:0 0 0 .2rem hsla(0,0%,60%,.25)}.is-focused [class*=" bmd-label"],.is-focused [class^=bmd-label]{color:#9c27b0}.is-focused .bmd-label-placeholder{color:#999}.is-focused .form-control{border-color:#d2d2d2}.is-focused .bmd-help{color:#555}.has-success [class*=" bmd-label"],.has-success [class^=bmd-label]{color:#4caf50}.has-success .form-control,.is-focused .has-success .form-control{background-image:linear-gradient(0deg,#4caf50 2px,rgba(76,175,80,0) 0),linear-gradient(0deg,#d2d2d2 1px,hsla(0,0%,82%,0) 0)}.has-success .form-control:invalid{background-image:linear-gradient(0deg,#f44336 2px,rgba(244,67,54,0) 0),linear-gradient(0deg,#d2d2d2 1px,hsla(0,0%,82%,0) 0)}.has-success .form-control:read-only{background-image:linear-gradient(0deg,#d2d2d2 1px,hsla(0,0%,82%,0) 0),linear-gradient(0deg,#d2d2d2 1px,hsla(0,0%,82%,0) 0)}.has-success .form-control.disabled,.has-success .form-control:disabled,.has-success .form-control[disabled],fieldset[disabled][disabled] .has-success .form-control{background-image:linear-gradient(90deg,#d2d2d2 0,#d2d2d2 30%,transparent 0,transparent);background-repeat:repeat-x;background-size:3px 1px}.has-success .form-control.form-control-success,.is-focused .has-success .form-control.form-control-success{background-image:linear-gradient(0deg,#4caf50 2px,rgba(76,175,80,0) 0),linear-gradient(0deg,#d2d2d2 1px,hsla(0,0%,82%,0) 0),"data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCA2MTIgNzkyIj48cGF0aCBmaWxsPSIjNWNiODVjIiBkPSJNMjMzLjggNjEwYy0xMy4zIDAtMjYtNi0zNC0xNi44TDkwLjUgNDQ4LjhDNzYuMyA0MzAgODAgNDAzLjMgOTguOCAzODljMTguOC0xNC4yIDQ1LjUtMTAuNCA1OS44IDguNGw3MiA5NUw0NTEuMyAyNDJjMTIuNS0yMCAzOC44LTI2LjIgNTguOC0xMy43IDIwIDEyLjQgMjYgMzguNyAxMy43IDU4LjhMMjcwIDU5MGMtNy40IDEyLTIwLjIgMTkuNC0zNC4zIDIwaC0yeiIvPjwvc3ZnPg=="}.has-success .form-control.form-control-warning,.is-focused .has-success .form-control.form-control-warning{background-image:linear-gradient(0deg,#4caf50 2px,rgba(76,175,80,0) 0),linear-gradient(0deg,#d2d2d2 1px,hsla(0,0%,82%,0) 0),"data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCA2MTIgNzkyIj48cGF0aCBmaWxsPSIjZjBhZDRlIiBkPSJNNjAzIDY0MC4ybC0yNzguNS01MDljLTMuOC02LjYtMTAuOC0xMC42LTE4LjUtMTAuNnMtMTQuNyA0LTE4LjUgMTAuNkw5IDY0MC4yYy0zLjcgNi41LTMuNiAxNC40LjIgMjAuOCAzLjggNi41IDEwLjggMTAuNCAxOC4zIDEwLjRoNTU3YzcuNiAwIDE0LjYtNCAxOC40LTEwLjQgMy41LTYuNCAzLjYtMTQuNCAwLTIwLjh6bS0yNjYuNC0zMGgtNjEuMlY1NDloNjEuMnY2MS4yem0wLTEwN2gtNjEuMlYzMDRoNjEuMnYxOTl6Ii8+PC9zdmc+"}.has-success .form-control.form-control-danger,.is-focused .has-success .form-control.form-control-danger{background-image:linear-gradient(0deg,#4caf50 2px,rgba(76,175,80,0) 0),linear-gradient(0deg,#d2d2d2 1px,hsla(0,0%,82%,0) 0),"data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCA2MTIgNzkyIj48cGF0aCBmaWxsPSIjZDk1MzRmIiBkPSJNNDQ3IDU0NC40Yy0xNC40IDE0LjQtMzcuNiAxNC40LTUyIDBsLTg5LTkyLjctODkgOTIuN2MtMTQuNSAxNC40LTM3LjcgMTQuNC01MiAwLTE0LjQtMTQuNC0xNC40LTM3LjYgMC01Mmw5Mi40LTk2LjMtOTIuNC05Ni4zYy0xNC40LTE0LjQtMTQuNC0zNy42IDAtNTJzMzcuNi0xNC4zIDUyIDBsODkgOTIuOCA4OS4yLTkyLjdjMTQuNC0xNC40IDM3LjYtMTQuNCA1MiAwIDE0LjMgMTQuNCAxNC4zIDM3LjYgMCA1MkwzNTQuNiAzOTZsOTIuNCA5Ni40YzE0LjQgMTQuNCAxNC40IDM3LjYgMCA1MnoiLz48L3N2Zz4="}.has-success .is-focused .valid-feedback{display:none;width:100%;margin-top:.25rem;font-size:80%;color:#4caf50}.has-success .is-focused .valid-tooltip{position:absolute;top:100%;z-index:5;display:none;max-width:100%;padding:.5rem;margin-top:.1rem;font-size:.875rem;line-height:1;color:#fff;background-color:rgba(76,175,80,.8);border-radius:.2rem}.has-success .is-focused .custom-select.is-valid,.has-success .is-focused .form-control.is-valid,.was-validated .has-success .is-focused .custom-select:valid,.was-validated .has-success .is-focused .form-control:valid{border-color:#4caf50}.has-success .is-focused .custom-select.is-valid:focus,.has-success .is-focused .form-control.is-valid:focus,.was-validated .has-success .is-focused .custom-select:valid:focus,.was-validated .has-success .is-focused .form-control:valid:focus{border-color:#4caf50;box-shadow:0 0 0 .2rem rgba(76,175,80,.25)}.has-success .is-focused .custom-select.is-valid~.valid-feedback,.has-success .is-focused .custom-select.is-valid~.valid-tooltip,.has-success .is-focused .form-control.is-valid~.valid-feedback,.has-success .is-focused .form-control.is-valid~.valid-tooltip,.was-validated .has-success .is-focused .custom-select:valid~.valid-feedback,.was-validated .has-success .is-focused .custom-select:valid~.valid-tooltip,.was-validated .has-success .is-focused .form-control:valid~.valid-feedback,.was-validated .has-success .is-focused .form-control:valid~.valid-tooltip{display:block}.has-success .is-focused .form-check-input.is-valid~.form-check-label,.was-validated .has-success .is-focused .form-check-input:valid~.form-check-label{color:#4caf50}.has-success .is-focused .form-check-input.is-valid~.valid-feedback,.has-success .is-focused .form-check-input.is-valid~.valid-tooltip,.was-validated .has-success .is-focused .form-check-input:valid~.valid-feedback,.was-validated .has-success .is-focused .form-check-input:valid~.valid-tooltip{display:block}.has-success .is-focused .custom-control-input.is-valid~.custom-control-label,.was-validated .has-success .is-focused .custom-control-input:valid~.custom-control-label{color:#4caf50}.has-success .is-focused .custom-control-input.is-valid~.custom-control-label:before,.was-validated .has-success .is-focused .custom-control-input:valid~.custom-control-label:before{background-color:#a3d7a5}.has-success .is-focused .custom-control-input.is-valid~.valid-feedback,.has-success .is-focused .custom-control-input.is-valid~.valid-tooltip,.was-validated .has-success .is-focused .custom-control-input:valid~.valid-feedback,.was-validated .has-success .is-focused .custom-control-input:valid~.valid-tooltip{display:block}.has-success .is-focused .custom-control-input.is-valid:checked~.custom-control-label:before,.was-validated .has-success .is-focused .custom-control-input:valid:checked~.custom-control-label:before{background-color:#6ec071}.has-success .is-focused .custom-control-input.is-valid:focus~.custom-control-label:before,.was-validated .has-success .is-focused .custom-control-input:valid:focus~.custom-control-label:before{box-shadow:0 0 0 1px #fafafa,0 0 0 .2rem rgba(76,175,80,.25)}.has-success .is-focused .custom-file-input.is-valid~.custom-file-label,.was-validated .has-success .is-focused .custom-file-input:valid~.custom-file-label{border-color:#4caf50}.has-success .is-focused .custom-file-input.is-valid~.custom-file-label:before,.was-validated .has-success .is-focused .custom-file-input:valid~.custom-file-label:before{border-color:inherit}.has-success .is-focused .custom-file-input.is-valid~.valid-feedback,.has-success .is-focused .custom-file-input.is-valid~.valid-tooltip,.was-validated .has-success .is-focused .custom-file-input:valid~.valid-feedback,.was-validated .has-success .is-focused .custom-file-input:valid~.valid-tooltip{display:block}.has-success .is-focused .custom-file-input.is-valid:focus~.custom-file-label,.was-validated .has-success .is-focused .custom-file-input:valid:focus~.custom-file-label{box-shadow:0 0 0 .2rem rgba(76,175,80,.25)}.has-success .is-focused .bmd-label-placeholder,.has-success .is-focused [class*=" bmd-label"],.has-success .is-focused [class^=bmd-label]{color:#4caf50}.has-success .is-focused .form-control{border-color:#4caf50}.has-success .is-focused .bmd-help{color:#555}.has-info [class*=" bmd-label"],.has-info [class^=bmd-label]{color:#00bcd4}.has-info .form-control,.is-focused .has-info .form-control{background-image:linear-gradient(0deg,#00bcd4 2px,rgba(0,188,212,0) 0),linear-gradient(0deg,#d2d2d2 1px,hsla(0,0%,82%,0) 0)}.has-info .form-control:invalid{background-image:linear-gradient(0deg,#f44336 2px,rgba(244,67,54,0) 0),linear-gradient(0deg,#d2d2d2 1px,hsla(0,0%,82%,0) 0)}.has-info .form-control:read-only{background-image:linear-gradient(0deg,#d2d2d2 1px,hsla(0,0%,82%,0) 0),linear-gradient(0deg,#d2d2d2 1px,hsla(0,0%,82%,0) 0)}.has-info .form-control.disabled,.has-info .form-control:disabled,.has-info .form-control[disabled],fieldset[disabled][disabled] .has-info .form-control{background-image:linear-gradient(90deg,#d2d2d2 0,#d2d2d2 30%,transparent 0,transparent);background-repeat:repeat-x;background-size:3px 1px}.has-info .form-control.form-control-success,.is-focused .has-info .form-control.form-control-success{background-image:linear-gradient(0deg,#00bcd4 2px,rgba(0,188,212,0) 0),linear-gradient(0deg,#d2d2d2 1px,hsla(0,0%,82%,0) 0),"data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCA2MTIgNzkyIj48cGF0aCBmaWxsPSIjNWNiODVjIiBkPSJNMjMzLjggNjEwYy0xMy4zIDAtMjYtNi0zNC0xNi44TDkwLjUgNDQ4LjhDNzYuMyA0MzAgODAgNDAzLjMgOTguOCAzODljMTguOC0xNC4yIDQ1LjUtMTAuNCA1OS44IDguNGw3MiA5NUw0NTEuMyAyNDJjMTIuNS0yMCAzOC44LTI2LjIgNTguOC0xMy43IDIwIDEyLjQgMjYgMzguNyAxMy43IDU4LjhMMjcwIDU5MGMtNy40IDEyLTIwLjIgMTkuNC0zNC4zIDIwaC0yeiIvPjwvc3ZnPg=="}.has-info .form-control.form-control-warning,.is-focused .has-info .form-control.form-control-warning{background-image:linear-gradient(0deg,#00bcd4 2px,rgba(0,188,212,0) 0),linear-gradient(0deg,#d2d2d2 1px,hsla(0,0%,82%,0) 0),"data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCA2MTIgNzkyIj48cGF0aCBmaWxsPSIjZjBhZDRlIiBkPSJNNjAzIDY0MC4ybC0yNzguNS01MDljLTMuOC02LjYtMTAuOC0xMC42LTE4LjUtMTAuNnMtMTQuNyA0LTE4LjUgMTAuNkw5IDY0MC4yYy0zLjcgNi41LTMuNiAxNC40LjIgMjAuOCAzLjggNi41IDEwLjggMTAuNCAxOC4zIDEwLjRoNTU3YzcuNiAwIDE0LjYtNCAxOC40LTEwLjQgMy41LTYuNCAzLjYtMTQuNCAwLTIwLjh6bS0yNjYuNC0zMGgtNjEuMlY1NDloNjEuMnY2MS4yem0wLTEwN2gtNjEuMlYzMDRoNjEuMnYxOTl6Ii8+PC9zdmc+"}.has-info .form-control.form-control-danger,.is-focused .has-info .form-control.form-control-danger{background-image:linear-gradient(0deg,#00bcd4 2px,rgba(0,188,212,0) 0),linear-gradient(0deg,#d2d2d2 1px,hsla(0,0%,82%,0) 0),"data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCA2MTIgNzkyIj48cGF0aCBmaWxsPSIjZDk1MzRmIiBkPSJNNDQ3IDU0NC40Yy0xNC40IDE0LjQtMzcuNiAxNC40LTUyIDBsLTg5LTkyLjctODkgOTIuN2MtMTQuNSAxNC40LTM3LjcgMTQuNC01MiAwLTE0LjQtMTQuNC0xNC40LTM3LjYgMC01Mmw5Mi40LTk2LjMtOTIuNC05Ni4zYy0xNC40LTE0LjQtMTQuNC0zNy42IDAtNTJzMzcuNi0xNC4zIDUyIDBsODkgOTIuOCA4OS4yLTkyLjdjMTQuNC0xNC40IDM3LjYtMTQuNCA1MiAwIDE0LjMgMTQuNCAxNC4zIDM3LjYgMCA1MkwzNTQuNiAzOTZsOTIuNCA5Ni40YzE0LjQgMTQuNCAxNC40IDM3LjYgMCA1MnoiLz48L3N2Zz4="}.has-info .is-focused .valid-feedback{display:none;width:100%;margin-top:.25rem;font-size:80%;color:#00bcd4}.has-info .is-focused .valid-tooltip{position:absolute;top:100%;z-index:5;display:none;max-width:100%;padding:.5rem;margin-top:.1rem;font-size:.875rem;line-height:1;color:#fff;background-color:rgba(0,188,212,.8);border-radius:.2rem}.has-info .is-focused .custom-select.is-valid,.has-info .is-focused .form-control.is-valid,.was-validated .has-info .is-focused .custom-select:valid,.was-validated .has-info .is-focused .form-control:valid{border-color:#00bcd4}.has-info .is-focused .custom-select.is-valid:focus,.has-info .is-focused .form-control.is-valid:focus,.was-validated .has-info .is-focused .custom-select:valid:focus,.was-validated .has-info .is-focused .form-control:valid:focus{border-color:#00bcd4;box-shadow:0 0 0 .2rem rgba(0,188,212,.25)}.has-info .is-focused .custom-select.is-valid~.valid-feedback,.has-info .is-focused .custom-select.is-valid~.valid-tooltip,.has-info .is-focused .form-control.is-valid~.valid-feedback,.has-info .is-focused .form-control.is-valid~.valid-tooltip,.was-validated .has-info .is-focused .custom-select:valid~.valid-feedback,.was-validated .has-info .is-focused .custom-select:valid~.valid-tooltip,.was-validated .has-info .is-focused .form-control:valid~.valid-feedback,.was-validated .has-info .is-focused .form-control:valid~.valid-tooltip{display:block}.has-info .is-focused .form-check-input.is-valid~.form-check-label,.was-validated .has-info .is-focused .form-check-input:valid~.form-check-label{color:#00bcd4}.has-info .is-focused .form-check-input.is-valid~.valid-feedback,.has-info .is-focused .form-check-input.is-valid~.valid-tooltip,.was-validated .has-info .is-focused .form-check-input:valid~.valid-feedback,.was-validated .has-info .is-focused .form-check-input:valid~.valid-tooltip{display:block}.has-info .is-focused .custom-control-input.is-valid~.custom-control-label,.was-validated .has-info .is-focused .custom-control-input:valid~.custom-control-label{color:#00bcd4}.has-info .is-focused .custom-control-input.is-valid~.custom-control-label:before,.was-validated .has-info .is-focused .custom-control-input:valid~.custom-control-label:before{background-color:#55ecff}.has-info .is-focused .custom-control-input.is-valid~.valid-feedback,.has-info .is-focused .custom-control-input.is-valid~.valid-tooltip,.was-validated .has-info .is-focused .custom-control-input:valid~.valid-feedback,.was-validated .has-info .is-focused .custom-control-input:valid~.valid-tooltip{display:block}.has-info .is-focused .custom-control-input.is-valid:checked~.custom-control-label:before,.was-validated .has-info .is-focused .custom-control-input:valid:checked~.custom-control-label:before{background-color:#08e3ff}.has-info .is-focused .custom-control-input.is-valid:focus~.custom-control-label:before,.was-validated .has-info .is-focused .custom-control-input:valid:focus~.custom-control-label:before{box-shadow:0 0 0 1px #fafafa,0 0 0 .2rem rgba(0,188,212,.25)}.has-info .is-focused .custom-file-input.is-valid~.custom-file-label,.was-validated .has-info .is-focused .custom-file-input:valid~.custom-file-label{border-color:#00bcd4}.has-info .is-focused .custom-file-input.is-valid~.custom-file-label:before,.was-validated .has-info .is-focused .custom-file-input:valid~.custom-file-label:before{border-color:inherit}.has-info .is-focused .custom-file-input.is-valid~.valid-feedback,.has-info .is-focused .custom-file-input.is-valid~.valid-tooltip,.was-validated .has-info .is-focused .custom-file-input:valid~.valid-feedback,.was-validated .has-info .is-focused .custom-file-input:valid~.valid-tooltip{display:block}.has-info .is-focused .custom-file-input.is-valid:focus~.custom-file-label,.was-validated .has-info .is-focused .custom-file-input:valid:focus~.custom-file-label{box-shadow:0 0 0 .2rem rgba(0,188,212,.25)}.has-info .is-focused .bmd-label-placeholder,.has-info .is-focused [class*=" bmd-label"],.has-info .is-focused [class^=bmd-label]{color:#00bcd4}.has-info .is-focused .form-control{border-color:#00bcd4}.has-info .is-focused .bmd-help{color:#555}.has-white [class*=" bmd-label"],.has-white [class^=bmd-label]{color:#fff}.has-white .form-control,.is-focused .has-white .form-control{background-image:linear-gradient(0deg,#fff 2px,hsla(0,0%,100%,0) 0),linear-gradient(0deg,#fff 1px,hsla(0,0%,100%,0) 0)}.has-white .form-control:invalid{background-image:linear-gradient(0deg,#f44336 2px,rgba(244,67,54,0) 0),linear-gradient(0deg,#fff 1px,hsla(0,0%,100%,0) 0)}.has-white .form-control:read-only{background-image:linear-gradient(0deg,#d2d2d2 1px,hsla(0,0%,82%,0) 0),linear-gradient(0deg,#fff 1px,hsla(0,0%,100%,0) 0)}.has-white .form-control.disabled,.has-white .form-control:disabled,.has-white .form-control[disabled],fieldset[disabled][disabled] .has-white .form-control{background-image:linear-gradient(90deg,#fff 0,#fff 30%,transparent 0,transparent);background-repeat:repeat-x;background-size:3px 1px}.has-white .form-control.form-control-success,.is-focused .has-white .form-control.form-control-success{background-image:linear-gradient(0deg,#fff 2px,hsla(0,0%,100%,0) 0),linear-gradient(0deg,#fff 1px,hsla(0,0%,100%,0) 0),"data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCA2MTIgNzkyIj48cGF0aCBmaWxsPSIjNWNiODVjIiBkPSJNMjMzLjggNjEwYy0xMy4zIDAtMjYtNi0zNC0xNi44TDkwLjUgNDQ4LjhDNzYuMyA0MzAgODAgNDAzLjMgOTguOCAzODljMTguOC0xNC4yIDQ1LjUtMTAuNCA1OS44IDguNGw3MiA5NUw0NTEuMyAyNDJjMTIuNS0yMCAzOC44LTI2LjIgNTguOC0xMy43IDIwIDEyLjQgMjYgMzguNyAxMy43IDU4LjhMMjcwIDU5MGMtNy40IDEyLTIwLjIgMTkuNC0zNC4zIDIwaC0yeiIvPjwvc3ZnPg=="}.has-white .form-control.form-control-warning,.is-focused .has-white .form-control.form-control-warning{background-image:linear-gradient(0deg,#fff 2px,hsla(0,0%,100%,0) 0),linear-gradient(0deg,#fff 1px,hsla(0,0%,100%,0) 0),"data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCA2MTIgNzkyIj48cGF0aCBmaWxsPSIjZjBhZDRlIiBkPSJNNjAzIDY0MC4ybC0yNzguNS01MDljLTMuOC02LjYtMTAuOC0xMC42LTE4LjUtMTAuNnMtMTQuNyA0LTE4LjUgMTAuNkw5IDY0MC4yYy0zLjcgNi41LTMuNiAxNC40LjIgMjAuOCAzLjggNi41IDEwLjggMTAuNCAxOC4zIDEwLjRoNTU3YzcuNiAwIDE0LjYtNCAxOC40LTEwLjQgMy41LTYuNCAzLjYtMTQuNCAwLTIwLjh6bS0yNjYuNC0zMGgtNjEuMlY1NDloNjEuMnY2MS4yem0wLTEwN2gtNjEuMlYzMDRoNjEuMnYxOTl6Ii8+PC9zdmc+"}.has-white .form-control.form-control-danger,.is-focused .has-white .form-control.form-control-danger{background-image:linear-gradient(0deg,#fff 2px,hsla(0,0%,100%,0) 0),linear-gradient(0deg,#fff 1px,hsla(0,0%,100%,0) 0),"data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCA2MTIgNzkyIj48cGF0aCBmaWxsPSIjZDk1MzRmIiBkPSJNNDQ3IDU0NC40Yy0xNC40IDE0LjQtMzcuNiAxNC40LTUyIDBsLTg5LTkyLjctODkgOTIuN2MtMTQuNSAxNC40LTM3LjcgMTQuNC01MiAwLTE0LjQtMTQuNC0xNC40LTM3LjYgMC01Mmw5Mi40LTk2LjMtOTIuNC05Ni4zYy0xNC40LTE0LjQtMTQuNC0zNy42IDAtNTJzMzcuNi0xNC4zIDUyIDBsODkgOTIuOCA4OS4yLTkyLjdjMTQuNC0xNC40IDM3LjYtMTQuNCA1MiAwIDE0LjMgMTQuNCAxNC4zIDM3LjYgMCA1MkwzNTQuNiAzOTZsOTIuNCA5Ni40YzE0LjQgMTQuNCAxNC40IDM3LjYgMCA1MnoiLz48L3N2Zz4="}.has-white .is-focused .valid-feedback{display:none;width:100%;margin-top:.25rem;font-size:80%;color:#fff}.has-white .is-focused .valid-tooltip{position:absolute;top:100%;z-index:5;display:none;max-width:100%;padding:.5rem;margin-top:.1rem;font-size:.875rem;line-height:1;color:#fff;background-color:hsla(0,0%,100%,.8);border-radius:.2rem}.has-white .is-focused .custom-select.is-valid,.has-white .is-focused .form-control.is-valid,.was-validated .has-white .is-focused .custom-select:valid,.was-validated .has-white .is-focused .form-control:valid{border-color:#fff}.has-white .is-focused .custom-select.is-valid:focus,.has-white .is-focused .form-control.is-valid:focus,.was-validated .has-white .is-focused .custom-select:valid:focus,.was-validated .has-white .is-focused .form-control:valid:focus{border-color:#fff;box-shadow:0 0 0 .2rem hsla(0,0%,100%,.25)}.has-white .is-focused .custom-select.is-valid~.valid-feedback,.has-white .is-focused .custom-select.is-valid~.valid-tooltip,.has-white .is-focused .form-control.is-valid~.valid-feedback,.has-white .is-focused .form-control.is-valid~.valid-tooltip,.was-validated .has-white .is-focused .custom-select:valid~.valid-feedback,.was-validated .has-white .is-focused .custom-select:valid~.valid-tooltip,.was-validated .has-white .is-focused .form-control:valid~.valid-feedback,.was-validated .has-white .is-focused .form-control:valid~.valid-tooltip{display:block}.has-white .is-focused .form-check-input.is-valid~.form-check-label,.was-validated .has-white .is-focused .form-check-input:valid~.form-check-label{color:#fff}.has-white .is-focused .form-check-input.is-valid~.valid-feedback,.has-white .is-focused .form-check-input.is-valid~.valid-tooltip,.was-validated .has-white .is-focused .form-check-input:valid~.valid-feedback,.was-validated .has-white .is-focused .form-check-input:valid~.valid-tooltip{display:block}.has-white .is-focused .custom-control-input.is-valid~.custom-control-label,.was-validated .has-white .is-focused .custom-control-input:valid~.custom-control-label{color:#fff}.has-white .is-focused .custom-control-input.is-valid~.custom-control-label:before,.was-validated .has-white .is-focused .custom-control-input:valid~.custom-control-label:before{background-color:#fff}.has-white .is-focused .custom-control-input.is-valid~.valid-feedback,.has-white .is-focused .custom-control-input.is-valid~.valid-tooltip,.was-validated .has-white .is-focused .custom-control-input:valid~.valid-feedback,.was-validated .has-white .is-focused .custom-control-input:valid~.valid-tooltip{display:block}.has-white .is-focused .custom-control-input.is-valid:checked~.custom-control-label:before,.was-validated .has-white .is-focused .custom-control-input:valid:checked~.custom-control-label:before{background-color:#fff}.has-white .is-focused .custom-control-input.is-valid:focus~.custom-control-label:before,.was-validated .has-white .is-focused .custom-control-input:valid:focus~.custom-control-label:before{box-shadow:0 0 0 1px #fafafa,0 0 0 .2rem hsla(0,0%,100%,.25)}.has-white .is-focused .custom-file-input.is-valid~.custom-file-label,.was-validated .has-white .is-focused .custom-file-input:valid~.custom-file-label{border-color:#fff}.has-white .is-focused .custom-file-input.is-valid~.custom-file-label:before,.was-validated .has-white .is-focused .custom-file-input:valid~.custom-file-label:before{border-color:inherit}.has-white .is-focused .custom-file-input.is-valid~.valid-feedback,.has-white .is-focused .custom-file-input.is-valid~.valid-tooltip,.was-validated .has-white .is-focused .custom-file-input:valid~.valid-feedback,.was-validated .has-white .is-focused .custom-file-input:valid~.valid-tooltip{display:block}.has-white .is-focused .custom-file-input.is-valid:focus~.custom-file-label,.was-validated .has-white .is-focused .custom-file-input:valid:focus~.custom-file-label{box-shadow:0 0 0 .2rem hsla(0,0%,100%,.25)}.has-white .is-focused .bmd-label-placeholder,.has-white .is-focused [class*=" bmd-label"],.has-white .is-focused [class^=bmd-label]{color:#fff}.has-white .is-focused .form-control{border-color:#fff}.has-white .is-focused .bmd-help{color:#555}.has-white .form-control:focus{color:#fff}.has-warning [class*=" bmd-label"],.has-warning [class^=bmd-label]{color:#ff9800}.has-warning .form-control,.is-focused .has-warning .form-control{background-image:linear-gradient(0deg,#ff9800 2px,rgba(255,152,0,0) 0),linear-gradient(0deg,#d2d2d2 1px,hsla(0,0%,82%,0) 0)}.has-warning .form-control:invalid{background-image:linear-gradient(0deg,#f44336 2px,rgba(244,67,54,0) 0),linear-gradient(0deg,#d2d2d2 1px,hsla(0,0%,82%,0) 0)}.has-warning .form-control:read-only{background-image:linear-gradient(0deg,#d2d2d2 1px,hsla(0,0%,82%,0) 0),linear-gradient(0deg,#d2d2d2 1px,hsla(0,0%,82%,0) 0)}.has-warning .form-control.disabled,.has-warning .form-control:disabled,.has-warning .form-control[disabled],fieldset[disabled][disabled] .has-warning .form-control{background-image:linear-gradient(90deg,#d2d2d2 0,#d2d2d2 30%,transparent 0,transparent);background-repeat:repeat-x;background-size:3px 1px}.has-warning .form-control.form-control-success,.is-focused .has-warning .form-control.form-control-success{background-image:linear-gradient(0deg,#ff9800 2px,rgba(255,152,0,0) 0),linear-gradient(0deg,#d2d2d2 1px,hsla(0,0%,82%,0) 0),"data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCA2MTIgNzkyIj48cGF0aCBmaWxsPSIjNWNiODVjIiBkPSJNMjMzLjggNjEwYy0xMy4zIDAtMjYtNi0zNC0xNi44TDkwLjUgNDQ4LjhDNzYuMyA0MzAgODAgNDAzLjMgOTguOCAzODljMTguOC0xNC4yIDQ1LjUtMTAuNCA1OS44IDguNGw3MiA5NUw0NTEuMyAyNDJjMTIuNS0yMCAzOC44LTI2LjIgNTguOC0xMy43IDIwIDEyLjQgMjYgMzguNyAxMy43IDU4LjhMMjcwIDU5MGMtNy40IDEyLTIwLjIgMTkuNC0zNC4zIDIwaC0yeiIvPjwvc3ZnPg=="}.has-warning .form-control.form-control-warning,.is-focused .has-warning .form-control.form-control-warning{background-image:linear-gradient(0deg,#ff9800 2px,rgba(255,152,0,0) 0),linear-gradient(0deg,#d2d2d2 1px,hsla(0,0%,82%,0) 0),"data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCA2MTIgNzkyIj48cGF0aCBmaWxsPSIjZjBhZDRlIiBkPSJNNjAzIDY0MC4ybC0yNzguNS01MDljLTMuOC02LjYtMTAuOC0xMC42LTE4LjUtMTAuNnMtMTQuNyA0LTE4LjUgMTAuNkw5IDY0MC4yYy0zLjcgNi41LTMuNiAxNC40LjIgMjAuOCAzLjggNi41IDEwLjggMTAuNCAxOC4zIDEwLjRoNTU3YzcuNiAwIDE0LjYtNCAxOC40LTEwLjQgMy41LTYuNCAzLjYtMTQuNCAwLTIwLjh6bS0yNjYuNC0zMGgtNjEuMlY1NDloNjEuMnY2MS4yem0wLTEwN2gtNjEuMlYzMDRoNjEuMnYxOTl6Ii8+PC9zdmc+"}.has-warning .form-control.form-control-danger,.is-focused .has-warning .form-control.form-control-danger{background-image:linear-gradient(0deg,#ff9800 2px,rgba(255,152,0,0) 0),linear-gradient(0deg,#d2d2d2 1px,hsla(0,0%,82%,0) 0),"data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCA2MTIgNzkyIj48cGF0aCBmaWxsPSIjZDk1MzRmIiBkPSJNNDQ3IDU0NC40Yy0xNC40IDE0LjQtMzcuNiAxNC40LTUyIDBsLTg5LTkyLjctODkgOTIuN2MtMTQuNSAxNC40LTM3LjcgMTQuNC01MiAwLTE0LjQtMTQuNC0xNC40LTM3LjYgMC01Mmw5Mi40LTk2LjMtOTIuNC05Ni4zYy0xNC40LTE0LjQtMTQuNC0zNy42IDAtNTJzMzcuNi0xNC4zIDUyIDBsODkgOTIuOCA4OS4yLTkyLjdjMTQuNC0xNC40IDM3LjYtMTQuNCA1MiAwIDE0LjMgMTQuNCAxNC4zIDM3LjYgMCA1MkwzNTQuNiAzOTZsOTIuNCA5Ni40YzE0LjQgMTQuNCAxNC40IDM3LjYgMCA1MnoiLz48L3N2Zz4="}.has-warning .is-focused .valid-feedback{display:none;width:100%;margin-top:.25rem;font-size:80%;color:#ff9800}.has-warning .is-focused .valid-tooltip{position:absolute;top:100%;z-index:5;display:none;max-width:100%;padding:.5rem;margin-top:.1rem;font-size:.875rem;line-height:1;color:#fff;background-color:rgba(255,152,0,.8);border-radius:.2rem}.has-warning .is-focused .custom-select.is-valid,.has-warning .is-focused .form-control.is-valid,.was-validated .has-warning .is-focused .custom-select:valid,.was-validated .has-warning .is-focused .form-control:valid{border-color:#ff9800}.has-warning .is-focused .custom-select.is-valid:focus,.has-warning .is-focused .form-control.is-valid:focus,.was-validated .has-warning .is-focused .custom-select:valid:focus,.was-validated .has-warning .is-focused .form-control:valid:focus{border-color:#ff9800;box-shadow:0 0 0 .2rem rgba(255,152,0,.25)}.has-warning .is-focused .custom-select.is-valid~.valid-feedback,.has-warning .is-focused .custom-select.is-valid~.valid-tooltip,.has-warning .is-focused .form-control.is-valid~.valid-feedback,.has-warning .is-focused .form-control.is-valid~.valid-tooltip,.was-validated .has-warning .is-focused .custom-select:valid~.valid-feedback,.was-validated .has-warning .is-focused .custom-select:valid~.valid-tooltip,.was-validated .has-warning .is-focused .form-control:valid~.valid-feedback,.was-validated .has-warning .is-focused .form-control:valid~.valid-tooltip{display:block}.has-warning .is-focused .form-check-input.is-valid~.form-check-label,.was-validated .has-warning .is-focused .form-check-input:valid~.form-check-label{color:#ff9800}.has-warning .is-focused .form-check-input.is-valid~.valid-feedback,.has-warning .is-focused .form-check-input.is-valid~.valid-tooltip,.was-validated .has-warning .is-focused .form-check-input:valid~.valid-feedback,.was-validated .has-warning .is-focused .form-check-input:valid~.valid-tooltip{display:block}.has-warning .is-focused .custom-control-input.is-valid~.custom-control-label,.was-validated .has-warning .is-focused .custom-control-input:valid~.custom-control-label{color:#ff9800}.has-warning .is-focused .custom-control-input.is-valid~.custom-control-label:before,.was-validated .has-warning .is-focused .custom-control-input:valid~.custom-control-label:before{background-color:#ffcc80}.has-warning .is-focused .custom-control-input.is-valid~.valid-feedback,.has-warning .is-focused .custom-control-input.is-valid~.valid-tooltip,.was-validated .has-warning .is-focused .custom-control-input:valid~.valid-feedback,.was-validated .has-warning .is-focused .custom-control-input:valid~.valid-tooltip{display:block}.has-warning .is-focused .custom-control-input.is-valid:checked~.custom-control-label:before,.was-validated .has-warning .is-focused .custom-control-input:valid:checked~.custom-control-label:before{background-color:#ffad33}.has-warning .is-focused .custom-control-input.is-valid:focus~.custom-control-label:before,.was-validated .has-warning .is-focused .custom-control-input:valid:focus~.custom-control-label:before{box-shadow:0 0 0 1px #fafafa,0 0 0 .2rem rgba(255,152,0,.25)}.has-warning .is-focused .custom-file-input.is-valid~.custom-file-label,.was-validated .has-warning .is-focused .custom-file-input:valid~.custom-file-label{border-color:#ff9800}.has-warning .is-focused .custom-file-input.is-valid~.custom-file-label:before,.was-validated .has-warning .is-focused .custom-file-input:valid~.custom-file-label:before{border-color:inherit}.has-warning .is-focused .custom-file-input.is-valid~.valid-feedback,.has-warning .is-focused .custom-file-input.is-valid~.valid-tooltip,.was-validated .has-warning .is-focused .custom-file-input:valid~.valid-feedback,.was-validated .has-warning .is-focused .custom-file-input:valid~.valid-tooltip{display:block}.has-warning .is-focused .custom-file-input.is-valid:focus~.custom-file-label,.was-validated .has-warning .is-focused .custom-file-input:valid:focus~.custom-file-label{box-shadow:0 0 0 .2rem rgba(255,152,0,.25)}.has-warning .is-focused .bmd-label-placeholder,.has-warning .is-focused [class*=" bmd-label"],.has-warning .is-focused [class^=bmd-label]{color:#ff9800}.has-warning .is-focused .form-control{border-color:#ff9800}.has-warning .is-focused .bmd-help{color:#555}.has-danger [class*=" bmd-label"],.has-danger [class^=bmd-label]{color:#f44336}.has-danger .form-control,.has-danger .form-control:invalid,.is-focused .has-danger .form-control{background-image:linear-gradient(0deg,#f44336 2px,rgba(244,67,54,0) 0),linear-gradient(0deg,#d2d2d2 1px,hsla(0,0%,82%,0) 0)}.has-danger .form-control:read-only{background-image:linear-gradient(0deg,#d2d2d2 1px,hsla(0,0%,82%,0) 0),linear-gradient(0deg,#d2d2d2 1px,hsla(0,0%,82%,0) 0)}.has-danger .form-control.disabled,.has-danger .form-control:disabled,.has-danger .form-control[disabled],fieldset[disabled][disabled] .has-danger .form-control{background-image:linear-gradient(90deg,#d2d2d2 0,#d2d2d2 30%,transparent 0,transparent);background-repeat:repeat-x;background-size:3px 1px}.has-danger .form-control.form-control-success,.is-focused .has-danger .form-control.form-control-success{background-image:linear-gradient(0deg,#f44336 2px,rgba(244,67,54,0) 0),linear-gradient(0deg,#d2d2d2 1px,hsla(0,0%,82%,0) 0),"data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCA2MTIgNzkyIj48cGF0aCBmaWxsPSIjNWNiODVjIiBkPSJNMjMzLjggNjEwYy0xMy4zIDAtMjYtNi0zNC0xNi44TDkwLjUgNDQ4LjhDNzYuMyA0MzAgODAgNDAzLjMgOTguOCAzODljMTguOC0xNC4yIDQ1LjUtMTAuNCA1OS44IDguNGw3MiA5NUw0NTEuMyAyNDJjMTIuNS0yMCAzOC44LTI2LjIgNTguOC0xMy43IDIwIDEyLjQgMjYgMzguNyAxMy43IDU4LjhMMjcwIDU5MGMtNy40IDEyLTIwLjIgMTkuNC0zNC4zIDIwaC0yeiIvPjwvc3ZnPg=="}.has-danger .form-control.form-control-warning,.is-focused .has-danger .form-control.form-control-warning{background-image:linear-gradient(0deg,#f44336 2px,rgba(244,67,54,0) 0),linear-gradient(0deg,#d2d2d2 1px,hsla(0,0%,82%,0) 0),"data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCA2MTIgNzkyIj48cGF0aCBmaWxsPSIjZjBhZDRlIiBkPSJNNjAzIDY0MC4ybC0yNzguNS01MDljLTMuOC02LjYtMTAuOC0xMC42LTE4LjUtMTAuNnMtMTQuNyA0LTE4LjUgMTAuNkw5IDY0MC4yYy0zLjcgNi41LTMuNiAxNC40LjIgMjAuOCAzLjggNi41IDEwLjggMTAuNCAxOC4zIDEwLjRoNTU3YzcuNiAwIDE0LjYtNCAxOC40LTEwLjQgMy41LTYuNCAzLjYtMTQuNCAwLTIwLjh6bS0yNjYuNC0zMGgtNjEuMlY1NDloNjEuMnY2MS4yem0wLTEwN2gtNjEuMlYzMDRoNjEuMnYxOTl6Ii8+PC9zdmc+"}.has-danger .form-control.form-control-danger,.is-focused .has-danger .form-control.form-control-danger{background-image:linear-gradient(0deg,#f44336 2px,rgba(244,67,54,0) 0),linear-gradient(0deg,#d2d2d2 1px,hsla(0,0%,82%,0) 0),"data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCA2MTIgNzkyIj48cGF0aCBmaWxsPSIjZDk1MzRmIiBkPSJNNDQ3IDU0NC40Yy0xNC40IDE0LjQtMzcuNiAxNC40LTUyIDBsLTg5LTkyLjctODkgOTIuN2MtMTQuNSAxNC40LTM3LjcgMTQuNC01MiAwLTE0LjQtMTQuNC0xNC40LTM3LjYgMC01Mmw5Mi40LTk2LjMtOTIuNC05Ni4zYy0xNC40LTE0LjQtMTQuNC0zNy42IDAtNTJzMzcuNi0xNC4zIDUyIDBsODkgOTIuOCA4OS4yLTkyLjdjMTQuNC0xNC40IDM3LjYtMTQuNCA1MiAwIDE0LjMgMTQuNCAxNC4zIDM3LjYgMCA1MkwzNTQuNiAzOTZsOTIuNCA5Ni40YzE0LjQgMTQuNCAxNC40IDM3LjYgMCA1MnoiLz48L3N2Zz4="}.has-danger .is-focused .valid-feedback{display:none;width:100%;margin-top:.25rem;font-size:80%;color:#f44336}.has-danger .is-focused .valid-tooltip{position:absolute;top:100%;z-index:5;display:none;max-width:100%;padding:.5rem;margin-top:.1rem;font-size:.875rem;line-height:1;color:#fff;background-color:rgba(244,67,54,.8);border-radius:.2rem}.has-danger .is-focused .custom-select.is-valid,.has-danger .is-focused .form-control.is-valid,.was-validated .has-danger .is-focused .custom-select:valid,.was-validated .has-danger .is-focused .form-control:valid{border-color:#f44336}.has-danger .is-focused .custom-select.is-valid:focus,.has-danger .is-focused .form-control.is-valid:focus,.was-validated .has-danger .is-focused .custom-select:valid:focus,.was-validated .has-danger .is-focused .form-control:valid:focus{border-color:#f44336;box-shadow:0 0 0 .2rem rgba(244,67,54,.25)}.has-danger .is-focused .custom-select.is-valid~.valid-feedback,.has-danger .is-focused .custom-select.is-valid~.valid-tooltip,.has-danger .is-focused .form-control.is-valid~.valid-feedback,.has-danger .is-focused .form-control.is-valid~.valid-tooltip,.was-validated .has-danger .is-focused .custom-select:valid~.valid-feedback,.was-validated .has-danger .is-focused .custom-select:valid~.valid-tooltip,.was-validated .has-danger .is-focused .form-control:valid~.valid-feedback,.was-validated .has-danger .is-focused .form-control:valid~.valid-tooltip{display:block}.has-danger .is-focused .form-check-input.is-valid~.form-check-label,.was-validated .has-danger .is-focused .form-check-input:valid~.form-check-label{color:#f44336}.has-danger .is-focused .form-check-input.is-valid~.valid-feedback,.has-danger .is-focused .form-check-input.is-valid~.valid-tooltip,.was-validated .has-danger .is-focused .form-check-input:valid~.valid-feedback,.was-validated .has-danger .is-focused .form-check-input:valid~.valid-tooltip{display:block}.has-danger .is-focused .custom-control-input.is-valid~.custom-control-label,.was-validated .has-danger .is-focused .custom-control-input:valid~.custom-control-label{color:#f44336}.has-danger .is-focused .custom-control-input.is-valid~.custom-control-label:before,.was-validated .has-danger .is-focused .custom-control-input:valid~.custom-control-label:before{background-color:#fbb4af}.has-danger .is-focused .custom-control-input.is-valid~.valid-feedback,.has-danger .is-focused .custom-control-input.is-valid~.valid-tooltip,.was-validated .has-danger .is-focused .custom-control-input:valid~.valid-feedback,.was-validated .has-danger .is-focused .custom-control-input:valid~.valid-tooltip{display:block}.has-danger .is-focused .custom-control-input.is-valid:checked~.custom-control-label:before,.was-validated .has-danger .is-focused .custom-control-input:valid:checked~.custom-control-label:before{background-color:#f77066}.has-danger .is-focused .custom-control-input.is-valid:focus~.custom-control-label:before,.was-validated .has-danger .is-focused .custom-control-input:valid:focus~.custom-control-label:before{box-shadow:0 0 0 1px #fafafa,0 0 0 .2rem rgba(244,67,54,.25)}.has-danger .is-focused .custom-file-input.is-valid~.custom-file-label,.was-validated .has-danger .is-focused .custom-file-input:valid~.custom-file-label{border-color:#f44336}.has-danger .is-focused .custom-file-input.is-valid~.custom-file-label:before,.was-validated .has-danger .is-focused .custom-file-input:valid~.custom-file-label:before{border-color:inherit}.has-danger .is-focused .custom-file-input.is-valid~.valid-feedback,.has-danger .is-focused .custom-file-input.is-valid~.valid-tooltip,.was-validated .has-danger .is-focused .custom-file-input:valid~.valid-feedback,.was-validated .has-danger .is-focused .custom-file-input:valid~.valid-tooltip{display:block}.has-danger .is-focused .custom-file-input.is-valid:focus~.custom-file-label,.was-validated .has-danger .is-focused .custom-file-input:valid:focus~.custom-file-label{box-shadow:0 0 0 .2rem rgba(244,67,54,.25)}.has-danger .is-focused .bmd-label-placeholder,.has-danger .is-focused [class*=" bmd-label"],.has-danger .is-focused [class^=bmd-label]{color:#f44336}.has-danger .is-focused .form-control{border-color:#f44336}.has-danger .is-focused .bmd-help{color:#555}.has-rose [class*=" bmd-label"],.has-rose [class^=bmd-label]{color:#e91e63}.has-rose .form-control,.is-focused .has-rose .form-control{background-image:linear-gradient(0deg,#e91e63 2px,rgba(233,30,99,0) 0),linear-gradient(0deg,#d2d2d2 1px,hsla(0,0%,82%,0) 0)}.has-rose .form-control:invalid{background-image:linear-gradient(0deg,#f44336 2px,rgba(244,67,54,0) 0),linear-gradient(0deg,#d2d2d2 1px,hsla(0,0%,82%,0) 0)}.has-rose .form-control:read-only{background-image:linear-gradient(0deg,#d2d2d2 1px,hsla(0,0%,82%,0) 0),linear-gradient(0deg,#d2d2d2 1px,hsla(0,0%,82%,0) 0)}.has-rose .form-control.disabled,.has-rose .form-control:disabled,.has-rose .form-control[disabled],fieldset[disabled][disabled] .has-rose .form-control{background-image:linear-gradient(90deg,#d2d2d2 0,#d2d2d2 30%,transparent 0,transparent);background-repeat:repeat-x;background-size:3px 1px}.has-rose .form-control.form-control-success,.is-focused .has-rose .form-control.form-control-success{background-image:linear-gradient(0deg,#e91e63 2px,rgba(233,30,99,0) 0),linear-gradient(0deg,#d2d2d2 1px,hsla(0,0%,82%,0) 0),"data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCA2MTIgNzkyIj48cGF0aCBmaWxsPSIjNWNiODVjIiBkPSJNMjMzLjggNjEwYy0xMy4zIDAtMjYtNi0zNC0xNi44TDkwLjUgNDQ4LjhDNzYuMyA0MzAgODAgNDAzLjMgOTguOCAzODljMTguOC0xNC4yIDQ1LjUtMTAuNCA1OS44IDguNGw3MiA5NUw0NTEuMyAyNDJjMTIuNS0yMCAzOC44LTI2LjIgNTguOC0xMy43IDIwIDEyLjQgMjYgMzguNyAxMy43IDU4LjhMMjcwIDU5MGMtNy40IDEyLTIwLjIgMTkuNC0zNC4zIDIwaC0yeiIvPjwvc3ZnPg=="}.has-rose .form-control.form-control-warning,.is-focused .has-rose .form-control.form-control-warning{background-image:linear-gradient(0deg,#e91e63 2px,rgba(233,30,99,0) 0),linear-gradient(0deg,#d2d2d2 1px,hsla(0,0%,82%,0) 0),"data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCA2MTIgNzkyIj48cGF0aCBmaWxsPSIjZjBhZDRlIiBkPSJNNjAzIDY0MC4ybC0yNzguNS01MDljLTMuOC02LjYtMTAuOC0xMC42LTE4LjUtMTAuNnMtMTQuNyA0LTE4LjUgMTAuNkw5IDY0MC4yYy0zLjcgNi41LTMuNiAxNC40LjIgMjAuOCAzLjggNi41IDEwLjggMTAuNCAxOC4zIDEwLjRoNTU3YzcuNiAwIDE0LjYtNCAxOC40LTEwLjQgMy41LTYuNCAzLjYtMTQuNCAwLTIwLjh6bS0yNjYuNC0zMGgtNjEuMlY1NDloNjEuMnY2MS4yem0wLTEwN2gtNjEuMlYzMDRoNjEuMnYxOTl6Ii8+PC9zdmc+"}.has-rose .form-control.form-control-danger,.is-focused .has-rose .form-control.form-control-danger{background-image:linear-gradient(0deg,#e91e63 2px,rgba(233,30,99,0) 0),linear-gradient(0deg,#d2d2d2 1px,hsla(0,0%,82%,0) 0),"data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCA2MTIgNzkyIj48cGF0aCBmaWxsPSIjZDk1MzRmIiBkPSJNNDQ3IDU0NC40Yy0xNC40IDE0LjQtMzcuNiAxNC40LTUyIDBsLTg5LTkyLjctODkgOTIuN2MtMTQuNSAxNC40LTM3LjcgMTQuNC01MiAwLTE0LjQtMTQuNC0xNC40LTM3LjYgMC01Mmw5Mi40LTk2LjMtOTIuNC05Ni4zYy0xNC40LTE0LjQtMTQuNC0zNy42IDAtNTJzMzcuNi0xNC4zIDUyIDBsODkgOTIuOCA4OS4yLTkyLjdjMTQuNC0xNC40IDM3LjYtMTQuNCA1MiAwIDE0LjMgMTQuNCAxNC4zIDM3LjYgMCA1MkwzNTQuNiAzOTZsOTIuNCA5Ni40YzE0LjQgMTQuNCAxNC40IDM3LjYgMCA1MnoiLz48L3N2Zz4="}.has-rose .is-focused .valid-feedback{display:none;width:100%;margin-top:.25rem;font-size:80%;color:#e91e63}.has-rose .is-focused .valid-tooltip{position:absolute;top:100%;z-index:5;display:none;max-width:100%;padding:.5rem;margin-top:.1rem;font-size:.875rem;line-height:1;color:#fff;background-color:rgba(233,30,99,.8);border-radius:.2rem}.has-rose .is-focused .custom-select.is-valid,.has-rose .is-focused .form-control.is-valid,.was-validated .has-rose .is-focused .custom-select:valid,.was-validated .has-rose .is-focused .form-control:valid{border-color:#e91e63}.has-rose .is-focused .custom-select.is-valid:focus,.has-rose .is-focused .form-control.is-valid:focus,.was-validated .has-rose .is-focused .custom-select:valid:focus,.was-validated .has-rose .is-focused .form-control:valid:focus{border-color:#e91e63;box-shadow:0 0 0 .2rem rgba(233,30,99,.25)}.has-rose .is-focused .custom-select.is-valid~.valid-feedback,.has-rose .is-focused .custom-select.is-valid~.valid-tooltip,.has-rose .is-focused .form-control.is-valid~.valid-feedback,.has-rose .is-focused .form-control.is-valid~.valid-tooltip,.was-validated .has-rose .is-focused .custom-select:valid~.valid-feedback,.was-validated .has-rose .is-focused .custom-select:valid~.valid-tooltip,.was-validated .has-rose .is-focused .form-control:valid~.valid-feedback,.was-validated .has-rose .is-focused .form-control:valid~.valid-tooltip{display:block}.has-rose .is-focused .form-check-input.is-valid~.form-check-label,.was-validated .has-rose .is-focused .form-check-input:valid~.form-check-label{color:#e91e63}.has-rose .is-focused .form-check-input.is-valid~.valid-feedback,.has-rose .is-focused .form-check-input.is-valid~.valid-tooltip,.was-validated .has-rose .is-focused .form-check-input:valid~.valid-feedback,.was-validated .has-rose .is-focused .form-check-input:valid~.valid-tooltip{display:block}.has-rose .is-focused .custom-control-input.is-valid~.custom-control-label,.was-validated .has-rose .is-focused .custom-control-input:valid~.custom-control-label{color:#e91e63}.has-rose .is-focused .custom-control-input.is-valid~.custom-control-label:before,.was-validated .has-rose .is-focused .custom-control-input:valid~.custom-control-label:before{background-color:#f492b4}.has-rose .is-focused .custom-control-input.is-valid~.valid-feedback,.has-rose .is-focused .custom-control-input.is-valid~.valid-tooltip,.was-validated .has-rose .is-focused .custom-control-input:valid~.valid-feedback,.was-validated .has-rose .is-focused .custom-control-input:valid~.valid-tooltip{display:block}.has-rose .is-focused .custom-control-input.is-valid:checked~.custom-control-label:before,.was-validated .has-rose .is-focused .custom-control-input:valid:checked~.custom-control-label:before{background-color:#ee4c83}.has-rose .is-focused .custom-control-input.is-valid:focus~.custom-control-label:before,.was-validated .has-rose .is-focused .custom-control-input:valid:focus~.custom-control-label:before{box-shadow:0 0 0 1px #fafafa,0 0 0 .2rem rgba(233,30,99,.25)}.has-rose .is-focused .custom-file-input.is-valid~.custom-file-label,.was-validated .has-rose .is-focused .custom-file-input:valid~.custom-file-label{border-color:#e91e63}.has-rose .is-focused .custom-file-input.is-valid~.custom-file-label:before,.was-validated .has-rose .is-focused .custom-file-input:valid~.custom-file-label:before{border-color:inherit}.has-rose .is-focused .custom-file-input.is-valid~.valid-feedback,.has-rose .is-focused .custom-file-input.is-valid~.valid-tooltip,.was-validated .has-rose .is-focused .custom-file-input:valid~.valid-feedback,.was-validated .has-rose .is-focused .custom-file-input:valid~.valid-tooltip{display:block}.has-rose .is-focused .custom-file-input.is-valid:focus~.custom-file-label,.was-validated .has-rose .is-focused .custom-file-input:valid:focus~.custom-file-label{box-shadow:0 0 0 .2rem rgba(233,30,99,.25)}.has-rose .is-focused .bmd-label-placeholder,.has-rose .is-focused [class*=" bmd-label"],.has-rose .is-focused [class^=bmd-label]{color:#e91e63}.has-rose .is-focused .form-control{border-color:#e91e63}.has-rose .is-focused .bmd-help{color:#555}.bmd-form-group{position:relative}.bmd-form-group:not(.has-success):not(.has-danger) [class*=" bmd-label"].bmd-label-floating,.bmd-form-group:not(.has-success):not(.has-danger) [class^=bmd-label].bmd-label-floating{color:#aaa}.bmd-form-group [class*=" bmd-label"],.bmd-form-group [class^=bmd-label]{position:absolute;pointer-events:none;transition:all .3s ease}.bmd-form-group [class*=" bmd-label"].bmd-label-floating,.bmd-form-group [class^=bmd-label].bmd-label-floating{will-change:left,top,contents;margin:0;line-height:1.4;font-weight:400}.bmd-form-group.is-filled .bmd-label-placeholder{display:none}.bmd-form-group.bmd-collapse-inline{display:flex;align-items:center;padding:0;min-height:2.1em}.bmd-form-group.bmd-collapse-inline .collapse{flex:1;display:none}.bmd-form-group.bmd-collapse-inline .collapse.show{max-width:1200px}.bmd-form-group.bmd-collapse-inline .collapse.show,.bmd-form-group.bmd-collapse-inline .collapsing,.bmd-form-group.bmd-collapse-inline .width:not(.collapse){display:block}.bmd-form-group.bmd-collapse-inline .collapsing{transition-duration:.2s;transition-timing-function:cubic-bezier(.4,0,.2,1)}.bmd-form-group .form-control,.bmd-form-group input::placeholder,.bmd-form-group label{line-height:1.1}.bmd-form-group label{color:#aaa}.bmd-form-group .checkbox label,.bmd-form-group .radio label,.bmd-form-group .switch label,.bmd-form-group label.checkbox-inline,.bmd-form-group label.radio-inline{line-height:1.5}.bmd-form-group .checkbox label,.bmd-form-group .radio label,.bmd-form-group label{font-size:.875rem}.bmd-form-group .bmd-label-floating,.bmd-form-group .bmd-label-placeholder{top:.6125rem}.bmd-form-group .is-filled .bmd-label-floating,.bmd-form-group .is-focused .bmd-label-floating{top:-1rem;left:0;font-size:.6875rem}.bmd-form-group .bmd-label-static{top:.35rem;left:0;font-size:.875rem}.bmd-form-group .bmd-help{margin-top:0;font-size:.75rem}.bmd-form-group .form-control.form-control-danger,.bmd-form-group .form-control.form-control-success,.bmd-form-group .form-control.form-control-warning{background-size:0 100%,100% 100%,.9375rem .9375rem}.bmd-form-group .form-control.form-control-danger,.bmd-form-group .form-control.form-control-danger:focus,.bmd-form-group .form-control.form-control-success,.bmd-form-group .form-control.form-control-success:focus,.bmd-form-group .form-control.form-control-warning,.bmd-form-group .form-control.form-control-warning:focus,.bmd-form-group.is-focused .bmd-form-group .form-control.form-control-danger,.bmd-form-group.is-focused .bmd-form-group .form-control.form-control-success,.bmd-form-group.is-focused .bmd-form-group .form-control.form-control-warning{padding-right:0;background-repeat:no-repeat,no-repeat;background-position:bottom,50% calc(100% - 1px),center right .46875rem}.bmd-form-group .form-control.form-control-danger:focus,.bmd-form-group .form-control.form-control-success:focus,.bmd-form-group .form-control.form-control-warning:focus,.bmd-form-group.is-focused .bmd-form-group .form-control.form-control-danger,.bmd-form-group.is-focused .bmd-form-group .form-control.form-control-success,.bmd-form-group.is-focused .bmd-form-group .form-control.form-control-warning{background-size:100% 100%,100% 100%,.9375rem .9375rem}.bmd-form-group.bmd-form-group-sm .form-control,.bmd-form-group.bmd-form-group-sm input::placeholder,.bmd-form-group.bmd-form-group-sm label{line-height:1.1}.bmd-form-group.bmd-form-group-sm label{color:#aaa}.bmd-form-group.bmd-form-group-sm .checkbox label,.bmd-form-group.bmd-form-group-sm .radio label,.bmd-form-group.bmd-form-group-sm .switch label,.bmd-form-group.bmd-form-group-sm label.checkbox-inline,.bmd-form-group.bmd-form-group-sm label.radio-inline{line-height:1.5}.bmd-form-group.bmd-form-group-sm .checkbox label,.bmd-form-group.bmd-form-group-sm .radio label,.bmd-form-group.bmd-form-group-sm label{font-size:.875rem}.bmd-form-group.bmd-form-group-sm .bmd-label-floating,.bmd-form-group.bmd-form-group-sm .bmd-label-placeholder{top:.175rem}.bmd-form-group.bmd-form-group-sm .is-filled .bmd-label-floating,.bmd-form-group.bmd-form-group-sm .is-focused .bmd-label-floating{top:-1.25rem;left:0;font-size:.6875rem}.bmd-form-group.bmd-form-group-sm .bmd-label-static{top:.1rem;left:0;font-size:.875rem}.bmd-form-group.bmd-form-group-sm .bmd-help{margin-top:0;font-size:.65625rem}.bmd-form-group.bmd-form-group-sm .form-control.form-control-danger,.bmd-form-group.bmd-form-group-sm .form-control.form-control-success,.bmd-form-group.bmd-form-group-sm .form-control.form-control-warning{background-size:0 100%,100% 100%,.6875rem .6875rem}.bmd-form-group.bmd-form-group-sm .form-control.form-control-danger,.bmd-form-group.bmd-form-group-sm .form-control.form-control-danger:focus,.bmd-form-group.bmd-form-group-sm .form-control.form-control-success,.bmd-form-group.bmd-form-group-sm .form-control.form-control-success:focus,.bmd-form-group.bmd-form-group-sm .form-control.form-control-warning,.bmd-form-group.bmd-form-group-sm .form-control.form-control-warning:focus,.bmd-form-group.is-focused .bmd-form-group.bmd-form-group-sm .form-control.form-control-danger,.bmd-form-group.is-focused .bmd-form-group.bmd-form-group-sm .form-control.form-control-success,.bmd-form-group.is-focused .bmd-form-group.bmd-form-group-sm .form-control.form-control-warning{padding-right:0;background-repeat:no-repeat,no-repeat;background-position:bottom,50% calc(100% - 1px),center right .34375rem}.bmd-form-group.bmd-form-group-sm .form-control.form-control-danger:focus,.bmd-form-group.bmd-form-group-sm .form-control.form-control-success:focus,.bmd-form-group.bmd-form-group-sm .form-control.form-control-warning:focus,.bmd-form-group.is-focused .bmd-form-group.bmd-form-group-sm .form-control.form-control-danger,.bmd-form-group.is-focused .bmd-form-group.bmd-form-group-sm .form-control.form-control-success,.bmd-form-group.is-focused .bmd-form-group.bmd-form-group-sm .form-control.form-control-warning{background-size:100% 100%,100% 100%,.6875rem .6875rem}.bmd-form-group.bmd-form-group-lg .form-control,.bmd-form-group.bmd-form-group-lg input::placeholder,.bmd-form-group.bmd-form-group-lg label{line-height:1.1}.bmd-form-group.bmd-form-group-lg label{color:#aaa}.bmd-form-group.bmd-form-group-lg .checkbox label,.bmd-form-group.bmd-form-group-lg .radio label,.bmd-form-group.bmd-form-group-lg .switch label,.bmd-form-group.bmd-form-group-lg label.checkbox-inline,.bmd-form-group.bmd-form-group-lg label.radio-inline{line-height:1.5}.bmd-form-group.bmd-form-group-lg .checkbox label,.bmd-form-group.bmd-form-group-lg .radio label,.bmd-form-group.bmd-form-group-lg label{font-size:.875rem}.bmd-form-group.bmd-form-group-lg .bmd-label-floating,.bmd-form-group.bmd-form-group-lg .bmd-label-placeholder{top:.7375rem}.bmd-form-group.bmd-form-group-lg .is-filled .bmd-label-floating,.bmd-form-group.bmd-form-group-lg .is-focused .bmd-label-floating{top:-1rem;left:0;font-size:.6875rem}.bmd-form-group.bmd-form-group-lg .bmd-label-static{top:.35rem;left:0;font-size:.875rem}.bmd-form-group.bmd-form-group-lg .bmd-help{margin-top:0;font-size:.9375rem}.bmd-form-group.bmd-form-group-lg .form-control.form-control-danger,.bmd-form-group.bmd-form-group-lg .form-control.form-control-success,.bmd-form-group.bmd-form-group-lg .form-control.form-control-warning{background-size:0 100%,100% 100%,1.1875rem 1.1875rem}.bmd-form-group.bmd-form-group-lg .form-control.form-control-danger,.bmd-form-group.bmd-form-group-lg .form-control.form-control-danger:focus,.bmd-form-group.bmd-form-group-lg .form-control.form-control-success,.bmd-form-group.bmd-form-group-lg .form-control.form-control-success:focus,.bmd-form-group.bmd-form-group-lg .form-control.form-control-warning,.bmd-form-group.bmd-form-group-lg .form-control.form-control-warning:focus,.bmd-form-group.is-focused .bmd-form-group.bmd-form-group-lg .form-control.form-control-danger,.bmd-form-group.is-focused .bmd-form-group.bmd-form-group-lg .form-control.form-control-success,.bmd-form-group.is-focused .bmd-form-group.bmd-form-group-lg .form-control.form-control-warning{padding-right:0;background-repeat:no-repeat,no-repeat;background-position:bottom,50% calc(100% - 1px),center right .59375rem}.bmd-form-group.bmd-form-group-lg .form-control.form-control-danger:focus,.bmd-form-group.bmd-form-group-lg .form-control.form-control-success:focus,.bmd-form-group.bmd-form-group-lg .form-control.form-control-warning:focus,.bmd-form-group.is-focused .bmd-form-group.bmd-form-group-lg .form-control.form-control-danger,.bmd-form-group.is-focused .bmd-form-group.bmd-form-group-lg .form-control.form-control-success,.bmd-form-group.is-focused .bmd-form-group.bmd-form-group-lg .form-control.form-control-warning{background-size:100% 100%,100% 100%,1.1875rem 1.1875rem}.form-control,input::placeholder,label{line-height:1.1}label{color:#aaa}.checkbox label,.radio label,.switch label,label.checkbox-inline,label.radio-inline{line-height:1.5}.checkbox label,.radio label,label{font-size:.875rem}.bmd-label-floating,.bmd-label-placeholder{top:.6125rem}.is-filled .bmd-label-floating,.is-focused .bmd-label-floating{top:-1rem;left:0;font-size:.6875rem}.bmd-label-static{top:.35rem;left:0;font-size:.875rem}.bmd-help{margin-top:0;font-size:.75rem}.form-control.form-control-danger,.form-control.form-control-success,.form-control.form-control-warning{background-size:0 100%,100% 100%,.9375rem .9375rem}.bmd-form-group.is-focused .form-control.form-control-danger,.bmd-form-group.is-focused .form-control.form-control-success,.bmd-form-group.is-focused .form-control.form-control-warning,.form-control.form-control-danger,.form-control.form-control-danger:focus,.form-control.form-control-success,.form-control.form-control-success:focus,.form-control.form-control-warning,.form-control.form-control-warning:focus{padding-right:0;background-repeat:no-repeat,no-repeat;background-position:bottom,50% calc(100% - 1px),center right .46875rem}.bmd-form-group.is-focused .form-control.form-control-danger,.bmd-form-group.is-focused .form-control.form-control-success,.bmd-form-group.is-focused .form-control.form-control-warning,.form-control.form-control-danger:focus,.form-control.form-control-success:focus,.form-control.form-control-warning:focus{background-size:100% 100%,100% 100%,.9375rem .9375rem}select,select.form-control{-moz-appearance:none;-webkit-appearance:none}@media (min-width:576px){.form-inline .input-group{display:inline-flex;align-items:center}}.form-control-feedback{position:absolute;top:4px;right:0;z-index:2;display:block;width:34px;height:34px;line-height:34px;text-align:center;pointer-events:none;opacity:0}.has-success .form-control-feedback{color:#4caf50;opacity:1}.has-danger .form-control-feedback{color:#f44336;opacity:1}.form-group{padding-bottom:10px;position:relative;margin:8px 0 0}.form-group .bmd-label-static{top:-10px}textarea{height:auto!important;resize:none;line-height:1.428571!important}.form-group input[type=file]{opacity:0;position:absolute;top:0;right:0;bottom:0;left:0;width:100%;height:100%;z-index:-1}.form-newsletter .form-group,.form-newsletter .input-group{float:left;width:78%;margin-right:2%;margin-top:9px;padding-top:5px}.form-newsletter .btn{float:left;width:20%;margin:9px 0 0}.form-file-upload .input-group-btn:last-child>.btn-round{border-radius:30px}.form-file-upload .input-group-btn .btn{margin:0}.form-file-upload .input-group{width:100%}.input-group .input-group-btn{padding:0 12px}.form-control[disabled],.form-group .form-control[disabled],fieldset[disabled] .form-control,fieldset[disabled] .form-group .form-control{background-color:transparent;cursor:not-allowed;border-bottom:1px dotted #d2d2d2;background-repeat:no-repeat}.input-group .input-group-text{display:flex;justify-content:center;align-items:center;padding:0 15px;background-color:transparent;border-color:transparent}.img-thumbnail{border-radius:16px}.img-raised{box-shadow:0 5px 15px -8px rgba(0,0,0,.24),0 8px 10px -5px rgba(0,0,0,.2)}.rounded{border-radius:6px!important}.navbar{border:0;border-radius:3px;padding:.625rem 0;margin-bottom:20px;height:auto!important;color:#555;background-color:#fff!important;box-shadow:0 4px 18px 0 rgba(0,0,0,.12),0 7px 10px -5px rgba(0,0,0,.15)}.navbar .dropdown-item:focus,.navbar .dropdown-item:hover{box-shadow:0 4px 20px 0 rgba(0,0,0,.14),0 7px 10px -5px hsla(0,0%,100%,.4);background-color:#fff;color:#555}.navbar .navbar-toggler .navbar-toggler-icon{background-color:#555}.navbar.fixed-top{border-radius:0}.navbar .navbar-nav .nav-item .nav-link{position:relative;color:inherit;padding:.9375rem;font-weight:400;font-size:12px;text-transform:uppercase;border-radius:3px;line-height:20px}.navbar .navbar-nav .nav-item .nav-link:not(.btn-just-icon) .fa{position:relative;top:2px;margin-top:-4px;margin-right:4px}.navbar .navbar-nav .nav-item .nav-link .fa,.navbar .navbar-nav .nav-item .nav-link .material-icons{font-size:1.25rem;max-width:24px;margin-top:-1.1em}.navbar .navbar-nav .nav-item .nav-link:not(.btn) .material-icons{margin-top:-7px;top:3px;position:relative;margin-right:3px}.navbar .navbar-nav .nav-item .nav-link.profile-photo{padding:0;margin:0 3px}.navbar .navbar-nav .nav-item .nav-link.profile-photo:after{display:none}.navbar .navbar-nav .nav-item .nav-link.profile-photo .profile-photo-small{height:40px;width:40px}.navbar .navbar-nav .nav-item .nav-link.profile-photo .ripple-container{border-radius:50%}.navbar .navbar-nav .dropdown-menu-right{transform-origin:100% 0}.navbar .navbar-nav .nav-item.active .nav-link,.navbar .navbar-nav .nav-item.active .nav-link:focus,.navbar .navbar-nav .nav-item.active .nav-link:hover{color:inherit;background-color:hsla(0,0%,100%,.1)}.navbar .btn,.navbar .navbar-nav .nav-item .btn{margin-top:0;margin-bottom:0}.navbar .navbar-toggler{cursor:pointer;outline:0}.navbar .navbar-toggler .navbar-toggler-icon{width:22px;height:2px;vertical-align:middle;outline:0;display:block;border-radius:1px}.navbar .navbar-toggler .navbar-toggler-icon+.navbar-toggler-icon{margin-top:4px}.navbar.navbar-absolute{position:absolute;width:100%;padding-top:10px;z-index:1029}.navbar .navbar-wrapper{display:inline-flex;align-items:center}.navbar .navbar-brand{position:relative;color:inherit;height:50px;font-size:1.125rem;line-height:30px;padding:.625rem 0;font-weight:300;margin-left:1rem}.navbar>.container{flex:1}.navbar.bg-primary{color:#fff;background-color:#9c27b0!important;box-shadow:0 4px 20px 0 rgba(0,0,0,.14),0 7px 12px -5px rgba(156,39,176,.46)}.navbar.bg-primary .dropdown-item:focus,.navbar.bg-primary .dropdown-item:hover{box-shadow:0 4px 20px 0 rgba(0,0,0,.14),0 7px 10px -5px rgba(156,39,176,.4);background-color:#9c27b0;color:#fff}.navbar.bg-primary .navbar-toggler .navbar-toggler-icon{background-color:#fff}.navbar.bg-info{color:#fff;background-color:#00bcd4!important;box-shadow:0 4px 20px 0 rgba(0,0,0,.14),0 7px 12px -5px rgba(0,188,212,.46)}.navbar.bg-info .dropdown-item:focus,.navbar.bg-info .dropdown-item:hover{box-shadow:0 4px 20px 0 rgba(0,0,0,.14),0 7px 10px -5px rgba(0,188,212,.4);background-color:#00bcd4;color:#fff}.navbar.bg-info .navbar-toggler .navbar-toggler-icon{background-color:#fff}.navbar.bg-warning{color:#fff;background-color:#ff9800!important;box-shadow:0 4px 20px 0 rgba(0,0,0,.14),0 7px 12px -5px rgba(255,152,0,.46)}.navbar.bg-warning .dropdown-item:focus,.navbar.bg-warning .dropdown-item:hover{box-shadow:0 4px 20px 0 rgba(0,0,0,.14),0 7px 10px -5px rgba(255,152,0,.4);background-color:#ff9800;color:#fff}.navbar.bg-warning .navbar-toggler .navbar-toggler-icon{background-color:#fff}.navbar.bg-rose{color:#fff;background-color:#e91e63!important;box-shadow:0 4px 20px 0 rgba(0,0,0,.14),0 7px 12px -5px rgba(233,30,99,.46)}.navbar.bg-rose .dropdown-item:focus,.navbar.bg-rose .dropdown-item:hover{box-shadow:0 4px 20px 0 rgba(0,0,0,.14),0 7px 10px -5px rgba(233,30,99,.4);background-color:#e91e63;color:#fff}.navbar.bg-rose .navbar-toggler .navbar-toggler-icon{background-color:#fff}.navbar.bg-danger{color:#fff;background-color:#f44336!important;box-shadow:0 4px 20px 0 rgba(0,0,0,.14),0 7px 12px -5px rgba(244,67,54,.46)}.navbar.bg-danger .dropdown-item:focus,.navbar.bg-danger .dropdown-item:hover{box-shadow:0 4px 20px 0 rgba(0,0,0,.14),0 7px 10px -5px rgba(244,67,54,.4);background-color:#f44336;color:#fff}.navbar.bg-danger .navbar-toggler .navbar-toggler-icon{background-color:#fff}.navbar.bg-success{color:#fff;background-color:#4caf50!important;box-shadow:0 4px 20px 0 rgba(0,0,0,.14),0 7px 12px -5px rgba(76,175,80,.46)}.navbar.bg-success .dropdown-item:focus,.navbar.bg-success .dropdown-item:hover{box-shadow:0 4px 20px 0 rgba(0,0,0,.14),0 7px 10px -5px rgba(76,175,80,.4);background-color:#4caf50;color:#fff}.navbar.bg-success .navbar-toggler .navbar-toggler-icon{background-color:#fff}.navbar.bg-dark{color:#fff;background-color:#212121!important;box-shadow:0 4px 20px 0 rgba(0,0,0,.14),0 7px 12px -5px rgba(33,33,33,.46)}.navbar.bg-dark .dropdown-item:focus,.navbar.bg-dark .dropdown-item:hover{box-shadow:0 4px 20px 0 rgba(0,0,0,.14),0 7px 10px -5px rgba(33,33,33,.4);background-color:#212121;color:#fff}.navbar.bg-dark .navbar-toggler .navbar-toggler-icon{background-color:#fff}.navbar.navbar-transparent{background-color:transparent!important;box-shadow:none}.navbar .notification{position:absolute;top:5px;border:1px solid #fff;right:10px;font-size:9px;background:#f44336;color:#fff;min-width:20px;padding:0 5px;height:20px;border-radius:10px;text-align:center;line-height:19px;vertical-align:middle;display:block}.navbar .navbar-minimize{padding:3px 0 0 15px}.navbar .collapse .navbar-nav .nav-item .nav-link{position:relative;padding:10px 15px;font-weight:400;font-size:12px;text-transform:uppercase;border-radius:3px;line-height:20px;margin-left:5px;color:inherit}.navbar .collapse .navbar-nav .nav-item .nav-link:not(.btn-just-icon) .fa{position:relative;top:2px;margin-top:-4px;margin-right:4px}.navbar .collapse .navbar-nav .nav-item .nav-link .fa,.navbar .collapse .navbar-nav .nav-item .nav-link .material-icons{font-size:1.25rem;max-width:24px;margin-top:-1.1em}.navbar .collapse .navbar-nav .nav-item .nav-link:not(.btn) .material-icons{margin-top:-3px;top:0;position:relative;margin-right:3px}.navbar .collapse .navbar-nav .nav-item .nav-link .notification{top:0}.off-canvas-sidebar .navbar .navbar-collapse .navbar-nav .nav-item .nav-link{padding-top:15px;padding-bottom:15px;font-weight:500;font-size:12px;text-transform:uppercase;border-radius:3px;color:#fff;margin:0 15px}.off-canvas-sidebar .navbar .navbar-collapse .navbar-nav .nav-item .nav-link:hover{background:hsla(0,0%,78%,.2)}.off-canvas-sidebar .navbar.navbar-transparent{padding-top:25px!important}.pagination>.page-item>.page-link,.pagination>.page-item>span{border:0;border-radius:30px!important;transition:all .3s;padding:0 11px;margin:0 3px;min-width:30px;height:30px;line-height:30px;color:#999;font-weight:400;font-size:12px;text-transform:uppercase;background:transparent;text-align:center}.pagination>.page-item.active>a,.pagination>.page-item.active>span,.pagination>.page-item>.page-link:focus,.pagination>.page-item>.page-link:hover,.pagination>.page-item>span:focus,.pagination>.page-item>span:hover{color:#999}.pagination>.page-item.active>a,.pagination>.page-item.active>a:focus,.pagination>.page-item.active>a:hover,.pagination>.page-item.active>span,.pagination>.page-item.active>span:focus,.pagination>.page-item.active>span:hover{background-color:#9c27b0;border-color:#9c27b0;color:#fff;box-shadow:0 4px 5px 0 rgba(156,39,176,.14),0 1px 10px 0 rgba(156,39,176,.12),0 2px 4px -1px rgba(156,39,176,.2)}.pagination.pagination-info>.page-item.active>a,.pagination.pagination-info>.page-item.active>a:focus,.pagination.pagination-info>.page-item.active>a:hover,.pagination.pagination-info>.page-item.active>span,.pagination.pagination-info>.page-item.active>span:focus,.pagination.pagination-info>.page-item.active>span:hover{background-color:#00bcd4;border-color:#00bcd4;box-shadow:0 4px 5px 0 rgba(0,188,212,.14),0 1px 10px 0 rgba(0,188,212,.12),0 2px 4px -1px rgba(0,188,212,.2)}.pagination.pagination-success>.page-item.active>a,.pagination.pagination-success>.page-item.active>a:focus,.pagination.pagination-success>.page-item.active>a:hover,.pagination.pagination-success>.page-item.active>span,.pagination.pagination-success>.page-item.active>span:focus,.pagination.pagination-success>.page-item.active>span:hover{background-color:#4caf50;border-color:#4caf50;box-shadow:0 4px 5px 0 rgba(76,175,80,.14),0 1px 10px 0 rgba(76,175,80,.12),0 2px 4px -1px rgba(76,175,80,.2)}.pagination.pagination-warning>.page-item.active>a,.pagination.pagination-warning>.page-item.active>a:focus,.pagination.pagination-warning>.page-item.active>a:hover,.pagination.pagination-warning>.page-item.active>span,.pagination.pagination-warning>.page-item.active>span:focus,.pagination.pagination-warning>.page-item.active>span:hover{background-color:#ff9800;border-color:#ff9800;box-shadow:0 4px 5px 0 rgba(255,152,0,.14),0 1px 10px 0 rgba(255,152,0,.12),0 2px 4px -1px rgba(255,152,0,.2)}.pagination.pagination-danger>.page-item.active>a,.pagination.pagination-danger>.page-item.active>a:focus,.pagination.pagination-danger>.page-item.active>a:hover,.pagination.pagination-danger>.page-item.active>span,.pagination.pagination-danger>.page-item.active>span:focus,.pagination.pagination-danger>.page-item.active>span:hover{background-color:#f44336;border-color:#f44336;box-shadow:0 4px 5px 0 rgba(244,67,54,.14),0 1px 10px 0 rgba(244,67,54,.12),0 2px 4px -1px rgba(244,67,54,.2)}.material-datatables .table .disabled-sorting:after,.material-datatables .table .disabled-sorting:before{display:none}.material-datatables .dataTables_paginate .pagination .paginate_button .page-link{padding:0 5px;margin:0}.nav-pills{border:0;border-radius:3px;padding:0 15px}.nav-pills:not(.flex-column) .nav-item+.nav-item:not(:first-child){margin-left:5px}.nav-pills.flex-column .nav-item+.nav-item{margin-top:5px}.nav-pills .nav-item .nav-link{line-height:24px;text-transform:uppercase;font-size:12px;font-weight:500;min-width:100px;text-align:center;color:#555;transition:all .3s;border-radius:30px;padding:10px 15px}.nav-pills .nav-item .nav-link:hover{background-color:hsla(0,0%,78%,.2)}.nav-pills .nav-item .nav-link.active{color:#fff;background-color:#9c27b0;box-shadow:0 4px 20px 0 rgba(0,0,0,.14),0 7px 10px -5px rgba(156,39,176,.4)}.nav-pills .nav-item i{display:block;font-size:30px;padding:15px 0}.nav-pills.nav-pills-info .nav-item .nav-link.active,.nav-pills.nav-pills-info .nav-item .nav-link.active:focus,.nav-pills.nav-pills-info .nav-item .nav-link.active:hover{background-color:#00bcd4;box-shadow:0 4px 20px 0 rgba(0,0,0,.14),0 7px 10px -5px rgba(0,188,212,.4);color:#fff}.nav-pills.nav-pills-rose .nav-item .nav-link.active,.nav-pills.nav-pills-rose .nav-item .nav-link.active:focus,.nav-pills.nav-pills-rose .nav-item .nav-link.active:hover{background-color:#e91e63;box-shadow:0 4px 20px 0 rgba(0,0,0,.14),0 7px 10px -5px rgba(233,30,99,.4);color:#fff}.nav-pills.nav-pills-success .nav-item .nav-link.active,.nav-pills.nav-pills-success .nav-item .nav-link.active:focus,.nav-pills.nav-pills-success .nav-item .nav-link.active:hover{background-color:#4caf50;box-shadow:0 4px 20px 0 rgba(0,0,0,.14),0 7px 10px -5px rgba(76,175,80,.4);color:#fff}.nav-pills.nav-pills-warning .nav-item .nav-link.active,.nav-pills.nav-pills-warning .nav-item .nav-link.active:focus,.nav-pills.nav-pills-warning .nav-item .nav-link.active:hover{background-color:#ff9800;box-shadow:0 4px 20px 0 rgba(0,0,0,.14),0 7px 10px -5px rgba(255,152,0,.4);color:#fff}.nav-pills.nav-pills-danger .nav-item .nav-link.active,.nav-pills.nav-pills-danger .nav-item .nav-link.active:focus,.nav-pills.nav-pills-danger .nav-item .nav-link.active:hover{background-color:#f44336;box-shadow:0 4px 20px 0 rgba(0,0,0,.14),0 7px 10px -5px rgba(244,67,54,.4);color:#fff}.nav-pills.nav-pills-icons .nav-item .nav-link{border-radius:4px}.tab-space{padding:20px 0 50px}.card .tab-content.tab-space{padding:20px 0 9px}html *{-webkit-font-smoothing:antialiased;-moz-osx-font-smoothing:grayscale}.h1,.h2,.h3,.h4,body,h1,h2,h3,h4,h5,h6{font-family:Roboto,Helvetica,Arial,sans-serif;font-weight:300;line-height:1.5em}.h1,h1{font-size:3.3125rem;line-height:1.15em}.h2,h2{font-size:2.25rem}.h3,h3{font-size:1.5625rem;margin:20px 0 10px}.h3,.h4,h3,h4{line-height:1.4em}.h4,h4{font-size:1.125rem;font-weight:300}.h5,h5{font-size:1.0625rem;line-height:1.4em;margin-bottom:15px}.h6,h6{font-size:.75rem;text-transform:uppercase;font-weight:500}.card-title,.card-title a,.footer-big h4,.footer-big h4 a,.footer-big h5,.footer-big h5 a,.footer-brand,.footer-brand a,.info-title,.info-title a,.media .media-heading,.media .media-heading a,.title,.title a{color:#3c4858;text-decoration:none}.card-blog .card-title{font-weight:700}h2.title{margin-bottom:2.142rem}.card-description,.description,.footer-big p{color:#999}.text-warning{color:#ff9800!important}.text-primary{color:#9c27b0!important}.text-danger{color:#f44336!important}.text-success{color:#4caf50!important}.text-info{color:#00bcd4!important}.text-rose{color:#e91e63!important}.text-gray{color:#999!important}.nav-tabs{border:0;border-radius:3px;padding:0 15px}.nav-tabs .nav-item .nav-link{position:relative;color:#fff;border:0;margin:0;border-radius:3px;line-height:24px;text-transform:uppercase;font-size:12px;padding:10px 15px;background-color:transparent;transition:background-color .3s 0s}.nav-tabs .nav-item .nav-link:hover{border:0}.nav-tabs .nav-item .nav-link,.nav-tabs .nav-item .nav-link:focus,.nav-tabs .nav-item .nav-link:hover{border:0!important;color:#fff!important;font-weight:500}.nav-tabs .nav-item.disabled .nav-link,.nav-tabs .nav-item.disabled .nav-link:hover{color:hsla(0,0%,100%,.5)}.nav-tabs .nav-item .material-icons{margin:-1px 5px 0 0}.nav-tabs .nav-item .nav-link.active{background-color:hsla(0,0%,100%,.2);transition:background-color .3s .2s}.nav-tabs .nav-link{border-bottom:.214rem solid transparent;color:#555}.nav-tabs .nav-link.active{color:#333;border-color:#9c27b0}.nav-tabs .nav-link.active:focus,.nav-tabs .nav-link.active:hover{border-color:#9c27b0}.nav-tabs .nav-link.disabled,.nav-tabs .nav-link.disabled:focus,.nav-tabs .nav-link.disabled:hover{color:#999}.nav-tabs.header-primary .nav-link{color:#fff}.nav-tabs.header-primary .nav-link.active{color:#fff;border-color:#fff}.nav-tabs.header-primary .nav-link.active:focus,.nav-tabs.header-primary .nav-link.active:hover{border-color:#fff}.nav-tabs.header-primary .nav-link.disabled,.nav-tabs.header-primary .nav-link.disabled:focus,.nav-tabs.header-primary .nav-link.disabled:hover{color:hsla(0,0%,100%,.84)}.nav-tabs.bg-inverse .nav-link{color:#fff}.nav-tabs.bg-inverse .nav-link.active{color:#fff;border-color:#fff}.nav-tabs.bg-inverse .nav-link.active:focus,.nav-tabs.bg-inverse .nav-link.active:hover{border-color:#fff}.nav-tabs.bg-inverse .nav-link.disabled,.nav-tabs.bg-inverse .nav-link.disabled:focus,.nav-tabs.bg-inverse .nav-link.disabled:hover{color:hsla(0,0%,100%,.84)}.card-nav-tabs{margin-top:45px}.card-nav-tabs .card-header{margin-top:-30px!important}.tab-content .tab-pane .td-actions{display:-ms-flexbox;display:flex}.card .tab-content .form-check{margin-top:6px}.tooltip-arrow{display:none}.tooltip.show{opacity:1;transform:translateZ(0)}.tooltip{opacity:0;transition:opacity,transform .2s ease;transform:translate3d(0,5px,0);font-size:.875rem}.tooltip.bs-tooltip-auto[x-placement^=top] .arrow:before,.tooltip.bs-tooltip-top .arrow:before{border-top-color:#fff}.tooltip.bs-tooltip-auto[x-placement^=right] .arrow:before,.tooltip.bs-tooltip-right .arrow:before{border-right-color:#fff}.tooltip.bs-tooltip-auto[x-placement^=left] .arrow:before,.tooltip.bs-tooltip-left .arrow:before{border-left-color:#fff}.tooltip.bs-tooltip-auto[x-placement^=bottom] .arrow:before,.tooltip.bs-tooltip-bottom .arrow:before{border-bottom-color:#fff}.tooltip-inner{padding:10px 15px;min-width:130px}.popover,.tooltip-inner{line-height:1.5em;background:#fff;border:none;border-radius:3px;box-shadow:0 8px 10px 1px rgba(0,0,0,.14),0 3px 14px 2px rgba(0,0,0,.12),0 5px 5px -3px rgba(0,0,0,.2);color:#555}.popover{padding:0;box-shadow:0 16px 24px 2px rgba(0,0,0,.14),0 6px 30px 5px rgba(0,0,0,.12),0 8px 10px -5px rgba(0,0,0,.2)}.popover.bottom>.arrow,.popover.left>.arrow,.popover.right>.arrow,.popover.top>.arrow{border:none}.popover.bs-popover-auto[x-placement^=bottom] .arrow:before,.popover.bs-popover-auto[x-placement^=left] .arrow:before,.popover.bs-popover-auto[x-placement^=right] .arrow:before,.popover.bs-popover-auto[x-placement^=top] .arrow:before,.popover.bs-popover-bottom .arrow:before,.popover.bs-popover-left .arrow:before,.popover.bs-popover-right .arrow:before,.popover.bs-popover-top .arrow:before{border:0}.popover-header{background-color:#fff;border:none;padding:15px 15px 5px;font-size:1.125rem;margin:0;color:#555}.popover-body{padding:10px 15px 15px;line-height:1.4;color:#555}.modal-dialog .modal-content{box-shadow:0 27px 24px 0 rgba(0,0,0,.2),0 40px 77px 0 rgba(0,0,0,.22);border-radius:6px;border:none}.modal-dialog .modal-content .card-signup{margin:0}.modal-dialog .modal-content .card-signup .modal-header{padding-top:0}.modal-dialog .close:focus{outline:none}.modal-dialog .modal-header{border-bottom:none;padding:24px 24px 0}.modal-dialog .modal-header .modal-title{text-align:center;width:100%}.modal-dialog .modal-header .close{position:absolute;top:15px;right:20px}.modal-dialog .modal-body{padding:24px 24px 16px}.modal-dialog .modal-footer{border-top:none;padding:24px}.modal-dialog .modal-footer.text-center{text-align:center}.modal-dialog .modal-footer button{margin:0;padding-left:16px;padding-right:16px;width:auto}.modal-dialog .modal-footer button.pull-left{padding-left:5px;padding-right:5px;position:relative;left:-5px}.modal-dialog .modal-body+.modal-footer{padding-top:0}.modal-backdrop{background:rgba(0,0,0,.3)}.modal .modal-dialog{margin-top:100px}.modal .modal-dialog.modal-login{width:360px}.modal .modal-dialog.modal-login .modal-header .close{color:#fff;text-shadow:none;position:absolute}.modal .modal-dialog.modal-login .modal-footer{padding-bottom:0;padding-top:0}.modal .modal-dialog.modal-login .modal-body{padding-left:4px;padding-bottom:0;padding-top:0}.modal .modal-dialog.modal-login .card-signup{margin-bottom:0}.modal .modal-dialog.modal-signup{max-width:900px}.modal .modal-dialog.modal-signup .info-horizontal{padding:0 0 20px}.modal .modal-dialog.modal-signup .modal-title{text-align:center;width:100%}.modal .modal-dialog.modal-signup .modal-footer{padding:0 5px}.modal .modal-dialog.modal-signup .modal-header{padding-top:0}.modal .modal-dialog.modal-signup .card-signup{padding:40px 0;margin-bottom:0}.modal .modal-dialog.modal-signup .modal-body{padding-bottom:0;padding-top:0}.modal .modal-header .close{color:#999}.modal .modal-header .close:focus,.modal .modal-header .close:hover{opacity:1}.modal .modal-header .close i{font-size:16px}.modal-notice .instruction{margin-bottom:25px}.modal-notice .picture{max-width:150px}.modal-notice .modal-content .btn-raised{margin-bottom:15px}.modal-small{width:300px;margin:0 auto}.modal-small .modal-body{margin-top:20px}body{background-color:#eee;color:#3c4858;font-weight:300}legend{border-bottom:0}.serif-font{font-family:Roboto Slab,Times New Roman,serif}*{-webkit-tap-highlight-color:rgba(255,255,255,0);-webkit-tap-highlight-color:transparent}:focus{outline:0}.form-check,label{font-size:14px;line-height:1.42857;color:#aaa;font-weight:400}.animation-transition-general,.lock-page .card-profile,.login-page .card-login,.sidebar .logo a.logo-mini,.sidebar .logo a.logo-normal,.sidebar .nav p,.sidebar .sidebar-wrapper .user .user-info [data-toggle=collapse]~div>ul>li>a span,.sidebar .sidebar-wrapper>.nav [data-toggle=collapse]~div>ul>li>a span,.sidebar .user .photo,.sidebar .user .user-info>a>span{transition:all .3s linear}.animation-transition-slow{transition:all .37s linear}.animation-transition-fast,.bootstrap-datetimepicker-widget table td>div,.bootstrap-datetimepicker-widget table td span,.bootstrap-datetimepicker-widget table th,.bootstrap-datetimepicker-widget table th>div{transition:all .15s ease 0s}.caret,.sidebar a{transition:all .15s ease-in}.offline-doc .navbar.navbar-transparent{padding-top:25px;border-bottom:none}.offline-doc .navbar.navbar-transparent .navbar-minimize{display:none}.offline-doc .navbar.navbar-transparent .collapse .navbar-nav .nav-link,.offline-doc .navbar.navbar-transparent .navbar-brand{color:#fff!important}.offline-doc .footer{z-index:3!important;position:absolute;width:100%;background:transparent;bottom:0;color:#fff}.offline-doc .page-header{display:flex;align-items:center}.offline-doc .page-header .content-center{z-index:3}.offline-doc .page-header .content-center .brand .title{color:#fff}.offline-doc .page-header:after{background-color:rgba(0,0,0,.5);content:"";display:block;height:100%;left:0;position:absolute;top:0;width:100%;z-index:2}.bd-docs .bd-toc-item .bd-sidenav a span{float:right;margin-top:5px;padding:3px 7px;font-size:8px;line-height:9px;background-color:#9c27b0}.bootstrap-datetimepicker-widget .timepicker .table-condesed .btn .ripple-container{width:40px;height:40px;margin:-11px 3px}.off-canvas-sidebar .wrapper-full-page .page-header{padding:15vh 0!important}.page-header{min-height:100vh;max-height:1000px;display:flex!important;padding:0;margin:0;border:0;color:#fff;position:relative;align-items:center}.page-header,.page-header .page-header-image{height:100%;background-position:50%;background-size:cover}.page-header .page-header-image{position:absolute;width:100%;z-index:-1}.page-header .content-center{position:absolute;top:50%;left:50%;z-index:2;transform:translate(-50%,-50%);text-align:center;color:#fff;padding:0 15px;width:100%;max-width:880px}.page-header footer{position:absolute;bottom:0;width:100%}.page-header .container{height:100%;z-index:1}.page-header.header-small{height:65vh;min-height:65vh}.page-header .iframe-container iframe{width:100%;box-shadow:0 16px 38px -12px rgba(0,0,0,.56),0 4px 25px 0 rgba(0,0,0,.12),0 8px 10px -5px rgba(0,0,0,.2)}.header-filter{position:relative}.header-filter:after,.header-filter:before{position:absolute;z-index:1;width:100%;height:100%;display:block;left:0;top:0;content:""}.header-filter:before{background:rgba(0,0,0,.5)}.header-filter .container{z-index:2;position:relative}.clear-filter:before{background:none}.purple-filter:after{background:rgba(101,47,142,.64);background:linear-gradient(45deg,rgba(101,47,142,.88),rgba(125,46,185,.45));background:-webkit-linear-gradient(135deg,rgba(101,47,142,.88),rgba(125,46,185,.45))}.header-filter[filter-color=primary]:after,.header-filter[filter-color=purple]:after{background:rgba(225,190,231,.56);background:linear-gradient(60deg,rgba(225,190,231,.56),rgba(186,104,200,.95))}.header-filter[filter-color=blue]:after,.header-filter[filter-color=info]:after{background:rgba(178,235,242,.56);background:linear-gradient(60deg,rgba(178,235,242,.56),rgba(77,208,225,.95))}.header-filter[filter-color=green]:after,.header-filter[filter-color=success]:after{background:rgba(165,214,167,.56);background:linear-gradient(60deg,rgba(165,214,167,.56),rgba(102,187,106,.95))}.header-filter[filter-color=orange]:after,.header-filter[filter-color=warning]:after{background:rgba(255,224,178,.56);background:linear-gradient(60deg,rgba(255,224,178,.56),rgba(255,183,77,.95))}.header-filter[filter-color=danger]:after,.header-filter[filter-color=red]:after{background:hsla(0,73%,77%,.56);background:linear-gradient(60deg,hsla(0,73%,77%,.56),rgba(239,83,80,.95))}.header-filter[filter-color=rose]:after{background:rgba(248,187,208,.56);background:linear-gradient(60deg,rgba(248,187,208,.56),rgba(240,98,146,.95))}.header-1 .wrapper,.header-2 .wrapper,.header-3 .wrapper{background:#ccc}.header-2 .page-header .container{padding-top:25vh}.header-2 .page-header .card{margin-top:60px}.header-3 .btn{margin:0}.card-form-horizontal .form-group,.header-3 h6{margin-bottom:0}.alert{border:0;border-radius:3px;position:relative;padding:20px 15px;line-height:20px}.alert b{font-weight:500;text-transform:uppercase;font-size:12px}.alert,.alert.alert-default{background-color:#fff;color:#555}.alert.alert-default .alert-link,.alert.alert-default a,.alert .alert-link,.alert a{color:#555}.alert.alert-inverse{background-color:#292929;color:#fff}.alert.alert-inverse .alert-link,.alert.alert-inverse a{color:#fff}.alert.alert-primary{background-color:#a72abd;color:#fff}.alert.alert-primary .alert-link,.alert.alert-primary a{color:#fff}.alert.alert-success{background-color:#55b559;color:#fff}.alert.alert-success .alert-link,.alert.alert-success a{color:#fff}.alert.alert-info{background-color:#00cae3;color:#fff}.alert.alert-info .alert-link,.alert.alert-info a{color:#fff}.alert.alert-warning{background-color:#ff9e0f;color:#fff}.alert.alert-warning .alert-link,.alert.alert-warning a{color:#fff}.alert.alert-danger{background-color:#f55145;color:#fff}.alert.alert-danger .alert-link,.alert.alert-danger a{color:#fff}.alert.alert-rose{background-color:#ea2c6d;color:#fff}.alert-danger,.alert-info,.alert-rose,.alert-success,.alert-warning,.alert.alert-rose .alert-link,.alert.alert-rose a{color:#fff}.alert-default .alert-link,.alert-default a{color:rgba(0,0,0,.87)}.alert span{display:block;max-width:89%}.alert.alert-danger{box-shadow:0 4px 20px 0 rgba(0,0,0,.14),0 7px 10px -5px rgba(244,67,54,.4)}.alert.alert-danger i{color:#f44336}.alert.alert-warning{box-shadow:0 4px 20px 0 rgba(0,0,0,.14),0 7px 10px -5px rgba(255,152,0,.4)}.alert.alert-warning i{color:#ff9800}.alert.alert-success{box-shadow:0 4px 20px 0 rgba(0,0,0,.14),0 7px 10px -5px rgba(76,175,80,.4)}.alert.alert-success i{color:#4caf50}.alert.alert-info{box-shadow:0 4px 20px 0 rgba(0,0,0,.14),0 7px 10px -5px rgba(0,188,212,.4)}.alert.alert-info i{color:#00bcd4}.alert.alert-primary{box-shadow:0 4px 20px 0 rgba(0,0,0,.14),0 7px 10px -5px rgba(156,39,176,.4)}.alert.alert-primary i{color:#9c27b0}.alert.alert-rose{box-shadow:0 4px 20px 0 rgba(0,0,0,.14),0 7px 10px -5px rgba(233,30,99,.4)}.alert.alert-rose i{color:#e91e63}.alert.alert-with-icon{margin-top:43px;padding-left:66px}.alert.alert-with-icon i[data-notify=icon]{display:block;left:15px;position:absolute;margin-top:-39px;font-size:20px;background-color:#fff;padding:9px;border-radius:50%;max-width:38px;box-shadow:0 16px 38px -12px rgba(0,0,0,.56),0 4px 25px 0 rgba(0,0,0,.12),0 8px 10px -5px rgba(0,0,0,.2)}.alert .close{line-height:.5}.alert .close i{color:#fff;font-size:11px}.alert .close:focus{outline:none}.alert i[data-notify=icon]{display:none}.alert .alert-icon{display:block;float:left;margin-right:1.071rem}.alert .alert-icon i{margin-top:-7px;top:5px;position:relative}.alert [data-notify=dismiss]{margin-right:5px}.places-buttons .btn{margin-bottom:30px}.footer{padding:.9375rem 0;text-align:center;display:flex}.footer ul{margin-bottom:0;padding:0;list-style:none}.footer ul li{display:inline-block}.footer ul li a{color:inherit;padding:.9375rem;font-weight:500;font-size:12px;text-transform:uppercase;border-radius:3px;position:relative;display:block}.footer ul li a,.footer ul li a:hover{text-decoration:none}.footer ul li .btn{margin:0}.footer ul.links-horizontal:first-child a{padding-left:0}.footer ul.links-horizontal:last-child a{padding-right:0}.footer ul.links-vertical li{display:block;margin-left:-5px;margin-right:-5px}.footer ul.links-vertical li a{padding:5px}.footer .social-buttons .btn,.footer .social-buttons a{margin-top:5px;margin-bottom:5px}.footer .footer-brand{float:left;height:50px;padding:15px;font-size:18px;line-height:20px;margin-left:-15px}.footer .footer-brand:focus,.footer .footer-brand:hover{color:#3c4858}.footer .copyright{padding:15px 0}.footer .copyright .material-icons{font-size:18px;position:relative;top:3px}.footer .pull-center{display:inline-block;float:none}.off-canvas-sidebar .footer{position:absolute;bottom:0;width:100%}@media screen and (min-width:768px){.footer .copyright{padding-right:15px}}.dropdown-menu{display:none;padding:.3125rem 0;border:0;opacity:0;transform:scale(0);transform-origin:0 0;will-change:transform,opacity;transition:transform .3s cubic-bezier(.4,0,.2,1),opacity .2s cubic-bezier(.4,0,.2,1);box-shadow:0 2px 5px 0 rgba(0,0,0,.26)}.dropdown-menu.showing{animation-name:d;animation-duration:.3s;animation-fill-mode:forwards;animation-timing-function:cubic-bezier(.4,0,.2,1)}.dropdown-menu.show,.open>.dropdown-menu{display:block;opacity:1;transform:scale(1)}.dropdown-menu.hiding{display:block;opacity:0;transform:scale(0)}.dropdown-menu[x-placement=bottom-start]{transform-origin:0 0}.dropdown-menu[x-placement=bottom-end]{transform-origin:100% 0}.dropdown-menu[x-placement=top-start]{transform-origin:0 100%}.dropdown-menu[x-placement=top-end]{transform-origin:100% 100%}.dropdown-menu .disabled>a{color:#777}.dropdown-menu .disabled>a:focus,.dropdown-menu .disabled>a:hover{text-decoration:none;background-color:transparent;background-image:none;color:#777}.dropdown-menu.dropdown-with-icons .dropdown-item{padding:.75rem 1.25rem .75rem .75rem}.dropdown-menu.dropdown-with-icons .dropdown-item .material-icons{vertical-align:middle;font-size:24px;position:relative;margin-top:-4px;top:1px;margin-right:12px;opacity:.5}.dropdown-menu .dropdown-item,.dropdown-menu li>a{position:relative;width:auto;display:flex;flex-flow:nowrap;align-items:center;color:#333;font-weight:400;text-decoration:none;font-size:.8125rem;border-radius:.125rem;margin:0 .3125rem;transition:all .15s linear;min-width:7rem;padding:.625rem 1.25rem;overflow:hidden;line-height:1.428571;text-overflow:ellipsis;word-wrap:break-word}@media (min-width:768px){.dropdown-menu .dropdown-item,.dropdown-menu li>a{padding-right:1.5rem;padding-left:1.5rem}}.dropdown-menu .dropdown-item:focus,.dropdown-menu .dropdown-item:hover,.dropdown-menu a:active,.dropdown-menu a:focus,.dropdown-menu a:hover{box-shadow:0 4px 20px 0 rgba(0,0,0,.14),0 7px 10px -5px rgba(156,39,176,.4);background-color:#9c27b0;color:#fff}.btn-group.bootstrap-select.open .caret,.dropdown.open .caret,.dropup.open .caret,a[aria-expanded=true] .caret,a[data-toggle=collapse][aria-expanded=true] .caret{filter:progid:DXImageTransform.Microsoft.BasicImage(rotation=2);transform:rotate(180deg)}.dropdown-toggle.bmd-btn-fab:after,.dropdown-toggle.bmd-btn-icon:after{display:none}.dropdown-toggle.bmd-btn-fab~.dropdown-menu.dropdown-menu-top-left,.dropdown-toggle.bmd-btn-fab~.dropdown-menu.dropdown-menu-top-right,.dropdown-toggle.bmd-btn-icon~.dropdown-menu.dropdown-menu-top-left,.dropdown-toggle.bmd-btn-icon~.dropdown-menu.dropdown-menu-top-right{bottom:2rem}.dropdown-toggle:after{will-change:transform;transition:transform .15s linear}.dropdown-toggle.bmd-btn-fab-sm~.dropdown-menu.dropdown-menu-top-left,.dropdown-toggle.bmd-btn-fab-sm~.dropdown-menu.dropdown-menu-top-right{bottom:2.5rem}.dropdown-toggle.bmd-btn-icon~.dropdown-menu{margin:0}.show>.dropdown-toggle:not(.dropdown-item):after{filter:progid:DXImageTransform.Microsoft.BasicImage(rotation=2);transform:rotate(180deg)}.dropdown-header{font-size:.75rem;padding-top:.625rem;padding-bottom:.625rem;text-transform:none;color:#777;line-height:1.428571;font-weight:inherit}@keyframes d{0%{opacity:0;transform:scale(0)}to{opacity:1;transform:scale(1)}}.dropdown-menu.bootstrap-datetimepicker-widget{opacity:0;transform:scale(0);transition-duration:.3s;transition-timing-function:cubic-bezier(.4,0,.2,1);transform-origin:0 0;will-change:transform,opacity;top:0}.dropdown-menu.bootstrap-datetimepicker-widget.top{transform-origin:0 100%}.dropdown-menu.bootstrap-datetimepicker-widget.open{opacity:1;transform:scale(1);top:0}.progress{height:4px;border-radius:0;background:#ddd;margin-bottom:20px}.progress,.progress .progress-bar{box-shadow:none}.progress .progress-bar.progress-bar-primary{background:#9c27b0!important}.progress .progress-bar.progress-bar-info{background:#00bcd4}.progress .progress-bar.progress-bar-success{background:#4caf50}.progress .progress-bar.progress-bar-warning{background:#ff9800}.progress .progress-bar.progress-bar-danger{background:#f44336}.progress .progress-bar.progress-bar-striped{background-image:linear-gradient(45deg,hsla(0,0%,100%,.15) 25%,transparent 0,transparent 50%,hsla(0,0%,100%,.15) 0,hsla(0,0%,100%,.15) 75%,transparent 0,transparent)!important;background-size:1rem 1rem!important}.progress.progress-line-primary{background:rgba(156,39,176,.2)}.progress.progress-line-info{background:rgba(0,188,212,.2)}.progress.progress-line-success{background:rgba(76,175,80,.2)}.progress.progress-line-warning{background:rgba(255,152,0,.2)}.progress.progress-line-danger{background:rgba(244,67,54,.2)}.togglebutton{vertical-align:middle}.togglebutton,.togglebutton .toggle,.togglebutton input,.togglebutton label{user-select:none}.togglebutton label{cursor:pointer}.form-group.is-focused .togglebutton label,.togglebutton label{color:rgba(0,0,0,.26)}.form-group.is-focused .togglebutton label:focus,.form-group.is-focused .togglebutton label:hover{color:rgba(0,0,0,.54)}fieldset[disabled] .form-group.is-focused .togglebutton label{color:rgba(0,0,0,.26)}.togglebutton label input[type=checkbox]{opacity:0;width:0;height:0}.togglebutton label .toggle{text-align:left;margin-left:5px}.togglebutton label .toggle,.togglebutton label input[type=checkbox][disabled]+.toggle{content:"";display:inline-block;width:30px;height:15px;background-color:rgba(80,80,80,.7);border-radius:15px;margin-right:15px;transition:background .3s ease;vertical-align:middle}.togglebutton label .toggle:after{content:"";display:inline-block;width:20px;height:20px;background-color:#fff;border-radius:20px;position:relative;box-shadow:0 1px 3px 1px rgba(0,0,0,.4);left:-5px;top:-2.5px;border:1px solid rgba(0,0,0,.54);transition:left .3s ease,background .3s ease,box-shadow .1s ease}.togglebutton label input[type=checkbox][disabled]+.toggle:after,.togglebutton label input[type=checkbox][disabled]:checked+.toggle:after{background-color:#bdbdbd}.togglebutton label input[type=checkbox]+.toggle:active:after,.togglebutton label input[type=checkbox][disabled]+.toggle:active:after{box-shadow:0 1px 3px 1px rgba(0,0,0,.4),0 0 0 15px rgba(0,0,0,.1)}.togglebutton label input[type=checkbox]:checked+.toggle:after{left:15px}.togglebutton label input[type=checkbox]:checked+.toggle{background-color:rgba(156,39,176,.7)}.togglebutton label input[type=checkbox]:checked+.toggle:after{border-color:#9c27b0}.togglebutton label input[type=checkbox]:checked+.toggle:active:after{box-shadow:0 1px 3px 1px rgba(0,0,0,.4),0 0 0 15px rgba(156,39,176,.1)}.ripple{position:relative}.ripple-container{position:absolute;top:0;left:0;z-index:1;width:100%;height:100%;overflow:hidden;pointer-events:none;border-radius:inherit}.ripple-container .ripple-decorator{position:absolute;width:20px;height:20px;margin-top:-10px;margin-left:-10px;pointer-events:none;background-color:rgba(0,0,0,.05);border-radius:100%;opacity:0;transform:scale(1);transform-origin:50%}.ripple-container .ripple-decorator.ripple-on{opacity:.1;transition:opacity .15s ease-in 0s,transform .5s cubic-bezier(.4,0,.2,1) .1s}.ripple-container .ripple-decorator.ripple-out{opacity:0;transition:opacity .1s linear 0s!important}.table>thead>tr>th{border-bottom-width:1px;font-size:1.0625rem;font-weight:300}.table .form-check{margin-top:0}.table .form-check .form-check-sign{top:-13px;left:0;padding-right:0}.table .checkbox,.table .radio{margin-top:0;margin-bottom:0;padding:0;width:15px}.table .checkbox .icons,.table .radio .icons{position:relative}.table .flag img{max-width:18px;margin-top:-2px}.table>tbody>tr>td,.table>tbody>tr>th,.table>tfoot>tr>td,.table>tfoot>tr>th,.table>thead>tr>td,.table>thead>tr>th{padding:12px 8px;vertical-align:middle;border-color:#ddd}.table thead tr th{font-size:1.063rem}.table .th-description{max-width:150px}.table .td-price{font-size:26px;font-weight:300;margin-top:5px;text-align:right}.table .td-total{font-weight:500;font-size:1.0625rem;padding-top:20px;text-align:right}.table .td-actions .btn{margin:0;padding:5px}.table>tbody>tr{position:relative}.table-shopping>thead>tr>th{font-size:.75rem;text-transform:uppercase}.table-shopping>tbody>tr>td{font-size:14px}.table-shopping>tbody>tr>td b{display:block;margin-bottom:5px}.table-shopping .td-name{font-weight:400;font-size:1.5em;line-height:1.42857143}.table-shopping .td-name small{color:#999;font-size:.75em;font-weight:300}.table-shopping .td-number{font-weight:300;font-size:1.125rem}.table-shopping .td-name{min-width:200px}.table-shopping .td-number{text-align:right;min-width:150px}.table-shopping .td-number small{margin-right:3px}.table-shopping .img-container{width:120px;max-height:160px;overflow:hidden;display:block}.table-shopping .img-container img{width:100%}.table-inverse{color:hsla(0,0%,100%,.84)}.table thead th{font-size:.95rem;font-weight:500;border-top-width:0;border-bottom-width:1px}.table-inverse thead th,thead.thead-inverse th{color:hsla(0,0%,100%,.54)}.table-inverse td,.table-inverse th,.table-inverse thead th{border-color:hsla(0,0%,100%,.06)}.table-striped>tbody>tr:nth-of-type(odd){background-color:#f9f9f9}.table.table-hover tbody tr:hover{background-color:#f5f5f5}.dataTable>tbody>tr>td,.dataTable>tbody>tr>th,.dataTable>tfoot>tr>td,.dataTable>tfoot>tr>th,.dataTable>thead>tr>td,.dataTable>thead>tr>th{padding:5px!important}.info{max-width:360px;margin:0 auto;padding:70px 0 30px}.info .icon{color:#999}.info .icon>i{font-size:3.85rem}.info .info-title{color:#3c4858;margin:1.75rem 0 .875rem}.info p{color:#999}.info-horizontal .icon{float:left;margin-top:24px;margin-right:10px}.info-horizontal .icon>i{font-size:2.25rem}.info-horizontal .description{overflow:hidden}.icon.icon-primary{color:#9c27b0}.icon.icon-info{color:#00bcd4}.icon.icon-success{color:#4caf50}.icon.icon-warning{color:#ff9800}.icon.icon-danger{color:#f44336}.icon.icon-rose{color:#e91e63}.card{border:0;margin-bottom:30px;margin-top:30px;border-radius:6px;color:#333;background:#fff;width:100%;box-shadow:0 2px 2px 0 rgba(0,0,0,.14),0 3px 1px -2px rgba(0,0,0,.2),0 1px 5px 0 rgba(0,0,0,.12)}.card .card-category:not([class*=text-]){color:#999}.card .card-category{margin-top:10px}.card .card-category .material-icons{position:relative;top:8px;line-height:0}.card .form-check{margin-top:5px}.card .card-title{margin-top:.625rem}.card .card-title:last-child{margin-bottom:0}.card.no-shadow .card-header-image,.card.no-shadow .card-header-image img{box-shadow:none!important}.card .card-body,.card .card-footer{padding:.9375rem 1.875rem}.card .card-body+.card-footer{padding-top:0;border:0;border-radius:6px}.card .card-footer{display:flex;align-items:center;background-color:transparent;border:0}.card .card-footer .author,.card .card-footer .stats{display:inline-flex}.card .card-footer .stats{color:#999}.card .card-footer .stats .material-icons{position:relative;top:-10px;margin-right:3px;margin-left:3px;font-size:18px}.card.bmd-card-raised{box-shadow:0 8px 10px 1px rgba(0,0,0,.14),0 3px 14px 2px rgba(0,0,0,.12),0 5px 5px -3px rgba(0,0,0,.2)}@media (min-width:992px){.card.bmd-card-flat{box-shadow:none}}.card .card-header{border-bottom:none;background:transparent}.card .card-header .title{color:#fff}.card .card-header .nav-tabs{padding:0}.card .card-header.card-header-image{position:relative;padding:0;z-index:1;margin-left:15px;margin-right:15px;margin-top:-30px;border-radius:6px}.card .card-header.card-header-image img{width:100%;border-radius:6px;pointer-events:none;box-shadow:0 5px 15px -8px rgba(0,0,0,.24),0 8px 10px -5px rgba(0,0,0,.2)}.card .card-header.card-header-image .card-title{position:absolute;bottom:15px;left:15px;color:#fff;font-size:1.125rem;text-shadow:0 2px 5px rgba(33,33,33,.5)}.card .card-header.card-header-image .colored-shadow{transform:scale(.94);top:12px;filter:blur(12px);position:absolute;width:100%;height:100%;background-size:cover;z-index:-1;transition:opacity .45s;opacity:0}.card .card-header.card-header-image.no-shadow{box-shadow:none}.card .card-header.card-header-image.no-shadow.shadow-normal{box-shadow:0 16px 38px -12px rgba(0,0,0,.56),0 4px 25px 0 rgba(0,0,0,.12),0 8px 10px -5px rgba(0,0,0,.2)}.card .card-header.card-header-image.no-shadow .colored-shadow{display:none!important}.card.bg-primary,.card .card-header-primary .card-icon,.card .card-header-primary .card-text,.card .card-header-primary:not(.card-header-icon):not(.card-header-text),.card.card-rotate.bg-primary .back,.card.card-rotate.bg-primary .front{background:linear-gradient(60deg,#ab47bc,#8e24aa)}.card.bg-info,.card .card-header-info .card-icon,.card .card-header-info .card-text,.card .card-header-info:not(.card-header-icon):not(.card-header-text),.card.card-rotate.bg-info .back,.card.card-rotate.bg-info .front{background:linear-gradient(60deg,#26c6da,#00acc1)}.card.bg-success,.card .card-header-success .card-icon,.card .card-header-success .card-text,.card .card-header-success:not(.card-header-icon):not(.card-header-text),.card.card-rotate.bg-success .back,.card.card-rotate.bg-success .front{background:linear-gradient(60deg,#66bb6a,#43a047)}.card.bg-warning,.card .card-header-warning .card-icon,.card .card-header-warning .card-text,.card .card-header-warning:not(.card-header-icon):not(.card-header-text),.card.card-rotate.bg-warning .back,.card.card-rotate.bg-warning .front{background:linear-gradient(60deg,#ffa726,#fb8c00)}.card.bg-danger,.card .card-header-danger .card-icon,.card .card-header-danger .card-text,.card .card-header-danger:not(.card-header-icon):not(.card-header-text),.card.card-rotate.bg-danger .back,.card.card-rotate.bg-danger .front{background:linear-gradient(60deg,#ef5350,#e53935)}.card.bg-rose,.card .card-header-rose .card-icon,.card .card-header-rose .card-text,.card .card-header-rose:not(.card-header-icon):not(.card-header-text),.card.card-rotate.bg-rose .back,.card.card-rotate.bg-rose .front{background:linear-gradient(60deg,#ec407a,#d81b60)}.card .card-header-primary .card-icon,.card .card-header-primary .card-text,.card .card-header-primary:not(.card-header-icon):not(.card-header-text){box-shadow:0 4px 20px 0 rgba(0,0,0,.14),0 7px 10px -5px rgba(156,39,176,.4)}.card .card-header-danger .card-icon,.card .card-header-danger .card-text,.card .card-header-danger:not(.card-header-icon):not(.card-header-text){box-shadow:0 4px 20px 0 rgba(0,0,0,.14),0 7px 10px -5px rgba(244,67,54,.4)}.card .card-header-rose .card-icon,.card .card-header-rose .card-text,.card .card-header-rose:not(.card-header-icon):not(.card-header-text){box-shadow:0 4px 20px 0 rgba(0,0,0,.14),0 7px 10px -5px rgba(233,30,99,.4)}.card .card-header-warning .card-icon,.card .card-header-warning .card-text,.card .card-header-warning:not(.card-header-icon):not(.card-header-text){box-shadow:0 4px 20px 0 rgba(0,0,0,.14),0 7px 10px -5px rgba(255,152,0,.4)}.card .card-header-info .card-icon,.card .card-header-info .card-text,.card .card-header-info:not(.card-header-icon):not(.card-header-text){box-shadow:0 4px 20px 0 rgba(0,0,0,.14),0 7px 10px -5px rgba(0,188,212,.4)}.card .card-header-success .card-icon,.card .card-header-success .card-text,.card .card-header-success:not(.card-header-icon):not(.card-header-text){box-shadow:0 4px 20px 0 rgba(0,0,0,.14),0 7px 10px -5px rgba(76,175,80,.4)}.card[class*=bg-],.card[class*=bg-] .card-title,.card[class*=bg-] .card-title a,.card[class*=bg-] .icon i,.card [class*=card-header-],.card [class*=card-header-] .card-title,.card [class*=card-header-] .card-title a,.card [class*=card-header-] .icon i{color:#fff}.card[class*=bg-] .icon i,.card [class*=card-header-] .icon i{border-color:hsla(0,0%,100%,.25)}.card[class*=bg-] .author a,.card[class*=bg-] .card-category,.card[class*=bg-] .card-description,.card[class*=bg-] .stats,.card [class*=card-header-] .author a,.card [class*=card-header-] .card-category,.card [class*=card-header-] .card-description,.card [class*=card-header-] .stats{color:hsla(0,0%,100%,.8)}.card[class*=bg-] .author a:active,.card[class*=bg-] .author a:focus,.card[class*=bg-] .author a:hover,.card [class*=card-header-] .author a:active,.card [class*=card-header-] .author a:focus,.card [class*=card-header-] .author a:hover{color:#fff}.card .author .avatar{width:30px;height:30px;overflow:hidden;border-radius:50%;margin-right:5px}.card .author a{color:#3c4858;text-decoration:none}.card .author a .ripple-container{display:none}.card .card-category-social .fa{font-size:24px;position:relative;margin-top:-4px;top:2px;margin-right:5px}.card .card-category-social .material-icons{position:relative;top:5px}.card[class*=bg-],.card[class*=bg-] .card-body{border-radius:6px}.card[class*=bg-] .card-body h1 small,.card[class*=bg-] .card-body h2 small,.card[class*=bg-] .card-body h3 small,.card[class*=bg-] h1 small,.card[class*=bg-] h2 small,.card[class*=bg-] h3 small{color:hsla(0,0%,100%,.8)}.card .card-stats{background:transparent;display:flex}.card .card-stats .author,.card .card-stats .stats{display:inline-flex}.card{box-shadow:0 1px 4px 0 rgba(0,0,0,.14)}.card .table tr:first-child td{border-top:none}.card .card-title{margin-top:0;margin-bottom:3px}.card .card-body{padding:.9375rem 20px;position:relative}.card .card-body .form-group{margin:8px 0 0}.card .card-header{z-index:3!important}.card .card-header .card-title{margin-bottom:3px}.card .card-header .card-category{margin:0}.card .card-header.card-header-text{display:inline-block}.card .card-header.card-header-text:after{content:"";display:table}.card .card-header.card-header-icon i,.card .card-header.card-header-text i{width:33px;height:33px;text-align:center;line-height:33px}.card .card-header.card-header-icon .card-title,.card .card-header.card-header-text .card-title{margin-top:15px;color:#3c4858}.card .card-header.card-header-icon h4,.card .card-header.card-header-text h4{font-weight:300}.card .card-header.card-header-tabs .nav-tabs{background:transparent;padding:0}.card .card-header.card-header-tabs .nav-tabs-title{float:left;padding:10px 10px 10px 0;line-height:24px}.card.card-plain .card-header.card-header-icon+.card-body .card-category,.card.card-plain .card-header.card-header-icon+.card-body .card-title{margin-top:-20px}.card .card-actions{position:absolute;z-index:1;top:-50px;width:calc(100% - 30px);left:17px;right:17px;text-align:center}.card .card-actions .card-header{padding:0;min-height:160px}.card .card-actions .btn{padding-left:12px;padding-right:12px}.card .card-actions .fix-broken-card{position:absolute;top:-65px}.card.card-chart .card-footer i:nth-child(1n+2){width:18px;text-align:center}.card.card-chart .card-category{margin:0}.card .card-body+.card-footer,.card .card-footer{padding:0;padding-top:10px;margin:0 15px 10px;border-radius:0;justify-content:space-between;align-items:center}.card .card-body+.card-footer h6,.card .card-footer h6{width:100%}.card .card-body+.card-footer .stats,.card .card-footer .stats{color:#999;font-size:12px;line-height:22px}.card .card-body+.card-footer .stats .card-category,.card .card-footer .stats .card-category{padding-top:7px;padding-bottom:7px;margin:0}.card .card-body+.card-footer .stats .material-icons,.card .card-footer .stats .material-icons{position:relative;top:4px;font-size:16px}.card [class*=card-header-]{margin:0 15px;padding:0;position:relative}.card [class*=card-header-] .card-title+.card-category{color:hsla(0,0%,100%,.8)}.card [class*=card-header-] .card-title+.card-category a{color:#fff}.card [class*=card-header-]:not(.card-header-icon):not(.card-header-text):not(.card-header-image){border-radius:3px;margin-top:-20px;padding:15px}.card [class*=card-header-] .card-icon,.card [class*=card-header-] .card-text{border-radius:3px;background-color:#999;padding:15px;margin-top:-20px;margin-right:15px;float:left}.card [class*=card-header-] .card-text{float:none;display:inline-block;margin-right:0}.card [class*=card-header-] .card-text .card-title{color:#fff;margin-top:0}.card [class*=card-header-] .ct-chart .card-title{color:#fff}.card [class*=card-header-] .ct-chart .card-category{margin-bottom:0;color:hsla(0,0%,100%,.62)}.card [class*=card-header-] .ct-chart .ct-label{color:hsla(0,0%,100%,.7)}.card [class*=card-header-] .ct-chart .ct-grid{stroke:hsla(0,0%,100%,.2)}.card [class*=card-header-] .ct-chart .ct-series-a .ct-bar,.card [class*=card-header-] .ct-chart .ct-series-a .ct-line,.card [class*=card-header-] .ct-chart .ct-series-a .ct-point,.card [class*=card-header-] .ct-chart .ct-series-a .ct-slice-donut{stroke:hsla(0,0%,100%,.8)}.card [class*=card-header-] .ct-chart .ct-series-a .ct-area,.card [class*=card-header-] .ct-chart .ct-series-a .ct-slice-pie{fill:hsla(0,0%,100%,.4)}.card [class*=card-header-] .ct-chart .ct-series-a .ct-bar{stroke-width:10px}.card [class*=card-header-] .ct-chart .ct-point{stroke-width:10px;stroke-linecap:round}.card [class*=card-header-] .ct-chart .ct-line{fill:none;stroke-width:4px}.card [data-header-animation=true]{transform:translateZ(0);transition:all .3s cubic-bezier(.34,1.61,.7,1)}.card:hover [data-header-animation=true]{transform:translate3d(0,-50px,0)}.card .map{height:280px;border-radius:6px;margin-top:15px}.card .map.map-big{height:420px}.card .card-body.table-full-width{padding:0}.card .card-plain .card-header-icon{margin-right:15px!important}.table-sales{margin-top:40px}.iframe-container{width:100%}.iframe-container iframe{width:100%;height:500px;border:0;box-shadow:0 16px 38px -12px rgba(0,0,0,.56),0 4px 25px 0 rgba(0,0,0,.12),0 8px 10px -5px rgba(0,0,0,.2)}.card-wizard .nav.nav-pills .nav-item{margin:0}.card-wizard .nav.nav-pills .nav-item .nav-link{padding:6px 15px!important}.card-wizard .nav-pills:not(.flex-column) .nav-item+.nav-item:not(:first-child){margin-left:0}.card-wizard .nav-item .nav-link.active,.card-wizard .nav-item .nav-link:focus,.card-wizard .nav-item .nav-link:hover{background-color:inherit!important;box-shadow:none!important}.card-wizard .input-group-text{padding:6px 15px 0!important}.card-wizard .card-footer{border-top:none!important}.card-chart .card-body+.card-footer,.card-product .card-body+.card-footer{border-top:1px solid #eee}.card-product .price{color:inherit}.card-collapse{margin-bottom:15px}.card-collapse .card .card-header a[aria-expanded=true]{color:#e91e63}.card-signup .card-header{margin:-40px 20px 15px;padding:20px 0;width:100%}.card-signup .card-body{padding:0 30px 0 10px}.card-signup .form-check{padding-top:27px}.card-signup .form-check label{margin-left:18px}.card-signup .form-check .form-check-sign{padding-right:27px}.card-signup .social-line{margin-top:1rem;text-align:center;padding:0}.card-signup .social-line .btn{color:#fff;margin-left:5px;margin-right:5px}.card-plain{background:transparent;box-shadow:none}.card-plain .card-header:not(.card-avatar){margin-left:0;margin-right:0}.card-plain .card-body{padding-left:5px;padding-right:5px}.card-plain .card-header-image{margin:0!important;border-radius:6px}.card-plain .card-header-image img{border-radius:6px}.card-plain .card-footer{padding-left:5px;padding-right:5px;background-color:transparent}.card-plain .card-header:not(.card-avatar) .card-category,.card-plain .card-header:not(.card-avatar) .card-description{color:#999}.card-stats .card-header.card-header-icon,.card-stats .card-header.card-header-text{text-align:right}.card-stats .card-header .card-icon+.card-category,.card-stats .card-header .card-icon+.card-title{padding-top:10px}.card-stats .card-header.card-header-icon .card-category,.card-stats .card-header.card-header-icon .card-title,.card-stats .card-header.card-header-text .card-category,.card-stats .card-header.card-header-text .card-title{margin:0}.card-stats .card-header .card-category{margin-bottom:0;margin-top:0}.card-stats .card-header .card-category:not([class*=text-]){color:#999;font-size:14px}.card-stats .card-header+.card-footer{border-top:1px solid #eee;margin-top:20px}.card-stats .card-header.card-header-icon i{font-size:36px;line-height:56px;width:56px;height:56px;text-align:center}.card-stats .card-body{text-align:right}.card-profile,.card-testimonial{margin-top:30px;text-align:center}.card-profile .card-avatar,.card-testimonial .card-avatar{margin:-50px auto 0;border-radius:50%;overflow:hidden;padding:0;box-shadow:0 16px 38px -12px rgba(0,0,0,.56),0 4px 25px 0 rgba(0,0,0,.12),0 8px 10px -5px rgba(0,0,0,.2)}.card-profile .card-avatar+.card-body,.card-testimonial .card-avatar+.card-body{margin-top:15px}.card-profile .card-avatar img,.card-testimonial .card-avatar img{width:100%;height:auto}.card-profile .card-body+.card-footer,.card-testimonial .card-body+.card-footer{margin-top:-15px}.card-profile .card-footer .btn.btn-just-icon,.card-testimonial .card-footer .btn.btn-just-icon{font-size:20px;padding:12px;line-height:1em}.card-plain.card-profile .card-avatar,.card-plain.card-testimonial .card-avatar{margin-top:0}.card-testimonial .card-avatar{max-width:100px;max-height:100px}.card-testimonial .card-footer{margin-top:0;display:block}.card-testimonial .card-footer .card-avatar{margin-top:10px;margin-bottom:-60px}.card-testimonial .card-description{font-style:italic}.card-testimonial .card-description+.card-title,.card-testimonial .icon{margin-top:30px}.card-testimonial .icon .material-icons{font-size:40px}.card-profile .card-header:not([class*=card-header-]){background:transparent}.card-profile .card-avatar{max-width:130px;max-height:130px}.card-blog{margin-top:60px}.card-blog [class*=col-] .card-header-image img{width:100%}.card-blog .carf-footer .stats .material-icons{font-size:18px;position:relative;top:4px;width:19px}.card-product{margin-top:30px}.card-product .btn-simple.btn-just-icon{padding:0}.card-product .card-footer .price h4{margin-bottom:0}.card-product .card-footer .btn{margin:0}.card-product .card-category,.card-product .card-description,.card-product .card-title{text-align:center}.card-product .category{margin-bottom:0}.card-product .category~.card-title{margin-top:0}.card-product .price{font-size:18px;color:#9a9a9a}.card-product .price-old{text-decoration:line-through;font-size:16px;color:#9a9a9a}.card-product .price-new{color:#f44336}.card-pricing{text-align:center}.card-pricing:after{background-color:rgba(0,0,0,.7)!important}.card-pricing .card-title{margin-top:30px}.card-pricing .card-body{padding:15px!important;margin:0!important}.card-pricing .card-icon{padding:10px 0 0}.card-pricing .card-icon i{font-size:55px;border:1px solid #e5e5e5;border-radius:50%;width:130px;line-height:130px;height:130px;color:#3c4858}.card-pricing .card-icon.icon-primary i{color:#9c27b0}.card-pricing .card-icon.icon-info i{color:#00bcd4}.card-pricing .card-icon.icon-success i{color:#4caf50}.card-pricing .card-icon.icon-warning i{color:#ff9800}.card-pricing .card-icon.icon-danger i{color:#f44336}.card-pricing .card-icon.icon-rose i{color:#e91e63}.card-pricing .card-icon.icon-white i{color:#fff}.card-pricing h1 small{font-size:18px;display:inline-flex;height:0}.card-pricing h1 small:first-child{position:relative;top:-17px;font-size:26px}.card-pricing ul{list-style:none;padding:0;max-width:240px;margin:10px auto}.card-pricing ul li{color:#999;text-align:center;padding:12px 0;border-bottom:1px solid hsla(0,0%,60%,.3)}.card-pricing ul li:last-child{border:0}.card-pricing ul li b{color:#3c4858}.card-pricing ul li i{top:6px;position:relative}.card-pricing.card-background ul li,.card-pricing[class*=bg-] ul li{color:#fff;border-color:hsla(0,0%,100%,.3)}.card-pricing.card-background ul li b,.card-pricing[class*=bg-] ul li b{color:#fff;font-weight:700}.card-pricing.card-background .card-category,.card-pricing.card-background [class*=text-],.card-pricing[class*=bg-] .card-category,.card-pricing[class*=bg-] [class*=text-]{color:#fff!important}.card-pricing .card-footer{z-index:2}.card-collapse,.card-collapse .card-header{box-shadow:none;background-color:transparent;border-radius:0}.card-collapse{margin:0}.card-collapse .card-header{border-bottom:1px solid #ddd;padding:25px 10px 5px 0;margin:0;box-shadow:none!important;background:#fff}.card-collapse .card-header a{color:#3c4858;font-size:.9375rem;display:block}.card-collapse .card-header a:active,.card-collapse .card-header a:hover,.card-collapse .card-header a[aria-expanded=true]{color:#e91e63}.card-collapse .card-header a i{float:right;top:4px;position:relative}.card-collapse .card-header a[aria-expanded=true] i{filter:progid:DXImageTransform.Microsoft.BasicImage(rotation=2);transform:rotate(180deg)}.card-collapse .card-body{padding:15px 0 5px}.card-form-horizontal .card-body{padding-left:15px;padding-right:15px}.card-form-horizontal .form-group .form-control,.card-form-horizontal .input-group .form-control{margin-bottom:0}.card-form-horizontal .btn,.card-form-horizontal form{margin:0}.card-form-horizontal .input-group .input-group-addon{padding-left:0}.card-form-horizontal .bmd-form-group{padding-bottom:0;padding-top:0}.back-background,.card-background,.front-background{background-position:50%;background-size:cover;text-align:center}.back-background .card-body,.card-background .card-body,.front-background .card-body{position:relative;z-index:2;min-height:280px;padding-top:40px;padding-bottom:40px;max-width:440px;margin:0 auto}.back-background .card-category,.back-background .card-description,.back-background small,.card-background .card-category,.card-background .card-description,.card-background small,.front-background .card-category,.front-background .card-description,.front-background small{color:hsla(0,0%,100%,.7)!important}.back-background .card-title,.card-background .card-title,.front-background .card-title{color:#fff;margin-top:10px}.back-background:not(.card-pricing) .btn,.card-background:not(.card-pricing) .btn,.front-background:not(.card-pricing) .btn{margin-bottom:0}.back-background:after,.card-background:after,.front-background:after{position:absolute;z-index:1;width:100%;height:100%;display:block;left:0;top:0;content:"";background-color:rgba(0,0,0,.56);border-radius:6px}.rotating-card-container{-o-perspective:800px;-ms-perspective:800px;perspective:800px}.rotating-card-container .card-rotate{background:transparent;box-shadow:none}.rotating-card-container .card-rotate:after{display:none}.rotating-card-container .card{transition:all .8s cubic-bezier(.34,1.45,.7,1);transform-style:preserve-3d;position:relative}.rotating-card-container .card .back,.rotating-card-container .card .front{-webkit-backface-visibility:hidden;backface-visibility:hidden;box-shadow:0 2px 2px 0 rgba(0,0,0,.14),0 3px 1px -2px rgba(0,0,0,.12),0 1px 5px 0 rgba(0,0,0,.2);position:absolute;background-color:#fff;border-radius:6px;top:0;left:0}.rotating-card-container .card .back,.rotating-card-container .card .back .card-body,.rotating-card-container .card .front,.rotating-card-container .card .front .card-body{justify-content:center;align-content:center;display:-moz-flex;display:-ms-flexbox;display:-o-flex;display:flex;-moz-flex-direction:column;-ms-flex-direction:column;-o-flex-direction:column;flex-direction:column}.rotating-card-container .card .front{z-index:2;position:relative}.rotating-card-container .card .back{transform:rotateY(180deg);z-index:5;text-align:center;width:100%;height:100%}.rotating-card-container .card .back.back-background:after{position:absolute;z-index:1;width:100%;height:100%;display:block;left:0;top:0;content:"";background-color:rgba(0,0,0,.56);border-radius:6px}.rotating-card-container .card .back.back-background .card-body{position:relative;z-index:2}.rotating-card-container .card .back .card-footer .btn{margin:0}.rotating-card-container .card .back .card-body{padding-left:15px;padding-right:15px}.rotating-card-container.hover.manual-flip .card,.rotating-card-container:not(.manual-flip):hover .card{transform:rotateY(180deg)}.card-profile .rotating-card-container .front{text-align:left}.back-background .card-body{min-height:auto;padding-top:15px;padding-bottom:15px}@media (-ms-high-contrast:none),screen and (-ms-high-contrast:active){.rotating-card-container .card .back,.rotating-card-container .card .front{backface-visibility:visible}.rotating-card-container .card .back{visibility:hidden;transition:visibility .3s cubic-bezier(.34,1.45,.7,1)}.rotating-card-container .card .front{z-index:4}.rotating-card-container.manual-flip.hover .card .back,.rotating-card-container:not(.manual-flip):hover .card .back{z-index:5;visibility:visible}}.card .card-body .col-form-label,.card .card-body .label-on-right{padding:17px 5px 0 0;text-align:right}.card .card-body .col-form-label.label-checkbox,.card .card-body .label-on-right.label-checkbox{padding-top:13px}.card .card-body .label-on-right{text-align:left}.card .label-on-right code{padding:2px 4px;font-size:90%;color:#c7254e;background-color:#f9f2f4;border-radius:4px}.card-wizard .input-group .form-group{width:80%}form .form-group{margin:8px 0 0}form .form-group label[for=inputState]{position:absolute;top:-12px}form .form-group select.form-control{position:absolute;top:-5px}form .form-group .error{font-size:.8rem;color:#f44336}form .card .card-footer .form-check{margin-left:7px}form .checkbox-radios{margin-top:8px}.bmd-label-static{top:-7px!important}.form-check .form-check-label{padding-right:15px}@media (max-width:991px){.card .card-body .col-form-label,.card .card-body .label-on-right{text-align:left;padding-left:15px;padding-top:8px}}.bmd-form-group.is-focused .bmd-label-floating{top:-.7rem!important}a{color:#9c27b0}a:focus,a:hover{color:#89229b;text-decoration:none}a.text-info:focus,a.text-info:hover{color:#00a5bb}a .material-icons{vertical-align:middle}.animation-transition-fast,.bootstrap-datetimepicker-widget table td>div,.bootstrap-datetimepicker-widget table td span,.bootstrap-datetimepicker-widget table th,.bootstrap-datetimepicker-widget table th>div,.bootstrap-tagsinput .tag,.bootstrap-tagsinput [data-role=remove],.card-collapse .card-header a i,.navbar{transition:all .15s ease 0s}.signup-page .card-signup form .form-check{padding-left:20px}.signup-page .card-signup form .form-check .form-check-label{padding-left:35px}.section-signup .card-signup .card-header{width:auto}.section-signup .card-signup .card-body .input-group{padding-bottom:7px;margin:27px 0 0}.offline-doc .page-header,.offline-free-doc .page-header{height:100vh!important}.offline-doc .page-header:after,.offline-free-doc .page-header:after{background:rgba(0,0,0,.5)!important}.offline-doc .footer,.offline-free-doc .footer{position:absolute;width:100%;background:transparent;bottom:0;color:#fff;z-index:1}.offline-doc .footer .copyright a,.offline-doc .navbar .navbar-brand,.offline-doc .navbar .navbar-collapse .nav-link,.offline-free-doc .footer .copyright a,.offline-free-doc .navbar .navbar-brand,.offline-free-doc .navbar .navbar-collapse .nav-link{color:#fff}@keyframes e{0%{transform-origin:top left;animation-timing-function:ease-in-out}20%,60%{transform:rotate(80deg);transform-origin:top left;animation-timing-function:ease-in-out}40%,80%{transform:rotate(60deg);transform-origin:top left;animation-timing-function:ease-in-out;opacity:1}to{transform:translate3d(0,700px,0);opacity:0}}.hinge{animation-name:e}.tim-row{margin-bottom:20px}.tim-white-buttons{background-color:#777}.title{margin-top:30px;margin-bottom:25px;min-height:32px}#map{z-index:2;height:calc(100vh - 70px);margin-top:70px}#map,.tim-typo{position:relative;width:100%}.tim-typo{padding-left:25%;margin-bottom:40px}.tim-typo .tim-note{bottom:5px;color:#c0c1c2;display:block;font-weight:400;font-size:13px;line-height:15px;left:0;margin-left:20px;position:absolute;width:260px}.tim-row{padding-top:50px}.tim-row h3{margin-top:0}#typography h1,#typography h2,#typography h3,#typography h4,#typography h5,#typography h6{margin-bottom:0}.switch{margin-right:20px}#navbar-full .navbar{border-radius:0!important;margin-bottom:15px;z-index:2}.space{height:130px;display:block}.space-110{height:110px;display:block}.space-50{height:50px;display:block}.space-70{height:70px;display:block}.navigation-example .img-src{background-attachment:scroll}.navigation-example{background-position:50%;background-size:cover;margin-top:0;min-height:740px}#notifications{background-color:#fff;display:block;width:100%;position:relative}#notifications .alert-danger{margin-bottom:0}.tim-note{text-transform:capitalize}#buttons .btn{margin:0 0 15px}.space-100{height:100px}.parallax,.space-100{display:block;width:100%}.parallax{height:570px;background-attachment:fixed;background-repeat:no-repeat;background-size:cover;background-position:50%}.parallax .parallax-image{width:100%;overflow:hidden;position:absolute}.parallax .parallax-image img{width:100%}@media (max-width:768px){.parallax .parallax-image{width:100%;height:640px;overflow:hidden}.parallax .parallax-image img{height:100%;width:auto}}.separator{content:"Separator";color:#fff;display:block;width:100%;padding:20px}.separator-line{height:1px;width:100%;display:block}.separator-line,.separator.separator-gray{background-color:#eee}.social-buttons-demo .btn{margin:10px 5px 7px 1px}.img-container{width:100%;overflow:hidden}.img-container img{width:100%}.section-black{background-color:#333}.animate{transition:1.5s ease-in-out;-moz-transition:1.5s ease-in-out;-webkit-transition:1.5s ease-in-out}.sharing-area{margin-top:80px}.sharing-area .btn{margin:15px 4px 0;color:#fff}.sharing-area .btn i{font-size:18px;position:relative;top:2px;margin-right:5px}#navbar{margin-bottom:-20px}.sharing-area .btn-twitter{background-color:#55acee}.sharing-area .btn-facebook{background-color:#3b5998}.sharing-area .btn-google-plus{background-color:#dd4b39}.sharing-area .btn-github{background-color:#333}#navbar .navbar{border-radius:0}@media (max-width:830px){.main-raised{margin-left:10px;margin-right:10px}}.bootstrap-select .hidden{display:none}.disabled{pointer-events:none;cursor:not-allowed}.bd-docs .alert-dismissible .close{top:10px}.bd-docs .bd-example .btn.btn-social{margin-bottom:10px}.bd-docs .bd-content .bd-title .btn{padding:7px 20px;margin-bottom:10px}.dropdown .dropdown-menu .dropdown-item.dropdown-toggle+.dropdown-menu{transform:scale(0);transform-origin:0 0;display:block}.dropdown .dropdown-menu.show .dropdown-item.dropdown-toggle+.dropdown-menu.show{left:101%!important;transform:scale(1)}.dropdown .dropdown-menu.show .dropdown-toggle.open:after{transform:rotate(180deg)}@media (max-width:991px){.menu-on-left .navbar .container,.menu-on-left .navbar .container-fluid{display:flex;flex-direction:row-reverse}.timepicker .btn .ripple-container{top:-11px;left:3px;z-index:1;width:40px;border-radius:50%!important;height:40px}}.card-calendar .fc-button:focus{outline:none}.error-page .title{font-size:12em;color:#fff;letter-spacing:14px;font-weight:700}.footer-big{padding:1.875rem 0}.footer-big .content{text-align:left}.footer-big .social-feed i{font-size:20px;display:table-cell;padding-right:10px}.footer-big .social-feed p{display:table-cell;vertical-align:top;overflow:hidden;padding-bottom:10px;max-width:300px}.footer-big .gallery-feed img{width:20%;margin-right:5%;margin-bottom:5%;float:left}.footer-white{background-color:#fff}.footer-gray{background-color:#eee}.footer-black{background:#232323;background:radial-gradient(ellipse at center,#585858 0,#232323 100%);background-size:550% 450%}.footer-black a{color:#fff;opacity:.86}.footer-black a:focus,.footer-black a:hover{opacity:1}.footer-black .copyright,.footer-black .footer-brand,.footer-black .footer-brand:focus,.footer-black .footer-brand:hover,.footer-black h4,.footer-black h5,.footer-black i{color:#fff}.footer-black hr{border-color:hsla(0,0%,100%,.2)}.rtl .bootstrap-navbar,.rtl .sidebar{right:0;left:auto}.rtl .bootstrap-navbar .nav-mobile-menu .notification,.rtl .sidebar .nav-mobile-menu .notification{float:right;margin-right:0;margin-left:8px}.rtl .bootstrap-navbar .nav i,.rtl .sidebar .nav i{float:right!important;margin-left:15px;margin-right:0}.rtl .bootstrap-navbar .nav p,.rtl .sidebar .nav p{margin:0;text-align:right}.rtl .bootstrap-navbar .nav .caret,.rtl .sidebar .nav .caret{left:11px;right:auto}.rtl .bootstrap-navbar .logo a.logo-mini,.rtl .sidebar .logo a.logo-mini{float:right;margin-right:30px;margin-left:10px}.rtl .bootstrap-navbar .logo .simple-text,.rtl .sidebar .logo .simple-text{text-align:right}.rtl .bootstrap-navbar .user .user-info>a>span,.rtl .sidebar .user .user-info>a>span{text-align:right;display:block}.rtl .bootstrap-navbar .user .photo,.rtl .sidebar .user .photo{float:right;margin-left:12px;margin-right:23px}.rtl .bootstrap-navbar .user .user-info .caret,.rtl .sidebar .user .user-info .caret{left:22px;right:auto}.rtl .bootstrap-navbar .sidebar-wrapper .nav [data-toggle=collapse]~div>ul>li>.sidebar-mini,.rtl .bootstrap-navbar .sidebar-wrapper .user .user-info [data-toggle=collapse]~div>ul>li>.sidebar-mini,.rtl .sidebar .sidebar-wrapper .nav [data-toggle=collapse]~div>ul>li>.sidebar-mini,.rtl .sidebar .sidebar-wrapper .user .user-info [data-toggle=collapse]~div>ul>li>.sidebar-mini{float:right;margin-left:15px;margin-right:0}.rtl .navbar-minimize{margin-right:15px}.rtl .navbar-header .navbar-toggle{margin:10px 0 10px 15px}.rtl .btn:not(.btn-just-icon):not(.btn-fab) .fa,.rtl .navbar .navbar-nav>li>a.btn:not(.btn-just-icon):not(.btn-fab) .fa{left:5px}.rtl .card .card-header.card-header-icon{float:right}.rtl .main-panel{float:left}.rtl .navbar>.container-fluid .navbar-brand{margin-right:10px}.rtl .dropdown-menu{right:auto;left:0}.rtl .card .card-header.card-header-tabs .nav-tabs-title{float:right;padding:10px 0 10px 10px}.rtl .card.card-product .card-footer{display:flex;align-items:center;flex-direction:row-reverse;justify-content:space-between}.rtl .navbar-nav.navbar-right>li>.dropdown-menu:after,.rtl .navbar-nav.navbar-right>li>.dropdown-menu:before{right:auto;left:12px}.rtl .card .form-horizontal .label-on-left{padding-top:16px;text-align:left}.rtl .form-horizontal .radio label span{right:2px}.rtl .form-check .form-check-label .form-check-sign .check:before{margin-right:11px}.rtl .card .checkbox .checkbox-material:before{left:0}.rtl .nav-pills>li+li{margin-right:0}.rtl .checkbox-inline,.rtl .radio-inline{padding-right:0;margin-top:5px}.rtl .form-horizontal .checkbox-radios .checkbox:first-child,.rtl .form-horizontal .checkbox-radios .radio:first-child{margin-top:5px}.rtl .checkbox label,.rtl .radio label{padding:0}.rtl .radio label{padding-right:28px}.rtl .card .form-horizontal .label-on-right{text-align:right;padding-top:17px}.rtl .alert button.close{left:10px!important;right:auto!important}.rtl .alert span[data-notify=icon] {right:15px;left:auto}.rtl .alert.alert-with-icon{padding-right:65px;padding-left:15px}.rtl .alert.alert-with-icon i[data-notify=icon]{right:15px;left:auto}@media (max-width:991px){.rtl .sidebar .sidebar-wrapper .user .user-info [data-toggle=collapse]~div>ul>li>.sidebar-normal,.rtl .sidebar .sidebar-wrapper>.nav [data-toggle=collapse]~div>ul>li>.sidebar-normal{text-align:right}}@media (max-width:768px){.rtl .navbar>.container-fluid .navbar-brand{margin-right:15px}.rtl .navbar-header .navbar-toggle{margin-left:30px}}@media (min-width:991px){.rtl.sidebar-mini .bootstrap-navbar .nav i,.rtl.sidebar-mini .sidebar .nav i{margin:0}.rtl.sidebar-mini .sidebar .sidebar-wrapper .user .user-info>a>span,.rtl.sidebar-mini .sidebar .sidebar-wrapper .user .user-info [data-toggle=collapse]~div>ul>li>.sidebar-normal,.rtl.sidebar-mini .sidebar .sidebar-wrapper>.nav [data-toggle=collapse]~div>ul>li>.sidebar-normal,.rtl.sidebar-mini .sidebar .sidebar-wrapper>.nav li>a p{position:relative}.rtl.sidebar-mini .sidebar .logo a.logo-normal,.rtl.sidebar-mini .sidebar .sidebar-wrapper .user .user-info>a>span,.rtl.sidebar-mini .sidebar .sidebar-wrapper .user .user-info [data-toggle=collapse]~div>ul>li>.sidebar-normal,.rtl.sidebar-mini .sidebar .sidebar-wrapper>.nav [data-toggle=collapse]~div>ul>li>.sidebar-normal,.rtl.sidebar-mini .sidebar .sidebar-wrapper>.nav li>a p,.rtl.sidebar-mini .sidebar:hover .sidebar-wrapper .user .user-info>a>span,.rtl.sidebar-mini .sidebar:hover .sidebar-wrapper .user .user-info [data-toggle=collapse]~div>ul>li>.sidebar-normal,.rtl.sidebar-mini .sidebar:hover .sidebar-wrapper>.nav [data-toggle=collapse]~div>ul>li>.sidebar-normal,.rtl.sidebar-mini .sidebar:hover .sidebar-wrapper>.nav li>a p{transform:translateX(25px)}.rtl.sidebar-mini .sidebar:hover .logo a.logo-normal,.rtl.sidebar-mini .sidebar:hover .sidebar-wrapper .user .user-info>a>span,.rtl.sidebar-mini .sidebar:hover .sidebar-wrapper .user .user-info [data-toggle=collapse]~div>ul>li>.sidebar-normal,.rtl.sidebar-mini .sidebar:hover .sidebar-wrapper>.nav [data-toggle=collapse]~div>ul>li>.sidebar-normal,.rtl.sidebar-mini .sidebar:hover .sidebar-wrapper>.nav li>a p{transform:translateZ(0)}}.rtl.sidebar-mini .nav .nav-item .nav-link i{margin-right:0}.rtl .navbar .collapse .nav-item .nav-link .notification{top:-10px}.rtl .sidebar-wrapper .nav .nav-item .collapse .nav .nav-item .nav-link .sidebar-mini,.rtl .sidebar-wrapper .nav .nav-item .collapsing .nav .nav-item .nav-link .sidebar-mini,.rtl .sidebar-wrapper .user .user-info .collapse .nav .nav-item .nav-link .sidebar-mini,.rtl .sidebar-wrapper .user .user-info .collapsing .nav .nav-item .nav-link .sidebar-mini{float:right}.rtl .sidebar-wrapper .nav .nav-item .collapse .nav .nav-item .nav-link .sidebar-normal,.rtl .sidebar-wrapper .nav .nav-item .collapsing .nav .nav-item .nav-link .sidebar-normal,.rtl .sidebar-wrapper .user .user-info .collapse .nav .nav-item .nav-link .sidebar-normal,.rtl .sidebar-wrapper .user .user-info .collapsing .nav .nav-item .nav-link .sidebar-normal{text-align:right;display:block}.rtl.sidebar-mini .collapse .nav .nav-item .nav-link .sidebar-mini,.rtl.sidebar-mini .collapsing .nav .nav-item .nav-link .sidebar-mini{margin-right:0!important}.rtl .sidebar .nav .nav-item .nav-link i{margin-right:0}.rtl .sidebar .nav .nav-item .nav .nav-item .nav-link .sidebar-mini,.rtl .sidebar .user .user-info [data-toggle=collapse]~div .nav .nav-item .nav-link .sidebar-mini{margin-right:0!important;float:right!important;margin-left:15px!important}.rtl .sidebar .user .user-info [data-toggle=collapse]~div .nav .nav-item .nav-link .sidebar-normal{display:block!important}.rtl .main-panel .card-header-text .card-text{float:right}.rtl .main-panel .card-header-text .card-text .card-category,.rtl .main-panel .card-header-text .card-text .card-title{text-align:right}.wrapper{position:relative;top:0;height:100vh}.sidebar{position:fixed;top:0;bottom:0;left:0;z-index:2;width:260px;box-shadow:0 16px 38px -12px rgba(0,0,0,.56),0 4px 25px 0 rgba(0,0,0,.12),0 8px 10px -5px rgba(0,0,0,.2)}.sidebar .caret{display:inline-block;width:0;height:0;margin-left:2px;vertical-align:middle;border-top:4px dashed;border-top:4px solid\9;border-right:4px solid transparent;border-left:4px solid transparent}.sidebar .sidebar-wrapper{position:relative;height:calc(100vh - 75px);overflow:auto;width:260px;z-index:4;padding-bottom:30px}.sidebar .sidebar-wrapper .dropdown .dropdown-backdrop{display:none!important}.sidebar .sidebar-wrapper .navbar-form{border:none;box-shadow:none}.sidebar .sidebar-wrapper .navbar-form .input-group{font-size:1.7em;height:36px;width:78%;padding-left:17px}.sidebar .sidebar-wrapper .user .user-info [data-toggle=collapse]~div>ul>li>a span,.sidebar .sidebar-wrapper>.nav [data-toggle=collapse]~div>ul>li>a span{display:inline-block}.sidebar .sidebar-wrapper .user .user-info [data-toggle=collapse]~div>ul>li>a .sidebar-normal,.sidebar .sidebar-wrapper>.nav [data-toggle=collapse]~div>ul>li>a .sidebar-normal{margin:0;position:relative;transform:translateX(0);opacity:1;white-space:nowrap;display:block}.sidebar .sidebar-wrapper .user .user-info [data-toggle=collapse]~div>ul>li>a .sidebar-mini,.sidebar .sidebar-wrapper>.nav [data-toggle=collapse]~div>ul>li>a .sidebar-mini{text-transform:uppercase;width:30px;margin-right:15px;text-align:center;letter-spacing:1px;position:relative;float:left;display:inherit}.sidebar .sidebar-wrapper .user .user-info [data-toggle=collapse]~div>ul>li>a i,.sidebar .sidebar-wrapper>.nav [data-toggle=collapse]~div>ul>li>a i{font-size:17px;line-height:20px;width:26px}.sidebar .nav{margin-top:15px;display:block}.sidebar .nav .caret{margin-top:13px;position:absolute;right:6px}.sidebar .nav li>a:focus,.sidebar .nav li>a:hover{background-color:transparent;outline:none}.sidebar .nav li:first-child>a{margin:0 15px}.sidebar .nav li.active>[data-toggle=collapse],.sidebar .nav li .dropdown-menu a:focus,.sidebar .nav li .dropdown-menu a:hover,.sidebar .nav li:hover>a{background-color:hsla(0,0%,78%,.2);color:#3c4858;box-shadow:none}.sidebar .nav li.active>[data-toggle=collapse] i{color:#a9afbb}.sidebar .nav li.active>a,.sidebar .nav li.active>a i{color:#fff}.sidebar .nav li.separator{margin:15px 0}.sidebar .nav li.separator:after{width:calc(100% - 30px);content:"";position:absolute;height:1px;left:15px;background-color:hsla(0,0%,71%,.3)}.sidebar .nav li.separator+li{margin-top:31px}.sidebar .nav p{margin:0;line-height:30px;font-size:14px;position:relative;display:block;height:auto;white-space:nowrap}.sidebar .nav i{font-size:24px;float:left;margin-right:15px;line-height:30px;width:30px;text-align:center;color:#a9afbb}.sidebar .nav li .dropdown-menu a,.sidebar .nav li a{margin:10px 15px 0;border-radius:3px;color:#3c4858;padding-left:10px;padding-right:10px;text-transform:capitalize;font-size:13px}.sidebar .sidebar-background{position:absolute;z-index:1;height:100%;width:100%;display:block;top:0;left:0;background-size:cover;background-position:50%}.sidebar .sidebar-background:after{position:absolute;z-index:3;width:100%;height:100%;content:"";display:block;background:#fff;opacity:.93}.sidebar .logo{padding:15px 0;margin:0;display:block;position:relative;z-index:4}.sidebar .logo a.logo-mini{opacity:1;float:left;width:30px;text-align:center;margin-left:23px;margin-right:15px}.sidebar .logo a.logo-normal{display:block;opacity:1;transform:translateZ(0)}.sidebar .logo:after{content:"";position:absolute;bottom:0;right:15px;height:1px;width:calc(100% - 30px);background-color:hsla(0,0%,71%,.3)}.sidebar .logo p{float:left;font-size:20px;margin:10px;color:#fff;line-height:20px}.sidebar .logo .simple-text{text-transform:uppercase;padding:5px 0;display:inline-block;font-size:18px;color:#3c4858;white-space:nowrap;font-weight:400;line-height:30px;overflow:hidden}.sidebar .logo-tim{border-radius:50%;border:1px solid #333;display:block;height:61px;width:61px;float:left;overflow:hidden}.sidebar .logo-tim img{width:60px;height:60px}.sidebar .user{padding-bottom:20px;margin:20px auto 0;position:relative}.sidebar .user:after{content:"";position:absolute;bottom:0;right:15px;height:1px;width:calc(100% - 30px);background-color:hsla(0,0%,71%,.3)}.sidebar .user .photo{width:34px;height:34px;overflow:hidden;float:left;z-index:5;margin-right:11px;border-radius:50%;margin-left:23px;box-shadow:0 16px 38px -12px rgba(0,0,0,.56),0 4px 25px 0 rgba(0,0,0,.12),0 8px 10px -5px rgba(0,0,0,.2)}.sidebar .user .photo img{width:100%}.sidebar .user a{color:#3c4858;padding:.5rem 15px;white-space:nowrap}.sidebar .user .user-info>a{display:block;line-height:18px;font-size:14px}.sidebar .user .user-info>a>span{display:block;position:relative;opacity:1}.sidebar .user .user-info .caret{position:absolute;top:8px;right:15px}.sidebar[data-background-color=black] .nav .nav-item .nav-link{color:#fff}.sidebar[data-background-color=black] .nav .nav-item i{color:hsla(0,0%,100%,.8)}.sidebar[data-background-color=black] .nav .nav-item.active [data-toggle=collapse],.sidebar[data-background-color=black] .nav .nav-item:hover [data-toggle=collapse]{color:#fff}.sidebar[data-background-color=black] .nav .nav-item.active [data-toggle=collapse] i,.sidebar[data-background-color=black] .nav .nav-item:hover [data-toggle=collapse] i{color:hsla(0,0%,100%,.8)}.sidebar[data-background-color=black] .simple-text,.sidebar[data-background-color=black] .user a{color:#fff}.sidebar[data-background-color=black] .sidebar-background:after{background:#000;opacity:.8}.sidebar[data-background-color=black] .nav li .dropdown-menu .dropdown-item{color:#fff}.sidebar[data-background-color=red]{background-color:#f44336}.sidebar[data-background-color=red] .nav .nav-item .nav-link{color:#fff}.sidebar[data-background-color=red] .nav .nav-item i{color:hsla(0,0%,100%,.8)}.sidebar[data-background-color=red] .nav .nav-item.active [data-toggle=collapse],.sidebar[data-background-color=red] .nav .nav-item:hover [data-toggle=collapse]{color:#fff}.sidebar[data-background-color=red] .nav .nav-item.active [data-toggle=collapse] i,.sidebar[data-background-color=red] .nav .nav-item:hover [data-toggle=collapse] i{color:hsla(0,0%,100%,.8)}.sidebar[data-background-color=red] .simple-text,.sidebar[data-background-color=red] .user a{color:#fff}.sidebar[data-background-color=red] .sidebar-background:after{background:#f44336;opacity:.8}.sidebar[data-background-color=red] .logo:after,.sidebar[data-background-color=red] .nav li.separator:after,.sidebar[data-background-color=red] .user:after{background-color:hsla(0,0%,100%,.3)}.sidebar[data-background-color=red] .nav li.active>[data-toggle=collapse],.sidebar[data-background-color=red] .nav li:hover:not(.active)>a{background-color:hsla(0,0%,100%,.1)}.sidebar[data-color=purple] li.active>a{background-color:#9c27b0;box-shadow:0 4px 20px 0 rgba(0,0,0,.14),0 7px 10px -5px rgba(156,39,176,.4)}.sidebar[data-color=azure] li.active>a{background-color:#00bcd4;box-shadow:0 4px 20px 0 rgba(0,0,0,.14),0 7px 10px -5px rgba(0,188,212,.4)}.sidebar[data-color=green] li.active>a{background-color:#4caf50;box-shadow:0 4px 20px 0 rgba(0,0,0,.14),0 7px 10px -5px rgba(76,175,80,.4)}.sidebar[data-color=orange] li.active>a{background-color:#ff9800;box-shadow:0 4px 20px 0 rgba(0,0,0,.14),0 7px 10px -5px rgba(255,152,0,.4)}.sidebar[data-color=danger] li.active>a{background-color:#f44336;box-shadow:0 4px 20px 0 rgba(0,0,0,.14),0 7px 10px -5px rgba(244,67,54,.4)}.sidebar[data-color=rose] li.active>a{background-color:#e91e63;box-shadow:0 4px 20px 0 rgba(0,0,0,.14),0 7px 10px -5px rgba(233,30,99,.4)}.sidebar[data-color=white] li.active>a{background-color:#fff;box-shadow:0 4px 20px 0 rgba(0,0,0,.14),0 7px 10px -5px hsla(0,0%,100%,.4)}.sidebar[data-color=white] .nav .nav-item.active>a:not([data-toggle=collapse]){color:#3c4858;opacity:1;box-shadow:0 4px 20px 0 rgba(0,0,0,.14),0 7px 10px -5px rgba(60,72,88,.4)}.sidebar[data-color=white] .nav .nav-item.active>a:not([data-toggle=collapse]) i{color:rgba(60,72,88,.8)}.sidebar.has-image:after,.sidebar[data-image]:after{opacity:.77}.main-panel{position:relative;float:right;width:calc(100% - 260px);transition:.33s,cubic-bezier(.685,.0473,.346,1)}.main-panel>.content{margin-top:70px;padding:30px 15px;min-height:calc(100vh - 123px)}.main-panel>.footer{border-top:1px solid #e7e7e7}.main-panel>.navbar{margin-bottom:0}.main-panel .header{margin-bottom:30px}.main-panel .header .title{margin-top:10px;margin-bottom:10px}.perfect-scrollbar-on .main-panel,.perfect-scrollbar-on .sidebar{height:100%;max-height:100%}.main-panel,.sidebar,.sidebar-wrapper{transition-property:top,bottom,width;transition-duration:.2s,.2s,.35s;transition-timing-function:linear,linear,ease;-webkit-overflow-scrolling:touch}.visible-on-sidebar-regular{display:inline-block!important}.visible-on-sidebar-mini{display:none!important}@media (min-width:991px){.sidebar-mini .visible-on-sidebar-regular{display:none!important}.sidebar-mini .visible-on-sidebar-mini{display:inline-block!important}.sidebar-mini .sidebar,.sidebar-mini .sidebar .sidebar-wrapper{width:80px}.sidebar-mini .main-panel{width:calc(100% - 80px)}.sidebar-mini .sidebar{display:block;font-weight:200;z-index:9999}.sidebar-mini .sidebar .logo a.logo-normal,.sidebar-mini .sidebar .sidebar-wrapper .user .user-info>a>span,.sidebar-mini .sidebar .sidebar-wrapper .user .user-info [data-toggle=collapse]~div>ul>li>a .sidebar-normal,.sidebar-mini .sidebar .sidebar-wrapper>.nav [data-toggle=collapse]~div>ul>li>a .sidebar-normal,.sidebar-mini .sidebar .sidebar-wrapper>.nav li>a p{opacity:0;transform:translate3d(-25px,0,0)}.sidebar-mini .sidebar:hover{width:260px}.sidebar-mini .sidebar:hover .logo a.logo-normal{opacity:1;transform:translateZ(0)}.sidebar-mini .sidebar:hover .sidebar-wrapper{width:260px}.sidebar-mini .sidebar:hover .sidebar-wrapper .user .user-info>a>span,.sidebar-mini .sidebar:hover .sidebar-wrapper .user .user-info [data-toggle=collapse]~div>ul>li>a .sidebar-normal,.sidebar-mini .sidebar:hover .sidebar-wrapper>.nav [data-toggle=collapse]~div>ul>li>a .sidebar-normal,.sidebar-mini .sidebar:hover .sidebar-wrapper>.nav li>a p{transform:translateZ(0);opacity:1}}.sidebar[data-background-color=black]{background:#191919}.fixed-plugin .dropdown .dropdown-menu{border-radius:10px}.fixed-plugin .dropdown .dropdown-menu li.adjustments-line{border-bottom:1px solid #ddd}.fixed-plugin .dropdown .dropdown-menu li{padding:5px 2px!important}.fixed-plugin .dropdown .dropdown-menu .adjustments-line .bootstrap-switch{position:absolute;right:10px!important}.fixed-plugin .dropdown .dropdown-menu .adjustments-line label{margin-bottom:.1rem!important}.fixed-plugin .btn{position:relative;padding:12px 30px;margin:.6rem 1px;font-size:.75rem;border-radius:.2rem;transition:box-shadow .2s cubic-bezier(.4,0,1,1),background-color .2s cubic-bezier(.4,0,.2,1);will-change:box-shadow,transform}.fixed-plugin .btn.btn-primary{color:#fff;background-color:#9c27b0;border-color:#9c27b0;box-shadow:0 2px 2px 0 rgba(156,39,176,.14),0 3px 1px -2px rgba(156,39,176,.2),0 1px 5px 0 rgba(156,39,176,.12)}.fixed-plugin .btn.btn-primary.focus,.fixed-plugin .btn.btn-primary:focus,.fixed-plugin .btn.btn-primary:hover{color:#fff;background-color:#9124a3;border-color:#701c7e}.fixed-plugin .btn.btn-primary.active,.fixed-plugin .btn.btn-primary:active,.open>.fixed-plugin .btn.btn-primary.dropdown-toggle,.show>.fixed-plugin .btn.btn-primary.dropdown-toggle{color:#fff;background-color:#9124a3;border-color:#701c7e;box-shadow:0 2px 2px 0 rgba(156,39,176,.14),0 3px 1px -2px rgba(156,39,176,.2),0 1px 5px 0 rgba(156,39,176,.12)}.fixed-plugin .btn.btn-primary.active.focus,.fixed-plugin .btn.btn-primary.active:focus,.fixed-plugin .btn.btn-primary.active:hover,.fixed-plugin .btn.btn-primary:active.focus,.fixed-plugin .btn.btn-primary:active:focus,.fixed-plugin .btn.btn-primary:active:hover,.open>.fixed-plugin .btn.btn-primary.dropdown-toggle.focus,.open>.fixed-plugin .btn.btn-primary.dropdown-toggle:focus,.open>.fixed-plugin .btn.btn-primary.dropdown-toggle:hover,.show>.fixed-plugin .btn.btn-primary.dropdown-toggle.focus,.show>.fixed-plugin .btn.btn-primary.dropdown-toggle:focus,.show>.fixed-plugin .btn.btn-primary.dropdown-toggle:hover{color:#fff;background-color:#9124a3;border-color:#3f1048}.open>.fixed-plugin .btn.btn-primary.dropdown-toggle.bmd-btn-icon{color:inherit;background-color:#9c27b0}.open>.fixed-plugin .btn.btn-primary.dropdown-toggle.bmd-btn-icon:hover{background-color:#9124a3}.fixed-plugin .btn.btn-primary.disabled.focus,.fixed-plugin .btn.btn-primary.disabled:focus,.fixed-plugin .btn.btn-primary.disabled:hover,.fixed-plugin .btn.btn-primary:disabled.focus,.fixed-plugin .btn.btn-primary:disabled:focus,.fixed-plugin .btn.btn-primary:disabled:hover{background-color:#9c27b0;border-color:#9c27b0}.fixed-plugin .btn.btn-primary:active,.fixed-plugin .btn.btn-primary:focus,.fixed-plugin .btn.btn-primary:hover{box-shadow:0 14px 26px -12px rgba(156,39,176,.42),0 4px 23px 0 rgba(0,0,0,.12),0 8px 10px -5px rgba(156,39,176,.2)}.fixed-plugin .btn.btn-primary.btn-link{box-shadow:none}.fixed-plugin .btn.btn-primary.btn-link,.fixed-plugin .btn.btn-primary.btn-link:active,.fixed-plugin .btn.btn-primary.btn-link:focus,.fixed-plugin .btn.btn-primary.btn-link:hover{background-color:transparent;color:#9c27b0}.fixed-plugin .btn.btn-secondary{color:#333;background-color:#fafafa;border-color:#ccc;box-shadow:0 2px 2px 0 hsla(0,0%,98%,.14),0 3px 1px -2px hsla(0,0%,98%,.2),0 1px 5px 0 hsla(0,0%,98%,.12)}.fixed-plugin .btn.btn-secondary.focus,.fixed-plugin .btn.btn-secondary:focus,.fixed-plugin .btn.btn-secondary:hover{color:#333;background-color:#f2f2f2;border-color:#adadad}.fixed-plugin .btn.btn-secondary.active,.fixed-plugin .btn.btn-secondary:active,.open>.fixed-plugin .btn.btn-secondary.dropdown-toggle,.show>.fixed-plugin .btn.btn-secondary.dropdown-toggle{color:#333;background-color:#f2f2f2;border-color:#adadad;box-shadow:0 2px 2px 0 hsla(0,0%,98%,.14),0 3px 1px -2px hsla(0,0%,98%,.2),0 1px 5px 0 hsla(0,0%,98%,.12)}.fixed-plugin .btn.btn-secondary.active.focus,.fixed-plugin .btn.btn-secondary.active:focus,.fixed-plugin .btn.btn-secondary.active:hover,.fixed-plugin .btn.btn-secondary:active.focus,.fixed-plugin .btn.btn-secondary:active:focus,.fixed-plugin .btn.btn-secondary:active:hover,.open>.fixed-plugin .btn.btn-secondary.dropdown-toggle.focus,.open>.fixed-plugin .btn.btn-secondary.dropdown-toggle:focus,.open>.fixed-plugin .btn.btn-secondary.dropdown-toggle:hover,.show>.fixed-plugin .btn.btn-secondary.dropdown-toggle.focus,.show>.fixed-plugin .btn.btn-secondary.dropdown-toggle:focus,.show>.fixed-plugin .btn.btn-secondary.dropdown-toggle:hover{color:#333;background-color:#f2f2f2;border-color:#8c8c8c}.open>.fixed-plugin .btn.btn-secondary.dropdown-toggle.bmd-btn-icon{color:inherit;background-color:#fafafa}.open>.fixed-plugin .btn.btn-secondary.dropdown-toggle.bmd-btn-icon:hover{background-color:#f2f2f2}.fixed-plugin .btn.btn-secondary.disabled.focus,.fixed-plugin .btn.btn-secondary.disabled:focus,.fixed-plugin .btn.btn-secondary.disabled:hover,.fixed-plugin .btn.btn-secondary:disabled.focus,.fixed-plugin .btn.btn-secondary:disabled:focus,.fixed-plugin .btn.btn-secondary:disabled:hover{background-color:#fafafa;border-color:#ccc}.fixed-plugin .btn.btn-secondary:active,.fixed-plugin .btn.btn-secondary:focus,.fixed-plugin .btn.btn-secondary:hover{box-shadow:0 14px 26px -12px hsla(0,0%,98%,.42),0 4px 23px 0 rgba(0,0,0,.12),0 8px 10px -5px hsla(0,0%,98%,.2)}.fixed-plugin .btn.btn-secondary.btn-link{box-shadow:none}.fixed-plugin .btn.btn-secondary.btn-link,.fixed-plugin .btn.btn-secondary.btn-link:active,.fixed-plugin .btn.btn-secondary.btn-link:focus,.fixed-plugin .btn.btn-secondary.btn-link:hover{background-color:transparent;color:#fafafa}.fixed-plugin .btn.btn-info{color:#fff;background-color:#00bcd4;border-color:#00bcd4;box-shadow:0 2px 2px 0 rgba(0,188,212,.14),0 3px 1px -2px rgba(0,188,212,.2),0 1px 5px 0 rgba(0,188,212,.12)}.fixed-plugin .btn.btn-info.focus,.fixed-plugin .btn.btn-info:focus,.fixed-plugin .btn.btn-info:hover{color:#fff;background-color:#00aec5;border-color:#008697}.fixed-plugin .btn.btn-info.active,.fixed-plugin .btn.btn-info:active,.open>.fixed-plugin .btn.btn-info.dropdown-toggle,.show>.fixed-plugin .btn.btn-info.dropdown-toggle{color:#fff;background-color:#00aec5;border-color:#008697;box-shadow:0 2px 2px 0 rgba(0,188,212,.14),0 3px 1px -2px rgba(0,188,212,.2),0 1px 5px 0 rgba(0,188,212,.12)}.fixed-plugin .btn.btn-info.active.focus,.fixed-plugin .btn.btn-info.active:focus,.fixed-plugin .btn.btn-info.active:hover,.fixed-plugin .btn.btn-info:active.focus,.fixed-plugin .btn.btn-info:active:focus,.fixed-plugin .btn.btn-info:active:hover,.open>.fixed-plugin .btn.btn-info.dropdown-toggle.focus,.open>.fixed-plugin .btn.btn-info.dropdown-toggle:focus,.open>.fixed-plugin .btn.btn-info.dropdown-toggle:hover,.show>.fixed-plugin .btn.btn-info.dropdown-toggle.focus,.show>.fixed-plugin .btn.btn-info.dropdown-toggle:focus,.show>.fixed-plugin .btn.btn-info.dropdown-toggle:hover{color:#fff;background-color:#00aec5;border-color:#004b55}.open>.fixed-plugin .btn.btn-info.dropdown-toggle.bmd-btn-icon{color:inherit;background-color:#00bcd4}.open>.fixed-plugin .btn.btn-info.dropdown-toggle.bmd-btn-icon:hover{background-color:#00aec5}.fixed-plugin .btn.btn-info.disabled.focus,.fixed-plugin .btn.btn-info.disabled:focus,.fixed-plugin .btn.btn-info.disabled:hover,.fixed-plugin .btn.btn-info:disabled.focus,.fixed-plugin .btn.btn-info:disabled:focus,.fixed-plugin .btn.btn-info:disabled:hover{background-color:#00bcd4;border-color:#00bcd4}.fixed-plugin .btn.btn-info:active,.fixed-plugin .btn.btn-info:focus,.fixed-plugin .btn.btn-info:hover{box-shadow:0 14px 26px -12px rgba(0,188,212,.42),0 4px 23px 0 rgba(0,0,0,.12),0 8px 10px -5px rgba(0,188,212,.2)}.fixed-plugin .btn.btn-info.btn-link{box-shadow:none}.fixed-plugin .btn.btn-info.btn-link,.fixed-plugin .btn.btn-info.btn-link:active,.fixed-plugin .btn.btn-info.btn-link:focus,.fixed-plugin .btn.btn-info.btn-link:hover{background-color:transparent;color:#00bcd4}.fixed-plugin .btn.btn-success{color:#fff;background-color:#4caf50;border-color:#4caf50;box-shadow:0 2px 2px 0 rgba(76,175,80,.14),0 3px 1px -2px rgba(76,175,80,.2),0 1px 5px 0 rgba(76,175,80,.12)}.fixed-plugin .btn.btn-success.focus,.fixed-plugin .btn.btn-success:focus,.fixed-plugin .btn.btn-success:hover{color:#fff;background-color:#47a44b;border-color:#39843c}.fixed-plugin .btn.btn-success.active,.fixed-plugin .btn.btn-success:active,.open>.fixed-plugin .btn.btn-success.dropdown-toggle,.show>.fixed-plugin .btn.btn-success.dropdown-toggle{color:#fff;background-color:#47a44b;border-color:#39843c;box-shadow:0 2px 2px 0 rgba(76,175,80,.14),0 3px 1px -2px rgba(76,175,80,.2),0 1px 5px 0 rgba(76,175,80,.12)}.fixed-plugin .btn.btn-success.active.focus,.fixed-plugin .btn.btn-success.active:focus,.fixed-plugin .btn.btn-success.active:hover,.fixed-plugin .btn.btn-success:active.focus,.fixed-plugin .btn.btn-success:active:focus,.fixed-plugin .btn.btn-success:active:hover,.open>.fixed-plugin .btn.btn-success.dropdown-toggle.focus,.open>.fixed-plugin .btn.btn-success.dropdown-toggle:focus,.open>.fixed-plugin .btn.btn-success.dropdown-toggle:hover,.show>.fixed-plugin .btn.btn-success.dropdown-toggle.focus,.show>.fixed-plugin .btn.btn-success.dropdown-toggle:focus,.show>.fixed-plugin .btn.btn-success.dropdown-toggle:hover{color:#fff;background-color:#47a44b;border-color:#255627}.open>.fixed-plugin .btn.btn-success.dropdown-toggle.bmd-btn-icon{color:inherit;background-color:#4caf50}.open>.fixed-plugin .btn.btn-success.dropdown-toggle.bmd-btn-icon:hover{background-color:#47a44b}.fixed-plugin .btn.btn-success.disabled.focus,.fixed-plugin .btn.btn-success.disabled:focus,.fixed-plugin .btn.btn-success.disabled:hover,.fixed-plugin .btn.btn-success:disabled.focus,.fixed-plugin .btn.btn-success:disabled:focus,.fixed-plugin .btn.btn-success:disabled:hover{background-color:#4caf50;border-color:#4caf50}.fixed-plugin .btn.btn-success:active,.fixed-plugin .btn.btn-success:focus,.fixed-plugin .btn.btn-success:hover{box-shadow:0 14px 26px -12px rgba(76,175,80,.42),0 4px 23px 0 rgba(0,0,0,.12),0 8px 10px -5px rgba(76,175,80,.2)}.fixed-plugin .btn.btn-success.btn-link{box-shadow:none}.fixed-plugin .btn.btn-success.btn-link,.fixed-plugin .btn.btn-success.btn-link:active,.fixed-plugin .btn.btn-success.btn-link:focus,.fixed-plugin .btn.btn-success.btn-link:hover{background-color:transparent;color:#4caf50}.fixed-plugin .btn.btn-warning{color:#fff;background-color:#ff9800;border-color:#ff9800;box-shadow:0 2px 2px 0 rgba(255,152,0,.14),0 3px 1px -2px rgba(255,152,0,.2),0 1px 5px 0 rgba(255,152,0,.12)}.fixed-plugin .btn.btn-warning.focus,.fixed-plugin .btn.btn-warning:focus,.fixed-plugin .btn.btn-warning:hover{color:#fff;background-color:#f08f00;border-color:#c27400}.fixed-plugin .btn.btn-warning.active,.fixed-plugin .btn.btn-warning:active,.open>.fixed-plugin .btn.btn-warning.dropdown-toggle,.show>.fixed-plugin .btn.btn-warning.dropdown-toggle{color:#fff;background-color:#f08f00;border-color:#c27400;box-shadow:0 2px 2px 0 rgba(255,152,0,.14),0 3px 1px -2px rgba(255,152,0,.2),0 1px 5px 0 rgba(255,152,0,.12)}.fixed-plugin .btn.btn-warning.active.focus,.fixed-plugin .btn.btn-warning.active:focus,.fixed-plugin .btn.btn-warning.active:hover,.fixed-plugin .btn.btn-warning:active.focus,.fixed-plugin .btn.btn-warning:active:focus,.fixed-plugin .btn.btn-warning:active:hover,.open>.fixed-plugin .btn.btn-warning.dropdown-toggle.focus,.open>.fixed-plugin .btn.btn-warning.dropdown-toggle:focus,.open>.fixed-plugin .btn.btn-warning.dropdown-toggle:hover,.show>.fixed-plugin .btn.btn-warning.dropdown-toggle.focus,.show>.fixed-plugin .btn.btn-warning.dropdown-toggle:focus,.show>.fixed-plugin .btn.btn-warning.dropdown-toggle:hover{color:#fff;background-color:#f08f00;border-color:#804c00}.open>.fixed-plugin .btn.btn-warning.dropdown-toggle.bmd-btn-icon{color:inherit;background-color:#ff9800}.open>.fixed-plugin .btn.btn-warning.dropdown-toggle.bmd-btn-icon:hover{background-color:#f08f00}.fixed-plugin .btn.btn-warning.disabled.focus,.fixed-plugin .btn.btn-warning.disabled:focus,.fixed-plugin .btn.btn-warning.disabled:hover,.fixed-plugin .btn.btn-warning:disabled.focus,.fixed-plugin .btn.btn-warning:disabled:focus,.fixed-plugin .btn.btn-warning:disabled:hover{background-color:#ff9800;border-color:#ff9800}.fixed-plugin .btn.btn-warning:active,.fixed-plugin .btn.btn-warning:focus,.fixed-plugin .btn.btn-warning:hover{box-shadow:0 14px 26px -12px rgba(255,152,0,.42),0 4px 23px 0 rgba(0,0,0,.12),0 8px 10px -5px rgba(255,152,0,.2)}.fixed-plugin .btn.btn-warning.btn-link{box-shadow:none}.fixed-plugin .btn.btn-warning.btn-link,.fixed-plugin .btn.btn-warning.btn-link:active,.fixed-plugin .btn.btn-warning.btn-link:focus,.fixed-plugin .btn.btn-warning.btn-link:hover{background-color:transparent;color:#ff9800}.fixed-plugin .btn.btn-danger{color:#fff;background-color:#f44336;border-color:#f44336;box-shadow:0 2px 2px 0 rgba(244,67,54,.14),0 3px 1px -2px rgba(244,67,54,.2),0 1px 5px 0 rgba(244,67,54,.12)}.fixed-plugin .btn.btn-danger.focus,.fixed-plugin .btn.btn-danger:focus,.fixed-plugin .btn.btn-danger:hover{color:#fff;background-color:#f33527;border-color:#e11b0c}.fixed-plugin .btn.btn-danger.active,.fixed-plugin .btn.btn-danger:active,.open>.fixed-plugin .btn.btn-danger.dropdown-toggle,.show>.fixed-plugin .btn.btn-danger.dropdown-toggle{color:#fff;background-color:#f33527;border-color:#e11b0c;box-shadow:0 2px 2px 0 rgba(244,67,54,.14),0 3px 1px -2px rgba(244,67,54,.2),0 1px 5px 0 rgba(244,67,54,.12)}.fixed-plugin .btn.btn-danger.active.focus,.fixed-plugin .btn.btn-danger.active:focus,.fixed-plugin .btn.btn-danger.active:hover,.fixed-plugin .btn.btn-danger:active.focus,.fixed-plugin .btn.btn-danger:active:focus,.fixed-plugin .btn.btn-danger:active:hover,.open>.fixed-plugin .btn.btn-danger.dropdown-toggle.focus,.open>.fixed-plugin .btn.btn-danger.dropdown-toggle:focus,.open>.fixed-plugin .btn.btn-danger.dropdown-toggle:hover,.show>.fixed-plugin .btn.btn-danger.dropdown-toggle.focus,.show>.fixed-plugin .btn.btn-danger.dropdown-toggle:focus,.show>.fixed-plugin .btn.btn-danger.dropdown-toggle:hover{color:#fff;background-color:#f33527;border-color:#a21309}.open>.fixed-plugin .btn.btn-danger.dropdown-toggle.bmd-btn-icon{color:inherit;background-color:#f44336}.open>.fixed-plugin .btn.btn-danger.dropdown-toggle.bmd-btn-icon:hover{background-color:#f33527}.fixed-plugin .btn.btn-danger.disabled.focus,.fixed-plugin .btn.btn-danger.disabled:focus,.fixed-plugin .btn.btn-danger.disabled:hover,.fixed-plugin .btn.btn-danger:disabled.focus,.fixed-plugin .btn.btn-danger:disabled:focus,.fixed-plugin .btn.btn-danger:disabled:hover{background-color:#f44336;border-color:#f44336}.fixed-plugin .btn.btn-danger:active,.fixed-plugin .btn.btn-danger:focus,.fixed-plugin .btn.btn-danger:hover{box-shadow:0 14px 26px -12px rgba(244,67,54,.42),0 4px 23px 0 rgba(0,0,0,.12),0 8px 10px -5px rgba(244,67,54,.2)}.fixed-plugin .btn.btn-danger.btn-link{box-shadow:none}.fixed-plugin .btn.btn-danger.btn-link,.fixed-plugin .btn.btn-danger.btn-link:active,.fixed-plugin .btn.btn-danger.btn-link:focus,.fixed-plugin .btn.btn-danger.btn-link:hover{background-color:transparent;color:#f44336}.fixed-plugin .btn.btn-rose{color:#fff;background-color:#e91e63;border-color:#e91e63;box-shadow:0 2px 2px 0 rgba(233,30,99,.14),0 3px 1px -2px rgba(233,30,99,.2),0 1px 5px 0 rgba(233,30,99,.12)}.fixed-plugin .btn.btn-rose.focus,.fixed-plugin .btn.btn-rose:focus,.fixed-plugin .btn.btn-rose:hover{color:#fff;background-color:#ea2c6d;border-color:#b8124a}.fixed-plugin .btn.btn-rose.active,.fixed-plugin .btn.btn-rose:active,.open>.fixed-plugin .btn.btn-rose.dropdown-toggle,.show>.fixed-plugin .btn.btn-rose.dropdown-toggle{color:#fff;background-color:#ea2c6d;border-color:#b8124a;box-shadow:0 2px 2px 0 rgba(233,30,99,.14),0 3px 1px -2px rgba(233,30,99,.2),0 1px 5px 0 rgba(233,30,99,.12)}.fixed-plugin .btn.btn-rose.active.focus,.fixed-plugin .btn.btn-rose.active:focus,.fixed-plugin .btn.btn-rose.active:hover,.fixed-plugin .btn.btn-rose:active.focus,.fixed-plugin .btn.btn-rose:active:focus,.fixed-plugin .btn.btn-rose:active:hover,.open>.fixed-plugin .btn.btn-rose.dropdown-toggle.focus,.open>.fixed-plugin .btn.btn-rose.dropdown-toggle:focus,.open>.fixed-plugin .btn.btn-rose.dropdown-toggle:hover,.show>.fixed-plugin .btn.btn-rose.dropdown-toggle.focus,.show>.fixed-plugin .btn.btn-rose.dropdown-toggle:focus,.show>.fixed-plugin .btn.btn-rose.dropdown-toggle:hover{color:#fff;background-color:#ea2c6d;border-color:#7b0c32}.open>.fixed-plugin .btn.btn-rose.dropdown-toggle.bmd-btn-icon{color:inherit;background-color:#e91e63}.open>.fixed-plugin .btn.btn-rose.dropdown-toggle.bmd-btn-icon:hover{background-color:#ea2c6d}.fixed-plugin .btn.btn-rose.disabled.focus,.fixed-plugin .btn.btn-rose.disabled:focus,.fixed-plugin .btn.btn-rose.disabled:hover,.fixed-plugin .btn.btn-rose:disabled.focus,.fixed-plugin .btn.btn-rose:disabled:focus,.fixed-plugin .btn.btn-rose:disabled:hover{background-color:#e91e63;border-color:#e91e63}.fixed-plugin .btn.btn-rose:active,.fixed-plugin .btn.btn-rose:focus,.fixed-plugin .btn.btn-rose:hover{box-shadow:0 14px 26px -12px rgba(233,30,99,.42),0 4px 23px 0 rgba(0,0,0,.12),0 8px 10px -5px rgba(233,30,99,.2)}.fixed-plugin .btn.btn-rose.btn-link{box-shadow:none}.fixed-plugin .btn.btn-rose.btn-link,.fixed-plugin .btn.btn-rose.btn-link:active,.fixed-plugin .btn.btn-rose.btn-link:focus,.fixed-plugin .btn.btn-rose.btn-link:hover{background-color:transparent;color:#e91e63}.fixed-plugin .btn,.fixed-plugin .btn.btn-default{color:#fff;background-color:#999;border-color:#999;box-shadow:0 2px 2px 0 hsla(0,0%,60%,.14),0 3px 1px -2px hsla(0,0%,60%,.2),0 1px 5px 0 hsla(0,0%,60%,.12)}.fixed-plugin .btn.btn-default.focus,.fixed-plugin .btn.btn-default:focus,.fixed-plugin .btn.btn-default:hover,.fixed-plugin .btn.focus,.fixed-plugin .btn:focus,.fixed-plugin .btn:hover{color:#fff;background-color:#919191;border-color:#7a7a7a}.fixed-plugin .btn.active,.fixed-plugin .btn.btn-default.active,.fixed-plugin .btn.btn-default:active,.fixed-plugin .btn:active,.open>.fixed-plugin .btn.btn-default.dropdown-toggle,.open>.fixed-plugin .btn.dropdown-toggle,.show>.fixed-plugin .btn.btn-default.dropdown-toggle,.show>.fixed-plugin .btn.dropdown-toggle{color:#fff;background-color:#919191;border-color:#7a7a7a;box-shadow:0 2px 2px 0 hsla(0,0%,60%,.14),0 3px 1px -2px hsla(0,0%,60%,.2),0 1px 5px 0 hsla(0,0%,60%,.12)}.fixed-plugin .btn.active.focus,.fixed-plugin .btn.active:focus,.fixed-plugin .btn.active:hover,.fixed-plugin .btn.btn-default.active.focus,.fixed-plugin .btn.btn-default.active:focus,.fixed-plugin .btn.btn-default.active:hover,.fixed-plugin .btn.btn-default:active.focus,.fixed-plugin .btn.btn-default:active:focus,.fixed-plugin .btn.btn-default:active:hover,.fixed-plugin .btn:active.focus,.fixed-plugin .btn:active:focus,.fixed-plugin .btn:active:hover,.open>.fixed-plugin .btn.btn-default.dropdown-toggle.focus,.open>.fixed-plugin .btn.btn-default.dropdown-toggle:focus,.open>.fixed-plugin .btn.btn-default.dropdown-toggle:hover,.open>.fixed-plugin .btn.dropdown-toggle.focus,.open>.fixed-plugin .btn.dropdown-toggle:focus,.open>.fixed-plugin .btn.dropdown-toggle:hover,.show>.fixed-plugin .btn.btn-default.dropdown-toggle.focus,.show>.fixed-plugin .btn.btn-default.dropdown-toggle:focus,.show>.fixed-plugin .btn.btn-default.dropdown-toggle:hover,.show>.fixed-plugin .btn.dropdown-toggle.focus,.show>.fixed-plugin .btn.dropdown-toggle:focus,.show>.fixed-plugin .btn.dropdown-toggle:hover{color:#fff;background-color:#919191;border-color:#595959}.open>.fixed-plugin .btn.btn-default.dropdown-toggle.bmd-btn-icon,.open>.fixed-plugin .btn.dropdown-toggle.bmd-btn-icon{color:inherit;background-color:#999}.open>.fixed-plugin .btn.btn-default.dropdown-toggle.bmd-btn-icon:hover,.open>.fixed-plugin .btn.dropdown-toggle.bmd-btn-icon:hover{background-color:#919191}.fixed-plugin .btn.btn-default.disabled.focus,.fixed-plugin .btn.btn-default.disabled:focus,.fixed-plugin .btn.btn-default.disabled:hover,.fixed-plugin .btn.btn-default:disabled.focus,.fixed-plugin .btn.btn-default:disabled:focus,.fixed-plugin .btn.btn-default:disabled:hover,.fixed-plugin .btn.disabled.focus,.fixed-plugin .btn.disabled:focus,.fixed-plugin .btn.disabled:hover,.fixed-plugin .btn:disabled.focus,.fixed-plugin .btn:disabled:focus,.fixed-plugin .btn:disabled:hover{background-color:#999;border-color:#999}.fixed-plugin .btn.btn-default:active,.fixed-plugin .btn.btn-default:focus,.fixed-plugin .btn.btn-default:hover,.fixed-plugin .btn:active,.fixed-plugin .btn:focus,.fixed-plugin .btn:hover{box-shadow:0 14px 26px -12px hsla(0,0%,60%,.42),0 4px 23px 0 rgba(0,0,0,.12),0 8px 10px -5px hsla(0,0%,60%,.2)}.fixed-plugin .btn.btn-default.btn-link,.fixed-plugin .btn.btn-link{background-color:transparent;color:#999;box-shadow:none}.fixed-plugin .btn.btn-default.btn-link:active,.fixed-plugin .btn.btn-default.btn-link:focus,.fixed-plugin .btn.btn-default.btn-link:hover,.fixed-plugin .btn.btn-link:active,.fixed-plugin .btn.btn-link:focus,.fixed-plugin .btn.btn-link:hover{background-color:transparent;color:#999}.fixed-plugin .btn.active.focus,.fixed-plugin .btn.active:focus,.fixed-plugin .btn.focus,.fixed-plugin .btn:active.focus,.fixed-plugin .btn:active:focus,.fixed-plugin .btn:focus{outline:0}.fixed-plugin .btn.btn-round{border-radius:30px}.fixed-plugin .button-container .btn:not(.btn-facebook):not(.btn-twitter){display:block}.fixed-plugin .button-container.github-star{margin-left:100px}.fixed-plugin .badge,.fixed-plugin li>a{transition:all .34s;-webkit-transition:all .34s;-moz-transition:all .34s}.fixed-plugin{position:fixed;top:115px;right:0;width:64px;background:rgba(0,0,0,.3);z-index:1031;border-radius:8px 0 0 8px;text-align:center}.fixed-plugin .fa-cog{color:#fff;padding:10px;border-radius:0 0 6px 6px;width:auto}.fixed-plugin .dropdown-menu{right:80px;left:auto;width:290px;border-radius:.1875rem;padding:0 10px}.fixed-plugin .dropdown-menu:after,.fixed-plugin .dropdown-menu:before{right:10px;margin-left:auto;left:auto}.fixed-plugin .fa-circle-thin{color:#fff}.fixed-plugin .active .fa-circle-thin{color:#0bf}.fixed-plugin .dropdown-menu>.active>a,.fixed-plugin .dropdown-menu>.active>a:focus,.fixed-plugin .dropdown-menu>.active>a:hover{color:#777;text-align:center}.fixed-plugin img{border-radius:0;width:100%;height:100px;margin:0 auto}.fixed-plugin .dropdown-menu li>a:focus,.fixed-plugin .dropdown-menu li>a:hover{box-shadow:none}.fixed-plugin .badge{border:3px solid #fff;border-radius:50%;cursor:pointer;display:inline-block;height:23px;margin-right:5px;position:relative;width:23px;padding:8px}.fixed-plugin .badge.active,.fixed-plugin .badge:hover{border-color:#0bf}.fixed-plugin .badge-black{background-color:#000}.fixed-plugin .badge-azure{background-color:#2ca8ff}.fixed-plugin .badge-green{background-color:#18ce0f}.fixed-plugin .badge-orange{background-color:#f96332}.fixed-plugin .badge-yellow{background-color:#ffb236}.fixed-plugin .badge-danger{background-color:#f44336}.fixed-plugin .badge-purple{background-color:#9368e9}.fixed-plugin .badge-white{background-color:hsla(0,0%,78%,.2)}.fixed-plugin .badge-rose{background-color:#e91e63}.fixed-plugin .badge-red{background-color:#f44336}.fixed-plugin h5{font-size:14px;margin:10px}.fixed-plugin .dropdown-menu li{display:block;padding:18px 2px;width:25%;float:left}.fixed-plugin li.adjustments-line,.fixed-plugin li.button-container,.fixed-plugin li.header-title{width:100%;height:50px;min-height:inherit}.fixed-plugin li.button-container{height:auto}.fixed-plugin li.button-container div{margin-bottom:5px}.fixed-plugin #sharrreTitle{text-align:center;padding:10px 0;height:50px}.fixed-plugin li.header-title{height:30px;line-height:25px;font-size:12px;font-weight:600;text-transform:uppercase;text-align:center}.fixed-plugin .adjustments-line p{float:left;display:inline-block;margin-bottom:0;font-size:1em;color:#3c4858;padding-top:0}.fixed-plugin .adjustments-line a .badge-colors{position:relative;top:-2px}.fixed-plugin .adjustments-line .togglebutton{padding-right:7px}.fixed-plugin .adjustments-line .togglebutton .toggle{margin-right:0}.fixed-plugin .dropdown-menu>li.adjustments-line>a{padding-right:0;padding-left:0;border-radius:0;margin:0}.fixed-plugin .dropdown-menu>li>a.img-holder{font-size:16px;text-align:center;border-radius:10px;background-color:#fff;border:3px solid #fff;padding-left:0;padding-right:0;opacity:1;cursor:pointer;display:block;max-height:100px;overflow:hidden;padding:0;min-width:25%}.fixed-plugin .dropdown-menu>li>a.switch-trigger:focus,.fixed-plugin .dropdown-menu>li>a.switch-trigger:hover{background-color:transparent}.fixed-plugin .dropdown-menu>li:focus>a.img-holder,.fixed-plugin .dropdown-menu>li:hover>a.img-holder{border-color:rgba(0,187,255,.53)}.fixed-plugin .dropdown-menu>.active>a.img-holder{border-color:#0bf;background-color:#fff}.fixed-plugin .dropdown-menu>li>a img{margin-top:auto}.fixed-plugin .btn-social{width:50%;display:block;width:48%;float:left;font-weight:600}.fixed-plugin .btn-social i{margin-right:5px}.fixed-plugin .btn-social:first-child{margin-right:2%}.fixed-plugin .adjustments-line a,.fixed-plugin .adjustments-line a:focus,.fixed-plugin .adjustments-line a:hover{color:transparent}.fixed-plugin .dropdown .dropdown-menu{top:-40px!important;opacity:0;left:-303px!important;transform-origin:100% 0}.fixed-plugin .dropdown.show .dropdown-menu{opacity:1;transform:scale(1)}.fixed-plugin .dropdown-menu:after,.fixed-plugin .dropdown-menu:before{content:"";display:inline-block;position:absolute;top:65px;width:16px;transform:translateY(-50%);-webkit-transform:translateY(-50%);-moz-transform:translateY(-50%)}.fixed-plugin .dropdown-menu:before{border-bottom:16px solid transparent;border-left:16px solid rgba(0,0,0,.2);border-top:16px solid transparent;right:-16px}.fixed-plugin .dropdown-menu:after{border-bottom:16px solid transparent;border-left:16px solid #fff;border-top:16px solid transparent;right:-15px}.wrapper-full-page~.fixed-plugin .dropdown.open .dropdown-menu{transform:translateY(-17%)}.wrapper-full-page~.fixed-plugin .dropdown .dropdown-menu{transform:translateY(-19%)}.wrapper:after{display:table;clear:both;content:" "}.wrapper.wrapper-full-page{height:auto;min-height:100vh}.login-page .footer .copyright,.login-page .footer a{color:#fff}.full-page:after,.full-page:before{display:block;content:"";position:absolute;width:100%;height:100%;top:0;left:0;z-index:2}.full-page:before{background-color:rgba(0,0,0,.5)}.full-page[filter-color=primary]:after,.full-page[filter-color=purple]:after{background:rgba(225,190,231,.56);background:linear-gradient(60deg,rgba(225,190,231,.56),rgba(186,104,200,.95))}.full-page[filter-color=primary].lock-page .form-group .form-control,.full-page[filter-color=purple].lock-page .form-group .form-control{background-image:linear-gradient(#9c27b0,#9c27b0),linear-gradient(#d2d2d2,#d2d2d2)}.full-page[filter-color=blue]:after,.full-page[filter-color=info]:after{background:rgba(178,235,242,.56);background:linear-gradient(60deg,rgba(178,235,242,.56),rgba(77,208,225,.95))}.full-page[filter-color=blue].lock-page .form-group .form-control,.full-page[filter-color=info].lock-page .form-group .form-control{background-image:linear-gradient(#00bcd4,#00bcd4),linear-gradient(#d2d2d2,#d2d2d2)}.full-page[filter-color=green]:after,.full-page[filter-color=success]:after{background:rgba(165,214,167,.56);background:linear-gradient(60deg,rgba(165,214,167,.56),rgba(102,187,106,.95))}.full-page[filter-color=green].lock-page .form-group .form-control,.full-page[filter-color=success].lock-page .form-group .form-control{background-image:linear-gradient(#4caf50,#4caf50),linear-gradient(#d2d2d2,#d2d2d2)}.full-page[filter-color=orange]:after,.full-page[filter-color=warning]:after{background:rgba(255,224,178,.56);background:linear-gradient(60deg,rgba(255,224,178,.56),rgba(255,183,77,.95))}.full-page[filter-color=orange].lock-page .form-group .form-control,.full-page[filter-color=warning].lock-page .form-group .form-control{background-image:linear-gradient(#ff9800,#ff9800),linear-gradient(#d2d2d2,#d2d2d2)}.full-page[filter-color=danger]:after,.full-page[filter-color=red]:after{background:hsla(0,73%,77%,.56);background:linear-gradient(60deg,hsla(0,73%,77%,.56),rgba(239,83,80,.95))}.full-page[filter-color=danger].lock-page .form-group .form-control,.full-page[filter-color=red].lock-page .form-group .form-control{background-image:linear-gradient(#f44336,#f44336),linear-gradient(#d2d2d2,#d2d2d2)}.full-page[filter-color=rose]:after{background:rgba(248,187,208,.56);background:linear-gradient(60deg,rgba(248,187,208,.56),rgba(240,98,146,.95))}.full-page[filter-color=rose].lock-page .form-group .form-control{background-image:linear-gradient(#e91e63,#e91e63),linear-gradient(#d2d2d2,#d2d2d2)}.full-page[data-image]:after{opacity:.8}.full-page>.content,.full-page>.footer{position:relative;z-index:4}.full-page>.content{min-height:calc(100vh - 80px)}.full-page .full-page-background{position:absolute;z-index:1;height:100%;width:100%;display:block;top:0;left:0;background-size:cover;background-position:50%}.full-page .footer,.full-page .footer .copyright a,.full-page .footer nav>ul a:not(.btn){color:#fff}.clear-filter:before{display:none}.lock-page>.content,.login-page>.content{padding-top:18vh}.login-page .card-login{transform:translateZ(0)}.login-page .card-login .card-header{margin-top:-40px}.login-page .card-login .card-body{padding:0 30px 0 10px}.login-page .card-login .card-body .input-group .input-group-text{padding:15px 15px 0}.login-page .card-login .card-body .input-group .form-control{padding-bottom:10px;margin:17px 0 0}.login-page .card-login .social-line .btn{margin-left:5px;margin-right:5px}.login-page .card-login.card-hidden{opacity:0;transform:translate3d(0,-60px,0)}.lock-page .card-profile{width:240px;margin:60px auto 0;color:#fff;left:0;right:0;display:block;transform:translateZ(0)}.lock-page .card-profile.card-hidden{opacity:0;transform:translate3d(0,-60px,0)}.lock-page .card-profile .card-avatar{max-width:90px;max-height:90px;margin-top:-45px}.lock-page .card-profile .card-footer{border:none;padding-top:0}.lock-page .card-profile .form-group{text-align:left;margin-top:15px}.lock-page .card-profile.with-animation{transition:.3s,ease-in}.lock-page .card-profile .card-body+.card-footer{padding:.9375rem 1.875rem;margin:0}.lock-page .footer{z-index:1;color:#fff}.lock-page .footer .copyright a{color:#fff}.lock-page .footer .copyright a:hover{color:#9c27b0}.register-page.page-header{background-position:top}.register-page .card-signup{border-radius:6px;box-shadow:0 16px 24px 2px rgba(0,0,0,.14),0 6px 30px 5px rgba(0,0,0,.12),0 8px 10px -5px rgba(0,0,0,.2);margin-bottom:100px;padding:40px 0;margin-top:15vh}.register-page .card-signup .info{max-width:360px;margin:0 auto;padding:0}.register-page .card-signup .info .info-title{color:#3c4858;margin:30px 0 15px}.register-page .card-signup .form-check{margin-top:20px;margin-bottom:0}.register-page .card-signup .form-check label{margin-left:27px}.register-page .card-signup .form-check .checkbox-material{padding-right:20px}.register-page .card-signup .form-check a{color:#9c27b0}.register-page .card-signup .info-horizontal .icon{float:left;margin-top:24px;margin-right:10px}.register-page .card-signup .info-horizontal .icon i{font-size:2.6em}.register-page .card-signup .info-horizontal .icon.icon-primary{color:#9c27b0}.register-page .card-signup .info-horizontal .icon.icon-info{color:#00bcd4}.register-page .card-signup .info-horizontal .icon.icon-success{color:#4caf50}.register-page .card-signup .info-horizontal .icon.icon-warning{color:#ff9800}.register-page .card-signup .info-horizontal .icon.icon-danger{color:#f44336}.register-page .card-signup .info-horizontal .icon.icon-rose{color:#e91e63}.register-page .card-signup .info-horizontal .description{overflow:hidden}.register-page .card-signup .form-group{margin:27px 0 0 7px;padding-bottom:0}.register-page .container{position:relative;z-index:3}.register-page .footer{color:#fff}.register-page .footer .container{padding:0}.register-page .footer .copyright a{color:#fff}.register-page .footer .copyright a:hover{color:#9c27b0}.register-page .form-check label{margin-left:27px}.register-page .form-check .form-check-label{padding-left:34px}.pricing-page{padding:120px 0}.pricing-page .title{color:#fff;margin-top:5vh}.pricing-page .section-space{display:block;height:70px}.pricing-page .card-plain .card-title,.pricing-page .card-plain .icon i,.pricing-page .description{color:#fff}.pricing-page.full-page:before{background-color:rgba(0,0,0,.65)}.pricing-page .footer{z-index:2;color:#fff}.pricing-page .footer .container{padding:0}.pricing-page .footer .copyright a{color:#fff}.pricing-page .footer .copyright a:hover{color:#9c27b0}.off-canvas-sidebar .navbar-toggler .navbar-toggler-icon{background-color:#fff!important}.off-canvas-sidebar .navbar-collapse .nav>li>a,.off-canvas-sidebar .navbar-collapse .nav>li>a:hover{color:#fff;margin:0 15px}.off-canvas-sidebar .navbar-collapse .nav>li>a:focus,.off-canvas-sidebar .navbar-collapse .nav>li>a:hover{background:hsla(0,0%,78%,.2)}.off-canvas-sidebar .navbar-collapse:after{background-color:#282828}.offline-doc .navbar .navbar-nav .nav-item .nav-link{color:#fff}@media screen and (max-width:991px){.off-canvas-sidebar .page-header>.container{padding-top:70px;padding-bottom:200px}.navbar .navbar-collapse .navbar-nav{display:-ms-flexbox;display:flex;-ms-flex-direction:column;flex-direction:column;padding-left:0;margin-bottom:0;list-style:none}}.social-line{padding:.9375rem 0}.timeline{list-style:none;padding:20px 0;position:relative;margin-top:30px}.timeline:before{top:50px;bottom:0;position:absolute;content:" ";width:3px;background-color:#e5e5e5;left:50%;margin-left:-1px}.timeline h6{color:#333;font-weight:400;margin:10px 0 0}.timeline.timeline-simple{margin-top:30px;padding:0 0 20px}.timeline.timeline-simple:before{left:5%;background-color:#e5e5e5}.timeline.timeline-simple>li>.timeline-panel{width:86%}.timeline.timeline-simple>li>.timeline-badge{left:5%}.timeline>li{margin-bottom:20px;position:relative}.timeline>li:after,.timeline>li:before{content:" ";display:table}.timeline>li:after{clear:both}.timeline>li>.timeline-panel{width:45%;float:left;padding:20px;margin-bottom:20px;position:relative;box-shadow:0 1px 4px 0 rgba(0,0,0,.14);border-radius:6px;color:rgba(0,0,0,.87);background:#fff}.timeline>li>.timeline-panel:before{position:absolute;top:26px;right:-15px;display:inline-block;border-top:15px solid transparent;border-left:15px solid #e4e4e4;border-right:0 solid #e4e4e4;border-bottom:15px solid transparent;content:" "}.timeline>li>.timeline-panel:after{position:absolute;top:27px;right:-14px;display:inline-block;border-top:14px solid transparent;border-left:14px solid #fff;border-right:0 solid #fff;border-bottom:14px solid transparent;content:" "}.timeline>li>.timeline-badge{color:#fff;width:50px;height:50px;line-height:51px;font-size:1.4em;text-align:center;position:absolute;top:16px;left:50%;margin-left:-24px;z-index:100;border-top-right-radius:50%;border-top-left-radius:50%;border-bottom-right-radius:50%;border-bottom-left-radius:50%}.timeline>li>.timeline-badge.primary{background-color:#9c27b0;box-shadow:0 4px 20px 0 rgba(0,0,0,.14),0 7px 10px -5px rgba(156,39,176,.4)}.timeline>li>.timeline-badge.success{background-color:#4caf50;box-shadow:0 4px 20px 0 rgba(0,0,0,.14),0 7px 10px -5px rgba(76,175,80,.4)}.timeline>li>.timeline-badge.warning{background-color:#ff9800;box-shadow:0 4px 20px 0 rgba(0,0,0,.14),0 7px 10px -5px rgba(255,152,0,.4)}.timeline>li>.timeline-badge.info{background-color:#00bcd4;box-shadow:0 4px 20px 0 rgba(0,0,0,.14),0 7px 10px -5px rgba(0,188,212,.4);padding:0}.timeline>li>.timeline-badge.danger{background-color:#f44336;box-shadow:0 4px 20px 0 rgba(0,0,0,.14),0 7px 10px -5px rgba(244,67,54,.4)}.timeline>li>.timeline-badge [class*=" ti-"],.timeline>li>.timeline-badge [class=material-icons],.timeline>li>.timeline-badge [class^=ti-]{line-height:inherit}.timeline>li.timeline-inverted>.timeline-panel{float:right;background-color:#fff}.timeline>li.timeline-inverted>.timeline-panel:before{border-left-width:0;border-right-width:15px;left:-15px;right:auto}.timeline>li.timeline-inverted>.timeline-panel:after{border-left-width:0;border-right-width:14px;left:-14px;right:auto}.timeline-heading{margin-bottom:15px}.timeline-title{margin-top:0;color:inherit}.timeline-body hr{margin-top:10px;margin-bottom:5px}.timeline-body .btn,.timeline-body>p,.timeline-body>ul{margin-bottom:0}.timeline-body>p+p{margin-top:5px}[class*=col-].cards{float:left}.btn.btn-facebook{color:#fff;background-color:#3b5998;border-color:#3b5998;box-shadow:0 2px 2px 0 rgba(59,89,152,.14),0 3px 1px -2px rgba(59,89,152,.2),0 1px 5px 0 rgba(59,89,152,.12)}.btn.btn-facebook.focus,.btn.btn-facebook:focus,.btn.btn-facebook:hover{color:#fff;background-color:#37538d;border-color:#2a3f6c}.btn.btn-facebook.active,.btn.btn-facebook:active,.open>.btn.btn-facebook.dropdown-toggle,.show>.btn.btn-facebook.dropdown-toggle{color:#fff;background-color:#37538d;border-color:#2a3f6c;box-shadow:0 2px 2px 0 rgba(59,89,152,.14),0 3px 1px -2px rgba(59,89,152,.2),0 1px 5px 0 rgba(59,89,152,.12)}.btn.btn-facebook.active.focus,.btn.btn-facebook.active:focus,.btn.btn-facebook.active:hover,.btn.btn-facebook:active.focus,.btn.btn-facebook:active:focus,.btn.btn-facebook:active:hover,.open>.btn.btn-facebook.dropdown-toggle.focus,.open>.btn.btn-facebook.dropdown-toggle:focus,.open>.btn.btn-facebook.dropdown-toggle:hover,.show>.btn.btn-facebook.dropdown-toggle.focus,.show>.btn.btn-facebook.dropdown-toggle:focus,.show>.btn.btn-facebook.dropdown-toggle:hover{color:#fff;background-color:#37538d;border-color:#17233c}.open>.btn.btn-facebook.dropdown-toggle.bmd-btn-icon{color:inherit;background-color:#3b5998}.open>.btn.btn-facebook.dropdown-toggle.bmd-btn-icon:hover{background-color:#37538d}.btn.btn-facebook.disabled.focus,.btn.btn-facebook.disabled:focus,.btn.btn-facebook.disabled:hover,.btn.btn-facebook:disabled.focus,.btn.btn-facebook:disabled:focus,.btn.btn-facebook:disabled:hover{background-color:#3b5998;border-color:#3b5998}.btn.btn-facebook:active,.btn.btn-facebook:focus,.btn.btn-facebook:hover{box-shadow:0 14px 26px -12px rgba(59,89,152,.42),0 4px 23px 0 rgba(0,0,0,.12),0 8px 10px -5px rgba(59,89,152,.2)}.btn.btn-facebook.btn-link{box-shadow:none}.btn.btn-facebook.btn-link,.btn.btn-facebook.btn-link:active,.btn.btn-facebook.btn-link:focus,.btn.btn-facebook.btn-link:hover{background-color:transparent;color:#3b5998}.btn.btn-twitter{color:#fff;background-color:#55acee;border-color:#55acee;box-shadow:0 2px 2px 0 rgba(85,172,238,.14),0 3px 1px -2px rgba(85,172,238,.2),0 1px 5px 0 rgba(85,172,238,.12)}.btn.btn-twitter.focus,.btn.btn-twitter:focus,.btn.btn-twitter:hover{color:#fff;background-color:#47a5ed;border-color:#1d91e8}.btn.btn-twitter.active,.btn.btn-twitter:active,.open>.btn.btn-twitter.dropdown-toggle,.show>.btn.btn-twitter.dropdown-toggle{color:#fff;background-color:#47a5ed;border-color:#1d91e8;box-shadow:0 2px 2px 0 rgba(85,172,238,.14),0 3px 1px -2px rgba(85,172,238,.2),0 1px 5px 0 rgba(85,172,238,.12)}.btn.btn-twitter.active.focus,.btn.btn-twitter.active:focus,.btn.btn-twitter.active:hover,.btn.btn-twitter:active.focus,.btn.btn-twitter:active:focus,.btn.btn-twitter:active:hover,.open>.btn.btn-twitter.dropdown-toggle.focus,.open>.btn.btn-twitter.dropdown-toggle:focus,.open>.btn.btn-twitter.dropdown-toggle:hover,.show>.btn.btn-twitter.dropdown-toggle.focus,.show>.btn.btn-twitter.dropdown-toggle:focus,.show>.btn.btn-twitter.dropdown-toggle:hover{color:#fff;background-color:#47a5ed;border-color:#126db2}.open>.btn.btn-twitter.dropdown-toggle.bmd-btn-icon{color:inherit;background-color:#55acee}.open>.btn.btn-twitter.dropdown-toggle.bmd-btn-icon:hover{background-color:#47a5ed}.btn.btn-twitter.disabled.focus,.btn.btn-twitter.disabled:focus,.btn.btn-twitter.disabled:hover,.btn.btn-twitter:disabled.focus,.btn.btn-twitter:disabled:focus,.btn.btn-twitter:disabled:hover{background-color:#55acee;border-color:#55acee}.btn.btn-twitter:active,.btn.btn-twitter:focus,.btn.btn-twitter:hover{box-shadow:0 14px 26px -12px rgba(85,172,238,.42),0 4px 23px 0 rgba(0,0,0,.12),0 8px 10px -5px rgba(85,172,238,.2)}.btn.btn-twitter.btn-link{box-shadow:none}.btn.btn-twitter.btn-link,.btn.btn-twitter.btn-link:active,.btn.btn-twitter.btn-link:focus,.btn.btn-twitter.btn-link:hover{background-color:transparent;color:#55acee}.btn.btn-pinterest{color:#fff;background-color:#cc2127;border-color:#cc2127;box-shadow:0 2px 2px 0 rgba(204,33,39,.14),0 3px 1px -2px rgba(204,33,39,.2),0 1px 5px 0 rgba(204,33,39,.12)}.btn.btn-pinterest.focus,.btn.btn-pinterest:focus,.btn.btn-pinterest:hover{color:#fff;background-color:#bf1f24;border-color:#97181d}.btn.btn-pinterest.active,.btn.btn-pinterest:active,.open>.btn.btn-pinterest.dropdown-toggle,.show>.btn.btn-pinterest.dropdown-toggle{color:#fff;background-color:#bf1f24;border-color:#97181d;box-shadow:0 2px 2px 0 rgba(204,33,39,.14),0 3px 1px -2px rgba(204,33,39,.2),0 1px 5px 0 rgba(204,33,39,.12)}.btn.btn-pinterest.active.focus,.btn.btn-pinterest.active:focus,.btn.btn-pinterest.active:hover,.btn.btn-pinterest:active.focus,.btn.btn-pinterest:active:focus,.btn.btn-pinterest:active:hover,.open>.btn.btn-pinterest.dropdown-toggle.focus,.open>.btn.btn-pinterest.dropdown-toggle:focus,.open>.btn.btn-pinterest.dropdown-toggle:hover,.show>.btn.btn-pinterest.dropdown-toggle.focus,.show>.btn.btn-pinterest.dropdown-toggle:focus,.show>.btn.btn-pinterest.dropdown-toggle:hover{color:#fff;background-color:#bf1f24;border-color:#5e0f12}.open>.btn.btn-pinterest.dropdown-toggle.bmd-btn-icon{color:inherit;background-color:#cc2127}.open>.btn.btn-pinterest.dropdown-toggle.bmd-btn-icon:hover{background-color:#bf1f24}.btn.btn-pinterest.disabled.focus,.btn.btn-pinterest.disabled:focus,.btn.btn-pinterest.disabled:hover,.btn.btn-pinterest:disabled.focus,.btn.btn-pinterest:disabled:focus,.btn.btn-pinterest:disabled:hover{background-color:#cc2127;border-color:#cc2127}.btn.btn-pinterest:active,.btn.btn-pinterest:focus,.btn.btn-pinterest:hover{box-shadow:0 14px 26px -12px rgba(204,33,39,.42),0 4px 23px 0 rgba(0,0,0,.12),0 8px 10px -5px rgba(204,33,39,.2)}.btn.btn-pinterest.btn-link{box-shadow:none}.btn.btn-pinterest.btn-link,.btn.btn-pinterest.btn-link:active,.btn.btn-pinterest.btn-link:focus,.btn.btn-pinterest.btn-link:hover{background-color:transparent;color:#cc2127}.btn.btn-google{color:#fff;background-color:#dd4b39;border-color:#dd4b39;box-shadow:0 2px 2px 0 rgba(221,75,57,.14),0 3px 1px -2px rgba(221,75,57,.2),0 1px 5px 0 rgba(221,75,57,.12)}.btn.btn-google.focus,.btn.btn-google:focus,.btn.btn-google:hover{color:#fff;background-color:#df5746;border-color:#b93120}.btn.btn-google.active,.btn.btn-google:active,.open>.btn.btn-google.dropdown-toggle,.show>.btn.btn-google.dropdown-toggle{color:#fff;background-color:#df5746;border-color:#b93120;box-shadow:0 2px 2px 0 rgba(221,75,57,.14),0 3px 1px -2px rgba(221,75,57,.2),0 1px 5px 0 rgba(221,75,57,.12)}.btn.btn-google.active.focus,.btn.btn-google.active:focus,.btn.btn-google.active:hover,.btn.btn-google:active.focus,.btn.btn-google:active:focus,.btn.btn-google:active:hover,.open>.btn.btn-google.dropdown-toggle.focus,.open>.btn.btn-google.dropdown-toggle:focus,.open>.btn.btn-google.dropdown-toggle:hover,.show>.btn.btn-google.dropdown-toggle.focus,.show>.btn.btn-google.dropdown-toggle:focus,.show>.btn.btn-google.dropdown-toggle:hover{color:#fff;background-color:#df5746;border-color:#802216}.open>.btn.btn-google.dropdown-toggle.bmd-btn-icon{color:inherit;background-color:#dd4b39}.open>.btn.btn-google.dropdown-toggle.bmd-btn-icon:hover{background-color:#df5746}.btn.btn-google.disabled.focus,.btn.btn-google.disabled:focus,.btn.btn-google.disabled:hover,.btn.btn-google:disabled.focus,.btn.btn-google:disabled:focus,.btn.btn-google:disabled:hover{background-color:#dd4b39;border-color:#dd4b39}.btn.btn-google:active,.btn.btn-google:focus,.btn.btn-google:hover{box-shadow:0 14px 26px -12px rgba(221,75,57,.42),0 4px 23px 0 rgba(0,0,0,.12),0 8px 10px -5px rgba(221,75,57,.2)}.btn.btn-google.btn-link{box-shadow:none}.btn.btn-google.btn-link,.btn.btn-google.btn-link:active,.btn.btn-google.btn-link:focus,.btn.btn-google.btn-link:hover{background-color:transparent;color:#dd4b39}.btn.btn-linkedin{color:#fff;background-color:#0976b4;border-color:#0976b4;box-shadow:0 2px 2px 0 rgba(9,118,180,.14),0 3px 1px -2px rgba(9,118,180,.2),0 1px 5px 0 rgba(9,118,180,.12)}.btn.btn-linkedin.focus,.btn.btn-linkedin:focus,.btn.btn-linkedin:hover{color:#fff;background-color:#086ca5;border-color:#06507a}.btn.btn-linkedin.active,.btn.btn-linkedin:active,.open>.btn.btn-linkedin.dropdown-toggle,.show>.btn.btn-linkedin.dropdown-toggle{color:#fff;background-color:#086ca5;border-color:#06507a;box-shadow:0 2px 2px 0 rgba(9,118,180,.14),0 3px 1px -2px rgba(9,118,180,.2),0 1px 5px 0 rgba(9,118,180,.12)}.btn.btn-linkedin.active.focus,.btn.btn-linkedin.active:focus,.btn.btn-linkedin.active:hover,.btn.btn-linkedin:active.focus,.btn.btn-linkedin:active:focus,.btn.btn-linkedin:active:hover,.open>.btn.btn-linkedin.dropdown-toggle.focus,.open>.btn.btn-linkedin.dropdown-toggle:focus,.open>.btn.btn-linkedin.dropdown-toggle:hover,.show>.btn.btn-linkedin.dropdown-toggle.focus,.show>.btn.btn-linkedin.dropdown-toggle:focus,.show>.btn.btn-linkedin.dropdown-toggle:hover{color:#fff;background-color:#086ca5;border-color:#03263b}.open>.btn.btn-linkedin.dropdown-toggle.bmd-btn-icon{color:inherit;background-color:#0976b4}.open>.btn.btn-linkedin.dropdown-toggle.bmd-btn-icon:hover{background-color:#086ca5}.btn.btn-linkedin.disabled.focus,.btn.btn-linkedin.disabled:focus,.btn.btn-linkedin.disabled:hover,.btn.btn-linkedin:disabled.focus,.btn.btn-linkedin:disabled:focus,.btn.btn-linkedin:disabled:hover{background-color:#0976b4;border-color:#0976b4}.btn.btn-linkedin:active,.btn.btn-linkedin:focus,.btn.btn-linkedin:hover{box-shadow:0 14px 26px -12px rgba(9,118,180,.42),0 4px 23px 0 rgba(0,0,0,.12),0 8px 10px -5px rgba(9,118,180,.2)}.btn.btn-linkedin.btn-link{box-shadow:none}.btn.btn-linkedin.btn-link,.btn.btn-linkedin.btn-link:active,.btn.btn-linkedin.btn-link:focus,.btn.btn-linkedin.btn-link:hover{background-color:transparent;color:#0976b4}.btn.btn-dribbble{color:#fff;background-color:#ea4c89;border-color:#ea4c89;box-shadow:0 2px 2px 0 rgba(234,76,137,.14),0 3px 1px -2px rgba(234,76,137,.2),0 1px 5px 0 rgba(234,76,137,.12)}.btn.btn-dribbble.focus,.btn.btn-dribbble:focus,.btn.btn-dribbble:hover{color:#fff;background-color:#e83e80;border-color:#df1a66}.btn.btn-dribbble.active,.btn.btn-dribbble:active,.open>.btn.btn-dribbble.dropdown-toggle,.show>.btn.btn-dribbble.dropdown-toggle{color:#fff;background-color:#e83e80;border-color:#df1a66;box-shadow:0 2px 2px 0 rgba(234,76,137,.14),0 3px 1px -2px rgba(234,76,137,.2),0 1px 5px 0 rgba(234,76,137,.12)}.btn.btn-dribbble.active.focus,.btn.btn-dribbble.active:focus,.btn.btn-dribbble.active:hover,.btn.btn-dribbble:active.focus,.btn.btn-dribbble:active:focus,.btn.btn-dribbble:active:hover,.open>.btn.btn-dribbble.dropdown-toggle.focus,.open>.btn.btn-dribbble.dropdown-toggle:focus,.open>.btn.btn-dribbble.dropdown-toggle:hover,.show>.btn.btn-dribbble.dropdown-toggle.focus,.show>.btn.btn-dribbble.dropdown-toggle:focus,.show>.btn.btn-dribbble.dropdown-toggle:hover{color:#fff;background-color:#e83e80;border-color:#a3134b}.open>.btn.btn-dribbble.dropdown-toggle.bmd-btn-icon{color:inherit;background-color:#ea4c89}.open>.btn.btn-dribbble.dropdown-toggle.bmd-btn-icon:hover{background-color:#e83e80}.btn.btn-dribbble.disabled.focus,.btn.btn-dribbble.disabled:focus,.btn.btn-dribbble.disabled:hover,.btn.btn-dribbble:disabled.focus,.btn.btn-dribbble:disabled:focus,.btn.btn-dribbble:disabled:hover{background-color:#ea4c89;border-color:#ea4c89}.btn.btn-dribbble:active,.btn.btn-dribbble:focus,.btn.btn-dribbble:hover{box-shadow:0 14px 26px -12px rgba(234,76,137,.42),0 4px 23px 0 rgba(0,0,0,.12),0 8px 10px -5px rgba(234,76,137,.2)}.btn.btn-dribbble.btn-link{box-shadow:none}.btn.btn-dribbble.btn-link,.btn.btn-dribbble.btn-link:active,.btn.btn-dribbble.btn-link:focus,.btn.btn-dribbble.btn-link:hover{background-color:transparent;color:#ea4c89}.btn.btn-github{color:#fff;background-color:#333;border-color:#333;box-shadow:0 2px 2px 0 rgba(51,51,51,.14),0 3px 1px -2px rgba(51,51,51,.2),0 1px 5px 0 rgba(51,51,51,.12)}.btn.btn-github.focus,.btn.btn-github:focus,.btn.btn-github:hover{color:#fff;background-color:#2b2b2b;border-color:#141414}.btn.btn-github.active,.btn.btn-github:active,.open>.btn.btn-github.dropdown-toggle,.show>.btn.btn-github.dropdown-toggle{color:#fff;background-color:#2b2b2b;border-color:#141414;box-shadow:0 2px 2px 0 rgba(51,51,51,.14),0 3px 1px -2px rgba(51,51,51,.2),0 1px 5px 0 rgba(51,51,51,.12)}.btn.btn-github.active.focus,.btn.btn-github.active:focus,.btn.btn-github.active:hover,.btn.btn-github:active.focus,.btn.btn-github:active:focus,.btn.btn-github:active:hover,.open>.btn.btn-github.dropdown-toggle.focus,.open>.btn.btn-github.dropdown-toggle:focus,.open>.btn.btn-github.dropdown-toggle:hover,.show>.btn.btn-github.dropdown-toggle.focus,.show>.btn.btn-github.dropdown-toggle:focus,.show>.btn.btn-github.dropdown-toggle:hover{color:#fff;background-color:#2b2b2b;border-color:#000}.open>.btn.btn-github.dropdown-toggle.bmd-btn-icon{color:inherit;background-color:#333}.open>.btn.btn-github.dropdown-toggle.bmd-btn-icon:hover{background-color:#2b2b2b}.btn.btn-github.disabled.focus,.btn.btn-github.disabled:focus,.btn.btn-github.disabled:hover,.btn.btn-github:disabled.focus,.btn.btn-github:disabled:focus,.btn.btn-github:disabled:hover{background-color:#333;border-color:#333}.btn.btn-github:active,.btn.btn-github:focus,.btn.btn-github:hover{box-shadow:0 14px 26px -12px rgba(51,51,51,.42),0 4px 23px 0 rgba(0,0,0,.12),0 8px 10px -5px rgba(51,51,51,.2)}.btn.btn-github.btn-link{box-shadow:none}.btn.btn-github.btn-link,.btn.btn-github.btn-link:active,.btn.btn-github.btn-link:focus,.btn.btn-github.btn-link:hover{background-color:transparent;color:#333}.btn.btn-youtube{color:#fff;background-color:#e52d27;border-color:#e52d27;box-shadow:0 2px 2px 0 rgba(229,45,39,.14),0 3px 1px -2px rgba(229,45,39,.2),0 1px 5px 0 rgba(229,45,39,.12)}.btn.btn-youtube.focus,.btn.btn-youtube:focus,.btn.btn-youtube:hover{color:#fff;background-color:#e73a35;border-color:#b91b16}.btn.btn-youtube.active,.btn.btn-youtube:active,.open>.btn.btn-youtube.dropdown-toggle,.show>.btn.btn-youtube.dropdown-toggle{color:#fff;background-color:#e73a35;border-color:#b91b16;box-shadow:0 2px 2px 0 rgba(229,45,39,.14),0 3px 1px -2px rgba(229,45,39,.2),0 1px 5px 0 rgba(229,45,39,.12)}.btn.btn-youtube.active.focus,.btn.btn-youtube.active:focus,.btn.btn-youtube.active:hover,.btn.btn-youtube:active.focus,.btn.btn-youtube:active:focus,.btn.btn-youtube:active:hover,.open>.btn.btn-youtube.dropdown-toggle.focus,.open>.btn.btn-youtube.dropdown-toggle:focus,.open>.btn.btn-youtube.dropdown-toggle:hover,.show>.btn.btn-youtube.dropdown-toggle.focus,.show>.btn.btn-youtube.dropdown-toggle:focus,.show>.btn.btn-youtube.dropdown-toggle:hover{color:#fff;background-color:#e73a35;border-color:#7d130f}.open>.btn.btn-youtube.dropdown-toggle.bmd-btn-icon{color:inherit;background-color:#e52d27}.open>.btn.btn-youtube.dropdown-toggle.bmd-btn-icon:hover{background-color:#e73a35}.btn.btn-youtube.disabled.focus,.btn.btn-youtube.disabled:focus,.btn.btn-youtube.disabled:hover,.btn.btn-youtube:disabled.focus,.btn.btn-youtube:disabled:focus,.btn.btn-youtube:disabled:hover{background-color:#e52d27;border-color:#e52d27}.btn.btn-youtube:active,.btn.btn-youtube:focus,.btn.btn-youtube:hover{box-shadow:0 14px 26px -12px rgba(229,45,39,.42),0 4px 23px 0 rgba(0,0,0,.12),0 8px 10px -5px rgba(229,45,39,.2)}.btn.btn-youtube.btn-link{box-shadow:none}.btn.btn-youtube.btn-link,.btn.btn-youtube.btn-link:active,.btn.btn-youtube.btn-link:focus,.btn.btn-youtube.btn-link:hover{background-color:transparent;color:#e52d27}.btn.btn-instagram{color:#fff;background-color:#125688;border-color:#125688;box-shadow:0 2px 2px 0 rgba(18,86,136,.14),0 3px 1px -2px rgba(18,86,136,.2),0 1px 5px 0 rgba(18,86,136,.12)}.btn.btn-instagram.focus,.btn.btn-instagram:focus,.btn.btn-instagram:hover{color:#fff;background-color:#145f96;border-color:#0b3452}.btn.btn-instagram.active,.btn.btn-instagram:active,.open>.btn.btn-instagram.dropdown-toggle,.show>.btn.btn-instagram.dropdown-toggle{color:#fff;background-color:#145f96;border-color:#0b3452;box-shadow:0 2px 2px 0 rgba(18,86,136,.14),0 3px 1px -2px rgba(18,86,136,.2),0 1px 5px 0 rgba(18,86,136,.12)}.btn.btn-instagram.active.focus,.btn.btn-instagram.active:focus,.btn.btn-instagram.active:hover,.btn.btn-instagram:active.focus,.btn.btn-instagram:active:focus,.btn.btn-instagram:active:hover,.open>.btn.btn-instagram.dropdown-toggle.focus,.open>.btn.btn-instagram.dropdown-toggle:focus,.open>.btn.btn-instagram.dropdown-toggle:hover,.show>.btn.btn-instagram.dropdown-toggle.focus,.show>.btn.btn-instagram.dropdown-toggle:focus,.show>.btn.btn-instagram.dropdown-toggle:hover{color:#fff;background-color:#145f96;border-color:#030f17}.open>.btn.btn-instagram.dropdown-toggle.bmd-btn-icon{color:inherit;background-color:#125688}.open>.btn.btn-instagram.dropdown-toggle.bmd-btn-icon:hover{background-color:#145f96}.btn.btn-instagram.disabled.focus,.btn.btn-instagram.disabled:focus,.btn.btn-instagram.disabled:hover,.btn.btn-instagram:disabled.focus,.btn.btn-instagram:disabled:focus,.btn.btn-instagram:disabled:hover{background-color:#125688;border-color:#125688}.btn.btn-instagram:active,.btn.btn-instagram:focus,.btn.btn-instagram:hover{box-shadow:0 14px 26px -12px rgba(18,86,136,.42),0 4px 23px 0 rgba(0,0,0,.12),0 8px 10px -5px rgba(18,86,136,.2)}.btn.btn-instagram.btn-link{box-shadow:none}.btn.btn-instagram.btn-link,.btn.btn-instagram.btn-link:active,.btn.btn-instagram.btn-link:focus,.btn.btn-instagram.btn-link:hover{background-color:transparent;color:#125688}.btn.btn-reddit{color:#fff;background-color:#ff4500;border-color:#ff4500;box-shadow:0 2px 2px 0 rgba(255,69,0,.14),0 3px 1px -2px rgba(255,69,0,.2),0 1px 5px 0 rgba(255,69,0,.12)}.btn.btn-reddit.focus,.btn.btn-reddit:focus,.btn.btn-reddit:hover{color:#fff;background-color:#ff500f;border-color:#c23400}.btn.btn-reddit.active,.btn.btn-reddit:active,.open>.btn.btn-reddit.dropdown-toggle,.show>.btn.btn-reddit.dropdown-toggle{color:#fff;background-color:#ff500f;border-color:#c23400;box-shadow:0 2px 2px 0 rgba(255,69,0,.14),0 3px 1px -2px rgba(255,69,0,.2),0 1px 5px 0 rgba(255,69,0,.12)}.btn.btn-reddit.active.focus,.btn.btn-reddit.active:focus,.btn.btn-reddit.active:hover,.btn.btn-reddit:active.focus,.btn.btn-reddit:active:focus,.btn.btn-reddit:active:hover,.open>.btn.btn-reddit.dropdown-toggle.focus,.open>.btn.btn-reddit.dropdown-toggle:focus,.open>.btn.btn-reddit.dropdown-toggle:hover,.show>.btn.btn-reddit.dropdown-toggle.focus,.show>.btn.btn-reddit.dropdown-toggle:focus,.show>.btn.btn-reddit.dropdown-toggle:hover{color:#fff;background-color:#ff500f;border-color:#802300}.open>.btn.btn-reddit.dropdown-toggle.bmd-btn-icon{color:inherit;background-color:#ff4500}.open>.btn.btn-reddit.dropdown-toggle.bmd-btn-icon:hover{background-color:#ff500f}.btn.btn-reddit.disabled.focus,.btn.btn-reddit.disabled:focus,.btn.btn-reddit.disabled:hover,.btn.btn-reddit:disabled.focus,.btn.btn-reddit:disabled:focus,.btn.btn-reddit:disabled:hover{background-color:#ff4500;border-color:#ff4500}.btn.btn-reddit:active,.btn.btn-reddit:focus,.btn.btn-reddit:hover{box-shadow:0 14px 26px -12px rgba(255,69,0,.42),0 4px 23px 0 rgba(0,0,0,.12),0 8px 10px -5px rgba(255,69,0,.2)}.btn.btn-reddit.btn-link{box-shadow:none}.btn.btn-reddit.btn-link,.btn.btn-reddit.btn-link:active,.btn.btn-reddit.btn-link:focus,.btn.btn-reddit.btn-link:hover{background-color:transparent;color:#ff4500}.btn.btn-tumblr{color:#fff;background-color:#35465c;border-color:#35465c;box-shadow:0 2px 2px 0 rgba(53,70,92,.14),0 3px 1px -2px rgba(53,70,92,.2),0 1px 5px 0 rgba(53,70,92,.12)}.btn.btn-tumblr.focus,.btn.btn-tumblr:focus,.btn.btn-tumblr:hover{color:#fff;background-color:#2f3f52;border-color:#1f2835}.btn.btn-tumblr.active,.btn.btn-tumblr:active,.open>.btn.btn-tumblr.dropdown-toggle,.show>.btn.btn-tumblr.dropdown-toggle{color:#fff;background-color:#2f3f52;border-color:#1f2835;box-shadow:0 2px 2px 0 rgba(53,70,92,.14),0 3px 1px -2px rgba(53,70,92,.2),0 1px 5px 0 rgba(53,70,92,.12)}.btn.btn-tumblr.active.focus,.btn.btn-tumblr.active:focus,.btn.btn-tumblr.active:hover,.btn.btn-tumblr:active.focus,.btn.btn-tumblr:active:focus,.btn.btn-tumblr:active:hover,.open>.btn.btn-tumblr.dropdown-toggle.focus,.open>.btn.btn-tumblr.dropdown-toggle:focus,.open>.btn.btn-tumblr.dropdown-toggle:hover,.show>.btn.btn-tumblr.dropdown-toggle.focus,.show>.btn.btn-tumblr.dropdown-toggle:focus,.show>.btn.btn-tumblr.dropdown-toggle:hover{color:#fff;background-color:#2f3f52;border-color:#06080b}.open>.btn.btn-tumblr.dropdown-toggle.bmd-btn-icon{color:inherit;background-color:#35465c}.open>.btn.btn-tumblr.dropdown-toggle.bmd-btn-icon:hover{background-color:#2f3f52}.btn.btn-tumblr.disabled.focus,.btn.btn-tumblr.disabled:focus,.btn.btn-tumblr.disabled:hover,.btn.btn-tumblr:disabled.focus,.btn.btn-tumblr:disabled:focus,.btn.btn-tumblr:disabled:hover{background-color:#35465c;border-color:#35465c}.btn.btn-tumblr:active,.btn.btn-tumblr:focus,.btn.btn-tumblr:hover{box-shadow:0 14px 26px -12px rgba(53,70,92,.42),0 4px 23px 0 rgba(0,0,0,.12),0 8px 10px -5px rgba(53,70,92,.2)}.btn.btn-tumblr.btn-link{box-shadow:none}.btn.btn-tumblr.btn-link,.btn.btn-tumblr.btn-link:active,.btn.btn-tumblr.btn-link:focus,.btn.btn-tumblr.btn-link:hover{background-color:transparent;color:#35465c}.btn.btn-behance{color:#fff;background-color:#1769ff;border-color:#1769ff;box-shadow:0 2px 2px 0 rgba(23,105,255,.14),0 3px 1px -2px rgba(23,105,255,.2),0 1px 5px 0 rgba(23,105,255,.12)}.btn.btn-behance.focus,.btn.btn-behance:focus,.btn.btn-behance:hover{color:#fff;background-color:#2673ff;border-color:#004dd9}.btn.btn-behance.active,.btn.btn-behance:active,.open>.btn.btn-behance.dropdown-toggle,.show>.btn.btn-behance.dropdown-toggle{color:#fff;background-color:#2673ff;border-color:#004dd9;box-shadow:0 2px 2px 0 rgba(23,105,255,.14),0 3px 1px -2px rgba(23,105,255,.2),0 1px 5px 0 rgba(23,105,255,.12)}.btn.btn-behance.active.focus,.btn.btn-behance.active:focus,.btn.btn-behance.active:hover,.btn.btn-behance:active.focus,.btn.btn-behance:active:focus,.btn.btn-behance:active:hover,.open>.btn.btn-behance.dropdown-toggle.focus,.open>.btn.btn-behance.dropdown-toggle:focus,.open>.btn.btn-behance.dropdown-toggle:hover,.show>.btn.btn-behance.dropdown-toggle.focus,.show>.btn.btn-behance.dropdown-toggle:focus,.show>.btn.btn-behance.dropdown-toggle:hover{color:#fff;background-color:#2673ff;border-color:#003597}.open>.btn.btn-behance.dropdown-toggle.bmd-btn-icon{color:inherit;background-color:#1769ff}.open>.btn.btn-behance.dropdown-toggle.bmd-btn-icon:hover{background-color:#2673ff}.btn.btn-behance.disabled.focus,.btn.btn-behance.disabled:focus,.btn.btn-behance.disabled:hover,.btn.btn-behance:disabled.focus,.btn.btn-behance:disabled:focus,.btn.btn-behance:disabled:hover{background-color:#1769ff;border-color:#1769ff}.btn.btn-behance:active,.btn.btn-behance:focus,.btn.btn-behance:hover{box-shadow:0 14px 26px -12px rgba(23,105,255,.42),0 4px 23px 0 rgba(0,0,0,.12),0 8px 10px -5px rgba(23,105,255,.2)}.btn.btn-behance.btn-link{box-shadow:none}.btn.btn-behance.btn-link,.btn.btn-behance.btn-link:active,.btn.btn-behance.btn-link:focus,.btn.btn-behance.btn-link:hover{background-color:transparent;color:#1769ff}.noUi-target,.noUi-target *{-webkit-touch-callout:none;-webkit-user-select:none;-ms-touch-action:none;touch-action:none;-ms-user-select:none;-moz-user-select:none;user-select:none;box-sizing:border-box}.noUi-target{position:relative;direction:ltr}.noUi-base{width:100%;height:100%;position:relative;z-index:1}.noUi-connect{position:absolute;right:0;top:0;left:0;bottom:0}.noUi-origin{position:absolute;height:0;width:0;margin:0;border-radius:0;height:2px;background:#c8c8c8}.noUi-origin[style^="left: 0"] .noUi-handle{background-color:#fff;border:2px solid #c8c8c8}.noUi-origin[style^="left: 0"] .noUi-handle.noUi-active{border-width:1px}.noUi-handle{position:relative;z-index:1}.noUi-state-tap .noUi-connect,.noUi-state-tap .noUi-origin{transition:top .3s,right .3s,bottom .3s,left .3s}.noUi-state-drag *{cursor:inherit!important}.noUi-base,.noUi-handle{transform:translateZ(0)}.noUi-horizontal{height:2px;margin:15px 0}.noUi-vertical{width:18px}.noUi-vertical .noUi-handle{width:28px;height:34px;left:-6px;top:-17px}.noUi-target{background:#c8c8c8;border-radius:4px}.noUi-connect{background:#3fb8af;transition:background .45s}.noUi-draggable{cursor:w-resize}.noUi-vertical .noUi-draggable{cursor:n-resize}.noUi-handle{box-sizing:border-box;width:14px;height:14px;left:-10px;top:-6px;cursor:pointer;border-radius:100%;transition:all .2s ease-out;border:1px solid;background:#fff;box-shadow:0 2px 2px 0 rgba(0,0,0,.14),0 3px 1px -2px rgba(0,0,0,.12),0 1px 5px 0 rgba(0,0,0,.2)}.noUi-handle.noUi-active{transform:scale3d(1.5,1.5,1)}.noUi-vertical .noUi-handle:after,.noUi-vertical .noUi-handle:before{width:14px;height:1px;left:6px;top:14px}.noUi-vertical .noUi-handle:after{top:17px}[disabled] .noUi-connect{background:#b8b8b8}[disabled].noUi-handle,[disabled] .noUi-handle,[disabled].noUi-target{cursor:not-allowed}.slider{background:#c8c8c8}.slider .noUi-connect{background-color:#9c27b0;border-radius:4px}.slider .noUi-handle{border-color:#9c27b0}.slider.slider-info .noUi-connect{background-color:#00bcd4}.slider.slider-info .noUi-handle{border-color:#00bcd4}.slider.slider-success .noUi-connect{background-color:#4caf50}.slider.slider-success .noUi-handle{border-color:#4caf50}.slider.slider-warning .noUi-connect{background-color:#ff9800}.slider.slider-warning .noUi-handle{border-color:#ff9800}.slider.slider-danger .noUi-connect{background-color:#f44336}.slider.slider-danger .noUi-handle{border-color:#f44336}.slider.slider-rose .noUi-connect{background-color:#e91e63}.slider.slider-rose .noUi-handle{border-color:#e91e63}.animated{animation-duration:1s;animation-fill-mode:both}.animated.infinite{animation-iteration-count:infinite}.animated.hinge{animation-duration:2s}.animated.bounceIn,.animated.bounceOut,.animated.flipOutX,.animated.flipOutY{animation-duration:.75s}@keyframes f{0%,to{transform:translateZ(0)}10%,30%,50%,70%,90%{transform:translate3d(-10px,0,0)}20%,40%,60%,80%{transform:translate3d(10px,0,0)}}.shake{animation-name:f}@keyframes g{0%{opacity:0;transform:translate3d(0,-100%,0)}to{opacity:1;transform:none}}.fadeInDown{animation-name:g}@keyframes h{0%{opacity:1}to{opacity:0}}.fadeOut{animation-name:h}@keyframes i{0%{opacity:1}to{opacity:0;transform:translate3d(0,100%,0)}}.fadeOutDown{animation-name:i}@keyframes j{0%{opacity:1}to{opacity:0;transform:translate3d(0,-100%,0)}}.fadeOutUp{animation-name:j}

/*!
* sweetalert2 v7.24.1
* Released under the MIT License.
*/@keyframes k{0%{transform:scale(.7)}45%{transform:scale(1.05)}80%{transform:scale(.95)}to{transform:scale(1)}}@keyframes l{0%{transform:scale(1);opacity:1}to{transform:scale(.5);opacity:0}}@keyframes m{0%{top:1.1875em;left:.0625em;width:0}54%{top:1.0625em;left:.125em;width:0}70%{top:2.1875em;left:-.375em;width:3.125em}84%{top:3em;left:1.3125em;width:1.0625em}to{top:2.8125em;left:.875em;width:1.5625em}}@keyframes n{0%{top:3.375em;right:2.875em;width:0}65%{top:3.375em;right:2.875em;width:0}84%{top:2.1875em;right:0;width:3.4375em}to{top:2.375em;right:.5em;width:2.9375em}}@keyframes o{0%{transform:rotate(-45deg)}5%{transform:rotate(-45deg)}12%{transform:rotate(-405deg)}to{transform:rotate(-405deg)}}@keyframes p{0%{margin-top:1.625em;transform:scale(.4);opacity:0}50%{margin-top:1.625em;transform:scale(.4);opacity:0}80%{margin-top:-.375em;transform:scale(1.15)}to{margin-top:0;transform:scale(1);opacity:1}}@keyframes q{0%{transform:rotateX(100deg);opacity:0}to{transform:rotateX(0deg);opacity:1}}body.swal2-toast-shown.swal2-has-input>.swal2-container>.swal2-toast{flex-direction:column;align-items:stretch}body.swal2-toast-shown.swal2-has-input>.swal2-container>.swal2-toast .swal2-actions{flex:1;align-self:stretch;justify-content:flex-end;height:2.2em}body.swal2-toast-shown.swal2-has-input>.swal2-container>.swal2-toast .swal2-loading{justify-content:center}body.swal2-toast-shown.swal2-has-input>.swal2-container>.swal2-toast .swal2-input{height:2em;margin:.3125em auto;font-size:1em}body.swal2-toast-shown.swal2-has-input>.swal2-container>.swal2-toast .swal2-validationerror{font-size:1em}body.swal2-toast-shown>.swal2-container{position:fixed;background-color:transparent}body.swal2-toast-shown>.swal2-container.swal2-shown{background-color:transparent}body.swal2-toast-shown>.swal2-container.swal2-top{top:0;right:auto;bottom:auto;left:50%;transform:translateX(-50%)}body.swal2-toast-shown>.swal2-container.swal2-top-end,body.swal2-toast-shown>.swal2-container.swal2-top-right{top:0;right:0;bottom:auto;left:auto}body.swal2-toast-shown>.swal2-container.swal2-top-left,body.swal2-toast-shown>.swal2-container.swal2-top-start{top:0;right:auto;bottom:auto;left:0}body.swal2-toast-shown>.swal2-container.swal2-center-left,body.swal2-toast-shown>.swal2-container.swal2-center-start{top:50%;right:auto;bottom:auto;left:0;transform:translateY(-50%)}body.swal2-toast-shown>.swal2-container.swal2-center{top:50%;right:auto;bottom:auto;left:50%;transform:translate(-50%,-50%)}body.swal2-toast-shown>.swal2-container.swal2-center-end,body.swal2-toast-shown>.swal2-container.swal2-center-right{top:50%;right:0;bottom:auto;left:auto;transform:translateY(-50%)}body.swal2-toast-shown>.swal2-container.swal2-bottom-left,body.swal2-toast-shown>.swal2-container.swal2-bottom-start{top:auto;right:auto;bottom:0;left:0}body.swal2-toast-shown>.swal2-container.swal2-bottom{top:auto;right:auto;bottom:0;left:50%;transform:translateX(-50%)}body.swal2-toast-shown>.swal2-container.swal2-bottom-end,body.swal2-toast-shown>.swal2-container.swal2-bottom-right{top:auto;right:0;bottom:0;left:auto}.swal2-popup.swal2-toast{flex-direction:row;align-items:center;width:auto;padding:.625em;box-shadow:0 0 .625em #d9d9d9;overflow-y:hidden}.swal2-popup.swal2-toast .swal2-header{flex-direction:row}.swal2-popup.swal2-toast .swal2-title{justify-content:flex-start;margin:0 .6em;font-size:1em}.swal2-popup.swal2-toast .swal2-close{position:static}.swal2-popup.swal2-toast .swal2-content{justify-content:flex-start;font-size:1em}.swal2-popup.swal2-toast .swal2-icon{width:2em;min-width:2em;height:2em;margin:0}.swal2-popup.swal2-toast .swal2-icon-text{font-size:2em;font-weight:700;line-height:1em}.swal2-popup.swal2-toast .swal2-icon.swal2-success .swal2-success-ring{width:2em;height:2em}.swal2-popup.swal2-toast .swal2-icon.swal2-error [class^=swal2-x-mark-line]{top:.875em;width:1.375em}.swal2-popup.swal2-toast .swal2-icon.swal2-error [class^=swal2-x-mark-line][class$=left]{left:.3125em}.swal2-popup.swal2-toast .swal2-icon.swal2-error [class^=swal2-x-mark-line][class$=right]{right:.3125em}.swal2-popup.swal2-toast .swal2-actions{height:auto;margin:0 .3125em}.swal2-popup.swal2-toast .swal2-styled{margin:0 .3125em;padding:.3125em .625em;font-size:1em}.swal2-popup.swal2-toast .swal2-styled:focus{box-shadow:0 0 0 .0625em #fff,0 0 0 .125em rgba(50,100,150,.4)}.swal2-popup.swal2-toast .swal2-success{border-color:#a5dc86}.swal2-popup.swal2-toast .swal2-success [class^=swal2-success-circular-line]{position:absolute;width:2em;height:2.8125em;transform:rotate(45deg);border-radius:50%}.swal2-popup.swal2-toast .swal2-success [class^=swal2-success-circular-line][class$=left]{top:-.25em;left:-.9375em;transform:rotate(-45deg);transform-origin:2em 2em;border-radius:4em 0 0 4em}.swal2-popup.swal2-toast .swal2-success [class^=swal2-success-circular-line][class$=right]{top:-.25em;left:.9375em;transform-origin:0 2em;border-radius:0 4em 4em 0}.swal2-popup.swal2-toast .swal2-success .swal2-success-ring{width:2em;height:2em}.swal2-popup.swal2-toast .swal2-success .swal2-success-fix{top:0;left:.4375em;width:.4375em;height:2.6875em}.swal2-popup.swal2-toast .swal2-success [class^=swal2-success-line]{height:.3125em}.swal2-popup.swal2-toast .swal2-success [class^=swal2-success-line][class$=tip]{top:1.125em;left:.1875em;width:.75em}.swal2-popup.swal2-toast .swal2-success [class^=swal2-success-line][class$=long]{top:.9375em;right:.1875em;width:1.375em}.swal2-popup.swal2-toast.swal2-show{animation:r .5s}.swal2-popup.swal2-toast.swal2-hide{animation:s .2s forwards}.swal2-popup.swal2-toast .swal2-animate-success-icon .swal2-success-line-tip{animation:t .75s}.swal2-popup.swal2-toast .swal2-animate-success-icon .swal2-success-line-long{animation:u .75s}@keyframes r{0%{transform:translateY(-.625em) rotate(2deg);opacity:0}33%{transform:translateY(0) rotate(-2deg);opacity:.5}66%{transform:translateY(.3125em) rotate(2deg);opacity:.7}to{transform:translateY(0) rotate(0);opacity:1}}@keyframes s{0%{opacity:1}33%{opacity:.5}to{transform:rotate(1deg);opacity:0}}@keyframes t{0%{top:.5625em;left:.0625em;width:0}54%{top:.125em;left:.125em;width:0}70%{top:.625em;left:-.25em;width:1.625em}84%{top:1.0625em;left:.75em;width:.5em}to{top:1.125em;left:.1875em;width:.75em}}@keyframes u{0%{top:1.625em;right:1.375em;width:0}65%{top:1.25em;right:.9375em;width:0}84%{top:.9375em;right:0;width:1.125em}to{top:.9375em;right:.1875em;width:1.375em}}body.swal2-shown:not(.swal2-no-backdrop):not(.swal2-toast-shown){overflow-y:hidden}body.swal2-height-auto{height:auto!important}body.swal2-no-backdrop .swal2-shown{top:auto;right:auto;bottom:auto;left:auto;background-color:transparent}body.swal2-no-backdrop .swal2-shown>.swal2-modal{box-shadow:0 0 10px rgba(0,0,0,.4)}body.swal2-no-backdrop .swal2-shown.swal2-top{top:0;left:50%;transform:translateX(-50%)}body.swal2-no-backdrop .swal2-shown.swal2-top-left,body.swal2-no-backdrop .swal2-shown.swal2-top-start{top:0;left:0}body.swal2-no-backdrop .swal2-shown.swal2-top-end,body.swal2-no-backdrop .swal2-shown.swal2-top-right{top:0;right:0}body.swal2-no-backdrop .swal2-shown.swal2-center{top:50%;left:50%;transform:translate(-50%,-50%)}body.swal2-no-backdrop .swal2-shown.swal2-center-left,body.swal2-no-backdrop .swal2-shown.swal2-center-start{top:50%;left:0;transform:translateY(-50%)}body.swal2-no-backdrop .swal2-shown.swal2-center-end,body.swal2-no-backdrop .swal2-shown.swal2-center-right{top:50%;right:0;transform:translateY(-50%)}body.swal2-no-backdrop .swal2-shown.swal2-bottom{bottom:0;left:50%;transform:translateX(-50%)}body.swal2-no-backdrop .swal2-shown.swal2-bottom-left,body.swal2-no-backdrop .swal2-shown.swal2-bottom-start{bottom:0;left:0}body.swal2-no-backdrop .swal2-shown.swal2-bottom-end,body.swal2-no-backdrop .swal2-shown.swal2-bottom-right{right:0;bottom:0}.swal2-container{display:flex;position:fixed;top:0;right:0;bottom:0;left:0;flex-direction:row;align-items:center;justify-content:center;padding:10px;background-color:transparent;z-index:1060;overflow-x:hidden;-webkit-overflow-scrolling:touch}.swal2-container.swal2-top{align-items:flex-start}.swal2-container.swal2-top-left,.swal2-container.swal2-top-start{align-items:flex-start;justify-content:flex-start}.swal2-container.swal2-top-end,.swal2-container.swal2-top-right{align-items:flex-start;justify-content:flex-end}.swal2-container.swal2-center{align-items:center}.swal2-container.swal2-center-left,.swal2-container.swal2-center-start{align-items:center;justify-content:flex-start}.swal2-container.swal2-center-end,.swal2-container.swal2-center-right{align-items:center;justify-content:flex-end}.swal2-container.swal2-bottom{align-items:flex-end}.swal2-container.swal2-bottom-left,.swal2-container.swal2-bottom-start{align-items:flex-end;justify-content:flex-start}.swal2-container.swal2-bottom-end,.swal2-container.swal2-bottom-right{align-items:flex-end;justify-content:flex-end}.swal2-container.swal2-grow-fullscreen>.swal2-modal{display:flex!important;flex:1;align-self:stretch;justify-content:center}.swal2-container.swal2-grow-row>.swal2-modal{display:flex!important;flex:1;align-content:center;justify-content:center}.swal2-container.swal2-grow-column{flex:1;flex-direction:column}.swal2-container.swal2-grow-column.swal2-bottom,.swal2-container.swal2-grow-column.swal2-center,.swal2-container.swal2-grow-column.swal2-top{align-items:center}.swal2-container.swal2-grow-column.swal2-bottom-left,.swal2-container.swal2-grow-column.swal2-bottom-start,.swal2-container.swal2-grow-column.swal2-center-left,.swal2-container.swal2-grow-column.swal2-center-start,.swal2-container.swal2-grow-column.swal2-top-left,.swal2-container.swal2-grow-column.swal2-top-start{align-items:flex-start}.swal2-container.swal2-grow-column.swal2-bottom-end,.swal2-container.swal2-grow-column.swal2-bottom-right,.swal2-container.swal2-grow-column.swal2-center-end,.swal2-container.swal2-grow-column.swal2-center-right,.swal2-container.swal2-grow-column.swal2-top-end,.swal2-container.swal2-grow-column.swal2-top-right{align-items:flex-end}.swal2-container.swal2-grow-column>.swal2-modal{display:flex!important;flex:1;align-content:center;justify-content:center}.swal2-container:not(.swal2-top):not(.swal2-top-start):not(.swal2-top-end):not(.swal2-top-left):not(.swal2-top-right):not(.swal2-center-start):not(.swal2-center-end):not(.swal2-center-left):not(.swal2-center-right):not(.swal2-bottom):not(.swal2-bottom-start):not(.swal2-bottom-end):not(.swal2-bottom-left):not(.swal2-bottom-right)>.swal2-modal{margin:auto}@media (-ms-high-contrast:active),(-ms-high-contrast:none){.swal2-container .swal2-modal{margin:0!important}}.swal2-container.swal2-fade{transition:background-color .1s}.swal2-container.swal2-shown{background-color:rgba(0,0,0,.4)}.swal2-popup{display:none;position:relative;flex-direction:column;justify-content:center;width:32em;max-width:100%;padding:1.25em;border-radius:.3125em;background:#fff;font-family:inherit;font-size:1rem;box-sizing:border-box}.swal2-popup:focus{outline:none}.swal2-popup.swal2-loading{overflow-y:hidden}.swal2-popup .swal2-header{display:flex;flex-direction:column;align-items:center}.swal2-popup .swal2-title{display:block;position:relative;max-width:100%;margin:0 0 .4em;padding:0;color:#595959;font-size:1.875em;font-weight:600;text-align:center;text-transform:none;word-wrap:break-word}.swal2-popup .swal2-actions{align-items:center;justify-content:center;margin:1.25em auto 0}.swal2-popup .swal2-actions:not(.swal2-loading) .swal2-styled[disabled]{opacity:.4}.swal2-popup .swal2-actions:not(.swal2-loading) .swal2-styled:hover{background-image:linear-gradient(rgba(0,0,0,.1),rgba(0,0,0,.1))}.swal2-popup .swal2-actions:not(.swal2-loading) .swal2-styled:active{background-image:linear-gradient(rgba(0,0,0,.2),rgba(0,0,0,.2))}.swal2-popup .swal2-actions.swal2-loading .swal2-styled.swal2-confirm{width:2.5em;height:2.5em;margin:.46875em;padding:0;border:.25em solid transparent;border-radius:100%;border-color:transparent;background-color:transparent!important;color:transparent;cursor:default;box-sizing:border-box;animation:v 1.5s linear 0s infinite normal;-webkit-user-select:none;-moz-user-select:none;-ms-user-select:none;user-select:none}.swal2-popup .swal2-actions.swal2-loading .swal2-styled.swal2-cancel{margin-right:30px;margin-left:30px}.swal2-popup .swal2-actions.swal2-loading :not(.swal2-styled).swal2-confirm:after{display:inline-block;width:15px;height:15px;margin-left:5px;border:3px solid #999;border-radius:50%;border-right-color:transparent;box-shadow:1px 1px 1px #fff;content:"";animation:v 1.5s linear 0s infinite normal}.swal2-popup .swal2-styled{margin:0 .3125em;padding:.625em 2em;font-weight:500;box-shadow:none}.swal2-popup .swal2-styled:not([disabled]){cursor:pointer}.swal2-popup .swal2-styled.swal2-confirm{border:0;border-radius:.25em;background:initial;background-color:#3085d6;color:#fff;font-size:1.0625em}.swal2-popup .swal2-styled.swal2-cancel{border:0;border-radius:.25em;background:initial;background-color:#aaa;color:#fff;font-size:1.0625em}.swal2-popup .swal2-styled:focus{outline:none;box-shadow:0 0 0 2px #fff,0 0 0 4px rgba(50,100,150,.4)}.swal2-popup .swal2-styled::-moz-focus-inner{border:0}.swal2-popup .swal2-footer{justify-content:center;margin:1.25em 0 0;padding-top:1em;border-top:1px solid #eee;color:#545454;font-size:1em}.swal2-popup .swal2-image{max-width:100%;margin:1.25em auto}.swal2-popup .swal2-close{position:absolute;top:0;right:0;justify-content:center;width:1.2em;height:1.2em;padding:0;transition:color .1s ease-out;border:none;border-radius:0;background:transparent;color:#ccc;font-family:serif;font-size:2.5em;line-height:1.2;cursor:pointer;overflow:hidden}.swal2-popup .swal2-close:hover{transform:none;color:#f27474}.swal2-popup>.swal2-checkbox,.swal2-popup>.swal2-file,.swal2-popup>.swal2-input,.swal2-popup>.swal2-radio,.swal2-popup>.swal2-select,.swal2-popup>.swal2-textarea{display:none}.swal2-popup .swal2-content{justify-content:center;margin:0;padding:0;color:#545454;font-size:1.125em;font-weight:300;line-height:normal;word-wrap:break-word}.swal2-popup #swal2-content{text-align:center}.swal2-popup .swal2-checkbox,.swal2-popup .swal2-file,.swal2-popup .swal2-input,.swal2-popup .swal2-radio,.swal2-popup .swal2-select,.swal2-popup .swal2-textarea{margin:1em auto}.swal2-popup .swal2-file,.swal2-popup .swal2-input,.swal2-popup .swal2-textarea{width:100%;transition:border-color .3s,box-shadow .3s;border:1px solid #d9d9d9;border-radius:.1875em;font-size:1.125em;box-shadow:inset 0 1px 1px rgba(0,0,0,.06);box-sizing:border-box}.swal2-popup .swal2-file.swal2-inputerror,.swal2-popup .swal2-input.swal2-inputerror,.swal2-popup .swal2-textarea.swal2-inputerror{border-color:#f27474!important;box-shadow:0 0 2px #f27474!important}.swal2-popup .swal2-file:focus,.swal2-popup .swal2-input:focus,.swal2-popup .swal2-textarea:focus{border:1px solid #b4dbed;outline:none;box-shadow:0 0 3px #c4e6f5}.swal2-popup .swal2-file::-webkit-input-placeholder,.swal2-popup .swal2-input::-webkit-input-placeholder,.swal2-popup .swal2-textarea::-webkit-input-placeholder{color:#ccc}.swal2-popup .swal2-file:-ms-input-placeholder,.swal2-popup .swal2-file::-ms-input-placeholder,.swal2-popup .swal2-input:-ms-input-placeholder,.swal2-popup .swal2-input::-ms-input-placeholder,.swal2-popup .swal2-textarea:-ms-input-placeholder,.swal2-popup .swal2-textarea::-ms-input-placeholder{color:#ccc}.swal2-popup .swal2-file::placeholder,.swal2-popup .swal2-input::placeholder,.swal2-popup .swal2-textarea::placeholder{color:#ccc}.swal2-popup .swal2-range input{width:80%}.swal2-popup .swal2-range output{width:20%;font-weight:600;text-align:center}.swal2-popup .swal2-range input,.swal2-popup .swal2-range output{height:2.625em;margin:1em auto;padding:0;font-size:1.125em;line-height:2.625em}.swal2-popup .swal2-input{height:2.625em;padding:.75em}.swal2-popup .swal2-input[type=number]{max-width:10em}.swal2-popup .swal2-file{font-size:1.125em}.swal2-popup .swal2-textarea{height:6.75em;padding:.75em}.swal2-popup .swal2-select{min-width:50%;max-width:100%;padding:.375em .625em;color:#545454;font-size:1.125em}.swal2-popup .swal2-checkbox,.swal2-popup .swal2-radio{align-items:center;justify-content:center}.swal2-popup .swal2-checkbox label,.swal2-popup .swal2-radio label{margin:0 .6em;font-size:1.125em}.swal2-popup .swal2-checkbox input,.swal2-popup .swal2-radio input{margin:0 .4em}.swal2-popup .swal2-validationerror{display:none;align-items:center;justify-content:center;padding:.625em;background:#f0f0f0;color:#666;font-size:1em;font-weight:300;overflow:hidden}.swal2-popup .swal2-validationerror:before{display:inline-block;width:1.5em;min-width:1.5em;height:1.5em;margin:0 .625em;border-radius:50%;background-color:#f27474;color:#fff;font-weight:600;line-height:1.5em;text-align:center;content:"!";zoom:normal}@supports (-ms-accelerator:true){.swal2-range input{width:100%!important}.swal2-range output{display:none}}@media (-ms-high-contrast:active),(-ms-high-contrast:none){.swal2-range input{width:100%!important}.swal2-range output{display:none}}@-moz-document url-prefix(){.swal2-close:focus{outline:2px solid rgba(50,100,150,.4)}}.swal2-icon{position:relative;justify-content:center;width:5em;height:5em;margin:1.25em auto 1.875em;border:.25em solid transparent;border-radius:50%;line-height:5em;cursor:default;box-sizing:content-box;-webkit-user-select:none;-moz-user-select:none;-ms-user-select:none;user-select:none;zoom:normal}.swal2-icon-text{font-size:3.75em}.swal2-icon.swal2-error{border-color:#f27474}.swal2-icon.swal2-error .swal2-x-mark{position:relative;flex-grow:1}.swal2-icon.swal2-error [class^=swal2-x-mark-line]{display:block;position:absolute;top:2.3125em;width:2.9375em;height:.3125em;border-radius:.125em;background-color:#f27474}.swal2-icon.swal2-error [class^=swal2-x-mark-line][class$=left]{left:1.0625em;transform:rotate(45deg)}.swal2-icon.swal2-error [class^=swal2-x-mark-line][class$=right]{right:1em;transform:rotate(-45deg)}.swal2-icon.swal2-warning{border-color:#facea8;color:#f8bb86}.swal2-icon.swal2-info{border-color:#9de0f6;color:#3fc3ee}.swal2-icon.swal2-question{border-color:#c9dae1;color:#87adbd}.swal2-icon.swal2-success{border-color:#a5dc86}.swal2-icon.swal2-success [class^=swal2-success-circular-line]{position:absolute;width:3.75em;height:7.5em;transform:rotate(45deg);border-radius:50%}.swal2-icon.swal2-success [class^=swal2-success-circular-line][class$=left]{top:-.4375em;left:-2.0635em;transform:rotate(-45deg);transform-origin:3.75em 3.75em;border-radius:7.5em 0 0 7.5em}.swal2-icon.swal2-success [class^=swal2-success-circular-line][class$=right]{top:-.6875em;left:1.875em;transform:rotate(-45deg);transform-origin:0 3.75em;border-radius:0 7.5em 7.5em 0}.swal2-icon.swal2-success .swal2-success-ring{position:absolute;top:-.25em;left:-.25em;width:100%;height:100%;border:.25em solid hsla(98,55%,69%,.3);border-radius:50%;z-index:2;box-sizing:content-box}.swal2-icon.swal2-success .swal2-success-fix{position:absolute;top:.5em;left:1.625em;width:.4375em;height:5.625em;transform:rotate(-45deg);z-index:1}.swal2-icon.swal2-success [class^=swal2-success-line]{display:block;position:absolute;height:.3125em;border-radius:.125em;background-color:#a5dc86;z-index:2}.swal2-icon.swal2-success [class^=swal2-success-line][class$=tip]{top:2.875em;left:.875em;width:1.5625em;transform:rotate(45deg)}.swal2-icon.swal2-success [class^=swal2-success-line][class$=long]{top:2.375em;right:.5em;width:2.9375em;transform:rotate(-45deg)}.swal2-progresssteps{align-items:center;margin:0 0 1.25em;padding:0;font-weight:600}.swal2-progresssteps li{display:inline-block;position:relative}.swal2-progresssteps .swal2-progresscircle{width:2em;height:2em;border-radius:2em;background:#3085d6;color:#fff;line-height:2em;text-align:center;z-index:20}.swal2-progresssteps .swal2-progresscircle:first-child{margin-left:0}.swal2-progresssteps .swal2-progresscircle:last-child{margin-right:0}.swal2-progresssteps .swal2-progresscircle.swal2-activeprogressstep{background:#3085d6}.swal2-progresssteps .swal2-progresscircle.swal2-activeprogressstep~.swal2-progresscircle,.swal2-progresssteps .swal2-progresscircle.swal2-activeprogressstep~.swal2-progressline{background:#add8e6}.swal2-progresssteps .swal2-progressline{width:2.5em;height:.4em;margin:0 -1px;background:#3085d6;z-index:10}[class^=swal2]{-webkit-tap-highlight-color:transparent}.swal2-show{animation:k .3s}.swal2-show.swal2-noanimation{animation:none}.swal2-hide{animation:l .15s forwards}.swal2-hide.swal2-noanimation{animation:none}[dir=rtl] .swal2-close{right:auto;left:0}.swal2-animate-success-icon .swal2-success-line-tip{animation:m .75s}.swal2-animate-success-icon .swal2-success-line-long{animation:n .75s}.swal2-animate-success-icon .swal2-success-circular-line-right{animation:o 4.25s ease-in}.swal2-animate-error-icon{animation:q .5s}.swal2-animate-error-icon .swal2-x-mark{animation:p .5s}@keyframes v{0%{transform:rotate(0deg)}to{transform:rotate(1turn)}}table.dataTable{clear:both;margin-top:6px!important;margin-bottom:6px!important;max-width:none!important;border-collapse:separate!important;border-spacing:0}table.dataTable td,table.dataTable th{box-sizing:content-box}table.dataTable td.dataTables_empty,table.dataTable th.dataTables_empty{text-align:center}table.dataTable.nowrap td,table.dataTable.nowrap th{white-space:nowrap}div.dataTables_wrapper div.dataTables_length label{font-weight:400;text-align:left;white-space:nowrap}div.dataTables_wrapper div.dataTables_length select{width:auto;display:inline-block}div.dataTables_wrapper div.dataTables_filter{text-align:right}div.dataTables_wrapper div.dataTables_filter label{font-weight:400;white-space:nowrap;text-align:left}div.dataTables_wrapper div.dataTables_filter input{margin-left:.5em;display:inline-block;width:auto}div.dataTables_wrapper div.dataTables_info{padding-top:.85em;white-space:nowrap}div.dataTables_wrapper div.dataTables_paginate{margin:0;white-space:nowrap;text-align:right}div.dataTables_wrapper div.dataTables_paginate ul.pagination{margin:2px 0;white-space:nowrap;justify-content:flex-end}div.dataTables_wrapper div.dataTables_processing{position:absolute;top:50%;left:50%;width:200px;margin-left:-100px;margin-top:-26px;text-align:center;padding:1em 0}table.dataTable thead>tr>td.sorting,table.dataTable thead>tr>td.sorting_asc,table.dataTable thead>tr>td.sorting_desc,table.dataTable thead>tr>th.sorting,table.dataTable thead>tr>th.sorting_asc,table.dataTable thead>tr>th.sorting_desc{padding-right:30px}table.dataTable thead>tr>td:active,table.dataTable thead>tr>th:active{outline:none}table.dataTable thead .sorting,table.dataTable thead .sorting_asc,table.dataTable thead .sorting_asc_disabled,table.dataTable thead .sorting_desc,table.dataTable thead .sorting_desc_disabled{cursor:pointer;position:relative}table.dataTable thead .sorting:after,table.dataTable thead .sorting:before,table.dataTable thead .sorting_asc:after,table.dataTable thead .sorting_asc:before,table.dataTable thead .sorting_asc_disabled:after,table.dataTable thead .sorting_asc_disabled:before,table.dataTable thead .sorting_desc:after,table.dataTable thead .sorting_desc:before,table.dataTable thead .sorting_desc_disabled:after,table.dataTable thead .sorting_desc_disabled:before{position:absolute;bottom:.9em;display:block;opacity:.3}table.dataTable thead .sorting:before,table.dataTable thead .sorting_asc:before,table.dataTable thead .sorting_asc_disabled:before,table.dataTable thead .sorting_desc:before,table.dataTable thead .sorting_desc_disabled:before{top:2px;right:1em;content:"\2191"}table.dataTable thead .sorting:after,table.dataTable thead .sorting_asc:after,table.dataTable thead .sorting_asc_disabled:after,table.dataTable thead .sorting_desc:after,table.dataTable thead .sorting_desc_disabled:after{top:2px;right:.5em;content:"\2193"}table.dataTable thead .sorting_asc:before,table.dataTable thead .sorting_desc:after{opacity:1}table.dataTable thead .sorting_asc_disabled:before,table.dataTable thead .sorting_desc_disabled:after{opacity:0}div.dataTables_scrollHead table.dataTable{margin-bottom:0!important}div.dataTables_scrollBody table{border-top:none;margin-top:0!important;margin-bottom:0!important}div.dataTables_scrollBody table thead .sorting:after,div.dataTables_scrollBody table thead .sorting:before,div.dataTables_scrollBody table thead .sorting_asc:after,div.dataTables_scrollBody table thead .sorting_asc:before,div.dataTables_scrollBody table thead .sorting_desc:after,div.dataTables_scrollBody table thead .sorting_desc:before{display:none}div.dataTables_scrollBody table tbody tr:first-child td,div.dataTables_scrollBody table tbody tr:first-child th{border-top:none}div.dataTables_scrollFoot>.dataTables_scrollFootInner{box-sizing:content-box}div.dataTables_scrollFoot>.dataTables_scrollFootInner>table{margin-top:0!important;border-top:none}@media screen and (max-width:767px){div.dataTables_wrapper div.dataTables_filter,div.dataTables_wrapper div.dataTables_info,div.dataTables_wrapper div.dataTables_length,div.dataTables_wrapper div.dataTables_paginate{text-align:center}}table.dataTable.table-sm>thead>tr>th{padding-right:20px}table.dataTable.table-sm .sorting:before,table.dataTable.table-sm .sorting_asc:before,table.dataTable.table-sm .sorting_desc:before{top:5px;right:.85em}table.dataTable.table-sm .sorting:after,table.dataTable.table-sm .sorting_asc:after,table.dataTable.table-sm .sorting_desc:after{top:5px}table.table-bordered.dataTable td,table.table-bordered.dataTable th{border-left-width:0}table.table-bordered.dataTable td:last-child,table.table-bordered.dataTable th:last-child{border-right-width:0}div.dataTables_scrollHead table.table-bordered,table.table-bordered.dataTable tbody td,table.table-bordered.dataTable tbody th{border-bottom-width:0}div.table-responsive>div.dataTables_wrapper>div.row{margin:0}div.table-responsive>div.dataTables_wrapper>div.row>div[class^=col-]:first-child{padding-left:0}div.table-responsive>div.dataTables_wrapper>div.row>div[class^=col-]:last-child{padding-right:0}div.dt-autofill-handle{position:absolute;height:8px;width:8px;z-index:102;box-sizing:border-box;border:1px solid #0275d8;background:#0275d8}div.dt-autofill-select{position:absolute;z-index:1001;background-color:#0275d8;background-image:repeating-linear-gradient(45deg,transparent,transparent 5px,hsla(0,0%,100%,.5) 0,hsla(0,0%,100%,.5) 10px)}div.dt-autofill-select.bottom,div.dt-autofill-select.top{height:3px;margin-top:-1px}div.dt-autofill-select.left,div.dt-autofill-select.right{width:3px;margin-left:-1px}div.dt-autofill-list{position:fixed;top:50%;left:50%;width:500px;margin-left:-250px;background-color:#fff;border-radius:6px;box-shadow:0 0 5px #555;border:2px solid #444;z-index:11;box-sizing:border-box;padding:1.5em 2em}div.dt-autofill-list ul{display:table;margin:0;padding:0;list-style:none;width:100%}div.dt-autofill-list ul li{display:table-row}div.dt-autofill-list ul li:last-child div.dt-autofill-button,div.dt-autofill-list ul li:last-child div.dt-autofill-question{border-bottom:none}div.dt-autofill-list ul li:hover{background-color:#f6f6f6}div.dt-autofill-list div.dt-autofill-question{display:table-cell;padding:.5em 0;border-bottom:1px solid #ccc}div.dt-autofill-list div.dt-autofill-question input[type=number]{width:30px}div.dt-autofill-list div.dt-autofill-button{display:table-cell;padding:.5em 0;border-bottom:1px solid #ccc}div.dt-autofill-background{position:fixed;top:0;left:0;width:100%;height:100%;background:rgba(0,0,0,.7);background:radial-gradient(ellipse farthest-corner at center,rgba(0,0,0,.3) 0,rgba(0,0,0,.7) 100%);z-index:10}div.dt-autofill-list div.dt-autofill-question input[type=number]{padding:6px;width:60px;margin:-2px 0}@keyframes w{to{transform:rotate(1turn)}}div.dt-button-info{position:fixed;top:50%;left:50%;width:400px;margin-top:-100px;margin-left:-200px;background-color:#fff;border:2px solid #111;box-shadow:3px 3px 8px rgba(0,0,0,.3);border-radius:3px;text-align:center;z-index:21}div.dt-button-info h2{padding:.5em;margin:0;font-weight:400;border-bottom:1px solid #ddd;background-color:#f3f3f3}div.dt-button-info>div{padding:1em}ul.dt-button-collection.dropdown-menu{display:block;z-index:2002;-ms-column-gap:8px;-o-column-gap:8px;column-gap:8px}ul.dt-button-collection.dropdown-menu.fixed{position:fixed;top:50%;left:50%;margin-left:-75px;border-radius:0}ul.dt-button-collection.dropdown-menu.fixed.two-column{margin-left:-150px}ul.dt-button-collection.dropdown-menu.fixed.three-column{margin-left:-225px}ul.dt-button-collection.dropdown-menu.fixed.four-column{margin-left:-300px}ul.dt-button-collection.dropdown-menu>*{break-inside:avoid}ul.dt-button-collection.dropdown-menu.two-column{width:300px;padding-bottom:1px;-ms-column-count:2;-o-column-count:2;column-count:2}ul.dt-button-collection.dropdown-menu.three-column{width:450px;padding-bottom:1px;-ms-column-count:3;-o-column-count:3;column-count:3}ul.dt-button-collection.dropdown-menu.four-column{width:600px;padding-bottom:1px;-ms-column-count:4;-o-column-count:4;column-count:4}ul.dt-button-collection.dropdown-menu .dt-button{border-radius:0}ul.dt-button-collection{-ms-column-gap:8px;-o-column-gap:8px;column-gap:8px}ul.dt-button-collection.fixed{position:fixed;top:50%;left:50%;margin-left:-75px;border-radius:0}ul.dt-button-collection.fixed.two-column{margin-left:-150px}ul.dt-button-collection.fixed.three-column{margin-left:-225px}ul.dt-button-collection.fixed.four-column{margin-left:-300px}ul.dt-button-collection>*{break-inside:avoid}ul.dt-button-collection.two-column{width:300px;padding-bottom:1px;-ms-column-count:2;-o-column-count:2;column-count:2}ul.dt-button-collection.three-column{width:450px;padding-bottom:1px;-ms-column-count:3;-o-column-count:3;column-count:3}ul.dt-button-collection.four-column{width:600px;padding-bottom:1px;-ms-column-count:4;-o-column-count:4;column-count:4}ul.dt-button-collection .dt-button{border-radius:0}ul.dt-button-collection.fixed{max-width:none}ul.dt-button-collection.fixed:after,ul.dt-button-collection.fixed:before{display:none}div.dt-button-background{position:fixed;top:0;left:0;width:100%;height:100%;z-index:999}@media screen and (max-width:767px){div.dt-buttons{float:none;width:100%;text-align:center;margin-bottom:.5em}div.dt-buttons a.btn{float:none}}div.dt-buttons a.btn.processing,div.dt-buttons button.btn.processing,div.dt-buttons div.btn.processing{color:rgba(0,0,0,.2)}div.dt-buttons a.btn.processing:after,div.dt-buttons button.btn.processing:after,div.dt-buttons div.btn.processing:after{position:absolute;top:50%;left:50%;width:16px;height:16px;margin:-8px 0 0 -8px;box-sizing:border-box;display:block;content:" ";border:2px solid #282828;border-radius:50%;border-left-color:transparent;border-right-color:transparent;animation:w 1.5s infinite linear;-o-animation:w 1.5s infinite linear;-ms-animation:w 1.5s infinite linear;-webkit-animation:w 1.5s infinite linear;-moz-animation:w 1.5s infinite linear}table.DTCR_clonedTable.dataTable{position:absolute!important;background-color:hsla(0,0%,100%,.7);z-index:202}div.DTCR_pointer{width:1px;background-color:#0275d8;z-index:201}table.DTFC_Cloned tr{background-color:#fff;margin-bottom:0}div.DTFC_LeftHeadWrapper table,div.DTFC_RightHeadWrapper table{border-bottom:none!important;margin-bottom:0!important;background-color:#fff}div.DTFC_LeftBodyWrapper table,div.DTFC_RightBodyWrapper table{border-top:none;margin:0!important}div.DTFC_LeftBodyWrapper table thead .sorting:after,div.DTFC_LeftBodyWrapper table thead .sorting_asc:after,div.DTFC_LeftBodyWrapper table thead .sorting_desc:after,div.DTFC_RightBodyWrapper table thead .sorting:after,div.DTFC_RightBodyWrapper table thead .sorting_asc:after,div.DTFC_RightBodyWrapper table thead .sorting_desc:after{display:none}div.DTFC_LeftBodyWrapper table tbody tr:first-child td,div.DTFC_LeftBodyWrapper table tbody tr:first-child th,div.DTFC_RightBodyWrapper table tbody tr:first-child td,div.DTFC_RightBodyWrapper table tbody tr:first-child th{border-top:none}div.DTFC_LeftFootWrapper table,div.DTFC_RightFootWrapper table{border-top:none;margin-top:0!important;background-color:#fff}div.DTFC_Blocker,table.dataTable.table-striped.DTFC_Cloned tbody{background-color:#fff}table.dataTable.fixedHeader-floating,table.dataTable.fixedHeader-locked{background-color:#fff;margin-top:0!important;margin-bottom:0!important}table.dataTable.fixedHeader-floating{position:fixed!important}table.dataTable.fixedHeader-locked{position:absolute!important}@media print{table.fixedHeader-floating{display:none}}table.dataTable tbody td.focus,table.dataTable tbody th.focus{box-shadow:inset 0 0 1px 2px #0275d8}table.dataTable.dtr-inline.collapsed>tbody>tr>td.child,table.dataTable.dtr-inline.collapsed>tbody>tr>td.dataTables_empty,table.dataTable.dtr-inline.collapsed>tbody>tr>th.child{cursor:default!important}table.dataTable.dtr-inline.collapsed>tbody>tr>td.child:before,table.dataTable.dtr-inline.collapsed>tbody>tr>td.dataTables_empty:before,table.dataTable.dtr-inline.collapsed>tbody>tr>th.child:before{display:none!important}table.dataTable.dtr-inline.collapsed>tbody>tr[role=row]>td:first-child,table.dataTable.dtr-inline.collapsed>tbody>tr[role=row]>th:first-child{position:relative;padding-left:30px;cursor:pointer}table.dataTable.dtr-inline.collapsed>tbody>tr[role=row]>td:first-child:before,table.dataTable.dtr-inline.collapsed>tbody>tr[role=row]>th:first-child:before{top:12px;left:4px;height:14px;width:14px;display:block;position:absolute;color:#fff;border:2px solid #fff;border-radius:14px;box-shadow:0 0 3px #444;box-sizing:content-box;text-align:center;text-indent:0!important;font-family:Courier New,Courier,monospace;line-height:14px;content:"+";background-color:#0275d8}table.dataTable.dtr-inline.collapsed>tbody>tr.parent>td:first-child:before,table.dataTable.dtr-inline.collapsed>tbody>tr.parent>th:first-child:before{content:"-";background-color:#d33333}table.dataTable.dtr-inline.collapsed.compact>tbody>tr>td:first-child,table.dataTable.dtr-inline.collapsed.compact>tbody>tr>th:first-child{padding-left:27px}table.dataTable.dtr-inline.collapsed.compact>tbody>tr>td:first-child:before,table.dataTable.dtr-inline.collapsed.compact>tbody>tr>th:first-child:before{top:5px;left:4px;height:14px;width:14px;border-radius:14px;line-height:14px;text-indent:3px}table.dataTable.dtr-column>tbody>tr>td.control,table.dataTable.dtr-column>tbody>tr>th.control{position:relative;cursor:pointer}table.dataTable.dtr-column>tbody>tr>td.control:before,table.dataTable.dtr-column>tbody>tr>th.control:before{top:50%;left:50%;height:16px;width:16px;margin-top:-10px;margin-left:-10px;display:block;position:absolute;color:#fff;border:2px solid #fff;border-radius:14px;box-shadow:0 0 3px #444;box-sizing:content-box;text-align:center;text-indent:0!important;font-family:Courier New,Courier,monospace;line-height:14px;content:"+";background-color:#0275d8}table.dataTable.dtr-column>tbody>tr.parent td.control:before,table.dataTable.dtr-column>tbody>tr.parent th.control:before{content:"-";background-color:#d33333}table.dataTable>tbody>tr.child{padding:.5em 1em}table.dataTable>tbody>tr.child:hover{background:transparent!important}table.dataTable>tbody>tr.child ul.dtr-details{display:inline-block;list-style-type:none;margin:0;padding:0}table.dataTable>tbody>tr.child ul.dtr-details>li{border-bottom:1px solid #efefef;padding:.5em 0}table.dataTable>tbody>tr.child ul.dtr-details>li:first-child{padding-top:0}table.dataTable>tbody>tr.child ul.dtr-details>li:last-child{border-bottom:none}table.dataTable>tbody>tr.child span.dtr-title{display:inline-block;min-width:75px;font-weight:700}div.dtr-modal{position:fixed;box-sizing:border-box;top:0;left:0;height:100%;width:100%;z-index:100;padding:10em 1em}div.dtr-modal div.dtr-modal-display{position:absolute;top:0;left:0;bottom:0;right:0;width:50%;height:50%;margin:auto;z-index:102;overflow:auto;background-color:#f5f5f7;border:1px solid #000;border-radius:.5em;box-shadow:0 12px 30px rgba(0,0,0,.6)}div.dtr-modal div.dtr-modal-content{position:relative;padding:1em}div.dtr-modal div.dtr-modal-close{position:absolute;top:6px;right:6px;width:22px;height:22px;border:1px solid #eaeaea;background-color:#f9f9f9;text-align:center;border-radius:3px;cursor:pointer;z-index:12}div.dtr-modal div.dtr-modal-close:hover{background-color:#eaeaea}div.dtr-modal div.dtr-modal-background{position:fixed;top:0;left:0;right:0;bottom:0;z-index:101;background:rgba(0,0,0,.6)}@media screen and (max-width:767px){div.dtr-modal div.dtr-modal-display{width:95%}}div.dtr-bs-modal table.table tr:first-child td{border-top:none}table.dataTable tr.group td{font-weight:700;background-color:#e0e0e0}table.dt-rowReorder-float{position:absolute!important;opacity:.8;table-layout:fixed;outline:2px solid #0275d8;outline-offset:-2px;z-index:2001}tr.dt-rowReorder-moving{outline:2px solid #888;outline-offset:-2px}body.dt-rowReorder-noOverflow{overflow-x:hidden}table.dataTable td.reorder{text-align:center;cursor:move}div.DTS{display:block!important}div.DTS tbody td,div.DTS tbody th{white-space:nowrap}div.DTS div.DTS_Loading{z-index:1}div.DTS div.dataTables_scrollBody{background:repeating-linear-gradient(45deg,#edeeff,#edeeff 10px,#fff 0,#fff 20px)}div.DTS div.dataTables_scrollBody table{z-index:2}div.DTS div.dataTables_length,div.DTS div.dataTables_paginate{display:none}div.DTS div.dataTables_scrollBody table{background-color:#fff}table.dataTable tbody>tr.selected,table.dataTable tbody>tr>.selected{background-color:#0275d8}table.dataTable.display tbody>tr.odd.selected,table.dataTable.display tbody>tr.odd>.selected,table.dataTable.stripe tbody>tr.odd.selected,table.dataTable.stripe tbody>tr.odd>.selected{background-color:#0272d3}table.dataTable.display tbody>tr.selected:hover,table.dataTable.display tbody>tr>.selected:hover,table.dataTable.hover tbody>tr.selected:hover,table.dataTable.hover tbody>tr>.selected:hover{background-color:#0271d0}table.dataTable.display tbody>tr.selected>.sorting_1,table.dataTable.display tbody>tr.selected>.sorting_2,table.dataTable.display tbody>tr.selected>.sorting_3,table.dataTable.display tbody>tr>.selected,table.dataTable.order-column tbody>tr.selected>.sorting_1,table.dataTable.order-column tbody>tr.selected>.sorting_2,table.dataTable.order-column tbody>tr.selected>.sorting_3,table.dataTable.order-column tbody>tr>.selected{background-color:#0273d4}table.dataTable.display tbody>tr.odd.selected>.sorting_1,table.dataTable.order-column.stripe tbody>tr.odd.selected>.sorting_1{background-color:#026fcc}table.dataTable.display tbody>tr.odd.selected>.sorting_2,table.dataTable.order-column.stripe tbody>tr.odd.selected>.sorting_2{background-color:#0270ce}table.dataTable.display tbody>tr.odd.selected>.sorting_3,table.dataTable.order-column.stripe tbody>tr.odd.selected>.sorting_3{background-color:#0270d0}table.dataTable.display tbody>tr.even.selected>.sorting_1,table.dataTable.order-column.stripe tbody>tr.even.selected>.sorting_1{background-color:#0273d4}table.dataTable.display tbody>tr.even.selected>.sorting_2,table.dataTable.order-column.stripe tbody>tr.even.selected>.sorting_2{background-color:#0274d5}table.dataTable.display tbody>tr.even.selected>.sorting_3,table.dataTable.order-column.stripe tbody>tr.even.selected>.sorting_3{background-color:#0275d7}table.dataTable.display tbody>tr.odd>.selected,table.dataTable.order-column.stripe tbody>tr.odd>.selected{background-color:#026fcc}table.dataTable.display tbody>tr.even>.selected,table.dataTable.order-column.stripe tbody>tr.even>.selected{background-color:#0273d4}table.dataTable.display tbody>tr.selected:hover>.sorting_1,table.dataTable.order-column.hover tbody>tr.selected:hover>.sorting_1{background-color:#026bc6}table.dataTable.display tbody>tr.selected:hover>.sorting_2,table.dataTable.order-column.hover tbody>tr.selected:hover>.sorting_2{background-color:#026cc8}table.dataTable.display tbody>tr.selected:hover>.sorting_3,table.dataTable.order-column.hover tbody>tr.selected:hover>.sorting_3{background-color:#026eca}table.dataTable.display tbody>tr:hover>.selected,table.dataTable.display tbody>tr>.selected:hover,table.dataTable.order-column.hover tbody>tr:hover>.selected,table.dataTable.order-column.hover tbody>tr>.selected:hover{background-color:#026bc6}table.dataTable tbody td.select-checkbox,table.dataTable tbody th.select-checkbox{position:relative}table.dataTable tbody td.select-checkbox:after,table.dataTable tbody td.select-checkbox:before,table.dataTable tbody th.select-checkbox:after,table.dataTable tbody th.select-checkbox:before{display:block;position:absolute;top:1.2em;left:50%;width:12px;height:12px;box-sizing:border-box}table.dataTable tbody td.select-checkbox:before,table.dataTable tbody th.select-checkbox:before{content:" ";margin-top:-6px;margin-left:-6px;border:1px solid #000;border-radius:3px}table.dataTable tr.selected td.select-checkbox:after,table.dataTable tr.selected th.select-checkbox:after{content:"\2714";margin-top:-11px;margin-left:-4px;text-align:center;text-shadow:1px 1px #b0bed9,-1px -1px #b0bed9,1px -1px #b0bed9,-1px 1px #b0bed9}div.dataTables_wrapper span.select-info,div.dataTables_wrapper span.select-item{margin-left:.5em}@media screen and (max-width:640px){div.dataTables_wrapper span.select-info,div.dataTables_wrapper span.select-item{margin-left:0;display:block}}table.dataTable tbody td.selected,table.dataTable tbody th.selected,table.dataTable tbody tr.selected{color:#fff}table.dataTable tbody td.selected a,table.dataTable tbody th.selected a,table.dataTable tbody tr.selected a{color:#a2d4ed}@media screen and (max-width:767px){table.dataTable>tbody>tr>td:first-child{padding-left:30px!important}table.dataTable.dtr-inline.collapsed>tbody>tr[role=row]>td:first-child:before,table.dataTable.dtr-inline.collapsed>tbody>tr[role=row]>th:first-child:before{top:50%;margin-top:-9px;left:4px;height:18px;width:18px;display:block;position:absolute;color:#4caf50;border:0 solid #fff;border-radius:14px;box-shadow:0 0 3px #444;box-sizing:content-box;text-align:center;font-family:Courier New,Courier,monospace;line-height:18px;content:"+";background-color:#fff}}svg{touch-action:none}.jvectormap-container{width:100%;height:100%;position:relative;overflow:hidden;touch-action:none}.jvectormap-tip{position:absolute;display:none;color:#555;line-height:1.5em;background:#fff;border:none;border-radius:30px;box-shadow:0 8px 10px 1px rgba(0,0,0,.14),0 3px 14px 2px rgba(0,0,0,.12),0 5px 5px -3px rgba(0,0,0,.2);padding:5px 10px;z-index:1040}.jvectormap-goback,.jvectormap-zoomin,.jvectormap-zoomout{position:absolute;left:10px;border-radius:3px;background:#292929;padding:3px;color:#fff;cursor:pointer;line-height:10px;text-align:center;box-sizing:content-box}.jvectormap-zoomin,.jvectormap-zoomout{width:10px;height:10px}.jvectormap-zoomin{top:10px}.jvectormap-zoomout{top:30px}.jvectormap-goback{bottom:10px;z-index:1000;padding:6px}.jvectormap-spinner{position:absolute;left:0;top:0;right:0;bottom:0;background:50% no-repeat url(data:image/gif;base64,R0lGODlhIAAgAPMAAP///wAAAMbGxoSEhLa2tpqamjY2NlZWVtjY2OTk5Ly8vB4eHgQEBAAAAAAAAAAAACH/C05FVFNDQVBFMi4wAwEAAAAh/hpDcmVhdGVkIHdpdGggYWpheGxvYWQuaW5mbwAh+QQJCgAAACwAAAAAIAAgAAAE5xDISWlhperN52JLhSSdRgwVo1ICQZRUsiwHpTJT4iowNS8vyW2icCF6k8HMMBkCEDskxTBDAZwuAkkqIfxIQyhBQBFvAQSDITM5VDW6XNE4KagNh6Bgwe60smQUB3d4Rz1ZBApnFASDd0hihh12BkE9kjAJVlycXIg7CQIFA6SlnJ87paqbSKiKoqusnbMdmDC2tXQlkUhziYtyWTxIfy6BE8WJt5YJvpJivxNaGmLHT0VnOgSYf0dZXS7APdpB309RnHOG5gDqXGLDaC457D1zZ/V/nmOM82XiHRLYKhKP1oZmADdEAAAh+QQJCgAAACwAAAAAIAAgAAAE6hDISWlZpOrNp1lGNRSdRpDUolIGw5RUYhhHukqFu8DsrEyqnWThGvAmhVlteBvojpTDDBUEIFwMFBRAmBkSgOrBFZogCASwBDEY/CZSg7GSE0gSCjQBMVG023xWBhklAnoEdhQEfyNqMIcKjhRsjEdnezB+A4k8gTwJhFuiW4dokXiloUepBAp5qaKpp6+Ho7aWW54wl7obvEe0kRuoplCGepwSx2jJvqHEmGt6whJpGpfJCHmOoNHKaHx61WiSR92E4lbFoq+B6QDtuetcaBPnW6+O7wDHpIiK9SaVK5GgV543tzjgGcghAgAh+QQJCgAAACwAAAAAIAAgAAAE7hDISSkxpOrN5zFHNWRdhSiVoVLHspRUMoyUakyEe8PTPCATW9A14E0UvuAKMNAZKYUZCiBMuBakSQKG8G2FzUWox2AUtAQFcBKlVQoLgQReZhQlCIJesQXI5B0CBnUMOxMCenoCfTCEWBsJColTMANldx15BGs8B5wlCZ9Po6OJkwmRpnqkqnuSrayqfKmqpLajoiW5HJq7FL1Gr2mMMcKUMIiJgIemy7xZtJsTmsM4xHiKv5KMCXqfyUCJEonXPN2rAOIAmsfB3uPoAK++G+w48edZPK+M6hLJpQg484enXIdQFSS1u6UhksENEQAAIfkECQoAAAAsAAAAACAAIAAABOcQyEmpGKLqzWcZRVUQnZYg1aBSh2GUVEIQ2aQOE+G+cD4ntpWkZQj1JIiZIogDFFyHI0UxQwFugMSOFIPJftfVAEoZLBbcLEFhlQiqGp1Vd140AUklUN3eCA51C1EWMzMCezCBBmkxVIVHBWd3HHl9JQOIJSdSnJ0TDKChCwUJjoWMPaGqDKannasMo6WnM562R5YluZRwur0wpgqZE7NKUm+FNRPIhjBJxKZteWuIBMN4zRMIVIhffcgojwCF117i4nlLnY5ztRLsnOk+aV+oJY7V7m76PdkS4trKcdg0Zc0tTcKkRAAAIfkECQoAAAAsAAAAACAAIAAABO4QyEkpKqjqzScpRaVkXZWQEximw1BSCUEIlDohrft6cpKCk5xid5MNJTaAIkekKGQkWyKHkvhKsR7ARmitkAYDYRIbUQRQjWBwJRzChi9CRlBcY1UN4g0/VNB0AlcvcAYHRyZPdEQFYV8ccwR5HWxEJ02YmRMLnJ1xCYp0Y5idpQuhopmmC2KgojKasUQDk5BNAwwMOh2RtRq5uQuPZKGIJQIGwAwGf6I0JXMpC8C7kXWDBINFMxS4DKMAWVWAGYsAdNqW5uaRxkSKJOZKaU3tPOBZ4DuK2LATgJhkPJMgTwKCdFjyPHEnKxFCDhEAACH5BAkKAAAALAAAAAAgACAAAATzEMhJaVKp6s2nIkolIJ2WkBShpkVRWqqQrhLSEu9MZJKK9y1ZrqYK9WiClmvoUaF8gIQSNeF1Er4MNFn4SRSDARWroAIETg1iVwuHjYB1kYc1mwruwXKC9gmsJXliGxc+XiUCby9ydh1sOSdMkpMTBpaXBzsfhoc5l58Gm5yToAaZhaOUqjkDgCWNHAULCwOLaTmzswadEqggQwgHuQsHIoZCHQMMQgQGubVEcxOPFAcMDAYUA85eWARmfSRQCdcMe0zeP1AAygwLlJtPNAAL19DARdPzBOWSm1brJBi45soRAWQAAkrQIykShQ9wVhHCwCQCACH5BAkKAAAALAAAAAAgACAAAATrEMhJaVKp6s2nIkqFZF2VIBWhUsJaTokqUCoBq+E71SRQeyqUToLA7VxF0JDyIQh/MVVPMt1ECZlfcjZJ9mIKoaTl1MRIl5o4CUKXOwmyrCInCKqcWtvadL2SYhyASyNDJ0uIiRMDjI0Fd30/iI2UA5GSS5UDj2l6NoqgOgN4gksEBgYFf0FDqKgHnyZ9OX8HrgYHdHpcHQULXAS2qKpENRg7eAMLC7kTBaixUYFkKAzWAAnLC7FLVxLWDBLKCwaKTULgEwbLA4hJtOkSBNqITT3xEgfLpBtzE/jiuL04RGEBgwWhShRgQExHBAAh+QQJCgAAACwAAAAAIAAgAAAE7xDISWlSqerNpyJKhWRdlSAVoVLCWk6JKlAqAavhO9UkUHsqlE6CwO1cRdCQ8iEIfzFVTzLdRAmZX3I2SfZiCqGk5dTESJeaOAlClzsJsqwiJwiqnFrb2nS9kmIcgEsjQydLiIlHehhpejaIjzh9eomSjZR+ipslWIRLAgMDOR2DOqKogTB9pCUJBagDBXR6XB0EBkIIsaRsGGMMAxoDBgYHTKJiUYEGDAzHC9EACcUGkIgFzgwZ0QsSBcXHiQvOwgDdEwfFs0sDzt4S6BK4xYjkDOzn0unFeBzOBijIm1Dgmg5YFQwsCMjp1oJ8LyIAACH5BAkKAAAALAAAAAAgACAAAATwEMhJaVKp6s2nIkqFZF2VIBWhUsJaTokqUCoBq+E71SRQeyqUToLA7VxF0JDyIQh/MVVPMt1ECZlfcjZJ9mIKoaTl1MRIl5o4CUKXOwmyrCInCKqcWtvadL2SYhyASyNDJ0uIiUd6GGl6NoiPOH16iZKNlH6KmyWFOggHhEEvAwwMA0N9GBsEC6amhnVcEwavDAazGwIDaH1ipaYLBUTCGgQDA8NdHz0FpqgTBwsLqAbWAAnIA4FWKdMLGdYGEgraigbT0OITBcg5QwPT4xLrROZL6AuQAPUS7bxLpoWidY0JtxLHKhwwMJBTHgPKdEQAACH5BAkKAAAALAAAAAAgACAAAATrEMhJaVKp6s2nIkqFZF2VIBWhUsJaTokqUCoBq+E71SRQeyqUToLA7VxF0JDyIQh/MVVPMt1ECZlfcjZJ9mIKoaTl1MRIl5o4CUKXOwmyrCInCKqcWtvadL2SYhyASyNDJ0uIiUd6GAULDJCRiXo1CpGXDJOUjY+Yip9DhToJA4RBLwMLCwVDfRgbBAaqqoZ1XBMHswsHtxtFaH1iqaoGNgAIxRpbFAgfPQSqpbgGBqUD1wBXeCYp1AYZ19JJOYgH1KwA4UBvQwXUBxPqVD9L3sbp2BNk2xvvFPJd+MFCN6HAAIKgNggY0KtEBAAh+QQJCgAAACwAAAAAIAAgAAAE6BDISWlSqerNpyJKhWRdlSAVoVLCWk6JKlAqAavhO9UkUHsqlE6CwO1cRdCQ8iEIfzFVTzLdRAmZX3I2SfYIDMaAFdTESJeaEDAIMxYFqrOUaNW4E4ObYcCXaiBVEgULe0NJaxxtYksjh2NLkZISgDgJhHthkpU4mW6blRiYmZOlh4JWkDqILwUGBnE6TYEbCgevr0N1gH4At7gHiRpFaLNrrq8HNgAJA70AWxQIH1+vsYMDAzZQPC9VCNkDWUhGkuE5PxJNwiUK4UfLzOlD4WvzAHaoG9nxPi5d+jYUqfAhhykOFwJWiAAAIfkECQoAAAAsAAAAACAAIAAABPAQyElpUqnqzaciSoVkXVUMFaFSwlpOCcMYlErAavhOMnNLNo8KsZsMZItJEIDIFSkLGQoQTNhIsFehRww2CQLKF0tYGKYSg+ygsZIuNqJksKgbfgIGepNo2cIUB3V1B3IvNiBYNQaDSTtfhhx0CwVPI0UJe0+bm4g5VgcGoqOcnjmjqDSdnhgEoamcsZuXO1aWQy8KAwOAuTYYGwi7w5h+Kr0SJ8MFihpNbx+4Erq7BYBuzsdiH1jCAzoSfl0rVirNbRXlBBlLX+BP0XJLAPGzTkAuAOqb0WT5AH7OcdCm5B8TgRwSRKIHQtaLCwg1RAAAOwAAAAAAAAAAAA==)}.jvectormap-legend-title{font-weight:700;font-size:14px;text-align:center}.jvectormap-legend-cnt{position:absolute}.jvectormap-legend-cnt-h{bottom:0;right:0}.jvectormap-legend-cnt-v{top:0;right:0}.jvectormap-legend{background:#000;color:#fff;border-radius:3px}.jvectormap-legend-cnt-h .jvectormap-legend{float:left;margin:0 10px 10px 0;padding:3px 3px 1px}.jvectormap-legend-cnt-h .jvectormap-legend .jvectormap-legend-tick{float:left}.jvectormap-legend-cnt-v .jvectormap-legend{margin:10px 10px 0 0;padding:3px}.jvectormap-legend-cnt-h .jvectormap-legend-tick{width:40px}.jvectormap-legend-cnt-h .jvectormap-legend-tick-sample{height:15px}.jvectormap-legend-cnt-v .jvectormap-legend-tick-sample{height:20px;width:20px;display:inline-block;vertical-align:middle}.jvectormap-legend-tick-text{font-size:12px}.jvectormap-legend-cnt-h .jvectormap-legend-tick-text{text-align:center}.jvectormap-legend-cnt-v .jvectormap-legend-tick-text{display:inline-block;vertical-align:middle;line-height:20px;padding-left:3px}

/*!
 * Datetimepicker for Bootstrap 3
 * ! version : 4.17.37
 * https://github.com/Eonasdan/bootstrap-datetimepicker/
 */.bootstrap-datetimepicker-widget .btn[data-action=clear]:after,.bootstrap-datetimepicker-widget .btn[data-action=decrementHours]:after,.bootstrap-datetimepicker-widget .btn[data-action=decrementMinutes]:after,.bootstrap-datetimepicker-widget .btn[data-action=incrementHours]:after,.bootstrap-datetimepicker-widget .btn[data-action=incrementMinutes]:after,.bootstrap-datetimepicker-widget .btn[data-action=showHours]:after,.bootstrap-datetimepicker-widget .btn[data-action=showMinutes]:after,.bootstrap-datetimepicker-widget .btn[data-action=today]:after,.bootstrap-datetimepicker-widget .btn[data-action=togglePeriod]:after,.bootstrap-datetimepicker-widget .picker-switch:after,.bootstrap-datetimepicker-widget table th.next:after,.bootstrap-datetimepicker-widget table th.prev:after,.sr-only{position:absolute;width:1px;height:1px;margin:-1px;padding:0;overflow:hidden;clip:rect(0,0,0,0);border:0}.bootstrap-datetimepicker-widget{list-style:none}.bootstrap-datetimepicker-widget a:hover{box-shadow:none!important}.bootstrap-datetimepicker-widget a .btn:hover{background-color:transparent}.bootstrap-datetimepicker-widget.dropdown-menu{padding:4px;width:19em}@media (min-width:768px){.bootstrap-datetimepicker-widget.dropdown-menu.timepicker-sbs{width:38em}}@media (min-width:991px){.bootstrap-datetimepicker-widget.dropdown-menu.timepicker-sbs{width:38em}}@media (min-width:1200px){.bootstrap-datetimepicker-widget.dropdown-menu.timepicker-sbs{width:38em}}.bootstrap-datetimepicker-widget.dropdown-menu.bottom:after,.bootstrap-datetimepicker-widget.dropdown-menu.bottom:before{right:auto;left:12px}.bootstrap-datetimepicker-widget.dropdown-menu.top{margin-top:auto;margin-bottom:27px;z-index:1111}.bootstrap-datetimepicker-widget.dropdown-menu.top.open{margin-top:auto;margin-bottom:27px}.bootstrap-datetimepicker-widget.dropdown-menu.pull-right:before{left:auto;right:6px}.bootstrap-datetimepicker-widget.dropdown-menu.pull-right:after{left:auto;right:7px}.bootstrap-datetimepicker-widget .list-unstyled{margin:0}.bootstrap-datetimepicker-widget a[data-action]{padding:0;margin:0;border-width:0;background-color:transparent;color:#9c27b0;box-shadow:none}.bootstrap-datetimepicker-widget a[data-action]:hover{background-color:transparent}.bootstrap-datetimepicker-widget a[data-action]:hover span{background-color:#eee;color:#9c27b0}.bootstrap-datetimepicker-widget a[data-action]:active{box-shadow:none}.bootstrap-datetimepicker-widget .timepicker-hour,.bootstrap-datetimepicker-widget .timepicker-minute,.bootstrap-datetimepicker-widget .timepicker-second{width:40px;height:40px;line-height:40px;font-weight:300;font-size:1.125rem;margin:0;border-radius:50%}.bootstrap-datetimepicker-widget button[data-action]{width:38px;height:38px;margin-right:3px;padding:0}.bootstrap-datetimepicker-widget .btn[data-action=incrementHours]:after{content:"Increment Hours"}.bootstrap-datetimepicker-widget .btn[data-action=incrementMinutes]:after{content:"Increment Minutes"}.bootstrap-datetimepicker-widget .btn[data-action=decrementHours]:after{content:"Decrement Hours"}.bootstrap-datetimepicker-widget .btn[data-action=decrementMinutes]:after{content:"Decrement Minutes"}.bootstrap-datetimepicker-widget .btn[data-action=showHours]:after{content:"Show Hours"}.bootstrap-datetimepicker-widget .btn[data-action=showMinutes]:after{content:"Show Minutes"}.bootstrap-datetimepicker-widget .btn[data-action=togglePeriod]:after{content:"Toggle AM/PM"}.bootstrap-datetimepicker-widget .btn[data-action=clear]:after{content:"Clear the picker"}.bootstrap-datetimepicker-widget .btn[data-action=today]:after{content:"Set the date to today"}.bootstrap-datetimepicker-widget .picker-switch{text-align:center;border-radius:3px;font-size:.875rem}.bootstrap-datetimepicker-widget .picker-switch:after{content:"Toggle Date and Time Screens"}.bootstrap-datetimepicker-widget .picker-switch td{padding:0;margin:0;height:auto;width:auto;line-height:inherit}.bootstrap-datetimepicker-widget .picker-switch td span{line-height:2.5;height:2.5em;width:100%;border-radius:3px;margin:2px 0!important}.bootstrap-datetimepicker-widget table{width:100%;margin:0}.bootstrap-datetimepicker-widget table.table-condensed tr>td,.bootstrap-datetimepicker-widget table td>div,.bootstrap-datetimepicker-widget table th>div{text-align:center}.bootstrap-datetimepicker-widget table th{height:20px;line-height:20px;width:20px;font-weight:500}.bootstrap-datetimepicker-widget table th.picker-switch{width:145px}.bootstrap-datetimepicker-widget table th.disabled,.bootstrap-datetimepicker-widget table th.disabled:hover{background:none;color:#eee;cursor:not-allowed}.bootstrap-datetimepicker-widget table th.next span,.bootstrap-datetimepicker-widget table th.prev span{border-radius:3px;height:27px;width:27px;line-height:28px;font-size:12px;border-radius:50%;text-align:center}.bootstrap-datetimepicker-widget table th.prev:after{content:"Previous Month"}.bootstrap-datetimepicker-widget table th.next:after{content:"Next Month"}.bootstrap-datetimepicker-widget table th.dow{text-align:center;border-bottom:1px solid #eee;font-size:12px;text-transform:uppercase;color:#333;font-weight:400;padding-bottom:5px;padding-top:10px}.bootstrap-datetimepicker-widget table thead tr:first-child th{cursor:pointer}.bootstrap-datetimepicker-widget table thead tr:first-child th.picker-switch:hover,.bootstrap-datetimepicker-widget table thead tr:first-child th:hover span{background:#eee}.bootstrap-datetimepicker-widget table td>div{border-radius:3px;height:54px;line-height:54px;width:54px;text-align:center}.bootstrap-datetimepicker-widget table td.cw>div{font-size:.8em;height:20px;line-height:20px;color:#999}.bootstrap-datetimepicker-widget table td.day>div{height:30px;line-height:30px;width:30px;text-align:center;padding:0;border-radius:50%;position:relative;z-index:-1;color:#3c4858;font-size:.875rem}.bootstrap-datetimepicker-widget table td.hour>div,.bootstrap-datetimepicker-widget table td.minute>div{border-radius:50%}.bootstrap-datetimepicker-widget table td.day:hover>div,.bootstrap-datetimepicker-widget table td.hour:hover>div,.bootstrap-datetimepicker-widget table td.minute:hover>div,.bootstrap-datetimepicker-widget table td.second:hover>div{background:#eee;cursor:pointer}.bootstrap-datetimepicker-widget table td.new>div,.bootstrap-datetimepicker-widget table td.old>div{color:#999}.bootstrap-datetimepicker-widget table td.today>div{position:relative}.bootstrap-datetimepicker-widget table td.today>div:before{content:"";display:inline-block;border:5px solid transparent;border-bottom-color:#9c27b0;position:absolute;bottom:4px;right:4px}.bootstrap-datetimepicker-widget table td.active:hover>div,.bootstrap-datetimepicker-widget table td.active>div{background-color:#9c27b0;color:#fff;box-shadow:0 4px 20px 0 rgba(0,0,0,.14),0 7px 10px -5px rgba(156,39,176,.4)}.bootstrap-datetimepicker-widget table td.active.today:before>div{border-bottom-color:#fff}.bootstrap-datetimepicker-widget table td.disabled:hover>div,.bootstrap-datetimepicker-widget table td.disabled>div{background:none;color:#eee;cursor:not-allowed}.bootstrap-datetimepicker-widget table td span{display:inline-block;width:40px;height:40px;line-height:40px;margin:3px;cursor:pointer;border-radius:50%;text-align:center}.bootstrap-datetimepicker-widget table td span:hover{background:#eee}.bootstrap-datetimepicker-widget table td span.active{background-color:#9c27b0;color:#fff}.bootstrap-datetimepicker-widget table td span.old{color:#999}.bootstrap-datetimepicker-widget table td span.disabled,.bootstrap-datetimepicker-widget table td span.disabled:hover{background:none;color:#eee;cursor:not-allowed}.bootstrap-datetimepicker-widget .timepicker-hours span,.bootstrap-datetimepicker-widget .timepicker-minutes span,.bootstrap-datetimepicker-widget .timepicker-picker span{border-radius:50%!important}.bootstrap-datetimepicker-widget.usetwentyfour td.hour{height:27px;line-height:27px}.input-group.date .input-group-addon{cursor:pointer}.table-condensed>tbody>tr>td,.table-condensed>tbody>tr>th,.table-condensed>tfoot>tr>td,.table-condensed>tfoot>tr>th,.table-condensed>thead>tr>td,.table-condensed>thead>tr>th{padding:1px;text-align:center;z-index:1;cursor:pointer}.btn-file{position:relative;overflow:hidden;vertical-align:middle}.btn-file>input{position:absolute;top:0;right:0;width:100%;height:100%;margin:0;font-size:23px;cursor:pointer;filter:alpha(opacity=0);opacity:0;direction:ltr}.fileinput{display:inline-block;margin-bottom:9px}.fileinput .form-control{display:inline-block;padding-top:7px;padding-bottom:5px;margin-bottom:0;vertical-align:middle;cursor:text}.fileinput .thumbnail{display:inline-block;margin-bottom:10px;overflow:hidden;text-align:center;vertical-align:middle;max-width:250px;box-shadow:0 10px 30px -12px rgba(0,0,0,.42),0 4px 25px 0 rgba(0,0,0,.12),0 8px 10px -5px rgba(0,0,0,.2)}.fileinput .thumbnail.img-circle{border-radius:50%;max-width:100px}.fileinput .thumbnail>img{max-height:100%;width:100%}.fileinput .btn{vertical-align:middle}.fileinput-exists .fileinput-new,.fileinput-new .fileinput-exists{display:none}.fileinput-inline .fileinput-controls{display:inline}.fileinput-filename{display:inline-block;overflow:hidden;vertical-align:middle}.form-control .fileinput-filename{vertical-align:bottom}.fileinput.input-group{display:table}.fileinput.input-group>*{position:relative;z-index:2}.fileinput.input-group>.btn-file{z-index:1}.fileinput-new.input-group .btn-file,.fileinput-new .input-group .btn-file{border-radius:0 4px 4px 0}.fileinput-new.input-group .btn-file.btn-sm,.fileinput-new .input-group .btn-file.btn-sm,.fileinput-new.input-group .btn-file.btn-xs,.fileinput-new .input-group .btn-file.btn-xs,.fileinput-new.input-group .btn-group-sm>.btn-file.btn,.fileinput-new .input-group .btn-group-sm>.btn-file.btn{border-radius:0 3px 3px 0}.fileinput-new.input-group .btn-file.btn-lg,.fileinput-new .input-group .btn-file.btn-lg,.fileinput-new.input-group .btn-group-lg>.btn-file.btn,.fileinput-new .input-group .btn-group-lg>.btn-file.btn{border-radius:0 6px 6px 0}.form-group.has-warning .fileinput .fileinput-preview{color:#ff9800}.form-group.has-warning .fileinput .thumbnail{border-color:#ff9800}.form-group.has-error .fileinput .fileinput-preview{color:#f44336}.form-group.has-error .fileinput .thumbnail{border-color:#f44336}.form-group.has-success .fileinput .fileinput-preview{color:#4caf50}.form-group.has-success .fileinput .thumbnail{border-color:#4caf50}.input-group-addon:not(:first-child){border-left:0}.thumbnail{border:0 none;border-radius:4px;padding:0}

/*!
 * FullCalendar v3.0.1 Stylesheet
 * Docs & License: http://fullcalendar.io/
 * (c) 2016 Adam Shaw
 */.fc{direction:ltr;text-align:left}.fc-rtl{text-align:right}body .fc{font-size:1em}.fc-unthemed .fc-content,.fc-unthemed .fc-divider,.fc-unthemed .fc-list-heading td,.fc-unthemed .fc-list-view,.fc-unthemed .fc-popover,.fc-unthemed .fc-row,.fc-unthemed tbody,.fc-unthemed td,.fc-unthemed th,.fc-unthemed thead{border-color:#ddd}.fc-unthemed .fc-popover{background-color:#fff}.fc-unthemed .fc-divider,.fc-unthemed .fc-list-heading td,.fc-unthemed .fc-popover .fc-header{background:#999}.fc-unthemed .fc-popover .fc-header .fc-close{color:#999}.fc-highlight{background:#bce8f1;opacity:.3}.fc-bgevent{background:#8fdf82;opacity:.3}.fc-nonbusiness{background:#d7d7d7}.fc-icon{display:inline-block;height:1em;line-height:1em;font-size:1em;text-align:center;overflow:hidden;font-family:Courier New,Courier,monospace;-webkit-touch-callout:none;-webkit-user-select:none;-moz-user-select:none;-ms-user-select:none;user-select:none}.fc-icon:after{position:relative}.fc-icon-left-single-arrow:after{content:"\02039";font-weight:700;font-size:200%;top:-7%}.fc-icon-right-single-arrow:after{content:"\0203A";font-weight:700;font-size:200%;top:-7%}.fc-icon-left-double-arrow:after{content:"\000AB";font-size:160%;top:-7%}.fc-icon-right-double-arrow:after{content:"\000BB";font-size:160%;top:-7%}.fc-icon-left-triangle:after{content:"\25C4";font-size:125%;top:3%}.fc-icon-right-triangle:after{content:"\25BA";font-size:125%;top:3%}.fc-icon-down-triangle:after{content:"\25BC";font-size:125%;top:2%}.fc-icon-x:after{content:"\000D7";font-size:200%;top:6%}.fc button{border:none;border-radius:30px;position:relative;padding:6px 12px;font-weight:400;letter-spacing:0;will-change:box-shadow,transform;transition:box-shadow .2s cubic-bezier(.4,0,1,1),background-color .2s cubic-bezier(.4,0,.2,1)}.fc button::-moz-focus-inner{border:0}.fc button,.fc button.btn-primary{box-shadow:0 2px 2px 0 rgba(156,39,176,.14),0 3px 1px -2px rgba(156,39,176,.2),0 1px 5px 0 rgba(156,39,176,.12)}.fc button,.fc button.active,.fc button.active:focus,.fc button.active:hover,.fc button.btn-primary,.fc button.btn-primary.active,.fc button.btn-primary.active:focus,.fc button.btn-primary.active:hover,.fc button.btn-primary:active,.fc button.btn-primary:active:focus,.fc button.btn-primary:active:hover,.fc button.btn-primary:focus,.fc button.btn-primary:hover,.fc button:active,.fc button:active:focus,.fc button:active:hover,.fc button:focus,.fc button:hover,.open>.fc button.btn-primary.dropdown-toggle,.open>.fc button.btn-primary.dropdown-toggle:focus,.open>.fc button.btn-primary.dropdown-toggle:hover,.open>.fc button.dropdown-toggle,.open>.fc button.dropdown-toggle:focus,.open>.fc button.dropdown-toggle:hover{background-color:#9c27b0;color:#fff}.fc button.btn-primary:active,.fc button.btn-primary:focus,.fc button.btn-primary:hover,.fc button:active,.fc button:focus,.fc button:hover{box-shadow:0 14px 26px -12px rgba(156,39,176,.42),0 4px 23px 0 rgba(0,0,0,.12),0 8px 10px -5px rgba(156,39,176,.2)}.fc button.btn-primary.disabled,.fc button.btn-primary.disabled.active,.fc button.btn-primary.disabled.focus,.fc button.btn-primary.disabled:active,.fc button.btn-primary.disabled:focus,.fc button.btn-primary.disabled:hover,.fc button.btn-primary:disabled,.fc button.btn-primary:disabled.active,.fc button.btn-primary:disabled.focus,.fc button.btn-primary:disabled:active,.fc button.btn-primary:disabled:focus,.fc button.btn-primary:disabled:hover,.fc button.btn-primary[disabled],.fc button.btn-primary[disabled].active,.fc button.btn-primary[disabled].focus,.fc button.btn-primary[disabled]:active,.fc button.btn-primary[disabled]:focus,.fc button.btn-primary[disabled]:hover,.fc button.disabled,.fc button.disabled.active,.fc button.disabled.focus,.fc button.disabled:active,.fc button.disabled:focus,.fc button.disabled:hover,.fc button:disabled,.fc button:disabled.active,.fc button:disabled.focus,.fc button:disabled:active,.fc button:disabled:focus,.fc button:disabled:hover,.fc button[disabled],.fc button[disabled].active,.fc button[disabled].focus,.fc button[disabled]:active,.fc button[disabled]:focus,.fc button[disabled]:hover,fieldset[disabled] .fc button,fieldset[disabled] .fc button.active,fieldset[disabled] .fc button.btn-primary,fieldset[disabled] .fc button.btn-primary.active,fieldset[disabled] .fc button.btn-primary.focus,fieldset[disabled] .fc button.btn-primary:active,fieldset[disabled] .fc button.btn-primary:focus,fieldset[disabled] .fc button.btn-primary:hover,fieldset[disabled] .fc button.focus,fieldset[disabled] .fc button:active,fieldset[disabled] .fc button:focus,fieldset[disabled] .fc button:hover{box-shadow:none}.fc button.btn-primary.btn-simple,.fc button.btn-simple{background-color:transparent;color:#9c27b0;box-shadow:none}.fc button.btn-primary.btn-simple:active,.fc button.btn-primary.btn-simple:focus,.fc button.btn-primary.btn-simple:hover,.fc button.btn-simple:active,.fc button.btn-simple:focus,.fc button.btn-simple:hover{background-color:transparent;color:#9c27b0}.fc button[disabled],.fc button[disabled]:focus,.fc button[disabled]:hover{cursor:default;background-color:#999;border-color:#999;box-shadow:0 2px 2px 0 hsla(0,0%,60%,.14),0 3px 1px -2px hsla(0,0%,60%,.2),0 1px 5px 0 hsla(0,0%,60%,.12)}.fc-state-default{border:1px solid}.fc button .fc-icon{position:relative;top:-.05em;margin:0 .2em;vertical-align:middle}.fc-state-active,.fc-state-disabled,.fc-state-down,.fc-state-hover{color:#333;background-color:#e6e6e6}.fc-state-hover{color:#333;text-decoration:none;background-position:0 -15px;transition:background-position .1s linear}.fc-state-active,.fc-state-down{background-color:#ccc;background-image:none;box-shadow:inset 0 2px 4px rgba(0,0,0,.15),0 1px 2px rgba(0,0,0,.05)}.fc-state-disabled{cursor:default;background-image:none;opacity:.65;box-shadow:none}.fc-button-group{display:inline-block}.fc .fc-button-group>*{float:left;margin:0 0 0 2px}.fc .fc-button-group>:first-child{margin-left:0}.fc-popover{position:absolute;box-shadow:0 2px 6px rgba(0,0,0,.15)}.fc-popover .fc-header{padding:2px 4px}.fc-popover .fc-header .fc-title{margin:0 2px}.fc-popover .fc-header .fc-close{cursor:pointer}.fc-ltr .fc-popover .fc-header .fc-title,.fc-rtl .fc-popover .fc-header .fc-close{float:left}.fc-ltr .fc-popover .fc-header .fc-close,.fc-rtl .fc-popover .fc-header .fc-title{float:right}.fc-unthemed .fc-popover{border-width:1px;border-style:solid}.fc-unthemed .fc-popover .fc-header .fc-close{font-size:.9em;margin-top:2px}.fc-popover>.ui-widget-header+.ui-widget-content{border-top:0}.fc-divider{border-style:solid;border-width:1px}hr.fc-divider{height:0;margin:0;padding:0 0 2px;border-width:1px 0}.fc-clear{clear:both}.fc-bg,.fc-bgevent-skeleton,.fc-helper-skeleton,.fc-highlight-skeleton{position:absolute;top:0;left:0;right:0}.fc-bg{bottom:0}.fc-bg table{height:100%}.fc table{width:100%;box-sizing:border-box;table-layout:fixed;border-collapse:collapse;border-spacing:0;font-size:1em}.fc th{text-align:center}.fc td,.fc th{border-style:solid;border-width:1px;padding:0;vertical-align:top}.fc td.fc-today{border-style:double}a[data-goto]{cursor:pointer}a[data-goto]:hover{text-decoration:underline}.fc .fc-row{border-style:solid;border-width:0}.fc-row table{border-left:0 hidden transparent;border-right:0 hidden transparent;border-bottom:0 hidden transparent}.fc-row:first-child table{border-top:0 hidden transparent}.fc-row{position:relative}.fc-row .fc-bg{z-index:1}.fc-row .fc-bgevent-skeleton,.fc-row .fc-highlight-skeleton{bottom:0}.fc-row .fc-bgevent-skeleton table,.fc-row .fc-highlight-skeleton table{height:100%}.fc-row .fc-bgevent-skeleton td,.fc-row .fc-highlight-skeleton td{border-color:transparent}.fc-row .fc-bgevent-skeleton{z-index:2}.fc-row .fc-highlight-skeleton{z-index:3}.fc-row .fc-content-skeleton{position:relative;z-index:4;padding-bottom:2px}.fc-row .fc-helper-skeleton{z-index:5}.fc-row .fc-content-skeleton td,.fc-row .fc-helper-skeleton td{background:none;border-color:transparent;border-bottom:0}.fc-row .fc-content-skeleton tbody td,.fc-row .fc-helper-skeleton tbody td{border-top:0}.fc-scroller{-webkit-overflow-scrolling:touch}.fc-scroller>.fc-day-grid,.fc-scroller>.fc-time-grid{position:relative;width:100%}.fc-event{position:relative;display:block;font-size:.85em;line-height:1.3;border-radius:2px;background-color:#4caf50;box-shadow:0 4px 20px 0 rgba(0,0,0,.14),0 7px 10px -5px rgba(76,175,80,.4);font-weight:400}.fc-event.event-azure{background-color:#00bcd4;box-shadow:0 4px 20px 0 rgba(0,0,0,.14),0 7px 10px -5px rgba(0,188,212,.4)}.fc-event.event-green{background-color:#4caf50;box-shadow:0 4px 20px 0 rgba(0,0,0,.14),0 7px 10px -5px rgba(76,175,80,.4)}.fc-event.event-orange{background-color:#ff9800;box-shadow:0 4px 20px 0 rgba(0,0,0,.14),0 7px 10px -5px rgba(255,152,0,.4)}.fc-event.event-red{background-color:#f44336;box-shadow:0 4px 20px 0 rgba(0,0,0,.14),0 7px 10px -5px rgba(244,67,54,.4)}.fc-event.event-rose{background-color:#e91e63;box-shadow:0 4px 20px 0 rgba(0,0,0,.14),0 7px 10px -5px rgba(233,30,99,.4)}.fc-event.event-default{background-color:#999;box-shadow:0 4px 20px 0 rgba(0,0,0,.14),0 7px 10px -5px hsla(0,0%,60%,.4)}.fc-event-dot{background-color:#3a87ad}.fc-event,.fc-event:hover,.ui-widget .fc-event{color:#fff;text-decoration:none}.fc-event.fc-draggable,.fc-event[href]{cursor:pointer}.fc-not-allowed,.fc-not-allowed .fc-event{cursor:not-allowed}.fc-event .fc-bg{z-index:1;background:#fff;opacity:.25}.fc-event .fc-content{position:relative;z-index:2}.fc-event .fc-resizer{position:absolute;z-index:4;display:none}.fc-event.fc-allow-mouse-resize .fc-resizer,.fc-event.fc-selected .fc-resizer{display:block}.fc-event.fc-selected .fc-resizer:before{content:"";position:absolute;z-index:9999;top:50%;left:50%;width:40px;height:40px;margin-left:-20px;margin-top:-20px}.fc-event.fc-selected{z-index:9999!important;box-shadow:0 2px 5px rgba(0,0,0,.2)}.fc-event.fc-selected.fc-dragging{box-shadow:0 2px 7px rgba(0,0,0,.3)}.fc-h-event.fc-selected:before{content:"";position:absolute;z-index:3;top:-10px;bottom:-10px;left:0;right:0}.fc-ltr .fc-h-event.fc-not-start,.fc-rtl .fc-h-event.fc-not-end{margin-left:0;border-left-width:0;padding-left:1px;border-top-left-radius:0;border-bottom-left-radius:0}.fc-ltr .fc-h-event.fc-not-end,.fc-rtl .fc-h-event.fc-not-start{margin-right:0;border-right-width:0;padding-right:1px;border-top-right-radius:0;border-bottom-right-radius:0}.fc-ltr .fc-h-event .fc-start-resizer,.fc-rtl .fc-h-event .fc-end-resizer{cursor:w-resize;left:-1px}.fc-ltr .fc-h-event .fc-end-resizer,.fc-rtl .fc-h-event .fc-start-resizer{cursor:e-resize;right:-1px}.fc-h-event.fc-allow-mouse-resize .fc-resizer{width:7px;top:-1px;bottom:-1px}.fc-h-event.fc-selected .fc-resizer{border-radius:4px;border-width:1px;width:6px;height:6px;border-style:solid;border-color:inherit;background:#fff;top:50%;margin-top:-4px}.fc-ltr .fc-h-event.fc-selected .fc-start-resizer,.fc-rtl .fc-h-event.fc-selected .fc-end-resizer{margin-left:-4px}.fc-ltr .fc-h-event.fc-selected .fc-end-resizer,.fc-rtl .fc-h-event.fc-selected .fc-start-resizer{margin-right:-4px}.fc-day-grid-event{margin:2px 5px 0;padding:0 1px}tr:first-child>td>.fc-day-grid-event{margin-top:2px}.fc-day-grid-event.fc-selected:after{content:"";position:absolute;z-index:1;top:-1px;right:-1px;bottom:-1px;left:-1px;background:#000;opacity:.25}.fc-day-grid-event .fc-content{white-space:nowrap;overflow:hidden;color:#fff}.fc-day-grid-event .fc-time{font-weight:700}.fc-ltr .fc-day-grid-event.fc-allow-mouse-resize .fc-start-resizer,.fc-rtl .fc-day-grid-event.fc-allow-mouse-resize .fc-end-resizer{margin-left:-2px}.fc-ltr .fc-day-grid-event.fc-allow-mouse-resize .fc-end-resizer,.fc-rtl .fc-day-grid-event.fc-allow-mouse-resize .fc-start-resizer{margin-right:-2px}a.fc-more{margin:1px 3px;font-size:.85em;cursor:pointer;text-decoration:none}a.fc-more:hover{text-decoration:underline}.fc-limited{display:none}.fc-day-grid .fc-row{z-index:1}.fc-more-popover{z-index:2;width:220px}.fc-more-popover .fc-event-container{padding:10px}.fc-now-indicator{position:absolute;border:0 solid red}.fc-unselectable{-webkit-user-select:none;-moz-user-select:none;-ms-user-select:none;user-select:none;-webkit-touch-callout:none;-webkit-tap-highlight-color:rgba(0,0,0,0)}.fc-toolbar{text-align:center;margin-bottom:1em}.fc-toolbar .fc-left{float:left}.fc-toolbar .fc-left h2{color:rgba(0,0,0,.87);font-weight:300}.fc-toolbar .fc-right{float:right}.fc-toolbar .fc-center{display:inline-block}.fc .fc-toolbar>*>*{float:left;margin-left:.75em}.fc .fc-toolbar>*>:first-child{margin-left:0}.fc-toolbar h2{margin:0;font-size:1.8em}.fc-toolbar button{position:relative}.fc-toolbar .fc-state-hover,.fc-toolbar .ui-state-hover{z-index:2}.fc-toolbar .fc-state-down{z-index:3}.fc-toolbar .fc-state-active,.fc-toolbar .ui-state-active{z-index:4}.fc-toolbar button:focus{z-index:5}.fc-view-container *,.fc-view-container :after,.fc-view-container :before{box-sizing:content-box}.fc-view,.fc-view>table{position:relative;z-index:1}.fc-basicDay-view .fc-content-skeleton,.fc-basicWeek-view .fc-content-skeleton{padding-bottom:1em}.fc-basic-view .fc-body .fc-row{min-height:4em}.fc-row.fc-rigid{overflow:hidden}.fc-row.fc-rigid .fc-content-skeleton{position:absolute;top:0;left:0;right:0}.fc-day-top.fc-other-month{opacity:.3}.fc-basic-view .fc-day-number,.fc-basic-view .fc-week-number{padding:2px}.fc-basic-view th.fc-day-number,.fc-basic-view th.fc-week-number{padding:0 2px}.fc-ltr .fc-basic-view .fc-day-top .fc-day-number{float:right}.fc-rtl .fc-basic-view .fc-day-top .fc-day-number{float:left}.fc-ltr .fc-basic-view .fc-day-top .fc-week-number{float:left;border-radius:0 0 3px 0}.fc-rtl .fc-basic-view .fc-day-top .fc-week-number{float:right;border-radius:0 0 0 3px}.fc-basic-view .fc-day-top .fc-week-number{min-width:1.5em;text-align:center;background-color:#f2f2f2;color:gray}.fc-basic-view td.fc-week-number{text-align:center}.fc-basic-view td.fc-week-number>*{display:inline-block;min-width:1.25em}.fc-agenda-view .fc-day-grid{position:relative;z-index:2}.fc-agenda-view .fc-day-grid .fc-row{min-height:3em}.fc-agenda-view .fc-day-grid .fc-row .fc-content-skeleton{padding-bottom:1em}.fc .fc-axis{vertical-align:middle;padding:0 4px;white-space:nowrap}.fc-ltr .fc-axis{text-align:right}.fc-rtl .fc-axis{text-align:left}.ui-widget td.fc-axis{font-weight:400}.fc-time-grid,.fc-time-grid-container{position:relative;z-index:1}.fc-time-grid{min-height:100%}.fc-time-grid table{border:0 hidden transparent}.fc-time-grid>.fc-bg{z-index:1}.fc-time-grid .fc-slats,.fc-time-grid>hr{position:relative;z-index:2}.fc-time-grid .fc-content-col{position:relative}.fc-time-grid .fc-content-skeleton{position:absolute;z-index:3;top:0;left:0;right:0}.fc-time-grid .fc-business-container{position:relative;z-index:1}.fc-time-grid .fc-bgevent-container{position:relative;z-index:2}.fc-time-grid .fc-highlight-container{z-index:3}.fc-time-grid .fc-event-container{position:relative;z-index:4}.fc-time-grid .fc-now-indicator-line{z-index:5}.fc-time-grid .fc-helper-container{position:relative;z-index:6}.fc-time-grid .fc-slats td{height:1.5em;border-bottom:0}.fc-time-grid .fc-slats .fc-minor td{border-top-style:dotted}.fc-time-grid .fc-slats .ui-widget-content{background:none}.fc-time-grid .fc-highlight-container{position:relative}.fc-time-grid .fc-highlight{position:absolute;left:0;right:0}.fc-ltr .fc-time-grid .fc-event-container{margin:0 2.5% 0 2px}.fc-rtl .fc-time-grid .fc-event-container{margin:0 2px 0 2.5%}.fc-time-grid .fc-bgevent,.fc-time-grid .fc-event{position:absolute;z-index:1}.fc-time-grid .fc-bgevent{left:0;right:0}.fc-v-event.fc-not-start{border-top-width:0;padding-top:1px;border-top-left-radius:0;border-top-right-radius:0}.fc-v-event.fc-not-end{border-bottom-width:0;padding-bottom:1px;border-bottom-left-radius:0;border-bottom-right-radius:0}.fc-time-grid-event{overflow:hidden}.fc-time-grid-event.fc-selected{overflow:visible}.fc-time-grid-event.fc-selected .fc-bg{display:none}.fc-time-grid-event .fc-content{overflow:hidden}.fc-time-grid-event .fc-time,.fc-time-grid-event .fc-title{padding:0 1px}.fc-time-grid-event .fc-time{font-size:.85em;white-space:nowrap}.fc-time-grid-event.fc-short .fc-content{white-space:nowrap}.fc-time-grid-event.fc-short .fc-time,.fc-time-grid-event.fc-short .fc-title{display:inline-block;vertical-align:top}.fc-time-grid-event.fc-short .fc-time span{display:none}.fc-time-grid-event.fc-short .fc-time:before{content:attr(data-start)}.fc-time-grid-event.fc-short .fc-time:after{content:"\000A0-\000A0"}.fc-time-grid-event.fc-short .fc-title{font-size:.85em;padding:0}.fc-time-grid-event.fc-allow-mouse-resize .fc-resizer{left:0;right:0;bottom:0;height:8px;overflow:hidden;line-height:8px;font-size:11px;font-family:monospace;text-align:center;cursor:s-resize}.fc-time-grid-event.fc-allow-mouse-resize .fc-resizer:after{content:"="}.fc-time-grid-event.fc-selected .fc-resizer{border-radius:5px;border-width:1px;width:8px;height:8px;border-style:solid;border-color:inherit;background:#fff;left:50%;margin-left:-5px;bottom:-5px}.fc-time-grid .fc-now-indicator-line{border-top-width:1px;left:0;right:0}.fc-time-grid .fc-now-indicator-arrow{margin-top:-5px}.fc-ltr .fc-time-grid .fc-now-indicator-arrow{left:0;border-width:5px 0 5px 6px;border-top-color:transparent;border-bottom-color:transparent}.fc-rtl .fc-time-grid .fc-now-indicator-arrow{right:0;border-width:5px 6px 5px 0;border-top-color:transparent;border-bottom-color:transparent}.fc-event-dot{display:inline-block;width:10px;height:10px;border-radius:5px}.fc-rtl .fc-list-view{direction:rtl}.fc-list-view{border-width:1px;border-style:solid}.fc .fc-list-table{table-layout:auto}.fc-list-table td{border-width:1px 0 0;padding:8px 14px}.fc-list-table tr:first-child td{border-top-width:0}.fc-list-heading{border-bottom-width:1px}.fc-list-heading td{font-weight:700}.fc-ltr .fc-list-heading-main{float:left}.fc-ltr .fc-list-heading-alt,.fc-rtl .fc-list-heading-main{float:right}.fc-rtl .fc-list-heading-alt{float:left}.fc-list-item.fc-has-url{cursor:pointer}.fc-list-item:hover td{background-color:#f5f5f5}.fc-list-item-marker,.fc-list-item-time{white-space:nowrap;width:1px}.fc-ltr .fc-list-item-marker{padding-right:0}.fc-rtl .fc-list-item-marker{padding-left:0}.fc-list-item-title a{text-decoration:none;color:inherit}.fc-list-item-title a[href]:hover{text-decoration:underline}.fc-list-empty-wrap2{position:absolute;top:0;left:0;right:0;bottom:0}.fc-list-empty-wrap1{width:100%;height:100%;display:table}.fc-list-empty{display:table-cell;vertical-align:middle;text-align:center}.fc-unthemed .fc-list-empty{background-color:#eee}.card-calendar table td{text-align:right}.card-calendar .card-body{padding:0!important}.card-calendar .fc-toolbar{padding-top:20px;padding-left:20px;padding-right:20px}.card-calendar .fc td:first-child{border-left:0}.card-calendar .fc td:last-child{border-right:0}.card-calendar .fc-basic-view td:last-child.fc-day-number,.card-calendar .fc-basic-view td:last-child.fc-week-number span{padding-right:20px}.card-calendar .fc .fc-day-header:last-child{padding-right:15px}.card-calendar .fc .fc-widget-header{border:0}.card-calendar .fc .fc-widget-header .fc-title{color:#fff}.card-calendar .fc th{text-align:right;color:#999}.card-calendar .title{margin-top:-9px}.card-calendar .fc .fc-body .fc-widget-content,.card-calendar .fc .fc-row:last-child td{border-bottom:0}.card-wizard{min-height:410px;box-shadow:0 16px 24px 2px rgba(0,0,0,.14),0 6px 30px 5px rgba(0,0,0,.12),0 8px 10px -5px rgba(0,0,0,.2);opacity:0}.card-wizard.active{opacity:1}.card-wizard .picture-container{position:relative;cursor:pointer;text-align:center}.card-wizard .wizard-navigation{position:relative}.card-wizard .picture{width:106px;height:106px;background-color:#999;border:4px solid #ccc;color:#fff;border-radius:50%;margin:5px auto;overflow:hidden;transition:all .2s;-webkit-transition:all .2s}.card-wizard .picture:hover{border-color:#2ca8ff}.card-wizard .moving-tab{position:absolute;text-align:center;padding:12px;font-size:12px;text-transform:uppercase;-webkit-font-smoothing:subpixel-antialiased;top:-6px;left:0;border-radius:4px;color:#fff;cursor:pointer;font-weight:500}.card-wizard[data-color=purple] .moving-tab{background-color:#9c27b0;box-shadow:0 4px 20px 0 rgba(0,0,0,.14),0 7px 10px -5px rgba(156,39,176,.4)}.card-wizard[data-color=purple] .picture:hover{border-color:#9c27b0}.card-wizard[data-color=purple] .choice.active .icon,.card-wizard[data-color=purple] .choice:hover .icon{border-color:#9c27b0;color:#9c27b0}.card-wizard[data-color=purple] .checkbox input[type=checkbox]:checked+.checkbox-material .check,.card-wizard[data-color=purple] .radio input[type=radio]:checked~.check{background-color:#9c27b0}.card-wizard[data-color=purple] .radio input[type=radio]:checked~.circle{border-color:#9c27b0}.card-wizard[data-color=green] .moving-tab{background-color:#4caf50;box-shadow:0 4px 20px 0 rgba(0,0,0,.14),0 7px 10px -5px rgba(76,175,80,.4)}.card-wizard[data-color=green] .picture:hover{border-color:#4caf50}.card-wizard[data-color=green] .choice.active .icon,.card-wizard[data-color=green] .choice:hover .icon{border-color:#4caf50;color:#4caf50}.card-wizard[data-color=green] .checkbox input[type=checkbox]:checked+.checkbox-material .check,.card-wizard[data-color=green] .radio input[type=radio]:checked~.check{background-color:#4caf50}.card-wizard[data-color=green] .radio input[type=radio]:checked~.circle{border-color:#4caf50}.card-wizard[data-color=blue] .moving-tab{background-color:#00bcd4;box-shadow:0 4px 20px 0 rgba(0,0,0,.14),0 7px 10px -5px rgba(0,188,212,.4)}.card-wizard[data-color=blue] .picture:hover{border-color:#00bcd4}.card-wizard[data-color=blue] .choice.active .icon,.card-wizard[data-color=blue] .choice:hover .icon{border-color:#00bcd4;color:#00bcd4}.card-wizard[data-color=blue] .checkbox input[type=checkbox]:checked+.checkbox-material .check,.card-wizard[data-color=blue] .radio input[type=radio]:checked~.check{background-color:#00bcd4}.card-wizard[data-color=blue] .radio input[type=radio]:checked~.circle{border-color:#00bcd4}.card-wizard[data-color=orange] .moving-tab{background-color:#ff9800;box-shadow:0 4px 20px 0 rgba(0,0,0,.14),0 7px 10px -5px rgba(255,152,0,.4)}.card-wizard[data-color=orange] .picture:hover{border-color:#ff9800}.card-wizard[data-color=orange] .choice.active .icon,.card-wizard[data-color=orange] .choice:hover .icon{border-color:#ff9800;color:#ff9800}.card-wizard[data-color=orange] .checkbox input[type=checkbox]:checked+.checkbox-material .check,.card-wizard[data-color=orange] .radio input[type=radio]:checked~.check{background-color:#ff9800}.card-wizard[data-color=orange] .radio input[type=radio]:checked~.circle{border-color:#ff9800}.card-wizard[data-color=red] .moving-tab{background-color:#f44336;box-shadow:0 4px 20px 0 rgba(0,0,0,.14),0 7px 10px -5px rgba(244,67,54,.4)}.card-wizard[data-color=red] .picture:hover{border-color:#f44336}.card-wizard[data-color=red] .choice.active .icon,.card-wizard[data-color=red] .choice:hover .icon{border-color:#f44336;color:#f44336}.card-wizard[data-color=red] .checkbox input[type=checkbox]:checked+.checkbox-material .check,.card-wizard[data-color=red] .radio input[type=radio]:checked~.check{background-color:#f44336}.card-wizard[data-color=red] .radio input[type=radio]:checked~.circle{border-color:#f44336}.card-wizard[data-color=rose] .moving-tab{background-color:#e91e63;box-shadow:0 4px 20px 0 rgba(0,0,0,.14),0 7px 10px -5px rgba(233,30,99,.4)}.card-wizard[data-color=rose] .picture:hover{border-color:#e91e63}.card-wizard[data-color=rose] .choice.active .icon,.card-wizard[data-color=rose] .choice:hover .icon{border-color:#e91e63;color:#e91e63}.card-wizard[data-color=rose] .checkbox input[type=checkbox]:checked+.checkbox-material .check,.card-wizard[data-color=rose] .radio input[type=radio]:checked~.check{background-color:#e91e63}.card-wizard[data-color=rose] .radio input[type=radio]:checked~.circle{border-color:#e91e63}.card-wizard .picture input[type=file]{cursor:pointer;display:block;height:100%;left:0;opacity:0!important;position:absolute;top:0;width:100%}.card-wizard .picture-src{width:100%}.card-wizard .tab-content{min-height:340px;padding:20px 15px}.card-wizard .wizard-footer{padding:0 15px}.card-wizard .wizard-footer .checkbox{margin-top:16px}.card-wizard .disabled{display:none}.card-wizard .wizard-header{text-align:center;padding:25px 0 35px}.card-wizard .wizard-header h5{margin:5px 0 0}.card-wizard .nav-pills>li{text-align:center}.card-wizard .btn{text-transform:uppercase}.card-wizard .info-text{text-align:center;font-weight:300;margin:10px 0 30px}.card-wizard .choice{text-align:center;cursor:pointer;margin-top:20px}.card-wizard .choice[disabled]{pointer-events:none;cursor:not-allowed;opacity:.26}.card-wizard .choice .icon{text-align:center;vertical-align:middle;height:116px;width:116px;border-radius:50%;color:#999;margin:0 auto 20px;border:4px solid #ccc;transition:all .2s;-webkit-transition:all .2s}.card-wizard .choice i{font-size:40px;line-height:111px}.card-wizard .choice.active .icon,.card-wizard .choice:hover .icon{border-color:#2ca8ff}.card-wizard .choice input[type=checkbox],.card-wizard .choice input[type=radio]{position:absolute;left:-10000px;z-index:-1}.card-wizard .btn-finish{display:none}.card-wizard .description{color:#999;font-size:14px}.card-wizard .wizard-title{margin:0}.card-wizard .nav-pills{background-color:hsla(0,0%,78%,.2)}.card-wizard .nav-pills>li+li{margin-left:0}.card-wizard .nav-pills>li>a{border:0!important;border-radius:0;line-height:18px;text-transform:uppercase;font-size:12px;font-weight:500;min-width:100px;text-align:center;color:#555!important}.card-wizard .nav-pills>li.active>a,.card-wizard .nav-pills>li.active>a:focus,.card-wizard .nav-pills>li.active>a:hover,.card-wizard .nav-pills>li>a:focus,.card-wizard .nav-pills>li>a:hover{background-color:inherit;box-shadow:none}.card-wizard .nav-pills>li i{display:block;font-size:30px;padding:15px 0}.card-wizard .tab-pane .form-group.select-wizard{margin-top:-6px}.ct-chart .ct-series-a .ct-area,.ct-chart .ct-series-a .ct-bar,.ct-chart .ct-series-a .ct-line,.ct-chart .ct-series-a .ct-point,.ct-chart .ct-series-a .ct-slice-donut,.ct-chart .ct-series-a .ct-slice-donut-solid,.ct-chart .ct-series-a .ct-slice-pie{stroke:#00bcd4}.ct-chart .ct-series-b .ct-area,.ct-chart .ct-series-b .ct-bar,.ct-chart .ct-series-b .ct-line,.ct-chart .ct-series-b .ct-point,.ct-chart .ct-series-b .ct-slice-donut,.ct-chart .ct-series-b .ct-slice-donut-solid,.ct-chart .ct-series-b .ct-slice-pie{stroke:#f44336}.ct-chart .ct-series-c .ct-area,.ct-chart .ct-series-c .ct-bar,.ct-chart .ct-series-c .ct-line,.ct-chart .ct-series-c .ct-point,.ct-chart .ct-series-c .ct-slice-donut,.ct-chart .ct-series-c .ct-slice-donut-solid,.ct-chart .ct-series-c .ct-slice-pie{stroke:#ff9800}.ct-chart .ct-bar{fill:none;stroke-width:10px}.ct-chart .ct-line{fill:none;stroke-width:4px}.ct-chart .ct-point{stroke-width:10px;stroke-linecap:round}.ct-chart .ct-grid{stroke:rgba(0,0,0,.2);stroke-width:1px;stroke-dasharray:2px}.ct-chart .ct-label{fill:rgba(0,0,0,.4);color:rgba(0,0,0,.4);display:flex}.ct-chart .ct-label.ct-vertical.ct-start{-ms-flex-align:flex-end;align-items:flex-end;-ms-flex-pack:flex-end;justify-content:flex-end;text-align:right;text-anchor:end}.ct-chart .ct-series-a .ct-area,.ct-chart .ct-series-a .ct-slice-donut-solid,.ct-chart .ct-series-a .ct-slice-pie{fill:#00bcd4}.ct-chart .ct-series-b .ct-area,.ct-chart .ct-series-b .ct-slice-donut-solid,.ct-chart .ct-series-b .ct-slice-pie{fill:#f44336}.ct-chart .ct-series-c .ct-area,.ct-chart .ct-series-c .ct-slice-donut-solid,.ct-chart .ct-series-c .ct-slice-pie{fill:#ff9800}

/*!
 * Bootstrap-select v1.13.1 (https://developer.snapappointments.com/bootstrap-select)
 *
 * Copyright 2012-2018 SnapAppointments, LLC
 * Licensed under MIT (https://github.com/snapappointments/bootstrap-select/blob/master/LICENSE)
 */select.bs-select-hidden,select.selectpicker{display:none!important}.bootstrap-select>.dropdown-toggle{padding-right:25px}.error .bootstrap-select .dropdown-toggle,.has-error .bootstrap-select .dropdown-toggle{border-color:#b94a48}.bootstrap-select.form-control:not([class*=col-]),.bootstrap-select:not([class*=col-]):not([class*=form-control]):not(.input-group-btn){width:100%}.bootstrap-select.btn-group:not(.input-group-btn),.bootstrap-select.btn-group[class*=col-]{float:none;display:inline-block;margin-left:0}.bootstrap-select.btn-group.dropdown-menu-right,.bootstrap-select.btn-group[class*=col-].dropdown-menu-right,.row .bootstrap-select.btn-group[class*=col-].dropdown-menu-right{float:right}.form-group .bootstrap-select.btn-group,.form-horizontal .bootstrap-select.btn-group,.form-inline .bootstrap-select.btn-group{margin-bottom:0}.form-group-lg .bootstrap-select.btn-group.form-control,.form-group-sm .bootstrap-select.btn-group.form-control{padding:0}.form-inline .bootstrap-select.btn-group .form-control{width:100%}.bootstrap-select.btn-group .dropdown-menu li.disabled a:focus,.bootstrap-select.btn-group .dropdown-menu li.disabled a:hover{box-shadow:none}.bootstrap-select.btn-group.disabled,.bootstrap-select.btn-group>.disabled{cursor:not-allowed}.bootstrap-select.btn-group.disabled:focus,.bootstrap-select.btn-group>.disabled:focus{outline:none!important}.bootstrap-select.btn-group.bs-container{position:absolute;height:0!important;padding:0!important}.bootstrap-select.btn-group.bs-container .dropdown-menu{z-index:1060}.bootstrap-select.btn-group .dropdown-toggle .filter-option{display:inline-block;overflow:hidden;width:100%;text-align:left;text-overflow:ellipsis}.bootstrap-select.btn-group .dropdown-toggle .caret{position:absolute;top:50%;right:16px;margin-top:-2px;vertical-align:middle}.bootstrap-select.btn-group[class*=col-] .dropdown-toggle{width:100%}.bootstrap-select.btn-group .dropdown-menu{border-radius:4px;padding:0;min-width:100%;box-sizing:border-box}.bootstrap-select.btn-group .dropdown-menu.inner{position:static;float:none;border:0;padding:5px 0;margin:0;box-shadow:none;-ms-overflow-style:auto}.bootstrap-select.btn-group .dropdown-menu li{position:relative}.bootstrap-select.btn-group .dropdown-menu li.active small{color:#fff}.bootstrap-select.btn-group .dropdown-menu li.disabled a{cursor:not-allowed}.bootstrap-select.btn-group .dropdown-menu li a{cursor:pointer;-webkit-user-select:none;-moz-user-select:none;-ms-user-select:none;user-select:none;outline:0}.bootstrap-select.btn-group .dropdown-menu li a:focus,.bootstrap-select.btn-group .dropdown-menu li a:hover{box-shadow:0 4px 20px 0 rgba(0,0,0,.14),0 7px 10px -5px rgba(156,39,176,.4)}.bootstrap-select .dropdown-item.active{background:#9c27b0;color:#fff}.bootstrap-select>select.bs-select-hidden,select.bs-select-hidden,select.selectpicker{display:none!important}.bootstrap-select{width:220px \0}.bootstrap-select>.dropdown-toggle{position:relative;width:100%;z-index:1;text-align:right;white-space:nowrap}.bootstrap-select>.dropdown-toggle.bs-placeholder,.bootstrap-select>.dropdown-toggle.bs-placeholder:active,.bootstrap-select>.dropdown-toggle.bs-placeholder:focus,.bootstrap-select>.dropdown-toggle.bs-placeholder:hover{color:#999}.bootstrap-select>.dropdown-toggle.bs-placeholder.btn-danger,.bootstrap-select>.dropdown-toggle.bs-placeholder.btn-danger:active,.bootstrap-select>.dropdown-toggle.bs-placeholder.btn-danger:focus,.bootstrap-select>.dropdown-toggle.bs-placeholder.btn-danger:hover,.bootstrap-select>.dropdown-toggle.bs-placeholder.btn-dark,.bootstrap-select>.dropdown-toggle.bs-placeholder.btn-dark:active,.bootstrap-select>.dropdown-toggle.bs-placeholder.btn-dark:focus,.bootstrap-select>.dropdown-toggle.bs-placeholder.btn-dark:hover,.bootstrap-select>.dropdown-toggle.bs-placeholder.btn-info,.bootstrap-select>.dropdown-toggle.bs-placeholder.btn-info:active,.bootstrap-select>.dropdown-toggle.bs-placeholder.btn-info:focus,.bootstrap-select>.dropdown-toggle.bs-placeholder.btn-info:hover,.bootstrap-select>.dropdown-toggle.bs-placeholder.btn-primary,.bootstrap-select>.dropdown-toggle.bs-placeholder.btn-primary:active,.bootstrap-select>.dropdown-toggle.bs-placeholder.btn-primary:focus,.bootstrap-select>.dropdown-toggle.bs-placeholder.btn-primary:hover,.bootstrap-select>.dropdown-toggle.bs-placeholder.btn-secondary,.bootstrap-select>.dropdown-toggle.bs-placeholder.btn-secondary:active,.bootstrap-select>.dropdown-toggle.bs-placeholder.btn-secondary:focus,.bootstrap-select>.dropdown-toggle.bs-placeholder.btn-secondary:hover,.bootstrap-select>.dropdown-toggle.bs-placeholder.btn-success,.bootstrap-select>.dropdown-toggle.bs-placeholder.btn-success:active,.bootstrap-select>.dropdown-toggle.bs-placeholder.btn-success:focus,.bootstrap-select>.dropdown-toggle.bs-placeholder.btn-success:hover{color:hsla(0,0%,100%,.5)}.bootstrap-select>select{position:absolute!important;bottom:0;left:50%;display:block!important;width:.5px!important;height:100%!important;padding:0!important;opacity:0!important;border:none}.bootstrap-select>select.mobile-device{top:0;left:0;display:block!important;width:100%!important;z-index:2}.bootstrap-select.is-invalid .dropdown-toggle,.error .bootstrap-select .dropdown-toggle,.has-error .bootstrap-select .dropdown-toggle,.was-validated .bootstrap-select .selectpicker:invalid+.dropdown-toggle{border-color:#b94a48}.bootstrap-select.is-valid .dropdown-toggle,.was-validated .bootstrap-select .selectpicker:valid+.dropdown-toggle{border-color:#28a745}.bootstrap-select.fit-width{width:auto!important}.bootstrap-select:not([class*=col-]):not([class*=form-control]):not(.input-group-btn){width:220px}.bootstrap-select .dropdown-toggle:focus{outline:thin dotted #333!important;outline:5px auto -webkit-focus-ring-color!important;outline-offset:-2px}.bootstrap-select.form-control{margin-bottom:0;padding:0;border:none}:not(.input-group)>.bootstrap-select.form-control:not([class*=col-]){width:100%}.bootstrap-select.form-control.input-group-btn{z-index:auto}.bootstrap-select.form-control.input-group-btn:not(:first-child):not(:last-child)>.btn{border-radius:0}.bootstrap-select:not(.input-group-btn),.bootstrap-select[class*=col-]{float:none;display:inline-block;margin-left:0}.bootstrap-select.dropdown-menu-right,.bootstrap-select[class*=col-].dropdown-menu-right,.row .bootstrap-select[class*=col-].dropdown-menu-right{float:right}.form-group .bootstrap-select,.form-horizontal .bootstrap-select,.form-inline .bootstrap-select{margin-bottom:0}.form-group-lg .bootstrap-select.form-control,.form-group-sm .bootstrap-select.form-control{padding:0}.form-group-lg .bootstrap-select.form-control .dropdown-toggle,.form-group-sm .bootstrap-select.form-control .dropdown-toggle{height:100%;font-size:inherit;line-height:inherit;border-radius:inherit}.bootstrap-select.form-control-lg .dropdown-toggle,.bootstrap-select.form-control-sm .dropdown-toggle,.input-group-lg>.bootstrap-select.form-control .dropdown-toggle,.input-group-lg>.input-group-append>.bootstrap-select.btn .dropdown-toggle,.input-group-lg>.input-group-append>.bootstrap-select.input-group-text .dropdown-toggle,.input-group-lg>.input-group-prepend>.bootstrap-select.btn .dropdown-toggle,.input-group-lg>.input-group-prepend>.bootstrap-select.input-group-text .dropdown-toggle,.input-group-sm>.bootstrap-select.form-control .dropdown-toggle,.input-group-sm>.input-group-append>.bootstrap-select.btn .dropdown-toggle,.input-group-sm>.input-group-append>.bootstrap-select.input-group-text .dropdown-toggle,.input-group-sm>.input-group-prepend>.bootstrap-select.btn .dropdown-toggle,.input-group-sm>.input-group-prepend>.bootstrap-select.input-group-text .dropdown-toggle{font-size:inherit;line-height:inherit;border-radius:inherit}.bootstrap-select.form-control-sm .dropdown-toggle,.input-group-sm>.bootstrap-select.form-control .dropdown-toggle,.input-group-sm>.input-group-append>.bootstrap-select.btn .dropdown-toggle,.input-group-sm>.input-group-append>.bootstrap-select.input-group-text .dropdown-toggle,.input-group-sm>.input-group-prepend>.bootstrap-select.btn .dropdown-toggle,.input-group-sm>.input-group-prepend>.bootstrap-select.input-group-text .dropdown-toggle{padding:.25rem .5rem}.bootstrap-select.form-control-lg .dropdown-toggle,.input-group-lg>.bootstrap-select.form-control .dropdown-toggle,.input-group-lg>.input-group-append>.bootstrap-select.btn .dropdown-toggle,.input-group-lg>.input-group-append>.bootstrap-select.input-group-text .dropdown-toggle,.input-group-lg>.input-group-prepend>.bootstrap-select.btn .dropdown-toggle,.input-group-lg>.input-group-prepend>.bootstrap-select.input-group-text .dropdown-toggle{padding:.5rem 1rem}.form-inline .bootstrap-select .form-control{width:100%}.bootstrap-select.disabled,.bootstrap-select>.disabled{cursor:not-allowed}.bootstrap-select.disabled:focus,.bootstrap-select>.disabled:focus{outline:none!important}.bootstrap-select.bs-container{position:absolute;top:0;left:0;height:0!important;padding:0!important}.bootstrap-select.bs-container .dropdown-menu{z-index:1060}.bootstrap-select .dropdown-toggle:before{content:"";display:inline-block}.bootstrap-select .dropdown-toggle .filter-option{position:absolute;top:0;left:0;padding-top:inherit;padding-right:inherit;padding-bottom:inherit;padding-left:inherit;height:100%;width:100%;text-align:left}.bootstrap-select .dropdown-toggle .filter-option-inner{padding-right:inherit}.bootstrap-select .dropdown-toggle .filter-option-inner-inner{overflow:hidden}.bootstrap-select .dropdown-toggle .caret{position:absolute;top:50%;right:12px;margin-top:-2px;vertical-align:middle}.input-group .bootstrap-select.form-control .dropdown-toggle{border-radius:inherit}.bootstrap-select[class*=col-] .dropdown-toggle{width:100%}.bootstrap-select .dropdown-menu{min-width:100%;box-sizing:border-box}.bootstrap-select .dropdown-menu>.inner:focus{outline:none!important}.bootstrap-select .dropdown-menu.inner{position:static;float:none;border:0;padding:0;margin:0;border-radius:0;box-shadow:none}.bootstrap-select .dropdown-menu li{position:relative}.bootstrap-select .dropdown-menu li.active small{color:#fff}.bootstrap-select .dropdown-menu li.disabled a{cursor:not-allowed}.bootstrap-select .dropdown-menu li a{cursor:pointer;-webkit-user-select:none;-moz-user-select:none;-ms-user-select:none;user-select:none}.bootstrap-select .dropdown-menu li a.opt{position:relative;padding-left:2.25em}.bootstrap-select .dropdown-menu li a span.check-mark{display:none}.bootstrap-select .dropdown-menu li a span.text{display:inline-block}.bootstrap-select .dropdown-menu li small{padding-left:.5em}.bootstrap-select .dropdown-menu .notify{position:absolute;bottom:5px;width:96%;margin:0 2%;min-height:26px;padding:3px 5px;background:#f5f5f5;border:1px solid #e3e3e3;box-shadow:inset 0 1px 1px rgba(0,0,0,.05);pointer-events:none;opacity:.9;box-sizing:border-box}.bootstrap-select .no-results{padding:3px;background:#f5f5f5;margin:0 5px;white-space:nowrap}.bootstrap-select.fit-width .dropdown-toggle .filter-option{position:static;display:inline;padding:0}.bootstrap-select.fit-width .dropdown-toggle .filter-option-inner,.bootstrap-select.fit-width .dropdown-toggle .filter-option-inner-inner{display:inline}.bootstrap-select.fit-width .dropdown-toggle .caret{position:static;top:auto;margin-top:-1px}.bootstrap-select.show-tick .dropdown-menu .selected span.check-mark{position:absolute;display:inline-block;right:15px;top:5px}.bootstrap-select.show-tick .dropdown-menu li a span.text{margin-right:34px}.bootstrap-select .bs-ok-default:after{content:"";display:block;width:.5em;height:1em;border-style:solid;border-width:0 .26em .26em 0;transform:rotate(45deg)}.bootstrap-select.show-menu-arrow.open>.dropdown-toggle,.bootstrap-select.show-menu-arrow.show>.dropdown-toggle{z-index:1061}.bootstrap-select.show-menu-arrow .dropdown-toggle .filter-option:before{content:"";border-left:7px solid transparent;border-right:7px solid transparent;border-bottom:7px solid hsla(0,0%,80%,.2);position:absolute;bottom:-4px;left:9px;display:none}.bootstrap-select.show-menu-arrow .dropdown-toggle .filter-option:after{content:"";border-left:6px solid transparent;border-right:6px solid transparent;border-bottom:6px solid #fff;position:absolute;bottom:-4px;left:10px;display:none}.bootstrap-select.show-menu-arrow.dropup .dropdown-toggle .filter-option:before{bottom:auto;top:-4px;border-top:7px solid hsla(0,0%,80%,.2);border-bottom:0}.bootstrap-select.show-menu-arrow.dropup .dropdown-toggle .filter-option:after{bottom:auto;top:-4px;border-top:6px solid #fff;border-bottom:0}.bootstrap-select.show-menu-arrow.pull-right .dropdown-toggle .filter-option:before{right:12px;left:auto}.bootstrap-select.show-menu-arrow.pull-right .dropdown-toggle .filter-option:after{right:13px;left:auto}.bootstrap-select.show-menu-arrow.open>.dropdown-toggle .filter-option:after,.bootstrap-select.show-menu-arrow.open>.dropdown-toggle .filter-option:before,.bootstrap-select.show-menu-arrow.show>.dropdown-toggle .filter-option:after,.bootstrap-select.show-menu-arrow.show>.dropdown-toggle .filter-option:before{display:block}.bs-actionsbox,.bs-donebutton,.bs-searchbox{padding:4px 8px}.bs-actionsbox{width:100%;box-sizing:border-box}.bs-actionsbox .btn-group button{width:50%}.bs-donebutton{float:left;width:100%;box-sizing:border-box}.bs-donebutton .btn-group button{width:100%}.bs-searchbox+.bs-actionsbox{padding:0 8px 4px}.bs-searchbox .form-control{margin-bottom:0;width:100%;float:none}.bootstrap-select .btn:focus{outline:none!important}.bootstrap-select .btn.dropdown-toggle.btn-link[aria-expanded=true],.bootstrap-select .btn.dropdown-toggle.btn-link[aria-expanded=true]:hover{background:transparent!important}.bootstrap-select .btn.dropdown-toggle[aria-expanded=true]:hover+.dropdown-menu.show .inner.show{background:transparent}.bootstrap-select .btn.dropdown-toggle.select-with-transition{border:0!important;background-image:linear-gradient(0deg,#9c27b0 2px,rgba(156,39,176,0) 0),linear-gradient(0deg,#d2d2d2 1px,hsla(0,0%,82%,0) 0);background-size:0 100%,100% 100%;background-repeat:no-repeat;background-position:bottom,50% calc(100% - 1px);background-color:transparent!important;transition:background 0s linear!important;float:none!important;box-shadow:none!important;border-radius:0!important;color:#3c4858!important;height:34px;padding-left:0!important;padding-bottom:5px!important}.bootstrap-select .btn.dropdown-toggle.select-with-transition:focus{background-size:100% 100%,100% 100%!important;transition-duration:.3s!important;box-shadow:none!important}.ps-container{-ms-touch-action:auto;touch-action:auto;overflow:hidden!important;-ms-overflow-style:none}@supports (-ms-overflow-style:none){.ps-container{overflow:auto!important}}@media (-ms-high-contrast:none),screen and (-ms-high-contrast:active){.ps-container{overflow:auto!important}}.ps-container.ps-active-x>.ps-scrollbar-x-rail,.ps-container.ps-active-y>.ps-scrollbar-y-rail{display:block;background-color:transparent}.ps-container.ps-in-scrolling.ps-x>.ps-scrollbar-x-rail{background-color:#eee;opacity:.9}.ps-container.ps-in-scrolling.ps-x>.ps-scrollbar-x-rail>.ps-scrollbar-x{background-color:#999;height:11px}.ps-container.ps-in-scrolling.ps-y>.ps-scrollbar-y-rail{background-color:#eee;opacity:.9}.ps-container.ps-in-scrolling.ps-y>.ps-scrollbar-y-rail>.ps-scrollbar-y{background-color:#999;width:11px}.ps-container>.ps-scrollbar-x-rail{display:none;position:absolute;opacity:0;transition:background-color .2s linear,opacity .2s linear;bottom:0;height:15px}.ps-container>.ps-scrollbar-x-rail>.ps-scrollbar-x{position:absolute;background-color:#aaa;border-radius:6px;transition:background-color .2s linear,height .2s linear,width .2s ease-in-out,border-radius .2s ease-in-out;bottom:2px;height:6px}.ps-container>.ps-scrollbar-x-rail:active>.ps-scrollbar-x,.ps-container>.ps-scrollbar-x-rail:hover>.ps-scrollbar-x{height:11px}.ps-container>.ps-scrollbar-y-rail{display:none;position:absolute;opacity:0;transition:background-color .2s linear,opacity .2s linear;right:0;width:15px}.ps-container>.ps-scrollbar-y-rail>.ps-scrollbar-y{position:absolute;background-color:#aaa;border-radius:6px;transition:background-color .2s linear,height .2s linear,width .2s ease-in-out,border-radius .2s ease-in-out;right:2px;width:6px}.ps-container>.ps-scrollbar-y-rail:active>.ps-scrollbar-y,.ps-container>.ps-scrollbar-y-rail:hover>.ps-scrollbar-y{width:11px}.ps-container:hover.ps-in-scrolling.ps-x>.ps-scrollbar-x-rail{background-color:#eee;opacity:.9}.ps-container:hover.ps-in-scrolling.ps-x>.ps-scrollbar-x-rail>.ps-scrollbar-x{background-color:#999;height:11px}.ps-container:hover.ps-in-scrolling.ps-y>.ps-scrollbar-y-rail{background-color:#eee;opacity:.9}.ps-container:hover.ps-in-scrolling.ps-y>.ps-scrollbar-y-rail>.ps-scrollbar-y{background-color:#999;width:11px}.ps-container:hover>.ps-scrollbar-x-rail,.ps-container:hover>.ps-scrollbar-y-rail{opacity:.6}.ps-container:hover>.ps-scrollbar-x-rail:hover{background-color:#eee;opacity:.9}.ps-container:hover>.ps-scrollbar-x-rail:hover>.ps-scrollbar-x{background-color:#999}.ps-container:hover>.ps-scrollbar-y-rail:hover{background-color:#eee;opacity:.9}.ps-container:hover>.ps-scrollbar-y-rail:hover>.ps-scrollbar-y{background-color:#999}.bootstrap-tagsinput{display:inline-block;padding:4px 6px;max-width:100%;line-height:22px}.bootstrap-tagsinput input{outline:none;background-color:transparent;margin:0;width:74px;max-width:inherit;display:inline-block}.bootstrap-tagsinput input,.bootstrap-tagsinput input:focus{border:none;box-shadow:none;background-image:none}.bootstrap-tagsinput.form-control input::-moz-placeholder{color:#777;opacity:1}.bootstrap-tagsinput.form-control input:-ms-input-placeholder,.bootstrap-tagsinput.form-control input::-webkit-input-placeholder{color:#777}.bootstrap-tagsinput .tag{cursor:pointer;margin:5px 3px 5px 0;position:relative;padding:3px 8px;border-radius:12px;color:#fff;font-weight:500;font-size:.75em;text-transform:uppercase;display:inline-block;line-height:1.5em;padding-left:.8em}.bootstrap-tagsinput .tag:hover{padding-right:18px}.bootstrap-tagsinput .tag:hover [data-role=remove]{opacity:1;padding-right:6px}.bootstrap-tagsinput .tag [data-role=remove]{cursor:pointer;position:absolute;top:3px;right:0;opacity:0}.bootstrap-tagsinput .tag [data-role=remove]:after{content:"x";padding:0 2px}.bootstrap-tagsinput.primary-badge .tag{background-color:#9c27b0;color:#fff}.bootstrap-tagsinput.primary-badge .tag .tagsinput-remove-link{color:#fff}.bootstrap-tagsinput.info-badge .tag{background-color:#00bcd4;color:#fff}.bootstrap-tagsinput.info-badge .tag .tagsinput-remove-link{color:#fff}.bootstrap-tagsinput.success-badge .tag{background-color:#4caf50;color:#fff}.bootstrap-tagsinput.success-badge .tag .tagsinput-remove-link{color:#fff}.bootstrap-tagsinput.warning-badge .tag{background-color:#ff9800;color:#fff}.bootstrap-tagsinput.warning-badge .tag .tagsinput-remove-link{color:#fff}.bootstrap-tagsinput.danger-badge .tag{background-color:#f44336;color:#fff}.bootstrap-tagsinput.danger-badge .tag .tagsinput-remove-link{color:#fff}.bootstrap-tagsinput.rose-badge .tag{background-color:#e91e63;color:#fff}.bootstrap-tagsinput.rose-badge .tag .tagsinput-remove-link,.card-signup .card-header .social-line .btn{color:#fff}.card-signup .text-divider{margin-top:30px;margin-bottom:0;text-align:center}.login-page .card-login .card-header{margin-top:-40px!important;margin-bottom:20px}.login-page .card-login .social-line{padding:0;margin-top:15px}.login-page .card-login .card-title{margin-top:10px;margin-bottom:10px;font-weight:700}.signup-page .page-header .container{padding-top:20vh}.signup-page .card-signup{border-radius:6px;box-shadow:0 16px 24px 2px rgba(0,0,0,.14),0 6px 30px 5px rgba(0,0,0,.12),0 8px 10px -5px rgba(0,0,0,.2);margin-bottom:100px;padding:40px 0}.signup-page .info-horizontal{padding:0 0 20px}.signup-page .social .btn{margin:5px}.signup-page .social h4{margin-top:20px}.signup-page .footer .container{padding:0}.signup-page .footer .copyright,.signup-page .footer a{color:#fff}.register-page .page-header{background-position:top}@media (max-width:991px){.page-header.pricing-page,.page-header.register-page{min-height:fit-content!important}}@media (max-width:991px){[class*=navbar-expand-]>.container,[class*=navbar-expand-]>.container-fluid{padding-left:15px;padding-right:15px}.navbar .navbar-collapse .navbar-nav>li.button-container{padding:15px}.bootstrap-select:not([class*=col-]):not([class*=form-control]):not(.input-group-btn){width:-webkit-fill-available!important}.bootstrap-select:not([class*=col-]):not([class*=form-control]):not(.input-group-btn) .dropdown-menu.show{min-width:auto;left:auto}.carousel .card .card-body{max-width:340px;margin:0 auto;min-height:400px}.navbar-collapse{position:fixed;display:block;top:0;height:100vh;width:230px;right:0;margin-right:0!important;z-index:1032;visibility:visible;background-color:#999;overflow-y:visible;border-top:none;text-align:left;padding-right:0;padding-left:0;max-height:none!important;transform:translate3d(230px,0,0);transition:all .5s cubic-bezier(.685,.0473,.346,1)}.navbar-collapse:after{top:0;left:0;height:100%;width:100%;position:absolute;background-color:#fff;display:block;content:"";z-index:1}.navbar-collapse .dropdown-toggle:after{position:absolute;right:16px;margin-top:8px}.navbar-collapse .navbar-nav{position:relative;z-index:3}.navbar-collapse .navbar-nav .nav-item .nav-link{color:#3c4858;margin:5px 15px}.navbar-collapse .navbar-nav .nav-item.button-container .nav-link{margin:15px}.navbar-collapse .navbar-nav .nav-item:after{width:calc(100% - 30px);content:"";display:block;height:1px;margin-left:15px}.navbar-collapse .navbar-nav .nav-item:last-child:after{display:none}.nav-open .navbar-collapse{transform:translateZ(0)}.nav-open .navbar-translate{transform:translate3d(-230px,0,0)}.navbar .navbar-translate{width:100%;position:relative;display:flex;-ms-flex-pack:justify!important;justify-content:space-between!important;-ms-flex-align:center;align-items:center;transition:transform .5s cubic-bezier(.685,.0473,.346,1)}.navbar .dropdown.show .dropdown-menu{display:block}.navbar .dropdown .dropdown-menu{display:none}.navbar .dropdown-menu .dropdown-item{margin-left:1.5rem;margin-right:1.5rem}.navbar .dropdown .dropdown-menu,.navbar .dropdown.show .dropdown-menu{background-color:transparent;border:0;padding-bottom:15px;transition:none;box-shadow:none;transform:none!important;width:auto;margin-bottom:15px;padding-top:0;height:300px;animation:none;opacity:1;overflow-y:scroll}.navbar.navbar-transparent .navbar-toggler .navbar-toggler-icon{background-color:#fff}#bodyClick{height:100%;width:100%;position:fixed;opacity:0;top:0;left:auto;right:230px;content:"";z-index:1029;overflow-x:hidden}#navbar .navbar-collapse,#navigation .navbar-collapse{display:none!important}.dropdown-menu.show .dropdown-item.open+.dropdown-menu.show{right:101%!important}.dropdown-menu.show .dropdown-item.open+.dropdown-menu.show .dropdown-item.open+.dropdown-menu,.dropdown-menu.show .dropdown-item.open+.dropdown-menu.show .dropdown-item.open+.dropdown-menu.show{left:-165px!important}}@media (min-width:991px){.navbar .navbar-nav{align-items:center}.navbar .navbar-nav .button-container{margin-left:.1875px}.sidebar .navbar-form{display:none!important}}@media screen and (max-width:991px){.presentation-page .section-components .components-macbook{max-width:850px!important;max-height:480px!important;margin-top:12vh;left:-12px}.presentation-page .section-components .coloured-card-img,.presentation-page .section-components .table-img{display:none}.presentation-page .section-components .social-img{left:47%;top:37%}.presentation-page .section-components .pin-btn-img{top:54%}.presentation-page .section-components .share-btn-img{top:12%}.presentation-page .section-components .coloured-card-btn-img{top:-2%;left:65%}.presentation-page .section-content .area-img{max-width:130px;max-height:170px}.presentation-page .section-content .info-img{max-width:170px;max-height:120px}}@media screen and (max-width:767px){.presentation-page .section-components .components-macbook{max-width:350px!important;max-height:250px!important;margin-top:12vh;left:-12px}.presentation-page .section-components .coloured-card-img,.presentation-page .section-components .table-img{display:none}.presentation-page .section-components .social-img{left:-7%;top:37%}.presentation-page .section-components .pin-btn-img{top:54%}.presentation-page .section-components .share-btn-img{top:7%}.presentation-page .section-components .coloured-card-btn-img{top:-2%}.login-page .container{padding-top:100px!important}.index-page #cd-vertical-nav,.presentation-page #cd-vertical-nav,.section-page #cd-vertical-nav{display:none}.index-page .cd-section .tim-typo .tim-note{width:60px}}@media screen and (max-width:400px){.cd-vertical-nav{display:none!important}}@media (max-width:991px){.form-group textarea{padding-top:15px}.nav-open .menu-on-left .main-panel{position:static}body,html{overflow-x:hidden}.nav-open .menu-on-left .main-panel,.nav-open .menu-on-left .navbar-fixed>div,.nav-open .menu-on-left .wrapper-full-page{transform:translate3d(260px,0,0)}.menu-on-left .off-canvas-sidebar,.menu-on-left .sidebar{left:0;right:auto;transform:translate3d(-260px,0,0)}.menu-on-left .close-layer{left:auto;right:0}.timeline:before,.timeline>li>.timeline-badge{left:5%}.timeline>li>.timeline-panel{float:right;width:86%}.timeline>li>.timeline-panel:before{border-left-width:0;border-right-width:15px;left:-15px;right:auto}.timeline>li>.timeline-panel:after{border-left-width:0;border-right-width:14px;left:-14px;right:auto}.nav-mobile-menu .dropdown .dropdown-menu{display:none;position:static!important;background-color:transparent;width:auto;float:none;box-shadow:none}.nav-mobile-menu .dropdown .dropdown-menu.showing{animation:initial;animation-duration:0s}.nav-mobile-menu .dropdown .dropdown-menu.hiding{transform:none;opacity:1}.nav-mobile-menu .dropdown.show .dropdown-menu{display:block}.nav-mobile-menu li.active>a{background-color:hsla(0,0%,100%,.1)}.navbar-minimize{display:none}.card .form-horizontal .label-on-left,.card .form-horizontal .label-on-right{padding-left:15px;padding-top:8px}.card .form-horizontal .form-group{margin-top:0}.card .form-horizontal .checkbox-radios{padding-bottom:15px}.card .form-horizontal .checkbox-inline,.card .form-horizontal .checkbox-radios .checkbox:first-child,.card .form-horizontal .checkbox-radios .radio:first-child{margin-top:0}.sidebar{display:none;box-shadow:none}.sidebar .sidebar-wrapper{padding-bottom:60px}.sidebar .nav-mobile-menu{margin-top:0}.sidebar .nav-mobile-menu .notification{float:left;line-height:30px;margin-right:8px}.sidebar .nav-mobile-menu .open .dropdown-menu{position:static;float:none;width:auto;margin-top:0;background-color:transparent;border:0;box-shadow:none}.main-panel{width:100%}.navbar-transparent{padding-top:15px;background-color:rgba(0,0,0,.45)}body{position:relative}.nav-open .main-panel,.nav-open .navbar .container,.nav-open .navbar .container .navbar-toggler,.nav-open .navbar .container .navbar-wrapper,.nav-open .wrapper-full-page{left:0;transform:translate3d(-260px,0,0)}.nav-open .sidebar{box-shadow:0 16px 38px -12px rgba(0,0,0,.56),0 4px 25px 0 rgba(0,0,0,.12),0 8px 10px -5px rgba(0,0,0,.2)}.nav-open .off-canvas-sidebar .navbar-collapse,.nav-open .sidebar{transform:translateZ(0)}.navbar .container,.navbar .container .navbar-toggler,.navbar .container .navbar-wrapper,.wrapper-full-page{transform:translateZ(0);transition:all .33s cubic-bezier(.685,.0473,.346,1);left:0}.off-canvas-sidebar .navbar .container{transform:none}.main-panel,.navbar-collapse{transition:all .33s cubic-bezier(.685,.0473,.346,1)}.navbar .navbar-collapse.collapse,.navbar .navbar-collapse.collapse.in,.navbar .navbar-collapse.collapsing{display:none!important}.off-canvas-sidebar .navbar .navbar-collapse.collapse,.off-canvas-sidebar .navbar .navbar-collapse.collapse.in,.off-canvas-sidebar .navbar .navbar-collapse.collapsing{display:block!important}.navbar-nav>li{float:none;position:relative;display:block}.off-canvas-sidebar nav .navbar-collapse{margin:0}.off-canvas-sidebar nav .navbar-collapse>ul{margin-top:19px}.off-canvas-sidebar nav .navbar-collapse,.sidebar{position:fixed;display:block;top:0;height:100vh;width:260px;right:0;left:auto;z-index:1032;visibility:visible;background-color:#9a9a9a;overflow-y:visible;border-top:none;text-align:left;padding-right:0;padding-left:0;transform:translate3d(260px,0,0);transition:all .33s cubic-bezier(.685,.0473,.346,1)}.off-canvas-sidebar nav .navbar-collapse>ul,.sidebar>ul{position:relative;z-index:4;width:100%}.off-canvas-sidebar nav .navbar-collapse:before,.sidebar:before{top:0;left:0;height:100%;width:100%;position:absolute;background-color:#282828;display:block;content:"";z-index:1}.off-canvas-sidebar nav .navbar-collapse .logo,.sidebar .logo{position:relative;z-index:4}.off-canvas-sidebar nav .navbar-collapse .navbar-form,.sidebar .navbar-form{margin:10px 0;float:none!important;padding-top:1px;padding-bottom:1px;position:relative}.off-canvas-sidebar nav .navbar-collapse .table-responsive,.sidebar .table-responsive{width:100%;margin-bottom:15px;overflow-x:scroll;overflow-y:hidden;-ms-overflow-style:-ms-autohiding-scrollbar;-webkit-overflow-scrolling:touch}.form-group.form-search .form-control{font-size:1.7em;height:37px;width:78%}.navbar-form .btn{position:absolute;top:-5px;right:-50px}.close-layer{height:100%;width:100%;position:absolute;opacity:0;top:0;left:auto;background:rgba(0,0,0,.35);content:"";z-index:9999;overflow-x:hidden;transition:all .37s ease-in}.close-layer.visible{opacity:1}.navbar-toggler .icon-bar{display:block;position:relative;background:#555!important;width:24px;height:2px;border-radius:1px;margin:0 auto}.navbar-header .navbar-toggler{padding:15px;margin-top:4px;width:40px;height:40px}.bar1,.bar2,.bar3{outline:1px solid transparent}@keyframes x{0%{top:0;transform:rotate(0deg)}45%{top:6px;transform:rotate(145deg)}75%{transform:rotate(130deg)}to{transform:rotate(135deg)}}@keyframes y{0%{top:6px;transform:rotate(135deg)}45%{transform:rotate(-10deg)}75%{transform:rotate(5deg)}to{top:0;transform:rotate(0)}}@keyframes z{0%{bottom:0;transform:rotate(0deg)}45%{bottom:6px;transform:rotate(-145deg)}75%{transform:rotate(-130deg)}to{transform:rotate(-135deg)}}@keyframes A{0%{bottom:6px;transform:rotate(-135deg)}45%{transform:rotate(10deg)}75%{transform:rotate(-5deg)}to{bottom:0;transform:rotate(0)}}.navbar-toggler .icon-bar:nth-child(2){top:0;animation:y .5s 0s;animation-fill-mode:forwards}.navbar-toggler .icon-bar:nth-child(3){opacity:1}.navbar-toggler .icon-bar:nth-child(4){bottom:0;animation:A .5s 0s;animation-fill-mode:forwards}.navbar-toggler.toggled .icon-bar:nth-child(2){top:6px;animation:x .5s 0s;animation-fill-mode:forwards}.navbar-toggler.toggled .icon-bar:nth-child(3){opacity:0}.navbar-toggler.toggled .icon-bar:nth-child(4){bottom:6px;animation:z .5s 0s;animation-fill-mode:forwards}.dropdown-menu .divider{background-color:hsla(0,0%,90%,.15)}.navbar-nav{margin:1px 0}.navbar-nav .open .dropdown-menu>li>a{padding:15px 15px 5px 50px}.navbar-nav .open .dropdown-menu>li:first-child>a{padding:5px 15px 5px 50px}.navbar-nav .open .dropdown-menu>li:last-child>a{padding:15px 15px 25px 50px}[class*=navbar-] .navbar-nav .active>a,[class*=navbar-] .navbar-nav .active>a:focus,[class*=navbar-] .navbar-nav .active>a:hover,[class*=navbar-] .navbar-nav .navbar-nav .open .dropdown-menu>li>a:active,[class*=navbar-] .navbar-nav .open .dropdown-menu>li>a,[class*=navbar-] .navbar-nav .open .dropdown-menu>li>a:focus,[class*=navbar-] .navbar-nav .open .dropdown-menu>li>a:hover,[class*=navbar-] .navbar-nav>li>a,[class*=navbar-] .navbar-nav>li>a:focus,[class*=navbar-] .navbar-nav>li>a:hover{color:#fff}[class*=navbar-] .navbar-nav .open .dropdown-menu>li>a,[class*=navbar-] .navbar-nav .open .dropdown-menu>li>a:focus,[class*=navbar-] .navbar-nav .open .dropdown-menu>li>a:hover,[class*=navbar-] .navbar-nav>li>a,[class*=navbar-] .navbar-nav>li>a:focus,[class*=navbar-] .navbar-nav>li>a:hover{opacity:.7;background:transparent}[class*=navbar-] .navbar-nav.navbar-nav .open .dropdown-menu>li>a:active{opacity:1}[class*=navbar-] .navbar-nav .dropdown>a:hover .caret{border-bottom-color:#777;border-top-color:#777}[class*=navbar-] .navbar-nav .dropdown>a:active .caret{border-bottom-color:#fff;border-top-color:#fff}.dropdown-menu{display:none}.navbar-fixed-top{-webkit-backface-visibility:hidden}#bodyClick{height:100%;width:100%;position:fixed;opacity:0;top:0;left:auto;right:260px;content:"";z-index:9999;overflow-x:hidden}.social-line .btn,.subscribe-line .form-control{margin:0 0 10px}.footer:not(.footer-big) nav>ul li,.social-line.pull-right{float:none}.social-area.pull-right{float:none!important}.form-control+.form-control-feedback{margin-top:-8px}.navbar-toggle:focus,.navbar-toggle:hover{background-color:transparent!important}.media-post .author{width:20%;float:none!important;display:block;margin:0 auto 10px}.media-post .media-body{width:100%}.navbar-collapse.collapse{height:100%!important}.navbar-collapse.collapse.in{display:block}.navbar-header .collapse,.navbar-toggle{display:block!important}.navbar-header{float:none}.navbar-collapse .nav p{font-size:1rem;margin:0}}@media (min-width:992px){.main-panel .navbar .navbar-collapse .navbar-nav .nav-item .nav-link p{display:none}.nav-mobile-menu,.sidebar .navbar-form{display:none!important}}


File: /public\css\style.css
.dosBotones{display:flex;align-items:center;justify-content:flex-end;}

File: /public\fontawesome\css\all.css
/*!
 * Font Awesome Free 5.14.0 by @fontawesome - https://fontawesome.com
 * License - https://fontawesome.com/license/free (Icons: CC BY 4.0, Fonts: SIL OFL 1.1, Code: MIT License)
 */
.fa,
.fas,
.far,
.fal,
.fad,
.fab {
  -moz-osx-font-smoothing: grayscale;
  -webkit-font-smoothing: antialiased;
  display: inline-block;
  font-style: normal;
  font-variant: normal;
  text-rendering: auto;
  line-height: 1; }

.fa-lg {
  font-size: 1.33333em;
  line-height: 0.75em;
  vertical-align: -.0667em; }

.fa-xs {
  font-size: .75em; }

.fa-sm {
  font-size: .875em; }

.fa-1x {
  font-size: 1em; }

.fa-2x {
  font-size: 2em; }

.fa-3x {
  font-size: 3em; }

.fa-4x {
  font-size: 4em; }

.fa-5x {
  font-size: 5em; }

.fa-6x {
  font-size: 6em; }

.fa-7x {
  font-size: 7em; }

.fa-8x {
  font-size: 8em; }

.fa-9x {
  font-size: 9em; }

.fa-10x {
  font-size: 10em; }

.fa-fw {
  text-align: center;
  width: 1.25em; }

.fa-ul {
  list-style-type: none;
  margin-left: 2.5em;
  padding-left: 0; }
  .fa-ul > li {
    position: relative; }

.fa-li {
  left: -2em;
  position: absolute;
  text-align: center;
  width: 2em;
  line-height: inherit; }

.fa-border {
  border: solid 0.08em #eee;
  border-radius: .1em;
  padding: .2em .25em .15em; }

.fa-pull-left {
  float: left; }

.fa-pull-right {
  float: right; }

.fa.fa-pull-left,
.fas.fa-pull-left,
.far.fa-pull-left,
.fal.fa-pull-left,
.fab.fa-pull-left {
  margin-right: .3em; }

.fa.fa-pull-right,
.fas.fa-pull-right,
.far.fa-pull-right,
.fal.fa-pull-right,
.fab.fa-pull-right {
  margin-left: .3em; }

.fa-spin {
  -webkit-animation: fa-spin 2s infinite linear;
          animation: fa-spin 2s infinite linear; }

.fa-pulse {
  -webkit-animation: fa-spin 1s infinite steps(8);
          animation: fa-spin 1s infinite steps(8); }

@-webkit-keyframes fa-spin {
  0% {
    -webkit-transform: rotate(0deg);
            transform: rotate(0deg); }
  100% {
    -webkit-transform: rotate(360deg);
            transform: rotate(360deg); } }

@keyframes fa-spin {
  0% {
    -webkit-transform: rotate(0deg);
            transform: rotate(0deg); }
  100% {
    -webkit-transform: rotate(360deg);
            transform: rotate(360deg); } }

.fa-rotate-90 {
  -ms-filter: "progid:DXImageTransform.Microsoft.BasicImage(rotation=1)";
  -webkit-transform: rotate(90deg);
          transform: rotate(90deg); }

.fa-rotate-180 {
  -ms-filter: "progid:DXImageTransform.Microsoft.BasicImage(rotation=2)";
  -webkit-transform: rotate(180deg);
          transform: rotate(180deg); }

.fa-rotate-270 {
  -ms-filter: "progid:DXImageTransform.Microsoft.BasicImage(rotation=3)";
  -webkit-transform: rotate(270deg);
          transform: rotate(270deg); }

.fa-flip-horizontal {
  -ms-filter: "progid:DXImageTransform.Microsoft.BasicImage(rotation=0, mirror=1)";
  -webkit-transform: scale(-1, 1);
          transform: scale(-1, 1); }

.fa-flip-vertical {
  -ms-filter: "progid:DXImageTransform.Microsoft.BasicImage(rotation=2, mirror=1)";
  -webkit-transform: scale(1, -1);
          transform: scale(1, -1); }

.fa-flip-both, .fa-flip-horizontal.fa-flip-vertical {
  -ms-filter: "progid:DXImageTransform.Microsoft.BasicImage(rotation=2, mirror=1)";
  -webkit-transform: scale(-1, -1);
          transform: scale(-1, -1); }

:root .fa-rotate-90,
:root .fa-rotate-180,
:root .fa-rotate-270,
:root .fa-flip-horizontal,
:root .fa-flip-vertical,
:root .fa-flip-both {
  -webkit-filter: none;
          filter: none; }

.fa-stack {
  display: inline-block;
  height: 2em;
  line-height: 2em;
  position: relative;
  vertical-align: middle;
  width: 2.5em; }

.fa-stack-1x,
.fa-stack-2x {
  left: 0;
  position: absolute;
  text-align: center;
  width: 100%; }

.fa-stack-1x {
  line-height: inherit; }

.fa-stack-2x {
  font-size: 2em; }

.fa-inverse {
  color: #fff; }

/* Font Awesome uses the Unicode Private Use Area (PUA) to ensure screen
readers do not read off random characters that represent icons */
.fa-500px:before {
  content: "\f26e"; }

.fa-accessible-icon:before {
  content: "\f368"; }

.fa-accusoft:before {
  content: "\f369"; }

.fa-acquisitions-incorporated:before {
  content: "\f6af"; }

.fa-ad:before {
  content: "\f641"; }

.fa-address-book:before {
  content: "\f2b9"; }

.fa-address-card:before {
  content: "\f2bb"; }

.fa-adjust:before {
  content: "\f042"; }

.fa-adn:before {
  content: "\f170"; }

.fa-adobe:before {
  content: "\f778"; }

.fa-adversal:before {
  content: "\f36a"; }

.fa-affiliatetheme:before {
  content: "\f36b"; }

.fa-air-freshener:before {
  content: "\f5d0"; }

.fa-airbnb:before {
  content: "\f834"; }

.fa-algolia:before {
  content: "\f36c"; }

.fa-align-center:before {
  content: "\f037"; }

.fa-align-justify:before {
  content: "\f039"; }

.fa-align-left:before {
  content: "\f036"; }

.fa-align-right:before {
  content: "\f038"; }

.fa-alipay:before {
  content: "\f642"; }

.fa-allergies:before {
  content: "\f461"; }

.fa-amazon:before {
  content: "\f270"; }

.fa-amazon-pay:before {
  content: "\f42c"; }

.fa-ambulance:before {
  content: "\f0f9"; }

.fa-american-sign-language-interpreting:before {
  content: "\f2a3"; }

.fa-amilia:before {
  content: "\f36d"; }

.fa-anchor:before {
  content: "\f13d"; }

.fa-android:before {
  content: "\f17b"; }

.fa-angellist:before {
  content: "\f209"; }

.fa-angle-double-down:before {
  content: "\f103"; }

.fa-angle-double-left:before {
  content: "\f100"; }

.fa-angle-double-right:before {
  content: "\f101"; }

.fa-angle-double-up:before {
  content: "\f102"; }

.fa-angle-down:before {
  content: "\f107"; }

.fa-angle-left:before {
  content: "\f104"; }

.fa-angle-right:before {
  content: "\f105"; }

.fa-angle-up:before {
  content: "\f106"; }

.fa-angry:before {
  content: "\f556"; }

.fa-angrycreative:before {
  content: "\f36e"; }

.fa-angular:before {
  content: "\f420"; }

.fa-ankh:before {
  content: "\f644"; }

.fa-app-store:before {
  content: "\f36f"; }

.fa-app-store-ios:before {
  content: "\f370"; }

.fa-apper:before {
  content: "\f371"; }

.fa-apple:before {
  content: "\f179"; }

.fa-apple-alt:before {
  content: "\f5d1"; }

.fa-apple-pay:before {
  content: "\f415"; }

.fa-archive:before {
  content: "\f187"; }

.fa-archway:before {
  content: "\f557"; }

.fa-arrow-alt-circle-down:before {
  content: "\f358"; }

.fa-arrow-alt-circle-left:before {
  content: "\f359"; }

.fa-arrow-alt-circle-right:before {
  content: "\f35a"; }

.fa-arrow-alt-circle-up:before {
  content: "\f35b"; }

.fa-arrow-circle-down:before {
  content: "\f0ab"; }

.fa-arrow-circle-left:before {
  content: "\f0a8"; }

.fa-arrow-circle-right:before {
  content: "\f0a9"; }

.fa-arrow-circle-up:before {
  content: "\f0aa"; }

.fa-arrow-down:before {
  content: "\f063"; }

.fa-arrow-left:before {
  content: "\f060"; }

.fa-arrow-right:before {
  content: "\f061"; }

.fa-arrow-up:before {
  content: "\f062"; }

.fa-arrows-alt:before {
  content: "\f0b2"; }

.fa-arrows-alt-h:before {
  content: "\f337"; }

.fa-arrows-alt-v:before {
  content: "\f338"; }

.fa-artstation:before {
  content: "\f77a"; }

.fa-assistive-listening-systems:before {
  content: "\f2a2"; }

.fa-asterisk:before {
  content: "\f069"; }

.fa-asymmetrik:before {
  content: "\f372"; }

.fa-at:before {
  content: "\f1fa"; }

.fa-atlas:before {
  content: "\f558"; }

.fa-atlassian:before {
  content: "\f77b"; }

.fa-atom:before {
  content: "\f5d2"; }

.fa-audible:before {
  content: "\f373"; }

.fa-audio-description:before {
  content: "\f29e"; }

.fa-autoprefixer:before {
  content: "\f41c"; }

.fa-avianex:before {
  content: "\f374"; }

.fa-aviato:before {
  content: "\f421"; }

.fa-award:before {
  content: "\f559"; }

.fa-aws:before {
  content: "\f375"; }

.fa-baby:before {
  content: "\f77c"; }

.fa-baby-carriage:before {
  content: "\f77d"; }

.fa-backspace:before {
  content: "\f55a"; }

.fa-backward:before {
  content: "\f04a"; }

.fa-bacon:before {
  content: "\f7e5"; }

.fa-bacteria:before {
  content: "\e059"; }

.fa-bacterium:before {
  content: "\e05a"; }

.fa-bahai:before {
  content: "\f666"; }

.fa-balance-scale:before {
  content: "\f24e"; }

.fa-balance-scale-left:before {
  content: "\f515"; }

.fa-balance-scale-right:before {
  content: "\f516"; }

.fa-ban:before {
  content: "\f05e"; }

.fa-band-aid:before {
  content: "\f462"; }

.fa-bandcamp:before {
  content: "\f2d5"; }

.fa-barcode:before {
  content: "\f02a"; }

.fa-bars:before {
  content: "\f0c9"; }

.fa-baseball-ball:before {
  content: "\f433"; }

.fa-basketball-ball:before {
  content: "\f434"; }

.fa-bath:before {
  content: "\f2cd"; }

.fa-battery-empty:before {
  content: "\f244"; }

.fa-battery-full:before {
  content: "\f240"; }

.fa-battery-half:before {
  content: "\f242"; }

.fa-battery-quarter:before {
  content: "\f243"; }

.fa-battery-three-quarters:before {
  content: "\f241"; }

.fa-battle-net:before {
  content: "\f835"; }

.fa-bed:before {
  content: "\f236"; }

.fa-beer:before {
  content: "\f0fc"; }

.fa-behance:before {
  content: "\f1b4"; }

.fa-behance-square:before {
  content: "\f1b5"; }

.fa-bell:before {
  content: "\f0f3"; }

.fa-bell-slash:before {
  content: "\f1f6"; }

.fa-bezier-curve:before {
  content: "\f55b"; }

.fa-bible:before {
  content: "\f647"; }

.fa-bicycle:before {
  content: "\f206"; }

.fa-biking:before {
  content: "\f84a"; }

.fa-bimobject:before {
  content: "\f378"; }

.fa-binoculars:before {
  content: "\f1e5"; }

.fa-biohazard:before {
  content: "\f780"; }

.fa-birthday-cake:before {
  content: "\f1fd"; }

.fa-bitbucket:before {
  content: "\f171"; }

.fa-bitcoin:before {
  content: "\f379"; }

.fa-bity:before {
  content: "\f37a"; }

.fa-black-tie:before {
  content: "\f27e"; }

.fa-blackberry:before {
  content: "\f37b"; }

.fa-blender:before {
  content: "\f517"; }

.fa-blender-phone:before {
  content: "\f6b6"; }

.fa-blind:before {
  content: "\f29d"; }

.fa-blog:before {
  content: "\f781"; }

.fa-blogger:before {
  content: "\f37c"; }

.fa-blogger-b:before {
  content: "\f37d"; }

.fa-bluetooth:before {
  content: "\f293"; }

.fa-bluetooth-b:before {
  content: "\f294"; }

.fa-bold:before {
  content: "\f032"; }

.fa-bolt:before {
  content: "\f0e7"; }

.fa-bomb:before {
  content: "\f1e2"; }

.fa-bone:before {
  content: "\f5d7"; }

.fa-bong:before {
  content: "\f55c"; }

.fa-book:before {
  content: "\f02d"; }

.fa-book-dead:before {
  content: "\f6b7"; }

.fa-book-medical:before {
  content: "\f7e6"; }

.fa-book-open:before {
  content: "\f518"; }

.fa-book-reader:before {
  content: "\f5da"; }

.fa-bookmark:before {
  content: "\f02e"; }

.fa-bootstrap:before {
  content: "\f836"; }

.fa-border-all:before {
  content: "\f84c"; }

.fa-border-none:before {
  content: "\f850"; }

.fa-border-style:before {
  content: "\f853"; }

.fa-bowling-ball:before {
  content: "\f436"; }

.fa-box:before {
  content: "\f466"; }

.fa-box-open:before {
  content: "\f49e"; }

.fa-box-tissue:before {
  content: "\e05b"; }

.fa-boxes:before {
  content: "\f468"; }

.fa-braille:before {
  content: "\f2a1"; }

.fa-brain:before {
  content: "\f5dc"; }

.fa-bread-slice:before {
  content: "\f7ec"; }

.fa-briefcase:before {
  content: "\f0b1"; }

.fa-briefcase-medical:before {
  content: "\f469"; }

.fa-broadcast-tower:before {
  content: "\f519"; }

.fa-broom:before {
  content: "\f51a"; }

.fa-brush:before {
  content: "\f55d"; }

.fa-btc:before {
  content: "\f15a"; }

.fa-buffer:before {
  content: "\f837"; }

.fa-bug:before {
  content: "\f188"; }

.fa-building:before {
  content: "\f1ad"; }

.fa-bullhorn:before {
  content: "\f0a1"; }

.fa-bullseye:before {
  content: "\f140"; }

.fa-burn:before {
  content: "\f46a"; }

.fa-buromobelexperte:before {
  content: "\f37f"; }

.fa-bus:before {
  content: "\f207"; }

.fa-bus-alt:before {
  content: "\f55e"; }

.fa-business-time:before {
  content: "\f64a"; }

.fa-buy-n-large:before {
  content: "\f8a6"; }

.fa-buysellads:before {
  content: "\f20d"; }

.fa-calculator:before {
  content: "\f1ec"; }

.fa-calendar:before {
  content: "\f133"; }

.fa-calendar-alt:before {
  content: "\f073"; }

.fa-calendar-check:before {
  content: "\f274"; }

.fa-calendar-day:before {
  content: "\f783"; }

.fa-calendar-minus:before {
  content: "\f272"; }

.fa-calendar-plus:before {
  content: "\f271"; }

.fa-calendar-times:before {
  content: "\f273"; }

.fa-calendar-week:before {
  content: "\f784"; }

.fa-camera:before {
  content: "\f030"; }

.fa-camera-retro:before {
  content: "\f083"; }

.fa-campground:before {
  content: "\f6bb"; }

.fa-canadian-maple-leaf:before {
  content: "\f785"; }

.fa-candy-cane:before {
  content: "\f786"; }

.fa-cannabis:before {
  content: "\f55f"; }

.fa-capsules:before {
  content: "\f46b"; }

.fa-car:before {
  content: "\f1b9"; }

.fa-car-alt:before {
  content: "\f5de"; }

.fa-car-battery:before {
  content: "\f5df"; }

.fa-car-crash:before {
  content: "\f5e1"; }

.fa-car-side:before {
  content: "\f5e4"; }

.fa-caravan:before {
  content: "\f8ff"; }

.fa-caret-down:before {
  content: "\f0d7"; }

.fa-caret-left:before {
  content: "\f0d9"; }

.fa-caret-right:before {
  content: "\f0da"; }

.fa-caret-square-down:before {
  content: "\f150"; }

.fa-caret-square-left:before {
  content: "\f191"; }

.fa-caret-square-right:before {
  content: "\f152"; }

.fa-caret-square-up:before {
  content: "\f151"; }

.fa-caret-up:before {
  content: "\f0d8"; }

.fa-carrot:before {
  content: "\f787"; }

.fa-cart-arrow-down:before {
  content: "\f218"; }

.fa-cart-plus:before {
  content: "\f217"; }

.fa-cash-register:before {
  content: "\f788"; }

.fa-cat:before {
  content: "\f6be"; }

.fa-cc-amazon-pay:before {
  content: "\f42d"; }

.fa-cc-amex:before {
  content: "\f1f3"; }

.fa-cc-apple-pay:before {
  content: "\f416"; }

.fa-cc-diners-club:before {
  content: "\f24c"; }

.fa-cc-discover:before {
  content: "\f1f2"; }

.fa-cc-jcb:before {
  content: "\f24b"; }

.fa-cc-mastercard:before {
  content: "\f1f1"; }

.fa-cc-paypal:before {
  content: "\f1f4"; }

.fa-cc-stripe:before {
  content: "\f1f5"; }

.fa-cc-visa:before {
  content: "\f1f0"; }

.fa-centercode:before {
  content: "\f380"; }

.fa-centos:before {
  content: "\f789"; }

.fa-certificate:before {
  content: "\f0a3"; }

.fa-chair:before {
  content: "\f6c0"; }

.fa-chalkboard:before {
  content: "\f51b"; }

.fa-chalkboard-teacher:before {
  content: "\f51c"; }

.fa-charging-station:before {
  content: "\f5e7"; }

.fa-chart-area:before {
  content: "\f1fe"; }

.fa-chart-bar:before {
  content: "\f080"; }

.fa-chart-line:before {
  content: "\f201"; }

.fa-chart-pie:before {
  content: "\f200"; }

.fa-check:before {
  content: "\f00c"; }

.fa-check-circle:before {
  content: "\f058"; }

.fa-check-double:before {
  content: "\f560"; }

.fa-check-square:before {
  content: "\f14a"; }

.fa-cheese:before {
  content: "\f7ef"; }

.fa-chess:before {
  content: "\f439"; }

.fa-chess-bishop:before {
  content: "\f43a"; }

.fa-chess-board:before {
  content: "\f43c"; }

.fa-chess-king:before {
  content: "\f43f"; }

.fa-chess-knight:before {
  content: "\f441"; }

.fa-chess-pawn:before {
  content: "\f443"; }

.fa-chess-queen:before {
  content: "\f445"; }

.fa-chess-rook:before {
  content: "\f447"; }

.fa-chevron-circle-down:before {
  content: "\f13a"; }

.fa-chevron-circle-left:before {
  content: "\f137"; }

.fa-chevron-circle-right:before {
  content: "\f138"; }

.fa-chevron-circle-up:before {
  content: "\f139"; }

.fa-chevron-down:before {
  content: "\f078"; }

.fa-chevron-left:before {
  content: "\f053"; }

.fa-chevron-right:before {
  content: "\f054"; }

.fa-chevron-up:before {
  content: "\f077"; }

.fa-child:before {
  content: "\f1ae"; }

.fa-chrome:before {
  content: "\f268"; }

.fa-chromecast:before {
  content: "\f838"; }

.fa-church:before {
  content: "\f51d"; }

.fa-circle:before {
  content: "\f111"; }

.fa-circle-notch:before {
  content: "\f1ce"; }

.fa-city:before {
  content: "\f64f"; }

.fa-clinic-medical:before {
  content: "\f7f2"; }

.fa-clipboard:before {
  content: "\f328"; }

.fa-clipboard-check:before {
  content: "\f46c"; }

.fa-clipboard-list:before {
  content: "\f46d"; }

.fa-clock:before {
  content: "\f017"; }

.fa-clone:before {
  content: "\f24d"; }

.fa-closed-captioning:before {
  content: "\f20a"; }

.fa-cloud:before {
  content: "\f0c2"; }

.fa-cloud-download-alt:before {
  content: "\f381"; }

.fa-cloud-meatball:before {
  content: "\f73b"; }

.fa-cloud-moon:before {
  content: "\f6c3"; }

.fa-cloud-moon-rain:before {
  content: "\f73c"; }

.fa-cloud-rain:before {
  content: "\f73d"; }

.fa-cloud-showers-heavy:before {
  content: "\f740"; }

.fa-cloud-sun:before {
  content: "\f6c4"; }

.fa-cloud-sun-rain:before {
  content: "\f743"; }

.fa-cloud-upload-alt:before {
  content: "\f382"; }

.fa-cloudscale:before {
  content: "\f383"; }

.fa-cloudsmith:before {
  content: "\f384"; }

.fa-cloudversify:before {
  content: "\f385"; }

.fa-cocktail:before {
  content: "\f561"; }

.fa-code:before {
  content: "\f121"; }

.fa-code-branch:before {
  content: "\f126"; }

.fa-codepen:before {
  content: "\f1cb"; }

.fa-codiepie:before {
  content: "\f284"; }

.fa-coffee:before {
  content: "\f0f4"; }

.fa-cog:before {
  content: "\f013"; }

.fa-cogs:before {
  content: "\f085"; }

.fa-coins:before {
  content: "\f51e"; }

.fa-columns:before {
  content: "\f0db"; }

.fa-comment:before {
  content: "\f075"; }

.fa-comment-alt:before {
  content: "\f27a"; }

.fa-comment-dollar:before {
  content: "\f651"; }

.fa-comment-dots:before {
  content: "\f4ad"; }

.fa-comment-medical:before {
  content: "\f7f5"; }

.fa-comment-slash:before {
  content: "\f4b3"; }

.fa-comments:before {
  content: "\f086"; }

.fa-comments-dollar:before {
  content: "\f653"; }

.fa-compact-disc:before {
  content: "\f51f"; }

.fa-compass:before {
  content: "\f14e"; }

.fa-compress:before {
  content: "\f066"; }

.fa-compress-alt:before {
  content: "\f422"; }

.fa-compress-arrows-alt:before {
  content: "\f78c"; }

.fa-concierge-bell:before {
  content: "\f562"; }

.fa-confluence:before {
  content: "\f78d"; }

.fa-connectdevelop:before {
  content: "\f20e"; }

.fa-contao:before {
  content: "\f26d"; }

.fa-cookie:before {
  content: "\f563"; }

.fa-cookie-bite:before {
  content: "\f564"; }

.fa-copy:before {
  content: "\f0c5"; }

.fa-copyright:before {
  content: "\f1f9"; }

.fa-cotton-bureau:before {
  content: "\f89e"; }

.fa-couch:before {
  content: "\f4b8"; }

.fa-cpanel:before {
  content: "\f388"; }

.fa-creative-commons:before {
  content: "\f25e"; }

.fa-creative-commons-by:before {
  content: "\f4e7"; }

.fa-creative-commons-nc:before {
  content: "\f4e8"; }

.fa-creative-commons-nc-eu:before {
  content: "\f4e9"; }

.fa-creative-commons-nc-jp:before {
  content: "\f4ea"; }

.fa-creative-commons-nd:before {
  content: "\f4eb"; }

.fa-creative-commons-pd:before {
  content: "\f4ec"; }

.fa-creative-commons-pd-alt:before {
  content: "\f4ed"; }

.fa-creative-commons-remix:before {
  content: "\f4ee"; }

.fa-creative-commons-sa:before {
  content: "\f4ef"; }

.fa-creative-commons-sampling:before {
  content: "\f4f0"; }

.fa-creative-commons-sampling-plus:before {
  content: "\f4f1"; }

.fa-creative-commons-share:before {
  content: "\f4f2"; }

.fa-creative-commons-zero:before {
  content: "\f4f3"; }

.fa-credit-card:before {
  content: "\f09d"; }

.fa-critical-role:before {
  content: "\f6c9"; }

.fa-crop:before {
  content: "\f125"; }

.fa-crop-alt:before {
  content: "\f565"; }

.fa-cross:before {
  content: "\f654"; }

.fa-crosshairs:before {
  content: "\f05b"; }

.fa-crow:before {
  content: "\f520"; }

.fa-crown:before {
  content: "\f521"; }

.fa-crutch:before {
  content: "\f7f7"; }

.fa-css3:before {
  content: "\f13c"; }

.fa-css3-alt:before {
  content: "\f38b"; }

.fa-cube:before {
  content: "\f1b2"; }

.fa-cubes:before {
  content: "\f1b3"; }

.fa-cut:before {
  content: "\f0c4"; }

.fa-cuttlefish:before {
  content: "\f38c"; }

.fa-d-and-d:before {
  content: "\f38d"; }

.fa-d-and-d-beyond:before {
  content: "\f6ca"; }

.fa-dailymotion:before {
  content: "\e052"; }

.fa-dashcube:before {
  content: "\f210"; }

.fa-database:before {
  content: "\f1c0"; }

.fa-deaf:before {
  content: "\f2a4"; }

.fa-deezer:before {
  content: "\e077"; }

.fa-delicious:before {
  content: "\f1a5"; }

.fa-democrat:before {
  content: "\f747"; }

.fa-deploydog:before {
  content: "\f38e"; }

.fa-deskpro:before {
  content: "\f38f"; }

.fa-desktop:before {
  content: "\f108"; }

.fa-dev:before {
  content: "\f6cc"; }

.fa-deviantart:before {
  content: "\f1bd"; }

.fa-dharmachakra:before {
  content: "\f655"; }

.fa-dhl:before {
  content: "\f790"; }

.fa-diagnoses:before {
  content: "\f470"; }

.fa-diaspora:before {
  content: "\f791"; }

.fa-dice:before {
  content: "\f522"; }

.fa-dice-d20:before {
  content: "\f6cf"; }

.fa-dice-d6:before {
  content: "\f6d1"; }

.fa-dice-five:before {
  content: "\f523"; }

.fa-dice-four:before {
  content: "\f524"; }

.fa-dice-one:before {
  content: "\f525"; }

.fa-dice-six:before {
  content: "\f526"; }

.fa-dice-three:before {
  content: "\f527"; }

.fa-dice-two:before {
  content: "\f528"; }

.fa-digg:before {
  content: "\f1a6"; }

.fa-digital-ocean:before {
  content: "\f391"; }

.fa-digital-tachograph:before {
  content: "\f566"; }

.fa-directions:before {
  content: "\f5eb"; }

.fa-discord:before {
  content: "\f392"; }

.fa-discourse:before {
  content: "\f393"; }

.fa-disease:before {
  content: "\f7fa"; }

.fa-divide:before {
  content: "\f529"; }

.fa-dizzy:before {
  content: "\f567"; }

.fa-dna:before {
  content: "\f471"; }

.fa-dochub:before {
  content: "\f394"; }

.fa-docker:before {
  content: "\f395"; }

.fa-dog:before {
  content: "\f6d3"; }

.fa-dollar-sign:before {
  content: "\f155"; }

.fa-dolly:before {
  content: "\f472"; }

.fa-dolly-flatbed:before {
  content: "\f474"; }

.fa-donate:before {
  content: "\f4b9"; }

.fa-door-closed:before {
  content: "\f52a"; }

.fa-door-open:before {
  content: "\f52b"; }

.fa-dot-circle:before {
  content: "\f192"; }

.fa-dove:before {
  content: "\f4ba"; }

.fa-download:before {
  content: "\f019"; }

.fa-draft2digital:before {
  content: "\f396"; }

.fa-drafting-compass:before {
  content: "\f568"; }

.fa-dragon:before {
  content: "\f6d5"; }

.fa-draw-polygon:before {
  content: "\f5ee"; }

.fa-dribbble:before {
  content: "\f17d"; }

.fa-dribbble-square:before {
  content: "\f397"; }

.fa-dropbox:before {
  content: "\f16b"; }

.fa-drum:before {
  content: "\f569"; }

.fa-drum-steelpan:before {
  content: "\f56a"; }

.fa-drumstick-bite:before {
  content: "\f6d7"; }

.fa-drupal:before {
  content: "\f1a9"; }

.fa-dumbbell:before {
  content: "\f44b"; }

.fa-dumpster:before {
  content: "\f793"; }

.fa-dumpster-fire:before {
  content: "\f794"; }

.fa-dungeon:before {
  content: "\f6d9"; }

.fa-dyalog:before {
  content: "\f399"; }

.fa-earlybirds:before {
  content: "\f39a"; }

.fa-ebay:before {
  content: "\f4f4"; }

.fa-edge:before {
  content: "\f282"; }

.fa-edge-legacy:before {
  content: "\e078"; }

.fa-edit:before {
  content: "\f044"; }

.fa-egg:before {
  content: "\f7fb"; }

.fa-eject:before {
  content: "\f052"; }

.fa-elementor:before {
  content: "\f430"; }

.fa-ellipsis-h:before {
  content: "\f141"; }

.fa-ellipsis-v:before {
  content: "\f142"; }

.fa-ello:before {
  content: "\f5f1"; }

.fa-ember:before {
  content: "\f423"; }

.fa-empire:before {
  content: "\f1d1"; }

.fa-envelope:before {
  content: "\f0e0"; }

.fa-envelope-open:before {
  content: "\f2b6"; }

.fa-envelope-open-text:before {
  content: "\f658"; }

.fa-envelope-square:before {
  content: "\f199"; }

.fa-envira:before {
  content: "\f299"; }

.fa-equals:before {
  content: "\f52c"; }

.fa-eraser:before {
  content: "\f12d"; }

.fa-erlang:before {
  content: "\f39d"; }

.fa-ethereum:before {
  content: "\f42e"; }

.fa-ethernet:before {
  content: "\f796"; }

.fa-etsy:before {
  content: "\f2d7"; }

.fa-euro-sign:before {
  content: "\f153"; }

.fa-evernote:before {
  content: "\f839"; }

.fa-exchange-alt:before {
  content: "\f362"; }

.fa-exclamation:before {
  content: "\f12a"; }

.fa-exclamation-circle:before {
  content: "\f06a"; }

.fa-exclamation-triangle:before {
  content: "\f071"; }

.fa-expand:before {
  content: "\f065"; }

.fa-expand-alt:before {
  content: "\f424"; }

.fa-expand-arrows-alt:before {
  content: "\f31e"; }

.fa-expeditedssl:before {
  content: "\f23e"; }

.fa-external-link-alt:before {
  content: "\f35d"; }

.fa-external-link-square-alt:before {
  content: "\f360"; }

.fa-eye:before {
  content: "\f06e"; }

.fa-eye-dropper:before {
  content: "\f1fb"; }

.fa-eye-slash:before {
  content: "\f070"; }

.fa-facebook:before {
  content: "\f09a"; }

.fa-facebook-f:before {
  content: "\f39e"; }

.fa-facebook-messenger:before {
  content: "\f39f"; }

.fa-facebook-square:before {
  content: "\f082"; }

.fa-fan:before {
  content: "\f863"; }

.fa-fantasy-flight-games:before {
  content: "\f6dc"; }

.fa-fast-backward:before {
  content: "\f049"; }

.fa-fast-forward:before {
  content: "\f050"; }

.fa-faucet:before {
  content: "\e005"; }

.fa-fax:before {
  content: "\f1ac"; }

.fa-feather:before {
  content: "\f52d"; }

.fa-feather-alt:before {
  content: "\f56b"; }

.fa-fedex:before {
  content: "\f797"; }

.fa-fedora:before {
  content: "\f798"; }

.fa-female:before {
  content: "\f182"; }

.fa-fighter-jet:before {
  content: "\f0fb"; }

.fa-figma:before {
  content: "\f799"; }

.fa-file:before {
  content: "\f15b"; }

.fa-file-alt:before {
  content: "\f15c"; }

.fa-file-archive:before {
  content: "\f1c6"; }

.fa-file-audio:before {
  content: "\f1c7"; }

.fa-file-code:before {
  content: "\f1c9"; }

.fa-file-contract:before {
  content: "\f56c"; }

.fa-file-csv:before {
  content: "\f6dd"; }

.fa-file-download:before {
  content: "\f56d"; }

.fa-file-excel:before {
  content: "\f1c3"; }

.fa-file-export:before {
  content: "\f56e"; }

.fa-file-image:before {
  content: "\f1c5"; }

.fa-file-import:before {
  content: "\f56f"; }

.fa-file-invoice:before {
  content: "\f570"; }

.fa-file-invoice-dollar:before {
  content: "\f571"; }

.fa-file-medical:before {
  content: "\f477"; }

.fa-file-medical-alt:before {
  content: "\f478"; }

.fa-file-pdf:before {
  content: "\f1c1"; }

.fa-file-powerpoint:before {
  content: "\f1c4"; }

.fa-file-prescription:before {
  content: "\f572"; }

.fa-file-signature:before {
  content: "\f573"; }

.fa-file-upload:before {
  content: "\f574"; }

.fa-file-video:before {
  content: "\f1c8"; }

.fa-file-word:before {
  content: "\f1c2"; }

.fa-fill:before {
  content: "\f575"; }

.fa-fill-drip:before {
  content: "\f576"; }

.fa-film:before {
  content: "\f008"; }

.fa-filter:before {
  content: "\f0b0"; }

.fa-fingerprint:before {
  content: "\f577"; }

.fa-fire:before {
  content: "\f06d"; }

.fa-fire-alt:before {
  content: "\f7e4"; }

.fa-fire-extinguisher:before {
  content: "\f134"; }

.fa-firefox:before {
  content: "\f269"; }

.fa-firefox-browser:before {
  content: "\e007"; }

.fa-first-aid:before {
  content: "\f479"; }

.fa-first-order:before {
  content: "\f2b0"; }

.fa-first-order-alt:before {
  content: "\f50a"; }

.fa-firstdraft:before {
  content: "\f3a1"; }

.fa-fish:before {
  content: "\f578"; }

.fa-fist-raised:before {
  content: "\f6de"; }

.fa-flag:before {
  content: "\f024"; }

.fa-flag-checkered:before {
  content: "\f11e"; }

.fa-flag-usa:before {
  content: "\f74d"; }

.fa-flask:before {
  content: "\f0c3"; }

.fa-flickr:before {
  content: "\f16e"; }

.fa-flipboard:before {
  content: "\f44d"; }

.fa-flushed:before {
  content: "\f579"; }

.fa-fly:before {
  content: "\f417"; }

.fa-folder:before {
  content: "\f07b"; }

.fa-folder-minus:before {
  content: "\f65d"; }

.fa-folder-open:before {
  content: "\f07c"; }

.fa-folder-plus:before {
  content: "\f65e"; }

.fa-font:before {
  content: "\f031"; }

.fa-font-awesome:before {
  content: "\f2b4"; }

.fa-font-awesome-alt:before {
  content: "\f35c"; }

.fa-font-awesome-flag:before {
  content: "\f425"; }

.fa-font-awesome-logo-full:before {
  content: "\f4e6"; }

.fa-fonticons:before {
  content: "\f280"; }

.fa-fonticons-fi:before {
  content: "\f3a2"; }

.fa-football-ball:before {
  content: "\f44e"; }

.fa-fort-awesome:before {
  content: "\f286"; }

.fa-fort-awesome-alt:before {
  content: "\f3a3"; }

.fa-forumbee:before {
  content: "\f211"; }

.fa-forward:before {
  content: "\f04e"; }

.fa-foursquare:before {
  content: "\f180"; }

.fa-free-code-camp:before {
  content: "\f2c5"; }

.fa-freebsd:before {
  content: "\f3a4"; }

.fa-frog:before {
  content: "\f52e"; }

.fa-frown:before {
  content: "\f119"; }

.fa-frown-open:before {
  content: "\f57a"; }

.fa-fulcrum:before {
  content: "\f50b"; }

.fa-funnel-dollar:before {
  content: "\f662"; }

.fa-futbol:before {
  content: "\f1e3"; }

.fa-galactic-republic:before {
  content: "\f50c"; }

.fa-galactic-senate:before {
  content: "\f50d"; }

.fa-gamepad:before {
  content: "\f11b"; }

.fa-gas-pump:before {
  content: "\f52f"; }

.fa-gavel:before {
  content: "\f0e3"; }

.fa-gem:before {
  content: "\f3a5"; }

.fa-genderless:before {
  content: "\f22d"; }

.fa-get-pocket:before {
  content: "\f265"; }

.fa-gg:before {
  content: "\f260"; }

.fa-gg-circle:before {
  content: "\f261"; }

.fa-ghost:before {
  content: "\f6e2"; }

.fa-gift:before {
  content: "\f06b"; }

.fa-gifts:before {
  content: "\f79c"; }

.fa-git:before {
  content: "\f1d3"; }

.fa-git-alt:before {
  content: "\f841"; }

.fa-git-square:before {
  content: "\f1d2"; }

.fa-github:before {
  content: "\f09b"; }

.fa-github-alt:before {
  content: "\f113"; }

.fa-github-square:before {
  content: "\f092"; }

.fa-gitkraken:before {
  content: "\f3a6"; }

.fa-gitlab:before {
  content: "\f296"; }

.fa-gitter:before {
  content: "\f426"; }

.fa-glass-cheers:before {
  content: "\f79f"; }

.fa-glass-martini:before {
  content: "\f000"; }

.fa-glass-martini-alt:before {
  content: "\f57b"; }

.fa-glass-whiskey:before {
  content: "\f7a0"; }

.fa-glasses:before {
  content: "\f530"; }

.fa-glide:before {
  content: "\f2a5"; }

.fa-glide-g:before {
  content: "\f2a6"; }

.fa-globe:before {
  content: "\f0ac"; }

.fa-globe-africa:before {
  content: "\f57c"; }

.fa-globe-americas:before {
  content: "\f57d"; }

.fa-globe-asia:before {
  content: "\f57e"; }

.fa-globe-europe:before {
  content: "\f7a2"; }

.fa-gofore:before {
  content: "\f3a7"; }

.fa-golf-ball:before {
  content: "\f450"; }

.fa-goodreads:before {
  content: "\f3a8"; }

.fa-goodreads-g:before {
  content: "\f3a9"; }

.fa-google:before {
  content: "\f1a0"; }

.fa-google-drive:before {
  content: "\f3aa"; }

.fa-google-pay:before {
  content: "\e079"; }

.fa-google-play:before {
  content: "\f3ab"; }

.fa-google-plus:before {
  content: "\f2b3"; }

.fa-google-plus-g:before {
  content: "\f0d5"; }

.fa-google-plus-square:before {
  content: "\f0d4"; }

.fa-google-wallet:before {
  content: "\f1ee"; }

.fa-gopuram:before {
  content: "\f664"; }

.fa-graduation-cap:before {
  content: "\f19d"; }

.fa-gratipay:before {
  content: "\f184"; }

.fa-grav:before {
  content: "\f2d6"; }

.fa-greater-than:before {
  content: "\f531"; }

.fa-greater-than-equal:before {
  content: "\f532"; }

.fa-grimace:before {
  content: "\f57f"; }

.fa-grin:before {
  content: "\f580"; }

.fa-grin-alt:before {
  content: "\f581"; }

.fa-grin-beam:before {
  content: "\f582"; }

.fa-grin-beam-sweat:before {
  content: "\f583"; }

.fa-grin-hearts:before {
  content: "\f584"; }

.fa-grin-squint:before {
  content: "\f585"; }

.fa-grin-squint-tears:before {
  content: "\f586"; }

.fa-grin-stars:before {
  content: "\f587"; }

.fa-grin-tears:before {
  content: "\f588"; }

.fa-grin-tongue:before {
  content: "\f589"; }

.fa-grin-tongue-squint:before {
  content: "\f58a"; }

.fa-grin-tongue-wink:before {
  content: "\f58b"; }

.fa-grin-wink:before {
  content: "\f58c"; }

.fa-grip-horizontal:before {
  content: "\f58d"; }

.fa-grip-lines:before {
  content: "\f7a4"; }

.fa-grip-lines-vertical:before {
  content: "\f7a5"; }

.fa-grip-vertical:before {
  content: "\f58e"; }

.fa-gripfire:before {
  content: "\f3ac"; }

.fa-grunt:before {
  content: "\f3ad"; }

.fa-guitar:before {
  content: "\f7a6"; }

.fa-gulp:before {
  content: "\f3ae"; }

.fa-h-square:before {
  content: "\f0fd"; }

.fa-hacker-news:before {
  content: "\f1d4"; }

.fa-hacker-news-square:before {
  content: "\f3af"; }

.fa-hackerrank:before {
  content: "\f5f7"; }

.fa-hamburger:before {
  content: "\f805"; }

.fa-hammer:before {
  content: "\f6e3"; }

.fa-hamsa:before {
  content: "\f665"; }

.fa-hand-holding:before {
  content: "\f4bd"; }

.fa-hand-holding-heart:before {
  content: "\f4be"; }

.fa-hand-holding-medical:before {
  content: "\e05c"; }

.fa-hand-holding-usd:before {
  content: "\f4c0"; }

.fa-hand-holding-water:before {
  content: "\f4c1"; }

.fa-hand-lizard:before {
  content: "\f258"; }

.fa-hand-middle-finger:before {
  content: "\f806"; }

.fa-hand-paper:before {
  content: "\f256"; }

.fa-hand-peace:before {
  content: "\f25b"; }

.fa-hand-point-down:before {
  content: "\f0a7"; }

.fa-hand-point-left:before {
  content: "\f0a5"; }

.fa-hand-point-right:before {
  content: "\f0a4"; }

.fa-hand-point-up:before {
  content: "\f0a6"; }

.fa-hand-pointer:before {
  content: "\f25a"; }

.fa-hand-rock:before {
  content: "\f255"; }

.fa-hand-scissors:before {
  content: "\f257"; }

.fa-hand-sparkles:before {
  content: "\e05d"; }

.fa-hand-spock:before {
  content: "\f259"; }

.fa-hands:before {
  content: "\f4c2"; }

.fa-hands-helping:before {
  content: "\f4c4"; }

.fa-hands-wash:before {
  content: "\e05e"; }

.fa-handshake:before {
  content: "\f2b5"; }

.fa-handshake-alt-slash:before {
  content: "\e05f"; }

.fa-handshake-slash:before {
  content: "\e060"; }

.fa-hanukiah:before {
  content: "\f6e6"; }

.fa-hard-hat:before {
  content: "\f807"; }

.fa-hashtag:before {
  content: "\f292"; }

.fa-hat-cowboy:before {
  content: "\f8c0"; }

.fa-hat-cowboy-side:before {
  content: "\f8c1"; }

.fa-hat-wizard:before {
  content: "\f6e8"; }

.fa-hdd:before {
  content: "\f0a0"; }

.fa-head-side-cough:before {
  content: "\e061"; }

.fa-head-side-cough-slash:before {
  content: "\e062"; }

.fa-head-side-mask:before {
  content: "\e063"; }

.fa-head-side-virus:before {
  content: "\e064"; }

.fa-heading:before {
  content: "\f1dc"; }

.fa-headphones:before {
  content: "\f025"; }

.fa-headphones-alt:before {
  content: "\f58f"; }

.fa-headset:before {
  content: "\f590"; }

.fa-heart:before {
  content: "\f004"; }

.fa-heart-broken:before {
  content: "\f7a9"; }

.fa-heartbeat:before {
  content: "\f21e"; }

.fa-helicopter:before {
  content: "\f533"; }

.fa-highlighter:before {
  content: "\f591"; }

.fa-hiking:before {
  content: "\f6ec"; }

.fa-hippo:before {
  content: "\f6ed"; }

.fa-hips:before {
  content: "\f452"; }

.fa-hire-a-helper:before {
  content: "\f3b0"; }

.fa-history:before {
  content: "\f1da"; }

.fa-hockey-puck:before {
  content: "\f453"; }

.fa-holly-berry:before {
  content: "\f7aa"; }

.fa-home:before {
  content: "\f015"; }

.fa-hooli:before {
  content: "\f427"; }

.fa-hornbill:before {
  content: "\f592"; }

.fa-horse:before {
  content: "\f6f0"; }

.fa-horse-head:before {
  content: "\f7ab"; }

.fa-hospital:before {
  content: "\f0f8"; }

.fa-hospital-alt:before {
  content: "\f47d"; }

.fa-hospital-symbol:before {
  content: "\f47e"; }

.fa-hospital-user:before {
  content: "\f80d"; }

.fa-hot-tub:before {
  content: "\f593"; }

.fa-hotdog:before {
  content: "\f80f"; }

.fa-hotel:before {
  content: "\f594"; }

.fa-hotjar:before {
  content: "\f3b1"; }

.fa-hourglass:before {
  content: "\f254"; }

.fa-hourglass-end:before {
  content: "\f253"; }

.fa-hourglass-half:before {
  content: "\f252"; }

.fa-hourglass-start:before {
  content: "\f251"; }

.fa-house-damage:before {
  content: "\f6f1"; }

.fa-house-user:before {
  content: "\e065"; }

.fa-houzz:before {
  content: "\f27c"; }

.fa-hryvnia:before {
  content: "\f6f2"; }

.fa-html5:before {
  content: "\f13b"; }

.fa-hubspot:before {
  content: "\f3b2"; }

.fa-i-cursor:before {
  content: "\f246"; }

.fa-ice-cream:before {
  content: "\f810"; }

.fa-icicles:before {
  content: "\f7ad"; }

.fa-icons:before {
  content: "\f86d"; }

.fa-id-badge:before {
  content: "\f2c1"; }

.fa-id-card:before {
  content: "\f2c2"; }

.fa-id-card-alt:before {
  content: "\f47f"; }

.fa-ideal:before {
  content: "\e013"; }

.fa-igloo:before {
  content: "\f7ae"; }

.fa-image:before {
  content: "\f03e"; }

.fa-images:before {
  content: "\f302"; }

.fa-imdb:before {
  content: "\f2d8"; }

.fa-inbox:before {
  content: "\f01c"; }

.fa-indent:before {
  content: "\f03c"; }

.fa-industry:before {
  content: "\f275"; }

.fa-infinity:before {
  content: "\f534"; }

.fa-info:before {
  content: "\f129"; }

.fa-info-circle:before {
  content: "\f05a"; }

.fa-instagram:before {
  content: "\f16d"; }

.fa-instagram-square:before {
  content: "\e055"; }

.fa-intercom:before {
  content: "\f7af"; }

.fa-internet-explorer:before {
  content: "\f26b"; }

.fa-invision:before {
  content: "\f7b0"; }

.fa-ioxhost:before {
  content: "\f208"; }

.fa-italic:before {
  content: "\f033"; }

.fa-itch-io:before {
  content: "\f83a"; }

.fa-itunes:before {
  content: "\f3b4"; }

.fa-itunes-note:before {
  content: "\f3b5"; }

.fa-java:before {
  content: "\f4e4"; }

.fa-jedi:before {
  content: "\f669"; }

.fa-jedi-order:before {
  content: "\f50e"; }

.fa-jenkins:before {
  content: "\f3b6"; }

.fa-jira:before {
  content: "\f7b1"; }

.fa-joget:before {
  content: "\f3b7"; }

.fa-joint:before {
  content: "\f595"; }

.fa-joomla:before {
  content: "\f1aa"; }

.fa-journal-whills:before {
  content: "\f66a"; }

.fa-js:before {
  content: "\f3b8"; }

.fa-js-square:before {
  content: "\f3b9"; }

.fa-jsfiddle:before {
  content: "\f1cc"; }

.fa-kaaba:before {
  content: "\f66b"; }

.fa-kaggle:before {
  content: "\f5fa"; }

.fa-key:before {
  content: "\f084"; }

.fa-keybase:before {
  content: "\f4f5"; }

.fa-keyboard:before {
  content: "\f11c"; }

.fa-keycdn:before {
  content: "\f3ba"; }

.fa-khanda:before {
  content: "\f66d"; }

.fa-kickstarter:before {
  content: "\f3bb"; }

.fa-kickstarter-k:before {
  content: "\f3bc"; }

.fa-kiss:before {
  content: "\f596"; }

.fa-kiss-beam:before {
  content: "\f597"; }

.fa-kiss-wink-heart:before {
  content: "\f598"; }

.fa-kiwi-bird:before {
  content: "\f535"; }

.fa-korvue:before {
  content: "\f42f"; }

.fa-landmark:before {
  content: "\f66f"; }

.fa-language:before {
  content: "\f1ab"; }

.fa-laptop:before {
  content: "\f109"; }

.fa-laptop-code:before {
  content: "\f5fc"; }

.fa-laptop-house:before {
  content: "\e066"; }

.fa-laptop-medical:before {
  content: "\f812"; }

.fa-laravel:before {
  content: "\f3bd"; }

.fa-lastfm:before {
  content: "\f202"; }

.fa-lastfm-square:before {
  content: "\f203"; }

.fa-laugh:before {
  content: "\f599"; }

.fa-laugh-beam:before {
  content: "\f59a"; }

.fa-laugh-squint:before {
  content: "\f59b"; }

.fa-laugh-wink:before {
  content: "\f59c"; }

.fa-layer-group:before {
  content: "\f5fd"; }

.fa-leaf:before {
  content: "\f06c"; }

.fa-leanpub:before {
  content: "\f212"; }

.fa-lemon:before {
  content: "\f094"; }

.fa-less:before {
  content: "\f41d"; }

.fa-less-than:before {
  content: "\f536"; }

.fa-less-than-equal:before {
  content: "\f537"; }

.fa-level-down-alt:before {
  content: "\f3be"; }

.fa-level-up-alt:before {
  content: "\f3bf"; }

.fa-life-ring:before {
  content: "\f1cd"; }

.fa-lightbulb:before {
  content: "\f0eb"; }

.fa-line:before {
  content: "\f3c0"; }

.fa-link:before {
  content: "\f0c1"; }

.fa-linkedin:before {
  content: "\f08c"; }

.fa-linkedin-in:before {
  content: "\f0e1"; }

.fa-linode:before {
  content: "\f2b8"; }

.fa-linux:before {
  content: "\f17c"; }

.fa-lira-sign:before {
  content: "\f195"; }

.fa-list:before {
  content: "\f03a"; }

.fa-list-alt:before {
  content: "\f022"; }

.fa-list-ol:before {
  content: "\f0cb"; }

.fa-list-ul:before {
  content: "\f0ca"; }

.fa-location-arrow:before {
  content: "\f124"; }

.fa-lock:before {
  content: "\f023"; }

.fa-lock-open:before {
  content: "\f3c1"; }

.fa-long-arrow-alt-down:before {
  content: "\f309"; }

.fa-long-arrow-alt-left:before {
  content: "\f30a"; }

.fa-long-arrow-alt-right:before {
  content: "\f30b"; }

.fa-long-arrow-alt-up:before {
  content: "\f30c"; }

.fa-low-vision:before {
  content: "\f2a8"; }

.fa-luggage-cart:before {
  content: "\f59d"; }

.fa-lungs:before {
  content: "\f604"; }

.fa-lungs-virus:before {
  content: "\e067"; }

.fa-lyft:before {
  content: "\f3c3"; }

.fa-magento:before {
  content: "\f3c4"; }

.fa-magic:before {
  content: "\f0d0"; }

.fa-magnet:before {
  content: "\f076"; }

.fa-mail-bulk:before {
  content: "\f674"; }

.fa-mailchimp:before {
  content: "\f59e"; }

.fa-male:before {
  content: "\f183"; }

.fa-mandalorian:before {
  content: "\f50f"; }

.fa-map:before {
  content: "\f279"; }

.fa-map-marked:before {
  content: "\f59f"; }

.fa-map-marked-alt:before {
  content: "\f5a0"; }

.fa-map-marker:before {
  content: "\f041"; }

.fa-map-marker-alt:before {
  content: "\f3c5"; }

.fa-map-pin:before {
  content: "\f276"; }

.fa-map-signs:before {
  content: "\f277"; }

.fa-markdown:before {
  content: "\f60f"; }

.fa-marker:before {
  content: "\f5a1"; }

.fa-mars:before {
  content: "\f222"; }

.fa-mars-double:before {
  content: "\f227"; }

.fa-mars-stroke:before {
  content: "\f229"; }

.fa-mars-stroke-h:before {
  content: "\f22b"; }

.fa-mars-stroke-v:before {
  content: "\f22a"; }

.fa-mask:before {
  content: "\f6fa"; }

.fa-mastodon:before {
  content: "\f4f6"; }

.fa-maxcdn:before {
  content: "\f136"; }

.fa-mdb:before {
  content: "\f8ca"; }

.fa-medal:before {
  content: "\f5a2"; }

.fa-medapps:before {
  content: "\f3c6"; }

.fa-medium:before {
  content: "\f23a"; }

.fa-medium-m:before {
  content: "\f3c7"; }

.fa-medkit:before {
  content: "\f0fa"; }

.fa-medrt:before {
  content: "\f3c8"; }

.fa-meetup:before {
  content: "\f2e0"; }

.fa-megaport:before {
  content: "\f5a3"; }

.fa-meh:before {
  content: "\f11a"; }

.fa-meh-blank:before {
  content: "\f5a4"; }

.fa-meh-rolling-eyes:before {
  content: "\f5a5"; }

.fa-memory:before {
  content: "\f538"; }

.fa-mendeley:before {
  content: "\f7b3"; }

.fa-menorah:before {
  content: "\f676"; }

.fa-mercury:before {
  content: "\f223"; }

.fa-meteor:before {
  content: "\f753"; }

.fa-microblog:before {
  content: "\e01a"; }

.fa-microchip:before {
  content: "\f2db"; }

.fa-microphone:before {
  content: "\f130"; }

.fa-microphone-alt:before {
  content: "\f3c9"; }

.fa-microphone-alt-slash:before {
  content: "\f539"; }

.fa-microphone-slash:before {
  content: "\f131"; }

.fa-microscope:before {
  content: "\f610"; }

.fa-microsoft:before {
  content: "\f3ca"; }

.fa-minus:before {
  content: "\f068"; }

.fa-minus-circle:before {
  content: "\f056"; }

.fa-minus-square:before {
  content: "\f146"; }

.fa-mitten:before {
  content: "\f7b5"; }

.fa-mix:before {
  content: "\f3cb"; }

.fa-mixcloud:before {
  content: "\f289"; }

.fa-mixer:before {
  content: "\e056"; }

.fa-mizuni:before {
  content: "\f3cc"; }

.fa-mobile:before {
  content: "\f10b"; }

.fa-mobile-alt:before {
  content: "\f3cd"; }

.fa-modx:before {
  content: "\f285"; }

.fa-monero:before {
  content: "\f3d0"; }

.fa-money-bill:before {
  content: "\f0d6"; }

.fa-money-bill-alt:before {
  content: "\f3d1"; }

.fa-money-bill-wave:before {
  content: "\f53a"; }

.fa-money-bill-wave-alt:before {
  content: "\f53b"; }

.fa-money-check:before {
  content: "\f53c"; }

.fa-money-check-alt:before {
  content: "\f53d"; }

.fa-monument:before {
  content: "\f5a6"; }

.fa-moon:before {
  content: "\f186"; }

.fa-mortar-pestle:before {
  content: "\f5a7"; }

.fa-mosque:before {
  content: "\f678"; }

.fa-motorcycle:before {
  content: "\f21c"; }

.fa-mountain:before {
  content: "\f6fc"; }

.fa-mouse:before {
  content: "\f8cc"; }

.fa-mouse-pointer:before {
  content: "\f245"; }

.fa-mug-hot:before {
  content: "\f7b6"; }

.fa-music:before {
  content: "\f001"; }

.fa-napster:before {
  content: "\f3d2"; }

.fa-neos:before {
  content: "\f612"; }

.fa-network-wired:before {
  content: "\f6ff"; }

.fa-neuter:before {
  content: "\f22c"; }

.fa-newspaper:before {
  content: "\f1ea"; }

.fa-nimblr:before {
  content: "\f5a8"; }

.fa-node:before {
  content: "\f419"; }

.fa-node-js:before {
  content: "\f3d3"; }

.fa-not-equal:before {
  content: "\f53e"; }

.fa-notes-medical:before {
  content: "\f481"; }

.fa-npm:before {
  content: "\f3d4"; }

.fa-ns8:before {
  content: "\f3d5"; }

.fa-nutritionix:before {
  content: "\f3d6"; }

.fa-object-group:before {
  content: "\f247"; }

.fa-object-ungroup:before {
  content: "\f248"; }

.fa-odnoklassniki:before {
  content: "\f263"; }

.fa-odnoklassniki-square:before {
  content: "\f264"; }

.fa-oil-can:before {
  content: "\f613"; }

.fa-old-republic:before {
  content: "\f510"; }

.fa-om:before {
  content: "\f679"; }

.fa-opencart:before {
  content: "\f23d"; }

.fa-openid:before {
  content: "\f19b"; }

.fa-opera:before {
  content: "\f26a"; }

.fa-optin-monster:before {
  content: "\f23c"; }

.fa-orcid:before {
  content: "\f8d2"; }

.fa-osi:before {
  content: "\f41a"; }

.fa-otter:before {
  content: "\f700"; }

.fa-outdent:before {
  content: "\f03b"; }

.fa-page4:before {
  content: "\f3d7"; }

.fa-pagelines:before {
  content: "\f18c"; }

.fa-pager:before {
  content: "\f815"; }

.fa-paint-brush:before {
  content: "\f1fc"; }

.fa-paint-roller:before {
  content: "\f5aa"; }

.fa-palette:before {
  content: "\f53f"; }

.fa-palfed:before {
  content: "\f3d8"; }

.fa-pallet:before {
  content: "\f482"; }

.fa-paper-plane:before {
  content: "\f1d8"; }

.fa-paperclip:before {
  content: "\f0c6"; }

.fa-parachute-box:before {
  content: "\f4cd"; }

.fa-paragraph:before {
  content: "\f1dd"; }

.fa-parking:before {
  content: "\f540"; }

.fa-passport:before {
  content: "\f5ab"; }

.fa-pastafarianism:before {
  content: "\f67b"; }

.fa-paste:before {
  content: "\f0ea"; }

.fa-patreon:before {
  content: "\f3d9"; }

.fa-pause:before {
  content: "\f04c"; }

.fa-pause-circle:before {
  content: "\f28b"; }

.fa-paw:before {
  content: "\f1b0"; }

.fa-paypal:before {
  content: "\f1ed"; }

.fa-peace:before {
  content: "\f67c"; }

.fa-pen:before {
  content: "\f304"; }

.fa-pen-alt:before {
  content: "\f305"; }

.fa-pen-fancy:before {
  content: "\f5ac"; }

.fa-pen-nib:before {
  content: "\f5ad"; }

.fa-pen-square:before {
  content: "\f14b"; }

.fa-pencil-alt:before {
  content: "\f303"; }

.fa-pencil-ruler:before {
  content: "\f5ae"; }

.fa-penny-arcade:before {
  content: "\f704"; }

.fa-people-arrows:before {
  content: "\e068"; }

.fa-people-carry:before {
  content: "\f4ce"; }

.fa-pepper-hot:before {
  content: "\f816"; }

.fa-percent:before {
  content: "\f295"; }

.fa-percentage:before {
  content: "\f541"; }

.fa-periscope:before {
  content: "\f3da"; }

.fa-person-booth:before {
  content: "\f756"; }

.fa-phabricator:before {
  content: "\f3db"; }

.fa-phoenix-framework:before {
  content: "\f3dc"; }

.fa-phoenix-squadron:before {
  content: "\f511"; }

.fa-phone:before {
  content: "\f095"; }

.fa-phone-alt:before {
  content: "\f879"; }

.fa-phone-slash:before {
  content: "\f3dd"; }

.fa-phone-square:before {
  content: "\f098"; }

.fa-phone-square-alt:before {
  content: "\f87b"; }

.fa-phone-volume:before {
  content: "\f2a0"; }

.fa-photo-video:before {
  content: "\f87c"; }

.fa-php:before {
  content: "\f457"; }

.fa-pied-piper:before {
  content: "\f2ae"; }

.fa-pied-piper-alt:before {
  content: "\f1a8"; }

.fa-pied-piper-hat:before {
  content: "\f4e5"; }

.fa-pied-piper-pp:before {
  content: "\f1a7"; }

.fa-pied-piper-square:before {
  content: "\e01e"; }

.fa-piggy-bank:before {
  content: "\f4d3"; }

.fa-pills:before {
  content: "\f484"; }

.fa-pinterest:before {
  content: "\f0d2"; }

.fa-pinterest-p:before {
  content: "\f231"; }

.fa-pinterest-square:before {
  content: "\f0d3"; }

.fa-pizza-slice:before {
  content: "\f818"; }

.fa-place-of-worship:before {
  content: "\f67f"; }

.fa-plane:before {
  content: "\f072"; }

.fa-plane-arrival:before {
  content: "\f5af"; }

.fa-plane-departure:before {
  content: "\f5b0"; }

.fa-plane-slash:before {
  content: "\e069"; }

.fa-play:before {
  content: "\f04b"; }

.fa-play-circle:before {
  content: "\f144"; }

.fa-playstation:before {
  content: "\f3df"; }

.fa-plug:before {
  content: "\f1e6"; }

.fa-plus:before {
  content: "\f067"; }

.fa-plus-circle:before {
  content: "\f055"; }

.fa-plus-square:before {
  content: "\f0fe"; }

.fa-podcast:before {
  content: "\f2ce"; }

.fa-poll:before {
  content: "\f681"; }

.fa-poll-h:before {
  content: "\f682"; }

.fa-poo:before {
  content: "\f2fe"; }

.fa-poo-storm:before {
  content: "\f75a"; }

.fa-poop:before {
  content: "\f619"; }

.fa-portrait:before {
  content: "\f3e0"; }

.fa-pound-sign:before {
  content: "\f154"; }

.fa-power-off:before {
  content: "\f011"; }

.fa-pray:before {
  content: "\f683"; }

.fa-praying-hands:before {
  content: "\f684"; }

.fa-prescription:before {
  content: "\f5b1"; }

.fa-prescription-bottle:before {
  content: "\f485"; }

.fa-prescription-bottle-alt:before {
  content: "\f486"; }

.fa-print:before {
  content: "\f02f"; }

.fa-procedures:before {
  content: "\f487"; }

.fa-product-hunt:before {
  content: "\f288"; }

.fa-project-diagram:before {
  content: "\f542"; }

.fa-pump-medical:before {
  content: "\e06a"; }

.fa-pump-soap:before {
  content: "\e06b"; }

.fa-pushed:before {
  content: "\f3e1"; }

.fa-puzzle-piece:before {
  content: "\f12e"; }

.fa-python:before {
  content: "\f3e2"; }

.fa-qq:before {
  content: "\f1d6"; }

.fa-qrcode:before {
  content: "\f029"; }

.fa-question:before {
  content: "\f128"; }

.fa-question-circle:before {
  content: "\f059"; }

.fa-quidditch:before {
  content: "\f458"; }

.fa-quinscape:before {
  content: "\f459"; }

.fa-quora:before {
  content: "\f2c4"; }

.fa-quote-left:before {
  content: "\f10d"; }

.fa-quote-right:before {
  content: "\f10e"; }

.fa-quran:before {
  content: "\f687"; }

.fa-r-project:before {
  content: "\f4f7"; }

.fa-radiation:before {
  content: "\f7b9"; }

.fa-radiation-alt:before {
  content: "\f7ba"; }

.fa-rainbow:before {
  content: "\f75b"; }

.fa-random:before {
  content: "\f074"; }

.fa-raspberry-pi:before {
  content: "\f7bb"; }

.fa-ravelry:before {
  content: "\f2d9"; }

.fa-react:before {
  content: "\f41b"; }

.fa-reacteurope:before {
  content: "\f75d"; }

.fa-readme:before {
  content: "\f4d5"; }

.fa-rebel:before {
  content: "\f1d0"; }

.fa-receipt:before {
  content: "\f543"; }

.fa-record-vinyl:before {
  content: "\f8d9"; }

.fa-recycle:before {
  content: "\f1b8"; }

.fa-red-river:before {
  content: "\f3e3"; }

.fa-reddit:before {
  content: "\f1a1"; }

.fa-reddit-alien:before {
  content: "\f281"; }

.fa-reddit-square:before {
  content: "\f1a2"; }

.fa-redhat:before {
  content: "\f7bc"; }

.fa-redo:before {
  content: "\f01e"; }

.fa-redo-alt:before {
  content: "\f2f9"; }

.fa-registered:before {
  content: "\f25d"; }

.fa-remove-format:before {
  content: "\f87d"; }

.fa-renren:before {
  content: "\f18b"; }

.fa-reply:before {
  content: "\f3e5"; }

.fa-reply-all:before {
  content: "\f122"; }

.fa-replyd:before {
  content: "\f3e6"; }

.fa-republican:before {
  content: "\f75e"; }

.fa-researchgate:before {
  content: "\f4f8"; }

.fa-resolving:before {
  content: "\f3e7"; }

.fa-restroom:before {
  content: "\f7bd"; }

.fa-retweet:before {
  content: "\f079"; }

.fa-rev:before {
  content: "\f5b2"; }

.fa-ribbon:before {
  content: "\f4d6"; }

.fa-ring:before {
  content: "\f70b"; }

.fa-road:before {
  content: "\f018"; }

.fa-robot:before {
  content: "\f544"; }

.fa-rocket:before {
  content: "\f135"; }

.fa-rocketchat:before {
  content: "\f3e8"; }

.fa-rockrms:before {
  content: "\f3e9"; }

.fa-route:before {
  content: "\f4d7"; }

.fa-rss:before {
  content: "\f09e"; }

.fa-rss-square:before {
  content: "\f143"; }

.fa-ruble-sign:before {
  content: "\f158"; }

.fa-ruler:before {
  content: "\f545"; }

.fa-ruler-combined:before {
  content: "\f546"; }

.fa-ruler-horizontal:before {
  content: "\f547"; }

.fa-ruler-vertical:before {
  content: "\f548"; }

.fa-running:before {
  content: "\f70c"; }

.fa-rupee-sign:before {
  content: "\f156"; }

.fa-rust:before {
  content: "\e07a"; }

.fa-sad-cry:before {
  content: "\f5b3"; }

.fa-sad-tear:before {
  content: "\f5b4"; }

.fa-safari:before {
  content: "\f267"; }

.fa-salesforce:before {
  content: "\f83b"; }

.fa-sass:before {
  content: "\f41e"; }

.fa-satellite:before {
  content: "\f7bf"; }

.fa-satellite-dish:before {
  content: "\f7c0"; }

.fa-save:before {
  content: "\f0c7"; }

.fa-schlix:before {
  content: "\f3ea"; }

.fa-school:before {
  content: "\f549"; }

.fa-screwdriver:before {
  content: "\f54a"; }

.fa-scribd:before {
  content: "\f28a"; }

.fa-scroll:before {
  content: "\f70e"; }

.fa-sd-card:before {
  content: "\f7c2"; }

.fa-search:before {
  content: "\f002"; }

.fa-search-dollar:before {
  content: "\f688"; }

.fa-search-location:before {
  content: "\f689"; }

.fa-search-minus:before {
  content: "\f010"; }

.fa-search-plus:before {
  content: "\f00e"; }

.fa-searchengin:before {
  content: "\f3eb"; }

.fa-seedling:before {
  content: "\f4d8"; }

.fa-sellcast:before {
  content: "\f2da"; }

.fa-sellsy:before {
  content: "\f213"; }

.fa-server:before {
  content: "\f233"; }

.fa-servicestack:before {
  content: "\f3ec"; }

.fa-shapes:before {
  content: "\f61f"; }

.fa-share:before {
  content: "\f064"; }

.fa-share-alt:before {
  content: "\f1e0"; }

.fa-share-alt-square:before {
  content: "\f1e1"; }

.fa-share-square:before {
  content: "\f14d"; }

.fa-shekel-sign:before {
  content: "\f20b"; }

.fa-shield-alt:before {
  content: "\f3ed"; }

.fa-shield-virus:before {
  content: "\e06c"; }

.fa-ship:before {
  content: "\f21a"; }

.fa-shipping-fast:before {
  content: "\f48b"; }

.fa-shirtsinbulk:before {
  content: "\f214"; }

.fa-shoe-prints:before {
  content: "\f54b"; }

.fa-shopify:before {
  content: "\e057"; }

.fa-shopping-bag:before {
  content: "\f290"; }

.fa-shopping-basket:before {
  content: "\f291"; }

.fa-shopping-cart:before {
  content: "\f07a"; }

.fa-shopware:before {
  content: "\f5b5"; }

.fa-shower:before {
  content: "\f2cc"; }

.fa-shuttle-van:before {
  content: "\f5b6"; }

.fa-sign:before {
  content: "\f4d9"; }

.fa-sign-in-alt:before {
  content: "\f2f6"; }

.fa-sign-language:before {
  content: "\f2a7"; }

.fa-sign-out-alt:before {
  content: "\f2f5"; }

.fa-signal:before {
  content: "\f012"; }

.fa-signature:before {
  content: "\f5b7"; }

.fa-sim-card:before {
  content: "\f7c4"; }

.fa-simplybuilt:before {
  content: "\f215"; }

.fa-sink:before {
  content: "\e06d"; }

.fa-sistrix:before {
  content: "\f3ee"; }

.fa-sitemap:before {
  content: "\f0e8"; }

.fa-sith:before {
  content: "\f512"; }

.fa-skating:before {
  content: "\f7c5"; }

.fa-sketch:before {
  content: "\f7c6"; }

.fa-skiing:before {
  content: "\f7c9"; }

.fa-skiing-nordic:before {
  content: "\f7ca"; }

.fa-skull:before {
  content: "\f54c"; }

.fa-skull-crossbones:before {
  content: "\f714"; }

.fa-skyatlas:before {
  content: "\f216"; }

.fa-skype:before {
  content: "\f17e"; }

.fa-slack:before {
  content: "\f198"; }

.fa-slack-hash:before {
  content: "\f3ef"; }

.fa-slash:before {
  content: "\f715"; }

.fa-sleigh:before {
  content: "\f7cc"; }

.fa-sliders-h:before {
  content: "\f1de"; }

.fa-slideshare:before {
  content: "\f1e7"; }

.fa-smile:before {
  content: "\f118"; }

.fa-smile-beam:before {
  content: "\f5b8"; }

.fa-smile-wink:before {
  content: "\f4da"; }

.fa-smog:before {
  content: "\f75f"; }

.fa-smoking:before {
  content: "\f48d"; }

.fa-smoking-ban:before {
  content: "\f54d"; }

.fa-sms:before {
  content: "\f7cd"; }

.fa-snapchat:before {
  content: "\f2ab"; }

.fa-snapchat-ghost:before {
  content: "\f2ac"; }

.fa-snapchat-square:before {
  content: "\f2ad"; }

.fa-snowboarding:before {
  content: "\f7ce"; }

.fa-snowflake:before {
  content: "\f2dc"; }

.fa-snowman:before {
  content: "\f7d0"; }

.fa-snowplow:before {
  content: "\f7d2"; }

.fa-soap:before {
  content: "\e06e"; }

.fa-socks:before {
  content: "\f696"; }

.fa-solar-panel:before {
  content: "\f5ba"; }

.fa-sort:before {
  content: "\f0dc"; }

.fa-sort-alpha-down:before {
  content: "\f15d"; }

.fa-sort-alpha-down-alt:before {
  content: "\f881"; }

.fa-sort-alpha-up:before {
  content: "\f15e"; }

.fa-sort-alpha-up-alt:before {
  content: "\f882"; }

.fa-sort-amount-down:before {
  content: "\f160"; }

.fa-sort-amount-down-alt:before {
  content: "\f884"; }

.fa-sort-amount-up:before {
  content: "\f161"; }

.fa-sort-amount-up-alt:before {
  content: "\f885"; }

.fa-sort-down:before {
  content: "\f0dd"; }

.fa-sort-numeric-down:before {
  content: "\f162"; }

.fa-sort-numeric-down-alt:before {
  content: "\f886"; }

.fa-sort-numeric-up:before {
  content: "\f163"; }

.fa-sort-numeric-up-alt:before {
  content: "\f887"; }

.fa-sort-up:before {
  content: "\f0de"; }

.fa-soundcloud:before {
  content: "\f1be"; }

.fa-sourcetree:before {
  content: "\f7d3"; }

.fa-spa:before {
  content: "\f5bb"; }

.fa-space-shuttle:before {
  content: "\f197"; }

.fa-speakap:before {
  content: "\f3f3"; }

.fa-speaker-deck:before {
  content: "\f83c"; }

.fa-spell-check:before {
  content: "\f891"; }

.fa-spider:before {
  content: "\f717"; }

.fa-spinner:before {
  content: "\f110"; }

.fa-splotch:before {
  content: "\f5bc"; }

.fa-spotify:before {
  content: "\f1bc"; }

.fa-spray-can:before {
  content: "\f5bd"; }

.fa-square:before {
  content: "\f0c8"; }

.fa-square-full:before {
  content: "\f45c"; }

.fa-square-root-alt:before {
  content: "\f698"; }

.fa-squarespace:before {
  content: "\f5be"; }

.fa-stack-exchange:before {
  content: "\f18d"; }

.fa-stack-overflow:before {
  content: "\f16c"; }

.fa-stackpath:before {
  content: "\f842"; }

.fa-stamp:before {
  content: "\f5bf"; }

.fa-star:before {
  content: "\f005"; }

.fa-star-and-crescent:before {
  content: "\f699"; }

.fa-star-half:before {
  content: "\f089"; }

.fa-star-half-alt:before {
  content: "\f5c0"; }

.fa-star-of-david:before {
  content: "\f69a"; }

.fa-star-of-life:before {
  content: "\f621"; }

.fa-staylinked:before {
  content: "\f3f5"; }

.fa-steam:before {
  content: "\f1b6"; }

.fa-steam-square:before {
  content: "\f1b7"; }

.fa-steam-symbol:before {
  content: "\f3f6"; }

.fa-step-backward:before {
  content: "\f048"; }

.fa-step-forward:before {
  content: "\f051"; }

.fa-stethoscope:before {
  content: "\f0f1"; }

.fa-sticker-mule:before {
  content: "\f3f7"; }

.fa-sticky-note:before {
  content: "\f249"; }

.fa-stop:before {
  content: "\f04d"; }

.fa-stop-circle:before {
  content: "\f28d"; }

.fa-stopwatch:before {
  content: "\f2f2"; }

.fa-stopwatch-20:before {
  content: "\e06f"; }

.fa-store:before {
  content: "\f54e"; }

.fa-store-alt:before {
  content: "\f54f"; }

.fa-store-alt-slash:before {
  content: "\e070"; }

.fa-store-slash:before {
  content: "\e071"; }

.fa-strava:before {
  content: "\f428"; }

.fa-stream:before {
  content: "\f550"; }

.fa-street-view:before {
  content: "\f21d"; }

.fa-strikethrough:before {
  content: "\f0cc"; }

.fa-stripe:before {
  content: "\f429"; }

.fa-stripe-s:before {
  content: "\f42a"; }

.fa-stroopwafel:before {
  content: "\f551"; }

.fa-studiovinari:before {
  content: "\f3f8"; }

.fa-stumbleupon:before {
  content: "\f1a4"; }

.fa-stumbleupon-circle:before {
  content: "\f1a3"; }

.fa-subscript:before {
  content: "\f12c"; }

.fa-subway:before {
  content: "\f239"; }

.fa-suitcase:before {
  content: "\f0f2"; }

.fa-suitcase-rolling:before {
  content: "\f5c1"; }

.fa-sun:before {
  content: "\f185"; }

.fa-superpowers:before {
  content: "\f2dd"; }

.fa-superscript:before {
  content: "\f12b"; }

.fa-supple:before {
  content: "\f3f9"; }

.fa-surprise:before {
  content: "\f5c2"; }

.fa-suse:before {
  content: "\f7d6"; }

.fa-swatchbook:before {
  content: "\f5c3"; }

.fa-swift:before {
  content: "\f8e1"; }

.fa-swimmer:before {
  content: "\f5c4"; }

.fa-swimming-pool:before {
  content: "\f5c5"; }

.fa-symfony:before {
  content: "\f83d"; }

.fa-synagogue:before {
  content: "\f69b"; }

.fa-sync:before {
  content: "\f021"; }

.fa-sync-alt:before {
  content: "\f2f1"; }

.fa-syringe:before {
  content: "\f48e"; }

.fa-table:before {
  content: "\f0ce"; }

.fa-table-tennis:before {
  content: "\f45d"; }

.fa-tablet:before {
  content: "\f10a"; }

.fa-tablet-alt:before {
  content: "\f3fa"; }

.fa-tablets:before {
  content: "\f490"; }

.fa-tachometer-alt:before {
  content: "\f3fd"; }

.fa-tag:before {
  content: "\f02b"; }

.fa-tags:before {
  content: "\f02c"; }

.fa-tape:before {
  content: "\f4db"; }

.fa-tasks:before {
  content: "\f0ae"; }

.fa-taxi:before {
  content: "\f1ba"; }

.fa-teamspeak:before {
  content: "\f4f9"; }

.fa-teeth:before {
  content: "\f62e"; }

.fa-teeth-open:before {
  content: "\f62f"; }

.fa-telegram:before {
  content: "\f2c6"; }

.fa-telegram-plane:before {
  content: "\f3fe"; }

.fa-temperature-high:before {
  content: "\f769"; }

.fa-temperature-low:before {
  content: "\f76b"; }

.fa-tencent-weibo:before {
  content: "\f1d5"; }

.fa-tenge:before {
  content: "\f7d7"; }

.fa-terminal:before {
  content: "\f120"; }

.fa-text-height:before {
  content: "\f034"; }

.fa-text-width:before {
  content: "\f035"; }

.fa-th:before {
  content: "\f00a"; }

.fa-th-large:before {
  content: "\f009"; }

.fa-th-list:before {
  content: "\f00b"; }

.fa-the-red-yeti:before {
  content: "\f69d"; }

.fa-theater-masks:before {
  content: "\f630"; }

.fa-themeco:before {
  content: "\f5c6"; }

.fa-themeisle:before {
  content: "\f2b2"; }

.fa-thermometer:before {
  content: "\f491"; }

.fa-thermometer-empty:before {
  content: "\f2cb"; }

.fa-thermometer-full:before {
  content: "\f2c7"; }

.fa-thermometer-half:before {
  content: "\f2c9"; }

.fa-thermometer-quarter:before {
  content: "\f2ca"; }

.fa-thermometer-three-quarters:before {
  content: "\f2c8"; }

.fa-think-peaks:before {
  content: "\f731"; }

.fa-thumbs-down:before {
  content: "\f165"; }

.fa-thumbs-up:before {
  content: "\f164"; }

.fa-thumbtack:before {
  content: "\f08d"; }

.fa-ticket-alt:before {
  content: "\f3ff"; }

.fa-tiktok:before {
  content: "\e07b"; }

.fa-times:before {
  content: "\f00d"; }

.fa-times-circle:before {
  content: "\f057"; }

.fa-tint:before {
  content: "\f043"; }

.fa-tint-slash:before {
  content: "\f5c7"; }

.fa-tired:before {
  content: "\f5c8"; }

.fa-toggle-off:before {
  content: "\f204"; }

.fa-toggle-on:before {
  content: "\f205"; }

.fa-toilet:before {
  content: "\f7d8"; }

.fa-toilet-paper:before {
  content: "\f71e"; }

.fa-toilet-paper-slash:before {
  content: "\e072"; }

.fa-toolbox:before {
  content: "\f552"; }

.fa-tools:before {
  content: "\f7d9"; }

.fa-tooth:before {
  content: "\f5c9"; }

.fa-torah:before {
  content: "\f6a0"; }

.fa-torii-gate:before {
  content: "\f6a1"; }

.fa-tractor:before {
  content: "\f722"; }

.fa-trade-federation:before {
  content: "\f513"; }

.fa-trademark:before {
  content: "\f25c"; }

.fa-traffic-light:before {
  content: "\f637"; }

.fa-trailer:before {
  content: "\e041"; }

.fa-train:before {
  content: "\f238"; }

.fa-tram:before {
  content: "\f7da"; }

.fa-transgender:before {
  content: "\f224"; }

.fa-transgender-alt:before {
  content: "\f225"; }

.fa-trash:before {
  content: "\f1f8"; }

.fa-trash-alt:before {
  content: "\f2ed"; }

.fa-trash-restore:before {
  content: "\f829"; }

.fa-trash-restore-alt:before {
  content: "\f82a"; }

.fa-tree:before {
  content: "\f1bb"; }

.fa-trello:before {
  content: "\f181"; }

.fa-tripadvisor:before {
  content: "\f262"; }

.fa-trophy:before {
  content: "\f091"; }

.fa-truck:before {
  content: "\f0d1"; }

.fa-truck-loading:before {
  content: "\f4de"; }

.fa-truck-monster:before {
  content: "\f63b"; }

.fa-truck-moving:before {
  content: "\f4df"; }

.fa-truck-pickup:before {
  content: "\f63c"; }

.fa-tshirt:before {
  content: "\f553"; }

.fa-tty:before {
  content: "\f1e4"; }

.fa-tumblr:before {
  content: "\f173"; }

.fa-tumblr-square:before {
  content: "\f174"; }

.fa-tv:before {
  content: "\f26c"; }

.fa-twitch:before {
  content: "\f1e8"; }

.fa-twitter:before {
  content: "\f099"; }

.fa-twitter-square:before {
  content: "\f081"; }

.fa-typo3:before {
  content: "\f42b"; }

.fa-uber:before {
  content: "\f402"; }

.fa-ubuntu:before {
  content: "\f7df"; }

.fa-uikit:before {
  content: "\f403"; }

.fa-umbraco:before {
  content: "\f8e8"; }

.fa-umbrella:before {
  content: "\f0e9"; }

.fa-umbrella-beach:before {
  content: "\f5ca"; }

.fa-underline:before {
  content: "\f0cd"; }

.fa-undo:before {
  content: "\f0e2"; }

.fa-undo-alt:before {
  content: "\f2ea"; }

.fa-uniregistry:before {
  content: "\f404"; }

.fa-unity:before {
  content: "\e049"; }

.fa-universal-access:before {
  content: "\f29a"; }

.fa-university:before {
  content: "\f19c"; }

.fa-unlink:before {
  content: "\f127"; }

.fa-unlock:before {
  content: "\f09c"; }

.fa-unlock-alt:before {
  content: "\f13e"; }

.fa-unsplash:before {
  content: "\e07c"; }

.fa-untappd:before {
  content: "\f405"; }

.fa-upload:before {
  content: "\f093"; }

.fa-ups:before {
  content: "\f7e0"; }

.fa-usb:before {
  content: "\f287"; }

.fa-user:before {
  content: "\f007"; }

.fa-user-alt:before {
  content: "\f406"; }

.fa-user-alt-slash:before {
  content: "\f4fa"; }

.fa-user-astronaut:before {
  content: "\f4fb"; }

.fa-user-check:before {
  content: "\f4fc"; }

.fa-user-circle:before {
  content: "\f2bd"; }

.fa-user-clock:before {
  content: "\f4fd"; }

.fa-user-cog:before {
  content: "\f4fe"; }

.fa-user-edit:before {
  content: "\f4ff"; }

.fa-user-friends:before {
  content: "\f500"; }

.fa-user-graduate:before {
  content: "\f501"; }

.fa-user-injured:before {
  content: "\f728"; }

.fa-user-lock:before {
  content: "\f502"; }

.fa-user-md:before {
  content: "\f0f0"; }

.fa-user-minus:before {
  content: "\f503"; }

.fa-user-ninja:before {
  content: "\f504"; }

.fa-user-nurse:before {
  content: "\f82f"; }

.fa-user-plus:before {
  content: "\f234"; }

.fa-user-secret:before {
  content: "\f21b"; }

.fa-user-shield:before {
  content: "\f505"; }

.fa-user-slash:before {
  content: "\f506"; }

.fa-user-tag:before {
  content: "\f507"; }

.fa-user-tie:before {
  content: "\f508"; }

.fa-user-times:before {
  content: "\f235"; }

.fa-users:before {
  content: "\f0c0"; }

.fa-users-cog:before {
  content: "\f509"; }

.fa-users-slash:before {
  content: "\e073"; }

.fa-usps:before {
  content: "\f7e1"; }

.fa-ussunnah:before {
  content: "\f407"; }

.fa-utensil-spoon:before {
  content: "\f2e5"; }

.fa-utensils:before {
  content: "\f2e7"; }

.fa-vaadin:before {
  content: "\f408"; }

.fa-vector-square:before {
  content: "\f5cb"; }

.fa-venus:before {
  content: "\f221"; }

.fa-venus-double:before {
  content: "\f226"; }

.fa-venus-mars:before {
  content: "\f228"; }

.fa-viacoin:before {
  content: "\f237"; }

.fa-viadeo:before {
  content: "\f2a9"; }

.fa-viadeo-square:before {
  content: "\f2aa"; }

.fa-vial:before {
  content: "\f492"; }

.fa-vials:before {
  content: "\f493"; }

.fa-viber:before {
  content: "\f409"; }

.fa-video:before {
  content: "\f03d"; }

.fa-video-slash:before {
  content: "\f4e2"; }

.fa-vihara:before {
  content: "\f6a7"; }

.fa-vimeo:before {
  content: "\f40a"; }

.fa-vimeo-square:before {
  content: "\f194"; }

.fa-vimeo-v:before {
  content: "\f27d"; }

.fa-vine:before {
  content: "\f1ca"; }

.fa-virus:before {
  content: "\e074"; }

.fa-virus-slash:before {
  content: "\e075"; }

.fa-viruses:before {
  content: "\e076"; }

.fa-vk:before {
  content: "\f189"; }

.fa-vnv:before {
  content: "\f40b"; }

.fa-voicemail:before {
  content: "\f897"; }

.fa-volleyball-ball:before {
  content: "\f45f"; }

.fa-volume-down:before {
  content: "\f027"; }

.fa-volume-mute:before {
  content: "\f6a9"; }

.fa-volume-off:before {
  content: "\f026"; }

.fa-volume-up:before {
  content: "\f028"; }

.fa-vote-yea:before {
  content: "\f772"; }

.fa-vr-cardboard:before {
  content: "\f729"; }

.fa-vuejs:before {
  content: "\f41f"; }

.fa-walking:before {
  content: "\f554"; }

.fa-wallet:before {
  content: "\f555"; }

.fa-warehouse:before {
  content: "\f494"; }

.fa-water:before {
  content: "\f773"; }

.fa-wave-square:before {
  content: "\f83e"; }

.fa-waze:before {
  content: "\f83f"; }

.fa-weebly:before {
  content: "\f5cc"; }

.fa-weibo:before {
  content: "\f18a"; }

.fa-weight:before {
  content: "\f496"; }

.fa-weight-hanging:before {
  content: "\f5cd"; }

.fa-weixin:before {
  content: "\f1d7"; }

.fa-whatsapp:before {
  content: "\f232"; }

.fa-whatsapp-square:before {
  content: "\f40c"; }

.fa-wheelchair:before {
  content: "\f193"; }

.fa-whmcs:before {
  content: "\f40d"; }

.fa-wifi:before {
  content: "\f1eb"; }

.fa-wikipedia-w:before {
  content: "\f266"; }

.fa-wind:before {
  content: "\f72e"; }

.fa-window-close:before {
  content: "\f410"; }

.fa-window-maximize:before {
  content: "\f2d0"; }

.fa-window-minimize:before {
  content: "\f2d1"; }

.fa-window-restore:before {
  content: "\f2d2"; }

.fa-windows:before {
  content: "\f17a"; }

.fa-wine-bottle:before {
  content: "\f72f"; }

.fa-wine-glass:before {
  content: "\f4e3"; }

.fa-wine-glass-alt:before {
  content: "\f5ce"; }

.fa-wix:before {
  content: "\f5cf"; }

.fa-wizards-of-the-coast:before {
  content: "\f730"; }

.fa-wolf-pack-battalion:before {
  content: "\f514"; }

.fa-won-sign:before {
  content: "\f159"; }

.fa-wordpress:before {
  content: "\f19a"; }

.fa-wordpress-simple:before {
  content: "\f411"; }

.fa-wpbeginner:before {
  content: "\f297"; }

.fa-wpexplorer:before {
  content: "\f2de"; }

.fa-wpforms:before {
  content: "\f298"; }

.fa-wpressr:before {
  content: "\f3e4"; }

.fa-wrench:before {
  content: "\f0ad"; }

.fa-x-ray:before {
  content: "\f497"; }

.fa-xbox:before {
  content: "\f412"; }

.fa-xing:before {
  content: "\f168"; }

.fa-xing-square:before {
  content: "\f169"; }

.fa-y-combinator:before {
  content: "\f23b"; }

.fa-yahoo:before {
  content: "\f19e"; }

.fa-yammer:before {
  content: "\f840"; }

.fa-yandex:before {
  content: "\f413"; }

.fa-yandex-international:before {
  content: "\f414"; }

.fa-yarn:before {
  content: "\f7e3"; }

.fa-yelp:before {
  content: "\f1e9"; }

.fa-yen-sign:before {
  content: "\f157"; }

.fa-yin-yang:before {
  content: "\f6ad"; }

.fa-yoast:before {
  content: "\f2b1"; }

.fa-youtube:before {
  content: "\f167"; }

.fa-youtube-square:before {
  content: "\f431"; }

.fa-zhihu:before {
  content: "\f63f"; }

.sr-only {
  border: 0;
  clip: rect(0, 0, 0, 0);
  height: 1px;
  margin: -1px;
  overflow: hidden;
  padding: 0;
  position: absolute;
  width: 1px; }

.sr-only-focusable:active, .sr-only-focusable:focus {
  clip: auto;
  height: auto;
  margin: 0;
  overflow: visible;
  position: static;
  width: auto; }
@font-face {
  font-family: 'Font Awesome 5 Brands';
  font-style: normal;
  font-weight: 400;
  font-display: block;
  src: url("../webfonts/fa-brands-400.eot");
  src: url("../webfonts/fa-brands-400.eot?#iefix") format("embedded-opentype"), url("../webfonts/fa-brands-400.woff2") format("woff2"), url("../webfonts/fa-brands-400.woff") format("woff"), url("../webfonts/fa-brands-400.ttf") format("truetype"), url("../webfonts/fa-brands-400.svg#fontawesome") format("svg"); }

.fab {
  font-family: 'Font Awesome 5 Brands';
  font-weight: 400; }
@font-face {
  font-family: 'Font Awesome 5 Free';
  font-style: normal;
  font-weight: 400;
  font-display: block;
  src: url("../webfonts/fa-regular-400.eot");
  src: url("../webfonts/fa-regular-400.eot?#iefix") format("embedded-opentype"), url("../webfonts/fa-regular-400.woff2") format("woff2"), url("../webfonts/fa-regular-400.woff") format("woff"), url("../webfonts/fa-regular-400.ttf") format("truetype"), url("../webfonts/fa-regular-400.svg#fontawesome") format("svg"); }

.far {
  font-family: 'Font Awesome 5 Free';
  font-weight: 400; }
@font-face {
  font-family: 'Font Awesome 5 Free';
  font-style: normal;
  font-weight: 900;
  font-display: block;
  src: url("../webfonts/fa-solid-900.eot");
  src: url("../webfonts/fa-solid-900.eot?#iefix") format("embedded-opentype"), url("../webfonts/fa-solid-900.woff2") format("woff2"), url("../webfonts/fa-solid-900.woff") format("woff"), url("../webfonts/fa-solid-900.ttf") format("truetype"), url("../webfonts/fa-solid-900.svg#fontawesome") format("svg"); }

.fa,
.fas {
  font-family: 'Font Awesome 5 Free';
  font-weight: 900; }


File: /public\index.php
<?php
require_once '../app/bootstrap.php';

/* Prácticamente hacemos una instancia de la clase Core */
$init = new Core;


File: /public\js\grupoLimiteAnchoBanda\index.js
const token = document.getElementById("tokenCSRF").value; //obtengo el token, que está en campo oculto del modal hotspotUserProfile

// para validar campos acepten solo numeros enteros
$(function(){
    $(".validarEntero").keydown(function(event){
        //alert(event.keyCode);
        if((event.keyCode < 48 || event.keyCode > 57) && (event.keyCode < 96 || event.keyCode > 105) && event.keyCode !==190  && event.keyCode !==110 && event.keyCode !==8 && event.keyCode !==9  ){
            return false;
        }
    });
});

let tablaUsers = $('#tablaUsersProfile').DataTable({
    responsive: true,
    //bDestroy: true,
    language: {
    "decimal": "",
    "emptyTable": "No hay información",
    "info": "Mostrando _START_ a _END_ de _TOTAL_ Entradas",
    "infoEmpty": "Mostrando 0 to 0 of 0 Entradas",
    "infoFiltered": "(Filtrado de _MAX_ total entradas)",
    "infoPostFix": "",
    "thousands": ",",
    "lengthMenu": "Mostrar _MENU_ Entradas",
    "loadingRecords": "Cargando...",
    "processing": "Procesando...",
    "search": "Buscar:",
    "zeroRecords": "Sin resultados encontrados"
    },
});

function showHotspotsUserProfile(id) {

    $.ajax({
        url: "grupolimiteanchobanda/getInfoHotspotUserProfile", 
        type: "POST",
        dataType:"json",
        data: {
            idProfile:id,
            tokenCsrf: token
        },
        success: function(respuesta) { //respuesta es un json
            ok = respuesta.ok;
            if(ok){
                userProfile = respuesta.userProfile[0]; //regresa un array, se ocupa el de la posición 1
                //si esos valores no existen, se mandan vacíos
                idUser = userProfile['.id'];
                name = userProfile.name || '';
                sharedUSers = userProfile['shared-users'] || '';
                velocidad = userProfile['rate-limit'] || '';
                //los separo por slash "2048k/2048k" --> regresa un array de 2048k , 2048k
                velocidad = velocidad.split("/"); 
                comment = userProfile.comment || '';
                //se pinta en los campos los valores obtenidos
                document.getElementById("idHotspotUserProfile").value = idUser;
                document.getElementById("name").value = name;
                document.getElementById("sharedUsers").value = sharedUSers;
                 //tomo el primer valor del array {2048k , 2048k} y tomo solo el valor numerico
                document.getElementById("limite").value = velocidad[0].replace(/[^\d]/, '');
                 //tomo el primer valor del array {2048k , 2048k} y tomo solo el string, k o m
                document.getElementById("tipoUnidad").value = velocidad[0].replace(/[0-9]/g, '');//
                $('#hotspotUserProfile').modal('show');//muestro el modal con los datos cargados
                activeButton(); //se llama la funcion para activar/desactivar el botón de actualizar del modal
            }            
        },
        error: function(respuesta) {
            console.log('error')
        }
    })
}

function activeButton() {
    
    name = document.getElementById("name").value ;
    sharedUsers = document.getElementById("sharedUsers").value;
    tipoUnidad = $("#tipoUnidad :selected").val();
    limite = document.getElementById("limite").value;
    
    let disabled = (name == '' || sharedUsers == '' || tipoUnidad == ''  || limite == '' ) ? true : false ;   

    $('#btnSavehotspotUserProfile').prop("disabled", disabled);
}

function updateHotspotUserProfile() {

    id = document.getElementById("idHotspotUserProfile").value ;
    name = document.getElementById("name").value ;
    sharedUsers = document.getElementById("sharedUsers").value;
    limite = document.getElementById("limite").value;
    tipoUnidad = $("#tipoUnidad :selected").val();
    //creo el objeto user con los datos recogidos
    user = { id, name, sharedUsers, limite, tipoUnidad };

    $.ajax({
        url: "grupolimiteanchobanda/updateHotspotUserProfile", 
        type: "POST",
        dataType:"json",
        data: {
            user,
            tokenCsrf: token
        },
        success: function(respuesta) { //respuesta es un json
            ok = respuesta.ok;
            if(ok){
                mensaje= respuesta.mensaje;
                showMessageNotify(mensaje, 'info', 2500); //muestro alerta
                $('#hotspotUserProfile').modal('hide');
                setTimeout(() => {
                    location.reload();
                }, 3000);
            }
                           
        },
        error: function(respuesta) {
            console.log('error')
        }
    })

}

function deleteHotspotsUserProfile(id, name) {
    Swal.fire({
        title: `¿Estás seguro de eliminar a ${name}?`,
        text: "¡No podrás revertir esto!",
        type: 'warning',
        showCancelButton: true,
        confirmButtonColor: '#3085d6',
        cancelButtonColor: '#d33',
        cancelButtonText: '¡Cancelar!',
        confirmButtonText: 'Sí, borrarlo!'
        }).then((result) => {
        if (result.value) {
            $.ajax({
                url: "grupolimiteanchobanda/deleteHotspotsUserProfile", 
                type: "POST",
                dataType:"json",
                data: {
                    id,
                    tokenCsrf: token
                },
                success: function(respuesta) { //respuesta es un json
                    ok = respuesta.ok;
                    if(ok){
                        mensaje = respuesta.mensaje+': '+name;
                        showMessageNotify(mensaje, 'success', 2000); //muestro alerta
                        setTimeout(() => {
                            location.reload();
                        }, 2500);
                    }              
                },
                error: function(respuesta) {
                    console.log('error')
                }
            })
        }
    })
}

// funcion exclusiva para mostrar mensajes como notificaciones
function showMessageNotify(mensaje, tipo, duracion) {
    $.notify({							
      message: `<i class="fa fa-sun"></i><strong> ${mensaje}</strong>`
      },{								
          type: tipo,
          delay: duracion,
          z_index: 3000,
    });
} 

File: /public\js\material-dashboard.minf066.js
/*!

 * Material Dashboard PRO - v2.1.0

 * Product Page: https://www.creative-tim.com/product/material-dashboard-pro
 * Copyright 2019 Creative Tim (https://www.creative-tim.com)

 * Coded by Creative Tim


 * The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

 */
isWindows=-1<navigator.platform.indexOf("Win"),isWindows?($(".sidebar .sidebar-wrapper, .main-panel").perfectScrollbar(),$("html").addClass("perfect-scrollbar-on")):$("html").addClass("perfect-scrollbar-off");var breakCards=!0,searchVisible=0,transparent=!0,transparentDemo=!0,fixedTop=!1,mobile_menu_visible=0,mobile_menu_initialized=!1,toggle_initialized=!1,bootstrap_nav_initialized=!1,seq=0,delays=80,durations=500,seq2=0,delays2=80,durations2=500;function debounce(t,n,i){var r;return function(){var e=this,a=arguments;clearTimeout(r),r=setTimeout(function(){r=null,i||t.apply(e,a)},n),i&&!r&&t.apply(e,a)}}$(document).ready(function(){$sidebar=$(".sidebar"),window_width=$(window).width(),$("body").bootstrapMaterialDesign({autofill:!1}),md.initSidebarsCheck(),window_width=$(window).width(),md.checkSidebarImage(),md.initMinimizeSidebar(),$(".dropdown-menu a.dropdown-toggle").on("click",function(e){var a=$(this),t=$(this).offsetParent(".dropdown-menu");return $(this).next().hasClass("show")||$(this).parents(".dropdown-menu").first().find(".show").removeClass("show"),$(this).next(".dropdown-menu").toggleClass("show"),$(this).closest("a").toggleClass("open"),$(this).parents("a.dropdown-item.dropdown.show").on("hidden.bs.dropdown",function(e){$(".dropdown-menu .show").removeClass("show")}),t.parent().hasClass("navbar-nav")||a.next().css({top:a[0].offsetTop,left:t.outerWidth()-4}),!1}),0!=$(".selectpicker").length&&$(".selectpicker").selectpicker(),$('[rel="tooltip"]').tooltip(),$('[data-toggle="popover"]').popover();var e=$(".tagsinput").data("color");0!=$(".tagsinput").length&&$(".tagsinput").tagsinput(),$(".bootstrap-tagsinput").addClass(e+"-badge"),$(".select").dropdown({dropdownClass:"dropdown-menu",optionClass:""}),$(".form-control").on("focus",function(){$(this).parent(".input-group").addClass("input-group-focus")}).on("blur",function(){$(this).parent(".input-group").removeClass("input-group-focus")}),1==breakCards&&$('[data-header-animation="true"]').each(function(){$(this);var a=$(this).parent(".card");a.find(".fix-broken-card").click(function(){console.log(this);var e=$(this).parent().parent().siblings(".card-header, .card-header-image");e.removeClass("hinge").addClass("fadeInDown"),a.attr("data-count",0),setTimeout(function(){e.removeClass("fadeInDown animate")},480)}),a.mouseenter(function(){var e=$(this);hover_count=parseInt(e.attr("data-count"),10)+1||0,e.attr("data-count",hover_count),20<=hover_count&&$(this).children(".card-header, .card-header-image").addClass("hinge animated")})}),$('input[type="checkbox"][required="true"], input[type="radio"][required="true"]').on("click",function(){$(this).hasClass("error")&&$(this).closest("div").removeClass("has-error")})}),$(document).on("click",".navbar-toggler",function(){if($toggle=$(this),1==mobile_menu_visible)$("html").removeClass("nav-open"),$(".close-layer").remove(),setTimeout(function(){$toggle.removeClass("toggled")},400),mobile_menu_visible=0;else{setTimeout(function(){$toggle.addClass("toggled")},430);var e=$('<div class="close-layer"></div>');0!=$("body").find(".main-panel").length?e.appendTo(".main-panel"):$("body").hasClass("off-canvas-sidebar")&&e.appendTo(".wrapper-full-page"),setTimeout(function(){e.addClass("visible")},100),e.click(function(){$("html").removeClass("nav-open"),mobile_menu_visible=0,e.removeClass("visible"),setTimeout(function(){e.remove(),$toggle.removeClass("toggled")},400)}),$("html").addClass("nav-open"),mobile_menu_visible=1}}),$(window).resize(function(){md.initSidebarsCheck(),seq=seq2=0,setTimeout(function(){md.initDashboardPageCharts()},500)}),md={misc:{navbar_menu_visible:0,active_collapse:!0,disabled_collapse_init:0},checkSidebarImage:function(){$sidebar=$(".sidebar"),image_src=$sidebar.data("image"),void 0!==image_src&&(sidebar_container='<div class="sidebar-background" style="background-image: url('+image_src+') "/>',$sidebar.append(sidebar_container))},showNotification:function(e,a){type=["","info","danger","success","warning","rose","primary"],color=Math.floor(6*Math.random()+1),$.notify({icon:"add_alert",message:"Welcome to <b>Material Dashboard Pro</b> - a beautiful admin panel for every web developer."},{type:type[color],timer:3e3,placement:{from:e,align:a}})},initDocumentationCharts:function(){if(0!=$("#dailySalesChart").length&&0!=$("#websiteViewsChart").length){dataDailySalesChart={labels:["M","T","W","T","F","S","S"],series:[[12,17,7,17,23,18,38]]},optionsDailySalesChart={lineSmooth:Chartist.Interpolation.cardinal({tension:0}),low:0,high:50,chartPadding:{top:0,right:0,bottom:0,left:0}};new Chartist.Line("#dailySalesChart",dataDailySalesChart,optionsDailySalesChart),new Chartist.Line("#websiteViewsChart",dataDailySalesChart,optionsDailySalesChart)}},initFormExtendedDatetimepickers:function(){$(".datetimepicker").datetimepicker({icons:{time:"fa fa-clock-o",date:"fa fa-calendar",up:"fa fa-chevron-up",down:"fa fa-chevron-down",previous:"fa fa-chevron-left",next:"fa fa-chevron-right",today:"fa fa-screenshot",clear:"fa fa-trash",close:"fa fa-remove"}}),$(".datepicker").datetimepicker({format:"MM/DD/YYYY",icons:{time:"fa fa-clock-o",date:"fa fa-calendar",up:"fa fa-chevron-up",down:"fa fa-chevron-down",previous:"fa fa-chevron-left",next:"fa fa-chevron-right",today:"fa fa-screenshot",clear:"fa fa-trash",close:"fa fa-remove"}}),$(".timepicker").datetimepicker({format:"h:mm A",icons:{time:"fa fa-clock-o",date:"fa fa-calendar",up:"fa fa-chevron-up",down:"fa fa-chevron-down",previous:"fa fa-chevron-left",next:"fa fa-chevron-right",today:"fa fa-screenshot",clear:"fa fa-trash",close:"fa fa-remove"}})},initSliders:function(){var e=document.getElementById("sliderRegular");noUiSlider.create(e,{start:40,connect:[!0,!1],range:{min:0,max:100}});var a=document.getElementById("sliderDouble");noUiSlider.create(a,{start:[20,60],connect:!0,range:{min:0,max:100}})},initSidebarsCheck:function(){$(window).width()<=991&&0!=$sidebar.length&&md.initRightMenu()},checkFullPageBackgroundImage:function(){$page=$(".full-page"),image_src=$page.data("image"),void 0!==image_src&&(image_container='<div class="full-page-background" style="background-image: url('+image_src+') "/>',$page.append(image_container))},initDashboardPageCharts:function(){if(0!=$("#dailySalesChart").length||0!=$("#completedTasksChart").length||0!=$("#websiteViewsChart").length){dataDailySalesChart={labels:["M","T","W","T","F","S","S"],series:[[12,17,7,17,23,18,38]]},optionsDailySalesChart={lineSmooth:Chartist.Interpolation.cardinal({tension:0}),low:0,high:50,chartPadding:{top:0,right:0,bottom:0,left:0}};var e=new Chartist.Line("#dailySalesChart",dataDailySalesChart,optionsDailySalesChart);md.startAnimationForLineChart(e),dataCompletedTasksChart={labels:["12p","3p","6p","9p","12p","3a","6a","9a"],series:[[230,750,450,300,280,240,200,190]]},optionsCompletedTasksChart={lineSmooth:Chartist.Interpolation.cardinal({tension:0}),low:0,high:1e3,chartPadding:{top:0,right:0,bottom:0,left:0}};var a=new Chartist.Line("#completedTasksChart",dataCompletedTasksChart,optionsCompletedTasksChart);md.startAnimationForLineChart(a);var t=Chartist.Bar("#websiteViewsChart",{labels:["J","F","M","A","M","J","J","A","S","O","N","D"],series:[[542,443,320,780,553,453,326,434,568,610,756,895]]},{axisX:{showGrid:!1},low:0,high:1e3,chartPadding:{top:0,right:5,bottom:0,left:0}},[["screen and (max-width: 640px)",{seriesBarDistance:5,axisX:{labelInterpolationFnc:function(e){return e[0]}}}]]);md.startAnimationForBarChart(t)}},initMinimizeSidebar:function(){$("#minimizeSidebar").click(function(){$(this);1==md.misc.sidebar_mini_active?($("body").removeClass("sidebar-mini"),md.misc.sidebar_mini_active=!1):($("body").addClass("sidebar-mini"),md.misc.sidebar_mini_active=!0);var e=setInterval(function(){window.dispatchEvent(new Event("resize"))},180);setTimeout(function(){clearInterval(e)},1e3)})},checkScrollForTransparentNavbar:debounce(function(){260<$(document).scrollTop()?transparent&&(transparent=!1,$(".navbar-color-on-scroll").removeClass("navbar-transparent")):transparent||(transparent=!0,$(".navbar-color-on-scroll").addClass("navbar-transparent"))},17),initRightMenu:debounce(function(){$sidebar_wrapper=$(".sidebar-wrapper"),mobile_menu_initialized?991<$(window).width()&&($sidebar_wrapper.find(".navbar-form").remove(),$sidebar_wrapper.find(".nav-mobile-menu").remove(),mobile_menu_initialized=!1):($navbar=$("nav").find(".navbar-collapse").children(".navbar-nav"),mobile_menu_content="",nav_content=$navbar.html(),nav_content='<ul class="nav navbar-nav nav-mobile-menu">'+nav_content+"</ul>",navbar_form=$("nav").find(".navbar-form").get(0).outerHTML,$sidebar_nav=$sidebar_wrapper.find(" > .nav"),$nav_content=$(nav_content),$navbar_form=$(navbar_form),$nav_content.insertBefore($sidebar_nav),$navbar_form.insertBefore($nav_content),$(".sidebar-wrapper .dropdown .dropdown-menu > li > a").click(function(e){e.stopPropagation()}),window.dispatchEvent(new Event("resize")),mobile_menu_initialized=!0)},200),startAnimationForLineChart:function(e){e.on("draw",function(e){"line"===e.type||"area"===e.type?e.element.animate({d:{begin:600,dur:700,from:e.path.clone().scale(1,0).translate(0,e.chartRect.height()).stringify(),to:e.path.clone().stringify(),easing:Chartist.Svg.Easing.easeOutQuint}}):"point"===e.type&&(seq++,e.element.animate({opacity:{begin:seq*delays,dur:durations,from:0,to:1,easing:"ease"}}))}),seq=0},startAnimationForBarChart:function(e){e.on("draw",function(e){"bar"===e.type&&(seq2++,e.element.animate({opacity:{begin:seq2*delays2,dur:durations2,from:0,to:1,easing:"ease"}}))}),seq2=0},initFullCalendar:function(){$calendar=$("#fullCalendar"),today=new Date,y=today.getFullYear(),m=today.getMonth(),d=today.getDate(),$calendar.fullCalendar({viewRender:function(e,a){"month"!=e.name&&$(a).find(".fc-scroller").perfectScrollbar()},header:{left:"title",center:"month,agendaWeek,agendaDay",right:"prev,next,today"},defaultDate:today,selectable:!0,selectHelper:!0,views:{month:{titleFormat:"MMMM YYYY"},week:{titleFormat:" MMMM D YYYY"},day:{titleFormat:"D MMM, YYYY"}},select:function(t,n){swal({title:"Create an Event",html:'<div class="form-group"><input class="form-control" placeholder="Event Title" id="input-field"></div>',showCancelButton:!0,confirmButtonClass:"btn btn-success",cancelButtonClass:"btn btn-danger",buttonsStyling:!1}).then(function(e){var a;event_title=$("#input-field").val(),event_title&&(a={title:event_title,start:t,end:n},$calendar.fullCalendar("renderEvent",a,!0)),$calendar.fullCalendar("unselect")}).catch(swal.noop)},editable:!0,eventLimit:!0,events:[{title:"All Day Event",start:new Date(y,m,1),className:"event-default"},{id:999,title:"Repeating Event",start:new Date(y,m,d-4,6,0),allDay:!1,className:"event-rose"},{id:999,title:"Repeating Event",start:new Date(y,m,d+3,6,0),allDay:!1,className:"event-rose"},{title:"Meeting",start:new Date(y,m,d-1,10,30),allDay:!1,className:"event-green"},{title:"Lunch",start:new Date(y,m,d+7,12,0),end:new Date(y,m,d+7,14,0),allDay:!1,className:"event-red"},{title:"Md-pro Launch",start:new Date(y,m,d-2,12,0),allDay:!0,className:"event-azure"},{title:"Birthday Party",start:new Date(y,m,d+1,19,0),end:new Date(y,m,d+1,22,30),allDay:!1,className:"event-azure"},{title:"Click for Creative Tim",start:new Date(y,m,21),end:new Date(y,m,22),url:"http://www.creative-tim.com/",className:"event-orange"},{title:"Click for Google",start:new Date(y,m,21),end:new Date(y,m,22),url:"http://www.creative-tim.com/",className:"event-orange"}]})},initVectorMap:function(){$("#worldMap").vectorMap({map:"world_mill_en",backgroundColor:"transparent",zoomOnScroll:!1,regionStyle:{initial:{fill:"#e4e4e4","fill-opacity":.9,stroke:"none","stroke-width":0,"stroke-opacity":0}},series:{regions:[{values:{AU:760,BR:550,CA:120,DE:1300,FR:540,GB:690,GE:200,IN:200,RO:600,RU:300,US:2920},scale:["#AAAAAA","#444444"],normalizeFunction:"polynomial"}]}})}};
//# sourceMappingURL=_site_dashboard_pro/assets/js/dashboard-pro.js.map


File: /public\js\plugins\bootstrap-notify.js
/*



     Creative Tim Modifications

     Lines: 236 was changed from top: 5px to top: 50% and we added margin-top: -9px. In this way the close button will be aligned vertically
     Line:219 - modified when the icon is set, we add the class "alert-with-icon", so there will be enough space for the icon.
	 Lines: 179/222 - class() was changed to html() so we can add the Material Design Icons



*/


/*
 * Project: Bootstrap Notify = v3.1.5
 * Description: Turns standard Bootstrap alerts into "Growl-like" notifications.
 * Author: Mouse0270 aka Robert McIntosh
 * License: MIT License
 * Website: https://github.com/mouse0270/bootstrap-growl
 */

/* global define:false, require: false, jQuery:false */

(function(factory) {
    if (typeof define === 'function' && define.amd) {
        // AMD. Register as an anonymous module.
        define(['jquery'], factory);
    } else if (typeof exports === 'object') {
        // Node/CommonJS
        factory(require('jquery'));
    } else {
        // Browser globals
        factory(jQuery);
    }
}(function($) {
    // Create the defaults once
    var defaults = {
        element: 'body',
        position: null,
        type: "info",
        allow_dismiss: true,
        allow_duplicates: true,
        newest_on_top: false,
        showProgressbar: false,
        placement: {
            from: "top",
            align: "right"
        },
        offset: 20,
        spacing: 10,
        z_index: 1031,
        delay: 5000,
        timer: 1000,
        url_target: '_blank',
        mouse_over: null,
        animate: {
            enter: 'animated fadeInDown',
            exit: 'animated fadeOutUp'
        },
        onShow: null,
        onShown: null,
        onClose: null,
        onClosed: null,
        icon_type: 'class',
        template: '<div data-notify="container" class="col-11 col-md-4 alert alert-{0}" role="alert"><button type="button" aria-hidden="true" class="close" data-notify="dismiss"><i class="fas fa-window-close"></i> </button><i data-notify="icon" class="material-icons"></i><span data-notify="title">{1}</span> <span data-notify="message">{2}</span><div class="progress" data-notify="progressbar"><div class="progress-bar progress-bar-{0}" role="progressbar" aria-valuenow="0" aria-valuemin="0" aria-valuemax="100" style="width: 0%;"></div></div><a href="{3}" target="{4}" data-notify="url"></a></div>'
    };

    String.format = function() {
        var str = arguments[0];
        for (var i = 1; i < arguments.length; i++) {
            str = str.replace(RegExp("\\{" + (i - 1) + "\\}", "gm"), arguments[i]);
        }
        return str;
    };

    function isDuplicateNotification(notification) {
        var isDupe = false;

        $('[data-notify="container"]').each(function(i, el) {
            var $el = $(el);
            var title = $el.find('[data-notify="title"]').text().trim();
            var message = $el.find('[data-notify="message"]').html().trim();

            // The input string might be different than the actual parsed HTML string!
            // (<br> vs <br /> for example)
            // So we have to force-parse this as HTML here!
            var isSameTitle = title === $("<div>" + notification.settings.content.title + "</div>").html().trim();
            var isSameMsg = message === $("<div>" + notification.settings.content.message + "</div>").html().trim();
            var isSameType = $el.hasClass('alert-' + notification.settings.type);

            if (isSameTitle && isSameMsg && isSameType) {
                //we found the dupe. Set the var and stop checking.
                isDupe = true;
            }
            return !isDupe;
        });

        return isDupe;
    }

    function Notify(element, content, options) {
        // Setup Content of Notify
        var contentObj = {
            content: {
                message: typeof content === 'object' ? content.message : content,
                title: content.title ? content.title : '',
                icon: content.icon ? content.icon : '',
                url: content.url ? content.url : '#',
                target: content.target ? content.target : '-'
            }
        };

        options = $.extend(true, {}, contentObj, options);
        this.settings = $.extend(true, {}, defaults, options);
        this._defaults = defaults;
        if (this.settings.content.target === "-") {
            this.settings.content.target = this.settings.url_target;
        }
        this.animations = {
            start: 'webkitAnimationStart oanimationstart MSAnimationStart animationstart',
            end: 'webkitAnimationEnd oanimationend MSAnimationEnd animationend'
        };

        if (typeof this.settings.offset === 'number') {
            this.settings.offset = {
                x: this.settings.offset,
                y: this.settings.offset
            };
        }

        //if duplicate messages are not allowed, then only continue if this new message is not a duplicate of one that it already showing
        if (this.settings.allow_duplicates || (!this.settings.allow_duplicates && !isDuplicateNotification(this))) {
            this.init();
        }
    }

    $.extend(Notify.prototype, {
        init: function() {
            var self = this;

            this.buildNotify();
            if (this.settings.content.icon) {
                this.setIcon();
            }
            if (this.settings.content.url != "#") {
                this.styleURL();
            }
            this.styleDismiss();
            this.placement();
            this.bind();

            this.notify = {
                $ele: this.$ele,
                update: function(command, update) {
                    var commands = {};
                    if (typeof command === "string") {
                        commands[command] = update;
                    } else {
                        commands = command;
                    }
                    for (var cmd in commands) {
                        switch (cmd) {
                            case "type":
                                this.$ele.removeClass('alert-' + self.settings.type);
                                this.$ele.find('[data-notify="progressbar"] > .progress-bar').removeClass('progress-bar-' + self.settings.type);
                                self.settings.type = commands[cmd];
                                this.$ele.addClass('alert-' + commands[cmd]).find('[data-notify="progressbar"] > .progress-bar').addClass('progress-bar-' + commands[cmd]);
                                break;
                            case "icon":
                                var $icon = this.$ele.find('[data-notify="icon"]');
                                if (self.settings.icon_type.toLowerCase() === 'class') {
                                    $icon.html(commands[cmd]);
                                } else {
                                    if (!$icon.is('img')) {
                                        $icon.find('img');
                                    }
                                    $icon.attr('src', commands[cmd]);
                                }
                                break;
                            case "progress":
                                var newDelay = self.settings.delay - (self.settings.delay * (commands[cmd] / 100));
                                this.$ele.data('notify-delay', newDelay);
                                this.$ele.find('[data-notify="progressbar"] > div').attr('aria-valuenow', commands[cmd]).css('width', commands[cmd] + '%');
                                break;
                            case "url":
                                this.$ele.find('[data-notify="url"]').attr('href', commands[cmd]);
                                break;
                            case "target":
                                this.$ele.find('[data-notify="url"]').attr('target', commands[cmd]);
                                break;
                            default:
                                this.$ele.find('[data-notify="' + cmd + '"]').html(commands[cmd]);
                        }
                    }
                    var posX = this.$ele.outerHeight() + parseInt(self.settings.spacing) + parseInt(self.settings.offset.y);
                    self.reposition(posX);
                },
                close: function() {
                    self.close();
                }
            };

        },
        buildNotify: function() {
            var content = this.settings.content;
            this.$ele = $(String.format(this.settings.template, this.settings.type, content.title, content.message, content.url, content.target));
            this.$ele.attr('data-notify-position', this.settings.placement.from + '-' + this.settings.placement.align);
            if (!this.settings.allow_dismiss) {
                this.$ele.find('[data-notify="dismiss"]').css('display', 'none');
            }
            if ((this.settings.delay <= 0 && !this.settings.showProgressbar) || !this.settings.showProgressbar) {
                this.$ele.find('[data-notify="progressbar"]').remove();
            }
        },
        setIcon: function() {

            this.$ele.addClass('alert-with-icon');

            if (this.settings.icon_type.toLowerCase() === 'class') {
                this.$ele.find('[data-notify="icon"]').html(this.settings.content.icon);
            } else {
                if (this.$ele.find('[data-notify="icon"]').is('img')) {
                    this.$ele.find('[data-notify="icon"]').attr('src', this.settings.content.icon);
                } else {
                    this.$ele.find('[data-notify="icon"]').append('<img src="' + this.settings.content.icon + '" alt="Notify Icon" />');
                }
            }
        },
        styleDismiss: function() {
            this.$ele.find('[data-notify="dismiss"]').css({
                position: 'absolute',
                right: '10px',
                top: '50%',
                marginTop: '-9px',
                zIndex: this.settings.z_index + 2
            });
        },
        styleURL: function() {
            this.$ele.find('[data-notify="url"]').css({
                backgroundImage: 'url(data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)',
                height: '100%',
                left: 0,
                position: 'absolute',
                top: 0,
                width: '100%',
                zIndex: this.settings.z_index + 1
            });
        },
        placement: function() {
            var self = this,
                offsetAmt = this.settings.offset.y,
                css = {
                    display: 'inline-block',
                    margin: '15px auto',
                    position: this.settings.position ? this.settings.position : (this.settings.element === 'body' ? 'fixed' : 'absolute'),
                    transition: 'all .5s ease-in-out',
                    zIndex: this.settings.z_index
                },
                hasAnimation = false,
                settings = this.settings;

            $('[data-notify-position="' + this.settings.placement.from + '-' + this.settings.placement.align + '"]:not([data-closing="true"])').each(function() {
                offsetAmt = Math.max(offsetAmt, parseInt($(this).css(settings.placement.from)) + parseInt($(this).outerHeight()) + parseInt(settings.spacing));
            });
            if (this.settings.newest_on_top === true) {
                offsetAmt = this.settings.offset.y;
            }
            css[this.settings.placement.from] = offsetAmt + 'px';

            switch (this.settings.placement.align) {
                case "left":
                case "right":
                    css[this.settings.placement.align] = this.settings.offset.x + 'px';
                    break;
                case "center":
                    css.left = 0;
                    css.right = 0;
                    break;
            }
            this.$ele.css(css).addClass(this.settings.animate.enter);
            $.each(Array('webkit-', 'moz-', 'o-', 'ms-', ''), function(index, prefix) {
                self.$ele[0].style[prefix + 'AnimationIterationCount'] = 1;
            });

            $(this.settings.element).append(this.$ele);

            if (this.settings.newest_on_top === true) {
                offsetAmt = (parseInt(offsetAmt) + parseInt(this.settings.spacing)) + this.$ele.outerHeight();
                this.reposition(offsetAmt);
            }

            if ($.isFunction(self.settings.onShow)) {
                self.settings.onShow.call(this.$ele);
            }

            this.$ele.one(this.animations.start, function() {
                hasAnimation = true;
            }).one(this.animations.end, function() {
                if ($.isFunction(self.settings.onShown)) {
                    self.settings.onShown.call(this);
                }
            });

            setTimeout(function() {
                if (!hasAnimation) {
                    if ($.isFunction(self.settings.onShown)) {
                        self.settings.onShown.call(this);
                    }
                }
            }, 600);
        },
        bind: function() {
            var self = this;

            this.$ele.find('[data-notify="dismiss"]').on('click', function() {
                self.close();
            });

            this.$ele.mouseover(function() {
                $(this).data('data-hover', "true");
            }).mouseout(function() {
                $(this).data('data-hover', "false");
            });
            this.$ele.data('data-hover', "false");

            if (this.settings.delay > 0) {
                self.$ele.data('notify-delay', self.settings.delay);
                var timer = setInterval(function() {
                    var delay = parseInt(self.$ele.data('notify-delay')) - self.settings.timer;
                    if ((self.$ele.data('data-hover') === 'false' && self.settings.mouse_over === "pause") || self.settings.mouse_over != "pause") {
                        var percent = ((self.settings.delay - delay) / self.settings.delay) * 100;
                        self.$ele.data('notify-delay', delay);
                        self.$ele.find('[data-notify="progressbar"] > div').attr('aria-valuenow', percent).css('width', percent + '%');
                    }
                    if (delay <= -(self.settings.timer)) {
                        clearInterval(timer);
                        self.close();
                    }
                }, self.settings.timer);
            }
        },
        close: function() {
            var self = this,
                posX = parseInt(this.$ele.css(this.settings.placement.from)),
                hasAnimation = false;

            this.$ele.data('closing', 'true').addClass(this.settings.animate.exit);
            self.reposition(posX);

            if ($.isFunction(self.settings.onClose)) {
                self.settings.onClose.call(this.$ele);
            }

            this.$ele.one(this.animations.start, function() {
                hasAnimation = true;
            }).one(this.animations.end, function() {
                $(this).remove();
                if ($.isFunction(self.settings.onClosed)) {
                    self.settings.onClosed.call(this);
                }
            });

            setTimeout(function() {
                if (!hasAnimation) {
                    self.$ele.remove();
                    if (self.settings.onClosed) {
                        self.settings.onClosed(self.$ele);
                    }
                }
            }, 600);
        },
        reposition: function(posX) {
            var self = this,
                notifies = '[data-notify-position="' + this.settings.placement.from + '-' + this.settings.placement.align + '"]:not([data-closing="true"])',
                $elements = this.$ele.nextAll(notifies);
            if (this.settings.newest_on_top === true) {
                $elements = this.$ele.prevAll(notifies);
            }
            $elements.each(function() {
                $(this).css(self.settings.placement.from, posX);
                posX = (parseInt(posX) + parseInt(self.settings.spacing)) + $(this).outerHeight();
            });
        }
    });

    $.notify = function(content, options) {
        var plugin = new Notify(this, content, options);
        return plugin.notify;
    };
    $.notifyDefaults = function(options) {
        defaults = $.extend(true, {}, defaults, options);
        return defaults;
    };
    $.notifyClose = function(command) {
        if (typeof command === "undefined" || command === "all") {
            $('[data-notify]').find('[data-notify="dismiss"]').trigger('click');
        } else {
            $('[data-notify-position="' + command + '"]').find('[data-notify="dismiss"]').trigger('click');
        }
    };

}));


File: /public\js\plugins\sweetalert2.js
/*!
* sweetalert2 v7.24.1
* Released under the MIT License.
*/
(function (global, factory) {
	typeof exports === 'object' && typeof module !== 'undefined' ? module.exports = factory() :
	typeof define === 'function' && define.amd ? define(factory) :
	(global.Sweetalert2 = factory());
}(this, (function () { 'use strict';

var _typeof = typeof Symbol === "function" && typeof Symbol.iterator === "symbol" ? function (obj) {
  return typeof obj;
} : function (obj) {
  return obj && typeof Symbol === "function" && obj.constructor === Symbol && obj !== Symbol.prototype ? "symbol" : typeof obj;
};











var classCallCheck = function (instance, Constructor) {
  if (!(instance instanceof Constructor)) {
    throw new TypeError("Cannot call a class as a function");
  }
};

var createClass = function () {
  function defineProperties(target, props) {
    for (var i = 0; i < props.length; i++) {
      var descriptor = props[i];
      descriptor.enumerable = descriptor.enumerable || false;
      descriptor.configurable = true;
      if ("value" in descriptor) descriptor.writable = true;
      Object.defineProperty(target, descriptor.key, descriptor);
    }
  }

  return function (Constructor, protoProps, staticProps) {
    if (protoProps) defineProperties(Constructor.prototype, protoProps);
    if (staticProps) defineProperties(Constructor, staticProps);
    return Constructor;
  };
}();







var _extends = Object.assign || function (target) {
  for (var i = 1; i < arguments.length; i++) {
    var source = arguments[i];

    for (var key in source) {
      if (Object.prototype.hasOwnProperty.call(source, key)) {
        target[key] = source[key];
      }
    }
  }

  return target;
};

var get = function get(object, property, receiver) {
  if (object === null) object = Function.prototype;
  var desc = Object.getOwnPropertyDescriptor(object, property);

  if (desc === undefined) {
    var parent = Object.getPrototypeOf(object);

    if (parent === null) {
      return undefined;
    } else {
      return get(parent, property, receiver);
    }
  } else if ("value" in desc) {
    return desc.value;
  } else {
    var getter = desc.get;

    if (getter === undefined) {
      return undefined;
    }

    return getter.call(receiver);
  }
};

var inherits = function (subClass, superClass) {
  if (typeof superClass !== "function" && superClass !== null) {
    throw new TypeError("Super expression must either be null or a function, not " + typeof superClass);
  }

  subClass.prototype = Object.create(superClass && superClass.prototype, {
    constructor: {
      value: subClass,
      enumerable: false,
      writable: true,
      configurable: true
    }
  });
  if (superClass) Object.setPrototypeOf ? Object.setPrototypeOf(subClass, superClass) : subClass.__proto__ = superClass;
};











var possibleConstructorReturn = function (self, call) {
  if (!self) {
    throw new ReferenceError("this hasn't been initialised - super() hasn't been called");
  }

  return call && (typeof call === "object" || typeof call === "function") ? call : self;
};





var slicedToArray = function () {
  function sliceIterator(arr, i) {
    var _arr = [];
    var _n = true;
    var _d = false;
    var _e = undefined;

    try {
      for (var _i = arr[Symbol.iterator](), _s; !(_n = (_s = _i.next()).done); _n = true) {
        _arr.push(_s.value);

        if (i && _arr.length === i) break;
      }
    } catch (err) {
      _d = true;
      _e = err;
    } finally {
      try {
        if (!_n && _i["return"]) _i["return"]();
      } finally {
        if (_d) throw _e;
      }
    }

    return _arr;
  }

  return function (arr, i) {
    if (Array.isArray(arr)) {
      return arr;
    } else if (Symbol.iterator in Object(arr)) {
      return sliceIterator(arr, i);
    } else {
      throw new TypeError("Invalid attempt to destructure non-iterable instance");
    }
  };
}();

var consolePrefix = 'SweetAlert2:';

/**
 * Filter the unique values into a new array
 * @param arr
 */
var uniqueArray = function uniqueArray(arr) {
  var result = [];
  for (var i = 0; i < arr.length; i++) {
    if (result.indexOf(arr[i]) === -1) {
      result.push(arr[i]);
    }
  }
  return result;
};

/**
 * Converts `inputOptions` into an array of `[value, label]`s
 * @param inputOptions
 */
var formatInputOptions = function formatInputOptions(inputOptions) {
  var result = [];
  if (typeof Map !== 'undefined' && inputOptions instanceof Map) {
    inputOptions.forEach(function (value, key) {
      result.push([key, value]);
    });
  } else {
    Object.keys(inputOptions).forEach(function (key) {
      result.push([key, inputOptions[key]]);
    });
  }
  return result;
};

/**
 * Standardise console warnings
 * @param message
 */
var warn = function warn(message) {
  console.warn(consolePrefix + ' ' + message);
};

/**
 * Standardise console errors
 * @param message
 */
var error = function error(message) {
  console.error(consolePrefix + ' ' + message);
};

/**
 * Private global state for `warnOnce`
 * @type {Array}
 * @private
 */
var previousWarnOnceMessages = [];

/**
 * Show a console warning, but only if it hasn't already been shown
 * @param message
 */
var warnOnce = function warnOnce(message) {
  if (!(previousWarnOnceMessages.indexOf(message) !== -1)) {
    previousWarnOnceMessages.push(message);
    warn(message);
  }
};

/**
 * If `arg` is a function, call it (with no arguments or context) and return the result.
 * Otherwise, just pass the value through
 * @param arg
 */
var callIfFunction = function callIfFunction(arg) {
  return typeof arg === 'function' ? arg() : arg;
};

var isThenable = function isThenable(arg) {
  return (typeof arg === 'undefined' ? 'undefined' : _typeof(arg)) === 'object' && typeof arg.then === 'function';
};

var DismissReason = Object.freeze({
  cancel: 'cancel',
  backdrop: 'overlay',
  close: 'close',
  esc: 'esc',
  timer: 'timer'
});

var version = "7.24.1";

var argsToParams = function argsToParams(args) {
  var params = {};
  switch (_typeof(args[0])) {
    case 'string':
      ['title', 'html', 'type'].forEach(function (name, index) {
        switch (_typeof(args[index])) {
          case 'string':
            params[name] = args[index];
            break;
          case 'undefined':
            break;
          default:
            error('Unexpected type of ' + name + '! Expected "string", got ' + _typeof(args[index]));
        }
      });
      break;

    case 'object':
      _extends(params, args[0]);
      break;

    default:
      error('Unexpected type of argument! Expected "string" or "object", got ' + _typeof(args[0]));
      return false;
  }
  return params;
};

/**
 * Adapt a legacy inputValidator for use with expectRejections=false
 */
var adaptInputValidator = function adaptInputValidator(legacyValidator) {
  return function adaptedInputValidator(inputValue, extraParams) {
    return legacyValidator.call(this, inputValue, extraParams).then(function () {
      return undefined;
    }, function (validationError) {
      return validationError;
    });
  };
};

var swalPrefix = 'swal2-';

var prefix = function prefix(items) {
  var result = {};
  for (var i in items) {
    result[items[i]] = swalPrefix + items[i];
  }
  return result;
};

var swalClasses = prefix(['container', 'shown', 'height-auto', 'iosfix', 'popup', 'modal', 'no-backdrop', 'toast', 'toast-shown', 'fade', 'show', 'hide', 'noanimation', 'close', 'title', 'header', 'content', 'actions', 'confirm', 'cancel', 'footer', 'icon', 'icon-text', 'image', 'input', 'has-input', 'file', 'range', 'select', 'radio', 'checkbox', 'textarea', 'inputerror', 'validationerror', 'progresssteps', 'activeprogressstep', 'progresscircle', 'progressline', 'loading', 'styled', 'top', 'top-start', 'top-end', 'top-left', 'top-right', 'center', 'center-start', 'center-end', 'center-left', 'center-right', 'bottom', 'bottom-start', 'bottom-end', 'bottom-left', 'bottom-right', 'grow-row', 'grow-column', 'grow-fullscreen']);

var iconTypes = prefix(['success', 'warning', 'info', 'question', 'error']);

// Remember state in cases where opening and handling a modal will fiddle with it.
var states = {
  previousBodyPadding: null
};

var hasClass = function hasClass(elem, className) {
  if (elem.classList) {
    return elem.classList.contains(className);
  }
  return false;
};

var focusInput = function focusInput(input) {
  input.focus();

  // place cursor at end of text in text input
  if (input.type !== 'file') {
    // http://stackoverflow.com/a/2345915/1331425
    var val = input.value;
    input.value = '';
    input.value = val;
  }
};

var addOrRemoveClass = function addOrRemoveClass(target, classList, add) {
  if (!target || !classList) {
    return;
  }
  if (typeof classList === 'string') {
    classList = classList.split(/\s+/).filter(Boolean);
  }
  classList.forEach(function (className) {
    if (target.forEach) {
      target.forEach(function (elem) {
        add ? elem.classList.add(className) : elem.classList.remove(className);
      });
    } else {
      add ? target.classList.add(className) : target.classList.remove(className);
    }
  });
};

var addClass = function addClass(target, classList) {
  addOrRemoveClass(target, classList, true);
};

var removeClass = function removeClass(target, classList) {
  addOrRemoveClass(target, classList, false);
};

var getChildByClass = function getChildByClass(elem, className) {
  for (var i = 0; i < elem.childNodes.length; i++) {
    if (hasClass(elem.childNodes[i], className)) {
      return elem.childNodes[i];
    }
  }
};

var show = function show(elem) {
  elem.style.opacity = '';
  elem.style.display = elem.id === swalClasses.content ? 'block' : 'flex';
};

var hide = function hide(elem) {
  elem.style.opacity = '';
  elem.style.display = 'none';
};

var empty = function empty(elem) {
  while (elem.firstChild) {
    elem.removeChild(elem.firstChild);
  }
};

// borrowed from jquery $(elem).is(':visible') implementation
var isVisible = function isVisible(elem) {
  return elem && (elem.offsetWidth || elem.offsetHeight || elem.getClientRects().length);
};

var removeStyleProperty = function removeStyleProperty(elem, property) {
  if (elem.style.removeProperty) {
    elem.style.removeProperty(property);
  } else {
    elem.style.removeAttribute(property);
  }
};

var getContainer = function getContainer() {
  return document.body.querySelector('.' + swalClasses.container);
};

var elementByClass = function elementByClass(className) {
  var container = getContainer();
  return container ? container.querySelector('.' + className) : null;
};

var getPopup = function getPopup() {
  return elementByClass(swalClasses.popup);
};

var getIcons = function getIcons() {
  var popup = getPopup();
  return popup.querySelectorAll('.' + swalClasses.icon);
};

var getTitle = function getTitle() {
  return elementByClass(swalClasses.title);
};

var getContent = function getContent() {
  return elementByClass(swalClasses.content);
};

var getImage = function getImage() {
  return elementByClass(swalClasses.image);
};

var getProgressSteps = function getProgressSteps() {
  return elementByClass(swalClasses.progresssteps);
};

var getValidationError = function getValidationError() {
  return elementByClass(swalClasses.validationerror);
};

var getConfirmButton = function getConfirmButton() {
  return elementByClass(swalClasses.confirm);
};

var getCancelButton = function getCancelButton() {
  return elementByClass(swalClasses.cancel);
};

var getButtonsWrapper = function getButtonsWrapper() {
  warnOnce('swal.getButtonsWrapper() is deprecated and will be removed in the next major release, use swal.getActions() instead');
  return elementByClass(swalClasses.actions);
};

var getActions = function getActions() {
  return elementByClass(swalClasses.actions);
};

var getFooter = function getFooter() {
  return elementByClass(swalClasses.footer);
};

var getCloseButton = function getCloseButton() {
  return elementByClass(swalClasses.close);
};

var getFocusableElements = function getFocusableElements() {
  var focusableElementsWithTabindex = Array.prototype.slice.call(getPopup().querySelectorAll('[tabindex]:not([tabindex="-1"]):not([tabindex="0"])'))
  // sort according to tabindex
  .sort(function (a, b) {
    a = parseInt(a.getAttribute('tabindex'));
    b = parseInt(b.getAttribute('tabindex'));
    if (a > b) {
      return 1;
    } else if (a < b) {
      return -1;
    }
    return 0;
  });

  // https://github.com/jkup/focusable/blob/master/index.js
  var otherFocusableElements = Array.prototype.slice.call(getPopup().querySelectorAll('a[href], area[href], input:not([disabled]), select:not([disabled]), textarea:not([disabled]), button:not([disabled]), iframe, object, embed, [tabindex="0"], [contenteditable], audio[controls], video[controls]'));

  return uniqueArray(focusableElementsWithTabindex.concat(otherFocusableElements));
};

var isModal = function isModal() {
  return !document.body.classList.contains(swalClasses['toast-shown']);
};

var isToast = function isToast() {
  return document.body.classList.contains(swalClasses['toast-shown']);
};

var isLoading = function isLoading() {
  return getPopup().hasAttribute('data-loading');
};

// Detect Node env
var isNodeEnv = function isNodeEnv() {
  return typeof window === 'undefined' || typeof document === 'undefined';
};

var sweetHTML = ('\n <div aria-labelledby="' + swalClasses.title + '" aria-describedby="' + swalClasses.content + '" class="' + swalClasses.popup + '" tabindex="-1">\n   <div class="' + swalClasses.header + '">\n     <ul class="' + swalClasses.progresssteps + '"></ul>\n     <div class="' + swalClasses.icon + ' ' + iconTypes.error + '">\n       <span class="swal2-x-mark"><span class="swal2-x-mark-line-left"></span><span class="swal2-x-mark-line-right"></span></span>\n     </div>\n     <div class="' + swalClasses.icon + ' ' + iconTypes.question + '">\n       <span class="' + swalClasses['icon-text'] + '">?</span>\n      </div>\n     <div class="' + swalClasses.icon + ' ' + iconTypes.warning + '">\n       <span class="' + swalClasses['icon-text'] + '">!</span>\n      </div>\n     <div class="' + swalClasses.icon + ' ' + iconTypes.info + '">\n       <span class="' + swalClasses['icon-text'] + '">i</span>\n      </div>\n     <div class="' + swalClasses.icon + ' ' + iconTypes.success + '">\n       <div class="swal2-success-circular-line-left"></div>\n       <span class="swal2-success-line-tip"></span> <span class="swal2-success-line-long"></span>\n       <div class="swal2-success-ring"></div> <div class="swal2-success-fix"></div>\n       <div class="swal2-success-circular-line-right"></div>\n     </div>\n     <img class="' + swalClasses.image + '" />\n     <h2 class="' + swalClasses.title + '" id="' + swalClasses.title + '"></h2>\n     <button type="button" class="' + swalClasses.close + '">\xD7</button>\n   </div>\n   <div class="' + swalClasses.content + '">\n     <div id="' + swalClasses.content + '"></div>\n     <input class="' + swalClasses.input + '" />\n     <input type="file" class="' + swalClasses.file + '" />\n     <div class="' + swalClasses.range + '">\n       <input type="range" />\n       <output></output>\n     </div>\n     <select class="' + swalClasses.select + '"></select>\n     <div class="' + swalClasses.radio + '"></div>\n     <label for="' + swalClasses.checkbox + '" class="' + swalClasses.checkbox + '">\n       <input type="checkbox" />\n     </label>\n     <textarea class="' + swalClasses.textarea + '"></textarea>\n     <div class="' + swalClasses.validationerror + '" id="' + swalClasses.validationerror + '"></div>\n   </div>\n   <div class="' + swalClasses.actions + '">\n     <button type="button" class="' + swalClasses.confirm + '">OK</button>\n     <button type="button" class="' + swalClasses.cancel + '">Cancel</button>\n   </div>\n   <div class="' + swalClasses.footer + '">\n   </div>\n </div>\n').replace(/(^|\n)\s*/g, '');

/*
 * Add modal + backdrop to DOM
 */
var init = function init(params) {
  // Clean up the old popup if it exists
  var c = getContainer();
  if (c) {
    c.parentNode.removeChild(c);
    removeClass([document.documentElement, document.body], [swalClasses['no-backdrop'], swalClasses['has-input'], swalClasses['toast-shown']]);
  }

  if (isNodeEnv()) {
    error('SweetAlert2 requires document to initialize');
    return;
  }

  var container = document.createElement('div');
  container.className = swalClasses.container;
  container.innerHTML = sweetHTML;

  var targetElement = typeof params.target === 'string' ? document.querySelector(params.target) : params.target;
  targetElement.appendChild(container);

  var popup = getPopup();
  var content = getContent();
  var input = getChildByClass(content, swalClasses.input);
  var file = getChildByClass(content, swalClasses.file);
  var range = content.querySelector('.' + swalClasses.range + ' input');
  var rangeOutput = content.querySelector('.' + swalClasses.range + ' output');
  var select = getChildByClass(content, swalClasses.select);
  var checkbox = content.querySelector('.' + swalClasses.checkbox + ' input');
  var textarea = getChildByClass(content, swalClasses.textarea);

  // a11y
  popup.setAttribute('role', params.toast ? 'alert' : 'dialog');
  popup.setAttribute('aria-live', params.toast ? 'polite' : 'assertive');
  if (!params.toast) {
    popup.setAttribute('aria-modal', 'true');
  }

  var oldInputVal = void 0; // IE11 workaround, see #1109 for details
  var resetValidationError = function resetValidationError(e) {
    if (Swal.isVisible() && oldInputVal !== e.target.value) {
      Swal.resetValidationError();
    }
    oldInputVal = e.target.value;
  };

  input.oninput = resetValidationError;
  file.onchange = resetValidationError;
  select.onchange = resetValidationError;
  checkbox.onchange = resetValidationError;
  textarea.oninput = resetValidationError;

  range.oninput = function (e) {
    resetValidationError(e);
    rangeOutput.value = range.value;
  };

  range.onchange = function (e) {
    resetValidationError(e);
    range.nextSibling.value = range.value;
  };

  return popup;
};

var parseHtmlToContainer = function parseHtmlToContainer(param, target) {
  if (!param) {
    return hide(target);
  }

  if ((typeof param === 'undefined' ? 'undefined' : _typeof(param)) === 'object') {
    target.innerHTML = '';
    if (0 in param) {
      for (var i = 0; i in param; i++) {
        target.appendChild(param[i].cloneNode(true));
      }
    } else {
      target.appendChild(param.cloneNode(true));
    }
  } else if (param) {
    target.innerHTML = param;
  } else {}
  show(target);
};

var animationEndEvent = function () {
  // Prevent run in Node env
  if (isNodeEnv()) {
    return false;
  }

  var testEl = document.createElement('div');
  var transEndEventNames = {
    'WebkitAnimation': 'webkitAnimationEnd',
    'OAnimation': 'oAnimationEnd oanimationend',
    'animation': 'animationend'
  };
  for (var i in transEndEventNames) {
    if (transEndEventNames.hasOwnProperty(i) && typeof testEl.style[i] !== 'undefined') {
      return transEndEventNames[i];
    }
  }

  return false;
}();

// Measure width of scrollbar
// https://github.com/twbs/bootstrap/blob/master/js/modal.js#L279-L286
var measureScrollbar = function measureScrollbar() {
  var supportsTouch = 'ontouchstart' in window || navigator.msMaxTouchPoints;
  if (supportsTouch) {
    return 0;
  }
  var scrollDiv = document.createElement('div');
  scrollDiv.style.width = '50px';
  scrollDiv.style.height = '50px';
  scrollDiv.style.overflow = 'scroll';
  document.body.appendChild(scrollDiv);
  var scrollbarWidth = scrollDiv.offsetWidth - scrollDiv.clientWidth;
  document.body.removeChild(scrollDiv);
  return scrollbarWidth;
};

var fixScrollbar = function fixScrollbar() {
  // for queues, do not do this more than once
  if (states.previousBodyPadding !== null) {
    return;
  }
  // if the body has overflow
  if (document.body.scrollHeight > window.innerHeight) {
    // add padding so the content doesn't shift after removal of scrollbar
    states.previousBodyPadding = parseInt(window.getComputedStyle(document.body).getPropertyValue('padding-right'));
    document.body.style.paddingRight = states.previousBodyPadding + measureScrollbar() + 'px';
  }
};

var undoScrollbar = function undoScrollbar() {
  if (states.previousBodyPadding !== null) {
    document.body.style.paddingRight = states.previousBodyPadding;
    states.previousBodyPadding = null;
  }
};

// Fix iOS scrolling http://stackoverflow.com/q/39626302/1331425
var iOSfix = function iOSfix() {
  var iOS = /iPad|iPhone|iPod/.test(navigator.userAgent) && !window.MSStream;
  if (iOS && !hasClass(document.body, swalClasses.iosfix)) {
    var offset = document.body.scrollTop;
    document.body.style.top = offset * -1 + 'px';
    addClass(document.body, swalClasses.iosfix);
  }
};

var undoIOSfix = function undoIOSfix() {
  if (hasClass(document.body, swalClasses.iosfix)) {
    var offset = parseInt(document.body.style.top, 10);
    removeClass(document.body, swalClasses.iosfix);
    document.body.style.top = '';
    document.body.scrollTop = offset * -1;
  }
};

var globalState = {};

// Restore previous active (focused) element
var restoreActiveElement = function restoreActiveElement() {
  var x = window.scrollX;
  var y = window.scrollY;
  globalState.restoreFocusTimeout = setTimeout(function () {
    if (globalState.previousActiveElement && globalState.previousActiveElement.focus) {
      globalState.previousActiveElement.focus();
      globalState.previousActiveElement = null;
    }
  }, 100); // issues/900
  if (typeof x !== 'undefined' && typeof y !== 'undefined') {
    // IE doesn't have scrollX/scrollY support
    window.scrollTo(x, y);
  }
};

/*
 * Global function to close sweetAlert
 */
var close = function close(onClose, onAfterClose) {
  var container = getContainer();
  var popup = getPopup();
  if (!popup) {
    return;
  }

  if (onClose !== null && typeof onClose === 'function') {
    onClose(popup);
  }

  removeClass(popup, swalClasses.show);
  addClass(popup, swalClasses.hide);

  var removePopupAndResetState = function removePopupAndResetState() {
    if (!isToast()) {
      restoreActiveElement();
      globalState.keydownTarget.removeEventListener('keydown', globalState.keydownHandler, { capture: globalState.keydownListenerCapture });
      globalState.keydownHandlerAdded = false;
    }

    if (container.parentNode) {
      container.parentNode.removeChild(container);
    }
    removeClass([document.documentElement, document.body], [swalClasses.shown, swalClasses['height-auto'], swalClasses['no-backdrop'], swalClasses['has-input'], swalClasses['toast-shown']]);

    if (isModal()) {
      undoScrollbar();
      undoIOSfix();
    }

    if (onAfterClose !== null && typeof onAfterClose === 'function') {
      setTimeout(function () {
        onAfterClose();
      });
    }
  };

  // If animation is supported, animate
  if (animationEndEvent && !hasClass(popup, swalClasses.noanimation)) {
    popup.addEventListener(animationEndEvent, function swalCloseEventFinished() {
      popup.removeEventListener(animationEndEvent, swalCloseEventFinished);
      if (hasClass(popup, swalClasses.hide)) {
        removePopupAndResetState();
      }
    });
  } else {
    // Otherwise, remove immediately
    removePopupAndResetState();
  }
};

/*
 * Global function to determine if swal2 popup is shown
 */
var isVisible$1 = function isVisible() {
  return !!getPopup();
};

/*
 * Global function to click 'Confirm' button
 */
var clickConfirm = function clickConfirm() {
  return getConfirmButton().click();
};

/*
 * Global function to click 'Cancel' button
 */
var clickCancel = function clickCancel() {
  return getCancelButton().click();
};

function fire() {
  var Swal = this;

  for (var _len = arguments.length, args = Array(_len), _key = 0; _key < _len; _key++) {
    args[_key] = arguments[_key];
  }

  return new (Function.prototype.bind.apply(Swal, [null].concat(args)))();
}

/**
 * Extends a Swal class making it able to be instantiated without the `new` keyword (and thus without `Swal.fire`)
 * @param ParentSwal
 * @returns {NoNewKeywordSwal}
 */
function withNoNewKeyword(ParentSwal) {
  var NoNewKeywordSwal = function NoNewKeywordSwal() {
    for (var _len = arguments.length, args = Array(_len), _key = 0; _key < _len; _key++) {
      args[_key] = arguments[_key];
    }

    if (!(this instanceof NoNewKeywordSwal)) {
      return new (Function.prototype.bind.apply(NoNewKeywordSwal, [null].concat(args)))();
    }
    Object.getPrototypeOf(NoNewKeywordSwal).apply(this, args);
  };
  NoNewKeywordSwal.prototype = _extends(Object.create(ParentSwal.prototype), { constructor: NoNewKeywordSwal });

  if (typeof Object.setPrototypeOf === 'function') {
    Object.setPrototypeOf(NoNewKeywordSwal, ParentSwal);
  } else {
    // Android 4.4
    // eslint-disable-next-line
    NoNewKeywordSwal.__proto__ = ParentSwal;
  }
  return NoNewKeywordSwal;
}

var defaultParams = {
  title: '',
  titleText: '',
  text: '',
  html: '',
  footer: '',
  type: null,
  toast: false,
  customClass: '',
  target: 'body',
  backdrop: true,
  animation: true,
  heightAuto: true,
  allowOutsideClick: true,
  allowEscapeKey: true,
  allowEnterKey: true,
  stopKeydownPropagation: true,
  keydownListenerCapture: false,
  showConfirmButton: true,
  showCancelButton: false,
  preConfirm: null,
  confirmButtonText: 'OK',
  confirmButtonAriaLabel: '',
  confirmButtonColor: null,
  confirmButtonClass: null,
  cancelButtonText: 'Cancel',
  cancelButtonAriaLabel: '',
  cancelButtonColor: null,
  cancelButtonClass: null,
  buttonsStyling: true,
  reverseButtons: false,
  focusConfirm: true,
  focusCancel: false,
  showCloseButton: false,
  closeButtonAriaLabel: 'Close this dialog',
  showLoaderOnConfirm: false,
  imageUrl: null,
  imageWidth: null,
  imageHeight: null,
  imageAlt: '',
  imageClass: null,
  timer: null,
  width: null,
  padding: null,
  background: null,
  input: null,
  inputPlaceholder: '',
  inputValue: '',
  inputOptions: {},
  inputAutoTrim: true,
  inputClass: null,
  inputAttributes: {},
  inputValidator: null,
  grow: false,
  position: 'center',
  progressSteps: [],
  currentProgressStep: null,
  progressStepsDistance: null,
  onBeforeOpen: null,
  onAfterClose: null,
  onOpen: null,
  onClose: null,
  useRejections: false,
  expectRejections: false
};

var deprecatedParams = ['useRejections', 'expectRejections'];

/**
 * Is valid parameter
 * @param {String} paramName
 */
var isValidParameter = function isValidParameter(paramName) {
  return defaultParams.hasOwnProperty(paramName) || paramName === 'extraParams';
};

/**
 * Is deprecated parameter
 * @param {String} paramName
 */
var isDeprecatedParameter = function isDeprecatedParameter(paramName) {
  return deprecatedParams.indexOf(paramName) !== -1;
};

/**
 * Show relevant warnings for given params
 *
 * @param params
 */
var showWarningsForParams = function showWarningsForParams(params) {
  for (var param in params) {
    if (!isValidParameter(param)) {
      warn('Unknown parameter "' + param + '"');
    }
    if (isDeprecatedParameter(param)) {
      warnOnce('The parameter "' + param + '" is deprecated and will be removed in the next major release.');
    }
  }
};

var deprecationWarning = '"setDefaults" & "resetDefaults" methods are deprecated in favor of "mixin" method and will be removed in the next major release. For new projects, use "mixin". For past projects already using "setDefaults", support will be provided through an additional package.';
var defaults$1 = {};

function withGlobalDefaults(ParentSwal) {
  var SwalWithGlobalDefaults = function (_ParentSwal) {
    inherits(SwalWithGlobalDefaults, _ParentSwal);

    function SwalWithGlobalDefaults() {
      classCallCheck(this, SwalWithGlobalDefaults);
      return possibleConstructorReturn(this, (SwalWithGlobalDefaults.__proto__ || Object.getPrototypeOf(SwalWithGlobalDefaults)).apply(this, arguments));
    }

    createClass(SwalWithGlobalDefaults, [{
      key: '_main',
      value: function _main(params) {
        return get(SwalWithGlobalDefaults.prototype.__proto__ || Object.getPrototypeOf(SwalWithGlobalDefaults.prototype), '_main', this).call(this, _extends({}, defaults$1, params));
      }
    }], [{
      key: 'setDefaults',
      value: function setDefaults(params) {
        warnOnce(deprecationWarning);
        if (!params || (typeof params === 'undefined' ? 'undefined' : _typeof(params)) !== 'object') {
          throw new TypeError('SweetAlert2: The argument for setDefaults() is required and has to be a object');
        }
        showWarningsForParams(params);
        // assign valid params from `params` to `defaults`
        Object.keys(params).forEach(function (param) {
          if (ParentSwal.isValidParameter(param)) {
            defaults$1[param] = params[param];
          }
        });
      }
    }, {
      key: 'resetDefaults',
      value: function resetDefaults() {
        warnOnce(deprecationWarning);
        defaults$1 = {};
      }
    }]);
    return SwalWithGlobalDefaults;
  }(ParentSwal);

  // Set default params if `window._swalDefaults` is an object


  if (typeof window !== 'undefined' && _typeof(window._swalDefaults) === 'object') {
    SwalWithGlobalDefaults.setDefaults(window._swalDefaults);
  }

  return SwalWithGlobalDefaults;
}

/**
 * Returns an extended version of `Swal` containing `params` as defaults.
 * Useful for reusing Swal configuration.
 *
 * For example:
 *
 * Before:
 * const textPromptOptions = { input: 'text', showCancelButton: true }
 * const {value: firstName} = await Swal({ ...textPromptOptions, title: 'What is your first name?' })
 * const {value: lastName} = await Swal({ ...textPromptOptions, title: 'What is your last name?' })
 *
 * After:
 * const TextPrompt = Swal.mixin({ input: 'text', showCancelButton: true })
 * const {value: firstName} = await TextPrompt('What is your first name?')
 * const {value: lastName} = await TextPrompt('What is your last name?')
 *
 * @param mixinParams
 */
function mixin(mixinParams) {
  var Swal = this;
  return withNoNewKeyword(function (_Swal) {
    inherits(MixinSwal, _Swal);

    function MixinSwal() {
      classCallCheck(this, MixinSwal);
      return possibleConstructorReturn(this, (MixinSwal.__proto__ || Object.getPrototypeOf(MixinSwal)).apply(this, arguments));
    }

    createClass(MixinSwal, [{
      key: '_main',
      value: function _main(params) {
        return get(MixinSwal.prototype.__proto__ || Object.getPrototypeOf(MixinSwal.prototype), '_main', this).call(this, _extends({}, mixinParams, params));
      }
    }]);
    return MixinSwal;
  }(Swal));
}

// private global state for the queue feature
var currentSteps = [];

/*
 * Global function for chaining sweetAlert popups
 */
var queue = function queue(steps) {
  var swal = this;
  currentSteps = steps;
  var resetQueue = function resetQueue() {
    currentSteps = [];
    document.body.removeAttribute('data-swal2-queue-step');
  };
  var queueResult = [];
  return new Promise(function (resolve, reject) {
    (function step(i, callback) {
      if (i < currentSteps.length) {
        document.body.setAttribute('data-swal2-queue-step', i);

        swal(currentSteps[i]).then(function (result) {
          if (typeof result.value !== 'undefined') {
            queueResult.push(result.value);
            step(i + 1, callback);
          } else {
            resetQueue();
            resolve({ dismiss: result.dismiss });
          }
        });
      } else {
        resetQueue();
        resolve({ value: queueResult });
      }
    })(0);
  });
};

/*
 * Global function for getting the index of current popup in queue
 */
var getQueueStep = function getQueueStep() {
  return document.body.getAttribute('data-swal2-queue-step');
};

/*
 * Global function for inserting a popup to the queue
 */
var insertQueueStep = function insertQueueStep(step, index) {
  if (index && index < currentSteps.length) {
    return currentSteps.splice(index, 0, step);
  }
  return currentSteps.push(step);
};

/*
 * Global function for deleting a popup from the queue
 */
var deleteQueueStep = function deleteQueueStep(index) {
  if (typeof currentSteps[index] !== 'undefined') {
    currentSteps.splice(index, 1);
  }
};

/**
 * Show spinner instead of Confirm button and disable Cancel button
 */
var showLoading = function showLoading() {
  var popup = getPopup();
  if (!popup) {
    Swal('');
  }
  popup = getPopup();
  var actions = getActions();
  var confirmButton = getConfirmButton();
  var cancelButton = getCancelButton();

  show(actions);
  show(confirmButton);
  addClass([popup, actions], swalClasses.loading);
  confirmButton.disabled = true;
  cancelButton.disabled = true;

  popup.setAttribute('data-loading', true);
  popup.setAttribute('aria-busy', true);
  popup.focus();
};

/**
 * Show spinner instead of Confirm button and disable Cancel button
 */
var getTimerLeft = function getTimerLeft() {
  return globalState.timeout && globalState.timeout.getTimerLeft();
};



var staticMethods = Object.freeze({
	isValidParameter: isValidParameter,
	isDeprecatedParameter: isDeprecatedParameter,
	argsToParams: argsToParams,
	adaptInputValidator: adaptInputValidator,
	close: close,
	closePopup: close,
	closeModal: close,
	closeToast: close,
	isVisible: isVisible$1,
	clickConfirm: clickConfirm,
	clickCancel: clickCancel,
	getPopup: getPopup,
	getTitle: getTitle,
	getContent: getContent,
	getImage: getImage,
	getButtonsWrapper: getButtonsWrapper,
	getActions: getActions,
	getConfirmButton: getConfirmButton,
	getCancelButton: getCancelButton,
	getFooter: getFooter,
	isLoading: isLoading,
	fire: fire,
	mixin: mixin,
	queue: queue,
	getQueueStep: getQueueStep,
	insertQueueStep: insertQueueStep,
	deleteQueueStep: deleteQueueStep,
	showLoading: showLoading,
	enableLoading: showLoading,
	getTimerLeft: getTimerLeft
});

// https://github.com/Riim/symbol-polyfill/blob/master/index.js

var _Symbol = typeof Symbol === 'function' ? Symbol : function () {
  var idCounter = 0;
  function _Symbol(key) {
    return '__' + key + '_' + Math.floor(Math.random() * 1e9) + '_' + ++idCounter + '__';
  }
  _Symbol.iterator = _Symbol('Symbol.iterator');
  return _Symbol;
}();

// WeakMap polyfill, needed for Android 4.4
// Related issue: https://github.com/sweetalert2/sweetalert2/issues/1071
// http://webreflection.blogspot.fi/2015/04/a-weakmap-polyfill-in-20-lines-of-code.html

var WeakMap$1 = typeof WeakMap === 'function' ? WeakMap : function (s, dP, hOP) {
  function WeakMap() {
    dP(this, s, { value: _Symbol('WeakMap') });
  }
  WeakMap.prototype = {
    'delete': function del(o) {
      delete o[this[s]];
    },
    get: function get(o) {
      return o[this[s]];
    },
    has: function has(o) {
      return hOP.call(o, this[s]);
    },
    set: function set(o, v) {
      dP(o, this[s], { configurable: true, value: v });
    }
  };
  return WeakMap;
}(_Symbol('WeakMap'), Object.defineProperty, {}.hasOwnProperty);

/**
 * This module containts `WeakMap`s for each effectively-"private  property" that a `swal` has.
 * For example, to set the private property "foo" of `this` to "bar", you can `privateProps.foo.set(this, 'bar')`
 * This is the approach that Babel will probably take to implement private methods/fields
 *   https://github.com/tc39/proposal-private-methods
 *   https://github.com/babel/babel/pull/7555
 * Once we have the changes from that PR in Babel, and our core class fits reasonable in *one module*
 *   then we can use that language feature.
 */

var privateProps = {
  promise: new WeakMap$1(),
  innerParams: new WeakMap$1(),
  domCache: new WeakMap$1()
};

/**
 * Show spinner instead of Confirm button and disable Cancel button
 */
function hideLoading() {
  var innerParams = privateProps.innerParams.get(this);
  var domCache = privateProps.domCache.get(this);
  if (!innerParams.showConfirmButton) {
    hide(domCache.confirmButton);
    if (!innerParams.showCancelButton) {
      hide(domCache.actions);
    }
  }
  removeClass([domCache.popup, domCache.actions], swalClasses.loading);
  domCache.popup.removeAttribute('aria-busy');
  domCache.popup.removeAttribute('data-loading');
  domCache.confirmButton.disabled = false;
  domCache.cancelButton.disabled = false;
}

// Get input element by specified type or, if type isn't specified, by params.input
function getInput(inputType) {
  var innerParams = privateProps.innerParams.get(this);
  var domCache = privateProps.domCache.get(this);
  inputType = inputType || innerParams.input;
  if (!inputType) {
    return null;
  }
  switch (inputType) {
    case 'select':
    case 'textarea':
    case 'file':
      return getChildByClass(domCache.content, swalClasses[inputType]);
    case 'checkbox':
      return domCache.popup.querySelector('.' + swalClasses.checkbox + ' input');
    case 'radio':
      return domCache.popup.querySelector('.' + swalClasses.radio + ' input:checked') || domCache.popup.querySelector('.' + swalClasses.radio + ' input:first-child');
    case 'range':
      return domCache.popup.querySelector('.' + swalClasses.range + ' input');
    default:
      return getChildByClass(domCache.content, swalClasses.input);
  }
}

function enableButtons() {
  var domCache = privateProps.domCache.get(this);
  domCache.confirmButton.disabled = false;
  domCache.cancelButton.disabled = false;
}

function disableButtons() {
  var domCache = privateProps.domCache.get(this);
  domCache.confirmButton.disabled = true;
  domCache.cancelButton.disabled = true;
}

function enableConfirmButton() {
  var domCache = privateProps.domCache.get(this);
  domCache.confirmButton.disabled = false;
}

function disableConfirmButton() {
  var domCache = privateProps.domCache.get(this);
  domCache.confirmButton.disabled = true;
}

function enableInput() {
  var input = this.getInput();
  if (!input) {
    return false;
  }
  if (input.type === 'radio') {
    var radiosContainer = input.parentNode.parentNode;
    var radios = radiosContainer.querySelectorAll('input');
    for (var i = 0; i < radios.length; i++) {
      radios[i].disabled = false;
    }
  } else {
    input.disabled = false;
  }
}

function disableInput() {
  var input = this.getInput();
  if (!input) {
    return false;
  }
  if (input && input.type === 'radio') {
    var radiosContainer = input.parentNode.parentNode;
    var radios = radiosContainer.querySelectorAll('input');
    for (var i = 0; i < radios.length; i++) {
      radios[i].disabled = true;
    }
  } else {
    input.disabled = true;
  }
}

// Show block with validation error
function showValidationError(error) {
  var domCache = privateProps.domCache.get(this);
  domCache.validationError.innerHTML = error;
  var popupComputedStyle = window.getComputedStyle(domCache.popup);
  domCache.validationError.style.marginLeft = '-' + popupComputedStyle.getPropertyValue('padding-left');
  domCache.validationError.style.marginRight = '-' + popupComputedStyle.getPropertyValue('padding-right');
  show(domCache.validationError);

  var input = this.getInput();
  if (input) {
    input.setAttribute('aria-invalid', true);
    input.setAttribute('aria-describedBy', swalClasses.validationerror);
    focusInput(input);
    addClass(input, swalClasses.inputerror);
  }
}

// Hide block with validation error
function resetValidationError() {
  var domCache = privateProps.domCache.get(this);
  if (domCache.validationError) {
    hide(domCache.validationError);
  }

  var input = this.getInput();
  if (input) {
    input.removeAttribute('aria-invalid');
    input.removeAttribute('aria-describedBy');
    removeClass(input, swalClasses.inputerror);
  }
}

var Timer = function Timer(callback, delay) {
  classCallCheck(this, Timer);

  var id, started, running;
  var remaining = delay;
  this.start = function () {
    running = true;
    started = new Date();
    id = setTimeout(callback, remaining);
  };
  this.stop = function () {
    running = false;
    clearTimeout(id);
    remaining -= new Date() - started;
  };
  this.getTimerLeft = function () {
    if (running) {
      this.stop();
      this.start();
    }
    return remaining;
  };
  this.getStateRunning = function () {
    return running;
  };
  this.start();
};

var defaultInputValidators = {
  email: function email(string, extraParams) {
    return (/^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9.-]+\.[a-zA-Z0-9-]{2,24}$/.test(string) ? Promise.resolve() : Promise.reject(extraParams && extraParams.validationMessage ? extraParams.validationMessage : 'Invalid email address')
    );
  },
  url: function url(string, extraParams) {
    // taken from https://stackoverflow.com/a/3809435/1331425
    return (/^https?:\/\/(www\.)?[-a-zA-Z0-9@:%._+~#=]{2,256}\.[a-z]{2,6}\b([-a-zA-Z0-9@:%_+.~#?&//=]*)$/.test(string) ? Promise.resolve() : Promise.reject(extraParams && extraParams.validationMessage ? extraParams.validationMessage : 'Invalid URL')
    );
  }
};

/**
 * Set type, text and actions on popup
 *
 * @param params
 * @returns {boolean}
 */
function setParameters(params) {
  // Use default `inputValidator` for supported input types if not provided
  if (!params.inputValidator) {
    Object.keys(defaultInputValidators).forEach(function (key) {
      if (params.input === key) {
        params.inputValidator = params.expectRejections ? defaultInputValidators[key] : Swal.adaptInputValidator(defaultInputValidators[key]);
      }
    });
  }

  // Determine if the custom target element is valid
  if (!params.target || typeof params.target === 'string' && !document.querySelector(params.target) || typeof params.target !== 'string' && !params.target.appendChild) {
    warn('Target parameter is not valid, defaulting to "body"');
    params.target = 'body';
  }

  var popup = void 0;
  var oldPopup = getPopup();
  var targetElement = typeof params.target === 'string' ? document.querySelector(params.target) : params.target;
  // If the model target has changed, refresh the popup
  if (oldPopup && targetElement && oldPopup.parentNode !== targetElement.parentNode) {
    popup = init(params);
  } else {
    popup = oldPopup || init(params);
  }

  // Set popup width
  if (params.width) {
    popup.style.width = typeof params.width === 'number' ? params.width + 'px' : params.width;
  }

  // Set popup padding
  if (params.padding) {
    popup.style.padding = typeof params.padding === 'number' ? params.padding + 'px' : params.padding;
  }

  // Set popup background
  if (params.background) {
    popup.style.background = params.background;
  }
  var popupBackgroundColor = window.getComputedStyle(popup).getPropertyValue('background-color');
  var successIconParts = popup.querySelectorAll('[class^=swal2-success-circular-line], .swal2-success-fix');
  for (var i = 0; i < successIconParts.length; i++) {
    successIconParts[i].style.backgroundColor = popupBackgroundColor;
  }

  var container = getContainer();
  var title = getTitle();
  var content = getContent().querySelector('#' + swalClasses.content);
  var actions = getActions();
  var confirmButton = getConfirmButton();
  var cancelButton = getCancelButton();
  var closeButton = getCloseButton();
  var footer = getFooter();

  // Title
  if (params.titleText) {
    title.innerText = params.titleText;
  } else if (params.title) {
    title.innerHTML = params.title.split('\n').join('<br />');
  }

  if (typeof params.backdrop === 'string') {
    getContainer().style.background = params.backdrop;
  } else if (!params.backdrop) {
    addClass([document.documentElement, document.body], swalClasses['no-backdrop']);
  }

  // Content as HTML
  if (params.html) {
    parseHtmlToContainer(params.html, content);

    // Content as plain text
  } else if (params.text) {
    content.textContent = params.text;
    show(content);
  } else {
    hide(content);
  }

  // Position
  if (params.position in swalClasses) {
    addClass(container, swalClasses[params.position]);
  } else {
    warn('The "position" parameter is not valid, defaulting to "center"');
    addClass(container, swalClasses.center);
  }

  // Grow
  if (params.grow && typeof params.grow === 'string') {
    var growClass = 'grow-' + params.grow;
    if (growClass in swalClasses) {
      addClass(container, swalClasses[growClass]);
    }
  }

  // Animation
  if (typeof params.animation === 'function') {
    params.animation = params.animation.call();
  }

  // Close button
  if (params.showCloseButton) {
    closeButton.setAttribute('aria-label', params.closeButtonAriaLabel);
    show(closeButton);
  } else {
    hide(closeButton);
  }

  // Default Class
  popup.className = swalClasses.popup;
  if (params.toast) {
    addClass([document.documentElement, document.body], swalClasses['toast-shown']);
    addClass(popup, swalClasses.toast);
  } else {
    addClass(popup, swalClasses.modal);
  }

  // Custom Class
  if (params.customClass) {
    addClass(popup, params.customClass);
  }

  // Progress steps
  var progressStepsContainer = getProgressSteps();
  var currentProgressStep = parseInt(params.currentProgressStep === null ? Swal.getQueueStep() : params.currentProgressStep, 10);
  if (params.progressSteps && params.progressSteps.length) {
    show(progressStepsContainer);
    empty(progressStepsContainer);
    if (currentProgressStep >= params.progressSteps.length) {
      warn('Invalid currentProgressStep parameter, it should be less than progressSteps.length ' + '(currentProgressStep like JS arrays starts from 0)');
    }
    params.progressSteps.forEach(function (step, index) {
      var circle = document.createElement('li');
      addClass(circle, swalClasses.progresscircle);
      circle.innerHTML = step;
      if (index === currentProgressStep) {
        addClass(circle, swalClasses.activeprogressstep);
      }
      progressStepsContainer.appendChild(circle);
      if (index !== params.progressSteps.length - 1) {
        var line = document.createElement('li');
        addClass(line, swalClasses.progressline);
        if (params.progressStepsDistance) {
          line.style.width = params.progressStepsDistance;
        }
        progressStepsContainer.appendChild(line);
      }
    });
  } else {
    hide(progressStepsContainer);
  }

  // Icon
  var icons = getIcons();
  for (var _i = 0; _i < icons.length; _i++) {
    hide(icons[_i]);
  }
  if (params.type) {
    var validType = false;
    for (var iconType in iconTypes) {
      if (params.type === iconType) {
        validType = true;
        break;
      }
    }
    if (!validType) {
      error('Unknown alert type: ' + params.type);
      return false;
    }
    var icon = popup.querySelector('.' + swalClasses.icon + '.' + iconTypes[params.type]);
    show(icon);

    // Animate icon
    if (params.animation) {
      addClass(icon, 'swal2-animate-' + params.type + '-icon');
    }
  }

  // Custom image
  var image = getImage();
  if (params.imageUrl) {
    image.setAttribute('src', params.imageUrl);
    image.setAttribute('alt', params.imageAlt);
    show(image);

    if (params.imageWidth) {
      image.setAttribute('width', params.imageWidth);
    } else {
      image.removeAttribute('width');
    }

    if (params.imageHeight) {
      image.setAttribute('height', params.imageHeight);
    } else {
      image.removeAttribute('height');
    }

    image.className = swalClasses.image;
    if (params.imageClass) {
      addClass(image, params.imageClass);
    }
  } else {
    hide(image);
  }

  // Cancel button
  if (params.showCancelButton) {
    cancelButton.style.display = 'inline-block';
  } else {
    hide(cancelButton);
  }

  // Confirm button
  if (params.showConfirmButton) {
    removeStyleProperty(confirmButton, 'display');
  } else {
    hide(confirmButton);
  }

  // Actions (buttons) wrapper
  if (!params.showConfirmButton && !params.showCancelButton) {
    hide(actions);
  } else {
    show(actions);
  }

  // Edit text on confirm and cancel buttons
  confirmButton.innerHTML = params.confirmButtonText;
  cancelButton.innerHTML = params.cancelButtonText;

  // ARIA labels for confirm and cancel buttons
  confirmButton.setAttribute('aria-label', params.confirmButtonAriaLabel);
  cancelButton.setAttribute('aria-label', params.cancelButtonAriaLabel);

  // Add buttons custom classes
  confirmButton.className = swalClasses.confirm;
  addClass(confirmButton, params.confirmButtonClass);
  cancelButton.className = swalClasses.cancel;
  addClass(cancelButton, params.cancelButtonClass);

  // Buttons styling
  if (params.buttonsStyling) {
    addClass([confirmButton, cancelButton], swalClasses.styled);

    // Buttons background colors
    if (params.confirmButtonColor) {
      confirmButton.style.backgroundColor = params.confirmButtonColor;
    }
    if (params.cancelButtonColor) {
      cancelButton.style.backgroundColor = params.cancelButtonColor;
    }

    // Loading state
    var confirmButtonBackgroundColor = window.getComputedStyle(confirmButton).getPropertyValue('background-color');
    confirmButton.style.borderLeftColor = confirmButtonBackgroundColor;
    confirmButton.style.borderRightColor = confirmButtonBackgroundColor;
  } else {
    removeClass([confirmButton, cancelButton], swalClasses.styled);

    confirmButton.style.backgroundColor = confirmButton.style.borderLeftColor = confirmButton.style.borderRightColor = '';
    cancelButton.style.backgroundColor = cancelButton.style.borderLeftColor = cancelButton.style.borderRightColor = '';
  }

  // Footer
  parseHtmlToContainer(params.footer, footer);

  // CSS animation
  if (params.animation === true) {
    removeClass(popup, swalClasses.noanimation);
  } else {
    addClass(popup, swalClasses.noanimation);
  }

  // showLoaderOnConfirm && preConfirm
  if (params.showLoaderOnConfirm && !params.preConfirm) {
    warn('showLoaderOnConfirm is set to true, but preConfirm is not defined.\n' + 'showLoaderOnConfirm should be used together with preConfirm, see usage example:\n' + 'https://sweetalert2.github.io/#ajax-request');
  }
}

/**
 * Open popup, add necessary classes and styles, fix scrollbar
 *
 * @param {Array} params
 */
var openPopup = function openPopup(params) {
  var container = getContainer();
  var popup = getPopup();

  if (params.onBeforeOpen !== null && typeof params.onBeforeOpen === 'function') {
    params.onBeforeOpen(popup);
  }

  if (params.animation) {
    addClass(popup, swalClasses.show);
    addClass(container, swalClasses.fade);
    removeClass(popup, swalClasses.hide);
  } else {
    removeClass(popup, swalClasses.fade);
  }
  show(popup);

  // scrolling is 'hidden' until animation is done, after that 'auto'
  container.style.overflowY = 'hidden';
  if (animationEndEvent && !hasClass(popup, swalClasses.noanimation)) {
    popup.addEventListener(animationEndEvent, function swalCloseEventFinished() {
      popup.removeEventListener(animationEndEvent, swalCloseEventFinished);
      container.style.overflowY = 'auto';
    });
  } else {
    container.style.overflowY = 'auto';
  }

  addClass([document.documentElement, document.body, container], swalClasses.shown);
  if (params.heightAuto && params.backdrop && !params.toast) {
    addClass([document.documentElement, document.body], swalClasses['height-auto']);
  }

  if (isModal()) {
    fixScrollbar();
    iOSfix();
  }
  if (!globalState.previousActiveElement) {
    globalState.previousActiveElement = document.activeElement;
  }
  if (params.onOpen !== null && typeof params.onOpen === 'function') {
    setTimeout(function () {
      params.onOpen(popup);
    });
  }
};

function _main(userParams) {
  var _this = this;

  showWarningsForParams(userParams);

  var innerParams = _extends({}, defaultParams, userParams);
  setParameters(innerParams);
  Object.freeze(innerParams);
  privateProps.innerParams.set(this, innerParams);

  // clear the previous timer
  if (globalState.timeout) {
    globalState.timeout.stop();
    delete globalState.timeout;
  }

  // clear the restore focus timeout
  clearTimeout(globalState.restoreFocusTimeout);

  var domCache = {
    popup: getPopup(),
    container: getContainer(),
    content: getContent(),
    actions: getActions(),
    confirmButton: getConfirmButton(),
    cancelButton: getCancelButton(),
    closeButton: getCloseButton(),
    validationError: getValidationError(),
    progressSteps: getProgressSteps()
  };
  privateProps.domCache.set(this, domCache);

  var constructor = this.constructor;

  return new Promise(function (resolve, reject) {
    // functions to handle all resolving/rejecting/settling
    var succeedWith = function succeedWith(value) {
      constructor.closePopup(innerParams.onClose, innerParams.onAfterClose); // TODO: make closePopup an *instance* method
      if (innerParams.useRejections) {
        resolve(value);
      } else {
        resolve({ value: value });
      }
    };
    var dismissWith = function dismissWith(dismiss) {
      constructor.closePopup(innerParams.onClose, innerParams.onAfterClose);
      if (innerParams.useRejections) {
        reject(dismiss);
      } else {
        resolve({ dismiss: dismiss });
      }
    };
    var errorWith = function errorWith(error$$1) {
      constructor.closePopup(innerParams.onClose, innerParams.onAfterClose);
      reject(error$$1);
    };

    // Close on timer
    if (innerParams.timer) {
      globalState.timeout = new Timer(function () {
        dismissWith('timer');
        delete globalState.timeout;
      }, innerParams.timer);
    }

    // Get the value of the popup input
    var getInputValue = function getInputValue() {
      var input = _this.getInput();
      if (!input) {
        return null;
      }
      switch (innerParams.input) {
        case 'checkbox':
          return input.checked ? 1 : 0;
        case 'radio':
          return input.checked ? input.value : null;
        case 'file':
          return input.files.length ? input.files[0] : null;
        default:
          return innerParams.inputAutoTrim ? input.value.trim() : input.value;
      }
    };

    // input autofocus
    if (innerParams.input) {
      setTimeout(function () {
        var input = _this.getInput();
        if (input) {
          focusInput(input);
        }
      }, 0);
    }

    var confirm = function confirm(value) {
      if (innerParams.showLoaderOnConfirm) {
        constructor.showLoading(); // TODO: make showLoading an *instance* method
      }

      if (innerParams.preConfirm) {
        _this.resetValidationError();
        var preConfirmPromise = Promise.resolve().then(function () {
          return innerParams.preConfirm(value, innerParams.extraParams);
        });
        if (innerParams.expectRejections) {
          preConfirmPromise.then(function (preConfirmValue) {
            return succeedWith(preConfirmValue || value);
          }, function (validationError) {
            _this.hideLoading();
            if (validationError) {
              _this.showValidationError(validationError);
            }
          });
        } else {
          preConfirmPromise.then(function (preConfirmValue) {
            if (isVisible(domCache.validationError) || preConfirmValue === false) {
              _this.hideLoading();
            } else {
              succeedWith(preConfirmValue || value);
            }
          }, function (error$$1) {
            return errorWith(error$$1);
          });
        }
      } else {
        succeedWith(value);
      }
    };

    // Mouse interactions
    var onButtonEvent = function onButtonEvent(event) {
      var e = event || window.event;
      var target = e.target || e.srcElement;
      var confirmButton = domCache.confirmButton,
          cancelButton = domCache.cancelButton;

      var targetedConfirm = confirmButton && (confirmButton === target || confirmButton.contains(target));
      var targetedCancel = cancelButton && (cancelButton === target || cancelButton.contains(target));

      switch (e.type) {
        case 'click':
          // Clicked 'confirm'
          if (targetedConfirm && constructor.isVisible()) {
            _this.disableButtons();
            if (innerParams.input) {
              var inputValue = getInputValue();

              if (innerParams.inputValidator) {
                _this.disableInput();
                var validationPromise = Promise.resolve().then(function () {
                  return innerParams.inputValidator(inputValue, innerParams.extraParams);
                });
                if (innerParams.expectRejections) {
                  validationPromise.then(function () {
                    _this.enableButtons();
                    _this.enableInput();
                    confirm(inputValue);
                  }, function (validationError) {
                    _this.enableButtons();
                    _this.enableInput();
                    if (validationError) {
                      _this.showValidationError(validationError);
                    }
                  });
                } else {
                  validationPromise.then(function (validationError) {
                    _this.enableButtons();
                    _this.enableInput();
                    if (validationError) {
                      _this.showValidationError(validationError);
                    } else {
                      confirm(inputValue);
                    }
                  }, function (error$$1) {
                    return errorWith(error$$1);
                  });
                }
              } else {
                confirm(inputValue);
              }
            } else {
              confirm(true);
            }

            // Clicked 'cancel'
          } else if (targetedCancel && constructor.isVisible()) {
            _this.disableButtons();
            dismissWith(constructor.DismissReason.cancel);
          }
          break;
        default:
      }
    };

    var buttons = domCache.popup.querySelectorAll('button');
    for (var i = 0; i < buttons.length; i++) {
      buttons[i].onclick = onButtonEvent;
      buttons[i].onmouseover = onButtonEvent;
      buttons[i].onmouseout = onButtonEvent;
      buttons[i].onmousedown = onButtonEvent;
    }

    // Closing popup by close button
    domCache.closeButton.onclick = function () {
      dismissWith(constructor.DismissReason.close);
    };

    if (innerParams.toast) {
      // Closing popup by internal click
      domCache.popup.onclick = function (e) {
        if (innerParams.showConfirmButton || innerParams.showCancelButton || innerParams.showCloseButton || innerParams.input) {
          return;
        }
        constructor.closePopup(innerParams.onClose, innerParams.onAfterClose);
        dismissWith(constructor.DismissReason.close);
      };
    } else {
      var ignoreOutsideClick = false;

      // Ignore click events that had mousedown on the popup but mouseup on the container
      // This can happen when the user drags a slider
      domCache.popup.onmousedown = function () {
        domCache.container.onmouseup = function (e) {
          domCache.container.onmouseup = undefined;
          // We only check if the mouseup target is the container because usually it doesn't
          // have any other direct children aside of the popup
          if (e.target === domCache.container) {
            ignoreOutsideClick = true;
          }
        };
      };

      // Ignore click events that had mousedown on the container but mouseup on the popup
      domCache.container.onmousedown = function () {
        domCache.popup.onmouseup = function (e) {
          domCache.popup.onmouseup = undefined;
          // We also need to check if the mouseup target is a child of the popup
          if (e.target === domCache.popup || domCache.popup.contains(e.target)) {
            ignoreOutsideClick = true;
          }
        };
      };

      domCache.container.onclick = function (e) {
        if (ignoreOutsideClick) {
          ignoreOutsideClick = false;
          return;
        }
        if (e.target !== domCache.container) {
          return;
        }
        if (callIfFunction(innerParams.allowOutsideClick)) {
          dismissWith(constructor.DismissReason.backdrop);
        }
      };
    }

    // Reverse buttons (Confirm on the right side)
    if (innerParams.reverseButtons) {
      domCache.confirmButton.parentNode.insertBefore(domCache.cancelButton, domCache.confirmButton);
    } else {
      domCache.confirmButton.parentNode.insertBefore(domCache.confirmButton, domCache.cancelButton);
    }

    // Focus handling
    var setFocus = function setFocus(index, increment) {
      var focusableElements = getFocusableElements(innerParams.focusCancel);
      // search for visible elements and select the next possible match
      for (var _i = 0; _i < focusableElements.length; _i++) {
        index = index + increment;

        // rollover to first item
        if (index === focusableElements.length) {
          index = 0;

          // go to last item
        } else if (index === -1) {
          index = focusableElements.length - 1;
        }

        // determine if element is visible
        var el = focusableElements[index];
        if (isVisible(el)) {
          return el.focus();
        }
      }
      // no visible focusable elements, focus the popup
      domCache.popup.focus();
    };

    var keydownHandler = function keydownHandler(e, innerParams) {
      if (innerParams.stopKeydownPropagation) {
        e.stopPropagation();
      }

      var arrowKeys = ['ArrowLeft', 'ArrowRight', 'ArrowUp', 'ArrowDown', 'Left', 'Right', 'Up', 'Down' // IE11
      ];

      if (e.key === 'Enter' && !e.isComposing) {
        if (e.target && _this.getInput() && e.target.outerHTML === _this.getInput().outerHTML) {
          if (['textarea', 'file'].indexOf(innerParams.input) !== -1) {
            return; // do not submit
          }

          constructor.clickConfirm();
          e.preventDefault();
        }

        // TAB
      } else if (e.key === 'Tab') {
        var targetElement = e.target || e.srcElement;

        var focusableElements = getFocusableElements(innerParams.focusCancel);
        var btnIndex = -1; // Find the button - note, this is a nodelist, not an array.
        for (var _i2 = 0; _i2 < focusableElements.length; _i2++) {
          if (targetElement === focusableElements[_i2]) {
            btnIndex = _i2;
            break;
          }
        }

        if (!e.shiftKey) {
          // Cycle to the next button
          setFocus(btnIndex, 1);
        } else {
          // Cycle to the prev button
          setFocus(btnIndex, -1);
        }
        e.stopPropagation();
        e.preventDefault();

        // ARROWS - switch focus between buttons
      } else if (arrowKeys.indexOf(e.key) !== -1) {
        // focus Cancel button if Confirm button is currently focused
        if (document.activeElement === domCache.confirmButton && isVisible(domCache.cancelButton)) {
          domCache.cancelButton.focus();
          // and vice versa
        } else if (document.activeElement === domCache.cancelButton && isVisible(domCache.confirmButton)) {
          domCache.confirmButton.focus();
        }

        // ESC
      } else if ((e.key === 'Escape' || e.key === 'Esc') && callIfFunction(innerParams.allowEscapeKey) === true) {
        dismissWith(constructor.DismissReason.esc);
      }
    };

    if (globalState.keydownHandlerAdded) {
      globalState.keydownTarget.removeEventListener('keydown', globalState.keydownHandler, { capture: globalState.keydownListenerCapture });
      globalState.keydownHandlerAdded = false;
    }

    if (!innerParams.toast) {
      globalState.keydownHandler = function (e) {
        return keydownHandler(e, innerParams);
      };
      globalState.keydownTarget = innerParams.keydownListenerCapture ? window : domCache.popup;
      globalState.keydownListenerCapture = innerParams.keydownListenerCapture;
      globalState.keydownTarget.addEventListener('keydown', globalState.keydownHandler, { capture: globalState.keydownListenerCapture });
      globalState.keydownHandlerAdded = true;
    }

    _this.enableButtons();
    _this.hideLoading();
    _this.resetValidationError();

    if (innerParams.input) {
      addClass(document.body, swalClasses['has-input']);
    }

    // inputs
    var inputTypes = ['input', 'file', 'range', 'select', 'radio', 'checkbox', 'textarea'];
    var input = void 0;
    for (var _i3 = 0; _i3 < inputTypes.length; _i3++) {
      var inputClass = swalClasses[inputTypes[_i3]];
      var inputContainer = getChildByClass(domCache.content, inputClass);
      input = _this.getInput(inputTypes[_i3]);

      // set attributes
      if (input) {
        for (var j in input.attributes) {
          if (input.attributes.hasOwnProperty(j)) {
            var attrName = input.attributes[j].name;
            if (attrName !== 'type' && attrName !== 'value') {
              input.removeAttribute(attrName);
            }
          }
        }
        for (var attr in innerParams.inputAttributes) {
          input.setAttribute(attr, innerParams.inputAttributes[attr]);
        }
      }

      // set class
      inputContainer.className = inputClass;
      if (innerParams.inputClass) {
        addClass(inputContainer, innerParams.inputClass);
      }

      hide(inputContainer);
    }

    var populateInputOptions = void 0;
    switch (innerParams.input) {
      case 'text':
      case 'email':
      case 'password':
      case 'number':
      case 'tel':
      case 'url':
        input = getChildByClass(domCache.content, swalClasses.input);
        input.value = innerParams.inputValue;
        input.placeholder = innerParams.inputPlaceholder;
        input.type = innerParams.input;
        show(input);
        break;
      case 'file':
        input = getChildByClass(domCache.content, swalClasses.file);
        input.placeholder = innerParams.inputPlaceholder;
        input.type = innerParams.input;
        show(input);
        break;
      case 'range':
        var range = getChildByClass(domCache.content, swalClasses.range);
        var rangeInput = range.querySelector('input');
        var rangeOutput = range.querySelector('output');
        rangeInput.value = innerParams.inputValue;
        rangeInput.type = innerParams.input;
        rangeOutput.value = innerParams.inputValue;
        show(range);
        break;
      case 'select':
        var select = getChildByClass(domCache.content, swalClasses.select);
        select.innerHTML = '';
        if (innerParams.inputPlaceholder) {
          var placeholder = document.createElement('option');
          placeholder.innerHTML = innerParams.inputPlaceholder;
          placeholder.value = '';
          placeholder.disabled = true;
          placeholder.selected = true;
          select.appendChild(placeholder);
        }
        populateInputOptions = function populateInputOptions(inputOptions) {
          inputOptions.forEach(function (_ref) {
            var _ref2 = slicedToArray(_ref, 2),
                optionValue = _ref2[0],
                optionLabel = _ref2[1];

            var option = document.createElement('option');
            option.value = optionValue;
            option.innerHTML = optionLabel;
            if (innerParams.inputValue.toString() === optionValue.toString()) {
              option.selected = true;
            }
            select.appendChild(option);
          });
          show(select);
          select.focus();
        };
        break;
      case 'radio':
        var radio = getChildByClass(domCache.content, swalClasses.radio);
        radio.innerHTML = '';
        populateInputOptions = function populateInputOptions(inputOptions) {
          inputOptions.forEach(function (_ref3) {
            var _ref4 = slicedToArray(_ref3, 2),
                radioValue = _ref4[0],
                radioLabel = _ref4[1];

            var radioInput = document.createElement('input');
            var radioLabelElement = document.createElement('label');
            radioInput.type = 'radio';
            radioInput.name = swalClasses.radio;
            radioInput.value = radioValue;
            if (innerParams.inputValue.toString() === radioValue.toString()) {
              radioInput.checked = true;
            }
            radioLabelElement.innerHTML = radioLabel;
            radioLabelElement.insertBefore(radioInput, radioLabelElement.firstChild);
            radio.appendChild(radioLabelElement);
          });
          show(radio);
          var radios = radio.querySelectorAll('input');
          if (radios.length) {
            radios[0].focus();
          }
        };
        break;
      case 'checkbox':
        var checkbox = getChildByClass(domCache.content, swalClasses.checkbox);
        var checkboxInput = _this.getInput('checkbox');
        checkboxInput.type = 'checkbox';
        checkboxInput.value = 1;
        checkboxInput.id = swalClasses.checkbox;
        checkboxInput.checked = Boolean(innerParams.inputValue);
        var label = checkbox.getElementsByTagName('span');
        if (label.length) {
          checkbox.removeChild(label[0]);
        }
        label = document.createElement('span');
        label.innerHTML = innerParams.inputPlaceholder;
        checkbox.appendChild(label);
        show(checkbox);
        break;
      case 'textarea':
        var textarea = getChildByClass(domCache.content, swalClasses.textarea);
        textarea.value = innerParams.inputValue;
        textarea.placeholder = innerParams.inputPlaceholder;
        show(textarea);
        break;
      case null:
        break;
      default:
        error('Unexpected type of input! Expected "text", "email", "password", "number", "tel", "select", "radio", "checkbox", "textarea", "file" or "url", got "' + innerParams.input + '"');
        break;
    }

    if (innerParams.input === 'select' || innerParams.input === 'radio') {
      var processInputOptions = function processInputOptions(inputOptions) {
        return populateInputOptions(formatInputOptions(inputOptions));
      };
      if (isThenable(innerParams.inputOptions)) {
        constructor.showLoading();
        innerParams.inputOptions.then(function (inputOptions) {
          _this.hideLoading();
          processInputOptions(inputOptions);
        });
      } else if (_typeof(innerParams.inputOptions) === 'object') {
        processInputOptions(innerParams.inputOptions);
      } else {
        error('Unexpected type of inputOptions! Expected object, Map or Promise, got ' + _typeof(innerParams.inputOptions));
      }
    } else if (['text', 'email', 'number', 'tel', 'textarea'].indexOf(innerParams.input) !== -1 && isThenable(innerParams.inputValue)) {
      constructor.showLoading();
      hide(input);
      innerParams.inputValue.then(function (inputValue) {
        input.value = innerParams.input === 'number' ? parseFloat(inputValue) || 0 : inputValue + '';
        show(input);
        _this.hideLoading();
      }).catch(function (err) {
        error('Error in inputValue promise: ' + err);
        input.value = '';
        show(input);
        _this.hideLoading();
      });
    }

    openPopup(innerParams);

    if (!innerParams.toast) {
      if (!callIfFunction(innerParams.allowEnterKey)) {
        if (document.activeElement) {
          document.activeElement.blur();
        }
      } else if (innerParams.focusCancel && isVisible(domCache.cancelButton)) {
        domCache.cancelButton.focus();
      } else if (innerParams.focusConfirm && isVisible(domCache.confirmButton)) {
        domCache.confirmButton.focus();
      } else {
        setFocus(-1, 1);
      }
    }

    // fix scroll
    domCache.container.scrollTop = 0;
  });
}



var instanceMethods = Object.freeze({
	hideLoading: hideLoading,
	disableLoading: hideLoading,
	getInput: getInput,
	enableButtons: enableButtons,
	disableButtons: disableButtons,
	enableConfirmButton: enableConfirmButton,
	disableConfirmButton: disableConfirmButton,
	enableInput: enableInput,
	disableInput: disableInput,
	showValidationError: showValidationError,
	resetValidationError: resetValidationError,
	_main: _main
});

var currentInstance = void 0;

// SweetAlert constructor
function SweetAlert() {
  // Prevent run in Node env
  if (typeof window === 'undefined') {
    return;
  }

  // Check for the existence of Promise
  if (typeof Promise === 'undefined') {
    error('This package requires a Promise library, please include a shim to enable it in this browser (See: https://github.com/sweetalert2/sweetalert2/wiki/Migration-from-SweetAlert-to-SweetAlert2#1-ie-support)');
  }

  for (var _len = arguments.length, args = Array(_len), _key = 0; _key < _len; _key++) {
    args[_key] = arguments[_key];
  }

  if (typeof args[0] === 'undefined') {
    error('SweetAlert2 expects at least 1 attribute!');
    return false;
  }

  currentInstance = this;

  var outerParams = Object.freeze(this.constructor.argsToParams(args));

  Object.defineProperties(this, {
    params: {
      value: outerParams,
      writable: false,
      enumerable: true
    }
  });

  var promise = this._main(this.params);
  privateProps.promise.set(this, promise);
}

// `catch` cannot be the name of a module export, so we define our thenable methods here instead
SweetAlert.prototype.then = function (onFulfilled, onRejected) {
  var promise = privateProps.promise.get(this);
  return promise.then(onFulfilled, onRejected);
};
SweetAlert.prototype.catch = function (onRejected) {
  var promise = privateProps.promise.get(this);
  return promise.catch(onRejected);
};
SweetAlert.prototype.finally = function (onFinally) {
  var promise = privateProps.promise.get(this);
  return promise.finally(onFinally);
};

// Assign instance methods from src/instanceMethods/*.js to prototype
_extends(SweetAlert.prototype, instanceMethods);

// Assign static methods from src/staticMethods/*.js to constructor
_extends(SweetAlert, staticMethods);

// Proxy to instance methods to constructor, for now, for backwards compatibility
Object.keys(instanceMethods).forEach(function (key) {
  SweetAlert[key] = function () {
    if (currentInstance) {
      var _currentInstance;

      return (_currentInstance = currentInstance)[key].apply(_currentInstance, arguments);
    }
  };
});

SweetAlert.DismissReason = DismissReason;

SweetAlert.noop = function () {};

SweetAlert.version = version;

var Swal = withNoNewKeyword(withGlobalDefaults(SweetAlert));
Swal.default = Swal;

return Swal;

})));
if (typeof window !== 'undefined' && window.Sweetalert2){  window.swal = window.sweetAlert = window.Swal = window.SweetAlert = window.Sweetalert2}

"undefined"!=typeof document&&function(e,t){var n=e.createElement("style");if(e.getElementsByTagName("head")[0].appendChild(n),n.styleSheet)n.styleSheet.disabled||(n.styleSheet.cssText=t);else try{n.innerHTML=t}catch(e){n.innerText=t}}(document,"@-webkit-keyframes swal2-show {\n" +
"  0% {\n" +
"    -webkit-transform: scale(0.7);\n" +
"            transform: scale(0.7); }\n" +
"  45% {\n" +
"    -webkit-transform: scale(1.05);\n" +
"            transform: scale(1.05); }\n" +
"  80% {\n" +
"    -webkit-transform: scale(0.95);\n" +
"            transform: scale(0.95); }\n" +
"  100% {\n" +
"    -webkit-transform: scale(1);\n" +
"            transform: scale(1); } }\n" +
"\n" +
"@keyframes swal2-show {\n" +
"  0% {\n" +
"    -webkit-transform: scale(0.7);\n" +
"            transform: scale(0.7); }\n" +
"  45% {\n" +
"    -webkit-transform: scale(1.05);\n" +
"            transform: scale(1.05); }\n" +
"  80% {\n" +
"    -webkit-transform: scale(0.95);\n" +
"            transform: scale(0.95); }\n" +
"  100% {\n" +
"    -webkit-transform: scale(1);\n" +
"            transform: scale(1); } }\n" +
"\n" +
"@-webkit-keyframes swal2-hide {\n" +
"  0% {\n" +
"    -webkit-transform: scale(1);\n" +
"            transform: scale(1);\n" +
"    opacity: 1; }\n" +
"  100% {\n" +
"    -webkit-transform: scale(0.5);\n" +
"            transform: scale(0.5);\n" +
"    opacity: 0; } }\n" +
"\n" +
"@keyframes swal2-hide {\n" +
"  0% {\n" +
"    -webkit-transform: scale(1);\n" +
"            transform: scale(1);\n" +
"    opacity: 1; }\n" +
"  100% {\n" +
"    -webkit-transform: scale(0.5);\n" +
"            transform: scale(0.5);\n" +
"    opacity: 0; } }\n" +
"\n" +
"@-webkit-keyframes swal2-animate-success-line-tip {\n" +
"  0% {\n" +
"    top: 1.1875em;\n" +
"    left: .0625em;\n" +
"    width: 0; }\n" +
"  54% {\n" +
"    top: 1.0625em;\n" +
"    left: .125em;\n" +
"    width: 0; }\n" +
"  70% {\n" +
"    top: 2.1875em;\n" +
"    left: -.375em;\n" +
"    width: 3.125em; }\n" +
"  84% {\n" +
"    top: 3em;\n" +
"    left: 1.3125em;\n" +
"    width: 1.0625em; }\n" +
"  100% {\n" +
"    top: 2.8125em;\n" +
"    left: .875em;\n" +
"    width: 1.5625em; } }\n" +
"\n" +
"@keyframes swal2-animate-success-line-tip {\n" +
"  0% {\n" +
"    top: 1.1875em;\n" +
"    left: .0625em;\n" +
"    width: 0; }\n" +
"  54% {\n" +
"    top: 1.0625em;\n" +
"    left: .125em;\n" +
"    width: 0; }\n" +
"  70% {\n" +
"    top: 2.1875em;\n" +
"    left: -.375em;\n" +
"    width: 3.125em; }\n" +
"  84% {\n" +
"    top: 3em;\n" +
"    left: 1.3125em;\n" +
"    width: 1.0625em; }\n" +
"  100% {\n" +
"    top: 2.8125em;\n" +
"    left: .875em;\n" +
"    width: 1.5625em; } }\n" +
"\n" +
"@-webkit-keyframes swal2-animate-success-line-long {\n" +
"  0% {\n" +
"    top: 3.375em;\n" +
"    right: 2.875em;\n" +
"    width: 0; }\n" +
"  65% {\n" +
"    top: 3.375em;\n" +
"    right: 2.875em;\n" +
"    width: 0; }\n" +
"  84% {\n" +
"    top: 2.1875em;\n" +
"    right: 0;\n" +
"    width: 3.4375em; }\n" +
"  100% {\n" +
"    top: 2.375em;\n" +
"    right: .5em;\n" +
"    width: 2.9375em; } }\n" +
"\n" +
"@keyframes swal2-animate-success-line-long {\n" +
"  0% {\n" +
"    top: 3.375em;\n" +
"    right: 2.875em;\n" +
"    width: 0; }\n" +
"  65% {\n" +
"    top: 3.375em;\n" +
"    right: 2.875em;\n" +
"    width: 0; }\n" +
"  84% {\n" +
"    top: 2.1875em;\n" +
"    right: 0;\n" +
"    width: 3.4375em; }\n" +
"  100% {\n" +
"    top: 2.375em;\n" +
"    right: .5em;\n" +
"    width: 2.9375em; } }\n" +
"\n" +
"@-webkit-keyframes swal2-rotate-success-circular-line {\n" +
"  0% {\n" +
"    -webkit-transform: rotate(-45deg);\n" +
"            transform: rotate(-45deg); }\n" +
"  5% {\n" +
"    -webkit-transform: rotate(-45deg);\n" +
"            transform: rotate(-45deg); }\n" +
"  12% {\n" +
"    -webkit-transform: rotate(-405deg);\n" +
"            transform: rotate(-405deg); }\n" +
"  100% {\n" +
"    -webkit-transform: rotate(-405deg);\n" +
"            transform: rotate(-405deg); } }\n" +
"\n" +
"@keyframes swal2-rotate-success-circular-line {\n" +
"  0% {\n" +
"    -webkit-transform: rotate(-45deg);\n" +
"            transform: rotate(-45deg); }\n" +
"  5% {\n" +
"    -webkit-transform: rotate(-45deg);\n" +
"            transform: rotate(-45deg); }\n" +
"  12% {\n" +
"    -webkit-transform: rotate(-405deg);\n" +
"            transform: rotate(-405deg); }\n" +
"  100% {\n" +
"    -webkit-transform: rotate(-405deg);\n" +
"            transform: rotate(-405deg); } }\n" +
"\n" +
"@-webkit-keyframes swal2-animate-error-x-mark {\n" +
"  0% {\n" +
"    margin-top: 1.625em;\n" +
"    -webkit-transform: scale(0.4);\n" +
"            transform: scale(0.4);\n" +
"    opacity: 0; }\n" +
"  50% {\n" +
"    margin-top: 1.625em;\n" +
"    -webkit-transform: scale(0.4);\n" +
"            transform: scale(0.4);\n" +
"    opacity: 0; }\n" +
"  80% {\n" +
"    margin-top: -.375em;\n" +
"    -webkit-transform: scale(1.15);\n" +
"            transform: scale(1.15); }\n" +
"  100% {\n" +
"    margin-top: 0;\n" +
"    -webkit-transform: scale(1);\n" +
"            transform: scale(1);\n" +
"    opacity: 1; } }\n" +
"\n" +
"@keyframes swal2-animate-error-x-mark {\n" +
"  0% {\n" +
"    margin-top: 1.625em;\n" +
"    -webkit-transform: scale(0.4);\n" +
"            transform: scale(0.4);\n" +
"    opacity: 0; }\n" +
"  50% {\n" +
"    margin-top: 1.625em;\n" +
"    -webkit-transform: scale(0.4);\n" +
"            transform: scale(0.4);\n" +
"    opacity: 0; }\n" +
"  80% {\n" +
"    margin-top: -.375em;\n" +
"    -webkit-transform: scale(1.15);\n" +
"            transform: scale(1.15); }\n" +
"  100% {\n" +
"    margin-top: 0;\n" +
"    -webkit-transform: scale(1);\n" +
"            transform: scale(1);\n" +
"    opacity: 1; } }\n" +
"\n" +
"@-webkit-keyframes swal2-animate-error-icon {\n" +
"  0% {\n" +
"    -webkit-transform: rotateX(100deg);\n" +
"            transform: rotateX(100deg);\n" +
"    opacity: 0; }\n" +
"  100% {\n" +
"    -webkit-transform: rotateX(0deg);\n" +
"            transform: rotateX(0deg);\n" +
"    opacity: 1; } }\n" +
"\n" +
"@keyframes swal2-animate-error-icon {\n" +
"  0% {\n" +
"    -webkit-transform: rotateX(100deg);\n" +
"            transform: rotateX(100deg);\n" +
"    opacity: 0; }\n" +
"  100% {\n" +
"    -webkit-transform: rotateX(0deg);\n" +
"            transform: rotateX(0deg);\n" +
"    opacity: 1; } }\n" +
"\n" +
"body.swal2-toast-shown.swal2-has-input > .swal2-container > .swal2-toast {\n" +
"  flex-direction: column;\n" +
"  align-items: stretch; }\n" +
"  body.swal2-toast-shown.swal2-has-input > .swal2-container > .swal2-toast .swal2-actions {\n" +
"    flex: 1;\n" +
"    align-self: stretch;\n" +
"    justify-content: flex-end;\n" +
"    height: 2.2em; }\n" +
"  body.swal2-toast-shown.swal2-has-input > .swal2-container > .swal2-toast .swal2-loading {\n" +
"    justify-content: center; }\n" +
"  body.swal2-toast-shown.swal2-has-input > .swal2-container > .swal2-toast .swal2-input {\n" +
"    height: 2em;\n" +
"    margin: .3125em auto;\n" +
"    font-size: 1em; }\n" +
"  body.swal2-toast-shown.swal2-has-input > .swal2-container > .swal2-toast .swal2-validationerror {\n" +
"    font-size: 1em; }\n" +
"\n" +
"body.swal2-toast-shown > .swal2-container {\n" +
"  position: fixed;\n" +
"  background-color: transparent; }\n" +
"  body.swal2-toast-shown > .swal2-container.swal2-shown {\n" +
"    background-color: transparent; }\n" +
"  body.swal2-toast-shown > .swal2-container.swal2-top {\n" +
"    top: 0;\n" +
"    right: auto;\n" +
"    bottom: auto;\n" +
"    left: 50%;\n" +
"    -webkit-transform: translateX(-50%);\n" +
"            transform: translateX(-50%); }\n" +
"  body.swal2-toast-shown > .swal2-container.swal2-top-end, body.swal2-toast-shown > .swal2-container.swal2-top-right {\n" +
"    top: 0;\n" +
"    right: 0;\n" +
"    bottom: auto;\n" +
"    left: auto; }\n" +
"  body.swal2-toast-shown > .swal2-container.swal2-top-start, body.swal2-toast-shown > .swal2-container.swal2-top-left {\n" +
"    top: 0;\n" +
"    right: auto;\n" +
"    bottom: auto;\n" +
"    left: 0; }\n" +
"  body.swal2-toast-shown > .swal2-container.swal2-center-start, body.swal2-toast-shown > .swal2-container.swal2-center-left {\n" +
"    top: 50%;\n" +
"    right: auto;\n" +
"    bottom: auto;\n" +
"    left: 0;\n" +
"    -webkit-transform: translateY(-50%);\n" +
"            transform: translateY(-50%); }\n" +
"  body.swal2-toast-shown > .swal2-container.swal2-center {\n" +
"    top: 50%;\n" +
"    right: auto;\n" +
"    bottom: auto;\n" +
"    left: 50%;\n" +
"    -webkit-transform: translate(-50%, -50%);\n" +
"            transform: translate(-50%, -50%); }\n" +
"  body.swal2-toast-shown > .swal2-container.swal2-center-end, body.swal2-toast-shown > .swal2-container.swal2-center-right {\n" +
"    top: 50%;\n" +
"    right: 0;\n" +
"    bottom: auto;\n" +
"    left: auto;\n" +
"    -webkit-transform: translateY(-50%);\n" +
"            transform: translateY(-50%); }\n" +
"  body.swal2-toast-shown > .swal2-container.swal2-bottom-start, body.swal2-toast-shown > .swal2-container.swal2-bottom-left {\n" +
"    top: auto;\n" +
"    right: auto;\n" +
"    bottom: 0;\n" +
"    left: 0; }\n" +
"  body.swal2-toast-shown > .swal2-container.swal2-bottom {\n" +
"    top: auto;\n" +
"    right: auto;\n" +
"    bottom: 0;\n" +
"    left: 50%;\n" +
"    -webkit-transform: translateX(-50%);\n" +
"            transform: translateX(-50%); }\n" +
"  body.swal2-toast-shown > .swal2-container.swal2-bottom-end, body.swal2-toast-shown > .swal2-container.swal2-bottom-right {\n" +
"    top: auto;\n" +
"    right: 0;\n" +
"    bottom: 0;\n" +
"    left: auto; }\n" +
"\n" +
".swal2-popup.swal2-toast {\n" +
"  flex-direction: row;\n" +
"  align-items: center;\n" +
"  width: auto;\n" +
"  padding: 0.625em;\n" +
"  box-shadow: 0 0 0.625em #d9d9d9;\n" +
"  overflow-y: hidden; }\n" +
"  .swal2-popup.swal2-toast .swal2-header {\n" +
"    flex-direction: row; }\n" +
"  .swal2-popup.swal2-toast .swal2-title {\n" +
"    justify-content: flex-start;\n" +
"    margin: 0 .6em;\n" +
"    font-size: 1em; }\n" +
"  .swal2-popup.swal2-toast .swal2-close {\n" +
"    position: initial; }\n" +
"  .swal2-popup.swal2-toast .swal2-content {\n" +
"    justify-content: flex-start;\n" +
"    font-size: 1em; }\n" +
"  .swal2-popup.swal2-toast .swal2-icon {\n" +
"    width: 2em;\n" +
"    min-width: 2em;\n" +
"    height: 2em;\n" +
"    margin: 0; }\n" +
"    .swal2-popup.swal2-toast .swal2-icon-text {\n" +
"      font-size: 2em;\n" +
"      font-weight: bold;\n" +
"      line-height: 1em; }\n" +
"    .swal2-popup.swal2-toast .swal2-icon.swal2-success .swal2-success-ring {\n" +
"      width: 2em;\n" +
"      height: 2em; }\n" +
"    .swal2-popup.swal2-toast .swal2-icon.swal2-error [class^='swal2-x-mark-line'] {\n" +
"      top: .875em;\n" +
"      width: 1.375em; }\n" +
"      .swal2-popup.swal2-toast .swal2-icon.swal2-error [class^='swal2-x-mark-line'][class$='left'] {\n" +
"        left: .3125em; }\n" +
"      .swal2-popup.swal2-toast .swal2-icon.swal2-error [class^='swal2-x-mark-line'][class$='right'] {\n" +
"        right: .3125em; }\n" +
"  .swal2-popup.swal2-toast .swal2-actions {\n" +
"    height: auto;\n" +
"    margin: 0 .3125em; }\n" +
"  .swal2-popup.swal2-toast .swal2-styled {\n" +
"    margin: 0 .3125em;\n" +
"    padding: .3125em .625em;\n" +
"    font-size: 1em; }\n" +
"    .swal2-popup.swal2-toast .swal2-styled:focus {\n" +
"      box-shadow: 0 0 0 0.0625em #fff, 0 0 0 0.125em rgba(50, 100, 150, 0.4); }\n" +
"  .swal2-popup.swal2-toast .swal2-success {\n" +
"    border-color: #a5dc86; }\n" +
"    .swal2-popup.swal2-toast .swal2-success [class^='swal2-success-circular-line'] {\n" +
"      position: absolute;\n" +
"      width: 2em;\n" +
"      height: 2.8125em;\n" +
"      -webkit-transform: rotate(45deg);\n" +
"              transform: rotate(45deg);\n" +
"      border-radius: 50%; }\n" +
"      .swal2-popup.swal2-toast .swal2-success [class^='swal2-success-circular-line'][class$='left'] {\n" +
"        top: -.25em;\n" +
"        left: -.9375em;\n" +
"        -webkit-transform: rotate(-45deg);\n" +
"                transform: rotate(-45deg);\n" +
"        -webkit-transform-origin: 2em 2em;\n" +
"                transform-origin: 2em 2em;\n" +
"        border-radius: 4em 0 0 4em; }\n" +
"      .swal2-popup.swal2-toast .swal2-success [class^='swal2-success-circular-line'][class$='right'] {\n" +
"        top: -.25em;\n" +
"        left: .9375em;\n" +
"        -webkit-transform-origin: 0 2em;\n" +
"                transform-origin: 0 2em;\n" +
"        border-radius: 0 4em 4em 0; }\n" +
"    .swal2-popup.swal2-toast .swal2-success .swal2-success-ring {\n" +
"      width: 2em;\n" +
"      height: 2em; }\n" +
"    .swal2-popup.swal2-toast .swal2-success .swal2-success-fix {\n" +
"      top: 0;\n" +
"      left: .4375em;\n" +
"      width: .4375em;\n" +
"      height: 2.6875em; }\n" +
"    .swal2-popup.swal2-toast .swal2-success [class^='swal2-success-line'] {\n" +
"      height: .3125em; }\n" +
"      .swal2-popup.swal2-toast .swal2-success [class^='swal2-success-line'][class$='tip'] {\n" +
"        top: 1.125em;\n" +
"        left: .1875em;\n" +
"        width: .75em; }\n" +
"      .swal2-popup.swal2-toast .swal2-success [class^='swal2-success-line'][class$='long'] {\n" +
"        top: .9375em;\n" +
"        right: .1875em;\n" +
"        width: 1.375em; }\n" +
"  .swal2-popup.swal2-toast.swal2-show {\n" +
"    -webkit-animation: showSweetToast .5s;\n" +
"            animation: showSweetToast .5s; }\n" +
"  .swal2-popup.swal2-toast.swal2-hide {\n" +
"    -webkit-animation: hideSweetToast .2s forwards;\n" +
"            animation: hideSweetToast .2s forwards; }\n" +
"  .swal2-popup.swal2-toast .swal2-animate-success-icon .swal2-success-line-tip {\n" +
"    -webkit-animation: animate-toast-success-tip .75s;\n" +
"            animation: animate-toast-success-tip .75s; }\n" +
"  .swal2-popup.swal2-toast .swal2-animate-success-icon .swal2-success-line-long {\n" +
"    -webkit-animation: animate-toast-success-long .75s;\n" +
"            animation: animate-toast-success-long .75s; }\n" +
"\n" +
"@-webkit-keyframes showSweetToast {\n" +
"  0% {\n" +
"    -webkit-transform: translateY(-0.625em) rotateZ(2deg);\n" +
"            transform: translateY(-0.625em) rotateZ(2deg);\n" +
"    opacity: 0; }\n" +
"  33% {\n" +
"    -webkit-transform: translateY(0) rotateZ(-2deg);\n" +
"            transform: translateY(0) rotateZ(-2deg);\n" +
"    opacity: .5; }\n" +
"  66% {\n" +
"    -webkit-transform: translateY(0.3125em) rotateZ(2deg);\n" +
"            transform: translateY(0.3125em) rotateZ(2deg);\n" +
"    opacity: .7; }\n" +
"  100% {\n" +
"    -webkit-transform: translateY(0) rotateZ(0);\n" +
"            transform: translateY(0) rotateZ(0);\n" +
"    opacity: 1; } }\n" +
"\n" +
"@keyframes showSweetToast {\n" +
"  0% {\n" +
"    -webkit-transform: translateY(-0.625em) rotateZ(2deg);\n" +
"            transform: translateY(-0.625em) rotateZ(2deg);\n" +
"    opacity: 0; }\n" +
"  33% {\n" +
"    -webkit-transform: translateY(0) rotateZ(-2deg);\n" +
"            transform: translateY(0) rotateZ(-2deg);\n" +
"    opacity: .5; }\n" +
"  66% {\n" +
"    -webkit-transform: translateY(0.3125em) rotateZ(2deg);\n" +
"            transform: translateY(0.3125em) rotateZ(2deg);\n" +
"    opacity: .7; }\n" +
"  100% {\n" +
"    -webkit-transform: translateY(0) rotateZ(0);\n" +
"            transform: translateY(0) rotateZ(0);\n" +
"    opacity: 1; } }\n" +
"\n" +
"@-webkit-keyframes hideSweetToast {\n" +
"  0% {\n" +
"    opacity: 1; }\n" +
"  33% {\n" +
"    opacity: .5; }\n" +
"  100% {\n" +
"    -webkit-transform: rotateZ(1deg);\n" +
"            transform: rotateZ(1deg);\n" +
"    opacity: 0; } }\n" +
"\n" +
"@keyframes hideSweetToast {\n" +
"  0% {\n" +
"    opacity: 1; }\n" +
"  33% {\n" +
"    opacity: .5; }\n" +
"  100% {\n" +
"    -webkit-transform: rotateZ(1deg);\n" +
"            transform: rotateZ(1deg);\n" +
"    opacity: 0; } }\n" +
"\n" +
"@-webkit-keyframes animate-toast-success-tip {\n" +
"  0% {\n" +
"    top: .5625em;\n" +
"    left: .0625em;\n" +
"    width: 0; }\n" +
"  54% {\n" +
"    top: .125em;\n" +
"    left: .125em;\n" +
"    width: 0; }\n" +
"  70% {\n" +
"    top: .625em;\n" +
"    left: -.25em;\n" +
"    width: 1.625em; }\n" +
"  84% {\n" +
"    top: 1.0625em;\n" +
"    left: .75em;\n" +
"    width: .5em; }\n" +
"  100% {\n" +
"    top: 1.125em;\n" +
"    left: .1875em;\n" +
"    width: .75em; } }\n" +
"\n" +
"@keyframes animate-toast-success-tip {\n" +
"  0% {\n" +
"    top: .5625em;\n" +
"    left: .0625em;\n" +
"    width: 0; }\n" +
"  54% {\n" +
"    top: .125em;\n" +
"    left: .125em;\n" +
"    width: 0; }\n" +
"  70% {\n" +
"    top: .625em;\n" +
"    left: -.25em;\n" +
"    width: 1.625em; }\n" +
"  84% {\n" +
"    top: 1.0625em;\n" +
"    left: .75em;\n" +
"    width: .5em; }\n" +
"  100% {\n" +
"    top: 1.125em;\n" +
"    left: .1875em;\n" +
"    width: .75em; } }\n" +
"\n" +
"@-webkit-keyframes animate-toast-success-long {\n" +
"  0% {\n" +
"    top: 1.625em;\n" +
"    right: 1.375em;\n" +
"    width: 0; }\n" +
"  65% {\n" +
"    top: 1.25em;\n" +
"    right: .9375em;\n" +
"    width: 0; }\n" +
"  84% {\n" +
"    top: .9375em;\n" +
"    right: 0;\n" +
"    width: 1.125em; }\n" +
"  100% {\n" +
"    top: .9375em;\n" +
"    right: .1875em;\n" +
"    width: 1.375em; } }\n" +
"\n" +
"@keyframes animate-toast-success-long {\n" +
"  0% {\n" +
"    top: 1.625em;\n" +
"    right: 1.375em;\n" +
"    width: 0; }\n" +
"  65% {\n" +
"    top: 1.25em;\n" +
"    right: .9375em;\n" +
"    width: 0; }\n" +
"  84% {\n" +
"    top: .9375em;\n" +
"    right: 0;\n" +
"    width: 1.125em; }\n" +
"  100% {\n" +
"    top: .9375em;\n" +
"    right: .1875em;\n" +
"    width: 1.375em; } }\n" +
"\n" +
"body.swal2-shown:not(.swal2-no-backdrop):not(.swal2-toast-shown) {\n" +
"  overflow-y: hidden; }\n" +
"\n" +
"body.swal2-height-auto {\n" +
"  height: auto !important; }\n" +
"\n" +
"body.swal2-no-backdrop .swal2-shown {\n" +
"  top: auto;\n" +
"  right: auto;\n" +
"  bottom: auto;\n" +
"  left: auto;\n" +
"  background-color: transparent; }\n" +
"  body.swal2-no-backdrop .swal2-shown > .swal2-modal {\n" +
"    box-shadow: 0 0 10px rgba(0, 0, 0, 0.4); }\n" +
"  body.swal2-no-backdrop .swal2-shown.swal2-top {\n" +
"    top: 0;\n" +
"    left: 50%;\n" +
"    -webkit-transform: translateX(-50%);\n" +
"            transform: translateX(-50%); }\n" +
"  body.swal2-no-backdrop .swal2-shown.swal2-top-start, body.swal2-no-backdrop .swal2-shown.swal2-top-left {\n" +
"    top: 0;\n" +
"    left: 0; }\n" +
"  body.swal2-no-backdrop .swal2-shown.swal2-top-end, body.swal2-no-backdrop .swal2-shown.swal2-top-right {\n" +
"    top: 0;\n" +
"    right: 0; }\n" +
"  body.swal2-no-backdrop .swal2-shown.swal2-center {\n" +
"    top: 50%;\n" +
"    left: 50%;\n" +
"    -webkit-transform: translate(-50%, -50%);\n" +
"            transform: translate(-50%, -50%); }\n" +
"  body.swal2-no-backdrop .swal2-shown.swal2-center-start, body.swal2-no-backdrop .swal2-shown.swal2-center-left {\n" +
"    top: 50%;\n" +
"    left: 0;\n" +
"    -webkit-transform: translateY(-50%);\n" +
"            transform: translateY(-50%); }\n" +
"  body.swal2-no-backdrop .swal2-shown.swal2-center-end, body.swal2-no-backdrop .swal2-shown.swal2-center-right {\n" +
"    top: 50%;\n" +
"    right: 0;\n" +
"    -webkit-transform: translateY(-50%);\n" +
"            transform: translateY(-50%); }\n" +
"  body.swal2-no-backdrop .swal2-shown.swal2-bottom {\n" +
"    bottom: 0;\n" +
"    left: 50%;\n" +
"    -webkit-transform: translateX(-50%);\n" +
"            transform: translateX(-50%); }\n" +
"  body.swal2-no-backdrop .swal2-shown.swal2-bottom-start, body.swal2-no-backdrop .swal2-shown.swal2-bottom-left {\n" +
"    bottom: 0;\n" +
"    left: 0; }\n" +
"  body.swal2-no-backdrop .swal2-shown.swal2-bottom-end, body.swal2-no-backdrop .swal2-shown.swal2-bottom-right {\n" +
"    right: 0;\n" +
"    bottom: 0; }\n" +
"\n" +
".swal2-container {\n" +
"  display: flex;\n" +
"  position: fixed;\n" +
"  top: 0;\n" +
"  right: 0;\n" +
"  bottom: 0;\n" +
"  left: 0;\n" +
"  flex-direction: row;\n" +
"  align-items: center;\n" +
"  justify-content: center;\n" +
"  padding: 10px;\n" +
"  background-color: transparent;\n" +
"  z-index: 1060;\n" +
"  overflow-x: hidden;\n" +
"  -webkit-overflow-scrolling: touch; }\n" +
"  .swal2-container.swal2-top {\n" +
"    align-items: flex-start; }\n" +
"  .swal2-container.swal2-top-start, .swal2-container.swal2-top-left {\n" +
"    align-items: flex-start;\n" +
"    justify-content: flex-start; }\n" +
"  .swal2-container.swal2-top-end, .swal2-container.swal2-top-right {\n" +
"    align-items: flex-start;\n" +
"    justify-content: flex-end; }\n" +
"  .swal2-container.swal2-center {\n" +
"    align-items: center; }\n" +
"  .swal2-container.swal2-center-start, .swal2-container.swal2-center-left {\n" +
"    align-items: center;\n" +
"    justify-content: flex-start; }\n" +
"  .swal2-container.swal2-center-end, .swal2-container.swal2-center-right {\n" +
"    align-items: center;\n" +
"    justify-content: flex-end; }\n" +
"  .swal2-container.swal2-bottom {\n" +
"    align-items: flex-end; }\n" +
"  .swal2-container.swal2-bottom-start, .swal2-container.swal2-bottom-left {\n" +
"    align-items: flex-end;\n" +
"    justify-content: flex-start; }\n" +
"  .swal2-container.swal2-bottom-end, .swal2-container.swal2-bottom-right {\n" +
"    align-items: flex-end;\n" +
"    justify-content: flex-end; }\n" +
"  .swal2-container.swal2-grow-fullscreen > .swal2-modal {\n" +
"    display: flex !important;\n" +
"    flex: 1;\n" +
"    align-self: stretch;\n" +
"    justify-content: center; }\n" +
"  .swal2-container.swal2-grow-row > .swal2-modal {\n" +
"    display: flex !important;\n" +
"    flex: 1;\n" +
"    align-content: center;\n" +
"    justify-content: center; }\n" +
"  .swal2-container.swal2-grow-column {\n" +
"    flex: 1;\n" +
"    flex-direction: column; }\n" +
"    .swal2-container.swal2-grow-column.swal2-top, .swal2-container.swal2-grow-column.swal2-center, .swal2-container.swal2-grow-column.swal2-bottom {\n" +
"      align-items: center; }\n" +
"    .swal2-container.swal2-grow-column.swal2-top-start, .swal2-container.swal2-grow-column.swal2-center-start, .swal2-container.swal2-grow-column.swal2-bottom-start, .swal2-container.swal2-grow-column.swal2-top-left, .swal2-container.swal2-grow-column.swal2-center-left, .swal2-container.swal2-grow-column.swal2-bottom-left {\n" +
"      align-items: flex-start; }\n" +
"    .swal2-container.swal2-grow-column.swal2-top-end, .swal2-container.swal2-grow-column.swal2-center-end, .swal2-container.swal2-grow-column.swal2-bottom-end, .swal2-container.swal2-grow-column.swal2-top-right, .swal2-container.swal2-grow-column.swal2-center-right, .swal2-container.swal2-grow-column.swal2-bottom-right {\n" +
"      align-items: flex-end; }\n" +
"    .swal2-container.swal2-grow-column > .swal2-modal {\n" +
"      display: flex !important;\n" +
"      flex: 1;\n" +
"      align-content: center;\n" +
"      justify-content: center; }\n" +
"  .swal2-container:not(.swal2-top):not(.swal2-top-start):not(.swal2-top-end):not(.swal2-top-left):not(.swal2-top-right):not(.swal2-center-start):not(.swal2-center-end):not(.swal2-center-left):not(.swal2-center-right):not(.swal2-bottom):not(.swal2-bottom-start):not(.swal2-bottom-end):not(.swal2-bottom-left):not(.swal2-bottom-right) > .swal2-modal {\n" +
"    margin: auto; }\n" +
"  @media all and (-ms-high-contrast: none), (-ms-high-contrast: active) {\n" +
"    .swal2-container .swal2-modal {\n" +
"      margin: 0 !important; } }\n" +
"  .swal2-container.swal2-fade {\n" +
"    transition: background-color .1s; }\n" +
"  .swal2-container.swal2-shown {\n" +
"    background-color: rgba(0, 0, 0, 0.4); }\n" +
"\n" +
".swal2-popup {\n" +
"  display: none;\n" +
"  position: relative;\n" +
"  flex-direction: column;\n" +
"  justify-content: center;\n" +
"  width: 32em;\n" +
"  max-width: 100%;\n" +
"  padding: 1.25em;\n" +
"  border-radius: 0.3125em;\n" +
"  background: #fff;\n" +
"  font-family: inherit;\n" +
"  font-size: 1rem;\n" +
"  box-sizing: border-box; }\n" +
"  .swal2-popup:focus {\n" +
"    outline: none; }\n" +
"  .swal2-popup.swal2-loading {\n" +
"    overflow-y: hidden; }\n" +
"  .swal2-popup .swal2-header {\n" +
"    display: flex;\n" +
"    flex-direction: column;\n" +
"    align-items: center; }\n" +
"  .swal2-popup .swal2-title {\n" +
"    display: block;\n" +
"    position: relative;\n" +
"    max-width: 100%;\n" +
"    margin: 0 0 0.4em;\n" +
"    padding: 0;\n" +
"    color: #595959;\n" +
"    font-size: 1.875em;\n" +
"    font-weight: 600;\n" +
"    text-align: center;\n" +
"    text-transform: none;\n" +
"    word-wrap: break-word; }\n" +
"  .swal2-popup .swal2-actions {\n" +
"    align-items: center;\n" +
"    justify-content: center;\n" +
"    margin: 1.25em auto 0; }\n" +
"    .swal2-popup .swal2-actions:not(.swal2-loading) .swal2-styled[disabled] {\n" +
"      opacity: .4; }\n" +
"    .swal2-popup .swal2-actions:not(.swal2-loading) .swal2-styled:hover {\n" +
"      background-image: linear-gradient(rgba(0, 0, 0, 0.1), rgba(0, 0, 0, 0.1)); }\n" +
"    .swal2-popup .swal2-actions:not(.swal2-loading) .swal2-styled:active {\n" +
"      background-image: linear-gradient(rgba(0, 0, 0, 0.2), rgba(0, 0, 0, 0.2)); }\n" +
"    .swal2-popup .swal2-actions.swal2-loading .swal2-styled.swal2-confirm {\n" +
"      width: 2.5em;\n" +
"      height: 2.5em;\n" +
"      margin: .46875em;\n" +
"      padding: 0;\n" +
"      border: .25em solid transparent;\n" +
"      border-radius: 100%;\n" +
"      border-color: transparent;\n" +
"      background-color: transparent !important;\n" +
"      color: transparent;\n" +
"      cursor: default;\n" +
"      box-sizing: border-box;\n" +
"      -webkit-animation: swal2-rotate-loading 1.5s linear 0s infinite normal;\n" +
"              animation: swal2-rotate-loading 1.5s linear 0s infinite normal;\n" +
"      -webkit-user-select: none;\n" +
"         -moz-user-select: none;\n" +
"          -ms-user-select: none;\n" +
"              user-select: none; }\n" +
"    .swal2-popup .swal2-actions.swal2-loading .swal2-styled.swal2-cancel {\n" +
"      margin-right: 30px;\n" +
"      margin-left: 30px; }\n" +
"    .swal2-popup .swal2-actions.swal2-loading :not(.swal2-styled).swal2-confirm::after {\n" +
"      display: inline-block;\n" +
"      width: 15px;\n" +
"      height: 15px;\n" +
"      margin-left: 5px;\n" +
"      border: 3px solid #999999;\n" +
"      border-radius: 50%;\n" +
"      border-right-color: transparent;\n" +
"      box-shadow: 1px 1px 1px #fff;\n" +
"      content: '';\n" +
"      -webkit-animation: swal2-rotate-loading 1.5s linear 0s infinite normal;\n" +
"              animation: swal2-rotate-loading 1.5s linear 0s infinite normal; }\n" +
"  .swal2-popup .swal2-styled {\n" +
"    margin: 0 .3125em;\n" +
"    padding: .625em 2em;\n" +
"    font-weight: 500;\n" +
"    box-shadow: none; }\n" +
"    .swal2-popup .swal2-styled:not([disabled]) {\n" +
"      cursor: pointer; }\n" +
"    .swal2-popup .swal2-styled.swal2-confirm {\n" +
"      border: 0;\n" +
"      border-radius: 0.25em;\n" +
"      background: initial;\n" +
"      background-color: #3085d6;\n" +
"      color: #fff;\n" +
"      font-size: 1.0625em; }\n" +
"    .swal2-popup .swal2-styled.swal2-cancel {\n" +
"      border: 0;\n" +
"      border-radius: 0.25em;\n" +
"      background: initial;\n" +
"      background-color: #aaa;\n" +
"      color: #fff;\n" +
"      font-size: 1.0625em; }\n" +
"    .swal2-popup .swal2-styled:focus {\n" +
"      outline: none;\n" +
"      box-shadow: 0 0 0 2px #fff, 0 0 0 4px rgba(50, 100, 150, 0.4); }\n" +
"    .swal2-popup .swal2-styled::-moz-focus-inner {\n" +
"      border: 0; }\n" +
"  .swal2-popup .swal2-footer {\n" +
"    justify-content: center;\n" +
"    margin: 1.25em 0 0;\n" +
"    padding-top: 1em;\n" +
"    border-top: 1px solid #eee;\n" +
"    color: #545454;\n" +
"    font-size: 1em; }\n" +
"  .swal2-popup .swal2-image {\n" +
"    max-width: 100%;\n" +
"    margin: 1.25em auto; }\n" +
"  .swal2-popup .swal2-close {\n" +
"    position: absolute;\n" +
"    top: 0;\n" +
"    right: 0;\n" +
"    justify-content: center;\n" +
"    width: 1.2em;\n" +
"    height: 1.2em;\n" +
"    padding: 0;\n" +
"    transition: color 0.1s ease-out;\n" +
"    border: none;\n" +
"    border-radius: 0;\n" +
"    background: transparent;\n" +
"    color: #cccccc;\n" +
"    font-family: serif;\n" +
"    font-size: 2.5em;\n" +
"    line-height: 1.2;\n" +
"    cursor: pointer;\n" +
"    overflow: hidden; }\n" +
"    .swal2-popup .swal2-close:hover {\n" +
"      -webkit-transform: none;\n" +
"              transform: none;\n" +
"      color: #f27474; }\n" +
"  .swal2-popup > .swal2-input,\n" +
"  .swal2-popup > .swal2-file,\n" +
"  .swal2-popup > .swal2-textarea,\n" +
"  .swal2-popup > .swal2-select,\n" +
"  .swal2-popup > .swal2-radio,\n" +
"  .swal2-popup > .swal2-checkbox {\n" +
"    display: none; }\n" +
"  .swal2-popup .swal2-content {\n" +
"    justify-content: center;\n" +
"    margin: 0;\n" +
"    padding: 0;\n" +
"    color: #545454;\n" +
"    font-size: 1.125em;\n" +
"    font-weight: 300;\n" +
"    line-height: normal;\n" +
"    word-wrap: break-word; }\n" +
"  .swal2-popup #swal2-content {\n" +
"    text-align: center; }\n" +
"  .swal2-popup .swal2-input,\n" +
"  .swal2-popup .swal2-file,\n" +
"  .swal2-popup .swal2-textarea,\n" +
"  .swal2-popup .swal2-select,\n" +
"  .swal2-popup .swal2-radio,\n" +
"  .swal2-popup .swal2-checkbox {\n" +
"    margin: 1em auto; }\n" +
"  .swal2-popup .swal2-input,\n" +
"  .swal2-popup .swal2-file,\n" +
"  .swal2-popup .swal2-textarea {\n" +
"    width: 100%;\n" +
"    transition: border-color .3s, box-shadow .3s;\n" +
"    border: 1px solid #d9d9d9;\n" +
"    border-radius: 0.1875em;\n" +
"    font-size: 1.125em;\n" +
"    box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.06);\n" +
"    box-sizing: border-box; }\n" +
"    .swal2-popup .swal2-input.swal2-inputerror,\n" +
"    .swal2-popup .swal2-file.swal2-inputerror,\n" +
"    .swal2-popup .swal2-textarea.swal2-inputerror {\n" +
"      border-color: #f27474 !important;\n" +
"      box-shadow: 0 0 2px #f27474 !important; }\n" +
"    .swal2-popup .swal2-input:focus,\n" +
"    .swal2-popup .swal2-file:focus,\n" +
"    .swal2-popup .swal2-textarea:focus {\n" +
"      border: 1px solid #b4dbed;\n" +
"      outline: none;\n" +
"      box-shadow: 0 0 3px #c4e6f5; }\n" +
"    .swal2-popup .swal2-input::-webkit-input-placeholder,\n" +
"    .swal2-popup .swal2-file::-webkit-input-placeholder,\n" +
"    .swal2-popup .swal2-textarea::-webkit-input-placeholder {\n" +
"      color: #cccccc; }\n" +
"    .swal2-popup .swal2-input:-ms-input-placeholder,\n" +
"    .swal2-popup .swal2-file:-ms-input-placeholder,\n" +
"    .swal2-popup .swal2-textarea:-ms-input-placeholder {\n" +
"      color: #cccccc; }\n" +
"    .swal2-popup .swal2-input::-ms-input-placeholder,\n" +
"    .swal2-popup .swal2-file::-ms-input-placeholder,\n" +
"    .swal2-popup .swal2-textarea::-ms-input-placeholder {\n" +
"      color: #cccccc; }\n" +
"    .swal2-popup .swal2-input::placeholder,\n" +
"    .swal2-popup .swal2-file::placeholder,\n" +
"    .swal2-popup .swal2-textarea::placeholder {\n" +
"      color: #cccccc; }\n" +
"  .swal2-popup .swal2-range input {\n" +
"    width: 80%; }\n" +
"  .swal2-popup .swal2-range output {\n" +
"    width: 20%;\n" +
"    font-weight: 600;\n" +
"    text-align: center; }\n" +
"  .swal2-popup .swal2-range input,\n" +
"  .swal2-popup .swal2-range output {\n" +
"    height: 2.625em;\n" +
"    margin: 1em auto;\n" +
"    padding: 0;\n" +
"    font-size: 1.125em;\n" +
"    line-height: 2.625em; }\n" +
"  .swal2-popup .swal2-input {\n" +
"    height: 2.625em;\n" +
"    padding: 0.75em; }\n" +
"    .swal2-popup .swal2-input[type='number'] {\n" +
"      max-width: 10em; }\n" +
"  .swal2-popup .swal2-file {\n" +
"    font-size: 1.125em; }\n" +
"  .swal2-popup .swal2-textarea {\n" +
"    height: 6.75em;\n" +
"    padding: 0.75em; }\n" +
"  .swal2-popup .swal2-select {\n" +
"    min-width: 50%;\n" +
"    max-width: 100%;\n" +
"    padding: .375em .625em;\n" +
"    color: #545454;\n" +
"    font-size: 1.125em; }\n" +
"  .swal2-popup .swal2-radio,\n" +
"  .swal2-popup .swal2-checkbox {\n" +
"    align-items: center;\n" +
"    justify-content: center; }\n" +
"    .swal2-popup .swal2-radio label,\n" +
"    .swal2-popup .swal2-checkbox label {\n" +
"      margin: 0 .6em;\n" +
"      font-size: 1.125em; }\n" +
"    .swal2-popup .swal2-radio input,\n" +
"    .swal2-popup .swal2-checkbox input {\n" +
"      margin: 0 .4em; }\n" +
"  .swal2-popup .swal2-validationerror {\n" +
"    display: none;\n" +
"    align-items: center;\n" +
"    justify-content: center;\n" +
"    padding: 0.625em;\n" +
"    background: #f0f0f0;\n" +
"    color: #666666;\n" +
"    font-size: 1em;\n" +
"    font-weight: 300;\n" +
"    overflow: hidden; }\n" +
"    .swal2-popup .swal2-validationerror::before {\n" +
"      display: inline-block;\n" +
"      width: 1.5em;\n" +
"      min-width: 1.5em;\n" +
"      height: 1.5em;\n" +
"      margin: 0 .625em;\n" +
"      border-radius: 50%;\n" +
"      background-color: #f27474;\n" +
"      color: #fff;\n" +
"      font-weight: 600;\n" +
"      line-height: 1.5em;\n" +
"      text-align: center;\n" +
"      content: '!';\n" +
"      zoom: normal; }\n" +
"\n" +
"@supports (-ms-accelerator: true) {\n" +
"  .swal2-range input {\n" +
"    width: 100% !important; }\n" +
"  .swal2-range output {\n" +
"    display: none; } }\n" +
"\n" +
"@media all and (-ms-high-contrast: none), (-ms-high-contrast: active) {\n" +
"  .swal2-range input {\n" +
"    width: 100% !important; }\n" +
"  .swal2-range output {\n" +
"    display: none; } }\n" +
"\n" +
"@-moz-document url-prefix() {\n" +
"  .swal2-close:focus {\n" +
"    outline: 2px solid rgba(50, 100, 150, 0.4); } }\n" +
"\n" +
".swal2-icon {\n" +
"  position: relative;\n" +
"  justify-content: center;\n" +
"  width: 5em;\n" +
"  height: 5em;\n" +
"  margin: 1.25em auto 1.875em;\n" +
"  border: .25em solid transparent;\n" +
"  border-radius: 50%;\n" +
"  line-height: 5em;\n" +
"  cursor: default;\n" +
"  box-sizing: content-box;\n" +
"  -webkit-user-select: none;\n" +
"     -moz-user-select: none;\n" +
"      -ms-user-select: none;\n" +
"          user-select: none;\n" +
"  zoom: normal; }\n" +
"  .swal2-icon-text {\n" +
"    font-size: 3.75em; }\n" +
"  .swal2-icon.swal2-error {\n" +
"    border-color: #f27474; }\n" +
"    .swal2-icon.swal2-error .swal2-x-mark {\n" +
"      position: relative;\n" +
"      flex-grow: 1; }\n" +
"    .swal2-icon.swal2-error [class^='swal2-x-mark-line'] {\n" +
"      display: block;\n" +
"      position: absolute;\n" +
"      top: 2.3125em;\n" +
"      width: 2.9375em;\n" +
"      height: .3125em;\n" +
"      border-radius: .125em;\n" +
"      background-color: #f27474; }\n" +
"      .swal2-icon.swal2-error [class^='swal2-x-mark-line'][class$='left'] {\n" +
"        left: 1.0625em;\n" +
"        -webkit-transform: rotate(45deg);\n" +
"                transform: rotate(45deg); }\n" +
"      .swal2-icon.swal2-error [class^='swal2-x-mark-line'][class$='right'] {\n" +
"        right: 1em;\n" +
"        -webkit-transform: rotate(-45deg);\n" +
"                transform: rotate(-45deg); }\n" +
"  .swal2-icon.swal2-warning {\n" +
"    border-color: #facea8;\n" +
"    color: #f8bb86; }\n" +
"  .swal2-icon.swal2-info {\n" +
"    border-color: #9de0f6;\n" +
"    color: #3fc3ee; }\n" +
"  .swal2-icon.swal2-question {\n" +
"    border-color: #c9dae1;\n" +
"    color: #87adbd; }\n" +
"  .swal2-icon.swal2-success {\n" +
"    border-color: #a5dc86; }\n" +
"    .swal2-icon.swal2-success [class^='swal2-success-circular-line'] {\n" +
"      position: absolute;\n" +
"      width: 3.75em;\n" +
"      height: 7.5em;\n" +
"      -webkit-transform: rotate(45deg);\n" +
"              transform: rotate(45deg);\n" +
"      border-radius: 50%; }\n" +
"      .swal2-icon.swal2-success [class^='swal2-success-circular-line'][class$='left'] {\n" +
"        top: -.4375em;\n" +
"        left: -2.0635em;\n" +
"        -webkit-transform: rotate(-45deg);\n" +
"                transform: rotate(-45deg);\n" +
"        -webkit-transform-origin: 3.75em 3.75em;\n" +
"                transform-origin: 3.75em 3.75em;\n" +
"        border-radius: 7.5em 0 0 7.5em; }\n" +
"      .swal2-icon.swal2-success [class^='swal2-success-circular-line'][class$='right'] {\n" +
"        top: -.6875em;\n" +
"        left: 1.875em;\n" +
"        -webkit-transform: rotate(-45deg);\n" +
"                transform: rotate(-45deg);\n" +
"        -webkit-transform-origin: 0 3.75em;\n" +
"                transform-origin: 0 3.75em;\n" +
"        border-radius: 0 7.5em 7.5em 0; }\n" +
"    .swal2-icon.swal2-success .swal2-success-ring {\n" +
"      position: absolute;\n" +
"      top: -.25em;\n" +
"      left: -.25em;\n" +
"      width: 100%;\n" +
"      height: 100%;\n" +
"      border: 0.25em solid rgba(165, 220, 134, 0.3);\n" +
"      border-radius: 50%;\n" +
"      z-index: 2;\n" +
"      box-sizing: content-box; }\n" +
"    .swal2-icon.swal2-success .swal2-success-fix {\n" +
"      position: absolute;\n" +
"      top: .5em;\n" +
"      left: 1.625em;\n" +
"      width: .4375em;\n" +
"      height: 5.625em;\n" +
"      -webkit-transform: rotate(-45deg);\n" +
"              transform: rotate(-45deg);\n" +
"      z-index: 1; }\n" +
"    .swal2-icon.swal2-success [class^='swal2-success-line'] {\n" +
"      display: block;\n" +
"      position: absolute;\n" +
"      height: .3125em;\n" +
"      border-radius: .125em;\n" +
"      background-color: #a5dc86;\n" +
"      z-index: 2; }\n" +
"      .swal2-icon.swal2-success [class^='swal2-success-line'][class$='tip'] {\n" +
"        top: 2.875em;\n" +
"        left: .875em;\n" +
"        width: 1.5625em;\n" +
"        -webkit-transform: rotate(45deg);\n" +
"                transform: rotate(45deg); }\n" +
"      .swal2-icon.swal2-success [class^='swal2-success-line'][class$='long'] {\n" +
"        top: 2.375em;\n" +
"        right: .5em;\n" +
"        width: 2.9375em;\n" +
"        -webkit-transform: rotate(-45deg);\n" +
"                transform: rotate(-45deg); }\n" +
"\n" +
".swal2-progresssteps {\n" +
"  align-items: center;\n" +
"  margin: 0 0 1.25em;\n" +
"  padding: 0;\n" +
"  font-weight: 600; }\n" +
"  .swal2-progresssteps li {\n" +
"    display: inline-block;\n" +
"    position: relative; }\n" +
"  .swal2-progresssteps .swal2-progresscircle {\n" +
"    width: 2em;\n" +
"    height: 2em;\n" +
"    border-radius: 2em;\n" +
"    background: #3085d6;\n" +
"    color: #fff;\n" +
"    line-height: 2em;\n" +
"    text-align: center;\n" +
"    z-index: 20; }\n" +
"    .swal2-progresssteps .swal2-progresscircle:first-child {\n" +
"      margin-left: 0; }\n" +
"    .swal2-progresssteps .swal2-progresscircle:last-child {\n" +
"      margin-right: 0; }\n" +
"    .swal2-progresssteps .swal2-progresscircle.swal2-activeprogressstep {\n" +
"      background: #3085d6; }\n" +
"      .swal2-progresssteps .swal2-progresscircle.swal2-activeprogressstep ~ .swal2-progresscircle {\n" +
"        background: #add8e6; }\n" +
"      .swal2-progresssteps .swal2-progresscircle.swal2-activeprogressstep ~ .swal2-progressline {\n" +
"        background: #add8e6; }\n" +
"  .swal2-progresssteps .swal2-progressline {\n" +
"    width: 2.5em;\n" +
"    height: .4em;\n" +
"    margin: 0 -1px;\n" +
"    background: #3085d6;\n" +
"    z-index: 10; }\n" +
"\n" +
"[class^='swal2'] {\n" +
"  -webkit-tap-highlight-color: transparent; }\n" +
"\n" +
".swal2-show {\n" +
"  -webkit-animation: swal2-show 0.3s;\n" +
"          animation: swal2-show 0.3s; }\n" +
"  .swal2-show.swal2-noanimation {\n" +
"    -webkit-animation: none;\n" +
"            animation: none; }\n" +
"\n" +
".swal2-hide {\n" +
"  -webkit-animation: swal2-hide 0.15s forwards;\n" +
"          animation: swal2-hide 0.15s forwards; }\n" +
"  .swal2-hide.swal2-noanimation {\n" +
"    -webkit-animation: none;\n" +
"            animation: none; }\n" +
"\n" +
"[dir='rtl'] .swal2-close {\n" +
"  right: auto;\n" +
"  left: 0; }\n" +
"\n" +
".swal2-animate-success-icon .swal2-success-line-tip {\n" +
"  -webkit-animation: swal2-animate-success-line-tip 0.75s;\n" +
"          animation: swal2-animate-success-line-tip 0.75s; }\n" +
"\n" +
".swal2-animate-success-icon .swal2-success-line-long {\n" +
"  -webkit-animation: swal2-animate-success-line-long 0.75s;\n" +
"          animation: swal2-animate-success-line-long 0.75s; }\n" +
"\n" +
".swal2-animate-success-icon .swal2-success-circular-line-right {\n" +
"  -webkit-animation: swal2-rotate-success-circular-line 4.25s ease-in;\n" +
"          animation: swal2-rotate-success-circular-line 4.25s ease-in; }\n" +
"\n" +
".swal2-animate-error-icon {\n" +
"  -webkit-animation: swal2-animate-error-icon 0.5s;\n" +
"          animation: swal2-animate-error-icon 0.5s; }\n" +
"  .swal2-animate-error-icon .swal2-x-mark {\n" +
"    -webkit-animation: swal2-animate-error-x-mark 0.5s;\n" +
"            animation: swal2-animate-error-x-mark 0.5s; }\n" +
"\n" +
"@-webkit-keyframes swal2-rotate-loading {\n" +
"  0% {\n" +
"    -webkit-transform: rotate(0deg);\n" +
"            transform: rotate(0deg); }\n" +
"  100% {\n" +
"    -webkit-transform: rotate(360deg);\n" +
"            transform: rotate(360deg); } }\n" +
"\n" +
"@keyframes swal2-rotate-loading {\n" +
"  0% {\n" +
"    -webkit-transform: rotate(0deg);\n" +
"            transform: rotate(0deg); }\n" +
"  100% {\n" +
"    -webkit-transform: rotate(360deg);\n" +
"            transform: rotate(360deg); } }");


File: /public\js\usuariosHotspot\activos.js
let tablaUsersActive = $('#tablaUsersActive').DataTable({
    responsive: true,
    //bDestroy: true,
    language: {
    "decimal": "",
    "emptyTable": "No hay información",
    "info": "Mostrando _START_ a _END_ de _TOTAL_ Entradas",
    "infoEmpty": "Mostrando 0 to 0 of 0 Entradas",
    "infoFiltered": "(Filtrado de _MAX_ total entradas)",
    "infoPostFix": "",
    "thousands": ",",
    "lengthMenu": "Mostrar _MENU_ Entradas",
    "loadingRecords": "Cargando...",
    "processing": "Procesando...",
    "search": "Buscar:",
    "zeroRecords": "Sin resultados encontrados"
    },
})

File: /public\js\usuariosHotspot\agregar.js
// para validar campos acepten solo numeros enteros
$(function(){
    $(".validarEntero").keydown(function(event){
        //alert(event.keyCode);
        if((event.keyCode < 48 || event.keyCode > 57) && (event.keyCode < 96 || event.keyCode > 105) && event.keyCode !==190  && event.keyCode !==110 && event.keyCode !==8 && event.keyCode !==9  ){
            return false;
        }
    });
});

File: /public\js\usuariosHotspot\generador.js
// para validar campos acepten solo numeros enteros
$(function(){
    $(".validarEntero").keydown(function(event){
        //alert(event.keyCode);
        if((event.keyCode < 48 || event.keyCode > 57) && (event.keyCode < 96 || event.keyCode > 105) && event.keyCode !==190  && event.keyCode !==110 && event.keyCode !==8 && event.keyCode !==9  ){
            return false;
        }
    });
});

File: /public\js\usuariosHotspot\index.js
const token = document.getElementById("tokenCSRF").value; //obtengo el token, que está en campo oculto del modal showUserHotspot


let tablaUsers = $('#tablaUsers').DataTable({
    responsive: true,
    //bDestroy: true,
    language: {
    "decimal": "",
    "emptyTable": "No hay información",
    "info": "Mostrando _START_ a _END_ de _TOTAL_ Entradas",
    "infoEmpty": "Mostrando 0 to 0 of 0 Entradas",
    "infoFiltered": "(Filtrado de _MAX_ total entradas)",
    "infoPostFix": "",
    "thousands": ",",
    "lengthMenu": "Mostrar _MENU_ Entradas",
    "loadingRecords": "Cargando...",
    "processing": "Procesando...",
    "search": "Buscar:",
    "zeroRecords": "Sin resultados encontrados"
    },
});

    //para marcar como seleccionado una fila
    $('#tablaUsers tbody').on('click', 'tr', function () {
        $(this).toggleClass('selected');
    });

//tablaUsers.rows({search: 'applied'}).select();
//para seleccionar todos los rows del datatable
$(".selectAll").on( "click", function(e) {
    if ($(this).is( ":checked" )) {
        tablaUsers.rows().select();        
    } else {
        tablaUsers.rows().deselect(); 
    }
});

function verTickets() {

    let users = $.map(tablaUsers.rows('.selected').data(), function (item) {
        return {'name':item[2], 'password':item[3], 'limitUptime':item[4],'profile':item[5],'comment':item[6]};
    });

    if(users.length > 0){
        localStorage.setItem('listaTicketsMK',JSON.stringify(users));        
        window.location.href = 'usuarioshotspot/vervouchers'; // redirijo        
    } else {
        users = [];
        localStorage.setItem('listaTicketsMK',JSON.stringify(users));
        showMessageNotify('Debes seleccionar un elemento de la tabla primero', 'danger', 2000); //muestro alerta

    }       
}


function showUserHotspot(id) {

    $.ajax({
        url: "usuarioshotspot/getInfoUserHotspot", 
        type: "POST",
        dataType:"json",
        data: {
            idUser:id,
            tokenCsrf: token
        },
        success: function(respuesta) { //respuesta es un json
            ok = respuesta.ok;
            if(ok){
                usuario = respuesta.user[0]; //regresa un array, se ocupa el de la posición 1
                //si esos valores no existen, se mandan vacíos
                idUser = usuario['.id'];
                name = usuario.name || '';
                password = usuario.password || '';
                profile = usuario.profile || '';
                comment = usuario.comment || '';
                //se pinta en los campos los valores obtenidos
                document.getElementById("idUserHotspot").value = idUser;
                document.getElementById("username").value = name;
                document.getElementById("password").value = password;
                document.getElementById("grupoLimiteAnchosBanda").value = profile;
                document.getElementById("informacion").value = comment;
                $('#showUserHotspot').modal('show');//muestro el modal con los datos cargados
                activeButton(); //se llama la funcion para activar/desactivar el botón de actualizar del modal

            }            
        },
        error: function(respuesta) {
            console.log('error')
        }
    })
}

function activeButton() {
    username = document.getElementById("username").value ;
    password = document.getElementById("password").value;
    profile = $("#grupoLimiteAnchosBanda :selected").val();
    comment = document.getElementById("informacion").value;
    
    let disabled = (username == '' || password == '' || profile == ''  || comment == '' ) ? true : false ;   

    $('#btnSaveUserHotspot').prop("disabled", disabled);
}

function updateUserHotspot() {
    id = document.getElementById("idUserHotspot").value ;
    username = document.getElementById("username").value ;
    password = document.getElementById("password").value;
    profile = $("#grupoLimiteAnchosBanda :selected").val();
    comment = document.getElementById("informacion").value;
    //creo el objeto user con los datos recogidos
    user = { id, username, password, profile, comment };

    $.ajax({
        url: "usuarioshotspot/updateUserHotspot", 
        type: "POST",
        dataType:"json",
        data: {
            user,
            tokenCsrf: token
        },
        success: function(respuesta) { //respuesta es un json
            ok = respuesta.ok;
            if(ok){
                mensaje= respuesta.mensaje;
                showMessageNotify(mensaje, 'info', 2500); //muestro alerta
                $('#showUserHotspot').modal('hide');
                setTimeout(() => {
                    location.reload();
                }, 3000);
            }
                           
        },
        error: function(respuesta) {
            console.log('error')
        }
    })

}

function deleteUserHotspot(id, username) {
    Swal.fire({
        title: `¿Estás seguro de eliminar al usuario  ${username}?`,
        text: "¡No podrás revertir esto!",
        type: 'warning',
        showCancelButton: true,
        confirmButtonColor: '#3085d6',
        cancelButtonColor: '#d33',
        cancelButtonText: '¡Cancelar!',
        confirmButtonText: 'Sí, borrarlo!'
        }).then((result) => {
        if (result.value) {
            $.ajax({
                url: "usuarioshotspot/deleteUserHotspot", 
                type: "POST",
                dataType:"json",
                data: {
                    id,
                    tokenCsrf: token
                },
                success: function(respuesta) { //respuesta es un json
                    ok = respuesta.ok;
                    if(ok){
                        mensaje = respuesta.mensaje+': '+username;
                        showMessageNotify(mensaje, 'success', 2000); //muestro alerta
                        setTimeout(() => {
                            location.reload();
                        }, 2500);
                    }              
                },
                error: function(respuesta) {
                    console.log('error')
                }
            })
        }
    })
}

function resetCounterUserHotspot(id, username) {
    Swal.fire({
        title: `Reiniciar el contador del usuario ${username}?`,
        text: "¡Si elimina el contador, el usuario puede iniciar sesión nuevamente si el límite de tiempo se ha agotado!",
        type: 'warning',
        showCancelButton: true,
        confirmButtonColor: '#3085d6',
        cancelButtonColor: '#d33',
        cancelButtonText: '¡Cancelar!',
        confirmButtonText: 'Sí, resetear!'
        }).then((result) => {
        if (result.value) {
            $.ajax({
                url: "usuarioshotspot/resetCounterUserHotspot", 
                type: "POST",
                dataType:"json",
                data: {
                    id,
                    tokenCsrf: token
                },
                success: function(respuesta) { //respuesta es un json
                    ok = respuesta.ok;
                    if(ok){
                        mensaje = respuesta.mensaje+': '+username;
                        showMessageNotify(mensaje, 'success', 2000); //muestro alerta
                        setTimeout(() => {
                            location.reload();
                        }, 2500);
                    }              
                },
                error: function(respuesta) {
                    console.log('error')
                }
            })
        }
    })
}

// funcion exclusiva para mostrar mensajes como notificaciones
function showMessageNotify(mensaje, tipo, duracion) {
    $.notify({							
      message: `<i class="fa fa-sun"></i><strong> ${mensaje}</strong>`
      },{								
          type: tipo,
          delay: duracion,
          z_index: 3000,
    });
} 

File: /public\js\usuariosHotspot\verVouchers.js
const encabezado = document.getElementById("encabezado").value; 
const pie = document.getElementById("pie").value; 

showVouchers();

function showVouchers() {
  if(localStorage.getItem('listaTicketsMK')){
    listadoTickets = JSON.parse(localStorage.getItem('listaTicketsMK')); //convierto a json
    if(listadoTickets.length > 0){
        contador=1;
        for (let i = 0; i < listadoTickets.length; i++) {

            name = listadoTickets[i]['name'];
            password = listadoTickets[i]['password'];
            profile = listadoTickets[i]['profile'];
            limitUptime = listadoTickets[i]['limitUptime'];
            comment = listadoTickets[i]['comment'];

            ticket = `
                <table style="display: inline-block; width: 250px; border: 1px solid #121DAE; line-height: 110%; font-family: arial; font-size: 12px; margin: 1px;">     
                    <tbody>         
                        <tr>             
                            <td style="text-align: center; color: #2F38F4; font-size: 13px; border-bottom: 1px #ccc solid;"><b>${encabezado}</b></td>        
                        </tr>          
                        <tr>              
                            <td>                   
                                <table style=" text-align: center; width: 240px; background-color: #fff; line-height: 110%; font-size: 11px;">              
                                    <tbody>                
                                        <tr style="background-color: #eee;">                               
                                            <td style="background-color: #fff; width: 33%"><b>Número</b></td>                               
                                            <td style="width: 33%"><b>Paquete</b></td>                                 
                                            <td style="width: 33%">Datos</td>                            
                                        </tr>                           
                                        <tr>                              
                                            <td ><b>${contador}</b></td>                              
                                            <td><b>${profile}</b></td>                              
                                            <td>Ilimitados</td>                   
                                        </tr>                       
                                    </tbody>                  
                                </table>           
                            </td>             
                        </tr>             
                        <tr>       
                            <td>                  
                                    <table style=" text-align: center; width: 240px; background-color: #fff; line-height: 110%; font-size: 11px;">               
                                        <tbody>                         
                                            <tr style="background-color: #eee;">                             
                                                <td style="width: 33%">Tiempo</td>                             
                                                <td style="width: 33%"></td>                             
                                                <td style="width: 33%">Precio</td>                         
                                            </tr>                         
                                            <tr>                        
                                                <td> ${limitUptime}</td>                             
                                                <td></td>                             
                                                <td>$${comment}</td>
                                            </tr>                     
                                    </tbody>                   
                                </table>                
                            </td>              
                        </tr>              
                        <tr>                 
                            <td>                      
                                <table style=" text-align: center; width: 240px; background-color: #fff; line-height: 110%; font-size: 12px; border-top: 1px solid #ccc;">    
                                    <tbody>                             
                                        <tr style="color: #1A16B8; font-size: 11px;">                       
                                            <td style="width: 50%">Usuario</td>                          
                                            <td>Contraseña</td>                   
                                        </tr>                         
                                        <tr style="background-color: #fff;">                                
                                            <td style="color: #000000; border: 1px #ccc solid;">${name}</td>                               
                                            <td style="color: #000000; border: 1px #ccc solid;">${password}</td>                                
                                        </tr>                          
                                    </tbody>                      
                                </table>                 
                            </td>              
                        </tr>              
                        <tr>                   
                            <td style="text-align: center; font-size:11px;">${pie}</td>             
                            </tr>      
                        </tbody>     
                </table>
            `;          
            contador ++;
            $("#vouchers").append(ticket);
        }
    }
  }    
}

File: /public\js\usuariosMikrotik\index.js
const token = document.getElementById("tokenCSRF").value; //obtengo el token, que está en campo oculto del modal showUserHotspot

let usersMikrotik = $('#usersMikrotik').DataTable({
    responsive: true,
    //bDestroy: true,
    language: {
    "decimal": "",
    "emptyTable": "No hay información",
    "info": "Mostrando _START_ a _END_ de _TOTAL_ Entradas",
    "infoEmpty": "Mostrando 0 to 0 of 0 Entradas",
    "infoFiltered": "(Filtrado de _MAX_ total entradas)",
    "infoPostFix": "",
    "thousands": ",",
    "lengthMenu": "Mostrar _MENU_ Entradas",
    "loadingRecords": "Cargando...",
    "processing": "Procesando...",
    "search": "Buscar:",
    "zeroRecords": "Sin resultados encontrados"
    },
});

function deleteUserMikrotik(id, username) {
    Swal.fire({
        title: `¿Estás seguro de eliminar a  ${username}?`,
        text: "¡No podrás revertir esto!",
        type: 'warning',
        showCancelButton: true,
        confirmButtonColor: '#3085d6',
        cancelButtonColor: '#d33',
        cancelButtonText: '¡Cancelar!',
        confirmButtonText: 'Sí, borrarlo!'
        }).then((result) => {
        if (result.value) {
            $.ajax({
                url: "usuariosmikrotik/deleteUserMikrotik", 
                type: "POST",
                dataType:"json",
                data: {
                    id,
                    tokenCsrf: token
                },
                success: function(respuesta) { //respuesta es un json
                    ok = respuesta.ok;
                    if(ok){
                        mensaje = respuesta.mensaje+': '+username;
                        showMessageNotify(mensaje, 'success', 2000); //muestro alerta
                        setTimeout(() => {
                            location.reload();
                        }, 2500);
                    }              
                },
                error: function(respuesta) {
                    console.log('error')
                }
            })
        }
    })
}

// funcion exclusiva para mostrar mensajes como notificaciones
function showMessageNotify(mensaje, tipo, duracion) {
    $.notify({							
      message: `<i class="fa fa-sun"></i><strong> ${mensaje}</strong>`
      },{								
          type: tipo,
          delay: duracion,
          z_index: 3000,
    });
} 

File: /public\js\usuariosMikrotik\reiniciarMikrotik.js
const token = document.getElementById("tokenCSRF").value; //obtengo el token, que está en campo oculto
const mikrotik = document.getElementById("mikrotik").value; //obtengo el mikrotik, que está en campo oculto
const urlRoot = document.getElementById("urlRoot").value; //obtengo el urlRoot, que está en campo oculto
  

function reboot() {
    Swal.fire({
        title: `¿Estás seguro de reiniciar el equipo ${mikrotik}?`,
        text: "¡Saldrás de la aplicación!",
        type: 'warning',
        showCancelButton: true,
        confirmButtonColor: '#3085d6',
        cancelButtonColor: '#d33',
        cancelButtonText: '¡Cancelar!',
        confirmButtonText: 'Sí, Reiniciar!'
        }).then((result) => {
        if (result.value) {
            $.ajax({
                url: "reiniciarmikrotik", 
                type: "POST",
                dataType:"json",
                data: {
                    tokenCsrf: token
                },
                success: function(respuesta) { //respuesta es un json
                    ok = respuesta.ok;
                    if(ok){
                        mensaje = respuesta.mensaje;
                        showMessageNotify(mensaje, 'success', 2000); //muestro alerta
                        setTimeout(() => {
                            document.location.href = urlRoot;
                        }, 2500);
                       
                    }              
                },
                error: function(respuesta) {
                    console.log('error')
                }
            })
        }
    });
}

// funcion exclusiva para mostrar mensajes como notificaciones
function showMessageNotify(mensaje, tipo, duracion) {
    $.notify({							
      message: `<i class="fa fa-sun"></i><strong> ${mensaje}</strong>`
      },{								
          type: tipo,
          delay: duracion,
          z_index: 3000,
    });
}

File: /README.md
# MikrotikPHP apiHotspotUserGenerator
Generador de usuario hotspot con API Mikrotik PHP 

Aplicación de gestión de usuarios hotspot que utiliza la API Mikrotik PHP. Tiene las siguientes capacidades:

1. Puede crear y generar usuarios hotspot a través de la interfaz de la aplicación
2. Puede administrar el ancho de banda del usuario a través de la interfaz de la aplicación
3. Puede configurar el tiempo de acceso a la red de hotspot a través de la interfaz de la aplicación
5. Realizado bajo MVC, POO


# Instalación y uso

1. Se requiere PHP en su version 7 en adelante. Recomendable tener tu entorno de prueba XAMPP en Windows o MAMP en Mac.
2. Poner en htdocs la carpeta del proyecto, (un nombre sin espacios).
3. En la estrucutura de directorios se cuenta con 3 archivos **.htaccess** de estos se tiene que cambiarle algo a uno de estos.
4. En la carpeta **public** se modifica en el **.htaccess** la linea ***/base/public/*** por el nombre que le hayas puesto a tu directorio en htdocs. Como ejemplo, ***base*** es la carpeta que contiene el proyecto, su **.htaccess**:

~~~
<IfModule mod_rewrite.c>
    Options -Multiviews
    RewriteEngine On
    RewriteBase /base/public/
    RewriteCond %{REQUEST_FILENAME} !-d
    RewriteCond %{REQUEST_FILENAME} !-f
    RewriteRule ^(.+)$ index.php?url=$1 [QSA,L]
</IfModule>
~~~

5. Sí en htdocs le pones de nombre **mikrovouchers** a la carpeta del proyecto, **RewriteBase** queda como  ***RewriteBase /mikrovouchers/public/***

~~~
<IfModule mod_rewrite.c>
    Options -Multiviews
    RewriteEngine On
    RewriteBase /mikrovouchers/public/
    RewriteCond %{REQUEST_FILENAME} !-d
    RewriteCond %{REQUEST_FILENAME} !-f
    RewriteRule ^(.+)$ index.php?url=$1 [QSA,L]
</IfModule>
~~~

6. Dentro del directorio **app/config** hay un archivo llamado **config.php** con un contenido que tiene unas contantes:

~~~
    <?php 

    // Raíz de la aplicación
    define('APPROOT', dirname(dirname (__FILE__)));
    // Url raíz
    define('URLROOT', 'http://localhost:8888/base');
    //nombre del sitio
    define('SITENAME', 'MikrotikPHP');
    define('ROOTFOLDER','/base/');
~~~

7. De esas constantes modificas su valor la constante **URLROOT**, y **ROOTFOLDER** por el nombre que tu le hayas puesto a la carpeta en **htdocs**. Donde **URLROOT** quedaría como **http://localhost/mikrovouchers** o **http://localhost:3030/mikrovouchers** si tu entorno de prueba de servidor requiere un puerto en especifico. La constante **ROOTFOLDER** solo tendría el nombre de la carpeta del proyecto **/mikrovouchers/**. Quedando así como se muestra:

~~~
    <?php 

    // Raíz de la aplicación
    define('APPROOT', dirname(dirname (__FILE__)));
    // Url raíz
    define('URLROOT', 'http://localhost/mikrovouchers');
    //nombre del sitio
    define('SITENAME', 'MikrotikPHP');
    define('ROOTFOLDER','/mikrovouchers/');
~~~

8. Por último y no menos importante, se requiere un router Mikrotik con el sistema RouterOS, porque se ocupará la API oficial para PHP para hacer cosas interesantes con este. Para este desarrollo se probó con un equipo similar al de la imagen.

![MikrotikRouter](https://i.mt.lv/cdn/rb_images/1284_hi_res.png)

Es requerido un router mikrotik, en teoria debe funcionar para todos los modelos, dado que todos son gobernados por RouterOS. Sí no se cuenta con un equipo real, es posible (creo yo) con GNS3 emular un router mikrotik.

