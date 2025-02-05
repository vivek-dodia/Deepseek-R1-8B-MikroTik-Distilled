# Repository Information
Name: ioBroker.mikrotik

# Directory Structure
Directory structure:
└── github_repos/ioBroker.mikrotik/
    ├── .eslintignore
    ├── .eslintrc.json
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
    │   │       ├── pack-6cc80069e8ea2cfc03d46307f18871c34a355634.idx
    │   │       └── pack-6cc80069e8ea2cfc03d46307f18871c34a355634.pack
    │   ├── packed-refs
    │   └── refs/
    │       ├── heads/
    │       │   └── master
    │       ├── remotes/
    │       │   └── origin/
    │       │       └── HEAD
    │       └── tags/
    ├── .gitattributes
    ├── .github/
    │   ├── auto-merge.yml
    │   ├── dependabot.yml
    │   ├── ISSUE_TEMPLATE/
    │   │   └── bug_report.md
    │   └── workflows/
    │       ├── dependabot-auto-merge.yml
    │       └── test-and-release.yml
    ├── .gitignore
    ├── .mocharc.json
    ├── .prettierignore
    ├── .prettierrc.js
    ├── .releaseconfig.json
    ├── admin/
    │   ├── i18n/
    │   │   ├── de/
    │   │   │   └── translations.json
    │   │   ├── en/
    │   │   │   └── translations.json
    │   │   ├── es/
    │   │   │   └── translations.json
    │   │   ├── fr/
    │   │   │   └── translations.json
    │   │   ├── it/
    │   │   │   └── translations.json
    │   │   ├── nl/
    │   │   │   └── translations.json
    │   │   ├── pl/
    │   │   │   └── translations.json
    │   │   ├── pt/
    │   │   │   └── translations.json
    │   │   ├── ru/
    │   │   │   └── translations.json
    │   │   ├── uk/
    │   │   │   └── translations.json
    │   │   └── zh-cn/
    │   │       └── translations.json
    │   ├── index_m.html
    │   └── words.js
    ├── docs/
    │   ├── de/
    │   │   ├── img/
    │   │   └── template.md
    │   ├── en/
    │   │   ├── img/
    │   │   └── template.md
    │   └── ru/
    │       ├── img/
    │       └── template.md
    ├── io-package.json
    ├── lib/
    │   ├── adapter-config.d.ts
    │   └── tools.js
    ├── LICENSE
    ├── main.js
    ├── main.test.js
    ├── package-lock.json
    ├── package.json
    ├── README.md
    ├── test/
    │   ├── integration.js
    │   ├── mocha.setup.js
    │   ├── mocharc.custom.json
    │   ├── package.js
    │   └── tsconfig.json
    └── tsconfig.json


# Content
File: /.eslintignore
**/.eslintrc.js
admin/words.js


File: /.eslintrc.json
{
    "root": true,
    "env": {
        "es6": true,
        "node": true,
        "mocha": true
    },
    "extends": ["eslint:recommended"],
    "plugins": [],
    "rules": {
        "indent": [
            "error",
            4,
            {
                "SwitchCase": 1
            }
        ],
        "no-console": "off",
        "no-unused-vars": [
            "error",
            {
                "ignoreRestSiblings": true,
                "argsIgnorePattern": "^_"
            }
        ],
        "no-var": "error",
        "no-trailing-spaces": "error",
        "prefer-const": "error",
        "quotes": [
            "error",
            "single",
            {
                "avoidEscape": true,
                "allowTemplateLiterals": true
            }
        ],
        "semi": ["error", "always"]
    },
    "parserOptions": {
        "ecmaVersion": 2020
    }
}


File: /.git\config
[core]
	repositoryformatversion = 0
	filemode = false
	bare = false
	logallrefupdates = true
	symlinks = false
	ignorecase = true
[remote "origin"]
	url = https://github.com/iobroker-community-adapters/ioBroker.mikrotik.git
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
0000000000000000000000000000000000000000 c15ac66b407fb69a5507561bbf899837bad6bd87 vivek-dodia <vivek.dodia@icloud.com> 1738606346 -0500	clone: from https://github.com/iobroker-community-adapters/ioBroker.mikrotik.git


File: /.git\logs\refs\heads\master
0000000000000000000000000000000000000000 c15ac66b407fb69a5507561bbf899837bad6bd87 vivek-dodia <vivek.dodia@icloud.com> 1738606346 -0500	clone: from https://github.com/iobroker-community-adapters/ioBroker.mikrotik.git


File: /.git\logs\refs\remotes\origin\HEAD
0000000000000000000000000000000000000000 c15ac66b407fb69a5507561bbf899837bad6bd87 vivek-dodia <vivek.dodia@icloud.com> 1738606346 -0500	clone: from https://github.com/iobroker-community-adapters/ioBroker.mikrotik.git


File: /.git\packed-refs
# pack-refs with: peeled fully-peeled sorted 
0284475d20b4754c9b6a47295bcd0d86ec918093 refs/remotes/origin/dependabot/npm_and_yarn/eslint-9.19.0
181764d702530951bfd9a3c3a2151fecae493d4e refs/remotes/origin/dependabot/npm_and_yarn/eslint-config-prettier-10.0.1
0f023ffca79577dbcd4c59ccf9981d5c1a8e61de refs/remotes/origin/dependabot/npm_and_yarn/iobroker/adapter-core-3.2.3
f6601d43cf94b3be86a5e02ceed713eb9073dd3f refs/remotes/origin/dependabot/npm_and_yarn/iobroker/testing-5.0.3
18d25e1ed01fb09a0b15fff946679bbb2198cfc0 refs/remotes/origin/dependabot/npm_and_yarn/mocha-11.1.0
75389f81007d6b9705764d8f8248e2af45f4f45b refs/remotes/origin/dependabot/npm_and_yarn/multi-a7b1dbc0cd
5cb609ceb31bd4da1ecd35382f2deff8e4d19323 refs/remotes/origin/dependabot/npm_and_yarn/multi-adb500430a
0f1e7668841be4a992eda4f2f6262f09b16b1819 refs/remotes/origin/dependabot/npm_and_yarn/multi-bd7f08ee8b
99c94e29ef74533b6c3fa23e5deb7e62c3bcd554 refs/remotes/origin/dependabot/npm_and_yarn/multi-be117bf1f7
46bd8f5206b099641cbc9b83496813b630fba4a2 refs/remotes/origin/dependabot/npm_and_yarn/sinon-19.0.2
493e57d1887a1f448ec00cfc15b0296e234037dc refs/remotes/origin/dependabot/npm_and_yarn/types/node-22.13.0
c15ac66b407fb69a5507561bbf899837bad6bd87 refs/remotes/origin/master
e87a815f8e1523ac3f6c7f1062272cccf08c440b refs/tags/v1.1.0
^a5b1c279fc815b2d4b914b18c1f4c053791e69a6
9167e69504680ee1089af317ce79cef2bbd0bd60 refs/tags/v1.1.1
^a4785ea969a7403835334cc1b491670b2d35a605
b31c3bdf956dffe991fa6547f3873053b44d3fcd refs/tags/v1.2.0
^3f35f7dd915509c49184f628894e67c9fe04e80d
3a7095dbb65d8f943533f6db5c26b6d3e833751f refs/tags/v1.2.1
^06277bcf5c4605624f683b70872cf2d37ea49a08


File: /.git\refs\heads\master
c15ac66b407fb69a5507561bbf899837bad6bd87


File: /.git\refs\remotes\origin\HEAD
ref: refs/remotes/origin/master


File: /.gitattributes
# Auto detect text files and perform LF normalization
* text=auto

# Custom for Visual Studio
*.cs     diff=csharp

# Standard to msysgit
*.doc	 diff=astextplain
*.DOC	 diff=astextplain
*.docx diff=astextplain
*.DOCX diff=astextplain
*.dot  diff=astextplain
*.DOT  diff=astextplain
*.pdf  diff=astextplain
*.PDF	 diff=astextplain
*.rtf	 diff=astextplain
*.RTF	 diff=astextplain


File: /.github\auto-merge.yml
# Configure here which dependency updates should be merged automatically.
# The recommended configuration is the following:
- match:
    # Only merge patches for production dependencies
    dependency_type: production
    update_type: "semver:patch"
- match:
    # Except for security fixes, here we allow minor patches
    dependency_type: production
    update_type: "security:minor"
- match:
    # and development dependencies can have a minor update, too
    dependency_type: development
    update_type: "semver:minor"

# The syntax is based on the legacy dependabot v1 automerged_updates syntax, see:
# https://dependabot.com/docs/config-file/#automerged_updates


File: /.github\dependabot.yml
version: 2
updates:
  - package-ecosystem: npm
    directory: "/"
    schedule:
      interval: monthly
      time: "04:00"
      timezone: Europe/Berlin
    open-pull-requests-limit: 15
    versioning-strategy: increase

  - package-ecosystem: github-actions
    directory: "/"
    schedule:
      interval: monthly
      time: "04:00"
      timezone: Europe/Berlin
    open-pull-requests-limit: 15


File: /.github\ISSUE_TEMPLATE\bug_report.md
---
name: Bug report
about: Something is not working as it should
title: ''
labels: ''
assignees: ''
---

**Describe the bug**  
A clear and concise description of what the bug is.

**To Reproduce**  
Steps to reproduce the behavior:
1. Go to '...'
2. Click on '...'
3. Scroll down to '....'
4. See error

**Expected behavior**  
A clear and concise description of what you expected to happen.

**Screenshots & Logfiles**  
If applicable, add screenshots and logfiles to help explain your problem.

**Versions:**  
 - Adapter version: <adapter-version>
 - JS-Controller version: <js-controller-version> <!-- determine this with `iobroker -v` on the console -->
 - Node version: <node-version> <!-- determine this with `node -v` on the console -->
 - Operating system: <os-name>

**Additional context**  
Add any other context about the problem here.


File: /.github\workflows\dependabot-auto-merge.yml
# Automatically merge Dependabot PRs when version comparison is within the range
# that is configured in .github/auto-merge.yml

name: Auto-Merge Dependabot PRs

on:
  # WARNING: This needs to be run in the PR base, DO NOT build untrusted code in this action
  # details under https://github.blog/changelog/2021-02-19-github-actions-workflows-triggered-by-dependabot-prs-will-run-with-read-only-permissions/
  pull_request_target:

jobs:
  auto-merge:
    if: github.actor == 'dependabot[bot]'
    runs-on: ubuntu-latest
    steps:
      - name: Checkout code
        uses: actions/checkout@v4

      - name: Check if PR should be auto-merged
        uses: ahmadnassri/action-dependabot-auto-merge@v2
        with:
          # In order to use this, you need to go to https://github.com/settings/tokens and
          # create a Personal Access Token with the permission "public_repo".
          # Enter this token in your repository settings under "Secrets" and name it AUTO_MERGE_TOKEN
          github-token: ${{ secrets.AUTO_MERGE_TOKEN }}
          # By default, squash and merge, so Github chooses nice commit messages
          command: squash and merge


File: /.github\workflows\test-and-release.yml
name: Test and Release

# Run this job on all pushes and pull requests
# as well as tags with a semantic version
on:
  push:
    branches:
      - "master"
    tags:
      # normal versions
      - "v[0-9]+.[0-9]+.[0-9]+"
      # pre-releases
      - "v[0-9]+.[0-9]+.[0-9]+-**"
  pull_request: {}

# Cancel previous PR/branch runs when a new commit is pushed
concurrency:
  group: ${{ github.ref }}
  cancel-in-progress: true

