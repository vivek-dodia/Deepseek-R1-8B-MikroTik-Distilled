# Repository Information
Name: Open-Hotspot-Manger-for-Mikrotik

# Directory Structure
Directory structure:
└── github_repos/Open-Hotspot-Manger-for-Mikrotik/
    ├── .env.example
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
    │   │       ├── pack-683255e086a589ebc605a12f9c2c574adf15ded6.idx
    │   │       └── pack-683255e086a589ebc605a12f9c2c574adf15ded6.pack
    │   ├── packed-refs
    │   └── refs/
    │       ├── heads/
    │       │   └── master
    │       ├── remotes/
    │       │   └── origin/
    │       │       └── HEAD
    │       └── tags/
    ├── .gitattributes
    ├── .gitignore
    ├── app/
    │   ├── Console/
    │   │   ├── Commands/
    │   │   │   └── Inspire.php
    │   │   └── Kernel.php
    │   ├── Events/
    │   │   └── Event.php
    │   ├── Exceptions/
    │   │   └── Handler.php
    │   ├── Http/
    │   │   ├── Controllers/
    │   │   │   ├── Auth/
    │   │   │   │   ├── AuthController.php
    │   │   │   │   └── PasswordController.php
    │   │   │   ├── Controller.php
    │   │   │   ├── HomeController.php
    │   │   │   ├── MikrotikController.php
    │   │   │   ├── RouterController.php
    │   │   │   └── UserController.php
    │   │   ├── Kernel.php
    │   │   ├── Middleware/
    │   │   │   ├── Authenticate.php
    │   │   │   ├── EncryptCookies.php
    │   │   │   ├── RedirectIfAuthenticated.php
    │   │   │   └── VerifyCsrfToken.php
    │   │   ├── Requests/
    │   │   │   └── Request.php
    │   │   └── routes.php
    │   ├── Jobs/
    │   │   └── Job.php
    │   ├── Listeners/
    │   │   └── .gitkeep
    │   ├── Mikrotik.php
    │   ├── Policies/
    │   │   └── .gitkeep
    │   ├── Providers/
    │   │   ├── AppServiceProvider.php
    │   │   ├── AuthServiceProvider.php
    │   │   ├── EventServiceProvider.php
    │   │   └── RouteServiceProvider.php
    │   └── User.php
    ├── artisan
    ├── bootstrap/
    │   ├── app.php
    │   ├── autoload.php
    │   └── cache/
    │       └── .gitignore
    ├── composer.json
    ├── composer.lock
    ├── config/
    │   ├── app.php
    │   ├── auth.php
    │   ├── broadcasting.php
    │   ├── cache.php
    │   ├── compile.php
    │   ├── database.php
    │   ├── filesystems.php
    │   ├── mail.php
    │   ├── queue.php
    │   ├── services.php
    │   ├── session.php
    │   └── view.php
    ├── database/
    │   ├── .gitignore
    │   ├── factories/
    │   │   └── ModelFactory.php
    │   ├── migrations/
    │   │   ├── .gitkeep
    │   │   ├── 2014_10_12_000000_create_users_table.php
    │   │   ├── 2014_10_12_100000_create_password_resets_table.php
    │   │   ├── 2016_04_14_031423_create_mikrotiks_table.php
    │   │   └── 2016_04_15_063918_add_port_to_router.php
    │   └── seeds/
    │       ├── .gitkeep
    │       └── DatabaseSeeder.php
    ├── gulpfile.js
    ├── laravel.md
    ├── package.json
    ├── phpunit.xml
    ├── public/
    │   ├── .htaccess
    │   ├── index.php
    │   ├── robots.txt
    │   └── web.config
    ├── readme.md
    ├── resources/
    │   ├── assets/
    │   │   └── sass/
    │   │       └── app.scss
    │   ├── lang/
    │   │   └── en/
    │   │       ├── auth.php
    │   │       ├── cocomas.php
    │   │       ├── pagination.php
    │   │       ├── passwords.php
    │   │       └── validation.php
    │   └── views/
    │       ├── app/
    │       │   ├── active/
    │       │   │   └── index.blade.php
    │       │   ├── binding/
    │       │   │   ├── create.blade.php
    │       │   │   ├── edit.blade.php
    │       │   │   └── index.blade.php
    │       │   └── user/
    │       │       ├── create.blade.php
    │       │       ├── edit.blade.php
    │       │       └── index.blade.php
    │       ├── auth/
    │       │   ├── emails/
    │       │   │   └── password.blade.php
    │       │   ├── login.blade.php
    │       │   ├── passwords/
    │       │   │   ├── email.blade.php
    │       │   │   └── reset.blade.php
    │       │   └── register.blade.php
    │       ├── errors/
    │       │   └── 503.blade.php
    │       ├── flash.blade.php
    │       ├── home.blade.php
    │       ├── layouts/
    │       │   └── app.blade.php
    │       ├── main-page.blade.php
    │       ├── router/
    │       │   └── mikrotik/
    │       │       └── edit.blade.php
    │       ├── sidemenu.blade.php
    │       ├── user/
    │       │   ├── create.blade.php
    │       │   └── profile.blade.php
    │       ├── vendor/
    │       │   └── .gitkeep
    │       └── welcome.blade.php
    ├── server.php
    ├── storage/
    │   ├── app/
    │   │   ├── .gitignore
    │   │   └── public/
    │   │       └── .gitignore
    │   ├── framework/
    │   │   ├── .gitignore
    │   │   ├── cache/
    │   │   │   └── .gitignore
    │   │   ├── sessions/
    │   │   │   └── .gitignore
    │   │   └── views/
    │   │       └── .gitignore
    │   └── logs/
    │       └── .gitignore
    └── tests/
        ├── ExampleTest.php
        └── TestCase.php


# Content
File: /.env.example
APP_ENV=local
APP_DEBUG=true
APP_KEY=SomeRandomString
APP_URL=http://localhost

DB_CONNECTION=mysql
DB_HOST=127.0.0.1
DB_PORT=3306
DB_DATABASE=homestead
DB_USERNAME=homestead
DB_PASSWORD=secret

CACHE_DRIVER=file
SESSION_DRIVER=file
QUEUE_DRIVER=sync

REDIS_HOST=127.0.0.1
REDIS_PASSWORD=null
REDIS_PORT=6379

MAIL_DRIVER=smtp
MAIL_HOST=mailtrap.io
MAIL_PORT=2525
MAIL_USERNAME=null
MAIL_PASSWORD=null
MAIL_ENCRYPTION=null


File: /.git\config
[core]
	repositoryformatversion = 0
	filemode = false
	bare = false
	logallrefupdates = true
	symlinks = false
	ignorecase = true
[remote "origin"]
	url = https://github.com/bleeloe/Open-Hotspot-Manger-for-Mikrotik.git
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
0000000000000000000000000000000000000000 d06e275e88037c94b54eeb8fc9bfca456f8da803 vivek-dodia <vivek.dodia@icloud.com> 1738606023 -0500	clone: from https://github.com/bleeloe/Open-Hotspot-Manger-for-Mikrotik.git


File: /.git\logs\refs\heads\master
0000000000000000000000000000000000000000 d06e275e88037c94b54eeb8fc9bfca456f8da803 vivek-dodia <vivek.dodia@icloud.com> 1738606023 -0500	clone: from https://github.com/bleeloe/Open-Hotspot-Manger-for-Mikrotik.git


File: /.git\logs\refs\remotes\origin\HEAD
0000000000000000000000000000000000000000 d06e275e88037c94b54eeb8fc9bfca456f8da803 vivek-dodia <vivek.dodia@icloud.com> 1738606023 -0500	clone: from https://github.com/bleeloe/Open-Hotspot-Manger-for-Mikrotik.git


File: /.git\packed-refs
# pack-refs with: peeled fully-peeled sorted 
4ce9060a4404d037b60b8820aaa8da49a3f25c54 refs/remotes/origin/develop
d06e275e88037c94b54eeb8fc9bfca456f8da803 refs/remotes/origin/master


File: /.git\refs\heads\master
d06e275e88037c94b54eeb8fc9bfca456f8da803


File: /.git\refs\remotes\origin\HEAD
ref: refs/remotes/origin/master


File: /.gitattributes
* text=auto
*.css linguist-vendored
*.less linguist-vendored


File: /.gitignore
/vendor
/node_modules
/public/storage
/.git
Homestead.yaml
Homestead.json
.env


File: /app\Console\Commands\Inspire.php
<?php

namespace App\Console\Commands;

use Illuminate\Console\Command;
use Illuminate\Foundation\Inspiring;

class Inspire extends Command
{
    /**
     * The name and signature of the console command.
     *
     * @var string
     */
    protected $signature = 'inspire';

    /**
     * The console command description.
     *
     * @var string
     */
    protected $description = 'Display an inspiring quote';

    /**
     * Execute the console command.
     *
     * @return mixed
     */
    public function handle()
    {
        $this->comment(PHP_EOL.Inspiring::quote().PHP_EOL);
    }
}


File: /app\Console\Kernel.php
<?php

namespace App\Console;

use Illuminate\Console\Scheduling\Schedule;
use Illuminate\Foundation\Console\Kernel as ConsoleKernel;

class Kernel extends ConsoleKernel
{
    /**
     * The Artisan commands provided by your application.
     *
     * @var array
     */
    protected $commands = [
        // Commands\Inspire::class,
    ];

    /**
     * Define the application's command schedule.
     *
     * @param  \Illuminate\Console\Scheduling\Schedule  $schedule
     * @return void
     */
    protected function schedule(Schedule $schedule)
    {
        // $schedule->command('inspire')
        //          ->hourly();
    }
}


File: /app\Events\Event.php
<?php

namespace App\Events;

abstract class Event
{
    //
}


File: /app\Exceptions\Handler.php
<?php

namespace App\Exceptions;

use Exception;
use Illuminate\Validation\ValidationException;
use Illuminate\Auth\Access\AuthorizationException;
use Illuminate\Database\Eloquent\ModelNotFoundException;
use Symfony\Component\HttpKernel\Exception\HttpException;
use Illuminate\Foundation\Exceptions\Handler as ExceptionHandler;

class Handler extends ExceptionHandler
{
    /**
     * A list of the exception types that should not be reported.
     *
     * @var array
     */
    protected $dontReport = [
        AuthorizationException::class,
        HttpException::class,
        ModelNotFoundException::class,
        ValidationException::class,
    ];

    /**
     * Report or log an exception.
     *
     * This is a great spot to send exceptions to Sentry, Bugsnag, etc.
     *
     * @param  \Exception  $e
     * @return void
     */
    public function report(Exception $e)
    {
        parent::report($e);
    }

    /**
     * Render an exception into an HTTP response.
     *
     * @param  \Illuminate\Http\Request  $request
     * @param  \Exception  $e
     * @return \Illuminate\Http\Response
     */
    public function render($request, Exception $e)
    {
        return parent::render($request, $e);
    }
}


File: /app\Http\Controllers\Auth\AuthController.php
<?php

namespace App\Http\Controllers\Auth;

use App\User;
use Validator;
use App\Http\Controllers\Controller;
use Illuminate\Foundation\Auth\ThrottlesLogins;
use Illuminate\Foundation\Auth\AuthenticatesAndRegistersUsers;

class AuthController extends Controller
{
    /*
    |--------------------------------------------------------------------------
    | Registration & Login Controller
    |--------------------------------------------------------------------------
    |
    | This controller handles the registration of new users, as well as the
    | authentication of existing users. By default, this controller uses
    | a simple trait to add these behaviors. Why don't you explore it?
    |
    */

    use AuthenticatesAndRegistersUsers, ThrottlesLogins;

    /**
     * Where to redirect users after login / registration.
     *
     * @var string
     */
    protected $redirectTo = '/home';

    /**
     * Create a new authentication controller instance.
     *
     * @return void
     */
    public function __construct()
    {
        $this->middleware($this->guestMiddleware(), ['except' => 'logout']);
    }

    /**
     * Get a validator for an incoming registration request.
     *
     * @param  array  $data
     * @return \Illuminate\Contracts\Validation\Validator
     */
    protected function validator(array $data)
    {
        return Validator::make($data, [
            'name' => 'required|max:255',
            'email' => 'required|email|max:255|unique:users',
            'password' => 'required|min:6|confirmed',
        ]);
    }

    /**
     * Create a new user instance after a valid registration.
     *
     * @param  array  $data
     * @return User
     */
    protected function create(array $data)
    {
        return User::create([
            'name' => $data['name'],
            'email' => $data['email'],
            'password' => bcrypt($data['password']),
        ]);
    }
}


File: /app\Http\Controllers\Auth\PasswordController.php
<?php

namespace App\Http\Controllers\Auth;

use App\Http\Controllers\Controller;
use Illuminate\Foundation\Auth\ResetsPasswords;

class PasswordController extends Controller
{
    /*
    |--------------------------------------------------------------------------
    | Password Reset Controller
    |--------------------------------------------------------------------------
    |
    | This controller is responsible for handling password reset requests
    | and uses a simple trait to include this behavior. You're free to
    | explore this trait and override any methods you wish to tweak.
    |
    */

    use ResetsPasswords;

    /**
     * Create a new password controller instance.
     *
     * @return void
     */
    public function __construct()
    {
        $this->middleware('guest');
    }
}


File: /app\Http\Controllers\Controller.php
<?php

namespace App\Http\Controllers;

use Illuminate\Foundation\Bus\DispatchesJobs;
use Illuminate\Routing\Controller as BaseController;
use Illuminate\Foundation\Validation\ValidatesRequests;
use Illuminate\Foundation\Auth\Access\AuthorizesRequests;
use Illuminate\Foundation\Auth\Access\AuthorizesResources;

class Controller extends BaseController
{
    use AuthorizesRequests, AuthorizesResources, DispatchesJobs, ValidatesRequests;
}


File: /app\Http\Controllers\HomeController.php
<?php

namespace App\Http\Controllers;

use App\Http\Requests;
use Illuminate\Http\Request;


class HomeController extends Controller
{
    /**
     * Create a new controller instance.
     *
     * @return void
     */
    public function __construct()
    {
        // $this->middleware('auth');
    }

    /**
     * Show the application dashboard.
     *
     * @return \Illuminate\Http\Response
     */
    public function index()
    {
        return view('home');
    }


    /**
     * undocumented function
     *
     * @return void
     * @author 
     **/
    public function user()
    {
        return view('app.user.index',[]);
    }

    /**
     * User Active
     *
     * @return void
     * @author 
     **/
    public function userActive()
    {
        return view('app.active.index',[]);
    }

    /**
     * List ip binding
     *
     * @return void
     * @author 
     **/
    public function IpBinding()
    {
        return view('app.binding.index',[]);
    }


    /**
     * create function
     *
     * @return void
     * @author 
     **/
    public function createIpBinding()
    {
        return view('app.binding.create',[]);   
    }


    /**
     * undocumented function
     *
     * @return void
     * @author 
     **/
    public function editIpBinding(Request $request,$id)
    {
        $router = new MikrotikController();

        $data = $router->routerPrint('/ip/hotspot/ip-binding/print',[
            'numbers' => '.id',
            'macaddress' => 'mac-address',
            'address' => 'address',
            'toaddress' => 'to-address',
            'server' => 'server',            
            'disabled' => 'disabled',
            'type' => 'type',            
            'where' => 'where',            
            'comment' => 'comment',
        ],$id);        
        return view('app.binding.edit',$data[0]);
    }

    /**
     * undocumented function
     *
     * @return void
     * @author 
     **/
    public function editIpBindingSave(Request $request,$id)
    {        
        $router = new MikrotikController();

        $action = $router->routerAction('/ip/hotspot/ip-binding/set',[
            'numbers' => $id,
            'mac-address' => $request->input('ma-caddress'),
            'address' => $request->input('address'),
            'to-address' => $request->input('to-address'),
            'server' => $request->input('server'),
            'disabled' => $request->input('disabled'),
            'type' => $request->input('type'),
            'where' => $request->input('where'),
            'comment' => $request->input('comment'),
        ],$id);        
        if ($action) {
            return redirect("/binding/$id/edit")->with('message','Saved');
        }
        return redirect("/binding/$id/edit")->with('message','Failed');
    }


    /**
     * Form Create User
     *
     * @return void
     * @author 
     **/
    public function createUser()
    {
        return view('app.user.create',[]);

    }


    /**
     * Edit User
     *
     * @return void
     * @author harylalamentik@gmail.com
     **/
    public function editUser(Request $request,$id)
    {

        $router = new MikrotikController();

        $data = $router->routerPrint('/ip/hotspot/user/print',[
            'numbers' => '.id',
            'disabled' => 'disabled',
            'name' => 'name',
            // 'password' => 'password',
            'email' => 'email',
            'profile' => 'profile',
            'server' => 'server',
            'bytesIn' => 'bytes-in',
            'bytesOut' => 'bytes-out',
            'address' => 'address',
            'comment' => 'comment',
            'limitBytesIn' => 'limit-bytes-in',                    
            'limitBytesOut' => 'limit-bytes-out',                    
            'limitBytesTotal' => 'limit-bytes-total',
            'limitUptime' => 'limit-uptime',
            'packetsIn' => 'packets-in',
            'packetsOut' => 'packets-out',
            'macAddress' => 'mac-caddress',
            'routes' => 'routes'
        ],$id);        
        return view('app.user.edit',$data[0]);
    }
    /**
     * undocumented function
     *
     * @return void
     * @author 
     **/
    public function editUserSave(Request $request,$id)
    {                
        $router = new MikrotikController();
        $action = $router->routerAction('/ip/hotspot/user/set',[
            'numbers' => $id,
            'disabled' => $request->input('disabled'),
            'name' => $request->input('name'),
            'password' => $request->input('password'),
            'email' => $request->input('email'),
            'profile' => $request->input('profile'),
            'server' => $request->input('server'),
            'bytes-in' => $request->input('bytesin'),
            'bytes-out' => $request->input('bytesout'),
            'address' => $request->input('address'),
            'comment' => $request->input('comment'),
            'limit-bytes-in' => $request->input('limitbytesin'),
            'limit-bytes-out' => $request->input('limitbytesout'),
            'limit-bytes-total' => $request->input('limitbytestotal'),
            'limit-uptime' => $request->input('limituptime'),
            'packets-in' => $request->input('packetsin'),
            'packets-out' => $request->input('packetsout'),
            'mac-address' => $request->input('maccaddress'),
            'routes' => $request->input('route')
        ]);

        if ($action) {
            return redirect("/user/$id/edit")->with('message','Saved');
        }
        return redirect("/user/$id/edit")->with('message','Failed');
    }

}


File: /app\Http\Controllers\MikrotikController.php
<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use \PEAR2\Net\RouterOS as RouterOS;
use App\Http\Requests;

class MikrotikController extends Controller
{

    protected $client;

    /**
     * construct
     *
     * @return void
     * @author 
     **/
    public function __construct()
    {

        $this->connection();
        
    }


    /**
     * Connection to router
     *
     * @return void
     * @author 
     **/
    protected function connection()
    {
        $mikrotik = \App\Mikrotik::find(1);                    

        try {
            $this->client = new RouterOS\Client($mikrotik->ipaddress, $mikrotik->user,\Crypt::
                decrypt($mikrotik->pass),$mikrotik->port);            
        } catch (\Exception $e) {
            print "Error connecting to RouterOS";    
        }
    }

    /**
     * Router Command
     *
     * @return void
     * @author 
     **/
    public function routerCommand(Request $request)
    {

        $request->header('Content-Type','text/plain');
        $util = new RouterOS\Util( $this->client );
        $util->changeMenu('/ip hotspot user');        
        echo $util->get(0, 'name');
        // foreach ($util->getAll() as $item) {
        //     echo 'IP: ', $item->getProperty('address'),
        //          ' MAC: ', $item->getProperty('mac-address'),
        //          "\n";
        // }
    }




    /**
     * Command print function
     *
     * @return void
     * @author 
     **/
    public function routerPrint($pathMenu=null, $argumentProperty = array(),$numbers = NULL)
    {   
        if (is_null($pathMenu)) {
            return null;
        }

        $client = $this->client;
        $request = new RouterOS\Request($pathMenu);
        if (!is_null($numbers)) {
            $request->setQuery(RouterOS\Query::where('.id', $numbers));
        }        
        $responses = $client->sendSync($request);
        $result  = array();
        foreach ($responses as $response) {
            if ($response->getType() === RouterOS\Response::TYPE_DATA) {                
                $field = array();
                foreach ($argumentProperty as $key => $value) {
                    $field[$key] = $response->getArgument($value);
                }
                array_push($result, $field);
            }
        }
        return ($result);
    }



    /**
     * Router Action
     * 
     * @return void
     * @author harylalamentik@gmail.com
     **/    
    public function routerAction($path, $setArgument = array())
    {                
        $routerRequest = new RouterOS\Request($path);           
        if (count($setArgument)) {
            foreach ($setArgument as $key => $value) {
                if (!empty($value)) {
                    $routerRequest->setArgument($key,$value);                
                }                
            }        
        }
        if ($this->client->sendSync($routerRequest)->getType() !== RouterOS\Response::TYPE_FINAL) {
            return FALSE;
        }        
        return TRUE;
    } 


    /**
     * Http remove user active hotspot 
     *
     * @return void
     * @author 
     **/
    public function hotspotKillActive(Request $request,$id)
    {
        if ($this->routerAction('/ip/hotspot/active/remove',['numbers'=>$id])) {
            return redirect('/user/active')->with('message','Removed');    
        }
        return redirect('/user/active')->with('message-error','Failed');

    }




    /**
     * Create User
     *
     * @return void
     * @author 
     **/
    public function createUser(Request $request)
    {

        $action = $this->routerAction('/ip/hotspot/user/add',[
            'server'=> $request->input('server'),
            'name'=> $request->input('name'),
            'password'=> $request->input('password'),
            'profile'=> $request->input('profile'),     
            'email'=> $request->input('email'),     
            'comment'=> $request->input('comment'),     
        ]);
        if ($action) {
            return redirect('/user/create')->with('message','Created');
        }
        return redirect('/user/create')->with('message-error','Failed');
    }


    /**
     * Remove hotspot user
     *
     * @return void
     * @author 
     **/
    public function removeUser(Request $request,$id)
    {        
        if ($this->routerAction('/ip/hotspot/user/remove',['numbers'=>$id])) {
            return redirect('/user')->with('message','Removed');    
        }
        return redirect('/user')->with('message-error','Failed');
    }

    /**
     * undocumented function
     *
     * @return void
     * @author 
     **/
    public function removeIpBinding(Request $request,$id)
    {
        if ($this->routerAction('/ip/hotspot/ip-binding/remove',['numbers'=>$id])) {
            return redirect('/binding')->with('message','Removed');    
        }
        return redirect('/binding')->with('message-error','Failed');
    }


    /**
     * Server Profiles
     *
     * @return void
     * @author 
     **/
    public function ServerProfile()
    {
        return $this->routerPrint('/ip/hotspot/profile/print',[
            'numbers' => '.id',
            'name' => 'name',
            'hotspot-address' => 'hotspot-address',
            'dns-name' => 'dns-name',
            'html-directory' => 'html-directory',
            'http-proxy' => 'http-proxy',
            'smtp-server' => 'smtp-server',
            'login-by' => 'login-by',
            'split-user-domain' => 'split-user-domain',                    
        ]);
    }


    /**
     * undocumented function
     *
     * @return void
     * @author 
     **/
    public function IpBinding(Request $request)
    {
        return $this->routerPrint('/ip/hotspot/ip-binding/print',[
            'numbers' => '.id',
            'mac-address' => 'mac-address',
            'address' => 'address',
            'to-address' => 'to-address',
            'server' => 'server',            
            'blocked' => 'blocked',            
            'bypassed' => 'bypassed',            
            'disabled' => 'disabled',            
            'type' => 'type',            
            'where' => 'where',            
            'comment' => 'comment',
        ]);
    }



    /**
     * undocumented function
     *
     * @return void
     * @author 
     **/
    public function createIpBinding(Request $request)
    {
        
        $action = $this->routerAction('/ip/hotspot/ip-binding/add',[        
            'mac-address'=> $request->input('mac-address'),            
            'comment'=> $request->input('comment'),     
            'address'=> $request->input('address'),     
            'to-address'=> $request->input('to-address'),     
            'type'=> $request->input('type'),     
            'email'=> $request->input('email'),     
            'server'=> $request->input('server'),
        ]);

        if ($action) {
            return redirect('/binding/create')->with('message','Created');
        }
        return redirect('/binding/create')->with('message-error','Failed');
    }



    /**
     * Display list user profile
     *
     * @return void
     * @author 
     **/
    public function UserProfile()
    {
        return $this->routerPrint('/ip/hotspot/user/profile/print',[
            'numbers' => '.id',
            'name' => 'name',
            'idle-itmeout' => 'idle-itmeout',
            'keepalive-timeout' => 'keepalive-timeout',
            'status-autorefresh' => 'status-autorefresh',
            'shared-users' => 'shared-users',
            'add-mac-cookie' => 'add-mac-cookie',
            'address-list' => 'address-list',
            'transparent-proxy' => 'transparent-proxy',
        ]);
    }



    /**
     * Show Hotspot User
     *
     * @return void
     * @author harylalamentik@gmail.com
     **/
    public function hsUsers(Request $request)
    {

        $request->header('Content-Type','application/json');

        return $this->routerPrint('/ip/hotspot/user/print',[
            'numbers' => '.id',
            'disabled' => 'disabled',
            'name' => 'name',
            // 'password' => 'password',
            'profile' => 'profile',
            'server' => 'server',
            'bytesIn' => 'bytes-in',
            'bytesOut' => 'bytes-out',
            'address' => 'address',
            'comment' => 'comment',
            'limitBytesIn' => 'limit-bytes-in',                    
            'limitBytesOut' => 'limit-bytes-out',                    
            'limitBytesTotal' => 'limit-bytes-total',
            'limitUptime' => 'limit-uptime',
            'packetsIn' => 'packets-in',
            'packetsOut' => 'packets-out',
            'macAddress' => 'mac-caddress',
            'routes' => 'routes',                    
        ]);    
    }


    /**
     * Show Hotspot Active User (online)
     *
     * @return void
     * @author harylalamentik@gmail.com
     **/
    public function hsActive(Request $request)
    {
        return $this->routerPrint('/ip/hotspot/active/print',[
            'numbers' => '.id',
            'radius' => 'radius',
            'server' => 'server',
            'user' => 'user',
            'ipaddress' => 'address',
            'uptime' => 'uptime',
            'loginBy' => 'login-by',
            'bytesIn' => 'bytes-in',
            'bytesOut' => 'bytes-out',
            'domain' => 'domain',
            'idleTime' => 'idle-time',
            'idleTimeout' => 'idle-timeout',
            'keepalive_timeout' => 'keepalive-timeout',
            'limitBytesIn' => 'limit-bytes-in',                    
            'limitBytesOut' => 'limit-bytes-out',                    
            'limitBytesTotal' => 'limit-bytes-total',
            'macAddress' => 'mac-address',
            'packetsIn' => 'packets-in',
            'packetsOut' => 'packets-out',
            'sessionTimeLeft' => 'session-time-left',
        ]);
    }
}


