# Repository Information
Name: PI-Mikrotik

# Directory Structure
Directory structure:
└── github_repos/PI-Mikrotik/
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
    │   │       ├── pack-3bfe2fe8697e32c5fa06f93c5ffad1a9f98c575e.idx
    │   │       └── pack-3bfe2fe8697e32c5fa06f93c5ffad1a9f98c575e.pack
    │   ├── packed-refs
    │   └── refs/
    │       ├── heads/
    │       │   └── master
    │       ├── remotes/
    │       │   └── origin/
    │       │       └── HEAD
    │       └── tags/
    ├── Comprobaciones.md
    ├── Configuración_básica_de_la_Red.md
    ├── Configuración_Herramientas_Alta_Disponibilida.md
    ├── Configuración_Herramientas_Seguridad.md
    ├── Definiciones.md
    ├── Fase1_GNS3.md
    ├── Fase2_GNS3.md
    ├── Fase3_GNS3.md
    ├── imagenesGNS3/
    │   ├── GNSFase2/
    │   └── GNSFase3/
    ├── ImagenesPI/
    │   ├── PIFase2/
    │   ├── PIFase3/
    │   └── Suricata/
    ├── Lista_de_Pruebas.md
    ├── Planificación_de_la_Red_de_una_empresa.md
    ├── README.md
    ├── Recursos.md
    ├── Suricata_Mikrotik.md
    └── _config.yml


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
	url = https://github.com/FranciscoCadena/PI-Mikrotik.git
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
0000000000000000000000000000000000000000 7b60a13e92e58c69251c1fa9a370ef86800c91f1 vivek-dodia <vivek.dodia@icloud.com> 1738606410 -0500	clone: from https://github.com/FranciscoCadena/PI-Mikrotik.git


File: /.git\logs\refs\heads\master
0000000000000000000000000000000000000000 7b60a13e92e58c69251c1fa9a370ef86800c91f1 vivek-dodia <vivek.dodia@icloud.com> 1738606410 -0500	clone: from https://github.com/FranciscoCadena/PI-Mikrotik.git


File: /.git\logs\refs\remotes\origin\HEAD
0000000000000000000000000000000000000000 7b60a13e92e58c69251c1fa9a370ef86800c91f1 vivek-dodia <vivek.dodia@icloud.com> 1738606410 -0500	clone: from https://github.com/FranciscoCadena/PI-Mikrotik.git


File: /.git\packed-refs
# pack-refs with: peeled fully-peeled sorted 
0f088904d1384188ae427723ff956bcd49fb78c1 refs/remotes/origin/Mikrotik
7b60a13e92e58c69251c1fa9a370ef86800c91f1 refs/remotes/origin/master


File: /.git\refs\heads\master
7b60a13e92e58c69251c1fa9a370ef86800c91f1


File: /.git\refs\remotes\origin\HEAD
ref: refs/remotes/origin/master