jobs:
  # Performs quick checks before the expensive test runs
  check-and-lint:
    if: contains(github.event.head_commit.message, '[skip ci]') == false

    runs-on: ubuntu-latest

    steps:
      - uses: ioBroker/testing-action-check@v1
        with:
          node-version: '20.x'
          # Uncomment the following line if your adapter cannot be installed using 'npm ci'
          # install-command: 'npm install'
          lint: true

  # Runs adapter tests on all supported node versions and OSes
  adapter-tests:
    if: contains(github.event.head_commit.message, '[skip ci]') == false

    runs-on: ${{ matrix.os }}
    strategy:
      matrix:
        node-version: [18.x, 20.x, 22.x]
        os: [ubuntu-latest, windows-latest, macos-latest]

    steps:
      - uses: ioBroker/testing-action-adapter@v1
        with:
          node-version: ${{ matrix.node-version }}
          os: ${{ matrix.os }}
          # Uncomment the following line if your adapter cannot be installed using 'npm ci'
          # install-command: 'npm install'

# TODO: To enable automatic npm releases, create a token on npmjs.org 
# Enter this token as a GitHub secret (with name NPM_TOKEN) in the repository options
# Then uncomment the following block:

  # Deploys the final package to NPM
  deploy:
    needs: [check-and-lint, adapter-tests]

    # Trigger this step only when a commit on any branch is tagged with a version number
    if: |
      contains(github.event.head_commit.message, '[skip ci]') == false &&
      github.event_name == 'push' &&
      startsWith(github.ref, 'refs/tags/v')

    runs-on: ubuntu-latest

    # Write permissions are required to create Github releases
    permissions:
      contents: write

    steps:
      - uses: ioBroker/testing-action-deploy@v1
        with:
          node-version: '20.x'
          # Uncomment the following line if your adapter cannot be installed using 'npm ci'
          # install-command: 'npm install'
          npm-token: ${{ secrets.NPM_TOKEN }}
          github-token: ${{ secrets.GITHUB_TOKEN }}

          # When using Sentry for error reporting, Sentry can be informed about new releases
          # To enable create a API-Token in Sentry (User settings, API keys)
          # Enter this token as a GitHub secret (with name SENTRY_AUTH_TOKEN) in the repository options
          # Then uncomment and customize the following block:
#          sentry: true
#          sentry-token: ${{ secrets.SENTRY_AUTH_TOKEN }}
#          sentry-project: "iobroker-pid"
#          sentry-version-prefix: "iobroker.pid"
#          # If your sentry project is linked to a GitHub repository, you can enable the following option
#          # sentry-github-integration: true


File: /.gitignore
*.class
tasks/
devfile/
.idea
.git
File: /.mocharc.json
{
    "require": [
        "./test/mocha.setup.js"
    ],
    "watch-files": [
        "!(node_modules|test)/**/*.test.js",
        "*.test.js",
        "test/**/test!(PackageFiles|Startup).js"
    ]
}

File: /.prettierignore
package.json
package-lock.json

File: /.prettierrc.js
module.exports = {
    semi: true,
    trailingComma: 'all',
    singleQuote: true,
    printWidth: 120,
    useTabs: false,
    tabWidth: 4,
    endOfLine: 'lf',
};


File: /.releaseconfig.json
{
    "plugins": ["iobroker", "license", "manual-review"]
}


File: /admin\i18n\de\translations.json
{
    "MikroTik adapter settings": "MikroTik-Adaptereinstellungen",
    "ch2": "Firewall/nat",
    "ch3": "DHCP-Server/Lease",
    "ch4": "Schnittstelle",
    "ch5": "Firewall/Filter",
    "ch6": "WLAN/Anmeldetabelle",
    "ch7": "Adresse",
    "ch8": "Firewall/Adressliste",
    "ch9": "caps-man/registration-table",
    "def": "Standard (8728)",
    "following": "Erhalten Sie folgende Daten:",
    "host": "IP Adresse",
    "login": "Anmeldung",
    "ms": "Millisekunden",
    "on save adapter restarts with new config immediately": "Beim Speichern wird der Adapter sofort mit der neuen Konfiguration neu gestartet",
    "password": "Passwort",
    "poll": "Datenaktualisierungsintervall",
    "port": "Hafen",
    "sec": "Sekunden",
    "timeout": "Auszeit"
}


File: /admin\i18n\en\translations.json
{
    "MikroTik adapter settings": "MikroTik adapter settings",
    "ch2": "firewall/nat",
    "ch3": "dhcp-server/lease",
    "ch4": "interface",
    "ch5": "firewall/filter",
    "ch6": "wireless/registration-table",
    "ch7": "address",
    "ch8": "firewall/address-list",
    "ch9": "caps-man/registration-table",
    "def": "default (8728)",
    "following": "Receive the following data:",
    "host": "IP Address",
    "login": "login",
    "ms": "milliseconds",
    "on save adapter restarts with new config immediately": "on save adapter restarts with new config immediately",
    "password": "password",
    "poll": "Data refresh interval",
    "port": "port",
    "sec": "seconds",
    "timeout": "timeout"
}


File: /admin\i18n\es\translations.json
{
    "MikroTik adapter settings": "Configuración del adaptador MikroTik",
    "ch2": "cortafuegos/nat",
    "ch3": "servidor dhcp/arrendamiento",
    "ch4": "interfaz",
    "ch5": "cortafuegos/filtro",
    "ch6": "mesa-de-registro/inalámbrica",
    "ch7": "DIRECCIÓN",
    "ch8": "firewall/lista de direcciones",
    "ch9": "caps-man/tabla-de-registro",
    "def": "predeterminado (8728)",
    "following": "Reciba los siguientes datos:",
    "host": "Dirección IP",
    "login": "acceso",
    "ms": "milisegundos",
    "on save adapter restarts with new config immediately": "Al guardar, el adaptador se reinicia con una nueva configuración inmediatamente.",
    "password": "contraseña",
    "poll": "Intervalo de actualización de datos",
    "port": "puerto",
    "sec": "segundos",
    "timeout": "se acabó el tiempo"
}


File: /admin\i18n\fr\translations.json
{
    "MikroTik adapter settings": "Paramètres de l'adaptateur MikroTik",
    "ch2": "pare-feu/nat",
    "ch3": "serveur DHCP/location",
    "ch4": "interface",
    "ch5": "pare-feu/filtre",
    "ch6": "table d'enregistrement/sans fil",
    "ch7": "adresse",
    "ch8": "pare-feu/liste d'adresses",
    "ch9": "casquettes-homme/table-d'inscription",
    "def": "par défaut (8728)",
    "following": "Recevez les données suivantes :",
    "host": "Adresse IP",
    "login": "se connecter",
    "ms": "millisecondes",
    "on save adapter restarts with new config immediately": "lors de la sauvegarde, l'adaptateur redémarre immédiatement avec une nouvelle configuration",
    "password": "mot de passe",
    "poll": "Intervalle d'actualisation des données",
    "port": "port",
    "sec": "secondes",
    "timeout": "temps mort"
}


File: /admin\i18n\it\translations.json
{
    "MikroTik adapter settings": "Impostazioni dell'adattatore MikroTik",
    "ch2": "firewall/nat",
    "ch3": "server DHCP/leasing",
    "ch4": "interfaccia",
    "ch5": "firewall/filtro",
    "ch6": "wireless/tabella di registrazione",
    "ch7": "indirizzo",
    "ch8": "firewall/elenco indirizzi",
    "ch9": "caps-man/tabella-registrazione",
    "def": "predefinito (8728)",
    "following": "Ricevi i seguenti dati:",
    "host": "Indirizzo IP",
    "login": "login",
    "ms": "millisecondi",
    "on save adapter restarts with new config immediately": "al salvataggio l'adattatore si riavvia immediatamente con la nuova configurazione",
    "password": "parola d'ordine",
    "poll": "Intervallo di aggiornamento dei dati",
    "port": "porta",
    "sec": "secondi",
    "timeout": "tempo scaduto"
}


File: /admin\i18n\nl\translations.json
{
    "MikroTik adapter settings": "MikroTik-adapterinstellingen",
    "ch2": "firewall/nat",
    "ch3": "dhcp-server/lease",
    "ch4": "koppel",
    "ch5": "firewall/filter",
    "ch6": "draadloos/registratietafel",
    "ch7": "adres",
    "ch8": "firewall/adreslijst",
    "ch9": "caps-man/inschrijvingstabel",
    "def": "standaard (8728)",
    "following": "Ontvang de volgende gegevens:",
    "host": "IP adres",
    "login": "Log in",
    "ms": "milliseconden",
    "on save adapter restarts with new config immediately": "bij het opslaan wordt de adapter onmiddellijk opnieuw opgestart met nieuwe configuratie",
    "password": "wachtwoord",
    "poll": "Interval voor gegevensvernieuwing",
    "port": "haven",
    "sec": "seconden",
    "timeout": "time-out"
}


File: /admin\i18n\pl\translations.json
{
    "MikroTik adapter settings": "Ustawienia adaptera MikroTik",
    "ch2": "zapora sieciowa/nat",
    "ch3": "serwer DHCP/dzierżawa",
    "ch4": "interfejs",
    "ch5": "zapora/filtr",
    "ch6": "tabela bezprzewodowa/rejestracyjna",
    "ch7": "adres",
    "ch8": "zapora ogniowa/lista adresów",
    "ch9": "caps-man/tabela-rejestracyjna",
    "def": "domyślny (8728)",
    "following": "Otrzymaj następujące dane:",
    "host": "Adres IP",
    "login": "Zaloguj sie",
    "ms": "milisekundy",
    "on save adapter restarts with new config immediately": "po zapisaniu adapter natychmiast uruchamia się ponownie z nową konfiguracją",
    "password": "hasło",
    "poll": "Interwał odświeżania danych",
    "port": "Port",
    "sec": "sekundy",
    "timeout": "koniec czasu"
}


File: /admin\i18n\pt\translations.json
{
    "MikroTik adapter settings": "Configurações do adaptador MikroTik",
    "ch2": "firewall/nat",
    "ch3": "servidor dhcp/aluguel",
    "ch4": "interface",
    "ch5": "firewall/filtro",
    "ch6": "sem fio/mesa de registro",
    "ch7": "endereço",
    "ch8": "firewall/lista de endereços",
    "ch9": "caps-man/tabela de registro",
    "def": "padrão (8728)",
    "following": "Receba os seguintes dados:",
    "host": "Endereço de IP",
    "login": "Conecte-se",
    "ms": "milissegundos",
    "on save adapter restarts with new config immediately": "ao salvar o adaptador reinicia com a nova configuração imediatamente",
    "password": "senha",
    "poll": "Intervalo de atualização de dados",
    "port": "porta",
    "sec": "segundos",
    "timeout": "tempo esgotado"
}


File: /admin\i18n\ru\translations.json
{
    "MikroTik adapter settings": "Настройки адаптера МикроТик",
    "ch2": "брандмауэр/нат",
    "ch3": "DHCP-сервер/аренда",
    "ch4": "интерфейс",
    "ch5": "брандмауэр/фильтр",
    "ch6": "беспроводной/регистрационный стол",
    "ch7": "адрес",
    "ch8": "брандмауэр/список адресов",
    "ch9": "шапки-человек/таблица-регистрации",
    "def": "по умолчанию (8728)",
    "following": "Получите следующие данные:",
    "host": "Айпи адрес",
    "login": "авторизоваться",
    "ms": "миллисекунды",
    "on save adapter restarts with new config immediately": "при сохранении адаптер немедленно перезагружается с новой конфигурацией",
    "password": "пароль",
    "poll": "Интервал обновления данных",
    "port": "порт",
    "sec": "секунды",
    "timeout": "тайм-аут"
}