File: /app\Http\Controllers\RouterController.php
<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;

use App\Http\Requests;

class RouterController extends Controller
{
    /**
     * Show Router Config Form
     *
     * @return void
     * @author 
     **/
    public function edit(Request $Request)
    {    	    	
    	return view('router.mikrotik.edit',['data'=>\App\Mikrotik::find(1)]);
    }


    /**
     * Update Router Config
     *
     * @return void
     * @author 
     **/
    public function update(Request $request)
    {    		
        
    	$data = \App\Mikrotik::find(1);
        $data->name = $request->input('name');
    	$data->user = $request->input('user');
    	if ($request->has('pass')) {    		
    		$data->pass = \Crypt::encrypt($request->input('pass'));
    	}    	
        $data->ipaddress = $request->input('ipaddress');
    	$data->port = $request->input('port');
    	$data->is_active = $request->input('is_active');
    	$data->save();
    	return redirect('/router')->with('message','Saved');
    }

}


File: /app\Http\Controllers\UserController.php
<?php

namespace App\Http\Controllers;

use App\Http\Requests;
use Illuminate\Http\Request;
use Auth;

class UserController extends Controller
{


	/**
	 * Form Create User
	 *
	 * @return void
	 * @author 
	 **/
	public function create()
	{
		return view('user.create');
	}

	/**
	 * UserCreate
	 *
	 * @return void
	 * @author harylalamentik@gmail.com
	 **/
	public function store(Request $request)
	{		
		$data = new \App\User;
		$data->name = $request->input('name');
		$data->email = $request->input('email');
		$data->password = \Hash::make($request->input('password'));		
		$data->save();
		return redirect('/user/register')->with('message','Saved');
	}

	/**
	 * Display Profile
	 *
	 * @return void
	 * @author harylalamentik@gmail.com
	 **/
	public function profile(Request $request)
	{		
		return view('user.profile',['data' => \App\User::find(Auth::user()->id)]);
	}
	/**
	 * Profile update
	 *
	 * @return void
	 * @author harylalamentik@gmail.com
	 **/
	public function update(Request $request)
	{		
		$data = \App\User::find(Auth::user()->id);
		$data->name = $request->input('name');
		$data->email = $request->input('email');
		if ($request->has('password')) {			
			$data->password = \Hash::make($request->input('password'));
		}			
		$data->save();
		return redirect('/u/profile')->with('message','Saved');
	}
}


File: /app\Http\Kernel.php
<?php

namespace App\Http;

use Illuminate\Foundation\Http\Kernel as HttpKernel;

class Kernel extends HttpKernel
{
    /**
     * The application's global HTTP middleware stack.
     *
     * These middleware are run during every request to your application.
     *
     * @var array
     */
    protected $middleware = [
        \Illuminate\Foundation\Http\Middleware\CheckForMaintenanceMode::class,
    ];

    /**
     * The application's route middleware groups.
     *
     * @var array
     */
    protected $middlewareGroups = [
        'web' => [
            \App\Http\Middleware\EncryptCookies::class,
            \Illuminate\Cookie\Middleware\AddQueuedCookiesToResponse::class,
            \Illuminate\Session\Middleware\StartSession::class,
            \Illuminate\View\Middleware\ShareErrorsFromSession::class,
            \App\Http\Middleware\VerifyCsrfToken::class,
        ],

        'api' => [
            'throttle:60,1',
        ],
    ];

    /**
     * The application's route middleware.
     *
     * These middleware may be assigned to groups or used individually.
     *
     * @var array
     */
    protected $routeMiddleware = [
        'auth' => \App\Http\Middleware\Authenticate::class,
        'auth.basic' => \Illuminate\Auth\Middleware\AuthenticateWithBasicAuth::class,
        'can' => \Illuminate\Foundation\Http\Middleware\Authorize::class,
        'guest' => \App\Http\Middleware\RedirectIfAuthenticated::class,
        'throttle' => \Illuminate\Routing\Middleware\ThrottleRequests::class,
    ];
}


File: /app\Http\Middleware\Authenticate.php
<?php

namespace App\Http\Middleware;

use Closure;
use Illuminate\Support\Facades\Auth;

class Authenticate
{
    /**
     * Handle an incoming request.
     *
     * @param  \Illuminate\Http\Request  $request
     * @param  \Closure  $next
     * @param  string|null  $guard
     * @return mixed
     */
    public function handle($request, Closure $next, $guard = null)
    {
        if (Auth::guard($guard)->guest()) {
            if ($request->ajax() || $request->wantsJson()) {
                return response('Unauthorized.', 401);
            } else {
                return redirect()->guest('login');
            }
        }

        return $next($request);
    }
}


File: /app\Http\Middleware\EncryptCookies.php
<?php

namespace App\Http\Middleware;

use Illuminate\Cookie\Middleware\EncryptCookies as BaseEncrypter;

class EncryptCookies extends BaseEncrypter
{
    /**
     * The names of the cookies that should not be encrypted.
     *
     * @var array
     */
    protected $except = [
        //
    ];
}


File: /app\Http\Middleware\RedirectIfAuthenticated.php
<?php

namespace App\Http\Middleware;

use Closure;
use Illuminate\Support\Facades\Auth;

class RedirectIfAuthenticated
{
    /**
     * Handle an incoming request.
     *
     * @param  \Illuminate\Http\Request  $request
     * @param  \Closure  $next
     * @param  string|null  $guard
     * @return mixed
     */
    public function handle($request, Closure $next, $guard = null)
    {
        if (Auth::guard($guard)->check()) {
            return redirect('/');
        }

        return $next($request);
    }
}


File: /app\Http\Middleware\VerifyCsrfToken.php
<?php

namespace App\Http\Middleware;

use Illuminate\Foundation\Http\Middleware\VerifyCsrfToken as BaseVerifier;

class VerifyCsrfToken extends BaseVerifier
{
    /**
     * The URIs that should be excluded from CSRF verification.
     *
     * @var array
     */
    protected $except = [
        //
    ];
}


File: /app\Http\Requests\Request.php
<?php

namespace App\Http\Requests;

use Illuminate\Foundation\Http\FormRequest;

abstract class Request extends FormRequest
{
    //
}


File: /app\Http\routes.php
<?php

/*
|--------------------------------------------------------------------------
| Application Routes
|--------------------------------------------------------------------------
|
| Here is where you can register all of the routes for an application.
| It's a breeze. Simply tell Laravel the URIs it should respond to
| and give it the controller to call when that URI is requested.
|
*/

Route::get('/laravel5', function () {
    return view('welcome');
});

Route::get('/', function(){
	return view('main-page');
});


Route::auth();

Route::group(['middleware'=>'auth'], function(){	

	Route::get('/home', 'HomeController@index');
	// API mikrotik hotspot
	Route::get('/hotspot/profile','MikrotikController@ServerProfile');
	Route::get('/hotspot/ip-binding','MikrotikController@IpBinding');
	Route::get('/hotspot/user','MikrotikController@hsUsers');
	Route::get('/hotspot/user/profile','MikrotikController@UserProfile');
	Route::get('/hotspot/active','MikrotikController@hsActive');	

	Route::get('/router/command','MikrotikController@routerCommand');	

	// Mikrotik user
	Route::get('/user','HomeController@user');
	Route::get('/user/create','HomeController@createUser');
	Route::post('/user/create','MikrotikController@createUser');
	Route::get('/user/remove/{id}','MikrotikController@removeUser');
	Route::get('/user/{id}/edit','HomeController@editUser');
	Route::post('/user/{id}/edit','HomeController@editUserSave');


	Route::get('/binding','HomeController@IpBinding');	
	Route::get('/binding/create','HomeController@createIpBinding');
	Route::post('/binding/create','MikrotikController@createIpBinding');
	Route::get('/binding/{id}/remove','MikrotikController@removeIpBinding');
	Route::get('/binding/{id}/edit','HomeController@editIpBinding');
	Route::post('/binding/{id}/edit','HomeController@editIpBindingSave');

	Route::get('/active/kill/{id?}','MikrotikController@hotspotKillActive');
	Route::get('/user/active','HomeController@userActive');	

	Route::get('/u/profile','UserController@profile');
	Route::post('/u/profile','UserController@update');

	Route::get('/user/register','UserController@create');
	Route::post('/user/register','UserController@store');

	Route::get('/router','RouterController@edit');
	Route::post('/router','RouterController@update');	

});

Route::group(['middleware'=>'guest'],function(){
	Route::match(['GET','POST'],'/register',function(){
		return view('main-page');
	});	
});


File: /app\Jobs\Job.php
<?php

namespace App\Jobs;

use Illuminate\Bus\Queueable;

abstract class Job
{
    /*
    |--------------------------------------------------------------------------
    | Queueable Jobs
    |--------------------------------------------------------------------------
    |
    | This job base class provides a central location to place any logic that
    | is shared across all of your jobs. The trait included with the class
    | provides access to the "onQueue" and "delay" queue helper methods.
    |
    */

    use Queueable;
}


File: /app\Listeners\.gitkeep



File: /app\Mikrotik.php
<?php

namespace App;

use Illuminate\Database\Eloquent\Model;

class Mikrotik extends Model
{
    //
}


File: /app\Policies\.gitkeep



File: /app\Providers\AppServiceProvider.php
<?php

namespace App\Providers;

use Illuminate\Support\ServiceProvider;

class AppServiceProvider extends ServiceProvider
{
    /**
     * Bootstrap any application services.
     *
     * @return void
     */
    public function boot()
    {
        //
    }

    /**
     * Register any application services.
     *
     * @return void
     */
    public function register()
    {
        //
    }
}


File: /app\Providers\AuthServiceProvider.php
<?php

namespace App\Providers;

use Illuminate\Contracts\Auth\Access\Gate as GateContract;
use Illuminate\Foundation\Support\Providers\AuthServiceProvider as ServiceProvider;

class AuthServiceProvider extends ServiceProvider
{
    /**
     * The policy mappings for the application.
     *
     * @var array
     */
    protected $policies = [
        'App\Model' => 'App\Policies\ModelPolicy',
    ];

    /**
     * Register any application authentication / authorization services.
     *
     * @param  \Illuminate\Contracts\Auth\Access\Gate  $gate
     * @return void
     */
    public function boot(GateContract $gate)
    {
        $this->registerPolicies($gate);

        //
    }
}


File: /app\Providers\EventServiceProvider.php
<?php

namespace App\Providers;

use Illuminate\Contracts\Events\Dispatcher as DispatcherContract;
use Illuminate\Foundation\Support\Providers\EventServiceProvider as ServiceProvider;

class EventServiceProvider extends ServiceProvider
{
    /**
     * The event listener mappings for the application.
     *
     * @var array
     */
    protected $listen = [
        'App\Events\SomeEvent' => [
            'App\Listeners\EventListener',
        ],
    ];

    /**
     * Register any other events for your application.
     *
     * @param  \Illuminate\Contracts\Events\Dispatcher  $events
     * @return void
     */
    public function boot(DispatcherContract $events)
    {
        parent::boot($events);

        //
    }
}


File: /app\Providers\RouteServiceProvider.php
<?php

namespace App\Providers;

use Illuminate\Routing\Router;
use Illuminate\Foundation\Support\Providers\RouteServiceProvider as ServiceProvider;

class RouteServiceProvider extends ServiceProvider
{
    /**
     * This namespace is applied to your controller routes.
     *
     * In addition, it is set as the URL generator's root namespace.
     *
     * @var string
     */
    protected $namespace = 'App\Http\Controllers';

    /**
     * Define your route model bindings, pattern filters, etc.
     *
     * @param  \Illuminate\Routing\Router  $router
     * @return void
     */
    public function boot(Router $router)
    {
        //

        parent::boot($router);
    }

    /**
     * Define the routes for the application.
     *
     * @param  \Illuminate\Routing\Router  $router
     * @return void
     */
    public function map(Router $router)
    {
        $this->mapWebRoutes($router);

        //
    }

    /**
     * Define the "web" routes for the application.
     *
     * These routes all receive session state, CSRF protection, etc.
     *
     * @param  \Illuminate\Routing\Router  $router
     * @return void
     */
    protected function mapWebRoutes(Router $router)
    {
        $router->group([
            'namespace' => $this->namespace, 'middleware' => 'web',
        ], function ($router) {
            require app_path('Http/routes.php');
        });
    }
}


File: /app\User.php
<?php

namespace App;

use Illuminate\Foundation\Auth\User as Authenticatable;

class User extends Authenticatable
{
    /**
     * The attributes that are mass assignable.
     *
     * @var array
     */
    protected $fillable = [
        'name', 'email', 'password',
    ];

    /**
     * The attributes that should be hidden for arrays.
     *
     * @var array
     */
    protected $hidden = [
        'password', 'remember_token',
    ];
}


File: /artisan
#!/usr/bin/env php
<?php

/*
|--------------------------------------------------------------------------
| Register The Auto Loader
|--------------------------------------------------------------------------
|
| Composer provides a convenient, automatically generated class loader
| for our application. We just need to utilize it! We'll require it
| into the script here so that we do not have to worry about the
| loading of any our classes "manually". Feels great to relax.
|
*/

require __DIR__.'/bootstrap/autoload.php';

$app = require_once __DIR__.'/bootstrap/app.php';

/*
|--------------------------------------------------------------------------
| Run The Artisan Application
|--------------------------------------------------------------------------
|
| When we run the console application, the current CLI command will be
| executed in this console and the response sent back to a terminal
| or another output device for the developers. Here goes nothing!
|
*/

$kernel = $app->make(Illuminate\Contracts\Console\Kernel::class);

$status = $kernel->handle(
    $input = new Symfony\Component\Console\Input\ArgvInput,
    new Symfony\Component\Console\Output\ConsoleOutput
);

/*
|--------------------------------------------------------------------------
| Shutdown The Application
|--------------------------------------------------------------------------
|
| Once Artisan has finished running. We will fire off the shutdown events
| so that any final work may be done by the application before we shut
| down the process. This is the last thing to happen to the request.
|
*/

$kernel->terminate($input, $status);

exit($status);


File: /bootstrap\app.php
<?php

/*
|--------------------------------------------------------------------------
| Create The Application
|--------------------------------------------------------------------------
|
| The first thing we will do is create a new Laravel application instance
| which serves as the "glue" for all the components of Laravel, and is
| the IoC container for the system binding all of the various parts.
|
*/

$app = new Illuminate\Foundation\Application(
    realpath(__DIR__.'/../')
);

/*
|--------------------------------------------------------------------------
| Bind Important Interfaces
|--------------------------------------------------------------------------
|
| Next, we need to bind some important interfaces into the container so
| we will be able to resolve them when needed. The kernels serve the
| incoming requests to this application from both the web and CLI.
|
*/

$app->singleton(
    Illuminate\Contracts\Http\Kernel::class,
    App\Http\Kernel::class
);

$app->singleton(
    Illuminate\Contracts\Console\Kernel::class,
    App\Console\Kernel::class
);

$app->singleton(
    Illuminate\Contracts\Debug\ExceptionHandler::class,
    App\Exceptions\Handler::class
);

/*
|--------------------------------------------------------------------------
| Return The Application
|--------------------------------------------------------------------------
|
| This script returns the application instance. The instance is given to
| the calling script so we can separate the building of the instances
| from the actual running of the application and sending responses.
|
*/

return $app;


File: /bootstrap\autoload.php
<?php

define('LARAVEL_START', microtime(true));

/*
|--------------------------------------------------------------------------
| Register The Composer Auto Loader
|--------------------------------------------------------------------------
|
| Composer provides a convenient, automatically generated class loader
| for our application. We just need to utilize it! We'll require it
| into the script here so that we do not have to worry about the
| loading of any our classes "manually". Feels great to relax.
|
*/

require __DIR__.'/../vendor/autoload.php';

/*
|--------------------------------------------------------------------------
| Include The Compiled Class File
|--------------------------------------------------------------------------
|
| To dramatically increase your application's performance, you may use a
| compiled class file which contains all of the classes commonly used
| by a request. The Artisan "optimize" is used to create this file.
|
*/

$compiledPath = __DIR__.'/cache/compiled.php';

if (file_exists($compiledPath)) {
    require $compiledPath;
}


File: /bootstrap\cache\.gitignore
*
!.gitignore


File: /composer.json
{
    "name": "laravel/laravel",
    "description": "The Laravel Framework.",
    "keywords": ["framework", "laravel"],
    "license": "MIT",
    "type": "project",
    "require": {
        "php": ">=5.5.9",
        "laravel/framework": "5.2.*",
        "pear2/net_transmitter": "1.0.0a4",
        "pear2/net_routeros": "1.0.0b4",
        "pear2/cache_shm": "^0.1.3",
        "laravelcollective/html": "5.2.*"
    },
    "require-dev": {
        "fzaninotto/faker": "~1.4",
        "mockery/mockery": "0.9.*",
        "phpunit/phpunit": "~4.0",
        "symfony/css-selector": "2.8.*|3.0.*",
        "symfony/dom-crawler": "2.8.*|3.0.*"
    },
    "autoload": {
        "classmap": [
            "database"
        ],
        "psr-4": {
            "App\\": "app/"
        }
    },
    "autoload-dev": {
        "classmap": [
            "tests/TestCase.php"
        ]
    },
    "scripts": {
        "post-root-package-install": [
            "php -r \"copy('.env.example', '.env');\""
        ],
        "post-create-project-cmd": [
            "php artisan key:generate"
        ],
        "post-install-cmd": [
            "Illuminate\\Foundation\\ComposerScripts::postInstall",
            "php artisan optimize"
        ],
        "post-update-cmd": [
            "Illuminate\\Foundation\\ComposerScripts::postUpdate",
            "php artisan optimize"
        ]
    },
    "config": {
        "preferred-install": "dist"
    }
}