File: /Comprobaciones.md
[Inicio](https://franciscocadena.github.io/PI-Mikrotik/)

# Comprobaciones

# Fase 1

## Comprobacion desde Cliente de Red

Para ello tan solo montamos un equipo en virtualbox, en este caso una ubuntu desktop, y lo fundamental es que en la parte de Red, esté en red interna y el nombre corresponda con la LAN a la cual hemos montado el servicio de dhcp. 

![Red interna cliente Virtualbox](./ImagenesPI/cliente.PNG "Red interna cliente Virtualbox")

En la configuración de la red lo dejamos todo en automático, en la pestaña de _ipv4_

![Configurar ip en automatico](./ImagenesPI/redcliente.PNG "Configurar ip en automatico")

Y luego en la pestaña de _detalles_ podemos ver como la ip, el gateway y el dns corresponde a lo que nosotros definimos previamente en el servidor de DNS

![IP del cliente dada por dhcp](./ImagenesPI/ipcliente.PNG "IP del cliente dada por dhcp")

Por último comprobamos que tiene ping desde la terminal y que puede navegar por internet.

![Ping a internet y navegación](./ImagenesPI/internetcliente.PNG "Ping a internet y navegación")

## Comprobacion desde Cliente de Red por vlan

Ahora probamos a entrar en un cliente desde la vlan 10, para ello desde virtualbox tendremos nuestra ova de CHR con una interfaz interna llamada vlan 10 como se muestra a continuación.

![Ruter red vlan en virtualbox](./ImagenesPI/routerredvlan.PNG "Ruter red vlan en virtualbox")

Y un ubuntu desktop con un interfaz que pertenezca a esa misma red interna

![Cliente red vlan en virtualbox](./ImagenesPI/clienteredvlan.PNG "Cliente red vlan en virtualbox")

Una vez dentro de nuestro SO de ubuntu vamo a la configuración de red para ver si nos ha dado nuestra ip por dhcp en la vlan 10

![IP en cliente por vlan](./ImagenesPI/clienteipvlan.PNG "IP en cliente por vlan")

También podemos comprobar desde Mikrotik que ha dado ip a un equipo yendo a la pestaña de __Leases__ desde la ventana de Dhcp server, donde nos da información del equipo como la ip que se le a asignado, la MAC, nombre del host del equipo, el tiempo en el que expira la ip arrendada, etc.

![Winbox ver arrendamiento de ip por dhcp](./ImagenesPI/dhcpiparrendada.PNG "Winbox ver arrendamiento de ip por dhcp")

Probamos a hacer ping desde la terminal.

![Ping a internet](./ImagenesPI/pingvlan.PNG "Ping a internet")

Y a navegar a internet.

![Navegar por internet](./ImagenesPI/internetvlan.PNG "Navegar por internet")

## Comprobaciones de reglas de firewall configuradas para la DMZ

#### Primero comenzaremos con el administrador de los servicios de la lan2 cuya ip es 192.168.20.2, el debe tener acceso a internet, poder hacer ping a la dmz, conectarse por ssh a la dmz, pero no debe tener acceso a la lan1.

![Lan2 salida a internet](./ImagenesPI/dmzinternet.PNG "Lan2 salida a internet")

Ping a uno de los servidores de la dmz

![Ping de lan a dmz](./ImagenesPI/dmzping.PNG "Ping de lan a dmz")

Conexión por ssh a uno de los servidores de la dmz

![Conexion por ssh a la dmz](./ImagenesPI/dmzssh.PNG "Conexion por ssh a la dmz")

No conexión con un trabajador de la lan1

![No hay ping a la lan1](./ImagenesPI/dmznopinglan1.PNG "No hay ping a la lan1")

#### En cambio el otro administrador de la lan2 cuya ip es 192.168.20.3 y que se encarga de la red lan1 si tendrá conexión a esta y a internet pero no a la dmz ni tampoco por ssh.

IP del administrador de la lan2 que se encarga de mantener la lan1

![IP del administrador de la lan2 que se encarga de mantener la lan1](./ImagenesPI/dmziplan2.PNG "IP del administrador de la lan2 que se encarga de mantener la lan1")

Sin conexión a la dmz

![Sin conexión a la dmz](./ImagenesPI/dmznopinglan2dmz.PNG "Sin conexión a la dmz")

Conexión a un trabajador de la red lan1

![Conexión a la red lan1](./ImagenesPI/dmzpinglan2lan1.PNG "Conexión a la red lan1")

#### Pruebas con un servidor de la dmz cuya ip será 192.168.30.3, que deberá tener acceso a internet, conexión con el administrador de servidor de la lan2, y todo lo demás denegado.

![IP de servidor de dmz](./ImagenesPI/dmzipserver.PNG "IP de servidor de dmz")

Ping con el Administrador de la red lan2

![Ping con el Administrador de la red lan2](./ImagenesPI/dmzpingdmzlan2.PNG "Ping con el Administrador de la red lan2")

No conexión con la red lan1

![No conexión con la red lan1](./ImagenesPI/dmznopingdmzlan1.PNG "No conexión con la red lan1")

#### Ahora probaremos que la red lan1 no tendrá conexión con nadie excepto con el administrador de la lan2, la ip de uno de los trabajadores de la lan1 será 192.168.10.254.

![IP de un equipo de la lan1](./ImagenesPI/dmziplan1.PNG "IP de un equipo de la lan1")

Sin conexión a la dmz

![Sin conexión a la dmz](./ImagenesPI/dmznopinglan1dmz.PNG "Sin conexión a la dmz")

Sin conexión al administrador de servidores de la lan2

![Sin conexión al administrador de servidores de la lan2](./ImagenesPI/dmznopinglan1lan2.PNG "Sin conexión al administrador de servidores de la lan2")

Sin conexión a internet

![Sin conexión a internet](./ImagenesPI/dmznopinglan1internet.PNG "Sin conexión a internet")

Conexión con el administrador de la red lan2 que mantiene la lan1

![Conexión con el administrador de la red lan2](./ImagenesPI/dmzpinglan1lan2admin.PNG "Conexión con el administrador de la red lan2")

#### Por último haremos la configuración de la última regla NAT que añadimos para hacer la comprobación de redirección de puertos, para ello podemos usar la máquina anfitriona en este caso una windows 10,  así que se realizará la prueba desde la powershell. 

![IP del equipo anfitrión de Windows 10](./ImagenesPI/dmzipanfitrion.PNG "IP del equipo anfitrión de Windows 10")

IP configuradas del router mikrotik donde podemos observar la ip de la wan y de las diferentes LANES

![IP del router](./ImagenesPI/dmzipsrouter.PNG "IP del router")

Ip del equipo servidor de la dmz al cual vamos a entrar por ssh

![Ip del equipo servidor de la dmz al cual vamos a entrar por ssh](./ImagenesPI/dmzipserverdmz.PNG "Ip del equipo servidor de la dmz al cual vamos a entrar por ssh")

Entrando por ssh al servidor de la dmz, usando la ip de la wan del router mikrotik

![SSH de anfitrión a dmz](./ImagenesPI/dmzsshanfitriondmz.PNG "SSh de anfitrión a dmz")

Comprobación de que estamos en el servidor de la dmz viendo su ip

![Comprobación de que estamos en el servidor de la dmz viendo su ip](./ImagenesPI/dmzipdmzanfitrion.PNG "Comprobación de que estamos en el servidor de la dmz viendo su ip")

Prueba con tracepath desde el servidor de la dmz estando por ssh desde el anfitrión

![Tracepath](./ImagenesPI/dmztracepath.PNG "Tracepath")

Prueba con traceroute desde el servidor de la dmz estando por ssh desde el anfitrión

![Traceroute](./ImagenesPI/dmztraceroute.PNG "Traceroute")

## Comprobaciones de vpn por ipsec

Una de las comprobaciones que podemos hacer para ver si el túnel funciona es desde Winbox vamos al menú izquierdo, hacemos clic donde dice __Tools__ y luego a __Ping__.
En esta ventana debemos definir en la pestaña _General_  en el apartado de _Ping To_, la dirección a la cual queremos hacer ping, que en este caso será la interfaz del gateway de la red local del router con el que hemos establecido el túnel, luego vamos a la pestaña de _Advanced_ y en el apartado de _Src. Address_ escribimos la ip de la interfaz del router donde nos encontramos ahora mismo que da a la red lan de este.
Una vez configurada ambas ip, le daremos al botón de Start y en la pantalla de abajo deberá verse si hay respuesta.

![Pestaña General, ip de la lan del router destino, conexión establecida](./ImagenesPI/ipsecping.PNG "Pestaña General, ip de la lan del router destino, conexión establecida")

![Pestaña Advanced, ip de la lan del router origen, conexión establecida](./ImagenesPI/ipsecping2.PNG "Pestaña Advanced, ip de la lan del router origen, conexión establecida")

La siguiente conexión será desde un cliente de una red a otro cliente de otra red lan diferente, en este caso la ip del cliente será 192.168.20.254 como se muestra en la siguiente imagen.

![IP de cliente](./ImagenesPI/ipsecipcliente.PNG "IP de cliente")

Y primero probaremos a hacer ping a la dirección 192.168.10.1 que corresponde a la interfaz de la lan del router que está al otro lado del túnel.

![Ping a la interfaz del ruter de la otra sede](./ImagenesPI/ipsecping3.PNG "Ping a la interfaz del ruter de la otra sede")

Y seguidamente haremos lo mismo pero con la ip de un cliente que pertenezca a la red lan que está al otro lado del túnel.

![Ping a un equipo de la otra sede](./ImagenesPI/ipsecping4.PNG "Ping a un equipo de la otra sede")

# Fase 2

## Comprobar Failover

Para realizar esta prueba entraremos por Winbox a uno de los router de la empresa, tendremos en pantalla, la terminal haciendo ping al 8.8.8.8 constantemente, la herramienta traceroute haciendo ping al 8.8.8.8 y la ventana de la lista de rutas.

![Conexión con el isp principal](./ImagenesPI/PIFase2/failoverprueba1.PNG "Conexión con el isp principal")

A continuación desconectamos el ISP1 que es el que definimos como principal, y observaremos como se pierde la conexión, hasta que pasado un tiempo se conectará automáticamente al ISP2 volviendo a tener conexión, no solo será visible porque vuelva a hacer ping al 8.8.8.8 desde la terminal, sino porque se verá reflejado en la ventana de Router list, cambiando de color la ruta que antes estaba en azul a negra y también cambiará la sigla definiendo que estará activa.

![Perdida de conexión con el isp principal](./ImagenesPI/PIFase2/failoverprueba2.PNG "Perdida de conexión con el isp principal")

![Reconexión con el isp secundario](./ImagenesPI/PIFase2/failoverprueba3.PNG "Reconexión con el isp secundario")

Por último volvemos a activar el ISP1 que antes se apagó, en cuanto se inicie deberá volver a pasar el la Route List como el principal, y en la ventana de traceroute, donde se perdió toda la conexión deberá de activarse nuevamente.

![Reconexión con el isp principal](./ImagenesPI/PIFase2/failoverprueba4.PNG "Reconexión con el isp principal")


## Comprobar VRRP

Para hacer la comprobación del vrrp , entraremos en un equipo cliente con SO Ubuntu desktop, comprobaremos su ip y gateway, para confirmar que está configurado según el Vrrp asociado al Router.

![Preparación de Prueba comprobando ip y gateway del equipo cliente](./ImagenesPI/PIFase2/vrrpprueba1.PNG "Preparación de Prueba comprobando ip y gateway del equipo cliente")

El siguiente paso será estar reproduciendo un video de youtube y estar haciendo ping al 8.8.8.8 continuamente desde el equipo cliente, también habrá  dos ventanas de Winbox donde veremos ambos router el maestro y el backup y dentro de cada una de estas ventanas veremos las ip e interfaces de ambos router, donde comprobaremos que el tráfico circula por el ether6-LAN del router maestro.

![Prueba de conexión](./ImagenesPI/PIFase2/vrrpprueba2.PNG "Prueba de conexión")

Seguidamente para no perder la conexión con Winbox del router maestro en vez de apagarlo desconectamos el interfaz ether6-LAN que es el que está conectado al equipo cliente.

![Desconectar interfaz ether6-LAN del router maestro](./ImagenesPI/PIFase2/vrrpprueba3.PNG "Desconectar interfaz ether6-LAN del router maestro")

Podemos comprobar como salta rápidamente el vrrp 1 del router backup, debido a que la respuesta es de unos 3 segundo, eso se puede confirmar viendo la ventana del equipo cliente que hace ping donde hay una parada de la secuencia del 41 al 45, apenas apreciable.
Acto seguido veremos como empieza a circular la conexión por el interfaz ether6-LAN del router backup.

![Activacion del router de respaldo por vrrp1](./ImagenesPI/PIFase2/vrrpprueba4.PNG "Activacion del router de respaldo por vrrp1")

Ahora volvemos a Conectar el cable ether6-LAN del router maestro.

![Conectar interfaz ether6-LAN del router maestro](./ImagenesPI/PIFase2/vrrpprueba5.PNG "Conectar interfaz ether6-LAN del router maestro")

Y en breves momento el vrrp 1 del backup vuelve a cambiar de negro a rojo, y la conexión vuelve a circular por el ether6-LAN del router maestro.

![Reconexión del vrrp1 del router maestro](./ImagenesPI/PIFase2/vrrpprueba6.PNG "Reconexión del vrrp1 del router maestro")

## Comprobar Ancho de Banda

Las pruebas se realizarán desde un Ubuntu desktop que se encuentre en la red LAN2, en la cual se mostrará en una imagen la ip del equipo que deberá corresponder con la de la red asignada, y el test de velocidad.

![Prueba de velocidad antes de la regla](./ImagenesPI/PIFase2/testvelocidad1.PNG "Prueba de velocidad antes de la regla.")

Seguidamente se realizará otro test de velocidad al mismo equipo con las reglas del ancho de banda ya definidas en el router y en donde deberá corresponder la ip del equipo a una de las reglas que se definen en el router.

![Prueba de velocidad después de la regla](./ImagenesPI/PIFase2/testvelocidad2.PNG "Prueba de velocidad después de la regla")

Como se observa en las imágenes anteriores, al principio tenia 1Mb de subida y bajada, y después con la regla que se definió en el router tiene una subida de  0.3Mb y una bajada de  0.8Mb.

## Comprobar balanceo de carga por PCC

Para esta comprobación se a partido de una ubuntu desktop, perteneciente a la red dmz, en la imagen se muestra que la ip del equipo corresponde a dicha red, también se verá en la imagen que hay dos pestañas de internet donde se reproducen videos por youtube y desde Winbox estando conectado al router principal que le da red a la dmz, debe haber fluido de paquetes por ambas interfaces WAN.
Lo que no se puede apreciar es la suma relativa del balanceo de carga en la interfaz que da red a la dmz, esto es debido a 2 factores:
- Como se está usando una virtualización con la OVA de CHR, está restringe la conexión a 1Mb
- También como es una virtualización se requiere dos proveedores de internet dando acceso a internet, cuando en este ejemplo solo se cuenta con la red de casa.

![Comprobacion de balanceo de carga con PCC](./ImagenesPI/PIFase2/pccprueba.PNG "Comprobacion de balanceo de carga con PCC")

# Fase 3

## Comprobar Port Knocking

Para realizar la comprobación del funcionamiento del port knocking primero mostraremos en una imagen las reglas creadas, para comprobar la cantidad de toques a realizar y por qué puertos debemos entrar. También se verán las interfaces e ip, en este caso nos conectaremos por la ip 192.168.0.23/24.

![Reglas firewall, interface he ip del router](./ImagenesPI/PIFase3/portknockingprueba1.PNG "Reglas firewall, interface he ip del router")

Luego estaremos en la pestaña de _address list_ estando conectado al router desde Winbox, he intentaremos por ssh y por winbox al router, dándonos error.  
 
![Error de conexión al router](./ImagenesPI/PIFase3/portknockingprueba2.PNG "Error de conexión al router")

En la siguiente imágenes veremos como vamos paso por paso conectándonos por ssh a los puertos definidos en las reglas, y la ip de nuestra máquina anfitriona irá apareciendo en la addresslist que corresponde a cada regla definida.

Primer toque, puerto 2000

![Llamando al puerto 2000](./ImagenesPI/PIFase3/portknockingprueba3.PNG "Llamando al puerto 2000")

Segundo toque, puerto 4000

![Llamando al puerto 4000](./ImagenesPI/PIFase3/portknockingprueba4.PNG "Llamando al puerto 4000")

Tercer toque, puerto 8000

![Llamando al puerto 8000](./ImagenesPI/PIFase3/portknockingprueba5.PNG "Llamando al puerto 8000")

Una vez que esté en la última address list podremos entrar por ssh sin tener que definir ningún puerto. 
También se puede ver el tiempo que estará la ip de nuestra máquina anfitriona en cada address list, cuando expire el tiempo de la última address list, la que da acceso seguro para entrar al router, nos echara del router, teniendo que repetir la secuencia.

Conexión por ssh sin necesidad del puerto porque ya está en la address list que tiene permiso de conexión.

![Entrando al router sin necesidad de puertos por estar en la lista de direcciones con permisos](./ImagenesPI/PIFase3/portknockingprueba6.PNG "Entrando al router sin necesidad de puertos por estar en la lista de direcciones con permisos")

Dentro de Mikrotik desde SSH, para confirmarlo se puede observar el nombre del router, las interfaces e ip tanto en el lado del winbox a la izquierda como en el lado de la conexión por ssh a la derecha de la imagen.

![Conexión establecida por ssh, y comprobación de que estamos en el router, mostrando sus ip e interfaces](./ImagenesPI/PIFase3/portknockingprueba7.PNG "Conexión establecida por ssh, y comprobación de que estamos en el router, mostrando sus ip e interfaces")

__Nota__ el cambio de color del powershell es debido a que una vez dentro de Mikrotik por ssh no se veía bien las letras, de hay que haya pasado a otro color.

## Comprobar el envío de correo por gmail

Para probar que funciona correctamente el envío de correo vamos a __Tools → Email__ y en la ventana que aparece le damos a _Send Email_, nos aparecerá una nueva ventana, rellenamos los campos en donde los primeros hacen referencia a nuestra cuenta con mikrotik, y luego definimos a qué correo se lo vamos a enviar y quien se lo envía, tal como se muestra en la siguiente imagen.

![Envió de correo manualmente desde Mikrotik](./ImagenesPI/PIFase3/gmailmikrotik2.PNG "Envió de correo manualmente desde Mikrotik")

Después de darle a enviar revisamos nuestro correo para ver si nos ha llegado el mensaje y comprobar que funciona correctamente.

![Correo recibido](./ImagenesPI/PIFase3/gmailmikrotik3.PNG "Correo recibido")

## Comprobar el envío de logs asignados

Como prueba para ver si funciona el aviso de errores y dhcp creadas en el router vamos a tener abierto los logs, las reglas creadas y vamos a desconectar uno de los interfaces wan que están como dhcp cliente.

![Prueba de envío de errores por correo](./ImagenesPI/PIFase3/gmailerror7.PNG "Prueba de envío de errores por correo")

Como vemos en el logs se a enviado un correo para notificarnos de un problema de dhcp.

![Desconexión del interfaz 3, y comprobación del envío de correo desde el log](./ImagenesPI/PIFase3/gmailerror8.PNG "Desconexión del interfaz 3, y comprobación del envío de correo desde el log")

Si ahora vamos a nuestro correo podemos ver como nos han llegado varios correos avisandonos de lo ocurrido en el router tanto con el servicio de dhcp como con la interfaz, dándonos diversos detalles cada correo.

![Comprobación de la llegada de los correos ](./ImagenesPI/PIFase3/gmailerror9.PNG "Comprobación de la llegada de los correos ")

## Comprobar la automatización de envios de Backups

Para probar de que tanto los script creados como las tareas programadas funcionan correctamente podemos modificar la hora de uno de los archivos para que correspondan con la hora que tenemos en ese momento.

![Modificar horario de la tarea para que concuerde con la hora actual](./ImagenesPI/PIFase3/respaldo8.PNG "Modificar horario de la tarea para que concuerde con la hora actual")

O bien desde la ventana de los Script podemos seleccionar uno de ellos y luego darle al botón de __Run Script__.

![Activar el Botón Run Scrip](./ImagenesPI/PIFase3/respaldo10.PNG "Activar el Botón Run Script")

El _Run Count_ corresponde a las veces que se a enviado por correo el script, o las veces que este se a ejecutado.
Hay que tener en cuenta que en el periodo de tiempo que definimos en las tareas es posible que de error o que no llegue algun correo si ambos _script_ deben ser enviados al mismo tiempo, por lo que recomiendo darle un margen entre un correo y otro.
 
A continuación comprobamos los correos que nos han llegado.

![Correos recibidos del router con las tareas programadas](./ImagenesPI/PIFase3/respaldo11.PNG "Correos recibidos del router con las tareas programadas")

Y el archivo que nos ha llegado de este

![Archivo de Bachup dentro del correo que ha llegado desde el router](./ImagenesPI/PIFase3/respaldo9.PNG "Archivo de Bachup dentro del correo que ha llegado desde el router")

## Comprobar funcionamiento de suricata

Vamos a probar el funcionamiento de suricata, para ello primero veremos los diferentes log de suricata y que nos aporta cada uno de ellos.
- __suricata.log:__ Recoge los eventos del mismo Suricata: inicializaciones, recargas, errores, etc.
- __stats.log:__ Recoge estadísticas regulares acerca del tráfico que se ha ido analizando hasta el momento.
- __fast.log:__ Recoge los eventos disparados por las reglas. Tiene como objetivo dar una impresión rápida y directa de los eventos.
- __eve.json:__ Recoge, igual que el anterior, los eventos disparados por las reglas, pero lo hace en formato JSON, lo que permite que posteriormente pueda ser interpretado de forma mucho más fácil por programas externos.

Bien una vez explicado un poco los diferentes archivos log, para hacer una pequeña prueba crearemos nuestra propia regla, para ello podemos hacerlo de varias formas la mas logica es crear un archivo de texto nuevo en la ruta por defecto que usa actualmente suricata la cual es _/var/lib/suricata/rules_, o también podemos crear un fichero de texto en la ruta /etc/suricata/rules la cual se crea automáticamente al instalar el _suricata-update_ el problema de esto es que deberemos especificar la ruta de este en el archivo de configuración de suricata en el apartado de __default-rule-path__, por ello es más recomendable crearlo en la ruta por defecto de _/var/lib/suricata/rules_.

![Creando el archivo custom.rules](./ImagenesPI/Suricata/crearcustomrules.PNG "Creando el archivo custom.rules")

Una vez creado el archivo de texto el cual podemos definir como _custom.rules_, dentro de este agregamos la siguiente línea __“alert icmp any any -> any any (msg: "ICMP detected"; sid: 1000001;)”__ salimos y guardamos, la regla anterior lo que hará será crear una alerta (visible en los logs) cada vez que detecte un paquete ICMP.

![Insertando la regla en custom.rules](./ImagenesPI/Suricata/reglamanual.PNG "Insertando la regla en custom.rules")

Una vez creada la alerta la definiremos en el archivo de configuración __suricata.yaml__, buscamos _rule-files_, y añadimos nuestra regla la cual definimos como _custom.rules_ debajo de _suricata.rules_.
Guardamos el archivo y reiniciamos suricata para que cargue las reglas nuevas.

![Agregando la regla creada manualmente al archivo suricata.yaml](./ImagenesPI/Suricata/agregarcustomrules.PNG "Agregando la regla creada manualmente al archivo suricata.yaml")

Ahora arrancamos suricata con el siguiente comando
~~~
suricata -c /etc/suricata/suricata.yaml -i enp0s3
~~~

Con la opción _-c_ definimos la ruta del archivo de configuración, y con _-i_ definimos que corra en modo PCAP, con lo que le definimos el nombre de la interfaz que en caso es enp0s3

__Nota__. Es conveniente antes de ejecutar el comando anterior desactivar las funciones de descarga de paquetes en la interfaz de red en la que escucha Suricata con el siguiente comando.
~~~
ethtool -K enp0s3 gro off lro off
~~~

Si no tenemos la herramienta ethtool, la podemos instalar con.
~~~
sudo apt-get install ethtool
~~~

![Instalación de la herramienta ethtool](./ImagenesPI/Suricata/instalarethtool.PNG "Instalación de la herramienta ethtool")

Si al ejecutar el comando nos aparece una línea comentando _Cannot change large-receive-offload_ significa que nuestra interfaz no es compatible con esta función y por tanto la  ignorara. 
Sin embargo, podemos verificar esto ejecutando el siguiente comando.
~~~
ethtool -k enp0s3 | grep large
~~~
El cual nos deberá responder con.
~~~
large-receive-offload: off [fixed]
~~~

![Ejecución de los comandos ethtool](./ImagenesPI/Suricata/ethtool.PNG "Ejecución de los comandos ethtool")

Una vez realizado y confirmado lo anterior ejecutamos el comando
~~~
suricata -c /etc/suricata/suricata.yaml -i enp0s3
~~~

![Arrancando suricata en modo PCAP](./ImagenesPI/Suricata/suricatapcap.PNG "Arrancando suricata en modo PCAP")

Y abrimos dos terminales nuevas, en una de ellas ejecutaremos el comando __tail -f /var/log/suricata/fast.log__ y en la otra terminal ejecutamos el comando __tail -f /var/log/suricata/eve.json__.

Teniendo todo listo abrimos una nueva terminal y hacemos ping al 8.8.8.8 por ejemplo o también podemos hacer ping desde un equipo diferente al equipo que tenga instalado suricata, si todo ha ido bien nos debería de saltar la información de los icmp capturados.

Ping al 8.8.8.8 desde la misma maquina.

![Prueba ping 8.8.8.8 desde mismo equipo](./ImagenesPI/Suricata/pruebasuricata1.PNG "Prueba ping 8.8.8.8 desde mismo equipo")

Ping desde un windows 10 al equipo que tiene instalado suricata con ip 192.168.0.23.

![Prueba ping desde diferente equipo a Suricata](./ImagenesPI/Suricata/pruebasuricata2.PNG "Prueba ping desde diferente equipo a Suricata")

## Comprobar funcionamiento de Suricata junto a Mikrotik

Para realizar la prueba partiremos del diagrama de la Fase 2 con los equipos Suricatas vinculados cada uno al router master y otro al router backup.

![Diagrama fase2 con Suricatas conectados a los Routers](./ImagenesPI/Suricata/fase3-suricata.PNG "Diagrama fase2 con Suricatas conectados a los Routers")

Una vez configurado Mikrotik, volvemos a nuestro Suricata, lo primero será crear una carpeta, por ejemplo dentro de la carpeta mikrotik creada donde nos descargamos la herramienta trafr, a la cual llamaremos _registros_.

![Creando carpeta registro y cambiando a root](./ImagenesPI/Suricata/suricataprueba1.PNG "Creando carpeta registro y cambiando a root")

Dentro de esta carpeta ejecutamos el siguiente comando estando como _root_ ya que las reglas de suricata están en un directorio donde solo tiene acceso el root.
__/usr/local/bin/trafr -s | suricata -c /etc/suricata/suricata.yaml -v -r /dev/stdin__
Con ello arrancamos la herramienta trafr que se encuentra actualmente en /usr/local/bin, y lo que recoge se lo envía a suricata el cual estará corriendo en modo pcap, enviando todo al directorio definido con la opción -r y procesandolos en orden.
El motivo de ejecutar el comando en la carpeta creada es porque al usar la opción -r en modo pcap (offline), suricata crea nuevos archivos .log en la ruta donde se ejecuta ese comando, por lo tanto en vez de visualizar los archivos de suricata que por defecto están en la ruta _/var/log/suricata_ visualizamos los nuevos creados.

![Nuevos Logs creados al ejecutar Suricata en la carpeta registros](./ImagenesPI/Suricata/nuevoslogs.PNG "Nuevos Logs creados al ejecutar Suricata en la carpeta registros")

Abrimos dos nuevas terminales, y nos dirigimos a la ruta _/mikrotik/registros_, para poder ver el tráfico que llega podemos usar 
~~~
File: /Configuración_básica_de_la_Red.md
[Inicio](https://franciscocadena.github.io/PI-Mikrotik/)

# Datos del documento

En este documento veremos lo siguiente:
- Tipos de licencia de Mikrotik 
- Donde descargar el CHR de Mikrotik y la herramienta de Winbox
- Conectarnos a mikrotik por Winbox
- Cambiar nombre de usuario y pass al acceder a mikrotik
- Resetear nuestro router
- Configuración de Dhcp cliente y servidor
- Donde se configura el Dns y el gateway
- Nombrar y crear ips
- Crear vlans y hacerlo con un solo router
- Crear un Vpn con protocolo IPsec
- Configurar reglas de Firewall para una DMZ

## Licencias Mikrotik, RouterOS y Winbox

Nuestro primer paso será ir a la página oficial de [Mikrotik](https://mikrotik.com/download), una vez dentro vamos a la pestaña de Software y luego a Download, aquí hay que tener algo en cuenta, el sistema operativo __RouterOS__ va por licencias, aquí podemos ver los distintos tipos de licencia y lo que nos ofrece cada una sacada directamente de la página oficial de mikrotik.

![Tabla de las distintas licencias de Mikrotik](./ImagenesPI/License.PNG "Tabla de las distintas licencias de Mikrotik")

Como vemos hay una licencia gratuita en plan de demostración, pero como es de prueba no trae todas las características, hay que tener en cuenta que estas licencias solo es necesario comprarlas si queremos su software para tener un PC como enrutador, ya que los diferentes productos de Hardware de mikrotik al comprarlos ya te vienen con un nivel de licencia el cual te lo especifican en sus características. Esto es algo importante porque en varios videotutoriales no te lo especifican, usando licencias de prueba o algunos que ya tienen comprado sin especificarlo.

Por lo tanto nosotros debemos descargar el __Cloud Host Router__, que no es más que una versión gratuita con todas las herramientas del RouterOS con la única pega de que la velocidad de Navegación será de 1 MB, esta versión te viene en varios formatos para poder ser virtualizado, por ello descargamos la versión OVA template para que sea reconocida por Virtualbox y de ellas la versión Stable.

![Imagen con las diferentes imágenes de CHR y sus versiones para descargar](./ImagenesPI/CHR.PNG "Imagen con las diferentes imágenes de CHR y sus versiones para descargar")

Una vez descargada el procesos para instalarlo en Virtualbox es el mismo que el de cualquier OVA importada, en cuanto la ova este importada tan solo deberemos definir las interfaces de red que vamos a usar que en este caso usaremos las 4, y definimos de qué tipo serán con lo que la ether 1 será la WAN así que la dejaremos en modo bridge para que coja la ip por DHCP de nuestro router de casa, y las otras 3 interfaces las pondremos como redes internas para la DMZ y las 2 redes LAN.

En cuanto lo tengamos listo la encendemos. Y lo primero que nos pedirá será el login, el cual por defecto será __admin__ y de password ninguno.

![Login Terminal RouterOS](./ImagenesPI/Login.PNG "Login Terminal RouterOS")

En cuanto entremos podemos observar que es una terminal que trabaja por línea de comando, debido a que su infraestructura deriva de Linux, en la siguiente imagen con el comando __ip address print__ podemos ver que la interfaz que se definió como puente en virtualbox ya tiene una ip asignada.

![Terminal ip address print](./ImagenesPI/adresprint.PNG "Terminal ip address print")

Y si usamos el comando __interface print__ nos dara informacion de todas las interfaces conectadas.

![Terminal interface print](./ImagenesPI/interfaceprint.PNG "Terminal interface print")

El hecho de que el Software de mikrotik trabaje por línea de comandos tiene sus partes positivas y negativas.

Como parte negativas, nos encontramos que debemos aprender nuevos comandos, y también según algunos administradores de redes de foros que algunas configuraciones avanzadas deben hacerse vía CLI, de ahí que mikrotik al igual que Cisco tengan sus propios cursos y certificados para aprender todo lo que nos puede ofrecer. 

Como parte positiva, podemos crear script para automatizar tareas o incluso para cargar configuraciones de red si estas son las mismas o similares, desde github muchas personas ponen a disposición de todos, script para realizar múltiples tareas y diferentes configuraciones.

Pero Mikrotik también puede ser configurado de forma gráfica, vía web o con herramientas como __Winbox__ la cual será la que usaremos.

Para ello podemos descargar Winbox desde la propia página de [Mikrotik](https://mikrotik.com/download), tan solo debemos elegir la versión de 32 o la de 64 bit, una vez descarga su instalación es muy simple tan solo hay que elegir la ruta donde se instalará y darle a siguiente.

![Descargar WinBox](./ImagenesPI/winboxdownload.PNG "Descargar WinBox")

En cuanto abrimos Winbox nos aparecerá una pantalla como la siguiente en la cual el mismo empezará a rastrear los diferentes equipos de Mikrotik que haya. 

![Entrar por MAC](./ImagenesPI/WBlogin.PNG "Entrar por MAC")

Como observamos en las imágenes ha detectado 2 equipos de Mikrotik, que en este caso ambos son CHR, pero uno tiene IP y el otro no, esto se debe porque al bajar la OVA de CHR ya está configurado para que de IP pero la otra OVA como a sido reseteada pierde esa configuración que trae por defecto, pero Winbox puede entrar directamente por la MAC, y una vez dentro ya configurar la ip de las Interfaces, y luego ya entrar por la ip, nombre de admin y password que hayamos definido en su primera configuración.

![Entrar por IP](./ImagenesPI/WBlogin2.PNG "Entrar por IP")

Una vez seleccionado un equipo le damos a __Connect__ y nos aparecerá la pantalla principal de Winbox que es la siguiente.

![Winbox Interface](./ImagenesPI/WBindex.PNG "Winbox Interface")

Prácticamente en el menú izquierdo tendremos todas las herramientas necesarias para hacer las configuraciones necesarias a nuestro Router. 

## Configuración 

### Reset

Como primeros pasos empezaremos por resetear la configuración del router, para ello desde el menu izquierdo vamos a __System → Reset__ Configuration
En la nueva ventana marcamos las casillas No Default Configuration y Do Not Backup, y luego le damos al botón de __Reset Configuration__

![Reseteo de Routeros](./ImagenesPI/Reset.PNG "Reseteo de Routeros")

### Login y Password

Nuestro siguiente paso será darle un nombre de usuario y una contraseña, para ello vamos a __System → Users__ y nos aparecerá el usuario admin que viene por defecto, vamos a  agregar un nuevo usuario dándole al símbolo del más, le damos un nombre, contraseña y lo metemos en el grupo de full para que tengo los privilegios de un admin. Le damos al botón de Apply y luego a OK, una vez creado marcamos al usuario admin y lo podemos eliminar o deshabilitar, pulsando el botón menos o la cruz respectivamente.

![Usuario y Pass](./ImagenesPI/Userpass.PNG "Usuario y Pass")

Ahora si nos desconectamos y nos volvemos a conectar veremos que nos impedirá entrar con el user admin, teniendo que usar nuestro nuevo usuario creado. Para desconectarnos tan solo le damos al botón __Session__ de la barra de herramientas y luego a __Disconnect__.

![Error al conectarse](./ImagenesPI/erropass.PNG "Error al conectarse")

### Nombrar Interfaces

El siguiente paso que vamos a hacer es definir las interfaces dando a cada una un nombre para poder diferenciarlas y que correspondan con lo definido en las interfaces de virtualbox.
Para ello tan solo debemos hacer doble clic en cada interfaz y darle un nombre en la ventana que nos aparecerá y luego a OK.
Si por el motivo que sea no tenemos la ventana de las interfaces que sale por defecto al iniciar Winbox, tan solo debemos hacer clic a donde dice __Interfaces__ en el menú izquierdo.

![Nombrear interfaz de WAN](./ImagenesPI/wan.PNG "Nombrear interfaz de WAN")

![Interfacez nombradas](./ImagenesPI/interfaces.PNG "Interfacez nombradas")

Hay que tener en cuenta que todo lo que estamos haciendo en Winbox directamente lo podemos ver reflejado en la terminal del RouterOS por ello si abrimos una terminal desde Winbox dándole a __New terminal__ desde el menú izquierdo y ejecutamos el comando antes usado de __interface print__ veremos como ahora todas las interfaces están nombradas.

![Terminal en Winbox](./ImagenesPI/WBterminal.PNG "Terminal en Winbox")

### WAN por DHCP

El siguiente paso será darle ip a la WAN, como está configurado como modo puente en virtualbox, haremos que reciba la ip en modo cliente DHCP y que sea el Router de casa el que se lo facilite.
Para ello en el menu izquierdo vamos a __IP → DHCP Cliente__, en la nueva ventana le damos al símbolo del más, y en la nueva ventana seleccionamos la interface que en este caso será la WAN y le damos al botón de OK.

![Configurando DHCP cliente en la WAN](./ImagenesPI/dhcpcliente.PNG "Configurando DHCP cliente en la WAN")

![WAN configurada y con ip dada por dhcp](./ImagenesPI/wandhcp.PNG "WAN configurada y con ip dada por dhcp")

### IP estaticas

Hemos visto que la WAN la hemos dejado como cliente de dhcp, pero si fuese un ISP con un ip publica estatica tambien se puede hacer, mostraremos cómo se realiza y de paso configuraremos ip estáticas para las redes LAN y la DMZ.
Para ello vamos al menú izquierdo, le damos a __IP → Addresses__, nos aparecerá una ventana donde estará solo la ip de wan dada por dhcp, así que nosotros le damos al símbolo del mas para agregar una ip.

![IP dinamica de la WAN](./ImagenesPI/ipwan.PNG "IP dinamica de la WAN")

Al darle al símbolo del mas, en la nueva ventana que nos aparece debemos definir la interfaz a la cual le vamos a dar la ip, escribimos su ip en addresses con su máscara de red y al darle a aplicar ya rellenara Winbox el apartado de Network definiendo la red a la que pertenece. Esto lo haremos con todas las interfaces de las LAN y la DMZ, si nuestro Router es un ISP y tiene una ip pública la definimos aquí, como no es el caso podemos dejarlo como cliente de dhcp. 

![Configurar ip estatica](./ImagenesPI/ipestatica.PNG "Configurar ip estatica")

Una vez todas las interfaces configuradas con su ip nos quedaría de esta manera.

![IPs configuradas](./ImagenesPI/ipslanes.PNG "IPs configuradas")

### Configurar enmascaramiento

Para ello desde el menú izquierdo debemos ir a __IP → Firewall__, una vez aquí vamos a la pestaña de __NAT__, y le damos al botón de más.

![Firewall NAT](./ImagenesPI/NAT.PNG "Firewall NAT")

En la nueva ventana estando en la pestaña de __general__, debemos asegurarnos que donde dice _chain_ este __srcnat__ que es lo mismo que source nat, y en out interface debe ser la __WAN__.  

![srcnat](./ImagenesPI/scrnat.PNG "srcnat")

Seguidamente vamos a la pestaña de Action, y donde dice Action debemos seleccionar masquerade.

![masquerade](./ImagenesPI/masquerade.PNG "masquerade")

Al final le damos a Apply y luego a OK

![enmascaramiento configurado](./ImagenesPI/natconfi.PNG "enmascaramiento configurado")

### Gateway

Para configurar la ruta de enlace por defecto, vamos al menú izquierdo, y le damos a __IP → Route List__, al tener la WAN por dhcp Winbox ya lo tendrá configurado por defecto, pero si tenemos que hacerlo de forma manual, tan solo le damos al símbolo del mas, y en la nueva ventana definimos el gateway que en este caso es el Router de casa, y las direcciones ip las dejamos en 0.0.0.0/0 para definir que son todas, aplicamos y le damos a ok.

![Gateway](./ImagenesPI/gateway.PNG "Gateway")

### DNS

Para configurar los DNS tan solo debemos ir desde el menú izquierdo a __IP → DNS__, donde en server podemos añadir los dns que queramos, en este ejemplo se están usando las dns públicas de google, para añadir más tan solo le damos a la flecha de abajo que hay justamente a la derecha de la pantalla del server, con ello se abrira otra pestaña para agregar otra dirección dns.
Si marcamos la opción de Allow Remote Requests, eso hará que nuestro dispositivo Mikrotik pase a ser un servidor dns para toda nuestra red LAN. Aplicamos y le damos a OK.

![DNS](./ImagenesPI/dns.PNG "DNS")

Ahora podemos probar si nuestro equipo Mikrotik tiene salida a internet, desde Winbox podemos abrir una terminarl y hacer ping a [Google](www.google.es) por ejemplo como se muestra en la imagen siguiente.

![Ping desde terminal de winbox](./ImagenesPI/ping1.PNG "Ping desde terminal de winbox")

### DHCP server

Ahora vamos a montar un servicio dhcp para los clientes de la LAN, esto es opcional ya que como anteriormente configuramos nuestra ip estática a cada interfaz correspondiente a cada LAN podríamos ir a cada equipo cliente de la LAN y establecer una ip estática definiendo su gateway que corresponda con los definidos en nuestro equipo Mikrotik.
Para crear nuestro servicio dhcp vamos desde el menú izquierdo a __IP → DHCP server__.

![Dhcp server](./ImagenesPI/dhcp.PNG "Dhcp server")

En esta ventana podemos darle al botón del mas y se nos abrirá una ventana donde configuramos los parámetros de nuestro servidor dhcp, como el nombre, que interfaz será la que tendrá el servicio de dhcp, el tiempo de concesión de la ip, el rango de ip, etc.

![Configurar Dhcp server](./ImagenesPI/dhcpserver.PNG "Configurar Dhcp server")

Pero también tenemos una forma de hacerla de forma guiada para ello le damos en vez de al boton mas al boton que dice DHCP Setup.

![Dhcp setup LAN](./ImagenesPI/dhcpsetup.PNG "Dhcp setup LAN")

Como vemos en la imagen lo primero que nos pedirá es que interfaz corresponderá al servicio de dhcp, en este ejemplo usamos la LAN1 y luego le damos a Next.

![Dhcp setup Red](./ImagenesPI/dhcpsetup2.PNG "Dhcp setup Red")

A continuación nos saldrá la dirección de red que corresponderá con el servidor de dhcp, dejamos la que viene por defecto y le damos a Next.

![Dhcp setup gateway](./ImagenesPI/dhcpsetup3.PNG "Dhcp setup gateway")

La siguiente pantalla hace referencia a cuál será el gateway de dicha red, comprobamos que sea correcta, con la ip que definimos para la red lan 1 y le damos a next.

![Dhcp setup rango](./ImagenesPI/dhcpsetup4.PNG "Dhcp setup rango")

La siguiente ventana es para definir el rango de ip que dará el servicio dhcp, como ejemplo podemos definir que de ip desde .100 hasta la .254 dejando un rango de ip libres por si necesitamos montar algún equipo con una ip fija.

![Dhcp setup dns](./ImagenesPI/dhcpsetup5.PNG "Dhcp setup dns")

La siguiente ventana hace referencia a los servidores de DNS que usará, en los cuales los 2 primeros hacen referencia a los que nos proporciona el Router de casa, y los 2 siguientes a los que nosotros añadimos cuando configuramos el DNS.

![Dhcp setup arrendamiento](./ImagenesPI/dhcpsetup6.PNG "Dhcp setup arrendamiento")

Por último nos preguntará el tiempo de arrendamiento de la ip de nuestro cliente.

![Dhcp setup configurado](./ImagenesPI/dhcpsetup7.PNG "Dhcp setup configurado")

Con el último paso ya habremos terminado de montar nuestro servicio de dhcp ahora solo queda montar un equipo de la LAN1 y ver si recibe una ip del rango definido y que tenga salida a internet.

## Vlan

Nuestro siguiente paso será crear redes virtuales para una LAN, por ejemplo supongamos que en una empresa en una misma LAN hay varios sectores por ejemplo: un grupo de Recursos Humanos, otro grupo de Administrativos, otro de Secretarios. Y para cada uno de estos grupos nombrados queremos que aunque estén en la misma red tengan sus propias redes diferenciadas una de las otras, pues para ello crearemos las Vlan, RouterOS admite __hasta 4095 interfaces vlan__, cada una con una ID de vlan única, por interfaz.

Para guiarnos nos fijamos en el siguiente diagrama en donde habrá 3 equipos en una misma LAN, pero cada uno tendrá su propia vlan diferenciada, por lo tanto configuraremos el Router con las 3 vlan en la interfaz de la LAN1, y luego para simular el switch lo haremos otro RouterOS donde designaremos cada vlan a un interfaz en modo bridge.

![Diagrama de red simple con 3 Vlan](./ImagenesPI/redvlanes.PNG "Diagrama de red simple con 3 Vlan")

Primero vamos al Router que terminamos de configurar al principio, nos vamos a interfaces desde el menu izquierdo, vamos a la _pestaña de Vlan_ y  le damos al símbolo más.

![Crear Vlan](./ImagenesPI/vlan1.PNG "Crear Vlan")

En esta nueva ventana definimos el nombre de la vlan, el tipo que será una vlan, su identificador, y a que interfaz irá vinculada. Terminado le damos a Apply y luego a OK.

![Crear Vlan30](./ImagenesPI/vlan30.PNG "Crear Vlan30")

Una vez configurada las 3 vlan, debemos darle sus ip, para ello desde el menu izquierdo vamos a __IP → Addresses__. le damos al símbolo del mas, y seleccionamos cada una de las vlan creadas y le damos una ip por ejemplo: 
- Vlan10 → 10.10.10.1
- Vlan20 → 20.20.20.1
- Vlan30 → 30.30.30.1

![Direccionamiento de las Vlan](./ImagenesPI/ipvlan.PNG "Direccionamiento de las Vlan")

Terminada la configuración  del router, lo que faltaria hacer seria conectar la interfaz del Router que corresponde a la LAN1 al interfaz principal del Switch. Hecho esto entramos en el Switch por el RouterOS para configurarlo.

El primer paso será parecido al realizado en el Router, vamos a seleccionar la interface ether1 que será la conectada al router y crearemos las 3 vlan que creamos en el Router. Como en el paso anterior le damos al símbolo del más estando en la ventana de las interfaces, y después a Vlan, y rellenamos los campos como hicimos en el Router, hasta tener las 3 vlan creadas.

![Crear vlan 10](./ImagenesPI/crearvlan10.PNG "Crear vlan 10")

![Creadas las 3 vlanes](./ImagenesPI/vlans.PNG "Creadas las 3 vlanes")

Una vez creada las vlan vamos a vincularla cada una con un interfaz del switch para eso haremos un bridge, con lo que nuestro siguiente paso será ir al menú izquierdo y luego a Bridge, y seguidamente al símbolo más para crearlo.

![Crear bridge](./ImagenesPI/bridge.PNG "Crear bridge")

Creamos 3 Bridge una para cada vlan anteriormente creada, tan solo definimos el nombre y le damos a OK.

Ahora estando en la misma ventana del __bridge__ cambiamos de pestaña yendo a _Ports_, y seguidamente le damos al símbolo más.
En la ventana que nos aparecerá, será donde definamos cada vlan con su correspondiente bridge y seguidamente ese mismo bridge con su interfaz, veamos el ejemplo con la vlan 10.

Primero en interfaz seleccionamos la vlan10_RH y en bridge seleccionamos bridge10_RRHH, aplicamos y luego ok.

![Bridge con vlan](./ImagenesPI/vlanbridge.PNG "Bridge con vlan")

Volvemos a darle al símbolo de más y ahora en interfaz seleccionamos ether2, y en bridge volvemos a elegir bridge10_RH.

![Bridge con interfaz](./ImagenesPI/etherbridge.PNG "Bridge con interfaz")

Ahora realizaremos los mismos pasos para unir el _ether3 con la vlan20_Secre y el Bridge20_Secretariado_, y después unimos el _eher4 con la vlan30_Admin y el bridge30_Administrativo_. Quedando al final todo como se muestra en la siguiente imagen.

![Todos los bridges creados](./ImagenesPI/bridgecreada.PNG "Todos los bridges creados")

Ahora con esta configuración cuando conectemos un PC al ether2 del switch corresponderá al vlan 10, si lo conectamos al ether3 corresponderá a la van 20, etc.

### Crear vlan solo en un Router

Si por el contrario en vez de tener un router y un switch solo tenemos un Router, el procedimiento sería muy parecido cambiando un par de cosas. Partiremos con la configuración que hicimos en la OVA de CHR que configuramos como Switch, con la diferencia de que ahora ether 1 no estará conectado a un Router sino a un ISP o en este caso al Router de casa, por lo tanto lo configuraremos como dhcp cliente.
Eso quiere decir que iremos al menú izquierdo y luego a __IP → Dhcp cliente__, le damos al símbolo más, seleccionamos el interface ether1 y le damos a ok, tal y como se ve en la siguiente imagen.

![Dhcp cliente de ether1](./ImagenesPI/dhcpcliente2.PNG "Dhcp cliente de ether1")

Como hemo dicho las vlan y los bridge ya están creadas porque partimos de la ova que antes configuramos, solo hemos cambiado de momento que el ether 1 reciba la ip por dhcp.

![Brige y vlan creadas](./ImagenesPI/bridgeyvlan.PNG "Brige y vlan creadas")

Ahora lo que debemos hacer es darle un direccionamiento a los bridge, para ello vamos al menú izquierdo, __IP → Addresses__ e iremos seleccionando cada uno de los Bridge y le daremos una IP, __OJO__ al asignarle la ip al bridge, hará que tanto la interfaz como la vlan puedan ver esa ip incluso si luego le configuramos dhcp.

![Dando ip al bridge](./ImagenesPI/ipbridge.PNG "Dando ip al bridge")

![Configuradas las ips para los 3 bridge](./ImagenesPI/ipsbridges.PNG "Configuradas las ips para los 3 bridge")

Ahora podemos dejar la configuración como está asignando una ip fija a cada equipo que se conecte a cada vlan, o podemos establecer un servicio dhcp a cada bridge, así que vamos a hacerlo.
Como siempre vamos al menú izquierdo, luego a __IP → Dhcp server__, y luego al símbolo más o al dhcp setup para que nos guíe el asistente, los pasos serán los mismos que los vistos anteriormente cuando configuramos el dhcp server con lo cual pasaremos a mostrar las capturas de imagenes de como seria la configuración.

![Interfaz del server](./ImagenesPI/dhcpbridge1.PNG "Interfaz del server")

![Red del dhcp](./ImagenesPI/dhcpbridge2.PNG "Red del dhcp")

![Puerta de enlace de la red](./ImagenesPI/dhcpbridge3.PNG "Puerta de enlace de la red")

![Rango de las ip asignadas por dhcp](./ImagenesPI/dhcpbridge4.PNG "Rango de las ip asignadas por dhcp")

![Servidores de DNS](./ImagenesPI/dhcpbridge5.PNG "Servidores de DNS")

![Tiempo de arrendamiento de la ip](./ImagenesPI/dhcpbridge6.PNG "Tiempo de arrendamiento de la ip")

Estos mismos pasos lo haremos para las otras 2 bridges. Quedando como resultado final tal y como se muestra en la siguiente imagen.

![Configurado el dhcp para las tres bridges](./ImagenesPI/dhcpbridgeconfig.PNG "Configurado el dhcp para las tres bridges")

Otro paso que debemos realizar es crear la regla de enmascaramiento en la NAT para el ether 1, de la misma forma que ya se realizó anteriormente, para no repetir solo pondremos las imágenes.

![Configurar enmascaramiento](./ImagenesPI/bridgenat.PNG "Configurar enmascaramiento")

![Configurar enmascaramiento](./ImagenesPI/bridgenat2.PNG "Configurar enmascaramiento")

Pero aún falta un detalle y es que si hacemos ping a la red de otra vlan por ejemplo a la vlan 20, nos responderá, y nosotros queremos que no se comuniquen entre ellas.

![Ping a otra Vlan](./ImagenesPI/ipvlanes.PNG "Ping a otra Vlan")

Tambien se puede ver la lista de rutas, en la cual vemos las rutas establecidas en el router.

![Lista de rutas del router](./ImagenesPI/listarutasvlan.PNG "Lista de rutas del router")

Por lo tanto debemos añadir un par de reglas en el Firewall, para que las vlans no se vean pero si salgan por internet.
Para ello en el menu izquierdo vamos a __IP → Firewall__, pestaña de _File Rules_ y le damos al símbolo de más. En donde definimos que todo lo que vaya desde la red 10.10.10.0 que pertenece a la vlan 10 con destino a la red 20.20.20.0 que pertenece a la vlan 20, le hacemos un drop

![Regla de firewall para vlan](./ImagenesPI/firewallvlan.PNG "Regla de firewall para vlan")

![Regla de firewall para vlan](./ImagenesPI/firewallvlan2.PNG "Regla de firewall para vlan")

Luego repetimos lo mismo pero a la inversa, todo lo que vaya de la vlan 20 a la vlan 10 le hacemos un drop.

![Regla de firewall inversa para vlan](./ImagenesPI/firewallvlan3.PNG "Regla de firewall inversa para vlan")

Entonces ya con esto podemos definir si queremos que alguna vlan si se vean entre ellas o que ninguna se vea entre ellas, en este caso haremos que sean completamente independientes y que no se vean entre ellas quedando todas las reglas como se muestra en la imagen.

![Reglas de firewall para vlanes creadas](./ImagenesPI/firewallvlanes.PNG "Reglas de firewall para vlanes creadas")

## Configurar DMZ y reglas de Firewall

Partiremos como ejemplo de la siguiente topografía de una red empresarial con 2 redes lan y una dmz.

![Topografia de red con dmz](./ImagenesPI/dmz.PNG "Topografia de red con dmz")

Vamos a pasar a configurar una dmz con las siguientes condiciones guiándonos de la imagen anterior. 
- La red de la dmz será la 192.168.30.0, donde habrá uno o varios servidores, según lo que necesite la empresa, como ejemplo pondremos 2, un servidor de ftp y otro de http, al ser servidores la ip será fija, tendrán acceso a internet.
- La red lan1 será la 192.168.10.0, será la que tenga a los trabajadores de la empresa, , y no tendrán acceso a internet.
- La red lan2 será la 192.168.20.0, también serán ip fijas puesto que solo estarán los administradores, estos si tendrán salida a internet, uno se encargará de mantener la dmz conectado por ssh, sin tener acceso a la red lan1 y el otro administrador se encargará del mantenimiento de la red lan1 sin tener acceso a la dmz.

La configuración que se verá será solamente reglas de firewall puesto que ya se a visto anteriormente como crear redes, nombrar ips, crear dhcp, etc.

Lo primero será redirigir lo que entre por la WAN a nuestros servidores dependiendo del protocolo y puerto que  usen, para ello vamos a __IP → Firewall__ y luego a la pestaña de NAT, una vez aquí añadiremos una nueva regla dándole al símbolo del mas, en donde pondremos las reglas que se muestran en las imágenes siguientes.

![Regla nat dmz puerto 80](./ImagenesPI/dmznat1.PNG "Regla nat dmz puerto 80")

![Redireccion de puerto para servidor de http](./ImagenesPI/dmznat2.PNG "Redireccion de puerto para servidor de http")

Como hemos visto en las 2 imágenes anteriores hemos definido que todo lo que venga por el protocolo tcp y puerto 80 lo redirija a una ip concreta la cual coincidirá con la ip de nuestro servidor web. Esta misma regla lo repetiremos con los puertos 8080 y 443.

Ahora haremos los mismo con el puerto 21, redirigiendo lo que venga por este puerto a la ip del servidor de ftp

![egla nat dmz puerto 21](./ImagenesPI/dmznat3.PNG "Regla nat dmz puerto 21")

![Redireccion de puerto para servidor ftp](./ImagenesPI/dmznat4.PNG "Redireccion de puerto para servidor ftp")

Una vez terminado todas nuestras reglas NAT deberían quedar como en la imagen siguiente.

![Configuración de reglas nat de la dmz](./ImagenesPI/dmznatconfi.PNG "Configuración de reglas nat de la dmz")

Vamos a añadir una regla más de NAT para posteriormente hacer una breve comprobación de que funciona la redirección de puerto usando el pc anfitrión de casa e intentando conectarnos por ssh a uno de los servidores de la dmz, usando la ip de la wan del router. 
Para ello simplemente añadiremos las siguientes reglas como se muestran a continuación.

![Regla nat dmz puerto 22](./ImagenesPI/dmznat5.PNG "Regla nat dmz puerto 22")

![Configuración de reglas para ssh](./ImagenesPI/dmznat6.PNG "Configuración de reglas para ssh")

Ahora pasaremos a la pestaña de _Files Rules_ dentro de la ventana de __Firewall__, lo primero que vamos a hacer es permitir que el Administrador de los servicios de la red lan2 pueda acceder a los servidores de http y ftp, como seran muchas imagenes para no repetir tanto solo veremos un ejemplo y luego se mostrará toda la configuración al final.

![Reglas de firewall](./ImagenesPI/dmzfire1.PNG "Reglas de firewall")

![Reglas de firewall aceptar](./ImagenesPI/dmzfire2.PNG "Reglas de firewall aceptar")

Podemos especificar también las reglas,  definiendo que solo se permiten las conexiones por un protocolo y puerto en concreto, quedando todas las reglas de la siguiente manera.

![Reglas de firewall aceptadas configuradas](./ImagenesPI/dmzfireconf.PNG "Reglas de firewall aceptadas configuradas")

La siguiente regla permite el tráfico de conexiones establecidas y relacionadas.

![Reglas de firewall](./ImagenesPI/dmzfire3.PNG "Reglas de firewall")

![Reglas de firewall conexiones establecidas y relacionadas](./ImagenesPI/dmzfire4.PNG "Reglas de firewall conexiones establecidas y relacionadas")

Paso seguido denegamos con la acción __reject__ cualquier otra conexión que vaya desde la lan2 a la dmz y viceversa.

![Regla de firewall reject](./ImagenesPI/dmzfire5.PNG "Regla de firewall reject")

Con lo cual ambas reglas nos quedarían de la siguiente manera.

![Reglas de firewall reject](./ImagenesPI/dmzfire6.PNG "Reglas de firewall reject")

Nuestro siguiente paso será que el Administrador de los servicios pueda conectarse por ssh a ambos servidores, para ello solo necesitamos crear una regla como se muestra a continuación.

![Reglas de firewall aceptar puerto 22](./ImagenesPI/dmzfire7.PNG "Reglas de firewall aceptar puerto 22")

El resto de las configuraciones son procesos parecidos, por lo que para no repetir veremos en la siguiente imagen como quedaria todas las reglas configuradas.

![Todas las relgas de firewall configuradas](./ImagenesPI/dmzfireconfigurada.PNG "Todas las relgas de firewall configuradas")

## Configurar VPN por IPsec

Es muy normal que una empresa que tenga varias sedes quiera tener conexión entre ellas, por ello suele ser usado crear vpn para que se comuniquen entre ellas, por eso vamos a hacer un ejemplo de como crear una vpn por ipsec según el siguiente diagrama, en el que habrá dos sedes con diferentes redes evidentemente y el vpn ira de un router al otro.

![Topografia de red con vpn](./ImagenesPI/ipsec.PNG "Topografia de red con vpn")

Para ver mejor la realización del vpn, vamos a usar dos nuevas imágenes del RouterOS. Con un adaptador puente y otro en red interna. 
Como primer paso vamos a darle nombre e ip a las interfaces. y un servidor de dhcp para la red interna, esto no será necesario enseñarlo en imágenes porque ya se vio anteriormente.
El siguiente paso será darle ip estáticas a la wan de los router, para ello vamos a mostrar un método rápido y sencillo que es con un ayudante de mikrotik, para ello vamos al menú izquierdo y seleccionamos __Quick Set__.

![Fase1](./ImagenesPI/quickset.PNG "")

Esta ventana que vemos es como una configuración inicial rápida, aquí podemos configurar lo siguiente.
- Dentro del apartado de Internet está la configuración de la WAN donde configuraremos lo siguiente:
  - En Address Acquisition definimos que queremos que sea Static
  - IP Address, definimos la ip del interfaz del router con salida a internet
  - En el gateway esta la ip del router de casa, pues todo esto es de manera virtual, en un entorno real será el gateway de nuestro ISP
  - Y de DNS podemos usar los de google
- En la parte de Local Network hace referencia a la interfaz que da a nuestra red LAN, en ella podemos configurar:
  - La ip de la interfaz que va a la red LAN, y su máscara
  - Activamos el servicio de DHCP para esta interfaz, definiendo el rango de las ip que va a proporcionar
  - Y activamos el NAT, para el enmascaramiento.

También podemos definir de paso la contraseña a la hora de acceder a nuestro router.
Tener en cuenta que se debe configurar ambos router, cada uno con sus ip.

 El siguiente paso será ir al menú izquierdo y darle a __IP → IPsec__, una vez abierta la ventana vamos a la pestaña de _Peer_, y le damos al símbolo del más.
 
![Configurar el vecino](./ImagenesPI/ipsecpeer.PNG "Configurar el vecino")

En esta nueva ventana debemos darle un nombre para identificar a nuestro vecino (Peer), en _Address_ escribimos la ip publica del router a donde queremos dirigirnos,  en _Local Address_ escribimos la ip publica del router que estamos configurando ahora mismo.

Pasamos a la pestaña _Identities_, le damos al símbolo más, y en la nueva ventana lo dejamos todo por defecto menos el apartado Secret que hará referencia a la clave compartida, esta deberá ser la misma en ambos router, hay que fijarse en el apartado _Peer_ que corresponda con el que creamos anteriormente.

![Configurar la clave en Identities](./ImagenesPI/ipsecidentity.PNG "Configurar la clave en Identities")

Terminado este paso vamos a la pestaña de Policies, le damos al símbolo del mas y en la nueva ventana en la pestaña _General_ nos aseguramos primero que en el apartado _Peer_ corresponda con el que deseamos configurar, seguidamente activamos la opción de __Tunnel__, en el apartado de _Src. Address_ escribimos el __CIDR__ de la red local que pertenece al router que estamos configurando, y en _Dst. Address_ escribimos el __CIDR__ de la red local de destino.

![Configurando las politicas de IPsec](./ImagenesPI/ipsecpolitica.PNG "Configurando las politicas de IPsec")

Toda esta configuración deberá ser realizada en el otro router donde queremos realizar el túnel, modificando solamente las ip para que correspondan con la configuración del mismo.

Cuando ambos estén configurados, debemos revisar dentro de __IPsec → Policies__ la pestaña _Status_
Y dentro de esta ventana, nos fijamos en donde dice _PH2 State_ que si está en __established__, en ambos router, eso confirma que el túnel a sido creado. 

![Estado del túnel](./ImagenesPI/ipsecpolicistatus.PNG "Estado del túnel")

También podemos corroborarlo yendo a la pestaña de  _Active Peers_ dentro de __IPsec__.

![Comprobación de Vecinos Activos](./ImagenesPI/ipsecactivepeer.PNG "Comprobación de Vecinos Activos")

O en la pestaña de Installed SAs.
Donde saldrá reflejado los vecinos con los que se ha establecido una conexión, la encriptación, la autentificación y las ip públicas de ambos router

![Pestaña de Installed SAs](./ImagenesPI/ipsecsas.PNG "Pestaña de Installed SAs")

Si todo esto está correcto nuestro siguiente paso es añadir una regla NAT en el Firewall para que ambas redes locales puedan comunicarse y no se vean afectadas por el enmascaramiento.
Por lo tanto vamos a __IP → Firewall__ pestaña _NAT_ y añadimos una nueva regla, donde dice _Chain_ lo dejamos como __srcnat__, y definimos la red local y la red de destino con su máscara.

![Configurar regla nat para ipsec](./ImagenesPI/ipsecnat1.PNG "Configurar regla nat para ipsec")

Una vez agregada la regla debemos hacer que esta sea la primera, con lo que la subiremos poniéndola por delante de regla NAT del enmascaramiento como se muestra a continuación.

![Reglas Nat en ipsec](./ImagenesPI/ipsecnatconf.PNG "Reglas Nat en ipsec")

__NOTA:__ Debido a las diferentes versiones de RouterOS puede variar la configuración con lo mostrado. Por ello hay que tener en cuenta lo siguiente:
- Para la configuración del vpn por ipsec se ha usado la versión de CHR __6.45.8__ debido a que realizando los mismos pasos en la version __6.46__ siempre ocurría algún problema.
- Las interfaces de los Router que daban acceso a internet se dejaron en modo cliente por dhcp, debido a que como es una virtualización era mejor que el router de casa les diera la ip y los dns.
- En la regla NAT para evitar el enmascaramiento en el apartado de Protocol hubo que definirlo, (aunque no siempre es necesario), lo que hay que hacer es comprobar si hay conexion entre ambas redes haciendo ping y según si hay conexion o no habra que modificar el protocolo de la regla nat, en este caso fue _50(ipsec-esp)_, para poder saber o modificar el tipo de protocolo que usa IPsec, vamos a __IP → IPsec__ pestaña _Policies_ y luego a la pestaña _Action_, como se muestra en la siguiente imagen.

![Comprobar el protocolo de IPsec](./ImagenesPI/ipsecpoliciaction.PNG "Comprobar el protocolo de IPsec")

[Inicio](https://franciscocadena.github.io/PI-Mikrotik/)














File: /Configuración_Herramientas_Alta_Disponibilida.md
[Inicio](https://franciscocadena.github.io/PI-Mikrotik/)

# En este apartado se explicara como configurar algunas herramientas que aporten Alta Disponibilidad a nuestra Red.

En donde se verán lo siguiente:
- Configuración básica de todos los router
- Montar un failover con rutas de respaldo
- Montar un VRRP
- Montar un Ancho de Banda en una determinada LAN y equipo
- Montar un Balanceo de carga por PCC con los dos proveedores de Internet
 
Para ello nos guiaremos de la siguiente topografia.

![Topografia sencilla para HA](./ImagenesPI/PIFase2/Fase2-2.PNG "Topografia sencilla para HA")

Los router __ISP__ no serían necesario tocarlos puesto que la ip nos la debería dar nuestro proveedor de internet, pero como esto es una virtualización explicaremos brevemente qué tipo de configuración básica le daremos.
 
Solo definiremos que tendrá tres interfaces uno que dé a internet, la cual tendrá ip dinámica y las otras dos interfaces corresponderá a los router de nuestra empresa donde le daremos un ip estática de __/30__.

Comencemos definiendo las interfaces del ISP, y a donde irá cada una.
 
![Interfaces del ISP](./ImagenesPI/PIFase2/isp2interface.PNG "Interfaces del ISP")
 
Seguiremos dándole ip dinámica a la interfaz WAN, para ello como siempre iremos a __ip →  dhcp__ cliente y definimos la regla para la WAN.

![Dhcp cliente de ISP](./ImagenesPI/PIFase2/isp2dhcpcliente.PNG "Dhcp cliente de ISP")

Ahora daremos direccionamiento a las otras dos interfaces que irán a los dos router que se encuentran en la empresa, estas ip serán estáticas con lo que no crearemos un servicio de dhcp, y seran /30.
 
![IP configuradas de ISP](./ImagenesPI/PIFase2/isp2ips.PNG "IP configuradas de ISP")

Definimos los servidores DNS y marcamos la casilla de __Allow Remote Request__.

![DNS del ISP](./ImagenesPI/PIFase2/isp2dns.PNG "DNS del ISP")

Por último creamos el enmascaramiento en NAT.

Todos estos pasos los realizaremos en ambos router ISP, teniendo precaución de no darle el mismo direccionamiento a las ip estáticas que van a los router de la empresa, por ejemplo.
- En el ISP1 se han configurado las siguientes ip:
  - 192.168.1.1/30 → Router Maestro
  - 192.168.3.1/.30 → Router Slave
- Y para el ISP2 se han configurado las siguiente ip:
  - 192.168.2.1/30 → Router Maestro
  - 192.168.4.1/30 → Router Slave

## Ahora pasaremos a los dos router que están en la empresa
 
Una buena práctica a la hora de trabajar con varios router y poder diferenciarlos es darles un nombre o identificador, para ello vamos al menú izquierdo donde dice __System → Identity__, en esta ventana podemos darle un nombre al router para poder definirlo.

![Nombrar al Router](./ImagenesPI/PIFase2/identity.PNG "Nombrar al Router")

Como siempre lo primero que haremos sera la configuracion basica del router, definiendo las interfaces, el direccionamiento de cada interfaz, el dns, y el servicio dhcp, pero en este caso no será necesario.

Por ello solo dejaremos las imágenes de cómo quedaría la configuración de ambos router, haciendo el mismo procedimiento en el otro router, donde solo habrá que cambiar las ips de las interfaces. 

### Master

Interfaces

![Interfaces configuradas](./ImagenesPI/PIFase2/masterinterface.PNG "Interfaces configuradas")

Ips

![IP configuradas](./ImagenesPI/PIFase2/masterips.PNG "IP configuradas")

DNS

![DNS configurado](./ImagenesPI/PIFase2/masterdns.PNG "DNS configurado")

NAT, como tenemos dos WAN debermos crear dos reglas de NAT una por cada WAN

![Nat de ambas Wan configurada](./ImagenesPI/PIFase2/masternat.PNG "Nat de ambas Wan configurada")

### Backup

Ips

![IP configuradas](./ImagenesPI/PIFase2/slaveips.PNG "IP configuradas")


## Failover Rutas de Respaldo

Ahora pasaremos a configurar el Failover en ambos router de la empresa, la idea de esto es definir a los router que cuando se pierda la conexión con uno de los ISP tire por el otro definiendo cuál será el principal y cuál el secundario, por ello ambos router tendrán dos interfaces WAN uno por cada ISP.
Para ello tan solo debemos ir al menú izquierdo, darle a IP → Routes, añadimos una nueva ruta dándole al símbolo (+).
En esta ventana definimos:
- __Dst Address__ 0.0.0.0/0 (Toda IP)
- __Gateway__ 192.168.1.1
- __Check Gateway__ ping (con esto validará haciendo ping al gateway de que este funciona y hay conexión a el)
- __Distance__ 1 (con el 1 definimos que será la principal)

![Configurar ruta principal](./ImagenesPI/PIFase2/master-route1.PNG "Configurar ruta principal")

El resto podemos dejarlo por defecto.
 
Una vez creada esta regla, pasamos a crear la siguiente, con los siguientes parámetros:
- __Dst Address__ 0.0.0.0/0 (Toda IP)
- __Gateway__ 192.168.2.1
- __Check Gateway__ ping (con esto validará haciendo ping al gateway de que este funciona y hay conexión a el)
- __Distance__ 2 (con el 2 definimos que será la secundaria o backup)

![Configurar ruta de respaldo](./ImagenesPI/PIFase2/master-route2.PNG "Configurar ruta de respaldo")
 
Como vemos la única diferencia con respecto a la anterior ha sido que hemos definido el otro gateway que corresponderá al otro ISP, será el secundario o ruta de respaldo, definido en Distance como 2.

Se puede observar en ambas imágenes, que la primera ruta que definimos con _Distance 1_ tiene un color negro y a la izquierda de la ventana tiene las siglas __AS__ correspondiendo la _A → active y la S → static_.
Mientas que la ruta que definimos con _Distance 2_ tiene un color azul y la sigla que aparece es solo __S → static__, eso nos indica que la ruta de color azul está a la espera y cuando se caiga la primera, se activará la segunda, eso se verá en el apartado de comprobaciones.  

Con esto conseguimos que cuando haya cualquier problema con el ISP1, nuestro router al hacer ping y comprobar que no hay respuesta pasará a hacer ping a la ruta de respaldo y si le responderá pasará a tirar el tráfico por este, con ello logramos no perder conexión a internet, solo una breve caída.

Este mismo proceso habrá que hacerlo en el otro router de la empresa, en donde solo habrá que cambiar las ip de los gateways en la creación de ambas rutas.

## VRRP

Este protocolo lo usaremos en aquellas LAN que no sean demasiado grandes y cuyas ip sean estáticas, esto es debido porque cuando una ip es dinámica y tiene 2 router dándole servicio de dhcp, en cuanto uno se caiga con volver a pedir ip por dhcp el mismo equipo cambiara la ip y el gateway, pero con  una ip estática no ocurre esto.

Por ello el protocolo vrrp lo que hace es crear un router virtual, y la ip que definimos en ese router virtual debe ser el mismo en ambos router, y será el gateway que usaremos en nuestros equipos que usen ip estática, de esta manera cuando haya cualquier problema con uno de los router el protocolo vrrp lo detectara y saltara al router de respaldo, consiguiendo así que el equipo cliente no se quede sin internet.

Lo primero que tendremos que hacer es ir a la pestaña de _VRRP_ dentro de la ventana de __interfaces list__, y darle al simbolo del (+) para crear uno.
En la ventana que nos aparece en la pestaña de _General_ tan solo definimos el nombre que deseamos que tenga nuestro vrrp, acto seguido vamos a la pestaña _VRRP_, y dentro de este configuraremos lo siguiente:
- __Interface__ ether6-LAN(donde definiremos en qué interfaz ira nuestro vrrp, en este caso será en LAN)
- __VRID__ 10 (este será el identificador de nuestro vrrp, es importante que este número coincida con el vrrp que crearemos en el router backup sino no funcionara el vrrp)
- Priority 100 (la prioridad define quien será el maestro y quien el backup, el que tenga un número mayor en este apartado será el master)

El resto de parámetros lo podemos dejar por defecto.

![Vrrp1 pestaña Vrrp del router maestro](./ImagenesPI/PIFase2/mastervrrp1.PNG "Vrrp1 pestaña Vrrp del router maestro")

![Vrrp1 pestaña General del router maestro](./ImagenesPI/PIFase2/mastervrrp1_1.PNG "Vrrp1 pestaña General del router maestro")

Como en este ejemplo de Red tenemos 2 redes estáticas, creamos otro vrrp, donde solo deberemos modificar el nombre, la interfaz que ahora será LAN2 y el VRID  a 20 por ejemplo, quedando como en la siguiente imagen.

![Vrrp2 pestaña Vrrp del router maestro](./ImagenesPI/PIFase2/mastervrrp2.PNG "Vrrp2 pestaña Vrrp del router maestro")

![Vrrp2 pestaña General del router maestro](./ImagenesPI/PIFase2/mastervrrp2_1.PNG "Vrrp2 pestaña General del router maestro")

Una vez creadas ambas vrrp podemos ver como quedan en el apartado de interfaces.

![Interfaces con los vrrp configurados](./ImagenesPI/PIFase2/mastervrrpinterfaces.PNG "Interfaces con los vrrp configurados")

Las siglas de la izquierda de __RM__ hacen referencia a _R → running y M → master_.
Esto aparecerá una vez que esté ambos router configurados.

El siguiente paso será darle ip a ambos vrrp, como siempre para ello vamos al menú izquierdo IP → Address, símbolo del (+).
En la ventana seleccionamos uno de los vrrp creados y le damos una ip dentro del rango de la red, con la precaución de que debe terminar en /32.

![IP configuradas en los dos vrrp](./ImagenesPI/PIFase2/mastervrrpips.PNG "IP configuradas en los dos vrrp")

Hacemos el mismo procedimiento para el otro vrrp, definiendo una ip que corresponda a su red ya que cada vrrp que hemos creado es para una LAN diferente.

#### Ahora pasaremos a configurar los VRRP en el router que hara de Backup

Como hicimos con el router master, lo primero será crear los vrrp para cada LAN, donde lo único que cambiaremos será la interfaz y la prioridad, dejando el mismo VRID, quedando ambos router como se muestra en las siguientes imágenes.

![Vrrp1 pestaña Vrrp del router backup](./ImagenesPI/PIFase2/slavevrrp1.PNG "Vrrp1 pestaña Vrrp del router backup")

![Vrrp1 pestaña General del router backup](./ImagenesPI/PIFase2/slavevrrp1_1.PNG "Vrrp1 pestaña General del router backup")

![Vrrp2 pestaña Vrrp del router backup](./ImagenesPI/PIFase2/slavevrrp2.PNG "Vrrp2 pestaña Vrrp del router backup")

![Vrrp2 pestaña General del router backup](./ImagenesPI/PIFase2/slavevrrp2_2.PNG "Vrrp2 pestaña General del router backup")

Una vez creado ambos vrrp, en la parte de interfaces podemos observar como ya están creadas y que aparece a la izquierda la sigla __B__ haciendo referencia  _B → backup_.

![Interfaces con los vrrp configurados](./ImagenesPI/PIFase2/slavevrrpinterface.PNG "Interfaces con los vrrp configurados")

El siguiente paso será darle las ip a ambos vrrp. donde deberán coincidir las ip de esos con las que usamos en el router master, quedando de la siguiente manera.

![IP configuradas en los dos vrrp](./ImagenesPI/PIFase2/slavevrrpips.PNG "IP configuradas en los dos vrrp")

Una vez creada, aparecerán de color rojo eso es debido a que están en modo de espera, y cuando falle el maestro este saltara cambiando el color a negro debido a que se habrá activado.

Una vez configurado ambos Router con sus respectivos vrrp, solo queda poner la ip fija a nuestros equipos clientes con el correspondiente gateway a cada uno según a la LAN a la que pertenezcan. 
Con lo que a un equipo de la LAN le pondremos de gateway 192.168.10.10, y a los que pertenezcan a la LAN 2  le pondremos de gateway 192.168.20.20.

## Ancho de Banda

Realizaremos el ancho de banda en la LAN 2 por ejemplo, para ello desde Winbox nos dirigimos al menú izquierdo  y seleccionamos la opción de __Queues__, en la ventana que nos aparece marcamos la pestaña _Simple Queues_ y luego le damos al símbolo del (+).
En esta nueva ventana donde dice __Name__ tan solo escribimos un nombre a la regla para definirla.
En __Target__ definimos a quien se le asigna el ancho de banda pudiendo usar una _ip en concreto_, el _CIDR_ de la red o incluso el _interfaz_.
En __Target Upload__ vamos a _Max Limit_ y definimos la velocidad de subida.
En __Target Download__ vamos a _Max Limit_ y definimos la velocidad de bajada.
El resto lo podemos dejar por defecto, aplicamos y le damos a OK.

![Creando regla a una IP](./ImagenesPI/PIFase2/mastervelocidad1.PNG "Creando regla a una IP")

Para poder hacerlo más visual aplicaremos otra regla en la cual definiremos a toda la red LAN 2. Con ello lo que conseguiremos es definir el límite de velocidad de la LAN2 y al vez poder definir el límite de velocidad de cada equipo dentro de la red.

![Creando regla a la red LAN2](./ImagenesPI/PIFase2/mastervelocidad2.PNG "Creando regla a la red LAN2")

Hay que tener en cuenta de que estas reglas se aplican igual que las de firewall, es decir empieza a aplicarse las reglas desde la primera a la última por tanto la regla más genérica debe estar abajo que en este caso es la regla que hace referencia a la red LAN2,  y la regla más específica debe estar más arriba que en este caso corresponde a la ip 192.168.20.4, quedando como se muestra en la imagen.

![Reglas creadas y ordenadas](./ImagenesPI/PIFase2/mastervelocidad3.PNG "Reglas creadas y ordenadas")

Si no seguimos este orden y dejamos la regla más general primero toda la red LAN2 tendrá el límite de velocidad indicado, sin aplicarse las otras reglas que definen la ip de cada equipo.
 
__Nota:__ Los colores del icono cambian dependiendo del uso que le dé al ancho de banda asignado; entonces, si se usa de un 0% a 50% del ancho de banda, la regla estará de color verde, si se usa del 50% a 70%, se volverá de color amarillo, y si sobrepasa el 70% se volverá de color rojo.

## Balanceo de carga con PCC

Para realizar el balanceo de carga seguiremos el diagrama de red del principio con la diferencia de que añadiremos una nueva red con la siguiente red 192.168.30.0/24, a la cual la llamaremos DMZ. El resto será igual.
Comenzamos yendo a __IP → FIREWALL__ y luego a la pestaña de _Mangle_ seguidamente añadimos una nueva regla dandole al simbolo del (+), en la nueva ventana que nos aparece estando en la pestaña de _General_ tan solo definimos en el apartado de __Chain__  con _prerouting_ y en el apartado __Dst.Address__ añadimos la red de una de las WAN que tenemos. Si tenemos varias redes LAN podemos definirla en __In. Interface__, si solo tenemos una o queremos que se aplique a todas no es necesario definirla.

![Regla de Mangle pestaña General](./ImagenesPI/PIFase2/mastermangle1.PNG "Regla de Mangle pestaña General")

Luego vamos a la Pestaña de _Action_ y en el apartado de __Action__ seleccionamos _Accept_, aplicamos y ok.

![Regla de Mangle pestaña Action](./ImagenesPI/PIFase2/mastermangle2.PNG "Regla de Mangle pestaña Action")

Esta regla la deberemos de repetir por cada interfaz que de acceso a internet, es decir si por ejemplo tenemos cuatro proveedores de internet habrá que crear cuatro reglas como estas, en donde solo habrá que cambiar el apartado de __Dst.Address__ por el CIDR correspondiente a cada ISP. En nuestro caso serán solo dos reglas, puesto que tenemos dos interfaces Wan.

Nuestro siguiente paso será crear reglas para marcar todas las peticiones de las conexiones que vengan desde internet.
Para ello creamos una nueva regla, en la pestaña _General_ definimos en __Chain__ como _prerouting_, en __In Interface__ seleccionamos una de las interfaces que den acceso a Internet, y en el apatado de __Connection Mark__ lo dejamos en _no mark_.

![Regla de mangle para marcado de peticiones, pestaña General](./ImagenesPI/PIFase2/mastermangle3.PNG "Regla de mangle para marcado de peticiones, pestaña General")

Ahora pasamos a la pestaña de _Action_, aquí en el apartado de __Action__ seleccionamos _mark connection_, en el apartado de __New Connection Mark__ damos un nombre que queramos, que nos sirva para  definirlo, y dejamos marcada la casilla de __Passthrough__, esto nos permite que si no se cumple esta regla pase a la siguiente que tengamos creada.

![Regla de mangle para marcado de peticiones, pestaña Action](./ImagenesPI/PIFase2/mastermangle4.PNG "Regla de mangle para marcado de peticiones, pestaña Action")

Las siguientes  reglas corresponden a cada proveedor de internet y a una interfaz que vaya a una red local que nosotros definimos.
Como siempre empezamos dandole al símbolo del (+) para crear una nueva regla, en la pestaña _General_ seleccionamos _prerouting_ en el apartado de __Chain__, en el apartado de __In Interface__ seleccionamos la red Lan que deseamos, en este caso será la interfaz que va a la DMZ.

![Regla Mangle LAN pestaña General](./ImagenesPI/PIFase2/mastermangle5.PNG "Regla Mangle LAN pestaña General")

Luego pasamos a la pestaña de _Advanced_ y en el apartado de __Per Connection Classifer__ seleccionamos _both addresses_ y nos saldrá a la derecha dos apartados para insertar números.
El primer número corresponde a la cantidad total de ISP que tengamos conectados en nuestro router, y el siguiente número corresponde al ISP para el que estamos creando la regla empezando siempre desde cero.
Por ejemplo si tenemos cuatro ISP conectados al router habrá que crear cuatro reglas, una por cada ISP conectado a nuestro router y el orden numérico para cada regla sería el siguiente:
- 4/0
- 4/1
- 4/2
- 4/3
Como se observa el primer número no cambia porque hace referencia al total, el que cambia es el segundo para saber a quien se le está aplicando la regla, como se empieza a contar desde el 0, si tenemos 4 ISP la cuenta será desde el 0 hasta el 3.

![Regla Mangle LAN pestaña Advanced](./ImagenesPI/PIFase2/mastermangle6.PNG "Regla Mangle LAN pestaña Advanced")

Ahora pasamos a la pestaña _Extra_ aquí buscamos la opción de __Dst.Address Type__, y en _Addres Type__ seleccionamos _local_,  y marcamos la casilla de _Invert_.

![Regla Mangle LAN pestaña Extra](./ImagenesPI/PIFase2/mastermangle7.PNG "Regla Mangle LAN pestaña Extra")

Por último vamos a la pestaña de _Action_, en esta seleccionamos _mark connection_ en el apartado de __Action__, en el apartado de __New Connection Mark__ seleccionamos uno de los nombres que definimos en las reglas anteriores para cada ISP, y dejamos marcada la opción de __Passtrough__. 

![Regla Mangle LAN pestaña Action](./ImagenesPI/PIFase2/mastermangle8.PNG "Regla Mangle LAN pestaña Action")

Como siempre se crearán tantas reglas como wan tengamos, como en este caso tenemos dos, habrá que crear otra regla idéntica a la anterior cambiando solamente en la pestaña _Action_ en el apartado __New connection Mark__ al nombre que le hayamos dado para la regla del otro ISP que tenemos conectado, y en la pestaña de _Advanced_ en el apartado de __Per Connection Classifier__ al seleccionar  _both addresses_ debemos cambiar el segundo número por el que corresponda que en este caso será 1, haciendo referencia al segundo ISP.

![Regla Mangle LAN pestaña Extra para ISP2](./ImagenesPI/PIFase2/mastermangle9.PNG "Regla Mangle LAN pestaña Extra para ISP2")

Las siguientes reglas serán para marcar la ruta de todos los paquetes que pasan por las conexiones.
En la pestaña _General_ seleccionamos el interfaz que va a nuestra red local en el apartado de __In Interface__, y en el apartado de __Connection Mark__ seleccionamos uno de los nombres que creamos al definir la regla de marcado de peticiones de conexión para cada ISP.

![Regla Mangle para marcar paquetes pestaña General](./ImagenesPI/PIFase2/mastermangle10.PNG "Regla Mangle para marcar paquetes pestaña General")

Luego pasamos a la pestaña de _Action_ en donde seleccionamos _mark routing_ en el apartado de __Action__, dejamos marcado la opción del __Passthrough__ y en el apartado de __New Routing Mark__ damos un nombre que haga referencia a uno de los ISP. 
Aplicamos y ok.

![Regla Mangle para marcar paquetes pestaña Action](./ImagenesPI/PIFase2/mastermangle11.PNG "Regla Mangle para marcar paquetes pestaña Action")

Creamos otra regla idéntica a la anterior para el otro ISP cambiando solo el apartado de __Connection Mark__ dentro de la pestaña _General_ por el nombre de la regla que hace referencia al otro ISP, y en la pestaña de _Action_ daremos otro nombre para identificar al otro ISP en el apartado de __New Routing Mark__

Ahora crearemos otras reglas como siempre una para cada ISP que tengamos conectado al router, para el _chain outpust_.
Por lo tanto en la nueva regla, en la pestaña _General_ seleccionamos _output_ en el apartado de __Chain__, y en el apartado de __Connection Mark__ seleccionamos uno de los nombres que definimos en las reglas para marcado de peticiones por conexiones para el ISP, en la siguiente regla que creemos se deberá cambiar solo este apartado seleccionando el nombre de la otra regla del otro ISP.

![Regla Mangle Output pestaña General](./ImagenesPI/PIFase2/mastermangle12.PNG "Regla Mangle Output pestaña General")

Pasamos a la pestaña de _Action_, en donde seleccionamos _mark routing_ en el apartado de __Action__, dejamos marcado __Passthroug__ y en el apartado de __New Routing Mark__ seleccionamos uno de los nombres que creamos cuando definimos las reglas de rutas de los paquetes. Cuando creemos las otras reglas este apartado será otro de los que cambie definiendo los otros nombres que definimos al crear las reglas de marcado de paquetes. 

![Regla Mangle Output pestaña Action](./ImagenesPI/PIFase2/mastermangle13.PNG "Regla Mangle Output pestaña Action")

Una vez creada todas las reglas para los dos ISP que tenemos en este ejemplo debería quedar como en la siguiente imagen.

![Todas las Reglas Mangle configuradas](./ImagenesPI/PIFase2/mastermangle14.PNG "Todas las Reglas Mangle configuradas")

El siguiente paso será agregar las rutas a la tabla de ruteo, para ello vamos a __IP → Routes__, y le damos al (+). Crearemos una ruta por cada ISP que tengamos conectado al router.
En esta ventana definimos como direcciones de destino todas, así que en el apartado de __Dst. Address__ escribimos 0.0.0.0/0.
En __Gateway__ escribimos la ip de nuestro ISP, en __Check Gateway__ lo dejamos en ping, dejamos todo lo demas por defecto y lo que debemos modificar es el apartado de __Routing Mark__ donde seleccionaremos uno de los nombre que definimos en las reglas que creamos para el marcado de ruta de los paquetes, lo interesante será que el nombre corresponda con la ip del ISP que estamos definiendo en la ruta.

![Creando ruta para PCC en ISP1](./ImagenesPI/PIFase2/masterpccroute.PNG "Creando ruta para PCC en ISP1")

Con esto conseguimos que todo el tráfico marcado para isp1 salga por el gateway que hemos definido.
La siguiente ruta que creemos para el otro ISP será idéntica a la anterior cambiando solo la ip del __Gateway__ por el otro ISP  y el apartado de __Routing Mark__ donde seleccionaremos el otro nombre de la otra regla creada de marcado de rutas.

Quedando las rutas como se muestra en la imagen.

![Rutas de PCC creadas](./ImagenesPI/PIFase2/masterpccroute2.PNG "Rutas de PCC creadas")

[Inicio](https://franciscocadena.github.io/PI-Mikrotik/)


File: /Configuración_Herramientas_Seguridad.md
[Inicio](https://franciscocadena.github.io/PI-Mikrotik/)

# Seguridad

En este apartado se explicara la configuración de:
- Port Knocking
- Envio de correo 
- Envio de backup por correo
- Envio de archivos log por cooreo
- Layer 7

Según el diagrama siguiente vamos a explicar como configurar el __Port Knocking__.

![Topografía de red con gns3 para Port Knocking](./ImagenesPI/PIFase3/topografia1.PNG "Topografía de red con gns3 para Port Knocking")

Partiremos de un router multiwan cuyas ip sean estáticas, y una red lan con servicio dhcp.

![Interfaces, direccionamiento de las mismas y las rutas](./ImagenesPI/PIFase3/ipsconfiguradas.PNG "Interfaces, direccionamiento de las mismas y las rutas")

## Crear Lista de Interfaces

Lo primero que podemos hacer para facilitar el trabajo a la hora de crear las reglas de firewall es definir todas las redes WAN en una lista.
Para ello estando en la ventana de Interfaces vamos a la pestaña de _Interface List_.
Le damos al botón que dice __List__ y en la nueva ventana de _Interface Lists_ le damos al símbolo del (+), en la nueva ventana llamada _New Interface List_ vamos al aparatado de __Name__ donde definiremos el nombre que queramos en este caso _WAN_, aplicamos y ok. Con esto ya nos aparecerá el nombre definido en la lista de interfaces.

![Crear lista Wan](./ImagenesPI/PIFase3/interfacelist.PNG "Crear lista Wan")

Ahora regresaremos a la ventana principal de _Interface List_ y le damos al (+), en esta nueva ventana lo que haremos será en el apartado _List_ elegir __WAN__ que fue el nombre que definimos antes, y en el apartado interface seleccionamos una de las diferentes interfaces wan que tengamos, en este caso como tengo tres debo agregar las tres interfaces a la lista wan.

![Agregar interfaces a la lista WAN](./ImagenesPI/PIFase3/agregarinterfaceslista.PNG "Agregar interfaces a la lista WAN")

Al final nos debe quedar la lista como en la imagen siguiente.

![Lista wan creada](./ImagenesPI/PIFase3/listwan.PNG "Lista wan creada")

## Port Knocking

Ahora pasamos a crear las reglas del port knocking, para ello vamos a __IP → Firewall__ y luego agregamos una regla dándole al (+).
En este ejemplo haremos que los golpes de puertos necesarios para poder entrar al router ya sea por (WinBox, SSH, Telenet, etc.) sean tres, tal y como se ve en la primera imagen de la topografía de red.
Lo primero en la pestaña _General_ vamos al apartado _Chain_ y le asignamos __Input__, luego vamos al apartado _Protocol_  y seleccionamos __6(tcp)__.
Al asignar un protocolo podremos definir los puertos de _Source y Destiny_ en este caso iremos al _Ds. Ports_ y escribimos 2000.
Lo siguiente será definir el interfaz wan de entrada en el apartado _In Interface_, el problema es que como en este ejemplo tenemos tres interfaces wan, se deberia crear tres reglas iguales para cada interfaz, por ello para simplificarlo y no crear tantas reglas, definimos con anterioridad una lista wan para todas las interfaces que van por wan.
Con lo cual nosotros vamos al apartado de _In Interface List_ y seleccionamos nuestra lista __WAN__ anteriormente creada, con esto tan solo hemos creado una regla definiendo a la entrada de todas las interfaces wan que tengamos asignada a esa lista, en vez de tener que crear una regla para cada interfaz de entrada por wan.

![Pestaña general regla 1](./ImagenesPI/PIFase3/portknockinggeneral1.PNG "Pestaña general regla 1")

Ahora pasamos a la pestaña de _Action_, y seleccionamos la opción de __add src to address list__  en el apartado de _Action_.
Luego en _Address List_ definimos el nombre que nosotros queramos, en este ejemplo se ha usado __temporal__.
Y en el apartado de _Timeout_ definimos el tiempo que la ip va a estar en esta lista, en este ejemplo se a usado una duración de 5 minutos (00:05:00).
Aplicamos y OK.


![Pestaña action regla 1](./ImagenesPI/PIFase3/portknockingaction1.PNG "Pestaña action regla 1")

Vamos a explicar que hace esta regla que acabamos de definir.
Lo que hemos hecho es definir que todo lo que entre al router por cualquier interfaz wan que se encuentre en la lista definida, y use el protocolo tcp y el puerto de destino 2000, lo agregue a una lista de direcciones que hemos llamado temporal, con una duración de 5 minutos, pasado ese tiempo se eliminará de la lista.
 
Ahora crearemos la siguiente regla que corresponderá con el segundo toque o golpeo de puerto.

![Pestaña general regla 2](./ImagenesPI/PIFase3/portknockinggeneral2.PNG "Pestaña general regla 2")

Como se ve en la imagen anterior de momento lo único que se ha cambiado en la pestaña _General_ a sido el __puerto de Destino__ que ahora es _4000_.
Ahora pasamos a la pestaña _Advanced_, una vez aquí vamos al apartado de _Src. Address List_ y seleccionamos __temporal__.

![Pestaña advanced regla 2](./ImagenesPI/PIFase3/portknockingadvanced2.PNG "Pestaña advanced regla 2")

Ahora pasamos a la pestaña _Action_ y definimos en el apartado de _Action_ __add src to address list__ en _Timeout_ podemos dejarlo de nuevo en 5 minutos eso es al gusto de cada uno, y en _Address List_ definimos un nuevo nombre, en este caso se a usado __permitido__.
Aplicamos y ok.

![Pestaña action regla 2](./ImagenesPI/PIFase3/portknockingaction2.PNG "Pestaña action regla 2")

Con esta segunda regla lo que hemos definido es que todas las ip que se encuentren en la lista de temporal tendrán que hacer una conexión al puerto 4000, y pasarán a estar por 5 minutos en otra lista de ip a la que hemos denominado permitido.
 
Ahora pasamos a definir el tercer toque o golpeo de puerto tal y como venía en el diagrama de red.
Los pasos serán muy parecidos a los aplicados a la segunda regla, con lo que en la pestaña general solo cambiamos el _Dst. Port_ por 8000.

![Pestaña general regla 3](./ImagenesPI/PIFase3/portknockinggeneral3.PNG "Pestaña general regla 3")

Seguidamente vamos a la pestaña de _Advanced_ y en el apartado de _Src. Address List_ definimos a la lista de ip que se encuentran en __permitido__ que son los que han realizado satisfactoriamente el primer y el segundo toque o golpeo de puerto.

![Pestaña advanced regla 3](./ImagenesPI/PIFase3/portknockingadvanced3.PNG "Pestaña advanced regla 3")

Luego vamos a la pestaña de _Action_ donde volvemos a seleccionar __add src to address list__ en el apartado de _Action_, en _Address List__ nombramos a la nueva lista como seguro, y en _Timeout_ esta vez le daremos bastante más tiempo que lo usados anteriormente en este caso 1 hora (01:00:00) o 60 minutos (00:60:00) ambas valen. 

![Pestaña advanced regla 3](./ImagenesPI/PIFase3/portknockingaction3.PNG "Pestaña advanced regla 3")

El motivo de añadir más tiempo a esta lista de ips es debido a que este será el último golpeo de puerto para poder acceder al router y por tanto esta ip tendrá acceso al router mientras se encuentre en esta lista, pasado ese tiempo será borrado y se le denegara el acceso al router, esto quiere decir que pasado 1 hora, la ip que haya podido acceder al router será eliminada de la lista y por tanto se le echara del router, debiendo conectarse nuevamente llamando a los tres toques o golpes de puerto que hemos definido.
Lo dos toques anteriores tenían un tiempo menor porque es el tiempo que le definimos para que llame al siguiente puerto, esto ayuda a que un cracker tenga poco tiempo para poder averiguar cual es el siguiente protocolo y puerto que debe usar para poder pasar la siguiente barrera de protección, puesto que pasado ese tiempo deberá empezara de nuevo llamando al primer puerto que se definió en la primera regla.
 
Ahora pasamos a definir la regla de aceptación.
En la pestaña _General_ tan solo definimos en _Chain_ el modo __Input_ y en _In. Interface List_ __WAN__.

![Pestaña general regla 4](./ImagenesPI/PIFase3/portknockinggeneral4.PNG "Pestaña general regla 4")

Luego pasamos a la pestaña de _Advanced_ donde en _Src. address List_ definimos a las ip que se encuentren en la lista de __seguro__ ya que estas ip previamente han tenido que pasar las dos reglas anteriores que definimos.

![Pestaña advanced regla 4](./ImagenesPI/PIFase3/portknockingadvanced4.PNG "Pestaña advanced regla 4")

Luego vamos a la pestaña de _Action_, donde el apartado de _Action_ lo dejamos en __accept__.
Aplicamos y OK.

![Pestaña action regla 4](./ImagenesPI/PIFase3/portknockingaction4.PNG "Pestaña action regla 4")

Con esta regla hemos definido que todas aquellas ip, que hayan pasado las tres reglas anteriores tendrán permiso para entrar al router.
 
Por último crearemos una regla la cual impida que cualquier ip que no cumpla estas condiciones pueda entrar al router.
Para ello creamos una nueva regla, donde en la pestaña de _General_ definimos __Input__ en el apartado de _Chain_ y nuestra lista de __WAN__ en el apartado de _In Interface List_

![Pestaña general regla 5](./ImagenesPI/PIFase3/portknockinggeneral5.PNG "Pestaña general regla 5")

Luego vamos a la pestaña de _Action_ y definimos __drop__ en el apartado de _Action_.
Aplicamos y OK.

![Pestaña action regla 5](./ImagenesPI/PIFase3/portknockingaction5.PNG "Pestaña action regla 5")

Al final nos deben quedar las cinco reglas creadas como en la imagen siguiente.
Cumpliendo con lo definido en el diagrama de red.

![Reglas de Port Knocking creadas](./ImagenesPI/PIFase3/portknockingreglas.PNG "Reglas de Port Knocking creadas")

## Crear Address List

A aparte del Port Knocking, podemos crear nosotros las address lists manualmente definiendo qué ip consideramos seguras para poder entrar en el router. 
Para ello tan solo tenemos que ir a la pestaña de _Address Lists_ dentro dentro de la ventana de __Firewall__ y una vez aquí darle al símbolo del (+).
En la ventana que nos aparece le damos un nombre a la lista de direcciones, agregamos la ip que vamos a permitir acceder al router y tambien si queremos podemos definir o no el tiempo que estará dentro de esta lista. 
Con esto podemos agregar todas las ip que queramos en una address list en concreto o crear una address list por ip, según más nos convenga.

![Creación manual de address list](./ImagenesPI/PIFase3/addresslista.PNG "Creación manual de address list")

Una vez que tengamos definidas nuestras address list tan solo debemos crear una regla de firewall en la que permitamos el acceso a estas listas, definiendolo en la pestaña de _advanced_ y seleccionar las _addres list_ que deseamos de las creadas antes en el apartado de __Src. Address List__. 

![Crear regla de Firewall agregando nuestra Address List creada](./ImagenesPI/PIFase3/exclusiones.PNG "Crear regla de Firewall agregando nuestra Address List creada")

![Regla creada](./ImagenesPI/PIFase3/portknockingreglas2.PNG "Regla creada")

## Configurar Gmail en Mikrotik

Lo primero es saber la ip de nuestro servicio de correo de gmail, y el puerto, para eso podemos ir al siguiente enlace [SMTP gmail](https://support.google.com/a/answer/176600?hl=es).
Y nos fijamos en el siguiente apartado que se muestra en la imagen.

![SMTP GMAIL](./ImagenesPI/PIFase3/gmail.PNG "SMTP GMAIL")

Lo más interesante de aquí son los puertos __(465 y 587)__ y la dirección del servidor smtp __smtp.gmail.com__.
Ahora pasamos a nuestro router mikotik, abrimos una terminal y hacemos ping a esa dirección de smtp, para saber la ip del mismo

![IP  de nuesto servicio SMTP](./ImagenesPI/PIFase3/smtpip.PNG "IP de nuesto servicio SMTP")

Apuntamos la ip que nos aparece porque nos servirá más adelante.
Con esto ya tenemos el puerto y la ip.
Ahora para dar más seguridad iremos a la siguiente página [Contraseña de aplicaciones](https://support.google.com/accounts/answer/185833?hl=es-419) y seguiremos los pasos para crear contraseñas de aplicaciones.

![Contraseña de aplicaciones](./ImagenesPI/PIFase3/contraseñaapp.PNG "Contraseña de aplicaciones")

Una vez dentro del apartado de contraseña de aplicación, vamos al apartado que dice _Seleccionar Aplicación_, marcamos otro, y escribimos por ejemplo _Router Mikortik_ o lo que cada uno vea mejor, y luego le damos a __Generar__.

![Creando contraseña de aplicaciones](./ImagenesPI/PIFase3/contraseñaapp2.PNG "Creando contraseña de aplicaciones")

Apuntamos la contraseña que nos dan de 16 dígitos después de darle al botón de generar.

![Contraseña dada por Gmail](./ImagenesPI/PIFase3/contraseñaapp3.PNG "Contraseña dada por Gmail")

Ahora tenemos todo lo necesario. Así que pasamos a nuestro router Mikrotik.
Una vez en el router vamos al menú izquierdo donde dice __Tools → Email__
y en la ventana que nos aparece escribimos lo siguiente en cada apartado.
- __Server:__ ip de nuestro servicio de smtp
- __Port:__ el puerto que vamos a usar
- __Start Tls:__ hace referencia al transporte criptográfico de seguridad
- __From:__ nuestro correo electrónico
- __User:__ el usuario al cual va dirigido, funciona mejor si dejamos nuestro correo al igual que en _from_
- __Password:__ la contraseña que nos dio google en el apartado de contraseña de aplicaciones. Aunque también se puede usar la propia contraseña de nuestro correo electronico, pero de esta manera no es tan segura ni fiable.
Aplicamos y ok.

![Configuración de correo en Mikrotik](./ImagenesPI/PIFase3/gmailmikrotik.PNG "Configuración de correo en Mikrotik")

Un dato a tener en cuenta para que funcione correctamene el envio de correos es tener activo nuestro servicio SNTP (Server Network Time Protocol) activado, para ello vamos a __System → SNTP client__.
En la ventana que nos aparece marcamos la casilla de _Enabled_, y en _Primary NTP Server_ escribimos __time.google.com__, luego le damos al botón de Apply y automáticamente nos reconocerá la ip de este servicio (siempre que tengamos bien configurado nuestro DNS), rellenando automáticamente lo necesario, así que le damos a OK.

![Configurar NTP](./ImagenesPI/PIFase3/sntpcliente.PNG "Configurar NTP")

## Configurar que nos lleguen errores y dhcp por correo

Una vez configurado nuestro servicio de correo en Mikrotik vamos a definir que queremos que nos envíe por email, para ellos vamos a __System → Logging__
Una vez aquí vamos primero a la pestaña de _Actions_, y le damos al simbolo del (+).

![Logging pestala Action](./ImagenesPI/PIFase3/gmailerror.PNG "Logging pestala Action")

En la ventanita que nos aparece, definimos el nombre de la acción en _Name_ por ejemplo __email__, definimos de que tipo será en _Type_ el cual será __email__, activamos la casilla _Start TLS_ y en el apartado _Email_ definimos el correo al cual será enviado, aplicamos y ok.

![Creando la acción de email](./ImagenesPI/PIFase3/gmailerror2.PNG "Creando la acción de email")

Ya nos deberá aparecer nuestra acción creada.

![Acción email creada](./ImagenesPI/PIFase3/gmailerror3.PNG "Acción email creada")

Acto seguido vamos a la pestaña de _Rules_ y le damos al símbolo del (+)

![Logging pestala Rules](./ImagenesPI/PIFase3/gmailerror4.PNG "Logging pestala Rules")

En la ventana que nos aparece en donde dice _Action_ seleccionamos la acción que previamente creamos como __email__, y en _Topics_ nos saldrá un desplegable con una gran cantidad de opciones donde podemos elegir la que deseemos, en este caso seleccionaremos __error__, luego le damos a aplicar y ok.

![Creando la regla de error por correo](./ImagenesPI/PIFase3/gmailerror5.PNG "Creando la regla de error por correo")

Con esta regla cada vez que se produzca un error en el router, nos será notificado al correo que definimos en la _Action_, de esta manera podemos crear todas las reglas que queramos definiendo qué aspectos queremos que se nos comuniquen por correo. 
En este ejemplo aparte de los errores se creó otra regla para el dhcp como se muestra a continuación.

![Reglas de error y dhcp creadas](./ImagenesPI/PIFase3/gmailerror6.PNG "Reglas de error y dhcp creadas")

## Configurar que nos lleguen archivox Backup por correo

También podemos configurar el router Mikrotik para que nos envíe automáticamente cada cierto tiempo un archivo de respaldo de la configuración del router.
Para ello usaremos los siguientes scripts.

Backup Binario

~~~
/system script add name=respaldo_binario source={/system backup save name=([/system identity get name] . "-" . \
[:pick [/system clock get date] 7 11] . [:pick [/system clock get date] 0 3] . [:pick [/system clock get date] 4 6]); \
/tool e-mail send to="youremail@yourdomain.com" subject=([/system identity get name] . " Backup " . \
[/system clock get date]) file=([/system identity get name] . "-" . [:pick [/system clock get date] 7 11] . \
[:pick [/system clock get date] 0 3] . [:pick [/system clock get date] 4 6] . ".backup"); :delay 10; \
/file rem [/file find name=([/system identity get name] . "-" . [:pick [/system clock get date] 7 11] . \
[:pick [/system clock get date] 0 3] . [:pick [/system clock get date] 4 6] . ".backup")]; \
:log info ("System Backup emailed at " . [/sys cl get time] . " " . [/sys cl get date])}
~~~

Backup Export

~~~
/system script add name=respaldo_export source={/export file=([/system identity get name] . "-" . \
[:pick [/system clock get date] 7 11] . [:pick [/system clock get date] 0 3] . [:pick [/system clock get date] 4 6]); \
/tool e-mail send to="backup@YOURDOMAIN.com" subject=([/system identity get name] . " Backup " . \
[/system clock get date]) file=([/system identity get name] . "-" . [:pick [/system clock get date] 7 11] . \
[:pick [/system clock get date] 0 3] . [:pick [/system clock get date] 4 6] . ".rsc"); :delay 10; \
/file rem [/file find name=([/system identity get name] . "-" . [:pick [/system clock get date] 7 11] . \
[:pick [/system clock get date] 0 3] . [:pick [/system clock get date] 4 6] . ".rsc")]; \
:log info ("System Backup emailed at " . [/sys cl get time] . " " . [/sys cl get date])}
~~~

Cada script corresponde a uno de los dos tipos de respaldo que puede crear Mikrotik.
 
- El __Binario__ es un respaldo total de la configuración del router, el cual guarda tanto los usuario como las contraseñas del mismo, está pensado para usarse en el mismo router cuando haya algún tipo de error, el tipo de texto esta en binario con lo cual si intentamos abrirlo está todo cifrado, siendo ilegible y solo reconocible por dispositivos mikrotik.
- El __Export__ puede ser un respaldo total o parcial de la configuración del router, el cual es un script de texto plano que no guarda ni los usuarios ni las contraseñas.

Pues una vez explicado eso, abrimos una terminal desde el router y copiamos uno de los dos script, lo pegamos en la terminal y le damos a _Intro_ para ejecutarlo, luego realizamos el mismo procedimiento con el otros script.

![Insertando ambos script en la terminal del route](./ImagenesPI/PIFase3/respaldo2.PNG "Insertando ambos script en la terminal del router")

Una vez ejecutado ambos script en la terminal vamos al menú izquierdo y luego a __System → Script__, en la ventana de _Script List_ nos deberá de aparecer dos archivos los cuales corresponden a los dos script ejecutados antes.

![Script en la lista de script](./ImagenesPI/PIFase3/respaldo3.PNG "Script en la lista de script")

Ahora deberemos de hacer algunas modificaciones a los dos script, hacemos doble clic por ejemplo en el _respaldobinario_ y buscamos la siguiente línea (/tool e-mail send to="youremail@yourdomain.com") en el cuadro de texto de abajo 
de la ventana, en esa línea debemos modificar lo que está entre comillas y agregar el correo al cual queremos que llegue el backup. 
También podemos fijarnos en la siguiente linea (subject=([/system identity get name]), esta línea hace referencia al nombre que le hayamos definido al router en __System Identity__, por lo tanto es bueno definir un nombre para cada router, no solo para identificarlo, sino para cuando nos llegue este correo sepamos a qué router hace referencia.

![Modificar el correo en los script](./ImagenesPI/PIFase3/respaldo4.PNG "Modificar el correo en los script")

Una vez cambiado el correo en ambos script pasamos a configurar el envío programado de los mismos, para ellos vamos al menú izquierdo, __System → Scheduler__ y luego al símbolo del (+).

![Ventana Scheduler](./ImagenesPI/PIFase3/respaldo5.PNG "Ventana Scheduler")

En la nueva ventana que nos aparece definiremos cuando se inicia y cada cuanto tiempo se ejecuta el script.
Por tanto en cada apartado configuraremos lo siguiente:
- __Name:__ Damos el nombre que queramos para definirlo
- __Start Date:__ Es la fecha en la cual empezará a ejecutarse esta tarea
- __Start Time:__ Es la hora de inicio en la cual emepazará a ejecutarse la tarea
- __Interval:__ Es el intervalo de tiempo, para que se ejecute nuevamente la tarea, es este ejemplo se a definido que sea una vez al dia es decir cada 24 horas
- __Owner:__ Hace referencia al propietario de la creación de la tarea, este aparece automáticamente al darle al botón _Apply_
- Las __Policies__ las podemos dejar por defecto todas marcadas
En el cuadro de texto de abajo escribimos el nombre del uno de los script que previamente creamos, para definir qué será eso lo que deberá ejecutar en el tiempo definido
Los demas campos se rellenan solos al darle al botón de _Apply_ le damos al OK para terminar.
Seguidamente creamos otra regla con el mismo tiemppo o distinto segun prefiramos para el otro script de respaldo el de __respaldoexport__.

![Creando la tarea programada para el primer script](./ImagenesPI/PIFase3/respaldo6.PNG "Creando la tarea programada para el primer script")

Al final nos quedarán ambas reglas creadas como en la imagen siguiente.

![Tareas programadas creadas](./ImagenesPI/PIFase3/respaldo7.PNG "Tareas programadas creadas")

## Layer 7

Vamos a configurar nuestro router mikrotik con layer 7 para filtrar ciertos paquetes y de esta manera bloquear el acceso a ciertas páginas web.

Nuestro primer paso será ir a __IP → Firewall__ y luego a la pestaña de _Layer 7 Protocols_, una vez aquí le damos al símbolo (+) y en la ventana que nos aparece definimos el nombre que nosotros queramos en el aparatado _Name_ y en el apartado _Regexp_ será donde insertemos una expresión regular.
En este caso se insertó la siguiente expresion regular:

~~~
^.+(youporn.com|pornhub.com|xvideos.com|xvideos|pornstars|youtube.com|youtu.be|googlevideo.com|facebook).*$
~~~

La idea será bloquear las paginas que vienen definidas en la expresión regular.
Aplicamos y Ok.

![Definiendo los Protocolos L7](./ImagenesPI/PIFase3/L7.PNG "Definiendo los Protocolos L7")

Nuestro siguiente paso será estando en la ventana de _Firewall_ ir a la pestaña de _Mangle_. 
Una vez aquí crearemos dos reglas.
La primera regla será para marcar las conexiones que van por DNS y que  cumplan el protocolo de L7 antes definido.
Para ello realizaremos lo siguiente, en la ventana que nos aparece al crear una nueva regla estando en la pestaña _General_  seleccionamos __prerouting__ en el apartado _chain_, en el apartado de _Protocol_ seleccionamos __UDP__,
en el apartado de _Dst.Port_ escribimos __53__ y en el apartado de _Connection Mark_ seleccionamos __no-mark__.
Ahora pasamos a la pestaña de Advanced, aquie solo debemos ir al aparatado de _Layer 7 Protocol_ y selecionar el protocolo que definimos anteriormente en Layer7, si tenemos varios pues seleccionamos el que nos interese, ya que podemos crear todos los protocolos de layer7 que queramos según nuestras necesidades.
Luego pasamos a la pestaña de _Action_, en ella seleccionamos __mark connection__ en el apartado de _Action_, en _New Connection Mark_  definimos un nombre que nosotros queramos y el _Passthough_ lo dejamos marcado para que pase a la siguiente regla. Aplicamos y OK.

![Configurar regla mangle pestaña general ](./ImagenesPI/PIFase3/L7manglegeneral.PNG "Configurar regla mangle pestaña general")

![Configurar regla mangle pestaña advanced](./ImagenesPI/PIFase3/L7mangleadvanced.PNG "Configurar regla mangle pestaña advanced")

![Configurar regla mangle pestaña action](./ImagenesPI/PIFase3/L7mangleaction.PNG "Configurar regla mangle pestaña action")

Ahora crearemos la otra regla para marcar los paquetes que provengan de las conexiones marcadas de la anterior regla.
Estando en la pestaña _General_ tan solo seleccionamos __prerouting__ en el apartado de _chain_ y en _Connection Mark_ seleccionamos el nombre que definimos en la anterior regla para las conexiones marcadas.
Luego pasamos a la pestaña _Action_, en esta seleccionamos __mark packet__ en el apartado de _Action_, definimos un nombre que nosotros queramos en el apartado de _New Packet Mark_ y marcamos el _Passthrough_.Aplicamos y ok.

![Configurar segunda regla mangle pestaña general](./ImagenesPI/PIFase3/L7manglegeneral2.PNG "Configurar segunda regla mangle pestaña general")

![Configurar segunda regla mangle pestaña action](./ImagenesPI/PIFase3/L7mangleaction2.PNG "Configurar segunda regla mangle pestaña action")

Ahora pasamos a crear las reglas de Firewall, entonces en la ventana de Firewall vamos a la pestaña de _Filter Rules_  y creamos dos reglas cuya _Action_ será __drop__, y en la pestaña _General_ en el apartado de _Packet Market_ seleccionamos el nombre que definimos en la segunda regla de mangle que usamos para definir los paquetes marcados.
La única diferencia de estas dos reglas será en el apartado _Chain_ donde uno hará referencia a la cadena __forward__ para prohibir las peticiones que coincidan con la definición de L7 señalada , y la otra regla hace referencia a la cadena  __Input__ porque en casos normales el router hace  las veces de DNS para la red.

![Configurar regla firewall pestaña general ](./ImagenesPI/PIFase3/L7firewallgeneral.PNG "Configurar regla firewall pestaña general")

![Configurar regla firewall pestaña action](./ImagenesPI/PIFase3/L7firewallaction.PNG "Configurar regla firewall pestaña action")

[Inicio](https://franciscocadena.github.io/PI-Mikrotik/)


File: /Definiciones.md
[Inicio](https://franciscocadena.github.io/PI-Mikrotik/)

# Definiciones

## Drop vs Reject

Para paquetes que vengan del exterior lo recomendable es usar _DROP_, para los paquetes dentro de una red Local o privada puede usarse _Reject_.
La opción REJECT envía un mensaje ICMPP avisando que fue rechazada, sin embargo esto puede ser usado por otras personas que realicen un ataque DDOS (denegación de servicios). Muchos de estos ataques son falsificaciones, que se aprovechan de la ventaja de REJECT vs DROP. 

## Port knocking

El bloqueo de puertos es un método que permite el acceso al enrutador solo después de recibir intentos de conexión secuenciados en un conjunto de puertos cerrados previamente especificados. Una vez que se recibe la secuencia correcta de los intentos de conexión, el RouterOS agrega dinámicamente una IP de origen del host a la lista de direcciones permitidas y podrá conectar su enrutador.

Mejora la seguridad de nuestro dispositivo y minimizar el riesgo de intentos de piratería en protocolos como SSH, Telnet, Winbox, etc.

## Expresión regular

Las expresiones regulares son patrones utilizados para encontrar una determinada combinación de caracteres dentro de una cadena de texto. Las expresiones regulares proporcionan una manera muy flexible de buscar o reconocer cadenas de texto. Por ejemplo, el grupo formado por las cadenas Handel, Händel y Haendel se describe con el patrón `"H(a|ä|ae)ndel"`.

## IPsec

Internet Protocol Security (IPsec) es un conjunto de protocolos definidos por Internet Engineering Task Force (IETF) para asegurar el intercambio de paquetes a través de redes IP / IPv6 desprotegidas como Internet.El conjunto de protocolos IPsec se puede dividir en los siguientes grupos:

- __Protocolos de intercambio de claves de Internet (IKE)__. Genera y distribuye dinámicamente claves criptográficas para AH y ESP.

Es un protocolo que proporciona material de claves autenticado para el marco de la Asociación de seguridad de Internet y el Protocolo de administración de claves (ISAKMP). Existen otros esquemas de intercambio de claves que funcionan con ISAKMP, pero IKE es el más utilizado. Juntos proporcionan medios para la autenticación de hosts y la gestión automática de asociaciones de seguridad (SA).

- __Encabezado de autenticación (AH) RFC 4302__

Es un protocolo que proporciona autenticación de todo o parte del contenido de un datagrama mediante la adición de un encabezado que se calcula en función de los valores en el datagrama. Las partes del datagrama que se usan para el cálculo y la ubicación del encabezado dependen de si se usa el modo túnel o transporte.

La presencia del encabezado AH permite verificar la integridad del mensaje, pero no lo encripta. Por lo tanto, AH proporciona autenticación pero no privacidad. Otro protocolo (ESP) se considera superior, proporciona privacidad de datos y también su propio método de autenticación.

- __Carga de seguridad de encapsulación (ESP) RFC 4303__

Utiliza cifrado de clave compartida para proporcionar privacidad de datos. ESP también admite su propio esquema de autenticación como el utilizado en AH.

ESP empaqueta sus campos de una manera muy diferente a AH. En lugar de tener solo un encabezado, divide sus campos en tres componentes:

- _Encabezado ESP_: viene antes de los datos cifrados y su ubicación depende de si ESP se usa en modo de transporte o en túnel.
- _ESP Trailer_: esta sección se coloca después de los datos cifrados. Contiene relleno que se utiliza para alinear los datos cifrados.
- _Datos de autenticación ESP_: este campo contiene un valor de comprobación de integridad (ICV), calculado de manera similar a cómo funciona el protocolo AH, para cuando se utiliza la función de autenticación opcional de ESP.

## Datagramas

Paquete sencillo enrutado en una red sin reconocimiento.

Un __datagrama__ es un fragmento de paquete que es enviado con la suficiente información como para que la red pueda simplemente encaminar el fragmento hacia el ordenador receptor, de manera independiente a los fragmentos restantes. Esto puede provocar una recomposición desordenada o incompleta del paquete en el ordenador destino. Su estructura se compone de _cabecera y datos_.

## TZSP

TaZmen Sniffer Protocol (TZSP) es un protocolo de encapsulación utilizado para envolver otros protocolos. Se usa comúnmente para envolver paquetes inalámbricos 802.11 para admitir sistemas de detección de intrusiones (IDS) , seguimiento inalámbrico u otras aplicaciones inalámbricas.
Usa el protocolo _UDP_ y el puerto 37008.

## PCAP

Es una interfaz de una aplicación de programación para captura de paquetes. La implementación del pcap para sistemas basados en Unix se conoce como libpcap; el port para Windows del libpcap recibe el nombre de WinPcap.

Algunos programas que usan pcap:
- Snort
- Suricata
- Nmap
- tcpdump

## Metodo PCC Matcher para el balanceo de carga

Permitirá dividir el tráfico en flujos iguales con la capacidad de mantener paquetes con un conjunto específico de opciones en un flujo particular (puede especificar este conjunto de opciones desde src-address, src-port, dst-address, dst-port)

PCC toma los campos seleccionados del encabezado IP y, con la ayuda de un algoritmo hash, convierte los campos seleccionados en un valor de 32 bits. Este valor se divide por un Denominador especificado y el resto se compara con un Remanente especificado , si es igual, se capturará el paquete. 

## VRRP

Virtual Router Redundancy Protocol (VRRP) es un protocolo de comunicaciones no propietario definido en el RFC 3768 diseñado para aumentar la disponibilidad de la puerta de enlace por defecto dando servicio a máquinas en la misma subred. El aumento de fiabilidad se consigue mediante el anuncio de un router virtual como una puerta de enlace por defecto en lugar de un router físico. Dos o más routers físicos se configuran representando al router virtual, con sólo uno de ellos realizando realmente el enrutamiento. Si el router físico actual que está realizando el enrutamiento falla, el otro router físico negocia para sustituirlo. Se denomina router maestro al router físico que realiza realmente el enrutamiento y routers de respaldo a los que están en espera de que el maestro falle.

## Protocol Layer 7

El protocolo layer7 es un método de búsqueda de patrones en flujos ICMP / TCP / UDP.
Funciona por medio de patrones pre-establecidos en la capa de Aplicación del modelo OSI.

L7 matcher recopila los primeros 10 paquetes de una conexión o los primeros 2 KB de una conexión y busca el patrón en los datos recopilados. Si el patrón no se encuentra en los datos recopilados, el comparador deja de inspeccionar más. La memoria asignada se libera y el protocolo se considera desconocido . Debe tener en cuenta que muchas conexiones aumentarán significativamente el uso de memoria y CPU.

El requisito adicional es que el emparejador de capa 7 debe ver ambas direcciones de tráfico (entrante y saliente). Para cumplir este requisito, las reglas deben establecerse en cadena hacia adelante . Si la regla se encuentra en entrada / prerouting cadena entonces la misma regla debe ser también situado en la salida / POSTROUTING cadena, de lo contrario los datos recogidos no puede ser completo que resulta en un patrón incorrectamente emparejado.

Para conocer el verdadero proposito con el que fue diseñado este protoloco, el cual no fue bloquear paginas web ni ningun tipo de censura, recomiendo ir a la pagian oficial yendo a este [enlace](http://l7-filter.sourceforge.net/) 

## ISP 

El proveedor de servicios de Internet, (ISP, por las siglas en inglés de Internet service provider) es la empresa que brinda conexión a Internet a sus clientes. Un ISP conecta a sus usuarios a Internet a través de diferentes tecnologías como ADSL, cablemódem, GSM, dial-up, etc.

## CGNAT (Carrier-Grade NAT o NAT444)

La idea es utilizar el espacio de direcciones compartido 100.64.0.0/10 dentro de la red del operador y realizar NAT en el enrutador de borde del operador para indicar IP pública o rango de IP pública. Lo que ocurre es que en lugar de hacer una vez NAT, hacen NAT dos veces.

![Diagrama de ejemplo de cgnat](imagenesGNS3/GNSFase3/CGNAT.PNG "Diagrama de ejemplo de cgnat")

## Gateway

La pasarela (en inglés gateway ) o puerta de enlace es el dispositivo que actúa de interfaz de conexión entre aparatos o dispositivos, y también posibilita compartir recursos entre dos o más ordenadores.

Su propósito es traducir la información del protocolo utilizado en una red inicial, al protocolo usado en la red de destino.

La pasarela es normalmente un equipo informático configurado para dotar a las máquinas de una red de área local (Local Area Network, LAN) conectadas a él de un acceso hacia una red exterior, generalmente realizando para ello operaciones de traducción de direcciones de red (Network Address Translation, NAT). Esta capacidad de traducción de direcciones permite aplicar una técnica llamada enmascaramiento de IP , usada muy a menudo para dar acceso a Internet a los equipos de una LAN compartiendo una única conexión a Internet, y por tanto, una única dirección IP externa.

## RoMON (Router Manager Overlay Network)

Protocolo propietario de Mikrotik, no activo por defecto, el cual permite enlazar y acceder a dispositivos routerOS que se encuentren tanto en capa 2 (nivel de enlace de datos) como en capa 3 (nivel de red) con versión 6.28 o superior en una red a través de winbox v3.x. Solo se necesita activar este protocolo en los routerOs que se deseen acceder

## Balanceo de Carga

Divide el tráfico entre interfaces de red de capa 4 (nivel de transporte).
Es sumamente útil donde existen enlaces de comunicación redundantes, ya que todos los enlaces se pueden utilizar al mismo tiempo.
Al utilizar múltiples enlaces de forma simultanea. se incrementa la disponibilidadd del ancho de banda. De esta fomra se evita la congestión o saturación de la red en un solo enlace.

[Inicio](https://franciscocadena.github.io/PI-Mikrotik/)


File: /Fase1_GNS3.md
[Inicio](https://franciscocadena.github.io/PI-Mikrotik/)

# Fase 1 con GNS3

En este apartado veremos el esquema de la topografía de red con gns3 según la fase 1, y como queda la configuración del router principal.

![topografía de red con gns3](./imagenesGNS3/fase1gns3.PNG "topografía de red con gns3")

Direcciones ip de las diferentes interfaces y bridges configuradas.

![Direccionamiento](./imagenesGNS3/direcciones.PNG "Direccionamiento")

Interfaces, vlans y bridges con nombres a las que estan configuradas.

![Interfaces definidas](./imagenesGNS3/interfaces.PNG "Interfaces definidas")

Dhcp cliente para la WAN que recibe la ip de un ISP que en este caso es el router de casa.

![dhcp cliente](./imagenesGNS3/dhcpcliente.PNG "dhcp cliente")

Dhcp server para los bridges.

![Dhcp server bridges](./imagenesGNS3/dhcpserver.PNG "Dhcp server bridges")

Dhcp server con las redes, gateway y dns.

![Dhcp server Network](./imagenesGNS3/dhcpserverredes.PNG "Dhcp server Network")

Dhcp server con las ip arrendadas.

![Dhcp server Leases](./imagenesGNS3/dhcpserverarrendada.PNG "Dhcp server Leases")

DNS.

![DNS](./imagenesGNS3/dns.PNG "DNS")

Lista de rutas.

![Route List](./imagenesGNS3/lista_de_rutas.PNG "Route List")

Configuracion de los puertos de los bridges donde se observa con que vlan e interfaces estan puenteadas.

![Bridges Ports](./imagenesGNS3/bridgesports.PNG "Bridges Ports")

Configuración de Nat por Firewall.

![Firewall NAT](./imagenesGNS3/firewallnat.PNG "Firewall NAT")

Reglas de Firewall.

![Firewall Rules](./imagenesGNS3/firewallreglas.PNG "Firewall Rules")

Politicas del tunel por IPsec.

![IPsec Policies](./imagenesGNS3/IPsecpolitica.PNG "IPsec Policies")

Vecinos que estan activos por el tunel creado.

![Ipsec Active Peers](./imagenesGNS3/ipsecvecinoactivo.PNG "Ipsec Active Peers")

[Inicio](https://franciscocadena.github.io/PI-Mikrotik/)








File: /Fase2_GNS3.md
[Inicio](https://franciscocadena.github.io/PI-Mikrotik/)

# Fase 2 con GNS3

En este apartado se verá la configuración de todos los router usando gns3,  según la siguiente imagen, que corresponde a la Fase 2 del proyecto.

![Topografia de la Fase 2 Virtualizado con GNS3](./imagenesGNS3/GNSFase2/gns3fase2.PNG "Topografia de la Fase 2 Virtualizado con GNS3")

Como se puede observar en la imagen anterior, la topografía de red ha sido simplificada con respecto a lo visto del diagrama de la fase 2 del apartado [Planificación de la Red Empresarial](./Planificación_de_la_Red_de_una_empresa.md).

Esto es debido porque a la hora de simular dos proveedores de internet, no es posible hacerlo usando solo la red que te da tu propio router de casa, por ello como sustitución de los dos ISP se a usado todos los interfaces que se pueden incorporar a la _OVA de GNS3_ que está siendo virtualizado por _Virtualbox_.

Esto quiere decir que todas las _nubes_ que se ven en el diagrama corresponden a la _ova de gns3_, el cual consta de __tres interfaces__, uno en modo anfitrión, otro en modo Nat y el último en modo Bridge, usando estos dos últimos que tienen salida a internet como si fuesen dos ISP.

También se a _simplificado las vlan_, porque sabiendo configurar dos, se sabe configurar todas las que se quieran, con ello es más fácil de entender y simplificar las reglas que tendrán cada router.

Cabe también destacar que el Router que está en la red de las vlan, es un Switch siendo simulado con el sistema operativo RouterOS, de hay que la imagen sea como la de un router.
 
A continuación se mostrará la configuración de cada uno de los router, para esta topografía de red donde ya tienen incorporado las herramientas de Alta disponibilidad que se explicaron en el documento de [Configuración de Herramientas de alta Disponibilidad](./Configuración_Herramientas_Alta_Disponibilida.md).
De hay que solo se muestre la configuración final, sin entrar en detalles de como configurarlos.

## Router Sede Madrid

### Quick Set

Se puede observar, que el router de la sede de Madrid tan solo trabaja con dos interfaces una WAN con ip estática, y una red LAN.

![Configuración Rapida del Router de Madrid](./imagenesGNS3/GNSFase2/gns3madridquickset.PNG "Configuración Rapida del Router de Madrid")

### Nat

Esta sería la regla de enmascaramiento y la regla que permite la navegación de la red lan de la sede de madrid con la red lan de la sede de sevilla por el vpn configurado.

![Reglas NAT del Router de Madrid](./imagenesGNS3/GNSFase2/gns3madridnat.PNG "Reglas NAT del Router de Madrid")

### Routes List

La siguiente imagen corresponde a las rutas creadas para la wan y para la lan.

![Lista de Rutas del Router de Madrid](./imagenesGNS3/GNSFase2/gns3madridroutes.PNG "Lista de Rutas del Router de Madrid")

### VPN IPsec

A Continuación se muestra la reglas configuradas para la creación del vpn con los dos router de la sede de sevilla.
 
Lo primero son los __Peer (vecinos)__.

![Pestaña Peer del Router de Madrid](./imagenesGNS3/GNSFase2/gns3madridpeers.PNG "Pestaña Peer del Router de Madrid")

En la siguiente imagen vemos las __Policies (Políticas)__ para cada vecino, donde se puede observar que uno de ellos está en _rojo_, ese corresponde al _router backup de la sede de sevilla_, con lo que si se pierde la conexión vpn con el router principal de sevilla, saltaría la conexión de vpn con el router backup de sevilla.

![Pestaña Policies del Router de Madrid](./imagenesGNS3/GNSFase2/gns3madridpolicies.PNG "Pestaña Policies del Router de Madrid")

Por último se ve en la siguiente imagen la conexión establecida con los vecinos activos donde se ve que se ha establecido conexión de _iniciador y respondedor_ con ambos router de sevilla.

![Pestaña Active Peer del Router de Madrid](./imagenesGNS3/GNSFase2/gns3madridactivepeer.PNG "Pestaña Active Peer del Router de Madrid")

## Router Master Sevilla

Ahora pasamos a ver la configuración del router principal de la sede de sevilla.

### Interfaces

Lo primero es ver las interfaces que tiene, en donde se ve por el nombre dado que tiene _tres interfaces que van por WAN_, las interfaces que van a las respectivas _redes locales (DMZ, LAN2, LAN “VLAN”)_, porque interfaz van las _vlan 10 y 20_,  y los _vrrp_ creados que van a las interfaces cuyo direccionamiento de red local es estático. 

![Interfaces del Router Master de Sevilla](./imagenesGNS3/GNSFase2/gns3masterinterface.PNG "Interfaces del Router Master de Sevilla")

### Dhcp y Dns

En la siguiente imagen se muestra el dns, y los dhcp server creados, los cuales van a las vlan.

![Dhcp y DNS del Router Master de Sevilla](./imagenesGNS3/GNSFase2/gns3masterdhcpdns.PNG "Dhcp y DNS del Router Master de Sevilla")

### VRRP

En la siguiente imagen se ven los vrrp creados, donde lo más importante aparte del nombre son la _Priority y el VRID_.

![VRRP creados en el Router Master de Sevill](./imagenesGNS3/GNSFase2/gns3mastervrrp.PNG "VRRP creados en el Router Master de Sevilla")

### IP de las interfaces

En la siguiente imagen se ve el direccionamiento de cada interfaz, vlan y vrrp.

![Direcciones de las interfaces del Router Master de Sevilla](./imagenesGNS3/GNSFase2/gns3masterips.PNG "Direcciones de las interfaces del Router Master de Sevilla")

### VPN por IPsec

Esta sería la configuración de Peer con la sede de Madrid.

![Pestaña Peer del Router Master de Sevilla](./imagenesGNS3/GNSFase2/gns3masterpeer.PNG "Pestaña Peer del Router Master de Sevilla")

Seguidamente vemos la Política asociada.

![Pestaña Ploicies del Router Master de Sevilla](./imagenesGNS3/GNSFase2/gns3masterpolicies.PNG "Pestaña Ploicies del Router Master de Sevilla")

Y por último el vecino Activo.

![Pestaña Active Peer del Router Master de Sevilla](./imagenesGNS3/GNSFase2/gns3masteractivepeer.PNG "Pestaña Active Peer del Router Master de Sevilla")

### Nat

En la siguiente imagen vemos las reglas de Nat creadas donde en primer lugar está la regla que permite la conexión de las redes locales entre las sedes de Sevilla y Madrid que van por vpn.
Luego el enmascaramiento de las tres interfaces wan.
Y por último las redirecciones de puerto para los servidores.

![Reglas Nat del Router Maestro de Sevilla](./imagenesGNS3/GNSFase2/gns3masternat.PNG "Reglas Nat del Router Maestro de Sevilla")

### Firewall

Estas serían las reglas de firewall, donde no hay muchos cambios con las ya creadas en la Fase 1.

![Reglas Firewall del Router Maestro de Sevilla](./imagenesGNS3/GNSFase2/gns3masterfirewall.PNG "Reglas Firewall del Router Maestro de Sevilla")

### Mangle (Reglas de Marcado)

En la siguiente imagen se ve las reglas creadas para el balanceo de carga por PCC, donde aunque tengamos tres interfaces WAN, solo se han usado dos de estas para el balanceo, el cual va dirigido para la DMZ.

![Reglas Mangle del Router Maestro de Sevilla](./imagenesGNS3/GNSFase2/gns3mastermangle.PNG "Reglas Mangle del Router Maestro de Sevilla")

### Routes List

En la siguiente imagen vemos todas las rutas creadas, en donde se puede ver el __failover__ definido por la _distance_, estos están en color celeste y en modo estático, esperando a que el principal caiga y activarse la siguiente que esté definida.
También se puede ver los dos interfaces que se están usando para el __balanceo de carga__ donde dice _routing mask_ que hacen referencia a que proveedor de internet va cada uno.
Podemos ver también las rutas correspondientes para las _vlan y los vrrp_.

![Lista de Rutas del Router Master de Sevilla](./imagenesGNS3/GNSFase2/gns3masterroutes.PNG "Lista de Rutas del Router Master de Sevilla")

### Ancho de Banda

En esta imagen podemos ver la configuración del _ancho de banda_ el cual consta de dos reglas una definida para toda la red LAN2 y otra que va primero para definir un determinado equipo dentro de la red LAN2.

![Reglas Queues (colas ) del Router Master de Sevilla](./imagenesGNS3/GNSFase2/gns3masterqueue.PNG "Reglas Queues (colas ) del Router Master de Sevilla")

## Router Backup de Sevilla

Ahora pasamos a la configuración del router de respaldo de la sede de sevilla, el cual tendrá reglas muy parecidas al del router master, donde la mayor diferencia será en las ip de las interfaces, y prioridades en los vrrp.

### Interfaces

La distribución y nombre de las interfaces son las mismas que las de router master, la mayor diferencia está en el nombre de las vlan.

![Interfaces Router Backup de Sevilla](./imagenesGNS3/GNSFase2/gns3backupinterfaces.PNG "Interfaces Router Backup de Sevilla")

### Dhcp y DNS

La única diferencia visible es el nombre de las vlan.

![Dhcp y DNS Router Backup de Sevilla](./imagenesGNS3/GNSFase2/gns3backupdhcpdns.PNG "Dhcp y DNS Router Backup de Sevilla")

### VRRP

En la VRRP la mayor diferencia radica en la prioridad, está al ser menos pasa a ser la de respaldo, mientras que la de router master al tener un número mayor pasa a ser el principal, el VRID y la ip deben ser idénticos a los que se definió en el router master.

![Vrrp creadas en Router Backup de Sevilla](./imagenesGNS3/GNSFase2/gns3backupvrrp.PNG "Vrrp creadas en Router Backup de Sevilla")

### IP de las Interfaces

En las ip de las interfaces es donde se aprecia la mayor diferencia de ambos routers, se puede apreciar el color rojo de los vrrp, esto es debido a que están de respaldo, es decir están a la espera de que si se cae el router master estas pasarían a estar activas.

![IP de las interfaces del Router Backup de Sevilla](./imagenesGNS3/GNSFase2/gns3backupips.PNG "IP de las interfaces del Router Backup de Sevilla")

### VPN por IPsec

Configuración de la vpn en el Router Backup de Sevilla.

Pestaña Peer del Router Backup de Sevilla.

![Pestaña Peer del Router Backup de Sevilla.](./imagenesGNS3/GNSFase2/gns3backuppeer.PNG "Pestaña Peer del Router Backup de Sevilla.")

Pestaña Policies del Router Backup de Sevilla.

![Pestaña Policies del Router Backup de Sevilla.](./imagenesGNS3/GNSFase2/gns3backupplocies.PNG "Pestaña Policies del Router Backup de Sevilla.")

Pestaña Active Peer del Router Backup de Sevilla.

![Pestaña Active Peer del Router Backup de Sevilla.](./imagenesGNS3/GNSFase2/gns3backupactivepeer.PNG "Pestaña Active Peer del Router Backup de Sevilla.")

### NAT

Reglas Nat del Router Backup de Sevilla

![Reglas Nat del Router Backup de Sevilla](./imagenesGNS3/GNSFase2/gns3backupnat.PNG "Reglas Nat del Router Backup de Sevilla")

### Firewall

Reglas Firewall del Router Backup de Sevilla

![Reglas Firewall del Router Backup de Sevilla](./imagenesGNS3/GNSFase2/gns3backupfirewall.PNG "Reglas Firewall del Router Backup de Sevilla")

### Mangle

Reglas de Marcado del Router Backup de Sevilla

![Reglas de Marcado del Router Backup de Sevilla](./imagenesGNS3/GNSFase2/gns3backupmangle.PNG "Reglas de Marcado del Router Backup de Sevilla")

### Routes List

En la lista de rutas del router backup de Sevilla, apenas se ven diferencia con el maestro, pero hay un detalle y es que no aparecen las rutas para las vrrp, esto es debido a que no están activas, si el router master se dañase por algún motivo, se activarán los vrrp de respaldo y entonces si aparecen las rutas de estos en el router backup. 

![Lista de Rutas del Router Backup de Sevilla](./imagenesGNS3/GNSFase2/gns3backuproutes.PNG "Lista de Rutas del Router Backup de Sevilla")

### Ancho de Banda

Reglas Queues del Router Backup de Sevilla

![Reglas Queues del Router Backup de Sevilla](./imagenesGNS3/GNSFase2/gns3backupqueue.PNG "Reglas Queues del Router Backup de Sevilla")

## Switch simulado por RouterOS

Por último veremos la configuración que tiene el _Switch_ de la red LAN donde están la vlans, el cual a sido simulado usando también el sistema operativo _RouterOS_, de hay que la imagen sea la de un router en vez de la de un Switch.

La primera imagen hace referencia al __Quick Set__ o configuración inicial, donde lo más destacable de aquí es donde dice _Mode_ que está activa la opción de _Bridge_ en vez de la de router como en todos los demás router configurados. 
También se puede apreciar que el direccionamiento de este es _dinámico_ y no requiere de _DNS_.

![Quick Set del Switch](./imagenesGNS3/GNSFase2/gns3switchquickset.PNG "Quick Set del Switch")

La siguiente imagen hace referencia a los diferentes _Bridges_ que se han creado en el Switch.
A diferencia de la _Fase 1_ donde el mismo router creaba las vlan, le daba direccionamiento y los repartía por los puertos. 
En esta fase se ha configurado de una manera más real, en donde los router master y backup tienen creadas las vlan, le dan un direccionamiento por Dhcp Server y definen porque interfaz salen, y el Switch por enlace troncal recibe esas vlan, las cuales también están creadas en el Switch, pero también tiene creadas los bridges para posteriormente definir por qué puerto ira cada vlan.

![Bridges creados en el Switch](./imagenesGNS3/GNSFase2/gns3switchbridge.PNG "Bridges creados en el Switch")

En la siguiente imagen se puede ver la asignación de cada interfaz con su bridge, donde podemos observar lo siguiente:
- Los dos interfaces WAN están en un mismo Bridge, esto será para luego definirlo en una Ruta de respaldo.
- Se puede ver las vlan definidas en el router master y el backup, que pertenecen a un mismo Bridge con el reparto de interfaces, con esto aseguramos que si cae el router master las vlan definidas en el router de respaldo las cuales tendrán el mismo direccionamiento que en el mater  ocuparan su lugar.
- Por último se puede ver un reparto de interfaces para cada vlan por medio de los Bridges. 

![Creación de Puertos para cada Bridges.](./imagenesGNS3/GNSFase2/gns3switchports.PNG "Creación de Puertos para cada Bridges.")

En la siguiente imagen se ven las interfaces del Switch.
- En donde podemos ver los Bridges creados.
- Las Vlan creadas y vinculadas, cada una a la interfaz que corresponden al router conectado que le proporciona el direccionamiento.
- Y también se pueden ver las interfaces que están en modo _slave (esclavo)_ con la letra __S__, esperando a que se conecte un equipo, y cuales están _running (corriendo)_ definidos por la letra __R__.

![Interfaces del Switch](./imagenesGNS3/GNSFase2/gns3switchinterface.PNG "Interfaces del Switch")

Por último vemos las rutas creadas en el Switch, donde se puede observar dos curiosidades:
- El Failover creado en el _Bridge_Lan_, y con gateway diferente, correspondiendo cada uno al router maestro y otro al backup, como ambos interfaces están vinculados con ese bridge, al caer uno se activaria el que está a la espera.
- También podemos ver que no aparecen las rutas de las vlan, eso es porque están en la lista de rutas de ambos router.

![Lista de Rutas del Switch](./imagenesGNS3/GNSFase2/gns3switchroutes.PNG "Lista de Rutas del Switch")

[Inicio](https://franciscocadena.github.io/PI-Mikrotik/)





















File: /Fase3_GNS3.md
[Inicio](https://franciscocadena.github.io/PI-Mikrotik/)

# Fase 3 con GNS3

En este apartado se muestra con la siguiente imagen como se a virtualizado la Fase 3 con GNS3 que se encuentra en el documento de planificación de red empresarial.

![Virtualización en GNS3 de la Fase 3](./imagenesGNS3//GNSFase3/gns3fase3.PNG "Virtualización en GNS3 de la Fase 3")

Esta vez en vez de mostrar las imágenes de la configuración final de cada router por winbox, se pasará los script de la configuración, para realizarla desde la terminal.

En esta fase están implementados y corriendo todo lo visto en las fases 1, 2 y 3, en donde los principales cambios han sido en las reglas de cortafuegos.

## Router Madrid

~~~
/interface ethernet
set [ find default-name=ether1 ] disable-running-check=no name=ether1-wan
set [ find default-name=ether2 ] disable-running-check=no name=ether2-D
set [ find default-name=ether3 ] disable-running-check=no
set [ find default-name=ether4 ] disable-running-check=no
set [ find default-name=ether5 ] disable-running-check=no
set [ find default-name=ether6 ] disable-running-check=no name=ether6-lan
/interface list
add name=WAN
add name=LAN
/interface wireless security-profiles
set [ find default=yes ] supplicant-identity=MikroTik
/ip ipsec peer
add address=192.168.0.32/32 local-address=192.168.0.40 name=sede3
add address=192.168.0.31/32 local-address=192.168.0.40 name=sede1
/ip pool
add name=dhcp_pool0 ranges=192.168.50.200-192.168.50.254
add name=dhcp_pool1 ranges=192.168.50.200-192.168.50.254
/ip dhcp-server
add address-pool=dhcp_pool1 disabled=no interface=ether6-lan name=dhcp2
/interface list member
add interface=ether1-wan list=WAN
add list=LAN
/ip address
add address=192.168.50.1/24 interface=ether6-lan network=192.168.50.0
add address=192.168.0.40/24 interface=ether1-wan network=192.168.0.0
/ip dhcp-client
add interface=ether1-wan
add dhcp-options=hostname,clientid interface=ether2-D
/ip dhcp-server network
add address=192.168.40.0/24 dns-server=\
    212.166.132.110,212.166.132.104,8.8.8.8,8.8.4.4 gateway=192.168.40.1
add address=192.168.50.0/24 gateway=192.168.50.1
/ip dns
set servers=8.8.8.8,8.8.4.4
/ip firewall nat
add action=accept chain=srcnat dst-address=192.168.20.0/24 src-address=\
    192.168.50.0/24
add action=masquerade chain=srcnat out-interface=ether1-wan
/ip ipsec identity
add peer=sede1 secret=Tik-academy
add peer=sede3 secret=Mikrotik
/ip ipsec policy
add dst-address=192.168.20.0/24 peer=sede1 sa-dst-address=192.168.0.31 \
    sa-src-address=192.168.0.40 src-address=192.168.50.0/24 tunnel=yes
add dst-address=192.168.20.0/24 peer=sede3 sa-dst-address=192.168.0.32 \
    sa-src-address=192.168.0.40 src-address=192.168.50.0/24 tunnel=yes
/ip route
add check-gateway=ping distance=1 gateway=192.168.0.1
/system identity
set name=Router-Madirid
/tool romon
set enabled=yes
~~~

## Router Master Sevilla

~~~
/interface ethernet
set [ find default-name=ether1 ] disable-running-check=no name=ether1-WAN1
set [ find default-name=ether2 ] disable-running-check=no name=ether2-WAN2
set [ find default-name=ether3 ] disable-running-check=no name=ether3-WAN3
set [ find default-name=ether4 ] disable-running-check=no name=ether4-Kali
set [ find default-name=ether5 ] disable-running-check=no name=\
    ether5-Suricata
set [ find default-name=ether6 ] disable-running-check=no
set [ find default-name=ether7 ] disable-running-check=no
set [ find default-name=ether8 ] disable-running-check=no
set [ find default-name=ether9 ] disable-running-check=no
set [ find default-name=ether10 ] disable-running-check=no name=ether10-LAN
set [ find default-name=ether11 ] disable-running-check=no name=ether11-LAN2
set [ find default-name=ether12 ] disable-running-check=no name=ether12-DMZ
/interface vrrp
add interface=ether11-LAN2 name=vrrp2 vrid=20
add interface=ether12-DMZ name=vrrp3 vrid=30
/interface vlan
add interface=ether10-LAN name=vlan10 vlan-id=10
add interface=ether10-LAN name=vlan20 vlan-id=20
/interface list
add name=WAN
add name=LAN
add name=vlanes
/interface wireless security-profiles
set [ find default=yes ] supplicant-identity=MikroTik
/ip firewall layer7-protocol
add name=Bloquear regexp="^.+(youporn.com|pornhub.com|xvideos.com|xvideos|porn\
    stars|youtube.com|youtu.be|googlevideo.com|facebook).*\$"
/ip ipsec peer
add address=192.168.0.40/32 local-address=192.168.0.31 name=sede2
/ip pool
add name=dhcp_pool4 ranges=192.168.4.100-192.168.4.254
add name=dhcp_pool5 ranges=192.168.10.200-192.168.10.254
add name=dhcp_pool6 ranges=10.10.10.200-10.10.10.254
add name=dhcp_pool7 ranges=20.20.20.200-20.20.20.254
/ip dhcp-server
add address-pool=dhcp_pool4 disabled=no interface=ether4-Kali name=dhcp4
add address-pool=dhcp_pool5 disabled=no interface=ether10-LAN name=dhcp1
add address-pool=dhcp_pool6 disabled=no interface=vlan10 name=dhcp2
add address-pool=dhcp_pool7 disabled=no interface=vlan20 name=dhcp3
/queue simple
add max-limit=256k/768k name=Admin-Vlan target=192.168.20.4/32
add max-limit=2M/2M name=Lan2 target=192.168.20.0/24
/system logging action
add email-start-tls=yes email-to=franciscomiguelcadenagarcia@gmail.com name=\
    email target=email
/interface list member
add interface=ether1-WAN1 list=WAN
add list=LAN
add list=LAN
add interface=ether2-WAN2 list=WAN
add interface=ether3-WAN3 list=WAN
add interface=vlan10 list=vlanes
add interface=vlan20 list=vlanes
/ip address
add address=192.168.30.1/24 interface=ether12-DMZ network=192.168.30.0
add address=192.168.20.1/24 interface=ether11-LAN2 network=192.168.20.0
add address=10.10.10.1/24 interface=vlan10 network=10.10.10.0
add address=20.20.20.1/24 interface=vlan20 network=20.20.20.0
add address=192.168.0.31/24 interface=ether1-WAN1 network=192.168.0.0
add address=192.168.1.2/24 interface=ether2-WAN2 network=192.168.1.0
add address=192.168.20.20 interface=vrrp2 network=192.168.20.20
add address=192.168.30.30 interface=vrrp3 network=192.168.30.30
add address=192.168.10.1/24 interface=ether10-LAN network=192.168.10.0
add address=10.0.3.10/24 interface=ether3-WAN3 network=10.0.3.0
add address=192.168.5.1/24 interface=ether5-Suricata network=192.168.5.0
add address=192.168.4.1/24 interface=ether4-Kali network=192.168.4.0
/ip dhcp-client
add interface=ether1-WAN1
add dhcp-options=hostname,clientid interface=ether3-WAN3
/ip dhcp-server network
add address=10.10.10.0/24 dns-server=8.8.8.8,8.8.4.4 gateway=10.10.10.1
add address=20.20.20.0/24 dns-server=8.8.8.8,8.8.4.4 gateway=20.20.20.1
add address=192.168.4.0/24 gateway=192.168.4.1
add address=192.168.10.0/24 gateway=192.168.10.1
/ip dns
set servers=8.8.8.8,8.8.4.4
/ip firewall filter
add action=add-src-to-address-list address-list=temporal \
    address-list-timeout=5m chain=input comment="Reglas de Port Knocking" \
    dst-port=2000 in-interface-list=WAN protocol=tcp
add action=add-src-to-address-list address-list=permitido \
    address-list-timeout=5m chain=input dst-port=4000 in-interface-list=WAN \
    protocol=tcp src-address-list=temporal
add action=add-src-to-address-list address-list=seguro address-list-timeout=\
    1h chain=input dst-port=8000 in-interface-list=WAN protocol=tcp \
    src-address-list=permitido
add action=accept chain=input src-address-list=seguro
add action=drop chain=forward comment="Filtro de paquetes de L7" packet-mark=\
    bloquear_packet
add action=drop chain=input packet-mark=bloquear_packet
add action=accept chain=forward comment="Permitir HTTP y HTTPS" dst-port=80 \
    protocol=tcp
add action=accept chain=output dst-port=80 out-interface-list=WAN protocol=\
    tcp
add action=accept chain=input in-interface-list=WAN protocol=tcp src-port=80
add action=accept chain=forward dst-port=8080 protocol=tcp
add action=accept chain=output dst-port=8080 protocol=tcp
add action=accept chain=input in-interface-list=WAN protocol=tcp src-port=\
    8080
add action=accept chain=forward dst-port=443 protocol=tcp
add action=accept chain=output dst-port=443 out-interface-list=WAN protocol=\
    tcp
add action=accept chain=input in-interface-list=WAN protocol=tcp src-port=443
add action=accept chain=forward comment="Permitir entrada por FTP" dst-port=\
    21 protocol=tcp
add action=accept chain=output dst-port=21 out-interface-list=WAN protocol=\
    tcp
add action=accept chain=input in-interface-list=WAN protocol=tcp src-port=21
add action=accept chain=forward comment="Permitir DNS" dst-port=53 protocol=\
    udp src-port=53
add action=accept chain=output dst-port=53 out-interface-list=WAN protocol=\
    udp
add action=accept chain=input in-interface-list=WAN protocol=udp src-port=53
add action=accept chain=output comment="Permitir ICMP" out-interface-list=WAN \
    protocol=icmp
add action=accept chain=input in-interface-list=WAN protocol=icmp
add action=accept chain=forward comment=\
    "Permitir conexiones entre Admin-Server y DMZ" dst-address=192.168.30.3 \
    dst-port=80 protocol=tcp src-address=192.168.20.3
add action=accept chain=forward dst-address=192.168.30.3 dst-port=8080 \
    protocol=tcp src-address=192.168.20.3
add action=accept chain=forward dst-address=192.168.30.3 dst-port=443 \
    protocol=tcp src-address=192.168.20.3
add action=accept chain=forward dst-address=192.168.30.4 dst-port=21 \
    protocol=tcp src-address=192.168.20.3
add action=accept chain=forward dst-port=22 protocol=tcp src-address=\
    192.168.20.3
add action=accept chain=forward dst-address=192.168.30.3 protocol=icmp \
    src-address=192.168.20.3
add action=accept chain=forward dst-address=192.168.30.4 protocol=icmp \
    src-address=192.168.20.3
add action=accept chain=forward dst-address=192.168.20.3 protocol=icmp \
    src-address=192.168.30.3
add action=accept chain=forward dst-address=192.168.20.3 protocol=icmp \
    src-address=192.168.30.4
add action=accept chain=forward comment=\
    "Permitir conexiones relacionadas y establecidas" connection-state=\
    established,related protocol=tcp
add action=accept chain=forward comment=\
    "Permitir conexiones entre Admin-LAN y LAN1 " in-interface=ether11-LAN2 \
    out-interface=ether10-LAN src-address=192.168.20.4
add action=accept chain=forward dst-address=192.168.20.4 in-interface=\
    ether10-LAN out-interface=ether11-LAN2
add action=accept chain=forward dst-address=10.10.10.0/24 src-address=\
    192.168.20.4
add action=accept chain=forward dst-address=20.20.20.0/24 src-address=\
    192.168.20.4
add action=accept chain=forward dst-address=192.168.20.4 src-address=\
    10.10.10.0/24
add action=accept chain=forward dst-address=192.168.20.4 src-address=\
    20.20.20.0/24
add action=drop chain=forward comment=\
    "Negar el resto de conexiones entre LAN2  y DMZ" dst-address=\
    192.168.30.0/24 src-address=192.168.20.0/24
add action=reject chain=forward in-interface=ether12-DMZ out-interface=\
    ether11-LAN2 reject-with=icmp-network-unreachable
add action=reject chain=forward comment=\
    "negar el resto de conexiones entre LAN2  y Vlanes" in-interface=\
    ether11-LAN2 out-interface-list=vlanes reject-with=\
    icmp-network-unreachable
add action=reject chain=forward in-interface-list=vlanes out-interface=\
    ether11-LAN2 reject-with=icmp-network-unreachable
add action=reject chain=forward comment=\
    "Negar conexiones entre DMZ  y Vlanes" in-interface=ether12-DMZ \
    out-interface-list=vlanes reject-with=icmp-network-unreachable
add action=reject chain=forward in-interface-list=vlanes out-interface=\
    ether12-DMZ reject-with=icmp-network-unreachable
add action=drop chain=forward comment="Negar conexiones entre vlanes" \
    dst-address=20.20.20.0/24 src-address=10.10.10.0/24
add action=drop chain=forward dst-address=10.10.10.0/24 src-address=\
    20.20.20.0/24
add action=drop chain=input comment="Denegar por Defecto" protocol=udp \
    src-port=!500,4500
add action=drop chain=output protocol=tcp src-port=!22,8291
add action=drop chain=output dst-port=!500,4500 protocol=udp
/ip firewall mangle
add action=sniff-tzsp chain=forward comment="Envio de trafico al IDS" \
    sniff-target=192.168.5.3 sniff-target-port=37008
add action=mark-connection chain=prerouting comment=\
    "Marcado de conexiones L7" connection-mark=no-mark dst-port=53 \
    layer7-protocol=Bloquear new-connection-mark=bloquear_con passthrough=yes \
    protocol=udp
add action=mark-packet chain=prerouting comment="Marcado de Paquetes de L7" \
    connection-mark=bloquear_con new-packet-mark=bloquear_packet passthrough=\
    yes
add action=accept chain=prerouting comment=\
    "Reglas de balanceo de carga para la DMZ" dst-address=192.168.0.0/24 \
    in-interface=ether12-DMZ
add action=accept chain=prerouting dst-address=10.0.3.0/24 in-interface=\
    ether12-DMZ
add action=mark-connection chain=prerouting connection-mark=no-mark \
    in-interface=ether1-WAN1 new-connection-mark=isp1_p passthrough=yes
add action=mark-connection chain=prerouting connection-mark=no-mark \
    in-interface=ether3-WAN3 new-connection-mark=isp3_t passthrough=yes
add action=mark-connection chain=prerouting connection-mark=no-mark \
    dst-address-type=!local in-interface=ether12-DMZ new-connection-mark=\
    isp1_p passthrough=yes per-connection-classifier=both-addresses:2/0
add action=mark-connection chain=prerouting connection-mark=no-mark \
    dst-address-type=!local in-interface=ether12-DMZ new-connection-mark=\
    isp3_t passthrough=yes per-connection-classifier=both-addresses:2/1
add action=mark-routing chain=prerouting connection-mark=isp1_p in-interface=\
    ether12-DMZ new-routing-mark=para_isp1 passthrough=yes
add action=mark-routing chain=prerouting connection-mark=isp3_t in-interface=\
    ether12-DMZ new-routing-mark=para_isp3 passthrough=yes
add action=mark-routing chain=output connection-mark=isp1_p new-routing-mark=\
    para_isp1 passthrough=yes
add action=mark-routing chain=output connection-mark=isp3_t new-routing-mark=\
    para_isp3 passthrough=yes
/ip firewall nat
add action=accept chain=srcnat comment="Permitir VPN entre redes" \
    dst-address=192.168.50.0/24 src-address=192.168.20.0/24
add action=accept chain=srcnat protocol=udp src-port=500,4500
add action=masquerade chain=srcnat comment=Enmascaramiento \
    out-interface-list=WAN
add action=dst-nat chain=dstnat comment="Redireccion de Puerto HTTP" \
    dst-port=80 in-interface-list=WAN protocol=tcp to-addresses=192.168.30.3
add action=dst-nat chain=dstnat dst-port=443 in-interface-list=WAN protocol=\
    tcp to-addresses=192.168.30.3
add action=dst-nat chain=dstnat dst-port=8080 in-interface-list=WAN protocol=\
    tcp to-addresses=192.168.30.3
add action=dst-nat chain=dstnat comment="Redireccion de Puertos FTP" \
    dst-port=21 in-interface-list=WAN protocol=tcp to-addresses=192.168.30.4
/ip ipsec identity
add peer=sede2 secret=Tik-academy
/ip ipsec policy
add dst-address=192.168.50.0/24 peer=sede2 sa-dst-address=192.168.0.40 \
    sa-src-address=192.168.0.31 src-address=192.168.20.0/24 tunnel=yes
/ip route
add check-gateway=ping distance=1 gateway=192.168.0.1 routing-mark=para_isp1
add check-gateway=ping distance=1 gateway=10.0.3.2 routing-mark=para_isp3
add check-gateway=ping distance=1 gateway=192.168.0.1
add check-gateway=ping distance=2 gateway=10.0.3.2
add distance=3 gateway=192.168.1.1
/system clock
set time-zone-name=Europe/Madrid
/system identity
set name=Router-Master-Sevilla
/system logging
add action=email disabled=yes topics=error
add action=email disabled=yes topics=dhcp
/system ntp client
set enabled=yes primary-ntp=216.239.35.4 secondary-ntp=130.206.3.166
/system scheduler
add interval=1d name=Respaldo_Binario on-event=respaldo_binario policy=\
    ftp,reboot,read,write,policy,test,password,sniff,sensitive,romon \
    start-date=jun/05/2020 start-time=12:00:00
add interval=1d name=Respaldo_Export on-event=respaldo_export policy=\
    ftp,reboot,read,write,policy,test,password,sniff,sensitive,romon \
    start-date=jun/05/2020 start-time=13:00:00
/system script
add dont-require-permissions=no name=respaldo_binario owner=admin policy=\
    ftp,reboot,read,write,policy,test,password,sniff,sensitive,romon source="/\
    system backup save name=([/system identity get name] . \"-\" . \\\
    \n[:pick [/system clock get date] 7 11] . [:pick [/system clock get date] \
    0 3] . [:pick [/system clock get date] 4 6]); \\\
    \n/tool e-mail send to=\"franciscomiguelcadenagarcia@gmail.com\" subject=(\
    [/system identity get name] . \" Backup \" . \\\
    \n[/system clock get date]) file=([/system identity get name] . \"-\" . [:\
    pick [/system clock get date] 7 11] . \\\
    \n[:pick [/system clock get date] 0 3] . [:pick [/system clock get date] 4\
    \_6] . \".backup\"); :delay 10; \\\
    \n/file rem [/file find name=([/system identity get name] . \"-\" . [:pick\
    \_[/system clock get date] 7 11] . \\\
    \n[:pick [/system clock get date] 0 3] . [:pick [/system clock get date] 4\
    \_6] . \".backup\")]; \\\
    \n:log info (\"System Backup emailed at \" . [/sys cl get time] . \" \" . \
    [/sys cl get date])"
add dont-require-permissions=no name=respaldo_export owner=admin policy=\
    ftp,reboot,read,write,policy,test,password,sniff,sensitive,romon source="/\
    export file=([/system identity get name] . \"-\" . \\\
    \n[:pick [/system clock get date] 7 11] . [:pick [/system clock get date] \
    0 3] . [:pick [/system clock get date] 4 6]); \\\
    \n/tool e-mail send to=\"franciscomiguelcadenagarcia@gmail.com\" subject=(\
    [/system identity get name] . \" Backup \" . \\\
    \n[/system clock get date]) file=([/system identity get name] . \"-\" . [:\
    pick [/system clock get date] 7 11] . \\\
    \n[:pick [/system clock get date] 0 3] . [:pick [/system clock get date] 4\
    \_6] . \".rsc\"); :delay 10; \\\
    \n/file rem [/file find name=([/system identity get name] . \"-\" . [:pick\
    \_[/system clock get date] 7 11] . \\\
    \n[:pick [/system clock get date] 0 3] . [:pick [/system clock get date] 4\
    \_6] . \".rsc\")]; \\\
    \n:log info (\"System Backup emailed at \" . [/sys cl get time] . \" \" . \
    [/sys cl get date])"
/tool e-mail
set address=173.194.76.108 from=franciscomiguelcadenagarcia@gmail.com \
    password=ddgiqcvsmccghwmp port=587 start-tls=yes user=\
    franciscomiguelcadenagarcia@gmail.com
/tool romon
set enabled=yes
~~~

## Router Backup Sevilla

~~~
/interface ethernet
set [ find default-name=ether1 ] disable-running-check=no name=ether1-WAN1
set [ find default-name=ether2 ] disable-running-check=no name=ether2-WAN2
set [ find default-name=ether3 ] disable-running-check=no name=ether3-WAN3
set [ find default-name=ether4 ] disable-running-check=no
set [ find default-name=ether5 ] disable-running-check=no name=\
    ether5-Suricata
set [ find default-name=ether6 ] disable-running-check=no
set [ find default-name=ether7 ] disable-running-check=no
set [ find default-name=ether8 ] disable-running-check=no
set [ find default-name=ether9 ] disable-running-check=no
set [ find default-name=ether10 ] disable-running-check=no name=ether10-LAN
set [ find default-name=ether11 ] disable-running-check=no name=ether11-LAN2
set [ find default-name=ether12 ] disable-running-check=no name=ether12-DMZ
/interface vrrp
add interface=ether11-LAN2 name=vrrp2 priority=50 vrid=20
add interface=ether12-DMZ name=vrrp3 priority=50 vrid=30
/interface vlan
add interface=ether10-LAN name=vlan10_respaldo vlan-id=10
add interface=ether10-LAN name=vlan20_respaldo vlan-id=20
/interface list
add name=WAN
add name=LAN
add name=vlanes
/interface wireless security-profiles
set [ find default=yes ] supplicant-identity=MikroTik
/ip firewall layer7-protocol
add name=Bloquear regexp="^.+(youporn.com|pornhub.com|xvideos.com|xvideos|porn\
    stars|youtube.com|youtu.be|googlevideo.com|facebook).*\$"
/ip ipsec peer
add address=192.168.0.40/32 local-address=192.168.0.32 name=sede2
/ip pool
add name=dhcp_pool0 ranges=192.168.10.200-192.168.10.254
add name=dhcp_pool1 ranges=10.10.10.200-10.10.10.254
add name=dhcp_pool2 ranges=20.20.20.200-20.20.20.254
add name=dhcp_pool3 ranges=30.30.30.200-30.30.30.254
/ip dhcp-server
add address-pool=dhcp_pool0 disabled=no interface=ether10-LAN name=dhcp1
add address-pool=dhcp_pool1 disabled=no interface=vlan10_respaldo name=dhcp2
add address-pool=dhcp_pool2 disabled=no interface=vlan20_respaldo name=dhcp3
/queue simple
add max-limit=256k/768k name=Admin-Vlan target=192.168.20.4/32
add max-limit=2M/2M name=LAN2 target=192.168.20.0/24
/system logging action
add email-start-tls=yes email-to=franciscomiguelcadenagarcia@gmail.com name=\
    email target=email
/interface list member
add interface=ether1-WAN1 list=WAN
add list=LAN
add interface=ether2-WAN2 list=WAN
add interface=ether3-WAN3 list=WAN
add interface=vlan10_respaldo list=vlanes
add interface=vlan20_respaldo list=vlanes
/ip address
add address=192.168.0.32/24 interface=ether1-WAN1 network=192.168.0.0
add address=192.168.30.2/24 interface=ether12-DMZ network=192.168.30.0
add address=192.168.20.2/24 interface=ether11-LAN2 network=192.168.20.0
add address=192.168.10.2/24 interface=ether10-LAN network=192.168.10.0
add address=10.10.10.2/24 interface=vlan10_respaldo network=10.10.10.0
add address=20.20.20.2/24 interface=vlan20_respaldo network=20.20.20.0
add address=192.168.30.30 interface=vrrp3 network=192.168.30.30
add address=192.168.20.20 interface=vrrp2 network=192.168.20.20
add address=192.168.1.3/24 interface=ether2-WAN2 network=192.168.1.0
add address=10.0.3.11/24 interface=ether3-WAN3 network=10.0.3.0
add address=192.168.6.1/24 interface=ether5-Suricata network=192.168.6.0
/ip dhcp-client
add interface=ether1-WAN1
add dhcp-options=hostname,clientid interface=ether3-WAN3
add dhcp-options=hostname,clientid interface=ether2-WAN2
/ip dhcp-server network
add address=10.10.10.0/24 dns-server=8.8.8.8,8.8.4.4 gateway=10.10.10.2
add address=20.20.20.0/24 dns-server=8.8.8.8,8.8.4.4 gateway=20.20.20.2
add address=192.168.10.0/24 gateway=192.168.10.2
/ip dns
set servers=8.8.8.8,8.8.4.4
/ip firewall filter
add action=add-src-to-address-list address-list=temporal \
    address-list-timeout=5m chain=input comment="Reglas de Port Knocking" \
    dst-port=3000 in-interface-list=WAN protocol=tcp
add action=add-src-to-address-list address-list=permitido \
    address-list-timeout=5m chain=input dst-port=5000 in-interface-list=WAN \
    protocol=tcp src-address-list=temporal
add action=add-src-to-address-list address-list=seguro address-list-timeout=\
    1h chain=input dst-port=7000 in-interface-list=WAN protocol=tcp \
    src-address-list=permitido
add action=accept chain=input in-interface-list=WAN src-address-list=seguro
add action=drop chain=forward comment="Filtro de paquetes de L7" packet-mark=\
    bloquear_packet
add action=drop chain=input packet-mark=bloquear_packet
add action=accept chain=forward comment="Permitir HTTP y HTTPS" dst-port=80 \
    protocol=tcp src-port=80
add action=accept chain=output dst-port=80 out-interface-list=WAN protocol=\
    tcp
add action=accept chain=input in-interface-list=WAN protocol=tcp src-port=80
add action=accept chain=forward dst-port=8080 protocol=tcp src-port=8080
add action=accept chain=output dst-port=8080 out-interface-list=WAN protocol=\
    tcp
add action=accept chain=input in-interface-list=WAN protocol=tcp src-port=\
    8080
add action=accept chain=forward dst-port=443 protocol=tcp src-port=443
add action=accept chain=output dst-port=443 out-interface-list=WAN protocol=\
    tcp
add action=accept chain=input in-interface-list=WAN protocol=tcp src-port=443
add action=accept chain=forward comment="Permitir entrada por FTP" dst-port=\
    21 protocol=tcp src-port=21
add action=accept chain=output dst-port=21 out-interface-list=WAN protocol=\
    tcp
add action=accept chain=input in-interface-list=WAN protocol=tcp src-port=21
add action=accept chain=forward comment="Permitir DNS" dst-port=53 protocol=\
    udp src-port=53
add action=accept chain=output dst-port=53 out-interface-list=WAN protocol=\
    udp
add action=accept chain=input in-interface-list=WAN protocol=udp src-port=53
add action=accept chain=output comment="Permitir icmp" out-interface-list=WAN \
    protocol=icmp
add action=accept chain=input in-interface-list=WAN protocol=icmp
add action=accept chain=forward comment=\
    "Permitir conexiones entre Admin-Server y DMZ" dst-address=192.168.30.3 \
    dst-port=80 protocol=tcp src-address=192.168.20.3
add action=accept chain=forward dst-address=192.168.30.3 dst-port=8080 \
    protocol=tcp src-address=192.168.20.3
add action=accept chain=forward dst-address=192.168.30.3 dst-port=443 \
    protocol=tcp src-address=192.168.20.3
add action=accept chain=forward dst-address=192.168.30.4 dst-port=21 \
    protocol=tcp src-address=192.168.20.3
add action=accept chain=forward dst-address=192.168.30.0/24 dst-port=22 \
    protocol=tcp src-address=192.168.20.3
add action=accept chain=forward dst-address=192.168.30.3 protocol=icmp \
    src-address=192.168.20.3
add action=accept chain=forward dst-address=192.168.30.4 protocol=icmp \
    src-address=192.168.20.3
add action=accept chain=forward dst-address=192.168.20.3 src-address=\
    192.168.30.3
add action=accept chain=forward dst-address=192.168.20.3 src-address=\
    192.168.30.4
add action=accept chain=forward comment=\
    "Permitir conexiones relacionadas y establecidas" connection-state=\
    established,related protocol=tcp
add action=accept chain=forward comment=\
    "Permitir conexiones entre Admin-LAN y LAN1 " in-interface=ether11-LAN2 \
    out-interface=ether10-LAN src-address=192.168.20.4
add action=accept chain=forward dst-address=192.168.20.4 in-interface=\
    ether10-LAN out-interface=ether11-LAN2
add action=accept chain=forward dst-address=10.10.10.0/24 src-address=\
    192.168.20.4
add action=accept chain=forward dst-address=20.20.20.0/24 src-address=\
    192.168.20.4
add action=accept chain=forward dst-address=192.168.20.4 src-address=\
    10.10.10.0/24
add action=accept chain=forward dst-address=192.168.20.4 src-address=\
    20.20.20.0/24
add action=drop chain=forward comment=\
    "Negar el resto de conexiones entre LAN2  y DMZ" dst-address=\
    192.168.30.0/24 src-address=192.168.20.0/24
add action=reject chain=forward in-interface=ether12-DMZ out-interface=\
    ether11-LAN2 reject-with=icmp-network-unreachable
add action=reject chain=forward comment=\
    "negar el resto de conexiones entre LAN2  y Vlanes" in-interface=\
    ether11-LAN2 out-interface-list=vlanes reject-with=\
    icmp-network-unreachable
add action=reject chain=forward in-interface-list=vlanes out-interface=\
    ether11-LAN2 reject-with=icmp-network-unreachable
add action=reject chain=forward comment=\
    "Negar conexiones entre DMZ  y Vlanes" in-interface=ether12-DMZ \
    out-interface-list=vlanes reject-with=icmp-network-unreachable
add action=reject chain=forward in-interface-list=vlanes out-interface=\
    ether12-DMZ reject-with=icmp-network-unreachable
add action=drop chain=forward comment="Negar conexiones entre vlanes" \
    dst-address=20.20.20.0/24 src-address=10.10.10.0/24
add action=drop chain=forward dst-address=10.10.10.0/24 src-address=\
    20.20.20.0/24
add action=drop chain=input comment="Denegar por Defecto" protocol=udp \
    src-port=!500,4500
add action=drop chain=output protocol=tcp src-port=!22,8291
add action=drop chain=output dst-port=!500,4500 protocol=udp
/ip firewall mangle
add action=sniff-tzsp chain=forward comment="Envio de trafico al IDS" \
    sniff-target=192.168.6.3 sniff-target-port=37008
add action=mark-connection chain=prerouting comment=\
    "Marcado de conexiones L7" connection-mark=no-mark dst-port=53 \
    layer7-protocol=Bloquear new-connection-mark=bloquear_con passthrough=yes \
    protocol=udp
add action=mark-packet chain=prerouting comment="Marcado de Paquetes de L7" \
    connection-mark=bloquear_con new-packet-mark=bloquear_packet passthrough=\
    yes
add action=accept chain=prerouting comment=\
    "Reglas de balanceo de carga para la DMZ" dst-address=192.168.0.0/24 \
    in-interface=ether12-DMZ
add action=accept chain=prerouting dst-address=10.0.3.0/24 in-interface=\
    ether12-DMZ
add action=mark-connection chain=prerouting connection-mark=no-mark \
    in-interface=ether1-WAN1 new-connection-mark=isp1_p passthrough=yes
add action=mark-connection chain=prerouting connection-mark=no-mark \
    in-interface=ether3-WAN3 new-connection-mark=isp3_t passthrough=yes
add action=mark-connection chain=prerouting connection-mark=no-mark \
    dst-address-type=!local in-interface=ether12-DMZ new-connection-mark=\
    isp1_p passthrough=yes per-connection-classifier=both-addresses:2/0
add action=mark-connection chain=prerouting connection-mark=no-mark \
    dst-address-type=!local in-interface=ether12-DMZ new-connection-mark=\
    isp3_t passthrough=yes per-connection-classifier=both-addresses:2/1
add action=mark-routing chain=prerouting connection-mark=isp1_p in-interface=\
    ether12-DMZ new-routing-mark=para_isp1 passthrough=yes
add action=mark-routing chain=prerouting connection-mark=isp3_t in-interface=\
    ether12-DMZ new-routing-mark=para_isp3 passthrough=yes
add action=mark-routing chain=output connection-mark=isp1_p new-routing-mark=\
    para_isp1 passthrough=yes
add action=mark-routing chain=output connection-mark=isp3_t new-routing-mark=\
    para_isp3 passthrough=yes
/ip firewall nat
add action=accept chain=srcnat comment="Permitir VPN entre redes" \
    dst-address=192.168.50.0/24 src-address=192.168.20.0/24
add action=accept chain=srcnat protocol=udp src-port=500,4500
add action=masquerade chain=srcnat comment=Enmascaramiento \
    out-interface-list=WAN
add action=dst-nat chain=dstnat comment="Redireccion de Puerto HTTP" \
    dst-port=80 in-interface-list=WAN protocol=tcp to-addresses=192.168.30.3
add action=dst-nat chain=dstnat dst-port=443 in-interface-list=WAN protocol=\
    tcp to-addresses=192.168.30.3
add action=dst-nat chain=dstnat dst-port=8080 in-interface-list=WAN protocol=\
    tcp to-addresses=192.168.30.3
add action=dst-nat chain=dstnat comment="Redireccion de Puertos FTP" \
    dst-port=21 in-interface-list=WAN protocol=tcp to-addresses=192.168.30.4
/ip ipsec identity
add peer=sede2 secret=Mikrotik
/ip ipsec policy
add dst-address=192.168.50.0/24 peer=sede2 sa-dst-address=192.168.0.40 \
    sa-src-address=192.168.0.32 src-address=192.168.20.0/24 tunnel=yes
/ip route
add check-gateway=ping distance=1 gateway=192.168.0.1 routing-mark=para_isp1
add check-gateway=ping distance=1 gateway=10.0.3.2 routing-mark=para_isp3
add check-gateway=ping distance=1 gateway=192.168.0.1
add check-gateway=ping distance=2 gateway=10.0.3.2
add distance=3 gateway=192.168.1.1
/system clock
set time-zone-name=Europe/Madrid
/system identity
set name=Router-Backup-Sevilla
/system logging
add action=email disabled=yes topics=dhcp
add action=email disabled=yes topics=error
/system ntp client
set enabled=yes primary-ntp=216.239.35.4 secondary-ntp=130.206.3.166
/system scheduler
add interval=1d name=Respaldo_Binario on-event=respaldo_binario policy=\
    ftp,reboot,read,write,policy,test,password,sniff,sensitive,romon \
    start-date=jun/06/2020 start-time=11:00:00
add interval=1d name=Respaldo_Export on-event=respaldo_export policy=\
    ftp,reboot,read,write,policy,test,password,sniff,sensitive,romon \
    start-date=jun/06/2020 start-time=14:00:00
/system script
add dont-require-permissions=no name=respaldo_binario owner=admin policy=\
    ftp,reboot,read,write,policy,test,password,sniff,sensitive,romon source="/\
    system backup save name=([/system identity get name] . \"-\" . \\\
    \n[:pick [/system clock get date] 7 11] . [:pick [/system clock get date] \
    0 3] . [:pick [/system clock get date] 4 6]); \\\
    \n/tool e-mail send to=\"franciscomiguelcadenagarcia@gmail.com\" subject=(\
    [/system identity get name] . \" Backup \" . \\\
    \n[/system clock get date]) file=([/system identity get name] . \"-\" . [:\
    pick [/system clock get date] 7 11] . \\\
    \n[:pick [/system clock get date] 0 3] . [:pick [/system clock get date] 4\
    \_6] . \".backup\"); :delay 10; \\\
    \n/file rem [/file find name=([/system identity get name] . \"-\" . [:pick\
    \_[/system clock get date] 7 11] . \\\
    \n[:pick [/system clock get date] 0 3] . [:pick [/system clock get date] 4\
    \_6] . \".backup\")]; \\\
    \n:log info (\"System Backup emailed at \" . [/sys cl get time] . \" \" . \
    [/sys cl get date])"
add dont-require-permissions=no name=respaldo_export owner=admin policy=\
    ftp,reboot,read,write,policy,test,password,sniff,sensitive,romon source="/\
    export file=([/system identity get name] . \"-\" . \\\
    \n[:pick [/system clock get date] 7 11] . [:pick [/system clock get date] \
    0 3] . [:pick [/system clock get date] 4 6]); \\\
    \n/tool e-mail send to=\"franciscomiguelcadenagarcia@gmail.com\" subject=(\
    [/system identity get name] . \" Backup \" . \\\
    \n[/system clock get date]) file=([/system identity get name] . \"-\" . [:\
    pick [/system clock get date] 7 11] . \\\
    \n[:pick [/system clock get date] 0 3] . [:pick [/system clock get date] 4\
    \_6] . \".rsc\"); :delay 10; \\\
    \n/file rem [/file find name=([/system identity get name] . \"-\" . [:pick\
    \_[/system clock get date] 7 11] . \\\
    \n[:pick [/system clock get date] 0 3] . [:pick [/system clock get date] 4\
    \_6] . \".rsc\")]; \\\
    \n:log info (\"System Backup emailed at \" . [/sys cl get time] . \" \" . \
    [/sys cl get date])"
/tool e-mail
set address=64.233.166.108 from=franciscomiguelcadenagarcia@gmail.com \
    password=tfmnpkpjtjczutsy port=587 start-tls=yes user=\
    franciscomiguelcadenagarcia@gmail.com
/tool romon
set enabled=yes
~~~

## Router Scwith

~~~
/interface bridge
add name=bridge_LAN
add name=bridge_vlan10
add name=bridge_vlan20
/interface ethernet
set [ find default-name=ether1 ] disable-running-check=no name=\
    ether1-WAN-Master
set [ find default-name=ether2 ] disable-running-check=no name=\
    ether2-WAN-Backup
set [ find default-name=ether3 ] disable-running-check=no
set [ find default-name=ether4 ] disable-running-check=no
set [ find default-name=ether5 ] disable-running-check=no
set [ find default-name=ether6 ] disable-running-check=no
set [ find default-name=ether7 ] disable-running-check=no
set [ find default-name=ether8 ] disable-running-check=no
set [ find default-name=ether9 ] disable-running-check=no
set [ find default-name=ether10 ] disable-running-check=no
set [ find default-name=ether11 ] disable-running-check=no
set [ find default-name=ether12 ] disable-running-check=no
/interface vlan
add interface=ether1-WAN-Master name=vlan10 vlan-id=10
add interface=ether2-WAN-Backup name=vlan10_respaldo vlan-id=10
add interface=ether1-WAN-Master name=vlan20 vlan-id=20
add interface=ether2-WAN-Backup name=vlan20_respaldo vlan-id=20
/interface list
add name=WAN
add name=LAN
/interface wireless security-profiles
set [ find default=yes ] supplicant-identity=MikroTik
/interface bridge port
add bridge=bridge_LAN interface=ether1-WAN-Master
add bridge=bridge_LAN interface=ether2-WAN-Backup
add bridge=bridge_LAN interface=ether5
add bridge=bridge_LAN interface=ether6
add bridge=bridge_vlan10 interface=vlan10
add bridge=bridge_vlan10 interface=vlan10_respaldo
add bridge=bridge_vlan10 interface=ether7
add bridge=bridge_vlan10 interface=ether8
add bridge=bridge_vlan20 interface=vlan20
add bridge=bridge_vlan20 interface=vlan20_respaldo
add bridge=bridge_vlan20 interface=ether9
add bridge=bridge_vlan20 interface=ether10
/interface list member
add interface=ether1-WAN-Master list=WAN
add interface=ether2-WAN-Backup list=WAN
add interface=ether3 list=LAN
add interface=ether4 list=LAN
add interface=ether5 list=LAN
add interface=ether6 list=LAN
add interface=ether7 list=LAN
add interface=ether8 list=LAN
add interface=ether9 list=LAN
add interface=ether10 list=LAN
add interface=ether11 list=LAN
add interface=ether12 list=LAN
/ip dhcp-client
add dhcp-options=hostname,clientid disabled=no interface=bridge_LAN
/ip firewall nat
add action=masquerade chain=srcnat
/system identity
set name=Switch-LAN1
/tool romon
set enabled=yes
~~~

[Inicio](https://franciscocadena.github.io/PI-Mikrotik/)


File: /Lista_de_Pruebas.md
[Inicio](https://franciscocadena.github.io/PI-Mikrotik/)

# Listado de Pruebas

Esto es un listado de pruebas a realizar para comprobar de que las configuraciones realizadas trabajan correctamente, estas comprobaciones se pueden ver en el documento de [Comprobaciones](./Comprobaciones.md)

## Fase 1

- Comprobar que la interfaz WAN del router que irá como cliente de dhcp, reciba ip y tenga conectividad.
- Comprobar que los equipos reciben ip dinámica para aquellos que tengan un servicio de dhcp, y ver que tengan conectividad al exterior.
- Comprobar que los equipos con ip estáticas, tienen conectividad con otros equipos y salida al exterior.
- Comprobar que las reglas de Nat y de firewall están bien configuradas haciendo pruebas de conectividad entre los equipos según como se haya configurado la red.
  - La DMZ debe tener salida al exterior y conexión con el administrador de los servidores de la LAN2, con el resto de equipos de la LAN2 y de la LAN1 no deben tener conexión. 
  - La LAN2 tendrá salida al exterior, dentro de esta habrá dos administradores uno para la DMZ donde solo este tendra conexion a ella incluso conexión por ssh, pero no tendra conexion a la LAN1, y el otro administrador de la LAN2  que se encargará de las Vlans deberá tener conexión a estas pero no a la DMZ.
  - Las Vlans no tendrán salida al exterior ni a la DMZ pero sí tendrá conexión con el administrador de LAN2 que se encarga de las Vlans.
- Comprobar que los equipos de cada vlan reciba ip dinámica y que no tengan conexión entre ellas mismas.
- Comprobar que se crea el túnel por IPsec, se establece la conexión entre los vecinos, y hay conectividad entre ellos y los equipos definidos de cada red.

## Fase 2

- Comprobar el funcionamiento de Failover, haciendo que uno de los ISP se apague y ver si salta la ruta de respaldo para que mantenga la conectividad, luego volver a encender el ISP que antes hemos apagado para comprobar que cambia de nuevo la ruta de respaldo a como estaba al principio.
- Comprobar el funcionamiento del vrrp, para ello se desconectara el router maestro, y se comprobará que en el equipo cliente sigue teniendo conexión a internet y que salta el vrrp que da al router backup, luego volvemos a encender el router maestro, y comprobamos que vuelve a cambiar la vrrp del backup al maestro.
- Comprobar que la velocidad de subida y bajada cambia según la regla aplicada, para ellos se hará dos test a un mismo equipo, uno antes de aplicar la regla, y luego otro test después de aplicar las reglas de ancho de banda.
- Comprobar el balanceo de carga para la DMZ, para ello usaremos una ubuntu desktop, abriremos dos pestañas de internet donde se estén viendo videos en ambos, se comprobará que la ip corresponde a un equipo de la DMZ, y por winbox comprobaremos si el tráfico fluye por ambos interfaces WAN , y la interfaz que da acceso a la DMZ deberá dar la suma relativa de ambos proveedores de internet.

## Fase 3

- Comprobar el funcionamiento de Port Knocking, para ello estaremos conestados al router por winbox e intentaremos entrar por ssh desde la maquina anfitriona, luego iremos entrando segun los puertos asignados para ver como se va agregando la ip de la maquina enfitriona a la Address List permitidas asta poder entrar en el router.
- Comprobar el funcionamiento del correo de mikrotik por gmail, realizando un envío del mismo y comprobar que nos ha llegado el correo.
- Comprobar que nos llegan los errores y problemas relacionados con dhcp por correo.
- Comprobar que el programa para que lleguen correos automaticamente segun el tiempo especificado funciona correctamente.
- Comprobar que Suricata funciona, creando una regla manualmente, que recoja todos los icmp, y ver si lo capta los archivos log.
- Comprobar que Suricata recibe los paquetes enviados por Mikrotik con la regla mangle, usando en mikrotik una regla que de alertas con todos los icmp.
- Comprobar el funcionamiento de Layer 7, para ello se verá si se bloquea las páginas que se definieron en el protocolo de layer 7 dentro de Firewall, pero seguimos teniendo acceso a internet a páginas que no definimos que se bloquearan.

[Inicio](https://franciscocadena.github.io/PI-Mikrotik/)



File: /Planificación_de_la_Red_de_una_empresa.md
[Inicio](https://franciscocadena.github.io/PI-Mikrotik/)

# La planificación se realizara en diferentes fases

## La primera fase sera montar una topografia de red como en la siguiente imagen.
![Fase 1 de Red](./ImagenesPI/FASE1.PNG "Topografia de Red de la Fase1")

__En la cual se configurara los siguientes aspectos__
- DHCP tanto cliente como servidor
- DNS
- Dar ip a las interfaces y nombrarlas para diferenciarlas.
- Crear redes internas.
- Crear una DMZ y uso de reglas de firewall.
- Creaciones de vlan y bridges.
- Creación de vpn entre dos router de diferentes redes con IPsec.
- Crear reglas básicas de NAT en el firewall, como enmascaramiento.

Todo este apartado estara en el documento de [configuracion de una red empresarial](./Configuración_básica_de_la_Red.md).

Configuración de Fase 1 con GNS3: [enlace](./Fase1_GNS3.md).

## La segunda fase tendrá algunos cambios en la topografía de red respecto a la anterior como se ve en la siguiente imagen.
![Fase 2 de Red](./ImagenesPI/PIFase2/Fase2.PNG "Topografia de Red de la Fase2")

__En esta parte implementaremos algunos tecnologias para que nuestra red tanga mayor disponibilidad__
- Se implementará un Failover de líneas de respaldo para ambos router con los dos ISP, para cuando uno de ellos falle, automáticamente tire por el otro.
- Se implementará un VRRP entre los dos router de la empresa para las redes estáticas de la DMZ y la LAN2 con ello ayudamos a que cuando un router se dañe sigamos teniendo conexión gracias a que tirara por el otro router, es un proceso muy parecido al failover.
- Se implementara un ancho de banda en la red LAN 2 puesto que tienen salida a internet, para ver como se configura y como funciona.
- Se implementara un balanceo de Carga para la DMZ.

Todo este apartado estara en el documento de [configuración de Herramientas que aportan Alta Disponibilidad](./Configuración_Herramientas_Alta_Disponibilida.md).

Configuración de Fase 2 con GNS3: [enlace](./Fase2_GNS3.md).

## La tercera fase principalmente consistirá en montar un IDS
![Fase 3 de Red](./ImagenesPI/PIFase3/FASE3.PNG "Topografia de Red de la Fase3")

__En esta fase se implementara lo siguiente__
- Se implementa el Port knocking en ambos routers, para darle una capa de seguridad frente a quienes quieran conectar remotamente al router, usando un código de puertos.
- Se configuraran ambos router para que nos envíen correo cuando se detecte errores o cualquier anomalía que nosotros queramos que se nos sea avisado, también se configurara el correo para que en una determinada hora de cada día nos mande un backup de la configuración de los router.
- Se configurara Mikrotik para que le envié todos los paquetes que atraviesen el router a un equipo con Suricata instalado como IDS.
- Se monta un sistema Kali, para simular que alguien a entrado a nuestro router y realiza un escaneo de red con nmap, para comprobar si Suricata lo detecta.
- Se configura el protocolo de Layer 7 para filtrar varias paginas y no tener acceso a estas.

Todo esto estara en los archivos de [Suricata-Mikrotik](./Suricata_Mikrotik.md) y en el de [configuración de Herramientas de Seguridad](./Configuración_Herramientas_Seguridad.md).

Configuración de Fase 3 con GNS3: [enlace](./Fase3_GNS3.md).

[Inicio](https://franciscocadena.github.io/PI-Mikrotik/)



File: /README.md
# PI-Mikrotik

Proyecto Integrado ASIR Mikrotik

## Introducción
Este proyecto se basa en Mikrotik, una empresa Europea que trabaja en temas de telecomunicaciones y redes, también aporta soluciones a la hora de crear una red ofreciendo sus propios productos con diversidad de router y switches tanto de gama baja como de gama alta, pudiendo adaptarse a las medidas económicas de cada empresa, y si eso no es suficiente también tiene un sistema operativo propio para que pueda implementarse en un pc.

En el proyecto se dará a conocer el sistema operativo que usa Mikrotik para configurar sus router llamado RouterOS y una herramienta que se usa habitualmente para configurar el router de manera gráfica llamado Winbox. 

Todo este proceso se realizará de manera práctica donde desarrollaremos una topografía de red que podría usar una empresa de manera virtual, en la cual enseñaremos a configurar métodos básicos para la creación de una red y profundizando más en temas de Seguridad y Alta disponibilidad.

__La estructura del documento es la siguiente__
- [Recursos](./Recursos.md) (donde se comenta las herramientas usadas para poder desarrollar el proyecto)
- [Planificación de la Red de una empresa](./Planificación_de_la_Red_de_una_empresa.md) (donde se irá mostrando las diferentes fases de topografías de red con imágenes y se comenta que herramientas se implementaran en cada una de ellas, para posteriormente ser virtualizadas con  gns3)
- Fase 1: [Configuración básica de la Red](./Configuración_básica_de_la_Red.md) (donde se explicara los pasos de configuración básica para montar una red )
- [Fase 1 con gns3](./Fase1_GNS3.md) (donde se verá la configuración realizada con gns3 de la fase 1)
- Fase 2: [Configuración de Herramientas que aportan Alta Disponibilidad](./Configuración_Herramientas_Alta_Disponibilida.md) (donde se explicará la configuración de algunas herramientas para darle una mejor disponibilidad a nuestra red)
- [Fase 2 con gns3](./Fase2_GNS3.md) (donde se verá la configuración realizada con gns3 de la fase 2)
- Fase 3: [Configuración de Herramientas para dar Seguridad](./Configuración_Herramientas_Seguridad.md) (donde se explicara la configuración de la herramienta Port knocking, el filtrado de páginas web con el protocolo layer 7 y el envio por correos de backup y archivos log)
- Fase 3: [Uso de Suricata como IDS junto a Mikrotik](./Suricata_Mikrotik.md) (donde se vera la Instalación de Suricata y los metodos de configuración para que Mikrotik le envie los paquetes a Suricata y trabaje como IDS)
- [Fase 3 con gns3](./Fase3_GNS3.md) (en donde se verá la imagen de la topografía final virtualizada con gns3 y los script de la configuración de cada router).
- [Lista de pruebas](./Lista_de_Pruebas.md) (listado de pruebas que se realizarán para comprobar que todo funciona correctamente) 
- [Comprobaciones](./Comprobaciones.md) (comprobaciones, basándonos en la lista de pruebas para confirmar el funcionamiento de nuestra configuración)
- [Definiciones](./Definiciones.md) (en donde se explicara algunas de las herrameintas usadas, protocolos, y otros conceptos).




File: /Recursos.md
# Recursos necesarios para el laboratorio
- Maquina Anfitriona 
- Herramienta Winbox instalada en la máquina anfitriona para configurar de manera gráfica el router
- VirtualBox como Sistema de Virtualización
- Network Notepad para diseñar planos de Red
- GNS3 para diseñar y configurar la red
- Uso de OVA Cloud Host Router para que actúen los PC como enrutadores de manera virtual
- ISO u Ovas de Ubuntu Desktop u otro S.O ligero para que trabajen como Clientes
- ISO u Ova de Kali Linux para usarlo como atacante a la red

[Inicio](https://franciscocadena.github.io/PI-Mikrotik/)


File: /Suricata_Mikrotik.md
[Inicio](https://franciscocadena.github.io/PI-Mikrotik/)

# Suricata como IDS junto a Mikrotik

La instalación de Suricata se realiza en un Ubuntu 18.04 Desktop, estando actualizado.

## Instalación de Suricata desde repositorio

Suricata ya viene por defecto en los repositorios de Ubuntu pero es posible que sea una versión antigua, por ello para asegurarnos de que se instala la última versión añadiremos el siguiente __PPA(Personal Package Archive) al repositorio__ con el siguiente comando.
~~~
sudo add-apt-repository ppa:oisf/suricata-stable
~~~

![Cargando repositorio suricata](./ImagenesPI/Suricata/repositorio.PNG "Cargando repositorio suricata")

![Pulsamos Intro para aceptar](./ImagenesPI/Suricata/repositorio2.PNG "Pulsamos Intro para aceptar")

Acto seguido actualizamos nuestro equipo con.
~~~
sudo apt update
~~~

![Actualización para que cargue los datos de nuevo repositorio](./ImagenesPI/Suricata/update.PNG "Actualización para que cargue los datos de nuevo repositorio")

Y pasamos a instalarlo con.
~~~
sudo apt install suricata jq
~~~

![Instalando suricata y la herramienta jq](./ImagenesPI/Suricata/instalar.PNG "Instalando suricata y la herramienta jq")

Con el comando anterior instalamos tanto suricata como la herramienta _jq_ la cual nos servirá para trabajar con las salidas que nos aporta el archivo __EVE.json__ del _log_.
 
Una vez instalado suricata podemos confirmarlo usando el siguiente comando para ver en qué estado se encuentra.
~~~
sudo systemctl status suricata
~~~

![Comprobar estado de Suricata](./ImagenesPI/Suricata/status.PNG "Comprobar estado de Suricata")

Y tambien podemos usar el siguiente comando que nos dara informacion de todo lo instalado, tanto herramientas, como librerías, directorios de instalación, etc.
~~~
sudo suricata --build-info
~~~ 

![Información de la instalación](./ImagenesPI/Suricata/build.PNG "Información de la instalación")

Lo siguiente que haremos será comprobar cuál es nuestra red y nuestra interfaz, para ello podemos usar el comando __ip a__ o cualquier otro que deseemos que nos de la información que deseamos.

![Recoger datos de la ip e interfaz](./ImagenesPI/Suricata/ip.PNG "Recoger datos de la ip e interfaz")

Una vez que conocemos estos datos iremos al archivo de configuración de suricata, que se encuentra en __/etc/suricata/suricata.yaml__, una vez dentro buscamos el _HOME_NET_ y especificamos la red que tenemos, por ejemplo si tenemos la siguiente ip 192.168.0.10, definiremos en el Home_Net que nuestra red se encuentra en 192.168.0.0/24 o podemos directamente definir la ip de nuestra interfaz siempre que esta sea fija.

![Archivo suricata.yaml](./ImagenesPI/Suricata/suricatayaml.PNG "Archivo suricata.yaml")

~~~
af-packet:
- interface: enp0s3
   cluster-id: 99
   cluster-type: cluster_flow
   defrag: yes
   use-mmap: yes
   tpacket-v3: yes
~~~

Seguidamente buscaremos en el documento todos los interfaces _eth0_ y los sustituiremos por el nuestro, una vez terminado guardamos, y pasaremos al siguiente fichero de texto __/etc/default/suricata__ donde buscaremos todos los _eth0_ y los sustituiremos por nuestra interfaz, al terminar guardamos y salimos.

![Archivo suricata dentro del directorio default](./ImagenesPI/Suricata/default.PNG "Archivo suricata dentro del directorio default")

Nuestro siguiente paso será instalar la herramienta __Suricata-update__ la cual es muy importante en suricata debido a que nos proporciona las _reglas_ para las _alertas_ que usará suricata, estas vienen firmadas de diversas fuentes, de esta manera las podemos descargar y tener siempre actualizadas.
Para ello tan solo debemos ejecutar el siguiente comando.
~~~
sudo suricata-update
~~~

![Instalar suricata-update y actualizar reglas](./ImagenesPI/Suricata/suricata-update.PNG "Instalar suricata-update y actualizar reglas")

Este comando funciona con versiones de suricata del 4.1 en adelante si son más antiguas habrá que instalarlo con los siguientes comandos:
~~~
apt install python-pip
pip install pyyaml
pip install https://github.com/OISF/suricata-update/archive/master.zip
pip install --pre --upgrade suricata-update
~~~
Todas las reglas se instalarán en la ruta por defecto __/var/lib/suricata/rules__, dentro del archivo __suricata.rules__.
 
Ahora reiniciamos suricata con.
~~~
sudo systemctl restart suricata
~~~ 

Luego nos aseguramos de que suricata está corriendo comprobando su fichero de _log_, usando el comando. 
~~~
File: /_config.yml
theme: jekyll-theme-leap-day
plugins:
  - jekyll-relative-links
relative_links:
  enabled: true
  collections: true
include:
  - Fase1_GNS3.md
  - Fase2_GNS3.md
  - Fase3_GNS3.md
  - Lista_de_Pruebas.md
  - README.md
  - Recursos.md
  - Suricata_Mikrotik.md
  - Comprobaciones.md
  - Definiciones.md
  - Planificación_de_la_Red_de_una_empresa.md
  - Configuración_Herramientas_Alta_Disponibilida.md
  - Configuración_básica_de_la_Red.md
  - Configuración_Herramientas_Seguridad.md
  - ImagenesPI
  - imagenesGNS3