File: /admin\i18n\uk\translations.json
{
    "MikroTik adapter settings": "Налаштування адаптера MikroTik",
    "ch2": "брандмауер/фіз",
    "ch3": "dhcp-сервер/оренда",
    "ch4": "інтерфейс",
    "ch5": "брандмауер/фільтр",
    "ch6": "бездротовий/реєстраційний стіл",
    "ch7": "адресу",
    "ch8": "брандмауер/список адрес",
    "ch9": "caps-man/registration-table",
    "def": "за замовчуванням (8728)",
    "following": "Отримайте такі дані:",
    "host": "IP-адреса",
    "login": "логін",
    "ms": "мілісекунд",
    "on save adapter restarts with new config immediately": "під час збереження адаптер негайно перезавантажується з новою конфігурацією",
    "password": "пароль",
    "poll": "Інтервал оновлення даних",
    "port": "порт",
    "sec": "секунд",
    "timeout": "час вийшов"
}


File: /admin\i18n\zh-cn\translations.json
{
    "MikroTik adapter settings": "MikroTik 适配器设置",
    "ch2": "防火墙/NAT",
    "ch3": "dhcp 服务器/租用",
    "ch4": "界面",
    "ch5": "防火墙/过滤器",
    "ch6": "无线/注册表",
    "ch7": "地址",
    "ch8": "防火墙/地址列表",
    "ch9": "帽人/登记表",
    "def": "默认（8728）",
    "following": "接收以下数据：",
    "host": "IP地址",
    "login": "登录",
    "ms": "毫秒",
    "on save adapter restarts with new config immediately": "保存适配器后立即使用新配置重新启动",
    "password": "密码",
    "poll": "数据刷新间隔",
    "port": "港口",
    "sec": "秒",
    "timeout": "暂停"
}


File: /admin\index_m.html
<html>
<head>
    <link rel="stylesheet" type="text/css" href="../../lib/css/materialize.css">
    <link rel="stylesheet" type="text/css" href="../../css/adapter.css"/>
    <script type="text/javascript" src="../../lib/js/jquery-3.2.1.min.js"></script>
    <script type="text/javascript" src="../../socket.io/socket.io.js"></script>
    <script type="text/javascript" src="../../js/translate.js"></script>
    <script type="text/javascript" src="../../lib/js/materialize.js"></script>
    <script type="text/javascript" src="../../js/adapter-settings.js"></script>
    <script type="text/javascript" src="words.js"></script>
    <style>
        .m .col .select-wrapper + label {
            top: -26px;
        }

        .m span {
            font-size: 0.9em;
        }

        .m .logo {
            padding: .5rem;
            width: 150px;
        }
    </style>
    <script type="text/javascript">
        function load(settings, onChange){
            if (!settings) return;
            $('.value').each(function (){
                var $key = $(this);
                var id = $key.attr('id');
                if ($key.attr('type') === 'checkbox'){
                    $key.prop('checked', settings[id]).change(function (){
                        onChange();
                    });
                } else {
                    $key.val(settings[id]).change(function (){
                        onChange();
                    }).keyup(function (){
                        onChange();
                    });
                }
            });
            onChange(false);
            M.updateTextFields();
        }

        function save(callback){
            var obj = {};
            $('.value').each(function (){
                var $this = $(this);
                if ($this.attr('type') === 'checkbox'){
                    obj[$this.attr('id')] = $this.prop('checked');
                } else {
                    obj[$this.attr('id')] = $this.val();
                }
            });
            callback(obj);
        }
    </script>
    <script>
        $(function (){
            $(".adapter-body").append("" +
                "<div class=\"m row\" style='display:block;position:absolute;bottom:130px;right:0;'>" +
                "<div class=\"col right\">" +
                "<div class=\"col\" style=\"margin-top:10px;float:right;margin-right:20px;\">" +
                "<a target=\"_blank\" href=\"https://sobe.ru/na/instalator\"><img style=\"float:right;\" src=\"https://img.shields.io/badge/Donate-YooMoney-green\" alt=\"\"></a>" +
                "<a target=\"_blank\" href=\"https://www.paypal.com/cgi-bin/webscr?cmd=_s-xclick&hosted_button_id=PFUALWTR2CTPY\"><img style=\"float:right;padding-right:10px;\" src=\"https://img.shields.io/badge/Donate-PayPal-green.svg\" alt=\"\"></a>" +
                "</div></div></div>");
        });
    </script>
    <style>
        .adapter-body {
            display: block;
        }

        .m .input-field > label {
            color: #5a5a5a;
        }

        .adapter-body::after {
            top: 0;
            left: 0;
            bottom: 0;
            right: 0;
            content: "";
            background: url(background.jpg);
            background-position: top;
            background-repeat: no-repeat;
            background-size: cover;
            opacity: 0.1;
            position: absolute;
            z-index: -1;
        }
    </style>
</head>

<body>
<div class="m adapter-container">
    <div class="row">
        <div class="row">
            <div class="input-field col s6">
                <img src="mikrotik_admin.png" class="logo">
            </div>
        </div>
        <div class="row">
            <div class="input-field col s12 m6 l4">
                <input class="value" id="host" type="text">
                <label for="host" class="translate">host</label>
            </div>
            <div class="input-field col s12 m6 l4">
                <input type="number" class="value" id="port"/>
                <label for="port" class="translate">port</label>
                <span class="translate">def</span>
            </div>
            <div class="input-field col s12 m6 l4">
                <input type="number" class="value" id="timeout"/>
                <label for="timeout" class="translate">timeout</label>
                <span class="translate">sec</span>
            </div>
            <div class="input-field col s12 m6 l4">
                <input type="number" class="value" id="poll"/>
                <label for="poll" class="translate">poll</label>
                <span class="translate">ms</span>
            </div>
        </div>
        <div class="row">
            <div class="input-field col s12 m6 l4">
                <input type="text" class="value" id="login">
                <label for="login" class="translate">login</label>
            </div>
            <div class="input-field col s12 m6 l4">
                <input type="password" class="value" id="password">
                <label for="password" class="translate">password</label>
            </div>
        </div>
        <div class="row">
            <div class="col s12 m3">
                <span class="translate" for="following">following</span>
            </div>
        </div>
        <div class="row">
            <div class="col s12 m3">
                <input type="checkbox" class="value" id="ch2"/>
                <span class="translate" for="ch2">ch2</span>
            </div>
        </div>
        <div class="row">
            <div class="col s12 m3">
                <input type="checkbox" class="value" id="ch3"/>
                <span class="translate" for="ch3">ch3</span>
            </div>
        </div>
        <div class="row">
            <div class="col s12 m3">
                <input type="checkbox" class="value" id="ch4"/>
                <span class="translate" for="ch4">ch4</span>
            </div>
        </div>
        <div class="row">
            <div class="col s12 m3">
                <input type="checkbox" class="value" id="ch5"/>
                <span class="translate" for="ch5">ch5</span>
            </div>
        </div>
        <div class="row">
            <div class="col s12 m3">
                <input type="checkbox" class="value" id="ch6"/>
                <span class="translate" for="ch6">ch6</span>
            </div>
        </div>
        <div class="row">
            <div class="col s12 m3">
                <input type="checkbox" class="value" id="ch7"/>
                <span class="translate" for="ch7">ch7</span>
            </div>
        </div>
        <div class="row">
            <div class="col s12 m3">
                <input type="checkbox" class="value" id="ch8"/>
                <span class="translate" for="ch8">ch8</span>
            </div>
        </div>
        <div class="row">
            <div class="col s12 m3">
                <input type="checkbox" class="value" id="ch9"/>
                <span class="translate" for="ch9">ch9</span>
            </div>
        </div>
        <div class="row">
            <div class="col s12">
                <p class="translate">on save adapter restarts with new config immediately</p>
            </div>
        </div>
    </div>
</div>
</body>

</html>


File: /admin\words.js
/*global systemDictionary:true */
/*
+===================== DO NOT MODIFY ======================+
| This file was generated by translate-adapter, please use |
| `translate-adapter adminLanguages2words` to update it.   |
+===================== DO NOT MODIFY ======================+
*/
'use strict';