File: /composer.lock
{
    "_readme": [
        "This file locks the dependencies of your project to a known state",
        "Read more about it at https://getcomposer.org/doc/01-basic-usage.md#composer-lock-the-lock-file",
        "This file is @generated automatically"
    ],
    "hash": "fda3892f329c1ef4e78a0bac2461a88f",
    "content-hash": "363eff09d16e752117726a86bade0def",
    "packages": [
        {
            "name": "classpreloader/classpreloader",
            "version": "3.0.0",
            "source": {
                "type": "git",
                "url": "https://github.com/ClassPreloader/ClassPreloader.git",
                "reference": "9b10b913c2bdf90c3d2e0d726b454fb7f77c552a"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/ClassPreloader/ClassPreloader/zipball/9b10b913c2bdf90c3d2e0d726b454fb7f77c552a",
                "reference": "9b10b913c2bdf90c3d2e0d726b454fb7f77c552a",
                "shasum": ""
            },
            "require": {
                "nikic/php-parser": "^1.0|^2.0",
                "php": ">=5.5.9"
            },
            "require-dev": {
                "phpunit/phpunit": "^4.8|^5.0"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "3.0-dev"
                }
            },
            "autoload": {
                "psr-4": {
                    "ClassPreloader\\": "src/"
                }
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "Michael Dowling",
                    "email": "mtdowling@gmail.com"
                },
                {
                    "name": "Graham Campbell",
                    "email": "graham@alt-three.com"
                }
            ],
            "description": "Helps class loading performance by generating a single PHP file containing all of the autoloaded files for a specific use case",
            "keywords": [
                "autoload",
                "class",
                "preload"
            ],
            "time": "2015-11-09 22:51:51"
        },
        {
            "name": "dnoegel/php-xdg-base-dir",
            "version": "0.1",
            "source": {
                "type": "git",
                "url": "https://github.com/dnoegel/php-xdg-base-dir.git",
                "reference": "265b8593498b997dc2d31e75b89f053b5cc9621a"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/dnoegel/php-xdg-base-dir/zipball/265b8593498b997dc2d31e75b89f053b5cc9621a",
                "reference": "265b8593498b997dc2d31e75b89f053b5cc9621a",
                "shasum": ""
            },
            "require": {
                "php": ">=5.3.2"
            },
            "require-dev": {
                "phpunit/phpunit": "@stable"
            },
            "type": "project",
            "autoload": {
                "psr-4": {
                    "XdgBaseDir\\": "src/"
                }
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "description": "implementation of xdg base directory specification for php",
            "time": "2014-10-24 07:27:01"
        },
        {
            "name": "doctrine/inflector",
            "version": "v1.1.0",
            "source": {
                "type": "git",
                "url": "https://github.com/doctrine/inflector.git",
                "reference": "90b2128806bfde671b6952ab8bea493942c1fdae"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/doctrine/inflector/zipball/90b2128806bfde671b6952ab8bea493942c1fdae",
                "reference": "90b2128806bfde671b6952ab8bea493942c1fdae",
                "shasum": ""
            },
            "require": {
                "php": ">=5.3.2"
            },
            "require-dev": {
                "phpunit/phpunit": "4.*"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "1.1.x-dev"
                }
            },
            "autoload": {
                "psr-0": {
                    "Doctrine\\Common\\Inflector\\": "lib/"
                }
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "Roman Borschel",
                    "email": "roman@code-factory.org"
                },
                {
                    "name": "Benjamin Eberlei",
                    "email": "kontakt@beberlei.de"
                },
                {
                    "name": "Guilherme Blanco",
                    "email": "guilhermeblanco@gmail.com"
                },
                {
                    "name": "Jonathan Wage",
                    "email": "jonwage@gmail.com"
                },
                {
                    "name": "Johannes Schmitt",
                    "email": "schmittjoh@gmail.com"
                }
            ],
            "description": "Common String Manipulations with regard to casing and singular/plural rules.",
            "homepage": "http://www.doctrine-project.org",
            "keywords": [
                "inflection",
                "pluralize",
                "singularize",
                "string"
            ],
            "time": "2015-11-06 14:35:42"
        },
        {
            "name": "jakub-onderka/php-console-color",
            "version": "0.1",
            "source": {
                "type": "git",
                "url": "https://github.com/JakubOnderka/PHP-Console-Color.git",
                "reference": "e0b393dacf7703fc36a4efc3df1435485197e6c1"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/JakubOnderka/PHP-Console-Color/zipball/e0b393dacf7703fc36a4efc3df1435485197e6c1",
                "reference": "e0b393dacf7703fc36a4efc3df1435485197e6c1",
                "shasum": ""
            },
            "require": {
                "php": ">=5.3.2"
            },
            "require-dev": {
                "jakub-onderka/php-code-style": "1.0",
                "jakub-onderka/php-parallel-lint": "0.*",
                "jakub-onderka/php-var-dump-check": "0.*",
                "phpunit/phpunit": "3.7.*",
                "squizlabs/php_codesniffer": "1.*"
            },
            "type": "library",
            "autoload": {
                "psr-0": {
                    "JakubOnderka\\PhpConsoleColor": "src/"
                }
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "BSD-2-Clause"
            ],
            "authors": [
                {
                    "name": "Jakub Onderka",
                    "email": "jakub.onderka@gmail.com",
                    "homepage": "http://www.acci.cz"
                }
            ],
            "time": "2014-04-08 15:00:19"
        },
        {
            "name": "jakub-onderka/php-console-highlighter",
            "version": "v0.3.2",
            "source": {
                "type": "git",
                "url": "https://github.com/JakubOnderka/PHP-Console-Highlighter.git",
                "reference": "7daa75df45242c8d5b75a22c00a201e7954e4fb5"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/JakubOnderka/PHP-Console-Highlighter/zipball/7daa75df45242c8d5b75a22c00a201e7954e4fb5",
                "reference": "7daa75df45242c8d5b75a22c00a201e7954e4fb5",
                "shasum": ""
            },
            "require": {
                "jakub-onderka/php-console-color": "~0.1",
                "php": ">=5.3.0"
            },
            "require-dev": {
                "jakub-onderka/php-code-style": "~1.0",
                "jakub-onderka/php-parallel-lint": "~0.5",
                "jakub-onderka/php-var-dump-check": "~0.1",
                "phpunit/phpunit": "~4.0",
                "squizlabs/php_codesniffer": "~1.5"
            },
            "type": "library",
            "autoload": {
                "psr-0": {
                    "JakubOnderka\\PhpConsoleHighlighter": "src/"
                }
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "Jakub Onderka",
                    "email": "acci@acci.cz",
                    "homepage": "http://www.acci.cz/"
                }
            ],
            "time": "2015-04-20 18:58:01"
        },
        {
            "name": "jeremeamia/SuperClosure",
            "version": "2.2.0",
            "source": {
                "type": "git",
                "url": "https://github.com/jeremeamia/super_closure.git",
                "reference": "29a88be2a4846d27c1613aed0c9071dfad7b5938"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/jeremeamia/super_closure/zipball/29a88be2a4846d27c1613aed0c9071dfad7b5938",
                "reference": "29a88be2a4846d27c1613aed0c9071dfad7b5938",
                "shasum": ""
            },
            "require": {
                "nikic/php-parser": "^1.2|^2.0",
                "php": ">=5.4",
                "symfony/polyfill-php56": "^1.0"
            },
            "require-dev": {
                "phpunit/phpunit": "^4.0|^5.0"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "2.2-dev"
                }
            },
            "autoload": {
                "psr-4": {
                    "SuperClosure\\": "src/"
                }
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "Jeremy Lindblom",
                    "email": "jeremeamia@gmail.com",
                    "homepage": "https://github.com/jeremeamia",
                    "role": "Developer"
                }
            ],
            "description": "Serialize Closure objects, including their context and binding",
            "homepage": "https://github.com/jeremeamia/super_closure",
            "keywords": [
                "closure",
                "function",
                "lambda",
                "parser",
                "serializable",
                "serialize",
                "tokenizer"
            ],
            "time": "2015-12-05 17:17:57"
        },
        {
            "name": "laravel/framework",
            "version": "v5.2.29",
            "source": {
                "type": "git",
                "url": "https://github.com/laravel/framework.git",
                "reference": "e3d644eb131f18c5f3d28ff7bc678bc797091f20"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/laravel/framework/zipball/e3d644eb131f18c5f3d28ff7bc678bc797091f20",
                "reference": "e3d644eb131f18c5f3d28ff7bc678bc797091f20",
                "shasum": ""
            },
            "require": {
                "classpreloader/classpreloader": "~3.0",
                "doctrine/inflector": "~1.0",
                "ext-mbstring": "*",
                "ext-openssl": "*",
                "jeremeamia/superclosure": "~2.2",
                "league/flysystem": "~1.0",
                "monolog/monolog": "~1.11",
                "mtdowling/cron-expression": "~1.0",
                "nesbot/carbon": "~1.20",
                "paragonie/random_compat": "~1.4",
                "php": ">=5.5.9",
                "psy/psysh": "0.7.*",
                "swiftmailer/swiftmailer": "~5.1",
                "symfony/console": "2.8.*|3.0.*",
                "symfony/debug": "2.8.*|3.0.*",
                "symfony/finder": "2.8.*|3.0.*",
                "symfony/http-foundation": "2.8.*|3.0.*",
                "symfony/http-kernel": "2.8.*|3.0.*",
                "symfony/polyfill-php56": "~1.0",
                "symfony/process": "2.8.*|3.0.*",
                "symfony/routing": "2.8.*|3.0.*",
                "symfony/translation": "2.8.*|3.0.*",
                "symfony/var-dumper": "2.8.*|3.0.*",
                "vlucas/phpdotenv": "~2.2"
            },
            "replace": {
                "illuminate/auth": "self.version",
                "illuminate/broadcasting": "self.version",
                "illuminate/bus": "self.version",
                "illuminate/cache": "self.version",
                "illuminate/config": "self.version",
                "illuminate/console": "self.version",
                "illuminate/container": "self.version",
                "illuminate/contracts": "self.version",
                "illuminate/cookie": "self.version",
                "illuminate/database": "self.version",
                "illuminate/encryption": "self.version",
                "illuminate/events": "self.version",
                "illuminate/exception": "self.version",
                "illuminate/filesystem": "self.version",
                "illuminate/hashing": "self.version",
                "illuminate/http": "self.version",
                "illuminate/log": "self.version",
                "illuminate/mail": "self.version",
                "illuminate/pagination": "self.version",
                "illuminate/pipeline": "self.version",
                "illuminate/queue": "self.version",
                "illuminate/redis": "self.version",
                "illuminate/routing": "self.version",
                "illuminate/session": "self.version",
                "illuminate/support": "self.version",
                "illuminate/translation": "self.version",
                "illuminate/validation": "self.version",
                "illuminate/view": "self.version"
            },
            "require-dev": {
                "aws/aws-sdk-php": "~3.0",
                "mockery/mockery": "~0.9.2",
                "pda/pheanstalk": "~3.0",
                "phpunit/phpunit": "~4.1",
                "predis/predis": "~1.0",
                "symfony/css-selector": "2.8.*|3.0.*",
                "symfony/dom-crawler": "2.8.*|3.0.*"
            },
            "suggest": {
                "aws/aws-sdk-php": "Required to use the SQS queue driver and SES mail driver (~3.0).",
                "doctrine/dbal": "Required to rename columns and drop SQLite columns (~2.4).",
                "fzaninotto/faker": "Required to use the eloquent factory builder (~1.4).",
                "guzzlehttp/guzzle": "Required to use the Mailgun and Mandrill mail drivers and the ping methods on schedules (~5.3|~6.0).",
                "league/flysystem-aws-s3-v3": "Required to use the Flysystem S3 driver (~1.0).",
                "league/flysystem-rackspace": "Required to use the Flysystem Rackspace driver (~1.0).",
                "pda/pheanstalk": "Required to use the beanstalk queue driver (~3.0).",
                "predis/predis": "Required to use the redis cache and queue drivers (~1.0).",
                "pusher/pusher-php-server": "Required to use the Pusher broadcast driver (~2.0).",
                "symfony/css-selector": "Required to use some of the crawler integration testing tools (2.8.*|3.0.*).",
                "symfony/dom-crawler": "Required to use most of the crawler integration testing tools (2.8.*|3.0.*)."
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "5.2-dev"
                }
            },
            "autoload": {
                "classmap": [
                    "src/Illuminate/Queue/IlluminateQueueClosure.php"
                ],
                "files": [
                    "src/Illuminate/Foundation/helpers.php",
                    "src/Illuminate/Support/helpers.php"
                ],
                "psr-4": {
                    "Illuminate\\": "src/Illuminate/"
                }
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "Taylor Otwell",
                    "email": "taylorotwell@gmail.com"
                }
            ],
            "description": "The Laravel Framework.",
            "homepage": "http://laravel.com",
            "keywords": [
                "framework",
                "laravel"
            ],
            "time": "2016-04-03 01:43:55"
        },
        {
            "name": "laravelcollective/html",
            "version": "v5.2.4",
            "source": {
                "type": "git",
                "url": "https://github.com/LaravelCollective/html.git",
                "reference": "3a312d39ffe37da0f57b602618b61fd07c1fcec5"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/LaravelCollective/html/zipball/3a312d39ffe37da0f57b602618b61fd07c1fcec5",
                "reference": "3a312d39ffe37da0f57b602618b61fd07c1fcec5",
                "shasum": ""
            },
            "require": {
                "illuminate/http": "5.2.*",
                "illuminate/routing": "5.2.*",
                "illuminate/session": "5.2.*",
                "illuminate/support": "5.2.*",
                "illuminate/view": "5.2.*",
                "php": ">=5.5.9"
            },
            "require-dev": {
                "illuminate/database": "5.2.*",
                "mockery/mockery": "~0.9",
                "phpunit/phpunit": "~4.0"
            },
            "type": "library",
            "autoload": {
                "psr-4": {
                    "Collective\\Html\\": "src/"
                },
                "files": [
                    "src/helpers.php"
                ]
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "Taylor Otwell",
                    "email": "taylorotwell@gmail.com"
                },
                {
                    "name": "Adam Engebretson",
                    "email": "adam@laravelcollective.com"
                }
            ],
            "description": "HTML and Form Builders for the Laravel Framework",
            "homepage": "http://laravelcollective.com",
            "time": "2016-01-27 22:29:54"
        },
        {
            "name": "league/flysystem",
            "version": "1.0.20",
            "source": {
                "type": "git",
                "url": "https://github.com/thephpleague/flysystem.git",
                "reference": "e87a786e3ae12a25cf78a71bb07b4b384bfaa83a"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/thephpleague/flysystem/zipball/e87a786e3ae12a25cf78a71bb07b4b384bfaa83a",
                "reference": "e87a786e3ae12a25cf78a71bb07b4b384bfaa83a",
                "shasum": ""
            },
            "require": {
                "php": ">=5.4.0"
            },
            "conflict": {
                "league/flysystem-sftp": "<1.0.6"
            },
            "require-dev": {
                "ext-fileinfo": "*",
                "mockery/mockery": "~0.9",
                "phpspec/phpspec": "^2.2",
                "phpunit/phpunit": "~4.8 || ~5.0"
            },
            "suggest": {
                "ext-fileinfo": "Required for MimeType",
                "league/flysystem-aws-s3-v2": "Allows you to use S3 storage with AWS SDK v2",
                "league/flysystem-aws-s3-v3": "Allows you to use S3 storage with AWS SDK v3",
                "league/flysystem-azure": "Allows you to use Windows Azure Blob storage",
                "league/flysystem-cached-adapter": "Flysystem adapter decorator for metadata caching",
                "league/flysystem-copy": "Allows you to use Copy.com storage",
                "league/flysystem-dropbox": "Allows you to use Dropbox storage",
                "league/flysystem-eventable-filesystem": "Allows you to use EventableFilesystem",
                "league/flysystem-rackspace": "Allows you to use Rackspace Cloud Files",
                "league/flysystem-sftp": "Allows you to use SFTP server storage via phpseclib",
                "league/flysystem-webdav": "Allows you to use WebDAV storage",
                "league/flysystem-ziparchive": "Allows you to use ZipArchive adapter"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "1.1-dev"
                }
            },
            "autoload": {
                "psr-4": {
                    "League\\Flysystem\\": "src/"
                }
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "Frank de Jonge",
                    "email": "info@frenky.net"
                }
            ],
            "description": "Filesystem abstraction: Many filesystems, one API.",
            "keywords": [
                "Cloud Files",
                "WebDAV",
                "abstraction",
                "aws",
                "cloud",
                "copy.com",
                "dropbox",
                "file systems",
                "files",
                "filesystem",
                "filesystems",
                "ftp",
                "rackspace",
                "remote",
                "s3",
                "sftp",
                "storage"
            ],
            "time": "2016-03-14 21:54:11"
        },
        {
            "name": "monolog/monolog",
            "version": "1.19.0",
            "source": {
                "type": "git",
                "url": "https://github.com/Seldaek/monolog.git",
                "reference": "5f56ed5212dc509c8dc8caeba2715732abb32dbf"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/Seldaek/monolog/zipball/5f56ed5212dc509c8dc8caeba2715732abb32dbf",
                "reference": "5f56ed5212dc509c8dc8caeba2715732abb32dbf",
                "shasum": ""
            },
            "require": {
                "php": ">=5.3.0",
                "psr/log": "~1.0"
            },
            "provide": {
                "psr/log-implementation": "1.0.0"
            },
            "require-dev": {
                "aws/aws-sdk-php": "^2.4.9",
                "doctrine/couchdb": "~1.0@dev",
                "graylog2/gelf-php": "~1.0",
                "jakub-onderka/php-parallel-lint": "0.9",
                "php-amqplib/php-amqplib": "~2.4",
                "php-console/php-console": "^3.1.3",
                "phpunit/phpunit": "~4.5",
                "phpunit/phpunit-mock-objects": "2.3.0",
                "raven/raven": "^0.13",
                "ruflin/elastica": ">=0.90 <3.0",
                "swiftmailer/swiftmailer": "~5.3"
            },
            "suggest": {
                "aws/aws-sdk-php": "Allow sending log messages to AWS services like DynamoDB",
                "doctrine/couchdb": "Allow sending log messages to a CouchDB server",
                "ext-amqp": "Allow sending log messages to an AMQP server (1.0+ required)",
                "ext-mongo": "Allow sending log messages to a MongoDB server",
                "graylog2/gelf-php": "Allow sending log messages to a GrayLog2 server",
                "mongodb/mongodb": "Allow sending log messages to a MongoDB server via PHP Driver",
                "php-amqplib/php-amqplib": "Allow sending log messages to an AMQP server using php-amqplib",
                "php-console/php-console": "Allow sending log messages to Google Chrome",
                "raven/raven": "Allow sending log messages to a Sentry server",
                "rollbar/rollbar": "Allow sending log messages to Rollbar",
                "ruflin/elastica": "Allow sending log messages to an Elastic Search server"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "2.0.x-dev"
                }
            },
            "autoload": {
                "psr-4": {
                    "Monolog\\": "src/Monolog"
                }
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "Jordi Boggiano",
                    "email": "j.boggiano@seld.be",
                    "homepage": "http://seld.be"
                }
            ],
            "description": "Sends your logs to files, sockets, inboxes, databases and various web services",
            "homepage": "http://github.com/Seldaek/monolog",
            "keywords": [
                "log",
                "logging",
                "psr-3"
            ],
            "time": "2016-04-12 18:29:35"
        },
        {
            "name": "mtdowling/cron-expression",
            "version": "v1.1.0",
            "source": {
                "type": "git",
                "url": "https://github.com/mtdowling/cron-expression.git",
                "reference": "c9ee7886f5a12902b225a1a12f36bb45f9ab89e5"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/mtdowling/cron-expression/zipball/c9ee7886f5a12902b225a1a12f36bb45f9ab89e5",
                "reference": "c9ee7886f5a12902b225a1a12f36bb45f9ab89e5",
                "shasum": ""
            },
            "require": {
                "php": ">=5.3.2"
            },
            "require-dev": {
                "phpunit/phpunit": "~4.0|~5.0"
            },
            "type": "library",
            "autoload": {
                "psr-0": {
                    "Cron": "src/"
                }
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "Michael Dowling",
                    "email": "mtdowling@gmail.com",
                    "homepage": "https://github.com/mtdowling"
                }
            ],
            "description": "CRON for PHP: Calculate the next or previous run date and determine if a CRON expression is due",
            "keywords": [
                "cron",
                "schedule"
            ],
            "time": "2016-01-26 21:23:30"
        },
        {
            "name": "nesbot/carbon",
            "version": "1.21.0",
            "source": {
                "type": "git",
                "url": "https://github.com/briannesbitt/Carbon.git",
                "reference": "7b08ec6f75791e130012f206e3f7b0e76e18e3d7"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/briannesbitt/Carbon/zipball/7b08ec6f75791e130012f206e3f7b0e76e18e3d7",
                "reference": "7b08ec6f75791e130012f206e3f7b0e76e18e3d7",
                "shasum": ""
            },
            "require": {
                "php": ">=5.3.0",
                "symfony/translation": "~2.6|~3.0"
            },
            "require-dev": {
                "phpunit/phpunit": "~4.0|~5.0"
            },
            "type": "library",
            "autoload": {
                "psr-4": {
                    "Carbon\\": "src/Carbon/"
                }
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "Brian Nesbitt",
                    "email": "brian@nesbot.com",
                    "homepage": "http://nesbot.com"
                }
            ],
            "description": "A simple API extension for DateTime.",
            "homepage": "http://carbon.nesbot.com",
            "keywords": [
                "date",
                "datetime",
                "time"
            ],
            "time": "2015-11-04 20:07:17"
        },
        {
            "name": "nikic/php-parser",
            "version": "v2.0.1",
            "source": {
                "type": "git",
                "url": "https://github.com/nikic/PHP-Parser.git",
                "reference": "ce5be709d59b32dd8a88c80259028759991a4206"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/nikic/PHP-Parser/zipball/ce5be709d59b32dd8a88c80259028759991a4206",
                "reference": "ce5be709d59b32dd8a88c80259028759991a4206",
                "shasum": ""
            },
            "require": {
                "ext-tokenizer": "*",
                "php": ">=5.4"
            },
            "require-dev": {
                "phpunit/phpunit": "~4.0"
            },
            "bin": [
                "bin/php-parse"
            ],
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "2.0-dev"
                }
            },
            "autoload": {
                "psr-4": {
                    "PhpParser\\": "lib/PhpParser"
                }
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "BSD-3-Clause"
            ],
            "authors": [
                {
                    "name": "Nikita Popov"
                }
            ],
            "description": "A PHP parser written in PHP",
            "keywords": [
                "parser",
                "php"
            ],
            "time": "2016-02-28 19:48:28"
        },
        {
            "name": "paragonie/random_compat",
            "version": "v1.4.1",
            "source": {
                "type": "git",
                "url": "https://github.com/paragonie/random_compat.git",
                "reference": "c7e26a21ba357863de030f0b9e701c7d04593774"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/paragonie/random_compat/zipball/c7e26a21ba357863de030f0b9e701c7d04593774",
                "reference": "c7e26a21ba357863de030f0b9e701c7d04593774",
                "shasum": ""
            },
            "require": {
                "php": ">=5.2.0"
            },
            "require-dev": {
                "phpunit/phpunit": "4.*|5.*"
            },
            "suggest": {
                "ext-libsodium": "Provides a modern crypto API that can be used to generate random bytes."
            },
            "type": "library",
            "autoload": {
                "files": [
                    "lib/random.php"
                ]
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "Paragon Initiative Enterprises",
                    "email": "security@paragonie.com",
                    "homepage": "https://paragonie.com"
                }
            ],
            "description": "PHP 5.x polyfill for random_bytes() and random_int() from PHP 7",
            "keywords": [
                "csprng",
                "pseudorandom",
                "random"
            ],
            "time": "2016-03-18 20:34:03"
        },
        {
            "name": "pear2/cache_shm",
            "version": "0.1.3",
            "source": {
                "type": "git",
                "url": "https://github.com/pear2/Cache_SHM.git",
                "reference": "fa0f3e753a1ff9d5b583dff1ddb299dc67b5921d"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/pear2/Cache_SHM/zipball/fa0f3e753a1ff9d5b583dff1ddb299dc67b5921d",
                "reference": "fa0f3e753a1ff9d5b583dff1ddb299dc67b5921d",
                "shasum": ""
            },
            "require": {
                "php": ">=5.3.0"
            },
            "suggest": {
                "ext-apc": ">=3.0.13",
                "ext-wincache": ">=1.1.0"
            },
            "type": "library",
            "autoload": {
                "psr-0": {
                    "PEAR2\\Cache\\SHM": "src/"
                }
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "LGPL-2.1"
            ],
            "authors": [
                {
                    "name": "Vasil Rangelov",
                    "email": "boen.robot@gmail.com",
                    "role": "lead"
                }
            ],
            "description": "Wrapper for shared memory and locking functionality across different PHP extensions.",
            "homepage": "http://pear2.github.com/Cache_SHM/",
            "keywords": [
                "abstraction",
                "apc",
                "cache",
                "caching",
                "lock",
                "locking",
                "pear2",
                "shm",
                "wincache"
            ],
            "time": "2014-11-04 13:02:07"
        },
        {
            "name": "pear2/net_routeros",
            "version": "1.0.0b4",
            "source": {
                "type": "git",
                "url": "https://github.com/pear2/Net_RouterOS.git",
                "reference": "03b061d9ebadf97114160f75bdf34a7ba0abe93a"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/pear2/Net_RouterOS/zipball/03b061d9ebadf97114160f75bdf34a7ba0abe93a",
                "reference": "03b061d9ebadf97114160f75bdf34a7ba0abe93a",
                "shasum": ""
            },
            "require": {
                "pear2/net_transmitter": ">=1.0.0a4",
                "php": ">=5.3.0"
            },
            "suggest": {
                "ext-apc": ">=3.0.13",
                "ext-openssl": "*",
                "ext-wincache": ">=1.1.0",
                "pear2/cache_shm": ">=0.1.2"
            },
            "type": "library",
            "autoload": {
                "psr-0": {
                    "PEAR2\\Net\\RouterOS\\": "src/",
                    "PEAR2\\Net\\Transmitter\\": "vendor/pear2/net_transmitter/src/",
                    "PEAR2\\Cache\\SHM": "vendor/pear2/cache_shm/src/"
                }
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "LGPL-2.1"
            ],
            "authors": [
                {
                    "name": "Vasil Rangelov",
                    "email": "boen.robot@gmail.com",
                    "role": "helper"
                }
            ],
            "description": "This package allows you to read and write information from a RouterOS host using MikroTik's RouterOS API.",
            "homepage": "http://pear2.github.com/Net_RouterOS/",
            "keywords": [
                "api",
                "mikrotik",
                "package",
                "pear2",
                "router",
                "routeros"
            ],
            "time": "2013-08-15 16:47:55"
        },
        {
            "name": "pear2/net_transmitter",
            "version": "1.0.0a4",
            "source": {
                "type": "git",
                "url": "https://github.com/pear2/Net_Transmitter.git",
                "reference": "dfd4c0d57a62d5cd48a0df4b03482986c258a935"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/pear2/Net_Transmitter/zipball/dfd4c0d57a62d5cd48a0df4b03482986c258a935",
                "reference": "dfd4c0d57a62d5cd48a0df4b03482986c258a935",
                "shasum": ""
            },
            "require": {
                "php": ">=5.3.0"
            },
            "suggest": {
                "ext-apc": ">=3.0.13",
                "ext-openssl": "*",
                "ext-wincache": ">=1.1.0",
                "pear2/cache_shm": ">=0.1.2"
            },
            "type": "library",
            "autoload": {
                "psr-0": {
                    "PEAR2\\Net\\Transmitter\\": "src/"
                }
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "LGPL-2.1"
            ],
            "authors": [
                {
                    "name": "Vasil Rangelov",
                    "email": "boen.robot@gmail.com",
                    "role": "helper"
                }
            ],
            "description": "A stream wrapper that ensures data integrity. Particularly useful for sockets.",
            "homepage": "http://pear2.github.com/Net_Transmitter/",
            "keywords": [
                "Socket",
                "integrity",
                "network",
                "networking",
                "package",
                "pear2",
                "sockets"
            ],
            "time": "2013-08-15 17:12:58"
        },
        {
            "name": "psr/log",
            "version": "1.0.0",
            "source": {
                "type": "git",
                "url": "https://github.com/php-fig/log.git",
                "reference": "fe0936ee26643249e916849d48e3a51d5f5e278b"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/php-fig/log/zipball/fe0936ee26643249e916849d48e3a51d5f5e278b",
                "reference": "fe0936ee26643249e916849d48e3a51d5f5e278b",
                "shasum": ""
            },
            "type": "library",
            "autoload": {
                "psr-0": {
                    "Psr\\Log\\": ""
                }
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "PHP-FIG",
                    "homepage": "http://www.php-fig.org/"
                }
            ],
            "description": "Common interface for logging libraries",
            "keywords": [
                "log",
                "psr",
                "psr-3"
            ],
            "time": "2012-12-21 11:40:51"
        },
        {
            "name": "psy/psysh",
            "version": "v0.7.2",
            "source": {
                "type": "git",
                "url": "https://github.com/bobthecow/psysh.git",
                "reference": "e64e10b20f8d229cac76399e1f3edddb57a0f280"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/bobthecow/psysh/zipball/e64e10b20f8d229cac76399e1f3edddb57a0f280",
                "reference": "e64e10b20f8d229cac76399e1f3edddb57a0f280",
                "shasum": ""
            },
            "require": {
                "dnoegel/php-xdg-base-dir": "0.1",
                "jakub-onderka/php-console-highlighter": "0.3.*",
                "nikic/php-parser": "^1.2.1|~2.0",
                "php": ">=5.3.9",
                "symfony/console": "~2.3.10|^2.4.2|~3.0",
                "symfony/var-dumper": "~2.7|~3.0"
            },
            "require-dev": {
                "fabpot/php-cs-fixer": "~1.5",
                "phpunit/phpunit": "~3.7|~4.0|~5.0",
                "squizlabs/php_codesniffer": "~2.0",
                "symfony/finder": "~2.1|~3.0"
            },
            "suggest": {
                "ext-pcntl": "Enabling the PCNTL extension makes PsySH a lot happier :)",
                "ext-pdo-sqlite": "The doc command requires SQLite to work.",
                "ext-posix": "If you have PCNTL, you'll want the POSIX extension as well.",
                "ext-readline": "Enables support for arrow-key history navigation, and showing and manipulating command history."
            },
            "bin": [
                "bin/psysh"
            ],
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-develop": "0.8.x-dev"
                }
            },
            "autoload": {
                "files": [
                    "src/Psy/functions.php"
                ],
                "psr-4": {
                    "Psy\\": "src/Psy/"
                }
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "Justin Hileman",
                    "email": "justin@justinhileman.info",
                    "homepage": "http://justinhileman.com"
                }
            ],
            "description": "An interactive shell for modern PHP.",
            "homepage": "http://psysh.org",
            "keywords": [
                "REPL",
                "console",
                "interactive",
                "shell"
            ],
            "time": "2016-03-09 05:03:14"
        },
        {
            "name": "swiftmailer/swiftmailer",
            "version": "v5.4.1",
            "source": {
                "type": "git",
                "url": "https://github.com/swiftmailer/swiftmailer.git",
                "reference": "0697e6aa65c83edf97bb0f23d8763f94e3f11421"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/swiftmailer/swiftmailer/zipball/0697e6aa65c83edf97bb0f23d8763f94e3f11421",
                "reference": "0697e6aa65c83edf97bb0f23d8763f94e3f11421",
                "shasum": ""
            },
            "require": {
                "php": ">=5.3.3"
            },
            "require-dev": {
                "mockery/mockery": "~0.9.1,<0.9.4"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "5.4-dev"
                }
            },
            "autoload": {
                "files": [
                    "lib/swift_required.php"
                ]
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "Chris Corbyn"
                },
                {
                    "name": "Fabien Potencier",
                    "email": "fabien@symfony.com"
                }
            ],
            "description": "Swiftmailer, free feature-rich PHP mailer",
            "homepage": "http://swiftmailer.org",
            "keywords": [
                "email",
                "mail",
                "mailer"
            ],
            "time": "2015-06-06 14:19:39"
        },
        {
            "name": "symfony/console",
            "version": "v3.0.4",
            "source": {
                "type": "git",
                "url": "https://github.com/symfony/console.git",
                "reference": "6b1175135bc2a74c08a28d89761272de8beed8cd"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/symfony/console/zipball/6b1175135bc2a74c08a28d89761272de8beed8cd",
                "reference": "6b1175135bc2a74c08a28d89761272de8beed8cd",
                "shasum": ""
            },
            "require": {
                "php": ">=5.5.9",
                "symfony/polyfill-mbstring": "~1.0"
            },
            "require-dev": {
                "psr/log": "~1.0",
                "symfony/event-dispatcher": "~2.8|~3.0",
                "symfony/process": "~2.8|~3.0"
            },
            "suggest": {
                "psr/log": "For using the console logger",
                "symfony/event-dispatcher": "",
                "symfony/process": ""
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "3.0-dev"
                }
            },
            "autoload": {
                "psr-4": {
                    "Symfony\\Component\\Console\\": ""
                },
                "exclude-from-classmap": [
                    "/Tests/"
                ]
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "Fabien Potencier",
                    "email": "fabien@symfony.com"
                },
                {
                    "name": "Symfony Community",
                    "homepage": "https://symfony.com/contributors"
                }
            ],
            "description": "Symfony Console Component",
            "homepage": "https://symfony.com",
            "time": "2016-03-16 17:00:50"
        },
        {
            "name": "symfony/debug",
            "version": "v3.0.4",
            "source": {
                "type": "git",
                "url": "https://github.com/symfony/debug.git",
                "reference": "a06d10888a45afd97534506afb058ec38d9ba35b"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/symfony/debug/zipball/a06d10888a45afd97534506afb058ec38d9ba35b",
                "reference": "a06d10888a45afd97534506afb058ec38d9ba35b",
                "shasum": ""
            },
            "require": {
                "php": ">=5.5.9",
                "psr/log": "~1.0"
            },
            "conflict": {
                "symfony/http-kernel": ">=2.3,<2.3.24|~2.4.0|>=2.5,<2.5.9|>=2.6,<2.6.2"
            },
            "require-dev": {
                "symfony/class-loader": "~2.8|~3.0",
                "symfony/http-kernel": "~2.8|~3.0"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "3.0-dev"
                }
            },
            "autoload": {
                "psr-4": {
                    "Symfony\\Component\\Debug\\": ""
                },
                "exclude-from-classmap": [
                    "/Tests/"
                ]
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "Fabien Potencier",
                    "email": "fabien@symfony.com"
                },
                {
                    "name": "Symfony Community",
                    "homepage": "https://symfony.com/contributors"
                }
            ],
            "description": "Symfony Debug Component",
            "homepage": "https://symfony.com",
            "time": "2016-03-30 10:41:14"
        },
        {
            "name": "symfony/event-dispatcher",
            "version": "v3.0.4",
            "source": {
                "type": "git",
                "url": "https://github.com/symfony/event-dispatcher.git",
                "reference": "9002dcf018d884d294b1ef20a6f968efc1128f39"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/symfony/event-dispatcher/zipball/9002dcf018d884d294b1ef20a6f968efc1128f39",
                "reference": "9002dcf018d884d294b1ef20a6f968efc1128f39",
                "shasum": ""
            },
            "require": {
                "php": ">=5.5.9"
            },
            "require-dev": {
                "psr/log": "~1.0",
                "symfony/config": "~2.8|~3.0",
                "symfony/dependency-injection": "~2.8|~3.0",
                "symfony/expression-language": "~2.8|~3.0",
                "symfony/stopwatch": "~2.8|~3.0"
            },
            "suggest": {
                "symfony/dependency-injection": "",
                "symfony/http-kernel": ""
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "3.0-dev"
                }
            },
            "autoload": {
                "psr-4": {
                    "Symfony\\Component\\EventDispatcher\\": ""
                },
                "exclude-from-classmap": [
                    "/Tests/"
                ]
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "Fabien Potencier",
                    "email": "fabien@symfony.com"
                },
                {
                    "name": "Symfony Community",
                    "homepage": "https://symfony.com/contributors"
                }
            ],
            "description": "Symfony EventDispatcher Component",
            "homepage": "https://symfony.com",
            "time": "2016-03-10 10:34:12"
        },
        {
            "name": "symfony/finder",
            "version": "v3.0.4",
            "source": {
                "type": "git",
                "url": "https://github.com/symfony/finder.git",
                "reference": "c54e407b35bc098916704e9fd090da21da4c4f52"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/symfony/finder/zipball/c54e407b35bc098916704e9fd090da21da4c4f52",
                "reference": "c54e407b35bc098916704e9fd090da21da4c4f52",
                "shasum": ""
            },
            "require": {
                "php": ">=5.5.9"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "3.0-dev"
                }
            },
            "autoload": {
                "psr-4": {
                    "Symfony\\Component\\Finder\\": ""
                },
                "exclude-from-classmap": [
                    "/Tests/"
                ]
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "Fabien Potencier",
                    "email": "fabien@symfony.com"
                },
                {
                    "name": "Symfony Community",
                    "homepage": "https://symfony.com/contributors"
                }
            ],
            "description": "Symfony Finder Component",
            "homepage": "https://symfony.com",
            "time": "2016-03-10 11:13:05"
        },
        {
            "name": "symfony/http-foundation",
            "version": "v3.0.4",
            "source": {
                "type": "git",
                "url": "https://github.com/symfony/http-foundation.git",
                "reference": "99f38445a874e7becb8afc4b4a79ee181cf6ec3f"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/symfony/http-foundation/zipball/99f38445a874e7becb8afc4b4a79ee181cf6ec3f",
                "reference": "99f38445a874e7becb8afc4b4a79ee181cf6ec3f",
                "shasum": ""
            },
            "require": {
                "php": ">=5.5.9",
                "symfony/polyfill-mbstring": "~1.1"
            },
            "require-dev": {
                "symfony/expression-language": "~2.8|~3.0"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "3.0-dev"
                }
            },
            "autoload": {
                "psr-4": {
                    "Symfony\\Component\\HttpFoundation\\": ""
                },
                "exclude-from-classmap": [
                    "/Tests/"
                ]
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "Fabien Potencier",
                    "email": "fabien@symfony.com"
                },
                {
                    "name": "Symfony Community",
                    "homepage": "https://symfony.com/contributors"
                }
            ],
            "description": "Symfony HttpFoundation Component",
            "homepage": "https://symfony.com",
            "time": "2016-03-27 14:50:32"
        },
        {
            "name": "symfony/http-kernel",
            "version": "v3.0.4",
            "source": {
                "type": "git",
                "url": "https://github.com/symfony/http-kernel.git",
                "reference": "579f828489659d7b3430f4bd9b67b4618b387dea"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/symfony/http-kernel/zipball/579f828489659d7b3430f4bd9b67b4618b387dea",
                "reference": "579f828489659d7b3430f4bd9b67b4618b387dea",
                "shasum": ""
            },
            "require": {
                "php": ">=5.5.9",
                "psr/log": "~1.0",
                "symfony/debug": "~2.8|~3.0",
                "symfony/event-dispatcher": "~2.8|~3.0",
                "symfony/http-foundation": "~2.8|~3.0"
            },
            "conflict": {
                "symfony/config": "<2.8"
            },
            "require-dev": {
                "symfony/browser-kit": "~2.8|~3.0",
                "symfony/class-loader": "~2.8|~3.0",
                "symfony/config": "~2.8|~3.0",
                "symfony/console": "~2.8|~3.0",
                "symfony/css-selector": "~2.8|~3.0",
                "symfony/dependency-injection": "~2.8|~3.0",
                "symfony/dom-crawler": "~2.8|~3.0",
                "symfony/expression-language": "~2.8|~3.0",
                "symfony/finder": "~2.8|~3.0",
                "symfony/process": "~2.8|~3.0",
                "symfony/routing": "~2.8|~3.0",
                "symfony/stopwatch": "~2.8|~3.0",
                "symfony/templating": "~2.8|~3.0",
                "symfony/translation": "~2.8|~3.0",
                "symfony/var-dumper": "~2.8|~3.0"
            },
            "suggest": {
                "symfony/browser-kit": "",
                "symfony/class-loader": "",
                "symfony/config": "",
                "symfony/console": "",
                "symfony/dependency-injection": "",
                "symfony/finder": "",
                "symfony/var-dumper": ""
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "3.0-dev"
                }
            },
            "autoload": {
                "psr-4": {
                    "Symfony\\Component\\HttpKernel\\": ""
                },
                "exclude-from-classmap": [
                    "/Tests/"
                ]
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "Fabien Potencier",
                    "email": "fabien@symfony.com"
                },
                {
                    "name": "Symfony Community",
                    "homepage": "https://symfony.com/contributors"
                }
            ],
            "description": "Symfony HttpKernel Component",
            "homepage": "https://symfony.com",
            "time": "2016-03-25 01:41:20"
        },
        {
            "name": "symfony/polyfill-mbstring",
            "version": "v1.1.1",
            "source": {
                "type": "git",
                "url": "https://github.com/symfony/polyfill-mbstring.git",
                "reference": "1289d16209491b584839022f29257ad859b8532d"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/symfony/polyfill-mbstring/zipball/1289d16209491b584839022f29257ad859b8532d",
                "reference": "1289d16209491b584839022f29257ad859b8532d",
                "shasum": ""
            },
            "require": {
                "php": ">=5.3.3"
            },
            "suggest": {
                "ext-mbstring": "For best performance"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "1.1-dev"
                }
            },
            "autoload": {
                "psr-4": {
                    "Symfony\\Polyfill\\Mbstring\\": ""
                },
                "files": [
                    "bootstrap.php"
                ]
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "Nicolas Grekas",
                    "email": "p@tchwork.com"
                },
                {
                    "name": "Symfony Community",
                    "homepage": "https://symfony.com/contributors"
                }
            ],
            "description": "Symfony polyfill for the Mbstring extension",
            "homepage": "https://symfony.com",
            "keywords": [
                "compatibility",
                "mbstring",
                "polyfill",
                "portable",
                "shim"
            ],
            "time": "2016-01-20 09:13:37"
        },
        {
            "name": "symfony/polyfill-php56",
            "version": "v1.1.1",
            "source": {
                "type": "git",
                "url": "https://github.com/symfony/polyfill-php56.git",
                "reference": "4d891fff050101a53a4caabb03277284942d1ad9"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/symfony/polyfill-php56/zipball/4d891fff050101a53a4caabb03277284942d1ad9",
                "reference": "4d891fff050101a53a4caabb03277284942d1ad9",
                "shasum": ""
            },
            "require": {
                "php": ">=5.3.3",
                "symfony/polyfill-util": "~1.0"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "1.1-dev"
                }
            },
            "autoload": {
                "psr-4": {
                    "Symfony\\Polyfill\\Php56\\": ""
                },
                "files": [
                    "bootstrap.php"
                ]
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "Nicolas Grekas",
                    "email": "p@tchwork.com"
                },
                {
                    "name": "Symfony Community",
                    "homepage": "https://symfony.com/contributors"
                }
            ],
            "description": "Symfony polyfill backporting some PHP 5.6+ features to lower PHP versions",
            "homepage": "https://symfony.com",
            "keywords": [
                "compatibility",
                "polyfill",
                "portable",
                "shim"
            ],
            "time": "2016-01-20 09:13:37"
        },
        {
            "name": "symfony/polyfill-util",
            "version": "v1.1.1",
            "source": {
                "type": "git",
                "url": "https://github.com/symfony/polyfill-util.git",
                "reference": "8de62801aa12bc4dfcf85eef5d21981ae7bb3cc4"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/symfony/polyfill-util/zipball/8de62801aa12bc4dfcf85eef5d21981ae7bb3cc4",
                "reference": "8de62801aa12bc4dfcf85eef5d21981ae7bb3cc4",
                "shasum": ""
            },
            "require": {
                "php": ">=5.3.3"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "1.1-dev"
                }
            },
            "autoload": {
                "psr-4": {
                    "Symfony\\Polyfill\\Util\\": ""
                }
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "Nicolas Grekas",
                    "email": "p@tchwork.com"
                },
                {
                    "name": "Symfony Community",
                    "homepage": "https://symfony.com/contributors"
                }
            ],
            "description": "Symfony utilities for portability of PHP codes",
            "homepage": "https://symfony.com",
            "keywords": [
                "compat",
                "compatibility",
                "polyfill",
                "shim"
            ],
            "time": "2016-01-20 09:13:37"
        },
        {
            "name": "symfony/process",
            "version": "v3.0.4",
            "source": {
                "type": "git",
                "url": "https://github.com/symfony/process.git",
                "reference": "e6f1f98bbd355d209a992bfff45e7edfbd4a0776"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/symfony/process/zipball/e6f1f98bbd355d209a992bfff45e7edfbd4a0776",
                "reference": "e6f1f98bbd355d209a992bfff45e7edfbd4a0776",
                "shasum": ""
            },
            "require": {
                "php": ">=5.5.9"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "3.0-dev"
                }
            },
            "autoload": {
                "psr-4": {
                    "Symfony\\Component\\Process\\": ""
                },
                "exclude-from-classmap": [
                    "/Tests/"
                ]
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "Fabien Potencier",
                    "email": "fabien@symfony.com"
                },
                {
                    "name": "Symfony Community",
                    "homepage": "https://symfony.com/contributors"
                }
            ],
            "description": "Symfony Process Component",
            "homepage": "https://symfony.com",
            "time": "2016-03-30 10:41:14"
        },
        {
            "name": "symfony/routing",
            "version": "v3.0.4",
            "source": {
                "type": "git",
                "url": "https://github.com/symfony/routing.git",
                "reference": "d061b609f2d0769494c381ec92f5c5cc5e4a20aa"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/symfony/routing/zipball/d061b609f2d0769494c381ec92f5c5cc5e4a20aa",
                "reference": "d061b609f2d0769494c381ec92f5c5cc5e4a20aa",
                "shasum": ""
            },
            "require": {
                "php": ">=5.5.9"
            },
            "conflict": {
                "symfony/config": "<2.8"
            },
            "require-dev": {
                "doctrine/annotations": "~1.0",
                "doctrine/common": "~2.2",
                "psr/log": "~1.0",
                "symfony/config": "~2.8|~3.0",
                "symfony/expression-language": "~2.8|~3.0",
                "symfony/http-foundation": "~2.8|~3.0",
                "symfony/yaml": "~2.8|~3.0"
            },
            "suggest": {
                "doctrine/annotations": "For using the annotation loader",
                "symfony/config": "For using the all-in-one router or any loader",
                "symfony/dependency-injection": "For loading routes from a service",
                "symfony/expression-language": "For using expression matching",
                "symfony/http-foundation": "For using a Symfony Request object",
                "symfony/yaml": "For using the YAML loader"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "3.0-dev"
                }
            },
            "autoload": {
                "psr-4": {
                    "Symfony\\Component\\Routing\\": ""
                },
                "exclude-from-classmap": [
                    "/Tests/"
                ]
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "Fabien Potencier",
                    "email": "fabien@symfony.com"
                },
                {
                    "name": "Symfony Community",
                    "homepage": "https://symfony.com/contributors"
                }
            ],
            "description": "Symfony Routing Component",
            "homepage": "https://symfony.com",
            "keywords": [
                "router",
                "routing",
                "uri",
                "url"
            ],
            "time": "2016-03-23 13:23:25"
        },
        {
            "name": "symfony/translation",
            "version": "v3.0.4",
            "source": {
                "type": "git",
                "url": "https://github.com/symfony/translation.git",
                "reference": "f7a07af51ea067745a521dab1e3152044a2fb1f2"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/symfony/translation/zipball/f7a07af51ea067745a521dab1e3152044a2fb1f2",
                "reference": "f7a07af51ea067745a521dab1e3152044a2fb1f2",
                "shasum": ""
            },
            "require": {
                "php": ">=5.5.9",
                "symfony/polyfill-mbstring": "~1.0"
            },
            "conflict": {
                "symfony/config": "<2.8"
            },
            "require-dev": {
                "psr/log": "~1.0",
                "symfony/config": "~2.8|~3.0",
                "symfony/intl": "~2.8|~3.0",
                "symfony/yaml": "~2.8|~3.0"
            },
            "suggest": {
                "psr/log": "To use logging capability in translator",
                "symfony/config": "",
                "symfony/yaml": ""
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "3.0-dev"
                }
            },
            "autoload": {
                "psr-4": {
                    "Symfony\\Component\\Translation\\": ""
                },
                "exclude-from-classmap": [
                    "/Tests/"
                ]
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "Fabien Potencier",
                    "email": "fabien@symfony.com"
                },
                {
                    "name": "Symfony Community",
                    "homepage": "https://symfony.com/contributors"
                }
            ],
            "description": "Symfony Translation Component",
            "homepage": "https://symfony.com",
            "time": "2016-03-25 01:41:20"
        },
        {
            "name": "symfony/var-dumper",
            "version": "v3.0.4",
            "source": {
                "type": "git",
                "url": "https://github.com/symfony/var-dumper.git",
                "reference": "3841ed86527d18ee2c35fe4afb1b2fc60f8fae79"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/symfony/var-dumper/zipball/3841ed86527d18ee2c35fe4afb1b2fc60f8fae79",
                "reference": "3841ed86527d18ee2c35fe4afb1b2fc60f8fae79",
                "shasum": ""
            },
            "require": {
                "php": ">=5.5.9",
                "symfony/polyfill-mbstring": "~1.0"
            },
            "require-dev": {
                "twig/twig": "~1.20|~2.0"
            },
            "suggest": {
                "ext-symfony_debug": ""
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "3.0-dev"
                }
            },
            "autoload": {
                "files": [
                    "Resources/functions/dump.php"
                ],
                "psr-4": {
                    "Symfony\\Component\\VarDumper\\": ""
                },
                "exclude-from-classmap": [
                    "/Tests/"
                ]
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "Nicolas Grekas",
                    "email": "p@tchwork.com"
                },
                {
                    "name": "Symfony Community",
                    "homepage": "https://symfony.com/contributors"
                }
            ],
            "description": "Symfony mechanism for exploring and dumping PHP variables",
            "homepage": "https://symfony.com",
            "keywords": [
                "debug",
                "dump"
            ],
            "time": "2016-03-10 10:34:12"
        },
        {
            "name": "vlucas/phpdotenv",
            "version": "v2.2.0",
            "source": {
                "type": "git",
                "url": "https://github.com/vlucas/phpdotenv.git",
                "reference": "9caf304153dc2288e4970caec6f1f3b3bc205412"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/vlucas/phpdotenv/zipball/9caf304153dc2288e4970caec6f1f3b3bc205412",
                "reference": "9caf304153dc2288e4970caec6f1f3b3bc205412",
                "shasum": ""
            },
            "require": {
                "php": ">=5.3.9"
            },
            "require-dev": {
                "phpunit/phpunit": "^4.8|^5.0"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "2.2-dev"
                }
            },
            "autoload": {
                "psr-4": {
                    "Dotenv\\": "src/"
                }
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "BSD"
            ],
            "authors": [
                {
                    "name": "Vance Lucas",
                    "email": "vance@vancelucas.com",
                    "homepage": "http://www.vancelucas.com"
                }
            ],
            "description": "Loads environment variables from `.env` to `getenv()`, `$_ENV` and `$_SERVER` automagically.",
            "homepage": "http://github.com/vlucas/phpdotenv",
            "keywords": [
                "dotenv",
                "env",
                "environment"
            ],
            "time": "2015-12-29 15:10:30"
        }
    ],
    "packages-dev": [
        {
            "name": "doctrine/instantiator",
            "version": "1.0.5",
            "source": {
                "type": "git",
                "url": "https://github.com/doctrine/instantiator.git",
                "reference": "8e884e78f9f0eb1329e445619e04456e64d8051d"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/doctrine/instantiator/zipball/8e884e78f9f0eb1329e445619e04456e64d8051d",
                "reference": "8e884e78f9f0eb1329e445619e04456e64d8051d",
                "shasum": ""
            },
            "require": {
                "php": ">=5.3,<8.0-DEV"
            },
            "require-dev": {
                "athletic/athletic": "~0.1.8",
                "ext-pdo": "*",
                "ext-phar": "*",
                "phpunit/phpunit": "~4.0",
                "squizlabs/php_codesniffer": "~2.0"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "1.0.x-dev"
                }
            },
            "autoload": {
                "psr-4": {
                    "Doctrine\\Instantiator\\": "src/Doctrine/Instantiator/"
                }
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "Marco Pivetta",
                    "email": "ocramius@gmail.com",
                    "homepage": "http://ocramius.github.com/"
                }
            ],
            "description": "A small, lightweight utility to instantiate objects in PHP without invoking their constructors",
            "homepage": "https://github.com/doctrine/instantiator",
            "keywords": [
                "constructor",
                "instantiate"
            ],
            "time": "2015-06-14 21:17:01"
        },
        {
            "name": "fzaninotto/faker",
            "version": "v1.5.0",
            "source": {
                "type": "git",
                "url": "https://github.com/fzaninotto/Faker.git",
                "reference": "d0190b156bcca848d401fb80f31f504f37141c8d"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/fzaninotto/Faker/zipball/d0190b156bcca848d401fb80f31f504f37141c8d",
                "reference": "d0190b156bcca848d401fb80f31f504f37141c8d",
                "shasum": ""
            },
            "require": {
                "php": ">=5.3.3"
            },
            "require-dev": {
                "phpunit/phpunit": "~4.0",
                "squizlabs/php_codesniffer": "~1.5"
            },
            "suggest": {
                "ext-intl": "*"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "1.5.x-dev"
                }
            },
            "autoload": {
                "psr-4": {
                    "Faker\\": "src/Faker/"
                }
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "François Zaninotto"
                }
            ],
            "description": "Faker is a PHP library that generates fake data for you.",
            "keywords": [
                "data",
                "faker",
                "fixtures"
            ],
            "time": "2015-05-29 06:29:14"
        },
        {
            "name": "hamcrest/hamcrest-php",
            "version": "v1.2.2",
            "source": {
                "type": "git",
                "url": "https://github.com/hamcrest/hamcrest-php.git",
                "reference": "b37020aa976fa52d3de9aa904aa2522dc518f79c"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/hamcrest/hamcrest-php/zipball/b37020aa976fa52d3de9aa904aa2522dc518f79c",
                "reference": "b37020aa976fa52d3de9aa904aa2522dc518f79c",
                "shasum": ""
            },
            "require": {
                "php": ">=5.3.2"
            },
            "replace": {
                "cordoval/hamcrest-php": "*",
                "davedevelopment/hamcrest-php": "*",
                "kodova/hamcrest-php": "*"
            },
            "require-dev": {
                "phpunit/php-file-iterator": "1.3.3",
                "satooshi/php-coveralls": "dev-master"
            },
            "type": "library",
            "autoload": {
                "classmap": [
                    "hamcrest"
                ],
                "files": [
                    "hamcrest/Hamcrest.php"
                ]
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "BSD"
            ],
            "description": "This is the PHP port of Hamcrest Matchers",
            "keywords": [
                "test"
            ],
            "time": "2015-05-11 14:41:42"
        },
        {
            "name": "mockery/mockery",
            "version": "0.9.4",
            "source": {
                "type": "git",
                "url": "https://github.com/padraic/mockery.git",
                "reference": "70bba85e4aabc9449626651f48b9018ede04f86b"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/padraic/mockery/zipball/70bba85e4aabc9449626651f48b9018ede04f86b",
                "reference": "70bba85e4aabc9449626651f48b9018ede04f86b",
                "shasum": ""
            },
            "require": {
                "hamcrest/hamcrest-php": "~1.1",
                "lib-pcre": ">=7.0",
                "php": ">=5.3.2"
            },
            "require-dev": {
                "phpunit/phpunit": "~4.0"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "0.9.x-dev"
                }
            },
            "autoload": {
                "psr-0": {
                    "Mockery": "library/"
                }
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "BSD-3-Clause"
            ],
            "authors": [
                {
                    "name": "Pádraic Brady",
                    "email": "padraic.brady@gmail.com",
                    "homepage": "http://blog.astrumfutura.com"
                },
                {
                    "name": "Dave Marshall",
                    "email": "dave.marshall@atstsolutions.co.uk",
                    "homepage": "http://davedevelopment.co.uk"
                }
            ],
            "description": "Mockery is a simple yet flexible PHP mock object framework for use in unit testing with PHPUnit, PHPSpec or any other testing framework. Its core goal is to offer a test double framework with a succinct API capable of clearly defining all possible object operations and interactions using a human readable Domain Specific Language (DSL). Designed as a drop in alternative to PHPUnit's phpunit-mock-objects library, Mockery is easy to integrate with PHPUnit and can operate alongside phpunit-mock-objects without the World ending.",
            "homepage": "http://github.com/padraic/mockery",
            "keywords": [
                "BDD",
                "TDD",
                "library",
                "mock",
                "mock objects",
                "mockery",
                "stub",
                "test",
                "test double",
                "testing"
            ],
            "time": "2015-04-02 19:54:00"
        },
        {
            "name": "phpdocumentor/reflection-docblock",
            "version": "2.0.4",
            "source": {
                "type": "git",
                "url": "https://github.com/phpDocumentor/ReflectionDocBlock.git",
                "reference": "d68dbdc53dc358a816f00b300704702b2eaff7b8"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/phpDocumentor/ReflectionDocBlock/zipball/d68dbdc53dc358a816f00b300704702b2eaff7b8",
                "reference": "d68dbdc53dc358a816f00b300704702b2eaff7b8",
                "shasum": ""
            },
            "require": {
                "php": ">=5.3.3"
            },
            "require-dev": {
                "phpunit/phpunit": "~4.0"
            },
            "suggest": {
                "dflydev/markdown": "~1.0",
                "erusev/parsedown": "~1.0"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "2.0.x-dev"
                }
            },
            "autoload": {
                "psr-0": {
                    "phpDocumentor": [
                        "src/"
                    ]
                }
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "Mike van Riel",
                    "email": "mike.vanriel@naenius.com"
                }
            ],
            "time": "2015-02-03 12:10:50"
        },
        {
            "name": "phpspec/prophecy",
            "version": "v1.6.0",
            "source": {
                "type": "git",
                "url": "https://github.com/phpspec/prophecy.git",
                "reference": "3c91bdf81797d725b14cb62906f9a4ce44235972"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/phpspec/prophecy/zipball/3c91bdf81797d725b14cb62906f9a4ce44235972",
                "reference": "3c91bdf81797d725b14cb62906f9a4ce44235972",
                "shasum": ""
            },
            "require": {
                "doctrine/instantiator": "^1.0.2",
                "php": "^5.3|^7.0",
                "phpdocumentor/reflection-docblock": "~2.0",
                "sebastian/comparator": "~1.1",
                "sebastian/recursion-context": "~1.0"
            },
            "require-dev": {
                "phpspec/phpspec": "~2.0"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "1.5.x-dev"
                }
            },
            "autoload": {
                "psr-0": {
                    "Prophecy\\": "src/"
                }
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "Konstantin Kudryashov",
                    "email": "ever.zet@gmail.com",
                    "homepage": "http://everzet.com"
                },
                {
                    "name": "Marcello Duarte",
                    "email": "marcello.duarte@gmail.com"
                }
            ],
            "description": "Highly opinionated mocking framework for PHP 5.3+",
            "homepage": "https://github.com/phpspec/prophecy",
            "keywords": [
                "Double",
                "Dummy",
                "fake",
                "mock",
                "spy",
                "stub"
            ],
            "time": "2016-02-15 07:46:21"
        },
        {
            "name": "phpunit/php-code-coverage",
            "version": "2.2.4",
            "source": {
                "type": "git",
                "url": "https://github.com/sebastianbergmann/php-code-coverage.git",
                "reference": "eabf68b476ac7d0f73793aada060f1c1a9bf8979"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/sebastianbergmann/php-code-coverage/zipball/eabf68b476ac7d0f73793aada060f1c1a9bf8979",
                "reference": "eabf68b476ac7d0f73793aada060f1c1a9bf8979",
                "shasum": ""
            },
            "require": {
                "php": ">=5.3.3",
                "phpunit/php-file-iterator": "~1.3",
                "phpunit/php-text-template": "~1.2",
                "phpunit/php-token-stream": "~1.3",
                "sebastian/environment": "^1.3.2",
                "sebastian/version": "~1.0"
            },
            "require-dev": {
                "ext-xdebug": ">=2.1.4",
                "phpunit/phpunit": "~4"
            },
            "suggest": {
                "ext-dom": "*",
                "ext-xdebug": ">=2.2.1",
                "ext-xmlwriter": "*"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "2.2.x-dev"
                }
            },
            "autoload": {
                "classmap": [
                    "src/"
                ]
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "BSD-3-Clause"
            ],
            "authors": [
                {
                    "name": "Sebastian Bergmann",
                    "email": "sb@sebastian-bergmann.de",
                    "role": "lead"
                }
            ],
            "description": "Library that provides collection, processing, and rendering functionality for PHP code coverage information.",
            "homepage": "https://github.com/sebastianbergmann/php-code-coverage",
            "keywords": [
                "coverage",
                "testing",
                "xunit"
            ],
            "time": "2015-10-06 15:47:00"
        },
        {
            "name": "phpunit/php-file-iterator",
            "version": "1.4.1",
            "source": {
                "type": "git",
                "url": "https://github.com/sebastianbergmann/php-file-iterator.git",
                "reference": "6150bf2c35d3fc379e50c7602b75caceaa39dbf0"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/sebastianbergmann/php-file-iterator/zipball/6150bf2c35d3fc379e50c7602b75caceaa39dbf0",
                "reference": "6150bf2c35d3fc379e50c7602b75caceaa39dbf0",
                "shasum": ""
            },
            "require": {
                "php": ">=5.3.3"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "1.4.x-dev"
                }
            },
            "autoload": {
                "classmap": [
                    "src/"
                ]
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "BSD-3-Clause"
            ],
            "authors": [
                {
                    "name": "Sebastian Bergmann",
                    "email": "sb@sebastian-bergmann.de",
                    "role": "lead"
                }
            ],
            "description": "FilterIterator implementation that filters files based on a list of suffixes.",
            "homepage": "https://github.com/sebastianbergmann/php-file-iterator/",
            "keywords": [
                "filesystem",
                "iterator"
            ],
            "time": "2015-06-21 13:08:43"
        },
        {
            "name": "phpunit/php-text-template",
            "version": "1.2.1",
            "source": {
                "type": "git",
                "url": "https://github.com/sebastianbergmann/php-text-template.git",
                "reference": "31f8b717e51d9a2afca6c9f046f5d69fc27c8686"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/sebastianbergmann/php-text-template/zipball/31f8b717e51d9a2afca6c9f046f5d69fc27c8686",
                "reference": "31f8b717e51d9a2afca6c9f046f5d69fc27c8686",
                "shasum": ""
            },
            "require": {
                "php": ">=5.3.3"
            },
            "type": "library",
            "autoload": {
                "classmap": [
                    "src/"
                ]
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "BSD-3-Clause"
            ],
            "authors": [
                {
                    "name": "Sebastian Bergmann",
                    "email": "sebastian@phpunit.de",
                    "role": "lead"
                }
            ],
            "description": "Simple template engine.",
            "homepage": "https://github.com/sebastianbergmann/php-text-template/",
            "keywords": [
                "template"
            ],
            "time": "2015-06-21 13:50:34"
        },
        {
            "name": "phpunit/php-timer",
            "version": "1.0.7",
            "source": {
                "type": "git",
                "url": "https://github.com/sebastianbergmann/php-timer.git",
                "reference": "3e82f4e9fc92665fafd9157568e4dcb01d014e5b"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/sebastianbergmann/php-timer/zipball/3e82f4e9fc92665fafd9157568e4dcb01d014e5b",
                "reference": "3e82f4e9fc92665fafd9157568e4dcb01d014e5b",
                "shasum": ""
            },
            "require": {
                "php": ">=5.3.3"
            },
            "type": "library",
            "autoload": {
                "classmap": [
                    "src/"
                ]
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "BSD-3-Clause"
            ],
            "authors": [
                {
                    "name": "Sebastian Bergmann",
                    "email": "sb@sebastian-bergmann.de",
                    "role": "lead"
                }
            ],
            "description": "Utility class for timing",
            "homepage": "https://github.com/sebastianbergmann/php-timer/",
            "keywords": [
                "timer"
            ],
            "time": "2015-06-21 08:01:12"
        },
        {
            "name": "phpunit/php-token-stream",
            "version": "1.4.8",
            "source": {
                "type": "git",
                "url": "https://github.com/sebastianbergmann/php-token-stream.git",
                "reference": "3144ae21711fb6cac0b1ab4cbe63b75ce3d4e8da"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/sebastianbergmann/php-token-stream/zipball/3144ae21711fb6cac0b1ab4cbe63b75ce3d4e8da",
                "reference": "3144ae21711fb6cac0b1ab4cbe63b75ce3d4e8da",
                "shasum": ""
            },
            "require": {
                "ext-tokenizer": "*",
                "php": ">=5.3.3"
            },
            "require-dev": {
                "phpunit/phpunit": "~4.2"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "1.4-dev"
                }
            },
            "autoload": {
                "classmap": [
                    "src/"
                ]
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "BSD-3-Clause"
            ],
            "authors": [
                {
                    "name": "Sebastian Bergmann",
                    "email": "sebastian@phpunit.de"
                }
            ],
            "description": "Wrapper around PHP's tokenizer extension.",
            "homepage": "https://github.com/sebastianbergmann/php-token-stream/",
            "keywords": [
                "tokenizer"
            ],
            "time": "2015-09-15 10:49:45"
        },
        {
            "name": "phpunit/phpunit",
            "version": "4.8.24",
            "source": {
                "type": "git",
                "url": "https://github.com/sebastianbergmann/phpunit.git",
                "reference": "a1066c562c52900a142a0e2bbf0582994671385e"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/sebastianbergmann/phpunit/zipball/a1066c562c52900a142a0e2bbf0582994671385e",
                "reference": "a1066c562c52900a142a0e2bbf0582994671385e",
                "shasum": ""
            },
            "require": {
                "ext-dom": "*",
                "ext-json": "*",
                "ext-pcre": "*",
                "ext-reflection": "*",
                "ext-spl": "*",
                "php": ">=5.3.3",
                "phpspec/prophecy": "^1.3.1",
                "phpunit/php-code-coverage": "~2.1",
                "phpunit/php-file-iterator": "~1.4",
                "phpunit/php-text-template": "~1.2",
                "phpunit/php-timer": ">=1.0.6",
                "phpunit/phpunit-mock-objects": "~2.3",
                "sebastian/comparator": "~1.1",
                "sebastian/diff": "~1.2",
                "sebastian/environment": "~1.3",
                "sebastian/exporter": "~1.2",
                "sebastian/global-state": "~1.0",
                "sebastian/version": "~1.0",
                "symfony/yaml": "~2.1|~3.0"
            },
            "suggest": {
                "phpunit/php-invoker": "~1.1"
            },
            "bin": [
                "phpunit"
            ],
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "4.8.x-dev"
                }
            },
            "autoload": {
                "classmap": [
                    "src/"
                ]
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "BSD-3-Clause"
            ],
            "authors": [
                {
                    "name": "Sebastian Bergmann",
                    "email": "sebastian@phpunit.de",
                    "role": "lead"
                }
            ],
            "description": "The PHP Unit Testing framework.",
            "homepage": "https://phpunit.de/",
            "keywords": [
                "phpunit",
                "testing",
                "xunit"
            ],
            "time": "2016-03-14 06:16:08"
        },
        {
            "name": "phpunit/phpunit-mock-objects",
            "version": "2.3.8",
            "source": {
                "type": "git",
                "url": "https://github.com/sebastianbergmann/phpunit-mock-objects.git",
                "reference": "ac8e7a3db35738d56ee9a76e78a4e03d97628983"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/sebastianbergmann/phpunit-mock-objects/zipball/ac8e7a3db35738d56ee9a76e78a4e03d97628983",
                "reference": "ac8e7a3db35738d56ee9a76e78a4e03d97628983",
                "shasum": ""
            },
            "require": {
                "doctrine/instantiator": "^1.0.2",
                "php": ">=5.3.3",
                "phpunit/php-text-template": "~1.2",
                "sebastian/exporter": "~1.2"
            },
            "require-dev": {
                "phpunit/phpunit": "~4.4"
            },
            "suggest": {
                "ext-soap": "*"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "2.3.x-dev"
                }
            },
            "autoload": {
                "classmap": [
                    "src/"
                ]
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "BSD-3-Clause"
            ],
            "authors": [
                {
                    "name": "Sebastian Bergmann",
                    "email": "sb@sebastian-bergmann.de",
                    "role": "lead"
                }
            ],
            "description": "Mock Object library for PHPUnit",
            "homepage": "https://github.com/sebastianbergmann/phpunit-mock-objects/",
            "keywords": [
                "mock",
                "xunit"
            ],
            "time": "2015-10-02 06:51:40"
        },
        {
            "name": "sebastian/comparator",
            "version": "1.2.0",
            "source": {
                "type": "git",
                "url": "https://github.com/sebastianbergmann/comparator.git",
                "reference": "937efb279bd37a375bcadf584dec0726f84dbf22"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/sebastianbergmann/comparator/zipball/937efb279bd37a375bcadf584dec0726f84dbf22",
                "reference": "937efb279bd37a375bcadf584dec0726f84dbf22",
                "shasum": ""
            },
            "require": {
                "php": ">=5.3.3",
                "sebastian/diff": "~1.2",
                "sebastian/exporter": "~1.2"
            },
            "require-dev": {
                "phpunit/phpunit": "~4.4"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "1.2.x-dev"
                }
            },
            "autoload": {
                "classmap": [
                    "src/"
                ]
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "BSD-3-Clause"
            ],
            "authors": [
                {
                    "name": "Jeff Welch",
                    "email": "whatthejeff@gmail.com"
                },
                {
                    "name": "Volker Dusch",
                    "email": "github@wallbash.com"
                },
                {
                    "name": "Bernhard Schussek",
                    "email": "bschussek@2bepublished.at"
                },
                {
                    "name": "Sebastian Bergmann",
                    "email": "sebastian@phpunit.de"
                }
            ],
            "description": "Provides the functionality to compare PHP values for equality",
            "homepage": "http://www.github.com/sebastianbergmann/comparator",
            "keywords": [
                "comparator",
                "compare",
                "equality"
            ],
            "time": "2015-07-26 15:48:44"
        },
        {
            "name": "sebastian/diff",
            "version": "1.4.1",
            "source": {
                "type": "git",
                "url": "https://github.com/sebastianbergmann/diff.git",
                "reference": "13edfd8706462032c2f52b4b862974dd46b71c9e"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/sebastianbergmann/diff/zipball/13edfd8706462032c2f52b4b862974dd46b71c9e",
                "reference": "13edfd8706462032c2f52b4b862974dd46b71c9e",
                "shasum": ""
            },
            "require": {
                "php": ">=5.3.3"
            },
            "require-dev": {
                "phpunit/phpunit": "~4.8"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "1.4-dev"
                }
            },
            "autoload": {
                "classmap": [
                    "src/"
                ]
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "BSD-3-Clause"
            ],
            "authors": [
                {
                    "name": "Kore Nordmann",
                    "email": "mail@kore-nordmann.de"
                },
                {
                    "name": "Sebastian Bergmann",
                    "email": "sebastian@phpunit.de"
                }
            ],
            "description": "Diff implementation",
            "homepage": "https://github.com/sebastianbergmann/diff",
            "keywords": [
                "diff"
            ],
            "time": "2015-12-08 07:14:41"
        },
        {
            "name": "sebastian/environment",
            "version": "1.3.5",
            "source": {
                "type": "git",
                "url": "https://github.com/sebastianbergmann/environment.git",
                "reference": "dc7a29032cf72b54f36dac15a1ca5b3a1b6029bf"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/sebastianbergmann/environment/zipball/dc7a29032cf72b54f36dac15a1ca5b3a1b6029bf",
                "reference": "dc7a29032cf72b54f36dac15a1ca5b3a1b6029bf",
                "shasum": ""
            },
            "require": {
                "php": ">=5.3.3"
            },
            "require-dev": {
                "phpunit/phpunit": "~4.4"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "1.3.x-dev"
                }
            },
            "autoload": {
                "classmap": [
                    "src/"
                ]
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "BSD-3-Clause"
            ],
            "authors": [
                {
                    "name": "Sebastian Bergmann",
                    "email": "sebastian@phpunit.de"
                }
            ],
            "description": "Provides functionality to handle HHVM/PHP environments",
            "homepage": "http://www.github.com/sebastianbergmann/environment",
            "keywords": [
                "Xdebug",
                "environment",
                "hhvm"
            ],
            "time": "2016-02-26 18:40:46"
        },
        {
            "name": "sebastian/exporter",
            "version": "1.2.1",
            "source": {
                "type": "git",
                "url": "https://github.com/sebastianbergmann/exporter.git",
                "reference": "7ae5513327cb536431847bcc0c10edba2701064e"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/sebastianbergmann/exporter/zipball/7ae5513327cb536431847bcc0c10edba2701064e",
                "reference": "7ae5513327cb536431847bcc0c10edba2701064e",
                "shasum": ""
            },
            "require": {
                "php": ">=5.3.3",
                "sebastian/recursion-context": "~1.0"
            },
            "require-dev": {
                "phpunit/phpunit": "~4.4"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "1.2.x-dev"
                }
            },
            "autoload": {
                "classmap": [
                    "src/"
                ]
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "BSD-3-Clause"
            ],
            "authors": [
                {
                    "name": "Jeff Welch",
                    "email": "whatthejeff@gmail.com"
                },
                {
                    "name": "Volker Dusch",
                    "email": "github@wallbash.com"
                },
                {
                    "name": "Bernhard Schussek",
                    "email": "bschussek@2bepublished.at"
                },
                {
                    "name": "Sebastian Bergmann",
                    "email": "sebastian@phpunit.de"
                },
                {
                    "name": "Adam Harvey",
                    "email": "aharvey@php.net"
                }
            ],
            "description": "Provides the functionality to export PHP variables for visualization",
            "homepage": "http://www.github.com/sebastianbergmann/exporter",
            "keywords": [
                "export",
                "exporter"
            ],
            "time": "2015-06-21 07:55:53"
        },
        {
            "name": "sebastian/global-state",
            "version": "1.1.1",
            "source": {
                "type": "git",
                "url": "https://github.com/sebastianbergmann/global-state.git",
                "reference": "bc37d50fea7d017d3d340f230811c9f1d7280af4"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/sebastianbergmann/global-state/zipball/bc37d50fea7d017d3d340f230811c9f1d7280af4",
                "reference": "bc37d50fea7d017d3d340f230811c9f1d7280af4",
                "shasum": ""
            },
            "require": {
                "php": ">=5.3.3"
            },
            "require-dev": {
                "phpunit/phpunit": "~4.2"
            },
            "suggest": {
                "ext-uopz": "*"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "1.0-dev"
                }
            },
            "autoload": {
                "classmap": [
                    "src/"
                ]
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "BSD-3-Clause"
            ],
            "authors": [
                {
                    "name": "Sebastian Bergmann",
                    "email": "sebastian@phpunit.de"
                }
            ],
            "description": "Snapshotting of global state",
            "homepage": "http://www.github.com/sebastianbergmann/global-state",
            "keywords": [
                "global state"
            ],
            "time": "2015-10-12 03:26:01"
        },
        {
            "name": "sebastian/recursion-context",
            "version": "1.0.2",
            "source": {
                "type": "git",
                "url": "https://github.com/sebastianbergmann/recursion-context.git",
                "reference": "913401df809e99e4f47b27cdd781f4a258d58791"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/sebastianbergmann/recursion-context/zipball/913401df809e99e4f47b27cdd781f4a258d58791",
                "reference": "913401df809e99e4f47b27cdd781f4a258d58791",
                "shasum": ""
            },
            "require": {
                "php": ">=5.3.3"
            },
            "require-dev": {
                "phpunit/phpunit": "~4.4"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "1.0.x-dev"
                }
            },
            "autoload": {
                "classmap": [
                    "src/"
                ]
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "BSD-3-Clause"
            ],
            "authors": [
                {
                    "name": "Jeff Welch",
                    "email": "whatthejeff@gmail.com"
                },
                {
                    "name": "Sebastian Bergmann",
                    "email": "sebastian@phpunit.de"
                },
                {
                    "name": "Adam Harvey",
                    "email": "aharvey@php.net"
                }
            ],
            "description": "Provides functionality to recursively process PHP variables",
            "homepage": "http://www.github.com/sebastianbergmann/recursion-context",
            "time": "2015-11-11 19:50:13"
        },
        {
            "name": "sebastian/version",
            "version": "1.0.6",
            "source": {
                "type": "git",
                "url": "https://github.com/sebastianbergmann/version.git",
                "reference": "58b3a85e7999757d6ad81c787a1fbf5ff6c628c6"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/sebastianbergmann/version/zipball/58b3a85e7999757d6ad81c787a1fbf5ff6c628c6",
                "reference": "58b3a85e7999757d6ad81c787a1fbf5ff6c628c6",
                "shasum": ""
            },
            "type": "library",
            "autoload": {
                "classmap": [
                    "src/"
                ]
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "BSD-3-Clause"
            ],
            "authors": [
                {
                    "name": "Sebastian Bergmann",
                    "email": "sebastian@phpunit.de",
                    "role": "lead"
                }
            ],
            "description": "Library that helps with managing the version number of Git-hosted PHP projects",
            "homepage": "https://github.com/sebastianbergmann/version",
            "time": "2015-06-21 13:59:46"
        },
        {
            "name": "symfony/css-selector",
            "version": "v3.0.4",
            "source": {
                "type": "git",
                "url": "https://github.com/symfony/css-selector.git",
                "reference": "65e764f404685f2dc20c057e889b3ad04b2e2db0"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/symfony/css-selector/zipball/65e764f404685f2dc20c057e889b3ad04b2e2db0",
                "reference": "65e764f404685f2dc20c057e889b3ad04b2e2db0",
                "shasum": ""
            },
            "require": {
                "php": ">=5.5.9"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "3.0-dev"
                }
            },
            "autoload": {
                "psr-4": {
                    "Symfony\\Component\\CssSelector\\": ""
                },
                "exclude-from-classmap": [
                    "/Tests/"
                ]
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "Jean-François Simon",
                    "email": "jeanfrancois.simon@sensiolabs.com"
                },
                {
                    "name": "Fabien Potencier",
                    "email": "fabien@symfony.com"
                },
                {
                    "name": "Symfony Community",
                    "homepage": "https://symfony.com/contributors"
                }
            ],
            "description": "Symfony CssSelector Component",
            "homepage": "https://symfony.com",
            "time": "2016-03-04 07:55:57"
        },
        {
            "name": "symfony/dom-crawler",
            "version": "v3.0.4",
            "source": {
                "type": "git",
                "url": "https://github.com/symfony/dom-crawler.git",
                "reference": "18a06d7a9af41718c20764a674a0ebba3bc40d1f"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/symfony/dom-crawler/zipball/18a06d7a9af41718c20764a674a0ebba3bc40d1f",
                "reference": "18a06d7a9af41718c20764a674a0ebba3bc40d1f",
                "shasum": ""
            },
            "require": {
                "php": ">=5.5.9",
                "symfony/polyfill-mbstring": "~1.0"
            },
            "require-dev": {
                "symfony/css-selector": "~2.8|~3.0"
            },
            "suggest": {
                "symfony/css-selector": ""
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "3.0-dev"
                }
            },
            "autoload": {
                "psr-4": {
                    "Symfony\\Component\\DomCrawler\\": ""
                },
                "exclude-from-classmap": [
                    "/Tests/"
                ]
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "Fabien Potencier",
                    "email": "fabien@symfony.com"
                },
                {
                    "name": "Symfony Community",
                    "homepage": "https://symfony.com/contributors"
                }
            ],
            "description": "Symfony DomCrawler Component",
            "homepage": "https://symfony.com",
            "time": "2016-03-23 13:23:25"
        },
        {
            "name": "symfony/yaml",
            "version": "v3.0.4",
            "source": {
                "type": "git",
                "url": "https://github.com/symfony/yaml.git",
                "reference": "0047c8366744a16de7516622c5b7355336afae96"
            },
            "dist": {
                "type": "zip",
                "url": "https://api.github.com/repos/symfony/yaml/zipball/0047c8366744a16de7516622c5b7355336afae96",
                "reference": "0047c8366744a16de7516622c5b7355336afae96",
                "shasum": ""
            },
            "require": {
                "php": ">=5.5.9"
            },
            "type": "library",
            "extra": {
                "branch-alias": {
                    "dev-master": "3.0-dev"
                }
            },
            "autoload": {
                "psr-4": {
                    "Symfony\\Component\\Yaml\\": ""
                },
                "exclude-from-classmap": [
                    "/Tests/"
                ]
            },
            "notification-url": "https://packagist.org/downloads/",
            "license": [
                "MIT"
            ],
            "authors": [
                {
                    "name": "Fabien Potencier",
                    "email": "fabien@symfony.com"
                },
                {
                    "name": "Symfony Community",
                    "homepage": "https://symfony.com/contributors"
                }
            ],
            "description": "Symfony Yaml Component",
            "homepage": "https://symfony.com",
            "time": "2016-03-04 07:55:57"
        }
    ],
    "aliases": [],
    "minimum-stability": "stable",
    "stability-flags": {
        "pear2/net_transmitter": 15,
        "pear2/net_routeros": 10
    },
    "prefer-stable": false,
    "prefer-lowest": false,
    "platform": {
        "php": ">=5.5.9"
    },
    "platform-dev": []
}