systemDictionary = {
    "MikroTik adapter settings": {                    "en": "MikroTik adapter settings",                        "de": "MikroTik-Adaptereinstellungen",                    "ru": "Настройки адаптера МикроТик",                      "pt": "Configurações do adaptador MikroTik",              "nl": "MikroTik-adapterinstellingen",                     "fr": "Paramètres de l'adaptateur MikroTik",              "it": "Impostazioni dell'adattatore MikroTik",            "es": "Configuración del adaptador MikroTik",             "pl": "Ustawienia adaptera MikroTik",                     "uk": "Налаштування адаптера MikroTik",                   "zh-cn": "MikroTik 适配器设置"},
    "ch2": {                                          "en": "firewall/nat",                                     "de": "Firewall/nat",                                     "ru": "брандмауэр/нат",                                   "pt": "firewall/nat",                                     "nl": "firewall/nat",                                     "fr": "pare-feu/nat",                                     "it": "firewall/nat",                                     "es": "cortafuegos/nat",                                  "pl": "zapora sieciowa/nat",                              "uk": "брандмауер/фіз",                                   "zh-cn": "防火墙/NAT"},
    "ch3": {                                          "en": "dhcp-server/lease",                                "de": "DHCP-Server/Lease",                                "ru": "DHCP-сервер/аренда",                               "pt": "servidor dhcp/aluguel",                            "nl": "dhcp-server/lease",                                "fr": "serveur DHCP/location",                            "it": "server DHCP/leasing",                              "es": "servidor dhcp/arrendamiento",                      "pl": "serwer DHCP/dzierżawa",                            "uk": "dhcp-сервер/оренда",                               "zh-cn": "dhcp 服务器/租用"},
    "ch4": {                                          "en": "interface",                                        "de": "Schnittstelle",                                    "ru": "интерфейс",                                        "pt": "interface",                                        "nl": "koppel",                                           "fr": "interface",                                        "it": "interfaccia",                                      "es": "interfaz",                                         "pl": "interfejs",                                        "uk": "інтерфейс",                                        "zh-cn": "界面"},
    "ch5": {                                          "en": "firewall/filter",                                  "de": "Firewall/Filter",                                  "ru": "брандмауэр/фильтр",                                "pt": "firewall/filtro",                                  "nl": "firewall/filter",                                  "fr": "pare-feu/filtre",                                  "it": "firewall/filtro",                                  "es": "cortafuegos/filtro",                               "pl": "zapora/filtr",                                     "uk": "брандмауер/фільтр",                                "zh-cn": "防火墙/过滤器"},
    "ch6": {                                          "en": "wireless/registration-table",                      "de": "WLAN/Anmeldetabelle",                              "ru": "беспроводной/регистрационный стол",                "pt": "sem fio/mesa de registro",                         "nl": "draadloos/registratietafel",                       "fr": "table d'enregistrement/sans fil",                  "it": "wireless/tabella di registrazione",                "es": "mesa-de-registro/inalámbrica",                     "pl": "tabela bezprzewodowa/rejestracyjna",               "uk": "бездротовий/реєстраційний стіл",                   "zh-cn": "无线/注册表"},
    "ch7": {                                          "en": "address",                                          "de": "Adresse",                                          "ru": "адрес",                                            "pt": "endereço",                                         "nl": "adres",                                            "fr": "adresse",                                          "it": "indirizzo",                                        "es": "DIRECCIÓN",                                        "pl": "adres",                                            "uk": "адресу",                                           "zh-cn": "地址"},
    "ch8": {                                          "en": "firewall/address-list",                            "de": "Firewall/Adressliste",                             "ru": "брандмауэр/список адресов",                        "pt": "firewall/lista de endereços",                      "nl": "firewall/adreslijst",                              "fr": "pare-feu/liste d'adresses",                        "it": "firewall/elenco indirizzi",                        "es": "firewall/lista de direcciones",                    "pl": "zapora ogniowa/lista adresów",                     "uk": "брандмауер/список адрес",                          "zh-cn": "防火墙/地址列表"},
    "ch9": {                                          "en": "caps-man/registration-table",                      "de": "caps-man/registration-table",                      "ru": "шапки-человек/таблица-регистрации",                "pt": "caps-man/tabela de registro",                      "nl": "caps-man/inschrijvingstabel",                      "fr": "casquettes-homme/table-d'inscription",             "it": "caps-man/tabella-registrazione",                   "es": "caps-man/tabla-de-registro",                       "pl": "caps-man/tabela-rejestracyjna",                    "uk": "caps-man/registration-table",                      "zh-cn": "帽人/登记表"},
    "def": {                                          "en": "default (8728)",                                   "de": "Standard (8728)",                                  "ru": "по умолчанию (8728)",                              "pt": "padrão (8728)",                                    "nl": "standaard (8728)",                                 "fr": "par défaut (8728)",                                "it": "predefinito (8728)",                               "es": "predeterminado (8728)",                            "pl": "domyślny (8728)",                                  "uk": "за замовчуванням (8728)",                          "zh-cn": "默认（8728）"},
    "following": {                                    "en": "Receive the following data:",                      "de": "Erhalten Sie folgende Daten:",                     "ru": "Получите следующие данные:",                       "pt": "Receba os seguintes dados:",                       "nl": "Ontvang de volgende gegevens:",                    "fr": "Recevez les données suivantes :",                  "it": "Ricevi i seguenti dati:",                          "es": "Reciba los siguientes datos:",                     "pl": "Otrzymaj następujące dane:",                       "uk": "Отримайте такі дані:",                             "zh-cn": "接收以下数据："},
    "host": {                                         "en": "IP Address",                                       "de": "IP Adresse",                                       "ru": "Айпи адрес",                                       "pt": "Endereço de IP",                                   "nl": "IP adres",                                         "fr": "Adresse IP",                                       "it": "Indirizzo IP",                                     "es": "Dirección IP",                                     "pl": "Adres IP",                                         "uk": "IP-адреса",                                        "zh-cn": "IP地址"},
    "login": {                                        "en": "login",                                            "de": "Anmeldung",                                        "ru": "авторизоваться",                                   "pt": "Conecte-se",                                       "nl": "Log in",                                           "fr": "se connecter",                                     "it": "login",                                            "es": "acceso",                                           "pl": "Zaloguj sie",                                      "uk": "логін",                                            "zh-cn": "登录"},
    "ms": {                                           "en": "milliseconds",                                     "de": "Millisekunden",                                    "ru": "миллисекунды",                                     "pt": "milissegundos",                                    "nl": "milliseconden",                                    "fr": "millisecondes",                                    "it": "millisecondi",                                     "es": "milisegundos",                                     "pl": "milisekundy",                                      "uk": "мілісекунд",                                       "zh-cn": "毫秒"},
    "on save adapter restarts with new config immediately": {"en": "on save adapter restarts with new config immediately", "de": "Beim Speichern wird der Adapter sofort mit der neuen Konfiguration neu gestartet", "ru": "при сохранении адаптер немедленно перезагружается с новой конфигурацией", "pt": "ao salvar o adaptador reinicia com a nova configuração imediatamente", "nl": "bij het opslaan wordt de adapter onmiddellijk opnieuw opgestart met nieuwe configuratie", "fr": "lors de la sauvegarde, l'adaptateur redémarre immédiatement avec une nouvelle configuration", "it": "al salvataggio l'adattatore si riavvia immediatamente con la nuova configurazione", "es": "Al guardar, el adaptador se reinicia con una nueva configuración inmediatamente.", "pl": "po zapisaniu adapter natychmiast uruchamia się ponownie z nową konfiguracją", "uk": "під час збереження адаптер негайно перезавантажується з новою конфігурацією", "zh-cn": "保存适配器后立即使用新配置重新启动"},
    "password": {                                     "en": "password",                                         "de": "Passwort",                                         "ru": "пароль",                                           "pt": "senha",                                            "nl": "wachtwoord",                                       "fr": "mot de passe",                                     "it": "parola d'ordine",                                  "es": "contraseña",                                       "pl": "hasło",                                            "uk": "пароль",                                           "zh-cn": "密码"},
    "poll": {                                         "en": "Data refresh interval",                            "de": "Datenaktualisierungsintervall",                    "ru": "Интервал обновления данных",                       "pt": "Intervalo de atualização de dados",                "nl": "Interval voor gegevensvernieuwing",                "fr": "Intervalle d'actualisation des données",           "it": "Intervallo di aggiornamento dei dati",             "es": "Intervalo de actualización de datos",              "pl": "Interwał odświeżania danych",                      "uk": "Інтервал оновлення даних",                         "zh-cn": "数据刷新间隔"},
    "port": {                                         "en": "port",                                             "de": "Hafen",                                            "ru": "порт",                                             "pt": "porta",                                            "nl": "haven",                                            "fr": "port",                                             "it": "porta",                                            "es": "puerto",                                           "pl": "Port",                                             "uk": "порт",                                             "zh-cn": "港口"},
    "sec": {                                          "en": "seconds",                                          "de": "Sekunden",                                         "ru": "секунды",                                          "pt": "segundos",                                         "nl": "seconden",                                         "fr": "secondes",                                         "it": "secondi",                                          "es": "segundos",                                         "pl": "sekundy",                                          "uk": "секунд",                                           "zh-cn": "秒"},
    "timeout": {                                      "en": "timeout",                                          "de": "Auszeit",                                          "ru": "тайм-аут",                                         "pt": "tempo esgotado",                                   "nl": "time-out",                                         "fr": "temps mort",                                       "it": "tempo scaduto",                                    "es": "se acabó el tiempo",                               "pl": "koniec czasu",                                     "uk": "час вийшов",                                       "zh-cn": "暂停"},
};

File: /docs\de\template.md
# Das ist die Dokumentation

(Picture)[img/picture.png)

File: /docs\en\template.md
# This is Documentation

(Picture)[img/picture.png)

File: /docs\ru\template.md
# Это документация

(Picture)[img/picture.png)

File: /io-package.json
{
  "common": {
    "name": "mikrotik",
    "version": "1.2.1",
    "news": {
      "1.2.1": {
        "en": "Default value for commands.add_firewall has been corrected [#138]\nSome issues reported by adapter-checker have been fixed\nTesting for node.js 22 has been added\nDependencies have been updated",
        "de": "Standardwert für commands.add_firewall wurde korrigiert [#138]\nEinige von Adapter-Checker gemeldete Probleme wurden behoben\nTests für node.js 22 wurden hinzugefügt\nAbhängigkeiten wurden aktualisiert",
        "ru": "Значение по умолчанию для commands.add_firewall было исправлено [#138]\nНекоторые проблемы, о которых сообщил адаптер-контроль, были исправлены\nДобавлено тестирование на node.js 22\nЗависимость обновлена",
        "pt": "Valor padrão para commands.add_firewall foi corrigido [#138]\nAlguns problemas relatados pelo verificador do adaptador foram corrigidos\nTestar para node.js 22 foi adicionado\nAs dependências foram atualizadas",
        "nl": "Standaardwaarde voor commando's.add_firewall is gecorrigeerd [#138]\nSommige problemen gemeld door adapter-checker zijn opgelost\nTest op node.js 22 is toegevoegd\nAfhankelijkheden zijn bijgewerkt",
        "fr": "La valeur par défaut pour commandes.add_firewall a été corrigée [#138]\nCertains problèmes signalés par l'adaptateur-vérificateur ont été corrigés\nTests pour node.js 22 a été ajouté\nLes dépendances ont été actualisées",
        "it": "Valore predefinito per commands.add_firewall è stato corretto [#138]\nAlcuni problemi segnalati da adattatore-checker sono stati risolti\nTest per node.js 22 è stato aggiunto\nLe dipendenze sono state aggiornate",
        "es": "Valor predeterminado para comandos.add_firewall ha sido corregido [#138]\nSe han resuelto algunas cuestiones comunicadas por el control de adaptador\nSe han añadido pruebas para node.js 22\nSe han actualizado las dependencias",
        "pl": "Wartość domyślna dla commands.add _ firewall została poprawiona [# 138]\nNiektóre problemy zgłoszone przez sprawdzacz adaptera zostały ustalone\nDodano badanie na node.js 22\nZaktualizowano zależności",
        "uk": "За замовчуванням значення для команд.add_firewall було виправлено [#138]\nДеякі питання, які повідомляються адаптером, були виправлені\nТестування для node.js 22 було додано\nЗалежність було оновлено",
        "zh-cn": "命令的默认值. add_ firewall 已被更正 [# 138]\n适配器检查器报告的一些问题已经解决\n增加了节点22测试\n依赖关系已更新"
      },
      "1.2.0": {
        "en": "Adapter requires node.js >= 18 and js-controller >= 5 now\nDependencies have been updated",
        "de": "Adapter benötigt node.js >= 18 und js-controller >= 5 jetzt\nAbhängigkeiten wurden aktualisiert",
        "ru": "Адаптер требует node.js >= 18 и js-контроллер >= 5 сейчас\nЗависимость обновлена",
        "pt": "Adapter requer node.js >= 18 e js-controller >= 5 agora\nAs dependências foram atualizadas",
        "nl": "Voor adaptor zijn node.js < 18 en js-controller > Nu 5\nAfhankelijkheden zijn bijgewerkt",
        "fr": "L'adaptateur nécessite node.js >= 18 et js-controller >= 5 maintenant\nLes dépendances ont été actualisées",
        "it": "Adattatore richiede node.js >= 18 e js-controller >= 5 ora\nLe dipendenze sono state aggiornate",
        "es": "Adaptador requiere node.js √≥= 18 y js-controller 5 ahora\nSe han actualizado las dependencias",
        "pl": "Adapter wymaga node.js > = 18 i kontroler js- > = 5 teraz\nZaktualizowano zależności",
        "uk": "Адаптер вимагає node.js >= 18 і js-controller >= 5 тепер\nЗалежність було оновлено",
        "zh-cn": "适配器需要节点.js QQ18和js控制器 QQ 现在5号\n依赖关系已更新"
      },
      "1.1.1": {
        "en": "Packages updated",
        "de": "Pakete aktualisiert",
        "ru": "Пакеты обновлены",
        "pt": "Pacotes atualizados",
        "nl": "Verpakking geüpload",
        "fr": "Packages updated",
        "it": "Pacchetti aggiornati",
        "es": "Paquetes actualizados",
        "pl": "Pakiet",
        "uk": "Пакети оновлені",
        "zh-cn": "更新的包装"
      },
      "1.0.15": {
        "en": "changed parse RAW",
        "de": "Parse RAW geändert",
        "ru": "изменен синтаксический анализ RAW",
        "pt": "alterado parse RAW",
        "nl": "veranderde parse RAW",
        "fr": "modifié l'analyse RAW",
        "it": "modificato parse RAW",
        "es": "cambio de análisis RAW",
        "pl": "zmieniono parsowanie RAW",
        "zh-cn": "更改解析RAW",
        "uk": "змінено розбір RAW"
      },
      "1.0.14": {
        "en": "added CAPsMAN",
        "de": "fügte CAPsMAN hinzu",
        "ru": "добавил CAPsMAN",
        "pt": "adicionado CAPsMAN",
        "nl": "CAPsMAN toegevoegd",
        "fr": "a ajouté CAPsMAN",
        "it": "ha aggiunto CAPsMAN",
        "es": "añadido CAPsMAN",
        "pl": "dodał CAPsMAN",
        "zh-cn": "添加了CAPsMAN",
        "uk": "додав CAPsMAN"
      },
      "1.0.13": {
        "en": "changed parsing RAW command\nadded last-link-up-time and last-link-down-time to interface",
        "de": "geänderter Parsing-RAW-Befehl\nLast-Link-Up-Time und Last-Link-Down-Time zur Schnittstelle hinzugefügt",
        "ru": "изменена команда синтаксического анализа RAW\nдобавлено время последней связи и время отключения последней ссылки в интерфейс",
        "pt": "foi alterado o comando RAW de análise\nadicionado o tempo do último link para cima e o tempo do último link para baixo para a interface",
        "nl": "gewijzigde parsing RAW-opdracht\nlaatste-link-up-time en last-link-down-time toegevoegd aan interface",
        "fr": "Modification de la commande d'analyse RAW\najout de l'heure de dernière liaison et de dernière interruption de liaison à l'interface",
        "it": "modificato il comando RAW di analisi\naggiunto il tempo di attività dell'ultimo collegamento e il tempo di inattività dell'ultimo collegamento all'interfaccia",
        "es": "se modificó el comando RAW de análisis sintáctico\nse agregó el tiempo de activación del último enlace y el tiempo de desactivación del último enlace a la interfaz",
        "pl": "zmieniono polecenie parsowania RAW\ndodano czas ostatniego łącza do interfejsu i czas wyłączenia ostatniego łącza do interfejsu",
        "zh-cn": "更改了解析RAW命令\n为接口添加了上次链接时间和上次链接时间",
        "uk": "змінена команда аналізу RAW\nдодано час останнього підключення та час останнього відключення зв’язку до інтерфейсу"
      },
      "1.0.12": {
        "en": "fixed error symb",
        "de": "fixed error symb",
        "ru": "fixed error symb",
        "pt": "fixed error symb",
        "fr": "fixed error symb",
        "nl": "fixed error symb",
        "it": "simbolo di errore corretto",
        "es": "símbolo de error arreglado",
        "pl": "naprawiono symbol błędu",
        "uk": "виправлена ​​помилка симв",
        "zh-cn": "固定错误符号"
      }
    },
    "titleLang": {
      "en": "MikroTik Router",
      "de": "MikroTik Router",
      "ru": "MikroTik Router",
      "pt": "MikroTik Router",
      "nl": "MikroTik Router",
      "fr": "Routeur MikroTik",
      "it": "MikroTik Router",
      "es": "MikroTik Router",
      "pl": "Ruter MikroTik",
      "uk": "Маршрутизатор MikroTik",
      "zh-cn": "MikroTik 路由器"
    },
    "desc": {
      "en": "ioBroker Mikrotik Adapter",
      "de": "ioBroker Mikrotik Adapter",
      "ru": "ioBroker Mikrotik Adapter",
      "pt": "adaptador ioBroker Mikrotik",
      "nl": "ioBroker Mikrotik Adapter",
      "fr": "adaptateur ioBroker Mikrotik",
      "it": "ioBroker Mikrotik adattatore",
      "es": "ioBroker Mikrotik Adapter",
      "pl": "joBroker Mikrotik Adapter",
      "uk": "ioBroker Mikrotik адаптер",
      "zh-cn": "ioBroker Mikrotik 适应器"
    },
    "platform": "Javascript/Node.js",
    "mode": "daemon",
    "licenseInformation": {
      "license": "MIT",
      "type": "free"
    },
    "icon": "mikrotik.png",
    "enabled": false,
    "extIcon": "https://raw.githubusercontent.com/iobroker-community-adapters/iobroker.mikrotik/master/admin/mikrotik.png",
    "keywords": [
      "mikrotik"
    ],
    "readme": "https://github.com/iobroker-community-adapters/iobroker.mikrotik/blob/master/README.md",
    "loglevel": "info",
    "tier": 2,
    "type": "hardware",
    "connectionType": "local",
    "dataSource": "poll",
    "adminUI": {
      "config": "materialize"
    },
    "authors": [
      {
        "name": "instalator",
        "email": "vvvalt@mail.ru"
      }
    ],
    "dependencies": [
      {
        "js-controller": ">=5.0.19"
      }
    ],
    "globalDependencies": [
      {
        "admin": ">=6.13.16"
      }
    ]
  },
  "native": {
    "host": "192.168.88.1",
    "port": 8728,
    "login": "admin",
    "password": "",
    "timeout": 10,
    "ch2": true,
    "ch3": true,
    "ch4": true,
    "ch5": true,
    "ch6": true,
    "ch7": true,
    "ch8": false,
    "ch9": false
  },
  "objects": [],
  "instanceObjects": [
    {
      "_id": "info.connection",
      "type": "state",
      "common": {
        "role": "indicator.connected",
        "name": "If connected to MikroTik",
        "type": "boolean",
        "read": true,
        "write": false,
        "def": false
      },
      "native": {}
    },
    {
      "_id": "commands.reboot",
      "type": "state",
      "common": {
        "role": "button",
        "name": "Reboot router",
        "type": "boolean",
        "read": false,
        "write": true,
        "def": false
      },
      "native": {}
    },
    {
      "_id": "commands.shutdown",
      "type": "state",
      "common": {
        "role": "button",
        "name": "Shut down router",
        "type": "boolean",
        "read": false,
        "write": true,
        "def": false
      },
      "native": {}
    },
    {
      "_id": "commands.raw",
      "type": "state",
      "common": {
        "role": "text",
        "name": "raw commands router api",
        "type": "string",
        "read": false,
        "write": true
      },
      "native": {}
    },
    {
      "_id": "commands.response",
      "type": "state",
      "common": {
        "role": "json",
        "name": "response router api",
        "type": "string",
        "read": true,
        "write": false
      },
      "native": {}
    },
    {
      "_id": "commands.usb_reset",
      "type": "state",
      "common": {
        "role": "button",
        "name": "USB power reset",
        "type": "boolean",
        "read": false,
        "write": true,
        "def": false
      },
      "native": {}
    },
    {
      "_id": "commands.add_firewall",
      "type": "state",
      "common": {
        "role": "text",
        "name": "add address to firewall",
        "type": "string",
        "read": false,
        "write": true,
        "def": ""
      },
      "native": {}
    }
  ]
}


File: /lib\adapter-config.d.ts
// This file extends the AdapterConfig type from "@types/iobroker"
// using the actual properties present in io-package.json
// in order to provide typings for adapter.config properties

import { native } from '../io-package.json';

type _AdapterConfig = typeof native;

// Augment the globally declared type ioBroker.AdapterConfig
declare global {
    namespace ioBroker {
        interface AdapterConfig extends _AdapterConfig {
            // Do not enter anything here!
        }
    }
}

File: /lib\tools.js
const axios = require('axios');

/**
 * Tests whether the given variable is a real object and not an Array
 * @param {any} it The variable to test
 * @returns {it is Record<string, any>}
 */
function isObject(it) {
    // This is necessary because:
    // typeof null === 'object'
    // typeof [] === 'object'
    // [] instanceof Object === true
    return Object.prototype.toString.call(it) === '[object Object]';
}

/**
 * Tests whether the given variable is really an Array
 * @param {any} it The variable to test
 * @returns {it is any[]}
 */
function isArray(it) {
    if (typeof Array.isArray === 'function') return Array.isArray(it);
    return Object.prototype.toString.call(it) === '[object Array]';
}

/**
 * Translates text to the target language. Automatically chooses the right translation API.
 * @param {string} text The text to translate
 * @param {string} targetLang The target languate
 * @param {string} [yandexApiKey] The yandex API key. You can create one for free at https://translate.yandex.com/developers
 * @returns {Promise<string>}
 */
async function translateText(text, targetLang, yandexApiKey) {
    if (targetLang === 'en') {
        return text;
    } else if (!text) {
        return '';
    }
    if (yandexApiKey) {
        return translateYandex(text, targetLang, yandexApiKey);
    } else {
        return translateGoogle(text, targetLang);
    }
}

/**
 * Translates text with Yandex API
 * @param {string} text The text to translate
 * @param {string} targetLang The target languate
 * @param {string} apiKey The yandex API key. You can create one for free at https://translate.yandex.com/developers
 * @returns {Promise<string>}
 */
async function translateYandex(text, targetLang, apiKey) {
    if (targetLang === 'zh-cn') {
        targetLang = 'zh';
    }
    try {
        const url = `https://translate.yandex.net/api/v1.5/tr.json/translate?key=${apiKey}&text=${encodeURIComponent(text)}&lang=en-${targetLang}`;
        const response = await axios({url, timeout: 15000});
        if (response.data && response.data.text && isArray(response.data.text)) {
            return response.data.text[0];
        }
        throw new Error('Invalid response for translate request');
    } catch (e) {
        throw new Error(`Could not translate to "${targetLang}": ${e}`);
    }
}

/**
 * Translates text with Google API
 * @param {string} text The text to translate
 * @param {string} targetLang The target languate
 * @returns {Promise<string>}
 */
async function translateGoogle(text, targetLang) {
    try {
        const url = `http://translate.googleapis.com/translate_a/single?client=gtx&sl=en&tl=${targetLang}&dt=t&q=${encodeURIComponent(text)}&ie=UTF-8&oe=UTF-8`;
        const response = await axios({url, timeout: 15000});
        if (isArray(response.data)) {
            // we got a valid response
            return response.data[0][0][0];
        }
        throw new Error('Invalid response for translate request');
    } catch (e) {
        if (e.response && e.response.status === 429) {
            throw new Error(
                `Could not translate to "${targetLang}": Rate-limited by Google Translate`
            );
        } else {
            throw new Error(`Could not translate to "${targetLang}": ${e}`);
        }
    }
}

module.exports = {
    isArray,
    isObject,
    translateText
};


File: /LICENSE
The MIT License (MIT)

Copyright (c) 2024 iobroker-community-adapters <iobroker-community-adapters@gmx.de>
Copyright (c) 2021-2022 instalator <vvvalt@mail.ru>

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.


File: /main.js
'use strict';
const utils = require('@iobroker/adapter-core');
let adapter;
const MikroNode = require('mikronode-ng');
let _poll, poll_time, connect = false, timer, iswlan = false;
let con, _con, connection, old_states, flagOnError = false;
const states = {
    'wireless':   [],
    'dhcp':       [],
    'interface':  [],
    'filter':     [],
    'nat':        [],
    'firewall':   [],
    'capsman':    [],
    'lists':      {
        'dhcp_list':     [],
        'wifi_list':     [],
        'firewall_list': []
    },
    'systeminfo': {}
};

const commands = {
    'reboot':       '/system/reboot',
    'shutdown':     '/system/shutdown',
    'usb_reset':    '/system/routerboard/usb/power-reset',
    'add_firewall': ''
};