File: /config\app.php
<?php

return [

    /*
    |--------------------------------------------------------------------------
    | Application Environment
    |--------------------------------------------------------------------------
    |
    | This value determines the "environment" your application is currently
    | running in. This may determine how you prefer to configure various
    | services your application utilizes. Set this in your ".env" file.
    |
    */

    'env' => env('APP_ENV', 'production'),

    /*
    |--------------------------------------------------------------------------
    | Application Debug Mode
    |--------------------------------------------------------------------------
    |
    | When your application is in debug mode, detailed error messages with
    | stack traces will be shown on every error that occurs within your
    | application. If disabled, a simple generic error page is shown.
    |
    */

    'debug' => env('APP_DEBUG', false),

    /*
    |--------------------------------------------------------------------------
    | Application URL
    |--------------------------------------------------------------------------
    |
    | This URL is used by the console to properly generate URLs when using
    | the Artisan command line tool. You should set this to the root of
    | your application so that it is used when running Artisan tasks.
    |
    */

    'url' => env('APP_URL', 'http://localhost'),

    /*
    |--------------------------------------------------------------------------
    | Application Timezone
    |--------------------------------------------------------------------------
    |
    | Here you may specify the default timezone for your application, which
    | will be used by the PHP date and date-time functions. We have gone
    | ahead and set this to a sensible default for you out of the box.
    |
    */

    'timezone' => 'UTC',

    /*
    |--------------------------------------------------------------------------
    | Application Locale Configuration
    |--------------------------------------------------------------------------
    |
    | The application locale determines the default locale that will be used
    | by the translation service provider. You are free to set this value
    | to any of the locales which will be supported by the application.
    |
    */

    'locale' => 'en',

    /*
    |--------------------------------------------------------------------------
    | Application Fallback Locale
    |--------------------------------------------------------------------------
    |
    | The fallback locale determines the locale to use when the current one
    | is not available. You may change the value to correspond to any of
    | the language folders that are provided through your application.
    |
    */

    'fallback_locale' => 'en',

    /*
    |--------------------------------------------------------------------------
    | Encryption Key
    |--------------------------------------------------------------------------
    |
    | This key is used by the Illuminate encrypter service and should be set
    | to a random, 32 character string, otherwise these encrypted strings
    | will not be safe. Please do this before deploying an application!
    |
    */

    'key' => env('APP_KEY'),

    'cipher' => 'AES-256-CBC',

    /*
    |--------------------------------------------------------------------------
    | Logging Configuration
    |--------------------------------------------------------------------------
    |
    | Here you may configure the log settings for your application. Out of
    | the box, Laravel uses the Monolog PHP logging library. This gives
    | you a variety of powerful log handlers / formatters to utilize.
    |
    | Available Settings: "single", "daily", "syslog", "errorlog"
    |
    */

    'log' => env('APP_LOG', 'single'),

    /*
    |--------------------------------------------------------------------------
    | Autoloaded Service Providers
    |--------------------------------------------------------------------------
    |
    | The service providers listed here will be automatically loaded on the
    | request to your application. Feel free to add your own services to
    | this array to grant expanded functionality to your applications.
    |
    */

    'providers' => [

        /*
         * Laravel Framework Service Providers...
         */
        Illuminate\Auth\AuthServiceProvider::class,
        Illuminate\Broadcasting\BroadcastServiceProvider::class,
        Illuminate\Bus\BusServiceProvider::class,
        Illuminate\Cache\CacheServiceProvider::class,
        Illuminate\Foundation\Providers\ConsoleSupportServiceProvider::class,
        Illuminate\Cookie\CookieServiceProvider::class,
        Illuminate\Database\DatabaseServiceProvider::class,
        Illuminate\Encryption\EncryptionServiceProvider::class,
        Illuminate\Filesystem\FilesystemServiceProvider::class,
        Illuminate\Foundation\Providers\FoundationServiceProvider::class,
        Illuminate\Hashing\HashServiceProvider::class,
        Illuminate\Mail\MailServiceProvider::class,
        Illuminate\Pagination\PaginationServiceProvider::class,
        Illuminate\Pipeline\PipelineServiceProvider::class,
        Illuminate\Queue\QueueServiceProvider::class,
        Illuminate\Redis\RedisServiceProvider::class,
        Illuminate\Auth\Passwords\PasswordResetServiceProvider::class,
        Illuminate\Session\SessionServiceProvider::class,
        Illuminate\Translation\TranslationServiceProvider::class,
        Illuminate\Validation\ValidationServiceProvider::class,
        Illuminate\View\ViewServiceProvider::class,

        /*
         * Application Service Providers...
         */
        App\Providers\AppServiceProvider::class,
        App\Providers\AuthServiceProvider::class,
        App\Providers\EventServiceProvider::class,
        App\Providers\RouteServiceProvider::class,

    ],

    /*
    |--------------------------------------------------------------------------
    | Class Aliases
    |--------------------------------------------------------------------------
    |
    | This array of class aliases will be registered when this application
    | is started. However, feel free to register as many as you wish as
    | the aliases are "lazy" loaded so they don't hinder performance.
    |
    */

    'aliases' => [

        'App' => Illuminate\Support\Facades\App::class,
        'Artisan' => Illuminate\Support\Facades\Artisan::class,
        'Auth' => Illuminate\Support\Facades\Auth::class,
        'Blade' => Illuminate\Support\Facades\Blade::class,
        'Cache' => Illuminate\Support\Facades\Cache::class,
        'Config' => Illuminate\Support\Facades\Config::class,
        'Cookie' => Illuminate\Support\Facades\Cookie::class,
        'Crypt' => Illuminate\Support\Facades\Crypt::class,
        'DB' => Illuminate\Support\Facades\DB::class,
        'Eloquent' => Illuminate\Database\Eloquent\Model::class,
        'Event' => Illuminate\Support\Facades\Event::class,
        'File' => Illuminate\Support\Facades\File::class,
        'Gate' => Illuminate\Support\Facades\Gate::class,
        'Hash' => Illuminate\Support\Facades\Hash::class,
        'Lang' => Illuminate\Support\Facades\Lang::class,
        'Log' => Illuminate\Support\Facades\Log::class,
        'Mail' => Illuminate\Support\Facades\Mail::class,
        'Password' => Illuminate\Support\Facades\Password::class,
        'Queue' => Illuminate\Support\Facades\Queue::class,
        'Redirect' => Illuminate\Support\Facades\Redirect::class,
        'Redis' => Illuminate\Support\Facades\Redis::class,
        'Request' => Illuminate\Support\Facades\Request::class,
        'Response' => Illuminate\Support\Facades\Response::class,
        'Route' => Illuminate\Support\Facades\Route::class,
        'Schema' => Illuminate\Support\Facades\Schema::class,
        'Session' => Illuminate\Support\Facades\Session::class,
        'Storage' => Illuminate\Support\Facades\Storage::class,
        'URL' => Illuminate\Support\Facades\URL::class,
        'Validator' => Illuminate\Support\Facades\Validator::class,
        'View' => Illuminate\Support\Facades\View::class,

    ],

];