function startAdapter(options) {
    return adapter = utils.adapter(Object.assign({}, options, {
        systemConfig: true,
        name:         'mikrotik',
        ready:        main,
        unload:       (callback) => {
            clearTimeout(_poll);
            clearTimeout(timer);
            if (connection && _con) {
                _con.clearEvents = true;
                connection.close();
            }
            try {
                adapter.log.debug('cleaned everything up...');
                callback();
            } catch (e) {
                callback();
            }
        },
        stateChange:  (id, state) => {
            if (state && !state.ack) {
                adapter.log.debug(`stateChange ${id} ${JSON.stringify(state)}`);
                const ids = id.split('.');
                let val = state.val;
                const cmd = ids[ids.length - 1].toString().toLowerCase();
                let cmdlist;
                //adapter.log.error('[cmd] = ' + cmd);
                if (commands[cmd] !== undefined) {
                    if (cmd === 'add_firewall') {
                        cmdlist = val.split(',');
                        SetCommand('/ip/firewall/address-list/add\n=list=' + cmdlist[0] + '\n=address=' + cmdlist[1] + '\n=comment=' + cmdlist[2]);
                    } else {
                        SetCommand(commands[cmd]);
                    }
                }
                if (cmd === 'raw') {
                    if (val[0] !== '/') {
                        val = '/' + val;
                    }
                    if (!val.includes('\u000A')){
                        val = val.replace(/\s/g, '\u000A=');
                    }
                    //cmdlist = val.split(',');
                    SetCommand(val);
                }
                if (cmd === 'send_sms') {
                    //system resource usb print
                    //port print detail
                    //tool sms send port=usb1 channel=2 phone-number="+7..." message="text"
                }
                if (cmd === 'disabled') {
                    let _id;
                    id = id.replace('disabled', 'id');
                    adapter.getState(id, (err, st) => {
                        if ((err || !st)){
                            adapter.log.error('getState ' + JSON.stringify(err));
                        } else {
                            _id = st.val.replace('*', '');
                            GetCmd(id, cmd, _id, val);
                        }
                    });
                }
            }
        }
    }));
}

function GetCmd(id, cmd, _id, val) {
    let set;
    const ids = id.split('.');
    if (val === true || val === 'true') {
        val = 'yes';
    } else {
        val = 'no';
    }
    if (ids[2] === 'filter') {
        set = '/ip/firewall/filter/set\n=disabled=' + val + '\n=.id=*' + _id;
    }
    if (ids[2] === 'interface') {
        set = '/interface/set\n=disabled=' + val + '\n=.id=*' + _id;
    }
    if (ids[2] === 'nat') {
        set = `/ip/firewall/nat/set\n=disabled=${val}\n=.id=*${_id}`;
    }
    if (ids[2] === 'firewall') {
        set = '/ip/firewall/address-list/set\n=disabled=' + val + '\n=.id=*' + _id;
    }
    SetCommand(set);
}

function SetCommand(set) {
    adapter.log.debug('SetCommand ' + set);
    _con.write(set, (ch) => {
        ch.once('done', (p) => {
            const d = MikroNode.parseItems(p);
            adapter.log.info('SetCommand Done response: ' + JSON.stringify(d));
            adapter.setState('commands.response', JSON.stringify(d), true);
        });
        ch.on('trap', (e /*, chan*/) => {
            adapter.log.debug('commands Trap response ' + e && e.errors[0]);
            adapter.setState('commands.response', e && e.errors[0].message, true);
        });
        ch.on('error', (e /*, chan*/) => {
            err(e);
        });
    });
}

function main() {
    adapter.subscribeStates('*');
    old_states = JSON.parse(JSON.stringify(states));
    poll_time = adapter.config.poll ? adapter.config.poll :5000;
    con = {
        'host':     adapter.config.host ? adapter.config.host : '192.168.1.11',
        'port':     adapter.config.port ? adapter.config.port : 8728,
        'login':    adapter.config.login ? adapter.config.login  :'admin',
        'password': adapter.config.password ? adapter.config.password : ''
    };
    if (con.host && con.port) {
        let _connection = MikroNode.getConnection(con.host, con.login, con.password, {
            port:           con.port,
            timeout:        adapter.config.timeout ? (adapter.config.timeout + (poll_time / 1000)) :(10 + (poll_time / 1000)),
            closeOnTimeout: false,
            closeOnDone:    false
        });
        connection = _connection.connect((c) => {
            _con = c.openChannel();
            _con.clearEvents = true;
            adapter.log.info('MikroTik ' + c.status + ' to: ' + c.host);
            adapter.setState('info.connection', true, true);
            connect = true;
            parse();
        });
        connection.on('trap', (e) => {
            adapter.log.debug('TRAP ' + JSON.stringify(e));
            err(e);
        });
        connection.on('timeout', (e) => {
            err(e);
        });
        connection.on('error', (e) => {
            err(e);
        });
        connection.on('close', (e) => {
            err(e);
        });
    }
}

function ch1(cb) {
    adapter.log.debug('ch1 send command');
    _con.write('/system/resource/print', (ch) => {
        ch.once('done', p => {
            adapter.log.debug('ch1 done: ' + JSON.stringify(p));
            const d = MikroNode.parseItems(p);
            states.systeminfo = d[0];
            adapter.log.debug('/system/resource/print' + JSON.stringify(d));
            cb && cb();
        });
        if (!flagOnError) {
            flagOnError = true;
            ch.on('error', (e) => {
                adapter.log.debug('Oops error: ' + e);
            });
        }
    });
}

function ch2(cb) {
    if (adapter.config.ch2) {
        adapter.log.debug('ch2 send command');
        _con.write('/ip/firewall/nat/print', (ch) => {
            ch.once('done', (p) => {
                adapter.log.debug('ch2 done: ' + JSON.stringify(p));
                const d = MikroNode.parseItems(p);
                ParseNat(d);
                adapter.log.debug('/ip/firewall/nat/print' + JSON.stringify(d));
                cb && cb();
            });
            /*ch.once('error', function(e, chan) {
                err(e, true);
            });*/
        });
    } else cb && cb();
}

function ch3(cb) {
    if (adapter.config.ch3) {
        adapter.log.debug('ch3 send command');
        _con.write('/ip/dhcp-server/lease/print', (ch) => {
            ch.once('done', (p) => {
                adapter.log.debug('ch3 done: ' + JSON.stringify(p));
                const d = MikroNode.parseItems(p);
                ParseDHCP(d);
                adapter.log.debug('/ip/dhcp-server/lease/print' + JSON.stringify(d));
                cb && cb();
            });
            /*ch.once('error', function(e, chan) {
                err(e, true);
            });*/
        });
    } else cb && cb();
}

function ch4(cb) {
    if (adapter.config.ch4) {
        adapter.log.debug('ch4 send command');
        _con.write('/interface/print', (ch) => {
            ch.once('done', (p) => {
                adapter.log.debug('ch4 done: ' + JSON.stringify(p));
                const d = MikroNode.parseItems(p);
                ParseInterface(d);
                adapter.log.debug('/interface/print' + JSON.stringify(d));
                cb && cb();
            });
            /*ch.once('error', function(e, chan) {
                err(e, true);
            });*/
        });
    } else cb && cb();
}

function ch5(cb) {
    if (adapter.config.ch5) {
        adapter.log.debug('ch5 send command');
        _con.write('/ip/firewall/filter/print', (ch) => {
            ch.once('done', (p) => {
                adapter.log.debug('ch5 done: ' + JSON.stringify(p));
                const d = MikroNode.parseItems(p);
                ParseFilter(d);
                adapter.log.debug('/ip/firewall/filter/print' + JSON.stringify(d));
                cb && cb();
            });
            /*ch.once('error', function(e, chan) {
                err(e, true);
            });*/
        });
    } else cb && cb();
}

function ch6(cb) {
    if (adapter.config.ch6) {
        adapter.log.debug('ch6 send command');
        if (iswlan) {
            _con.write('/interface/wireless/registration-table/print', (ch) => {
                ch.once('done', (p) => {
                    adapter.log.debug('ch6 done: ' + JSON.stringify(p));
                    const d = MikroNode.parseItems(p);
                    ParseWiFi(d);
                    adapter.log.debug('/interface/wireless/registration-table/print' + JSON.stringify(d));
                    cb && cb();
                });
                /*ch.once('error', function(e, chan) {
                 err(e, true);
                 });*/
            });
        } else {
            adapter.log.debug('Mikrotik is not WiFi');
            cb && cb();
        }
    } else cb && cb();
}

function ch7(cb) {
    if (adapter.config.ch7) {
        adapter.log.debug('ch7 send command');
        _con.write('/ip/address/print', (ch) => {
            ch.once('done', (p) => {
                adapter.log.debug('ch7 done: ' + JSON.stringify(p));
                const d = MikroNode.parseItems(p);
                ParseWAN(d);
                adapter.log.debug('/ip/address/print' + JSON.stringify(d));
                cb && cb();
            });
            /*ch.once('error', function(e, chan) {
             err(e, true);
             });*/
        });
    } else cb && cb();
}

function ch8(cb) {
    if (adapter.config.ch8) {
        adapter.log.debug('ch8 send command');
        _con.write('/ip/firewall/address-list/print', (ch) => {
            ch.once('done', (p) => {
                adapter.log.debug('ch8 done: ' + JSON.stringify(p));
                const d = MikroNode.parseItems(p);
                ParseFirewallList(d);
                adapter.log.debug('/ip/firewall/address-list/print' + JSON.stringify(d));
                cb && cb();
            });
            /*ch.once('error', function(e, chan) {
             err(e, true);
             });*/
        });
    } else cb && cb();
}

function ch9(cb) {
    if (adapter.config.ch9) {
        adapter.log.debug('ch9 send command');
        _con.write('/caps-man/registration-table/print', (ch) => {
            ch.once('done', (p) => {
                adapter.log.debug('ch9 done: ' + JSON.stringify(p));
                const d = MikroNode.parseItems(p);
                ParseCapsMan(d);
                adapter.log.debug('/caps-man/registration-table/print' + JSON.stringify(d));
                cb && cb();
            });
        });
    } else cb && cb();
}

function parse() {
    adapter.log.debug('Start parse function');
    clearTimeout(_poll);
    _poll = setTimeout(() => {
        ch1(() => {
            ch2(() => {
                ch3(() => {
                    ch4(() => {
                        ch5(() => {
                            ch6(() => {
                                ch7(() => {
                                    ch8(() => {
                                        ch9(() => {
                                            SetStates();
                                        });
                                    });
                                });
                            });
                        });
                    });
                });
            });
        });
    }, poll_time);
}

function ParseNat(d, cb) {
    const res = [];
    d.forEach((item, i) => {
        if (d[i]['.id'] !== undefined) {
            res.push({
                'id':            d[i]['.id'],
                'chain':         d[i]['chain'],
                'comment':       d[i]['comment'] ? d[i]['comment'] :'',
                'disabled':      d[i]['disabled'],
                'out-interface': d[i]['out-interface'] ? d[i]['out-interface'] :'',
                'in-interface':  d[i]['in-interface'] ? d[i]['in-interface'] :'',
                'dst-port':      d[i]['dst-port'] ? d[i]['dst-port'] :'',
                'to-ports':      d[i]['to-ports'] ? d[i]['dto-ports'] :'',
                'protocol':      d[i]['protocol'] ? d[i]['protocol'] :'',
                'to-addresses':  d[i]['to-addresses'] ? d[i]['to-addresses'] :'',
                'action':        d[i]['action']
            });
        }
    });
    states.nat = res;
    cb && cb();
}

function ParseFilter(d, cb) {
    const res = [];
    d.forEach((item, i) => {
        if (d[i]['disabled'] !== undefined) {
            res.push({
                'id':       d[i]['.id'],
                'chain':    d[i]['chain'],
                'comment':  d[i]['comment'] ? d[i]['comment'] :'',
                'disabled': d[i]['disabled']
            });
        }
    });
    states.filter = res;
    cb && cb();
}