File: /config\auth.php
<?php

return [

    /*
    |--------------------------------------------------------------------------
    | Authentication Defaults
    |--------------------------------------------------------------------------
    |
    | This option controls the default authentication "guard" and password
    | reset options for your application. You may change these defaults
    | as required, but they're a perfect start for most applications.
    |
    */

    'defaults' => [
        'guard' => 'web',
        'passwords' => 'users',
    ],

    /*
    |--------------------------------------------------------------------------
    | Authentication Guards
    |--------------------------------------------------------------------------
    |
    | Next, you may define every authentication guard for your application.
    | Of course, a great default configuration has been defined for you
    | here which uses session storage and the Eloquent user provider.
    |
    | All authentication drivers have a user provider. This defines how the
    | users are actually retrieved out of your database or other storage
    | mechanisms used by this application to persist your user's data.
    |
    | Supported: "session", "token"
    |
    */

    'guards' => [
        'web' => [
            'driver' => 'session',
            'provider' => 'users',
        ],

        'api' => [
            'driver' => 'token',
            'provider' => 'users',
        ],
    ],

    /*
    |--------------------------------------------------------------------------
    | User Providers
    |--------------------------------------------------------------------------
    |
    | All authentication drivers have a user provider. This defines how the
    | users are actually retrieved out of your database or other storage
    | mechanisms used by this application to persist your user's data.
    |
    | If you have multiple user tables or models you may configure multiple
    | sources which represent each model / table. These sources may then
    | be assigned to any extra authentication guards you have defined.
    |
    | Supported: "database", "eloquent"
    |
    */

    'providers' => [
        'users' => [
            'driver' => 'eloquent',
            'model' => App\User::class,
        ],

        // 'users' => [
        //     'driver' => 'database',
        //     'table' => 'users',
        // ],
    ],

    /*
    |--------------------------------------------------------------------------
    | Resetting Passwords
    |--------------------------------------------------------------------------
    |
    | Here you may set the options for resetting passwords including the view
    | that is your password reset e-mail. You may also set the name of the
    | table that maintains all of the reset tokens for your application.
    |
    | You may specify multiple password reset configurations if you have more
    | than one user table or model in the application and you want to have
    | separate password reset settings based on the specific user types.
    |
    | The expire time is the number of minutes that the reset token should be
    | considered valid. This security feature keeps tokens short-lived so
    | they have less time to be guessed. You may change this as needed.
    |
    */

    'passwords' => [
        'users' => [
            'provider' => 'users',
            'email' => 'auth.emails.password',
            'table' => 'password_resets',
            'expire' => 60,
        ],
    ],

];