function ParseInterface(d, cb) {
    const res = [];
    d.forEach((item, i) => {
        if (d[i]['name'] !== undefined) {
            res.push({
                'name':                d[i]['name'].replace('*', '_').replace('<', '').replace('>', ''),
                'id':                  d[i]['.id'],
                'type':                d[i]['type'],
                'disabled':            d[i]['disabled'],
                'mac-address':         d[i]['mac-address'],
                'running':             d[i]['running'],
                'total_rx_byte':       d[i]['rx-byte'],
                'total_tx_byte':       d[i]['tx-byte'],
                'last-link-up-time':   d[i]['last-link-up-time'] ? d[i]['last-link-up-time'] :'',
                'last-link-down-time': d[i]['last-link-down-time'] ? d[i]['last-link-down-time'] :'',
                'rx':                  (((parseInt(d[i]['rx-byte']) - parseInt(old_states.interface[i] ? old_states.interface[i]['total_rx_byte'] : d[i]['rx-byte'])) / (adapter.config.poll / 1000)) * 0.008).toFixed(2),
                'tx':                  (((parseInt(d[i]['tx-byte']) - parseInt(old_states.interface[i] ? old_states.interface[i]['total_tx_byte'] : d[i]['tx-byte'])) / (adapter.config.poll / 1000)) * 0.008).toFixed(2),
                'total_rx_packet':     d[i]['rx-packet'],
                'total_tx_packet':     d[i]['tx-packet'],
                'rx_packet':           ((parseInt(d[i]['rx-packet']) - parseInt(old_states.interface[i] ? old_states.interface[i]['total_rx_packet'] : d[i]['rx-packet'])) / (adapter.config.poll / 1000)).toFixed(0),
                'tx_packet':           ((parseInt(d[i]['tx-packet']) - parseInt(old_states.interface[i] ? old_states.interface[i]['total_tx_packet'] : d[i]['tx-packet'])) / (adapter.config.poll / 1000)).toFixed(0),
            });
        }
        if (d[i]['type'] === 'wlan') {
            iswlan = true;
        }
    });
    states.interface = res;
    cb && cb();
}

function ParseWiFi(d, cb) {
    const res = [];
    let name;
    states.lists.wifi_list = [];
    d.forEach((item, i) => {
        name = '';
        if (d[i]['mac-address'] !== undefined) {
            getNameWiFi(d[i]['mac-address'], n => {
                name = n;
                res.push({
                    'last-ip':       d[i]['last-ip'],
                    'id':            d[i]['.id'],
                    'mac-address':   d[i]['mac-address'],
                    'last-activity': d[i]['last-activity'],
                    'interface':     d[i]['interface'],
                    'name':          name
                });
            });
        }
        states.lists.wifi_list.push({
            ip:   d[i]['last-ip'],
            mac:  d[i]['mac-address'],
            name: name
        });
    });
    states.wireless = res;
    cb && cb();
}

function ParseDHCP(d, cb) {
    const res = [];
    states.lists.dhcp_list = [];
    d.forEach((item, i) => {
        //if (d[i]['host-name']/* !== undefined*/) {
        if (!d[i]['host-name'] && d[i]['mac-address']) {
            if (d[i]['comment']) {
                d[i]['host-name'] = d[i]['comment'];
            } else {
                d[i]['host-name'] = d[i]['mac-address'].replace(/[:]+/g, '');
            }
        }
        if (d[i]['.id'] !== undefined) {
            res.push({
                'name':        d[i]['host-name'] ? d[i]['host-name'] :d[i]['comment'],
                'id':          d[i]['.id'],
                'address':     d[i]['address'],
                'mac-address': d[i]['mac-address'],
                'server':      d[i]['server'],
                'status':      d[i]['status'],
                'comment':     d[i]['comment'] ? d[i]['comment'] : '',
                'blocked':     d[i]['blocked']
            });
            //}
            if (d[i]['status'] !== 'waiting') {
                states.lists.dhcp_list.push({
                    ip:   d[i]['address'],
                    mac:  d[i]['mac-address'],
                    name: d[i]['host-name'] ? d[i]['host-name'] :d[i]['comment']
                });
            }
        }
    });
    states.dhcp = res;
    cb && cb();
}

function ParseWAN(d, cb) {
    d.forEach((item, i) => {
        if (d[i]['.id'] !== undefined) {
            if (d[i]['interface'] === d[i]['actual-interface']) {
                states.systeminfo.wan = d[i]['address'];
                states.systeminfo.wan_disabled = d[i]['disabled'];
            }
        }
    });
    cb && cb();
}

function ParseFirewallList(d, cb) {
    const res = [];
    states.lists.firewall_list = [];
    d.forEach((item, i) => {
        if (d[i]['address'] !== undefined) {
            res.push({
                'address':  d[i]['address'],
                'id':       d[i]['.id'],
                'name':     d[i]['list'] + d[i]['.id'].replace('*', '_').replace('<', '').replace('>', ''),
                'disabled': d[i]['disabled'],
                'comment':  d[i]['comment'] ? d[i]['comment'] :''
            });
        }
        states.lists.firewall_list.push({
            name:    d[i]['list'],
            address: d[i]['address']
        });
    });
    states.firewall = res;
    cb && cb();
}

function ParseCapsMan(d, cb) {
    const res = [];
    d.forEach((item, i) => {
        if (d[i]['interface'] !== undefined) {
            res.push({
                'name' : d[i]['mac-address'].replace(/[:]+/g, ''),
                'id':  d[i]['.id'],
                'interface':  d[i]['interface'],
                'ssid':  d[i]['ssid'],
                'rx-rate':  d[i]['rx-rate'],
                'rx-signal':  d[i]['rx-signal'],
                'uptime':  d[i]['uptime'],
                'bytes':  d[i]['bytes'],
                'mac':       d[i]['mac-address'],
                'comment':  d[i]['comment'] ? d[i]['comment'] :''
            });
        }
    });
    states.capsman = res;
    cb && cb();
}

function SetStates() {
    Object.keys(states).forEach((key) => {
        if (states[key].length !== undefined && key !== 'lists') {
            states[key].forEach((item, i) => {
                Object.keys(states[key][i]).forEach((k) => {
                    if (old_states[key][i] === undefined) {
                        old_states[key].push({});
                    }
                    if (states[key][i][k] !== old_states[key][i][k]) {
                        old_states[key][i][k] = states[key][i][k];
                        let ids = '';
                        if (states[key][i]['name'] !== undefined) {
                            if (states[key][i]['server'] !== undefined) {
                                ids = `${key}.${states[key][i]['server']}.${states[key][i]['name'].replace('*', '_').replace('<', '').replace('>', '')}.${k}`;
                            } else {
                                ids = `${key}.${states[key][i]['name'].replace('*', '_').replace('<', '').replace('>', '')}.${k}`;
                            }
                        } else {
                            adapter.log.debug('SetStates obj: ' + JSON.stringify(states[key]));
                            adapter.log.debug('SetStates: ' + JSON.stringify(states[key][i]));
                            //let id_key = states[key][i]['id'] ? states[key][i]['id'] :
                            ids = `${key}.id${states[key][i]['id'].replace('*', '_')}.${k}`;
                        }
                        setObject(ids, states[key][i][k]);
                    }
                });
            });
        } else {
            if (key === 'lists') {
                Object.keys(states[key]).forEach((k) => {
                    const ids = key + '.' + k;
                    setObject(ids, JSON.stringify(states[key][k]));
                });
            } else if (key === 'systeminfo') {
                Object.keys(states[key]).forEach((k) => {
                    if (states[key][k] !== old_states[key][k]) {
                        old_states[key][k] = states[key][k];
                        const ids = key + '.' + k;
                        setObject(ids, states[key][k]);
                    }
                });
            }
        }
    });
    parse();
}

function setObject(name, val) {
    let type = 'string';
    let role = 'state';
    let write = false;
    const _name = name.slice(name.lastIndexOf('.') + 1);
    const obj = name.slice(0, name.lastIndexOf('.'));
    //adapter.log.debug('setObject ' + JSON.stringify(name));
    adapter.getObject(name, (err, state) => {
        if ((err || !state)) {
            if (name.includes('disabled') || name.includes('blocked')){
                type = 'boolean';
                write = true;
            } else {
                role = 'indicator';
            }

            adapter.setObjectNotExists(obj, {
                type:   'channel',
                common: {name: '', type: 'state'},
                native: {}
            }, () => {
                adapter.setObject(name, {
                    type:   'state',
                    common: {
                        name:  _name,
                        desc:  _name,
                        type,
                        role,
                        read:  true,
                        write: write
                    },
                    native: {}
                }, () => {
                    updateChannel(obj, _name, val);
                    adapter.setState(name, {val: val, ack: true});
                });
            });
        } else {
            updateChannel(obj, _name, val);
            adapter.setState(name, {val: val, ack: true});
        }
    });
}

function updateChannel(obj, name, val) {
    if (name === 'comment') {
        adapter.getObject(obj, (err, state) => {
            if (!err && state !== null) {
                if (state.common && (state.common.name !== val)) {
                    adapter.extendObject(obj, {common: {name: val, type: 'state'}});
                }
            }
        });
    }
}

function getNameWiFi(mac, cb) {
    let res = mac;
    let n = 0;
    states.dhcp.forEach((item, i) => {
        if (states.dhcp[i]['mac-address'] === mac) {
            res = states.dhcp[i]['name'];
        }
        n++;
        if (n === states.dhcp.length) {
            cb(res);
        }
    });
}

function err(e, er) {
    if (e) {
        e = e.toString();
        if (connect) {
            adapter.log.error('Oops: ' + e);
        }
        if (e.includes('cannot log in')) {
            adapter.log.error(`Error: ${e}. Incorrect username or password`);
        }
        if (e.includes('ECONNRESET') || e.includes('closed') || e.includes('ended') || e.includes('Timeout') && !er) {
            connection.close();
            flagOnError = false;
            clearTimeout(_poll);
            clearTimeout(timer);
            connect = false;
            _poll = null;
            adapter.log.error('Error socket: Reconnect after 15 sec...');
            adapter.setState('info.connection', false, true);
            timer = setTimeout(() => {
                clearTimeout(timer);
                main();
            }, 15000);
        }
    }
}

if (module.parent) {
    module.exports = startAdapter;
} else {
    startAdapter();
}


File: /main.test.js
'use strict';

/**
 * This is a dummy TypeScript test file using chai and mocha
 *
 * It's automatically excluded from npm and its build output is excluded from both git and npm.
 * It is advised to test all your modules with accompanying *.test.js-files
 */

// tslint:disable:no-unused-expression

const { expect } = require('chai');
// import { functionToTest } from "./moduleToTest";

describe('module to test => function to test', () => {
    // initializing logic
    const expected = 5;

    it(`should return ${expected}`, () => {
        const result = 5;
        // assign result a value from functionToTest
        expect(result).to.equal(expected);
        // or using the should() syntax
        result.should.equal(expected);
    });
    // ... more tests => it

});

// ... more test suites => describe