File: /config\broadcasting.php
<?php

return [

    /*
    |--------------------------------------------------------------------------
    | Default Broadcaster
    |--------------------------------------------------------------------------
    |
    | This option controls the default broadcaster that will be used by the
    | framework when an event needs to be broadcast. You may set this to
    | any of the connections defined in the "connections" array below.
    |
    */

    'default' => env('BROADCAST_DRIVER', 'pusher'),

    /*
    |--------------------------------------------------------------------------
    | Broadcast Connections
    |--------------------------------------------------------------------------
    |
    | Here you may define all of the broadcast connections that will be used
    | to broadcast events to other systems or over websockets. Samples of
    | each available type of connection are provided inside this array.
    |
    */

    'connections' => [

        'pusher' => [
            'driver' => 'pusher',
            'key' => env('PUSHER_KEY'),
            'secret' => env('PUSHER_SECRET'),
            'app_id' => env('PUSHER_APP_ID'),
            'options' => [
                //
            ],
        ],

        'redis' => [
            'driver' => 'redis',
            'connection' => 'default',
        ],

        'log' => [
            'driver' => 'log',
        ],

    ],

];


File: /config\cache.php
<?php

return [

    /*
    |--------------------------------------------------------------------------
    | Default Cache Store
    |--------------------------------------------------------------------------
    |
    | This option controls the default cache connection that gets used while
    | using this caching library. This connection is used when another is
    | not explicitly specified when executing a given caching function.
    |
    */

    'default' => env('CACHE_DRIVER', 'file'),

    /*
    |--------------------------------------------------------------------------
    | Cache Stores
    |--------------------------------------------------------------------------
    |
    | Here you may define all of the cache "stores" for your application as
    | well as their drivers. You may even define multiple stores for the
    | same cache driver to group types of items stored in your caches.
    |
    */

    'stores' => [

        'apc' => [
            'driver' => 'apc',
        ],

        'array' => [
            'driver' => 'array',
        ],

        'database' => [
            'driver' => 'database',
            'table' => 'cache',
            'connection' => null,
        ],

        'file' => [
            'driver' => 'file',
            'path' => storage_path('framework/cache'),
        ],

        'memcached' => [
            'driver' => 'memcached',
            'servers' => [
                [
                    'host' => env('MEMCACHED_HOST', '127.0.0.1'),
                    'port' => env('MEMCACHED_PORT', 11211),
                    'weight' => 100,
                ],
            ],
        ],

        'redis' => [
            'driver' => 'redis',
            'connection' => 'default',
        ],

    ],

    /*
    |--------------------------------------------------------------------------
    | Cache Key Prefix
    |--------------------------------------------------------------------------
    |
    | When utilizing a RAM based store such as APC or Memcached, there might
    | be other applications utilizing the same cache. So, we'll specify a
    | value to get prefixed to all our keys so we can avoid collisions.
    |
    */

    'prefix' => 'laravel',

];


File: /config\compile.php
<?php

return [

    /*
    |--------------------------------------------------------------------------
    | Additional Compiled Classes
    |--------------------------------------------------------------------------
    |
    | Here you may specify additional classes to include in the compiled file
    | generated by the `artisan optimize` command. These should be classes
    | that are included on basically every request into the application.
    |
    */

    'files' => [
        //
    ],

    /*
    |--------------------------------------------------------------------------
    | Compiled File Providers
    |--------------------------------------------------------------------------
    |
    | Here you may list service providers which define a "compiles" function
    | that returns additional files that should be compiled, providing an
    | easy way to get common files from any packages you are utilizing.
    |
    */

    'providers' => [
        //
    ],

];


File: /config\database.php
<?php

return [

    /*
    |--------------------------------------------------------------------------
    | PDO Fetch Style
    |--------------------------------------------------------------------------
    |
    | By default, database results will be returned as instances of the PHP
    | stdClass object; however, you may desire to retrieve records in an
    | array format for simplicity. Here you can tweak the fetch style.
    |
    */

    'fetch' => PDO::FETCH_CLASS,

    /*
    |--------------------------------------------------------------------------
    | Default Database Connection Name
    |--------------------------------------------------------------------------
    |
    | Here you may specify which of the database connections below you wish
    | to use as your default connection for all database work. Of course
    | you may use many connections at once using the Database library.
    |
    */

    'default' => env('DB_CONNECTION', 'mysql'),

    /*
    |--------------------------------------------------------------------------
    | Database Connections
    |--------------------------------------------------------------------------
    |
    | Here are each of the database connections setup for your application.
    | Of course, examples of configuring each database platform that is
    | supported by Laravel is shown below to make development simple.
    |
    |
    | All database work in Laravel is done through the PHP PDO facilities
    | so make sure you have the driver for your particular database of
    | choice installed on your machine before you begin development.
    |
    */

    'connections' => [

        'sqlite' => [
            'driver' => 'sqlite',
            'database' => env('DB_DATABASE', database_path('database.sqlite')),
            'prefix' => '',
        ],

        'mysql' => [
            'driver' => 'mysql',
            'host' => env('DB_HOST', 'localhost'),
            'port' => env('DB_PORT', '3306'),
            'database' => env('DB_DATABASE', 'forge'),
            'username' => env('DB_USERNAME', 'forge'),
            'password' => env('DB_PASSWORD', ''),
            'charset' => 'utf8',
            'collation' => 'utf8_unicode_ci',
            'prefix' => '',
            'strict' => false,
            'engine' => null,
        ],

        'pgsql' => [
            'driver' => 'pgsql',
            'host' => env('DB_HOST', 'localhost'),
            'port' => env('DB_PORT', '5432'),
            'database' => env('DB_DATABASE', 'forge'),
            'username' => env('DB_USERNAME', 'forge'),
            'password' => env('DB_PASSWORD', ''),
            'charset' => 'utf8',
            'prefix' => '',
            'schema' => 'public',
        ],

    ],

    /*
    |--------------------------------------------------------------------------
    | Migration Repository Table
    |--------------------------------------------------------------------------
    |
    | This table keeps track of all the migrations that have already run for
    | your application. Using this information, we can determine which of
    | the migrations on disk haven't actually been run in the database.
    |
    */

    'migrations' => 'migrations',

    /*
    |--------------------------------------------------------------------------
    | Redis Databases
    |--------------------------------------------------------------------------
    |
    | Redis is an open source, fast, and advanced key-value store that also
    | provides a richer set of commands than a typical key-value systems
    | such as APC or Memcached. Laravel makes it easy to dig right in.
    |
    */

    'redis' => [

        'cluster' => false,

        'default' => [
            'host' => env('REDIS_HOST', 'localhost'),
            'password' => env('REDIS_PASSWORD', null),
            'port' => env('REDIS_PORT', 6379),
            'database' => 0,
        ],

    ],

];


File: /config\filesystems.php
<?php

return [

    /*
    |--------------------------------------------------------------------------
    | Default Filesystem Disk
    |--------------------------------------------------------------------------
    |
    | Here you may specify the default filesystem disk that should be used
    | by the framework. A "local" driver, as well as a variety of cloud
    | based drivers are available for your choosing. Just store away!
    |
    | Supported: "local", "ftp", "s3", "rackspace"
    |
    */

    'default' => 'local',

    /*
    |--------------------------------------------------------------------------
    | Default Cloud Filesystem Disk
    |--------------------------------------------------------------------------
    |
    | Many applications store files both locally and in the cloud. For this
    | reason, you may specify a default "cloud" driver here. This driver
    | will be bound as the Cloud disk implementation in the container.
    |
    */

    'cloud' => 's3',

    /*
    |--------------------------------------------------------------------------
    | Filesystem Disks
    |--------------------------------------------------------------------------
    |
    | Here you may configure as many filesystem "disks" as you wish, and you
    | may even configure multiple disks of the same driver. Defaults have
    | been setup for each driver as an example of the required options.
    |
    */

    'disks' => [

        'local' => [
            'driver' => 'local',
            'root' => storage_path('app'),
        ],

        'public' => [
            'driver' => 'local',
            'root' => storage_path('app/public'),
            'visibility' => 'public',
        ],

        's3' => [
            'driver' => 's3',
            'key' => 'your-key',
            'secret' => 'your-secret',
            'region' => 'your-region',
            'bucket' => 'your-bucket',
        ],

    ],

];


File: /config\mail.php
<?php

return [

    /*
    |--------------------------------------------------------------------------
    | Mail Driver
    |--------------------------------------------------------------------------
    |
    | Laravel supports both SMTP and PHP's "mail" function as drivers for the
    | sending of e-mail. You may specify which one you're using throughout
    | your application here. By default, Laravel is setup for SMTP mail.
    |
    | Supported: "smtp", "mail", "sendmail", "mailgun", "mandrill",
    |            "ses", "sparkpost", "log"
    |
    */

    'driver' => env('MAIL_DRIVER', 'smtp'),

    /*
    |--------------------------------------------------------------------------
    | SMTP Host Address
    |--------------------------------------------------------------------------
    |
    | Here you may provide the host address of the SMTP server used by your
    | applications. A default option is provided that is compatible with
    | the Mailgun mail service which will provide reliable deliveries.
    |
    */

    'host' => env('MAIL_HOST', 'smtp.mailgun.org'),

    /*
    |--------------------------------------------------------------------------
    | SMTP Host Port
    |--------------------------------------------------------------------------
    |
    | This is the SMTP port used by your application to deliver e-mails to
    | users of the application. Like the host we have set this value to
    | stay compatible with the Mailgun e-mail application by default.
    |
    */

    'port' => env('MAIL_PORT', 587),

    /*
    |--------------------------------------------------------------------------
    | Global "From" Address
    |--------------------------------------------------------------------------
    |
    | You may wish for all e-mails sent by your application to be sent from
    | the same address. Here, you may specify a name and address that is
    | used globally for all e-mails that are sent by your application.
    |
    */

    'from' => ['address' => null, 'name' => null],

    /*
    |--------------------------------------------------------------------------
    | E-Mail Encryption Protocol
    |--------------------------------------------------------------------------
    |
    | Here you may specify the encryption protocol that should be used when
    | the application send e-mail messages. A sensible default using the
    | transport layer security protocol should provide great security.
    |
    */

    'encryption' => env('MAIL_ENCRYPTION', 'tls'),

    /*
    |--------------------------------------------------------------------------
    | SMTP Server Username
    |--------------------------------------------------------------------------
    |
    | If your SMTP server requires a username for authentication, you should
    | set it here. This will get used to authenticate with your server on
    | connection. You may also set the "password" value below this one.
    |
    */

    'username' => env('MAIL_USERNAME'),

    /*
    |--------------------------------------------------------------------------
    | SMTP Server Password
    |--------------------------------------------------------------------------
    |
    | Here you may set the password required by your SMTP server to send out
    | messages from your application. This will be given to the server on
    | connection so that the application will be able to send messages.
    |
    */

    'password' => env('MAIL_PASSWORD'),

    /*
    |--------------------------------------------------------------------------
    | Sendmail System Path
    |--------------------------------------------------------------------------
    |
    | When using the "sendmail" driver to send e-mails, we will need to know
    | the path to where Sendmail lives on this server. A default path has
    | been provided here, which will work well on most of your systems.
    |
    */

    'sendmail' => '/usr/sbin/sendmail -bs',

];


File: /config\queue.php
<?php

return [

    /*
    |--------------------------------------------------------------------------
    | Default Queue Driver
    |--------------------------------------------------------------------------
    |
    | The Laravel queue API supports a variety of back-ends via an unified
    | API, giving you convenient access to each back-end using the same
    | syntax for each one. Here you may set the default queue driver.
    |
    | Supported: "null", "sync", "database", "beanstalkd",
    |            "sqs", "redis"
    |
    */

    'default' => env('QUEUE_DRIVER', 'sync'),

    /*
    |--------------------------------------------------------------------------
    | Queue Connections
    |--------------------------------------------------------------------------
    |
    | Here you may configure the connection information for each server that
    | is used by your application. A default configuration has been added
    | for each back-end shipped with Laravel. You are free to add more.
    |
    */

    'connections' => [

        'sync' => [
            'driver' => 'sync',
        ],

        'database' => [
            'driver' => 'database',
            'table' => 'jobs',
            'queue' => 'default',
            'expire' => 60,
        ],

        'beanstalkd' => [
            'driver' => 'beanstalkd',
            'host' => 'localhost',
            'queue' => 'default',
            'ttr' => 60,
        ],

        'sqs' => [
            'driver' => 'sqs',
            'key' => 'your-public-key',
            'secret' => 'your-secret-key',
            'prefix' => 'https://sqs.us-east-1.amazonaws.com/your-account-id',
            'queue' => 'your-queue-name',
            'region' => 'us-east-1',
        ],

        'redis' => [
            'driver' => 'redis',
            'connection' => 'default',
            'queue' => 'default',
            'expire' => 60,
        ],

    ],

    /*
    |--------------------------------------------------------------------------
    | Failed Queue Jobs
    |--------------------------------------------------------------------------
    |
    | These options configure the behavior of failed queue job logging so you
    | can control which database and table are used to store the jobs that
    | have failed. You may change them to any database / table you wish.
    |
    */

    'failed' => [
        'database' => env('DB_CONNECTION', 'mysql'),
        'table' => 'failed_jobs',
    ],

];


File: /config\services.php
<?php

return [

    /*
    |--------------------------------------------------------------------------
    | Third Party Services
    |--------------------------------------------------------------------------
    |
    | This file is for storing the credentials for third party services such
    | as Stripe, Mailgun, Mandrill, and others. This file provides a sane
    | default location for this type of information, allowing packages
    | to have a conventional place to find your various credentials.
    |
    */

    'mailgun' => [
        'domain' => env('MAILGUN_DOMAIN'),
        'secret' => env('MAILGUN_SECRET'),
    ],

    'ses' => [
        'key' => env('SES_KEY'),
        'secret' => env('SES_SECRET'),
        'region' => 'us-east-1',
    ],

    'sparkpost' => [
        'secret' => env('SPARKPOST_SECRET'),
    ],

    'stripe' => [
        'model' => App\User::class,
        'key' => env('STRIPE_KEY'),
        'secret' => env('STRIPE_SECRET'),
    ],

];


File: /config\session.php
<?php

return [

    /*
    |--------------------------------------------------------------------------
    | Default Session Driver
    |--------------------------------------------------------------------------
    |
    | This option controls the default session "driver" that will be used on
    | requests. By default, we will use the lightweight native driver but
    | you may specify any of the other wonderful drivers provided here.
    |
    | Supported: "file", "cookie", "database", "apc",
    |            "memcached", "redis", "array"
    |
    */

    'driver' => env('SESSION_DRIVER', 'file'),

    /*
    |--------------------------------------------------------------------------
    | Session Lifetime
    |--------------------------------------------------------------------------
    |
    | Here you may specify the number of minutes that you wish the session
    | to be allowed to remain idle before it expires. If you want them
    | to immediately expire on the browser closing, set that option.
    |
    */

    'lifetime' => 120,

    'expire_on_close' => false,

    /*
    |--------------------------------------------------------------------------
    | Session Encryption
    |--------------------------------------------------------------------------
    |
    | This option allows you to easily specify that all of your session data
    | should be encrypted before it is stored. All encryption will be run
    | automatically by Laravel and you can use the Session like normal.
    |
    */

    'encrypt' => false,

    /*
    |--------------------------------------------------------------------------
    | Session File Location
    |--------------------------------------------------------------------------
    |
    | When using the native session driver, we need a location where session
    | files may be stored. A default has been set for you but a different
    | location may be specified. This is only needed for file sessions.
    |
    */

    'files' => storage_path('framework/sessions'),

    /*
    |--------------------------------------------------------------------------
    | Session Database Connection
    |--------------------------------------------------------------------------
    |
    | When using the "database" or "redis" session drivers, you may specify a
    | connection that should be used to manage these sessions. This should
    | correspond to a connection in your database configuration options.
    |
    */

    'connection' => null,

    /*
    |--------------------------------------------------------------------------
    | Session Database Table
    |--------------------------------------------------------------------------
    |
    | When using the "database" session driver, you may specify the table we
    | should use to manage the sessions. Of course, a sensible default is
    | provided for you; however, you are free to change this as needed.
    |
    */

    'table' => 'sessions',

    /*
    |--------------------------------------------------------------------------
    | Session Sweeping Lottery
    |--------------------------------------------------------------------------
    |
    | Some session drivers must manually sweep their storage location to get
    | rid of old sessions from storage. Here are the chances that it will
    | happen on a given request. By default, the odds are 2 out of 100.
    |
    */

    'lottery' => [2, 100],

    /*
    |--------------------------------------------------------------------------
    | Session Cookie Name
    |--------------------------------------------------------------------------
    |
    | Here you may change the name of the cookie used to identify a session
    | instance by ID. The name specified here will get used every time a
    | new session cookie is created by the framework for every driver.
    |
    */

    'cookie' => 'laravel_session',

    /*
    |--------------------------------------------------------------------------
    | Session Cookie Path
    |--------------------------------------------------------------------------
    |
    | The session cookie path determines the path for which the cookie will
    | be regarded as available. Typically, this will be the root path of
    | your application but you are free to change this when necessary.
    |
    */

    'path' => '/',

    /*
    |--------------------------------------------------------------------------
    | Session Cookie Domain
    |--------------------------------------------------------------------------
    |
    | Here you may change the domain of the cookie used to identify a session
    | in your application. This will determine which domains the cookie is
    | available to in your application. A sensible default has been set.
    |
    */

    'domain' => null,

    /*
    |--------------------------------------------------------------------------
    | HTTPS Only Cookies
    |--------------------------------------------------------------------------
    |
    | By setting this option to true, session cookies will only be sent back
    | to the server if the browser has a HTTPS connection. This will keep
    | the cookie from being sent to you if it can not be done securely.
    |
    */

    'secure' => false,

    /*
    |--------------------------------------------------------------------------
    | HTTP Access Only
    |--------------------------------------------------------------------------
    |
    | Setting this value to true will prevent JavaScript from accessing the
    | value of the cookie and the cookie will only be accessible through
    | the HTTP protocol. You are free to modify this option if needed.
    |
    */

    'http_only' => true,

];


File: /config\view.php
<?php

return [

    /*
    |--------------------------------------------------------------------------
    | View Storage Paths
    |--------------------------------------------------------------------------
    |
    | Most templating systems load templates from disk. Here you may specify
    | an array of paths that should be checked for your views. Of course
    | the usual Laravel view path has already been registered for you.
    |
    */

    'paths' => [
        realpath(base_path('resources/views')),
    ],

    /*
    |--------------------------------------------------------------------------
    | Compiled View Path
    |--------------------------------------------------------------------------
    |
    | This option determines where all the compiled Blade templates will be
    | stored for your application. Typically, this is within the storage
    | directory. However, as usual, you are free to change this value.
    |
    */

    'compiled' => realpath(storage_path('framework/views')),

];


File: /database\.gitignore
*.sqlite


File: /database\factories\ModelFactory.php
<?php

/*
|--------------------------------------------------------------------------
| Model Factories
|--------------------------------------------------------------------------
|
| Here you may define all of your model factories. Model factories give
| you a convenient way to create models for testing and seeding your
| database. Just tell the factory how a default model should look.
|
*/

$factory->define(App\User::class, function (Faker\Generator $faker) {
    return [
        'name' => $faker->name,
        'email' => $faker->safeEmail,
        'password' => bcrypt(str_random(10)),
        'remember_token' => str_random(10),
    ];
});


File: /database\migrations\.gitkeep



File: /database\migrations\2014_10_12_000000_create_users_table.php
<?php

use Illuminate\Database\Schema\Blueprint;
use Illuminate\Database\Migrations\Migration;

class CreateUsersTable extends Migration
{
    /**
     * Run the migrations.
     *
     * @return void
     */
    public function up()
    {
        Schema::create('users', function (Blueprint $table) {
            $table->increments('id');
            $table->string('name');
            $table->string('email')->unique();
            $table->string('password');
            $table->rememberToken();
            $table->timestamps();
        });
        DB::table('users')->insert(
            array(
                'name' => 'Admin',
                'email' => 'admin@localhost.local',
                'password' => \Hash::make('admin'),
            )
        );
    }

    /**
     * Reverse the migrations.
     *
     * @return void
     */
    public function down()
    {
        Schema::drop('users');
    }
}


File: /database\migrations\2014_10_12_100000_create_password_resets_table.php
<?php

use Illuminate\Database\Schema\Blueprint;
use Illuminate\Database\Migrations\Migration;

class CreatePasswordResetsTable extends Migration
{
    /**
     * Run the migrations.
     *
     * @return void
     */
    public function up()
    {
        Schema::create('password_resets', function (Blueprint $table) {
            $table->string('email')->index();
            $table->string('token')->index();
            $table->timestamp('created_at');
        });
    }

    /**
     * Reverse the migrations.
     *
     * @return void
     */
    public function down()
    {
        Schema::drop('password_resets');
    }
}


File: /database\migrations\2016_04_14_031423_create_mikrotiks_table.php
<?php

use Illuminate\Database\Schema\Blueprint;
use Illuminate\Database\Migrations\Migration;

class CreateMikrotiksTable extends Migration
{
    /**
     * Run the migrations.
     *
     * @return void
     */
    public function up()
    {
        Schema::create('mikrotiks', function (Blueprint $table) {
            $table->increments('id');
            $table->string('name');
            $table->string('ipaddress');
            $table->string('user');
            $table->string('pass');
            $table->string('is_active');
            $table->timestamps();
        });
        DB::table('mikrotiks')->insert(
            array(
                'name' => 'Router Name',
                'ipaddress' => '',
                'user' => '',
                'is_active' => 'true',
                'pass' => \Hash::make('admin'),
            )
        );
    }

    /**
     * Reverse the migrations.
     *
     * @return void
     */
    public function down()
    {
        Schema::drop('mikrotiks');
    }
}


File: /database\migrations\2016_04_15_063918_add_port_to_router.php
<?php

use Illuminate\Database\Schema\Blueprint;
use Illuminate\Database\Migrations\Migration;

class AddPortToRouter extends Migration
{
    /**
     * Run the migrations.
     *
     * @return void
     */
    public function up()
    {
        Schema::table('mikrotiks', function($table) {
            $table->integer('port')->unsigned();
        });
    }

    /**
     * Reverse the migrations.
     *
     * @return void
     */
    public function down()
    {
        $table->dropColumn('port');
    }
}


File: /database\seeds\.gitkeep



File: /database\seeds\DatabaseSeeder.php
<?php

use Illuminate\Database\Seeder;

class DatabaseSeeder extends Seeder
{
    /**
     * Run the database seeds.
     *
     * @return void
     */
    public function run()
    {
        // $this->call(UsersTableSeeder::class);
    }
}


File: /gulpfile.js
var elixir = require('laravel-elixir');

/*
 |--------------------------------------------------------------------------
 | Elixir Asset Management
 |--------------------------------------------------------------------------
 |
 | Elixir provides a clean, fluent API for defining some basic Gulp tasks
 | for your Laravel application. By default, we are compiling the Sass
 | file for our application, as well as publishing vendor resources.
 |
 */

elixir(function(mix) {
    mix.sass('app.scss');
});


File: /laravel.md
# Laravel PHP Framework