File: /package-lock.json
{
  "name": "iobroker.mikrotik",
  "version": "1.2.1",
  "lockfileVersion": 2,
  "requires": true,
  "packages": {
    "": {
      "name": "iobroker.mikrotik",
      "version": "1.2.1",
      "license": "MIT",
      "dependencies": {
        "@iobroker/adapter-core": "^3.1.6",
        "mikronode-ng": "^1.0.11"
      },
      "devDependencies": {
        "@alcalzone/release-script": "^3.8.0",
        "@alcalzone/release-script-plugin-iobroker": "^3.7.2",
        "@alcalzone/release-script-plugin-license": "^3.7.0",
        "@alcalzone/release-script-plugin-manual-review": "^3.7.0",
        "@iobroker/adapter-dev": "^1.3.0",
        "@iobroker/testing": "^4.1.3",
        "@tsconfig/node14": "^14.1.0",
        "@types/chai": "^4.3.16",
        "@types/chai-as-promised": "^7.1.8",
        "@types/mocha": "^10.0.8",
        "@types/node": "^20.14.12",
        "@types/proxyquire": "^1.3.31",
        "@types/sinon": "^17.0.3",
        "@types/sinon-chai": "^3.2.12",
        "chai": "^4.5.0",
        "chai-as-promised": "^7.1.2",
        "eslint": "^8.57.0",
        "eslint-config-prettier": "^9.1.0",
        "eslint-plugin-prettier": "^5.2.3",
        "mocha": "^10.7.3",
        "prettier": "^3.4.2",
        "proxyquire": "^2.1.3",
        "sinon": "^18.0.0",
        "sinon-chai": "^3.7.0",
        "typescript": "~5.7.3"
      },
      "engines": {
        "node": ">=18"
      }
    },
File: /package.json
{
  "name": "iobroker.mikrotik",
  "version": "1.2.1",
  "description": "MikroTik Router Adapter",
  "author": {
    "name": "instalator",
    "email": "vvvalt@mail.ru"
  },
  "contributors": [
    {
      "name": "instalator",
      "email": "vvvalt@mail.ru"
    }
  ],
  "homepage": "https://github.com/iobroker-community-adapters/iobroker.mikrotik",
  "license": "MIT",
  "keywords": [
    "ioBroker",
    "mikrotik"
  ],
  "repository": {
    "type": "git",
    "url": "https://github.com/iobroker-community-adapters/ioBroker.mikrotik.git"
  },
  "engines": {
    "node": ">=18"
  },
  "dependencies": {
    "@iobroker/adapter-core": "^3.1.6",
    "mikronode-ng": "^1.0.11"
  },
  "devDependencies": {
    "@alcalzone/release-script": "^3.8.0",
    "@alcalzone/release-script-plugin-iobroker": "^3.7.2",
    "@alcalzone/release-script-plugin-license": "^3.7.0",
    "@alcalzone/release-script-plugin-manual-review": "^3.7.0",
    "@iobroker/adapter-dev": "^1.3.0",
    "@iobroker/testing": "^4.1.3",
    "@tsconfig/node14": "^14.1.0",
    "@types/chai": "^4.3.16",
    "@types/chai-as-promised": "^7.1.8",
    "@types/mocha": "^10.0.8",
    "@types/node": "^20.14.12",
    "@types/proxyquire": "^1.3.31",
    "@types/sinon": "^17.0.3",
    "@types/sinon-chai": "^3.2.12",
    "chai": "^4.5.0",
    "chai-as-promised": "^7.1.2",
    "eslint": "^8.57.0",
    "eslint-config-prettier": "^9.1.0",
    "eslint-plugin-prettier": "^5.2.3",
    "mocha": "^10.7.3",
    "prettier": "^3.4.2",
    "proxyquire": "^2.1.3",
    "sinon": "^18.0.0",
    "sinon-chai": "^3.7.0",
    "typescript": "~5.7.3"
  },
  "main": "main.js",
  "files": [
    "admin/",
    "lib/",
    "main.js",
    "io-package.json",
    "docs/",
    "LICENSE"
  ],
  "scripts": {
    "test:js": "mocha --config test/mocharc.custom.json \"{!(node_modules|test)/**/*.test.js,*.test.js,test/**/test!(PackageFiles|Startup).js}\"",
    "test:package": "mocha test/package --exit",
    "test:integration": "mocha test/integration --exit",
    "test": "npm run test:js && npm run test:package",
    "check": "tsc --noEmit -p tsconfig.check.json",
    "lint": "eslint",
    "translate": "translate-adapter",
    "release": "release-script"
  },
  "bugs": {
    "url": "https://github.com/iobroker-community-adapters/iobroker.mikrotik/issues"
  },
  "readmeFilename": "README.md"
}


File: /README.md
![Logo](admin/mikrotik_admin.png)
ioBroker MikroTik Router adapter
=================
![Number of Installations](http://iobroker.live/badges/mikrotik-installed.svg)
![Number of Installations](http://iobroker.live/badges/mikrotik-stable.svg)
[![NPM version](http://img.shields.io/npm/v/iobroker.mikrotik.svg)](https://www.npmjs.com/package/iobroker.mikrotik)
[![Downloads](https://img.shields.io/npm/dm/iobroker.mikrotik.svg)](https://www.npmjs.com/package/iobroker.mikrotik)
[![Tests](https://github.com/instalator/iobroker.mikrotik/workflows/Test%20and%20Release/badge.svg)](https://github.com/instalator/ioBroker.mikrotik/actions/) 

[![NPM](https://nodei.co/npm/iobroker.mikrotik.png?downloads=true)](https://nodei.co/npm/iobroker.mikrotik/)

[![Donate](https://img.shields.io/badge/Donate-YooMoney-green)](https://sobe.ru/na/instalator)
[![Donate](https://img.shields.io/badge/Donate-PayPal-green.svg)](https://www.paypal.com/cgi-bin/webscr?cmd=_s-xclick&hosted_button_id=PFUALWTR2CTPY)

## Using
### add_firewall
Add address to firewall list and enable.  
e.g. `name,127.0.0.1,comment`.
### raw
Send api command to mikrotik, the result of execution will be received in the `mikrotik.0.commands.response` object
e.g.:  
 `/ip/firewall/address-list/add\n=list=2vpn\n=address=195.82.146.0/24\n=comment=rutracker.org`. OR
 `ip/firewall/address-list/add list=FuckRKN address=195.82.146.0/24 comment=rutracker.org`   
 `ip/kid-control/print`   
 `ip/kid-control/pause .id=*1`
 `ip/kid-control/resume .id=*1`
### reboot, shutdown
Reboot/shutdown mikrotik
### usb_reset
Reset power USB in mikrotik


*The created objects are not deleted automatically when deleted in the router.*

## Changelog
<!--
	Placeholder for the next version (at the beginning of the line):
	### **WORK IN PROGRESS**
-->
### 1.2.1 (2024-07-25)
* (mcm1957) Default value for commands.add_firewall has been corrected [#138]
* (mcm1957) Some issues reported by adapter-checker have been fixed
* (mcm1957) Testing for node.js 22 has been added
* (mcm1957) Dependencies have been updated

### 1.2.0 (2024-04-20)
- (mcm1957) Adapter requires node.js >= 18 and js-controller >= 5 now
- (mcm1957) Dependencies have been updated

### 1.1.1 (2022-10-17)
* (bluefox) Packages updated

### 1.0.16
* (instalator) changed parse RAW

### 1.0.14
* (instalator) added CAPsMAN [issues#28](https://github.com/instalator/ioBroker.mikrotik/issues/33)

### 1.0.13
* (instalator) changed parse RAW command
* (instalator) added last-link-up-time and last-link-down-time to interface
* (instalator) added [issues#28](https://github.com/instalator/ioBroker.mikrotik/issues/31)

### 1.0.12
* (instalator) fixed error symb

### 1.0.11
* (instalator) fixed [issues#28](https://github.com/instalator/ioBroker.mikrotik/issues/28)

### 1.0.10
* (instalator) added name object
* (instalator) fix error

### 1.0.6
* (instalator) added in interface RX/TX (packets) [issues#20](https://github.com/instalator/ioBroker.mikrotik/issues/20)
* (instalator) Added Support for Compact mode
* (instalator) Refactoring

### 1.0.5
* (instalator) Update Login Protocol [issues#23](https://github.com/instalator/ioBroker.mikrotik/issues/23)

### 1.0.4
* (instalator) fix add_firewall command [issues#18](https://github.com/instalator/ioBroker.mikrotik/issues/18#issue-358331248)

### 1.0.3
* (instalator) added checkboxes - receive the following data

### 1.0.2
* (bondrogeen) added support for the Admin 3
* (instalator) fixed some bugs
* (instalator) added in settings time polling

### 1.0.1
* (instalator) Change in objects symbol "*" to "_", see [issues#10](https://github.com/instalator/ioBroker.mikrotik/issues/10)
* (instalator) fix [issues#9](https://github.com/instalator/ioBroker.mikrotik/issues/9)
* (instalator) add to settings Timeout get
* (instalator) add firewall list [issues#7](https://github.com/instalator/ioBroker.mikrotik/issues/7) and command 'add_firewall' e.g. "name,127.0.0.1,comment"

### 1.0.0
* (instalator) up to stable

### 0.0.20
* (instalator) add mask for password in settings dialog
* (instalator) added info error login or password

### 0.0.12
* (instalator) change logic connect

### 0.0.11
* (instalator) added WAN address to systeminfo

### 0.0.10
* (instalator) change logo
* (instalator) fix error

### 0.0.4
* (instalator) added commands usb power reset
* (instalator) fix error

### 0.0.2
* (instalator) added command 'disabled ' for: filter, interface, filter nat.
* (instalator) fix error
* (instalator) added list dhcp and Wi-Fi client

### 0.0.1
* (instalator) initial version

## License

The MIT License (MIT)

Copyright (c) 2024 iobroker-community-adapters <iobroker-community-adapters@gmx.de>
Copyright (c) 2021-2022 instalator <vvvalt@mail.ru>

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.


File: /test\integration.js
const path = require('path');
const { tests } = require('@iobroker/testing');

// Run integration tests - See https://github.com/ioBroker/testing for a detailed explanation and further options
tests.integration(path.join(__dirname, '..'));


File: /test\mocha.setup.js
// Don't silently swallow unhandled rejections
process.on('unhandledRejection', (e) => {
    throw e;
});

// enable the should interface with sinon
// and load chai-as-promised and sinon-chai by default
const sinonChai = require('sinon-chai');
const chaiAsPromised = require('chai-as-promised');
const { should, use } = require('chai');

should();
use(sinonChai);
use(chaiAsPromised);


File: /test\mocharc.custom.json
{
    "require": ["test/mocha.setup.js"],
    "watch-files": ["!(node_modules|test)/**/*.test.js", "*.test.js", "test/**/test!(PackageFiles|Startup).js"]
}


File: /test\package.js
const path = require('path');
const { tests } = require('@iobroker/testing');

// Validate the package files
tests.packageFiles(path.join(__dirname, '..'));


File: /test\tsconfig.json
{
    "extends": "../tsconfig.json",
    "compilerOptions": {
        "noImplicitAny": false
    },
    "include": ["./**/*.js"]
}


File: /tsconfig.json
{
    "compileOnSave": true,
    "compilerOptions": {
        // do not compile anything, this file is just to configure type checking
        "noEmit": true,

        // check JS files
        "allowJs": true,
        "checkJs": true,

        "module": "commonjs",
        "moduleResolution": "node",
        // this is necessary for the automatic typing of the adapter config
        "resolveJsonModule": true,

        // Set this to false if you want to disable the very strict rules (not recommended)
        "strict": true,
        // Or enable some of those features for more fine-grained control
        // "strictNullChecks": true,
        // "strictPropertyInitialization": true,
        // "strictBindCallApply": true,
        "noImplicitAny": false,
        // "noUnusedLocals": true,
        // "noUnusedParameters": true,

        // Consider targetting es2017 or higher if you require the new NodeJS 8+ features
        "target": "es2015",

    },
    "include": [
        "**/*.js",
        "**/*.d.ts"
    ],
    "exclude": [