[![Build Status](https://travis-ci.org/laravel/framework.svg)](https://travis-ci.org/laravel/framework)
[![Total Downloads](https://poser.pugx.org/laravel/framework/d/total.svg)](https://packagist.org/packages/laravel/framework)
[![Latest Stable Version](https://poser.pugx.org/laravel/framework/v/stable.svg)](https://packagist.org/packages/laravel/framework)
[![Latest Unstable Version](https://poser.pugx.org/laravel/framework/v/unstable.svg)](https://packagist.org/packages/laravel/framework)
[![License](https://poser.pugx.org/laravel/framework/license.svg)](https://packagist.org/packages/laravel/framework)

Laravel is a web application framework with expressive, elegant syntax. We believe development must be an enjoyable, creative experience to be truly fulfilling. Laravel attempts to take the pain out of development by easing common tasks used in the majority of web projects, such as authentication, routing, sessions, queueing, and caching.

Laravel is accessible, yet powerful, providing tools needed for large, robust applications. A superb inversion of control container, expressive migration system, and tightly integrated unit testing support give you the tools you need to build any application with which you are tasked.

## Official Documentation

Documentation for the framework can be found on the [Laravel website](http://laravel.com/docs).

## Contributing

Thank you for considering contributing to the Laravel framework! The contribution guide can be found in the [Laravel documentation](http://laravel.com/docs/contributions).

## Security Vulnerabilities

If you discover a security vulnerability within Laravel, please send an e-mail to Taylor Otwell at taylor@laravel.com. All security vulnerabilities will be promptly addressed.

## License

The Laravel framework is open-sourced software licensed under the [MIT license](http://opensource.org/licenses/MIT).


File: /package.json
{
  "private": true,
  "devDependencies": {
    "gulp": "^3.9.1"
  },
  "dependencies": {
    "laravel-elixir": "^5.0.0",
    "bootstrap-sass": "^3.0.0"
  }
}


File: /phpunit.xml
<?xml version="1.0" encoding="UTF-8"?>
<phpunit backupGlobals="false"
         backupStaticAttributes="false"
         bootstrap="bootstrap/autoload.php"
         colors="true"
         convertErrorsToExceptions="true"
         convertNoticesToExceptions="true"
         convertWarningsToExceptions="true"
         processIsolation="false"
         stopOnFailure="false">
    <testsuites>
        <testsuite name="Application Test Suite">
            <directory suffix="Test.php">./tests</directory>
        </testsuite>
    </testsuites>
    <filter>
        <whitelist processUncoveredFilesFromWhitelist="true">
            <directory suffix=".php">./app</directory>
            <exclude>
                <file>./app/Http/routes.php</file>
            </exclude>
        </whitelist>
    </filter>
    <php>
        <env name="APP_ENV" value="testing"/>
        <env name="CACHE_DRIVER" value="array"/>
        <env name="SESSION_DRIVER" value="array"/>
        <env name="QUEUE_DRIVER" value="sync"/>
    </php>
</phpunit>


File: /public\.htaccess
<IfModule mod_rewrite.c>
    <IfModule mod_negotiation.c>
        Options -MultiViews
    </IfModule>

    RewriteEngine On

    # Redirect Trailing Slashes If Not A Folder...
    RewriteCond %{REQUEST_FILENAME} !-d
    RewriteRule ^(.*)/$ /$1 [L,R=301]

    # Handle Front Controller...
    RewriteCond %{REQUEST_FILENAME} !-d
    RewriteCond %{REQUEST_FILENAME} !-f
    RewriteRule ^ index.php [L]

    # Handle Authorization Header
    RewriteCond %{HTTP:Authorization} .
    RewriteRule .* - [E=HTTP_AUTHORIZATION:%{HTTP:Authorization}]
</IfModule>


File: /public\index.php
<?php

/**
 * Laravel - A PHP Framework For Web Artisans
 *
 * @package  Laravel
 * @author   Taylor Otwell <taylorotwell@gmail.com>
 */

/*
|--------------------------------------------------------------------------
| Register The Auto Loader
|--------------------------------------------------------------------------
|
| Composer provides a convenient, automatically generated class loader for
| our application. We just need to utilize it! We'll simply require it
| into the script here so that we don't have to worry about manual
| loading any of our classes later on. It feels nice to relax.
|
*/

require __DIR__.'/../bootstrap/autoload.php';

/*
|--------------------------------------------------------------------------
| Turn On The Lights
|--------------------------------------------------------------------------
|
| We need to illuminate PHP development, so let us turn on the lights.
| This bootstraps the framework and gets it ready for use, then it
| will load up this application so that we can run it and send
| the responses back to the browser and delight our users.
|
*/

$app = require_once __DIR__.'/../bootstrap/app.php';

/*
|--------------------------------------------------------------------------
| Run The Application
|--------------------------------------------------------------------------
|
| Once we have the application, we can handle the incoming request
| through the kernel, and send the associated response back to
| the client's browser allowing them to enjoy the creative
| and wonderful application we have prepared for them.
|
*/

$kernel = $app->make(Illuminate\Contracts\Http\Kernel::class);

$response = $kernel->handle(
    $request = Illuminate\Http\Request::capture()
);

$response->send();

$kernel->terminate($request, $response);


File: /public\robots.txt
User-agent: *
Disallow:


File: /public\web.config
<configuration>
  <system.webServer>
    <rewrite>
      <rules>
        <rule name="Imported Rule 1" stopProcessing="true">
          <match url="^(.*)/$" ignoreCase="false" />
          <conditions>
            <add input="{REQUEST_FILENAME}" matchType="IsDirectory" ignoreCase="false" negate="true" />
          </conditions>
          <action type="Redirect" redirectType="Permanent" url="/{R:1}" />
        </rule>
        <rule name="Imported Rule 2" stopProcessing="true">
          <match url="^" ignoreCase="false" />
          <conditions>
            <add input="{REQUEST_FILENAME}" matchType="IsDirectory" ignoreCase="false" negate="true" />
            <add input="{REQUEST_FILENAME}" matchType="IsFile" ignoreCase="false" negate="true" />
          </conditions>
          <action type="Rewrite" url="index.php" />
        </rule>
      </rules>
    </rewrite>
  </system.webServer>
</configuration>


File: /readme.md
# Open Hotspot Manager for Mikrotik

Hotspot Manager working with Mikrotik API.

Developed with Laravel Framework

## Instalation
Clone from repository

```
git clone https://github.com/bleeloe/Open-Hotspot-Manger-for-Mikrotik.git 
```

Run Composer, please you have to install composer first https://getcomposer.org/
```
composer update
```
Edit configuration file
edit `.env` file then change config based on your mysql configuration

host, user, password and database name.


after editing run artisan command 
```
php artisan migrate
```


Default user
username `admin@localhost.local`


password `admin`


## Features:
 - Easy add, edit dan delete user.
 - Kill Active User Online 
 - Easy ip-binding management

## Contributing
Thank you for considering contributing to Open Hotspot Manager for Mikrotik! 
Please pull request to develop branch


## License

The Open Hotspot Manager is open-sourced software licensed under the [MIT license](http://opensource.org/licenses/MIT).


File: /resources\assets\sass\app.scss
File: /resources\lang\en\auth.php
<?php

return [

    /*
    |--------------------------------------------------------------------------
    | Authentication Language Lines
    |--------------------------------------------------------------------------
    |
    | The following language lines are used during authentication for various
    | messages that we need to display to the user. You are free to modify
    | these language lines according to your application's requirements.
    |
    */

    'failed' => 'These credentials do not match our records.',
    'throttle' => 'Too many login attempts. Please try again in :seconds seconds.',

];


File: /resources\lang\en\cocomas.php
<?php

return [

    /*
    |--------------------------------------------------------------------------
    | Cocomas
    |--------------------------------------------------------------------------
    |
    | The following language lines are used during authentication for various
    | messages that we need to display to the user. You are free to modify
    | these language lines according to your application's requirements.
    |
    */

    'success' => 'Success!',
    'error' => 'Error!',

];


File: /resources\lang\en\pagination.php
<?php

return [

    /*
    |--------------------------------------------------------------------------
    | Pagination Language Lines
    |--------------------------------------------------------------------------
    |
    | The following language lines are used by the paginator library to build
    | the simple pagination links. You are free to change them to anything
    | you want to customize your views to better match your application.
    |
    */

    'previous' => '&laquo; Previous',
    'next'     => 'Next &raquo;',

];


File: /resources\lang\en\passwords.php
<?php

return [

    /*
    |--------------------------------------------------------------------------
    | Password Reset Language Lines
    |--------------------------------------------------------------------------
    |
    | The following language lines are the default lines which match reasons
    | that are given by the password broker for a password update attempt
    | has failed, such as for an invalid token or invalid new password.
    |
    */

    'password' => 'Passwords must be at least six characters and match the confirmation.',
    'reset' => 'Your password has been reset!',
    'sent' => 'We have e-mailed your password reset link!',
    'token' => 'This password reset token is invalid.',
    'user' => "We can't find a user with that e-mail address.",

];


File: /resources\lang\en\validation.php
<?php

return [

    /*
    |--------------------------------------------------------------------------
    | Validation Language Lines
    |--------------------------------------------------------------------------
    |
    | The following language lines contain the default error messages used by
    | the validator class. Some of these rules have multiple versions such
    | as the size rules. Feel free to tweak each of these messages here.
    |
    */

    'accepted'             => 'The :attribute must be accepted.',
    'active_url'           => 'The :attribute is not a valid URL.',
    'after'                => 'The :attribute must be a date after :date.',
    'alpha'                => 'The :attribute may only contain letters.',
    'alpha_dash'           => 'The :attribute may only contain letters, numbers, and dashes.',
    'alpha_num'            => 'The :attribute may only contain letters and numbers.',
    'array'                => 'The :attribute must be an array.',
    'before'               => 'The :attribute must be a date before :date.',
    'between'              => [
        'numeric' => 'The :attribute must be between :min and :max.',
        'file'    => 'The :attribute must be between :min and :max kilobytes.',
        'string'  => 'The :attribute must be between :min and :max characters.',
        'array'   => 'The :attribute must have between :min and :max items.',
    ],
    'boolean'              => 'The :attribute field must be true or false.',
    'confirmed'            => 'The :attribute confirmation does not match.',
    'date'                 => 'The :attribute is not a valid date.',
    'date_format'          => 'The :attribute does not match the format :format.',
    'different'            => 'The :attribute and :other must be different.',
    'digits'               => 'The :attribute must be :digits digits.',
    'digits_between'       => 'The :attribute must be between :min and :max digits.',
    'distinct'             => 'The :attribute field has a duplicate value.',
    'email'                => 'The :attribute must be a valid email address.',
    'exists'               => 'The selected :attribute is invalid.',
    'filled'               => 'The :attribute field is required.',
    'image'                => 'The :attribute must be an image.',
    'in'                   => 'The selected :attribute is invalid.',
    'in_array'             => 'The :attribute field does not exist in :other.',
    'integer'              => 'The :attribute must be an integer.',
    'ip'                   => 'The :attribute must be a valid IP address.',
    'json'                 => 'The :attribute must be a valid JSON string.',
    'max'                  => [
        'numeric' => 'The :attribute may not be greater than :max.',
        'file'    => 'The :attribute may not be greater than :max kilobytes.',
        'string'  => 'The :attribute may not be greater than :max characters.',
        'array'   => 'The :attribute may not have more than :max items.',
    ],
    'mimes'                => 'The :attribute must be a file of type: :values.',
    'min'                  => [
        'numeric' => 'The :attribute must be at least :min.',
        'file'    => 'The :attribute must be at least :min kilobytes.',
        'string'  => 'The :attribute must be at least :min characters.',
        'array'   => 'The :attribute must have at least :min items.',
    ],
    'not_in'               => 'The selected :attribute is invalid.',
    'numeric'              => 'The :attribute must be a number.',
    'present'              => 'The :attribute field must be present.',
    'regex'                => 'The :attribute format is invalid.',
    'required'             => 'The :attribute field is required.',
    'required_if'          => 'The :attribute field is required when :other is :value.',
    'required_unless'      => 'The :attribute field is required unless :other is in :values.',
    'required_with'        => 'The :attribute field is required when :values is present.',
    'required_with_all'    => 'The :attribute field is required when :values is present.',
    'required_without'     => 'The :attribute field is required when :values is not present.',
    'required_without_all' => 'The :attribute field is required when none of :values are present.',
    'same'                 => 'The :attribute and :other must match.',
    'size'                 => [
        'numeric' => 'The :attribute must be :size.',
        'file'    => 'The :attribute must be :size kilobytes.',
        'string'  => 'The :attribute must be :size characters.',
        'array'   => 'The :attribute must contain :size items.',
    ],
    'string'               => 'The :attribute must be a string.',
    'timezone'             => 'The :attribute must be a valid zone.',
    'unique'               => 'The :attribute has already been taken.',
    'url'                  => 'The :attribute format is invalid.',

    /*
    |--------------------------------------------------------------------------
    | Custom Validation Language Lines
    |--------------------------------------------------------------------------
    |
    | Here you may specify custom validation messages for attributes using the
    | convention "attribute.rule" to name the lines. This makes it quick to
    | specify a specific custom language line for a given attribute rule.
    |
    */

    'custom' => [
        'attribute-name' => [
            'rule-name' => 'custom-message',
        ],
    ],

    /*
    |--------------------------------------------------------------------------
    | Custom Validation Attributes
    |--------------------------------------------------------------------------
    |
    | The following language lines are used to swap attribute place-holders
    | with something more reader friendly such as E-Mail Address instead
    | of "email". This simply helps us make messages a little cleaner.
    |
    */

    'attributes' => [],

];


File: /resources\views\app\active\index.blade.php
@extends('layouts.app')
@section('content')
<div class="container-fluid">
    <div class="row">        
        @include('sidemenu')
        <div class="col-md-10 col-sm-10 col-xs-10">
            <div class="panel panel-default">
                <div class="panel-heading"><strong>Active</strong></div>
                <div class="panel-body">
				<table data-toggle="table" data-url="{{url('/hotspot/active')}}" data-pagination="true" data-height="450" data-search="true" data-show-toggle="true" data-show-columns="true" data-trim-on-search="false" data-show-refresh="true" class="table table-striped">
				    <thead>
				        <tr>
							<th data-visible="false" data-sortable="true" data-field="numbers">numbers</th>
							<th data-visible="true" data-sortable="true" data-formatter="df">#</th>
							<th data-visible="false" data-sortable="true" data-field="radius">radius</th>
							<th data-visible="true" data-sortable="true" data-field="server">server</th>
							<th data-visible="true" data-sortable="true" data-field="user">user</th>
							<th data-visible="true" data-sortable="true" data-field="ipaddress">ipaddress</th>
							<th data-visible="true" data-sortable="true" data-field="uptime">uptime</th>
							<th data-visible="true" data-sortable="true" data-field="loginBy">loginBy</th>
							<th data-visible="true" data-sortable="true" data-field="bytesIn">bytesIn</th>	
							<th data-visible="true" data-sortable="true" data-field="bytesOut">bytesOut</th>
							<th data-visible="true" data-sortable="false" data-field="domain">domain</th>
							<th data-visible="true" data-sortable="true" data-field="idleTime">idleTime</th>
							<th data-visible="true" data-sortable="true" data-field="idleTimeout">idleTimeout</th>
							<th data-visible="true" data-sortable="true" data-field="keepalive_timeout">keepalive_timeout</th>
							<th data-visible="false" data-sortable="true" data-field="limitBytesIn">limitBytesIn</th>
							<th data-visible="false" data-sortable="true" data-field="limitBytesOut">limitBytesOut</th>
							<th data-visible="false" data-sortable="true" data-field="limitBytesTotal">limitBytesTotal</th>
							<th data-visible="false" data-sortable="true" data-field="limitUptime">limitUptime</th>
							<th data-visible="false" data-sortable="true" data-field="packetsIn">packetsIn</th>
							<th data-visible="false" data-sortable="true" data-field="packetsOut">packetsOut</th>
							<th data-visible="false" data-sortable="true" data-field="macAddress">macAddress</th>
							<th data-visible="false" data-sortable="true" data-field="sessionTimeLeft">sessionTimeLeft</th>							
				        </tr>
				    </thead>
				    <tbody>				        
				    </tbody>
				</table>
                    
                </div>
            </div>
        </div>
    </div>
</div>
<script type="text/javascript">
	function df(value,row,index){
		return '<a href="{{url('/active/kill')}}/'+row.numbers+'" class="btn btn-danger btn-sm"><i class="glyphicon glyphicon-remove"></i></a>';
	}
</script>
@endsection


File: /resources\views\app\binding\create.blade.php
@extends('layouts.app')
@section('content')
<div class="container-fluid">
    <div class="row">        
        @include('sidemenu')
        <div class="col-md-10 col-sm-10 col-xs-10">
        @include('flash')
        <form method="post">
        	<input type="hidden" name="_token" value="{!! csrf_token() !!}">        
            <div class="panel panel-default">
                <div class="panel-heading">Binding / Create</div>
                <div class="panel-body">
	                <div class="row">
	                	<div class="col-md-10">
	                		<div class="form-group">
	                			<label for="mac-address">mac-address</label>
	                			<input name="mac-address" type="text" class="form-control" id="mac-address" value="{{old('mac-address')}}">
	                		</div>
	                		<div class="form-group">
	                			<label for="address">address</label>
	                			<input name="address" type="text" class="form-control" id="address" value="{{old('address')}}">
	                		</div>
	                		<div class="form-group">
	                			<label for="to-address">to-address</label>
	                			<input name="to-address" type="text" class="form-control" id="to-address" value="{{old('to-address')}}">
	                		</div>
	                		<div class="form-group">
	                			<label for="server">server</label>
	                			<input name="server" type="text" class="form-control" id="server" value="{{old('server')}}">
	                		</div>
	                		<div class="form-group">
	                			<label for="type">type</label>
	                			<input name="type" type="text" class="form-control" id="type" value="{{old('type')}}">
	                		</div>

	                		<div class="form-group">
	                			<label for="comment">Comment</label>
	                			<input name="comment" type="text" class="form-control" id="comment" value="{{old('comment')}}">
	                		</div>
	                	</div>
	                </div>
                </div>
                <div class="panel-footer">                	
	                <button type="submit" class="btn btn-default">Save</button>	                
                </div>
            </div>
    	</form>	
        </div>
    </div>
</div>
@endsection


File: /resources\views\app\binding\edit.blade.php
@extends('layouts.app')
@section('content')
<div class="container-fluid">
    <div class="row">        
        @include('sidemenu')
        <div class="col-md-10 col-sm-10 col-xs-10">
        @include('flash')
        <form method="post">
        	<input type="hidden" name="_token" value="{!! csrf_token() !!}">        
            <div class="panel panel-default">
                <div class="panel-heading">Binding / Create</div>
                <div class="panel-body">
	                <div class="row">
	                	<div class="col-md-10">
	                		<div class="form-group">
	                			<label for="mac-address">mac-address</label>
	                			<input name="mac-address" type="text" class="form-control" id="mac-address" value="{{old('mac-address',$macaddress)}}">
	                		</div>
	                		<div class="form-group">
	                			<label for="address">address</label>
	                			<input name="address" type="text" class="form-control" id="address" value="{{old('address',$address)}}">
	                		</div>
	                		<div class="form-group">
	                			<label for="to-address">to-address</label>
	                			<input name="to-address" type="text" class="form-control" id="to-address" value="{{old('to-address',$toaddress)}}">
	                		</div>
	                		<div class="form-group">
	                			<label for="server">server</label>
	                			<input name="server" type="text" class="form-control" id="server" value="{{old('server',$server)}}">
	                		</div>
	                		<div class="form-group">
	                			<label for="type">type</label>
	                			<input name="type" type="text" class="form-control" id="type" value="{{old('type',$type)}}">
	                		</div>
	                		<div class="form-group">
	                			<label for="comment">Comment</label>
	                			<input name="comment" type="text" class="form-control" id="comment" value="{{old('comment',$comment)}}">
	                		</div>
	                		<div class="form-group">
	                			<label for="disabled">disabled</label>
	                			<input name="disabled" type="text" class="form-control" id="disabled" value="{{old('disabled',$disabled)}}">
	                		</div>
	                	</div>
	                </div>
                </div>
                <div class="panel-footer">
                	<a href="{{url('/binding')}}" class="btn btn-default"><i class="gylphicon glyphicon-back"></i> Back</a>
	                <button type="submit" class="btn btn-default">Save</button>	                
                </div>
            </div>
    	</form>	
        </div>
    </div>
</div>
@endsection


File: /resources\views\app\binding\index.blade.php
@extends('layouts.app')
@section('content')
<div class="container-fluid">
    <div class="row">        
        @include('sidemenu')
        <div class="col-md-10 col-sm-10 col-xs-10">
            <div class="panel panel-default">
                <div class="panel-heading"><strong>Binding</strong></div>
                <div id="toolbar">                	
                	<div class="btn-group">
                	<a href="{{url('/binding/create')}}" title="add user" class="btn btn-primary"><i class="glyphicon glyphicon-plus"></i></a>	
                	</div>                	
                </div>
				<table data-toggle="table" data-url="{{url('/hotspot/ip-binding')}}" data-pagination="true" data-height="450" data-search="true" data-show-toggle="true" data-show-columns="true" data-trim-on-search="false" data-show-refresh="true" class="table table-striped" data-toolbar="#toolbar">
				    <thead>
				        <tr>
				        	<th data-visible="true" data-sortable="true" data-formatter="df">Delete</th>
				        	<th data-visible="true" data-sortable="true" data-formatter="df1">Edit</th>
							<th data-visible="false" data-sortable="true" data-field="numbers">numbers</th>							
							<th data-visible="true" data-sortable="true" data-field="disabled">disabled</th>							
							<th data-visible="true" data-sortable="true" data-field="mac-address">mac-address</th>							
							<th data-visible="true" data-sortable="true" data-field="comment">comment</th>
							<th data-visible="true" data-sortable="true" data-field="address">address</th>
							<th data-visible="true" data-sortable="true" data-field="to-address">to-address</th>
							<th data-visible="true" data-sortable="true" data-field="type">type</th>
							<th data-visible="true" data-sortable="true" data-field="server">server</th>					
				        </tr>
				    </thead>
				    <tbody>				        
				    </tbody>
				</table>
                    
                </div>
            </div>
        </div>
    </div>
</div>
<script type="text/javascript">
	function df(value,row,index){
		return '<a href="{{url('/binding')}}/'+row.numbers+'/remove" class="btn btn-danger btn-sm"><i class="glyphicon glyphicon-remove"></i></a>';
	};
	function df1(value,row,index){
		return '<a href="{{url('/binding')}}/'+row.numbers+'/edit" class="btn btn-primary btn-sm"><i class="glyphicon glyphicon-edit"></i></a>';
	}
</script>
@endsection


File: /resources\views\app\user\create.blade.php
@extends('layouts.app')
@section('content')
<div class="container-fluid">
    <div class="row">        
        @include('sidemenu')
        <div class="col-md-10 col-sm-10 col-xs-10">
        @include('flash')
        <form method="post">
        	<input type="hidden" name="_token" value="{!! csrf_token() !!}">        
            <div class="panel panel-default">
                <div class="panel-heading">User / Create</div>
                <div class="panel-body">
	                <div class="row">
	                	<div class="col-md-10">
	                		<div class="form-group">
	                			<label for="server">Server</label>
	                			<input name="server" type="text" class="form-control" id="server" value="{{old('server')}}">
	                		</div>
	                		<div class="form-group">
	                			<label for="name">Name</label>
	                			<input name="name" autocomplete="off" type="text" required class="form-control" id="name" value="{{old('name')}}">
	                		</div>
	                		<div class="form-group">
	                			<label for="password">Password</label>
	                			<input name="password" type="password" required class="form-control" id="password" value="{{old('password')}}">
	                		</div>
	                		<div class="form-group">
	                			<label for="profile">Profile</label>
	                			<input name="profile" type="text" class="form-control" id="profile" value="{{old('profile')}}">
	                		</div>
	                		<div class="form-group">
	                			<label for="email">Email</label>
	                			<input name="email" type="text" class="form-control" id="email" value="{{old('email')}}">
	                		</div>
	                		<div class="form-group">
	                			<label for="comment">Comment</label>
	                			<input name="comment" type="text" class="form-control" id="comment" value="{{old('comment')}}">
	                		</div>
	                	</div>
	                </div>
                </div>
                <div class="panel-footer">                	
	                <button type="submit" class="btn btn-default">Save</button>	                
                </div>
            </div>
    	</form>	
        </div>
    </div>
</div>
@endsection


File: /resources\views\app\user\edit.blade.php
@extends('layouts.app')
@section('content')
<div class="container-fluid">
    <div class="row">        
        @include('sidemenu')
        <div class="col-md-10 col-sm-10 col-xs-10">
        @include('flash')
        <form method="post">
        	<input type="hidden" name="_token" value="{!! csrf_token() !!}">        
            <div class="panel panel-default">
                <div class="panel-heading">User / Create</div>
                <div class="panel-body">
	                <div class="row">
	                	<div class="col-md-10">
	                		<div class="form-group">
	                			<label for="server">Server</label>
	                			<input name="server" type="text" class="form-control" id="server" value="{{old('server',$server)}}">
	                		</div>
	                		<div class="form-group">
	                			<label for="name">Name</label>
	                			<input name="name" autocomplete="off" type="text" required class="form-control" id="name" value="{{old('name',$name)}}">
	                		</div>
	                		<div class="form-group">
	                			<label for="password">Password</label>
	                			<input name="password" type="password" class="form-control" id="password" value="{{old('password')}}">
	                		</div>
	                		<div class="form-group">
	                			<label for="profile">Profile</label>
	                			<input name="profile" type="text" class="form-control" id="profile" value="{{old('profile',$profile)}}">
	                		</div>
	                		<div class="form-group">
	                			<label for="email">Email</label>
	                			<input name="email" type="text" class="form-control" id="email" value="{{old('email',$email)}}">
	                		</div>
	                		<div class="form-group">
	                			<label for="disabled">disabled</label>
	                			<input name="disabled" type="text" class="form-control" id="disabled" value="{{old('disabled',$disabled)}}">
	                		</div>
	                		<div class="form-group">
	                			<label for="comment">Comment</label>
	                			<input name="comment" type="text" class="form-control" id="comment" value="{{old('comment',$comment)}}">
	                		</div>
	                	</div>
	                </div>
                </div>
                <div class="panel-footer">                	
                	<a href="{{url('/user')}}" class="btn btn-default"><i class="gylphicon glyphicon-back"></i> Back</a>
	                <button type="submit" class="btn btn-primary">Save</button>	                
                </div>
            </div>
    	</form>	
        </div>
    </div>
</div>
@endsection


File: /resources\views\app\user\index.blade.php
@extends('layouts.app')
@section('content')
<div class="container-fluid">
    <div class="row">        
        @include('sidemenu')
        <div class="col-md-10 col-sm-10 col-xs-10">
        @include('flash')
            <div class="panel panel-default">
                <div class="panel-heading"><strong>User</strong></div>
                <div class="panel-body">
                <div id="toolbar">
                	<a href="{{url('/user/create')}}" title="add user" class="btn btn-primary"><i class="glyphicon glyphicon-plus"></i></a>
                </div>
				<table data-toggle="table" data-url="{{url('/hotspot/user')}}" data-pagination="true" data-height="450" data-search="true" data-show-toggle="true" data-show-columns="true" data-trim-on-search="false" data-show-refresh="true" class="table table-striped" data-toolbar="#toolbar">
				    <thead>
				        <tr>
							<th data-visible="false" data-sortable="true" data-field="numbers">#</th>
							<th data-formatter="df">Remove</th>
							<th data-formatter="edit">Edit</th>
							<th data-visible="true" data-sortable="true" data-field="disabled">disabled</th>
							<th data-visible="true" data-sortable="true" data-field="name">name</th>
							<th data-visible="false" data-sortable="true" data-field="password">password</th>
							<th data-visible="true" data-sortable="true" data-field="profile">profile</th>
							<th data-visible="true" data-sortable="true" data-field="server">server</th>
							<th data-visible="true" data-sortable="true" data-field="bytesIn">bytesIn</th>
	            			<th data-visible="true" data-sortable="true" data-field="bytesOut">bytesOut</th>
							<th data-visible="false" data-sortable="true" data-field="address">address</th>
							<th data-visible="true" data-sortable="true" data-field="comment">comment</th>
							<th data-visible="false" data-sortable="true" data-field="limitBytesIn">limitBytesIn</th>
							<th data-visible="false" data-sortable="true" data-field="limitBytesOut">limitBytesOut</th>
							<th data-visible="false" data-sortable="true" data-field="limitBytesTotal">limitBytesTotal</th>
							<th data-visible="false" data-sortable="true" data-field="limitUptime">limitUptime</th>
							<th data-visible="false" data-sortable="true" data-field="packetsIn">packetsIn</th>
							<th data-visible="false" data-sortable="true" data-field="packetsOut">packetsOut</th>
							<th data-visible="false" data-sortable="true" data-field="macAddress">macAddress</th>
							<th data-visible="false" data-sortable="true" data-field="routes">routes</th>
				        </tr>
				    </thead>
				    <tbody>				        
				    </tbody>
				</table>
                    
                </div>
            </div>
        </div>
    </div>
</div>
<script type="text/javascript">
	function df(value,row,index){
		return '<a title="Delete User Permanent" href="{{url('/user/remove')}}/'+row.numbers+'" class="btn btn-danger btn-sm"><i class="glyphicon glyphicon-remove"></i></a>';
	}
	function edit(value,row,index){
		return '<a title="Delete User Permanent" href="{{url('/user/')}}/'+row.numbers+'/edit" class="btn btn-default btn-sm"><i class="glyphicon glyphicon-edit"></i></a>';
	}
</script>
@endsection


File: /resources\views\auth\emails\password.blade.php
Click here to reset your password: <a href="{{ $link = url('password/reset', $token).'?email='.urlencode($user->getEmailForPasswordReset()) }}"> {{ $link }} </a>


File: /resources\views\auth\login.blade.php
@extends('layouts.app')

@section('content')
<div class="container">
    <div class="row">
        <div class="col-md-8 col-md-offset-2">
            <div class="panel panel-default">
                <div class="panel-heading">Login</div>
                <div class="panel-body">
                    <form class="form-horizontal" role="form" method="POST" action="{{ url('/login') }}">
                        {!! csrf_field() !!}

                        <div class="form-group{{ $errors->has('email') ? ' has-error' : '' }}">
                            <label class="col-md-4 control-label">E-Mail Address</label>

                            <div class="col-md-6">
                                <input type="email" class="form-control" name="email" value="{{ old('email') }}">

                                @if ($errors->has('email'))
                                    <span class="help-block">
                                        <strong>{{ $errors->first('email') }}</strong>
                                    </span>
                                @endif
                            </div>
                        </div>

                        <div class="form-group{{ $errors->has('password') ? ' has-error' : '' }}">
                            <label class="col-md-4 control-label">Password</label>

                            <div class="col-md-6">
                                <input type="password" class="form-control" name="password">

                                @if ($errors->has('password'))
                                    <span class="help-block">
                                        <strong>{{ $errors->first('password') }}</strong>
                                    </span>
                                @endif
                            </div>
                        </div>

                        <div class="form-group">
                            <div class="col-md-6 col-md-offset-4">
                                <div class="checkbox">
                                    <label>
                                        <input type="checkbox" name="remember"> Remember Me
                                    </label>
                                </div>
                            </div>
                        </div>

                        <div class="form-group">
                            <div class="col-md-6 col-md-offset-4">
                                <button type="submit" class="btn btn-primary">
                                    <i class="fa fa-btn fa-sign-in"></i>Login
                                </button>

                                <a class="btn btn-link" href="{{ url('/password/reset') }}">Forgot Your Password?</a>
                            </div>
                        </div>
                    </form>
                </div>
            </div>
        </div>
    </div>
</div>
@endsection


File: /resources\views\auth\passwords\email.blade.php
@extends('layouts.app')

<!-- Main Content -->
@section('content')
<div class="container">
    <div class="row">
        <div class="col-md-8 col-md-offset-2">
            <div class="panel panel-default">
                <div class="panel-heading">Reset Password</div>
                <div class="panel-body">
                    @if (session('status'))
                        <div class="alert alert-success">
                            {{ session('status') }}
                        </div>
                    @endif

                    <form class="form-horizontal" role="form" method="POST" action="{{ url('/password/email') }}">
                        {!! csrf_field() !!}

                        <div class="form-group{{ $errors->has('email') ? ' has-error' : '' }}">
                            <label class="col-md-4 control-label">E-Mail Address</label>

                            <div class="col-md-6">
                                <input type="email" class="form-control" name="email" value="{{ old('email') }}">

                                @if ($errors->has('email'))
                                    <span class="help-block">
                                        <strong>{{ $errors->first('email') }}</strong>
                                    </span>
                                @endif
                            </div>
                        </div>

                        <div class="form-group">
                            <div class="col-md-6 col-md-offset-4">
                                <button type="submit" class="btn btn-primary">
                                    <i class="fa fa-btn fa-envelope"></i>Send Password Reset Link
                                </button>
                            </div>
                        </div>
                    </form>
                </div>
            </div>
        </div>
    </div>
</div>
@endsection


File: /resources\views\auth\passwords\reset.blade.php
@extends('layouts.app')

@section('content')
<div class="container">
    <div class="row">
        <div class="col-md-8 col-md-offset-2">
            <div class="panel panel-default">
                <div class="panel-heading">Reset Password</div>

                <div class="panel-body">
                    <form class="form-horizontal" role="form" method="POST" action="{{ url('/password/reset') }}">
                        {!! csrf_field() !!}

                        <input type="hidden" name="token" value="{{ $token }}">

                        <div class="form-group{{ $errors->has('email') ? ' has-error' : '' }}">
                            <label class="col-md-4 control-label">E-Mail Address</label>

                            <div class="col-md-6">
                                <input type="email" class="form-control" name="email" value="{{ $email or old('email') }}">

                                @if ($errors->has('email'))
                                    <span class="help-block">
                                        <strong>{{ $errors->first('email') }}</strong>
                                    </span>
                                @endif
                            </div>
                        </div>

                        <div class="form-group{{ $errors->has('password') ? ' has-error' : '' }}">
                            <label class="col-md-4 control-label">Password</label>

                            <div class="col-md-6">
                                <input type="password" class="form-control" name="password">

                                @if ($errors->has('password'))
                                    <span class="help-block">
                                        <strong>{{ $errors->first('password') }}</strong>
                                    </span>
                                @endif
                            </div>
                        </div>

                        <div class="form-group{{ $errors->has('password_confirmation') ? ' has-error' : '' }}">
                            <label class="col-md-4 control-label">Confirm Password</label>
                            <div class="col-md-6">
                                <input type="password" class="form-control" name="password_confirmation">

                                @if ($errors->has('password_confirmation'))
                                    <span class="help-block">
                                        <strong>{{ $errors->first('password_confirmation') }}</strong>
                                    </span>
                                @endif
                            </div>
                        </div>

                        <div class="form-group">
                            <div class="col-md-6 col-md-offset-4">
                                <button type="submit" class="btn btn-primary">
                                    <i class="fa fa-btn fa-refresh"></i>Reset Password
                                </button>
                            </div>
                        </div>
                    </form>
                </div>
            </div>
        </div>
    </div>
</div>
@endsection


File: /resources\views\auth\register.blade.php
@extends('layouts.app')

@section('content')
<div class="container">
    <div class="row">
        <div class="col-md-8 col-md-offset-2">
            <div class="panel panel-default">
                <div class="panel-heading">Register</div>
                <div class="panel-body">
                    <form class="form-horizontal" role="form" method="POST" action="{{ url('/register') }}">
                        {!! csrf_field() !!}

                        <div class="form-group{{ $errors->has('name') ? ' has-error' : '' }}">
                            <label class="col-md-4 control-label">Name</label>

                            <div class="col-md-6">
                                <input type="text" class="form-control" name="name" value="{{ old('name') }}">

                                @if ($errors->has('name'))
                                    <span class="help-block">
                                        <strong>{{ $errors->first('name') }}</strong>
                                    </span>
                                @endif
                            </div>
                        </div>

                        <div class="form-group{{ $errors->has('email') ? ' has-error' : '' }}">
                            <label class="col-md-4 control-label">E-Mail Address</label>

                            <div class="col-md-6">
                                <input type="email" class="form-control" name="email" value="{{ old('email') }}">

                                @if ($errors->has('email'))
                                    <span class="help-block">
                                        <strong>{{ $errors->first('email') }}</strong>
                                    </span>
                                @endif
                            </div>
                        </div>

                        <div class="form-group{{ $errors->has('password') ? ' has-error' : '' }}">
                            <label class="col-md-4 control-label">Password</label>

                            <div class="col-md-6">
                                <input type="password" class="form-control" name="password">

                                @if ($errors->has('password'))
                                    <span class="help-block">
                                        <strong>{{ $errors->first('password') }}</strong>
                                    </span>
                                @endif
                            </div>
                        </div>

                        <div class="form-group{{ $errors->has('password_confirmation') ? ' has-error' : '' }}">
                            <label class="col-md-4 control-label">Confirm Password</label>

                            <div class="col-md-6">
                                <input type="password" class="form-control" name="password_confirmation">

                                @if ($errors->has('password_confirmation'))
                                    <span class="help-block">
                                        <strong>{{ $errors->first('password_confirmation') }}</strong>
                                    </span>
                                @endif
                            </div>
                        </div>

                        <div class="form-group">
                            <div class="col-md-6 col-md-offset-4">
                                <button type="submit" class="btn btn-primary">
                                    <i class="fa fa-btn fa-user"></i>Register
                                </button>
                            </div>
                        </div>
                    </form>
                </div>
            </div>
        </div>
    </div>
</div>
@endsection


File: /resources\views\errors\503.blade.php
<!DOCTYPE html>
<html>
    <head>
        <title>Be right back.</title>

        <link href="https://fonts.googleapis.com/css?family=Lato:100" rel="stylesheet" type="text/css">

        <style>
            html, body {
                height: 100%;
            }

            body {
                margin: 0;
                padding: 0;
                width: 100%;
                color: #B0BEC5;
                display: table;
                font-weight: 100;
                font-family: 'Lato';
            }

            .container {
                text-align: center;
                display: table-cell;
                vertical-align: middle;
            }

            .content {
                text-align: center;
                display: inline-block;
            }

            .title {
                font-size: 72px;
                margin-bottom: 40px;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <div class="content">
                <div class="title">Be right back.</div>
            </div>
        </div>
    </body>
</html>


File: /resources\views\flash.blade.php
<?php

/* 
 * Cocomas 
 * 
 * Copyright 2014
 * 
 * Developed by Mashary
 */

?>
{{-- @if($errors) --}}
	{{-- @foreach ($errors->all() as $message) --}}
	{{-- <div class="alert alert-danger alert-dismissible" role="alert"> --}}
		{{-- <button type="button" class="close" data-dismiss="alert" aria-label="Close"><span aria-hidden="true">&times;</span></button> --}}
		{{-- <strong>{{trans('cocomas.error')}}!</strong> {{ $message }} --}}
	{{-- </div> --}}
	{{-- @endforeach --}}
{{-- @endif --}}

@if (\Session::has('message'))
<div class="alert alert-success alert-dismissible" role="alert">
	<button type="button" class="close" data-dismiss="alert" aria-label="Close"><span aria-hidden="true">&times;</span></button>
	<strong>{{trans('cocomas.success')}}!</strong> {{ session('message') }}
</div>
@endif

@if (\Session::has('message-error'))
<div class="alert alert-danger alert-dismissible" role="alert">
	<button type="button" class="close" data-dismiss="alert" aria-label="Close"><span aria-hidden="true">&times;</span></button>
	<strong>{{trans('cocomas.error')}}!</strong> {{ session('message-error') }}
</div>
@endif

File: /resources\views\home.blade.php
@extends('layouts.app')
@section('content')
<div class="container-fluid">
    <div class="row">        
        @include('sidemenu')
        <div class="col-md-10 col-sm-10 col-xs-10">
            <div class="panel panel-default">
                <div class="panel-heading"><strong>Home</strong></div>
                <div class="panel-body">
                    Welcome back Dude!!!
                </div>
            </div>
        </div>
    </div>
</div>
@endsection


File: /resources\views\layouts\app.blade.php
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="shortcut icon" type="image/png" href="/favicon.png"/>
    <link href="/favicon.png" rel="apple-touch-icon">
    <link href="/favicon.png" rel="apple-touch-icon" sizes="76x76">
    <link href="/favicon.png" rel="apple-touch-icon" sizes="120x120">
    <link href="/favicon.png" rel="apple-touch-icon" sizes="152x152">
    <link href="/favicon.png" rel="apple-touch-icon" sizes="180x180">
    <link href="/favicon.png" rel="icon" sizes="192x192">
    <link href="/favicon.png" rel="icon" sizes="128x128">    
    <title>Open Hotspot Manager for Mikrotik</title>

    <!-- Fonts -->
    <!-- <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.4.0/css/font-awesome.min.css" rel='stylesheet' type='text/css'>
    <link href="https://fonts.googleapis.com/css?family=Lato:100,300,400,700" rel='stylesheet' type='text/css'> -->

    <!-- Latest compiled and minified CSS -->
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/css/bootstrap.min.css" integrity="sha384-1q8mTJOASx8j1Au+a5WDVnPi2lkFfwwEAa8hDDdjZlpLegxhjVME1fgjWPGmkzs7" crossorigin="anonymous">

    <!-- Optional theme -->
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/css/bootstrap-theme.min.css" integrity="sha384-fLW2N01lMqjakBkx3l/M9EahuwpSfeNvV63J5ezn3uZzapT0u7EYsXMjQV+0En5r" crossorigin="anonymous">
    <!-- Latest compiled and minified CSS -->
    <link rel="stylesheet" href="//cdnjs.cloudflare.com/ajax/libs/bootstrap-table/1.10.1/bootstrap-table.min.css">

    {{-- <link href="{{ elixir('css/app.css') }}" rel="stylesheet"> --}}
</head>
<body id="app-layout">
    <nav class="navbar navbar-default navbar-static-top">
        <div class="container">
            <div class="navbar-header">

                <!-- Collapsed Hamburger -->
                <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#app-navbar-collapse">
                    <span class="sr-only">Toggle Navigation</span>
                    <span class="icon-bar"></span>
                    <span class="icon-bar"></span>
                    <span class="icon-bar"></span>
                </button>

                <!-- Branding Image -->
                <a class="navbar-brand" href="{{ url('/') }}">
                    Open Hotspot Manger for Mikrotik
                </a>
            </div>

            <div class="collapse navbar-collapse" id="app-navbar-collapse">
                <!-- Left Side Of Navbar -->
                <ul class="nav navbar-nav">
                    @if (!Auth::guest())
                        <li><a href="{{ url('/home') }}">Home</a></li>                        
                        <li><a href="{{ url('/user/register') }}">Register</a></li>
                    @endif                                        
                </ul>
                <!-- Right Side Of Navbar -->
                <ul class="nav navbar-nav navbar-right">
                    <!-- Authentication Links -->
                    @if (Auth::guest())
                        <li><a href="{{ url('/login') }}">Login</a></li>                        
                    @else
                        <li class="dropdown">
                            <a href="#" class="dropdown-toggle" data-toggle="dropdown" role="button" aria-expanded="false">
                                <strong>{{ Auth::user()->name }}</strong> <span class="caret"></span>
                            </a>

                            <ul class="dropdown-menu" role="menu">
                                <li><a href="{{ url('/u/profile') }}"><i class="fa fa-btn fa-sign-out"></i>Profile</a></li>
                                <li><a href="{{ url('/logout') }}"><i class="fa fa-btn fa-sign-out"></i>Logout</a></li>
                            </ul>
                        </li>
                    @endif
                </ul>
            </div>
        </div>
    </nav>
    
    @yield('content')
    <div class="row">
        <div class="col-md-12 text-center">
            Open Hotspot Manager &copy; 2016
        </div>
    </div>
    
    <!-- JavaScripts -->
    <script src="http://code.jquery.com/jquery-1.12.3.min.js" integrity="sha256-aaODHAgvwQW1bFOGXMeX+pC4PZIPsvn2h1sArYOhgXQ=" crossorigin="anonymous"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/js/bootstrap.min.js"></script>    
    <script src="//cdnjs.cloudflare.com/ajax/libs/bootstrap-table/1.10.1/bootstrap-table.min.js"></script>
    {{-- <script src="{{ elixir('js/app.js') }}"></script> --}}
</body>
</html>


File: /resources\views\main-page.blade.php
@extends('layouts.app')
@section('content')
<div class="container-fluid">
    <div class="row">
        <div class="col-md-10 col-md-offset-1">            
            <div class="panel panel-default">
                <div class="panel-heading"><strong>Hotspot Management</strong></div>
                <div class="panel-body">
                    <ul>
                        <li><strong>User Management</strong>
                        </li>
                        <li><strong>IP Binding</strong></li>
                    </ul>
                </div>
            </div>
        </div>
    </div>    
</div>
@endsection


File: /resources\views\router\mikrotik\edit.blade.php
@extends('layouts.app')
@section('content')
<div class="container-fluid">
    <div class="row">        
        @include('sidemenu')
        <div class="col-md-10 col-sm-10 col-xs-10">
        @include('flash')
        <form method="post">
        	<input type="hidden" name="_token" value="{!! csrf_token() !!}">        
            <div class="panel panel-default">
                <div class="panel-heading">Edit</div>
                <div class="panel-body">
	                <div class="row">
	                	<div class="col-md-10">	                		
	                		<div class="form-group">
	                			<label for="name">Name</label>
	                			<input name="name" autocomplete="off" type="text" required class="form-control" id="name" value="{{old('name',$data->name)}}">
	                		</div>
	                		<div class="form-group">
	                			<label for="user">User</label>
	                			<input name="user" autocomplete="off" type="text" required class="form-control" id="user" value="{{old('user',$data->user)}}">
	                		</div>
	                		<div class="form-group">
	                			<label for="pass">Password</label>
	                			<input autocomplete="off"  name="pass" type="password" class="form-control" id="pass" value="{{old('pass')}}">
	                		</div>
	                		<div class="form-group">
	                			<label for="ipaddress">Ipaddress</label>
	                			<input name="ipaddress" type="text" class="form-control" id="ipaddress" value="{{old('ipaddress',$data->ipaddress)}}">
	                		</div>
	                		<div class="form-group">
	                			<label for="port">Port</label>
	                			<input name="port" type="text" class="form-control" id="port" value="{{old('port',$data->port)}}">
	                		</div>
	                		<div class="form-group">
	                			<label for="is_active">is_active</label>
	                			<input name="is_active" type="text" class="form-control" id="is_active" value="{{old('is_active',$data->is_active)}}">
	                		</div>	                		
	                	</div>
	                </div>
                </div>
                <div class="panel-footer">                	
                	<a href="{{url('/user')}}" class="btn btn-default"><i class="gylphicon glyphicon-back"></i> Back</a>
	                <button type="submit" class="btn btn-primary">Save</button>	                
                </div>
            </div>
    	</form>	
        </div>
    </div>
</div>
@endsection


File: /resources\views\sidemenu.blade.php
<div class="col-md-2 col-sm-2 hidden-xs">
    <div class="list-group">
    	<div class="list-group-item"><strong>Hotspot</strong></div>    	
        <a href="{{url('/user')}}" title="User" class="list-group-item {{(url('/user')==url()->current())?'active':''}}"><i class="glyphicon glyphicon-user"></i> User</a>
        <a href="{{url('/user/active')}}" title="Active" class="list-group-item {{(url('/user/active')==url()->current())?'active':''}}"><i class="glyphicon glyphicon-globe"></i> Active</a>
        <a href="{{url('/binding')}}" title="Binding" class="list-group-item {{(url('/binding')==url()->current())?'active':''}}"><i class="glyphicon glyphicon-phone"></i> Binding</a>        
    </div>  
    <div class="list-group">
    	<div class="list-group-item"><strong>Router</strong></div>
        <a href="{{url('/router')}}" title="Mirktoik Router" class="list-group-item {{(url('/router')==url()->current())?'active':''}}"><i class="glyphicon glyphicon-cog"></i> Mikrotik</a>
    </div>          
</div>        
<div class="col-xs-2 hidden-sm hidden-md hidden-lg">
    <div class="list-group">        
        <a href="{{url('/user')}}" title="User" class="list-group-item {{(url('/user')==url()->current())?'active':''}}"><i class="glyphicon glyphicon-user"></i></a>
        <a href="{{url('/user/active')}}" title="Active" class="list-group-item {{(url('/user/active')==url()->current())?'active':''}}"><i class="glyphicon glyphicon-globe"></i></a>
        <a href="{{url('/binding')}}" title="Binding" class="list-group-item {{(url('/binding')==url()->current())?'active':''}}"><i class="glyphicon glyphicon-phone"></i></a>
    </div>  
    <div class="list-group">        
        <a href="{{url('/router')}}" title="Mirktoik Router" class="list-group-item {{(url('/router')==url()->current())?'active':''}}"><i class="glyphicon glyphicon-cog"></i></a>
    </div>          
</div>        

File: /resources\views\user\create.blade.php
@extends('layouts.app')
@section('content')
<div class="container-fluid">
    <div class="row">        
        @include('sidemenu')
        <div class="col-md-10 col-sm-10 col-xs-10">
        @include('flash')        
        <form method="post">
        	<input type="hidden" name="_token" value="{!! csrf_token() !!}">        
            <div class="panel panel-default">
                <div class="panel-heading"><strong>Register User</strong></div>
                <div class="panel-body">
	                <div class="row">
	                	<div class="col-md-10">
	                		<div class="form-group">
	                			<label for="name">Name</label>
	                			<input name="name" autocomplete="off" type="text" required class="form-control" id="name" value="{{old('name')}}">
	                		</div>
	                		<div class="form-group">
	                			<label for="password">Password</label>
	                			<input name="password" required type="password" class="form-control" id="password" value="{{old('password')}}" placeholder="">
	                		</div>
	                		<div class="form-group">
	                			<label for="email">Email</label>
	                			<input name="email" type="text" class="form-control" id="email" value="{{old('email')}}">
	                		</div>	                		
	                	</div>
	                </div>
                </div>
                <div class="panel-footer">                	
	                <button type="submit" class="btn btn-default">Save</button>	                
                </div>
            </div>
    	</form>	
        </div>
    </div>
</div>
@endsection


File: /resources\views\user\profile.blade.php
@extends('layouts.app')
@section('content')
<div class="container-fluid">
    <div class="row">        
        @include('sidemenu')
        <div class="col-md-10 col-sm-10 col-xs-10">
        @include('flash')        
        <form method="post">
        	<input type="hidden" name="_token" value="{!! csrf_token() !!}">        
            <div class="panel panel-default">
                <div class="panel-heading"><strong>Profile</strong></div>
                <div class="panel-body">
	                <div class="row">
	                	<div class="col-md-10">	                		
	                		<div class="form-group">
	                			<label for="name">Name</label>
	                			<input name="name" autocomplete="off" type="text" required class="form-control" id="name" value="{{old('name',$data->name)}}">
	                		</div>
	                		<div class="form-group">
	                			<label for="password">Password</label>
	                			<input name="password" type="password" class="form-control" id="password" value="{{old('password')}}" placeholder="Change Password">
	                		</div>	                		
	                		<div class="form-group">
	                			<label for="email">Email</label>
	                			<input name="email" type="text" class="form-control" id="email" value="{{old('email',$data->email)}}">
	                		</div>	                		
	                	</div>
	                </div>
                </div>
                <div class="panel-footer">                	
	                <button type="submit" class="btn btn-default">Save</button>	                
                </div>
            </div>
    	</form>	
        </div>
    </div>
</div>
@endsection


File: /resources\views\vendor\.gitkeep



File: /resources\views\welcome.blade.php
@extends('layouts.app')

@section('content')
<div class="container">
    <div class="row">
        <div class="col-md-10 col-md-offset-1">
            <div class="panel panel-default">
                <div class="panel-heading">Welcome</div>

                <div class="panel-body">
                    Your Application's Landing Page.
                </div>
            </div>
        </div>
    </div>
</div>
@endsection


File: /server.php
<?php

/**
 * Laravel - A PHP Framework For Web Artisans
 *
 * @package  Laravel
 * @author   Taylor Otwell <taylorotwell@gmail.com>
 */

$uri = urldecode(
    parse_url($_SERVER['REQUEST_URI'], PHP_URL_PATH)
);

// This file allows us to emulate Apache's "mod_rewrite" functionality from the
// built-in PHP web server. This provides a convenient way to test a Laravel
// application without having installed a "real" web server software here.
if ($uri !== '/' && file_exists(__DIR__.'/public'.$uri)) {
    return false;
}

require_once __DIR__.'/public/index.php';


File: /storage\app\.gitignore
*
!public/
!.gitignore


File: /storage\app\public\.gitignore
*
!.gitignore


File: /storage\framework\.gitignore
config.php
routes.php
schedule-*
compiled.php
services.json
events.scanned.php
routes.scanned.php
down


File: /storage\framework\cache\.gitignore
*
!.gitignore


File: /storage\framework\sessions\.gitignore
*
!.gitignore


File: /storage\framework\views\.gitignore
*
!.gitignore


File: /storage\logs\.gitignore
*
!.gitignore


File: /tests\ExampleTest.php
<?php

use Illuminate\Foundation\Testing\WithoutMiddleware;
use Illuminate\Foundation\Testing\DatabaseMigrations;
use Illuminate\Foundation\Testing\DatabaseTransactions;

class ExampleTest extends TestCase
{
    /**
     * A basic functional test example.
     *
     * @return void
     */
    public function testBasicExample()
    {
        $this->visit('/')
             ->see('Laravel 5');
    }
}


File: /tests\TestCase.php
<?php

class TestCase extends Illuminate\Foundation\Testing\TestCase
{
    /**
     * The base URL to use while testing the application.
     *
     * @var string
     */
    protected $baseUrl = 'http://localhost';

    /**
     * Creates the application.
     *
     * @return \Illuminate\Foundation\Application
     */
    public function createApplication()
    {
        $app = require __DIR__.'/../bootstrap/app.php';

        $app->make(Illuminate\Contracts\Console\Kernel::class)->bootstrap();

        return $app;
    }
}


